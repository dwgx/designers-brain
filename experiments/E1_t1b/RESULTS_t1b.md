# E1_t1b · §8.1b 纯风格段重跑 · 同格对照（T1「暴风雨中的海边灯塔」）

> **E-02**（wave7）· 2026-10-15 · 直连网关 `/v1/images/generations` · 模型 `grok-imagine-image-2.0`
> 7 格 × 3 张 = **21 张**（明细见 §3）；E0 对照复用 `E1_t1/cells/e0_baseline`（不重跑）。
> 配方：`prompt = 主题句 + " " + 模块卡 §8.1b 纯风格正向段`（逐行解包为单行）；负向段未随请求发送（同 E1_t1）。
> 上游：`E1_t1/RESULTS.md`（偏置版 36 张 = 诊断素材）；本目录 =「题材偏置诊断 → §8.1b 拆分 → 重跑对照」收口产物。

## 1. 题材偏置诊断表（12 格）

> 口径：逐格目检 E1_t1 输出（36 张）× 对照模块 §8.1 的题材词。
> - **场景保留** = 输出即 T1 场景（灯塔＋礁岩＋风暴），题材词未实体化，或仅以无主体性的次要元素出现；
> - **场景被替换（题材偏置）** = 题材词实体化并占据/改写画面主体（人物 / 肖像 / 室内 / 静物 四类）。

| # | 格 | 分类 | prompt 题材词（§8.1 证据） | 输出内容描述（E1_t1 证据） | 处置 |
|---|----|------|---------------------------|---------------------------|------|
| 1 | e0_baseline | 场景保留（对照） | —（无风格段） | 写实灯塔＋礁岩＋巨浪＋乌云：纯 T1 场景 | —（对照复用） |
| 2 | e1_da_vinci | **场景被替换（题材偏置）** | 「a young woman seated…」「an ambiguous half-smile」「soft curly hair」「figures emerge…」（人物） | 前景女性坐像（卷发、微侧身）成为主角，灯塔退为背景；另有花卉/植物点缀 | → §8.1b + 重跑 |
| 3 | e1_michelangelo | **场景被替换（题材偏置）** | 「colossal muscular nude figures」「idealised faces」「heavy clinging drapery」（人物） | 裸体肌肉人物以漩涡状环绕画面，灯塔缩为中央小元素 | → §8.1b + 重跑 |
| 4 | e1_van_gogh | 场景保留（次要道具漂移） | 「flame-like cypress」「wheat field」「glowing lemon-yellow stars」（风景道具） | 灯塔＋巨浪＋涡旋星空主体保留；cypress / wheat field 作次要元素出现 | 注记（不重跑） |
| 5 | e1_monet | 场景保留 | —（无题材词） | 灯塔＋海＋浪完整保留（高调柔光化） | 注记（不重跑） |
| 6 | e1_picasso | **场景被替换（题材偏置）** | 「Analytic Cubist portrait」「a seated man」「watch chain / hands clasped in the lap」（肖像/人物） | 坐姿男子肖像（领带、表链、交叠双手）占主体，灯塔退为背景 | → §8.1b + 重跑 |
| 7 | e1_cezanne | **场景被替换（题材偏置）** | 「still-life foreground」「slightly tipped tabletop」（静物） | 前景静物（果盘、水果、布）占下三分之一，灯塔风景退为中远景 | → §8.1b + 重跑 |
| 8 | e1_matisse | 场景保留（抽象剪影漂移） | 「dancer / snail / leaf / star motifs」（母题词） | 灯塔＋浪＋云保留；leaf / star 等抽象剪影少量出现；未见人物 | 注记（不重跑） |
| 9 | e1_hokusai | 场景保留（次要题材元素） | 「distant Mount Fuji」「tiny silhouetted figures」（风景/人物·微型） | 灯塔＋浪＋雨主体保留；富士山与微型人物仅作远景/比例元素 | 注记（不重跑） |
| 10 | e1_caravaggio | **场景被替换（题材偏置）** | 「faces and hands catch the light」「gestures point at…」「ordinary working people」「plain dark interior」（人物/室内） | 人物叙事占主体（指点灯塔 / 持灯塔画布），灯塔退为道具或背景 | → §8.1b + 重跑 |
| 11 | e1_vermeer | **场景被替换（题材偏置）** | 「interior genre scene, single figure…」「window」「tiled floor」（室内/人物） | 室内场景＋窗前人物；灯塔仅透过窗/画框可见 | → §8.1b + 重跑 |
| 12 | e1_durer | **场景被替换（题材偏置）** | 「allegorical objects…dense still-life of symbols」「monogram plate / cartellino」（静物） | 前景符号静物（罗盘、球体、梯子、沙漏等）＋签名牌占下三分之一；灯塔风景保留于中远景 | → §8.1b + 重跑 |

