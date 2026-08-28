# End-to-end game generation, game-code agents, and verification benchmarks

> 检索截止 / Research cutoff: **2026-08-29 (Asia/Shanghai)**
> 本底稿只引用论文官网、arXiv、ACL Anthology、PMLR、OpenReview、ACM/IEEE 页面、作者项目页和官方代码/数据仓库。它专门回答“AI 能否把需求变成可运行游戏或游戏工程”，不收录以让 agent 玩游戏、提高游戏得分为主要目标的工作。

## Scope and labels / 范围与开放性标记

- **Included:** natural-language-to-playable-game；完整游戏规则与关卡联合生成；Unity / Unreal / Godot / Phaser / Pygame 等工程或代码生成；多智能体游戏开发；game-jam project generation；自动编译、运行、试玩、验证、修复或优化生成游戏。
- **Excluded from the main list:** 只让 agent 玩现成游戏；只提升 score / win rate；通用软件工程 benchmark；只生成角色、贴图、音频或单个关卡；仅生成动作条件视频而不产生可执行游戏逻辑的 world model。
- **Open:** 官方公开了完成该条目核心任务所需的代码/数据/任务和 evaluator（专有 API、商业引擎或重硬件依赖仍单独注明）。
- **Partial:** 只公开了其中一部分，例如框架、模型、demo、任务或评分器，但无法按论文协议完整复核。
- **Closed:** 没有可核验的官方实现/任务/评分器，或只有论文、产品页面、视频和静态展示。
- “Open”描述的是**工件可得性**，不是结果绝对可重复；LLM/VLM judge、外部 API、引擎版本与素材许可证仍会造成变动。

## A. Benchmarks and evaluation sets / 基准与评测集

### 1. V-GameGym (SKYLENAGE-GameCodeGym)

