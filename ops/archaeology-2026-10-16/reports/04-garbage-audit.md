# 04 · 项目树垃圾/陈旧件审计（ProjectGarbageAudit · Wave1）

> 范围：`D:/Project/Designers_Brain` 根目录未分类件 + 指定目录候选。**只读审计**：未移动、未删除、未改 `.gitignore`。
> 审计时刻：2026-10-16 ≈08:05 JST（会话内相对时间换算，标 ≈）。
> 口径：逐件 peek ≤10 行判内容；引用检查 = 全仓 grep **文件名/路径字符串**（含被 gitignore 的件；`.git` 无命中）；吸收对照 = 对照 `knowledge/` 产物逐条抽样。
> 建议集：KEEP / QUARANTINE（可移入 `quarantine/Designers_Brain/`，不删除）/ INSPECT（先核后动）。

---

## 0 · 摘要

1. **根目录未分类件共 56 个 ≈2.4 MB**：`_tmp_*.html` ×50、`_tmp_*` 非 HTML ×4（quotes.json / corr2.txt / decovivago.js / chrono.json）、`louvre_search1.html`、`omp-session-*.html`。另有目录 `_tmp_michel/`（16 件 ≈4.0 MB）与 `_scratch/`（10 子目录）。任务书估「~24 个 `_tmp_*.html`」，**实测 50 个**（18 组信件×2 + let155×2 + 14 个站点/维基页）。
2. `_tmp_*.html` 全部为 **Van Gogh Letters（vangoghletters.org）抓取缓存**（BioVanGogh/wave14 所用；主脑判语见 09-session-condensed.txt L970/L992/L1067）。核心引文已吸收进 `dossiers/van_gogh.md` §11 与 `_corpus/van_gogh.md`（抽样 12 项、直接命中 ≥10，见 §2）→ **整批 QUARANTINE**。
3. `_tmp_michel/` 16 件 = 米开朗基罗来源集（Condivi / Vasari / Milanesi / Gutenberg《Le lettere》）；A-32 已收口，语料 #16 逐字命中 → **QUARANTINE**。
4. 纯垃圾（无需再核）：`_tmp_yale.html`（Cloudflare 挑战页）、`louvre_search1.html`（WAF 拦截页）→ QUARANTINE。
5. `omp-session-2026-10-15T22-30-09-428Z_*.html`（600 KB，10-16 ≈07:40 落盘）：OMP「Session Export」页（内嵌 base64 会话数据）；本审计环境浏览器通道断开、未能解码定性 → **INSPECT**（移交 SessionStoreRecon/ExportHtmlIdent 线索）。
6. `_scratch/`：9 个画家子目录（原始抓取件，对应 dossier 均已交付）→ QUARANTINE 候选；**`rc-test/` 例外保留**（属当前考古操作的 robocopy 测试，11 分钟前活跃）。
7. `_private/` 完整性 OK（58 份艺术家清单 + README + 总索引占位；双保险在）——**按权利隔离层要求：只审完整性，不提议动**。
8. 目录候选 `experiments/`、`docs/skill/{draft,refs,tests,walkthrough_01}`、`skills/`、`templates/` 均为**在用资产**（引用 35–138 文件）→ **KEEP**。
9. `.gitignore` 覆盖：`_private/` ✓、`/_scratch/` ✓、`/_tmp_*` ✓（含 `_tmp_michel` 与全部非 HTML `_tmp_*`）；`louvre_search1.html`、`omp-session-*.html` **未覆盖**（§6）。

---

## 1 · 根目录未分类文件 —— 逐件表（56 件）

### 1.1 `_tmp_*.html` 信件碎片 —— 38 件（19 组；≈0.61 MB）

> 是什么：vangoghletters.org 信件页的 body 片段（`_translation`=英译 / `_original_text`=荷·法原文；无 `<title>`，故标题扫描不见）。抓取批 ≈10-15 23:30–24:00 JST（页面生成戳 14:31–14:36 UTC = 23:31–23:36 JST）。
> 引用：**全部 0**（家族串 `_tmp_*.html` 在 09-session-condensed.txt 出现 3 处；仅 `_tmp_001_original_text.html` 在 L971 目录清单被点名 1 次）。吸收：见 §2。

