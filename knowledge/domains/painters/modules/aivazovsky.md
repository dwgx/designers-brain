# 艾瓦佐夫斯基 模块卡 — `aivazovsky`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/aivazovsky.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **透明浪体**：浪脊 2–4 级透光阶梯、泡沫只在脊线与落点（≤30% 浪体）；「雕塑浪形」而不改笔——浪是光可穿过的体积
2. **月光路径**：夜海有且仅有一条发光路径柱（自光源延伸 ≥40% 画高）；月亮连通域 1 个、单光源——水面对光的反射即结构
3. **极低地平线＋火水对撞**：天空占 ≥55–60%（《黑海》「除了天空和水一无所有」）；暖族与冷族各 ≥15% 面积同屏对撞
4. **浪峰「将落未落」＋人造物剪影**：主浪脊线凸弧未闭合、取最高势能帧；船／桅／人 L ≤25% 深剪影、人 ≤10% 画高不画脸
5. **水的形态库＋表面平滑＋银灰档**：штиль／зыбь／буря 三档循环重画；非泡沫区笔触隐没（高频 ≤ 泡沫区 1/3）；晚年近乎单色银灰（中位饱和 ≤0.25）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Aivazovsky-style Romantic marine oil painting — the water itself is the protagonist:
a translucent wave body, light passing through the crest in two to four graded steps
from deep blue-green to luminous white, foam kept as a lace of small bright touches
along crest lines and impact points, no opaque flat water; one single luminous body
(full moon or low sun) with a long shimmering reflection path running from the source
down across the water toward the viewer; very low horizon, the sky taking the upper
two thirds, sea and sky as two halves; warm and cool collide — golden-amber light
against cold blue-green water; ships, masts or a distant fortress only as dark
silhouettes (tiny human figures, no faces); smooth blended surface, no impasto,
no visible brush texture outside foam; clouds luminous and storm-charged, backlit
edges; dramatic but readable wave anatomy — crests not yet breaking, frozen at the
moment of highest energy; palette either fire-toned (sunset/storm) or blue-marine
(day) or silver-grey (late restrained mode)
```
**负向约束（`--no` 风格）**
```
--no Turner-style edge dissolution or atmospheric fog swallowing the scene,
no steam, no weather-as-subject, no dissolving contours; no ukiyo-e line-wave
families, no claw foam drawn as graphic lines, no flat colour fill, no silhouette
waves; no pointillism, no dabs, no impasto, no palette-knife texture, no thick
visible brushstrokes; no chiaroscuro spotlight on faces, no single indoor light
source, no deep brown-black shadow crush; no ice fields, no frozen sea; no neon,
no HDR, no photographic realism, no watermark, no lettering overlays
```

## 代码艺术规则（§8.2 原样）

1. **透光浪体规则**：主浪面（非泡沫掩膜区）存在 ≥2 级由深到亮的连续明度阶梯（每级 ΔL ≥8/255、带宽 ≥2% 画幅），阶梯沿浪脊方向单调；泡沫区（高亮高频掩膜）面积 ≤30% 浪体。自查：分区明度直方图 + 阶梯检测 + 泡沫掩膜。（依据：[R12] 透光分析；§1-1）
2. **月光路径规则**：全帧高亮柱（L ≥0.9 且 S ≤0.25 的银白像素）构成**单一连通路径**，自发光体（唯一连通域）延伸至画面下部 ≥40% 画高；路径宽度沿远端收束（近宽远窄，比率 ≥2）；无第二发光体、无第二高亮柱。自查：连通域 + 路径追踪 + 宽度比。（依据：§1-2；[R12] 夜曲）
3. **低地平线规则**：开放海景帧地平线位于画面**下 1/3 带**（0.55–0.75 画高区间，自顶算 ≥55% 处）；天/海面积比 ≥1.2；天海交界线水平度 ±1.5°。自查：线检测 + 面积比。（依据：§1-3；Крамской「ничего нет, кроме неба и воды」）
4. **泡沫花边规则**：泡沫以**高频细碎结构**呈现（边缘密度 ≥3 倍于浪面区），形态为线网/花边而非实心白块（实心白连通域面积 ≤泡沫总面积 25%）；泡沫只出现在脊线与落点，谷底无泡沫。自查：边缘检测 + 连通域面积分布。（依据：§2-5「разбегающуюся сеть пены」）
5. **双色温规则**：火水档帧内暖族（H 20–60°）与冷族（H 160–230°）面积各 ≥15%，且**暖族集中于光源/光路带、冷族集中于水体**（分区显著）；银灰档例外（全帧饱和 ≤0.25，规则改判「单色档」）。自查：HSV 掩膜 + 分区统计。（对照 C-12：与北斋蓝轴、梵高互补轴预检）
6. **剪影规则**：船只/人物/建筑为深剪影（L ≤25%，细节线 ≤10 条/对象）；人物高 ≤10% 画高、无面部特征；剪影对象与高亮水面的明度差 ≥0.5。自查：对象分割 + 明度统计。（依据：§1-6）
7. **平滑表面规则**：非泡沫区高频纹理能量 ≤ 泡沫区的 1/3；无厚涂阴影（局部对比度与画布纹理均匀）；笔触方向性 ≤弱（方向直方图熵高）。自查：频域能量 + 局部对比。（依据：§1-8「не исправлял раз положенного мазка」）
8. **浪峰定格规则（运动预算）**：动画帧间，浪脊线**不闭合**（无完整落水线）；主浪高度 ≥1/3 画高；帧间浪体位移 ≤2% 画幅/帧（「将落未落」的悬停态）；泡沫位移允许 ≤10%/秒（水在动、势能悬停）。自查：脊线检测 + 光流。（与 C-09 对齐：本档案站「动」侧但取悬停帧）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1/2/4/6 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **浪体透明强度（透光阶梯）**`[归纳]` | 水面不透明：只有泡沫与反光，无透光层 | 单层透光：浪脊 1 级青绿透光 | 多层透光：浪脊 2–4 级透光阶梯＋浪内色渐变（《九级浪》《在浪中》档） | **70%** |
| P2 | **月光/单光源强度（路径柱）**`[归纳]` | 无天体：阴天/雾光（银灰档） | 天体在云后：局部光斑与水面碎光 | 满月/落日＋完整路径柱：发光体 1 个、路径柱贯通 ≥40% 画高 | **60%** |
| P3 | **风暴能量档（штиль/зыбь/буря）**`[归纳]` | штиль：镜面海、无浪峰（镜平档） | зыбь：涌浪/初起风暴（《黑海》档） | буря：风暴/九级浪/拍岸碎浪（浪峰 ≥1/3 画高、泡沫密布） | **65%** |
| P4 | **地平线与天海比**`[归纳]` | 高地平线（≥中线）：港城/岸景为主 | 中线附近：天海均分 | 极低地平线（下 1/3 带）：天空 ≥60%、开放海（《黑海》《在浪中》档） | **60%** |
| P5 | **人造物/人物剪影密度**`[归纳]` | 0：纯海（《在浪中》档） | 1 组远景剪影：帆船/堡/岛（点缀级） | ≥1 组近中景：遇难船/小艇/人群（戏剧档，人物仍 ≤10% 画高） | **40%** |
| P6 | **色温档（火/蓝/银灰）**`[归纳]` | 银灰单色：全帧饱和 ≤0.25（晚年档） | 蓝色海：冷蓝绿体系（1870s голубые марины） | 火水对撞：暖冷双族各 ≥15%、光源带高饱和（1840s–50s 与夜战档） | **55%** |

> **用法**：P1/P3 定「是不是艾瓦佐夫斯基的水」（两条中 ≥1 条 ≥ 中档才成立——纯银灰档可 P1 中档）；P2 定月光能力（「月光海」能力标签的主参数）；P4 定空间工程（开放海必须 P4 ≥ 中）；P5 是叙事层参数（可关，纯海档见《在浪中》）；P6 定色档（火→蓝→银灰是生涯三档，组合时按 C-12 声明色相面积归属）。**越界警报（与 §3.1 对齐，组合实验按此判分）**：① 出现**边缘溶解＋天气当主角＋水不可数**（雾化大气吞掉浪体）→ 越界透纳；② 出现**曲线族/爪状泡沫线/平涂剪影浪**→ 越界北斋；③ 出现**点彩/短笔并置**→ 越界修拉/莫奈；④ **画内单点光落在人脸**、暗部塌陷为深棕黑→ 越界卡拉瓦乔/伦勃朗（本档案的光落**水**上）；⑤ 冰封/冻海为主→ 越界弗里德里希。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 透纳）**（× 透纳；本卡 §3.1 分工条款）：大气事件 vs 水体本身：主角判定／边缘处理／光的作用／水可数性四判据＋边界注（≥2 轴联合）；天气轴二选一或分区
- **分工（vs 北斋）**（× 北斋；本卡 §3.1 分工条款）：浪：线／剪影（版画）vs 透明介质（油画）——判据四条；浪的媒介逻辑二选一（或分区）
- **分工（vs 弗里德里希）**（× 弗里德里希；本卡 §3.1 分工条款）：水的两档：冰封静默 vs 液态能量——水相／人的角色／色调三判据；C-09 站「动」侧
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-05 笔触（平滑侧）／C-09 运动预算（浪体节奏）／C-12 色相面积（火水对撞双色温声明）／C-13 阴影色相（阴影即水色）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/aivazovsky.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
