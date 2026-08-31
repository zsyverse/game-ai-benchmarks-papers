# Contributing / 参与贡献

Thanks for helping keep this map accurate and useful. 感谢你帮助维护这份准确、实用的资料索引。

This repository covers **systems that generate games**, not systems that play them. Read [SCOPE.md](SCOPE.md) before proposing an entry.

本仓库收录的是**生成游戏的系统**，而不是玩游戏的智能体。提交条目前请先阅读 [SCOPE.md](SCOPE.md)。

## Add or correct an entry / 新增或修正条目

Please open an issue or pull request with:

- canonical title and year;
- one primary-source link (paper page, proceedings, project page, or official repository);
- type: benchmark, environment, dataset, paper, or tool;
- entry role: core generator, generation-specific resource, or explicitly labelled boundary/framing work;
- generation scope: complete game, code/project, rules/mechanics, level/playable content, or interactive world;
- task and evaluation metric, if it is a benchmark;
- code/data availability and license, if known;
- a concise English and Chinese description.

请通过 Issue 或 Pull Request 提供：

- 正式标题与年份；
- 至少一个一手来源链接（论文页、正式论文集、项目主页或官方仓库）；
- 类型：基准、环境、数据集、论文或工具；
- 条目角色：核心生成器、生成专用资源，或明确标注的边界/领域框架；
- 生成范围：完整游戏、代码/工程、规则/机制、关卡/可玩内容或交互世界；
- 如果是基准，请写明任务和评测指标；
- 已知的代码、数据可用性与许可证；
- 简洁且语义一致的中英文说明。

## Quality rules / 质量规则

- Prefer primary sources over blogs and listicles. / 优先引用一手来源，不以博客或二手榜单代替。
- Do not label a demo or dataset as a benchmark without an evaluation protocol. / 没有评测协议的演示或数据集不要标为基准。
- Verify artifact status from the official repository or hosting page; a paper's “we release” statement is not sufficient by itself. / 必须在官方仓库或托管页面核验工件状态；不能只依据论文中的“我们已发布”。
- Avoid duplicated links and marketing claims. / 避免重复链接和未经验证的宣传性描述。
- Merge preprints, conference/journal extensions, and renamed releases of the same system into one version family unless the generated task or system is materially different. / 同一系统的预印本、会议/期刊扩展和更名版本应合并为一个版本族；只有生成任务或系统有实质差异时才分开计数。
- Keep both READMEs semantically aligned. / 保持中英文 README 的语义一致。
- Exclude game-playing agents, NPC AI, and gameplay benchmarks unless they directly evaluate generated games or content. / 排除玩游戏的智能体、NPC AI 和游玩 benchmark，除非它们直接用于评测生成的游戏或内容。
- When a work mixes generation and gameplay, state what is scored: the generated artifact may qualify, while policy return, win rate, or agent task success does not. / 当工作同时包含生成与游玩时，必须说明评分对象：生成工件可以收录，策略回报、胜率或智能体任务成功率本身不构成收录理由。
