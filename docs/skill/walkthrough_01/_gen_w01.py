#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""walkthrough_01 · 图像生成脚本（直连网关 /v1/images/generations，模型 grok-imagine-image-2.0）

复刻 experiments/E2_t1/_gen_e2.py 的调用方式（post_json / download / 重试 / 留档），
输入改为本目录 prompts.json 的 jobs[]，产物与结果回填 prompts.json。

用法:
  python _gen_w01.py                 # 生成 prompts.json 中全部无结果的 job
  python _gen_w01.py --only cand1_monet_dawn
  python _gen_w01.py --force         # 忽略已有图片，重出

落盘（每 job）: <out>/<name>.jpg + <name>.req.json + <name>.resp.json
  失败尝试另存 <name>.req_failN.json / <name>.resp_failN.json
  重试 ≤2（单张总尝试 ≤3）；单 job 失败不阻塞其它 job。
日志: run_log.jsonl，每行一次尝试，不含任何密钥。
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
PROMPTS = os.path.join(HERE, "prompts.json")
LOG = os.path.join(HERE, "run_log.jsonl")

ENDPOINT = "http://192.168.11.4:3000/v1/images/generations"
MODEL = "grok-imagine-image-2.0"
SIZE = "1024x1536"
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


def log_line(entry):
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")


def gen_one(key, job, force=False):
    """生成单 job（含重试）。返回 result dict 或 None。"""
    out_dir = os.path.join(HERE, job["out"])
    os.makedirs(out_dir, exist_ok=True)
    name = job["name"]
    img_path = os.path.join(out_dir, name + ".jpg")
    if (not force) and os.path.exists(img_path) and os.path.getsize(img_path) > 1000:
        print("  [skip] %s already exists" % name, flush=True)
        return None

    body_str = json.dumps({"model": MODEL, "prompt": job["prompt"], "n": 1, "size": SIZE},
                          ensure_ascii=False)
    attempts = []
    for attempt in range(1, MAX_RETRIES + 2):
        t0 = time.time()
        entry = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "job": name,
                 "attempt": attempt, "ok": False, "t0": t0}
        status, resp_bytes, api_s = post_json(body_str, key)
        entry["status"] = status
        entry["api_s"] = round(api_s, 2)
        err = None
        url = None
        img_bytes = None
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
        entry["total_s"] = round(time.time() - t0, 2)

        if err:
            entry["error"] = err
            attempts.append((attempt, False, body_str, resp_bytes, None))
            log_line(entry)
            print("  [%s] attempt %d FAILED: %s" % (name, attempt, err[:140]), flush=True)
            if attempt <= MAX_RETRIES:
                time.sleep(3.0)
            continue

        w, h, fmt = img_dims(img_bytes)
        entry["ok"] = True
        entry["url"] = url
        entry["bytes"] = len(img_bytes)
        entry["sha256"] = hashlib.sha256(img_bytes).hexdigest()
        entry["w"], entry["h"], entry["format"] = w, h, fmt
        attempts.append((attempt, True, body_str, resp_bytes, img_bytes))
        log_line(entry)
        print("  [%s] ok (%.1fs, %sx%s, %dB)" % (name, entry["total_s"], w, h, len(img_bytes)), flush=True)
        break

    ok_attempt = None
    for attempt, ok, _b, _r, _i in attempts:
        if ok:
            ok_attempt = attempt
    result = {"ok": ok_attempt is not None}
    for attempt, ok, body_str2, resp_bytes2, img_bytes2 in attempts:
        if ok and attempt == ok_attempt:
            with open(os.path.join(out_dir, name + ".req.json"), "w", encoding="utf-8") as fh:
                fh.write(body_str2)
            with open(os.path.join(out_dir, name + ".resp.json"), "wb") as fh:
                fh.write(resp_bytes2)
            with open(img_path, "wb") as fh:
                fh.write(img_bytes2)
            w, h, fmt = img_dims(img_bytes2)
            result.update({
                "attempt": attempt,
                "url": entry.get("url"),
                "img": "%s/%s.jpg" % (job["out"], name),
                "req": "%s/%s.req.json" % (job["out"], name),
                "resp": "%s/%s.resp.json" % (job["out"], name),
                "bytes": len(img_bytes2),
                "img_sha256": hashlib.sha256(img_bytes2).hexdigest(),
                "w": w, "h": h, "format": fmt,
            })
        else:
            with open(os.path.join(out_dir, "%s.req_fail%d.json" % (name, attempt)), "w", encoding="utf-8") as fh:
                fh.write(body_str2)
            with open(os.path.join(out_dir, "%s.resp_fail%d.json" % (name, attempt)), "wb") as fh:
                fh.write(resp_bytes2)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    doc = json.load(open(PROMPTS, encoding="utf-8"))
    key = load_key()
    t_start = time.time()
    n_ok = n_fail = n_skip = 0
    changed = False
    for job in doc["jobs"]:
        if args.only and job["name"] != args.only:
            continue
        print("=== %s (%s) ===" % (job["name"], job["direction"]), flush=True)
        res = gen_one(key, job, force=args.force)
        if res is None:
            n_skip += 1
            continue
        job["result"] = res
        changed = True
        if res["ok"]:
            n_ok += 1
        else:
            n_fail += 1
        time.sleep(SLEEP_BETWEEN)
    if changed:
        with open(PROMPTS, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
    print("=== DONE: %d ok / %d fail / %d skip in %.0fs ===" % (n_ok, n_fail, n_skip, time.time() - t_start), flush=True)
    sys.exit(0 if n_fail == 0 else 1)


if __name__ == "__main__":
    main()
