# Procedural content generation and automated game design: verified primary sources

> 检索截止 / Verified through: **2026-09-01** (Asia/Shanghai). This note is deliberately limited to systems that generate games, rules, mechanics, levels, or game-world components. It does **not** include agents whose task is only to play a game.

## Inclusion and status rules / 收录与开放性口径

- **Scope labels:** `full-game`, `rules`, `levels`, `components`, or `survey`. `components` means that the output does not by itself define playable rules or a complete game.
- **Open:** official paper plus sufficient author-released code/data/evaluator to run the central pipeline.
- **Partial:** a useful official artifact is public, but some training data, generated corpus, evaluator, historical code, or other essential piece is absent.
- **Closed:** a primary paper/proceedings page is public, but no reproducible official release was located. A paper saying that data are public does not qualify unless the artifact can actually be found.
- **Paper-only by design:** a survey or conceptual framework that does not claim to release a generator.
- RL papers appear only where the RL policy is the **content generator**. Procgen, CoinRun, ALE, MineRL agent tracks, GVGAI playing tracks, and other playing-only benchmarks are excluded.

Boundary classification is explicit in the public index: **Ludii** is rule-language/runtime infrastructure, **GVGAI** is a mixed framework of which only generation tracks are relevant, **WaveFunctionCollapse** is an adjacent generic constraint technique, **Danesh** tunes and analyses fixed generators, and the **AI Settlement Generation Challenge** is a component-level settlement benchmark. None is counted as a core game/level generator.

### 2026-08-29 through 2026-08-31 incremental check

The official arXiv category feeds were still topped by submissions from **2026-08-28** at the cutoff; keyword-sorted feeds for procedural content, procedural levels, game-level generation, game-content generation, and generator programs returned no paper first submitted on August 29–31. A second check of the relevant CoG, FDG, AIIDE, and IEEE Transactions on Games primary records found no newly posted high-confidence generation paper in that window. No new recent paper was added. Three initial historical passes recovered 26 generation families, from EGGG through early multiobjective, grammar, n-gram, search, cellular-automata, and probabilistic generators, bringing the intermediate total to 86. Two final primary-source passes added 27 independent level-generation, metageneration, competition, and evaluation families, bringing this PCG collection to **113 version families**.

A final independent audit on **2026-09-01** corrected the AIBIRDS judging/artifact description and recovered two more independent records: an Angry Birds generation corpus and a Mario diffusion-level generator. The PCG collection therefore contains **115 version families**. / 2026-09-01 的最终独立复核修正了 AIBIRDS 的评分与工件描述，并补回 Angry Birds 生成语料和 Mario 扩散关卡生成器两个独立条目，因此 PCG 集合现为 **115 个版本族**。

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
- **Open status:** **Closed.** The publication is accessible, but no official historical implementation/data release was located.

### 2. Automatic Generation and Evaluation of Recombination Games / Evolutionary Game Design (Ludi)

- **Year / venue:** 2008, Queensland University of Technology PhD thesis; extended in IEEE Transactions on Computational Intelligence and AI in Games, 2010.
- **Scope:** `rules`
- **Generated content:** rule sets for abstract combinatorial board games expressed as ludemes.
- **Method:** Ludi evolves recombinations of rule building blocks and uses automated self-play measurements to score candidates.
- **Evaluation:** playability and heuristic qualities such as balance, depth, and decisiveness; the process produced human-playable games including Yavalath.
- **中文说明:** Ludi 把棋类规则拆成可重组的 ludeme，再通过自博弈筛掉无效或失衡的规则组合。
- **English summary:** Ludi evolves recombinations of rule primitives and filters them with automated play-based quality estimates.
- **Primary sources:** [official QUT repository record](https://eprints.qut.edu.au/17025/), [thesis PDF](https://eprints.qut.edu.au/17025/1/Cameron_Browne_Thesis.pdf), [journal extension](https://doi.org/10.1109/TCIAIG.2010.2041928), [Ludii successor platform](https://ludii.games/)
- **Open status:** **Partial.** The thesis, journal record, and successor Ludii ecosystem are public, but the original Ludi experiment is not packaged as a current reproducible benchmark.

### 3. Multi-faceted Evolution of Simple Arcade Games (ANGELINA)

- **Year / venue:** 2011, IEEE CIG.
- **Scope:** `full-game`
- **Generated content:** playable arcade games with mechanics, rules, and level layouts.
- **Method:** ANGELINA co-evolves several facets of a game rather than optimizing one fixed content type; automated play helps judge candidates.
- **Evaluation:** generated games are checked for functional play and examined as design artifacts; this is a system demonstration, not a fixed leaderboard.
- **中文说明:** ANGELINA 同时搜索机制与关卡等多个设计面，是“自动做游戏”而非单独画地图的经典系统。
- **English summary:** ANGELINA jointly evolves multiple facets of simple arcade games and evaluates them through automated play.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2011.6032019)
- **Open status:** **Closed.** No complete official release of this historical ANGELINA version was located.

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
- **Open status:** **Closed.** No official runnable release was located.

### 6. Automatic Game Design via Mechanic Generation

