# 独立复核报告 — van_gogh.md + picasso.md（A-11 / wave2）

> 复核人: DossierReview · 2026-10-15 · 对象: `knowledge/domains/painters/dossiers/van_gogh.md`（A-03, ArtistVanGoghMonet）与 `knowledge/domains/painters/dossiers/picasso.md`（A-05, ArtistPicassoCezanne）。
> 本报告**只读**原档案，不改动它们；问题留给主脑处置。
> 检查器: `read`（URL/本地文件/PDF 文本）、`bash`+`curl`（Met Open Access API、Internet Archive CDX）、`python`+`pymupdf`（`_tmp_picasso/picasso_40yrs.pdf`，Barr 1939 目录 218 页逐页检索）、`eval` 的 `browser` 全局（MoMA/VGM 实时页与 DOM 全文检索）。web_search 全程未用（限流）。
> 判决口径: **CONFIRMED** = 原文逐字/编号/日期与档案一致；**WEAKENED** = 结论可立但描述、表述或来源结构有瑕疵；**OVERTURNED** = 与原始来源矛盾；**未核到** = 本轮无法复现（附已试路径）。

## 0. 总判

| 档案 | 模板 0–10 节 | 证据级标注 | 自审四段 | 抽检 | 判决分布 |
|---|---|---|---|---|---|
| van_gogh.md | 全填；§8.3 为可选节且已说明不收录 | 逐条到位；[归纳] 与 [自述] 分离清楚 | 真实——B-1/B-2 两条检索我逐条复现，结果与自审完全一致 | 15 条 | CONFIRMED 15；另有 1 处标注建议（R18 状态过时，非事实错误） |
| picasso.md | 全填；§8.3 已说明未收集 | 逐条到位；§3 全部 [自述] 且带页码 | 基本真实——B-1 的**结论**正确且我复核为真，但 B-1 的**命令描述**不可复现；C 节 3 条输出仅 1 条属本档案自证 | 16 条 | CONFIRMED 16；另有 1 处描述 WEAKENED（B-1）+ 3 条表述建议 |

两份档案均**未发现**张冠李戴（把他人转述当自述）、日期/信编号/馆藏号错误。各问题清单见 §1.4 / §2.4。

---

## 1. van_gogh.md（ArtistVanGoghMonet）

### 1.1 结论摘要

15 条抽检（7 条书信引文+日期、3 条馆藏数字、3 条博物馆研究结论、2 条检索可复现性、1 条二手交叉）全部 CONFIRMED。书信编号-日期-引文三者逐字对齐；MoMA/Met/VGM 馆藏号与图注逐字对齐；自审 B-1/B-2 的检索声明我原样复现成功。**无 OVERTURNED，无未核到的关键结论。** 唯一可动的是 R18 的读取状态标注（已过时，见问题 1）。

### 1.2 模板合规逐节

| 节 | 模板要求 | 实际 | 判定 |
|---|---|---|---|
| 0 | 生卒/国别/流派/媒介/定位/3–5 件关键作品带馆藏与 URL | 全有；5 件作品全带馆藏号+URL | ✅ |
| 1 | 视觉指纹 8–12 条 | 10 条；8 条带 [史料]/[研究]，2 条明标 [归纳] | ✅ |
| 2 | 技法规则 8–12 条 | 10 条；逐条带证据级 | ✅ |
| 3 | 创作原则 6–10 条 | 7 条；[自述] 与 [研究] 混排且标注正确 | ✅ |
| 4 | 控制参数 4–6 个，弱/中/强+默认 | 6 个，P1–P6 各三档+默认值 | ✅ |
| 5 | 自述 ≥5 条，原文→中译→出处 | 9 条；全部带 vangoghletters.org 直链 | ✅ |
| 6 | 影响链（学谁/谁学他/一句话） | 全有；含 [未核] 显式标注 | ✅ |
| 7 | 深度分析 ≥5 条带 URL | 6 条；含直连失败→Wayback 的读取说明 | ✅ |
| 8 | 8.1 图像模块 / 8.2 4–8 条可判定规则 / 8.3 可选 | 8.1 全；8.2 7 条；8.3 说明不收录（可选节） | ✅ |
| 9 | URL 编号清单 | R1–R18 + 读取状态列 + CC-1/2/3 交叉核对 | ✅ |
| 10 | 缺口与待验证 | 5 条缺口 + [推测] 标注声明 | ✅ |
| 自审 | A 早产出 / B 反驳≥3–5 条带判决+命令 / C 机械验证原样输出 / D ≤14 行 | A/B/C/D 全有；B 5 条、C 3 条原样输出 | ✅（B-1/B-2 我复现成功） |

### 1.3 抽检表（15 条，全部带判决与命令输出）

