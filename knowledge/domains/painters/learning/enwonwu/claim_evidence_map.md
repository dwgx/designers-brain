<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-enwonwu；原正文 SHA-256 `21f8b6b3737b9a4928f9875c813ec9a7f974744f804f746b4c25309f3dfa2a5c`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-enwonwu — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-enwonwu/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 b083aa5ae98c3016（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 f4298d78f2f7ffb1（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/enwonwu.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `7391423e3286333098499dc28dc348eed02429fa5f5ae97918da1fe29946fbdb`；`§0`、`§1`、`§4`、`§8.2:L223-234`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [enwonwu.md](../../modules/enwonwu.md) sha256 `c2fc7876e29c87074d04d20155618940d8d6afad3c8d6bf7db904de9790bb209`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [enwonwu.md](../../dossiers/_corpus/enwonwu.md) sha256 `00cdc569ad7ae5b3968a512358f5ac92d09238795fa546b96fa35e544b366772`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/enwonwu.md:L224` §8.2-1「1. **雕塑性剪影规则**：主体外轮廓完整（无断裂）；缩至 256px 主体可辨；主体内部明度层 ≤4（块面化，非连续渐变）。自查：轮廓连通域 + 缩略图目检 + 明度直方图。（依据：[R19]「described h…」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/enwonwu.md:L225` §8.2-2「2. **暖土色域规则**：暖色（红/橙/黄/赭/棕系）面积 **≥50%**；冷色 **≤25%**；高饱和（S≥0.5）面积 **8–25%** 且连通域 ≤4 处（点状点缀）。自查：色相直方图 + 连通域计数。（依…」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/enwonwu.md:L226` §8.2-3「3. **均匀光规则**：面部明暗对比 **≤2.5:1**；硬边阴影 0 处（阴影边界梯度 >15%/px 者 = 0）；暗部明度 ≥纯黑+10%。自查：面部区域对比度 + 阴影边界梯度。（依据：[R14] 描述与作品…」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/enwonwu.md:L227` §8.2-4「4. **图像志规则**：仪式/舞蹈档 ≥1 个可辨认的假面/舞蹈/神祇元素；肖像档 ≥1 件民族服饰/头巾元素；符号元素同框 **≤3 类**（防奇观化堆叠）。自查：元素分类计数。（依据：[R13]「coded res…」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/enwonwu.md:L228` §8.2-5「5. **运动/舞蹈规则**：≥2 组肢体重叠或斜向动作线；全片 **0 帧运动模糊**（运动以姿态表达）；躯干/肢体轴向偏垂直 ≥10° 者 ≥2 处。自查：姿态估计 + 运动模糊检测。（依据：[R20]「layeri…」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/enwonwu.md:L229` §8.2-6「6. **肖像视角规则**：3/4 或正面；长颈（**颈长/头长 ≥0.4**）；视线平静（眉眼口形变 ≤15% 中性面）**或**直接平视观者（Children of Biafra 档）——二选一，不得混用。自查：视角…」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/enwonwu.md:L230` §8.2-7「7. **织物/图案规则**：头巾/织物图案区 **5–30%** 面积；图案为块面/条纹/几何（gele 式）；无细密满铺。自查：图案区面积 + 纹理尺度。（依据：[R3]「richly-patterned head…」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/enwonwu.md:L231` §8.2-8「8. **浅空间/背景规则**：背景层数 **≤2**；收敛线 ≤1 组；肖像档背景无叙事物（墙/暗底/平色）。自查：区域分割 + 消失点估计。（依据：[R3]「背景被省略」类著录；[R7]）」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（10 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/enwonwu.md:§1-1`「\| 1 \| **雕塑性体量（「雕塑家的画」）**：形体以块面/体量成立，人物如雕像般「立起」；剪影清晰、内部平实 \| 主要人物外轮廓完整、缩至 256px 可辨；单形体内部明度层 ≤4；「他始终把自己…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/enwonwu.md:§1-2`「\| 2 \| **假面/舞蹈/神祇图像志**：mmuo（假面）、agbogho mmuo、舞蹈、Anyanwu/Sango 神祇——文化-精神主体，非装饰 \| 仪式档画面 ≥1 个可辨认的假面/舞蹈/神…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/enwonwu.md:§1-3`「\| 3 \| **舞蹈运动与肢体层叠**：以重叠肢体、旋动弧线捕捉舞蹈；「layering of limbs」为馆方/策展定式 \| ≥2 组肢体重叠或斜向动作线；全片 0 帧运动模糊（运动以姿态表达）…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/enwonwu.md:§1-4`「\| 4 \| **暖土色域＋点状高饱和**：赭/棕/红/金为底；高饱和集中在小面积（头巾/珠饰/衣布）作重音 \| 暖色面积 ≥50%；冷色 ≤25%；高饱和（S≥0.5）面积 8–25% 且连通域 ≤4…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/enwonwu.md:§1-5`「\| 5 \| **尊严的肖像**：3/4 或正面、长颈、姿态挺直；平静或平视的凝视；不做心理戏剧 \| 颈长/头长 ≥0.4；眉眼口形变 ≤15% 中性面；或直接平视观者（Children of Biaf…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/enwonwu.md:§1-6`「\| 6 \| **均匀漫射光**：光服务于形体与图像志的可读；无硬光开关、无戏剧性明暗切割 \| 面部明暗对比 ≤2.5:1；硬边阴影 0 处；暗部明度 ≥纯黑+10% \| `[归纳]`（对照作品；与卡拉…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/enwonwu.md:§1-7`「\| 7 \| **浅空间/背景简化**：肖像背景＝平色/暖墙/暗底；风景＝色带与云层；无叙事杂物 \| 背景层数 ≤2；收敛线 ≤1 组；肖像档背景无叙事物 \| `[归纳]`（对照图库；[R3]「背景被省…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/enwonwu.md:§1-8`「\| 8 \| **笔触：面部收敛、衣饰放开**：面部细致（"deft brushwork"），织物「透明化处理」（"diaphanous treatment"）；风暴档转为「粗厉的大笔触」（"bold,…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/enwonwu.md:§1-9`「\| 9 \| **拉长与「上升」的形体**（雕塑侧）：如树生长的拉长曲线——「把元素拉长如音乐的主音」；顶天立地的上升感 \| 长宽比 ≥4:1 的立柱式形体；曲线为主轴（非直线）；基座连接如「防止升空」…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/enwonwu.md:§1-10`「\| 10 \| **象征的克制（非宣传化）**：象征由姿态、服饰、图像志承载；不堆叠符号、不做口号 \| 象征性元素 ≤3 类；无文字/标语；情绪中性偏庄严 \| `[研究]`（[R13]「non-prop…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-44"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/enwonwu.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/enwonwu.md:§8.2 尾注:L233`「> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–8 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-enwonwu/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-52"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 78373d51fe31fb05（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-enwonwu/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-enwonwu/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **29 行**（§A5+§B8+§C10+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
