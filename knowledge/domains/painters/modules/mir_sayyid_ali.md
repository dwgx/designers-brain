# 米尔·赛义德·阿里 模块卡 — `mir_sayyid_ali`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/mir_sayyid_ali.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 11 条）

1. **大幅开本＋棉布载体**：叶面长边 ≥60 cm（约 65–70×50–55 cm 档）、画心近方形、布纹可见；多层合装（画/书法/加固层胶合、画与文本对页一体）——《哈姆扎纳马》的工程化开本
2. **微书级细节＋物质世界记录**：高频细节区 ≥1、可辨器物/织物类型 ≥5——「meticulous attention to detail」「accurate depiction of the material world」
3. **签名式手法三件**：小瞳孔＋可见眼白；细密纹样（纹样区 ≥2）；主题诗句上书上毯（诗行 ∈ 画面物件）——签名嵌入画内物件（学生纸片/毯缘/书写板）
4. **事件动势群像＋尖角几何岩**：战斗/夜袭/救援/追逐（人物 ≥8、事件进行时）；岩石多角直线边 ≥2、沿水道成组——「large, dynamic, and fantastic」
5. **印度融合风物＋夜景火光**：印度元素 ≥1（象/热带树/印度建筑/深肤色）；暖色光源点 ≥3、背景明度 ≤35%——《城中夜》档

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Mir Sayyid Ali-style early Mughal manuscript page — a monumental folio from the Hamzanama (India, c. 1565–1575):
a large, dynamic narrative scene from an epic adventure — a night raid, battle, rescue, or court intrigue —
staged in a walled city, an encampment, or a rocky landscape; crowded with many figures, horses, and demons in action;
opaque watercolor and gold on cotton cloth, bold saturated colors — strong reds, blues, greens and oranges;
minute, meticulous detail in textiles, armor, weapons, carpets, and architecture, an encyclopedic record of the material world;
sharply cut, geometric rocks along a stream; tall slender figures with small pupils ringed by eye-whites;
horses with elegantly outlined, smooth-textured forms; high viewpoint, vertical format, stacked planes, no vanishing point;
Persian pictorial conventions fused with Indian naturalism in animals, plants, and buildings; trimmed field, no outer frame;
matte flat pigment, gold accents used sparingly as flat spots
```
**负向约束（`--no` 风格）**
```
--no single-point perspective, converging lines, vanishing point, cast shadows from one light, chiaroscuro, sfumato,
photographic depth of field, atmospheric haze, European easel composition, oil-paint impasto, visible brushwork,
metallic sheen, relief or texture on the gold, specular highlights, small page format, minimal detail,
large empty unpatterned voids, watermark, 3D render, anime, cartoon, modern clothing, woodblock keyline print
```

## 代码艺术规则（§8.2 原样）

1. **事件动势群像规则**：画面含 ≥1 事件进行时（战斗/夜袭/救援/追逐）且人物 ≥8（群像档）；全静场判失败（弱档除外）。自查：事件计数 + 人体框计数。（依据：§3.1 轴②；[R19][R20]）
2. **细节密度规则**：高频细节区 ≥1——局部窗口的边缘密度高于全帧中位数 ≥1.5×（纹样/织物/建筑装饰可读）。自查：分块边缘密度统计。（依据：微书档 [R1][R19]）
3. **尖角几何岩规则**：沿水道出现的岩块以直线边为主（直线边 ≥2、圆润度低）。自查：形状近似（多边形拟合 + 直线边计数）。（依据：[R19]）
4. **小瞳孔眼白规则**：在可辨尺度下，人物眼部为点状瞳孔 + 可见眼白（人检；可选模板匹配）。自查：局部区域目检。（依据：Seyller「签名式清单」[R19]）
5. **无消失点规则（族征）**：全帧直线族中，平行后退线不得收敛——「消失点检验」= 0 组汇聚线（≥3 条线共点即失败）。自查：Hough 线检测 + 共点聚类。（依据：层叠平面 [R11][R19]；与贝赫扎德同侧）
6. **人物比例恒定规则（族征）**：人物高度不随「纵深」缩放；同帧人物高度方差 ≤15%。自查：人体框高度统计。（依据：无透视纵深语法 [R19]）
7. **融合风物规则**：印度元素 ≥1 处可辨（象/热带植物/印度建筑形制/深肤色人物）；「纯波斯」判弱档。自查：元素目检计数。（依据：转译轴 [R11][R8]）
8. **色彩与金层规则**：高饱和不透明色（S ≥0.5）面积 ≥30%；金区为**平涂点金**（区域内部明度动态范围 ≤5%、无光泽起伏）、面积 ≤5%、单列不计色数（C-15/N6 接口）。自查：HSV 掩膜 + 区域明度方差。（依据：平涂点金 [R11][R19]；vs 克里姆特判据）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母 = 假想参考帧）；1/3/4 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **开本与载体档**（硬轴）`[归纳]` | 纸本小页（长边 ≤30 cm 档；贝赫扎德邻域） | 中幅（约 40–55 cm 档；单页画/对页） | 大幅棉布（≥65 × 50 cm、多层合装；《哈姆扎纳马》档） | **70%** |
| P2 | **细节密度**`[归纳]` | 简化表面（大色块为主） | 织物/砖石可读纹样 | 微书级（器物/纹样/建筑装饰全可读；「eye-strainingly fine」档） | **70%** |
| P3 | **事件动势强度**`[归纳]` | 静场（端坐/静立为主） | 局部动作（行走/指点/交谈） | 事件进行时群像（战斗/夜袭/救援；≥8 人、武器与马匹在动） | **60%** |
| P4 | **融合风物度**`[归纳]` | 纯波斯风物（赫拉特/塔布里兹类型） | 混入 1–2 处印度元素 | 印度元素显著（动物自然主义、印度建筑与装束、深肤色；≥3 处） | **55%** |
| P5 | **夜光装置**`[归纳]` | 无光照装置（昼景平光） | 室内灯烛（局部暖光点 1–2） | 夜景主调（火把/灯火 ≥3 光源、深底暖点；《城中夜》档） | **30%** |
| P6 | **工程/版面参数**（工作流参数）`[归纳]` | 单页画（无文本） | 画 + 文本对页一体 | 多卷工程叶（双画叶/工程标记/裁切痕档） | **中档** |

> **用法**：P1（硬轴）+ P2/P3/P4 定「是不是米尔·赛义德·阿里（vs 贝赫扎德）」——P1 强 + 其余 ≥2 条 ≥ 中档才成立；P3 定事件强度；P5 定夜景档；P6 是版面参数（单页 vs 工程叶，不进画面重叠计算，按 `expansion.md` §4.3 规则 5 归「工作流参数」栏）。
> **分工注（与 §3.1 对齐）**：P1 降为「弱」且 P2 升「微书」、空场增大、静场为主，即越界进入**贝赫扎德**领域；P1 保持强但色彩升为「平涂金天/满幅奢华」、姿态转「旋转飞扬」，即越界进入**苏丹·穆罕默德**领域；等宽线 + 平涂 + 留白 ≥35% → **北斋**领域；金层若出现光泽/材质（非平涂点金）→ **克里姆特**领域——组合实验按此判分。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 贝赫扎德 / 苏丹·穆罕默德）**（× 贝赫扎德 / 苏丹·穆罕默德；本卡 §3.1 分工条款（同族三站））：细密画线第三站：波斯原典（静态精巧/纸本小页）／动势色彩（萨法维奢华）／转译融合（莫卧儿工程）——四轴判据（开本载体为硬轴）；同族三站不得互串
- **分工（vs 北斋）**（× 北斋；本卡 §3.1 分工条款）：叙事图像媒介不同：手抄本 vs 版画——四轴（媒介版面／空间／人群／表面）；负空间口径须显式取值或分区（C-17）
- **系统缺口登记（细密画线第三站）**（× 贝赫扎德 / 苏丹·穆罕默德 / 北斋 / 克里姆特；本卡 §3.1 缺口登记）：补齐「大幅叙事页＋跨传统融合＋工程化工作坊」；不借贝小页空场／苏平涂金天／北斋版画留白；金为点金 ≤5%（按 C-15/N6 单列）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合预检（写死））：重点：C-15/N6 金层单列与「平涂点金、非高光材质」声明／C-16 反约束适用域（声明 flat matte, no specular highlights）／C-17 负空间（满幅、空场少）／C-07 表面同侧声明／N3／N4
- **near-miss（conflicts.md §4 表）**：#11（负空间：× 北斋 / 贝赫扎德 → 显式取值或分区（N4）；负空间轴单主）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/mir_sayyid_ali.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
