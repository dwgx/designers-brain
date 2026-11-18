"""Reproduce the finite count-checker regression cases without changing the checkout."""
from pathlib import Path
import argparse, hashlib, json, runpy

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--root', type=Path, required=True)
args = parser.parse_args()
root = args.root.resolve()
here = Path(__file__).resolve().parent
manifest = json.loads((here / 'PATCH-MANIFEST.json').read_text('utf-8'))
guards = {x['path']: x['sha256'] for x in manifest['source_guards']}
checker = (root / 'tools/check_library_counts.py').read_bytes()
assert hashlib.sha256(checker).hexdigest() == manifest['files'][0]['after_sha256'], 'Checker differs from reviewed repair'
runpy.run_path(str(here / 'validate_actual_repository.py'), init_globals={
    'CHECKER_SOURCE': checker.decode('utf-8'),
    'ROOT_PATH': str(root),
    'EXPECTED_SOURCE_HASHES': guards,
})
