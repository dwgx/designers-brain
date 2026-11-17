<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-kitagawa_utamaro；原正文 SHA-256 `8f6a11b4427bfd4beb757919c10e6e8299d07d9e67abf2629dc5e5ebfa843a25`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-kitagawa_utamaro — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-kitagawa_utamaro/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 08969b0fdbb7e3e2（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 22c2937ae8b76c94（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/kitagawa_utamaro.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `8d7393648f604216c6eb144817d8fb6e507bfe134c89da075f4a83348c30ee86`；`§0`、`§1`、`§4`、`§8.2:L190-198`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [kitagawa_utamaro.md](../../modules/kitagawa_utamaro.md) sha256 `173affaf6c46f9c45f5a237e957daf4da88d7423642916c598142cb92ee038b9`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [kitagawa_utamaro.md](../../dossiers/_corpus/kitagawa_utamaro.md) sha256 `4761e57ca3019a43abdd39ab908d725b2221ba8c632e9b30aa643570092920de`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 7 条规则逐条回源（7 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/kitagawa_utamaro.md:L191` §8.2-1「1. **特写比例**：头部（含髪）高度 ÷ 画高 ≥40%（强档 ≥50%）；裁切线位于肩—胸之间；主体人形数 = 1（镜中映像计为同一主体）。`[归纳]`」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/kitagawa_utamaro.md:L192` §8.2-2「2. **线系统**：無線档——面部边缘无连续墨线（面部轮廓线覆盖率 ≤10%）且靠底色对比读形；标准档——毛描き细线密度 ≥15 条/100px（发区）、衣纹主線单笔连续 ≥60px 占比 ≥50%。`[归纳]`」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/kitagawa_utamaro.md:L193` §8.2-3「3. **背景规则**：背景为均质场（局部方差 ≤ 阈值）或云母纹理；背景道具 ≤2 件；投影/阴影面积 ≤2%；无透视消失点（收敛点 ≤1 且不在画内）。`[归纳]`」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/kitagawa_utamaro.md:L194` §8.2-4「4. **色域规则**：肌肤区（低饱和高明度）≥25% 面积；墨/黑（发）≥12%；主色相 ≤6 族；渐变带宽度 ≤1% 短边（轻ぼかし ≤1 段）。`[归纳]`」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/kitagawa_utamaro.md:L195` §8.2-5「5. **微表情差分规则**：同系列多帧时，眉/目/口线段的帧间差异 ≤3px 级（参考帧）但可辨——结构相似度落于 0.75–0.95 区间；禁「同脸复制」与「无差异」。`[归纳]`」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/kitagawa_utamaro.md:L196` §8.2-6「6. **手势-道具规则**：≥1 处手部与道具/面部交互（持·触·托）；可辨手指数 ≥3；道具 ≤2 件；手部线密度高于衣纹（重点描写区）。`[归纳]`」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/kitagawa_utamaro.md:L197` §8.2-7「7. **静帧语义**：单帧发布时按静帧处理——动画时人物位移 ≤1% 画幅/秒、转折（振り向き）≤1 次；禁叙事推拉与镜头运动（与德加卡「过程态」互斥，见 §3.1）。`[归纳]`」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-28"></a>
## §C §1 视觉指纹（10 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/kitagawa_utamaro.md:§1-1`「\| 1 \| **大首绘特写**：头与肩占据画面——「近接した三分身」「首から上で切り取った特徴的構図」 \| 头部（含髪）高度 ÷ 画高 ≥40%（强档 ~50%+）；裁切位于肩—胸之间 \| `[研究]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/kitagawa_utamaro.md:§1-2`「\| 2 \| **线条的微表情**：一見似て非なる脸——眉、细长目（slit eyes）、鼻筋、小口由线段微差区分人物与情绪 \| 眉/目/口线段差异 ≤3px 级（参考帧）但可辨；「顔立ちや表情、目や眉…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/kitagawa_utamaro.md:§1-3`「\| 3 \| **毛发细线（毛描き/kewari）**：发丝一根一根、「delicate lines to convey the form and flow of hair」 \| 发区细线密度显著高于衣…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/kitagawa_utamaro.md:§1-4`「\| 4 \| **背景压缩与云母/空摺**：云母摺 glitter 衬底、無線空摺、素背景——无景深、无投影 \| 背景为均质场（单色/云母纹理）；背景道具 ≤2 件 \| `[史料]`+`[研究]`（[R…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/kitagawa_utamaro.md:§1-5`「\| 5 \| **不施轮廓线的肌肤**：顔・首の輪郭に墨線を用いず、版の凹凸（無線空摺）で表現；肤色自背景「浮出」 \| 面部边缘无连续墨线（無線档）；肌肤区低饱和高明度 \| `[研究]`（[R9]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/kitagawa_utamaro.md:§1-6`「\| 6 \| **服饰图案**：小纹·格子·縞·千鸟·菊等「fashion media」；图案细密而色调克制 \| 彩色像素 ≤50%；色相 ≤5 族；墨线始终可见 \| `[研究]`（[R8][R16]）…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/kitagawa_utamaro.md:§1-7`「\| 7 \| **手势与道具**：手拭·団扇·文·镜·ポッピン·烟管——手部动作承担情绪（托腮、绞巾、持扇） \| ≥1 处手—道具/面部交互；手指数可辨 \| `[研究]`（[R10][R8]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/kitagawa_utamaro.md:§1-8`「\| 8 \| **构图三式**：正面/半侧面近距；三角形多人（三美人）；镜与后姿（姿見） \| 主体居中或轻偏；无强斜线；裁切为制式（肩胸）而非抓拍 \| `[研究]`（[R18][R17]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/kitagawa_utamaro.md:§1-9`「\| 9 \| **平面色域**：无投影、无渐变（除轻ぼかし）；色不掩线；墨线主导 \| 渐变带 ≤1% 短边；阴影面积 ≤2% \| `[归纳]`（据 [R16][R17] 图版归纳） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/kitagawa_utamaro.md:§1-10`「\| 10 \| **款印系统**：款「哥麿筆」「歌麿画」「相見 歌麿画」；自矜款「正銘歌麿」＋「自成一家」印；版元标记（蔦屋·上村等） \| 款/印位置与版元标记可查（如針仕事「上村」印） \| `[史料]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-43"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/kitagawa_utamaro.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/kitagawa_utamaro.md:§8.2 尾注:L197`「3. **背景规则**：背景为均质场（局部方差 ≤ 阈值）或云母纹理；背景道具 ≤2 件；投影/阴影面积 ≤2%；无透视消失点（收敛点 ≤1 且不在画内）。`[归纳]`」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-kitagawa_utamaro/mechanism_notes.md:§5`（7 条 counters，逐条回指 §8.2-1…§8.2-7） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-51"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 6ab681297be600d4（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-kitagawa_utamaro/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-kitagawa_utamaro/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **28 行**（§A5+§B7+§C10+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 7 行 = dossier §8.2 的 7 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
