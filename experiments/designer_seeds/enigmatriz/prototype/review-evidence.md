# REVIEW EVIDENCE — SEED-PROTOTYPE-enigmatriz-REVIEW

Reviewer: ReviewGateSeedProto (glm-5.3-flash), independent of author SeedDepsRevisit. Review target: `staging/SEED-EXPERIMENT-enigmatriz/prototype/`. Repo `SOURCE@designers-brain (read-only source repo)` @ `f008952365a77e140cbda3f3959d43ef000f9a22` read-only. Reviewed 2026-11-15T14:26Z. No author file touched; all reviewer commands wrote only to a system temp dir (`<tmp>`).

## Verdict: ACCEPTED

All six assignment checks pass on recomputation from raw bytes/pixels. The prototype is an honest candidate-mechanism-hypothesis fixture with correct E1/E2/E3 boundaries.

## Check 1 — Dir manifest hash recomputed: MATCH

Recipe (recovered by this reviewer and verified on all three prototypes): lines `<relpath>  <sha256>` (two spaces), paths relative to `prototype/` with forward slashes, sorted by path, joined with `\n`, no trailing newline; sha256 of that text.

- Files in scope: **30** (8 top-level + 11 `outputs/` + 11 `rerun_20261115/`)
- Recomputed: `d12059faa2415f2d7c2ba2227408f44da08e6db6346582187945963c5a4fa4b8`
- Claimed: `d12059fa…` → **MATCH**.

Note: the three review-gate files this review adds are NOT part of the 30-file manifest (they did not exist when the claim was made); a future re-manifest must exclude `review-*` / `review-gate-*` files or expect a different hash.

## Check 2 — Deterministic rerun executed by this reviewer: BYTE-IDENTICAL

- `python -X utf8 build.py <tempdir>` (exit 0) → `diff -r` of my fresh run vs author `outputs/`: **IDENTICAL** (11/11 files).
- Author `rerun_20261115/` vs `outputs/`: **IDENTICAL** (11/11).
- `run_evidence.json.deterministic_rerun`: run1=run2=11 files, per-file sha256 bound in `receipt.json.artifacts[]` — all 17 artifact hashes recomputed by this reviewer, 17/17 match.

## Check 3 — Enigmatriz-specific measurements: ALL REPRODUCED FROM RAW OUTPUTS

- **Glyph-coverage ramp**: recomputed Pearson from `outputs/cell_ledger_normal.json` / `cell_ledger_reversed.json` (15 in-mask cells, cell mean luminance vs chosen glyph coverage):
  - normal **+0.879535** (claimed +0.8795) ✓
  - reversed **−0.899008** (claimed −0.8990) ✓
  - **sign flip confirmed** → the reversal CONTROL demonstrably inverts the measured ramp mapping. 15/15 in-mask glyphs changed between normal/reversed (claimed 15) ✓. Ramp itself is MEASURED (coverages 0.000…0.368, `assumed_at_darkest: false`), not assumed.
- **Outside-mask diff = 0**: recomputed pixel-wise (Pillow ImageChops) on `input_chart.png` / `render_normal.png` / `render_reversed.png` (120×60), mask rect 8,8–72,52: chart↔normal = 0, chart↔reversed = 0, normal↔reversed = 0 ✓ (out-of-mask only; C4: no out-mask cell touched).
- **Font declared by path+sha, NOT redistributed**: `config.json.font` declares `C:/Windows/Fonts/consola.ttf` + sha256 `cf00b507…db0179`; this reviewer hashed the actual file → matches. `rglob("*.ttf")` over the whole prototype tree → **NONE** (no font bytes copied). Fallback path exists but declared font was available.
- **MetricPilot reuse**: imported `staging/METRIC-PILOT/fixtures/metrics.py` (sha `7662e159…` matches declaration) and recomputed on the in-mask synthetic chart (65×45): `lap_var` variance **621.0324, N=2709** (claimed 621.03) ✓; `lum_hist` N=2925, bin_counts `[225,395,226,378,495,540,225,0,0,441]`, max_bin_share 0.184615, midtone 0.430769 — all match `checks.json` C7 exactly. Interfaces reused as pure numeric functions; no dossier threshold applied to any artwork ✓.

## Check 4 — E2/E3/active boundaries: CLEAN

- Every promotion-adjacent sentence in README.md/RESULT.md/config.json/receipt.json/run_evidence.json is a **negation** ("Seed stays E1; no E2/E3/active promotion"; "do NOT promote the seed (still E1)"; `no_e2_e3_active_change: true`).
- Framing is candidate-hypothesis throughout: `config.json.status = "candidate_mechanism_hypothesis_NOT_E3_NOT_validated_reproduction"`, labels `[LOCAL-MECHANISM-PROTOTYPE · NOT EVIDENCE · NOT E2/E3 · pending_human aesthetic judgement reserved]`, reversal explicitly a CONTROL, aesthetic judgement `pending_human`.
- Parent `state.md` byte-unchanged: current sha256 `5b648dd4…` == hash declared in prototype `receipt.json.input_hashes` ("parent, preserved") ✓.
- `spawns_allowed: false`, receipt `review: null` (not self-accepted), claims are 2× `observation/supported` only ✓.

## Check 5 — verify-receipt.py: TOOL ABSENT; equivalent validation PASS

`verify-receipt.py` is **not present anywhere on this machine** (searched `SOURCE@designers-brain (read-only source repo)`, campaign RUN_ROOT, `<home>/.dwgx`, `<private-source-tree>` for both the script and `receipt.schema.json` — the `<package>/` tree referenced in README/verify-receipt.out no longer exists locally). The tool rerun itself could not be executed → the literal "exit 0 ×3" rerun is [UNVERIFIED] as a command execution.

Equivalent independent validation performed instead (all on raw bytes):
- Structural: `schema_version 1.0`, goal/dedup/baseline ids present, `status=submitted`, `author_actor_id=SeedDepsRevisit`, `review=null`, `human_review.status=not_applicable`, `execution.receipt_sha256` == sha256(`runner_receipt.json`) ✓.
- **17/17 artifact hashes recomputed → match**; **4/4 input_hashes recomputed → match** (config, build.py, METRIC-PILOT metrics.py, parent state.md); claim `source_refs.retrieved_bytes_sha256` bindings → match ✓.
- Stored `verify-receipt.out` contains `ok: true`, `errors: []`, `EXIT_CODE=0` (author-attested, not re-executed — see above).

## Non-material nits

1. `checks.json` C6 field `pass: null` — the pass verdict lives in `run_evidence.json.deterministic_rerun` (11/11 byte-identical); verified true by this reviewer. Cosmetic split only.
2. `receipt.json.execution.started_at == ended_at` (identical timestamps) — multi-command batch recorded as one entry; per-file hash binding makes this non-material.
