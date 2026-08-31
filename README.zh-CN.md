# 游戏生成 Benchmark 与论文

[English](README.md) · 简体中文

> 经过一手来源核验的双语资料库：只收录**生成游戏的 AI**，不收录玩游戏的 AI。

本仓库覆盖生成完整游戏、可执行规则与机制、游戏代码与引擎工程、关卡与可玩内容，以及动作条件交互世界的研究。目前包含 **198 条详细分类记录**（允许有意义的跨分类重复），以及 **500 多个论文与官方工件链接**。

最近一次完整核验：**2026-09-01**。

## 按生成目标浏览

| 专题 | 中文 | English | 覆盖范围 |
| --- | --- | --- | --- |
| 端到端游戏与代码 | [50 个 benchmark 与论文](docs/zh-CN/end-to-end.md) | [50 benchmarks and papers](docs/en/end-to-end.md) | 提示词到游戏、引擎/工程/代码生成、游戏开发 agent、验证、修复与共创 |
| 自动游戏设计与 PCG | [115 篇论文与资源](docs/zh-CN/pcg.md) | [115 papers and resources](docs/en/pcg.md) | 完整游戏、规则/机制、关卡生成、数据集、PCG benchmark 与奠基综述 |
| 可交互游戏世界 | [33 篇论文与资源](docs/zh-CN/interactive-worlds.md) | [33 papers and resources](docs/en/interactive-worlds.md) | 动作条件生成器、学习式渲染器/状态引擎、生成数据集/benchmark 与领域边界材料 |
| 详细证据 | [一手来源核验底稿](research/README.md) | [Research notes](research/README.md) | 任务定义、评测协议、工件可用性、边界判断和一手来源依据 |

精确的收录与排除规则见 [SCOPE.md](SCOPE.md)。

## 条目如何分层

| 条目角色 | 含义 |
| --- | --- |
| 核心生成器 | 直接输出可运行游戏、可执行规则/机制、游戏代码/工程修改、可玩内容，或供人控制的生成式世界 |
| 生成专用资源 | 专门评测或支撑上述生成产物的 benchmark、数据集、语料库、验证器、修复环节或评分器 |
| 边界或领域框架 | 明确放在独立分区中的基础设施、混合框架、综述、分类或观点论文；不把它们描述成生成器 |

这种分层让资料库保持广度，同时不会虚增真正游戏生成系统的数量。

## 什么算“生成游戏”？

