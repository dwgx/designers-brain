# 里维拉 模块卡 — `rivera`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/rivera.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **公共建筑尺度的群像**：单面墙人形 ≥20、单人 ≤ 画面高 1/4、人群面积 ≥40%——无单一主角；历史全景跨 ≥3 个时代元素
2. **建筑一体化＋工程精确**：构图轴与建筑轴偏差 ≤10%、≥1 个建筑构件参与构图（东＝初生／西＝终末）；机械零件 ≥5 可辨、全焦平面
3. **面孔双轨制＋劳动者体量**：可指认肖像 ≥2／面（列宁／萨帕塔／福特）＋类型化群众；肩宽／手掌夸大、体块 > 细节（力量来自劳动）
4. **土色底＋民间亮色＋象征汇编**：土色系 ≥60%、高饱和 ≤25% 成块（墨西哥红／钴蓝／玉米黄）；符号成对 ≥2 组（生／死、建设／毁灭）
5. **水平分带＋蛇形线＋哑光材料感**：水平带 ≥2 层、消失点 0；流程线横穿 ≥60% 宽；镜面高光＝0、giornata 接缝可检出

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Mexican muralist public fresco in the manner of Diego Rivera — a monumental public mural narrative:
dozens of monumental working figures — workers, peasants, soldiers, market women — arranged in broad
processional bands along sweeping serpentine lines (conveyor belts, rivers, roads, banners), all moving
in one collective direction; no single protagonist, no portrait focus — the crowd itself is the subject;
historical panorama compressing centuries on one wall: Aztec and pre-Columbian motifs beside colonial
friars, revolutionary soldiers and modern machinery, each era legible by dress, tools and architecture;
engineering-precision objects — blast furnaces, stamping presses, assembly lines, turbines — rendered
sharply, every part readable, no depth-of-field blur; composition integrated with the architecture:
level band divisions, arch and doorway shapes echoed in the layout, symmetrical axes locked to the wall;
matte buon-fresco surface — pigments absorbed into lime plaster, no gloss, no varnish reflections, faint
giornata seams; earth-tone palette of ochre, terracotta, umber and grey-green covering most of the wall,
with folk-bright accents (Mexican red, cobalt blue, maize yellow) in clothing, fruit and banners;
flesh modeled in simplified, heavy volumes — the monumental body of labor; equal diffuse daylight,
no dramatic single-source shadow, no candlelight; symbols paired as contrasts: life/death half-face,
construction/destruction, north/south, past/future; hand-lettered banners rare and functional
```
**负向约束（`--no` 风格）**
```
--no single heroic portrait focus, intimate small-scale easel painting, domestic interior, dream
surrealism, candlelit chiaroscuro, single-source dramatic spotlight, altar or church iconography,
deep single-point perspective, vanishing-point corridor, soft-focus bokeh, shallow depth of field,
pastel palette, watercolor wash, glossy oil sheen, visible impasto brushwork, gold leaf decoration,
horror vacui ornament, anime, cartoon, 3D render, HDR, watermark, museum frame
```

## 代码艺术规则（§8.2 原样）

1. **群像密度规则**：单帧可辨人形 **≥12**；人群面积占比 **≥40%**；单一人形面积 ≤15%（防肖像化）。自查：人物检测 + 实例分割 + 面积统计。（依据：[R7]「multi-figure」；§1-1）**豁免注**：纯象征/构件面板（如 Power House 单色件）按 P1 弱档豁免、以整周期主面板计。
2. **流程线规则**：检出 **≥1 条主导流程线**（传送带/队列/河流/弧线）横穿画面 ≥60% 宽度；人群朝向一致度 **≥70%**。自查：光流方向直方图 + 曲线拟合。（依据：[R7]「serpentine conveyors」；§1-10）
3. **分带构图规则**：水平叙事带 **≥2 层**（带边界倾角 ≤5°）；单点消失点 = 0 或 ≥2 个互相矛盾；层带各自承载不同叙事环节。自查：边缘方向直方图 + 消失点估计。（依据：[R5] Frozen Assets 三层；§1-9）
4. **建筑一体规则**：画面内 **≥1 个建筑构件**（拱/门/柱/楼梯）参与构图；构图对称轴与画框/拱形轴偏差 ≤10%。自查：结构线检测 + 对称轴度量。（依据：[R7] 四墙方向象征；§1-3）
5. **物象精确规则**：机械/工艺物体清晰度 ≥主体 80%；单件可辨零件 **≥5**；全焦平面（无 ≥2px 高斯虚化区）。自查：清晰度图 + 边缘计数 + 模糊核检测。（依据：[R7]「engineering precision」；§1-4）
6. **色域规则**：土色系（赭/砖红/灰绿，含去饱和）面积 **≥60%**；高饱和亮色区（S≥0.7）**≤25%** 且成块分布；纯黑（V≤0.05）面积 ≤5%。自查：HSV 掩膜统计。（依据：[R3][R7]；§1-7）
7. **平光规则**：画内单点强光源 = 0（高亮连通域 ≥2 且成带状即为「无单点」）；阴影边界过渡带 **≥1% 短边**（软于米开朗基罗 ≤0.6% 的硬边档）；全帧明度中位 0.35–0.70。自查：亮度质心 + 梯度带宽 + 直方图。（对照 C-01：与 Lane B 禁令同侧；依据：[R7] 平光壁画观察）
8. **时间压缩规则**：可识别时代元素 **≥3 个时期**（服装/器物/建筑式样）；同屏历史层 **≥2**（防单一时代叙事）。自查：时代元素分类计数（对照 §12 符号表）。（依据：[R12] 三墙结构；§1-2）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–4 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **群像密度（Figure Density）**`[归纳]` | ≤5 人（单幅/肖像档；**越界：卡罗/戈雅档**） | 5–30 人（一面墙的段落） | ≥30 人/整墙，类型化群众成阵（工程全景档） | **75%** |
| P2 | **时间跨度（Historical Scope）**`[归纳]` | 单一时刻（事件画档） | 一个时期（如殖民期段落） | 跨世纪全景：≥3 个时期同组画（前哥伦布→殖民→革命→未来） | **65%** |
| P3 | **建筑一体度（Site Integration）**`[归纳]` | 独立画面（可搬运；**越界：架上档**） | 适配墙面（尺寸/比例服从） | 墙面/拱/楼梯井一体：构图轴=建筑轴，离墙即失义（国家宫楼梯井档） | **70%** |
| P4 | **工业/物质精确度（Material Precision）**`[归纳]` | 象征化概括（看不清工艺） | 可辨工艺/工具 | 工程图级：零件/流程可追踪（底特律档） | **60%** |
| P5 | **色彩档（Color Register）**`[归纳]` | 单色/素描档（sinopia 阶段） | 土色为主+局部亮色 | 民间高饱和成块分区（墨西哥红/钴蓝/玉米黄） | **55%** |
| P6 | **公共尺度与观看（Scale & Audience）**`[归纳]` | 架上/近观（**越界：戈雅/卡罗档**） | 房间尺度（单面墙） | 建筑尺度：米级高、多面周期、人流运动观看 | **80%** |

> **用法**：P1/P6 定「是不是里维拉」（群像+公共尺度，两条中 ≥1 条 ≥ 中档、且不得同时落弱档）；P2/P3 定「叙事与建筑档」（单面 → 周期 → 楼梯井级一体）；P4 是「工程精确」参数（底特律/工业题材拉高，象征题材可降）；P5 是色彩参数（可关到 sinopia 单色档）。**越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若出现**教堂/神学叙事 + 英雄化裸体漩涡** → 越界米开朗基罗；② 若转为**单幅架上事件 + 近距私人凝视** → 越界戈雅；③ 若出现**小画幅 + 正面单人 + 私密符号身体** → 越界卡罗；④ 若出现**风景崇高 + 背向凝视/天气事件** → 越界弗里德里希/透纳；⑤ 若出现**人造光 + 都市孤独几何** → 越界霍珀。本表档位阈值为 `[归纳]`（本项目操作化建议，未经渲染实验校准）。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 米开朗基罗）**（× 米开朗基罗；本卡 §3.1 分工条款）：纪念性：宗教 vs 现代政治——判据四条（≥3 同档）＋边界注（Chapingo／疫苗面板）
- **分工（vs 戈雅）**（× 戈雅；本卡 §3.1 分工条款）：历史画 vs 壁画工程：可移动架上 vs 不可移动墙面——判据四条（≥3 同档）
- **分工（vs 卡罗）**（× 卡罗；本卡 §3.1 镜像条款（与 kahlo.md §3.1 互查一致））：公共巨幅 vs 私密小幅——四判据（≥3 同档）；默认不并置，组合须显式分区
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01 硬阴影（壁画平光／漫射侧，显式声明）／C-02·C-18（与米氏组合按 70/30 选主）／C-12 色相预算（土色底＋民间亮色成块）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/rivera.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
