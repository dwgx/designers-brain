#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E1_t1 · contact sheets 拼接：
  sheet_<cell>.png —— 每格 3 张横排一行（单图高 720，顶部标签条）
  sheet_all.png   —— 12 行 × 3 列总表（缩略高 260，左侧标签槽）
缺失的图用占位框标 MISSING（不阻塞出表）。
"""
import json
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
CELLS_DIR = os.environ.get("E1_CELLS_DIR") or os.path.join(HERE, "cells")
OUT_DIR = os.environ.get("E1_OUT_DIR") or HERE

FONT_PATH = "C:/Windows/Fonts/msyh.ttc"
FONT_BOLD = "C:/Windows/Fonts/msyhbd.ttc"

CELL_H = 720
CELL_GAP = 12
CELL_MARGIN = 16
LABEL_H = 46

ALL_H = 260
ALL_GAP = 8
ALL_MARGIN = 14
GUTTER = 208
HEADER_H = 56

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
    label = "%s · %s" % (cell, module_name)
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
    w = ALL_MARGIN * 2 + GUTTER + thumb_w * 3 + ALL_GAP * 2
    h = ALL_MARGIN * 2 + HEADER_H + ALL_H * len(cells) + ALL_GAP * (len(cells) - 1)
    canvas = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(canvas)
    d.text((ALL_MARGIN, ALL_MARGIN + 4), "E-01 · E0+E1 首批图像实验 · T1「暴风雨中的海边灯塔」",
           font=font(26, bold=True), fill=FG)
    d.text((ALL_MARGIN, ALL_MARGIN + 36), "12 格 × 3 张 · grok-imagine-image-2.0 · 直连网关 · 2026-10-15",
           font=font(21), fill=FG_DIM)
    y = ALL_MARGIN + HEADER_H
    for c in cells:
        cell = c["cell"]
        d.text((ALL_MARGIN + 4, y + ALL_H // 2 - 34), cell, font=font(24, bold=True), fill=FG)
        d.text((ALL_MARGIN + 4, y + ALL_H // 2 + 6), c.get("module_name") or "", font=font(22), fill=FG_DIM)
        x = ALL_MARGIN + GUTTER
        for i in (1, 2, 3):
            p = os.path.join(CELLS_DIR, cell, "img_%02d.jpg" % i)
            if os.path.exists(p):
                canvas.paste(load_img(p, ALL_H), (x, y))
            else:
                d.rectangle([x, y, x + thumb_w, y + ALL_H], fill=MISSING_BG, outline=(200, 80, 80))
                d.text((x + 8, y + 8), "MISSING", font=font(18), fill=(255, 160, 160))
            x += thumb_w + ALL_GAP
        y += ALL_H + ALL_GAP
    out = os.path.join(OUT_DIR, "sheet_all.png")
    canvas.save(out)
    return out, canvas.size


def main():
    with open(os.path.join(HERE, "prompts.json"), encoding="utf-8") as fh:
        cells = json.load(fh)["cells"]
    for c in cells:
        out, size = make_cell_sheet(c["cell"], c.get("module_name") or "")
        print("wrote %s %sx%s" % (os.path.basename(out), size[0], size[1]))
    out, size = make_all_sheet(cells)
    print("wrote %s %sx%s" % (os.path.basename(out), size[0], size[1]))


if __name__ == "__main__":
    main()
