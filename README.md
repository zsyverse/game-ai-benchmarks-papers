# Game AI Benchmarks & Papers

English · [简体中文](README.zh-CN.md)

A researched, bilingual map of benchmarks and primary-source papers for **building games with AI** and **building agents that play games**.

This repository currently covers **66 curated entries** and more than **150 primary-source links**. It distinguishes reproducible benchmarks from datasets, environments, papers, tools, and demos—because a playable demo is not automatically a benchmark.

Last fully verified: **2026-08-29**.

## Browse the collection

| Area | English | 中文 | Coverage |
| --- | --- | --- | --- |
| Game creation | [Benchmarks & papers](docs/en/game-creation.md) | [基准与论文](docs/zh-CN/game-creation.md) | 9 benchmarks/datasets, 7 generation or development-agent papers, 7 interactive-world systems |
| Game agents | [Benchmarks & papers](docs/en/game-agents.md) | [基准与论文](docs/zh-CN/game-agents.md) | 25 benchmark/environment/platform rows and 18 selected agent papers |
| Verification notes | [Game creation sources](research/game-generation-sources.md) | [Game-agent sources](research/game-agent-sources.md) | Detailed task definitions, metrics, artifact status, access restrictions, and provenance |

## Quick map

| If you want to evaluate… | Good starting points |
| --- | --- |
| Agents editing real game-engine repositories | [GameDevBench](https://github.com/waynchi/gamedevbench) (Godot, deterministic tests), [GameEngineBench](https://github.com/Nitrode-Research/GameEngineBench) (Unreal C++, behavioral tests) |
| End-to-end game generation | [GameCraft-Bench](https://github.com/FreedomIntelligence/gamecraft-bench) (Godot), [V-GameGym](https://github.com/alibaba/SKYLENAGE-GameCodeGym) (Pygame) |
| Procedural level/content generation | [PCG Benchmark](https://github.com/amidos2006/pcg_benchmark), [VGLC](https://github.com/TheVGLC/TheVGLC), [GVGAI](https://github.com/GAIGResearch/GVGAI) |
| LLM/VLM agents across several games | [BALROG](https://github.com/balrog-ai/BALROG), [VideoGameBench](https://github.com/alexzhang13/videogamebench), [SmartPlay](https://github.com/microsoft/SmartPlay), [GameBench](https://github.com/Joshuaclymer/GameBench) |
| Minecraft and open-world agents | [MineDojo](https://github.com/MineDojo/MineDojo), [MineRL](https://github.com/minerllabs/minerl), [BEDD](https://github.com/minerllabs/basalt-benchmark), [Crafter](https://github.com/danijar/crafter) |
| Generalization in classic RL/game suites | [ALE](https://github.com/Farama-Foundation/Arcade-Learning-Environment), [Procgen](https://github.com/openai/procgen), [NLE](https://github.com/NetHack-LE/nle), [MiniHack](https://github.com/NetHack-LE/minihack) |
| Competitive or multi-agent play | [SMACv2](https://github.com/oxwhirl/smacv2), [Melting Pot](https://github.com/google-deepmind/meltingpot), [OpenSpiel](https://github.com/google-deepmind/open_spiel), [Honor of Kings Arena](https://github.com/tencent-ailab/hok_env) |
| Action-conditioned interactive worlds | [DIAMOND](https://github.com/eloialonso/diamond), [Oasis](https://github.com/etched-ai/open-oasis), [GameGen-X](https://github.com/GameGen-X/GameGen-X), [Matrix-Game](https://github.com/SkyworkAI/Matrix-Game), [Hunyuan-GameCraft](https://github.com/Tencent-Hunyuan/Hunyuan-GameCraft-1.0) |

## Labels used in this repository

### Resource kind

| Label | Meaning |
| --- | --- |
| `Benchmark` / `B` | A repeatable task with an evaluation protocol or metric |
| `Environment` / `Platform` / `P` | An interactive research interface, possibly without one fixed task set or score |
| `Dataset` | Reusable data that may not define a complete evaluation |
| `Paper` | A research method or result, not necessarily reusable as a benchmark |
| `Tool` | Development or evaluation infrastructure |

### Reproducibility

| Label | Meaning |
| --- | --- |
| **Yes** | Public tasks/data plus runnable evaluation or training/inference code make the same score definition obtainable in principle |
| **Partial** | Some artifacts are public, but required tasks, tests, outputs, scorer, data, weights, or licensed assets are missing |
| **No** | No public, fixed benchmark protocol plus usable artifacts was available at the verification cutoff |

## Important cautions

- **World models and game-building agents are separate tasks.** One predicts pixels or latents under actions; the other edits code, scenes, and assets inside an engine. Their scores should not share a leaderboard.
- **Model-judge and deterministic-test scores are not equivalent.** Record the judge model/version, seeds, game/engine version, interaction budget, and aggregation rule.
- **Commercial games and assets have separate licenses.** A public repository does not grant rights to ROMs, game clients, engine SDKs, videos, or training data.
- **Artifact status changes.** At the cutoff, GameXpert-Bench was only a release scaffold and no verifiable JamBench artifact URL could be located; both are marked **No**, despite their papers describing full benchmarks.

## Repository map

```text
.
├── README.md / README.zh-CN.md
├── docs/
│   ├── en/       # English curated tables
│   └── zh-CN/    # 中文完整对照表
├── research/     # Primary-source verification notes
└── .github/      # Resource suggestion template
```

## Contributing

Corrections and additions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and include at least one primary-source link, a resource type, task, metrics, artifact status, and matching English/Chinese descriptions.

## License

This index is released under the [MIT License](LICENSE). Linked papers, code, datasets, games, models, and other artifacts retain their original licenses.
