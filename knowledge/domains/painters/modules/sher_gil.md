# 阿姆里塔·谢尔吉尔 模块卡 — `sher_gil`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/sher_gil.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 10 条）

1. **饱和暖色域**：红/赭/土黄/黄绿＋白、深褐肤色为底；主色相 ≤6 族、高饱和（S≥0.5）面积 ≥35%——「saturated with intense reds, ochres, browns, yellows and greens」
2. **形体简化＋平面化**：单形体内部明度变化 ≤15%、渐变带 ≤10%、轮廓清晰；晚期更甚（「simplified forms, audaciously framed」）——高更式平面化处理的印度转译
3. **大眼·静默的脸＋纪念碑人物**：面部对比集中在眼部（眼睛＝面部最暗细节块）、视线低垂/内向；主要人物高 ≥45% 画幅——「large, sad eyes」「pensive faces」
4. **群像并置＋日常室内**：女性/儿童并排或围坐（2–5 人、互锁视线 ≤1 对）；床/椅/门廊/院墙入画——印度现代绘画中「首次出现的亲密家庭场景」
5. **色调的「音乐性」＋忧郁底色**：同族色 3+ 明度/饱和度层次（「sonorous modulations of color」）；整体明度中低、姿态松垂（languorous poses）——与「幸福的小构图」构成双面

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**
```
Amrita Sher-Gil-style Indian modernist composition — post-impressionist colour translated into Indian subjects, painted with an insider's gaze (the artist belongs to the land she paints):
saturated warm palette — intense reds, ochres, browns, yellows and greens; deep brown skin tones set against brick red, mustard and emerald; cool greens and blues reserved for shadows, foliage and drapery only;
simplified monumental figures, flattened like Gauguin yet observed from within — village women, children and the poor, dignified and unsentimental, large sad eyes, pensive lowered gazes, silent faces;
groups of two to five women and children seated or standing close together in shallow stage-like space — a verandah, a courtyard wall, a whitewashed interior; no deep perspective, no vanishing point;
intimate domestic scenes — charpoys, grinding stones, brass pots, a bride being dressed, women resting between chores;
architecture and animals woven into the scene — white domes, arches, elephants and camels at the edge of the village;
matte controlled surface — vigorous but organised brushwork, colour areas carrying the image, shadows simplified into soft dark masses, no dramatic chiaroscuro;
mood: quiet melancholy and languor — "infinite submission and patience", silent dignity; colour read as sonorous modulation, never mere decoration;
palette: vermilion, brick red, cadmium yellow, ochre, emerald green, viridian, deep brown, off-white; sky often a flat band of pale colour;
setting: Shimla hills, Saraya village, South Indian temple towns — white-clad figures, red earth, mango groves
```
**负向约束（`--no` 风格）**
```
--no orientalist exoticism, colonial gaze, Tahitian/Polynesian imagery, symbolic idols or spirits, cloisonnist heavy black outlines as an end in themselves, art-nouveau ornament, gold leaf, pointillist dots, optical colour mixing, impasto-only expressionism, whole-canvas complementary vibration, dramatic tenebrism, single hard light source, deep single-point perspective, aerial perspective, sfumato, pastel sweetness, doll faces, glamour retouching, photographic realism, text, watermark, 3D render, anime
```

## 代码艺术规则（§8.2 原样）

