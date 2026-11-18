"""Run the proposed checker against real repository counts and isolated README copies.

The runner supplies CHECKER_SOURCE, ROOT_PATH and EXPECTED_SOURCE_HASHES when
executed remotely. No candidate/publication file is written. Only parse_readme's
input root is redirected to three temporary copies for mutation cases; every
counter, rights-row/path comparison and main() exit path runs unchanged against
the real repository. Temporary copies are deleted at the end.
"""
from pathlib import Path
import contextlib, hashlib, io, json, sys, tempfile, types

root = Path(ROOT_PATH)
for rel, expected in EXPECTED_SOURCE_HASHES.items():
    assert hashlib.sha256((root / rel).read_bytes()).hexdigest() == expected, rel

module = types.ModuleType('proposed_public_counts')
module.__file__ = str(root / 'tools/check_library_counts.py')
exec(compile(CHECKER_SOURCE, '<proposed tools/check_library_counts.py>', 'exec'), module.__dict__)
original_parse = module.parse_readme
original_readmes = {name: (root / name).read_text(encoding='utf-8') for name in module.README_PATTERNS}
cases = [
    {'id': 'actual_repository_positive', 'exit': 0},
    {'id': 'comma_and_bold_equivalent_positive', 'exit': 0, 'file': 'README.zh-CN.md', 'old': '2044 条带来源引文', 'new': '**2,044** 条带来源引文'},
    {'id': 'en_citations_changed', 'exit': 1, 'file': 'README.md', 'field': 'citations', 'old': '2,044 source-linked quotations', 'new': '2,043 source-linked quotations'},
    {'id': 'zh_modules_changed_other_76_preserved', 'exit': 1, 'file': 'README.zh-CN.md', 'field': 'modules', 'old': '76 张可组合模块卡', 'new': '75 张可组合模块卡'},
    {'id': 'ja_dossiers_changed_other_76_preserved', 'exit': 1, 'file': 'README.ja.md', 'field': 'dossiers', 'old': '画家ドシエ76件', 'new': '画家ドシエ75件'},
    {'id': 'en_historical_label_pd_cc0_changed', 'exit': 1, 'file': 'README.md', 'field': 'license_pd_cc0', 'old': 'historical 701/38', 'new': 'historical 700/38'},
    {'id': 'zh_file_attribution_changed', 'exit': 1, 'file': 'README.zh-CN.md', 'field': 'rights_attribution_required', 'old': '文件级保守分类为：**39 件需署名', 'new': '文件级保守分类为：**38 件需署名'},
    {'id': 'ja_conditional_changed', 'exit': 1, 'file': 'README.ja.md', 'field': 'rights_jurisdiction_dependent', 'old': '法域によって条件が異なる1点', 'new': '法域によって条件が異なる2点'},
    {'id': 'en_license_footer_count_changed', 'exit': 1, 'file': 'README.md', 'field': 'license_section_pd_cc0_no_stated_attribution', 'old': '699 carry recognized PD/CC0 labels', 'new': '698 carry recognized PD/CC0 labels'},
    {'id': 'en_citation_declaration_missing', 'exit': 2, 'file': 'README.md', 'field': 'citations', 'old': '**2,044 source-linked quotations** and ', 'new': ''},
    {'id': 'ja_attribution_false_declaration_missing', 'exit': 2, 'file': 'README.ja.md', 'field': 'rights_pd_cc0_no_stated_attribution', 'old': '帰属条件が記載されていない既知のPD/CC0ラベル699点、', 'new': ''},
    {'id': 'en_negative_dossiers_rejected', 'exit': 2, 'file': 'README.md', 'field': 'dossiers', 'old': '76 painter dossiers', 'new': '-76 painter dossiers'},
    {'id': 'en_decimal_dossiers_rejected', 'exit': 2, 'file': 'README.md', 'field': 'dossiers', 'old': '76 painter dossiers', 'new': '1.76 painter dossiers'},
]
results = []
with tempfile.TemporaryDirectory(prefix='designers-brain-readme-counts-') as temporary:
    overlay = Path(temporary)
    for case in cases:
        if case['id'] == 'actual_repository_positive':
            module.parse_readme = original_parse
        else:
            for name, text in original_readmes.items():
                if name == case.get('file'):
                    assert text.count(case['old']) == 1, case['id']
                    text = text.replace(case['old'], case['new'], 1)
                (overlay / name).write_text(text, encoding='utf-8', newline='\n')
            module.parse_readme = lambda ignored_root, name: original_parse(overlay, name)
        sys.argv = ['check_library_counts.py', '--root', str(root), '--json']
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            try:
                actual_exit = module.main()
            except SystemExit as exc:
                actual_exit = exc.code
        output = json.loads(stdout.getvalue()) if stdout.getvalue().strip() else None
        failed = [x for x in output['checks'] if not x['ok']] if output else []
        assert actual_exit == case['exit'], (case['id'], actual_exit, stderr.getvalue())
        if case['exit'] == 1:
            assert len(failed) == 1 and failed[0]['source'] == case['file'] and failed[0]['item'] == case['field'], (case['id'], failed)
        elif case['exit'] == 2:
            assert case['file'] in stderr.getvalue() and repr(case['field']) in stderr.getvalue(), (case['id'], stderr.getvalue())
        else:
            assert output['pass'] is True and not failed
        results.append({**case, 'actual_exit': actual_exit, 'failed_checks': failed, 'stderr': stderr.getvalue(),
                        'measured': output['measured'] if output else None,
                        'checks_count': len(output['checks']) if output else None,
                        'actual_repository_json_output': output if case['id'] == 'actual_repository_positive' else None,
                        'passed_expected_result': True})

print(json.dumps({'status': 'PASS', 'checker_sha256': hashlib.sha256(CHECKER_SOURCE.encode('utf-8')).hexdigest(),
                  'repository': str(root), 'source_hash_guards': EXPECTED_SOURCE_HASHES,
                  'scope': 'Actual repository counters and unchanged main() for every case; only README parse input redirected to real temporary copies for mutations. No source/rights/image/README in candidate or publication clone changed.',
                  'results': results}, ensure_ascii=False, indent=2))
