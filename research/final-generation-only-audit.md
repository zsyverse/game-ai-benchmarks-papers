# Final generation-only audit / 最终“只收生成”审计

> Audit cutoff / 审计截止：**2026-09-01 (Asia/Shanghai)**
>
> Public files checked / 公开文件：`docs/en/pcg.md`、`docs/zh-CN/pcg.md` 及对应 research notes。
>
> This note records the independent findings and their later resolution in the public index. / 本文记录独立发现及其在公开索引中的后续处理。

**Resolution / 处理状态（2026-09-01）：** #111's judging and artifact description was corrected in both languages; the Angry Birds corpus and Mario diffusion paper were independently verified and added as #114–115. The first-author diffusion repository was located after the initial audit, changing its final status from unclassified to **Partial, unlicensed author code**. / 中英文 #111 的评分与工件说明均已修正；Angry Birds 语料与 Mario 扩散论文经独立复核后作为 #114–115 补入。初审后又定位到扩散论文第一作者仓库，因此最终状态定为 **Partial，无许可证作者代码**。

## Executive conclusion / 核心结论

The scope boundary is sound. No source in the audited PCG range **#87–115** is primarily a paper about an agent playing a fixed game. Player models, A*, MCTS, RL, and self-play in these records are used to generate, repair, constrain, train, or evaluate game content. Titles, publication-family grouping, and displayed years are materially correct against the checked publisher records and papers.

范围边界正确：本轮核验的 PCG **#87–115** 中没有以“智能体玩固定游戏”为主要目标的论文。条目中的玩家模型、A*、MCTS、RL 与 self-play 都服务于内容生成、修复、约束、训练或评价。经出版方记录与论文核对，题名、版本族合并和展示年份整体正确。

There is **no scope-integrity blocker** and no evidence of a broken English/Chinese mapping. The collection should still be described as curated rather than exhaustive. This audit found and resolved:

1. one definite factual/artifact correction in **#111 AIBIRDS**;
2. one high-confidence missing generation dataset;
3. one high-confidence missing direct level-generation paper.

上述三项均已处理，因此仓库可以继续作为“经核验的精选索引”发布；但仍不宣称穷尽了所有游戏生成文献。

## Audit method and coverage / 方法与覆盖

- Compared the English and Chinese PCG rows by stable source number, section, year, title, URL order, and scope label. At audit start, the repository validator reported `pcg=113`; after resolving the findings, both languages contain the same 115 source identifiers in the same section counts.
- Re-read the primary paper text or official metadata for #87–113, with special attention to the recently added MdMC branches (#87–95), latent/self-supervised approaches (#96–99), metageneration (#100–105), and benchmarks/evaluation (#106–113), then independently inspected the papers and first-party artifacts for #114–115.
- Checked the target rows' publisher, proceedings, arXiv, archived-author, and author-repository URLs. All target URLs resolved during this audit. DOI endpoints returning HTTP 202 or bot-facing 403 responses were not treated as dead when the DOI metadata and destination remained valid.
- Rechecked benchmark coverage against the repository's own inclusion precedent: a fixed generation corpus is in scope even when it does not itself generate content, as shown by VGLC (#18).

Representative primary sources used in the pass:

- #87: [official IJCAI record and paper](https://www.ijcai.org/Abstract/16/116).
- #88–89, #91–92, #102, #108, #110: official [AAAI AIIDE proceedings](https://ojs.aaai.org/index.php/AIIDE).
- #90: [official IJCAI paper](https://www.ijcai.org/proceedings/2017/0105.pdf) and [author experiment repository](https://bitbucket.org/Sam_Snodgrass/ijcai_2017).
- #93–94, #106–107: archived author or official conference papers already linked by the index.
- #95–105, #109, #111–113: the displayed IEEE/ACM/arXiv/TechRxiv records and author repositories, including the detailed local audits for #96–105.

## Findings for PCG #87–113 / 新增条目复核

### #87–99: generation scope and bibliography

No correction is required from this pass.

- #87 really evaluates constrained generation for **Super Mario Bros.** and **Kid Icarus**; Lode Runner is future work, and the index states this correctly.
- #89 reports 66 MdMC plus 66 LSTM models, so the indexed total of **132 models** is correct.
- #92 explicitly reports **nine gameplay videos**, **13,492 chunks**, and recruitment of **73 participants**; those figures are not inferred from a secondary survey.
- #94 generates complete, described-as-playable Mario levels. The music metaphor is an internal representation, not music-asset generation.
- #96–99 have the correct canonical titles and publication years. Their A*, player, evolution, and RL components evaluate or train generators; none changes the records into playing-agent papers.

