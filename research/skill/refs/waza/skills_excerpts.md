# Waza 技能摘录（ui / think）+ routing rule

> 来源: https://github.com/tw93/Waza — plugins/waza/skills/ui/SKILL.md, plugins/waza/skills/think/SKILL.md, rules/waza-routing.md
> 摘录日期: 2026-10-15。节选（含省略），完整原文见仓库。

## 1. ui/SKILL.md（节选）

name: ui
description: "Produces distinctive production UI and screenshot-grounded visual polish. Use when building or restyling pages, components, or typography. Not for backend logic or data pipelines."
when_to_use: "做组件, 不好看, 不和谐, 不清晰, 很丑, 很怪, 很傻, 突兀, 不协调, 字体, 排版, UI, 截图, build page, create component, make it look good, screenshot with visual complaint, font looks wrong"
dispatch_intent: "UI, component, page, visual interface, frontend, artifact-grounded screenshot aesthetic complaint" ---


## Outcome Contract

- Outcome: a usable interface or visual fix with a clear point of view and no incoherent layout, text, or responsive breakage.
- Done when: the real rendered surface or generated artifact has been checked against the user's visual goal and the relevant viewport states.
- Evidence: screenshots, rendered UI, source components, design tokens, accessibility constraints, and user-provided references.
- Output: the implemented visual change or a precise visual review with the remaining verification gap named.

**Output language rule:** Never use U+2014 em dash in any output from this skill. Use commas, colons, or periods instead.


Resolve the five direction dimensions below before writing code. Take colour, type, width, and voice from the current product's tokens, sibling components, screenshots, and the repo's git history first; then from other shipped products by the same team or author when they exist; then from the conversation. Model-default palettes, default fonts, and freehand graphics are allowed only when no reference exists. Infer first. Across every path in the request, ask in one compact clarification round with at most two sub-questions, only when the missing answer would materially change a deliverable. State the strongest inferred answer for every unresolved dimension and ask the user to correct only the material assumptions. An omitted answer accepts the stated assumption. A contradictory answer reopens only the affected dimension and must be resolved before that deliverable proceeds. An existing product may answer all five without another user turn.

1. **Who uses this, and in what context?** Analyst dashboard differs from landing page or onboarding flow. See "App shell exception" below if the answer is a sidebar + main workspace layout.

## When Asked For Options

Give at least 3 variations across genuinely different dimensions; the Options Guide in `references/design-reference.md` names the dimensions, the mix, and the basic-to-bold progression.

Offer without being asked when the decision is taste, not correctness: icon, weight, accent, motion feel. Two labeled candidates beat one landed guess, because the reply is a single letter instead of a rewrite round. For a structural change, describe the end state in a sentence or two and get a nod before writing the code.


## Hard Rules

Always-on bans for every mode, each with its rewrite in the Absolute Bans table of `references/design-reference.md`: no thick side-border accents, gradient text, default glass cards, reflex purple-to-blue/cyan-on-dark palettes, generic rounded shadow-card grids, modal escapes for ordinary overflow, `transition: all`, or layout-property animation.

Two motion rules apply in every mode, including the ones that skip the full reference. Frequency decides whether something animates at all: nothing keyboard-initiated animates, and anything the user triggers hundreds of times a day reads motion as lag, so it gets none. And every pressable thing moves on press, not only on hover, because hover is pointer-only and an unmoved control leaves the click unacknowledged.


## Output: Aesthetic Review

After significant build phases and at handoff, re-read the visual thesis from direction lock. If what is on screen drifted toward a generic default, identify the specific element that broke first (typeface, color, card treatment, spacing) and fix it before continuing.

Before the handoff summary, a new page or visual system also runs the Aesthetic Review Checks in `references/design-reference.md`. Every surface runs the AI Slop Test: would a stranger glancing at the first viewport say "an AI made this"? Scan it for the Absolute Bans and Common Traps in `references/design-reference.md` (reflex font, default gradient, centered hero with two CTAs side by side, three identical cards, generic top nav) and fix typography, color, or layout until any that were not an explicit part of the direction are gone.

If any check fails, fix first. Render the product's supported viewport or window range yourself: web breakpoints on both sides, and native minimum width, minimum height, their combination, and normal size. Test samples do not require new layout branches. Only when the host cannot render, say so and hand the user the exact view to check.

End with:
- Aesthetic direction, named and justified in 2-3 sentences
- Non-obvious choices explained: typeface, color decisions, layout logic
- Instructions for replacing placeholder content with real content

After handoff, stop.

---

## 2. think/SKILL.md（节选）

name: think
description: "Turns rough ideas into approved, decision-complete plans before coding. Use when planning architecture, judging whether to build, or writing a handoff. Not for bug fixes or small edits."
when_to_use: "出方案, 给方案, 怎么设计, 用什么方案, 有没有必要, 值不值得, what's the best approach, plan this, how should I, should we keep this"
dispatch_intent: "New feature, architecture, how should I design this, value judgment, executable plan, handoff" ---


