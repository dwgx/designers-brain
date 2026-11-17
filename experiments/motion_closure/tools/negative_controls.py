#!/usr/bin/env python3
"""Verify a real package, then require actual mutated package copies to fail the CLI."""
import argparse
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import verify_all as v


def write_json(path, value):
    path.write_bytes((json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode('utf-8'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--ffmpeg')
    parser.add_argument('--positive-report', type=Path,
                        help='Reuse an existing full verification only when its manifest and all current file bindings match')
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    results = []
    try:
        if args.positive_report:
            original = v.read_json(args.positive_report)
            positive = original.get('verification', original)
            v.validate_package(args.root)
            v.need(positive.get('ok') is True and positive.get('schema') == 'motion-public-verification@2.0.0' and
                   positive.get('manifest_sha256') == v.sha256(args.root / 'manifest.json') and
                   positive.get('release_pins_sha256') == v.PINS_SHA256 and set(positive.get('media', {})) == set(v.IDS),
                   'Existing positive report does not match this exact package')
        else:
            positive = v.verify(args.root, args.ffmpeg)
        with tempfile.TemporaryDirectory(prefix='motion-negative-') as temporary:
            work = Path(temporary) / 'package'
            shutil.copytree(args.root, work, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
            pristine_manifest = (work / 'manifest.json').read_bytes()

            def trial(name, mutate, expected):
                touched = {}

                def change(rel, data):
                    path = work / rel
                    touched.setdefault(rel, path.read_bytes() if path.exists() else None)
                    if data is None:
                        path.unlink()
                    else:
                        path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(data)

                manifest = json.loads(pristine_manifest)
                try:
                    mutate(change, manifest)
                    write_json(work / 'manifest.json', manifest)
                    argv = [sys.executable, str(ROOT / 'verify_all.py'), '--root', str(work)]
                    if args.ffmpeg:
                        argv += ['--ffmpeg', args.ffmpeg]
                    run = subprocess.run(argv, capture_output=True, text=True, encoding='utf-8', timeout=180)
                    report = json.loads(run.stdout)
                    passed = run.returncode == 1 and report.get('ok') is False and expected in report.get('reason', '')
                    results.append({'case': name, 'expected_failure': expected, 'exit': run.returncode,
                                    'actual_reason': report.get('reason'), 'passed': passed})
                    v.need(passed, 'Negative control did not fail as expected: ' + name)
                finally:
                    for rel, data in touched.items():
                        path = work / rel
                        if data is None:
                            path.unlink(missing_ok=True)
                        else:
                            path.write_bytes(data)
                    (work / 'manifest.json').write_bytes(pristine_manifest)

            trial('missing_current_renderer', lambda c, m: c(m['cards']['03']['renderer_source_rel'], None), 'Missing file: sources/MOTION-03/render.py')
            trial('tampered_current_renderer', lambda c, m: c(m['cards']['03']['renderer_source_rel'], b'# replaced\n'), 'SHA mismatch: sources/MOTION-03/render.py')
            trial('missing_shared_helper', lambda c, m: c('sources/cjk_text.py', None), 'Missing file: sources/cjk_text.py')
            trial('tampered_shared_helper', lambda c, m: c('sources/cjk_text.js', b'// replaced\n'), 'SHA mismatch: sources/cjk_text.js')
            trial('omitted_renderer_sha', lambda c, m: m['cards']['03'].pop('renderer_source_sha256'), 'mandatory manifest binding differs: renderer_source_sha256')
            trial('missing_card', lambda c, m: m['cards'].pop('14'), 'denominator must be exactly 12')
            trial('missing_video', lambda c, m: c(m['cards']['03']['media_rel'], None), 'Missing file: media/MOTION-03.mp4')
            trial('truncated_video', lambda c, m: c(m['cards']['03']['media_rel'], (work / m['cards']['03']['media_rel']).read_bytes()[:2048]), 'SHA mismatch: media/MOTION-03.mp4')

            def bad_font(change, manifest):
                entry = manifest['cards']['03']; path = work / entry['run_rel']
                run = json.loads(path.read_bytes()); run['font_dependency']['font_sha256'] = '0' * 64
                change(entry['run_rel'], (json.dumps(run) + '\n').encode())
                entry['run_sha256'] = v.sha256(path)
            trial('font_receipt_semantic_forgery', bad_font, 'wrong font SHA')

            def bad_seek(change, manifest):
                entry = manifest['browser']; path = work / entry['rel']
                browser = json.loads(path.read_bytes()); browser['videos'][0]['seeks'][0]['observed'] = 0
                browser['videos'][0]['passed'] = True
                change(entry['rel'], (json.dumps(browser) + '\n').encode()); entry['sha256'] = v.sha256(path)
            trial('false_seek_pass', bad_seek, 'normalized receipt differs from pinned original')

        report = {'ok': True, 'positive_manifest_sha256': positive['manifest_sha256'],
                  'positive_full_decode_reused': bool(args.positive_report),
                  'negative_controls': results, 'scope': 'Real file mutations in a disposable copy, each rejected by the public CLI with exit 1. Original package unmodified.'}; code = 0
    except v.EnvironmentError_ as e:
        report = {'ok': False, 'failure': 'environment', 'reason': str(e), 'negative_controls': results}; code = 2
    except (v.VerificationError, OSError, ValueError, subprocess.TimeoutExpired) as e:
        report = {'ok': False, 'failure': 'negative_control', 'reason': str(e), 'negative_controls': results}; code = 1
    args.report.parent.mkdir(parents=True, exist_ok=True); write_json(args.report, report)
    print(json.dumps(report, ensure_ascii=False, indent=2)); return code


if __name__ == '__main__':
    sys.exit(main())
