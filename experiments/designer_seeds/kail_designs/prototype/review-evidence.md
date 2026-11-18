# REVIEW EVIDENCE — SEED-PROTOTYPE-kail_designs-REVIEW

Reviewer: ReviewGateSeedProto (glm-5.3-flash), independent of author SeedDepsRevisit. Review target: `staging/SEED-EXPERIMENT-kail_designs/prototype/`. Repo `SOURCE@designers-brain (read-only source repo)` @ `f008952365a77e140cbda3f3959d43ef000f9a22` read-only. Reviewed 2026-11-15T14:26Z. No author file touched; all reviewer commands wrote only to a system temp dir.

## Verdict: ACCEPTED

All six assignment checks pass on recomputation from raw bytes/pixels, including full first-principles reproduction of the grain operator.

## Check 1 — Dir manifest hash recomputed: MATCH

Recipe (verified by this reviewer against all three prototypes): lines `<relpath>  <sha256>` (two spaces), paths relative to `prototype/` with forward slashes, sorted by path, joined with `\n`, no trailing newline; sha256 of that text.

- Files in scope: **44** (8 top-level + 18 `outputs/` + 18 `rerun_20261115/`)
- Recomputed: `615cde69ebd528b438431a070c53e1da679e2b9cb085e3b11ec217598726cbc8`
- Claimed: `615cde69…` → **MATCH**.

(The three review-gate files this review adds are not part of the 44-file manifest.)

## Check 2 — Deterministic rerun executed by this reviewer: BYTE-IDENTICAL

- `python -X utf8 build.py <tempdir>` (exit 0) → `diff -r` my fresh run vs author `outputs/`: **IDENTICAL** (18/18 files).
- Author `rerun_20261115/` vs `outputs/`: **IDENTICAL** (18/18).
- `receipt.json.artifacts[]`: **24/24 hashes recomputed by this reviewer → match**.

## Check 3 — kail_designs-specific measurements: ALL REPRODUCED FROM RAW GRIDS/PIXELS

- **RAW 8-bit code values declared**: `config.json.color_units` declares input/internal/output all in "8-bit grayscale code value 0..255", explicitly "NOT sRGB EOTF / NOT CIE L*", with a note that this scale is deliberately NOT the METRIC-PILOT L* scale used in the enigmatriz prototype ("Do not mix the two scales") ✓.
- **Exposure clip 0 → 1113**: recomputed from pixels — baseline v0: **0** pixels at 255; v1_exposure: **1113** pixels ≥255 over the whole 64×48 image (441 of them in the bright region, remainder from the ramp: 235×1.35=317.25 > 255) — exact match with `checks.json` C2 `exposure_clip_255: [0, 1113]`, gain 1.35, bright mean 250→337.5 raw ✓.
- **Halo ring mean 129.206 → 155.132, bright region unchanged**: recomputed from the stored pre-clamp field grids (`v0_baseline.json` / `v2_halo.json` `field`, ring = halo_region rect minus bright rect, n=648): **129.2063 → 155.1323** — matches claimed 129.206/155.132 exactly. Bright region mean 250.0000 → 250.0000 (**unchanged**, halo is ring-only, gain·falloff applied only outside the bright rect) ✓. (PNG-based recompute differs by ≤0.06 solely from 8-bit clamping — pre-clamp JSON grids are the declared measurement surface, and the author's numbers match those.)
- **Grain flat diff 5.867, coordinate-deterministic**: flat-region mean |v3−v0| recomputed from PNGs = **5.8671** (claimed 5.8671, n=143) ✓. Determinism proven by reproduction: `120 + 12·(((x·73 + y·151 + x·y·7) mod 41) − 20)/20` predicts every v3_grain flat-region pixel **exactly (max error 0, 143/143)** — no RNG, no seed state; overall mean abs diff 6.0361 also matches ✓.

## Check 4 — Two product pages NOT conflated: CLEAN

- `checks.json` C7: "ONE self-authored operator stack (exposure→halo→grain) in declared order; two product pages NOT conflated; NO time-continuity / website-determinism / 4K / video-export / real-shader-pipeline claim".
- README/RESULT label: "single self-authored pass stack, NOT two product pages conflated into one proven shader pipeline"; boundary text keeps the two product pages' labels separate. ✓

## Check 5 — E2/E3/active boundaries: CLEAN

- Every promotion-adjacent sentence is a **negation** ("Seed stays E1; no E2/E3/active promotion"; `no_e2_e3_active_change: true`); candidate-hypothesis framing throughout.
- `receipt.json.claims` = 2× `observation/supported`; `review: null` (not self-accepted); `spawns_allowed: false`.
- Parent `state.md` byte-unchanged: current sha256 `150edc67…` == hash declared in prototype `receipt.json.input_hashes` ("parent, preserved") ✓.

## Check 6 — verify-receipt.py: TOOL ABSENT; equivalent validation PASS

`verify-receipt.py` / `receipt.schema.json` are **not present anywhere on this machine** (searched repo, RUN_ROOT, `<home>/.dwgx`, `<private-source-tree>`); the `<package>/` path referenced in README/verify-receipt.out no longer exists locally → the literal "exit 0" tool rerun is [UNVERIFIED] as a command execution.

Equivalent independent validation performed instead (all on raw bytes):
- Structural: `schema_version 1.0`, ids present, `status=submitted`, `author_actor_id=SeedDepsRevisit`, `review=null`, `human_review.status=not_applicable`, `execution.receipt_sha256` == sha256(`runner_receipt.json`) ✓.
- **24/24 artifact hashes** + **4/4 input_hashes** recomputed → match; claim `source_refs.retrieved_bytes_sha256` bindings → match ✓.
- Stored `verify-receipt.out`: `ok: true`, `errors: []`, `EXIT_CODE=0` (author-attested, not re-executed — see above).

## Non-material nit

`checks.json` C6 field `pass: null` — pass verdict lives in `run_evidence.json.deterministic_rerun` (18/18 byte-identical, verified true by this reviewer). Cosmetic split only.