Give opinions directly. Take a position and state what evidence would change it. Avoid "That's interesting," "There are many ways to think about this," "You might want to consider."


## Propose Approaches

Give one recommended approach with rationale. Include effort, risk, and what existing code it builds on. Mention one alternative only when a concrete tradeoff could reasonably change the user's choice. Always include one minimal option.

Anything that asks a person to install or configure something (hook, MCP server, editor plugin, config key, pricing tier, per-day limit) is a setup cost paid by every user. Default to the zero-setup form: a built-in command plus a skill, a fixed sensible default, a doc line. Offer the setup-requiring form only after naming why the zero-setup one cannot do the job.

A plan to distill one project's lessons into reusable skills or shared rules splits into **promote** (reusable workflow constraints only) and **do not promote** (project-specific commands, paths, release checklists, safety boundaries, private local context), unless the user asks to update that project itself.

For the recommendation, identify the most fragile assumption (premise collapse) and state it explicitly: "This plan assumes X. If X does not hold, Y happens." If the assumption is load-bearing and fragile, deform the design to survive its failure.

**Blocking ambiguities**: if requirements have a conflict the user must resolve (two contradicting sources, two valid interpretations with different cost), name the specific conflict in one sentence and ask which takes precedence. Do not silently pick.

**Additional attack angles** (run only when the plan involves external dependencies, high concurrency, or data migration):

| Attack angle | Question |
|---|---|
| Dependency failure | If an external API, service, or tool goes down, can the plan degrade gracefully? |
| Scale explosion | At 10x data volume or user load, which step breaks first? |
| Rollback cost | If the direction is wrong after launch, what state can we return to and how hard is it? |

If an attack holds, deform the design to survive it. If it shatters the approach entirely, discard it and tell the user why. Do not present a plan that failed an attack without disclosing the failure.

Get approval before proceeding.

## Simplicity Gate

Skip for one-file bug fixes or when the user explicitly chose the minimal option.

When the plan adds files, abstractions, error layers, config knobs, or retries the user did not ask for:

- **Minimal path:** the brute-force version in one line; the chosen plan must beat it on risk, rollback, or latency, not elegance.
- **Defensive layers:** every try/catch, retry, fallback, or flag maps to one named failure mode; delete layers that only "might" fail.
- **Surface delta:** list new commands, env vars, flags, or services; prefer +0 unless a user split needs a knob.
- **Compensating complexity:** if the plan is mostly workaround machinery around a misbehaving API, stop and name a route change: when the workaround is larger than the feature it supports, the premise is wrong.

If the gate fails, shrink the plan or switch to the minimal option before asking for approval.

## Hard Rules

- **No placeholders in approved plans.** Every step must be concrete before approval. Forbidden patterns: TBD, TODO, "implement later," "similar to step N," "details to be determined." A plan with placeholders is a promise to plan later.

## Output

**Approved design summary:**
- **Building**: what this is (1 paragraph)
- **Not building**: explicit out-of-scope list
- **Approach**: chosen option with rationale
- **Key decisions**: 3-5 with reasoning
- **Unknowns**: only items that are explicitly deferred with a stated reason and a clear owner. Not vague gaps. If an unknown blocks a decision, loop back before approval.

If the user only approves the design, end with the plan. If implementation is requested, follow Implementation Handoff instead of asking them to repeat the request.

---

## 3. rules/waza-routing.md（全文）

# Waza Routing

Waza ships eight installed skills. When a request matches a trigger below, prefer the matching skill over a generic implementation. Do not reimplement the workflow from scratch.

| skill   | use when                                                                                  |
|---------|-------------------------------------------------------------------------------------------|
| think   | new feature / architecture / "怎么设计" / "有没有必要" / "值不值得" / product judgment    |
| ui      | UI / page / component / frontend / typography / screenshot says "丑/不清晰/不和谐"        |
| check   | review / "看看代码" / pre-merge / release / push / close issue / project audit |
| hunt    | error / crash / regression / test failure / "以前是好的" / screenshot proves regression    |
| write   | draft / rewrite / proofread / "去 AI 味" / tweet / launch copy / document review          |
| learn   | deep dive into an unfamiliar domain / compile a batch of sources into one article         |
| read | read / fetch / quote / cite / convert / save a URL or PDF / "看这个链接" / "读一下" |
| health  | Claude/Codex/Pi ignores instructions / hook misfire / config drift / agent config audit / rot |

When two skills both match, read both `SKILL.md` "Not for" sections to disambiguate. Still ambiguous, ask the user. Never silently pick one.

Full routing table with chaining and disambiguation: <https://github.com/tw93/Waza/blob/main/skills/RESOLVER.md>

