# Workflow — Lanes & the LOOP Protocol

English · [中文](i18n/zh-CN/WORKFLOW.md) · [日本語](i18n/ja/WORKFLOW.md)

> Entry: `AGENTS.md` · Architecture: `docs/ARCHITECTURE.md` · Queue: `ops/GOALS.md` · Templates: `templates/`
> This file is the operations manual. Changing it means changing the workflow — consult the main brain first.

## 1. Roles

- **Main brain** (the top-level agent session): sets direction, slices work, dispatches, accepts results (reads artifacts + runs acceptance), synthesizes, and maintains `ops/GOALS.md`, this file, and `docs/`.
- **Research workers** (in-session subagents): write to the **exclusive paths** given in their briefs. Named (`agent://<Name>`); may cross-check each other by message. Sub-sub-agents only when a brief explicitly allows a read-only child.
- **Cross-harness workers** (out-of-process, **versioned job directories** — the historical `dispatch.ps1` + `board.py` flow is retired): a brief lands in a versioned job dir; the worker plans → executes → verifies → reports via files (`last.md` + `receipt.json`); every claim carries a path+key or the command that produced it. In-process work uses named subagents (below).

## 2. Lanes

| Lane | Content | State |
|---|---|---|
| **A — Painter distillation** | 76 painter dossiers + quote corpus (2044 sourced quotes) + image library (739 sourced artworks) + 76 composable module cards (228/228 verbatim checks) | Done |
| **B — Agent code-art** | 15-card anatomy (MG styles), HTML/Blender pipelines, prompt corpus, GitHub/Opus-5.5 evidence | Done |
| **C — Cross-harness dispatch** | Slicing + bookkeeping + receipt reconciliation for external workers | All entries closed |
| **D — Web / browser** | Sources, image library (739 sourced works — 701 PD/CC0 + 38 attribution-required, see `NOTICE.md`), reference-frame mapping, video archive | Done |
| **S — Skill** | `skills/designers-brain/` package: ecosystem study → spec → build → blind test → walkthrough | Done (PRE milestone) |
| **E — Experiments** (cross-lane) | Image experiments (E1/E2 series) + end-to-end animation tests (web ×2, Blender ×1) | Batch 1 done; E3/E4 queued |

## 3. The LOOP protocol (every research line runs this loop)

1. Take an `open` item from `ops/GOALS.md` (it must already have an artifact path + acceptance condition).
2. Deep research: tools unlimited; **new leads are appended to `ops/GOALS.md` immediately** as sub-items (new ID + artifact path) — never dropped.
3. Land artifacts at the item's path; every claim carries its source; evidence grades `[自述]/[史料]/[研究]/[归纳]/[推测]`.
4. Self-review in four parts: **A early output** (land something first, then continue) → **B rebuttal** (try to overturn your 3–5 strongest claims; tag `CONFIRMED/WEAKENED/OVERTURNED` + the command run; delete overturned claims from artifacts) → **C mechanical verification** (name one checker; paste raw output) → **D ≤14-line summary** (established / overturned / unknown / next).
5. Main-brain acceptance: read artifacts, run the acceptance condition; **the implementer never accepts their own work**; key artifacts are re-checked by someone else.
6. Update `ops/GOALS.md` (mark done + queue new items) → report to the Owner in one message (conclusion first).

## 4. Write-path discipline

- One writer per path. Collisions are re-sliced by the main brain — never worked around.
- Filenames encode ownership (e.g., `knowledge/domains/painters/dossiers/<id>.md` belongs to that artist's worker).
- Raw sources (`knowledge/domains/motion-graphics/origin/`) are **read-only**.

## 5. Evidence standard

- Every key claim = `path + key` or a URL; quotes must be checkable (letters / interviews / museum pages).
- Numbers carry denominator + date; "not found" ≠ "does not exist" (write "未找到（已查: …）").
- Project stance: "creation principles" are **induced operational rules**, not claims about an artist's inner state; sourced statements and AI inductions are labeled separately.

## 6. Tool map

| Tool | Use |
|---|---|
| `web_search` / `read`(URL) | general retrieval & static fetch |
| eval `browser` / chrome-devtools MCP | JS-heavy pages, interactions, screenshots |
| `task` subagents | in-process research fan-out (named, IRC-addressable) |
| versioned job dirs (cross-process) | out-of-process dispatch: brief in → `last.md` + `receipt.json` out (the retired `dispatch.ps1` + `board.py` board flow is history — recorded in `ops/OPS-LOG.md`) |
| `sessq` / `archive` | historical sessions & old measurements |

## 7. Reporting shape (to the Owner)

First line = conclusion or next step; numbered multi-step; ≤5 items per group; no pleasantries; concrete durations.
