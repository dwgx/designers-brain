# 马奈 模块卡 — `manet`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/manet.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **取消中间调**：中间调带（V 0.40–0.65）≤25%、亮暗过渡带 ≤1% 短边——大块亮／暗直接咬合，「没有半调子」
2. **平面化空间＋黑是主色**：消失点 ≤1（强档 0）、背景贴住人物；深色（V ≤0.2）面积 15–40%、黑区内部平整（std ≤0.06）
3. **色域收窄＋色斑组织**：高饱和 ≤10%、连通域 1–3（斗牛红／吧台橙）；对象读作「一块色斑」——细节 ≤2 类／对象（Zola）
4. **alla prima＋正面光**：宽笔湿接湿、色层 ≤3、笔触覆盖 ≥60%（黑部干净大平涂）；面部被正面光「洗亮」、阴影 ≤15%
5. **日本版画式裁切＋直视观众**：主体被裁切 ≥1 处、强对角线 ≥1；正面／直视目光（挑战性）；题材全为当下——现代生活观察

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Manet-style modern-life painting — alla prima, flat and frontal:
a scene from contemporary Paris (1860s–1880s) — a café-concert, a balcony, a garden, a bar, a railway, a boating party — observed from life;
space compressed and flattened: figures push forward close to the picture plane, the background is a shallow wall of muted colour, no atmospheric depth, perspective reduced or ignored;
mid-tones suppressed: lights and darks meet abruptly, faces and figures look lit by a flat frontal light, shadows almost eliminated (peinture claire); no chiaroscuro, no half-tone transitions;
a restricted palette — black, white, grey, browns, earth tones — with one to three saturated accents (a red cap, a green railing, orange fruit, a pink dress); black used as a colour of area, not as darkness;
broad visible brushwork laid in once, wet-in-wet; black areas kept flat (aplats), whites loaded; each figure simplified to a few frank patches (taches);
edges blurred only where wet paint met wet paint; details omitted, everything abridged;
composition cropped like a Japanese print: figures cut by the frame, a strong diagonal, asymmetrical balance, a mirror or railing as a device;
the modern subject looks out with a direct, unembarrassed gaze;
19th-century oil on canvas, museum quality
```

**负向约束（`--no` 风格）**
```
--no chiaroscuro, sfumato, half-tone gradients, soft modelling, deep atmospheric perspective, aerial recession,
smooth invisible brushwork, academic finish, glossy varnish, multi-layer glazing,
bravura performance strokes, society-portrait glamour, elongated elegance,
decorative flat colour blocks, pure high-key flat tints, pattern-equals-figure wallpaper, cut-paper edges,
single candle-lit spotlight, near-black background, dramatic tenebrism,
impressionist atmospheric envelope, fog-like unifying light, pastel colour haze,
sentimental narrative, mythological or allegorical framing,
digital smoothness, airbrushed skin, photo-bash, 3D render, cartoon, text
```

## 代码艺术规则（§8.2 原样）

1. **中间调压缩规则**：直方图中带（V 0.40–0.65）面积 **≤25%**；亮/暗双峰可辨（峰间距 ≥0.25）；无宽渐变带（过渡带 ≤1% 短边）。自查：明度直方图 + 双峰检测。（依据：[R7]「contrastes brutaux」；[R25]「did away with most half-tones」）
2. **平面化空间规则**：背景梯度层 ≤2；消失点 ≤1（强档 0）；人物轮廓与背景明度差 ≥15%、边缘可描。自查：区域分割 + 消失点估计 + 边缘对比。（依据：[R2]「close to the picture plane」；[R7]「profondeur absente」）
3. **黑色预算规则**：深色（V ≤0.2）面积 **15–40%**；黑区内部标准差 ≤0.06（平整，非细碎渐变）。自查：暗区面积 + 局部方差。（依据：[R14]「blacks and greys」；[R8]「aplats」）
4. **色域与点缀规则**：主色族 ≤5（黑/白/灰/棕 + 1–2 家族）；高饱和（S ≥0.6）面积 **≤10%**、连通域 1–3。自查：色相聚类 + 饱和度直方图。（依据：[R2]「restrained color scheme」）
5. **笔触可见性规则**：可见笔触覆盖 **≥60%**；色层 ≤3（alla prima，无多层罩染）；笔触方向族 2–5 个。自查：边缘方向场 + 梯度带。（依据：[R23]；[R24]「abridged」）
6. **正面光规则**：面部阴影面积 **≤15%**；无单侧硬阴影（亮暗分界无强方向性）；允许 1–2 px 湿接湿融合带。自查：面部区域明度分布。（依据：[R15]「peinture claire」）
7. **裁切与装置规则**：主体被画框裁切 **≥1 处**；强对角线 ≥1；对称装置（镜面/栏杆/舞台框）≤1 且承担构图任务。自查：边缘相交检测 + 线检测。（依据：[R4] 日本版画；[R30] 镜面）
8. **题材与视线规则**：当代生活题材（可点检道具 ≥2：咖啡馆/酒杯/船/栏杆/铁路）；≥1 人物直视观众（或明确的「观察者」视点）。自查：道具检测 + 视线估计。（依据：[R1] 现代生活；[R6]「défie de son regard」）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–8 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **中间调压缩度**`[归纳]` | 保留较完整明暗过渡（早期学院档） | 中间调明显压缩、亮暗对比增强（肖像/阳台档） | 亮暗直接并置、过渡带近乎消失（《吹笛少年》/《奥林匹亚》档） | **70%** |
| P2 | **平面化程度**`[归纳]` | 保留体积与纵深（风景/海景档） | 背景压平、人物简化（《阳台》档） | 全画面平面化、透视取消（《吹笛少年》档） | **60%** |
| P3 | **黑/深色预算**`[归纳]` | 少黑（亮调档：《划船》/《阿让特伊》类） | 黑色为深色骨架（肖像档） | 大面积黑（西班牙装束/吧台女黑裙档） | **55%** |
| P4 | **色域宽度**`[归纳]` | 多色高调（Argenteuil 档） | 收窄：黑/白/灰/棕 + 2–3 处纯色（主档） | 近单色 + 单点饱和（《吹笛少年》红黑档） | **50%（收窄档）** |
| P5 | **笔触显现度（alla prima）**`[归纳]` | 平滑收笔（少数完成度极高局部） | 可见、干脆的宽笔（主档） | 色斑/宽涂组织全画（《吧台》档） | **65%** |
| P6 | **构图装置（裁切/对称）**`[归纳]` | 完整构图、正对（肖像档） | 轻微裁切/偏轴（阳台档） | 日本版画式强裁切 + 对称装置（《划船》/《吧台》镜面档） | **55%** |

> **用法**：P1 + P2 定「是不是马奈」（≥2 条 ≥中档才成立）；P3 + P4 定「西班牙/黑档 vs 亮调档」；P5 定完成度档；P6 定构图档（P1–P6 均进画面重叠计算）。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若笔触转向**表演/完成**、空间**保持体积**、中间调**完整过渡** → 越界进入**萨金特**档；② 若平面变为**纯色平涂/无明暗**、色纯度每块 ≥70%、图案与主体同权 → 越界进入**马蒂斯**档；③ 若出现**画外单光源 + 近黑背景 + 光斑只落脸/手/道具** → 越界**卡拉瓦乔**档；④ 若出现**大气包络**（远景对比下降、雾色统一全画） → 越界**莫奈**档。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 萨金特）**（× 萨金特；本卡 §3.1 分工条款（对侧互查一致））：alla prima 两条路：平面组织 vs 表演／完成——四轴＋判据四条；alla prima 为共享技艺、区分在功能（N3）
- **分工（vs 马蒂斯）**（× 马蒂斯；本卡 §3.1 分工条款（唯一正本））：平面的两条路：写实平面化 vs 装饰色块——四轴＋判据四条；平面化程度轴单主
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-03 中间调／C-12 色相预算／C-05 笔触

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/manet.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
