# Game Generation Benchmarks & Papers

English · [简体中文](README.zh-CN.md)

> A bilingual, primary-source-verified bibliography of **AI that generates games**—not AI that plays them.

This repository covers systems that create complete games, executable rules and mechanics, game code and engine projects, levels and playable content, or action-conditioned interactive worlds. It contains **198 detailed category records** (with intentional cross-listing) and more than **500 links to papers and official artifacts**.

Last fully verified: **2026-09-01**.

## Browse by generation target

| Collection | English | 中文 | Coverage |
| --- | --- | --- | --- |
| End-to-end games and code | [50 benchmarks and papers](docs/en/end-to-end.md) | [50 个 benchmark 与论文](docs/zh-CN/end-to-end.md) | Prompt-to-game, engine/project/code generation, game-development agents, verification, repair, and co-creation |
| Automated design and PCG | [115 papers and resources](docs/en/pcg.md) | [115 篇论文与资源](docs/zh-CN/pcg.md) | Complete games, rules/mechanics, level generation, datasets, PCG benchmarks, and foundational surveys |
| Interactive game worlds | [33 papers and resources](docs/en/interactive-worlds.md) | [33 篇论文与资源](docs/zh-CN/interactive-worlds.md) | Action-conditioned generators, learned renderers/state engines, generation datasets/benchmarks, and field-boundary readings |
| Detailed evidence | [Research notes](research/README.md) | [一手来源核验底稿](research/README.md) | Task definitions, evaluation protocols, artifact availability, boundary decisions, and primary-source evidence |

Read the exact inclusion and exclusion rules in [SCOPE.md](SCOPE.md).

## How entries are separated

| Entry role | What it means |
| --- | --- |
| Core generator | Directly outputs a runnable game, executable rules/mechanics, game code/project changes, playable content, or a human-controllable generated world |
| Generation resource | A benchmark, dataset, corpus, verifier, repair stage, or evaluator built specifically for those generated outputs |
| Boundary or framing | Infrastructure, a mixed framework, survey, taxonomy, or perspective kept in an explicitly labelled section; it is not presented as a generator |

This separation keeps the bibliography broad without inflating the number of actual generation systems.

## What counts as game generation?

