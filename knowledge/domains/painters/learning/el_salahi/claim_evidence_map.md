<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-el_salahi；原正文 SHA-256 `1338a43b371c3e4dc3f4875341455574fa4d56e107053ae3ae7d6334d8d4a3d9`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-el_salahi — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-el_salahi/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 9420032116938278（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 f5aed8c8a8af5997（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/el_salahi.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `11e6f129f269006943bc71af2dc30fd73e6627dee5a72b1700bd4f04b2f7c1d9`；`§0`、`§1`、`§4`、`§8.2:L227-240`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [el_salahi.md](../../modules/el_salahi.md) sha256 `c5cc8b27d1e8e85f3d905f75a470054835fef8acf03cea8f861b2c0a4169a0ef`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [el_salahi.md](../../dossiers/_corpus/el_salahi.md) sha256 `bc6cc537460697c4cda77cbc51f30c6d285075600b934786ffbd1b791b15085a`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/el_salahi.md:L230` §8.2-1「\| 1 \| **字母骨架在场** \| ≥1 类可辨字母构件（alif 竖笔 / 圆环 / 点群）；笔画线宽 p90/p10 ≥ 2.5；连写段落 ≥1/3 画幅长 \| 形态检测（竖笔段/闭环/点簇）+ 笔画宽度统计 \|」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/el_salahi.md:L231` §8.2-2「\| 2 \| **索默色域** \| 色相簇 ≤6；平均饱和度 ≤45%；高纯色（S≥70%）面积 ≤10% \| 逐帧直方图 + 色相聚类 \|」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/el_salahi.md:L232` §8.2-3「\| 3 \| **有机生长/分块** \| 分块数 1–12；块间主笔势方向相关系数 ≥0.5（同源）或单幅呈「核→外」尺度梯度（近核笔画密度 ≥ 边缘 1.5 倍） \| 分块检测 + 主方向相关 + 密度梯度图 \|」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/el_salahi.md:L233` §8.2-4「\| 4 \| **面具/胚胎形象预算** \| 头形/面具锚点 0–5 个；单锚点面积 ≤8%；双眼成对出现（≥1 对） \| 形状检测 + 成对性检查 \|」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/el_salahi.md:L234` §8.2-5「\| 5 \| **黑白粒子-整体** \| 双色像素占比 ≥85%（黑白档）；粒子尺度方差大（p90/p10 ≥ 4）；缩略图（1/16）下读为单一整体形（连通域 ≤3） \| 二值化统计 + 多尺度连通域 \|」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/el_salahi.md:L235` §8.2-6「\| 6 \| **书写运动预算** \| 全片无叙事位移；若为动画，笔迹生长速度调制 ≤2%/s；帧间差 ≤1.5% \| 帧差图 + 生长曲线拟合 \|」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/el_salahi.md:L236` §8.2-7「\| 7 \| **基底显影** \| 折痕/braille/窗膜/拼接缝可见但 ≤15% 面积；≥1 条主笔沿痕迹走向（相关系数 ≥0.4） \| 线检测 + 痕迹掩膜相关 \|」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/el_salahi.md:L237` §8.2-8「\| 8 \| **越界检查（组合护栏）** \| 金箔 0；细密画书页框 0；高纯度互补对撞对 0；可读标语/整行文本 0；纯几何硬边网格 0 \| 按 §3.1 判据逐项清单核对 + OCR 扫描（仅计「可读句」） \|」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（12 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/el_salahi.md:§1-1`「\| 1 \| **字母骨架（letter-bone）** \| 画面结构由阿拉伯字母构件构成/演化：alif 竖笔、圆环（bowl）、点群（nuqta）；作者自述工作法="break down the b…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/el_salahi.md:§1-2`「\| 2 \| **面具/头形与双眼** \| 面具式头部、拉长头形、成对「离体之眼」（disembodied eyes）、头顶新月；Tate 馆方文本："heads of the figures reca…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/el_salahi.md:§1-3`「\| 3 \| **索默土色系（sombre earth palette）** \| 黑、白、焦赭、土黄为主；"colors of earth and skin colour shades"；同屏色相少、少…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/el_salahi.md:§1-4`「\| 4 \| **线为主角、书写性笔势** \| 线=一切之本（"all images can be reduced to lines"）；笔势带书写速度感；线宽变化大、连笔段落长 \| `[自述]`（[R…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/el_salahi.md:§1-5`「\| 5 \| **平涂浅空间** \| 无线性透视、无消失点；形体与图案互相咬合（"blurs the distinction between abstract form, pattern and fig…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/el_salahi.md:§1-6`「\| 6 \| **有机生长构图（nucleus → whole）** \| 从「核」生长、无草图先行；每片可独立装裱又组合成整体；多联屏（九联 *The Inevitable*；*Reborn Sound…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/el_salahi.md:§1-7`「\| 7 \| **正方形 / 竖长小画幅** \| 方画幅常见（T13979 2588×2600 mm；*No Shade but His Shade* 95×95 cm）；后期小纸片为竖长（*Priso…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/el_salahi.md:§1-8`「\| 8 \| **缝合与拼接的底材** \| *Reborn Sounds I* 的物理构造=damouriya 手织窄布三幅横拼 + 纵向裁切；缝合线/拼接痕可见 \| `[研究]`（[R4]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/el_salahi.md:§1-9`「\| 9 \| **黑白粒子-整体（1970s–90s 主导）** \| 中期约 17 年黑白阶段：粒子（笔画/小块）各自成幅又聚为整体；作者语 "the particle and the whole" \|…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/el_salahi.md:§1-10`「\| 10 \| **树 / 哈拉扎（haraz）母题（晚期）** \| 竖向线束成树/林；Tate："recurring vertical lines to convey woodlands or ind…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F11 | `dossiers/el_salahi.md:§1-11`「\| 11 \| **冥想式重复与微小尺度** \| 点、短笔、braille 印记式重复；药盒/信封上的小画（后经丝网放大）；"drawing is a kind of meditation" \| `[自述]`（[R33][R34]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F12 | `dossiers/el_salahi.md:§1-12`「\| 12 \| **文字残影（可读性受控）** \| 字母可辨度介于「完全不可读」与「可读标语」之间：局部可辨字根/词（*The Mosque* 内浮雕式安拉之名），整体不承载可读文本 \| `[研究]`（[R20]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-46"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/el_salahi.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/el_salahi.md:§8.2 尾注:L239`「> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；与 [style_card.md](../../../../../templates/style_card.md) 的填写规则对齐。」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-el_salahi/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-54"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 7927d7d5c56b665f（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-el_salahi/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-el_salahi/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **31 行**（§A5+§B8+§C12+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
