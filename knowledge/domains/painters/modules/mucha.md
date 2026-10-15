# 慕夏 模块卡 — `mucha`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/mucha.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **光环/拱形背景＋平面装饰空间**：人物头后拱形/环形装饰 ≥1、环线框住面部；无消失点、无投影，深度只靠色层与纹样叠置
2. **长窄画幅＋近真人尺寸＋静止端庄**：宽高比 ≥1:2.5；主体人物高度 ≥ 画面高 70%、姿态静止——「为海报设计引入尊严与克制」
3. **连续曲线系统（whiplash/arabesque）＋自然纹样编织**：发丝/衣褶/茎叶全为连续 S 形曲线（无硬折角）；花叶母题 ≥3 处沿曲线生长；发丝覆盖 ≥10% 画面
4. **平涂＋淡彩（pastel）**：石版平涂色块、套色 ≤8 档、无写实连续渐变；色相少而整（暖粉/青绿/金褐/灰蓝）
5. **字画一体＋边框系统＋圆/拱几何（Q formula）**：手绘装饰字体与图像同构同框；完整闭合装饰边框 ≥1 圈；坐姿人物嵌入圆形母题/拱形平台

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Mucha-style Art Nouveau poster — a tall narrow format with a near life-size, still standing woman:
an idealised serene profile or three-quarter figure in flowing robes,
her long wavy hair curling in continuous arabesque lines;
an ornate rainbow-arched halo behind her head, focusing the face;
a single family of sinuous curves unifying hair, drapery and plant stems — no straight lines, no hard corners;
flowers and foliage (lilies, irises, vines) woven into the background and the border along the same curves;
flat pastel colour areas — soft rose, sage green, teal, gold-ochre, cream — with no realistic shading;
an elaborate ornamental frame enclosing the composition;
hand-drawn decorative lettering integrated into the layout as a design element
[poster variant] a title band with art-nouveau lettering at the top or bottom;
[panel variant] no text, pure ornament, presented as a decorative panel
```
**负向约束（`--no` 风格）**
```
--no metal leaf, gold foil, foil seams, metallic specular highlights, thick impasto, textured oil surface,
photographic realism, 3D render, harsh chiaroscuro, deep cast shadows, single-point perspective,
neon colours, harsh saturation, digital gradients, airbrushed glow, minimalism, bauhaus geometry,
grid-based pattern fills, blocky shapes, abstract expressionism, graffiti, grunge texture, cut-out collage,
clean sans-serif typography, watermark
```

## 代码艺术规则（§8.2 原样）

1. **曲线族一致性**：全帧主要轮廓的曲率连续（无折角）；发丝/衣褶/花茎的线宽族 ≤3 档；直线段仅允许出现在版面分隔/标题基线上，占比 ≤5%。（依据 §1-4）
2. **光环规则**：主角头部后方存在拱形/环形装饰；环中心与头部包围盒中心距离 ≤ 头宽 50%；环线与面部区域不重叠（聚焦而非遮挡）。
3. **近真人静止度**：主体人物高度 ≥ 画面高 60%（强档 ≥70%）；帧间姿态位移（若有动画）≤ 2% 画面高——「静止」是身份特征。
4. **色彩预算**：饱和色（S ≥ 0.6）面积 ≤ 15%；主色相 ≤ 5 个；无连续渐变（渐变面积 ≤ 5%，纸张/印刷噪点除外）。（依据 8 色印刷口径）
5. **纹样生长规则**：花叶母题 ≥3 处，且每处纹样的主轴方向与其「附着对象」（发/衣/框）的切线夹角 ≤ 30°——纹样沿曲线生长、非贴片。
6. **字画一体（海报档）**：排版文字 ≥1 区；字体为手绘装饰体（笔画曲率与画面曲线同族）；文字区与图像共用边框或纹样边界；无文字档（装饰板）则本规则跳过、检查 P6 边框完整度。
7. **边框完整度**：装饰板/海报档存在闭合边框（或上下装饰带 ≥2 段）；边框纹样与画内纹样同族（同一母题库）。
8. **越界警报（组合用）**：帧内出现金属镜面/箔块 → 越界克里姆特域；出现网格单元填充 → 越界若冲域；出现「无文字、无曲线骨架」的纯平涂图案 → 越界马蒂斯域。自查：材质高光检测 + 网格周期检测 + 文字检测。

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–3/5–7 条与 §1/§4 同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **曲线密度 / 装饰线强度**`[归纳]` | 仅人物轮廓为曲线，背景留白或单色（Gismonda 的「留白档」） | 发丝 + 衣褶 + 局部花饰（曲线纹样覆盖约 20–40%） | 满幅曲线纹样 + 边框 + 光环（覆盖 ≥50%，无空白区） | **60%** |
| P2 | **光环/拱环强度**`[归纳]` | 无环（纯装饰板/静物档） | 单环拱线框住头部（Gismonda 档） | 多重同心环 + 星/花/文字嵌入，环成为构图主体（Zodiac/Job 档） | **50%** |
| P3 | **文字整合度（字画一体）**`[归纳]` | 无文字（装饰板档） | 标题区 + 装饰字体（标题与图像分区但同框） | 文字嵌入纹样与边框、笔画带曲线装饰、文字成为构图组件（Job/Moët 档） | **60%** |
| P4 | **色数 / 淡彩度**`[归纳]` | 1–2 色（单色/双色平印档） | 5–8 色淡彩（subtle pastel，对比柔和） | 8+ 色富装饰（含金褐色、多色纹样层） | **55%** |
| P5 | **女性主角尺度与静止度**`[归纳]` | 半身/头像（装饰板局部档） | 3/4 身或坐姿（Q formula 圆内坐姿档） | 近真人全身静止站姿（人物 ≥ 画面高 70%，Gismonda 档） | **70%** |
| P6 | **边框/版面完成度**`[归纳]` | 无框（直接满幅） | 简易装饰框/单线框 | 完整装饰框 + 标题栏 + 边角花饰（《时代》哥特窗式档） | **60%** |

> **用法**：P1/P5 定「是不是慕夏」起步（曲线族 + 近真人静止女性，两条同时 ≥ 中档才成立）；P2/P3 定「海报档 ↔ 装饰板档」的滑轨；P4 定色彩档；P6 定版面完成度。
> **越界警报（与 §3.1 对齐）**：出现金属/金箔材质层 → 越界到**克里姆特**域；出现「平涂纯色图案、无文字、无曲线骨架」→ 越界到**马蒂斯** P4 域；出现网格单元填充 → 越界到**若冲**域。组合实验按此判分。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 克里姆特）**（× 克里姆特；本卡 §3.1 分工条款）：装饰家族两档写死：平面/印刷档（线系统＋平涂＋字画一体＋大众复制）vs 材质/工艺档（金箔/金属＋写实对撞）——判据四条，不得同屏混用
- **C-15**（× 克里姆特类金属层口径；本卡 §3.1 组合注记）：慕夏的平涂印刷面按普通色数计数、不享受金属层豁免（N6）
- **分工（vs 马蒂斯）**（× 马蒂斯；本卡 §3.1 分工条款）：同为平面：印刷曲线＋字画一体＋海报职能 vs 剪纸平涂（图案＝面、无文字、无曲线骨架）——判据 ≥2 项
- **分工（vs 伊藤若冲）**（× 伊藤若冲；本卡 §3.1 分工条款）：东西两档：机械复制（石版）＋曲线＋版面 vs 手绘浓彩＋网格重复——不得互相复制（慕夏禁升目网格/裏彩）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/mucha.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
