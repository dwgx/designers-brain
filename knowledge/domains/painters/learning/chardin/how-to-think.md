<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-chardin；原正文 SHA-256 `4e883992b4e1845c01b2206cc6831f9775f361df07586e96c3febef0d723c9a1`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-chardin — How to Think（创作决策序）

> 任务 `LEARN-chardin`（A-30）· 依赖 `AUDIT-chardin`（ACCEPTED，磁盘 `receipt.json` `status=accepted` / `review.verdict=accepted` / `review-evidence.md` Verdict=accepted）。仓库 内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留） @ `f008952365a77e140cbda3f3959d43ef000f9a22`（只读）。
> **本文回答**：「用夏尔丹这套做一次创作决策时，先选什么、牺牲什么、为什么、何时失效」。它是**决策序**，不是生平、不是技法清单、不是心理画像。
> **本文两条贯穿线（brief 强调①）**：**D1–D3 = 弱光源 + 反光网络（不可见前提）**，**D4–D6 = 质感层积（可见输出）**，**D7–D8 = 收口与边界**（含 D8 的 Cochin/Diderot 闭环与 CE 介质 open）。**弱光源是前提，质感层积是输出；先定光再堆表面，是本卡决策序的骨架。**
> 证据底座与三件冻结输入哈希见 [learning_path.md](learning_path.md) 抬头；逐 claim 定位见 [claim_evidence_map.md](claim_evidence_map.md)。

---

<a id="db-source-line-10"></a>
## 0. 严格分栏规则（先读）

| 标记 | 含义 | 允许写什么 | 禁止写什么 |
|---|---|---|---|
| `[自述]`（`[self-written]`） | 本人书信（corpus 仅 2 条：Q2 1778 致 d'Angivillier「画家的账」、Q3「转粉彩」） | 只引用 `_corpus/chardin.md:L18-L30` 带「来源/fr.wikipedia 转录/原件未回查」注记的原话 | 不把转记、同时代评述、后世研究写成「夏尔丹说」；不把 Q2/Q3 升格为一手档案认证（§10-1） |
| `[自述转记]`（`[reported speech]`） | 他人转记的本人话语（Q1 Cochin 1780 信「sentiment」、Q4 Malraux 异文、Q5 经马蒂斯转引、Q6 Le Bas 夹克轶事） | 只按 corpus 逐条类型标注引用；注明 Q1 取为主文本、Q4 为同源异文 | 不从转记推「他心里怎么想」；不把 Q1 写成亲笔（是 Cochin 信中转记的对话） |
| `[史料]`（`[archive]`/`[contemporary record]`） | 同时代记录/档案/馆藏（Q7 学院会议记录 1728、Q8 Mariette、Q9 La Font、Q10 Raynal、Q11–Q13 Diderot、Q14 Éloge、Q15–Q17 讣闻/题诗） | 用其支撑技法史实、作品信息、Cochin/Diderot 闭环 | 不把 Diderot 的赞词写成「夏尔丹自述其方法」 |
| `[研究]`（`[research]`） | 馆方与艺术史研究（Q18–Q28：Goncourt 1864、Proust、Denis、Faure、Malraux、Démoris、Rosenberg、Met Baetjer 2015、NGL 2018） | 用其支撑视觉机制、分工口径、反光网络/略失焦等 | 不把「研究」升格为「自述」 |
| `[归纳]` | 本项目从作品/技法推得的**可判定操作规则与参数** | §8.2 八条、§4 六参数、conflicts.md 冲突判定与 N 规则、本卡「先选/牺牲/何时失效」的决策结构、**「质感层积」「弱光源」两个机制标签** | 不冒充史料、不冒充作者自述、不冒充像素实测；不把标签写成「夏尔丹提出『质感层积』」 |
| `[推测]` | 关于作者心理状态、动机、性格的臆断 | **本卡不使用** | **严禁从画面外观反推「夏尔丹当时在想什么/感到什么」**——`00-GOAL.md:L9` 红线 |

