# 13 · CountsFix2 — ARCHITECTURE/WORKFLOW 同类漂移补修 + README 三语软措辞

> 写手：CountsFix2（收口批补派单）｜日期：2026-10-16｜状态：**完成（9 文件 / 24 行 / 33 数；未 commit；本报告为本单唯一新增产物）**
> 范围：`docs/ARCHITECTURE.md` 三版 · `docs/WORKFLOW.md` 三版 · `README.md` 三语（软措辞）——**纯机械改数 + 软措辞同步**；未动其它；未 commit；未触碰 PROTOCOLS。
> 来源：`reports/11-counts-refresh.md` §3.2 丁（同类漂移·范围外 8 处 + 另变体）· §4 备注 3（「~300 lines」）；口径复核 = 2026-10-16 盘上实（`_index.md` · `_corpus/INDEX.md` · `_images/manifest.md` · `_extract.py --check` 实跑）。

**一句话结论**：丁类 8 处 + 全部另变体 + 同族软措辞，共 **24 行 / 33 数（9 文件）** 按现口径替换完毕（**62 / 1613 / 618 / 186 / ~300–600**）；改后 9 文件「变体集全扫」= **0 残留**；未 commit。

---

## §1 口径核验（2026-10-16 盘上实）

| 计数 | 旧值 | **采用值** | 核验证据（实跑） |
|---|---|---|---|
| 画家档案 | 11 | **62** | `dossiers/_index.md`：「全表 62 行重算 → 合计 62 位」；磁盘实计 72 = 62 + wave21 十位（未纳入在产） |
| 模块卡 | 11 | **62** | `modules/` 实计 62 卡（+README + `_extract.py`） |
| 逐字校验 | 33 | **186** | 复跑 `python knowledge/domains/painters/modules/_extract.py --check` → `checks=186 ok=186 fail=0   # 62 卡 × §8.1/§8.2/§4 逐字比对` |
| 语料引文 | 126 | **1613** | `_corpus/INDEX.md`：「合计 62 文件 1613 条」 |
| 公开图 | 33 | **618** | `_images/manifest.md`：「现共 62 位画家 / 公开 618 张」（私有层例外 676 张，分开记） |
| 档案行数 | ~250–380 / ~300 | **~300–600** | 72 文件实计（不含 4 件元文件 `_index/_crosscheck/_review/expansion`）：最小 bada_shanren 394 / 最大 rembrandt 593 |

## §2 逐处 before → after（9 文件 / 24 行）

### ① `docs/ARCHITECTURE.md` — 5 行 / 6 数

| 行 | before | after |
|---|---|---|
| L34 | `— domain #1: 11 painters` | `— domain #1: 62 painters` |
| L52 | ` literature)  ~300 lines each)` | ` literature)  ~300–600 lines each)` |
| L55 | `11 painters, each ~250–380 lines.` | `62 painters, each ~300–600 lines.` |
| L56 | `33 verbatim checks` | `186 verbatim checks` |
| L72 | `(11 modules)` | `(62 modules)` |

### ② `docs/i18n/zh-CN/ARCHITECTURE.md` — 5 行 / 6 数

| 行 | before | after |
|---|---|---|
| L37 | `— domain #1: 11 painters` | `— domain #1: 62 painters` |
| L55 | ` literature)  ~300 lines each)` | ` literature)  ~300–600 lines each)` |
| L58 | `11 位画家，每份约 250–380 行。` | `62 位画家，每份约 300–600 行。` |
| L59 | `33 项逐字校验` | `186 项逐字校验` |
| L75 | `（11 个模块）` | `（62 个模块）` |

### ③ `docs/i18n/ja/ARCHITECTURE.md` — 5 行 / 6 数

| 行 | before | after |
|---|---|---|
| L37 | `— domain #1: 11 painters` | `— domain #1: 62 painters` |
| L55 | ` literature)  ~300 lines each)` | ` literature)  ~300–600 lines each)` |
| L58 | `画家 11 名、各約 250〜380 行。` | `画家 62 名、各約 300〜600 行。` |
| L59 | `逐語チェック 33 件` | `逐語チェック 186 件` |
| L75 | `（モジュール 11 件）` | `（モジュール 62 件）` |

