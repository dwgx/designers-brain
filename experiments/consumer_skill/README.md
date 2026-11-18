# Consumer skill evidence — historical chain and C1 closure trial

Public, explicitly normalized projections of the non-private artifacts of the SKILL-S06 consumer chain (attempt `P4R-20261117T123432`), so the chain can be verified from this repo instead of only from release notes. Narrative + binding hashes + fresh rerun table: [`docs/skill/consumer-evidence.md`](../../docs/skill/consumer-evidence.md).

## Current closure attempt

[C1-closure](C1-closure/README.md) is a separate frozen e0 attempt: protocol complete, case failed, H1 partial. Actual A/B PNGs, preregistered measurements, specific negative and independent Root review are published with an explicit privacy projection map. It does not alter the historical blocked C1 below.

## Historical layout

- `C1/` — blocked holdout: `A-SEAL.json` (seal record; candidate `c35d748e…` / tree `fb24565b…`), `CUE.json`. `holdout_status: blocked` — no real train/control holdout work family in public sources; recorded as blocked, not fabricated.
- `C2/` — `receipt.json`, `RESULT.md` (`case_verdict: success`, scoped work-process verdict); `stage-A/` unaided-selection artifacts (checker, layout, retrieval log); `stage-B/` `check_runner.py` + `cases/` (positive, neg_role, neg_budget, missing) + historical stderr logs + the A/A decision pair.
- `C3/` — `RESULT.md`, `cue-poll.log`, `stage-B/` `verify_reuse.py` + verify outputs.
- `SHA256SUMS.txt` — 44 explicitly listed historical and fresh-rerun files. The new C1 closure projection has its own PUBLIC-PROJECTION.json and current input-delta record.
- `C2/stage-B/runs_fresh_20261118/` — **fresh rerun outputs from this checkout (2026-11-18)**, not historical copies.

## Rerun

```bash
cd experiments/consumer_skill/C2/stage-B
python -B check_runner.py --input-dir cases/positive --out /tmp/pos.out   # exit 0, 16 checks 0 failed
python -B check_runner.py --input-dir cases/neg_role  --out /tmp/nr.out   # exit 1, 15 checks 2 failed
python -B check_runner.py --input-dir cases/neg_budget --out /tmp/nb.out  # exit 1, 16 checks 1 failed
python -B check_runner.py --input-dir cases/missing   --out /tmp/ms.out   # exit 2, missing input = no silent pass
```

Python 3 stdlib only. Fresh reruns 2026-11-18 reproduced all four exits (see `runs_fresh_20261118/`).

## What was excluded, and why

- `C1-GOAL-filled.md`, `C2-GOAL-filled.md`, `C3-GOAL-filled.md` — stage briefs embedding local absolute paths (private staging only).
- Historical `*_stdout.txt` run logs, `manifest.json` copies with absolute invocation paths, `_aa_run1/2.txt`, stage-b-response: same reason (local paths; the run facts they evidence are re-derivable by the rerun above, and the sealed decision outputs `_aa_decision1/2.txt` + diff are included).
- `A-SEAL.json` seals three C1 stage-A files (incl. `sketch-three-values.svg`) that remain in private staging; the seal record is included, the sealed media are not.

Before commit, the 32 staged evidence copies were byte-compared against their source files. In the checked-in Git version, 20 still match the recorded original SHA and 12 have only CRLF-to-LF normalization; all 32 remain byte-identical to the e0 Git blobs. [HISTORICAL32-PROJECTION.json](HISTORICAL32-PROJECTION.json) binds both hashes and the exact reconstruction. The current 44-entry checksum list verifies actual repository bytes. Receipts are `consumer_case_result_receipt_not_acceptance` — not acceptance, not publication, no human-aesthetic claim; `human_review` stays `pending_human`.

Fresh C2 log paths were redacted for publication; original and public hashes are distinguished in docs/audit/closure-20261118/runtime/PROJECTION-MANIFEST.json. The historical 32 source copies and decision outputs remain separate from these fresh logs.
