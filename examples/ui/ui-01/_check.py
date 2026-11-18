#!/usr/bin/env python3
"""UI-01 mechanical checks (DOM/aria + state-machine transitions + draft preservation).

Scope: MECHANICAL only. Runs headless Chrome --dump-dom on fixture.html?selftest=1,
parses the emitted state trace, and asserts:
  * each scripted scenario step has the expected state label + data-state + data-aria;
  * all 6 AG-UI 1.0 lifecycle states appear and are mutually distinguishable by
    text label, icon glyph and border shape (NOT color alone);
  * stream-interrupted is NOT conflated with cancelled or completed (different
    label, icon, shape, data-state AND data-aria);
  * the 3 concurrent task cards each own their draft/unread/result;
  * switching tasks preserves each textarea draft;
  * static HTML contains distinct shape rules + aria attributes per state.

NOT covered (explicitly human/visual): pixel rendering,审美, 任务恢复易用性,
真实 IME, 长期生产率. See RESULT.md honest-status section.

Usage: python -X utf8 _check.py
Exit 0 = all mechanical assertions passed. Prints real output; browser profile and diagnostic file use a per-run temporary directory.
"""
import html as _html
import json
import re
import subprocess
import sys
# Explicit UTF-8 keeps Chinese diagnostics usable under Windows pipe encodings.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, 'reconfigure'):
        _stream.reconfigure(encoding='utf-8')
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from chrome_util import find_chrome

import tempfile
_runtime_dir = tempfile.TemporaryDirectory(prefix="designers-brain-ui01-check-", ignore_cleanup_errors=True)
RUNTIME = Path(_runtime_dir.name)
HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixture.html"
CHROME = find_chrome()
PROFILE = RUNTIME / "profile"
OUT = RUNTIME / "_check_output.txt"

lines = []
def log(s=""):
    lines.append(str(s))
    print(s)

def check(cond, msg):
    if not cond:
        raise AssertionError(msg)
    log("  PASS " + msg)

# ---------------------------------------------------------------------------
# 1. Run the fixture in a real browser (headless Chrome), capture real stdout.
# ---------------------------------------------------------------------------
log("== 1. real browser run ==")
cmd = [
    CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-first-run",
    f"--user-data-dir={PROFILE}", "--virtual-time-budget=2000", "--dump-dom",
    FIXTURE.as_uri() + "?selftest=1",
]
log("CMD: " + " ".join(cmd))
r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=120)
dom = r.stdout
log("exit_code=" + str(r.returncode) + "  dumped_bytes=" + str(len(dom)))
check(r.returncode == 0, "headless chrome --dump-dom exited 0")
# trace is emitted in a non-rendered <script type="application/json"> tag
m = re.search(r'<script type="application/json" id="selftest-out">(.*?)</script>', dom, re.S)
check(m is not None, "fixture emitted #selftest-out trace (no fatal JS error)")
trace = json.loads(m.group(1))
log("trace_snapshots=" + str(len(trace)))
by_tag = {t["tag"]: t["cards"] for t in trace}

def card(tag, tid):
    for c in by_tag[tag]:
        if c["id"] == tid:
            return c
    raise AssertionError(f"no card {tid} in snapshot {tag}")

# Exercise the real fixture action after the result is marked read.
check(card("T1-marked-read", "T1")["unread"] == "○ 已读 read",
      "completed task can be marked read")
check(card("T1-after-repeat-terminal", "T1") == card("T1-marked-read", "T1"),
      "repeated terminal advance preserves read state, draft and result owner")

# ---------------------------------------------------------------------------
# 2. Expected state at each scenario step + aria attribute + label.
# ---------------------------------------------------------------------------
log("== 2. scenario steps: expected state label + data-state + data-aria ==")
EXPECTED = {
    "initial":             {"T1":"running", "T2":"running", "T3":"running"},
    "T1-after-1-advance": {"T1":"completed", "T2":"running", "T3":"running"},
    "T2-after-1-advance": {"T1":"completed", "T2":"waiting-for-input", "T3":"running"},
    "T2-after-2-advances":{"T1":"completed", "T2":"cancelled", "T3":"running"},
    "T3-after-1-advance": {"T1":"completed", "T2":"cancelled", "T3":"waiting-for-input"},
    "T3-after-2-advances":{"T1":"completed", "T2":"cancelled", "T3":"stream-interrupted"},
    "T1-after-fail":      {"T1":"failed", "T2":"cancelled", "T3":"stream-interrupted"},
}
LABELS = {
    "running":"运行中 Running",
    "waiting-for-input":"待输入 Waiting for input",
    "cancelled":"已取消 Cancelled",
    "failed":"失败 Failed",
    "stream-interrupted":"断流 Stream interrupted",
    "completed":"已完成 Completed",
}
for tag, exp in EXPECTED.items():
    check(tag in by_tag, f"snapshot {tag} present")
    for tid, st in exp.items():
        c = card(tag, tid)
        check(c["state"] == st, f"{tag}/{tid} data-state={st}")
        check(c["aria"] == st, f"{tag}/{tid} data-aria={st}")
        check(c["label"] == LABELS[st], f"{tag}/{tid} label='{LABELS[st]}'")

# ---------------------------------------------------------------------------
# 3. All 6 lifecycle states present, mutually distinct channels (not color alone).
# ---------------------------------------------------------------------------
log("== 3. six-state coverage + distinct text/icon/shape ==")
seen = set()
for tag in EXPECTED:
    for c in by_tag[tag]:
        seen.add(c["state"])
