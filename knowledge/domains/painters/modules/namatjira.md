# 纳马吉拉 模块卡 — `namatjira`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/namatjira.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **白干桉（ghost gum）剪影**：近垂直白干＋分叉枝、明度 ≥85%（纸白＋极淡灰）——树可裁切为「肖像」
2. **远山转色（距离色）**：中远景山体色相随距离向紫/蓝位移（红褐→紫灰→蓝紫）、明度对比随距离下降
3. **高地平线＋层带构图**：山体占画面上半为主、天空带 ≤40%；前景树/岩—中景河床滩地（水为枢纽）—远景山体三带
4. **透明水彩分层＋铅笔/石墨底稿可见**：同一区域变体淡彩叠加、色层薄而透无厚涂；山脊线与树位有底稿痕
5. **土色系色域＋天空空场＋署名不署日期**：赭红/土黄/紫灰/深蓝/纸白、无互补对撞；深蓝或晨昏纯色天空、云 ≤15%；右下「ALBERT NAMATJIRA」、馆藏记 Not dated

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**

```
Mid-century Central Australian watercolour landscape in the Hermannsburg School register: transparent
watercolour over a faint graphite underdrawing on watercolour paper; a high horizon compresses the
scene into stacked bands — foreground trees or rocks, a middle ground of dry riverbed, waterhole or
flood-scoured flats, and ranges with isolated peaks lifted against an empty sky; distance shifts
colour as it recedes — red-brown ridges step back into mauve, violet and blue-grey, contrast dropping
with each step; one or two white-trunked ghost gums stand as near-silhouettes, bark folds reading like
skin and branches like arms, a tree sometimes cropped like a portrait at the frame's edge; the sky is
a broad unclouded field of deep blue, or a dawn/dusk gradient that ignites the rock faces; iron-red
gorge walls glow orange only where the noon sun strikes them directly; water appears as a mirror for
the sky or a pale scar across the riverbed; the palette stays in the earth register — ochre reds,
earth yellows, violet greys, deep blues and paper white; pigment is laid in repeated, varied thin
washes, one colour at a time, returned to again and again until all parts of the composition hold in
balance; matte paper surface, no varnish, no gloss, no heavy impasto; quiet static light fixed at one
moment of day, no weather event, no figures or only distant incidental ones; the land itself is the
portrait — named country, held in stillness
```

**负向约束（`--no` 风格）**

```
--no storm, squall, rain, snow, dramatic weather event, swirling fog, dissolving edges, steam, smoke,
speed, motion blur, atmospheric chaos, turbulent sky, oil-painting impasto, thick texture, palette
knife, opaque gouache coverage, glossy varnish, saturated complementary-contrast pairs, neon colours,
firework sunset, night scene, artificial light, city, buildings, motor vehicles, power lines, fences,
figures in ceremony, sacred or ceremonial motifs, dot painting, boomerang or dreamcatcher clichés,
generic outback stock imagery with kangaroo and emu icons, text, watermark, signature, lettering,
frame, borders, collage, 3D render, HDR, photorealistic photograph, glossy AI look
```

## 代码艺术规则（§8.2 原样）

| # | 规则 | 可判定阈值（默认） | 自查方法 |
|---|---|---|---|
| 1 | **远山色相位移** | 远景带（画面上 1/3 山体区）平均色相 vs 前景带位移 ≥25°（向蓝紫）；明度对比逐带递减 | 分带色相直方图 + 带间 ΔH 计算 |
| 2 | **地平线与层带** | 地平线位于画面高度 35–60%（自上而下计）；层带 ≥3 条（前景/中景/远景）；天空带 ≤40% | 水平边缘检测 + 带划分 |
| 3 | **色数预算（土色系）** | 同屏色相簇 ≤7（赭红/土黄/紫灰/深蓝/纸白 + ≤2 点缀）；饱和度均值 ≤55%、峰值 ≤75%；互补色对撞面积 ≤10% | 逐帧直方图 + 色相聚类 |
| 4 | **白干桉剪影** | 树档：≥1 株近垂直白干（值 ≥85%、干宽 ≤4% 画幅、分叉 ≥2）；非树档允许 0 株但须有山体剪影（轮廓可辨） | 连通域明度筛选 + 形状检查 |
| 5 | **天空空场** | 天空区域 ≥20% 画幅；云覆盖 ≤15%；无事件性云型（积雨云/风暴云纹理） | 分块明度/纹理统计 |
| 6 | **分层罩染可见度** | 岩面/山体每块 ≥3 个明度台阶（步长 ≤12%/级），无单色平涂大块；可选档：检出底稿线残留 | 明度分层计数 + 边缘图（可选） |
| 7 | **静场运动预算** | 视频档：无天气运动；仅允许 ≤1%/s 的光色慢调制；帧间差 ≤1.5%；无溶解/位移 | 帧差图 + 调制曲线拟合 |
| 8 | **文化合规检查** | 素材与语义清单核对：神圣/仪式专属元素 0 个；人物 0–2 个且非仪式场景；无文字/签名/品牌；无冒充署名 | 清单对照 + OCR 扫描 |

> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；与 `templates/style_card.md` 的填写规则对齐。第 8 条为本模块特有的伦理验收项（与档案头部"文化伦理声明"配套）。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **远山转色度**（Distance Colour Shift）`[归纳]` | 远山仍红褐（近色，无距离位移） | 紫灰一档（红→紫灰） | 远山紫蓝、与前景土红形成明显色相位移（≥25°） | **75%** |
| P2 | **白干桉在场度**（Ghost Gum Presence）`[归纳]` | 无树或树仅为远处剪影 | 1–2 株中景树（占画面 ≤1/6） | 前景大株"树肖像"（裁切、白干占画面 ≥1/4） | **60%** |
| P3 | **天空空场度**（Sky Emptiness）`[归纳]` | 云层丰富（≤1/4 空场） | 少量条云、天空半开 | 深蓝或晨昏纯色空场（云 ≤15%） | **70%** |
| P4 | **峡谷红壁光**（Gorge Light）`[归纳]` | 阴影平涂（无受光逻辑） | 单侧受光（晨/夕斜光） | 正午全亮红橙（"舞台幕布"档） | **50%**（需要时切 90%） |
| P5 | **地平线高度**（Horizon Height）`[归纳]` | 低地平线（天空 ≥1/2，非其招牌） | 地平线约 1/3（天空 30–40%） | 高地平线（山体占 ≥2/3、层带压缩） | **60%** |
| P6 | **罩染层数**（Wash Layering）`[归纳]` | 单层平涂（一遍过） | 2–3 层叠加 | 同一区域 ≥4 次回到（variant washes 平衡法） | **65%** |

> 用法：**P1＋P5 定"是不是纳马吉拉"**（远山转色＋高地平线）；P2 切"树肖像档"（单株大特写）与"全景档"（无树/远树）；P3/P4 切时刻与峡谷档；P6 定"水彩层次"的厚薄。三档描述可直接作判定标准写进自查表。
> 数据来源：档位阈值为 `[归纳]`（本项目操作化建议，未经渲染实验校准）；特征观察取自 [R1][R2][R6][R7][R8]。
> **分工注（与康斯泰勃尔/透纳，必须写死）**：P1 强档（远山紫蓝位移）＋P3 强档（空场天空）是本模块专属；**"湿润农事地点＋云型系统研究"整体属于康斯泰勃尔档、"事件光色＋边缘溶解"整体属于透纳档，禁止在本模块同档出现**（见 §3.1 与 §8.1 越界警报）。本注为 `[归纳]`。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 康斯泰勃尔）**（× 康斯泰勃尔（future）；本卡 §3.1 分工条款）：水彩风景两档写死：干旱岩质亲属制乡国（几乎无人＋深蓝空场）vs 湿润农事牧歌（云型系统研究＋劳作人物）——地点系统二选一
- **分工（vs 透纳）**（× 透纳；本卡 §3.1 分工条款）：光的身份：具象土地档（静、地名、剪影清晰、色层可点）vs 事件光色档（热、动、边缘溶解）——70/30 选主导轴
- **对照（vs 恩格瓦雷）**（× 恩格瓦雷；本卡 §3.1 次级注）：具象水彩风景 vs 全幅符号/大地抽象——默认不组合，如组合须显式分区（[推测] 级对照，仅记录）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01（软边水彩、无硬阴影）/ C-09（站「静场」侧）/ C-05（淡染层、笔触弱于油画厚涂档）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/namatjira.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
