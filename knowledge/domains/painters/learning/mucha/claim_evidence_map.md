<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-mucha；原正文 SHA-256 `d0d66b42220cbe00daaf8f86ea9d2729f7d400f9839e874a532d027153ad92cf`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-mucha — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-mucha/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 7d288703bd81bef9（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 41cd14d0389530aa（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/mucha.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `3ba421803ed757f22e1766d0c64632723e1c3a33f07eb4dbf14133bd22aa3314`；`§0`、`§1`、`§4`、`§8.2:L228-239`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [mucha.md](../../modules/mucha.md) sha256 `622734acc3de2d55df98214674d1f2c49d30ebd9c172eba0fe593f831ee5118a`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [mucha.md](../../dossiers/_corpus/mucha.md) sha256 `40bfbe58f377597e0fc9dd3b453288180e9c2efc01914a578b4d8d7a91312315`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/mucha.md:L229` §8.2-1「1. **曲线族一致性**：全帧主要轮廓的曲率连续（无折角）；发丝/衣褶/花茎的线宽族 ≤3 档；直线段仅允许出现在版面分隔/标题基线上，占比 ≤5%。（依据 §1-4）」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/mucha.md:L230` §8.2-2「2. **光环规则**：主角头部后方存在拱形/环形装饰；环中心与头部包围盒中心距离 ≤ 头宽 50%；环线与面部区域不重叠（聚焦而非遮挡）。」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/mucha.md:L231` §8.2-3「3. **近真人静止度**：主体人物高度 ≥ 画面高 60%（强档 ≥70%）；帧间姿态位移（若有动画）≤ 2% 画面高——「静止」是身份特征。」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/mucha.md:L232` §8.2-4「4. **色彩预算**：饱和色（S ≥ 0.6）面积 ≤ 15%；主色相 ≤ 5 个；无连续渐变（渐变面积 ≤ 5%，纸张/印刷噪点除外）。（依据 8 色印刷口径）」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/mucha.md:L233` §8.2-5「5. **纹样生长规则**：花叶母题 ≥3 处，且每处纹样的主轴方向与其「附着对象」（发/衣/框）的切线夹角 ≤ 30°——纹样沿曲线生长、非贴片。」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/mucha.md:L234` §8.2-6「6. **字画一体（海报档）**：排版文字 ≥1 区；字体为手绘装饰体（笔画曲率与画面曲线同族）；文字区与图像共用边框或纹样边界；无文字档（装饰板）则本规则跳过、检查 P6 边框完整度。」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/mucha.md:L235` §8.2-7「7. **边框完整度**：装饰板/海报档存在闭合边框（或上下装饰带 ≥2 段）；边框纹样与画内纹样同族（同一母题库）。」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/mucha.md:L236` §8.2-8「8. **越界警报（组合用）**：帧内出现金属镜面/箔块 → 越界克里姆特域；出现网格单元填充 → 越界若冲域；出现「无文字、无曲线骨架」的纯平涂图案 → 越界马蒂斯域。自查：材质高光检测 + 网格周期检测 + 文字检测…」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（10 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/mucha.md:§1-1`「\| 1 \| **光环/拱形背景**：人物头后一道（彩虹形）拱环，把视线聚到面部——《Gismonda》起成为其海报固定特征 \| 头后拱形/环形装饰 ≥1；环线框住面部 \| `[史料]` [R2]（"t…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/mucha.md:§1-2`「\| 2 \| **长窄画幅 + 近真人尺寸 + 静止端庄**：《Gismonda》216 × 74.2 cm（≈2.9:1）；人物几乎等身、静止——「为海报设计引入了尊严与克制」 \| 宽高比 ≥1:2.…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/mucha.md:§1-3`「\| 3 \| **理想化女性主角**：广告与装饰板几乎全部以「华美场景中的美丽女性」为主角，头发呈阿拉伯式曲线充满画面 \| 主角=女性；发丝覆盖面积 ≥10% 画面；无写实肖像特征 \| `[研究]` […」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/mucha.md:§1-4`「\| 4 \| **连续曲线系统（whiplash / arabesque）**：发丝、衣褶、植物茎叶全用连续 S 形曲线；线与线同族，画面无硬折角 \| 主要轮廓曲率连续（无折角）；发丝呈带状流动；直线仅…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/mucha.md:§1-5`「\| 5 \| **自然纹样编织**：花（百合、鸢尾、玫瑰）、叶、藤蔓作为背景/边框/发饰编织为图案层；纹样与人物同权 \| 可识别花叶母题 ≥3 处；纹样沿曲线生长（非贴片） \| `[研究]` [R6][…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/mucha.md:§1-6`「\| 6 \| **平涂 + 淡彩（pastel）**：石版印刷的平涂色块 + 柔和淡彩；色相少而整（暖粉、青绿、金褐、灰蓝） \| 色阶数少（套色 ≤8 档）；无写实环境色/连续渐变 \| `[史料]` […」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/mucha.md:§1-7`「\| 7 \| **字画一体**：标题/广告文字是版面的构成组件——手绘装饰字体，与图像同构、共用边框；早年杂志封面即显「对书法与字体设计的创新处理」 \| 排版文字 ≥1 区；字体笔画含曲线装饰；文字与图…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/mucha.md:§1-8`「\| 8 \| **边框与装饰框系统**：画面外缘常设装饰边框（花环、几何框、《时代》系列的「哥特窗式」框）；无文字的装饰板以边框完成「作品化」 \| 完整闭合边框 ≥1 圈；框内纹样与画内纹样同族 \| `…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/mucha.md:§1-9`「\| 9 \| **构图几何：圆/拱/菱形底座（Q formula）**：坐姿人物嵌入圆形母题、布幔垂尾；或人物立于拱形平台 \| 圆/拱几何母题框住主体 ≥1；对称轴明确 \| `[研究]` [R5]（"a…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/mucha.md:§1-10`「\| 10 \| **平面装饰空间**：以背景纹样/光环代替写实纵深；主体如舞台浮雕，空间由色块与纹样层叠而成 \| 无消失点、无投影；深度仅靠遮挡与色层 \| `[归纳]`（依据 [R2][R3][R8]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-44"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/mucha.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/mucha.md:§8.2 尾注:L238`「> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–3/5–7 条与 §1/§4 同轴，组合实验时以本节自查表为准。」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-mucha/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-52"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 08f550a27048c09e（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-mucha/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-mucha/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **29 行**（§A5+§B8+§C10+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
