# Protocols

> Hard rules for operating this repository — human or AI. Where a rule says *must*, a violation is an incident to be recorded in `ops/OPS-LOG.md`.

## 1. Core principles

1. **One writer per path.** Any file has exactly one writer at a time (a person, an agent, or the main brain). Parallel writers coordinate via explicit handoff, never by both editing.
2. **Evidence grades on every claim.** `[自述]` / `[史料]` / `[研究]` / `[归纳]` / `[推测]`; quotes must carry a source. If something cannot be found: write "未找到（已查: …）" — never fill gaps silently.
3. **No claim without a check.** Capabilities are `[UNVERIFIED]` until an experiment or script exercises them. "Done" requires a runnable verification (a command or a file that a third party can re-run).
4. **State authorities.** `ops/GOALS.md` is the single source of truth for work state. `ops/OPS-LOG.md` is append-only history. Dispatch boards are snapshots; where a board and the disk disagree, **the disk wins** — say so and correct the board.
5. **Pointers, not copies.** The skill and indexes reference knowledge files; they never duplicate content. Content lives in exactly one place.

## 2. Agent operating protocol

- **Brief format** (delegated work): `# Target` (files in scope) · `# Change` (steps) · `# Acceptance` (observable, checkable) · discipline notes. One writer per brief.
- **Receipt format**: end each work item with a receipt — what changed, artifact paths, raw verification output, and a four-part self-review (early output / rebuttal / mechanical verification / summary). Completion status lives in the receipt, not in a rewritten goal.
- **Forbidden writes** (unless explicitly granted in the brief): `ops/GOALS.md`, `ops/OPS-LOG.md`, machine-level boards, anything outside the repo.
- **Budgets**: soft tool-call budgets per brief; at the limit, land the best current state and list gaps. Never spin.
- **Two failure-handling patterns** (proven):
  - *Zero-output timeout* (e.g., a channel times out with no artifacts) → re-dispatch on another channel, split smaller.
  - *Crash mid-run with partial artifacts* → **resume the same session**; verify what landed first; never restart from a blank state without checking.

## 3. Research protocol

- Prefer primary sources (works, letters, treatises, museum records, archives). Every dossier section marks its grade.
- Quotes: verbatim, with source (book/letter/URL + date where known). Machine translation of quotes must be marked as translation.
- Distill **operational rules** ("what can be executed"), not inner states: principles are inductions from evidence, not claims about the artist's mind.
- New domains follow the registry contract (`docs/ARCHITECTURE.md` §3.2): cards + index + conflicts + output mapping + intensity + evidence, before `status: active`.

## 4. Verification protocol

- Every experiment ships a verifier script; acceptance = the verifier passes, with raw output pasted into the receipt.
- **Independent review**: outputs are reviewed by an agent that did not produce them, from a *clean context* (no process narrative — only artifacts + rubric). Reviews must not inflate; "cannot verify" is a valid verdict.
- **Determinism contracts** (animation/code output): C1–C10 in `templates/determinism_contract.md`, including the **out-of-order re-render check** — sequential re-renders can hide state bugs; always re-render a non-contiguous sample and compare frame hashes.
- Blender outputs: P1 determinism note (EEVEE sampling noise bounds) is the honest ceiling unless bit-exactness is demonstrated.
- Three-place sync rule: when a distilled fact changes, update the source of truth first, then the derived artifacts that quote it (e.g., conflicts list → style card → experiment design).

## 5. Composition & conflict protocol

- Composition of two modules requires the full pre-check, in order: conflict table scan → near-miss explicit values → N1 anti-constraint recompute → N3 axis-ownership (auxiliary conflict lines are **removed entirely**, never downgraded) → N4 split decision (same pixel statistic → pick one; separable regions → zoning table + mask) → N9 acceptance (main module full set + auxiliary non-conflict axes; "dual standards on a conflict axis" is a failure).
- Silent compromise is forbidden: every merge either keeps one side, zones the surface, or rewrites the conflicting clause with the documented句式.
- Authoritative file: `knowledge/cross/conflicts.md` (C-01–C-18, N1–N9).

## 6. Image channel protocol

- Channel: direct gateway API; **bare model name** `grok-imagine-image-2.0` (a `buddyfarm/` prefix 404s on this path — opposite of the CLI). Request 1024×1536; actual return 768×1152.
- The channel has **no negative-prompt parameter**: negative segments are archived in the request record but never sent.
- Archive contract: `req` / `resp` / image + `sha256` manifest. Traceable, not reproducible (no seed) — never promise reproducibility.
- Details and probe evidence: `knowledge/cross/image_channel.md`.

## 7. Skill interaction protocol

- The skill's first action on a design request is the **first-ask package** (3+2 items; defaults spoken; ≤3 rounds). Opt-out ("just do it") is allowed but must be recorded with a one-line assumption list.
- Visual decisions need **visible** candidates (2–3) and a hard stop after showing. A `design-brief.md` gate file records intent / non-goals / constraints / user's verbatim choices / assumptions / approval scope. Approval covers only what was actually shown.
- Full protocol: `skills/designers-brain/SKILL.md`; rationale: `docs/skill/skill_spec.md`.

## 8. Git & release protocol

- Commit messages: English, imperative, no AI attribution. `commit` is free; **push requires the three checks** pasted in the reply: (1) working tree clean, (2) local log matches intent, (3) diff stat has no unrelated files.
- Never commit: secrets, credentials, third-party media (see `.gitignore`), or machine-specific caches. Run the secret scan before publishing.
- Layout changes are recorded in `docs/MIGRATION.md` (old → new path table) — history is preserved via `git mv`.

## 9. i18n protocol

- English is canonical for `docs/` and the root README trio. `docs/i18n/zh-CN/` and `docs/i18n/ja/` are translations, updated when the English source changes materially (or explicitly marked stale).
- Keep product names, file paths, and protocol keywords (N1–N9, C-01–C-18, evidence grades) untranslated; translate prose, not identifiers.

## 10. Incident & lesson protocol

- Incidents (channel outages, rule violations, near-misses, overturned claims) are appended to `ops/OPS-LOG.md` with date, what happened, disposition. Overturned conclusions are deleted from artifacts and marked `OVERTURNED: …` in the log.
- A lesson that changes behavior must be written into a *rule* (this file) or a brief template — not just the log.

## 11. Security & privacy

- No credentials in the repo, ever. Tokens found in captured material are redacted before publication.
- Private infrastructure is described generically in public docs; probe evidence stays local-only when it embeds private endpoints.
- Museum images: only public-domain / openly licensed sources; attribution recorded in `knowledge/INDEX.md` and image manifests.
