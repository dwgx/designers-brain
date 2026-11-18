#!/usr/bin/env python3
"""Verify the pinned public release, including every decoded frame. Never renders."""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
from html.parser import HTMLParser
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import struct
import subprocess
import sys

IDS = ('02', '03', '04', '05', '06', '07', '09', '10', '12', '13', '14', '15')
NATIVE = ('03', '04', '05', '06', '07', '09', '14')
JS_NATIVE = ('04', '05', '06', '07', '09')
PINS_SHA256 = '08197a51b14034ec1544b8943f3273c97ca86ea32d27f28484f72038e94db627'
SHA = re.compile(r'^[0-9a-f]{64}$')
SPEC = {'resolution': [1920, 1080], 'fps': 30, 'frames': 300,
        'duration_sec': 10, 'codec': 'h264', 'pixel_format': 'yuv420p'}
REJECTED_BROWSER_SHA256 = '178a37b3c9fe44ff13528da63f1a7f5ab8f24dbfcbda9534a2928c3c99ac40d3'


class VerificationError(Exception):
    pass


class EnvironmentError_(Exception):
    pass


def need(condition, message):
    if not condition:
        raise VerificationError(message)


def sha256(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding='utf-8-sig'))
    except (OSError, ValueError) as e:
        raise VerificationError('Cannot read JSON: ' + Path(path).name) from e


def canonical_file(root, rel):
    need(isinstance(rel, str) and '\\' not in rel and ':' not in rel,
         'Invalid relative file path')
    p = PurePosixPath(rel)
    need(not p.is_absolute() and '..' not in p.parts and str(p) == rel,
         'Non-canonical relative file path: ' + rel)
    path = Path(root) / p
    need(path.is_file(), 'Missing file: ' + rel)
    need(path.resolve().is_relative_to(Path(root).resolve()), 'Escaping path: ' + rel)
    return path


def bound_file(root, rel, expected):
    need(isinstance(expected, str) and SHA.fullmatch(expected), 'Missing/invalid SHA: ' + str(rel))
    path = canonical_file(root, rel)
    need(sha256(path) == expected, 'SHA mismatch: ' + rel)
    return path


def finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def validate_font(font, pins, card):
    need(isinstance(font, dict), card + ': missing font receipt')
    need(font.get('font_sha256') == pins['render_font_sha256'], card + ': wrong font SHA')
    name = font.get('file_name')
    need(isinstance(name, str) and name and '/' not in name and '\\' not in name,
         card + ': font filename must be public and relative')
    need(font.get('missing_glyphs') == [] and font.get('fallback_used') is False,
         card + ': font missing-glyph/fallback evidence failed')
    need(font.get('face_index') == 0, card + ': unexpected font face')
    if card in JS_NATIVE:
        need(font.get('helper_sha256') == pins['helpers']['sources/cjk_text.py'], card + ': font helper mismatch')
        need(font.get('js_helper_sha256') == pins['helpers']['sources/cjk_text.js'], card + ': JS font helper mismatch')


