# 游戏生成 Benchmark 与论文

[English](README.md) · 简体中文

> 经过一手来源核验的双语资料库：只收录**生成游戏的 AI**，不收录玩游戏的 AI。

本仓库覆盖生成完整游戏、可执行规则与机制、游戏代码与引擎工程、关卡与可玩内容，以及动作条件交互世界的研究。目前包含 **82 条详细分类记录**（允许有意义的跨分类重复），以及 **200 多个论文与官方工件链接**。

最近一次完整核验：**2026-08-29**。

## 按生成目标浏览

| 专题 | 中文 | English | 覆盖范围 |
| --- | --- | --- | --- |
| 端到端游戏与代码 | [29 个 benchmark 与论文](docs/zh-CN/end-to-end.md) | [29 benchmarks and papers](docs/en/end-to-end.md) | 提示词到游戏、引擎/工程/代码生成、游戏开发 agent、验证、修复与共创 |
| 自动游戏设计与 PCG | [35 篇论文与资源](docs/zh-CN/pcg.md) | [35 papers and resources](docs/en/pcg.md) | 完整游戏、规则/机制、关卡生成、数据集、PCG benchmark 与奠基综述 |
| 可交互游戏世界 | [18 篇论文与资源](docs/zh-CN/interactive-worlds.md) | [18 papers and resources](docs/en/interactive-worlds.md) | 动作条件视频世界、学习式游戏引擎、显式状态/机制、多人和长时生成 |
| 详细证据 | [一手来源核验底稿](research/README.md) | [Research notes](research/README.md) | 任务定义、评测协议、工件可用性、边界判断和一手来源依据 |

精确的收录与排除规则见 [SCOPE.md](SCOPE.md)。

## 什么算“生成游戏”？

