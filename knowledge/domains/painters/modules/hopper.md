# 霍珀 模块卡 — `hopper`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/hopper.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **硬边光影**：亮暗边界近乎刀切、投影锐利、方向一致且平行（长投影）——「crisp light/shadow」
2. **几何化建筑块面**：建筑／窗／墙简化为矩形（「radically simplified」）；正交几何主导
3. **无人／稀疏人烟**：人物 0–3、互不交流；窗／门槛母题（frame-in-frame）；阈限空间
4. **夜间人造光／霓虹**：光池＋深色环境高对比（「harsh electric light」）；日光本身是主角（几何光斑）
5. **电影式取景＋凝滞瞬间**：非常规裁切、从外看内——「just before or just after the climax」，无动作

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**

```
American realist painting of a modern city scene, hard-edged directional light with sharp cast
shadows and crisp boundaries between light and shade, simplified rectilinear architecture reduced
to large geometric blocks (storefront rows, diner, gas station, hotel room, movie theater, office),
empty or sparsely populated space — at most one or two solitary figures, turned away or absorbed,
not interacting, a window, door or counter acting as a frame-within-the-frame, muted field of ochre,
brick red, olive green and bone white pierced by a few saturated accents (red barber pole, green
storefront, yellow gas pumps, blue sky), sunlight falling as clear geometric shapes on walls and
sidewalks, long parallel cast shadows, cool deep shadows with detail (not black), cinematic viewpoint
as if seen from the street or from a passing train, frozen stillness just before or after an event,
20th-century American urban or coastal setting, oil on canvas, simplified painterly surfaces with
restrained brushwork
```

**负向约束（`--no` 风格）**

```
--no soft diffused window light, sfumato, hazy atmosphere, mist, pointillé highlight dots,
candlelit tenebrism, near-black background with single dramatic light, impressionist broken
brushwork, heavy impasto, rainbow neon palette, crowded busy street, motion blur, action or
movement, text, watermark, signature, fantasy elements, pastoral idyll, 17th-century Dutch interior,
warm nostalgic glow
```

## 代码艺术规则（§8.2 原样）

| # | 规则 | 可判定阈值（默认） | 自查方法 |
|---|---|---|---|
| 1 | **硬边光影** | 亮暗边界过渡带 ≤2 px（1024 px 宽画布）；禁止 ≥8 px 的羽化渐晕 | 对明暗交界做梯度宽度统计，取中位数 |
| 2 | **投影几何一致** | 所有投影方向同一光源方位（偏差 ≤5°）；投影为简单多边形（边数 ≤6） | 投影主轴角度直方图 + 形状简化度 |
| 3 | **正交几何主导** | 建筑长边 ≥70% 与水平/垂直轴夹角 ≤2°；画面矩形块 ≥6 个 | 边缘角度直方图 / 霍夫直线统计 |
| 4 | **人烟预算** | 人物数 ≤2（默认 0–1）；若有人物：占画面积 ≤8%，且无互动（视线不相交、无肢体接触） | 人物检测 + 面积与视线向量检查 |
| 5 | **色域与两级明度** | 色相簇 ≤7；亮部（≥75%）与暗部（≤35%）像素合计 ≥60%，中间调压缩；夜档暖光池面积 ≤25% 且集中在光源/照射面 | 逐帧直方图 + 色相聚类 |
| 6 | **光源数受控** | 昼档：1 个太阳方向；夜档：≤3 个可见光源，各带明确照射面；禁止无源漫射光 | 高光/光源连通域计数 |
| 7 | **全片静止** | 相机固定；帧间差 ≤1%（除光源闪烁 ≤2 Hz 外不允许运动元素） | 帧差图：非光源区域非零像素占比 |
| 8 | **画中框取景** | 至少 1 个画中框（窗/门/镜/柜台）且被画边裁切 ≥1 处；主体（若存在）距画面中心 ≥1/8 宽 | 边界框位置与边缘相交统计 |

> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；与 `templates/style_card.md` 的填写规则对齐。第 5 条的"两级明度"对应 *Nighthawks* 式"酸性高对比"与昼档"阳光块面"两种情形。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **光影硬度**（Light–Shadow Edge Hardness）`[归纳]` | 漫射柔光、边界模糊（**越界：进入维米尔档**） | 清晰光源，但边缘仍柔、投影短 | **硬边光 + 锐利投影**，亮暗边界近乎刀切，投影平行且几何化 | **85%**（本模块身份） |
| P2 | **几何简化度**（Geometric Simplification）`[归纳]` | 细节较全、纹理可见（早期水彩） | 块面化，细节选择性省略 | 建筑=矩形组合，"radically simplified"；字不可读、装饰略去 | **80%** |
| P3 | **孤寂度**（Emptiness / Isolation）`[归纳]` | 2–4 人且存在互动（少见档） | 1–2 人、互不交流（couple 画法） | **无人或单人（背对/低头）**，空间本身成为主体 | **75%** |
| P4 | **夜光配比**（Artificial-Light Ratio）`[归纳]` | 纯日光（*Ground Swell*） | 黄昏混合光（*Gas*：自然光＋人造光） | 夜间人造光主导、霓虹/灯窗光池（*Nighthawks*） | **50%**（日/夜双档可用） |
| P5 | **取景电影化**（Cinematic Crop）`[归纳]` | 正面全景、主体居中（习作） | 非对称取景、视点明确 | 边缘裁切 + 画中框（窗/门/柜台）+ 从外看内的视点 | **70%** |
| P6 | **色彩对比策略**（Color Contrast）`[归纳]` | 全画面低对比灰调 | 灰调 + 局部饱和色点 | 大面积互补对撞（红绿/黄蓝）+ 亮暗两级压缩中间调 | **65%** |

> 用法：**P1/P2 定"是不是霍珀"**（硬边 + 几何）；P3/P5 定"孤独与取景"（无人/画中框）；P4/P6 切"日档还是夜档"（昼：P4 低、亮部大；夜：P4 高、光池 + 冷暗域）。三档描述可直接作判定标准写进自查表。
> 数据来源：档位阈值取自 [R1][R5][R7][R10][R13][R20]；**档位划分本身为 `[归纳]`**（本项目操作化建议，未经渲染实验校准）。
> **分工注（与维米尔，必须写死）**：P1 强档（硬边光）＋P2 强档（几何简化）是本模块专属；**"柔窗光 + 点状高光（pointillés）"组合整体属于维米尔模块，禁止在本模块同档出现**——需要柔光时不得同时保留本模块的"无人 + 硬边投影"标志机制（见 §3 分工口径与 §8.1 越界警报）。本注为 `[归纳]`。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **C-01**（× Lane B「硬阴影」禁令；本卡 §8.2-1）：硬边光影按 C-01 同口径显式改写（给出半影宽度值）
- **分工（vs 维米尔）**（× 维米尔；本卡 §4 分工注 + §8.1 负向段）：光影硬度：硬边光＋几何简化 vs 柔窗光＋点状高光——同屏显式分区，默认二选一
- **越界（vs 卡拉瓦乔）**（× 卡拉瓦乔；本卡 §8.2-6）：夜景光源结构：城市电光（多实用光源）vs 单一烛光＋近黑背景（戏剧结构）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/hopper.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
