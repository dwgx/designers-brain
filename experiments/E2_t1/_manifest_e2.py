#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E2_t1 · 统计与哈希清单（生成后运行）：
  stats_e2.json          —— 每格 3 张的 sha/字节/尺寸 + 尝试/重试/耗时 + prompt sha
  sha256_manifest_e2.txt —— 本目录全部产物（cells/** + 顶层文件）逐文件 sha256
"""
import glob
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CELLS_DIR = os.path.join(HERE, "cells")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    with open(os.path.join(HERE, "prompts_e2.json"), encoding="utf-8") as fh:
        doc = json.load(fh)
    cells = doc["cells"]

    log = []
    lp = os.path.join(HERE, "run_log.jsonl")
    if os.path.exists(lp):
        for line in open(lp, encoding="utf-8"):
            line = line.strip()
            if line:
                log.append(json.loads(line))

    stats = {"date": "2026-10-15", "n_cells": len(cells), "cells": []}
    for c in cells:
        cid = c["cell"]
        entry = {
            "cell": cid, "title": c["title"],
            "main": c["main"]["id"], "aux": c["aux"]["id"],
            "prompt_sha256": c["prompt_sha256"],
            "imgs": [], "n_ok": 0, "attempts": 0, "retries": 0, "fails": 0, "total_s": 0.0,
        }
        for i in (1, 2, 3):
            p = os.path.join(CELLS_DIR, cid, "img_%02d.jpg" % i)
            if os.path.exists(p):
                from PIL import Image
                with Image.open(p) as im:
                    w, h = im.size
                entry["imgs"].append({"n": i, "sha256": sha256_file(p),
                                      "bytes": os.path.getsize(p), "w": w, "h": h})
                entry["n_ok"] += 1
        tries = [e for e in log if e.get("cell") == cid]
        entry["attempts"] = len(tries)
        entry["fails"] = len([e for e in tries if not e.get("ok")])
        entry["retries"] = max(0, len(tries) - 3)
        entry["total_s"] = round(sum(e.get("total_s", 0.0) for e in tries), 1)
        stats["cells"].append(entry)

    with open(os.path.join(HERE, "stats_e2.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(stats, fh, ensure_ascii=False, indent=2)
    print("wrote stats_e2.json")

    files = []
    for root, _dirs, names in os.walk(HERE):
        for n in names:
            p = os.path.join(root, n)
            rel = os.path.relpath(p, HERE).replace("\\", "/")
            if rel.startswith("_pilot"):
                continue
            files.append(rel)
    files.sort()
    with open(os.path.join(HERE, "sha256_manifest_e2.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# E2_t1 sha256 manifest — 2026-10-15\n")
        for rel in files:
            fh.write("%s  %s\n" % (sha256_file(os.path.join(HERE, rel)), rel))
    print("wrote sha256_manifest_e2.txt (%d files)" % len(files))


if __name__ == "__main__":
    main()
