# 徐悲鸿 模块卡 — `xu_beihong`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/xu_beihong.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 12 条）

1. **解剖学精确的奔马**（学院素描底子：炭笔排线＋擦笔、石膏-人体-肖像三级）：马体关键结构点（肩胛/肘/腕/球节）位置可考、腿骨比例接近真马；腾空后腿＋交叉前腿、≥1 条腿短缩透视——「熟悉马之骨架、肌肉、组织」后的「动态与神情」
2. **墨块-线合成**：躯干以墨块（浓淡晕染）分体积、鬃/尾/轮廓以扫笔线出速度；线不勾轮廓而表运动、边界不勾死——「以线条和墨块简练地挥写出运动中的马群」
3. **留白即空间＋明暗交界线**：单马档背景交代 ≤10%、留白 ≥50%（款印补位平衡）；面部/人体由一条可追踪的明暗交界线组织体积与节奏——「黑白分明」（新七法）
4. **主题性群像＋动物托兴**：历史/现实题材成组呼应（≥5 人时视线/动作构成画面内回路）；马/狮/鹰承载民族人格寓意、题款与形象互文（「哀鸣思战斗」）——油画端＝古典写实＋中国题材（「民族化」）
5. **设色克制＋碑派款印**：墨为主、淡彩为辅（墨色区 ≥60%、彩域 ≤30%、朱砂只作点醒）；碑派方折线条入画、长题与印（「东海王孙」）为画面构件

## 图像 prompt（§8.1 原样）

**正向段（可直接粘贴）**

```
Modern Chinese ink painting in the manner of Xu Beihong, realist-fusion: a single galloping
horse in full stride — hind legs extended mid-air, forelegs crossed and tucked in foreshortening,
neck arched, head thrust forward, lean and bony rather than fleshy; the body built with ink
masses — broad wet brush sweeps dividing light and dark to model the chest, haunch and belly —
while the mane and tail fly out as fast sweeping strokes, dry-brush and split-brush streaks
carrying the speed; anatomical structure exact and legible (shoulder, elbow, knee, fetlock,
hoof); a narrow ink range of dense black, mid grey and pale wash, with paper-white kept as the
highest light; vast empty paper behind the horse, no ground line, no background scenery; a
calligraphic inscription and one or two red seals balancing the composition; subtle warm washes
of ochre and pale red allowed; motion frozen in one instant, a mood of resolve and aspiration
```

**负向约束（`--no` 风格）**

```
--no western oil rendering, no photorealistic background, no landscape scenery, no ground or
cast shadow, no heavy impasto, no bright multicolour palette, no decorative patterns, no flat
cel shading, no symmetrical standing pose, no fleshy or pampered horse, no glossy finish, no 3D
render, no anime, no chibi, no watermark, no fake seals, no text other than the calligraphic
inscription, no horse tack and saddle, no rider
```

## 代码艺术规则（§8.2 原样）

| # | 规则 | 可判定阈值（默认） | 自查方法 |
|---|---|---|---|
| 1 | **留白率** | 单马档：纸白（L ≥0.90 且 S ≤0.10）面积 ≥50%；背景元素（非主体、非纸白）≤5% | 逐帧亮度/饱和度分割 + 主体掩膜外统计 |
| 2 | **墨色分层** | 主体区明度直方图 3–5 个峰（浓/重/淡/清）；最暗簇 L ≤0.15、纸白 L ≥0.90；中灰平坦段（0.45–0.60）占比 ≤15% | 逐帧直方图 + 峰检测 |
| 3 | **墨块-线比** | 躯干区「面状像素」（窗口墨覆盖 ≥60%）占主体 40–70%；鬃尾区「线状像素」（覆盖 10–40% 且方向一致）占鬃尾区 ≥60% | 分区覆盖率 + 方向统计 |
| 4 | **鬃尾速度线** | 鬃/尾区方向直方图主方向占比 ≥50%（单峰）；线骨架长度中位数 ≥画面短边 5% | 方向直方图 + 骨架长度统计 |
| 5 | **解剖锚点** | 4 肢 + 头 + 尾可见；前膝/飞节位置可标；腿长/体长比 0.75–1.05（真马近似） | 关键点标注 + 比例测量 |
| 6 | **款印预算** | 题款 + 印章合计面积 ≤8%；高饱和（S ≥0.50）红色连通域 1–3 个且为全帧唯一高饱和簇 | 连通域 + HSV 统计 |
| 7 | **色域** | 全帧平均饱和度 ≤0.30；高饱和（S ≥0.50）面积 ≤5%；色相簇 ≤4 | HSV 直方图 + 色相聚类 |
| 8 | **运动预算（动画附加）** | 奔马动画：身体位移方向抖动 ≤10°；腿相位周期与躯干位移相关系数 ≥0.7；鬃尾摆动幅度 ≥体高 3%、频率 ≥步频 1/2 | 光流/关键点追踪 + 相位分析 |

