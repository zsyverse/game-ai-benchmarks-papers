# Scope / 收录范围

This repository indexes **papers about generating games**, not papers about playing them.

本仓库只索引**生成游戏的论文**，不收录以玩游戏为核心的论文。

## The two allowed roles / 仅允许两种角色

| Role | Required evidence | 必要条件 |
| --- | --- | --- |
| Generation method / 生成方法 | The paper's central contribution directly generates an eligible output and evaluates that generator. | 论文核心贡献直接生成合格产物，并对该生成器进行评测。 |
| Generation benchmark / 生成 Benchmark | The paper formally defines an eligible generation task, evaluation protocol, and empirical generator comparison. | 论文正式定义合格的生成任务、评测协议，并实证比较生成器。 |

A dataset, corpus, metric, verifier, competition platform, or tool does not qualify by itself. It qualifies only when the paper itself satisfies one of the two roles above.

数据集、语料库、指标、验证器、竞赛平台或工具本身不足以获得收录资格；只有论文本身满足上述两种角色之一时才收录。

## Eligible generated outputs / 合格生成产物

| Output | Definition | 定义 |
| --- | --- | --- |
| Complete game | A runnable game containing gameplay, rules, code, and the required project structure. | 包含玩法、规则、代码及必要工程结构的可运行游戏。 |
| Game code or project | Executable code and scenes assembled into a runnable game/project, or a self-contained executable mechanic. Ordinary patches to an existing repository do not qualify. | 装配成可运行游戏/工程的可执行代码与场景，或可独立执行的游戏机制；对既有仓库做普通补丁不符合条件。 |
| Rules or mechanics | An executable game description, program, rule set, or mechanic that changes gameplay. | 能改变玩法的可执行游戏描述、程序、规则集或机制。 |
| Playable content | A playable level, map, dungeon, puzzle, quest, task, track, or rhythm chart. | 可玩的关卡、地图、地牢、谜题、任务、赛道或节奏谱面。 |
| Interactive game world | A generated game world whose observations, geometry, or state change step by step with player input. | 其画面、几何或状态随玩家输入逐步变化的生成式游戏世界。 |

## Excluded / 不收录

| Excluded work | Reason |
| --- | --- |
| Game-playing agents, NPC/player policies, and gameplay benchmarks / 游玩智能体、NPC/玩家策略和 gameplay benchmark | The evaluated product is a policy, score, return, or task success rather than a generated game artifact. / 被评测对象是策略、得分、回报或任务成功率，而不是生成的游戏工件。 |
| Dataset/corpus-only papers / 纯数据集或语料库论文 | Data without a formal generation task and evaluator is not a generation benchmark. / 没有正式生成任务与 evaluator 的数据不构成生成 benchmark。 |
| Surveys, taxonomies, position papers, and research agendas / 综述、分类、立场论文和研究议程 | They organize or discuss the field but do not propose a generator or generation benchmark. / 它们梳理或讨论领域，但不提出生成器或生成 benchmark。 |
| General infrastructure, runtimes, and framework-only proposals / 通用基础设施、运行时与纯框架设想 | Supporting or describing a possible generator is not the same as demonstrating one. / 支撑或描述可能的生成器，不等于实际提出并验证生成方法。 |
| Coding-agent benchmarks on existing game repositories / 既有游戏仓库上的 coding-agent benchmark | Implementing scoped feature patches is software-engineering evaluation, not a benchmark for generating a game. / 实现局部功能补丁属于软件工程评测，不是游戏生成 benchmark。 |
| Metric-only or evaluator-only studies / 纯指标或纯 evaluator 研究 | Measuring outputs without defining a formal benchmark or generation method is outside scope. / 只测量产物、但不定义正式 benchmark 或生成方法，超出范围。 |
| Standalone repair, QA, bug finding, balancing, or parameter tuning / 独立修复、QA、查错、平衡或调参 | Modifying an existing artifact is insufficient unless it is an internal stage of a substantive generation method. / 只修改既有工件不足以收录；除非它是实质生成方法的内部环节。 |
| Authoring UI without substantive automatic generation / 没有实质自动生成的创作界面 | Manual editing assistance alone is not a generation method. / 仅辅助人工编辑不构成生成方法。 |
| Isolated assets, reskins, or narrative structures / 孤立资产、换皮或叙事结构 | Images, textures, 3D props, music, dialogue, stories, narrative JSON, cards, or settlements qualify only when integrated by the paper into an eligible playable output. / 图像、纹理、3D 物件、音乐、对话、故事、叙事 JSON、卡牌或聚落，只有由论文方法集成进合格可玩产物时才收录。 |
| Non-playable scenes or zero-player simulations / 不可玩场景或零玩家模拟 | A generated environment is not a generated game unless the paper makes it directly playable or interactive. / 生成环境只有被论文方法直接做成可玩或可交互产物时，才属于游戏生成。 |
| Prompted video without stepwise player control / 无逐步玩家控制的提示词视频 | A game-looking clip is not an interactive generated game world. / 看起来像游戏的片段不等于可交互生成式游戏世界。 |
| Planning- or policy-centered world models / 以规划或策略为核心的 world model | Excluded when the main result is action selection, NPC behavior, or policy learning. / 主要结果是动作选择、NPC 行为或策略学习时排除。 |

## Decision tests / 判定测试

- Judge the paper by its **central research contribution**, not by a demo, dataset name, or incidental use in a game pipeline.
- Playtesting, search, RL, solvers, and self-play are allowed only when they generate or evaluate the generated artifact itself.
- A mixed paper qualifies as a benchmark only when it formally defines and empirically evaluates an eligible generation track.
- When the evidence is ambiguous, exclude the paper until a primary source demonstrates that it passes the rule.

- 按论文的**核心研究贡献**判定，不能只依据 demo、数据集名称或在游戏流水线中的附带用途。
- 试玩、搜索、RL、求解器和自博弈只有在直接生成或评测生成工件时才允许。
- 混合主题论文只有在正式定义并实证评测合格生成赛道时，才可作为 benchmark 收录。
- 证据不明确时先排除，直到一手来源证明其符合规则。

## Canonical-record rule / Canonical 记录规则

The same paper may appear in only one public category. Preprints, published versions, renamed releases, and benchmark/method names from the same paper are merged into one canonical record. A genuinely distinct follow-up paper remains separate.

同一论文只能出现在一个公开分类中。预印本、正式发表版、更名发布，以及同一论文中的 benchmark/方法名称应合并成一条 canonical 记录；实质不同的后续论文仍单独收录。