Primary evidence includes the [#87 official PDF](https://www.ijcai.org/Proceedings/16/Papers/116.pdf), the official AIIDE records for [#89](https://doi.org/10.1609/aiide.v13i1.12930) and [#92](https://doi.org/10.1609/aiide.v12i1.12861), and the paper-linked repositories for [#96](https://github.com/StarryBar/level-generation-for-lode-runner), [#98](https://github.com/pbontrager/GenerativePlayingNetworks), and [#99](https://github.com/amidos2006/ImitatingEvolution).

### #100–105: metageneration boundary

No correction is required from this pass.

- #100, #101, #103, #104, and #105 output a reusable generator, generator program, or WFC example that functions as a stochastic generator. Solver/play traces are fitness signals.
- #102 Marahel is correctly distinguished as a human-authored **generator language**, not falsely described as an automatic metagenerator.
- #112 Danesh is correctly kept outside the strict metageneration count because it tunes a fixed generator rather than synthesizing a new representation.

The publication titles and years agree with the official DOI/arXiv records: [#100](https://doi.org/10.1145/2538528.2538541), [#101](https://doi.org/10.1109/CIG.2012.6374174), [#102](https://doi.org/10.1609/aiide.v13i2.12970), [#103](https://doi.org/10.1109/CIG.2019.8847961), [#104](https://doi.org/10.1145/3402942.3409606), and [#105](https://arxiv.org/abs/2607.02082).

### #106–110 and #113: benchmark/evaluation accuracy

No correction is required from this pass.

- #106's paper says it compares **seven generators plus original SMB levels** with six metrics, two introduced in that paper. The linked supplemental ZIP is not preserved on the archived project page, so `Closed, archived landing page only` remains defensible.
- #107 explicitly introduces **20** proposed metrics and leaves computational implementation for later work.
- #108 explicitly reports **148 levels** and **37 retained participants** after cleaning.
- #113 is a comparison of Sokoban **generation systems** under a shared protocol, not a Sokoban-solving benchmark. Its 2022 online/DOI year and 2023 journal year are correctly represented as `2022 / 2023`.

Primary evidence: [#106 archived official paper](https://web.archive.org/web/20180921071717id_/http%3A%2F%2Ffdg2014.org%2Fpapers%2Ffdg2014_paper_14.pdf), [#107 archived official paper](https://web.archive.org/web/20170829055620id_/http%3A%2F%2Fwww.fdg2015.org%2Fpapers%2Ffdg2015_paper_16.pdf), [#108 official record](https://doi.org/10.1609/aiide.v11i1.12785), and [#113 official preprint](https://doi.org/10.36227/techrxiv.16640095.v3).

## Definite correction found and resolved: #111 AIBIRDS / 已发现并修正的明确问题

### Evaluation wording

At audit start, the row said the five submissions were judged for “fun, creativity, difficulty/balance, and diversity.” The paper defines three scored judging categories: **Fun**, **Creativity**, and **Difficulty** (described in the method as balanced difficulty). Similarity/variety is discussed as a possible penalty or limitation, but **diversity is not a fourth separately reported judging score**.

Resolved wording:

> Five submissions passed the competition's structural/constraint checks. Eleven judging panels scored Fun, Creativity, and balanced Difficulty; excessive similarity could be penalized separately.

This is supported directly by [the author manuscript](https://matthewstephenson.info/papers/The%202017%20AIBIRDS%20Level%20Generation%20Competition.pdf) and the [archived official 2017 results page](https://web.archive.org/web/20210121085841id_/http://www.aibirds.org/level-generation-competition/2017-results.html).

### Artifact wording

At audit start, the artifact note was too pessimistic. An archived official AIBIRDS page links [stepmat/IratusAves](https://github.com/stepmat/IratusAves) as the winning generator, and its README identifies it as the winning 2017/2018 entry. The repository contains the generator, example outputs, Science Birds builds, and a **GPL-3.0** license. It also states that agent-performance and stability-analysis features were removed for compatibility, and it is not the complete five-submission/judging package.

Resolved status:

> **Partial, GPL winning-generator release** — the official competition site links the public IratusAves/MSG generator and examples, but the exact five submissions, task inputs, selected outputs, judge-level data, and removed analysis features are not packaged together.

The section and `levels competition` scope should remain unchanged.

## High-confidence omissions found and resolved / 已发现并补入的高置信漏项

### P0 dataset: Corpus for Angry Birds Level Generation (2019)

- Publisher record: [DOI 10.1109/ICOMET.2019.8673443](https://doi.org/10.1109/ICOMET.2019.8673443).
- First-party artifact: [AdeelZafar123/AngryBirdsDataSet](https://github.com/AdeelZafar123/AngryBirdsDataSet).
- The paper reports **200 tile-encoded levels: 100 original Angry Birds levels and 100 baseline-generator levels**. The public 2.8 MB ZIP currently contains 103 text-file entries covering only 100 unique original-level IDs; IDs 61, 62, and 75 are duplicated, packaging/dimension inconsistencies remain, and the claimed generated half was not found.
- At audit start, it was absent by exact title, DOI, and repository URL from the English index, Chinese index, and PCG source note.

**Resolved:** added as #114 under `Level and playable-content generation, repair, datasets, and benchmarks`, near VGLC and AIBIRDS, as generation-specific training data. Its final status is **Partial, public archive without a license**: the central ZIP is meaningful but incomplete relative to the paper, and the repository has no README/schema documentation, split manifest, code, release, metric implementation, or evaluator.

This is not a playing-agent corpus. The paper positions the data for machine-learning Angry Birds level generation, so it matches the repository's existing dataset exception; it is not presented as a trained-generator experiment or fixed benchmark.

### P0 paper: Using Unconditional Diffusion Models in Level Generation for Super Mario Bros (2023)

- Publisher record: [DOI 10.23919/MVA57639.2023.10215856](https://doi.org/10.23919/MVA57639.2023.10215856).
- Author manuscript: [ESSLab PDF](https://esslab.jp/publications/LeeMVA2023.pdf).
- First-author implementation: [hyeonjoon-lee/UnconditionalDiffusionSMB](https://github.com/hyeonjoon-lee/UnconditionalDiffusionSMB).
- Official metadata gives the exact title, authors Hyeon Joon Lee and Edgar Simo-Serra, year 2023, and MVA proceedings placement.
- At audit start, it was absent by exact title and DOI from all index and research files.

**Resolved:** added as #115 after a full artifact inspection. The method trains on 5,925 unique 14×14 windows from 33 VGLC ground-level files, and the released evaluator measures generated outputs rather than agent skill. The author repository contains preprocessing, training, generation, evaluation, raw levels, a simulator, example outputs, and a notebook, but no license, dependency manifest, required processed NPZ, checkpoint, evaluated sample arrays, or result bundle; final status is **Partial, unlicensed author code**. The direct Mario generation task is not a game-playing paper or an alias of another indexed version family.

## Benchmark coverage judgment / Benchmark 覆盖判断

The collection now covers the principal benchmark families already claimed in the public index:

- Mario AI level-generation track, the seven-generator comparative framework, and direct Mario diffusion-level evaluation;
- VGLC and the now-audited Angry Birds corpus as generation-specific training resources;
- GVGAI generation tracks and runtime boundary;
- AIBIRDS and ChatGPT4PCG physics-level competitions;
- the modern multi-domain PCG Benchmark;
- generation-evaluation methodologies and the unified Sokoban comparison;
- GDMC settlement generation as a clearly labelled component benchmark.

This is broad and correctly excludes ALE, Procgen, CoinRun, MineRL, and other playing-policy benchmarks. After adding #114–115, this audit has no remaining high-confidence omission to report. The index is still described as curated rather than exhaustive because future and hard-to-discover work can always surface.

## Final disposition / 最终处置建议

- **No scope blocker:** safe to state that the index is generation-only and excludes playing-only agents.
- **Resolved factual/artifact correction:** #111 was revised in both languages and its research note.
- **Resolved completeness actions:** the Angry Birds corpus and 2023 unconditional-diffusion Mario paper were added as #114–115 after artifact inspection.
- Keep wording such as “curated,” “research cutoff,” and “contributions welcome”; avoid “complete” or “exhaustive.”
