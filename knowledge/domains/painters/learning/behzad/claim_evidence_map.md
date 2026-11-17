<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-behzad；原正文 SHA-256 `8b8f0ea38e964a64048c83e7f5b2fc204e94e37716937957598ec7de8008395e`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-behzad — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-behzad/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 6ccc328100006497（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 30866616e12ec784（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/behzad.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `1515666b73ab64ccff1b9ef9614b67f56f6ab77a32ff673fbb884623a87772c0`；`§0`、`§1`、`§4`、`§8.2:L201-212`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [behzad.md](../../modules/behzad.md) sha256 `0133ab7b80a19a02b7dfa7a8c3fcfb3a5e79044fa657181dfb4a0c68baf25438`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [behzad.md](../../dossiers/_corpus/behzad.md) sha256 `6ded267c75af1e518e7d416501567fbb96aacd2b9767c926f31a500ec8280083`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/behzad.md:L202` §8.2-1「1. **无消失点规则**：全帧直线族中，平行后退线不得收敛——「消失点检验」= 0 组汇聚线（≥3 条线共点即失败）。自查：Hough 线检测 + 共点聚类。（依据：层叠平面空间 `[研究]`[R4][R6]）」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/behzad.md:L203` §8.2-2「2. **层叠分区规则**：画面须有 ≥2 个由建筑/台地/墙线切分的空间分区；事件点 ≥2 个分区（时间-空间转译可读）。自查：分区掩膜 + 事件对象计数。（依据：空间读作时间 `[研究]`[R1][R6]）」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/behzad.md:L204` §8.2-3「3. **人物比例恒定规则**：人物高度不随「纵深」缩放（上下位置变化 ≠ 大小变化）；同帧人物高度方差 ≤15%。自查：人体框高度统计。（依据：无透视纵深语法 `[研究]`[R4]）」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/behzad.md:L205` §8.2-4「4. **微书图案规则**：≥1 区域存在高频可读图案（砖/织物/瓷砖），图案频率高于全帧中位数；同时保留 ≥1 块「未图案化空场」（面积 ≥10%）。自查：高频能量图 + 空白区检测。（依据：微书精度 + 空场节奏 `…」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/behzad.md:L206` §8.2-5「5. **金预算规则**：金色（H 40–55°、S ≥0.5、V ≥0.7）面积 ≤5%，连通域 ≤7 个，每个须与「光晕/器皿/边框/宝座」之一相交。自查：HSV 掩膜 + 连通域。（依据：金只做点状 `[研究]`[…」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/behzad.md:L207` §8.2-6「6. **色阶克制规则**：色相簇 ≤8；最大色相簇面积 ≥20%（主调存在）；高饱和（S ≥0.7）面积 ≤25%（无全帧高饱和铺底）。自查：色相直方图聚类。（依据：克制色阶 `[研究]`[R4][R12]）」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/behzad.md:L208` §8.2-7「7. **文本整合规则**：文本栏/题记 ≥1 处，且与画面构图相交（不悬浮于空白角落）；书法线条密度与图案密度同量级。自查：文本区域检测 + 位置校验。（依据：手抄本页整体设计 `[史料]`[R1][R6]）」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/behzad.md:L209` §8.2-8「8. **勾线无排线规则**：明暗由色块深浅与勾线表达；交叉排线交叉点密度 ≈ 0；轮廓线宽度全帧方差小。自查：方向场 + 线宽统计。（依据：赫拉特晚期勾线特征 `[研究]`[R2][R4]）」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（11 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/behzad.md:§1-1`「\| 1 \| **层叠平面空间（无单点透视）**：纵深靠「平面层叠 + 上下位置」表达；地平线高置；平行后退线不收敛 \| 消失点检验 ≈ 0（无汇聚线族）；空间分区 ≥2 层 \| `[研究]` [R4]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/behzad.md:§1-2`「\| 2 \| **建筑切分叙事（空间读作时间）**：宫殿/宅院被「切开」为多室多层剖面；同一画面容纳时间序列（如七间锁室逐一穿行） \| 建筑剖面层数 ≥2；同建筑内事件点 ≥2 \| `[研究]` [R1…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/behzad.md:§1-3`「\| 3 \| **微书级精度**：织物、砖石、器物上满布可读纹样；书法/题记质量与画等重 \| 单位面积图案频率高；存在可读铭文/题记 ≥1 \| `[研究]` [R2][R4] \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/behzad.md:§1-4`「\| 4 \| **人物＝理想类型 + 微妙情绪**：非个体肖像，但姿态与表情比同代细密画更含蓄具体 \| 类型化面孔为主；情绪姿态 ≥1 处（低头/回首/伸手） \| `[研究]` [R1][R4] \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/behzad.md:§1-5`「\| 5 \| **克制色阶 + 金点**：矿物色有限套色；大面积「未图案化空场」；金作点状强调（光环、器皿、边框） \| 色相数量有限；空场面积可观；金面积小且集中 \| `[研究]` [R4][R12]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/behzad.md:§1-6`「\| 6 \| **明度对比被强调**：在平面系统内用深浅组织前后与焦点（「比中世纪细密画家更自觉地使用 value」） \| 明度分层清晰；焦点区对比高于四周 \| `[研究]` [R4] \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/behzad.md:§1-7`「\| 7 \| **姿态/视线编排**：人物的手势与朝向把观看路径「接力」过画面 \| 视线链 ≥3 跳（A 看 B、B 指向 C…） \| `[研究]` [R4][R12] \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/behzad.md:§1-8`「\| 8 \| **叙事游戏性（藏细节）**：半藏的眼睛、伪装的动物、边缘小事件——供内行「寻宝」 \| 与主叙事无关的嵌入细节 ≥1 \| `[研究]` [R4] \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/behzad.md:§1-9`「\| 9 \| **「签名式」枯树曲枝**：景观荒疏、树少叶、枝呈锐角折线，反复出现（研究者称几乎成签名母题） \| 树形重复特征；叶量低 \| `[研究]` [R10] \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/behzad.md:§1-10`「\| 10 \| **题记嵌入物件**：签名/纪年藏在器物（箭袋、袍服徽章、建筑铭文）上，不作独立落款 \| 签名位置 ∈ 画内物件 \| `[史料]` [R3][R6] \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F11 | `dossiers/behzad.md:§1-11`「\| 11 \| **手抄本页整体设计**：画面与书板/边框/书法的版面关系是作品的一部分；单页、双页、对开都是设计单位 \| 文本栏与画共排版；边框/书板样式统一 \| `[史料]` [R1][R6] \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-45"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/behzad.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/behzad.md:§8.2 尾注:L211`「> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母 = 假想参考帧）；1–2 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-behzad/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-53"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 32a9a8ca862cd9e7（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-behzad/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-behzad/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **30 行**（§A5+§B8+§C11+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