**红线（`00-GOAL.md:L9`「How to Think 必须区分作者可核实的自述与研究者推断，不能编造作者心理」）**：
- 下文每一「决策步」都带**证据等级**；凡涉及「为什么这样选」的因果解释，源自项目规则则标 `[归纳]`，源自作者言语则标 `[自述]`/`[自述转记]`/`[史料]`/`[研究]` 并给 locator，**二者不混写在一句里**。
- 不写「夏尔丹觉得…」「他想要表达…」「他下意识…」这类从画面推心理的句子。`dossiers/chardin.md:L10` 与 `_corpus/chardin.md:L5` 已把「无画论、无书信集、无日记」写成结构性事实；dossier `L10` 明言「凡涉及『他心里如何』的表述，一律按**操作规则**处理」。
- **夏尔丹声音的结构性稀薄**：28 条语料里本人书写仅 **2**（Q2/Q3，且转录层）、转记 4、同时代记录 10、后世研究 11、档案 1（`grep '^- 类型：'` 实测 2/4/1/10/11=28，AUDIT `RESULT.md §3`）。因此本文的「为什么」**绝大多数来自同时代/后世文字与项目归纳**，而非作者自述——这正是必须分栏的原因。

**Cochin/Diderot 闭环底本（brief 强调②）**：本卡引用的全部逐字原文见 `learning_path.md §2` 专段（Q1/Q11/Q12/Q13/Q18/Q27/Q28 法文旧拼写照录 + 中文意译 + locator + fetch 核验状态）。本卡只复用该证据环的回指，不重访 4 份 fetch 缓存、不升级为一手档案认证。**「引文 37/37」= dossier 自审 C（D:478–516），不是语料条数；语料分母 = 28**（见 `learning_path.md §2` 分母辨析表，brief 强调③）——本文引用只到 Q1–Q28，绝不把 37 当语料数。

---

<a id="db-source-line-30"></a>
## 1. 决策序总览（先选什么 → 牺牲什么 → 为什么 → 何时失效）

