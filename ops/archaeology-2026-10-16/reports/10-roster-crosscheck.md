# 10 · Roster Crosscheck — 62 位画家名册交叉核对（重跑）

> 写手：RosterCrosscheck2（Wave1-R2 重派；原单 RosterCrosscheck 死于 503 波）｜日期：2026-10-16｜状态：**完成（只读，零改动）**
> 数据基准：磁盘实测（glob / grep / read，2026-10-16 10:4x JST）；GOALS 现行版（含本波 A-107 收口）
> 交付：本报告（`local://reports/10-roster-crosscheck.md`，供主脑收集；另落本目录 .json 副本）

**一句话结论**：73 个非下划线档案全部在位、全部有 Lane A 行覆盖 → **三表无异常项**（① 0 · ② 0 · ③ 仅 A-30 open）；模块卡 **62 张** ↔ `_extract.py --check` **186/186**（= 62×3）对账成立；抽验 3 份档案 × 5 锚点 **15/15 全命中**。

---

## §1 实际档案清单（`ls knowledge/domains/painters/dossiers/*.md`，排除下划线件）

- 目录 .md 共 76 项；排除下划线件（`_index.md` / `_review.md` / `_crosscheck.md`）→ **73 件**。
- **73 = 72 位画家档案 + `expansion.md`（扩展候选分析，A-09）**。
- 口径拆分：72 位 = **62 位（「62 位名册」wave1–20，已并入三索引 + 模块卡）** + **10 位 wave21（在盘、已收口；索引口径「在产注明」，模块卡待扩）**。
- 全清单：
  - wave1–2（11）：da_vinci / michelangelo / van_gogh / monet / picasso / cezanne / matisse / hokusai / caravaggio / vermeer / durer
  - wave12–13（9）：turner / rembrandt / klimt / goya / seurat / hopper / bada_shanren / qi_baishi / ito_jakuchu
  - wave15（8）：mucha / munch / kandinsky / velazquez / bosch / huang_gongwang / kahlo / behzad
  - wave17（7）：friedrich / repin / ravi_varma / degas / gauguin / van_eyck / kngwarreye
  - wave18（7）：hiroshige / sargent / piero_della_francesca / artemisia_gentileschi / namatjira / el_salahi / wu_guanzhong
  - wave19（10）：fan_kuan / sesshu / constable / poussin / bruegel / el_greco / holbein / aivazovsky / okeeffe / rivera
  - wave20（10）：zhao_mengfu / ni_zan / qiu_ying / ogata_korin / blake / chardin / manet / sorolla / zorn / sultan_mohammed
  - wave21（10）：xu_beihong / li_keran / sher_gil / tarsila / chen_hongshou / xu_wei / hogarth / mir_sayyid_ali / de_chirico / rockwell
  - 分析件（1）：expansion

## §2 GOALS Lane A 解析（状态 / 产出路径 / 归属）

- Lane A 表共 **113 行**（A-01..A-109 = 109 行 + E-01..E-04 = 4 行）。
- 状态分布（现行）：**done 112**（含 A-12 `done(v0.1)`）· **open 1**（A-30）· running 0 · blocked 0。
- 产出路径映射：72 位画家 → 72 个 `dossiers/<id>.md` 行系（建档 + 加固/重派行，覆盖全部 72 个画家文件）；非档案行：`_corpus/`（A-10）· `_review.md`（A-11）· `experiments/design.md`（A-12）· `motion-graphics/sources/`（A-13）· `_crosscheck.md`（A-14）· `modules/`（A-19/50/76/108）· `dossiers/`（A-51/75/107/109）· `program/roster.md`（A-29）· `experiments/E1_t1|E1_t1b|E1_t1c|E2_t1/`（E-01..04）。
- 归属：Artist*（wave12–21 主档）· Bio*（wave14 加固 ×11）· Hard*（wave16p2 加固 ×9）· IndexMerge1/2/3 · ModuleLibrary/ModuleCards20/42/62 · CrossLinkSync · 主脑（A-12/13/30）等。
- 备注：**A-107 本波内由 running → done**（主脑 10:19 收口：verify 257/0 复跑 + 62 行/1613 条/公开 618+私有 676 + commit `cea77cb`）。

