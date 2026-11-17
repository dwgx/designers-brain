# Migration binding — BATCH 1 (PROVISIONAL)

> **rev2 (2026-11-16):** the ledger was regenerated to the current **297-dir** staging census (adds `MOTION-14` to held-back → 87), re-bound to `staging-keyfiles-v3.json` final manifest `6fbbc98b08b2feba…` and `migration-manifest.json` v2 sha16 `33c58b69f8f63ba9`. The final commit/tree SHA is bound externally in `staging/CANDIDATE-PREP/phase3/sealed/candidate-bytes-v3.json` (not quoted here, to avoid a self-referential hash). Counts: 194 stable / 87 held-back / 16 staging-only / 952 bound key-file hashes.

**PROVISIONAL under S09 LIFT. NOT release-ready. NOT an acceptance/promotion decision. NOT a content migration.**

`MIGRATION-BINDING-BATCH-1.json` is the **first migration batch** for the candidate tree: a labeled, hash-bound, per-path **migration intent ledger** for the STABLE GATED SET (194 staging dirs). It binds each path's target, status class, receipt status, and key-file SHA-256 (952 hashes sourced from `staging/CANDIDATE-PREP/phase3/sealed/staging-keyfiles-v3.json`, manifest `2f0c58cb88eddbf4…`).

## What this batch is / is not

- **IS:** the provisional per-path migration binding requested by Main's phase-4 dispatch — every stable path marked with its status class in `migration-manifest.json` v2, plus this machine-readable binding artifact in the candidate tree.
- **IS NOT:** the F01–F41 content diffs of `REGISTRY-INTEGRATION/preview/writer-plan.md` §3 (Phase C). Those still require Main's A/B rulings on F03/F05/F10/F12/F17/F20/F21 (C-06/C-07/N1/N3/C-09 etc.) and affected re-acceptance; **NOT supplied, NOT applied**. No repo knowledge/content file was edited by this batch.
- **IS NOT:** an acceptor/promotion run. `accept_receipt_v2.py` was **never invoked to promote**. The S09 gate's own recommendation states formal promotion of retrospective contracts is the coordinator's route.
- **IS NOT:** final binding. Per Main: "final binding at freeze after promotion pass."

## Authority (evidence)
- S09 lift: `staging/ACCEPT-FIX-REVIEW/review-gate-s09v3-receipt.json` — `verdict=ACCEPT/FINAL-GATE-PASS`, acceptor `b2f2f5d2a8ceb828f417723887c63d194b206d9f5a9469f4da354ef62ebfcbbb`.
- RebindAuditFix Class-A 20/76 metadata repair: `staging/ACCEPT-FIX/migration-gate-audit/RESULT.md` (23/23 PASS), `class-a-repair/REPORT.md` (20/20 chain).
- Seal version history: `staging/CANDIDATE-PREP/phase3/sealed/VERSION-INDEX.md` (v1/v2 retained, v3 current).
- Status classes / held-back list: `staging/CANDIDATE-PREP/phase3/migration-manifest.json` (v2; v1 preserved verbatim as `migration-manifest-v1.json`).

## Held back (86 dirs, explicitly NOT migrated)
STYLE-B4/B5 family (repairs in flight), CONFLICT-10..18, RULE-07/08/09, BASELINE-MAP, ROUTES-MAP, MOTION-03/04/05/07/09/10/13/15 (renders in flight). 16 further dirs are staging-only previews/scratch with no candidate target.

## Next (coordinator / repo-write lane, NOT this batch)
1. Main A/B rulings → Phase C F01–F41 content diffs (one writer, ordered pass per writer-plan.md §3).
2. Re-bind staging-keyfiles seal to current bytes at freeze.
3. Recompute README counts AFTER migration (`tools/check_library_counts.py`), G7 whole-tree scan, independent G8 binding of the final commit/tree.
4. No push/force/PR/tag before those gates.