- **Year / venue:** 2014, AAAI.
- **Scope:** `rules`
- **Generated content:** game mechanics/rules satisfying designer-provided requirements.
- **Method:** formal mechanic representations and search are combined with simulated execution to construct and test candidate designs.
- **Evaluation:** case-study games test whether generated mechanics realize target gameplay requirements and remain executable.
- **中文说明:** 该工作把机制写成可推理的形式模型，再搜索满足设计约束的规则，而不是让代理去玩固定游戏。
- **English summary:** Formalized mechanics are searched and simulated to synthesize rule sets that meet design requirements.
- **Primary sources:** [AAAI proceedings](https://doi.org/10.1609/aaai.v28i1.8788)
- **Open status:** **Closed.** The evaluation is documented, but no official complete code/data package was located.

### 7. A Rogue Dream: Automatically Generating Meaningful Content for Games (ANGELINA)

- **Year / venue:** 2014, AIIDE.
- **Scope:** `full-game`
- **Generated content:** complete small games whose mechanics, content, and framing are derived from topical source material.
- **Method:** ANGELINA selects concepts from news/current-affairs input, searches game designs, and assembles playable artifacts around a chosen theme.
- **Evaluation:** generated games are presented as creative case studies and assessed qualitatively rather than through a reusable benchmark.
- **中文说明:** 这一代 ANGELINA 会从现实主题出发自动选择概念、做机制并产出带意义表达的完整小游戏。
- **English summary:** ANGELINA converts topical source material into themed, playable games through autonomous design search.
- **Primary sources:** [AIIDE proceedings](https://doi.org/10.1609/aiide.v10i3.12745)
- **Open status:** **Closed.** Generated examples are documented, but the complete system is not released as a reproducible package.

### 8. Automated Game Design via Conceptual Expansion / Conceptual Game Expansion

- **Year / venue:** *Automated Game Design via Conceptual Expansion*, AIIDE 2018; journal expansion *Conceptual Game Expansion*, registered/online in 2021 and formally published in IEEE Transactions on Games 14(1), 2022.
- **Scope:** `full-game`
- **Generated content:** novel games made by recombining learned representations of existing games.
- **Method:** conceptual expansion blends learned game graphs/components instead of relying on a hand-authored rule grammar.
- **Evaluation:** the system is asked to reconstruct held-out existing games, providing a measurable proxy before presenting novel recombinations.
- **中文说明:** Conceptual Expansion 从已有游戏中学习结构，再“概念混合”出新游戏，并先用复原已知游戏验证方法。
- **English summary:** Learned game representations are recombined through conceptual expansion and evaluated by reconstructing known games.
- **Primary sources:** [AIIDE paper](https://doi.org/10.1609/aiide.v14i1.13022), [arXiv](https://arxiv.org/abs/1809.02232), [journal article](https://doi.org/10.1109/TG.2021.3060005)
- **Open status:** **Closed.** No official end-to-end artifact package was located.

### 9. Orchestrating Game Generation

- **Year / venue:** 2018, IEEE Transactions on Games.
- **Scope:** `survey`
- **Generated content:** a system architecture for coordinating generators of rules, levels, visuals, audio, and other game facets.
- **Method:** proposes orchestration patterns and interfaces so heterogeneous generators can exchange constraints and feedback.
- **Evaluation:** synthesizes evidence from existing generation systems and design scenarios; it is an architecture/framework paper, not itself a benchmark.
- **中文说明:** 这篇工作解释如何让规则、关卡、图像等生成器协同，避免把“各做一个组件”误称为自动生成完整游戏。
- **English summary:** A framework organizes how specialized generators can coordinate to produce coherent multi-facet games.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TG.2018.2870876)
- **Open status:** **Paper-only by design.** This is a conceptual orchestration framework, not a released generator suite.

### 10. Puck: A Slow and Personal Automated Game Designer

- **Year / venue:** 2022, AIIDE.
- **Scope:** `full-game`
- **Generated content:** a personal, continuously evolving collection of small playable game designs.
- **Method:** Puck explores designs over long periods and incorporates a designer's ongoing interaction and preferences rather than optimizing a one-shot benchmark score.
- **Evaluation:** reflective longitudinal case study of generated games and the human–system relationship.
- **中文说明:** Puck 强调长期、个性化的自动设计过程，用持续积累的设计作品替代一次性生成排行榜。
- **English summary:** Puck slowly explores a personalized space of complete game designs in a longitudinal human–AI process.
- **Primary sources:** [AIIDE proceedings](https://doi.org/10.1609/aiide.v18i1.21968)
- **Open status:** **Closed.** The paper documents the system and artifacts, but no complete official reproducibility package was located.

### 11. Ludii – The Ludemic General Game System (boundary infrastructure)

- **Year / venue:** 2020, ECAI.
- **Scope:** `infrastructure` (not a generator)
- **Generated content:** Ludii itself is a formal rule language, compiler/runtime, and game corpus; it is infrastructure for rule generation rather than a generator by itself.
- **Method:** games are composed from ludemes in a compact grammar, enabling automated execution, concept extraction, and downstream search such as GAVEL.
- **Evaluation:** coverage and faithful execution across a broad collection of traditional strategy games.
- **中文说明:** Ludii 是规则生成所依赖的“可执行游戏语言与语料库”，本身不要误标成自动生成算法。
- **English summary:** Ludii supplies an executable ludeme-based language and corpus on which rule-generation systems can search.
- **Primary sources:** [ECAI DOI](https://doi.org/10.3233/FAIA200120), [arXiv](https://arxiv.org/abs/1905.05013), [official platform/library](https://ludii.games/)
- **Open status:** **Partial.** The platform and game library are accessible, but the full current engine is distributed as an application rather than a complete open-source research stack. It is indexed in the boundary section, not counted as a generator.

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
- **Open status:** **Closed.** A fixed official task set, generator code, and evaluator package were not located.

### 15. ScriptDoctor: Automatic Generation of PuzzleScript Games via LLMs and Tree Search

- **Year / venue:** 2025, IEEE CoG.
- **Scope:** `full-game`
- **Generated content:** complete PuzzleScript rule files and puzzle levels.
- **Method:** an LLM iteratively revises a game using compiler errors, control-flow feedback, and BFS playtesting; each trial has a bounded repair budget.
- **Evaluation:** compilation rate, presence of a solver solution, and the stricter rate where every level is solvable with solution length greater than ten; BFS is capped at one million states.
- **中文说明:** ScriptDoctor 用编译器和求解器反馈循环“看病”，直到 PuzzleScript 游戏既能编译又有可解关卡。
- **English summary:** Compiler and tree-search feedback iteratively repair LLM-generated PuzzleScript games into solvable artifacts.
- **Primary sources:** [arXiv](https://arxiv.org/abs/2506.06524), [IEEE DOI](https://doi.org/10.1109/COG64752.2025.11114269), [official PuzzleScript runtime](https://github.com/increpare/PuzzleScript)
- **Open status:** **Closed.** The upstream PuzzleScript runtime is not a ScriptDoctor artifact; no official ScriptDoctor implementation or 610-game experiment corpus was located.

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

### 20. General Video Game AI: A Multitrack Framework for Evaluating Agents, Games, and Content Generation Algorithms (mixed-framework boundary)

- **Year / venue:** 2019, IEEE Transactions on Games.
- **Scope:** `mixed framework`; only its generation tracks are in scope.
- **Generated content:** VGDL levels and, in the generation tracks, content for many rule-defined games.
- **Method:** a common VGDL runtime separates game rules, level descriptions, generators, and automated players.
- **Evaluation:** the framework defines generation-track validity/playability procedures and competition protocols; playing-agent tracks are outside this note's scope.
- **中文说明:** GVGAI 的价值在于用统一 VGDL 引擎评测跨游戏关卡生成；这里不收录它的“玩游戏”排行榜。
- **English summary:** GVGAI provides a shared executable language and competition protocol for general level generation across games.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TG.2019.2901021), [2016 level-generation-track precursor](https://doi.org/10.1145/2908812.2908920), [official framework](https://github.com/GAIGResearch/GVGAI).
- **Open status:** **Open.** The engine, sample games, and level-generation interfaces are publicly maintained. The playing-agent tracks remain excluded.

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
- **Open status:** **Closed.** No official maintained implementation package was located.

### 27. Level Generation Through Large Language Models

- **Year / venue:** 2023, FDG.
- **Scope:** `levels`
- **Generated content:** Sokoban levels represented as text grids.
- **Method:** language models are fine-tuned/autoregressively trained on level strings; experiments vary dataset size and test preliminary property control.
- **Evaluation:** functional/solvable level rate and scaling with training-set size, plus initial controllability experiments.
- **中文说明:** 论文把 Sokoban 地图当作语言序列，验证 LLM 能生成可解关卡且效果随数据量明显提升。
- **English summary:** Language models generate Sokoban grids, with solvability improving sharply as the level dataset grows.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/3582437.3587211), [arXiv](https://arxiv.org/abs/2302.05817)
- **Open status:** **Closed.** The paper/protocol is public, but no complete official training/evaluation package was located.

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

- **Year / venue:** 2016, DiGRA/FDG workshop publication; player-tailored extension at the AIIDE Experimental AI in Games workshop.
- **Scope:** `levels`
- **Generated content:** Super Mario Bros. tile levels learned from human-authored levels; the extension learns player-specific styles from gameplay videos.
- **Method:** serializes 2D levels as character sequences and trains LSTMs under several representations; the extension trains four individual models and one combined-player model from observation traces.
- **Evaluation:** compares representations in a human-level-derived feature space, then samples 4,000 levels from each of the five tailored models (20,000 total) for feature-space analysis.
- **中文说明:** 该版本族把二维 Mario 地图序列化为字符串；扩展版又从四名玩家的视频轨迹训练个人模型和组合模型，直接生成玩家定制关卡。
- **English summary:** LSTMs learn string encodings of Mario maps, with a follow-up conditioning the learned style on observed individual or combined player traces.
- **Primary sources:** [official proceedings DOI](https://doi.org/10.26503/dl.v2016i1.752), [arXiv](https://arxiv.org/abs/1603.00930), [player-tailored extension](https://doi.org/10.1609/aiide.v12i2.12895), [five tailored generated-level corpora](https://tinyurl.com/SMB-from-Video), [original SMBRNN generated-level corpus](https://tinyurl.com/SMBRNN).
- **Open status:** **Partial, legacy outputs only.** The generated-level corpora remain downloadable, but no generator, trained model, video-processing pipeline, training code, or evaluation package was verified.

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

### 31. WaveFunctionCollapse Is Constraint Solving in the Wild (adjacent-technique boundary)

- **Year / venue:** 2017, FDG; expanded analysis in IEEE Transactions on Games (2021).
- **Scope:** `adjacent technique`; generic constraint generation rather than a game-specific generator.
- **Generated content:** tile maps/images satisfying local patterns learned from an example.
- **Method:** interprets WaveFunctionCollapse as constraint solving over overlapping or tiled adjacency models, repeatedly propagating local compatibility constraints.
- **Evaluation:** analyses algorithmic behaviour, constraint failures, and representative generation tasks; it does not guarantee global gameplay or solvability.
- **中文说明:** WFC 会从样例学习局部邻接约束并生成一致地图，但局部合法不等于关卡可通关，必须单独做玩法验证。
- **English summary:** WFC generates locally consistent tile maps through learned adjacency constraints, without ensuring global playability.
- **Primary sources:** [FDG DOI](https://doi.org/10.1145/3102071.3110566), [journal DOI](https://doi.org/10.1109/TG.2021.3076368), [original official implementation](https://github.com/mxgmn/WaveFunctionCollapse)
- **Open status:** **Open/Partial.** The reference implementation is public, but the papers are analyses rather than a fixed gameplay benchmark; the method is kept in the boundary section.

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

### 33. The AI Settlement Generation Challenge in Minecraft (GDMC; component boundary)

- **Year / venue:** 2020, KI – Künstliche Intelligenz.
- **Scope:** `components` benchmark; not a complete game/level generator.
- **Generated content:** context-aware Minecraft settlements placed into previously unseen maps.
- **Method:** a competition harness supplies terrain and evaluates generators that plan roads, buildings, land use, and adaptation to local geography.
- **Evaluation:** expert judging of adaptability, functionality, narrative/aesthetics, and related settlement qualities; exact annual rubrics evolve.
- **中文说明:** GDMC 是很有价值的开放生成挑战，但产物是聚落与世界内容，不是带新规则的完整游戏。
- **English summary:** GDMC benchmarks generators of terrain-aware Minecraft settlements, not generators of new game mechanics.
- **Primary sources:** [Springer DOI](https://doi.org/10.1007/s13218-020-00635-0), [official framework](https://github.com/avdstaaij/gdmc_http_interface)
- **Open status:** **Open/Partial.** The interface and competition materials are public; judging includes human assessment and varies by year. It is listed as a boundary resource rather than a core generator.

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

## E. Additional level and playable-content generation families / 补充关卡与可玩内容生成族

### 36. PCGPT: Procedural Content Generation via Transformers

- **Year / venue:** 2023, arXiv preprint.
- **Scope and task/method:** `levels`; a return-conditioned causal transformer learns from offline PCGRL trajectories and iteratively predicts Sokoban items and positions.
- **Evaluation:** success rate and edit-step behaviour over 10,000 random initial maps, with diversity/complexity analysis and PCGRL comparisons.
- **Official artifacts:** [paper](https://arxiv.org/abs/2310.02405).
- **Open status:** **Closed.** The paper says its 3,000-map offline dataset is public but supplies no working location; no author code, data, checkpoint, or evaluator was verified.
- **中文说明:** PCGPT 把造 Sokoban 关卡视为离线轨迹建模，但“数据公开”的文字声明没有对应可取得链接，因此不能标开放。
- **English summary:** PCGPT generates Sokoban edits from offline PCGRL trajectories with a causal transformer, but its claimed public dataset could not be located.

### 37. ChatGPT4PCG Competition family

- **Year / venue:** 2023 and 2024, IEEE Conference on Games competition papers; treated as one evolving competition family.
- **Scope and task/method:** `levels` benchmark; prompts or Python prompt programs make ChatGPT emit function calls that construct letter-shaped Science Birds levels.
- **Evaluation:** physical stability and letter similarity in both editions, with within-character diversity and a revised classifier/pipeline added in 2024.
- **Official artifacts:** [first paper](https://arxiv.org/abs/2303.15662), [second paper](https://arxiv.org/abs/2403.02610), [competition site](https://chatgpt4pcg.github.io/), [official repository organization](https://github.com/orgs/chatgpt4pcg/repositories), [2024 code and raw data](https://github.com/chatgpt4pcg/experiments-2024).
- **Open status:** **Open.** The modified engine, response collection, text/XML conversion, similarity/diversity checks, scoring, prompt-engineering examples, and experiment data are public.
- **中文说明:** 两届竞赛用同一 Science Birds 任务逐步完善稳定性、字符相似度与多样性评价，应合并成一个版本族。
- **English summary:** The two ChatGPT4PCG editions form an open benchmark family for prompt-driven, physically stable Science Birds level generation.

### 38. Procedural Level Generation in Educational Games From Natural Language Instruction

- **Year / venue:** 2024, IEEE Transactions on Games.
- **Scope and task/method:** `levels`; natural-language instructional goals drive educational-game level generation and learned candidate selection.
- **Evaluation:** instruction alignment and level quality under alternative generation/selection settings.
- **Official artifacts:** [IEEE DOI](https://doi.org/10.1109/TG.2024.3392670).
- **Open status:** **Closed.** No official task set, code, trained model, generated corpus, or evaluator release was verified.
- **中文说明:** 该工作直接从教学语言要求生成教育游戏关卡，不是完整教育游戏生成，但属于明确的自然语言条件关卡 PCG。
- **English summary:** Natural-language learning goals condition the generation and selection of educational-game levels, without a public reproduction package.

### 39. Improving Conditional Level Generation Using Automated Validation in Match-3 Games

- **Year / venue:** 2024, IEEE Transactions on Games.
- **Scope and task/method:** `levels`; a cVAE is conditioned on board size, symmetry, and bot-estimated move difficulty, with automated post-generation validation.
- **Evaluation:** validity, size/difficulty condition accuracy, plagiarism/novelty, tile-distribution style fidelity, and diversity.
- **Official artifacts:** [IEEE DOI](https://doi.org/10.1109/TG.2024.3440214), [arXiv](https://arxiv.org/abs/2409.06349).
- **Open status:** **Closed.** The industrial level data, scripted bot, model implementation, and evaluator are not officially released.
- **中文说明:** 论文把“需要多少步通关”的 bot 统计作为条件，提升 Match-3 关卡有效率，但数据与验证器并未开放。
- **English summary:** Automated play statistics condition and validate Match-3 layout generation, though the proprietary data and pipeline are closed.

### 40. Making New Connections: LLMs as Puzzle Generators

- **Year / venue:** 2024, AIIDE.
- **Scope and task/method:** `puzzles`; Tree of Thoughts prompting generates complete 16-word Connections puzzles, including seeded and deliberately misleading false groups.
- **Evaluation:** a human study compares challenge, enjoyment, creativity, and overall quality with published New York Times puzzles.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2407.11240), [AIIDE DOI](https://doi.org/10.1609/aiide.v20i1.31869), [author repository with prompts and puzzle corpora](https://github.com/TimMerino1710/making-new-connections).
- **Open status:** **Partial.** Prompts plus generated and published puzzle JSON are public, but the full orchestration and user-study/evaluation package are absent.
- **中文说明:** 这篇论文研究的是“出 Connections 谜题”而不是解谜；作者公开了提示和谜题语料，但没有完整实验流水线。
- **English summary:** LLMs generate complete Connections puzzles that humans compare with published puzzles; prompts and corpora are public, not the full study.

### 41. Moonshine: Distilling Game Content Generators into Steerable Generative Models

- **Year / venue:** arXiv 2024; AAAI 2025.
- **Scope and task/method:** `levels`; Brogue's constructive generator produces dungeon maps, an LLM labels them, and text-conditioned diffusion/feed-forward models distil the generator.
- **Evaluation:** map variety, text/map accuracy, quality, connectivity, CLIP alignment, and human assessment against the constructive source.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2408.09594), [AAAI DOI](https://doi.org/10.1609/aaai.v39i13.33571), [official dungeon map-description dataset](https://huggingface.co/datasets/DolphinNie/dungeon-dataset).
- **Open status:** **Partial.** The train/validation/test map-description archives are downloadable, but source code, checkpoints, prompts, and the complete evaluator are not.
- **中文说明:** Moonshine 用传统生成器造海量地图，再用 LLM 补文本标签，最终学习可用自然语言控制的 text-to-map 模型。
- **English summary:** Moonshine distils a black-box dungeon generator into steerable text-to-map models; only the synthetic dataset is released.

### 42. PCGRL+: Scaling, Control and Generalization in Reinforcement Learning Level Generators

- **Year / venue:** 2024, IEEE Conference on Games.
- **Scope and task/method:** `levels`; JAX/GPU parallelization scales PCGRL training and adds randomized map sizes, frozen pinpoints, and OOD-size evaluation.
- **Evaluation:** environment throughput, billion-step training behaviour, controllability, representation/observation effects, and generalization to larger unseen maps.
- **Official artifacts:** [paper](https://arxiv.org/abs/2408.12525), [author PCGRL-JAX repository](https://github.com/smearle/pcgrl-jax).
- **Open status:** **Open.** Apache-2.0 environments, models, training, sweeps, evaluation, controls, and larger-map scripts are public.
- **中文说明:** PCGRL+ 把 PCGRL 完整迁移到 JAX/GPU，并把研究重点扩展到尺寸、固定关键点与超出训练尺度的泛化。
- **English summary:** PCGRL+ makes RL level generation GPU-scalable and tests controllability and out-of-distribution map-size generalization.

### 43. ChatPCG to PCGRLLM version family

- **Year / venue:** ChatPCG, IEEE CoG 2024; PCGRLLM, IEEE Transactions on Games 2026.
- **Scope and task/method:** `levels`; an LLM writes reward functions that steer PCGRL generators, while the extension adds feedback and reasoning-based prompts for story-to-reward generation.
- **Evaluation:** reward correctness, generated-content controllability, story alignment, feedback iterations, prompting ablations, and comparison with human rewards.
- **Official artifacts:** [ChatPCG paper](https://arxiv.org/abs/2406.11875), [PCGRLLM paper](https://arxiv.org/abs/2502.10906), [IEEE DOI](https://doi.org/10.1109/TG.2026.3695197), [ChatPCG prompts](https://github.com/bic4907/ChatPCG), [PCGRLLM code](https://github.com/bic4907/pcgrl-llm).
- **Open status:** **Open.** The prompt artifacts and expanded JAX-based training/evaluation implementation are public.
- **中文说明:** 这一版本族不是让 LLM 直接画地图，而是让它写出 PCGRL 奖励，再由内容生成策略执行设计目标。
- **English summary:** ChatPCG/PCGRLLM use language models to author rewards that turn natural-language design intent into controlled PCGRL content.

### 44. Word2Minecraft: Generating 3D Game Levels through Large Language Models

- **Year / venue:** 2025, arXiv preprint.
- **Scope and task/method:** `levels`; structured stories are converted into Minecraft levels with scaled spatial layouts, goals, obstacles, and gameplay constraints.
- **Evaluation:** structural metrics plus human ratings of story coherence, aesthetics, objectives, map enjoyment, and model comparisons.
- **Official artifacts:** [paper](https://arxiv.org/abs/2503.16536), [official code/examples branch](https://github.com/JMZ-kk/Word2Minecraft/tree/word2mc_v0).
- **Open status:** **Open, API/environment-dependent.** Apache-2.0 generation and play code plus examples are public; an LLM API and Minecraft tooling are external.
- **中文说明:** Word2Minecraft 从故事中的主角目标、反派挑战和环境设置构造带玩法约束的三维 Minecraft 关卡。
- **English summary:** Word2Minecraft turns structured narratives into spatially coherent, goal-bearing Minecraft levels through an open API-dependent pipeline.

### 45. IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation

- **Year / venue:** 2025, IEEE Conference on Games.
- **Scope and task/method:** `levels`; task-specific sentence embeddings condition a PCGRL policy directly on natural-language requirements.
- **Evaluation:** controllability over several level properties and generalization to held-out instructions, compared with generic embeddings/baselines.
- **Official artifacts:** [paper](https://arxiv.org/abs/2503.12358), [official code and instruction data](https://github.com/bic4907/language-instructed-pcgrl).
- **Open status:** **Open.** Apache-2.0 instruction splits, data collection, encoders, environments, training, and evaluation commands are public.
- **中文说明:** IPCGRL 让关卡生成策略直接理解自然语言属性要求，并专门测量对未见指令的泛化能力。
- **English summary:** IPCGRL learns instruction embeddings that let an RL content generator follow and generalize natural-language level constraints.

### 46. Evolutionary Level Repair

- **Year / venue:** 2025, GECCO Companion.
- **Scope and task/method:** `levels` repair; evolutionary and quality-diversity search minimally edits non-functional PCGML outputs into complete/reachable levels.
- **Evaluation:** completeness and reachability, number of edits, fitness, diversity/archive properties, and comparisons among search variants.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2506.19359), [ACM DOI](https://doi.org/10.1145/3712255.3726692).
- **Open status:** **Closed.** No author code, broken/repaired level corpus, experiment configuration, or evaluator package was verified.
- **中文说明:** 该方法把“生成后修复”作为混合 PCG 的独立阶段，在尽量少改动的条件下补足关卡功能。
- **English summary:** Evolutionary and quality-diversity search repair broken learned levels while limiting edits, without a public reproduction package.

### 47. Human-Aligned Procedural Level Generation RL via Text-Level-Sketch Shared Representation (VIPCGRL)

- **Year / venue:** arXiv 2025; IEEE Transactions on Games 2026.
- **Scope and task/method:** `levels`; quadruple contrastive learning aligns text, level states, sketches, and human/AI styles, then an embedding-similarity reward guides PCGRL.
- **Evaluation:** quantitative controllability and human-likeness metrics plus human evaluation of cross-modal intent alignment.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2508.09860), [IEEE DOI](https://doi.org/10.1109/TG.2026.3713793), [official code and dataset](https://github.com/bic4907/VIPCGRL).
- **Open status:** **Open.** Apache-2.0 text/level/sketch data, encoders, style translation, policy training, and evaluation scripts are public.
- **中文说明:** VIPCGRL 不只接受文本，还把关卡图和草图映射到共享空间，以更接近人类设计意图的奖励训练生成策略。
- **English summary:** VIPCGRL aligns text, levels, and sketches in one representation and rewards an RL generator for matching human intent.

### 48. A Database-Driven Framework for 3D Level Generation with LLMs

- **Year / venue:** 2025, AIIDE.
- **Scope and task/method:** `levels`; LLM-assisted offline construction of room, facility, and mechanic databases supports multi-floor assembly, constrained placement, progression, and two-stage navigation repair.
- **Evaluation:** diversity, topological order, spatial-constraint satisfaction, connectivity/navigability, and parameterized gameplay pacing.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2508.18533), [AIIDE DOI](https://doi.org/10.1609/aiide.v21i1.36840).
- **Open status:** **Closed.** No official database, pipeline implementation, generated level set, or evaluator was verified.
- **中文说明:** 该框架把三维关卡拆成可复用的房间、设施和机制数据库，并在装配后专门修复多层导航。
- **English summary:** Reusable architectural and mechanic databases drive multi-floor 3D level assembly and navigation repair, but no artifacts are released.

### 49. From Unstable to Playable: Stabilizing Angry Birds Levels via Object Segmentation

- **Year / venue:** 2025, AIIDE.
- **Scope and task/method:** `levels` repair; object segmentation finds structural gaps in rendered PCG levels and targeted XML edits stabilize the corresponding Angry Birds structures.
- **Evaluation:** segmentation-model comparison and changes in stability/playability over generated and synthetically damaged levels.
- **Official artifacts:** [paper](https://arxiv.org/abs/2509.23787).
- **Open status:** **Closed.** Training data, segmentation/repair code, input levels, repaired outputs, and evaluation scripts are not officially released.
- **中文说明:** 这项工作把关卡渲染图中的结构断裂定位回 XML 关卡并修补，最终评价对象是修复后的可玩关卡。
- **English summary:** Image segmentation locates structural gaps and repairs generated Angry Birds levels, without an official implementation or dataset.

### 50. Zero-shot 3D Map Generation with LLM Agents

- **Year / venue:** 2025, arXiv preprint.
- **Scope and task/method:** `levels`; an Actor maps natural-language intent to opaque PCG-tool parameters and a Critic iteratively checks tool names, ranges, ordering, alignment, and completeness.
- **Evaluation:** a new instruction-following benchmark compares structural validity, preference alignment, and dual-agent gains with single-agent baselines.
- **Official artifacts:** [paper](https://arxiv.org/abs/2512.10501).
- **Open status:** **Closed.** No author-linked code, benchmark cases, map outputs, or evaluator was verified. An exact-title GitHub recreation is not counted because it is not linked to the paper or authors.
- **中文说明:** 论文让双代理零样本配置三维 PCG 工具，但网上同名复刻没有作者身份链，不能当作官方开源。
- **English summary:** Actor–Critic agents configure 3D PCG tools from language, but the reported benchmark and pipeline have no verified official release.

### 51. From Generation to Gameplay: Authoring Race Tracks With Repulsive Curves

- **Year / venue:** 2025, IEEE Transactions on Games.
- **Scope and task/method:** `levels`; repulsive-curve energies optimize editable closed centerlines that are converted into drivable race-track geometry.
- **Evaluation:** geometric quality and smoothness, runtime/editability, and actual gameplay/driving suitability.
- **Official artifacts:** [IEEE DOI](https://doi.org/10.1109/TG.2025.3561107).
- **Open status:** **Closed.** No official curve-authoring implementation, track corpus, playable build, or evaluator was verified.
- **中文说明:** 这篇论文不仅生成曲线，还把它们做成能驾驶的赛道并评价 gameplay，因此属于关卡生成而非赛车代理。
- **English summary:** Repulsive curves are transformed into editable, drivable race tracks and evaluated through geometry and gameplay, with no public package.

### 52. STRUM: End-to-End Generation of Playable Rhythm-Game Charts

- **Year / venue:** 2026, arXiv preprint.
- **Scope and task/method:** `playable-content`; source separation, onset/pitch models, ASR, and spectral rules convert raw audio into multi-instrument Clone Hero/YARG MIDI charts at four difficulties.
- **Evaluation:** per-instrument onset precision/recall/F1, 30-song screened benchmark, confusion analysis, timing study, and component ablations.
- **Official artifacts:** [paper](https://arxiv.org/abs/2605.12135), [official code and benchmark manifest](https://github.com/opria123/strum), [official model weights](https://huggingface.co/opria123/strum).
- **Open status:** **Open.** The generation pipeline, training/evaluation scripts, benchmark results/manifest, and approximately 6 GB of checkpoints are public; source songs remain separately licensed.
- **中文说明:** STRUM 从一首原始录音直接生成决定玩法节奏的多乐器谱面，代码、权重和 benchmark manifest 都已发布。
- **English summary:** STRUM openly converts raw songs into playable multi-instrument rhythm-game charts and releases code, weights, and benchmark metadata.

### 53. Multiverse: Language-Conditioned Multi-Game Level Blending

- **Year / venue:** 2026, arXiv preprint.
- **Scope and task/method:** `levels`; a shared text/level latent representation with multi-positive contrastive supervision supports blending across Mario, Zelda, Lode Runner, and dungeon domains.
- **Evaluation:** text alignment, blend quality, same-/cross-genre results, interpolation behaviour, and zero-shot compositional prompts.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.26782), [official code and data](https://github.com/bic4907/Multiverse-multigame-pcg).
- **Open status:** **Open.** MIT-licensed datasets, annotations, models, Docker setup, training, inference, and text-blend evaluation are public.
- **中文说明:** Multiverse 把四种游戏关卡放进共享表示，用自然语言指定跨游戏结构混合，并支持组合提示的零样本生成。
- **English summary:** Multiverse learns a shared multi-game level space for language-guided blending and zero-shot composition across four domains.

### 54. From World-Gen to Quest-Line

- **Year / venue:** 2026, arXiv/SSRN preprint.
- **Scope and task/method:** `playable-content`; schema-constrained JSON passes through world, NPC, player-character, campaign-quest, and detailed quest-expansion stages.
- **Evaluation:** repeated-run human ratings of structural completeness, internal consistency, narrative coherence, diversity, and actionability.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2604.25482), [official pipeline and run data](https://github.com/borawskiD/PCG_in_RPG_Systems_Using_LLM).
- **Open status:** **Open, API-dependent.** The modular Python pipeline, prompts/configuration, dependencies, structured outputs, and sample experiments are public; GPT access is external.
- **中文说明:** 该系统用显式 JSON 依赖把世界设定一路传递到战役和具体任务，生成的是可供 RPG 实作的结构化可玩内容。
- **English summary:** A public staged pipeline preserves dependencies from RPG world generation through structured campaign and expanded quest content.

### 55. From LLM-Driven Trading Card Generation to Procedural Relatedness

- **Year / venue:** 2026, arXiv preprint.
- **Scope and task/method:** `playable-content`; retrieval over processed card mechanics, a local LLM, diffusion workflows, and export tooling generate personalized Pokémon-style cards with mechanics and art.
- **Evaluation:** 49 participants create 196 cards and rate aesthetics, representativeness, intent realization, and adaptation/co-creation experience.
- **Official artifacts:** [paper](https://arxiv.org/abs/2604.27972), [official pipeline, processed data, workflows, and results](https://github.com/JohannesPfau/generativePokemonTCG).
- **Open status:** **Open.** Scripts, a processed mechanics corpus, prompts/schema, example workflows, and generated/study outputs are public; third-party model/card-tool dependencies remain.
- **中文说明:** 该管线同时生成卡牌机制和画面，并公开检索语料、生成脚本及用户研究输出，不是孤立的卡图生成。
- **English summary:** An open retrieval/LLM/diffusion pipeline co-generates personalized trading-card mechanics and visuals and publishes study outputs.

### 56. Representing and Generating Levels Over Time through Playtrace Reconstructive Partitioning

- **Year / venue:** 2026, Foundations of Digital Games.
- **Scope and task/method:** `levels`; a playtrace-derived “cake” representation captures a level over solution time, and PRP samples/reconstructs Sokoban levels from partitions.
- **Evaluation:** validity and solution diversity against six state-of-the-art PCG approaches.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2607.12097), [ACM DOI](https://doi.org/10.1145/3815598.3815619), [paper-linked repository](https://github.com/emily-halina/PRP-Sokoban).
- **Open status:** **Closed at the cutoff.** The official repository exists but is empty, contradicting the paper's statement that source/cake representations are there; no runnable code or data can be inspected.
- **中文说明:** PRP 用解题轨迹表达关卡随时间的结构，但截止日论文所链接仓库为空，所以必须按 Closed 标注。
- **English summary:** PRP generates valid Sokoban levels from a playtrace-aware representation, but its linked repository was empty at the cutoff.

### 57. Procedural Content Metageneration via Program Search and Continual Abstraction Discovery

- **Year / venue:** 2026, accepted at IEEE Conference on Games.
- **Scope and task/method:** `generator`; an LLM mutates/crosses complete Python generators while Continual Abstraction Discovery extracts validated reusable helpers during search.
- **Evaluation:** 160 complete 50-generation runs across Sokoban, Zelda, Dangerous Dave, and Lode Runner; final fitness, learned-library adoption/calls, and CAD/API ablations.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.17947), [author project page and four example generators](https://github.com/matt-quant-heads-io/procedural-content-metageneration).
- **Open status:** **Partial demo.** Four executable example generators and explanatory media are public, but the evolutionary search/CAD implementation, 160-run dataset, prompts, and evaluator are absent.
- **中文说明:** 这项工作生成的是“关卡生成器程序”本身；作者只公开了四个结果生成器和展示页，尚未公开完整搜索实验。
- **English summary:** LLM program search evolves generators and discovers reusable abstractions; only example generators and media are public.

## F. Recent evaluation and survey readings / 近期评价与综述

### 58. On the Evaluation of Procedural Level Generation Systems

- **Year / venue:** 2024, Foundations of Digital Games.
- **Scope and task/method:** `evaluation survey`; defines a taxonomy spanning evaluation-free descriptions, direct content analysis, simulation/agents, and human studies, then applies it to recent level-generation work.
- **Evaluation:** audits 138 papers and reports inconsistent practices, limited framework/method reuse, and barriers to comparison; it does not rank generators.
- **Official artifacts:** [paper](https://arxiv.org/abs/2404.18657), [official coded data, query exports, analysis, and outputs](https://github.com/KrellFace/PCG_Eval_Survey).
- **Open status:** **Open data.** The raw Web of Science exports, trimmed annotations, analysis code, and visualisation outputs are public.
- **中文说明:** 这篇工作专门研究“关卡生成到底怎么评价”，并公开逐篇编码数据，能解释为什么不同论文的可玩性或多样性分数不能直接横比。
- **English summary:** A modern taxonomy and open coded survey expose weaknesses and inconsistency in procedural-level evaluation practice.

### 59. Procedural Content Generation via Generative Artificial Intelligence

- **Year / venue:** arXiv 2024; Interdisciplinary Information Sciences 2026.
- **Scope and task/method:** `survey`; reviews generative-AI PCG across terrains, levels, items, and stories with special attention to scarce customized training data.
- **Evaluation:** literature synthesis of model families, content domains, and data-efficiency approaches rather than an empirical benchmark.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2407.09013), [journal DOI](https://doi.org/10.4036/iis.2026.r.01).
- **Open status:** **Paper-only by design.** No companion code or review dataset is claimed.
- **中文说明:** 该综述聚焦生成式 AI 如何进入 PCG，以及小样本、单样例和合成数据方法如何缓解游戏内容数据稀缺。
- **English summary:** The survey maps generative-AI approaches to PCG content domains and emphasizes the field's domain-specific data scarcity.

### 60. Procedural Content Generation in Games: A Survey with Insights on Emerging LLM Integration

- **Year / venue:** 2024, AIIDE.
- **Scope and task/method:** `survey`; compares search-based, machine-learning, noise/function-based, hybrid, and LLM PCG by generated content and publication trends.
- **Evaluation:** taxonomy, historical comparison, literature counts, research gaps, and future directions; no generator leaderboard is defined.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2410.15644), [AIIDE DOI](https://doi.org/10.1609/aiide.v20i1.31877).
- **Open status:** **Paper-only by design.** It is a survey without an official code/data companion.
- **中文说明:** 该综述把 LLM 放进搜索、机器学习、传统函数和混合 PCG 的历史脉络，适合用于理解方法边界而非比较单一分数。
- **English summary:** A broad PCG survey situates emerging LLM methods alongside search, ML, constructive, and hybrid approaches.

## G. Additional verified classic generation work / 补核经典生成工作

### 61. Launchpad: A Rhythm-Based Level Generator for 2-D Platformers

- **Year / venue:** online 2010; IEEE Transactions on Computational Intelligence and AI in Games 3(1), 2011. The shorter precursor appeared at FDG 2009.
- **Scope and task/method:** `levels`; a two-tier grammar first generates player-action rhythms and then geometry, joining rhythm groups into parameter-controlled complete 2-D platform levels that are playable by construction.
- **Evaluation:** linearity and leniency plots over 10,000 generated levels characterize expressive range; normalized edit distance and clustering compare rhythm groups and expose generator biases.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TCIAIG.2010.2095855), [author manuscript](https://users.soe.ucsc.edu/~ejw/papers/Smith-Launchpad-TCIAIG-2011.pdf), [FDG 2009 precursor](https://doi.org/10.1145/1536513.1536548), [official legacy demo](https://users.soe.ucsc.edu/~gsmith/launchpad/platformer/), [official visualization and source](https://users.soe.ucsc.edu/~gsmith/launchpad/viztool/).
- **Open status:** **Partial, legacy-only.** The Flash demo and Java/Processing visualization remain downloadable, and the visualization source is exposed, but modern browsers cannot run them directly and the complete level-generator source was not released.
- **Scope decision:** generation is the research product; player physics and playability constraints are used to construct valid levels, not to train or rank a playing policy.
- **中文说明:** Launchpad 用节奏语法和几何语法自动装配保证可玩的完整平台关卡，并以 10,000 个样本分析生成空间；遗留 demo 尚在，但完整生成器源码缺失。
- **English summary:** Launchpad generates guaranteed-playable platform levels from action rhythms and evaluates the generator's expressive range rather than a player's score.

### 62. Variations Forever: Flexibly Generating Rulesets from a Sculptable Design Space of Mini-Games

- **Year / venue:** 2010, IEEE Conference on Computational Intelligence and Games; expanded as an answer-set-programming method paper in IEEE Transactions on Computational Intelligence and AI in Games, 2011.
- **Scope and task/method:** `rules`; answer-set programming declaratively specifies and constrains a code-like mini-game design space, while LPARSE/SMODELS enumerate rulesets that a Flixel-based engine instantiates as playable games. The 2011 paper generalizes the design-space method and also reconstructs a maze generator.
- **Evaluation:** qualitative prototype analysis focuses on design-space flexibility, expressivity, constraint sculpting, and a novel indirect-push solution; the method paper adds worked encodings rather than a generator leaderboard. Automatic game-quality optimization remains future work.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/ITW.2010.5593343), [author manuscript](https://users.soe.ucsc.edu/~amsmith/papers/ieeecig20_vf.pdf), [ASP method extension](https://doi.org/10.1109/TCIAIG.2011.2158545), [extension author manuscript](https://users.soe.ucsc.edu/~amsmith/papers/tciaig-asp4pcg.pdf).
- **Open status:** **Closed.** The paper's public demo returned 404 at the 2026-08-31 cutoff, and no official generator, engine source, design-space package, or evaluation corpus was verified.
- **Scope decision:** the output is a large space of executable game rulesets and playable mini-games; the player explores generated games but no playing policy, return, or win-rate benchmark is proposed.
- **中文说明:** Variations Forever 用 ASP 表达并裁剪小游戏规则空间，再把采样规则实例化为可玩游戏；这是规则生成，不是玩游戏 agent。
- **English summary:** A declarative ASP generator samples executable mini-game rulesets from a sculptable design space, with qualitative rather than policy-based evaluation.

### 63. EGGG: Automated Programming for Game Generation

- **Year / venue:** 2000, IBM Systems Journal.
- **Scope and task/method:** `full-game`; EGGG accepts an abstract game/rule specification, selects compatible reusable implementation components, and composes them into an executable game program.
- **Evaluation:** the paper presents the programming architecture and generated examples, but does not define a standardized quantitative benchmark or comparative user study.
- **Primary sources:** [IBM DOI](https://doi.org/10.1147/sj.393.0782).
- **Open status:** **Closed.** No official source, executable, component library, example corpus, or reproducibility package was verified at the cutoff.
- **Scope decision:** the system's product is an implemented game, not a policy that plays a fixed game.
- **中文说明:** EGGG 从抽象游戏与规则规格选择、组合可复用实现组件，编译出能运行的游戏程序，是早于现代 LLM 的端到端自动游戏编程工作。
- **English summary:** EGGG composes reusable software components from an abstract game specification to produce a functioning game program.

### 64. Procedural Level Design for Platform Games

- **Year / venue:** 2006, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE).
- **Scope and task/method:** `levels`; proposes a four-layer component/pattern/cell/structure representation, physics-aware difficulty estimation, and hill climbing toward requested difficulty for 2-D platform levels.
- **Evaluation:** demonstrates a working pattern builder and example difficulty calculations; the paper explicitly states that the complete cell-and-structure architecture had not yet been implemented.
- **Primary sources:** [AIIDE DOI and proceedings record](https://doi.org/10.1609/aiide.v2i1.18755).
- **Open status:** **Closed.** No official implementation, generated-level corpus, or fixed evaluator package was verified.
- **Scope decision:** it is retained as a foundational generator prototype with its incomplete implementation stated prominently, rather than represented as a finished benchmark.
- **中文说明:** 论文提出平台关的四层生成结构与物理感知难度搜索，但当时只有 pattern builder 已实现，因此按“奠基原型”而非完整系统收录。
- **English summary:** An early platform-level design architecture combines hierarchical patterns with target-difficulty search, although only its pattern-building stage was implemented.

### 65. Automatic Design of Balanced Board Games

- **Year / venue:** 2007, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE).
- **Scope and task/method:** `rules`; a genetic algorithm recombines boards, pieces, victory conditions, and rule mutations into executable Zillions of Games rule files.
- **Evaluation:** each candidate receives 100 self-play games; 500 genetic-algorithm iterations are compared with 500 random samples using balance, draw behavior, and diversity measures.
- **Primary sources:** [AIIDE DOI and proceedings record](https://doi.org/10.1609/aiide.v3i1.18777).
- **Open status:** **Closed.** The experiment depends on the commercial Zillions of Games runtime, and no paper-specific generator, rules corpus, or experiment package was verified.
- **Scope decision:** self-play is used only to evaluate newly generated rule sets; return or playing strength is not the research product.
- **中文说明:** 这项工作直接进化可执行棋类规则文件，并用每个候选 100 局自博弈评价平衡性；自博弈是设计评分器，不是论文目标。
- **English summary:** A genetic algorithm generates executable board-game rules and uses automated matches only to filter for balanced, non-trivial designs.

### 66. Towards Automated Game Design

- **Year / venue:** 2007, AI*IA 2007: Artificial Intelligence and Human-Oriented Computing.
- **Scope and task/method:** `full-game`; uses WordNet and ConceptNet to map requested nouns and verbs through abstract mechanics into concrete J2ME mechanics, controls, graphics, and runnable WarioWare-style micro-games.
- **Evaluation:** demonstrates generated games running on the prototype platform and analyzes the design pipeline; a systematic user study or common benchmark is left to future work.
- **Primary sources:** [Springer DOI and chapter record](https://doi.org/10.1007/978-3-540-74782-6_54).
- **Open status:** **Closed.** No official generator, J2ME mechanic library, output corpus, or evaluation package was verified.
- **Scope decision:** this is a distinct system and authorship lineage from the 2008 evolutionary study *An Experiment in Automatic Game Design*; the two are not collapsed into one version family.
- **中文说明:** 系统把自然语言概念映射为机制、控制与图形，生成可运行的 J2ME 微游戏；它与 2008 年进化式自动游戏设计论文不是同一系统或扩展版。
- **English summary:** Semantic knowledge bases drive the assembly of runnable J2ME micro-games, independently of the better-known 2008 evolutionary automatic-design experiment.

### 67. Towards Automatic Personalised Content Creation for Racing Games

- **Year / venue:** 2006 precursor, *Making Racing Fun Through Player Modeling and Track Evolution*; expanded at the 2007 IEEE Conference on Computational Intelligence and Games.
- **Scope and task/method:** `levels`; learns models of individual driving behavior and evolves smooth closed racing tracks whose challenge and speed profile target each modeled player.
- **Evaluation:** models five drivers and compares track representations and initialization schemes through controller progress, variance, speed, and qualitative personalization results.
- **Primary sources:** [IEEE DOI for the expanded paper](https://doi.org/10.1109/CIG.2007.368106), [UCL institutional record for the 2006 precursor](https://discovery.ucl.ac.uk/id/eprint/1330829/).
- **Open status:** **Closed.** No official track generator, player-model code, generated outputs, or evaluation package was verified.
- **Scope decision:** player controllers supply preference/difficulty estimates for generated tracks; the evaluated output is personalized playable content, not driving-policy performance.
- **中文说明:** 论文学习五名车手的行为，再进化与个人能力相匹配的闭合赛道；玩家模型和控制器只服务于赛道生成与评价。
- **English summary:** Driver models guide evolutionary search toward personalized playable race tracks rather than toward a stronger driving agent.

### 68. Towards Automatic Personalized Content Generation for Platform Games

- **Year / venue:** 2010, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE).
- **Scope and task/method:** `levels`; searches Mario level parameters using learned player-experience models and generates the next level for a particular playing style.
- **Evaluation:** experience models use 327 players and 1,308 sessions; adapted levels are tested with two controllers and people, and 60% of the ten direct-comparison participants prefer the adapted level.
- **Primary sources:** [AIIDE DOI and proceedings record](https://doi.org/10.1609/aiide.v6i1.12399).
- **Open status:** **Closed.** No official adaptation code, trained player models, generated-level corpus, or experiment data was verified.
- **Scope decision:** related player-model-only papers that stop before generating content are excluded; this paper is included because it actually searches parameters and emits the personalized level.
- **中文说明:** 与只建立玩家体验模型的前作不同，这篇论文实际搜索 Mario 关卡参数并生成个性化下一关，因此属于生成游戏内容。
- **English summary:** Learned experience models are operationalized to search and emit personalized Mario levels, rather than being evaluated only as player models.

### 69. Polymorph: A Model for Dynamic Level Generation

- **Year / venue:** 2010, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE).
- **Scope and task/method:** `levels`; learns difficulty and player-skill models, then generates short platform segments online so structural challenge follows current performance.
- **Evaluation:** uses 211 players and 2,258 segment playthroughs; the learned model orders difficulty pairs, and the paper examines dynamically selected example segments.
- **Primary sources:** [AIIDE DOI and proceedings record](https://doi.org/10.1609/aiide.v6i1.12417).
- **Open status:** **Closed.** The paper historically linked official Polymorph and data-collector Flash applications, but those links now fail; no generator source, learned model, or experiment data remain available.
- **Scope decision:** online adaptation changes the playable level geometry itself, so this is dynamic content generation rather than a playing-agent task.
- **中文说明:** Polymorph 根据玩家当前表现在线生成下一段平台关几何；其核心产物是动态关卡，而不是控制角色的策略。
- **English summary:** Polymorph continually generates platform segments whose structural difficulty follows an estimated player-skill trajectory.

### 70. Tanagra: Reactive Planning and Constraint Solving for Mixed-Initiative Level Design

- **Year / venue:** a 2010 FDG expressive-range precursor; IEEE Transactions on Computational Intelligence and AI in Games, 2011.
- **Scope and task/method:** `levels`; combines reactive planning with numerical constraints to autonomously generate or regenerate rhythm-paced 2-D platform levels around designer edits while preserving reachability.
- **Evaluation:** maps linearity and leniency over 10,000 unique generated levels and demonstrates responsive co-creation operations.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TCIAIG.2011.2159716), [2010 expressive-range precursor](https://doi.org/10.1145/1814256.1814260), [author manuscript](https://users.soe.ucsc.edu/~ejw/papers/Smith-Tanagra-TCIAIG-2011.pdf), [official legacy demonstration](https://users.soe.ucsc.edu/~gsmith/tanagra/v2_demo/demo.htm).
- **Open status:** **Closed, legacy demo only.** The Flash demonstration remains online, but no generator source or runnable reproducibility package was verified.
- **Scope decision:** mixed initiative does not make the work editor-only: Tanagra contains a substantive automatic generator that can create and repair playable levels without requiring every placement from a human.
- **中文说明:** Tanagra 既能响应设计师编辑，也能自主规划并约束求解出可达平台关；因包含实质自动生成器，归入关卡核心分区。
- **English summary:** Reactive planning and constraint solving support both autonomous generation and responsive co-creation of reachable platform levels.

### 71. Sentient Sketchbook: Computer-Aided Game Level Authoring

- **Year / venue:** 2013, Foundations of Digital Games.
- **Scope and task/method:** `levels`; feasible-infeasible novelty/objective search generates playable strategy-map alternatives in real time from the designer's current sketch.
- **Evaluation:** compares constrained-search methods over 20 runs and reports 24 design sessions with five industry experts.
- **Primary sources:** [official paper PDF](https://sentientsketchbook.com/research/sentient_sketchbook.pdf), [official project](https://sentientsketchbook.com/), [official 2014 JAR download](https://sentientsketchbook.com/download.php).
- **Open status:** **Partial, legacy-only.** A runnable historical JAR remains available, but no source, modern runtime package, or complete experiment data was verified.
- **Scope decision:** although mixed-initiative, the system automatically proposes complete playable alternatives and has a primary generator evaluation; the related map-sketch generation work is treated as the same system family rather than counted again.
- **中文说明:** Sentient Sketchbook 会从当前草图实时生成完整、可玩的策略地图备选，并非只提供手工编辑界面，因此列入关卡核心分区。
- **English summary:** The tool automatically searches for playable strategy-map alternatives around a designer sketch and exposes them in a mixed-initiative workflow.

### 72. Learning to Generate Video Game Maps Using Markov Models

- **Year / venue:** 2013–2016, AIIDE conference series and IEEE Transactions on Computational Intelligence and AI in Games.
- **Scope and task/method:** `levels`; learns single-layer and hierarchical multi-dimensional Markov models from human-authored maps, then samples new Mario, Lode Runner, and Kid Icarus levels.
- **Evaluation:** compares playability, linearity, and leniency with non-hierarchical/manual hierarchies and Mario competition generators; the 2015 automatically learned hierarchy reaches 66% Mario playability.
- **Primary sources:** [journal version](https://doi.org/10.1109/TCIAIG.2016.2623560), [2013 AIIDE paper](https://doi.org/10.1609/aiide.v9i2.12586), [2014 AIIDE hierarchy paper](https://doi.org/10.1609/aiide.v10i1.12708), [2015 AIIDE paper](https://doi.org/10.1609/aiide.v11i1.12794). The same family also includes the FDG 2014 paper *Experiments in Map Generation Using Markov Chains*, whose legacy official URL is HTTP-only.
- **Open status:** **Closed.** The 2015 paper historically linked Mario/Lode Runner training sets, but the package is no longer visible; no official generator code, trained models, fixed data package, or evaluation scripts were verified.
- **Scope decision:** the five records are methodological extensions of the same map-generation lineage and are counted as one version family, not five papers. Later constrained-sampling, domain-transfer, training-data, movement-model, and multi-layer branches make independent generation contributions and are listed separately as sources 87–91.
- **中文说明:** 这一版本族从单层多维 Markov 模型逐步扩展到自动学习层级结构，直接生成 Mario、Lode Runner 与 Kid Icarus 地图；五个版本合并计数一次。
- **English summary:** A sequence of Markov-map papers progresses from flat to learned hierarchical models for sampling playable platform and puzzle levels.

### 73. Procedural Level Generation Using Occupancy-Regulated Extension

- **Year / venue:** 2010, IEEE Conference on Computational Intelligence and Games.
- **Scope and task/method:** `levels`; iteratively attaches human-authored geometry chunks at possible player-occupancy anchors, supporting varied platform spaces and mixed-initiative extension at arbitrary scales.
- **Evaluation:** critically analyzes outputs from an Infinite Mario implementation with 42 chunks; complete levels take about 15 seconds to generate. No experimental playtest was run, and the system explicitly does not guarantee playability.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/ITW.2010.5593333), [author manuscript](https://www.cs.hmc.edu/~pmawhorter/research/papers/procedural_level_generation_using_occupancy_regulated_extension-Mawhorter_Mateas-2010.pdf).
- **Open status:** **Closed.** No official generator, chunk library, generated-level corpus, or evaluator package was verified.
- **Scope decision:** the algorithm's output is newly constructed level geometry; occupancy is a construction control, not a gameplay-return objective.
- **中文说明:** ORE 在玩家可能占据的锚点处拼接人工几何块，直接生成多样的平台关空间；论文明确说明当时尚不保证可玩。
- **English summary:** ORE assembles authored chunks at player-occupancy anchors to generate varied platform spaces, without claiming a playability guarantee.

### 74. Towards Multiobjective Procedural Map Generation / Multiobjective Exploration of the StarCraft Map Space

- **Year / venue:** 2010, FDG PCGames workshop and IEEE Conference on Computational Intelligence and Games.
- **Scope and task/method:** `levels`; multiobjective evolutionary search generates complete RTS maps including terrain, bases, and resources, with the expanded paper instantiating the representation for StarCraft.
- **Evaluation:** Pareto-front approximations expose trade-offs among partly conflicting predicted-player-experience objectives such as fairness, resource/base placement, paths, and terrain characteristics; each point is a viable candidate map.
- **Primary sources:** [StarCraft paper DOI](https://doi.org/10.1109/ITW.2010.5593346), [generic precursor DOI](https://doi.org/10.1145/1814256.1814259), [precursor institutional manuscript](https://www.um.edu.mt/library/oar/bitstream/123456789/81279/1/Towards_multiobjective_procedural_map_generation_2010.pdf), [StarCraft institutional manuscript](https://www.um.edu.mt/library/oar/bitstream/123456789/29280/1/Multiobjective_exploration_of_the_starcraft_map_space_2010.pdf).
- **Open status:** **Closed.** The papers and institutional manuscripts are available, but no official map generator, StarCraft exporter, experiment data, or evaluator release was verified.
- **Scope decision:** the Pareto fronts rank generated maps and support selection; no RTS-playing agent or win-rate benchmark is the research product.
- **中文说明:** 该版本族从通用策略地图扩展到完整 StarCraft 地图，用 Pareto 前沿呈现公平性、资源和地形目标的权衡。
- **English summary:** Multiobjective evolution produces complete RTS maps and exposes design trade-offs as Pareto fronts for automatic or assisted selection.

### 75. Adventures in Level Design / Generating Missions and Spaces for Adaptable Play Experiences

- **Year / venue:** 2010, FDG PCGames workshop; extended in IEEE Transactions on Computational Intelligence and AI in Games, 2011.
- **Scope and task/method:** `levels`; generative grammars first rewrite mission graphs and then construct spatial layouts that make the generated action-adventure progression executable.
- **Evaluation:** generated case studies demonstrate coherent mission-to-space mappings, adaptation operations, and the expressive consequences of the grammar rules; no common quantitative leaderboard is defined.
- **Primary sources:** [journal DOI](https://doi.org/10.1109/TCIAIG.2011.2149523), [2010 precursor DOI](https://doi.org/10.1145/1814256.1814257), [institutional author manuscript](https://research.hva.nl/files/149264/453867_Dormans_Bakkes_-_Generating_Missions_and_Spaces_for_Adaptable_Play_Experiences.pdf).
- **Open status:** **Closed.** An official institutional manuscript is available, but no generator, grammar package, output corpus, or evaluator was verified.
- **Scope decision:** missions and spaces are jointly generated as playable structure rather than as prose-only narrative or a policy trace.
- **中文说明:** 系统先生成任务图，再生成能承载该任务进程的空间，把任务与关卡联合起来，而不是只写故事文本。
- **English summary:** Coupled grammars generate an action-adventure mission graph and the spatial level needed to enact that mission.

### 76. Towards a Generic Framework for Automated Video Game Level Creation / A Generic Approach to Challenge Modeling

- **Year / venue:** 2010, EvoApplications; extended in IEEE Transactions on Computational Intelligence and AI in Games, 2011.
- **Scope and task/method:** `levels`; feasible-infeasible two-population evolution separates hard play/connectivity constraints from optimization of a top-down target challenge model.
- **Evaluation:** the precursor generates example levels for two genres, and the extended system studies valid output and controllable challenge behavior across domain definitions.
- **Primary sources:** [journal DOI](https://doi.org/10.1109/TCIAIG.2011.2161310), [framework precursor](https://doi.org/10.1007/978-3-642-12239-2_14).
- **Open status:** **Closed.** No official implementation, domain encodings, generated-level set, or evaluation scripts were verified.
- **Scope decision:** simulated feasibility and challenge estimates score generated levels; agent performance is an evaluator signal, not the output.
- **中文说明:** FI-2Pop 把玩法硬约束与目标挑战度分开搜索，可跨游戏类型生成连通、可玩的目标难度关卡。
- **English summary:** A generic FI-2Pop framework evolves feasible levels toward top-down challenge targets across multiple game genres.

### 77. Search-Based Procedural Generation of Maze-Like Levels

- **Year / venue:** 2011, IEEE Transactions on Computational Intelligence and AI in Games.
- **Scope and task/method:** `levels`; evolutionary search constructs connected, solvable maze-like layouts under explicit path and structural objectives instead of sampling unconstrained random mazes.
- **Evaluation:** compares representations and operators through path, connectivity, and structural properties of generated populations.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TCIAIG.2011.2138707).
- **Open status:** **Closed.** No official generator, benchmark instances, generated corpus, or experiment package was verified.
- **Scope decision:** the mazes themselves are the optimized artifact; solver/path calculations only evaluate those artifacts.
- **中文说明:** 论文用进化搜索直接构造连通、可解的迷宫式关卡，并以路径和结构指标筛选，而不是训练走迷宫策略。
- **English summary:** Evolutionary search generates solvable maze-like levels and evaluates their path and topology rather than an agent's return.

### 78. Evolving Interesting Maps for a First Person Shooter

- **Year / venue:** 2011, EvoApplications.
- **Scope and task/method:** `levels`; evolves complete maps loadable in Cube 2 and uses bot matches plus average fighting time only as a proxy fitness for map interest.
- **Evaluation:** compares four map representations and finds substantial differences in their ability to produce interesting, playable FPS layouts.
- **Primary sources:** [Springer DOI and chapter record](https://doi.org/10.1007/978-3-642-20525-5_7).
- **Open status:** **Closed.** No official evolutionary system, Cube 2 map corpus, bot configuration, or evaluator package was verified.
- **Scope decision:** bots evaluate newly generated FPS maps; stronger bot play, score, or win rate is not the paper's contribution.
- **中文说明:** 系统进化可载入 Cube 2 的完整 FPS 地图，并用 bot 平均交战时间评价地图趣味性；bot 只是评分器。
- **English summary:** Evolution generates playable Cube 2 maps, while bot fighting time serves only as a map-quality estimate.

### 79. Evolving Levels for Super Mario Bros Using Grammatical Evolution

- **Year / venue:** 2012, IEEE Conference on Computational Intelligence and Games; personalized extension at AIIDE 2012.
- **Scope and task/method:** `levels`; grammatical evolution composes complete Mario levels from a compact design grammar, while the extension uses learned engagement, frustration, and challenge models as fitness functions for player-specific generation.
- **Evaluation:** compares expressive range, aesthetic and similarity measures against feature-based and original generators; the extension uses experience models trained from more than 1,500 crowd-sourced game sessions.
- **Primary sources:** [CIG DOI](https://doi.org/10.1109/CIG.2012.6374170), [personalized AIIDE extension](https://doi.org/10.1609/aiide.v8i1.12501), [institutional author manuscript](https://www.um.edu.mt/library/oar/bitstream/123456789/22937/1/Evolving_Levels_for_Super_Mario_Bros_Using_Grammat.pdf).
- **Open status:** **Closed.** No official GE implementation, grammar/evolution package, generated corpus, player-model package, or evaluation scripts were verified.
- **Scope decision:** this is distinct from source 68's four-parameter exhaustive-search adapter: the generative representation and search space are replaced by grammatical evolution.
- **中文说明:** 这一族用设计语法进化完整 Mario 关卡，并在扩展版中用众包玩家体验模型优化个性化内容；它与来源 68 的小参数穷举适配器不同。
- **English summary:** Grammatical evolution generates complete Mario levels and later optimizes them against learned player-experience models.

### 80. Procedural Content Generation Using Patterns as Objectives

- **Year / venue:** 2014, EvoApplications.
- **Scope and task/method:** `levels`; represents Mario-like levels as sequences of micro-pattern slices extracted from human levels and evolves them toward meso-pattern objectives; the multi-level extension adds macro-pattern composition.
- **Evaluation:** studies the distributions of micro-, meso-, and macro-patterns, showing recognizable source style with substantial geometric variation.
- **Primary sources:** [Springer DOI and chapter record](https://doi.org/10.1007/978-3-662-45523-4_27), [multi-level extension](https://doi.org/10.1109/CIG.2014.6932909).
- **Open status:** **Closed.** No official generator, extracted-pattern dataset, generated-level corpus, or analysis package was verified.
- **Scope decision:** design patterns are search objectives for newly generated levels, not labels for analyzing a fixed corpus alone.
- **中文说明:** 系统把人工关卡切片作为微观模式，以更高层的中观设计模式作为进化目标，直接生成新的 Mario 风格关卡。
- **English summary:** Evolution recombines human-level slices while optimizing for larger design patterns, retaining style without copying whole levels.

### 81. Linear Levels Through N-Grams

- **Year / venue:** 2014, 18th International Academic MindTrek Conference (AcademicMindTrek 2014), pp. 200–206.
- **Scope and task/method:** `levels`; learns n-gram transition models over vertical slices of human-authored Mario levels and samples new left-to-right levels at different history lengths.
- **Evaluation:** compares n-gram orders through generated tile/pattern distributions, structural characteristics, and expressive-range behavior.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/2676467.2676506), [official IT University research record](https://pure.itu.dk/en/publications/linear-levels-through-n-grams/).
- **Open status:** **Closed.** No official implementation, trained models, fixed corpus snapshot, or evaluation scripts were verified.
- **Scope decision:** this vertical-slice sequence model is methodologically separate from source 72's tile-level multi-dimensional Markov family.
- **中文说明:** 论文从 Mario 纵向切片学习 n-gram 并采样横向关卡；它与来源 72 的二维多维 Markov 模型不是同一系统。
- **English summary:** Vertical-slice n-grams learn local sequence structure from Mario levels and sample new linear platform stages.

### 82. MCMCTS PCG 4 SMB: Monte Carlo Tree Search to Guide Platformer Level Generation

- **Year / venue:** 2015, AIIDE Experimental AI in Games workshop.
- **Scope and task/method:** `levels`; uses Mario-trained Markov transitions as MCTS moves and rollouts, pruning unsolvable branches while exposing designer controls for gaps, enemies, and rewards.
- **Evaluation:** uses 200 rollouts per move to generate 320-slice levels in under 30 seconds with a near-playability guarantee; a player study probes eight parameter variants and downstream experience models.
- **Primary sources:** [AIIDE DOI and open proceedings paper](https://doi.org/10.1609/aiide.v11i3.12816).
- **Open status:** **Closed.** No official generator, training corpus, player-study data, or evaluator release was verified.
- **Scope decision:** MCTS is repurposed as a content search procedure; the research output is a generated Mario level, not a Mario-playing policy.
- **中文说明:** MCMCTS 把通常用于玩游戏的 MCTS 改作关卡搜索，用 Markov 转移扩展并剪枝不可解 Mario 关卡。
- **English summary:** MCTS guides a Markov generator toward solvable, designer-controlled Mario levels rather than toward stronger game play.

### 83. Sampling Hyrule: Multi-Technique Probabilistic Level Generation for Action Role Playing Games

- **Year / venue:** 2015, AIIDE Experimental AI in Games workshop; builds on the FDG 2015 paper *Data-Driven Learning of Level Topology*.
- **Scope and task/method:** `levels`; samples Zelda dungeon topology from a Bayesian network, generates individual rooms by interpolation in a PCA-compressed space, and repairs or resamples constraint violations.
- **Evaluation:** checks room accessibility, key-door ordering, required special-room types, and completion constraints; 20 dungeons are sampled at each of the 12-, 35-, and 47-room scales.
- **Primary sources:** [AIIDE DOI and open proceedings paper](https://doi.org/10.1609/aiide.v11i3.12817).
- **Open status:** **Closed.** No official generator, learned Bayesian/PCA models, Zelda corpus, generated output set, or evaluator package was verified.
- **Scope decision:** the predecessor learns topology; Sampling Hyrule operationalizes it into an actual generator, so the two are one development lineage rather than two counted entries.
- **中文说明:** 系统从 Zelda 人工地牢学习拓扑和房间表示，再采样并修复成可通关地牢；前作与生成版合并为一个版本族。
- **English summary:** A learned Bayesian topology and PCA room model are combined to sample constraint-valid, completable Zelda-style dungeons.

### 84. Automatic Generation of Game Elements via Evolution

- **Year / venue:** 2010, IEEE Conference on Computational Intelligence and Games.
- **Scope and task/method:** `playable-content`; uses evolutionary search and dynamic programming to generate solvable chess-maze and chromatic-puzzle instances under fixed rules, creating new challenge layouts rather than cosmetic assets.
- **Evaluation:** runs 540 chess-parameter experiments; both targeted conditions achieve 30/30 successes, and seven groups of 30 inspected outputs contain no duplicates.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/ITW.2010.5593341).
- **Open status:** **Closed.** No official generator, puzzle corpus, solver/evaluator, or experiment package was verified.
- **Scope decision:** the outputs are playable puzzle instances, consistent with the collection's inclusion of Sokoban, Connections, and other generated puzzles.
- **中文说明:** 论文进化新的 chess maze 和 chromatic puzzle 可玩实例；固定的是规则，生成的是决定挑战的谜题结构，因此不是纯资产。
- **English summary:** Evolution produces complete playable instances in two puzzle domains and is evaluated as content search rather than game play.

### 85. Alone We Can Do So Little, Together We Can Do So Much: A Combinatorial Approach for Generating Game Content

- **Year / venue:** 2014, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE).
- **Scope and task/method:** `levels`; trains non-negative matrix factorization on 5,000 200×15 Mario levels from five dissimilar generators, then recombines learned component patterns into loadable new levels.
- **Evaluation:** expressivity metrics show that the combined generator can resemble each source generator while covering a wider and more novel content space.
- **Primary sources:** [AIIDE DOI and open proceedings paper](https://doi.org/10.1609/aiide.v10i1.12729).
- **Open status:** **Closed.** No official NMF generator, five-source training set, generated corpus, or analysis scripts were verified.
- **Scope decision:** this paper implements and evaluates a new combinatorial generator; it is not merely a comparison of the five input systems.
- **中文说明:** 系统学习五个差异明显的 Mario 生成器所产模式并重新组合，能覆盖比任一单独生成器更宽的新颖内容空间。
- **English summary:** NMF learns from five Mario generators and recombines their component patterns into a broader joint generative space.

### 86. Cellular Automata for Real-Time Generation of Infinite Cave Levels

- **Year / venue:** 2010, FDG PCGames workshop.
- **Scope and task/method:** `levels`; generates Cave Crawler cave-map regions with cellular automata on demand, allowing an effectively infinite playable level to expand during play.
- **Evaluation:** ten-run timing tests report about `1.4×10^-4 ms` for random-map generation, `4.1×10^-1 ms` for cellular-automata maps, and 349 ms for a 3×3 base grid, testing real-time feasibility rather than player performance.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/1814256.1814266).
- **Open status:** **Closed.** No official Cave Crawler generator, source, generated-map corpus, or performance harness was verified.
- **Scope decision:** the paper's output is an indefinitely extending playable cave map; generation-time measurements are system evaluation, not gameplay-agent metrics.
- **中文说明:** 论文在 Cave Crawler 游玩过程中按需生成洞穴区域，使地图近似无限扩展；耗时实验评价生成器能否实时运行。
- **English summary:** Cellular automata generate cave regions online so a Cave Crawler level can expand indefinitely within real-time timing budgets.

### 87. Controllable Procedural Content Generation via Constrained Multi-Dimensional Markov Chain Sampling

- **Year / venue:** 2016, Twenty-Fifth International Joint Conference on Artificial Intelligence (IJCAI-16).
- **Scope and task/method:** `levels`; adds global constraints and constrained sampling to learned multi-dimensional Markov chains so the generator can target structural requirements in Super Mario Bros. and Kid Icarus maps.
- **Evaluation:** samples 100 maps for every feasible algorithm–constraint-set combination and compares valid samples, playability, and satisfaction of the requested structural controls. Lode Runner is mentioned only as future work, not as an evaluated domain.
- **Primary sources:** [official IJCAI abstract page](https://www.ijcai.org/Abstract/16/116), [official proceedings PDF](https://www.ijcai.org/Proceedings/16/Papers/116.pdf).
- **Open status:** **Closed.** No official implementation, constraint definitions, trained models, fixed training corpus, generated-map set, or evaluation package was verified.
- **Scope decision:** constrained sampling is a substantive controllable-generation contribution beyond source 72's learned hierarchy, so the paper is listed separately rather than hidden inside that lineage.
- **中文说明:** 论文把全局约束直接纳入多维 Markov 采样，在 Mario 与 Kid Icarus 上生成满足结构控制的地图；Lode Runner 只出现在未来工作中。
- **English summary:** Global constraints steer MdMC sampling toward controllable Mario and Kid Icarus maps instead of merely filtering unconstrained samples afterward.

### 88. An Approach to Domain Transfer in Procedural Content Generation of Two-Dimensional Videogame Levels

- **Year / venue:** 2016, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE).
- **Scope and task/method:** `levels`; learns tile mappings among Super Mario Bros., Kid Icarus, and Kid Kool so a probabilistic generator can train on level data from a structurally related game.
- **Evaluation:** compares human-authored, random, and automatically learned mappings through likelihood, linearity, leniency, and the expressive spaces of generated levels.
- **Primary sources:** [AIIDE DOI and open proceedings record](https://doi.org/10.1609/aiide.v12i1.12853).
- **Open status:** **Closed.** No official transfer implementation, tile mappings, trained models, fixed cross-domain corpus, generated output set, or evaluation scripts were verified.
- **Scope decision:** the paper contributes and evaluates a distinct domain-transfer generator rather than another parameter setting of the source 72 hierarchy.
- **中文说明:** 系统自动学习 Mario、Kid Icarus 与 Kid Kool 间的瓷砖映射，让关卡生成器可以迁移使用另一款游戏的训练数据。
- **English summary:** Learned cross-game tile mappings let a probabilistic generator transfer level structure among three 2-D platformers.

### 89. Studying the Effects of Training Data on Machine Learning-Based Procedural Content Generation

- **Year / venue:** 2017, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE).
- **Scope and task/method:** `levels` evaluation; trains MdMC and LSTM Mario generators on systematically varied quantities and qualities of human-authored level data to isolate how the corpus changes generated content.
- **Evaluation:** evaluates 132 trained models through expressive volume, plagiarism, validity/quality, and diversity rather than through player-agent return.
- **Primary sources:** [AIIDE DOI and open proceedings record](https://doi.org/10.1609/aiide.v13i1.12930).
- **Open status:** **Closed.** No official 132-model set, controlled training subsets, generated-level corpus, training code, or analysis package was verified.
- **Scope decision:** this is retained as a generator-specific evaluation study: its experimental objects and outcomes are trained content generators and their emitted Mario levels, not policies that play Mario.
- **中文说明:** 论文训练 132 个 MdMC/LSTM Mario 生成模型，专门研究训练数据数量与质量怎样改变生成内容，因此属于生成器评价而非玩游戏研究。
- **English summary:** A controlled 132-model study measures how the amount and quality of training data affect Mario PCGML outputs.

### 90. Player Movement Models for Video Game Level Generation

- **Year / venue:** 2017, Twenty-Sixth International Joint Conference on Artificial Intelligence (IJCAI-17).
- **Scope and task/method:** `levels`; learns action and surrounding-conditioned movement likelihoods from Mario gameplay video, then uses the movement model to guide MdMC/VLR level sampling toward plausible human traversal paths.
- **Evaluation:** compares conditioned variants through path likelihood, playability, linearity, leniency, and generated-level examples; player movement is a generation constraint, not a policy-performance target.
- **Primary sources:** [IJCAI DOI](https://doi.org/10.24963/ijcai.2017/105), [official proceedings PDF](https://www.ijcai.org/proceedings/2017/0105.pdf), [author experiment repository](https://bitbucket.org/Sam_Snodgrass/ijcai_2017).
- **Open status:** **Partial, legacy/unlicensed.** The Bitbucket repository contains code, training data, and sampled levels, but no license, maintained environment, or modern reproduction instructions were verified.
- **Scope decision:** learning a player model is an intermediate step; the paper's implemented output is newly sampled Mario geometry conditioned on likely human paths.
- **中文说明:** 系统从 Mario 游玩视频学习移动似然，再把它作为关卡采样约束；代码、训练数据与样例仍在 Bitbucket，但没有许可证或现代环境。
- **English summary:** Movement patterns learned from video steer probabilistic generation toward Mario levels with plausible human traversal paths.

### 91. Procedural Level Generation Using Multi-Layer Level Representations with MdMCs

- **Year / venue:** 2017, IEEE Conference on Computational Intelligence and Games; Lode Runner extension at the AIIDE Experimental AI in Games workshop.
- **Scope and task/method:** `levels`; couples structural, path, and auxiliary semantic layers so MdMC sampling preserves relationships that one tile layer misses. Mario uses structural/path/height layers; the extension uses structural/path/section layers for Lode Runner.
- **Evaluation:** compares layer combinations and generated maps through playability and structural/style characteristics in Mario and Lode Runner.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2017.8080447), [official CIG paper](https://cig2017.com/wp-content/uploads/2017/08/paper_9.pdf), [Lode Runner extension](https://doi.org/10.1609/aiide.v13i2.12966).
- **Open status:** **Closed.** No official generator, aligned multilayer corpus, trained models, generated output set, or evaluation scripts were verified.
- **Scope decision:** the CIG paper and its Lode Runner extension are one multilayer-representation family; their explicit cross-layer generation contribution is separate from the flat/hierarchical map lineage in source 72.
- **中文说明:** 多层表示把结构、路径和高度/分区共同建模，在 Mario 与 Lode Runner 中保留单层瓷砖表示容易丢失的跨层关系。
- **English summary:** Coupled semantic layers let MdMCs sample levels whose geometry remains consistent with traversable paths and higher-level structure.

### 92. Game Level Generation from Gameplay Videos

- **Year / venue:** 2015 workshop precursor *Toward Game Level Generation from Gameplay Videos*; expanded at AIIDE 2016.
- **Scope and task/method:** `levels`; extracts Mario geometry and player movement from raw gameplay videos without source maps, learns a probabilistic graph over observed chunks, and assembles complete new levels.
- **Evaluation:** extracts 13,492 chunks from nine videos, compares generated style likelihood with existing generators, and evaluates complete generated levels in a 73-person play study.
- **Primary sources:** [AIIDE DOI and open proceedings record](https://doi.org/10.1609/aiide.v12i1.12861).
- **Open status:** **Closed.** No official video-processing pipeline, source-video set, learned graph, generator, generated-level corpus, comparison code, or player-study data was verified.
- **Scope decision:** the 2015 precursor and 2016 full paper are one development family; this probabilistic-graph pipeline is distinct from source 29's player-tailored LSTM generator.
- **中文说明:** 该版本族在没有原始地图文件的情况下，从九段 Mario 视频提取 13,492 个片段并学习概率图，再装配完整新关卡。
- **English summary:** Geometry and motion recovered from raw Mario videos train a probabilistic graph that assembles full playable levels.

### 93. Autoencoders for Level Generation, Repair, and Recognition

- **Year / venue:** 2016, ICCC workshop paper.
- **Scope and task/method:** `levels`; trains an autoencoder over small Mario tile windows and decodes noisy or incomplete inputs to generate new tiles, repair damaged regions, and recognize level style.
- **Evaluation:** uses 22 Mario maps and 4,366 windows in a proof-of-concept analysis of reconstruction, noise-driven generation, repair, and recognition.
- **Primary sources:** [archived author manuscript](https://web.archive.org/web/20230507072222id_/http%3A%2F%2Fjulian.togelius.com%2FJain2016Autoencoders.pdf).
- **Open status:** **Closed.** No official code, trained autoencoder, fixed data split, generated/repaired corpus, or evaluation package was verified.
- **Scope decision:** the system actually emits and repairs game-level tiles; recognition is one of three tested uses, not the sole task.
- **中文说明:** Autoencoder 从 Mario 小窗口学习表示，并通过解码含噪或缺失输入来生成与修复瓷砖；识别只是并列用途之一。
- **English summary:** A small autoencoder proof of concept decodes noisy Mario windows for generation and repair as well as style recognition.

### 94. Composing Video Game Levels with Music Metaphors through Functional Scaffolding

- **Year / venue:** 2015, First Computational Creativity and Games Workshop.
- **Scope and task/method:** `levels`; treats Mario tile types as musical voices, learns accompaniment relationships with NEAT, and composes the voices into complete playable levels through functional scaffolding.
- **Evaluation:** qualitatively analyses generated examples and the learned functional relationships among tile voices as a proof of concept rather than defining a shared benchmark.
- **Primary sources:** [archived author manuscript](https://web.archive.org/web/20160903064341id_/http%3A%2F%2Fjulian.togelius.com%2FHoover2015Composing.pdf).
- **Open status:** **Closed.** No official generator, training corpus, evolved-network set, generated levels, or evaluator was verified.
- **Scope decision:** the music metaphor is an internal compositional representation; the output is a complete Mario level, so this is not music-asset generation.
- **中文说明:** 论文把 Mario 瓷砖类型视作音乐声部并学习其“伴奏”关系，最终产物仍是完整可玩关卡，而不是游戏音乐。
- **English summary:** Learned accompaniment relations among tile “voices” scaffold the composition of complete Mario levels.

### 95. Online Level Generation in Super Mario Bros via Learning Constructive Primitives

- **Year / venue:** 2016, IEEE Conference on Computational Intelligence and Games; expanded online in 2017 and in IEEE Transactions on Games 10(2), 2018.
- **Scope and task/method:** `levels`; learns short constructive primitives through active designer feedback, composes them online into quality-controlled Mario levels, and in the journal extension adapts generated difficulty from live player performance.
- **Evaluation:** compares generators over 100-level sets, maps ten expressive ranges of 100 levels each, and reports about 0.057 seconds to construct a 200×15 level.
- **Primary sources:** [conference DOI](https://doi.org/10.1109/CIG.2016.7860397), [institutional author manuscript](https://pure.manchester.ac.uk/ws/files/37088685/ieee_cig2016.pdf), [journal DOI](https://doi.org/10.1109/TCIAIG.2017.2740210), [author project and downloads](https://staff.cs.manchester.ac.uk/~shipa/mario.html).
- **Open status:** **Partial, legacy demos.** Executable online/adaptive generators and tutorials remain downloadable. The source archive is password-restricted to non-commercial use, and no experiment data, trained primitive package, or maintained build was verified.
- **Scope decision:** the 2016 online generator and 2018 adaptive expansion are one constructive-primitives family; adaptation changes generated geometry rather than optimizing a Mario-playing policy.
- **中文说明:** 系统从设计师反馈学习构造原语，实时组合 Mario 关卡并在扩展版中动态适配难度；历史可执行 demo 尚存，但源码受密码和非商业用途限制。
- **English summary:** Learned constructive primitives support fast online Mario generation and later real-time difficulty adaptation, with only legacy demos still openly downloadable.

### 96. Autoencoder and Evolutionary Algorithm for Level Generation in Lode Runner

- **Year / venue:** 2019, IEEE Conference on Games.
- **Scope and task/method:** `levels`; decodes 16-dimensional AE/VAE latent vectors into Lode Runner layouts, then applies patch crossover and latent mutation to evolve connected maps in which A* can collect all gold.
- **Evaluation:** augments 150 source levels to 300 training examples, samples 10,000 decoder candidates, and analyses 330 evolved levels. The VAE and AE have mean corpus similarity of 25.36% and 27.05% respectively; A* is a feasibility evaluator, not the research product.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2019.8848076), [official conference PDF](https://ieee-cog.org/2019/papers/paper_232.pdf), [author-associated repository](https://github.com/StarryBar/level-generation-for-lode-runner), [detailed artifact audit](pcg-96-99-primary-sources.md).
- **Open status:** **Partial, legacy/unlicensed.** Notebooks, A*, visualizations, and source data are public, but no license, dependency lock, checkpoints, seeds, results, or tests are present; the visible notebook uses ten iterations while the paper reports 150 generations.
- **Scope decision:** the system emits new Lode Runner maps and uses search only to evaluate/repair them; it is independent of the earlier Mario autoencoder proof of concept in source 93.
- **中文说明:** AE/VAE 先解码 Lode Runner 布局，再以进化和 A* 修复为连通、可收集全部黄金的关卡；作者关联仓库存在但无法精确复现实验。
- **English summary:** Latent autoencoder samples are evolved into connected, gold-collectible Lode Runner levels, with a useful but incomplete legacy code/data release.

### 97. Generating Game Levels for Multiple Distinct Games with a Common Latent Space

- **Year / venue:** 2020, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE), volume 16(1), pp. 109–115.
- **Scope and task/method:** `levels`; a branched DCGAN maps one 128-dimensional latent vector through shared layers and four game-specific branches to aligned 16×16 Boulderdash, Link, Zelda, and Roguelike levels.
- **Evaluation:** trains on 5,000 aligned four-game groups. On 50 outputs per game, solvability is 70%, 52%, 54%, and 40% respectively; path-distance distributions quantify cross-game correspondence and Levenshtein distances quantify within-game action novelty.
- **Primary sources:** [canonical AIIDE DOI](https://doi.org/10.1609/aiide.v16i1.7485), [official article](https://ojs.aaai.org/index.php/AIIDE/article/view/7485), [official PDF](https://ojs.aaai.org/index.php/AIIDE/article/download/7485/7346), [detailed artifact audit](pcg-96-99-primary-sources.md).
- **Open status:** **Closed.** No first-party implementation, aligned training set, model, checkpoints, generated corpus, or evaluation package was identified.
- **Scope decision:** automated GVGAI agents only check generated-level solvability. The separate DOI `10.1609/aiide.v15i1.7418` serves a byte-identical copy of the canonical 2020 PDF and is not counted again.
- **中文说明:** Branched GAN 从同一潜向量生成四款游戏中玩法对齐的完整关卡；重复 DOI 指向完全相同 PDF，只保留规范的 2020 记录。
- **English summary:** A shared latent trunk and four output branches generate corresponding playable layouts for four distinct grid games.

### 98. Learning to Generate Levels From Nothing

- **Year / venue:** arXiv precursor in 2020; IEEE Conference on Games, 2021.
- **Scope and task/method:** `levels`; a Generative Playing Network co-trains a Zelda level generator and player from no human levels, adapting generated difficulty toward the player's learning frontier; a semi-supervised condition uses five authored levels.
- **Evaluation:** trains for 50 million frames in a 12×16×14 representation and analyses displayed playable samples, convergence, and human simplicity. The target of approximately 50% player wins is a training objective, not a held-out generated-level success rate.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/COG52621.2021.9619131), [arXiv](https://arxiv.org/abs/2002.05259), [MIT-licensed author repository](https://github.com/pbontrager/GenerativePlayingNetworks), [detailed artifact audit](pcg-96-99-primary-sources.md).
- **Open status:** **Partial.** The generator, player, training loop, environment wrappers, and paper configuration are public, but no checkpoints, result bundle, tests, release tag, container, or complete dependency lock was verified.
- **Scope decision:** the player supplies the curriculum signal for generation; unlike PCGRL, the generator does not edit tiles as an RL policy, so this is a distinct self-supervised generation family.
- **中文说明:** GPN 在没有人工关卡的条件下协同学习 Zelda 玩家和生成器，玩家只为生成器提供学习前沿信号；公开代码完整度尚不足以复现论文结果。
- **English summary:** A co-evolving player supplies the learning signal for a Zelda generator trained from no authored levels, with a partial MIT-licensed implementation.

### 99. Mutation Models: Learning to Generate Levels by Imitating Evolution

- **Year / venue:** 2022, International Conference on the Foundations of Digital Games.
- **Scope and task/method:** `levels`; a CNN learns successful mutations from evolutionary trajectories and iteratively edits 50/50 random 14×14 binary maps into connected mazes without evaluating fitness at inference.
- **Evaluation:** the assisted two-epoch model reaches 99.67% success and 86.83% descriptor diversity over 100 outputs, averaging 18.21 edit sweeps and 0.6612 seconds versus evolution's 12.6957 seconds. Diversity is the fraction with a distinct `(longest path, empty tiles)` pair.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/3555858.3563267), [arXiv](https://arxiv.org/abs/2206.05497), [author repository](https://github.com/amidos2006/ImitatingEvolution), [detailed artifact audit](pcg-96-99-primary-sources.md).
- **Open status:** **Partial, unlicensed.** Author code covers evolutionary data construction, training, inference, games, and configurations, but omits a license, trained models, trajectory datasets, result bundle, tests, and an exact locked environment; visible configuration has drifted from the paper.
- **Scope decision:** evolution produces demonstrations during training and the learned mutation model produces new maze levels; no agent-control or maze-playing policy is trained.
- **中文说明:** 模型模仿进化中的成功 mutation，以约 20 倍速度把随机二值图修复为连通迷宫；代码公开但没有许可证、模型、轨迹数据或精确复现配置。
- **English summary:** A learned mutation operator imitates evolutionary repair to generate connected mazes much faster at inference, with an incomplete author code release.

### 100. Compositional Procedural Content Generation

- **Year / venue:** 2012, Third Workshop on Procedural Content Generation in Games.
- **Scope and task/method:** `generator`; a μ+λ evolution strategy searches 17 parameters of an Answer Set Programming file that is itself a reusable generator of complete, well-formed, winnable roguelike dungeons.
- **Evaluation:** averages the first 20 solver outputs per candidate. Reckless and smart A* evaluators approximate challenge and skill differentiation; the shown run uses μ=30, λ=30 and plateaus after roughly 40 generations.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/2538528.2538541), [metageneration audit](pcg-metageneration-primary-sources.md).
- **Open status:** **Closed.** No paper-specific ASP program, outer search, generated-dungeon corpus, seeds, or evaluation harness was verified.
- **Scope decision:** the A* agents evaluate generated dungeons. This is a separate roguelike/ASP system from source 101's interactive Mario generator generation, despite their shared metageneration framing.
- **中文说明:** 外层进化搜索 ASP 地牢生成器的参数，内层程序可反复生成受约束且可通关的 roguelike 地牢；A* 只负责评价生成内容。
- **English summary:** Evolution tunes an ASP program into a reusable constrained dungeon generator rather than directly encoding one dungeon.

### 101. A Procedural Procedural Level Generator Generator

- **Year / venue:** 2012, IEEE Conference on Computational Intelligence and Games.
- **Scope and task/method:** `generator`; interactive evolution synthesizes stochastic Mario level generators made of roughly 14–24 parameterized drawing agents, while a human selects parents through cloud, sample-level, playable, and simulation views.
- **Evaluation:** reports informal designer self-evaluation, qualitative within/between-generator diversity, ten-level A* playability estimates, an offline three-level/100-generation initializer, and speed tests over 100 random generators × 100 levels; it is not a controlled user study.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2012.6374174), [institutional record](https://www.um.edu.mt/library/oar/handle/123456789/29696), [institutional full text](https://www.um.edu.mt/library/oar/bitstream/123456789/29696/1/A_procedural_procedural_level_generator_generator.pdf), [author repository](https://github.com/ManuelKers/PPLGG), [metageneration audit](pcg-metageneration-primary-sources.md).
- **Open status:** **Partial, legacy/unlicensed.** Java source is public, but the README is empty and no license, tagged release, build guide, seed database, result corpus, or reproduction script was verified.
- **Scope decision:** the Mario A* agent estimates the playability of sampled levels; the research output is the reusable generator population, not a game-playing policy.
- **中文说明:** PPLGG 通过交互进化合成多个绘制智能体组成的 Mario 关卡生成器；公开 Java 源码是无许可证、无构建说明的历史快照。
- **English summary:** Users interactively evolve reusable agent-based Mario generators while A* only estimates the playability of their samples.

### 102. Marahel: A Language for Constructive Level Generation

- **Year / venue:** 2017, AIIDE Experimental AI in Games workshop.
- **Scope and task/method:** `generator language`; declares entities, regions, neighborhoods, and sequential explorers whose conditions/actions form compact stochastic generators for 2-D tile maps.
- **Evaluation:** implements five hand-authored generators and maps their expressive ranges along empty-space percentage, isolated elements, and cell-wise entropy.
- **Primary sources:** [AIIDE DOI](https://doi.org/10.1609/aiide.v13i2.12970), [official paper](https://ojs.aaai.org/index.php/AIIDE/article/download/12970/12818), [author implementation](https://github.com/amidos2006/marahel), [metageneration audit](pcg-metageneration-primary-sources.md).
- **Open status:** **Open implementation with a license caveat.** The language runtime, documentation, compiled browser library, and examples are public, but no software license was detected.
- **Scope decision:** humans author the 2017 scripts; source 104 later searches the language automatically. They are connected predecessors, not two publication versions of one method.
- **中文说明:** Marahel 让人用 explorer、neighborhood、条件和动作编写紧凑的构造式关卡生成器，为后续自动搜索生成器程序提供表示语言。
- **English summary:** Marahel is a public constructive-generator language and the explicit representation predecessor to later evolutionary metageneration.

### 103. Optimising Level Generators for General Video Game AI

- **Year / venue:** 2019, IEEE Conference on Games.
- **Scope and task/method:** `generator`; introduces parameterized GVGAI constructive generators and a genetic Meta Generator that searches their parameters for Butterflies, Freeway, and The Snowman.
- **Evaluation:** compares the Meta Generator with random and constructive baselines using composite generated-level fitness derived from AI playtesting; results are game-dependent and are reported as comparable or better, not uniformly dominant.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2019.8847961), [institutional record](https://cris.maastrichtuniversity.nl/en/publications/optimising-level-generators-for-general-video-game-ai/), [institutional full text](https://cris.maastrichtuniversity.nl/files/95969450/Winands_2019_Optimising_level_generators_for_general.pdf), [GPL GVGAI framework](https://github.com/GAIGResearch/GVGAI), [metageneration audit](pcg-metageneration-primary-sources.md).
- **Open status:** **Closed for the paper-specific method.** The upstream GVGAI framework is public, but no paper-identified Meta Generator, parameter sets, generated levels, logs, or evaluation data was verified.
- **Scope decision:** AI agents supply a generated-level fitness. The paper's focused Meta Generator is distinct from source 20's broad mixed framework and from playing-agent tracks.
- **中文说明:** Meta Generator 在三款 GVGAI 游戏上搜索构造式生成器参数；AI 试玩只构成生成关卡的复合适应度，论文特定实现未找到。
- **English summary:** Genetic search optimizes reusable GVGAI level generators from playtest-derived content fitness rather than optimizing a player.

### 104. Multi-Objective Level Generator Generation with Marahel

- **Year / venue:** 2020, Foundations of Digital Games PCG Workshop; arXiv v2 and the ACM record are one publication family.
- **Scope and task/method:** `generator`; NSGA-II and grammatical evolution map 102-integer chromosomes to compact Marahel programs that generate Binary, Zelda, and Sokoban maps.
- **Evaluation:** uses population 500 for 2,000 generations and averages each candidate over 50 maps, comparing final Pareto fronts with 500 random generators. Most component objectives improve, but the restricted language produces trade-offs and Zelda/Sokoban scripts often rely on favorable random initialization.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/3402942.3409606), [arXiv](https://arxiv.org/abs/2005.08368), [experiment repository](https://github.com/amidos2006/marahel-evolution), [Marahel framework](https://github.com/amidos2006/marahel), [metageneration audit](pcg-metageneration-primary-sources.md).
- **Open status:** **Open research snapshot with license and packaging caveats.** Central search/evaluation code and best scripts/chromosomes are public, but there is no detected license, README, dependency manifest, tagged release, or turnkey command.
- **Scope decision:** solvers and pathfinding score sampled maps. This is automatic generator-program synthesis, not a version of the human-authored Marahel language paper.
- **中文说明:** 多目标进化把整数染色体翻译成 Binary、Zelda 与 Sokoban 的 Marahel 生成器程序；核心实验快照公开但缺许可证和复现封装。
- **English summary:** Multiobjective evolution searches Marahel programs that are themselves reusable generators across three tile-map domains.

### 105. Evolutionary Wave Function Collapse

- **Year / venue:** 2026, accepted short paper at IEEE Conference on Games; arXiv posted 2026-07-02.
- **Scope and task/method:** `generator`; evolves a 4×4 tile example whose 2×2 patterns let WFC stochastically generate 8×8 connectivity mazes or 16×16 Zelda layouts.
- **Evaluation:** evolution and random search each receive 1,000 genotype evaluations (population 10 × 100 generations). Evolution improves mazes clearly and Zelda modestly; exact global entity/progression constraints remain difficult, and each genotype is evaluated from only one stochastic output.
- **Primary sources:** [arXiv record](https://arxiv.org/abs/2607.02082), [full text](https://arxiv.org/pdf/2607.02082), [metageneration audit](pcg-metageneration-primary-sources.md).
- **Open status:** **Closed.** No paper-specific evolutionary code, genotype set, generated corpus, run logs, or experiment data was verified.
- **Scope decision:** unlike source 31's generic WFC analysis, this paper explicitly evolves WFC examples as game-level generators and evaluates their output in two domains.
- **中文说明:** 进化搜索可充当 WFC 生成器的微型样例，在迷宫上提升明显、Zelda 全局约束上提升有限；尚无论文特定工件。
- **English summary:** Evolution searches tiny WFC examples as reusable game-level generators, with stronger results on local maze structure than global Zelda constraints.

### 106. A Comparative Evaluation of Procedural Level Generators in the Mario AI Framework

- **Year / venue:** 2014, Foundations of Digital Games.
- **Scope and task/method:** `levels` benchmark; ports seven Mario generator families and original Super Mario Bros. levels into a shared framework and contributes two pattern-based measures alongside four existing expressive-range metrics.
- **Evaluation:** compares output distributions, parameter effects, controllability, compression distance, and metric correlations, establishing a common quantitative baseline rather than ranking playing agents.
- **Primary sources:** [archived official FDG paper](https://web.archive.org/web/20180921071717id_/http%3A%2F%2Ffdg2014.org%2Fpapers%2Ffdg2014_paper_14.pdf), [archived author project page](https://web.archive.org/web/20220122165324id_/http%3A%2F%2Fsokath.com%2Ffdg2014_pcg_evaluation%2F).
- **Open status:** **Closed, archived landing page only.** The paper and landing page survive, but the linked `platform_level_metrics.zip` was not archived and no runnable code/level package was verified.
- **Scope decision:** the evaluated objects are level generators and their generated corpora; the paper explicitly positions the framework as a baseline for future generators and metrics.
- **中文说明:** 论文首次在统一 Mario 框架中量化比较七类生成器与原版关卡，并加入两项模式指标；历史代码/关卡压缩包已经不可用。
- **English summary:** A shared Mario framework compares seven generator families with six expressivity measures and provides a historical generator-evaluation baseline.

### 107. Towards a Procedural Evaluation Technique: Metrics for Level Design

- **Year / venue:** 2015, Foundations of Digital Games.
- **Scope and task/method:** `evaluation framework`; derives 20 theory-driven quantitative measures from Mario-like 2-D and Portal 2 3-D level-design activities, spanning aesthetics, topology, player tactics, and difficulty.
- **Evaluation:** organizes the measures into a common design vocabulary and proposes metric vectors as stylistic fingerprints. The paper explicitly leaves full computational implementation and broader genre validation to future work.
- **Primary sources:** [archived official FDG paper](https://web.archive.org/web/20170829055620id_/http%3A%2F%2Fwww.fdg2015.org%2Fpapers%2Ffdg2015_paper_16.pdf).
- **Open status:** **Paper-only by design.** The contribution is the metric vocabulary and derivation method, not a claimed software release.
- **Scope decision:** the framework is dedicated to automatic evaluation of generated levels and therefore meets the collection's benchmark/evaluator exception without being a generator itself.
- **中文说明:** 论文从二维和三维关卡设计实践整理 20 项量化指标，把设计语言转成未来可自动计算的生成内容评价框架。
- **English summary:** Twenty design-theory metrics turn level-design vocabulary into a structured evaluation framework, with implementation left for future work.

### 108. An Empirical Evaluation of Evaluation Metrics of Procedurally Generated Mario Levels

- **Year / venue:** 2015, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE).
- **Scope and task/method:** `evaluation study`; compares leniency, linearity, density, and compression distance with human judgments of levels from four Infinite Mario PCG systems.
- **Evaluation:** computes metrics over 148 levels and retains 37 participants after cleaning; each participant plays one practice level and one level from each generator in a balanced Latin-square design. Leniency correlates only weakly with perceived difficulty, and metric similarity misses a significant enjoyment difference.
- **Primary sources:** [AIIDE DOI and open proceedings record](https://doi.org/10.1609/aiide.v11i1.12785).
- **Open status:** **Closed.** No official 148-level set, participant data, metric implementation, analysis code, or reproduction package was verified.
- **Scope decision:** the work evaluates procedural generators and generated content; no learned player policy or playing-agent performance is proposed.
- **中文说明:** 研究以 37 名参与者和四个 Mario 生成器实证检验自动指标，发现 leniency 等不能可靠替代玩家评价。
- **English summary:** A four-generator player study shows that common automatic Mario metrics can support exploration but cannot replace human evaluation.

### 109. Understanding Mario: An Evaluation of Design Metrics for Platformers

- **Year / venue:** 2017, International Conference on the Foundations of Digital Games.
- **Scope and task/method:** `evaluation framework`; defines simple rule-, structure-, and completion-action-based platformer measures and applies them to authored Mario-series levels and Infinite Mario content.
- **Evaluation:** studies the measures' ability to distinguish games/content sources, their relationships with one another, and the design differences exposed across human and generated levels.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/3102071.3102080).
- **Open status:** **Closed.** No official normalized corpus, metric implementation, extracted-feature set, or analysis package was verified.
- **Scope decision:** although related to source 108's concern with metric validity, this paper contributes a different measure set and cross-game structural/action analysis, so it remains separate.
- **中文说明:** 论文以规则、结构和通关动作定义平台关设计指标，并在多个 Mario 游戏及生成内容上检验区分能力和指标关系。
- **English summary:** Structural, rule-based, and completion-action measures expose design differences across authored and generated Mario platform levels.

### 110. Expanding Expressive Range: Evaluation Methodologies for Procedural Content Generation

- **Year / venue:** 2018, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE).
- **Scope and task/method:** `evaluation framework`; extends two-axis expressive-range plots with high-dimensional corner plots, kernel density estimates, energy distance between distributions, plagiarism/self-similarity measures, and nearest/farthest representative samples.
- **Evaluation:** demonstrates these techniques on generator datasets, showing how distributional structure and copied/self-repeated content can be hidden by a single scatter plot.
- **Primary sources:** [AIIDE DOI and open proceedings record](https://doi.org/10.1609/aiide.v14i1.13012).
- **Open status:** **Closed at cutoff.** The paper's historical Dropbox dataset link returns 404, and no maintained code, dataset mirror, or complete analysis package was verified.
- **Scope decision:** this is a general methodology for judging PCG systems and their output distributions, not an evaluation of game-playing capability.
- **中文说明:** 论文把 expressive range 扩展到高维分布、energy distance、抄袭和自重复分析，弥补二维散点图隐藏结构的问题。
- **English summary:** High-dimensional distribution plots and distance/similarity analyses broaden expressive-range evaluation beyond two hand-picked axes.

### 111. The 2017 AIBIRDS Level Generation Competition

- **Year / venue:** competition held in 2017; article published online in 2018 and in IEEE Transactions on Games, 2019.
- **Scope and task/method:** `levels` competition; Science Birds generators receive input constraints and must emit stable, solvable physics levels within a time limit.
- **Evaluation:** five submissions pass automatic structure/validity checks. Eleven judging panels score Fun, Creativity, and balanced Difficulty; excessive similarity may be penalized, but diversity is not a fourth separately reported score. Agents/solvers only test generated levels.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TG.2018.2854896), [author manuscript](https://matthewstephenson.info/papers/The%202017%20AIBIRDS%20Level%20Generation%20Competition.pdf), [archived official results](https://web.archive.org/web/20210121085841id_/http://www.aibirds.org/level-generation-competition/2017-results.html), [winning IratusAves/MSG generator](https://github.com/stepmat/IratusAves), [Science Birds runtime](https://github.com/lucasnfe/science-birds).
- **Open status:** **Partial, GPL winning-generator release.** IratusAves/MSG publishes the winning generator, examples, Science Birds builds, and a GPL-3.0 license. The exact five submissions, task inputs, selected outputs, judge-level data, and removed agent-performance/stability-analysis features are not packaged together.
- **Scope decision:** this is explicitly a level-generation competition; it is independent of later ChatGPT4PCG Science Birds competitions and is not an Angry Birds-playing benchmark.
- **中文说明:** AIBIRDS 2017 要求五个参赛生成器在约束和时间内产生稳定、可解的物理关卡，再由 11 个评审小组从趣味、创造性和难度评价；GPL 获胜生成器已公开。
- **English summary:** A generation-only Science Birds competition combines automatic validity constraints with three judging categories, and its winning generator is publicly released under GPL-3.0.

### 112. Danesh: Interactive Tools for Understanding Procedural Content Generators

- **Year / venue:** 2016 IEEE CIG precursor *Towards the Automatic Optimisation of Procedural Content Generators*; expanded online in 2021 and in IEEE Transactions on Games, 2022.
- **Scope and task/method:** `generator-tuning`; a Unity/C# tool annotates an existing generator's parameters, metrics, generation, and visualization functions to analyse output, discover influential fields, explore expressive range, smooth interfaces, and search toward target metric values.
- **Evaluation:** a 53-developer survey finds 85% manually tune parameters and inspect output. Cave-generator experiments compare random search, hill climbing, and evolution in three parameter/metric scenarios; the system tunes a fixed generator rather than synthesizing new code.
- **Primary sources:** [journal DOI](https://doi.org/10.1109/TG.2021.3078323), [2016 IEEE DOI](https://doi.org/10.1109/CIG.2016.7860424), [institutional author manuscript](https://research.gold.ac.uk/id/eprint/18950/1/Cook_CIG2016.pdf), [author repository](https://github.com/gamesbyangelina/Danesh), [metageneration audit](pcg-metageneration-primary-sources.md).
- **Open status:** **Partial, legacy/unlicensed.** Central Unity source is public, but no license, maintained Unity release, dependency lock, result package, or turnkey reproduction path was verified.
- **Scope decision:** the 2016 optimizer and later interactive-analysis paper are one Danesh system family. It remains in the infrastructure/boundary section because it searches parameters of a fixed generator rather than generating a new representation.
- **中文说明:** Danesh 为固定 PCG 增加自动分析、可视化、参数发现和目标指标调优；历史 Unity 源码公开但无许可证或现代复现包。
- **English summary:** Danesh helps developers inspect and tune fixed procedural generators, making it generation infrastructure rather than a generator-generating core method.

### 113. Procedural Level Generation for Sokoban via Deep Learning: An Experimental Study

- **Year / venue:** journal DOI registered in 2022; IEEE Transactions on Games, 2023.
- **Scope and task/method:** `levels` benchmark study; reimplements bootstrapped conditional neural generators, controllable/uncontrollable PCGRL, and Generative Playing Networks on one Sokoban task.
- **Evaluation:** compares generation quality, diversity, controllability, and control confusion under a common experimental protocol, treating players/solvers only as generated-level evaluators or generator-training components.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TG.2022.3175795), [official TechRxiv preprint](https://doi.org/10.36227/techrxiv.16640095.v3).
- **Open status:** **Closed.** No official unified implementation, trained-model set, generated corpus, seed manifest, or evaluation package was verified; the availability of individual upstream methods is not a release of this comparison.
- **Scope decision:** this is a benchmark-like cross-method study of level generators rather than a paper about learning to solve Sokoban, so it stays within the generation-only boundary.
- **中文说明:** 论文把多类深度 Sokoban 生成器放进统一协议，比较质量、多样性、可控性和 control confusion；求解只服务于生成评价。
- **English summary:** A unified Sokoban study compares several deep level-generation families across output quality, diversity, and controllability rather than playing skill.

### 114. Corpus for Angry Birds Level Generation

- **Year / venue:** 2019, 2nd International Conference on Computing, Mathematics and Engineering Technologies (iCoMET), Sukkur, Pakistan, 30–31 January 2019, pp. 1–4; IEEE; DOI 10.1109/ICOMET.2019.8673443.
- **Authors:** Adeel Zafar, Shahbaz Hassan, and Qazi Shuja uddin.
- **Scope and task/method:** `levels` dataset; defines a tile-based machine-learning corpus reported as 200 Angry Birds levels: 100 from the original game and 100 from a baseline generator. The paper presents corpus construction and representation; using it to imitate level style for a future Angry Birds level-generation competition is proposed as next work.
- **Evaluation:** this is a corpus/representation paper, not a trained-generator experiment or fixed benchmark. It defines no fixed train/validation/test split, quantitative generator comparison, metric implementation, or reusable evaluator.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/ICOMET.2019.8673443), [IEEE record](https://ieeexplore.ieee.org/document/8673443/), [author dataset repository](https://github.com/AdeelZafar123/AngryBirdsDataSet), and [sole repository commit](https://github.com/AdeelZafar123/AngryBirdsDataSet/commit/3a88f3cf0d32b6bcc2d6dfb611da59a0bf1f9e84).
- **Artifact audit:** the repository's sole artifact is `Angry Bird Game Levels.zip` (2,811,915 bytes). It contains 103 `.txt` entries covering 100 unique numbered original-level IDs; 61, 62, and 75 each occur twice. Its folders and included summary table describe original-game levels 1–100, with additional filename/dimension packaging inconsistencies. No matrices corresponding to the paper's claimed 100 baseline-generated levels were found. The repository also has no README, detected license, schema guide, split manifest, code, release, tag, metric implementation, or evaluator.
- **Open status:** **Partial, public archive without a license.** A meaningful first-party corpus artifact is public, but the observable archive is incomplete relative to the paper's reported 200-level composition and is weakly packaged.
- **Scope decision:** this is generation-specific training data, like VGLC, rather than a playing-agent corpus, a benchmark with a fixed evaluation protocol, or another version of the 2017 AIBIRDS level-generation competition.
- **中文说明:** 论文声称语料含 100 个原版关卡和 100 个 baseline 生成关；作者仓库唯一 ZIP 实际可核验到 100 个原版关卡唯一编号（共 103 个文本条目，61、62、75 各重复一次），并存在文件名/尺寸封装不一致。未发现声称的 100 个生成关矩阵，也没有许可证、README/schema、划分、代码、指标实现或 evaluator。
- **English summary:** The paper reports a 200-level tile-encoded Angry Birds generation corpus, but the public author ZIP currently exposes only 100 unique original-level IDs—with duplicate entries and packaging inconsistencies—and lacks the claimed generated half and benchmark tooling.

### 115. Using Unconditional Diffusion Models in Level Generation for Super Mario Bros

- **Year / venue:** 2023, 18th International Conference on Machine Vision and Applications (MVA), Hamamatsu, Japan, 23–25 July 2023, pp. 1–5.
- **Scope and task/method:** `levels`; a DDPM-style unconditional UNet with Performer attention learns 5,925 unique 14×14, 11-channel windows extracted at stride one from 33 VGLC ground-level files (13 SMB and 20 SMB2(J)). It samples categorical Mario patches while comparing linear, quadratic, and sigmoid noise schedules and per-sprite temperature scaling. The repository's four underground files are outside the configured training path.
- **Training protocol:** the preprocessing yields 6,216 windows before global deduplication and 5,925 after it. The paper trains for 500 epochs; code defaults are batch size 64, AdamW at 3e-4, and 1,000 diffusion steps, with no train/validation/test split.
- **Evaluation:** visual quality is only a qualitative author judgment, without a blind user study or quantitative fidelity score. For edit distance/coverage/A* solvability, quadratic moderate scaling scores 41.89/0.33/0.70 and quadratic coarse scores 61.89/0.02/0.62, versus MarioGPT's 50.78/0.20/0.74. The paper omits sample count and coverage threshold; released code uses 100 samples, threshold 10, simulator `max_time=25`, and success only when `marioStatus==1`.
- **Primary sources:** [IEEE DOI](https://doi.org/10.23919/MVA57639.2023.10215856), [author manuscript](https://esslab.jp/publications/LeeMVA2023.pdf), and [first-author code repository](https://github.com/hyeonjoon-lee/UnconditionalDiffusionSMB).
- **Artifact audit:** preprocessing, training, sampling, evaluation, 33 ground and four underground raw level files, a Mario simulator, sprites, an example notebook, and nine epoch-500 output montages are public. Missing are the required processed `unique_onehot.npz`, every checkpoint, evaluated diffusion/MarioGPT sample array, tabulated result bundle, baseline configuration, random seeds, dependency manifest or version lock, test suite, tag, and release. Training, generation, and evaluation also expect incompatible checkpoint/output paths without manual intervention.
- **Open status:** **Partial, unlicensed author code.** The repository has no detected software license, and its useful central implementation does not provide a complete paper reproduction path.
- **Scope decision:** the model directly generates Mario layouts, while A* solely evaluates those outputs. MarioGPT is a comparison baseline, not a version alias; the author PDF and code are companion artifacts of the same MVA paper rather than additional records.
- **中文说明:** 无条件 DDPM 式 UNet 在 33 个地上关卡得到的 5,925 个去重 14×14 Mario 片段上训练；作者公开预处理、训练、采样和评价代码，但缺许可证、处理后训练数据、checkpoint、被评样本数组与结果包。
- **English summary:** An unconditional categorical diffusion model generates Mario level patches from 5,925 unique training windows and is evaluated for diversity and simulator solvability, with useful but incomplete unlicensed author code.

## Explicit exclusions / 明确排除

- **Game-playing only:** ALE, Procgen Benchmark, CoinRun, NetHack Learning Environment, MineRL/BASALT, Crafter, BabyAI, GVGAI playing tracks, and similar agent-control benchmarks do not generate game designs or levels.
- **METAGAME/METAGAMER:** random chess-like games are generated only as a domain for evaluating a general-game-playing system; the central method and results concern play, so the work is not counted as automated game design.
- **Playtesting agents:** MCTS/RL/search papers are not included merely because they evaluate a game. They appear above only when the policy/search process is directly optimizing generated content.
- **Asset or narrative generation alone:** texture, sprite, music, dialogue, story, and video generation are `components` unless the work also instantiates executable rules/mechanics. A visual world model that predicts the next frame is not automatically a generated game.
- **Mixed-initiative tools:** systems that only help a human edit content are outside this core list unless they include a substantive automatic generator and a primary evaluation of its outputs.