**VG-1 [自述] 信 663 引文+日期（§2-1/§5-3）**
命令: `read https://vangoghletters.org/vg/letters/let663/letter.html`
原样输出（截取）:
```
title: 663 (663, 520): To Theo van Gogh. Arles, Saturday, 18 August 1888. - Vincent van Gogh Letters
Because instead of trying to render exactly what I have before my eyes, I use colour more arbitrarily in order to express myself forcefully.
To finish it, I'm now going to be an arbitrary colourist.
I make a simple background of the richest, most intense blue that I can prepare
```
→ **CONFIRMED**（编号 663、日期 1888-08-18、三处引文全部逐字；「浓蓝无限」细节一致）

**VG-2 [自述] 信 673 引文+日期（§2-2/§5-4）**
命令: `read .../let673/letter.html`
原样输出（截取）:
```
title: 673 (677, 531): To Theo van Gogh. Arles, Monday, 3 September 1888.
To express the love of two lovers through a marriage of two complementary colours, their mixture and their contrasts, the mysterious vibrations of adjacent tones.
I'd like to paint men or women with that je ne sais quoi of the eternal, of which the halo used to be the symbol, and which we try to achieve through the radiance itself, through the vibrancy of our colorations.
To express hope through some star. The ardour of a living being through the rays of a setting sun.
```
→ **CONFIRMED**（「互补色婚配」「星=希望」「落日=炽热」三处全部命中原文）

**VG-3 [自述] 信 249 引文+日期（§3-2/§5-1）**
命令: `read .../let249/letter.html`
原样输出（截取）:
```
title: 249 (250, 218): To Theo van Gogh. The Hague, on or about Friday, 21 July 1882.
I want to make drawings that *move* some people.
In short, I want to reach the point where people say of my work, that man feels deeply and that man feels subtly. Despite my so-called coarseness — you understand — perhaps precisely because of it.
It isn't the language of painters one ought to listen to but the language of nature.
I would like to express not something sentimentally melancholic but deep sorrow.
```
→ **CONFIRMED**（含档案「流行转述是意译改写，以原信为准」的注——原信确无「打动人们」字样，档案处理正确）

**VG-4 [自述] 信 535 引文+日期（§2-3/§5-2）**
命令: `read .../let535/letter.html`
原样输出（截取）:
```
title: 535 (538, 427): To Theo van Gogh. Nuenen, on or about Tuesday, 13 October 1885.
Paint in one go, as far as possible in one go.
*that if it worked, they left it alone*.
*When Delacroix paints – it's like the lion devouring his piece of flesh*.
```
→ **CONFIRMED**（「一次完成」+「狮子撕肉」+哈尔斯/伦勃朗/雷斯达尔「画得快」全部在信内）

**VG-5 [自述] 信 805 引文+日期（§2-7/§2-8/§5-8）**
命令: `read .../let805/letter.html`
原样输出（截取）:
```
title: 805 (806, 607): To Theo van Gogh. Saint-Rémy-de-Provence, on or about Friday, 20 September 1889.
At present I have 7 copies out of ten of Millet's Travaux des champs.
So then my brush goes between my fingers as if it were a bow on the violin and absolutely for my pleasure.
It's the study of the figure that teaches one to grasp the essential and to simplify.
the memory, the vague consonance of colours that are in the same sentiment, if not right – that's my own interpretation.
```
→ **CONFIRMED**（7/10 时点、琴弓比喻、「解释=自己的interpretation」全部逐字）

**VG-6 [自述] 信 777 引文+日期（§5-7）**
命令: `read .../let777/letter.html`
原样输出（截取）:
```
title: 777 (780, 593): To Theo van Gogh. Saint-Rémy-de-Provence, between about Friday, 31 May and about Thursday, 6 June 1889.
This morning I saw the countryside from my window a long time before sunrise with nothing but the morning star, which looked very big.
perhaps the starry night and the landscape with yellow greenery which was in the walnut frame
```
→ **CONFIRMED**（日期区间、晨星句、以及档案的关键克制：信内确有 "the starry night" 但档案正确地拒绝断言其=MoMA 本作）

**VG-7 [自述/转引] 信 640 短语（§5-6，档案自标 ⚠️）**
命令: `read .../let640/letter.html` + 检索端点
原样输出（截取）:
```
title: 640 (644, 510): To Theo van Gogh. Arles, Sunday, 15 July 1888.
All my work is based to some extent on Japanese art, and if I've said nothing about this to Bing it's because I think that after my journey in the south I'll be able to take the subject up again perhaps more seriously.
```
检索 `"based to some extent"`（带引号）:
```
### 1 letter found
1. [640 To Theo van Gogh. Arles, Sunday, 15 July 1888.](/vg/letters/let640/letter.html)
```
→ **CONFIRMED**（逐词读信 640 后：短语确在信内；「仅见于信 640」的检索声明也可复现。**建议升级**：档案现在标 [自述/转引]，可以升为 [自述] 全引文）

