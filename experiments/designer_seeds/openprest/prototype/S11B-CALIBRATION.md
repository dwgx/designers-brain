# S11 §B — bounded claim calibration (openprest prototype)

> Author `SeedDepsRevisit` · S11 §B calibration r1 · status `submitted` · research-grade stays research-grade.
> This is a CLAIM-LEVEL calibration of the EXISTING prototype. The prototype is NOT re-run beyond the two
> deterministic fixture generations; no new experiment, font, source, or image API is added.
> Parent E2/E3/active states, parent receipts/gates, and reviewer-owned `review-*` files are NOT touched here.

## 1. The overclaim that was corrected

The original `config.json` `small_size_limitation`, `build.py` small-size block, emitted
`small_size_limitation.json`, `checks.json` C4, `run_evidence.json` C4, and `README.md` described the 4px
small-size case as **"connectivity / counter (enclosed-hole) loss recorded / the 'A' counter collapses"**.

Evidence it did not support (from `seed-prototype-independent-review.md` §F3, supervisor read-only pixel
topology on the four rasters):

| image | black 8-connected components | white 4-connected enclosed holes |
|---|---:|---:|
| s1 (r=2) | 35 | 0 |
| s2 (r=4) | 35 | 0 |
| s3 (r=7) | 35 | 0 |
| 4px small | 35 | 0 |

`build.py` C4 checks ONLY `small_led["n_primitives"] == expected_n` (35). A count check is NOT a connectivity
or counter (enclosed-hole) measurement. No "big image had a hole, small image lost it" topological evidence
was produced. Human perception of dot-matrix legibility is a different, unmeasured question.

## 2. Calibrated claim (what the small-size case actually demonstrates)

**small-size render emitted / 35 primitives retained / connectivity-counter (enclosed-hole) topology and
readability UNMEASURED / `pending_human`.** No "loss recorded", no "hole collapses", no connectivity claim.

Applied consistently to: `config.json` (`small_size_limitation` + intended C4), `build.py` (docstring,
small-size block, small_led note/outcome, checks C4 key/note), emitted `outputs/small_size_limitation.json`,
`outputs/checks.json` C4, `outputs/glyphs_small_size.svg` comment, `outputs/run_config_snapshot.json` (config
SHA), `run_evidence.json` (intended C4, actual C4, per-file hashes), `runner_receipt.json` (input + artifact
hashes), `receipt.json` (all bindings + limitations), `README.md`, `RESULT.md`.

## 3. What actually changed after re-running the affected fixture

Commands (both exit 0): `python -X utf8 build.py outputs` and `python -X utf8 build.py rerun_20261115`.
All 18 outputs regenerate; 18/18 byte-identical between `outputs/` and `rerun_20261115/`.

Changed output bytes (geometry PNGs UNCHANGED — the A/H masks, grid, and primitive coordinates are identical):

| file | reason |
|---|---|
| `outputs/checks.json` | C4 key → `C4_small_size_render_recorded`, calibrated note |
| `outputs/glyphs_small_size.svg` | comment text |
| `outputs/small_size_limitation.json` | note/outcome/case wording |
| `outputs/run_config_snapshot.json` | embeds the new `config.json` SHA |

All other 14 output files (3 setting PNG/SVG, bad-grid PNG/SVG, small-size PNG, 4 ledgers, parameter_ledger,
3 primitives_*.json) are byte-identical to the original. All hash bindings in `run_evidence.json`,
`runner_receipt.json`, and `receipt.json` were recomputed from bytes (not hand-copied) and verified consistent.

## 4. Claim bounds (unchanged from the preserved experiment)

2-glyph hand-declared geometry toy (A/H = 35 primitives); ONE filled-circle primitive family at r=2/4/7;
bad-grid case DETECTED (out_of_grid=35, unregistered_scale=35). NOT a complete font / language coverage /
readability proof. "未找到 fvar" does NOT prove the artist did NOT use a variable font (remains 未证实).
15 negative barcode decodes NOT re-run; no usable-encoding claim. Reversal/bad-case are controls, not
aesthetic judgments. NOT E2/E3 evidence, NOT a validated reproduction, NOT an E3 success, NOT the artist's
geometry. Aesthetic/design validity stays `pending_human`. Seed stays E1; no E2/E3/active promotion.

## 5. What was NOT done (bounded scope)

- No new readability/topology experiment, no human study, no font engine, no new glyph, no source collection.
- No change to parent `state.md`, parent receipts, `review-*` reviewer files, E2/E3/active gates.
- No promotion; S09 acceptance remains PAUSED.

---

`verify-receipt.py` (PKG tool SHA `00ef6071ed8b021b049569b3cfbead45238fff1f0a9e2ecbe787c614af767bd0`,
schema SHA `c553112d336e66e03639f7a569abd8f9b8ddc0707a5b3667ecd9d355a9a1fb31`) is run on the final
`receipt.json` (status `submitted` → schema-only validation, `verify-receipt.py:20-21`); result saved in
`verify-receipt.out`. Tool/schema DO exist in the sealed PKG (the earlier reviewer "tool_absent" claim is
the reviewer's to correct in its own files).
