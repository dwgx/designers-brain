#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E1_t1c · contact sheets 拼接（§8.1b v2 重跑）：
  sheet_e1_michelangelo_v2.png —— 3 张横排一行（单图高 720，顶部标签条）
  compare_michelangelo_v2.png  —— 三版对照：3 行 × 3 列
      （上：E1 偏置版 §8.1（E1_t1）；中：E1b 部分解除 §8.1b v1（E1_t1b）；
        下：E1c v2 §8.1b v2（E1_t1c））
缺失的图用占位框标 MISSING（不阻塞出表）。
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
CELLS_DIR = os.environ.get("E1C_CELLS_DIR") or os.path.join(HERE, "cells")
OUT_DIR = os.environ.get("E1C_OUT_DIR") or HERE
E1_T1_DIR = os.environ.get("E1_T1_DIR") or os.path.normpath(os.path.join(HERE, "..", "E1_t1"))
E1_T1B_DIR = os.environ.get("E1_T1B_DIR") or os.path.normpath(os.path.join(HERE, "..", "E1_t1b"))

FONT_PATH = "C:/Windows/Fonts/msyh.ttc"
FONT_BOLD = "C:/Windows/Fonts/msyhbd.ttc"

CELL_H = 720
CELL_GAP = 12
CELL_MARGIN = 16
LABEL_H = 46

CMP_H = 540
CMP_GAP = 10
CMP_MARGIN = 16
CMP_GUTTER = 320
CMP_HEADER = 84
CMP_LABEL_H = 34

BG = (24, 24, 28)
FG = (238, 238, 240)
FG_DIM = (168, 168, 176)
MISSING_BG = (60, 32, 32)

CELL_ID = "e1_michelangelo_v2"

COMPARE_ROWS = [
    ("E1 偏置版（§8.1，E1_t1）\n题材被替换：裸体肌肉人物环绕",
     os.path.join(E1_T1_DIR, "cells", "e1_michelangelo")),
    ("E1b v1 版（§8.1b v1，E1_t1b）\n部分解除：灯塔回中心，肌体仍环绕",
     os.path.join(E1_T1B_DIR, "cells", "e1_michelangelo")),
    ("E1c v2 版（§8.1b v2，E1_t1c）\n本轮：从句级改写后重跑",
     os.path.join(CELLS_DIR, CELL_ID)),
]


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


def make_cell_sheet():
    imgs = []
    for i in (1, 2, 3):
        p = os.path.join(CELLS_DIR, CELL_ID, "img_%02d.jpg" % i)
        imgs.append(load_img(p, CELL_H) if os.path.exists(p) else None)
    widths = [im.width if im else round(768 * CELL_H / 1152) for im in imgs]
    w = CELL_MARGIN * 2 + sum(widths) + CELL_GAP * (len(imgs) - 1)
    h = CELL_MARGIN * 2 + LABEL_H + CELL_H
    canvas = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(canvas)
    label = "%s · 米开朗基罗（§8.1b v2 版）" % CELL_ID
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
    out = os.path.join(OUT_DIR, "sheet_%s.png" % CELL_ID)
    canvas.save(out)
    return out, canvas.size


def make_compare_sheet():
    tw = round(768 * CMP_H / 1152)
    w = CMP_MARGIN * 2 + CMP_GUTTER + tw * 3 + CMP_GAP * 2
    h = CMP_MARGIN * 2 + CMP_HEADER + CMP_LABEL_H + (CMP_H + CMP_GAP) * len(COMPARE_ROWS)
    canvas = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(canvas)
    d.text((CMP_MARGIN, CMP_MARGIN + 6), "三版对照 · e1_michelangelo · 米开朗基罗 · T1「暴风雨中的海边灯塔」",
           font=font(28, bold=True), fill=FG)
    d.text((CMP_MARGIN, CMP_MARGIN + 46),
           "上：E1 偏置版（§8.1）／中：E1b 部分解除（§8.1b v1）／下：E1c v2（§8.1b v2，本轮）",
           font=font(20), fill=FG_DIM)
    y = CMP_MARGIN + CMP_HEADER + CMP_LABEL_H
    for label, folder in COMPARE_ROWS:
        lines = label.split("\n")
        d.text((CMP_MARGIN + 4, y + CMP_H // 2 - 34), lines[0], font=font(20, bold=True), fill=FG)
        if len(lines) > 1:
            d.text((CMP_MARGIN + 4, y + CMP_H // 2 + 2), lines[1], font=font(18), fill=FG_DIM)
        x = CMP_MARGIN + CMP_GUTTER
        for i in (1, 2, 3):
            paste_or_missing(canvas, d, x, y, tw, CMP_H,
                             os.path.join(folder, "img_%02d.jpg" % i))
            x += tw + CMP_GAP
        y += CMP_H + CMP_GAP
    out = os.path.join(OUT_DIR, "compare_michelangelo_v2.png")
    canvas.save(out)
    return out, canvas.size


def main():
    out, size = make_cell_sheet()
    print("wrote %s %sx%s" % (os.path.basename(out), size[0], size[1]))
    out, size = make_compare_sheet()
    print("wrote %s %sx%s" % (os.path.basename(out), size[0], size[1]))


if __name__ == "__main__":
    main()
