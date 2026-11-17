#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S05 kail_designs LOCAL mechanism prototype (CANDIDATE HYPOTHESIS, NOT E3).

Small SELF-CREATED luminance field + EXPLICIT exposure / halo / grain toggles,
FOUR variants max. Coordinate-deterministic (NO random module, NO seed).
Pure stdlib + Pillow. No image API, no WebGL, no author artwork, no ffmpeg.
This is ONE self-authored pass stack, NOT two product pages conflated into a
proven shader pipeline.
"""
import sys, json, hashlib
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else (HERE / "outputs")
OUT.mkdir(parents=True, exist_ok=True)
CFG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))

W = CFG["field"]["width"]; H = CFG["field"]["height"]
BR = CFG["field"]["bright_region"]
HR = CFG["field"]["halo_region"]
FR = CFG["field"]["flat_region"]
TG = CFG["toggles"]
VARIANTS = CFG["variants_at_most_four"]


def in_rect(x, y, r):
    return r["x0"] <= x <= r["x1"] and r["y0"] <= y <= r["y1"]


def clamp(v):
    return 0 if v < 0 else (255 if v > 255 else int(round(v)))


def grain(x, y):
    # coordinate-deterministic signed pattern, NO random state, NOT a website seed
    return ((x*73 + y*151 + x*y*7) % 41) - 20


# ---- 1. self-created base luminance field (raw code values 0..255) ----
base = []
for y in range(H):
    row = []
    for x in range(W):
        v = 20.0 + (235.0 - 20.0) * x / (W - 1)   # horizontal linear ramp
        if in_rect(x, y, FR):
            v = FR["value"]                        # flat patch
        if in_rect(x, y, BR):
            v = BR["value"]                        # bright region (halo source)
        row.append(v)
    base.append(row)

# expose the raw base array as evidence (JSON 2D list) + PNG
(OUT / "input_field.json").write_text(json.dumps({
    "units": "raw 8-bit grayscale code value 0..255 (self-created, NOT sRGB photography)",
    "width": W, "height": H, "field": base,
    "bright_region": BR, "halo_region": HR, "flat_region": FR,
    "note": "coordinate-deterministic field; no RNG."
}, ensure_ascii=False, indent=1), encoding="utf-8")
def save_png(grid, name):
    im = Image.new("L", (W, H))
    p = im.load()
    for y in range(H):
        for x in range(W):
            p[x, y] = clamp(grid[y][x])
    im.save(OUT / name)
save_png(base, "input_field.png")

# ---- 2. operators (explicit, declared order: exposure -> halo -> grain) ----
def ops(grid, vcfg):
    out = [row[:] for row in grid]
    # exposure: multiplicative gain on code values
    if vcfg["exposure"]:
        g = TG["exposure"]["gain"]
        out = [[v * g for v in row] for row in out]
    # halo: local box-mean contribution from the bright region to the halo ring
    if vcfg["halo"]:
        mean_br = sum(base[y][x] for y in range(BR["y0"], BR["y1"]+1)
                      for x in range(BR["x0"], BR["x1"]+1)) / ((BR["x1"]-BR["x0"]+1)*(BR["y1"]-BR["y0"]+1))
        rad = TG["halo"]["radius_px"]; gain = TG["halo"]["gain"]
        for y in range(H):
            for x in range(W):
                if in_rect(x, y, HR) and not in_rect(x, y, BR):
                    # distance from bright-rect border (Manhattan-ish, clamped)
                    dx = max(BR["x0"]-x, x-BR["x1"], 0)
                    dy = max(BR["y0"]-y, y-BR["y1"], 0)
                    d = max(dx, dy)
                    falloff = max(0.0, 1.0 - d / (rad + 1.0))
                    out[y][x] += gain * mean_br * falloff
    # grain: coordinate-deterministic signed noise
    if vcfg["grain"]:
        amp = TG["grain"]["amplitude"]
        out = [[out[y][x] + amp * (grain(x, y) / 20.0) for x in range(W)] for y in range(H)]
    return out


def clipped_counts(grid):
    flat = [clamp(v) for row in grid for v in row]
    return {"at_0": sum(1 for v in flat if v == 0), "at_255": sum(1 for v in flat if v == 255)}


def region_mean(grid, r):
    vals = [grid[y][x] for y in range(H) for x in range(W) if in_rect(x, y, r)]
    return sum(vals) / len(vals) if vals else 0.0


def diff_stats(a, b):
    """a,b raw float grids; diff on CLAMPED output bytes."""
    overall = bright = halo = flat = 0.0
    nb = nh = nf = 0
    for y in range(H):
        for x in range(W):
            d = abs(clamp(a[y][x]) - clamp(b[y][x]))
            overall += d
            if in_rect(x, y, BR): bright += d; nb += 1
            if in_rect(x, y, HR) and not in_rect(x, y, BR): halo += d; nh += 1
            if in_rect(x, y, FR): flat += d; nf += 1
    n = W * H
    return {"mean_abs_diff_overall": round(overall/n, 4),
            "mean_abs_diff_bright_region": round(bright/nb, 4) if nb else None,
            "mean_abs_diff_halo_region": round(halo/nh, 4) if nh else None,
            "mean_abs_diff_flat_region": round(flat/nf, 4) if nf else None}


# ---- 3. produce exactly 4 variants ----
variants = {}
for vcfg in VARIANTS:
    g = ops(base, vcfg)
    variants[vcfg["id"]] = g
    save_png(g, vcfg["id"] + ".png")
    (OUT / (vcfg["id"] + ".json")).write_text(json.dumps({
        "id": vcfg["id"], "toggles": {k: vcfg[k] for k in ("exposure", "halo", "grain")},
        "description": vcfg["description"],
        "units": "raw 8-bit grayscale code value 0..255, clamp(0,255) on write",
        "dimensions": [W, H], "clipping": clipped_counts(g),
        "region_mean_raw": {"bright": round(region_mean(g, BR), 3),
                            "halo_ring": round(
                                sum(g[y][x] for y in range(H) for x in range(W)
                                    if in_rect(x, y, HR) and not in_rect(x, y, BR)) /
                                max(1, sum(1 for y in range(H) for x in range(W)
                                    if in_rect(x, y, HR) and not in_rect(x, y, BR))), 3),
                            "flat": round(region_mean(g, FR), 3)},
        "field": g,
    }, indent=1), encoding="utf-8")

# ---- 4. difference maps (each variant vs baseline) ----
base_g = variants["v0_baseline"]
diff_results = {}
for vid in [v["id"] for v in VARIANTS if v["id"] != "v0_baseline"]:
    g = variants[vid]
    dmap = [[abs(clamp(g[y][x]) - clamp(base_g[y][x])) for x in range(W)] for y in range(H)]
    im = Image.new("L", (W, H)); p = im.load()
    for y in range(H):
        for x in range(W):
            p[x, y] = 255 if dmap[y][x] > 255 else dmap[y][x]
    im.save(OUT / ("diff_%s.png" % vid))
    st = diff_stats(g, base_g)
    diff_results[vid] = {"diff_map": "diff_%s.png" % vid, "stats": st, "dims": [W, H]}
    (OUT / ("diff_%s.json" % vid)).write_text(json.dumps(diff_results[vid], indent=1), encoding="utf-8")

# ---- 5. checks ----
base_clip = clipped_counts(base_g)
exp_clip = clipped_counts(variants["v1_exposure"])
halo_mean_base = sum(base_g[y][x] for y in range(H) for x in range(W)
                     if in_rect(x,y,HR) and not in_rect(x,y,BR)) / max(1, sum(1 for y in range(H) for x in range(W) if in_rect(x,y,HR) and not in_rect(x,y,BR)))
halo_mean_v2 = sum(variants["v2_halo"][y][x] for y in range(H) for x in range(W)
                   if in_rect(x,y,HR) and not in_rect(x,y,BR)) / max(1, sum(1 for y in range(H) for x in range(W) if in_rect(x,y,HR) and not in_rect(x,y,BR)))
bright_mean_base = region_mean(base_g, BR)
bright_mean_v2 = region_mean(variants["v2_halo"], BR)
grain_flat_diff = diff_results["v3_grain"]["stats"]["mean_abs_diff_flat_region"]
grain_overall_diff = diff_results["v3_grain"]["stats"]["mean_abs_diff_overall"]

checks = {
    "C1_four_variants_unchanged_dims": {
        "n_variants": len(VARIANTS), "at_most_four": len(VARIANTS) <= 4,
        "dims_all": [list(Image.open(OUT / (v["id"] + ".png")).size) for v in VARIANTS],
        "pass": len(VARIANTS) <= 4 and all(Image.open(OUT / (v["id"] + ".png")).size == (W, H) for v in VARIANTS)},
    "C2_exposure_effect_and_clipping": {
        "gain": TG["exposure"]["gain"],
        "baseline_bright_mean": round(bright_mean_base, 3),
        "exposure_bright_mean": round(region_mean(variants["v1_exposure"], BR), 3),
        "baseline_clip_255": base_clip["at_255"], "exposure_clip_255": exp_clip["at_255"],
        "clipping_increased": exp_clip["at_255"] > base_clip["at_255"],
        "color_units": "raw 8-bit grayscale code value 0..255 (declared, NOT sRGB EOTF / NOT CIE L*)",
        "pass": region_mean(variants["v1_exposure"], BR) > bright_mean_base and exp_clip["at_255"] > base_clip["at_255"]},
    "C3_halo_localized_effect": {
        "halo_ring_mean_baseline": round(halo_mean_base, 3),
        "halo_ring_mean_v2": round(halo_mean_v2, 3),
        "halo_ring_increased": halo_mean_v2 > halo_mean_base,
        "bright_region_mean_baseline": round(bright_mean_base, 3),
        "bright_region_mean_v2": round(bright_mean_v2, 3),
        "bright_region_unchanged": abs(bright_mean_v2 - bright_mean_base) < 0.01,
        "halo_diff_map_mean": diff_results["v2_halo"]["stats"]["mean_abs_diff_halo_region"],
        "pass": halo_mean_v2 > halo_mean_base and abs(bright_mean_v2 - bright_mean_base) < 0.01},
    "C4_grain_high_frequency_effect": {
        "flat_region_mean_abs_diff": grain_flat_diff,
        "overall_mean_abs_diff": grain_overall_diff,
        "flat_diff_positive": grain_flat_diff > 0,
        "coordinate_deterministic": True, "rng_used": False,
        "pass": grain_flat_diff > 0},
    "C5_evidence_retained": {
        "input_field_json": True, "input_field_png": True,
        "variant_pngs": [v["id"] + ".png" for v in VARIANTS],
        "variant_jsons": [v["id"] + ".json" for v in VARIANTS],
        "diff_maps": [d["diff_map"] for d in diff_results.values()],
        "pass": True},
    "C6_deterministic_rerun": {"note": "filled by run_evidence.json after two identical runs", "pass": None},
    "C7_boundary_single_stack": {
        "pass": True,
        "label": "ONE self-authored operator stack (exposure->halo->grain) in declared order; two product pages NOT conflated; NO time-continuity / website-determinism / 4K / video-export / real-shader-pipeline claim"},
}
(OUT / "checks.json").write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding="utf-8")
(OUT / "run_config_snapshot.json").write_text(json.dumps({"config_sha256": hashlib.sha256((HERE/"config.json").read_bytes()).hexdigest()}, indent=2), encoding="utf-8")
print("kail_designs build OK ->", OUT)
print("variants:", len(VARIANTS), "| exposure clip255:", base_clip["at_255"], "->", exp_clip["at_255"])
print("halo ring mean:", round(halo_mean_base,2), "->", round(halo_mean_v2,2))
print("grain flat diff:", grain_flat_diff)
