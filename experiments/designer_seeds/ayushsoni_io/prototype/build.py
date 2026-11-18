#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S12-B / ayushsoni_io LOCAL mechanism prototype (author SeedDepsB).

Same four separation/connection/overlap/merge RELATIONS mapped onto TWO
self-authored vocabularies that actually change form (beam vs stamp).
8 keyframes + one 12-frame transition contact sheet (cap).

Deterministic: stdlib math + Pillow only, NO RNG, NO network, NO author media.
The verifier reads ACTUAL SVG element text and ACTUAL PNG bytes; it never
trusts a state JSON as proof that a connector / position / background exists.

Run:  python -X utf8 build.py <outdir>
"""
import json, math, sys
from pathlib import Path
from xml.etree import ElementTree as ET
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
CFG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
W, H = CFG["canvas"]["W"], CFG["canvas"]["H"]
BG = tuple(CFG["canvas"]["background_rgb"])
R = CFG["atom_radius"]
CY = CFG["atom_center_y"]
SG = CFG["state_geometry"]
REL = CFG["relations"]
VOCABS = list(CFG["vocabularies"].keys())
TH = CFG["thresholds"]
SEL = CFG["selection_rect_px"]
CORR = CFG["connector_corridor_px"]


def lerp(a, b, t):
    return a + (b - a) * t


def state_at(vocab, relation, t=None):
    s = dict(SG[relation])
    if t is not None:
        a, b = SG["separated"], SG["connected"]
        s = {"ax": lerp(a["ax"], b["ax"], t), "bx": lerp(a["bx"], b["bx"], t),
             "connector_width": lerp(a["connector_width"], b["connector_width"], t),
             "fused": False}
    return s


def svg_atom_beam(g, cx, cy, tag):
    ET.SubElement(g, "circle", {"cx": f"{cx:.2f}", "cy": f"{cy:.2f}", "r": f"{R}",
                                "fill": "#5664c4", "data-role": "atom", "data-atom": tag})
    ET.SubElement(g, "circle", {"cx": f"{cx:.2f}", "cy": f"{cy:.2f}", "r": f"{R*0.55:.2f}",
                                "fill": "#dfe6f7", "data-role": "atom-inner", "data-atom": tag})


def svg_atom_stamp(g, cx, cy, tag):
    pts = f"{cx:.2f},{cy-R:.2f} {cx+R:.2f},{cy:.2f} {cx:.2f},{cy+R:.2f} {cx-R:.2f},{cy:.2f}"
    ET.SubElement(g, "polygon", {"points": pts, "fill": "#786046",
                                  "data-role": "atom", "data-atom": tag})
    p2 = f"{cx:.2f},{cy-R*0.5:.2f} {cx+R*0.5:.2f},{cy:.2f} {cx:.2f},{cy+R*0.5:.2f} {cx-R*0.5:.2f},{cy:.2f}"
    ET.SubElement(g, "polygon", {"points": p2, "fill": "#c9b89c",
                                  "data-role": "atom-inner", "data-atom": tag})


def svg_atom(g, vocab, cx, cy, tag):
    (svg_atom_beam if vocab == "beam" else svg_atom_stamp)(g, cx, cy, tag)


def svg_connector_beam(g, ax, bx, cy, width):
    if width <= 0:
        return
    hw = width / 2.0
    pts = (f"{ax:.2f},{cy-hw:.2f} {bx:.2f},{cy-hw*0.35:.2f} "
           f"{bx:.2f},{cy+hw*0.35:.2f} {ax:.2f},{cy+hw:.2f}")
    ET.SubElement(g, "polygon", {"points": pts, "fill": "#8fb0e0", "data-role": "connector",
                                  "data-from": "A", "data-to": "B", "data-width": f"{width:.2f}"})


def svg_connector_stamp(g, ax, bx, cy, width):
    if width <= 0:
        return
    hw, mx = width / 2.0, (ax + bx) / 2.0
    d = (f"M {ax:.2f} {cy-hw:.2f} L {mx-6:.2f} {cy-hw:.2f} L {mx:.2f} {cy-hw*0.45:.2f} "
         f"L {mx+6:.2f} {cy-hw:.2f} L {bx:.2f} {cy-hw:.2f} L {bx:.2f} {cy+hw:.2f} "
         f"L {mx+6:.2f} {cy+hw:.2f} L {mx:.2f} {cy+hw*0.45:.2f} L {mx-6:.2f} {cy+hw:.2f} "
         f"L {ax:.2f} {cy+hw:.2f} Z")
    ET.SubElement(g, "path", {"d": d, "fill": "#a98c66", "data-role": "connector",
                               "data-from": "A", "data-to": "B", "data-width": f"{width:.2f}"})


def svg_fused_beam(g, ax, bx, cy):
    x0, x1 = ax - R * 0.4, bx + R * 0.4
    ET.SubElement(g, "rect", {"x": f"{x0:.2f}", "y": f"{cy-R*0.62:.2f}",
                               "width": f"{x1-x0:.2f}", "height": f"{R*1.24:.2f}",
                               "rx": f"{R*0.62:.2f}", "fill": "#5664c4",
                               "data-role": "fused", "data-from": "A", "data-to": "B"})


def svg_fused_stamp(g, ax, bx, cy):
    cx, rr = (ax + bx) / 2.0, (bx - ax) / 2.0 + R * 0.55
    pts = [f"{cx+rr*math.cos(math.pi/8+k*math.pi/4):.2f},{cy+rr*0.7*math.sin(math.pi/8+k*math.pi/4):.2f}"
           for k in range(8)]
    ET.SubElement(g, "polygon", {"points": " ".join(pts), "fill": "#786046",
                                  "data-role": "fused", "data-from": "A", "data-to": "B"})


def build_svg(vocab, relation, s, extra_blob=None):
    ax, bx = s["ax"], s["bx"]
    svg = ET.Element("svg", {"xmlns": "http://www.w3.org/2000/svg",
                              "width": str(W), "height": str(H), "viewBox": f"0 0 {W} {H}",
                              "data-vocab": vocab, "data-state": relation,
                              "data-ax": f"{ax:.2f}", "data-bx": f"{bx:.2f}",
                              "data-connector-width": f"{s['connector_width']:.2f}"})
    ET.SubElement(svg, "rect", {"x": "0", "y": "0", "width": str(W), "height": str(H),
                                 "fill": "#f2f3f2", "data-role": "background"})
    g = ET.SubElement(svg, "g", {"data-role": "objects"})
    if s["connector_width"] > 0:
        (svg_connector_beam if vocab == "beam" else svg_connector_stamp)(
            g, ax + R * 0.5, bx - R * 0.5, CY, s["connector_width"])
    if s["fused"]:
        (svg_fused_beam if vocab == "beam" else svg_fused_stamp)(g, ax, bx, CY)
        for cx, tag in ((ax, "A"), (bx, "B")):
            ET.SubElement(g, "circle", {"cx": f"{cx:.2f}", "cy": f"{CY}", "r": "4",
                                         "fill": "#ffffff", "data-role": "fused-mark", "data-atom": tag})
    else:
        svg_atom(g, vocab, ax, CY, "A")
        svg_atom(g, vocab, bx, CY, "B")
    if extra_blob is not None:
        bx0, by0, rr = extra_blob
        ET.SubElement(svg, "circle", {"cx": f"{bx0}", "cy": f"{by0}", "r": f"{rr}",
                                       "fill": "#00a0a0", "data-role": "out-of-selection-blob"})
    ET.indent(svg, space="  ")
    return ET.tostring(svg, encoding="unicode")


def _poly_points(s):
    return [(float(p.split(",")[0]), float(p.split(",")[1])) for p in s.strip().split()]


def hexcol(s):
    s = s.lstrip("#")
    return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4))


def _paint(el, d):
    tag = el.tag.split("}")[-1]
    if tag == "rect":
        x, y = float(el.get("x", 0)), float(el.get("y", 0))
        w, h = float(el.get("width", 0)), float(el.get("height", 0))
        fill = hexcol(el.get("fill", "#f2f3f2"))
        rx = float(el.get("rx", 0))
        if rx > 0:
            d.rounded_rectangle([x, y, x + w, y + h], radius=rx, fill=fill)
        else:
            d.rectangle([x, y, x + w, y + h], fill=fill)
    elif tag == "circle":
        cx, cy, r = float(el.get("cx")), float(el.get("cy")), float(el.get("r"))
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=hexcol(el.get("fill", "#000000")))
    elif tag == "polygon":
        d.polygon(_poly_points(el.get("points")), fill=hexcol(el.get("fill", "#000000")))
    elif tag == "path" and el.get("d"):
        toks = el.get("d").replace("M", " ").replace("L", " ").replace("Z", " ").split()
        nums = [float(t) for t in toks]
        pts = [(nums[i], nums[i + 1]) for i in range(0, len(nums) - 1, 2)]
        d.polygon(pts, fill=hexcol(el.get("fill", "#000000")))


def render_png(svg_text):
    root = ET.fromstring(svg_text)
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    paint_roles = ("background", "connector", "atom", "atom-inner", "fused",
                   "fused-mark", "out-of-selection-blob")
    for role in paint_roles:
        for el in root.iter():
            if el.get("data-role") == role:
                _paint(el, d)
    return img


def svg_meta(svg_text):
    root = ET.fromstring(svg_text)
    roles = {}
    for el in root.iter():
        r = el.get("data-role")
        if r:
            roles.setdefault(r, []).append(el)
    return root, roles


def geom_signature(svg_text):
    root, _ = svg_meta(svg_text)
    sig = set()
    for el in root.iter():
        r = el.get("data-role")
        if r in ("atom", "atom-inner", "connector", "fused"):
            shape = "path" if el.get("d") else ("points" if el.get("points") else "rect/circle")
            sig.add((el.tag.split("}")[-1], r, shape))
    return sig


def png_nonbg_in_corridor(img):
    x0, y0, x1, y1 = CORR
    cnt, px = 0, img.load()
    for y in range(y0, y1):
        for x in range(x0, x1):
            if px[x, y] != BG:
                cnt += 1
    return cnt


def png_outside_selection_diff(img_a, img_b):
    x0, y0, x1, y1 = SEL
    pa, pb, cnt = img_a.load(), img_b.load(), 0
    for y in range(H):
        for x in range(W):
            if x0 <= x < x1 and y0 <= y < y1:
                continue
            if pa[x, y] != pb[x, y]:
                cnt += 1
    return cnt


def png_atomA_centroid(img):
    px, xs = img.load(), []
    for y in range(CY - R, CY + R):
        for x in range(0, W // 2):
            r, g, b = px[x, y]
            if (r, g, b) == BG or (r > 200 and g > 200 and b > 200):
                continue
            xs.append(x)
    if not xs:
        return None
    xs.sort()
    cluster = [x for x in xs if x <= xs[0] + 2 * R + 30]
    return sum(cluster) / len(cluster)


def build_all(outdir):
    outdir = Path(outdir)
    if not outdir.is_absolute():
        outdir = HERE / outdir
    neg = outdir / "negatives"
    outdir.mkdir(parents=True, exist_ok=True)
    neg.mkdir(parents=True, exist_ok=True)

    keyframes = {}
    for vocab in VOCABS:
        for relation in REL:
            s = state_at(vocab, relation)
            svg = build_svg(vocab, relation, s)
            png = render_png(svg)
            stem = f"key_{vocab}_{relation}"
            (outdir / f"{stem}.svg").write_text(svg, encoding="utf-8")
            png.save(outdir / f"{stem}.png")
            keyframes[(vocab, relation)] = (svg, png, s)

    tv = "beam"
    frames = []
    for i in range(12):
        t = i / 11.0
        s = state_at(tv, "connected", t=t)
        svg = build_svg(tv, "connected", s)
        png = render_png(svg)
        frames.append((svg, png, s))
        (outdir / f"trans_{i:02d}.svg").write_text(svg, encoding="utf-8")
        png.save(outdir / f"trans_{i:02d}.png")
    tiles_x, tiles_y = 4, 3
    tw, th = CFG["transition"]["tile_px"]
    sheet = Image.new("RGB", (tw * tiles_x, th * tiles_y), (255, 255, 255))
    for i, (svg, png, s) in enumerate(frames):
        tile = png.resize((tw, th))
        ImageDraw.Draw(tile).text((3, 2), f"f{i:02d}", fill=(20, 20, 20))
        sheet.paste(tile, ((i % tiles_x) * tw, (i // tiles_x) * th))
    sheet.save(outdir / "transition_contact_sheet.png")

    # F1 missing connector (real SVG element removal + real PNG corridor loss)
    base_svg = keyframes[(tv, "connected")][0]
    root = ET.fromstring(base_svg)
    for g in root.iter():
        for child in list(g):
            if child.get("data-role") == "connector":
                g.remove(child)
    ET.indent(root, space="  ")
    f1_svg = ET.tostring(root, encoding="unicode")
    f1_png = render_png(f1_svg)
    (neg / "F1_missing_connector.svg").write_text(f1_svg, encoding="utf-8")
    f1_png.save(neg / "F1_missing_connector.png")
    (neg / "F1_state.json").write_text(json.dumps(
        {"state": "connected", "connector_present": True,
         "note": "DELIBERATELY WRONG claim: connector element was removed from the SVG/PNG"},
        indent=2), encoding="utf-8")

    # F2 position jump (shift atom A of transition frame 06)
    f2_svg, f2_png, f2_s = frames[6]
    root = ET.fromstring(f2_svg)
    root.set("data-ax", f"{f2_s['ax']+70:.2f}")
    for el in root.iter():
        if el.get("cx") and float(el.get("cx")) < W / 2:
            el.set("cx", f"{float(el.get('cx'))+70:.2f}")
        if el.get("points"):
            pts = _poly_points(el.get("points"))
            if sum(p[0] for p in pts) / len(pts) < W / 2:
                el.set("points", " ".join(f"{x+70:.2f},{y:.2f}" for x, y in pts))
    ET.indent(root, space="  ")
    f2_svg2 = ET.tostring(root, encoding="unicode")
    render_png(f2_svg2).save(neg / "F2_position_jump.png")
    (neg / "F2_position_jump.svg").write_text(f2_svg2, encoding="utf-8")

    # F3 out-of-selection background change
    f3_svg = build_svg("beam", "separated", state_at("beam", "separated"), extra_blob=(40, 40, 22))
    (neg / "F3_out_of_selection_change.svg").write_text(f3_svg, encoding="utf-8")
    render_png(f3_svg).save(neg / "F3_out_of_selection_change.png")

    ledger = {
        "relations_order": REL, "vocabularies": VOCABS,
        "keyframes": [{"vocab": v, "relation": r, "ax": SG[r]["ax"], "bx": SG[r]["bx"],
                       "connector_width": SG[r]["connector_width"]} for v in VOCABS for r in REL],
        "transition_frames": [{"i": i, "t": round(i / 11.0, 4),
                               "ax": round(frames[i][2]["ax"], 2)} for i in range(12)],
    }
    (outdir / "state_ledger.json").write_text(json.dumps(ledger, indent=2), encoding="utf-8")
    return keyframes, frames, neg


def run_checks(outdir, keyframes, frames, neg):
    outdir = Path(outdir) if Path(outdir).is_absolute() else HERE / outdir
    checks = {}

    pairs_ok, order_ok, corr_ok = 0, True, True
    for vocab in VOCABS:
        seen = []
        for relation in REL:
            svg_p = outdir / f"key_{vocab}_{relation}.svg"
            png_p = outdir / f"key_{vocab}_{relation}.png"
            if svg_p.is_file() and png_p.is_file():
                pairs_ok += 1
            txt = svg_p.read_text(encoding="utf-8")
            root = ET.fromstring(txt)
            seen.append(root.get("data-state"))
            _, roles = svg_meta(txt)
            conns = roles.get("connector", [])
            if relation == "connected" and (not conns or conns[0].get("data-from") != "A" or conns[0].get("data-to") != "B"):
                corr_ok = False
        if seen != REL:
            order_ok = False
    checks["P1_keyframes_and_relation_order"] = {
        "passed": pairs_ok == 8 and order_ok and corr_ok, "pairs": pairs_ok,
        "relation_order_preserved": order_ok, "connector_A_to_B_preserved": corr_ok,
        "read_from": "actual .svg files (ET parse) + actual .png existence"}

    sb = geom_signature(keyframes[("beam", "connected")][0])
    ss = geom_signature(keyframes[("stamp", "connected")][0])
    diff = sb.symmetric_difference(ss)
    checks["P2_vocabularies_change_form"] = {
        "passed": len(diff) >= TH["vocab_geometry_min_differing_elements"],
        "beam_sig": [list(x) for x in sorted(sb)], "stamp_sig": [list(x) for x in sorted(ss)],
        "differing_elements": len(diff), "read_from": "actual SVG element tags/roles"}

    png_centroids, svg_ax = [], []
    for svg, png, s in frames:
        png_centroids.append(png_atomA_centroid(png))
        svg_ax.append(float(ET.fromstring(svg).get("data-ax")))
    steps_png = [abs(png_centroids[i + 1] - png_centroids[i]) for i in range(11)]
    steps_svg = [abs(svg_ax[i + 1] - svg_ax[i]) for i in range(11)]
    checks["P3_smooth_transition"] = {
        "passed": max(steps_png) <= TH["position_step_max_px"] and max(steps_svg) <= TH["position_step_max_px"],
        "max_step_png_px": round(max(steps_png), 3), "max_step_svg_px": round(max(steps_svg), 3),
        "threshold_px": TH["position_step_max_px"],
        "read_from": "actual transition PNG centroids + actual SVG data-ax"}

    od = png_outside_selection_diff(keyframes[("beam", "separated")][1], keyframes[("beam", "connected")][1])
    checks["P4_outside_selection_diff_zero"] = {
        "passed": od <= TH["outside_selection_max_diff_px"], "outside_diff_px": od,
        "read_from": "actual PNG bytes of key_beam_separated vs key_beam_connected"}

    f1_svg = (neg / "F1_missing_connector.svg").read_text(encoding="utf-8")
    _, f1_roles = svg_meta(f1_svg)
    f1_svg_has_connector = len(f1_roles.get("connector", [])) > 0
    f1_png_corridor = png_nonbg_in_corridor(Image.open(neg / "F1_missing_connector.png").convert("RGB"))
    base_corridor = png_nonbg_in_corridor(keyframes[("beam", "connected")][1])
    f1_detected = (not f1_svg_has_connector) and f1_png_corridor < base_corridor * 0.5 and f1_png_corridor < TH["connector_corridor_min_nonbg_px"]
    naive_json = json.loads((neg / "F1_state.json").read_text(encoding="utf-8"))
    naive_would_pass = bool(naive_json["state"] == "connected" and naive_json["connector_present"])
    checks["F1_missing_connector_DETECTED"] = {
        "must_fail": True, "passed": f1_detected and naive_would_pass,
        "verdict": "FAILED (missing connector: real SVG connector element removed + PNG corridor pixels gone)",
        "note": "verifier reads real SVG connector element + real PNG corridor pixels; state-JSON alone says connector_present=true (wrong)",
        "svg_connector_elements": len(f1_roles.get("connector", [])),
        "png_corridor_nonbg_px": f1_png_corridor, "correct_corridor_nonbg_px": base_corridor,
        "naive_state_json_would_pass": naive_would_pass, "detected_from_real_bytes": f1_detected}

    f2_svg = (neg / "F2_position_jump.svg").read_text(encoding="utf-8")
    f2_ax = float(ET.fromstring(f2_svg).get("data-ax"))
    f2_centroid = png_atomA_centroid(Image.open(neg / "F2_position_jump.png").convert("RGB"))
    expected_ax = frames[6][2]["ax"]
    expected_centroid = png_atomA_centroid(frames[6][1])
    f2_detected = (abs(f2_ax - expected_ax) > TH["position_step_max_px"] * 3 and
                   abs(f2_centroid - expected_centroid) > TH["position_step_max_px"] * 2)
    checks["F2_position_jump_DETECTED"] = {
        "must_fail": True, "passed": f2_detected, "verdict": "FAILED (position jump: atom A shifted in real SVG data-ax + PNG centroid)",
        "expected_ax": round(expected_ax, 2),
        "fault_ax": f2_ax, "expected_png_centroid": round(expected_centroid, 2),
        "fault_png_centroid": round(f2_centroid, 2), "detected_from_real_bytes": f2_detected}

    f3_png = Image.open(neg / "F3_out_of_selection_change.png").convert("RGB")
    f3_od = png_outside_selection_diff(keyframes[("beam", "separated")][1], f3_png)
    checks["F3_out_of_selection_change_DETECTED"] = {
        "must_fail": True, "passed": f3_od > TH["outside_selection_max_diff_px"],
        "verdict": "FAILED (out-of-selection background change painted outside registered selection)",
        "outside_diff_px": f3_od, "detected_from_real_bytes": f3_od > TH["outside_selection_max_diff_px"]}

    pos = ["P1_keyframes_and_relation_order", "P2_vocabularies_change_form",
           "P3_smooth_transition", "P4_outside_selection_diff_zero"]
    negk = ["F1_missing_connector_DETECTED", "F2_position_jump_DETECTED", "F3_out_of_selection_change_DETECTED"]
    checks["_summary"] = {
        "positive_checks": pos, "negative_controls": negk,
        "all_positive_pass": all(checks[k]["passed"] for k in pos),
        "all_negative_controls_detected": all(checks[k]["passed"] for k in negk),
        "verifier_never_uses_state_json_as_proof": True}
    return checks


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "outputs"
    keyframes, frames, neg = build_all(outdir)
    checks = run_checks(outdir, keyframes, frames, neg)
    out = Path(outdir) if Path(outdir).is_absolute() else HERE / outdir
    (out / "checks.json").write_text(json.dumps(checks, indent=2), encoding="utf-8")
    s = checks["_summary"]
    print("ayushsoni_io checks:", "POS=", s["all_positive_pass"],
          "NEG_DETECTED=", s["all_negative_controls_detected"])
    for k, v in checks.items():
        if k != "_summary":
            print(f"  {k}: passed={v.get('passed')}")
    return 0 if s["all_positive_pass"] and s["all_negative_controls_detected"] else 1


if __name__ == "__main__":
    sys.exit(main())
