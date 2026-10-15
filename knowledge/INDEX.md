# 素材索引 — images_index

> 覆盖声明（2026-10-15）：`提示词全文.md` 已 100% 读；`总览_15张卡.jpg` 全图看过；
> 全分辨率单独看过：`00_片头倒计时`、`01_3D质感`、`02_液态`、`11_像素`、`15_综艺花字`、`16_片尾`、`panels/01_panel`。
> 其余卡片（03-10、12-14）的信息 = 总览图缩略 + 全文转录（两者一致）；如后续需要逐张全分辨率复核，见 GOALS D-03。

## 1. `knowledge/domains/motion-graphics/origin/` 本地素材

来源：微信视频号 2026-10 的一条 2m52s 视频（`10cd03a4d43ec624cdbb96bbc0ec1f6d.mp4`，1280×720，30fps）。
内容 = **15 张「10 秒 MG 动画」代码提示词卡片**，页脚署名 `Claude Code · Opus 5.5`。每张卡：左/右一栏提示词 + 一栏 10 秒样片（进度条 00:04/00:10 样式）+ 作品名。

| 文件 | 是什么 |
|---|---|
| `提示词全文.md` | 15 条提示词的**逐字转录** + 切片时间表 + 方法说明 + 观察。17.4KB。 |
| `总览_15张卡.jpg` | 15 张卡的总览拼图（1920×1930）。 |
| `00_片头倒计时.png` | 片头卡：淡紫底大字「5.5」（开场倒计时）。 |
| `01_3D质感.png` … `15_综艺花字.png` | 15 张整卡截图（1920×1080）。 |
| `16_片尾.png` | 片尾汇总卡：15 张缩略图 + 「15 种画风 · 15 段提示词；截图存好，【】里换成你的内容」。 |
| `panels/01_panel.png` … `15_panel.png` | 提示词栏 2× 放大裁切图。 |

### 15 卡速览（渲染器 / 收尾文案 / 已见作品名）

| # | 风格（中/英） | 渲染器 | 结尾落地文案 | 作品名（卡片页脚，已见者） |
|---|---|---|---|---|
| 01 | 3D 质感 / 3D MATERIAL | **Blender Python** | PLAY | 《PLAY》 |
| 02 | 液态 / LIQUID | 网页逐帧（WebGL 着色器） | 合 | 《合》 |
| 03 | 等轴 2.5D / ISO 2.5D | 网页逐帧 | 书归原位 | — |
| 04 | 复古未来 Synthwave / RETRO FUTURE | 网页逐帧 | 午夜电台 / FM 88.8 | — |
| 05 | 形变 / MORPH | 网页逐帧 | 灵感 | — |
| 06 | 包豪斯 / BAUHAUS | 网页逐帧 | 3 分 | — |
| 07 | 科幻 HUD / SCI-FI HUD | 网页逐帧 | 着陆成功 | — |
| 08 | 一笔画 / ONE LINE | 网页逐帧 | 山野骑行 | — |
| 09 | 玻璃拟态 / GLASSMORPHISM | 网页逐帧 | 晴朗 | — |
| 10 | 拼贴 / COLLAGE | 网页逐帧 | 猫头鹰日报 | — |
| 11 | 像素 / PIXEL | 网页逐帧 | 大丰收！ | 《大丰收》 |
| 12 | 手绘线条沸腾 / HAND-DRAWN | 网页逐帧 | 早安 | — |
| 13 | 扁平矢量 / FLAT VECTOR | 网页逐帧 | 番茄意面 | — |
| 14 | 贴纸科普 / STICKER SCIENCE | 网页逐帧 | 不到 1% 的水 | — |
| 15 | 综艺花字 / VARIETY TEXT | 网页逐帧 | 完美早餐→焦了？！→烫烫烫→外焦里嫩 | 《焦了》 |

结构解剖见 `knowledge/domains/motion-graphics/cards/structure.md`。

## 2. Owner 与 ChatGPT 对话中引用的作品（远程图床链接，可能过期）

