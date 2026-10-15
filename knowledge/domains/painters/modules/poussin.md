# 普桑 模块卡 — `poussin`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/poussin.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **舞台式清晰**：人物如演员被调度——基座线成排（与水平夹角 ≤10°）、平行于画面的排布；背景是建筑／山体布景
2. **几何骨架＋冻结的瞬间**：对角／交叉轴线 ≥2 组、平行带 ≥2、左右配重；动作取「中段」——暴力场面亦呈「abstract, choreographed quality」
3. **中景可读＋清晰光**：前／中／远三档分层（尺度梯度＋遮挡＋布景，不用大气消融）；均匀白昼光——暗部占比低、无单点戏剧光斑
4. **受控色阶（modes）＋理想化人体**：色相簇 ≤8、中位饱和 ≤0.55（暖土底＋蓝绿点缀）；人体比例理想、面貌类型化、衣褶如雕塑
5. **清晰轮廓＋完成表面＋叙事可读**：轮廓可辨（亮度阶跃 ≥0.2）、无可见笔触（线先于色）；单一主事件＋可数辅助组——「lisez l'histoire et le tableau」

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Poussin-style classical composition — clarity, order, and a stage set for history:
figures disposed like actors on a stage, arranged in rows parallel to the picture plane,
dispersed with measured intervals in a well-defined space;
a clear geometric armature — long diagonals, verticals, balanced masses, deliberate symmetry;
each figure held in a legible rhetorical attitude, gesture and bearing readable as language;
even, lucid daylight — shadow present but never swallowing form, no single dramatic source,
no near-black background; light that lets every form be read;
a noble restrained palette — ochre red, blue, olive green, earth tones — modulated like a musical mode;
idealized bodies after the antique, drapery with clear sculptural folds;
a legible middle ground: staged planes, architecture as backdrop, scale steps for depth;
the action frozen at its chosen moment — balanced, choreographed, never blurred;
smooth enamel-like surface, crisp contours, invisible brushwork;
serene, rational, deliberately composed — everything appropriate to the subject
```
**负向约束（`--no` 风格）**
```
--no chiaroscuro darkness, near-black backgrounds, single spotlight, tenebrism, dramatic cast shadow,
sfumato haze, atmospheric dissolution, misty vanishing distances, melting edges,
swirling contorted struggle, individual agony, writhing bodies, motion blur,
impasto, visible brushstrokes, glazing reflections, rough canvas texture,
accidental crowding, murky shadows, picturesque disorder, gothic ruins, storm drama, sublime wilderness,
saturated neon colours, complementary-colour vibration, sentimental pathos, horror, grotesque,
photorealistic skin, cartoon, anime, 3D render, HDR gloss
```

## 代码艺术规则（§8.2 原样）

1. **舞台排列规则**：≥60% 主要人物的触地点（脚/基座）落在 ≤15% 画高的水平带内；人物群至少形成 **2 组「排」**（组心连线与水平夹角 ≤10°）。自查：姿态/触地点检测 + 聚类。（依据：[R7]「arranged in rows… parallel to the picture plane」）
2. **几何骨架规则**：检出 ≥2 条长度 ≥40% 对角线的直线，且 ≥1 组交叉；左右半区视觉质量差 ≤15%（配重），或检出 ≥1 组镜像呼应对。自查：Hough 直线 + 质量配平度量。（依据：[R7]「abstract, choreographed quality」；[R1]《萨宾》几何评注）
3. **清晰光规则（无暗绘法）**：全帧 L<0.2 像素占比 ≤15%；最大暗区连通域 ≤5% 画面；高亮连通域（≥0.95×max 且面积 >2%）数量 = 0（无戏剧亮斑）；全帧亮度均值 0.45–0.75。自查：直方图 + 连通域分析。（依据：[R4] 玛纳信；[R7] 对卡拉瓦乔的立场）
4. **受控色阶规则**：色相簇 ≤8（30° 分桶、占比 ≥5% 者计数）；全帧中位饱和 ≤0.55；S>0.8 的大区块（面积 >3%）数量 = 0；暖土色（H 20–50°）作底、冷色（H 180–260°）作点缀。自查：HSV 掩膜统计。（对照 C-12：与北斋蓝、梵高互补对形成轴差）
5. **冻结编排规则**：无运动模糊核；人物重心投影落在支撑面内（平衡可读）；≥1 组对称/配重对位；极端失稳姿态（倒地/奔跑终点类）计数 ≤1。自查：模糊核 + 姿态估计 + 对称检测。（与 C-09 对齐：站「冻结/编排」侧）
6. **空间分层规则**：≥3 个深度层（遮挡链 ≥2 级）；同类物体尺度梯度：近景/中景高度比 ≥1.5；**中景非空缺**——中带（1/3–2/3 画高）可辨元素数 ≥3。自查：遮挡排序 + 尺度回归。（对照弗里德里希「middle ground missing」）
7. **轮廓清晰规则**：主体轮廓处亮度阶跃 ≥0.2（在 ≤3px 内完成）；轮廓边缘链断裂率 ≤20%。自查：边缘剖面 + 链跟踪。（对照：达·芬奇 ≥1.5% 短边柔边；米开朗基罗 ≤0.6% 硬边——普桑取「可读」区间）
8. **表面完成规则**：平坦区高频能量（Laplacian 方差）≤5（笔触不可见）；镜面高光（V≥0.95 且面积 >1%）数量 ≤2；无釉彩反射带（V≥0.95 且面积 >5% 者 = 0）。自查：多尺度能量 + 高光计数。（依据：[R7]「favors line over color」；[R8] couches fines）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–5 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **舞台清晰度（调度感）**`[归纳]` | 人物自然分布、背景简化（早年档） | 分层舞台 + 建筑布景（《吗哪》档） | 排成与画面平行的排、完全舞台化（《大卫的凯旋》《金牛犊》档） | **70%** |
| P2 | **几何骨架强度**`[归纳]` | 自然构图（早期） | 可见对角/对称配重（《阿卡迪亚》档） | 显式网格/平行带/双轴交叉（《萨宾》《舞蹈》档） | **65%** |
| P3 | **姿态冻结度（编排感）**`[归纳]` | 自然动作瞬间 | 动作中段冻结（《萨宾》档） | 舞蹈式/静物式编排（《舞蹈》档） | **60%** |
| P4 | **光的清晰度**`[归纳]` | 明暗对比偏强（1620s 威尼斯期档） | 均匀白昼光（成熟期默认） | 全画面无暗部遮蔽（晚期风景档） | **70%** |
| P5 | **色阶模式（冷暖/收窄度）**`[归纳]` | 暖调多色（早年档） | 收窄色阶（红黄蓝 + 土色；1630s 起） | 近单色阶/冷调（晚期档） | **60%** |
| P6 | **叙事密度**`[归纳]` | 单人/圣像 | 3–5 人小场景 | 群像历史场景（多组辅助叙事） | **55%** |

> **用法**：P1/P2/P4 定「是不是普桑」（三条中 ≥2 条 ≥ 中档才成立）；P3/P5 定时代档（早年威尼斯 → 中期舞台 → 晚期冷调）；P6 是题材参数（可关）。**越界警报（与 §3.1 对齐，组合实验按此判分）**：① 出现**画外单光源 + 近黑背景** → 越界卡拉瓦乔；② 出现 **sfumato 全域柔边 + 空气消融远景** → 越界达·芬奇；③ 出现**个体化扭转挣扎 + 硬边凿刻** → 越界米开朗基罗；④ 出现**层带阻隔 + 中景空缺 + 凝视背影** → 越界弗里德里希；⑤ 出现**室内点状高光 + 光学盒空间** → 越界维米尔。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 达·芬奇）**（× 达·芬奇；本卡 §3.1 分工条款）：柔和 vs 几何清晰：消融档 vs 清晰档——判据四条＋边界注（以 1630s 起中期为准）
- **分工（vs 米开朗基罗）**（× 米开朗基罗；本卡 §3.1 分工条款）：动态 vs 静态平衡：terribilità 个体化扭转 vs 编排／配重——判据四条＋边界注（编排 vs 个体化扭曲）
- **分工（vs 弗里德里希）**（× 弗里德里希；本卡 §3.1 分工条款（镜像确认））：古典舞台 vs 浪漫建构——纵深秩序／人物角色／光／象征四判据
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01 硬阴影（均匀光侧，显式声明无单点戏剧光）／C-09 运动预算（冻结／编排侧）／C-12 色相预算（受控色阶）／C-14 渐变

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/poussin.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
