# ASCII selected-region mask + MEASURED glyph-coverage ramp (normal + reversed control) — prototype/ (S05 LOCAL mechanism prototype)

> [LOCAL-MECHANISM-PROTOTYPE · NOT EVIDENCE · NOT E2/E3 · pending_human aesthetic judgement reserved]
> status: **submitted · candidate mechanism hypothesis · NOT E2/E3 · NOT a validated reproduction**
> parent task SEED-EXPERIMENT-enigmatriz ORIGINAL state/runner/reviewer records are PRESERVED untouched.
> Repo @ f0089523 READ-ONLY. Writes confined to this `prototype/` dir. `spawns_allowed=false`.

## What this is
Synthetic 120x60 grayscale chart; explicit 8,8-72,52 rectangular mask; 10x5 grid of 12px cells. Glyph ink coverage MEASURED with declared Consolas font (NOT assumed '@' darkest), ramp sorted ascending. In-mask cells substituted with glyph tiles; OUT-mask pixels kept byte-identical to input. Normal + reversed ramp control. MetricPilot srgb8_to_Lstar/lum_hist/lap_var reused as numeric interfaces on the synthetic chart.

## Environment (probed on host)
- Python 3.14.7, Pillow 12.3.0 (8x8 in-memory mean=127.0 confirmed), jsonschema 4.26.0.
- stdlib + Pillow only. NO image API, NO browser/WebGL, NO ffmpeg, NO historical/author media, NO credentials, NO RNG (coordinate-deterministic where noise is needed).

## Files
- `config.json` — FINAL run config + post-hoc `observed_after_run` correction record (NOT a provably frozen pre-registration; see `S11B-CALIBRATION.md` §2). It declares the synthetic chart, ONE mask rectangle, measured glyph ramp, and intended/observed checks; C4 in `build.py` is a constant `True`, NOT a general mask validator.
- `build.py` — executable mechanism source (deterministic; run twice for rerun evidence).
- `outputs/` — actual PNG/SVG/ASCII/JSON outputs + `checks.json` + `run_config_snapshot.json`.
- `rerun_20261115/` — full second-generation outputs (deterministic rerun evidence).
- `run_evidence.json` — post-run outcomes: intended checks vs actual, rerun identity, real hashes.
- `README.md` / `RESULT.md` / `runner_receipt.json` / `receipt.json` / `verify-receipt.out`.

## Reproduce
```
python -X utf8 build.py outputs
python -X utf8 build.py rerun_20261115
python -X utf8 <package>/tools/verify-receipt.py receipt.json --schema <package>/templates/receipt.schema.json --workspace-root <RUN_ROOT>
```

## Boundary
Only supports OUR implemented selected-region/quantization mechanism. NOT the artist's algorithm, NOT automatic mask toolchain, NOT human 'looks like enigmatriz'. Reversal is a CONTROL, not an aesthetic failure. Seed stays E1; no E2/E3/active promotion.
These local engineering fixtures do NOT alter the image API matrix/budget, do NOT satisfy the E3 evidence gate, and do NOT promote the seed (still E1). Aesthetic/design validity stays `pending_human`.
- `S11B-CALIBRATION.md` — S11 §B claim calibration (receipt binding recompute, config honesty, C4 bounds).

## S11 §B calibration (added, no experiment change)
- Config is a final run config + post-hoc correction record, NOT pre-registered; "PRE-RUN config" label removed.
- `build.py` C4 `pass` is a constant `True` → not an independent/general mask validator; only THIS mask (8,8-72,52) had outside-mask diff verified = 0.
- Receipt binding: reviewer `reviewed_artifact_hashes[0]` recorded `d23093dd89ed6ee7f1f5885e0…` (wrong); recomputed author-receipt byte-SHA was `d23093dd89ed6ee79e1d7d7ba0…`; FINAL byte-SHA after this calibration is in `verify-receipt.out`. See `S11B-CALIBRATION.md` §1. Reviewer-owned files are NOT edited here.
