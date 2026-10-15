# 歌川广重 模块卡 — `hiroshige`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/hiroshige.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **裁剪式取景（把「镜头」推近）**：近景物被画幅裁切、贴到镜头前（与画框相交 ≥1、边缘带被前景占据 ≥15%）；远景被前景框住
2. **天气即主角**：雨/雪/雾/月是每张的「情绪装置」（天气符号面积 ≥15%；同系列 ≥2 张以天气命名）
3. **渐印大气（bokashi）**：天空/水面/雾为连续梯度（长边 ≥30% 画幅、无 ≥3% 明度跳变）；蓝体系与渐印绑定（蓝 25–40%、纯平涂大块蓝 ≤1 块）
4. **竖幅切景＋旅人剪影**：地平线在上/下 1/3、近/中/远 ≥3 层；人物 ≤10% 画高、≤8 条线/人、几笔成组沿路排列、不画脸
5. **线骨架＋名所题名框系列语法**：等宽轮廓线＋平涂/渐印、无排线（雨线族等长等距 15°–45°、不承担明暗）；题名框跨张一致（方差 ≤5%）＋落款固定；季节/月令编码；套印微错位/空摺/云母摺

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Hiroshige-style ukiyo-e woodblock landscape print — one sheet of a lyrical travel series:
flat colour areas printed inside a uniform-width black keyline, no hatching, no modelling;
weather is the subject — fine parallel diagonal rain lines, snow kept as unprinted white paper,
horizontal mist bands, a single pale moon low over water;
smooth bokashi gradients in sky and water (indigo to pale cream), no banding;
a cropped foreground element cut by the picture edge — bridge pile, lantern, pine bough,
window frame — with the middle ground and one distant landmark (castle keep, temple pagoda,
Mount Fuji) framed beyond it; vertical composition with near, middle and far planes stacked,
horizon set off-centre; a few anonymous travellers, tiny and unmodelled — walking, punting,
crossing a bridge, pausing at a teahouse; muted mineral palette — indigo and Prussian blue,
ochre, grey-green, soft vermilion seals; title cartouche in a corner, signature at the margin;
paper grain and slightly misregistered colour plates
```
**负向约束（`--no` 风格）**
```
--no hatching or crosshatching for shading, no photographic realism, no 3D render,
no single-point linear perspective with vanishing lines, no dramatic cast shadows,
no single candle or spotlight source, no chiaroscuro, no impasto, no neon glow,
no western oil-painting brushwork, no spiral wave families, no thunderstorm spectacle,
no speed lines, no explosive motion, no crowds of detailed faces, no portrait close-ups,
no layered manuscript architecture, no calligraphic text panels inside the image,
no gold leaf, no HDR gloss, no watermark, no lettering overlays
```

## 代码艺术规则（§8.2 原样）

1. **系列一致性规则**：同系列帧间题名框位置方差 ≤5% 画幅、落款位置固定、画幅比例一致——跨帧可检出「同套」语法。自查：框检测 + 位置统计。（依据：[R7] 题名框/改印记述）
2. **天气线族规则**：降雨帧存在方向方差 ≤10°、长度方差 ≤20% 的斜线群（与画面成 15°–45°），线等宽（变化 ≤30%）、无交叉、无排线塑形；雪帧白色区（V ≥0.9）**无颜料边缘**（留纸白）。自查：直线检测 + 方向直方图 + 明度掩膜。（依据：作品《庄野》《大はし》；留纸工艺 [R2]）
3. **渐印规则（bokashi）**：每帧 ≥1 条连续梯度带（长边 ≥30% 画幅），带内相邻像素明度差 ≤2/255（无 ≥3% 跳变）、梯度方向单调；优先位于天空/水面。自查：梯度带检测 + 单调性检查。（依据：[R2][R7]）
4. **裁剪框景规则**：≥1 个前景元素与画框相交（边缘带 10% 宽度内被前景占据 ≥15%），该元素细部纹理 ≤10 边缘点/千像素；远景符号（塔/山/桥）位于画面中轴 ±25%。自查：边缘占用 + 纹理密度 + 位置度量。（依据：[R6]「too close to the lens」）
5. **旅人规则**：人物实例高 ≤10% 画高、细节线 ≤8 条、组内同向（朝向方差 ≤30°）、无面部特写（人脸关键点命中 ≤1 组）。自查：实例分割 + 骨架线计数 + 朝向统计。（依据：[R3]「integrating local inhabitants」；对照 §3.1 判据③）
6. **色相预算规则**：蓝系（H 190–250°）面积 25–40%，其中 ≥60% 位于渐印带内；饱和 ≥0.85 的纯色块总面积 ≤5%（红/黄只作印章级点缀）；主色 ≤8。自查：HSV 掩膜 + 色块统计。（对照 C-12：与北斋蓝轴二选一；依据 [R1] ヒロシゲブルー条）
7. **竖幅叠层规则**（竖幅帧）：近/中/远三层可分层（沿纵向边缘密度递减 ≥2 级或尺度比 ≥3×）；地平线/海平线位于上/下 1/3 带（不在中线 ±5%）。自查：分层 + 线检测。（依据：[R1]「近景・中景・遠景を重ねた構図」）
8. **静场规则（运动预算）**：帧间光流 Δ ≤2%/帧；无运动模糊核、无镜头特效；允许雨线族整体做 ≤10%/秒 的视差位移——「天气在动、画面不动」。自查：光流场 + 模糊核检测。（与 C-09 对齐：广重站「静」侧；依据：版画为静态媒介 + §3.1 判据④）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–2/4–5/7 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **系列叙事强度（骨架与序列）**`[归纳]` | 单张独立名所（无系列语法） | 中小套（10–30 张，主题组） | 大序列（55–120 张，宿场/月令/方位推进，成套发行） | **70%** |
| P2 | **天气/时刻强度**`[归纳]` | 晴天白昼（天气缺席） | 晨昏/雨雪/月雾之一为主角 | 极端天气主导（白雨/夜雪/夕立/暴雪，天气入题名） | **60%** |
| P3 | **渐印大气梯度强度（bokashi）**`[归纳]` | 平涂为主，渐变带 <10% 画幅 | 单段主梯度带（天空或水面，长边 ≥30%） | 多段大面积渐印（天空＋水面＋雾，≥2 条梯度带） | **65%** |
| P4 | **裁剪框景强度**`[归纳]` | 全景平视，近景无遮挡 | 近景元素入边缘一角（≥1 处与画框相交） | 极端裁剪：近景占 ≥1/3 画幅、被画框切断、远景被框住 | **60%** |
| P5 | **旅人密度**`[归纳]` | 0–2 人（纯景档） | 3–8 人（行列/渡口/茶屋） | ≥10 人成组（祭礼/桥梁人流，沿路径分布） | **50%** |
| P6 | **蓝（Hiroshige blue）与色调**`[归纳]` | 素雅棕绿（蓝 <15%） | 蓝为主调之一（25–40%，与渐印绑定） | 蓝主导＋多段渐印（≥40%；组合时按 C-12 声明主色归属） | **55%** |

> **用法**：P1/P2/P4 定「是不是广重」（三条中 ≥2 条 ≥ 中档才成立）；P3/P6 定大气与色档（平涂 → 单段渐印 → 多段渐印；「Hiroshige blue」出现在中-强档）；P5 是人物层参数（可关，纯景档见《蒲原》《洗馬》）。**越界警报（与 §3.1 对齐，组合实验按此判分）**：① 出现**曲线族/尺度戏法/动势事件**（浪、风暴、速度）→ 越界北斋；② 转为**一次性天气事件＋边缘溶解**（风暴现场、无系列性）→ 越界透纳；③ 出现**多层建筑剖面/微书图案/图内书法与诗**→ 越界贝赫扎德；④ **排线塑形/实心黑**→ 越界丢勒；⑤ **画内单点光源＋暗部塌陷**→ 越界卡拉瓦乔/伦勃朗（广重为平面天光＋渐印）。**蓝轴特别条款**：P6 强档（≥40%）与北斋 C-12 主张（蓝 ≥40%）互斥——组合时二选一（N3），广重侧降档或只取「渐印机制」。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 北斋）**（× 北斋；本卡 §3.1 分工条款）：系列叙事两档写死：抒情旅途（地理-季节序列＋天气变量＋匿名旅人）vs 动势奇景（母题连作＋曲线族＋尺度戏法）——判定须 ≥2 轴联合成立
- **C-12**（× 北斋；本卡 §3.1 分工条款）：蓝轴：只允许一方主张「主色 ≥40%」——北斋为主时广重降点缀级或只取渐印机制；广重为主（默认 25–40%）时北斋降点缀级
- **分工（vs 贝赫扎德）**（× 贝赫扎德；本卡 §3.1 分工条款）：版画序列（跨张、可拆售、图外注记）vs 手抄本单页（页内、装订一体、图内文本）——叙事单位二选一
- **分工（vs 透纳）**（× 透纳；本卡 §3.1 分工条款）：天气：可重访的系列情绪（旅程档）vs 一次性事件现场（事件档）——C-09 站「静」侧（雨线是图形不是运动场）
- **同侧声明**（× 丢勒 / Lane B 02 卡；本卡 §3.1 分工条款）：平涂/无排线为双方共侧（C-07/C-16 无需改写）；雨线族须显式声明「母题线、不承担明暗」防误判排线

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/hiroshige.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
