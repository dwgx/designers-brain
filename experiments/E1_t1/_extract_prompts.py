#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E1_t1 · 从 11 张模块卡抽取 §8.1 英文正向/负向段，合成 12 格 prompt，写 prompts.json。

配方（E-01 锁定，全文见 RESULTS.md）：
  prompt = THEME + " " + §8.1 正向段（逐行解包为单行，内容逐字不变）
  负向段：不随请求发送（grok-imagine 通道无负向参数）——记录在 prompts.json / RESULTS.md 备查。

校验依据：模块卡经 `python _extract.py --check` 逐字比对（checks=33 ok=33 fail=0）。
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "knowledge", "domains", "painters", "modules"))

THEME = ("A lighthouse on a rocky coast in a storm, towering waves crashing against "
         "the rocks, dark storm clouds overhead.")

MODULES = [
    ("da_vinci", "达·芬奇"),
    ("michelangelo", "米开朗基罗"),
    ("van_gogh", "梵高"),
    ("monet", "莫奈"),
    ("picasso", "毕加索"),
    ("cezanne", "塞尚"),
    ("matisse", "马蒂斯"),
    ("hokusai", "葛饰北斋"),
    ("caravaggio", "卡拉瓦乔"),
    ("vermeer", "维米尔"),
    ("durer", "丢勒"),
]


def extract_block(md_text, marker_regex):
    """取 marker 行之后第一个 ``` 围栏块，逐行解包为单行（内容不变）。"""
    lines = md_text.splitlines()
    idx = None
    for i, ln in enumerate(lines):
        if re.search(marker_regex, ln):
            idx = i
            break
    if idx is None:
        raise ValueError("marker not found: %s" % marker_regex)
    j = idx + 1
    while j < len(lines) and not lines[j].strip().startswith("```"):
        j += 1
    if j >= len(lines):
        raise ValueError("no opening fence after marker: %s" % marker_regex)
    k = j + 1
    block = []
    while k < len(lines) and not lines[k].strip().startswith("```"):
        block.append(lines[k].rstrip())
        k += 1
    if k >= len(lines):
        raise ValueError("no closing fence: %s" % marker_regex)
    return " ".join(" ".join(block).split())


def main():
    cells = []
    cells.append({
        "cell": "e0_baseline",
        "module": None,
        "module_name": "基线（无风格段）",
        "prompt": THEME,
    })
    for mid, mname in MODULES:
        path = os.path.join(MODULES_DIR, mid + ".md")
        with open(path, encoding="utf-8") as fh:
            md = fh.read()
        positive = extract_block(md, r"\*\*正向段")
        negative = extract_block(md, r"\*\*负向约束")
        prompt = THEME + " " + positive
        cells.append({
            "cell": "e1_" + mid,
            "module": mid,
            "module_name": mname,
            "positive": positive,
            "negative": negative,
            "prompt": prompt,
        })

    doc = {
        "experiment": "E-01 · E0+E1 首批图像实验 · 主题 T1（暴风雨中的海边灯塔）",
        "date": "2026-10-15",
        "model": "grok-imagine-image-2.0",
        "endpoint": "/v1/images/generations",
        "size_requested": "1024x1536",
        "theme": THEME,
        "recipe": ("prompt = THEME + ' ' + 模块 §8.1 正向段（逐行解包为单行）；"
                   "负向段未随请求发送（通道无负向参数），仅记录备查。"),
        "cells": cells,
    }
    out = os.path.join(HERE, "prompts.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)

    print("wrote", out)
    for c in cells:
        print("---", c["cell"], "| prompt chars:", len(c["prompt"]))
        print("   ", c["prompt"][:110], "...")
        if c.get("negative"):
            print("    [negative chars:", len(c["negative"]), "]")


if __name__ == "__main__":
    main()
