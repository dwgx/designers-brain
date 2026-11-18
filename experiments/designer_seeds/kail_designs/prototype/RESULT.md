# RESULT — SEED-EXPERIMENT-kail_designs/prototype

Status `submitted`. Phase S05-SEED-PROTOTYPES. Author `SeedDepsRevisit` (reused S01 assessment owner).
NOT self-accepted; independent GLM review of what was actually tested is a later gate.

## Actual objective outcomes (all checks from `outputs/checks.json`)
- C1 exactly 4 variants (<=4), all 64x48 unchanged dims
- C2 exposure gain 1.35: bright mean 250->337.5 (raw), clip@255 0->1113, color units declared
- C3 halo localized: ring mean 129.206->155.132, bright region unchanged (250.0), halo diff map mean 25.96
- C4 grain: flat-region mean abs diff 5.867, coordinate-deterministic, no RNG
- C5 input field/variants/diff maps/arrays all retained
- C6 deterministic rerun all 18 files byte-identical
- C7 BOUNDARY: single self-authored stack; two product pages NOT conflated; no time-continuity/website/4K/video/shader-pipeline claim

## Key measured numbers
{
  "n_variants": 4,
  "dims": [
    64,
    48
  ],
  "exposure_clip_255": [
    0,
    1113
  ],
  "halo_ring_mean": [
    129.206,
    155.132
  ],
  "bright_region_unchanged": true,
  "grain_flat_diff": 5.8671,
  "rng_used": false
}

## Deterministic rerun
- run1 `outputs/` (18 files) vs run2 `rerun_20261115/` (18 files): **ALL FILES BYTE-IDENTICAL (PASS)**.
- Each per-file sha256 is bound in `receipt.json` `artifacts[]` and `runner_receipt.json`.

## Honest boundaries
Candidate local post-processing mechanism ONLY. NOT the real ascii-magic/backgrounds.supply kernel, NOT their default pass order, NOT a proven shader pipeline. Two product pages' labels NOT merged. No time-continuity / website-determinism / 4K / video-export claim. Seed stays E1; no E2/E3/active promotion.

## NOT claimed
- No E2/E3/active promotion, no validated reproduction, no human aesthetic judgement, no author-tool/algorithm identification.
- No generated image, no image API call, no budget consumption, no gateway/credential, no ffmpeg/archive media, no repo writes.
- Parent task's original goal (mechanism reproduction/ablation/E3 candidate) is NOT satisfied by this prototype sub-output; `required_artifact_kinds` of the parent are unchanged.

## S11 §B calibration (claim-level only; no experiment re-run)
- Bounded to the tested chain: exposure→halo→grain, 4 single-toggle variants (clip 0→1113 included), one self-created 64x48 field.
- Four single toggles do NOT verify combined pass order / full-stack effect; C4 `flat_region_mean_abs_diff=5.8671 > 0` is NOT a spectrum / low-frequency-preservation measurement. Declared order is a design declaration. See `S11B-CALIBRATION.md`.
