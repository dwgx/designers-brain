# E1_t1c · michelangelo §8.1b v2 从句级改写 · 重跑与三版对照（T1「暴风雨中的海边灯塔」）

> **E-03**（wave8）· 2026-10-15 · 直连网关 `/v1/images/generations` · 模型 `grok-imagine-image-2.0`
> 1 格 × 3 张 = **3 张**（§8.1b v2）；三版对照：E1 偏置版（E1_t1）/ E1b 部分解除（E1_t1b）/ E1c v2（本目录）。
> 配方：`prompt = 主题句 + " " + 模块卡 §8.1b v2 正向段`（逐行解包为单行）；负向段未随请求发送（同 E1_t1 / E1_t1b）。
> 上游：`E1_t1b/RESULTS_t1b.md` §4.2（负向发现：部分解除——风格语言与人体绑定）；本目录 =「从句级改写（v2）→ 重跑 → 三版对照」收口产物。

## 1. 背景与目标

- E-02 结论（E1_t1b §4.2）：michelangelo 仅删题材名词（§8.1b v1）后**部分解除**——灯塔回中心、可读性大幅提升，但「巨型肌肉形体」仍以漩涡状环绕出现（云体巨人 / 盘绕巨体）；**题材偏置的根源不只在题材名词，还在与人体绑定的视觉语言本身**（serpentine torsion / 雕塑式体积 / 仰视透视 / many interlocking forms）。
- 本实验（E-03）动作：
  1. **从句级改写 §8.1b（v2）**——把人体绑定从句改写成可迁移到无机物的等价视觉语言（① 体积块面扭转→岩石/浪体（+云）块体的扭转；② 仰视透视→低角度构图；③ 肌肉起伏→表面雕塑化起伏），保留可判定阈值；v1 原样保留可审计（卡内 + 快照 + 备份）。
  2. **重跑 3 张**（T1 主题）→ `cells/e1_michelangelo_v2/`（req/resp 留档）。
  3. **三版对照** `compare_michelangelo_v2.png` + 结论（解除 / 仍绑定 / 新问题）。
- 隔离变量：E1c 与 E1b 的唯一差异 = §8.1b 文本（v1→v2）；主题句、模型、尺寸、配方、重试口径完全一致。

## 2. §8.1b v2 从句级改写记录（逐处前后对照）

> v1 = E-02 原版（单行文本 sha256 `3326164fb5666fb9…`，整节逐字存档 `s81b_v1_snapshot.md`）；
> v2 = 本版（单行文本 sha256 `214dd6735d18f835…`，写入卡内「正向段 v2」）。
> 原则：人体绑定从句 → 可迁移到无机物的等价语言；**可判定阈值保留**（S-curve 反扭 / 硬边阴影 / 漩涡构图 / 限色 / 尺度与透视）。
> 卡内位置：`knowledge/domains/painters/modules/michelangelo.md` §8.1b；审计：`s81b_v2_derivation.json` + `_backup_card_before_v2/michelangelo.md`。

### 2.1 逐处对照表（5 处改写 + 2 处保留）

| # | v1 从句 | v2 从句 | 改写类型 | 保留的可判定阈值 |
|---|---------|---------|----------|------------------|
| 1 | `colossal, heroic forms with clearly defined volumes` | `colossal masses with clearly defined volumes` | 形体词清扫（heroic forms→masses） | colossal（尺度）/ clearly defined volumes（体积可读性） |
| 2 | `forms locked in serpentine torsion — counter-rotations forming an S-curve` | `rock, wave and cloud masses locked in serpentine torsion — counter-rotating blocks forming an S-curve` | **体积块面扭转→岩石/浪体（+云）块体的扭转** | serpentine torsion / S-curve（几何可判定，§8.2-2 扭转检测的视觉源） |
| 3 | `forms designed to be seen from below, strong foreshortening, monumental scale` | `low-angle composition, strong foreshortening, monumental scale` | **仰视透视→低角度构图** | strong foreshortening / monumental scale（透视与尺度可读性） |
| 4 | `sculptural modelling — forms look chiselled out of the surface, hard-edged cast shadows, relief-like light and shadow` | `sculptural modelling — surfaces rise and fall as if chiselled from solid mass, hard-edged cast shadows, relief-like light and shadow` | **肌肉起伏→表面雕塑化起伏** | hard-edged cast shadows / relief-like light and shadow（§8.2-3 硬边阴影） |
| 5 | `dense swirling composition of many interlocking forms rotating around a calm central axis` | `dense swirling composition of many interlocking masses rotating around a calm central axis` | 形体词清扫（interlocking forms→masses） | dense / swirling / calm central axis（§8.2-4 构图密度） |
| 6 | `limited fresco palette of earthy ochre, muted green, pale violet and sky blue, matte plaster surface` | （不变） | 保留 | §8.2-6 色彩（饱和 ≤0.5、强调色 ≤2、四族限色） |
| 7 | `an atmosphere of awe and terribilità` | （不变） | 保留 | 氛围词（无形体绑定） |

