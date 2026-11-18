#!/usr/bin/env python3
"""Stage B runner for C2 — applies the SEALED A decision predicate.

I/O contract: reads ONLY the --input-dir's layout.json/layout.html; writes ONLY
--out (stdout text is also produced by the caller shell). No network, no
subprocess, no image API, no writes to A, no writes outside B.

The decision checks below are IDENTICAL in predicate to A/check_layout.py
(sealed, sha c68dcf16...). What Stage B ADDS is correct process semantics:
  - any failing check -> nonzero exit + 'FAIL' text (A's checker always exit 0),
  - missing/unreadable/malformed input -> clean error + 'FAIL' + nonzero, no silent pass,
  - extra break-test predicates (role ownership removed / salience budget over limit)
    are applied when their expectation flags are set in layout.json.

argv: python check_runner.py --input-dir DIR --out FILE
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone


def sha256(path):
    import hashlib
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(65536), b""):
            h.update(c)
    return h.hexdigest()


def evaluate(input_dir):
    """Return (checks, meta). Raises on missing/invalid input (caller maps to FAIL)."""
    spec_path = os.path.join(input_dir, "layout.json")
    html_path = os.path.join(input_dir, "layout.html")
    for p in (spec_path, html_path):
        if not os.path.isfile(p):
            raise FileNotFoundError("missing required input file: " + p)
    spec = json.load(open(spec_path, "r", encoding="utf-8"))
    html = open(html_path, "r", encoding="utf-8").read()

    checks = []

    def rec(name, ok, detail):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})

    # --- A-identical predicate: flicker ---
    fl = spec["flicker"]
    rec("flicker_zero_elements",
        fl["flashing_element_count"] == 0 and fl["animated_element_count"] == 0,
        "flashing=%s animated=%s max_hz=%s" % (
            fl["flashing_element_count"], fl["animated_element_count"], fl["max_frequency_hz"]))
    rec("flicker_max_hz_le_3", fl["max_frequency_hz"] <= 3,
        "max_frequency_hz=%s (<=3)" % fl["max_frequency_hz"])
    banned = fl["banned_in_css"]
    found = [b for b in banned if re.search(r"(?i)" + re.escape(b), html)]
    rec("html_has_no_banned_temporal_tokens", not found, "banned tokens found in HTML: %s" % (found or "none"))
    rec("html_has_no_script", not re.search(r"(?is)<script", html),
        "script tag present: %s" % bool(re.search(r"(?is)<script", html)))

    # --- A-identical predicate: salience formula ---
    slots = spec["slots"]
    computed = {}
    for sid, s in sorted(slots.items()):
        base = 0.45 * min(s["contrast_ratio"], 7) / 7 + 0.25 * s["font_weight"] / 700 + 0.30 * (1 - s["area_fraction"])
        val = round(min(base + (0.10 if s["accent"] else 0.0), 1.0), 2)
        computed[sid] = val
    declared = {sid: s["salience"] for sid, s in slots.items()}
    rec("salience_formula_matches_declared", computed == declared,
        "computed=%s declared=%s" % (computed, declared))
    top = max(computed, key=lambda k: computed[k]) if computed else None
    rec("top_salience_slot_is_S1", top == "S1", "top slot=%s" % top)

    # --- A-identical predicate: role ownership + contrast ---
    rb = spec["variants"]["role_based"]
    ps = spec["variants"]["pure_style"]
    rb_top = rb.get("binding", {}).get(top) if top else None
    ps_top = ps.get("binding", {}).get(top) if top else None
    rec("role_based_top_role_is_data", rb_top == "readable_data_value",
        "role_based S1 role=%s" % rb_top)
    rec("pure_style_top_role_is_decoration", ps_top == "illustrative_decoration",
        "pure_style S1 role=%s" % ps_top)
    rec("variants_differ_only_in_binding",
        rb.get("binding") != ps.get("binding") and
        rb.get("top_salience_role") == rb_top and ps.get("top_salience_role") == ps_top,
        "binding A=%s binding B=%s" % (rb.get("binding"), ps.get("binding")))
    rec("style_layer_declared_constant",
        all(k in spec["style_layer_held_constant"] for k in ("palette", "type_family", "spacing_scale_px", "slot_set")),
        "single shared style_layer_held_constant block present")

    # --- A-identical predicate: anchor + static slots ---
    anchor = spec["verification_anchor"]["end_copy"]
    rec("anchor_present_twice_in_html", html.count(anchor) == 2,
        "end_copy %r occurrences=%s" % (anchor, html.count(anchor)))
    for cls in ("s1", "s2", "s3"):
        rec("slot_class_present_%s" % cls, ('class="%s"' % cls) in html,
            "class %r count=%s" % (cls, html.count('class="%s"' % cls)))

    # --- Stage B break-test predicates (only active when flagged) ---
    exp = spec.get("_b_expectation", {})
    if exp.get("require_role_ownership_table"):
        # N3: every role must be owned by exactly one slot in each variant.
        table_ok = all(
            sorted(v.get("binding", {}).values()) == ["illustrative_decoration", "no_label_baseline", "readable_data_value"]
            for v in (rb, ps)
        )
        rec("role_ownership_table_complete", table_ok,
            "each variant binds all 3 roles exactly once (N3 L315)")

    if exp.get("salience_budget_cap") is not None:
        cap = exp["salience_budget_cap"]
        over = [sid for sid, v in computed.items() if v > cap]
        rec("salience_within_budget_cap", not over,
            "cap=%s computed=%s over=%s" % (cap, computed, over or "none"))

    meta = {
        "layout_json_sha256": sha256(spec_path),
        "layout_html_sha256": sha256(html_path),
        "layout_json_bytes": os.path.getsize(spec_path),
        "layout_html_bytes": os.path.getsize(html_path),
        "expectation": exp,
    }
    return checks, meta


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    lines = []
    lines.append("C2 Stage B check runner")
    lines.append("argv: " + " ".join(sys.argv))
    lines.append("input_dir: " + os.path.abspath(args.input_dir))
    lines.append("observed_at_utc: " + datetime.now(timezone.utc).isoformat())

    try:
        checks, meta = evaluate(args.input_dir)
    except Exception as e:
        lines.append("ERROR: " + type(e).__name__ + ": " + str(e))
        lines.append("FAIL (input impossible to evaluate; no silent pass)")
        out = "\n".join(lines) + "\n"
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        open(args.out, "w", encoding="utf-8").write(out)
        print(out, end="")
        return 2

    lines.append("input sha256: layout.json=%s layout.html=%s" % (
        meta["layout_json_sha256"], meta["layout_html_sha256"]))
    lines.append("expectation flags: " + json.dumps(meta["expectation"], ensure_ascii=False))
    n_fail = 0
    for c in checks:
        tag = "PASS" if c["pass"] else "FAIL"
        if not c["pass"]:
            n_fail += 1
        lines.append("[%s] %s | %s" % (tag, c["check"], c["detail"]))
    verdict = "PASS" if n_fail == 0 else "FAIL"
    lines.append("TOTAL: %d checks, %d failed" % (len(checks), n_fail))
    lines.append("RESULT: " + verdict + "  (exit=" + ("0" if n_fail == 0 else "1") + ")")
    out = "\n".join(lines) + "\n"
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    open(args.out, "w", encoding="utf-8").write(out)
    print(out, end="")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
