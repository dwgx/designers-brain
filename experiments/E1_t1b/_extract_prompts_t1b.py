#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E1_t1b · 从模块卡抽取 §8.1b 纯风格正向段，合成 7 格 prompt，写 prompts_t1b.json。

配方（E-02 锁定）：
  prompt = THEME + " " + §8.1b 正向段（逐行解包为单行，内容逐字不变）
  §8.1b 来源：knowledge/domains/painters/modules/<id>.md（E-02 派生，7 卡；§8.1 原样保留）
  E0 对照：复用 E1_t1/cells/e0_baseline（不重跑）。

校验：7 卡均含「## §8.1b 纯风格段（场景可迁移）」且围栏块可解包。
"""
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "knowledge", "domains", "painters", "modules"))

THEME = ("A lighthouse on a rocky coast in a storm, towering waves crashing against "
         "the rocks, dark storm clouds overhead.")

MODULES = [
    ("da_vinci", "达·芬奇"),
    ("michelangelo", "米开朗基罗"),
    ("picasso", "毕加索"),
    ("cezanne", "塞尚"),
    ("caravaggio", "卡拉瓦乔"),
    ("vermeer", "维米尔"),
    ("durer", "丢勒"),
]


def extract_s81b(md_text):
    """取「## §8.1b 纯风格段（场景可迁移）」后第一个 ``` 围栏块，逐行解包为单行。"""
    marker = "## §8.1b 纯风格段（场景可迁移）"
    idx = md_text.find(marker)
    if idx < 0:
        raise ValueError("§8.1b marker not found")
    j = md_text.find("```", idx)
    k = md_text.find("```", j + 3)
    if j < 0 or k < 0:
        raise ValueError("§8.1b fence not found")
    block = md_text[j + 3:k]
    return " ".join(block.split())


def main():
    cells = []
    for mid, mname in MODULES:
        with open(os.path.join(MODULES_DIR, mid + ".md"), encoding="utf-8") as fh:
            md = fh.read()
        s81b = extract_s81b(md)
        prompt = THEME + " " + s81b
        cells.append({
            "cell": "e1_" + mid,
            "module": mid,
            "module_name": mname,
            "prompt": prompt,
            "s81b_text": s81b,
            "s81b_sha256": hashlib.sha256(s81b.encode("utf-8")).hexdigest(),
            "source": "knowledge/domains/painters/modules/%s.md §8.1b" % mid,
        })
    doc = {
        "experiment": "E-02 · E1_t1b 纯风格段（§8.1b）重跑 · 主题 T1（暴风雨中的海边灯塔）",
        "date": "2026-10-15",
        "model": "grok-imagine-image-2.0",
        "endpoint": "/v1/images/generations",
        "size_requested": "1024x1536",
        "theme": THEME,
        "recipe": ("prompt = THEME + ' ' + 模块卡 §8.1b 纯风格正向段（逐行解包为单行）；"
                   "负向段未随请求发送（通道无负向参数）；E0 对照复用 E1_t1（不重跑）。"),
        "control": "experiments/E1_t1/cells/e0_baseline（复用）",
        "counterpart": "experiments/E1_t1/（偏置版 §8.1，对照用）",
        "cells": cells,
    }
    out = os.path.join(HERE, "prompts_t1b.json")
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
    print("wrote %s (%d cells)" % (out, len(cells)))
    for c in cells:
        print("  %-16s s81b=%dc prompt=%dc sha=%s" %
              (c["cell"], len(c["s81b_text"]), len(c["prompt"]), c["s81b_sha256"][:8]))


if __name__ == "__main__":
    main()
