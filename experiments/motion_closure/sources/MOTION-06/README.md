# MOTION-06

Bauhaus grid composition: primary-colour geometry, mechanical beat-aligned movements and final poster hold.

Source SHA-256: `ec68f579afe1f7dbd588d8036b116865348bf50ebec23ec0d0ff01b815ad69ff`

MP4 SHA-256: `d37d758a87c6fe064999519b92f45a3f85650e385414cfb64aaf54cb38ffd976`

All delivered videos: H.264/avc1, yuv420p, 1920×1080, 30 fps, 300 frames, 10 seconds.

## Current generation

This renderer computes its final raster directly at 1920×1080. No lower-resolution render or pixel-replication wrapper is used. This describes raster resolution, not a claim of an original After Effects/Blender/native-authoring project.

From the package root, with Python + Pillow, Node.js for JS cards, FFmpeg/libx264 and the documented existing font:

```sh
python tools/render_native.py 06 --font /path/to/simhei.ttf --outdir /path/to/new-render-06
python tools/encode_frames.py --frames /path/to/new-render-06/frames --output /path/to/new-MOTION-06.mp4
```

The guarded entry requires the recorded font SHA. New encoded bytes may differ with encoder builds; they are a new experiment and cannot replace the published pinned MP4 without a reviewed release update.

[Normalized run receipt](../../evidence/MOTION-06/RUN.json) · [Font dependency](../../evidence/MOTION-06/font-dependency.json)