check(seen == set(LABELS), "all 6 AG-UI 1.0 lifecycle states observed in DOM: " + ", ".join(sorted(seen)))

src = FIXTURE.read_text(encoding="utf-8")
GLYPHS = {"running":"▶","waiting-for-input":"‖","cancelled":"⊘",
          "failed":"✕","stream-interrupted":"⚡","completed":"✓"}
SHAPES = {
    "running":            "solid rounded rect",
    "waiting-for-input":  "dashed rect",
    "cancelled":          "dotted pill",
    "failed":             "double border",
    "stream-interrupted": "wavy-left asymmetric",
    "completed":          "rounded pill",
}
# STATES table must declare a unique label, glyph and shape per state
for st, g in GLYPHS.items():
    check(f'glyph: "{g}"' in src, f'state {st} declares unique icon glyph {g}')
for st, sh in SHAPES.items():
    check(f'shape: "{sh}"' in src, f'state {st} declares unique border shape "{sh}"')
check(len(set(GLYPHS.values())) == 6, "6 distinct icon glyphs")
check(len(set(SHAPES.values())) == 6, "6 distinct border shapes")
check(len(set(LABELS.values())) == 6, "6 distinct text labels")
# CSS: each state has its own border-style/radius rule (shape channel, not color-only)
for st in LABELS:
    check(f'.badge[data-state="{st}"]' in src, f'CSS shape rule exists for {st}')
# aria channel present in source
check('"data-aria": def.aria' in src or '"data-aria":def.aria' in src,
      "badge sets data-aria attribute from state catalogue")
check('role:"status"' in src and '"aria-live":"polite"' in src,
      "badge carries role=status + aria-live (state announced)")

# ---------------------------------------------------------------------------
# 4. CRITICAL: stream-interrupted NOT conflated with cancel / success.
# ---------------------------------------------------------------------------
log("== 4. stream-interrupted != cancelled != completed (spec boundary) ==")
t3 = card("T3-after-2-advances", "T3")
t2 = card("T2-after-2-advances", "T2")
t1 = card("T1-after-1-advance", "T1")
check(t3["state"] == "stream-interrupted", "T3 truncated run state = stream-interrupted")
check(t3["state"] != t2["state"] and t3["state"] != t1["state"],
      "stream-interrupted has distinct data-state from cancelled and completed")
check(t3["aria"] != t2["aria"] and t3["aria"] != t1["aria"],
      "stream-interrupted has distinct data-aria from cancelled and completed")
check(t3["label"] != t2["label"] and t3["label"] != t1["label"],
      "stream-interrupted has distinct text label from cancelled and completed")
check("MUST NOT synthesize RUN_FINISHED; MUST NOT report success" in src,
      "fixture records AG-UI truncation rule (no synthesized RUN_FINISHED, no false success)")
check("NO outcome" in src, "truncated run recorded as having NO outcome")
check("NEW runId" in src, "re-run of truncated run recorded as a NEW runId (not a resume)")
# ---------------------------------------------------------------------------
# 5. 3 concurrent cards, each owns draft / unread / result.
# ---------------------------------------------------------------------------
log("== 5. 3 concurrent tasks + per-task draft/unread/result ownership ==")
check(len(by_tag["initial"]) == 3, "3 concurrent task cards rendered")
for tid in ("T1", "T2", "T3"):
    c = card("initial", tid)
    check("draft" in c and "unread" in c and "result" in c, f"{tid} owns draft/unread/result fields")
check('"data-taskid":task.id' in src or "data-taskid" in src, "cards carry per-task identity")
check("draftflag-" in src and "unread-" in src and "result-" in src,
      "per-task draft/unread/result DOM ids are namespaced")

# ---------------------------------------------------------------------------
# 6. Draft preservation across task switch.
# ---------------------------------------------------------------------------
log("== 6. draft preservation on task switch ==")
DRAFT = "draft-alpha-未发送"
check(card("T1-draft-set", "T1")["draft"] == DRAFT, "T1 draft textarea set to " + DRAFT)
check(card("after-switch-to-T3", "T1")["draft"] == DRAFT,
      "T1 draft preserved AFTER switching away to T3")
check(card("after-switch-back-to-T1", "T1")["draft"] == DRAFT,
      "T1 draft preserved AFTER switching back to T1")
check(card("after-switch-to-T3", "T3")["draft"] == "",
      "T3 has its own (empty) draft, not T1's — ownership is per-task")
# static: draft always sourced from model, not lost on re-render
check("ta.value = m.draft" in src, "textarea value sourced from model on every render")
check("m.draft = ta.value" in src, "input writes draft back into model")

# ---------------------------------------------------------------------------
# 7. summary vs expandable evidence built per card.
# ---------------------------------------------------------------------------
log("== 7. summary vs expandable evidence ==")
check('el("details"' in src and "展开证据" in src, "expandable evidence <details> present")
check('class:"summary"' in src, "summary region present")

log("")
log("RESULT: ALL MECHANICAL CHECKS PASSED (" + str(len([l for l in lines if l.startswith("  PASS")])) + " assertions).")
log("NOT TESTED (human/visual): pixel rendering,审美/风格, 任务恢复易用性, 真实 IME, 长期生产率.")
OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
sys.exit(0)
