# MOTION-04 — 10-synthwave

Model-rendered research artifact. `human_review=pending` (no human aesthetic acceptance).

## Contract / mechanism

- Origin: staging/MOTION-04 (accepted old renderer, low-res 640x360)
- Mechanism (from staging INVENTORY): 条纹太阳/铬字/RGB split 1-2px (VHS/合成波)
- Platform: target_renderer=`raster (pure-JS procedural)`; executed=`frozen renderFrame + integer geometry scale (raster)`; relation=`restricted_adaptation`.
- Raster proof only — not a browser/WebGL native render.
- Audio: `not_applicable`.

## Params

- seed: `20261115`
- resolution: `[1920, 1080]` (fps 30, frames 300)
- schedule: BEAT=15 (120bpm), 18 beats, freeze>=270; SKIP_FRAME=256 repeats 255; VHS scanlines + RGB split 1-2px (original)
- renderer: `node render.js + native_scale_render.js`

## Source vs output hashes (kept separate)

- ORIGINAL staging renderer (render.js) sha256: `ad87c3a756f85cc8dfdf2ba3affee5224c039bb276903a97b53511d9b7fb154e`
- ORIGINAL staging mp4 (motion.mp4) sha256: `1fe611fe20693709373ccddc9070cae8df509909beba0a5a0174208c4b386b5c`
- ORIGINAL resolution: `[640, 360]`
- DELIVERED mp4 sha256: `2ee12606fa60433348b1823b5370236389a2c734df69fa1d5120a4a19065fb52`
- DELIVERED renderer copy sha256: `ad87c3a756f85cc8dfdf2ba3affee5224c039bb276903a97b53511d9b7fb154e`

## Measured (fresh full decode of delivered mp4)

- decoded_frames: `300`; dimensions: `[[1920, 1080]]`; fps: `30.0`; duration: `10.0s`
- distinct first/mid/last signatures: `3`
- size_bytes: `12237642`
- contact sheet: `gallery/contact_sheets/MOTION-04.jpg` (8 keyframes)

## Adaptation notes (honesty)

Native re-render at 1920x1080: frozen renderFrame(n) unchanged + integer geometry scale S=3 (x->3x, y->3y, RGB-split shift from the original 1-2 logical px becomes 3-6 native px). Seed, beat schedule, VHS skip and RGB-split method untouched. Mechanism preserved; geometry scaled. Encoder size ~11.7MiB (mp4v; H264 unavailable) — fidelity kept over artificial shrinkage.

## Reproduction

# Native re-render (frozen renderer + integer geometry scale S=3)

```bash
# 1. render 300 native 1920x1080 PNG frames + frame_hashes.json
node tools/native_scale_render.js sources/MOTION-04/render.js renders/MOTION-04 full 640 360 'rgb'
# 2. deterministic fresh-process sample (non-contiguous / repeated)
node tools/native_scale_render.js sources/MOTION-04/render.js _det_scratch/MOTION-04-sample batch 640 360 'rgb' 5,77,150,233,299,77,150
# 3. encode to mp4v MP4 (30fps / 1920x1080 / 300f)
python tools/encode_frames.py renders/MOTION-04/frames media/MOTION-04.mp4 300
# 4. verify all 12 delivered mp4s (full decode)
python verify_all.py --dir .
```

