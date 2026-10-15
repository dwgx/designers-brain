# Superpowers 跨 Harness 工作原理摘录（Part 1-3）

> 来源: https://raw.githubusercontent.com/obra/superpowers/main/docs/porting-to-a-new-harness.md
> 摘录日期: 2026-10-15。Part 1「How Superpowers works across harnesses」至 Part 3「Definition of done」。
> Part 4-8（集成形态 / 移植流程 / 分发 / Windows / PR）见完整原文。

---

## Part 1 — How Superpowers works across harnesses

Superpowers is the same content everywhere. What changes per harness is the thin
layer that delivers that content to the model and translates its instructions
into the harness's native tools. Three components:

1. **Skills (harness-agnostic).** Everything in `skills/` is the source of
   truth, shared verbatim by every harness. Skills are written to describe
   *actions* — "invoke a skill", "read a file", "dispatch a subagent", "create a
   todo" — and never name a specific tool. This is what lets one skill body run
   on Claude Code, Codex, Gemini, pi, and the rest without edits.

2. **Tool mapping (per-harness).** Each harness needs the action vocabulary
   translated into its real tool names. That translation lives in
   `skills/using-superpowers/references/<harness>-tools.md` and/or inline in the
   harness's bootstrap injector (see Part 5). It says, e.g., "*dispatch a
   subagent* → call `task` with `subagent_type`."

3. **Bootstrap (per-harness).** At the start of every session, the full
   `skills/using-superpowers/SKILL.md` is injected into the model's context,
   wrapped in `<EXTREMELY_IMPORTANT>` tags, with the tool mapping appended. That
   injected skill is what teaches the model that skills exist and that it must
   check for a relevant skill before acting. **The bootstrap is the entire
   integration.** Without it, the skill files are inert — present on disk, never
   invoked.

### Two rules that make this work

**1. Skills name actions, not tools.** Do **not** edit skill bodies to fit your
harness. Porting adds a tool-mapping reference and a bootstrap injector; it
never reaches into `skills/*/SKILL.md` to swap tool names. (The project's
contributor guidelines treat skill content as carefully-tuned behavior-shaping
code; rewording it for "compliance" is rejected on sight.)

**2. Everything ships through the harness's own install mechanism. Never edit the
user's files.** The bootstrap, the skills, and the tool mapping all get delivered
*as part of what the harness installs* — a plugin, an extension, a marketplace
entry, an extension-bundled context file. A port **must not** reach into a user's
global or personal config (`~/.gemini/config/AGENTS.md`, `settings.json`,
`trustedFolders.json`, a hand-edited `~/.bashrc`, etc.) to inject anything. The
harness owns what it loads; your install artifact is the only thing you get to
write. If the install mechanism genuinely can't carry the bootstrap, that is a
limitation to surface (Part 6) — never a license to hand-edit the user's config.
(Shape C is *not* an exception: Gemini's context file is fine because it ships
*inside the installed extension* and is declared by the manifest's
`contextFileName` — the harness loads the extension's own file, not a file you
edited in the user's home.)

---

## Part 2 — Can this harness be supported?

A harness can support Superpowers only if it can do all of the following. Check
these before writing code — if the first one fails, stop.

### Hard requirement: automatic session-start injection

The harness must let you inject text into the model's context **at the start of
every session, with no per-session opt-in by your human partner.** This is the
one non-negotiable capability. It can take any form:

- a **hook/event system** that runs a shell command at session start and reads
  its stdout (Claude Code, Cursor, Copilot CLI), or
- an **in-process plugin/extension** with a session-start or message lifecycle
  callback that can mutate the message array (OpenCode, pi), or
- an **instructions-file** convention where the harness loads a context file that
  *your installed extension ships and declares* (e.g. Gemini's `contextFileName`
  pointing at the extension's own `GEMINI.md`) — not a file you edit in the user's
  home.

If the only way to get Superpowers in front of the model is for your human
partner to opt in each session (paste a prompt, run a command, enable a mode),
the harness
**cannot** be properly supported. The acceptance test in Part 3 will fail, and
the PR will be closed. This is the single most common reason a "port" isn't a
real port.

### The rest of the capability checklist

| Capability | Why it's needed | If absent |
|---|---|---|
| **Skill discovery + invocation** | The model must be able to load a skill's full content on demand | If there's no native skill tool, the sanctioned fallback is to `read` the relevant `SKILL.md` directly — see Part 5. A harness with neither a skill tool nor file-read cannot work. |
| **File read / write / edit** | Nearly every skill manipulates files | Essential. No workaround. |
| **Run shell commands** | TDD, verification, git workflows | Essential. |
| **Subagent / task dispatch** | `dispatching-parallel-agents`, `subagent-driven-development` | Degradable: if unavailable, those specific skills tell the model to do the work inline or report the missing capability — *never* to invent a `Task` call. Some harnesses gate this behind a config flag (e.g. Codex needs multi-agent enabled). |
| **Todo / task tracking** | Progress tracking in several skills | Degradable: fall back to a plan file or `TODO.md`. |
| **Web fetch / search** | A few skills | Degradable. |
| **Shell or polyglot script execution (Windows)** | Only for the shell-hook shape, only if you want Windows support | See Part 7. In-process-plugin harnesses sidestep this entirely. |

"Degradable" means: the skill already has fallback wording for the missing
tool. Your job in the tool mapping is to point at the real tool when it exists
and reuse that fallback wording when it doesn't.

### You may not need a new directory at all

Some "new harnesses" are really existing integrations under a different
installer. Factory's Droid, for example, consumes the Claude Code plugin via its
own `plugin install` command and needs no new files here. Before building,
check whether the harness can simply load an existing manifest. A port that adds
nothing to this repo but a paragraph in the README is a perfectly good outcome.

---

## Part 3 — Definition of done

A port is finished when **all** of these are true:

1. The `using-superpowers` bootstrap loads at session start, every session, with
   no per-session opt-in.
2. A tool mapping exists for the harness (in
   `references/<harness>-tools.md`, inline in the bootstrap, or both — per Part 5).
3. Skills can actually be invoked — natively, or via the documented
   read-`SKILL.md` fallback — and the model follows them.
4. **The acceptance test passes.** In a clean session, the user message:

   > Let's make a react todo list

   auto-triggers the `brainstorming` skill *before any code is written*. Capture
   the full transcript — the PR requires it.
5. Tests cover the integration (Part 5) and pass.
6. A real user can install it through the harness's own mechanism (not by
   hand-copying files), and the version is tracked in `.version-bump.json` where
   applicable (Part 6). Note that some installers rewrite or strip the manifest on
   install (one drops it to just `{"name": …}`), so "the *installed* files report
   the repo version" is not always achievable — track the version at the source
   manifest and don't treat a rewritten installed manifest as a failure.

A quick smoke check before the full acceptance test: start a session and ask the
model to describe its superpowers. If the bootstrap injected, it knows it has
them. (OpenCode's install doc uses `opencode run --print-logs "hello" 2>&1 |
grep -i superpowers` for the same goal via a different mechanism — log-grep
rather than asking the model; the `2>&1` matters because logs go to stderr. Find
your harness's equivalent.)

---

