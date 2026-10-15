# Repo Standards — conventions for a public research/knowledge repo

> **For:** Designers_Brain, pre-public restructure (2026-10-15). This is a "copy-paste-able conventions list": every convention below is backed by ≥1 real repo example.
> **Path note:** written at `research/repo_standards.md`; after the migration it lives at `docs/notes/repo_standards.md`.
> **Method:** authenticated GitHub API (`gh api`) + raw file reads, 2026-10-15. No web_search (rate-limited). Quotes are verbatim excerpts; star counts as of that date.
> **Evidence grade:** `[研究]` (read directly from primary repos) + `[归纳]` (recommendations in §5). Not yet reviewed by a second agent.
> **Language:** EN-primary per assignment; §5 conclusions CN/EN-mixed.

---

## 0. TL;DR — the 12 conventions that matter most

| # | Convention | Best example |
|---|---|---|
| 1 | README = stable "front door": one-liner + what's-inside index + quickstart + license; volatile state lives elsewhere | spec-kit, openai-cookbook |
| 2 | Content lives in topic dirs, each self-describing (per-dir README index or registry file) | papers-we-love, anthropic-cookbook |
| 3 | `AGENTS.md` at root = machine entry point ("README for agents"); nearest-file-wins; no required fields | papers-we-love, openai-cookbook |
| 4 | `CLAUDE.md` coexists as thin pointer/symlink; don't fork instructions | react.dev, anthropic-cookbook |
| 5 | Rules layer: `CONTRIBUTING.md` + style guides + (optionally) `skills/` with frontmatter | tldr, obra/superpowers |
| 6 | State layer: dated plan files (`YYYY-MM-DD-slug.md`), goals/specs dirs, append-only logs | superpowers `docs/plans/`, spec-kit `.specify/` |
| 7 | Machine-readable indexes (registry/authors/CITATION) beat prose for catalogs | openai-cookbook `registry.yaml` |
| 8 | README translations: `README.<lang>.md` (dot + BCP-47), switcher block at top, current language not linked | spec-kit, lobe-chat, gitea |
| 9 | Bulk translations → dedicated dir (`readme_i18n/`, `translations/<lang>/`, `content/<lang>/`) | immich, microsoft, kubernetes |
| 10 | Tool-managed regions marked with HTML comments; translations carry a sync baseline | Co-op Translator markers, superpowers-zh `upstream-sync.json` |
| 11 | Dual license: `LICENSE` (content, CC-BY-4.0) + `LICENSE-CODE` (MIT) + README License section | azure-docs, dotnet/docs |
| 12 | Naming: all lowercase; one separator style per category; number prefixes only when order matters | papers-we-love rules, genai lesson dirs |

---

## 1. Reference repos — five samples, dissected

Selection: research/knowledge repos, large + actively maintained, distinct genres (cookbook / course / paper corpus / awesome list / curriculum). All layouts below were listed live via API on 2026-10-15.

