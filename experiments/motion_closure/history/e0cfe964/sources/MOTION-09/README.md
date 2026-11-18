# MOTION-09 — 12-aurora-glass

Model-rendered research artifact. `human_review=pending` (no human aesthetic acceptance).

## Contract / mechanism

- Origin: staging/MOTION-09 (accepted old renderer, low-res 640x360)
- Mechanism (from staging INVENTORY): 相邻色/backdrop blur ~30px+1px 高光 (毛玻璃)
- Platform: target_renderer=`raster (pure-JS procedural)`; executed=`frozen renderFrame + integer geometry scale (raster)`; relation=`restricted_adaptation`.
- Raster proof only — not a browser/WebGL native render.
- Audio: `not_applicable`.

## Params

- seed: `20261115`
- resolution: `[1920, 1080]` (fps 30, frames 300)
- schedule: HOLD=270, ACTIONS from beat_schedule, one sweep interval 180..210, APP_NAME_ONSET=216, DEPTH_AMPS=[2,4,7] (original)
- renderer: `node render.js + native_scale_render.js`

## Source vs output hashes (kept separate)

- ORIGINAL staging renderer (render.js) sha256: `8c4d4a07ac77d4b1dc6fc5cbaf2dcca2d9cb19e546cf2ddbeeb063d2f247eb8b`
- ORIGINAL staging mp4 (motion.mp4) sha256: `e2c866bae3b5d37ee56431396b98e621c6e05438ed1d2e1231cd1287243bc67b`
- ORIGINAL resolution: `[640, 360]`
- DELIVERED mp4 sha256: `aee1e1d19b76373037d3f72e627ba6346d811c9fd51205751a680a7cd4cf910f`
- DELIVERED renderer copy sha256: `8c4d4a07ac77d4b1dc6fc5cbaf2dcca2d9cb19e546cf2ddbeeb063d2f247eb8b`

## Measured (fresh full decode of delivered mp4)

- decoded_frames: `300`; dimensions: `[[1920, 1080]]`; fps: `30.0`; duration: `10.0s`
- distinct first/mid/last signatures: `3`
- size_bytes: `4113874`
- contact sheet: `gallery/contact_sheets/MOTION-09.jpg` (8 keyframes)

## Adaptation notes (honesty)

Native re-render: frozen renderFrame(n, seed) unchanged + integer geometry scale S=3. Seed, sine ease, light-field blur, glass cards and depth amplitudes untouched; blur radius in logical px scales by S. Mechanism preserved; geometry scaled.

## Reproduction

# Native re-render (frozen renderer + integer geometry scale S=3)

```bash
# 1. render 300 native 1920x1080 PNG frames + frame_hashes.json
node tools/native_scale_render.js sources/MOTION-09/render.js renders/MOTION-09 full 640 360 'rgb'
# 2. deterministic fresh-process sample (non-contiguous / repeated)
node tools/native_scale_render.js sources/MOTION-09/render.js _det_scratch/MOTION-09-sample batch 640 360 'rgb' 5,77,150,233,299,77,150
# 3. encode to mp4v MP4 (30fps / 1920x1080 / 300f)
python tools/encode_frames.py renders/MOTION-09/frames media/MOTION-09.mp4 300
# 4. verify all 12 delivered mp4s (full decode)
python verify_all.py --dir .
```

