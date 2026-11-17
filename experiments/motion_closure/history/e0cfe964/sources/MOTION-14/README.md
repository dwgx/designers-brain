# MOTION-14 — 19-paperclip

Model-rendered research artifact. `human_review=pending` (no human aesthetic acceptance).

## Contract / mechanism

- Origin: staging/MOTION-14 (accepted old renderer, low-res 960x540)
- Mechanism (from staging INVENTORY): charts to scale/8-12px 白描边 (实物贴纸科普)
- Platform: target_renderer=`raster (pure-python Pillow)`; executed=`frozen render_frame + integer geometry scale (raster)`; relation=`restricted_adaptation`.
- Raster proof only — not a browser/WebGL native render.
- Audio: `not_applicable`.

## Params

- seed: `20261115`
- resolution: `[1920, 1080]` (fps 30, frames 300)
- schedule: ADD_FRAMES sticker/chart additions, CAMERA_KEYS pan+zoom smoothstep, freeze 290..299 (original)
- renderer: `python render.py + native_scale_render.py`

## Source vs output hashes (kept separate)

- ORIGINAL staging renderer (render.py) sha256: `88a26cf3a72ab47359ee22b1c06596dfbec0ec197a1630a8165959dbacf58d27`
- ORIGINAL staging mp4 (motion.mp4) sha256: `f68716774fbef245e598d05543eaaac7d767759b8c7dd44864576c251353defe`
- ORIGINAL resolution: `[960, 540]`
- DELIVERED mp4 sha256: `e8fc5d22e1810406b61191557925d0c2e68ec571cdca89ba5da78d34d28aca4a`
- DELIVERED renderer copy sha256: `88a26cf3a72ab47359ee22b1c06596dfbec0ec197a1630a8165959dbacf58d27`

## Measured (fresh full decode of delivered mp4)

- decoded_frames: `300`; dimensions: `[[1920, 1080]]`; fps: `30.0`; duration: `10.0s`
- distinct first/mid/last signatures: `3`
- size_bytes: `5900038`
- contact sheet: `gallery/contact_sheets/MOTION-14.jpg` (8 keyframes)

## Adaptation notes (honesty)

Native re-render at 1920x1080: frozen render_frame(n, seed) unchanged + integer geometry scale S=2 (x->2x, y->2y, PIL NEAREST). Seed, ADD schedule, camera pan/zoom series, proportional bar lengths and white outline width untouched. Mechanism preserved; geometry scaled. The renderer loads a system CJK font with a built-in fallback; no private asset copied.

## Reproduction

# Native re-render (frozen renderer + integer geometry scale S=2)

```bash
# 1. render 300 native 1920x1080 PNG frames + frame_hashes.json
python tools/native_scale_render.py sources/MOTION-14/render.py renders/MOTION-14 full
# 2. deterministic fresh-process sample (non-contiguous / repeated)
python tools/native_scale_render.py sources/MOTION-14/render.py _det_scratch/MOTION-14-sample batch 5,77,150,233,299,77,150
# 3. encode to mp4v MP4 (30fps / 1920x1080 / 300f)
python tools/encode_frames.py renders/MOTION-14/frames media/MOTION-14.mp4 300
# 4. verify all 12 delivered mp4s (full decode)
python verify_all.py --dir .
```

