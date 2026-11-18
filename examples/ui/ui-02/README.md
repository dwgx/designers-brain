# UI-02 — tokens, focus and Chinese composition

Open [fixture.html](fixture.html). This is a research example, not a production
editor or a complete DTCG implementation.

## Resolver

The supported subset is sRGB color objects, px/rem dimensions and whole-token
curly aliases. Explicit types, alias-derived types and nearest parent/root
group types use one validation path. Invalid raw name segments, incompatible
alias types, invalid values, missing targets and cycles fail explicitly. Other
token/color types and property-level/JSON Pointer aliases are unsupported.

```bash
python -B resolver_negative.py
```

Twenty controls passed again in the 2026-11-17 22:48 UTC
[closure run](../../../docs/audit/closure-20261118/runtime/foundation-final-run/RESULT.json):
original 14-token fixture, resolution ordering/defaults, genuine alias type
conflicts, valid alias and root-type inheritance, illegal dotted-name collision,
document-entry validation, legal names containing an interior dollar/space,
invalid values, cycle/missing references and modifier inputs. Official subset
rules are linked in the source.

## Browser check and measured result

```bash
python -B cdp_ime_test.py
python -B _check.py
```

The CDP driver launches fresh Chrome, follows four real Tab inputs to compose,
checks visible focus, sends once before a same-page reset, then uses CDP to
exercise a browser composition session. Enter during composition must send
zero times; after commit, one Enter must send exactly once with
`isComposing=false`. Unknown observations fail. Reset clears both the closure
and window counters.

The 22:48 UTC Windows run used Chrome 157.0.8103.79 and returned exit 0. Its
[fresh CDP evidence](../../../docs/audit/closure-20261118/runtime/foundation-final-run/ui02-ime.json)
records:

- Four Tab inputs reached name, email, toolbar-bold and compose with visible focus.
- A same-page reset changed the send counter from 1 to 0.
- Composition start/end were observed; sends during composition were **0**.
- A single Enter after commit produced a count of **1**, a delta of **1**, and
  `enterAfterComposition_isComposing=false`.

The subsequent 22:52 UTC
[targeted harness rerun](../../../docs/audit/closure-20261118/runtime/runtime-harness-rerun/RESULT.json)
printed **63 assertions** and exit 0 in two concurrent UI-02 subprocesses.
Each used an independent temporary profile; this is the recorded concurrency
case, not a general stress-test claim.

The case-local [IME report](evidence/ime_cdp_evidence.json) is an earlier passing
Windows run from 22:14 UTC, with its original timestamp and source bindings.
It is no longer a pending placeholder. The later closure CDP report above is
separately preserved. `_check.py` refuses unbound or nonpassing evidence; a
future fixture/driver/support change requires a new bound report before the
changed version is treated as verified.

Cloud Chromium's earlier socket-permission failure remains historical. The
original pre-repair JSON remains [archived](evidence/history/ime_cdp_evidence-original.json),
and the [historical accepted receipt](evidence/receipt.json) is unchanged.

Dependencies: Python 3.10+, `jsonschema`, `referencing`, `websocket-client` or
`websockets.sync`, and Chrome via [shared discovery](../chrome_util.py).
No original profile or private dependency path is required.

CDP exercises the browser event layer. An OS-native candidate window, locale
specific IME behavior, complete keyboard accessibility, full Chinese
typography, WCAG conformance, human focus usability and human aesthetics remain
untested. CSS support and remaining typography gaps are retained in
[cjk_layout.json](cjk_layout.json).
