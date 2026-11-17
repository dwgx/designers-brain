#!/usr/bin/env python3
"""Real CDP composition / Tab / exactly-one-submit fixture check.

Browser input via Input.*; not an OS IME candidate-window test. Historical
receipt and original IME JSON are retained under evidence/history/. This run
writes fresh source-bound evidence, including failure instead of stale green.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from cdp_util import ChromeSession


def harness_gate(ev):
    """Unknown observations remain unknown and fail this bounded contract."""
    return (all(type(ev.get(key)) is int for key in ("sendCountDuringComposition", "sendCountAfterComposition", "sendDeltaAfterComposition"))
            and ev.get("compositionStartFired") is True
            and ev.get("compositionEndFired") is True
            and ev.get("enterDuringComposition_isComposing") is True
            and ev.get("enterAfterComposition_isComposing") is False
            and ev.get("compositionStateEnded") is True
            and ev.get("sendCountDuringComposition") == 0
            and ev.get("sendCountAfterComposition") == 1
            and ev.get("sendDeltaAfterComposition") == 1
            and ev.get("resetControlPassed") is True
            and ev.get("tabFocusPassed") is True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fixture", type=Path, default=HERE / "fixture.html")
    ap.add_argument("--output", type=Path, default=HERE / "evidence" / "ime_cdp_evidence.json")
    args = ap.parse_args()
    ev = {"method": "CDP Input.imeSetComposition + Input.dispatchKeyEvent",
          "realBrowser": False, "isSyntheticJsKeydown": False, "harnessGate": False,
          "recordedUtc": datetime.now(timezone.utc).isoformat(),
          "fixtureSha256": hashlib.sha256(args.fixture.read_bytes()).hexdigest(),
          "driverSha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "supportHashes": {name: hashlib.sha256((HERE.parent / name).read_bytes()).hexdigest()
                            for name in ("cdp_util.py", "chrome_util.py")},
          "untested": ["OS-native CJK IME / candidate window", "locale-specific IME quirks", "human aesthetic judgement"]}
    exit_code = 2
    try:
        with ChromeSession() as chrome:
            ev.update(realBrowser=True, userAgent=chrome.version.get("userAgent"),
                      browserVersion=chrome.version, transport=chrome.transport)
            chrome.navigate(args.fixture, "typeof window.__ui02 !== 'undefined'")
            chrome.evaluate("window.__ui02.reset()")
            focus = []
            for _ in range(4):
                chrome.key("Tab", "Tab", 9)
                focus.append(chrome.evaluate("document.activeElement.id"))
            focus_style = chrome.evaluate("(()=>{const e=document.activeElement,s=getComputedStyle(e);return {id:e.id,focusVisible:e.matches(':focus-visible'),outline:s.outlineStyle,width:parseFloat(s.outlineWidth)};})()")
            ev["tabSequenceObserved"] = focus
            ev["focusObserved"] = focus_style
            ev["tabFocusPassed"] = (focus == ["field-name", "field-email", "toolbar-bold", "compose"]
                                    and focus_style["focusVisible"] and focus_style["outline"] != "none" and focus_style["width"] > 0)
            if not ev["tabFocusPassed"]:
                raise AssertionError("real Tab path did not reach compose with visible focus")

            # Prime once through real input, then reset on the SAME page. The old
            # reset only changed a window mirror and would produce count=2 later.
            chrome.key("Enter", "Enter", 13)
            before_reset = chrome.evaluate("window.__ui02.getSendCount()")
            chrome.evaluate("window.__ui02.reset()")
            after_reset = chrome.evaluate("window.__ui02.getSendCount()")
            ev["resetBefore"] = before_reset
            ev["resetAfter"] = after_reset
            ev["resetControlPassed"] = before_reset == 1 and after_reset == 0

            def arm(key):
                chrome.evaluate("window." + key + "=null;document.getElementById('compose').addEventListener('keydown',e=>{window." + key + "={isComposing:e.isComposing,key:e.key,keyCode:e.keyCode};},{once:true,capture:true});")
            chrome.call("Input.imeSetComposition", {"text": "nihao", "selectionStart": 5, "selectionEnd": 5})
            chrome.call("Input.imeSetComposition", {"text": "ni hao", "selectionStart": 6, "selectionEnd": 6})
            arm("__capDuring")
            chrome.key("Enter", "Enter", 13)
            during = chrome.evaluate("window.__capDuring")
            send_during = chrome.evaluate("window.__ui02.getSendCount()")
            chrome.call("Input.insertText", {"text": "你好"})
            time.sleep(.1)
            ended = chrome.evaluate("window.__ui02.isComposing()")
            starts = chrome.evaluate("window.__ui02.getCompStart()")
            ends = chrome.evaluate("window.__ui02.getCompEnd()")
            arm("__capAfter")
            chrome.key("Enter", "Enter", 13)
            after = chrome.evaluate("window.__capAfter")
            send_after = chrome.evaluate("window.__ui02.getSendCount()")
            if type(send_during) is not int or type(send_after) is not int:
                raise AssertionError("missing/noninteger send counts")
            ev.update(compositionStartFired=starts >= 1, compositionEndFired=ends >= 1,
                enterDuringComposition_isComposing=(during or {}).get("isComposing"),
                enterDuringComposition_keyCode=(during or {}).get("keyCode"),
                enterAfterComposition_isComposing=(after or {}).get("isComposing"),
                compositionStateEnded=ended is False,
                sendFiredDuringComposition=send_during != 0,
                sendFiredAfterComposition=send_after - send_during == 1,
                sendCountDuringComposition=send_during, sendCountAfterComposition=send_after,
                sendDeltaAfterComposition=send_after - send_during,
                capturedKeydownDuring=during, capturedKeydownAfter=after,
                fixtureEventLog=chrome.evaluate("window.__ui02.eventLog()"))
            ev["harnessGate"] = harness_gate(ev)
            exit_code = 0 if ev["harnessGate"] else 1
    except Exception as exc:
        ev["error"] = type(exc).__name__ + ": " + str(exc)
    ev["exitCode"] = exit_code
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(ev, ensure_ascii=False, indent=2), encoding="utf-8")
    print("HARNESS_GATE=" + ("PASS" if ev["harnessGate"] else "FAIL"))
    print(json.dumps({k: ev.get(k) for k in ("sendCountDuringComposition", "sendCountAfterComposition", "sendDeltaAfterComposition", "enterAfterComposition_isComposing", "tabFocusPassed", "resetControlPassed", "error")}, ensure_ascii=False))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