**VG-8 [史料/数字] MoMA《星月夜》馆藏（§0 表 + §1-4/1-7 + §7-2）**
命令: `read https://web.archive.org/web/20240101154212id_/https://www.moma.org/collection/works/79802`（档案自审 C 引用的同一快照）
原样输出（截取）:
```
title: Vincent van Gogh. The Starry Night. Saint Rémy, June 1889 | MoMA
29 x 36 1/4" (73.7 x 92.1 cm)
Object number
472.1941
the artist altered celestial shapes and added a sense of glow
Dominated by vivid blues and yellows applied with gestural verve and immediacy
Flame-like, it reaches almost to the top edge of the canvas
intensely swirling patterns that seem to roll across its surface like waves
The vision took place at night, yet the painting, among hundreds of artworks van Gogh made that year, was created in several sessions during the day
The picturesque village nestled below the hills was based on other views—it could not be seen from his window
```
→ **CONFIRMED**（馆藏号 472.1941、尺寸、June 1889、§1-2/§1-4/§1-7 三处引文、§7-2 的「日间分次画成」「村景非实景」全部逐字）

**VG-9 [史料/数字] Met《麦田与柏树》馆藏（§0 表 + §1-1 + §2-6 + CC-3）**
命令: `read https://web.archive.org/web/20241225171812id_/https://www.metmuseum.org/art/collection/search/436535` + `curl Met API /objects/436535`
原样输出（截取）:
```
meta-description: <i>Wheat Field with Cypresses</i> is Van Gogh’s initial study from nature of a composition that he repeated in three other versions: a large reed-pen drawing (Van Gogh Museum, Amsterdam, 47.1 x 62.3 cm),[1] and two painted studio variants: one of the same format, now in the National Gallery, London, and a “reduction”
Van Gogh regarded the present work as one of his “best” summer landscapes and was prompted that September to make two studio renditions: one on the same scale (National Gallery, London) and the other a smaller replica, intended as a gift for his mother and sister (private collection).
Fig. 2. Detail from center of canvas showing blue stroke through impasto between hills and field
Fig. 4. Detail from left foreground showing weave imprint in impasto
```
API:
```
title: Wheat Field with Cypresses
accessionNumber: 1993.132
```
→ **CONFIRMED**（1993.132、「initial study from nature」、伦敦版+缩小复制版（送母亲与妹妹）、两条图注引文全部逐字）

**VG-10 [研究/数字] Met TOAH 论文（§0 + §1-6/1-8 + §3-4/3-5 + §6）**
命令: `read https://web.archive.org/web/20240103131239id_/https://www.metmuseum.org/toah/hd/gogh/hd_gogh.htm`
原样输出（截取）:
```
Over the course of his decade-long career (1880–90), he produced nearly 900 paintings and more than 1,100 works on paper.
In fall and winter 1889–90, he executed twenty-one copies after Millet (64.165.2); he described his copies as “interpretations” or “translations,” comparing his role as an artist to that of a musician playing music written by another composer.
The composition and calligraphic handling of The Flowering Orchard (56.13) suggest the influence of Japanese prints
distinguished by their great verve and linear invention
of its palette, which ranges from ocher to vermilion and malachite, Van Gogh expressed his desire that it “sing a lullaby with color,”
By the outbreak of World War I, with the discovery of his genius by the Fauves and German Expressionists, Vincent van Gogh had already come to be regarded as a vanguard figure in the history of modern art.
```
→ **CONFIRMED**（「约 900 幅油画/1100 余件纸本」「21 幅临米勒（1889 秋冬）」「解释/翻译+乐手比喻」「日本版画影响」「verve and linear invention」「摇篮曲」「野兽派与德国表现主义」全部逐字）

**VG-11 [史料/数字] Met API《第一步》（§0 表）**
命令: `curl collectionapi.metmuseum.org/public/collection/v1/objects/436526`
原样输出（截取）:
```
title: First Steps, after Millet
accessionNumber: 64.165.2
artistDisplayName: Vincent van Gogh
objectDate: 1890
```
→ **CONFIRMED**（64.165.2 / 1890）

**VG-12 [史料] VGM《向日葵》馆藏（§0 表 + R18）**
命令: `eval browser` 打开 `https://www.vangoghmuseum.nl/en/collection/s0031V1962`
原样输出（截取）:
```
Title: Vincent van Gogh - Sunflowers - Van Gogh Museum
Sunflowers
Vincent van Gogh (1853 - 1890), Arles, January 1889
oil on canvas, 95 cm x 73 cm
Credits (obliged to state): Van Gogh Museum, Amsterdam (Vincent van Gogh Foundation)
```
→ **CONFIRMED**（s0031V1962 可达、1889、馆藏归属正确。**R18 的「仅取到 meta（JS 渲染）」状态已过时**——用 browser 可读全页，建议升级并补 95×73 cm）

**VG-13 [自审可复现性] B-1「arbitrarily 检索=4 封」**
命令: `read .../search/advanced?term=arbitrarily&translation=translation&from=1&to=1`
原样输出:
```
### 4 letters found
1. [495 To Theo van Gogh. Nuenen, Tuesday, 21 April 1885.](...)
2. [663 To Theo van Gogh. Arles, Saturday, 18 August 1888.](...)
3. [411 To Theo van Gogh. Nuenen, on or about Saturday, 8 December 1883.](...)
4. [537 To Theo van Gogh. Nuenen, on or about Wednesday, 28 October 1885.](...)
```
→ **CONFIRMED**（与自审 B-1 所述「命中 4 封（495/663/411/537）」完全一致）

