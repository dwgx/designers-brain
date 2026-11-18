# Motion closure — 12 playable studies

This package contains **12 complete videos**, their procedural source files, a playable gallery, and evidence bound to the delivered bytes. Every video is **1920×1080, 30 fps, 300 frames, 10 seconds, H.264/avc1 and yuv420p**. Seven repaired studies compute their raster directly at 1920×1080; five accepted original videos retain their previous bytes.

| Delivery | Cards | What changed |
|---|---|---|
| Current native-resolution render | 03, 04, 05, 06, 07, 09, 14 | Final native raster sources, actual font outlines where needed, complete final H.264 encodes and bound render/font evidence |
| Preserved original delivery | 02, 10, 12, 13, 15 | MP4 and source bytes unchanged; full media decode and strict browser measurements still cover these five |

Here, **native resolution describes the raster computed by these Python and JavaScript renderers**. It does not assert delivery of an After Effects, Blender, browser-native or other original authoring-platform project. These are visual mechanism studies; this package does not claim audio review, broad device compatibility, a production motion library, human aesthetic approval, or completed owner scoring.

## Watch

From this directory:

```sh
python tools/serve_gallery.py
```

Open the printed localhost URL. The gallery contains 12 controlled HTML video elements, source links and four-frame contact sheets made from the actual delivered MP4s at frames 0, 120, 233 and 299. The preview server implements HTTP byte ranges. A deployed server must return valid `206 Content-Range` responses and `video/mp4`; a default Python HTTP server does not establish that requirement.

## Verify the delivered package

Python 3.10+ and an FFmpeg build are required. `ffprobe` and OpenCV are not required. The default command **does not rerender any animation**:

```sh
python verify_all.py --ffmpeg /path/to/ffmpeg --report /path/to/verification.json
```

Omit `--ffmpeg` when FFmpeg is on `PATH`, or set `FFMPEG`. Paths may be quoted on Windows. Exit `0` means every check completed; `1` is a failed file, evidence or media check; `2` is an unavailable/unfinished tool environment. Missing evidence is a failure and cannot be skipped into a passing result.

The verifier enforces the fixed 12-card set, pinned sizes and SHA-256 values for all 12 videos and render sources, both shared CJK helpers, seven current render/font receipts, and strict browser evidence. It decodes **every video to EOF**, checks all 300 decoded frames, verifies their dimensions and pixel format, and checks every frame's timestamp and duration against 30 fps. Input H.264/avc1 and yuv420p are checked before output conversion; frame-rate or scaling filters are not used to make an incorrect file pass. New seven-video encodes must also have their MP4 `moov` atom before `mdat` for fast start.

`release-pins.json` is itself SHA-bound by the verifier. It records the previous and current source/media SHA values, original raw run-receipt SHA values, the recorded font dependency, and the strict browser receipt/probe source. This provides reproducible release integrity within the reviewed checkout; it is not a digital signature from an external trust authority. A different release needs an explicit reviewed pin update.

## What the receipts prove

The seven normalized `evidence/MOTION-XX/RUN.json` files preserve the actual Windows run's 300 PNG hashes, complete decoded-frame hash ledger, recorded tool versions, four successful command roles, source/video/font bindings, and the fresh-process checks at frames **299, 120 and 0**. Private absolute command paths were removed through an allowlist. Each public receipt retains its original raw receipt's SHA. Repeated frame hashes are allowed for intentional holds.

MOTION-14's [data-source receipt](evidence/MOTION-14/DATA-SOURCE.json) records its USGS table, selected groups and rounding. The values describe stored water as a percentage of total water. The four selected groups do not form the entire distribution and are not normalized to 100%; the small freshwater-lakes-plus-rivers group is the approximate sum of two already-rounded percentages. This is distinct from usable or accessible water supply.

The browser evidence records **an actual isolated Chrome session across all 12 videos**: 1080p load, four seeks at 0.5, 4, 233/30 and 299/30 seconds, settled `currentTime` within 0.12 seconds, SHA-256 of drawn 32×18 RGBA pixels with at least two distinct frames, HTTP 206, and actual playhead advance. The verifier recomputes these acceptance conditions from the recorded values and checks the normalized receipt against the pinned raw original. Reading this receipt is distinct from opening a new Chrome session.

`history/rejected-weak-browser` retains the earlier seven-video probe whose claimed seek successes were invalid: every observed seek time was zero. Its seek PASS flags are rejected; current acceptance uses the subsequent all-12 strict probe. The old load/play observations remain historical evidence only.

The `INTEGRATION-VERIFY.json` receipt records the integration-time full decode. Running `verify_all.py` produces a fresh verification against the files actually present. Neither receipt supplies human design scores.

## Reproduce one of the seven current native renders

Optional generation requires **Python + Pillow**, **Node.js for cards 04/05/06/07/09**, and an existing CJK font. JavaScript's shared CJK helper invokes Python/Pillow; these five cards are not dependency-free JavaScript. The two helpers live directly under `sources/`, so the renderers' `../cjk_text.js` import resolves without private paths. The guard sets `MOTION_PYTHON` to the invoking Python interpreter and uses explicit UTF-8 exchange.

Some frozen renderer comments retain historical phrases such as “dependency-free” or references to an earlier staging-only schedule/checker. The dependency list and current commands in this README describe this delivered package; those historical phrases do not add missing tools or remove the actual Python/Pillow dependency.

The final Windows font dependency is `simhei.ttf`, face index 0, SHA-256:

```text
9b1959db3b3abeb7efdaec26edf7dfe871a6039de8d614af7248575207be629e
```

Fonts and font licenses are not redistributed. Use an existing authorized local font. The guarded reproduction command requires this recorded font SHA; a different font is a new visual experiment, with a new dependency receipt and review, rather than a byte-identical reproduction of this release.

```sh
python tools/render_native.py 03 --font /path/to/simhei.ttf --outdir /path/to/new-render-03
python tools/encode_frames.py --frames /path/to/new-render-03/frames --output /path/to/new-MOTION-03.mp4 --ffmpeg /path/to/ffmpeg --receipt /path/to/encode.json
```

The output directory must be new. The encoder fully loads all **exactly 300 PNGs**, rejects missing/extra/mixed or unreadable frames and incorrect dimensions, writes H.264 to a temporary file, and publishes the output only after strict full decode succeeds. It never skips a damaged frame. Encoder builds can produce different compressed bytes; regenerated MP4s do not silently replace the pinned public release.

## Negative controls

```sh
python tools/negative_controls.py --ffmpeg /path/to/ffmpeg --report /path/to/negative-controls.json
```

This first verifies the real package, then changes copies in a temporary directory: missing and modified sources/helpers, omitted source SHA, missing video, truncated video, removed card, and forged font/browser measurements. Each mutation must fail with exit `1`; a missing executable or skipped test is not accepted as a successful negative control. The original package is never edited.

After a successful full verification, add `--positive-report /path/to/verification.json` to avoid repeating that same full decode. The script accepts the existing report only when its schema, manifest SHA and complete media set match, and it freshly rechecks every current file/evidence binding before applying the negative controls. `verify_all.py` itself always performs its full decode.

## History and boundaries

`history/e0cfe964/` preserves the old manifest, sources and permissive tools for traceability. Its scale-wrapper route and its global `mp4v` codec label are superseded. Those historical scripts are not current generation entry points, and their prose should not be read as a present native-render claim. Old media binaries are not duplicated; previous/current SHA mappings remain in the manifests and release pins. The current package excludes render PNG sequences, font binaries, FFmpeg executables and private absolute project paths.
