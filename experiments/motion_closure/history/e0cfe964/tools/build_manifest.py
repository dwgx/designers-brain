#!/usr/bin/env python3
"""Build manifest.json for the 12 delivered motion MP4s from ACTUAL bytes.

Collects: output sha256/size, full-decode decoded frame count + per-frame dims,
fps/duration, distinct first/mid/last signature, renderer source sha256. Original
author/staging provenance hashes are supplied separately in provenance.json and
copied here under 'original' (kept distinct from new 'output' hashes).

Usage: python build_manifest.py <motion_closure_dir> <provenance.json> <out.json>
"""
import os
import sys
import json
import hashlib
import cv2

W, H, FPS, FRAMES = 1920, 1080, 30.0, 300
IDS = ["02", "03", "04", "05", "06", "07", "09", "10", "12", "13", "14", "15"]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def sig(frame):
    return hashlib.sha256(frame.tobytes()).hexdigest()


def measure(mp4):
    cap = cv2.VideoCapture(mp4)
    fps = cap.get(cv2.CAP_PROP_FPS)
    n = 0; dims = set(); samp = {}
    while True:
        ok, fr = cap.read()
        if not ok:
            break
        dims.add((fr.shape[1], fr.shape[0]))
        if n == 0: samp["first"] = sig(fr)
        if n == FRAMES // 2: samp["mid"] = sig(fr)
        if n == FRAMES - 1: samp["last"] = sig(fr)
        n += 1
    cap.release()
    return {"decoded_frames": n, "fps": round(fps, 6),
            "duration_sec": round(n / fps, 4) if fps else None,
            "dimensions_set": sorted([list(x) for x in dims]),
            "distinct_sample_count": len(set(samp.values()))}


def main():
    root, prov_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(prov_path, "r", encoding="utf-8") as fh:
        prov = json.load(fh)
    cards = {}
    for c in IDS:
        c = str(c)
        mp4 = os.path.join(root, "media", "MOTION-%s.mp4" % c)
        info = prov["cards"][c]
        renderer_rel = info["renderer_source_rel"]
        rec = {
            "id": c,
            "origin": info["origin"],
            "slug": info["slug"],
            "mechanism": info["mechanism"],
            "media_rel": "media/MOTION-%s.mp4" % c,
            "output_sha256": sha256(mp4),
            "size_bytes": os.path.getsize(mp4),
            "renderer_source_rel": renderer_rel,
            "renderer_source_sha256": sha256(os.path.join(root, renderer_rel)),
            "original": info["original"],
            "measured": measure(mp4),
            "params": info["params"],
            "notes": info["notes"],
            "platform": info["platform"],
        }
        cards[c] = rec
    man = {"schema": "motion-closure-manifest@1.0.0",
           "spec": {"resolution": [W, H], "fps": FPS, "frames": FRAMES,
                    "duration_sec": 10.0, "codec": "mp4v"},
           "cards": cards}
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(man, fh, indent=2, ensure_ascii=False)
    print(json.dumps({"cards": len(cards), "out": out_path,
                      "all_300": all(cards[c]["measured"]["decoded_frames"] == FRAMES
                                     for c in cards), "ok": True}))


if __name__ == "__main__":
    main()
