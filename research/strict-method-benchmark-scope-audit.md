# Strict Method / Benchmark Scope Audit

> Audit cutoff: **2026-09-04 (Asia/Shanghai)**  
> First-pass surface: 198 public English rows and their Chinese mirrors: 50
> end-to-end, 115 PCG, and 33 interactive-world rows.
> Second-pass surface: all 151 canonical English records left after the first
> cleanup: 39 end-to-end, 89 PCG, and 23 interactive-world records.

## Decision rule

`KEEP` requires the paper's central contribution to be either:

1. a method that directly produces a playable game, executable game code or
   project, executable rules or mechanics, a playable level/map/task/chart, or
   a player-controllable generated game world; or
2. a benchmark that explicitly defines and empirically evaluates one of those
   generation tasks.

`REMOVE` covers dataset/corpus-only work, surveys/taxonomies/position papers,
general runtime or infrastructure, metric-only or non-benchmark comparison
studies, authoring interfaces without a substantive automatic generator,
standalone repair/QA, asset-only work, NPC/player agents, policy-oriented world
models, and loosely related material. Artifact availability does not determine
scope. `REMOVE-DUPLICATE` means the paper is in scope but must have only one
canonical public row.

The audit was performed from primary sources recorded in the then-broad
dossiers. After the decisions were applied, the current dossiers were pruned to
accepted records only:
[end-to-end](end-to-end-generation-sources.md),
[PCG](pcg-automated-design-sources.md), and
[interactive worlds](interactive-world-generation-sources.md). Identifiers in
the exact-action lists refer to the **pre-cleanup public row number** for
end-to-end, the former public `Source #` for PCG, and the pre-cleanup public row
order for interactive worlds; old line references likewise describe that
pre-cleanup snapshot. The original files remain recoverable in Git history.
The three current source dossiers are renumbered one-to-one with current public
IDs, while removal determinations are preserved in this audit.

## First-pass result: 198 candidates to 151 canonical records

| Action | End-to-end | PCG | Interactive worlds | Total |
| --- | ---: | ---: | ---: | ---: |
| Strict topical `REMOVE` | 7 | 21 | 11 | **39** |
| `REMOVE-DUPLICATE` / merge | 3 | 5 | 0 | **8** |
| Move between sections | 1 out | 0 | 1 in | 0 |
| Canonical qualifying records after cleanup | 39 | 89 | 23 | **151** |

Thus the pre-cleanup headline count of 198 was inflated by 39 out-of-scope rows
and 8 duplicate rows. The first-pass result was **151 canonical records**. A
second, narrower paper-by-paper check of those 151 records appears at the end
of this file and supersedes that count for the current public collection.

## Exact removal and consolidation lists

### End-to-end

Strict topical removals (English and Chinese tables have matching row numbers):

- `#7`, `docs/*/end-to-end.md:L19` — **VeriGame / GameGen-Verifier**:
  verifier accuracy/efficiency is the research product, not a generation method
  or generation benchmark.
- `#35`, `L59` — **Grounding Machine Creativity in Game Design Knowledge
  Representations**: negative probing of existing model/IR combinations; it
  proposes neither a generator nor a formal benchmark.
- `#43`, `L74` — **Fly, Fail, Fix**: standalone tuning/repair of one fixed
  Flappy Bird configuration.
- `#44`, `L75` — **Repairing General Game Descriptions**: standalone minimal
  repair of existing faulty GDL.
- `#45`, `L76` — **AutoBG**: produces natural-language rulebooks, not executable
  rules, code, or a playable build.
- `#48`, `L86` — **Agentic Game Development as a Verifiable Trajectory Data
  Engine**: its main contribution is a trajectory/world-model research agenda
  and asset-edit tasks, not game generation.
- `#49`, `L87` — **Lottery and Sprint Arcade**: voice-driven editing of fields
  in a fixed game is an HCI/configuration study, not automatic generation.

Duplicate rows to merge:

- Remove `#19` (`L36`) into canonical `#8` (`L20`): both are the OpenGame paper,
  arXiv `2604.18394`.
- Remove `#22` (`L39`) into canonical `#9` (`L21`): both are the
  PlaytestArena/Play2Code paper, arXiv `2605.28258`.
