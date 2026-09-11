# Independent audit: five classic game-generation additions and research guide

Audit date: **2026-09-05 (Asia/Shanghai)**. Read SCOPE.md, current public PCG rows #13–17, their source-dossier blocks, the original expansion note, and the Chinese research guide. This audit changes no public records. It distinguishes original full text, original preview/abstract, and later author corroboration. No generator was executed or reported result independently reproduced.

## Findings

No mandatory topical removal was established for these five records under the existing SCOPE: complete games **or executable rules/mechanics** qualify. The largest remaining evidence limitation is the missing original method/experiment chapters for the 2012 ACCME and 2016 chess papers. Their primary abstracts explicitly establish generation and evaluation; lack of downloadable full text alone does not negate those statements. The co-creative 2023 paper qualifies narrowly as executable rules/systems, not as a complete playable game. The guide is mostly a clearly identified editorial reading framework, but two broad method-family formulations and the unqualified lineage arrow should be tightened.

## #13 — ACCME, 2012

**Verdict:** retain, with partial-original-text evidence; no quantitative upgrading.

Primary sources retrieved:

- [Springer chapter](https://link.springer.com/chapter/10.1007/978-3-642-29178-4_20), original Abstract.
- **Newly recovered original preview:** [Springer preview PDF](https://page-one.springer.com/pdf/preview/10.1007/978-3-642-29178-4_20), exactly printed pages **194–195**, not the full ten-page chapter.

The original abstract states that ACCME “uses co-operative co-evolution to automatically evolve simple platform games,” and investigates both fitness maximization and whether its scores “correlate with player preference in the resulting games.” Page 194, Introduction, says section 3 presents the automatic 2D-platform-game system and experiments. These are explicit method/output/evaluation claims, not an unevaluated architecture announcement.

Page 195's **The ANGELINA System** subsection describes the *prior 2011 system*: maps, layouts, rulesets, composition, and experiments. It must **not** be silently used as the precise ACCME representation or 2012 experimental evidence. The current row avoids that error; the acronym “Metroidvania Engine” is supported by the original abstract, but it does not prove a general commercial-quality Metroidvania generator.

Retrieval limitation: Springer `/content/pdf/` returns subscription chapter HTML, not PDF. The old Imperial manuscript path returned/was already documented as 404; Goldsmiths CCG requests timed out and its alternate author path was 404. OpenAlex identified a CiteSeerX copy (10.1.1.298.8726), but its document endpoint returned an archived 404 page; archive CDX returned 503. These attempts did not recover sections 3–4. Do not state participant counts, correlations, significance or detailed fitness decomposition.

**Recommended evidence note:** “Original publisher abstract and original pp.194–195 preview inspected; method and experimental sections unavailable in this pass.” Current Closed wording should remain “no official generator/experiment package verified,” not “the authors released nothing.” A paywalled article is not itself evidence that its software was never public.

## #14 — Towards Generating Arcade Game Rules with VGDL, 2015

**Verdict:** retain full-game method; existing numerical summary verified.

Original [author PDF](https://www.kmjn.org/publications/GeneratingVGDL_CIG15.pdf) retrieved as PDF and text-inspected. [Author landing page](https://www.kmjn.org/publications/GeneratingVGDL_CIG15-abstract.html) and [publication DOI](https://doi.org/10.1109/CIG.2015.7317941) identify the paper.

- **Section V.C, Results:** “We evolved 54 total games: 45 from the human-designed games, and 9 from a randomly generated starting point.” It explicitly reports **40 mutated and six random-start games** with fitness above **0.98**.
- **Figures 6–7:** provide an evolved VGDL description from a random start and screenshots; the random branch includes descriptions and levels. This is actual new executable-game generation in addition to mutations of human seeds.
- **Section VI, Discussion:** “the VGDL game generation process was not able to create any game of reasonably high quality,” with further examples of player-independent/luck-dominated outcomes. The authors explicitly say they did **not** verify with humans whether games were good or bad.
- **Section VII, Conclusion:** reports playable VGDL games of varying quality and acknowledges trivial/luck-based rules. This supports generation-method scope despite weak design quality.

The existing public and dossier summaries preserve the negative results. Do not turn high fitness into a human-quality success rate, and do not interpret the 54 as 54 verified enjoyable games. No independent author-linked paper-specific generator release was found in the author landing page/PDF inspected here; Closed/unverified remains appropriately cautious.

## #15 — Evolving Chess-like Games Using Relative Algorithm Performance Profiles, 2016

**Verdict:** retain executable-rules method; original full experimental evidence remains unavailable.

Primary evidence:

- [Original Springer chapter abstract](https://link.springer.com/chapter/10.1007/978-3-319-31204-0_37), publication date 2016-03-15, pages 574–589. It explicitly addresses “automatic generation of complete rules,” formalizes the relative algorithm-performance method, applies it to evolving chess-like boardgames and reports “playable and balanced games.” This is not a prose-rulebook inference.
- [Coauthor Marek Szykuła's institutional homepage](https://ii.uni.wroc.pl/~msz/), publication **[16]**, confirms the 2016 paper, authors, venue, volume and pages. The author list supplies only its DOI, not a manuscript link. This is bibliographic corroboration, not full-method evidence.
- [Later coauthor manuscript, Mapping Chess Aesthetics…](https://antoniosliapis.com/papers/mapping_chess_aesthetics_onto_procedurally_generated_chess-like_games.pdf), original PDF retrieved and inspected. **Section 2.1** explicitly says it uses the evolutionary system in reference **[14]** and describes symmetric games, one royal piece, an initial pawn-like row, and agent-profile comparisons with human-made chess-like games. **Section 2.2** defines regular-expression piece moves, finite-automaton legal-move computation, alternating turns and terminal conditions. **Section 3 and Table 1** actually use the 2016 generated game **The Legacy of Ibis**, providing stronger corroboration than a casual citation.

Important attribution boundary: later descriptions establish the executable representation and continued use of an earlier output. They do not independently recover the 2016 generation-run counts, human testing, statistical significance or all implementation details. “Good quality” in the abstract is the authors' claim; it should not become an established human-experience result.

Retrieval limitation: original Springer PDF endpoint returned chapter/paywall HTML. Preview endpoint returned 403; the direct historical Kowalski host was unavailable/404. The Szykuła homepage had no linked 2016 PDF, and OpenAlex had only the publisher location. No original experimental numbers should be added. No official generator or evaluated-game package was verified; retain that bounded Closed statement.

## #16 — Adversarial Random Forest Classifier for Automated Game Design, 2021

**Verdict:** retain joint VGDL game generator; Partial is a packaging judgment, not a scope judgment.

[Original full text](https://arxiv.org/html/2107.12501) inspected, especially **sections 3–5 and Table 1**.

- **Method / Game generation:** VGDL has separate description and level files. Descriptions include sprite classes, interaction rules and termination conditions; a neighbor replaces a sprite, interaction or termination rule, and level search changes layout. The learned RF is a fitness signal internal to generation, not the standalone scored output.
- **Experiments:** eight human training games, two representations (with/without termination information), five iterations. **Table 1** reports completion, average/max scores and moves for MCTS and random agents. This supports the present evaluation summary; it does not establish a novel high-quality-game success rate.
- **Discussion:** timer terminations explain many completions in the no-termination setting. Both a five-minute wall-clock limit and a 700-move cap were imposed. The authors explicitly discuss why move-count differences are confounded by MCTS computation. Current negative-result wording is justified.

[Official README](https://raw.githubusercontent.com/HonestPretzels/RF_Adversarial_PCG/master/level-generation/README.md) was freshly retrieved. Steps 2–4 describe `gameGen.py`, `train.py`, and `levelGen.py`; step 5 explicitly invokes human play through `vgdl.util.humanplay.play_vgdl`. This confirms the intended runnable game format. The current main-agent note previously inspected a tree without `train.py`; this audit could not independently recheck that absence because fresh GitHub API tree requests hit **403**. Do not describe this audit as independently reconfirming missing files. The accessible README plus full text confirms substantial public source intent, but neither proves successful reproducibility. Partial with an explicit legacy-setup limitation is defensible; missing license alone is insufficient to downgrade status.

## #17 — A Controllable Co-Creative Agent for Game System Design, 2023

**Verdict:** retain only as executable rules/game-system generation; sharpen the meaning of “playable.”

[Original full text](https://arxiv.org/html/2308.02317) inspected, named subsections **Modeling Games Generically**, **Game Evaluator**, **Genetic Game Generator**, **Study**, and **Tables 1–2**.

- **Modeling Games Generically:** “A human game designer could then take those systems and mechanics and build levels, stories, and the rest of the actual playable game.” Therefore this paper does **not** establish a complete game build. It explicitly cannot simulate AI characters or processes independent of the player.
- **Game Evaluator:** components may be stored as JSON; implemented Q-learning executes states, actions, transitions and resource constraints. A rollout stops at the epoch limit or when no valid action remains. This is an executable state/resource system, not solely narrative JSON. Current SCOPE explicitly permits executable rules/mechanics, so this boundary is not a reason to force removal.
- **Genetic Game Generator:** chromosomes have variable length; mutation changes or **adds** components under structural constraints. The work contains a substantive generator beyond its separate fixed-parameter balancer.
- **Study / Expressive Range:** **100,000 random designs**, roughly **33,000 selected as playable**, then metric statistics over simulated playthroughs. These are not 33,000 human-tested games and not a success-rate evaluation of the optimized genetic generator alone.
- **Study / Controllability:** **25 random games**, each target metric weighted **−100/+100**, others held at 1; both balancer and generator tested. **Table 2** gives p-values, including generator action-novelty **0.106**, interactivity **0.5**, curiosity **0.5**, and state-novelty **0.052**. Do not summarize all ten metrics as successfully controlled; the mixed-result summary is appropriate.

**Recommended public wording:** “100,000 random abstract systems, approximately 33,000 accepted for simulated play,” followed by the 25-design weighted-control tests. This is more precise than “33,000 playable games.” Keep `rules`, not `full-game`. No paper-specific release was verified by this pass; the generic CreativeWand framework is not evidence of an open game-domain generator.

## Research-guide audit

Audited [Chinese guide](../docs/zh-CN/research-guide.md). Its taxonomy and five-layer checklist are useful editorial synthesis; it already states that the checklist is not a universal standard. The following distinguishes evidence-backed facts from editorial judgments.

### 1. Lineage arrow — narrow clarification recommended

The table says **GameGAN → CADDY → Playable Environments**, followed by “早期研究谱系.” Primary evidence supports a related research sequence, but the arrow can imply direct architecture inheritance.

- [CADDY original full text](https://arxiv.org/html/2101.12195), **section 2, Related Works**, describes GameGAN's action-labeled training and contrasts CADDY's unsupervised action discovery. This supports antecedent/contrast, not “CADDY is an improved version of GameGAN.”
- [Playable Environments full text](https://arxiv.org/html/2203.01914), **Related Work / Playable Video Generation**, explicitly identifies CADDY as its prior task baseline and contrasts single-object control with camera/3D control. **Tables 2–3** compare CADDY and adaptations. The lineage here is much stronger, but even Table 2 does not show dominance on every metric (CADDY has lower FID and ADD there).

Suggested replacement: “早期动作控制生成：GameGAN；无动作标注的可玩视频：CADDY；进一步加入相机与三维控制：Playable Environments。” Cite those papers directly and avoid an implied universal ranking. The existing sentence saying later methods do not universally replace earlier ones is worth keeping.

### 2. Method-family capabilities — frame as objectives, not guarantees

“演化与质量多样性” currently says “搜索多个可玩且差异化的解.” That is a useful aim but too strong as a family-wide capability guarantee. The [VGDL 2015 original](https://www.kmjn.org/publications/GeneratingVGDL_CIG15.pdf), **section VI**, supplies a concrete counterexample: high-fitness outputs can be trivial or luck-dominated. The [2023 co-creative paper](https://arxiv.org/html/2308.02317), **Study/Table 2**, similarly distinguishes randomly executable systems from effective metric control.

Suggested replacement: “以可玩性、质量或行为差异为目标，搜索规则与关卡候选；保证程度取决于约束和评价器。” Likewise, “可控分布采样” should say “尝试按设计属性生成多样候选,” since empirical controllability is not a guarantee that every requested conjunction is satisfiable.

### 3. Sample dependence — separate kinds of supervision

The “学习迭代编辑器与局部更新规则” row groups PCGRL, NCA and Path of Destruction under “减少对人工样本的依赖.” This is directionally reasonable but hides different dependencies. [PoD](https://arxiv.org/html/2202.10184), **section II**, derives training trajectories from existing authored levels; [NCA](https://arxiv.org/html/2109.05489), **Introduction/Method**, learns by quality-diversity search with functional criteria. A clearer phrasing is “以奖励/约束或少量示例的破坏轨迹学习迭代生成；样本需求因方法而异.” Do not imply all four are dataset-free.

### 4. Five-layer evaluation checklist — retain as editorial framework

The guide explicitly introduces this as a cross-paper reading checklist, **not** a shared standard. It does not claim a formally validated “comprehensive benchmark,” so no removal is needed. Strengthen attribution to “本仓库的阅读检查清单” if desired. Its five categories deliberately mix execution, gameplay correctness, sustained interaction, controllability/diversity and experience/cost; they should not be converted to a common additive score without a new validated protocol.

Concrete primary support includes [VGDL 2015](https://www.kmjn.org/publications/GeneratingVGDL_CIG15.pdf), **section VI**, for the disconnect between proxy fitness and human game quality; [Co-creative 2023](https://arxiv.org/html/2308.02317), **Table 2**, for uneven target controllability; and [diffusion Sokoban](https://arxiv.org/html/2608.15958), **sections 2.4 and 3**, for separating solver-free training from solver-based post-generation assessment. These support checking the distinctions, not claiming the five-layer organization is an established external taxonomy.

### 5. Comparison advice — explicitly recommendation, not findings

The paragraph requiring input, budgets, sampling/filtering, evaluator dependencies and failure denominators is sound methodological advice, not an empirical finding that all indexed papers satisfy those conditions. Keep it in recommendation form. “吞吐高不等于控制响应快” is a valid definitional distinction between throughput and latency; the guide should not use it to rank any paper without comparable measurements. This audit did not independently reread every recent benchmark listed in the guide and therefore cannot certify all their task counts or evaluation details.

## Priority changes recommended to the integrating agent

1. Upgrade ACCME evidence note from abstract-only to **abstract + original two-page preview**, while explicitly retaining the missing-method/experiment limitation.
2. Clarify #17 as **executable abstract systems and simulated play**, not complete playable-game production or human-tested playability.
3. Replace the guide's lineage arrow with explicit task progression and change family-level capability guarantees into generation objectives.
4. Preserve honest uncertainty: the 2016 original text was not recovered, RF file absence was not independently rechecked here, and no external implementation was run.
