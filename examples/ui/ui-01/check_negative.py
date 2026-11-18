#!/usr/bin/env python3
"""UI-01 NEGATIVE CONTROLS (research fixture, mechanical only).

The UI-01 fixture is a *state-machine simulation*, not a live AG-UI/SSE
consumer: it has no network event-injection endpoint. Its contract is encoded
in (a) the selftest trace driver inside fixture.html and (b) the assertions in
_check.py. These negatives test THAT contract:

  POSITIVE control : run the real _check.py on the pristine fixture -> exit 0.
  NEGATIVE control : copy fixture.html into an isolated temp dir, inject
      extra-advance / wrong-task / relabelled-truncation / altered-rule
      faults into the scripted selftest driver, and assert that _check.py FAILS
      (nonzero) on the tampered copy. If a fault were silently accepted, the
      check would be a false-positive green and this script exits nonzero.

All tampering happens on a TEMP COPY. The shipped fixture and _check.py are
never modified. Exit 0 = positive passed AND every negative was detected.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECK = HERE / "_check.py"
FIXTURE = HERE / "fixture.html"

lines: list[str] = []
def log(s=""):
    lines.append(str(s)); print(s)

def run_check(fixture_dir: Path) -> tuple[int, str]:
    """Run the real _check.py inside `fixture_dir` (fresh copy of harness)."""
    d = fixture_dir
    shutil.copy2(CHECK, d / "_check.py")
    # chrome_util lives one level up relative to the case dir; make one available.
    parent = d.parent
    shutil.copy2(HERE.parent / "chrome_util.py", parent / "chrome_util.py")
    env = __import__("os").environ.copy()
    r = subprocess.run([sys.executable, "-X", "utf8", "_check.py"],
                       cwd=str(d), capture_output=True, text=True,
                       encoding="utf-8", timeout=180, env=env)
    return r.returncode, r.stdout + "\n" + r.stderr

def make_case(tmp: Path, name: str, transform) -> Path:
    """Copy fixture + check into tmp/<name>/ and apply a text transform."""
    case_dir = tmp / name
    case_dir.mkdir(parents=True, exist_ok=True)
    src = FIXTURE.read_text(encoding="utf-8")
    case_dir.joinpath("fixture.html").write_text(transform(src), encoding="utf-8", newline="\n")
    return case_dir

def fail_if(cond, msg):
    if cond:
        log("FAIL " + msg)
        raise AssertionError(msg)
    log("  PASS " + msg)

def main() -> int:
    log("== UI-01 negative controls ==")
    log("fixture_contract=state-machine simulation (no live AG-UI/SSE transport)")

    # ---- POSITIVE control: pristine fixture must pass -----------------------
    with tempfile.TemporaryDirectory(prefix="ui01_pos_") as td:
        pos = Path(td) / "clean"
        pos.mkdir()
        shutil.copy2(FIXTURE, pos / "fixture.html")
        rc, out = run_check(pos)
        log("POSITIVE clean fixture _check exit=%d" % rc)
        tail = [l for l in out.splitlines() if l.startswith("RESULT:")]
        log("  " + (tail[-1] if tail else "(no RESULT line)"))
        fail_if(rc != 0, "pristine fixture must PASS the real check")

    # ---- NEGATIVE transforms on isolated copies -----------------------------
    # Each fault changes the state OBSERVED AT AN EXPECTED snapshot tag, so the
    # real _check.py (which asserts those tags) must detect it.
    # N1: Mutate the scripted selftest to advance T2 twice before its snapshot.
    # This is not transport-event deduplication; the real terminal no-op is
    # exercised separately by _check.py on the unchanged fixture.
    def dup_completion(src: str) -> str:
        needle = 'A.advance("T2"); snap("T2-after-1-advance");'
        assert needle in src
        return src.replace(
            needle,
            'A.advance("T2"); A.advance("T2"); snap("T2-after-1-advance");', 1)

    # N2: OUT-OF-ORDER event -- an event meant for T3 advances a different
    #     card first, so at the checked T3 tag the state is still 'running'.
    def out_of_order(src: str) -> str:
        needle = 'A.advance("T3"); snap("T3-after-1-advance");'
        assert needle in src
        return src.replace(
            needle,
            'A.advance("T1"); snap("T3-after-1-advance");', 1)

    # N3: RECONNECT / partial stream treated as SUCCESS -- the truncated-run
    #     step is relabelled 'completed', so the checked T3 terminal tag fails.
    def reconnect_as_success(src: str) -> str:
        needle = 'state:"stream-interrupted"'
        assert needle in src
        return src.replace(needle, 'state:"completed"', 1)

    # N4: UNKNOWN event / dropped contract rule -- remove the explicit
    #     "no synthesized RUN_FINISHED on truncation" rule the check asserts.
    def unknown_event(src: str) -> str:
        needle = "MUST NOT synthesize RUN_FINISHED"
        assert needle in src
        return src.replace(needle, "MAY synthesize RUN_FINISHED", 1)

    negatives = [
        ("N1_scripted_extra_advance", dup_completion, "T2-after-1-advance/T2 data-state=waiting-for-input"),
        ("N2_scripted_wrong_task", out_of_order, "T3-after-1-advance/T3 data-state=waiting-for-input"),
        ("N3_relabelled_truncation", reconnect_as_success, "T3-after-2-advances/T3 data-state=stream-interrupted"),
        ("N4_rule_text_altered", unknown_event, "fixture records AG-UI truncation rule"),
    ]
    with tempfile.TemporaryDirectory(prefix="ui01_neg_") as td:
        tmp = Path(td)
        for name, transform, expected_assertion in negatives:
            d = make_case(tmp, name, transform)
            rc, out = run_check(d)
            log("%s _check exit=%d" % (name, rc))
            tail = [l for l in out.splitlines()
                    if l.startswith("AssertionError") or l.startswith("RESULT:")]
            log("  " + (tail[-1] if tail else "(no result line)"))
            fail_if(rc != 1 or "AssertionError: " + expected_assertion not in out,
                    "%s must fail with its intended assertion, not a harness error" % name)

    log("")
    log("RESULT: ALL NEGATIVE CONTROLS DETECTED; positive control passed.")
    log("LIMITATION: this is a state-machine simulation. No live AG-UI/SSE")
    log("reconnect/duplicate-event handling over a network transport is claimed.")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError as e:
        print("NEGATIVE-CONTROL FAILURE: " + str(e))
        sys.exit(2)
