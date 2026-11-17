#!/usr/bin/env python3
"""Encode a card's 300 rendered PNG frames to 1920x1080/30fps MP4 (mp4v).

Usage:
  python encode_frames.py <frames_dir> <out.mp4> [expected_frames]

Reads frames f0000.png .. f0299.png in order. Uses cv2.VideoWriter with mp4v
(ffmpeg is not on PATH in this environment). Verifies every frame was written by
decoding the output to EOF and reporting counts. Prints JSON to stdout.
"""
import os
import sys
import json
import cv2

W, H, FPS = 1920, 1080, 30


def main():
    frames_dir, out_mp4 = sys.argv[1], sys.argv[2]
    expected = int(sys.argv[3]) if len(sys.argv) > 3 else 300
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    vw = cv2.VideoWriter(out_mp4, fourcc, FPS, (W, H))
    if not vw.isOpened():
        print(json.dumps({"error": "VideoWriter failed to open", "out": out_mp4}))
        sys.exit(2)
    written = 0
    bad = []
    for n in range(expected):
        p = os.path.join(frames_dir, "f%04d.png" % n)
        img = cv2.imread(p)
        if img is None or img.shape[:2] != (H, W):
            bad.append({"n": n, "path": p, "shape": None if img is None else list(img.shape)})
            continue
        vw.write(img)
        written += 1
    vw.release()
    # decode-back verification
    cap = cv2.VideoCapture(out_mp4)
    decoded = 0
    dims = set()
    while True:
        ok, fr = cap.read()
        if not ok:
            break
        decoded += 1
        dims.add((fr.shape[1], fr.shape[0]))
    cap.release()
    print(json.dumps({
        "out": os.path.basename(out_mp4), "codec": "mp4v", "fourcc": "mp4v",
        "fps": FPS, "target_resolution": [W, H], "expected_frames": expected,
        "written": written, "bad_frames": bad[:5], "bad_frame_count": len(bad),
        "decoded_frames": decoded, "decoded_dimensions": sorted([list(d) for d in dims]),
        "size_bytes": os.path.getsize(out_mp4),
    }, indent=2))


if __name__ == "__main__":
    main()
