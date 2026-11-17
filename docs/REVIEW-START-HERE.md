# Review start here — 当前可查看交付

2026-11-18 的收口修复已把当前工程成果、历史记录和未验证效果分开。先看[完整审计](audit/closure-20261118/REVIEW.md)，再按下列入口查看实际内容。

| 想看什么 | 入口 | 观看重点 |
| --- | --- | --- |
| 12段 Motion | [画廊](../experiments/motion_closure/gallery/index.html) | 03书体/中文/拉远；14相机连续性和小量比例说明；其他片逐段播放与拖动 |
| 三个 UI 案例 | [UI README](../examples/ui/README.md) | 当前截图、交互入口、真实浏览器记录和适用范围 |
| 76位画家怎样学习 | [学习索引](../knowledge/domains/painters/learning/INDEX.md) · [覆盖矩阵](../knowledge/domains/painters/learning/COVERAGE-MATRIX.md) | 新增7份决策流程均有选择、取舍、失败条件和来源 |
| 七个 seed 的实际产物 | [seed 包](../experiments/designer_seeds/README.md) | 原型机制及PNG/SVG；均为E1，不代表作者算法 |
| 新消费者失败案例 | [消费者说明](skill/consumer-evidence.md) · [A/B](../experiments/consumer_skill/C1-closure/) | 局部指标通过为何仍出现对象辨识问题 |
| 真人评分 | [23格查看指引](HUMAN-REVIEW-VIEWING.md) · [评分表](HUMAN-REVIEW-SCORES.md) | 22实验格＋1可选基线；实际看图后填写，当前留空 |
| 文件权利与能力边界 | [NOTICE](../NOTICE.md) · [CAPABILITIES](../knowledge/CAPABILITIES.md) | 39明确需署名、699未标需署名、1条件不确定；逐文件判断 |

## 在本地播放 Motion

从仓库根目录运行：

```sh
python experiments/motion_closure/tools/serve_gallery.py --port 8765
```

打开 http://127.0.0.1:8765/gallery/index.html 。完整可复验命令、字体/运行时依赖和证据路径见 [Motion README](../experiments/motion_closure/README.md)。GitHub源码页不直接运行HTML；本地画廊提供真实视频控件。

最终版本和干净克隆复验见 [FINAL-GATE.json](audit/closure-20261118/FINAL-GATE.json) 与对应 release；人工评分、图像服务和研究等级不由发布动作自动升级。
