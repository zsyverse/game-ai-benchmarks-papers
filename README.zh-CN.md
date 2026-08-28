# Game AI 基准与论文

[English](README.md) · 简体中文

这是一份经过一手来源核验的双语资料地图，聚焦 **用 AI 制作游戏** 和 **打造会玩游戏的智能体** 两条主线。

仓库目前收录 **66 个精选条目**，包含 **150 多个一手来源链接**。它会明确区分可复现 benchmark、数据集、环境、论文、工具与演示项目——因为“能玩的 demo”不自动等于 benchmark。

最近一次完整核验：**2026-08-29**。

## 浏览资料库

| 方向 | 中文 | English | 覆盖内容 |
| --- | --- | --- | --- |
| 游戏创作 | [基准与论文](docs/zh-CN/game-creation.md) | [Benchmarks & papers](docs/en/game-creation.md) | 9 个 benchmark/数据集、7 篇生成或开发智能体论文、7 个交互世界系统 |
| 游戏智能体 | [基准与论文](docs/zh-CN/game-agents.md) | [Benchmarks & papers](docs/en/game-agents.md) | 25 行 benchmark/环境/平台、18 篇精选智能体论文 |
| 核验底稿 | [游戏创作来源](research/game-generation-sources.md) | [游戏智能体来源](research/game-agent-sources.md) | 详细任务定义、指标、工件状态、访问限制及来源依据 |

## 快速导航

| 如果你想评测…… | 建议从这里开始 |
| --- | --- |
| 修改真实游戏引擎仓库的智能体 | [GameDevBench](https://github.com/waynchi/gamedevbench)（Godot，确定性测试）、[GameEngineBench](https://github.com/Nitrode-Research/GameEngineBench)（Unreal C++，行为测试） |
| 端到端生成完整游戏 | [GameCraft-Bench](https://github.com/FreedomIntelligence/gamecraft-bench)（Godot）、[V-GameGym](https://github.com/alibaba/SKYLENAGE-GameCodeGym)（Pygame） |
| 程序化关卡或内容生成 | [PCG Benchmark](https://github.com/amidos2006/pcg_benchmark)、[VGLC](https://github.com/TheVGLC/TheVGLC)、[GVGAI](https://github.com/GAIGResearch/GVGAI) |
| 跨多款游戏的 LLM/VLM 智能体 | [BALROG](https://github.com/balrog-ai/BALROG)、[VideoGameBench](https://github.com/alexzhang13/videogamebench)、[SmartPlay](https://github.com/microsoft/SmartPlay)、[GameBench](https://github.com/Joshuaclymer/GameBench) |
| Minecraft 与开放世界智能体 | [MineDojo](https://github.com/MineDojo/MineDojo)、[MineRL](https://github.com/minerllabs/minerl)、[BEDD](https://github.com/minerllabs/basalt-benchmark)、[Crafter](https://github.com/danijar/crafter) |
| 经典 RL / 游戏套件上的泛化 | [ALE](https://github.com/Farama-Foundation/Arcade-Learning-Environment)、[Procgen](https://github.com/openai/procgen)、[NLE](https://github.com/NetHack-LE/nle)、[MiniHack](https://github.com/NetHack-LE/minihack) |
| 竞技或多智能体游戏 | [SMACv2](https://github.com/oxwhirl/smacv2)、[Melting Pot](https://github.com/google-deepmind/meltingpot)、[OpenSpiel](https://github.com/google-deepmind/open_spiel)、[Honor of Kings Arena](https://github.com/tencent-ailab/hok_env) |
| Action-conditioned 交互世界 | [DIAMOND](https://github.com/eloialonso/diamond)、[Oasis](https://github.com/etched-ai/open-oasis)、[GameGen-X](https://github.com/GameGen-X/GameGen-X)、[Matrix-Game](https://github.com/SkyworkAI/Matrix-Game)、[Hunyuan-GameCraft](https://github.com/Tencent-Hunyuan/Hunyuan-GameCraft-1.0) |

## 仓库使用的标签

### 资源类型

| 标签 | 含义 |
| --- | --- |
| `Benchmark` / `B` | 具有可重复任务以及评测协议或指标 |
| `环境` / `平台` / `P` | 交互式研究接口，可能没有唯一固定任务集或总分 |
| `数据集` | 可复用数据，但不一定定义完整评测方法 |
| `论文` | 研究方法或成果，不一定能够作为 benchmark 复用 |
| `工具` | 开发或评测基础设施 |

### 复现性

| 标签 | 含义 |
| --- | --- |
| **Yes** | 公开任务/数据以及可运行的评测或训练/推理代码，原则上可得到同定义分数 |
| **Partial** | 部分工件已公开，但所需任务、测试、输出、评分器、数据、权重或授权资产仍有缺失 |
| **No** | 截止核验日期，没有同时提供固定 benchmark 协议与可用工件 |

## 重要注意事项

- **世界模型与游戏构建智能体是两类任务。** 前者在动作条件下预测像素或 latent，后者在游戏引擎中编辑代码、场景和资产，两者不应共用排行榜。
- **模型评分与确定性测试的分数不等价。** 应记录 judge 模型/版本、随机种子、游戏或引擎版本、交互预算和聚合规则。
- **商业游戏与素材有独立许可。** 公开 GitHub 仓库不代表同时获得 ROM、游戏客户端、引擎 SDK、视频或训练数据的使用权。
- **工件状态会变化。** 截止核验日期，GameXpert-Bench 仍只有发布占位仓库，JamBench 也没有可核验的官方工件链接；即使论文描述了完整 benchmark，本仓库仍将两者标为 **No**。

## 仓库结构

```text
.
├── README.md / README.zh-CN.md
├── docs/
│   ├── en/       # 英文完整对照表
│   └── zh-CN/    # 中文完整对照表
├── research/     # 一手来源核验底稿
└── .github/      # 资源推荐 Issue 模板
```

## 参与贡献

欢迎补充和纠错。请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，并至少提供一个一手来源链接、资源类型、任务、指标、工件状态，以及语义对应的中英文简介。

## 许可证

本索引使用 [MIT License](LICENSE)。所链接论文、代码、数据集、游戏、模型及其他工件仍遵循各自的原始许可证。
