# 端到端游戏生成：Benchmark 与论文索引

[返回首页](../../README.zh-CN.md) · [English](../en/end-to-end.md) · [自动设计与 PCG](pcg.md) · [交互世界](interactive-worlds.md) · [收录范围](../../SCOPE.md)

> 检索截止：**2026-08-29（Asia/Shanghai）**。本索引只收录把提示词、规格或规则转成可执行游戏、游戏工程、游戏代码，或为生成游戏提供验证/编辑工件的工作。这里**明确排除玩游戏的论文**：如果主要目标是学习游玩策略、提高得分或在现有游戏中获胜，就不纳入。

只生成单个关卡、单类资产，以及仅输出动作条件视频的世界模型均不属于核心范围。只有当 gameplay、self-play 或 GUI agent 被用于测试或修复生成游戏时才会出现。**Open** 表示核心工件已公开；**Partial** 表示只公开部分组件、demo 或评测材料；**Closed** 表示截至检索日未核验到可复现的官方发布。

## 1. Benchmark 与评测集（10 条）

| # | 年份 | 论文/资源 | 范围 | 生成内容 | 评测 | 工件/状态 |
| ---: | :---: | --- | --- | --- | --- | --- |
| 1 | 2025 | [V-GameGym（SKYLENAGE-GameCodeGym）](https://arxiv.org/abs/2509.20136) | 从自然语言需求开始生成 Pygame；含 100 个主题簇、2,219 个经核查样本。 | 可运行的 Pygame 工程。 | 加权代码、截图和 gameplay 视频 judge 分数。 | **Open** — [项目/排行榜](https://v-gamegym.github.io/)、[代码](https://github.com/alibaba/SKYLENAGE-GameCodeGym)、[数据集](https://huggingface.co/datasets/alibabagroup/SKYLENAGE-GameCodeGym)；依赖 judge 模型。 |
| 2 | 2026 | [GameDevBench](https://arxiv.org/abs/2602.11103) | Godot 4.4.1 工程中的 333 个仓库编辑任务。 | 对现有游戏的玩法、UI、图形和动画修改。 | 确定性 Godot 行为测试；pass@1/任务成功率。 | **Open** — [项目](https://waynechi.com/gamedevbench)、[任务、runner 与结果](https://github.com/waynchi/gamedevbench)。 |
| 3 | 2026 | [GameCraft-Bench](https://arxiv.org/abs/2606.17861) | 15 类游戏的 140 个从零生成 brief。 | 完整 Godot 游戏和可回放输入轨迹。 | 回放轨迹后执行 build gate，并按机制、内容、视觉和呈现加权评分。 | **Open，环境依赖重** — [项目/demo](https://tongxuluo.github.io/gamecraft-bench-website/)、[代码、任务与 verifier](https://github.com/FreedomIntelligence/gamecraft-bench)。 |
| 4 | 2026 | [GameEngineBench](https://arxiv.org/abs/2607.03525) | 9 个真实 UE5 仓库中的 110 个原生 C++ 任务。 | 玩法、网络、动画、UI、持久化、XR 和渲染等引擎兼容修改。 | 隐藏 Unreal 运行时行为测试；仅编译通过不算成功。 | **Open，环境依赖重** — [任务、runner 与结果](https://github.com/Nitrode-Research/GameEngineBench)；需要本地 UE5。 |
| 5 | 2026 | [GameXpert-Bench](https://arxiv.org/abs/2608.21833) | 生命周期 benchmark：97 个 GameGen、100 个 GameFix，以及 17 条六轮 GameOpt 链。 | 新游戏、缺陷修复及玩法/呈现的迭代优化。 | 完整性/体验/视觉 rubric、回归测试、修复比例和优化分数。 | **截至检索日 Closed** — [官方仓库](https://github.com/Kwen-Chen/GameXpert-Bench)仍是发布脚手架，未含 benchmark 或 evaluator。 |
| 6 | 2026 | [JamBench / JamSet（JAMER）](https://arxiv.org/abs/2606.19830) | 8,133 个已验证 game-jam Godot 工程的项目级语料；其中 benchmark 300 个、训练集 7,833 个。 | 主题驱动工程，以及函数、脚本或完整脚本补全。 | L1/L2/L3a 通过率、结构完整度和确定性行为对齐分数。 | **截至检索日 Closed** — 未核验到可用的官方工件链接。 |
| 7 | 2026 | [VeriGame / GameGen-Verifier](https://arxiv.org/abs/2605.07442) | 覆盖 7 类、100 个游戏规格的 specification compliance 评测。 | 可验证关键点、注入目标状态、短交互探针和判定。 | 对照人工判断计算 Acc@5、Prec@5、Rec@5、F1@5 和 Time@5。 | **Partial** — [实现](https://github.com/NetX-lab/GameGen-Verifier)含 harness 与规格，但不含完整生成游戏证据。 |
| 8 | 2026 | [OpenGame-Bench](https://arxiv.org/abs/2604.18394) | 5 类网页游戏、150 个提示词，从空工作区开始。 | 完整浏览器游戏，每任务评测 3 个随机种子。 | 浏览器执行后的 Build Health、Visual Usability 和逐需求 Intent Alignment。 | **Partial** — [项目](https://yelonlft.github.io/OpenGame-landing-page/)与[框架/demo 源码](https://github.com/leigest519/OpenGame)已公开；任务和 evaluator 尚待发布。 |
| 9 | 2026 | [PlaytestArena](https://arxiv.org/abs/2605.28258) | 8 类、200 个浏览器游戏提示词及可观察 gameplay rubric。 | 生成游戏，以及供修复使用的 GUI agent 试玩判定。 | GUI agent 在不看源码的情况下试玩并计算 rubric 通过率；用 32 个游戏核对人工一致性。 | **Partial** — [项目](https://continual-game-generation.vercel.app/)和[八个 demo 的仓库](https://github.com/RunRiotComeOn/gui-agents-for-continual-game-generation)已公开，完整 arena 未公开。 |
| 10 | 2026 | [PlayGen-20（AutoUE）](https://arxiv.org/abs/2603.07106) | 按难度划分的 20 个 Unreal Engine 3D 游戏自然语言 brief。 | 完整场景、PCG 图、C++ 玩法/交互模块和可运行游戏。 | 场景、玩法和视觉分数，加图/模块/交互检查及运行时证据。 | **Open，环境依赖重** — [代码](https://github.com/Pluto156/AutoUE)、[数据集、demo、资产与结果](https://huggingface.co/datasets/Pluto156/AutoUE_DataSet)；需要 UE5 和 API key。 |

## 2. 核心端到端、游戏代码与完整规则生成论文（13 篇）

| # | 年份 | 论文/资源 | 范围 | 生成内容 | 评测 | 工件/状态 |
| ---: | :---: | --- | --- | --- | --- | --- |
| 11 | 2024 | [Game Generation via Large Language Models](https://arxiv.org/abs/2404.08706) | 用提示词联合生成完整 VGDL 规则与关卡。 | 同时包含机制和关卡的可执行游戏描述。 | 比较多种上下文设置下的编译与可玩性。 | **Closed** — [IEEE 记录](https://doi.org/10.1109/COG60054.2024.10645597)；未核验到官方实现或固定 benchmark。 |
| 12 | 2024 | [Grammar-Based Game Description Generation Using Large Language Models（GGDG）](https://arxiv.org/abs/2407.17404) | 把自然语言意图转成受语法约束的 Ludii 程序。 | 语法正确、可执行的完整游戏描述。 | 比较不同生成设置的语法有效性、执行情况和游戏质量。 | **Open** — [IEEE DOI](https://doi.org/10.1109/TG.2024.3520214)、[代码与实验脚本](https://github.com/tsunehiko/ggdg)；Ludii 需另行获取。 |
| 13 | 2024 | [GAVEL — Generating Games via Evolution and Language Models](https://arxiv.org/abs/2407.09388) | 对 Ludii 程序变异进行质量多样性搜索。 | 新颖、可执行的桌游规则程序。 | QD 分数、可玩 archive 覆盖、fitness、语义新颖性和专家分析。 | **Open** — [代码、数据与 checkpoint](https://github.com/gdrtodd/gavel)、[可玩的生成游戏](https://ludii.games/library.php)。 |
| 14 | 2023，2025 修订 | [GameGPT — Multi-agent Collaborative Framework for Game Development](https://arxiv.org/abs/2310.08067) | 用角色分工 agents 规划并实现游戏开发需求。 | 计划、任务、代码和游戏开发工件。 | 框架案例研究；没有标准化任务/evaluator 套件。 | **Closed** — 未核验到官方实现。 |
| 17 | 2025 | [ScriptDoctor — Automatic Generation of PuzzleScript Games via LLMs and Tree Search](https://arxiv.org/abs/2506.06524) | 借助编译器、CFG 和求解器反馈迭代生成完整 PuzzleScript。 | 经修复的 PuzzleScript 游戏与关卡。 | 编译、是否存在求解器解，以及严格的多关卡可解性。 | **论文复现 Closed** — [IEEE DOI](https://doi.org/10.1109/COG64752.2025.11114269)、[上游 PuzzleScript 引擎](https://github.com/increpare/PuzzleScript)；未核验到 ScriptDoctor/语料发布。 |
| 18 | 2025 | [Cardiverse — Harnessing LLMs for Novel Card Game Prototyping](https://aclanthology.org/2025.emnlp-main.1511/) | 由机制图谱驱动新卡牌游戏原型生成。 | 新机制、可执行游戏代码和可玩原型。 | 机制新颖性/相似度、用户评分、代码 pass@3、执行一致性及辅助锦标赛。 | **Open** — [arXiv](https://arxiv.org/abs/2502.07128)、[代码/数据](https://github.com/danruili/Cardiverse)。 |
| 19 | 2024，2025 修订 | [A Text-to-Game Engine for UGC-Based Role-Playing Games（Zagii）](https://arxiv.org/abs/2407.08195) | 运行时 text-to-RPG 生成。 | 叙事、角色、环境、视听资产和游戏机制。 | 产品使用、可玩性和参与度统计；没有固定公开 baseline。 | **Closed** — [官方产品](https://rpggo.ai/)可访问，但代码、数据和 evaluator 未公开。 |
| 20 | 2026 | [OpenGame — Open Agentic Coding for Games](https://arxiv.org/abs/2604.18394) | 从一个 brief 和空工作区生成多文件 Phaser/TypeScript 工程。 | 带生成式视听资产的完整浏览器游戏。 | OpenGame-Bench 的 Build Health、Visual Usability 和 Intent Alignment。 | **Partial** — [项目](https://yelonlft.github.io/OpenGame-landing-page/)、[框架与 demo 源码](https://github.com/leigest519/OpenGame)；模型、训练数据和完整 evaluator 未发布。 |
| 21 | 2026 | [CreativeGame — Toward Mechanic-Aware Creative Game Generation](https://arxiv.org/abs/2604.19926) | 利用版本谱系与记忆演化机制感知的 HTML5 游戏。 | 新游戏、显式机制增量和版本轨迹。 | 机制实现、结构变化、新颖性、运行时稳健性及论文报告的 LLM 质量评分。 | **仅 Partial demo** — [项目](https://yiweishi-cn.github.io/CreativeEvolutionGame/)、[demo 仓库](https://github.com/yiweishi-cn/CreativeEvolutionGame)、[OpenReview 记录](https://openreview.net/forum?id=VtmBAGCN7o)。 |
| 22 | 2025 | [UniGen — 90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development](https://arxiv.org/abs/2509.26161) | 从自然语言需求自动完成 Unity 规划、编码、装配与调试。 | Unity 蓝图、C# 脚本、绑定组件、场景和可运行 3D 原型。 | 3 个原型的功能完整度交互矩阵及人工开发耗时对比。 | **Partial** — [代码](https://github.com/yxwan123/UniGen)；缺少受评工程、资产、矩阵和 evaluator。 |
| 23 | 2026 | [GUI Agents for Continual Game Generation（Play2Code）](https://arxiv.org/abs/2605.28258) | 最多五轮重复执行浏览器游戏生成、GUI 试玩和代码修复。 | 完整浏览器游戏及连续修复版本。 | PlaytestArena rubric 通过率和 play–code 各轮提升。 | **Partial** — [项目](https://continual-game-generation.vercel.app/)、[八个 demo 的仓库](https://github.com/RunRiotComeOn/gui-agents-for-continual-game-generation)；完整系统/任务/evaluator 未发布。 |
| 24 | 2025 | [Boardwalk — Towards a Framework for Creating Board Games with LLMs](https://arxiv.org/abs/2508.16447) | 把 12 款桌游的匿名化自然语言规则转成 Python 实现。 | 自由格式和兼容 Boardwalk API 的可玩桌游。 | 可玩性、规则遵循、成功率及模型/错误分析。 | **Partial** — [会议 DOI](https://doi.org/10.5753/sbgames.2025.10222)、[Boardwalk API/示例](https://github.com/LabCRAIG/boardwalk)；缺少完整输出/evaluator。 |
| 26 | 2026 | [AutoUE — Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems](https://arxiv.org/abs/2603.07106) | 从自然语言 brief 到 UE5 资产检索、PCG 场景构建、C++ 实现和运行测试。 | 含场景、玩法模块和交互的完整可运行 3D 游戏。 | PlayGen-20 场景/玩法/视觉评分及引擎原生运行检查。 | **Open，环境依赖重** — [代码](https://github.com/Pluto156/AutoUE)、[数据集与生成 demo](https://huggingface.co/datasets/Pluto156/AutoUE_DataSet)。 |

## 3. 生成相关邻接研究：共创、验证与轨迹数据（5 篇）

这些工作直接服务于生成游戏，但并不都是“提示词到完整游戏”的自主系统。

| # | 年份 | 论文/资源 | 范围 | 生成内容 | 评测 | 工件/状态 |
| ---: | :---: | --- | --- | --- | --- | --- |
| 15 | 2025 | [DreamGarden — A Designer Assistant for Growing Games from a Single Prompt](https://arxiv.org/abs/2410.01791) | 从单一创意出发，在人类参与下规划并实现 Unreal 游戏环境。 | 设计师可修剪、细化的层级计划和已实现环境模块。 | HCI 系统分析与用户研究，不是自动 coding benchmark。 | **Closed** — [ACM DOI](https://doi.org/10.1145/3706598.3714233)；未核验到完整官方系统/evaluator 发布。 |
| 16 | 2025 | [Game Development as Human–LLM Interaction（ChatGE）](https://aclanthology.org/2025.acl-long.218/) | 在扑克类游戏上展示多轮共同开发。 | 脚本片段、代码片段和设计指引，而非经验证的完整 build。 | 交互质量，以及代码正确性的 F-ESR、F-Acc、ESR 和 Acc。 | **Closed** — [arXiv](https://arxiv.org/abs/2408.09386)；未核验到官方发布包。 |
| 25 | 2024 | [Automatic Bug Detection in LLM-Powered Text-Based Games Using LLMs](https://aclanthology.org/2024.findings-acl.907/) | 针对规格、状态和交互轨迹的纯验证工作。 | LLM 驱动文字游戏的逻辑/一致性缺陷报告。 | 受控 bug detection 实验。 | **Closed** — 未核验到官方代码、数据或 evaluator 发布。 |
| 27 | 2026 | [Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models](https://arxiv.org/abs/2608.25518) | 把 Unity/Unreal/Godot 开发变成可验证多模态训练轨迹来源。 | 引擎编辑、可执行工件，以及编译器/运行时/人工反馈轨迹。 | UnitySceneBench 及 held-out/跨引擎迁移诊断。 | **Partial** — [预览代码/checkpoint](https://github.com/LanceZPF/cardinal-preview)；完整轨迹引擎和数据集并非开箱可用。 |
| 28 | 2026 | [Lottery and Sprint Arcade — Enabling Player-Driven Game Editing with Generative AI](https://arxiv.org/abs/2607.10711) | 玩家在固定类 Space Invaders 游戏中通过约 100 个配置字段进行语音编辑。 | 对机制、视觉、交互和音频的结构化修改。 | 用户体验、NASA-TLX 工作负荷和编辑日志分析。 | **Closed** — 未核验到官方系统、研究数据或 evaluator 发布。 |

## 4. Learned-engine 边界项（1 篇）

该条目会生成可交互体验，但不产出显式规则、源代码或传统引擎工程，因此不能与 game-code benchmark 混成一个排行榜。

| # | 年份 | 论文/资源 | 范围 | 生成内容 | 评测 | 工件/状态 |
|---:|:---:|---|---|---|---|---|
| 29 | 2024 | [Playable Game Generation](https://arxiv.org/abs/2412.00887) | 从游戏视频与动作数据学习动作条件 latent-dynamics 引擎。 | 可实时操作的视频帧，而非可执行源代码或工程文件。 | 视觉保真、动作/动力学对齐、长时一致性和实时可玩性。 | **对 learned-engine pipeline 为 Partial/Open** — [官方实现](https://github.com/GreatX3/Playable-Game-Generation)；训练数据可复现性需另行判断。 |
