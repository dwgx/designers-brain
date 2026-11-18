#!/usr/bin/env python3
"""Encode exactly 300 valid 1080p PNGs as H.264; publish only after full decode."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from verify_all import EnvironmentError_, VerificationError, ffmpeg_binary, measure_media, need, sha256


def inspect_frames(directory):
    try:
        from PIL import Image
    except ImportError as e:
        raise EnvironmentError_('Pillow is required to inspect input PNG pixels') from e
    directory = Path(directory)
    need(directory.is_dir(), 'Frame directory missing')
    files = sorted(directory.glob('*.png'))
    expected = [{('f_%04d.png' if underscore else 'f%04d.png') % n for n in range(300)}
                for underscore in (False, True)]
    names = {p.name for p in files}
    need(len(files) == 300 and names in expected, 'Exactly f0000..f0299.png or f_0000..f_0299.png required; no missing/extra/mixed files')
    pattern = 'f_%04d.png' if names == expected[1] else 'f%04d.png'
    hashes = {}
    for index in range(300):
        path = directory / (pattern % index)
        try:
            with Image.open(path) as im:
                im.load()
                need(im.format == 'PNG' and im.size == (1920, 1080) and im.mode in ('RGB', 'RGBA', 'P', 'L', 'LA'),
                     'Invalid PNG dimensions/mode: ' + path.name)
        except (OSError, ValueError) as e:
            raise VerificationError('Unreadable input PNG: ' + path.name) from e
        hashes[str(index)] = sha256(path)
    return pattern, hashes


def encode(directory, output, ffmpeg=None):
    output = Path(output)
    need(output.suffix.lower() == '.mp4', 'Output must be an .mp4 file')
    need(not output.exists(), 'Output already exists; choose a new destination')
    pattern, hashes = inspect_frames(directory)
    exe = ffmpeg_binary(ffmpeg)
    output.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix='.' + output.stem + '-', suffix='.mp4', dir=output.parent)
    os.close(descriptor); Path(temporary).unlink()
    argv = [exe, '-hide_banner', '-nostdin', '-v', 'error', '-n', '-framerate', '30', '-start_number', '0',
            '-i', str(Path(directory) / pattern), '-frames:v', '300', '-an', '-c:v', 'libx264',
            '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', temporary]
    try:
        result = subprocess.run(argv, capture_output=True, timeout=600)
        need(result.returncode == 0, 'FFmpeg encoder failed; no final output published')
        measurement = measure_media(temporary, exe, require_faststart=True)
        need(not output.exists(), 'Output appeared while encoding; refusing to replace it')
        # link is exclusive, unlike rename on POSIX. Both paths are on the same filesystem.
        try:
            os.link(temporary, output)
        except FileExistsError as e:
            raise VerificationError('Output appeared while encoding; refusing to replace it') from e
        Path(temporary).unlink()
    except (OSError, subprocess.TimeoutExpired) as e:
        raise EnvironmentError_('Encoding could not complete; no final output published') from e
    finally:
        Path(temporary).unlink(missing_ok=True)
    return {'schema': 'motion-encode@2.0.0', 'ok': True, 'file': output.name,
            'sha256': sha256(output), 'bytes': output.stat().st_size, 'input_png_sha256': hashes,
            'parameters': {'encoder': 'libx264', 'crf': 18, 'preset': 'medium', 'faststart': True,
                           'fps': 30, 'frames': 300, 'pattern': pattern}, 'measured': measurement,
            'encoder_stdout_sha256': hashlib.sha256(result.stdout).hexdigest(),
            'encoder_stderr_sha256': hashlib.sha256(result.stderr).hexdigest()}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--frames', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--ffmpeg')
    p.add_argument('--receipt', type=Path)
    args = p.parse_args()
    try:
        receipt = encode(args.frames, args.output, args.ffmpeg); code = 0
    except EnvironmentError_ as e:
        receipt = {'ok': False, 'failure': 'environment', 'reason': str(e)}; code = 2
    except (VerificationError, OSError, ValueError) as e:
        receipt = {'ok': False, 'failure': 'verification', 'reason': str(e)}; code = 1
    text = json.dumps(receipt, ensure_ascii=False, indent=2) + '\n'
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True); args.receipt.write_bytes(text.encode('utf-8'))
    print(text, end=''); return code


if __name__ == '__main__':
    sys.exit(main())
