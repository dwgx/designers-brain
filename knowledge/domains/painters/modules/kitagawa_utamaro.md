# 喜多川歌麿 模块卡 — `kitagawa_utamaro`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/kitagawa_utamaro.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **大首绘特写＋构图三式**：头与肩占据画面——头部（含髪）高度 ÷ 画高 ≥40%（强档 ~50%+）、裁切位于肩—胸之间；正面/半侧面近距、三角形多人（三美人）、镜与后姿（姿見）三式，主体居中或轻偏、无强斜线——「近接した三分身」「首から上で切り取った特徴的構図」
2. **线条的微表情**：一見似て非なる脸——眉、细长目、鼻筋、小口由线段微差（≤3px 级但可辨）区分人物与情绪；「顔立ちや表情、目や眉、鼻の微かな違いで描き分け」
3. **毛描き＋無線空摺**：发丝一根一根逐根描写（「delicate lines to convey the form and flow of hair」）、密度显著高于衣纹；顔・首の輪郭に墨線を用いず、版の凹凸で表現（無線档）——肌肤自背景「浮出」
4. **背景压缩＋平面色域**：云母摺/素背景、无景深、无投影、背景道具 ≤2 件；无渐变（除轻ぼかし）、色不掩线、墨线主导；服饰图案（小纹·格子·縞·千鸟·菊）细密而色调克制（彩色像素 ≤50%、色相 ≤5 族）
5. **手势道具＋款印系统**：手拭·団扇·文·镜·ポッピン等道具承担情绪（≥1 处手—道具/面部交互）；款「哥麿筆」「相見 歌麿画」、自矜款「正銘歌麿」＋「自成一家」印、版元标记（蔦屋·上村）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Japanese ukiyo-e bijin ōkubi-e portrait in the manner of Kitagawa Utamaro (c. 1790s):
a single woman seen close up — head and shoulders filling most of the vertical ōban frame,
cropped at the shoulders, turned slightly to one side or gazing into a mirror;
elongated oval face, delicate features — narrow slit eyes, fine arched eyebrows,
long straight nose, tiny pursed mouth; the expression held in micro-differences of line,
calm and interior, a mood caught mid-thought;
skin without a printed outline, pale and luminous, floating free of the ground;
hair drawn strand by strand (kewari) — heavy black masses of the Shimada coiffure,
fine loose hairs at the temples and nape, combs and kanzashi as accents;
a flat background field — plain colour or softly glittering mica (kira-zuri),
no setting, no shadows, no perspective; at most one or two props — a round fan,
a folded letter, a hand towel, a mirror — held or touched by the hand;
kimono and obi patterned with small repeating motifs (stripes, checks, chidori plovers,
maple leaves, chrysanthemums), colour restrained: ink black, beni red, indigo blue,
yellow, white; flat decorative space; woodblock print texture, visible paper grain
```
**负向约束（`--no` 风格）**
```
--no western perspective, cast shadows, chiaroscuro, gradients, airbrush, sfumato,
photorealistic rendering, 3D render, oil-paint impasto, heavy texture, glowing highlights,
full-length standing figure, crowded background, landscape scenery, many subjects in action,
dramatic directional lighting, stage light, backlight, lens flare, anime or manga faces,
chibi proportions, sweet pastel palette, glossy surface, photograph, text or watermark
```

## 代码艺术规则（§8.2 原样）

1. **特写比例**：头部（含髪）高度 ÷ 画高 ≥40%（强档 ≥50%）；裁切线位于肩—胸之间；主体人形数 = 1（镜中映像计为同一主体）。`[归纳]`
2. **线系统**：無線档——面部边缘无连续墨线（面部轮廓线覆盖率 ≤10%）且靠底色对比读形；标准档——毛描き细线密度 ≥15 条/100px（发区）、衣纹主線单笔连续 ≥60px 占比 ≥50%。`[归纳]`
3. **背景规则**：背景为均质场（局部方差 ≤ 阈值）或云母纹理；背景道具 ≤2 件；投影/阴影面积 ≤2%；无透视消失点（收敛点 ≤1 且不在画内）。`[归纳]`
4. **色域规则**：肌肤区（低饱和高明度）≥25% 面积；墨/黑（发）≥12%；主色相 ≤6 族；渐变带宽度 ≤1% 短边（轻ぼかし ≤1 段）。`[归纳]`
5. **微表情差分规则**：同系列多帧时，眉/目/口线段的帧间差异 ≤3px 级（参考帧）但可辨——结构相似度落于 0.75–0.95 区间；禁「同脸复制」与「无差异」。`[归纳]`
6. **手势-道具规则**：≥1 处手部与道具/面部交互（持·触·托）；可辨手指数 ≥3；道具 ≤2 件；手部线密度高于衣纹（重点描写区）。`[归纳]`
7. **静帧语义**：单帧发布时按静帧处理——动画时人物位移 ≤1% 画幅/秒、转折（振り向き）≤1 次；禁叙事推拉与镜头运动（与德加卡「过程态」互斥，见 §3.1）。`[归纳]`

## 控制参数（§4 原样）

**P1 特写强度（Close-up）**（默认 强）`[归纳]`
- 弱: 全身像（早期清長风；《青楼仁和嘉女芸者部》档）
- 中: 半身胸像（《当時全盛美人揃》膝上裁切档）
- 强: 大首绘（頭部 ≥40% 画高；《浮気之相》《当時三美人》档）

**P2 线系统（Line Mode）**（默认 中）`[归纳]`
- 弱: 轮廓线明确（主線强、毛描き少）
- 中: 主線＋毛描き＋衣纹线（标准档）
- 强: 無線空摺（顔·首不施轮廓线＋空摺；《娘日時計》档）

**P3 背景处理（Ground）**（默认 中-强）`[归纳]`
- 弱: 有景（室内/道具组；《針仕事》档）
- 中: 素背景＋道具 1–2 件（団扇·文·镜）
- 强: 雲母摺/空摺纹理（大首绘档）

**P4 表情-心理强度（Expression）**（默认 中）`[归纳]`
- 弱: 中性静穆（正面无表情）
- 中: 微表情（眼神/嘴角/手势微差；《物思恋》档）
- 强: 叙事性情感（浮気/笑み/振り向き；《浮気之相》《ポッピン》档）

**P5 服饰图案密度（Pattern）**（默认 中）`[归纳]`
- 弱: 单色/极简纹
- 中: 小纹＋縞＋格子适量
- 强: 多色多纹满铺（千鸟·菊·藤；《瀧川》《物思恋》档）

**P6 动作幅度（Pose）**（默认 中）`[归纳]`
- 弱: 端坐/静止（《三美人》档）
- 中: 日常动作（手拭·団扇·読文）
- 强: 转折瞬间（振り向き·吹く·回眸；《ポッピン》档）

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 北斋）**（× 北斋；本卡 §3.1 分工条款（写死））：线/平面叙事分档：题材（风景·漫画·万物 vs 人物特写）／构图（非对称＋主斜线＋尺度戏法 vs 近距居中＋背景压缩）／线（等宽轮廓服务剪影 vs 主線＋毛描き、可切無線）／动势（动态事件 vs 静止心理）——四判据（①面部占比 ≥40% vs 剪影 ≤1/8 画高；②毛描き细线；③主斜线；④蓝预算 vs 墨＋紅＋膚）；两卡禁项互列（歌禁「人物剪影化/尺度戏法/蓝预算主导」；北禁「大首特写/毛描き细线满布/云母背景」）
- **分工（vs 德加）**（× 德加；本卡 §3.1 分工条款（写死；对侧备查互引 `modules/degas.md`，四轴对齐））：日常瞬间分档：瞬间性质（定格美·完成态 vs 抓拍·过程态）／构图（制式肩胸裁切 vs 偏心裁切 ≥15%）／视点（对望·镜中 vs 背面·侧背）／光（平光·云母材质光效 vs 人工光源·亮暗分区）——四判据（①正面可读 vs ≥1/3 背对侧背；②无边缘切割 vs ≥1 处；③无方向光源 vs 方向光源/光路；④完成态静帧 vs 过程态瞬间）；两卡禁项互列（歌禁「人工光分区/偏心抓拍裁切/背面主导」；德禁「云母平光/正面大首/制式肩胸裁切」）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-05 表面系统／C-12 色相预算（墨＋紅＋膚色域）／C-17 负空间（背景压缩、无景深）；不借北斋的斜线戏法与蓝预算；不借德加的人工光与偏心裁切

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/kitagawa_utamaro.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
