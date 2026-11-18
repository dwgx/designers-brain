# MOTION-07

Science-fiction HUD linework: deterministic five-frame ticks and a whole-state cyan-to-orange change.

Source SHA-256: `8addb10cf26c18d0b4959b51c5bc1a96cbe614415d5f4b3feef8d4e2beb6f5f1`

MP4 SHA-256: `ef955281b1a5ef82c3cf97b6cfc74476552ac707038c03ed8b6f8c7b2d1b7e42`

All delivered videos: H.264/avc1, yuv420p, 1920×1080, 30 fps, 300 frames, 10 seconds.

## Current generation

This renderer computes its final raster directly at 1920×1080. No lower-resolution render or pixel-replication wrapper is used. This describes raster resolution, not a claim of an original After Effects/Blender/native-authoring project.

From the package root, with Python + Pillow, Node.js for JS cards, FFmpeg/libx264 and the documented existing font:

```sh
python tools/render_native.py 07 --font /path/to/simhei.ttf --outdir /path/to/new-render-07
python tools/encode_frames.py --frames /path/to/new-render-07/frames --output /path/to/new-MOTION-07.mp4
```

The guarded entry requires the recorded font SHA. New encoded bytes may differ with encoder builds; they are a new experiment and cannot replace the published pinned MP4 without a reviewed release update.

[Normalized run receipt](../../evidence/MOTION-07/RUN.json) · [Font dependency](../../evidence/MOTION-07/font-dependency.json)