对话里为 8 位画家各配了示例图。图床（`images.openai.com` 静态链接）**已抽 1 条验证**（2026-10-15 实测：《印象·日出》链接返回 image/jpeg 正常；其余 [UNVERIFIED]）；
正典来源建议用 Wikimedia Commons / 馆方开放数据（GOALS D-02 入库）。

| 画家 | 引用作品 | 馆藏（核对用） |
|---|---|---|
| 达·芬奇 | 《岩间圣母》Virgin of the Rocks | 卢浮宫（另有伦敦版） |
| 达·芬奇 | 头图（Doronchenkov 访谈配图） | — |
| 米开朗基罗 | 《创造亚当》局部 Creation of Adam (detail) | 西斯廷礼拜堂 |
| 米开朗基罗 | 《利比亚女先知》Libyan Sibyl | 西斯廷礼拜堂 |
| 梵高 | 《麦田与柏树》Wheat Field with Cypresses (1889) | 大都会艺术博物馆 |
| 莫奈 | 《印象·日出》Impression, Sunrise (1872) | 玛摩丹莫奈美术馆 |
| 莫奈 | 《睡莲》Water Lilies | 橘园/各馆多版本 |
| 毕加索 | 《丹尼尔-亨利·卡恩维勒肖像》Daniel-Henry Kahnweiler (1910) | 芝加哥艺术博物馆 |
| 毕加索 | 《三个音乐家》Three Musicians (1921) | MoMA |
| 塞尚 | 《圣维克多山》Mont Sainte-Victoire | 多版本（MoMA/普希金等） |
| 马蒂斯 | 《红色画室》Red Studio (1911) | MoMA |
| 葛饰北斋 | 《神奈川冲浪里》Great Wave off Kanagawa | 大英博物馆等 |
| — | 泛用头图 ×3（西班牙语艺术史文章、Artpedia、Khan Academy、Gagosian/Damien Hirst） | 与 8 画家无直接关系 |

## 3. 源视频

`10cd03a4d43ec624cdbb96bbc0ec1f6d.mp4`（1280×720, 30fps, 2m52s, 视频号 2026-10）：
**本机未找到**（已查 Downloads / Videos / Desktop / 项目目录，2026-10-15）。**已定位线上来源（2026-10-15，Bing 检索）**：
- Bilibili《用AI做MG动画视频效果真不错！15种风格提示词全分享出来》 https://www.bilibili.com/video/BV1g7po6qEgM/
- YouTube "Claude Opus 5.5 animation: 15 styles with music and sound" https://www.youtube.com/watch?v=EGTvXtF_SQE（15 卡展示片本体候选，下载中）
- 作者：Vincent文森特 @VincentWei93（X 帖 https://x.com/VincentWei93/status/2104957548797604116）；展示页 https://vincentwei1021.github.io/mg-styles-15/（页面自述：15 支 10 秒片，全部由 AI 按提示词写代码渲染，附成片/说明/提示词/源码）
- 同作者另一项目：video-shotcraft（Claude Code / Codex 视频技能包） https://vincentwei1021.github.io/video-shotcraft/
**下载状态（2026-10-15）**：两条均已下载至 `knowledge/domains/motion-graphics/sources/`——① Bilibili 教程片（123s，作者出镜讲解：两智能体分工 / 只换内容不动骨架）；② YouTube 展示片（179s，1080p，= 仓库 `videos/` 15 支片的合集展示；其风格标签与 15 卡互为同一系统的不同中文译名）。另：仓库 `videos/` 目录含 15 支成片 mp4（4–38MB/支，raw 直链可取，如 `videos/20-pixel.mp4`）。见 GOALS A-13 / D-03。

## 4. 待办

- D-02：**已完成**——33 张代表作图 + `knowledge/domains/painters/dossiers/_images/manifest.md`（282 行，逐张 license）。
- D-03：15 卡样片关键帧对照（源片已备；仓库 15 支参考帧已抽至 `knowledge/domains/motion-graphics/sources/refs/`，样式↔卡片映射注记待补）。
