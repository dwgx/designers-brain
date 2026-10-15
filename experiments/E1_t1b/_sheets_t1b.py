#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E1_t1b · contact sheets 拼接（§8.1b 重跑）：
  sheet_<cell>.png     —— 每格 3 张横排一行（§8.1b 纯风格版；单图高 720，顶部标签条）
  sheet_all_t1b.png    —— E0 对照（复用）+ 7 行 × 3 列总表（缩略高 260，左侧标签槽）
  compare_<cell>.png   —— 同格对照：3 行 × 3 列（E0 对照 / §8.1 偏置版 / §8.1b 纯风格版）
  compare_all_t1b.png  —— 7 格对照总表（每格 3 行；缩略高 200）
缺失的图用占位框标 MISSING（不阻塞出表）。
"""
import json
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
CELLS_DIR = os.environ.get("E1B_CELLS_DIR") or os.path.join(HERE, "cells")
OUT_DIR = os.environ.get("E1B_OUT_DIR") or HERE
E1_T1_DIR = os.environ.get("E1_T1_DIR") or os.path.normpath(os.path.join(HERE, "..", "E1_t1"))

FONT_PATH = "C:/Windows/Fonts/msyh.ttc"
FONT_BOLD = "C:/Windows/Fonts/msyhbd.ttc"

CELL_H = 720
CELL_GAP = 12
CELL_MARGIN = 16
LABEL_H = 46

ALL_H = 260
ALL_GAP = 8
ALL_MARGIN = 14
GUTTER = 216
HEADER_H = 56

CMP_H = 540
CMP_GAP = 10
CMP_MARGIN = 16
CMP_GUTTER = 250
CMP_HEADER = 84
CMP_LABEL_H = 34

CMPALL_H = 190
CMPALL_GAP = 8
CMPALL_MARGIN = 14
CMPALL_GUTTER = 250
CMPALL_HEADER = 60
CMPALL_GROUP_H = 38

BG = (24, 24, 28)
FG = (238, 238, 240)
FG_DIM = (168, 168, 176)
MISSING_BG = (60, 32, 32)


def font(size, bold=False):
    path = FONT_BOLD if bold else FONT_PATH
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default(size=size)


def load_img(path, target_h):
    im = Image.open(path).convert("RGB")
    w = round(im.width * target_h / im.height)
    return im.resize((w, target_h), Image.LANCZOS)


def paste_or_missing(canvas, d, x, y, w, h, path):
    if os.path.exists(path):
        canvas.paste(load_img(path, h), (x, y))
    else:
        d.rectangle([x, y, x + w, y + h], fill=MISSING_BG, outline=(200, 80, 80))
        d.text((x + 8, y + 8), "MISSING", font=font(18), fill=(255, 160, 160))


def make_cell_sheet(cell, module_name):
    imgs = []
    for i in (1, 2, 3):
        p = os.path.join(CELLS_DIR, cell, "img_%02d.jpg" % i)
        imgs.append(load_img(p, CELL_H) if os.path.exists(p) else None)
    widths = [im.width if im else round(768 * CELL_H / 1152) for im in imgs]
    w = CELL_MARGIN * 2 + sum(widths) + CELL_GAP * (len(imgs) - 1)
    h = CELL_MARGIN * 2 + LABEL_H + CELL_H
    canvas = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(canvas)
    label = "%s · %s（§8.1b 纯风格版）" % (cell, module_name)
    d.text((CELL_MARGIN, CELL_MARGIN + 8), label, font=font(30, bold=True), fill=FG)
    x = CELL_MARGIN
    y = CELL_MARGIN + LABEL_H
    for i, im in enumerate(imgs, 1):
        if im:
            canvas.paste(im, (x, y))
        else:
            d.rectangle([x, y, x + widths[i - 1], y + CELL_H], fill=MISSING_BG, outline=(200, 80, 80))
            d.text((x + 12, y + 12), "MISSING img_%02d" % i, font=font(24), fill=(255, 160, 160))
        x += widths[i - 1] + CELL_GAP
    out = os.path.join(OUT_DIR, "sheet_%s.png" % cell)
    canvas.save(out)
    return out, canvas.size


def make_all_sheet(cells):
    thumb_w = round(768 * ALL_H / 1152)
    rows = [("e0_baseline", "基线对照（E1_t1 复用）", os.path.join(E1_T1_DIR, "cells", "e0_baseline"))]
    for c in cells:
        rows.append((c["cell"], (c.get("module_name") or "") + "（§8.1b）",
                     os.path.join(CELLS_DIR, c["cell"])))
    w = ALL_MARGIN * 2 + GUTTER + thumb_w * 3 + ALL_GAP * 2
    h = ALL_MARGIN * 2 + HEADER_H + ALL_H * len(rows) + ALL_GAP * (len(rows) - 1)
    canvas = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(canvas)
    d.text((ALL_MARGIN, ALL_MARGIN + 4), "E-02 · E1_t1b · §8.1b 纯风格段重跑 · T1「暴风雨中的海边灯塔」",
           font=font(25, bold=True), fill=FG)
    d.text((ALL_MARGIN, ALL_MARGIN + 36),
           "7 格 × 3 张（§8.1b）+ E0 对照（复用 E1_t1）· grok-imagine-image-2.0 · 2026-10-15",
           font=font(18), fill=FG_DIM)
    y = ALL_MARGIN + HEADER_H
    for cell, sub, folder in rows:
        d.text((ALL_MARGIN + 4, y + ALL_H // 2 - 34), cell, font=font(24, bold=True), fill=FG)
        d.text((ALL_MARGIN + 4, y + ALL_H // 2 + 6), sub, font=font(21), fill=FG_DIM)
        x = ALL_MARGIN + GUTTER
        for i in (1, 2, 3):
            paste_or_missing(canvas, d, x, y, thumb_w, ALL_H,
                             os.path.join(folder, "img_%02d.jpg" % i))
            x += thumb_w + ALL_GAP
        y += ALL_H + ALL_GAP
    out = os.path.join(OUT_DIR, "sheet_all_t1b.png")
    canvas.save(out)
    return out, canvas.size


def _row(canvas, d, x0, y, h, label, folder):
    d.text((x0 + 4, y + h // 2 - 26), label, font=font(21, bold=True), fill=FG)
    x = x0 + CMP_GUTTER
    tw = round(768 * h / 1152)
    for i in (1, 2, 3):
        paste_or_missing(canvas, d, x, y, tw, h, os.path.join(folder, "img_%02d.jpg" % i))
        x += tw + CMP_GAP
    return y + h + CMP_GAP


def make_compare_sheet(cell, module_name):
    rows = [
        ("E0 对照（E1_t1 复用）", os.path.join(E1_T1_DIR, "cells", "e0_baseline")),
        ("§8.1 偏置版（E1_t1）", os.path.join(E1_T1_DIR, "cells", cell)),
        ("§8.1b 纯风格版（E1_t1b）", os.path.join(CELLS_DIR, cell)),
    ]
    tw = round(768 * CMP_H / 1152)
    w = CMP_MARGIN * 2 + CMP_GUTTER + tw * 3 + CMP_GAP * 2
    h = CMP_MARGIN * 2 + CMP_HEADER + CMP_LABEL_H + (CMP_H + CMP_GAP) * len(rows)
    canvas = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(canvas)
    d.text((CMP_MARGIN, CMP_MARGIN + 6), "同格对照 · %s · %s" % (cell, module_name),
           font=font(28, bold=True), fill=FG)
    d.text((CMP_MARGIN, CMP_MARGIN + 46),
           "上：E0 对照（复用）／中：§8.1 偏置版（E1_t1）／下：§8.1b 纯风格版（E1_t1b）",
           font=font(20), fill=FG_DIM)
    y = CMP_MARGIN + CMP_HEADER + CMP_LABEL_H
    for label, folder in rows:
        y = _row(canvas, d, CMP_MARGIN, y, CMP_H, label, folder)
    out = os.path.join(OUT_DIR, "compare_%s.png" % cell)
    canvas.save(out)
    return out, canvas.size


def make_compare_all(cells):
    tw = round(768 * CMPALL_H / 1152)
    w = CMPALL_MARGIN * 2 + CMPALL_GUTTER + tw * 3 + CMPALL_GAP * 2
    group_h = CMPALL_GROUP_H + (CMPALL_H + CMPALL_GAP) * 3
    h = CMPALL_MARGIN * 2 + CMPALL_HEADER + group_h * len(cells) + CMPALL_GAP * (len(cells) - 1)
    canvas = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(canvas)
    d.text((CMPALL_MARGIN, CMPALL_MARGIN + 4), "E-02 · E1_t1b · 同格对照总表（§8.1 偏置版 vs §8.1b 纯风格版）",
           font=font(21, bold=True), fill=FG)
    d.text((CMPALL_MARGIN, CMPALL_MARGIN + 36),
           "每格 3 行：E0 对照 / §8.1 偏置版 / §8.1b 纯风格版 · 2026-10-15",
           font=font(18), fill=FG_DIM)
    y = CMPALL_MARGIN + CMPALL_HEADER
    for c in cells:
        cell = c["cell"]
        d.text((CMPALL_MARGIN + 4, y + 8), "%s · %s" % (cell, c.get("module_name") or ""),
               font=font(21, bold=True), fill=(255, 220, 150))
        y += CMPALL_GROUP_H
        for label, folder in (
                ("E0 对照", os.path.join(E1_T1_DIR, "cells", "e0_baseline")),
                ("§8.1 偏置版", os.path.join(E1_T1_DIR, "cells", cell)),
                ("§8.1b 纯风格版", os.path.join(CELLS_DIR, cell))):
            d.text((CMPALL_MARGIN + 4, y + CMPALL_H // 2 - 22), label, font=font(18, bold=True), fill=FG)
            x = CMPALL_MARGIN + CMPALL_GUTTER
            for i in (1, 2, 3):
                paste_or_missing(canvas, d, x, y, tw, CMPALL_H,
                                 os.path.join(folder, "img_%02d.jpg" % i))
                x += tw + CMPALL_GAP
            y += CMPALL_H + CMPALL_GAP
        y += CMPALL_GAP
    out = os.path.join(OUT_DIR, "compare_all_t1b.png")
    canvas.save(out)
    return out, canvas.size


def main():
    with open(os.path.join(HERE, "prompts_t1b.json"), encoding="utf-8") as fh:
        cells = json.load(fh)["cells"]
    for c in cells:
        out, size = make_cell_sheet(c["cell"], c.get("module_name") or "")
        print("wrote %s %sx%s" % (os.path.basename(out), size[0], size[1]))
    out, size = make_all_sheet(cells)
    print("wrote %s %sx%s" % (os.path.basename(out), size[0], size[1]))
    for c in cells:
        out, size = make_compare_sheet(c["cell"], c.get("module_name") or "")
        print("wrote %s %sx%s" % (os.path.basename(out), size[0], size[1]))
    out, size = make_compare_all(cells)
    print("wrote %s %sx%s" % (os.path.basename(out), size[0], size[1]))


if __name__ == "__main__":
    main()
