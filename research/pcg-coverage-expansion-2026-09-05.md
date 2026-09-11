# PCG coverage expansion — 2026-09-05

Checked on **2026-09-05 (Asia/Shanghai)** against the existing 86 PCG records, SCOPE.md and the strict scope audit. Nineteen of the original 20 candidates remain integrated as public PCG records #92–110; MIPCGRL is held pending playable-output evidence, and the distinct second ChatGPT4PCG protocol occupies #111 after the five historical-rule additions, with matching English/Chinese tables and source-dossier blocks. This is not a claim of exhaustive coverage. The main omissions are whole method families (neural cellular automata, GFlowNets, destruction-trained iterative generators), non-Mario dungeon and puzzle construction, rhythm-chart generation, and recent multi-agent/language-conditioned PCG.

## Search and evidence method

Used the primary arXiv Atom API (`https://export.arxiv.org/api/query`) with title/all-field queries for procedural content generation, level generation, Sokoban generation, dungeon generation, rhythm-game generation, puzzle generation, and Dance Dance Convolution. Recent-work queries explicitly used submittedDate 2024-01-01 through 2026-09-05; broader domain queries included older work. Queried up to 100 results per targeted search. This covered hundreds of returned records including irrelevant matches, not an exhaustive citation graph. Read the primary full-text HTML for the accepted candidates below, focusing on methods, generation outputs, evaluation, limitations, and author-linked artifacts. GitHub API repository metadata and READMEs were used to verify linked releases; no code was executed.

Evidence levels: **F** = primary full text inspected; **A** = primary abstract only. “Closed/unverified” means no usable paper-specific release was verified in this pass, not proof that no release exists. Artifact status reflects available generation/training/evaluation components; missing licenses are documented separately and do not by themselves change Open to Partial. Historical dependencies and missing reproducibility packages are noted separately from topical eligibility.

The original 20 candidates reviewed below are distinct from the existing public PCG records by title and arXiv identity. Distinct follow-up papers remain separate where they add a new generator design rather than merely republish the same paper. Shared code repositories are not proof of paper duplication. Do not attach other already-indexed papers' linked identifiers to their evidence rows.

## Integrated additions and bilingual descriptions

### 1. Dance Dance Convolution — 2017

