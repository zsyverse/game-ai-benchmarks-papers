# Research evidence / 研究依据

The public index contains only canonical game-generation methods and formal generation benchmarks. These files preserve the primary-source evidence used to make those decisions.

公开索引只包含 canonical 游戏生成方法与正式生成 benchmark。以下文件保留判定所依据的一手来源证据。

**Latest integration / 最新整合：** [Completion review / 调研补完](completion-review-2026-09-08.md) records the current **203** entries, the original ANGELINA 3D paper correction, historical Sokoban addition, focused world-domain follow-up and practical experiment entry points. / 当前 **203 条**；原始方法归属、历史谜题、世界域续查和实验选型见该页。

## Source dossiers / 一手来源底稿

- [End-to-end game and game-code generation](end-to-end-generation-sources.md)
- [Automated game design and PCG](pcg-automated-design-sources.md)
- [Interactive game-world generation](interactive-world-generation-sources.md)

The dossiers correspond one-to-one with accepted public records and contain no extra candidates. Historical removal decisions are retained in the strict audit; the coverage notes below also preserve newly screened exclusions and unresolved leads.

三份底稿与公开收录条目一一对应，不含额外候选。历史删除决定保留在严格审计中；下方增补记录另保留本轮排除和待核验的线索。

## Reliability corrections / 可靠性纠错：2026-09-05

Start with the [critical re-audit / 可靠性复核](reliability-audit-2026-09-05.md): evidence locations, corrected claims, pending decisions and remaining limits. The prior 41-addition snapshot contained errors; it is not a quality certificate.

先读[可靠性复核](reliability-audit-2026-09-05.md)：包含原文定位、实质性纠错、待核验决定及局限。前轮 41 条增补快照存在错误，不作为调研质量证明。

## Coverage expansion and reconciliation / 覆盖增补与对账：2026-09-05

The preceding expansion was a **143 → 184** snapshot. The targeted re-audit yields **189 records**: split Matrix (+3), Hunyuan (+1), GenieRedux (+1), and the 2024 ChatGPT4PCG competition (+1); move MIPCGRL to pending (−1). The former ChatPCG/PCGRLLM row now represents PCGRLLM only; parameter-adjustment-only ChatPCG is not counted. A second targeted discovery pass added nine records to reach 198. Initial September 8 review admitted four more (Playing with Data, DATA Agent, ANGELINA Part II and Video2Game), reaching a 202-record snapshot. Subsequent original-paper comparison replaces Part II with ICCC 2014 *Ludus Ex Machina* (net zero); Taylor–Parberry's 2011 Sokoban method adds one, yielding **203 current records**. The Sonancia pair remains held. None of these passes is a new full-corpus audit.

前轮增补为 **143 → 184** 的历史快照；复核后为 **189 条**：Matrix 拆分净增 3，Hunyuan、GenieRedux、2024 ChatGPT4PCG 各净增 1，MIPCGRL 转待核验减 1。原 ChatPCG/PCGRLLM 条目仅保留 PCGRLLM，独立数值调参的 ChatPCG 不计数。同日第二轮定向查漏再增 9 条至 198；9 月 8 日初次复核再纳入 Playing with Data、DATA Agent、ANGELINA Part II 和 Video2Game 共 4 条，形成 202 条快照。同日进一步全文比对后，以 ICCC 2014 *Ludus Ex Machina* 替换 Part II（净增 0），再补 Taylor–Parberry 2011 Sokoban（+1），当前 **203 条**；Sonancia 两篇仍待核验。这些均不是全库重新审计。

| Collection / 分类 | Before / 原有 | Re-audit / 复核后 | Further discovery / 继续查漏 | Now / 当前 |
| --- | ---: | ---: | ---: | ---: |
| End-to-end / 端到端 | 34 | 37 | +1 | 38 |
| Automated design and PCG / 自动设计与 PCG | 86 | 111 | +9 | 120 |
| Interactive worlds / 交互世界 | 23 | 41 | +4 | 45 |
| Total / 总数 | 143 | 189 | +14 | 203 |

- [End-to-end additions and screening](end-to-end-coverage-expansion-2026-09-05.md): Mage, scenario-based serious-game generation, and executable card mechanics.
- [Historical full-game/rule generation](classic-game-coverage-expansion-2026-09-05.md): five additions, including cooperative co-evolution, VGDL evolution, chess-rule generation, random-forest-guided generation, and controllable game-system design.
- [PCG method and task coverage](pcg-coverage-expansion-2026-09-05.md): twenty additions spanning charts, Sokoban, dungeons, NCA, GFlowNets, iterative editing and recent controlled generation.
- [Interactive-world additions and versions](interactive-world-coverage-expansion-2026-09-05.md): early playable simulators, streaming world methods, two generation benchmarks, and separate follow-up papers.
- [中文研究导读](../docs/zh-CN/research-guide.md) / [English research guide](../docs/en/research-guide.md): synthesis of method families, benchmark differences and reading routes.

Independent audits of the first expansion, which changed no public records themselves but drove the corrections above:

对首轮增补的独立审计，本身不改动公开记录，但推动了上述纠错：