| Layer | Output | Representative work |
| --- | --- | --- |
| Complete game | A runnable project containing gameplay, rules, scenes, code, and assets | [AutoUE](https://arxiv.org/abs/2603.07106), [OpenGame](https://arxiv.org/abs/2604.18394), [STORY2GAME](https://arxiv.org/abs/2505.03547), [GamED.AI](https://arxiv.org/abs/2604.23947) |
| Rules and mechanics | An executable game description, program, or parameter set defining new gameplay | [GAVEL](https://arxiv.org/abs/2407.09388), [GGDG](https://arxiv.org/abs/2407.17404), [RLGDG](https://arxiv.org/abs/2503.15783), [Mortar](https://arxiv.org/abs/2601.00105) |
| Levels and playable content | Maps, puzzles, dungeons, quests, charts, or other content that directly determines play | [MarioGPT](https://arxiv.org/abs/2302.05981), [PCGRL+](https://arxiv.org/abs/2408.12525), [Word2Minecraft](https://arxiv.org/abs/2503.16536), [Multiverse](https://arxiv.org/abs/2603.26782) |
| Learned interactive world | Action-conditioned pixels, geometry, and/or explicit state that can be controlled in real time | [GenieRedux](https://arxiv.org/abs/2504.02515), [GameFactory](https://arxiv.org/abs/2501.08325), [Solaris](https://arxiv.org/abs/2602.22208), [MASS](https://arxiv.org/abs/2608.06257) |

The fourth layer is deliberately kept separate: generating a controllable video world is not the same as authoring explicit code, rules, and assets in a conventional engine.

## Benchmark quick start

| Benchmark | Generation task | Evaluation | Availability at cutoff |
| --- | --- | --- | --- |
| [V-GameGym](https://arxiv.org/abs/2509.20136) | Natural language → runnable Pygame | Code, screenshot, and gameplay-video evidence | **Open** |
| [WebGameBench](https://arxiv.org/abs/2605.17637) | Specification → deployed browser game | Runtime usability checked against human gameplay review | **Closed** |
| [GameDevBench](https://arxiv.org/abs/2602.11103) | Edit real Godot repositories | Deterministic runtime tests | **Open** |
| [GameCraft-Bench](https://arxiv.org/abs/2606.17861) | Brief → complete Godot game | Replay, build gate, mechanics/content/visual rubric | **Open; environment-heavy** |
| [GameEngineBench](https://arxiv.org/abs/2607.03525) | Implement native C++ tasks in UE5 repositories | Hidden Unreal behavioral tests | **Closed; official repository unavailable at cutoff** |
| [PlayGen-20 / AutoUE](https://arxiv.org/abs/2603.07106) | Brief → complete UE5 3D game | Scene, gameplay, visual, graph/module, and runtime checks | **Open; environment-heavy** |
| [PCG Benchmark](https://arxiv.org/abs/2503.21474) | Generate levels/content across many domains | Quality, diversity, and controllability | **Open** |
| [ChatGPT4PCG](https://arxiv.org/abs/2303.15662) | Prompt/program → stable Science Birds level | Stability, character similarity, and diversity | **Open** |
| [OpenGame-Bench](https://arxiv.org/abs/2604.18394) | Prompt → browser game | Build health, visual usability, intent alignment | **Partial** |
| [PlaytestArena](https://arxiv.org/abs/2605.28258) | Prompt → browser game with GUI playtesting | Observable rubric pass rate | **Partial** |
| [GameXpert-Bench](https://arxiv.org/abs/2608.21833) | Generate, fix, and optimize games | Lifecycle-specific rubrics and tests | **Closed; release scaffold only** |
| [WildWorld / WildBench](https://arxiv.org/abs/2603.23497) | Generate action/state-aligned ARPG rollouts | Action Following and State Alignment | **Partial** |
| [PlayWorld](https://arxiv.org/abs/2608.13552) | Generated world → long-horizon agent probes | Geometry, interaction, and visible/hidden evolution | **Open; API-dependent** |

## Historical path

- **2000–2015 — automated game design and early PCG:** EGGG, Ludi, ANGELINA, Game-o-Matic, early platform/racing/RTS/puzzle generators, mission–space grammars, Launchpad, Polymorph, Tanagra, Sentient Sketchbook, n-gram/Markov maps, Sampling Hyrule, generator-generating systems, and the first shared Mario/metric evaluations established automatic rules, levels, and complete-game design.
- **2016–2022 — PCGML, learned levels, and metageneration:** VGLC, constrained/domain-transfer/multilayer Markov models, video-to-level and LSTM systems, learned constructive primitives, Lode Runner autoencoders, MarioGAN, DoomGAN, TOAD-GAN, PCGRL, shared latent spaces, Generative Playing Networks, mutation models, Marahel metageneration, AIBIRDS, and its generation corpus broadened both generation and its evaluation.
- **2023–2025 — language models, diffusion, and learned worlds:** MarioGPT, unconditional Mario diffusion, Promptable Game Models, Word2World, GAVEL, RLGDG, STORY2GAME, ScriptDoctor, Cardiverse, and GameFactory expanded generation from maps to code, mechanics, and controllable video.
- **2026 — engine-native agents and stateful worlds:** Godot/Unreal/browser benchmarks, AutoUE, Mortar, MAGIC, long-horizon/multiplayer world models, explicit state generation, and automatic playtest-repair loops became central.

## Explicitly excluded: playing games

The following are important Game AI research, but they do not belong in a generation-only bibliography:

- DQN, AlphaGo, AlphaZero, MuZero, Agent57, AlphaStar, OpenAI Five, Voyager, SIMA, and other game-playing agents;
- BALROG, VideoGameBench, MineRL/BASALT, MineDojo agent tasks, ALE, Procgen, NLE, Crafter, and other gameplay/control benchmarks;
- Dreamer, SimPLe, IRIS, and **DIAMOND**, because their central result is policy learning or game-playing return rather than a human-controllable generated game world;
- GameWAM, ActSWM, and similar action-generating or planning policies whose primary metric is task success;
- METAGAME/METAGAMER, because random chess-like game generation is used as a test domain for general game playing rather than evaluated as the research product;
- standalone NPC AI, player modelling, matchmaking, game analytics, and asset-only generation.

Automated players can still appear as **evaluators** of generated designs, and RL can appear when the policy itself is the **content generator**, as in PCGRL.

## Availability labels

| Label | Meaning |
| --- | --- |
| **Open** | The official core code/data/tasks and meaningful evaluation or runnable weights are available |
| **Partial** | Useful official artifacts exist, but an essential task set, evaluator, training stack, data, model, or output set is missing |
| **Closed** | No reproducible official implementation or benchmark package was verified at the cutoff |
| **Paper-only by design** | A framing, position, or taxonomy paper intentionally proposes no generator or runnable artifact |

These labels describe artifact availability, not licensing, cost, deterministic reproducibility, or research quality.

## Repository map

```text
.
├── README.md / README.zh-CN.md
├── SCOPE.md
├── docs/
│   ├── en/{end-to-end,pcg,interactive-worlds}.md
│   └── zh-CN/{end-to-end,pcg,interactive-worlds}.md
├── research/          # detailed primary-source evidence
├── scripts/           # bilingual/count/link validation
└── .github/           # issue template and validation workflow
```

## Contributing

Corrections and additions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md). Every proposal must identify what the system **generates**, provide a primary-source link, state its evaluation and artifact availability, and include matching English and Chinese descriptions.

## License

This index is released under the [MIT License](LICENSE). Linked papers, code, datasets, games, models, and other artifacts retain their original licenses.
