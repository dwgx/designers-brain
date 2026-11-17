#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S12-B / AnnasXechoes LOCAL mechanism prototype (author SeedDepsB).

Self-drawn vessel, FIXED composition. 2x2 geometry-semantics x surface-treatment
(4 images) + a NEW vessel baseline/full-treatment (2 images) = 6 images total.

Two DISJOINT color channels make the two factors independently measurable from
REAL PNG bytes: FORM (dark) changes with geometry, SURFACE (light) changes with
surface treatment. Both only inside registered part masks; outside-mask diff
must be zero. Negative controls are real files that MUST fail.

Deterministic: Pillow only, NO RNG, NO network, NO author/reference media.
Run: python -X utf8 build.py <outdir>
"""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
CFG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
W, H = CFG["canvas"]["W"], CFG["canvas"]["H"]
BG = tuple(CFG["canvas"]["background_rgb"])
MASKS = {k: tuple(v) for k, v in CFG["part_masks_px"].items()}
PARTS = CFG["parts"]
FORM = tuple(CFG["color_roles_rgb"]["form_dark"])
STEX = tuple(CFG["color_roles_rgb"]["surface_tex"])
SHI = tuple(CFG["color_roles_rgb"]["surface_highlight"])
TH = CFG["thresholds"]
BOX = tuple(CFG["fixed_composition"]["bounding_box_px"])


def near(px, target, tol=18):
    return all(abs(px[i] - target[i]) <= tol for i in range(3))


def in_mask(x, y, masks):
    for name, (x0, y0, x1, y1) in masks.items():
        if x0 <= x < x1 and y0 <= y < y1:
            return name
    return None


def draw_base():
    """Fixed composition: background + bounding box + registration frame.
    Byte-identical across all 6 stimuli (no per-config variation here)."""
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    x0, y0, x1, y1 = BOX
    d.rectangle([x0, y0, x1, y1], outline=(210, 206, 198), width=2)
    # fixed light-direction cue (top-left): a small constant corner marker
    d.line([(x0 + 8, y0 + 8), (x0 + 26, y0 + 8)], fill=(200, 196, 188), width=2)
    return img


def draw_form(d, part, geom, vessel):
    """Draw the vessel part FORM inside its mask, in FORM_DARK color."""
    x0, y0, x1, y1 = MASKS[part]
    if part == "handle":
        if geom == "G0_ordinary":
            # open arc (stroked) inside handle mask
            cx, cy, r = (x0 + x1) // 2, (y0 + y1) // 2 + 10, 34
            d.arc([cx - r, cy - r - 6, cx + r, cy + r - 6], start=200, end=340,
                  fill=FORM, width=7)
        else:
            # closed ring (stroked circle)
            cx, cy, r = (x0 + x1) // 2, (y0 + y1) // 2, 34
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=FORM, width=7)
    elif part == "clasp":
        if geom == "G0_ordinary":
            # filled small rect
            d.rectangle([x0 + 14, y0 + 12, x1 - 14, y1 - 12], fill=FORM)
        else:
            # seal window: outer rect ring + inner cross (different form pixel count)
            d.rectangle([x0 + 10, y0 + 8, x1 - 10, y1 - 8], outline=FORM, width=6)
            cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
            d.line([(cx, y0 + 14), (cx, y1 - 14)], fill=FORM, width=5)
            d.line([(x0 + 16, cy), (x1 - 16, cy)], fill=FORM, width=5)
    elif part == "body":
        if vessel == "v1":
            d.rounded_rectangle([x0 + 12, y0 + 10, x1 - 12, y1 - 12], radius=22,
                                outline=FORM, width=6)
            # a fixed base seam (v1 detail, constant for both geometries)
            d.line([(x0 + 20, y1 - 40), (x1 - 20, y1 - 40)], fill=FORM, width=3)
        else:
            # tall box v2 (DIFFERENT self-drawn everyday container)
            d.rectangle([x0 + 30, y0 + 6, x1 - 30, y1 - 8], outline=FORM, width=6)
            d.line([(x0 + 40, y0 + 30), (x1 - 40, y0 + 30)], fill=FORM, width=3)


def draw_surface(img, part, surface, shift=(0, 0)):
    """Overlay SURFACE treatment INSIDE the part mask using disjoint LIGHT colors.

    CRITICAL: never overwrite FORM_DARK pixels. Surface is composited ONLY onto
    pixels that are not the form color, so the FORM channel stays byte-invariant
    when only the surface factor changes (true separate localizability).
    """
    if surface == "S0_matte":
        return
    x0, y0, x1, y1 = MASKS[part]
    dx, dy = shift
    x0, y0, x1, y1 = x0 + dx, y0 + dy, x1 + dx, y1 + dy
    px = img.load()

    def put(x, y, color):
        if 0 <= x < W and 0 <= y < H and not near(px[x, y], FORM, tol=24):
            px[x, y] = color

    n = CFG["surface_treatment"]["S1_opposed"]["texture_lines"]
    for i in range(n):
        yy = y0 + 6 + (i + 1) * (y1 - y0 - 12) // (n + 1)
        for xx in range(x0 + 8, x1 - 8):
            put(xx, yy, STEX)
    for yy in range(y0 + 6, y0 + 16):           # broad highlight
        for xx in range(x0 + 10, x1 - 10):
            put(xx, yy, SHI)
    for yy in range(y1 - 14, y1 - 8):           # narrow highlight
        for xx in range(x0 + 10, x0 + 40):
            put(xx, yy, SHI)


def build_image(geom, surface, vessel, wrong_mask_shift=None, role_field_only=False):
    img = draw_base()
    d = ImageDraw.Draw(img)
    # FORM layer (varies with geometry)
    for p in PARTS:
        draw_form(d, p, geom, vessel)
    # SURFACE layer (varies with surface; composited onto NON-form pixels only)
    for p in PARTS:
        if wrong_mask_shift is not None:
            draw_surface(img, p, surface, shift=wrong_mask_shift)
        else:
            draw_surface(img, p, surface)
    return img

def metric_form(img, masks=MASKS):
    """Count FORM_DARK pixels per mask (geometry signal)."""
    px, out = img.load(), {p: 0 for p in PARTS}
    for p, (x0, y0, x1, y1) in masks.items():
        for y in range(y0, y1):
            for x in range(x0, x1):
                if near(px[x, y], FORM):
                    out[p] += 1
    return out


def metric_surface(img, masks=MASKS):
    """Count SURFACE light pixels per mask (surface signal)."""
    px, out = img.load(), {p: 0 for p in PARTS}
    for p, (x0, y0, x1, y1) in masks.items():
        for y in range(y0, y1):
            for x in range(x0, x1):
                if near(px[x, y], STEX) or near(px[x, y], SHI):
                    out[p] += 1
    return out


def outside_mask_diff(img_a, img_b, masks=MASKS):
    """Diff pixels OUTSIDE the union of part masks (real PNG bytes)."""
    pa, pb, cnt = img_a.load(), img_b.load(), 0
    for y in range(H):
        for x in range(W):
            if in_mask(x, y, masks) is not None:
                continue
            if pa[x, y] != pb[x, y]:
                cnt += 1
    return cnt


def build_all(outdir):
    outdir = Path(outdir) if Path(outdir).is_absolute() else HERE / outdir
    neg = outdir / "negatives"
    outdir.mkdir(parents=True, exist_ok=True)
    neg.mkdir(parents=True, exist_ok=True)
    imgs = {}
    for stem, geom, surface, vessel in [
        ("v1_G0_S0", "G0_ordinary", "S0_matte", "v1"),
        ("v1_G0_S1", "G0_ordinary", "S1_opposed", "v1"),
        ("v1_G1_S0", "G1_ceremonial", "S0_matte", "v1"),
        ("v1_G1_S1", "G1_ceremonial", "S1_opposed", "v1"),
        ("v2_baseline", "G0_ordinary", "S0_matte", "v2"),
        ("v2_full", "G1_ceremonial", "S1_opposed", "v2"),
    ]:
        im = build_image(geom, surface, vessel)
        im.save(outdir / f"{stem}.png")
        imgs[stem] = im

    # Masks image (verifier artifact, NOT a stimulus): each part a distinct value.
    m = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(m)
    for i, (p, (x0, y0, x1, y1)) in enumerate(MASKS.items(), start=1):
        md.rectangle([x0, y0, x1, y1], fill=60 * i)
    m.save(outdir / "part_masks.png")

    # N1 wrong-mask negative: surface drawn with a SHIFTED mask (offset outside
    # registered masks) -> real nonzero outside-mask diff.
    n1 = build_image("G0_ordinary", "S1_opposed", "v1", wrong_mask_shift=(120, 0))
    n1.save(neg / "N1_wrong_mask.png")
    # N2 role-field-only negative: a config claiming ceremonial, but the PNG is
    # byte-identical to v1_G0_S0 (ZERO pixel change). Verifier must detect no form change.
    imgs["v1_G0_S0"].save(neg / "N2_role_field_only.png")
    (neg / "N2_role_field_claim.json").write_text(json.dumps(
        {"declared_geometry": "G1_ceremonial", "pixels_changed": 0,
         "note": "DELIBERATELY WRONG: only a role field was written; no geometry pixels changed"},
        indent=2), encoding="utf-8")

    # Prediction table (material/narrative INTENT is a prediction, NOT measured effect)
    (outdir / "prediction_only.md").write_text(
        "# Material / narrative intent — PREDICTION ONLY, not measured\n\n"
        "This prototype manipulates geometry and surface as controlled visual stimuli. "
        "Whether a viewer reads 'reliquary', 'sacred', 'precious', 'decayed' or any "
        "narrative/material realism is NOT measured here and stays pending_human. "
        "No answer text is drawn into the images. TzKT+IPFS are treated as possibly one "
        "metadata index+storage (rights None / All Rights Reserved); no reference image "
        "is copied into outputs.\n", encoding="utf-8")
    return imgs, neg


def run_checks(outdir, imgs, neg):
    outdir = Path(outdir) if Path(outdir).is_absolute() else HERE / outdir
    checks = {}
    names = ["v1_G0_S0", "v1_G0_S1", "v1_G1_S0", "v1_G1_S1", "v2_baseline", "v2_full"]

    # Q1: 6 real PNGs; fixed composition byte-identical (compare OUTSIDE masks = 0
    # between the two extreme v1 configs, and background corner pixel equality)
    exist = all((outdir / f"{n}.png").is_file() for n in names)
    checks["Q1_six_stimuli_and_fixed_composition"] = {
        "passed": exist and outside_mask_diff(imgs["v1_G0_S0"], imgs["v1_G1_S1"]) == 0,
        "all_six_exist": exist, "fixed_composition_outside_diff_px": outside_mask_diff(imgs["v1_G0_S0"], imgs["v1_G1_S1"]),
        "read_from": "actual PNG bytes"}

    # Q2: outside-mask diff = 0 for each v1 factor change
    od = {n: outside_mask_diff(imgs["v1_G0_S0"], imgs[n]) for n in names}
    checks["Q2_outside_mask_diff_zero"] = {
        "passed": all(v <= TH["outside_mask_max_diff_px"] for k, v in od.items() if k.startswith("v1")),
        "outside_diff_px": od, "threshold_px": TH["outside_mask_max_diff_px"],
        "read_from": "actual PNG bytes outside union of registered part masks"}

    # Q3: geometry separately localizable (G0_S0 -> G1_S0)
    f_a, s_a = metric_form(imgs["v1_G0_S0"]), metric_surface(imgs["v1_G0_S0"])
    f_g, s_g = metric_form(imgs["v1_G1_S0"]), metric_surface(imgs["v1_G1_S0"])
    form_delta = {p: f_g[p] - f_a[p] for p in PARTS}
    surf_delta_on_geometry = {p: abs(s_g[p] - s_a[p]) for p in PARTS}
    geom_ok = (form_delta["handle"] >= TH["form_count_change_min_px"] and
               form_delta["clasp"] >= TH["form_count_change_min_px"] and
               abs(form_delta["body"]) <= TH["cross_attribution_max_form_delta_px"] and
               all(v <= TH["cross_attribution_max_surface_delta_px"] for v in surf_delta_on_geometry.values()))
    checks["Q3_geometry_separately_localizable"] = {
        "passed": geom_ok, "form_pixel_delta_per_part": form_delta,
        "surface_pixel_delta_when_only_geometry_changed": surf_delta_on_geometry,
        "note": "form changes in handle+clasp, body form unchanged, surface channel unchanged",
        "read_from": "actual PNG bytes (disjoint FORM/SURFACE colors)"}

    # Q4: surface separately localizable (G0_S0 -> G0_S1)
    f_s, s_s = metric_form(imgs["v1_G0_S1"]), metric_surface(imgs["v1_G0_S1"])
    surf_delta = {p: s_s[p] - s_a[p] for p in PARTS}
    form_delta_on_surface = {p: abs(f_s[p] - f_a[p]) for p in PARTS}
    surf_ok = (sum(surf_delta.values()) >= TH["surface_tex_change_min_px"] and
               all(v <= TH["cross_attribution_max_form_delta_px"] for v in form_delta_on_surface.values()))
    checks["Q4_surface_separately_localizable"] = {
        "passed": surf_ok, "surface_pixel_delta_per_part": surf_delta,
        "form_pixel_delta_when_only_surface_changed": form_delta_on_surface,
        "note": "surface channel changes, FORM channel unchanged",
        "read_from": "actual PNG bytes (disjoint colors)"}

    # Q5: vessel2 baseline->full changes BOTH form and surface, outside-mask diff 0
    f2b, s2b = metric_form(imgs["v2_baseline"]), metric_surface(imgs["v2_baseline"])
    f2f, s2f = metric_form(imgs["v2_full"]), metric_surface(imgs["v2_full"])
    v2_form = sum(abs(f2f[p] - f2b[p]) for p in PARTS)
    v2_surf = sum(abs(s2f[p] - s2b[p]) for p in PARTS)
    v2_od = outside_mask_diff(imgs["v2_baseline"], imgs["v2_full"])
    checks["Q5_vessel2_transfer_stimulus"] = {
        "passed": v2_form >= TH["form_count_change_min_px"] and v2_surf >= TH["surface_tex_change_min_px"] and v2_od == 0,
        "form_delta_total": v2_form, "surface_delta_total": v2_surf,
        "outside_mask_diff_px": v2_od, "read_from": "actual PNG bytes"}

    # N1 must-fail: wrong-mask -> nonzero outside-mask diff DETECTED
    n1 = Image.open(neg / "N1_wrong_mask.png").convert("RGB")
    n1_od = outside_mask_diff(imgs["v1_G0_S1"], n1)  # both S1, only mask shifted
    n1_detected = n1_od > TH["outside_mask_max_diff_px"]
    checks["N1_wrong_mask_DETECTED"] = {
        "must_fail": True, "passed": n1_detected,
        "verdict": "FAILED (wrong mask: surface texture applied outside registered part masks -> nonzero outside-mask diff)",
        "outside_diff_px_vs_correct_S1": n1_od,
        "note": "surface texture applied at shifted mask; verifier reads real outside-mask diff",
        "detected_from_real_bytes": n1_detected}

    # N2 must-fail: role-field-only -> form_pixels did NOT change DETECTED
    n2 = Image.open(neg / "N2_role_field_only.png").convert("RGB")
    n2_claim = json.loads((neg / "N2_role_field_claim.json").read_text(encoding="utf-8"))
    n2_form_delta = sum(abs(metric_form(n2)[p] - f_a[p]) for p in PARTS)
    n2_detected = n2_claim["declared_geometry"] == "G1_ceremonial" and n2_form_delta <= TH["cross_attribution_max_form_delta_px"]
    checks["N2_role_field_only_DETECTED"] = {
        "must_fail": True, "passed": n2_detected,
        "declared_geometry_in_config": n2_claim["declared_geometry"],
        "verdict": "FAILED (role-field-only: a config claim says ceremonial but ZERO pixels changed -> no mechanism)",
        "note": "DELIBERATELY byte-identical to v1_G0_S0.png: only a false JSON role claim was written. Printing a material/part name does NOT touch the visual mechanism; verifier reads real PNG form bytes, not the claim.",
        "detected_from_real_bytes": n2_detected}

    pos = ["Q1_six_stimuli_and_fixed_composition", "Q2_outside_mask_diff_zero",
           "Q3_geometry_separately_localizable", "Q4_surface_separately_localizable",
           "Q5_vessel2_transfer_stimulus"]
    negk = ["N1_wrong_mask_DETECTED", "N2_role_field_only_DETECTED"]
    checks["_summary"] = {
        "positive_checks": pos, "negative_controls": negk,
        "image_count": 6, "image_cap": 6,
        "all_positive_pass": all(checks[k]["passed"] for k in pos),
        "all_negative_controls_detected": all(checks[k]["passed"] for k in negk),
        "verifier_reads_real_png_bytes": True}
    return checks


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "outputs"
    imgs, neg = build_all(outdir)
    checks = run_checks(outdir, imgs, neg)
    out = Path(outdir) if Path(outdir).is_absolute() else HERE / outdir
    (out / "checks.json").write_text(json.dumps(checks, indent=2), encoding="utf-8")
    s = checks["_summary"]
    print("AnnasXechoes checks:", "POS=", s["all_positive_pass"], "NEG_DETECTED=", s["all_negative_controls_detected"])
    for k, v in checks.items():
        if k != "_summary":
            print(f"  {k}: passed={v.get('passed')}")
    return 0 if s["all_positive_pass"] and s["all_negative_controls_detected"] else 1


if __name__ == "__main__":
    sys.exit(main())
