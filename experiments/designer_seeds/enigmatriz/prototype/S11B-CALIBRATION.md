# S11 §B — bounded claim calibration (enigmatriz prototype)

> Author `SeedDepsRevisit` · S11 §B calibration r1 · status `submitted` · research-grade stays research-grade.
> This is a CLAIM-LEVEL calibration of the EXISTING prototype. No experiment is re-run, extended, or added.
> The frozen `config.json`, `build.py`, `outputs/`, `rerun_20261115/`, `run_evidence.json`, `runner_receipt.json`
> bytes are PRESERVED UNCHANGED (the supervisor's independent 11/11 byte-identical reproduction still holds).
> Parent E2/E3/active states, parent receipts/gates, and reviewer-owned `review-*` files are NOT touched here.

## 1. Receipt binding — recomputed from actual bytes (record both values honestly)

The S11 §B gate finding is a reviewer-side binding error. This document records BOTH values honestly;
it does NOT edit the reviewer-owned `review-gate-receipt.json` (that fix belongs to `ReviewGateSeedProto`).

Recompute command (run this session, read bytes, not hand-copied):

```
python -c "import hashlib;print(hashlib.sha256(open(r'<RUN_ROOT>/staging/SEED-EXPERIMENT-enigmatriz/prototype/receipt.json','rb').read()).hexdigest())"
```

| Field | Value | Status |
|---|---|---|
| `review-gate-receipt.json` `review.reviewed_artifact_hashes[0]` (RECORDED by reviewer) | `d23093dd89ed6ee7f1f5885e02f3ba2c7f583bc62a488b07e11dc8bbbf02b0ee` | WRONG — does not equal any author receipt bytes; looks like a hand-copy/transcription error of the value below (both begin `d23093dd89ed6ee7`). |
| `review-gate-receipt.json` `input_hashes[0]` for author `receipt.json` (RECORDED by reviewer) | `d23093dd89ed6ee79e1d7d7ba01675953417b5b34d4060334a5b4595a4b47a35` | Was the correct byte-SHA of the author receipt BEFORE this calibration. |
| author `receipt.json` byte-SHA BEFORE this calibration (recomputed from bytes) | `d23093dd89ed6ee79e1d7d7ba01675953417b5b34d4060334a5b4595a4b47a35` | Matches S11 §B.2 "actual author receipt SHA" and the reviewer's `input_hashes[0]`. |
| author `receipt.json` byte-SHA AFTER this calibration (recomputed from bytes — FINAL) | recorded in `verify-receipt.out` footer + `SEED-DEPS-REVISIT/assessment.md` §S11B | This is the binding `ReviewGateSeedProto` must now recompute from the current bytes. |

The corruption is in `reviewed_artifact_hashes[0]` only; `input_hashes[0]` was correct for the pre-calibration
bytes. Because this calibration edits the author `receipt.json` (to refresh README/RESULT artifact hashes and
add this addendum as a bound artifact), the correct binding value is now the FINAL byte-SHA recorded in
`verify-receipt.out`, NOT the old `d23093dd…`. The waiting gate must re-read the file bytes and compute it —
never hand-copy a digest. The old recorded value `f1f5885e…` and the old recomputed value `d23093dd…` are
both kept above so the discrepancy is auditable; the gate re-verifies against the final bytes.

## 2. Config honesty — what the config actually does vs what was claimed

- `config.json` is the **FINAL run config plus a post-hoc correction record**, NOT a provably frozen
  pre-registration. Its `intended_checks_before_run` (C3) already embeds the OBSERVED Pearson values
  (`+0.8795 / -0.8990`), and `observed_after_run.note_on_honesty` explicitly states the originally drafted
  "normal expected negative / reversed positive" wording was corrected to match what the code implements
  (bright→dense). Use it as the final run config + historical correction record; do NOT grant it
  pre-registered evidence status. README previously called it a "PRE-RUN config" — that label is corrected here.
- What the config actually drives: a synthetic 120x60 grayscale chart, ONE explicit axis-aligned mask
  rectangle (8,8–72,52), 10x5 grid of 12px cells, a MEASURED glyph-coverage ramp (Consolas declared by
  path+sha256, not redistributed), normal + reversed mapping, and MetricPilot numeric interfaces on the
  synthetic chart. It does NOT implement an automatic mask toolchain, the artist's algorithm, or any
  general mask-safety proof.
- `build.py` C4 `pass` is a **constant `True`** (see `build.py` checks dict, `C4_selected_region_checks`).
  It is NOT an independent general mask validator. The only mask evidence actually produced is for THIS
  declared rectangle: outside-mask pixel difference = 0 (recomputed by the supervisor: 4275 outside-mask
  pixels, chart↔normal / chart↔reversed / normal↔reversed all 0). No other mask was tested. Consumers must
  not read the single boolean as a universal validator.

## 3. Claim bounds (unchanged from the preserved experiment)

Only the implemented selected-region/quantization mechanism on synthetic input is supported. Reversal is a
CONTROL, not an aesthetic failure. NOT E2/E3 evidence, NOT a validated reproduction, NOT an E3 success, NOT
the artist's algorithm, NOT human "looks like enigmatriz". Aesthetic judgement stays `pending_human`.
Seed stays E1; no E2/E3/active promotion. Pearson / lum_hist / lap_var numbers come from the synthetic
chart only; NO dossier threshold was applied to any artwork.

## 4. What was NOT done (bounded scope)

- No new experiment, no new mask, no new font, no new output image, no image API, no network, no credentials.
- No change to parent `state.md`, parent receipts, `review-*` reviewer files, E2/E3/active gates.
- No promotion; S09 acceptance remains PAUSED.

---

`verify-receipt.py` (PKG tool SHA `00ef6071ed8b021b049569b3cfbead45238fff1f0a9e2ecbe787c614af767bd0`,
schema SHA `c553112d336e66e03639f7a569abd8f9b8ddc0707a5b3667ecd9d355a9a1fb31`) is run on the final
`receipt.json` (status `submitted` → schema-only validation, `verify-receipt.py:20-21`); result saved in
`verify-receipt.out`. Tool/schema DO exist in the sealed PKG (correcting the earlier reviewer "tool_absent"
claim — that correction is the reviewer's to make in its own files).
