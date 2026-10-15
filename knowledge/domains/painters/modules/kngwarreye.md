# 恩格瓦雷 模块卡 — `kngwarreye`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/kngwarreye.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **全幅图案场（all-over field）**：无地平线/消失点/中心焦点；四个画边等权、「no right way up」（挂哪个方向都不算倒）
2. **点阵＋线网**：点＝种子/花/植物符号（「dots within dots」、点径从针尖到指节跨度极大）；线网＝山药藤/地下块根/地面裂纹（单线连续）
3. **条纹/身体图式（awelye）＋手势性**：黑底上白/彩粗条＝女性体绘图式、随笔势轻微起伏不修边；笔触带速度感与刷毛痕
4. **分层叠加＋点的呼吸＋语义锚点沉入**：底色→线层→点层→覆盖；点场密度涨落（脉动）；鸸鹋脚印/块根等具象锚点先出现、后被点场淹没
5. **大尺幅多联屏＋不签名＋哑光材料痕**：2–9 m 级、多联屏（22/4/18 联）；「Not signed. Not dated.」；丙烯哑光无罩染、干笔飞白、画布边缘不收齐

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**

```
Contemporary Aboriginal desert painting in an all-over gestural register: an edge-to-edge surface
of layered dots and meandering linear tracks, no horizon line, no vanishing point, no central
focal point — the image reads the same from any orientation, it has no right way up; marks range
freely in scale from pinhead dots to knuckle-sized dabs and from fine threads to broad loaded
brush-strokes, laid down in rhythmic, rapid, arm-wide gestures; a pulsing dot field (seeds,
grasses, blossoms) expands and contracts across the canvas and half-submerges sparse abstracted
anchors (three-toed emu footprints, yam tubers and trailing vines, rock holes); an underlying
layer of tangled lines (yam roots, ground cracks, sand-drawing meanders) shows through the paint;
palette follows earth and season — red and yellow ochre, black and white; or muted grey, purple
and brown atmospheres; or an explosive bright "dump dump" range; or black ground crossed by bold
white and coloured stripes; matte synthetic polymer paint on linen or canvas, dry-brush and
bristle traces visible, unstretched cloth worked on the ground, edges left unfinished; monumental
scale, multi-panel works, raw confident gesture, no varnish, no gloss, no signature
```

**负向约束（`--no` 风格）**

```
--no photorealistic landscape, horizon line, vanishing point, single focal point, central
subject, symmetrical composition, smooth airbrushed gradients, glossy varnish, uniform
machine-made dots, identical dots in a perfect grid, optical colour-mixing pointillism,
complementary-colour dot pairs meant to blend at a distance, crowded city scene, western
oil-painting impasto, 3D rendering, drop shadows, text, watermark, signature, frame, borders,
dreamcatcher or boomerang clichés, generic "tribal" clip-art, faux-ethnic decoration,
photographic realism
```

## 代码艺术规则（§8.2 原样）

| # | 规则 | 可判定阈值（默认） | 自查方法 |
|---|---|---|---|
| 1 | **点场覆盖与脉动** | 点场覆盖率 60–95%；沿画幅滑窗密度方差 ≥0.02（≥2 个涨落峰） | 逐帧分块密度统计（8×8 滑窗） |
| 2 | **手势尺度方差** | 点径 p90/p10 ≥ 4；同帧内 ≥3 种尺度档共存；禁止单一同径点阵 | 连通域尺寸分布统计 |
| 3 | **全幅无方向** | 旋转 90° 后密度直方图差异 ≤5%；无主导水平/垂直轴向（边缘角度直方图无 >35% 单峰） | 旋转不变性检查 + 边缘角度直方图 |
| 4 | **线网自由度** | 线档：允许连续缠绕长线（≥1 条贯穿 ≥1/2 画幅）；线宽可变（p90/p10 ≥ 2.5） | 线骨架提取 + 宽度统计 |
| 5 | **色域分期（四档选一）** | 同屏色相簇 ≤8；黑底条纹档条带 ≥6 条且黑底占比 ≥45%；亮色档饱和度峰值 ≥70% 但平均 ≤45% | 逐帧直方图 + 色相聚类 |
| 6 | **呼吸式运动预算** | 全片无叙事位移；密度/尺度调制幅度 ≤2%/s；帧间差 ≤1.5% | 帧差图 + 调制曲线拟合 |
| 7 | **语义锚点预算** | 锚点（三趾印/块根/岩孔类）0–3 个，单个面积 ≤2%，且被点/线覆盖 ≥50%（"半淹没"） | 形状检测 + 覆盖比例检查 |
| 8 | **文化合规检查** | 素材与语义清单核对：神圣/仪式专属元素 0 个（清单外元素为 0）；无文字/签名/品牌 | 清单对照 + OCR 扫描 |

> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；与 `templates/style_card.md` 的填写规则对齐。第 8 条为本模块特有的伦理验收项（与档案头部"文化伦理声明"配套）。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **点阵覆盖度**（Dot Coverage）`[归纳]` | 点稀疏、底大面积外露（近纸本素描） | 点半覆盖，线/底与点同权（1990–92 过渡档） | 点场几乎全覆盖、底仅从缝隙透出（Ntange 档） | **80%** |
| P2 | **手势尺度方差**（Scale Variance of Marks）`[归纳]` | 点径均匀、笔触等宽（**越界：进入修拉档**） | 点径有小幅变化（1–2 倍） | 点径/笔触跨度大（针尖到指节、细线到宽条），同幅内多尺度共存 | **85%**（本模块身份） |
| P3 | **全幅无方向度**（All-over / No Right Way Up）`[归纳]` | 有地平线或明确重心（越界） | 无地平线但密度有一处主峰 | 四边等权、密度分布近各向同性，旋转 90° 仍成立 | **90%** |
| P4 | **线网主导度**（Line Network Dominance）`[归纳]` | 纯点场无线（早期 dump dot 档） | 线在点下隐约可见（underlayer） | 线为主语：缠绕线束/单线连续（Big Yam 档） | **50%**（点/线双档可用） |
| P5 | **体绘图式条纹强度**（Awelye Stripes）`[归纳]` | 无条纹（点场/线网档） | 短横带、局部条纹（早期绷边纹） | 通幅粗条纹、黑底白/彩条（Awelye II 档） | **40%**（需要时切 90%） |
| P6 | **语义锚点可见度**（Motif Anchors）`[归纳]` | 锚点全沉（纯抽象观感） | 锚点隐约可辨（淹没一半） | 鸸鹋三趾印/块根/岩孔清晰可数（≥1 处） | **60%** |

> 用法：**P2＋P3 定"是不是恩格瓦雷"**（多尺度手势＋无方向全幅）；P1/P4 切"点场还是线网"（点档：P1 高、P4 低；线档：P1 中低、P4 高）；P5 切"体绘条纹档"；P6 决定"外部观看者能否看到具象锚点"。三档描述可直接作判定标准写进自查表。
> 数据来源：档位阈值为 `[归纳]`（本项目操作化建议，未经渲染实验校准）；特征观察取自 [R10][R13][R18][R21][R37]。
> **分工注（与修拉，必须写死）**：P2 强档（尺度方差大）＋P3 强档（无方向）是本模块专属；**"同径细密点＋互补色对＋光学混合意图"整体属于修拉模块，禁止在本模块同档出现**——需要点彩感时不得同时保留本模块的"全幅无方向＋语义锚点"标志机制（见 §3 分工口径与 §8.1 越界警报）。本注为 `[归纳]`。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 修拉）**（× 修拉；本卡 §3.1 分工口径）：「点」的两个物种写死：符号/大地（尺寸方差大＋语义锚点 ≥1＋无光学混合目标）vs 光学混合（同径加密＋互补色对）——默认二选一，同屏显式分区
- **越界判据**（× 修拉；本卡 §3.1 分工口径）：同径化＋加密到光学混合尺度＋引入互补色对＋取消语义锚点 → 滑入修拉档（反向：点彩＋地平线＋城市人物不得入本模块）
- **对照（vs 康定斯基）**（× 康定斯基；本卡 §3.1 次级注）：土地与身体叙事驱动 vs 欧陆理论驱动——[推测] 级对照，仅记录、不写死

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/kngwarreye.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