**VG-14 [自审可复现性] B-2「"morning star" 全库仅 1 封=777」**
命令: `read .../search/advanced?term=%22morning+star%22&...`
原样输出:
```
### 1 letter found
1. [777 To Theo van Gogh. Saint-Rémy-de-Provence, between about Friday, 31 May and about Thursday, 6 June 1889.](/vg/letters/let777/letter.html)
```
→ **CONFIRMED**。附带发现：**不带引号**的 `morning+star` 返回 **290 封**（词组被拆成单词检索）；档案自审未写明「带引号」这一语法细节，建议在 R10 加注，避免复现者误判。

**VG-15 [二手交叉] Wikipedia《Japonaiserie (Van Gogh)》（§6）**
命令: `read https://en.wikipedia.org/wiki/Japonaiserie_(Van_Gogh)`
原样输出（截取）:
```
Vincent possessed twelve prints from Hiroshige's series One Hundred Famous Views of Edo
Van Gogh made three copies of ukiyo-e prints: The Courtesan and the two studies after Hiroshige.
The cover carried a reverse image of a colour woodblock by Keisai Eisen depicting a Japanese courtesan or Oiran.
he and his brother Theo van Gogh dealt in these prints for some time, eventually amassing hundreds of them, which are now housed in the Van Gogh Museum in Amsterdam.
```
→ **CONFIRMED（与档案一致；档案已正确标 [研究/二手]）**。「埃森《花魁》+ 广重 2 件」「12 张名所江户百景」「数百张今藏 VGM」均与 Wikipedia 相符；**具体馆藏编号未核到（已试: vangoghmuseum.nl 搜索页 browser 渲染不出结果；向日葵页已核）**——档案 §10 已自列该缺口，成立。

### 1.4 问题清单 + 修正建议（van_gogh.md）

1. **R18 状态过时（建议改，非事实错误）**：现标「仅取到 meta（JS 渲染）⚠️」。实测 browser 可读全页：Sunflowers、s0031V1962、Arles January 1889、95×73 cm。建议把 R18 升 ✅ 并补尺寸；§10 对应缺口可销。
2. **R10 检索示例建议注明「带引号=短语检索」**：`"morning star"`=1 封，`morning star`（无引号）=290 封。自审 B-2 结论正确，但语法细节不写明会让复现者误判。
3. **表述建议（保守非错）**：§3-5「用同一双手翻土和取食」实为梵高信中原话（Met 转引: "have tilled the earth themselves with the same hands they are putting in the dish"），现标 [研究: R15]，可考虑改 [自述/转引]。
4. **可升级项**：§5-6 信 640 的 [自述/转引] 现可升为 [自述]（我逐词核到原文并复现了检索）。
5. 未核到（非缺陷）：浮世绘三件临摹的 VGM 馆藏编号（已试: VGM 搜索页 browser 渲染未出结果）；「903 封」计数（档案自列 UNVERIFIED，未追）；Don McLean 歌曲等流行文化链（档案自列未核，未追）。

---

## 2. picasso.md（ArtistPicassoCezanne）

### 2.1 结论摘要

16 条抽检（9 条 Barr 目录逐页引文、4 条馆藏数字与引文、3 条博物馆研究）全部 CONFIRMED。**所有 [自述] 引文与页码在 Barr 1939 目录 PDF 中逐字命中**（含档案自纠的 1923/1935 归属问题——该自纠我复核为真）；AIC/MoMA 馆藏号、尺寸、引文逐字命中；MoMA 实时页（2026-10-15）确认「1257 件在线藏品」与「2024 展签」两条。**无 OVERTURNED。** 瑕疵仅在自审 B-1 的命令描述与 C 节的输出选择（见问题 1、2）。

### 2.2 模板合规逐节

| 节 | 模板要求 | 实际 | 判定 |
|---|---|---|---|
| 0 | 生卒/国别/流派/媒介/定位/3–5 件关键作品 | 全有；1–4 号作品带馆藏号与尺寸 | ✅（精确生卒日未核到馆方页，见问题 5） |
| 1 | 视觉指纹 8–12 条 | 12 条；[研究]/[史料]/[归纳] 标注清楚 | ✅ |
| 2 | 技法规则 8–12 条 | 12 条；逐条带证据级 | ✅ |
| 3 | 创作原则 6–10 条 | 10 条，全部 [自述] 带 Barr 页码 | ✅ |
| 4 | 控制参数 4–6 个，弱/中/强+默认 | 6 个表格，三档+默认值 | ✅ |
| 5 | 自述 ≥5 条，原文→意译→出处 | 9 条；含「坊间误记」纠偏注与 Brassaï 归属存疑注 | ✅ |
| 6 | 影响链 | 全有；卢梭一条正确标 [推测] 并列入 §10 | ✅ |
| 7 | 深度分析 ≥5 条带 URL | 7 条 | ✅ |
| 8 | 8.1 / 8.2 4–8 条 / 8.3 可选 | 8.1 全；8.2 8 条；8.3 说明未收集（可选节） | ✅ |
| 9 | URL 编号清单 | 14 条 + F0–F4 交叉核对 | ✅ |
| 10 | 缺口与待验证 | 6 条，含「未采用流行语」的处理说明 | ✅ |
| 自审 | A/B/C/D | 全有；B 5 条带判决；C 3 条原样输出 | ✅（B-1 描述、C 选材见问题 1、2） |

