# REVIEW EVIDENCE — SEED-PROTOTYPE-openprest-REVIEW

Reviewer: ReviewGateSeedProto (glm-5.3-flash), independent of author SeedDepsRevisit. Review target: `staging/SEED-EXPERIMENT-openprest/prototype/`. Repo `SOURCE@designers-brain (read-only source repo)` @ `f008952365a77e140cbda3f3959d43ef000f9a22` read-only. Reviewed 2026-11-15T14:26Z. No author file touched; all reviewer commands wrote only to a system temp dir.

## Verdict: ACCEPTED

All six assignment checks pass on recomputation from raw outputs.

## Check 1 — Dir manifest hash recomputed: MATCH

Recipe (verified by this reviewer against all three prototypes): lines `<relpath>  <sha256>` (two spaces), paths relative to `prototype/` with forward slashes, sorted by path, joined with `\n`, no trailing newline; sha256 of that text.

- Files in scope: **44** (8 top-level + 18 `outputs/` + 18 `rerun_20261115/`)
- Recomputed: `d14462e611c36193e6488af7a3eddfadf3119fc0ecb7e10019554821eb960e77`
- Claimed: `d14462e6…` → **MATCH**.

(The three review-gate files this review adds are not part of the 44-file manifest.)

## Check 2 — Deterministic rerun executed by this reviewer: BYTE-IDENTICAL

- `python -X utf8 build.py <tempdir>` (exit 0) → `diff -r` my fresh run vs author `outputs/`: **IDENTICAL** (18/18 files).
- Author `rerun_20261115/` vs `outputs/`: **IDENTICAL** (18/18).
- `receipt.json.artifacts[]`: **24/24 hashes recomputed by this reviewer → match** (includes both run dirs, receipts, run_evidence).

## Check 3 — Openprest-specific measurements: ALL VERIFIED FROM RAW JSON

- **A(18) + H(17) = 35 primitives**: recomputed from `outputs/primitives_s1.json` — `primitives[]` length 35; per-glyph split **A=18, H=17** (matches `A_on_cells: 18`, `H_on_cells: 17`, and `config.json` glyph-mask on-cell lists). Same n=35, out_of_grid=0 for s2 and s3 (`checks.json` C1 per_setting, only `radius_px` varies 2/4/7 — C2 registered-radius-only confirmed).
- **Bad-grid case DETECTED, not silently accepted**: `outputs/primitives_bad_grid_offset.json.in_bounds_check`: **out_of_grid_count = 35**, **unregistered_scale_count = 35**, `detected: true`, `outcome: "DETECTED (expected failure)"`. Verified the inputs: offset [8,8] applied and radius r=9 ∉ registered radii [2,4,7] — the named failure the config demands. ✓
- **4px small-size limitation recorded**: `outputs/small_size_limitation.json`: cell_px=4, canvas 60×40, n_primitives=35, r=1; explicitly "RECORDED LIMITATION, not a legibility/readability claim and not a font"; `checks.json` C4 pass with "connectivity/counter loss recorded; NO readability claim" ✓.
- **NOT labeled a font**: `checks.json` C7 label = "2-glyph hand-declared geometry toy; NOT a font; variable-font axis NOT proven/disproven; author geometry NOT claimed"; README label `[… NOT a full font · NOT a variable-font-axis claim]`; RESULT.md "NOT a complete font / language coverage / readability proof", "'未找到 fvar' does NOT prove the artist did NOT use a variable font (remains 未证实)" ✓. No font files in tree; PNG/SVG built from stdlib geometry only.

## Check 4 — E2/E3/active boundaries: CLEAN

- Every promotion-adjacent sentence in README.md/RESULT.md/config.json/receipt.json/run_evidence.json is a **negation** ("Seed stays E1; no E2/E3/active promotion"; `no_e2_e3_active_change: true`).
- Candidate-hypothesis framing throughout; `receipt.json.claims` = 2× `observation/supported`; `review: null` (not self-accepted); `spawns_allowed: false`.
- Parent `state.md` byte-unchanged: current sha256 `3586aea0…` == hash declared in prototype `receipt.json.input_hashes` ("parent, preserved") ✓.

## Check 5 — verify-receipt.py: TOOL ABSENT; equivalent validation PASS

`verify-receipt.py` / `receipt.schema.json` are **not present anywhere on this machine** (searched repo, RUN_ROOT, `<home>/.dwgx`, `<private-source-tree>`); the `<package>/` path referenced in README/verify-receipt.out no longer exists locally → the literal "exit 0" tool rerun is [UNVERIFIED] as a command execution.

Equivalent independent validation performed instead (all on raw bytes):
- Structural: `schema_version 1.0`, ids present, `status=submitted`, `author_actor_id=SeedDepsRevisit`, `review=null`, `human_review.status=not_applicable`, `execution.receipt_sha256` == sha256(`runner_receipt.json`) ✓.
- **24/24 artifact hashes** + **4/4 input_hashes** recomputed → match; claim `source_refs.retrieved_bytes_sha256` bindings → match ✓.
- Stored `verify-receipt.out`: `ok: true`, `errors: []`, `EXIT_CODE=0` (author-attested, not re-executed — see above).

## Non-material nit

`checks.json` C6 field `pass: null` — pass verdict lives in `run_evidence.json.deterministic_rerun` (18/18 byte-identical, verified true by this reviewer). Cosmetic split only.
