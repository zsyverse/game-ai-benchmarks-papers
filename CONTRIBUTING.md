# Contributing / 参与贡献

This repository accepts only papers that pass the strict rules in [SCOPE.md](SCOPE.md): direct game-generation methods or formal benchmarks for those generation tasks.

本仓库只接受通过 [SCOPE.md](SCOPE.md) 严格规则的论文：直接生成游戏的方法，或正式评测这些生成任务的 benchmark。

## Before proposing an entry / 提交前

Search all three public collections first. The same paper must not be added to multiple categories, and a preprint must not be duplicated when its published version is already present.

请先搜索三个公开分类。同一论文不能添加到多个分类；已有正式发表版时，也不能再重复添加预印本。

## Required information / 必填信息

- Canonical paper title and year. / 论文正式标题与年份。
- One primary paper source: proceedings page, DOI, arXiv, or OpenReview. / 一个论文一手来源：正式论文集、DOI、arXiv 或 OpenReview。
- Exactly one role: **generation method paper** or **generation benchmark paper**. / 只能选择一种角色：**生成方法论文**或**生成 benchmark 论文**。
- The eligible generated output: complete game, code/project, rules/mechanics, playable content, or interactive game world. / 合格生成产物：完整游戏、代码/工程、规则/机制、可玩内容或交互式游戏世界。
- Primary-source evidence that generation is the paper's central contribution. / 一手来源证据，证明生成是论文核心贡献。
- For a benchmark: generation task, protocol, metrics, and empirical generator experiments. / 对 benchmark：需提供生成任务、协议、指标及生成器实证实验。
- Official code/data/model links and verified availability, if any. / 如有，请提供官方代码、数据、模型链接及已核验可用性。
- Concise, semantically aligned English and Chinese descriptions. / 简洁且语义一致的中英文描述。

## Copyable proposal template / 可复制的提案模板

Use this in an issue or pull-request description. Fill it from the primary paper and official releases; say what could not be verified. Missing code does not justify inventing a release or marking it Open. / 可复制到 issue 或 PR 描述中。根据原论文和官方发布填写，明确未核验内容；没有代码时不要编造链接或标成 Open。

```text
Title / 正式标题:
Year and version / 年份与版本:
Role / 角色: generation method OR generation benchmark
Collection / 分类: end-to-end OR pcg OR interactive-worlds
Paper / 论文一手来源:
Generated output / 生成产物:
Central generation evidence / 核心生成贡献证据: section/page/table
Evaluation and limits / 评测与局限: task, protocol, metrics, caveats
Official code / 官方代码:
Other artifacts / 数据、模型、项目页:
Status / 工件状态: Open OR Partial OR Closed; missing components
Checked on / 核查日期:
English summary:
中文描述:
Duplicate/version check / 去重与版本关系:
```

For the actual index, copy the destination table's schema, not the short homepage reading-list format. Preserve its numbered ID, year, linked title, task/output/evaluation fields and final artifact cell; PCG also has machine-readable output tags. Add the corresponding numbered source-dossier block. / 正式入库时沿用目标分类表的列结构，不使用首页的简短阅读条目代替。保留编号、年份、标题链接、任务/产物/评测字段及末尾工件列；PCG 还包含可机读的产物标签，并同步补充来源底稿中的对应编号。

Homepage reading picks reuse accepted records and are not counted again. Use consistent `Paper`, `Code`, `Project`, `Data` or `Models` labels where appropriate, retain material caveats, and never infer a paper's authors or venue from a similarly named repository. / 首页阅读起点复用已收录记录，不重复计数。简短资源标签保持一致，保留关键局限，不凭同名仓库推测作者或发表场所。

## Automatic rejection / 自动拒绝

Do not propose dataset/corpus-only work, surveys, taxonomies, position papers, framework-only proposals, ordinary coding-agent tasks in existing game repositories, metric-only studies, standalone repair/QA/balancing/tuning, non-playable scenes, reskins, isolated asset or narrative generation, NPC/player agents, or policy/planning-centered world models.

不要提交纯数据集/语料库、综述、分类、立场论文、纯框架设想、既有游戏仓库中的普通 coding-agent 任务、纯指标研究、独立修复/QA/平衡/调参、不可玩场景、换皮、孤立资产或叙事生成、NPC/玩家智能体，或以策略/规划为核心的 world model。

## Quality rules / 质量规则

- Verify claims from the paper and official artifacts, not blogs, listicles, or repository names. / 根据论文和官方工件核验，不依赖博客、二手榜单或仓库名称。
- Do not call a dataset a benchmark unless the paper defines a fixed generation task, evaluator, and empirical protocol. / 没有固定生成任务、evaluator 与实证协议时，不要把数据集称为 benchmark。
- Merge versions of the same paper, but do not merge distinct follow-up papers merely because they share a system name. / 合并同一论文的不同版本，但不要仅因系统同名就合并实质不同的后续论文。
- Keep numbering, titles, years, URLs, availability labels, and section membership aligned across English and Chinese pages. / 保持中英文页面的编号、标题、年份、URL、可用性标签和分区一致。
- Run `python3 scripts/validate_index.py` and Markdown lint before opening a pull request. / 提交 PR 前运行 `python3 scripts/validate_index.py` 和 Markdown lint。

