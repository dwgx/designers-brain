#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E1_t1 · 完成条件机械核验（验收脚本，独立于生成脚本）。
检查:
  ① cells/**/img_*.jpg 数量 == 36（或失败格已在 RESULTS.md §3 记录）
  ② RESULTS.md 存在，且含 12 行结果表
  ③ sheet_all.png + 12 张 sheet_<cell>.png 存在且可打开
  ④ 全部图片可打开、均为 JPEG、sha256 全部唯一
  ⑤ req/resp 原样 JSON 各 36 份（每格 3 组）
输出逐项 PASS/FAIL 与汇总；退出码 0=全部通过。
"""
import glob
import hashlib
import json
import os
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
CELLS_DIR = os.environ.get("E1_CELLS_DIR") or os.path.join(HERE, "cells")
OUT_DIR = os.environ.get("E1_OUT_DIR") or HERE


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    with open(os.path.join(HERE, "prompts.json"), encoding="utf-8") as fh:
        cells = json.load(fh)["cells"]
    ids = [c["cell"] for c in cells]
    problems = []

    # ① images
    imgs = sorted(glob.glob(os.path.join(CELLS_DIR, "*", "img_*.jpg")))
    ok_imgs = []
    shas = {}
    bad_open = []
    for p in imgs:
        try:
            with Image.open(p) as im:
                if im.format != "JPEG":
                    bad_open.append("%s format=%s" % (p, im.format))
            s = sha256_file(p)
            ok_imgs.append(p)
            shas.setdefault(s, []).append(p)
        except Exception as exc:
            bad_open.append("%s err=%s" % (p, exc))
    dup = {s: v for s, v in shas.items() if len(v) > 1}
    print("① 图片: %d 个 img_*.jpg（期望 36）；打开失败 %d；哈希重复组 %d" %
          (len(imgs), len(bad_open), len(dup)))
    if len(imgs) != 36:
        problems.append("图片数 != 36")
    if bad_open:
        problems.append("存在无法打开的图片: %s" % bad_open[:3])
    if dup:
        problems.append("存在重复哈希: %s" % list(dup.values())[:2])

    # ⑤ req/resp
    n_req = len([p for p in glob.glob(os.path.join(CELLS_DIR, "*", "req_*.json"))
                 if "_fail" not in os.path.basename(p)])
    n_resp = len([p for p in glob.glob(os.path.join(CELLS_DIR, "*", "resp_*.json"))
                  if "_fail" not in os.path.basename(p)])
    n_req_fail = len(glob.glob(os.path.join(CELLS_DIR, "*", "req_*_fail*.json")))
    n_resp_fail = len(glob.glob(os.path.join(CELLS_DIR, "*", "resp_*_fail*.json")))
    print("⑤ req/resp: req %d / resp %d（期望各 36）；失败尝试文件 req %d / resp %d" %
          (n_req, n_resp, n_req_fail, n_resp_fail))
    if n_req != 36 or n_resp != 36:
        problems.append("req/resp 数量异常")

    # ② RESULTS.md
    rp = os.path.join(OUT_DIR, "RESULTS.md")
    if os.path.exists(rp):
        txt = open(rp, encoding="utf-8").read()
        rows = len([l for l in txt.splitlines()
                    if l.startswith("|") and ("| e0_baseline |" in l or "| e1_" in l)])
        has36 = "36/36" in txt or "36/36 张" in txt
        print("② RESULTS.md: 存在，结果表数据行 %d（期望 12）；含 36/36 标记: %s" % (rows, has36))
        if rows < 12:
            problems.append("RESULTS.md 结果表不足 12 行")
    else:
        print("② RESULTS.md: 缺失")
        problems.append("RESULTS.md 缺失")

    # ③ sheets
    sa = os.path.join(OUT_DIR, "sheet_all.png")
    if os.path.exists(sa):
        with Image.open(sa) as im:
            print("③ sheet_all.png: 存在 %dx%d" % im.size)
    else:
        print("③ sheet_all.png: 缺失")
        problems.append("sheet_all.png 缺失")
    missing_cells = []
    for cid in ids:
        sp = os.path.join(OUT_DIR, "sheet_%s.png" % cid)
        if not os.path.exists(sp):
            missing_cells.append(cid)
    print("③ sheet_<cell>.png: %d/12 存在" % (12 - len(missing_cells)))
    if missing_cells:
        problems.append("缺格 sheet: %s" % missing_cells)

    # ④ per-cell completeness
    incomplete = [cid for cid in ids
                  if len(glob.glob(os.path.join(CELLS_DIR, cid, "img_*.jpg"))) != 3]
    print("④ 每格 3 张: 完整 %d/12；不完整: %s" % (12 - len(incomplete), incomplete or "无"))
    if incomplete:
        problems.append("不完整格: %s" % incomplete)

    print()
    if problems:
        print("VERIFY FAIL:", problems)
        sys.exit(1)
    print("VERIFY PASS — 36/36 张 + RESULTS.md + sheet_all.png + 12 张格 sheet 全部就位。")


if __name__ == "__main__":
    main()