- Remove `#24` (`L41`) into canonical `#10` (`L22`): both are the
  PlayGen-20/AutoUE paper, arXiv `2603.07106`.

Move `#50` **Playable Game Generation** (`L95`) to interactive worlds. It is a
real-time, player-controlled learned engine, but it does not emit executable
source code or a conventional game project.

### PCG

Strict topical removals from `docs/*/pcg.md`:

- `#9` (`L144`) — survey/architecture only.
- `#11` (`L134`) — Ludii is a language/runtime and corpus, not a generator.
- `#18` (`L39`) — VGLC is a corpus without a fixed generation benchmark.
- `#31` (`L136`) — generic WFC analysis, not a game-specific playable-content
  generator or formal benchmark.
- `#32` (`L126`) — Minecraft voxel structures are component/asset generation,
  without playable-level or mechanics generation.
- `#33` (`L137`) — settlement-component benchmark, not a benchmark for a game,
  playable level/map/task, or executable mechanics.
- `#34` (`L145`) — survey/taxonomy only.
- `#35` (`L146`) — survey/taxonomy only.
- `#46` (`L107`) — standalone level repair.
- `#49` (`L110`) — standalone stability repair of existing Angry Birds levels.
- `#55` (`L116`) — generates non-executable trading-card items and artwork,
  not a playable game or executable rules.
- `#58` (`L151`) — evaluation survey only.
- `#59` (`L152`) — survey only.
- `#60` (`L153`) — survey only.
- `#89` (`L65`) — comparison of training-data effects on existing generator
  families, with no new generation method or formal benchmark.
- `#107` (`L147`) — metric vocabulary/framework only.
- `#108` (`L148`) — empirical metric-validity study only.
- `#109` (`L149`) — design-metric framework only.
- `#110` (`L150`) — evaluation methodology only.
- `#112` (`L138`) — inspection and parameter-tuning infrastructure for a fixed
  generator, not a direct generation method.
- `#114` (`L84`) — Angry Birds corpus only; no generator or fixed benchmark.

Cross-page duplicate rows to remove from PCG and retain in end-to-end:

- PCG `#12` (`L28`) ↔ end-to-end `#14`: **GAVEL**.
- PCG `#13` (`L29`) ↔ end-to-end `#13`: **GGDG**.
- PCG `#14` (`L30`) ↔ end-to-end `#12`: **Game Generation via LLMs**.
- PCG `#15` (`L31`) ↔ end-to-end `#16`: **ScriptDoctor**.
- PCG `#16` (`L32`) ↔ end-to-end `#17`: **Cardiverse**.

### Interactive worlds

Strict topical removals from `docs/*/interactive-worlds.md`:

- `#5`, `L17` — **Oasis** is a technical/model release without a paper.
- `#15`, `L27` — **ReactiveGWM** centers NPC strategy and behavior steering.
- `#23`, `L35` — **Magpie** is a learned renderer; conventional code retains
  rules, physics, and state transitions.
- `#25`, `L44` — **EgoCS-400K** is a dataset without a fixed generation
  benchmark/evaluator.
- `#26`, `L45` — **PhysEditWorld** is a dataset/resource with proposed tasks,
  not a formal released benchmark.
- `#28`, `L47` — **Game2World Engine** is HUD-removal preprocessing and its
  benchmark evaluates UI removal, not game-world generation.
- `#29`, `L55` — position/taxonomy paper only.
- `#30`, `L56` — **GameGen-X** generates prompted/event-conditioned videos but
  does not expose a stepwise player-control loop.
- `#31`, `L57` — survey/perspective plus collection-engine description; no
  generator.
- `#32`, `L58` — position/profiling paper; no generator or empirical generation
  benchmark.
- `#33`, `L59` — **WorldMind** centers state-aware NPC planning and behavior.

After those removals, add end-to-end `#50` **Playable Game Generation** here as
one canonical method-paper row.

## Row-by-row determinations

The compact reasons below ensure every pre-cleanup public row has an explicit
decision. Duplicate and move decisions are included rather than silently
counting the same paper twice.

### End-to-end: all 50 rows

