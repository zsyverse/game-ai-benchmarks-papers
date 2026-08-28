# 程序化游戏生成与自动游戏设计

[返回首页](../../README.zh-CN.md) · [English](../en/pcg.md) · [端到端生成](end-to-end.md) · [交互世界](interactive-worlds.md) · [收录范围](../../SCOPE.md)

> 检索截止：**2026-08-29（Asia/Shanghai）**。本索引只收录生成游戏、可执行规则或机制、关卡、游戏世界组件的工作；主要任务只是游玩现有游戏的论文不在范围内。

自动游玩、自博弈、搜索和学习型代理只有在**评价生成设计**时才会出现。强化学习只有在策略**负责生成或编辑内容**时才会出现，例如 PCGRL；纯游戏游玩 RL benchmark 和代理排行榜均排除。**Open** 表示核心官方产物公开；**Partial** 表示有可用产物，但完整历史系统或实验流水线缺失；**Paper-only** 表示未核实到官方可运行版本。

## 1. 完整游戏、规则与机制（15）

| 来源编号 | 年份 | 论文/资源 | 范围 | 生成内容 / 方法 | 评测 | 产物/状态 |
| ---: | :---: | --- | --- | --- | --- | --- |
| 1 | 2008 | [An Experiment in Automatic Game Design](https://doi.org/10.1109/CIG.2008.5035629) | `full-game` | 进化包含规则和棋盘配置的完整双人小游戏；学习型代理只负责评价设计。 | 奖励可学习但不简单、能区分玩家水平的游戏，并检查进化所得游戏是否可玩。 | **Paper-only** — 未核实到官方历史实现或数据版本。 |
| 2 | 2008 | [Automatic Generation and Evaluation of Recombination Games](https://eprints.qut.edu.au/17025/)（[论文 PDF](https://eprints.qut.edu.au/17025/1/Cameron_Browne_Thesis.pdf)、[后继 Ludii](https://ludii.games/)） | `rules` | Ludi 通过重组 ludeme 进化抽象棋类规则，并用自动自博弈过滤候选规则集。 | 衡量可玩性、平衡性、深度和决断性；该过程产出了包括 Yavalath 在内的真人可玩游戏。 | **Partial** — 论文和后继生态公开，但原始 Ludi 实验不是开箱即用的 benchmark。 |
| 3 | 2011 | [Multi-faceted Evolution of Simple Arcade Games](https://doi.org/10.1109/CIG.2011.6032019) | `full-game` | ANGELINA 协同进化街机游戏的机制、规则和关卡布局，并以自动游玩辅助评价候选。 | 检查功能性游玩并把生成游戏作为设计作品分析，而非采用固定排行榜。 | **Paper-only** — 未核实到该版 ANGELINA 的完整官方发布。 |
| 4 | 2012 | [The Micro-Rhetorics of Game-o-Matic](https://doi.org/10.1145/2282338.2282347) | `full-game` | 把用户给出的概念关系图映射为机制模板、实体、规则和呈现选择，生成可玩小游戏。 | 通过细读和示例判断交互能否表达目标关系，没有统一自动分数。 | **Partial** — 项目证据公开，但未核实到持续维护的端到端生成器/评测器。 |
| 5 | 2013 | [Mechanic Miner: Reflection-Driven Game Mechanic Discovery and Level Design](https://doi.org/10.1007/978-3-642-37192-9_29) | `rules` | 反思模拟游玩轨迹以发现规则变化，再构造能显露新机制效果的关卡。 | 用自动游玩区分候选机制诱发的行为，并分析生成示例。 | **Paper-only** — 未核实到官方可运行版本。 |
| 6 | 2014 | [Automatic Game Design via Mechanic Generation](https://doi.org/10.1609/aaai.v28i1.8788) | `rules` | 搜索形式化机制表示并模拟候选，从而合成满足设计师要求的规则。 | 以案例检验生成机制能否执行并实现目标玩法属性。 | **Paper-only** — 未核实到完整官方代码/数据包。 |
| 7 | 2014 | [A Rogue Dream: Automatically Generating Meaningful Content for Games](https://doi.org/10.1609/aiide.v10i3.12745) | `full-game` | ANGELINA 从时事来源提取主题，搜索机制与内容并装配完整可玩的小游戏。 | 将生成游戏作为创意案例进行定性分析，而非可复用 benchmark。 | **Paper-only** — 示例有记录，但完整系统未被公开打包。 |
| 8 | 2018 / 2021 | [Automated Game Design via Conceptual Expansion](https://doi.org/10.1609/aiide.v14i1.13022)（[arXiv](https://arxiv.org/abs/1809.02232)、[期刊版](https://doi.org/10.1109/TG.2021.3060005)） | `full-game` | 学习现有游戏的结构表示，再混合其图结构/组件以创造新游戏。 | 先复原留出的已知游戏作为可量化代理任务，再展示新组合。 | **Paper-only** — 未核实到官方端到端产物包。 |
| 10 | 2022 | [Puck: A Slow and Personal Automated Game Designer](https://doi.org/10.1609/aiide.v18i1.21968) | `full-game` | 通过与设计师持续互动，缓慢探索并积累个性化的完整小游戏设计集合。 | 采用生成游戏及人机关系的反思性长期案例研究。 | **Paper-only** — 系统产物有记录，但未核实到完整复现包。 |
| 11 | 2020 | [Ludii — The Ludemic General Game System](https://doi.org/10.3233/FAIA200120)（[arXiv](https://arxiv.org/abs/1905.05013)、[平台/游戏库](https://ludii.games/)） | `rules` 基础设施 | 提供基于 ludeme 的可执行规则语言、编译器/运行时和游戏语料，供下游规则搜索使用；它本身不是生成器。 | 展示对大量传统策略游戏的覆盖和忠实执行。 | **Partial** — 平台和游戏库可访问，但当前引擎并非完整开源研究栈。 |
| 12 | 2024 | [GAVEL: Generating Games via Evolution and Language Models](https://arxiv.org/abs/2407.09388) | `full-game` | 结合 fill-in-the-middle CodeLlama 与 MAP-Elites，生成可执行的 Ludii 双人棋类游戏。 | 报告 QD 分数、可玩及高适应度档案格、语义新颖性和专家定性评价。 | **Open** — 作者公开了[代码/数据](https://github.com/gdrtodd/gavel)和[可玩游戏库](https://ludii.games/library.php)。 |
| 13 | 2024 | [Grammar-Based Game Description Generation Using Large Language Models](https://doi.org/10.1109/TG.2024.3520214)（[arXiv](https://arxiv.org/abs/2407.17404)） | `rules` | 从游戏描述规范推导最小语法，再用解析器给出的合法前缀和候选符号迭代修复 LLM 输出。 | 与直接使用 LLM 的基线比较语法有效率和生成成功率。 | **Open** — 作者公开了[实现与评测流程](https://github.com/tsunehiko/ggdg)。 |
| 14 | 2024 | [Game Generation via Large Language Models](https://arxiv.org/abs/2404.08706)（[IEEE 记录](https://doi.org/10.1109/COG60054.2024.10645597)） | `full-game` | 在不同文档和上下文示例条件下，提示 LLM 联合生成 VGDL 规则与关卡。 | 检查不同提示条件下的编译/执行和可玩结构。 | **Paper-only** — 未核实到官方任务集、生成器和评测器整包。 |
| 15 | 2025 | [ScriptDoctor: Automatic Generation of PuzzleScript Games via LLMs and Tree Search](https://arxiv.org/abs/2506.06524)（[IEEE 记录](https://doi.org/10.1109/COG64752.2025.11114269)） | `full-game` | 使用编译错误、控制流反馈和有预算上限的 BFS 游玩测试，迭代修复完整 PuzzleScript 规则文件与关卡。 | 衡量编译率、求解成功率，以及所有关卡均可解且解长超过十步的更严格比例。 | **Partial** — [PuzzleScript 运行时](https://github.com/increpare/PuzzleScript)开放，但未核实到 ScriptDoctor 代码和完整语料。 |
| 16 | 2025 | [Cardiverse: Harnessing LLMs for Novel Card Game Prototyping](https://aclanthology.org/2025.emnlp-main.1511/)（[arXiv](https://arxiv.org/abs/2502.07128)） | `full-game` | 通过图索引变异机制，生成可执行卡牌游戏代码，并对照对局记录检查行为。 | 评测机制相似度/新颖性、用户评分、pass@3、执行一致性及启发式锦标赛。 | **Open** — 官方[代码、示例、数据与评测命令](https://github.com/danruili/Cardiverse)均公开。 |

## 2. 关卡生成、数据集与评测环境（15）

| 来源编号 | 年份 | 论文/资源 | 范围 | 生成内容 / 方法 | 评测 | 产物/状态 |
| ---: | :---: | --- | --- | --- | --- | --- |
| 17 | 2025 | [The Procedural Content Generation Benchmark](https://arxiv.org/abs/2503.21474)（[ACM 记录](https://doi.org/10.1145/3723498.3723794)） | `levels` benchmark | 为迷宫、平台关、地牢、谜题、弹幕及一个街机规则任务统一 Gym 风格生成接口。 | 提供统一的质量、成对阈值多样性和目标满足可控性指标，以及逐样本明细向量。 | **Open** — [框架](https://github.com/amidos2006/pcg_benchmark)和[基线实验](https://github.com/amidos2006/benchmark_experiments)均公开。 |
| 18 | 2016 | [VGLC: The Video Game Level Corpus](https://arxiv.org/abs/1606.07487) | `levels` 数据集 | 把多款游戏的经典人工瓷砖关卡规范化为机器可读文本；它本身不生成关卡。 | 不规定统一指标，因此下游可玩性、相似性、新颖性和多样性分数不能自动横向比较。 | **Open 数据集 / Partial benchmark** — [官方语料库](https://github.com/TheVGLC/TheVGLC)公开，但评测因论文而异。 |
| 19 | 2011 | [The 2010 Mario AI Championship: Level Generation Track](https://doi.org/10.1109/TCIAIG.2011.2166267) | `levels` 竞赛 | 定义在线生成赛道，由算法创建 Mario 风格关卡，并可选地根据玩家/游玩信息进行条件生成。 | 采用竞赛协议、玩家偏好/体验和关卡特征统计。 | **Partial** — 协议与结果有记录，但原始完整服务和参赛提交未被维护为开箱即用版本。 |
| 20 | 2019 | [General Video Game AI: A Multitrack Framework for Evaluating Agents, Games, and Content Generation Algorithms](https://doi.org/10.1109/TG.2019.2901021) | `levels` 框架 | 用统一 VGDL 运行时分离多款游戏的规则、关卡描述、生成器和自动评测器。 | 为生成赛道定义有效性/可玩性检查与竞赛协议；本文不收录其中的玩游戏代理赛道。 | **Open** — [引擎、游戏与关卡生成接口](https://github.com/GAIGResearch/GVGAI)持续公开维护。 |
| 21 | 2018 | [Evolving Mario Levels in the Latent Space of a Deep Convolutional GAN](https://doi.org/10.1145/3205455.3205517) | `levels` | 用 DCGAN 学习 Mario 关卡潜空间，再以 CMA-ES 和新颖性/质量多样性搜索优化潜变量。 | 衡量可玩性、目标属性及潜空间多样性/覆盖度。 | **Open** — [实验代码](https://github.com/icaros-usc/MarioGAN-LSI)和 [VGLC 训练语料](https://github.com/TheVGLC/TheVGLC)均公开。 |
| 22 | 2020 | [TOAD-GAN: Coherent Style Level Generation from a Single Example](https://doi.org/10.1609/aiide.v16i1.7401)（[arXiv](https://arxiv.org/abs/2008.01531)） | `levels` | 仅用一个样例关卡训练多尺度 GAN，生成风格与空间尺度相符的连贯瓷砖地图。 | 在多种游戏中评估瓷砖模式/风格相似性、多样性和领域特定可玩性。 | **Open** — 官方[训练/生成代码与示例](https://github.com/Mawiszus/TOAD-GAN)公开。 |
| 23 | 2020 | [PCGRL: Procedural Content Generation via Reinforcement Learning](https://doi.org/10.1609/aiide.v16i1.7416) | `levels` | 把 RL 策略训练为**内容生成器**，让其在多个领域以 narrow、turtle 或 wide 表示编辑瓷砖。 | 比较训练效率、内容有效性/质量、多样性及不同表示下的行为。 | **Open** — [环境、表示、指标与训练代码](https://github.com/amidos2006/gym-pcgrl)均公开。 |
| 24 | 2021 | [Learning Controllable Content Generators](https://arxiv.org/abs/2105.02993)（[IEEE 记录](https://doi.org/10.1109/COG52621.2021.9619159)） | `levels` | 用设计师指定的属性目标调节 PCGRL 的观测和奖励，生成多样且目标可控的瓷砖关卡。 | 相对无目标条件的生成器，衡量目标误差/覆盖度、多样性和质量。 | **Partial** — 工作建立在开放 PCGRL 上，但未核实到单独打包的官方实验版本。 |
| 25 | 2018 | [Talakat: Bullet Hell Generation through Constrained MAP-Elites](https://arxiv.org/abs/1806.04718) | `levels` | 结合 spawner 语言与约束 MAP-Elites，生成可执行且行为多样的弹幕攻击模式。 | 评估可玩/存活约束、档案覆盖度及行为描述子上的多样性。 | **Open** — 作者公开了[领域运行时与生成代码](https://github.com/amidos2006/Talakat)。 |
| 26 | 2018 | [Generating Levels That Teach Mechanics](https://doi.org/10.1145/3235765.3235820)（[arXiv](https://arxiv.org/abs/1807.06734)） | `levels` | 进化完整 A* 代理能通过、但缺失目标动作或感知的代理不能通过的 Mario 教程关。 | 用差异可解性判断成功是否必须依赖目标机制；代理只负责评价。 | **Paper-only** — 未核实到官方维护的实现。 |
| 27 | 2023 | [Level Generation Through Large Language Models](https://doi.org/10.1145/3582437.3587211)（[arXiv](https://arxiv.org/abs/2302.05817)） | `levels` | 在 Sokoban 网格字符串上训练自回归语言模型，并改变数据量及初步属性控制设置。 | 衡量功能性/可解生成率、数据规模效应和初步可控性。 | **Paper-only** — 未核实到完整官方训练/评测包。 |
| 28 | 2023 | [MarioGPT: Open-Ended Text2Level Generation through Large Language Models](https://arxiv.org/abs/2302.05981) | `levels` | 用冻结文本编码器和判别器/分类器引导 GPT-2 关卡模型，把提示映射为 Mario 瓷砖布局。 | 评估提示—属性对齐、新颖性/多样性及可玩性/可解性。 | **Open** — 作者公开了[训练/推理代码与模型产物](https://github.com/shyamsn97/mario-gpt)。 |
| 29 | 2016 | [Super Mario as a String: Platformer Level Generation Via LSTMs](https://doi.org/10.26503/dl.v2016i1.752)（[arXiv](https://arxiv.org/abs/1603.00930)） | `levels` | 将二维 Mario 地图序列化为字符序列，在多种表示下训练 LSTM 并采样新关卡。 | 在从人工关卡提取的特征空间中比较生成结果和不同表示。 | **Paper-only** — 未核实到作者发布的可运行实现。 |
| 30 | 2018 | [DOOM Level Generation Using Generative Adversarial Networks](https://doi.org/10.1109/GEM.2018.8516539)（[arXiv](https://arxiv.org/abs/1804.09154)） | `levels` | 在人工地图上训练图像 GAN 和拓扑条件 GAN，生成包含空间、高度、墙体与物件的 DOOM 布局。 | 衡量与人工关卡的拓扑/分布相似性，并定性检查输出。 | **Open** — 官方[预处理、模型、生成数据与实验代码](https://github.com/edoardogiacomello/DoomGAN)均公开。 |
| 31 | 2017 / 2021 | [WaveFunctionCollapse Is Constraint Solving in the Wild](https://doi.org/10.1145/3102071.3110566)（[期刊分析](https://doi.org/10.1109/TG.2021.3076368)） | `levels` | 从样例学习局部瓷砖邻接模式，并传播兼容性约束以生成地图/图像。 | 分析约束行为与失败；局部一致并不保证全局可玩或可解。 | **Open/Partial** — [参考实现](https://github.com/mxgmn/WaveFunctionCollapse)公开，但论文未定义固定玩法 benchmark。 |

## 3. 仅组件生成（2）

这些产物是有用的游戏世界内容，但不会定义新的可执行规则或完整游戏。

| 来源编号 | 年份 | 论文/资源 | 范围 | 生成内容 / 方法 | 评测 | 产物/状态 |
| ---: | :---: | --- | --- | --- | --- | --- |
| 32 | 2021 | [World-GAN: A Generative Model for Minecraft Worlds](https://doi.org/10.1109/COG52621.2021.9619133) | `components` | 把单样例多尺度 GAN 扩展到三维 Minecraft 体素结构和世界区域；不生成玩法规则。 | 评估结构连贯性、多样性及与来源风格的定性相似度。 | **Open** — 官方[代码与示例](https://github.com/Mawiszus/World-GAN)公开。 |
| 33 | 2020 | [The AI Settlement Generation Challenge in Minecraft](https://doi.org/10.1007/s13218-020-00635-0) | `components` benchmark | 评测在未见 Minecraft 地图中规划适应地形的道路、建筑和聚落的生成器。 | 专家按适应性、功能性、叙事/美学等质量评价，具体 rubric 逐年变化。 | **Open/Partial** — [接口与竞赛材料](https://github.com/avdstaaij/gdmc_http_interface)公开，但评审部分依赖人工且逐年变化。 |

## 4. 综述与分类法（3）

| 来源编号 | 年份 | 论文/资源 | 范围 | 生成内容 / 方法 | 评测 | 产物/状态 |
| ---: | :---: | --- | --- | --- | --- | --- |
| 9 | 2018 | [Orchestrating Game Generation](https://doi.org/10.1109/TG.2018.2870876) | `survey` / 架构 | 提出让规则、关卡、视觉、音频等生成器交换约束与反馈的模式和接口；它本身不是生成器套件。 | 综合已有系统和设计场景，而不定义实证排行榜。 | **Paper-only by design** — 这是概念性的生成编排框架。 |
| 34 | 2011 | [Search-Based Procedural Content Generation: A Taxonomy and Survey](https://doi.org/10.1109/TCIAIG.2011.2148116) | `survey` | 按表示、评价、编码和在线/离线维度，梳理关卡、规则、地图、谜题等搜索式生成。 | 提供分类法与文献综合，而非实证排行榜。 | **Paper-only by design** — 这是综述而非产物发布。 |
| 35 | 2018 | [Procedural Content Generation via Machine Learning](https://doi.org/10.1109/TG.2018.2846639)（[作者稿](https://arxiv.org/abs/1702.00539)） | `survey` | 从训练数据来源、学习表示、生成策略及输入输出域关系等方面定义 PCGML。 | 综合相关文献，并提出数据稀缺、可控性、评价和泛化等研究议程。 | **Paper-only by design** — 这是分类/综述而非单一 benchmark 实现。 |

## 明确排除

- 排除 ALE、Procgen、CoinRun、NetHack Learning Environment、MineRL/BASALT、Crafter、BabyAI、GVGAI 玩游戏赛道等纯游玩 benchmark 和代理控制任务。
- 不会仅因 MCTS、RL、搜索或自博弈论文游玩/评价固定游戏就将其收录；只有当它们评价生成设计，或直接生成/优化内容时才会出现在上表。
- 单独的纹理、精灵、音乐、对话、故事、视频及下一帧世界模型不属于完整游戏生成，最多归为组件生成。