| 步 | 先选什么（决策） | 牺牲什么 | 为什么（分栏） | 何时失效（边界） | 本步等级 |
|---|---|---|---|---|---|
| D1 | **先定「弱光源」**：单一漫射侧光、无画外戏剧光、暗部暖褐/灰绿有层次 | 牺牲戏剧性明暗（卡拉瓦乔档）、牺牲冷蓝平坦暗部（维米尔档）、牺牲锐投影 | `[史料]` Q11 Diderot「c'est la substance même des objets… l'air et la lumière」、Q10 Raynal 放而不混（`_corpus/chardin.md:L76-L88`）；`[归纳]` §8.2-3 纯黑 ≤0.5% / 暖阴影 H20–60° / 暗部标准差 ≥2/255（`modules/chardin.md:L46`）、P4 光质柔和 60%（`L62`） | 组合任务本身要求「画外单光 + 近黑背景」（卡拉瓦乔侧）或「冷调光学结构」（维米尔侧）→ 本卡不适用、换模块（§3.1 默认二选一） | `[史料]`+`[归纳]`；失效 `[归纳]` |
| D2 | **先织「反光网络」**：≥2 处跨物反光、所有高光为宽软反光带 | 牺牲孤立点状高光（维米尔档）、牺牲「各物自带高光即够」 | `[研究]` Q18 Goncourt「un travail systématique de reflets… envelopper chaque chose de la teinte et de la lumière de tout ce qui l'avoisine」（`_corpus/chardin.md:L134-L139`）；`[归纳]` §8.2-2 跨物反光 ≥2 / 宽软形圆度 ≤0.7 或长宽比 ≥2 / σ ≥2px / 禁 1–3px 点（`modules/chardin.md:L45`）、P2 65%（`L60`） | 与 C-11 高光计数组合时按 N7 单列「反光带」类、不并入点状计数；画面只有单一物体无邻物可映（CE-1 粉彩自画像类）→ 规则空白，按介质分栏（D8） | `[研究]`+`[归纳]`；失效 `[归纳]` |
| D3 | **先立「材质分工 + 浅空间中立场」**：同屏 ≥2–3 类材质各有专属笔法、物体贴前缘、背景中性半调 | 牺牲纵深可读的荷兰室内、牺牲地砖/单点透视网格、牺牲背景叙事细节 | `[研究]` Q27 Met「never disguise the rough texture of paint」（`_corpus/chardin.md:L199-L204`）、Q26 Rosenberg 层积/罩染/fondu（`L192-L197`）；`[归纳]` §8.2-6 材质专属处理、§8.2-4 背景边缘密度 ≤前景 30% / 包围盒 ≥50%（`modules/chardin.md:L47,L49`）、P3 70% / P5 65%（`L61,L63`） | 与塞尚组合时「形体处理」按 N4 不可拆、不得折中「半几何半触感」；门洞第二空间仅《La Fontaine》类边界注允许（§3.1 判据 ≥2 轴，不看「有没有门」） | `[研究]`+`[归纳]`；失效 `[归纳]` |
| D4 | **在光内做「放而不混的层积」**：颜色一笔一笔并置、不预先调匀、近看颗粒退后成物 | 牺牲预先调匀的平滑渐变（达·芬奇侧）、牺牲「抹平笔触/多层罩染到不可见」、牺牲一律点彩 | `[史料]` Q10 Raynal「mosaïque de pièces de rapport… point carré」（`_corpus/chardin.md:L76-L81`）、Q12 Diderot 远近检验「Approchez-vous, tout se brouille… Éloignez-vous, tout se crée」（`L90-L95`）；`[归纳]` §8.2-1 可辨笔触 30–80% / 粒径 2–8px / 方向峰值 ≤35%（`modules/chardin.md:L44`）、P1 70%（`L59`） | 组合需 C-05「笔触可见度」轴单主（N3）；做成统一方向 tache 族 → 越界塞尚（`L67` ②）；把层积读成「无方向乱笔」→ 丢 D1–D3 前提（F1） | `[史料]`+`[归纳]`；失效 `[归纳]` |
| D5 | **选「表面完成度：堆叠 + 罩染 + 局部揉合」**：厚涂与透明层并存、无裸露画布、边缘柔软融入 | 牺牲未完成感/骨架线可见（塞尚档）、牺牲镜面完美高光、牺牲硬边 | `[研究]` Q26 Rosenberg「larges touches… puis aux reflets, aux transparences, au « fondu »」（`_corpus/chardin.md:L192-L197`）；`[归纳]` §8.2-8 裸露画布 ≤1% / 边缘过渡带 ≥2px / 64×64 块 L* 梯度 0.5–3（`modules/chardin.md:L51`）、P6 50% 时期滑轨（`L64`） | 晚期档（约 1755 后）P6 升强（反光/透明/fondu 主导）；粉彩档按介质分栏（CE-2：纯色平行笔触与 §8.2-1 ≤35% 方向峰值需显式 scope） | `[研究]`+`[归纳]`；失效 `[归纳]` |
| D6 | **选「悬浮静默 + 谦卑母题」**：无叙事/无动作矢量链、动作中停、日常器物主角化 | 牺牲情节/道德剧/寓意道具、牺牲直视观众的心理交流、牺牲运动模糊 | `[研究]` Q25 Démoris「saisis dans un temps mort… en position de repos」（`_corpus/chardin.md:L185-L190`）、Q19 Goncourt「life of inanimate objects」（`L141-L146`）；`[归纳]` §8.2-7 0 帧运动模糊 / Δ ≤1% / 动作中停（`modules/chardin.md:L50`）、§1-6/§1-8（`dossiers/chardin.md:L44,L46`） | 任务本身要求叙事高潮/动势（Lane B 动作档）→ 本卡不适用；与维米尔组合时仍按「≥2 轴」判、不靠「安静」气质混同 | `[研究]`+`[归纳]`；失效 `[归纳]` |
| D7 | **收笔 = 按 §8.1 生成后三件事回检**：反光是否跨物（≥2 邻物色）/ 高光是否宽软（无点状系统）/ 暗部是否暖而有层次 | 牺牲「按预定清单画满即停」；牺牲近观抠细节的收尾 | `[归纳]` `dossiers/chardin.md:L198`（§8.1「生成后自查三件事」）、§8.1 `L196` 定调三件套 P1 70%+P2 65%+P4 60%；`[史料]`/`[研究]` 闭环 Q1/Q11/Q12/Q18/Q27 是这三件事的文字根 | 进入动画/C-09 运动预算域时「停止」变帧级判据（夏站静场侧、仅反光微动）；像素阈值未实测，自查是**练习自查**非原作事实报告 | `[归纳]` 为主；根 `[史料]`/`[研究]` |
| D8 | **组合前先判轴、并携带 open 项**：C-01/C-05/C-11/C-12/C-13 按 N1/N3/N4/N7 重算；**Cochin/Diderot 闭环按「证据环」标注、不写成自述链**；**CE-1/CE-2 按介质分栏** | 牺牲「把 37/37 当语料数」「把 Q1 当亲笔」「把 CE 规则空白写成已完成」的便利；牺牲收口动作（本 lane 无写权） | `[归纳]` 四条越界警报（`modules/chardin.md:L67`）、§3.1 分工（`dossiers/chardin.md:L85-L97`）；`[史料]`/`[研究]` 闭环 Q1–Q28 的转录/转述性质（AUDIT `RESULT.md §2`/`§9`）；`[归纳]` CE-1/CE-2（AUDIT `RESULT.md §6`，`[inference]` 未渲染） | 若实验 lane 完成 E 系列实测 / 来源 lane 回查原档 / CONFLICT lane 补 chardin 行 → 相应 open 注记方可移除（**本轮不得移除**） | `[归纳]`+`[史料]`/`[研究]`（open） |

