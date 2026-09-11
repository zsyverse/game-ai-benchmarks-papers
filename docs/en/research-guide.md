# Game Generation Research: Methods, Evaluation, and Reading Routes

[Home](../../README.md) · [中文](../zh-CN/research-guide.md) · [Scope](../../SCOPE.md) · [Coverage evidence](../../research/README.md)

> First prepared **2026-09-05**, with targeted additions on **2026-09-08**, from the existing index and primary-source research. Scores from different tasks are not combined into a universal leaderboard.

## Distinguish the generated artifact

Game generation includes at least three different problems: generating programs and rules for conventional engines, generating playable content under existing mechanics, and learning worlds that evolve with player actions. Their correctness and reproducibility requirements differ; one system can combine several of them.

| Research object | Generated result | Typical controls | Essential checks | Index |
| --- | --- | --- | --- | --- |
| Games, programs and mechanics | Engine projects, code, executable rules/mechanics | Specifications, examples, constraints, iterative feedback | Build, runtime, rule implementation, actual play | [End-to-end](end-to-end.md) |
| Automated design and PCG | Rule systems, levels, maps, dungeons, puzzles, missions, charts | Target properties, spatial/temporal constraints, text, audio, examples | Reachability/solvability, condition satisfaction, diversity, experience | [PCG](pcg.md) |
| Interactive worlds | Continuously generated observations, geometry or state | Stepwise keys, mouse, discrete actions, event instructions | Action response, causal/numerical correctness, memory, latency | [Interactive worlds](interactive-worlds.md) |