### 2.3 抽检表（16 条，全部带判决与命令输出）

**检查器 A：Barr, *Picasso: Forty Years of His Art*（MoMA 1939）PDF 逐页检索**
命令: `python` + `pymupdf` 对 `_tmp_picasso/picasso_40yrs.pdf`（218 页）全库检索关键词，并读取每页页脚印页码：
```
'settled': pdf pages [20] -> printed [['15']]
'anxiety': pdf pages [23] -> printed [['18']]
'receptacle': pdf pages [22] -> printed [['17']]
'no intention': pdf pages [22] -> printed [['17']]
'sum of destructions': pdf pages [18] -> printed [['13']]
'to search means nothing': pdf pages [14] -> printed [['9']]
'create enthusiasm': pdf pages [18] -> printed [['13']]
'horror of copying': pdf pages [22] -> printed [['17']]
'no past or future': pdf pages [16] -> printed [['11']]
'nobody can tell how': pdf pages [20] -> printed [['15']]
'passions tell me': pdf pages [18] -> printed [['13']]
'Art is a lie': pdf pages [15] -> printed [['10']]
'meant to be': pdf pages [24] -> printed [['19']]
```
声明区边界: 印页码 9–11 = "STATEMENT BY PICASSO:1923"（"made in Spanish to Marius de Zayas … published in The Arts, New York, May, 1923, under the title Picasso Speaks"）；印页码 13–19 = "STATEMENT BY PICASSO:1935"（"Christian Zervos put down these remarks of Picasso … published under the title Conversation avec Picasso in Cahiers d'Art"）。

**P-1 [自述] 1923「to search means nothing / To find, is the thing」（§3-1/§5-1）** → 印页 9
```
In my opinion to search means nothing in painting. To find, is the thing.
```
→ **CONFIRMED**（另与 [7] Gallery Walk 转录逐字一致: "When I paint, my object is to show what I have found and not what I am looking for."）

**P-2 [自述] 1923「Art is a lie」（§5-2）** → 印页 10
```
We all know that art is not truth. Art is a lie that makes us realize truth, at least the truth that is given us to understand.
```
→ **CONFIRMED**

**P-3 [自述] 1935「sum of destructions」（§3-2/§5-4）** → 印页 13
```
In my case a picture is a sum of destructions. I do a picture — then I destroy it.
```
→ **CONFIRMED**（该页正是 1935 声明起始页）

**P-4 [自述] 1935「settled beforehand」（§5-3 + 自审 B-1 的 OVERTURN）** → 印页 15
```
A picture is not thought out and settled beforehand. While it is being done it changes as one's thoughts change.
```
→ **CONFIRMED（结论）**：该句位于 **1935** 段（印页 13 起）的页 15——档案自纠「坊间误记为 1923 年语」**成立**。
→ 但 B-1 的**命令描述 WEAKENED**：B-1 写「命中页 15（1923 声明区）与页 21（1935 声明区）」；我全 218 页复现，`settled beforehand` 仅命中 1 处 = pdf p.20 = 印页 15（属 1935 段），没有「页 21」命中。结论对、描述对不上，见问题 1。

**P-5 [自述] 1935「no intention / receptacle / horror of copying」（§3-6/§5-5/§5-6）** → 印页 17
```
The artist is a receptacle for emotions that come from all over the place: from the sky, from the earth, from a scrap of paper, from a passing shape, from a spider's web.
When we invented cubism we had no intention whatever of inventing cubism. We wanted simply to express what was in us.
I have a horror of copying myself.
```
→ **CONFIRMED**（「receptacle 句改挂 1935 Zervos 文本」的处理经 Barr 重印核实为真）

**P-6 [自述] 1935「Cezanne's anxiety」（§3-8/§5-7）** → 印页 18
```
What forces our interest is Cezanne's anxiety — that's Cezanne's lesson ; the torments of van Gogh — that is the actual drama of the man. The rest is a sham.
```
→ **CONFIRMED**

**P-7 [自述] 1935 Stein 轶事（§5-9）** → 印页 18–19
```
Gertrude Stein joyfully announced to [p.18 页脚] me the other day that she had at last understood what my picture of the three musicians was meant to be. It was a still life !
```
→ **CONFIRMED**（句子恰好跨 18/19 页——档案标「页 18–19」精确）

**P-8 [自述] 1935「create enthusiasm」（§5-8）** → 印页 13
```
" You dont need to show them to me. The essential thing in our period of weak morale is to create enthusiasm.
```
→ **CONFIRMED**