> 读法：D1–D3（弱光源+反光+材质分工）与 D4–D5（质感层积+完成度）的「为什么」上半来自**同时代记录/馆方研究/转记**，D1–D8 的阈值与冲突判定几乎全是**项目 `[归纳]` 判据**；所有「何时失效」为 `[归纳]`。**任何一步都不含「从画面推作者心理」。**

---

<a id="db-source-line-47"></a>
## 2. 逐展开（每步：先选 / 牺牲 / 为什么[分栏] / 何时失效 / 等级）

<a id="db-source-line-49"></a>
### D1 · 先定「弱光源」（漫射侧光，暗部暖而有层次）
- **先选**：单一漫射侧光（多自左上/前方）、无画外戏剧光、无锐投影；暗部只用暖褐/灰绿、保留层次。`[归纳]` §8.2-3 / P4 60%（`modules/chardin.md:L46,L62`）。
- **牺牲**：戏剧性明暗、冷蓝平坦暗部、硬边投影。
- **为什么（分栏，不混写）**：
  - `[史料]`：Q11 Diderot 1763「c'est la substance même des objets, c'est l'air et la lumière que tu prends à la pointe de ton pinceau」（`_corpus/chardin.md:L83-L88`）——「把空气与光钉在画布上」是同时代人对**光为物服务**的描述，不是画家自述。
  - `[归纳]`：把「无纯黑大块 / 暖阴影 / 无冷蓝主导」固定成 §8.2-3 的像素阈值，是本项目对「弱」的可判定化；**这些数值不是夏尔丹说过的话、未对原作测量**（`dossiers/chardin.md:L281,L212`）。
