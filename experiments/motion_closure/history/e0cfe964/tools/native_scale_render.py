#!/usr/bin/env python3
"""Native-resolution geometry scaler for the low-resolution Python motion cards.

HONESTY / PURPOSE
-----------------
The shipped sources/MOTION-XX/render.py files are the FROZEN originals. Their pure
render_frame(n, seed) is imported and called UNCHANGED. This wrapper applies one
deterministic integer geometric scale S to the produced PIL image:

    x -> x*S , y -> y*S , every 1px stroke -> an S x S block (NEAREST neighbour).

S is exact: 960x540 * 2 = 1920x1080. No resampling filters, no new colours, no
interpolation, no frame duplication, no wall clock, no RNG. Seed, schedule and
drawing method are the original's, so temporal behaviour is identical to the
frozen card. This is a RASTER render with uniformly SCALED GEOMETRY — NOT a
browser/WebGL/Blender native re-author; it adds no finer native detail than the
logical grid. See each card's NOTES.md.

CLI
  python native_scale_render.py <render.py> <outdir> full
  python native_scale_render.py <render.py> <outdir> batch <n,n,..>
"""
import sys
sys.dont_write_bytecode = True
import os
import json
import hashlib
import importlib.util
from pathlib import Path

from PIL import Image

TARGET_W, TARGET_H, FRAMES, FPS = 1920, 1080, 300, 30


def load_renderer(path):
    spec = importlib.util.spec_from_file_location("frozen_render", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def render_one(R, n, out_dir, S):
    img = R.render_frame(n, R.SEED)          # FROZEN pure function, unchanged
    assert img.size == (R.W, R.H), (img.size, (R.W, R.H))
    native = img.resize((TARGET_W, TARGET_H), Image.Resampling.NEAREST)
    assert native.size == (TARGET_W, TARGET_H)
    name = "f%04d.png" % n
    p = Path(out_dir) / "frames" / name
    native.save(p, format="PNG", compress_level=6, optimize=False)
    return sha(p)


def main():
    renderer, out_dir, mode = sys.argv[1], sys.argv[2], sys.argv[3]
    R = load_renderer(renderer)
    S = TARGET_W // R.W
    assert R.W * S == TARGET_W and R.H * S == TARGET_H, (R.W, R.H, S)
    frames_dir = Path(out_dir) / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)

    if mode == "full":
        hashes = {}
        for n in range(FRAMES):
            hashes["%04d" % n] = render_one(R, n, out_dir, S)
        (frames_dir / "frame_hashes.json").write_text(json.dumps({
            "seed": R.SEED, "fps": FPS, "frames": FRAMES,
            "resolution": [TARGET_W, TARGET_H],
            "source_resolution": [R.W, R.H], "geometry_scale": S,
            "renderer": "frozen-original-render_frame + integer-geometry-scale@1.0.0",
            "hashes": hashes,
        }, indent=1, sort_keys=True), encoding="utf-8")
        print(json.dumps({"mode": "full", "frames": FRAMES,
                          "resolution": [TARGET_W, TARGET_H], "scale": S, "ok": True}))
    elif mode == "batch":
        out = {}
        for tok in sys.argv[4].split(","):
            n = int(tok)
            out[n] = render_one(R, n, out_dir, S)
        print(json.dumps({"mode": "batch", "scale": S, "hashes": out}))
    else:
        print("usage: native_scale_render.py <render.py> <outdir> full|batch [n,n,..]",
              file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