> 说明：全部阈值为 `[归纳]`（本项目操作化建议，未经渲染实验校准）；与 `templates/style_card.md` 的填写规则对齐。署名合规：输出不得含伪题款/伪印章（见 §8.1 版权护栏）。

## 控制参数（§4 原样）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **解剖-结构强度**（Anatomical Structure）`[归纳]` | 结构隐于笔墨、以势取胜（大写意动物小品档） | 结构可读（写意马、花鸟档） | 解剖精确、关节与肌群可考（奔马/《愚公移山》档） | **80%**（身份参数） |
| P2 | **墨块-线比**（Ink-Mass / Line Ratio）`[归纳]` | 以线为主（白描/速写感） | 线墨相当、块面与线并置 | 墨块主导（大笔扫出躯干、浓淡分体积） | **60%** |
| P3 | **运动强度**（Motion Intensity）`[归纳]` | 静立/回首/饮水（立马、饮马档） | 行走/振鬃/腾跃预备 | 全速奔跃：腾空后腿 + 交叉前腿 + 扫鬃尾（招牌档） | **75%** |
| P4 | **留白率**（Negative Space）`[归纳]` | ≤20%：背景有交代（地面/水面/场景） | 30–50%：主体外大部留白 | ≥60%：仅主体 + 款印，全纸空阔（单马典型档） | **70%** |
| P5 | **写实-写意落差**（Rendering Mix）`[归纳]` | 通体写实（油画/素描档） | 头、颈、蹄写实、躯干写意（国画奔马典型） | 大体写意、仅关键结构点写实（大写意档） | **55%** |
| P6 | **题款叙事度**（Inscription Narrative）`[归纳]` | 穷款（仅名） | 短题（纪年 + 名） | 长题：诗/纪事/寄意（长沙会战题、巴人汲水诗档） | **50%** |

> 用法：**P1 + P2 + P3 定「是不是徐悲鸿的奔马」**（结构 + 墨块-线 + 全速运动——三条中 ≥2 条 ≥ 中档才成立）；P4 是空间档（单马 ≥60% 留白为典型）；P5 切「国画写意档 / 油画素描写实档」；P6 是叙事档（题款越强、家国叙事越显）。
> 数据来源：档位阈值为 `[归纳]`（本项目操作化建议，未经渲染实验校准）；特征观察取自 [R6][R10][R13]。
> **分工注（与 §3.1 对齐）**：P1 强档 + P3 强档 + P4 强档（解剖 × 奔跃 × 大留白）是本模块专属组合；**「银灰统调 + 点线面网络 + 彩点预算」整体属于吴冠中模块**；**「积墨 + 逆光 + 亮口」整体属于李可染模块**；**「方构图 + 民间瓷绘色」整体属于林风眠模块（预写）**；**「银笔/羽毛笔手稿页 + 自然研究」整体属于达芬奇模块**——均不得在本模块同档出现。需要抽象感时不得取消解剖结构与主题叙事（P1 弱 + P6 弱 → 越界警报，应换吴冠中/林风眠档）。本注为 `[归纳]`。

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

- **分工（vs 达·芬奇）**（× 达·芬奇；本卡 §3.1 分工条款（第一写死条款））：素描两体系：观察-记录（银笔/羽毛笔手稿）vs 训练-创作准备（炭笔/擦笔；石膏-人体-肖像三级）——四判据（媒介笔法／素描职能／画面合成／主题域）；分轴、不得混用两套签名机制
- **分工（vs 吴冠中 / 李可染）**（× 吴冠中 / 李可染；本卡 §3.1 分工条款（已收口，含互锁行））：同代四路径：写实融合 vs 形式美（吴）vs 逆光山水（李）——各四判据；同屏须显式分轴（造型轴归徐）；不得混用「奔马墨块扫笔」与「点线面网络／积墨亮口」两组标志机制
- **分工（vs 林风眠）**（× 林风眠（future）；本卡 §3.1 预写条款）：同代四路径之三：写实融合 vs 现代主义融合（方构图＋民间瓷绘色）——四判据（造型／构图／色彩／主义）；`lin_fengmian.md` 未落盘，落盘后复核
- **组合预检（Lane B）**（× Lane B；本卡 §3.1 组合注记）：重点：C-17 负空间（单马档留白 ≥50%）／C-05 笔触可见度（墨块-线 vs「只有渐变」）／C-12 色相预算（墨为主＋朱砂点醒）

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/xu_beihong.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