- **何时失效**：组合要求卡拉瓦乔「画外单光 + 近黑背景」或维米尔「冷调光学结构」时按 §3.1 默认二选一，本卡不适用。
- **等级**：`[归纳]`（主）+ `[史料]`（根）；失效 `[归纳]`。

<a id="db-source-line-58"></a>
### D2 · 先织「反光网络」（≥2 处跨物反光 + 宽软反光带）
- **先选**：铜面映肉红、玻璃含红蓝、银器承接果与布；所有高光画成宽软反光带（非 1–3px 点）。
- **牺牲**：孤立点状高光系统；「各物自带高光即够」。
- **为什么（分栏）**：
  - `[研究]`：Q18 Goncourt 1864「un travail systématique de reflets… envelopper chaque chose de la teinte et de la lumière de tout ce qui l'avoisine」（`_corpus/chardin.md:L134-L139`）——「每个物体裹上周围一切的色调与光」是 19 世纪研究文字。
  - `[归纳]`：§8.2-2 把「≥2 处 / 宽软形 / 禁点状」写成可执行判据（`modules/chardin.md:L45`）；C-11 按 N7 单列「反光带」类（`conflicts.md:L326`）。
- **何时失效**：单一物体无邻物可映（CE-1 粉彩自画像类）→ 规则空白，按介质分栏（D8），不硬套 D:112 的「P1/P2 ≥中档」门。
- **等级**：`[研究]`+`[归纳]`；失效 `[归纳]`。

<a id="db-source-line-67"></a>
### D3 · 先立「材质分工 + 浅空间中立场」
- **先选**：同屏 ≥2–3 类材质各有专属笔法（金属宽软反光带 / 玻璃透射+反光 / 食物颗粒点触 / 瓷温润渐变）；物体贴前缘、桌沿水平（可略斜）、背景单一中性半调。
- **牺牲**：纵深可读的荷兰室内、地砖/单点透视网格、背景叙事细节。
- **为什么（分栏）**：
  - `[研究]`：Q27 Met「never disguise the rough texture of paint」（`_corpus/chardin.md:L199-L204`）、Q28 NGL「keeping objects slightly out of focus… the extraordinary beauty with which he endowed ordinary objects」（`L206-L211`）。
  - `[归纳]`：§8.2-6「禁止两种材质共用同一处理（防一律点彩）」、§8.2-4「背景边缘密度 ≤前景 30%」（`modules/chardin.md:L47,L49`）。
- **何时失效**：与塞尚组合按 N4「形体处理不可拆」、不得折中「半几何半触感」（`conflicts.md:L314`）；《La Fontaine》门洞第二空间仅在 §3.1 边界注（≥2 轴，尤②③⑤）内允许。
- **等级**：`[研究]`+`[归纳]`；失效 `[归纳]`。

<a id="db-source-line-76"></a>
### D4 · 在光内做「放而不混的层积」
- **先选**：颜色一笔一笔并置、不预先调匀；近看「马赛克/针脚」、退后聚合成物；混合发生在眼睛而非调色板。
- **牺牲**：预先调匀的平滑渐变、抹平笔触、一律点彩。
- **为什么（分栏）**：
  - `[史料]`：Q10 Raynal 1750「Il place ses couleurs l'une après l'autre sans presque les mêler… mosaïque de pièces de rapport… point carré」（`_corpus/chardin.md:L76-L81`）；Q12 Diderot「Approchez-vous, tout se brouille… Éloignez-vous, tout se crée」（`L90-L95`）——**放而不混 + 远近检验是两条同时代记录**，不是画家自述。
  - `[归纳]`：§8.2-1 可辨笔触 30–80% / 粒径 2–8px / 方向峰值 ≤35%（与塞尚 4–8 角度族区分）（`modules/chardin.md:L44`）。
- **何时失效**：C-05 按 N3 让「笔触可见度」轴单主；出现统一方向 tache 族 → 越界塞尚（`L67` ②）；把层积读成「无方向乱笔」→ 丢 D1–D3（F1）。
- **等级**：`[史料]`+`[归纳]`；失效 `[归纳]`。

