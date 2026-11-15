<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-holbein；原正文 SHA-256 `32e9f4f017764bcaeda6c008cd8af008853498ce70c028e0f38a7c0225e11e31`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-holbein — 学习路径（A-30 §8.1 / Lane B 形状）

> **本文件全部为建议练习（suggested practice）**，不是「已证实学习收益」。截至本轮，所有 §4 六参数档位与 §8.2 八条规则阈值均为本项目 `[归纳]`、**未对荷尔拜因原作做像素测量**（dossier §8.2 末注 L216 / §10-6 L270），也没有任何 human review / 真人学习成效评价（01-AUDIT.md §8.1 L273）。不得把本文件写成「已验证的教学法」或「荷尔拜因本人的方法」。
>
> **证据底本**：内部证据 c4717bb05ac27410（未公开；来源记录由维护者保留）（**ACCEPTED**：`receipt.json` status=accepted、review=accepted；`review-evidence.md` verdict accepted / 0 blocking / 0 non-blocking；`review-gate-receipt.json` verdict accepted）。本 shard 沿用其 `文件:节:行号` 定位纪律与 79 claim-units 分母，**不重审、不改 repo、不复制 AUDIT 产物**。基线 commit `f008952365a77e140cbda3f3959d43ef000f9a22`（repo READ-ONLY）。
> **证据级别照录** dossier §0 / AUDIT claim map 卷首 L6：`[自述]`=本人写下（画内文字/遗嘱）｜`[史料]`=同时代记录/档案/馆藏｜`[研究]`=艺术史家/博物馆/学术资料｜`[归纳]`=本项目从作品归纳的操作规则｜`[推测]`=低置信。
> **本次交办强调**：① **北方文艺复兴肖像精工 + 织物质感机制**（物证级细节 + 净面材质分化）；② **X-AGES 双说**（馆方英译 28/24 vs 25/29）作为 conflict 携带、铭文拉丁原文 29/25 优先、报告不修；③ **Windsor drawings + 遗嘱逐字证据**（语料 Q1 自身 locator drift，L13601–13614 实为 "THE WINDSOR DRAWINGS" 页文本、遗嘱逐字在 L17540–17565）；④ **13 rights rows = 12 PD + 1 CC0**。

---

<a id="db-source-line-11"></a>
## §1 前置知识（先具备什么，再开练）

1. **先接受分工条款（写死，`[归纳]` 口径级）**：荷尔拜因 = **材质的物证（油画净面、无排线）＋ 外表静默（信息照明）**；**vs 丢勒**＝「线的密度 / 版画规则化」 vs 「材质的物证 / 罩染净面」（dossier §3.1 L76-82；第一写死条款）；**vs 伦勃朗**＝「客观物证 / 信息光 / 情绪画外」 vs 「心理内心光 / 情感照明 / 情绪画内」（dossier §3.1 L83-89；第二写死条款）。两条主分工轴不得混用；B1/B2 已被自审 WEAKENED 并补「≥2 轴联合成立 / 心理是否被画内光承载」边界注（dossier 自审 B L435-436）。判分口径见 §4 用法（dossier L102）：出现排线 → 越界丢勒；硬切光斑 → 越界卡拉瓦乔/伦勃朗；可见厚涂笔触 → 越界伦勃朗/梵高。**这是本卡组合时的冲突轴。**
2. **先分清三个「层」**（02-EXECUTION-PLAN.md L64 学习顺序：观察对象→创作决策→机制→参数→一次练习→反例→自检）：
   - **档案事实层**（`[史料]/[研究]`）：作品、年代、馆藏、生平（dossier §0 / §7 / §11）、26 条 corpus 引文（[holbein.md](../../dossiers/_corpus/holbein.md)，AUDIT §E 逐条核语言/翻译/类型）。
   - **自述层**（`[自述]`，**极薄**）：荷尔拜因**几乎没有传世书信与日记**（dossier 卷首 L9），`[自述]` 仅以**画内文字（签名/题铭）与 1543 遗嘱**为主。Q1–Q10 = self-written 10 条（corpus §一），其余为 contemporary record 9 / reported speech 4 / 身后 3 = 26（AUDIT §E 分型）。**自述不规定任何数值阈值、决策顺序或「物证级细节」这个机制词。**
   - **操作化规则层**（`[归纳]`）：§4 六参数（P1–P6，dossier L95-100）、§8.2 八条可判定规则（dossier L207-214）、§8.1 prompt / §8.2 自查。档位划分与阈值本身为 `[归纳]`、未做像素实测（dossier §10-6 L270）。
