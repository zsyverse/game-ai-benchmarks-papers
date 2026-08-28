# AI Game Generation / Game-Development Agents: verified primary sources

> 检索截止：2026-08-29（Asia/Shanghai）。本文件只收录可直接访问的一手来源：论文官网、arXiv / PMLR / ACL Anthology / OpenReview、作者项目页和官方代码仓库。
> Scope: text-to-game, game/level/code generation, coding agents for game engines, and action-conditioned playable world models.

## How to read the reproducibility label / “真正可评测”口径

- **Yes**：公开了任务/数据与可运行的 evaluator 或训练/推理代码，第三方原则上可以得到同定义的分数。
- **Partial**：公开了部分工件（如模型、数据、规范或推理代码），但缺任务、隐藏测试、生成成品、完整评分器或必要资产中的一部分。
- **No**：是重要 paper/demo/tool，但没有公开、固定的 benchmark protocol + artifacts；不能把它当成 benchmark 排名。

## 1. Public benchmarks and datasets / 公开基准与数据集

### PCG Benchmark — The Procedural Content Generation Benchmark

- **Type:** benchmark + tool
- **Year / venue:** 2025, Foundations of Digital Games (FDG 2025)
- **Task:** 用统一 Gym-like API 比较 content generators；当前仓库覆盖 Arcade Rules、Binary maze、Dangerous Dave、Isaac、Lode Runner、MiniDungeons、SMB、Sokoban、Talakat、Zelda 等问题/变体。
- **Metrics:** `quality`（通过问题质量约束的内容比例）、`diversity`（彼此足够不同的比例）、`controllability`（满足给定控制条件的比例）；各 problem 还返回逐样本 0–1 details。
- **Primary sources:** [paper (arXiv)](https://arxiv.org/abs/2503.21474), [ACM DOI](https://doi.org/10.1145/3723498.3723794), [official framework](https://github.com/amidos2006/pcg_benchmark), [official experiment code](https://github.com/amidos2006/benchmark_experiments)
- **Truly evaluable:** **Yes.** MIT-licensed evaluator、problem definitions 和 baseline experiments 均公开。

### VGLC — The Video Game Level Corpus

- **Type:** dataset + paper
- **Year / venue:** 2016, 7th Workshop on Procedural Content Generation
- **Task:** 以易解析的 text/tile formats 提供经典游戏关卡，用于 level-generation training/evaluation。
- **Metrics:** 数据集本身不规定统一指标；研究通常自行报告 playability、tile-pattern divergence、novelty/diversity 等，因此不同论文的数值不可默认横比。
- **Primary sources:** [paper](https://arxiv.org/abs/1606.07487), [official corpus](https://github.com/TheVGLC/TheVGLC)
- **Truly evaluable:** **Partial.** 数据公开，但它是 corpus，不是带固定 evaluator/leaderboard 的 benchmark。

### V-GameGym (SKYLENAGE-GameCodeGym)

- **Type:** benchmark + dataset + tool + paper
- **Year / status:** 2025, arXiv preprint
- **Task:** 从 natural-language requirements 生成可运行 Pygame；2,219 个经人工检查的样本、100 个 thematic clusters，来自 2,190 个 repositories。
- **Metrics:** code、static screenshot、dynamic gameplay/video 三模态 judge 分数的加权和；另报告 0–40 / 40–60 / 60–80 / 80–100 quality bands 与 solved-game count。
- **Primary sources:** [paper](https://arxiv.org/abs/2509.20136), [official project/leaderboard](https://v-gamegym.github.io/), [official code](https://github.com/alibaba/SKYLENAGE-GameCodeGym), [official dataset](https://huggingface.co/datasets/alibabagroup/SKYLENAGE-GameCodeGym)
- **Truly evaluable:** **Yes.** 公开 test set、generation/execution/evaluation pipeline 和媒体录制工具；LLM/VLM judge 仍带模型依赖与非确定性。

### GameDevBench — Evaluating Agentic Capabilities Through Game Development

- **Type:** benchmark + dataset + paper
- **Year / venue:** 2026, ICML 2026（官方仓库标注）
- **Task:** 333 个 Godot 4.4.1 repository-editing tasks，来自 web/video tutorials；覆盖 2D/3D graphics & animation、UI、gameplay logic，并测试 coding agent 使用 screenshot/video feedback 的能力。
- **Metrics:** deterministic Godot tests 的 **pass@1 / task success rate**；不是 CLIP 或 VLM judge proxy。
- **Primary sources:** [paper](https://arxiv.org/abs/2602.11103), [official project](https://waynechi.com/gamedevbench), [official code/tasks/results](https://github.com/waynchi/gamedevbench)
- **Truly evaluable:** **Yes.** 333 task archives、runner、validator、结果与固定 Godot version 均公开。

### GameCraft-Bench — Can Agents Build Playable Games End-to-End in a Real Game Engine?

- **Type:** benchmark + dataset + paper
- **Year / status:** 2026, arXiv preprint
- **Task:** 140 个自然语言到完整 Godot game 的任务，跨 15 个 game families；agent 还需提交 replayable input traces，验证器实际启动并回放游戏。
- **Metrics:** build gate × weighted rubric score；四类为 **Core Mechanics (0.15)、Content Depth (0.35)、Functional Visuals (0.15)、Art and Presentation (0.35)**，由 replay video/frames 上的 multimodal judge 评分。
- **Primary sources:** [paper](https://arxiv.org/abs/2606.17861), [official project/demos](https://tongxuluo.github.io/gamecraft-bench-website/), [official code/data/tasks](https://github.com/FreedomIntelligence/gamecraft-bench)
- **Truly evaluable:** **Yes, environment-heavy.** 任务与 verifier 已公开；需 Godot 4.6.2、Linux UI tooling 及 judge API，LLM judge 不是完全确定性。

### GameEngineBench — Evaluating Coding Agents on Real C++ Runtime Environments

- **Type:** benchmark + dataset + paper
- **Year / status:** 2026, arXiv preprint
- **Task:** 9 个真实 Unreal Engine 5 repositories 中的 110 个 scoped native-C++ tasks，涉及 gameplay、replication、AI/world orchestration、animation、UI/session、persistence、XR 和 rendering plugins。
- **Metrics:** hidden Unreal automation behavioral tests 的 **pass@1**；编译通过但 runtime contract 不满足仍算失败。
- **Primary sources:** [paper](https://arxiv.org/abs/2607.03525), [official code/tasks/results](https://github.com/Nitrode-Research/GameEngineBench)
- **Truly evaluable:** **Yes, with caveats.** runner/tasks/tests 公开，但需本地 Unreal Engine；部分 EOS tasks 还需从 Epic 获取 SDK。

### GameXpert-Bench — How Far Are Coding Agents from Expert Game Development?

- **Type:** benchmark + paper
- **Year / status:** 2026, arXiv preprint
- **Task:** 三条 lifecycle tracks：**GameGen**（97 个从空 workspace 生成游戏的任务，11 genres）、**GameFix**（50 个 human-verified game levels 构造的 100 tasks，每题 19–27 injected bugs）、**GameOpt**（17 条六轮 optimization chains，共 102 requests）。
- **Metrics:** GameGen 为 Completeness、Richness、Player Experience、Visual Quality 四项等权总分；GameFix 用 Fail-to-Pass + Pass-to-Pass tests、bug-fixed ratio、近满分 survival-curve 的 **Strict** 与 self-discovery **Cliff**；GameOpt 评 gameplay/level/balance/art/UI/audio 并做 regression checks。
- **Primary sources:** [paper](https://arxiv.org/abs/2608.21833), [official repository](https://github.com/Kwen-Chen/GameXpert-Bench)
- **Truly evaluable:** **No as of the cutoff.** 官方 repository README 明示仍是 “public release scaffold”，paper、benchmark data、evaluation code 和 model artifacts 尚待加入；不要把论文中的 leaderboard 当作现已可复现。

### JamBench / JamSet (JAMER)

- **Type:** benchmark + dataset + paper
- **Year / status:** 2026, arXiv preprint
- **Task:** 从 game-jam repositories 构建 Godot project-level corpus；论文报告 8,133 verified projects，其中 300 为 JamBench、7,833 为 JamSet；含 theme-driven from-scratch generation 与 function/script/full-script completion。
- **Metrics:** L1/L2/L3a pass rates、**Structural Completeness Score (SCS)**、**Behavioral Alignment Score (BAS)**；后者对 deterministic input 下的 runtime behavior 与 reference 比较。
- **Primary source:** [paper](https://arxiv.org/abs/2606.19830)
- **Truly evaluable:** **No as of the cutoff.** 论文写称 code/data public，但其 arXiv source/HTML 没有给出可访问 artifact URL，GitHub/Hugging Face 也未定位到作者发布；应待官方链接出现后再升级状态。

### GameGen-Verifier / VeriGame

- **Type:** tool + dataset + paper
- **Year / status:** 2026, arXiv preprint
- **Task:** 将 game specification 拆成 verifiable keypoints，向 runtime 注入目标 state，再并行执行短交互验证；VeriGame 含 100 个、7 genres 的游戏规范。
- **Metrics:** 对 human specification-element judgments 的 **Acc@5, Prec@5, Rec@5, F1@5** 与 **Time@5**（5 runs）；论文报告最高 92.2% Acc@5 / 95.4% F1@5。
- **Primary sources:** [paper](https://arxiv.org/abs/2605.07442), [official implementation](https://github.com/NetX-lab/GameGen-Verifier)
- **Truly evaluable:** **Partial.** harness、100 specs 与 10 example descriptions 公开，但 README 明示完整 generated games、runs/logs/screenshots 未提交；可运行自生成示例，不能原样复核完整论文数据。

## 2. Game/code generation and development-agent papers / 生成与开发智能体论文

### Game Generation via Large Language Models

- **Type:** paper
- **Year / venue:** 2024, IEEE Conference on Games (CoG 2024)
- **Task:** 以 Video Game Description Language (VGDL) 同时生成 game rules 与 levels，研究不同 prompt context 组合。
- **Evaluation:** 论文实验验证生成流程，但没有发布固定 public test set、runner 或 leaderboard。
- **Primary sources:** [paper](https://arxiv.org/abs/2404.08706), [IEEE DOI](https://doi.org/10.1109/COG60054.2024.10645597)
- **Truly evaluable:** **No.** 关键方法论文，不是公开 benchmark。

### GAVEL — Generating Games via Evolution and Language Models

- **Type:** paper + tool + dataset
- **Year / venue:** 2024, NeurIPS 2024
- **Task:** 对 Ludii game-description code 训练 fill-in-the-middle CodeLlama，并以 MAP-Elites / quality-diversity search 自动产生新 board games。
- **Metrics:** QD score、playable archive cells、fitness > 0.5 cells，以及 Ludii semantic concepts 上的 novelty；论文另做 expert qualitative analysis。
- **Primary sources:** [paper](https://arxiv.org/abs/2407.09388), [official code/data](https://github.com/gdrtodd/gavel), [playable generated examples](https://ludii.games/library.php)
- **Truly evaluable:** **Yes for the paper pipeline.** 代码、Ludii fork、训练数据和 checkpoint links 公开；它不是通用 text-to-game leaderboard。

### DreamGarden — A Designer Assistant for Growing Games from a Single Prompt

- **Type:** paper + prototype/tool
- **Year / venue:** 2025, ACM CHI 2025
- **Task:** LLM planner 把一个高层 prompt 分解成 hierarchical plan，由 specialized modules 在 Unreal Engine 中实现；用户可 seed、prune、feedback。
- **Evaluation:** user study / HCI design evaluation，非自动 benchmark。
- **Primary sources:** [paper](https://arxiv.org/abs/2410.01791), [ACM DOI](https://doi.org/10.1145/3706598.3714233)
- **Truly evaluable:** **No.** 未发现作者公开完整 Unreal system、固定 task set 与 evaluator。

### GameGPT — Multi-agent Collaborative Framework for Game Development

- **Type:** paper
- **Year / status:** 2023 (revised 2025), arXiv preprint
- **Task:** 以 planning、task identification、implementation 的 multi-agent collaboration，配合 layered lexicons 与 code-generation decoupling，降低 hallucination/redundancy。
- **Evaluation:** framework/case-study paper；没有公开标准 benchmark artifacts。
- **Primary source:** [paper](https://arxiv.org/abs/2310.08067)
- **Truly evaluable:** **No.** 不能把同名非作者 GitHub 项目视作官方代码。

### Game Development as Human-LLM Interaction (ChatGE)

- **Type:** paper + prototype/tool
- **Year / venue:** 2025, ACL 2025 Long Paper
- **Task:** 对话式 Chat Game Engine；每轮生成 game-script segment、code snippet 与 user guidance，以 poker-family games 为 case study。
- **Metrics:** interaction quality（guidance/logic/relevance/coherence/conciseness）以及 code correctness 的 F-ESR、F-Acc、ESR、Acc。
- **Primary sources:** [ACL Anthology](https://aclanthology.org/2025.acl-long.218/), [arXiv](https://arxiv.org/abs/2408.09386)
- **Truly evaluable:** **No.** 论文有明确定义的实验，但未找到官方公开 data/model/evaluator package。

### ScriptDoctor — Automatic Generation of PuzzleScript Games via LLMs and Tree Search

- **Type:** paper + method
- **Year / venue:** 2025, IEEE CoG 2025
- **Task:** LLM 生成 PuzzleScript，循环利用 compiler errors、CFG errors 与 BFS playtesting feedback 修正；每次 trial 最多 10 次生成。
- **Metrics:** compilation rate、存在 solver solution 的比例、所有 levels 可解且 solution length > 10 的 success；BFS 上限 1M states。
- **Primary sources:** [paper](https://arxiv.org/abs/2506.06524), [IEEE DOI](https://doi.org/10.1109/COG64752.2025.11114269), [upstream PuzzleScript engine](https://github.com/increpare/PuzzleScript)
- **Truly evaluable:** **Partial/No.** 评测定义清楚，但未定位到作者发布的 ScriptDoctor implementation 和 610-game experiment corpus；PuzzleScript upstream 本身不等于论文代码。

### Cardiverse — Harnessing LLMs for Novel Card Game Prototyping

- **Type:** paper + tool + dataset
- **Year / venue:** 2025, EMNLP 2025
- **Task:** graph-indexed card-game mechanic variation、经 gameplay records 验证的 game-code generation，以及 self-play optimized heuristic ensemble gameplay AI。
- **Metrics:** mechanics similarity/novelty 与 user ratings；code generation 报 pass@3 generation success、execution consistency；gameplay AI 用 tournament/self-play outcomes。
- **Primary sources:** [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1511/), [arXiv](https://arxiv.org/abs/2502.07128), [official code/data](https://github.com/danruili/Cardiverse)
- **Truly evaluable:** **Yes for the released pipeline.** MIT code、example data、evaluation CLIs 可运行；它是 card-game prototyping system，不是跨引擎通用 benchmark。

### A Text-to-Game Engine for UGC-Based Role-Playing Games (Zagii)

- **Type:** paper + commercial prototype/tool
- **Year / status:** 2024/2025 revision, arXiv preprint
- **Task:** 由简单文本实时生成 RPG narrative、characters、environment、visual/audio assets 与 mechanics；论文报告 Zagii 支撑数百游戏和数万 sessions。
- **Evaluation:** product usage/playability/engagement statistics；论文明确指出缺公开 dataset 与 baseline。
- **Primary sources:** [paper](https://arxiv.org/abs/2407.08195), [official product site cited by paper](https://rpggo.ai/)
- **Truly evaluable:** **No.** 可体验产品不等于开放 benchmark；无固定 test set/evaluator/code。

## 3. Interactive world / video game generation / 可交互世界模型

### Genie — Generative Interactive Environments

- **Type:** paper + model research
- **Year / venue:** 2024, ICML 2024
- **Task:** 从无 action labels 的 Internet gameplay videos 学 latent actions、video tokenizer 与 dynamics model，再从单张 prompt image 生成可由隐动作控制的 2D platformer-like environment。
- **Metrics:** next-frame/token prediction与人类可玩性/controllability analyses；不是标准 game benchmark。
- **Primary sources:** [PMLR paper](https://proceedings.mlr.press/v235/bruce24a.html), [arXiv](https://arxiv.org/abs/2402.15391), [official project page](https://sites.google.com/view/genie-2024/home)
- **Truly evaluable:** **No.** 未公开训练数据、weights 或完整 inference code。

### GameNGen — Diffusion Models Are Real-Time Game Engines

- **Type:** paper + project demo
- **Year / status:** 2024, arXiv preprint
- **Task:** 先用 RL agent 收集 Doom trajectories，再训练 action-conditioned diffusion model，以约 20 FPS 模拟可交互 Doom。
- **Metrics:** visual quality（PSNR/LPIPS 等）、autoregressive stability 与 human study；不是公开 benchmark suite。
- **Primary sources:** [paper](https://arxiv.org/abs/2408.14837), [official project](https://gamengen.github.io/), [official project-page repository](https://github.com/GameNGen/GameNGen.github.io)
- **Truly evaluable:** **No.** 官方只公开论文/展示页；网上若干 reproduction repositories 不是作者 release。

### DIAMOND — Diffusion for World Modeling: Visual Details Matter in Atari

- **Type:** paper + tool/model
- **Year / venue:** 2024, NeurIPS 2024 Spotlight
- **Task:** 在 learned diffusion world model 中训练 RL agent；主要是 Atari 100k，并提供 playable pretrained Atari models 和 CSGO world-model branch。
- **Metrics:** Atari 100k agent returns / human-normalized aggregate performance，以及 world-model visual fidelity analyses。
- **Primary sources:** [paper](https://arxiv.org/abs/2405.12399), [official project](https://diamond-wm.github.io/), [official code/checkpoints](https://github.com/eloialonso/diamond)
- **Truly evaluable:** **Yes.** 训练/推理/play scripts、configs 和 pretrained models 公开；Atari ROM 使用者需自行确认许可。

### Oasis — A Universe in a Transformer

- **Type:** tool/model + technical project
- **Year / status:** 2024, Decart × Etched technical release
- **Task:** diffusion-transformer Minecraft-like world model，按 keyboard input autoregressively 生成 gameplay frames。
- **Metrics:** 官方 release 重点是实时交互 demo，不提供独立、固定 leaderboard protocol。
- **Primary sources:** [official project](https://oasis-model.github.io/), [official 500M inference code](https://github.com/etched-ai/open-oasis), [official weights](https://huggingface.co/Etched/oasis-500m)
- **Truly evaluable:** **Partial.** 500M weights 与 action-conditioned inference 公开，可实际生成；最强在线版本、训练代码/数据和标准 evaluator 未公开。

### GameGen-X — Interactive Open-world Game Video Generation

- **Type:** paper + dataset + tool
- **Year / venue:** 2025, ICLR 2025
- **Task:** diffusion transformer 同时做 text-to-game-video 与基于当前 clip/actions 的 interactive continuation；配套 OGameData。
- **Metrics:** video generation quality、temporal quality 与 action controllability（详见论文）；数据 release 主要提供 YouTube IDs/timestamps/captions，而非重新分发 raw videos。
- **Primary sources:** [OpenReview](https://openreview.net/forum?id=8VG8tpPZhe), [arXiv](https://arxiv.org/abs/2411.00769), [official code/data metadata](https://github.com/GameGen-X/GameGen-X), [official project](https://gamegen-x.github.io/)
- **Truly evaluable:** **Partial.** OGameData metadata/subsets 与实现仓库公开，但原视频受 URL 存活/版权影响，模型 release 完整度需以仓库当前状态为准；不是固定 benchmark。

### Matrix-Game series

- **Type:** paper + dataset + tool/model
- **Year / status:** 2025–2026, arXiv preprints / open-source releases
- **Task:** keyboard/mouse-conditioned interactive video world generation；1.0 提出 Matrix-Game 与 Minecraft dataset，2.0 强调 real-time streaming，3.0 加 long-horizon memory 与 720p real-time generation。
- **Metrics:** video fidelity/temporal consistency、action controllability、inference speed/latency 与 long-horizon consistency；不同版本不可直接按一个分数横比。
- **Primary sources:** [1.0 paper](https://arxiv.org/abs/2506.18701), [2.0 paper](https://arxiv.org/abs/2508.13009), [3.0 paper](https://arxiv.org/abs/2604.08995), [official unified repository](https://github.com/SkyworkAI/Matrix-Game)
- **Truly evaluable:** **Partial/Yes for released inference.** 官方仓库含各版本实现；能否完整训练/复核论文表格取决于每版公开 weights/data 和硬件，不能等同于 turnkey benchmark。

### Hunyuan-GameCraft — High-dynamic Interactive Game Video Generation

- **Type:** paper + tool/model
- **Year / status:** 2025, arXiv preprint
- **Task:** 将 keyboard/mouse signals 统一到 camera representation，以 hybrid history conditioning 长序列生成高动态 interactive game video；训练覆盖 100+ AAA games 的百万级 gameplay recordings。
- **Metrics:** visual fidelity、dynamics/physical realism、action controllability、long-term consistency 与 inference efficiency（论文相对 baselines）。
- **Primary sources:** [paper](https://arxiv.org/abs/2506.17201), [official project](https://hunyuan-gamecraft.github.io/), [official code](https://github.com/Tencent-Hunyuan/Hunyuan-GameCraft-1.0), [official weights](https://huggingface.co/tencent/Hunyuan-GameCraft-1.0)
- **Truly evaluable:** **Partial/Yes for inference.** inference、checkpoints、Gradio 已公开（最低约 24GB VRAM，官方推荐 80GB）；训练集/训练 pipeline 未完整公开，且它不是 leaderboard benchmark。

## 4. Selection notes / 避坑说明

1. **“可玩 demo”不等于 benchmark。** Genie、GameNGen、Oasis、Hunyuan-GameCraft 等很重要，但若没有固定 tasks + evaluator，就应列为 paper/tool，而不是写进 benchmark leaderboard。
2. **world model 与 game-building agent 是不同任务。** 前者预测 pixels/latents under actions；后者要生成/修改 code、scenes、assets 并通过 engine/runtime tests。比较时应分榜。
3. **VLM/LLM judge 与 deterministic tests 应分开报告。** GameDevBench/GameEngineBench 的行为测试更可重复；GameCraft-Bench/V-GameGym 的视觉/体验维度覆盖更广，但依赖 judge model/version。
4. **数据可访问性需动态复核。** YouTube-ID datasets（如 OGameData）会 link-rot；Unreal/EOS/Atari 等还涉及引擎、SDK、ROM 或素材许可。
5. **截至检索日不要把 GameXpert-Bench、JamBench 标成“可下载”。** 两篇论文都描述了完整基准，但前者官方 repo 明示尚待 release，后者没有可核验 artifact URL。