<a id="db-source-line-85"></a>
### D5 · 选「表面完成度：堆叠 + 罩染 + 局部揉合」
- **先选**：厚涂（empâtement）与透明层并存、无裸露画布、边缘柔软融入环境；早期大笔并置明显、晚期反光/透明/fondu 主导（P6 时期滑轨）。
- **牺牲**：未完成感/骨架线可见（塞尚档 5–8% 裸露）、镜面完美高光、硬边线。
- **为什么（分栏）**：
  - `[研究]`：Q26 Rosenberg 1979「peint par larges touches qu'il dispose côte à côte sans les fondre… il accordera une place de plus en plus grande aux reflets, aux transparences, au « fondu »」（`_corpus/chardin.md:L192-L197`）。
  - `[归纳]`：§8.2-8 裸露画布 ≤1% / 过渡带 ≥2px / 64×64 块 L* 梯度 0.5–3（`modules/chardin.md:L51`）；P6 50%（`L64`）。
- **何时失效**：晚期档 P6 升强；粉彩档（Q/§2-7「纯色平行笔触」）与 §8.2-1 ≤35% 方向峰值在未显式分栏时相冲 → CE-2，按介质 scope（D8）。
- **等级**：`[研究]`+`[归纳]`；失效 `[归纳]`。

<a id="db-source-line-94"></a>
### D6 · 选「悬浮静默 + 谦卑母题」
- **先选**：无叙事/无动势线、人物「动作中停」、日常器物主角化；静物天然静止。
- **牺牲**：情节/道德剧/寓意道具、直视观众的心理交流、运动模糊。
- **为什么（分栏）**：
  - `[研究]`：Q25 Démoris 1969「saisis dans un temps mort de cette action… en position de repos」（`_corpus/chardin.md:L185-L190`）、Q19 Goncourt「Who has expressed… the life of inanimate objects?」（`L141-L146`）、Q9 La Font「moments… nullement intéressants」（`L69-L74`）。
  - `[归纳]`：§8.2-7 0 帧运动模糊 / Δ ≤1%（`modules/chardin.md:L50`）、§1-6/§1-8（`dossiers/chardin.md:L44,L46`）。
- **何时失效**：任务要求叙事高潮/动势（Lane B 动作档）→ 本卡不适用；与维米尔组合仍按 §3.1「≥2 轴」判，不靠「安静」气质混同。
- **等级**：`[研究]`+`[归纳]`；失效 `[归纳]`。

<a id="db-source-line-103"></a>
### D7 · 收笔 = 生成后三件事回检
- **先选**：按 §8.1（`dossiers/chardin.md:L198`）回检 ① 反光是否跨物（≥2 邻物色）？② 高光是否宽软（无 1–3px 点状系统）？③ 暗部是否暖而有层次（无冷蓝平坦、无纯黑）？
- **牺牲**：画满清单即停；近观抠细节收尾。
- **为什么（分栏）**：
  - `[归纳]`：`L198` 三件事、`L196` 定调三件套（P1 70% + P2 65% + P4 60%；「缺 P2 退化普通暗调静物、缺 P4 滑向卡拉瓦乔」）。
  - `[史料]`/`[研究]`：三件事的文字根 = 闭环 Q1（用感受）、Q11（物的实体/空气光）、Q12（远近）、Q18（反光）、Q27（粗糙质地）——**证据环的回指，不是作者自述链**。
- **何时失效**：进入动画/C-09 域时「停止」变帧级判据（夏站静场侧、仅反光微动）；像素阈值未实测，自查是**练习自查**非原作事实报告。
- **等级**：`[归纳]` 为主；根 `[史料]`/`[研究]`。

