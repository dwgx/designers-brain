# refs — mg-styles-15 参考帧与「15 支片 ↔ 15 卡」映射（D-03）

> **上游**：GitHub 仓库 `Vincentwei1021/mg-styles-15`（MIT）→ `videos/` 15 支成片，raw 直链模板
> `https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/videos/<slug>.mp4`
> **对照物**：`research/origin_cards/`（15 卡截图 + 提示词全文）+ `research/agent-art/cards/mg-styles-15_compare.md`（B-10 逐条对照；规则级证据见其 §2.1）
> **本目录**：15 张基础帧 `<slug>.png` + 30 张补帧 `<slug>_t3.png` / `<slug>_t8.png` + `_refs_sheet.png`（15 帧总览 5×3）
> **状态**：v1.0 · 2026-10-15 · RefsMapping（wave6）——15/15 映射（视觉 + 规则双通道逐支确认）；补帧 30/30（t=3s/8s，ffmpeg 直读 raw URL）

## 1. 映射表（repo 文件名 ↔ 卡号 ↔ 卡名 ↔ 证据）

> 卡号/卡名 = 本地 15 卡编号（`research/origin_cards/`）；排序 = repo slug 顺序。
> 证据口径：**视觉** = 逐张目检本目录 `<slug>.png`（帧出自对应成片）；**规则** = 仓库 `prompts/<slug>.md` 与卡内「画风段」的量化规则配对（8 组数字指纹级独立命中，见 B-10 §2.0）。

| # | repo 文件名 | 卡号 | 卡名 | 证据 |
|---|---|---|---|---|
| 1 | `videos/01-flat-vector.mp4` | 13 | 扁平矢量 | 视觉：纯色几何城市/角色一镜到底（popwise「One Dot」）；prompt「stagger 2~4 帧」「squash&stretch ~10%」↔ 卡 13「错开 2-4 帧」「压扁约 10%」 |
| 2 | `videos/02-line-art.mp4` | 08 | 一笔画 | 视觉：金色单线画种子→建筑（ATELIER LINEA）；prompt「the whole film is ONE continuous line…tail is the start of the next」↔ 卡 08「整支片子只有一根线…尾巴接着下一个形状的开头」 |
| 3 | `videos/03-isometric.mp4` | 03 | 等轴 2.5D | 视觉：微缩城市 30° 等角（ISOPOLIS）；prompt「30°等角投影」「顶面延迟 2~3 帧盖上」↔ 卡 03「斜线一律 30°」「先落地基，再升墙，最后盖顶」 |
| 4 | `videos/04-3d-render.mp4` | 01 | 3D 质感 | 视觉：粉色软胶字标+克隆球阵（soft.）；prompt「SSS 软胶」「Cloner+Effector 群体波浪」「damped spring jiggle」↔ 卡 01「橡胶透一点光」「一大片小物体像波浪起伏」「压扁、回弹、晃几下才停」 |
| 5 | `videos/05-cel-boil.mp4` | 12 | 手绘线条沸腾 | 视觉：火柴→火焰精灵，纸纹+线抖（手作）；prompt「3~4 张微差线稿循环」「一拍二（实际 12fps）」「smear 只保留 1 帧」↔ 卡 12 逐字同数 |
| 6 | `videos/06-collage.mp4` | 10 | 拼贴 | 视觉：老照片剪贴+半调网点（NOGGIN「脑洞大开」）；prompt「2~4px 白描边」「12fps ±2px 抖动」「嘴巴替换帧」↔ 卡 10「剪刀剪的白边」「一秒 8-12 次、抖一两个像素」「嘴换两三张剪纸」 |
| 7 | `videos/07-liquid.mp4` | 02 | 液态 | 视觉：紫底液滴融合（drop.）；prompt「metaball 融合」「次级液滴延迟 2~3 帧」↔ 卡 02「靠近就融成一团」「小液滴晚 2-3 帧到」 |
| 8 | `videos/08-morph.mp4` | 05 | 形变 | 视觉：蓝底白形链式变形（一形万象）；prompt「先收敛为中介简形（圆/胶囊）再展开」「否则会打结」↔ 卡 05「先收成圆或胶囊，再展开」「不打结」 |
| 9 | `videos/09-bauhaus.mp4` | 06 | 包豪斯 | 视觉：红黄蓝黑网格海报（KONSTRUKTION）；prompt「quarter circles rotate 90°」「禁用 overshoot」↔ 卡 06「旋转是 90° 的倍数」「不回弹、不过冲」 |
| 10 | `videos/10-synthwave.mp4` | 04 | 复古未来 | 视觉：条纹太阳+铬字 NEON DRIVE；prompt「striped retro sun」「RGB split 1~2px」↔ 卡 04「带横条缺口的太阳」「红蓝通道错开一两个像素」 |
| 11 | `videos/12-aurora-glass.mp4` | 09 | 玻璃拟态 | 视觉：极光斑+毛玻璃卡片（Aurora）；prompt「adjacent hues only」「backdrop blur ~30px + 1px 高光」↔ 卡 09「只用相邻 2-3 色」「毛玻璃…一圈细亮边」 |
| 12 | `videos/18-hanazi.mp4` | 15 | 综艺花字 | 视觉：猫咪素材+「？？？」花字（喵呜日记 EP.07）；prompt「pop 0→1.15→1.0 in ~8 frames」「2-frame stagger」↔ 卡 15「回弹约 8 帧」「错开 2 帧」 |
| 13 | `videos/19-paperclip.mp4` | 14 | 贴纸科普 | 视觉：手机贴纸+周期表「70/118」（手机元素）；prompt「charts are exact (bars to scale)」「8~12px 白描边」↔ 卡 14「柱长照真实数字画」「实物照片抠图+白边」 |
| 14 | `videos/20-pixel.mp4` | 11 | 像素 | 视觉：像素游戏场景（PIXEL QUEST）；prompt「Internal 320×180」「PICO-8-like 16–32 colours」「whole pixels」↔ 卡 11 逐字同数 |
| 15 | `videos/22-hud.mp4` | 07 | 科幻 HUD | 视觉：青色 HUD→橙色目标锁定（KESTREL-9）；prompt「cyan #00E5FF…orange alert」「锁定框 scale 1.4→1.0」↔ 卡 07「冷色…状态一变换成暖色」「锁定框从大缩到目标上」 |

