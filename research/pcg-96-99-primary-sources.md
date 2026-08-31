# Primary-source audit: PCG candidates 96–99

> Audit cutoff: **2026-08-31 (Asia/Shanghai)**. This note checks the four records against papers, official proceedings, and author-associated repositories. Search engines and scholarly indexes were used only for discovery; every claim below is tied to a primary source.

## Decision

All four works belong in a **game-generation** bibliography. Their output is a game level, not a policy for playing an existing level. Some papers use an agent or pathfinder to create a training signal, optimize a generator, or test playability; that does not change the generated artifact.

| # | Work | Generated artifact | Include? | Artifact status | Main qualification |
| --- | --- | --- | --- | --- | --- |
| 96 | *Autoencoder and Evolutionary Algorithm for Level Generation in Lode Runner* | Lode Runner levels | **Yes** | **Partial** | An author-associated code/data repository exists, but it is unlicensed, unpinned, and does not reproduce the paper configuration without repair. |
| 97 | *Generating Game Levels for Multiple Distinct Games with a Common Latent Space* | Paired levels for four games | **Yes** | **Closed** | The paper reports a substantial benchmark, but supplies no repository link and no first-party implementation or data release was found. |
| 98 | *Learning to Generate Levels From Nothing* | Zelda levels | **Yes** | **Partial** | MIT-licensed training code and a paper configuration are public; checkpoints, result artifacts, tests, and a locked environment are absent. |
| 99 | *Mutation Models: Learning to Generate Levels by Imitating Evolution* | Binary maze levels | **Yes** | **Partial** | Author code/configuration is public, but the current repository has drifted beyond the paper and omits the trained models, datasets, results, license, and exact environment. |

Status is based on the release observable at cutoff:

- **Open**: the central paper artifact and a substantially complete, documented reproduction path are public.
- **Partial**: a first-party or author-associated artifact is public, but material inputs, outputs, licensing, or reproduction details are missing.
- **Closed**: no first-party implementation/data/model artifact was identifiable; the paper itself may still be freely readable.

These labels describe public artifact completeness, not research quality.

## 96. Autoencoder and Evolutionary Algorithm for Level Generation in Lode Runner

### Bibliography and scope