补充说明：

- #2 中「云体」一并纳入扭转块体——E-02 证据里「云体巨人」是主要人体化载体之一（img_01/02）；「counter-rotations→counter-rotating blocks」为块面级表述。
- #3 视角升格为**构图级属性**，不再暗示「供仰视的（人物）形体」。
- #4 塑造对象从「forms（会读成肌体）」改为「surface 的起伏」；`chiselled` 保留「凿出」的雕刻感。
- v2 块体名词（岩石/浪体/云体）对应 T1 场景无机块体；换场景时按同类替换（卡内 note 已注明）。
- 未加入显式反人物短语（保持「仅从句级改写」的实验纯度——若重跑仍绑定，记为新问题/后续手段）。

### 2.2 改写后全文（v2，单行）

```text
High Renaissance fresco in the manner of Michelangelo Buonarroti: colossal masses with clearly defined volumes; rock, wave and cloud masses locked in serpentine torsion — counter-rotating blocks forming an S-curve; low-angle composition, strong foreshortening, monumental scale; sculptural modelling — surfaces rise and fall as if chiselled from solid mass, hard-edged cast shadows, relief-like light and shadow; dense swirling composition of many interlocking masses rotating around a calm central axis; limited fresco palette of earthy ochre, muted green, pale violet and sky blue, matte plaster surface; an atmosphere of awe and terribilità
```

### 2.3 v1 原样保留（可审计）三处 + 重跑结论回填

1. 卡内「### v1 审计存档」（逐字块，含折行原样）；
2. `s81b_v1_snapshot.md`（E-02 原节整节逐字，sha256 `8b71fcab4bab8f49…`）；
3. `_backup_card_before_v2/michelangelo.md`（改写前整卡备份）。
4. 重跑结论回填（post-run 注释，非 `_apply_s81b_v2.py` 产物）：卡内 note 追加一行「重跑验证…」（v2 文本未变，sha 仍 `214dd673…`）；记录于 `s81b_v2_derivation.json` → `post_run`。

## 3. 重跑结果（1 格 × 3 张）

| # | 格 | 模块 | §8.1b v2 sha 前 8 | 尺寸（请求 → 实回） | 耗时 | sha256 前 8 位（img_01 / 02 / 03） |
|---|----|------|-------------------|--------------------|------|-----------------------------------|
| 1 | e1_michelangelo_v2 | 米开朗基罗 | `214dd673` | 1024x1536 → 768×1152×3 | 58.5s（均 ≈19.5s/张） | `dd79ba3d` / `fd9b401d` / `4cb48350` |

- **3/3 一次成功**（0 重试、0 失败；墙钟 61s）。耗时口径同 E1_t1 / E1_t1b（请求→落盘合计）；明细见 `run_log.jsonl` / `stats_t1c.json`。
- 逐张目检（含 2×2 放大 `_inspect/`）：
  - **img_01**：灯塔立于凿刻感礁岩尖峰；左上方云体成强螺旋涡、右下浪面出清晰螺旋漩涡；岩面硬边凿痕、低角度构图、赭/紫灰/青蓝限色。**无人物**。
  - **img_02**：灯塔居中偏上；紫灰风暴云成卷、岩脊呈对角 S 形，浪花留白；**无人物**。
  - **img_03**：高塔立于大块堆叠礁岩；云绕塔身成涡、左侧大浪卷起螺旋；**无人物**。

## 4. 三版对照与结论

> 对照图：`compare_michelangelo_v2.png`（3 行 × 3 列：上 E1 偏置 / 中 E1b v1 部分 / 下 E1c v2）；单格横排：`sheet_e1_michelangelo_v2.png`。

| # | 版本 | 状态（E-02 口径） | 输出描述 | 判定 |
|---|------|-------------------|----------|------|
| 1 | §8.1 偏置版（E1_t1） | 场景被替换（题材偏置） | 裸体肌肉人物以漩涡状环绕画面，灯塔缩为中央小元素（sha `98b89e61` / `8e4f902e` / `ed1c573b`） | 偏置（基线） |
| 2 | §8.1b v1（E1_t1b） | 部分解除 | 灯塔回中心；但巨型肌肉形体仍环绕出现（云体巨人 / 盘绕巨体）（sha `10447f51` / `697f5921` / `e39ca250`） | 部分解除 |
| 3 | §8.1b v2（E1_t1c） | —（本轮） | 灯塔场景完整；扭转/雕塑/漩涡/限色落在云、浪、岩上；**无人体母题**（sha `dd79ba3d` / `fd9b401d` / `4cb48350`） | **解除** |

### 4.1 结论：解除（3/3）

