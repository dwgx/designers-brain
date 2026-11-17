# NOTICE — Third-Party Attributions

This repository distills, analyzes, and builds upon third-party material. Media
files that cannot be redistributed (tutorial videos, reference clips) are
**excluded** from the repository (see `.gitignore`).

## Knowledge & card sources

- **mg-styles-15** — https://github.com/Vincentwei1021/mg-styles-15 (MIT).
  Source of the 15 motion-graphics style cards distilled in
  `knowledge/domains/motion-graphics/`. Original card credit: "Claude Code · Opus 5.5".
  The card screenshots and transcript in `.../origin/` derive from this project.
- **video-shotcraft** — https://github.com/Vincentwei1021/video-shotcraft (Apache-2.0, as recorded in the source research). Analyzed in
  `knowledge/domains/motion-graphics/cards/video_shotcraft.md` (analysis only; no code copied).

## Skill-format research archive (`docs/skill/refs/`)

- **superpowers** — https://github.com/obra/superpowers · https://github.com/obra/superpowers-skills (MIT). Format and interaction-protocol research; excerpts archived.
- **agentskills.io** — specification excerpts (https://agentskills.io/specification).
- **Waza** — https://github.com/tw93/Waza (MIT). Routing/infer-first excerpts.
- **huashu-design**, **oil-ui**, **ux-ui-agent-skills** — design-consultant patterns; excerpts archived for research per their source licenses.

## Images

- The public image library holds **739 images** (`knowledge/domains/painters/dossiers/_images/`).
  They are **not uniformly public-domain**: by the central manifest's License-column
  (artwork-level label) accounting, **701 rows are labeled public domain / CC0**
  (The Met Open Access, Art Institute of Chicago CC0, Cleveland Museum of Art CC0,
  PD/PD-Art/PD-US scans on Wikimedia Commons) and **38 are labeled openly
  licensed but attribution-bearing** — see the next section. This 701/38 split is a
  *label accounting convention*, **not** a file-level "credit-free" count.
- **File-level reuse safety:** the authoritative, machine-readable file-level
  classification is `knowledge/domains/painters/dossiers/_images/rights-file-level.json`.
  Under this project's conservative convention **39 of the 739 distributed JPGs
  require attribution** (the 38 below plus `qi_baishi/morning_glory_1950.jpg`),
  699 carry recognized PD/CC0 labels with no stated attribution condition, and
  one (`klimt/the_kiss.jpg`) remains jurisdiction-dependent. The Commons source
  states CC BY-SA 4.0 for the digital reproduction and a PD-Art exception in
  applicable jurisdictions; this project does not choose a jurisdiction. Do not
  interpret null as permission-free or read 701 as 701 credit-free files.
- Per-image source URL, license string and credit line: `knowledge/INDEX.md` and
  `knowledge/domains/painters/dossiers/_images/manifest.md` (single manifest, 逐张明细).
- Copyright-uncleared material is kept in the private layer (`_private/`) and is
  never committed or redistributed (see the manifest's 「私有层例外」 section).

## Images whose manifest License label is not PD/CC0 (38 license-column rows)

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

- The 38 count follows the manifest's License column: a row is listed here when its
  license label is not `Public domain` / `PD-*` / `CC0`. The remaining **701** rows
  carry PD/CC0 labels; that is an artwork-level accounting convention, **not** a
  statement that all 701 distributed JPG files are credit-free (courtesy credit
  still welcome).
- **Composite case (counted in the file-level 39):** `qi_baishi/morning_glory_1950.jpg`
  — the **artwork** is PD-China (Qi Baishi, 1950), but the distributed JPG is a 2023
  photograph by **Jean-Pierre Dalbéra** (Musée Cernuschi, Paris) licensed **CC BY 2.0**
  (Flickr review 2023-02-06). Reuse requires credit to the photographer, the CC BY 2.0
  license, a link to the deed, and an indication of changes. It is counted on the PD
  side of the 701/38 *label* split but is one of the **39 file-level attribution
  rows** in `rights-file-level.json` — the two accounts must not be conflated.
- For definitive per-file reuse terms (including composite PD-artwork + CC-BY-photo
  cases and PD-Art jurisdiction notes), consult
  `knowledge/domains/painters/dossiers/_images/rights-file-level.json`; it is a
  conservative project convention, not a global legal judgment.
- The 744 images in the private layer (`_private/`, 57 artists, incl. Hopper, Kahlo,
  Kngwarreye, Namatjira, O'Keeffe, Rivera) are **copyright-uncleared research copies**
  and are not covered by this NOTICE; they are never redistributed.

## Quotes

- Artist letters, interviews, and scholarship are quoted for research and
  commentary with inline citations; original rights remain with their holders.

## AI provenance

- Portions of this repository's text, code, and images were produced with AI
  agents (see `docs/WORKFLOW.md`). Verification records distinguish implementation,
  executed checks, model review and pending human evaluation; an archived receipt
  does not by itself verify every present-day claim or artifact.