| 层级 | 输出 | 代表工作 |
| --- | --- | --- |
| 完整游戏 | 包含玩法、规则、场景、代码和资产的可运行工程 | [AutoUE](https://arxiv.org/abs/2603.07106)、[OpenGame](https://arxiv.org/abs/2604.18394)、[STORY2GAME](https://arxiv.org/abs/2505.03547)、[GamED.AI](https://arxiv.org/abs/2604.23947) |
| 规则与机制 | 定义新玩法的可执行游戏描述、程序或参数配置 | [GAVEL](https://arxiv.org/abs/2407.09388)、[GGDG](https://arxiv.org/abs/2407.17404)、[RLGDG](https://arxiv.org/abs/2503.15783)、[Mortar](https://arxiv.org/abs/2601.00105) |
| 关卡与可玩内容 | 直接决定玩法的地图、谜题、地牢、任务、谱面或其他内容 | [MarioGPT](https://arxiv.org/abs/2302.05981)、[PCGRL+](https://arxiv.org/abs/2408.12525)、[Word2Minecraft](https://arxiv.org/abs/2503.16536)、[Multiverse](https://arxiv.org/abs/2603.26782) |
| 学习式交互世界 | 可实时控制的动作条件像素、几何和/或显式状态 | [GenieRedux](https://arxiv.org/abs/2504.02515)、[GameFactory](https://arxiv.org/abs/2501.08325)、[Solaris](https://arxiv.org/abs/2602.22208)、[MASS](https://arxiv.org/abs/2608.06257) |

第四层有意单独整理：生成可控制的视频世界，不等于在传统引擎中创作显式代码、规则和资产。

## Benchmark 快速入口

| Benchmark | 生成任务 | 评测方式 | 截止核验日可用性 |
| --- | --- | --- | --- |
| [V-GameGym](https://arxiv.org/abs/2509.20136) | 自然语言 → 可运行 Pygame | 代码、截图和 gameplay 视频证据 | **Open** |
| [WebGameBench](https://arxiv.org/abs/2605.17637) | Specification → 已部署浏览器游戏 | 与人工实际试玩复核对齐的运行时可用性 | **Closed** |
| [GameDevBench](https://arxiv.org/abs/2602.11103) | 修改真实 Godot 仓库 | 确定性运行时测试 | **Open** |
| [GameCraft-Bench](https://arxiv.org/abs/2606.17861) | Brief → 完整 Godot 游戏 | 回放、build gate、机制/内容/视觉 rubric | **Open；环境依赖重** |
| [GameEngineBench](https://arxiv.org/abs/2607.03525) | 在 UE5 仓库实现原生 C++ 任务 | 隐藏 Unreal 行为测试 | **Closed；截止核验日官方仓库不可用** |
| [PlayGen-20 / AutoUE](https://arxiv.org/abs/2603.07106) | Brief → 完整 UE5 3D 游戏 | 场景、玩法、视觉、图/模块和运行时检查 | **Open；环境依赖重** |
| [PCG Benchmark](https://arxiv.org/abs/2503.21474) | 跨多种领域生成关卡/内容 | 质量、多样性与可控性 | **Open** |
| [ChatGPT4PCG](https://arxiv.org/abs/2303.15662) | Prompt/program → 稳定的 Science Birds 关卡 | 稳定性、字符相似度与多样性 | **Open** |
| [OpenGame-Bench](https://arxiv.org/abs/2604.18394) | Prompt → 浏览器游戏 | 构建健康、视觉可用性、需求对齐 | **Partial** |
| [PlaytestArena](https://arxiv.org/abs/2605.28258) | Prompt → 浏览器游戏并由 GUI 试玩 | 可观察 rubric 通过率 | **Partial** |
| [GameXpert-Bench](https://arxiv.org/abs/2608.21833) | 生成、修复和优化游戏 | 分生命周期 rubric 与测试 | **Closed；仅有发布脚手架** |
| [WildWorld / WildBench](https://arxiv.org/abs/2603.23497) | 生成动作/状态对齐的 ARPG rollout | Action Following 与 State Alignment | **Partial** |
| [PlayWorld](https://arxiv.org/abs/2608.13552) | 生成世界 → 长时 agent 探针 | 几何、交互，以及可见/隐藏世界演化 | **Open；依赖 API** |

## 发展脉络

- **2000–2015——自动游戏设计与早期 PCG：** EGGG、Ludi、ANGELINA、Game-o-Matic、早期平台关/赛道/RTS/谜题生成、任务—空间语法、Launchpad、Polymorph、Tanagra、Sentient Sketchbook、n-gram/Markov 地图、Sampling Hyrule、生成器生成系统，以及首批统一 Mario/指标评价，奠定了自动生成规则、关卡和完整游戏的方向。
- **2016–2022——PCGML、学习式关卡与元生成：** VGLC、约束/域迁移/多层 Markov、视频到关卡与 LSTM、学习式构造原语、Lode Runner autoencoder、MarioGAN、DoomGAN、TOAD-GAN、PCGRL、共享潜空间、Generative Playing Networks、mutation models、Marahel 元生成、AIBIRDS 及其生成语料，共同扩展了生成方法与评价体系。
- **2023–2025——语言模型、扩散与学习式世界：** MarioGPT、无条件 Mario 扩散、Promptable Game Models、Word2World、GAVEL、RLGDG、STORY2GAME、ScriptDoctor、Cardiverse 和 GameFactory，把生成对象从地图扩展到代码、机制与可控视频。
- **2026——引擎原生 agent 与有状态世界：** Godot/Unreal/浏览器 benchmark、AutoUE、Mortar、MAGIC、长时/多人世界模型、显式状态生成和自动试玩修复闭环成为重点。

## 明确排除：玩游戏

以下工作是重要的 Game AI 研究，但不属于只看生成的资料库：

- DQN、AlphaGo、AlphaZero、MuZero、Agent57、AlphaStar、OpenAI Five、Voyager、SIMA 等玩游戏智能体；
- BALROG、VideoGameBench、MineRL/BASALT、MineDojo agent 任务、ALE、Procgen、NLE、Crafter 等游玩/控制 benchmark；
- Dreamer、SimPLe、IRIS 和 **DIAMOND**，因为其核心结果是策略学习或游戏回报，而不是供人控制的生成式游戏世界；
- GameWAM、ActSWM 等以任务成功率为主要指标的动作生成或规划策略；
- METAGAME/METAGAMER，因为随机棋类生成只是通用玩游戏研究的测试域，而不是被评价的研究产物；
- 单独的 NPC AI、玩家建模、匹配、游戏分析，以及只生成资产的工作。

自动玩家仍可作为生成设计的**评测器**出现；如果 RL 策略本身就是**内容生成器**，例如 PCGRL，也会收录。

## 可用性标签

| 标签 | 含义 |
| --- | --- |
| **Open** | 官方核心代码/数据/任务以及有意义的评测或可运行权重已经公开 |
| **Partial** | 有可用官方工件，但仍缺少关键任务集、评分器、训练栈、数据、模型或输出集合 |
| **Closed** | 截止核验日期，未核验到可复现的官方实现或 benchmark 包 |
| **Paper-only by design** | 框架、立场或 taxonomy 论文有意不提出生成器或可运行工件 |

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
├── scripts/           # 双语、计数与链接校验
└── .github/           # Issue 模板与校验 workflow
```

## 参与贡献

欢迎补充和纠错。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。每个提议都必须说明系统**生成什么**、提供一手来源链接、写明评测与工件可用性，并附语义对应的中英文说明。

## 许可证

本索引使用 [MIT License](LICENSE)。所链接论文、代码、数据集、游戏、模型及其他工件仍遵循各自的原始许可证。
