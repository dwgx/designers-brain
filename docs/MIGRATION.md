# MIGRATION — Layout Refactor (2026-10-15)

> Purpose: record the pre-public restructure from the flat `research/*` layout to the
> public `knowledge / experiments / docs / ops` architecture. Path references in live
> documents were rewritten; historical logs (`ops/OPS-LOG.md`, `ops/session-digest.md`)
> keep old paths — consult the table below when reading them.

## 1. Why

The repo is going public and will keep expanding (more designer domains, deep research
per domain). The old layout mixed sources, distilled knowledge, pipelines, experiments
and ops state under one `research/` tree. New layout separates by role:

- `knowledge/` — distilled, reusable knowledge (the product)
- `experiments/` — evidence & validation runs (with scripts)
- `docs/` — architecture, workflow, protocols, i18n
- `ops/` — AI-ops state (goals, logs)
- `skills/` — the consumable agent skill
- `templates/` — reusable templates

## 2. Mapping (old → new)

| Old path | New path |
|---|---|
| `research/artists/` | `knowledge/domains/painters/dossiers/` |
| `research/prompts/artist_modules/` | `knowledge/domains/painters/modules/` |
| `research/agent-art/cards/{structure, mg-styles-15_compare, mg-styles-15_handbook, author_tutorial, video_shotcraft, video_shotcraft_handbook}.md` | `knowledge/domains/motion-graphics/cards/` |
| `research/agent-art/cards/{review_rubric.md, image_channel.md}` | `knowledge/cross/` |
| `research/agent-art/cards/_image_probes/` | `knowledge/cross/_image_probes/` |
| `research/agent-art/{conflicts.md, transfer_guide.md}` | `knowledge/cross/` |
| `research/agent-art/{html, blender, prompts, github, opus55}/` | `knowledge/agent-art/` |
| `research/origin_cards/` | `knowledge/domains/motion-graphics/origin/` |
| `research/source_video/` | `knowledge/domains/motion-graphics/sources/` |
| `research/experiments/` | `experiments/` |
| `research/skill/` | `docs/skill/` |
| `research/images_index.md` | `knowledge/INDEX.md` |
| `research/repo_standards.md` | `docs/notes/repo_standards.md` |
| `WORKFLOW.md` | `docs/WORKFLOW.md` (rewritten, EN) |
| `PROJECT.md` | retired → content folded into `docs/ARCHITECTURE.md` + `docs/ROADMAP.md` |
| `GOALS.md` | `ops/GOALS.md` |
| `OPS-LOG.md` | `ops/OPS-LOG.md` |
| `SESSION-DIGEST.md` | `ops/session-digest.md` |
| `AGENTS.md.before-agents15-20261015` | `ops/archive/agents-before-20261015.md` |
| `_tmp_picasso/` | `knowledge/domains/painters/_scratch/picasso/` (gitignored) |

## 3. Reference rewrite policy

- Live documents (knowledge, docs, skills, templates, experiments, ops/GOALS.md):
  all old path strings rewritten to new paths (single-pass, longest-first).
- Historical logs (`ops/OPS-LOG.md`, `ops/session-digest.md`): content NOT rewritten;
  a note points here. Old paths in those files map via the table above.
- Machine-specific media stays excluded from git (see `.gitignore`): frame sequences,
  `node_modules/`, third-party videos, physics bake data.

## 4. Post-migration verification (must all pass)

- `python knowledge/domains/painters/modules/_extract.py --check` → `checks=33 ok=33 fail=0`
- `python docs/skill/_selfcheck.py` → `RESULT: PASS` (junctions 4/4, domains ok)
- `python experiments/E1_t1b/_verify_t1b.py` → `VERIFY PASS`
- `python experiments/E1_t1c/_verify_t1c.py` → `VERIFY PASS`
- `python experiments/E2_t1/_verify_e2.py` → `VERIFY PASS`
- `python docs/skill/walkthrough_01/_verify_w01.py` → `checks=64 ok=64`
- Repo-wide: no remaining `research/` path references outside historical logs
  (`git grep -n "research/"` reviewed manually).