| 文件 | 大小 | 日期 | 引用 | 建议 |
|---|---|---|---|---|
| `_tmp_001_translation.html` | 3.3 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_001_original_text.html` | 2.6 KB | 10-15 ≈23:5x | 1 | QUARANTINE |
| `_tmp_156_translation.html` | 16.7 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_156_original_text.html` | 8.8 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_497_translation.html` | 17.8 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_497_original_text.html` | 16.1 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_569_translation.html` | 16.6 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_569_original_text.html` | 11.0 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_574_translation.html` | 26.5 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_574_original_text.html` | 18.7 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_677_translation.html` | 19.0 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_677_original_text.html` | 15.6 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_682_translation.html` | 29.0 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_682_original_text.html` | 20.1 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_691_translation.html` | 21.7 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_691_original_text.html` | 15.6 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_741_translation.html` | 24.0 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_741_original_text.html` | 15.3 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_769_translation.html` | 2.0 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_769_original_text.html` | 1.3 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_776_translation.html` | 30.4 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_776_original_text.html` | 23.9 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_783_translation.html` | 18.9 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_783_original_text.html` | 11.4 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_819_translation.html` | 15.6 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_819_original_text.html` | 9.0 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_881_translation.html` | 10.8 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_881_original_text.html` | 7.9 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_899_translation.html` | 5.9 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_899_original_text.html` | 3.3 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_900_translation.html` | 6.4 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_900_original_text.html` | 4.5 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_901_translation.html` | 9.6 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_901_original_text.html` | 6.0 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_902_translation.html` | 13.4 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_902_original_text.html` | 9.8 KB | 10-15 ≈23:5x | 0 | QUARANTINE |
| `_tmp_let155.html`（信 155 全页） | 100.8 KB | 10-15 ≈23:31 | 0 | QUARANTINE |
| `_tmp_let155_orig.html`（信 155 原文） | 34.4 KB | 10-15 ≈23:31 | 0 | QUARANTINE |

### 1.2 `_tmp_*` 其余件 —— 16 件（≈1.18 MB）

> 均为同批抓取的站点元页 / 维基缓存 / 工作件。引用：全部 0（逐件核过 `_tmp_(about|chrono|corr|lw|letters_list|context1|search|wiki|yale|quotes|decovivago|let155)`）。

| 文件 | 大小 | 日期 | 引用 | 建议 | 是什么 |
|---|---|---|---|---|---|
| `_tmp_about.html` | 31.7 KB | 10-15 ≈23:5x | 0 | QUARANTINE | 站点「About this edition」（「903 封」口径来源，已入 dossier §10/§12 注） |
| `_tmp_chrono.html` | 230.5 KB | 10-15 ≈23:5x | 0 | QUARANTINE | 站点「Chronology」页（§11 年表来源族） |
| `_tmp_chrono.json` | 53.2 KB | 10-15 ≈23:5x | 0 | QUARANTINE | 同上，JSON 版（含「Groot-Zundert, Markt 26」，已入 dossier §11） |
| `_tmp_context1.html` | 109.4 KB | 10-15 ≈23:5x | 0 | QUARANTINE | 「Biographical & historical context」页 |
| `_tmp_corr.html` | 6.4 KB | 10-15 ≈23:5x | 0 | QUARANTINE | 「Correspondents」页（v1） |
| `_tmp_corr2.html` | 64.8 KB | 10-15 ≈23:5x | 0 | QUARANTINE | 「Correspondents」页（v2 抓取，较大版） |
| `_tmp_corr2.txt` | 15.5 KB | 10-15 ≈23:5x | 0 | QUARANTINE | 通信统计文摘（Theo 651/820 段） |
| `_tmp_letters_list.html` | 132.6 KB | 10-15 ≈23:5x | 0 | QUARANTINE | 「The letters」总表页 |
| `_tmp_lw.html` | 18.8 KB | 10-15 ≈23:5x | 0 | QUARANTINE | 「Van Gogh as a letter-writer」文 |
| `_tmp_search1.html` | 7.8 KB | 10-15 ≈23:36 | 0 | QUARANTINE | 站内搜索「preoccupy」结果（→定位 let783，已入语料 #30） |
| `_tmp_search2.html` | 21.7 KB | 10-15 ≈23:36 | 0 | QUARANTINE | 站内搜索第二页/第二词结果 |
| `_tmp_wiki_nc.html` | 191.0 KB | 10-15 ≈23:5x | 0 | QUARANTINE | 维基《The Night Café》（Yale 页 403 的替代来源，dossier §12 第 5 件） |
| `_tmp_wiki_snr.html` | 226.7 KB | 10-15 ≈23:5x | 0 | QUARANTINE | 维基《Starry Night Over the Rhône》（Orsay 页 404 的替代来源，§12 第 6 件） |
| `_tmp_yale.html` | 5.5 KB | 10-15 ≈23:5x | 0 | QUARANTINE | **纯垃圾**：Cloudflare「Just a moment…」挑战页（Yale 抓取失败件） |
| `_tmp_decovivago.js` | 90.3 KB | 10-15 ≈23:5x | 0 | QUARANTINE | 站点前端 JS 合辑（无独立价值） |
| `_tmp_quotes.json` | 2.6 KB | 10-15 ≈23:5x | 0 | QUARANTINE | 引文工作件（155fire/155mel/156/497/569/677/682/691/741/783/881/899/900/902；多数已入语料） |