<a id="db-source-line-112"></a>
### D8 · 组合前先判轴、并携带 open 项
- **先选**：C-01（软光侧顺风）/C-05（笔触「可见但非全覆盖」显式取值）/C-11（按 N7 单列反光带）/C-12（暖土色系显式取值）/C-13（暖褐/灰绿阴影）按 N1/N3/N4/N7 重算；**Cochin/Diderot 闭环标注为「证据环（他人文字 + 转记）」**；**CE-1/CE-2 按介质分栏**。
- **牺牲**：把 37/37 当语料数、把 Q1 当亲笔、把 CE 规则空白写成「已完成」的便利；收口动作（本 lane 无写权）。
- **为什么（分栏）**：
  - `[归纳]`：四条越界警报（`modules/chardin.md:L67`）、§3.1 分工（`dossiers/chardin.md:L85-L97`）、CE-1/CE-2（AUDIT `RESULT.md §6`，`[inference]` 未渲染验证）。
  - `[史料]`/`[研究]`：闭环 Q1–Q28 的转录/转述性质（AUDIT `RESULT.md §2` 分母辨析、§9 unresolved #1 原档未回查）；「引文 37/37」是 dossier 自审 C（D:478–516）作者主张、语料分母=28（G:88 / INDEX L74 同句并列，审者 `review-evidence.md §3` VERIFIED）。
- **何时失效**：实验 lane 完成 E 系列实测 / 来源 lane 回查 1780/1778 原档 / CONFLICT lane 补 chardin 具名行并修 C-11/12/13 陈旧数值 locator / `_scratch` 进入可读 lane 重跑 37/37 → 相应 open 注记方可移除（**本轮不得移除**）。
- **等级**：`[归纳]`+`[史料]`/`[研究]`（open）。

---

<a id="db-source-line-123"></a>
## 3. 等级 / 红线复核（本卡自检）

- **全表 `[推测]` 计数 = 0**。所有「为什么」均可回指 [chardin.md](../../dossiers/_corpus/chardin.md) 逐条（带类型与行号）、dossier §1/§2/§3/§4/§8.1/§8.2、§10 或 conflicts.md 具体行（逐条 locator 见 [claim_evidence_map.md](claim_evidence_map.md)）。
- **同形异义 / 分母警告**：① 「质感层积」「弱光源」是本项目 `[归纳]` 机制标签（学习方法），**不是**史料术语、不是作者自述；② 「Cochin/Diderot 闭环」是**证据环**，A/B′/B″ 是同时代文字、C/D 是后世研究、A 是转记——**不得**写成「夏尔丹自述其层积法」；③ 「引文 37/37」= 自审抽查、**语料 = 28**，三者（含图像 17=11+3+3）分母分栏不混用（brief 强调③④）。
- **心理红线**：本文零句「夏尔丹觉得/想要/下意识」；凡「为什么」涉及作者，只引用带载体的言语记录或明确标 `[归纳]` 的项目规则（`00-GOAL.md:L9`、`dossiers/chardin.md:L10`）。
- **转录层诚实**：Q1 经 fetch1 逐字核但**原档私人文书未回查**（§10-1）；Q2/Q3 是 `[self-written]` 但经 fr.wikipedia 转录、原件未回查；Q12 法文逐字未独立 web 复取（AUDIT `claim_evidence_map.md:L130`）——本卡全部沿用 AUDIT 的「supported-via-transcription，不升一手」口径。
- **阈值诚实**：§4/§8.2 全 `[归纳]`、未对原作像素测量（分母＝假想参考帧，`dossiers/chardin.md:L281,L212`）；AUDIT `image_seen=0`；本卡自查是建议练习自查、非原作事实报告。
- **open 携带**：CE-1（粉彩自画像被 D:112 门误判）、CE-2（粉彩平行笔触 vs §8.2-1 方向峰值）、原档未回查、Artcurial €24,381,400 未复取、conflicts.md 无 chardin 具名行 + 数值 locator 陈旧、37/37 未重跑——全部照实携带、不收口、不改写仓库/审计产物（AUDIT unresolved #1–#5）。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
