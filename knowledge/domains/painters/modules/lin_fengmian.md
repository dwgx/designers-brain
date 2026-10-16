# 林风眠 模块卡 — `lin_fengmian`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/lin_fengmian.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **方纸布阵＋几何秩序**：正方形满幅（画幅比 1:1±5%）、四方等量扩展、画面画满（常连签名的位置也没有）——「构成一统天下与大气磅礴之感」；静物「像是压缩在斜面上」（塞尚式平面化）、桌面/门窗变形、不合透视——「追求艺术构成中的几何秩序」
2. **块面与线弦的二重唱**：块面塑造奠定「建筑性」＋流畅长线配合补充（块面 ≥2 处、长线 ≥3 组、线不闭合描边）；形象在「面与线重唱中忽隐忽现」；用笔快速爽利露锋——「转出来的线条就是活的」
3. **墨彩调合＋涂白**：墨与彩不分先后、相互叠压——「墨中叠彩，彩中叠墨」（水粉厚抹、色中掺墨、纸背托色）；无「先勾后填」式边界；大块白色主动涂上去（主动白区 3–15%、白区见笔触）——「叠白法」「白分五彩」
4. **民间瓷绘色＋仕女/戏曲题材**：民间「大红大绿」＋印象派冷暖转折（主色相 ≤5、高饱和为小面积点面）；仕女＝蛋形脸/修长身/忧郁眼（坐姿与屏风背景（马蒂斯式）、修长与忧郁（莫迪利亚尼（future）式））；戏曲人物「折叠」在画面上（平面化叠加、无固定视点、无叙事时间线）
5. **逆光暮色＋孤寂哀艳**：逆光、暮色、秋林、芦苇孤雁；黑树白水、黑白对照；画的是记忆与梦中的景（非对景写生）——「淡淡的哀愁与悲凉」与彩色「哀艳」并存（「宫花寂寞红」式对照）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Lin Fengmian-style lyrical modernism, ink and colour on xuan paper — a square, fully composed picture where Western form and Chinese ink melt into one:
one quiet subject — a seated lady with an oval face and melancholy eyes, a screen or round window behind her, a lotus or a slender vase nearby; or an opera figure folded flat across the picture; or a vase of gladioli, a cat, a lone heron over reeds, a dusk landscape with a black tree and white water;
block-shapes laid in broad washes answered by fast "iron-wire" brush lines — surface and line in duet, shapes appearing and vanishing between them;
the square filled edge to edge, four directions equally extended, no empty corner, no signature space;
colour mixed with ink — thick white gouache painted on for walls, lotus, pale robes and brides; deep black for crows, pines, fishing boats and hair;
a folk-ceramic palette warmed into dusk — vermilion, rose, jade green, lilac, raw sienna — bright and sad at once, like glazed Song ware; light of late afternoon or moonlight, soft edges where colour melts into the paper;
matte surface, gentle washes, colour pressed over ink and ink over colour, no gloss, no impasto, museum reproduction quality
```
**负向约束（`--no` 风格）**
```
--no pure flat colour blocks with hard-cut edges, paper cut-outs, wallpaper or textile patterns, fauvist saturated fields, decorative arabesque,
point-line-plane networks in silver-grey with scattered colour dots, all-over line mesh, abstract landscape without a subject,
academic modelling, anatomical chiaroscuro, hard cast shadows, single dramatic light source, sfumato, grisaille,
impasto, thick oil texture, glossy varnish, neon, HDR, 3D render, text, signature, watermark, frame
```

## 代码艺术规则（§8.2 原样）

1. **方构图规则**：帧纵横比 1:1±5%；四边触满率 ≥85%；无签名区/空角（负空间 ≤20%，且须为主动安排）。（自查：画幅检测＋分区直方图；对照 §3.1 判据②）
2. **墨彩调合规则**：墨-彩交织区（低饱和深色与彩色过渡带）≥30%；硬边色块（边缘梯度 >2× 中位梯度）<5%；无「先勾后填」闭合描边。（自查：边缘梯度图＋色域分割；对照 §3.1 判据①③）
3. **涂白规则**：主动白区（V≥0.85、S≤0.15）占 3–15%；白区内可见笔触纹理（高频能量中档）；与纸白留白并存。（自查：HSV 统计＋纹理能量；对照 §1-4）
4. **色域规则**：主色相 ≤5（墨黑/灰白/朱红/翠绿/紫/赭）；高饱和像素（S>0.6）≤12%；平均明度 ≤0.6；彩色以点面出现、不铺满。（对照 C-06/C-12）
5. **线弦规则**：快速书写线 ≥3 组（粗细均匀、露锋、曲率连续）；块面 ≥2 处；线不闭合、不作轮廓描边（非工笔填色）。（自查：线段方向直方图；对照 §1-2）
6. **孤寂母题规则**：每帧 ≥1 母题（仕女/戏曲人物/芦雁/孤鹜/猫/瓶花/暮景）；无叙事性事件与情节；情绪基调「哀而不伤」。（自查：母题库＋情绪分类器）
7. **几何秩序规则**：近方形/圆/弧的几何构成 ≥2 处；透视有意变形（桌面/门窗/瓶罐至少一处不合透视）。（对照 §1-8）
8. **渗化规则**：边缘柔度中等（笔触边界羽化 1–3px 等效）；无 3D 光影与硬投影（须显式声明「柔边、无硬边投影」）；表面哑光（高光连通域 ≤1）。（对照 C-01/C-05/C-18）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1/2/3/5 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。与 `conflicts.md` 的关系：**C-01**（硬阴影——林「柔边渗化」显式声明）、**C-05**（笔触——林「薄涂渗化、可见但非厚涂」档）、**C-06**（饱和度——林「中低＋民间色小面积」）、**C-12**（色相面积——墨与灰白为底）、**C-17**（负空间——「涂白」为主动元素）、**C-18**（形体——抒情线面）为组合预检重点。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **方纸布阵度（Squared Format）**`[归纳]` | 长方形/立轴式残余 | 近方形（1:1±10%） | 正方形满幅、四方等量、无签名位 | **85%** |
| P2 | **墨彩调合度（Ink–Colour Fusion）**`[归纳]` | 墨彩分施（先墨后彩） | 局部交融 | 墨彩齐下、墨中叠彩、彩中叠墨 | **70%** |
| P3 | **涂白度（Painted Whites）**`[归纳]` | 传统留白为主 | 灰白层次 | 大块涂白、叠白、「白分五彩」 | **55%** |
| P4 | **民间色度（Folk / Ceramic Palette）**`[归纳]` | 浅绛水墨 | 民间色点缀 | 瓷绘浓艳＋印象派冷暖、「大红大绿、天真烂漫」 | **60%** |
| P5 | **孤寂度（Solitude & Melancholy）**`[归纳]` | 平和明媚 | 淡哀愁 | 悲凉哀艳、孤鹜/黑衣女/暮色 | **65%** |
| P6 | **折叠几何度（Fold & Geometry）**`[归纳]` | 自然写实 | 几何化变形 | 时空折叠、皮影几何、多视点平面 | **50%** |

> **用法**：P1/P2 定「是不是林风眠」的起步（两条中 ≥1 条 ≥ 中档才成立——方纸布阵或墨彩调合）；P3 定「白」的档位（中档=灰白层次，强档=涂白）；P4 定色域（民间色为小面积点面，不得铺满）；P5 定情绪档；P6 定几何/折叠档。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若「点线面独立成网＋银灰统调＋彩点」→ 越界**吴冠中**；② 若「纯色平涂、剪裁硬边、剪纸/图案」→ 越界**马蒂斯**；③ 若「明暗交界线＋解剖素描＋主题性大构图」→ 越界**徐悲鸿**；④ 若「积墨黑体＋亮口＋逆光」→ 越界**李可染**；⑤ 若「零对象、纯抽象形式」→ 越界**康定斯基/赵无极侧**。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 吴冠中）**（× 吴冠中；本卡 §3.1 分工条款（第一写死条款））：师生线两档：林＝构图/色块（方纸布阵＋块面线弦，形式服务抒情）vs 吴＝形式抽象（点线面独立成网＋银灰彩点，形式即主题）——四判据（造型单元／构图与留白／色彩／路径）；判定不得只看「方形/墨彩」，须看①点线面是否独立为形式主体、②是否银灰统调彩点化；对侧缺项：`wu_guanzhong.md` §3.1 无「vs 林风眠」条款
- **分工（vs 马蒂斯）**（× 马蒂斯；本卡 §3.1 分工条款（第二写死条款））：色块两档：西方平面 vs 水墨色块——四判据（色块性质／明暗与光／色彩来源与功能／平面生成）；判定不得只看「色块＋平面」，须过①色块性质、②明暗两轴；对侧缺项：`matisse.md` §3.1 无「vs 林风眠」条款
- **分工（vs 徐悲鸿）**（× 徐悲鸿；本卡 §3.1 分工条款（对称落地））：同代四路径之三：写实融合 vs 现代主义融合——四轴（造型／构图／色彩／主义；与 `xu_beihong.md` §3.1 预写逐字对齐）；本档即对侧「落盘后复核」的落地（对侧状态词待更新）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01 硬阴影（柔边渗化/无硬边投影，须显式声明）／C-05 笔触（薄涂渗化、可见非厚涂）／C-06 饱和度（中低＋民间色小面积）／C-12 色相面积（墨与灰白为底、彩色为点面）／C-17 负空间（涂白为主动元素）／C-18 形体（抒情线面、柔边流动档）；句式改写：C-14（「渐变仅限宣纸渗化与墨彩过渡，不得成平滑数码渐变」）＋声明「哑光、渗化、色墨互叠、无清漆」；不借塞尚结构色块、莫奈色点分解、齐白石大写意、李可染逆光积墨

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/lin_fengmian.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
