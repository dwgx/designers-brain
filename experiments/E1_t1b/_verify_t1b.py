#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E1_t1b · 完成条件机械核验（验收脚本，独立于生成脚本）。
检查:
  ① cells/**/img_*.jpg 数量 == 21（7 格 × 3）
  ② RESULTS_t1b.md 存在：含 12 行诊断表（场景保留/场景被替换）+ 7 行同格对照 + 7 格覆盖
  ③ sheet_all_t1b.png + 7 张 sheet_<cell>.png + 7 张 compare_<cell>.png + compare_all_t1b.png
  ④ 全部图片可打开、均为 JPEG、sha256 全部唯一
  ⑤ req/resp 原样 JSON 各 21 份（每格 3 组）
  ⑥ 模块卡 §8.1b：7 卡「纯风格段」+ 4 卡「场景可迁移性注记」
  ⑦ 模块卡逐字校验：python _extract.py --check → fail=0 且 ok=checks（保底 ≥33）
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
CELLS_DIR = os.environ.get("E1B_CELLS_DIR") or os.path.join(HERE, "cells")
OUT_DIR = os.environ.get("E1B_OUT_DIR") or HERE
MODULES_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "knowledge", "domains", "painters", "modules"))

PURE = ["da_vinci", "michelangelo", "picasso", "cezanne", "caravaggio", "vermeer", "durer"]
NOTE = ["van_gogh", "monet", "matisse", "hokusai"]
N_EXPECT = 21


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    with open(os.path.join(HERE, "prompts_t1b.json"), encoding="utf-8") as fh:
        cells = json.load(fh)["cells"]
    ids = [c["cell"] for c in cells]
    problems = []

    # ① images
    imgs = sorted(glob.glob(os.path.join(CELLS_DIR, "*", "img_*.jpg")))
    bad_open = []
    shas = {}
    for p in imgs:
        try:
            with Image.open(p) as im:
                if im.format != "JPEG":
                    bad_open.append("%s format=%s" % (p, im.format))
                im.verify()
            s = sha256_file(p)
            shas.setdefault(s, []).append(p)
        except Exception as exc:
            bad_open.append("%s err=%s" % (p, exc))
    dup = {s: v for s, v in shas.items() if len(v) > 1}
    print("① 图片: %d 个 img_*.jpg（期望 %d）；打开失败 %d；哈希重复组 %d" %
          (len(imgs), N_EXPECT, len(bad_open), len(dup)))
    if len(imgs) != N_EXPECT:
        problems.append("图片数 != %d" % N_EXPECT)
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
    print("⑤ req/resp: req %d / resp %d（期望各 %d）；失败尝试文件 req %d / resp %d" %
          (n_req, n_resp, N_EXPECT, n_req_fail, n_resp_fail))
    if n_req != N_EXPECT or n_resp != N_EXPECT:
        problems.append("req/resp 数量异常")

    # ② RESULTS_t1b.md
    rp = os.path.join(OUT_DIR, "RESULTS_t1b.md")
    if os.path.exists(rp):
        txt = open(rp, encoding="utf-8").read()
        diag_rows = [l for l in txt.splitlines()
                     if re.match(r"^\|\s*\d+\s*\|", l) and ("场景保留" in l or "场景被替换" in l)]
        comp_rows = [l for l in txt.splitlines()
                     if re.match(r"^\|\s*\d+\s*\|", l) and "解除" in l]
        miss_cells = [cid for cid in ids if cid not in txt]
        print("② RESULTS_t1b.md: 诊断表行 %d（期望 ≥12）；同格对照行 %d（期望 ≥7）；缺格 %s" %
              (len(diag_rows), len(comp_rows), miss_cells or "无"))
        if len(diag_rows) < 12:
            problems.append("诊断表不足 12 行")
        if len(comp_rows) < 7:
            problems.append("同格对照不足 7 行")
        if miss_cells:
            problems.append("RESULTS_t1b.md 未覆盖: %s" % miss_cells)
    else:
        print("② RESULTS_t1b.md: 缺失")
        problems.append("RESULTS_t1b.md 缺失")

    # ③ sheets
    sa = os.path.join(OUT_DIR, "sheet_all_t1b.png")
    ca = os.path.join(OUT_DIR, "compare_all_t1b.png")
    for p, label in ((sa, "sheet_all_t1b.png"), (ca, "compare_all_t1b.png")):
        if os.path.exists(p):
            with Image.open(p) as im:
                print("③ %s: 存在 %dx%d" % (label, im.size[0], im.size[1]))
        else:
            print("③ %s: 缺失" % label)
            problems.append("%s 缺失" % label)
    missing_sheets = [cid for cid in ids
                      if not os.path.exists(os.path.join(OUT_DIR, "sheet_%s.png" % cid))]
    missing_cmp = [cid for cid in ids
                   if not os.path.exists(os.path.join(OUT_DIR, "compare_%s.png" % cid))]
    print("③ sheet_<cell>.png: %d/7；compare_<cell>.png: %d/7" %
          (7 - len(missing_sheets), 7 - len(missing_cmp)))
    if missing_sheets:
        problems.append("缺格 sheet: %s" % missing_sheets)
    if missing_cmp:
        problems.append("缺格 compare: %s" % missing_cmp)

    # ④ per-cell completeness
    incomplete = [cid for cid in ids
                  if len(glob.glob(os.path.join(CELLS_DIR, cid, "img_*.jpg"))) != 3]
    print("④ 每格 3 张: 完整 %d/7；不完整: %s" % (7 - len(incomplete), incomplete or "无"))
    if incomplete:
        problems.append("不完整格: %s" % incomplete)

    # ⑥ §8.1b in module cards
    miss_pure = []
    for mid in PURE:
        t = open(os.path.join(MODULES_DIR, mid + ".md"), encoding="utf-8").read()
        if "## §8.1b 纯风格段（场景可迁移）" not in t:
            miss_pure.append(mid)
    miss_note = []
    for mid in NOTE:
        t = open(os.path.join(MODULES_DIR, mid + ".md"), encoding="utf-8").read()
        if "## §8.1b 场景可迁移性注记" not in t:
            miss_note.append(mid)
    print("⑥ 模块卡 §8.1b: 纯风格段 %d/7；注记 %d/4" % (7 - len(miss_pure), 4 - len(miss_note)))
    if miss_pure:
        problems.append("缺 §8.1b 纯风格段: %s" % miss_pure)
    if miss_note:
        problems.append("缺 §8.1b 注记: %s" % miss_note)

    # ⑦ module verbatim check
    try:
        r = subprocess.run([sys.executable, "_extract.py", "--check"], cwd=MODULES_DIR,
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        import re as _re
        # 动态解析（卡数 11→20→42→62 增长不再破；保底 ≥33 = 原始验收下限）
        _m = _re.search(r"checks=(\d+) ok=(\d+) fail=(\d+)", r.stdout)
        ok7 = bool(_m) and _m.group(3) == "0" and _m.group(1) == _m.group(2) and int(_m.group(2)) >= 33
        print("⑦ 模块卡逐字校验: %s" % (("checks=%s ok=%s fail=0（≥33 保底）" % (_m.group(1), _m.group(2))) if ok7 else "FAIL\n" + r.stdout[-400:]))
        if not ok7:
            problems.append("模块卡逐字校验失败")
    except Exception as exc:
        print("⑦ 模块卡逐字校验: 运行失败 %s" % exc)
        problems.append("模块卡逐字校验无法运行")

    print()
    if problems:
        print("VERIFY FAIL:", problems)
        sys.exit(1)
    print("VERIFY PASS — 21/21 张 + 诊断表(12) + 同格对照(7) + §8.1b(7+4) + 逐字校验(全过，≥33 保底) 全部就位。")


if __name__ == "__main__":
    main()
