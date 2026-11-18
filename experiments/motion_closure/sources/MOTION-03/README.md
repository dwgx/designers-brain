# MOTION-03

Fixed-angle isometric library; six books return to their shelves; visible three-sided books, bounded occlusion, actual CJK floor text and a continuous final pullback.

Source SHA-256: `8497f7d577c4d2c73791de8311f34893db62756d655c99a1bc17237790dce162`

MP4 SHA-256: `2a48c5564f950443a694413434b59cb4d957dca5e4e78fcaadb8f19dbfa1df34`

All delivered videos: H.264/avc1, yuv420p, 1920×1080, 30 fps, 300 frames, 10 seconds.

## Current generation

This renderer computes its final raster directly at 1920×1080. No lower-resolution render or pixel-replication wrapper is used. This describes raster resolution, not a claim of an original After Effects/Blender/native-authoring project.

From the package root, with Python + Pillow, Node.js for JS cards, FFmpeg/libx264 and the documented existing font:

```sh
python tools/render_native.py 03 --font /path/to/simhei.ttf --outdir /path/to/new-render-03
python tools/encode_frames.py --frames /path/to/new-render-03/frames --output /path/to/new-MOTION-03.mp4
```

The guarded entry requires the recorded font SHA. New encoded bytes may differ with encoder builds; they are a new experiment and cannot replace the published pinned MP4 without a reviewed release update.

[Normalized run receipt](../../evidence/MOTION-03/RUN.json) · [Font dependency](../../evidence/MOTION-03/font-dependency.json)