3. **最小工具/概念**：方向滤波器 + 频域能量统计（净面）、梯度剖面抽样（边缘）、高光形状分类 + 纹理统计（材质分化）、OCR + 接触点检测（物证清单）、文字框高度 + 载体分类（铭文）、亮度质心 + 阶跃检测（软光）、Hough 直线 + 对称性检验（几何）、仿射校正 + IoU（变形装置）。这些是 §8.2「自查方法」列要求的量，**不是史实**。
4. **先读冲突表**：组合前读 [conflicts.md](../../../../cross/conflicts.md) §1/§2/§3 与卡「冲突注记」。**本次 reality**：`grep -niE 'Holbein|荷尔拜因' conflicts.md` = **0 命中**（AUDIT §9 / X-CONFLICTS）→ holbein **无专属 C-row**；模块卡 L85 / 档案 §3.1 L89 仅以「预检指针」引用通用 **C-01（L55，硬阴影）/ C-05（L109，笔触可见度）/ C-12（L203，色相预算）**；§4 near-miss 11 对中无 holbein 近邻对。记为事实，非缺陷。注意 C-01/C-05/C-12 的 `(dossier.md L<行号>)` 行号普遍 stale（AUDIT §G 11 处，报告不修）。
5. **accepted basis 边界**：AUDIT 6 次公开抓取（ngl_ambassadors.html / hervey1900.txt / wiki_holbein3.html / ngl_erasmus.html / chamberlain1.txt / chamberlain2_raw.txt，sha 见 coverage-manifest.json）是**已接受的上游文本佐证**。本路径只把它们当**定性/逐字佐证**，不重新抓取、不重设分母、不把 HTML 文本命中当作原作像素真值；`review-evidence.md` §3 已 6/6 重算 match。

---

<a id="db-source-line-24"></a>
## §2 重点作品及来源（引用现有记录，不新增编造）

作品与馆藏、权利信息**沿用 dossier §12「临摹/学习清单（10 件）」与 §0 关键作品表**；本 lane 未打开任何外部 URL、未逐张目检 13 张公开图（AUDIT §6 / §12：image_seen 未设、权利为 metadata 层引用）。下列定位均可寻址到现有档案。