- 3 张均**无人体/类人体母题**（含云/浪/岩区域的 2×2 放大细看，未发现人形残留）；T1 场景（灯塔＋礁岩＋风暴）完整；风格语言落点清晰：云涡 / 浪旋 / 岩体凿刻 + 低角度构图 + 漩涡绕中央轴 + 限色（赭/暗绿/紫/青蓝）。
- 与 E1b 对比：v1 的「云体巨人 / 盘绕巨体」消失；与 E1 对比：裸体人物漩涡消失。**仅从句级改写即完成解除**（未用显式反人物短语、未调参）。
- 收口：E-02 遗留的 michelangelo「部分解除」经 v2 复核 → **解除**；至此 E1_t1b 7 格 + E1_t1c 1 格 = **7/7 全部解除或基本解除**（durer 为基本解除，其余 6 格解除）。

### 4.2 新问题 / 代价（如实记录）

1. **扭转落点再分配**：扭转主要落在云 / 浪（云涡、浪旋、S 形脊线），岩体更多呈「凿刻 / 堆叠」而非明显「扭动」——风格语言承担者发生转移（接受；如需岩石也呈现明显扭动，属后续调参项，本轮未二次调参）。
2. **模块指纹变化（去题材的必然代价）**：去人后「人体即舞台」指纹不再出现；风格辨识度依赖漩涡构图 + 雕塑化凿刻 + terribilità 氛围，画面更接近「雕塑化的暴风海景」。对「像不像米开朗基罗」的判定标准需按无机物场景重新校准（记录在案，不判缺陷）。
3. **单评审目检口径**：本判定为单评审（agent 目检，含放大）；无第二评审 / 无人评六维打分（同 E1_t1b §5 缺口）。
4. 无其它退化：无伪影、无风格崩坏、无文字 / 签名残留。

## 5. 缺口与偏差

1. **通道口径与 E1_t1 / E1_t1b 一致**：负向段未发送；尺寸请求 1024x1536、实回 768×1152；模型用裸名 `grok-imagine-image-2.0`。
2. **机械辅助探针（负向结果）**：肤色像素占比启发式**不可分**——本风格土黄/赭石调色板与肉色区间重叠，三版数值同量级（A 变体 ≈0.38–0.53；`_aux_flesh_share.py`）→ 不足以机械判定人体出现与否；判定以逐格目检为准。
3. **§8.1b v2 为派生编辑段（非档案原文）**：不影响 §8.1 / §8.2 / §4 逐字校验（`checks=33 ok=33 fail=0`）。
4. **E1_t1b 复现口径**：E1_t1b 记录的 michelangelo sha（`3326164f`）指向 v1；v1 全文仍可复现（卡内存档 + `s81b_v1_snapshot.md`）。
5. 人评六维打分（design.md §5）仍待评分者补。

## 6. 文件清单与复现

- `cells/e1_michelangelo_v2/`：`req_*.json` / `resp_*.json` / `img_*.jpg`（各 3 份；无失败尝试文件）
- `sheet_e1_michelangelo_v2.png` · `compare_michelangelo_v2.png` · `_inspect/`（3 张 2×2 放大）· `prompts_t1c.json`
- `run_log.jsonl` · `stats_t1c.json` · `sha256_manifest_t1c.txt`（19 条，含卡 sha）
- 审计：`s81b_v1_snapshot.md` · `s81b_v2_derivation.json` · `_backup_card_before_v2/michelangelo.md`
- 脚本链：`_apply_s81b_v2.py`（写 v2 入卡 + 快照 + 备份）→ `_extract_prompts_t1c.py` → `_gen_t1c.py batch`（重试 ≤2、间隔 0.8s）→ `_sheets_t1c.py` → `_report_t1c.py` → `_verify_t1c.py`（验收）
- 复现：写卡（如未应用）——先从 `_backup_card_before_v2/michelangelo.md` 恢复卡，再跑 `python _apply_s81b_v2.py`；出图链——`python _extract_prompts_t1c.py && python _gen_t1c.py batch && python _sheets_t1c.py && python _report_t1c.py && python _verify_t1c.py`
- 模块卡侧：`knowledge/domains/painters/modules/_extract.py --check` → `checks=33 ok=33 fail=0`（§8.1 段在 §8.1b 处截断比对；`--write` 重建保留 §8.1b 节）

## 7. 机械核验（2026-10-15）

- 图片文件：**3/3 存在**；Pillow 打开校验 3/3 通过；sha256 全部唯一。
- 请求/响应 JSON：req 3 份 / resp 3 份。
- 对照图 / 单格图存在且可打开。
- 模块卡：v2 块与 `prompts_t1c.json` 一致；v1 审计存档逐字（=snapshot）；逐字校验 `checks=33 ok=33 fail=0`。
- 验收脚本：`python _verify_t1c.py` → `VERIFY PASS`。

---

> 落款：MichelangeloV2（wave8）· 2026-10-15 · 产物自校验可复跑（见 §6）；引用请带路径。