## Editing workflow / 编辑流程

1. Search titles, system names, and paper identifiers with `python3 scripts/search_index.py "keyword"`. Search covers both languages and all three categories. / 用 `python3 scripts/search_index.py "关键词"` 查标题、系统名和论文标识符；检索覆盖双语及三个分类。
2. Add or update the corresponding English and Chinese rows under `docs/`. Keep the same category and number in both languages. / 同步新增或修改 `docs/` 下的中英文条目，保持分类和编号一致。
3. Add or update the matching numbered block in the category's [source dossier](research/README.md). Record the primary source, inclusion evidence, evaluation, and artifact availability; rejected candidates belong in the strict audit. / 同步更新该分类[来源底稿](research/README.md)中相同编号的证据块，记录一手来源、准入依据、评测和工件可用性；被拒候选记入严格审计。
4. If counts change, update both READMEs, collection introductions and headings, dossier totals, and `COLLECTIONS`, `EXPECTED_TOTAL`, and `EXPECTED_SECTION_HEADINGS` in `scripts/validate_index.py`. These are explicit assertions, not automatically generated totals. / 数量变化时，同步更新双语 README、分类页简介与分区标题、底稿总数，以及校验脚本中的上述三个常量；这些是显式断言，并非自动统计值。
5. Regenerate the compact reading views with `python3 scripts/build_paper_list.py --write`. The two `paper-list.md` files are derived from the canonical tables and numbered evidence headings; do not edit them by hand. / 用该命令重新生成双语速览。两份 `paper-list.md` 来自规范分类表和来源底稿的编号标题，不要手工修改。
6. Run the checks below from the repository root. / 在仓库根目录运行以下检查。

```bash
python3 scripts/validate_index.py
python3 scripts/build_paper_list.py --check
python3 -m unittest discover -s scripts -p 'test_*.py'
npx --yes markdownlint-cli2@0.23.2 "*.md" "docs/**/*.md" "research/**/*.md"
```

Python 3.10+ is required; Markdown lint also requires Node.js/npm. Search and index validation work offline. Lint may download its pinned package on first use. / 需要 Python 3.10+；Markdown lint 另需 Node.js/npm。检索与索引校验可离线运行，lint 首次使用可能下载指定版本的工具包。

Automatic checks verify structure, bilingual metadata, counts, identities, and local file links. They do not read the papers, verify external URLs live, or establish semantic equivalence of translated descriptions. `python3 scripts/check_links.py` checks external links live on demand (also run monthly by a scheduled workflow); publisher sites that block scripted clients are reported as `blocked` and need a browser check rather than an edit. Keep full-verification dates unchanged unless the full collection has actually been reverified. / 自动检查覆盖结构、双语元数据、数量、论文标识和本地文件链接，不会阅读论文、实时核验外链或判定描述翻译的语义一致性。`python3 scripts/check_links.py` 可按需实时检查外链（另有每月定时工作流）；拦截脚本访问的出版社站点会标为 `blocked`，需人工用浏览器核对而不是修改条目。只有确实重新核验完整集合时，才能更新完整核验日期。

## Repository layout / 仓库结构

The homepage is a reading/navigation layer; collection tables hold canonical metadata, and dossiers hold evidence. The generated [English](docs/en/paper-list.md) / [中文](docs/zh-CN/paper-list.md) compact lists offer a year-sorted reading view without another manually maintained catalog. See the [English](docs/en/search.md) / [中文](docs/zh-CN/search.md) search guide for filters and exports. / 首页用于阅读与导航，分类表保存规范条目，底稿保存证据。自动生成的速览按年份组织阅读，检索指南说明筛选和导出；编辑时保持层次分工。

```text
.
├── README.md / README.zh-CN.md       # Entry points / 阅读入口
├── SCOPE.md                         # Inclusion rules / 收录范围
├── CONTRIBUTING.md                  # Proposal and editing guide / 贡献说明
├── docs/
│   ├── en/                          # English collections and guide
│   └── zh-CN/                       # 中文分类与研究导读
├── research/                        # Evidence, reviews, held leads / 证据与待定线索
└── scripts/
    ├── build_paper_list.py          # Generated reading views / 自动生成速览
    ├── search_index.py              # Offline search/export / 离线检索与导出
    ├── validate_index.py            # Structure and metadata checks / 结构校验
    ├── check_links.py               # On-demand live link checks / 外链检查
    ├── test_build_paper_list.py      # View consistency tests / 速览一致性测试
    └── test_search_index.py         # Search regression tests / 检索回归测试
```
