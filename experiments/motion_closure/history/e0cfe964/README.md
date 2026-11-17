# Motion Closure — 12-card motion delivery

Model-rendered research artifacts. `human_review=pending` — no human aesthetic
acceptance is recorded. These are **raster-render proof**, not browser/WebGL
native-render proof.

## What is delivered

All 12 cards at **1920×1080 / 300 frames / 30 fps / 10 s**, full-decoded from the
delivered bytes (not from metadata):

| Source | Cards | Route |
|---|---|---|
| Original 1080 mp4 reused after fresh full decode | 02, 10, 12, 13, 15 | byte-identical staging originals |
| Native re-render of the frozen pure renderer at 1920×1080 | 03, 14 (S=2), 04, 05, 06, 07, 09 (S=3) | original `renderFrame(n, seed)` unchanged + integer geometry scale |

For the 7 re-rendered cards, the **mechanism, seed and beat/time schedule are
unchanged**; only geometry is scaled (x→x·S, y→y·S, 1px stroke→S×S block, no
resampling/filtering, no frame duplication, no wall clock, no RNG stream). This is
an honest raster re-author at higher resolution, **not** an upscale of the old
video and **not** a browser-native implementation. Per-card adaptations are in
`sources/MOTION-XX/README.md`.

The 300-frame PNG sequences for the 7 re-rendered cards are **reproduction
intermediates and are not shipped** (to avoid a heavy frame sequence);
`renders/MOTION-XX/frames/frame_hashes.json` is kept as the determinism baseline.
Step 1 of the reproduction commands regenerates the PNGs.

## Layout

- `media/MOTION-XX.mp4` — the 12 delivered MP4s (mp4v, cv2.VideoWriter).
- `sources/MOTION-XX/` — frozen original renderer + per-card README (params,
  source-vs-output hashes, reproduction commands, adaptation notes).
- `renders/MOTION-XX/frames/frame_hashes.json` — determinism baseline (SHA256 of
  each of the 300 frames) for the 7 re-rendered cards; PNGs regenerated on demand.
- `gallery/index.html`, `gallery/README.md`, `gallery/contact_sheets/MOTION-XX.jpg`
  — viewable gallery with 8 keyframes per card.
- `manifest.json` — binds every output sha256; original staging author/source
  hashes are recorded separately under `original` and in `provenance.json`.
- `verify_all.py` — full-decode verifier; `tools/` — reproduction/evidence tools.

## Verify (from this directory)

```bash
python verify_all.py --dir .                       # exit 0: all 12 pass
python tools/check_determinism.py                  # fresh-process non-contiguous/reordered/repeated hashes
python tools/fresh_decode.py media/*.mp4           # per-frame decode of any/all mp4s
```

Evidence logs (verifier, both negative controls, determinism, fresh decodes,
encoder settings) are in `lanes/MOTION/logs/` at the campaign root.

## Known limitations

- Raster procedural renders, not browser/compositor (WebGL/shader) native renders.
- Silent output (audio not applicable to these cards).
- mp4v codec only: H264/OpenH264 unavailable and ffmpeg not on PATH; OpenCV's
  quality/bitrate params are ignored by its FFmpeg backend. MOTION-04 is ~11.7 MiB
  (~9.8 Mbps), just over the soft 12 MB decimal target; fidelity was kept rather
  than distorting the mechanism to shrink bytes.
- Geometry-scale adaptation preserves the drawing method but does not add native
  detail beyond the original logical grid.
- Human aesthetic acceptance remains pending; model/script checks cannot substitute.
