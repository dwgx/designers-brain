# Consumer evidence — historical chain and current failed C1 trial

## Current C1 closure trial

The new single attempt [C1-CLOSURE-20261118-001](../../experiments/consumer_skill/C1-closure/README.md) completed its protocol against frozen e0cfe964/ae4a28ae: A was sealed before the genuine hint-level-2 CUE; the second topic and measurements were locked before the held-out image observation. Both actual rendered PNGs were viewed. **The case failed; H1 is partial.** A reads as a pot/jar more than the intended cloth bag, and B loses too much vehicle form. The specific altered-outline negative was rejected; local green metrics did not override the visual failure. [Root review](../../experiments/consumer_skill/C1-closure/control/ROOT-REVIEW.md) and [final input delta](../../experiments/consumer_skill/C1-closure/FINAL-INPUT-DELTA.json) separate model review, original input identity, later changes and absent human acceptance.

Eight input blobs were identity-checked; six bodies/ranges were actually consumed. SKILL.md and LEARNING-INDEX.json were identity checks only. This is a bounded trial of the selected public painter learning route, not proof that the complete skill was consumed, the full library generalizes, or a human learned. The three reference family IDs were defined for this trial and do not establish unseen-by-model examples.

### Readability after local checks

Before applying a local style rule, identify essential object/material landmarks and its actual domain. After rendering, inspect whether the intended form remains readable; report a partial or failed output when it does not, even if numerical checks pass. A lost outline alone does not establish sfumato. This guidance is inferred from one failed case and is not a validated improvement. Preserve the failed attempt; a new independent study would be needed to test improvement.

## Historical P4R chain below

The following C1/C2/C3 records retain their original attempt, version and verdict. The old C1 block is a historical grouping/input gap, not a current claim that no reference grouping can be defined. The new trial above neither overwrites nor retroactively passes it.

Status language first: these are **work-process receipts for candidate `c35d748e…` / tree `fb24565b…`**, not independent acceptance, not publication, and not human approval. `human_review` stays `pending_human` everywhere.

## What this documents

The skill's consumer chain (task `SKILL-S06`) was run once against this exact candidate version, in three sealed stages (attempt id `P4R-20261117T123432`, staged 2026-11-17). Public projections of the non-private artifacts now live in [`experiments/consumer_skill/`](../../experiments/consumer_skill/README.md) so the chain is verifiable in-repo instead of only in release notes.

## Stage results

| Stage | Verdict | Meaning | Receipt |
|---|---|---|---|
| C1 | `holdout_status: blocked` | No real train/control holdout work family exists in public sources; recorded as blocked, not fabricated (`no_real_train_control_holdout_work_family_in_public_sources`) | `experiments/consumer_skill/C1/A-SEAL.json`, `CUE.json` |
| C2 | `case_verdict: success` (scoped) | Stage A unaided selection → sealed; Stage B seal-verified continuation with checker: **16 checks, 0 failed** on the positive fixture; negative fixtures fail as designed | `experiments/consumer_skill/C2/RESULT.md`, `receipt.json` |
| C3 | `case_verdict: success` (scoped) | Same shape with reuse-plan stage; all four required controls executed for this candidate version only | `experiments/consumer_skill/C3/RESULT.md` |

## Binding chain (sha256)

- C1 seal record: `A-SEAL.json` → candidate `c35d748e1cc9f23415fff0bf019a9c03234c421e`, tree `fb24565b02597057784cbeed23f70ba657711804`; `binding_sha256 15e418fcec6746756136fd954a4962f30a0c38f8d84b7408a7666569bfd280cc`; stage-A manifest `60447154d75996c1527f3876ba273134a57be6738eda37fb6612d2cc64a6bcca`.
- C2 goal `a2777c12cf9c3314050e07f962c95b5de506bdf3dbe2bac233dde2e9075d6444`; binding `075913f4571eecdc3194227d576cc4a37c76228e6c4bbb5a6d4fea9f44bfa351` (status=bound).
- C3 goal `4f524a5e9eccf8b987fcf0e4b022c49e46726c70c256af50ed294489fd03fdcd`; binding `60d9f31502fcb8eda0358995ec3833b94a784bff97bb6c8423d57f7533d58ded` (status=bound); C3 stage-A manifest `1df477a15f907c825e6fcf847a9a20e2879bad2b7984c976f60009d3fdede94b`.
- A/A determinism: the two decision outputs are identical to each other. Their recorded original CRLF SHA is `f9a833bd708dfa4810c248a6430d8c768652d624f74dca33a6e9a32f2dffa20b` ×2; the checked-in LF projection is `9a16370a87d32501f66177a5bc3c8ed5a0d313197900d78dd1beb9a7ce65db81` ×2. Exact LF-to-CRLF reconstruction recovers the original digest, and the decision diff remains empty.
- Full per-file hashes: `experiments/consumer_skill/SHA256SUMS.txt`.

## Negative-control exit table (fresh rerun in this checkout, 2026-11-18)

`cd experiments/consumer_skill/C2/stage-B` then `python -B check_runner.py --input-dir cases/<case> --out <file>`:

| Case | Exit | Output tail | Raw log |
|---|---|---|---|
| `positive` | 0 | `TOTAL: 16 checks, 0 failed` / `RESULT: PASS (exit=0)` | `runs_fresh_20261118/positive.stdout.txt` |
| `neg_role` | 1 | `TOTAL: 15 checks, 2 failed` / `RESULT: FAIL (exit=1)` | `runs_fresh_20261118/neg_role.stdout.txt` |
| `neg_budget` | 1 | `TOTAL: 16 checks, 1 failed` / `RESULT: FAIL (exit=1)` | `runs_fresh_20261118/neg_budget.stdout.txt` |
| `missing` | 2 | `ERROR: FileNotFoundError: missing required input file` (no silent pass) | `runs_fresh_20261118/missing.stdout.txt` |

Missing dependencies and broken inputs fail nonzero; a missing input can never pass silently.

## Honest limits

- Receipts record `requested=buddyfarm/hy4flash-free (from binding); served/provider model not independently observable -> unknown`. Model identity is not a measurement here.
- The three stage goal briefs and some raw stdout logs embed local absolute paths and are **not** redistributed; the private staging retains them. The pre-commit staging comparison was 32/32. Current Git bytes preserve 20 original digests and normalize 12 files only from CRLF to LF; all 32 match the e0 Git blobs. [Historical projection](../../experiments/consumer_skill/HISTORICAL32-PROJECTION.json) and the 44-entry checksum list state current and original identities separately.
- Success scope = the consumer work process for this candidate version. It does not claim full-library generality, external acceptance, or human aesthetic approval.
