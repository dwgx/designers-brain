# MOTION-07 — 22-hud

Model-rendered research artifact. `human_review=pending` (no human aesthetic acceptance).

## Contract / mechanism

- Origin: staging/MOTION-07 (accepted old renderer, low-res 640x360)
- Mechanism (from staging INVENTORY): cyan→orange 状态切换/锁定框 scale 1.4→1.0 (HUD 界面)
- Platform: target_renderer=`raster (pure-JS procedural)`; executed=`frozen renderFrame + integer geometry scale (raster)`; relation=`restricted_adaptation`.
- Raster proof only — not a browser/WebGL native render.
- Audio: `not_applicable`.

## Params

- seed: `20261115`
- resolution: `[1920, 1080]` (fps 30, frames 300)
- schedule: TICK=5 (60 ticks), FREEZE_T=54 clamped, hudState(t) cyan->orange + lock scale 1.4->1.0 (original)
- renderer: `node render.js + native_scale_render.js`

## Source vs output hashes (kept separate)

- ORIGINAL staging renderer (render.js) sha256: `7f43ffef07f2d3d29335d82b5789978b4522d90d80fec478239c40ff8e1c4077`
- ORIGINAL staging mp4 (motion.mp4) sha256: `772b26b5b3695e43a329e54f33287b48948bf4bfb9ce31e175ca5673f80010a9`
- ORIGINAL resolution: `[640, 360]`
- DELIVERED mp4 sha256: `752224881f10c9f55ca4c5eea39b2685024decc66c85088f063edc1fed50b751`
- DELIVERED renderer copy sha256: `7f43ffef07f2d3d29335d82b5789978b4522d90d80fec478239c40ff8e1c4077`

## Measured (fresh full decode of delivered mp4)

- decoded_frames: `300`; dimensions: `[[1920, 1080]]`; fps: `30.0`; duration: `10.0s`
- distinct first/mid/last signatures: `3`
- size_bytes: `5632543`
- contact sheet: `gallery/contact_sheets/MOTION-07.jpg` (8 keyframes)

## Adaptation notes (honesty)

Native re-render: frozen renderFrame(n, seed) unchanged + integer geometry scale S=3. Seed-bound speckle, tick schedule, reveal-by-stroke and lock scale untouched. Mechanism preserved; geometry scaled.

## Reproduction

# Native re-render (frozen renderer + integer geometry scale S=3)

```bash
# 1. render 300 native 1920x1080 PNG frames + frame_hashes.json
node tools/native_scale_render.js sources/MOTION-07/render.js renders/MOTION-07 full 640 360 '[[4,23,28],[7,31,38],[0,229,255],[255,106,0]]'
# 2. deterministic fresh-process sample (non-contiguous / repeated)
node tools/native_scale_render.js sources/MOTION-07/render.js _det_scratch/MOTION-07-sample batch 640 360 '[[4,23,28],[7,31,38],[0,229,255],[255,106,0]]' 5,77,150,233,299,77,150
# 3. encode to mp4v MP4 (30fps / 1920x1080 / 300f)
python tools/encode_frames.py renders/MOTION-07/frames media/MOTION-07.mp4 300
# 4. verify all 12 delivered mp4s (full decode)
python verify_all.py --dir .
```

