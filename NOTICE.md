# NOTICE — Third-Party Attributions

This repository distills, analyzes, and builds upon third-party material. Media
files that cannot be redistributed (tutorial videos, reference clips) are
**excluded** from the repository (see `.gitignore`).

## Knowledge & card sources

- **mg-styles-15** — https://github.com/Vincentwei1021/mg-styles-15 (MIT).
  Source of the 15 motion-graphics style cards distilled in
  `knowledge/domains/motion-graphics/`. Original card credit: "Claude Code · Opus 5.5".
  The card screenshots and transcript in `.../origin/` derive from this project.
- **video-shotcraft** — https://github.com/... (Apache-2.0). Analyzed in
  `knowledge/domains/motion-graphics/cards/video_shotcraft*.md` (analysis only; no code copied).

## Skill-format research archive (`docs/skill/refs/`)

- **superpowers** — https://github.com/obra/superpowers · https://github.com/obra/superpowers-skills (MIT). Format and interaction-protocol research; excerpts archived.
- **agentskills.io** — specification excerpts (https://agentskills.io/specification).
- **Waza** — https://github.com/tw93/Waza (MIT). Routing/infer-first excerpts.
- **huashu-design**, **oil-ui**, **ux-ui-agent-skills** — design-consultant patterns; excerpts archived for research per their source licenses.

## Images

- The public image library holds **739 images** (`knowledge/domains/painters/dossiers/_images/`).
  They are **not uniformly public-domain**: **701 are public domain or CC0**
  (The Met Open Access, Art Institute of Chicago CC0, Cleveland Museum of Art CC0,
  PD/PD-Art/PD-US scans on Wikimedia Commons) and **38 are openly
  licensed but attribution-bearing** — see the next section.
- Per-image source URL, license string and credit line: `knowledge/INDEX.md` and
  `knowledge/domains/painters/dossiers/_images/manifest.md` (single manifest, 逐张明细).
- Copyright-uncleared material is kept in the private layer (`_private/`) and is
  never committed or redistributed (see the manifest's 「私有层例外」 section).

## Images not PD/CC0 (38)

These 38 of the 739 images are **not** public-domain/CC0. The underlying artwork is
usually PD; what carries the license is the modern **photograph / scan / museum
reproduction**, or the museum's terms of use. When you reuse, redistribute or
publish any of them (or a derivative of the image file), you **must reproduce the
per-image credit line** recorded in the manifest's License column. Grouped by
source category:

| # | Source category | Count | Files (under `_images/`) | Attribution requirement |
|---|---|---|---|---|
| 1 | Wikimedia Commons — **CC BY-SA 4.0** photographic reproduction of a PD work | 13 | `da_vinci/last_supper` (uploader LoganTheWatermelon) · `michelangelo/david` (photo Livioandronico2013) · `mucha/le_pater_1899` (photo SiefkinDR 2018) · `degas/combing_the_hair_1896` (NGL photo) · `piero_della_francesca/diptych_federico_battista` + `diptych_reverse_triumphs` (photo Sailko / Francesco Bini) · `piero_della_francesca/madonna_di_senigallia` (photo Mongolo1984) · `xu_wei/zahua_scroll_{colophon,leaves,peony,pomegranate}` (photo Augustohai 2017) · `qi_baishi/seal_script_couplet` + `seal_impression_changsha` (photo 陳寅恪) | Credit the photographer/uploader **by name**, name the license (CC BY-SA 4.0), link the license deed, and indicate changes; **ShareAlike** applies to the image file (the PD artwork itself stays PD). |
| 2 | Wikimedia Commons — **CC BY-SA 3.0** (photo of PD design) | 1 | `kandinsky/blaue_reiter_almanac_cover_1912` (photo Goesseln 2010) | Same as #1, with CC BY-SA 3.0. |
| 3 | Wikimedia Commons — **CC BY 3.0** (photo of PD painting) | 1 | `turner/norham_castle_sunrise` (photo Sailko; Tate N01981) | Credit photographer + CC BY 3.0 + license link. |
| 4 | Wikimedia Commons — **CC BY 2.0** (photo of a PD-China work) | 1 | `qi_baishi/lotus_and_insects` (photo Jnzl's Photos) | Credit photographer + CC BY 2.0 + license link. (The painting is PD-China; only the photograph is licensed.) |
| 5 | **ColBase** — ColBase 利用規約 (National Institutes for Cultural Heritage, Japan) | 14 | `ito_jakuchu/` ×9 (`doshoku_saie_gunkei`, `doshoku_saie_rogan`, `doshoku_saie_gunyo`, `doshoku_saie_kikka`, `kasonehanzu`, `genpo_yoka`, `shoubai_gunkei_zu_byobu`, `kaiboji_gunkei_zu`, `ishidoro_zu_byobu`) · `kitagawa_utamaro/` ×5 (`fujin_sogaku_juttai_uwaki`, `musume_hidokei_uma`, `takashima_ohisa_fan`, `toji_zensei_bijin_takigawa`, `yamauba_kintaro_kurieda`) | Must display the credit line **「出典：ColBase（https://colbase.nich.go.jp/）」** (source: ColBase) next to the image; no endorsement implication; third-party rights (e.g. works still in copyright) excluded. |
| 6 | **National Palace Museum, Taipei** — 政府資料開放授權條款 (Open Government Data License, CC BY 4.0-compatible) | 8 | `fan_kuan/wanghui_fa_fankuan` · `qiu_ying/han_palace_d_full_scroll`, `han_palace_d_konghou`, `han_palace_d_serving_ladies`, `han_palace_d_stairs_attendant`, `han_palace_s06_peacock_kids`, `han_palace_s08_flower_picking`, `han_palace_s12_doucao_reading` | Attribute **國立故宮博物院 (National Palace Museum)** as the source, state the license and link it; CC BY 4.0-compatible terms (attribution required, no additional restrictions). |
| | **Total** | **38** | | |

Notes:

- The count follows the manifest's License column: a row is listed here when its
  license is not `Public domain` / `PD-*` / `CC0`. The remaining **701** rows are
  PD/CC0 and need no attribution (courtesy credit still welcome).
- Borderline row, not counted above: `qi_baishi/morning_glory_1950.jpg` — the
  **artwork** is PD-China and is counted on the PD side, but the photograph is
  **CC BY 2.0** (Jean-Pierre Dalbéra), so credit the photographer when reusing that
  file.
- The 744 images in the private layer (`_private/`, 57 artists, incl. Hopper, Kahlo,
  Kngwarreye, Namatjira, O'Keeffe, Rivera) are **copyright-uncleared research copies**
  and are not covered by this NOTICE; they are never redistributed.

## Quotes

- Artist letters, interviews, and scholarship are quoted for research and
  commentary with inline citations; original rights remain with their holders.

## AI provenance

- Portions of this repository's text, code, and images were produced with AI
  agents (see `docs/WORKFLOW.md`); all outputs pass the repository's evidence
  and verification protocols.