**小结**：12 格中 **7 格判定「场景被替换（题材偏置）」** → 全部进入 §8.1b 拆分 + 重跑（da_vinci / michelangelo / picasso / cezanne / caravaggio / vermeer / durer）；5 格「场景保留」（e0 对照 + van_gogh / monet / matisse / hokusai；其中 3 格含次要漂移，记入 §2.3 注记）。

## 2. §8.1b 拆分记录（7 卡纯风格段 + 4 卡注记）

### 2.1 口径与位置

- **删除**：题材词（人物 / 肖像 / 室内 / 静物）与场景专属道具；**保留**：视觉语言（光 / 色 / 笔触 / 结构 / 构图规则）与氛围；个别句做最小改写以保可读（明细见 §2.2）。
- **位置**：`knowledge/domains/painters/modules/<id>.md` →「## §8.1b 纯风格段（场景可迁移）」（7 卡）；未偏置卡为「## §8.1b 场景可迁移性注记」（4 卡）。
- **§8.1 原样保留**：逐字校验不受影响——`python _extract.py --check` → `checks=33 ok=33 fail=0`（§8.1 段在 §8.1b 处截断后比对；`--write` 重建时原样保留 §8.1b 节）。
- **审计**：删除项 / 改写 / 全文见 `s81b_derivation.json`；写入脚本 `_apply_s81b_cards.py`（改动前备份在 `_backup_cards_before_s81b/`）。

### 2.2 删除 / 改写明细（7 卡）

| 卡 | 删除项（题材词 / 道具） | 最小改写 |
|----|--------------------------|----------|
| da_vinci | young woman、half-smile、curly hair、figures、flowers | the figures→forms、distant mountains→distant forms |
| michelangelo | nude figures、muscle groups、bodies（torsion）、drapery、idealised faces、flesh tones | figures→forms（3 处） |
| picasso | portrait、seated man、anchors（hair / tie / watch / hands）、seated pose、frontally posed | figure and background→foreground and background |
| cezanne | still-life foreground、Bathers period、tipped tabletop | objects carry→forms carry、Bathers period→late period |
| caravaggio | faces and hands、gestures、working people as saints、dark interior（no landscape / no sky）、prop accent | walls and floor→areas、figures pushed flat→the main motif pushed flat、narrative action→dramatic action |
| vermeer | interior genre scene、single figure、window、plaster wall、object list（porcelain…bread crust）、tiled floor / window frames、Delft world | single window→single source、plaster wall→pale areas、pushing the figure forward 删除 |
| durer | contrapposto figures、microtexture examples（hairs / grass / leaf）、monogram plate、cartellino、allegorical still-life | calm measured figures…→calm, measured composition |

### 2.3 未偏置卡注记（4 卡，一句话）

| 卡 | 场景可迁移性注记 |
|----|------------------|
| van_gogh | §8.1 无人物/肖像/室内/静物题材词；E1_t1 灯塔场景保留，风格可直接跨场景迁移（cypress / wheat field / stars 等风景道具词仅作次要元素出现，可按需删除）。 |
| monet | §8.1 无题材词；E1_t1 灯塔场景完整保留，风格可直接跨场景迁移（无需拆分）。 |
| matisse | §8.1 仅含装饰母题词（dancer / snail / leaf / star）；E1_t1 未见人物实体化、场景保留，风格可迁移（如需更纯净可删母题词）。 |
| hokusai | §8.1 含 Mount Fuji / tiny figures 等非主体题材词；E1_t1 中仅作远景与比例元素、未替换场景，风格可迁移（如需更纯净可删上述词）。 |

