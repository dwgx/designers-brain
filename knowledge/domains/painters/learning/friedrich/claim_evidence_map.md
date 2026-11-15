<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-friedrich；原正文 SHA-256 `ffb777c68e91d73bdbc5cccc1d73a7bb56b888971afc646ba43f05055f217fea`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-friedrich — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-friedrich/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 a286ae00a272c7a9（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 3cb5263221d67ac9（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/friedrich.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `a8c7e4b427da4109822efdc60faa8c3320e0edb5558137e90b7daf8d833e9149`；`§0`、`§1`、`§4`、`§8.2:L188-199`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [friedrich.md](../../modules/friedrich.md) sha256 `5a26ced20d6fc90af902a0515a2f364276c292af40cc98499d569578232e8af7`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [friedrich.md](../../dossiers/_corpus/friedrich.md) sha256 `00d1f54d00e0948600f11b22927fa243567615d6026a15ccaa9ca8c304b0167f`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/friedrich.md:L189` §8.2-1「1. **Rückenfigur 规则**：焦点人形**背向**（人脸关键点命中 ≤1 组、五官不可辨）；位于中轴 ±10% 画宽；多人时 ≤3 人且同一朝向。自查：人脸关键点检测 + 实例分割 + 中轴度量。（依据：[…」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/friedrich.md:L190` §8.2-2「2. **冻结规则**：视频帧间全局光流 Δ ≤0.5%/帧（事件外）；无运动模糊核；仅允许雾带/水面的极慢渐变（局部光流 ≤2% 短边/秒）。自查：光流场 + 模糊核检测。（与 C-09 运动预算对齐：弗里德里希站「冻…」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/friedrich.md:L191` §8.2-3「3. **层带规则**：检出 **≥3 条水平带边界**（倾角 ≤3°）；天空带面积占比 ≥40%；单带内边缘密度 ≤全帧均值的 0.8 倍。自查：边缘方向直方图 + 水平带分割。（依据：[R7]「陆/海/天三元素」）」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/friedrich.md:L192` §8.2-4「4. **无透视轴规则**：单消失点引导线 = 0；山棱/岸线走向向中轴收束（左右向心斜线对 ≥1 组）。自查：Hough 直线 + 消失点估计。（依据：[R5]「Mittelsenkrechte 与两侧坠落山棱」）」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/friedrich.md:L193` §8.2-5「5. **逆光剪影规则**：人形/前景剪影的明度中位 < 全帧明度中位 − 0.15；光源质心位于天空带（上 1/3）；**无画内单点光源**（高亮连通域 ≥2 或成带状）。自查：亮度质心 + 剪影分割。（依据：[R5]…」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/friedrich.md:L194` §8.2-6「6. **冷调低饱和规则**：全帧中位饱和 ≤0.35；蓝灰（H 180–240°）/ 褐（20–45°）/ 赭金（35–55°）三族合计面积 ≥80%；饱和 ≥0.85 的区块（≥3% 面积）数量 = 0。自查：HSV…」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/friedrich.md:L195` §8.2-7「7. **象征点检规则**：≥1 个象征元素在场（十字/哥特废墟/枯橡树/墓/锚 五类可点检）；象征物面积 ≤5% 画布、且位于中轴 ±15% 或天际线带内。自查：对象检测 + 位置度量。（依据：[R2] 象征清单；[R…」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/friedrich.md:L196` §8.2-8「8. **软光与雾面规则（无硬阴影 + 点彩）**：阴影边界梯度带宽 ≥2% 短边（软过渡）；暗部 V ≥0.05（**不出现纯黑大块**）；镜面高光（V≥0.95 且面积 >1%）数量 = 0；雾/雪区高频能量集中于…」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（10 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/friedrich.md:§1-1`「\| 1 \| **Rückenfigur（背影人物）**：人物从背后看、面对景深，观者被邀请「站到他身后」；是「凝视」的装置而非叙事角色——[R5] 原文：「Es ist daher vor allem…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/friedrich.md:§1-2`「\| 2 \| **静默与静止（无动作）**：人物「无动作地与自然对话」；有人形容他们「刚刚进入画面，停留良久，然后再走下去」——画面时间被拉长为「停留」 \| 人物姿态静止（站/坐/倚）；无叙事性动作与交…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/friedrich.md:§1-3`「\| 3 \| **层带式构图（水平分层）**：画面「以清晰的简洁水平地分为陆、海、天三个元素」；多数构图为 2–4 条水平带（前景条带 + 水/山带 + 天空带），带内细节稀薄 \| ≥3 条水平带、分界…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/friedrich.md:§1-4`「\| 4 \| **空间阻隔 + 剪影对撞**：前景被「空间屏障」（墙、门、坡沿、岩石）与远景隔开；前景以**深色剪影平面**与背景对撞；《雾海漫游者》甚至**没有通向纵深的透视轴**——山只是左右向中央…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/friedrich.md:§1-5`「\| 5 \| **人物—尺度比（渺小化）**：人物被缩小到「孤独圆圈里的孤独中心」；尺度被用来把观者的凝视「导向形而上的维度」（Murray 语） \| 人形高度多数 ≤ 画面高度 1/6；人形与地平线/…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/friedrich.md:§1-6`「\| 6 \| **对称与中轴几何**：以对称、重复、平行位移组织画面；三角形/对角线/双曲线被明确使用；中轴常由人物或建筑锁定；黄金比分割（注：他生前不知道这个术语——术语 1850 年才出现） \| 主…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/friedrich.md:§1-7`「\| 7 \| **逆光剪影与暮色光**：光从天空来（落日/月/晨光），人物近黑；「晚霞的微光……柔和地照向大地」（泰申祭坛画自述）；暮色与黎明是他最常用的两个时刻 \| 光源位于天空带；人形明度 < 背景…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/friedrich.md:§1-8`「\| 8 \| **冷调低饱和色谱**：色域收窄——蓝灰、褐、赭石、淡金为主；大气效果靠「平滑渐变的调子」而非色彩；雪景以「单一基本音」（Beenken）概括 \| 全帧中位饱和低；无大块纯黑（暗部带蓝/褐…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/friedrich.md:§1-9`「\| 9 \| **象征装置库**：十字架（高处、逆光）、哥特废墟/远教堂、枯橡树与树桩、墓与墓地门、锚；「十字与放晴的天空许诺永生；细月暗示希望」 \| ≥1 个象征元素在场；十字/废墟/枯树/墓/锚五类…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/friedrich.md:§1-10`「\| 10 \| **雾、海、雪的气象包络**：雾/雪/海不是背景而是**主体**——「风景被雾包裹时，会显得更宏大、更庄严」（自述）；冬景「无人踏足」（Beenken 语） \| 大气现象占画面 ≥1/3…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-44"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/friedrich.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/friedrich.md:§8.2 尾注:L198`「> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–5 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-friedrich/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-52"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 75a5d06d37dd7b7b（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-friedrich/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-friedrich/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **29 行**（§A5+§B8+§C10+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
