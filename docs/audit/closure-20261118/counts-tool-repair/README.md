# Public-count checker repair

The first clean-clone gate failed because the old checker expected obsolete README wording. Its Chinese/Japanese headline checks also accepted a number found elsewhere on the page. The corrected read-only checker parses each semantic field exactly once, compares all three languages with actual repository counts, and separates artwork-level manifest labels from file-level attribution records.

The final proposal was run against the actual review checkout. Thirteen cases returned the required result: two positives (41/41 comparisons), seven single-field count mutations (exit 1), and four structural failures (exit 2: two missing fields, one negative count and one fractional count). Negative cases redirect only README parsing to temporary copies of the real documents; all actual counters and main() still read the real repository. No candidate README, image, rights data or historical baseline was changed by these tests.

An independent reviewer found that the first proposal could read the trailing 76 from -76 or 1.76. That proposal was not integrated. The final token boundary rejects both specific counterexamples while preserving Japanese declarations without spaces. The older failed clean-clone receipt remains in ../initial-clean-gate/.

VALIDATION.json is a machine-path-redacted projection of the actual run. PROJECTION.json binds original and public bytes; PATCH-MANIFEST.json binds the unchanged source documents and before/after checker bytes. This is counting and disclosure validation, not a worldwide legal determination or a claim that every source was independently re-read.

From the repository root, run the current positive check and the preserved finite regression cases:

```text
python -X utf8 -B tools/check_library_counts.py --json
python -X utf8 -B docs/audit/closure-20261118/counts-tool-repair/reproduce.py --root .
```

The regression cases intentionally require the recorded README/rights input hashes. A later legitimate content change needs a separately reviewed update; the runner does not silently change its expectations.