- Sarjak Thakkar, Changxing Cao, Lifan Wang, Tae Jong Choi, and Julian Togelius.
- IEEE Conference on Games (CoG), London, 20–23 August 2019.
- DOI: [10.1109/CIG.2019.8848076](https://doi.org/10.1109/CIG.2019.8848076).
- Primary records: [IEEE record](https://ieeexplore.ieee.org/document/8848076), [official CoG proceedings](https://ieee-cog.org/2019/proceedings/), and [official conference PDF](https://ieee-cog.org/2019/papers/paper_232.pdf).

**Include.** The system decodes latent vectors into new Lode Runner level layouts and evolves them toward playable, connected maps. A* is a feasibility evaluator inside the generation loop, not a game-playing contribution.

### Method and reported evidence

- The source corpus contains **150** Lode Runner levels, represented with five channels for bricks, ladders, ropes, enemies, and gold. The paper describes the playable area as **22 × 32**; the released notebooks use **24 × 32 × 5**, consistent with adding a boundary/padding representation but not explicitly documented as such.
- Horizontal flipping expands the 150 source levels to **300 training examples**.
- The autoencoder/VAE experiments use latent dimension **16**, learning rate **0.001**, and **1,000 epochs**. The decoder is sampled to form **10,000 candidate levels**.
- Evolution uses **10 independent populations**, population size **32**, crossover probability **0.78**, mutation probability **0.1**, and **150 generations**. Crossover operates on level patches and mutation perturbs the latent representation.
- A* checks whether all gold is collectible; connectivity is the fraction of reachable coordinates. The paper explicitly reports that most raw autoencoder outputs are not playable before evolution.
- For **330 generated levels** compared tile-by-tile with the original corpus:
  - VAE: mean similarity **25.36%**; **73/330** exceed 30% similarity and **3/330** exceed 50%.
  - Vanilla AE: mean similarity **27.05%**; **130/330** exceed 30% and **38/330** exceed 50%.
- The authors characterize the VAE output as denser and more complex/difficult, and the vanilla AE output as sparser and simpler. These are paper conclusions, not an independently replicated user study.

### Artifact audit

The previously missed artifact is [StarryBar/level-generation-for-lode-runner](https://github.com/StarryBar/level-generation-for-lode-runner). It is strongly author-associated: commits are attributed to “Lifan,” matching coauthor Lifan Wang, and its first commit predates the conference. The paper does not itself link the repository, so “author-associated” is more precise than “official archival release.”

Observed contents include:

- [`AE_16.ipynb`](https://github.com/StarryBar/level-generation-for-lode-runner/blob/master/AE_16.ipynb), [`VAE_16.ipynb`](https://github.com/StarryBar/level-generation-for-lode-runner/blob/master/VAE_16.ipynb), and [`VAE_4.ipynb`](https://github.com/StarryBar/level-generation-for-lode-runner/blob/master/VAE_4.ipynb);
- [`astar.py`](https://github.com/StarryBar/level-generation-for-lode-runner/blob/master/astar.py);
- two NumPy level-data files and level visualizations.

Material limitations:

- no LICENSE (`license: null` in the GitHub repository metadata), release, tag, or archived commit named by the paper;
- no dependency manifest, environment lock, checkpoint, seed record, result bundle, or automated test;
- notebooks contain absolute Windows paths and use legacy TensorFlow 1 APIs;
- a notebook sets `n_iterations = 10`, whereas the paper reports 150 evolutionary generations;
- the repository README is only a title and does not explain the 22 × 32 versus 24 × 32 representation difference.

**Final status: Partial.** There is meaningful code and source data, so Closed would be wrong. The missing license/environment/results and configuration mismatch make Open too strong.

## 97. Generating Game Levels for Multiple Distinct Games with a Common Latent Space

### Bibliography and scope

- Vikram Kumaran, Bradford W. Mott, and James C. Lester.
- AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE) 2020, volume 16, issue 1, pp. 109–115.
- Canonical DOI: [10.1609/aiide.v16i1.7485](https://doi.org/10.1609/aiide.v16i1.7485).
- Primary records: [official article page](https://ojs.aaai.org/index.php/AIIDE/article/view/7485) and [official PDF](https://ojs.aaai.org/index.php/AIIDE/article/download/7485/7346).

**Include.** The model generates level tensors for four games from one shared latent vector. Agents are used to solve generated levels and measure cross-game gameplay correspondence; the research output remains generated content.

### Method and reported evidence

- A branched DCGAN has a shared latent trunk, four game-specific generator branches, and four discriminators.
- Training examples are aligned across **Boulderdash, Link, Zelda, and Roguelike** by deriving four corresponding levels from a common gameplay-action sequence.
- Each output is **16 × 16** with **nine sprite channels**. The input is a **128-dimensional Gaussian** vector.
- The training set contains **5,000 aligned four-game groups**. Training uses batch size **64**, **600–1,200 epochs**, one GPU, and **30% discriminator dropout**.
- Solvability is evaluated on **50 generated levels per game**. An agent gets up to five attempts of at most **2,000 ticks** each; one successful attempt marks a level solvable. Figure 7 reports:
  - Boulderdash: **70%**;
  - Link: **52%**;
  - Roguelike: **54%**;
  - Zelda: **40%**.
- Cross-game gameplay similarity is measured from Manhattan distances between ideal paths. The generated condition has Wasserstein distance **161** from the training distribution, versus **283** for a random baseline.
- The novelty experiment compares pairwise Levenshtein distances between solution-action sequences for **100 training and 100 generated levels per game**. The paper presents distributions and a qualitative conclusion that they are similar; it does **not** report one scalar “novelty score.”

### DOI de-duplication

The AAAI OJS also exposes [10.1609/aiide.v15i1.7418](https://doi.org/10.1609/aiide.v15i1.7418) with 2019/volume-15 metadata and pp. 102–108. Its downloadable PDF is byte-identical to the canonical 2020 article PDF (SHA-256 `edf18154036a3bbe8f625079bcea6d0016ac9efb6970977e27e17fd179f1e02e`). The PDF itself says copyright 2020 and pp. 109–115. Treat this as a duplicate/misregistered record, **not a second paper**; retain only `10.1609/aiide.v16i1.7485` in the bibliography.

### Artifact audit

The official paper and article page contain no code/data URL. At cutoff, exact-title/DOI searches and author/institution repository checks did not identify a first-party implementation or release. In particular, Bradford Mott's public GitHub account and the NC State IntelliMedia organization do not expose a repository matching the paper. Absence from a public search cannot prove that no private or differently named artifact exists; it does establish that no citable public first-party artifact was identifiable.

**Final status: Closed.** Retain the paper's reported protocol and results, but do not imply that its paired 5,000-example dataset, model, checkpoints, or evaluator are downloadable.

## 98. Learning to Generate Levels From Nothing

### Bibliography and scope

- Philip Bontrager and Julian Togelius.
- IEEE Conference on Games (CoG) 2021, pp. 1–8.
- DOI: [10.1109/COG52621.2021.9619131](https://doi.org/10.1109/COG52621.2021.9619131).
- Primary preprint: [arXiv:2002.05259](https://arxiv.org/abs/2002.05259).

**Include.** A Generative Playing Network (GPN) generates Zelda levels. The player learns on those levels while the generator adapts difficulty toward the player's learning frontier. Playing is the generator's training signal rather than the paper's final artifact.

### Method and reported evidence

- The generator aims to make the player's expected reward approximately zero, corresponding to roughly a **50% win rate** under the paper's reward formulation. This is an optimization target, not a reported held-out level-success statistic.
- The domain is the GVGAI Zelda 2D dungeon crawler, represented as **12 × 16 × 14** tensors.
- The generator samples a **512-dimensional Gaussian latent vector**. The player is a nine-layer residual network plus GRU with a 512-dimensional encoding.
- The paper studies (1) fully self-supervised training from no human levels and (2) a semi-supervised variant using **five human-authored levels** for pretraining/elitism.
- Training runs for **50 million frames**. Reported configuration details include minibatch **128**, 10 generator updates, 90 diversity updates, 20 million pretraining steps, 16 parallel workers, 30% elite environments, and sampling a human level for 50% of episodes in the semi-supervised condition.
- The paper displays random samples after 50 million frames and says those displayed levels are playable/winnable, but it gives no independent large-sample success percentage or scalar diversity score. It also reports convergence toward a single design after 50 million frames and that the learned levels are simple for humans. The figures must not be summarized as “100% of generated levels are solvable.”

### Artifact audit

The author repository [pbontrager/GenerativePlayingNetworks](https://github.com/pbontrager/GenerativePlayingNetworks) is public and MIT-licensed. Its README links the paper and identifies [`paper_run.py`](https://github.com/pbontrager/GenerativePlayingNetworks/blob/master/paper_run.py) as the paper-parameter entry point. It includes the generator, agent, training loop, environment wrappers, and example images.

Reproduction limitations:

- the setup depends on the `ascii` branch of GVGAI_GYM plus OpenAI Baselines and `pytorch-a2c-ppo-acktr-gail`;
- the repository has no released checkpoint, result bundle, training trace, test suite, tag/release, or container/complete dependency lock;
- the README warns that default parameters differ from the paper settings;
- the last visible repository commit is from 2020, so rebuilding the legacy dependency stack may require compatibility work.

**Final status: Partial.** The core implementation and explicit paper configuration are stronger than a demo-only release, but the missing trained state, results, tests, and reproducible environment prevent an Open classification under the audit definition.

## 99. Mutation Models: Learning to Generate Levels by Imitating Evolution

### Bibliography and scope

- Ahmed Khalifa, Michael Cerny Green, and Julian Togelius.
- Foundations of Digital Games (FDG) 2022, pp. 1–9.
- DOI: [10.1145/3555858.3563267](https://doi.org/10.1145/3555858.3563267).
- Primary preprint: [arXiv:2206.05497](https://arxiv.org/abs/2206.05497).

**Include.** The learned mutation model iteratively repairs random tile maps into connected 2D mazes. Evolution produces demonstrations during training; inference produces levels without evaluating fitness. The task is content generation, not game playing.

### Method and reported evidence

- Successful mutations from evolutionary trajectories supervise a CNN. Generation begins from **50/50 solid/empty noise** and iteratively edits a **14 × 14** maze.
- In the Normal condition, evolution completes before the model is trained. In Assisted evolution, the model is retrained from scratch every **100 generations** and used as a mutation operator; **25% random actions** preserve exploration.
- Evolution uses μ = λ = **50**, runs for **2,000 generations**, and is repeated in **three independent full runs**. Histories of the top 10 chromosomes form the learning dataset.
- Each prediction sees an **8 × 8 crop** around a proposed mutation location. The CNN has **224,771 parameters** and is trained with Adam at **1e-4**, batch size **32**, and categorical cross-entropy. Normal models train for 2, 4, or 8 epochs; Assisted trains for 2.
- Each model generates **100 levels** and may sweep all 196 tiles up to 196 times. Success means that every empty tile belongs to one connected component.
- Table 1 reports mean ± standard deviation:

| Condition | Success | Diversity | Iterations |
| --- | ---: | ---: | ---: |
| Assisted-2 | **99.67% ± 0.49%** | **86.83% ± 3.8%** | **18.21 ± 18.57** |
| Normal-2 | 30.17% ± 32.7% | 28.5% ± 30.62% | 61.7 ± 47.22 |
| Normal-4 | 66.83% ± 49.22% | 59.33% ± 43.69% | 23.55 ± 48.59 |
| Normal-8 | 65.17% ± 48.37% | 60% ± 44.59% | 31.78 ± 23.84 |

- Table 2 compares the best network condition with evolution:

| Generator | Success | Diversity | Time |
| --- | ---: | ---: | ---: |
| Network | 99.67% ± 0.49% | 86.83% ± 3.8% | 0.6612 ± 2.3874 s |
| Evolution | 100% | 96% | 12.6957 ± 2.2571 s |

The reported generation speed is therefore approximately **20× faster**. “Diversity” is specifically the fraction of successful levels with a distinct `(longest path length, empty tile count)` pair; it is not a general perceptual-diversity measure.

### Artifact audit

The author repository [amidos2006/ImitatingEvolution](https://github.com/amidos2006/ImitatingEvolution) directly links the paper and contains evolutionary search, MAP-Elites extensions, binary/Zelda/Sokoban environments, dataset construction, network training/inference, JSON configurations, and a requirements file. This establishes first-party provenance and meaningful implementation coverage.

Material limitations:

- no LICENSE (`license: null`), tag/release, trained model, released trajectory dataset, paper result bundle, seed manifest, or test suite;
- [`requirements.txt`](https://github.com/amidos2006/ImitatingEvolution/blob/main/requirements.txt) lists only unpinned `numpy`, `torch`, `tqdm`, and `Pillow`;
- the repository continued into broader experiments after publication and its branches/configuration have drifted; for example, the visible training configuration uses learning rate `1e-5`, while the paper specifies `1e-4`;
- the README's inference example refers to a `results/...` checkpoint that is not committed.

**Final status: Partial.** The repository is sufficient to inspect and adapt the method, but it is not a clean, exact reproduction package for the FDG results.

## Indexing corrections to carry forward

1. Keep all four records inside the generation-only scope; describe agents/pathfinders as training or evaluation components.
2. Change #96 from Closed, if currently so labelled, to **Partial** and cite the author-associated repository.
3. Store only the canonical 2020 DOI for #97; do not count the volume-15 DOI as another work.
4. Keep #97 **Closed** unless a first-party release is later identified.
5. Mark #98 and #99 **Partial**, and do not translate sample figures or optimization targets into dataset-wide success claims.
