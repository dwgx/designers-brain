# Designer seed research prototype — `enigmatriz`

> **RESEARCH PROTOTYPE — local mechanism hypothesis only. NOT proven author method. NOT E2/E3 evidence. NOT human aesthetic approval.**

This directory preserves an already-produced local engineering prototype for the E1/seed
designer handle `enigmatriz`. The designer domain is **not active** in this candidate
(`skills/designers-brain/domains.yaml` lists only `painter` and `mg-motion`), and all
seven designer seeds remain **E1 / seed** with E2/E3/active gates unmet.

## What is here
- `prototype/` — the original mechanism code (`build.py`), run parameters
  (`config.json`), small evidence outputs (`outputs/`) and the original run/review
  receipts, re-packaged from the historical staging prototype.
- `prototype/README.md`, `prototype/RESULT.md`, `prototype/S11B-CALIBRATION.md` —
  what was actually implemented and measured, including honest calibration of claims.
- `../PACKAGE-MANIFEST.json` — per-file original SHA256, packaged SHA256 and a flag
  showing whether private absolute locators were scrubbed.
- `prototype/vendor/metrics.py` — a self-contained copy of the project-owned METRIC-PILOT
  numeric-utility fixture (`srgb8_to_Lstar`/`lum_hist`/`lap_var`), whose SHA256 matches the
  `module_sha256` declared in `config.json`. Added so the prototype reproduces in a clean
  relocated checkout; `build.py` was given one extra local resolution candidate. The
  mechanism itself is unchanged (fresh rerun `checks.json` is identical to the packaged one).

## Status (unchanged)
- Evidence level: **E1**. E2/E3/active: **not promoted**.
- Prototype sub-artifacts are successful local mechanism demonstrations; they are kept
  so they do not vanish behind the parent task's blocked/uncertain status. They do **not**
  satisfy the parent goal's `required_artifact_kinds` and are **not** an E3 reproduction.
- No generated image service, no third-party/author/client media, no credentials, no RNG
  (where declared), no network generation. Aesthetic/design validity is `pending_human`.

## Privacy / provenance
Historical text contained private absolute workspace locators. On packaging these were
scrubbed to logical labels (`SOURCE@designers-brain`, `OLD_CAMPAIGN_ROOT`,
`CAMPAIGN_PACKAGE`, `<home>`); original byte hashes are retained in
`../PACKAGE-MANIFEST.json` so historical identity is not rewritten. The read-only
source of truth for the seed dossier and media is the SOURCE designers domain.

See `prototype/README.md` for exact reproduction commands and boundary statements.
