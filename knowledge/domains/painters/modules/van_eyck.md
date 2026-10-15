# 凡·艾克 模块卡 — `van_eyck`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/van_eyck.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **物证级微细节**：1:1 放大后前景任意 300×300px 区域仍可读出 ≥10 个独立小物/高光事件；同一物件投影与倒影并存（每粒念珠独立高光点）
2. **镜面反射与「镜中空间」**：≥1 个反射面（凸镜/金属/水面）内含可读第二空间（房间结构＋≥1 人影），与主空间几何自洽
3. **材质百科**：单帧可辨材质 ≥6 类、各有专属光学行为（宽漫反射/逐线可辨/无高光/锐点/透射+反射/镜面）；织物纹理在 1:1 裁片中可数线
4. **单一定向光＋完整物理链**：光自左上方/左侧窗；投影方向平行（±10°）、投影/反射/透射同链——光源在画面之外（连画框线脚投影也按此算）
5. **透明罩染宝石色＋题刻署名系统＋空间嵌套**：多层薄罩染、表面平滑几乎不见笔触；ALS ICH CAN 格言与拟物铭文 ≥1 处；室内→窗→街景多层可读空间

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Van Eyck-style oil panel — evidence-grade micro-realism in oil on oak:
one room under a single directional daylight from a window on the left; short, consistent shadows;
every material rendered at forensic fidelity — silk velvet, brocade threads countable,
sable fur with broken edges and no sheen, brass chandelier catching sharp point highlights,
polished wood reflecting the oranges on the sill, amber prayer beads casting BOTH a shadow and a
reflection on the plaster wall; a convex mirror on the back wall holding a readable second space:
the room, the couple seen from behind, the door, two tiny figures entering;
faces modelled wet-in-wet over thin translucent glazes — jewel-deep colour, no visible brushwork,
stubble built from tiny dabs (darker first, lighter after, a touch of blue at the chin);
objects carry a double reading (real thing first, symbol second): one lit candle, a lap dog,
oranges, discarded clogs, the mirror itself; an inscription painted as if chiselled into stone or
cast in bronze on the frame — a motto, a name, a date ("ALS ICH CAN", "fuit hic");
palette: crimson, emerald, ultramarine, gold, lead white, warm grey; matte-versus-gloss contrast
per material; still, silent, courtly; faithful observation, proportions quietly adjusted, no idealisation
[drawing variant] silverpoint and brush on a chalk ground: fine hatching, detail density receding with
distance, tower architecture minutely described, sky barely sketched
```
**负向约束（`--no` 风格）**
```
--no impasto or visible brushwork, no palette-knife texture, no sfumato haze swallowing detail,
no single-point hard cast shadows, no multiple light sources, no near-black tenebrist background,
no flat poster colours, no neon saturation, no impressionist dabs covering the canvas,
no smiling camera-ready faces, no anachronistic objects, no lens flare or bokeh,
no cartoon, anime, 3D render, photographic HDR
```

## 代码艺术规则（§8.2 原样）

1. **微细节密度规则**：长边 1800px 帧中，随机 3 个 300×300px 前景裁片，每片可辨识独立小物/高光事件 **≥8**；织物区一条 100px 横切线上可数纹理线 **≥6**。自查：裁片目检 + 边缘密度图 + 线频率谱。（依据：[R1] "astonishing level of detail"；[R16] 织线可辨）
2. **镜面内容规则**：**≥1** 个反射面（凸镜/金属/水面），其内部区域（面积 ≥0.5% 帧）含可读结构——**≥2** 条直线元素（房间线脚/窗框）+ **≥1** 个小人影（高度 ≤5% 帧高）。自查：反射区域分割 + 直线检测（Hough）+ 小尺度人形检测。（依据：[R6] 镜中两人影；[R16] 盔甲中的圣母与画家）
3. **点状高光规则**：金属/玻璃/宝石上的高光为离散点（单点面积 ≤0.05% 帧面积，数量 ≥15），且每个高光点位于**入射角一致**的几何位置（同一光源方向）——与维米尔 pointillés 的区分：凡的高光**服务镜面几何**、维的服务材质暗示（按 N7 分类口径统计）。自查：高光连通域 + 光源方向拟合。（依据：[R1] 念珠逐粒高光）
4. **光链一致规则**：全帧主投影方向夹角 **≤10°**；**≥1** 物件同时呈现投影与镜像反射；无第二主光源（窗外的烛光等亮度 ≤ 主窗光斑峰值 30%——烛是符号不是光源）。自查：投影方向直方图 + 影/反光共存计数。（依据：[R5] 画面外光源；[R1] 念珠影+反光）
5. **材质高光形态规则**：**≥5** 类材质各有专属高光形态——织物=宽漫反射（高光区面积 ≥2%、边缘软）、金属=锐点（σ ≤2px）、毛皮=无高光（V>0.9 区域 ≤0.1%）、玻璃=透射+反射双区、木/石=哑光+纹理。自查：材质分类 + 高光形态统计。（依据：[R1][R16]）
6. **铭文拟物规则**：**≥1** 处铭文（署名/日期/格言）以拟物方式呈现——文字区与支撑材质视觉融合（刻石/铸铜/织物），字体 ∈ {哥特体, 罗马大写, 希腊字母转写}；文字基线贴合支撑面透视。自查：文字检测 + 文字区与材质边界融合检查。（依据：[R2] 刻石感签名；[R15] 双层铜框铭文）
7. **深度嵌套规则**：**≥2** 层可读空间（室内→窗→远景；或主空间→镜中空间）；每层独立信息（远景层含 ≥1 建筑轮廓 + 天空带）；层间以物理开口连接（窗/镜/门）。自查：层次分割 + 每层信息量下限。（依据：[R1] 窗外樱桃树；[R6] 镜中空间）
8. **静止与在场规则**：全画面无运动模糊（模糊核 ≤1px）；直视画外者 **≤1**；手势可命名率 ≥1（宣誓/呈递/持物/致敬）；无戏剧性动作姿态。自查：光流=0（视频帧）+ 视线检测 + 姿态分类。（依据：[R4] 手部意义；[R1] 举手问候）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；2–4 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **微细节密度**（Micro-detail Density）`[归纳]` | 主要形体清晰、材质概括（工坊/远景档） | 织物与金属纹理可辨、高光成组（肖像档） | 逐粒高光、逐线织纹、1:1 放大仍有信息（阿尔诺菲尼/凡德帕勒档） | **70%** |
| P2 | **反射与镜面**（Reflection & Mirror）`[归纳]` | 哑光无镜面（纸本/素描档） | 金属与玻璃的离散点状高光（肖像档） | **含内容**的镜面反射（凸镜/盔甲/水面）+ 材质互反（阿尔诺菲尼/凡德帕勒档） | **60%** |
| P3 | **材质多样性**（Material Inventory）`[归纳]` | ≤3 类材质 | 5–7 类（织物/毛皮/金属/木/石） | 10+ 类（+玻璃/水/地毯/珐琅），每类专属高光形态 | **65%** |
| P4 | **光链完整度**（Light-Chain Coherence）`[归纳]` | 平光/漫射（底稿档） | 定向光 + 一致投影 | 定向光 + 投影 + 反射 + 透射 + 画面外光源证据（框影）（根特档） | **70%** |
| P5 | **题刻与框架**（Inscription & Frame）`[归纳]` | 无铭文 | 署名 + 日期（拟物：刻石/铸铜感） | 多语种铭文系统 + 框画成石/铜/织 + 铭文与图像互注（根特/德累斯顿档） | **中（署名+日期）** |
| P6 | **体制与画幅**（工作流参数）`[归纳]` | 单幅肖像/半身（20–35cm 级） | 私人小三联/双联（便携祭坛，30–35cm 级） | 公共多联祭坛（≥12 面板、开闭双面体制，3.75×5.2m 级） | **1**（单幅起步） |

> **用法**：P1/P4 定"是不是凡·艾克"（微细节 + 光链；两条同时 ≥ 中档才成立）；P2/P3 定"物证强度"（肖像档→物证档的滑轨）；P5 定铭文档；P6 是组稿参数（单幅 vs 多联，不进画面重叠计算，按 `expansion.md` §4.3 规则 5 归「工作流参数」栏）。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 细节转为**选择性省略**、表面压平、高光只作点状暗示 → 越界**维米尔**；② "灰"改由排线承担、实心填充为主 → 越界**丢勒**；③ 出现画外单光源 + 近黑背景 + 亮部只落脸/手 → 越界**卡拉瓦乔**；④ 无轮廓线烟状过渡、细节溶解进雾 → 越界**达·芬奇**。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 维米尔）**（× 维米尔；本卡 §3.1 分工条款）：技术型写实两档写死：物证档（累积细节＋有内容的镜面）vs 光学档（选择式省略＋无内容高光点）——判据四条，70/30 选主导
- **分工（vs 丢勒）**（× 丢勒；本卡 §3.1 分工条款）：细节两条介质路线：油彩面（透明罩染/镜面反射）vs 版画线（排线密度）——「灰」从哪来两式
- **分工（vs 达·芬奇）**（× 达·芬奇；本卡 §3.1 分工条款）：细节的两种用途：物证呈现（硬边高光、逐件可考）vs 氛围统一（烟状过渡溶解细节）——边缘轴冲突
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-01 硬阴影 / C-05 笔触 / C-11 高光计数 / C-12 色相预算

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/van_eyck.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
