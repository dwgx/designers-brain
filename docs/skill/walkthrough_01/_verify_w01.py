#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""walkthrough_01 · 机械验证（先机械后人工——评审前置）

检查（全部打印 PASS/FAIL + 计数）:
  1. 段逐字：每个 job 的 main_segment（归一化空白）是模块卡原文的子串；sha256 与 prompts.json 一致
  2. prompt 组装：prompt == theme + [fusion] + main_segment [+ axis_note]（逐字重组比对）
  3. 留档：req / resp / img 存在；req JSON 的 model/prompt/size 与记录一致；resp JSON 有 data[0].url
  4. 图片：JPEG 魔数；尺寸记录一致（实回 768×1152）；img sha256 与记录一致
  5. 产物清单：candidates ≥2 张真图 + 对比页；final 定稿图
用法: python _verify_w01.py
"""
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CARDS = os.path.join(REPO, "knowledge", "domains", "painters", "modules")

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print("  [%s] %s%s" % (tag, name, ("  " + detail) if detail else ""))


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def main():
    doc = json.load(open(os.path.join(HERE, "prompts.json"), encoding="utf-8"))
    jobs = doc["jobs"]
    print("== 1. 段逐字（main_segment ⊂ 卡原文；sha256 复核）==")
    for j in jobs:
        card = open(os.path.join(CARDS, j["main_card"] + ".md"), encoding="utf-8").read()
        check("%s segment-verbatim" % j["name"], norm(j["main_segment"]) in norm(card))
        check("%s segment-sha256" % j["name"],
              hashlib.sha256(j["main_segment"].encode("utf-8")).hexdigest() == j["main_segment_sha256"])

    print("== 2. prompt 组装（逐字重组比对）==")
    for j in jobs:
        parts = [j["theme"]]
        if j["fusion"]:
            parts.append(j["fusion"])
        parts.append(j["main_segment"])
        if j["axis_note"]:
            parts.append(j["axis_note"])
        rebuilt = " ".join(parts)
        check("%s prompt==rebuild" % j["name"], rebuilt == j["prompt"])
        check("%s prompt-sha256" % j["name"],
              sha_bytes(j["prompt"].encode("utf-8")) == j["prompt_sha256"])

    print("== 3. 留档（req/resp/img）==")
    for j in jobs:
        r = j.get("result") or {}
        check("%s has-result" % j["name"], bool(r.get("ok")))
        for key in ("img", "req", "resp"):
            p = os.path.join(HERE, r.get(key, ""))
            check("%s %s-exists" % (j["name"], key), os.path.exists(p), r.get(key, ""))
        req = json.load(open(os.path.join(HERE, r["req"]), encoding="utf-8"))
        check("%s req.prompt==job.prompt" % j["name"], req.get("prompt") == j["prompt"])
        check("%s req.model==bare-name" % j["name"], req.get("model") == "grok-imagine-image-2.0")
        check("%s req.size" % j["name"], req.get("size") == "1024x1536")
        resp = json.load(open(os.path.join(HERE, r["resp"]), encoding="utf-8"))
        check("%s resp.url" % j["name"], bool(resp.get("data", [{}])[0].get("url")))

    print("== 4. 图片（魔数/尺寸/sha256）==")
    for j in jobs:
        r = j["result"]
        b = open(os.path.join(HERE, r["img"]), "rb").read()
        check("%s jpeg-magic" % j["name"], b[:2] == b"\xff\xd8")
        check("%s img-sha256" % j["name"], sha_bytes(b) == r["img_sha256"])
        check("%s dims=768x1152" % j["name"], (r["w"], r["h"]) == (768, 1152), "%sx%s" % (r["w"], r["h"]))

    print("== 5. 产物清单 ==")
    cands = [j for j in jobs if j["role"] == "candidate"]
    check("candidates>=2", len(cands) >= 2, "%d" % len(cands))
    check("compare-page", os.path.exists(os.path.join(HERE, "candidates", "compare_candidates.png")))
    finals = [j for j in jobs if j["role"] == "final"]
    check("final==1", len(finals) == 1)
    for f in finals:
        check("final img exists", os.path.exists(os.path.join(HERE, f["result"]["img"])))

    print("\nRESULT: checks=%d ok=%d fail=%d" % (PASS + FAIL, PASS, FAIL))
    sys.exit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
