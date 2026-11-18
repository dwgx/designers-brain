# Stage B — C2 / P4R-C2-20261117T123432

## Provenance and context

- Root seal verified OK BEFORE reading instructions: A-SEAL byte sha == cue.root_seal_sha256; all identity fields, both manifest SHA references, three-way A-file SHA (READY/manifest/A-SEAL), tz-aware UTC ordering (issued 2026-11-17T12:41:48Z >= sealed observation), candidate HEAD/tree clean, and all 8 bound public-entrypoint SHA/bytes unchanged. Verification output showed 30/30 PASS, `VERIFY_OK`; cue.instructions was not exposed to the model until verification passed.
- CUE action: `continue`; source_snapshot = CAPABILITIES.json (0cfed044…) + conflicts.md (a5718276…), both still matching the bound hashes.
- hint_level: the cue is a bounded continuation directive (threshold provenance + run positive/negative/missing + channel labeling + A/A + static-limitation note). No new mechanism was supplied; it operates on the mechanism I sealed in A.

## New hint vs. what I already had

Newly requested in Stage B: (1) line-level provenance for every decision constant; (2) a nonzero-exit/FAIL-text runner for positive, broken, and missing-input cases; (3) explicit separation of text vs image counter-examples with no `image_seen`; (4) separation of the static zero-flicker claim from rendered-timing verification; (5) A/A repeat determinism. All are checks on the sealed A artifact; nothing in A was changed (A layout.json/layout.html/manifest.json SHA re-verified unchanged before and after Stage B).

## 1) Threshold / decision-constant provenance (file + line)

Every literal that drives a decision in `B/check_runner.py`, mapped to the final source actually adopted. Where a number is a self-declared design constant with no source threshold, that is stated — none is passed off as sourced.

| Constant / predicate | Value | Source (file + exact line) | Relation |
|---|---|---|---|
| three annotation roles = readable_data_value / illustrative_decoration / no_label_baseline | tuple | `knowledge/CAPABILITIES.json` L17837 (`roktim___.mechanism_summary`) | verbatim role vocabulary; the mechanism adopted |
| role evidence caveat, no human/reader claim | — | `knowledge/CAPABILITIES.json` L17839-17840 (limitations: fixture numbers not measurements; reader misinterpretation & design quality unmeasured; no image-generation service) | caps every claim as mechanical/declared |
| one owner per axis / role owned by exactly one slot (`role_ownership_table_complete`) | 3 roles, each once | `knowledge/cross/conflicts.md` L314-315 (N3: 每个轴只能有一个持有者) | N3 gives single-owner rule; I apply it to salience-slot ownership of roles. "3" is the count of sourced roles from CAPABILITIES L17837, not a fabricated threshold. |
| separable object classes -> explicit partition + per-part budget | predicate enabling 2 variants | `knowledge/cross/conflicts.md` L317-318 (N4: 可分的空间区域或对象类别 → 可拆，但必须写死分区表 + 掩膜定义) | justifies splitting by role class with an explicit binding table |
| motion/flicker budget field, per-layer cap | `max_frequency_hz <= 3` | task rule "不超过 3 Hz" (Goal L26) is the authority for 3 Hz; mechanism framing from `conflicts.md` L332-333 (N8: 运动预算字段, 分层拆分必须给掩膜与各层上限) and C-09 L166-177 (event-region vs field; per-layer Δ/angular caps) | 3 Hz is the user-stated constraint, NOT invented; my layout uses 0 flashing elements so it is satisfied trivially. N8/C-09 motivate expressing it as an explicit per-layer field. |
| flicker element counts = 0 | 0 | self-declared property of the chosen no-flicker scheme (Goal L26 explicitly permits a no-flicker solution) | design decision, not a sourced threshold |
| salience formula weights 0.45 / 0.25 / 0.30, contrast cap 7, accent +0.10, cap 1.0 | declared | NO source threshold exists for these numbers; they are my declared salience model, recorded as such in A/layout.json `salience_formula` and A/unaided-selection.json `still_missing_evidence` | self-declared; used only for mechanical reproducibility, explicitly NOT a perceptual measurement. The cue's "不得只凭自造常量" is satisfied by binding each of them here to "self-declared, unsourced, measured=nothing" rather than pretending a source. |
| `salience_budget_cap` check | cap from expectation (e.g. 0.8 in neg_budget) | break-test hook requested by cue item 6 (抬高 salience budget 超限) | Stage-B test parameter, not a product threshold |
| verification anchor count = 2 (one per variant) | 2 | `knowledge/domains/motion-graphics/cards/structure.md` L15-19 (收尾文案 = 一帧可验收的终点) + A/layout.json `verification_anchor` (2 variants) | "one anchor per frame" sourced; count 2 = two declared variants |
| banned temporal CSS tokens / no `<script>` | list | Goal L26 (禁高频闪烁) + determinism contract `templates/determinism_contract.md` C2-C5 L16-22 (no real-time clocks, no state-triggered CSS transitions) | static-enforcement of the no-flicker claim |
| top-salience slot must be S1 | S1 | derived: slot numbers in A/layout.json (`contrast_ratio` 7.2, `font_weight` 700, `area_fraction` 0.06, accent) make S1 the max under the declared formula; not a sourced absolute threshold | internal consistency of my own declared model |

