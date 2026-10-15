#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""walkthrough_01 · 候选对比页拼接（3 方向横排一行，顶部标题 + 每图标签条）
产物: candidates/compare_candidates.png
缺失的图用占位框标 MISSING（不阻塞出表）。
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "candidates", "compare_candidates.png")

FONT_PATH = "C:/Windows/Fonts/msyh.ttc"
FONT_BOLD = "C:/Windows/Fonts/msyhbd.ttc"

IMG_H = 960
GAP = 14
MARGIN = 20
LABEL_H = 44
HEADER_H = 86
BG = (24, 24, 28)
FG = (238, 238, 240)
FG_DIM = (168, 168, 176)
MISSING_BG = (60, 32, 32)

ITEMS = [
    ("cand1_monet_dawn.jpg", "① 晨光 · 莫奈（单模块）", "晨光/空气感——湿润反光与蒸汽"),
    ("cand2_vermeer_monet_windowlight.jpg", "② 窗光 · 维米尔 70% × 莫奈 30%", "窗光静物——倒奶一刻，点状高光"),
    ("cand3_matisse_colorblocks.jpg", "③ 色块 · 马蒂斯（单模块）", "剪纸色块——图形感最强"),
]


def font(size, bold=False):
    try:
        return ImageFont.truetype(FONT_BOLD if bold else FONT_PATH, size)
    except Exception:
        return ImageFont.load_default(size=size)


def load_img(path, target_h):
    im = Image.open(path).convert("RGB")
    w = round(im.width * target_h / im.height)
    return im.resize((w, target_h), Image.LANCZOS)


def main():
    imgs = []
    for fn, _t, _s in ITEMS:
        p = os.path.join(HERE, "candidates", fn)
        imgs.append(load_img(p, IMG_H) if os.path.exists(p) else None)
    widths = [im.width if im else round(768 * IMG_H / 1152) for im in imgs]
    w = MARGIN * 2 + sum(widths) + GAP * (len(imgs) - 1)
    h = MARGIN * 2 + HEADER_H + LABEL_H + IMG_H
    canvas = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(canvas)
    d.text((MARGIN, MARGIN + 4), "拾光 · 开业主视觉——候选对比页（walkthrough_01）",
           font=font(30, bold=True), fill=FG)
    d.text((MARGIN, MARGIN + 48), "通道：grok-imagine-image-2.0（裸模型名）· 请求 1024x1536 / 实回 768x1152 · 负向段未发送（留档）",
           font=font(17), fill=FG_DIM)
    x = MARGIN
    y = MARGIN + HEADER_H
    for (fn, title, sub), im, wd in zip(ITEMS, imgs, widths):
        d.text((x, y), title, font=font(21, bold=True), fill=FG)
        d.text((x, y + 24), sub, font=font(15), fill=FG_DIM)
        if im:
            canvas.paste(im, (x, y + LABEL_H))
        else:
            d.rectangle([x, y + LABEL_H, x + wd, y + LABEL_H + IMG_H], fill=MISSING_BG, outline=(200, 80, 80))
            d.text((x + 12, y + LABEL_H + 12), "MISSING " + fn, font=font(22), fill=(255, 160, 160))
        x += wd + GAP
    canvas.save(OUT)
    print("saved:", OUT, canvas.size)


if __name__ == "__main__":
    main()
