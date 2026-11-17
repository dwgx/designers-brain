# RESULT — SEED-EXPERIMENT-openprest/prototype

Status `submitted`. Phase S05-SEED-PROTOTYPES. Author `SeedDepsRevisit` (reused S01 assessment owner).
NOT self-accepted; independent GLM review of what was actually tested is a later gate.

## Actual objective outcomes (all checks from `outputs/checks.json`)
- C1 35 primitives per setting, 0 out-of-grid
- C2 only radius_px varied; glyph masks + grid centers identical across s1/s2/s3
- C3 bad case DETECTED (out_of_grid=35, unregistered_scale=35)
- C4 small-size render emitted at 4px with 35 primitives retained; connectivity/counter (enclosed-hole) topology and readability NOT measured (C4 checks only n_primitives); unmeasured / pending_human. NO "topology loss recorded" claim.
- C5 SVG+PNG outputs exist (220x140 main, 60x40 small)
- C6 deterministic rerun all 18 files byte-identical
- C7 BOUNDARY: NOT a full font, variable-font axis NOT proven/disproven, author geometry NOT claimed

## Key measured numbers
{
  "n_primitives_per_setting": 35,
  "settings": [
    "s1(r=2)",
    "s2(r=4)",
    "s3(r=7)"
  ],
  "bad_case_detected": true,
  "bad_out_of_grid": 35,
  "bad_unregistered_scale": 35,
  "small_size_cell_px": 4,
  "small_size_n_primitives": 35,
  "ledger_bounds_s2": {
    "x_min": 28,
    "x_max": 192,
    "y_min": 22,
    "y_max": 118
  }
}

## Deterministic rerun
- run1 `outputs/` (18 files) vs run2 `rerun_20261115/` (18 files): **ALL FILES BYTE-IDENTICAL (PASS)**.
- Each per-file sha256 is bound in `receipt.json` `artifacts[]` and `runner_receipt.json`.

## Honest boundaries
2-glyph hand-declared geometry toy. NOT a complete font / language coverage / readability proof. '未找到 fvar' does NOT prove the artist did NOT use a variable font (remains 未证实). 15 negative barcode decodes NOT re-run; no usable-encoding claim. Seed stays E1; no E2/E3/active promotion. S11-B calibration: the 4px case is a small-size RENDER with 35 primitives retained; connectivity/counter topology and readability are UNMEASURED / `pending_human`.

## NOT claimed
- No E2/E3/active promotion, no validated reproduction, no human aesthetic judgement, no author-tool/algorithm identification.
- No generated image, no image API call, no budget consumption, no gateway/credential, no ffmpeg/archive media, no repo writes.
- Parent task's original goal (mechanism reproduction/ablation/E3 candidate) is NOT satisfied by this prototype sub-output; `required_artifact_kinds` of the parent are unchanged.
