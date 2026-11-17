# C1-CLOSURE-20261118-001 — 有限消费者结果

## 结论

**protocol_complete = true；case_verdict = failed。**

本次完成了公共入口自主检索、三值构图A、独立封存后的真实CUE、第二题材B、两张实际PNG观察、ML/VM/LS分组与留出次序、冻结方案的局部测量和真实坏例检验。失败判定针对实际构图的充分性：两图局部“受光结构—背光失边—视觉重心”关系有实现，但A主体像壶而非布袋，B过度失边使车体不完整，未充分保持可读形体。H1记 **partial**，本次不足以宣布跨题材构图消费成功。没有技术阻塞，也没有为保绿改判据或修改封存图像。

H2在这三份实际观察的范围内，支持把绘画复制图、线描和壁面绘画照片的边界说清。这个判断不代表全库泛化、艺术家心理、真人学习收益或审美接受。root仍负责独立裁决，本消费者不自写accepted。

## 实际交付

- A：`A/01-focus-plan.json`、`A/01-focus-plan.svg`先标视觉重心；`A/02-three-value-sketch.svg`为种子库布质样本袋三值稿；`A/02-sketch-spec.json`列出应弱化外缘和理由。A不可改。
- A真实渲染：`B/A-render.png`，960×640；本模型已看图并记录题材辨识缺陷。
- B：`B/second-topic-spec.json`先标焦点及边缘，`B/second-topic.svg`为山口履带气象测量车，`B/B-render.png`为实际渲染；本模型已看图并记录车体合灰过度。
- `B/measurement-plan.json`和`B/check-compositions.py`在测量前冻结；`B/PRE-HOLDOUT-SEAL.json`在LS像素之前锁定二题、规格、计划和检查代码。
- `B/bad-outline.svg/.png`是真实坏例；`B/measurement-results.json`记录具体拒绝，`B/observation-and-scope.md`给出H1/H2、来源署名和时序。
- `cue-gate-result.json`记录有效CUE读取前的全部校验；最终文件清单、A不变复核与receipt随附。

## 选择与来源

本消费者从 `knowledge/INDEX.md` 的实际相对链接进入学习导航，独立选择da_vinci路径的三级起稿及非人物分支。依据公共学习路径L87–91的暗底／中间调／亮部起稿、模块L75的暗侧化开和亮部保结构，将其应用为局部明暗邻接及同值失边。把最显著邻接放在指定焦点，是本消费者的构图推论，不冒充来源原文或艺术家意图。

学习路径SHA为 `00a7010818682d14c14003f8e2ef06949ff25fb1bcc4ef1deca76986dde22730`；模块卡SHA为 `e6ad4d1b24b25994bfc4cc467677d1f323545e28bba17f1efd7428f8dcc88cc3`。全部读取范围、八个Stage A实际读取blob和导航依据见 `A/source-read-ledger.json`、`A/retrieval-log.md`。六入口均实际核对原字节，未借父仓库git。

来源含球体、面部局部、人物提示词和具体量规，暴露已诚实记录。没有读取旧消费者、隐藏答案、其他分析文件或其他会话。Stage A图像像素暴露为0；Stage B参考分组来自root CUE，hint_level=2，不能称无提示泛化。

## 数值与图像并列解释

固定ROI中，A暗/亮值分别42.438%/24.683%，B分别51.958%/18.597%，两者RGB跨度144；预标失边横截线的相邻差均为0。恢复A失边外轮廓后，真实PNG出现136→64→136，差72，具体错误 `LOST_EDGE_A_E1_ADJACENCY_BROKEN` 成立。源SVG均只有三种灰值；PNG抗锯齿后A有145种灰值、B有144种。这些事实证明局部表示与检查器执行有效，不能证明形体可读、注意力或审美有效。

本次实际看图进一步发现了前述形体损失，因此不能用检查全绿代替个案判定。未满足完整连续渐变机制；未测Canny链、源L阈值、空气透视色相/饱和、Laplacian或真人视觉注意。三值草图的硬形块不能称完整sfumato。

ML可见面部/暗发的关系但不只有一个亮区；VM轮廓及几何线是必要表达；LS保留建筑透视、群像手势和贯穿亮桌布，且壁面照片保存状态复杂。LS没有被预设为同域正例。本次三张名画观察不构成模型此前未见、因果学习或全库覆盖的证明。

## 输入身份与接受边界

- case：C1；attempt：C1-CLOSURE-20261118-001；version：C1-CLOSURE-v1；单次1800秒上限。
- 冻结HEAD：`e0cfe964ed8b326721115630faf1e05b00de3f23`；tree：`ae4a28ae66544c77d7a8938194d5d6f32f6bedcd`。
- binding：`5e0bdad6fad5c3186a97b5ca0cb0f7c70aa06c36cbbf8cb4f0e2e8e045aa8744`。
- 请求模型：`native_subagent_inherited_parent`；served model：`unknown`，不伪造型号。
- 执行、局部验证、模型观察与root独立裁决分开；人评和外部接受仍为空。失败也保留完整成果与原时序，不启动重试。
