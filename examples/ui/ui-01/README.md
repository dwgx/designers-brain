# UI-01 — scripted lifecycle fixture

Open [fixture.html](fixture.html). Three concurrent cards demonstrate running,
waiting-for-input, completed, cancelled, failed and stream-interrupted states,
with labels, icons, borders and per-card drafts/results. This is a scripted
fixture; it does not consume live AG-UI/SSE events.

## Repair

A card at its last step disables further advance and the handler returns
without changing state. Marking a completed result read followed by a repeated
advance preserves read status, draft and result owner. The browser selftest
exercises these actions and `_check.py` asserts the resulting states.

Each harness invocation uses its own temporary Chrome profile, addressing the
profile collision observed in the first concurrent closure run. Console output
is configured for UTF-8. The negative controller requires exit 1 **and the
intended AssertionError**, so an unrelated harness failure is not accepted as
a caught mutation.

## Run

From this directory, with Python and discoverable Chrome:

```bash
python -B _check.py
python -B check_negative.py
```

## Verified Windows result

On 2026-11-17 at 22:52 UTC, the
[targeted harness rerun](../../../docs/audit/closure-20261118/runtime/runtime-harness-rerun/RESULT.json)
returned exit 0 for both commands. `_check.py` printed **119 assertions**,
including the terminal-action/read-state regression. The clean negative-control
fixture passed, and all four mutated fixtures returned exit 1 with their
specified assertion:

| Mutation | Intended assertion reached |
|---|---|
| Extra advance before the T2 snapshot | `T2-after-1-advance/T2 data-state=waiting-for-input` |
| Wrong-card advance before the T3 snapshot | `T3-after-1-advance/T3 data-state=waiting-for-input` |
| Relabelled truncation terminal state | `T3-after-2-advances/T3 data-state=stream-interrupted` |
| Altered truncation-rule text | `fixture records AG-UI truncation rule` |

The run also exercised UI-01 checks alongside two UI-02 checks in separate
subprocesses. It supports that measured concurrency case, not unlimited
parallel execution. Source hashes, command exits and log hashes are in the
rerun record; the exact harness changes are in
[PATCHES.json](../../../docs/audit/closure-20261118/runtime/runtime-harness-repair/PATCHES.json).

The earlier cloud socket-permission failure and the
[first closure run's](../../../docs/audit/closure-20261118/runtime/foundation-final-run/RESULT.json)
unsuccessful concurrent negative control remain historical failures. The old
117-assertion result is also historical; neither replaces the 119-assertion
result on the repaired source.

The mutations test the scripted contract, not network event deduplication or
reconnection. The failure-injection button is a demo override, not evidence of
a legal production transition after an ended run. The inherited
[receipt](evidence/receipt.json) is unchanged. No human visual/usability
acceptance is claimed. Chrome profiles and console outputs are runtime-only
OS temporary files; [Chrome discovery](../chrome_util.py) contains no private
executable location.
