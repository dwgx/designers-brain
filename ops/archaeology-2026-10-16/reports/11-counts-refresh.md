# 11 · Counts Refresh — README/ROADMAP 三语计数批修（DB-4 / I02）

> 写手：CountsRefresh（DB-4/I02 批修单）｜日期：2026-10-16｜状态：**完成（6 文件机械改数；未 commit；本报告为本单唯一新增产物）**
> 口径来源：`08-absorb-check.md` §2 项 1（+ §1 表行 4）；现口径复核 = 2026-10-16 盘上实（`_index.md` · `_corpus/INDEX.md` · `_images/manifest.md` · `_extract.py --check` 实跑）
> 范围：`README.md` · `README.zh-CN.md` · `README.ja.md` · `docs/ROADMAP.md` · `docs/i18n/zh-CN/ROADMAP.md` · `docs/i18n/ja/ROADMAP.md`——**纯机械改数**；其余数字/文案未动；未 commit；未触碰其它文件。

**一句话结论**：18 处过期计数按现口径全部替换（**62 / 62 / 1613 / 618 / 186**）；六文件改后「全变体扫描」= **0 残留**；全仓 6 模式残留 109 处 / 45 文件已全部归类——其中**同类漂移·本批范围外 8 处（`docs/ARCHITECTURE.md` 三版 + `docs/WORKFLOW.md` 两版）未动、待主脑排期**；其余为历史记录 / 不同语境 / 本地层（均合理，见 §3.2）。

---

## §1 口径核验（2026-10-16 盘上实）

| 计数 | 旧值 | **采用值** | 核验证据 |
|---|---|---|---|
| 画家档案 | 11 | **62** | `dossiers/_index.md` 主表「**合计 62 位**」（wave18/19/20 并入）；磁盘实计 72 = 62 + wave21 十位（「未纳入（在产）」，含 xu_wei 已落盘） |
| 模块卡 | 11 | **62** | `modules/` 实计 62 卡（+README+`_extract.py`）；脚本头注「62 份档案 → 62 张卡」 |
| 逐字校验 | 33 | **186** | 复跑 `python knowledge/domains/painters/modules/_extract.py --check` → `checks=186 ok=186 fail=0   # 62 卡 × §8.1/§8.2/§4` |
| 语料引文 | 126 | **1613** | `_corpus/INDEX.md`「**合计 62 文件 1613 条**」 |
| 公开图 | 33 | **618** | `_images/manifest.md`「**现共 62 位画家 / 公开 618 张**」（另有私有层例外 676 张，分开记） |

> **62 / 72 说明**：主句统一用 **62**（名册口径）；磁盘 72 含 wave21 十位（xu_beihong / li_keran / sher_gil / tarsila / chen_hongshou / xu_wei / hogarth / mir_sayyid_ali / de_chirico / rockwell）。「62 in registry / 72 on disk」注记**未插入正文**——理由与备选落点见 §4-①。

## §2 六文件 before → after（逐条）

### ① `README.md` — 3 行 / 5 数
| 行 | before | after |
|---|---|---|
| L16 | `**11 painter dossiers**` · `126 sourced quotes` · `33 public-domain artworks` | `**62 painter dossiers**` · `1613 sourced quotes` · `618 public-domain artworks` |
| L17 | `**11 composable module cards**` | `**62 composable module cards**` |
| L45 | `# module-card verbatim check (33 checks)` | `# module-card verbatim check (186 checks)` |

### ② `README.zh-CN.md` — 3 行 / 5 数
| 行 | before | after |
|---|---|---|
| L19 | `**11 份画家档案**` · `126 条带来源引文` · `33 件公有领域作品` | `**62 份画家档案**` · `1613 条带来源引文` · `618 件公有领域作品` |
| L20 | `**11 张可组合模块卡**` | `**62 张可组合模块卡**` |
| L48 | `(33 checks)` | `(186 checks)` |

