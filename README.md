# Game Generation Benchmarks & Papers

English · [简体中文](README.zh-CN.md)

> A bilingual, primary-source-verified bibliography of **AI that generates games**—not AI that plays them.

This repository covers systems that create complete games, executable rules and mechanics, game code and engine projects, levels and playable content, or action-conditioned interactive worlds. It contains **82 detailed category records** (with intentional cross-listing) and more than **200 links to papers and official artifacts**.

Last fully verified: **2026-08-29**.

## Browse by generation target

| Collection | English | 中文 | Coverage |
| --- | --- | --- | --- |
| End-to-end games and code | [29 benchmarks and papers](docs/en/end-to-end.md) | [29 个 benchmark 与论文](docs/zh-CN/end-to-end.md) | Prompt-to-game, engine/project/code generation, game-development agents, verification, repair, and co-creation |
| Automated design and PCG | [35 papers and resources](docs/en/pcg.md) | [35 篇论文与资源](docs/zh-CN/pcg.md) | Complete games, rules/mechanics, level generation, datasets, PCG benchmarks, and foundational surveys |
| Interactive game worlds | [18 papers and resources](docs/en/interactive-worlds.md) | [18 篇论文与资源](docs/zh-CN/interactive-worlds.md) | Action-conditioned video worlds, learned game engines, explicit state/mechanics, multiplayer and long-horizon generation |
| Detailed evidence | [Research notes](research/README.md) | [一手来源核验底稿](research/README.md) | Task definitions, evaluation protocols, artifact availability, boundary decisions, and primary-source evidence |

Read the exact inclusion and exclusion rules in [SCOPE.md](SCOPE.md).

## What counts as game generation?

| Layer | Output | Representative work |
| --- | --- | --- |
| Complete game | A runnable project containing gameplay, rules, scenes, code, and assets | [AutoUE](https://arxiv.org/abs/2603.07106), [OpenGame](https://arxiv.org/abs/2604.18394), [GameCraft-Bench](https://arxiv.org/abs/2606.17861), [V-GameGym](https://arxiv.org/abs/2509.20136) |
| Rules and mechanics | An executable game description or program defining new gameplay | [Ludi](https://eprints.qut.edu.au/17025/), [ANGELINA](https://doi.org/10.1109/CIG.2011.6032019), [GAVEL](https://arxiv.org/abs/2407.09388), [GGDG](https://arxiv.org/abs/2407.17404) |
| Levels and playable content | Maps, puzzles, dungeons, attack patterns, or tutorial levels under fixed or partly generated rules | [MarioGAN](https://doi.org/10.1145/3205455.3205517), [TOAD-GAN](https://arxiv.org/abs/2008.01531), [PCGRL](https://doi.org/10.1609/aiide.v16i1.7416), [MarioGPT](https://arxiv.org/abs/2302.05981) |
| Learned interactive world | Action-conditioned pixels, geometry, and/or explicit state that can be controlled in real time | [Genie](https://proceedings.mlr.press/v235/bruce24a.html), [GameNGen](https://arxiv.org/abs/2408.14837), [GameFactory](https://arxiv.org/abs/2501.08325), [StatePlay](https://arxiv.org/abs/2607.26754) |

The fourth layer is deliberately kept separate: generating a controllable video world is not the same as authoring explicit code, rules, and assets in a conventional engine.

## Benchmark quick start

| Benchmark | Generation task | Evaluation | Availability at cutoff |
| --- | --- | --- | --- |
| [V-GameGym](https://arxiv.org/abs/2509.20136) | Natural language → runnable Pygame | Code, screenshot, and gameplay-video evidence | **Open** |
| [GameDevBench](https://arxiv.org/abs/2602.11103) | Edit real Godot repositories | Deterministic runtime tests | **Open** |
| [GameCraft-Bench](https://arxiv.org/abs/2606.17861) | Brief → complete Godot game | Replay, build gate, mechanics/content/visual rubric | **Open; environment-heavy** |
| [GameEngineBench](https://arxiv.org/abs/2607.03525) | Implement native C++ tasks in UE5 repositories | Hidden Unreal behavioral tests | **Open; environment-heavy** |
| [PlayGen-20 / AutoUE](https://arxiv.org/abs/2603.07106) | Brief → complete UE5 3D game | Scene, gameplay, visual, graph/module, and runtime checks | **Open; environment-heavy** |
| [PCG Benchmark](https://arxiv.org/abs/2503.21474) | Generate levels/content across many domains | Quality, diversity, and controllability | **Open** |
| [OpenGame-Bench](https://arxiv.org/abs/2604.18394) | Prompt → browser game | Build health, visual usability, intent alignment | **Partial** |
| [PlaytestArena](https://arxiv.org/abs/2605.28258) | Prompt → browser game with GUI playtesting | Observable rubric pass rate | **Partial** |
| [GameXpert-Bench](https://arxiv.org/abs/2608.21833) | Generate, fix, and optimize games | Lifecycle-specific rubrics and tests | **Closed; release scaffold only** |

## Historical path

- **2008–2014 — automated game design:** Ludi, ANGELINA, Game-o-Matic, Mechanic Miner, and formal mechanic generation established the idea of generating rules and complete games.
- **2016–2021 — PCGML and learned levels:** VGLC, LSTM level generation, MarioGAN, DoomGAN, TOAD-GAN, PCGRL, and controllable PCGRL made data-driven content generation reproducible.
- **2023–2025 — language models for games:** MarioGPT, GameGPT, GAVEL, grammar-guided rule generation, ScriptDoctor, Cardiverse, GameFactory, and newer text-to-game systems expanded generation from maps to code and mechanics.
- **2026 — engine-native agents and stateful worlds:** Godot/Unreal/browser benchmarks, AutoUE, long-horizon world models, explicit mechanics/state generation, and automatic playtest-repair loops became central.

## Explicitly excluded: playing games

The following are important Game AI research, but they do not belong in a generation-only bibliography:

- DQN, AlphaGo, AlphaZero, MuZero, Agent57, AlphaStar, OpenAI Five, Voyager, SIMA, and other game-playing agents;
- BALROG, VideoGameBench, MineRL/BASALT, MineDojo agent tasks, ALE, Procgen, NLE, Crafter, and other gameplay/control benchmarks;
- Dreamer, SimPLe, IRIS, and **DIAMOND**, because their central result is policy learning or game-playing return rather than a human-controllable generated game world;
- GameWAM and similar action-generating policies whose primary metric is task success;
- standalone NPC AI, player modelling, matchmaking, game analytics, and asset-only generation.

Automated players can still appear as **evaluators** of generated designs, and RL can appear when the policy itself is the **content generator**, as in PCGRL.

## Availability labels

| Label | Meaning |
| --- | --- |
| **Open** | The official core code/data/tasks and meaningful evaluation or runnable weights are available |
| **Partial** | Useful official artifacts exist, but an essential task set, evaluator, training stack, data, model, or output set is missing |
| **Closed / Paper-only** | No reproducible official implementation or benchmark package was verified at the cutoff |

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
└── .github/           # scoped resource-suggestion template
```

## Contributing

Corrections and additions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md). Every proposal must identify what the system **generates**, provide a primary-source link, state its evaluation and artifact availability, and include matching English and Chinese descriptions.

## License

This index is released under the [MIT License](LICENSE). Linked papers, code, datasets, games, models, and other artifacts retain their original licenses.