## 3. 重跑结果总表（7 行）

| # | 格 | 模块 | §8.1b sha 前 8 | 尺寸（请求 → 实回） | 耗时 | sha256 前 8 位（img_01 / 02 / 03） |
|---|----|------|----------------|--------------------|------|-----------------------------------|
| 1 | e1_da_vinci | 达·芬奇 | 21015cfe | 1024x1536 → 768×1152×3 | 51.6s（均 17.2s/张） | ddd68b7e / a6e4b014 / 418d75e9 |
| 2 | e1_michelangelo | 米开朗基罗 | 3326164f | 1024x1536 → 768×1152×3 | 61.0s（均 20.3s/张） | 10447f51 / 697f5921 / e39ca250 |
| 3 | e1_picasso | 毕加索 | 6d730e72 | 1024x1536 → 768×1152×3 | 51.7s（均 17.2s/张） | b611e9ab / bb8001a0 / 1bf23ac6 |
| 4 | e1_cezanne | 塞尚 | 9a3502cb | 1024x1536 → 768×1152×3 | 72.0s（均 24.0s/张） | b2bc10f9 / fcd67657 / a6b0ee7a |
| 5 | e1_caravaggio | 卡拉瓦乔 | e651a3eb | 1024x1536 → 768×1152×3 | 59.1s（均 19.7s/张） | 407e57f5 / 32be7e27 / 1c7a5dc9 |
| 6 | e1_vermeer | 维米尔 | 012500f1 | 1024x1536 → 768×1152×3 | 56.0s（均 18.7s/张） | 037458d4 / 9cbcb65d / d4bbb159 |
| 7 | e1_durer | 丢勒 | 381ab146 | 1024x1536 → 768×1152×3 | 65.0s（均 21.7s/张） | 2264f442 / a22b5ae8 / ce61fc80 |

合计 **21/21 张一次成功**（0 重试、0 失败；总耗时 433s，均 ≈20.6s/张）。E0 对照复用 `E1_t1/cells/e0_baseline`（sha 前 8：71c50d88 / 2fa08527 / 75bdf061，未重跑）。
耗时口径同 E1_t1：该格全部尝试的「请求→落盘」时长合计；明细见 `run_log.jsonl` / `stats_t1b.json`。

## 4. 同格对照（偏置版 §8.1 vs 纯风格版 §8.1b）

> 每格三行对照图：`compare_<cell>.png`（上：E0 对照 / 中：§8.1 偏置版 / 下：§8.1b 纯风格版）；7 格总表 `compare_all_t1b.png`。

| # | 格 | 偏置版（§8.1，E1_t1） | 纯风格版（§8.1b，E1_t1b） | 判定 |
|---|----|----------------------|---------------------------|------|
| 1 | e1_da_vinci | 前景女性坐像（卷发/微侧身/谜样微笑）成主角；花卉点缀；灯塔退为背景 | 女性/花卉消失；雾中灯塔＋圆锥形礁岩＋暗海涌浪；sfumato 无硬边、低饱和、单侧柔光、空气透视 | **解除** |
| 2 | e1_michelangelo | 裸体肌肉人物漩涡环绕画面；灯塔缩为中央小元素 | 灯塔升为画面中心锚点；但巨型肌肉形体仍环绕出现（云体巨人/盘绕巨体）——人物母题未消除 | **部分解除** |
| 3 | e1_picasso | 坐姿男子肖像（领带/表链/交叠双手）占主体；灯塔退为背景 | 男子消失；灯塔分解为 40–120 个半透明角面（5 色系/6 级明度跳变）；浪花成棱面白簇 | **解除** |
| 4 | e1_cezanne | 前景静物（果盘/水果/布）占下三分之一；灯塔风景退为中远景 | 静物消失；灯塔＋海岸＋海面全部由短平行笔触（taches）构成；天空与大地等分量、无大气后退 | **解除** |
| 5 | e1_caravaggio | 人物叙事（指点灯塔/持灯塔画布）占主体；灯塔退为道具或背景 | 人物消失；单一高位硬光夜海——灯塔/灯室受光、浪花高光、其余压近黑；暖土色域＋受光边缘厚涂 | **解除** |
| 6 | e1_vermeer | 室内场景＋窗前人物；灯塔仅透过窗/画框可见 | 室内/人物消失；灯塔＋海岸在单侧柔光下高调呈现；蓝灰平影、青金＋赭黄对、点状高光 | **解除** |
| 7 | e1_durer | 前景符号静物（罗盘/球体/梯子/沙漏等）＋签名牌占下三分之一 | 静物/cartellino 消失；纯排线灯塔海景（天空密线场、浪花留白）；img_02 左下残留小「D」标记 | **基本解除** |