### ③ `README.ja.md` — 3 行 / 5 数
| 行 | before | after |
|---|---|---|
| L19 | `**画家ドシエ（資料ファイル）11 件**` · `出典付き引用 126 件` · `パブリックドメイン作品 33 点` | `**画家ドシエ（資料ファイル）62 件**` · `出典付き引用 1613 件` · `パブリックドメイン作品 618 点` |
| L20 | `**合成可能なモジュールカード 11 枚**` | `**合成可能なモジュールカード 62 枚**` |
| L48 | `(33 checks)` | `(186 checks)` |

### ④ `docs/ROADMAP.md` — L7 / 5 数
`11 dossiers`→`62` · `126 sourced quotes`→`1613` · `33 PD artworks`→`618` · `11 composable module cards`→`62` · `(33/33 verbatim checks)`→`(186/186)`

### ⑤ `docs/i18n/zh-CN/ROADMAP.md` — L10 / 5 数
`11 份档案`→`62` · `126 条`→`1613` · `33 件`→`618` · `11 张`→`62` · `（33/33 逐字校验）`→`（186/186）`

### ⑥ `docs/i18n/ja/ROADMAP.md` — L10 / 5 数
`11 件`→`62` · `126 件`→`1613` · `33 点`→`618` · `11 枚`→`62` · `（逐語チェック 33/33）`→`（186/186）`

> 合计 **10 行 / 18 数**；`git diff --stat`（六文件）= `6 files changed, 12 insertions(+), 12 deletions(-)`。before 全文复现：`git diff -- <file>`（本批 diff 仅含这些行）。

## §3 复核 grep

### 3.1 六文件（改后；含变体集，期望空）

命令（变体集 = `33 checks|11 painter|126 sourced|33 public-domain|11 位|11 张|33/33|11 份|11 件|11 枚|126 条|126 件|33 件|33 点`）：

```
$ grep -nE "33 checks|11 painter|126 sourced|33 public-domain|11 位|11 张|33/33|11 份|11 件|11 枚|126 条|126 件|33 件|33 点" \
    README.md README.zh-CN.md README.ja.md docs/ROADMAP.md docs/i18n/zh-CN/ROADMAP.md docs/i18n/ja/ROADMAP.md
（无输出；EXIT=1 —— 六文件残留 = 0 ✓）
```

改后状态（`grep -n "62\|1613\|618\|186"`，剔 http/badge/日期噪声）：

```
README.md:16:- **62 painter dossiers** (da Vinci, Michelangelo, Van Gogh, Monet, Picasso, Cézanne, Matisse, Hokusai, Caravaggio, Vermeer, Dürer) — ~300 lines of evidence each, 1613 sourced quotes, 618 public-domain artworks.
README.md:17:- **62 composable module cards** + **15 motion-graphics style cards** (10-second animation skeletons).
README.md:45:# module-card verbatim check (186 checks)
README.zh-CN.md:19:- **62 份画家档案**（达·芬奇、米开朗基罗、梵高、莫奈、毕加索、塞尚、马蒂斯、葛饰北斋、卡拉瓦乔、维米尔、丢勒）——每份约 300 行证据、1613 条带来源引文、618 件公有领域作品。
README.zh-CN.md:20:- **62 张可组合模块卡** + **15 张动态图形风格卡**（10 秒动画骨架）。
README.zh-CN.md:48:# module-card verbatim check (186 checks)
README.ja.md:19:- **画家ドシエ（資料ファイル）62 件**（ダ・ヴィンチ、ミケランジェロ、ファン・ゴッホ、モネ、ピカソ、セザンヌ、マティス、北斎、カラヴァッジョ、フェルメール、デューラー）——各約 300 行のエビデンス、出典付き引用 1613 件、パブリックドメイン作品 618 点。
README.ja.md:20:- **合成可能なモジュールカード 62 枚** + **モーショングラフィックスのスタイルカード 15 枚**（10 秒アニメーションの骨格）。
README.ja.md:48:# module-card verbatim check (186 checks)
docs/ROADMAP.md:7:- **Domain #1 — painters**: 62 dossiers (~300 lines each) + 1613 sourced quotes + 618 PD artworks + 62 composable module cards (186/186 verbatim checks).
docs/i18n/zh-CN/ROADMAP.md:10:- **领域 #1 —— 画家**：62 份档案（每份约 300 行）+ 1613 条带来源引文 + 618 件公有领域作品 + 62 张可组合模块卡（186/186 逐字校验）。
docs/i18n/ja/ROADMAP.md:10:- **ドメイン #1——画家**：ドシエ（資料ファイル）62 件（各約 300 行）+ 出典付き引用 1613 件 + パブリックドメイン作品 618 点 + 合成可能なモジュールカード 62 枚（逐語チェック 186/186）。
```