### 1.3 其他根未分类件 —— 2 件

| 文件 | 大小 | 日期 | 引用 | 建议 | 说明 |
|---|---|---|---|---|---|
| `louvre_search1.html` | 4.5 KB | 10-16 ≈04:0x | 1 | QUARANTINE | **纯垃圾**：WADP「I am not a robot」拦截页（Louvre 站内搜索抓取失败件；命中：`knowledge/.../_scratch/rivera/selfcheck_output.txt` L78 记 `?? louvre_search1.html`） |
| `omp-session-2026-10-15T22-30-09-428Z_01a141af-….html` | 600.4 KB | 10-16 ≈07:40 | 0 | **INSPECT** | OMP「Session Export」自包含页（内嵌 base64 会话数据；会话 01a141af…，起于 07:30:09 JST）。全仓无该会话 ID/文件名的引用；本审计浏览器通道断开未能解码 → 先定性（若本仓相关 → 归 F: `sessions/`；否则 quarantine） |

---

## 2 · `_tmp_*` 吸收对照表（对照 `knowledge/` 产物）

> 方法：抽取源件中的特征引文/事实 → grep `knowledge/`。结果如下（12 项，直接命中 ≥10）：

| # | 特征引文/事实（源件） | knowledge 落点 | 命中 |
|---|---|---|---|
| 1 | `Dikwijls denk ik aan U beiden…`（let899） | `_corpus/van_gogh.md` #32 + dossier §11 S12 | ✓ 逐字 |
| 2 | `mélancholie active`（let155） | `_corpus/van_gogh.md` #22 + dossier §11 S2 | ✓ 逐字 |
| 3 | `Tel a un grand foyer dans son âme…`（quotes.json "155fire"） | `_corpus/van_gogh.md` #21 | ✓ 逐字 |
| 4 | `Si seulement je puis continuer…`（let156） | dossier §11（S3 段） | ✓ 逐字 |
| 5 | `handenarbeid…`（let497） | `_corpus/van_gogh.md` #24 | ✓ 逐字 |
| 6 | `charretiers…sommet de la colline`（let900，提奥） | `_corpus/van_gogh.md` #35 + dossier §11 S14 | ✓ 逐字 |
| 7 | `obelisque egyptienne`（let783） | `_corpus/van_gogh.md` #30 | ✓ 逐字 |
| 8 | `Zundert…nid de pie`（let741） | `_corpus/van_gogh.md` #29 | ✓ 逐字 |
| 9 | 「Groot-Zundert, Markt 26」出生（chrono.json） | dossier §11 一（家庭与早年） | ✓ |
| 10 | 「the 903 surviving letters」（about.html） | dossier §10/§12 注（「About 页原文」） | ✓ |
| 11 | 《The Night Café》/《Starry Night Over the Rhône》作品条目（wiki_nc / wiki_snr；Yale/Orsay 直连 403/404 的替代） | dossier §12 第 5/6 件（含「直读失败」注） | ✓ 间接 |
| 12 | 搜索「preoccupy」→ let783 选集 | 用于选信；let783 已入语料 #30 | ✓ 间接 |

