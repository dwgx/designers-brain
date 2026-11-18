# Two hand-declared glyph masks (A/H) + one dot primitive family at 3 sizes + bad-grid control + small-size render — prototype/ (S05 LOCAL mechanism prototype; S11-B claim calibration)

> [LOCAL-MECHANISM-PROTOTYPE · NOT EVIDENCE · NOT E2/E3 · NOT a full font · NOT a variable-font-axis claim]
> status: **submitted · candidate mechanism hypothesis · NOT E2/E3 · NOT a validated reproduction**
> parent task SEED-EXPERIMENT-openprest ORIGINAL state/runner/reviewer records are PRESERVED untouched.
> Repo @ f0089523 READ-ONLY. Writes confined to this `prototype/` dir. `spawns_allowed=false`.

## What this is
Manually declared 5x7 ON-cell bitmaps for A(18 cells) and H(17 cells) = 35 primitives. Fixed 16px grid, 220x140 canvas. ONE filled-circle primitive family at r=2/4/7 (s1/s2/s3); SVG (stdlib text) + PNG (Pillow) both emitted with identical primitive coordinate/count/bounds ledgers. A deliberately bad case (half-cell offset + unregistered r=9) is detected by the in-bounds/uniform-scale check. A small-size (cell_px=4) render is emitted with the 35 primitives retained. **S11-B calibration:** the small-size case does NOT measure connectivity / counter (enclosed-hole) topology or readability — C4 checks only the primitive count. Topology-readability loss is UNMEASURED / `pending_human`; no "loss recorded / hole collapses" claim. Independent pixel topology (S11 §F3: black 8-connected components = 35 and white 4-connected enclosed holes = 0 for all four rasters) shows no "big had hole, small lost it" evidence.

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
2-glyph hand-declared geometry toy. NOT a complete font / language coverage / readability proof. '未找到 fvar' does NOT prove the artist did NOT use a variable font (remains 未证实). 15 negative barcode decodes NOT re-run; no usable-encoding claim. Seed stays E1; no E2/E3/active promotion.
These local engineering fixtures do NOT alter the image API matrix/budget, do NOT satisfy the E3 evidence gate, and do NOT promote the seed (still E1). Aesthetic/design validity stays `pending_human`. S11-B: small-size render emitted / 35 primitives retained / connectivity-counter topology and readability unmeasured / `pending_human`.
