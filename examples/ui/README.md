# Three UI research fixtures

The three imported fixtures retain their historical receipts. The repaired
sources have now been exercised on Windows with Chrome 157.0.8103.79. The
2026-11-17 22:48 UTC [closure run](../../docs/audit/closure-20261118/runtime/foundation-final-run/RESULT.json)
records the resolver, CDP and UI-03 browser checks. The 22:52 UTC
[targeted harness rerun](../../docs/audit/closure-20261118/runtime/runtime-harness-rerun/RESULT.json)
records the repaired UI-01 negative controls and concurrent temporary-profile
checks. These are measured research contracts, with the limits below.

| Case | Open the example | Run documentation | Verified scope |
|---|---|---|---|
| UI-01 | [Lifecycle fixture](ui-01/fixture.html) | [README](ui-01/README.md) | 119 assertions; terminal advance/read-state regression; clean positive and four mutations rejected by their intended assertions |
| UI-02 | [Tokens, Chinese input and focus](ui-02/fixture.html) | [README](ui-02/README.md) | 20 resolver controls; 63 assertions; actual CDP Tab/focus and same-page reset; composition sends 0 during and exactly 1 after commit |
| UI-03 | [Counter component](ui-03/fixture/index.html) | [README](ui-03/README.md) | 10 Node checks; geometry, CDP input and live-DOM gates pass; comment/div and removed-aria-label browser controls rejected |

## Evidence chronology and limits

Cloud Chromium's earlier socket-permission failure remains a historical
environment result; it is not the current Windows verification status. The
first closure RESULT still contains an unsuccessful concurrent UI-01 negative
run. It has not been rewritten as passing: the later targeted rerun binds the
repaired harness sources and their actual successful results.

UI-02 and UI-03 also retain detailed case-local reports from 22:14 UTC. Those
timestamps remain unchanged. The later closure commands provide fresh execution
evidence; UI-03's retained full geometry report has the same source hashes and
pixel measurements as the independently checked 22:48 run. See each case for
the precise reports and coverage.

The resolver and static/behavior checks do not establish production AG-UI
transport recovery, OS-native IME candidate-window behavior, full keyboard or
WCAG conformance, aesthetic approval or actual human acceptance. UI-03 model
aesthetics remain untested and human judgement remains pending.

## Dependencies and portability

Python 3.10+; Node 24; Chrome/Chromium. Browser scripts discover Chrome through
`UI_CHROME`, PATH, then platform conventions via [chrome_util.py](chrome_util.py).
They launch only a fresh owned process with a temporary profile. The UI-01 and
UI-02 harnesses now allocate separate temporary directories for each invocation;
the targeted rerun exercised four concurrent subprocesses successfully.

Python dependencies: `jsonschema`, `referencing`, `Pillow`, and
`websocket-client` (or the already-installed `websockets` synchronous API).
The small [cdp_util.py](cdp_util.py) prefers websocket-client. No global install,
vendored node_modules, private binary path, profile or session is required.
Node's static HTML check calls Python's stdlib HTMLParser; `UI_PYTHON` can select
that interpreter when its command is not `python`.

Historical `evidence/receipt.json` files remain historical accepted receipts.
They do not certify modified source bytes. UI-02's original IME JSON and UI-03's
original matrix remain under each case's `evidence/history/`. Future source
changes require checks bound to those changed bytes; the recorded runs above
do not certify later revisions automatically.

`python -B check_gate_contracts.py` passed seven **synthetic gate controls** in
the closure run. It never substitutes for real browser execution.
