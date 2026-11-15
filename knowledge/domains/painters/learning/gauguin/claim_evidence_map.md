<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-gauguin；原正文 SHA-256 `3bb1e1652cf909872b97f1d35c3de922a4b3d84b40134d18be2b632bcf915e0e`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-gauguin — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-gauguin/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 f6058261bf18bc4e（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 985b06a55b311fc4（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/gauguin.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `7211fa83a2944a5b1b35349c1b20171376f35b395efbcb8e836340adae7a619c`；`§0`、`§1`、`§4`、`§8.2:L218-229`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [gauguin.md](../../modules/gauguin.md) sha256 `bb5a3059b2eb96ec7029fd416ec0db3effeaf77beb8637872e79bdc6db23abf2`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [gauguin.md](../../dossiers/_corpus/gauguin.md) sha256 `41266f71a6b6915f6fe706246280845d954858123c639b80a7ab937820741c46`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/gauguin.md:L219` §8.2-1「1. **平涂度规则**：主要色块（各 ≥5% 画布面积）内部明度标准差 ≤5%（0–255 尺度 ≤12）、色相变化 ≤8°；全帧「渐变带」（连续过渡 >2% 短边）面积 ≤10%。自查：区域分割 + 分区统计。」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/gauguin.md:L220` §8.2-2「2. **轮廓线规则**：暗轮廓（明度 ≤30%）线宽 ≥0.3% 短边；覆盖主要形体边界 ≥60%；线宽变异 ≤2:1（不得时粗时细如书法）。自查：边缘/线条检测 + 暗像素掩膜。（依据：[R3]「heavy blac…」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/gauguin.md:L221` §8.2-3「3. **色数规则**：主色 ≤10（含黑轮廓）；**光学混合点阵 0 命中**（点径 ≤2 px 的孤立像素簇不得成规模 ≥5% 面积）。自查：色彩量化 + 点阵检测。（与修拉模块的分离判据）」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/gauguin.md:L222` §8.2-4「4. **硬边界规则**：色块边界梯度带 ≤1% 短边（无羽化、无抗锯齿宽边）；相邻色块明度跳变 ≥15%。自查：边界梯度剖面。（依据：[R3]「no subtle gradations」）」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/gauguin.md:L223` §8.2-5「5. **空间规则**：线性透视消失点检测 0 命中；水平色带 ≥2 层（绿/黄/红类）；天空区（如存在）为纯色或图案、**非渐变**。自查：直线透视检测 + 色带分割。（依据：[R8]「天空消失了」）」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/gauguin.md:L224` §8.2-6「6. **装饰同权规则**：图案区与人物区渲染级别差 ≤1 级（同为平涂）；强档图案密度 ≥10% 面积（pareu/纹样/树冠图案化）。自查：分区渲染级别比对。（依据：[R1]「decorative abstract…」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/gauguin.md:L225` §8.2-7「7. **象征色锚点规则**：≥1 处非自然色区（红草地/黄天/粉沙/紫影）≥8% 面积，且与主题锚定（宗教/神话/异域——须能指出对应关系）。自查：色相异常检测 + 主题对照表。」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/gauguin.md:L226` §8.2-8「8. **合成/静止规则（视频帧附加）**：场景不可对景复原（多源拼合特征：人物/神像/纹样来源异质）；静止悬置——事件外光流 Δ ≤1%/帧；无运动模糊、无镜头运动（与 C-09 运动预算的「冻结」侧一致）。自查：光流…」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（10 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/gauguin.md:§1-1`「1. **平涂色块**：大面积色块内部**几乎无渐变、无笔触纹理**——单区明度变化 ≤5%、笔触被抹平；与印象派/塞尚的「笔触构造」直接对立。`[研究]`（[R1]「broad, matte fie…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/gauguin.md:§1-2`「2. **景泰蓝式粗轮廓（Cloisonnism）**：形体由**深色粗轮廓线**勾出、内部平涂——命名来自中世纪景泰蓝珐琅（cloisonné）工艺（批评家 Édouard Dujardin 命名，…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/gauguin.md:§1-3`「3. **象征性/非自然色彩**：颜色不与自然对应——**红草地、柠檬黄天空、粉沙滩、紫色阴影**；用色按情绪/象征逻辑选择（「最美的绿」「尽可能蓝」）；Met 语：他「**把色彩从模仿再现中解放出来…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/gauguin.md:§1-4`「4. **色带层叠的空间（天空常被删除）**：无传统透视；空间由 2–4 条水平色带层叠构成。Orsay 对《Arearea》的判语：**「天空消失了，绿—黄—红的平面序列构成构图的骨架」**（"Le…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/gauguin.md:§1-5`「5. **装饰性图案与人物结合**：图案（布料纹样、雕像、树冠、器物）与人物**同权**；Met 语：塔希提作品「把**装饰性抽象图案**与人物形象结合」（"combining decorative…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/gauguin.md:§1-6`「6. **简化与古拙化**：形体简化为本质轮廓——「简化形体与比例，让轮廓获得有力而雄辩的表现力」（Sérusier 转记 1888）；人物**正面/侧面化、姿态庄严静止**（hieratic）。`[…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/gauguin.md:§1-7`「7. **记忆与想象的合成**：场景不是对景写生——由**照片（婆罗浮屠浮雕、马奈《奥林匹亚》）、文献（Moerenhout 1837）、记忆、其他画作**重组而成（自引与母题复用：同一人物在多画中「…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/gauguin.md:§1-8`「8. **静穆与神秘（mystery）**：画面安静、时间悬置——Mallarmé 的判语「**如此明亮中放入如此多的神秘**」被高更本人反复引用为题词。`[史料]`（[R16]）`[研究]`（[R1…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/gauguin.md:§1-9`「9. **母题群**：布列塔尼（coiffe 农妇、十字架、收获、田野）→ 塔希提/马克萨斯（vahine、pareu、神像、芒果、热带植被）→ 宗教图像（基督、圣母、天使、幽灵 Tupapau）。`…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/gauguin.md:§1-10`「10. **哑光表面**：稀释油彩（*peinture à l'essence*——沥去油、以松节油调色）与吸油处理 → **哑光、无光、近壁画**的表面；木刻则粗粝（像木雕一样凿刻）。`[研究]`（…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-44"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/gauguin.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/gauguin.md:§8.2 尾注:L228`「> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–5 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-gauguin/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 8 个规则边界入口为 [inference] 纸面设计；不等于 8 个已成立反例 |

<a id="db-source-line-52"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 b2bc3df85fc2c3aa（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-gauguin/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-gauguin/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **29 行**（§A5+§B8+§C10+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

<a id="db-source-line-63"></a>
## §F 修复补充锚点（非原 29 行表格的新实测 claim）
- **G-E1/G-E2 / 局部规则**：dossier §12《黄色基督》、§8.2 R1/R2/R3 与 §4 P1/P2/P3。六色练习及固定形状／布局／色板、80% 对 40% 轮廓控制均为 proposed；数字是设计目标，未测。
- **G-E3 / 形式与语义范围**：corpus #3 与 #5（本地自述分级）、dossier §12《布道后的幻象》《死者的幽灵》、§8.2 R7。对象可替换，不自动删除选定关系；不要求所有练习具有宗教符号。
- **规则否定的限度**：dossier §4 至少 P1/P2/P3 之二中档，P6 为工作流。单 R 失败不推出全局风格否定；静态图不能证明来源工作流。原表仍为 29 行；本节仅补可寻址的教学假设，不更新为已验证机制。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
