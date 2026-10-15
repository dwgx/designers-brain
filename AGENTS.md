# Designers_Brain — Agent Entry

You are working in **Designers_Brain**, a research repository that distills designers' visual languages into composable, verifiable modules — packaged as an agent skill. Operated by AI agents; Owner: dwgx1.

## Read first (in order)

1. `docs/PROTOCOLS.md` — hard rules: evidence grades, write scope, verification, git/release, security.
2. `docs/WORKFLOW.md` — lanes & the LOOP protocol; roles; tool map.
3. `docs/ARCHITECTURE.md` — repo layout, knowledge model, extension points.
4. `ops/GOALS.md` — the current work queue (**single source of truth** for state).

## Hard rules (short version)

- **One writer per path.** Don't touch `ops/GOALS.md` or `ops/OPS-LOG.md` unless you are the main brain (or your brief explicitly grants it).
- **Evidence grades on every claim** (`[自述]/[史料]/[研究]/[归纳]/[推测]`); quotes carry sources; "not found" is written as 未找到（已查: …）.
- **No "done" without a runnable check** — name the command, paste raw output. Unverified = `[UNVERIFIED]`.
- **Raw sources are read-only**: `knowledge/domains/motion-graphics/origin/`.
- **No secrets, no third-party media** in commits; run the secret scan before publishing.
- Docs are English; Chinese is acceptable in raw research notes (dossiers, logs).
- Commit freely; **push only after the three checks** (PROTOCOLS §8).

## Layout at a glance

`knowledge/` distilled product · `experiments/` evidence runs · `docs/` manuals · `skills/designers-brain/` the skill · `ops/` state · `templates/` reusable templates.

## Commands (runnable checks)

```bash
python docs/skill/_selfcheck.py                                  # skill refs + junctions + domains → expect PASS
python knowledge/domains/painters/modules/_extract.py --check    # module cards → expect checks=33 ok=33
cd experiments/E2_t1 && python _verify_e2.py                     # experiment → expect VERIFY PASS
```

Every experiment directory ships its own `_verify*.py`; every knowledge domain ships a checker.

## Recent learnings (keep current)

- Sequential re-renders can hide state bugs — always re-render a **non-contiguous sample** and compare frame hashes (out-of-order rerun).
- One writer per path; `ops/GOALS.md` / `ops/OPS-LOG.md` are main-brain only.
- Pipelines transfer across models; **style mechanisms must be rewritten with matching mechanical checks**.
