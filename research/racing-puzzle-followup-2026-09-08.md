# Racing and Sokoban follow-up — 2026-09-08

> Integration completed on 2026-09-08: the main pass independently read the original paper and visually rechecked its experimental page, then added the Sokoban method as public PCG #120. The draft rows below preserve the recommendation stage. Racing remains held; see the [latest integration](completion-review-2026-09-08.md).

## Outcome and evidence boundary

**Recommend one addition:** Joshua Taylor and Ian Parberry's *Procedural Generation of Sokoban Levels* (GAMEON-NA 2011). The full author-hosted conference paper independently demonstrates a new generator, actual JSoko-compatible playable output, and generator experiments. The racing-paper lead remains **held**, with a more precise access diagnosis: the institutional record is available but explicitly has no attached files, while the inspected ACM landing/PDF requests are blocked.

This is a bounded follow-up to [the September 5 discovery note](further-content-discovery-2026-09-05.md), covering only these two papers under [SCOPE.md](../SCOPE.md). It is not a complete historical puzzle/racing survey. No third-party generator, game, solver, or experiment was executed. Scientific claims come from the original paper; later studies are not borrowed to fill missing evidence. Public-index integration is left to the main research pass.

## 1. Procedural Generation of Sokoban Levels — recommend

### Primary sources and canonical identity