| ID | Decision | One-sentence basis |
| ---: | --- | --- |
| 1 | KEEP | Formally benchmarks requirements-to-runnable-Pygame generation. |
| 2 | KEEP | Formally benchmarks implementation of behavioral Godot project tasks. |
| 3 | KEEP | Benchmarks brief-to-complete-playable-Godot generation. |
| 4 | KEEP | Benchmarks game-specific UE5 code/project implementation. |
| 5 | KEEP | Its lifecycle benchmark contains a substantive from-scratch GameGen track. |
| 6 | KEEP | JamBench defines and evaluates theme-driven project and full-script generation. |
| 7 | REMOVE | It evaluates a verifier, not a game generator or generation benchmark. |
| 8 | KEEP | Canonical row for the formal OpenGame browser-game generation benchmark. |
| 9 | KEEP | Canonical row for a 200-prompt playable-game generation benchmark. |
| 10 | KEEP | Canonical row for brief-to-runnable-UE5 generation and its benchmark. |
| 11 | KEEP | Benchmarks 111 specifications mapped to runnable web games. |
| 12 | KEEP | Directly generates executable VGDL rules and levels together. |
| 13 | KEEP | Directly generates executable Ludii game programs. |
| 14 | KEEP | Quality-diversity search directly creates executable Ludii games. |
| 15 | KEEP | Its agents plan, generate, and execute game code rather than play a fixed game. |
| 16 | KEEP | It creates complete PuzzleScript games; repair is internal generation feedback. |
| 17 | KEEP | It creates mechanics, executable code, and playable card-game prototypes. |
| 18 | KEEP | It maps text to runnable role-playing mechanics and gameplay. |
| 19 | REMOVE-DUPLICATE | It is the same OpenGame paper as canonical row 8. |
| 20 | KEEP | It directly evolves executable HTML5 games and mechanic deltas. |
| 21 | KEEP | It produces Unity code, scenes, and runnable prototypes from requirements. |
| 22 | REMOVE-DUPLICATE | It is the same Play2Code/PlaytestArena paper as canonical row 9. |
| 23 | KEEP | It generates playable Python board-game code from natural-language rules. |
| 24 | REMOVE-DUPLICATE | It is the same AutoUE/PlayGen-20 paper as canonical row 10. |
| 25 | KEEP | It generates a human-interactive gameplay state process rather than a policy. |
| 26 | KEEP | It produces goals, tile maps, and a runnable 2-D game from a story. |
| 27 | KEEP | It synthesizes executable mechanics from example frames. |
| 28 | KEEP | It produces executable full-game Ludii descriptions from language. |
| 29 | KEEP | It generates interactive-fiction worlds and executable action code. |
| 30 | KEEP | It automatically generates, selects, and revises JavaScript games. |
| 31 | KEEP | It generates Unity-compatible game-mechanic code/templates from a GDD. |
| 32 | KEEP | It compiles language into executable ECS spells and behaviors. |
| 33 | KEEP | It evolves mechanics and composes them into complete playable games. |
| 34 | KEEP | It outputs directly applicable balanced rule configurations; self-play is evaluation. |
| 35 | REMOVE | It is negative empirical probing without a new generator or formal benchmark. |
| 36 | KEEP | It generates complete playable educational web games from questions. |
| 37 | KEEP | It turns natural-language rules into executable Python game environments. |
| 38 | KEEP | It trains a complete-Godot-project code generator through verification. |
| 39 | KEEP | It generates a runnable, navigable multi-scene Unity project. |
| 40 | KEEP | It directly generates executable VGDL rules. |
| 41 | KEEP | It rebuilds and evaluates a rule generator that produces new mechanics. |
| 42 | KEEP | It adds executable role code and runtime mechanics from language. |
| 43 | REMOVE | It only tunes/repairs one fixed game's configuration. |
| 44 | REMOVE | It only repairs existing faulty game descriptions. |
| 45 | REMOVE | Its output is a non-executable natural-language rulebook. |
| 46 | KEEP | Its automatic planner builds and compiles game-project actors, assets, and scenes. |
| 47 | KEEP | ChatGE incrementally builds and executes a complete `CustomGame`, evaluated whole-game. |
| 48 | REMOVE | Its central result is trajectory/world-model infrastructure and asset editing. |
| 49 | REMOVE | It is voice-driven field editing in one fixed game. |
| 50 | KEEP-MOVE | It is a real-time player-controlled learned engine and belongs in interactive worlds. |

