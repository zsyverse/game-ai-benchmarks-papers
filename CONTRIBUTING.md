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

## Automatic rejection / 自动拒绝

Do not propose dataset/corpus-only work, surveys, taxonomies, position papers, framework-only proposals, ordinary coding-agent tasks in existing game repositories, metric-only studies, standalone repair/QA/balancing/tuning, non-playable scenes, reskins, isolated asset or narrative generation, NPC/player agents, or policy/planning-centered world models.

不要提交纯数据集/语料库、综述、分类、立场论文、纯框架设想、既有游戏仓库中的普通 coding-agent 任务、纯指标研究、独立修复/QA/平衡/调参、不可玩场景、换皮、孤立资产或叙事生成、NPC/玩家智能体，或以策略/规划为核心的 world model。

## Quality rules / 质量规则

- Verify claims from the paper and official artifacts, not blogs, listicles, or repository names. / 根据论文和官方工件核验，不依赖博客、二手榜单或仓库名称。
- Do not call a dataset a benchmark unless the paper defines a fixed generation task, evaluator, and empirical protocol. / 没有固定生成任务、evaluator 与实证协议时，不要把数据集称为 benchmark。
- Merge versions of the same paper, but do not merge distinct follow-up papers merely because they share a system name. / 合并同一论文的不同版本，但不要仅因系统同名就合并实质不同的后续论文。
- Keep numbering, titles, years, URLs, availability labels, and section membership aligned across English and Chinese pages. / 保持中英文页面的编号、标题、年份、URL、可用性标签和分区一致。
- Run `python3 scripts/validate_index.py` and Markdown lint before opening a pull request. / 提交 PR 前运行 `python3 scripts/validate_index.py` 和 Markdown lint。