- **Conference paper:** Joshua Taylor and Ian Parberry, *Procedural Generation of Sokoban Levels*, GAMEON-NA 2011, pp. 5–12. The [author publication list](https://ianparberry.com/pubs/) identifies the venue as the 6th International North American Conference on Intelligent Games and Simulation, EUROSIS. The running header of the [complete conference PDF](https://ianparberry.com/pubs/GAMEON-NA_METH_03.pdf) uses the short description “6th Annual North American Conference on AI and Simulation in Games.” These refer to the same paper, not separate records.
- **Author project page:** [Sokoban Generator](https://ianparberry.com/research/sokoban/), directly linked by the paper's introduction and reference list through its former `larc.unt.edu` address. The current author-hosted page links the same conference PDF, [technical-report version](https://ianparberry.com/techreports/LARC-2011-01.pdf), level sets, experimental data, and JSoko playback instructions. Treat the technical-report link as an alternate version, not an additional paper.
- **Identifier caution:** no conference-paper DOI was verified. Crossref's `10.12794/metadc801887` belongs to Joshua Taylor's differently titled *The Procedural Generation of Interesting Sokoban Levels* repository item, not a verified DOI for this coauthored conference paper. Do not attach it to the public row.
- **Distinctness:** this 2011 paper generates room geometry, goal positions, and initial box/avatar states. It is not the already indexed 2019 *Procedural Generation of Initial States of Sokoban*, nor a renamed neural Sokoban generator. The author site's linked 2015 player-attention study is a distinct later work; its human results are not evidence from this 2011 paper and are not newly admitted here.

### Generation representation and eligible playable output

The method section on printed pp. 6–8 has three substantive stages, all in the same generator:

1. **Construct a new room.** Randomized, rotated/reflected 3×3 wall/floor templates tile a user-sized grid; overlapping template borders must agree. Failed partial layouts are discarded. Post-checks reject disconnected floor, large open rectangles, insufficient free space, and selected dead ends. This is generative construction from templates, not only solving or repairing a supplied puzzle.
2. **Place goals.** The implementation tries combinations of goal positions by brute force in randomized order. A time limit can return the best result found so far; an interrupted search should not be described as a completed global optimum.
3. **Choose starting states by reverse search.** Starting with boxes on the goal squares, a memory-saving double iterative-deepening procedure seeks states whose shortest solution path is longest. The implemented distance is **box lines**: consecutive pushes of one box in one direction count as one line. Avatar positions are abstracted to reachable connected regions. Reversing legal solution transitions establishes solvability of the produced states; the system does not need a separate forward solver to reject unsolvable candidates.

An additional level-set layer ranks/selects generated sibling states, applies author-chosen heuristic penalties/rewards, removes exact rotation/reflection duplicates after dropping avatar position, then writes sorted level sets to files. This is an internal generation/selection stage, not a separate paper. The score and difficulty-sort formula are subjective heuristics; their existence does not establish validated human difficulty or enjoyment.

**Playable integration is explicit:** the introduction on p. 5 directs readers to several hundred generated levels and an existing Java game, JSoko, on which to play them. The “Experimental Results” section and Figure 6 show generated levels in that game. The [author project page](https://ianparberry.com/research/sokoban/) gives concrete `Load Level → External Level` instructions and supplies five text-format level sets. It explicitly says the authors did **not** create JSoko. Therefore the eligible output is **playable Sokoban puzzles/levels**, not a complete new game, and the external game's openness is not the generator's openness.

### Evaluation: units, denominators, and limits

The “Experimental Results” section, printed pp. 8–10, evaluates offline generation time and resulting solution length. All table entries average **10 random samples per setting**, using an Intel i7 3.2 GHz quad-core/hyperthreaded machine. The implementation itself does not use multiple cores; the authors run independent copies concurrently. No modern-hardware or single-process-throughput claim follows.

**Size is measured in template blocks, not individual tiles.** The explicit example on p. 9 says a 2×2 puzzle has 36 cells: four 3×3 templates. Figure 3 visually confirms the block layouts. Do not describe the 2×2 setting as a four-cell Sokoban puzzle or compare it directly to modern papers' tile-grid sizes.

| Original table and setting | Reported average generation time | Reported average solution moves | Correct reading |
| --- | --- | --- | --- |
| Table 1: 2 boxes; 1×2, 2×2, 2×3, 3×3 template grids | <1 s, 1.9 s, 16 s, 128 s | 26, 48, 60, 73 | Ten samples for each size; cheap two-box cases do not establish real-time generation for larger cases. |
| Table 2: 3 boxes; same four template grids | 58 s, 2.7 min, 1.1 h, 24.5 h | 38, 69, 98, 115 | The largest reported three-box setting takes approximately one day on average. |
| Table 3: fixed 2×2 template grid; 2, 3, 4, 5 boxes | 1.9 s, 2.7 min, 3.4 h, 26 h | 48, 69, 100, 109 | Ten samples per box count; the first two conditions overlap Tables 1–2, so do not sum all displayed rows as distinct samples. |

The “Moves” columns are measured with JSoko's **“move optimal with best pushes”** autosolver, whereas the generator's distance objective uses **box lines**. These are different metrics. The proof-by-construction of solvability should also be separated from this post-generation solution-length measurement.

The text reports separate four-hour-limited examples with 5–6 boxes, but gives no sample denominator or controlled success rate for that demonstration. It also reports that a more ordinary iterative-deepening variant is several times faster but can crash above 1.5 GB on some levels, whereas the proposed method stayed below 40 MB on those levels; the comparison is not a broad memory benchmark with a published per-case denominator.

The theoretical runtime is described as exponential/combinatorial. The original text's general statement that three-box levels can be generated in minutes must not obscure Table 2's larger settings measured in hours. “Offline” is the appropriate public description.

### What the paper does not establish

- **No human interest or difficulty validation in this paper.** Printed p. 10 explicitly says: “we provide no justification for this claim in this paper” about the authors finding the puzzles interesting. Playtesting is future work. Do not write that users preferred the outputs or that difficulty control was psychologically validated.
- **No general superiority over human-designed puzzles or competing generators.** The quantitative study mainly varies size and box count and reports runtime/solver moves. The introduction's motivation about human designs does not become a controlled comparison.
- **No unconditional global-hardness optimum under the timer.** Reverse construction ensures the returned candidates are solvable; the exhaustive “farthest” objective is not guaranteed to be fully optimized when search is cut short.
- **No full duplicate/diversity guarantee.** Exact rotation/reflection removal still leaves puzzles that humans would regard as similar, acknowledged on p. 8. Structural rejection rules and heuristic ranking may also restrict variety.

### Artifact inspection — Partial, data/levels available

This is stronger evidence than a merely clickable “code” link, but weaker than a released generator implementation:

- The [author project page](https://ianparberry.com/research/sokoban/) and all five **actual level-file responses** were fetched on 2026-09-08: [level1.txt](https://ianparberry.com/research/sokoban/level1.txt), [level2.txt](https://ianparberry.com/research/sokoban/level2.txt), [level3.txt](https://ianparberry.com/research/sokoban/level3.txt), [level4.txt](https://ianparberry.com/research/sokoban/level4.txt), [level5.txt](https://ianparberry.com/research/sokoban/level5.txt). All returned HTTP 200, with respectively 9,351; 9,690; 22,152; 10,719; and 10,379 bytes. Inspected response prefixes contain real ASCII Sokoban boards, avatar/box/goal markers, and generation-time/box-line comments, not empty files or HTML error pages. These are author-provided artifacts, not independently validated solutions.
- The [experiment ZIP](https://ianparberry.com/research/sokoban/SokobanPaperData.zip) was fetched successfully, HTTP 200, **33,396 bytes**. Its actual ZIP manifest was inspected in memory: **23 files**, comprising 11 condition-named level text files, 11 matching `Sln` solver-result text files, and `fdg sokoban paper data.xlsx`. The filename's `fdg` string is not evidence that this is a different published paper; the official project page links it as the data for the 2011 conference paper.
- Read the `Sln 2x3-2.txt`, `Sln 2x3-3.txt`, and `Sln 2x3-4.txt` contents: each lists 10 levels with moves, pushes, solver time and “solved” status. These are **archived author solver reports**, not results reproduced in this pass. The ZIP also contains the extra `2x3-4` condition; do not assume all files map one-to-one to displayed table rows without further data reconciliation.
- The spreadsheet was **not opened or analytically reconciled** with the paper; listing its name establishes presence only. No generator source or build/reproduction scripts appeared in the inspected ZIP, paper links, or author project page. The author's [GitHub account](https://github.com/Ian-Parberry), linked from his site's menu, was also checked through its current repository listing; no paper-specific Sokoban generator release was found there.
- Recommended label: **Partial — author-released playable level sets and experiment data/logs; no core generator source or turnkey reproduction package verified.** This is a date-limited inspection statement, not a claim that no source was ever released. JSoko is third-party software and must not be passed off as the authors' generator code.

### Candidate bilingual public rows

These are drafts for one canonical `puzzles` content-method record. `NEW` is a placeholder, not a second record or final index number.

| # | Year | Paper | Output | Generation method/task | Evaluation | Artifacts/status |
| ---: | :---: | --- | --- | --- | --- | --- |
| NEW | 2011 | [Procedural Generation of Sokoban Levels](https://ianparberry.com/pubs/GAMEON-NA_METH_03.pdf) ([author project](https://ianparberry.com/research/sokoban/)) | `puzzles` | Constructs new template-based rooms, searches goal placements, and reverse-searches solvable starting states using box-line distance; exports JSoko-compatible level sets. | Ten samples per size/box-count setting measure offline generation time and solver moves; larger cases take hours, and human interest/difficulty is not validated. | **Partial** — author-released playable levels and experiment data/logs; no core generator source or turnkey reproduction package verified. |
| NEW | 2011 | [Procedural Generation of Sokoban Levels](https://ianparberry.com/pubs/GAMEON-NA_METH_03.pdf)（[作者项目](https://ianparberry.com/research/sokoban/)） | `puzzles` | 构造模板房间、搜索目标位置，再按箱子推行线距离反向搜索可解初态，导出 JSoko 可玩的关卡集。 | 每个尺寸/箱数设置 10 个样本，测离线生成耗时和求解步数；较大实例耗时数小时，未验证玩家兴趣或主观难度。 | **Partial** — 作者关卡集及实验数据/日志可取得；未核实核心生成器源码或一键复现包。 |

### Suggested research-guide takeaway

**EN:** Reverse construction can guarantee puzzle solvability without a forward solver in the generation loop, but the objective used for search, the metric reported by a downstream solver, and the difficulty experienced by players are separate quantities. Taylor–Parberry 2011 explicitly illustrates this distinction and the offline cost of exhaustive search.

**中文：** 反向构造可以在生成环节不调用正向求解器的情况下保证可解，但“搜索优化的距离”“下游求解器统计的步数”和“玩家感受到的难度”是三件事。Taylor–Parberry 2011 同时说明这种区别以及穷举搜索的离线成本。

## 2. Interactive Evolution for the Procedural Generation of Tracks in a High-End Racing Game — continue to hold

### Metadata verified; full-text evidence still missing

- **Exact record:** Luigi Cardamone, Daniele Loiacono and Pier Luca Lanzi, GECCO 2011, pp. 395–402, [DOI 10.1145/2001576.2001631](https://doi.org/10.1145/2001576.2001631). The [Crossref publisher-deposited record](https://api.crossref.org/works/10.1145/2001576.2001631) confirms title, ordered authors, page range, date, and the official ACM landing/PDF URLs. It is metadata support, not a substitute for method/experiment sections.
- **Institutional page recovered:** [Politecnico di Milano record](https://re.public.polimi.it/handle/11311/609170), HTTP 200 on this pass, confirms the title/authors/year but explicitly states **“Non ci sono file associati a questo prodotto”**: there are no files attached to this record. The previous note's “institutional access intermittent” can therefore be updated to this precise current finding; this page is not a hidden full-text download.
- **Publisher access:** the [ACM landing page](https://dl.acm.org/doi/10.1145/2001576.2001631) and [official PDF endpoint](https://dl.acm.org/doi/pdf/10.1145/2001576.2001631) both returned HTTP 403 challenge pages, not article text. No attempt was made to bypass the challenge or use a restricted account.
- **Author-route check:** Daniele Loiacono's [current university homepage](https://loiacono.faculty.polimi.it/) is available and links a CV and Scholar profile, but the inspected page does not supply this manuscript. The former Lanzi faculty route redirected to an intranet login. A Semantic Scholar DOI lookup returned no open-access PDF URL; that secondary lookup was used only to locate possible sources, not to support scientific claims. Search-engine attempts did not recover a verified author manuscript.

### Admission decision and next requirement

**Hold outside the public count.** The recovered material still does not let this pass verify the paper's generation representation, actual game/export integration, experimental denominators, preference claims, or official generator artifacts. No game name, participant count, measured benefit, or Open/Closed label is inferred from the title, abstract, venue, or surrounding citations. Distinctness from the existing 2007 racing work is plausible but does not by itself satisfy admission.

The next useful action is to obtain an authorized full conference paper or author manuscript, then check generation representation, actual playable instantiation, evaluation unit/sample counts, limitations, and release provenance. Repeating the institutional page alone will not fill the gap, because it has no attachment.

There is deliberately **no proposed public scientific row** for this held paper: such a row would invite unsupported method/evaluation content. A bilingual evidence-ledger summary is safe:

| Language | Held-lead summary |
| --- | --- |
| EN | GECCO 2011 identity verified; the institutional record has no attached file and ACM full text was inaccessible in this pass. Keep uncounted until primary full-text method, playable-output and evaluation evidence is recovered. |
| 中文 | 已确认 GECCO 2011 论文身份；机构记录没有附件，本次无法取得 ACM 全文。保留线索但不计数，待原文核实方法、可玩产物和评测证据。 |

## Inspection record for handoff

- Complete Sokoban paper: all eight PDF pages were text-extracted and read, including method, experiments, conclusion, references and biography; printed pp. 9–10 were also rendered and visually checked for Tables 1–3 and Figures 3–5. This directly confirmed the 24.5 h/26 h entries, 10-sample captions and 36-cell example.
- Temporary cross-review files: `/tmp/racing-puzzle-research.jdQ4nW/sokoban-2011.pdf`, `/tmp/racing-puzzle-research.jdQ4nW/sokoban-2011.txt`, `sokoban-5.png`, and `sokoban-6.png`. These temporary paths are not repository deliverables or permanent citations.
- Level files and ZIP were fetched/read in memory, not executed; the ZIP manifest and three solver logs were inspected. No spreadsheet analysis, complete artifact reproduction, user study or gameplay was performed.
