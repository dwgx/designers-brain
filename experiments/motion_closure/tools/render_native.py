#!/usr/bin/env python3
"""Explicit optional rerender of one current native card; never called by verify_all."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from verify_all import NATIVE, PINS_SHA256, VerificationError, bound_file, need, read_json, sha256


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('card', choices=NATIVE)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--font', type=Path, required=True)
    parser.add_argument('--node', default='node')
    args = parser.parse_args()
    try:
        pins = read_json(bound_file(ROOT, 'release-pins.json', PINS_SHA256))
        need(args.font.is_file(), 'Font file missing (fonts are not redistributed)')
        need(sha256(args.font) == pins['render_font_sha256'],
             'Font SHA differs from the published render dependency; this command reproduces the pinned release')
        need(not args.outdir.exists(), 'Choose a new output directory; existing render evidence is not overwritten')
        source = bound_file(ROOT, pins['cards'][args.card]['renderer_source_rel'],
                            pins['cards'][args.card]['renderer_source_sha256'])
        for rel, digest in pins['helpers'].items():
            bound_file(ROOT, rel, digest)
        env = dict(os.environ)
        env['MOTION_PYTHON'] = sys.executable
        env['MOTION_CJK_FONT'] = str(args.font.resolve())
        env['MOTION_CJK_FONT_INDEX'] = '0'
        env['MOTION' + args.card + '_FONT'] = str(args.font.resolve())
        env['MOTION' + args.card + '_FONT_INDEX'] = '0'
        args.outdir.mkdir(parents=True)
        if source.suffix == '.js':
            command = [args.node, str(source), 'full', str(args.outdir.resolve())]
        else:
            command = [sys.executable, '-B', str(source), 'all', '--outdir', str(args.outdir.resolve())]
        return subprocess.run(command, env=env, cwd=ROOT).returncode
    except (VerificationError, OSError, ValueError) as e:
        print(json.dumps({'ok': False, 'reason': str(e)}, ensure_ascii=False)); return 1


if __name__ == '__main__':
    sys.exit(main())