1. **暖色域规则**：暖色（红/橙/黄/赭系）面积 ≥55%；高饱和（S≥0.5）面积 35–70%；冷色面积 ≤25% 且集中于阴影/植被/布景；主色相 ≤6 族。自查：色相分割 + 面积统计。
2. **平面化规则**：主要形体（各 ≥5% 画布）内部明度标准差 ≤12（0–255 尺度）；连续渐变带（>2% 短边）面积 ≤10%；形体轮廓可见（边界梯度带 ≤1.5% 短边）。自查：分区统计 + 梯度剖面。
3. **面部规则**：面部对比集中于眼部（眼部区对比度 ≥ 面部其余区均值的 1.5 倍）；嘴部对比 ≤ 面部均值；视线低垂/内向 ≥50%（相关作品）。自查：面部区域分割 + 对比度测量。（依据：[R2]「large, sad eyes」）
4. **前景纪念碑规则**：主人物高 ≥45% 画幅（1935–37 档）；人物组重心位于画面下部 2/3；人物与背景明度差 ≥15%。自查：人物掩膜 + 高度测量。
5. **浅空间规则**：透视收敛线 ≤1 组且不强调；纵深层次 ≤2；天空/背景为平色带或墙面（无渐变云）。自查：直线透视检测 + 分区。（依据：[R2]「浅舞台/室内盒式」）
6. **群像规则**：人物数 2–5；互锁视线 ≤1 对；人物间距 ≤0.3 画幅宽（紧凑组）。自查：人物检测 + 视线方向估计。
7. **情绪静默规则**：整体明度中低（均值 0.35–0.55）；表情强度低（眉眼口形变幅度 ≤15% 中性面）；姿态松垂（头/肩倾角 ≥10°）。自查：明度直方图 + 姿态估计。（依据：[R2]「languorous poses」）
8. **图像志分离规则（与高更域的分界判据）**：民族日常元素（服饰/器物/建筑/动物）≥3 类；**象征性神像/幽灵元素 0 命中**；无装饰纹样满铺（图案区 ≤10% 面积）。自查：元素分类计数 + 图案密度。（依据：[R3][R7]）

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1–8 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **色彩饱和度/暖色域强度**`[归纳]` | 低饱和、欧式灰调（巴黎学院习作档） | 局部强化暖色、冷色在场（早期肖像档） | 全画面饱和暖色域（红/赭/黄绿），冷色退居（印度期档） | **75%** |
| P2 | **形体简化/平面化度**`[归纳]` | 完整明暗塑形、表面堆叠（巴黎写实档） | 简化 + 局部塑形（1935 过渡档） | 本质轮廓 + 平色块、细节集中面部（1937–40 档） | **70%** |
| P3 | **人物前景纪念碑度**`[归纳]` | 人物小而远、风景主导（Hill Scene 过渡档） | 中等人物、半身近景 | 前景大人物占下部 2/3、近距（1937 三部曲档） | **70%** |
| P4 | **情绪静默度（忧郁/克制）**`[归纳]` | 中性表情、轻快构图 | 沉思、低垂视线 | 静默忧郁 + 松垂姿态（母题定式） | **65%** |
| P5 | **民族日常图像志密度**`[归纳]` | 无地方元素（巴黎档） | 1–2 件（一件纱丽/一只水罐） | 服饰+器物+建筑+动物 ≥4 类同框（晚期档） | **60%** |
| P6 | **空间压缩/浅舞台度**`[归纳]` | 深透视、风景纵深 | 浅景 2 层 | 盒式/舞台式浅空间、背景=墙/门廊（室内档） | **65%** |

> **用法**：P1/P2/P3 定「是不是谢尔吉尔」（三条中 ≥2 条 ≥ 中档才成立）；P4/P5 定情绪与题材档（巴黎→印度→晚期）；P6 定空间档。
> **越界警报（与 §3.1 对齐，组合实验按此判分）**：① 若出现**象征符号 + 色带层叠 + 静穆神秘**（神像/幽灵/装饰神性）→ 越界进入**高更**域；② 若出现**私人生命事件符号 + 正面镜像 + 还愿画小画幅** → 越界进入**卡罗**域；③ 若出现**硬光开关**（画内无光源、亮部只落脸/手）→ 越界进入**卡拉瓦乔**域；④ 若平面化沦为**无描边纯色装饰配比**（无情绪色域）→ 越界进入**马蒂斯**域；⑤ 若出现**物理不可能的场景变形**（声波天/融化空间）→ 越界进入**蒙克**域；⑥ 若人物转为**标准化神像 + 达显正面** → 越界进入**拉维·瓦尔马**域。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 高更）**（× 高更；本卡 §3.1 分工条款（写死））：「异域」凝视的反转：外部建构（符号化/神话化/记忆拼合）vs 本地平视（同胞/共情/社会现实）——四判据（凝视位置／母题来源／色彩功能／空间）；平面语法可借、凝视对象与情绪不可混
- **分工（vs 卡罗）**（× 卡罗；本卡 §3.1 分工条款（写死））：民族 vs 自传：他者/群体/社会现场 vs 自我/家族/生命事件编码——四判据（题材主语／符号可解码性／身体功能／观看关系）；二选一或显式分区
- **分工（vs 拉维·瓦尔马）**（× 拉维·瓦尔马；本卡 §3.1 分工条款（对齐复读））：生产形式（独幅 vs 复制）／图像志（个体观察 vs 标准化神祇）／观看关系（私密/反身 vs 达显礼拜）——判据三条；与 `ravi_varma.md` §3.8 预写条款复读对齐
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-05 笔触可见度／C-12 色相面积预算／C-16 平涂系反约束适用域（色域情绪成立、不误伤）；组合纪律：表面语法可借、凝视与符号不可混（vs 高更）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/sher_gil.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