For example, [Pharos Night](https://arxiv.org/abs/2608.12216) composes executable card mechanics inside an existing Unity game; [Dance Dance Convolution](https://arxiv.org/abs/1703.06891) converts audio into playable charts; [GameGAN](https://arxiv.org/abs/2005.12126) generates the next game screen from a key press. Classifying them solely by LLM, GAN or diffusion architecture obscures these differences.

## Method families and coverage added

| Family | Representative work | Main capability | Questions to check |
| --- | --- | --- | --- |
| Constraints, grammars, planning and search | Variations Forever, Tanagra, [Sokoban start-state generation](https://arxiv.org/abs/1907.02548), [High Dimensional PCG](https://arxiv.org/abs/2602.18943) | Encode rules, paths, key/door dependencies, time or layer changes into generation | Which properties are guaranteed? Does a valid plan become a playable artifact? |
| Evolution and quality diversity | Ludi, ANGELINA, GAVEL, [dungeon MAP-Elites](https://arxiv.org/abs/2202.09301), [FPS MAP-Elites](https://arxiv.org/abs/2605.30570) | Search for candidates targeting playability, quality or behavioral diversity; guarantees depend on constraints and evaluators | Does agent fitness reflect meaningful play? Does archive diversity imply gameplay diversity? |
| Learning from examples | LSTMs, GANs, Transformers, [diffusion Sokoban](https://arxiv.org/abs/2608.15958) | Learn level/chart styles and sample content | Validity, solvability, memorization, transfer and conditional control |
| Learned editors and local update rules | PCGRL, [NCA](https://arxiv.org/abs/2109.05489), [Path of Destruction](https://arxiv.org/abs/2202.10184), [multi-agent PCGRL](https://arxiv.org/abs/2510.04862) | Learn iterative generation from rewards/constraints or destructed example trajectories; data requirements vary | Editing budget, global reward cost, initial-state distribution and size generalization |
| Controllable distribution sampling | [Start Small / GFlowNet](https://arxiv.org/abs/2209.15052), Moonshine | Attempt to sample diverse candidates conditioned on requested properties | Joint condition satisfaction, conflicting objectives, diversity and unseen combinations |
| Program synthesis and execution feedback | GGDG, GAVEL, ScriptDoctor, AVR-Agent, Play2Code | Produce executable artifacts and improve them using compilation, solving, recordings or playtests | From-scratch generation versus local patches, feedback reliability and matched budgets |
| Workflow instantiation and bounded mechanic composition | [Scenario-based serious-game generation](https://arxiv.org/abs/1911.07380), [Pharos Night](https://arxiv.org/abs/2608.12216) | Instantiate authored workflows or predefined mechanic combinations as executable gameplay | Which rules are designer-authored? What can the generator change? Does the study isolate generation effects? |
| Learned interactive simulation | GameGAN (action labels); [CADDY](https://arxiv.org/abs/2101.12195) (discovered actions); [Playable Environments](https://arxiv.org/abs/2203.01914) (camera/3D control); Genie, GameNGen, [Vid2World](https://arxiv.org/abs/2505.14357), Matrix-Game | Let actions drive a neurally generated world | Actual stepwise interaction, training-world exposure, persistent memory and rules |

These works show related task developments, not a single version lineage or universal replacement by newer methods. Constraints and search remain useful for explicit solvability requirements; neural methods often target style, expressive range and interactive generation. Hybrid systems combine these strengths. The collection pages and [source dossiers](../../research/README.md) document individual claims.

This expansion strengthens rhythm-game coverage: Dance Dance Convolution (2017), TaikoNation (2021), beat-aligned Transformer generation (2023), Dance Dance ConvLSTM (2025), and ITGPT (2026), alongside the existing STRUM. Together they cover step placement, action selection, holds, difficulty conditions and different chart formats. Their output is playable choreography, not general music synthesis.

## Comparing benchmarks

| Benchmark | Generation task | Main evidence | What it does not establish |
| --- | --- | --- | --- |
| [V-GameGym](https://arxiv.org/abs/2509.20136) | Requirements to Pygame projects | Multimodal code, screenshot and gameplay-video scores | High visual scores imply complete rule implementation |
| [GameCraft-Bench](https://arxiv.org/abs/2606.17861) | Briefs to complete Godot games | Build gate, submitted-input replay and mechanic/content/visual scoring | A successful replay covers every reachable failure |
| [ByteSized32](https://aclanthology.org/2023.emnlp-main.830/) | 16 unseen scientific/common-sense tasks to complete Python text games, using 32 references | Three-step bounded runtime crawl, specification/physical fidelity and human winnability | Passing a runtime crawl proves whole-game correctness; an agent failing to win proves unsolvability |
| [Mage](https://arxiv.org/abs/2605.07342) | Scene builders for 26 Unity goal patterns | Compilation, initialization, structure and static mechanism paths | Successful `Awake()` or high static F1 means a player can win |
| [PlaytestArena](https://arxiv.org/abs/2605.28258) | 200 browser-game generation tasks | GUI-agent play and observable rubrics | Automated playtesting is identical to human experience |
| [PCG Benchmark](pcg.md) | Playable content under several fixed mechanics | Task-specific quality, controllability and diversity protocols | Raw scores can be averaged across tasks as general capability |
| [WorldMark](https://arxiv.org/abs/2604.21686) | Shared action programs to generated world trajectories | Control, response latency, stability, memory and visual quality | Correct camera/navigation implies correct complex game rules |
| [WorldRoamBench](https://arxiv.org/abs/2606.31672) | First/third-person generated-world navigation | Action following, visual drift, interaction physics, scene/subject memory | A public leaderboard implies downloadable tasks and evaluators |

Comparisons should identify inputs, generation budgets, sample counts, filters, feedback rounds, judge models and whether failures remain in the denominator. Video-world reports also need resolution, hardware, context length, throughput FPS and action-to-first-frame latency. High throughput does not by itself establish responsive control.

## Five evaluation questions

This is a cross-paper reading framework, not a standard adopted by every paper:

1. **Can it execute?** Can the program build and launch, the rules run, the level load or the video model continue?
2. **Are mechanics correct?** Check inputs, collisions, score, resources, outcomes and events through behavior, not merely code or appearance.
3. **Can play continue?** Check reachability/solvability, interaction stability, and preserved layout/state when revisiting locations.
4. **Is generation controllable?** Check difficulty, style, topology, mechanics or emotional targets, conflicting conditions, repetition and training-data memorization.
5. **Is it worthwhile and affordable?** Look for designed player studies or experience measures together with time, compute, API cost and dependencies.

[Model as a Game](https://arxiv.org/abs/2503.21172) examines numerical and spatial consistency; [Mage](https://arxiv.org/abs/2605.07342) separates compilation/initialization from mechanism alignment; [diffusion Sokoban](https://arxiv.org/abs/2608.15958) requires distinguishing solver-free training from solver-free evaluation or demo filtering. These distinctions materially affect interpretation.

## Qualifications retained after re-audit

- **Task boundaries:** the scenario-based framework instantiates authored linear workflows; Pharos Night composes a predefined mechanic vocabulary. Neither establishes arbitrary whole-game synthesis.
- **Denominators and empty-set scoring:** Mage structural F1 covers runtime-pass outputs only; static paths cover all 858 attempts. Its 0.12 no-schema win-path floor comes from empty-reference matches, not playability.
- **Executable rules are not finished games:** approximately 33,000 designs in the 2023 controllable co-creative study pass simulator feasibility; humans must still complete the actual playable game.
- **Availability is not reproduction:** WorldRoamBench releases benchmark inputs, but a complete evaluator was not verified. Quantum reservoir level generation uses circuit simulation, not demonstrated quantum-hardware advantage.
- **Separate substantive follow-ups:** a shared system brand does not justify folding distinct architectures, training procedures or benchmark editions into one paper. See the [reliability audit](../../research/reliability-audit-2026-09-05.md) for splits and experimental corrections.

## Questions sharpened by further discovery

Newly located papers make several important distinctions more explicit:

- **One intended solution, or every solution meeting the design goal?** [Refraction 2012](https://doi.org/10.1145/2282338.2282370) generates mission graphs and spatial instances; [Quantifying over Play](https://adamsmith.as/papers/fdg2013_shortcuts.pdf) jointly generates puzzles excluding formally specified shortcuts. Its four examples demonstrate feasibility, not efficient solving at arbitrary scales.
- **Runnable, or winnable?** ByteSized32 reflection raises runtime pass from 28.1% to 57.3%, but human winnability only from 30.2% to 37.5%. These cannot be collapsed into one generation-success rate.
- **A good graph, or a good final game?** [Evolving Missions](https://doi.org/10.1109/CIG.2016.7860396) evaluates mission graphs before post-processing, while instantiated layouts can contain excessive empty rooms. Recheck design goals on the final artifact.
- **Guaranteed solvability, or validated human difficulty?** [Taylor–Parberry 2011](https://ianparberry.com/pubs/GAMEON-NA_METH_03.pdf) reverse-generates solvable Sokoban states, but box-line search distance, JSoko solution moves and human difficulty are different quantities. Larger settings average roughly one day; player interest was not validated.
- **Must generated worlds be continuous video?** [Unbounded](https://arxiv.org/abs/2410.18975) uses turn-based language/image generation and character-state updates. Its GPT-4 scores are not directly comparable with camera-trajectory error, engine FPS or deterministic rule correctness.

These are paper-specific comparison leads, not universal field conclusions. See the [further-discovery notes](../../research/README.md) for additions, unresolved candidates and discovery limits.

## September 8 addition: identify the actual automation boundary

[Playing with Data](https://doi.org/10.26503/dl.v2016i1.801) and [DATA Agent](https://arxiv.org/abs/1810.02251) do more than generate prose: linked data becomes accessible places, collectible clues, interrogation facts and locked-door conditions. Incorrect source facts can nevertheless enter the game; yield or playability does not establish puzzle quality or challenge.

[Ludus Ex Machina (ICCC 2014)](https://computationalcreativity.net/iccc2014/wp-content/uploads/2014/06/4.2_Cook.pdf) assembles themes, retrieved assets and stock executable rules into Unity 3D games, relying on a premade rule library with weak rule/zone evolution. [Part II](https://doi.org/10.1109/TCIAIG.2016.2520305) is a distinct follow-up paper that repeats the same game-jam outcomes and adds subjective author curation; it is no longer separately counted as a generation method. [Video2Game](https://arxiv.org/abs/2404.09833) reconstructs geometry, textures and colliders from video and integrates them as playable content through partly manual engine assembly. Ask which parts each pipeline generates and which people decide; neither should be flattened into fully automatic from-scratch game invention.

Correcting the original method's identity does not permit filling evidence gaps across papers. The [three-paper comparison](../../research/angelina-paper-identity-2026-09-08.md) keeps the AISB precursor, ICCC method and Part II contributions separate.

Sonancia's 2015 tension-curve experiments and its 2016 expanded lighting/3D-audio playable demonstrator are evidence from distinct papers; this batch does not combine them into one counted result. See the [integration and remaining gaps](../../research/further-research-integration-2026-09-08.md).

## Choosing an experimental starting point

These recommendations follow official release documentation; they are neither successful reproduction reports nor cross-task rankings. The September 8 check covered version-specific documentation, dependencies and selected code. See the [pinned evidence and experiment reporting checklist](../../research/experiment-entry-points-2026-09-08.md).

| Research objective | Suggested starting point | Resolve before comparing results |
| --- | --- | --- |
| Compare content generators under fixed mechanics | [PCG Benchmark](https://github.com/amidos2006/pcg_benchmark) and its separate [experiment repository](https://github.com/amidos2006/benchmark_experiments) | Fix environment ID, representation, control set, candidate-evaluation budget and batch size; equal iterations need not be fair, and diversity depends on the sample set |
| Controllable generation and size transfer without authored training levels | [Start Small](https://github.com/yahiaetman/ms-level-gen) | A solvability analyzer is still needed; Sokoban depends on `sokosolve`. Build the condition model after training, and do not treat the environment file as an exact dependency lock |
| Complete text-game code and reflection | [ByteSized32](https://github.com/cognitiveailab/BYTESIZED32) | Fix reference/task pairings, API and judge models; update labels when tasks change, and execute generated code in isolation |
| Action-conditioned visual generation with an explicit game domain | [Matrix-Game version 1](https://github.com/SkyworkAI/Matrix-Game/tree/main/Matrix-Game-1) | Authors specify at least 80 GB GPU memory for one 65-frame inference; do not borrow version 2/3 real-time metrics or treat inference release as full training reproduction |

Report raw candidates, executable outputs, winnable outputs, filtered quality, full-batch and valid-subset diversity, human intervention, and separate generation/evaluation time. Keep failed and unresolved cases; solver timeout is not an unsolvability proof. Match inputs, total budgets and judging conditions across models rather than combining paper-reported scores into a leaderboard.

## Reading by research objective

- **Text games and explicit world programs:** start with ByteSized32 specifications, transitions and human winnability; compare task scope with STORY2GAME, IDGE and Distilling Game Code World Model Generation. Separate generating an environment from training its player.
- **Complete-game generation:** compare GameCraft-Bench, Mage and PlaytestArena task/failure definitions, then read GGDG/GAVEL, ScriptDoctor and AVR-Agent/Play2Code for generation and feedback design.
- **Controllable levels or puzzles:** start with PCG Benchmark and a constraint/search method, then compare PCGRL, NCA, Start Small, Path of Destruction and diffusion under the same game and control budget.
- **Interactive worlds:** read GameGAN, CADDY and Playable Environments for actions/state representations, followed by Genie/GameNGen, Vid2World and recent memory-based models; use WorldMark/WorldRoamBench to compare control and long-horizon evaluation.

## Boundaries and remaining gaps

This expands methods and generation benchmarks within the [existing scope](../../SCOPE.md). Isolated assets, generic narrative, NPC policies, agent-playing benchmarks, framework-only proposals and product blogs without papers do not enter the public count. “Game” or “world” in a name is not inclusion evidence.

Discovery used arXiv searches, reference following, author projects and code/model releases. It did not enumerate every conference proceedings year or rerun the methods. Historical PCG available only in proceedings or thesis libraries, unpublished commercial systems, and ambiguous general-scene versus game-world candidates remain possible gaps. [Coverage notes](../../research/README.md) retain unresolved and exclusion evidence rather than filling these gaps by inference.

The original full-verification date remains **2026-09-04**; **2026-09-05** and **2026-09-08** identify explicitly marked additions and reviews, not fresh verification of the whole corpus or every artifact. Accessible official artifacts do not establish successful reproduction; paper-reported results were not independently rerun.