- **Year / status:** 2025, arXiv preprint.
- **Input → output:** natural-language requirements → runnable Pygame projects; 2,219 human-checked samples in 100 thematic clusters, mined from 2,190 repositories.
- **Evaluation:** weighted code, static-screenshot and dynamic-gameplay/video judge scores; also reports quality bands and solved-game counts.
- **Official artifacts:** [paper](https://arxiv.org/abs/2509.20136), [project/leaderboard](https://v-gamegym.github.io/), [code](https://github.com/alibaba/SKYLENAGE-GameCodeGym), [dataset](https://huggingface.co/datasets/alibabagroup/SKYLENAGE-GameCodeGym).
- **Availability:** **Open.** Test data and generation, execution, recording and evaluation pipeline are public; judge-model dependence remains.
- **纳入理由 / Inclusion:** 直接评测“自然语言需求到可运行游戏代码”，而不是游戏玩家代理。
- **中文：** 用三模态执行证据评测大模型从需求生成完整 Pygame 游戏的能力。
- **English:** *V-GameGym evaluates requirement-to-runnable-Pygame generation with code, screenshot, and gameplay-video evidence.*

### 2. GameDevBench

- **Year / venue:** 2026, ICML 2026 (as stated by the official repository).
- **Input → output:** 333 repository-editing tasks from web/video tutorials → modifications to Godot 4.4.1 projects across gameplay logic, UI, 2D/3D graphics and animation.
- **Evaluation:** deterministic Godot behavioral tests; primary reporting is pass@1 / task success.
- **Official artifacts:** [paper](https://arxiv.org/abs/2602.11103), [project](https://waynechi.com/gamedevbench), [tasks, runner and results](https://github.com/waynchi/gamedevbench).
- **Availability:** **Open.** Task archives, validator, results and fixed engine version are public.
- **纳入理由 / Inclusion:** 是真实游戏工程中的 coding-agent benchmark；目标是实现/修改游戏，不是游玩得分。
- **中文：** 用确定性 Godot 测试衡量 coding agent 能否完成真实游戏工程任务。
- **English:** *GameDevBench tests coding agents on 333 real Godot repository tasks with deterministic runtime checks.*

### 3. GameCraft-Bench

- **Year / status:** 2026, arXiv preprint.
- **Input → output:** 140 natural-language briefs across 15 game families → complete Godot games plus replayable input traces.
- **Evaluation:** build gate multiplied by a weighted rubric: Core Mechanics 0.15, Content Depth 0.35, Functional Visuals 0.15, Art and Presentation 0.35; a verifier launches each game and replays submitted traces before multimodal judging.
- **Official artifacts:** [paper](https://arxiv.org/abs/2606.17861), [project/demos](https://tongxuluo.github.io/gamecraft-bench-website/), [code, tasks and verifier](https://github.com/FreedomIntelligence/gamecraft-bench).
- **Availability:** **Open, environment-heavy.** Requires Godot 4.6.2, Linux UI tooling and a judge API; the visual judge is not deterministic.
- **纳入理由 / Inclusion:** 评测从空工程端到端构建可玩游戏，而非局部补全。
- **中文：** 要求 agent 同时交付完整 Godot 游戏和可回放操作轨迹，用真实运行验证可玩性。
- **English:** *GameCraft-Bench evaluates end-to-end Godot game creation by replaying agent-submitted input traces before scoring the result.*

### 4. GameEngineBench

- **Year / status:** 2026, arXiv preprint.
- **Input → output:** 110 scoped native-C++ tasks in nine real Unreal Engine 5 repositories → engine-compatible code changes spanning gameplay, networking, animation, UI, persistence, XR and rendering.
- **Evaluation:** pass@1 on hidden Unreal automation behavioral tests; compilation alone is insufficient.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.03525), [tasks, runner and results](https://github.com/Nitrode-Research/GameEngineBench).
- **Availability:** **Open, environment-heavy.** A local Unreal installation is required; some EOS tasks additionally require Epic's SDK.
- **纳入理由 / Inclusion:** 衡量 agent 对真实商业引擎 runtime contracts 的实现能力，不是普通算法题。
- **中文：** 在真实 UE5 C++ 仓库中用运行时行为测试检验游戏引擎 coding agent。
- **English:** *GameEngineBench measures coding agents on real Unreal C++ repositories using runtime behavioral tests rather than build success alone.*

### 5. GameXpert-Bench

- **Year / status:** 2026, arXiv preprint.
- **Input → output:** three lifecycle tracks: GameGen (97 from-scratch tasks, 11 genres), GameFix (100 tasks built from 50 human-verified levels with 19–27 injected bugs each), and GameOpt (17 six-round chains, 102 requests).
- **Evaluation:** GameGen averages Completeness, Richness, Player Experience and Visual Quality; GameFix uses fail-to-pass/pass-to-pass tests, bug-fixed ratio and Strict/Cliff curves; GameOpt scores gameplay, level, balance, art, UI and audio with regression checks.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.21833), [official repository](https://github.com/Kwen-Chen/GameXpert-Bench).
- **Availability:** **Closed as of the cutoff.** The official repository identifies itself as a public-release scaffold; benchmark data, evaluator and model artifacts are not yet present.
- **纳入理由 / Inclusion:** 少见地覆盖生成、修复、优化三段游戏开发生命周期，但不能误写成已可下载 benchmark。
- **中文：** 把完整游戏生成、密集缺陷修复和多轮体验优化放进同一个生命周期基准。
- **English:** *GameXpert-Bench spans from-scratch generation, dense game repair, and iterative optimization, but its benchmark artifacts are not yet released.*

### 6. JamBench / JamSet (JAMER)

- **Year / status:** 2026, arXiv preprint.
- **Input → output:** project-level Godot data from game-jam repositories; the paper reports 8,133 verified projects, with 300 in JamBench and 7,833 in JamSet, supporting theme-driven creation and function/script/full-script completion.
- **Evaluation:** L1/L2/L3a pass rates, Structural Completeness Score (SCS), and Behavioral Alignment Score (BAS) under deterministic inputs.
- **Official source:** [paper](https://arxiv.org/abs/2606.19830).
- **Availability:** **Closed as of the cutoff.** The paper says code/data are public, but its official paper/source does not expose a working artifact URL and no author release could be verified.
- **纳入理由 / Inclusion:** game-jam project corpus and engine-level behavioral comparison directly target game development, but release claims must be separated from observed availability.
- **中文：** 用真实 game-jam Godot 工程构建项目级生成与补全基准，并比较运行时行为。
- **English:** *JAMER derives project-level Godot generation and completion tasks from game-jam repositories, with structural and behavioral scoring.*

### 7. VeriGame / GameGen-Verifier

- **Year / status:** 2026, arXiv preprint.
- **Input → output:** game specification → verifiable keypoints, injected target states, short parallel runtime interactions and per-keypoint verdicts; VeriGame contains 100 specifications across seven genres.
- **Evaluation:** Acc@5, Prec@5, Rec@5, F1@5 and Time@5 against human specification-element judgments.
- **Official artifacts:** [paper](https://arxiv.org/abs/2605.07442), [implementation](https://github.com/NetX-lab/GameGen-Verifier).
- **Availability:** **Partial.** Harness, 100 specs and examples are public, but the repository does not include the complete paper set of generated games, runs, logs and screenshots.
- **纳入理由 / Inclusion:** 直接验证生成游戏是否满足 specification，且通过状态注入避免仅靠长时间随机试玩。
- **中文：** 把游戏需求拆成可验证点，通过状态注入和短交互高效核验生成结果。
- **English:** *GameGen-Verifier checks specification compliance by injecting target states and running short, parallel gameplay probes.*

### 8. OpenGame-Bench

- **Year / status:** 2026, introduced in the OpenGame arXiv report.
- **Input → output:** 150 natural-language prompts in five web-game genres → complete browser games from empty workspaces; three random seeds per task.
- **Evaluation:** Build Health (BH), Visual Usability (VU: pixel heuristics plus VLM) and Intent Alignment (IA: weighted per-requirement VLM verdict), all on a 0–100 scale after headless-browser execution.
- **Official artifacts:** [paper](https://arxiv.org/abs/2604.18394), [project](https://yelonlft.github.io/OpenGame-landing-page/), [framework and demo sources](https://github.com/leigest519/OpenGame).
- **Availability:** **Partial.** The framework and runnable demo sources are public, but the README says the evaluation pipeline “will be released soon”; the 150 tasks/evaluator and GameCoder-27B weights are not downloadable at the cutoff.
- **纳入理由 / Inclusion:** 是端到端网页游戏生成评测，但必须区分“OpenGame 框架已开源”和“OpenGame-Bench 尚未完整发布”。
- **中文：** 在真实浏览器中同时评测生成游戏的构建健康、视觉可用性与需求对齐。
- **English:** *OpenGame-Bench scores browser-game agents on build health, visual usability, and intent alignment, though its full task/evaluator release is pending.*

### 9. PlaytestArena

- **Year / status:** 2026, introduced in *GUI Agents for Continual Game Generation* (arXiv preprint).
- **Input → output:** 200 browser-game generation prompts across eight genres plus observable gameplay rubrics → generated games and GUI-agent playtest verdicts.
- **Evaluation:** rubric pass rate from a GUI agent that opens and plays the game without source-code or internal-state access; the paper validates agreement against humans on a stratified 32-game subset.
- **Official artifacts:** [paper](https://arxiv.org/abs/2605.28258), [project](https://continual-game-generation.vercel.app/), [official demo gallery](https://github.com/RunRiotComeOn/gui-agents-for-continual-game-generation).
- **Availability:** **Partial.** Eight playable demos are public, but the 200 tasks, arena implementation, Play2Code system and evaluator are not in the official repository.
- **纳入理由 / Inclusion:** 将“可玩”落实为 GUI agent 的真实试玩证据，并把结果用于下一轮代码修复。
- **中文：** 用 GUI 代理实际游玩 200 个浏览器游戏任务，以可观察 rubric 评测并驱动持续修复。
- **English:** *PlaytestArena evaluates 200 browser-game tasks through real GUI play, and its feedback powers iterative code repair in Play2Code.*

### 10. PlayGen-20 (AutoUE)

- **Year / venue:** 2026, Findings of ACL 2026 (acceptance stated in the paper's arXiv record).
- **Input → output:** 20 natural-language 3D-game briefs (5 easy, 7 medium, 8 hard) → complete Unreal Engine scenes, PCG graphs, C++ gameplay/interaction modules and runnable games.
- **Evaluation:** Scene, Gameplay and Visual scores weighted 0.35/0.35/0.30; additional graph/module/interaction metrics; runtime commands execute inside Unreal and collect screenshots/logs.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.07106), [code](https://github.com/Pluto156/AutoUE), [dataset, 20 demo games, assets and experimental data](https://huggingface.co/datasets/Pluto156/AutoUE_DataSet).
- **Availability:** **Open, environment-heavy.** Apache-2.0 code and data are public; Unreal Engine and external API keys are required, and judge scores are non-deterministic.
- **纳入理由 / Inclusion:** 目前最直接的“自然语言到商业引擎完整 3D 游戏 + runtime test”评测之一。
- **中文：** 在 UE5 中端到端生成场景、C++ 玩法代码和交互对象，并用运行时证据评测。
- **English:** *PlayGen-20 evaluates natural-language-to-complete-UE5 generation, including scenes, C++ gameplay code, interactions, and runtime playtests.*

## B. End-to-end generation and game-development systems / 端到端生成与开发系统论文

### 11. Game Generation via Large Language Models

- **Year / venue:** 2024, IEEE Conference on Games (CoG 2024).
- **Input → output:** prompts with different context combinations → Video Game Description Language (VGDL) rules and levels generated together.
- **Evaluation:** compilation/playability-oriented experiments across prompt settings; no fixed public benchmark package.
- **Official sources:** [paper](https://arxiv.org/abs/2404.08706), [IEEE record](https://doi.org/10.1109/COG60054.2024.10645597).
- **Availability:** **Closed.** No official task set, runner or implementation release was verified.
- **纳入理由 / Inclusion:** 同时生成规则与关卡，跨过了“只做既有游戏关卡”的边界。
- **中文：** 用 LLM 一次生成 VGDL 游戏规则和配套关卡，而非只为固定规则生成地图。
- **English:** *This work uses LLMs to generate both VGDL game rules and levels instead of levels for a fixed game.*

### 12. Grammar-Based Game Description Generation Using Large Language Models (GGDG)

- **Year / venue:** 2024, IEEE Transactions on Games.
- **Input → output:** natural-language game intent plus a dynamically extracted grammar → valid Ludii game-description programs.
- **Evaluation:** grammatical validity and Ludii execution/game-quality concepts; compares grammar-constrained generation, standard generation and supervised fine-tuning settings.
- **Official artifacts:** [paper](https://arxiv.org/abs/2407.17404), [IEEE DOI](https://doi.org/10.1109/TG.2024.3520214), [code and experiment scripts](https://github.com/tsunehiko/ggdg).
- **Availability:** **Open.** Apache-2.0 code includes grammar/data construction and evaluation scripts; users obtain Ludii separately.
- **纳入理由 / Inclusion:** 输出可由通用游戏系统执行的完整规则描述，不是自然语言概念草图。
- **中文：** 通过动态语法约束把自然语言转成可执行、语法正确的 Ludii 游戏程序。
- **English:** *GGDG constrains LLMs with extracted grammars to produce executable Ludii game descriptions from natural-language intent.*

### 13. GAVEL — Generating Games via Evolution and Language Models

- **Year / venue:** 2024, NeurIPS 2024.
- **Input → output:** Ludii descriptions and fill-in-the-middle mutations → novel executable board-game programs through MAP-Elites quality-diversity search.
- **Evaluation:** QD score, playable archive cells, cells above fitness 0.5, semantic-concept novelty and expert qualitative analysis.
- **Official artifacts:** [paper](https://arxiv.org/abs/2407.09388), [code, data and checkpoints](https://github.com/gdrtodd/gavel), [playable generated games](https://ludii.games/library.php).
- **Availability:** **Open.** Code, Ludii fork, training data and checkpoint links are public.
- **纳入理由 / Inclusion:** 自动生成新的完整棋盘游戏规则程序；其 gameplay simulation 是生成质量测试，不是训练玩家 agent。
- **中文：** 将代码语言模型和质量多样性搜索结合，进化出可执行的新 Ludii 棋盘游戏。
- **English:** *GAVEL evolves novel executable Ludii board games by combining a code model with MAP-Elites quality-diversity search.*

### 14. GameGPT — Multi-agent Collaborative Framework for Game Development

- **Year / status:** 2023, revised 2025, arXiv preprint.
- **Input → output:** high-level game-development request → planned tasks and implementation artifacts through planning, task-identification and coding agents with layered lexicons.
- **Evaluation:** framework and case studies; no standardized released task/evaluator suite.
- **Official source:** [paper](https://arxiv.org/abs/2310.08067).
- **Availability:** **Closed.** No author implementation was verified; unrelated repositories with the same name are not official artifacts.
- **纳入理由 / Inclusion:** 早期明确把多智能体软件开发流程专门用于游戏工程。
- **中文：** 用分工协作的 LLM agents 规划并实现游戏工程，同时针对幻觉和重复工作设计约束。
- **English:** *GameGPT applies a role-specialized multi-agent workflow to game planning and implementation while targeting hallucination and redundancy.*

### 15. DreamGarden — A Designer Assistant for Growing Games from a Single Prompt

- **Year / venue:** 2025, ACM CHI 2025.
- **Input → output:** one high-level dream/memory/idea → a hierarchical plan and implemented Unreal Engine game environment; designers can seed, prune and give feedback.
- **Evaluation:** HCI system analysis and user study rather than an automatic coding benchmark.
- **Official sources:** [paper](https://arxiv.org/abs/2410.01791), [ACM DOI](https://doi.org/10.1145/3706598.3714233).
- **Availability:** **Closed.** No complete official Unreal system, fixed tasks or evaluator release was verified.
- **纳入理由 / Inclusion:** 直接研究单提示到 Unreal 游戏环境的规划、实现与人机共创工作流。
- **中文：** 把一个高层创意拆成层级计划，并由专门模块在 Unreal 中逐步长成游戏环境。
- **English:** *DreamGarden decomposes one high-level prompt into a hierarchical plan whose modules grow an Unreal game environment with designer feedback.*

### 16. Game Development as Human–LLM Interaction (ChatGE)

- **Year / venue:** 2025, ACL 2025 Long Paper.
- **Input → output:** multi-turn designer conversation → game-script segments, code snippets and user guidance, demonstrated on poker-family games.
- **Evaluation:** interaction quality (guidance, logic, relevance, coherence, conciseness) plus code correctness measures F-ESR, F-Acc, ESR and Acc.
- **Official sources:** [ACL Anthology](https://aclanthology.org/2025.acl-long.218/), [arXiv](https://arxiv.org/abs/2408.09386).
- **Availability:** **Closed.** The paper defines experiments, but no official data/model/evaluator package was verified.
- **纳入理由 / Inclusion:** 目标是通过对话持续构建游戏逻辑与代码，不是让 LLM 参加扑克比赛。
- **中文：** 将游戏开发建模为人和 LLM 的多轮交互，每轮共同产生脚本、代码和操作指引。
- **English:** *ChatGE treats game development as a multi-turn human–LLM process that emits game scripts, code, and designer guidance.*

### 17. ScriptDoctor — Automatic Generation of PuzzleScript Games via LLMs and Tree Search

- **Year / venue:** 2025, IEEE CoG 2025.
- **Input → output:** textual generation prompts and prior failure feedback → complete PuzzleScript games repaired over as many as ten trials using compiler, control-flow-graph and BFS-solver feedback.
- **Evaluation:** compilation rate, existence of a solver solution, and strict success where all levels are solvable with solution length over ten; BFS cap is one million states.
- **Official sources:** [paper](https://arxiv.org/abs/2506.06524), [IEEE DOI](https://doi.org/10.1109/COG64752.2025.11114269), [upstream PuzzleScript engine](https://github.com/increpare/PuzzleScript).
- **Availability:** **Closed for paper reproduction.** The upstream engine is public, but no author release of ScriptDoctor or its 610-game experimental corpus was verified.
- **纳入理由 / Inclusion:** 自动编译、静态分析、求解和修复共同构成完整游戏生成闭环。
- **中文：** LLM 生成 PuzzleScript 后，根据编译、控制流和求解失败反复自修，直到获得可解游戏。
- **English:** *ScriptDoctor repeatedly repairs generated PuzzleScript games using compiler, CFG, and BFS-solver feedback.*

### 18. Cardiverse — Harnessing LLMs for Novel Card Game Prototyping

- **Year / venue:** 2025, EMNLP 2025.
- **Input → output:** graph-indexed mechanic variations → executable card-game code and prototypes; gameplay records are used to validate implementations.
- **Evaluation:** mechanic similarity/novelty and user ratings; code pass@3 generation success and execution consistency; gameplay-AI tournaments are auxiliary validation.
- **Official artifacts:** [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1511/), [arXiv](https://arxiv.org/abs/2502.07128), [code/data](https://github.com/danruili/Cardiverse).
- **Availability:** **Open.** MIT-licensed code, examples and evaluation CLIs are public.
- **纳入理由 / Inclusion:** 核心贡献是新卡牌机制和可执行原型生成；self-play 用于验证/优化生成设计，而非论文最终目标。
- **中文：** 从机制图谱提出新卡牌规则，生成可执行代码，再用运行记录和锦标赛验证原型。
- **English:** *Cardiverse proposes novel card mechanics, generates executable prototypes, and validates them with gameplay records and tournaments.*

### 19. A Text-to-Game Engine for UGC-Based Role-Playing Games (Zagii)

- **Year / status:** 2024, revised 2025, arXiv preprint.
- **Input → output:** simple text → RPG narrative, characters, environment, visual/audio assets and game mechanics generated at runtime.
- **Evaluation:** product usage, playability and engagement statistics; the paper acknowledges the lack of a public dataset and baseline.
- **Official sources:** [paper](https://arxiv.org/abs/2407.08195), [official product](https://rpggo.ai/).
- **Availability:** **Closed.** An accessible product is not a reproducible benchmark; there is no public code, fixed test set or evaluator.
- **纳入理由 / Inclusion:** 明确以 text-to-game 为系统目标并生成玩法机制，而非只做 RPG 对话。
- **中文：** 从简短文本实时生成 RPG 的故事、角色、场景、视听资产和玩法机制。
- **English:** *Zagii turns short text into runtime-generated RPG narratives, characters, environments, assets, and mechanics.*

### 20. OpenGame — Open Agentic Coding for Games

- **Year / status:** 2026, arXiv technical report.
- **Input → output:** one natural-language brief and an empty workspace → a complete multi-file Phaser/TypeScript browser game with generated visual/audio assets.
- **Method/evaluation:** an evolving Template Skill, living Debug Skill and GameCoder-27B; evaluated on the 150-task OpenGame-Bench with BH/VU/IA scores.
- **Official artifacts:** [paper](https://arxiv.org/abs/2604.18394), [project](https://yelonlft.github.io/OpenGame-landing-page/), [framework and demo source](https://github.com/leigest519/OpenGame).
- **Availability:** **Partial.** The Apache-2.0 framework and runnable demo source archives are usable with external models, but GameCoder-27B, the training data and complete benchmark evaluator are not released.
- **纳入理由 / Inclusion:** 输出完整多文件网页游戏，正面解决场景 wiring、资源注册和跨文件一致性。
- **中文：** 用可积累的项目模板和调试协议，从单提示自主搭建并修复完整 Phaser 网页游戏。
- **English:** *OpenGame builds and repairs complete multi-file Phaser games from one prompt using reusable templates and a living debug protocol.*

### 21. CreativeGame — Toward Mechanic-Aware Creative Game Generation

- **Year / status:** 2026, arXiv report/preprint; no accepted venue is claimed here.
- **Input → output:** prompt or source-game concept plus parent version and lineage memory → a new HTML5 game, explicit mechanic plan/delta and version trace.
- **Evaluation:** 71 lineages, 88 saved nodes and a 774-mechanic archive; CreativeProxyReward combines mechanic realization, structural change, novelty and runtime robustness. Reported LLM-rated creativity/playability scores are not human-validated.
- **Official artifacts:** [paper](https://arxiv.org/abs/2604.19926), [project](https://yiweishi-cn.github.io/CreativeEvolutionGame/), [demo repository](https://github.com/yiweishi-cn/CreativeEvolutionGame), [OpenReview record](https://openreview.net/forum?id=VtmBAGCN7o).
- **Availability:** **Partial demo only.** The static repository exposes four four-version playable lineages, not the reported 6,181-line Python pipeline, 71 lineages, internal prompt library or evaluator.
- **纳入理由 / Inclusion:** 独特点在于把 mechanics 当作显式的规划、保留、变异和评测对象，而不只做换皮。
- **中文：** 通过机制增量规划、运行时验证和谱系记忆，让 HTML5 游戏跨版本持续演化。
- **English:** *CreativeGame evolves HTML5 games across versions by planning mechanic deltas, validating runtime behavior, and reusing lineage memory.*

### 22. UniGen — 90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development

- **Year / status:** 2025, arXiv preprint; the PDF labels an ICSE 2026 manuscript but contains placeholder DOI/bibliographic fields, so no venue acceptance is asserted here.
- **Input → output:** natural-language requirement → Unity blueprint, C# runtime/editor scripts, bound components, constructed scene and runnable 3D prototype via planning, generation, automation and debugging agents.
- **Evaluation:** three prototypes (Obstacle Run, Coin Collection and Haunted Jaunt); binary interaction matrices yield 100%, 93.8% and 89.5% functional completeness; manual comparison reports development time from about 140 to under 12 minutes.
- **Official artifacts:** [paper](https://arxiv.org/abs/2509.26161), [code](https://github.com/yxwan123/UniGen).
- **Availability:** **Partial.** A small pipeline release is public, but the evaluated Unity projects, interaction matrices, assets and full evaluator are not included.
- **纳入理由 / Inclusion:** 直接自动完成 Unity C# 编写、场景装配和组件绑定，而非只输出孤立代码片段。
- **中文：** 四类 agents 把文字需求转成已装配、可运行的 Unity 3D 游戏原型。
- **English:** *UniGen converts a natural-language brief into a runnable Unity prototype by generating C# code and automating scene/component assembly.*

### 23. GUI Agents for Continual Game Generation (Play2Code)

- **Year / status:** 2026, arXiv preprint.
- **Input → output:** game prompt → browser game; a GUI agent then plays each build and sends observations/fix lists back to the coding agent for up to five rounds with shared memory.
- **Evaluation:** on 200 PlaytestArena tasks, the paper reports a 66.8% rubric pass rate, +37.1 points over single-pass generation and +14.6 over an agentic-coding baseline; scores rise across play–code rounds.
- **Official artifacts:** [paper](https://arxiv.org/abs/2605.28258), [project](https://continual-game-generation.vercel.app/), [eight-demo repository](https://github.com/RunRiotComeOn/gui-agents-for-continual-game-generation).
- **Availability:** **Partial.** Playable demos are public, but the full system, tasks and evaluator are not.
- **纳入理由 / Inclusion:** GUI agent 的“玩”是对生成物的自动测试和修复信号，不是研究如何在现有游戏中取得高分。
- **中文：** 让 GUI 试玩代理把实际交互故障反馈给 coding agent，形成持续生成—试玩—修复闭环。
- **English:** *Play2Code turns GUI playtest observations into iterative code repairs, making game generation a continual play–code loop.*

### 24. Boardwalk — Towards a Framework for Creating Board Games with LLMs

- **Year / venue:** 2025, SBGames 2025.
- **Input → output:** anonymized natural-language rules for 12 board games → Python implementations, both free-form and against the Boardwalk API; models also adapt free-form code to the API.
- **Evaluation:** playability and rule compliance, success rate, and error analysis across Claude 3.7 Sonnet, DeepSeek-V3 and GPT-4o, including popular and obscure games.
- **Official artifacts:** [paper](https://arxiv.org/abs/2508.16447), [conference DOI](https://doi.org/10.5753/sbgames.2025.10222), [Boardwalk API/examples](https://github.com/LabCRAIG/boardwalk).
- **Availability:** **Partial.** The API and examples are public, but the complete 12-game experiment outputs and evaluator suite are not in the repository.
- **纳入理由 / Inclusion:** 直接考察“自然语言规则到可玩的数字桌游代码”，并通过匿名化降低背诵现成实现的影响。
- **中文：** 要求 LLM 把匿名化桌游规则实现成可玩 Python 游戏，并检查规则一致性。
- **English:** *Boardwalk tests whether LLMs can implement playable Python board games from anonymized natural-language rules.*

### 25. Automatic Bug Detection in LLM-Powered Text-Based Games Using LLMs

- **Year / venue:** 2024, Findings of ACL 2024.
- **Input → output:** LLM-powered text-game specifications, states and interaction traces → detected logic/consistency bugs.
- **Evaluation:** controlled bug-detection experiments reported in the paper; the work is verification rather than game-playing policy learning.
- **Official source:** [ACL Anthology](https://aclanthology.org/2024.findings-acl.907/).
- **Availability:** **Closed.** No author code/data/evaluator release was verified.
- **纳入理由 / Inclusion:** 属于“与生成强相关的自动验证”，应标成辅助 verification paper，而不是端到端生成器。
- **中文：** 用 LLM 自动发现 LLM 驱动文字游戏中的状态与逻辑缺陷，为生成游戏提供质量保障。
- **English:** *This work uses LLMs to detect logic and consistency bugs in LLM-powered text games as a generation-verification aid.*

### 26. AutoUE — Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems

- **Year / venue:** 2026, Findings of ACL 2026 (acceptance stated in the arXiv record).
- **Input → output:** natural-language brief decomposed into scene and gameplay descriptions → asset retrieval, PCG scene, C++ gameplay/interaction code and a complete runnable Unreal Engine game.
- **Evaluation:** PlayGen-20; scene/gameplay/visual scoring plus engine-native graph/module/interaction checks and automated runtime screenshots/logs.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.07106), [code](https://github.com/Pluto156/AutoUE), [dataset and generated demo games](https://huggingface.co/datasets/Pluto156/AutoUE_DataSet).
- **Availability:** **Open, environment-heavy.** Reproduction requires UE5 and API keys; LLM judging is variable.
- **纳入理由 / Inclusion:** 从需求到商业引擎完整 3D 游戏、C++ 逻辑和自动试玩，完整覆盖目标范围。
- **中文：** 多智能体在 UE5 内联合生成场景、玩法模块和交互代码，并自动运行测试成品。
- **English:** *AutoUE turns a natural-language brief into a complete UE5 game with generated scenes, C++ gameplay code, interactions, and runtime tests.*

### 27. Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models

- **Year / status:** 2026, arXiv preprint.
- **Input → output:** developer requests and multimodal engine context → Unity/Unreal/Godot edits, executable artifacts and compiler/runtime/human-feedback trajectories for training world models.
- **Evaluation:** UnitySceneBench has 720 training, 80 validation and 200 test examples; reports Unity asset classification/generation, held-out Unity and Unity-to-Unreal/Godot transfer, plus embodied diagnostics.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.25518), [preview code/checkpoint release](https://github.com/LanceZPF/cardinal-preview).
- **Availability:** **Partial.** The paper says a checkpoint and reproduction materials are released, but the full trajectory engine and all engine datasets are not a turnkey public benchmark.
- **纳入理由 / Inclusion:** 核心是通过真实游戏引擎开发产生可验证代码/场景轨迹；后续 embodied-agent 结果是下游用途，不是主任务。
- **中文：** 把游戏引擎中的生成、编译、运行和人工反馈轨迹作为可验证训练数据引擎。
- **English:** *This work treats executable game-development trajectories and engine feedback as verifiable data for training world models.*

### 28. Lottery and Sprint Arcade — Enabling Player-Driven Game Editing with Generative AI

- **Year / venue:** 2026, Journal of the Society for Art and Science, 25(2).
- **Input → output:** in-play voice commands → LLM-translated structured updates to roughly 100 configuration fields of a Space-Invaders-like game, modifying mechanics, visuals, interactions and audio.
- **Evaluation:** user study with subjective experience, NASA-TLX workload and editing-log analysis; it evaluates co-editing rather than general from-scratch generation.
- **Official source:** [paper](https://arxiv.org/abs/2607.10711).
- **Availability:** **Closed.** No official system, study data or evaluator release was verified.
- **纳入理由 / Inclusion:** 属于受限但明确的自然语言游戏编辑；应标成 co-creation 邻接项，不能等同于通用端到端生成。
- **中文：** 玩家边玩边用语音修改玩法和表现参数，形成自然语言驱动的迭代游戏共创。
- **English:** *The system lets players alter mechanics and presentation during play by mapping voice commands to structured game-configuration edits.*

## C. Boundary case: learned playable engines / 边界项：可交互生成引擎

### 29. Playable Game Generation

- **Year / status:** 2024, arXiv preprint.
- **Input → output:** game video and action data → an action-conditioned latent-dynamics model that emits real-time playable video frames rather than source code or engine projects.
- **Evaluation:** visual fidelity, dynamics/action alignment, long-horizon consistency and real-time playability experiments.
- **Official artifacts:** [paper](https://arxiv.org/abs/2412.00887), [official implementation](https://github.com/GreatX3/Playable-Game-Generation).
- **Availability:** **Partial/Open for the released learned-engine pipeline.** The official repository provides implementation material, but this is not a requirement-to-code benchmark and training-data reproducibility must be checked separately.
- **纳入理由 / Inclusion:** 仅作为边界记录：它确实“生成可玩的游戏体验”，但输出是动作条件视频世界，不是含显式规则和源码的游戏工程。
- **中文：** 学习一个可实时操作的生成式游戏引擎，但不产出传统游戏代码或项目文件。
- **English:** *Playable Game Generation produces an action-conditioned, real-time learned game engine, not an executable source-code project.*

## D. Explicit exclusions / 明确排除

- **AgentOdyssey** ([paper](https://arxiv.org/abs/2606.24893)): although it procedurally creates long-horizon text games, its principal purpose is to train/evaluate test-time continual-learning **playing agents**, so it is outside this repository's generation-only core.
- **MarioGPT / Word2Minecraft / VGLC / most PCG level benchmarks:** valuable for level/content generation, but they do not produce a complete game with new rules and executable development artifacts; keep them out of the end-to-end table.
- **Genie, GameNGen, DIAMOND, Oasis, GameGen-X, Matrix-Game, Hunyuan-GameCraft and similar world models:** action-conditioned interactive generation is not the same as producing code, rules, scenes and assets that a conventional engine executes. They belong in a separately labeled learned-engine/world-model section, never in the coding-agent leaderboard.
- **Game-playing benchmarks and agents** such as Atari score suites, MineDojo/BALROG-style play evaluation, Pokémon agents, Diplomacy agents and text-game reasoning agents are excluded regardless of whether they use LLMs.

## E. Comparison cautions / 对比注意

1. **From-scratch generation and repository editing are different tasks.** GameCraft-Bench/OpenGame-Bench/V-GameGym begin from briefs; GameDevBench/GameEngineBench modify existing projects. Their headline scores are not directly comparable.
2. **Deterministic engine tests and LLM/VLM judges must be separated.** GameDevBench and GameEngineBench emphasize behavior tests; GameCraft-Bench, V-GameGym, OpenGame-Bench and PlayGen-20 cover visual/experience dimensions but depend on judge versions.
3. **A released framework does not imply a released benchmark.** OpenGame is runnable while its 150-task evaluation pipeline remains pending; Play2Code and CreativeGame currently expose demos rather than their full research pipelines.
4. **“Compiles” is weaker than “playable,” and “playable” is weaker than “good.”** Robust reports should show build/runtime success, specification/mechanic correctness, and presentation/player-experience scores separately.
5. **Engine and license dependencies matter.** Unreal/Unity SDK access, proprietary assets, browser automation, API keys and version-locked Godot projects can make an otherwise open benchmark expensive or legally constrained to reproduce.
