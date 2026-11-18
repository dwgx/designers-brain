# RESULT — SEED-EXPERIMENT-enigmatriz/prototype

Status `submitted`. Phase S05-SEED-PROTOTYPES. Author `SeedDepsRevisit` (reused S01 assessment owner).
NOT self-accepted; independent GLM review of what was actually tested is a later gate.

## Actual objective outcomes (all checks from `outputs/checks.json`)
- C1 measured ramp (10 glyphs, coverage 0.000..0.368)
- C2 outside-mask diff = 0 (chart/normal/reversed all 0)
- C3 reversal sign flip (pearson +0.8795 / -0.8990, 15 in-mask glyphs changed)
- C4 15 in-mask / 35 out-mask cells, all in-mask have glyph, none out-mask touched
- C5 dims 120x60 unchanged, ASCII 10x5
- C6 deterministic rerun all 11 files byte-identical
- C7 MetricPilot interfaces reused (lum_hist N=2925, lap_var var=621.03)

## Key measured numbers
{
  "measured_ramp_ascending_coverage": " -.:=+*#%@",
  "outside_mask_diff": [
    0,
    0,
    0
  ],
  "pearson_normal": 0.879535,
  "pearson_reversed": -0.899008,
  "sign_flipped": true,
  "in_mask_cells": 15,
  "out_mask_cells": 35,
  "changed_glyphs": 15,
  "metricpilot_lum_hist_N": 2925,
  "metricpilot_lap_var": 621.0324
}

## Deterministic rerun
- run1 `outputs/` (11 files) vs run2 `rerun_20261115/` (11 files): **ALL FILES BYTE-IDENTICAL (PASS)**.
- Each per-file sha256 is bound in `receipt.json` `artifacts[]` and `runner_receipt.json`.

## Honest boundaries
Only supports OUR implemented selected-region/quantization mechanism. NOT the artist's algorithm, NOT automatic mask toolchain, NOT human 'looks like enigmatriz'. Reversal is a CONTROL, not an aesthetic failure. Seed stays E1; no E2/E3/active promotion.

## NOT claimed
- No E2/E3/active promotion, no validated reproduction, no human aesthetic judgement, no author-tool/algorithm identification.
- No generated image, no image API call, no budget consumption, no gateway/credential, no ffmpeg/archive media, no repo writes.
- Parent task's original goal (mechanism reproduction/ablation/E3 candidate) is NOT satisfied by this prototype sub-output; `required_artifact_kinds` of the parent are unchanged.

## S11 §B calibration (claim-level only; no experiment re-run)
- Config honesty: final run config with post-hoc correction, NOT frozen pre-registration; C4 is a constant `True` (not a general mask validator); only this declared mask had outside-mask diff = 0.
- Receipt binding: recorded `reviewed_artifact_hashes[0]` = `d23093dd89ed6ee7f1f5885e02f3ba2c7f583bc62a488b07e11dc8bbbf02b0ee` (incorrect) vs recomputed-from-bytes author receipt = `d23093dd89ed6ee79e1d7d7ba01675953417b5b34d4060334a5b4595a4b47a35` (pre-calibration). Final byte-SHA after calibration is in `verify-receipt.out`; reviewer-owned files untouched. See `S11B-CALIBRATION.md`.
