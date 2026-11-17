<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-manet；原正文 SHA-256 `fd028d82bc51ad2320867b055cb9f4aba18aae3a3b4e35ef0b5d88f08540aa3c`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-manet — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-manet/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 67fa82e56a3a8efb（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 0c837fc03c5e8d6a（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/manet.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `426f3d2e6febc8326ed07e50268eb3a3ead967da07a732a6616feebfc09ef53f`；`§0`、`§1`、`§4`、`§8.2:L242-253`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [manet.md](../../modules/manet.md) sha256 `486ec9e11e2cb9122be9a52efed72ba0b1865bdf31d882a51683d20d51147b99`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [manet.md](../../dossiers/_corpus/manet.md) sha256 `46fc8c8b0d0ceee73a123b3a3ef2938c346929032b8c39de5050d19f7c2b163a`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/manet.md:L243` §8.2-1「1. **中间调压缩规则**：直方图中带（V 0.40–0.65）面积 **≤25%**；亮/暗双峰可辨（峰间距 ≥0.25）；无宽渐变带（过渡带 ≤1% 短边）。自查：明度直方图 + 双峰检测。（依据：[R7]「con…」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/manet.md:L244` §8.2-2「2. **平面化空间规则**：背景梯度层 ≤2；消失点 ≤1（强档 0）；人物轮廓与背景明度差 ≥15%、边缘可描。自查：区域分割 + 消失点估计 + 边缘对比。（依据：[R2]「close to the picture…」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/manet.md:L245` §8.2-3「3. **黑色预算规则**：深色（V ≤0.2）面积 **15–40%**；黑区内部标准差 ≤0.06（平整，非细碎渐变）。自查：暗区面积 + 局部方差。（依据：[R14]「blacks and greys」；[R8]「…」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/manet.md:L246` §8.2-4「4. **色域与点缀规则**：主色族 ≤5（黑/白/灰/棕 + 1–2 家族）；高饱和（S ≥0.6）面积 **≤10%**、连通域 1–3。自查：色相聚类 + 饱和度直方图。（依据：[R2]「restrained co…」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/manet.md:L247` §8.2-5「5. **笔触可见性规则**：可见笔触覆盖 **≥60%**；色层 ≤3（alla prima，无多层罩染）；笔触方向族 2–5 个。自查：边缘方向场 + 梯度带。（依据：[R23]；[R24]「abridged」）」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/manet.md:L248` §8.2-6「6. **正面光规则**：面部阴影面积 **≤15%**；无单侧硬阴影（亮暗分界无强方向性）；允许 1–2 px 湿接湿融合带。自查：面部区域明度分布。（依据：[R15]「peinture claire」）」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/manet.md:L249` §8.2-7「7. **裁切与装置规则**：主体被画框裁切 **≥1 处**；强对角线 ≥1；对称装置（镜面/栏杆/舞台框）≤1 且承担构图任务。自查：边缘相交检测 + 线检测。（依据：[R4] 日本版画；[R30] 镜面）」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/manet.md:L250` §8.2-8「8. **题材与视线规则**：当代生活题材（可点检道具 ≥2：咖啡馆/酒杯/船/栏杆/铁路）；≥1 人物直视观众（或明确的「观察者」视点）。自查：道具检测 + 视线估计。（依据：[R1] 现代生活；[R6]「défie…」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（10 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/manet.md:§1-1`「\| 1 \| **取消中间调（亮暗直接并置）**：大块亮/暗直接咬合，过渡带极窄——「没有半调子」；人物像被硬光照亮 \| 中间调带（V 0.40–0.65）面积 ≤25%；亮暗过渡带 ≤1% 短边 \|…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/manet.md:§1-2`「\| 2 \| **平面化空间**：背景不后退、贴住人物——「人物向前推到画面平面」；透视被削弱/忽略 \| 消失点 ≤1（强档 0）；背景梯度层 ≤2；人物轮廓与背景明度差 ≥15% \| `[研究]`（[…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/manet.md:§1-3`「\| 3 \| **黑是主色**：黑用于**形体与面积**（西班牙装束、女仆、礼服、吧台女黑裙），不是阴影；「被印象派禁用的黑与灰」照用 \| 深色（V ≤0.2）面积 15–40%；黑区内部标准差 ≤0.…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/manet.md:§1-4`「\| 4 \| **色域收窄 + 少量饱和点**：黑/白/灰/棕为骨架，纯色只作 1–3 处强调（斗牛服的红、吧台的橙、花的粉） \| 高饱和（S ≥0.6）面积 ≤10%、连通域 1–3 \| `[研究]`…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/manet.md:§1-5`「\| 5 \| **色斑（tache）组织**：对象被读作「一块色斑」——「一头靠墙的头不过是一块或白或灰的斑」 \| 笔触/色斑连通域密度高；细节被省略（可辨细节 ≤2 类/对象） \| `[史料]`（[R…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/manet.md:§1-6`「\| 6 \| **干脆、可见、一次性的笔触（alla prima）**：宽笔、湿接湿、几乎不罩染；黑部是「干净的大平涂（aplats）」，白部堆厚 \| 笔触覆盖 ≥60%；色层 ≤3；黑区平整 \| `[…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/manet.md:§1-7`「\| 7 \| **正面光 / 亮色画法（peinture claire）**：面部被正面光「洗亮」，阴影几近取消；湿接湿处边缘微微化开 \| 面部阴影面积 ≤15%；无单侧强阴影；融合带 1–2 px \|…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/manet.md:§1-8`「\| 8 \| **日本版画式裁切与构图**：船被切、人物出画、非对称；「大块色面 + 强对角线」 \| 主体被画框裁切 ≥1 处；强对角线 ≥1；对称装置（镜/栏杆）≤1 \| `[研究]`（[R4]「br…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/manet.md:§1-9`「\| 9 \| **直视观众的现代人物**：正面/直视——目光是「挑战」不是「被看」；题材全为当下（草地、阳台、咖啡馆、酒吧、铁路） \| 直视观众人物 ≥1（作品层面）；服饰道具为当代 \| `[研究]`（…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/manet.md:§1-10`「\| 10 \| **浅背景/中性背景**：背景常为无叙事的灰/棕/暗面（吹笛少年灰底、西班牙歌手棕底、阳台暗室） \| 背景可辨细节 ≤2 类；背景无叙事符号（镜面装置除外） \| `[史料]`（[R2]「…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-44"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/manet.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/manet.md:§8.2 尾注:L252`「> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–8 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-manet/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-52"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 fcfac8a2af0d7a4a（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-manet/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-manet/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **29 行**（§A5+§B8+§C10+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
