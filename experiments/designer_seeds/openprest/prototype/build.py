#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S05 openprest LOCAL mechanism prototype (CANDIDATE HYPOTHESIS, NOT E3).

Two MANUALLY DEFINED glyph masks (A/H) on a fixed grid + ONE dot primitive
family at THREE size/density settings + ONE deliberately bad grid case +
a small-size render. Stdlib SVG + Pillow PNG. No font engine.
No author artwork, no font files, no image API. Deterministic (no RNG).
S11-B calibration: the small-size case only EMITS a render and RETAINS the
35 primitives. Connectivity/counter (enclosed-hole) topology and readability
are NOT measured here (C4 checks only the primitive count); they stay
unmeasured / pending_human. No "loss recorded / hole collapses" claim.
"""
import sys, json, hashlib
from pathlib import Path
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else (HERE / "outputs")
OUT.mkdir(parents=True, exist_ok=True)
CFG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))

GM = CFG["glyph_masks"]
G = CFG["grid"]
PF = CFG["primitive_family"]
SETTINGS = PF["settings"]
CELL = G["cell_px"]
CW, CH = G["canvas_w"], G["canvas_h"]
ORIG = {"A": G["glyph_origin_A"], "H": G["glyph_origin_H"]}


def centers(glyph):
    """Declared grid centers for each ON cell of a glyph."""
    ox, oy = ORIG[glyph]
    out = []
    for c, r in GM[glyph]["on_cells"]:
        # center of cell (c,r)
        out.append((ox + c*CELL + CELL//2, oy + r*CELL + CELL//2))
    return out


def primitives_for(settings_id, bad=False):
    """One primitive family (filled circle). Returns list of {x,y,r,glyph,col,row}."""
    s = next(s for s in SETTINGS if s["id"] == settings_id)
    r = CFG["bad_case"]["unregistered_radius_px"] if bad else s["radius_px"]
    dx, dy = CFG["bad_case"]["offset_px"] if bad else (0, 0)
    prims = []
    for g in ("A", "H"):
        for (i, (c, rr)) in enumerate(GM[g]["on_cells"]):
            ox, oy = ORIG[g]
            x = ox + c*CELL + CELL//2 + dx
            y = oy + rr*CELL + CELL//2 + dy
            prims.append({"glyph": g, "col": c, "row": rr, "x": x, "y": y, "r": r})
    return prims, r, bool(bad)


def in_bounds_check(prims, registered_radii, cell_px, cw, ch):
    """Each primitive center must be the exact center of a declared grid cell
    and within canvas; radius must be a registered setting value."""
    declared_centers = set(centers("A")) | set(centers("H"))
    out_of_grid = [p for p in prims if (p["x"], p["y"]) not in declared_centers
                   or not (0 <= p["x"] < cw and 0 <= p["y"] < ch)]
    unreg = [p for p in prims if p["r"] not in registered_radii]
    return {"out_of_grid_count": len(out_of_grid),
            "unregistered_scale_count": len(unreg),
            "detected": len(out_of_grid) > 0 or len(unreg) > 0,
            "example_out_of_grid": out_of_grid[:3], "example_unregistered": unreg[:3]}


def svg_of(prims, r, cw, ch, title):
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">' % (cw, ch, cw, ch),
             '<!-- %s | self-authored 2-glyph geometry toy, NOT a font -->' % title,
             '<rect width="100%" height="100%" fill="#ffffff"/>']
    for p in prims:
        parts.append('<circle cx="%d" cy="%d" r="%d" fill="#000000"/>' % (p["x"], p["y"], p["r"]))
    parts.append('</svg>')
    return "\n".join(parts)


def png_of(prims, cw, ch):
    im = Image.new("L", (cw, ch), 255)
    d = ImageDraw.Draw(im)
    for p in prims:
        x, y, r = p["x"], p["y"], p["r"]
        d.ellipse([x-r, y-r, x+r, y+r], fill=0)
    return im


registered = [s["radius_px"] for s in SETTINGS]
ledgers = {}
checks_primitive = {}

# ---- main 3 settings ----
for s in SETTINGS:
    sid = s["id"]
    prims, r, is_bad = primitives_for(sid, bad=False)
    b = in_bounds_check(prims, registered, CELL, CW, CH)
    svg = svg_of(prims, r, CW, CH, "setting %s r=%d" % (sid, r))
    png = png_of(prims, CW, CH)
    (OUT / ("glyphs_%s.svg" % sid)).write_text(svg, encoding="utf-8")
    png.save(OUT / ("glyphs_%s.png" % sid))
    # primitive coordinate/count/bounds ledger
    led = {
        "setting_id": sid, "radius_px": r, "primitive_family": PF["name"],
        "n_primitives": len(prims), "expected_n_primitives": len(GM["A"]["on_cells"]) + len(GM["H"]["on_cells"]),
        "A_on_cells": len(GM["A"]["on_cells"]), "H_on_cells": len(GM["H"]["on_cells"]),
        "bounds": {"x_min": min(p["x"] for p in prims), "x_max": max(p["x"] for p in prims),
                   "y_min": min(p["y"] for p in prims), "y_max": max(p["y"] for p in prims),
                   "canvas": [cw := CW, ch := CH]},
        "in_bounds_check": b, "primitives": prims,
    }
    (OUT / ("primitives_%s.json" % sid)).write_text(json.dumps(led, indent=1), encoding="utf-8")
    ledgers[sid] = led
    checks_primitive[sid] = b

# ---- deliberately bad grid case ----
bad_prims, bad_r, _ = primitives_for("s2", bad=True)
bad_check = in_bounds_check(bad_prims, registered, CELL, CW, CH)
(OUT / "glyphs_bad_grid_offset.svg").write_text(svg_of(bad_prims, bad_r, CW, CH, "DELIBERATELY BAD grid offset"), encoding="utf-8")
png_of(bad_prims, CW, CH).save(OUT / "glyphs_bad_grid_offset.png")
bad_led = {
    "case_id": CFG["bad_case"]["id"], "description": CFG["bad_case"]["description"],
    "radius_px": bad_r, "registered_radii": registered, "offset_applied": CFG["bad_case"]["offset_px"],
    "n_primitives": len(bad_prims), "in_bounds_check": bad_check,
    "expected_failure": CFG["bad_case"]["expected_failure"],
    "outcome": "DETECTED (expected failure)" if bad_check["detected"] else "NOT DETECTED (check bug)",
}
(OUT / "primitives_bad_grid_offset.json").write_text(json.dumps(bad_led, indent=1), encoding="utf-8")

# ---- small-size render (topology/readability NOT measured) ----
SS = CFG["small_size_limitation"]
scell = SS["cell_px"]; scw, sch = SS["canvas_w"], SS["canvas_h"]
# recompute A/H centers at the small cell size with a small origin
def small_centers(glyph):
    ox, oy = (6, 4) if glyph == "A" else (34, 4)
    return [(ox + c*scell + scell//2, oy + rr*scell + scell//2) for c, rr in GM[glyph]["on_cells"]]
small_prims = []
for g in ("A", "H"):
    for (x, y) in small_centers(g):
        small_prims.append({"glyph": g, "x": x, "y": y, "r": 1})
small_svg = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d">' % (scw, sch),
             '<!-- small-size render (cell_px=4); topology/readability unmeasured, NOT a legibility proof -->',
             '<rect width="100%" height="100%" fill="#ffffff"/>']
for p in small_prims:
    small_svg.append('<circle cx="%d" cy="%d" r="%d" fill="#000000"/>' % (p["x"], p["y"], p["r"]))
small_svg.append('</svg>')
(OUT / "glyphs_small_size.svg").write_text("\n".join(small_svg), encoding="utf-8")
png_of(small_prims, scw, sch).save(OUT / "glyphs_small_size.png")
small_led = {
    "case": "small_size_render", "cell_px": scell, "canvas": [scw, sch],
    "n_primitives": len(small_prims), "radius_px": 1,
    "note": "Small-size render emitted at 4px cells / r=1; the 35 declared primitives are retained. Connectivity / counter (enclosed-hole) topology and readability are NOT measured by this fixture (C4 checks only n_primitives == 35) and stay unmeasured / pending_human. This is NOT a legibility/readability claim, NOT a font, and NOT a demonstration of topology loss.",
    "outcome": "small-size render emitted; 35 primitives retained; topology-readability loss unmeasured / pending_human",
}
(OUT / "small_size_limitation.json").write_text(json.dumps(small_led, indent=1), encoding="utf-8")

# ---- parameter ledger (what varied, what did not) ----
param_ledger = {
    "constant_across_all_settings": {
        "glyph_masks": {g: GM[g]["on_cells"] for g in ("A", "H")},
        "grid_cell_px": CELL, "origins": ORIG, "canvas": [CW, CH],
        "primitive_family": PF["name"], "n_settings": len(SETTINGS),
    },
    "varied_dimension": "radius_px ONLY (one dot primitive family)",
    "settings": [{"id": s["id"], "radius_px": s["radius_px"]} for s in SETTINGS],
    "bad_case": {"id": CFG["bad_case"]["id"], "changed": ["half-cell offset", "unregistered radius"]},
    "small_size_case": {"cell_px": scell, "canvas": [scw, sch]},
}
(OUT / "parameter_ledger.json").write_text(json.dumps(param_ledger, ensure_ascii=False, indent=1), encoding="utf-8")

# ---- checks ----
expected_n = len(GM["A"]["on_cells"]) + len(GM["H"]["on_cells"])
C1 = all(l["n_primitives"] == expected_n and not l["in_bounds_check"]["detected"] for l in ledgers.values())
# same centers across settings?
base_centers = sorted((p["x"], p["y"]) for p in ledgers["s1"]["primitives"])
C2 = all(sorted((p["x"], p["y"]) for p in l["primitives"]) == base_centers for l in ledgers.values()) \
     and all(set(p["r"] for p in l["primitives"]) == {l["radius_px"]} for l in ledgers.values())
C3 = bad_check["detected"]
C4 = small_led["n_primitives"] == expected_n  # ONLY primitive count; NOT a connectivity/counter/readability test
C5 = all((OUT / f).is_file() for f in ["glyphs_s1.svg","glyphs_s1.png","glyphs_s2.svg","glyphs_s2.png","glyphs_s3.svg","glyphs_s3.png","glyphs_bad_grid_offset.svg","glyphs_small_size.svg"])
C7 = True  # boundary enforced by explicit label in config + this file + RESULT
checks = {
    "C1_primitive_count_and_in_bounds": {"pass": C1, "expected_n_primitives": expected_n,
        "per_setting": {sid: {"n": ledgers[sid]["n_primitives"], "out_of_grid": ledgers[sid]["in_bounds_check"]["out_of_grid_count"]} for sid in ledgers}},
    "C2_only_registered_radius_varied": {"pass": C2, "note": "glyph masks + grid centers identical across s1/s2/s3; only radius_px changes"},
    "C3_bad_case_detected": {"pass": C3, "out_of_grid_count": bad_check["out_of_grid_count"],
        "unregistered_scale_count": bad_check["unregistered_scale_count"], "outcome": bad_led["outcome"]},
    "C4_small_size_render_recorded": {"pass": C4, "cell_px": scell, "n_primitives": small_led["n_primitives"],
        "note": "small-size render emitted; 35 primitives retained; connectivity/counter (enclosed-hole) topology and readability NOT measured (C4 checks only n_primitives); unmeasured / pending_human"},
    "C5_svg_and_png_outputs_exist": {"pass": C5, "main_canvas": [CW, CH], "small_canvas": [scw, sch]},
    "C6_deterministic_rerun": {"note": "filled by run_evidence.json after two identical runs", "pass": None},
    "C7_boundary_no_full_font_no_axis_claim": {"pass": C7,
        "label": "2-glyph hand-declared geometry toy; NOT a font; variable-font axis NOT proven/disproven; author geometry NOT claimed"},
}
(OUT / "checks.json").write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding="utf-8")
(OUT / "run_config_snapshot.json").write_text(json.dumps({"config_sha256": hashlib.sha256((HERE/"config.json").read_bytes()).hexdigest()}, indent=2), encoding="utf-8")
print("openprest build OK ->", OUT)
print("expected/actual primitives per setting:", expected_n, [ledgers[s]["n_primitives"] for s in ledgers])
print("bad case detected:", C3, "| small-size n:", small_led["n_primitives"])