def validate_run(run, pins, card):
    need(run.get('schema') == 'motion-public-run@2.0.0', card + ': invalid RUN schema')
    need(run.get('case') == 'MOTION-' + card and run.get('status') == 'passed', card + ': RUN incomplete')
    need(run.get('raw_run_sha256') == pins['raw_run_sha256'][card], card + ': raw RUN provenance mismatch')
    pin = pins['cards'][card]
    need(run.get('source_sha256') == pin['renderer_source_sha256'], card + ': RUN source mismatch')
    commands = run.get('commands', [])
    need(len(commands) == 4 and all(x.get('exit') == 0 for x in commands), card + ': unsuccessful RUN commands')
    need([x.get('role') for x in commands] == ['render', 'fresh_process', 'encode', 'full_decode'], card + ': RUN roles missing')
    for command in commands:
        for field in ('stdout_sha256', 'stderr_sha256'):
            need(isinstance(command.get(field), str) and SHA.fullmatch(command[field]), card + ': RUN log SHA missing')
    png = run.get('png', {})
    need(png.get('decoded_frames') == 300 and png.get('resolution') == [1920, 1080], card + ': PNG count/dimensions')
    ledger = png.get('sha256', {})
    need(set(ledger) == {str(n) for n in range(300)} and
         all(isinstance(x, str) and SHA.fullmatch(x) for x in ledger.values()), card + ': incomplete PNG ledger')
    need(run.get('fresh_process_same_png_sha_at') == [299, 120, 0], card + ': fresh-process evidence missing')
    video = run.get('video', {})
    expected = {'sha256': pin['output_sha256'], 'bytes': pin['size_bytes'], 'codec': 'h264',
                'pixel_format': 'yuv420p', 'fps': 30, 'duration_seconds': 10,
                'decoded_frames': 300, 'resolution': [1920, 1080]}
    for key, value in expected.items():
        need(video.get(key) == value, card + ': RUN video ' + key + ' mismatch')
    hashes = video.get('all_decoded_frame_sha256', [])
    need(len(hashes) == 300 and all(isinstance(x, str) and SHA.fullmatch(x) for x in hashes),
         card + ': incomplete historical decoded-frame ledger')
    validate_font(run.get('font_dependency'), pins, card)
    if card in JS_NATIVE:
        need(run.get('auxiliary_sources') == {Path(k).name: v for k, v in pins['helpers'].items()},
             card + ': RUN helper source mismatch')


def validate_browser(browser, pins):
    """Checks measurements, never trusts top-level/row passed booleans."""
    need(browser.get('schema') == 'motion-browser-strict@2.0.0', 'Strict browser receipt required')
    rows = browser.get('videos', [])
    need(len(rows) == 12 and {r.get('card') for r in rows} == set(IDS), 'Browser denominator must be exactly 12')
    need(browser.get('raw_receipt_sha256') == pins['raw_browser_sha256'], 'Browser original receipt SHA mismatch')
    need(browser.get('probe_source_sha256') == pins['browser_probe_source_sha256'], 'Browser probe source SHA mismatch')
    requests = browser.get('http_requests', [])
    need({r.get('card') for r in requests if r.get('status') == 206} == set(IDS), 'Browser HTTP 206 evidence missing for a card')
    for request in requests:
        card = request.get('card')
        need(card in pins['cards'] and request.get('size') == pins['cards'][card]['size_bytes'], 'Browser HTTP media size mismatch')
    for row in rows:
        card = row['card']; prefix = card + ': browser '
        need(row.get('mp4_sha256') == pins['cards'][card]['output_sha256'], prefix + 'media SHA mismatch')
        load = row.get('load', {})
        need(load.get('width') == 1920 and load.get('height') == 1080, prefix + 'dimensions')
        need(finite(load.get('duration')) and abs(load['duration'] - 10) <= .05 and load.get('readyState', 0) >= 2,
             prefix + 'load duration/readiness')
        seeks = row.get('seeks', [])
        expected = (.5, 4, 233 / 30, 299 / 30)
        need(len(seeks) == 4, prefix + 'four seeks required')
        thumbnails = []
        for seek, requested in zip(seeks, expected):
            need(finite(seek.get('requested')) and abs(seek['requested'] - requested) < .001,
                 prefix + 'seek target changed')
            need(finite(seek.get('observed')) and abs(seek['observed'] - requested) <= .12,
                 prefix + 'seek did not reach requested time')
            need(seek.get('seeking') is False and seek.get('readyState', 0) >= 2, prefix + 'seek unsettled')
            digest = seek.get('thumbnail_sha256')
            need(isinstance(digest, str) and SHA.fullmatch(digest), prefix + 'drawn video thumbnail missing')
            thumbnails.append(digest)
        need(len(set(thumbnails)) >= 2, prefix + 'drawn frames did not change')
        playback = row.get('playback', {})
        need(finite(playback.get('start')) and finite(playback.get('end')) and
             playback['end'] - playback['start'] >= .2, prefix + 'playhead did not advance')
    return {'cards': 12, 'scope': 'Recorded Chrome load, measured seeks/canvas, real playhead advance; no new browser session'}


