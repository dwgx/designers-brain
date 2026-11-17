# MOTION-03 — 03-isometric

Model-rendered research artifact. `human_review=pending` (no human aesthetic acceptance).

## Contract / mechanism

- Origin: staging/MOTION-03 (accepted old renderer, low-res 960x540)
- Mechanism (from staging INVENTORY): 30°等角投影/顶面延迟 2-3 帧 (几何等轴生长)
- Platform: target_renderer=`raster (pure-python Pillow)`; executed=`frozen render_frame + integer geometry scale (raster)`; relation=`restricted_adaptation`.
- Raster proof only — not a browser/WebGL native render.
- Audio: `not_applicable`.

## Params

- seed: `20261115`
- resolution: `[1920, 1080]` (fps 30, frames 300)
- schedule: growth windows FOUND_DUR=30, WALL_DUR=60, ROOF_DELAY=2, ROOF_DUR=12; camera_pan -0.30/+0.10 px/frame (original)
- renderer: `python render.py + native_scale_render.py`

## Source vs output hashes (kept separate)

- ORIGINAL staging renderer (render.py) sha256: `d6493df994d176ccc2c60c321cabc273047ef4e6564360313ad6029216138289`
- ORIGINAL staging mp4 (motion.mp4) sha256: `ae6b83b9b9868d9b2b1841b806ce5b9e8372e78607366bb6da406e676308f005`
- ORIGINAL resolution: `[960, 540]`
- DELIVERED mp4 sha256: `e47d0ae332b8916143f902438c4b5babf936061baf42398024e3a0e57f0e84c3`
- DELIVERED renderer copy sha256: `d6493df994d176ccc2c60c321cabc273047ef4e6564360313ad6029216138289`

## Measured (fresh full decode of delivered mp4)

- decoded_frames: `300`; dimensions: `[[1920, 1080]]`; fps: `30.0`; duration: `10.0s`
- distinct first/mid/last signatures: `3`
- size_bytes: `6569202`
- contact sheet: `gallery/contact_sheets/MOTION-03.jpg` (8 keyframes)

## Adaptation notes (honesty)

Native re-render at 1920x1080 by calling frozen render_frame(n, seed) unchanged then applying integer geometry scale S=2 (x->2x, y->2y, 1px stroke->2x2 block, PIL NEAREST). Seed, growth schedule, 30-degree isometric basis and camera pan untouched. Mechanism preserved; geometry scaled. No upscaling of old video; every frame freshly rendered from the pure function.

## Reproduction

# Native re-render (frozen renderer + integer geometry scale S=2)

```bash
# 1. render 300 native 1920x1080 PNG frames + frame_hashes.json
python tools/native_scale_render.py sources/MOTION-03/render.py renders/MOTION-03 full
# 2. deterministic fresh-process sample (non-contiguous / repeated)
python tools/native_scale_render.py sources/MOTION-03/render.py _det_scratch/MOTION-03-sample batch 5,77,150,233,299,77,150
# 3. encode to mp4v MP4 (30fps / 1920x1080 / 300f)
python tools/encode_frames.py renders/MOTION-03/frames media/MOTION-03.mp4 300
# 4. verify all 12 delivered mp4s (full decode)
python verify_all.py --dir .
```

