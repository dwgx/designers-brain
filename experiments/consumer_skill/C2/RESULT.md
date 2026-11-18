# RESULT — C2 / P4R-C2-20261117T123432

## Verdict

`case_verdict: success` (bounded scope: the sealed Stage A artifact plus the Stage B seal-verified continuation all completed with real, recorded evidence). This is a WORK-PROCESS verdict for this candidate/attempt only. It is NOT independent acceptance, NOT a reviewer verdict, NOT publication, and NOT a claim of human learning/aesthetic/full-library effect.

## Independent byte pointers and real observation order

1. Goal read + hard guards (before any knowledge read):
   - Goal file sha256 `a2777c12cf9c3314050e07f962c95b5de506bdf3dbe2bac233dde2e9075d6444` (matches task).
   - Binding `staging/P4R-ROOT-CTRL/.../consumer-binding-C2.json` sha256 `075913f4571eecdc3194227d576cc4a37c76228e6c4bbb5a6d4fea9f44bfa351`; status=bound; case/attempt/commit/tree match Goal.
   - Candidate repo (git -C candidate): HEAD `c35d748e1cc9f23415fff0bf019a9c03234c421e`, tree `fb24565b02597057784cbeed23f70ba657711804`, `status --porcelain` empty.
   - All 8 public entrypoints recomputed sha256+bytes == binding; nothing null/empty/placeholder.
2. Stage A unaided work (owned dir `staging/P4R-CONSUMERS/P4R-C2-20261117T123432/A/`), files created without overwriting:
   - `unaided-selection.json` sha256 `7a39a8049b2afdc4f7cc3ab31c9934a726a6f43a4c2c823f1675b110d673565f` (10581 B)
   - `retrieval-log.md` sha256 `7c6a1f9cabf958d35067906e98cfd5135745928d93b1167e70e4e3ccc4301e40` (7146 B)
   - `layout.json` sha256 `a63161154c1bd631a1b77268ac13afb1949572b2e7f00e1e57a39400a7230f52` (3328 B)
   - `layout.html` sha256 `fe9f83c85435619a4bd1596dce755d7ed811aa520472cff8ec65fbd6ae2af5e0` (4022 B)
   - `check_layout.py` sha256 `c68dcf16f7d6b0dedeb9ed680c9f53143c75275ed0443138f9064a31233cb3dd` (5894 B)
   - `check-output.json` sha256 `7fcb4e14904f1c3f703bc1f564b725ad8acdc9c26a97c4d763ebb304c17a0051` (3114 B) — genuine run, exit 0, 14/14 PASS
   - `manifest.json` sha256 `fd1c777075d8a03706b2df7ac1508e2c822828bc990e929323db5f9b90a6993a` (1707 B; lists the 6 above, excludes itself)
   - `READY.json` sha256 `d78c53b74b82bb6a3fb72aa40ae36c31f55dc994b01532ff4a9cd0b8916e8509` (733 B)
   - Printed exactly: `READY C2 P4R-C2-20261117T123432 fd1c777075d8a03706b2df7ac1508e2c822828bc990e929323db5f9b90a6993a`
   - Observation: A is immutable history after READY. At final check, all 6 A files still match manifest (A_STILL_SEALED=True).
3. Root seal + cue (read-only from Root Control dir):
   - CUE detected at poll 7 (≤20 s/poll, under 480 s/count limits); first 6 polls absent. CUE sha256 `bda52a67b260498858cacf5b511365bf23de48dea20c4a30313901b15348bce2`.
   - A-SEAL sha256 `fad3f4527447f5b1450c918fce557b73de55690f73f94680d59910bf1f12c72d`.
   - Verification script (run BEFORE reading instructions) returned 30/30 PASS and `VERIFY_OK`: A-SEAL byte SHA == cue.root_seal_sha256; identity/commit/tree/binding/manifest SHA all match; three-way A-file SHA (READY/manifest/A-SEAL) all match; observed/issued both tz-aware UTC with issued `2026-11-17T12:41:48Z` >= sealed observation; candidate HEAD/tree/clean still match; 8 public entrypoints still bound. cue.instructions was never printed before this passed.
   - CUE action `continue`; instructions covered: threshold provenance, run positive/negative/missing with stdout↔exit consistency, text-vs-image counter-example separation (no image_seen), optional bounded reference (not taken), static-zero-flicker vs rendered-timing limitation, A/A + break test.
4. Stage B (owned dir `B/`), all writes after the verified cue:
   - `check_runner.py` sha256 `46d9635503aa4ce0a194343254dc86334d65c952f55d5ce7213337bea12d42fb` (7575 B) — A-identical predicates, correct pass/fail exit, break predicates. I/O confined to supplied `--input-dir` and `--out`; no network/subprocess/image/A writes.
   - `response.md` sha256 `19e77114dc6a48318a20033eb7526700c6bb4bcd3dce0661c8eb754f469a1b61` (10579 B) — threshold provenance table + all run results + channel labels + limitation.
   - Case inputs: `cases/positive/layout.json` sha `5938c6ac…c7c99`, `cases/neg_role/layout.json` sha `3633d41f…e132`, `cases/neg_budget/layout.json` sha `86a02b91…ebd1` (full SHAs in response §2 and B/runs stdout).
   - Run stdout/stderr SHAs are enumerated in `receipt.json` below. Every case had stderr 0 bytes.

## Completed / failed / missing / not-run

- Completed: hard guards; unaided A + READY seal; bounded cue polling + verified seal; Stage B provenance table; positive run (exit 0, PASS 16/16); two known-fault negatives (each exit 1, FAIL with matching text); missing-input case (exit 2, clean error, no silent pass); A/A repeat (identical decision lines, sha `f9a833bd708dfa4810c248a6430d8c768652d624f74dca33a6e9a32f2dffa20b`); break test (FAIL on ownership removal and budget overrun).
- Failed (expected, as counter-examples): neg_role and neg_budget — these are the intended failing inputs, not defects in the work.
- Missing/unavailable: no image-generation channel, no browser/capture harness, no human reader test. Recorded as limitations; not inferred into other channels.
- Not run: optional historical repair checker (CUE item 4, explicitly non-penalized to skip); no network probes/installs/large renders; no new case/experiment/API calls for waiting.

## Model / scope / boundaries

- requested_model (from binding): `buddyfarm/hy4flash-free`; requested_effort `xhigh`. served/provider model could NOT be independently observed in this environment -> `served_model: unknown`; the declared binding value is not presented as a measurement.
- Results apply only to candidate final_commit `c35d748e…` / tree `fb24565b…`, case C2, attempt `P4R-C2-20261117T123432`.
- The mechanism is a mechanical/declared salience-ownership contrast. It does not demonstrate real human learning, aesthetic acceptance, E2/E3 promotion, actual image-generation output, or full-library effect. Static zero-flicker is verified only at the source-structure level; rendered-timing flicker compliance is `[UNVERIFIED]` (no frames captured).
- The author submits this artifact; the author does not write or claim `accepted`.