For row 47, the stricter decision follows the
[ACL paper](https://aclanthology.org/2025.acl-long.218/): section 3.1 says the
snippets progressively build complete `CustomGame` code which is executed for
play, and sections 6.3–6.4 evaluate the entire game's ESR/accuracy. The current
pre-cleanup public row's “rather than a verified complete build” wording was too broad.

### PCG: all 115 rows

| ID | Decision | One-sentence basis |
| ---: | --- | --- |
| 1 | KEEP | Evolution directly produces complete two-player games. |
| 2 | KEEP | Ludi evolves executable abstract-board-game rules. |
| 3 | KEEP | ANGELINA co-evolves mechanics, rules, and levels into games. |
| 4 | KEEP | Game-o-Matic maps concept graphs to small playable games. |
| 5 | KEEP | It discovers rule changes and builds levels exposing them. |
| 6 | KEEP | It searches formal representations to synthesize executable mechanics. |
| 7 | KEEP | It assembles complete playable games from themes, mechanics, and content. |
| 8 | KEEP | It blends structured game representations to create new games. |
| 9 | REMOVE | It is a conceptual orchestration survey/architecture. |
| 10 | KEEP | Puck automatically accumulates complete playable game designs. |
| 11 | REMOVE | Ludii is infrastructure, not a generation method. |
| 12 | REMOVE-DUPLICATE | GAVEL is canonically retained as end-to-end row 14. |
| 13 | REMOVE-DUPLICATE | GGDG is canonically retained as end-to-end row 13. |
| 14 | REMOVE-DUPLICATE | Game Generation via LLMs is canonically retained as end-to-end row 12. |
| 15 | REMOVE-DUPLICATE | ScriptDoctor is canonically retained as end-to-end row 16. |
| 16 | REMOVE-DUPLICATE | Cardiverse is canonically retained as end-to-end row 17. |
| 17 | KEEP | It is a formal multi-domain procedural-generation benchmark. |
| 18 | REMOVE | VGLC is dataset-only and prescribes no fixed evaluator. |
| 19 | KEEP | It is a formal Mario level-generation competition/benchmark. |
| 20 | KEEP | Its dedicated generation track formally evaluates cross-game level generators. |
| 21 | KEEP | It searches a learned Mario latent space for playable levels. |
| 22 | KEEP | TOAD-GAN directly generates tile levels from one example. |
| 23 | KEEP | The RL policy directly edits and generates content. |
| 24 | KEEP | It directly learns target-controlled tile-level generators. |
| 25 | KEEP | It generates executable bullet-hell attack patterns. |
| 26 | KEEP | It evolves playable tutorial levels requiring specified mechanics. |
| 27 | KEEP | It trains language models to generate solvable Sokoban levels. |
| 28 | KEEP | MarioGPT directly maps prompts to playable Mario levels. |
| 29 | KEEP | LSTMs directly sample complete Mario levels. |
| 30 | KEEP | GANs directly synthesize DOOM layouts. |
| 31 | REMOVE | The paper analyzes generic WFC rather than a playable game generator. |
| 32 | REMOVE | It generates Minecraft voxel components without playable-level objectives. |
| 33 | REMOVE | It benchmarks settlement components rather than playable games or levels. |
| 34 | REMOVE | It is a search-based-PCG survey/taxonomy. |
| 35 | REMOVE | It is a PCGML survey/taxonomy. |
| 36 | KEEP | A causal transformer directly generates Sokoban edits and layouts. |
| 37 | KEEP | It is a formal prompt-to-Science-Birds-level competition family. |
| 38 | KEEP | It turns instructional language into educational-game levels. |
| 39 | KEEP | A conditional VAE directly generates and validates Match-3 layouts. |
| 40 | KEEP | It generates complete playable Connections puzzle instances. |
| 41 | KEEP | It distils a dungeon generator into steerable generative models. |
| 42 | KEEP | PCGRL+ trains scalable level-generation policies. |
| 43 | KEEP | Generated reward programs drive PCGRL to produce requested levels. |
| 44 | KEEP | It converts stories into Minecraft levels with gameplay constraints. |
| 45 | KEEP | It trains a language-instructed level-generation policy. |
| 46 | REMOVE | Its sole contribution is repair of already-broken levels. |
| 47 | KEEP | VIPCGRL directly generates levels aligned to text or sketches. |
| 48 | KEEP | It automatically assembles navigable multi-floor 3-D levels. |
| 49 | REMOVE | Its sole contribution is stabilization/repair of existing levels. |
| 50 | KEEP | It maps language to PCG parameters that generate 3-D maps. |
| 51 | KEEP | It optimizes and exports drivable race-track geometry. |
| 52 | KEEP | STRUM generates loadable, playable rhythm-game charts. |
| 53 | KEEP | It generates and blends levels across four game domains. |
| 54 | KEEP | It generates structured, actionable RPG quests and dependencies. |
| 55 | REMOVE | It produces non-executable card items/art rather than a playable game. |
| 56 | KEEP | PRP directly reconstructs and generates valid Sokoban levels. |
| 57 | KEEP | Program search produces generators whose evaluated output is game levels. |
| 58 | REMOVE | It is an evaluation survey. |
| 59 | REMOVE | It is a generative-AI PCG survey. |
| 60 | REMOVE | It is a PCG/LLM survey. |
| 61 | KEEP | Launchpad generates complete platform levels playable by construction. |
| 62 | KEEP | ASP samples executable rulesets instantiated as playable mini-games. |
| 63 | KEEP | EGGG composes abstract specifications into functioning game programs. |
| 64 | KEEP | Its central method is hierarchical, physics-aware platform-level generation. |
| 65 | KEEP | It evolves executable balanced board-game rule files. |
| 66 | KEEP | It generates runnable WarioWare-style micro-games. |
| 67 | KEEP | It evolves playable personalized racing tracks. |
| 68 | KEEP | It searches and generates personalized Mario levels. |
| 69 | KEEP | It generates platform segments online from a player model. |
| 70 | KEEP | Tanagra automatically generates/regenerates reachable platform levels. |
| 71 | KEEP | It automatically proposes playable strategy-map alternatives. |
| 72 | KEEP | Learned Markov models directly sample multi-game maps. |
| 73 | KEEP | It directly constructs Infinite-Mario platform spaces/levels from chunks. |
| 74 | KEEP | It evolves complete RTS maps. |
| 75 | KEEP | It jointly generates mission graphs and matching spaces. |
| 76 | KEEP | It evolves connected levels toward target challenge. |
| 77 | KEEP | It evolves connected, solvable maze-like levels. |
| 78 | KEEP | It evolves FPS maps loadable in Cube 2. |
| 79 | KEEP | Grammatical evolution directly creates Mario levels. |
| 80 | KEEP | It evolves Mario levels toward learned pattern objectives. |
| 81 | KEEP | N-grams directly sample linear Mario levels. |
| 82 | KEEP | MCTS guides generation of near-guaranteed-playable Mario levels. |
| 83 | KEEP | It samples and validates multi-scale Zelda dungeons. |
| 84 | KEEP | It generates solvable chess-maze and chromatic-puzzle instances. |
| 85 | KEEP | It recombines learned components into loadable Mario levels. |
| 86 | KEEP | Cellular automata generate an expanding playable cave level in real time. |
| 87 | KEEP | Constrained Markov sampling produces controlled Mario/Kid-Icarus maps. |
| 88 | KEEP | Its domain-transfer method directly improves cross-game level generation. |
| 89 | REMOVE | It is a training-data-effects comparison, not a new method or benchmark. |
| 90 | KEEP | Learned movement models constrain generation toward plausible traversal paths. |
| 91 | KEEP | Multi-layer representations directly generate Mario/Lode-Runner maps. |
| 92 | KEEP | It extracts structure from videos and assembles complete new levels. |
| 93 | KEEP | The autoencoder includes noise-driven generation, so it is not repair-only. |
| 94 | KEEP | It composes complete playable Mario levels through learned tile voices. |
| 95 | KEEP | It learns primitives and composes quality-controlled Mario levels online. |
| 96 | KEEP | AE/VAE decoding plus evolution generates playable Lode Runner layouts. |
| 97 | KEEP | A common latent space generates solvable levels for four games. |
| 98 | KEEP | The co-trained generator directly produces playable Zelda levels. |
| 99 | KEEP | At inference it transforms random maps into connected generated mazes. |
| 100 | KEEP | It evolves a reusable generator of complete winnable dungeons. |
| 101 | KEEP | Interactive evolution synthesizes executable Mario level generators. |
| 102 | KEEP | Marahel scripts directly execute constructive 2-D map generation. |
| 103 | KEEP | Its meta-generator optimizes constructive generators and their level output. |
| 104 | KEEP | It evolves generator programs that produce Zelda/Sokoban/Binary maps. |
| 105 | KEEP | It evolves WFC examples that generate maze and Zelda layouts. |
| 106 | KEEP | It explicitly establishes and empirically evaluates a reusable Mario-generator benchmark. |
| 107 | REMOVE | It specifies metric vocabulary but no generator or formal benchmark. |
| 108 | REMOVE | It only tests metric validity against human judgments. |
| 109 | REMOVE | It contributes platformer design metrics, not generation. |
| 110 | REMOVE | It contributes evaluation methodology, not generation. |
| 111 | KEEP | It is a formal Angry Birds level-generation competition. |
| 112 | REMOVE | It analyzes/tunes fixed generators rather than proposing direct generation. |
| 113 | KEEP | Besides comparison, it proposes generation-method modifications for Sokoban. |
| 114 | REMOVE | It is a corpus paper without a generator or fixed benchmark. |
| 115 | KEEP | A diffusion model directly generates Mario level patches. |

### Interactive worlds: all 33 rows

| ID | Decision | One-sentence basis |
| ---: | --- | --- |
| 1 | KEEP | It generates action-conditioned Tennis/Minecraft game-world rollouts. |
| 2 | KEEP | Genie turns an image into a player-controlled generated platform world. |
| 3 | KEEP | GenieRedux trains action-controlled CoinRun/RetroAct world generators. |
| 4 | KEEP | GameNGen is a real-time player-controlled generated Doom engine. |
| 5 | REMOVE | Oasis has no method or benchmark paper to index. |
| 6 | KEEP | GameFactory transfers keyboard/mouse control into newly generated scenes. |
| 7 | KEEP | MineWorld is explicitly a real-time player-controlled Minecraft generator. |
| 8 | KEEP | Matrix-Game generates real-time keyboard/mouse-controlled game worlds. |
| 9 | KEEP | GameCraft generates long action-controlled multi-game rollouts. |
| 10 | KEEP | It proposes and evaluates a real-time action-conditioned game engine. |
| 11 | KEEP | Solaris generates synchronized worlds from two players' control streams. |
| 12 | KEEP | MultiGen generates editable shared multiplayer worlds at interactive speed. |
| 13 | KEEP | WorldCam generates keyboard/mouse-controlled 3-D game-world observations. |
| 14 | KEEP | ActionParty generates multiplayer video with subject-specific controls. |
| 15 | REMOVE | Its central contribution is steering NPC strategies and behavior. |
| 16 | KEEP | SCOPE generates game observations from dense frame-aligned player controls. |
| 17 | KEEP | MIRA generates real-time worlds from four players' actions. |
| 18 | KEEP | StatePlay generates action-conditioned video plus mechanics-relevant state. |
| 19 | KEEP | WanToFight generates a real-time two-player combat world. |
| 20 | KEEP | MASS advances one generated shared state from all players' actions. |
| 21 | KEEP | ForgeWM trains real-time action-conditioned world generators. |
| 22 | KEEP | Marionette generates action-driven state, geometry, and game observations. |
| 23 | REMOVE | It learns only appearance rendering while a conventional engine supplies gameplay. |
| 24 | KEEP | WildBench formally evaluates action following and state alignment in generated worlds. |
| 25 | REMOVE | It is a dataset paper without a fixed generation benchmark. |
| 26 | REMOVE | It is a dataset/resource with proposed but not formalized benchmark tasks. |
| 27 | KEEP | PlayWorld is a formal benchmark whose scored object is the generated world. |
| 28 | REMOVE | It is HUD-removal preprocessing, not game-world generation. |
| 29 | REMOVE | It is a position/taxonomy paper without a generator or benchmark. |
| 30 | REMOVE | It produces prompted clips without a stepwise player-control interface. |
| 31 | REMOVE | It is a survey/perspective and collection-engine description. |
| 32 | REMOVE | It is a position/profiling paper without a generator benchmark. |
| 33 | REMOVE | Its central contribution is NPC planning and behavior. |

The section should then receive end-to-end `#50` **Playable Game Generation** as
its 23rd canonical qualifying record.

## Applied cleanup requirements

- Delete or archive the 39 topical `REMOVE` rows; do not merely relabel them as
  “boundary resources.”
- Merge the eight duplicate rows so one paper has one canonical public record
  and one global count.
- Apply identical removals and moves to English and Chinese pages.
- Prune source dossiers to the accepted canonical records and preserve removal
  decisions in this audit; recompute all public counts from the cleaned rows.

## Second-pass recheck of the first-pass 151 canonical records

This second pass re-read every record remaining after the first cleanup. IDs in
this section are the **first-pass 151-row IDs**, not the 198-row pre-cleanup IDs
used above or the final 143-row IDs. The narrower test retains a paper only when its central research
contribution directly generates one of the following, or formally benchmarks
that generation task:

- a playable game or executable game project;
- executable rules, mechanics, or gameplay behavior;
- a playable level, map, task, or rhythm chart; or
- a player-controllable generative game engine or world model.

A method does not have to invent a new commercial title or IP. A learned engine
that simulates an existing game remains in scope when player input advances the
generated world. Conversely, editing tasks inside existing repositories,
player/NPC policies, offline prompted video, rendering alone, datasets,
framework descriptions, fixed-parameter tuning, asset reskinning, and
non-executable narrative structures remain out of scope. An automated player or
playtesting agent may be used as an evaluator without changing the paper's
scope: the decisive question is whether the scored research object is the
generated game/content/world or the playing agent.

### Second-pass result

| Current section | Rechecked | `KEEP` | `REMOVE` |
| --- | ---: | ---: | ---: |
| End-to-end | 39 | 34 | 5 |
| PCG | 89 | 86 | 3 |
| Interactive worlds | 23 | 23 | 0 |
| **Total** | **151** | **143** | **8** |

The resulting public collection therefore contains **143 canonical records**.
The exact first-pass-ID decisions are:

- **End-to-end `KEEP`:** `#1`, `#3`, `#5`–`#13`, `#15`–`#29`,
  `#31`–`#37`, `#39`.
- **End-to-end `REMOVE`:** `#2`, `#4`, `#14`, `#30`, `#38`.
- **PCG `KEEP`:** `#1`–`#10`, `#12`–`#17`, `#19`–`#86`,
  `#88`–`#89`.
- **PCG `REMOVE`:** `#11`, `#18`, `#87`.
- **Interactive worlds `KEEP`:** `#1`–`#23`.
- **Interactive worlds `REMOVE`:** none.

### Eight records removed in the second pass

#### End-to-end

- `#2` — **GameDevBench**: the
  [paper](https://arxiv.org/abs/2602.11103) constructs 333 tasks by turning
  tutorials into edits of existing Godot repositories. Its evaluated object is
  a multimodal coding agent's success on scoped repository tasks, not a method
  or benchmark for generating a game.
- `#4` — **GameEngineBench**: the
  [paper](https://arxiv.org/abs/2607.03525) evaluates scoped native-C++
  implementation tasks inside nine existing Unreal Engine 5 repositories. It
  is explicitly a software-engineering-agent benchmark, not a game-generation
  benchmark.
- `#14` — **GameGPT**: the
  [paper](https://arxiv.org/abs/2310.08067) proposes a multi-agent architecture,
  but its body proceeds from the framework description directly to references:
  it supplies no experiment section, generated-game evidence, fixed generation
  task, or official implementation. It is framework-only evidence, not a
  demonstrated generation method.
- `#30` — **RuleSmith**: the
  [paper](https://arxiv.org/abs/2602.06232) runs self-play and Bayesian
  optimization over CivMini's fixed multidimensional parameter space. Its
  output is a balance-oriented parameter configuration; it does not generate
  new rules, mechanics, content, or a game.
- `#38` — **DreamGarden**: section 2.4 of the
  [paper](https://arxiv.org/abs/2410.01791) states that “DreamGarden is
  restricted to generating 0-player simulations” and presents playable game
  snippets as future work. The reported system therefore does not directly
  produce a playable game under this audit's rule.

#### PCG

- `#11` — **A Rogue Dream: Automatically Generating Meaningful Content for
  Games**: the [official paper PDF](https://ojs.aaai.org/index.php/AIIDE/article/download/12745/12593)
  describes dynamic reskinning of one fixed roguelite. It replaces the images
  for the player, enemies, items, and goal and selects from pre-authored
  abilities; it does not generate rules, mechanics, levels, or a complete game.
  See also the [AIIDE record](https://doi.org/10.1609/aiide.v10i3.12745).
- `#18` — **Procedural Level Design for Platform Games**: the
  [official paper PDF](https://ojs.aaai.org/index.php/AIIDE/article/download/18755/18531)
  says the prototype implements only a single-pattern builder, while the cell
  structure and full-level generator remain unimplemented. The demonstrated
  contribution is therefore an isolated construction component rather than a
  method that directly generates playable levels. See also the
  [AIIDE record](https://doi.org/10.1609/aiide.v2i1.18755).
- `#87` — **From World-Gen to Quest-Line**: the
  [paper](https://arxiv.org/abs/2604.25482) outputs narrative JSON describing a
  world, NPCs, player, quest, dialogue, choices, and outcomes. It supplies no
  engine execution, gameplay logic, or playable artifact and describes the
  evaluation as application-driven rather than benchmark-driven. It is thus
  non-executable narrative generation, not game generation.

### Canonical citation correction for PCG `#8`

PCG `#8` remains a `KEEP`, but its canonical citation had pointed to the wrong
paper about the same system. It was corrected from **The Micro-Rhetorics of
Game-o-Matic** ([old DOI](https://doi.org/10.1145/2282338.2282347)) to
**Game-O-Matic**
([method-paper DOI](https://doi.org/10.1145/2538528.2538537)), presented at the
Third Workshop on Procedural Content Generation in Games in 2012. The latter is
the system paper describing how the generator selects and combines
micro-rhetorics from a concept map to produce coherent playable games. This is
a same-system citation correction, not an additional canonical record.

### Explicit boundary keeps

The following potentially confusing records remain in scope after primary-
source review:

- End-to-end `#21` **IDGE** accepts free-form rules and player actions and
  generates successive gameplay states. It acts as a customizable generative
  game engine, not a poker-playing policy.
- End-to-end `#25` **STORY2GAME** generates executable action code and evaluates
  complete interactive playthroughs; its narrative input does not make the
  output merely a story.
- End-to-end `#28` **Real-Time World Crafting** and `#37` **Open Role-Playing
  with Delta-Engines** generate new executable behaviors, abilities, and
  mechanics code inside base engines. They do more than tune fixed parameters.
- Interactive-world `#1`–`#21` all generate world observations or state
  step-by-step in response to player controls. Training or data-collection
  agents are auxiliary and do not turn these papers into player-agent work.
- Interactive-world `#22` **WildBench** and `#23` **PlayWorld** formally score
  generated worlds. Their agent players are test probes, not the research
  object being optimized.
- PCG `#53` **Marahel** uses scripts as stochastic level-generator
  specifications whose interpreter directly emits maps; it is not merely an
  authoring language. The implementation claim is documented in the
  [official paper PDF](https://ojs.aaai.org/index.php/AIIDE/article/download/12970/12818).
- PCG `#57` formally compares seven Mario generator families under a shared
  evaluation and therefore qualifies as a generator benchmark. PCG `#59` both
  runs a unified benchmark study and proposes substantive changes to a Sokoban
  generation method; neither is a metric-only paper.
