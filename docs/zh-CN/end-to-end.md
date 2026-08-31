# 端到端游戏生成：Benchmark 与论文索引

[返回首页](../../README.zh-CN.md) · [English](../en/end-to-end.md) · [自动设计与 PCG](pcg.md) · [交互世界](interactive-worlds.md) · [收录范围](../../SCOPE.md)

> 检索截止：**2026-08-31（Asia/Shanghai）**。本索引共有 **50 条纯生成记录**，收录把提示词、规格、示例或规则转成可执行游戏、游戏工程、游戏代码、机制/规则，或为生成游戏提供验证/编辑工件的工作。这里**明确排除玩游戏的论文**：如果主要目标是学习游玩策略、提高得分或在现有游戏中获胜，就不纳入。

只生成单个关卡、单类资产，以及仅输出动作条件视频的世界模型均不属于核心范围。只有当 gameplay、self-play 或 GUI agent 被用于评估、修复或平衡生成设计时才会出现。**Open** 表示核心工件已公开；**Partial** 表示只公开部分组件、demo、数据或评测材料；**Closed** 表示截至检索日未核验到可复现的官方发布。

## 1. Benchmark 与评测集（11 条）

| # | 年份 | 论文/资源 | 范围 | 生成内容 | 评测 | 工件/状态 |
| ---: | :---: | --- | --- | --- | --- | --- |
| 1 | 2025 | [V-GameGym（SKYLENAGE-GameCodeGym）](https://arxiv.org/abs/2509.20136) | 从自然语言需求开始生成 Pygame；论文报告 100 个主题簇、2,219 个经核查样本，但当前发布的 JSONL 为 2,218 行。 | 可运行的 Pygame 工程。 | 加权代码、截图和 gameplay 视频 judge 分数。 | **Open** — [项目/排行榜](https://v-gamegym.github.io/)、[代码](https://github.com/alibaba/SKYLENAGE-GameCodeGym)、[数据集](https://huggingface.co/datasets/alibabagroup/SKYLENAGE-GameCodeGym)、[发布规模记录](https://datasets-server.huggingface.co/size?dataset=alibabagroup%2FSKYLENAGE-GameCodeGym)；依赖 judge 模型。 |
| 2 | 2026 | [GameDevBench](https://arxiv.org/abs/2602.11103) | Godot 4.4.1 工程中的 333 个仓库编辑任务。 | 对现有游戏的玩法、UI、图形和动画修改。 | 确定性 Godot 行为测试；pass@1/任务成功率。 | **Open** — [项目](https://waynechi.com/gamedevbench)、[任务、runner 与结果](https://github.com/waynchi/gamedevbench)。 |
| 3 | 2026 | [GameCraft-Bench](https://arxiv.org/abs/2606.17861) | 15 类游戏的 140 个从零生成 brief。 | 完整 Godot 游戏和可回放输入轨迹。 | 回放轨迹后执行 build gate，并按机制、内容、视觉和呈现加权评分。 | **Open，环境依赖重** — [项目/demo](https://tongxuluo.github.io/gamecraft-bench-website/)、[代码、任务与 verifier](https://github.com/FreedomIntelligence/gamecraft-bench)。 |
| 4 | 2026 | [GameEngineBench](https://arxiv.org/abs/2607.03525) | 论文定义了 9 个真实 UE5 仓库中的 110 个原生 C++ 任务。 | 玩法、网络、动画、UI、持久化、XR 和渲染等引擎兼容修改。 | 隐藏 Unreal 运行时行为测试；仅编译通过不算成功。 | **Closed — 截止日官方仓库不可用。** 论文链接的[仓库](https://github.com/Nitrode-Research/GameEngineBench)在 8 月 29 日仅公开 110 个任务包中的 15 个，8 月 31 日通过 Web/API/search 均返回 404；始终未观察到完整结果包。 |
| 5 | 2026 | [GameXpert-Bench](https://arxiv.org/abs/2608.21833) | 生命周期 benchmark：97 个 GameGen、100 个 GameFix，以及 17 条六轮 GameOpt 链。 | 新游戏、缺陷修复及玩法/呈现的迭代优化。 | 完整性/体验/视觉 rubric、回归测试、修复比例和优化分数。 | **截至检索日 Closed** — [官方仓库](https://github.com/Kwen-Chen/GameXpert-Bench)仍是发布脚手架，未含 benchmark 或 evaluator。 |
| 6 | 2026 | [JamBench / JamSet（JAMER）](https://arxiv.org/abs/2606.19830) | 8,133 个已验证 game-jam Godot 工程的项目级语料；其中 benchmark 300 个、训练集 7,833 个。 | 主题驱动工程，以及函数、脚本或完整脚本补全。 | L1/L2/L3a 通过率、结构完整度和确定性行为对齐分数。 | **截至检索日 Closed** — 未核验到可用的官方工件链接。 |
| 7 | 2026 | [VeriGame / GameGen-Verifier](https://arxiv.org/abs/2605.07442) | 覆盖 7 类、100 个游戏规格的 specification compliance 评测。 | 可验证关键点、注入目标状态、短交互探针和判定。 | 对照人工判断计算 Acc@5、Prec@5、Rec@5、F1@5 和 Time@5。 | **Partial** — [实现](https://github.com/NetX-lab/GameGen-Verifier)含 harness 与规格，但不含完整生成游戏证据。 |
| 8 | 2026 | [OpenGame-Bench](https://arxiv.org/abs/2604.18394) | 5 类网页游戏、150 个提示词，从空工作区开始。 | 完整浏览器游戏，每任务评测 3 个随机种子。 | 浏览器执行后的 Build Health、Visual Usability 和逐需求 Intent Alignment。 | **Partial** — [项目](https://yelonlft.github.io/OpenGame-landing-page/)与[框架/demo 源码](https://github.com/leigest519/OpenGame)已公开；任务和 evaluator 尚待发布。 |
| 9 | 2026 | [PlaytestArena](https://arxiv.org/abs/2605.28258) | 8 类、200 个浏览器游戏提示词及可观察 gameplay rubric。 | 生成游戏，以及供修复使用的 GUI agent 试玩判定。 | GUI agent 在不看源码的情况下试玩并计算 rubric 通过率；用 32 个游戏核对人工一致性。 | **Partial** — [项目](https://continual-game-generation.vercel.app/)和[八个 demo 的仓库](https://github.com/RunRiotComeOn/gui-agents-for-continual-game-generation)已公开，完整 arena 未公开。 |
| 10 | 2026 | [PlayGen-20（AutoUE）](https://arxiv.org/abs/2603.07106) | 按难度划分的 20 个 Unreal Engine 3D 游戏自然语言 brief。 | 完整场景、PCG 图、C++ 玩法/交互模块和可运行游戏。 | 场景、玩法和视觉分数，加图/模块/交互检查及运行时证据。 | **Open，环境依赖重** — [代码](https://github.com/Pluto156/AutoUE)、[数据集、demo、资产与结果](https://huggingface.co/datasets/Pluto156/AutoUE_DataSet)；需要 UE5 和 API key。 |
| 11 | 2026 | [WebGameBench](https://arxiv.org/abs/2605.17637) | 111 个冻结规格到浏览器游戏的任务；论文评测 12 个 coding agents 和 14 种评测配置。 | 完成构建、部署并可在浏览器访问的游戏，而不只是源码提交。 | 运行时 Excellent/Usable/Unusable 标签，并用独立人工 gameplay 复核。 | **Closed** — 截至检索日未公开链接官方任务集、运行时 evaluator 或仓库。 |

## 2. 既有核心系统：端到端、游戏代码与完整规则生成（13 篇）

| # | 年份 | 论文/资源 | 范围 | 生成内容 | 评测 | 工件/状态 |
| ---: | :---: | --- | --- | --- | --- | --- |
| 12 | 2024 | [Game Generation via Large Language Models](https://arxiv.org/abs/2404.08706) | 用提示词联合生成完整 VGDL 规则与关卡。 | 同时包含机制和关卡的可执行游戏描述。 | 比较多种上下文设置下的编译与可玩性。 | **Closed** — [IEEE 记录](https://doi.org/10.1109/COG60054.2024.10645597)；未核验到官方实现或固定 benchmark。 |
| 13 | 2024 | [Grammar-Based Game Description Generation Using Large Language Models（GGDG）](https://arxiv.org/abs/2407.17404) | 把自然语言意图转成受语法约束的 Ludii 程序。 | 语法正确、可执行的完整游戏描述。 | 比较不同生成设置的语法有效性、执行情况和游戏质量。 | **Open** — [IEEE DOI](https://doi.org/10.1109/TG.2024.3520214)、[代码与实验脚本](https://github.com/tsunehiko/ggdg)；Ludii 需另行获取。 |
| 14 | 2024 | [GAVEL — Generating Games via Evolution and Language Models](https://arxiv.org/abs/2407.09388) | 对 Ludii 程序变异进行质量多样性搜索。 | 新颖、可执行的桌游规则程序。 | QD 分数、可玩 archive 覆盖、fitness、语义新颖性和专家分析。 | **Open** — [代码、数据与 checkpoint](https://github.com/gdrtodd/gavel)、[可玩的生成游戏](https://ludii.games/library.php)。 |
| 15 | 2023，2025 修订 | [GameGPT — Multi-agent Collaborative Framework for Game Development](https://arxiv.org/abs/2310.08067) | 用角色分工 agents 规划并实现游戏开发需求。 | 计划、任务、代码和游戏开发工件。 | 框架案例研究；没有标准化任务/evaluator 套件。 | **Closed** — 未核验到官方实现。 |
| 16 | 2025 | [ScriptDoctor — Automatic Generation of PuzzleScript Games via LLMs and Tree Search](https://arxiv.org/abs/2506.06524) | 借助编译器、CFG 和求解器反馈迭代生成完整 PuzzleScript。 | 经修复的 PuzzleScript 游戏与关卡。 | 编译、是否存在求解器解，以及严格的多关卡可解性。 | **Closed** — [IEEE DOI](https://doi.org/10.1109/COG64752.2025.11114269)；[上游 PuzzleScript 引擎](https://github.com/increpare/PuzzleScript)已公开，但未核验到 ScriptDoctor/语料发布。 |
| 17 | 2025 | [Cardiverse — Harnessing LLMs for Novel Card Game Prototyping](https://aclanthology.org/2025.emnlp-main.1511/) | 由机制图谱驱动新卡牌游戏原型生成。 | 新机制、可执行游戏代码和可玩原型。 | 机制新颖性/相似度、用户评分、代码 pass@3、执行一致性及辅助锦标赛。 | **Open** — [arXiv](https://arxiv.org/abs/2502.07128)、[代码/数据](https://github.com/danruili/Cardiverse)。 |
| 18 | 2024，2025 修订 | [A Text-to-Game Engine for UGC-Based Role-Playing Games（Zagii）](https://arxiv.org/abs/2407.08195) | 运行时 text-to-RPG 生成。 | 叙事、角色、环境、视听资产和游戏机制。 | 产品使用、可玩性和参与度统计；没有固定公开 baseline。 | **Closed** — [官方产品](https://rpggo.ai/)可访问，但代码、数据和 evaluator 未公开。 |
| 19 | 2026 | [OpenGame — Open Agentic Coding for Games](https://arxiv.org/abs/2604.18394) | 从一个 brief 和空工作区生成多文件 Phaser/TypeScript 工程。 | 带生成式视听资产的完整浏览器游戏。 | OpenGame-Bench 的 Build Health、Visual Usability 和 Intent Alignment。 | **Partial** — [项目](https://yelonlft.github.io/OpenGame-landing-page/)、[框架与 demo 源码](https://github.com/leigest519/OpenGame)；模型、训练数据和完整 evaluator 未发布。 |
| 20 | 2026 | [CreativeGame — Toward Mechanic-Aware Creative Game Generation](https://arxiv.org/abs/2604.19926) | 利用版本谱系与记忆演化机制感知的 HTML5 游戏。 | 新游戏、显式机制增量和版本轨迹。 | 机制实现、结构变化、新颖性、运行时稳健性及论文报告的 LLM 质量评分。 | **仅 Partial demo** — [项目](https://yiweishi-cn.github.io/CreativeEvolutionGame/)、[demo 仓库](https://github.com/yiweishi-cn/CreativeEvolutionGame)、[OpenReview 记录](https://openreview.net/forum?id=VtmBAGCN7o)。 |
| 21 | 2025 | [UniGen — 90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development](https://arxiv.org/abs/2509.26161) | 从自然语言需求自动完成 Unity 规划、编码、装配与调试。 | Unity 蓝图、C# 脚本、绑定组件、场景和可运行 3D 原型。 | 3 个原型的功能完整度交互矩阵及人工开发耗时对比。 | **Partial** — [代码](https://github.com/yxwan123/UniGen)；缺少受评工程、资产、矩阵和 evaluator。 |
| 22 | 2026 | [GUI Agents for Continual Game Generation（Play2Code）](https://arxiv.org/abs/2605.28258) | 最多五轮重复执行浏览器游戏生成、GUI 试玩和代码修复。 | 完整浏览器游戏及连续修复版本。 | PlaytestArena rubric 通过率和 play–code 各轮提升。 | **Partial** — [项目](https://continual-game-generation.vercel.app/)、[八个 demo 的仓库](https://github.com/RunRiotComeOn/gui-agents-for-continual-game-generation)；完整系统/任务/evaluator 未发布。 |
| 23 | 2025 | [Boardwalk — Towards a Framework for Creating Board Games with LLMs](https://arxiv.org/abs/2508.16447) | 把 12 款桌游的匿名化自然语言规则转成 Python 实现。 | 自由格式和兼容 Boardwalk API 的可玩桌游。 | 可玩性、规则遵循、成功率及模型/错误分析。 | **Partial** — [会议 DOI](https://doi.org/10.5753/sbgames.2025.10222)、[Boardwalk API/示例](https://github.com/LabCRAIG/boardwalk)；缺少完整输出/evaluator。 |
| 24 | 2026 | [AutoUE — Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems](https://arxiv.org/abs/2603.07106) | 从自然语言 brief 到 UE5 资产检索、PCG 场景构建、C++ 实现和运行测试。 | 含场景、玩法模块和交互的完整可运行 3D 游戏。 | PlayGen-20 场景/玩法/视觉评分及引擎原生运行检查。 | **Open，环境依赖重** — [代码](https://github.com/Pluto156/AutoUE)、[数据集与生成 demo](https://huggingface.co/datasets/Pluto156/AutoUE_DataSet)。 |

## 3. 其他核心系统：可执行游戏、代码、机制与规则（17 篇）

这些工作与仓库的生成核心直接重合。最后两条覆盖较早但明确的规则生成研究。

| # | 年份 | 论文/资源 | 范围 | 生成内容 | 评测 | 工件/状态 |
| ---: | :---: | --- | --- | --- | --- | --- |
| 25 | 2024 | [Instruction-Driven Game Engines on Large Language Models（IDGE）](https://arxiv.org/abs/2404.00276) / [Poker case study](https://arxiv.org/abs/2410.13441) | 根据自由文本扑克规则和玩家动作预测下一状态，支持自定义变体。 | 执行 gameplay 状态转移，而非生成玩家策略。 | 200 个域内和 50 个域外回合上的整局/状态成功率。 | **Partial** — 论文链接的[仓库](https://github.com/gingasan/idge)只有 `data/train.zip`；有 demo，但没有引擎、训练和评测代码。 |
| 26 | 2024 | [Word2World](https://arxiv.org/abs/2405.06686) | 从故事提示生成叙事、目标、连贯 tile 世界和可玩 2D 游戏。 | 故事约束的地图及可运行 tile-game 体验。 | LLM 连贯性评分、传统 PCG/路径检查、模型比较和流水线消融。 | **Open，依赖 API/操作系统** — [代码与示例](https://github.com/umair-nasir14/Word2World)；文档配置面向 Windows 和 OpenAI API。 |
| 27 | 2024 | [Mechanic Maker — Accessible Game Development Via Symbolic Learning Program Synthesis](https://arxiv.org/abs/2410.01096) | 从用户给出的示例帧序列符号合成可执行机制。 | 能复现所示游戏状态转移的规则。 | 用户研究、Frame Error、任务完成、自由创作分析及动机/可用性问卷。 | **Closed** — 未核验到官方工具源码、研究数据或复现包。 |
| 28 | 2025 | [Grammar and Gameplay-Aligned RL for Game Description Generation（RLGDG）](https://arxiv.org/abs/2503.15783) | 通过 SFT+GRPO 把自然语言描述转成可执行 Ludii 程序。 | 同时对齐语法和玩法概念的完整游戏描述。 | 对比 SFT baseline 的语法有效性、兼容性、功能性和概念保真。 | **Open，环境依赖重** — [训练/数据/评测代码](https://github.com/tsunehiko/rlgdg)；需要 Ludii、Docker 和 GPU 训练。 |
| 29 | 2025 | [STORY2GAME](https://arxiv.org/abs/2505.03547) | 从生成故事构建可跟踪世界状态、动作前置条件/效果、引擎动作代码和按需新动作。 | 可在游玩中扩展动作词表的交互式文字冒险。 | 单动作编译率、整篇故事完全编译率，以及动态动作的语义成功率。 | **Open，依赖 API** — [第一作者公开的代码、提示词、样例与结果仓库](https://github.com/foxanon183/Story2Game)。 |
| 30 | 2025 | [Multi-Agent Game Generation and Evaluation via Audio-Visual Recordings](https://arxiv.org/abs/2508.00632) | 从提示词和多媒体资产库生成多版 JavaScript 游戏，并用录屏选择、迭代。 | 浏览器游戏、动画、音视频录制和成对质量判定。 | AVR-Eval 的损坏/错配识别，以及相对 one-shot 生成的成对胜率。 | **Open，环境依赖重** — [AVR-Agent/AVR-Eval 代码、提示词、任务与实验脚本](https://github.com/SamsungSAILMontreal/AVR-Eval-Agent)；论文资产需按各自许可证另行下载。 |
| 31 | 2025 | [Automated Unity Game Template Generation from GDDs](https://arxiv.org/abs/2509.08847) | 把 Game Design Document 转成结构化规格和 Unity 兼容 C# 模板。 | 核心机制、系统、架构和原型代码。 | 编译、GDD 遵循、最佳实践和模块化；论文报告平均 4.8/5.0。 | **Partial** — [合成 GDD/代码数据](https://huggingface.co/datasets/AmnaHassan/Unity-Engine-CSharp-Code-and-Game-Design-Document-Code-Pairs-Mix-and-Jam)和[真实 GDD 配对数据](https://huggingface.co/datasets/AmnaHassan/Real-Game-Design-Documents-With-AI-Generated-Code-Pairs)已公开；论文链接的[微调模型](https://huggingface.co/AmnaHassan/llama3-unity-gdd-finetuned)匿名访问返回 401，且生成器、Unity package 和 evaluator 代码未公开。 |
| 32 | 2025 | [Real-Time World Crafting](https://arxiv.org/abs/2510.16952) | 把自然语言请求编译成受限 DSL，在运行时配置 ECS。 | 固定 2D 游戏中的新法术和元胞自动机行为。 | Gemini/GPT/Claude 提示策略比较、经验证的 LLM judge、延迟和人工 pilot 分析。 | **Open，依赖 API** — [demo 源码、可玩工件、实验代码与数据](https://github.com/austin-the-drake/real-time-world-crafting-wordplay-demo)。 |
| 33 | 2026 | [Mortar — Evolving Mechanics for Automatic Game Design](https://arxiv.org/abs/2601.00105) | 用 LLM 变异和质量多样性搜索演化机制，再由树搜索组合成完整游戏。 | 演化机制及完整可玩游戏组合。 | 对玩家技能排序的贡献、多样性/可玩性、组件消融和用户研究。 | **Closed** — 未核验到官方实现、机制 archive、生成游戏语料或 evaluator。 |
| 34 | 2026 | [RuleSmith](https://arxiv.org/abs/2602.06232) | 对 CivMini 规则参数执行多智能体自博弈和贝叶斯优化。 | 可直接应用且可解释的平衡规则配置。 | 胜率差异、收敛/样本分配，以及优化参数的 held-out 评测。 | **Open** — [项目](https://adonis-galaxy.github.io/RuleSmith-website/)、[MIT 代码、CivMini 与优化示例](https://github.com/Adonis-galaxy/RuleSmith)。 |
| 35 | 2026 | [Grounding Machine Creativity in Game Design Knowledge Representations](https://arxiv.org/abs/2603.07101) | 将 26 个 goal-playable-pattern 实例直接或经人工 IR 转成 Unity C# 工程。 | 受模式约束的 Unity 代码与工程工件。 | 自动 Unity replay/编译，以及 grounding/工程卫生失败分析；所有受评生成物均未编译成功。 | **Closed** — 未核验到本论文的生成代码、提示词、输出或 replay evaluator；文中引用的 Unity 工具只是上游依赖。 |
| 36 | 2026 | [GamED.AI](https://arxiv.org/abs/2604.23947) | 用层级 agents 和确定性质量门把教师问题转成完整网页教育游戏。 | 覆盖 15 种机制、5 个学科和 3 个教育层级的可玩游戏。 | 200 个问题；内部 FOL validator、schema compliance、token/成本统计和 50 个精选 demo。 | **Open** — [ACL demo 记录](https://doi.org/10.18653/v1/2026.acl-demo.84)、[50 游戏在线库](https://shivena99.github.io/GamED-AI/acl-demo/library/)、[MIT 流水线/源码](https://github.com/ShivenA99/GamED-AI)。 |
| 37 | 2026 | [Distilling Game Code World Model Generation into Lightweight LLMs](https://arxiv.org/abs/2605.24375) | 把自然语言规则转成覆盖 30 款完全/不完全信息游戏的可执行 Python 环境。 | 合法动作、状态转移、观察、奖励和完整 GameCWM。 | 结构/语义验证、执行层规则遵循，以及 SFT 与 SFT+RLVR 对比。 | **Open** — [30 游戏数据、golden 实现、生成样本、训练与 evaluator 代码](https://github.com/tktserapio/internalizing-cwm-sft-grpo)；未声称提供现成 checkpoint。 |
| 38 | 2026 | [The Verifier is the Curriculum](https://arxiv.org/abs/2607.09709) | 用 strict-launch gate 自蒸馏 brief 到完整 Godot 游戏的生成器，测试未见游戏族。 | 经后训练的 14B 游戏代码模型和 launch-grounded 训练候选。 | 4 个 held-out 家族；单候选干净启动率 8.8%→42.2%，best-of-K 覆盖 18/25→25/25，并含匹配对照。 | **Closed** — 未核验到官方 LoRA/checkpoint、自蒸馏数据或方法代码；上游 GameCraft-Bench 发布不属于本论文工件。 |
| 39 | 2026 | [MAGIC](https://arxiv.org/abs/2607.11594) | 从单提示生成带 portal 脚本的连通、可导航多场景 Unity 工程。 | 多个带物件场景、共享转场表示、portal 和可运行工程装配。 | 100-case 转场基准；报告 0.99 precision、0.95 recall、0.96 F1，并检查可导航性。 | **Partial，环境依赖重** — [生成与评测代码](https://github.com/sereneee1201/MAGIC)已公开，但仓库说明完整 100-case benchmark 只能申请获取。 |
| 40 | 2019 | [General Video Game Rule Generation](https://arxiv.org/abs/1906.05160) | 在专用 GVGAI 规则生成赛道中，根据游戏关卡生成 VGDL 规则。 | random、constructive 和 search 三类可执行规则集。 | 三种生成器的可玩性、趣味/质量观察和规则集多样性。 | **Open** — 官方[GVGAI 规则生成框架与三种生成器](https://github.com/GAIGResearch/GVGAI/tree/master/src/tracks/ruleGeneration)均已公开。 |
| 41 | 2023 | [Mechanic Maker 2.0](https://arxiv.org/abs/2309.09476) | 开放 Unity 规则生成环境，用 RL 或 A* agent 评价候选。 | 新平台游戏规则，以及评测轨迹/模型。 | 比较学习式 RL 与静态 A* 近似器产生的规则分布，并分析人工可用性。 | **Open，环境依赖重** — [完整 Unity 工程、规则数据、结果和已训练 ONNX agents](https://github.com/Harcurio/MechanicMiner)。 |

## 4. 共创、修复与人机协作设计（4 篇）

这些工作因最终产物会改变游戏代码或规则而符合范围，但不应与自主“提示词到完整游戏”系统混排排名。

| # | 年份 | 论文/资源 | 范围 | 生成内容 | 评测 | 工件/状态 |
| ---: | :---: | --- | --- | --- | --- | --- |
| 42 | 2024 | [Open Role-Playing with Delta-Engines](https://arxiv.org/abs/2408.05842) | base engine 加 LLM neural proxy，把自然语言成长选择逐步转成角色代码。 | Free Pokémon 案例中的自定义能力、招式和运行时机制。 | 合成角色的执行率、GPT-4 正确率、数据分析和 10 人共创。 | **官方案例 Open** — [引擎/UI 代码、提示词、训练/测试角色数据和 LoRA 链接](https://github.com/gingasan/delta-engine/tree/main/free-pokemon)已公开；不是通用从零游戏生成器。 |
| 43 | 2025 | [Fly, Fail, Fix](https://arxiv.org/abs/2507.12666) | RL 试玩器提供指标/图像，LMM 把固定 Flappy Bird 配置改向目标行为。 | 对难度、间距、速度、重力等机制/配置的迭代修改。 | 4 种反馈条件、每轮 5 个 episode、目标分数 10，每种配置 10 次试验。 | **Closed** — 只有论文引用的[上游 Flappy Bird RL 环境](https://github.com/markub3327/flappy-bird-gymnasium)公开；LMM designer loop、配置和评测包未公开。 |
| 44 | 2025 | [Repairing General Game Descriptions](https://arxiv.org/abs/2508.10438) | 从错误 GDL 和形式化 well-formedness/GTL 要求寻找最小规则修复。 | 用 ASP 选择规则编辑，恢复终止性、可玩性、弱可胜性或指定时序属性。 | toy、井字棋和 blocks-world 实例；修复存在性/最小性及 solver 行为。 | **Open，依赖较重** — [encoding、修复代码和实例](https://github.com/hharryyf/gdlRepair)；需要 Clingo 与 Guess-and-Check。 |
| 45 | 2026 | [AutoBG](https://arxiv.org/abs/2606.01976) | 从多轮构思生成完整规则书，critic gate 迭代修订，并用 150 个玩家 persona 提供反馈。 | 结构化桌游草案和持续修订的自然语言规则书。 | 207 个 held-out 游戏、baseline 对比、缺陷诊断/修订质量和 30 人用户研究。 | **Closed** — 论文标注资源“coming soon”；截至检索日没有公开官方代码、2.2K 规则书、180K 评论、模型或 evaluator。 |

## 5. 其他生成相关邻接研究（4 篇）

这些既有工作直接服务于生成游戏，但并不都是“提示词到完整游戏”的自主系统。

| # | 年份 | 论文/资源 | 范围 | 生成内容 | 评测 | 工件/状态 |
| ---: | :---: | --- | --- | --- | --- | --- |
| 46 | 2025 | [DreamGarden — A Designer Assistant for Growing Games from a Single Prompt](https://arxiv.org/abs/2410.01791) | 从单一创意出发，在人类参与下规划并实现 Unreal 游戏环境。 | 设计师可修剪、细化的层级计划和已实现环境模块。 | HCI 系统分析与用户研究，不是自动 coding benchmark。 | **Closed** — [ACM DOI](https://doi.org/10.1145/3706598.3714233)；未核验到完整官方系统/evaluator 发布。 |
| 47 | 2025 | [Game Development as Human–LLM Interaction（ChatGE）](https://aclanthology.org/2025.acl-long.218/) | 在扑克类游戏上展示多轮共同开发。 | 脚本片段、代码片段和设计指引，而非经验证的完整 build。 | 交互质量，以及代码正确性的 F-ESR、F-Acc、ESR 和 Acc。 | **Closed** — [arXiv](https://arxiv.org/abs/2408.09386)；未核验到官方发布包。 |
| 48 | 2026 | [Agentic Game Development as a Verifiable Trajectory Data Engine](https://arxiv.org/abs/2608.25518) | 把 Unity/Unreal/Godot 开发变成可验证多模态训练轨迹来源。 | 引擎编辑、可执行工件，以及编译器/运行时/人工反馈轨迹。 | UnitySceneBench 及 held-out/跨引擎迁移诊断。 | **Partial** — [预览审计/复现代码和脱敏结果](https://github.com/LanceZPF/cardinal-preview)已公开；checkpoint 尚不可下载，只计划后续上传。 |
| 49 | 2026 | [Lottery and Sprint Arcade — Player-Driven Game Editing](https://arxiv.org/abs/2607.10711) | 玩家在固定类 Space Invaders 游戏中通过约 100 个配置字段进行语音编辑。 | 对机制、视觉、交互和音频的结构化修改。 | 用户体验、NASA-TLX 工作负荷和编辑日志分析。 | **Closed** — 未核验到官方系统、研究数据或 evaluator 发布。 |

## 6. Learned-engine 边界项（1 篇）

该条目会生成可交互体验，但不产出显式规则、源代码或传统引擎工程，因此不能与 game-code benchmark 混成一个排行榜。

| # | 年份 | 论文/资源 | 范围 | 生成内容 | 评测 | 工件/状态 |
| ---: | :---: | --- | --- | --- | --- | --- |
| 50 | 2024 | [Playable Game Generation](https://arxiv.org/abs/2412.00887) | 从游戏视频与动作数据学习动作条件 latent-dynamics 引擎。 | 可实时操作的视频帧，而非可执行源代码或工程文件。 | 视觉保真、动作/动力学对齐、长时一致性和实时可玩性。 | **Partial** — [官方实现](https://github.com/GreatX3/Playable-Game-Generation)已公开，但完整训练数据/复现链路未公开。 |
