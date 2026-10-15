# 皮耶罗·德拉·弗朗切斯卡 模块卡 — `piero_della_francesca`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/piero_della_francesca.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **几何即构图（轴线/对称/比例）**：主轴线贯穿 ≥80% 帧高、左右视觉质量差 ≤15%；关键元素落网格交点/分割线；场景间对称呼应
2. **透视盒（可测空间）**：消失点 ≤2、地砖可数行、进深可推算——「精确的透视空间表现」为标志
3. **均匀白昼光＋几何化投影**：投影方向夹角 ≤10°、影长 ≤物高 25%、无大面积深黑；影按透视法则计算并引导视线（最早实践者之一）；夜景档画内光源（天使发光）
4. **浅色珍珠调＋静止无表情**：全帧平均饱和 ≤0.35、明度中位 ≥0.55、高饱和 ≤3%；动作冻结中途、面孔不做表情（timelessness）；同款宁静脸型跨作品复用
5. **几何化自然与建筑＋侧面像/徽章肖像**：云/树冠/山体低多边形化（轮廓拐点 ≤6 段）、建筑是空间标尺（直线元素 ≥30% 画面）；双联画古钱币式正侧面（偏转 ≥80%）、背景地平线连续

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Piero della Francesca style — measured geometry and mathematical light:
a calm stage built on a perspective grid; the composition locked to a central axis —
figures, architecture and landscape aligned on strict verticals and simple ratios;
space constructed, not suggested: a coffered barrel vault, an arcade of classical columns,
a scallop-shell apse with an ostrich egg hanging at its centre, a tiled floor receding to
one or two vanishing points; bodies simplified into quiet geometric volumes with clear,
continuous contours — almost no visible brushwork, matte tempera or fresco surface;
one even, clear daylight washing the whole scene, short soft shadows whose direction is
computed and consistent; a cool pearl palette — pale blue sky, grey-green fields, chalky
flesh laid over a green-grey underpainting, faded rose, muted crimson and ultramarine
accents, gold rarely and precisely placed; faces impassive and timeless — one serene
facial type — gestures frozen mid-motion, hands exact and still; landscape reduced to
geometric hills, a winding river, a small walled town, trees as vertical accents;
stillness, silence, ceremonial order; sacred narrative set in a recognizable Tuscan valley
[night variant] the whole scene lit by a single luminous body inside the picture —
an angel descending with a cross, radiating light that falls off smoothly into the
darkness; only the tent and the sleeping guards emerge from the dark
```
**负向约束（`--no` 风格）**
```
--no sfumato haze or smoky blending, no soft dissolving edges, no impasto, no palette-knife
texture, no dramatic chiaroscuro or single-spot tenebrism, no near-black background,
no visible brushstrokes or impressionist dabs, no hatching, no high saturation or neon
colours, no multiple light sources, no inconsistent shadow directions, no movement blur,
no exaggerated or grimacing expressions, no twisting muscular bodies, no baroque
turbulence, no cartoon, anime, 3D render, photographic HDR
```

## 代码艺术规则（§8.2 原样）

1. **轴线与网格规则**：画面含 **≥1** 条贯穿性垂直主轴（贯穿 ≥80% 帧高）；主要人物质心与轴线水平偏差 **≤2%** 帧宽；若有地面，网格/地砖行可数 **≥6** 行且近大远小单调。自查：列梯度投影 + 质心检测 + 地砖行计数。（依据：[R1] "the strict alignment of the dove, the bowl and Christ's praying hands"；网格结构）
2. **透视收敛规则**：建筑/地面直线元素向 **≤2** 个消失点收敛，拟合角度误差 **≤1.5°**；进深方向尺度比单调递减。自查：Hough 直线拟合 + 消失点求交。（依据：[R18] "precise perspective representation of space"；[R11] 贝壳穹顶可推算）
3. **光一致规则**：全帧投影方向夹角 **≤10°**；阴影长度 **≤物高 25%**（低斜度光）；无第二主光源（亮度次峰 ≤主峰 30%）。自查：阴影区域方向直方图 + 影长比。（依据：[R19] 影的透视计算；[R1] 晨光浅影）
4. **画内光源规则（夜景档）**：夜景中全帧最亮连通域中心与可见发光体（天使/灯）距离 **≤5%** 帧宽；亮度沿距离**单调衰减**（径向拟合 R² ≥0.8）。自查：亮度场径向衰减拟合。（依据：[R16] "illumined by the light which proceeds from the angel himself"）
5. **浅色域规则**：全帧平均饱和度 **≤0.35**、明度中位 **≥0.55**；高饱和像素（S>0.75）面积 **≤3%**；主色相（面积 ≥2% 者）**≤5** 个。自查：HSV 统计。（依据：[R1] "pale tones"；[R2] 蛋彩→油彩的饱和度变化）
6. **静止规则**：无运动模糊（模糊核 ≤1px，光流残差 ≤1px）；群像姿态镜像对称度 **≥70%**（若为对称构图）；直视画外者 **≤1**。自查：光流 + 镜像匹配 + 视线检测。（依据：[R14] "immobilità cerimoniale"；[R1] "find stillness"）
7. **几何轮廓规则**：云/树冠/山体轮廓可用 **≤6** 段折线近似（低多边形度）；建筑直线元素占比 **≥30%**；无碎片化高频轮廓。自查：多边形近似误差 + 直线占比。（依据：[R1] 鸽子前缩翅膀与云同形；[R6]）
8. **投影几何规则**：**≥1** 处影子为可读几何形（圆/椭圆/多边形），其形状与光源方向自洽（误差 **≤15%**）；影可与主体构成视线路径（人工核）。自查：影子形状拟合 + 光向一致性。（依据：[R20] "the shadow cast by Jerome's legs that leads the eye … to the pages in his open book"）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；2/3/8 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **几何秩序度**（Geometric Order）`[归纳]` | 自由构图、局部对称（战场群像档） | 主轴线 + 局部网格（群像/叙事档） | 全画轴线/对称/比例分割（受洗/复活/圣母档） | **70%** |
| P2 | **透视深度**（Perspective Depth）`[归纳]` | 浅空间、背景装饰化（部分晚期小型板画） | 单点透视 + 地砖/建筑线可读（肖像/圣像档） | 可测深度：多层建筑盒、进深可推算、贝壳穹顶级（鞭笞/布雷拉档） | **75%** |
| P3 | **光的行为**（Light Behavior）`[归纳]` | 侧向浅影（低斜度晨光档） | 均匀漫射白昼光（多数圣像档） | 均匀光 + **投影链几何化**（影作构件；圣杰罗姆档）／显式切换：**夜景档**（画内点光源=天使之光，君士坦丁档） | **中（白昼均匀）** |
| P4 | **色域与表面**（Palette & Surface）`[归纳]` | 局部重色/深色点缀（早期蛋彩档） | 浅色为主 + 局部饱和点缀（受洗/圣诞档） | 全画珍珠浅调：低饱和、高明度、绿灰底（晚期油彩档） | **70%** |
| P5 | **静止与表情度**（Stillness & Expression）`[归纳]` | 动态人群（战场/叙事多动作档） | 静立人物、动作冻结（多数档） | 完全仪式化：无表情 + 镜像对称 + 目光内敛（双联/圣母档） | **75%** |
| P6 | **工作流参数**（画幅体制）`[归纳]` | 单幅木板（肖像/圣像 40–80cm 级） | 多联祭坛（polyptych，2–15 板） | 湿壁画组画（整墙循环，3×7m 级单景） | **1**（单幅起步） |

> **用法**：P1/P2 定"是不是皮耶罗"（几何骨架 + 可测空间；两条同时 ≥ 中档才成立）；P3/P4 定"光的档位与色温"（白昼均匀 ↔ 夜景点光；浅色域是身份的底色）；P5 定"仪式强度"；P6 是组稿参数（单幅/多联/组画，不进画面重叠计算，按 `expansion.md` §4.3 规则 5 归「工作流参数」栏）。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 边缘化开、过渡带变宽 ≥1.5% 短边、无轮廓线 → 越界**达芬奇**；② 空间改由色阶/笔触生成、轮廓破碎、出现黑影蓝阴影 → 越界**塞尚**；③ 出现画外单光源 + 近黑背景 + 亮部只落脸/手 → 越界**卡拉瓦乔**；④ 人体扭转、肩髋反向、硬边凿刻阴影 → 越界**米开朗基罗**；⑤ 点状高光群 + 左窗高调 + 暗部压平 → 越界**维米尔**。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 达·芬奇）**（× 达·芬奇；本卡 §3.1 分工条款）：清晰几何 vs sfumato 写死：过渡带窄（≤0.6% 短边级）＋轮廓在场＋透视盒 vs ≥1.5% 短边＋无轮廓＋空气透视——与 C-02 同轴（单主轴、不可同帧双标准）；C-05 两模块同侧可协同
- **分工（vs 塞尚）**（× 塞尚；本卡 §3.1 分工条款）：数学空间 vs 色彩调制：透视测量＋一致明暗 vs 色阶编织＋破碎轮廓——冲突轴＝空间生成器与阴影系统（C-05/C-10）
- **分工（vs 米开朗基罗）**（× 米开朗基罗；本卡 §3.1 分工条款）：几何静立（肩髋夹角 ≤10°）vs 扭转体（≥25°）；浅影 vs 硬边凿刻
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-02 过渡带 / C-05 笔触 / C-10 深度衰减 / C-14 渐变禁令 vs 均匀光

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/piero_della_francesca.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