## 2. 每支一句话（内容差异 vs 卡内分镜）

> 仓库成片与本地卡为**同一提示词体系的两次独立运行**（B-10 §0.2）：差异统一为「同签名规则、不同故事/文案/配色」；以下只标各支关键差异（仓库片 ↔ 卡内【】分镜）。

1. **01-flat-vector**：popwise「One Dot」——一个圆点串起太阳、城市、窗口角色、通知图标到品牌 logo 的一镜到底解释片；卡 13 分镜是「番茄的旅行」（发芽→货车→意面）——同签名、不同故事与收尾。
2. **02-line-art**：ATELIER LINEA——种子长成建筑、收成字母组合 logo 并填金；卡 08 是自行车→太阳→山脊→徽章「山野骑行」——一笔画语法相同，题材不同。
3. **03-isometric**：ISOPOLIS「城市自己生长」——地块→楼群→车流/传送→拉远成 SMART CITY OS；卡 03 是图书馆还书分拣「书归原位」——等轴语法相同，场景不同。
4. **04-3d-render**：soft.「柔软着陆」——粉色软胶字标 + 铬球 + 克隆球阵；卡 01 是玻璃弹珠浪 + 橡胶 PLAY——材质三件套相同，字标与配色不同。
5. **05-cel-boil**：手作 HAND MADE——火柴划燃→火焰精灵→手绘标题；卡 12 是闹钟「早安」——boil/纸纹/一拍二语法相同，故事不同。
6. **06-collage**：NOGGIN「脑洞大开」——维多利亚头像掀盖涌出太空杂物 + 构成主义大字；卡 10 是猫头鹰主编「猫头鹰日报」——剪贴语法相同，主角不同。
7. **07-liquid**：drop.「万物始于一滴」——液滴融合→波浪→FLUX 字标；卡 02 是液态金属聚成「合」——metaball 语法相同，字标不同。
8. **08-morph**：一形万象——杯→太阳→海→海鸥→纸飞机→定位→心→morphe；卡 05 是灯泡→气泡→铅笔→星星→「灵感」——链式形变相同，链条不同。
9. **09-bauhaus**：KONSTRUKTION「二十拍构成」——120BPM 一拍一动、冻结成包豪斯海报；卡 06 是篮球「3 分」海报——机械网格语法相同，主题不同。
10. **10-synthwave**：NEON DRIVE「霓虹夜驰 1986」——网格飞行→铬字砸落→霓虹手写；卡 04 是「午夜电台 FM 88.8」——VHS/铬字语法相同，标题不同。
11. **12-aurora-glass**：Aurora「思考，自有光」——极光斑 + 玻璃卡片 + 液态镜头扫过；卡 09 是天气 App「晴朗」——玻璃拟态语法相同，产品叙事不同。
12. **18-hanazi**：喵呜日记 EP.07（竖屏 1080×1920）——猫咪素材 + 「？？？」等花字；卡 15 是吐司机「烫烫烫」——花字语法相同，素材层不同。
13. **19-paperclip**：「一部手机里，藏着多少种元素？70/118」——手机贴纸→周期表→柱状图；卡 14 是「地球上的水 不到 1%」——贴纸科普语法相同，题材不同。
14. **20-pixel**：PIXEL QUEST——主角跑跳→宝箱→「欢迎来到像素世界！」；卡 11 是像素渔夫「大丰收」——像素语法相同，剧本不同。
15. **22-hud**：隼眼-9——轨道扫描→目标锁定→橙色警报；卡 07 是着陆舱「着陆成功」——HUD 语法相同，任务不同。

