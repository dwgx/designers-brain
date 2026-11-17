#!/usr/bin/env python3
"""UI-02 A2 mechanical checks. Prints PASS/FAIL per assertion; exit 0 iff all pass.

Checks (each maps to a brief requirement):
  [T] DTCG JSON validates against the official 2025.10 format schema (draft-07),
      using a local referencing.Registry built from the schema's embedded $defs.
  [T] Alias resolution ORDER: chained alias action->brand->primary resolves to
      the explicit primary value; resolution happens AFTER resolver ordering.
  [T] Cycle detection: the cycle file is STRUCTURALLY schema-valid but the
      resolver MUST raise a circular-reference error naming the chain.
  [T] Resolver resolutionOrder override order + input validation.
  [F] Focus order: tab sequence keyboard-only completable + roving tabindex
      asserted from the real-browser DOM dump (fixture.html?selftest=1).
  [I] Composition flag gating: asserted in code (fixture) AND in real-browser
      test output captured via CDP Input.imeSetComposition (genuine composition).
  [CJK] CSS-implemented vs untested punctuation/禁则 rules recorded.

Run: python -X utf8 _check.py   (writes _check_output.txt)
"""
import html as _html
import hashlib
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

from jsonschema import Draft7Validator
from referencing import Registry, Resource
import dtcg_resolver as R

import tempfile
_runtime_dir = tempfile.TemporaryDirectory(prefix="designers-brain-ui02-check-", ignore_cleanup_errors=True)
RUNTIME = Path(_runtime_dir.name)
HERE = Path(__file__).resolve().parent
SCHEMA = HERE / "schema" / "dtcg-format-schema.json"
TOKENS = HERE / "tokens.tokens.json"
CYCLE = HERE / "tokens-cycle.tokens.json"
RESOLVER = HERE / "themes.resolver.json"
FIXTURE = HERE / "fixture.html"
OUT = RUNTIME / "_check_output.txt"

lines = []
def log(s=""):
    lines.append(str(s)); print(s)

_n = [0]
def check(cond, msg):
    _n[0] += 1
    if not cond:
        log("  FAIL " + msg)
        raise AssertionError(msg)
    log("  PASS " + msg)

# ---------------------------------------------------------------------------
log("== [T1] official DTCG 2025.10 format-schema validation ==")
schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
# Build a local registry from the schema's embedded $defs (each has an $id
# equal to the external $ref URL), so no network is needed at validation time.
defs = schema.get("definitions", {})
resources = []
for key, sub in defs.items():
    if isinstance(sub, dict) and sub.get("$id"):
        resources.append((sub["$id"], Resource.from_contents(sub)))
# The main format.json itself must also be in the registry.
registry = Registry().with_resources([(schema["$id"], Resource.from_contents(schema))] + resources)
validator = Draft7Validator(schema, registry=registry)

tokens = json.loads(TOKENS.read_text(encoding="utf-8"))
errs = sorted(validator.iter_errors(tokens), key=lambda e: list(e.path))
check(not errs, "tokens.tokens.json validates against official DTCG 2025.10 format.json"
      + (" (errors: " + "; ".join(e.message for e in errs[:3]) + ")" if errs else ""))

cycle_doc = json.loads(CYCLE.read_text(encoding="utf-8"))
cyc_errs = list(validator.iter_errors(cycle_doc))
check(not cyc_errs, "tokens-cycle.tokens.json is STRUCTURALLY schema-valid (aliases are opaque strings)"
      + (" (errors: " + "; ".join(e.message for e in cyc_errs[:3]) + ")" if cyc_errs else ""))

# ---------------------------------------------------------------------------
log("== [T2] alias resolution order + chained aliases (format 7.2.2) ==")
R.check_names_and_types(tokens)
resolved = R.resolve_all(tokens)
primary = resolved["color.primary"]
check(isinstance(primary, dict) and primary.get("hex") == "#0066cc",
      "color.primary explicit value is the base color object")
check(resolved["color.brand"] == primary,
      "color.brand = {color.primary} resolves to FULL $value of primary")
check(resolved["color.action"] == primary,
      "color.action = {color.brand} chained alias resolves through brand to primary")
check(resolved["color.text"] == resolved["color.ink"],
      "color.text = {color.ink} resolves correctly")
# Dimension alias
check(resolved["layout.control"] == resolved["size.controlHeight"],
      "layout.control = {size.controlHeight} dimension alias resolves")
# Resolution must NOT be guessable from value; type is declared (format 5.2.2)
types = dict(R.check_names_and_types(tokens))
check(types["color.action"] == "color",
      "alias token color.action keeps declared $type=color")

# ---------------------------------------------------------------------------
log("== [T3] cycle detection (format 7.2.3, resolver 6.3) ==")
got_cycle = None
try:
    R.resolve_all(cycle_doc)
except R.DTCGError as e:
    got_cycle = str(e)
check(got_cycle is not None, "cycle file triggers a DTCGError (not a successful resolution)")
check("circular reference" in (got_cycle or "").lower(),
      "error is a circular-reference error per format 7.2.3")
