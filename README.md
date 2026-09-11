# Game Generation Methods & Benchmarks

[中文](README.zh-CN.md) · [All papers](docs/en/paper-list.md) · [Research guide](docs/en/research-guide.md) · [Contribute](CONTRIBUTING.md)

[![Validate bibliography](https://github.com/zsyverse/game-ai-benchmarks-papers/actions/workflows/validate.yml/badge.svg)](https://github.com/zsyverse/game-ai-benchmarks-papers/actions/workflows/validate.yml) [![GitHub stars](https://img.shields.io/github/stars/zsyverse/game-ai-benchmarks-papers?style=flat)](https://github.com/zsyverse/game-ai-benchmarks-papers/stargazers) [![License](https://img.shields.io/github/license/zsyverse/game-ai-benchmarks-papers?style=flat)](https://github.com/zsyverse/game-ai-benchmarks-papers/blob/main/LICENSE)

A curated, bilingual collection of papers that **generate games rather than play them**: runnable games and code, playable content, and player-controlled generated worlds.

**203 canonical records** across three collections. One paper, one record; substantive follow-ups remain separate.

> Last fully verified: **2026-09-04**. Targeted additions and reviews: **2026-09-05 / 2026-09-08**. These are not new full-corpus audits or reproduction reports.

## Contents

- [Browse the collection](#browse-the-collection) · [All papers](docs/en/paper-list.md)
- [Start reading](#start-reading)
- [Find papers quickly](#find-papers-quickly)
- [Inclusion test](#inclusion-test) · [Artifact labels](#artifact-labels)
- [Research synthesis and coverage](#research-synthesis-and-coverage)
- [Contributing](#contributing) · [License](#license)

## Browse the collection

| Collection | Records | What you will find |
| --- | --- | --- |
| End-to-end games and code | [38 records](docs/en/end-to-end.md) | 10 benchmarks + 28 methods: runnable games, engine projects/code, executable rules and mechanics |
| Automated design and PCG | [120 records](docs/en/pcg.md) | 18 complete-game/rule methods + 102 playable-content methods and benchmarks: levels, maps, quests, puzzles and charts |
| Interactive game worlds | [45 records](docs/en/interactive-worlds.md) | 41 methods + 4 benchmarks: game worlds that evolve with stepwise player input |

[All papers — 203-record quick view](docs/en/paper-list.md) lists titles, years, artifact labels and evidence links on one page. Open a category for full task descriptions, evaluations and limitations.

New to the field? Start with the [research guide](docs/en/research-guide.md) for method families and reading routes. Detailed primary-source evidence lives in the [source dossiers](research/README.md).

## Start reading

Six entry points into different tasks—not a ranking or an additional collection. **Paper** links to the primary paper; **Code** links to official releases, whose completeness and requirements are documented in the full collection rows.

### Games and executable code

- **ByteSized32** (2023) · [Paper](https://aclanthology.org/2023.emnlp-main.830/) · [Code](https://github.com/cognitiveailab/BYTESIZED32) — Complete Python text games from task descriptions; runtime validity and human winnability are evaluated separately. API-dependent.
- **GameCraft-Bench** (2026) · [Paper](https://arxiv.org/abs/2606.17861) · [Code](https://github.com/FreedomIntelligence/gamecraft-bench) — Brief-to-Godot generation evaluated after build checks and input-trace replay. Environment-heavy.

### Playable content and PCG

- **PCGRL** (2020) · [Paper](https://doi.org/10.1609/aiide.v16i1.7416) · [Code](https://github.com/amidos2006/gym-pcgrl) — An RL policy edits tiles to generate levels; the policy is the generator, not the player.
- **The Procedural Content Generation Benchmark** (2025) · [Paper](https://arxiv.org/abs/2503.21474) · [Code](https://github.com/amidos2006/pcg_benchmark) · [Experiments](https://github.com/amidos2006/benchmark_experiments) — Shared interfaces for task-specific quality, diversity and controllability evaluation.

### Interactive worlds

- **GameGAN** (2020) · [Paper](https://arxiv.org/abs/2005.12126) · [Code (Partial)](https://github.com/nv-tlabs/GameGAN_code) — Keyboard-conditioned Pac-Man/VizDoom screen generation with memory for revisited layouts. Pretrained weights and the complete Pac-Man corpus were not verified.
- **WorldMark** (2026) · [Paper](https://arxiv.org/abs/2604.21686) · [Code](https://github.com/AlayaLab/WorldMark) — Shared key programs for evaluating action response, latency, stability, memory and visual quality. External generators require separate installation.

For hands-on work, see the [experimental entry points and pinned artifact evidence](research/experiment-entry-points-2026-09-08.md). These are setup recommendations, not independently reproduced results.

## Find papers quickly

Search locally from the repository root with Python 3.10+; no dependencies or network required.

```bash
python3 scripts/search_index.py Godot --status Open
python3 scripts/search_index.py --category interactive-worlds --year 2026
```

The [search guide](docs/en/search.md) covers bilingual keywords, filters, JSON export and how to interpret years and artifact labels.

## Inclusion test

A paper must centrally propose a **direct generation method** or a **formal generation benchmark** for a runnable game, executable code/rules, playable content or player-controlled generated world—not an agent's playing ability.

Playing/NPC policies, non-playable assets or scenes, video without stepwise player control, and support-only studies do not qualify. Playtesting, search, RL and self-play qualify only when they generate or evaluate the generated artifact itself.

See [SCOPE.md](SCOPE.md) for the complete exclusions and version/deduplication rules, and the [strict scope audit](research/strict-method-benchmark-scope-audit.md) for inclusion decisions.

## Artifact labels

| Label | Meaning |
| --- | --- |
| **Open** | Official core implementation and meaningful reproduction artifacts were verified |
| **Partial** | An official release exists, but a material component is missing |
| **Closed** | No runnable official core release was verified |

Availability is not paper quality, license freedom or proof of successful reproduction. Full rows retain evaluation limits and version-specific caveats.

## Research synthesis and coverage

- **2026-09-08 — [Latest refinement](research/completion-review-2026-09-08.md):** original ANGELINA 3D method attribution, historical Sokoban generation, world-domain follow-up and experimental entry points.
- **2026-09-05–08 — [Further discovery and integration](research/further-research-integration-2026-09-08.md):** text-game benchmarks, constrained puzzles, linked-data adventures, themed 3D generation, reconstructed playable content and interactive worlds.
- **2026-09-05 — [Reliability re-audit](research/reliability-audit-2026-09-05.md):** corrected identities, version splits and experimental interpretations; coverage additions include historical rules, rhythm charts, NCA, GFlowNets and dungeon/puzzle generation.

[Coverage notes and unresolved leads](research/README.md) retain primary evidence and specific gaps. Unsupported candidates are not counted. The collection is not an exhaustive census, and neither its size nor structural validation establishes research completeness or reproducibility.

## Contributing

Corrections, missing papers and official artifact links are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) for duplicate checks, an entry template and validation commands. Submissions need a primary paper source, inclusion evidence and aligned English/Chinese descriptions.

Format references: [five high-star collections and the patterns adapted here](research/reference-format-audit-2026-09-08.md). Stars informed sample selection, not paper inclusion.

## License

This index is released under the [MIT License](LICENSE). Linked papers and artifacts retain their original licenses.
