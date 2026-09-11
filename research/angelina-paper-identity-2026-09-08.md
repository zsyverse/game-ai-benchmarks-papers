# ANGELINA 3D paper identity and evidence audit — 2026-09-08

> Implemented on 2026-09-08: public PCG #18 and its canonical dossier now use ICCC 2014 *Ludus Ex Machina*. Part II is a separately identified follow-up source, not a separately counted method or a renamed version. The main pass cross-checked original method passages and rendered evaluation pages before integration.

## Decision / 结论

**Replace the current PCG #18 primary paper with *Ludus Ex Machina: Building A 3D Game Designer That Competes Alongside Humans* (ICCC 2014), without increasing the count.** Keep *The ANGELINA Videogame Design System, Part II* as a separately identified follow-up evaluation/context source. Keep the AISB 2014 paper as a separately identified, non-counted precursor whose own generator evaluation is insufficient under `SCOPE.md`.

建议将当前 PCG #18 的主论文改为 **ICCC 2014 的 Ludus Ex Machina**，总数不变；Part II 作为身份独立的后续评测/上下文来源，AISB 2014 作为身份独立但自身评测不足的前驱保留在证据笔记中。**这不是把三篇论文认定为同一篇，也不是按系统品牌强行合并。**准入筛选与论文身份是两件事：ICCC 本文直接描述并评测合格的生成方法；本次未在 Part II 中确认相对该生成工作独立新增的 3D 生成方法，不能把对既有方法的新评测自动计为另一个生成方法。

The earlier note's “ICCC original unavailable” condition is resolved: the official PDF returned HTTP 200 on this check and was read in full. The three full texts were compared directly. No generator was executed, no historical game build was independently played, and no claim of complete historical ANGELINA-family deduplication is made.

## Primary sources and reading record

