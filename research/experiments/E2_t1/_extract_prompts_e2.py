#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E2_t1 · 组合 prompt 构建（E-04 首批组合实验，70/30 主辅）→ prompts_e2.json

配方（E-04 口径，全文见 RESULTS_E2.md §0）：
  prompt = THEME + " " + 融合句（70/30） + " " + 主段 + " " + 辅段 [+ " " + 分区句（仅 e2c）]
  主/辅段来源（逐字，逐行解包为单行，内容不变）：
    - §8.1b 纯风格段：da_vinci / caravaggio / cezanne（E-02 派生的 7 卡之 3）
    - §8.1 正向段（+ §8.1b 场景可迁移性注记口径）：monet / van_gogh（4 卡之 2）
  负向段：不随请求发送（通道无负向参数）；原文一并存档备查（N1 重算记录见 RESULTS_E2.md §3）。

校验：三格主/辅段均可从模块卡解包；prompt 组装后逐段回含（self-check）。
"""
import hashlib
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "prompts", "artist_modules"))

THEME = ("A lighthouse on a rocky coast in a storm, towering waves crashing against "
         "the rocks, dark storm clouds overhead.")

# e2c · C-10 分区句（显式写分层边界；② 对比梯度限远景层 ③ 近景禁雾色）
PARTITION_E2C = (
    "Split the scene into two explicit layers at the horizon: the sky and the distant "
    "water layer follow the atmospheric envelope — soft haze, a gradual falling-off of "
    "contrast confined to this layer, colour gathered into one air tone; the mid-ground "
    "and foreground layer (rocks, waves, the lighthouse) follows the structural treatment "
    "— compressed space, near and far forms at the same scale, shifting viewpoints, and "
    "no fog or haze colour in this near layer."
)

CELLS = [
    {
        "cell": "e2a_monet_van_gogh",
        "title": "E2a · 莫奈(主) + 梵高(辅)",
        "main": {"id": "monet", "zh": "莫奈", "en": "Claude Monet", "source": "§8.1 正向段（4 卡注记口径：可迁移，无需拆分）"},
        "aux": {"id": "van_gogh", "zh": "梵高", "en": "Vincent van Gogh", "source": "§8.1 正向段（4 卡注记口径：可迁移；风景道具词仅作次要元素）"},
        "partition": None,
    },
    {
        "cell": "e2b_da_vinci_caravaggio",
        "title": "E2b · 达·芬奇(主) + 卡拉瓦乔(辅)",
        "main": {"id": "da_vinci", "zh": "达·芬奇", "en": "Leonardo da Vinci", "source": "§8.1b 纯风格段（7 卡）"},
        "aux": {"id": "caravaggio", "zh": "卡拉瓦乔", "en": "Caravaggio", "source": "§8.1b 纯风格段（7 卡）"},
        "partition": None,
    },
    {
        "cell": "e2c_monet_cezanne",
        "title": "E2c · 莫奈(主) + 塞尚(辅)",
        "main": {"id": "monet", "zh": "莫奈", "en": "Claude Monet", "source": "§8.1 正向段（4 卡注记口径）"},
        "aux": {"id": "cezanne", "zh": "塞尚", "en": "Paul Cézanne", "source": "§8.1b 纯风格段（7 卡）"},
        "partition": PARTITION_E2C,
    },
]


def _fence_after(md_text, pos):
    """取 pos 之后第一个 ``` 围栏块，逐行解包为单行（内容不变）。"""
    j = md_text.find("```", pos)
    k = md_text.find("```", j + 3)
    if j < 0 or k < 0:
        raise ValueError("fence not found after pos=%d" % pos)
    return " ".join(md_text[j + 3:k].split())


def extract_s81b(md_text):
    """「## §8.1b 纯风格段（场景可迁移）」后第一个围栏块。"""
    marker = "## §8.1b 纯风格段（场景可迁移）"
    idx = md_text.find(marker)
    if idx < 0:
        raise ValueError("§8.1b marker not found")
    return _fence_after(md_text, idx)


def extract_s81_pos(md_text):
    """「**正向段」后第一个围栏块（§8.1 正向段；4 卡口径）。"""
    m = re.search(r"\*\*正向段", md_text)
    if not m:
        raise ValueError("§8.1 positive marker not found")
    return _fence_after(md_text, m.end())


def extract_negative(md_text):
    """「**负向约束」后第一个围栏块（原文存档；不发送）。"""
    m = re.search(r"\*\*负向约束", md_text)
    if not m:
        raise ValueError("negative marker not found")
    return _fence_after(md_text, m.end())


def build_cell(cfg):
    segs = {}
    negs = {}
    for role in ("main", "aux"):
        mid = cfg[role]["id"]
        with open(os.path.join(MODULES_DIR, mid + ".md"), encoding="utf-8") as fh:
            md = fh.read()
        seg = extract_s81b(md) if mid in ("da_vinci", "caravaggio", "cezanne") else extract_s81_pos(md)
        segs[role] = seg
        negs[role] = extract_negative(md)
    lead = ("Fusion of two painterly languages: %s dominant (70%%), %s secondary (30%%)."
            % (cfg["main"]["en"], cfg["aux"]["en"]))
    parts = [THEME, lead, segs["main"], segs["aux"]]
    if cfg["partition"]:
        parts.append(cfg["partition"])
    prompt = " ".join(parts)
    # self-check：逐段回含
    for p in parts:
        assert p in prompt, "segment not contained in prompt"
    return {
        "cell": cfg["cell"],
        "title": cfg["title"],
        "main": dict(cfg["main"]),
        "aux": dict(cfg["aux"]),
        "lead": lead,
        "partition": cfg["partition"],
        "main_segment": segs["main"],
        "aux_segment": segs["aux"],
        "main_segment_sha256": hashlib.sha256(segs["main"].encode("utf-8")).hexdigest(),
        "aux_segment_sha256": hashlib.sha256(segs["aux"].encode("utf-8")).hexdigest(),
        "main_negative": negs["main"],
        "aux_negative": negs["aux"],
        "prompt": prompt,
        "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
    }


def main():
    cells = [build_cell(c) for c in CELLS]
    doc = {
        "experiment": "E-04 · E2 首批组合实验（70/30 主辅）· 主题 T1（暴风雨中的海边灯塔）",
        "date": "2026-10-15",
        "model": "grok-imagine-image-2.0",
        "endpoint": "/v1/images/generations",
        "size_requested": "1024x1536",
        "theme": THEME,
        "recipe": ("prompt = THEME + ' ' + 融合句（70/30） + ' ' + 主段 + ' ' + 辅段 "
                   "[+ ' ' + 分区句（仅 e2c）]；主/辅段逐字取自模块卡（§8.1b 或 §8.1）；"
                   "负向段未随请求发送（通道无负向参数），原文存档备查。"),
        "cells": cells,
    }
    out = os.path.join(HERE, "prompts_e2.json")
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
    print("wrote %s (%d cells)" % (out, len(cells)))
    for c in cells:
        print("=" * 100)
        print(c["cell"], "|", c["title"])
        print("  main seg sha=%s  aux seg sha=%s  prompt sha=%s" % (
            c["main_segment_sha256"][:8], c["aux_segment_sha256"][:8], c["prompt_sha256"][:8]))
        print("  prompt chars:", len(c["prompt"]))
        print("-" * 100)
        print(c["prompt"])
    print("=" * 100)


if __name__ == "__main__":
    main()
