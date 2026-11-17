# Retrieval log — C2 / P4R-C2-20261117T123432 — Stage A unaided

Author clock (start of retrieval) UTC: 2026-11-17T12:35:05.698840+00:00
Author clock (after retrieval) UTC: 2026-11-17T12:36:20.568553+00:00
Clock source: local python datetime; self-reported, not a Root observation.

Preconditions actually checked BEFORE reading any knowledge content:
1. Goal file sha256 = a2777c12cf9c3314050e07f962c95b5de506bdf3dbe2bac233dde2e9075d6444 (matches binding in task).
2. consumer-binding-C2.json sha256 = 075913f4571eecdc3194227d576cc4a37c76228e6c4bbb5a6d4fea9f44bfa351; status=bound; case C2 / attempt P4R-C2-20261117T123432 / candidate_root / final_commit c35d748e1cc9f23415fff0bf019a9c03234c421e / final_tree fb24565b02597057784cbeed23f70ba657711804 all consistent with Goal.
3. Candidate repo itself (git -C <candidate>): HEAD=c35d748e1cc9f23415fff0bf019a9c03234c421e, tree=fb24565b02597057784cbeed23f70ba657711804, status --porcelain EMPTY (clean).
4. All 8 public entrypoints recomputed sha256 + bytes match the binding exactly (no null/placeholder/empty arrays).
No version mismatch; proceeded. No parent-directory HEAD was substituted.

Actual read order (only what was actually done):

1. knowledge/INDEX.md (whole, 96 lines). sha d4688562..., 6834 B.
   - Got: 15-card MG prompt system overview; L79-95 pointer sections DB-PUBLIC-KNOWLEDGE (learning + style candidates) and G5-CAPABILITIES. Locators to the two domain INDEX files and CAPABILITIES.md.
   - Still undecided: which mechanism fits a NEW subject with unclear hierarchy.

2. knowledge/domains/painters/style_candidates/INDEX.md (whole, 93 lines). sha 23f73d35..., 7661 B.
   - Got: L1-3 explicit boundary '候选、反例及能力增量分别保留... 纸面反例不等于实际图像实验' (paper counter-example != image experiment); 65 style drafts are draft/not E4; 11 legacy §8.1b entries.
   - Still undecided: how to build a refuting contrast without claiming an E4/image result.

3. knowledge/CAPABILITIES.md (whole, 144 lines). sha d928a281..., 16612 B (matches binding exactly).
   - Got: state legend L7-12 (supported/conditional/unsupported/untested); L16 supported=0, conditional=28; L124-134 seven designer seeds including roktim___ 'Synthetic SVG annotation roles separating readable data values, illustrative decoration and no-label baseline'; all painter image=untested.
   - Still undecided: is the roktim role-separation a usable mechanism or only a paper note? Followed pointer to CAPABILITIES.json for basis.

4. knowledge/domains/motion-graphics/cards/structure.md (whole, 53 lines). sha dd4321f3..., 4529 B.
   - Got: L8-19 four-part skeleton; L13 rules are '可验收的量化/物理约束', L16-17 anti-degeneration '别做成' segment; L21-29 why effective (quantified rules, plan->execute->verify, verification anchor); L36-45 Lane A/B isomorphism.
   - Still undecided: the exact mechanism; but 'quantified rules + anti-degeneration + anchor' became the shape of my check.

5. knowledge/domains/painters/learning/INDEX.md (whole, 133 lines). sha c24e16e7..., 13423 B.
   - Got: L1-3 '建议练习不是已验证的学习效果'; L39-50 cross-author comparison axes; complete 76-path table.
   - Still undecided: not directly used for the mechanism; confirms no learning claims allowed.

6. skills/designers-brain/references/output-forms.md (whole, 18 lines). sha ea98a0bb..., 1208 B.
   - Got: pointer-only; templates/style_card.md, determinism_contract.md, transfer_guide.md; L8 '读法：出稿前按形态核对必带字段'.
   - Still undecided: followed the two template pointers.

7. knowledge/cross/conflicts.md (targeted reads: headings via grep; C-08 L151-164; C-09 L166-177; N-rules L303-340; near-miss L344-360). sha a5718276..., 66241 B.
   - Got: C-09 L170-177 van Gogh star flicker period 0.8-1.5s (0.67-1.25 Hz, passes 3Hz) BUT full-field motion vs single event; N3 axis ownership table; N4 separable-by-object-class + partition table; N8 motion budget field; N9 verification anchor.
   - This is where the decisive mechanism crystallized: N4 lets separable OBJECT CLASSES be split with an explicit ownership table; a role-based hierarchy is such a split. C-09/N8 gave the 'no temporal salience without a measured budget' reason to prefer no flicker.

8. templates/determinism_contract.md (L1-40, C1-C10). sha 15628b05..., 11817 B. (located from output-forms.md L6)
   - Got: C1-C8, esp. C2 pure function of t, C3 no real-time clocks, C5 no state-triggered CSS transitions, C4 seeded randomness only. A static layout trivially satisfies these with 0 animated frames.

9. templates/style_card.md (headings grep: L1-24 card structure, L188 combination notes). sha f2cc36a7..., 17696 B. (located from output-forms.md L5)

10. knowledge/domains/painters/style_candidates/aivazovsky/style_only_draft.md (L1-7, L22-52). sha b0574794..., 23609 B. (located from style_candidates/INDEX.md L7)
    - Got: concrete example of a relationized 'pure style' draft; L1-7 marks status=draft, E4-unexecuted, '[归纳]' not pixel-measured; L22-52 role-ish R1-R8 relations. Confirms any 'pure style' artifact here is a paper draft, not validated.

11. knowledge/CAPABILITIES.json (targeted: roktim___ entry ~L17828-17841 via grep). sha 0cfed044..., 981803 B.
    - Got: mechanism_summary (annotation roles separating readable data / illustrative decoration / no-label baseline), limitations (fixture numbers not measurements; reader misinterpretation & design quality unmeasured), E1, local_visual_output_count=10 but 'submitted' prototype, parent_goal_satisfied=false.
    - Decided: roktim's role separation is the intended MECHANISM, but its numbers are declared/unmeasured -> my contrast must be mechanical, not a human reading test.

12. skills/designers-brain/SKILL.md (L75-94 '怎么出'). sha f1c19ddc..., 11550 B. (located from output-forms.md L8 pointer to SKILL.md)
    - Got: three output forms; web brief requires deterministic contract; '出稿后按 review_rubric 走独立评审'. Confirms a layout + spec + check is a legitimate checkable deliverable.

Operations NOT performed (do not claim): no image-generation call, no network probe, no install, no browser/capture harness, no large render, no read of any Root Control file / CUE / old consumer record / fixture / hidden answer / reviewer verdict, no scan of other sessions or projects, no git write.

Verification reconciliation: an early hand-transcription had written CAPABILITIES.md bytes as 16616; re-check with wc -c, stat and python len all returned 16612, matching the binding. The 16616 value was a transcription slip, corrected in both A files before sealing. sha256 (d928a281...) matched the bound hash throughout. All 8 entrypoints match both sha256 and bytes.

What I still cannot decide from public material alone (carried honestly into unaided-selection.json):
- Actual human reading order / aesthetic quality: no channel, no human test; roktim limitations explicitly say unmeasured.
- Whether the declared salience weights correspond to real perceptual salience.
- Whether an image channel exists: CAPABILITIES.md says supported=0 and painter image=untested.