| 练习用作品（照录 §12 标题/馆藏） | 本路径用来观察的机制 | 来源定位（现有记录） |
|---|---|---|
| 《大使们》1533（NGL NG1314；207×209.5 cm） | **物证叙事** + 织物质感（缎/毛/金各自高光签名）+ 受控畸变（骷髅）+ 铭文编码（地面/鞘/书页） | dossier §12-1 L369-374；§1-1/§1-7/§1-10；AUDIT S1-1/S1-7/S1-10；NGL 页抓取 sha 19a66a…（X-AGES 双说亦在此页） |
| 《墓中基督》1521/22（Kunstmuseum Basel；30.5×200 cm 极端横幅） | **不修辞的物证**；格式服务内容；「情感强度不得由光承载」 | dossier §12-2 L376-381；counterexample.md §反例1/§反例3 |
| 《伊拉斯谟》1523（NGL L658） | **学者肖像编码**（手-书-铭文）；书脊/书口铭文；拉丁原文未核到（X-ERASMUS honest unverified） | dossier §12-3 L383-387；corpus Q5/Q6；AUDIT X-ERASMUS |
| 《克里斯蒂娜》1538（NGL NG2475） | **几何三角 + 服丧黑**；三小时写生的「静」；面具级静默 | dossier §12-4 L389-393；§3-5；corpus Q16 |
| 《克利夫斯的安妮》1539（Louvre INV1348） | **素蓝平面背景**；头带铭文/胸针婚姻语义；纹样密度逐件可数 | dossier §12-5 L395-399；§1-8；corpus Q9 |
| 《吉斯泽》1532（Berlin Gemäldegalerie） | **职业属性静物化**（桌面物证清单 ≥8 件）；执笔的手 | dossier §12-7 L407-411；§1-5/§1-6 |
| 《托马斯·莫尔》1527（Frick） | **朋友肖像的克制**；红袍金链身份；guarded restraint | dossier §12-8 L413-417；§3-1 |
| 自画像 1542/43（Uffizi） | **自我声明**（圆形 tondo、Basel 市民自题、直视）；净面让脸承担全部 | dossier §12-10 L419-422；§3.1「自我书写 1–2 件」 |

> **权利/图像边界**：13 张公开图逐张 license 见 内部证据 4a9fdf1ecb3ea8b6（未公开；来源记录由维护者保留）（12 Public domain + 1 CC0 `dead_christ.jpg`）；本 lane 只引用记录、不复制像素、不重新授权（外部许可页真实性 `unverified`）。`henry_viii.jpg` 为 **After Holbein 摹本**、`darmstadt_madonna.jpg` 1528 补笔有工作室参与 —— 按现有口径不升级/不降级。
> **逐字证据边界**：语料 Q1 遗嘱（corpus L15–L23）逐字命中 Chamberlain Vol2 抓取 sha 62bcfbaa… 的 **L17540–17565**（`gohooste / John Holbeine / servaunte to the Kynges Magestye / Octaber / sealed and sealed [sic] / MVCxliij / Snecher / Obynger / Maynert`）；但语料 Q1 自身注写 `chamberlain2_raw.txt:13601–13614`，该处实为 **"248 THE WINDSOR DRAWINGS"** 页文本（review-evidence.md §2 独立复现）→ 两套行号对应不同分卷/OCR 版本，**只报告漂移、不判对错、不改源**。

---

<a id="db-source-line-44"></a>
## §3 要观察的机制（北方文艺复兴肖像精工 + 织物质感，带定位与等级）

> 本节把 §4 六参数与 §8.2 八规则翻译成「看什么」，全部带 `文件:节:行` 定位。量化阈值均 `[归纳]`、未实测（dossier §8.2 末注 L216）。

