# 康定斯基 模块卡 — `kandinsky`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/kandinsky.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **零对象（成熟期非具象）**：可命名对象 ≈0；编号制标题（Composition/Improvisation No. X）——「像什么」的问题被取消
2. **元素可枚举＋线独立于形**：点/线/圆/三角/方/自由形类别 ≥3、可数元素 ≥8；线不闭合物体——细长连通域 ≥5、≥2 条穿越色块边界
3. **色彩声部化＋色彩-形式对应**：色相族 4–8、互补对 ≥1、高纯度并置；包豪斯期「圆↔蓝、方↔红、三角↔黄」对位声部
4. **中心构成/对位＋浅空间漂浮**：元素绕 1–2 个视觉中心（早期爆炸式涡旋）或全幅对位（晚期圆系）；无地平线/透视/接地投影
5. **黑的重音＋表面三档**：黑色像素占比 5–25%、含 ≥1 主形；表面按时期三档（厚涂刀痕/平匀硬边/砂质哑光）；母题残留梯度（骑手→零→生物形态）

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴；以「成熟期非具象 + 色彩声部」为默认档）**
```
Kandinsky-style non-objective composition — painting as visual music, no recognizable objects:
a cosmos of points, lines, circles, triangles and free-form shapes floating in a shallow luminous field;
colors treated as sounding voices — pure saturated hues in counterpoint, complementary pairs (red-green, blue-orange, yellow-violet);
one dominant circle or a central constellation as the anchor, with diagonal tensions crossing the field;
thin, independent lines that travel across color areas like a musical staff, never outlining objects;
black used as an accent mass, not as shadow; matte painted surface with visible brushwork, no gloss;
dynamic equilibrium — calm and tension held at once, everything weightless, no horizon, no perspective
[early expressive variant] softened contours, floating fragments of rider / hill / church dissolving into color patches
[Bauhaus variant] precise geometry — circle, triangle, straight lines — on a grid of quiet tensions,
primary colors with black, hard edges, flat even surfaces
```
**负向约束（`--no` 风格）**
```
--no recognizable objects, faces, figures, landscapes, still life, perspective, vanishing point,
horizon line, cast shadows, grounding, photographic realism, 3D render, glossy varnish, neon glow,
airbrushed gradients, symmetrical ornament, Mondrian-style black grid, paint splatter/drips,
monochrome minimalism, decorative wallpaper pattern, text, watermark, signature
```

## 代码艺术规则（§8.2 原样）