### ④ `docs/WORKFLOW.md` — 2 行 / 4 数

| 行 | before | after |
|---|---|---|
| L18 | `11 painter dossiers + quote corpus (126 sourced quotes) + image library + 11 composable module cards` | `62 painter dossiers + quote corpus (1613 sourced quotes) + image library + 62 composable module cards` |
| L21 | `(33 PD works)` | `(618 PD works)` |

### ⑤ `docs/i18n/zh-CN/WORKFLOW.md` — 2 行 / 4 数

| 行 | before | after |
|---|---|---|
| L21 | `11 份画家档案 + 引文语料库（126 条带来源引文）+ 图像库 + 11 张可组合模块卡` | `62 份画家档案 + 引文语料库（1613 条带来源引文）+ 图像库 + 62 张可组合模块卡` |
| L24 | `（33 件公有领域作品）` | `（618 件公有领域作品）` |

### ⑥ `docs/i18n/ja/WORKFLOW.md` — 2 行 / 4 数

| 行 | before | after |
|---|---|---|
| L21 | `画家ドシエ（資料ファイル）11 件 + 引用コーパス（出典付き引用 126 件）+ 画像ライブラリ + 合成可能なモジュールカード 11 枚` | `画家ドシエ（資料ファイル）62 件 + 引用コーパス（出典付き引用 1613 件）+ 画像ライブラリ + 合成可能なモジュールカード 62 枚` |
| L24 | `（パブリックドメイン作品 33 点）` | `（パブリックドメイン作品 618 点）` |

### ⑦–⑨ README 三语（软措辞）— 各 1 行 / 1 数

| 文件 | 行 | before | after |
|---|---|---|---|
| `README.md` | L16 | `~300 lines of evidence each` | `~300–600 lines of evidence each` |
| `README.zh-CN.md` | L19 | `每份约 300 行证据` | `每份约 300–600 行证据` |
| `README.ja.md` | L19 | `各約 300 行のエビデンス` | `各約 300〜600 行のエビデンス` |

> 对照丁表：8 处基础命中（ARCH EN 2 · ja 1 · zh 2；WORKFLOW EN 2 · zh 1）全含；「另变体」（`33 verbatim checks` · `11 modules` · `モジュール 11 件` · `33 PD works` · `11 份` · `126 条` · `33 件` · `11 件` · `11 枚` · `126 件` · `33 点` · `~250–380`）全部随改；ja/WORKFLOW 的纯变体命中一并同步。另：3 版 ARCH 图内 `~300 lines each` 为超出 8 处与丁表变体清单的「同句族」软措辞（§4-3 的「~300 lines」），一并同步为 `~300–600`——超出字面清单的部分集中在此，如不需可单点回退。

## §3 复核输出（原样）

### 3.1 变体集 grep（9 文件；期望空）

```
$ grep -nE "11 painter|11 modules|11 composable|33 verbatim|33 PD|126 sourced|~250|~300 lines|11 位|11 个模块|11 份|11 张|11 件|11 枚|画家 11|モジュール 11|33 项|33 件|33 点|33 校验|126 条|126 件|250–380|250〜380|约 300 行|約 300 行" \
    README.md README.zh-CN.md README.ja.md \
    docs/ARCHITECTURE.md docs/WORKFLOW.md \
    docs/i18n/zh-CN/ARCHITECTURE.md docs/i18n/zh-CN/WORKFLOW.md \
    docs/i18n/ja/ARCHITECTURE.md docs/i18n/ja/WORKFLOW.md
（无输出；EXIT=1 —— 9 文件残留 = 0 ✓）
```

补充扫描（独立 token，边界匹配）：9 文件中 `(?<![0-9])(11|33|126|250)(?![0-9])` = **0 处**（`C1–C10` / `768×1152` 等邻接数字不误报）。