| 机制 | 可判定量（§8.2） | 来源定位 | 等级 |
|---|---|---|---|
| **M1 物证级表面 / 织物质感分化** | ≥3 类材质各自高光签名可分类（缎=宽软高光；毛皮=纤维级纹理+软阴影；金=点/线状高光；玻璃=小镜面点；纸=低反差微纹理）；每类面积 ≥5% | dossier §8.2-3 L209；§1-1 L34；NGL「recreate a variety of textures」(R1) + Foister「minutely rendered clothing」(R15)；AUDIT S1-1 | `[史料]/[研究]`（馆方/学者原话）+ `[归纳]`（≥3 类 / ≥5% 阈值） |
| **M2 净面（无排线、无笔触）** | hatching/crosshatching 检出 = 0；可见笔触覆盖率 ≤5%；表面纹理以 <2px 尺度为主 | dossier §8.2-1 L207；§1-2 L35；Ganz「enamel-like lustre」(R13→R15)；§3.1 vs 丢勒分工轴 | `[史料]`（工艺描述）+ `[归纳]`（阈值） |
| **M3 外硬内柔的边缘** | 物体边界梯度带宽 ≤2px（1000px 参考帧）；面部内过渡带宽 ≥2% 短边；边界外 3px 内无 >30% 中间值羽化带 | dossier §8.2-2 L208；§1-3 L36；Strong「everything began with a drawing」/Rowlands (R15) | `[研究]`（线描基因）+ `[归纳]`（阈值） |
| **M4 物证清单（道具 + 文字）** | ≥3 件道具/文字，每件「可读」（文字 OCR 置信 ≥0.8 或仪器刻度可数）；人物-道具接触关系 ≥1 处 | dossier §8.2-4 L210；§1-6 L39；NGL「visual essay on the religious and political turmoil」(R1) | `[史料]` + `[归纳]` |
| **M5 铭文编码（画内文字）** | 字符高度 ≥ 全画高 1%；位于**功能表面**（地面/书页/书脊/鞘/头带）；≥1 处「自指」（签名/年龄/箴言） | dossier §8.2-5 L211；§1-7 L40；corpus Q2–Q9（Q2 `Joannes Holbein pingebat, 1533` / Q3 `AET. SVAE 29` / Q4 `AETATIS SVE 25` / Q8 `Veritas odium parit` / Q9 `A BON FINE`） | `[自述]`（画内文字本身）+ `[归纳]`（1% / 功能表面判据） |
| **M6 软光 / 信息照明** | 无画内光源；阴影边界带宽 ≥2% 短边；暗部 V ≥0.05；亮度阶跃 ≤10%/px（无硬切投影） | dossier §8.2-6 L212；§3.1 L83-84「光是信息照明」；C-01（站无硬阴影侧） | `[归纳]`（分工依据 + 阈值） |
| **M7 几何构图 / 平面背景** | 中轴 ±5% 有锚点；可检出对称或三角/圆结构线 ≥1 组 | dossier §8.2-7 L213；§1-8/§1-9；R2 克里斯蒂娜三角；R7「abstract blue background」 | `[史料]` + `[归纳]`（±5%） |
| **M8 受控畸变 / 隐藏装置（可选）** | 变形元素面积 ≤8%；正常视角为「干扰色块」；斜视角/仿射校正后 IoU ≥0.5 | dossier §8.2-8 L214；§1-10 L43；NGL「bottom right corner」/1787「à prendre de l'angle gauche」（两说并记，X-ANGLE） | `[史料]`（观看角度两说）+ `[归纳]`（8% / IoU） |

> **两重点机制的咬合点（北方文艺复兴肖像精工）**：dossier §6.2 L142 一句话来历——「先用**对脸写生**拿到『像』（素描系统，§2-1 L49）→ 用**几何转写 + 薄层罩染**把材质逐件交付（净面工艺，§2-2/3 L50-51）→ 用**铭文与物品**把身份编码进画面（文本系统）→ 最后把『隐藏』也做成精确机械装置」。M1（织物质感）+ M2（净面）是同一工艺的两面：**精工不是高清滤镜，而是一套物证装置**（dossier L142）。练习阶梯即围绕这条咬合展开。
> **X-AGES 约束**：M5 的「年龄铭文」在本卡旗舰作《大使们》上恰是 conflict 焦点——馆方同页 In-depth「28 and 24」vs Audio description「25 and 29」，语料 Q3/Q4 与 Hervey 拉丁铭文逐字为 **29 / 25**（AET. SVAE 29 / AETATIS SVE 25）。练习里只引用**铭文原文 29/25** 作为身份编码证据，馆方英译双说作为 known-open 携带、不裁断、不写进任一年龄数值的默认档。

---

<a id="db-source-line-64"></a>
## §4 三段练习阶梯（建议练习；顺序 = 观察→决策→机制→参数→一次练习→反例→自检）

> **全部练习为建议练习、效果未经人评**；§8.2 八阈值均为 `[归纳]` 未实测、只作为**自查口径**而非史实（dossier §8.2 末注 L216 / §10-6 L270）。三阶梯对应 dossier §12 组合练习建议 L421：第 1/7 件物证叙事、第 3/8 静默与编码、第 4/5 几何与平面、第 2/6 格式极端。

