# MOTION-05 — 08-morph

Model-rendered research artifact. `human_review=pending` (no human aesthetic acceptance).

## Contract / mechanism

- Origin: staging/MOTION-05 (accepted old renderer, low-res 640x360)
- Mechanism (from staging INVENTORY): 收敛中介简形再展开/不打结 (链式拓扑形变)
- Platform: target_renderer=`raster (pure-JS procedural)`; executed=`frozen renderFrame + integer geometry scale (raster)`; relation=`restricted_adaptation`.
- Raster proof only — not a browser/WebGL native render.
- Audio: `not_applicable`.

## Params

- seed: `20261115`
- resolution: `[1920, 1080]` (fps 30, frames 300)
- schedule: BEAT=15; MORPH_WINDOWS bg at 30/105/180/270; linear radial morph (no easing); FREEZE_AT=270 (original)
- renderer: `node render.js + native_scale_render.js`

## Source vs output hashes (kept separate)

- ORIGINAL staging renderer (render.js) sha256: `2706ae15ee60f0488e81dac9257dbcd3db016b8e53b7658341fed4ae0bd5f53e`
- ORIGINAL staging mp4 (motion.mp4) sha256: `ce52aba1bf0870a5a7e93d220e277a99d45b819cf28a2a75283ec3206ae1b1c4`
- ORIGINAL resolution: `[640, 360]`
- DELIVERED mp4 sha256: `3d8914d101369cf9236f884b0941b934ce192c681f6052f849021e625410d95d`
- DELIVERED renderer copy sha256: `2706ae15ee60f0488e81dac9257dbcd3db016b8e53b7658341fed4ae0bd5f53e`

## Measured (fresh full decode of delivered mp4)

- decoded_frames: `300`; dimensions: `[[1920, 1080]]`; fps: `30.0`; duration: `10.0s`
- distinct first/mid/last signatures: `3`
- size_bytes: `2061784`
- contact sheet: `gallery/contact_sheets/MOTION-05.jpg` (8 keyframes)

## Adaptation notes (honesty)

Native re-render: frozen renderFrame(n) unchanged + integer geometry scale S=3. Seed, morph windows, linear radial speed, freeze and palette untouched. Mechanism preserved; geometry scaled. Indexed palette read from the frozen renderer's RGB constant.

## Reproduction

# Native re-render (frozen renderer + integer geometry scale S=3)

```bash
# 1. render 300 native 1920x1080 PNG frames + frame_hashes.json
node tools/native_scale_render.js sources/MOTION-05/render.js renders/MOTION-05 full 640 360 '[[26,26,58],[14,77,92],[138,75,30],[91,42,107],[16,26,58],[244,234,210],[40,30,50],[240,190,60]]'
# 2. deterministic fresh-process sample (non-contiguous / repeated)
node tools/native_scale_render.js sources/MOTION-05/render.js _det_scratch/MOTION-05-sample batch 640 360 '[[26,26,58],[14,77,92],[138,75,30],[91,42,107],[16,26,58],[244,234,210],[40,30,50],[240,190,60]]' 5,77,150,233,299,77,150
# 3. encode to mp4v MP4 (30fps / 1920x1080 / 300f)
python tools/encode_frames.py renders/MOTION-05/frames media/MOTION-05.mp4 300
# 4. verify all 12 delivered mp4s (full decode)
python verify_all.py --dir .
```

