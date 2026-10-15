# Contributing

Thanks for your interest. This repository is AI-operated, but human contributions are welcome — especially evidence fixes, new domains, and translations.

## What helps most

1. **New domains** — follow the registry contract (`docs/ARCHITECTURE.md` §3.2). Open an issue before building.
2. **Evidence fixes** — a wrong quote, a dead source link, a mislabeled evidence grade. Small, high-value.
3. **Translations** — improvements to `docs/i18n/zh-CN/` and `docs/i18n/ja/` and the README variants.
4. **Verifier improvements** — make the mechanical checks stricter or faster.

## Ground rules

- **One writer per path**; a PR should touch a coherent scope.
- **Every claim carries an evidence grade + source** (`[自述]/[史料]/[研究]/[归纳]/[推测]`); quotes must be checkable.
- **Run the relevant verifier** and paste its output in the PR description.
- **Never commit third-party media** (videos, clips) — see `.gitignore` and `NOTICE.md`.
- Docs are English (canonical); keep protocol identifiers (`N1–N9`, `C-01–C-18`, grades) untranslated.

## How to add a domain

1. Card directory (one file per card) + index (capability map).
2. Conflict list (or explicit reuse of generic rules + deltas).
3. Output-form mapping (image prompt / web animation / Blender).
4. Intensity mechanism (or an explicit gap marker).
5. Experiments + verifiers (`[UNVERIFIED]` until they pass).
6. Register in `skills/designers-brain/domains.yaml`.
7. Run `python docs/skill/_selfcheck.py` → PASS.

## How to add a card

- Start from `templates/artist_module.md` (painters) or the style-card template (motion).
- Keep evidence grades on every section; add the card to the domain index.
- Run `python knowledge/domains/painters/modules/_extract.py --check` (painters) or the domain's checker.

## Review process

1. Mechanical checks first (verifier output required).
2. Independent review second — a reviewer working from a **clean context** (artifacts + rubric only, no process narrative).
3. "Cannot verify" is a valid verdict; reviews must not inflate.

## License

Contributions are accepted under [MIT](LICENSE) (code) and [CC BY 4.0](LICENSE-CONTENT.md) (content).
