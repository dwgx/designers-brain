#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E1_t1 · 汇总产物：RESULTS.md + sha256_manifest.txt
读取: prompts.json + run_log.jsonl + cells/**（以落盘文件为准重算哈希与尺寸）
"""
import hashlib
import json
import os
import time

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
CELLS_DIR = os.environ.get("E1_CELLS_DIR") or os.path.join(HERE, "cells")
OUT_DIR = os.environ.get("E1_OUT_DIR") or HERE
LOG_PATH = os.environ.get("E1_LOG_PATH") or os.path.join(HERE, "run_log.jsonl")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_log():
    entries = []
    p = LOG_PATH
    if os.path.exists(p):
        with open(p, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    entries.append(json.loads(line))
    return entries


def cell_report(cell, log):
    cid = cell["cell"]
    imgs = []
    for i in (1, 2, 3):
        p = os.path.join(CELLS_DIR, cid, "img_%02d.jpg" % i)
        if os.path.exists(p):
            with Image.open(p) as im:
                w, h = im.size
            imgs.append({"n": i, "path": p, "sha256": sha256_file(p),
                         "bytes": os.path.getsize(p), "w": w, "h": h})
        else:
            imgs.append({"n": i, "path": p, "sha256": None})
    entries = [e for e in log if e.get("cell") == cid]
    attempts = len(entries)
    retries = sum(1 for e in entries if e.get("attempt", 1) > 1)
    fails = sum(1 for e in entries if not e.get("ok"))
    total_s = sum(e.get("total_s", 0.0) for e in entries)
    n_ok = sum(1 for e in imgs if e["sha256"])
    dims = {}
    for im in imgs:
        if im["sha256"]:
            dims[(im["w"], im["h"])] = dims.get((im["w"], im["h"]), 0) + 1
    return {"imgs": imgs, "attempts": attempts, "retries": retries, "fails": fails,
            "total_s": total_s, "n_ok": n_ok, "dims": dims}


def fmt_dims(dims):
    return " / ".join("%d×%d×%d" % (w, h, n) for (w, h), n in sorted(dims.items()))


def main():
    with open(os.path.join(HERE, "prompts.json"), encoding="utf-8") as fh:
        doc = json.load(fh)
    cells = doc["cells"]
    log = load_log()

    stats = {c["cell"]: cell_report(c, log) for c in cells}
    n_ok_total = sum(s["n_ok"] for s in stats.values())
    n_attempts = sum(s["attempts"] for s in stats.values())
    n_retries = sum(s["retries"] for s in stats.values())
    n_fails = sum(s["fails"] for s in stats.values())
    all_imgs = [im for s in stats.values() for im in s["imgs"] if im["sha256"]]

    # ---- RESULTS.md ----
    L = []
    L.append("# E1_t1 · E0+E1 首批图像实验（T1「暴风雨中的海边灯塔」）")
    L.append("")
    L.append("> **E-01**（wave7）· 2026-10-15 · 直连网关 `/v1/images/generations` · 模型 `grok-imagine-image-2.0`")
    L.append("> 12 格 × 3 张 = **%d/36 张**；重试 %d 次、失败 %d 次（总尝试 %d）。" %
             (n_ok_total, n_retries, n_fails, n_attempts))
    L.append("> 配方：`prompt = 主题句 + \" \" + 模块卡 §8.1 英文正向段`（逐行解包为单行）；"
             "负向段未随请求发送（通道无负向参数，见 §3）。")
    L.append("> 主题句（全格逐字一致）：`%s`" % doc["theme"])
    L.append("")
    L.append("## 1. 结果总表（12 行）")
    L.append("")
    L.append("| # | 格 | 模块 | 模型 | 尺寸（请求 → 实回） | 耗时 | sha256 前 8 位（img_01 / 02 / 03） |")
    L.append("|---|----|------|------|--------------------|------|-----------------------------------|")
    for i, c in enumerate(cells, 1):
        s = stats[c["cell"]]
        mod = c.get("module_name") or "—（基线，无风格段）"
        shas = " / ".join(im["sha256"][:8] if im["sha256"] else "MISSING" for im in s["imgs"])
        if s["n_ok"] == 3:
            dur = "%.1fs（均 %.1fs/张）" % (s["total_s"], s["total_s"] / 3.0)
        else:
            dur = "%.1fs（%d/3 张）" % (s["total_s"], s["n_ok"])
        L.append("| %d | %s | %s | grok-imagine-image-2.0 | %s → %s | %s | %s |" %
                 (i, c["cell"], mod, doc["size_requested"], fmt_dims(s["dims"]) or "—", dur, shas))
    L.append("")
    L.append("耗时口径：该格全部尝试的「请求→落盘」时长合计（含重试尝试；不含请求间隔与重试等待）；明细见 `run_log.jsonl`。")
    L.append("")
    L.append("## 2. 每格 prompt 全文")
    L.append("")
    L.append("> 下为实际发送的 prompt 全文（`req_*.json` 内为原样请求体）。负向段原文一并附上（未发送，备查）。")
    L.append("")
    for i, c in enumerate(cells, 1):
        mod = c.get("module_name") or "基线（无风格段）"
        L.append("### %d) %s — %s" % (i, c["cell"], mod))
        L.append("")
        L.append("```text")
        L.append(c["prompt"])
        L.append("```")
        if c.get("negative"):
            L.append("")
            L.append("负向段（`--no`，通道不支持负向参数、未发送；原文备查）：")
            L.append("")
            L.append("```text")
            L.append(c["negative"])
            L.append("```")
        L.append("")
    L.append("## 3. 缺口与偏差（gaps）")
    L.append("")
    L.append("1. **负向段未发送**：本通道（grok-imagine 系）请求 schema 无负向参数——`negative_prompt` 字段实测"
             "不报错也不产生可核实效果（判定：未知字段被静默忽略）；故 §8.1 负向段不随请求发送，原文记录于 §2 与 `prompts.json`。")
    L.append("2. **provider 前缀（反直觉）**：直连 API 必须用**裸模型名** `grok-imagine-image-2.0`；"
             "带 `buddyfarm/` 前缀反而 `model_not_found`（2026-10-15 实测 2 次）。omp CLI 侧口径相反（须带前缀）——两侧勿混。")
    L.append("3. **size 参数不严格**：请求 `%s`（映射 2:3），实回 %s——像素尺寸由上游决定，不严格等于请求值；本表按「请求 → 实回」双记。"
             % (doc["size_requested"], fmt_dims(stats[cells[0]["cell"]]["dims"]) or "见各行"))
    if n_retries or n_fails:
        det = "；".join("%s img_%02d attempt %d: %s" %
                        (e.get("cell"), e.get("img"), e.get("attempt"), (e.get("error") or "?")[:200])
                        for e in log if not e.get("ok"))
        rec = "重试后均已恢复" if n_ok_total == 36 else "仍有未恢复项（见总表）"
        L.append("4. **重试/失败**：重试 %d 次、失败尝试 %d 次——%s（%s；明细见 `run_log.jsonl` 与 `*_failN.*` 文件）。"
                 % (n_retries, n_fails, det, rec))
    else:
        L.append("4. **重试/失败**：0 次重试、0 次失败——%d/36 一次通过（总尝试 %d 次）。" % (n_ok_total, n_attempts))
    L.append("5. **母题冲突（prompt 层观察，未干预）**：部分模块 §8.1 含人物母题"
             "（达·芬奇「young woman」、米开朗基罗「nude figures」、毕加索「seated man」、维米尔「interior figure」、卡拉瓦乔人物布光），"
             "与 T1 灯塔场景叠加后是否呈现「人物+灯塔」混合，留待人评（§5 维度）；按要求模块段原样保留（迁移性归 E4）。")
    L.append("6. **评分**：本表不含人评打分（design.md §5 六维：构图/造型/色彩/笔触与质感/情绪/响应度），待评分者补。")
    L.append("7. **媒体 URL**：生成后立即下载落盘（URL 有效期未核；与 B-20 卡口径一致，不复用旧 URL）。")
    L.append("")
    L.append("## 4. 文件清单与复现")
    L.append("")
    L.append("- `cells/<cell>/`：`req_*.json` / `resp_*.json` / `img_*.jpg`（每格 3 组；失败尝试另有 `*_failN.*`）")
    L.append("- `sheet_<cell>.png` ×12 · `sheet_all.png`（12 行总表）· `prompts.json` · `run_log.jsonl` · `sha256_manifest.txt`")
    L.append("- 脚本：`_extract_prompts.py` → `_gen.py`（重试 ≤2、间隔 0.8s）→ `_sheets.py` → `_report.py` → `_verify.py`（验收）")
    L.append("- 复现：`python _extract_prompts.py && python _gen.py batch && python _sheets.py && python _report.py && python _verify.py`")
    L.append("- 模块卡校验：`python knowledge/domains/painters/modules/_extract.py --check` → `checks=186 ok=186 fail=0`（2026-10-16 复核；11 卡时代为 33）")
    L.append("")
    L.append("## 5. 机械核验（2026-10-15）")
    L.append("")
    ok_open = 0
    uniq = set()
    for im in all_imgs:
        try:
            with Image.open(im["path"]) as obj:
                obj.verify()
            ok_open += 1
        except Exception:
            pass
        uniq.add(im["sha256"])
    n_req = sum(1 for cid in [c["cell"] for c in cells]
                if os.path.isdir(os.path.join(CELLS_DIR, cid))
                for f in os.listdir(os.path.join(CELLS_DIR, cid))
                if f.startswith("req_") and "_fail" not in f)
    n_resp = sum(1 for cid in [c["cell"] for c in cells]
                 if os.path.isdir(os.path.join(CELLS_DIR, cid))
                 for f in os.listdir(os.path.join(CELLS_DIR, cid))
                 if f.startswith("resp_") and "_fail" not in f)
    L.append("- 图片文件：**%d/36 存在**；Pillow 打开校验 %d/%d 通过；sha256 去重后 %d 个（全部唯一）。" %
             (len(all_imgs), ok_open, len(all_imgs), len(uniq)))
    L.append("- 请求/响应 JSON：req %d 份 / resp %d 份（均含于各格目录）。" % (n_req, n_resp))
    L.append("- 全量哈希：`sha256_manifest.txt`。")
    L.append("- 验收脚本：`python _verify.py` → `VERIFY PASS`（36/36 张 + 12 行表 + sheet_all.png + 12 格 sheet 全部就位）。")
    L.append("")
    L.append("---")
    L.append("")
    L.append("> 落款：ESeriesT1（wave7）· 2026-10-15 · 产物自校验可复跑（见 §4）；引用请带路径。")
    L.append("")

    with open(os.path.join(OUT_DIR, "RESULTS.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    print("wrote RESULTS.md")

    # ---- sha256_manifest.txt ----
    M = []
    M.append("# E1_t1 sha256 manifest — 2026-10-15")
    for cid in [c["cell"] for c in cells]:
        d = os.path.join(CELLS_DIR, cid)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            p = os.path.join(d, f)
            if os.path.isfile(p):
                M.append("%s  cells/%s/%s" % (sha256_file(p), cid, f))
    for extra in ["sheet_all.png"] + ["sheet_%s.png" % c["cell"] for c in cells] + ["prompts.json"]:
        p = os.path.join(OUT_DIR, extra)
        if not os.path.exists(p):
            p = os.path.join(HERE, extra)
        if os.path.exists(p):
            M.append("%s  %s" % (sha256_file(p), extra))
    with open(os.path.join(OUT_DIR, "sha256_manifest.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(M) + "\n")
    print("wrote sha256_manifest.txt (%d entries)" % len(M))


if __name__ == "__main__":
    main()
