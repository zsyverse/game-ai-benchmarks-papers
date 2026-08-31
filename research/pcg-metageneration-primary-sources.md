# Procedural content metageneration: verified primary sources

> Verified through: **2026-08-31** (Asia/Shanghai). This note follows the
> generator lineage in which search, interaction, or optimization produces a
> reusable content generator rather than only one level. Playing or solving
> agents are in scope only when they evaluate generated content.

## Classification and artifact rules

- **Core metageneration:** the output of the outer process is a reusable
  generator, generator program, or compact example that acts as a stochastic
  generator.
- **Generator tuning:** the outer process selects parameters of a fixed
  generator but does not synthesize a new program structure. This is retained
  as a boundary case.
- **Generator language:** a language or runtime in which humans author
  generators. This can be a necessary predecessor without itself being a
  metagenerator.
- A public repository without a license is described as **public source**, not
  unqualified “open source.” The paper may use the latter phrase, but the
  repository state controls the artifact note here.
- **Open research snapshot** means that the central author-released
  implementation and meaningful outputs are public, even if packaging is
  weak. **Partial** means that useful source exists but the paper's full
  experiment cannot be reproduced from the release. **Closed** means that no
  paper-specific implementation or data release was verified.

## At-a-glance lineage

| Year | Work | Role in the lineage | Strict core? | Recommended version treatment |
| :---: | --- | --- | :---: | --- |
| 2012 | Compositional Procedural Content Generation | Evolution searches parameters of an ASP dungeon generator | Yes | Standalone paper; do not merge with PPLGG |
| 2012 | A Procedural Procedural Level Generator Generator | Interactive evolution synthesizes agent-based Mario generators | Yes | Standalone paper and implementation |
| 2016 | Danesh | Tunes parameters of an existing generator | Boundary | Standalone generator-tuning/infrastructure entry |
| 2017 | Marahel | Language/runtime for human-authored constructive generators | No | Standalone predecessor or a linked precursor |
| 2019 | Optimising Level Generators for General Video Game AI | A Meta Generator searches parameterized GVGAI generators | Yes | Standalone paper; base GVGAI is only infrastructure |
| 2020 | Multi-Objective Level Generator Generation with Marahel | NSGA-II evolves Marahel generator programs | Yes | Merge arXiv v2 and ACM DOI as one publication family |
| 2026 | Evolutionary Wave Function Collapse | Evolution produces small WFC examples that act as generators | Yes | Standalone follow-up; do not merge with generic WFC |

## 1. Compositional Procedural Content Generation

### Bibliographic record

- **Authors:** Julian Togelius, Tróndur Justinussen, Anders Hartzen.
- **Venue/year/pages:** Third Workshop on Procedural Content Generation in
  Games, 2012, pp. 1–4.
