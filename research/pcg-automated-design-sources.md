# Automated game design and PCG: verified primary sources

> Research cutoff / 检索截止: **2026-09-04 (Asia/Shanghai)**.
>
> Targeted follow-up / 定向续查：**2026-09-08**, current #18 and #117–120; not a full-corpus re-audit / 非全库重新审计。

This dossier contains exactly the **120 canonical records** in the public PCG index: 18 complete-game/rule/mechanic methods and 102 playable-content methods or formal generation benchmarks. The 29 additions (#13–17 and #93–116) were verified on **2026-09-05**; the earlier full-index cutoff remains unchanged. Original full texts for the 2012 ACCME and 2016 chess-rule papers were not recovered; those records explicitly distinguish publisher-abstract and later coauthor evidence from direct full-text inspection.

本底稿与公开 PCG 索引严格一一对应，共 **120 条 canonical 记录**：18 条完整游戏/规则/机制方法，以及 102 条可玩内容方法或正式生成 benchmark。本轮新增 29 条（#13–17、#93–116）于 **2026-09-05** 核验，不代表全库重新审计。2012 年 ACCME 和 2016 年棋类规则论文的原始全文未找回；相应底稿明确区分出版社摘要、作者后续论文佐证与原始全文核验。

Every numbered dossier record corresponds to the same public ID. Only direct generation methods and formal generation benchmarks appear here; rejected and unresolved candidates are documented in the strict audit and coverage notes.

每条底稿记录与同编号公开条目对应。这里只保留直接生成方法与正式生成 benchmark；被拒与未决候选记录在严格审计和覆盖增补笔记中。

## Complete-game, rule, and mechanic generation / 完整游戏、规则与机制生成

### 1. EGGG: Automated Programming for Game Generation

- **Year / venue:** 2000, IBM Systems Journal.
- **Scope and task/method:** `full-game`; EGGG accepts an abstract game/rule specification, selects compatible reusable implementation components, and composes them into an executable game program.
- **Evaluation:** the paper presents the programming architecture and generated examples, but does not define a standardized quantitative benchmark or comparative user study.
- **Primary sources:** [IBM DOI](https://doi.org/10.1147/sj.393.0782).
- **Open status:** **Closed.** No official source, executable, component library, example corpus, or reproducibility package was verified at the cutoff.
- **Scope decision:** the system's product is an implemented game, not a policy that plays a fixed game.
- **中文说明:** EGGG 从抽象游戏与规则规格选择、组合可复用实现组件，编译出能运行的游戏程序，是早于现代 LLM 的端到端自动游戏编程工作。
- **English summary:** EGGG composes reusable software components from an abstract game specification to produce a functioning game program.

### 2. Automatic Design of Balanced Board Games

- **Year / venue:** 2007, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE).
- **Scope and task/method:** `rules`; a genetic algorithm recombines boards, pieces, victory conditions, and rule mutations into executable Zillions of Games rule files.
- **Evaluation:** each candidate receives 100 self-play games; 500 genetic-algorithm iterations are compared with 500 random samples using balance, draw behavior, and diversity measures.
- **Primary sources:** [AIIDE DOI and proceedings record](https://doi.org/10.1609/aiide.v3i1.18777).
- **Open status:** **Closed.** The experiment depends on the commercial Zillions of Games runtime, and no paper-specific generator, rules corpus, or experiment package was verified.
- **Scope decision:** self-play is used only to evaluate newly generated rule sets; return or playing strength is not the research product.
- **中文说明:** 这项工作直接进化可执行棋类规则文件，并用每个候选 100 局自博弈评价平衡性；自博弈是设计评分器，不是论文目标。
- **English summary:** A genetic algorithm generates executable board-game rules and uses automated matches only to filter for balanced, non-trivial designs.

### 3. Towards Automated Game Design

- **Year / venue:** 2007, AI*IA 2007: Artificial Intelligence and Human-Oriented Computing.
- **Scope and task/method:** `full-game`; uses WordNet and ConceptNet to map requested nouns and verbs through abstract mechanics into concrete J2ME mechanics, controls, graphics, and runnable WarioWare-style micro-games.
- **Evaluation:** demonstrates generated games running on the prototype platform and analyzes the design pipeline; a systematic user study or common benchmark is left to future work.
- **Primary sources:** [Springer DOI and chapter record](https://doi.org/10.1007/978-3-540-74782-6_54).
- **Open status:** **Closed.** No official generator, J2ME mechanic library, output corpus, or evaluation package was verified.
- **Scope decision:** this is a distinct system and authorship lineage from the 2008 evolutionary study *An Experiment in Automatic Game Design*; the two are not collapsed into one version family.
- **中文说明:** 系统把自然语言概念映射为机制、控制与图形，生成可运行的 J2ME 微游戏；它与 2008 年进化式自动游戏设计论文不是同一系统或扩展版。
- **English summary:** Semantic knowledge bases drive the assembly of runnable J2ME micro-games, independently of the better-known 2008 evolutionary automatic-design experiment.

### 4. An Experiment in Automatic Game Design

- **Year / venue:** 2008, IEEE CIG.
- **Scope:** `full-game`
- **Generated content:** small two-player games, including rules and board configurations.
- **Method:** evolutionary search over a game-description space, with learning agents used only as automatic design evaluators.
- **Evaluation:** fitness rewards games that are learnable yet non-trivial and distinguishes player skill; the paper inspects evolved playable games.
- **中文说明:** 这是用“会学习的代理之间是否能拉开水平”来评价并进化完整小游戏的早期代表作。
- **English summary:** A foundational experiment evolves complete games and scores them through differences between learning players.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2008.5035629)
- **Open status:** **Closed.** The publication is accessible, but no official historical implementation/data release was located.

### 5. Automatic Generation and Evaluation of Recombination Games

- **Year / venue:** 2008, Queensland University of Technology PhD thesis; extended in IEEE Transactions on Computational Intelligence and AI in Games, 2010.
- **Scope:** `rules`
- **Generated content:** rule sets for abstract combinatorial board games expressed as ludemes.
- **Method:** Ludi evolves recombinations of rule building blocks and uses automated self-play measurements to score candidates.
- **Evaluation:** playability and heuristic qualities such as balance, depth, and decisiveness; the process produced human-playable games including Yavalath.
- **中文说明:** Ludi 把棋类规则拆成可重组的 ludeme，再通过自博弈筛掉无效或失衡的规则组合。
- **English summary:** Ludi evolves recombinations of rule primitives and filters them with automated play-based quality estimates.
- **Primary sources:** [official QUT repository record](https://eprints.qut.edu.au/17025/), [thesis PDF](https://eprints.qut.edu.au/17025/1/Cameron_Browne_Thesis.pdf), [journal extension](https://doi.org/10.1109/TCIAIG.2010.2041928), [Ludii successor platform](https://ludii.games/)
- **Open status:** **Partial.** The thesis, journal record, and successor Ludii ecosystem are public, but the original Ludi experiment is not packaged as a current reproducible benchmark.

### 6. Variations Forever: Flexibly Generating Rulesets from a Sculptable Design Space of Mini-Games

- **Year / venue:** 2010, IEEE Conference on Computational Intelligence and Games; expanded as an answer-set-programming method paper in IEEE Transactions on Computational Intelligence and AI in Games, 2011.
- **Scope and task/method:** `rules`; answer-set programming declaratively specifies and constrains a code-like mini-game design space, while LPARSE/SMODELS enumerate rulesets that a Flixel-based engine instantiates as playable games. The 2011 paper generalizes the design-space method and also reconstructs a maze generator.
- **Evaluation:** qualitative prototype analysis focuses on design-space flexibility, expressivity, constraint sculpting, and a novel indirect-push solution; the method paper adds worked encodings rather than a generator leaderboard. Automatic game-quality optimization remains future work.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/ITW.2010.5593343), [author manuscript](https://users.soe.ucsc.edu/~amsmith/papers/ieeecig20_vf.pdf), [ASP method extension](https://doi.org/10.1109/TCIAIG.2011.2158545), [extension author manuscript](https://users.soe.ucsc.edu/~amsmith/papers/tciaig-asp4pcg.pdf).
- **Open status:** **Closed.** The paper's public demo returned 404 at the 2026-08-31 cutoff, and no official generator, engine source, design-space package, or evaluation corpus was verified.
- **Scope decision:** the output is a large space of executable game rulesets and playable mini-games; the player explores generated games but no playing policy, return, or win-rate benchmark is proposed.
- **中文说明:** Variations Forever 用 ASP 表达并裁剪小游戏规则空间，再把采样规则实例化为可玩游戏；这是规则生成，不是玩游戏 agent。
- **English summary:** A declarative ASP generator samples executable mini-game rulesets from a sculptable design space, with qualitative rather than policy-based evaluation.

### 7. Multi-faceted Evolution of Simple Arcade Games

- **Year / venue:** 2011, IEEE CIG.
- **Scope:** `full-game`
- **Generated content:** playable arcade games with mechanics, rules, and level layouts.
- **Method:** ANGELINA co-evolves several facets of a game rather than optimizing one fixed content type; automated play helps judge candidates.
- **Evaluation:** generated games are checked for functional play and examined as design artifacts; this is a system demonstration, not a fixed leaderboard.
- **中文说明:** ANGELINA 同时搜索机制与关卡等多个设计面，是“自动做游戏”而非单独画地图的经典系统。
- **English summary:** ANGELINA jointly evolves multiple facets of simple arcade games and evaluates them through automated play.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2011.6032019)
- **Open status:** **Closed.** No complete official release of this historical ANGELINA version was located.

### 8. Game-O-Matic: Generating Videogames That Represent Ideas

- **Year / venue:** 2012, Third Workshop on Procedural Content Generation in Games.
- **Scope:** `full-game`
- **Generated content:** small playable arcade games intended to express relationships between real-world concepts.
- **Method:** Game-o-Matic maps a user-authored concept/relation graph to game-mechanic patterns, entities, rules, and presentation choices.
- **Evaluation:** generated examples assess whether the resulting interaction communicates the intended idea; there is no common automatic score.
- **中文说明:** Game-o-Matic 从概念关系图直接装配可玩的表达性小游戏，目标是让机制本身“表达观点”。
- **English summary:** Game-o-Matic turns conceptual relationship graphs into small playable, rhetorically expressive games.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/2538528.2538537)
- **Open status:** **Closed.** No official maintained end-to-end generator, source, or evaluator was verified.

### 9. Mechanic Miner: Reflection-Driven Game Mechanic Discovery and Level Design

- **Year / venue:** 2013, EvoApplications.
- **Scope:** `rules`
- **Generated content:** new mechanics and levels designed to expose the consequences of those mechanics.
- **Method:** ANGELINA reflects on simulated play traces, searches for mechanically interesting rule changes, and constructs supporting levels.
- **Evaluation:** automated play distinguishes behaviours induced by candidate mechanics; the paper analyses generated mechanic/level examples.
- **中文说明:** Mechanic Miner 不只变异规则，还会反思玩法差异并生成能展示新机制的关卡。
- **English summary:** The system discovers mechanics through play-trace reflection and builds levels that make their effects visible.
- **Primary sources:** [Springer DOI](https://doi.org/10.1007/978-3-642-37192-9_29)
- **Open status:** **Closed.** No official runnable release was located.

### 10. Automatic Game Design via Mechanic Generation

- **Year / venue:** 2014, AAAI.
- **Scope:** `rules`
- **Generated content:** game mechanics/rules satisfying designer-provided requirements.
- **Method:** formal mechanic representations and search are combined with simulated execution to construct and test candidate designs.
- **Evaluation:** case-study games test whether generated mechanics realize target gameplay requirements and remain executable.
- **中文说明:** 该工作把机制写成可推理的形式模型，再搜索满足设计约束的规则，而不是让代理去玩固定游戏。
- **English summary:** Formalized mechanics are searched and simulated to synthesize rule sets that meet design requirements.
- **Primary sources:** [AAAI proceedings](https://doi.org/10.1609/aaai.v28i1.8788)
- **Open status:** **Closed.** The evaluation is documented, but no official complete code/data package was located.

### 11. Automated Game Design via Conceptual Expansion

- **Year / venue:** *Automated Game Design via Conceptual Expansion*, AIIDE 2018; journal expansion *Conceptual Game Expansion*, registered/online in 2021 and formally published in IEEE Transactions on Games 14(1), 2022.
- **Scope:** `full-game`
- **Generated content:** novel games made by recombining learned representations of existing games.
- **Method:** conceptual expansion blends learned game graphs/components instead of relying on a hand-authored rule grammar.
- **Evaluation:** the system is asked to reconstruct held-out existing games, providing a measurable proxy before presenting novel recombinations.
- **中文说明:** Conceptual Expansion 从已有游戏中学习结构，再“概念混合”出新游戏，并先用复原已知游戏验证方法。
- **English summary:** Learned game representations are recombined through conceptual expansion and evaluated by reconstructing known games.
- **Primary sources:** [AIIDE paper](https://doi.org/10.1609/aiide.v14i1.13022), [arXiv](https://arxiv.org/abs/1809.02232), [journal article](https://doi.org/10.1109/TG.2021.3060005)
- **Open status:** **Closed.** No official end-to-end artifact package was located.

### 12. Puck: A Slow and Personal Automated Game Designer

- **Year / venue:** 2022, AIIDE.
- **Scope:** `full-game`
- **Generated content:** a personal, continuously evolving collection of small playable game designs.
- **Method:** Puck explores designs over long periods and incorporates a designer's ongoing interaction and preferences rather than optimizing a one-shot benchmark score.
- **Evaluation:** reflective longitudinal case study of generated games and the human–system relationship.
- **中文说明:** Puck 强调长期、个性化的自动设计过程，用持续积累的设计作品替代一次性生成排行榜。
- **English summary:** Puck slowly explores a personalized space of complete game designs in a longitudinal human–AI process.
- **Primary sources:** [AIIDE proceedings](https://doi.org/10.1609/aiide.v18i1.21968)
- **Open status:** **Closed.** The paper documents the system and artifacts, but no complete official reproducibility package was located.

### 13. Initial Results from Co-operative Co-evolution for Automated Platformer Design

- **Year / venue:** 2012, EvoApplications; Michael Cook, Simon Colton, Jeremy Gow.
- **Scope:** `full-game`
- **Generated content:** complete simple platform games produced by ACCME, a cooperative co-evolutionary Metroidvania engine.
- **Method:** cooperative co-evolution automatically evolves platform games; this is a distinct platform-game follow-up to the earlier arcade-game system.
- **Evaluation:** the publisher abstract explicitly reports investigation of fitness maximization and whether fitness correlates with player preference for generated games.
- **Evidence level:** publisher abstract plus original two-page preview (pp194–195), not full method/experiment text. The preview's description of ANGELINA2011 is prior work, not direct evidence about ACCME. No participant count, coefficient, or undocumented representation detail is inferred.
- **Primary sources:** [publisher chapter and abstract](https://doi.org/10.1007/978-3-642-29178-4_20); [original preview](https://page-one.springer.com/pdf/preview/10.1007/978-3-642-29178-4_20); [detailed verification note](classic-game-coverage-expansion-2026-09-05.md#accme-2012).
- **Open status:** **Closed** — no official generator or experiment package verified; the publisher abstract and original two-page preview were inspected, but the method/experiment sections remain unavailable.
- **中文说明:** ACCME 用合作协同进化生成平台游戏，并检验适应度优化及其与玩家偏好的关系；已核查出版社摘要和原始两页预览，方法/实验章节仍未取得。
- **English summary:** ACCME evolves platform games through cooperative co-evolution and evaluates fitness optimization and player preference.

- **Independent audit:** [primary-source section evidence and limitations](independent-pcg-audit-2026-09-05.md), checked 2026-09-05.

### 14. Towards Generating Arcade Game Rules with VGDL

- **Year / venue:** 2015, IEEE CIG; Thorbjørn S. Nielsen, Gabriella A. B. Barros, Julian Togelius, Mark J. Nelson.
- **Scope:** `full-game`
- **Generated content:** executable VGDL games, including games evolved from randomly generated rules and levels rather than only existing-game modifications.
- **Method:** evolution strategies mutate and recombine interaction rules, guided by relative controller scores/win rates and penalties for trivial wins and always-winning designs.
- **Evaluation:** section V.C reports 54 evolved games: 45 from human-designed seeds and nine from random starts; 40 seeded and six random-start games exceed 0.98 fitness. Section VI explains that high fitness does not establish human quality: many games are trivial or luck-dependent. Figures 6–7 show random-start generated rules and running games; no human study was conducted.
- **Scope decision:** the random-start generation branch is substantive and produces new executable games; this is not merely tuning. It is distinct from the later dedicated rule-generation track paper.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2015.7317941), [author manuscript](https://www.kmjn.org/publications/GeneratingVGDL_CIG15.pdf), [author abstract](https://www.kmjn.org/publications/GeneratingVGDL_CIG15-abstract.html).
- **Open status:** **Closed.** The author manuscript is public, but no paper-specific official generator or generated-game package was verified.
- **中文说明:** 用相对控制器表现引导规则演化，生成可执行 VGDL 游戏；随机起点实验符合从头生成要求，但高适应度常与实际玩法质量脱节。
- **English summary:** Relative controller performance guides VGDL rule evolution from random and existing-game seeds, with explicit negative findings on gameplay quality.

### 15. Evolving Chess-like Games Using Relative Algorithm Performance Profiles

- **Year / venue:** 2016, EvoApplications; Jakub Kowalski and Marek Szykuła.
- **Scope:** `rules`
- **Generated content:** complete executable chess-like rules in the Simplified Boardgames representation.
- **Method:** evolves rule sets by matching relative performance profiles of algorithms of different strengths to profiles of model games.
- **Evaluation:** the original publisher abstract explicitly reports evolved playable, balanced games. The authors' later full-text account confirms the generator's symmetrical games, royal piece, pawn-like initial row, and comparisons using multiple algorithms.
- **Evidence level:** original publisher abstract plus directly inspected coauthor follow-up manuscript; the original full text could not be recovered. No numerical experimental claims are inferred. The later paper describes regular-language piece moves and finite-automaton legal-move computation, confirming executable rules.
- **Primary sources:** [publisher chapter and abstract](https://doi.org/10.1007/978-3-319-31204-0_37), [coauthor's later full-text confirmation, sections 1–2.2](https://antoniosliapis.com/papers/mapping_chess_aesthetics_onto_procedurally_generated_chess-like_games.pdf).
- **Open status:** **Closed.** No official generator or evaluated-game package verified.
- **中文说明:** 以目标棋类游戏中的智能体相对表现为参照，演化完整可执行棋类规则；原始摘要与作者后续全文相互佐证，但未取得原实验数值细节。
- **English summary:** Evolves executable chess-like rules toward the relative algorithm-performance profiles of model games.

### 16. Adversarial Random Forest Classifier for Automated Game Design

- **Year / venue:** 2021, FDG; Thomas Maurer and Matthew Guzdial.
- **Scope:** `full-game`
- **Generated content:** jointly generated VGDL description files and tile levels, including sprites, interactions, termination rules, and parameters.
- **Method:** an RF classifier learns to distinguish eight human games from generated games; greedy hill climbing searches rule/level neighbors, then the RF retrains on successive output batches. Random-agent rollouts reject immediate crashes.
- **Evaluation:** two representations, with and without termination information, over five iterations each. Table 1 compares MCTS and random-agent completion, mean/max score, and moves. Completed-game counts are identical between agents in every generated batch; move-count differences are confounded by a five-minute time limit. Human-quality generation is not established.
- **Scope decision:** the learned classifier is internal to a generator that directly outputs new rules and levels; this is not an evaluator-only contribution.
- **Primary sources:** [arXiv](https://arxiv.org/abs/2107.12501), [full text](https://arxiv.org/html/2107.12501), [FDG DOI](https://doi.org/10.1145/3472538.3472587).
- **Official artifacts:** [repository](https://github.com/HonestPretzels/RF_Adversarial_PCG) includes generation/classification code, MCTS/random agents, experiment scripts, eight human training games, 80 evaluated generated games, per-game logs, and output CSV.
- **Open status:** **Partial, legacy setup.** The README calls absent `train.py`; no dependency/environment manifest or license file was verified. The source and evaluated outputs are public, but execution was not tested.
- **中文说明:** 随机森林作为学习到的适应度，驱动规则与关卡联合生成；公开实验揭示类人质量不足及评测混淆，工件需要修复历史安装流程。
- **English summary:** Adversarial RF retraining guides joint rule-and-level search, with negative generation-quality results and substantial but incompletely packaged artifacts.

### 17. A Controllable Co-Creative Agent for Game System Design

- **Year / venue:** 2023, arXiv.
- **Scope:** `rules`
- **Generated content:** executable game systems composed of state-machine-like components and resource flows.
- **Method:** Evolves executable abstract state/resource-flow systems by adding and modifying components under weighted design metrics; these are not complete games.
- **Evaluation:** Expressive-range analysis of 100,000 random abstract systems, approximately 33,000 accepted for simulated play; weighted-control tests on 25 designs show mixed metric-level significance.
- **Scope decision:** the generator changes components and flow structure, rather than only balancing fixed parameters of a pre-existing game. “Modeling Games Generically” acknowledges that humans still supply levels, stories and the rest of an actual playable game; Game Evaluator nevertheless executes states/actions/transitions/resources, and Genetic Game Generator changes structure, qualifying as abstract executable rules rather than complete games.
- **Primary sources:** [arXiv](https://arxiv.org/abs/2308.02317), [full text](https://arxiv.org/html/2308.02317).
- **Open status:** **Closed.** No paper-specific game generator or evaluator release verified. The related CreativeWand framework's checked release tree contains generic infrastructure/text examples, not this paper's generator.
- **中文说明:** 以状态和资源流建模可执行游戏，演化新增系统组件，并用可玩性分布和定向控制实验检验生成结果；指标可控性的证据有强弱差异。
- **English summary:** Evolves executable state/resource-flow game systems under controllable design metrics, with mixed metric-level controllability results.

### 18. Ludus Ex Machina: Building A 3D Game Designer That Competes Alongside Humans

- **Primary identity:** Michael Cook and Simon Colton; Fifth ICCC, 2014. [Official paper](https://computationalcreativity.net/iccc2014/wp-content/uploads/2014/06/4.2_Cook.pdf), [venue contents](https://computationalcreativity.net/iccc2014/proceedings/). The official proceedings correct the erroneous “Third” in Part II's bibliography.
- **Role/output:** generation method, `full-game`. Predesign retrieves theme-associated media; cooperative coevolution searches level geometry, zone maps, entity placements and stock executable rules. Postdesign exports required resources and design data as a separate Unity project and game binaries. Human-authored tile/behaviour libraries bound the design space; arbitrary new rule-code generation remains future work (PDF pp. 2–5).
- **Evaluation:** Figure 2 is a single-run four-species fitness trace, not repeated-seed evidence. Table 1 reports *To That Sect* and *Stretch Bouquet Point*, 500/551 overall among 780 December 2013 Ludum Dare jam-track entries. The contest setup uses 60 generations with populations 35/35/20/15, about three hours per game including retrieval; this differs from the typical 30-per-species/40-generation setup (pp. 5–7).
- **Limits:** little improvement in rules/zone fitness and simplistic core gameplay; different games confound the disclosed/undisclosed-author comparison, and raw voting data were not obtained. These rankings do not establish human-level design, universal playability or a causal attribution-bias effect.
- **Artifacts:** **Closed/unverified.** No official paper-specific runnable generator or reproduction package verified. Historical entry links and a Unity-export description do not establish current reproducibility.
- **Separate follow-up, not another counted method:** [Part II](https://doi.org/10.1109/TCIAIG.2016.2520305) is an independently identified later paper, not this paper's renamed/published version. Its Figure 8 repeats the same jam event. Its §V.C adds subjective author curation of 30 outputs each from three versions (33%, 60%, 80%); this is not an experiment reported in ICCC 2014 and not a playable rate. The AISB 2014 precursor also remains separately identified, with insufficient standalone generator evaluation for admission.
- **Scope correction, 2026-09-08:** replaces the former Part II primary entry without changing the count. The original method now supplies direct generation/evaluation evidence; no distinct additional generator in Part II was established for a second method record. See the [three-paper identity and evidence comparison](angelina-paper-identity-2026-09-08.md). This is a local scope correction, not a complete historical ANGELINA audit.
- **中文要点：** 原始 3D 生成方法以 ICCC 2014 为准；四物种协同进化完整 Unity 游戏，但图块、行为和媒体仍依赖预制/检索。后续策展实验归 Part II，不跨文移植或重复计数。
- **English summary:** Theme-conditioned cooperative coevolution generates complete Unity games; single-run fitness and game-jam outcomes provide bounded evidence, with later curation separately attributed.

## Playable-content methods and benchmarks / 可玩内容方法与 Benchmark

- **Independent audit:** [primary-source section evidence and limitations](independent-pcg-audit-2026-09-05.md), checked2026-09-05.

### 19. The Procedural Content Generation Benchmark

- **Year / venue:** 2025, FDG.
- **Scope:** `levels`
- **Generated content:** a unified testbed spanning mazes, platform levels, dungeons, puzzles, bullet-hell patterns, and one arcade-rule problem.
- **Method:** Gym-like problem APIs standardize content, quality constraints, controls, and generator evaluation across domains.
- **Evaluation:** `quality`, pairwise-threshold `diversity`, and target-satisfaction `controllability`, plus per-sample 0–1 detail vectors.
- **中文说明:** 这是目前最直接的 PCG 算法统一 benchmark，把多个游戏内容域放进同一套质量、多样性、可控性接口。
- **English summary:** A common API evaluates generators across many PCG domains with quality, diversity, and controllability measures.
- **Primary sources:** [paper](https://arxiv.org/abs/2503.21474), [ACM DOI](https://doi.org/10.1145/3723498.3723794), [official framework](https://github.com/amidos2006/pcg_benchmark), [official experiments](https://github.com/amidos2006/benchmark_experiments)
- **Open status:** **Open.** MIT-licensed problems, evaluator, baselines, and experiments are public.
- **Targeted release-document check, 2026-09-08:** [pinned framework and experiment READMEs](experiment-entry-points-2026-09-08.md) distinguish the two repositories, environment/representation versions, population-dependent diversity and candidate-evaluation budgets. Documentation was checked, but no experiment was run.

### 20. The 2010 Mario AI Championship: Level Generation Track

- **Year / venue:** 2011, IEEE Transactions on Computational Intelligence and AI in Games.
- **Scope:** `levels`
- **Generated content:** Super Mario Bros.-style levels created online for a player.
- **Method:** the competition API lets generators condition content on player/gameplay information; submitted algorithms ranged from constructive to adaptive approaches.
- **Evaluation:** competition protocol and player studies compare generated levels using play experience/preferences and measured level characteristics.
- **中文说明:** 这一赛道把“为真实玩家现场生成 Mario 关卡”正式做成比赛，是后续平台关卡 benchmark 的重要起点。
- **English summary:** The championship formalized online Mario level generation and evaluated submissions with players and level statistics.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TCIAIG.2011.2166267)
- **Open status:** **Partial.** The protocol and results are primary-source documented, but the original full competition service/submissions are not maintained as a turnkey package.

### 21. General Video Game AI: A Multitrack Framework for Evaluating Agents, Games, and Content Generation Algorithms

- **Year / venue:** 2019, IEEE Transactions on Games.
- **Scope:** `levels` benchmark; only the formally defined generation track is represented by this record.
- **Generated content:** VGDL levels produced for many rule-defined games through the dedicated generation interface.
- **Method:** a common VGDL runtime separates game rules, level descriptions, generators, and evaluators so generation systems can be compared under one protocol.
- **Evaluation:** the framework defines generation-track validity/playability procedures and competition protocols; playing-agent tracks are outside this note's scope.
- **中文说明:** GVGAI 的价值在于用统一 VGDL 引擎评测跨游戏关卡生成；这里不收录它的“玩游戏”排行榜。
- **English summary:** GVGAI provides a shared executable language and competition protocol for general level generation across games.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TG.2019.2901021), [2016 level-generation-track precursor](https://doi.org/10.1145/2908812.2908920), [official framework](https://github.com/GAIGResearch/GVGAI).
- **Open status:** **Open.** The engine, sample games, and level-generation interfaces are publicly maintained. The playing-agent tracks remain excluded.

### 22. Launchpad: A Rhythm-Based Level Generator for 2-D Platformers

- **Year / venue:** online 2010; IEEE Transactions on Computational Intelligence and AI in Games 3(1), 2011. The shorter precursor appeared at FDG 2009.
- **Scope and task/method:** `levels`; a two-tier grammar first generates player-action rhythms and then geometry, joining rhythm groups into parameter-controlled complete 2-D platform levels that are playable by construction.
- **Evaluation:** linearity and leniency plots over 10,000 generated levels characterize expressive range; normalized edit distance and clustering compare rhythm groups and expose generator biases.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TCIAIG.2010.2095855), [author manuscript](https://users.soe.ucsc.edu/~ejw/papers/Smith-Launchpad-TCIAIG-2011.pdf), [FDG 2009 precursor](https://doi.org/10.1145/1536513.1536548), [official legacy demo](https://users.soe.ucsc.edu/~gsmith/launchpad/platformer/), [official visualization and source](https://users.soe.ucsc.edu/~gsmith/launchpad/viztool/).
- **Open status:** **Partial, legacy-only.** The Flash demo and Java/Processing visualization remain downloadable, and the visualization source is exposed, but modern browsers cannot run them directly and the complete level-generator source was not released.
- **Scope decision:** generation is the research product; player physics and playability constraints are used to construct valid levels, not to train or rank a playing policy.
- **中文说明:** Launchpad 用节奏语法和几何语法自动装配保证可玩的完整平台关卡，并以 10,000 个样本分析生成空间；遗留 demo 尚在，但完整生成器源码缺失。
- **English summary:** Launchpad generates guaranteed-playable platform levels from action rhythms and evaluates the generator's expressive range rather than a player's score.

### 23. Towards Automatic Personalised Content Creation for Racing Games

- **Year / venue:** 2006 precursor, *Making Racing Fun Through Player Modeling and Track Evolution*; expanded at the 2007 IEEE Conference on Computational Intelligence and Games.
- **Scope and task/method:** `levels`; learns models of individual driving behavior and evolves smooth closed racing tracks whose challenge and speed profile target each modeled player.
- **Evaluation:** models five drivers and compares track representations and initialization schemes through controller progress, variance, speed, and qualitative personalization results.
- **Primary sources:** [IEEE DOI for the expanded paper](https://doi.org/10.1109/CIG.2007.368106), [UCL institutional record for the 2006 precursor](https://discovery.ucl.ac.uk/id/eprint/1330829/).
- **Open status:** **Closed.** No official track generator, player-model code, generated outputs, or evaluation package was verified.
- **Scope decision:** player controllers supply preference/difficulty estimates for generated tracks; the evaluated output is personalized playable content, not driving-policy performance.
- **中文说明:** 论文学习五名车手的行为，再进化与个人能力相匹配的闭合赛道；玩家模型和控制器只服务于赛道生成与评价。
- **English summary:** Driver models guide evolutionary search toward personalized playable race tracks rather than toward a stronger driving agent.

### 24. Towards Automatic Personalized Content Generation for Platform Games

- **Year / venue:** 2010, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE).
- **Scope and task/method:** `levels`; searches Mario level parameters using learned player-experience models and generates the next level for a particular playing style.
- **Evaluation:** experience models use 327 players and 1,308 sessions; adapted levels are tested with two controllers and people, and 60% of the ten direct-comparison participants prefer the adapted level.
- **Primary sources:** [AIIDE DOI and proceedings record](https://doi.org/10.1609/aiide.v6i1.12399).
- **Open status:** **Closed.** No official adaptation code, trained player models, generated-level corpus, or experiment data was verified.
- **Scope decision:** related player-model-only papers that stop before generating content are excluded; this paper is included because it actually searches parameters and emits the personalized level.
- **中文说明:** 与只建立玩家体验模型的前作不同，这篇论文实际搜索 Mario 关卡参数并生成个性化下一关，因此属于生成游戏内容。
- **English summary:** Learned experience models are operationalized to search and emit personalized Mario levels, rather than being evaluated only as player models.

### 25. Polymorph: A Model for Dynamic Level Generation

- **Year / venue:** 2010, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE).
- **Scope and task/method:** `levels`; learns difficulty and player-skill models, then generates short platform segments online so structural challenge follows current performance.
- **Evaluation:** uses 211 players and 2,258 segment playthroughs; the learned model orders difficulty pairs, and the paper examines dynamically selected example segments.
- **Primary sources:** [AIIDE DOI and proceedings record](https://doi.org/10.1609/aiide.v6i1.12417).
- **Open status:** **Closed.** The paper historically linked official Polymorph and data-collector Flash applications, but those links now fail; no generator source, learned model, or experiment data remain available.
- **Scope decision:** online adaptation changes the playable level geometry itself, so this is dynamic content generation rather than a playing-agent task.
- **中文说明:** Polymorph 根据玩家当前表现在线生成下一段平台关几何；其核心产物是动态关卡，而不是控制角色的策略。
- **English summary:** Polymorph continually generates platform segments whose structural difficulty follows an estimated player-skill trajectory.

### 26. Tanagra: Reactive Planning and Constraint Solving for Mixed-Initiative Level Design

- **Year / venue:** a 2010 FDG expressive-range precursor; IEEE Transactions on Computational Intelligence and AI in Games, 2011.
- **Scope and task/method:** `levels`; combines reactive planning with numerical constraints to autonomously generate or regenerate rhythm-paced 2-D platform levels around designer edits while preserving reachability.
- **Evaluation:** maps linearity and leniency over 10,000 unique generated levels and demonstrates responsive co-creation operations.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TCIAIG.2011.2159716), [2010 expressive-range precursor](https://doi.org/10.1145/1814256.1814260), [author manuscript](https://users.soe.ucsc.edu/~ejw/papers/Smith-Tanagra-TCIAIG-2011.pdf), [official legacy demonstration](https://users.soe.ucsc.edu/~gsmith/tanagra/v2_demo/demo.htm).
- **Open status:** **Closed, legacy demo only.** The Flash demonstration remains online, but no generator source or runnable reproducibility package was verified.
- **Scope decision:** mixed initiative does not make the work editor-only: Tanagra contains a substantive automatic generator that can create and repair playable levels without requiring every placement from a human.
- **中文说明:** Tanagra 既能响应设计师编辑，也能自主规划并约束求解出可达平台关；因包含实质自动生成器，归入关卡核心分区。
- **English summary:** Reactive planning and constraint solving support both autonomous generation and responsive co-creation of reachable platform levels.

### 27. Sentient Sketchbook: Computer-Aided Game Level Authoring

- **Year / venue:** 2013, Foundations of Digital Games.
- **Scope and task/method:** `levels`; feasible-infeasible novelty/objective search generates playable strategy-map alternatives in real time from the designer's current sketch.
- **Evaluation:** compares constrained-search methods over 20 runs and reports 24 design sessions with five industry experts.
- **Primary sources:** [official paper PDF](https://sentientsketchbook.com/research/sentient_sketchbook.pdf), [official project](https://sentientsketchbook.com/), [official 2014 JAR download](https://sentientsketchbook.com/download.php).
- **Open status:** **Partial, legacy-only.** A runnable historical JAR remains available, but no source, modern runtime package, or complete experiment data was verified.
- **Scope decision:** although mixed-initiative, the system automatically proposes complete playable alternatives and has a primary generator evaluation; the related map-sketch generation work is treated as the same system family rather than counted again.
- **中文说明:** Sentient Sketchbook 会从当前草图实时生成完整、可玩的策略地图备选，并非只提供手工编辑界面，因此列入关卡核心分区。
- **English summary:** The tool automatically searches for playable strategy-map alternatives around a designer sketch and exposes them in a mixed-initiative workflow.

### 28. Learning to Generate Video Game Maps Using Markov Models

- **Year / venue:** 2013–2016, AIIDE conference series and IEEE Transactions on Computational Intelligence and AI in Games.
- **Scope and task/method:** `levels`; learns single-layer and hierarchical multi-dimensional Markov models from human-authored maps, then samples new Mario, Lode Runner, and Kid Icarus levels.
- **Evaluation:** compares playability, linearity, and leniency with non-hierarchical/manual hierarchies and Mario competition generators; the 2015 automatically learned hierarchy reaches 66% Mario playability.
- **Primary sources:** [journal version](https://doi.org/10.1109/TCIAIG.2016.2623560), [2013 AIIDE paper](https://doi.org/10.1609/aiide.v9i2.12586), [2014 AIIDE hierarchy paper](https://doi.org/10.1609/aiide.v10i1.12708), [2015 AIIDE paper](https://doi.org/10.1609/aiide.v11i1.12794). The same family also includes the FDG 2014 paper *Experiments in Map Generation Using Markov Chains*, whose legacy official URL is HTTP-only.
- **Open status:** **Closed.** The 2015 paper historically linked Mario/Lode Runner training sets, but the package is no longer visible; no official generator code, trained models, fixed data package, or evaluation scripts were verified.
- **Scope decision:** the five records are methodological extensions of the same map-generation lineage and are counted as one version family, not five papers. Later constrained-sampling, domain-transfer, training-data, movement-model, and multi-layer branches make independent generation contributions and are listed separately in this dossier.
- **中文说明:** 这一版本族从单层多维 Markov 模型逐步扩展到自动学习层级结构，直接生成 Mario、Lode Runner 与 Kid Icarus 地图；五个版本合并计数一次。
- **English summary:** A sequence of Markov-map papers progresses from flat to learned hierarchical models for sampling playable platform and puzzle levels.

### 29. Procedural Level Generation Using Occupancy-Regulated Extension

- **Year / venue:** 2010, IEEE Conference on Computational Intelligence and Games.
- **Scope and task/method:** `levels`; iteratively attaches human-authored geometry chunks at possible player-occupancy anchors, supporting varied platform spaces and mixed-initiative extension at arbitrary scales.
- **Evaluation:** critically analyzes outputs from an Infinite Mario implementation with 42 chunks; complete levels take about 15 seconds to generate. No experimental playtest was run, and the system explicitly does not guarantee playability.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/ITW.2010.5593333), [author manuscript](https://www.cs.hmc.edu/~pmawhorter/research/papers/procedural_level_generation_using_occupancy_regulated_extension-Mawhorter_Mateas-2010.pdf).
- **Open status:** **Closed.** No official generator, chunk library, generated-level corpus, or evaluator package was verified.
- **Scope decision:** the algorithm's output is newly constructed level geometry; occupancy is a construction control, not a gameplay-return objective.
- **中文说明:** ORE 在玩家可能占据的锚点处拼接人工几何块，直接生成多样的平台关空间；论文明确说明当时尚不保证可玩。
- **English summary:** ORE assembles authored chunks at player-occupancy anchors to generate varied platform spaces, without claiming a playability guarantee.

### 30. Multiobjective Exploration of the StarCraft Map Space

- **Year / venue:** 2010, FDG PCGames workshop and IEEE Conference on Computational Intelligence and Games.
- **Scope and task/method:** `levels`; multiobjective evolutionary search generates complete RTS maps including terrain, bases, and resources, with the expanded paper instantiating the representation for StarCraft.
- **Evaluation:** Pareto-front approximations expose trade-offs among partly conflicting predicted-player-experience objectives such as fairness, resource/base placement, paths, and terrain characteristics; each point is a viable candidate map.
- **Primary sources:** [StarCraft paper DOI](https://doi.org/10.1109/ITW.2010.5593346), [generic precursor DOI](https://doi.org/10.1145/1814256.1814259), [precursor institutional manuscript](https://www.um.edu.mt/library/oar/bitstream/123456789/81279/1/Towards_multiobjective_procedural_map_generation_2010.pdf), [StarCraft institutional manuscript](https://www.um.edu.mt/library/oar/bitstream/123456789/29280/1/Multiobjective_exploration_of_the_starcraft_map_space_2010.pdf).
- **Open status:** **Closed.** The papers and institutional manuscripts are available, but no official map generator, StarCraft exporter, experiment data, or evaluator release was verified.
- **Scope decision:** the Pareto fronts rank generated maps and support selection; no RTS-playing agent or win-rate benchmark is the research product.
- **中文说明:** 该版本族从通用策略地图扩展到完整 StarCraft 地图，用 Pareto 前沿呈现公平性、资源和地形目标的权衡。
- **English summary:** Multiobjective evolution produces complete RTS maps and exposes design trade-offs as Pareto fronts for automatic or assisted selection.

### 31. Generating Missions and Spaces for Adaptable Play Experiences

- **Year / venue:** 2010, FDG PCGames workshop; extended in IEEE Transactions on Computational Intelligence and AI in Games, 2011.
- **Scope and task/method:** `levels`; generative grammars first rewrite mission graphs and then construct spatial layouts that make the generated action-adventure progression executable.
- **Evaluation:** generated case studies demonstrate coherent mission-to-space mappings, adaptation operations, and the expressive consequences of the grammar rules; no common quantitative leaderboard is defined.
- **Primary sources:** [journal DOI](https://doi.org/10.1109/TCIAIG.2011.2149523), [2010 precursor DOI](https://doi.org/10.1145/1814256.1814257), [institutional author manuscript](https://research.hva.nl/files/149264/453867_Dormans_Bakkes_-_Generating_Missions_and_Spaces_for_Adaptable_Play_Experiences.pdf).
- **Open status:** **Closed.** An official institutional manuscript is available, but no generator, grammar package, output corpus, or evaluator was verified.
- **Scope decision:** missions and spaces are jointly generated as playable structure rather than as prose-only narrative or a policy trace.
- **中文说明:** 系统先生成任务图，再生成能承载该任务进程的空间，把任务与关卡联合起来，而不是只写故事文本。
- **English summary:** Coupled grammars generate an action-adventure mission graph and the spatial level needed to enact that mission.

### 32. A Generic Approach to Challenge Modeling for the Procedural Creation of Video Game Levels

- **Year / venue:** 2010, EvoApplications; extended in IEEE Transactions on Computational Intelligence and AI in Games, 2011.
- **Scope and task/method:** `levels`; feasible-infeasible two-population evolution separates hard play/connectivity constraints from optimization of a top-down target challenge model.
- **Evaluation:** the precursor generates example levels for two genres, and the extended system studies valid output and controllable challenge behavior across domain definitions.
- **Primary sources:** [journal DOI](https://doi.org/10.1109/TCIAIG.2011.2161310), [framework precursor](https://doi.org/10.1007/978-3-642-12239-2_14).
- **Open status:** **Closed.** No official implementation, domain encodings, generated-level set, or evaluation scripts were verified.
- **Scope decision:** simulated feasibility and challenge estimates score generated levels; agent performance is an evaluator signal, not the output.
- **中文说明:** FI-2Pop 把玩法硬约束与目标挑战度分开搜索，可跨游戏类型生成连通、可玩的目标难度关卡。
- **English summary:** A generic FI-2Pop framework evolves feasible levels toward top-down challenge targets across multiple game genres.

### 33. Search-Based Procedural Generation of Maze-Like Levels

- **Year / venue:** 2011, IEEE Transactions on Computational Intelligence and AI in Games.
- **Scope and task/method:** `levels`; evolutionary search constructs connected, solvable maze-like layouts under explicit path and structural objectives instead of sampling unconstrained random mazes.
- **Evaluation:** compares representations and operators through path, connectivity, and structural properties of generated populations.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TCIAIG.2011.2138707).
- **Open status:** **Closed.** No official generator, benchmark instances, generated corpus, or experiment package was verified.
- **Scope decision:** the mazes themselves are the optimized artifact; solver/path calculations only evaluate those artifacts.
- **中文说明:** 论文用进化搜索直接构造连通、可解的迷宫式关卡，并以路径和结构指标筛选，而不是训练走迷宫策略。
- **English summary:** Evolutionary search generates solvable maze-like levels and evaluates their path and topology rather than an agent's return.

### 34. Evolving Interesting Maps for a First Person Shooter

- **Year / venue:** 2011, EvoApplications.
- **Scope and task/method:** `levels`; evolves complete maps loadable in Cube 2 and uses bot matches plus average fighting time only as a proxy fitness for map interest.
- **Evaluation:** compares four map representations and finds substantial differences in their ability to produce interesting, playable FPS layouts.
- **Primary sources:** [Springer DOI and chapter record](https://doi.org/10.1007/978-3-642-20525-5_7).
- **Open status:** **Closed.** No official evolutionary system, Cube 2 map corpus, bot configuration, or evaluator package was verified.
- **Scope decision:** bots evaluate newly generated FPS maps; stronger bot play, score, or win rate is not the paper's contribution.
- **中文说明:** 系统进化可载入 Cube 2 的完整 FPS 地图，并用 bot 平均交战时间评价地图趣味性；bot 只是评分器。
- **English summary:** Evolution generates playable Cube 2 maps, while bot fighting time serves only as a map-quality estimate.

### 35. Evolving Levels for Super Mario Bros Using Grammatical Evolution

- **Year / venue:** 2012, IEEE Conference on Computational Intelligence and Games; personalized extension at AIIDE 2012.
- **Scope and task/method:** `levels`; grammatical evolution composes complete Mario levels from a compact design grammar, while the extension uses learned engagement, frustration, and challenge models as fitness functions for player-specific generation.
- **Evaluation:** compares expressive range, aesthetic and similarity measures against feature-based and original generators; the extension uses experience models trained from more than 1,500 crowd-sourced game sessions.
- **Primary sources:** [CIG DOI](https://doi.org/10.1109/CIG.2012.6374170), [personalized AIIDE extension](https://doi.org/10.1609/aiide.v8i1.12501), [institutional author manuscript](https://www.um.edu.mt/library/oar/bitstream/123456789/22937/1/Evolving_Levels_for_Super_Mario_Bros_Using_Grammat.pdf).
- **Open status:** **Closed.** No official GE implementation, grammar/evolution package, generated corpus, player-model package, or evaluation scripts were verified.
- **Scope decision:** this is distinct from the four-parameter exhaustive-search adapter in *Towards Automatic Personalized Content Generation for Platform Games*: the generative representation and search space are replaced by grammatical evolution.
- **中文说明:** 这一族用设计语法进化完整 Mario 关卡，并在扩展版中用众包玩家体验模型优化个性化内容；它与 *Towards Automatic Personalized Content Generation for Platform Games* 的小参数穷举适配器不同。
- **English summary:** Grammatical evolution generates complete Mario levels and later optimizes them against learned player-experience models.

### 36. Procedural Content Generation Using Patterns as Objectives

- **Year / venue:** 2014, EvoApplications.
- **Scope and task/method:** `levels`; represents Mario-like levels as sequences of micro-pattern slices extracted from human levels and evolves them toward meso-pattern objectives; the multi-level extension adds macro-pattern composition.
- **Evaluation:** studies the distributions of micro-, meso-, and macro-patterns, showing recognizable source style with substantial geometric variation.
- **Primary sources:** [Springer DOI and chapter record](https://doi.org/10.1007/978-3-662-45523-4_27), [multi-level extension](https://doi.org/10.1109/CIG.2014.6932909).
- **Open status:** **Closed.** No official generator, extracted-pattern dataset, generated-level corpus, or analysis package was verified.
- **Scope decision:** design patterns are search objectives for newly generated levels, not labels for analyzing a fixed corpus alone.
- **中文说明:** 系统把人工关卡切片作为微观模式，以更高层的中观设计模式作为进化目标，直接生成新的 Mario 风格关卡。
- **English summary:** Evolution recombines human-level slices while optimizing for larger design patterns, retaining style without copying whole levels.

### 37. Linear Levels Through N-Grams

- **Year / venue:** 2014, 18th International Academic MindTrek Conference (AcademicMindTrek 2014), pp. 200–206.
- **Scope and task/method:** `levels`; learns n-gram transition models over vertical slices of human-authored Mario levels and samples new left-to-right levels at different history lengths.
- **Evaluation:** compares n-gram orders through generated tile/pattern distributions, structural characteristics, and expressive-range behavior.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/2676467.2676506), [official IT University research record](https://pure.itu.dk/en/publications/linear-levels-through-n-grams/).
- **Open status:** **Closed.** No official implementation, trained models, fixed corpus snapshot, or evaluation scripts were verified.
- **Scope decision:** this vertical-slice sequence model is methodologically separate from the tile-level multi-dimensional Markov family in *Learning to Generate Video Game Maps Using Markov Models*.
- **中文说明:** 论文从 Mario 纵向切片学习 n-gram 并采样横向关卡；它与 *Learning to Generate Video Game Maps Using Markov Models* 的二维多维 Markov 模型不是同一系统。
- **English summary:** Vertical-slice n-grams learn local sequence structure from Mario levels and sample new linear platform stages.

### 38. MCMCTS PCG 4 SMB: Monte Carlo Tree Search to Guide Platformer Level Generation

- **Year / venue:** 2015, AIIDE Experimental AI in Games workshop.
- **Scope and task/method:** `levels`; uses Mario-trained Markov transitions as MCTS moves and rollouts, pruning unsolvable branches while exposing designer controls for gaps, enemies, and rewards.
- **Evaluation:** uses 200 rollouts per move to generate 320-slice levels in under 30 seconds with a near-playability guarantee; a player study probes eight parameter variants and downstream experience models.
- **Primary sources:** [AIIDE DOI and open proceedings paper](https://doi.org/10.1609/aiide.v11i3.12816).
- **Open status:** **Closed.** No official generator, training corpus, player-study data, or evaluator release was verified.
- **Scope decision:** MCTS is repurposed as a content search procedure; the research output is a generated Mario level, not a Mario-playing policy.
- **中文说明:** MCMCTS 把通常用于玩游戏的 MCTS 改作关卡搜索，用 Markov 转移扩展并剪枝不可解 Mario 关卡。
- **English summary:** MCTS guides a Markov generator toward solvable, designer-controlled Mario levels rather than toward stronger game play.

### 39. Sampling Hyrule: Multi-Technique Probabilistic Level Generation for Action Role Playing Games

- **Year / venue:** 2015, AIIDE Experimental AI in Games workshop; builds on the FDG 2015 paper *Data-Driven Learning of Level Topology*.
- **Scope and task/method:** `levels`; samples Zelda dungeon topology from a Bayesian network, generates individual rooms by interpolation in a PCA-compressed space, and repairs or resamples constraint violations.
- **Evaluation:** checks room accessibility, key-door ordering, required special-room types, and completion constraints; 20 dungeons are sampled at each of the 12-, 35-, and 47-room scales.
- **Primary sources:** [AIIDE DOI and open proceedings paper](https://doi.org/10.1609/aiide.v11i3.12817).
- **Open status:** **Closed.** No official generator, learned Bayesian/PCA models, Zelda corpus, generated output set, or evaluator package was verified.
- **Scope decision:** the predecessor learns topology; Sampling Hyrule operationalizes it into an actual generator, so the two are one development lineage rather than two counted entries.
- **中文说明:** 系统从 Zelda 人工地牢学习拓扑和房间表示，再采样并修复成可通关地牢；前作与生成版合并为一个版本族。
- **English summary:** A learned Bayesian topology and PCA room model are combined to sample constraint-valid, completable Zelda-style dungeons.

### 40. Automatic Generation of Game Elements via Evolution

- **Year / venue:** 2010, IEEE Conference on Computational Intelligence and Games.
- **Scope and task/method:** `playable-content`; uses evolutionary search and dynamic programming to generate solvable chess-maze and chromatic-puzzle instances under fixed rules, creating new challenge layouts rather than cosmetic assets.
- **Evaluation:** runs 540 chess-parameter experiments; both targeted conditions achieve 30/30 successes, and seven groups of 30 inspected outputs contain no duplicates.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/ITW.2010.5593341).
- **Open status:** **Closed.** No official generator, puzzle corpus, solver/evaluator, or experiment package was verified.
- **Scope decision:** the outputs are playable puzzle instances, consistent with the collection's inclusion of Sokoban, Connections, and other generated puzzles.
- **中文说明:** 论文进化新的 chess maze 和 chromatic puzzle 可玩实例；固定的是规则，生成的是决定挑战的谜题结构，因此不是纯资产。
- **English summary:** Evolution produces complete playable instances in two puzzle domains and is evaluated as content search rather than game play.

### 41. Alone We Can Do So Little, Together We Can Do So Much: A Combinatorial Approach for Generating Game Content

- **Year / venue:** 2014, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE).
- **Scope and task/method:** `levels`; trains non-negative matrix factorization on 5,000 200×15 Mario levels from five dissimilar generators, then recombines learned component patterns into loadable new levels.
- **Evaluation:** expressivity metrics show that the combined generator can resemble each source generator while covering a wider and more novel content space.
- **Primary sources:** [AIIDE DOI and open proceedings paper](https://doi.org/10.1609/aiide.v10i1.12729).
- **Open status:** **Closed.** No official NMF generator, five-source training set, generated corpus, or analysis scripts were verified.
- **Scope decision:** this paper implements and evaluates a new combinatorial generator; it is not merely a comparison of the five input systems.
- **中文说明:** 系统学习五个差异明显的 Mario 生成器所产模式并重新组合，能覆盖比任一单独生成器更宽的新颖内容空间。
- **English summary:** NMF learns from five Mario generators and recombines their component patterns into a broader joint generative space.

### 42. Cellular Automata for Real-Time Generation of Infinite Cave Levels

- **Year / venue:** 2010, FDG PCGames workshop.
- **Scope and task/method:** `levels`; generates Cave Crawler cave-map regions with cellular automata on demand, allowing an effectively infinite playable level to expand during play.
- **Evaluation:** ten-run timing tests report about `1.4×10^-4 ms` for random-map generation, `4.1×10^-1 ms` for cellular-automata maps, and 349 ms for a 3×3 base grid, testing real-time feasibility rather than player performance.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/1814256.1814266).
- **Open status:** **Closed.** No official Cave Crawler generator, source, generated-map corpus, or performance harness was verified.
- **Scope decision:** the paper's output is an indefinitely extending playable cave map; generation-time measurements are system evaluation, not gameplay-agent metrics.
- **中文说明:** 论文在 Cave Crawler 游玩过程中按需生成洞穴区域，使地图近似无限扩展；耗时实验评价生成器能否实时运行。
- **English summary:** Cellular automata generate cave regions online so a Cave Crawler level can expand indefinitely within real-time timing budgets.

### 43. Controllable Procedural Content Generation via Constrained Multi-Dimensional Markov Chain Sampling

- **Year / venue:** 2016, Twenty-Fifth International Joint Conference on Artificial Intelligence (IJCAI-16).
- **Scope and task/method:** `levels`; adds global constraints and constrained sampling to learned multi-dimensional Markov chains so the generator can target structural requirements in Super Mario Bros. and Kid Icarus maps.
- **Evaluation:** samples 100 maps for every feasible algorithm–constraint-set combination and compares valid samples, playability, and satisfaction of the requested structural controls. Lode Runner is mentioned only as future work, not as an evaluated domain.
- **Primary sources:** [official IJCAI abstract page](https://www.ijcai.org/Abstract/16/116), [official proceedings PDF](https://www.ijcai.org/Proceedings/16/Papers/116.pdf).
- **Open status:** **Closed.** No official implementation, constraint definitions, trained models, fixed training corpus, generated-map set, or evaluation package was verified.
- **Scope decision:** constrained sampling is a substantive controllable-generation contribution beyond the learned hierarchy in *Learning to Generate Video Game Maps Using Markov Models*, so the paper is listed separately rather than hidden inside that lineage.
- **中文说明:** 论文把全局约束直接纳入多维 Markov 采样，在 Mario 与 Kid Icarus 上生成满足结构控制的地图；Lode Runner 只出现在未来工作中。
- **English summary:** Global constraints steer MdMC sampling toward controllable Mario and Kid Icarus maps instead of merely filtering unconstrained samples afterward.

### 44. An Approach to Domain Transfer in Procedural Content Generation of Two-Dimensional Videogame Levels

- **Year / venue:** 2016, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE).
- **Scope and task/method:** `levels`; learns tile mappings among Super Mario Bros., Kid Icarus, and Kid Kool so a probabilistic generator can train on level data from a structurally related game.
- **Evaluation:** compares human-authored, random, and automatically learned mappings through likelihood, linearity, leniency, and the expressive spaces of generated levels.
- **Primary sources:** [AIIDE DOI and open proceedings record](https://doi.org/10.1609/aiide.v12i1.12853).
- **Open status:** **Closed.** No official transfer implementation, tile mappings, trained models, fixed cross-domain corpus, generated output set, or evaluation scripts were verified.
- **Scope decision:** the paper contributes and evaluates a distinct domain-transfer generator rather than another parameter setting of the hierarchy in *Learning to Generate Video Game Maps Using Markov Models*.
- **中文说明:** 系统自动学习 Mario、Kid Icarus 与 Kid Kool 间的瓷砖映射，让关卡生成器可以迁移使用另一款游戏的训练数据。
- **English summary:** Learned cross-game tile mappings let a probabilistic generator transfer level structure among three 2-D platformers.

### 45. Player Movement Models for Video Game Level Generation

- **Year / venue:** 2017, Twenty-Sixth International Joint Conference on Artificial Intelligence (IJCAI-17).
- **Scope and task/method:** `levels`; learns action and surrounding-conditioned movement likelihoods from Mario gameplay video, then uses the movement model to guide MdMC/VLR level sampling toward plausible human traversal paths.
- **Evaluation:** compares conditioned variants through path likelihood, playability, linearity, leniency, and generated-level examples; player movement is a generation constraint, not a policy-performance target.
- **Primary sources:** [IJCAI DOI](https://doi.org/10.24963/ijcai.2017/105), [official proceedings PDF](https://www.ijcai.org/proceedings/2017/0105.pdf), [author experiment repository](https://bitbucket.org/Sam_Snodgrass/ijcai_2017).
- **Open status:** **Partial, legacy/unlicensed.** The Bitbucket repository contains code, training data, and sampled levels, but no license, maintained environment, or modern reproduction instructions were verified.
- **Scope decision:** learning a player model is an intermediate step; the paper's implemented output is newly sampled Mario geometry conditioned on likely human paths.
- **中文说明:** 系统从 Mario 游玩视频学习移动似然，再把它作为关卡采样约束；代码、训练数据与样例仍在 Bitbucket，但没有许可证或现代环境。
- **English summary:** Movement patterns learned from video steer probabilistic generation toward Mario levels with plausible human traversal paths.

### 46. Procedural Level Generation Using Multi-Layer Level Representations with MdMCs

- **Year / venue:** 2017, IEEE Conference on Computational Intelligence and Games; Lode Runner extension at the AIIDE Experimental AI in Games workshop.
- **Scope and task/method:** `levels`; couples structural, path, and auxiliary semantic layers so MdMC sampling preserves relationships that one tile layer misses. Mario uses structural/path/height layers; the extension uses structural/path/section layers for Lode Runner.
- **Evaluation:** compares layer combinations and generated maps through playability and structural/style characteristics in Mario and Lode Runner.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2017.8080447), [official CIG paper](https://cig2017.com/wp-content/uploads/2017/08/paper_9.pdf), [Lode Runner extension](https://doi.org/10.1609/aiide.v13i2.12966).
- **Open status:** **Closed.** No official generator, aligned multilayer corpus, trained models, generated output set, or evaluation scripts were verified.
- **Scope decision:** the CIG paper and its Lode Runner extension are one multilayer-representation family; their explicit cross-layer generation contribution is separate from the flat/hierarchical map lineage in *Learning to Generate Video Game Maps Using Markov Models*.
- **中文说明:** 多层表示把结构、路径和高度/分区共同建模，在 Mario 与 Lode Runner 中保留单层瓷砖表示容易丢失的跨层关系。
- **English summary:** Coupled semantic layers let MdMCs sample levels whose geometry remains consistent with traversable paths and higher-level structure.

### 47. Game Level Generation from Gameplay Videos

- **Year / venue:** 2015 workshop precursor *Toward Game Level Generation from Gameplay Videos*; expanded at AIIDE 2016.
- **Scope and task/method:** `levels`; extracts Mario geometry and player movement from raw gameplay videos without source maps, learns a probabilistic graph over observed chunks, and assembles complete new levels.
- **Evaluation:** extracts 13,492 chunks from nine videos, compares generated style likelihood with existing generators, and evaluates complete generated levels in a 73-person play study.
- **Primary sources:** [AIIDE DOI and open proceedings record](https://doi.org/10.1609/aiide.v12i1.12861).
- **Open status:** **Closed.** No official video-processing pipeline, source-video set, learned graph, generator, generated-level corpus, comparison code, or player-study data was verified.
- **Scope decision:** the 2015 precursor and 2016 full paper are one development family; this probabilistic-graph pipeline is distinct from the player-tailored LSTM generator in *Super Mario as a String: Platformer Level Generation Via LSTMs*.
- **中文说明:** 该版本族在没有原始地图文件的情况下，从九段 Mario 视频提取 13,492 个片段并学习概率图，再装配完整新关卡。
- **English summary:** Geometry and motion recovered from raw Mario videos train a probabilistic graph that assembles full playable levels.

### 48. Autoencoders for Level Generation, Repair, and Recognition

- **Year / venue:** 2016, ICCC workshop paper.
- **Scope and task/method:** `levels`; trains an autoencoder over small Mario tile windows and decodes noisy or incomplete inputs to generate new tiles, repair damaged regions, and recognize level style.
- **Evaluation:** uses 22 Mario maps and 4,366 windows in a proof-of-concept analysis of reconstruction, noise-driven generation, repair, and recognition.
- **Primary sources:** [archived author manuscript](https://web.archive.org/web/20230507072222id_/http%3A%2F%2Fjulian.togelius.com%2FJain2016Autoencoders.pdf).
- **Open status:** **Closed.** No official code, trained autoencoder, fixed data split, generated/repaired corpus, or evaluation package was verified.
- **Scope decision:** the system actually emits and repairs game-level tiles; recognition is one of three tested uses, not the sole task.
- **中文说明:** Autoencoder 从 Mario 小窗口学习表示，并通过解码含噪或缺失输入来生成与修复瓷砖；识别只是并列用途之一。
- **English summary:** A small autoencoder proof of concept decodes noisy Mario windows for generation and repair as well as style recognition.

### 49. Composing Video Game Levels with Music Metaphors through Functional Scaffolding

- **Year / venue:** 2015, First Computational Creativity and Games Workshop.
- **Scope and task/method:** `levels`; treats Mario tile types as musical voices, learns accompaniment relationships with NEAT, and composes the voices into complete playable levels through functional scaffolding.
- **Evaluation:** qualitatively analyses generated examples and the learned functional relationships among tile voices as a proof of concept rather than defining a shared benchmark.
- **Primary sources:** [archived author manuscript](https://web.archive.org/web/20160903064341id_/http%3A%2F%2Fjulian.togelius.com%2FHoover2015Composing.pdf).
- **Open status:** **Closed.** No official generator, training corpus, evolved-network set, generated levels, or evaluator was verified.
- **Scope decision:** the music metaphor is an internal compositional representation; the output is a complete Mario level, so this is not music-asset generation.
- **中文说明:** 论文把 Mario 瓷砖类型视作音乐声部并学习其“伴奏”关系，最终产物仍是完整可玩关卡，而不是游戏音乐。
- **English summary:** Learned accompaniment relations among tile “voices” scaffold the composition of complete Mario levels.

### 50. Online Level Generation in Super Mario Bros via Learning Constructive Primitives

- **Year / venue:** 2016, IEEE Conference on Computational Intelligence and Games; expanded online in 2017 and in IEEE Transactions on Games 10(2), 2018.
- **Scope and task/method:** `levels`; learns short constructive primitives through active designer feedback, composes them online into quality-controlled Mario levels, and in the journal extension adapts generated difficulty from live player performance.
- **Evaluation:** compares generators over 100-level sets, maps ten expressive ranges of 100 levels each, and reports about 0.057 seconds to construct a 200×15 level.
- **Primary sources:** [conference DOI](https://doi.org/10.1109/CIG.2016.7860397), [institutional author manuscript](https://pure.manchester.ac.uk/ws/files/37088685/ieee_cig2016.pdf), [journal DOI](https://doi.org/10.1109/TCIAIG.2017.2740210), [author project and downloads](https://staff.cs.manchester.ac.uk/~shipa/mario.html).
- **Open status:** **Partial, legacy demos.** Executable online/adaptive generators and tutorials remain downloadable. The source archive is password-restricted to non-commercial use, and no experiment data, trained primitive package, or maintained build was verified.
- **Scope decision:** the 2016 online generator and 2018 adaptive expansion are one constructive-primitives family; adaptation changes generated geometry rather than optimizing a Mario-playing policy.
- **中文说明:** 系统从设计师反馈学习构造原语，实时组合 Mario 关卡并在扩展版中动态适配难度；历史可执行 demo 尚存，但源码受密码和非商业用途限制。
- **English summary:** Learned constructive primitives support fast online Mario generation and later real-time difficulty adaptation, with only legacy demos still openly downloadable.

### 51. Autoencoder and Evolutionary Algorithm for Level Generation in Lode Runner

- **Year / venue:** 2019, IEEE Conference on Games.
- **Scope and task/method:** `levels`; decodes 16-dimensional AE/VAE latent vectors into Lode Runner layouts, then applies patch crossover and latent mutation to evolve connected maps in which A* can collect all gold.
- **Evaluation:** augments 150 source levels to 300 training examples, samples 10,000 decoder candidates, and analyses 330 evolved levels. The VAE and AE have mean corpus similarity of 25.36% and 27.05% respectively; A* is a feasibility evaluator, not the research product.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2019.8848076), [official conference PDF](https://ieee-cog.org/2019/papers/paper_232.pdf), [author-associated repository](https://github.com/StarryBar/level-generation-for-lode-runner), [detailed artifact audit](pcg-96-99-primary-sources.md).
- **Open status:** **Partial, legacy/unlicensed.** Notebooks, A*, visualizations, and source data are public, but no license, dependency lock, checkpoints, seeds, results, or tests are present; the visible notebook uses ten iterations while the paper reports 150 generations.
- **Scope decision:** the system emits new Lode Runner maps and uses search only to evaluate/repair them; it is independent of the earlier Mario proof of concept in *Autoencoders for Level Generation, Repair, and Recognition*.
- **中文说明:** AE/VAE 先解码 Lode Runner 布局，再以进化和 A* 修复为连通、可收集全部黄金的关卡；作者关联仓库存在但无法精确复现实验。
- **English summary:** Latent autoencoder samples are evolved into connected, gold-collectible Lode Runner levels, with a useful but incomplete legacy code/data release.

### 52. Generating Game Levels for Multiple Distinct Games with a Common Latent Space

- **Year / venue:** 2020, AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE), volume 16(1), pp. 109–115.
- **Scope and task/method:** `levels`; a branched DCGAN maps one 128-dimensional latent vector through shared layers and four game-specific branches to aligned 16×16 Boulderdash, Link, Zelda, and Roguelike levels.
- **Evaluation:** trains on 5,000 aligned four-game groups. On 50 outputs per game, solvability is 70%, 52%, 54%, and 40% respectively; path-distance distributions quantify cross-game correspondence and Levenshtein distances quantify within-game action novelty.
- **Primary sources:** [canonical AIIDE DOI](https://doi.org/10.1609/aiide.v16i1.7485), [official article](https://ojs.aaai.org/index.php/AIIDE/article/view/7485), [official PDF](https://ojs.aaai.org/index.php/AIIDE/article/download/7485/7346), [detailed artifact audit](pcg-96-99-primary-sources.md).
- **Open status:** **Closed.** No first-party implementation, aligned training set, model, checkpoints, generated corpus, or evaluation package was identified.
- **Scope decision:** automated GVGAI agents only check generated-level solvability. The separate DOI `10.1609/aiide.v15i1.7418` serves a byte-identical copy of the canonical 2020 PDF and is not counted again.
- **中文说明:** Branched GAN 从同一潜向量生成四款游戏中玩法对齐的完整关卡；重复 DOI 指向完全相同 PDF，只保留规范的 2020 记录。
- **English summary:** A shared latent trunk and four output branches generate corresponding playable layouts for four distinct grid games.

### 53. Learning to Generate Levels From Nothing

- **Year / venue:** arXiv precursor in 2020; IEEE Conference on Games, 2021.
- **Scope and task/method:** `levels`; a Generative Playing Network co-trains a Zelda level generator and player from no human levels, adapting generated difficulty toward the player's learning frontier; a semi-supervised condition uses five authored levels.
- **Evaluation:** trains for 50 million frames in a 12×16×14 representation and analyses displayed playable samples, convergence, and human simplicity. The target of approximately 50% player wins is a training objective, not a held-out generated-level success rate.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/COG52621.2021.9619131), [arXiv](https://arxiv.org/abs/2002.05259), [MIT-licensed author repository](https://github.com/pbontrager/GenerativePlayingNetworks), [detailed artifact audit](pcg-96-99-primary-sources.md).
- **Open status:** **Partial.** The generator, player, training loop, environment wrappers, and paper configuration are public, but no checkpoints, result bundle, tests, release tag, container, or complete dependency lock was verified.
- **Scope decision:** the player supplies the curriculum signal for generation; unlike PCGRL, the generator does not edit tiles as an RL policy, so this is a distinct self-supervised generation family.
- **中文说明:** GPN 在没有人工关卡的条件下协同学习 Zelda 玩家和生成器，玩家只为生成器提供学习前沿信号；公开代码完整度尚不足以复现论文结果。
- **English summary:** A co-evolving player supplies the learning signal for a Zelda generator trained from no authored levels, with a partial MIT-licensed implementation.

### 54. Mutation Models: Learning to Generate Levels by Imitating Evolution

- **Year / venue:** 2022, International Conference on the Foundations of Digital Games.
- **Scope and task/method:** `levels`; a CNN learns successful mutations from evolutionary trajectories and iteratively edits 50/50 random 14×14 binary maps into connected mazes without evaluating fitness at inference.
- **Evaluation:** the assisted two-epoch model reaches 99.67% success and 86.83% descriptor diversity over 100 outputs, averaging 18.21 edit sweeps and 0.6612 seconds versus evolution's 12.6957 seconds. Diversity is the fraction with a distinct `(longest path, empty tiles)` pair.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/3555858.3563267), [arXiv](https://arxiv.org/abs/2206.05497), [author repository](https://github.com/amidos2006/ImitatingEvolution), [detailed artifact audit](pcg-96-99-primary-sources.md).
- **Open status:** **Partial, unlicensed.** Author code covers evolutionary data construction, training, inference, games, and configurations, but omits a license, trained models, trajectory datasets, result bundle, tests, and an exact locked environment; visible configuration has drifted from the paper.
- **Scope decision:** evolution produces demonstrations during training and the learned mutation model produces new maze levels; no agent-control or maze-playing policy is trained.
- **中文说明:** 模型模仿进化中的成功 mutation，以约 20 倍速度把随机二值图修复为连通迷宫；代码公开但没有许可证、模型、轨迹数据或精确复现配置。
- **English summary:** A learned mutation operator imitates evolutionary repair to generate connected mazes much faster at inference, with an incomplete author code release.

### 55. Compositional Procedural Content Generation

- **Year / venue:** 2012, Third Workshop on Procedural Content Generation in Games.
- **Scope and task/method:** `generator`; a μ+λ evolution strategy searches 17 parameters of an Answer Set Programming file that is itself a reusable generator of complete, well-formed, winnable roguelike dungeons.
- **Evaluation:** averages the first 20 solver outputs per candidate. Reckless and smart A* evaluators approximate challenge and skill differentiation; the shown run uses μ=30, λ=30 and plateaus after roughly 40 generations.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/2538528.2538541), [metageneration audit](pcg-metageneration-primary-sources.md).
- **Open status:** **Closed.** No paper-specific ASP program, outer search, generated-dungeon corpus, seeds, or evaluation harness was verified.
- **Scope decision:** the A* agents evaluate generated dungeons. This is a separate roguelike/ASP system from the interactive Mario method in *A Procedural Procedural Level Generator Generator*, despite their shared metageneration framing.
- **中文说明:** 外层进化搜索 ASP 地牢生成器的参数，内层程序可反复生成受约束且可通关的 roguelike 地牢；A* 只负责评价生成内容。
- **English summary:** Evolution tunes an ASP program into a reusable constrained dungeon generator rather than directly encoding one dungeon.

### 56. A Procedural Procedural Level Generator Generator

- **Year / venue:** 2012, IEEE Conference on Computational Intelligence and Games.
- **Scope and task/method:** `generator`; interactive evolution synthesizes stochastic Mario level generators made of roughly 14–24 parameterized drawing agents, while a human selects parents through cloud, sample-level, playable, and simulation views.
- **Evaluation:** reports informal designer self-evaluation, qualitative within/between-generator diversity, ten-level A* playability estimates, an offline three-level/100-generation initializer, and speed tests over 100 random generators × 100 levels; it is not a controlled user study.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2012.6374174), [institutional record](https://www.um.edu.mt/library/oar/handle/123456789/29696), [institutional full text](https://www.um.edu.mt/library/oar/bitstream/123456789/29696/1/A_procedural_procedural_level_generator_generator.pdf), [author repository](https://github.com/ManuelKers/PPLGG), [metageneration audit](pcg-metageneration-primary-sources.md).
- **Open status:** **Partial, legacy/unlicensed.** Java source is public, but the README is empty and no license, tagged release, build guide, seed database, result corpus, or reproduction script was verified.
- **Scope decision:** the Mario A* agent estimates the playability of sampled levels; the research output is the reusable generator population, not a game-playing policy.
- **中文说明:** PPLGG 通过交互进化合成多个绘制智能体组成的 Mario 关卡生成器；公开 Java 源码是无许可证、无构建说明的历史快照。
- **English summary:** Users interactively evolve reusable agent-based Mario generators while A* only estimates the playability of their samples.

### 57. Marahel: A Language for Constructive Level Generation

- **Year / venue:** 2017, AIIDE Experimental AI in Games workshop.
- **Scope and task/method:** `generator language`; declares entities, regions, neighborhoods, and sequential explorers whose conditions/actions form compact stochastic generators for 2-D tile maps.
- **Evaluation:** implements five hand-authored generators and maps their expressive ranges along empty-space percentage, isolated elements, and cell-wise entropy.
- **Primary sources:** [AIIDE DOI](https://doi.org/10.1609/aiide.v13i2.12970), [official paper](https://ojs.aaai.org/index.php/AIIDE/article/download/12970/12818), [author implementation](https://github.com/amidos2006/marahel), [metageneration audit](pcg-metageneration-primary-sources.md).
- **Open status:** **Open implementation with a license caveat.** The language runtime, documentation, compiled browser library, and examples are public, but no software license was detected.
- **Scope decision:** humans author the 2017 scripts; *Multi-Objective Level Generator Generation with Marahel* later searches the language automatically. They are connected predecessors, not two publication versions of one method.
- **中文说明:** Marahel 让人用 explorer、neighborhood、条件和动作编写紧凑的构造式关卡生成器，为后续自动搜索生成器程序提供表示语言。
- **English summary:** Marahel is a public constructive-generator language and the explicit representation predecessor to later evolutionary metageneration.

### 58. Optimising Level Generators for General Video Game AI

- **Year / venue:** 2019, IEEE Conference on Games.
- **Scope and task/method:** `generator`; introduces parameterized GVGAI constructive generators and a genetic Meta Generator that searches their parameters for Butterflies, Freeway, and The Snowman.
- **Evaluation:** compares the Meta Generator with random and constructive baselines using composite generated-level fitness derived from AI playtesting; results are game-dependent and are reported as comparable or better, not uniformly dominant.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2019.8847961), [institutional record](https://cris.maastrichtuniversity.nl/en/publications/optimising-level-generators-for-general-video-game-ai/), [institutional full text](https://cris.maastrichtuniversity.nl/files/95969450/Winands_2019_Optimising_level_generators_for_general.pdf), [GPL GVGAI framework](https://github.com/GAIGResearch/GVGAI), [metageneration audit](pcg-metageneration-primary-sources.md).
- **Open status:** **Closed for the paper-specific method.** The upstream GVGAI framework is public, but no paper-identified Meta Generator, parameter sets, generated levels, logs, or evaluation data was verified.
- **Scope decision:** AI agents supply a generated-level fitness. The paper's focused Meta Generator is distinct from the broad mixed framework in *General Video Game AI: A Multitrack Framework for Evaluating Agents, Games, and Content Generation Algorithms* and from playing-agent tracks.
- **中文说明:** Meta Generator 在三款 GVGAI 游戏上搜索构造式生成器参数；AI 试玩只构成生成关卡的复合适应度，论文特定实现未找到。
- **English summary:** Genetic search optimizes reusable GVGAI level generators from playtest-derived content fitness rather than optimizing a player.

### 59. Multi-Objective Level Generator Generation with Marahel

- **Year / venue:** 2020, Foundations of Digital Games PCG Workshop; arXiv v2 and the ACM record are one publication family.
- **Scope and task/method:** `generator`; NSGA-II and grammatical evolution map 102-integer chromosomes to compact Marahel programs that generate Binary, Zelda, and Sokoban maps.
- **Evaluation:** uses population 500 for 2,000 generations and averages each candidate over 50 maps, comparing final Pareto fronts with 500 random generators. Most component objectives improve, but the restricted language produces trade-offs and Zelda/Sokoban scripts often rely on favorable random initialization.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/3402942.3409606), [arXiv](https://arxiv.org/abs/2005.08368), [experiment repository](https://github.com/amidos2006/marahel-evolution), [Marahel framework](https://github.com/amidos2006/marahel), [metageneration audit](pcg-metageneration-primary-sources.md).
- **Open status:** **Open research snapshot with license and packaging caveats.** Central search/evaluation code and best scripts/chromosomes are public, but there is no detected license, README, dependency manifest, tagged release, or turnkey command.
- **Scope decision:** solvers and pathfinding score sampled maps. This is automatic generator-program synthesis, not a version of the human-authored Marahel language paper.
- **中文说明:** 多目标进化把整数染色体翻译成 Binary、Zelda 与 Sokoban 的 Marahel 生成器程序；核心实验快照公开但缺许可证和复现封装。
- **English summary:** Multiobjective evolution searches Marahel programs that are themselves reusable generators across three tile-map domains.

### 60. Evolutionary Wave Function Collapse

- **Year / venue:** 2026, accepted short paper at IEEE Conference on Games; arXiv posted 2026-07-02.
- **Scope and task/method:** `generator`; evolves a 4×4 tile example whose 2×2 patterns let WFC stochastically generate 8×8 connectivity mazes or 16×16 Zelda layouts.
- **Evaluation:** evolution and random search each receive 1,000 genotype evaluations (population 10 × 100 generations). Evolution improves mazes clearly and Zelda modestly; exact global entity/progression constraints remain difficult, and each genotype is evaluated from only one stochastic output.
- **Primary sources:** [arXiv record](https://arxiv.org/abs/2607.02082), [full text](https://arxiv.org/pdf/2607.02082), [metageneration audit](pcg-metageneration-primary-sources.md).
- **Open status:** **Closed.** No paper-specific evolutionary code, genotype set, generated corpus, run logs, or experiment data was verified.
- **Scope decision:** this paper explicitly evolves WFC examples as game-level generators and evaluates their output in two domains; its contribution is generation rather than generic WFC analysis.
- **中文说明:** 进化搜索可充当 WFC 生成器的微型样例，在迷宫上提升明显、Zelda 全局约束上提升有限；尚无论文特定工件。
- **English summary:** Evolution searches tiny WFC examples as reusable game-level generators, with stronger results on local maze structure than global Zelda constraints.

### 61. A Comparative Evaluation of Procedural Level Generators in the Mario AI Framework

- **Year / venue:** 2014, Foundations of Digital Games.
- **Scope and task/method:** `levels` benchmark; ports seven Mario generator families and original Super Mario Bros. levels into a shared framework and contributes two pattern-based measures alongside four existing expressive-range metrics.
- **Evaluation:** compares output distributions, parameter effects, controllability, compression distance, and metric correlations, establishing a common quantitative baseline rather than ranking playing agents.
- **Primary sources:** [archived official FDG paper](https://web.archive.org/web/20180921071717id_/http%3A%2F%2Ffdg2014.org%2Fpapers%2Ffdg2014_paper_14.pdf), [archived author project page](https://web.archive.org/web/20220122165324id_/http%3A%2F%2Fsokath.com%2Ffdg2014_pcg_evaluation%2F).
- **Open status:** **Closed, archived landing page only.** The paper and landing page survive, but the linked `platform_level_metrics.zip` was not archived and no runnable code/level package was verified.
- **Scope decision:** the evaluated objects are level generators and their generated corpora; the paper explicitly positions the framework as a baseline for future generators and metrics.
- **中文说明:** 论文首次在统一 Mario 框架中量化比较七类生成器与原版关卡，并加入两项模式指标；历史代码/关卡压缩包已经不可用。
- **English summary:** A shared Mario framework compares seven generator families with six expressivity measures and provides a historical generator-evaluation baseline.

### 62. The 2017 AIBIRDS Level Generation Competition

- **Year / venue:** competition held in 2017; article published online in 2018 and in IEEE Transactions on Games, 2019.
- **Scope and task/method:** `levels` competition; Science Birds generators receive input constraints and must emit stable, solvable physics levels within a time limit.
- **Evaluation:** five submissions pass automatic structure/validity checks. Eleven judging panels score Fun, Creativity, and balanced Difficulty; excessive similarity may be penalized, but diversity is not a fourth separately reported score. Agents/solvers only test generated levels.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TG.2018.2854896), [author manuscript](https://matthewstephenson.info/papers/The%202017%20AIBIRDS%20Level%20Generation%20Competition.pdf), [archived official results](https://web.archive.org/web/20210121085841id_/http://www.aibirds.org/level-generation-competition/2017-results.html), [winning IratusAves/MSG generator](https://github.com/stepmat/IratusAves), [Science Birds runtime](https://github.com/lucasnfe/science-birds).
- **Open status:** **Partial, GPL winning-generator release.** IratusAves/MSG publishes the winning generator, examples, Science Birds builds, and a GPL-3.0 license. The exact five submissions, task inputs, selected outputs, judge-level data, and removed agent-performance/stability-analysis features are not packaged together.
- **Scope decision:** this is explicitly a level-generation competition; it is independent of later ChatGPT4PCG Science Birds competitions and is not an Angry Birds-playing benchmark.
- **中文说明:** AIBIRDS 2017 要求五个参赛生成器在约束和时间内产生稳定、可解的物理关卡，再由 11 个评审小组从趣味、创造性和难度评价；GPL 获胜生成器已公开。
- **English summary:** A generation-only Science Birds competition combines automatic validity constraints with three judging categories, and its winning generator is publicly released under GPL-3.0.

### 63. Procedural Level Generation for Sokoban via Deep Learning: An Experimental Study

- **Year / venue:** journal DOI registered in 2022; IEEE Transactions on Games, 2023.
- **Scope and task/method:** `levels` benchmark study; reimplements bootstrapped conditional neural generators, controllable/uncontrollable PCGRL, and Generative Playing Networks on one Sokoban task.
- **Evaluation:** compares generation quality, diversity, controllability, and control confusion under a common experimental protocol, treating players/solvers only as generated-level evaluators or generator-training components.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/TG.2022.3175795), [official TechRxiv preprint](https://doi.org/10.36227/techrxiv.16640095.v3).
- **Open status:** **Closed.** No official unified implementation, trained-model set, generated corpus, seed manifest, or evaluation package was verified; the availability of individual upstream methods is not a release of this comparison.
- **Scope decision:** this is a benchmark-like cross-method study of level generators rather than a paper about learning to solve Sokoban, so it stays within the generation-only boundary.
- **中文说明:** 论文把多类深度 Sokoban 生成器放进统一协议，比较质量、多样性、可控性和 control confusion；求解只服务于生成评价。
- **English summary:** A unified Sokoban study compares several deep level-generation families across output quality, diversity, and controllability rather than playing skill.

### 64. Evolving Mario Levels in the Latent Space of a Deep Convolutional GAN

- **Year / venue:** 2018, GECCO.
- **Scope:** `levels`
- **Generated content:** Super Mario Bros. tile levels.
- **Method:** a DCGAN learns a level latent space from VGLC; CMA-ES and novelty/quality-diversity search optimize latent vectors for desired level properties.
- **Evaluation:** generated-level playability plus objective properties and latent-space diversity/coverage under evolutionary search.
- **中文说明:** MarioGAN 先学习关卡潜空间，再在潜空间里进化可玩性或设计属性，奠定了“GAN + 搜索”的路线。
- **English summary:** MarioGAN evolves vectors in a learned GAN latent space to produce playable and diverse Mario levels.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/3205455.3205517), [official experiment repository](https://github.com/icaros-usc/MarioGAN-LSI), [VGLC data](https://github.com/TheVGLC/TheVGLC)
- **Open status:** **Open.** Author-maintained code and the public training corpus are available.

### 65. TOAD-GAN: Coherent Style Level Generation from a Single Example

- **Year / venue:** 2020, AIIDE.
- **Scope:** `levels`
- **Generated content:** tile-based levels matching the style and spatial scale of one example level.
- **Method:** a multi-scale generative adversarial network learns tile patterns from a single training level and composes new coherent maps.
- **Evaluation:** tile-pattern/style similarity, diversity, and domain-specific playability across several game level types.
- **中文说明:** TOAD-GAN 只需一个样例就能学习多尺度关卡风格，特别适合 PCG 常见的小数据场景。
- **English summary:** A multi-scale GAN learns from one level and generates coherent, stylistically related tile maps.
- **Primary sources:** [AIIDE proceedings](https://doi.org/10.1609/aiide.v16i1.7401), [arXiv](https://arxiv.org/abs/2008.01531), [official code](https://github.com/Mawiszus/TOAD-GAN)
- **Open status:** **Open.** Official training/generation code and examples are public.

### 66. PCGRL: Procedural Content Generation via Reinforcement Learning

- **Year / venue:** 2020, AIIDE.
- **Scope:** `levels`
- **Generated content:** levels for binary maps, Zelda-like dungeons, Sokoban, and other tile domains.
- **Method:** the RL policy is the **generator**: it edits tiles under narrow, turtle, or wide observation/action representations and receives content-quality rewards.
- **Evaluation:** training efficiency, validity/quality, diversity, and representation-dependent behaviour across multiple domains.
- **中文说明:** PCGRL 把造关卡建模成强化学习环境；这里的 RL 策略负责放砖块，不是负责通关。
- **English summary:** PCGRL trains an RL policy to edit tiles into valid levels and compares several generation representations.
- **Primary sources:** [AIIDE proceedings](https://doi.org/10.1609/aiide.v16i1.7416), [official environment/code](https://github.com/amidos2006/gym-pcgrl)
- **Open status:** **Open.** Environments, representations, metrics, and training code are public.

### 67. Learning Controllable Content Generators

- **Year / venue:** 2021, IEEE CoG.
- **Scope:** `levels`
- **Generated content:** diverse tile levels targeted to designer-specified content-property values.
- **Method:** makes PCGRL generators goal-aware by conditioning observations and rewards on distance to a requested heuristic target.
- **Evaluation:** target error/coverage, output diversity, and quality relative to goal-unaware generators across multiple domains.
- **中文说明:** 这项工作把 PCGRL 从“生成一个高分关卡”推进到“按设计师指定属性生成不同关卡”。
- **English summary:** Goal-conditioned PCGRL produces diverse levels while steering designer-selected quantitative properties.
- **Primary sources:** [arXiv](https://arxiv.org/abs/2105.02993), [IEEE DOI](https://doi.org/10.1109/COG52621.2021.9619159)
- **Open status:** **Partial.** The paper is public and builds on open PCGRL, but no separately packaged official experiment release was located.

### 68. Talakat: Bullet Hell Generation through Constrained MAP-Elites

- **Year / venue:** 2018, GECCO workshop/preprint.
- **Scope:** `levels`
- **Generated content:** executable bullet-hell attack scripts/patterns.
- **Method:** a domain language defines spawners; constrained MAP-Elites separates infeasible and feasible candidates while illuminating behaviour dimensions.
- **Evaluation:** playability/survival constraints, archive coverage, and diversity over bullet-pattern behaviour descriptors.
- **中文说明:** Talakat 用带约束的 MAP-Elites 生成弹幕脚本，在保证可玩的同时系统覆盖不同弹幕风格。
- **English summary:** Constrained MAP-Elites fills a diverse archive of playable bullet-hell patterns expressed in a generator language.
- **Primary sources:** [arXiv](https://arxiv.org/abs/1806.04718), [official project/code](https://github.com/amidos2006/Talakat)
- **Open status:** **Open.** The domain runtime and generation code are author-released.

### 69. Generating Levels That Teach Mechanics

- **Year / venue:** 2018, FDG.
- **Scope:** `levels`
- **Generated content:** small Mario levels designed to teach a particular action or mechanic.
- **Method:** evolution searches for levels beatable by a full A* agent but not by deliberately impaired variants that cannot perform or perceive the target mechanic.
- **Evaluation:** differential solvability between the full and restricted agents operationalizes whether a level requires the intended skill.
- **中文说明:** 它用“完整代理能过、不会某机制的代理过不了”作为目标，自动生成会教玩家机制的教程关。
- **English summary:** Tutorial levels are evolved so that success specifically depends on the mechanic they are intended to teach.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/3235765.3235820), [arXiv](https://arxiv.org/abs/1807.06734)
- **Open status:** **Closed.** No official maintained implementation package was located.

### 70. Level Generation Through Large Language Models

- **Year / venue:** 2023, FDG.
- **Scope:** `levels`
- **Generated content:** Sokoban levels represented as text grids.
- **Method:** language models are fine-tuned/autoregressively trained on level strings; experiments vary dataset size and test preliminary property control.
- **Evaluation:** functional/solvable level rate and scaling with training-set size, plus initial controllability experiments.
- **中文说明:** 论文把 Sokoban 地图当作语言序列，验证 LLM 能生成可解关卡且效果随数据量明显提升。
- **English summary:** Language models generate Sokoban grids, with solvability improving sharply as the level dataset grows.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/3582437.3587211), [arXiv](https://arxiv.org/abs/2302.05817)
- **Open status:** **Closed.** The paper/protocol is public, but no complete official training/evaluation package was located.

### 71. MarioGPT: Open-Ended Text2Level Generation through Large Language Models

- **Year / venue:** 2023, NeurIPS.
- **Scope:** `levels`
- **Generated content:** Super Mario Bros. levels conditioned on natural-language prompts.
- **Method:** a GPT-2 level model is steered by a frozen text encoder and discriminator/classifier guidance to connect descriptions with tile layouts.
- **Evaluation:** prompt–level attribute alignment, novelty/diversity, and playability/solvability analyses.
- **中文说明:** MarioGPT 提供了典型的 text-to-level 任务：用“很多管道、少量敌人”等自然语言控制 Mario 地图。
- **English summary:** MarioGPT maps free-form textual level descriptions to diverse and playable Mario tile layouts.
- **Primary sources:** [arXiv](https://arxiv.org/abs/2302.05981), [official code/models](https://github.com/shyamsn97/mario-gpt)
- **Open status:** **Open.** Training/inference code and model artifacts are author-released.

### 72. Super Mario as a String: Platformer Level Generation Via LSTMs

- **Year / venue:** 2016, DiGRA/FDG workshop publication; player-tailored extension at the AIIDE Experimental AI in Games workshop.
- **Scope:** `levels`
- **Generated content:** Super Mario Bros. tile levels learned from human-authored levels; the extension learns player-specific styles from gameplay videos.
- **Method:** serializes 2D levels as character sequences and trains LSTMs under several representations; the extension trains four individual models and one combined-player model from observation traces.
- **Evaluation:** compares representations in a human-level-derived feature space, then samples 4,000 levels from each of the five tailored models (20,000 total) for feature-space analysis.
- **中文说明:** 该版本族把二维 Mario 地图序列化为字符串；扩展版又从四名玩家的视频轨迹训练个人模型和组合模型，直接生成玩家定制关卡。
- **English summary:** LSTMs learn string encodings of Mario maps, with a follow-up conditioning the learned style on observed individual or combined player traces.
- **Primary sources:** [official proceedings DOI](https://doi.org/10.26503/dl.v2016i1.752), [arXiv](https://arxiv.org/abs/1603.00930), [player-tailored extension](https://doi.org/10.1609/aiide.v12i2.12895), [five tailored generated-level corpora](https://tinyurl.com/SMB-from-Video), [original SMBRNN generated-level corpus](https://tinyurl.com/SMBRNN).
- **Open status:** **Partial, legacy outputs only.** The generated-level corpora remain downloadable, but no generator, trained model, video-processing pipeline, training code, or evaluation package was verified.

### 73. DOOM Level Generation Using Generative Adversarial Networks

- **Year / venue:** 2018, IEEE Games, Entertainment, and Media Conference (GEM).
- **Scope:** `levels`
- **Generated content:** DOOM level layouts including occupied space, height, walls, and placed game objects.
- **Method:** compares a plain image GAN with a topology-conditioned GAN trained on extracted structural features from human maps.
- **Evaluation:** topological and distributional similarity to human-authored levels, plus qualitative inspection of generated layouts.
- **中文说明:** 这是把 GAN 从二维瓷砖关卡扩展到带高度、墙体和物件拓扑的第一人称射击地图的早期工作。
- **English summary:** Image- and topology-conditioned GANs learn structural features of human DOOM maps and synthesize new layouts.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/GEM.2018.8516539), [arXiv](https://arxiv.org/abs/1804.09154), [official author code/data](https://github.com/edoardogiacomello/DoomGAN)
- **Open status:** **Open.** The first author publishes preprocessing, models, generated data, and experiment code.

### 74. PCGPT: Procedural Content Generation via Transformers

- **Year / venue:** 2023, arXiv preprint.
- **Scope and task/method:** `levels`; a return-conditioned causal transformer learns from offline PCGRL trajectories and iteratively predicts Sokoban items and positions.
- **Evaluation:** success rate and edit-step behaviour over 10,000 random initial maps, with diversity/complexity analysis and PCGRL comparisons.
- **Official artifacts:** [paper](https://arxiv.org/abs/2310.02405).
- **Open status:** **Closed.** The paper says its 3,000-map offline dataset is public but supplies no working location; no author code, data, checkpoint, or evaluator was verified.
- **中文说明:** PCGPT 把造 Sokoban 关卡视为离线轨迹建模，但“数据公开”的文字声明没有对应可取得链接，因此不能标开放。
- **English summary:** PCGPT generates Sokoban edits from offline PCGRL trajectories with a causal transformer, but its claimed public dataset could not be located.

### 75. Using Unconditional Diffusion Models in Level Generation for Super Mario Bros

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

### 76. ChatGPT4PCG Competition

- **Year / venue:** 2023, IEEE CoG.
- **Scope and task/method:** `levels` benchmark; single reusable single-turn prompt for letter-shaped Science Birds levels.
- **Evaluation:** stability/similarity; preliminary 150-level experiment (5 prompts ×3 letters ×10), distinct from proposed 26-letter competition protocol.
- **Primary sources:** [paper](https://arxiv.org/abs/2303.15662), [full text, §III and experiments](https://arxiv.org/html/2303.15662), [official site](https://chatgpt4pcg.github.io/), [code](https://github.com/orgs/chatgpt4pcg/repositories).
- **Open status:** **Open** official evaluation tools. The materially revised 2024 protocol is separately #112.

### 77. Procedural Level Generation in Educational Games From Natural Language Instruction

- **Year / venue:** 2024, IEEE Transactions on Games.
- **Scope and task/method:** `levels`; natural-language instructional goals drive educational-game level generation and learned candidate selection.
- **Evaluation:** instruction alignment and level quality under alternative generation/selection settings.
- **Official artifacts:** [IEEE DOI](https://doi.org/10.1109/TG.2024.3392670).
- **Open status:** **Closed.** No official task set, code, trained model, generated corpus, or evaluator release was verified.
- **中文说明:** 该工作直接从教学语言要求生成教育游戏关卡，不是完整教育游戏生成，但属于明确的自然语言条件关卡 PCG。
- **English summary:** Natural-language learning goals condition the generation and selection of educational-game levels, without a public reproduction package.

### 78. Improving Conditional Level Generation Using Automated Validation in Match-3 Games

- **Year / venue:** 2024, IEEE Transactions on Games.
- **Scope and task/method:** `levels`; a cVAE is conditioned on board size, symmetry, and bot-estimated move difficulty, with automated post-generation validation.
- **Evaluation:** validity, size/difficulty condition accuracy, plagiarism/novelty, tile-distribution style fidelity, and diversity.
- **Official artifacts:** [IEEE DOI](https://doi.org/10.1109/TG.2024.3440214), [arXiv](https://arxiv.org/abs/2409.06349).
- **Open status:** **Closed.** The industrial level data, scripted bot, model implementation, and evaluator are not officially released.
- **中文说明:** 论文把“需要多少步通关”的 bot 统计作为条件，提升 Match-3 关卡有效率，但数据与验证器并未开放。
- **English summary:** Automated play statistics condition and validate Match-3 layout generation, though the proprietary data and pipeline are closed.

### 79. Making New Connections: LLMs as Puzzle Generators

- **Year / venue:** 2024, AIIDE.
- **Scope and task/method:** `puzzles`; Tree of Thoughts prompting generates complete 16-word Connections puzzles, including seeded and deliberately misleading false groups.
- **Evaluation:** a human study compares challenge, enjoyment, creativity, and overall quality with published New York Times puzzles.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2407.11240), [AIIDE DOI](https://doi.org/10.1609/aiide.v20i1.31869), [author repository with prompts and puzzle corpora](https://github.com/TimMerino1710/making-new-connections).
- **Open status:** **Partial.** Prompts plus generated and published puzzle JSON are public, but the full orchestration and user-study/evaluation package are absent.
- **中文说明:** 这篇论文研究的是“出 Connections 谜题”而不是解谜；作者公开了提示和谜题语料，但没有完整实验流水线。
- **English summary:** LLMs generate complete Connections puzzles that humans compare with published puzzles; prompts and corpora are public, not the full study.

### 80. Moonshine: Distilling Game Content Generators into Steerable Generative Models

- **Year / venue:** arXiv 2024; AAAI 2025.
- **Scope and task/method:** `levels`; Brogue's constructive generator produces dungeon maps, an LLM labels them, and text-conditioned diffusion/feed-forward models distil the generator.
- **Evaluation:** map variety, text/map accuracy, quality, connectivity, CLIP alignment, and human assessment against the constructive source.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2408.09594), [AAAI DOI](https://doi.org/10.1609/aaai.v39i13.33571), [official dungeon map-description dataset](https://huggingface.co/datasets/DolphinNie/dungeon-dataset).
- **Open status:** **Partial.** The train/validation/test map-description archives are downloadable, but source code, checkpoints, prompts, and the complete evaluator are not.
- **中文说明:** Moonshine 用传统生成器造海量地图，再用 LLM 补文本标签，最终学习可用自然语言控制的 text-to-map 模型。
- **English summary:** Moonshine distils a black-box dungeon generator into steerable text-to-map models; only the synthetic dataset is released.

### 81. PCGRL+: Scaling, Control and Generalization in Reinforcement Learning Level Generators

- **Year / venue:** 2024, IEEE Conference on Games.
- **Scope and task/method:** `levels`; JAX/GPU parallelization scales PCGRL training and adds randomized map sizes, frozen pinpoints, and OOD-size evaluation.
- **Evaluation:** environment throughput, billion-step training behaviour, controllability, representation/observation effects, and generalization to larger unseen maps.
- **Official artifacts:** [paper](https://arxiv.org/abs/2408.12525), [author PCGRL-JAX repository](https://github.com/smearle/pcgrl-jax).
- **Open status:** **Open.** Apache-2.0 environments, models, training, sweeps, evaluation, controls, and larger-map scripts are public.
- **中文说明:** PCGRL+ 把 PCGRL 完整迁移到 JAX/GPU，并把研究重点扩展到尺寸、固定关键点与超出训练尺度的泛化。
- **English summary:** PCGRL+ makes RL level generation GPU-scalable and tests controllability and out-of-distribution map-size generalization.

### 82. PCGRLLM

- **Year / venue:** arXiv2025; IEEE Transactions on Games2026.
- **Scope and task/method:** `levels`; LLM-generated story-conditioned PCGRL rewards, self-alignment, and an outer loop of feedback from trained policies' generated content.
- **Evaluation:** enemy-encounter instruction accuracy, key-door-dependent playability via pathfinding, feedback/reasoning ablations and human-designed rewards. Not measured human enjoyment.
- **Primary sources:** [full text, architecture/experiment scenarios/AppendixB](https://arxiv.org/html/2502.10906), [IEEE DOI](https://doi.org/10.1109/TG.2026.3695197), [official implementation](https://github.com/bic4907/pcgrl-llm).
- **Open status:** **Open** training/evaluation implementation. ChatPCG2024 is a distinct standalone character-parameter tuning predecessor, not counted; see the [hold/exclusion evidence](pcg-coverage-expansion-2026-09-05.md).

### 83. Word2Minecraft: Generating 3D Game Levels through Large Language Models

- **Year / venue:** 2025, arXiv preprint.
- **Scope and task/method:** `levels`; structured stories are converted into Minecraft levels with scaled spatial layouts, goals, obstacles, and gameplay constraints.
- **Evaluation:** structural metrics plus human ratings of story coherence, aesthetics, objectives, map enjoyment, and model comparisons.
- **Official artifacts:** [paper](https://arxiv.org/abs/2503.16536), [official code/examples branch](https://github.com/JMZ-kk/Word2Minecraft/tree/word2mc_v0).
- **Open status:** **Open, API/environment-dependent.** Apache-2.0 generation and play code plus examples are public; an LLM API and Minecraft tooling are external.
- **中文说明:** Word2Minecraft 从故事中的主角目标、反派挑战和环境设置构造带玩法约束的三维 Minecraft 关卡。
- **English summary:** Word2Minecraft turns structured narratives into spatially coherent, goal-bearing Minecraft levels through an open API-dependent pipeline.

### 84. IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation

- **Year / venue:** 2025, IEEE Conference on Games.
- **Scope and task/method:** `levels`; task-specific sentence embeddings condition a PCGRL policy directly on natural-language requirements.
- **Evaluation:** controllability over several level properties and generalization to held-out instructions, compared with generic embeddings/baselines.
- **Official artifacts:** [paper](https://arxiv.org/abs/2503.12358), [official code and instruction data](https://github.com/bic4907/language-instructed-pcgrl).
- **Open status:** **Open.** Apache-2.0 instruction splits, data collection, encoders, environments, training, and evaluation commands are public.
- **中文说明:** IPCGRL 让关卡生成策略直接理解自然语言属性要求，并专门测量对未见指令的泛化能力。
- **English summary:** IPCGRL learns instruction embeddings that let an RL content generator follow and generalize natural-language level constraints.

### 85. Human-Aligned Procedural Level Generation RL via Text-Level-Sketch Shared Representation

- **Year / venue:** arXiv 2025; IEEE Transactions on Games 2026.
- **Scope and task/method:** `levels`; quadruple contrastive learning aligns text, level states, sketches, and human/AI styles, then an embedding-similarity reward guides PCGRL.
- **Evaluation:** quantitative controllability and human-likeness metrics plus human evaluation of cross-modal intent alignment.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2508.09860), [IEEE DOI](https://doi.org/10.1109/TG.2026.3713793), [official code and dataset](https://github.com/bic4907/VIPCGRL).
- **Open status:** **Open.** Apache-2.0 text/level/sketch data, encoders, style translation, policy training, and evaluation scripts are public.
- **中文说明:** VIPCGRL 不只接受文本，还把关卡图和草图映射到共享空间，以更接近人类设计意图的奖励训练生成策略。
- **English summary:** VIPCGRL aligns text, levels, and sketches in one representation and rewards an RL generator for matching human intent.

### 86. A Database-Driven Framework for 3D Level Generation with LLMs

- **Year / venue:** 2025, AIIDE.
- **Scope and task/method:** `levels`; LLM-assisted offline construction of room, facility, and mechanic databases supports multi-floor assembly, constrained placement, progression, and two-stage navigation repair.
- **Evaluation:** diversity, topological order, spatial-constraint satisfaction, connectivity/navigability, and parameterized gameplay pacing.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2508.18533), [AIIDE DOI](https://doi.org/10.1609/aiide.v21i1.36840).
- **Open status:** **Closed.** No official database, pipeline implementation, generated level set, or evaluator was verified.
- **中文说明:** 该框架把三维关卡拆成可复用的房间、设施和机制数据库，并在装配后专门修复多层导航。
- **English summary:** Reusable architectural and mechanic databases drive multi-floor 3D level assembly and navigation repair, but no artifacts are released.

### 87. Zero-shot 3D Map Generation with LLM Agents

- **Year / venue:** 2025, arXiv preprint.
- **Scope and task/method:** `levels`; an Actor maps natural-language intent to opaque PCG-tool parameters and a Critic iteratively checks tool names, ranges, ordering, alignment, and completeness.
- **Evaluation:** a new instruction-following benchmark compares structural validity, preference alignment, and dual-agent gains with single-agent baselines.
- **Official artifacts:** [paper](https://arxiv.org/abs/2512.10501).
- **Open status:** **Closed.** No author-linked code, benchmark cases, map outputs, or evaluator was verified. An exact-title GitHub recreation is not counted because it is not linked to the paper or authors.
- **中文说明:** 论文让双代理零样本配置三维 PCG 工具，但网上同名复刻没有作者身份链，不能当作官方开源。
- **English summary:** Actor–Critic agents configure 3D PCG tools from language, but the reported benchmark and pipeline have no verified official release.

### 88. From Generation to Gameplay: Authoring Race Tracks With Repulsive Curves

- **Year / venue:** 2025, IEEE Transactions on Games.
- **Scope and task/method:** `levels`; repulsive-curve energies optimize editable closed centerlines that are converted into drivable race-track geometry.
- **Evaluation:** geometric quality and smoothness, runtime/editability, and actual gameplay/driving suitability.
- **Official artifacts:** [IEEE DOI](https://doi.org/10.1109/TG.2025.3561107).
- **Open status:** **Closed.** No official curve-authoring implementation, track corpus, playable build, or evaluator was verified.
- **中文说明:** 这篇论文不仅生成曲线，还把它们做成能驾驶的赛道并评价 gameplay，因此属于关卡生成而非赛车代理。
- **English summary:** Repulsive curves are transformed into editable, drivable race tracks and evaluated through geometry and gameplay, with no public package.

### 89. STRUM: End-to-End Generation of Playable Rhythm-Game Charts

- **Year / venue:** 2026, arXiv preprint.
- **Scope and task/method:** `playable-content`; source separation, onset/pitch models, ASR, and spectral rules convert raw audio into multi-instrument Clone Hero/YARG MIDI charts at four difficulties.
- **Evaluation:** per-instrument onset precision/recall/F1, 30-song screened benchmark, confusion analysis, timing study, and component ablations.
- **Official artifacts:** [paper](https://arxiv.org/abs/2605.12135), [official code and benchmark manifest](https://github.com/opria123/strum), [official model weights](https://huggingface.co/opria123/strum).
- **Open status:** **Open.** The generation pipeline, training/evaluation scripts, benchmark results/manifest, and approximately 6 GB of checkpoints are public; source songs remain separately licensed.
- **中文说明:** STRUM 从一首原始录音直接生成决定玩法节奏的多乐器谱面，代码、权重和 benchmark manifest 都已发布。
- **English summary:** STRUM openly converts raw songs into playable multi-instrument rhythm-game charts and releases code, weights, and benchmark metadata.

### 90. Multiverse: Language-Conditioned Multi-Game Level Blending

- **Year / venue:** 2026, arXiv preprint.
- **Scope and task/method:** `levels`; a shared text/level latent representation with multi-positive contrastive supervision supports blending across Mario, Zelda, Lode Runner, and dungeon domains.
- **Evaluation:** text alignment, blend quality, same-/cross-genre results, interpolation behaviour, and zero-shot compositional prompts.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.26782), [official code and data](https://github.com/bic4907/Multiverse-multigame-pcg).
- **Open status:** **Open.** MIT-licensed datasets, annotations, models, Docker setup, training, inference, and text-blend evaluation are public.
- **中文说明:** Multiverse 把四种游戏关卡放进共享表示，用自然语言指定跨游戏结构混合，并支持组合提示的零样本生成。
- **English summary:** Multiverse learns a shared multi-game level space for language-guided blending and zero-shot composition across four domains.

### 91. Representing and Generating Levels Over Time through Playtrace Reconstructive Partitioning

- **Year / venue:** 2026, Foundations of Digital Games.
- **Scope and task/method:** `levels`; a playtrace-derived “cake” representation captures a level over solution time, and PRP samples/reconstructs Sokoban levels from partitions.
- **Evaluation:** validity and solution diversity against six state-of-the-art PCG approaches.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2607.12097), [ACM DOI](https://doi.org/10.1145/3815598.3815619), [paper-linked repository](https://github.com/emily-halina/PRP-Sokoban).
- **Open status:** **Closed at the cutoff.** The official repository exists but is empty, contradicting the paper's statement that source/cake representations are there; no runnable code or data can be inspected.
- **中文说明:** PRP 用解题轨迹表达关卡随时间的结构，但截止日论文所链接仓库为空，所以必须按 Closed 标注。
- **English summary:** PRP generates valid Sokoban levels from a playtrace-aware representation, but its linked repository was empty at the cutoff.

### 92. Procedural Content Metageneration via Program Search and Continual Abstraction Discovery

- **Year / venue:** 2026, accepted at IEEE Conference on Games.
- **Scope and task/method:** `generator`; an LLM mutates/crosses complete Python generators while Continual Abstraction Discovery extracts validated reusable helpers during search.
- **Evaluation:** 160 complete 50-generation runs across Sokoban, Zelda, Dangerous Dave, and Lode Runner; final fitness, learned-library adoption/calls, and CAD/API ablations.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.17947), [author project page and four example generators](https://github.com/matt-quant-heads-io/procedural-content-metageneration).
- **Open status:** **Partial demo.** Four executable example generators and explanatory media are public, but the evolutionary search/CAD implementation, 160-run dataset, prompts, and evaluator are absent.
- **中文说明:** 这项工作生成的是“关卡生成器程序”本身；作者只公开了四个结果生成器和展示页，尚未公开完整搜索实验。
- **English summary:** LLM program search evolves generators and discovers reusable abstractions; only example generators and media are public.

### 93. Dance Dance Convolution

- **Year / venue:** 2017; ICML 2017.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `playable-content`; Converts audio into playable DDR step charts through CNN/LSTM onset placement and conditional sequence-based step selection.
- **Evaluation:** Compares placement F-scores/AUC and symbolic-step perplexity/accuracy against regression, MLP, CNN and n-gram baselines on two chart datasets.
- **Primary-source evidence:** pipeline “ingests audio features” and “produces a playable DDR choreography”; running step placement and selection in sequence yields a playable step chart. Evaluates placement by perplexity/AUC/F-score and selection by perplexity/token accuracy on Fraxtil and In The Groove, including non-neural and neural baselines.
- **Primary sources:** [paper](https://arxiv.org/abs/1703.06891), [full text](https://arxiv.org/html/1703.06891).
- **Open status:** **Open, legacy dependencies** — [MIT author repository](https://github.com/chrisdonahue/ddc), dataset preparation, training, inference and scripts; README warns the local demo needs TensorFlow 0.12.1. Music packs are separately downloaded.
- **中文说明:** 用 CNN/LSTM 预测踩点时刻，再以条件序列模型选择箭头动作，将音频转成可玩的 DDR 谱面。 在 Fraxtil 与 In The Groove 数据上比较踩点 F-score/AUC、动作困惑度和准确率，并与回归、MLP、CNN、n-gram 基线对照。
- **English summary:** Converts audio into playable DDR step charts through CNN/LSTM onset placement and conditional sequence-based step selection.

### 94. TaikoNation: Patterning-focused Chart Generation for Rhythm Action Games

- **Year / venue:** 2021; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `playable-content`; Generates playable osu!taiko charts from music with a patterning-focused neural model and chart-format post-processing.
- **Evaluation:** Compares binary rhythm-pattern statistics on 10 held-out songs with DDC and random noise, using corresponding human Taiko/DDR charts; not a human preference study.
- **Primary-source evidence:** prediction averaging and post-processing explicitly convert outputs “back into a playable format.” Generates osu!taiko charts and evaluates human-like patterning against Dance Dance Convolution; comparisons include pattern and note-timing behavior rather than music generation alone.
- **Primary sources:** [paper](https://arxiv.org/abs/2107.12506), [full text](https://arxiv.org/html/2107.12506).
- **Open status:** **Partial, unlicensed** — [author source](https://github.com/emily-halina/TaikoNationV1) includes training code, charts, outputs and TensorFlow checkpoints, but documentation is unfinished and hard-coded input/model paths do not match the released layout.
- **中文说明:** 采用重视音符组合规律的神经模型，从音乐生成 osu!taiko 谱面，并通过后处理导出可玩格式。 对比音符与时刻匹配及类人工谱面模式，检查相对既有自动编舞基线的改进。
- **English summary:** Generates playable osu!taiko charts from music with a patterning-focused neural model and chart-format post-processing.

- **Independent audit:** [primary-source section evidence and limitations](independent-pcg-audit-2026-09-05.md), checked2026-09-05.

### 95. Beat-Aligned Spectrogram-to-Sequence Generation of Rhythm-Game Charts

- **Year / venue:** 2023; ISMIR 2023 late-breaking/demo extended abstract.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `playable-content`; Conditions a Transformer on beat-aligned log-Mel spectrograms, difficulty and preceding chart tokens to generate four-key rhythm charts.
- **Evaluation:** Measures micro-F1 against previous methods and ablates beat alignment, dataset scaling, pretraining and fine-tuning.
- **Primary-source evidence:** section 2 defines four-key osu!mania tap/hold/release charts; section 3 compares micro-F1, data scaling, pretraining/fine-tuning and beat-alignment ablation. Uses 6,781 retained charts/2,004 songs after filtering, not the larger raw collection count.
- **Primary sources:** [paper](https://arxiv.org/abs/2311.13687), [full text](https://arxiv.org/html/2311.13687).
- **Open status:** **Open code; externally hosted weights** — [MIT repository](https://github.com/stet-stet/goct_ismir2023) and [author demos](https://stet-stet.github.io/goct/); README documents preprocessing, train/validation/test lists and a 300 MB model archive on Google Drive. The archive was linked but not downloaded in this pass.
- **中文说明:** 以节拍对齐的声谱、难度和此前谱面 token 为条件，用 Transformer 生成四键音游谱面。 比较 micro-F1，并消融节拍对齐、数据规模、预训练与微调；论文为 ISMIR LBD 扩展摘要。
- **English summary:** Conditions a Transformer on beat-aligned log-Mel spectrograms, difficulty and preceding chart tokens to generate four-key rhythm charts.

### 96. Dance Dance ConvLSTM

- **Year / venue:** 2025; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `playable-content`; Uses ConvLSTM-based onset placement and symbolic-step models to generate DDR/StepMania `.sm` charts from music.
- **Evaluation:** Compares precision/recall/F1 and step/hold accuracy with a reimplemented DDC; separates fixed 0.5 thresholds from oracle per-chart F1-max thresholds, so published predecessor scores are not directly comparable.
- **Primary-source evidence:** full method separately trains step placement and symbolic selection; section 6 evaluates Fraxtil using F1/precision/recall, symbolic accuracy and held-note accuracy. This is a distinct ConvLSTM method, not a new name for the 2017 paper.
- **Primary sources:** [paper](https://arxiv.org/abs/2507.01644), [full text](https://arxiv.org/html/2507.01644).
- **Open status:** **Open** — [author code](https://github.com/miguelomalley/DDCL) provides `.sm` generation, preprocessing and model training; no software license was detected and the full experiment was not reproduced.
- **中文说明:** 用 ConvLSTM 踩点预测与动作序列模型，将音乐转成 DDR/StepMania 的 `.sm` 谱面。 对比踩点 precision/recall/F1、动作与长按准确率，并消融模型设计。
- **English summary:** Uses ConvLSTM-based onset placement and symbolic-step models to generate DDR/StepMania `.sm` charts from music.

- **Independent audit:** [primary-source section evidence and limitations](independent-pcg-audit-2026-09-05.md), checked2026-09-05.

### 97. ITGPT: A Transformer Based Architecture for the Generation of Dance Dance Revolution and In the Groove Charts

- **Year / venue:** 2026; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `playable-content`; Generates DDR/ITG charts through Transformer-based step-placement and step-selection models.
- **Evaluation:** Compares onset performance, symbolic/top-k/hold accuracy and computation with predecessor chart generators and model-size variants.
- **Primary-source evidence:** section 6 compares placement and selection with predecessor models on an expanded Fraxtil collection, including top-k accuracy, held-note accuracy and computation. It is a distinct Transformer follow-up to DDCL.
- **Primary sources:** [paper](https://arxiv.org/abs/2607.14148), [full text](https://arxiv.org/html/2607.14148).
- **Open status:** **Open** — [MIT source](https://github.com/miguelomalley/ITGPT) with training, preprocessing, requirements and `generate_charts.py`; author README links an HF Space and GUI generation release. Music packs remain external inputs.
- **中文说明:** 以 Transformer 分别建模踩点与动作选择，自动生成 DDR/ITG 可玩谱面。 在扩展 Fraxtil 数据上比较踩点、动作/top-k/长按准确率与计算成本，并对模型规模做对照。
- **English summary:** Generates DDR/ITG charts through Transformer-based step-placement and step-selection models.

### 98. Procedural Generation of Initial States of Sokoban

- **Year / venue:** 2019; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `levels`; Generates solvable, difficult Sokoban start states using reverse search guided by pattern-database heuristics, conflicts and novelty.
- **Evaluation:** Compares generated-state hardness across heuristic variants and human-authored xSokoban problems through solver effort and conflict measures.
- **Primary-source evidence:** proposes Beta, a reverse-search generator using pattern-database difficulty and novelty to produce solvable starting arrangements. Section 7 uses 90 xSokoban problems, compares generator heuristics and specialized-solver hardness; it creates new puzzle instances, not just a solver.
- **Primary sources:** [paper](https://arxiv.org/abs/1907.02548), [full text](https://arxiv.org/html/1907.02548).
- **Open status:** **Closed** — no official Beta source or generated experiment package located in inspected full text.
- **中文说明:** 以模式数据库启发式、冲突和新颖性引导反向搜索，生成可解且较难的 Sokoban 初始局面。 基于 90 个 xSokoban 问题比较生成器变体，通过求解开销与冲突指标对照人工谜题。
- **English summary:** Generates solvable, difficult Sokoban start states using reverse search guided by pattern-database heuristics, conflicts and novelty.

### 99. Two-step Constructive Approaches for Dungeon Generation

- **Year / venue:** 2019; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `levels`; Combines three architectural layout creators and three object furnishers into complete MiniDungeons 2 levels.
- **Evaluation:** Measures expressive range and generated-level behavior in simulations with procedural player personas.
- **Primary-source evidence:** MiniDungeons 2 construction first generates floors/walls, then places start, goal, monsters, traps and treasures. Three layout creators combine with three furnishers. Expressivity analysis and procedural-persona simulations evaluate resulting complete game levels.
- **Primary sources:** [paper](https://arxiv.org/abs/1906.04660), [full text](https://arxiv.org/html/1906.04660).
- **Open status:** **Closed** — no paper-specific implementation or fixed experiment release verified.
- **中文说明:** 将三种空间布局生成器与三种对象布置器组合，生成含起终点、敌人、陷阱和奖励的 MiniDungeons 2 关卡。 分析表达范围，并用程序化玩家画像模拟游玩生成关卡。
- **English summary:** Combines three architectural layout creators and three object furnishers into complete MiniDungeons 2 levels.

### 100. Generative Adversarial Network Rooms in Generative Graph Grammar Dungeons for The Legend of Zelda

- **Year / venue:** 2020; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `levels`; Combines GAN-generated Zelda rooms with mission-structured graph grammars and internal repair to form complete playable dungeons.
- **Evaluation:** Thirty participants compare three dungeon conditions; GAN rooms are less organized and more complex, without broad enjoyment superiority.
- **Primary-source evidence:** GAN rooms are assembled with a graph grammar into full dungeons; a repair phase makes them playable. Only 10/30 GAN and 16/30 grammar-only dungeons required repair. User study compares generated dungeons with the original game and grammar-only layouts.
- **Primary sources:** [paper](https://arxiv.org/abs/2001.05065), [full text](https://arxiv.org/html/2001.05065).
- **Open status:** **Open, legacy dependencies** — author [paper-specific MM-NEAT experiment](https://github.com/schrum2/MM-NEAT/tree/master/batch/Experiments-2020-CEC-ZeldaGAN), GAN loader and study/play scripts; old Java/Maven/Python setup and no fresh reproduction.
- **中文说明:** 用 GAN 生成 Zelda 房间，再以任务结构图文法组织并内部修复，得到完整可玩地牢。 通过玩家研究与原版、纯图文法地牢比较乐趣、房间复杂度和挑战。
- **English summary:** Combines GAN-generated Zelda rooms with mission-structured graph grammars and internal repair to form complete playable dungeons.

- **Independent audit:** [primary-source section evidence and limitations](independent-pcg-audit-2026-09-05.md), checked2026-09-05.

### 101. Illuminating Diverse Neural Cellular Automata for Level Generation

- **Year / venue:** 2021 / 2022; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `generator`; Uses CMA-ME quality-diversity search to learn archives of neural cellular automata that iteratively generate maze, Sokoban and Zelda levels.
- **Evaluation:** Compares archive quality/diversity and unseen-seed stability against CPPN generator representations and training variants.
- **Primary-source evidence:** CMA-ME evolves archives of NCA generators for maze, Sokoban and Zelda. Evaluation explicitly compares generator archive quality/diversity, CPPN representations and generalization to unseen seeds; NCA policies output tile maps, not game-playing policies.
- **Primary sources:** [paper](https://arxiv.org/abs/2109.05489), [full text](https://arxiv.org/html/2109.05489).
- **Open status:** **Open, legacy configuration caveats** — [MIT code](https://github.com/smearle/control-pcgrl) explicitly identifies the paper and describes evolution/evaluation commands; README notes outdated instructions and cluster-specific setup.
- **中文说明:** 通过 CMA-ME 质量多样性搜索学习一组神经元胞自动机，迭代生成迷宫、Sokoban 和 Zelda 关卡。 比较生成器档案的质量、多样性及新随机种子上的稳定性，并对照 CPPN 表示与训练设置。
- **English summary:** Uses CMA-ME quality-diversity search to learn archives of neural cellular automata that iteratively generate maze, Sokoban and Zelda levels.

### 102. Path of Destruction: Learning an Iterative Level Generator Using a Small Dataset

- **Year / venue:** 2022; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `levels`; Learns inverse actions from destructive trajectories of a small level set, then iteratively converts random maps into new playable levels.
- **Evaluation:** Measures playability and uniqueness over 10,000 trials per generator across three games and dataset/hyperparameter variants.
- **Primary-source evidence:** destructive mutations generate self-supervised training trajectories; inference starts from random unseen maps and creates playable Zelda, Danger Dave and Sokoban levels. Evaluates each trained generator over 10,000 inference trials, reporting playability and uniqueness. It passes the scope rule because repair is the internal generation mechanism.
- **Primary sources:** [paper](https://arxiv.org/abs/2202.10184), [full text](https://arxiv.org/html/2202.10184).
- **Open status:** **Closed at check** — paper-linked [repository](https://github.com/matt-quant-heads-io/path_of_destruction) returned GitHub API 404 on 2026-09-05; do not infer openness from the paper's footnote.
- **中文说明:** 从少量关卡的破坏轨迹学习逆向动作，再从随机地图迭代生成新可玩关卡。 每个生成器运行 10,000 次，在三个游戏和不同数据量/超参数下统计可玩率与唯一性。
- **English summary:** Learns inverse actions from destructive trajectories of a small level set, then iteratively converts random maps into new playable levels.

### 103. Controllable Path of Destruction

- **Year / venue:** 2023; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `levels`; Conditions destruction-trained iterative dungeon generators on designer-selected path and enemy-distance properties.
- **Evaluation:** Measures dungeon playability, duplicate/diversity behavior and target controllability; excludes its separate Lego-asset experiment.
- **Primary-source evidence:** adds conditional inputs to destruction/repair trajectories. The in-scope task is a complete dungeon with one player, key and door, connected paths and target properties. Reports 78.86 ± 4.95% playable output and about 24.42% diversity. Lego cars are outside this record's scope.
- **Primary sources:** [paper](https://arxiv.org/abs/2305.18553), [full text](https://arxiv.org/html/2305.18553).
- **Open status:** **Closed** — no distinct working official implementation/evaluation package verified.
- **中文说明:** 为破坏轨迹训练的迭代地牢生成器加入路径长度、敌人距离等设计条件。 检查地牢可玩率、多样性/重复率和目标可控性；不计其独立 Lego 资产实验。
- **English summary:** Conditions destruction-trained iterative dungeon generators on designer-selected path and enemy-distance properties.

### 104. Start Small: Training Controllable Game Level Generators without Training Data by Learning at Multiple Sizes

- **Year / venue:** 2022 / 2023; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `levels`; Trains controllable autoregressive GFlowNet level generators through a small-to-large size curriculum without authored training levels or shaped rewards.
- **Evaluation:** Measures solvability, diversity, target control, speed and unseen-size generation for Sokoban, Zelda and Danger Dave.
- **Primary-source evidence:** recurrent autoregressive GFlowNets learn first at small sizes, then larger sizes, without an authored dataset or shaped reward. Generates Sokoban, Zelda and Danger Dave; compares playability, diversity, control and unseen sizes, reporting 9× training/generation speed versus a controllable RL comparator for Sokoban.
- **Primary sources:** [paper](https://arxiv.org/abs/2209.15052), [full text](https://arxiv.org/html/2209.15052).
- **Open status:** **Open** — [MIT code](https://github.com/yahiaetman/ms-level-gen) includes environment, game analyzers, method implementations, experiment configurations, generation and analysis commands; README links pretrained weights and generated samples.
- **Targeted release-document check, 2026-09-08:** [pinned README and dependency file](experiment-entry-points-2026-09-08.md) establish the `sokosolve` dependency, post-training condition-model fitting, lower-bound rather than exact dependency pins, and playable-subset selection of displayed examples. Authored-data-free does not mean solver-free. No training, inference or weight download was performed.
- **中文说明:** 使用由小到大的尺寸课程训练可控自回归 GFlowNet，无需人工训练关卡或塑形奖励。 在 Sokoban、Zelda、Danger Dave 上比较可解性、多样性、可控性、速度与未见尺寸泛化。
- **English summary:** Trains controllable autoregressive GFlowNet level generators through a small-to-large size curriculum without authored training levels or shaped rewards.

### 105. Illuminating the Space of Dungeon Maps, Locked-door Missions and Enemy Placement Through MAP-Elites

- **Year / venue:** 2022; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `levels`; Evolves complete dungeon layouts, key/locked-door missions and enemy placements with a feasibility-preserving tree representation and MAP-Elites.
- **Evaluation:** Computational archive analysis plus 96 players, 74 complete survey respondents and 121 level plays; exploratory feedback, not a controlled superiority result.
- **Primary-source evidence:** a tree encoding guarantees key/locked-door mission feasibility; MAP-Elites generates room layouts with enemies. Full text says volunteers played a game prototype with generated levels. Computational and player-feedback experiments evaluate generation, not just representation.
- **Primary sources:** [paper](https://arxiv.org/abs/2202.09301), [full text](https://arxiv.org/html/2202.09301).
- **Open status:** **Closed** — no official experiment package verified.
- **中文说明:** 结合保证任务可行性的树表示与 MAP-Elites，生成房间、钥匙锁门任务和敌人配置。 计算分析搜索档案收敛，并让玩家在加载生成地牢的原型中提供反馈。
- **English summary:** Evolves complete dungeon layouts, key/locked-door missions and enemy placements with a feasibility-preserving tree representation and MAP-Elites.

- **Independent audit:** [primary-source section evidence and limitations](independent-pcg-audit-2026-09-05.md), checked2026-09-05.

### 106. High Dimensional Procedural Content Generation

- **Year / venue:** 2026; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `levels`; Generates platform levels in joint geometry/layer or geometry/time spaces, then grounds validated plans into playable Unity scenarios.
- **Evaluation:** Compares three algorithms per axis using solver trajectories for reachability, target control, structure, robustness and runtime; Unity demonstrations support human play but are not user studies or joint-mechanic validation.
- **Primary-source evidence:** Direction-Space incorporates layer changes/gravity/world switching; Direction-Time represents moving platforms/obstacles in time-expanded graphs. Methods generate, ground and validate levels; Unity case study states the level is generated directly from the planner and “what you see is exactly what is playable.” Separate-axis experiments, not demonstrated joint multi-mechanic composition.
- **Primary sources:** [paper](https://arxiv.org/abs/2602.18943), [full text](https://arxiv.org/html/2602.18943).
- **Open status:** **Closed** — no author implementation/project release verified in full text.
- **中文说明:** 在几何与层切换或时间的联合空间中生成平台关卡，并将验证过的规划实例化为 Unity 可玩场景。 每个方向比较三种算法及多种尺度，检查可达性、可控性、结构、鲁棒性与耗时；尚未验证多机制联合组合。
- **English summary:** Generates platform levels in joint geometry/layer or geometry/time spaces, then grounds validated plans into playable Unity scenarios.

- **Independent audit:** [primary-source section evidence and limitations](independent-pcg-audit-2026-09-05.md), checked2026-09-05.

### 107. Procedural Generation of First Person Shooter Maps using Map-Elites

- **Year / venue:** 2026; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `levels`; Uses MAP-Elites with sliding boundaries and alternative spatial encodings to evolve FPS deathmatch maps.
- **Evaluation:** Compares four representations on map quality/diversity using topology descriptors and emergent properties from actual game simulations.
- **Primary-source evidence:** MESB evolves playable FPS maps with four encodings, including new Point-Line and Spatial-Layout representations; a Duel/deathmatch environment evaluates emergent gameplay properties. Compares topology and gameplay feature pairs, map quality and diversity.
- **Primary sources:** [paper](https://arxiv.org/abs/2605.30570), [full text](https://arxiv.org/html/2605.30570).
- **Open status:** **Closed for the paper-specific generator at check** — linked [generator repository](https://github.com/SimoDedo/MAPElites_FPS_Maps) returned API 404. A separate underlying runtime does not make the method reproducible.
- **中文说明:** 用滑动边界 MAP-Elites 和不同空间编码演化 FPS 死亡竞赛地图。 结合拓扑描述符与实际游戏模拟产生的行为指标，比较四种表示的地图质量和多样性。
- **English summary:** Uses MAP-Elites with sliding boundaries and alternative spatial encodings to evolve FPS deathmatch maps.

### 108. Solvable Sokoban Without a Solver via Diffusion

- **Year / venue:** 2026; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `levels`; Trains masked discrete diffusion on Sokoban tile completion and samples new puzzles without solver-based training supervision.
- **Evaluation:** Uses a solver after generation to assess solvability, and studies pattern-distribution match, memorization, temperature and one-wall repairs.
- **Primary-source evidence:** masked discrete diffusion learns tile completion from 450,000 Boxoban puzzles without solver rewards/labels; evaluation generates 5,000 puzzles per sampled checkpoint and runs a solver. Final reported solvability 77.4%; also measures local-pattern JSD, memorization and temperature. “Without a solver” describes training, not evaluation or filtering in the demo.
- **Primary sources:** [paper](https://arxiv.org/abs/2608.15958), [full text](https://arxiv.org/html/2608.15958).
- **Open status:** **Partial, unlicensed inference/model release** — [official repository](https://github.com/sinabaghal/SokobanPlayground) has `model.pt`, generation and browser-play export; README's `play.py` checks solvability before exporting. No full training/experiment reproduction package verified.
- **中文说明:** 以 Sokoban 格子补全训练掩码离散扩散模型，无需求解器提供训练奖励或可解标签。 生成后用求解器测可解率，并分析局部模式分布、记忆、温度与单墙修复；试玩脚本也会筛选可解实例。
- **English summary:** Trains masked discrete diffusion on Sokoban tile completion and samples new puzzles without solver-based training supervision.

### 109. All Stories Are One Story: Emotional Arc Guided Procedural Game Level Generation

- **Year / venue:** 2025; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `levels`; Converts emotional-arc-conditioned story graphs into connected Unity ARPG rooms with instantiated entities, gameplay attributes and generated sprites.
- **Evaluation:** A 16-person exploratory study compares engagement, coherence and emotional perception, supplemented by interviews and sentiment analysis.
- **Primary-source evidence:** branching story nodes map to complete ARPG dungeon rooms with enemies/props, gameplay attributes and navigation. Outputs playable Unity WebGL games. Sixteen participants compare emotional-arc and non-arc experiences; ratings, interviews and sentiment analysis evaluate generated play. Unlike narrative-only JSON work, a playable pipeline is explicit.
- **Primary sources:** [paper](https://arxiv.org/abs/2508.02132), [full text](https://arxiv.org/html/2508.02132).
- **Open status:** **Closed** — no official generator/build/study-data release verified in inspected paper.
- **中文说明:** 把情感弧条件下的故事图转成连通 Unity ARPG 房间，实例化角色、敌人、玩法属性与图像资源。 用 16 人探索性研究比较参与感、连贯性及情感感知，并结合访谈和情绪分析。
- **English summary:** Converts emotional-arc-conditioned story graphs into connected Unity ARPG rooms with instantiated entities, gameplay attributes and generated sprites.

### 110. Video Game Level Design as a Multi-Agent Reinforcement Learning Problem

- **Year / venue:** 2025; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Scope and task/method:** `levels`; Trains multiple cooperating PCGRL editing agents to generate maze and dungeon levels while sharing costly global quality evaluations.
- **Evaluation:** Compares generator reward, editing budgets and generalization to unseen rectangular/square maps over multiple training and evaluation seeds.
- **Primary-source evidence:** multiple turtle agents jointly edit maps in binary-maze and dungeon domains, reducing global reward calculations per editing action. Dungeons require one player/key/door and relevant paths. Evaluates ten training seeds with fifty episodes per condition, square/rectangular OOD sizes and differing board-scan budgets. This is a distinct multi-agent follow-up, not the existing single-agent scaling paper.
- **Primary sources:** [paper](https://arxiv.org/abs/2510.04862), [full text](https://arxiv.org/html/2510.04862).
- **Open status:** **Open shared implementation, snapshot caveat** — [Apache-2.0 author code](https://github.com/smearle/pcgrl-jax), training/sweeps/evaluation instructions; exact paper snapshot and all results were not checked.
- **中文说明:** 训练多个协同编辑地图的 PCGRL 智能体，共享昂贵的全局质量计算，生成迷宫和地牢。 跨多组训练与评测种子比较生成质量、编辑预算及未见矩形/方形地图泛化。
- **English summary:** Trains multiple cooperating PCGRL editing agents to generate maze and dungeon levels while sharing costly global quality evaluations.

### 111. Level Generation with Quantum Reservoir Computing

- **Year / venue:** 2025; primary paper; publication details and preprint versions in linked source.
- **Verified:** 2026-09-05 (Asia/Shanghai), incremental addition; primary full-text methods/evaluation and author-linked artifact checks.
- **Method:** Simulates quantum-reservoir sequence models on classical computers to generate Mario layouts and playable Roblox obstacle-course sequences.
- **Evaluation:** Studies novelty, broken sequences, temperature and qubit budgets against Markov/random baselines; real quantum hardware and its real-time deployment remain future work.

- **Primary sources:** [paper](https://arxiv.org/abs/2505.13287), [full text](https://arxiv.org/html/2505.13287).
- **Open status:** **Partial** — [Apache-2.0 paper-specific data/notebook](https://github.com/moth-quantum/OpenData/tree/main/Level_Generation_with_Quantum_Reservoir_Computing) includes analysis, but imports missing local `archeo` modules; not a complete runnable QRC training release.

- **Independent audit:** [primary-source section evidence and limitations](independent-pcg-audit-2026-09-05.md), checked2026-09-05.

### 112. The Second ChatGPT4PCG Competition

- **Year / venue:** 2024, IEEE CoG.
- **Scope and task/method:** `levels` competition; Python prompt programs allow multi-turn/control flow for letter-shaped Science Birds levels.
- **Evaluation:** adds within-character diversity, font-trained similarity classifier and function-signature ablations, plus advanced prompting examples.
- **Primary sources:** [paper](https://arxiv.org/abs/2403.02610), [full text](https://arxiv.org/html/2403.02610), [code and raw data](https://github.com/chatgpt4pcg/experiments-2024), [site](https://chatgpt4pcg.github.io/).
- **Open status:** **Open** official generation/evaluation experiment artifacts.
- **Identity:** materially revised submission/scoring protocol from #76, not a duplicate citation.

### 113. A Case Study of Expressively Constrainable Level Design Automation Tools for a Puzzle Game

- **Verified:** 2026-09-05 (Asia/Shanghai); primary-source method, playable-output and evaluation inspection.
- **Authors/year/venue:** Adam M. Smith, Erik Andersen, Michael Mateas, Zoran Popović; FDG 2012. [ACM DOI](https://doi.org/10.1145/2282338.2282370), [author full text](https://adamsmith.as/papers/fdg2012generation.pdf), [author bibliography](https://adamsmith.as/).
- **Scope:** `puzzles`; substantive generation, not only a puzzle solver or editing UI. §5.1 constructs mission DAGs from desired mathematical expressions and piece constraints; §5.2 embeds them into Refraction's spatial board. Explicit quote: “realize a puzzle with sufficient detail to be played in the live game.” §6.4 says the original tools were “integrated ... into a research version of the game”; §6.5 combines ASP mission generation and embedding into a monolithic puzzle generator. Player pieces, fixed sources/targets, beam directions and fractional power form executable Refraction puzzles (§4, Figs1–3).
- **Method:** compares constructive mission generation plus randomized DFS embedding with declarative ASP equivalents; ASP additionally controls mathematical subgraphs, blocker symmetry, compositional balance, beam spacing/crossings. Solving alternative player arrangements is a third tool, not the sole basis for inclusion. The two implementations across three tasks are **one paper**, not six canonical methods.
- **Evaluation:** §7.1 compares code size and **1,000 random-seed runs on fixed inputs derived from one high-complexity example**, not 1,000 independent puzzle specifications or a user study. Mission generation: feed-forward <1ms total versus ASP <1ms search +530ms grounding. Embedding: DFS650ms versus ASP110ms search +630ms grounding. Solver: DFS no solution within one-hour timeout versus ASP350ms search +340ms grounding. Figures3–4/§7.2 show controlled style differences.
- **Negative/limited result:** raw ASP search is faster for embedding, but 110+630=740ms **total** is not faster than DFS650ms on the reported uncached setting. Grounding can be cached only when requirements do not change. Timing is from one fixed-input example on a 2006-era Xeon, not a general speed benchmark. A required reference solution does **not** guarantee all alternative solutions practice the intended concept; that motivates the genuinely distinct 2013 follow-up. No measured educational-learning benefit or human enjoyment claim.
- **Artifacts:** **Closed/unverified** — paper describes Java, AnsProlog and Lua implementations and XML-level utilities; author bibliography links the paper, not a checked generator/experiment archive. Generic ASP tools remain separate.
- **Canonical identity:** different from existing Tanagra, Dormans missions/spaces, and the generic ASP methodology citation attached to Variations Forever. This paper implements and measures full Refraction generation, while the 2013 follow-up changes the generation guarantee.
- **中文说明:** 用构造式/DFS 与 ASP 方法生成任务图并嵌入空间棋盘，形成带数学与风格约束的可玩 Refraction 激光分数谜题。 比较代码量、风格控制及固定示例输入下的 1,000 次随机种子运行；ASP 搜索耗时与 grounding 开销须分开。
- **English summary:** Generates Refraction mission graphs and embeds them as playable laser/fraction puzzles using constructive/DFS and ASP implementations with explicit style constraints. Compares code size, style control and 1,000 seeded runs on fixed example inputs; ASP search-time gains must be separated from grounding overhead.
- **Discovery note:** [further content discovery](further-content-discovery-2026-09-05.md).

### 114. Quantifying over Play: Constraining Undesirable Solutions in Puzzle Design

- **Verified:** 2026-09-05 (Asia/Shanghai); primary-source method, playable-output and evaluation inspection.
- **Authors/year/venue:** Adam M. Smith, Eric Butler, Zoran Popović; FDG 2013, verified against [author bibliography](https://adamsmith.as/) and [complete author manuscript](https://adamsmith.as/papers/fdg2013_shortcuts.pdf). No exact DOI was verified; do not use an unrelated Crossref fuzzy-title result.
- **Scope:** `puzzles`. §5.5 formulates **generation** of a solvable puzzle for which every solution practices the required concept: existential puzzle/reference-solution variables and universal alternative-solution variables. §6 builds an actual Refraction 2 generator, not merely a verifier for existing levels. §6.2 guesses puzzle piece types, positions, ports and source powers; §6.3 translates two design predicates into disjunctive ASP, integrating candidate generation and counterexample feedback.
- **Generation guarantee:** the theory concerns the formalized bounded mechanics and specified concept predicate. It excludes explicitly modeled shortcuts, not every subjective undesirable play experience or every possible implementation bug. The full problem is formulated as NP^NP-complete; the seven-line generic translator alone is not the game-specific ~120-line encoding.
- **Evaluation:** §6.4/Figs3–4 present **four generated examples**, not a large benchmark or player experiment. Total construction-to-first-result times (search subset in parentheses):7.26s(2.12s),18.9s(8.29s),152s(140s),74.2s(67.2s). First two require splitter/combiner use; latter two require a monolithic network spanning all pieces, including a blocker-free case. Reported machine is a 2011-era2.2GHz Corei7, single-threaded construction and eight-thread search.
- **Negative/limited result:** author language is explicitly “promising feasibility results”; examples are selected concept demonstrations without statistical coverage, measured enjoyment or validated player-specific learning. Integrating empirical player models is future work. Complexity guarantees do not imply efficient generation for arbitrary instances.
- **Artifacts:** **Closed/unverified** — source snippets, metasp translator and commands are printed, but no complete official Refraction encoding/build/results package was verified through the paper or author bibliography. Do not call the generic metasp/Potassco links the paper's open generator.
- **Canonical identity:** retain separately from2012: prior work generated a puzzle-and-one-good-solution pair and could admit shortcuts; this paper jointly synthesizes puzzles excluding all modeled bad solutions. Its generator experiments substantiate more than a renamed version or QA-only extension.
- **中文说明:** 将量化约束转换为析取式 ASP，联合生成可解 Refraction 谜题并排除已形式化的捷径解。 用四个概念约束实例及构建/搜索计时展示可行性；不是大样本或玩家研究。
- **English summary:** Jointly synthesizes Refraction puzzles and rules out modeled shortcut solutions through quantified constraints translated into disjunctive ASP. Four concept-constrained generated examples with construction/search timings demonstrate feasibility; no large-sample or human evaluation.
- **Discovery note:** [further content discovery](further-content-discovery-2026-09-05.md).

### 115. Evolving Playable Content for Cut the Rope through a Simulation-Based Approach

- **Year / venue:** AIIDE 2013, pp. 72–78.
- **Primary sources:** [publisher record](https://ojs.aaai.org/index.php/AIIDE/article/view/12690), [DOI](https://doi.org/10.1609/aiide.v9i1.12690), [official PDF](https://ojs.aaai.org/index.php/AIIDE/article/download/12690/12538).
- **Verified:** 2026-09-05 (Asia/Shanghai); primary-source method, playable-output and evaluation inspection.
- **Metadata discrepancy:** the original PDF orders **Mohammad Shaker, Noor Shaker, Julian Togelius**, while current OJS/Crossref metadata orders Noor then Mohammad. Same paper/DOI, not two records. Preserve original-PDF authors in prose if an ordered author list is needed; public rows omit authors.
- **Scope qualification:** §4 calls simulation-based playability testing its main contribution. Crucially, §3 and §5–6 integrate that agent into **Ropossum's grammatical-evolution generator**, evolve from random populations and evaluate newly generated playable outputs. Recommendation is for this integrated generation method, under SCOPE's internal-stage exception, not for the Prolog playing agent as a separate record or for arbitrary evaluation-only use.
- **Playable output:** §2 describes the authors' C#/XNA **Cut The Rope: Play Forever** clone built on modified CRUST physics. Generated candy, OmNom target, ropes, air-cushions, bumpers, bubbles and rockets define actual timed-interaction physics puzzles. Figures1/2/8 show game/clone components and generated levels. This is not a claim of exporting into ZeptoLab's proprietary executable or owning/distributing its reused art.
- **Method:** GE samples level grammars, first checks weighted design constraints, then evaluates simulated solvability with a Prolog rule-based action filter and depth-first search. More informed rules use physics and reachable components; adaptive action-dependent time steps reduce search. §5's fitness combines design penalties and playability; this is new generation, not hand-authored level repair.
- **Evaluation:** §5 experiment setup: 100 runs, maximum 100 generations, population 20; runs stop when a playable level is found. Search caps at 80 actions (~15 sec). §6:4,500 candidate levels,335 pass design-constraint threshold,123 playable levels reported. Do **not** call these 100% solvability, a fixed 200,000 evaluated candidates, or100 unique successful runs: stopping and intermediate outputs change denominators. Mean detection times:29.8±58.3sec for playable versus210.6±167.6sec for unsuccessful tests; mean explored nodes115 versus638. Generated samples in Fig8.
- **Negative/limited result:** only 36% of supplied components were used in solutions, suggesting superfluous design; 72.3% of actions were waiting. Heuristic action restriction and80-action cap mean unsuccessful search is not proof of true unsolvability (explicitly acknowledged in introduction). No player enjoyment study or new education result. Do not compare these timings directly with discrete Refraction generation.
- **Artifacts:** **Closed/unverified** — source implementation described (C#, XNA, JTrolog communicating through files), but no official core-source/reproduction package verified; generic CRUST/JTrolog does not establish method openness. The paper states an accessible authoring UI is ongoing work, not a released complete package.
- **Identity:** directly distinguishes the earlier CIG 2013 **Automatic Generation and Analysis of Physics-Based Puzzle Games** heuristic Ropossum generator. Neither it nor the AIIDE authoring-tool demonstration is counted additionally here; this recommendation concerns the exact simulation-guided paper.
- **中文说明:** 将 Prolog 引导的物理仿真与有界 DFS 嵌入文法进化，生成可玩的 Cut the Rope 克隆版关卡。 4,500 个候选中335个通过设计约束，报告123个可玩产物；仅36%的组件用于解法，有界搜索失败不代表确实无解。
- **English summary:** Integrates Prolog-guided physics simulation and bounded DFS into a grammatical-evolution generator for playable Cut the Rope-clone levels. Reports 4,500 candidates, 335 design-valid and 123 playable outputs; only36% of components were used, and failed bounded search does not prove unsolvability.
- **Discovery note:** [further content discovery](further-content-discovery-2026-09-05.md).

### 116. Evolving Missions to Create Game Spaces

- **Authors/year/venue:** Daniel Karavolos, Antonios Liapis, Georgios N. Yannakakis; IEEE CIG 2016. [DOI](https://doi.org/10.1109/CIG.2016.7860396), [author publication entry](https://antoniosliapis.com/publications.php#karavolos2016evolvingmissions), [author manuscript](https://antoniosliapis.com/papers/evolving_missions_to_create_game_spaces.pdf).
- **Evidence-access caveat:** PDF extraction recovered the methods, tables, results, conclusion and references, but Poppler reported a malformed cross-reference/end-of-stream issue in an embedded content stream. Numeric claims below rely on recovered textual table/section content; no visual pixel-accurate figure review or complete binary-integrity claim is made.
- **Scope:** `levels`/playable mission spaces, not isolated narrative graphs. §III-A/TableI maps nodes to start/end, combat, reward and puzzle actions in Dwarf Quest. §III-D **From Mission Graphs to Levels** specifies graph post-processing and spatial layout solving. §IV-D/Fig6 converts evolved examples into **Dwarf Quest levels** using grammar refinement plus the existing layout solver. Acknowledgments explicitly identify developer access to Dwarf Quest source code. Figure1 anchors the playable game mechanics; generated graphs are not only a story outline.
- **Method:** mutation-only evolutionary search starts from start/end connected by one edge; add/change/delete nodes and edges under constraints,10% elitism and fitness-proportionate selection. Five objectives target shortest path, exploration, alternating node categories, dispersed rewards and balanced rewards. Grammar and layout solving materialize selected graphs, with added empty nodes, triangle breaking and omission of non-neutral degree-one nodes as internal adaptation stages.
- **Evaluation:** §IV: 20 runs ×100 generations ×population 100 per setting, single/combined objectives and a constant-fitness random-selection baseline. TableIII reports objective scores; TableIV topology/node composition; Fig5 uses 2,000 final individuals per objective for expressive range. Summed-objective optimization's best score is 2.8× baseline, but this is a **designed fitness proxy**, not enjoyment or human difficulty.
- **Critical limitation:** §IV explicitly evaluates graphs **before post-processing**. §IV-D/Fig6 and discussion show complex graphs create excessive empty rooms/long corridors, so high graph scores need not mean good final gameplay. Single-objective variation can favor tiny graphs; balanced-reward fitness can be maximized with no safe area around either reward. Fight nodes are underrepresented because random type sampling gives them lower mass. No user study; no published success rate for all final playable exports. Author subjective “interesting” should not be restated as measured player preference.
- **Artifacts:** **Closed/unverified** — author publication entry links paper/BibTeX, not an official generator/experiment archive. Dwarf Quest developer source access by the researchers does not establish public source availability. Existing game, thesis/layout solver and generic GA infrastructure are not a complete release of this method.
- **Identity:** distinct from existing Dormans grammar-based missions/spaces (#31),2015 mixed-initiative authoring work cited by this paper, and later dungeon MAP-Elites. Its new contribution is evolutionary mission representation/objectives with instantiated Dwarf Quest outputs.
- **中文说明:** 按路径、探索和奖励目标进化玩家行动任务图，再经文法细化与空间布局生成 Dwarf Quest 关卡。 每种设置20次运行，与随机选择比较任务图适应度及表达范围；指标在后处理前计算，复杂最终布局可能产生过多空房间。
- **English summary:** Evolves player-action mission graphs under path, exploration and reward objectives, then refines and spatially instantiates them as Dwarf Quest levels. Twenty runs per setting compare graph fitness/expressivity with random selection; metrics precede post-processing, and complex final layouts can contain excessive empty rooms.
- **Discovery note:** [further content discovery](further-content-discovery-2026-09-05.md).

### 117. Playing with Data: Procedural Generation of Adventures from Open Data

- **Identity:** Gabriella A. B. Barros, Antonios Liapis, Julian Togelius; DiGRA/FDG 2016. [DOI](https://doi.org/10.26503/dl.v2016i1.801), [complete author manuscript](https://antoniosliapis.com/papers/playing_with_data.pdf), [author publication list](https://antoniosliapis.com/publications.php).
- **Scope:** playable adventure content in a fixed adventure client. The subsection **“Setting up clues and creating the story flow”** converts linked-data paths into NPCs, books, locations, clues and **access conditions**: a subsequent object becomes accessible after the preceding clue is read. This creates playable progression and unlock dependencies, not merely renamed people or replaced portraits. Vague/false clues have a 50% probability and introduce dead ends. The conclusion describes a working travel/interaction prototype whose objective is to reach the target person.
- **Method:** select real starting/target people, search DBpedia relationships, map intermediate graph nodes to adventure objects and locations, then generate clues and conditions along the path. The generated artifact is an adventure instantiated in the client, not independent invention of every core mechanic.
- **Evaluation:** **RESULTS / Table 2** reports **851 runs**, using distinct random pairs from a 99-person list derived from Time's 100 important people (American GI excluded). There are **819 error-free runs**, **32 runs with errors**, and **827 playable runs**. These last two success counts differ because some errors are noncatastrophic; do not label 819 the playable count or silently discard the distinction. Error categories are no path 10, search error 9, parsing error 12 and other 1.
- **Table 3:** cities 3.82 ± 1.39; buildings 7.86 ± 2.36; NPCs 5.33 ± 2.32; items 4.14 ± 2.36; real-NPC ratio 74% ± 20%; average path length 8.34 ± 2.45, minimum 3, maximum 13. **Figures 2, 5 and 6** and accompanying examples show Einstein→Thatcher / Monroe→Mandela adventures and actual gameplay screenshots.
- **Negative findings:** erroneous DBpedia relations can produce absurd geography, such as New York City being part of South Africa. Visiting every place and speaking to every NPC can circumvent careful deduction; dead ends remain shallow, and subplots/hidden items are not implemented. Human experience evaluation is future work, so the automated yield is not an enjoyment result.
- **Artifacts:** no paper-specific official generator, client build or experiment package was verified in the inspected paper/publication entry. Use **Closed/unverified**.

- **Review date:** 2026-09-08; independent paper record.

### 118. DATA Agent

- **Identity:** Michael Cerny Green, Gabriella A. B. Barros, Antonios Liapis, Julian Togelius; FDG 2018. [DOI](https://doi.org/10.1145/3235765.3235792), [arXiv record](https://arxiv.org/abs/1810.02251), [complete HTML](https://arxiv.org/html/1810.02251).
- **Scope:** **§4.1.3 and §4.2** describe generated murder mysteries with suspect claims, factual contradictions, interrogations, keys and locked buildings. The Java generator and Unity3D client (§4) turn the generated graph into interactive mysteries, rather than leaving it as prose or disconnected narrative JSON.
- **Method:** **§4.2.1 Suspect Selection** evolves groups of three suspects using μ+λ search and cascading elitism: population 50, 500 generations, victim–suspect and suspect–suspect linkage rankings, successive removal of each ranking's bottom half, retaining 25% before mutation repopulates. One suspect is randomly marked culprit. **§4.2.2 Path Generation** builds victim-to-suspect paths with a maximum of four edges/five articles and selected entity types, generating the clue/person/item/location structure.
- **Evaluation:** **§5 User Study** has **30 participants**, each playing two generated cases, Albert Einstein and Britney Spears, in randomized order, with logs and questionnaires. **Table 2** reports interaction ratios. This is an exploratory two-case study, not broad statistical coverage of all possible generated mysteries.
- **Negative findings:** **§6** reports low challenge, substantial neutral responses about fun, and straightforward solutions. Open-data problems include nonsensical/trivial facts, mismatched portraits and treating the German Empire as a city. Only 30 game objects were used versus the predecessor's 135, simplifying the studied experiences. Participants knew the AI/open-data origin, creating a possible attribution bias. Willingness to try another mystery is not measured long-term engagement, and most did not want to replay the same mystery.
- **Artifacts:** no DATA Agent-specific official source/build was verified from the full paper's links. The linked MuseumVILLE repository is another project and must not be attributed to DATA Agent. Use **Closed/unverified**.

- **Review date:** 2026-09-08; independent paper record.

### 119. Video2Game: Real-time, Interactive, Realistic and Browser-Compatible Environment from a Single Video

- **Review date:** 2026-09-08; primary method and gameplay text independently rechecked; artifact file inspection dated 2026-09-05, no execution.
- **Canonical identity:** **Video2Game: Real-time, Interactive, Realistic and Browser-Compatible Environment from a Single Video**, CVPR 2024, pp. 4578–4588. [CVF proceedings](https://openaccess.thecvf.com/content/CVPR2024/html/Xia_Video2Game_Real-time_Interactive_Realistic_and_Browser-Compatible_Environment_from_a_Single_CVPR_2024_paper.html), [arXiv 2404.09833](https://arxiv.org/abs/2404.09833), [full text](https://arxiv.org/html/2404.09833). The preprint and CVPR paper are one record.
- **Decision:** **Include as PCG `playable-content`**, specifically reconstructed playable 3D scenes. Do not count it again under interactive video world models or describe it as synthesizing all game code/rules. It was absent from the public indexes when checked in this pass.
- **EN:** Reconstructs video scenes as neural-textured meshes with object-level collision models, then integrates them into browser-playable environments for navigation, driving and object interaction; scene assembly and gameplay configuration remain partly manual.
- **中文：** 将视频场景重建为带神经纹理和对象级碰撞模型的网格，再集成为支持导航、驾驶及物体交互的浏览器可玩环境；场景装配与玩法配置仍有人工环节。
- **Generated playable output evidence:** §3 describes NeRF reconstruction, neural-texture mesh baking and individual physical entities. §3.4 integrates outputs with Sketchbook/Three.js, a GLSL shader and Cannon.js. The gaming application section describes **executable environments with mesh geometry, materials and rigid-body physics encoded in GLB/texture files**, not just screenshots. Demonstrations include Gardenvase navigation and shooting footballs to knock the vase off its table, plus KITTI-360 running/coin collection, driving and collisions with reconstructed roadside cars. The project has an actual [Gardenvase game entry](https://video2game.github.io/src/garden/index.html) instantiating `new Video2Game.World('build/assets/world.glb')`; merely watching a robot simulation video is not the basis for inclusion.
- **Automation boundary — explicit primary evidence:** §3.3 allows **mass and friction to be set manually or estimated by an LLM**; collision shape is chosen according to object/task. Appendix C states that overlapping boundaries between the 14 KITTI blocks are **manually defined** before mesh assembly. Fracture animation is precomputed. The author [readme.md](https://raw.githubusercontent.com/video2game/video2game/main/readme.md) tells users to **manually configure** screen size, intrinsics, rendering meshes and collision-model paths in `game_dev/src/ts/world/World.ts`; it warns that advanced Cannon.js physical interactions require laborious tasks and recommends Unreal for easier development. Thus this is a reconstruction-to-playable-content pipeline with authored runtime integration, not automatic invention of collecting/shooting/driving mechanics. Its central generator still materially creates the playable environment integrated by the paper, satisfying the scope's playable-content rule.
- **Evaluation:** §4 benchmarks Gardenvase, KITTI-360 and an indoor VR-NeRF scene. Table 1 evaluates novel-view quality and interactive compatibility; geometry/mesh comparisons and component ablations test the reconstruction and baking method. Table 4 measures runtime across hardware/platforms. The reported **over-100 FPS** demonstrations are conventional engine **rendering/simulation rates after offline scene construction**, not neural video generation throughput, and must not be mixed with GameNGen/SANA/Wonder FPS. Game interaction examples are demonstrations, not a standardized gameplay success benchmark. The robot track is separate and not the admission basis.
- **Official artifacts and actual files:** [repository](https://github.com/video2game/video2game), [exact lowercase readme.md](https://raw.githubusercontent.com/video2game/video2game/main/readme.md), [project/game](https://video2game.github.io/), [game source](https://github.com/video2game/video2game/tree/main/game_dev). A recursive official tree response (`truncated: false`) verified `train.py`, `extract_mesh.py`, `baking_pretrain.py`, `baking_pretrain_export.py`, `collision_model_generate.py`, `eval_nerf.py`, `eval_textured_mesh.py`, game TypeScript sources, built JavaScript, GLB worlds/actors and collider classes. Do not misclassify the repo as absent because uppercase `README.md` returns 404.
- **Openness:** **Partial.** The live README marks NeRF, mesh extraction/postprocessing, baking pretraining, collision generation and evaluation released, but **Baking Finetune Module** and **GPT-4 Query** remain unchecked. Public `game_dev` provides an executable engine scaffold with documented manual setup, not a verified one-click reproduction of every paper scene and physics interaction. Full pipeline, asset loading and gameplay were not executed in this audit. The project warns about cross-origin asset-loading issues; no browser-security setting was changed during inspection.

### 120. Procedural Generation of Sokoban Levels

- **Identity and verification:** Joshua Taylor and Ian Parberry, GAMEON-NA 2011, pp. 5–12; checked 2026-09-08. [Author-hosted conference paper](https://ianparberry.com/pubs/GAMEON-NA_METH_03.pdf), [author project](https://ianparberry.com/research/sokoban/), [full evidence and artifact manifest](racing-puzzle-followup-2026-09-08.md). No conference-paper DOI was verified; the differently titled thesis must not supply one.
- **Role/output:** generation method, `puzzles`. Generates new room geometry from overlapping 3×3 templates, brute-force goal placements, and initial states via memory-saving reverse search; exports JSoko-compatible level sets. This is not just a solver or a repair pass on a supplied puzzle.
- **Guarantee and objective:** reversing legal moves from solved states guarantees solvable returned states. The search distance is box lines (consecutive pushes of one box in one direction), not the downstream solver's move count. A timer returns the current best; it does not certify completed global-hardness optimization. Additional heuristic ranking and rotation/reflection deduplication shape the selected output.
- **Evaluation:** Tables 1–3 average ten random samples per size/box setting on an Intel i7 3.2 GHz machine. Dimensions count template blocks: 2×2 means 36 cells. Three boxes on 3×3 blocks average 24.5 h; five boxes on 2×2 blocks average 26 h. JSoko's “move optimal with best pushes” reports solution moves. Reused conditions across tables are not additional independent sample groups.
- **Limits:** exponential offline cost; heuristic difficulty and residual perceptual duplicates. The conclusion explicitly offers no justification for human interest and leaves player testing to future work. Do not import the author site's later 2015 study, equate solver moves with human difficulty, or describe larger cases as real-time generation.
- **Artifacts:** **Partial.** Five actual author level-file responses contain ASCII puzzles. The downloaded [experiment ZIP](https://ianparberry.com/research/sokoban/SokobanPaperData.zip) contains 11 level text files, 11 solver-result logs and one spreadsheet; three logs were read, the spreadsheet was only listed. No core generator source or turnkey build/reproduction package verified. JSoko is third-party playback/solver software, not the authors' generator.
- **Review boundary:** complete original text plus rendered experimental pages independently checked; no generator, solver, game or archived experiment was rerun.
- **中文要点：** 模板构造与反向搜索生成保证可解的 Sokoban 关卡；区分模板块尺寸、箱线目标、下游求解步数与未经验证的人类难度。
- **English summary:** Template construction and reverse search generate solvable Sokoban puzzles, with explicit offline costs and available output/experiment artifacts but no verified core source.
