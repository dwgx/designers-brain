#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E1_t1c · 完成条件机械核验（验收脚本，独立于生成脚本）。
检查:
  ① cells/e1_michelangelo_v2/img_*.jpg 数量 == 3；可打开、JPEG、sha256 唯一
  ② req/resp 原样 JSON 各 3 份（每格 3 组）
  ③ sheet_e1_michelangelo_v2.png + compare_michelangelo_v2.png 存在且可打开
  ④ RESULTS_t1c.md 存在：含逐处对照表（≥7 行）、三版标签、结论「解除」、v1/v2 sha
  ⑤ 模块卡 §8.1b：v2 块 == prompts_t1c.json（sha 214dd673…）；v1 审计存档 == snapshot 逐字；
     「重跑验证」回填行存在
  ⑥ 对照源存在：E1_t1（偏置）与 E1_t1b（v1）各 3 张
  ⑦ 模块卡逐字校验：python _extract.py --check → ok=33 fail=0
输出逐项 PASS/FAIL 与汇总；退出码 0=全部通过。
"""
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
CELLS_DIR = os.environ.get("E1C_CELLS_DIR") or os.path.join(HERE, "cells")
OUT_DIR = os.environ.get("E1C_OUT_DIR") or HERE
MODULES_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "prompts", "artist_modules"))
E1_T1_DIR = os.path.normpath(os.path.join(HERE, "..", "E1_t1"))
E1_T1B_DIR = os.path.normpath(os.path.join(HERE, "..", "E1_t1b"))

CELL = "e1_michelangelo_v2"
V2_SHA = "214dd6735d18f8352fe24bbca4b7d0533112e2adb392644d32b9f582d180f0e7"
V1_SHA = "3326164fb5666fb9cd5dc896ea3cd267c4c95f9f568e2d96c8909cbc0ee24c2c"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_fence_after(text, marker, start=0):
    m = text.find(marker, start)
    if m < 0:
        return None
    j = text.find("```", m)
    k = text.find("```", j + 3)
    if j < 0 or k < 0:
        return None
    return text[j + 3:k]


def main():
    problems = []

    # ① images
    imgs = sorted(glob.glob(os.path.join(CELLS_DIR, CELL, "img_*.jpg")))
    bad = []
    shas = {}
    for p in imgs:
        try:
            with Image.open(p) as im:
                if im.format != "JPEG":
                    bad.append("%s format=%s" % (p, im.format))
                im.verify()
            shas.setdefault(sha256_file(p), []).append(p)
        except Exception as exc:
            bad.append("%s err=%s" % (p, exc))
    dup = {s: v for s, v in shas.items() if len(v) > 1}
    print("① 图片: %d 个（期望 3）；打开失败 %d；哈希重复组 %d" % (len(imgs), len(bad), len(dup)))
    if len(imgs) != 3:
        problems.append("图片数 != 3")
    if bad:
        problems.append("无法打开的图片: %s" % bad[:3])
    if dup:
        problems.append("重复哈希: %s" % list(dup.values())[:2])

    # ② req/resp
    n_req = len([p for p in glob.glob(os.path.join(CELLS_DIR, CELL, "req_*.json"))
                 if "_fail" not in os.path.basename(p)])
    n_resp = len([p for p in glob.glob(os.path.join(CELLS_DIR, CELL, "resp_*.json"))
                  if "_fail" not in os.path.basename(p)])
    print("② req/resp: req %d / resp %d（期望各 3）" % (n_req, n_resp))
    if n_req != 3 or n_resp != 3:
        problems.append("req/resp 数量异常")

    # ③ sheets
    for name in ("sheet_e1_michelangelo_v2.png", "compare_michelangelo_v2.png"):
        p = os.path.join(OUT_DIR, name)
        if os.path.exists(p):
            with Image.open(p) as im:
                print("③ %s: 存在 %dx%d" % (name, im.size[0], im.size[1]))
        else:
            print("③ %s: 缺失" % name)
            problems.append("%s 缺失" % name)

    # ④ RESULTS_t1c.md
    rp = os.path.join(OUT_DIR, "RESULTS_t1c.md")
    if os.path.exists(rp):
        txt = open(rp, encoding="utf-8").read()
        clause_rows = [l for l in txt.splitlines() if re.match(r"^\|\s*[1-7]\s*\|", l)]
        has_jiechu = "解除" in txt
        has_three = all(s in txt for s in ("E1 偏置", "E1b", "E1c"))
        has_v1 = V1_SHA[:8] in txt
        has_v2 = V2_SHA[:8] in txt
        print("④ RESULTS_t1c.md: 对照表行 %d（期望 ≥7）；「解除」%s；三版标签 %s；v1 sha %s；v2 sha %s" %
              (len(clause_rows), has_jiechu, has_three, has_v1, has_v2))
        if len(clause_rows) < 7:
            problems.append("逐处对照表不足 7 行")
        if not has_jiechu:
            problems.append("RESULTS 缺结论「解除」")
        if not has_three:
            problems.append("RESULTS 缺三版标签")
        if not (has_v1 and has_v2):
            problems.append("RESULTS 缺 v1/v2 sha")
    else:
        print("④ RESULTS_t1c.md: 缺失")
        problems.append("RESULTS_t1c.md 缺失")

    # ⑤ module card consistency
    with open(os.path.join(MODULES_DIR, "michelangelo.md"), encoding="utf-8") as fh:
        card = fh.read()
    with open(os.path.join(HERE, "prompts_t1c.json"), encoding="utf-8") as fh:
        doc = json.load(fh)
    s81b = doc["cells"][0]["s81b_text"]
    card_v2 = extract_fence_after(card, "**正向段 v2（可直接粘贴）**：")
    card_v1 = extract_fence_after(card, "### v1 审计存档")
    with open(os.path.join(HERE, "s81b_v1_snapshot.md"), encoding="utf-8") as fh:
        snap = fh.read()
    snap_v1 = extract_fence_after(snap, "**正向段（可直接粘贴）**：")
    ok_v2 = card_v2 is not None and " ".join(card_v2.split()) == s81b
    ok_v1 = card_v1 is not None and card_v1 == snap_v1
    ok_line = "重跑验证" in card
    print("⑤ 模块卡: v2==prompts %s；v1 存档==snapshot %s；回填行 %s；v2 sha==%s %s" %
          (ok_v2, ok_v1, ok_line, V2_SHA[:8],
           hashlib.sha256(s81b.encode("utf-8")).hexdigest() == V2_SHA))
    if not ok_v2:
        problems.append("卡内 v2 块与 prompts_t1c.json 不一致")
    if not ok_v1:
        problems.append("卡内 v1 存档与 snapshot 不一致")
    if not ok_line:
        problems.append("卡内缺「重跑验证」回填行")
    if hashlib.sha256(s81b.encode("utf-8")).hexdigest() != V2_SHA:
        problems.append("v2 sha 与预期不符")

    # ⑥ counterparts
    c1 = glob.glob(os.path.join(E1_T1_DIR, "cells", "e1_michelangelo", "img_*.jpg"))
    c2 = glob.glob(os.path.join(E1_T1B_DIR, "cells", "e1_michelangelo", "img_*.jpg"))
    print("⑥ 对照源: E1_t1 %d 张 / E1_t1b %d 张（期望各 3）" % (len(c1), len(c2)))
    if len(c1) != 3 or len(c2) != 3:
        problems.append("对照源图片缺失")

    # ⑦ module verbatim check
    try:
        r = subprocess.run([sys.executable, "_extract.py", "--check"], cwd=MODULES_DIR,
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        ok7 = ("fail=0" in r.stdout) and ("ok=33" in r.stdout)
        print("⑦ 模块卡逐字校验: %s" % ("ok=33 fail=0" if ok7 else "FAIL\n" + r.stdout[-400:]))
        if not ok7:
            problems.append("模块卡逐字校验失败")
    except Exception as exc:
        print("⑦ 模块卡逐字校验: 运行失败 %s" % exc)
        problems.append("模块卡逐字校验无法运行")

    print()
    if problems:
        print("VERIFY FAIL:", problems)
        sys.exit(1)
    print("VERIFY PASS — 3/3 张 + req/resp + 三版对照图 + §8.1b v2（卡内/快照/回填）+ 逐字校验(33/33) 全部就位。")


if __name__ == "__main__":
    main()
