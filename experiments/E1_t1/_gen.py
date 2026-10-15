#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E1_t1 · 批量生成脚本（网关直连 /v1/images/generations，模型 grok-imagine-image-2.0）

用法:
  python _gen.py pilot            # 管线试跑 2 张（e0_baseline + e1_van_gogh）→ _pilot/
  python _gen.py batch            # 12 格 × 3 张 = 36 张 → cells/<cell>/
  python _gen.py batch --only e1_da_vinci,e1_monet
  python _gen.py batch --force    # 忽略已有图片，全部重出

落盘（每格）: req_01.json / resp_01.json / img_01.jpg（01..03）
  失败尝试另存 req_XX_failN.json / resp_XX_failN.json
  重试 ≤2（单张总尝试 ≤3）；单格失败不阻塞其它格。
日志: run_log.jsonl（pilot 为 _pilot/pilot_log.jsonl），每行一次尝试，不含任何密钥。
"""
import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CELLS_DIR = os.path.join(HERE, "cells")
PILOT_DIR = os.path.join(HERE, "_pilot")

ENDPOINT = "http://192.168.11.4:3000/v1/images/generations"
MODEL = "grok-imagine-image-2.0"
SIZE = "1024x1536"
N_PER_CELL = 3
MAX_RETRIES = 2          # 重试次数上限（总尝试 = 1 + MAX_RETRIES）
SLEEP_BETWEEN = 0.8      # 请求间隔（秒）
TIMEOUT_API = 180
TIMEOUT_DL = 120

_OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def load_key():
    key = (os.environ.get("BUDDYFARM_API_KEY") or "").strip()
    if key:
        return key
    env_path = r"C:\Users\dwgx1\.omp\agent\.env"
    with open(env_path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line.startswith("BUDDYFARM_API_KEY="):
                return line.split("=", 1)[1].strip()
    raise SystemExit("FATAL: BUDDYFARM_API_KEY not found")


def post_json(body_str, key):
    req = urllib.request.Request(
        ENDPOINT, data=body_str.encode("utf-8"),
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
        method="POST")
    t0 = time.time()
    try:
        with _OPENER.open(req, timeout=TIMEOUT_API) as resp:
            return resp.status, resp.read(), time.time() - t0
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read(), time.time() - t0


def download(url):
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
    t0 = time.time()
    try:
        with _OPENER.open(req, timeout=TIMEOUT_DL) as resp:
            return resp.status, resp.read(), time.time() - t0
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read(), time.time() - t0


def img_dims(data):
    try:
        from PIL import Image
        import io
        im = Image.open(io.BytesIO(data))
        return im.size[0], im.size[1], im.format
    except Exception:
        return None, None, None


def log_line(log_path, entry):
    with open(log_path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")


def gen_one(key, cell, idx, prompt, out_dir, log_path, force=False):
    """生成单张（含重试）。返回 True/False。"""
    nn = "%02d" % idx
    img_path = os.path.join(out_dir, "img_%s.jpg" % nn)
    if (not force) and os.path.exists(img_path) and os.path.getsize(img_path) > 1000:
        print("  [skip] %s img_%s.jpg already exists" % (cell, nn), flush=True)
        return True

    body_str = json.dumps({"model": MODEL, "prompt": prompt, "n": 1, "size": SIZE},
                          ensure_ascii=False)
    attempts = []
    for attempt in range(1, MAX_RETRIES + 2):
        t0 = time.time()
        entry = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "cell": cell, "img": idx,
                 "attempt": attempt, "ok": False, "t0": t0}
        status, resp_bytes, api_s = post_json(body_str, key)
        entry["status"] = status
        entry["api_s"] = round(api_s, 2)
        err = None
        url = None
        img_bytes = None
        dl_s = 0.0
        if status != 200:
            err = "http %s: %s" % (status, resp_bytes[:200].decode("utf-8", "replace"))
        else:
            try:
                data = json.loads(resp_bytes.decode("utf-8"))
                url = data["data"][0]["url"]
            except Exception as exc:
                err = "bad response json: %s" % exc
        if err is None and url:
            st2, img_bytes, dl_s = download(url)
            entry["dl_s"] = round(dl_s, 2)
            if st2 != 200:
                err = "download http %s" % st2
            elif not img_bytes or img_bytes[:2] != b"\xff\xd8":
                err = "downloaded bytes not jpeg (magic=%s)" % (img_bytes[:4].hex() if img_bytes else "empty")
        entry["t1"] = time.time()
        entry["total_s"] = round(entry["t1"] - t0, 2)

        if err:
            entry["error"] = err
            attempts.append((attempt, False, body_str, resp_bytes, None))
            log_line(log_path, entry)
            print("  [%s img_%s] attempt %d FAILED: %s" % (cell, nn, attempt, err[:140]), flush=True)
            if attempt <= MAX_RETRIES:
                time.sleep(3.0)
            continue

        # success
        w, h, fmt = img_dims(img_bytes)
        entry["ok"] = True
        entry["url"] = url
        entry["bytes"] = len(img_bytes)
        entry["sha256"] = hashlib.sha256(img_bytes).hexdigest()
        entry["w"], entry["h"], entry["format"] = w, h, fmt
        attempts.append((attempt, True, body_str, resp_bytes, img_bytes))
        log_line(log_path, entry)
        print("  [%s img_%s] ok (%.1fs, %sx%s, %dB)" % (cell, nn, entry["total_s"], w, h, len(img_bytes)), flush=True)
        break

    # 落盘：失败尝试 → fail 文件；最终成功 → 标准文件
    ok_attempt = None
    for attempt, ok, _b, _r, _i in attempts:
        if ok:
            ok_attempt = attempt
    for attempt, ok, body_str2, resp_bytes2, img_bytes2 in attempts:
        if ok and attempt == ok_attempt:
            with open(os.path.join(out_dir, "req_%s.json" % nn), "w", encoding="utf-8") as fh:
                fh.write(body_str2)
            with open(os.path.join(out_dir, "resp_%s.json" % nn), "wb") as fh:
                fh.write(resp_bytes2)
            with open(img_path, "wb") as fh:
                fh.write(img_bytes2)
        else:
            with open(os.path.join(out_dir, "req_%s_fail%d.json" % (nn, attempt)), "w", encoding="utf-8") as fh:
                fh.write(body_str2)
            with open(os.path.join(out_dir, "resp_%s_fail%d.json" % (nn, attempt)), "wb") as fh:
                fh.write(resp_bytes2)

    return ok_attempt is not None


def run_cells(key, cells, out_root, log_path, force=False):
    t_start = time.time()
    total_ok = 0
    total_fail = 0
    for cell in cells:
        out_dir = os.path.join(out_root, cell["cell"])
        os.makedirs(out_dir, exist_ok=True)
        print("=== %s (%s) ===" % (cell["cell"], cell.get("module_name") or "baseline"), flush=True)
        for idx in range(1, N_PER_CELL + 1):
            ok = gen_one(key, cell["cell"], idx, cell["prompt"], out_dir, log_path, force=force)
            if ok:
                total_ok += 1
            else:
                total_fail += 1
            time.sleep(SLEEP_BETWEEN)
    wall = time.time() - t_start
    print("=== DONE: %d ok / %d fail in %.0fs ===" % (total_ok, total_fail, wall), flush=True)
    return total_fail == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["pilot", "batch"])
    ap.add_argument("--only", default="")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    with open(os.path.join(HERE, "prompts.json"), encoding="utf-8") as fh:
        doc = json.load(fh)
    all_cells = doc["cells"]
    by_id = {c["cell"]: c for c in all_cells}

    key = load_key()

    if args.mode == "pilot":
        os.makedirs(PILOT_DIR, exist_ok=True)
        cells = [by_id["e0_baseline"], by_id["e1_van_gogh"]]
        log_path = os.path.join(PILOT_DIR, "pilot_log.jsonl")
        ok = run_cells(key, cells, PILOT_DIR, log_path, force=args.force)
        sys.exit(0 if ok else 1)

    # batch
    cells = all_cells
    if args.only:
        wanted = [s.strip() for s in args.only.split(",") if s.strip()]
        cells = [by_id[w] for w in wanted]
    os.makedirs(CELLS_DIR, exist_ok=True)
    log_path = os.path.join(HERE, "run_log.jsonl")
    ok = run_cells(key, cells, CELLS_DIR, log_path, force=args.force)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
