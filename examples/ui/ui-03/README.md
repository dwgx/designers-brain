# UI-03 — layered counter acceptance

Open [fixture/index.html](fixture/index.html). The component and geometry,
behavior and semantic contracts are separated; model and human judgements
remain independent. This is a small research fixture.

## Run

From this case directory:

```bash
node fixture/run_checks.js
python -B check_negative.py
python -B fixture/run_visual.py
python -B check_negative.py --browser
```

The Node command runs five reducer checks and five static semantic checks.
It uses Python's stdlib HTMLParser, ignores comments, and checks the unique
`#counter` and `#count`, rather than any button-looking source text. It is not
an HTML5 accessibility tree; the browser driver separately checks live DOM.
Set `UI_PYTHON` if the Python executable is not named `python`.

The negative controller checks a clean positive fixture and two isolated
mutants: the actual control replaced by div with a button hidden in a comment,
and removal of the required `aria-label` (the `missing_name` case). No candidate
source is changed. `--browser`
requires a real browser PASS on the positive and a semantic-layer FAIL/exit 1
on each mutant. A dependency or environment exit 2 does not count as rejection.

## Verified Windows result and evidence times

The 2026-11-17 22:48 UTC
[closure run](../../../docs/audit/closure-20261118/runtime/foundation-final-run/RESULT.json)
records exit 0 for the Node checks, browser runner and browser negative-control
controller on Chrome 157.0.8103.79. All **10 Node checks** passed; the positive
browser report passed geometry, behavior **and** semantics.

The detailed [case report](evidence/browser-current/report.json) and its PNGs
retain the earlier **22:14 UTC** Windows run. Its source hashes and full geometry
measurements match the independently checked 22:48 run; the old timestamp is
not rewritten. At 320×200, DPR1, Pillow's exact RGB channel difference with
zero tolerance counted **7,829** changed pixels for hover, **59,528** for dark,
and **0** for default recheck, out of 64,000 pixels. These are exact RGB
measurements, not pixelmatch's perceptual metric or aesthetic scores.

The browser used CDP mouse input and Tab/Enter/Space/disabled controls. It
observed one activation per pointer, Enter and Space input, visible Tab focus,
and no count change from disabled pointer or keyboard input. The live-DOM
contract checked the actual target's button/type/required `aria-label`, pressed/disabled state,
output, visibility and state agreement. It is not a complete accessibility-tree
or WCAG audit.

The retained [negative-control record](evidence/negative-current/controls.json)
has the same **0 / 1 / 1** positive/comment-div/missing-name exits for both Node
and browser as the closure run:

| Case | Browser layer result | Meaning of the measured rejection |
|---|---|---|
| Positive | Geometry, behavior and semantics pass; exit 0 | The declared mechanical contract passes |
| Comment/div | Geometry passes; behavior and semantics fail; exit 1 | The live target is a div; Tab/Enter/Space do not satisfy the button contract, despite a button in a comment |
| `missing_name` | Geometry and behavior pass; semantics fails; exit 1 | Matching pixels and working input do not replace the required explicit `aria-label` |

Here the report's `name` field reads `aria-label` directly. The mutant retains
its visible button text; this is an explicit-label contract failure, not a
measurement of the browser's computed accessible name.

Model aesthetics remain **untested** and human judgement remains
**pending_human**. Final browser exit requires all three mechanical layers;
none can mask another. The controller itself exits 0 when its positive passes
and both intended failures are detected.

## Outputs, dependencies and history

The default output is `evidence/browser-current/report.json`, four screenshots
and three difference images. `--output PATH` selects another directory;
browser negatives use `evidence/negative-current/` by default. The closure run
used separate output directories recorded in its receipt, preserving the
case-local 22:14 evidence.

Dependencies: Node 24, Python 3.10+, Pillow, websocket-client (or websockets.sync),
and discoverable Chrome. No npm packages or global installation are needed.

Cloud Chromium's earlier socket-permission failure remains historical and does
not describe the successful Windows runs. See the
[current five-layer matrix](VERIFICATION_MATRIX.md). The
[original matrix](evidence/history/VERIFICATION_MATRIX-original.md) and
[accepted receipt](evidence/receipt.json) remain unchanged historical records,
including their old staging paths and pixelmatch measurements. Future code
changes require new source-bound checks; those historical receipts do not
certify revised source bytes.
