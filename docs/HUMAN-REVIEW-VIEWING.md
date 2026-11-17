# Human review — 23 empty scoring positions

The original private scoring table contains **23 positions: 22 experimental cells plus one optional baseline**, grouped as 12 + 7 + 1 + 3. Its E1 heading says “12 cells + baseline”, but the actual E1 table has **11 styles plus the optional baseline**. The table rows, not that historical heading, determine this count. All five primary score columns remain empty. Original table SHA-256: `b501d5f5922f9ccb53f3c5c989e7d054a05dd68446fe29fbf60a3acdaed4e156`. The private original is unchanged.

## View and score

Score composition, form, color, brushwork/texture and mood from 1–5; leave uncertain cells blank. Prompt-change responsiveness is an E3-only dimension and is N/A for this set. Record failure modes and overlapping styles separately. Use the [blank public worksheet](HUMAN-REVIEW-SCORES.md) or your private table. Model review never supplies a human score.

| Group | Position | Actual image | Additional question |
| --- | --- | --- | --- |
| E1_t1 | e0_baseline | [sheet_e0_baseline.png](../experiments/E1_t1/sheet_e0_baseline.png) | Optional reference |
| E1_t1 | e1_caravaggio | [sheet_e1_caravaggio.png](../experiments/E1_t1/sheet_e1_caravaggio.png) | Failure mode / overlapping style |
| E1_t1 | e1_cezanne | [sheet_e1_cezanne.png](../experiments/E1_t1/sheet_e1_cezanne.png) | Failure mode / overlapping style |
| E1_t1 | e1_da_vinci | [sheet_e1_da_vinci.png](../experiments/E1_t1/sheet_e1_da_vinci.png) | Failure mode / overlapping style |
| E1_t1 | e1_durer | [sheet_e1_durer.png](../experiments/E1_t1/sheet_e1_durer.png) | Failure mode / overlapping style |
| E1_t1 | e1_hokusai | [sheet_e1_hokusai.png](../experiments/E1_t1/sheet_e1_hokusai.png) | Failure mode / overlapping style |
| E1_t1 | e1_matisse | [sheet_e1_matisse.png](../experiments/E1_t1/sheet_e1_matisse.png) | Failure mode / overlapping style |
| E1_t1 | e1_michelangelo | [sheet_e1_michelangelo.png](../experiments/E1_t1/sheet_e1_michelangelo.png) | Failure mode / overlapping style |
| E1_t1 | e1_monet | [sheet_e1_monet.png](../experiments/E1_t1/sheet_e1_monet.png) | Failure mode / overlapping style |
| E1_t1 | e1_picasso | [sheet_e1_picasso.png](../experiments/E1_t1/sheet_e1_picasso.png) | Failure mode / overlapping style |
| E1_t1 | e1_van_gogh | [sheet_e1_van_gogh.png](../experiments/E1_t1/sheet_e1_van_gogh.png) | Failure mode / overlapping style |
| E1_t1 | e1_vermeer | [sheet_e1_vermeer.png](../experiments/E1_t1/sheet_e1_vermeer.png) | Failure mode / overlapping style |
| E1_t1b | e1_caravaggio | [compare_e1_caravaggio.png](../experiments/E1_t1b/compare_e1_caravaggio.png) | Was subject bias removed? |
| E1_t1b | e1_cezanne | [compare_e1_cezanne.png](../experiments/E1_t1b/compare_e1_cezanne.png) | Was subject bias removed? |
| E1_t1b | e1_da_vinci | [compare_e1_da_vinci.png](../experiments/E1_t1b/compare_e1_da_vinci.png) | Was subject bias removed? |
| E1_t1b | e1_durer | [compare_e1_durer.png](../experiments/E1_t1b/compare_e1_durer.png) | Was subject bias removed? |
| E1_t1b | e1_michelangelo | [compare_e1_michelangelo.png](../experiments/E1_t1b/compare_e1_michelangelo.png) | Was subject bias removed? |
| E1_t1b | e1_picasso | [compare_e1_picasso.png](../experiments/E1_t1b/compare_e1_picasso.png) | Was subject bias removed? |
| E1_t1b | e1_vermeer | [compare_e1_vermeer.png](../experiments/E1_t1b/compare_e1_vermeer.png) | Was subject bias removed? |
| E1_t1c | michelangelo_v2 | [compare_michelangelo_v2.png](../experiments/E1_t1c/compare_michelangelo_v2.png) | Improved / same / worse vs v1 |
| E2_t1 | e2a_monet_van_gogh | [sheet_e2a_monet_van_gogh.png](../experiments/E2_t1/sheet_e2a_monet_van_gogh.png) | Were conflicting standards silently combined? |
| E2_t1 | e2b_da_vinci_caravaggio | [sheet_e2b_da_vinci_caravaggio.png](../experiments/E2_t1/sheet_e2b_da_vinci_caravaggio.png) | Were conflicting standards silently combined? |
| E2_t1 | e2c_monet_cezanne | [sheet_e2c_monet_cezanne.png](../experiments/E2_t1/sheet_e2c_monet_cezanne.png) | Were conflicting standards silently combined? |

## Overviews and scope

- [E1 overview](../experiments/E1_t1/sheet_all.png)
- [Style-only comparison](../experiments/E1_t1b/compare_all_t1b.png)
- [Composition overview](../experiments/E2_t1/sheet_all_e2.png)
- [Consumer evidence](skill/consumer-evidence.md), [UI research fixtures](../examples/ui/README.md), and [motion gallery](../experiments/motion_closure/gallery/index.html) are separate deliverables.

Each image experiment retains its original verification outputs and SHA manifest. These 23 positions assess the historical image experiment configurations, not 23 artists or 23 reviewers. They do not establish or block the code/checker results. Human completion remains `pending_human` until a real person supplies the ratings.