def browser_from_raw(raw, raw_sha):
    rows = []
    for row in raw.get('videos', []):
        item = {k: row[k] for k in ('card', 'mp4_sha256', 'utc', 'load', 'playback', 'canPlayH264') if k in row}
        item['seeks'] = []
        for seek in row.get('seeks', []):
            point = {k: seek[k] for k in ('requested', 'observed', 'readyState', 'seeking') if k in seek}
            point['thumbnail_sha256'] = seek.get('frame_signature_32x18')
            item['seeks'].append(point)
        rows.append(item)
    return {'schema': 'motion-browser-strict@2.0.0', 'raw_receipt_sha256': raw_sha,
            'probe_source_sha256': raw.get('probe_source_sha256'), 'http_requests': raw.get('http_requests'),
            'browser': raw.get('browser'), 'videos': rows,
            'scope': 'Recorded actual Chrome load, measured seeks with SHA-256 of drawn 32x18 RGBA pixels, HTTP 206 and playhead advance. No human aesthetic or audio claim.'}


def ffmpeg_binary(value=None):
    value = value or os.environ.get('FFMPEG', 'ffmpeg')
    found = shutil.which(value)
    if found is None and Path(value).is_file():
        found = str(Path(value).resolve())
    if not found:
        raise EnvironmentError_('FFmpeg executable not found; use --ffmpeg or FFMPEG')
    return found


def mp4_atoms(path):
    atoms = []
    length = Path(path).stat().st_size
    with Path(path).open('rb') as f:
        position = 0
        while position < length:
            f.seek(position); header = f.read(8)
            need(len(header) == 8, 'Truncated MP4 atom header')
            size, name = struct.unpack('>I4s', header); header_len = 8
            if size == 1:
                large = f.read(8); need(len(large) == 8, 'Truncated MP4 extended atom')
                size = struct.unpack('>Q', large)[0]; header_len = 16
            elif size == 0:
                size = length - position
            need(size >= header_len and position + size <= length, 'Truncated/invalid MP4 atom')
            atoms.append((name.decode('ascii', errors='replace'), position)); position += size
    names = [x[0] for x in atoms]
    need('moov' in names and 'mdat' in names, 'MP4 moov/mdat missing')
    return {'faststart': names.index('moov') < names.index('mdat'), 'atoms': names}