<a id="db-source-line-68"></a>
### 阶梯 1：净面物证 + 织物质感（单人肖像精工的起步档）
- **观察对象**：《吉斯泽》桌面物证清单、《克利夫斯的安妮》金线珠饰逐件可数、《大使们》缎/毛/金。dossier §12-5/7/1；§1-1。
- **创作决策**（how-to-think D1/D2）：先做**对脸写生素描** → 几何转写 → 薄层罩染逐件交付材质；牺牲「可见笔触」「排线做明暗」「表情叙事」。
- **机制**：M1 + M2 + M3（净面材质分化 + 外硬内柔）。
- **参数**：P1 中→强（物证级细节密度，默认 70%）、P2 中→强（净面程度，默认 65%）、P3 中（情绪克制，默认 60%）；P4/P5/P6 弱档（纯肖像档把 P4 弱、P6 关，dossier §8.1 L201）。
- **一次可做的练习**（§12-7 L411 / §12-5 L399）：① 画一位职业者的「桌面」：≥8 件与职业相关物品全部可辨识、人物只需半身；② 同一块织物画 3 版（缎/毛/金），检查每类高光签名是否可分类；③ 生成式：固定 prompt 只改 `material class / brush texture / glaze layers`，4–6 张成组自查 hatching=0。
- **反例**：出现交叉排线 → 越界丢勒（§3.1 第一轴）；出现可见厚涂/肌理表达 → 越界伦勃朗/梵高；把同规格铭文放到毛皮/金线区 → 触发 counterexample.md §反例2 的「功能表面」张力。
- **自检**：§8.2-1（hatching=0、笔触 ≤5%、<2px 纹理）、§8.2-2（边界 ≤2px、面部内过渡 ≥2%）、§8.2-3（≥3 类材质、每类 ≥5%）。

<a id="db-source-line-77"></a>
### 阶梯 2：物证叙事 + 铭文编码（《大使们》档）
- **观察对象**：《大使们》双人 + 中轴物台（上层天文仪器 / 下层音乐与算术）、两双手锚点、铭文在地面/鞘/书页；《伊拉斯谟》手-书-铭文。dossier §12-1/3。
- **创作决策**（how-to-think D3/D4）：先写「用哪些物品/文字回答『他是谁/这是什么时刻』」，把语义交给**物证清单**而非表情；牺牲「人物互动」「平均照亮」「戏剧光」。
- **机制**：M4 + M5 + M6（物证清单 + 铭文编码 + 信息软光）+ M7（中轴锚点）。
- **参数**：P1 强、P2 强（《大使们》档，dossier §8.1 L201）、P4 强（≥3 处铭文）、P5 中（单向柔光默认 55%）、P6 中（骷髅 + 十字架，可选）。
- **一次可做的练习**（§12-1 L374 / §12-3 L387）：① 画「双人 + 物台」：两人不互动，全部语义交给台上 ≥6 件物品；② 加 ≥2 处可读文字（其中一处自指，字符 ≥1% 画高且落在**功能表面**）；③ 画「正在工作的人」：手-物关系必须成立（写/按/持），≥1 处人物-道具接触点；④ 加一个「只在一个角度成立」的装置（简单透视/网格），检查它是否不干扰正面读解。
- **反例**：把 P1/P2 满档误当「≥2 条≥中档即成立」的充分条件（counterexample.md §反例1：《墓中基督》6:1 横幅即反例）→ 须把「画幅比 + 题材类别」写成分母前置条件；把情感强度挂到光上（引入硬光/烛光）→ 同时破 §3.1 第二轴与 C-01。
- **自检**：§8.2-4（≥3 道具可读、OCR ≥0.8、接触 ≥1）、§8.2-5（字符 ≥1%、功能表面、≥1 自指）、§8.2-6（无画内光源、阶跃 ≤10%/px）、§8.2-7（中轴 ±5% 锚点）。
- **X-AGES 诚实**：练习若涉及「年龄铭文」，只用 Q3/Q4 的 **29/25**（Hervey 逐字）；馆方英译 28/24 vs 25/29 双说作为 `conflict (NEW)` 携带、不裁断、不写入默认档（AUDIT X-AGES / review-evidence.md §3）。

