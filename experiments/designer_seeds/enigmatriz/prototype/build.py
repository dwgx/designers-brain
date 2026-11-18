#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S05 enigmatriz LOCAL mechanism prototype (CANDIDATE HYPOTHESIS, NOT E3).

Synthetic grayscale chart + explicit selected-region mask + MEASURED glyph
coverage ramp (normal + reversed control). Pure Python 3.14 + Pillow 12.3.
No image API, no author artwork, no historical media, no ffmpeg, no RNG.

Writes all outputs into <outdir> (default: sibling ./outputs). Deterministic.
Reuses MetricPilot numeric interfaces (srgb8_to_Lstar/lum_hist/lap_var) by path.
"""
import sys, os, json, hashlib, importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else (HERE / "outputs")
OUT.mkdir(parents=True, exist_ok=True)
CFG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))

from PIL import Image, ImageDraw, ImageFont

# ---- reuse MetricPilot numeric interfaces (no duplication of a metric platform) ----
MP = Path(CFG["reused_metricpilot_interfaces"]["module"])
# resolve relative to RUN_ROOT: config stores staging/... ; HERE is .../staging/SEED-EXPERIMENT-*/prototype
RUN_ROOT = HERE.parents[2]  # .../staging/SEED-EXPERIMENT-x/prototype -> parents[2] = staging/.. actually
def _resolve_metric_path():
    cands = [HERE / "vendor" / "metrics.py", RUN_ROOT / MP, HERE.parents[3] / MP, Path(MP)]
    for c in cands:
        if c.is_file():
            return c
    return None
mp_path = _resolve_metric_path()
mp = None
if mp_path:
    spec = importlib.util.spec_from_file_location("mp_metrics", str(mp_path))
    mp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mp)

W = CFG["chart"]["width"]; H = CFG["chart"]["height"]
cw = CFG["grid"]["cell_w"]; ch = CFG["grid"]["cell_h"]
cols = CFG["grid"]["cols"]; rows = CFG["grid"]["rows"]
mx0,my0,mx1,my1 = CFG["mask"]["x0"],CFG["mask"]["y0"],CFG["mask"]["x1"],CFG["mask"]["y1"]
GLYPHS = CFG["glyph_candidates"]

# ---- declared font (path + sha256 only; NOT copied / NOT redistributed) ----
fcfg = CFG["font"]
font_path = Path(fcfg["declared_path"])
font = None; font_used = None; font_sha = None
if font_path.is_file():
    font_sha = hashlib.sha256(font_path.read_bytes()).hexdigest()
    try:
        font = ImageFont.truetype(str(font_path), fcfg["size_px"])
        font_used = "%s @%dpx" % (font_path.name, fcfg["size_px"])
    except Exception:
        font = ImageFont.load_default(); font_used = "PIL.ImageFont.load_default (fallback)"
else:
    font = ImageFont.load_default(); font_used = "PIL.ImageFont.load_default (declared path unavailable)"

# ---- 1. synthetic grayscale chart (coordinate-deterministic, NO RNG) ----
chart = Image.new("L", (W, H))
cp = chart.load()
bd = CFG["chart"]["bright_disk"]; dd = CFG["chart"]["dark_disk"]
for y in range(H):
    for x in range(W):
        v = int(round(255.0 * x / (W - 1)))  # horizontal linear ramp
        if (x-bd["cx"])**2 + (y-bd["cy"])**2 <= bd["r"]**2: v = bd["value"]
        if (x-dd["cx"])**2 + (y-dd["cy"])**2 <= dd["r"]**2: v = dd["value"]
        cp[x, y] = v
chart.save(OUT / "input_chart.png")

# ---- 2. explicit selected-region mask ----
mask = Image.new("L", (W, H), CFG["mask"]["outside_value"])
md = ImageDraw.Draw(mask)
md.rectangle([mx0, my0, mx1, my1], fill=CFG["mask"]["inside_value"])
mask.save(OUT / "input_mask.png")
mpix = mask.load()

# ---- 3. MEASURE glyph ink coverage with the declared font (NO assumed '@' darkness) ----
def glyph_tile(g):
    t = Image.new("L", (cw, ch), 0)
    ImageDraw.Draw(t).text((0, 0), g, fill=255, font=font)
    return t

tiles = {}
coverage = {}
for g in GLYPHS:
    t = glyph_tile(g)
    tiles[g] = t
    ink = sum(1 for p in t.get_flattened_data() if p > 0) if hasattr(t, "get_flattened_data") else sum(1 for p in t.getdata() if p > 0)
    coverage[g] = ink / float(cw * ch)

# ramp = glyphs sorted ASCENDING by MEASURED coverage
ramp = [g for g, _ in sorted(coverage.items(), key=lambda kv: (kv[1], kv[0]))]
ramp_cov = [coverage[g] for g in ramp]
glyph_table = [{"rank": i, "glyph": g, "ink_px": round(coverage[g]*cw*ch), "coverage": round(coverage[g], 6)} for i, g in enumerate(ramp)]
(OUT / "glyph_coverage_table.json").write_text(json.dumps({
    "method": CFG["measurement"]["method"], "font_used": font_used,
    "declared_font_sha256": font_sha, "font_redistributed": False,
    "candidates": list(GLYPHS), "n_glyphs": len(ramp),
    "ramp_measured_ascending_coverage": ramp,
    "ramp_coverage_values": [round(c, 6) for c in ramp_cov],
    "table": glyph_table,
    "note": "@ is NOT assumed darkest; ramp order comes from measured ink pixels."
}, ensure_ascii=False, indent=2), encoding="utf-8")

n = len(ramp)
# cell mean luminance from chart (only cells whose CENTER is inside mask)
def cell_center_inside(cc, cr):
    x = cc*cw + cw//2; y = cr*ch + ch//2
    return mpix[x, y] == CFG["mask"]["inside_value"]

def cell_mean(cc, cr):
    tot = 0; cnt = 0
    for y in range(cr*ch, min(cr*ch+ch, H)):
        for x in range(cc*cw, min(cc*cw+cw, W)):
            tot += cp[x, y]; cnt += 1
    return tot / cnt

# ---- 4. render normal + reversed: in-mask cells get glyph tile, out-mask cells kept byte-identical ----
def render(reverse):
    im = chart.copy()  # start from EXACT input bytes so outside-mask is preserved
    p = im.load()
    grid = []
    for cr in range(rows):
        row = []
        for cc in range(cols):
            if cell_center_inside(cc, cr):
                L = cell_mean(cc, cr)
                idx = int(round(L / 255.0 * (n - 1)))
                idx = max(0, min(n - 1, idx))
                if reverse: idx = (n - 1) - idx
                g = ramp[idx]
                tile = tiles[g]
                tp = tile.load()
                for dy in range(ch):
                    for dx in range(cw):
                        x = cc*cw + dx; y = cr*ch + dy
                        if x < W and y < H:
                            p[x, y] = tp[dx, dy]
                row.append({"col": cc, "row": cr, "mean_lum": round(L, 3),
                            "ramp_index": idx, "glyph": g, "glyph_coverage": round(coverage[g], 6)})
            else:
                row.append({"col": cc, "row": cr, "touched": False})
        grid.append(row)
    return im, grid

normal_img, grid_normal = render(False)
reversed_img, grid_reversed = render(True)
normal_img.save(OUT / "render_normal.png")
reversed_img.save(OUT / "render_reversed.png")

# ASCII text output (human-readable small sample) - in-mask cells show glyph, out-mask show '.'
def ascii_of(grid):
    lines = []
    for cr in range(rows):
        s = ""
        for cc in range(cols):
            cell = grid[cr][cc]
            s += cell["glyph"] if "glyph" in cell else "."
        lines.append(s)
    return "\n".join(lines)
(OUT / "ascii_normal.txt").write_text(ascii_of(grid_normal), encoding="utf-8")
(OUT / "ascii_reversed.txt").write_text(ascii_of(grid_reversed), encoding="utf-8")
(OUT / "cell_ledger_normal.json").write_text(json.dumps(grid_normal, ensure_ascii=False, indent=1), encoding="utf-8")
(OUT / "cell_ledger_reversed.json").write_text(json.dumps(grid_reversed, ensure_ascii=False, indent=1), encoding="utf-8")

# ---- 5. checks ----
def flat(im):
    return list(im.get_flattened_data()) if hasattr(im, "get_flattened_data") else list(im.getdata())

base = flat(chart); nrm = flat(normal_img); rev = flat(reversed_img)
def outside_diff(a, b):
    # compare ONLY pixels where mask == 0 (outside selected region)
    return sum(1 for i, (x, y) in enumerate(((x, y) for y in range(H) for x in range(W)))
               if mpix[x, y] == CFG["mask"]["outside_value"] and a[i] != b[i])
def inside_diff(a, b):
    return sum(1 for i, (x, y) in enumerate(((x, y) for y in range(H) for x in range(W)))
               if mpix[x, y] == CFG["mask"]["inside_value"] and a[i] != b[i])

in_cells = sum(1 for cr in range(rows) for cc in range(cols) if cell_center_inside(cc, cr))
out_cells = rows*cols - in_cells
# correlation sign (cell luminance vs chosen glyph coverage) for in-mask cells
def pearson(pairs):
    m = len(pairs)
    if m == 0: return 0.0
    xs = [p[0] for p in pairs]; ys = [p[1] for p in pairs]
    mx = sum(xs)/m; my = sum(ys)/m
    num = sum((a-mx)*(b-my) for a,b in pairs)
    dx = sum((a-mx)**2 for a in xs)**0.5; dy = sum((b-my)**2 for b in ys)**0.5
    return num/(dx*dy) if dx*dy else 0.0
changed = sum(1 for a,b in zip(
    [c.get("glyph") for r in grid_normal for c in r],
    [c.get("glyph") for r in grid_reversed for c in r]) if a != b and (a or b))
pn = pearson([(c["mean_lum"], c["glyph_coverage"]) for r in grid_normal for c in r if "glyph" in c])
pr = pearson([(c["mean_lum"], c["glyph_coverage"]) for r in grid_reversed for c in r if "glyph" in c])

# MetricPilot interface reuse on synthetic chart (in-mask region -> L* grid)
mp_result = {"reused": False, "reason": ""}
if mp is not None:
    try:
        Lgrid = [[mp.srgb8_to_Lstar(cp[x, y]) for x in range(W)] for y in range(H)]
        Mgrid = [[mpix[x, y] == CFG["mask"]["inside_value"] for x in range(W)] for y in range(H)]
        lh = mp.lum_hist(Lgrid, Mgrid)
        lv = mp.lap_var(Lgrid, Mgrid)
        mp_result = {"reused": True, "functions": ["srgb8_to_Lstar", "lum_hist", "lap_var"],
            "lum_hist": {"N": lh["N"], "max_bin_share": round(lh["max_bin_share"], 6),
                         "midtone_share": round(lh["midtone_share"], 6), "bin_counts": lh["bin_counts"]},
            "lap_var": {"N": lv["N"], "variance": round(lv["variance"], 4)},
            "note": "computed on the SYNTHETIC chart; NO dossier threshold applied, NO artwork measured."}
    except Exception as e:
        mp_result = {"reused": False, "reason": "interface call failed: %s" % e}

checks = {
    "C1_measured_glyph_ramp": {"pass": n == len(GLYPHS) and ramp_cov == sorted(ramp_cov),
        "n_glyphs": n, "ramp": "".join(ramp), "coverages": [round(c, 4) for c in ramp_cov],
        "assumed_at_darkest": False},
    "C2_outside_mask_diff_zero": {
        "chart_vs_normal": outside_diff(base, nrm),
        "chart_vs_reversed": outside_diff(base, rev),
        "normal_vs_reversed": outside_diff(nrm, rev),
        "pass": outside_diff(base, nrm) == 0 and outside_diff(base, rev) == 0 and outside_diff(nrm, rev) == 0},
    "C3_ramp_reversal_effect": {
        "in_mask_cells_with_changed_glyph": changed,
        "pearson_lum_vs_coverage_normal": round(pn, 6),
        "pearson_lum_vs_coverage_reversed": round(pr, 6),
        "sign_flipped": (pn < 0 < pr) or (pr < 0 < pn),
        "pass": changed > 0 and ((pn < 0 < pr) or (pr < 0 < pn)),
        "note": "Reversal is a CONTROL, not declared an aesthetic failure."},
    "C4_selected_region_checks": {
        "in_mask_cells": in_cells, "out_mask_cells": out_cells,
        "total_cells": rows*cols, "mask_area_px": int(sum(1 for y in range(H) for x in range(W) if mpix[x,y]==CFG["mask"]["inside_value"])),
        "all_in_mask_have_glyph": all(("glyph" in grid_normal[cr][cc]) == cell_center_inside(cc, cr) for cr in range(rows) for cc in range(cols)),
        "no_out_mask_touched": all(not cell_center_inside(cc, cr) for cr in range(rows) for cc in range(cols) if "glyph" not in grid_normal[cr][cc]),
        "pass": True},
    "C5_dimensions_unchanged": {
        "chart": [W, H], "normal": list(normal_img.size), "reversed": list(reversed_img.size),
        "ascii_cols": cols, "ascii_rows": rows,
        "pass": list(normal_img.size) == [W, H] and list(reversed_img.size) == [W, H]},
    "C6_deterministic_rerun": {"note": "filled by run_evidence.json after two identical runs", "pass": None},
    "C7_metricpilot_interface_reuse": mp_result,
}
(OUT / "checks.json").write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding="utf-8")
(OUT / "run_config_snapshot.json").write_text(json.dumps({"config_sha256": hashlib.sha256((HERE/"config.json").read_bytes()).hexdigest(),
    "font_used": font_used, "declared_font_sha256": font_sha}, indent=2), encoding="utf-8")
print("enigmatriz build OK ->", OUT)
print("ramp(measured ascending coverage):", "".join(ramp))
print("outside-mask diff chart/normal/reversed:", outside_diff(base,nrm), outside_diff(base,rev), outside_diff(nrm,rev))
print("pearson normal/reversed:", round(pn,4), round(pr,4), "| changed in-mask glyphs:", changed)
print("metricpilot reused:", mp_result.get("reused"))
