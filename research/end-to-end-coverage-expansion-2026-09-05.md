# End-to-end coverage expansion — 2026-09-05

This pass extends the 2026-09-04 index using primary papers and author-linked releases. It does not reverify every previously accepted entry or claim an exhaustive literature census.

## Discovery

Queried the arXiv Atom API for `ti:"game generation"`, `ti:"game development" AND (all:LLM OR all:"large language")`, game/benchmark titles with generation terms, `game synthesis`, `text-to-game`, and executable code/rules. Broader title searches returned up to 180 records; mathematical game theory, agent-playing benchmarks and already indexed paper identities were screened out. Followed methods, evaluation, limitations and artifact links in candidate full texts. Google search requests returned JavaScript-only pages, so they supplied no evidence. This pass is strongest for arXiv and author-linked material; conference-only and industrial work remain possible omissions.

## Accepted additions

### Mage: Multi-Axis Evaluation of LLM-Generated Executable Game Scenes Beyond Compile-Pass Rate

- Primary source: [paper](https://arxiv.org/abs/2605.07342), [full text](https://arxiv.org/html/2605.07342), 2026 preprint. Do not describe the submission as an accepted NeurIPS paper.
- Sections 3–5 define 26 complete Unity 2D goal-pattern scenes, two extracted IR conditions plus a natural-language baseline, four models, three seeds and 858 actual generation attempts. One model/condition is omitted for context overflow; 936 is the theoretical factorial total, not the observed sample size.
- Section 4 defines compilation, runtime initialization, structural fidelity and mechanism adherence. Mechanism adherence uses static condition-path extraction; runtime success checks `Awake()` and clean exit. Section 7 explicitly says runtime playability is not measured. Neither runtime-pass nor structural F1 establishes that a player can win. Structural F1 uses only runtime-pass outputs, with varying denominators; static mechanism paths use all 858 attempts. Section 5.2.1/Table 3 explains the no-schema win-path floor of 0.12 by three empty reference paths out of 26 and F1(empty, empty)=1, not observed gameplay correctness.
- This is a formal generation benchmark with tasks, ground truth, an evaluator and generator comparisons, unlike a metric-only study or ordinary repository repair benchmark.
- Verified the paper-linked [code release](https://anonymous.4open.science/r/neurips-ir-benchmark-game-scene-3F65/) and [data release](https://huggingface.co/datasets/anon-neurips-2026-0502/scene-level-grounding-benchmark). The data API exposes patterns, ground-truth representations, IR, outputs, logs and metrics. Read the code README, `reproduction/run_eval_only.sh`, `m1_funnel.py` and evaluation pipeline; these are substantive artifacts, not a placeholder. **Open**, with Unity/HPC requirements and local-path configuration caveats; reproduction was not executed.
- Deduplication: the paper's earlier working title, “Scene-Level Grounding …”, is the same release and gets no separate record. The July compiler-error census is a distinct analysis, but was not added merely because it reuses the task family.

### Developing a Scenario-Based Video Game Generation Framework: Preliminary Results

- Primary source: [paper](https://arxiv.org/abs/1911.07380), [full text](https://arxiv.org/html/1911.07380), 2019.
- Sections II–III map practitioner-defined **linear** scenarios and workflow/state diagrams to Unity interactions. Goals, scoring and workflow are authored; player decisions do not change outcomes and errors deduct points. Assets are substituted by tags after primitive-object flow tests. This instantiates bounded authored scenarios, not open-ended game synthesis. Hospital and BioGarden are generated as runnable serious-game prototypes, with task outcomes and state transitions, rather than only scene assets or a proposed framework.
- Results compare the generated and manually developed versions on CPU, memory, rendering and development effort. Generation takes 3.5 and 4 hours after a three-week generator implementation. These small-case timings do not establish a general speedup; user/learning-outcome evaluation is future work.
- **Closed**: inspected primary text did not expose a verified paper-specific generator/reproduction release. Existing commercial simulation tools and Unity assets are dependencies, not this paper's code.

### Pharos Night: Crown Pursuit

- Primary source: [paper](https://arxiv.org/abs/2608.12216), 2026. arXiv HTML was unavailable; downloaded the primary PDF and inspected methods, implementation and playtest sections with text extraction.
- Sections 3.2, 3.3 and 4.2 explain actual rule execution: player materials and free-text spells produce JSON selecting and composing preconditions, actions, triggers and effects. Unity parses this into card objects and executes the resulting combinations during combat. Numeric strengths come from designer-defined levels.
- It qualifies specifically as bounded executable mechanic generation inside an existing game. It is not a from-scratch whole-game generator or unrestricted synthesis of arbitrary new code. NPC behavior is an additional feature and is not the inclusion basis.
- Section 5 reports an exploratory 13-person playtest with questionnaires and open-ended feedback. The study concerns the combined experience, so it does not isolate the causal effect of the generator or supply a formal generation benchmark.
- **Closed**: no official implementation, build or study package was verified in the paper or the targeted repository search.

## Exclusions and unresolved leads

| Candidate | Primary source | Decision |
| --- | --- | --- |
| S3Gym | [paper](https://arxiv.org/abs/2608.31100) | Agent self-improvement in seven text games; evaluated product is the agent policy, not game generation. |
| AgentOdyssey | [paper](https://arxiv.org/abs/2606.24893) | Generated games serve continual-learning agent evaluation; no demonstrated central generation benchmark. |
| Beyond Asking | [paper](https://arxiv.org/abs/2608.16196) | Core contribution is player-trait inference and difficulty adaptation, not substantial game generation. |
| Code World Models for General Game Playing | [paper](https://arxiv.org/abs/2510.04542) | Generated code supports MCTS and the main comparison is agent playing strength. Distinguish the already indexed subsequent generator-training paper. |
| Knowledge-Conditioned, Single-Pass LLM Synthesis … | [paper](https://arxiv.org/abs/2607.10187) | Error-census analysis of existing generators; abstract reports no runnable scene in 10,400 attempts. Do not add automatically alongside Mage without a distinct qualifying method/benchmark contribution. |
| High-quality generation of dynamic game content via small language models | [full text](https://arxiv.org/html/2601.23206) | Section 3.1 generates smear-campaign prose/posters; reputation updates are fixed non-AI logic. The evaluated output is text, not newly executable mechanics. |
| LLM-Assisted Refactoring and Gameplay Feature Generation in an Endless Runner | [paper](https://arxiv.org/abs/2606.21171) | Six local modifications in an existing Pygame system, excluded repository-patch scope. |
| Bridging Pedagogy and Play | [paper](https://arxiv.org/abs/2603.03644) | Structured co-design language/interface; playable generation and generator experiments were not established from the inspected abstract. |

The separate 2023 controllable co-creative system was also inspected in full: its evolutionary generator produces executable component/state/resource-flow designs and evaluates approximately 33,000 simulator-feasible rule designs, not finished human-playable games. It is assigned to the PCG rule-generation section, with evidence recorded in the [classic-game expansion](classic-game-coverage-expansion-2026-09-05.md).

## Limits

One existing metadata correction: **General Video Game Rule Generation** was published at CIG **2017**, DOI [10.1109/CIG.2017.8080431](https://doi.org/10.1109/CIG.2017.8080431). Crossref's publisher-registered title, authors and publication date match the [arXiv record](https://arxiv.org/abs/1906.05160), which was uploaded in 2019. Both public rows and the canonical dossier now use publication year 2017; no extra record is counted.

Search saturation in the targeted end-to-end queries mostly returned existing records and out-of-scope agent, metric and patch studies. The three accepted additions fill identifiable gaps; they are not a claim that only three papers were missing. Artifact availability was checked on 2026-09-05, without running third-party code or reproducing published results.