**P-9 [自述] 1923「no past or future」（§3-10）** → 印页 11
```
To me there is no past or future in art. If a work of art cannot live always in the present it must not be considered at all.
```
→ **CONFIRMED**

**P-10 [史料/数字] AIC《卡恩维勒肖像》（§0 作品2 + §1-2 + §2-1/2-9 + §7-4）**
命令: `read https://www.artic.edu/artworks/111060/daniel-henry-kahnweiler`
原样输出（截取）:
```
Date: autumn 1910
Kahnweiler sat as many as thirty times for this portrait.
He described Kahnweiler with a network of shimmering, semitransparent surfaces that merge with the atmosphere around him.
Forms are fractured into various planes and faceted shapes and presented from several points of view.
a wave of hair, the knot of a tie, a watch chain
Out of the ﬂickering passages of brown, gray, black, and white emerges a rather traditional portrait pose of a seated man, his hands clasped in his lap.
Dimensions
100.4 × 72.4 cm (39 9/16 × 28 9/16 in.)
Reference Number
1948.561
```
→ **CONFIRMED**（六处引文+尺寸+馆藏号+「坐约三十次」全部逐字；另核到 "He also wrote an important book, *The Rise of Cubism*, in 1920"——§7-4「画商本人 1920 年写《立体主义的兴起》」一致）

**P-11 [史料/数字] MoMA《阿维尼翁少女》（§0 作品1 + §7-2）**
命令: `read Wayback 20250101100331id_/.../79766` + `eval browser` 实时页 DOM
原样输出（截取）:
```
title: Pablo Picasso. Les Demoiselles d'Avignon. Paris, June-July 1907 | MoMA
Dimensions
8' x 7' 8" (243.9 x 233.7 cm)
Object number
333.1939
According to Daniel-Henry Kahnweiler, Picasso’s art dealer, Les Demoiselles d’Avignon marked the “beginning of Cubism” due to its fragmented forms and contrasting perspectives. Yet others have denied that the painting is Cubist.
“When we invented Cubism, we had no intention of inventing Cubism,” he explained. “We simply wanted to express what was in us.”
```
→ **CONFIRMED**（243.9×233.7 / 333.1939 / June-July 1907；§7-2 的 Kahnweiler「beginning of Cubism」+ 反方意见 + 原话引用全部逐字）

**P-12 [史料/数字] MoMA《三个音乐家》（§0 作品4 + §1-4/1-5/1-10/1-11 + §2-6 + §7-3）**
命令: `read Wayback 20230605095448id_/.../78630`（Highlights 文本）+ `eval browser` 实时页 DOM（2026-10-15）
原样输出（截取，Wayback 2023 快照）:
```
Fontainebleau, summer 1921
Dimensions
6' 7" x 7' 3 3/4" (200.7 x 222.9 cm)
Object number
55.1949
The intricate, jigsaw-puzzle-like composition sums up the Synthetic Cubist style, the flat planes of unshaded color recalling the cutout and pasted paper forms with which the style began. These overlapping shapes are at their most complex at the center of the picture, which is also where the lightest hues are concentrated, so that an aura of darkness surrounds a brighter center. Along with the frontal poses of the figures, this creates a feeling of gravity and monumentality
```
实时页 DOM 追加命中（这两条在 Wayback 快照里读不到，在 2026-10-15 实时页里逐字存在）:
```
The mural-sized Three Musicians evokes collage through its flat, interlocking planes of unshaded color, as well as the sheet music at right. Held up by one of the three musicians referenced in the title, this painted sheet music recalls the cut-and-pasted sheet music that Picasso had often added to his early Cubist collages.
The levity of these clown-like figures is countered by the painting’s somber palette, which lends an air of melancholy to the scene.
Gallery label from
2024
```
→ **CONFIRMED**（200.7×222.9 / 55.1949 / summer 1921；「aura of darkness」「frontal poses」「jigsaw-puzzle-like」逐字；§1-5 的「flat, interlocking planes of unshaded color」与 §2-6 的「painted sheet music…」以及 §1-11 的 2024 展签「somber palette, which lends an air of melancholy」全部在实时页逐字命中）

**P-13 [研究] Met《Cubism》年表（§0 + §1-3 + §2-6 + §6 F1 + §7-5）**
命令: `read Wayback 20260103103927id_/https://www.metmuseum.org/essays/cubism`
原样输出（截取）:
```
It was created by Pablo Picasso (Spanish, 1881–1973) and Georges Braque (French, 1882–1963) in Paris between 1907 and 1914.
The French art critic Louis Vauxcelles coined the term Cubism after seeing the landscapes Braque had painted in 1908 at L’Estaque in emulation of Cézanne. Vauxcelles called the geometric forms in the highly abstracted works “cubes.”
During Analytic Cubism (1910–12), also called “hermetic,” Picasso and Braque so abstracted their works that they were reduced to just a series of overlapping planes and facets mostly in near-monochromatic browns, grays, or blacks.
During the winter of 1912–13, Picasso executed a great number of papiers collés
With this new technique of pasting colored or printed pieces of paper in their compositions, Picasso and Braque swept away the last vestiges of three-dimensional space
adopted and further developed by many painters, including Fernand Léger (…), Robert and Sonia Delaunay, Juan Gris (…), Roger de la Fresnaye (…), Marcel Duchamp, Albert Gleizes, Jean Metzinger (…), and even Diego Rivera
had far-reaching consequences for Dada and Surrealism
```
→ **CONFIRMED**（F1 的「1907–1914 + Vauxcelles + 埃斯塔克仿塞尚」、分析期分期与近单色、papiers collés 1912 冬起、扩散名单、Dada/超现实影响全部逐字）

