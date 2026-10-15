# 尾形光琳 模块卡 — `ogata_korin`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/ogata_korin.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 11 条）

1. **総金地**：背景金箔／金泥铺满（金区 ≥70% 强档）；箔足网格状淡线、亮度变异 σ≈2–8%——金是材质层（非平涂单色）
2. **大和絵限定色板＋笔触可见**：群青／緑青／朱／胡粉／墨（色相簇 ≤6）；群青厚涂、緑青刷痕——色块内部明度动态 ≥8%
3. **母题纹样化＋双幅对照**：同形重复 ≥8 组、姿态模板 ≤3（型紙复用）；左右隻密度／材质对比（右花密／左金宽；金地／银流）
4. **たらし込み＋金与水并置**：湿层渗化斑纹（斑缘模糊 2–6px）；金箔＋银箔／金泥二元——「金与水」的材质语汇
5. **平面大构图＋余白＋静止**：无焦点透视、空间靠重叠与对照；金空区 ≥40%（左隻）；无动势线——动只封在纹样里

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
a decorative Japanese folding-screen painting (byobu) in the manner of Ogata Korin and the Rinpa school:
a total gold ground of applied gold leaf covering the whole background, faint foil seams and a soft
uneven sheen (not flat yellow); simplified natural motifs — irises, plum trees, waves, cranes,
autumn grasses — reduced to clear silhouettes and rhythmically repeated like stencil-cut patterns
(katagami), the same forms recurring with slight variation; a limited Yamato-e palette — deep
ultramarine azurite blues, malachite greens, shell-white, cinnabar red and sumi ink — laid over
the gold; paint applied with visible brushwork, thickly pooled petals and briskly brushed leaves,
yet the whole reads as flat ornament; tarashikomi — wet-on-wet pooling where ink or colour drops
into still-wet pigment — used for tree trunks, bridges and water; metallic planes of gold and
silver (a silver stream blackened to deep grey, gold-leaf squares around painted areas); flat
screen composition, no linear perspective, space suggested only by overlaps and by the rhythm of
clusters; large calm areas of bare gold used as composition; asymmetry and calculated contrast
between the two screens of a pair (dense flowers versus open gold); plum blossoms painted without
outlines, petals formed by pigment alone ("Korin plum"); crisp simplified edges, motion frozen;
the surface of a luxury craft object as much as a painting
```

**负向约束（`--no` 风格）**
```
--no Western perspective, vanishing point, 3D shading, cast shadows, chiaroscuro, photorealism,
photographic detail, atmospheric perspective, smooth gradients, airbrush, soft focus, heavy
impasto ridges, glittering specular highlights, plastic gold, zero-brushwork vector flatness,
machine-perfect symmetry, mirror-symmetric pair, cluttered realistic foliage, botanical
illustration, muted muddy colours, pastel palette, grey-beige tonality, portraits, realistic
human faces, urban scenes, Art Nouveau whiplash lines, Vienna Secession ornament, geometric
pattern blocks colliding with figures
```

## 代码艺术规则（§8.2 原样）

1. **金地检测**：P1≥强时，金色带（H 38–55°、S 25–70%、V 55–95%）像素占比 ≥65%；金区须有箔目级亮度变异（σ 2–8% 明度），单一 RGB 平涂（ΔV ≤1.5%）判 fail。
2. **色相簇**：全帧色相簇 ≤6；蓝簇（H 200–240°）面积 5–25%（群青）、绿簇（H 90–150°）5–20%（緑青）；色相簇 >8 越界。
3. **母题重复**：同类母题（花/鸟/波峰）实例 ≥8 时姿态模板 ≤3；相邻实例间距变异系数 ≤0.35（节奏性，非随机散布）。
4. **轮廓线**：宽度 ≥2px 且长度 >40px 的均匀深色轮廓线覆盖 ≤30% 形体周长；「光琳梅」花弁区轮廓覆盖率 ≤10%（无描线成形）。
5. **たらし込み斑**：P5≥中时，斑纹区（低频边界模糊 2–6px 的高频缺失区）面积 5–25%；斑内明度动态 ≥10%。
6. **平涂界限（vs 马蒂斯）**：任一「纹样色块」内部明度动态范围 ≥8%；若全帧最大色块内部动态 ≤5% → 属马蒂斯域（退档）。
7. **空间**：无消失点（直线族透视收敛检测 fail）；深度线索仅重叠顺序；无投影/阴影（带方向性的 >25% 亮度差区块 → fail）。
8. **双幅对照（成对时）**：左右幅平均色相/密度差 ≥20%（对照成立），但母题节奏相关系数 ≥0.4（同族）；镜像对称（翻转后相关系数 >0.9）→ fail。
9. **运动（动画时）**：全画面静止；唯一允许动：水面微动 ≤2px/帧（波濤/水流）或金地反光缓变 ≤1%/帧；母题位移 = 0。
10. **金属 vs 颜料区分**：金色区不得出现镜面高光斑（亮度 >95% 且面积 >0.5%）；黑/深灰水区（V<25%）只能来自水/墨，且必须邻接金或银区（红白梅模式）。

## 控制参数（§4 原样）

**P1 金地覆盖率（金箔/金泥）**（默认 75%）`[归纳]`
- 弱（≤20%）：素地/墨画/局部金泥（竹梅図、維摩図）
- 中（20–70%）：部分金地或金限定使用（太公望図、躑躅図）
- 强（≥70%）：総金地（燕子花図、紅白梅図、風神雷神図、八橋図）

**P2 母題反復度（型紙/节奏）**（默认 70%）`[归纳]`
- 弱：单株/单景无重复（太公望図、中村内蔵助像）
- 中：2–4 组轻重复（八橋図＝桥＋花群；群鶴＝列）
- 强：≥8 组均齐反復（燕子花図＝8 群说；型紙反復）

**P3 色彩系统（大和絵彩色 ↔ 墨）**（默认 65%）`[归纳]`
- 弱：墨一色（竹梅図・維摩図・波濤図的墨调）
- 中：彩色 2–3 系＋金（太公望図・躑躅図）
- 强：群青/緑青/朱/胡粉 4＋系浓彩＋金（燕子花図・紅白梅図）

**P4 余白（金地空区）**（默认 40%）`[归纳]`
- 弱（≤10%）：满密（紅白梅図右隻）
- 中（10–40%）：穿插（風神雷神図の上方金空区）
- 强（≥40%）：大金空区（燕子花図左隻型）

**P5 たらし込み强度**（默认 40%）`[归纳]`
- 弱（0）：几乎无（燕子花図）
- 中：局部（紅白梅図の幹、八橋図の橋）
- 强：水/幹/岩广域（紅白梅図の流れ＋幹）

**P6 画面装置（屏风构成）**（默认 强）`[归纳]`
- 弱：掛幅/扇面/団扇（小品）
- 中：二曲一双/六曲一隻（風神雷神図・紅白梅図）
- 强：六曲一双大画面（燕子花図・八橋図）

> 用法：P1/P3 决定「是不是光琳的金地彩画」；P2 决定「写生↔纹样」档位；P4 决定「疏密对照」；P5 决定「水性斑纹」强度；P6 决定画面装置。三档描述可直接进逐帧自查表。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 克里姆特）**（× 克里姆特；本卡 §3.1 分工条款）：同为「金」：自然纹样／屏风平面 vs 人物对撞／现代——判据 a–d 四条；「金」来源不得混用、同屏分区
- **分工（vs 马蒂斯）**（× 马蒂斯；本卡 §3.1 分工条款）：装饰：平涂 vs 金与水的图案——判据 a–d；三选口径（金属＋人物→克；金／水材质→光琳；平涂纯色→马）
- **简表（邻近模块）**（× 若冲 / 北斋 / 广重 / 慕夏 / 卡拉瓦乔 / 伦勃朗 / 维米尔 / 达·芬奇；本卡 §3.1 简表）：无画内光源系统（平面天光＋金地反光）；不得借暗部塌陷／sfumato／版画动势；「浪」母题：事件 vs 纹样
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-15 色数／金彩计数口径／C-16 反约束适用域／C-17 负空间（预检以 conflicts.md 为正本）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/ogata_korin.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