- **Primary record:** [ACM DOI](https://doi.org/10.1145/2538528.2538541).

### Generated object and method

The paper presents an evolutionary–ASP composition for a fictional roguelike.
The outer genotype contains 17 discrete values, including map size, entrance
and exit coordinates, path-length constraints, trap and monster counts, open
tiles, and buff counts. These values are substituted into an Answer Set
Programming file. Running the resulting ASP program can produce many
dungeons, so the parameterized ASP program is the generated **inner dungeon
generator**, not merely one generated level.

The ASP layer guarantees that returned dungeons are complete, well formed,
and winnable. A \(\mu+\lambda\) elitist evolution strategy is the outer search
and optimizes properties that are less convenient to express as hard
constraints.

### Evaluation

- For each candidate generator, the ASP solver's first 20 dungeons are
  evaluated and their fitness is averaged.
- A reckless A*-based agent follows the shortest path, while a smarter agent
  avoids hazards and collects nearby buffs. Their path and damage outcomes
  approximate challenge and skill differentiation.
- The reported configuration uses \(\mu=30\), \(\lambda=30\), with per-locus
  mutation probability 0.3. The example run shown in the paper reaches a
  plateau after roughly 40 generations.
- This is a small proof-of-concept experiment, not a multi-domain benchmark or
  human study.

The agents are therefore **generated-dungeon evaluators**. The paper is not a
playing-agent contribution.

### Artifacts and license

- No paper-specific implementation, ASP program, generated-dungeon corpus,
  seeds, or evaluation harness was verified.
- The paper refers to an earlier example ASP maze program, but that upstream
  example is not a release of this experiment.
- **Status:** **Closed.** There is no verified code or data license because no
  paper-specific artifact release was found.

### Split/merge judgment

This is a direct conceptual predecessor of PPLGG, and the PPLGG paper itself
describes both systems as compositional or “procedural procedural content
generator generators.” It must nevertheless remain separate: it has different
authors, a roguelike domain, ASP representation, automatic numerical fitness,
and constraint guarantees. PPLGG instead evolves agent populations for Mario
under interactive selection.

## 2. A Procedural Procedural Level Generator Generator (PPLGG)

### Bibliographic record

- **Authors:** Manuel Kerssemakers, Jeppe Tuxen, Julian Togelius, Georgios N.
  Yannakakis.
- **Venue/year/pages:** IEEE Conference on Computational Intelligence and
  Games, 2012, pp. 335–341.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2012.6374174),
  [University of Malta repository record](https://www.um.edu.mt/library/oar/handle/123456789/29696),
  [institutional full text](https://www.um.edu.mt/library/oar/bitstream/123456789/29696/1/A_procedural_procedural_level_generator_generator.pdf),
  [author repository](https://github.com/ManuelKers/PPLGG).

The University of Malta metadata also contains the unrelated identifier
`10.1109/CIG.2012.6374098`. Crossref, IEEE, the paper pagination, and the title
record agree on **10.1109/CIG.2012.6374174**, which is the identifier that
should be used.

### Generated object and method

PPLGG uses an interactive genetic algorithm to evolve reusable Super Mario
Bros. level generators. Each inner generator is a collection of approximately
14–24 parameterized drawing agents. Agent parameters control spawn time and
position, lifetime/tokens, movement, triggers, boundary behavior, and tile
placement actions. Because agent behavior is stochastic, one evolved
collection generates arbitrarily many related levels rather than encoding one
fixed map.

The interface presents generator-level cloud maps, individual level samples,
a playable game view, and a simulation-based playability estimate. The human
selects one or more preferred generators as parents; crossover exchanges
whole agents, while mutation changes, adds, or removes agents.

### Evaluation

- The interface samples ten levels from a generator and lets Robin
  Baumgarten's A*-based Mario agent attempt them. The playability estimate is
  the mean proportion of those levels traversed before death.
- An offline initialization phase evaluates three levels per candidate and
  evolves for at most 100 generations to seed a database with generators that
  tend to produce playable levels.
- The paper labels its main evaluation an **informal self-evaluation by the
  designers**. It discusses perceived control and user fatigue, but does not
  report a controlled external user study.
- Diversity is examined qualitatively both among outputs of one generator and
  between generators. The paper argues that outputs can vary locally while
  retaining recognizable generator-specific style.
- Performance testing samples 100 levels from each of 100 randomly initialized
  generators and also tests viable database generators at several widths.
  Ordinary 300-block levels are reported at more than 20 generations per
  second on the test laptop.

The Mario agent is used only to evaluate generated levels. The research object
is the generator and its outputs, not the agent's game-playing score.

### Artifacts and license

- The author repository exposes Java source for the agents, genetic algorithm,
  GUI, Mario integration, and generator fitness classes.
- The repository was created in November 2011 and last pushed in December
  2011, before the 2012 publication. It is credible implementation evidence,
  but it is not a packaged archival reproduction of every reported experiment.
- The root `README` is empty. There is no detected license, tagged release,
  dependency/build guide, paper seed database, result corpus, or reproduction
  script.
- **Status:** **Partial, legacy public source.** Public visibility does not
  grant a reusable software license.

### Split/merge judgment

No separate peer-reviewed precursor or journal extension was verified. The
repository is an implementation artifact, not another publication version.
PPLGG should be one standalone row and should link, but not merge with,
Compositional PCG.

## 3. Towards the Automatic Optimisation of Procedural Content Generators

### Bibliographic record

- **Authors:** Michael Cook, Jeremy Gow, Simon Colton.
- **Venue/year/pages:** IEEE Conference on Computational Intelligence and
  Games, 2016, pp. 1–8.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2016.7860424),
  [institutional author manuscript](https://research.gold.ac.uk/id/eprint/18950/1/Cook_CIG2016.pdf),
  [author code repository](https://github.com/gamesbyangelina/Danesh).

### Generated object and method

Danesh is a Unity/C# analysis and development tool attached to an existing
procedural generator. Users annotate generation, visualization, metric, and
parameter functions. The tool can then visualize expressive range, identify
fields whose changes materially affect output metrics, and automatically
search a selected parameter space toward target metric values.

The paper's running example is a cellular-automata cave generator. Danesh
tests random search, hill climbing, and evolutionary search over its parameter
configurations. The output of this outer process is a **tuned configuration of
a fixed generator**, not newly synthesized generator code or rule structure.

### Evaluation

- The cave example uses connectedness, density, openness, jaggedness, and wall
  distribution metrics.
- Automatic field identification compares 20 generated samples at baseline
  and test values, flagging fields when the mean metric changes by more than
  one baseline standard deviation.
- Parameter search is tested in three scenarios: two parameters/two metrics,
  two parameters/three metrics, and four parameters/four metrics.
- Random search and hill climbing use 15 samples per test over 100 iterations;
  evolutionary search uses population 15 for 15 generations. Each scenario is
  run five times with time and target-fitness comparisons.
- Random search responds quickly, while hill climbing and evolution can be
  better for high-fitness refinement in the hardest case. No algorithm reaches
  the deliberately unreachable 0.95 target in the second scenario.
- A survey of 53 game developers motivates the interface—85% reported manual
  parameter adjustment and output inspection—but the paper does not report a
  completed user evaluation of Danesh itself.

### Artifacts and license

- The author repository contains a Unity project with `Assets`,
  `ProjectSettings`, and a short README. It was last pushed in March 2016.
- The paper calls Danesh open source, but the public repository has no detected
  license file or GitHub-recognized license. Redistribution rights should not
  be inferred from repository visibility.
- No frozen experiment result package or maintained modern Unity release was
  verified.
- **Status:** **Partial, legacy public source.** The central tool code exists,
  but licensing and turnkey experimental reproduction are incomplete.

### Split/merge and scope judgment

Danesh cites PPLGG but is not a version of it. Its generic fixed-generator
parameter tuning is an important adjacent step toward metageneration, yet it
does not create a new generator representation. In a strict index it belongs
under `generator-tuning` or infrastructure/boundary rather than the core
generator-generating-generator count.

## 4. Marahel: A Language for Constructive Level Generation

### Bibliographic record

- **Authors:** Ahmed Khalifa, Julian Togelius.
- **Venue/year/pages:** Proceedings of the AAAI Conference on Artificial
  Intelligence and Interactive Digital Entertainment 13(2), 2017, pp. 84–91.
- **Primary sources:** [AAAI DOI](https://doi.org/10.1609/aiide.v13i2.12970),
  [AAAI full text](https://ojs.aaai.org/index.php/AIIDE/article/download/12970/12818),
  [author repository](https://github.com/amidos2006/marahel).

### Generated object and method

Marahel is a constructive language and JavaScript/TypeScript framework for 2D
tile-based level generators. A script declares metadata, entities, optional
regions and neighborhoods, and sequential “explorers” that visit and modify
tiles through conditions and actions. Each hand-authored Marahel script is a
reusable stochastic generator.

This paper does **not** automatically generate the scripts. Its stated second
motivation is to create a generator space that could later be searched by
evolution, which the 2020 paper implements.

### Evaluation

- The paper defines five generators and samples their maps.
- Their expressive ranges are analyzed along percentage of empty space,
  number of isolated elements, and cell-wise entropy of empty space.
- The result demonstrates that compact Marahel definitions can express
  generators with strongly different output distributions. It is not a
  benchmark of automatically discovered generators.

### Artifacts and license

- The official repository provides the framework, compiled browser library,
  language documentation, and examples.
- The repository has no detected license file or GitHub-recognized license.
  It is therefore author-released public source, not safely redistributable
  under a stated open-source license.
- **Status:** **Open implementation with a license caveat.** The language's
  central runtime and documentation are public; this paper does not claim a
  separate training dataset or search pipeline.

### Split/merge judgment

Marahel 2017 is the direct representation-language predecessor of Marahel
2020, but the generated objects differ materially: humans author generators
in 2017, whereas evolution generates the generator programs in 2020. For a
fine-grained index they should be separate, cross-linked rows. A compact index
may link 2017 as a precursor inside the 2020 row, but it should not describe
the two as conference/journal versions of one paper.

## 5. Optimising Level Generators for General Video Game AI

### Bibliographic record

- **Authors:** Olve Drageset, Mark H. M. Winands, Raluca D. Gaina, Diego
  Pérez-Liébana.
- **Venue/year/pages:** IEEE Conference on Games, 2019, pp. 1–8.
- **Primary sources:** [IEEE DOI](https://doi.org/10.1109/CIG.2019.8847961),
  [Maastricht University publication record](https://cris.maastrichtuniversity.nl/en/publications/optimising-level-generators-for-general-video-game-ai/),
  [institutional full text](https://cris.maastrichtuniversity.nl/files/95969450/Winands_2019_Optimising_level_generators_for_general.pdf),
  [official GVGAI framework](https://github.com/GAIGResearch/GVGAI).

### Generated object and method

The paper introduces a parameterized constructive level generator inside
GVGAI and a **Meta Generator** that applies genetic parameter search over such
generators. A candidate is evaluated through several levels sampled from the
parameterized generator, so the outer search targets a reusable generator
rather than directly evolving a single fixed map.

The tested games are Butterflies, Freeway, and The Snowman. The contribution
also includes a comparison baseline for GVGAI level generators and a composite
level-fitness function based on AI play-testing.

### Evaluation

- The Meta Generator is compared with random and constructive level-generator
  baselines on all three games.
- The composite evaluator derives properties of generated levels through AI
  play-testing. Game-playing is therefore an evaluation instrument for
  generated content.
- The paper reports the Meta Generator as on par with or better than the
  baselines depending on the game; it does not claim uniform dominance.
- The authors state their intention to submit the Meta Generator to the 2019
  GVGAI Level Generation competition. That future-tense statement is not
  evidence of a preserved competition submission.

### Artifacts and license

- The base GVGAI repository is public and its `LICENSE.txt` specifies GNU GPL
  version 3 or later.
- The current official repository tree exposes general random, constructive,
  and genetic level-generator infrastructure, but no paper-identified Meta
  Generator implementation or experiment package was verified.
- No paper-specific parameter sets, generated levels, run logs, or evaluation
  data release was found.
- **Status:** **Closed for the paper-specific method.** The GPL-licensed GVGAI
  framework is upstream infrastructure, not sufficient evidence that the Meta
  Generator experiment is reproducible.

### Split/merge judgment

This is a distinct, explicit metageneration contribution and a direct
predecessor cited by Marahel 2020. It should not be merged with the broad
GVGAI framework paper or repository: the framework contains playing, rule,
and level-generation tracks, while this paper's scoped contribution is the
Meta Generator and its generated-level evaluator.

## 6. Multi-Objective Level Generator Generation with Marahel

### Bibliographic record

- **Authors:** Ahmed Khalifa, Julian Togelius.
- **Venue/year/pages:** International Conference on the Foundations of Digital
  Games / PCG Workshop, 2020, pp. 1–8.
- **Primary sources:** [ACM DOI](https://doi.org/10.1145/3402942.3409606),
  [arXiv record](https://arxiv.org/abs/2005.08368),
  [experiment repository](https://github.com/amidos2006/marahel-evolution),
  [Marahel framework](https://github.com/amidos2006/marahel).

### Generated object and method

The outer NSGA-II search evolves compact Marahel programs. A chromosome has
102 integers: one controls the number of explorers, one is a random seed, and
five blocks of 20 integers can describe explorers. A context-free grammar and
Tracery map the integers to a restricted subset of the Marahel language.

Each resulting script is itself a constructive generator for one of three 2D
domains:

- **Binary:** maze-like maps whose empty cells should be connected and whose
  longest path should improve over the random initial map.
- **Zelda:** maps with player, key, door, enemies, reachability, and path-length
  requirements.
- **Sokoban:** maps with player, crates, targets, count consistency, and
  solution-length requirements.

Solving and pathfinding are used to score generated maps; the paper is not
about learning a policy that plays a fixed game.

### Evaluation

- NSGA-II uses population 500 for 2,000 generations, with crossover rate 0.7
  and mutation rate 0.3.
- Fitness for one candidate generator is the average over 50 sampled maps.
- The analysis compares final Pareto fronts and examples with 500 randomly
  sampled generators.
- In Binary, the restricted representation cannot simultaneously reach the
  preferred connectivity and path-improvement extremes, producing a clear
  trade-off.
- Zelda and Sokoban improve on many component objectives, but full playability
  remains difficult. The evolved scripts often depend on a favorable random
  initialization and erase or preserve it rather than constructing the whole
  layout robustly.
- The paper explicitly identifies the averaging operator, restricted language,
  and initialization explorer as limitations and future experimental targets.

### Artifacts and license

- The official experiment repository contains NSGA-II and MAP-Elites code,
  parsers, domain evaluators, Marahel/Tracery runtimes, parameter grammars, and
  best Binary, Zelda, and Sokoban scripts/chromosomes.
- The repository is a single 2020 research snapshot. It has no README,
  dependency manifest, tagged release, or detected license.
- The separate Marahel repository supplies the maintained language runtime and
  documentation, but it also has no detected license.
- **Status:** **Open research snapshot with license and packaging caveats.**
  The central author code and representative outputs are public, but reuse
  rights and turnkey commands are not documented.

### Split/merge judgment

The [arXiv version](https://arxiv.org/abs/2005.08368) reached v2 in July 2020
and corresponds to the eight-page ACM publication. They should be one row.
Marahel 2017 is a distinct predecessor, not an earlier version of this paper.
Compositional PCG, PPLGG, and the 2019 GVGAI Meta Generator are independent
prior systems and should only be cross-linked.

## 7. Evolutionary Wave Function Collapse

### Bibliographic record

- **Authors:** Dipika Rajesh, Ahmed Khalifa, Julian Togelius.
- **Venue/year:** accepted short paper at IEEE Conference on Games 2026; arXiv
  v1 posted 2026-07-02.
- **Primary sources:** [arXiv record](https://arxiv.org/abs/2607.02082),
  [full text](https://arxiv.org/pdf/2607.02082).
- No DOI or final IEEE record was verified at the cutoff; the arXiv record says
  “accepted at CoG 2026.”

### Generated object and method

Evolutionary WFC evolves a compact 4×4 tile image rather than a finished
level. WFC extracts 2×2 patterns from that image and stochastically expands
them into larger outputs. The small image therefore acts as a reusable WFC
**generator genotype** and WFC is the genotype-to-phenotype mapping.

The method is evaluated in two domains: 8×8 connectivity mazes and 16×16
Zelda-style layouts. It directly cites PPLGG 2012 and Marahel 2020 as prior
work on searching for generators rather than individual levels.

### Evaluation

- Evolution uses population 10 for 100 generations with tournament selection,
  adaptive mutation, and elitism.
- Random search uses the same 1,000 genotype evaluations as the baseline.
- Maze fitness rewards a single connected traversable region and long paths.
  Zelda fitness combines entity-count targets with reachability and path
  structure, using metrics from the PCG Benchmark.
- Evolutionary search produces a clear improvement over random search in the
  Maze domain, where local WFC patterns can support global connectivity.
- It also improves Zelda layouts, but the gap is smaller and exact global
  constraints—one player, key, and door—remain difficult for a local-pattern
  model.
- Each genotype is evaluated from only one stochastic WFC generation. The
  paper flags this noisy estimate and the lack of explicit global constraints
  as limitations.

### Artifacts and license

- The paper links the generic upstream WFC implementation and the PCG
  Benchmark as dependencies/references, but neither is an implementation of
  this evolutionary method.
- No author-released Evolutionary WFC code, genotype set, generated-level
  corpus, run logs, or experiment data was verified.
- **Status:** **Closed.** There is no paper-specific software or data license
  to report.

### Split/merge judgment

This is a direct 2026 follow-up to the PPLGG/Marahel generator-search line and
is a strong core-metageneration inclusion. It should remain separate from the
generic WaveFunctionCollapse boundary resource: the latter supplies a generic
constraint technique, while this paper evolves WFC inputs as game-level
generators and evaluates them in two game domains. It is also separate from
the 2026 paper *Procedural Content Metageneration via Program Search and
Continual Abstraction Discovery*, which evolves complete Python generator
programs rather than WFC examples.

## Final scope and inclusion judgment

### Core generator-generating-generator papers

The high-confidence core set in this note is:

1. *Compositional Procedural Content Generation* (2012).
2. *A Procedural Procedural Level Generator Generator* (2012).
3. *Optimising Level Generators for General Video Game AI* (2019).
4. *Multi-Objective Level Generator Generation with Marahel* (2020).
5. *Evolutionary Wave Function Collapse* (2026).

Marahel 2017 is a necessary generator-language predecessor. Danesh 2016 is a
useful generator-tuning boundary system. Neither should be described as
playing-game research.

### Strict playing-paper exclusion check

- PPLGG's Mario A* agent estimates generated-level playability.
- Compositional PCG's two A* agents estimate challenge and skill
  differentiation of generated dungeons.
- The GVGAI Meta Generator uses AI play-testing inside a generated-level
  fitness function.
- Marahel 2020 and Evolutionary WFC use pathfinding or puzzle/game constraints
  to score generated maps.

In every case, the agent or solver is subordinate to generation evaluation.
None has policy return, win rate, or fixed-game control as its main research
output.
