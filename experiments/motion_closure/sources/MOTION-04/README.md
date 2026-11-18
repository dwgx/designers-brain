# MOTION-04

Synthwave midnight-radio title: striped sun, perspective grid, chrome CJK lettering, restrained scanlines and RGB separation.

Source SHA-256: `53670d3ac6fde7ca9fc22488ce39b78eb5d65f87d7e9bc36865f5026d04042a8`

MP4 SHA-256: `7c2cb752f390629abf32ffdcfdeb133a7134473c75f4486c9bcd9f6844195d80`

All delivered videos: H.264/avc1, yuv420p, 1920×1080, 30 fps, 300 frames, 10 seconds.

## Current generation

This renderer computes its final raster directly at 1920×1080. No lower-resolution render or pixel-replication wrapper is used. This describes raster resolution, not a claim of an original After Effects/Blender/native-authoring project.

From the package root, with Python + Pillow, Node.js for JS cards, FFmpeg/libx264 and the documented existing font:

```sh
python tools/render_native.py 04 --font /path/to/simhei.ttf --outdir /path/to/new-render-04
python tools/encode_frames.py --frames /path/to/new-render-04/frames --output /path/to/new-MOTION-04.mp4
```

The guarded entry requires the recorded font SHA. New encoded bytes may differ with encoder builds; they are a new experiment and cannot replace the published pinned MP4 without a reviewed release update.

[Normalized run receipt](../../evidence/MOTION-04/RUN.json) · [Font dependency](../../evidence/MOTION-04/font-dependency.json)
