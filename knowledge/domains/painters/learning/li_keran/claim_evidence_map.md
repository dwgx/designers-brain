<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-li_keran；原正文 SHA-256 `2381a3c6dee5294e36bebba0859513f257d0e33e427303357410fc78cc973a5b`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-li_keran — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-li_keran/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 a581c39218d2121a（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 5bf338c0f6ff1421（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/li_keran.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `3ccf87470ed40599724aa05b584b9b1e661dbd980cb918781986547c02c500f5`；`§0`、`§1`、`§4`、`§8.2:L222-233`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [li_keran.md](../../modules/li_keran.md) sha256 `524d277b9ac0dfa4989d7693d867cd1a8034d85bcbdbd8ab4d23d9c36c9bc53b`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [li_keran.md](../../dossiers/_corpus/li_keran.md) sha256 `f314ffda14a9b1044f57586858a4581f73bd3efa55fb83aa4f17b2890850ed44`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/li_keran.md:L223` §8.2-1「1. **逆光结构规则**：画内最亮区（V≥0.85）被暗部（V≤0.35）包围比例 ≥60%；光向一致度 ≥70%；「亮口」连通域 **1–3 个**（画眼集中，避免平均）。自查：亮度直方图 + 光源方向估计 + 连通…」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/li_keran.md:L224` §8.2-2「2. **积墨层次规则**：深色区（V≤0.35）内可辨明度层 **≥5 级**；无单一死黑连通域 >15% 画面；无镜面高光（V≥0.98 且面积>1%）。自查：局部直方图 + 分水岭分层计数 + 高光掩膜。（依据：[…」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/li_keran.md:L225` §8.2-3「3. **满构图规则**：留白（V≥0.9 且 S≤0.1 的近纸色区）**≤15%**；主体触画幅边 ≥1 处；无连续空白背景带（对照 C-17）。自查：纸色掩膜统计 + 边缘接触检测。（依据：[R20]「满」；§1-…」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/li_keran.md:L226` §8.2-4「4. **亮口形态规则**：垂直亮带（高宽比 ≥5:1）≥1（瀑布档）或水面亮区 ≥15% 面积（江景档）——二选一必居其一；亮口边缘有墨色烘染过渡带（≥0.5% 短边）。自查：形态学 + 连通域 + 梯度带宽。（依据：…」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/li_keran.md:L227` §8.2-5「5. **色域规则**：常规档——无彩色区（S≤0.25）面积 ≥70%，彩色仅限赭石/花青/藤黄低饱和烘染；朱砂档——红色（H∈[0,15]∪[345,360]，S≥0.5）面积 30–70%，红区边缘黑墨交织（红黑边…」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/li_keran.md:L228` §8.2-6「6. **柔边规则**：无硬投影——阴影边界过渡带 ≥1% 短边（软于卡拉瓦乔档）；全帧明度中位 ≤0.35；最亮/最暗比 ≥8:1（极限对比）。自查：梯度带宽 + 直方图。（依据：[R6][R8]；§1-2）」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/li_keran.md:L229` §8.2-7「7. **点景规则**：点景（屋/船/人/牛）合计 ≤10% 面积、单体 ≤2%；白墙黑瓦对 ≤20 组；人物/牛高度 ≤画面高 1/10。自查：实例计数（检测或人工）。（依据：§1-7）」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/li_keran.md:L230` §8.2-8「8. **体量规则**：主峰/主体面积 ≥25%；主体轮廓由墨块边缘生成（无细线勾描：边缘线宽 >2px 占比 ≤20%）；垂直元素（瀑布/树干/塔）≥1 条贯穿中景。自查：分区统计 + 边缘宽度直方图。（依据：[R8]…」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（12 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/li_keran.md:§1-1`「\| 1 \| **逆光成画眼**：光在景物背后——山体/林木背光成重墨体块，轮廓与缝隙透光；「亮」从「黑」里渗出 \| 画面最亮区（瀑布/水面/云气）位于景物之后或被重墨包围；主体正面最暗区与背景最亮区同…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/li_keran.md:§1-2`「\| 2 \| **积墨的层叠黑**：墨分多遍积染、层理可辨，黑而透气——「黑中透亮」 \| 深色区明度低（V≤0.2）但梯度连续、可辨层次 ≥5 级；无死黑、无油光 \| `[研究]`（[R5][R8]）…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/li_keran.md:§1-3`「\| 3 \| **满构图**：景物充满画幅、天地留白极少；主体顶天立地、「扑面而来」 \| 留白（纸色）面积 ≤15%；主峰/树冠触画幅边 ≥1 处 \| `[归纳]`（据 [R6][R8] 观察；与范宽「…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/li_keran.md:§1-4`「\| 4 \| **重与厚的体量**：山如铁铸、树如墨柱；团块性笔墨结构（非线描结构） \| 团块面积占比高；轮廓由墨块边缘生成而非细线勾描 \| `[研究]`（[R8]「团块性笔墨结构」） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/li_keran.md:§1-5`「\| 5 \| **亮口的定点**：瀑布/江水/白墙/云气作为「光」的载体，成为最强对比 \| ≥1 处「亮口」（V≥0.85 连通域）被重墨包围；全帧明度中位 ≤0.35 \| `[归纳]`（据 [R6][…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/li_keran.md:§1-6`「\| 6 \| **对景写生的光学空间**：定点观察、真实光影关系；中景为主体 \| 画内光向统一（阴影方向一致度 ≥70%）；中景占画面主体、近景少 \| `[史料/研究]`（[R4][R6]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/li_keran.md:§1-7`「\| 7 \| **点景符号**：白墙黑瓦屋舍、帆船、山道、牧童与牛——微小点景与巨大山水同框 \| 点景合计 ≤画面面积 10%；人物/牛高度 ≤画面高 1/10 \| `[归纳]`（据 [R6][R8]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/li_keran.md:§1-8`「\| 8 \| **色彩克制**：以墨为主，赭石/花青/藤黄为辅；朱砂红（万山红遍）为特例档 \| 常规档墨色区 ≥70%；朱砂档：红色（朱砂域）为主色、仍以黑墨压阵 \| `[归纳]`（据 [R6][R9]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/li_keran.md:§1-9`「\| 9 \| **笔法沉涩**：用笔慢、重、涩，短促笔线积叠；书法（北碑/黄道周）功底入画 \| 线条短促、无飘滑长线；飞白、墨点与积染并用 \| `[研究]`（[R6]「沉涩的笔调」；[R17]「慢」）…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/li_keran.md:§1-10`「\| 10 \| **瀑布＝垂直光柱**：瀑布作垂直亮带切入黑山——他反复使用的「光」装置 \| ≥1 条垂直亮带（高宽比 ≥5:1）贯穿中景；带缘有墨色烘染过渡 \| `[归纳]`（据 [R6]「瀑布浓缩为…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F11 | `dossiers/li_keran.md:§1-11`「\| 11 \| **题跋与印章**：长题记录创作缘起；「废画三千」「白发学童」「可贵者胆」「所要者魂」「千难一易」「师牛堂」等 \| 印章可辨；题跋常 ≥10 字；部分作品重复题写同一段文字（牛图） \| `[史料]`（[R1][R4][R6]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F12 | `dossiers/li_keran.md:§1-12`「\| 12 \| **牛与牧童的墨块**：牛体以浓墨大块造型、牧童细线点出；与山水同源的笔墨练习 \| 牛体块面感强、四肢结构简练；多与柳树/水塘组合 \| `[史料/研究]`（[R6][R9]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-46"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/li_keran.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/li_keran.md:§8.2 尾注:L232`「> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–4 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-li_keran/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-54"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 c6d77a44affe8228（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-li_keran/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-li_keran/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **31 行**（§A5+§B8+§C12+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