旁证（会话记录）：09-session-condensed.txt **L970**（主脑判语「`_tmp_*.html` files at root … van_gogh letters pages … from BioVanGogh」）、**L992**（「40 letter pages downloaded」）、**L1067**（BioVanGogh 回执「先核盘 → **复用缓存 `_tmp_*`** → 逐节写盘完成」）。
结论：`_tmp_*` 为**已吸收的原始抓取缓存**；无在途引用；可整批移入 quarantine（不删除，家族「只进不删」）。

---

## 3 · `_tmp_michel/`（16 件 ≈4.0 MB）—— 已吸收，可移

| 文件 | 大小 | 是什么 |
|---|---|---|
| `wiki_michel.txt` | 44.5 KB | Wikipedia《Michelangelo》缓存 |
| `wiki_david.txt` | 36.7 KB | Wikipedia《David》缓存 |
| `wiki_volta_it.txt` | 30.8 KB | it.wiki《Volta della Cappella Sistina》缓存 |
| `wiki_sistine.txt` | 67.4 KB | Wikipedia《Sistine Chapel ceiling》缓存 |
| `wiki_tomb.txt` | 21.0 KB | Wikipedia《Tomb of Julius II》缓存 |
| `gut_lettere.txt` | 1.1 MB | Gutenberg《Le lettere di Michelangelo Buonarroti》（27,163 行；语料 #16 逐字命中） |
| `milanesi.txt` | 1.1 MB | Milanesi 1875 版书信集转录（与 #16–22 同源） |
| `vasari_wrap.txt` | 288.9 KB | Vasari《Le vite》米氏篇转写 |
| `vasari_clean.txt` | 286.5 KB | 同上清洗版 |
| `vasari_rendered.html` | 457.9 KB | 同上渲染件 |
| `vasari_raw.txt` | 330 B | it.wikisource 转写指针（`<pages index="Vasari …" from=363 to=444 />`） |
| `condivi_wrap.txt` | 129.3 KB | Condivi《Vita》1553 转写 |
| `condivi_clean.txt` | 128.3 KB | 同上清洗版 |
| `condivi_critical.txt` | 132.3 KB | 同上校勘版（Versione critica） |
| `condivi_full.txt` | 178.3 KB | 同上全量版 |
| `condivi_main.txt` | 677 B | it.wikisource 转写指针（`<pages index="Condivi …" from=13 to=115 />`） |

**吸收证据**：A-32 已 done（GOALS：§11 2816 字 + 35 行年表 + 14 来源；语料 +7→22；引文 7/7）；`fantasia grande`（语料 #16）逐字命中 `gut_lettere.txt` L847–851；dossier §11 明述「以 Condivi（1553）与 Vasari（1568）两传为经、Milanesi 编 1875 版为纬」。
**引用**：0（全仓无 `_tmp_michel` 字符串）。**建议**：QUARANTINE（如需扩信集可从 quarantine 取回）。

---

## 4 · 目录候选 —— 逐项

