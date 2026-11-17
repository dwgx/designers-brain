# S11 §B — bounded claim calibration (kail_designs prototype)

> Author `SeedDepsRevisit` · S11 §B calibration r1 · status `submitted` · research-grade stays research-grade.
> This is a CLAIM-LEVEL calibration of the EXISTING prototype. No experiment is re-run, extended, or added.
> The frozen `config.json`, `build.py`, `outputs/`, `rerun_20261115/`, `run_evidence.json`, `runner_receipt.json`
> bytes are PRESERVED UNCHANGED (config/code/outputs existence and boundaries confirmed by the supervisor).
> Parent E2/E3/active states, parent receipts/gates, and reviewer-owned `review-*` files are NOT touched here.

## 1. Bound claims to the chain actually tested

What was ACTUALLY run (from `outputs/checks.json` / `run_evidence.json`, unchanged bytes):

- ONE self-authored 64x48 grayscale field in RAW 8-bit code values 0..255 (no EOTF / no CIE L*).
- EXACTLY FOUR variants, each a SINGLE toggle from the baseline:
  | variant | toggle | measured effect |
  |---|---|---|
  | `v0_baseline` | none | reference field |
  | `v1_exposure` | exposure gain 1.35 only | bright-region mean 250→337.5 (raw), clip@255 **0→1113**, clipping_increased=true |
  | `v2_halo` | halo toggle only | halo-ring mean 129.206→155.132, bright-region mean unchanged 250.0, halo diff-map mean 25.9614 |
  | `v3_grain` | grain toggle only | flat-region mean abs diff 5.8671, overall mean abs diff 6.0361, coordinate-deterministic, rng_used=false |
- C1 all four are 64x48, dimensions UNCHANGED. C6 deterministic rerun 18/18 byte-identical.

The supported claim is therefore narrowly: **the exposure→halo→grain single-toggle chain on this one
self-created field produced the four bounded measurements above (clip 0→1113, 4 variants)**. The declared
order in `config.json` `variants_at_most_four` and the C7 "ONE self-authored operator stack (exposure->halo->grain)
in declared order" label is a DESIGN DECLARATION, not an experimentally verified causal claim.

## 2. What the four single-toggle variants do NOT establish

- **No combined-pass-order verification.** No variant enables two or three toggles together; there is no
  exposure+halo, halo+grain, or full-stack (exposure→halo→grain) output. The effect of composition/order was
  NOT measured. Do not write "verified full stack" or "validated default pass order".
- **C4 MAD>0 is NOT spectrum / low-frequency preservation evidence.** C4 checks only
  `flat_region_mean_abs_diff > 0` plus coordinate-determinism. No FFT / frequency-band / low-frequency
  retention measurement was run. The config C4 wording "overall low-frequency structure preserved" is a
  design intent, not a measured result; "grain is high-frequency" is a hypothesis, not a spectral finding.
- **Not the real kernel.** NOT the ascii-magic / backgrounds.supply real kernel, NOT their default pass order,
  NOT a proven shader pipeline. Two product pages' feature labels are NOT merged into one claimed pipeline.
- **No generalization.** No time-continuity, website-determinism, 4K, or video-export claim; no author
  artwork, no image API, no human aesthetic judgement. Aesthetic/design validity stays `pending_human`.

## 3. Claim bounds (unchanged from the preserved experiment)

CANDIDATE local post-processing mechanism hypothesis ONLY. NOT E2/E3 evidence, NOT a validated reproduction,
NOT an E3 success. Seed stays E1; no E2/E3/active promotion. `status=submitted` validates schema only
(`verify-receipt.py:20-21`); author does not self-accept; independent review is a later gate.

## 4. What was NOT done (bounded scope)

- No new variant, no combined-toggle run, no spectral analysis, no new output image, no image API, no network,
  no credentials, no font/author-media/source collection.
- No change to parent `state.md`, parent receipts, `review-*` reviewer files, E2/E3/active gates.
- No promotion; S09 acceptance remains PAUSED.

---

`verify-receipt.py` (PKG tool SHA `00ef6071ed8b021b049569b3cfbead45238fff1f0a9e2ecbe787c614af767bd0`,
schema SHA `c553112d336e66e03639f7a569abd8f9b8ddc0707a5b3667ecd9d355a9a1fb31`) is run on the final
`receipt.json` (status `submitted` → schema-only validation); result saved in `verify-receipt.out`.
Tool/schema DO exist in the sealed PKG (the earlier reviewer "tool_absent" claim is the reviewer's to correct).