1. **零对象规则**：对象检测器（COCO 类）最高置信度 < 0.35，且不存在可命名对象区域；「看起来像脸/物」的强暗示 = 0。（依据：§1-1 `[研究]`[R14]）
2. **元素计数规则**：可数元素 ≥8；元素类别 ≥3（点/线/圆/自由形/多边形）；存在 ≥1 个「主形」（面积前 3 的连通域）。（依据：《点线面》元素清单 `[自述]`[R7]）
3. **色彩预算规则**：色相族 4–8（包豪斯档 3–5）；互补对 ≥1 组；高饱和（S≥0.5）像素面积 ≥15%；近单色档仅在「刻意克制」时允许且须显式声明。（依据：色彩声部化 `[自述]`[R6]；与 Lane B 色数上限的冲突按 C-15/N6 处理——康定斯基模块的色数**不在 ≤3 色上限域**内）
4. **线-色块关系规则**：细长连通域（线）≥5；其中 ≥2 条与 ≥2 个色块相交（穿越）；线不得闭合为物体轮廓（闭合线包围区内不得出现「可命名对象」）。（依据：线=独立轨迹 `[自述]`[R7]）
5. **空间规则**：地平线检测 = 0；消失点检测失败；画面无「接地投影」（底部接触阴影 = 0）。（依据：漂浮/浅空间 `[研究]`[R14]）
6. **漂浮/分布规则**：元素质心分布无「全压底部」或「全贴边」；元素与背景对比 ≥ 阈值且**无阴影连接**；上/下、左/右元素质量差 ≤ 35%（动态平衡）。（依据：对位与平衡 `[自述]`[R4][R17]）
7. **黑色重音规则**：黑色像素占比 5–25%（早期档 ≤30%）；黑色连通域 ≥1 个「主形」（面积 ≥ 全画 1%）；黑色不得仅作细线（需有块面级黑）。（依据：黑=重音 `[史料]`[R10][R14]）
8. **时期判据规则**（可切换档）：早期档 = 轮廓软 + 对象碎片 ≤2 + 不协和（色相对撞 ≥3 组）；包豪斯档 = 硬边 + 几何元素 ≥60% + 色形对应对 ≥1；巴黎档 = 生物形态 ≥3 + 砂质纹理（高频粗糙）+ 深色底 ≥40%。（依据：§4 P2 滑轨 `[归纳]`）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–3 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **非具象度（对象残留的反面）**`[归纳]` | 对象可辨：骑手/山/教堂仍读得出（1908–10 档） | 对象碎片残留（1911–14 档：锚点 ≤2 且被吞没） | 零对象：可命名对象 ≈0（1913 后成熟档） | **80%** |
| P2 | **几何化程度**`[归纳]` | 自由曲线/有机形为主（1911–14、1934–44 档） | 混合：几何与有机并置（1921、1933–35 过渡档） | 规整几何：圆/三角/直线/网格感（1922–33 包豪斯档） | **50%**（按时期切换） |
| P3 | **色彩声部强度**`[归纳]` | 2–3 色族、近单色（刻意克制档） | 4–6 色族、互补对 1–2 组 | 全谱对撞：多色族+互补对 ≥2+黑色重音（Composition VII/VIII 档） | **70%** |
| P4 | **线的独立性**`[归纳]` | 线=轮廓（贴边勾形） | 线与色块半独立（部分穿越） | 线=独立轨迹：悬空/穿越/成族（《点线面》档） | **75%** |
| P5 | **空间漂浮度（重力解除）**`[归纳]` | 浅空间叠层、有地面暗示 | 漂浮层次、无明确地面 | 全漂浮：无地平线、无重力、元素悬浮（Several Circles 档） | **65%** |
| P6 | **元素密度 / 事件数**`[归纳]` | 大色域+少元素（≤5 个主元素） | 中密度（6–12 个主元素） | 高密度（≥13 个主元素，Composition VII 级） | **50%** |

> **用法**：P1+P3 定「是不是康定斯基」（零对象 + 色彩声部；两条同时 ≥中档才成立）；P2 定时期（反几何→几何→有机的滑轨）；P4/P5 定「抽象语法纯度」；P6 是构图规模参数。
> **分工注（与 §3.1 对齐）**：P1 若为「弱」且 P2 为「弱」→ 回到「表现主义具象」域（本模块早期档，允许，但组合时按具象系处理）；P1=强 且 **P3=弱** 且 P2=强 → 蒙德里安域（**禁止**）；P3=强 且 P4=弱 → 滑向装饰平面（马蒂斯域，需错峰取值）。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 毕加索）**（× 毕加索；本卡 §3.1 分工条款）：解构↔抽象边界写死：对象锚点 ≥3＋近单色（毕）vs ≈0 对象＋色彩声部（康）——可组合但分轴（N3）
- **分工（vs 萨拉希）**（× 萨拉希；本卡 §3.1 分工条款）：抽象两路径：理论/音乐性（元素语法推导）vs 书法线（书写笔势＋文字残影）
- **分工（vs 吴冠中）**（× 吴冠中；本卡 §3.1 分工条款）：零对象＋油/版 vs 风景母题残留＋水墨——抽象化动力相反（内在必然 vs 自然形式简化）
- **分工（vs 恩格瓦雷）**（× 恩格瓦雷；本卡 §3.1 分工条款）：普世精神/音乐（符号无指涉）vs 土地与身体记忆（符号有大地指涉）
- **范围注**（× 蒙德里安/波洛克/罗斯科（未来模块）；本卡 §3.1 范围注）：不得借入黑网格与纯几何硬边/滴洒/色域模糊——出现即越界
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-15 色数上限 / C-16 反约束适用域 / C-17 负空间

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/kandinsky.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
