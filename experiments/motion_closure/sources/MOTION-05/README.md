# MOTION-05

Connected outline morph: bulb → bubble → pencil → star, circle mediators, bounded squash/stretch and final hold.

Source SHA-256: `882d2505eff9c525fa74cf93cd93ccad15d6adbe6a10d02fce9759505ed707ca`

MP4 SHA-256: `ca7a6f7e0b3a11b8ac71de02e09015ff8be19c6dcaa75c6c656753c588745ae1`

All delivered videos: H.264/avc1, yuv420p, 1920×1080, 30 fps, 300 frames, 10 seconds.

## Current generation

This renderer computes its final raster directly at 1920×1080. No lower-resolution render or pixel-replication wrapper is used. This describes raster resolution, not a claim of an original After Effects/Blender/native-authoring project.

From the package root, with Python + Pillow, Node.js for JS cards, FFmpeg/libx264 and the documented existing font:

```sh
python tools/render_native.py 05 --font /path/to/simhei.ttf --outdir /path/to/new-render-05
python tools/encode_frames.py --frames /path/to/new-render-05/frames --output /path/to/new-MOTION-05.mp4
```

The guarded entry requires the recorded font SHA. New encoded bytes may differ with encoder builds; they are a new experiment and cannot replace the published pinned MP4 without a reviewed release update.

[Normalized run receipt](../../evidence/MOTION-05/RUN.json) · [Font dependency](../../evidence/MOTION-05/font-dependency.json)
