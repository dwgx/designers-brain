# 倪瓒 模块卡 — `ni_zan`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/ni_zan.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **一河两岸三段式**：近岸（坡石＋疏林）／中景水面／远岸三层横向展开；水面带占画幅 25–45%——构图骨架即「简」的载体
2. **空亭＋几乎无人物**：近岸简笔小亭（≤10 笔、亭内无人）；山水全无人迹——「倪雲林生平不畫人物，惟龍門僧一幅有之」
3. **折带皴＋干笔淡墨**：侧锋方折「折带」笔法、皴线成组近平行；通幅干笔淡墨、浓墨仅作点醒、笔痕见飞白
4. **水面＝纸色＋平远法**：水面区无墨迹（≥85% 纸色）、无波纹倒影；视点低平、远山低矮平缓（主峰 ≤15% 画高）
5. **疏林不画根＋逸品气质**：前景树 4–7 株、树干挺劲、不露树根；萧散简远荒寒空寂——「似嫩而苍，简中寓繁」

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Chinese literati ink landscape in the manner of Ni Zan (倪瓒, 1301–1374):
monochrome ink on paper, extremely sparse and tranquil; a "one river, two banks"
composition in three horizontal bands — a low foreground bank with a few tall,
slender trees (4–6, branches set on four sides, no exposed roots, leaves dotted
sparingly in dry ink) and one small empty pavilion (no people inside); a wide calm
band of unpainted paper as the river, about one third of the picture; a low, even
ridge of far mountains across the water, pale and flat; rock and slope forms built
with the "folded-ribbon" (zhedai cun) side-brush texture — angular, band-like
strokes in pale ink, more texture than wash, with sparse moss dots along edges and
bases; dry, tender brushwork throughout, feathery flying-white, no wet ink blobs;
only a few dark accents as moss dots and leaf dots; no figures, no wind, no motion;
a thin calm horizon; silent, cold, desolate yet luminous mood (荒寒空寂, 萧散简远,
"似嫩而苍"); a neat column of small standard-script calligraphy with a five- or
seven-character poem and one or two small red seals, dated in cyclical characters;
generous white space above and below; the paper breathes
```
**负向约束（`--no` 风格）**
```
--no color, colored washes, saturated hues, gold, glossy sheen, oil paint, impasto,
3D or photorealistic rendering, heavy black ink masses, wet ink blobs, dense texture
strokes (raindrop / ax-cut), crosshatching, western shading, chiaroscuro, cast
shadows, single light source, linear perspective, human figures, faces, animals,
narrative action, boats with people, wind lines, storm, waves, motion, crowded
composition, centered symmetry, tall monumental peaks, full-bleed mountains,
detailed foliage, exposed tree roots, decorative prettiness, sweet colors
```

## 代码艺术规则（§8.2 原样）

1. **三段式比例**：沿垂直方向扫描墨迹覆盖率曲线，应呈"高（近岸）—低（水面带）—中低（远山）"分布；水面带高度占画幅 25–45%；水面带内纸色像素 ≥85%（无波纹、无倒影）。
2. **留白**：全幅纸色（≥90% 亮度基准）面积 ≥40%；天空区无渲染（像素标准差 ≤2%）；纸色区无均匀噪点或纹理。
3. **单色墨与淡墨主导**：彩色像素（饱和度 >10%）≤1%；墨色中位灰度 ≥60%（淡墨主导）；最暗 10% 像素（浓墨域）面积 ≤10%；可辨灰阶 ≥3 级（如淡/中/浓三带）。
4. **折带皴单元**：山石纹理线段中含 ≥1 处 ≥60° 折角的线段比例 ≥50%；线组成组出现（≥3 线/组）且组内方向夹角 ≤30°；无钉头/雨点簇（小点簇密度低于阈值）。
5. **疏林**：树实例 4–6（容差 3–10）；树干倾角 ≤10°；根部无裸露（树干最低点被坡石轮廓覆盖或与其相交）；单树叶片点 ≤80 点。
6. **人物零出现**：人形实例 = 0；亭/屋内部无人物像素团；允许空舟 ≤1。
7. **静态性（动画时）**：帧间光流 ≤0.5%/帧；无风线、水波位移、镜头运动；仅允许 ≤2px 云气呼吸；款印静止；墨色不得闪变（帧间差 ≤1%）。

## 控制参数（§4 原样）

**P1 三段式清晰度（Three-band Clarity）**（默认 中–强）`[归纳]`
- 弱: 近岸/远山较满、水面 <30%（早期《秋林野兴》式）
- 中: 典型一河两岸、水面 30–45%
- 强: 水面 ≥45%、两岸极简（晚年简笔）

**P2 干笔淡墨度（Dry-brush & Pale-ink）**（默认 中–强）`[归纳]`
- 弱: 墨色较湿、渲染较多（绢本早期，如《松林亭子》）
- 中: 干笔皴擦为主、淡墨统调
- 强: 极干极淡、几近无渲染（晚年《容膝斋图》式）

**P3 折带皴方折度（Folded-ribbon Angularity）**（默认 中–强）`[归纳]`
- 弱: 圆笔披麻为主（早期学董巨）
- 中: 折带初成、方圆兼有（《松林亭子》"方折"）
- 强: 全侧笔折带、方硬清劲（典型晚年）

**P4 疏林密度（Tree Sparsity）**（默认 中）`[归纳]`
- 弱: 1–3 株（极简坡树）
- 中: 4–6 株（《六君子》式典型）
- 强: 7–10 株或加竹丛（《渔庄秋霁》式）

**P5 空亭/点景（Empty Pavilion）**（默认 中）`[归纳]`
- 弱: 无亭（纯坡林水）
- 中: 单空亭（典型）
- 强: 亭＋茅屋/馆舍＋竹（多点景，仍无人）

**P6 款题密度（Inscription Density）**（默认 中）`[归纳]`
- 弱: 短款（名＋干支）
- 中: 款＋绝句
- 强: 长跋/诗塘长题（《容膝斋图》式）

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 马蒂斯）**（× 马蒂斯；本卡 §3.1 分工条款）：极简两路径：色块（高纯平涂）vs 笔墨／留白（近单色墨）——判据四条；色彩轴归马、笔墨与留白轴归倪（N3）
- **分工（vs 八大山人）**（× 八大山人；本卡 §3.1 分工条款（对侧口径互查））：减笔同族：构图减法（一河两岸／空亭）vs 形象减法（单主体／白眼）——判据五条；两卡禁项互列；留白 55–60% 交集取显式值
- **分工（vs 塞尚）**（× 塞尚；本卡 §3.1 分工条款）：几何化两条路：构图几何化（横纵分割）vs 形体几何化（圆柱／球／锥）——判据四条

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/ni_zan.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
