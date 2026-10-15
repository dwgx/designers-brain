# 康斯泰勃尔 模块卡 — `constable`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/constable.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **天空是「主音」**：天空带 ≥35%、云型可辨（积云／层积云／卷云／雨云）；地平线几乎总可见——「sky is the key note, the standard of scale」
2. **「康斯泰勃尔之雪」＋绿底红点**：树冠／树篱亮白小点（V≥0.9）密集闪烁（评论界讥为「雪」）；绿族 ≥30%、红族 0.3–3% 点状（红缨／红砖／红屋顶）
3. **固定地点锚定**：≥1 个可辨识地标（Flatford 磨坊池／Willy Lott 宅／Dedham 塔／萨利斯伯里尖顶）——画面是可指认的实景，非理想风景
4. **水＝天空之镜＋曲线引导**：浅水降饱和镜像天空；河／路作「line of beauty」蛇形引导线——单消失点可读，云研究地平线压至下缘
5. **速写与完成作两档＋表面清脆**：现场速写（松、快）→ 六英尺完成作（结构完整）并存；干笔斑驳、可见但不堆砌的笔触、无镜面反光

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Constable-style observational landscape — a specific, recognisable place faithfully recorded:
a working rural scene at a fixed, identifiable spot (mill pond, river ford, water meadow, village lane),
clear and legible depth with one readable vanishing point; the horizon visible, high visibility, no fog;
the sky a material part of the composition — one third to one half of the canvas,
stacked cumulus with soft grey undersides and one darker shower cloud, patches of blue between;
broad, fresh daylight; soft diffuse shadows, no theatrical lighting;
green meadows and tree masses dominate the middle distance; water in the lower third mirrors the sky in muted tones;
one or two small figures and horses engaged in rural work (haymakers, a cart crossing a ford, a barge on a river),
faces indistinct, no dramatic action; individual trees painted as portraits — bark, trunks, pollarded willows;
"Constable's snow": tiny dabs and flecks of white catching sunlight on leaves and hedges;
small, deliberate notes of red — harness fringes, a brick wall, red roof tiles — set against the greens;
crisp, fresh, dry-brush surface, visible but restrained brushwork; the freshness of a sketch
united with the structure of a finished exhibition picture
```
**负向约束（`--no` 风格）**
```
--no storm event, shipwreck, fire, disaster narrative, swirling vortex composition, dissolving edges, fog banks swallowing the horizon,
no artificial light, no night scene, no hard cast shadows, no single spot light, chiaroscuro, glossy varnish reflections,
no impressionist colour division, no complementary-colour vibration, no saturated purple shadows, no black in shadows,
no symbolic apparatus (crosses, ruins, graves as symbols), no contemplative back-turned figure,
no idealised composite landscape, no generic alpine or italianate scenery, no picturesque ruin,
no blur, no motion smear, no cartoon, anime, 3D render, HDR gloss
```

## 代码艺术规则（§8.2 原样）

1. **天空可读规则**：天空带面积 ≥35%（上 1/3 内云覆盖 ≥50%）；检出 ≥1 种云型结构（积云团块/层云条带/卷云丝缕）；**地平线可见性检查**：地平线处梯度带宽 ≤ 全帧中位梯度的 2 倍（无雾幕吞没）。自查：区域分割 + 边缘梯度。 （依据：[R16]「sky is the key note」；[R16] 引 Thornes「visibility nearly always very good」）
2. **白点规则（「雪」）**：树冠/树篱区亮斑（V≥0.9，直径 0.05–0.6% 短边）数量 ≥15；白点集中分布于植被高频区（不与天空区混淆）。自查：亮度阈值 + 斑点检测 + 区域掩膜。 （依据：[R1]「tiny dabs of white paint」；[R4]「snow」批评史）
3. **绿-蓝-红预算规则**：绿族（H 70–150°）面积 ≥30%；天空蓝（H 190–230°）≥10%；红族（H 0–20°）0.3–3% 且**点状集中**（≥2 处、每处 ≤1%）；饱和 ≥0.85 的区块（≥3% 面积）数量 = 0（防梵高式互补振动）。自查：HSV 掩膜统计。 （依据：[R2] 红缨对位；对照 C-12）
4. **无事件规则（vs 透纳判据）**：无风暴/灾难叙事元素；帧间全局光流 ≤1.5%/帧（事件外）；水面仅微风级涟漪（局部光流 ≤2% 短边/秒）；边缘保持可辨（主体轮廓梯度带宽 ≤1% 短边）。自查：光流场 + 轮廓梯度。 （依据：§3.1 判据②④）
5. **地点锚定规则**：≥1 个建筑地标（塔/磨坊/白墙宅/教堂）位于中景—天际线带；单消失点估计成功（RANSAC 直线收敛 ≥5 条）；构图对应可辨的固定视角（非随机全景）。自查：对象检测 + 消失点估计。 （依据：[R2] Flatford 实景；[R7] Harnham 定点）
6. **水镜规则**：水面区域（下部条带）色调 ≈ 天空蓝的降饱和镜像（色相差 ≤25°，饱和为天空的 0.4–0.8 倍）；水平条带结构可检出。自查：分区色相/饱和比对。 （依据：对三件水面作品的一致观察 `[归纳]`）
7. **人物劳作规则**：人物/马匹 ≤5 个实例；姿态分类为劳作（弯腰/持械/驾车），无背向凝视者、无戏剧手势；人脸关键点命中 ≤1 组（不可辨）。自查：姿态估计 + 人脸检测。 （依据：[R2] haymakers；§3.1 vs 弗里德里希判据④）
8. **表面与光规则**：无硬阴影（阴影边界梯度带宽 ≥1% 短边）；镜面高光块（V≥0.95 且面积 >1%）数量 = 0；表面哑光、笔触可见（高频能量集中于 2–6px 尺度带，干笔斑驳可检出）。自查：梯度带宽 + 直方图 + 多尺度能量比。 （依据：[R16]「crispness」；[R9] 干笔 dapple；对照 C-01）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–5 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **天空占比与云可读性**`[归纳]` | 20–35%（树框/闭合构图，天空被枝叶切割） | 35–50%（六英尺典型：《干草车》档） | ≥50% + 云型细读（云研究/《萨利斯伯里》档） | **50%** |
| P2 | **气象题记密度**（题跋制度）`[归纳]` | 无题记（完成作档） | 背面日期简记（如「Sepr. 24th」） | 完整记录：日/时刻/风向/天气/云型（云研究档） | **40%** |
| P3 | **「雪」白点强度**（闪烁笔点）`[归纳]` | 普通高光，无点状闪烁 | 树冠/树篱可见白点簇 | 全画闪烁（被讥「snow/whitewash」档） | **65%** |
| P4 | **地点锚定度**（可辨地标）`[归纳]` | 一般化乡村（无地标） | 可辨地方建筑（磨坊/白屋/村舍） | 明确地标：Dedham 塔 / 萨利斯伯里尖顶 / Flatford 磨坊池视角 | **75%** |
| P5 | **红点强调密度**`[归纳]` | 0–1 处（或无） | 2–3 处小面积（红缨/红砖/屋顶） | ≥4 处或大面积红缨（醒目对位档） | **50%** |
| P6 | **完成度（速写↔完成作）**`[归纳]` | 现场速写（alla prima、底子裸露、笔触飞动） | 等大稿（结构推敲中、快笔大面） | 六英尺完成作（结构完整、仍保活力） | **55%** |

> **用法**：P1/P3/P4 定「是不是康斯泰勃尔」（三条中 ≥2 条 ≥ 中档才成立）；P2 是「观察档案」开关（云研究档开满、完成作档关闭）；P5/P6 定表现档位。**越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若出现**风暴/沉船/火灾等事件叙事、边缘溶解** → 越界透纳；② 若出现**系列化时刻编号、色点分解、有色阴影** → 越界莫奈；③ 若出现**外加象征装置（十字架/废墟/墓）、背向凝视者、地点不可辨** → 越界弗里德里希；④ 若出现**硬单点光 + 戏剧投影** → 越界卡拉瓦乔；⑤ 若出现**室内光/人造光几何** → 越界维米尔/霍珀。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 透纳）**（× 透纳；本卡 §3.1 分工条款）：事件崇高 vs 固定地点／忠实观察：天气＝事件 vs 记录——判据四条＋边界注（≥2 轴联合）；康卡不进入灾难事件档
- **分工（vs 莫奈）**（× 莫奈；本卡 §3.1 分工条款）：瞬时氛围 vs 观察笔记：系列变量 vs 单次记录（题记锚定、不可复用）——判据四条；分界在制度不在题材
- **分工（vs 弗里德里希）**（× 弗里德里希；本卡 §3.1 分工条款（互查一致））：忠实 vs 精神化：地点忠实度／象征计数／天空角色／人物四判据——互查记录 2026-10-16，两侧表述一致
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01 硬阴影（户外漫射、与硬光侧互斥）／C-09 运动预算（低动势侧）／C-05 笔触（可见但非全覆盖，显式划界）／C-12 色相预算（绿族主导＋红点）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/constable.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
