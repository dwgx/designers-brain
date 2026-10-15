#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E2_t1 · 完成条件机械核验（验收脚本，独立于生成脚本）。
检查:
  ① cells/**/img_*.jpg 数量 == 9（3 格 × 3）；可打开、JPEG、sha256 唯一
  ② req/resp 原样 JSON 各 9 份（每格 3 组；失败尝试另计）
  ③ RESULTS_E2.md：存在；含 N1 / N4 / N9 / 双标准 记录；覆盖 3 格；含各格 prompt sha 前 8
  ④ sheet_all_e2.png + 3 张 sheet_<cell>.png
  ⑤ prompts_e2.json 与模块卡重抽逐段一致（sha256 复核）
  ⑥ combo_records.json：3 格 × {n1, n4, n9} 记录
  ⑦ 模块卡逐字校验回归：python _extract.py --check → ok=33 fail=0
输出逐项 PASS/FAIL 与汇总；退出码 0=全部通过。
"""
import glob
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
CELLS_DIR = os.environ.get("E2_CELLS_DIR") or os.path.join(HERE, "cells")
OUT_DIR = os.environ.get("E2_OUT_DIR") or HERE
MODULES_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "prompts", "artist_modules"))

CELL_IDS = ["e2a_monet_van_gogh", "e2b_da_vinci_caravaggio", "e2c_monet_cezanne"]
N_EXPECT = 9


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_extractor():
    spec = importlib.util.spec_from_file_location(
        "_extract_prompts_e2", os.path.join(HERE, "_extract_prompts_e2.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    with open(os.path.join(HERE, "prompts_e2.json"), encoding="utf-8") as fh:
        doc = json.load(fh)
    cells = doc["cells"]
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

    # ② req/resp
    n_req = len([p for p in glob.glob(os.path.join(CELLS_DIR, "*", "req_*.json"))
                 if "_fail" not in os.path.basename(p)])
    n_resp = len([p for p in glob.glob(os.path.join(CELLS_DIR, "*", "resp_*.json"))
                  if "_fail" not in os.path.basename(p)])
    n_req_fail = len(glob.glob(os.path.join(CELLS_DIR, "*", "req_*_fail*.json")))
    n_resp_fail = len(glob.glob(os.path.join(CELLS_DIR, "*", "resp_*_fail*.json")))
    print("② req/resp: req %d / resp %d（期望各 %d）；失败尝试文件 req %d / resp %d" %
          (n_req, n_resp, N_EXPECT, n_req_fail, n_resp_fail))
    if n_req != N_EXPECT or n_resp != N_EXPECT:
        problems.append("req/resp 数量异常")

    # ③ RESULTS_E2.md
    rp = os.path.join(OUT_DIR, "RESULTS_E2.md")
    if os.path.exists(rp):
        txt = open(rp, encoding="utf-8").read()
        need_tokens = ["N1", "N4", "N9", "双标准"]
        miss_tok = [t for t in need_tokens if t not in txt]
        miss_cells = [cid for cid in ids if cid not in txt]
        n_lead = txt.count("Fusion of two painterly languages")
        sha_hits = {c["cell"]: (c["prompt_sha256"][:8] in txt) for c in cells}
        prompt_missing = [c["cell"] for c in cells if c["prompt"] not in txt]
        print("③ RESULTS_E2.md: 关键词缺 %s；缺格 %s；融合句出现 %d 次；prompt sha 前8命中 %s；prompt 全文缺 %s" %
              (miss_tok or "无", miss_cells or "无", n_lead, sha_hits, prompt_missing or "无"))
        if miss_tok:
            problems.append("RESULTS_E2.md 缺关键词: %s" % miss_tok)
        if miss_cells:
            problems.append("RESULTS_E2.md 未覆盖: %s" % miss_cells)
        if n_lead < 3:
            problems.append("融合句出现 <3 次")
        if not all(sha_hits.values()):
            problems.append("prompt sha 前8 未全部出现: %s" % sha_hits)
        if prompt_missing:
            problems.append("prompt 全文未出现（可能转录误差）: %s" % prompt_missing)
    else:
        print("③ RESULTS_E2.md: 缺失")
        problems.append("RESULTS_E2.md 缺失")

    # ④ sheets
    sa = os.path.join(OUT_DIR, "sheet_all_e2.png")
    if os.path.exists(sa):
        with Image.open(sa) as im:
            print("④ sheet_all_e2.png: 存在 %dx%d" % (im.size[0], im.size[1]))
    else:
        print("④ sheet_all_e2.png: 缺失")
        problems.append("sheet_all_e2.png 缺失")
    missing_sheets = [cid for cid in ids
                      if not os.path.exists(os.path.join(OUT_DIR, "sheet_%s.png" % cid))]
    print("④ sheet_<cell>.png: %d/3" % (3 - len(missing_sheets)))
    if missing_sheets:
        problems.append("缺格 sheet: %s" % missing_sheets)

    # ⑤ prompts re-extraction
    try:
        mod = load_extractor()
        rebuilt = [mod.build_cell(c) for c in mod.CELLS]
        ok5 = all(rb["prompt"] == c["prompt"] and
                  rb["main_segment_sha256"] == c["main_segment_sha256"] and
                  rb["aux_segment_sha256"] == c["aux_segment_sha256"]
                  for rb, c in zip(rebuilt, cells))
        print("⑤ prompts_e2.json 重抽复核: %s" % ("一致" if ok5 else "不一致"))
        if not ok5:
            problems.append("prompts_e2.json 与模块卡重抽不一致")
    except Exception as exc:
        print("⑤ prompts_e2.json 重抽复核: 运行失败 %s" % exc)
        problems.append("prompts_e2.json 重抽复核无法运行")

    # ⑥ combo_records.json
    crp = os.path.join(OUT_DIR, "combo_records.json")
    if os.path.exists(crp):
        with open(crp, encoding="utf-8") as fh:
            rec = json.load(fh)
        rec_ids = [c.get("cell") for c in rec.get("cells", [])]
        ok6 = rec_ids == ids and all(
            set(c.keys()) >= {"cell", "n1", "n4", "n9"} for c in rec["cells"])
        print("⑥ combo_records.json: %s（cells=%s）" % ("OK" if ok6 else "结构异常", rec_ids))
        if not ok6:
            problems.append("combo_records.json 结构异常")
    else:
        print("⑥ combo_records.json: 缺失")
        problems.append("combo_records.json 缺失")

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
    print("VERIFY PASS — 9/9 张 + RESULTS_E2.md（N1/N4/N9/双标准） + sheet_all_e2 + 3 格 sheet + 重抽复核 + 逐字校验(33/33) 全部就位。")


if __name__ == "__main__":
    main()
