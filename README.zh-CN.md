# 游戏生成方法与 Benchmark

[English](README.md) · [Web UI](https://zsyverse.github.io/game-ai-benchmarks-papers/) · [全部论文速览](docs/zh-CN/paper-list.md) · [研究导读](docs/zh-CN/research-guide.md) · [参与贡献](CONTRIBUTING.md)

[![Validate bibliography](https://github.com/zsyverse/game-ai-benchmarks-papers/actions/workflows/validate.yml/badge.svg)](https://github.com/zsyverse/game-ai-benchmarks-papers/actions/workflows/validate.yml) [![GitHub stars](https://img.shields.io/github/stars/zsyverse/game-ai-benchmarks-papers?style=flat)](https://github.com/zsyverse/game-ai-benchmarks-papers/stargazers) [![License](https://img.shields.io/github/license/zsyverse/game-ai-benchmarks-papers?style=flat)](https://github.com/zsyverse/game-ai-benchmarks-papers/blob/main/LICENSE)

一份关注**生成游戏，而不是玩游戏**的双语论文清单：覆盖可运行游戏与代码、可玩内容，以及玩家可控制的生成式世界。

三个分类，共 **203 条 canonical 记录**。一篇论文只计一次，实质不同的后续论文单独收录。

> 最近一次完整核验：**2026-09-04**。定向增补与复核：**2026-09-05 / 2026-09-08**，不代表全库重新审计或实验复现。

## 目录

- [浏览索引](#浏览索引) · [全部论文速览](docs/zh-CN/paper-list.md)
- [从这些论文读起](#从这些论文读起)
- [快速查找论文](#快速查找论文)
- [准入测试](#准入测试) · [工件标签](#工件标签)
- [调研综述与覆盖增补](#调研综述与覆盖增补)
- [参与贡献](#参与贡献) · [许可证](#许可证)

## 浏览索引

| 分类 | 条目数 | 可以找到什么 |
| --- | --- | --- |
| 端到端游戏与代码 | [38 条记录](docs/zh-CN/end-to-end.md) | 10 个 benchmark + 28 个方法：可运行游戏、引擎工程/代码、可执行规则与机制 |
| 自动设计与 PCG | [120 条记录](docs/zh-CN/pcg.md) | 18 个完整游戏/规则方法 + 102 个可玩内容方法与 benchmark：关卡、地图、任务、谜题、谱面 |
| 交互式游戏世界 | [45 条记录](docs/zh-CN/interactive-worlds.md) | 41 个方法 + 4 个 benchmark：随玩家输入逐步变化的生成式游戏世界 |

[全部论文速览 — 203 条记录](docs/zh-CN/paper-list.md)：在一页内浏览标题、年份、工件标签和证据链接。进入分类页可查看完整任务说明、评测与限制。

初次了解这个领域，可先读[研究导读](docs/zh-CN/research-guide.md)，了解方法谱系与阅读路线。详细一手证据见[来源底稿](research/README.md)。

## 从这些论文读起

六个不同任务的阅读起点，不是排行榜，也不额外计数。**Paper** 指向论文一手来源，**Code** 指向官方发布；完整性和运行要求以分类表中的详细记录为准。

### 游戏与可执行代码

- **ByteSized32**（2023）· [Paper](https://aclanthology.org/2023.emnlp-main.830/) · [Code](https://github.com/cognitiveailab/BYTESIZED32) — 从任务说明生成完整 Python 文本游戏，分别评测运行有效性与人工可通关性；依赖外部 API。
- **GameCraft-Bench**（2026）· [Paper](https://arxiv.org/abs/2606.17861) · [Code](https://github.com/FreedomIntelligence/gamecraft-bench) — 从需求生成 Godot 游戏，通过构建检查并回放操作轨迹后评分；运行环境要求较重。

### 可玩内容与 PCG

- **PCGRL**（2020）· [Paper](https://doi.org/10.1609/aiide.v16i1.7416) · [Code](https://github.com/amidos2006/gym-pcgrl) — 用强化学习策略编辑地图单元生成关卡；策略是生成器，不是玩家。
- **The Procedural Content Generation Benchmark**（2025）· [Paper](https://arxiv.org/abs/2503.21474) · [Code](https://github.com/amidos2006/pcg_benchmark) · [Experiments](https://github.com/amidos2006/benchmark_experiments) — 以统一接口评测不同 PCG 任务的质量、多样性与可控性。

### 交互世界

- **GameGAN**（2020）· [Paper](https://arxiv.org/abs/2005.12126) · [Code (Partial)](https://github.com/nv-tlabs/GameGAN_code) — 生成按键控制的 Pac-Man/VizDoom 游戏画面，用记忆保持重访布局；未核验到预训练权重与完整 Pac-Man 语料。
- **WorldMark**（2026）· [Paper](https://arxiv.org/abs/2604.21686) · [Code](https://github.com/AlayaLab/WorldMark) — 用统一按键程序评测动作响应、延迟、稳定性、记忆和视觉质量；需另行安装外部生成器。

准备动手实验时，参考[实验起点与固定版本工件证据](research/experiment-entry-points-2026-09-08.md)。这些是选型与配置建议，不是独立复现成功报告。

## 快速查找论文

在仓库根目录使用 Python 3.10+ 本地检索，无需安装依赖或联网。

```bash
python3 scripts/search_index.py Godot --status Open --lang zh-CN
python3 scripts/search_index.py --category interactive-worlds --year 2026 --lang zh-CN
```

[检索使用指南](docs/zh-CN/search.md)说明双语关键词、筛选参数、JSON 导出，以及年份和工件标签的解读方式。

## 准入测试

论文的核心贡献必须是**直接生成方法**或**正式生成 benchmark**，产物为可运行游戏、可执行代码/规则、可玩内容或玩家可控制的生成式世界，而不是智能体的游玩能力。

游玩/NPC 策略、不可玩资产或场景、无逐步玩家控制的视频，以及仅提供支撑组件的研究不符合范围。试玩、搜索、RL 和自博弈只有在直接生成或评测生成工件时才符合范围。

完整排除项及版本合并、去重规则见 [SCOPE.md](SCOPE.md)，具体收录决定见[严格范围审计](research/strict-method-benchmark-scope-audit.md)。

## 工件标签

| 标签 | 含义 |
| --- | --- |
| **Open** | 已核验到官方核心实现和有意义的复现工件 |
| **Partial** | 存在官方发布，但缺少关键组件 |
| **Closed** | 未核验到可运行的官方核心发布 |

可用性不代表论文质量、许可证自由度或复现成功。完整分类表保留评测限制与版本特定说明。

## 调研综述与覆盖增补

- **2026-09-08 — [最新补完](research/completion-review-2026-09-08.md)：** ANGELINA 原始 3D 方法归属、历史 Sokoban 生成、世界域续查与实验起点。
- **2026-09-05–08 — [继续查漏与整合](research/further-research-integration-2026-09-08.md)：** 文本游戏 benchmark、约束谜题、链接数据冒险、主题 3D 生成、重建式可玩内容与交互世界。
- **2026-09-05 — [可靠性复核](research/reliability-audit-2026-09-05.md)：** 论文身份、版本拆分及实验解读纠错；增补覆盖历史规则、音游谱面、NCA、GFlowNet 和地牢/谜题生成。

[覆盖记录与未决线索](research/README.md)保留一手证据和具体缺口，证据不足的候选不计数。本索引并非穷尽式普查，条目数量和结构校验都不代表调研完整性或实验可复现性。

## 参与贡献

欢迎纠错、补充遗漏论文和官方工件链接。[CONTRIBUTING.md](CONTRIBUTING.md) 提供去重要求、可复制的条目模板与校验命令。提交内容须包含论文一手来源、准入依据和语义一致的中英文描述。

格式参考：[五个高 star 清单及本仓库的借鉴方式](research/reference-format-audit-2026-09-08.md)。Star 仅用于选择样式样本，不用于决定论文收录。

## 许可证

本索引采用 [MIT License](LICENSE)。链接论文与工件仍遵循各自原许可证。
