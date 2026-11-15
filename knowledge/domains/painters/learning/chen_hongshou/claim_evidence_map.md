<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-chen_hongshou；原正文 SHA-256 `e143a6c1cf1aeee67d25a5d5ae95ccb603d236c6957f2c2f7e413d4150b48c20`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-chen_hongshou — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-chen_hongshou/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 ca937b0e9b318ef2（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 e1ae260dabba32ca（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/chen_hongshou.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `629cbf7e5800daa1a8170bc47e512c76dc4d4ed6c2f1cafb94f0daef82ae48ea`；`§0`、`§1`、`§4`、`§8.2:L203-211`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [chen_hongshou.md](../../modules/chen_hongshou.md) sha256 `4084ee9e7745b55eadd4aa00eae5d4ae5cf526622ceaa0b443868f3de54da4d6`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [chen_hongshou.md](../../dossiers/_corpus/chen_hongshou.md) sha256 `158c813a4d97ed97a1036a2a01344a70aa4fccbee51e9327750fa01dca7d32e1`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 7 条规则逐条回源（7 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/chen_hongshou.md:L204` §8.2-1「1. **变形比例**：主要人物头长（下颌至头顶）÷ 全身长 ≥ 1/6（强档 ≥1/5）；头宽 ÷ 肩宽 ≥ 0.75；面轮廓的方直段（曲率 ≤ 阈值）占周长 ≥40%。`[归纳]`」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/chen_hongshou.md:L205` §8.2-2「2. **一笔连绵的线**：衣纹主轮廓线中，单笔连续长度 ≥60px（1000px 参考帧）的笔画占比 ≥50%；单笔中段线宽变化 ≤1.5×（「游丝档」）；「方折档」允许线宽恒定但转折角 ≥45° 的折点 ≥2 处/1…」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/chen_hongshou.md:L206` §8.2-3「3. **无排线**：全帧交叉排线（两组以上线方向夹角 ≥15° 且密度 >2 线/10px）面积 ≤1%；线密度与局部明度的单调映射不成立（\|r\| ≤0.4）；单色实心填充面积 ≤10%。`[归纳]`」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/chen_hongshou.md:L207` §8.2-4「4. **装饰纹样密度**：可辨纹样单元（松针组、云纹、器物纹、衣纹图案）≥1 单元/1000px²（强档）；器物/陈设元素 1–8 件/画面；纹样重复率（同类单元 ≥2 次）≥50%。`[归纳]`」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/chen_hongshou.md:L208` §8.2-5「5. **背景压缩**：人物画背景留白（高亮均质区）≥35%；透视线收敛点数量 ≤1 且不在画内；平面道具（屏风/石/案）承担 ≥1 个空间分层。`[归纳]`」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/chen_hongshou.md:L209` §8.2-6「6. **设色古艳**：彩色像素（饱和度 >15%）≤45%；色相 ≤4 族（石青/石绿/朱/赭黄）；单块饱和度 ≥70% 的连通域面积 ≤3%；线迹穿过色块的可见度 ≥60%。`[归纳]`」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/chen_hongshou.md:L210` §8.2-7「7. **版画字段（插图/叶子档）**：题名/题赞文字区（文字列或框）存在且 ≤8% 画面；纯白描（无灰阶填充带）；刻工署名（角落小字）1 处；动画时人物位移 ≤1% 画幅/秒（酒牌为静帧语义，禁叙事推拉）。`[归纳]`」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-28"></a>
## §C §1 视觉指纹（10 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/chen_hongshou.md:§1-1`「\| 1 \| **变形比例（头大身短）**：人物头部偏大、体形肥短，「与身体相比显然不合比例」，面型多趋方正 \| 主要人物头长÷全身长 ≥1/6（强档 ≥1/5）；头宽÷肩宽 ≥0.75 \| `[研究]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/chen_hongshou.md:§1-2`「\| 2 \| **壮年版画的方折瘦硬线**：《水浒叶子》「多用方折直拐的瘦硬线条」 \| 单线转折角 ≥45° 的折点密度高；线质挺硬、少弧线 \| `[研究]`（[R18]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/chen_hongshou.md:§1-3`「\| 3 \| **晚年版画的高古游丝描**：《博古叶子》「多用圆润纤劲的高古游丝描，舒缓静谧，张弛有致」「宽袍大袖的线条虽长，皆一笔勾出，不另起笔，紧劲连绵，如行云流水」 \| 长线单笔连续、无中途顿点；…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/chen_hongshou.md:§1-4`「\| 4 \| **装饰性图案**：「松、石造型规律，颇富图案装饰趣味」（台北故宫）；纹样化图案大量运用 \| 松针成组、石形几何化；纹样单元可辨、重复出现 \| `[史料]`+`[研究]`（[R11][R2…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/chen_hongshou.md:§1-5`「\| 5 \| **古器物陈设入画**：「尤其喜欢用古器物作为画面的构成部分」；汉瓦秦铜之设「其器具得五十二」 \| 器物（瓶罍、尊卤、几案、屏风）1–8 件/图；器物有考古依据 \| `[研究]`（[R18…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/chen_hongshou.md:§1-6`「\| 6 \| **「高古奇骇」的面容**：面孔方正、五官紧凑；仕女细目、高士奇骇；「铁线」细劲控制 \| 面部线为细匀墨线；表情克制（仪式感、静穆） \| `[研究]`（[R12][R18]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/chen_hongshou.md:§1-7`「\| 7 \| **背景压缩/无背景**：人物画常置人物于空白或极简道具之间；《九歌图》卷「no background setting」 \| 背景留白 ≥35%；无透视消失点；屏风/器物为平面道具 \| `…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/chen_hongshou.md:§1-8`「\| 8 \| **设色古艳**：矿物色（石青石绿、朱、赭）「brilliant coloring with mineral pigments」，色不掩线；有时以石绿石青画脸 \| 彩色像素 ≤45%；色相…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/chen_hongshou.md:§1-9`「\| 9 \| **线是骨架（白描性）**：绘画与版画皆以线立骨，「一笔勾出」；版画稿为纯白描 \| 无排线/无渐变填充；线覆盖高、灰阶少 \| `[归纳]`（据 [R12][R18] 图版与馆方著录归纳）…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/chen_hongshou.md:§1-10`「\| 10 \| **款印系统**：款「洪绶」「老莲」「溪山老莲洪绶」「老迟/悔迟」；晚年版画刻「徽州黄君蒨刻」类刻工款 \| 本幅款印位置与刻工署名可查（如西厢「武林項南洲刊」） \| `[史料]`（[R1…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-43"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/chen_hongshou.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/chen_hongshou.md:§8.2 尾注:L210`「1. **变形比例**：主要人物头长（下颌至头顶）÷ 全身长 ≥ 1/6（强档 ≥1/5）；头宽 ÷ 肩宽 ≥ 0.75；面轮廓的方直段（曲率 ≤ 阈值）占周长 ≥40%。`[归纳]`」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-chen_hongshou/mechanism_notes.md:§5`（7 条 counters，逐条回指 §8.2-1…§8.2-7） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-51"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 3ce89f86ccd9bebd（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-chen_hongshou/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-chen_hongshou/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **28 行**（§A5+§B7+§C10+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 7 行 = dossier §8.2 的 7 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
