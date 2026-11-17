<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-constable；原正文 SHA-256 `3721c426374cb3765917fd458e51d0cd72f4a2df1d7ef2fefe109b03332d4c40`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `constable` §8.1b（draft）

> 比较对象：现有卡 [constable.md](../../modules/constable.md)（`card_sha256=054ebfea…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

现有卡：视觉指纹要点、§8.1 图像 prompt（**正向段把 `mill pond / Dedham / Salisbury / Flatford / haymakers / a cart crossing a ford / pollarded willows / specific recognisable place` 写死为题材**）、§8.2 八条逐帧规则、§4 六参数、冲突注记（C-01/C-09/C-12 引用）。

- **能做**：在「英国乡村记录性风景」**默认题材域**内，用 §8.2 的 8 条（区域分割+边缘梯度、亮度阈值+斑点检测、HSV 掩膜、光流场+轮廓梯度、对象检测+RANSAC 消失点、分区色相/饱和、姿态+人脸、梯度带宽+多尺度能量）自查；`_extract.py --check` 校验 §8.1/§8.2/§4 逐字一致（AUDIT-constable 实测 228/228，constable 已在 ARTISTS 表内；§8.1b 排除）。
- **不能做**：**跨场景路由**。把这套「可读带状天空 + 绿-蓝-红预算 + 白点闪烁 + 无事件 + 软光干笔」迁到抽象地形/气象面板、数据景观、无字 key visual 时，§8.1 正向段会强制带回磨坊/干草车/教堂尖顶，把内容对象当风格前提 → 01-AUDIT.md A06 的混淆。
- **本卡特有的已登记误判**：AUDIT-constable 记录 **1 个 §4 机制强反例**——「云研究档（P2 强、P6 弱、无人物无地标）被 §4 越界警报③『地点不可辨 → 越界弗里德里希』误判」。无 §8.1b 时卡没有把 P4（地点锚定）/P2（题记）写成**档位开关**的写法，跨场景路由会重复这个误判。

<a id="db-source-line-13"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
|---|---|---|
| **介质无关的关系量** | §8.1 绑定地标/农人/树种/云型 | 拆成 R1–R8：天空带(≥35%/云覆盖/地平线梯度带宽比 ≤2)、白点(≥15 个/直径 %短边)、绿-蓝-红预算(面积%/高饱和块=0)、无事件(全局光流 ≤1.5%/帧/轮廓带宽)、锚点+单消失点(RANSAC ≥5 条，**档位可选**)、水镜(色相差/饱和比)、劳作小实例(≤5，**可选层**)、哑光软光(带宽/高光块=0/2–6px) |
| **默认题材泄漏剥离表** | 无 | §1 表把 Dedham/干草车/pollarded willows/「可辨地点」逐项降级；给「迁移判据」；§1 注把 P4 明写为**档位开关**（云研究档 P4 弱合法，不得单轴判越界） |
| **必要耦合 C1–C5** | §3.1 四判据散落 | ⟨R1∧R4⟩ 可见地平线×无事件（与透纳两轴联合）、⟨R3∧R2⟩ 绿底×白点×红点对位、⟨两个归零约束⟩、⟨R5∧R6⟩ 单消失点×水镜、⟨P4 档位开关⟩（AUDIT 反例对应） |
| **正例 + 强反例** | 卡只有同域自查三问 | 抽象地形/气象面板正例（绿 38%/蓝 14%/红 3 处，八条全可算，无需认出干草车/Dedham）+ 无字 key visual；[counterexamples.md](counterexamples.md) 4 条 [inference]：撤纹理抹平白点干笔 / 反转空间改雾幕吞地平线+漩涡 / 保留色板放大红块+硬光 / 内容泄漏反证（把地标/农人升为必要条件会误判云研究档） |
| **适用/不适用 + 组合预检** | 散落 | 7 类不适用 + C-12/C-01/C-09 与 §3.1 透纳 70/30、莫奈「只借色彩亮度保记录结构」、弗里德里希四判据选侧 |

**路由收益（一句话）**：从「认出英国乡村 → 套 §8.1 prompt」升级为「读出 R1–R8 关系 → 判断任意带状/绿底/软光场景是否满足可见地平线×无事件耦合，并按 P2/P4 档位决定是否带锚点/题记层」；跨场景判定**不再依赖地标识别**，且避免云研究档被误判越界。

<a id="db-source-line-25"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：staging-only 草案；[constable.md](../../modules/constable.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**（`card_has_81b=false`）。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在乡村风景默认题材域内自查，但**不获得**跨场景路由能力，AUDIT 登记的云研究档误判风险仍在。不得把「草案已写」记成「卡已具备 §8.1b」。
- **draft ≠ E4 passed**：正例/反例全部 `[inference]` 纸面推演；**未渲染像素、未跑生成通道、未做预注册 E4**（02-EXECUTION-PLAN Lane C）。所有阈值沿用 dossier `[归纳] 未对原作做像素测量（分母＝假想参考帧）`（§8.2 注 L212 / §10-7 L265），不升级为 validated。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-constable]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-constable]

<a id="db-source-line-32"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3；02-EXECUTION-PLAN.md Lane C；03-RESEARCH-AGENDA.md L145/L149；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） constable `card_has_81b=false`；AUDIT-constable/receipt.json + counterexample.md（accepted；3 处内容漂移 + 1 个 §4 机制强反例；与 friedrich.md §3.1 互查 CONFIRMED）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