### 4.1 e1_da_vinci — 解除

- 偏置版：三张均为「前景女性坐像＋背景灯塔海岸」，人物是画面主角（§8.1 的 young woman 句逐字落地）。
- 纯风格版：女性与花卉全部消失；三张均为雾中灯塔海景（img_01 暖光黄昏、img_02 雾中灯标、img_03 圆锥礁岩群）——sfumato/空气透视/窄色域完整保留；保留的「rocks shaped like rounded cones」形状语言直接以圆锥形礁岩呈现。
- 结论：删除人物句后风格未受损，偏置干净解除。

### 4.2 e1_michelangelo — 部分解除（重要反例）

- 偏置版：裸体人物填满画面、灯塔被挤成中央小元素。
- 纯风格版：构图重心回到灯塔（灯塔居中、可读性大幅提升）；但「巨型肌肉形体」仍以漩涡状环绕出现（img_01/02 云体巨人、img_03 盘绕巨体），人体母题未消除。
- 结论：**题材偏置的根源不只在题材名词，还在与人体绑定的视觉语言本身**（serpentine torsion / 雕塑式体积 / 仰视透视 / 「many interlocking forms」会被模型解读为人体）。仅删名词不足以解除；彻底解除需进一步改写这些从句（或接受「人体即本模块风格本体」）。已留作 E1_t1b 的负向发现，未二次调参。
- 后续（E-03 · E1_t1c，2026-10-15）：已从句级改写 §8.1b（v2）并重跑——T1 重跑 3/3 解除（无人形母题）；见 `experiments/E1_t1c/RESULTS_t1c.md` §4。

### 4.3 e1_picasso — 解除

- 偏置版：坐姿男子（领带/表链/交叠双手等 anchors）为画面主角。
- 纯风格版：男子消失；灯塔成为 40–120 个半透明角面组成的「棱面灯塔」（灯室可辨），浪花亦成棱面白簇；4–5 色系、中心最亮、边缘暗晕全部落地。
- 结论：删除 portrait/man/anchors 后，立体主义方法完整迁移到灯塔场景。

### 4.4 e1_cezanne — 解除

- 偏置版：果盘/水果/布的静物前景占画面下三分之一。
- 纯风格版：静物消失；灯塔、海岸、海面、天空全部由短平行笔触（taches）构成；天空与大地等分量、无大气后退、蓝网络贯穿阴影与轮廓。
- 结论：删除 still-life foreground / tipped tabletop 后，笔触与色彩调制语言完整迁移。

### 4.5 e1_caravaggio — 解除

- 偏置版：人物叙事（指点灯塔或持灯塔画布）占主体。
- 纯风格版：人物消失；夜海场景中灯塔与灯室被单一高位硬光照亮、浪花为高光主战场、其余压入近黑；暖土色域与受光边缘厚涂（impasto）完整落地。
- 结论：删除人物句与「dark interior, no landscape, no sky」后，tenebrism 光源结构完整迁移到夜景海景。

### 4.6 e1_vermeer — 解除

