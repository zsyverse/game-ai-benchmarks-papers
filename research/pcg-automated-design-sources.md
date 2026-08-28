# Procedural content generation and automated game design: verified primary sources

> 检索截止 / Verified through: **2026-08-29** (Asia/Shanghai). This note is deliberately limited to systems that generate games, rules, mechanics, levels, or game-world components. It does **not** include agents whose task is only to play a game.

## Inclusion and status rules / 收录与开放性口径

- **Scope labels:** `full-game`, `rules`, `levels`, `components`, or `survey`. `components` means that the output does not by itself define playable rules or a complete game.
- **Open:** official paper plus sufficient author-released code/data/evaluator to run the central pipeline.
- **Partial:** a useful official artifact is public, but some training data, generated corpus, evaluator, historical code, or other essential piece is absent.
- **Paper-only:** a primary paper/proceedings page is public, but no official runnable release was located.
- RL papers appear only where the RL policy is the **content generator**. Procgen, CoinRun, ALE, MineRL agent tracks, GVGAI playing tracks, and other playing-only benchmarks are excluded.

## A. Complete games, rules, and mechanics / 完整游戏、规则与机制

### 1. An Experiment in Automatic Game Design

- **Year / venue:** 2008, IEEE CIG.
- **Scope:** `full-game`
- **Generated content:** small two-player games, including rules and board configurations.
- **Method:** evolutionary search over a game-description space, with learning agents used only as automatic design evaluators.
- **Evaluation:** fitness rewards games that are learnable yet non-trivial and distinguishes player skill; the paper inspects evolved playable games.
- **中文说明:** 这是用“会学习的代理之间是否能拉开水平”来评价并进化完整小游戏的早期代表作。
- **English summary:** A foundational experiment evolves complete games and scores them through differences between learning players.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2008.5035629)
- **Open status:** **Paper-only.** The publication is accessible, but no official historical implementation/data release was located.

### 2. Automatic Generation and Evaluation of Recombination Games (Ludi)

- **Year / venue:** 2008, Queensland University of Technology PhD thesis.
- **Scope:** `rules`
- **Generated content:** rule sets for abstract combinatorial board games expressed as ludemes.
- **Method:** Ludi evolves recombinations of rule building blocks and uses automated self-play measurements to score candidates.
- **Evaluation:** playability and heuristic qualities such as balance, depth, and decisiveness; the process produced human-playable games including Yavalath.
- **中文说明:** Ludi 把棋类规则拆成可重组的 ludeme，再通过自博弈筛掉无效或失衡的规则组合。
- **English summary:** Ludi evolves recombinations of rule primitives and filters them with automated play-based quality estimates.
- **Primary sources:** [official QUT repository record](https://eprints.qut.edu.au/17025/), [thesis PDF](https://eprints.qut.edu.au/17025/1/Cameron_Browne_Thesis.pdf), [Ludii successor platform](https://ludii.games/)
- **Open status:** **Partial.** The paper and successor Ludii ecosystem are public, but the original Ludi experiment is not packaged as a current reproducible benchmark.

### 3. Multi-faceted Evolution of Simple Arcade Games (ANGELINA)

- **Year / venue:** 2011, IEEE CIG.
- **Scope:** `full-game`
- **Generated content:** playable arcade games with mechanics, rules, and level layouts.
- **Method:** ANGELINA co-evolves several facets of a game rather than optimizing one fixed content type; automated play helps judge candidates.
- **Evaluation:** generated games are checked for functional play and examined as design artifacts; this is a system demonstration, not a fixed leaderboard.
- **中文说明:** ANGELINA 同时搜索机制与关卡等多个设计面，是“自动做游戏”而非单独画地图的经典系统。
- **English summary:** ANGELINA jointly evolves multiple facets of simple arcade games and evaluates them through automated play.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2011.6032019)
- **Open status:** **Paper-only.** No complete official release of this historical ANGELINA version was located.

### 4. The Micro-Rhetorics of Game-o-Matic

- **Year / venue:** 2012, Foundations of Digital Games (FDG).
- **Scope:** `full-game`
- **Generated content:** small playable arcade games intended to express relationships between real-world concepts.
- **Method:** Game-o-Matic maps a user-authored concept/relation graph to game-mechanic patterns, entities, rules, and presentation choices.
- **Evaluation:** close readings and generated examples assess whether the resulting interaction communicates the intended idea; there is no common automatic score.
- **中文说明:** Game-o-Matic 从概念关系图直接装配可玩的表达性小游戏，目标是让机制本身“表达观点”。
- **English summary:** Game-o-Matic turns conceptual relationship graphs into small playable, rhetorically expressive games.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/2282338.2282347)
- **Open status:** **Partial.** Primary paper and project evidence are public, but a maintained end-to-end generator/evaluator is not.