# chain a -> b -> c -> a is named in the message
check(all(x in (got_cycle or "") for x in ("loop.a", "loop.b", "loop.c")),
      "error names the full a->b->c->a chain ('affecting all tokens in the circular chain')")
# self loop too
got_self = None
try:
    R.resolve_alias(cycle_doc, "selfLoop.x")
except R.DTCGError as e:
    got_self = str(e)
check(got_self is not None and "circular" in got_self.lower(),
      "direct self-cycle selfLoop.x also detected")

# ---------------------------------------------------------------------------
log("== [T4] resolver resolutionOrder override + input validation (6.2/6.1/5.2) ==")
res = json.loads(RESOLVER.read_text(encoding="utf-8"))
# light + comfortable: defaults
flat, vals, eff = R.resolve_document(res, {})
check(eff == {"theme": "light", "density": "comfortable"},
      "empty inputs fall back to declared defaults (4.1.5.3)")
check(vals["color.ink"]["hex"] == "#1a1a1f",
      "theme=light yields light ink")
check(vals["size.controlHeight"]["value"] == 44,
      "density=comfortable yields 44px control height")
# dark + compact
flat2, vals2, eff2 = R.resolve_document(res, {"theme": "dark", "density": "compact"})
check(eff2 == {"theme": "dark", "density": "compact"}, "explicit inputs accepted")
check(vals2["color.surface"]["hex"] == "#121217",
      "theme=dark overrides base surface (resolutionOrder: theme later than base)")
check(vals2["size.controlHeight"]["value"] == 24,
      "density=compact overrides base 44px (resolutionOrder: density last)")
# alias is resolved AFTER flattening: color.action -> color.brand -> dark/hc brand
check(vals2["color.action"]["hex"] == "#0066cc",
      "color.action alias resolves to brand AFTER ordering (resolver 6.3), dark keeps brand")
flat3, vals3, _ = R.resolve_document(res, {"theme": "hc"})
check(vals3["color.brand"]["hex"] == "#ffff00",
      "theme=hc overrides brand (last modifier wins on conflict)")
check(vals3["color.action"]["hex"] == "#ffff00",
      "color.action chained alias re-resolves to the OVERRIDDEN brand (order before alias)")
# input validation failures
for bad, label in [({"nope": "x"}, "unknown modifier key"),
                   ({"theme": 1}, "non-string input value"),
                   ({"theme": "neon"}, "value not in contexts")]:
    thrown = None
    try:
        R.validate_inputs(res, bad)
    except R.DTCGError as e:
        thrown = str(e)
    check(thrown is not None, "resolver 6.1/5.2 rejects " + label)

# ---------------------------------------------------------------------------
log("== [F] focus path — real-browser DOM dump (keyboard-only + roving tabindex) ==")
CHROME = find_chrome()
PROFILE = RUNTIME / "profile"
url = FIXTURE.resolve().as_uri() + "?selftest=1"
cmd = [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-first-run",
       "--user-data-dir=" + str(PROFILE), "--virtual-time-budget=3000", "--dump-dom", url]
r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=120)
log("  chrome exit_code=" + str(r.returncode) + " dom_bytes=" + str(len(r.stdout)))
check(r.returncode == 0, "headless chrome --dump-dom exited 0")
m = re.search(r'<pre id="selftest-out">(.*?)</pre>', r.stdout, re.S)
check(m is not None, "fixture emitted #selftest-out (no fatal JS error)")
trace = json.loads(_html.unescape(m.group(1)))
log("  trace keys: " + ", ".join(sorted(trace.keys())))

check(trace.get("tabSequence") == ["field-name", "field-email", "toolbar-bold",
                                    "compose", "send", "open-dialog"],
      "tab sequence is complete & keyboard-only: every control reachable by Tab in DOM order"
      + " (toolbar is ONE tab stop; its items use roving tabindex per APG)")


check(trace.get("allReachableByKeyboard") is True,
      "keyboard-only completability asserted (every action has a Tab-reachable control)")
# roving tabindex: exactly one toolbar item has tabindex=0 at any time
roving = trace.get("rovingSnapshots", [])
check(len(roving) >= 3, "roving tabindex snapshots captured for each arrow-key step")
for i, snap in enumerate(roving):
    zeros = [it["id"] for it in snap["items"] if it["tabindex"] == 0]
    check(len(zeros) == 1, "roving step %d: exactly ONE toolbar item has tabindex=0" % i)
check(roving[0]["active"] == "toolbar-bold", "initial roving active = first item (APG)")
check(roving[1]["active"] == "toolbar-italic", "ArrowRight moves active to 2nd item")
check(roving[2]["active"] == "toolbar-underline", "ArrowRight wraps/moves to 3rd item")
check(trace.get("focusRestoredAfterDialog") is True,
      "focus returns to trigger after dialog close (APG persistence of focus)")
check(trace.get("targetSizeMinPx") == 24 and trace.get("focusRingWidthPx") == 2,
      "WCAG 2.5.8 (24x24 AA) + 2.4.13 (2px perimeter AAA) values wired from tokens")