- Source: [paper](https://arxiv.org/abs/1703.06891); [full text](https://arxiv.org/html/1703.06891). **F**, ICML 2017 confirmed by author repository citation.
- Evidence: pipeline “ingests audio features” and “produces a playable DDR choreography”; running step placement and selection in sequence yields a playable step chart. Evaluates placement by perplexity/AUC/F-score and selection by perplexity/token accuracy on Fraxtil and In The Groove, including non-neural and neural baselines.
- Artifact: **Open, legacy dependencies** — [MIT author repository](https://github.com/chrisdonahue/ddc), dataset preparation, training, inference and scripts; README warns the local demo needs TensorFlow 0.12.1. Music packs are separately downloaded.
- EN method: Converts audio into playable DDR step charts through CNN/LSTM onset placement and conditional sequence-based step selection.
- EN evaluation: Compares placement F-scores/AUC and symbolic-step perplexity/accuracy against regression, MLP, CNN and n-gram baselines on two chart datasets.
- 中文方法：用 CNN/LSTM 预测踩点时刻，再以条件序列模型选择箭头动作，将音频转成可玩的 DDR 谱面。
- 中文评测：在 Fraxtil 与 In The Groove 数据上比较踩点 F-score/AUC、动作困惑度和准确率，并与回归、MLP、CNN、n-gram 基线对照。

### 2. TaikoNation: Patterning-focused Chart Generation for Rhythm Action Games — 2021

- Source: [paper](https://arxiv.org/abs/2107.12506); [full text](https://arxiv.org/html/2107.12506). **F**.
- Evidence: prediction averaging and post-processing explicitly convert outputs “back into a playable format.” Generates osu!taiko charts and evaluates human-like patterning against Dance Dance Convolution; comparisons include pattern and note-timing behavior rather than music generation alone.
- Artifact: **Partial, unlicensed** — [author source](https://github.com/emily-halina/TaikoNationV1) includes training code, charts, outputs and TensorFlow checkpoints, but documentation is unfinished and hard-coded input/model paths do not match the released layout.
- EN method: Generates playable osu!taiko charts from music with a patterning-focused neural model and chart-format post-processing.
- EN evaluation: Compares binary rhythm-pattern statistics on 10 held-out songs with DDC and random noise, using corresponding human Taiko/DDR charts; not a human preference study.
- 中文方法：采用重视音符组合规律的神经模型，从音乐生成 osu!taiko 谱面，并通过后处理导出可玩格式。
- 中文评测：在 10 首留出歌曲上，将二值节奏模式统计与 DDC、随机噪声及相应人工 Taiko/DDR 谱面对比；不是玩家偏好研究。

- Audit: [independent primary-source check](independent-pcg-audit-2026-09-05.md).

### 3. Beat-Aligned Spectrogram-to-Sequence Generation of Rhythm-Game Charts — 2023

- Source: [paper](https://arxiv.org/abs/2311.13687); [full text](https://arxiv.org/html/2311.13687). **F**, ISMIR late-breaking/demo extended abstract; disclose this publication type.
- Evidence: section 2 defines four-key osu!mania tap/hold/release charts; section 3 compares micro-F1, data scaling, pretraining/fine-tuning and beat-alignment ablation. Uses 6,781 retained charts/2,004 songs after filtering, not the larger raw collection count.
- Artifact: **Open code; externally hosted weights** — [MIT repository](https://github.com/stet-stet/goct_ismir2023) and [author demos](https://stet-stet.github.io/goct/); README documents preprocessing, train/validation/test lists and a 300 MB model archive on Google Drive. The archive was linked but not downloaded in this pass.
- EN method: Conditions a Transformer on beat-aligned log-Mel spectrograms, difficulty and preceding chart tokens to generate four-key rhythm charts.
- EN evaluation: Measures micro-F1 against previous methods and ablates beat alignment, dataset scaling, pretraining and fine-tuning.
- 中文方法：以节拍对齐的声谱、难度和此前谱面 token 为条件，用 Transformer 生成四键音游谱面。
- 中文评测：比较 micro-F1，并消融节拍对齐、数据规模、预训练与微调；论文为 ISMIR LBD 扩展摘要。

### 4. Dance Dance ConvLSTM — 2025

- Source: [paper](https://arxiv.org/abs/2507.01644); [full text](https://arxiv.org/html/2507.01644). **F**.
- Evidence: full method separately trains step placement and symbolic selection; section 6 evaluates Fraxtil using F1/precision/recall, symbolic accuracy and held-note accuracy. This is a distinct ConvLSTM method, not a new name for the 2017 paper.
- Artifact: **Open** — [author repository](https://github.com/miguelomalley/DDCL) has `.sm` generation, preprocessing and model training; no detected software license and the full experiment was not reproduced.
- EN method: Uses ConvLSTM-based onset placement and symbolic-step models to generate DDR/StepMania `.sm` charts from music.
- EN evaluation: Compares precision/recall/F1 and step/hold accuracy with a reimplemented DDC; separates fixed 0.5 thresholds from oracle per-chart F1-max thresholds, so published predecessor scores are not directly comparable.
- 中文方法：用 ConvLSTM 踩点预测与动作序列模型，将音乐转成 DDR/StepMania 的 `.sm` 谱面。
- 中文评测：与重新实现的 DDC 比较 precision/recall/F1、动作及长按准确率；固定 0.5 阈值与逐谱面 oracle 最优 F1 阈值需区分，不能直接宣称优于前作已发表分数。

- Audit: [independent primary-source check](independent-pcg-audit-2026-09-05.md).

### 5. ITGPT: A Transformer Based Architecture for the Generation of Dance Dance Revolution and In the Groove Charts — 2026

- Source: [paper](https://arxiv.org/abs/2607.14148); [full text](https://arxiv.org/html/2607.14148). **F**.
- Evidence: section 6 compares placement and selection with predecessor models on an expanded Fraxtil collection, including top-k accuracy, held-note accuracy and computation. It is a distinct Transformer follow-up to DDCL.
- Artifact: **Open** — [MIT source](https://github.com/miguelomalley/ITGPT) with training, preprocessing, requirements and `generate_charts.py`; author README links an HF Space and GUI generation release. Music packs remain external inputs.
- EN method: Generates DDR/ITG charts through Transformer-based step-placement and step-selection models.
- EN evaluation: Compares onset performance, symbolic/top-k/hold accuracy and computation with predecessor chart generators and model-size variants.
- 中文方法：以 Transformer 分别建模踩点与动作选择，自动生成 DDR/ITG 可玩谱面。
- 中文评测：在扩展 Fraxtil 数据上比较踩点、动作/top-k/长按准确率与计算成本，并对模型规模做对照。

### 6. Procedural Generation of Initial States of Sokoban — 2019

- Source: [paper](https://arxiv.org/abs/1907.02548); [full text](https://arxiv.org/html/1907.02548). **F**, IJCAI 2019 per primary metadata.
- Evidence: proposes Beta, a reverse-search generator using pattern-database difficulty and novelty to produce solvable starting arrangements. Section 7 uses 90 xSokoban problems, compares generator heuristics and specialized-solver hardness; it creates new puzzle instances, not just a solver.
- Artifact: **Closed/unverified** — no official Beta source or generated experiment package located in inspected full text.
- EN method: Generates solvable, difficult Sokoban start states using reverse search guided by pattern-database heuristics, conflicts and novelty.
- EN evaluation: Compares generated-state hardness across heuristic variants and human-authored xSokoban problems through solver effort and conflict measures.
- 中文方法：以模式数据库启发式、冲突和新颖性引导反向搜索，生成可解且较难的 Sokoban 初始局面。
- 中文评测：基于 90 个 xSokoban 问题比较生成器变体，通过求解开销与冲突指标对照人工谜题。

### 7. Two-step Constructive Approaches for Dungeon Generation — 2019

- Source: [paper](https://arxiv.org/abs/1906.04660); [full text](https://arxiv.org/html/1906.04660). **F**, FDG PCG workshop.
- Evidence: MiniDungeons 2 construction first generates floors/walls, then places start, goal, monsters, traps and treasures. Three layout creators combine with three furnishers. Expressivity analysis and procedural-persona simulations evaluate resulting complete game levels.
- Artifact: **Closed/unverified** — no paper-specific implementation or fixed experiment release verified.
- EN method: Combines three architectural layout creators and three object furnishers into complete MiniDungeons 2 levels.
- EN evaluation: Measures expressive range and generated-level behavior in simulations with procedural player personas.
- 中文方法：将三种空间布局生成器与三种对象布置器组合，生成含起终点、敌人、陷阱和奖励的 MiniDungeons 2 关卡。
- 中文评测：分析表达范围，并用程序化玩家画像模拟游玩生成关卡。

### 8. Generative Adversarial Network Rooms in Generative Graph Grammar Dungeons for The Legend of Zelda — 2020

- Source: [paper](https://arxiv.org/abs/2001.05065); [full text](https://arxiv.org/html/2001.05065). **F**, IEEE CEC 2020 per metadata.
- Evidence: GAN rooms are assembled with a graph grammar into full dungeons; a repair phase makes them playable. Only 10/30 GAN and 16/30 grammar-only dungeons required repair. User study compares generated dungeons with the original game and grammar-only layouts.
- Artifact: **Open, legacy dependencies** — author [paper-specific MM-NEAT experiment](https://github.com/schrum2/MM-NEAT/tree/master/batch/Experiments-2020-CEC-ZeldaGAN), GAN loader and study/play scripts; old Java/Maven/Python setup and no fresh reproduction.
- EN method: Combines GAN-generated Zelda rooms with mission-structured graph grammars and internal repair to form complete playable dungeons.
- EN evaluation: Thirty participants compare three dungeon conditions; GAN rooms are less organized and more complex, without broad enjoyment superiority.
- 中文方法：用 GAN 生成 Zelda 房间，再以任务结构图文法组织并内部修复，得到完整可玩地牢。
- 中文评测：30 名参与者对比三类地牢；GAN 房间组织性较差、复杂度较高，并未普遍提高乐趣。

- Audit: [independent primary-source check](independent-pcg-audit-2026-09-05.md).

### 9. Illuminating Diverse Neural Cellular Automata for Level Generation — 2021 / 2022

- Source: [paper](https://arxiv.org/abs/2109.05489); [full text](https://arxiv.org/html/2109.05489). **F**; 2021 preprint and repository's 2022 paper section are one record.
- Evidence: CMA-ME evolves archives of NCA generators for maze, Sokoban and Zelda. Evaluation explicitly compares generator archive quality/diversity, CPPN representations and generalization to unseen seeds; NCA policies output tile maps, not game-playing policies.
- Artifact: **Open, legacy configuration caveats** — [MIT code](https://github.com/smearle/control-pcgrl) explicitly identifies the paper and describes evolution/evaluation commands; README notes outdated instructions and cluster-specific setup.
- EN method: Uses CMA-ME quality-diversity search to learn archives of neural cellular automata that iteratively generate maze, Sokoban and Zelda levels.
- EN evaluation: Compares archive quality/diversity and unseen-seed stability against CPPN generator representations and training variants.
- 中文方法：通过 CMA-ME 质量多样性搜索学习一组神经元胞自动机，迭代生成迷宫、Sokoban 和 Zelda 关卡。
- 中文评测：比较生成器档案的质量、多样性及新随机种子上的稳定性，并对照 CPPN 表示与训练设置。

### 10. Path of Destruction: Learning an Iterative Level Generator Using a Small Dataset — 2022

- Source: [paper](https://arxiv.org/abs/2202.10184); [full text](https://arxiv.org/html/2202.10184). **F**, SSCI 2022.
- Evidence: destructive mutations generate self-supervised training trajectories; inference starts from random unseen maps and creates playable Zelda, Danger Dave and Sokoban levels. Evaluates each trained generator over 10,000 inference trials, reporting playability and uniqueness. It passes the scope rule because repair is the internal generation mechanism.
- Artifact: **Closed at check** — paper-linked [repository](https://github.com/matt-quant-heads-io/path_of_destruction) returned GitHub API 404 on 2026-09-05; do not infer openness from the paper's footnote.
- EN method: Learns inverse actions from destructive trajectories of a small level set, then iteratively converts random maps into new playable levels.
- EN evaluation: Measures playability and uniqueness over 10,000 trials per generator across three games and dataset/hyperparameter variants.
- 中文方法：从少量关卡的破坏轨迹学习逆向动作，再从随机地图迭代生成新可玩关卡。
- 中文评测：每个生成器运行 10,000 次，在三个游戏和不同数据量/超参数下统计可玩率与唯一性。

### 11. Controllable Path of Destruction — 2023

- Source: [paper](https://arxiv.org/abs/2305.18553); [full text](https://arxiv.org/html/2305.18553). **F**, CoG 2023.
- Evidence: adds conditional inputs to destruction/repair trajectories. The in-scope task is a complete dungeon with one player, key and door, connected paths and target properties. Reports 78.86 ± 4.95% playable output and about 24.42% diversity. Lego cars are outside this record's scope.
- Artifact: **Closed/unverified** — no distinct working official implementation/evaluation package verified.
- EN method: Conditions destruction-trained iterative dungeon generators on designer-selected path and enemy-distance properties.
- EN evaluation: Measures dungeon playability, duplicate/diversity behavior and target controllability; excludes its separate Lego-asset experiment.
- 中文方法：为破坏轨迹训练的迭代地牢生成器加入路径长度、敌人距离等设计条件。
- 中文评测：检查地牢可玩率、多样性/重复率和目标可控性；不计其独立 Lego 资产实验。

### 12. Start Small: Training Controllable Game Level Generators without Training Data by Learning at Multiple Sizes — 2022 / 2023

- Source: [paper](https://arxiv.org/abs/2209.15052); [full text](https://arxiv.org/html/2209.15052); [journal DOI](https://doi.org/10.1016/j.aej.2023.04.019). **F**. Preprint and journal are one record.
- Evidence: recurrent autoregressive GFlowNets learn first at small sizes, then larger sizes, without an authored dataset or shaped reward. Generates Sokoban, Zelda and Danger Dave; compares playability, diversity, control and unseen sizes, reporting 9× training/generation speed versus a controllable RL comparator for Sokoban.
- Artifact: **Open** — [MIT code](https://github.com/yahiaetman/ms-level-gen) includes environment, game analyzers, method implementations, experiment configurations, generation and analysis commands; README links pretrained weights and generated samples.
- EN method: Trains controllable autoregressive GFlowNet level generators through a small-to-large size curriculum without authored training levels or shaped rewards.
- EN evaluation: Measures solvability, diversity, target control, speed and unseen-size generation for Sokoban, Zelda and Danger Dave.
- 中文方法：使用由小到大的尺寸课程训练可控自回归 GFlowNet，无需人工训练关卡或塑形奖励。
- 中文评测：在 Sokoban、Zelda、Danger Dave 上比较可解性、多样性、可控性、速度与未见尺寸泛化。

### 13. Illuminating the Space of Dungeon Maps, Locked-door Missions and Enemy Placement Through MAP-Elites — 2022

- Source: [paper](https://arxiv.org/abs/2202.09301); [full text](https://arxiv.org/html/2202.09301). **F**.
- Evidence: a tree encoding guarantees key/locked-door mission feasibility; MAP-Elites generates room layouts with enemies. Full text says volunteers played a game prototype with generated levels. Computational and player-feedback experiments evaluate generation, not just representation.
- Artifact: **Closed/unverified** — no official experiment package verified.
- EN method: Evolves complete dungeon layouts, key/locked-door missions and enemy placements with a feasibility-preserving tree representation and MAP-Elites.
- EN evaluation: Computational archive analysis plus 96 players, 74 complete survey respondents and 121 level plays; exploratory feedback, not a controlled superiority result.
- 中文方法：结合保证任务可行性的树表示与 MAP-Elites，生成房间、钥匙锁门任务和敌人配置。
- 中文评测：计算分析档案，并收集 96 名玩家、74 份完整问卷和 121 次关卡游玩反馈；属于探索性研究，并非受控优越性结论。

- Audit: [independent primary-source check](independent-pcg-audit-2026-09-05.md).

### 14. High Dimensional Procedural Content Generation — 2026

- Source: [paper](https://arxiv.org/abs/2602.18943); [full text](https://arxiv.org/html/2602.18943). **F**.
- Evidence: Direction-Space incorporates layer changes/gravity/world switching; Direction-Time represents moving platforms/obstacles in time-expanded graphs. Methods generate, ground and validate levels; Unity case study states the level is generated directly from the planner and “what you see is exactly what is playable.” Separate-axis experiments, not demonstrated joint multi-mechanic composition.
- Artifact: **Closed/unverified** — no author implementation/project release verified in full text.
- EN method: Generates platform levels in joint geometry/layer or geometry/time spaces, then grounds validated plans into playable Unity scenarios.
- EN evaluation: Compares three algorithms per axis using solver trajectories for reachability, target control, structure, robustness and runtime; Unity demonstrations support human play but are not user studies or joint-mechanic validation.
- 中文方法：在几何与层切换或时间的联合空间中生成平台关卡，并将验证过的规划实例化为 Unity 可玩场景。
- 中文评测：每个方向比较三种算法，以求解器轨迹量化可达性、可控性、结构、鲁棒性和耗时；Unity 展示支持人工游玩，但不是用户研究或多机制联合验证。

- Audit: [independent primary-source check](independent-pcg-audit-2026-09-05.md).

### 15. Procedural Generation of First Person Shooter Maps using Map-Elites — 2026

- Source: [paper](https://arxiv.org/abs/2605.30570); [full text](https://arxiv.org/html/2605.30570). **F**.
- Evidence: MESB evolves playable FPS maps with four encodings, including new Point-Line and Spatial-Layout representations; a Duel/deathmatch environment evaluates emergent gameplay properties. Compares topology and gameplay feature pairs, map quality and diversity.
- Artifact: **Closed for the paper-specific generator at check** — linked [generator repository](https://github.com/SimoDedo/MAPElites_FPS_Maps) returned API 404. A separate underlying runtime does not make the method reproducible.
- EN method: Uses MAP-Elites with sliding boundaries and alternative spatial encodings to evolve FPS deathmatch maps.
- EN evaluation: Compares four representations on map quality/diversity using topology descriptors and emergent properties from actual game simulations.
- 中文方法：用滑动边界 MAP-Elites 和不同空间编码演化 FPS 死亡竞赛地图。
- 中文评测：结合拓扑描述符与实际游戏模拟产生的行为指标，比较四种表示的地图质量和多样性。

### 16. Solvable Sokoban Without a Solver via Diffusion — 2026

- Source: [paper](https://arxiv.org/abs/2608.15958); [full text](https://arxiv.org/html/2608.15958). **F**.
- Evidence: masked discrete diffusion learns tile completion from 450,000 Boxoban puzzles without solver rewards/labels; evaluation generates 5,000 puzzles per sampled checkpoint and runs a solver. Final reported solvability 77.4%; also measures local-pattern JSD, memorization and temperature. “Without a solver” describes training, not evaluation or filtering in the demo.
- Artifact: **Partial, unlicensed inference/model release** — [official repository](https://github.com/sinabaghal/SokobanPlayground) has `model.pt`, generation and browser-play export; README's `play.py` checks solvability before exporting. No full training/experiment reproduction package verified.
- EN method: Trains masked discrete diffusion on Sokoban tile completion and samples new puzzles without solver-based training supervision.
- EN evaluation: Uses a solver after generation to assess solvability, and studies pattern-distribution match, memorization, temperature and one-wall repairs.
- 中文方法：以 Sokoban 格子补全训练掩码离散扩散模型，无需求解器提供训练奖励或可解标签。
- 中文评测：生成后用求解器测可解率，并分析局部模式分布、记忆、温度与单墙修复；试玩脚本也会筛选可解实例。

### 17. All Stories Are One Story: Emotional Arc Guided Procedural Game Level Generation — 2025

- Source: [paper](https://arxiv.org/abs/2508.02132); [full text](https://arxiv.org/html/2508.02132). **F**.
- Evidence: branching story nodes map to complete ARPG dungeon rooms with enemies/props, gameplay attributes and navigation. Outputs playable Unity WebGL games. Sixteen participants compare emotional-arc and non-arc experiences; ratings, interviews and sentiment analysis evaluate generated play. Unlike narrative-only JSON work, a playable pipeline is explicit.
- Artifact: **Closed/unverified** — no official generator/build/study-data release verified in inspected paper.
- EN method: Converts emotional-arc-conditioned story graphs into connected Unity ARPG rooms with instantiated entities, gameplay attributes and generated sprites.
- EN evaluation: A 16-person exploratory study compares engagement, coherence and emotional perception, supplemented by interviews and sentiment analysis.
- 中文方法：把情感弧条件下的故事图转成连通 Unity ARPG 房间，实例化角色、敌人、玩法属性与图像资源。
- 中文评测：用 16 人探索性研究比较参与感、连贯性及情感感知，并结合访谈和情绪分析。

### 18. Video Game Level Design as a Multi-Agent Reinforcement Learning Problem — 2025

- Source: [paper](https://arxiv.org/abs/2510.04862); [full text](https://arxiv.org/html/2510.04862). **F**.
- Evidence: multiple turtle agents jointly edit maps in binary-maze and dungeon domains, reducing global reward calculations per editing action. Dungeons require one player/key/door and relevant paths. Evaluates ten training seeds with fifty episodes per condition, square/rectangular OOD sizes and differing board-scan budgets. This is a distinct multi-agent follow-up, not the existing single-agent scaling paper.
- Artifact: **Open shared implementation, snapshot caveat** — [Apache-2.0 author code](https://github.com/smearle/pcgrl-jax), training/sweeps/evaluation instructions; exact paper snapshot and all results were not checked.
- EN method: Trains multiple cooperating PCGRL editing agents to generate maze and dungeon levels while sharing costly global quality evaluations.
- EN evaluation: Compares generator reward, editing budgets and generalization to unseen rectangular/square maps over multiple training and evaluation seeds.
- 中文方法：训练多个协同编辑地图的 PCGRL 智能体，共享昂贵的全局质量计算，生成迷宫和地牢。
- 中文评测：跨多组训练与评测种子比较生成质量、编辑预算及未见矩形/方形地图泛化。

### 19. Level Generation with Quantum Reservoir Computing — 2025

- Source: [paper](https://arxiv.org/abs/2505.13287); [full text](https://arxiv.org/html/2505.13287). **F**.
- Evidence: introduction explicitly defers real quantum-device training/generation; the actual study uses classical circuit simulation and produces sequences for a playable Roblox obby. Hardware latency is prospective, not demonstrated deployment.
- Artifact: **Partial** — [Apache-2.0 paper-specific data/notebook](https://github.com/moth-quantum/OpenData/tree/main/Level_Generation_with_Quantum_Reservoir_Computing) includes analysis, but imports missing local `archeo` modules; not a complete runnable QRC training release.
- EN method: Simulates quantum-reservoir sequence models on classical computers to generate Mario layouts and playable Roblox obstacle-course sequences.
- EN evaluation: Studies novelty, broken sequences, temperature and qubit budgets against Markov/random baselines; real quantum hardware and its real-time deployment remain future work.
- 中文方法：在经典计算机上模拟量子储备池序列模型，生成 Mario 布局与可玩的 Roblox 障碍赛道序列。
- 中文评测：与 Markov/随机基线比较新颖性、错误序列、温度和量子比特预算；真实量子硬件训练/生成及实时部署仍是未来工作。

- Audit: [independent primary-source check](independent-pcg-audit-2026-09-05.md).

## Held candidate: MIPCGRL (not counted)

The original twentieth candidate, [Multi-Objective Instruction-Aware Representation Learning in Procedural Content Generation RL](https://arxiv.org/abs/2508.09193), has a substantive representation-learning/generation contribution and public training/evaluation code. However, inspected [dungeon3 domain](https://github.com/k-shyun/MIPCGRL/blob/main/envs/probs/dungeon3.py) and [default configuration](https://github.com/k-shyun/MIPCGRL/blob/main/conf/config.py) define BORDER/EMPTY/WALL/BAT without player/start/goal, while reported metrics cover regions/path length/walls/bats rather than a verified playable task. Under SCOPE, hold until primary generation-to-playable-output evidence or another qualifying demonstrated domain is available. Not an absolute unplayability claim. See [independent audit, original #111](independent-pcg-audit-2026-09-05.md).

## Additional identity correction: benchmark #111

[The Second ChatGPT4PCG Competition](https://arxiv.org/abs/2403.02610) now has its own canonical record because Python-program submissions, multi-turn/control-flow allowance, diversity scoring, font-based classifier and function-signature evaluation materially change the [2023 protocol](https://arxiv.org/abs/2303.15662). This is one added formal benchmark, not another generator variant. Official [code/raw data](https://github.com/chatgpt4pcg/experiments-2024) available. Combined with MIPCGRL's hold, PCG stays111.

[ChatPCG2024](https://arxiv.org/abs/2406.11875) adjusts character/skill parameters and is excluded as standalone tuning. [PCGRLLM](https://arxiv.org/abs/2502.10906) stays#81, with 2025/2026 dates, trained-policy feedback and pathfinding-validated story levels. Do not conflate these papers' outputs or artifact releases.

## Explicitly held or rejected leads

| Candidate | Evidence | Decision and reason |
| --- | --- | --- |
| Dungeon and Platformer Level Blending and Generation using Conditional VAEs (2021) | Full text inspected | **Hold/exclude mixed-output claim**: body states blended levels need new mechanics, lack playability evaluation, and fully playable hybrids are future work. Non-blended layouts may warrant a narrower future review, but do not add broadly from the abstract. |
| A Novel Procedural Generation for Level Design of Mansions and Dungeons (2026; 2606.03857) | **A**, full HTML unavailable in this pass | Hold: abstract reports BSP/graph layout and BFS connectivity on 100,000 maps, but direct playable integration versus indoor-space generation requires full-text confirmation. |
| Procedural Game Level Design with Deep Reinforcement Learning (2025; 2510.15120) | **F** | Hold: Unity hummingbird navigation and flower placement are described, but inspected claims center learned agent efficiency and arrangements of collectibles; a complete playable-level generation/evaluation claim remains weaker than accepted candidates. |
| Level Generation with Constrained Expressive Range (2025; 2504.05334) | **F**, selected methods/evaluation | Hold pending careful boundary review: constraint-driven generation, density/difficulty coverage and interestingness analysis are real, but direct playable artifact evidence not fully established in this pass. |
| Level generation for rhythm VR games (2023; 2304.06809) | **A** | Hold: bachelor's thesis generates Ragnarock action timing/selection and a web application; verify full evaluation and thesis inclusion convention before adding. |
| Tree Search vs Optimization Approaches for Map Generation (2019/2020; 1903.11678) | **A** | Promising future review: abstract proposes new representations and compares Binary/Zelda/Sokoban generators, but full method/scope and artifact verification was not completed. |
| ChartGenEval (2026), generation-metric and training-data-effect papers | Search result screening | Do not add merely for evaluating charts or existing generators; formal generation-benchmark or new-method evidence is required. |
| CrossWordBench, SATBench, DungeonBench, Autoverse, agent-planning papers | Search result screening | Do not classify as generation benchmarks from names alone; central research objects often remain reasoning or playing agents. |
| 3D buildings, city/assets, music-only generation, narrative-only quest JSON | Existing scope plus search screening | Excluded unless integrated by the paper into an eligible playable output. |

## Remaining coverage limitations

This expansion is strong in 2017–2026 learned generation and non-Mario domains. Older graph-grammar mission generation, physics puzzle generation (including Cut the Rope), crosswords/nonograms/Sudoku and academic quest execution deserve a separate publisher/author-library sweep; the arXiv-only discovery route is less complete before 2015. The current evidence does not justify claiming all classic PCG literature is covered. Repository availability is checked, but released software has not been installed or reproduced.
