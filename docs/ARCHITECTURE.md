# Architecture

English · [中文](i18n/zh-CN/ARCHITECTURE.md) · [日本語](i18n/ja/ARCHITECTURE.md)

> Designers_Brain distills the working languages of artists and designers into composable, verifiable modules that AI agents can execute — and packages them as a skill any agent can load. Give the repo to an agent; it asks first, then designs and replaces with evidence.

## 1. The idea

Most "style prompts" are vibes. This project turns them into **engineering artifacts**:

- **Distillation** — for each domain (starting with painters), we read primary sources (works, letters, treatises, scholarship), extract the *operational rules* behind a visual language, and compress them into **modules** that can be composed, tuned, and verified.
- **Evidence grades** — every claim is tagged: `[自述]` (self-account / primary quote), `[史料]` (historical record), `[研究]` (research literature), `[归纳]` (our induction), `[推测]` (speculation). Grades travel with the claim into every downstream artifact.
- **Experiments** — every module gets exercised end-to-end (image generation, web animation, Blender scenes) with mechanical checks; unsupported claims stay marked `[UNVERIFIED]`.
- **The skill** — the distilled knowledge is packaged as an agent skill (`skills/designers-brain/`) that turns any capable agent into a design consultant: it asks the right questions first, recommends modules with conflict pre-checks, and produces output in one of three forms (image prompt / 10-second web animation / Blender brief).

The project's name is the ambition: a *brain for designers* — deep research per domain, expanding outward.

## 2. Repository layout

```
designers-brain/
├── README.md · README.zh-CN.md · README.ja.md   — public face (EN primary + translations)
├── LICENSE · LICENSE-CODE · NOTICE.md            — CC BY 4.0 (content) + MIT (code) + third-party notices
├── AGENTS.md · CLAUDE.md                         — entry points for AI agents
├── CONTRIBUTING.md                               — how to contribute (domains, cards, fixes)
├── docs/
│   ├── ARCHITECTURE.md · WORKFLOW.md · PROTOCOLS.md · ROADMAP.md
│   ├── MIGRATION.md                              — layout history (old → new paths)
│   ├── skill/                                    — skill design research: ecosystem study, spec, tests, walkthrough
│   └── i18n/zh-CN/ · i18n/ja/                    — translations of the four docs above
├── knowledge/                                    — the distilled product
│   ├── INDEX.md                                  — full source/image index
│   ├── domains/
│   │   ├── painters/       (dossiers/ + modules/) — domain #1: 11 painters
│   │   └── motion-graphics/ (cards/ + origin/ + sources/) — domain #2: 15 MG style cards
│   ├── cross/                                    — cross-domain rules: conflicts, transfer guide, review rubric, image channel
│   └── agent-art/                                — how agents make art with code: HTML/Blender pipelines, prompt corpus, evidence
├── skills/designers-brain/                       — the consumable skill (SKILL.md + references/ + domains.yaml)
├── experiments/                                  — evidence runs (E-series + animation tests), scripts included
├── templates/                                    — reusable templates (module, style card, determinism contract, design brief)
└── ops/                                          — AI-ops state: GOALS.md (work queue) · OPS-LOG.md (append-only log)
```

## 3. Knowledge model

### 3.1 Layers

```
sources ──▶ dossiers ──▶ modules / cards ──▶ skill (pointers only)
(quotes,     (full evidence    (operational,      (routing + protocols,
 images,      per artist,       composable)        never copies content)
 literature)  ~300 lines each)
```

- **Dossiers** (`knowledge/domains/painters/dossiers/`) — per-artist evidence files: visual fingerprint, technique rules, working principles, control parameters, quotes with citations, image manifest. 11 painters, each ~250–380 lines.
- **Modules** (`.../modules/`) — per-artist *module cards*: image prompt segment (§8.1 / §8.1b style-only), code-art rules (§8.2), control parameters (§4), conflict notes. Cards are mechanically extracted from dossiers (`_extract.py`, 33 verbatim checks).
- **Cross rules** (`knowledge/cross/`) — conflicts between modules (C-01–C-18), composition rules (N1–N9), the model transfer guide, review rubric, and image-channel documentation.
- **Skill** (`skills/designers-brain/`) — routes to the above by pointer; contains no duplicated content, so knowledge updates never need skill edits.

### 3.2 Domains & the registry contract

Domains are registered in `skills/designers-brain/domains.yaml`. A domain may be `active` only if it ships all of:

1. a card directory (one file per card, index consistent);
2. an index (capability map + composition notes);
3. a conflict list (or explicit reuse of the generic rules + domain deltas);
4. output-form mapping (image prompt / web animation / Blender — which are supported, and field differences);
5. an intensity mechanism (or an explicit gap marker);
6. evidence (experiments) or `[UNVERIFIED]` status;
7. a registry entry + self-check coverage.

Active domains: `painter` (11 modules), `mg-motion` (15 style cards). New domains (photography, typography, …) plug in by meeting the same contract.

### 3.3 Evidence grades

`[自述]` self-account (must carry a source) · `[史料]` historical record · `[研究]` research literature · `[归纳]` our induction · `[推测]` speculation. Unverified capabilities are marked `[UNVERIFIED]` and never promised as delivered.

## 4. The skill

- **Entry**: `skills/designers-brain/SKILL.md` (progressive disclosure: catalog → body → references).
- **Activation (local)**: junction into the harness scan path (`~/.agents/skills`, `~/.claude/skills`, `~/.codex/skills`); project-level `.agents/skills/` for repo-local sessions.
- **Distribution**: plugin manifests (`.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`).
- **Interaction protocol** (full text in the skill): first action is the **first-ask package** (business / audience / materials / style intent / replacement axis — 3+2 fill-in, defaults spoken aloud); ≤3 conversation rounds; visual decisions require *visible* candidates and stop after showing; a `design-brief.md` gate file records intent, assumptions, and approval scope.
- **Replacement semantics**: change content (keep skeleton) / change style (keep content) / tune intensity — with explicit locked sections per mode.
- **Output forms**: image prompt (channel: `grok-imagine-image-2.0` direct gateway; no negative-prompt channel; 768×1152), 10-second web animation brief (determinism contract C1–C10 + out-of-order rerun check), Blender brief (C9 + P1 determinism note).

## 5. Experiments

`experiments/` holds the evidence. Each experiment directory contains its scripts, raw request/response archives, outputs, and a verifier (`_verify*.py`) whose pass is the acceptance gate.

- `E1_t1*` — 12-cell style-transfer matrix: baseline, subject-bias diagnosis, style-only segment split (7/7 resolved).
- `E2_t1` — first composition batch (Monet×Van Gogh, da Vinci×Caravaggio, Monet×Cézanne): fusion works, conflict axes resolved either/or or by zoning.
- `anim_test_01/02/03` — three end-to-end pipelines verified with non-frontier models: pixel card (web), one-line card (web), 3D texture card (Blender). Key finding: *pipelines transfer, style mechanisms must be rewritten with matching mechanical checks*.

## 6. Operations (AI-ops)

This repo is **operated by AI agents**; the ops layer is first-class:

- `ops/GOALS.md` — single source of truth for work state (every item: status / goal / artifact path / owner + acceptance line).
- `ops/OPS-LOG.md` — append-only: channel status, incidents, lessons, authorization records.
- **The LOOP**: take goal → deep research → land artifacts (evidence-graded) → self-review → main-brain acceptance → queue new leads. Detailed in `docs/WORKFLOW.md`; hard rules in `docs/PROTOCOLS.md`.
- Machine-level dispatch boards live outside the repo (`~/.dwgx/ops/boards/`) — a board is a snapshot, never a source of truth.

## 7. Docs & i18n

- `docs/` is written in English (canonical). `docs/i18n/zh-CN/` and `docs/i18n/ja/` mirror `ARCHITECTURE / WORKFLOW / PROTOCOLS / ROADMAP`; the root README trio follows GitHub convention.
- Translations are reviewed for terminology consistency; when the English source changes materially, translations are updated or explicitly marked stale.
- Chinese remains the working language of raw research notes (dossiers, logs); the public interface is trilingual.

## 8. Extension points

- **New domain** → registry contract (§3.2) + `domains.yaml` entry + self-check coverage.
- **New output form** (e.g., print-ready poster, video) → add to output-form mapping with its mandatory fields + determinism/verification notes.
- **New pipeline** (e.g., Blender → web) → documented in `knowledge/agent-art/` with probes and a verifier.
- **New language** → mirror `docs/i18n/<lang>/` + README variant; add to the language switcher.

## 9. Non-goals

- Not a model-training project (no fine-tunes, no LoRA training — distilled knowledge is prompt/code-level).
- No redistribution of third-party media (videos, reference clips are excluded; see `.gitignore` and `NOTICE.md`).
- No claim without evidence grade; no "done" without a runnable check.