# ---------------------------------------------------------------------------
log("== [I] composition gating — in-code assertion + real-browser CDP evidence ==")
fixture_src = FIXTURE.read_text(encoding="utf-8")
check("compositionstart" in fixture_src and "compositionend" in fixture_src
      and "isComposing" in fixture_src,
      "fixture registers compositionstart/end handlers and checks isComposing")
check("if (e.isComposing || composing) return;" in fixture_src
      or "e.isComposing || composing" in fixture_src,
      "send action is GATED by isComposing flag / composition session in keydown handler")
check("keyCode === 229" in fixture_src or "keyCode === 229 || e.isComposing" in fixture_src,
      "fixture also guards the legacy keyCode===229 IME-confirmation case")
# Real browser CDP evidence (produced by cdp_ime_test.py)
cdp = HERE / "evidence" / "ime_cdp_evidence.json"
check(cdp.is_file(), "ime_cdp_evidence.json present (real-browser CDP composition run)")
ev = json.loads(cdp.read_text(encoding="utf-8"))
check(ev.get("fixtureSha256") == hashlib.sha256(FIXTURE.read_bytes()).hexdigest(),
      "CDP evidence binds the current fixture bytes")
check(ev.get("driverSha256") == hashlib.sha256((HERE / "cdp_ime_test.py").read_bytes()).hexdigest(),
      "CDP evidence binds the current driver bytes")
check(all(ev.get("supportHashes", {}).get(name) == hashlib.sha256((HERE.parent / name).read_bytes()).hexdigest()
          for name in ("cdp_util.py", "chrome_util.py")),
      "CDP evidence binds the shared browser support code")
check(ev.get("harnessGate") is True and ev.get("exitCode") == 0,
      "fresh CDP harness passed, not a historical/unbound receipt")
check(ev.get("sendCountDuringComposition") == 0
      and ev.get("sendCountAfterComposition") == 1
      and ev.get("sendDeltaAfterComposition") == 1,
      "composition suppresses sending and the following Enter sends exactly once")
check(ev.get("compositionStateEnded") is True and ev.get("resetControlPassed") is True
      and ev.get("tabFocusPassed") is True,
      "composition ended, same-page reset is consistent, and real Tab focus is visible")
check(ev.get("method") == "CDP Input.imeSetComposition + Input.dispatchKeyEvent",
      "evidence declares browser-level IME injection method (not JS dispatchEvent)")
check(ev.get("realBrowser") is True and "Chrome" in ev.get("userAgent", ""),
      "evidence comes from real headless Chrome (UA recorded)")
check(ev.get("compositionStartFired") is True and ev.get("compositionEndFired") is True,
      "genuine DOM compositionstart/compositionend fired")
check(ev.get("enterDuringComposition_isComposing") is True,
      "Enter keydown DURING composition carries isComposing=true (UI Events 3.6.5)")
check(ev.get("enterAfterComposition_isComposing") is False,
      "Enter keydown AFTER composition carries isComposing=false")
check(ev.get("sendFiredDuringComposition") is False,
      "IME confirmation did NOT fire the send action (primary acceptance criterion)")
check(ev.get("sendFiredAfterComposition") is True,
      "a real Enter AFTER composition DOES fire send (control: gate isn't a blanket block)")
check(ev.get("isSyntheticJsKeydown") is False,
      "evidence is NOT a synthetic JS KeyboardEvent dispatch")
log("  NOTE: headless Chrome CDP composition is a real browser composition session,")
log("        but no OS-level CJK IME (e.g. Microsoft Pinyin) was installed/tested.")
log("        Honest status: browser-level IME PASS; OS-IME/visual: UNTESTED.")

# ---------------------------------------------------------------------------
log("== [CJK] CLREQ 2026-11-04 line-break / 禁则 rules (CSS vs untested) ==")
cjk = HERE / "cjk_layout.json"
check(cjk.is_file(), "cjk_layout.json rule matrix present")
cm = json.loads(cjk.read_text(encoding="utf-8"))
css_impl = [x for x in cm["rules"] if x["status"] == "css_implemented"]
untested = [x for x in cm["rules"] if x["status"] == "untested"]
check(len(css_impl) >= 3, "at least 3 CLREQ rules mapped to CSS properties (line-break/word-break/etc)")
check(len(untested) >= 1, "at least 1 CLREQ rule honestly marked untested (not CSS-implementable here)")
for x in css_impl:
    check(x.get("cssProperty") and x.get("clreqLocator"),
          "CSS rule %s cites clreq locator + CSS property" % x["id"])
log("  CSS-implemented: " + ", ".join(x["id"] for x in css_impl))
log("  Untested: " + ", ".join(x["id"] for x in untested))

log("")
log("RESULT: ALL MECHANICAL CHECKS PASSED (%d assertions)." % _n[0])
log("NOT TESTED: OS-level CJK IME (Microsoft Pinyin / candidate window), pixel/visual rendering,")
log("            审美/风格, WCAG full conformance audit, real human keyboard usability.")
OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
sys.exit(0)
