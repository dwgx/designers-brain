#!/usr/bin/env python3
"""Run the established comment/div and removed-name controls on isolated copies.

Default: real Node/static checks. --browser additionally requires the real CDP
driver to PASS the pristine fixture and FAIL each semantic mutant with exit 1
and an explicit failed semantic layer. An environment exit 2 never counts as a
successful negative control.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIX = HERE / "fixture"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--browser", action="store_true")
    ap.add_argument("--output", type=Path, default=HERE / "evidence" / "negative-current")
    args = ap.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    html = (FIX / "index.html").read_text(encoding="utf-8")
    tag = re.search(r'<button\b[^>]*>Add one</button>', html, re.S).group()
    div = html.replace(tag, tag.replace('<button', '<div', 1).replace('</button>', '</div>'))
    div = div.replace('<body data-variant="default">', '<body data-variant="default">\n<!-- preserved example: ' + tag + ' -->')
    cases = [("positive", html), ("comment_div", div),
             ("missing_name", html.replace('aria-label="Add one to the counter"', ''))]
    rows = []
    env = os.environ.copy()
    env["UI_PYTHON"] = sys.executable
    for name, text in cases:
        with tempfile.TemporaryDirectory(prefix="ui03-negative-") as temp:
            temp = Path(temp)
            fixture = temp / "index.html"
            fixture.write_text(text, encoding="utf-8")
            shutil.copy2(FIX / "component.js", temp / "component.js")
            run = subprocess.run(["node", str(FIX / "run_checks.js"), "--html", str(fixture)],
                                 capture_output=True, text=True, encoding="utf-8", timeout=30, env=env)
            static = json.loads(run.stdout)
            expected = 0 if name == "positive" else 1
            ok = run.returncode == expected
            if name != "positive":
                ok = ok and any(not s["ok"] for s in static["semantics"])
            row = {"case": name, "static_exit": run.returncode, "static": static, "ok": bool(ok)}
            if args.browser:
                out = args.output / name
                real = subprocess.run([sys.executable, "-B", str(FIX / "run_visual.py"),
                    "--fixture", str(fixture), "--output", str(out)], capture_output=True,
                    text=True, encoding="utf-8", timeout=120, env=env)
                report = json.loads((out / "report.json").read_text(encoding="utf-8"))
                row["browser_exit"] = real.returncode
                row["browser_report"] = name + "/report.json"
                row["ok"] = row["ok"] and real.returncode == expected
                if name != "positive":
                    row["ok"] = row["ok"] and report.get("layers", {}).get("semantics", {}).get("ok") is False
            rows.append(row)
    result = {"browser_executed": args.browser, "cases": rows, "ok": all(r["ok"] for r in rows)}
    (args.output / "controls.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"ok": result["ok"], "browser_executed": args.browser,
                      "cases": [{k: r[k] for k in ("case", "static_exit", "ok")} for r in rows]}))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
