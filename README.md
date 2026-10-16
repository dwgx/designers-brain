# Designers_Brain

> **A brain for designers.** Deep-research distillation of artists' and designers' visual languages into composable, verifiable modules — packaged as an agent skill that **asks before it designs**.

English · [中文](README.zh-CN.md) · [日本語](README.ja.md)

[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE-CODE)

## What this is

Give this repository to an AI agent and it becomes a design consultant: it asks the right questions first, recommends styles from a distilled library, checks conflicts before combining, and produces output with evidence — image prompts, 10-second web animations, or Blender briefs.

Inside:

- **62 painter dossiers** (da Vinci, Michelangelo, Van Gogh, Monet, Picasso, Cézanne, Matisse, Hokusai, Caravaggio, Vermeer, Dürer) — ~300–600 lines of evidence each, 1613 sourced quotes, 618 public-domain artworks.
- **62 composable module cards** + **15 motion-graphics style cards** (10-second animation skeletons).
- **Cross-module rules**: 18 conflict entries (C-01–C-18) + composition rules N1–N9.
- **A skill** (`skills/designers-brain/`) implementing the ask-first consultant protocol.
- **Experiments with mechanical checks**: style-transfer matrices (E-series) and three end-to-end animation pipelines (web ×2, Blender ×1).

## Quickstart

### 1. Load the skill

```bash
# Claude Code / Codex / omp — activate via junction (no copy):
# (Windows PowerShell)
New-Item -ItemType Junction -Path "$HOME\.claude\skills\designers-brain" `
  -Target "<path-to-repo>\skills\designers-brain"
```

Then just ask for design work: *"Help me pick a style and produce a poster for …"* — the skill triggers on design/replacement requests. Plugin manifests are included for packaging (`.claude-plugin/`, `.codex-plugin/`, `.agents/plugins/`).

### 2. Browse the knowledge

- Start at [`knowledge/INDEX.md`](knowledge/INDEX.md) (full source index).
- Painter modules: [`knowledge/domains/painters/modules/`](knowledge/domains/painters/modules/) — each card is directly composable into a prompt.
- Motion styles: [`knowledge/domains/motion-graphics/`](knowledge/domains/motion-graphics/).
- Composition rules: [`knowledge/cross/conflicts.md`](knowledge/cross/conflicts.md).

### 3. Reproduce an experiment

```bash
# module-card verbatim check (186 checks)
python knowledge/domains/painters/modules/_extract.py --check

# image experiment verification (example: composition batch)
cd experiments/E2_t1 && python _verify_e2.py
```

## How it works

1. **Deep research** — primary sources per artist/domain; every claim carries an evidence grade (`[自述]/[史料]/[研究]/[归纳]/[推测]`).
2. **Distillation** — evidence compresses into operational rules: modules that can be composed, tuned, and mechanically checked.
3. **Verification** — every capability is exercised end-to-end before it is claimed; verifiers ship with the artifacts.
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

**PRE milestone complete** (2026-10): first two domains distilled, skill built and blind-tested, three pipelines verified end-to-end. Next: domain expansion, intensity sweeps, human scoring — see [`docs/ROADMAP.md`](docs/ROADMAP.md).

## License

Content & docs: [CC BY 4.0](LICENSE). Code: [MIT](LICENSE-CODE). Third-party: see [NOTICE.md](NOTICE.md).