| 候选 | 大小 | 日期（≈） | 引用 | 建议 | 备注 |
|---|---|---|---|---|---|
| `_scratch/` | 200+ 件（glob 上限截断，未 du） | 06:0x（rc-test 07:55） | 跨层 ≥10 处（.gitignore / OPS-LOG / condensed / 各 RESUME 自引） | **QUARANTINE（9 画家子目录）+ rc-test 保留** | 子目录：xu_beihong / behzad / p2_rembrandt / qi_baishi / el_salahi / friedrich / bosch / munch / bio_hokusai（对应 dossier 均已交付）；rc-test = 当前考古操作的 robocopy 测试（源：image_probes 会话目录；1 文件 12.5k；07:55:31） |
| `_private/` | images_hi_res 55+ 子目录；books 60+ 件（单件至 120 MB）；papers 40+ 件；videos 空 | 06–07:0x | 路径自引为主；公开文档按纪律不写私有路径 | **不动（只审完整性）** | 完整性：58 份 `INVENTORY_*.md` + `README.md` + 总索引（占位「暂无条目」，待「大师参考库」回填）；双保险 = `.gitignore` + `.git/info/exclude`（原文「# Private research layer — local double-insurance」）；抽查 chardin 10 件与清单一致 ✓；缺口：`videos/` 为空目录 |
| `experiments/` | ≈1.2 GB 级（大头帧序列/校验图，多被 gitignore；E 系列图件为 MB 级） | 21:0x–23:0x | **≥89 文件**（README×3 / AGENTS / MIGRATION / skill_spec / skill_ecosystem / walkthrough 脚本 / transfer_guide / conflicts / 各 checks.md / GOALS…） | **KEEP** | E1_t1 / E1_t1b / E1_t1c / E2_t1 + anim_test_01/02/03_blender + design.md；各带 `_verify*.py`（重构后回归全 PASS，MIGRATION §4） |
| `docs/skill/draft/` | 9.1 KB（1 件：SKILL.md） | ≈23:0x | 6+ 文件（build_receipt / _selfcheck / skill_spec / GOALS S-02…） | **KEEP** | 历史草案（build_receipt 明示「draft 保留为历史草案」） |
| `docs/skill/refs/` | 23 件 ≈0.17 MB | 21–22:0x | 5+ 文件（NOTICE.md / _selfcheck / skill_spec / skill_ecosystem / build_receipt…） | **KEEP** | superpowers 9 / spec 5 / design-packs 3 / waza 2 / zh 2 / community 1（GOALS S-01「refs 留档 23 文件」吻合） |
| `docs/skill/tests/` | 4 件 ≈35 KB | 22–23:0x | 4+ 文件（GOALS S-04/S-05 / test_report / session-digest / condensed…） | **KEEP** | red/green_transcript + autotrigger_probe + （上级 test_report） |
| `docs/skill/walkthrough_01/` | 12 件 + final/ + candidates/（图件 MB 级） | ≈23:0x | 10+ 文件（README×3 / MIGRATION / GOALS S-05 / condensed…） | **KEEP** | S-05 走查全链产物（机械 64/64） |
| `skills/` | 包 ≈20 KB 级（SKILL.md + references×9 + domains.yaml + agents） | ≈01:0x | **≥35 文件**（README×3 / ARCHITECTURE×3 / PROTOCOLS×3 / WORKFLOW×3 / CONTRIBUTING / _selfcheck / build_receipt…） | **KEEP** | 活跃 skill 包（junction ×4 解析） |
| `templates/` | 5 件 ≈34 KB | 17–23:0x | **138 文件**（全部画家档案/模块/实验/文档引用） | **KEEP** | style_card / design_brief / determinism_contract / artist_module / loop_goal |

---

## 5 · QUARANTINE 清单（可执行）

> 目标位：`quarantine/Designers_Brain/`（家族口径；不删除，收据由主脑记）。备选落点：按 MIGRATION 先例（`_tmp_picasso`/`_scratch/turner` → `knowledge/domains/painters/_scratch/`）并入本地 scratch——两选一，由主脑裁定；本清单以 quarantine 为默认。
> 前置：无（A–C 均已吸收/纯垃圾，无在途引用）。**本审计只读，未执行任何移动。**

**A. 根 `_tmp_*` —— 54 件 ≈1.79 MB**
- A1. 信件碎片 38 件 ≈0.61 MB：`_tmp_{001,156,497,569,574,677,682,691,741,769,776,783,819,881,899,900,901,902}_{translation,original_text}.html` + `_tmp_let155.html` + `_tmp_let155_orig.html` —— 理由：已吸收（§2 抽样命中）；原始缓存可再取。
- A2. 站点/维基件 16 件 ≈1.18 MB：`_tmp_about.html`、`_tmp_chrono.html`、`_tmp_chrono.json`、`_tmp_context1.html`、`_tmp_corr.html`、`_tmp_corr2.html`、`_tmp_corr2.txt`、`_tmp_letters_list.html`、`_tmp_lw.html`、`_tmp_search1.html`、`_tmp_search2.html`、`_tmp_wiki_nc.html`、`_tmp_wiki_snr.html`、`_tmp_yale.html`、`_tmp_decovivago.js`、`_tmp_quotes.json` —— 理由：已吸收/纯垃圾（yale=挑战页、decovivago=站点 JS）。

