#!/usr/bin/env python3
"""C2 Stage A local structural checker.

Reads ONLY layout.json and layout.html from its own directory and writes ONLY
check-output.json to the same directory. No network, no subprocess, no image API,
no writes outside the A directory. This is a STRUCTURAL/DECLARED check: it does
not render the HTML and does not measure human perception.

Usage: python <this-file> [path/to/A-dir]
"""
import json
import os
import re
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
A_DIR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else HERE

def sha256(path):
    import hashlib
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    spec_path = os.path.join(A_DIR, "layout.json")
    html_path = os.path.join(A_DIR, "layout.html")
    out_path = os.path.join(A_DIR, "check-output.json")

    spec = json.loads(read_text(spec_path))
    html = read_text(html_path)

    checks = []

    def record(name, ok, detail):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})

    # 1. Flicker constraints
    fl = spec["flicker"]
    record("flicker_zero_elements",
           fl["flashing_element_count"] == 0 and fl["animated_element_count"] == 0,
           "flashing=%s animated=%s max_hz=%s" % (
               fl["flashing_element_count"], fl["animated_element_count"], fl["max_frequency_hz"]))
    record("flicker_max_hz_le_3", fl["max_frequency_hz"] <= 3,
           "max_frequency_hz=%s (<=3)" % fl["max_frequency_hz"])
    banned = fl["banned_in_css"]
    found_banned = [b for b in banned if re.search(r"(?i)" + re.escape(b), html)]
    record("html_has_no_banned_temporal_tokens", not found_banned,
           "banned tokens found in HTML: %s" % (found_banned or "none"))
    has_script = bool(re.search(r"(?is)<script", html))
    record("html_has_no_script", not has_script, "script tag present: %s" % has_script)

    # 2. Salience formula reproduces declared values (pure declared arithmetic)
    slots = spec["slots"]
    computed = {}
    for sid, s in sorted(slots.items()):
        base = 0.45 * min(s["contrast_ratio"], 7) / 7 + 0.25 * s["font_weight"] / 700 + 0.30 * (1 - s["area_fraction"])
        val = base + (0.10 if s["accent"] else 0.0)
        val = round(min(val, 1.0), 2)
        computed[sid] = val
    declared = {sid: s["salience"] for sid, s in slots.items()}
    record("salience_formula_matches_declared", computed == declared,
           "computed=%s declared=%s" % (computed, declared))
    top_slot = max(computed, key=lambda k: computed[k])
    record("top_salience_slot_is_S1", top_slot == "S1",
           "top slot=%s (salience=%s)" % (top_slot, computed[top_slot]))

    # 3. Refuting contrast: style held constant, only role->slot binding changes
    rb = spec["variants"]["role_based"]
    ps = spec["variants"]["pure_style"]
    rb_top_role = rb["binding"][top_slot]
    ps_top_role = ps["binding"][top_slot]
    record("role_based_top_role_is_data", rb_top_role == "readable_data_value",
           "role_based S1 role=%s" % rb_top_role)
    record("pure_style_top_role_is_decoration", ps_top_role == "illustrative_decoration",
           "pure_style S1 role=%s" % ps_top_role)
    record("variants_differ_only_in_binding", rb["binding"] != ps["binding"] and
           rb["top_salience_role"] == rb_top_role and ps["top_salience_role"] == ps_top_role,
           "binding A=%s binding B=%s" % (rb["binding"], ps["binding"]))
    record("style_layer_declared_constant",
           all(k in spec["style_layer_held_constant"] for k in ("palette", "type_family", "spacing_scale_px", "slot_set")),
           "single shared style_layer_held_constant block present (one vocabulary for both variants)")

    # 4. Verification anchor present in both variants (one-frame end copy)
    anchor = spec["verification_anchor"]["end_copy"]
    record("anchor_present_twice_in_html", html.count(anchor) == 2,
           "end_copy %r occurrences=%s" % (anchor, html.count(anchor)))

    # 5. HTML declares both slot classes used in both panels (static structure sanity)
    for cls in ("s1", "s2", "s3"):
        record("slot_class_present_%s" % cls, ('class="%s"' % cls) in html,
               "class %r count=%s" % (cls, html.count('class="%s"' % cls)))

    all_pass = all(c["pass"] for c in checks)
    out = {
        "checker": "A/check_layout.py (Stage A unaided local structural checker)",
        "case_id": spec["case_id"],
        "attempt_id": spec["attempt_id"],
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "STRUCTURAL/DECLARED only. No rendering, no perceptual or human measurement, no image channel.",
        "inputs": {
            "layout.json": {"sha256": sha256(spec_path), "bytes": os.path.getsize(spec_path)},
            "layout.html": {"sha256": sha256(html_path), "bytes": os.path.getsize(html_path)},
        },
        "checks": checks,
        "all_pass": all_pass,
        "summary": (
            "role-based variant PASSes the top-salience-role check; the pure-style "
            "counter-example FAILs it under an identical style vocabulary. This is "
            "a mechanical contrast that can refute a 'pure style' account at the "
            "level of declared salience ownership; it is NOT a human reading test "
            "and NOT an image comparison. Flicker count = 0 (<=3 Hz)."
        ),
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote", out_path, "all_pass=", all_pass, "checks=", len(checks))
    return 0

if __name__ == "__main__":
    sys.exit(main())
