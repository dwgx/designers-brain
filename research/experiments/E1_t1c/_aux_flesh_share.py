#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E1_t1c · 辅助探针：肤色像素占比启发式（三版对照）。

目的：尝试用「暖肤色像素占比」机械辅助判定「人体母题是否出现」。
结论（负向）：**不可分**——本风格的土黄/赭石调色板与肉色区间重叠，
E1 / E1b / E1c 三版数值同量级（A 变体 ≈0.38–0.53），不足以机械判定；
判定以逐格目检（含 2×2 放大细看 `_inspect/`）为准。本脚本仅存档该负向结果。

用法: python _aux_flesh_share.py
"""
import numpy as np
from PIL import Image

SETS = {
    "E1  (§8.1 偏置版)": ["../E1_t1/cells/e1_michelangelo/img_%02d.jpg" % i for i in (1, 2, 3)],
    "E1b (§8.1b v1)":    ["../E1_t1b/cells/e1_michelangelo/img_%02d.jpg" % i for i in (1, 2, 3)],
    "E1c (§8.1b v2)":    ["cells/e1_michelangelo_v2/img_%02d.jpg" % i for i in (1, 2, 3)],
}


def hsv(path):
    a = np.asarray(Image.open(path).convert("RGB")).astype(np.float32) / 255.0
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx = a.max(-1); mn = a.min(-1)
    v = mx; delta = np.maximum(mx - mn, 1e-9)
    s = np.where(mx > 1e-6, (mx - mn) / np.maximum(mx, 1e-6), 0)
    h = np.zeros_like(mx)
    mr = (mx == r); mg = (mx == g) & ~mr; mb = ~mr & ~mg
    h[mr] = 60 * np.mod((g - b)[mr] / delta[mr], 6)
    h[mg] = 60 * ((b - r)[mg] / delta[mg] + 2)
    h[mb] = 60 * ((r - g)[mb] / delta[mb] + 4)
    return h, s, v


def share(path):
    h, s, v = hsv(path)
    A = ((h >= 5) & (h <= 50) & (s >= 0.15) & (v >= 0.25)).mean()          # 宽松暖肤色
    B = ((h >= 10) & (h <= 45) & (s >= 0.20) & (s <= 0.75) & (v >= 0.35)).mean()  # 较严肉色
    return A, B


def main():
    print("肤色占比启发式（不可分，负向结果存档）")
    for name, paths in SETS.items():
        vals = [share(p) for p in paths]
        print("  %-16s A: %.3f %.3f %.3f | B: %.3f %.3f %.3f" %
              (name, *[v[0] for v in vals], *[v[1] for v in vals]))


if __name__ == "__main__":
    main()
