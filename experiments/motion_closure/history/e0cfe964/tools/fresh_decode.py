#!/usr/bin/env python3
"""Fresh full-decode auditor for candidate motion MP4s.

Reads every frame with cap.read() to EOF. Records declared header frame_count
separately from actual decoded count, per-frame dimensions (unique set), fps,
duration, size, and sha256 of the file bytes. Prints JSON to stdout.

Usage:
    python fresh_decode.py <file> [<file> ...]
"""
import os
import sys
import json
import hashlib
import cv2


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def measure(path):
    rec = {"file": os.path.basename(path), "present": os.path.isfile(path)}
    if not rec["present"]:
        return rec
    rec["size_bytes"] = os.path.getsize(path)
    rec["sha256"] = sha256(path)
    cap = cv2.VideoCapture(path)
    opened = cap.isOpened()
    rec["cv2_opened"] = bool(opened)
    if not opened:
        return rec
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames_hdr = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    w_hdr = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h_hdr = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    rec["fps_header"] = round(fps, 6) if fps else fps
    rec["frame_count_header"] = int(frames_hdr) if frames_hdr else int(frames_hdr)
    rec["resolution_header"] = [int(w_hdr), int(h_hdr)]

    n = 0
    dims = set()
    bad_dims = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        n += 1
        hh, ww = frame.shape[:2]
        dims.add((ww, hh))
        if n > 100000:
            break
    cap.release()
    rec["decoded_frames"] = n
    rec["decoded_dimensions_set"] = sorted([list(d) for d in dims])
    rec["unique_dimension_count"] = len(dims)
    rec["bad_dim_frames"] = bad_dims
    if fps:
        rec["duration_sec"] = round(n / fps, 4)
    return rec


def main():
    recs = [measure(p) for p in sys.argv[1:]]
    print(json.dumps(recs, indent=2))


if __name__ == "__main__":
    main()
