# MOTION-09

Glassmorphism over a moving blurred aurora light field; restrained highlights, native-resolution CJK text and final hold.

Source SHA-256: `dbff6af27a11ec3ad928fc7f633178ef06fb2453b115cda27d7c016773a010a0`

MP4 SHA-256: `553e3335f20571a561800cbd8e208b26af945d2ee39e2e23743797d776bd5e57`

All delivered videos: H.264/avc1, yuv420p, 1920×1080, 30 fps, 300 frames, 10 seconds.

## Current generation

This renderer computes its final raster directly at 1920×1080. No lower-resolution render or pixel-replication wrapper is used. This describes raster resolution, not a claim of an original After Effects/Blender/native-authoring project.

From the package root, with Python + Pillow, Node.js for JS cards, FFmpeg/libx264 and the documented existing font:

```sh
python tools/render_native.py 09 --font /path/to/simhei.ttf --outdir /path/to/new-render-09
python tools/encode_frames.py --frames /path/to/new-render-09/frames --output /path/to/new-MOTION-09.mp4
```

The guarded entry requires the recorded font SHA. New encoded bytes may differ with encoder builds; they are a new experiment and cannot replace the published pinned MP4 without a reviewed release update.

[Normalized run receipt](../../evidence/MOTION-09/RUN.json) · [Font dependency](../../evidence/MOTION-09/font-dependency.json)
