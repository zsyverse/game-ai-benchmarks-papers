# End-to-end game generation: verified primary sources

> Research cutoff / 检索截止: **2026-09-04 (Asia/Shanghai)**.

This dossier contains exactly the **39 canonical records** in the public end-to-end index: 10 formal generation benchmarks and 29 direct generation methods.

本底稿与公开端到端索引严格一一对应，共 **39 条 canonical 记录**：10 条正式生成 benchmark 与 29 条直接生成方法。

Every numbered dossier record corresponds to the same public ID. Only direct generation methods and formal generation benchmarks appear here; rejected candidates are documented solely in the strict audit.

每条底稿记录与同编号公开条目对应。这里只保留直接生成方法与正式生成 benchmark；被拒候选仅记录在严格审计中。

## Generation benchmarks / 生成 Benchmark

### 1. V-GameGym (SKYLENAGE-GameCodeGym)

- **Year / status:** 2025, arXiv preprint.
- **Input → output:** natural-language requirements → runnable Pygame projects; the paper/README report 2,219 human-checked samples in 100 thematic clusters, while the downloadable JSONL contains 2,218 rows.
- **Evaluation:** weighted code, static-screenshot and dynamic-gameplay/video judge scores; also reports quality bands and solved-game counts.
- **Official artifacts:** [paper](https://arxiv.org/abs/2509.20136), [project/leaderboard](https://v-gamegym.github.io/), [code](https://github.com/alibaba/SKYLENAGE-GameCodeGym), [dataset](https://huggingface.co/datasets/alibabagroup/SKYLENAGE-GameCodeGym), [released-size record](https://datasets-server.huggingface.co/size?dataset=alibabagroup%2FSKYLENAGE-GameCodeGym).
- **Availability:** **Open.** Test data and generation, execution, recording and evaluation pipeline are public; judge-model dependence remains.
- **纳入理由 / Inclusion:** 直接评测“自然语言需求到可运行游戏代码”，而不是游戏玩家代理。
- **中文：** 用三模态执行证据评测大模型从需求生成完整 Pygame 游戏的能力；论文报告 2,219 条，当前发布数据为 2,218 行。
- **English:** *V-GameGym evaluates requirement-to-runnable-Pygame generation with code, screenshot, and gameplay-video evidence; the paper reports 2,219 samples and the release contains 2,218 rows.*

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
- **Official artifacts/timeline:** [paper](https://arxiv.org/abs/2607.03525), [paper-linked repository](https://github.com/Nitrode-Research/GameEngineBench), [task-tree URL](https://github.com/Nitrode-Research/GameEngineBench/tree/main/tasks_unreal), [results-tree URL](https://github.com/Nitrode-Research/GameEngineBench/tree/main/results). On Aug 29 the repository exposed 15 `ue_task_*` packages and no complete result bundle; on Aug 31 the repository and both tree URLs returned 404 through the Web, GitHub API and repository search.
- **Availability:** **Closed — official repository unavailable at the cutoff.** The 15/110 partial snapshot is retained as a dated observation, not presented as an artifact that remained downloadable on Aug 31.
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

### 7. OpenGame / OpenGame-Bench — Open Agentic Coding for Games

- **Year / status:** 2026, introduced in the OpenGame arXiv report.
- **Input → output:** 150 natural-language prompts in five web-game genres → complete browser games from empty workspaces; three random seeds per task.
- **Evaluation:** Build Health (BH), Visual Usability (VU: pixel heuristics plus VLM) and Intent Alignment (IA: weighted per-requirement VLM verdict), all on a 0–100 scale after headless-browser execution.
- **Official artifacts:** [paper](https://arxiv.org/abs/2604.18394), [project](https://yelonlft.github.io/OpenGame-landing-page/), [framework and demo sources](https://github.com/leigest519/OpenGame).
- **Availability:** **Partial.** The framework and runnable demo sources are public, but the README says the evaluation pipeline “will be released soon”; the 150 tasks/evaluator and GameCoder-27B weights are not downloadable at the cutoff.
- **纳入理由 / Inclusion:** 是端到端网页游戏生成评测，但必须区分“OpenGame 框架已开源”和“OpenGame-Bench 尚未完整发布”。
- **中文：** 在真实浏览器中同时评测生成游戏的构建健康、视觉可用性与需求对齐。
- **English:** *OpenGame-Bench scores browser-game agents on build health, visual usability, and intent alignment, though its full task/evaluator release is pending.*

### 8. Play2Code / PlaytestArena — GUI Agents for Continual Game Generation

- **Year / status:** 2026, introduced in *GUI Agents for Continual Game Generation* (arXiv preprint).
- **Input → output:** 200 browser-game generation prompts across eight genres plus observable gameplay rubrics → generated games and GUI-agent playtest verdicts.
- **Evaluation:** rubric pass rate from a GUI agent that opens and plays the game without source-code or internal-state access; the paper validates agreement against humans on a stratified 32-game subset.
- **Official artifacts:** [paper](https://arxiv.org/abs/2605.28258), [project](https://continual-game-generation.vercel.app/), [official demo gallery](https://github.com/RunRiotComeOn/gui-agents-for-continual-game-generation).
- **Availability:** **Partial.** Eight playable demos are public, but the 200 tasks, arena implementation, Play2Code system and evaluator are not in the official repository.
- **纳入理由 / Inclusion:** 将“可玩”落实为 GUI agent 的真实试玩证据，并把结果用于下一轮代码修复。
- **中文：** 用 GUI 代理实际游玩 200 个浏览器游戏任务，以可观察 rubric 评测并驱动持续修复。
- **English:** *PlaytestArena evaluates 200 browser-game tasks through real GUI play, and its feedback powers iterative code repair in Play2Code.*

### 9. AutoUE / PlayGen-20 — Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems

- **Year / venue:** 2026, Findings of ACL 2026 (acceptance stated in the paper's arXiv record).
- **Input → output:** 20 natural-language 3D-game briefs (5 easy, 7 medium, 8 hard) → complete Unreal Engine scenes, PCG graphs, C++ gameplay/interaction modules and runnable games.
- **Evaluation:** Scene, Gameplay and Visual scores weighted 0.35/0.35/0.30; additional graph/module/interaction metrics; runtime commands execute inside Unreal and collect screenshots/logs.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.07106), [code](https://github.com/Pluto156/AutoUE), [dataset, 20 demo games, assets and experimental data](https://huggingface.co/datasets/Pluto156/AutoUE_DataSet).
- **Availability:** **Open, environment-heavy.** Apache-2.0 code and data are public; Unreal Engine and external API keys are required, and judge scores are non-deterministic.
- **纳入理由 / Inclusion:** 目前最直接的“自然语言到商业引擎完整 3D 游戏 + runtime test”评测之一。
- **中文：** 在 UE5 中端到端生成场景、C++ 玩法代码和交互对象，并用运行时证据评测。
- **English:** *PlayGen-20 evaluates natural-language-to-complete-UE5 generation, including scenes, C++ gameplay code, interactions, and runtime playtests.*

### 10. WebGameBench

- **Priority / year:** P0; 2026, arXiv preprint.
- **Input → output:** 111 frozen Structured WebGame Specifications → source artifacts that must build, serve and run as browser-accessible games; the paper evaluates 12 coding agents under 14 configurations.
- **Evaluation:** an actual browser assigns Excellent, Usable or Unusable; the Usable-rate label is checked against independent human gameplay review. The best reported configuration reaches 76.9% usable but 20.2% excellent.
- **Official source:** [paper](https://arxiv.org/abs/2605.17637).
- **Availability:** **Closed.** No official 111-task package, deployment/runtime evaluator, human-review subset or repository was linked publicly at the cutoff.
- **纳入理由 / Inclusion:** 评分对象是 coding agent 交付的可运行游戏应用，而不是源码片段或玩现成游戏的能力。
- **中文：** WebGameBench 用真实构建、部署和浏览器交互评测 111 个“需求到游戏应用”任务，但公开论文尚未配套可下载 benchmark。
- **English:** *WebGameBench evaluates 111 requirement-to-browser-game tasks at the delivered-application level, but its task and runtime-evaluator artifacts are not public.*

## Generation methods / 生成方法

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

### 15. ScriptDoctor — Automatic Generation of PuzzleScript Games via LLMs and Tree Search

- **Year / venue:** 2025, IEEE CoG 2025.
- **Input → output:** textual generation prompts and prior failure feedback → complete PuzzleScript games repaired over as many as ten trials using compiler, control-flow-graph and BFS-solver feedback.
- **Evaluation:** compilation rate, existence of a solver solution, and strict success where all levels are solvable with solution length over ten; BFS cap is one million states.
- **Official sources:** [paper](https://arxiv.org/abs/2506.06524), [IEEE DOI](https://doi.org/10.1109/COG64752.2025.11114269), [upstream PuzzleScript engine](https://github.com/increpare/PuzzleScript).
- **Availability:** **Closed.** The upstream engine is public, but no author release of ScriptDoctor or its 610-game experimental corpus was verified; the engine alone is not a paper artifact.
- **纳入理由 / Inclusion:** 自动编译、静态分析、求解和修复共同构成完整游戏生成闭环。
- **中文：** LLM 生成 PuzzleScript 后，根据编译、控制流和求解失败反复自修，直到获得可解游戏。
- **English:** *ScriptDoctor repeatedly repairs generated PuzzleScript games using compiler, CFG, and BFS-solver feedback.*

### 16. Cardiverse — Harnessing LLMs for Novel Card Game Prototyping

- **Year / venue:** 2025, EMNLP 2025.
- **Input → output:** graph-indexed mechanic variations → executable card-game code and prototypes; gameplay records are used to validate implementations.
- **Evaluation:** mechanic similarity/novelty and user ratings; code pass@3 generation success and execution consistency; gameplay-AI tournaments are auxiliary validation.
- **Official artifacts:** [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1511/), [arXiv](https://arxiv.org/abs/2502.07128), [code/data](https://github.com/danruili/Cardiverse).
- **Availability:** **Open.** MIT-licensed code, examples and evaluation CLIs are public.
- **纳入理由 / Inclusion:** 核心贡献是新卡牌机制和可执行原型生成；self-play 用于验证/优化生成设计，而非论文最终目标。
- **中文：** 从机制图谱提出新卡牌规则，生成可执行代码，再用运行记录和锦标赛验证原型。
- **English:** *Cardiverse proposes novel card mechanics, generates executable prototypes, and validates them with gameplay records and tournaments.*

### 17. A Text-to-Game Engine for UGC-Based Role-Playing Games (Zagii)

- **Year / status:** 2024, revised 2025, arXiv preprint.
- **Input → output:** simple text → RPG narrative, characters, environment, visual/audio assets and game mechanics generated at runtime.
- **Evaluation:** product usage, playability and engagement statistics; the paper acknowledges the lack of a public dataset and baseline.
- **Official sources:** [paper](https://arxiv.org/abs/2407.08195), [official product](https://rpggo.ai/).
- **Availability:** **Closed.** An accessible product is not a reproducible benchmark; there is no public code, fixed test set or evaluator.
- **纳入理由 / Inclusion:** 明确以 text-to-game 为系统目标并生成玩法机制，而非只做 RPG 对话。
- **中文：** 从简短文本实时生成 RPG 的故事、角色、场景、视听资产和玩法机制。
- **English:** *Zagii turns short text into runtime-generated RPG narratives, characters, environments, assets, and mechanics.*

### 18. CreativeGame — Toward Mechanic-Aware Creative Game Generation

- **Year / status:** 2026, arXiv report/preprint; no accepted venue is claimed here.
- **Input → output:** prompt or source-game concept plus parent version and lineage memory → a new HTML5 game, explicit mechanic plan/delta and version trace.
- **Evaluation:** 71 lineages, 88 saved nodes and a 774-mechanic archive; CreativeProxyReward combines mechanic realization, structural change, novelty and runtime robustness. Reported LLM-rated creativity/playability scores are not human-validated.
- **Official artifacts:** [paper](https://arxiv.org/abs/2604.19926), [project](https://yiweishi-cn.github.io/CreativeEvolutionGame/), [demo repository](https://github.com/yiweishi-cn/CreativeEvolutionGame), [OpenReview record](https://openreview.net/forum?id=VtmBAGCN7o).
- **Availability:** **Partial demo only.** The static repository exposes four four-version playable lineages, not the reported 6,181-line Python pipeline, 71 lineages, internal prompt library or evaluator.
- **纳入理由 / Inclusion:** 独特点在于把 mechanics 当作显式的规划、保留、变异和评测对象，而不只做换皮。
- **中文：** 通过机制增量规划、运行时验证和谱系记忆，让 HTML5 游戏跨版本持续演化。
- **English:** *CreativeGame evolves HTML5 games across versions by planning mechanic deltas, validating runtime behavior, and reusing lineage memory.*

### 19. UniGen — 90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development

- **Year / status:** 2025, arXiv preprint; the PDF labels an ICSE 2026 manuscript but contains placeholder DOI/bibliographic fields, so no venue acceptance is asserted here.
- **Input → output:** natural-language requirement → Unity blueprint, C# runtime/editor scripts, bound components, constructed scene and runnable 3D prototype via planning, generation, automation and debugging agents.
- **Evaluation:** three prototypes (Obstacle Run, Coin Collection and Haunted Jaunt); binary interaction matrices yield 100%, 93.8% and 89.5% functional completeness; manual comparison reports development time from about 140 to under 12 minutes.
- **Official artifacts:** [paper](https://arxiv.org/abs/2509.26161), [code](https://github.com/yxwan123/UniGen).
- **Availability:** **Partial.** A small pipeline release is public, but the evaluated Unity projects, interaction matrices, assets and full evaluator are not included.
- **纳入理由 / Inclusion:** 直接自动完成 Unity C# 编写、场景装配和组件绑定，而非只输出孤立代码片段。
- **中文：** 四类 agents 把文字需求转成已装配、可运行的 Unity 3D 游戏原型。
- **English:** *UniGen converts a natural-language brief into a runnable Unity prototype by generating C# code and automating scene/component assembly.*

### 20. Boardwalk — Towards a Framework for Creating Board Games with LLMs

- **Year / venue:** 2025, SBGames 2025.
- **Input → output:** anonymized natural-language rules for 12 board games → Python implementations, both free-form and against the Boardwalk API; models also adapt free-form code to the API.
- **Evaluation:** playability and rule compliance, success rate, and error analysis across Claude 3.7 Sonnet, DeepSeek-V3 and GPT-4o, including popular and obscure games.
- **Official artifacts:** [paper](https://arxiv.org/abs/2508.16447), [conference DOI](https://doi.org/10.5753/sbgames.2025.10222), [Boardwalk API/examples](https://github.com/LabCRAIG/boardwalk).
- **Availability:** **Partial.** The API and examples are public, but the complete 12-game experiment outputs and evaluator suite are not in the repository.
- **纳入理由 / Inclusion:** 直接考察“自然语言规则到可玩的数字桌游代码”，并通过匿名化降低背诵现成实现的影响。
- **中文：** 要求 LLM 把匿名化桌游规则实现成可玩 Python 游戏，并检查规则一致性。
- **English:** *Boardwalk tests whether LLMs can implement playable Python board games from anonymized natural-language rules.*

### 21. Instruction-Driven Game Engines on Large Language Models (IDGE)

- **Priority / year:** P0; 2024, with the later [Poker case study](https://arxiv.org/abs/2410.13441) treated as the same family.
- **Input → output:** free-form poker rules, current state and player actions → autoregressive next states for customizable poker variants.
- **Evaluation:** 200 in-domain rounds over variants of ten prototype games and 50 out-of-domain rounds over five scripts; reports round-level success and state/function accuracy.
- **Official artifacts:** [main paper](https://arxiv.org/abs/2404.00276), [paper-linked repository](https://github.com/gingasan/idge), plus paper-linked video demos.
- **Availability:** **Partial.** The repository tree contains only `README.md` and `data/train.zip`; it does not release the engine, curriculum-training implementation, test harness or reported outputs.
- **纳入理由 / Inclusion:** 模型充当按用户规则执行状态转移的游戏引擎；最终产物不是扑克玩家策略。
- **中文：** IDGE 从自然语言扑克规则和动作生成下一游戏状态，但官方仓库目前只给训练数据压缩包，不能复现引擎。
- **English:** *IDGE executes natural-language poker rules through next-state generation, but its official repository releases only a training-data archive rather than the engine pipeline.*

### 22. Word2World

- **Priority / year:** P0; 2024, arXiv preprint.
- **Input → output:** story prompt → story, narrative objectives, tile placement and a runnable 2D tile game through iterative feedback.
- **Evaluation:** LLM-based story/world coherence and objective placement, plus conventional PCG path/connectivity checks; compares LLMs and ablates pipeline stages.
- **Official artifacts:** [paper](https://arxiv.org/abs/2405.06686), [code and examples](https://github.com/umair-nasir14/Word2World).
- **Availability:** **Open, API/OS dependent.** Apache-2.0 code, configs and playable examples are public; the documented setup supports Windows and OpenAI APIs.
- **纳入理由 / Inclusion:** 它联合生成故事、目标、地图与可运行游戏体验，不只是孤立叙事或静态资产。
- **中文：** Word2World 把故事分步变成叙事目标、连贯 tile 世界和可运行 2D 游戏，并用 LLM 与路径检查迭代修正。
- **English:** *Word2World turns stories into coherent tile worlds and playable 2D games through LLM feedback and conventional path checks.*

### 23. Mechanic Maker — Accessible Game Development Via Symbolic Learning Program Synthesis

- **Priority / year:** P0; 2024, AIIDE 2024.
- **Input → output:** continuous valid example-frame sequences supplied by a user → symbolically synthesized rules that reproduce the demonstrated state transitions.
- **Evaluation:** human-subject study across programming/game-development experience; Frame Error against reference transitions, task completion, free-play analysis and motivation/usability surveys.
- **Official source:** [paper](https://arxiv.org/abs/2410.01096).
- **Availability:** **Closed.** No official Mechanic Maker application/source, frame/event logs, final games, study data or reproduction scripts were verified.
- **纳入理由 / Inclusion:** 最终输出是由示例合成的可执行游戏机制；用户研究而非玩家得分是主要验证。
- **中文：** Mechanic Maker 让用户用状态帧示例而非代码表达机制，再由符号程序合成系统生成规则。
- **English:** *Mechanic Maker synthesizes executable mechanics from user-demonstrated frame transitions, lowering the programming barrier to game design.*

### 24. Grammar and Gameplay-Aligned RL for Game Description Generation (RLGDG)

- **Priority / year:** P0; 2025, IEEE Conference on Games 2025.
- **Input → output:** natural-language game descriptions → executable Ludii programs via SFT followed by GRPO.
- **Evaluation:** grammar-prefix validity, Ludii compatibility, functionality and concept fidelity; compares SFT, RL reward variants and the full two-stage method.
- **Official artifacts:** [paper](https://arxiv.org/abs/2503.15783), [training/data/evaluation code](https://github.com/tsunehiko/rlgdg).
- **Availability:** **Open, environment-heavy.** MIT code includes preprocessing, SFT/GRPO recipes and evaluation; users obtain Ludii separately and need Docker/GPU resources.
- **纳入理由 / Inclusion:** 直接训练模型从文字描述生成兼顾语法和玩法概念的完整可执行规则程序。
- **中文：** RLGDG 用语法奖励和玩法概念奖励后训练 LLM，使自然语言到 Ludii 游戏描述同时更可编译、更忠于玩法。
- **English:** *RLGDG combines SFT and grammar/gameplay rewards to generate Ludii programs that are both executable and concept-faithful.*

### 25. STORY2GAME

- **Priority / year:** P0; 2025, arXiv preprint.
- **Input → output:** generated story → populated world state, action preconditions/effects and engine action code; player-requested unseen actions can trigger new state attributes and revisions of prior actions.
- **Evaluation:** per-sentence/action compilation, percentage of fully compiled stories, and compilation/commonsense-semantic success for 90 dynamically generated actions.
- **Official artifacts:** [paper](https://arxiv.org/abs/2505.03547), [first-author code, prompts, samples and results](https://github.com/foxanon183/Story2Game).
- **Availability:** **Open, API dependent.** The public repository includes the game builder, dynamic-action notebooks, prompts, story skeletons and result files; API credentials are required.
- **纳入理由 / Inclusion:** 同时生成故事、状态表示和可执行动作逻辑，并用能否完整交互通关检验生成物。
- **中文：** STORY2GAME 从故事自动建立世界状态与动作代码，还能在玩家提出新动作时动态扩展引擎。
- **English:** *STORY2GAME generates an interactive-fiction world and executable action logic, then extends both when players request unseen actions.*

### 26. Multi-Agent Game Generation and Evaluation via Audio-Visual Recordings

- **Priority / year:** P0; 2025, arXiv preprint.
- **Input → output:** a content description and multimedia asset bank → multiple JavaScript games/animations, audio-visual recordings, relative evaluations and iteratively revised candidates.
- **Evaluation:** AVR-Eval distinguishes good from broken/mismatched content and compares candidates by pairwise win rate; AVR-Agent is compared with one-shot generation.
- **Official artifacts:** [paper](https://arxiv.org/abs/2508.00632), [AVR-Agent/AVR-Eval repository](https://github.com/SamsungSAILMontreal/AVR-Eval-Agent).
- **Availability:** **Open, environment-heavy.** MIT code, prompts, task CSVs and paper experiment scripts are public; Chromium/Xvfb/PulseAudio/FFmpeg and model APIs/GPUs are required, and asset licenses require manual downloads.
- **纳入理由 / Inclusion:** AVR 中的试玩录像服务于生成游戏的选择和修复，而不是评价一个玩游戏 agent 的成绩。
- **中文：** AVR-Agent 生成多版 JavaScript 游戏，再让全模态 evaluator 看带声音的实际录屏选优并反馈迭代。
- **English:** *AVR-Agent generates JavaScript games and uses omni-modal comparisons of recorded gameplay audio/video to select and revise candidates.*

### 27. Automated Unity Game Template Generation from GDDs

- **Priority / year:** P0; 2025, arXiv preprint.
- **Input → output:** Game Design Documents → extracted specifications and Unity-compatible C# templates implementing core mechanics, systems and architecture.
- **Evaluation:** compilation success, GDD adherence, best-practice adoption and code modularity across game genres; the paper reports an average 4.8/5.0 for the fine-tuned model.
- **Official artifacts:** [paper](https://arxiv.org/abs/2509.08847), [synthetic GDD/code data](https://huggingface.co/datasets/AmnaHassan/Unity-Engine-CSharp-Code-and-Game-Design-Document-Code-Pairs-Mix-and-Jam), [real-GDD pairs](https://huggingface.co/datasets/AmnaHassan/Real-Game-Design-Documents-With-AI-Generated-Code-Pairs), [paper-linked fine-tuned model endpoint](https://huggingface.co/AmnaHassan/llama3-unity-gdd-finetuned).
- **Availability:** **Partial.** The two datasets are anonymously accessible. The model endpoint returns 401 to anonymous access at the cutoff, so it is not counted as publicly downloadable; the end-to-end parser/generator, custom Unity integration package, evaluation prompts and scored outputs are also absent.
- **纳入理由 / Inclusion:** 系统目标是把设计文档落成 Unity 机制和工程代码，而不是只摘要 GDD。
- **中文：** 该框架把 GDD 解析成结构化规格并生成 Unity C# 模板；两套数据公开，但模型匿名访问为 401，整套生成器也未发布。
- **English:** *The work maps GDDs to Unity C# templates; two datasets are public, while the tuned-model endpoint rejects anonymous access and the generator is unreleased.*

### 28. Real-Time World Crafting

- **Priority / year:** P0; 2025, Wordplay @ EMNLP 2025.
- **Input → output:** natural-language behavior request → a constrained DSL that safely configures a custom ECS at runtime for spells or cellular automata.
- **Evaluation:** Gemini/GPT/Claude model and prompting comparisons, validated LLM-judge ratings, inference latency, bidirectional translation and human-pilot analysis.
- **Official artifacts:** [paper](https://arxiv.org/abs/2510.16952), [demo source, playable artifact, analysis code and data](https://github.com/austin-the-drake/real-time-world-crafting-wordplay-demo).
- **Availability:** **Open, API dependent.** The MIT repository includes GameMaker source, experiment prompts/code, CSV/database data and analyses; an API key is required for live generation.
- **纳入理由 / Inclusion:** 用户语言被编译成受限但可执行的游戏行为和机制，而不是角色动作策略。
- **中文：** Real-Time World Crafting 用受限 DSL 和 ECS 把自然语言安全地变成运行时法术或元胞行为。
- **English:** *Real-Time World Crafting compiles natural language into a constrained DSL that safely creates new ECS game behaviors at runtime.*

### 29. Mortar — Evolving Mechanics for Automatic Game Design

- **Priority / year:** P0; 2026, arXiv preprint.
- **Input → output:** archived mechanics plus LLM mutations → a quality-diversity archive whose candidates are composed by tree search into complete games.
- **Evaluation:** each mechanic's contribution to preserving a skill-based ordering over players, game diversity/playability, system ablations and a human study.
- **Official source:** [paper](https://arxiv.org/abs/2601.00105).
- **Availability:** **Closed.** No official implementation, prompts, mechanic archive, composed games, player approximators or evaluator was verified.
- **纳入理由 / Inclusion:** self-play/tree search 只是设计 fitness；最终研究对象是演化机制和组合出的完整游戏。
- **中文：** Mortar 用 LLM 与质量多样性搜索演化机制，再把机制组合成完整游戏，以技能排序和人评检验。
- **English:** *Mortar evolves mechanics with an LLM/QD loop and evaluates them inside complete games through skill ordering and human feedback.*

### 30. RuleSmith

- **Priority / year:** P0; 2026, arXiv preprint.
- **Input → output:** CivMini's multidimensional rule space and self-play traces → interpretable parameter configurations that reduce faction win-rate disparities.
- **Evaluation:** Bayesian-optimization convergence, acquisition-based sample allocation, balance metrics and evaluation of a pre-optimized configuration.
- **Official artifacts:** [paper](https://arxiv.org/abs/2602.06232), [project](https://adonis-galaxy.github.io/RuleSmith-website/), [code](https://github.com/Adonis-galaxy/RuleSmith).
- **Availability:** **Open.** MIT code includes CivMini, LLM agents, self-play, optimization/evaluation scripts, visualization and an optimized `theta.json` example.
- **纳入理由 / Inclusion:** multi-agent play 是规则设计 evaluator；核心输出是可直接应用的平衡规则配置。
- **中文：** RuleSmith 用 LLM 自博弈估计平衡度，再以贝叶斯优化寻找可解释、可落地的 CivMini 规则参数。
- **English:** *RuleSmith uses LLM self-play as a design evaluator and Bayesian optimization to emit directly applicable balanced-rule parameters.*

### 31. GamED.AI

- **Priority / year:** P0; 2026, ACL 2026 System Demonstrations.
- **Input → output:** instructor-provided educational question → game concept, mechanic contract, scenes/content/assets and an assembled playable web game through six hierarchical phases.
- **Evaluation:** 200 questions over five domains; 90% internal FOL-validator pass rate, 98.3% schema compliance, 73% token reduction, cost/latency reporting and 50 curated games.
- **Official artifacts:** [paper](https://arxiv.org/abs/2604.23947), [ACL demo record](https://doi.org/10.18653/v1/2026.acl-demo.84), [live 50-game library](https://shivena99.github.io/GamED-AI/acl-demo/library/), [code](https://github.com/ShivenA99/GamED-AI).
- **Availability:** **Open.** MIT backend/frontend source, agent prompts, deterministic validators, generation CLI and 50 static game artifacts are public; generation uses external APIs.
- **纳入理由 / Inclusion:** 直接从教师问题生成完整可玩教育游戏；内部 validator 衡量架构合规，不应误写成独立教学效果 benchmark。
- **中文：** GamED.AI 用分阶段 agents、机制契约和确定性质量门，在一分钟内把问题生成网页教育游戏。
- **English:** *GamED.AI turns educational questions into playable web games through hierarchical agents, mechanic contracts and deterministic quality gates.*

### 32. Distilling Game Code World Model Generation into Lightweight LLMs

- **Priority / year:** P0; 2026, arXiv preprint.
- **Input → output:** natural-language rules for 30 perfect/imperfect-information games → executable Python GameCWMs implementing legal actions, transitions, observations and rewards.
- **Evaluation:** structural/semantic verifier and behavioral scenarios; compares base Qwen2.5-3B, SFT and SFT+RLVR for syntax and execution-level rule adherence.
- **Official artifacts:** [paper](https://arxiv.org/abs/2605.24375), [code/data repository](https://github.com/tktserapio/internalizing-cwm-sft-grpo).
- **Availability:** **Open.** The repository exposes 30 rule/golden-code pairs, SFT data, generated samples, training code, reward functions and behavioral evaluation; it does not claim a downloadable trained checkpoint.
- **纳入理由 / Inclusion:** 论文主要产物是从规则生成可执行游戏环境及其 verifier，而不是用 CWM 提高玩家成绩。
- **中文：** 该工作把 30 款游戏的自然语言规则蒸馏进小模型，使其生成可执行 Python 状态转移环境。
- **English:** *This work distills natural-language-to-executable GameCWM generation into a 3B model and releases the 30-game data and verifier pipeline.*

### 33. The Verifier is the Curriculum

- **Priority / year:** P0; 2026, arXiv preprint.
- **Input → output:** GameCraft briefs and strict-launch-filtered candidates → successive LoRA-distilled 14B generators for complete Godot projects.
- **Evaluation:** four unseen families; per-candidate clean launch rises from 8.8% to 42.2%, best-of-K coverage from 18/25 to 25/25, with gold-duplication, quantity/quality and lenient-filter controls.
- **Official source:** [paper](https://arxiv.org/abs/2607.09709).
- **Availability:** **Closed.** No official LoRA/checkpoint, accepted/rejected candidate set, self-distillation scripts or experiment outputs were verified. The separately public GameCraft-Bench is upstream infrastructure, not a release of this method.
- **纳入理由 / Inclusion:** 研究训练的是完整游戏代码生成器；strict-launch 是生成 curriculum/verifier，不是玩游戏任务。
- **中文：** 该方法只用 Godot 严格启动信号做自蒸馏，显著提高未见游戏族的干净启动率，但方法工件尚未公开。
- **English:** *Strict-launch-gated self-distillation improves out-of-family Godot generation, but the trained adapters, data and method code are unreleased.*

### 34. MAGIC

- **Priority / year:** P0; 2026, arXiv preprint.
- **Input → output:** one natural-language prompt → transition-aware IR, furnished scenes, portal scripts and one runnable multi-scene Unity project.
- **Evaluation:** 100 multi-scene cases; execution-based transition agent reports 0.99 precision, 0.95 recall and 0.96 F1, with portal recovery and navigability comparisons.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.11594), [generation/evaluation code](https://github.com/sereneee1201/MAGIC).
- **Availability:** **Partial, environment-heavy.** The pipeline and evaluator are public with example ground truth; the README says the complete 100-case benchmark is available only upon request. Unity, Blender, API access and about 23 GB of third-party objects are required.
- **纳入理由 / Inclusion:** 输出是含多场景、脚本与真实 portal 运行验证的完整工程，不是单场景资产生成。
- **中文：** MAGIC 从一个提示生成连通多场景 Unity 工程，并让 evaluator 实际穿越 portal；代码公开但 100-case 基准未直接下载。
- **English:** *MAGIC builds runnable connected multi-scene Unity projects and executes portal transitions, while its full 100-case benchmark remains request-only.*

### 35. General Video Game Rule Generation

- **Priority / year:** P0; 2019, arXiv/competition-framework paper.
- **Input → output:** a fixed game level → VGDL rules via random, constructive or search-based generators in the GVGAI rule-generation track.
- **Evaluation:** early comparison of playability/interestingness and expressive diversity; constructive rules are more consistently playable while search generates more diverse but uneven rulesets.
- **Official artifacts:** [paper](https://arxiv.org/abs/1906.05160), [exact GVGAI rule-generation source](https://github.com/GAIGResearch/GVGAI/tree/master/src/tracks/ruleGeneration).
- **Availability:** **Open.** The official framework contains the API, runner and all three generator implementations; this is not merely a link to the broader playing-agent tracks.
- **纳入理由 / Inclusion:** 它专门定义从关卡反推可执行规则的 generation track，补齐了完整 GVGAI multitrack 论文无法替代的规则生成记录。
- **中文：** 该工作给定关卡生成 VGDL 规则，并公开 random、constructive、search 三种规则生成器。
- **English:** *General Video Game Rule Generation defines a level-to-VGDL-rule task and releases the exact random, constructive and search generators.*

### 36. Mechanic Maker 2.0

- **Priority / year:** P0; 2023, AIIDE 2023.
- **Input → output:** an open Unity automatic-game-design environment → generated platform-game rules evaluated by learned RL or static A* player approximators.
- **Evaluation:** compares the distinct rule sets induced by RL and A* evaluation and examines which outputs may be more usable by humans.
- **Official artifacts:** [paper](https://arxiv.org/abs/2309.09476), [full Unity project](https://github.com/Harcurio/MechanicMiner).
- **Availability:** **Open, environment-heavy.** The repository contains the Unity rule-generation project, rule JSON, results and trained ONNX agents. It is a different system from 2024 Mechanic Maker.
- **纳入理由 / Inclusion:** RL 的作用是评价候选规则；最终生成物仍是新的游戏规则集。
- **中文：** Mechanic Maker 2.0 重建开放 Unity 规则生成框架，并比较 RL 与 A* 评价器如何改变生成规则分布。
- **English:** *Mechanic Maker 2.0 releases a Unity rule generator and studies how learned RL versus A* evaluators shape its generated mechanics.*

### 37. Open Role-Playing with Delta-Engines

- **Priority / year:** P1; 2024, arXiv preprint.
- **Input → output:** a fixed base engine and natural-language growth choices → incremental role-code deltas produced by an LLM neural proxy.
- **Evaluation:** 100-role execution rate, GPT-4 code-correctness rate, generated-data analysis and ten-person human–AI co-design in Free Pokémon.
- **Official artifacts:** [paper](https://arxiv.org/abs/2408.05842), [official Free Pokémon repository](https://github.com/gingasan/delta-engine/tree/main/free-pokemon).
- **Availability:** **Open for the case study.** Engine/UI code, prompts, train/test role script-code pairs and a LoRA download link are public; this does not establish a general from-scratch generator.
- **纳入理由 / Inclusion:** 最终输出是新增角色能力和运行时机制代码；agent play 仅帮助验证这些机制。
- **中文：** Delta-Engine 在固定 base engine 上按玩家语言逐步添加角色代码，实现可扩展的运行时机制共创。
- **English:** *Delta-Engine incrementally adds role code and mechanics from natural-language growth choices within the released Free Pokémon case study.*

### 38. DreamGarden — A Designer Assistant for Growing Games from a Single Prompt

- **Year / venue:** 2025, ACM CHI 2025.
- **Input → output:** one high-level dream/memory/idea → a hierarchical plan and implemented Unreal Engine game environment; designers can seed, prune and give feedback.
- **Evaluation:** HCI system analysis and user study rather than an automatic coding benchmark.
- **Official sources:** [paper](https://arxiv.org/abs/2410.01791), [ACM DOI](https://doi.org/10.1145/3706598.3714233).
- **Availability:** **Closed.** No complete official Unreal system, fixed tasks or evaluator release was verified.
- **纳入理由 / Inclusion:** 直接研究单提示到 Unreal 游戏环境的规划、实现与人机共创工作流。
- **中文：** 把一个高层创意拆成层级计划，并由专门模块在 Unreal 中逐步长成游戏环境。
- **English:** *DreamGarden decomposes one high-level prompt into a hierarchical plan whose modules grow an Unreal game environment with designer feedback.*

### 39. Game Development as Human–LLM Interaction (ChatGE)

- **Year / venue:** 2025, ACL 2025 Long Paper.
- **Input → output:** multi-turn designer conversation → code segments progressively assembled into a complete `CustomGame` and executed for play, demonstrated on poker-family games.
- **Evaluation:** interaction quality (guidance, logic, relevance, coherence, conciseness), fragment-level F-ESR/F-Acc, and whole-game ESR/Acc.
- **Official sources:** [ACL Anthology](https://aclanthology.org/2025.acl-long.218/), [arXiv](https://arxiv.org/abs/2408.09386).
- **Availability:** **Closed.** The paper defines experiments, but no official data/model/evaluator package was verified.
- **纳入理由 / Inclusion:** 目标是通过对话增量构建并执行完整游戏，不是让 LLM 参加扑克比赛。
- **中文：** 将游戏开发建模为人和 LLM 的多轮交互，代码片段逐步组成完整 `CustomGame` 并执行试玩。
- **English:** *ChatGE incrementally assembles generated code segments into a complete executable `CustomGame` and evaluates both fragment-level and whole-game correctness.*