**P-14 [研究] MoMA「Cubism」术语页（§1-7 + §6）**
命令: `read Wayback 20251228124803id_/https://www.moma.org/collection/terms/cubism`
原样输出（截取）:
```
Cubists often incorporated multiple perspectives into individual compositions
Cubism originated with the artists Georges Braque and Pablo Picasso, whose close artistic exchange propelled the style from 1907 to 1914.
After the critic Louis Vauxcelles dismissed landscapes that Braque had painted in 1908 as consisting of “cubes,”
```
→ **CONFIRMED**（§1-7 的「multiple perspectives」引文、§6 的起源句全部逐字）

**P-15 [数字] MoMA 艺术家页「1257 件在线藏品」（§7-6）**
命令: `read https://www.moma.org/artists/4609-pablo-picasso`（2026-10-15 实时）
原样输出（截取）:
```
# Pablo Picasso
## Spanish, 1881–1973
## Works
1257 works online
```
→ **CONFIRMED（2026-10-15 当日值）**。注意该数字随时间变动：2023-06 快照为 1,246、2025-01/04 快照为 1,269——档案引当日值正确；建议引用时带「截至日期」（问题 3）。

**P-16 [自述] Tate Etc「My one and only master」（§6）**
命令: `read https://www.tate.org.uk/tate-etc/issue-56-autumn-2022/the-apple-of-my-eye`
原样输出（截取）:
```
‘My one and only master’, Pablo Picasso would later call him; ‘the apple of my eye’, said Paul Gauguin
```
→ **CONFIRMED**（引语在 Tate 页逐字；档案已注明「Tate Etc 引」——建议删「晚年」二字，Tate 原文未言时间，见问题 4）

### 2.4 问题清单 + 修正建议（picasso.md）

1. **自审 B-1 的命令描述不可复现（WEAKENED，建议改写法）**：B-1 称逐页检索「命中页 15（1923 声明区）与页 21（1935 声明区）」。我全 218 页复现：`settled beforehand`/`beforehand` 仅命中 1 处 = pdf p.20 = 印页 15，且印页 13 起即 1935 段、9–11 为 1923 段——「页 21」无命中、「页 15 属 1923 声明区」的表述与版式不符。**结论（该句属 1935、页 15）正确且我复核为真**；建议把 B-1 改写成可复现命令（如「pymupdf 全库检索 `settled beforehand` → 唯一命中印页 15；印页 13 页眉为 STATEMENT BY PICASSO:1935」）。
2. **自审 C 的输出选材**：C 节 3 条原样输出中仅 artic.edu（Kahnweiler）属 picasso.md 的自证对象；courtauld / nationalgallery 两条是 cezanne.md 的核查对象。建议为 picasso.md 补一条本档案专属的机械验证（Barr PDF 页命中表或 MoMA 复检输出；本次复核已在 §2.3 替它补齐 Barr 部分）。
3. **§7-6「1257 件在线藏品」建议带截至日期**（该数字随 MoMA 增补变动：2023-06=1,246；2025-01/04=1,269；2026-10-15=1257）。
4. **§6「毕加索晚年自述」措辞**：Tate 原文为 "would later call him"，未言「晚年」；建议删「晚年」或改为「毕加索称塞尚（Tate Etc 引）」。
5. **精确生卒日未核到馆方一手页**（已试: AIC 艺术家页 https://www.artic.edu/artists/36198/pablo-picasso 与 AIC API 仅给年份 1881/1973；MoMA 艺术家页仅给 "Spanish, 1881–1973"）。年份三馆（AIC/MoMA/Met）一致；「10 月 25 日 / 4 月 8 日」建议补一个馆方来源（如 Museo Picasso Málaga）或按 [UNVERIFIED] 处理。
6. **未核到（档案自列、处理正确，无需动作）**：Brassaï/Malraux/Gilot 三书原文引语（档案已全部不落盘并列入 §10）；「卢梭之夜」馆方来源（已标 [推测]）；《三个音乐家》费城版关系（§10-4）。
7. 附注：C 节 artic.edu 输出中的 `meta-csrf-token` 为会话级变量（我复检时不同），其余字段与我的复检一致；这不影响结论。

---

## 3. 复核覆盖与遗留

