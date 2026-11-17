<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-degas；原正文 SHA-256 `8f3f17ae2137f970ba1687a28789e023032f9fb71a5160d4c12e8bee002553e1`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 风格级强反例 — `degas` [inference]

> 全部为**纸面推演 [inference]**，未渲染像素、未跑生成通道、未做 E4。每条给具体撤去/反转/保留操作，点名被破坏的 §8.1b 关系 ID 与 dossier §8.2 规则行。题材对象（舞者、排练室、纱裙、把杆、舞台脚灯、浴女）全部保留，证明「题材齐备≠风格成立」。

<a id="db-source-line-5"></a>
## CE-D1 — 撤去纹理：把「方向性排线 2–5 族」改成均匀圆点 / sfumato 渐变

**操作**：全套芭蕾题材保留；把粉彩排线 + 擦揉 + 覆盖（可见笔触 ≥70%、方向族 2–5、色层 ≥2）换成修拉式均匀点阵，或换成达·芬奇式平滑 sfumato。

**被破坏的规则**：
- R5（§8.2-5 L249「可见笔触 ≥70%、方向族 2–5、平滑渐变带 ≤2% 短边、可见色层 ≥2」）→ 点阵无方向族 / 渐变带超限；
- 连带破 C2（人工光 × 方向性笔触）、C3（方向族 2–5 × 修拉点阵互斥）。
- 对应 §4 越界警报②「均匀点阵 + 补色光学混合、人物几何化定格 → 越界**修拉**」、§8.1 负向 `no uniform pointillist dots, no optical colour mixture, no smooth gradients`。

**为何是风格级反例**：只换表面笔触系统，未改任何人物/场所；证明「描线成面」是纯方向场关系，不是「画了舞者」的附属。

<a id="db-source-line-16"></a>
## CE-D2 — 反转空间：把「高视点偏心裁切」改成正面居中舞台全景

**操作**：保留舞者、脚灯、粉彩、纱裙；但把视平线从 ≥55% 画高放平、主体居中完整不裁切、地板线族不收敛、四角与中心均匀收尾。

**被破坏的规则**：
- R1（§8.2-1 L245「质心偏 ≥15% 画宽、≥1 处边缘切割、对角横跨 ≥60% 画宽」）→ 居中完整 fail；
- R2（§8.2-2 L246「视平线 ≥55%、俯角 10–25°、地板线族 ≥3 收敛」）→ 平视 fail；
- R8（§8.2-8 L252「四角与中心完成度差 ≥1 档、裸底 ≥5%」）→ 均匀收尾 fail；
- 连带破 C1（取景框 × 高视点）。
- 对应 §8.1 负向 `no symmetrical centred composition, full uncropped figures, stage-front ballet glamour, tutus in perfect rows`。

**为何是风格级反例**：只反转取景/视点关系；证明「frame used like a viewfinder, not a stage」是纯几何关系。

<a id="db-source-line-29"></a>
## CE-D3 — 保留色板撤掉形状：赭/棕/白蓝 + 单点红色还在，但撤掉人工方向光与亮部集中

**操作**：保留 `ochre, burnt sienna, umber, pale blue, viridian, touches of vermilion` 色板与一处红/橙事件；把脚灯/顶灯/窗光换成无源户外自然光 + 大气包络 + 边缘溶解，亮部铺满全画。

**被破坏的规则**：
- R3（§8.2-3 L247「方向性光源夹角 ≤45° 或可见光路、亮部 V≥0.9 集中 ≤35%、暗部 ≥30% 时脸/手仍可读」）→ 无方向光、亮部不集中；
- R5（渐变带 ≤2% 短边）→ 大气包络用宽渐变，fail；
- 连带破 C2（人工光 × 方向性笔触）。
- 对应 §4 越界警报①「无源自然光 + 大气包络、边缘溶解、系列变量为时刻/天气 → 越界**莫奈**」、§8.1 负向 `no plein-air natural light, atmospheric envelope, fog, soft dissolving contours, sfumato`。

**为何是风格级反例**：色板（最直观线索）完全保留，风格仍不成立——反驳「认出赭棕+纱裙白配色就是德加」。

<a id="db-source-line-41"></a>
## CE-D4（内容泄漏反证）— 把「必须有芭蕾舞者/排练室」升为必要条件

**操作**：不改像素，只在集成时把 `dancers in rehearsal / rehearsal room / theatre interior` 写成 §8.1b 前提。

**后果**：[style_only_draft.md](style_only_draft.md) 正例 1（机械车间俯拍）与 §8.1 `[sculpture variant]`（蜡像/铜像、真实布裙）会被误判「不像德加」；§4 用法把 P3/P4 定为「时期与媒介档」、P6 归「工作流参数（不进画面重叠计算）」；§8.2 全部分母是质心偏移 / Hough / 亮度直方图 / 人脸关键点 / 方向场 / 支撑点 / SSIM / 完成度热力图。

**结论**：舞者/排练室是内容基底，不是风格前提；A-55 原书级核验确认「repetition is exactly what the dancers do」是**操作陈述**（工作流），不是内心状态或题材绑定。本反例破的是规则写法，不是像素。

> 与 AUDIT-degas 的关系：其 accepted counterexample.md 是 **§4 机制层**反例（2+1 条，含 70/30 纪律张力）与 A-55 原书级核验；本文件 4 条是**纯风格关系层 [inference]**反例，两者不同层、不互相替代。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [capability_delta.md](capability_delta.md)
- [source-claims.json](source-claims.json)
