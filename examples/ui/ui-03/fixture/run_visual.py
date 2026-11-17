#!/usr/bin/env python3
"""Fixture-level browser geometry, real input and live DOM checks, kept separate.

Pillow exact RGB pixel difference is NOT pixelmatch/perceptual similarity.
No model aesthetic or human judgement is produced. No global installation.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from cdp_util import ChromeSession


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mechanical_gate(layers):
    return all(layers.get(layer, {}).get("ok") is True for layer in ("geometry", "behavior", "semantics"))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fixture", type=Path, default=Path(__file__).with_name("index.html"))
    ap.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "evidence" / "browser-current")
    args = ap.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    report = {"schema_version": 1, "case": "UI-03", "started_utc": datetime.now(timezone.utc).isoformat(),
              "layers": {"geometry": {}, "behavior": {}, "semantics": {},
                         "model_aesthetic": {"status": "untested"}, "human": {"status": "pending_human"}},
              "ok": False, "scope": "same-process geometry + browser CDP input + live DOM contract; not aesthetic/WCAG/user-goal approval"}
    exit_code = 2
    try:
        from PIL import Image, ImageChops
        import PIL
        fixture = args.fixture.resolve()
        report["source_hashes"] = {"fixture/index.html": digest(fixture),
            "fixture/component.js": digest(fixture.with_name("component.js")),
            "fixture/run_visual.py": digest(Path(__file__)),
            "cdp_util.py": digest(ROOT / "cdp_util.py"), "chrome_util.py": digest(ROOT / "chrome_util.py")}
        report["fixture_override"] = fixture != Path(__file__).with_name("index.html").resolve()
        with ChromeSession() as chrome:
            report["environment"] = {"browser": chrome.version, "transport": chrome.transport,
                "python": sys.version.split()[0], "pillow": PIL.__version__}
            chrome.call("Emulation.setDeviceMetricsOverride", {"width": 320, "height": 200, "deviceScaleFactor": 1, "mobile": False})
            chrome.call("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": 0, "y": 0})
            chrome.navigate(fixture, "typeof window.UI03 !== 'undefined'")
            shots, pixels = [], {}
            for variant, name in (("default", "default"), ("hover", "hover"), ("dark", "dark"), ("default", "default-recheck")):
                chrome.evaluate("window.UI03.setVariant(" + json.dumps(variant) + ")")
                time.sleep(.2)  # settle the fixture's declared 80ms CSS transition
                blob = base64.b64decode(chrome.call("Page.captureScreenshot", {"format": "png", "fromSurface": True})["data"])
                path = output / (name + ".png")
                path.write_bytes(blob)
                with Image.open(path) as image:
                    pixels[name] = image.convert("RGB")
                shots.append({"path": path.name, "sha256": digest(path), "bytes": len(blob),
                              "width": pixels[name].width, "height": pixels[name].height})
            diffs = []
            for name in ("hover", "dark", "default-recheck"):
                if pixels[name].size != pixels["default"].size:
                    raise RuntimeError("screenshot size changed inside one process")
                difference = ImageChops.difference(pixels["default"], pixels[name])
                changed = sum(any(channel != 0 for channel in pixel) for pixel in difference.getdata())
                path = output / ("diff-default-" + name + ".png")
                difference.save(path)
                stable = name == "default-recheck"
                diffs.append({"comparison": "default_vs_" + name, "changed_pixels": changed,
                    "total_pixels": 64000, "expected": "identical" if stable else "different",
                    "ok": changed == 0 if stable else changed > 0,
                    "diff_path": path.name, "sha256": digest(path)})
            geometry = {"algorithm": "Pillow exact RGB channel difference; zero channel tolerance; not pixelmatch",
                "viewport": {"width": 320, "height": 200, "dpr": 1}, "screenshots": shots, "diffs": diffs,
                "ok": all((s["width"], s["height"]) == (320, 200) for s in shots) and all(d["ok"] for d in diffs)}
            report["layers"]["geometry"] = geometry

            behavior = []
            def rec(name, ok, actual):
                behavior.append({"id": name, "ok": bool(ok), "actual": actual})
            def state():
                return chrome.evaluate("window.UI03.getState()")
            def click():
                point = chrome.evaluate("(()=>{const r=document.getElementById('counter').getBoundingClientRect(); return {x:r.x+r.width/2,y:r.y+r.height/2};})()")
                for kind in ("mousePressed", "mouseReleased"):
                    chrome.call("Input.dispatchMouseEvent", dict(point, type=kind, button="left", clickCount=1))

            chrome.navigate(fixture, "typeof window.UI03 !== 'undefined'")
            click()
            rec("CDP_pointer_exactly_once", state()["count"] == 1 and state()["pressed"] is True, state())
            chrome.navigate(fixture, "typeof window.UI03 !== 'undefined'")
            chrome.key("Tab", "Tab", 9)
            focus = chrome.evaluate("(()=>{const e=document.activeElement,s=getComputedStyle(e);return {id:e.id,focusVisible:e.matches(':focus-visible'),outline:s.outlineStyle,width:parseFloat(s.outlineWidth)};})()")
            rec("CDP_Tab_reaches_visible_focus", focus["id"] == "counter" and focus["focusVisible"] and focus["outline"] != "none" and focus["width"] > 0, focus)
            chrome.key("Enter", "Enter", 13)
            rec("CDP_Enter_exactly_once", state()["count"] == 1, state())
            chrome.key(" ", "Space", 32)
            rec("CDP_Space_exactly_once", state()["count"] == 2, state())
            chrome.evaluate("window.UI03.setDisabled(true)")
            before = state()
            click()
            rec("CDP_disabled_pointer_noop", state() == before, state())
            chrome.key("Enter", "Enter", 13)
            rec("CDP_disabled_keyboard_noop", state() == before, state())
            report["layers"]["behavior"] = {"method": "CDP Input.dispatchMouseEvent/Input.dispatchKeyEvent; no JS dispatchEvent", "checks": behavior, "ok": all(b["ok"] for b in behavior)}
            live = chrome.evaluate("""(()=>{
              const e=document.getElementById('counter'),o=document.getElementById('count');
              const s=window.UI03.getState(),r=e.getBoundingClientRect(),cs=getComputedStyle(e);
              return {counterCount:document.querySelectorAll('#counter').length,tag:e.tagName.toLowerCase(),type:e.getAttribute('type'),role:e.getAttribute('role'),
                ariaPressed:e.getAttribute('aria-pressed'),name:e.getAttribute('aria-label'),expectedName:window.UI03.ACCESSIBLE_NAME,
                text:e.innerText.trim(),visible:r.width>0&&r.height>0&&cs.visibility==='visible'&&cs.display!=='none',
                disabled:e.disabled===true,pressed:s.pressed,stateDisabled:s.disabled,
                outputCount:document.querySelectorAll('#count').length,outputTag:o.tagName.toLowerCase(),live:o.getAttribute('aria-live'),outputText:o.innerText.trim(),stateCount:s.count};
            })()""")
            semantic_ok = (live["counterCount"] == 1 and live["tag"] == "button" and live["type"] == "button"
                and live["role"] in (None, "button") and live["name"] == live["expectedName"] and bool(live["name"])
                and live["ariaPressed"] == str(live["pressed"]).lower() and live["text"] == "Add one" and live["visible"]
                and live["disabled"] == live["stateDisabled"] and live["outputCount"] == 1 and live["outputTag"] == "output"
                and live["live"] == "polite" and live["outputText"] == str(live["stateCount"]))
            report["layers"]["semantics"] = {"method": "live DOM contract, not a full accessibility-tree audit", "actual": live, "ok": semantic_ok}
            report["ok"] = mechanical_gate(report["layers"])
            exit_code = 0 if report["ok"] else 1
    except Exception as exc:
        report["error"] = type(exc).__name__ + ": " + str(exc)
    report["finished_utc"] = datetime.now(timezone.utc).isoformat()
    report["exit_code"] = exit_code
    (output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"case": "UI-03", "ok": report["ok"], "exit_code": exit_code,
        "layers": {k: v.get("ok", v.get("status")) for k, v in report["layers"].items()}, "error": report.get("error")}, ensure_ascii=False))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