## 3. 补帧（t=3s / t=8s）：清单、命令与坑位

- 文件：`<slug>_t3.png` / `<slug>_t8.png` × 15 支 = **30 张**（命名 = repo slug + 秒数）。
- 规格：随源片——15 支 1920×1080；`18-hanazi` 1080×1920（竖屏）；PNG rgb24。
- 命令（本机实测可跑；本机 ffmpeg **无 glob** → 逐支显式 URL，不依赖本地 mp4）：

```bash
ffmpeg -hide_banner -loglevel error -nostdin -y -ss 3 \
  -i "https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/videos/<slug>.mp4" \
  -frames:v 1 -update 1 "<slug>_t3.png"     # t=8s 换成 -ss 8
```

- 本机坑位（供复用）：① 单帧落盘必须 `-update 1`，否则 image2 报「does not contain an image sequence pattern」；② 本机裸 `bash <script>.sh` 会解析到 WSL（无 ffmpeg）——脚本请在本 shell 直接执行；③ `-ss` 放 `-i` 前 = 输入侧定位（默认 accurate seek，一次下载可取任意时刻）。
- `_refs_sheet.png`：15 帧总览（5×3，行序 = 本表 slug 顺序）；本次重生成（此前为半成品，仅含 19/20/22 三帧）。

## 4. 缺口

1. **编号缺口 7 种**：作者完整风格集 ≥22 种（11 grain / 13 图文快闪 / 14 sticker journal / 15 国潮新中式 / 16 glitch / 17 vaporwave / 21 acid graphics），仓库未发布 → 无片无帧可映射（B-10 §1.3）。
2. **基础帧时刻未记录**：`<slug>.png`（15 张）抽取时刻无记录；本次补帧固定 t=3s/8s（每支 3 个时间点）。如需逐镜头级覆盖，按 §3 命令批量补抽即可。
3. **静态帧边界 + 口径差异**：补帧不含音频/运动/卡点信息（音频研究见 B-10/B-13）；本地卡统一 1920×1080/30fps，仓库 `04-3d-render`、`05-cel-boil` 实为 24fps、`18-hanazi` 为竖屏（B-10 已注记）。

## 5. 验收（原样输出，2026-10-15）