Note on the cue's "不得只凭自造常量": the sourced constraints (roles, single-owner, separable classes, motion-budget framing, 3 Hz, anchor, no-flicker) are line-bound above. The salience weights are admitted self-declared model constants because the public sources supply no salience-number threshold; claiming otherwise would be false provenance. They are used only to make the declared contrast mechanically reproducible, never asserted as perceptual fact.

## 2) Checker execution results (stdout/exit consistent)

Tool source: `B/check_runner.py`, sha256 `46d9635503aa4ce0a194343254dc86334d65c952f55d5ce7213337bea12d42fb`. Predicates are A-identical to the sealed `A/check_layout.py` (sha `c68dcf16…`); Stage B adds correct exit semantics and the two break predicates.

| Case | argv (abbreviated) | exit | stdout verdict | Expected | Consistent? |
|---|---|---:|---|---|---|
| (a) positive = own layout | `python B/check_runner.py --input-dir B/cases/positive --out B/runs/positive.stdout.txt` | 0 | PASS, 16 checks, 0 failed | exit 0 + PASS | yes |
| (b1) known-fault: role ownership broken (`pure_style` S1 wrongly = readable_data_value) | `... --input-dir B/cases/neg_role ...` | 1 | FAIL, 15 checks, 2 failed (`pure_style_top_role_is_decoration`, `variants_differ_only_in_binding`) | nonzero + FAIL | yes |
| (b2) known-fault: salience budget over cap (cap 0.8, S1=1.0) | `... --input-dir B/cases/neg_budget ...` | 1 | FAIL, 16 checks, 1 failed (`salience_within_budget_cap`, over=['S1']) | nonzero + FAIL | yes |
| (c) missing input file | `... --input-dir B/cases/missing ...` | 2 | `ERROR: FileNotFoundError: ... layout.json` then `FAIL (input impossible to evaluate; no silent pass)`; stderr 0 bytes | nonzero, clean, no silent pass | yes |
| (5/A-A) positive repeat | `... --out B/runs/positive_repeat.stdout.txt` | 0 | PASS, 16 checks, 0 failed | same verdict as run 1 | yes |

Full stdout is in `B/runs/*.stdout.txt` and stderr in `B/runs/*.stderr.txt`. Input SHAs per run are printed in stdout. stdout verdict and exit code agree in every case (PASS↔0, FAIL↔1, missing-FAIL↔2).

## 5/A-A) Determinism and break test

- A/A: run 1 and repeat of the same positive layout produced identical decision lines (`[PASS]`/`[FAIL]`/`TOTAL`/`RESULT`), sha256 `f9a833bd708dfa4810c248a6430d8c768652d624f74dca33a6e9a32f2dffa20b` for both normalized decision files. The only raw-text difference is the echoed `--out` filename and the timestamp, neither of which is a decision.
- Break test: removing role ownership (b1) and raising the salience cap past the top slot (b2) each produced FAIL with exit 1. The predicate therefore discriminates rather than passing everything.

## 3) Counter-example channel labeling

- **Text/declared counter-example: PRESENT.** In A/layout.json and A/layout.html, the `pure_style` variant is a text/declared counter-example: identical palette/typeface/spacing/slot numbers, only the role→slot binding changed so illustration owns S1 and the data value drops to S2. Its expected verdict is FAIL under the role-ownership check (confirmed in A/check-output.json and B positive run where the check `pure_style_top_role_is_decoration` passes because the *variant* correctly demonstrates the failure mode).
- **Program-check counter-example: PRESENT and EXECUTED.** The broken-input cases b1/b2 are programmatic counter-examples; their FAIL outputs are recorded above.
- **Image counter-example: NOT PRESENT.** No image was generated, no image API was called, no browser/capture harness ran. `image_seen` = false / not applicable. I do not infer image availability from a text spec or a passing structural check. Per Goal L28 and CUE item 3, text counter-example, program check, and image counter-example are recorded as distinct channels.

## 4) Optional bounded reference

Not copied. CUE item 4 makes the historical repair checker (`SUP/C2-ROOT-REPAIR-R1/check_layout.py`, sha `a7274ea4…`) optional and explicitly non-penalized if skipped. I did not read or copy it; threshold provenance was derived from the public sources bound in this case (table in §1). No side effects to report from that option.

## 6) Static zero-flicker vs rendered timing — LIMITATION

The check `flicker_zero_elements` / `html_has_no_banned_temporal_tokens` verifies only that the delivered static HTML contains no scripting, CSS keyframes, transitions, timers, or temporal tokens, and that the declared flashing-element count is 0. This is a **static/declared** claim. It does NOT verify rendered-time behavior: I did not run a browser, capture frames, or measure a pixel difference across frames, so I cannot prove that a hypothetical future renderer would produce no flicker. Per CUE item 5 this is recorded as a limitation, not upgraded to a rendered-timing result. The ≤3 Hz constraint is satisfied by construction (0 flashing elements → 0 Hz) in the static artifact; rendered compliance remains `[UNVERIFIED]`.

## Scope of the result

This is a mechanical/declared mechanism demonstration under a constant style vocabulary. It does NOT show human reading-order improvement, aesthetic acceptance, E2/E3 promotion, real image-generation output, or full-library effect. Applied only to candidate final_commit c35d748e…/tree fb24565b… and case C2.
