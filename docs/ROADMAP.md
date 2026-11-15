# Roadmap

English · [中文](i18n/zh-CN/ROADMAP.md) · [日本語](i18n/ja/ROADMAP.md)

## Where we are — PRE milestone (2026-10)

- **Domain #1 — painters**: 76 dossiers (~300–600 lines each) + 2044 sourced quotes + 739 sourced artworks (**701 public-domain/CC0 + 38 openly licensed, attribution per image** — see [`NOTICE.md`](../NOTICE.md#images-not-pdcc0-38)) + 76 composable module cards (228/228 verbatim checks). *(PRE-milestone figures kept for the record: 62 dossiers / 1613 quotes / 618 images — the 618 were previously described as all PD, which is wrong for 38 of them / 62 cards / 186 checks.)*【测量对齐注记 2026-11-16 · H4CandidatePrep】本行沿用 source@f008952 既定文案，其 735/697 为 wave23 补足 4 张（klimt ×3、turner ×1）落地前的快照漂移；候选树实测 images=739 / PD+CC0=701 / open=38（tools/check_library_counts.py），按 Main S16 ruling 对齐为 739/701；checker 常量未改。
- **Domain #2 — motion graphics**: 15 style cards distilled from `mg-styles-15` (MIT) + origin transcript + reference pipelines (HTML / Blender).
- **Skill**: `designers-brain` v0.2 — built, activated (junctions + packaging), RED-GREEN blind test PASS, full walkthrough (café identity, 3 directions) with gate file and independent review.
- **Experiments**: style-separation 7/7 resolved (`E1_t1b/c`), composition batch 9/9 (`E2_t1`), three end-to-end animation pipelines verified (web ×2, Blender ×1).
- **Repo**: public release with trilingual docs (EN / zh-CN / ja) and AI-ops protocols.

## Phase 1 — depth (near term)

- Human six-dimension scoring of E-series outputs → calibrate style fidelity & fusion quality.
- **E3** intensity sweep (30 / 50 / 75 / 100%) for painter modules — the "tunable strength" promise is currently `[UNVERIFIED]`.
- **E4** theme transfer (beyond the storm-lighthouse theme) across modules.
- End-to-end tests for the remaining motion-graphics cards (12 of 15).
- Painter batch 2 candidates (Turner, Klimt, Rembrandt, …) per `knowledge/domains/painters/dossiers/expansion.md`.
- Blender determinism P1 → P0 exploration; audio pacing / mastering study.

## Phase 2 — breadth (new domains)

- Expand via the registry contract (`docs/ARCHITECTURE.md` §3.2): candidates — photography, cinematography, typography, product/industrial design, sound design.
- Each domain: sources → dossiers → modules → conflict list → experiments → skill registration.

## Phase 3 — platform

- Community contributions (see `CONTRIBUTING.md`), issue templates, tagged releases.
- Skill distribution via plugin marketplace once interfaces stabilize.
- Additional languages for docs and README.

## Principles (fixed)

- Evidence grades on every claim; no claim without a runnable check.
- Pipelines transfer across models; **style mechanisms must be rewritten with matching mechanical checks** (verified finding).
- Style segments must be separable from subject matter (verified 7/7).
- AI-operated under `docs/PROTOCOLS.md`; work state in `ops/GOALS.md`.

## Known gaps

- Intensity response unverified (E3 not yet run) — marked `[UNVERIFIED]` wherever relevant.
- Human aesthetic scoring pending (mechanical checks and single-reviewer inspection only so far).
- Blender bit-exactness not demonstrated (honest ceiling: P1, ≤0.05% pixels).
- Audio: synthesis works; beat-sync precision and mastering remain open.
