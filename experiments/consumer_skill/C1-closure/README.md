# C1 closure attempt — complete process, failed case

This is the single attempt `C1-CLOSURE-20261118-001` against frozen e0cfe964/ae4a28ae. [Consumer result](RESULT.md) and [Root independent review](control/ROOT-REVIEW.md) agree: H1 is partial and the case failed because both real drawings lose important form/readability. It is not a technical block or a human rating. The historical blocked C1 in `../C1/` remains unchanged.

- [A rendered output](B/A-render.png) and [B rendered output](B/B-render.png).
- [Frozen measurements and actual negative control](B/measurement-results.json).
- [Original consumer receipt](receipt.json), [pre-holdout seal](B/PRE-HOLDOUT-SEAL.json) and [Root decision](control/ROOT-REVIEW.json).
- [Public projection map](PUBLIC-PROJECTION.json): some locator-bearing documents are redacted, with original and public hashes distinguished. Raw operational tool logs and orchestration scripts are retained privately, not silently claimed present here. The 49-file original manifest records the original run, not this smaller public projection.

The checker is a local composition checker; its green values do not make this failed case pass. To reproduce its measurements, copy this directory to a new temporary folder, remove only that copy's `B/measurement-results.json`, then run `python -B B/check-compositions.py` with NumPy and Pillow. Preserve the published evidence. It verifies the five pre-holdout locks before measuring and writes a new timestamped result. The three original reference images remain in the existing public image library, with their own credits; no images are re-licensed or duplicated here.