**B. `_tmp_michel/` —— 16 件 ≈4.0 MB**
- `wiki_{michel,david,volta_it,sistine,tomb}.txt`、`gut_lettere.txt`、`milanesi.txt`、`vasari_{wrap,clean,rendered.html,raw}.txt`、`condivi_{wrap,clean,critical,full,main}.txt` —— 理由：已吸收（A-32；语料 #16 逐字命中）。

**C. 根其他 —— 1 件**
- `louvre_search1.html`（4.5 KB）—— 理由：WAF 拦截页，无内容价值。

**小计（A–C）：71 件 ≈5.75 MB。**

**D. 条件项（先核后动；不计入小计）**
- `_scratch/` 9 个画家子目录（xu_beihong、behzad、p2_rembrandt、qi_baishi、el_salahi、friedrich、bosch、munch、bio_hokusai）—— 已交付画家的抓取件；建议随收口波核后移入（**rc-test/ 保留至操作收尾**）。
- `omp-session-2026-…html`（600 KB）—— 待定性（INSPECT；若判为垃圾再并入）。
- 附带发现（非清单）：`knowledge/_private/` 空目录（repin 工误建；已被 ignore 覆盖）——建议收尾时清理。

---

## 6 · `.gitignore` 覆盖检查

| 路径 | 已忽略？ | 依据 | 备注 |
|---|---|---|---|
| `_private/` | ✅ | `.gitignore`「Private research layer (never commit)」+ `.git/info/exclude`「# Private research layer — local double-insurance」 | 双保险；check-ignore 实测通过（rivera 自检输出） |
| `_scratch/`（根） | ✅ | `.gitignore`「Worker scratch/temp (local only)」`/_scratch/` | — |
| `_tmp_*`（全部，含 `_tmp_michel/`、`_tmp_quotes.json` 等） | ✅ | `.gitignore` `/_tmp_*` | 覆盖本批全部 54+16 件 |
| `knowledge/domains/painters/_scratch/` | ✅（附） | `.gitignore` 同名条目 | 与本批 `_scratch/` 并存的另一处本地层 |
| `louvre_search1.html` | ❌ **未覆盖** | — | 若留树会出现在 `git status`（未跟踪） |
| `omp-session-*.html` | ❌ **未覆盖** | — | 同上 |
| `experiments/*/ref/**`（媒体） | 部分 ✅ | mkv/mp4/webm 条目 | 其余实验件为在库资产 |

> 注：本审计**未修改** `.gitignore`（非目标）；上表仅报告事实，供主脑处置时参考。

---

## 7 · 方法与限制

- 引用检查：全仓 grep（含被 gitignore 的件；`.git` 目录无命中）；命中 = **文件名字符串出现在某文件内容中**；「0 命中」仅表示「仓库内无指向它的引用」，不代表内容无价值（本批价值判断依据为吸收对照）。
- mtime 为审计时的相对读数换算（审计时刻 ≈08:05 JST），标 ≈；页面内嵌生成戳用于交叉校正。
- `omp-session-*.html` 未能解码定性：本环境浏览器通道断开（重试 3 次失败）；其内嵌 base64 会话数据可由主脑侧任一可用通道解码。
- 本报告为**只读审计结论**：未移动、未删除、未改 `.gitignore`；所有处置动作留待主脑/收口波执行。

## 附录 · 根目录「未分类文件」全表说明

§1 即全表（56 件 = 50 `_tmp_*.html` + 4 `_tmp_*` 非 HTML + 2 孤立 HTML）。根目录其余文件均属**标准仓库件**（`.gitignore`/`.gitattributes`/`LICENSE`/`LICENSE-CODE`/`NOTICE.md`/`README{.md,.zh-CN.md,.ja.md}`/`AGENTS.md`/`CLAUDE.md`/`CODE_OF_CONDUCT.md`/`SECURITY.md`/`CONTRIBUTING.md`）与目录（`ops/`、`knowledge/`、`docs/`、`templates/`、`skills/`、`experiments/`、`.agents/`、`.claude-plugin/`、`.codex-plugin/`、`_private/`、`_scratch/`、`_tmp_michel/`）——不属未分类，未列入。

---
> 生成：ProjectGarbageAudit（Wave1）· 2026-10-16 · 源文件：`local://reports/04-garbage-audit.md`（待主脑收编至 `ops/archaeology-2026-10-16/reports/04-garbage-audit.md`）。