### 5. Mechanic Miner: Reflection-Driven Game Mechanic Discovery and Level Design

- **Year / venue:** 2013, EvoApplications.
- **Scope:** `rules`
- **Generated content:** new mechanics and levels designed to expose the consequences of those mechanics.
- **Method:** ANGELINA reflects on simulated play traces, searches for mechanically interesting rule changes, and constructs supporting levels.
- **Evaluation:** automated play distinguishes behaviours induced by candidate mechanics; the paper analyses generated mechanic/level examples.
- **中文说明:** Mechanic Miner 不只变异规则，还会反思玩法差异并生成能展示新机制的关卡。
- **English summary:** The system discovers mechanics through play-trace reflection and builds levels that make their effects visible.
- **Primary sources:** [Springer DOI](https://doi.org/10.1007/978-3-642-37192-9_29)
- **Open status:** **Paper-only.** No official runnable release was located.

### 6. Automatic Game Design via Mechanic Generation

- **Year / venue:** 2014, AAAI.
- **Scope:** `rules`
- **Generated content:** game mechanics/rules satisfying designer-provided requirements.
- **Method:** formal mechanic representations and search are combined with simulated execution to construct and test candidate designs.
- **Evaluation:** case-study games test whether generated mechanics realize target gameplay requirements and remain executable.
- **中文说明:** 该工作把机制写成可推理的形式模型，再搜索满足设计约束的规则，而不是让代理去玩固定游戏。
- **English summary:** Formalized mechanics are searched and simulated to synthesize rule sets that meet design requirements.
- **Primary sources:** [AAAI proceedings](https://doi.org/10.1609/aaai.v28i1.8788)
- **Open status:** **Paper-only.** The evaluation is documented, but no official complete code/data package was located.

### 7. A Rogue Dream: Automatically Generating Meaningful Content for Games (ANGELINA)

- **Year / venue:** 2014, AIIDE.
- **Scope:** `full-game`
- **Generated content:** complete small games whose mechanics, content, and framing are derived from topical source material.
- **Method:** ANGELINA selects concepts from news/current-affairs input, searches game designs, and assembles playable artifacts around a chosen theme.
- **Evaluation:** generated games are presented as creative case studies and assessed qualitatively rather than through a reusable benchmark.
- **中文说明:** 这一代 ANGELINA 会从现实主题出发自动选择概念、做机制并产出带意义表达的完整小游戏。
- **English summary:** ANGELINA converts topical source material into themed, playable games through autonomous design search.
- **Primary sources:** [AIIDE proceedings](https://doi.org/10.1609/aiide.v10i3.12745)
- **Open status:** **Paper-only.** Generated examples are documented, but the complete system is not released as a reproducible package.

### 8. Automated Game Design via Conceptual Expansion

- **Year / venue:** 2018 AIIDE; expanded treatment in 2021 IEEE Transactions on Games.
- **Scope:** `full-game`
- **Generated content:** novel games made by recombining learned representations of existing games.
- **Method:** conceptual expansion blends learned game graphs/components instead of relying on a hand-authored rule grammar.
- **Evaluation:** the system is asked to reconstruct held-out existing games, providing a measurable proxy before presenting novel recombinations.
- **中文说明:** Conceptual Expansion 从已有游戏中学习结构，再“概念混合”出新游戏，并先用复原已知游戏验证方法。
- **English summary:** Learned game representations are recombined through conceptual expansion and evaluated by reconstructing known games.
- **Primary sources:** [AIIDE paper](https://doi.org/10.1609/aiide.v14i1.13022), [arXiv](https://arxiv.org/abs/1809.02232), [journal article](https://doi.org/10.1109/TG.2021.3060005)
- **Open status:** **Paper-only.** No official end-to-end artifact package was located.

### 9. Orchestrating Game Generation

- **Year / venue:** 2018, IEEE Transactions on Games.
- **Scope:** `survey`
- **Generated content:** a system architecture for coordinating generators of rules, levels, visuals, audio, and other game facets.
- **Method:** proposes orchestration patterns and interfaces so heterogeneous generators can exchange constraints and feedback.
- **Evaluation:** synthesizes evidence from existing generation systems and design scenarios; it is an architecture/framework paper, not itself a benchmark.
- **中文说明:** 这篇工作解释如何让规则、关卡、图像等生成器协同，避免把“各做一个组件”误称为自动生成完整游戏。
- **English summary:** A framework organizes how specialized generators can coordinate to produce coherent multi-facet games.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TG.2018.2870876)
- **Open status:** **Paper-only.** This is a conceptual orchestration framework, not a released generator suite.

### 10. Puck: A Slow and Personal Automated Game Designer

- **Year / venue:** 2022, AIIDE.
- **Scope:** `full-game`
- **Generated content:** a personal, continuously evolving collection of small playable game designs.
- **Method:** Puck explores designs over long periods and incorporates a designer's ongoing interaction and preferences rather than optimizing a one-shot benchmark score.
- **Evaluation:** reflective longitudinal case study of generated games and the human–system relationship.
- **中文说明:** Puck 强调长期、个性化的自动设计过程，用持续积累的设计作品替代一次性生成排行榜。
- **English summary:** Puck slowly explores a personalized space of complete game designs in a longitudinal human–AI process.
- **Primary sources:** [AIIDE proceedings](https://doi.org/10.1609/aiide.v18i1.21968)
- **Open status:** **Paper-only.** The paper documents the system and artifacts, but no complete official reproducibility package was located.

### 11. Ludii – The Ludemic General Game System

- **Year / venue:** 2020, ECAI.
- **Scope:** `rules`
- **Generated content:** Ludii itself is a formal rule language, compiler/runtime, and game corpus; it is infrastructure for rule generation rather than a generator by itself.
- **Method:** games are composed from ludemes in a compact grammar, enabling automated execution, concept extraction, and downstream search such as GAVEL.
- **Evaluation:** coverage and faithful execution across a broad collection of traditional strategy games.
- **中文说明:** Ludii 是规则生成所依赖的“可执行游戏语言与语料库”，本身不要误标成自动生成算法。
- **English summary:** Ludii supplies an executable ludeme-based language and corpus on which rule-generation systems can search.
- **Primary sources:** [ECAI DOI](https://doi.org/10.3233/FAIA200120), [arXiv](https://arxiv.org/abs/1905.05013), [official platform/library](https://ludii.games/)
- **Open status:** **Partial.** The platform and game library are accessible, but the full current engine is distributed as an application rather than a complete open-source research stack.

### 12. GAVEL: Generating Games via Evolution and Language Models

- **Year / venue:** 2024, NeurIPS.
- **Scope:** `full-game`
- **Generated content:** executable two-player board games in the Ludii description language.
- **Method:** a fill-in-the-middle CodeLlama proposes Ludii code; MAP-Elites/quality-diversity search retains playable, fit, and conceptually diverse games.
- **Evaluation:** QD score, playable archive cells, cells above a fitness threshold, semantic-concept novelty, and expert qualitative review.
- **中文说明:** GAVEL 把代码大模型与 MAP-Elites 结合，真正搜索并输出可在 Ludii 中运行的新棋类游戏。
- **English summary:** GAVEL couples a Ludii code model with quality-diversity evolution to generate executable novel board games.
- **Primary sources:** [paper](https://arxiv.org/abs/2407.09388), [official code/data](https://github.com/gdrtodd/gavel), [official playable library](https://ludii.games/library.php)
- **Open status:** **Open.** Code, data preparation, Ludii fork, experiment configuration, and model links are author-released.

### 13. Grammar-Based Game Description Generation Using Large Language Models

- **Year / venue:** 2024, IEEE Transactions on Games.
- **Scope:** `rules`
- **Generated content:** machine-readable game descriptions generated from natural-language requirements.
- **Method:** first derives a minimal grammar from the GDL specification, then iteratively repairs LLM output with a parser that exposes valid prefixes and candidate symbols.
- **Evaluation:** grammatical validity and successful generation are compared with direct-LLM baselines; iterative grammar guidance significantly improves validity.
- **中文说明:** 该框架用语法约束逐步修复 LLM 生成的游戏规则代码，重点解决“看起来像代码但不能解析”。
- **English summary:** Grammar-guided iterative decoding turns natural-language requests into syntactically valid executable game descriptions.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TG.2024.3520214), [arXiv](https://arxiv.org/abs/2407.17404), [official code](https://github.com/tsunehiko/ggdg)
- **Open status:** **Open.** The authors publish the implementation and evaluation workflow.

### 14. Game Generation via Large Language Models

- **Year / venue:** 2024, IEEE Conference on Games (CoG).
- **Scope:** `full-game`
- **Generated content:** VGDL game rules together with levels.
- **Method:** an LLM is prompted with different combinations of game-language documentation and in-context examples.
- **Evaluation:** generated descriptions are checked for compilation/execution and playable structure across prompt conditions; no persistent leaderboard is provided.
- **中文说明:** 论文直接让 LLM 生成 VGDL 规则和关卡，并比较给多少语言文档与示例最有效。
- **English summary:** LLMs generate both VGDL rules and levels under different documentation and example contexts.
- **Primary sources:** [arXiv](https://arxiv.org/abs/2404.08706), [IEEE DOI](https://doi.org/10.1109/COG60054.2024.10645597)
- **Open status:** **Paper-only.** A fixed official task set, generator code, and evaluator package were not located.

### 15. ScriptDoctor: Automatic Generation of PuzzleScript Games via LLMs and Tree Search

- **Year / venue:** 2025, IEEE CoG.
- **Scope:** `full-game`
- **Generated content:** complete PuzzleScript rule files and puzzle levels.
- **Method:** an LLM iteratively revises a game using compiler errors, control-flow feedback, and BFS playtesting; each trial has a bounded repair budget.
- **Evaluation:** compilation rate, presence of a solver solution, and the stricter rate where every level is solvable with solution length greater than ten; BFS is capped at one million states.
- **中文说明:** ScriptDoctor 用编译器和求解器反馈循环“看病”，直到 PuzzleScript 游戏既能编译又有可解关卡。
- **English summary:** Compiler and tree-search feedback iteratively repair LLM-generated PuzzleScript games into solvable artifacts.
- **Primary sources:** [arXiv](https://arxiv.org/abs/2506.06524), [IEEE DOI](https://doi.org/10.1109/COG64752.2025.11114269), [official PuzzleScript runtime](https://github.com/increpare/PuzzleScript)
- **Open status:** **Partial.** The upstream runtime is open, but no official ScriptDoctor implementation and full experiment corpus were located.

### 16. Cardiverse: Harnessing LLMs for Novel Card Game Prototyping

- **Year / venue:** 2025, EMNLP.
- **Scope:** `full-game`
- **Generated content:** playable digital card-game variants, including mechanics and executable code.
- **Method:** graph-indexed mechanic variation, LLM code generation checked against gameplay records, and self-play-based heuristic assembly.
- **Evaluation:** mechanic similarity/novelty and user ratings; pass@3 generation success and execution consistency; tournaments for gameplay heuristics.
- **中文说明:** Cardiverse 不只是写卡牌文本，而是变异机制、生成可执行游戏代码并用对局记录验证。
- **English summary:** Cardiverse proposes novel card-game mechanics, compiles them into code, and validates behaviour through gameplay traces.
- **Primary sources:** [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1511/), [arXiv](https://arxiv.org/abs/2502.07128), [official code/data](https://github.com/danruili/Cardiverse)
- **Open status:** **Open.** Official code, examples, data, and evaluation commands are released.

## B. Level generation, datasets, and evaluation testbeds / 关卡生成、数据集与评测环境

### 17. The Procedural Content Generation Benchmark

- **Year / venue:** 2025, FDG.
- **Scope:** `levels`
- **Generated content:** a unified testbed spanning mazes, platform levels, dungeons, puzzles, bullet-hell patterns, and one arcade-rule problem.
- **Method:** Gym-like problem APIs standardize content, quality constraints, controls, and generator evaluation across domains.
- **Evaluation:** `quality`, pairwise-threshold `diversity`, and target-satisfaction `controllability`, plus per-sample 0–1 detail vectors.
- **中文说明:** 这是目前最直接的 PCG 算法统一 benchmark，把多个游戏内容域放进同一套质量、多样性、可控性接口。
- **English summary:** A common API evaluates generators across many PCG domains with quality, diversity, and controllability measures.
- **Primary sources:** [paper](https://arxiv.org/abs/2503.21474), [ACM DOI](https://doi.org/10.1145/3723498.3723794), [official framework](https://github.com/amidos2006/pcg_benchmark), [official experiments](https://github.com/amidos2006/benchmark_experiments)
- **Open status:** **Open.** MIT-licensed problems, evaluator, baselines, and experiments are public.

### 18. VGLC: The Video Game Level Corpus

- **Year / venue:** 2016, 7th Workshop on Procedural Content Generation.
- **Scope:** `levels`
- **Generated content:** VGLC does not generate content; it supplies machine-readable tile levels used to train and compare level generators.
- **Method:** canonical levels from several games are normalized into text/tile representations with game-specific metadata.
- **Evaluation:** no universal metric is prescribed; downstream papers use playability, tile-pattern similarity, novelty, and diversity, so scores are not automatically comparable.
- **中文说明:** VGLC 是 PCGML 最常用的关卡语料库之一，但它是数据集而不是带固定排行榜的 benchmark。
- **English summary:** VGLC standardizes classic tile levels for training PCGML systems but does not impose one evaluator.
- **Primary sources:** [paper](https://arxiv.org/abs/1606.07487), [official corpus](https://github.com/TheVGLC/TheVGLC)
- **Open status:** **Open as a dataset; Partial as a benchmark.** The corpus is public, while evaluation remains paper-specific.

### 19. The 2010 Mario AI Championship: Level Generation Track

- **Year / venue:** 2011, IEEE Transactions on Computational Intelligence and AI in Games.
- **Scope:** `levels`
- **Generated content:** Super Mario Bros.-style levels created online for a player.
- **Method:** the competition API lets generators condition content on player/gameplay information; submitted algorithms ranged from constructive to adaptive approaches.
- **Evaluation:** competition protocol and player studies compare generated levels using play experience/preferences and measured level characteristics.
- **中文说明:** 这一赛道把“为真实玩家现场生成 Mario 关卡”正式做成比赛，是后续平台关卡 benchmark 的重要起点。
- **English summary:** The championship formalized online Mario level generation and evaluated submissions with players and level statistics.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TCIAIG.2011.2166267)
- **Open status:** **Partial.** The protocol and results are primary-source documented, but the original full competition service/submissions are not maintained as a turnkey package.

### 20. General Video Game AI: A Multitrack Framework for Evaluating Agents, Games, and Content Generation Algorithms

- **Year / venue:** 2019, IEEE Transactions on Games.
- **Scope:** `levels`
- **Generated content:** VGDL levels and, in the generation tracks, content for many rule-defined games.
- **Method:** a common VGDL runtime separates game rules, level descriptions, generators, and automated players.
- **Evaluation:** the framework defines generation-track validity/playability procedures and competition protocols; playing-agent tracks are outside this note's scope.
- **中文说明:** GVGAI 的价值在于用统一 VGDL 引擎评测跨游戏关卡生成；这里不收录它的“玩游戏”排行榜。
- **English summary:** GVGAI provides a shared executable language and competition protocol for general level generation across games.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TG.2019.2901021), [official framework](https://github.com/GAIGResearch/GVGAI)
- **Open status:** **Open.** The engine, sample games, and level-generation interfaces are publicly maintained.

### 21. Evolving Mario Levels in the Latent Space of a Deep Convolutional GAN

- **Year / venue:** 2018, GECCO.
- **Scope:** `levels`
- **Generated content:** Super Mario Bros. tile levels.
- **Method:** a DCGAN learns a level latent space from VGLC; CMA-ES and novelty/quality-diversity search optimize latent vectors for desired level properties.
- **Evaluation:** generated-level playability plus objective properties and latent-space diversity/coverage under evolutionary search.
- **中文说明:** MarioGAN 先学习关卡潜空间，再在潜空间里进化可玩性或设计属性，奠定了“GAN + 搜索”的路线。
- **English summary:** MarioGAN evolves vectors in a learned GAN latent space to produce playable and diverse Mario levels.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/3205455.3205517), [official experiment repository](https://github.com/icaros-usc/MarioGAN-LSI), [VGLC data](https://github.com/TheVGLC/TheVGLC)
- **Open status:** **Open.** Author-maintained code and the public training corpus are available.

### 22. TOAD-GAN: Coherent Style Level Generation from a Single Example

- **Year / venue:** 2020, AIIDE.
- **Scope:** `levels`
- **Generated content:** tile-based levels matching the style and spatial scale of one example level.
- **Method:** a multi-scale generative adversarial network learns tile patterns from a single training level and composes new coherent maps.
- **Evaluation:** tile-pattern/style similarity, diversity, and domain-specific playability across several game level types.
- **中文说明:** TOAD-GAN 只需一个样例就能学习多尺度关卡风格，特别适合 PCG 常见的小数据场景。
- **English summary:** A multi-scale GAN learns from one level and generates coherent, stylistically related tile maps.
- **Primary sources:** [AIIDE proceedings](https://doi.org/10.1609/aiide.v16i1.7401), [arXiv](https://arxiv.org/abs/2008.01531), [official code](https://github.com/Mawiszus/TOAD-GAN)
- **Open status:** **Open.** Official training/generation code and examples are public.

### 23. PCGRL: Procedural Content Generation via Reinforcement Learning

- **Year / venue:** 2020, AIIDE.
- **Scope:** `levels`
- **Generated content:** levels for binary maps, Zelda-like dungeons, Sokoban, and other tile domains.
- **Method:** the RL policy is the **generator**: it edits tiles under narrow, turtle, or wide observation/action representations and receives content-quality rewards.
- **Evaluation:** training efficiency, validity/quality, diversity, and representation-dependent behaviour across multiple domains.
- **中文说明:** PCGRL 把造关卡建模成强化学习环境；这里的 RL 策略负责放砖块，不是负责通关。
- **English summary:** PCGRL trains an RL policy to edit tiles into valid levels and compares several generation representations.
- **Primary sources:** [AIIDE proceedings](https://doi.org/10.1609/aiide.v16i1.7416), [official environment/code](https://github.com/amidos2006/gym-pcgrl)
- **Open status:** **Open.** Environments, representations, metrics, and training code are public.

### 24. Learning Controllable Content Generators

- **Year / venue:** 2021, IEEE CoG.
- **Scope:** `levels`
- **Generated content:** diverse tile levels targeted to designer-specified content-property values.
- **Method:** makes PCGRL generators goal-aware by conditioning observations and rewards on distance to a requested heuristic target.
- **Evaluation:** target error/coverage, output diversity, and quality relative to goal-unaware generators across multiple domains.
- **中文说明:** 这项工作把 PCGRL 从“生成一个高分关卡”推进到“按设计师指定属性生成不同关卡”。
- **English summary:** Goal-conditioned PCGRL produces diverse levels while steering designer-selected quantitative properties.
- **Primary sources:** [arXiv](https://arxiv.org/abs/2105.02993), [IEEE DOI](https://doi.org/10.1109/COG52621.2021.9619159)
- **Open status:** **Partial.** The paper is public and builds on open PCGRL, but no separately packaged official experiment release was located.

### 25. Talakat: Bullet Hell Generation through Constrained MAP-Elites

- **Year / venue:** 2018, GECCO workshop/preprint.
- **Scope:** `levels`
- **Generated content:** executable bullet-hell attack scripts/patterns.
- **Method:** a domain language defines spawners; constrained MAP-Elites separates infeasible and feasible candidates while illuminating behaviour dimensions.
- **Evaluation:** playability/survival constraints, archive coverage, and diversity over bullet-pattern behaviour descriptors.
- **中文说明:** Talakat 用带约束的 MAP-Elites 生成弹幕脚本，在保证可玩的同时系统覆盖不同弹幕风格。
- **English summary:** Constrained MAP-Elites fills a diverse archive of playable bullet-hell patterns expressed in a generator language.
- **Primary sources:** [arXiv](https://arxiv.org/abs/1806.04718), [official project/code](https://github.com/amidos2006/Talakat)
- **Open status:** **Open.** The domain runtime and generation code are author-released.

### 26. Generating Levels That Teach Mechanics

- **Year / venue:** 2018, FDG.
- **Scope:** `levels`
- **Generated content:** small Mario levels designed to teach a particular action or mechanic.
- **Method:** evolution searches for levels beatable by a full A* agent but not by deliberately impaired variants that cannot perform or perceive the target mechanic.
- **Evaluation:** differential solvability between the full and restricted agents operationalizes whether a level requires the intended skill.
- **中文说明:** 它用“完整代理能过、不会某机制的代理过不了”作为目标，自动生成会教玩家机制的教程关。
- **English summary:** Tutorial levels are evolved so that success specifically depends on the mechanic they are intended to teach.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/3235765.3235820), [arXiv](https://arxiv.org/abs/1807.06734)
- **Open status:** **Paper-only.** No official maintained implementation package was located.

### 27. Level Generation Through Large Language Models

- **Year / venue:** 2023, FDG.
- **Scope:** `levels`
- **Generated content:** Sokoban levels represented as text grids.
- **Method:** language models are fine-tuned/autoregressively trained on level strings; experiments vary dataset size and test preliminary property control.
- **Evaluation:** functional/solvable level rate and scaling with training-set size, plus initial controllability experiments.
- **中文说明:** 论文把 Sokoban 地图当作语言序列，验证 LLM 能生成可解关卡且效果随数据量明显提升。
- **English summary:** Language models generate Sokoban grids, with solvability improving sharply as the level dataset grows.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/3582437.3587211), [arXiv](https://arxiv.org/abs/2302.05817)
- **Open status:** **Paper-only.** The paper/protocol is public, but no complete official training/evaluation package was located.

### 28. MarioGPT: Open-Ended Text2Level Generation through Large Language Models

- **Year / venue:** 2023, NeurIPS.
- **Scope:** `levels`
- **Generated content:** Super Mario Bros. levels conditioned on natural-language prompts.
- **Method:** a GPT-2 level model is steered by a frozen text encoder and discriminator/classifier guidance to connect descriptions with tile layouts.
- **Evaluation:** prompt–level attribute alignment, novelty/diversity, and playability/solvability analyses.
- **中文说明:** MarioGPT 提供了典型的 text-to-level 任务：用“很多管道、少量敌人”等自然语言控制 Mario 地图。
- **English summary:** MarioGPT maps free-form textual level descriptions to diverse and playable Mario tile layouts.
- **Primary sources:** [arXiv](https://arxiv.org/abs/2302.05981), [official code/models](https://github.com/shyamsn97/mario-gpt)
- **Open status:** **Open.** Training/inference code and model artifacts are author-released.

### 29. Super Mario as a String: Platformer Level Generation Via LSTMs

- **Year / venue:** 2016, DiGRA/FDG workshop publication.
- **Scope:** `levels`
- **Generated content:** Super Mario Bros. tile levels learned from a corpus of human-authored levels.
- **Method:** serializes 2D levels as character sequences and trains LSTMs under several data representations to predict and sample tiles.
- **Evaluation:** compares generated levels and alternative representations within a feature space derived from human-authored Mario levels.
- **中文说明:** 该工作把二维 Mario 地图序列化为字符串，用 LSTM 学习长距离结构，是早期深度 PCGML 的代表。
- **English summary:** LSTMs learn several string encodings of Mario maps and sample levels resembling the human-authored corpus.
- **Primary sources:** [official proceedings DOI](https://doi.org/10.26503/dl.v2016i1.752), [arXiv](https://arxiv.org/abs/1603.00930)
- **Open status:** **Paper-only.** No author-released runnable implementation was located; VGLC supplies related public level data.

### 30. DOOM Level Generation Using Generative Adversarial Networks

- **Year / venue:** 2018, IEEE Games, Entertainment, and Media Conference (GEM).
- **Scope:** `levels`
- **Generated content:** DOOM level layouts including occupied space, height, walls, and placed game objects.
- **Method:** compares a plain image GAN with a topology-conditioned GAN trained on extracted structural features from human maps.
- **Evaluation:** topological and distributional similarity to human-authored levels, plus qualitative inspection of generated layouts.
- **中文说明:** 这是把 GAN 从二维瓷砖关卡扩展到带高度、墙体和物件拓扑的第一人称射击地图的早期工作。
- **English summary:** Image- and topology-conditioned GANs learn structural features of human DOOM maps and synthesize new layouts.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/GEM.2018.8516539), [arXiv](https://arxiv.org/abs/1804.09154), [official author code/data](https://github.com/edoardogiacomello/DoomGAN)
- **Open status:** **Open.** The first author publishes preprocessing, models, generated data, and experiment code.

### 31. WaveFunctionCollapse Is Constraint Solving in the Wild

- **Year / venue:** 2017, FDG; expanded analysis in IEEE Transactions on Games (2021).
- **Scope:** `levels`
- **Generated content:** tile maps/images satisfying local patterns learned from an example.
- **Method:** interprets WaveFunctionCollapse as constraint solving over overlapping or tiled adjacency models, repeatedly propagating local compatibility constraints.
- **Evaluation:** analyses algorithmic behaviour, constraint failures, and representative generation tasks; it does not guarantee global gameplay or solvability.
- **中文说明:** WFC 会从样例学习局部邻接约束并生成一致地图，但局部合法不等于关卡可通关，必须单独做玩法验证。
- **English summary:** WFC generates locally consistent tile maps through learned adjacency constraints, without ensuring global playability.
- **Primary sources:** [FDG DOI](https://doi.org/10.1145/3102071.3110566), [journal DOI](https://doi.org/10.1109/TG.2021.3076368), [original official implementation](https://github.com/mxgmn/WaveFunctionCollapse)
- **Open status:** **Open/Partial.** The reference implementation is public, but the papers are analyses rather than a fixed gameplay benchmark.

## C. Component-only generation / 仅生成游戏组件（不等于完整游戏）

### 32. World-GAN: A Generative Model for Minecraft Worlds

- **Year / venue:** 2021, IEEE CoG.
- **Scope:** `components`
- **Generated content:** Minecraft voxel structures/world regions learned from a single example.
- **Method:** extends the single-example, multi-scale GAN idea into 3D and generates block volumes at multiple spatial scales.
- **Evaluation:** structural coherence, diversity, and qualitative comparison to the source style; no new game rules or objectives are generated.
- **中文说明:** World-GAN 生成的是 Minecraft 三维建筑/地形组件，不会生成一套新玩法，因此不能归为完整游戏生成。
- **English summary:** A multi-scale 3D GAN synthesizes Minecraft voxel structures from one example, without generating gameplay rules.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/COG52621.2021.9619133), [official code](https://github.com/Mawiszus/World-GAN)
- **Open status:** **Open.** Official code and examples are public.

### 33. The AI Settlement Generation Challenge in Minecraft (GDMC)

- **Year / venue:** 2020, KI – Künstliche Intelligenz.
- **Scope:** `components`
- **Generated content:** context-aware Minecraft settlements placed into previously unseen maps.
- **Method:** a competition harness supplies terrain and evaluates generators that plan roads, buildings, land use, and adaptation to local geography.
- **Evaluation:** expert judging of adaptability, functionality, narrative/aesthetics, and related settlement qualities; exact annual rubrics evolve.
- **中文说明:** GDMC 是很有价值的开放生成挑战，但产物是聚落与世界内容，不是带新规则的完整游戏。
- **English summary:** GDMC benchmarks generators of terrain-aware Minecraft settlements, not generators of new game mechanics.
- **Primary sources:** [Springer DOI](https://doi.org/10.1007/s13218-020-00635-0), [official framework](https://github.com/avdstaaij/gdmc_http_interface)
- **Open status:** **Open/Partial.** The interface and competition materials are public; judging includes human assessment and varies by year.

## D. Foundational surveys and taxonomies / 奠基综述与分类

### 34. Search-Based Procedural Content Generation: A Taxonomy and Survey

- **Year / venue:** 2011, IEEE Transactions on Computational Intelligence and AI in Games.
- **Scope:** `survey`
- **Generated content:** no new generator benchmark; the paper organizes search-based generation of levels, rules, maps, puzzles, and other content.
- **Method:** defines content representations, evaluation functions, direct/indirect encodings, and online/offline generation dimensions.
- **Evaluation:** taxonomy and literature synthesis rather than an empirical leaderboard.
- **中文说明:** 这是理解“搜索空间、内容表示、适应度函数、在线/离线生成”这些 PCG 基本概念的奠基综述。
- **English summary:** The survey establishes the core taxonomy for representing, searching, and evaluating procedurally generated game content.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TCIAIG.2011.2148116)
- **Open status:** **Paper-only by design.** It is a survey, not an artifact release.

### 35. Procedural Content Generation via Machine Learning (PCGML)

- **Year / venue:** 2018, IEEE Transactions on Games.
- **Scope:** `survey`
- **Generated content:** no single generator; formalizes learning generators from existing game content rather than hand-coding every rule.
- **Method:** taxonomy spans training-data sources, learned representations, generation strategies, and relationships between data and output domains.
- **Evaluation:** literature synthesis plus a research agenda covering data scarcity, controllability, evaluation, and generalization.
- **中文说明:** PCGML 综述确立了“从已有游戏内容学习生成器”的研究范式，也是理解 VGLC、MarioGAN、TOAD-GAN 的入口。
- **English summary:** PCGML defines how machine-learned models acquire and generate game content from example data.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TG.2018.2846639), [author manuscript](https://arxiv.org/abs/1702.00539)
- **Open status:** **Paper-only by design.** It is a taxonomy/survey rather than one benchmark implementation.

## Explicit exclusions / 明确排除

- **Game-playing only:** ALE, Procgen Benchmark, CoinRun, NetHack Learning Environment, MineRL/BASALT, Crafter, BabyAI, GVGAI playing tracks, and similar agent-control benchmarks do not generate game designs or levels.
- **Playtesting agents:** MCTS/RL/search papers are not included merely because they evaluate a game. They appear above only when the policy/search process is directly optimizing generated content.
- **Asset or narrative generation alone:** texture, sprite, music, dialogue, story, and video generation are `components` unless the work also instantiates executable rules/mechanics. A visual world model that predicts the next frame is not automatically a generated game.
- **Mixed-initiative tools:** systems that only help a human edit content are outside this core list unless they include a substantive automatic generator and a primary evaluation of its outputs.