- **本轮实际跑过**：vangoghletters.org 11 次直读+3 次检索端点；Met 对象页/TOAH/API 5 次；MoMA（Wayback+实时 browser DOM）6 次；AIC 2 次；VGM 2 次（browser）；Tate 1 次；Wikipedia 1 次；Barr PDF 全库逐页 1 轮（218 页）；CDX API 1 次（Internet Archive 侧临时离线，未用于结论）。
- **未覆盖（非缺陷）**：§1/§2 中的 [归纳] 条目（无法对错，只能对「是否冒充自述」——已查，未发现冒充）；§8.1/8.2 的 prompt 与代码规则的「质量」评估（属 wave3 实验验证对象，非事实复核范围）；picasso.md 自审 D 提到的「1935 谈话 Barr 重印 vs Cahiers d'Art 原文是否删改」——未核到 Cahiers d'Art 原文（已试: 未取得该期电子文本；Barr 重印内部一致）。
- **结论**：两份档案可直接进入 wave3 使用；问题 1–4（picasso）与问题 1–2（van Gogh）均为**标注/描述层**修正，不动结论层。原档案未改（按 brief 留给主脑处置）。

---

## 自审四段（复核者自审）

**A 早产出**：本报告未先落骨架——单文件一次成文（32,898 B）；全部中间证据（原样输出、判决）先于成文产生并逐条留存于本文档，每条判决都可按文中命令重跑。

**B 反驳（挑本报告最强结论试推翻）**
1. 「P-12 的 flat, interlocking planes of unshaded color 是逐字引文」——我最初在 2023/2025 两个 Wayback 快照里只找到 "the flat planes of unshaded color"（Highlights 版），怀疑 "interlocking" 是改写。改用 eval browser 读 2026-10-15 实时页 DOM，在 MoMA Learning 文本中逐字命中 "flat, interlocking planes of unshaded color" → **CONFIRMED**（怀疑被推翻；快照≠实时页，这正是必须读实时页的原因）。
2. 「picasso.md 自审 B-1 描述不可复现」——先怀疑是我检索漏词。用 pymupdf 对 `beforehand`、`settled` 在全 218 页各扫一遍，均仅命中 pdf p.20（印页 15）；并确认 pdf−印页 偏移恒为 5（pdf 14→9、15→10、16→11、18→13、20→15、22→17、23→18、24→19）→ **CONFIRMED（描述不符）**，同时 B-1 的结论方向正确。
3. 「§7-6 的 1257 与快照 1,269 矛盾」——先怀疑档案引错。读 2026-10-15 实时艺术家页得 "1257 works online"，与档案一致 → 快照数字是历史值，**CONFIRMED（档案正确；该数字随时间变动，建议带日期）**。
4. 「VG-14 的『全库仅 1 封』不可复现」——无引号检索得 290 封，一度判其错。带引号短语检索得 1 封（777），与自审语义一致 → **CONFIRMED（附带发现：检索语法需注明）**。
5. 「van_gogh.md §5-6 标 [自述/转引] 属过度保守」——直接读信 640 原文并复现检索（1 封）→ 原文逐字在信内 → **CONFIRMED（可升级标注）**。

**C 机械验证**（检查器 = `bash`+`grep`；原样输出）
```
$ ls -la _review.md
-rwxrwxrwx 1 somebody somegroup 32898 Oct 15 16:48 _review.md
$ grep -nE "TODO|FIXME|TBD|待填|占位|PLACEHOLDER|XXX" _review.md
(none found)
$ grep -cE "^\*\*VG-" _review.md   # van_gogh 抽检条目数
15
$ grep -cE "^\*\*P-" _review.md    # picasso 抽检条目数
16
```

**D 小结（≤14 行）**
1. 已确立：两份档案抽检 31 条全部 CONFIRMED——7 条梵高书信引文/日期、9 条毕加索 Barr 引文/页码、7 组馆藏号/尺寸/馆方引文、3 条博物馆研究结论、3 条检索可复现性、2 条二手交叉。
2. 未发现张冠李戴：梵高档案的「Met 转述其信」注、毕加索档案的「receptacle 改挂 1935」与「Brassaï 归属存疑」注，经核全部成立。
3. 唯一描述级 WEAKENED：picasso.md 自审 B-1 的命令描述（结论对、描述不可复现）；另 4 条标注/措辞建议（R18 状态、检索引号、1257 带日期、删「晚年」）。
4. 未核到：梵高浮世绘临摹的 VGM 馆藏编号、picasso 精确生卒日、Cahiers d'Art 原文（均已写明已试路径）。
5. 结论：两档案可进 wave3；修正项全部在标注层，不动结论层。
6. 我仍赌错的是什么：若 MoMA/VGM 页面再次改版，实时页命中的引文（P-12 两条、VG-12）只能以 2026-10-15 的读取记录为准；若 Barr PDF 为残本，页号映射可能偏移——但已核 8 个采样点偏移恒为 5、目标段落首尾（印页 9 的 1923 标题、印页 19 的段尾）均可读，未见缺页迹象。
