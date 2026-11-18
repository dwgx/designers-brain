# C3 — RESULT

case_id: C3 · attempt_id: P4R-C3-20261117T123432 · task_id: SKILL-S06

## case_verdict: success (scoped)
Scope of success: Stage A unaided selection → Root A-SEAL → verified CUE → Stage B response with all four required controls actually executed, for THIS candidate version (`c35d748…` / tree `fb24565…`) and case C3 only. The consumer work process completed end to end. This is NOT a claim of external acceptance, publication, human aesthetic approval, or full-library generality; author cannot self-write `accepted`.

## Observation order (independent byte pointers, actual order)
1. **Goal** `C3-GOAL-filled.md` sha256 `4f524a5e9eccf8b987fcf0e4b022c49e46726c70c256af50ed294489fd03fdcd` — read in full first.
2. **Binding** `consumer-binding-C3.json` sha256 `60d9f31502fcb8eda0358995ec3833b94a784bff97bb6c8423d57f7533d58ded` — status=bound, all fields complete; 7 entrypoints each unique sha256+bytes.
3. **Candidate hard guards** — own-git HEAD `c35d748e1cc9f23415fff0bf019a9c03234c421e`, tree `fb24565b02597057784cbeed23f70ba657711804`, clean tree; all 7 entrypoint sha/bytes matched binding. No version drift.
4. **Stage A sealed (owner-written)** `A/unaided-selection.json` sha `45453470420d…`, `A/retrieval-log.md` sha `025c516d2778…`, `A/reuse-plan.md` sha `62d708174d61…`, `A/manifest.json` sha `1df477a15f907c825e6fcf847a9a20e2879bad2b7984c976f60009d3fdede94b`, `A/READY.json` (binds manifest sha). READY printed `READY C3 P4R-C3-20261117T123432 1df477a15f907c825e6fcf847a9a20e2879bad2b7984c976f60009d3fdede94b`. A frozen after READY; never modified.
5. **Cue polling** — CUE.json found at poll 12 (~220 s); no CUE content read before verification.
6. **Root A-SEAL** `A-SEAL.json` sha256 `3c7d6d29252fb01353df2234baff714c7da7f2d7d74115c2163f405598c2a935`; observed_at_utc `2026-11-17T12:40:05.145624Z`. Root independently re-read the 3 A content files with matching sha/bytes.
7. **CUE** `CUE.json` sha256 `ffbbe9a133c16c96636b851512ef9afca27ba811fce1555c2b93bd89bf5445f4`, issued_at_utc `2026-11-17T12:40:44.139172Z`, action=continue. Verification ran via a boolean-only check BEFORE instructions were printed: all identity/manifest/file-SHA/timestamp/candidate/entrypoint checks PASS; issued >= observed. Only then were instructions read.
8. **Stage B** — `B/verify_reuse.py` sha `4ab815111d4b…` authored and run with real argv (see receipt); all 4 controls PASS; `B/verify-output.json` sha `aef86bd33b6a…`; stdout/stderr captured; exit code 0 (deliberately not the PASS gate).

## Requests status
| Request item | Status |
|---|---|
| 10s MG animation, Blender-Python 3D-texture first preference | Route selected = card 01 3D质感 (only Blender card); satisfied by lawful reuse of preserved 10.000s 1920×1080/300f out.mp4 — **reused, not newly generated this run** |
| Verified status/conditions/evidence | Done: blender=conditional, preserved fields intact, 4 reuse SHAs verified |
| Compare alternative evidence-backed route + why not | Done: web10s conditional (02 液态) weaker + not Blender; card-01 web10s=unsupported exact limit stated |
| Byte-verify reuse, record decision/scope | Done: 4/4 matched; rights CC BY 4.0 / MIT; bounded evaluation reuse; no new-render claim |
| Controls (A/A, inflation, missing field, hash mismatch, exit0≠PASS) | Done: all PASS with expected/actual recorded |
| Missing evidence / unknown | Retained: current-runtime reproducibility, served/provider model, formal acceptance |

## Model / evidence boundaries
- requested_model = `buddyfarm/hy4flash-free` (from binding startup binding), requested_effort = `xhigh`. **served/provider model = unknown** (no model telemetry observed); a declared model is not a measured one.
- Results apply only to candidate commit `c35d748…` / tree `fb24565…` and case C3. They do not establish human learning, aesthetic acceptance, E2/E3 promotion, a working render service, or whole-library effect.
- No video was generated, no service probed, no API call made; no file, run, or video delivery fabricated.
- Author submits this result; author does not self-accept. External exact-SHA gate remains unfilled (`acceptance_binding.final_gate_locator_at_generation=null`, `self_acceptance=false`).

STATUS: DONE