<a id="db-source-line-87"></a>
### 阶梯 3：几何/平面/格式极端 + 收口
- **观察对象**：《克里斯蒂娜》三重三角 + 服丧黑全身像、《克利夫斯的安妮》素蓝平面背景、《墓中基督》6:1 横幅、自画像 tondo、白厅《亨利八世》摹本权力姿势。dossier §12-2/4/5/6/10。
- **创作决策**（how-to-think D5/D6/D7）：选「几何结构线 / 平面背景 / 极端格式」作为静默的载体；牺牲「三维场景纵深」「可爱化」「装饰金平面」。
- **机制**：M7（几何/平面）+ M8（可选受控畸变）+ M6（情感强度归物证与格式、不归光）。
- **参数**：P1 强、P3 强（面具级静默）、P5 中–强（较强定向但仍软边）、P6 关/中；P4 弱（纯肖像档）。
- **一次可做的练习**（§12-2 L381 / §12-4 L393 / §12-5 L399 / §12-10 L422）：① 画 6:1 横幅「横陈物」：不用任何戏剧光，全凭解剖/材质精度；② 画全身「静立」像：用 ≥2 组三角形结构线定位，只许黑 + 肤色 + 一处暖色；③ 正面肖像 + 纯色平面背景，不画手，语义收进服饰细节与 1 处铭文；④ 圆形自画像：禁工具与背景，只留一处自指铭文。
- **反例**：全画系统性拉长 → 越界格列柯；装饰金平面 + 图案化 → 越界克里姆特；高彩度补色并置 → 越界梵高；硬切投影 → 越界卡拉瓦乔（§4 越界警报 dossier L102 六条）。
- **收口自查**：跑 §8.2 八条逐帧自查；按 §4 用法判「这个需求还是不是荷尔拜因」（P1/P2/P3 中 ≥2 条 ≥ 中档才成立 → **必要非充分**，见 counterexample.md §反例1）；按 §8.1 中文说明换模块或降档，而不是去改阈值。

---

<a id="db-source-line-98"></a>
## §5 可观察结果（产物级 / 不是学习成效）

> 本节只列**画面自查可观察特征**，不写「学习者能力提高」「已证实学习收益」（01-AUDIT.md §8.1 L273）。全部为 `[归纳]` 规则层的产出判据，非原作像素真值。

| 阶梯 | 可观察的产物特征（§8.2 量纲） | 不是 |
|---|---|---|
| 1 | hatching=0；笔触覆盖 ≤5%；≥3 类材质各自高光签名可分类、每类 ≥5%；物体边界 ≤2px / 面部内过渡 ≥2% | 不是「荷尔拜因用过的实测阈值」 |
| 2 | ≥3 件道具可读、文字 OCR ≥0.8、接触点 ≥1；字符 ≥1% 画高且落功能表面、≥1 自指；无画内光源、阶跃 ≤10%/px；中轴 ±5% 有锚点 | 不是「情感/身份被成功解码」的人评 |
| 3 | ≥1 组三角/圆结构线；平面背景面积占比可测；变形元素 ≤8% 且仿射校正后 IoU ≥0.5（启用时）；六条越界警报均不触发 | 不是「风格迁移已通过 E4」 |
| 收口 | §4 用法 P1/P2/P3 ≥2 条 ≥ 中档 + 八条逐帧自查通过 | 不是「accepted」——本产物 `submitted` 待独立审者裁定 |

---

