# Rejected seek claim

This historical seven-video probe recorded actual load and real playhead advance. It incorrectly marked its seek check passed: every requested seek observed currentTime=0. Those seek PASS flags are explicitly rejected. It used a server without the byte-range behavior required by the corrected probe. Current browser evidence is evidence/BROWSER-STRICT-12.raw.json and the pinned normalized receipt; it measures all 12 videos using HTTP 206, time tolerance 0.12 seconds, settled seeks and drawn video pixel hashes. This archive is not part of the current acceptance result.