## §3 三表（GOALS ⇄ 档案交叉核对）

### ① GOALS done 但文件缺失 / 路径不符 —— **0 项（无异常）**

| # | 检查 | 结果 |
|---|---|---|
| 1 | done 行 × dossier 路径（72 位） | **72/72 文件在盘** ✓ |
| 2 | done 行 × 非档案路径（design.md / sources/ / roster.md / conflicts.md / E1×3+E2 / _corpus/ / _review.md / _crosscheck.md / modules/ / dossiers/） | **全部在盘** ✓ |
| — | **异常项** | **无** |

### ② 文件存在但无 GOALS 行 —— **0 项（无异常）**

| # | 检查 | 结果 |
|---|---|---|
| 1 | 73 件档案逐一回查 GOALS 行 | **73/73 有行** ✓（含 expansion → A-09；wave21 ×10 → A-97..A-106） |
| — | **异常项** | **无** |

口径注（供主脑）：与「62 位名册」的 10 件差集 = **wave21 十位**（有行、在盘；尚未并入三索引与模块卡，属既定「在产」设计，下轮 index merge4 / 模块卡 62→72 处理）。

### ③ 仍 open / running —— **Lane A 1 项**

| ID | 状态 | 一句话 |
|---|---|---|
| A-30 | open | 学习产物：每大师「学习路径卡」+ 总学习路线（Owner 已批；roster 后启动；归属主脑） |

- Lane A 无 running / blocked。跨 lane 补充：S-06（Lane S，open）。全表口径：**done 146 / open 2（A-30、S-06）/ running 0 / blocked 0（148 行）**。
- 时点注：A-107 在上一轮快照中为 running，本波已收口为 done（见 §2 备注）。

## §4 抽验：3 份档案 × 5 锚点（grep 实测）

选样：da_vinci（wave1）· goya（wave13）· rockwell（wave21）。

| 档案 | `## 4. 控制参数` | `### 8.1` | `### 8.2` | `## 11.` | `## 12.` | 结论 |
|---|---|---|---|---|---|---|
| da_vinci.md | ✓ L63 | ✓ L128 | ✓ L158 | ✓ L210 | ✓ L327 | **5/5** |
| goya.md | ✓ L93 | ✓ L202 | ✓ L233 | ✓ L305 | ✓ L386 | **5/5** |
| rockwell.md | ✓ L96 | ✓ L199 | ✓ L241 | ✓ L316 | ✓ L383 | **5/5** |

**汇总：3/3 份、15/15 锚点全部命中**（结构同构成立）。

## §5 计数对账（验收项）