### 3.2 全仓残留（6 模式；文本文件、`-I` 跳过二进制）

```
$ for p in "33 checks" "11 painter" "126 sourced" "33 public-domain" "11 位" "11 张"; do grep -rInF "$p" . --exclude-dir=.git ...; done
计数：33 checks=2 · 11 painter=7 · 126 sourced=2 · 33 public-domain=1 · 11 位=43 · 11 张=54 → 合计 109 处 / 45 文件
```

**六文件内 = 0**（见 3.1）；以下为其余命中，逐类判定：

**甲 · 历史记录 / 快照（合理；保留，不改）— 40 处 / 13 文件**
- `ops/archaeology-2026-10-16/reports/08-absorb-check.md`(2) · `09-session-condensed.txt`(19) · `02-digest-waves12-21.md`(1) · `09-session-index.md`(1)——本波审计/转录历史（08 即本单任务书，描述修前状态）。
- `ops/OPS-LOG.md`(1) · `ops/session-digest.md`(1) · `ops/GOALS.md`(4)——追加式日志 / 波次史 / 历史条目（A-19/A-27/A-44/D-02）。
- `docs/notes/i18n-audit-ja.md`(3)——10-15 审计快照（引用当时 EN/JA 原文）。
- `docs/skill/draft/SKILL.md`(1) · `docs/skill/skill_ecosystem.md`(1)——设计期草稿/研究稿（描述当时现状）。
- `knowledge/domains/painters/dossiers/_crosscheck.md`(4) · `program/README.md`(1) · `dossiers/_index.md`(1)——当时复核范围 / wave14 计划 / 合并日志（「既有 11 位」）。

**乙 · 不同语境数字（合理；非全局口径）— 37 处 / 18 文件**
- 每位画家图数 / 作品描述 / 卡片序号等：`dossiers/kandinsky.md`(5) · `dossiers/rockwell.md`(2) · `dossiers/{sher_gil,hiroshige,goya}.md`(各1) · `dossiers/_images/manifest.md`(11) · `_images/{mucha,el_greco}/MANIFEST.md`(各2) · `_images/{qi_baishi,kandinsky,hogarth,chardin}/MANIFEST.md`(各1) · `_images/ravi_varma/MANIFEST.md`(2) · `program/roster.md`(2) · `knowledge/cross/transfer_guide.md`(1) · `experiments/anim_test_01/index.html`(1) · `experiments/E1_t1/_extract_prompts.py`(1) · `experiments/E1_t1b/_apply_s81b_cards.py`(1)。
- 例：`kandinsky` 图库 11 张（其本人图数）· `ravi_varma` 作品名「11 位女乐手」· `transfer_guide`「第 11 张卡（像素风）」（15 卡之第 11）· `roster`「中国候选 11 位」（分段计数）· `_images/manifest` 的 wave4 历史基线（「11 位 ×3 张时口径」）。

**丙 · 本地 / 私有层（不入库；合理）— 24 处 / 9 文件**
- `knowledge/domains/painters/_scratch/`：`index_merge3/backup/manifest.md`(11) · `index_merge3/backup/_index.md`(1) · `index_merge2/reconcile.md`(2) · `index_merge2/RECEIPT.md`(1) · `index_merge/RECEIPT.md`(1) · `kandinsky/part3.md`(4) · `sher_gil/check_output.txt`(1) · `p2_goya/pre_edit_backup_goya.md`(1)。
- `_private/INVENTORY_kandinsky.md`(2)——私有层（永不提交）。

