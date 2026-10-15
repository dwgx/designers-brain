# 埃尔·格列柯 模块卡 — `el_greco`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/el_greco.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **纵向拉长**：焦点人物头身比 ≥9（「拉长到超出可信度」）；晚期画幅高窄（高:宽 ≥2:1）——「完美而不被缩小」
2. **火焰状笔触＋概念性变形**：形体边缘碎化、高频边缘密度 ≥全帧 1.5×；与解剖冲突 ≥2 处而身份锚点保留——「概念性艺术」的自觉纲领
3. **非现实色＋自有光**：酸黄绿／冷蓝／朱红「事件」色；画中从无太阳——人人自带光或反射「不可见光源」，无方向性投影
4. **未定义空间＋云幕隔离＋锯齿上升**：背景熵值低、上部云带、无地平线；群像按锯齿／螺旋向上——垂直性主导、构图重心上移
5. **小头长身蛇形扭动＋拜占庭底色＋肖像**：肩髋反向扭转、手指细长；早期金底平坦色域＋希腊字母签名；肖像面部精确、环境「幽灵般」

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
El Greco-style visionary painting — an elongated, upward-reaching composition of spiritual intensity:
figures stretched along the vertical axis beyond natural proportion — small heads on long swaying bodies,
serpentine twist (figura serpentinata), long thin hands and fingers;
forms dematerialised by a flickering, flame-like brushwork — edges broken into flickers, thin glazes, not impasto;
each figure carries its own light — no sun, no single external source; an inner radiance that bleaches the robes;
unreal, acid colours — sulphurous yellow-greens, cold blues, grey-violet — with a single crimson or scarlet accent;
an undefined space sealed by a curtain of clouds, no landscape illusion, no deep perspective;
figures crowded near the picture plane, zigzag or ascending arrangement;
turbulent grey-green storm sky or an open heaven of pure light;
Byzantine undercurrent: frontal gazes, gold or flat colour fields, Greek-letter inscription, icon-like saints with attributes;
palette: azurite blue, lead-tin yellow, vermilion, madder lake, ochre, red lead, bone white — seldom natural ultramarine;
brush: thin glazes over a grey underpainting, rough and unmixed passages, red ground showing through;
devotional, ecstatic, weightless — saints, martyrs, the Virgin, heavenly visions
[late style variant] figures elongated beyond credibility, colours bleached white-hot, space dissolved in light
[portrait variant] bust-length portrait, precise observation, black and white dress with one colour note, spectral plain background, rhetorical hand gesture
```
**负向约束（`--no` 风格）**
```
--no realistic anatomy and proportion, naturalistic daylight, deep linear perspective with vanishing point, landscape detail,
hard cast shadows from a single light source, heavy chiaroscuro with near-black background, impasto relief with palette-knife texture,
complementary-colour vibration across the whole canvas, photographic skin tones, smooth sfumato, cheerful pastoral scenes,
genre anecdote, still life, decorative gold ornament, flat cartoon vector, text watermark, 3D render, anime
```

## 代码艺术规则（§8.2 原样）

1. **拉长规则**：焦点人物实例分割框**高/宽比 ≥3.5**；人脸框高 ÷ 人物框高 **≤0.11**（≥9 头身）。自查：人体关键点 + 实例分割框比例计算。（依据：[R3] elongated beyond credibility；[R7] 拉长句）
2. **火舌笔触规则**：形体轮廓外 2% 环带内高频边缘密度 **≥ 全帧均值 1.5×**；边缘连通段中位长度 ≤ 短边 1.5%（碎化）；无厚涂（法线/浮雕强度低）。自查：边缘检测 + 连通域统计 + 表面法线估计。（依据：[R3] flickering brushwork；[R6] llameantes；[R7] Pacheco）
3. **非现实色规则**：≥2 个面积 ≥5% 区块落于酸黄绿（H 60–90°, S 0.3–0.6）或冷蓝（H 200–230°, S 0.3–0.7）；红色（H 0–15°）面积 ≤12% 但为全帧**最高饱和**；全帧中位饱和 ≤0.55。自查：HSV 掩膜 + 面积统计。（依据：[R3] unreal colors；[R6] ácidos/incandescentes）
4. **自有光规则**：阴影方向一致性 ≤0.3（无方向性投影）；人物区域亮度均值离散度 ≤0.15（人人被照）；高光（V>0.95）连通域 ≥4 且分散。自查：阴影方向场 + 分区亮度统计。（依据：[R5][R6] 不可见光源/无太阳；与 C-01 对齐：站「无硬阴影」侧）
5. **云幕/未定义空间规则**：背景区域纹理熵 ≤ 全帧均值 0.7×；地平线检测命中 ≤1 条弱线；透视收敛线索 ≤2 组。自查：熵图 + 直线检测。（依据：[R6] 云幕隔离的未定义空间）
6. **形体连续性规则**：人物轮廓**连续无断裂**（断裂点 ≤1 处且非结构性）；无面片拼接边（直线折角段计数 = 0）。自查：轮廓跟踪 + 折角检测。（依据：[R3] 概念性而非解构；与 §3.1 vs 毕加索判据同轴）
7. **上升/飘浮动态规则（视频帧）**：光流主方向向上（平均 v_y < 0；|v_y| 中位数 ≤1.5% 短边/帧）；形体沿轴缓慢上升；「闪烁」允许局部高频振荡（振幅 ≤1% 短边）。自查：光流场直方图。（与 C-09 对齐：站「弱上升场」侧——介于冻结与全画面场之间）
8. **酸色 + 红事件规则（色相预算）**：主色相族 ≤3（蓝 / 黄绿 / 灰紫）+ 红事件 ≤12% 面积且饱和度最高；无互补对全幅 1:1 振动。自查：色相直方图 + 面积预算。（与 C-12 对齐：蓝为罩染层积、非平涂大色域）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–6 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **拉长度（elongation）**`[归纳]` | 自然比例（意大利期档：《净化圣殿》《治愈盲人》） | 拉长 1.2–1.4（《三位一体》《奥尔加斯》档） | 「超出可信度」：头身比 ≥10（《无原罪》《第五封印》档） | **65%** |
| P2 | **火焰化笔触（flickering）**`[归纳]` | 平滑罩染、边缘干净（早期/肖像档） | 可见碎笔触 + 罩染（成熟期） | 火舌状、形体解材化（晚期档） | **55%** |
| P3 | **非现实色强度**`[归纳]` | 土色/自然色主导（意大利期） | 酸色对比出现（青绿/黄/冷蓝 + 红事件） | 漂白 + 荧光酸（晚期白炽化） | **55%** |
| P4 | **自有光强度**`[归纳]` | 环境光（早期） | 局部光晕/背光（成熟期） | 人人自带光、光源不可见、白炽（晚期） | **60%** |
| P5 | **空间压缩/云幕**`[归纳]` | 有景深/建筑背景（早期、部分肖像） | 背景简化、地平线模糊 | 未定义空间 + 云幕 + 人物拥挤贴面 | **55%** |
| P6 | **系列/版本性**（工作流参数）`[归纳]` | 单件 | 少数变体（同题 2–3 版） | 系列化（12 使徒 / 圣方济各 ~100 幅档） | **1**（单幅起步） |

> **用法**：P1/P2/P4 定「是不是格列柯」（三条中 ≥2 条 ≥ 中档才成立）；P3/P5 定时期档（意大利化 → 成熟 → 晚期白炽的滑轨）；P6 是组稿参数（单幅 vs 系列，不进画面重叠计算，按 `expansion.md` §4.3 规则 5 归「工作流参数」栏）。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若扭曲改为**压缩/波动**且题材转世俗心理 → 越界进入**蒙克**档；② 若变形改为**面片拆解 + 多视点**、色彩转近单色 → 越界**毕加索**档；③ 若出现**画外单光源 + 近黑背景 + 高光只落脸手道具** → 越界**卡拉瓦乔**；④ 若表面转为**厚涂能量场 + 互补对振动** → 越界**梵高**。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 蒙克）**（× 蒙克；本卡 §3.1 分工条款（与 munch.md §3.1 对称互锁））：扭曲两路：宗教狂喜（纵向拉伸＋上升）vs 焦虑内爆（压缩／波动／倾斜）——判据四条；冲突时以「扭曲方向」为准
- **分工（vs 毕加索）**（× 毕加索；本卡 §3.1 分工条款）：变形两路：单视点连续拉伸 vs 面片拆解＋多视点——判据四条；不得机制混写（同谱系两端）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01 硬阴影（光为内在／不可见光源，与卡拉瓦乔不同轴）／C-05 笔触／C-09 运动预算／C-12 色相预算

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/el_greco.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
