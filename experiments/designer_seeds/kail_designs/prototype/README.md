# Self-created luminance field + explicit exposure / halo / grain toggles (4 variants) — prototype/ (S05 LOCAL mechanism prototype)

> [LOCAL-MECHANISM-PROTOTYPE · NOT EVIDENCE · NOT E2/E3 · single self-authored pass stack, NOT two product pages conflated into one proven shader pipeline]
> status: **submitted · candidate mechanism hypothesis · NOT E2/E3 · NOT a validated reproduction**
> parent task SEED-EXPERIMENT-kail_designs ORIGINAL state/runner/reviewer records are PRESERVED untouched.
> Repo @ f0089523 READ-ONLY. Writes confined to this `prototype/` dir. `spawns_allowed=false`.

## What this is
64x48 self-created luminance field (linear ramp + flat patch + bright region + halo ring), declared in RAW 8-bit code values 0..255 (no EOTF/L*). ONE self-authored operator stack (exposure->halo->grain) in declared order. **4 variants, each a SINGLE toggle**: baseline / exposure-only (clip 0→1113) / halo-only / grain-only. Coordinate-deterministic grain (NO RNG, NO website seed). Difference maps + regional diff stats + clipping counts emitted. **S11-B bound:** this tests ONLY the four single-toggle variants on one field; NO combined-toggle / full-stack-order verification, and C4 MAD>0 is NOT a spectrum / low-frequency-preservation measurement (see `S11B-CALIBRATION.md`).

## Environment (probed on host)
- Python 3.14.7, Pillow 12.3.0 (8x8 in-memory mean=127.0 confirmed), jsonschema 4.26.0.
- stdlib + Pillow only. NO image API, NO browser/WebGL, NO ffmpeg, NO historical/author media, NO credentials, NO RNG (coordinate-deterministic where noise is needed).

## Files
- `config.json` — PRE-RUN config + intended checks + declared color units / boundaries.
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
Candidate local post-processing mechanism ONLY. NOT the real ascii-magic/backgrounds.supply kernel, NOT their default pass order, NOT a proven shader pipeline. Two product pages' labels NOT merged. No time-continuity / website-determinism / 4K / video-export claim. Seed stays E1; no E2/E3/active promotion.
These local engineering fixtures do NOT alter the image API matrix/budget, do NOT satisfy the E3 evidence gate, and do NOT promote the seed (still E1). Aesthetic/design validity stays `pending_human`.
- `S11B-CALIBRATION.md` — S11 §B claim calibration (bounds to the exposure→halo→grain single-toggle chain, clip 0→1113, 4 variants).

## S11 §B calibration (added, no experiment change)
- Claims bounded to what was tested: 4 variants (v0 baseline + v1 exposure-only clip 0→1113 + v2 halo-only + v3 grain-only), 64x48, single toggles only.
- NOT established: combined pass order / full-stack causal effect; spectrum or low-frequency retention from C4 MAD>0; real kernel / default pass order / proven shader pipeline. Declared stack order is a design declaration, not a measured result.