<a id="db-source-line-111"></a>
## §6 常见失败（反例 / 失败条件，按冲突与现有记录）

> 完整展开见 `mechanism_notes.md §C/§F` 与 内部证据 3151350c5955afba（未公开；来源记录由维护者保留）（3 则全标 `[inference]`、未像素实测、未目检、未跑生成器、未推翻规则）。

1. **越界丢勒**：出现排线/交叉排线做明暗 → 破 §8.2-1、§3.1 第一轴（dossier L102 越界警报①）。
2. **越界卡拉瓦乔/伦勃朗**：硬切光斑 / 戏剧投影 / 烛光 → 破 §8.2-6、C-01、§3.1 第二轴（警报②）；可见厚涂笔触/肌理表达 → 破 M2（警报③）。
3. **counterexample §反例1**：《墓中基督》6:1 横幅 P1/P2 满档仍难同时满足 §8.2-7（中轴 ±5% 锚点）与 §8.2-3（≥3 类材质每类 ≥5%）→ §4「≥2 条≥中档」是**必要非充分**；「画幅比 + 题材类别」是未显式入参的隐藏分母。
4. **counterexample §反例2**：可读铭文（≥1% 画高 / OCR ≥0.8）与净面无笔触 + 软边低阶跃在同像素区张力 → 「文字落在**功能表面**」是消解张力的隐藏必要条件，不是装饰条款。
5. **counterexample §反例3**：《墓中基督》冲击来自物证 + 极端格式而非光 → 「情感强度不得由光承载」是可操作判据。
6. **其余越界**：全画系统性拉长（格列柯）/ 装饰金平面（克里姆特）/ 高彩度补色并置（梵高）（dossier L102 警报④⑤⑥）。
7. **known-open 不进判分**：X-AGES 双说、11 处 C-row 行号漂移、Q1 遗嘱 locator drift、X-ANGLE 观看角度两说、X-ITALY 两说 —— 均**报告不修**、不改变 §4/§8.2/分工条款的 `supported` 状态（AUDIT §9 / §12）。

---

<a id="db-source-line-125"></a>
## §7 下一步（接入 A-30 总路线，不越界）

| 对方 / 去向 | 处置 | 定位 |
|---|---|---|
| **vs 丢勒** | 冲突轴 = 明暗手段（排线密度 vs 净面罩染）+ 精准对象（规则化 vs 物证化）；须 ≥2 轴联合成立；同屏「谁管线、谁管面」不可互换主风格 | dossier §3.1 L76-82；§12 L421 A/B 对照 |
| **vs 伦勃朗** | 冲突轴 = 光的功能（信息照明 vs 情感照明）+ 情绪位置（画外 vs 画内）；同用时选 70/30 主导轴 | dossier §3.1 L83-89 |
| **C-01 / C-05 / C-12** | 预检指针：C-01 站「无硬阴影/软光」侧、C-05 站「近无笔触」侧、C-12「低饱和 + 深黑 + 金，靠材质不靠彩度」；holbein 无专属 C-row | dossier §3.1 L90；modules/holbein.md L85；AUDIT X-CONFLICTS |
| **STYLE-holbein / A-12 实验 lane** | 缺 §8.1b 纯风格节（card_has_81b=false）与像素实测属 STYLE / A-12 lane；本 LEARN lane 无 repo 写权、不测量、不升级为已推翻 | ledger artist-shards.json artists[holbein]；dossier §10-6 L270 |
| **指标阈值回改** | §4/§8.2 阈值 `[归纳]` 未实测（分母＝假想参考帧），组合实验可按 §8.2 自查表回改 | dossier §8.2 末注 L216 / §10-6 L270 |
| **独立审者** | 本产物 `submitted`（review=null），待非作者审者复验 5 产物 hash 与定位后出 verdict | receipt.json；verify-receipt.py 语义门 |

---

<a id="db-source-line-138"></a>
## §8 使用边界（硬边界，照录）