| Repo | Genre | Stars | License (API) | Signature pattern |
|---|---|---|---|---|
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | knowledge-base / cookbook | 76.6k | MIT | Minimal README + metadata files + AGENTS.md |
| [anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) | knowledge-base / cookbook | 53.5k | MIT | "Table of recipes" index into topic dirs |
| [papers-we-love/papers-we-love](https://github.com/papers-we-love/papers-we-love) | research corpus (community) | 110.6k | none (per-paper licenses) | snake_case topic dirs + strict naming rules |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | awesome-* (meta standard) | 519.3k | CC0-1.0 | Spec split into named files; all-lowercase filenames |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | course / curriculum | 121.4k | MIT | Numbered lesson dirs + `translations/` + markers |

### 1.1 openai/openai-cookbook

**Top-level layout** (live listing):
```
.codex/  .github/  articles/  examples/  images/
AGENTS.md  CONTRIBUTING.md  LICENSE  README.md
authors.yaml  registry.yaml  .gitignore
```
**README first screen** (whole README = 20 lines): logo via `<picture>` with dark/light variants → `> ✨ Navigate at cookbook.openai.com` → one-paragraph "what" → quickstart note (env var `OPENAI_API_KEY`) → "Most code examples are written in Python" → link to related resources → `## License / MIT License`. **No long content in the README.**
**docs/ organization:** none. Content split by role: `articles/` (narrative guides) vs `examples/` (runnable, one subfolder per topic with its own `requirements.txt`); `registry.yaml` + `authors.yaml` drive the public website (cookbook.openai.com). `AGENTS.md` documents exactly this ("Update `registry.yaml` whenever you add content…").
**Naming:** `examples/<topic>/`, notebook names "lowercase, dash-or-underscore-separated" (stated in AGENTS.md).
**Borrow:** tiny README + machine-readable registry + an AGENTS.md that encodes the content workflow.

### 1.2 anthropics/anthropic-cookbook

**Top-level layout:** topic dirs at root — `capabilities/ coding/ claude_agent_sdk/ cost_optimization/ evals/ extended_thinking/ finetuning/ managed_agents/ misc/ multimodal/ patterns/ skills/ third_party/ tool_use/ tool_evaluation/` — plus `anthropic_cookbook/` (installable package), `scripts/ tests/ Makefile/ registry.yaml authors.yaml`, `CLAUDE.md`, `CONTRIBUTING.md`, `.claude/`.
**README first screen** (69 lines): title → 1-para description → `## Prerequisites` → `## Explore Further` (docs/Discord links) → `## Contributing` → **`## Table of recipes`** — an index grouped by category (Capabilities / Tool Use / Third-Party / Multimodal / Advanced), each item linking to a *directory* or notebook with a one-line description → `## Additional Resources`.
**docs/ organization:** the README *is* the index; every topic dir is self-contained; validation via `Makefile` + `tests/`.
**Naming:** snake_case topic dirs; notebooks snake_case.
**Borrow:** "Table of recipes"-style index (grouped, one line per entry, links to dirs); root dirs = capabilities, not file types.

### 1.3 papers-we-love/papers-we-love

**Top-level layout:** ~70 snake_case topic dirs (`machine_learning/ distributed_systems/ …`), each containing a `README.md` index + optionally hosted PDFs + subtopic dirs; plus `scripts/download.sh`, `nautilus.db` (search index), `.github/CONTRIBUTING.md`, `AGENTS.md`, `CODE_OF_CONDUCT.md`, `README.md`.
**README first screen:** community description ("a directory of some of the best papers…") → explicit license-awareness note ("Due to licenses we cannot always host the papers themselves… you will see a :scroll: emoji next to its title") → Info / How to Read a Paper / Download (`./scripts/download.sh`) / Contributing / Copyright.
**docs/ organization:** per-topic READMEs are the documentation; policy lives in `.github/CONTRIBUTING.md` (source of truth), and `AGENTS.md` restates the machine rules: *"Repository purpose / Layout / Editing paper indexes / Scripts and validation"* — e.g. "Preserve the target README's existing headings, ordering, Markdown style, and level of description."
**Naming rules** (from CONTRIBUTING + AGENTS.md, verbatim): "Directory names are undercased and separated by underscores"; "Paper names are undercased and separated by dashes (example: `out-of-the-tar-pit.pdf`)"; include year; PRs rebased to 1 commit.
**Borrow:** per-dir index READMEs; explicit written naming rules; a repo whose content has mixed licenses handles it with a marker (`:scroll:`) + link-out policy.

### 1.4 sindresorhus/awesome

**Top-level layout:** `readme.md awesome.md contributing.md create-list.md pull_request_template.md media/ license .editorconfig .gitattributes .github/` — note: **everything lowercase**, including `readme.md` and `license`.
**README first screen:** centered logo → a nav row of 4 links (`What is an awesome list?` / `Contribution guide` / `Creating a list` / RSS) → "Just type `awesome.re` to go here" → `## Contents` (a TOC of ~25 categories) → the categorized list itself.
**docs/ organization:** the *spec* is split into purpose-named files: `awesome.md` = manifesto ("The awesome manifesto" — what qualifies as awesome, badge usage), `contributing.md`, `create-list.md`. The README links these at the top.
**Naming:** all-lowercase, hyphenated where needed (`code-of-conduct.md`, `pull_request_template.md`).
**Borrow:** split meta/spec docs into small named files linked from the README top; a nav row beats a long intro; lowercase discipline.

### 1.5 microsoft/generative-ai-for-beginners

**Top-level layout:** numbered lesson dirs `00-course-setup/` … `21-meta/`; `translations/` (40+ language dirs; README claims 50+ translations) + `translated_images/`; `docs/`; `shared/ tests/ images/ presentations/`; `AGENTS.md`, `CHANGELOG.md`, `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `LICENSE`, docsify `index.html`.
**README first screen:** thumbnail image → one-liner ("21 Lessons teaching…") → badge rows (license / contributors / issues / PRs / social / Discord) → **`### 🌐 Multi-Language Support`** — a marker-commented table of links to `./translations/<lang>/README.md`, "Translations maintained with Co-op Translator", plus a sparse-checkout tip for cloning without translations → `# Getting Started` → lesson table (00–21 with links, descriptions, videos).
**docs/ organization:** `docs/` holds docsify navigation (`_sidebar.md`, `_navbar.md`) + roadmap/security guides; per-lesson `README.md` files are the content units; each lesson dir self-contained.
**Naming:** lesson dirs `NN-kebab-case` (order encoded); translation dirs BCP-47-ish (`zh-CN`, `ja`, `ko`, `pt-BR`).
**Borrow:** number prefixes for sequenced content; a "what's inside" lesson/dir table; i18n as a first-screen section with machine-managed markers.

### 1.6 Cross-cutting distillate

- **README is a front door, not the product** (except awesome, where the list *is* the product — and even there the spec lives in separate files). Keep it stable; point to structure.
- **Every content dir is self-describing:** per-dir `README.md` index (PWL, anthropic, genai) or registry file (openai-cookbook).
- **Root meta layer:** `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `LICENSE`(+s), `CHANGELOG.md`, and — new normal — `AGENTS.md`/`CLAUDE.md` (3 of these 5 repos ship an AGENTS.md; anthropic ships CLAUDE.md).
- **Machine-readable sidecars** for catalogs: `registry.yaml`, `authors.yaml`, `CITATION.cff`, `nautilus.db`.
- **Naming discipline:** all lowercase; separators consistent per category (`_` for dirs in PWL/anthropic; `-` for files); number prefixes only when order matters.

---

## 2. Agent-collaboration workflow docs

### 2.1 The AGENTS.md standard (agents.md)

Source: <https://agents.md/> (site + repo `agentsmd/agents.md`; the file name is the standard). Verbatim key points:

- "**Think of AGENTS.md as a README for agents**: a dedicated, predictable place to provide the context and instructions to help AI coding agents work on your project."
- Used by "over 60k open-source projects"; works across agents (Codex, Jules, Cursor, Amp, goose, opencode, Zed, VS Code, Devin, …); now stewarded by the **Agentic AI Foundation (Linux Foundation)**.
- **No required fields** — "just standard Markdown. Use any headings you like."
- Popular sections: *Project overview / Build and test commands / Code style guidelines / Testing instructions / Security considerations* (+ commit & PR rules).
- **Nesting:** "Place another AGENTS.md inside each package. Agents automatically read the nearest file in the directory tree, so the closest one takes precedence" (the main OpenAI repo has 88 AGENTS.md files). Conflict rule: "The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything."
- Migration tip: `mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md` (symlink for backward compat).

**Verified adopter examples (fetched today):**

- **papers-we-love** — an AGENTS.md written for a *knowledge* repo (not an app): sections `Repository purpose / Layout / Editing paper indexes / Scripts and validation`; states "This is not an application project: there is no package manager, build, or unit-test suite" and gives the exact validation commands (`bash -n scripts/download.sh`, link checks). ← best template for us.
- **openai/openai-cookbook** — "Repository Guidelines": *Project Structure & Module Organization / Build, Test, and Development Commands / Coding Style & Naming Conventions / Testing Guidelines / Commit & Pull Request Guidelines / Metadata & Publication Workflow / Review Guidelines / Recent Learnings*. The **Recent Learnings** section is a running log of agent lessons ("`uv run` can inherit the wrong virtualenv… → Clear `VIRTUAL_ENV`… → Avoids misleading mismatch warnings").
- **microsoft/generative-ai-for-beginners** — Project Overview (incl. "Translations directory with 40+ language versions") + Setup Commands with copyable bash.
- **github/spec-kit**, **obra/superpowers** — both ship root AGENTS.md (superpowers also ships `GEMINI.md`; spec-kit nests agent integrations under `integrations/`).

### 2.2 superpowers methodology — doc structure (reference our existing research)

Repo: [obra/superpowers](https://github.com/obra/superpowers) (verified root layout today): `skills/` (15 skills), `docs/`, `hooks/`, `scripts/`, `assets/`, plugin manifests for 10+ harnesses (`.claude-plugin/ .codex-plugin/ .cursor-plugin/ .devin-plugin/ .hermes-plugin/ .kimi-plugin/ .muse-plugin/ .antigravity-plugin/ .opencode/ .pi/`), `AGENTS.md`, `GEMINI.md`, `RELEASE-NOTES.md`.

- `docs/plans/` uses **dated filenames**: `2025-11-22-opencode-support-design.md`, `2026-01-17-visual-brainstorming.md` (design vs implementation as sibling docs). `docs/superpowers/{plans,specs}` = another state layer.
- **Do not re-research; cite our archive:** the full write-up is `docs/skill/skill_ecosystem.md` (S-01) with原文 in `docs/skill/refs/superpowers/`. Key doc-structure rules it established (all verbatim there):
  - `description` frontmatter states **only when to use** — never summarize the workflow (a summarized description gets followed *instead of* the body);
  - **one-level-deep references** ("Keep file references one level deep"); no `@` force-loads (burns 200k+ context);
  - SKILL.md <500 lines, then split into `references/`; progressive disclosure (3 layers);
  - scripts invoked via interpreter (`bash scripts/tool.sh`), never bare paths;
  - state/handoff artifacts live in files, not chat (gate files, plan docs).

### 2.3 spec-kit — "structured processes, reusable templates, documented outcomes"

Repo: [github/spec-kit](https://github.com/github/spec-kit). README: "an open source toolkit that gives AI coding agents structured processes, reusable templates, and documented outcomes"; three independent entry points (build / bug-fix / assess) presented as a table.
**Layering (verified):** `.specify/memory/constitution.md` (project principles) + `templates/` (`constitution-template.md`, `spec-template.md`, `plan-template.md`, `tasks-template.md`, `checklist-template.md`, `commands/`) + `docs/` (`concepts/ guides/ reference/ community/`, `toc.yml`) — i.e. **constitution → spec → plan → tasks → checklist** as a doc pipeline, with the state files generated into user projects.
**Borrow:** separate "principles" from "plans" from "tasks"; templates as first-class repo citizens.

### 2.4 Synthesis — the "AI-ops-friendly" doc structure

Five layers, each with a home and a job (models in parentheses):

| Layer | Role | Files | Models |
|---|---|---|---|
| **Entry** | Where an agent starts | `AGENTS.md` (canonical) + `CLAUDE.md`/`GEMINI.md` (pointer/symlink) + `README.md` (humans) | papers-we-love; superpowers; spec-kit |
| **Rules** | How to work here | `CONTRIBUTING.md`, style guides, `skills/<name>/SKILL.md` w/ frontmatter | tldr `contributing-guides/`; superpowers `skills/` |
| **State** | What's in flight / decided | `docs/plans/YYYY-MM-DD-slug.md`, `specs/`, goals/queue files, append-only logs | superpowers `docs/plans/`; our `ops/GOALS.md` + `OPS-LOG.md` |
| **Index** | Machine-readable catalog | `registry.yaml`, `authors.yaml`, `CITATION.cff`, `nautilus.db`, `INDEX.md` | openai-cookbook; PEG (`CITATION.cff`) |
| **History** | What happened | `CHANGELOG.md`, `RELEASE-NOTES.md` | genai; superpowers |

Plus four mechanics that make it work:
1. **Nearest-file-wins nesting** (AGENTS.md standard) — put sub-rules next to the content they govern.
2. **One level deep references** — link, don't chain; no force-loads.
3. **Marker comments for tool-managed regions** — `<!-- X START --> … <!-- X END -->` (see §3.3).
4. **A "Recent Learnings" / lessons section** that accretes rules from incidents (openai-cookbook).

---

## 3. i18n conventions

### 3.1 README translation files — naming + switcher

**File-naming variants seen in the wild (all verified):**

| Style | Example file(s) | Repo |
|---|---|---|
| dot + BCP-47: `README.<lang>.md` | `README.zh-CN.md`, `README.ja.md`, `README.ko.md` | [github/spec-kit](https://github.com/github/spec-kit) |
| dot + BCP-47 | `README.zh-CN.md` | [lobehub/lobe-chat](https://github.com/lobehub/lobe-chat) |
| hyphen + underscore | `README-zh_CN.md` | [ant-design/ant-design](https://github.com/ant-design/ant-design) |
| dot + lowercase | `README.zh-cn.md`, `README.zh-tw.md` | [go-gitea/gitea](https://github.com/go-gitea/gitea) |
| underscore + glibc-ish, in a dir | `readme_i18n/README_zh_CN.md` (20 languages) | [immich-app/immich](https://github.com/immich-app/immich) |

→ For a new repo, pick **one**; the most common modern style in our sample is `README.<BCP-47>.md` (`zh-CN`, `zh-TW`, `ja`, `ko`). Keep codes consistent (`zh-CN` not `zh_CN` not `zh-cn` mixed).

**Switcher block — three verified shapes:**

1. **Centered block, current language in `<strong>` (not linked):** spec-kit — every language file mirrors the same block with its own language bolded (example = English README; the ja file carries `<strong>日本語</strong>`, etc.):
   ```html
   <p align="center">
       <strong>English</strong> ·
       <a href="./README.zh-CN.md">简体中文</a> ·
       <a href="./README.ja.md">日本語</a> ·
       <a href="./README.ko.md">한국어</a>
   </p>
   ```
2. **Inline bold-current line** (lobe-chat): EN file: `**English** · [简体中文](./README.zh-CN.md) · [Official Site]…`; zh file: `[English](./README.md) · **简体中文** · …`
3. **Nav-row / top-line style**: ant-design `… · English · [中文](./README-zh_CN.md)` (current = plain text); gitea `[繁體中文](./README.zh-tw.md) | [简体中文](./README.zh-cn.md)` right under badges (current language omitted from the list; in the zh file it lists English + 繁體中文).

**Distilled rules:** current language is never a link to itself (bold or plain); all other languages are linked; the block sits at the top (under title/badges); **the same block, same order, in every language file**; for >3–4 languages move the switcher to a single centered row (immich lists 20) and/or a `readme_i18n/` dir.

### 3.2 Dir-based i18n organization (`docs/i18n/<lang>/` equivalents)

Real patterns for when translations outgrow root README files:

| Pattern | Layout | Repo (verified) |
|---|---|---|
| `readme_i18n/README_<locale>.md` | one dir for translated READMEs; 20 files | immich |
| `translations/<lang>/` | full parallel copy per language (course = every lesson); `en` included | microsoft/generative-ai-for-beginners |
| `content/<lang>/` | per-language docs trees + per-language `README.md`; root README has a "Localization READMEs" table (bn, de, en, es, fr, ja, ko, zh-cn, …) | kubernetes/website |
| `pages.<lang>/` | one dir per language for a flat page collection | tldr-pages/tldr |
| `files/<locale>/` (separate repo) | translation repo split from source repo; locales `es fr ja ko pt-br ru zh-cn zh-tw` | mdn/translated-content |
| per-page suffix `<name>.<lang>.mdx` + `_meta.<lang>.json` | site-docs i18n (Nextra style); 13 languages | dair-ai/Prompt-Engineering-Guide |

**Choosing:** README-only → dot-suffix files at root (or `readme_i18n/` if many); a few doc pages → one dir per language; whole docs tree → `translations/<lang>/` or `content/<lang>/`; very large / many contributors → separate repo (MDN model).

### 3.3 Translation quality & maintenance — the通行做法

1. **Source of truth + translate direction, stated explicitly.** tldr CONTRIBUTING: "Translations of pages should be done based on the English (US) page… If the English pages don't exist for the command, it should be added first in a PR before creating a translation." And: "When fixing errors in an existing translation, it is suggested to update the page to match the latest version of the English page."
2. **Upstream sync baseline file.** Our own reference: `docs/skill/refs/zh/upstream-sync.json` (superpowers-zh) records `{upstream, commit, version, date, evidence, trackedPaths}` so an audit can compute "what changed upstream since last sync" — because diffing headings alone hides body edits ("上游 v6.3.0 加了 113 行，我们一声不吭" — the recorded incident). **This is the single most copyable mechanism for us.**
3. **Tool-managed regions via marker comments + automation.** Microsoft repos: `#### Translations maintained with [Co-op Translator](…)` / Phi-3Cookbook: "Supported via GitHub Action (Automated & Always-Up-to-Date)" — the language table is wrapped in `<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->` … `END` so a bot can rewrite just that block. Also: sparse-checkout tip to avoid cloning 50+ translations.
4. **Active-locale gating + reviewer teams.** MDN: "we are only accepting updates to active locales — this means locales that have active community maintenance teams in place to review PRs"; list of active locales; `PEERS_GUIDELINES.md` for reviewers; `l10n-<locale>` issue labels for task routing.
5. **Per-language style guides + translation templates.** tldr `contributing-guides/` contains `style-guide.md` + `style-guide.{zh,ar,cs,de,ko,ru}.md` and `translation-templates/` (7 template files: `common-arguments`, `common-descriptions`, `notes`, `see-also-mentions`, …) so common phrases translate consistently; "add [a new language] to the translation templates".
6. **Progress/outdated tracking + tooling badges.** tldr points contributors to a tldri18n progress site "to see the overall progress of all translations, and which translations are missing or outdated"; gitea shows a Crowdin localized-% badge in the README (translation happens in Crowdin, not the repo).
7. **Outdated markers** — policy-level in the above (MDN active locales; tldri18n "outdated"; Co-op keeps always-up-to-date). For a small repo the practical version: keep a `date`/`commit` note in each translated file's header and a note like "This translation may lag behind the English source" where relevant. *(No strong single-repo per-file banner example was verified in this pass — treat as a recommendation, not a cited convention.)*

---

## 4. Dual licensing — code MIT + content CC-BY-4.0

### 4.1 Verified instances

**Pattern A — Microsoft docs pattern (LICENSE + LICENSE-CODE + ThirdPartyNotices).**
- [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs) (11.0k★, active): root `LICENSE` = **CC-BY-4.0** full text; `LICENSE-CODE` = **MIT** ("The MIT License (MIT) Copyright (c) Microsoft Corporation"); `ThirdPartyNotices.md` carries the explicit grant (verbatim):
  > "Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the [Creative Commons Attribution 4.0 International Public License]… and grant you a license to any code in the repository under the [MIT License]. See the [LICENSE-CODE](LICENSE-CODE) file."
  README ends with a `## License` section: "For all licensing information, refer to: LICENSE / LICENSE-CODE / ThirdPartyNotices."
- [dotnet/docs](https://github.com/dotnet/docs) (4.8k★): same three files, **no README license section** (files only). GitHub sidebar shows **CC-BY-4.0** (detected from `LICENSE` only — `LICENSE-CODE` is not surfaced in the repo's license badge; observed on both repos).

**Pattern B — LICENSE-DOCS.md + README statement.**
- [reactjs/react.dev](https://github.com/reactjs/react.dev): `LICENSE-DOCS.md` = CC-BY-4.0 full text; README `## License` (verbatim): "Content submitted to react.dev is CC-BY-4.0 licensed, as found in the LICENSE-DOCS.md file." (no root `LICENSE`; code terms not restated in the README).

**Pattern C — README footer line (canonical, older).**
- [twbs/bootstrap](https://github.com/twbs/bootstrap) README footer (verbatim): "## Copyright and license — Code and documentation copyright 2011-2026 the Bootstrap Authors. Code released under the [MIT License](…/LICENSE). Docs released under [Creative Commons](…by/3.0)." (CC-BY-**3.0** for docs; the *footer-line pattern* is what's transferable.)

**Single-license content repos (for contrast):** [kubernetes/website](https://github.com/kubernetes/website) `LICENSE` = CC-BY-4.0 only; [openai/openai-cookbook](https://github.com/openai/openai-cookbook) = plain MIT for everything.

### 4.2 How to arrange it (distilled)

- **File set:** `LICENSE` (content, CC-BY-4.0) + `LICENSE-CODE` (MIT) + optional `ThirdPartyNotices.md` (trademark/third-party notes + the explicit dual grant). This is the most copyable, already-proven arrangement for "code MIT + content CC-BY-4.0".
- **README "License" section:** one short block linking the files (azure-docs style) — or the react.dev single-sentence style if you prefer minimal.
- **Detection caveat:** GitHub shows only the license detected from `LICENSE` (CC-BY-4.0). If you need the sidebar to reflect both, different filenames would be required — but the Microsoft pattern is widely accepted as-is; don't over-optimize for the badge.
- **NOTICE:** Apache-2.0 convention; not needed for MIT+CC. `ThirdPartyNotices.md` is the Microsoft variant (trademarks + third-party content).
- **Third-party content:** papers-we-love model — only redistribute when the license permits; otherwise link out and mark hosted items (`:scroll:`); state this policy in CONTRIBUTING. (Applies to us: PD/CC0 artwork sources, excluded videos.)

---

## 5. 结论 — 给 Designers_Brain 的直接建议（≤15 条）

> 每条可执行；括号内为对标仓库。前 6 条建议在公开前完成，其余可增量做。

1. **README.md 做「前门」并保持稳定（EN 为主）**：标题 + 一句话 + 状态行 + 语言切换块 + "What's inside" 表（`knowledge/ experiments/ docs/ skills/ ops/ templates/` 各一行说明）+ 快速开始（怎么读、怎么跑校验命令）+ License 页脚。易变状态不放 README，链到 `ops/GOALS.md`。（对标：spec-kit、openai-cookbook、awesome 的导航行）
2. **新增 `README.zh-CN.md`**，采用 `README.<lang>.md` 点号风格 + BCP-47 代码；两份文件的顶部放同一切换块：当前语言加粗/不链接，其余链接，顺序一致。（对标：spec-kit 的 `<strong>` 块、lobe-chat）
3. **`AGENTS.md` 保持为机器入口，并升级结构**：Purpose → Layout（目录地图）→ Commands（可原样跑的校验命令：`python docs/skill/_selfcheck.py`、`_extract.py --check`、`_verify_*.py`）→ Conventions（证据分级、一个路径一个写手）→ PR rules → **Recent Learnings**（把事故教训沉淀进来，如乱序重渲、越权写 GOALS）。（对标：papers-we-love 结构 + openai-cookbook 的 Recent Learnings；标准见 agents.md）
4. **`CLAUDE.md` 用符号链接或三行指针指向 AGENTS.md**，不复制内容（nearest-file-wins，防止两份规则漂移）。（对标：agents.md FAQ 的 symlink 做法；react.dev/anthropic-cookbook 均单独有 CLAUDE.md，可对比）
5. **双许可落地：`LICENSE` = CC-BY-4.0（正文/知识内容：dossiers、cards、guides、README 文字）+ `LICENSE-CODE` = MIT（脚本：`_extract.py`、`_verify*.py`、skill scripts）+ 可选 `ThirdPartyNotices.md`（第三方来源与商标注记）；README 加 "License" 节链接两者。**（对标：azure-docs / dotnet/docs；注意 GitHub 侧栏只会显示 CC-BY-4.0——可接受）〔需 Owner 最终拍板许可选择〕
6. **第三方素材合规注记**：仓库已排除重媒体；在 `ThirdPartyNotices.md`（或 README License 节）写明「馆藏图来源 Met/AIC/Cleveland/Commons，各自许可（PD/CC0）为准，不随本仓再许可；被排除的第三方视频不随仓分发」。（对标：papers-we-love 的 Respect content licenses）
7. **docs/ 加一个 `docs/README.md` 索引**：WORKFLOW / ARCHITECTURE / ROADMAP / MIGRATION / notes/ / skill/ 各一行说明；`docs/notes/` 文件数超过 5 个时同样加索引。（对标：superpowers `docs/`、spec-kit `docs/toc.yml`）
8. **状态分层对齐「入口 / 规则 / 状态」三层**：现状已基本成立（AGENTS=入口、WORKFLOW+CONTRIBUTING=规则、ops/=状态）；补一条 README 指引「Project state → ops/GOALS.md」，新计划文档用 `YYYY-MM-DD-slug.md` 命名。（对标：superpowers `docs/plans/`、spec-kit `.specify/memory/constitution.md`）
9. **命名风格写死进 CONTRIBUTING**：全小写；知识文件/主题目录用 `_`（沿用现状），slug/ID 内允许 `-`（`mg-styles-15`）；仅有序内容用数字前缀（`E1_t1`、未来的 `00-`）；语言代码统一 BCP-47（`zh-CN`）。（对标：papers-we-love 的三条命名规则原文）
10. **机器可读索引**（低优先，增量）：`knowledge/INDEX.md` 保持；模块/卡片数量增长后考虑加 `registry.yaml` 式清单（id/path/tags）或给卡片加 frontmatter，避免纯散文检索。（对标：openai-cookbook `registry.yaml`、PWL `nautilus.db`）
11. **补齐标准元文件**：`CONTRIBUTING.md`（提案流程 + 证据规则 + 「实现者不验收」复核门）、`CODE_OF_CONDUCT.md`、`SECURITY.md`；如希望被学术引用，加 `CITATION.cff`。（对标：PEG 的 `CITATION.cff`、spec-kit）
12. **文档级 i18n 先不动，定好模式再动**：若未来翻译 dossier，建议 `translations/<lang>/`（全量平行）或按 `content/<lang>/` 分节；任何翻译产物都带一个 `upstream-sync.json` 式基线（源 commit/日期），修错时「同步到最新源文」。（对标：MDN active-locale + tldr 规则 + 我们的 superpowers-zh 基线）
13. **工具代管区块用 HTML 注释标记**：未来若自动生成语言表/索引表，包 `<!-- X START -->…<!-- X END -->`，让 agent/CI 可机械重写。（对标：Co-op Translator 标记）
14. **校验命令可见化**：README + AGENTS.md 里列全可跑命令（这是本仓最硬的资产：`checks=33 ok=33`、`VERIFY PASS`、乱序重渲）；「能跑的检查」比「说过的标准」更能约束外部贡献者与 agent。（对标：openai-cookbook AGENTS.md 的 Commands 节、genai 的 Setup Commands）
15. **公开后加最小 CI**：markdown link check（lychee 式）+ markdownlint + 现有 `_verify` 脚本；至少做到发布前手动全链检查一次。（对标：papers-we-love 的 Lychee CI、dotnet/docs 的 docs-verifier）

**未决项（留 Owner/主脑）**：① 许可最终选择（CC-BY-4.0 假设）；② README 主语言（建议 EN 主 + zh-CN 副，但本仓内容以中文为主，反向亦可）；③ 是否/何时做文档级翻译；④ 引用格式（CITATION）作者名与年份。

---

## 6. Gaps & caveats（本次未覆盖 / 未核实）

- 未验证「翻译文件内 outdated 横幅」的单一强实例（只核实了策略级机制：MDN active locales、tldri18n 进度站、Co-op 自动化）——§3.3.7 已标注为建议。
- `openai/codex` 的 AGENTS.md 在 agents.md 站点被引用为示例，但按当前仓库路径直读未命中（404）——未深挖其实际位置；不影响结论（已用 5 个直接核实的 AGENTS.md 实例）。
- Vue/Nuxt/Electron 等生态的 i18n 组织未采样（时间预算）；如需扩展，优先看 `vuejs-translations/*` 多仓模式。
- GitHub 对 `LICENSE-CODE` 的识别行为只在 azure-docs / dotnet/docs 两个仓观察（均只显示 CC-BY-4.0）；更细的 licensee 规则未穷举。
- 所有星数为 2026-10-15 快照。

## 7. Sources（本次直读的仓库与页面）

- <https://agents.md/> · <https://github.com/agentsmd/agents.md>
- <https://github.com/openai/openai-cookbook>（README、LICENSE、AGENTS.md、root tree）
- <https://github.com/anthropics/anthropic-cookbook>（README、root tree）
- <https://github.com/papers-we-love/papers-we-love>（README、AGENTS.md、.github/CONTRIBUTING.md、machine_learning/）
- <https://github.com/sindresorhus/awesome>（readme.md、awesome.md、root tree）
- <https://github.com/microsoft/generative-ai-for-beginners>（README、LICENSE、translations/、docs/、AGENTS.md）
- <https://github.com/github/spec-kit>（README + README.ja/zh-CN/ko、.specify/、templates/、docs/）
- <https://github.com/obra/superpowers>（root tree、docs/、skills/）+ 本仓 `docs/skill/skill_ecosystem.md`、`docs/skill/refs/`（S-01 留档）
- <https://github.com/lobehub/lobe-chat> · <https://github.com/ant-design/ant-design> · <https://github.com/go-gitea/gitea> · <https://github.com/immich-app/immich>
- <https://github.com/tldr-pages/tldr>（README、CONTRIBUTING、contributing-guides/）· <https://github.com/mdn/translated-content>（README、files/）· <https://github.com/dair-ai/Prompt-Engineering-Guide>（README、pages/）
- <https://github.com/MicrosoftDocs/azure-docs> · <https://github.com/dotnet/docs> · <https://github.com/reactjs/react.dev> · <https://github.com/twbs/bootstrap> · <https://github.com/kubernetes/website>
- <https://github.com/microsoft/Phi-3Cookbook>（Co-op Translator 标记实例）

*Research note, 2026-10-15. Written by RepoStandards worker. Reviewer: none yet — recommend one independent pass before the repo goes public.*
