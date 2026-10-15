#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E1_t1c · 机械产物：sha256_manifest_t1c.txt + stats_t1c.json（RESULTS_t1c.md 的机械部分）
读取: prompts_t1c.json + run_log.jsonl + cells/**（以落盘文件为准重算哈希与尺寸）
"""
import hashlib
import json
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
CELLS_DIR = os.environ.get("E1C_CELLS_DIR") or os.path.join(HERE, "cells")
OUT_DIR = os.environ.get("E1C_OUT_DIR") or HERE
LOG_PATH = os.environ.get("E1C_LOG_PATH") or os.path.join(HERE, "run_log.jsonl")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_log():
    entries = []
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    entries.append(json.loads(line))
    return entries


def main():
    with open(os.path.join(HERE, "prompts_t1c.json"), encoding="utf-8") as fh:
        cells = json.load(fh)["cells"]
    log = load_log()

    stats = {"date": "2026-10-15", "n_cells": len(cells), "cells": []}
    for c in cells:
        cid = c["cell"]
        imgs = []
        for i in (1, 2, 3):
            p = os.path.join(CELLS_DIR, cid, "img_%02d.jpg" % i)
            if os.path.exists(p):
                with Image.open(p) as im:
                    w, h = im.size
                imgs.append({"n": i, "sha256": sha256_file(p), "bytes": os.path.getsize(p),
                             "w": w, "h": h})
            else:
                imgs.append({"n": i, "sha256": None})
        entries = [e for e in log if e.get("cell") == cid]
        attempts = len(entries)
        retries = sum(1 for e in entries if e.get("attempt", 1) > 1)
        fails = sum(1 for e in entries if not e.get("ok"))
        total_s = sum(e.get("total_s", 0.0) for e in entries)
        n_ok = sum(1 for im in imgs if im["sha256"])
        dims = sorted({(im["w"], im["h"]) for im in imgs if im["sha256"]})
        stats["cells"].append({
            "cell": cid, "module": c["module"], "module_name": c["module_name"],
            "imgs": imgs, "n_ok": n_ok, "attempts": attempts, "retries": retries,
            "fails": fails, "total_s": round(total_s, 1), "dims": dims,
            "s81b_sha256": c["s81b_sha256"],
            "v1_sha256_audit": "3326164fb5666fb9cd5dc896ea3cd267c4c95f9f568e2d96c8909cbc0ee24c2c",
        })

    with open(os.path.join(OUT_DIR, "stats_t1c.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(stats, fh, ensure_ascii=False, indent=2)
    print("wrote stats_t1c.json")
    for s in stats["cells"]:
        shas = " / ".join((im["sha256"][:8] if im["sha256"] else "MISSING") for im in s["imgs"])
        print("  %-20s ok=%d/3 attempts=%d fails=%d %.1fs dims=%s\n      sha: %s" %
              (s["cell"], s["n_ok"], s["attempts"], s["fails"], s["total_s"], s["dims"], shas))

    # ---- sha256_manifest_t1c.txt ----
    M = ["# E1_t1c sha256 manifest — 2026-10-15"]
    for c in cells:
        cid = c["cell"]
        d = os.path.join(CELLS_DIR, cid)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            p = os.path.join(d, f)
            if os.path.isfile(p):
                M.append("%s  cells/%s/%s" % (sha256_file(p), cid, f))
    extras = ["sheet_e1_michelangelo_v2.png", "compare_michelangelo_v2.png",
              "prompts_t1c.json", "s81b_v1_snapshot.md", "s81b_v2_derivation.json"]
    for extra in extras:
        p = os.path.join(OUT_DIR, extra)
        if os.path.exists(p):
            M.append("%s  %s" % (sha256_file(p), extra))
    card = os.path.normpath(os.path.join(HERE, "..", "..", "prompts", "artist_modules", "michelangelo.md"))
    if os.path.exists(card):
        M.append("%s  research/prompts/artist_modules/michelangelo.md" % sha256_file(card))
    insp = os.path.join(OUT_DIR, "_inspect")
    if os.path.isdir(insp):
        for f in sorted(os.listdir(insp)):
            p = os.path.join(insp, f)
            if os.path.isfile(p):
                M.append("%s  _inspect/%s" % (sha256_file(p), f))
    with open(os.path.join(OUT_DIR, "sha256_manifest_t1c.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(M) + "\n")
    print("wrote sha256_manifest_t1c.txt (%d entries)" % len(M))


if __name__ == "__main__":
    main()