| 层级 | 输出 | 代表工作 |
| --- | --- | --- |
| 完整游戏 | 包含玩法、规则、场景、代码和资产的可运行工程 | [AutoUE](https://arxiv.org/abs/2603.07106)、[OpenGame](https://arxiv.org/abs/2604.18394)、[GameCraft-Bench](https://arxiv.org/abs/2606.17861)、[V-GameGym](https://arxiv.org/abs/2509.20136) |
| 规则与机制 | 定义新玩法的可执行游戏描述或程序 | [Ludi](https://eprints.qut.edu.au/17025/)、[ANGELINA](https://doi.org/10.1109/CIG.2011.6032019)、[GAVEL](https://arxiv.org/abs/2407.09388)、[GGDG](https://arxiv.org/abs/2407.17404) |
| 关卡与可玩内容 | 在固定或部分生成规则下产生地图、谜题、地牢、弹幕或教程关 | [MarioGAN](https://doi.org/10.1145/3205455.3205517)、[TOAD-GAN](https://arxiv.org/abs/2008.01531)、[PCGRL](https://doi.org/10.1609/aiide.v16i1.7416)、[MarioGPT](https://arxiv.org/abs/2302.05981) |
| 学习式交互世界 | 可实时控制的动作条件像素、几何和/或显式状态 | [Genie](https://proceedings.mlr.press/v235/bruce24a.html)、[GameNGen](https://arxiv.org/abs/2408.14837)、[GameFactory](https://arxiv.org/abs/2501.08325)、[StatePlay](https://arxiv.org/abs/2607.26754) |

第四层有意单独整理：生成可控制的视频世界，不等于在传统引擎中创作显式代码、规则和资产。

## Benchmark 快速入口

| Benchmark | 生成任务 | 评测方式 | 截止核验日可用性 |
| --- | --- | --- | --- |
| [V-GameGym](https://arxiv.org/abs/2509.20136) | 自然语言 → 可运行 Pygame | 代码、截图和 gameplay 视频证据 | **Open** |
| [GameDevBench](https://arxiv.org/abs/2602.11103) | 修改真实 Godot 仓库 | 确定性运行时测试 | **Open** |
| [GameCraft-Bench](https://arxiv.org/abs/2606.17861) | Brief → 完整 Godot 游戏 | 回放、build gate、机制/内容/视觉 rubric | **Open；环境依赖重** |
| [GameEngineBench](https://arxiv.org/abs/2607.03525) | 在 UE5 仓库实现原生 C++ 任务 | 隐藏 Unreal 行为测试 | **Open；环境依赖重** |
| [PlayGen-20 / AutoUE](https://arxiv.org/abs/2603.07106) | Brief → 完整 UE5 3D 游戏 | 场景、玩法、视觉、图/模块和运行时检查 | **Open；环境依赖重** |
| [PCG Benchmark](https://arxiv.org/abs/2503.21474) | 跨多种领域生成关卡/内容 | 质量、多样性与可控性 | **Open** |
| [OpenGame-Bench](https://arxiv.org/abs/2604.18394) | Prompt → 浏览器游戏 | 构建健康、视觉可用性、需求对齐 | **Partial** |
| [PlaytestArena](https://arxiv.org/abs/2605.28258) | Prompt → 浏览器游戏并由 GUI 试玩 | 可观察 rubric 通过率 | **Partial** |
| [GameXpert-Bench](https://arxiv.org/abs/2608.21833) | 生成、修复和优化游戏 | 分生命周期 rubric 与测试 | **Closed；仅有发布脚手架** |

## 发展脉络

- **2008–2014——自动游戏设计：** Ludi、ANGELINA、Game-o-Matic、Mechanic Miner 与形式化机制生成，奠定了自动生成规则和完整游戏的方向。
- **2016–2021——PCGML 与学习式关卡：** VGLC、LSTM 关卡生成、MarioGAN、DoomGAN、TOAD-GAN、PCGRL 与可控 PCGRL，使数据驱动内容生成逐步可复现。
- **2023–2025——语言模型生成游戏：** MarioGPT、GameGPT、GAVEL、语法约束规则生成、ScriptDoctor、Cardiverse、GameFactory 及新一代 text-to-game 系统，把生成对象从地图扩展到代码和机制。
- **2026——引擎原生 agent 与有状态世界：** Godot/Unreal/浏览器 benchmark、AutoUE、长时世界模型、显式机制/状态生成和自动试玩修复闭环成为重点。

## 明确排除：玩游戏

以下工作是重要的 Game AI 研究，但不属于只看生成的资料库：

- DQN、AlphaGo、AlphaZero、MuZero、Agent57、AlphaStar、OpenAI Five、Voyager、SIMA 等玩游戏智能体；
- BALROG、VideoGameBench、MineRL/BASALT、MineDojo agent 任务、ALE、Procgen、NLE、Crafter 等游玩/控制 benchmark；
- Dreamer、SimPLe、IRIS 和 **DIAMOND**，因为其核心结果是策略学习或游戏回报，而不是供人控制的生成式游戏世界；
- GameWAM 等以任务成功率为主要指标的动作生成策略；
- 单独的 NPC AI、玩家建模、匹配、游戏分析，以及只生成资产的工作。

自动玩家仍可作为生成设计的**评测器**出现；如果 RL 策略本身就是**内容生成器**，例如 PCGRL，也会收录。

## 可用性标签

| 标签 | 含义 |
| --- | --- |
| **Open** | 官方核心代码/数据/任务以及有意义的评测或可运行权重已经公开 |
| **Partial** | 有可用官方工件，但仍缺少关键任务集、评分器、训练栈、数据、模型或输出集合 |
| **Closed / Paper-only** | 截止核验日期，未核验到可复现的官方实现或 benchmark 包 |

这些标签描述的是工件可用性，不代表许可、成本、确定性复现程度或研究质量。

## 仓库结构

```text
.
├── README.md / README.zh-CN.md
├── SCOPE.md
├── docs/
│   ├── en/{end-to-end,pcg,interactive-worlds}.md
│   └── zh-CN/{end-to-end,pcg,interactive-worlds}.md
├── research/          # 详细的一手来源核验底稿
└── .github/           # 限定范围的资源推荐模板
```

## 参与贡献

欢迎补充和纠错。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。每个提议都必须说明系统**生成什么**、提供一手来源链接、写明评测与工件可用性，并附语义对应的中英文说明。

## 许可证

本索引使用 [MIT License](LICENSE)。所链接论文、代码、数据集、游戏、模型及其他工件仍遵循各自的原始许可证。