def measure_media(path, ffmpeg=None, require_faststart=False):
    """Read the original stream to EOF without fps/scale conversion (FFmpeg only)."""
    path = Path(path)
    need(path.is_file(), 'Media missing: ' + path.name)
    container = mp4_atoms(path)
    need(not require_faststart or container['faststart'], 'New media must have moov before mdat')
    exe = ffmpeg_binary(ffmpeg)
    argv = [exe, '-hide_banner', '-nostdin', '-loglevel', 'info', '-xerror', '-err_detect', 'explode',
            '-i', str(path), '-map', '0:v:0', '-an', '-sn', '-dn', '-vf', 'showinfo',
            '-fps_mode', 'passthrough', '-f', 'framemd5', '-']
    try:
        result = subprocess.run(argv, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=180)
    except (OSError, subprocess.TimeoutExpired) as e:
        raise EnvironmentError_('FFmpeg could not finish full decode: ' + path.name) from e
    need(result.returncode == 0, 'FFmpeg failed full decode: ' + path.name)
    before_output = re.split(r'Stream mapping:|Output #', result.stderr, maxsplit=1)[0]
    streams = re.findall(r'Stream #0:[^\n]*Video:[^\n]*', before_output)
    need(len(streams) == 1, 'Exactly one input video stream required: ' + path.name)
    stream = streams[0]
    need(re.search(r'Video:\s*h264\b', stream) and re.search(r'\bavc1\b', stream), 'Input codec must be H.264/avc1: ' + path.name)
    need(re.search(r'\byuv420p\b', stream), 'Input pixel format must be yuv420p: ' + path.name)
    frames = re.findall(r'\bn:\s*(\d+)\s+pts:\s*(-?\d+)\s+pts_time:\S+.*?\bfmt:(\S+).*?\bs:(\d+)x(\d+)\b', result.stderr)
    need(len(frames) == 300, 'Full decoded frame count is ' + str(len(frames)) + ', expected 300: ' + path.name)
    need([int(x[0]) for x in frames] == list(range(300)), 'Decoded frame sequence incomplete: ' + path.name)
    need(all(x[2:] == ('yuv420p', '1920', '1080') for x in frames), 'A decoded frame has wrong dimensions/pixel format: ' + path.name)
    input_tb_match = re.search(r'config in time_base:\s*(\d+)/(\d+)', result.stderr)
    need(input_tb_match is not None, 'Decoded input time base missing: ' + path.name)
    input_tb = Fraction(int(input_tb_match[1]), int(input_tb_match[2]))
    need(all(int(frame[1]) * input_tb == Fraction(index, 30) for index, frame in enumerate(frames)),
         'Original decoded timestamps are not exactly 30 fps from time zero: ' + path.name)
    tb_match = re.search(r'^#tb 0:\s*(\d+)/(\d+)\s*$', result.stdout, re.M)
    need(tb_match is not None, 'Frame time base missing: ' + path.name)
    tb = Fraction(int(tb_match[1]), int(tb_match[2]))
    rows = []
    for line in result.stdout.splitlines():
        if not line or line.startswith('#'):
            continue
        parts = [s.strip() for s in line.split(',')]
        need(len(parts) == 6 and re.fullmatch(r'[0-9a-f]{32}', parts[5]), 'Invalid decoded frame checksum row')
        try:
            values = [int(x) for x in parts[:5]]
        except ValueError as e:
            raise VerificationError('Invalid decoded frame timestamps') from e
        rows.append((*values, parts[5]))
    need(len(rows) == 300, 'Frame checksum denominator is not 300: ' + path.name)
    for index, (stream_id, dts, pts, duration, size, _) in enumerate(rows):
        need(stream_id == 0 and pts * tb == Fraction(index, 30) and duration * tb == Fraction(1, 30),
             'Decoded timing is not 300 constant-rate frames at 30 fps: ' + path.name)
        need(size == 1920 * 1080 * 3 // 2, 'Decoded raw frame size differs: ' + path.name)
    checksums = [row[-1] for row in rows]
    need(len(set(checksums)) >= 2, 'Media is a repeated still image: ' + path.name)
    return {'decoded_frames': 300, 'resolution': [1920, 1080], 'fps': 30, 'duration_sec': 10,
            'codec': 'h264', 'codec_tag': 'avc1', 'pixel_format': 'yuv420p', 'faststart': container['faststart'],
            'distinct_decoded_frames': len(set(checksums)),
            'decoded_frame_md5_ledger_sha256': hashlib.sha256(('\n'.join(checksums) + '\n').encode()).hexdigest(),
            'decode': 'FFmpeg to EOF, showinfo per-frame dimensions and framemd5 per-frame PTS/duration'}


class GalleryParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.sources = []; self.controls = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'video':
            if 'controls' in attrs:
                self.controls += 1
            if 'src' in attrs:
                self.sources.append(attrs['src'])
        elif tag == 'source':
            self.sources.append(attrs.get('src'))


def validate_package(root):
    root = Path(root)
    pins = read_json(bound_file(root, 'release-pins.json', PINS_SHA256))
    bound_file(root, 'history/rejected-weak-browser/BROWSER.json', REJECTED_BROWSER_SHA256)
    need(set(pins['cards']) == set(IDS), 'Release pins denominator')
    manifest = read_json(canonical_file(root, 'manifest.json'))
    need(manifest.get('schema') == 'motion-closure-manifest@2.0.0', 'Manifest schema')
    need(manifest.get('spec') == SPEC, 'Manifest delivery specification')
    need(manifest.get('release_pins_sha256') == PINS_SHA256, 'Manifest release pin binding')
    need(isinstance(manifest.get('cards'), dict) and set(manifest['cards']) == set(IDS), 'Manifest denominator must be exactly 12')
    need(manifest.get('helpers') == pins['helpers'], 'Manifest helper denominator/SHA')
    need(manifest.get('data_sources') == pins['data_sources'], 'Manifest data source binding')
    for rel, digest in pins['data_sources'].items():
        bound_file(root, rel, digest)
    for rel, digest in pins['helpers'].items():
        bound_file(root, rel, digest)
    for card in IDS:
        entry, pin = manifest['cards'][card], pins['cards'][card]
        for key in ('media_rel', 'output_sha256', 'size_bytes', 'renderer_source_rel', 'renderer_source_sha256'):
            need(key in entry and entry[key] == pin[key], card + ': mandatory manifest binding differs: ' + key)
        media = bound_file(root, entry['media_rel'], entry['output_sha256'])
        need(media.stat().st_size == entry['size_bytes'], card + ': media bytes mismatch')
        bound_file(root, entry['renderer_source_rel'], entry['renderer_source_sha256'])
        if card in NATIVE:
            need(entry.get('generation') == 'native-1920x1080-current', card + ': generation route')
            run = read_json(bound_file(root, entry.get('run_rel'), entry.get('run_sha256')))
            validate_run(run, pins, card)
            font = read_json(bound_file(root, entry.get('font_rel'), entry.get('font_sha256')))
            need(font == run['font_dependency'], card + ': detached font receipt')
        else:
            need(entry.get('generation') == 'preserved-original-bytes', card + ': preserved media route')
    browser_ref = manifest.get('browser', {})
    browser = read_json(bound_file(root, browser_ref.get('rel'), browser_ref.get('sha256')))
    raw_browser = read_json(bound_file(root, browser_ref.get('raw_rel'), pins['raw_browser_sha256']))
    need(browser == browser_from_raw(raw_browser, pins['raw_browser_sha256']), 'Browser normalized receipt differs from pinned original')
    browser_result = validate_browser(browser, pins)
    contacts = manifest.get('gallery', {})
    need(set(contacts) == set(IDS), 'Contact sheet denominator must be 12')
    for card, contact in contacts.items():
        need(contact.get('source_mp4_sha256') == pins['cards'][card]['output_sha256'] and
             contact.get('decoded_frame_indices') == [0, 120, 233, 299], card + ': contact sheet source binding')
        bound_file(root, contact.get('rel'), contact.get('sha256'))
    gallery = GalleryParser()
    gallery.feed(canonical_file(root, 'gallery/index.html').read_text(encoding='utf-8'))
    expected_media = {'../' + pins['cards'][c]['media_rel'] for c in IDS}
    need(gallery.controls == 12 and len(gallery.sources) == 12 and set(gallery.sources) == expected_media,
         'Gallery must contain 12 playable controlled video elements')
    need(not (root / 'tools/native_scale_render.py').exists() and not (root / 'tools/native_scale_render.js').exists(),
         'Historical scale wrappers must not be current tools')
    return pins, manifest, browser_result


def verify(root, ffmpeg=None):
    pins, manifest, browser_result = validate_package(root)
    measurements = {}
    for card in IDS:
        measurements[card] = measure_media(Path(root) / pins['cards'][card]['media_rel'], ffmpeg, card in NATIVE)
    return {'ok': True, 'schema': 'motion-public-verification@2.0.0', 'cards': 12,
            'release_pins_sha256': PINS_SHA256, 'manifest_sha256': sha256(Path(root) / 'manifest.json'),
            'browser': browser_result, 'media': measurements,
            'scope': 'Fresh full decode and file/receipt binding. Does not rerender, rerun Chrome, or assign human aesthetic scores.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--ffmpeg')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    try:
        report = verify(args.root, args.ffmpeg); code = 0
    except EnvironmentError_ as e:
        report = {'ok': False, 'failure': 'environment', 'reason': str(e)}; code = 2
    except (VerificationError, KeyError, TypeError, ValueError, OSError) as e:
        report = {'ok': False, 'failure': 'verification', 'reason': str(e)}; code = 1
    text = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True); args.report.write_bytes(text.encode('utf-8'))
    print(text, end=''); return code


if __name__ == '__main__':
    sys.exit(main())
