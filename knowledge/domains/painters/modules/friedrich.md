# 弗里德里希 模块卡 — `friedrich`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/friedrich.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **Rückenfigur（背影人物）**：背向/近背向、面部不可辨、位于中轴或黄金分割——「首先是一次观看的反思」
2. **静默与静止（无动作）**：人物站/坐/倚、无叙事性动作与交流；全画无运动模糊类笔触——画面时间被拉长为「停留」
3. **层带式构图＋空间阻隔与剪影对撞**：≥3 条水平带（陆/海/天）、天空占比常 ≥1/2；前景 ≥1 深色剪影体与远景隔开、无单点透视轴、中景常缺
4. **人物—尺度渺小化＋对称中轴几何**：人形 ≤ 画高 1/6、群体 ≤3 人；对称/重复/平行位移、三角形与对角线；中轴由人物或建筑锁定
5. **逆光剪影＋冷调暮色＋象征装置库＋雾海雪包络**：光源在天空带（落日/月/晨光）、人形明度 < 背景；蓝灰/褐/赭/淡金低饱和；十字/哥特废墟/枯橡/墓/锚可点检；大气现象 ≥1/3

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Friedrich-style contemplative landscape — the sublime observed, not enacted:
a single figure (or two) seen from behind, small against an immense nature, still and contemplative,
face hidden, dark silhouette; the viewer placed at the figure's shoulder;
nature stratified into broad horizontal bands — land, water, sky — with clean, level divisions;
a low foreground barrier (shore, rock ledge, wall, gate) separating us from the depth;
no conventional perspective axis — mountains and slopes fall toward the central vertical;
dawn or dusk: light comes from the sky, a pale gold band under blue-grey clouds,
long still water, mist veils and snow haze in smooth tonal gradations;
muted narrow palette — slate blue, grey-green, earth brown, ochre, pale gold, bone white;
one quietly legible symbolic element: a cross on a rock, a Gothic ruin,
a bare oak, a gravestone, an anchor; diffuse ambient light, no hard shadows;
matte, thin, drawing-like paint surface with precise small details;
silence and duration — a pause that lasts
```
**负向约束（`--no` 风格）**
```
--no dramatic action, storm or weather event, turbulent waves, speed, swirling energy,
hard cast shadows, single spot light, chiaroscuro, theatre lighting, glossy varnish reflections,
bright saturated colours, complementary-colour vibration, impasto fireworks, decorative gold,
crowds, narrative anecdote, genre scene, readable faces, portrait likeness,
urban night, artificial light, neon, deep linear perspective, theatrical stage,
photorealistic skin, cartoon, anime, 3D render, HDR gloss
```

## 代码艺术规则（§8.2 原样）

1. **Rückenfigur 规则**：焦点人形**背向**（人脸关键点命中 ≤1 组、五官不可辨）；位于中轴 ±10% 画宽；多人时 ≤3 人且同一朝向。自查：人脸关键点检测 + 实例分割 + 中轴度量。（依据：[R5]「看一个观看者」；[R1] Rückenfigur 主题化）
2. **冻结规则**：视频帧间全局光流 Δ ≤0.5%/帧（事件外）；无运动模糊核；仅允许雾带/水面的极慢渐变（局部光流 ≤2% 短边/秒）。自查：光流场 + 模糊核检测。（与 C-09 运动预算对齐：弗里德里希站「冻结」侧）
3. **层带规则**：检出 **≥3 条水平带边界**（倾角 ≤3°）；天空带面积占比 ≥40%；单带内边缘密度 ≤全帧均值的 0.8 倍。自查：边缘方向直方图 + 水平带分割。（依据：[R7]「陆/海/天三元素」）
4. **无透视轴规则**：单消失点引导线 = 0；山棱/岸线走向向中轴收束（左右向心斜线对 ≥1 组）。自查：Hough 直线 + 消失点估计。（依据：[R5]「Mittelsenkrechte 与两侧坠落山棱」）
5. **逆光剪影规则**：人形/前景剪影的明度中位 < 全帧明度中位 − 0.15；光源质心位于天空带（上 1/3）；**无画内单点光源**（高亮连通域 ≥2 或成带状）。自查：亮度质心 + 剪影分割。（依据：[R5][R7]）
6. **冷调低饱和规则**：全帧中位饱和 ≤0.35；蓝灰（H 180–240°）/ 褐（20–45°）/ 赭金（35–55°）三族合计面积 ≥80%；饱和 ≥0.85 的区块（≥3% 面积）数量 = 0。自查：HSV 掩膜统计。（对照 C-12：与梵高互补对/北斋蓝形成轴差）
7. **象征点检规则**：≥1 个象征元素在场（十字/哥特废墟/枯橡树/墓/锚 五类可点检）；象征物面积 ≤5% 画布、且位于中轴 ±15% 或天际线带内。自查：对象检测 + 位置度量。（依据：[R2] 象征清单；[R1] 哥特=最明确象征）
8. **软光与雾面规则（无硬阴影 + 点彩）**：阴影边界梯度带宽 ≥2% 短边（软过渡）；暗部 V ≥0.05（**不出现纯黑大块**）；镜面高光（V≥0.95 且面积 >1%）数量 = 0；雾/雪区高频能量集中于 2–8px 尺度带（点彩纹理可见）且整体梯度平滑（低频占优）。自查：梯度带宽 + 直方图 + 多尺度能量比。（对照 C-01：与卡拉瓦乔/米开朗基罗硬阴影侧的显式互斥；依据：[R9] Smalte 点彩；[R4] Punktreihen）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–5 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **背影化强度（Rückenfigur）**`[归纳]` | 无人物纯风景（《冰海》《瓦茨曼》档） | 1 个背影或 ≤3 人小群体（《月下双人》《吕根白垩崖》档） | 单背影居中轴、全画锚点（《雾海漫游者》档） | **70%** |
| P2 | **尺度比（人物 vs 风景）**`[归纳]` | 人物 ≥1/4 画高（近景肖像性） | 1/6–1/8 画高 | ≤1/10 画高（渺小化；《海边僧侣》档） | **60%** |
| P3 | **静默度（运动预算）**`[归纳]` | 云/水有可感动势（早期档） | 全画静止，仅雾带/水面极慢渐变 | 完全冻结——除光色不动（《海边僧侣》档） | **75%** |
| P4 | **层带结构强度**`[归纳]` | 2 带（前/后两段式） | 3 带（陆/海/天 或 前/中/远） | ≥4 带 + 明确空间阻隔（墙/门/坡沿切断） | **60%** |
| P5 | **光色档（时刻与反差）**`[归纳]` | 日间高调、色域偏亮（写生档） | 暮色/晨光冷金、中等反差 | 近黑剪影 + 发光天空、高反差（《海边僧侣》《冰海》档） | **55%** |
| P6 | **象征装置密度**`[归纳]` | 0–1（纯自然档） | 1–2（十字/废墟/枯树之一二） | ≥3（十字 + 哥特废墟 + 墓/枯橡树） | **50%** |

> **用法**：P1/P2/P3 定「是不是弗里德里希」（三条中 ≥2 条 ≥ 中档才成立）；P4/P5 定时刻与结构档（日间写生 → 暮色凝视 → 夜/冬的极端）；P6 是象征层参数（可关）。**越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若出现**单点硬光 + 戏剧投影** → 越界卡拉瓦乔；② 若转为**全画能量场/漩涡/天气事件** → 越界透纳；③ 若出现**人造光/都市几何/夜街** → 越界霍珀；④ 若人物**无脸扭曲 + 非现实色区** → 越界蒙克；⑤ 若地点可辨且象征归零、天空为气象记录 → 越界康斯泰勃尔。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 透纳）**（× 透纳；本卡 §3.1 分工条款）：崇高两档写死：凝视档（冷——冻结＋层带＋凝视者）vs 事件档（热——风暴/浪/蒸汽/边缘溶解）——判定须 ≥2 轴联合成立
- **分工（vs 康斯泰勃尔）**（× 康斯泰勃尔（future）；本卡 §3.1 分工条款）：精神化档（地点合成/象征密度高/背向凝视）vs 观察档（特定地点忠实记录/云研究/劳作人物）——判据四条
- **分工（vs 蒙克）**（× 蒙克；本卡 §3.1 镜像确认）：自然的身份：神性的崇高 vs 焦虑的症状——与 munch.md §3.1 互为对侧
- **分工（vs 普桑）**（× 普桑（future）；本卡 §3.1 分工条款）：浪漫的建构（层带阻隔＋中景空缺＋凝视者）vs 古典的舞台（纵深可读为完整舞台＋历史行动者）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01（漫射天光、无硬阴影）/ C-09（站「冻结」侧）/ C-12（冷调低饱和、天空带主导）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/friedrich.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
