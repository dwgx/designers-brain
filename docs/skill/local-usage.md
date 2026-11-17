# 本地加载与来源核对

从你要使用的仓库版本开始。先让 agent 读取 [SKILL.md](../../skills/designers-brain/SKILL.md)，再使用该文件旁的解析器；不要根据当前工作目录猜测知识根目录。

## 仓库自身检查

在 checkout 根目录运行：

```text
python -X utf8 -B skills/designers-brain/resolve_repo.py --json
python -X utf8 -B docs/skill/_selfcheck.py --repo-only
```

前一命令应返回 `ok: true` 和这份 checkout 的实际 `repo`。后一命令核对仓库文件与引用；`--repo-only` 不检查宿主安装或自然语言自动触发。不要把这两种结果合并成完整消费验收。

## OMP 的实际入口

OMP 18.20.2 提供 `skills.customDirectories`、`skill list --json` 和 `read skill://`。新建一份仅供本次子进程使用的 YAML，将占位路径换成实际绝对路径：

```yaml
skills:
  enabled: true
  customDirectories:
    - "<absolute-checkout-path>/skills"
```

这里指向 `skills` 父目录，而不是 `skills/designers-brain`。在继承该 YAML 的 OMP 子进程中执行：

```text
omp config get skills.customDirectories --json
omp skill list --json
omp read skill://designers-brain:raw
omp read skill://designers-brain/resolve_repo.py:raw
```

本项目的隔离检查通过子进程环境变量 `PI_CONFIG_FILES` 指向该 YAML，`PI_CODING_AGENT_DIR` 指向临时状态目录，`OMP_PROFILE=default`；不会修改全局配置或复制凭据。进程退出后，本次临时注册结束。日常使用可按宿主自己的配置方式登记相同目录。

检查 `skill list --json` 的唯一目标条目：其顶层 `filePath` 应是新 checkout 的 `SKILL.md`，`baseDir` 应是同一 skill 目录。`:raw` 读取的内容应与这份源文件完全一致。随后运行该目录的 `resolve_repo.py --json`，核对解析后的 Git commit/tree；不能因名字相同或输出含有关键词就认为加载了新版本。

宿主发现和文件读取属于工程检查；自然语言是否选中正确 skill、能否满足设计需求，以及图像/动画/Blender 是否实际生成，需要各自的消费或输出证据。其他宿主的安装方式由该宿主定义，仓库附带的 plugin manifests 不是所有宿主已完成安装的证明。

## 开始一次设计任务

先读[能力矩阵](../../knowledge/CAPABILITIES.md)，选择具体实体及输出路线，再按 [SKILL](../../skills/designers-brain/SKILL.md) 补齐主题、受众、素材、风格和替换意图。学习任务从[76条路径](../../knowledge/domains/painters/learning/INDEX.md)进入；纯风格候选和反例从[风格索引](../../knowledge/domains/painters/style_candidates/INDEX.md)进入。

图像生成脚本需要你当前已授权服务的 `IMAGE_GEN_ENDPOINT` 和 `IMAGE_GEN_API_KEY`。脚本不会自动回退个人配置文件；已有的请求、模型、尺寸与服务失败记录只说明原运行时的状态。仓库不包含服务凭据。
