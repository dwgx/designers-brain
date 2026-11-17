#!/usr/bin/env python3
"""Verifier for the 12 delivered motion MP4s (real full-decode, not isOpened).

For every declared card it:
  * opens media/MOTION-XX.mp4 and cap.read()s to EOF (counts decoded frames),
  * asserts EVERY decoded frame is exactly 1920x1080,
  * asserts fps==30 and duration==10s (300 frames / 30 fps),
  * asserts the file's sha256 matches the manifest entry (source(output) binding),
  * samples first/middle/last decoded frames and asserts they are not all identical
    (distinct-frame check, catches a single repeated frame padded to 300),
  * asserts the renderer source sha256 matches the manifest entry.

A manifest JSON (manifest.json in --dir) supplies expected sha256s. Exit 0 iff all
12 cards pass; nonzero on any failure. Prints a JSON report to stdout.

Usage: python verify_all.py --dir <motion_closure_dir> [--manifest <path>]
"""
import os as _os
_os.environ.setdefault("OPENCV_FFMPEG_LOGLEVEL", "-8")
import os
import hashlib
import json
import argparse
import cv2
import sys

W, H, FPS, FRAMES = 1920, 1080, 30.0, 300
IDS = ["02", "03", "04", "05", "06", "07", "09", "10", "12", "13", "14", "15"]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def frame_signature(frame):
    # cheap but content-bound signature of a decoded frame
    return hashlib.sha256(frame.tobytes()).hexdigest()


def verify_card(root, card, man):
    rec = {"card": card, "pass": False, "checks": {}}
    checks = rec["checks"]
    mp4 = os.path.join(root, "media", "MOTION-%s.mp4" % card)
    if not os.path.isfile(mp4):
        rec["error"] = "missing mp4"
        return rec
    actual_sha = sha256(mp4)
    checks["mp4_sha256_actual"] = actual_sha
    expected_sha = man["cards"][card]["output_sha256"]
    checks["mp4_sha256_expected"] = expected_sha
    checks["mp4_sha_match"] = actual_sha == expected_sha

    cap = cv2.VideoCapture(mp4)
    opened = bool(cap.isOpened())
    checks["cv2_opened"] = opened
    if not opened:
        cap.release()
        rec["error"] = "cannot open"
        return rec
    fps_hdr = cap.get(cv2.CAP_PROP_FPS)
    checks["fps_header"] = round(fps_hdr, 6)
    checks["fps_ok"] = abs(fps_hdr - FPS) < 0.01

    n = 0
    bad_dims = 0
    sample = {}
    targets = {0: "first", FRAMES // 2: "mid", FRAMES - 1: "last"}
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        h, w = frame.shape[:2]
        if (w, h) != (W, H):
            bad_dims += 1
        if n in targets:
            sample[targets[n]] = frame_signature(frame)
        n += 1
        if n > FRAMES + 50:  # safety bound; a valid card is exactly FRAMES
            break
    cap.release()
    checks["decoded_frames"] = n
    checks["decoded_frames_ok"] = n == FRAMES
    checks["bad_dimension_frames"] = bad_dims
    checks["all_frames_1920x1080"] = bad_dims == 0 and n == FRAMES
    checks["duration_sec"] = round(n / fps_hdr, 4) if fps_hdr else None
    checks["duration_ok"] = fps_hdr > 0 and abs(n / fps_hdr - 10.0) < 0.05

    sigs = [sample.get(k) for k in ("first", "mid", "last")]
    checks["sampled_signatures_present"] = all(s is not None for s in sigs)
    distinct = len(set(s for s in sigs if s is not None))
    checks["distinct_sample_count"] = distinct
    checks["distinct_frames_ok"] = checks["sampled_signatures_present"] and distinct >= 2

    # source renderer sha binding
    src = man["cards"][card].get("renderer_source_rel")
    if src:
        sp = os.path.join(root, src)
        checks["source_sha_actual"] = sha256(sp) if os.path.isfile(sp) else None
        checks["source_sha_expected"] = man["cards"][card].get("renderer_source_sha256")
        checks["source_sha_match"] = (checks["source_sha_actual"] ==
                                      checks["source_sha_expected"])

    bool_keys = ["mp4_sha_match", "cv2_opened", "fps_ok", "decoded_frames_ok",
                 "all_frames_1920x1080", "duration_ok", "distinct_frames_ok"]
    if src:
        bool_keys.append("source_sha_match")
    rec["pass"] = all(checks.get(k) is True for k in bool_keys)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="motion_closure directory")
    ap.add_argument("--manifest", default=None, help="path to manifest.json")
    args = ap.parse_args()
    root = os.path.abspath(args.dir)
    manifest_path = args.manifest or os.path.join(root, "manifest.json")
    with open(manifest_path, "r", encoding="utf-8") as fh:
        man = json.load(fh)
    results = [verify_card(root, c, man) for c in IDS]
    passed = sum(1 for r in results if r["pass"])
    report = {"dir": root, "manifest": os.path.abspath(manifest_path),
              "cards_passed": passed, "cards_total": len(IDS),
              "all_pass": passed == len(IDS), "results": results}
    print(json.dumps(report, indent=2))
    sys.exit(0 if report["all_pass"] else 1)


if __name__ == "__main__":
    main()