### 3.2 `git diff --stat`（我名下 9 文件；含本波此前未提交改动）

```
 README.ja.md                    |  6 +++---
 README.md                       |  6 +++---
 README.zh-CN.md                 |  6 +++---
 docs/ARCHITECTURE.md            | 19 ++++++++++++++-----
 docs/WORKFLOW.md                |  4 ++--
 docs/i18n/ja/ARCHITECTURE.md    | 10 +++++-----
 docs/i18n/ja/WORKFLOW.md        |  4 ++--
 docs/i18n/zh-CN/ARCHITECTURE.md | 10 +++++-----
 docs/i18n/zh-CN/WORKFLOW.md     |  4 ++--
 9 files changed, 39 insertions(+), 30 deletions(-)
```

> 说明：stat 含此前未提交改动（CountsFix 的 README 计数 · DocsAbsorb 的 ARCHITECTURE §3.4 +9 行）。**本单净增量 = 24 行（24−/24+）**——对照开工前整文件备份（本机 `/tmp`，非入库）逐文件 diff 复核：README 三语各 1 行 · ARCH 三版各 5 行 · WORKFLOW 三版各 2 行；全部为行内替换（文件行数不变），除这 24 行外无其它字节改动；字节增量对账：合计 +45 B——README×3 各 +6 · ARCH 三版各 +7 · WORKFLOW 三版各 +2，逐项与替换文本长度吻合。

### 3.3 口径复跑（原始输出）

```
$ python knowledge/domains/painters/modules/_extract.py --check
...
checks=186 ok=186 fail=0   # 62 卡 × §8.1/§8.2/§4 逐字比对
```

### 3.4 路径级核对（本单写路径）

```
$ git status --porcelain -- <9 文件 + 本报告>
 M README.ja.md
 M README.md
 M README.zh-CN.md
 M docs/ARCHITECTURE.md
 M docs/WORKFLOW.md
 M docs/i18n/ja/ARCHITECTURE.md
 M docs/i18n/ja/WORKFLOW.md
 M docs/i18n/zh-CN/ARCHITECTURE.md
 M docs/i18n/zh-CN/WORKFLOW.md
?? ops/archaeology-2026-10-16/reports/13-counts-fix2.md
```

## §4 备注（供主脑）

1. **「62 / 72」注记**：沿用 CountsFix 裁定，未插入正文（62 = 名册口径；磁盘 72 含 wave21 十位）。
2. **行数口径**：`~300–600` 按实测 394–593 上取整（§1 表）；9 处行数措辞全部同步（README×3 · ARCH 正文×3 · ARCH 图内×3）。
3. **范围外同类残留（未动；供主脑）**：
   - `docs/ROADMAP.md` 三语：「~300 lines」/「每份约 300 行」/「各約 300 行」（CountsFix 遗留、非本单 Target；如需一句式即可补）。
   - 更远同族（扩扫所见，疑属历史/设计期类）：`knowledge/cross/conflicts.md`（「11 份」×7）· `docs/skill/skill_spec.md`（「11 份」×2）。
4. **写路径**：本单只动 9 文件 + 本报告；PROTOCOLS 未触碰；未 commit。

## §5 自审四段（compact）

- **A 早产出**：先读 11 报告 §3.2 丁 + §4 → 四源口径复核（§1）→ 24 行机械改 → 变体集全扫 → 本报告。
- **B 反驳**：①「残留=0」——9 文件内成立（29 变体全扫空 + 独立 token 扫描 0）；全仓非 0，属历史/语境/私有类（11 报告 §3.2 甲乙丙）＋ ROADMAP 软措辞（§4-3，未动）。②「数字对不对」——`_index` / `_corpus` / `_images` / `_extract --check` 四源一致。③「有没有多改」——对照开工前备份：仅 9 文件 24 行。
- **C 机械验证**：变体集 grep EXIT=1；`--check` = 186/186；本单 diff = 24−/24+。
- **D 小结**：丁类收口完成、未 commit；ROADMAP 软措辞与更远同族 2 文件留待主脑。
