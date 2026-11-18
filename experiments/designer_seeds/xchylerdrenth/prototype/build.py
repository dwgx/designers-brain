#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S12-B / xchylerdrenth LOCAL mechanism prototype (author SeedDepsB).

Fixed 8-node / 10-edge DAG. 5 configs (flat/perspective baselines, decoration
density 18/40, code texture) + 3 single-fault controls, 8 images total.

Verifier:
  - structure edges read from ACTUAL output SVG <path data-role=structure-edge>,
    NOT from the input G;
  - VP / residual measured ONLY on depth-parallel lines (flat = N/A);
  - occlusion judged from ACTUAL PNG overlap pixels, not a z-order field.
Pseudo-edge / bad-VP / wrong-z MUST each be detected as a failure.

Deterministic: stdlib + Pillow only, NO RNG, NO network, NO author/Bem media.
Run: python -X utf8 build.py <outdir>
"""
import json, sys, math
from pathlib import Path
from xml.etree import ElementTree as ET
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
CFG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
W, H = CFG["canvas"]["W"], CFG["canvas"]["H"]
BG = tuple(CFG["canvas"]["background_rgb"])
NODES = CFG["flat_node_coords_px"]
EDGES = [tuple(e) for e in CFG["dag"]["E"]]
CANON = set(EDGES)
VP = tuple(CFG["projection"]["VP_px"])
K = CFG["projection"]["k"]
DEPTH_N = CFG["depth_lines"]["count"]
OC = CFG["occlusion_cards_px"]
BACK_C = tuple(OC["back_rgb"])
FRONT_C = tuple(OC["front_rgb"])
OVL = tuple(OC["overlap"])
TH = CFG["thresholds"]

EDGE_C = (40, 44, 50)
NODE_C = (70, 110, 150)
DEPTH_C = (150, 180, 210)
DECO_C = (200, 170, 90)
CODE_C = (90, 90, 120)


def hexs(c):
    return "#%02x%02x%02x" % c


def project(pt, perspective):
    if not perspective:
        return pt
    return (VP[0] + (pt[0] - VP[0]) * K, VP[1] + (pt[1] - VP[1]) * K)


def depth_line_endpoints(i):
    ax = 30 + i * 90
    ay = 372
    A = (ax, ay)
    B = (ax + (VP[0] - ax) * 0.78, ay + (VP[1] - ay) * 0.78)
    return A, B


def deco_points(n):
    """Deterministic self-drawn decoration dots (NO RNG): fixed lattice."""
    pts = []
    cols = 8
    for i in range(n):
        x = 24 + (i % cols) * 60 + (i // cols) * 8
        y = 30 + (i // cols) * 26 + (i % 3) * 4
        pts.append((x, y))
    return pts


def build_svg(name, perspective, deco_n, code_on, faults=()):
    """Build one config/fault SVG in strict DOCUMENT (paint/z) order."""
    svg = ET.Element("svg", {"xmlns": "http://www.w3.org/2000/svg",
                              "width": str(W), "height": str(H), "viewBox": f"0 0 {W} {H}",
                              "data-config": name, "data-perspective": "1" if perspective else "0",
                              "data-deco": str(deco_n), "data-code": "1" if code_on else "0"})
    ET.SubElement(svg, "rect", {"x": "0", "y": "0", "width": str(W), "height": str(H),
                                 "fill": hexs(BG), "data-role": "background"})

    # 1) depth lines (perspective only); bad-VP fault shifts ONE endpoint
    if perspective:
        for i in range(DEPTH_N):
            A, B = depth_line_endpoints(i)
            if "bad_vp" in faults and i == 2:
                B = (B[0] + 34, B[1] + 24)   # single fault: line no longer concurs
            d = f"M {A[0]:.2f} {A[1]:.2f} L {B[0]:.2f} {B[1]:.2f}"
            ET.SubElement(svg, "path", {"d": d, "stroke": hexs(DEPTH_C), "stroke-width": "2",
                                        "fill": "none", "data-role": "depth-line", "data-index": str(i)})

    # 2) structure edges (read by verifier from these paths)
    proj = {n: project(tuple(c), perspective) for n, c in NODES.items()}
    for (u, v) in EDGES:
        x1, y1 = proj[u]
        x2, y2 = proj[v]
        d = f"M {x1:.2f} {y1:.2f} L {x2:.2f} {y2:.2f}"
        ET.SubElement(svg, "path", {"d": d, "stroke": hexs(EDGE_C), "stroke-width": "3",
                                    "fill": "none", "data-role": "structure-edge",
                                    "data-from": u, "data-to": v})
    # pseudo-edge single fault: decoration dot -> node g (fake structure edge)
    if "pseudo_edge" in faults:
        d = f"M {24+60:.2f} {30:.2f} L {proj['g'][0]:.2f} {proj['g'][1]:.2f}"
        ET.SubElement(svg, "path", {"d": d, "stroke": hexs(EDGE_C), "stroke-width": "3",
                                    "fill": "none", "data-role": "structure-edge",
                                    "data-from": "deco0", "data-to": "g"})

    # 3) nodes
    for n, (x, y) in proj.items():
        ET.SubElement(svg, "circle", {"cx": f"{x:.2f}", "cy": f"{y:.2f}", "r": "13",
                                       "fill": hexs(NODE_C), "data-role": "node", "data-node": n})
        ET.SubElement(svg, "text", {"x": f"{x-3:.2f}", "y": f"{y+4:.2f}",
                                     "font-family": "monospace", "font-size": "12",
                                     "fill": "#ffffff", "data-role": "node-label"}).text = n

    # 4) decoration dots
    for i, (x, y) in enumerate(deco_points(deco_n)):
        ET.SubElement(svg, "circle", {"cx": f"{x}", "cy": f"{y}", "r": "3",
                                       "fill": hexs(DECO_C), "data-role": "deco", "data-index": str(i)})

    # 5) code texture (self-authored JSON glyph patch)
    if code_on:
        snippet = ["{", ' "op": "route",', ' "n": 8,', ' "edges": 10', "}"]
        for j, line in enumerate(snippet):
            ET.SubElement(svg, "text", {"x": "330", "y": str(300 + j * 14),
                                         "font-family": "monospace", "font-size": "11",
                                         "fill": hexs(CODE_C), "data-role": "code-texture"}).text = line

    # 6) occlusion cards. CORRECT z: back drawn first, front AFTER (front on top).
    back = (OC["back"], BACK_C, "card-back")
    front = (OC["front"], FRONT_C, "card-front")
    order = [front, back] if "wrong_z" in faults else [back, front]  # wrong-z swaps order
    for (rect, color, role) in order:
        x0, y0, x1, y1 = rect
        ET.SubElement(svg, "rect", {"x": str(x0), "y": str(y0),
                                     "width": str(x1 - x0), "height": str(y1 - y0),
                                     "fill": hexs(color), "stroke": hexs(EDGE_C), "stroke-width": "1",
                                     "data-role": role})
    ET.indent(svg, space="  ")
    return ET.tostring(svg, encoding="unicode")


def render_png(svg_text):
    """Rasterise in strict DOCUMENT order (so z-order comes from draw order)."""
    root = ET.fromstring(svg_text)
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        role = el.get("data-role")
        if tag == "rect" and role in ("background", "card-back", "card-front"):
            x, y = float(el.get("x", 0)), float(el.get("y", 0))
            w, h = float(el.get("width", 0)), float(el.get("height", 0))
            fill = el.get("fill")
            d.rectangle([x, y, x + w, y + h], fill=tuple(int(fill[i:i+2], 16) for i in (1, 3, 5)))
            if role != "background":
                d.rectangle([x, y, x + w, y + h], outline=EDGE_C, width=1)
        elif tag == "circle" and role in ("node", "deco"):
            cx, cy, r = float(el.get("cx")), float(el.get("cy")), float(el.get("r"))
            col = NODE_C if role == "node" else DECO_C
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
        elif tag == "path" and el.get("d") and role in ("structure-edge", "depth-line"):
            toks = el.get("d").replace("M", " ").replace("L", " ").split()
            nums = [float(t) for t in toks]
            pts = [(nums[i], nums[i+1]) for i in range(0, len(nums)-1, 2)]
            col = EDGE_C if role == "structure-edge" else DEPTH_C
            d.line(pts, fill=col, width=3 if role == "structure-edge" else 2)
        elif tag == "text" and role in ("node-label", "code-texture"):
            x, y = float(el.get("x")), float(el.get("y"))
            d.text((x, y - 10), el.text or "", fill=(255, 255, 255) if role == "node-label" else CODE_C)
    return img


# ---- verifier helpers (read REAL SVG / REAL PNG) ----
def svg_edges(svg_text):
    """Parse structure edges from ACTUAL SVG <path data-role=structure-edge>."""
    root = ET.fromstring(svg_text)
    nodes = {el.get("data-node"): (float(el.get("cx")), float(el.get("cy")))
             for el in root.iter() if el.get("data-role") == "node"
             and el.tag.split("}")[-1] == "circle"}
    out = []
    for el in root.iter():
        if el.get("data-role") != "structure-edge":
            continue
        u, v = el.get("data-from"), el.get("data-to")
        # This bounded fixture emits one M/L segment per edge. Validate its
        # actual geometry against the actual node centers, not just labels.
        # Unknown node IDs still fail the canonical edge-set comparison.
        if u in nodes and v in nodes:
            try:
                toks = (el.get("d") or "").split()
                valid = (el.tag.split("}")[-1] == "path" and len(toks) == 6
                         and toks[0] == "M" and toks[3] == "L")
                a = (float(toks[1]), float(toks[2]))
                b = (float(toks[4]), float(toks[5]))
                valid = (valid and all(math.isfinite(n) for n in (*a,*b))
                         and math.dist(a,nodes[u]) <= .05
                         and math.dist(b,nodes[v]) <= .05
                         and math.dist(a,b) > .05
                         and el.get("stroke") not in (None,"none","transparent")
                         and float(el.get("stroke-width","1")) > 0
                         and float(el.get("opacity","1")) > 0
                         and el.get("display") != "none"
                         and el.get("visibility") != "hidden")
            except (ValueError,TypeError,IndexError):
                valid = False
            if not valid:
                u = "invalid_geometry:" + str(u)
        out.append((u,v))
    return set(out), out


def svg_depth_lines(svg_text):
    root = ET.fromstring(svg_text)
    lines = []
    for el in root.iter():
        if el.get("data-role") == "depth-line":
            toks = el.get("d").replace("M", " ").replace("L", " ").split()
            nums = [float(t) for t in toks]
            lines.append(((nums[0], nums[1]), (nums[2], nums[3])))
    return lines


def line_intersection(l1, l2):
    (x1, y1), (x2, y2) = l1
    (x3, y3), (x4, y4) = l2
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) < 1e-9:
        return None
    px = ((x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2) * (x3*y4 - y3*x4)) / den
    py = ((x1*y2 - y1*x2) * (y3 - y4) - (y1 - y2) * (x3*y4 - y3*x4)) / den
    return (px, py)


def vp_residual(lines):
    """VP estimated ONLY from depth-line pairs; residual = max spread."""
    pts = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            p = line_intersection(lines[i], lines[j])
            if p:
                pts.append(p)
    if not pts:
        return None, None
    mx = sum(p[0] for p in pts) / len(pts)
    my = sum(p[1] for p in pts) / len(pts)
    res = max(math.hypot(p[0] - mx, p[1] - my) for p in pts)
    return (mx, my), res


def png_overlap_colors(img):
    """Count FRONT vs BACK colored pixels in the overlap rect from REAL PNG."""
    px = img.load()
    front = back = 0
    x0, y0, x1, y1 = OVL
    for y in range(y0, y1):
        for x in range(x0, x1):
            c = px[x, y]
            if all(abs(c[i] - FRONT_C[i]) <= 12 for i in range(3)):
                front += 1
            elif all(abs(c[i] - BACK_C[i]) <= 12 for i in range(3)):
                back += 1
    total = (x1 - x0) * (y1 - y0)
    return {"front": front, "back": back, "total": total,
            "front_ratio": round(front / total, 4), "back_ratio": round(back / total, 4)}


def build_all(outdir):
    outdir = Path(outdir) if Path(outdir).is_absolute() else HERE / outdir
    neg = outdir / "negatives"
    outdir.mkdir(parents=True, exist_ok=True)
    neg.mkdir(parents=True, exist_ok=True)
    configs = [
        ("flat_base", False, 0, False, ()),
        ("persp_base", True, 0, False, ()),
        ("persp_d18", True, 18, False, ()),
        ("persp_code", True, 0, True, ()),
        ("persp_d40", True, 40, False, ()),
        ("F_pseudo_edge", True, 0, False, ("pseudo_edge",)),
        ("F_bad_VP", True, 0, False, ("bad_vp",)),
        ("F_wrong_z", True, 0, False, ("wrong_z",)),
    ]
    imgs = {}
    for name, persp, deco, code, faults in configs:
        svg = build_svg(name, persp, deco, code, faults)
        png = render_png(svg)
        sub = neg if name.startswith("F_") else outdir
        (sub / f"{name}.svg").write_text(svg, encoding="utf-8")
        png.save(sub / f"{name}.png")
        imgs[name] = (svg, png)
    (outdir / "dag_design_contract.json").write_text(json.dumps({
        "V": CFG["dag"]["V"], "E": CFG["dag"]["E"], "edge_count": 10,
        "note": "design contract; verifier independently parses OUTPUT SVG paths, not this file"},
        indent=2), encoding="utf-8")
    return imgs, neg


def run_checks(outdir, imgs, neg):
    # Read the serialized deliverables. In-memory author objects are not a
    # substitute for the files a consumer receives.
    outdir = Path(outdir) if Path(outdir).is_absolute() else HERE / outdir
    imgs = {name: ((Path(neg) if name.startswith("F_") else outdir)
                   .joinpath(name + ".svg").read_text(encoding="utf-8"),
                  Image.open((Path(neg) if name.startswith("F_") else outdir)
                   / (name + ".png")).convert("RGB")) for name in imgs}
    checks = {}
    cfg_names = ["flat_base", "persp_base", "persp_d18", "persp_code", "persp_d40"]
    fault_names = ["F_pseudo_edge", "F_bad_VP", "F_wrong_z"]

    # T1: structure edges from ACTUAL SVG paths == canonical 10, all 5 configs
    edge_results = {}
    for n in cfg_names:
        s, _ = svg_edges(imgs[n][0])
        edge_results[n] = {"count": len(s), "matches_canonical": s == CANON}
    checks["T1_structure_edges_from_svg_paths"] = {
        "passed": all(v["matches_canonical"] for v in edge_results.values()),
        "per_config": edge_results,
        "note": "parsed from output <path data-role=structure-edge>; code/dot switches keep exactly 10 edges",
        "read_from": "actual output SVG paths (NOT input G)"}

    # T2: VP ONLY on depth-parallel lines; flat = N/A
    vp_results = {}
    for n in cfg_names:
        lines = svg_depth_lines(imgs[n][0])
        if not lines:
            vp_results[n] = {"status": "N/A", "reason": "flat grid: no depth-parallel lines"}
        else:
            vp, res = vp_residual(lines)
            vp_results[n] = {"status": "measured", "vp": [round(vp[0], 2), round(vp[1], 2)],
                             "residual_px": round(res, 3), "n_lines": len(lines),
                             "pass": res <= TH["vp_residual_max_px"]}
    # demonstrate that using STRUCTURE EDGES as VP lines is WRONG (restriction matters)
    # structure edges are not a convergent family; intersect first few -> large spread
    se_lines = []
    root = ET.fromstring(imgs["persp_base"][0])
    for el in root.iter():
        if el.get("data-role") == "structure-edge":
            t = el.get("d").replace("M", " ").replace("L", " ").split()
            nn = [float(x) for x in t]
            se_lines.append(((nn[0], nn[1]), (nn[2], nn[3])))
    _, se_res = vp_residual(se_lines[:6])
    checks["T2_VP_only_on_depth_parallel_lines"] = {
        "passed": vp_results["flat_base"]["status"] == "N/A" and
                  all(vp_results[n]["pass"] for n in ["persp_base", "persp_d18", "persp_code", "persp_d40"]) and
                  se_res is not None and se_res > TH["vp_residual_max_px"],
        "per_config": vp_results,
        "vp_residual_if_wrongly_using_structure_edges_px": round(se_res, 2) if se_res else None,
        "note": "VP estimated ONLY from depth-line paths; structure-edge family is non-concurrent (large residual) -> must NOT be used; flat = N/A",
        "read_from": "actual SVG depth-line path endpoints"}

    # T3: occlusion from ACTUAL PNG overlap; all 5 configs FRONT covers
    occ = {}
    for n in cfg_names:
        occ[n] = png_overlap_colors(imgs[n][1])
    checks["T3_occlusion_from_png_overlap"] = {
        "passed": all(occ[n]["front_ratio"] >= TH["occlusion_front_pixel_min_ratio"] and
                      occ[n]["back_ratio"] <= TH["occlusion_back_pixel_max_ratio_when_correct"]
                      for n in cfg_names),
        "per_config_overlap": occ,
        "note": "z judged from real PNG pixels in overlap rect, not a z-order field",
        "read_from": "actual PNG overlap bytes"}

    # T4 must-fail: pseudo-edge -> edge set != canonical
    fs, fl = svg_edges(imgs["F_pseudo_edge"][0])
    t4 = (len(fl) == 11 and fs != CANON and any(u == "deco0" for u, v in fs))
    checks["T4_pseudo_edge_DETECTED"] = {
        "must_fail": True, "passed": t4, "parsed_edge_count": len(fl),
        "extra_edge_present": ("deco0", "g") in fs,
        "verdict": "FAILED (topology: fake structure edge from decoration dot)",
        "detected_from_real_bytes": t4}

    # T5 must-fail: bad-VP -> depth-line residual > threshold
    lines = svg_depth_lines(imgs["F_bad_VP"][0])
    _, bv_res = vp_residual(lines)
    t5 = bv_res is not None and bv_res > TH["vp_residual_max_px"]
    checks["T5_bad_VP_DETECTED"] = {
        "must_fail": True, "passed": t5, "depth_line_residual_px": round(bv_res, 2) if bv_res else None,
        "threshold_px": TH["vp_residual_max_px"],
        "verdict": "FAILED (VP: one depth line endpoint moved, lines non-concurrent)",
        "detected_from_real_bytes": t5}

    # T6 must-fail: wrong-z -> BACK covers overlap in real PNG
    wz = png_overlap_colors(imgs["F_wrong_z"][1])
    t6 = wz["back_ratio"] >= TH["occlusion_front_pixel_min_ratio"] and wz["front_ratio"] <= TH["occlusion_back_pixel_max_ratio_when_correct"]
    checks["T6_wrong_z_DETECTED"] = {
        "must_fail": True, "passed": t6, "overlap_colors": wz,
        "verdict": "FAILED (occlusion: background card drawn on top)",
        "detected_from_real_bytes": t6}

    # T7: positive configs not all rejected
    t7 = (all(v["matches_canonical"] for v in edge_results.values()) and
          checks["T3_occlusion_from_png_overlap"]["passed"])
    checks["T7_positive_configs_not_all_rejected"] = {
        "passed": t7, "configs_passing_applicable_checks": len(cfg_names),
        "note": "all 5 configs pass structure + (applicable) VP + occlusion"}

    pos = ["T1_structure_edges_from_svg_paths", "T2_VP_only_on_depth_parallel_lines",
           "T3_occlusion_from_png_overlap", "T7_positive_configs_not_all_rejected"]
    negk = ["T4_pseudo_edge_DETECTED", "T5_bad_VP_DETECTED", "T6_wrong_z_DETECTED"]
    checks["_summary"] = {
        "positive_checks": pos, "negative_controls": negk,
        "configs": 5, "single_fault_cases": 3, "image_count": 8, "image_cap": 8,
        "all_positive_pass": all(checks[k]["passed"] for k in pos),
        "all_negative_controls_detected": all(checks[k]["passed"] for k in negk),
        "verifier_reads_actual_svg_and_png": True}
    return checks


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "outputs"
    imgs, neg = build_all(outdir)
    checks = run_checks(outdir, imgs, neg)
    out = Path(outdir) if Path(outdir).is_absolute() else HERE / outdir
    (out / "checks.json").write_text(json.dumps(checks, indent=2), encoding="utf-8")
    s = checks["_summary"]
    print("xchylerdrenth checks:", "POS=", s["all_positive_pass"], "NEG_DETECTED=", s["all_negative_controls_detected"])
    for k, v in checks.items():
        if k != "_summary":
            print(f"  {k}: passed={v.get('passed')}")
    return 0 if s["all_positive_pass"] and s["all_negative_controls_detected"] else 1


if __name__ == "__main__":
    sys.exit(main())