```
=== A. 全量清点（30 个补帧）===
-rwxrwxrwx 1 somebody somegroup  297465 Oct 15 18:31 01-flat-vector_t3.png
-rwxrwxrwx 1 somebody somegroup   24557 Oct 15 18:36 01-flat-vector_t8.png
-rwxrwxrwx 1 somebody somegroup  915109 Oct 15 18:36 02-line-art_t3.png
-rwxrwxrwx 1 somebody somegroup 1032733 Oct 15 18:36 02-line-art_t8.png
-rwxrwxrwx 1 somebody somegroup 2165044 Oct 15 18:36 03-isometric_t3.png
-rwxrwxrwx 1 somebody somegroup 2270929 Oct 15 18:36 03-isometric_t8.png
-rwxrwxrwx 1 somebody somegroup 2308589 Oct 15 18:36 04-3d-render_t3.png
-rwxrwxrwx 1 somebody somegroup 2253996 Oct 15 18:36 04-3d-render_t8.png
-rwxrwxrwx 1 somebody somegroup 2126903 Oct 15 18:36 05-cel-boil_t3.png
-rwxrwxrwx 1 somebody somegroup 2101976 Oct 15 18:36 05-cel-boil_t8.png
-rwxrwxrwx 1 somebody somegroup 3035302 Oct 15 18:36 06-collage_t3.png
-rwxrwxrwx 1 somebody somegroup 2430187 Oct 15 18:36 06-collage_t8.png
-rwxrwxrwx 1 somebody somegroup 1820576 Oct 15 18:36 07-liquid_t3.png
-rwxrwxrwx 1 somebody somegroup 1981783 Oct 15 18:36 07-liquid_t8.png
-rwxrwxrwx 1 somebody somegroup 1570227 Oct 15 18:36 08-morph_t3.png
-rwxrwxrwx 1 somebody somegroup 1553633 Oct 15 18:36 08-morph_t8.png
-rwxrwxrwx 1 somebody somegroup 1233782 Oct 15 18:36 09-bauhaus_t3.png
-rwxrwxrwx 1 somebody somegroup 1253903 Oct 15 18:36 09-bauhaus_t8.png
-rwxrwxrwx 1 somebody somegroup 2300213 Oct 15 18:36 10-synthwave_t3.png
-rwxrwxrwx 1 somebody somegroup 2401985 Oct 15 18:36 10-synthwave_t8.png
-rwxrwxrwx 1 somebody somegroup 1787638 Oct 15 18:36 12-aurora-glass_t3.png
-rwxrwxrwx 1 somebody somegroup 1719125 Oct 15 18:36 12-aurora-glass_t8.png
-rwxrwxrwx 1 somebody somegroup 2171494 Oct 15 18:36 18-hanazi_t3.png
-rwxrwxrwx 1 somebody somegroup 1869673 Oct 15 18:37 18-hanazi_t8.png
-rwxrwxrwx 1 somebody somegroup  532347 Oct 15 18:37 19-paperclip_t3.png
-rwxrwxrwx 1 somebody somegroup  597312 Oct 15 18:37 19-paperclip_t8.png
-rwxrwxrwx 1 somebody somegroup 1907084 Oct 15 18:37 20-pixel_t3.png
-rwxrwxrwx 1 somebody somegroup 1698169 Oct 15 18:37 20-pixel_t8.png
-rwxrwxrwx 1 somebody somegroup 2779682 Oct 15 18:37 22-hud_t3.png
-rwxrwxrwx 1 somebody somegroup 2599733 Oct 15 18:37 22-hud_t8.png

=== B. 抽查 1：01-flat-vector_t8.png ===
width=1920
height=1080
pix_fmt=rgb24
=== C. 抽查 2：18-hanazi_t3.png ===
width=1080
height=1920
pix_fmt=rgb24
=== D. SHA256 ===
21b5771e0cf0198754539d4eb9561edf14d54d93281bb68737c744f7efc7c24a  01-flat-vector_t8.png
e025b9620ab0e0b9a0f964920aa3614a0a6f81c20ed5742cd5515d741cca43f5  18-hanazi_t3.png
```
