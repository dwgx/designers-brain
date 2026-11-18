# MOTION-06 — 09-bauhaus

Model-rendered research artifact. `human_review=pending` (no human aesthetic acceptance).

## Contract / mechanism

- Origin: staging/MOTION-06 (accepted old renderer, low-res 640x360)
- Mechanism (from staging INVENTORY): quarter circles 90° 旋转/禁用 overshoot (机械几何网格)
- Platform: target_renderer=`raster (pure-JS procedural)`; executed=`frozen renderFrame + integer geometry scale (raster)`; relation=`restricted_adaptation`.
- Raster proof only — not a browser/WebGL native render.
- Audio: `not_applicable`.

## Params

- seed: `20261115`
- resolution: `[1920, 1080]` (fps 30, frames 300)
- schedule: BEAT=15, beatOf clamped to 18, one actor per beat, CELL=40 grid, rotation only 90deg multiples, freeze 270..299 (original)
- renderer: `node render.js + native_scale_render.js`

## Source vs output hashes (kept separate)

- ORIGINAL staging renderer (render.js) sha256: `e8a4c1dc91523382a0eec6374f28b2fd611d931bfecaae4563c21be282fb03ca`
- ORIGINAL staging mp4 (motion.mp4) sha256: `b23a53013411c62e83cd76dc0635b5a1bd0058d0670fa97a27857543e5e10c94`
- ORIGINAL resolution: `[640, 360]`
- DELIVERED mp4 sha256: `677d4186dabc1266bc515504d5c40f6f6553ccbf646c65bb1611dbc4b1fa5405`
- DELIVERED renderer copy sha256: `e8a4c1dc91523382a0eec6374f28b2fd611d931bfecaae4563c21be282fb03ca`

## Measured (fresh full decode of delivered mp4)

- decoded_frames: `300`; dimensions: `[[1920, 1080]]`; fps: `30.0`; duration: `10.0s`
- distinct first/mid/last signatures: `3`
- size_bytes: `3504709`
- contact sheet: `gallery/contact_sheets/MOTION-06.jpg` (8 keyframes)

## Adaptation notes (honesty)

Native re-render: frozen renderFrame(n, seed) unchanged + integer geometry scale S=3 (40px grid -> 120px native cells). Seed phase, one-actor-per-beat schedule and 90deg-only rotations untouched. Mechanism preserved; geometry scaled.

## Reproduction

# Native re-render (frozen renderer + integer geometry scale S=3)

```bash
# 1. render 300 native 1920x1080 PNG frames + frame_hashes.json
node tools/native_scale_render.js sources/MOTION-06/render.js renders/MOTION-06 full 640 360 '[[239,233,216],[26,26,26],[214,48,38],[240,190,0],[29,78,156]]'
# 2. deterministic fresh-process sample (non-contiguous / repeated)
node tools/native_scale_render.js sources/MOTION-06/render.js _det_scratch/MOTION-06-sample batch 640 360 '[[239,233,216],[26,26,26],[214,48,38],[240,190,0],[29,78,156]]' 5,77,150,233,299,77,150
# 3. encode to mp4v MP4 (30fps / 1920x1080 / 300f)
python tools/encode_frames.py renders/MOTION-06/frames media/MOTION-06.mp4 300
# 4. verify all 12 delivered mp4s (full decode)
python verify_all.py --dir .
```

