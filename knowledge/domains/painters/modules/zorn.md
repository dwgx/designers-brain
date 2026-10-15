# 佐恩 模块卡 — `zorn`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/zorn.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **四色封闭系统（色板宽度）**：黑／白／赭／朱为主色（≤4 族）；黑代蓝（黑＋白冷灰在暖赭旁读作蓝）——「限制迫使诚实地使用明度关系」
2. **单点朱红**：全画面唯一饱和点（S ≥0.6）≤3% 面积且单连通域（唇／缎带／别针）——其余面积 S ≤0.35
3. **安置的过渡**：亮暗过渡由 2–4 级离散笔触构成、从不混合（「never blended the light-shadow edge」）——明度优先、先两值后细节
4. **水彩＋蚀刻双艺**：水彩＝透明层＋纸白（≥10%）＋水光公式；蚀刻＝平行线骤雨（无线廓、近乱远成形、手刮）——两门精准手艺
5. **受控侧光＋不设防的瞬间**：北窗稳定光／北欧夏夜光；人物在动作中途（「he is not posing, he is living」）——题材三联：肖像／户外裸体／达拉纳民俗

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Zorn-style painting with a closed four-colour palette — the discipline of control, not display:
a figure painted directly from life in one flow, no preliminary drawing; large hog-bristle brush marks placed as discrete strokes, light-shadow transitions stated as steps, never blended;
tones built from a closed set — lead white, yellow ochre, vermilion, ivory black; ivory black mixed with white standing in for blue; low-chroma field of ochre, warm grey and black;
one single saturated note of vermilion spent deliberately — a lip, a cheek, a ribbon, a pin — in an otherwise muted field;
canvas toned to a grey-red middle value before the first stroke; lights built with ochre and white, darks kept transparent, pure white reserved for the final small thick highlights;
a single source of controlled light — a large north window for portraits; pale cold Nordic summer-night light or reflections off water outdoors — side light with warm-cool control inside the four colours;
subject: Swedish burghers and international sitters, or nude bathers among rocks and water, or Dalarna folk life (dances, boats, timber interiors);
figure caught mid-action, unguarded, not posing; precision of drawing and value is the bravura — edges placed, forms simplified into one light mass and one dark mass before nuance;
[watercolour variant] transparent washes, soft tones laid first and a few rapid dark strokes after the paint dries, paper left white for the brightest light, water reflections built from the white of the paper;
[etching variant] pure needle etching — parallel line-masses like showers of lines, no contour lines, values born from the spacing of the hatching, hand-scraping for tone, forms emerging from interrupted lines, illegible up close, recomposing at a distance;
19th-century oil on canvas / watercolour on paper / etching on copper, museum quality, Scandinavian light
```
**负向约束（`--no` 风格）**
```
--no wide-spectrum palette, many saturated hues, rainbow accents, fauvist colour chords, high-chroma complementary pairs,
soft blended light-shadow edges, sfumato gradients, airbrushed transitions, glossy academic finish, tight invisible brushwork,
visible preliminary drawing, ruled construction lines, layered glazing, heavy impasto fireworks, palette-knife surface events,
flamboyant once-only strokes as the subject, theatrical bravura for its own sake,
single candlelit spotlight with near-black background, dramatic tenebrism, hard-edged chiaroscuro,
silver-grey atmospheric envelope, contours dissolving into air,
white-on-white as the subject, direct blazing noon sunlight,
digital smoothness, photo-bash, 3D render, cartoon, text
```

## 代码艺术规则（§8.2 原样）

1. **色板收束规则**：主色相 ≤4 族（H 直方图峰 ≤4）；无独立蓝色相（蓝感来自黑+白混合区）；高彩度（S ≥0.6）面积 ≤3%。自查：HSV 直方图 + 色相族聚类。（依据：[R11]；[R16]）
2. **单点朱红规则**：全帧高饱和（S ≥0.6）连通域 1–2 个，且落在焦点附近（距三分点/画面中心 ≤15% 短边）；其余面积 S ≤0.35。自查：饱和度掩膜 + 连通域 + 位置检测。（依据：[R16]「spent it deliberately」；[R3]《仲夏之舞》红腰带）
3. **明度结构规则**：亮块（V ≥0.7）面积 ≥35%、暗块（V ≤0.3）面积 ≥20%；中间调以离散色阶构成（色阶计数 2–4 级）。自查：明度直方图 + 色阶分割。（依据：[R8][R16]）
4. **过渡安置规则**：亮暗边界**无平滑渐变**（边界梯度带宽 ≤1.5% 短边）；过渡带由可见笔触阶跃构成（阶跃数 ≥2）。自查：边缘梯度带宽 + 阶跃检测。（依据：[R16]「never blended」；[R8]）
5. **光规则**：单一主导光源（亮暗分界夹角 ≤45°）；**暗部透明**（暗部均值 V ≥0.15；近黑 V ≤0.1 大块面积 ≤10%）。自查：亮度直方图 + 光源方向估计。（依据：[R1] 北窗；[R3] 夏夜光）
6. **笔触安置规则**：可见笔触覆盖 ≥55%；无 >12 px 的无笔触平滑区；笔触方向族 2–5 个（面部收敛、织物/水活跃）。自查：笔触覆盖掩膜 + 方向场。（依据：[R16]；[R9]）
7. **水彩变体规则**（媒介参数）：纸白保留 ≥10%；色层 2–4；快速扫笔方向族 ≥2；水面高光由纸白构成（暗部区内白像素连通域）。自查：纸白掩膜 + 层数直方图 + 高光定位。（依据：[R9] 水彩公式；[R2] 水光）
8. **蚀刻变体规则**（媒介参数）：平行线族方向一致性 ≥80%（主方向 ±15°）；**无轮廓线**（边缘连续性 ≤40%，形体靠线中断）；明度与线距相关（采样区明度 vs 线距相关系数 ≥0.6）。自查：方向场 + 边缘连续性 + 相关分析。（依据：[R10]「Les valeurs naissent du rapprochement ou de l'éloignement des tailles」；[R2]）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–6 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **色板收束度**`[归纳]` | 5–6 主色（早期水彩/风景档，允许少量蓝绿） | 四色为主 + 少量例外（钴蓝/铬绿点缀——《自画像在红中》类） | **严格四色封闭**（肖像纪律档——Harrison 1909 / 1896 自画像档） | **70%** |
| P2 | **明度结构强度**`[归纳]` | 柔和过渡、细节优先（水彩档） | 两值简化 + 中间调安置（主档） | 两值骨架 + 过渡全用离散笔触、禁混合（晚期肖像档） | **65%** |
| P3 | **光类型**`[归纳]` | 画室漫光（早期肖像档） | 北窗/侧光受控光（肖像主档） | 北欧夏夜/水边反射光（户外档）或火光/烛光（民俗室内档） | **60%** |
| P4 | **精度/「控制即炫技」档**`[归纳]` | 速写式即兴（蚀刻小品/水彩草稿档） | 完成度肖像（面部分离笔触、形准档） | 物证级精准（水彩高峰《仲夏之舞》细节/蚀刻肖像档） | **65%** |
| P5 | **题材/社会装置**`[归纳]` | 国际委托肖像（美国档） | 瑞典市民/乡土肖像与室内（市民档） | 达拉纳民俗场景或户外裸体（水边档） | **50%** |
| P6 | **媒介与即兴度**（工作流参数）`[归纳]` | 蚀刻（针法排练/完成品档） | 油画（主档） | 水彩（透明即兴档） | **油画** |

> **用法**：P1 + P2 定「是不是佐恩」（≥2 条 ≥中档才成立）；P1 + P2 + P4 是「四色控制」三件套；P3 定场景（画室/户外/民俗室内）；P5 定题材档；P6 是组稿参数（媒介轴，不进画面重叠计算，按 `expansion.md` §4.3 规则 5 归「工作流参数」栏）。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若色板放宽为多色相 + 多饱和点、笔触转向表演性炫技 → 越界进入**萨金特**档；② 若白上加白成为主题、光变为直射正午阳光 → 越界**索罗拉**档；③ 若蚀刻变为多工艺试验/私藏小品、产量与流通归零 → 越界**德加**档；④ 若出现**画外单光源 + 近黑背景 + 高光只落脸/手/道具** → 越界**卡拉瓦乔**档；⑤ 若色板收窄为单色/近单色（单色调色板）→ 越界**萨金特《持玫瑰的夏洛特》档**或**惠斯勒**方向（佐恩的单色作品属早期档，不是其身份）。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 萨金特）**（× 萨金特；本卡 §3.1 分工条款（与 sargent.md §3.1 四轴对齐））：色板宽度／炫技位置／题材·社会装置／光四轴；色板宽度轴单主（N3）＋ N1 反约束重算
- **分工（vs 德加）**（× 德加；本卡 §3.1 分工条款）：蚀刻：不同目标（过程／试验 vs 完成／公共）——四轴；蚀刻机制各单主
- **分工（vs 索罗拉）**（× 索罗拉；本卡 §3.1 互引条款（互查完成））：阳光白 vs 有限色板四轴；色板宽度轴单主（索不借四色封闭、佐不借全光谱）
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-05 笔触／C-12 色相面积／C-03·C-04 直方图／C-08·C-09 运动预算

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/zorn.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