**丁 · 同类漂移 · 本批范围外（未动；待主脑）— 8 处 / 5 文件**（另含变体命中）

| 文件 | 命中 | 内容 | 建议 |
|---|---|---|---|
| `docs/ARCHITECTURE.md` | 2 | L34/L55 `11 painters`（另变体：L56 `33 verbatim checks` · L72 `11 modules` · L55 `~250–380 lines`） | 与 i18n 两版同步处理；注意该文件正被本波其它单修改中（写路径独占） |
| `docs/i18n/ja/ARCHITECTURE.md` | 1 | L37 `11 painters`（另变体：L75 `モジュール 11 件`） | 同上 |
| `docs/i18n/zh-CN/ARCHITECTURE.md` | 2 | L37 `11 painters` · L58 `11 位画家` | 同上 |
| `docs/WORKFLOW.md` | 2 | L18 `11 painter dossiers` · `126 sourced quotes` · `11 composable module cards`（另变体：L21 `33 PD works`） | 建议同批或后续批 |
| `docs/i18n/zh-CN/WORKFLOW.md` | 1 | L21 `11 张可组合模块卡`（另变体：`11 份` · `126 条` · L24 `33 件`） | 同上；`docs/i18n/ja/WORKFLOW.md` L21/L24 为纯变体命中（`11 件/11 枚/126 件/33 点`），一并供主脑 |

> 说明：丁类未按本单权限改动（非目标 6 文件；且 `docs/ARCHITECTURE.md` 写路径正被占用）。上表「另变体」为 6 模式之外的同类计数，未计入 8 处。

## §4 备注（待主脑裁定）

1. **62 / 72 注记未插入正文**——理由：本批口径为「纯机械改数」，且六句均为汇总句、无 registry/disk 歧义场景。备选落点（如需）：`README.md` L16 或 `docs/ROADMAP.md` L7 括注「62 in registry / 72 on disk」；zh/ja 是否跟注请一并定（涉及措辞，超出「纯数字替换」）。
2. **人名清单保留**——三语括注仍列原 11 名（未动，属文案）；改后读作「62 份档案（达·芬奇…丢勒）」= 非穷举列举。如主脑需要，可一句式小改（加「等/含」或换代表性名单）——待令。
3. **「~300 lines」未动**——实测 62 档案全文 394–593 行（最小 bada_shanren 394 / 最大 rembrandt 593；不含 4 件元文件）；如该值指 v1 时代口径或「证据段」则无需动——请主脑定是否另修。
4. **丁类（范围外同类漂移）**——清单见 §3.2；建议并入本波收口或另开小单（注意写路径独占）。
5. **其余数字已 grep 核对、未改**：15 风格卡（15/15 同源 ✓）· 18 冲突条目（C-01–C-18 ✓）· N1–N9（9 条 ✓）· 7/7（E1_t1b/c ✓）· 9/9（E2 ✓）· v0.2（SKILL.md ✓）· 三条端到端管线（anim_test_01/02/03_blender ✓）。
6. **工作树**：本批仅动 6 文件（12+/12−）；未 commit；`_extract.py --check` 复跑 186/186 PASS。

## §5 自审四段（compact）

- **A 早产出**：先复核口径（4 源交叉）→ 逐文件改（18 数）→ 全仓复核 → 本报告。
- **B 反驳**：①「残留=0」——六文件内成立（含变体集全扫空）；全仓非 0（109 处），已逐类归因、丁类 8 处不遮掩。②「数字对不对」——`_index` / `_corpus` / `_images` / `_extract --check` 四源一致。③「有没有多改」——`git diff --stat` = 12+/12−，仅 6 文件、仅 18 数。
- **C 机械验证**：`_extract.py --check` = `checks=186 ok=186 fail=0`；变体集 grep 空（EXIT=1）；残留计数 109/45 与逐文件明细对账一致（2/7/2/1/43/54）。
- **D 小结**：批修完成、未 commit；残留分类完毕；「62/72 注记」「人名清单」「~300」三项备选改动与丁类清单待主脑。
