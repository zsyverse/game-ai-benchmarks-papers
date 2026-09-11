# Historical complete-game and rule-generation coverage expansion

Verified 2026-09-05. This focused audit checks omissions from the 12 historical complete-game/rule/mechanic methods and 34 end-to-end records present when this pass began. It follows [SCOPE](../SCOPE.md) and the [strict audit](strict-method-benchmark-scope-audit.md). It does not expand the scope to game-playing, asset generation, authoring frameworks, or surveys.

The five additions below are integrated as PCG public records #13–17. Three have directly inspected method full text; two older Springer papers have primary publisher abstracts that explicitly establish generation and evaluation, with the limits of that evidence stated. No numerical results are inferred for those two. None is a duplicate of the existing Ludi, ANGELINA 2011, Mechanic Miner 2013, or GVGAI rule-generation record.

## Recommended English rows

| Year | Paper | Output | Generation method/task | Evaluation | Artifacts/status |
| --- | --- | --- | --- | --- | --- |
| 2012 | [Initial Results from Co-operative Co-evolution for Automated Platformer Design](https://doi.org/10.1007/978-3-642-29178-4_20) | `full-game` | ACCME uses cooperative co-evolution to automatically evolve simple platform games. | Tests fitness maximization and the relationship between fitness and player preference for generated games. | **Closed** — no official generator or experiment package verified; the publisher abstract establishes method and evaluation, but this pass could not recover the historical full text. |
| 2015 | [Towards Generating Arcade Game Rules with VGDL](https://doi.org/10.1109/CIG.2015.7317941) ([author manuscript](https://www.kmjn.org/publications/GeneratingVGDL_CIG15.pdf)) | `full-game` | Evolution strategies generate VGDL games from random rules/levels or existing-game seeds, guided by relative controller performance. | Evaluates 54 evolved games, including nine from random starts; generated examples reveal interesting interactions but frequently trivial or luck-dependent gameplay. | **Closed** — the author manuscript is public; no paper-specific official generator/output package was verified. |
| 2016 | [Evolving Chess-like Games Using Relative Algorithm Performance Profiles](https://doi.org/10.1007/978-3-319-31204-0_37) | `rules` | Evolves complete executable chess-like rule sets in Simplified Boardgames, matching relative agent-performance profiles to model games. | Reports playable, balanced generated games; the authors' later full-text paper confirms the generator and describes its rule representation and evaluation. | **Closed** — no official generator or evaluated-game package verified; numerical experiment details were not recovered in this pass. |
| 2021 | [Adversarial Random Forest Classifier for Automated Game Design](https://arxiv.org/abs/2107.12501) ([DOI](https://doi.org/10.1145/3472538.3472587)) | `full-game` | Learns a human-likeness fitness function with a random forest and iteratively hill-climbs joint VGDL rules and levels. | Eight human games; two representations over five iterations; MCTS/random-agent completion, scores, move counts, and qualitative outputs expose weak quality and evaluation confounds. | **Partial, legacy setup** — [generator, evaluated games, agents, and logs](https://github.com/HonestPretzels/RF_Adversarial_PCG) are public, but setup is incomplete and README names a missing training entrypoint. |
| 2023 | [A Controllable Co-Creative Agent for Game System Design](https://arxiv.org/abs/2308.02317) | `rules` | Evolves executable abstract game systems by adding and modifying state-machine-like components and resource flows under weighted design metrics; humans still build the rest of the actual game. | Expressive-range analysis of 100,000 random designs, approximately 33,000 accepted for simulated play; targeted controllability tests on 25 systems have mixed significance across metrics. | **Closed** — no paper-specific generator or evaluation release verified; the general CreativeWand framework is not this game's generator. |

## Recommended Chinese rows

| 年份 | 论文 | 产物 | 生成方法/任务 | 评测 | 工件/状态 |
| --- | --- | --- | --- | --- | --- |
| 2012 | [Initial Results from Co-operative Co-evolution for Automated Platformer Design](https://doi.org/10.1007/978-3-642-29178-4_20) | `full-game` | ACCME 通过合作协同进化自动生成简单平台游戏。 | 检验适应度优化效果，以及生成游戏的适应度与玩家偏好的关系。 | **Closed** — 未核验到官方生成器或实验包；出版社摘要明确描述方法与评测，但本轮未找回历史全文。 |
| 2015 | [Towards Generating Arcade Game Rules with VGDL](https://doi.org/10.1109/CIG.2015.7317941)（[作者全文](https://www.kmjn.org/publications/GeneratingVGDL_CIG15.pdf)） | `full-game` | 以随机规则/关卡或既有游戏为种子，通过控制器相对表现引导演化策略，生成 VGDL 游戏。 | 评测 54 个演化游戏，其中 9 个从随机起点生成；实例包含有趣交互，但不少玩法过于简单或依赖运气。 | **Closed** — 作者全文公开；未核验到论文专属官方生成器或输出包。 |
| 2016 | [Evolving Chess-like Games Using Relative Algorithm Performance Profiles](https://doi.org/10.1007/978-3-319-31204-0_37) | `rules` | 在 Simplified Boardgames 表示中演化完整可执行棋类规则，使不同强度智能体的相对表现接近目标游戏。 | 报告可玩、平衡的生成游戏；作者后续论文全文进一步确认生成器、规则表示与评测方法。 | **Closed** — 未核验到官方生成器或受测游戏包；本轮未取得原实验数值细节。 |
| 2021 | [Adversarial Random Forest Classifier for Automated Game Design](https://arxiv.org/abs/2107.12501)（[DOI](https://doi.org/10.1145/3472538.3472587)） | `full-game` | 用随机森林学习类人设计适应度，迭代爬山搜索，联合生成 VGDL 规则与关卡。 | 8 个人工游戏、两种表示各 5 轮；以 MCTS/随机智能体的完成率、分数、步数和实例分析揭示质量不足及评测混淆。 | **Partial，历史环境** — [生成器、受测游戏、智能体和日志](https://github.com/HonestPretzels/RF_Adversarial_PCG)公开，但安装不完整，README 引用的训练入口文件缺失。 |
| 2023 | [A Controllable Co-Creative Agent for Game System Design](https://arxiv.org/abs/2308.02317) | `rules` | 通过增添、修改类状态机组件和资源流，在加权设计指标下演化可执行游戏系统。 | 10 万个随机设计中约 3.3 万个可玩；以 25 个游戏测试定向可控性，不同指标的显著性结果不一致。 | **Closed** — 未核验到论文专属生成器或评测发布；通用 CreativeWand 框架不能算作本方法工件。 |

## Dossiers and exact evidence

### ACCME, 2012

- **Primary source:** [publisher chapter and abstract](https://link.springer.com/chapter/10.1007/978-3-642-29178-4_20), Michael Cook, Simon Colton, Jeremy Gow, EvoApplications 2012.
- **Scope evidence:** the abstract explicitly says the system “uses co-operative co-evolution to automatically evolve simple platform games” and that experiments address fitness maximization and correlation with player preference. This is a demonstrated generator, not merely a design-architecture proposal.
- **Distinctness:** its platform-game system and evaluated player preferences are different from the 2011 simple arcade-game paper. The publisher references that 2011 paper as prior work.
- **Independent audit update:** the [original Springer preview PDF](https://page-one.springer.com/pdf/preview/10.1007/978-3-642-29178-4_20) was recovered and inspected: printed pages 194–195 only. The abstract and introduction confirm the platform-game generator and planned experiment coverage; methods/experiments remain unavailable. Page 195's ANGELINA subsection describes the 2011 predecessor, not ACCME's precise implementation.
- **Evidence limit:** historical author PDF `https://www.doc.ic.ac.uk/~sgc/papers/cook_evogames12.pdf` is now 404; Goldsmiths archive requests timed out. No participant count, result coefficient, or exact ACCME representation claim is recommended without recovering the remaining manuscript.
- **Availability:** Closed under this repository's verified-artifact usage. The publisher record alone is not a released generator.

### VGDL evolution, 2015

- **Primary sources:** [author landing page](https://www.kmjn.org/publications/GeneratingVGDL_CIG15-abstract.html), [author PDF](https://www.kmjn.org/publications/GeneratingVGDL_CIG15.pdf), [DOI](https://doi.org/10.1109/CIG.2015.7317941).
- **Input → output:** randomly generated VGDL descriptions and levels, or human-designed seeds → executable evolved game descriptions, with generated starting levels for the random branch. Not limited to tuning an existing game.
- **Method:** evolution strategy with mutation/crossover; interaction-rule mutation; DeepSearch and DoNothing give relative score/win-rate fitness, penalizing trivially fast wins and always-winning designs.
- **Exact experiment:** section V.C reports 54 evolved games: 45 from human-designed seeds and nine from randomly generated starts; 40 seeded and six random-start games scored above 0.98. High fitness is **not** evidence of good human experience. Section VI explains luck, triviality, missing challenge, and the lack of a human experiment. Figures 6–7 give random-start rule code and running game screenshots.
- **Importance:** fills the predecessor step between early evolutionary systems and the later GVGAI rule-generation competition. It is distinct from the later three-generator paper, so must not be merged merely for using VGDL.
- **Availability:** author PDF responds as `application/pdf`; author page links the PDF/DOI, but no method-specific repository. No official code claim should be inferred from the general GVGAI repository.

### Chess rule evolution, 2016

- **Primary source:** [publisher abstract/chapter](https://link.springer.com/chapter/10.1007/978-3-319-31204-0_37), Jakub Kowalski and Marek Szykuła, published 2016-03-15.
- **Direct primary evidence:** abstract explicitly describes automatic generation of complete rules, formalizes relative algorithm performance profiles, applies the method to evolving chess-like boardgames, and reports playable balanced outcomes.
- **Additional author-owned full text:** [Kowalski, Liapis, Żarczyński 2018 manuscript](https://antoniosliapis.com/papers/mapping_chess_aesthetics_onto_procedurally_generated_chess-like_games.pdf), sections 1–2.1. It identifies the 2016 source as its rule generator and describes fully symmetrical games with a royal piece and a pawn-like row, evaluated by multiple algorithms of differing strength against profiles of human-made games.
- **Executable representation:** the same full text's section 2.2 documents Simplified Boardgames, rectangular boards, and regular-language piece moves with finite-automaton legal-move computation. This is actual executable gameplay, not prose rulebooks.
- **Evidence limit:** the original publisher full-text PDF endpoint returned a subscription HTML page; no numerical run count or human-test statistic was verified. The later paper is used as coauthor confirmation, not as the canonical generation paper.
- **Availability:** no official implementation or generated corpus verified; Closed. The author web hosts could not be accessed reliably and should not be presented as working releases.

### Adversarial random-forest generation, 2021

- **Primary sources:** [full text](https://arxiv.org/html/2107.12501), [paper-linked repository](https://github.com/HonestPretzels/RF_Adversarial_PCG), [setup instructions](https://github.com/HonestPretzels/RF_Adversarial_PCG/blob/master/level-generation/README.md).
- **Scope:** section 3 generates both description and level files: avatar/sprites, interactions, terminations, parameters, and tile map. A short random-agent playthrough rejects immediate crashes. Greedy search changes rules and level geometry; the RF is repeatedly retrained to distinguish eight human games from eight outputs. Therefore this is a generator with a learned evaluator, not evaluator-only work.
- **Experiment:** sections 4–5 compare representations with/without termination information over five rounds each. Table 1 reports completion, mean/max score, and move count against a random agent. MCTS and random have identical completed-game counts on every generated batch. Apparent move-count advantages are confounded by a five-minute wall-clock limit, and no human-quality conclusion is supported.
- **Artifacts inspected using GitHub tree API:** `gameGen.py`, `classifierGenerate.py`, `classification.py`, `gameComprehension.py`, `gameCheck.py`, `mcts.py`, `randomAgent.py`, `experiment.ps1`, training human games, `games/output/Experiment1` and `Experiment2` with five batches each, per-game logs, and `output.csv`.
- **Reproducibility limit:** no dependency/environment manifest or license file in the checked tree. README calls `train.py`, which is absent; actual available entrypoints differ. Public source and evaluated outputs are substantial, but this warrants Partial with legacy-setup caveat rather than a turnkey claim. No code execution was attempted.

### Controllable game-system generation, 2023

- **Primary source:** [arXiv full text](https://arxiv.org/html/2308.02317).
- **Evidence:** independently reviewed by the parent researcher and supplied for this consolidated note: the Genetic Game Generator adds state/resource-flow components and evaluates simulated playable systems. Generation goes beyond fixed-parameter balancing.
- **Experiment:** approximately 33,000 abstract systems accepted for simulated play among 100,000 random designs; controllability over 25 designs with metric weights at ±100. These are not human-tested games or the optimized generator's standalone success rate. Some metrics fail to show the intended significant changes. Preserve the mixed result.
- **Independent scope clarification:** the original Modeling Games Generically subsection says a human must still build levels, stories and the rest of a complete playable game. The implemented Game Evaluator nevertheless executes states, actions, transitions and resource constraints, and the Genetic Game Generator adds components. Retain narrowly as executable abstract rules/systems, not complete games; see [independent audit](independent-classic-audit-2026-09-05.md).
- **Availability audit from parent researcher:** CreativeWand's release2.0 tree contains a generic framework/text example, not this paper's game generator. Closed, with no borrowed openness claim from a related framework.

## Exclusions, duplicates, and unresolved leads

| Candidate | Decision and evidence |
| --- | --- |
| [Mapping Chess Aesthetics onto Procedurally Generated Chess-like Games, 2018](https://antoniosliapis.com/papers/mapping_chess_aesthetics_onto_procedurally_generated_chess-like_games.pdf) | Exclude. Read primary manuscript. Its new output is chess-piece shape/appearance; it consumes rules generated by previous papers. Section 1 explicitly says experiments evolve pieces for two previously generated games. |
| [Recombinable Game Mechanics for Automated Design Support, 2008](https://www.kmjn.org/publications/Mechanics_AIIDE08-abstract.html) | Do not add from this evidence. Author abstract proposes event-calculus architecture and manual modification/critique of an example game; no substantive automatic generator established. |
| [Automated Game Design Learning, 2017](https://arxiv.org/abs/1707.03333) | Exclude. Research-field/agenda paper; the abstract explicitly proposes the field and surveys existing projects. |
| [Software Engineering For Automated Game Design, 2020](https://arxiv.org/html/2004.01770) | Exclude from this expansion. Software-engineering impact/position framing, not sufficiently established as a new generation method. |
| [A Vision For Continuous Automated Game Design, 2017](https://arxiv.org/html/1707.09661) | Do not add as a full-game method based on current evidence. Primary text repeatedly frames a roadmap; first module and game example require separate scope adjudication rather than counting the whole proposed architecture as implemented. |
| [Aesthetic Considerations for Automated Platformer Design, 2012](https://doi.org/10.1609/aiide.v8i1.12524) | Hold. Publisher metadata describes ANGELINA3 theme/multimedia selection. Without full text, cannot distinguish substantive gameplay generation from asset orchestration of the prior platformer system; avoid duplication/asset-only inflation. |
| [Knowledge-Driven Game Design by Non-Programmers, 2014](https://arxiv.org/abs/1404.4713) | Hold/exclude under present evidence. Abstract centers infrastructure and board-game extension, not a verified new automated generator. |
| [ChatGPT and Other LLMs as Evolutionary Engines for Online Interactive Collaborative Game Design, 2023](https://arxiv.org/abs/2303.02155) | Hold. Abstract establishes evolved design ideas; no executable output verified in this pass. |
| [Latent Combinational Game Design, 2022](https://arxiv.org/abs/2206.14203) | Existing PCG line of work; not added to historical rules section merely because title says game design. |
| Ludi, Variations Forever, Mechanic Miner, Game-O-Matic, General Video Game Rule Generation | Already canonical in the repository; no additional count for a new URL, later upload date, or method name. |
| [Inductive General Game Playing, 2019](https://arxiv.org/abs/1906.09627) | Unresolved, not added. Its task is rule induction from traces, but the abstract alone does not prove reconstructed complete games rather than predicate-learning tasks. |

The strict audit's exclusions for A Rogue Dream, GameGPT, DreamGarden, and pure Ludii infrastructure remain in force. This pass found no reason to reverse them.
