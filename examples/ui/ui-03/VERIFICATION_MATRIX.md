# UI-03 — current five-layer verification matrix

The repaired source passed the three mechanical browser layers on Windows
Chrome 157.0.8103.79. The 2026-11-17 **22:48 UTC**
[closure receipt](../../../docs/audit/closure-20261118/runtime/foundation-final-run/RESULT.json)
records the fresh Node, browser and browser-negative commands. The detailed
[case report and PNGs](evidence/browser-current/report.json) retain their
**22:14 UTC** timestamp; their source hashes and geometry measurements match
the independently checked 22:48 run. These two records are not relabelled as
one run. Geometry, behavior and semantics do not certify aesthetics or human
acceptance.

| Layer | Executed method | Verified result | Evidence |
|---|---|---|---|
| 1. Geometry | Same-process 320×200/DPR1 screenshots; Pillow exact RGB channel difference, zero tolerance | PASS: hover 7,829/64,000 changed pixels; dark 59,528/64,000; default repeat 0/64,000 | [Retained full report](evidence/browser-current/report.json), screenshots and difference PNGs; closure browser exit 0 |
| 2. Behavior | Five Node reducer checks; actual CDP mouse, Tab, Enter, Space and disabled controls | PASS: five reducer checks and six browser checks; pointer/Enter/Space activate once each, Tab shows focus, disabled pointer/keyboard are no-ops | [Full report](evidence/browser-current/report.json); `ui03-node` and `ui03-browser` in closure receipt |
| 3. Semantics | HTMLParser checks the unique counter/output; browser verifies live tag, required aria-label, aria/visibility/state | PASS on positive; comment/div and removed-aria-label mutants rejected by static and live-DOM gates | [Controls](evidence/negative-current/controls.json); `ui03-negatives` closure command exit 0 means both expected failures were detected |
| 4. Model aesthetic judgement | Separate subjective review if undertaken | Untested | No model opinion derived from numeric checks |
| 5. Human judgement | Actual reviewer, stimulus and explicit judgement required | Pending human | No human score or approval supplied |

The positive/comment-div/missing-name Node and browser exits are **0 / 1 / 1**.
In the comment/div mutant, geometry passes but keyboard behavior and live
semantics fail. In `missing_name`, geometry and behavior pass while the
required `aria-label` check fails. The visible button text remains, and the
report reads the attribute directly; it does not measure the browser's
computed accessible name. These observed controls show why a green behavior
layer or identical pixels cannot overwrite this declared semantic contract.

The final browser exit requires all three mechanical layers. An environment
or dependency failure exits 2, distinct from a measured contract failure
(exit 1). The live-DOM checks are a limited contract, not a full accessibility
tree, WCAG conformance test or human usability review.

The seven synthetic gate controls also passed in the closure run:
`python -B ../check_gate_contracts.py`. They do not execute Chrome and are
separate from the actual input and pixel evidence above.

The earlier cloud socket-permission failure remains a historical environment
result. The [original matrix](evidence/history/VERIFICATION_MATRIX-original.md)
is retained as a historical record under `evidence/history/`, with its old
pixelmatch counts and staging paths.
The current Pillow results name their algorithm and environment and do not
reuse those historical numbers. Later source changes require new bound
evidence before this matrix can describe them as verified.