- [Classic full-game/rule additions (PCG #13–17) and the research guide](independent-classic-audit-2026-09-05.md)
- [PCG content additions (former #92–111)](independent-pcg-audit-2026-09-05.md)
- [Interactive-world additions and the Matrix/Hunyuan splits](independent-world-audit-2026-09-05.md)

## Further discovery and held leads / 继续查漏与待定线索：2026-09-05–08

The second pass searched author bibliographies, venue proceedings and citation chains rather than arXiv keywords alone. Thirteen records were integrated across September 5 and September 8; each note also keeps uncounted candidates and their specific evidence gaps.

第二轮查漏以作者著作目录、会议论文集和引用链为主，不只依赖 arXiv 关键词。9 月 5 日至 8 日共整合 13 条记录；各笔记同时保留已阅读但未计数的候选及其具体证据缺口。

- [Executable-game discovery](further-end-to-end-discovery-2026-09-05.md): ByteSized32 added as a generation benchmark (end-to-end #10); six candidates screened out.
- [Playable-content discovery](further-content-discovery-2026-09-05.md): two Refraction puzzle generators, simulation-guided Cut the Rope generation, and mission-graph evolution added (current PCG #113–116); racing-track and map-sketch leads held.
- [Interactive-world discovery](further-world-discovery-2026-09-05.md): Yume, SANA-WM, Wonder and Unbounded added (interactive worlds #38–41); Yume-1.5, RELIC and minWM held pending game-world output evidence.
- [Classic game-generation discovery](further-classic-discovery-2026-09-05.md): Playing with Data and DATA Agent accepted; the initial Part II method attribution is superseded by the original-paper review below. Sonancia 2015/2016 remain separate held identities.

**September 8 decisions / 9 月 8 日决定：** [integration and next gaps](further-research-integration-2026-09-08.md) records the four additional accepted papers, independent review, and reasons not to combine Sonancia's 2015 experiments with the changed 2016 playable demonstrator. Video2Game is counted once as reconstructed PCG playable content, with manual assembly and engine-rendering caveats.

[继续调研整合记录](further-research-integration-2026-09-08.md)说明新增四篇的依据，以及 Sonancia 两篇为什么不能跨文拼接证据。Video2Game 仅在 PCG 可玩内容中计一次，明确人工装配与引擎渲染边界。

**Later September 8 refinement / 同日后续补完：**

- [ANGELINA paper identities](angelina-paper-identity-2026-09-08.md): original ICCC 2014 method replaces Part II in #18, no count increase; journal curation and shared jam evidence remain separately attributed. / 原始方法替换，不增计数，不跨文移植策展实验。
- [Historical Sokoban and racing](racing-puzzle-followup-2026-09-08.md): Taylor–Parberry 2011 becomes PCG #120; racing remains held without full text. / 补入历史 Sokoban，竞速全文仍待核验。
- [World-domain follow-up](world-domain-followup-2026-09-08.md): Yume-1.5, RELIC and minWM remain separate held candidates; current releases do not inherit game-domain evidence from predecessors or training data. / 区分真实控制、发布状态和本版本游戏域输出。

Searches used primary arXiv discovery, citation following, publisher/author pages, and author-linked code/model releases. Most additions have inspected full-text method/evaluation evidence; the 2012 ACCME paper has an original abstract and two-page preview, while the 2016 chess-rule paper relies on its publisher abstract and a coauthor's later full text. These limits appear in their rows and notes. No external implementation was run and no reported experimental result was independently reproduced.

检索结合 arXiv、引用追溯、出版社/作者页面及官方代码/模型发布。多数新增条目核查了全文方法与实验；2012 年 ACCME 核查了出版社摘要和原版两页预览；2016 年棋类规则生成核查了出版社摘要及共同作者的后续全文。证据局限已在条目和笔记中注明。未运行外部实现，也未独立复现论文实验结果。

This is not a systematic census of every conference year. Inaccessible historical papers and general scene-generation candidates without established game interaction remain visible as unresolved leads rather than being counted.

本轮不是对所有会议年份的系统穷举。无法访问的历史全文、尚未确认游戏交互的通用场景生成等，作为未决线索保留，不直接计数。

## Experimental entry points / 实验选型与复现边界

- [Pinned artifact evidence and experiment reporting checklist / 固定版本工件证据与实验记录单](experiment-entry-points-2026-09-08.md): PCG Benchmark, Start Small, ByteSized32 and Matrix-Game version 1. Distinguishes benchmark versus experiment packages, authored-data-free versus solver-free training, API drift, dependency locks and version-specific hardware requirements. No implementation was executed. / 区分框架与实验包、无人工数据与无求解器、API 漂移、依赖锁及版本特定硬件要求；未运行第三方实现。

## Format references / 格式参考

Repository presentation has a separate [five-sample format audit / 五个高 star 清单格式核查](reference-format-audit-2026-09-08.md). It records GitHub star snapshots, fixed README revisions and the navigation/entry patterns adapted here; these samples are not evidence for including game-generation papers. / 格式调研与论文证据分开，不用样本热度决定论文收录。

## Strict scope audit / 严格范围审计

- [Two-pass method/benchmark-only audit: 198 candidates to 143 canonical records](strict-method-benchmark-scope-audit.md)

The audit applies one rule to every former row, then rechecks every survivor: keep only a direct generation method or a formal benchmark of an eligible generation task, and merge duplicate paper records globally.

该审计先对清理前全部条目使用同一规则，再逐篇复核所有保留项：只保留直接生成方法或合格生成任务的正式 benchmark，并在全仓库合并重复论文记录。

Last full verification / 最近一次完整核验：**2026-09-04**.
