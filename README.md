# Designers_Brain

> **A brain for designers.** Deep-research distillation of artists' and designers' visual languages into composable, verifiable modules — packaged as an agent skill that **asks before it designs**.

English · [中文](README.zh-CN.md) · [日本語](README.ja.md)

[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE-CODE)

## What this is

Give this repository to an AI agent and it becomes a design consultant: it asks the right questions first, recommends styles from a distilled library, checks conflicts before combining, and produces output with evidence — image prompts, 10-second web animations, or Blender briefs.

Inside:

- **76 painter dossiers** (da Vinci, Michelangelo, Van Gogh, Monet, Picasso, Cézanne, Matisse, Hokusai, Caravaggio, Vermeer, Dürer, …) — ~300–600 lines of evidence each, 2044 sourced quotes, 739 sourced artworks: **701 public-domain/CC0 images + 38 openly licensed images that carry per-image attribution requirements** (see [NOTICE.md](NOTICE.md)). *(PRE-milestone counts, kept for the record: 62 dossiers / 1613 quotes / 618 images — the image total was previously described as uniformly public-domain, which is not accurate for 38 of the 739.)*
- **76 composable module cards** + **15 motion-graphics style cards** (10-second animation skeletons). *(PRE: 62 cards.)*
- **Cross-module rules**: 18 conflict entries (C-01–C-18) + composition rules N1–N9.
- **A skill** (`skills/designers-brain/`) implementing the ask-first consultant protocol.
- **Experiments with mechanical checks**: style-transfer matrices (E-series) and three end-to-end animation pipelines (web ×2, Blender ×1).

- **76 learning paths and 65 new style candidates**, with source claims, counterexamples and [concrete reading routes](knowledge/domains/painters/learning/INDEX.md). Eleven existing style sections remain linked to their original cards.
- **An evidence-scoped [capability matrix](knowledge/CAPABILITIES.md)**: image, web10s and Blender are assessed separately, with historical, partial and untested results distinguished.

## Quickstart

### 1. Load the skill

Open the repository and let your agent read [`skills/designers-brain/SKILL.md`](skills/designers-brain/SKILL.md). Resolve its actual repository root before following its references:

```text
python -X utf8 -B skills/designers-brain/resolve_repo.py --json
python -X utf8 -B docs/skill/_selfcheck.py --repo-only
```

For OMP, use the host's `skills.customDirectories` entry pointing at this checkout's **`skills` parent directory**. See [local loading and source checks](docs/skill/local-usage.md) for the configuration and real `skill://` reads. Other hosts have their own discovery/install mechanisms; one host's junction is not a shared installation for all hosts.

Then give a concrete design brief, for example: *"Help me pick a style and prepare a poster for …"*. The skill asks for missing requirements and reads the capability matrix before promising an output route. Host discovery, automatic selection and successful rendering are separate checks.

### 2. Browse the knowledge

- Start at [`knowledge/INDEX.md`](knowledge/INDEX.md) (full source index).
- Painter modules: [`knowledge/domains/painters/modules/`](knowledge/domains/painters/modules/) — each card is directly composable into a prompt.
- Motion styles: [`knowledge/domains/motion-graphics/`](knowledge/domains/motion-graphics/).
- Composition rules: [`knowledge/cross/conflicts.md`](knowledge/cross/conflicts.md).

### 3. Reproduce an experiment

```bash
# module-card verbatim check (228 checks — 76 cards × §8.1/§8.2/§4)
python knowledge/domains/painters/modules/_extract.py --check

# image experiment verification (example: composition batch)
cd experiments/E2_t1 && python _verify_e2.py
```

## How it works

1. **Deep research** — primary sources per artist/domain; every claim carries an evidence grade (`[自述]/[史料]/[研究]/[归纳]/[推测]`).
2. **Distillation** — evidence compresses into operational rules: modules that can be composed, tuned, and mechanically checked.
3. **Verification** — record the exact output route, implementation, checks and limits. The capability matrix separates supported, conditional, unsupported and untested claims; historical verifiers retain their original scope.
4. **AI operations** — the repo is operated by AI agents under explicit protocols (`docs/WORKFLOW.md`, `docs/PROTOCOLS.md`); work state lives in `ops/GOALS.md`.

## Repository map

```
knowledge/    distilled product (domains, cross rules, agent-art pipelines, index)
experiments/  evidence runs (E-series, animation tests) with scripts & verifiers
skills/       designers-brain — the consumable agent skill
docs/         architecture, workflow, protocols, roadmap (+ zh-CN / ja translations)
ops/          GOALS.md (work queue) · OPS-LOG.md (append-only log)
templates/    module / style-card / determinism / design-brief templates
```

## Demo artifacts

- Animation pipelines: `experiments/anim_test_01/out.mp4` · `anim_test_02/out.mp4` · `anim_test_03_blender/out.mp4`
- Style-separation comparison: `experiments/E1_t1b/compare_all_t1b.png`
- Composition sheet: `experiments/E2_t1/sheet_all_e2.png`
- Skill walkthrough (café identity, 3 directions): `docs/skill/walkthrough_01/candidates/compare_candidates.png`

## Status

The November 2026 research update integrates learning paths, style candidates, source-linked navigation and per-output capability states. See [CAPABILITIES](knowledge/CAPABILITIES.md) for what existing evidence supports. Learning exercises and textual style rules do not by themselves establish image generation, browser rendering, Blender execution or measured learning benefits.

The October PRE milestone remains a historical record. Current release acceptance is recorded against exact versions in the release notes; this working tree and a local commit do not establish publication. Remaining research directions are in [`docs/ROADMAP.md`](docs/ROADMAP.md).

## License

Content & docs: [CC BY 4.0](LICENSE). Code: [MIT](LICENSE-CODE). Third-party: see [NOTICE.md](NOTICE.md).

Image licensing is **not** uniform: of the 739 sourced artworks, 701 are public-domain or CC0, and 38 are openly licensed (CC BY 3.0/4.0, CC BY-SA 3.0/4.0, ColBase terms, NPM open data) and **must keep their per-image credit lines** when redistributed. Categories and attribution requirements: [NOTICE.md](NOTICE.md#images-not-pdcc0-38).