- 偏置版：室内场景＋窗前人物；灯塔仅透过窗/画框可见。
- 纯风格版：室内与人物消失；灯塔＋海岸在单侧柔光（左）下高调呈现——蓝灰平影、青金＋赭黄对、水面点状高光（pointillés）、软边。
- 结论：删除 interior/figure/window 等词后，「柔光＋高调＋蓝灰影」的光学语言完整迁移；氛围由暴烈转为静谧（风格固有，非题材漂移）。

### 4.7 e1_durer — 基本解除

- 偏置版：前景符号静物（罗盘/球体/梯子/沙漏/魔方阵）＋cartellino/签名牌占下三分之一。
- 纯风格版：静物与 cartellino 消失；纯排线版灯塔海景——天空以密线场收口、浪花以留白纸色表现、交叉排线塑形。
- 残留：img_02 左下角有小「D」形标记（Dürer monogram 残影，minor）；判定「基本解除」。

## 5. 缺口与偏差

1. **通道口径与 E1_t1 一致**：负向段未发送（通道无负向参数，见 `E1_t1/RESULTS.md` §3）；`size` 请求 1024x1536、实回 768×1152（不严格）；模型用裸名 `grok-imagine-image-2.0`。
2. **本次重跑无重试/无失败**：21 张一次成功（总尝试 21；耗时 433s）。与 E1_t1（37 次尝试、1 失败）相比本次更顺。
3. **§8.1b 为派生编辑段（非档案原文）**：删除/改写逐卡记录于 §2.2 与 `s81b_derivation.json`；§8.1 原样保留（逐字校验 33/33）。
4. **残留（重跑观察，未二次调参）**：e1_michelangelo 人物母题未完全解除（风格语言与人体绑定，见 §4.2）；e1_durer img_02 左下残留小「D」标记。
5. **E0 对照未重跑**：按任务口径复用 `E1_t1/cells/e0_baseline`。
6. **评分口径**：本报告 §4 为单评审（agent 目检）描述性对照；design.md §5 六维人评打分仍待评分者补。

## 6. 文件清单与复现

- `cells/<cell>/`：`req_*.json` / `resp_*.json` / `img_*.jpg`（7 格 × 3 组；无失败尝试文件）
- `sheet_<cell>.png` ×7 · `sheet_all_t1b.png`（8 行 = E0 对照 + 7 格）· `compare_<cell>.png` ×7 · `compare_all_t1b.png`
- `prompts_t1b.json` · `run_log.jsonl` · `stats_t1b.json` · `sha256_manifest_t1b.txt`（81 条）
- 脚本链：`_apply_s81b_cards.py`（写 §8.1b 入卡）→ `_extract_prompts_t1b.py` → `_gen_t1b.py batch`（重试 ≤2、间隔 0.8s）→ `_sheets_t1b.py` → `_report_t1b.py` → `_verify_t1b.py`（验收）
- 复现：`python _apply_s81b_cards.py && python _extract_prompts_t1b.py && python _gen_t1b.py batch && python _sheets_t1b.py && python _report_t1b.py && python _verify_t1b.py`
- 模块卡侧：`knowledge/domains/painters/modules/_extract.py --check` → `checks=33 ok=33 fail=0`（§8.1 段在 §8.1b 处截断比对；`--write` 重建保留 §8.1b）；`README.md` 已补 §8.1b 使用/维护说明；改动前卡片备份在 `_backup_cards_before_s81b/`。

## 7. 机械核验（2026-10-15）

- 图片文件：**21/21 存在**；Pillow 打开校验 21/21 通过；sha256 去重后 21 个（全部唯一）。
- 请求/响应 JSON：req 21 份 / resp 21 份（均含于各格目录）。
- 全量哈希：`sha256_manifest_t1b.txt`。
- 模块卡：7 卡「§8.1b 纯风格段」+ 4 卡「§8.1b 场景可迁移性注记」；逐字校验 `checks=33 ok=33 fail=0`。
- 验收脚本：`python _verify_t1b.py` → `VERIFY PASS`（21/21 张 + 诊断表 12 行 + 同格对照 7 行 + §8.1b 7+4 + 逐字校验 33/33）。

---

> 落款：EStyleSep（wave7）· 2026-10-15 · 产物自校验可复跑（见 §6）；引用请带路径。