| 项 | 数值 | 依据（实测） |
|---|---|---|
| 档案数（dossiers/*.md − 下划线） | **73** = 72 画家 + 1 分析件（其中 62 在册 + 10 wave21 在产） | glob 实测，见 §1 |
| 模块卡数（modules/*.md − README） | **62** | glob 实测 |
| GOALS done 数 | **Lane A 112/113**（A-30 open）· **全表 146/148**（A-30、S-06 open） | grep 实测 |
| `_extract.py --check` | **checks=186 ok=186 fail=0**（= 62 卡 × 3 段） | 本波实跑，见 §6 |

对账链：62 卡 × 3 = **186** = `--check` 输出 ✓；档案 73 = 62 + 10 + 1 ✓（三口径自洽，无矛盾项）。

## §6 `_extract.py --check` 运行记录与输出

- 运行注记：本侦察位为**只读沙箱**（无 bash/Python 执行面，与同波各侦察工同例）→ `--check` 取**本波实跑**（最新冻结态）：
  - 实跑 A：`cd D:/Project/Designers_Brain && python knowledge/domains/painters/modules/_extract.py --check 2>&1` — EndgameReconcile2，2026-10-16 10:1x JST → 尾行 `checks=186 ok=186 fail=0`，**EXIT=0**（见 `03-endgame-reconcile.md` §3.2）。
  - 实跑 B：主脑复核（同波，校验器修复后全绿批次）→ `extract --check: 186/186`。
- 完整输出（62 卡逐张 · 63 行；留档 `mc62/check_final_output.txt`，与实跑尾行逐字一致）：

```
[da_vinci] §8.1 ok (1441c) · §8.2 ok (522c) · §4 ok (602c)
[michelangelo] §8.1 ok (1257c) · §8.2 ok (536c) · §4 ok (588c)
[van_gogh] §8.1 ok (1106c) · §8.2 ok (609c) · §4 ok (695c)
[monet] §8.1 ok (935c) · §8.2 ok (584c) · §4 ok (655c)
[picasso] §8.1 ok (1104c) · §8.2 ok (561c) · §4 ok (702c)
[cezanne] §8.1 ok (1313c) · §8.2 ok (628c) · §4 ok (659c)
[matisse] §8.1 ok (1025c) · §8.2 ok (1066c) · §4 ok (1034c)
[hokusai] §8.1 ok (1228c) · §8.2 ok (457c) · §4 ok (755c)
[caravaggio] §8.1 ok (1448c) · §8.2 ok (694c) · §4 ok (1268c)
[vermeer] §8.1 ok (1512c) · §8.2 ok (931c) · §4 ok (1163c)
[durer] §8.1 ok (1544c) · §8.2 ok (692c) · §4 ok (880c)
[turner] §8.1 ok (1370c) · §8.2 ok (852c) · §4 ok (1037c)
[rembrandt] §8.1 ok (1511c) · §8.2 ok (894c) · §4 ok (1686c)
[klimt] §8.1 ok (1465c) · §8.2 ok (1100c) · §4 ok (1568c)
[goya] §8.1 ok (1551c) · §8.2 ok (980c) · §4 ok (1080c)
[seurat] §8.1 ok (1453c) · §8.2 ok (721c) · §4 ok (768c)
[hopper] §8.1 ok (1481c) · §8.2 ok (834c) · §4 ok (1228c)
[bada_shanren] §8.1 ok (1591c) · §8.2 ok (510c) · §4 ok (624c)
[qi_baishi] §8.1 ok (1289c) · §8.2 ok (801c) · §4 ok (909c)
[ito_jakuchu] §8.1 ok (1591c) · §8.2 ok (678c) · §4 ok (839c)
[mucha] §8.1 ok (1423c) · §8.2 ok (741c) · §4 ok (1006c)
[munch] §8.1 ok (1659c) · §8.2 ok (1124c) · §4 ok (1092c)
[kandinsky] §8.1 ok (1484c) · §8.2 ok (977c) · §4 ok (1034c)
[velazquez] §8.1 ok (1675c) · §8.2 ok (786c) · §4 ok (1096c)
[bosch] §8.1 ok (1545c) · §8.2 ok (890c) · §4 ok (894c)
[kahlo] §8.1 ok (1653c) · §8.2 ok (799c) · §4 ok (1316c)
[behzad] §8.1 ok (1780c) · §8.2 ok (944c) · §4 ok (916c)
[huang_gongwang] §8.1 ok (1949c) · §8.2 ok (645c) · §4 ok (686c)
[friedrich] §8.1 ok (1568c) · §8.2 ok (1164c) · §4 ok (969c)
[repin] §8.1 ok (1730c) · §8.2 ok (748c) · §4 ok (996c)
[ravi_varma] §8.1 ok (1347c) · §8.2 ok (734c) · §4 ok (879c)
[degas] §8.1 ok (2315c) · §8.2 ok (1443c) · §4 ok (1201c)
[gauguin] §8.1 ok (1766c) · §8.2 ok (995c) · §4 ok (1212c)
[van_eyck] §8.1 ok (1915c) · §8.2 ok (1313c) · §4 ok (1176c)
[kngwarreye] §8.1 ok (1838c) · §8.2 ok (812c) · §4 ok (1212c)
[hiroshige] §8.1 ok (1637c) · §8.2 ok (1155c) · §4 ok (1117c)
[sargent] §8.1 ok (2171c) · §8.2 ok (1025c) · §4 ok (1083c)
[piero_della_francesca] §8.1 ok (1978c) · §8.2 ok (1358c) · §4 ok (1236c)
[artemisia_gentileschi] §8.1 ok (1992c) · §8.2 ok (1096c) · §4 ok (1178c)
[namatjira] §8.1 ok (2218c) · §8.2 ok (880c) · §4 ok (1081c)
[el_salahi] §8.1 ok (1811c) · §8.2 ok (856c) · §4 ok (1352c)
[wu_guanzhong] §8.1 ok (1892c) · §8.2 ok (825c) · §4 ok (1243c)
[fan_kuan] §8.1 ok (2081c) · §8.2 ok (655c) · §4 ok (731c)
[sesshu] §8.1 ok (1585c) · §8.2 ok (1033c) · §4 ok (955c)
[constable] §8.1 ok (1951c) · §8.2 ok (1310c) · §4 ok (1016c)
[poussin] §8.1 ok (1706c) · §8.2 ok (1230c) · §4 ok (917c)
[bruegel] §8.1 ok (1517c) · §8.2 ok (1065c) · §4 ok (1008c)
[el_greco] §8.1 ok (2096c) · §8.2 ok (1188c) · §4 ok (1018c)
[holbein] §8.1 ok (2061c) · §8.2 ok (925c) · §4 ok (954c)
[aivazovsky] §8.1 ok (1635c) · §8.2 ok (1236c) · §4 ok (1174c)
[okeeffe] §8.1 ok (1985c) · §8.2 ok (1061c) · §4 ok (1065c)
[rivera] §8.1 ok (2048c) · §8.2 ok (1120c) · §4 ok (1154c)
[zhao_mengfu] §8.1 ok (1723c) · §8.2 ok (748c) · §4 ok (767c)
[ni_zan] §8.1 ok (1787c) · §8.2 ok (541c) · §4 ok (659c)
[qiu_ying] §8.1 ok (2052c) · §8.2 ok (754c) · §4 ok (1185c)
[ogata_korin] §8.1 ok (2089c) · §8.2 ok (798c) · §4 ok (785c)
[blake] §8.1 ok (2445c) · §8.2 ok (940c) · §4 ok (1217c)
[chardin] §8.1 ok (1746c) · §8.2 ok (1149c) · §4 ok (1113c)
[manet] §8.1 ok (1997c) · §8.2 ok (1072c) · §4 ok (1025c)
[sorolla] §8.1 ok (1290c) · §8.2 ok (678c) · §4 ok (1044c)
[zorn] §8.1 ok (2668c) · §8.2 ok (1090c) · §4 ok (1118c)
[sultan_mohammed] §8.1 ok (1513c) · §8.2 ok (1001c) · §4 ok (972c)
checks=186 ok=186 fail=0   # 62 卡 × §8.1/§8.2/§4 逐字比对
```

## §7 方法与留痕（复核用）

- 工具/命令：`ls/glob dossiers|modules` · `grep GOALS 全表（状态/路径）` · `grep -n 5 锚点 ×3 档案` · `_extract.py --check`（实跑记录见 §6）——**全程只读**。
- Non-goals 遵守：未改 GOALS / 未改任何档案（零写入项目文件）。
- 报告落点：`local://reports/10-roster-crosscheck.md`（本文件）；另落本目录同名 `.json` 副本（供直读兜底）。