- **repo READ-ONLY** @ `f008952365a77e140cbda3f3959d43ef000f9a22`；0 文件改动、0 git 操作、0 subagent spawns、0 credentials、0 外部 URL 重新抓取。
- **未打开任何 .jpg**（image_seen 未设）、未复访 Commons imageinfo / 馆方页 → 13 张权利是 **metadata 层引用**（12 PD + 1 CC0），非独立再 adjudicate；`review-evidence.md` §5 确认。
- **语料未逐条回校原刊**：Q5/Q6 拉丁/希腊原文、X-AMERBACH-VERSE 上方拉丁诗句、Q13/Q14 OCR 回校、van Mander 荷兰文 —— 全保持 unknown/partial（AUDIT §5 / §12）；`X-ERASMUS` / `X-AMERBACH-VERSE` 为 honest `unverified`。本 shard 只声称「本机档案内自洽 + 定位可寻址」。
- **X-AGES / X-ANGLE / X-ITALY / 11 处行号漂移 / Q1 遗嘱 locator drift**：全部 **报告不修**（contract），作为 known-open / conflict 携带，不关闭、不裁断、不改源。铭文拉丁原文 29/25 优先于馆方英译双说。
- **练习效果**：全部为建议练习；无 human review、无真人学习成效数据，`human_review.status=not_applicable`，**不写「已证实学习收益」**。
- **`review:null`**：本产物 `submitted`，待独立审者（非作者）裁定；作者不自接受。本包 dispatch_contract_state 对 LEARN 未绑定 bound contract → `submitted` 不经 accepted/reused 语义门（与 AUDIT 首版同口径；AUDIT 现已经 gate 升为 accepted，本 LEARN 仍待自身独立审阅）。
- **下一步**：① 独立审者复验 5 产物 hash 与定位；② 主张「学习收益」需固定样本包 + 真人评价；③ A-12 实验 lane 做参考帧像素实测后回改阈值；④ A-30 总路线按 §7 分支接入组合实验。

---

<a id="db-source-line-150"></a>
## 附：本文件每条断言的定位索引

| 断言类 | 主定位 |
|---|---|
| A-30 8-section 形状 / 3 阶梯 | 02-EXECUTION-PLAN.md L64；01-AUDIT.md §8.1 L273；本卡 §1–§8 |
| 北方文艺复兴肖像精工 + 织物质感 | dossier §1-1 L34 / §2-3 L51 / §6.2 L142；§8.2-3 L209；AUDIT S1-1 |
| X-AGES 双说（28/24 vs 25/29） | AUDIT RESULT §7 额外发现 / X-AGES；claim_evidence_map.md §F X-AGES；review-evidence.md §3；ngl_ambassadors.html sha 19a66a… L709 vs L738；hervey1900.txt sha f7734f75… L456-457 |
| Windsor drawings + 遗嘱逐字 | corpus Q1 L15–L23；review-evidence.md §2；chamberlain2_raw.txt sha 62bcfbaa… L13600-13603 "248 THE WINDSOR DRAWINGS" / L17540-17565 遗嘱逐字；AUDIT §9 §G |
| 13 rights rows = 12 PD + 1 CC0 | AUDIT rights_review.md §逐张表 / RESULT §6；review-evidence.md §5；coverage-manifest.json images_public=13 |
| §4 六参数 / §8.2 八规则 | dossier §4 L95-102 / §8.2 L207-216；modules/holbein.md §4 / §8.2 |
| 3 个 `[inference]` 反例 | 内部证据 82fa3400e8077a9c（未公开；来源记录由维护者保留） RESULT §8；review-evidence.md §7 |
| 证据底本 ACCEPTED | 内部证据 152f099a4d351899（未公开；来源记录由维护者保留） (status accepted / review accepted)；review-gate-receipt.json (verdict accepted)；review-evidence.md §1 |

## 同一条目的附页

- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
