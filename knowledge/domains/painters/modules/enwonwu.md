# 本·恩沃恩乌 模块卡 — `enwonwu`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/enwonwu.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **雕塑性体量（「雕塑家的画」）**：形体以块面/体量成立、人物如雕像般「立起」；剪影清晰、内部平实（主要人物外轮廓完整、缩至 256px 可辨；单形体内部明度层 ≤4）——「他始终把自己描述为雕塑家」
2. **假面/舞蹈/神祇图像志＋肢体层叠**：mmuo（假面）、agbogho mmuo、舞蹈、Anyanwu/Sango 神祇——文化-精神主体、非装饰（元素同框 ≤3 类防奇观化堆叠）；≥2 组肢体重叠或斜向动作线（「layering of limbs」）；运动以姿态表达（0 帧运动模糊）
3. **尊严的肖像＋均匀漫射光＋浅空间**：3/4 或正面、长颈（颈长/头长 ≥0.4）、姿态挺直、平静或平视凝视；面部明暗对比 ≤2.5:1、硬边阴影 0 处、暗部明度 ≥纯黑+10%；背景层数 ≤2、收敛线 ≤1 组、无叙事杂物
4. **暖土色域＋点状高饱和＋笔触两档**：赭/棕/红/金为底（暖色 ≥50%、冷色 ≤25%）；高饱和集中小面积（头巾/珠饰/衣布；8–25%、连通域 ≤4）；笔触面部收敛（「deft brushwork」）、衣饰放开（「diaphanous treatment」），风暴档转粗厉大笔触（「bold, slashing brushstrokes」）
5. **拉长「上升」形体＋象征克制**：长宽比 ≥4:1 立柱式形体、曲线为主轴、顶天立地「上升感」（「把元素拉长如音乐的主音」）；象征性元素 ≤3 类、无文字/标语、情绪中性偏庄严（非宣传化）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
A mid-20th-century Nigerian modernist portrait in the manner of Ben Enwonwu — a sculptor's painting:
a young Nigerian woman in traditional Yoruba dress, a richly patterned gele head-tie, her long neck rising against the folded cloth, seen in three-quarter view with a calm, self-possessed gaze — or, looking back over her shoulder, regal and serene;
the figure conceived as a solid volume — clear silhouette, broad planes, drapery folded like carved cloth; the face modelled with quiet care, ornaments and fabric given with freer, decisive strokes;
warm earth palette — ochre, burnt sienna, terracotta, deep brown, gold — with one or two saturated accents (indigo, turquoise, lemon) kept small and deliberate;
even, diffused light that keeps every form legible; shallow space, the background a flat warm wall or a quiet dark ground;
the mood of a national icon — dignified, self-possessed, quietly monumental;
oil on canvas, museum quality, mid-century African modernism
[dance / masquerade variant] a whirling masquerade figure with an elaborate headdress caught mid-step — limbs layered and overlapped to suggest movement, the body a curved sculptural mass; warm earth ground with saturated costume accents; the movement held in the pose, no blur
[sculpture variant] a tall, slender bronze or dark-wood figure rising out of a block — arms lifted toward the sun, an elongated curve tapering to a point, "wonderfully and precisely balanced"
```
**负向约束（`--no` 风格）**
```
--no Western society-portrait bravura, alla prima dashing brushwork as display, high-key glamour lighting, courtly psychological drama, fans and ballgowns and brocade sofas,
--no colonial exoticism (no "juju" spectacle, no safari or ethnographic props), no folklore clichés,
--no hard chiaroscuro, no single theatrical spotlight, no near-black tenebrism,
--no cubist fracture, no abstract expressionism, no all-over pattern without a figure,
--no photographic hyperrealism, no digital smoothness, no text, no watermark
```

## 代码艺术规则（§8.2 原样）

1. **雕塑性剪影规则**：主体外轮廓完整（无断裂）；缩至 256px 主体可辨；主体内部明度层 ≤4（块面化，非连续渐变）。自查：轮廓连通域 + 缩略图目检 + 明度直方图。（依据：[R19]「described himself as a sculptor」；[R7] 展评）
2. **暖土色域规则**：暖色（红/橙/黄/赭/棕系）面积 **≥50%**；冷色 **≤25%**；高饱和（S≥0.5）面积 **8–25%** 且连通域 ≤4 处（点状点缀）。自查：色相直方图 + 连通域计数。（依据：图库全作品对照；[R3] 头巾/衣布）
3. **均匀光规则**：面部明暗对比 **≤2.5:1**；硬边阴影 0 处（阴影边界梯度 >15%/px 者 = 0）；暗部明度 ≥纯黑+10%。自查：面部区域对比度 + 阴影边界梯度。（依据：[R14] 描述与作品对照；反卡拉瓦乔/萨金特域）
4. **图像志规则**：仪式/舞蹈档 ≥1 个可辨认的假面/舞蹈/神祇元素；肖像档 ≥1 件民族服饰/头巾元素；符号元素同框 **≤3 类**（防奇观化堆叠）。自查：元素分类计数。（依据：[R13]「coded resistance」；[R14]）
5. **运动/舞蹈规则**：≥2 组肢体重叠或斜向动作线；全片 **0 帧运动模糊**（运动以姿态表达）；躯干/肢体轴向偏垂直 ≥10° 者 ≥2 处。自查：姿态估计 + 运动模糊检测。（依据：[R20]「layering of limbs」）
6. **肖像视角规则**：3/4 或正面；长颈（**颈长/头长 ≥0.4**）；视线平静（眉眼口形变 ≤15% 中性面）**或**直接平视观者（Children of Biafra 档）——二选一，不得混用。自查：视角估计 + 面部形变。（依据：[R3][R14]）
7. **织物/图案规则**：头巾/织物图案区 **5–30%** 面积；图案为块面/条纹/几何（gele 式）；无细密满铺。自查：图案区面积 + 纹理尺度。（依据：[R3]「richly-patterned head tie」）
8. **浅空间/背景规则**：背景层数 **≤2**；收敛线 ≤1 组；肖像档背景无叙事物（墙/暗底/平色）。自查：区域分割 + 消失点估计。（依据：[R3]「背景被省略」类著录；[R7]）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–8 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **雕塑性体量度**`[归纳]` | 平面/绘画性主导（线条＋色块） | 形体有块面、剪影清楚（肖像档） | 雕像式体量——块面/剪影/「立起」感（雕塑本体＝100%） | **70%** |
| P2 | **民族图像志密度**`[归纳]` | 无（纯肖像/纯风景） | 1–2 类（服饰/头巾/织物纹样） | ≥3 类（假面/舞蹈/神祇/王室/建筑同框） | **55%** |
| P3 | **舞蹈/运动强度**`[归纳]` | 静态（肖像/静物） | 姿态动势（一个动作瞬间） | 旋动群像/肢体层叠（dance forms 档） | **60%** |
| P4 | **暖土色域强度**`[归纳]` | 灰/冷调 | 暖底＋冷色点缀 | 全画面暖土（赭/棕/红/金）＋点状高饱和 | **75%** |
| P5 | **光均匀度（反戏剧度）**`[归纳]` | 戏剧性明暗（越界档，见下） | 单侧柔光 | 漫射均匀光、形体全可读 | **70%** |
| P6 | **媒介/材质**（工作流参数）`[归纳]` | 纸本（水彩/素描速写） | 油画（肖像/舞蹈/风景主档） | 木雕/铜雕（三维公共档） | **油画（绘画）/木雕（雕塑）** |

> **用法**：P1＋P4 定「是不是恩沃恩乌」（两条中 ≥1 条强档＋另一条 ≥中档才成立）；P2/P3 定题材档（肖像→舞蹈→仪式）；P5 定光档；P6 是组稿参数（媒介轴，不进画面重叠计算，按 `expansion.md` §4.3 规则 5 归「工作流参数」栏）。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若出现**主导光＋高调亮部＋织物炫技**→越界**萨金特**域；② 若出现**大面积饱和色域＋色调情绪＋村庄静默**→越界**谢尔吉尔**域；③ 若出现**象征符号堆叠＋静物神像＋装饰纹样满铺**→越界**高更**域；④ 若出现**硬光开关（画内无光源、亮部只落脸/手）**→越界**卡拉瓦乔**域；⑤ 若出现**标准化神像＋达显正面＋法器清单**→越界**拉维·瓦尔马**域。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 萨金特）**（× 萨金特；本卡 §3.1 分工条款（第一写死条款））：肖像：西方炫技 vs 非洲现代性——四轴（笔触与完成度／肖像的社会装置／光与色／形体观）；判据①–④（表演 vs 建构／社交身份 vs 民族象征／主导光+高调 vs 均匀光+暖土／绘画性 vs 雕塑性）；「肖像」轴单主（N3）、70/30 起；对侧缺项：`sargent.md` §3.1 无「vs 恩沃恩乌」条款
- **分工（vs 谢尔吉尔）**（× 谢尔吉尔；本卡 §3.1 分工条款（第二写死条款；与 `sher_gil.md` §3.1 互锁））：非西方现代主义两路径：后印象派转译 vs 西非雕塑传统转译——四判据（形式家谱／身体功能／饱和色分布／作品功能）；「非西方现代主义」轴单主、同用须显式分区或二选一；不得混用凝视制度；对侧缺项：`sher_gil.md` §3.1 无「vs 恩沃恩乌」条款
- **次级注记（vs 高更 / 卡拉瓦乔 / 毕加索 / 萨金特 / 佐恩）**（× 高更 / 卡拉瓦乔 / 毕加索 / 萨金特 / 佐恩；本卡 §3.1 次级注记）：不借高更的象征符号装置（假面/神祇＝文化-精神主体，非异域奇观）／不借萨金特·佐恩的社交炫技／不借卡拉瓦乔硬光开关（恩＝均匀漫射光）／不借毕加索的形体重组（形体完整圆润）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-05 笔触可见度（可见但受控，须显式取值）／C-12 色相面积预算（暖土 ≥50%＋冷色退居）／C-01 硬阴影（与 Lane B 默认同侧，声明「无硬边投影」）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/enwonwu.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
