# 林飞龙 模块卡 — `lam`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/lam.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **混种合体（人×动物×植物）**：主体是「进行中的变形」——马首/鸟首、马蹄、爪形手、果实状乳房、植物茎干与人体无缝过渡；每主体可拆 ≥2 类部件来源、人-植物边界不可分、无拼贴接缝（生长式非装配式）
2. **满幅丛林（无地平线）＋竖向节律**：负空间 ≤15%、地平线检测=无、四边被植物触边（秆 ≥8 根/画幅）；秆/肢/颈构成多列竖线＋弧线对位（竖线族 ≥3 组）——「dense, vertiginous composition」、整体被读作「舞蹈/仪式进行时」
3. **面具脸＋多重首级＋修长肢体**：面具化脸（非洲面具谱系）＋「一颈多头」并置、面部无肖像个性；四肢长宽比 ≥5:1、手形足（handlike feet）、指/趾 ≥4 分歧；性征并置与夸张（部件 ≥1.5×、雌雄同体特征可同体）
4. **暗绿-赭-黑主域＋红橙闪点＋符号库**：主色族 ≤4（绿/黑/赭/红橙）、红橙面积 2–8%（「almost shrill colors」）、哑光稀薄；甘蔗＝奴隶制与榨取史、烟叶＝存续传统；供盘/月亮/鼓等仪式道具、神祇可指名（Elegguá/Ogún/Oshún/Damballah）
5. **薄涂-渗化表面（kraft 纸底透出）**：稀释油彩渗入纸纤维、滴点/飞溅保留、炭笔底稿线可见、露纸 5–20%；表面高频纹理可见但非厚涂（无 ≥2mm 厚堆）、哑光无清漆感

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Wifredo Lam-style Afro-Caribbean ritual modernism — a dense, haunted tropical scene where human, animal and vegetal forms grow into one another:
one to four hybrid beings emerging from a thicket of sugarcane, bamboo and broad leaves — bodies part human, part horse, part bird, part plant,
limbs elongated and spiky, feet like hands, masks for faces, a second head rising from one neck;
no horizon — the jungle fills every edge, stalks stand in rhythmic verticals, a crescent moon or a red-orange spark glows through the dark green;
sombre palette of deep greens, blacks, ochres and browns, with small flashes of blood-red and orange; matte, thin paint,
washes soaked into kraft paper, drips and splatters left visible, charcoal underdrawing showing through, bare paper breathing in places;
ritual objects quietly present — a small offering dish with corn and fruit, tobacco leaves in a red-stained hand, scissors, a drum-like rhythm of forms;
eroticized anatomy held sacred rather than grotesque — full lips, round buttocks, one breast, male and female attributes side by side;
the whole composition moving like a slow dance, ceremonial and trance-like, intimate with night;
oil and charcoal on paper mounted on canvas, museum reproduction quality, muted sheen, no varnish gloss
```
**负向约束（`--no` 风格）**
```
--no cubist fragmentation, multiple viewpoints, collage elements, letters, newspaper scraps, analytic cubist grid,
bright candy colors, all-over decorative patterns, wallpaper motifs, ornamental gold,
daylight panorama, moral allegory, devils and punishments, catalogued monsters,
photographic realism, botanical illustration detail, jungle undergrowth realism, chiaroscuro drama, impasto, glossy 3D render, HDR, neon, text, signature, watermark, frame
```

## 代码艺术规则（§8.2 原样）

1. **混种规则**：全帧 ≥1 个主体可拆出 ≥2 类部件来源（人/马/鸟/植物/果实）；「拼贴接缝」（直线剪切边＋粘贴边界）＝0；马首/鸟首/爪形足模板命中 ≥1。（自查：边缘图＋部件模板；对照 §3.1 判据①）
2. **密度规则**：负空间（天空/纯背景可见像素）≤15%；地平线检测＝无；画面四边触边率 ≥90%。（自查：分区直方图＋地平线检测；对照 §3.1 判据②）
3. **色域规则**：全帧主色相 ≤4（绿/黑/赭/红橙）；红橙像素占比 2–8%；高饱和像素（S>0.6）≤12%；平均明度 ≤0.45（暗域档）。（自查：HSV 统计；对照 §3.1 判据③）
4. **表面规则**：露纸/浅底区 5–20%；滴点/飞溅连通域 ≥3；厚涂高光＝0（无等效厚堆亮斑）；表面高频能量显式中档（介于平涂与厚涂之间——须声明）。（对照 C-01/C-05：显式声明「柔边薄涂、哑光」）
5. **面具规则**：面部类型化（无肖像个性）；面具脸 ≥1；P6 强档时非人首（马首/鸟首/无面）≥1。（自查：人脸检测＋类型化判定）
6. **仪式符号规则**：每帧 ≥1 符号（月/供盘/烟叶/剪刀/鼓式节律）；符号承担叙事、不得商品化陈列（禁静物化摆设）。（对照 §3.1 判据①；对照 C-12 色相预算）
7. **性征并置规则**：≥1 夸张部件（尺度 ≥1.5× 自然比例）；雌雄特征可同体；「神圣而非色情」——不做写实裸露（避免 slide 到 body-horror/装饰色情）。（自查：比例测量＋姿态库）
8. **节律规则**：竖线族 ≥3 组；弧线与竖线交替；构图重心偏下（植被承载重量）。（自查：线段方向直方图）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1/2/3/4/6 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。与 `conflicts.md` 的关系：**C-01**（硬阴影——林「柔边薄涂」显式声明）、**C-05**（笔触——林「薄涂渗化、非厚涂」档）、**C-06**（饱和度——林「中低＋小面积红橙」）、**C-12**（色相面积——绿黑主导）、**C-17**（负空间——林「≤15%」侧）、**C-18**（形体——有机流动档）为组合预检重点。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **混种度（Hybridity）**`[归纳]` | 单一物种畸变/装饰性变形 | 人＋动物部件（马首/鸟喙/爪手） | 人-动物-植物三元合体、多头并置、生长式过渡 | **75%** |
| P2 | **丛林密度（Jungle Density）**`[归纳]` | 留白/天空可见、地平线在场 | 植被围合、局部天光 | 满幅无地平线、负空间 ≤15%、四边触边 | **80%** |
| P3 | **暗域度（Sombre Palette）**`[归纳]` | 亮色铺开（越界警报：博斯侧/高更侧） | 暗绿-赭为主、局部亮部 | 黑-暗绿-棕＋红橙闪点＋月光夜色 | **70%** |
| P4 | **仪式符号密度（Ritual Symbols）**`[归纳]` | 无（纯形体练习） | ≥1 符号（月/供盘/烟叶/剪刀） | 神祇在场（orisha 可指名、被附体状态） | **50%** |
| P5 | **性征夸张（Erotic Exaggeration）**`[归纳]` | 自然比例 | 单部件夸张（唇/乳/臀） | 多部件＋雌雄同体并置（esteatopigia 档） | **45%** |
| P6 | **面具化（Masking）**`[归纳]` | 具象脸（肖像期遗产） | 面具脸（类型化、无个性） | 面具＋非人首（马首/鸟首/无面） | **65%** |

> **用法**：P1/P2 定「是不是林飞龙」的起步（两条中 ≥1 条 ≥ 中档才成立——混种合体或满幅丛林）；P3 定氛围（暗域档）；P4 定仪式档（中档=符号，强档=神祇在场）；P5/P6 定身体-面部档。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若「碎裂/多视点/拼贴物（字母/报纸/木纹）」→ 越界**毕加索**（P1 弱档连用即越界）；② 若「明亮全景＋多事件编目＋可解码的道德讽喻」→ 越界**博斯**；③ 若「装饰性热带色＋图案化植物」→ 越界**高更/塔西拉侧**；④ 若「植物学细描＋丛林透视消失点」→ 越界**卢梭式**；⑤ 若「壁画工程尺度＋历史全景」→ 越界**里维拉**。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 毕加索）**（× 毕加索；本卡 §3.1 分工条款（第一写死条款））：立体主义：欧洲内部发明 vs 带回加勒比的神话载体——四判据（神话/符号指向／形体构造／色彩／方向与主体性）；判定须 ≥2 轴联合（尤其①④）、不得只看「面具脸」或「几何感」；组合纪律：碎裂度轴不得双开、拼贴物（字母/报纸/木纹）禁入、仪式符号不得降格为静物陈列
- **分工（vs 博斯）**（× 博斯；本卡 §3.1 分工条款（第二写死条款））：混种生物：道德编码讽喻 vs 仪式性在场——四判据（合体职能／场景组织／情绪距离／色与光）；判定须 ≥2 轴联合（尤其①③）；「混种」非独有、职能才是判据；组合纪律：「怪诞」轴不得同帧折中、明亮奇观与道德编码禁入林式暗域
- **次级注记（vs 高更 / 卡罗 / 里维拉 / 卢梭）**（× 高更 / 卡罗 / 里维拉 / 卢梭（future）；本卡 §3.1 次级注记）：不借高更的塔希提装饰色（加勒比＝历史现场，非「热带装饰」）／不借卡罗的自传象征／不借里维拉的壁画工程尺度／不借卢梭式的植物学细描（植物是符号非标本）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01 硬阴影（柔边薄涂/哑光，须显式声明）／C-05 笔触（薄涂渗化、可见非厚涂）／C-06 饱和度（中低＋小面积红橙）／C-12 色相面积（绿黑主导预算）／C-17 负空间（≤15% 侧）／C-18 形体（有机流动档）；句式改写：C-14（「渐变仅限稀释油彩的渗化/擦痕，不得成平滑数码渐变」）＋声明「哑光、薄涂、纸底透出、无清漆」

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/lam.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
