# MOTION-14

Water-distribution editorial animation using rounded USGS categories; continuous float camera with final pixel cropping.

Source SHA-256: `9fe0628daaf02250b5f22b984101bde9a022dea1f39a675f87b6e7efb61e169d`

MP4 SHA-256: `763bd4a5d7e1cf986bf8d0d337ddb3f8e5e366a5d9bb9640e3dbb94ed52452a3`

All delivered videos: H.264/avc1, yuv420p, 1920×1080, 30 fps, 300 frames, 10 seconds.

## Current generation

This renderer computes its final raster directly at 1920×1080. No lower-resolution render or pixel-replication wrapper is used. This describes raster resolution, not a claim of an original After Effects/Blender/native-authoring project.

From the package root, with Python + Pillow, Node.js for JS cards, FFmpeg/libx264 and the documented existing font:

```sh
python tools/render_native.py 14 --font /path/to/simhei.ttf --outdir /path/to/new-render-14
python tools/encode_frames.py --frames /path/to/new-render-14/frames --output /path/to/new-MOTION-14.mp4
```

The guarded entry requires the recorded font SHA. New encoded bytes may differ with encoder builds; they are a new experiment and cannot replace the published pinned MP4 without a reviewed release update.

[Normalized run receipt](../../evidence/MOTION-14/RUN.json) · [Font dependency](../../evidence/MOTION-14/font-dependency.json)