| Label | Paper identity | Source and verification |
| --- | --- | --- |
| A | Michael Cook, Simon Colton, Jeremy Gow. *Automating Game Design In Three Dimensions*. AISB Symposium on AI and Games, April 2014. | [Institutional record](https://research.gold.ac.uk/id/eprint/17354/) and [institutional full text](https://research.gold.ac.uk/17354/1/COM-Cook2014.pdf), all 4 PDF pages read. The institutional record identifies publication on 2014-04-01; the later deposit date is not a new publication. |
| B | Michael Cook, Simon Colton. *Ludus Ex Machina: Building A 3D Game Designer That Competes Alongside Humans*. ICCC 2014. | [Official proceedings](https://computationalcreativity.net/iccc2014/proceedings/) and [official full text](https://computationalcreativity.net/iccc2014/wp-content/uploads/2014/06/4.2_Cook.pdf), all 9 PDF pages read. The official proceedings explicitly identify the **Fifth** ICCC, Ljubljana, 9–13 June 2014, and this title/author pair. |
| C | Michael Cook, Simon Colton, Jeremy Gow. *The ANGELINA Videogame Design System, Part II*. Online 2016 / journal issue 2017. | [DOI](https://doi.org/10.1109/TCIAIG.2016.2520305), [institutional record](https://research.gold.ac.uk/id/eprint/18949/), [accepted full text](https://research.gold.ac.uk/18949/1/COM-Cook2016b.pdf), all 13 PDF pages read. Accepted manuscript and published journal versions remain one identity for C, not additional records. |

Page references below use the individual PDF page position; C also has printed manuscript page numbers. Text extraction was supplemented with rendered-page inspection of A Figure 1; B Figure 2, game-jam setup, and Table 1; C §V.C. This audit follows the research skill's primary-source policy and the PDF skill's visual checks for important figures/tables. Temporary downloaded PDFs and extracted text were kept outside the repository; this Markdown is the durable evidence record.

**Bibliographic trap:** C reference [27] calls B a paper from the “Third” ICCC in 2014. The official 2014 proceedings say Fifth. Use the venue's own record, not that erroneous ordinal copied from the journal bibliography. [B proceedings; C p. 12, ref. 27]

## A. AISB 2014: real generator, insufficient paper-level evaluation

### What the paper itself contributes

- A describes ANGELINA-5 as a Unity-based cooperative-coevolution system for complete themed 3D games, not merely a proposed Unity editor or isolated asset generator. §3.1 takes a theme word/phrase, selects a rare noun, expands associations, retrieves models/fonts/sounds, and constructs themed zones. Its music and title steps select/transform existing resources; they do not create all media from scratch. [A pp. 2–3, §3.1]
- §3.2 has four evolved species: **Level Design, Zoning, Placement, Ruleset**. Levels arrange human-authored tiles; placements specify player/exit and two entity types; rules combine supplied behaviour code such as movement, death and score. Expanding the behaviour stock through automatic code generation remains future work. [A p. 3, §3.2; p. 4, §4]
- §3.3 exports game data and only its needed assets to a separate Unity project, from which executable game binaries can be exported. Figure 1 expressly shows *Hit The Bulls-Spy*'s whole map and a screenshot of the final game **while running**. Playable-output evidence is therefore present, unlike a paper with only static geometry renders. [A pp. 1, 4, Figure 1 and §3.3]

### What is and is not evaluated

- A gives internal fitness definitions and a “typical” configuration of **40 individuals per species and 50 generations**. These are algorithm/configuration descriptions, not a measured result from an evaluated sample. [A pp. 3–4, §3.2]
- A contains no reported repeated-run experiment, numerical outcome table, convergence graph, generator comparison, player study, or evaluation of its illustrated output beyond showing that it exists. The 150 manually analysed jam themes concern the construction of the theme-extraction heuristic, not 150 evaluated generated games. [A pp. 1–4; §3.1 and §3.2]
- Its §4 identifies richer games, automatic entity code, and modular/evolved fitness functions as future work. Do not import those capabilities from Mechanic Miner or later ANGELINA versions into this record. [A p. 4, §4]

**Admission decision:** HOLD/non-counted technical precursor. A meets direct generation and playable-output requirements but does not independently report enough generator evaluation under the repository's strict scope. B's later fitness graph and jam results cannot retrospectively become A's experiment. A and B are separate papers, with different titles and author lists; the shared system and example game do not make them identical publications.

## B. ICCC 2014: supported primary generation-method record

### Generator and output

- The central contribution is the implemented ANGELINA-5 3D game designer and its entry into a human game-design contest. B describes the whole predesign/design/postdesign pipeline rather than treating the generator as an incidental evaluator input. [B p. 1, Abstract and Introduction; pp. 2–5, Design Process]
- A phrase is reduced to a theme word and expanded via associations. Asset retrieval and texture/audio zoning supply multimedia inputs. Cooperative coevolution then evolves **four species: level, zone map, entity placement and ruleset**. Stock behaviours supply the executable rules; this is not free-form invention of arbitrary new rule code. [B pp. 2–5, Predesign Phase and Design Phase]
- Fitness combines local checks with a complete candidate game assembled from current species exemplars. A simple controller attempts to reach the exit and records triggered rules. Level continuity, zone connectedness, entity spread and path distance contribute to selection. These checks do not prove universal solvability or rich gameplay. [B pp. 4–5, Design Phase]
- Postdesign exports a separate Unity project containing the design data and needed assets, then executable binaries. The work therefore produces **complete runnable games**, not just theme matching, downloaded artwork, an abstract layout, or a patch to an existing game. [B p. 5, Postdesign Phase]

### Empirical evidence that belongs to B

1. **Figure 2, one run:** a fitness-versus-generation plot for the four species. The text expressly calls it a sample/single run and reports little evolutionary improvement in the Zone Map and Ruleset species, which it describes as underdeveloped. Level and Placement show clearer improvement. It is not a repeated-seed statistical study. The stated typical configuration is **30 individuals per species, 40 generations**, different from A's illustrative configuration. [B p. 5, Figure 2 and Evolutionary Performance]
2. **Ludum Dare 28, December 2013:** two generated entries, *To That Sect* and *Stretch Bouquet Point*. The paper's contest setup is **60 generations** with populations of **35 level / 35 placement / 20 ruleset / 15 zone**, and approximately **three hours per game**, including web-asset retrieval. These are the jam setup/timings, not the typical setup used elsewhere in the paper. [B p. 6, ANGELINA and Ludum Dare 28]
3. **Table 1:** overall positions **500 and 551 among 780 jam-track submissions**. The 2,064 figure elsewhere is both tracks together; it is not the denominator for these rankings. Overall is its own rating category, not the mean of the other seven. [B pp. 2, 6–7, Game Jams and Table 1]
4. *To That Sect* disclosed software authorship; *Stretch Bouquet Point* used a pseudonym and edited commentary without that disclosure. The authors rated equal numbers of other submissions from the two accounts to seek comparable visibility, but these were **different games**, not the same game randomized across disclosure conditions. Specific voting data were unavailable. Potential attribution bias is plausible but not causally isolated or statistically established by this design. [B pp. 6–7, setup and Results]

| Table 1 ranking, lower is better | To That Sect | Stretch Bouquet Point |
| --- | ---: | ---: |
| Overall | 500 | 551 |
| Fun | 515 | 543 |
| Audio | 211 | 444 |
| Graphics | 441 | 520 |
| Mood | 180 | 479 |
| Innovation | 282 | 525 |
| Theme | 533 | 545 |
| Humour | 403 | 318 |

The disclosed entry ranked higher in seven of eight categories, but this is descriptive evidence only. Neither the table nor being ahead of some human entries establishes “human-level game design.” The paper discusses simplistic gameplay, weak/erroneous word associations, little variation in core objectives, and a generated soundtrack that can be overwhelmed by loud chanting. [B pp. 6–8, Entries, Results and Future Work]

### Artifact status

The inspected B paper links historical playable entries through `http://tinyurl.com/tothatsect` and `http://tinyurl.com/stretchpoint`; its Unity output/export description is not a released generator package. No official paper-specific runnable generator, source distribution or reproduction package was verified in this audit. Use **Closed/unverified** with that narrow meaning, not “proved never released.” Historical links, a PDF, or a pictured game are not evidence of a currently reproducible pipeline.

**Admission decision:** ACCEPT as the primary `full-game` generation-method paper for this 3D lineage. Replace the current #18 primary identity rather than add another counted record on top of C. This replaces a weakly attributed journal-method entry with a directly supported original method paper; it does not assert that B and C are bibliographically the same paper.

## C. Part II: distinct follow-up, overlapping generator and jam evidence

### Its own content and additional evaluation

- C §III describes the earlier ANGELINA3 news-conditioned Metroidvania generation: news/media acquisition, an artistic-direction species tied to reachable map regions, and template-based commentary. Its example games are explicitly dated May 2012. §V.B explicitly points to the earlier *Aesthetic Considerations for Automated Platformer Design* for an initial creativity assessment. This audit does not claim to re-audit or merge the entire 2012 family. [C pp. 3–7, §III; p. 9, §V.B and ref. 30]
- C §IV calls the themed 3D system ANGELINA4 and refers directly to B, reference [27], for both predesign details and the species/evolutionary parameters. Its short summary lists **three** species rather than B's four. This difference in naming/summary is real, but C supplies neither a clear changed zoning algorithm nor a before/after experiment establishing an independent new generator; do not infer a new method solely from the count discrepancy. [C p. 7, §IV.A–B]
- C §V.A / Figure 8 repeats the **same two December 2013 Ludum Dare 28 entries and all eight ranking pairs** in B Table 1. It also notes later contest participation, but does not provide another comparable outcome table for those events. The repeated 500/551 result is **one shared empirical event**, not two independent validations. [B p. 7, Table 1; C p. 8, §V.A and Figure 8]
- C does add a **curation assessment absent from A and B**: 30 games each from ANGELINA1, ANGELINA3 and ANGELINA4, with curation coefficients of **33%, 60% and 80%**. The paper defines this as the proportion the system's designer would be happy to show others and explicitly calls it entirely subjective. It is not an independent player rating, playable rate, success rate, or proof of 80% autonomous-quality output. [C p. 9, §V.C]
- C also develops the FACE-model analysis and proposes dependence/independence and sequential/parallel extensions to a PCG taxonomy. These are evaluation/classification contributions. They should not be mislabeled a new substantive generation algorithm. [C pp. 9–11, §V.B and §VI]

### Scope and identity decision

**Keep C as an independently cited follow-up evaluation/context source, not a second counted generation method in this local correction.** It is not just a renamed B or its published version: the author list, scope, news-generator discussion, curation experiment and classification contributions differ. Conversely, publication-level distinctness does not automatically satisfy the repository's requirement that the central contribution be a substantive generator or a formal generation benchmark.

Within these three primary texts, B provides the strongest original method-plus-evaluation basis for the themed 3D generation entry. C points back to B for the 3D method and reuses its jam evidence, while its identifiable additions here concern assessment, curation and conceptual framing. No independent added 3D generation contribution was verified that warrants another method count. This is a conservative scope decision, **not a claim that journals can never extend conference work, nor a rule that any overlap in experiments means duplicate papers**.

If future work establishes a genuinely distinct, evaluated generation contribution in C relative to the already indexed predecessors, re-assess that contribution explicitly. Do not restore a separate count merely because C contains another experiment, because it is a journal paper, or because ANGELINA4 and ANGELINA-5 look like different version names.

## Provenance map: avoid moving evidence between papers

| Evidence | A: AISB 2014 | B: ICCC 2014 | C: Part II |
| --- | --- | --- | --- |
| *Hit The Bulls-Spy* map/running screenshot | Figure 1 | Figure 1 | Not the 3D evaluation example used here |
| Typical evolution configuration | 40 individuals/species, 50 generations | 30 individuals/species, 40 generations | Directs readers to B for 3D parameters |
| Single-run four-species fitness graph | Not reported | Figure 2 | Not an independent repeated result |
| 2013 jam: *To That Sect* / *Stretch Bouquet Point* | Not reported | Table 1; original detailed report in these sources | Figure 8; same event and ranking pairs |
| Curation of 30 outputs from each of three versions | Not reported | Not reported | §V.C, additional subjective assessment |
| New 3D rule-code invention | Future work | Future work | Premade rule database; no verified new 3D rule-invention method |

This table tracks **evidence provenance**, not an assertion that A/B/C are versions of one paper.

## Suggested public #18 replacement rows

Keep the public category and record count stable. Link C as “follow-up evaluation” if desired, not as a parenthetical alternate title or published version. A remains a non-counted precursor in the dossier.

| # | Year | Paper | Output | Generation method/task | Evaluation | Artifacts/status |
| ---: | :---: | --- | --- | --- | --- | --- |
| 18 | 2014 | [Ludus Ex Machina: Building A 3D Game Designer That Competes Alongside Humans](https://computationalcreativity.net/iccc2014/wp-content/uploads/2014/06/4.2_Cook.pdf) ([follow-up evaluation: Part II](https://doi.org/10.1109/TCIAIG.2016.2520305)) | `full-game` | Theme-conditioned cooperative coevolution of Unity level geometry, zones, entity placements and stock executable rules, packaged with retrieved assets as complete games. | One-run fitness graph and two Ludum Dare entries ranked 500/551 of 780; underdeveloped rule/zone evolution and uncontrolled authorship-disclosure comparison limit conclusions. | **Closed/unverified** — no official paper-specific runnable generator or reproduction package verified. |
| 18 | 2014 | [Ludus Ex Machina: Building A 3D Game Designer That Competes Alongside Humans](https://computationalcreativity.net/iccc2014/wp-content/uploads/2014/06/4.2_Cook.pdf)（[后续评测：Part II](https://doi.org/10.1109/TCIAIG.2016.2520305)） | `full-game` | 根据主题协同进化 Unity 关卡几何、分区、实体布局与预制可执行规则，结合检索资产导出完整游戏。 | 单次运行 fitness 曲线及两款 Ludum Dare 作品，在 780 项中列第 500/551；规则/分区进化不足，作者身份披露比较并非受控实验。 | **Closed/unverified** — 未核实论文专属官方可运行生成器或复现包。 |

## Suggested canonical dossier block

### 18. Ludus Ex Machina: Building A 3D Game Designer That Competes Alongside Humans

- **Primary identity:** Michael Cook and Simon Colton; ICCC 2014. [Official paper](https://computationalcreativity.net/iccc2014/wp-content/uploads/2014/06/4.2_Cook.pdf), [venue contents](https://computationalcreativity.net/iccc2014/proceedings/). The official conference is the Fifth ICCC, despite Part II reference [27]'s incorrect “Third.”
- **Role/output:** generation method, `full-game`. Theme-conditioned cooperative coevolution over level designs, zone maps, entity placements and executable rules, with retrieved media and standalone Unity export. Human-authored tile/behaviour libraries bound the design space; automatic creation of arbitrary entity-rule code is future work. [B pp. 2–5]
- **Evaluation:** B Figure 2 is a single-run four-species fitness trace, not repeated-seed evidence. B Table 1 reports *To That Sect* / *Stretch Bouquet Point*, 500/551 overall among 780 December 2013 Ludum Dare jam-track entries. The paper reports about three hours per jam entry including asset retrieval. [B pp. 5–7]
- **Limits:** simplistic core gameplay and limited rule/zone evolution; two different games confound the disclosed/undisclosed-author comparison; raw voting data were not obtained. Rankings support evaluated generated output, not human-level design or a quantified attribution-bias effect. [B pp. 5–8]
- **Artifacts:** Closed/unverified; no official paper-specific generator or reproduction package verified. Historic game-entry links and Unity export descriptions do not establish current reproducibility.
- **Identity and follow-up:** A, the AISB 2014 paper, is a separately identified precursor with playable-output evidence but no adequate standalone generator evaluation. C, Part II (DOI 10.1109/TCIAIG.2016.2520305), is a separate follow-up source, not B's renamed/published version. It repeats the same jam results and adds subjective curation of 30 outputs each from three versions (33/60/80%), plus creativity/taxonomy analysis. C is not separately counted in this correction because no distinct added generation contribution was verified. Do not transfer C's curation figures into B's own experiment list.
- **中文要点：** 原始生成方法以 ICCC 2014 为准；四物种协同进化完整 Unity 游戏，但图块、行为和媒体资源仍依赖预制/检索输入。单次 fitness 曲线和两项 game jam 结果不等于多种子统计、通用可通关保证或人类水平设计。Part II 的策展实验是后续作者主观评测；三篇论文身份各自保留，公开方法条目仅计此项。

## Integration cautions

1. This proposal **replaces** #18; it adds no count and needs no downstream renumbering.
2. Update current prose that calls Part II newly discovered independent 3D generation work. Preserve dated historical reports as history, but add a pointer to this correction where a reader could otherwise mistake an old conclusion for the current decision.
3. Do not put “33/60/80% curation” in B's evaluation cell without explicitly marking it as a later C experiment. Do not retain “news/theme-conditioned” in B's method description if that suggests the earlier Guardian-news selection pipeline is B's newly introduced method.
4. Do not claim A, B and C are one canonical paper. Only C's own accepted/online/issue versions share that identity; A and C are non-counted literature sources for different scope reasons.
5. This audit is deliberately local to these three papers and the current #18 correction. It does not certify every previously indexed ANGELINA record, nor establish that every older paper or historical game link has been rechecked.
