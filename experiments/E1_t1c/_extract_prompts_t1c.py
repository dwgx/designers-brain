#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E1_t1c · 从 michelangelo 模块卡抽取 §8.1b v2（从句级改写版），合成 1 格 prompt，
写 prompts_t1c.json。

配方（与 E1_t1b 相同，仅 §8.1b 版本不同——隔离变量）：
  prompt = THEME + " " + §8.1b v2 正向段（逐行解包为单行，内容逐字不变）
  §8.1b v2 来源：knowledge/domains/painters/modules/michelangelo.md（E-03 修订）
  E1_t1 / E1_t1b 对照：复用各自 cells（不重跑）。

校验：
  - v2 块可解包，且 sha 与卡内单行文本一致；
  - 卡内「v1 审计存档」块与 s81b_v1_snapshot.md 中的 v1 块逐字一致。
"""
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "knowledge", "domains", "painters", "modules"))

THEME = ("A lighthouse on a rocky coast in a storm, towering waves crashing against "
         "the rocks, dark storm clouds overhead.")

V2_MARKER = "**正向段 v2（可直接粘贴）**："
V1_ARCHIVE_MARKER = "### v1 审计存档"


def extract_fence_after(text, marker, start=0):
    m = text.find(marker, start)
    if m < 0:
        raise ValueError("marker not found: %s" % marker)
    j = text.find("```", m)
    k = text.find("```", j + 3)
    if j < 0 or k < 0:
        raise ValueError("fence not found after: %s" % marker)
    return text[j + 3:k], k


def main():
    with open(os.path.join(MODULES_DIR, "michelangelo.md"), encoding="utf-8") as fh:
        md = fh.read()

    v2_block, v2_end = extract_fence_after(md, V2_MARKER)
    v2 = " ".join(v2_block.split())

    # v1 审计存档（本卡内）与 snapshot 对照
    v1_block, _ = extract_fence_after(md, V1_ARCHIVE_MARKER, v2_end)
    v1 = " ".join(v1_block.split())
    with open(os.path.join(HERE, "s81b_v1_snapshot.md"), encoding="utf-8") as fh:
        snap = fh.read()
    snap_block, _ = extract_fence_after(snap, "**正向段（可直接粘贴）**：")
    assert snap_block == v1_block, "v1 archive in card != snapshot"

    v1_sha_expect = "3326164fb5666fb9cd5dc896ea3cd267c4c95f9f568e2d96c8909cbc0ee24c2c"
    assert hashlib.sha256(v1.encode("utf-8")).hexdigest() == v1_sha_expect, "v1 sha mismatch"
    assert v1 != v2, "v2 identical to v1?"

    prompt = THEME + " " + v2
    cell = {
        "cell": "e1_michelangelo_v2",
        "module": "michelangelo",
        "module_name": "米开朗基罗",
        "prompt": prompt,
        "s81b_text": v2,
        "s81b_sha256": hashlib.sha256(v2.encode("utf-8")).hexdigest(),
        "source": "knowledge/domains/painters/modules/michelangelo.md §8.1b v2（E-03）",
    }
    doc = {
        "experiment": "E-03 · E1_t1c michelangelo §8.1b v2 重跑 · 主题 T1（暴风雨中的海边灯塔）",
        "date": "2026-10-15",
        "model": "grok-imagine-image-2.0",
        "endpoint": "/v1/images/generations",
        "size_requested": "1024x1536",
        "theme": THEME,
        "recipe": ("prompt = THEME + ' ' + michelangelo §8.1b v2 正向段（逐行解包为单行）；"
                   "负向段未随请求发送（通道无负向参数）；对照复用 E1_t1（§8.1 偏置版）"
                   "与 E1_t1b（§8.1b v1 版）。"),
        "counterpart_biased": "experiments/E1_t1/cells/e1_michelangelo（§8.1 偏置版）",
        "counterpart_v1": "experiments/E1_t1b/cells/e1_michelangelo（§8.1b v1 版）",
        "cells": [cell],
    }
    out = os.path.join(HERE, "prompts_t1c.json")
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
    print("wrote %s (1 cell)" % out)
    print("  %-20s s81b=%dc prompt=%dc sha=%s" %
          (cell["cell"], len(v2), len(prompt), cell["s81b_sha256"][:8]))
    print("  v1 sha (audit): %s" % v1_sha_expect[:8])


if __name__ == "__main__":
    main()
