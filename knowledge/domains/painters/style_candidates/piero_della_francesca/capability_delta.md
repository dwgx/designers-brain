<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-piero_della_francesca；原正文 SHA-256 `eebe88f32b51e6a5b761656a032c2c9f6cf4ebff798157991ef0bdd7ea6a4964`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `piero_della_francesca` §8.1b（draft）

> 比较对象：现有卡 [piero_della_francesca.md](../../modules/piero_della_francesca.md)（`card_sha256=54bba5ba1373…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

现有卡：视觉指纹要点、§8.1 图像 prompt（**正向段把 皮耶罗·德拉·弗朗切斯卡 默认题材专名写死为题材**）、§8.2 逐帧规则、§4 六参数、冲突注记。

- **能做**：在「几何秩序圣像/湿壁画组画」**默认题材域**内，用 §8.2 的 8 条(列梯度+质心+地砖行、Hough 拟合+消失点、影向直方图+影长、径向衰减拟合、HSV 统计、光流+镜像+视线、多边形近似+直线占比、影形拟合+光向)自查 `_extract.py --check` 所校验的 §8.1/§8.2/§4 逐字一致(AUDIT-piero 记录 §8.1b 被排除在逐字比对之外)。
- **不能做**：**跨场景路由**。把「主轴网格 + 透视收敛 + 一致浅影 + 珍珠浅调 + 静止 + 低多边形轮廓 + 几何影」迁到抽象轴线海报、建筑透视 UI、等距信息图时，§8.1 正向段会强制带回受洗/复活/鞭笞圣像、托斯卡纳山谷与「sacred narrative」体裁，把内容对象当风格前提 → 01-AUDIT.md A06 所指「有模块/能抽取/已做纯风格迁移」混淆。
- ****本卡特有的档位内张力(AUDIT-piero 登记)**：§4 P3 把「夜景档(画内点光源)」写成显式切换，而 §8.2-3(昼档影一致/无第二主光源)与 §8.2-4(夜档径向衰减)分属两档、不可同时套；§3.1 vs 达·芬奇写「明暗过渡带窄」但 §8.2 无独立过渡带规则，靠 R7/R5 间接约束。另《圣诞》「影被刻意省略」(§7-2 L138)为神迹档特例。无 §8.1b 时卡没有「P3 昼/夜单主开关」的写法，跨场景路由易把两套光源自查混用。**

<a id="db-source-line-13"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
|---|---|---|
| 介质/语义无关的关系量 | §8.1 绑定受洗/复活/鞭笞/圣母/真十字架/托斯卡纳 | 拆成 R1–R8：主轴贯穿/质心偏差/地砖行、消失点/角度误差/尺度、影向夹角/影长/次峰、中心距/衰减R²、平均饱和/明度中位/色相、模糊核/镜像/直视、折线段/直线占比、影形自洽——全是列梯度/Hough/HSV/拟合统计量 |
| 默认题材泄漏剥离表 | 无 | §1 表把作品名/圣像/地名、建筑器物清单、宗教体裁与永恒品题、颜料绿灰底考据、透视论著作名逐项降级；给迁移判据：撤专名后 §8.2 自查仍可算 = 纯风格；夜景档只留**径向衰减统计量** |
| 档位显式化 | 卡内昼/夜两档自查、窄过渡带未处理 | §1 注把 P3 写成**昼/夜单主开关**(昼用 R3、夜用 R4，不同时启用)、把「窄过渡带」标为「由 R7/R5 间接约束、须显式取值」；C1–C5 列出 ⟨主轴×收敛⟩、⟨光一致×影几何⟩、⟨浅调×低多边形⟩、⟨静止×轴线⟩、⟨档位互斥⟩ |
| 正例 + 强反例 | 卡只有同域自查三问 | 抽象轴线网格海报正例(八条全可算，无需认出圣像)+ 等距 UI 信息图正例；[counterexamples.md](counterexamples.md) 3 条 [inference]：撤清晰边缘改 sfumato / 保留轴线改色阶扭转 / 内容泄漏反证 |
| 适用/不适用 + 组合预检 | 散落在越界警报 | 列 6 类不适用(sfumato、色阶扭转、画外单光、扭转人体、点状高光、巴洛克动势)+ C-02/C-05/C-10/C-01/C-14 预检 |

**路由收益（一句话）**：从「认出皮耶罗圣像 → 套 §8.1 prompt」升级为「读出 R1–R8 关系 → 判断任意轴线/透视场景是否满足主轴×收敛、光一致×影几何等耦合，并按 P3 档位决定昼/夜光源自查」；跨场景判定**不再依赖受洗/鞭笞或透视论著作名**。

<a id="db-source-line-25"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：回退契约：staging-only 草案；[piero_della_francesca.md](../../modules/piero_della_francesca.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**(`card_has_81b=false`)。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在默认题材域内自查，但**不获得**跨场景路由能力，也不解决昼/夜档与窄过渡带张力。不得把「草案已写」记成「卡已具备 §8.1b」。
- **草案与实测分离**：轴线/收敛/影几何的正反例是 `[inference]` 纸面判读；未渲染像素、未接生成通道、未跑预注册 E4。皮耶罗 §8.2 注 / §10-9 的 `[归纳] 未实测` 与昼/夜档互斥口径不升格为 validated。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-piero_della_francesca]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-piero_della_francesca]

<a id="db-source-line-32"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3（11/76 存在性检查非 E4）；02-EXECUTION-PLAN.md Lane C；03-RESEARCH-AGENDA.md；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） piero_della_francesca `card_has_81b=false`；AUDIT-piero_della_francesca/receipt.json（accepted）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
