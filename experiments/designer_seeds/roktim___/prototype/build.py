#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S12-B / roktim___ LOCAL mechanism prototype (author SeedDepsB).

Same label frame, 4 cards: no-label / readable synthetic data / decorative
value explicitly marked / annotation-removed negative. Computed value comes
from a self-authored small array (synthetic fixture), NOT product telemetry.

The verifier reads ACTUAL SVG <text data-role=...> bytes; removing the
annotation or tampering the computed value MUST be detected as a failure.

Deterministic: stdlib + Pillow only, NO RNG, NO network, NO author media.
Run: python -X utf8 build.py <outdir>
"""
import json, sys, hashlib
from pathlib import Path
from xml.etree import ElementTree as ET
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
CFG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
W, H = CFG["canvas"]["W"], CFG["canvas"]["H"]
BG = tuple(CFG["canvas"]["background_rgb"])
INK = tuple(CFG["fixed_frame"]["colors"]["ink"])
ACCENT = tuple(CFG["fixed_frame"]["colors"]["accent"])
WARN = tuple(CFG["fixed_frame"]["colors"]["warn"])
LB = tuple(CFG["fixed_frame"]["label_box_px"])
FX = CFG["synthetic_fixture"]
ARR = FX["array"]
TOL = CFG["thresholds"]["value_tolerance"]

# fixed text positions per semantic role
POS = {
    "fig":       (52, 40),
    "title":     (52, 66),
    "n":         (52, 262),
    "value":     (52, 286),
    "unit":      (200, 286),
    "source":    (52, 310),
    "note":      (52, 332),
    "decorative-marker": (52, 310),
}

# computed values (from the array, by run code)
MEAN = sum(ARR) / len(ARR)
COUNT = len(ARR)
ARR_HASH = hashlib.sha256(json.dumps(ARR).encode()).hexdigest()[:16]


def recompute(array):
    return sum(array) / len(array), len(array), min(array), max(array)


def base_draw():
    """Fixed neutral geometric background + label frame (byte-identical base)."""
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # fixed 8px dotted grid
    for x in range(0, W, 32):
        for y in range(0, H, 32):
            d.point((x, y), fill=(222, 222, 218))
    # a self-drawn abstract neutral mark (NOT a classical artwork)
    d.ellipse([190, 90, 322, 222], outline=(205, 205, 200), width=2)
    d.line([(256, 90), (256, 222)], fill=(215, 215, 210), width=1)
    d.line([(190, 156), (322, 156)], fill=(215, 215, 210), width=1)
    # label frame (fixed box)
    x0, y0, x1, y1 = LB
    d.rectangle([x0, y0, x1, y1], outline=(60, 62, 64), width=2)
    return img


def build_card_svg(card, texts, decorative=False):
    """texts: list of (role, string, color, size). SVG <text> is authoritative."""
    svg = ET.Element("svg", {"xmlns": "http://www.w3.org/2000/svg",
                              "width": str(W), "height": str(H), "viewBox": f"0 0 {W} {H}",
                              "data-card": card, "data-decorative": "1" if decorative else "0",
                              "data-array-hash16": ARR_HASH,
                              "data-mean": f"{MEAN:.4f}"})
    ET.SubElement(svg, "rect", {"x": "0", "y": "0", "width": str(W), "height": str(H),
                                 "fill": "#f6f6f4", "data-role": "background"})
    g = ET.SubElement(svg, "g", {"data-role": "text-layer"})
    for role, s, color, size in texts:
        x, y = POS[role]
        t = ET.SubElement(g, "text", {"x": str(x), "y": str(y),
                                       "font-family": "monospace", "font-size": str(size),
                                       "fill": color, "data-role": role})
        t.text = s
    # label frame as SVG rect (fixed composition)
    ET.SubElement(svg, "rect", {"x": str(LB[0]), "y": str(LB[1]),
                                 "width": str(LB[2] - LB[0]), "height": str(LB[3] - LB[1]),
                                 "fill": "none", "stroke": "#3c3e40", "stroke-width": "2",
                                 "data-role": "label-frame"})
    ET.indent(svg, space="  ")
    return ET.tostring(svg, encoding="unicode")


def render_card_png(svg_text):
    """Rasterise the same readable text with Pillow default font (deterministic)."""
    root = ET.fromstring(svg_text)
    img = base_draw()
    d = ImageDraw.Draw(img)
    for el in root.iter():
        if el.tag.split("}")[-1] == "text" and el.get("data-role"):
            role = el.get("data-role")
            x, y = POS[role]
            fill = INK
            if role == "decorative-marker":
                fill = WARN
            elif role == "value":
                fill = ACCENT
            d.text((x, y - 12), el.text or "", fill=fill)
    return img


def hexs(rgb):
    return "#%02x%02x%02x" % rgb


def card_texts(card):
    """Return (svg, png) for one of the 4 cards, plus metadata."""
    if card == "C1_no_label":
        # no semantic-role text at all; frame present but EMPTY
        svg = build_card_svg(card, [], decorative=False)
        return svg, render_card_png(svg)
    if card == "C2_readable_synthetic":
        texts = [
            ("fig", "FIG. 28", hexs(INK), 16),
            ("title", "SYNTHETIC FIXTURE / TELEMETRY LABEL", hexs(INK), 15),
            ("n", f"N={COUNT} samples", hexs(INK), 15),
            ("value", f"mean = {MEAN:.1f}", hexs(ACCENT), 20),
            ("unit", "ms (fixture unit)", hexs(INK), 14),
            ("source", f"source: synthetic array sha16={ARR_HASH}", hexs(INK), 13),
            ("note", "SYNTHETIC / mean(array) / NOT a product measurement", hexs(INK), 13),
        ]
        svg = build_card_svg(card, texts, decorative=False)
        return svg, render_card_png(svg)
    if card == "C3_decorative_marked":
        texts = [
            ("fig", "FIG. 28", hexs(INK), 16),
            ("title", "DECORATIVE VALUE CARD", hexs(INK), 15),
            ("n", f"N={COUNT} samples", hexs(INK), 15),
            ("value", "value = 99.7", hexs(ACCENT), 20),
            ("unit", "ms (decorative)", hexs(INK), 14),
            ("decorative-marker", "ILLUSTRATIVE / NOT PERFORMANCE DATA", hexs(WARN), 15),
            ("note", "synthetic decoration only / no computed claim", hexs(INK), 13),
        ]
        svg = build_card_svg(card, texts, decorative=True)
        return svg, render_card_png(svg)
    if card == "C4_annotation_removed":
        # card3 with the decorative-marker AND note annotation REMOVED
        texts = [
            ("fig", "FIG. 28", hexs(INK), 16),
            ("title", "DECORATIVE VALUE CARD", hexs(INK), 15),
            ("n", f"N={COUNT} samples", hexs(INK), 15),
            ("value", "value = 99.7", hexs(ACCENT), 20),
            ("unit", "ms (decorative)", hexs(INK), 14),
        ]
        svg = build_card_svg(card, texts, decorative=True)
        return svg, render_card_png(svg)
    raise ValueError(card)


def build_all(outdir):
    outdir = Path(outdir) if Path(outdir).is_absolute() else HERE / outdir
    neg = outdir / "negatives"
    outdir.mkdir(parents=True, exist_ok=True)
    neg.mkdir(parents=True, exist_ok=True)
    cards = {}
    for card in ["C1_no_label", "C2_readable_synthetic", "C3_decorative_marked", "C4_annotation_removed"]:
        svg, png = card_texts(card)
        (outdir / f"{card}.svg").write_text(svg, encoding="utf-8")
        png.save(outdir / f"{card}.png")
        cards[card] = (svg, png)
    # N_tamper: one-off copy of C2 with the computed value text CHANGED.
    root = ET.fromstring(cards["C2_readable_synthetic"][0])
    for el in root.iter():
        if el.get("data-role") == "value":
            el.text = "mean = 71.3"   # DELIBERATELY WRONG (recompute = 14.0)
    ET.indent(root, space="  ")
    tamper_svg = ET.tostring(root, encoding="unicode")
    (neg / "N_tamper_value.svg").write_text(tamper_svg, encoding="utf-8")
    render_card_png(tamper_svg).save(neg / "N_tamper_value.png")
    # fixture ledger (real computed values)
    (outdir / "fixture_ledger.json").write_text(json.dumps({
        "array": ARR, "array_sha256": hashlib.sha256(json.dumps(ARR).encode()).hexdigest(),
        "computed": {"mean": MEAN, "count": COUNT, "min": min(ARR), "max": max(ARR)},
        "formula": FX["formula"], "unit": FX["unit_value"],
        "note": FX["note"], "brief_3_lines": FX["brief_3_lines"],
    }, indent=2), encoding="utf-8")
    return cards, neg


# ---- verifier reads ACTUAL SVG <text> bytes ----
def read_text_roles(svg_text):
    root = ET.fromstring(svg_text)
    out = {}
    for el in root.iter():
        if el.tag.split("}")[-1] == "text" and el.get("data-role"):
            out.setdefault(el.get("data-role"), []).append(el.text or "")
    return root, out


def parse_value(role_texts):
    # "mean = 14.0" -> 14.0
    for t in role_texts:
        if "=" in t:
            try:
                return float(t.split("=")[1].strip())
            except ValueError:
                pass
    return None


def run_checks(outdir, cards, neg):
    outdir = Path(outdir) if Path(outdir).is_absolute() else HERE / outdir
    checks = {}

    # R1: C2 readable from actual SVG text + value == recompute
    _, c2 = read_text_roles(cards["C2_readable_synthetic"][0])
    have = all(k in c2 for k in ["value", "unit", "source", "note"])
    v = parse_value(c2.get("value", []))
    rc, rn, rmin, rmax = recompute(ARR)
    consistent = v is not None and abs(v - rc) <= TOL
    source_ok = any(ARR_HASH in s for s in c2.get("source", []))
    checks["R1_C2_readable_and_value_consistent"] = {
        "passed": have and consistent and source_ok,
        "roles_present": sorted(c2.keys()), "value_from_svg_text": v,
        "recomputed_mean": rc, "array_sha16_visible": ARR_HASH, "source_matches_array": source_ok,
        "read_from": "actual SVG <text data-role> bytes"}

    # R2: C3 decorative marker present as real SVG text
    root3, c3 = read_text_roles(cards["C3_decorative_marked"][0])
    marker = " ".join(c3.get("decorative-marker", []))
    checks["R2_C3_decorative_marker"] = {
        "passed": root3.get("data-decorative") == "1" and "ILLUSTRATIVE" in marker and "NOT PERFORMANCE DATA" in marker,
        "marker_text": marker, "data-decorative": root3.get("data-decorative"),
        "read_from": "actual SVG attribute + <text> bytes"}

    # R3: distinct semantic roles (FIG/N/VALUE) read by data-role, NOT regex.
    # Demonstrate a naive regex WOULD conflate them (extracts all numbers as one bag).
    import re
    all_svg_text = cards["C2_readable_synthetic"][0]
    naive_numbers = re.findall(r"\d+\.?\d*", all_svg_text)
    distinct = (len({r for r in ["fig", "n", "value"] if r in c2}) == 3 and
                c2.get("fig") and c2.get("n") and c2.get("value"))
    checks["R3_semantic_roles_distinct"] = {
        "passed": distinct and len(set(naive_numbers)) >= 4,
        "fig_text": c2.get("fig"), "n_text": c2.get("n"), "value_text": c2.get("value"),
        "naive_regex_number_bag": naive_numbers,
        "note": "verifier reads by data-role; a naive regex would mix FIG.28 / N=8 / mean=14.0 / sha hash digits into one unlabeled bag",
        "read_from": "actual SVG data-role attributes"}

    # R6: C1 no-label has ZERO semantic-role <text>
    _, c1 = read_text_roles(cards["C1_no_label"][0])
    checks["R6_C1_no_label"] = {
        "passed": len(c1) == 0, "semantic_roles": sorted(c1.keys()),
        "read_from": "actual SVG <text> bytes"}

    # R4 must-fail: C4 annotation-removed -> contract check DETECTS missing annotation
    _, c4 = read_text_roles(cards["C4_annotation_removed"][0])
    has_marker = "decorative-marker" in c4 and "ILLUSTRATIVE" in " ".join(c4["decorative-marker"])
    has_note = "note" in c4 and len(c4["note"]) > 0
    missing = not (has_marker and has_note)
    # contract check that would wrongly pass if annotations existed:
    annotation_present_would_pass = has_marker and has_note
    checks["R4_annotation_removed_DETECTED"] = {
        "must_fail": True, "passed": missing,
        "decorative_marker_present": has_marker, "note_present": has_note,
        "verdict": "FAILED (annotation missing) -> label contract is absent, as required",
        "note": "expected failure = missing LABEL CONTRACT, NOT an observed human misreading",
        "detected_from_real_bytes": missing}

    # R5 must-fail: N_tamper value mismatch -> verifier DETECTS
    t_svg = (neg / "N_tamper_value.svg").read_text(encoding="utf-8")
    _, ct = read_text_roles(t_svg)
    tv = parse_value(ct.get("value", []))
    mismatch = tv is not None and abs(tv - rc) > TOL
    checks["R5_tampered_value_DETECTED"] = {
        "must_fail": True, "passed": mismatch,
        "tampered_value_from_svg": tv, "recomputed_mean": rc,
        "verdict": "FAILED (value != source recomputation)",
        "detected_from_real_bytes": mismatch}

    pos = ["R1_C2_readable_and_value_consistent", "R2_C3_decorative_marker",
           "R3_semantic_roles_distinct", "R6_C1_no_label"]
    negk = ["R4_annotation_removed_DETECTED", "R5_tampered_value_DETECTED"]
    checks["_summary"] = {
        "positive_checks": pos, "negative_controls": negk,
        "cards": 4, "card_cap": 4,
        "all_positive_pass": all(checks[k]["passed"] for k in pos),
        "all_negative_controls_detected": all(checks[k]["passed"] for k in negk),
        "verifier_reads_actual_svg_text": True}
    return checks


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "outputs"
    cards, neg = build_all(outdir)
    checks = run_checks(outdir, cards, neg)
    out = Path(outdir) if Path(outdir).is_absolute() else HERE / outdir
    (out / "checks.json").write_text(json.dumps(checks, indent=2), encoding="utf-8")
    s = checks["_summary"]
    print("roktim___ checks:", "POS=", s["all_positive_pass"], "NEG_DETECTED=", s["all_negative_controls_detected"])
    for k, v in checks.items():
        if k != "_summary":
            print(f"  {k}: passed={v.get('passed')}")
    return 0 if s["all_positive_pass"] and s["all_negative_controls_detected"] else 1


if __name__ == "__main__":
    sys.exit(main())
