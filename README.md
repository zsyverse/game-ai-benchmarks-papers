# Game Generation Methods & Benchmarks

[中文](README.zh-CN.md)

A bilingual, strictly scoped index of research that **generates games rather than plays them**. The collection contains **151 canonical records**: direct game-generation methods and formal benchmarks for those generation tasks. Each paper or version family has one canonical record; cross-listing is not counted twice.

## Browse the collection

| Collection | English | 中文 | Included output |
| --- | --- | --- | --- |
| End-to-end games and code | [39 records](docs/en/end-to-end.md) | [39 条记录](docs/zh-CN/end-to-end.md) | Runnable games, engine projects/code, executable rules and mechanics |
| Automated design and PCG | [89 records](docs/en/pcg.md) | [89 条记录](docs/zh-CN/pcg.md) | Complete games/rules and playable levels, maps, quests, puzzles, or charts |
| Interactive game worlds | [23 records](docs/en/interactive-worlds.md) | [23 条记录](docs/zh-CN/interactive-worlds.md) | Generated game worlds controlled step by step by player input |
| Scope and evidence | [Scope](SCOPE.md) | [Strict audit](research/strict-method-benchmark-scope-audit.md) | Inclusion rules and primary-source-backed decisions |

## Inclusion test

Every public record must have one of two roles:

1. **Generation method** — the paper's central contribution directly produces a runnable game, executable code/project, executable rules/mechanics, playable level/map/task/chart, or a player-controllable generated game world.
2. **Generation benchmark** — the paper formally defines a task and empirical evaluation protocol for one of those generated outputs.

The generated artifact—not an agent's score, policy return, or playing ability—must be the research object being proposed or evaluated.

## Excluded

- Game-playing agents, NPC/player policies, and gameplay benchmarks.
- Dataset/corpus-only papers, surveys, taxonomies, and position papers.
- General infrastructure, authoring tools without substantive automatic generation, and metric-only studies.
- Standalone verification, repair, QA, or parameter tuning without a direct generator.
- Standalone images, textures, 3D assets, music, dialogue, stories, cards, or other isolated components.
- Prompted game video without a stepwise player-control loop, and world models centered on planning or policy learning.

When a paper mixes generation with playtesting, search, RL, or self-play, it is included only if those techniques generate or evaluate the generated artifact itself. See [SCOPE.md](SCOPE.md) for the full decision rule.

## Artifact labels

| Label | Meaning |
| --- | --- |
| **Open** | Official core implementation and meaningful reproduction artifacts were verified |
| **Partial** | An official release exists, but a material component is missing |
| **Closed** | No runnable official core release was verified |

These labels describe artifact availability, not paper quality.

## Repository map

```text
.
├── README.md / README.zh-CN.md
├── SCOPE.md
├── CONTRIBUTING.md
├── docs/
│   ├── en/
│   └── zh-CN/
├── research/
└── scripts/validate_index.py
```

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing an entry. New entries must include a primary paper source, evidence that the central contribution passes the inclusion test, and matching English/Chinese descriptions.

Last fully verified: **2026-09-04**.

## License

This index is released under the [MIT License](LICENSE). Linked papers and artifacts retain their original licenses.
