# Scope / 收录范围

This repository is about **AI that generates games**, not AI that plays them.

本仓库只关注 **生成游戏的 AI**，不收录以“玩游戏”为目标的 AI。

## Included / 收录

| Scope | English definition | 中文定义 |
| --- | --- | --- |
| End-to-end game generation | Generate a runnable or playable game from text, examples, references, or high-level specifications. | 从文本、示例、参考或高层需求生成可运行、可玩的游戏。 |
| Game code and project generation | Create or edit source code, scenes, engine projects, rules, or runtime behavior to implement a game. | 生成或修改源码、场景、引擎工程、规则与运行时行为，从而实现游戏。 |
| Automated game design | Generate complete games, rulesets, mechanics, balance, or interacting systems. | 自动生成完整游戏、规则集、机制、平衡或相互作用的系统。 |
| Level and playable-content generation | Generate levels, maps, quests, dungeons, or other content that directly determines gameplay. | 生成关卡、地图、任务、地牢等直接决定玩法的内容。 |
| Interactive-world generation | Generate action-conditioned, playable visual worlds or learned game simulators. | 生成受玩家动作控制、可交互的视觉世界或学习式游戏模拟器。 |
| Evaluation resources | Benchmarks, datasets, corpora, and evaluators built specifically for the categories above. | 专门评测上述任务的 benchmark、数据集、语料库和评分器。 |
| Foundational surveys | A small set of surveys or taxonomies that directly organize automated game generation or PCG. | 少量直接梳理自动游戏生成或 PCG 的综述与分类论文。 |

## Entry roles / 条目角色

Every included record must be assigned one of these roles so that supporting resources are not mistaken for generation systems.

每条记录都必须归入以下角色之一，避免把支撑资源误认为游戏生成系统。

| Role | English rule | 中文规则 |
| --- | --- | --- |
| Core generator / 核心生成器 | The system outputs a runnable game, executable rules or mechanics, game code/project changes, playable content, or a human-controllable generated world. | 系统直接输出可运行游戏、可执行规则/机制、游戏代码/工程修改、可玩内容，或供人控制的生成式世界。 |
| Generation resource / 生成专用资源 | A benchmark, dataset, corpus, verifier, repair stage, or evaluator built specifically for one of the generation outputs above. | 专门服务于上述生成对象的 benchmark、数据集、语料库、验证器、修复环节或评分器。 |
| Boundary or framing / 边界或领域框架 | Infrastructure, a mixed framework, survey, taxonomy, or perspective that directly structures the field but is not itself a generator. It must appear in an explicitly labelled subsection and must not be described as a generation model. | 直接组织该领域的基础设施、混合框架、综述、分类或观点论文，但其本身不是生成器；必须放在明确标注的分区中，且不能描述成生成模型。 |

## Excluded / 不收录

| Excluded topic | Reason |
| --- | --- |
| Game-playing agents, policies, or gameplay benchmarks / 游戏智能体、策略与游玩 benchmark | The output is an action policy or score, not a generated game. / 输出是动作策略或游戏得分，而不是新游戏。 |
| DQN, AlphaGo, AlphaZero, MuZero, Voyager, SIMA, BALROG, MineDojo-agent evaluations, and similar work | These systems primarily learn to play, plan, or act in an existing environment. / 核心任务是在已有环境中游玩、规划或行动。 |
| NPC AI, player modeling, matchmaking, cheat detection, or game analytics | They operate on an existing game without generating the game itself. / 它们处理已有游戏，但不生成游戏本身。 |
| Standalone image, texture, 3D-asset, music, dialogue, or story generation | The field is too broad; include it only when the work integrates the component into a playable-game generation pipeline. / 范围过宽；只有直接集成到可玩游戏生成流程时才收录。 |
| General-purpose world models for driving or robotics | Included only when the work explicitly targets games or playable virtual worlds. / 只有明确面向游戏或可玩虚拟世界时才收录。 |
| Pure game testing or bug finding | Included only when it is an evaluator or stage of a game-generation benchmark. / 只有作为游戏生成 benchmark 的评分器或流程阶段时才收录。 |

## Method-versus-output tests / 方法与产物判定

- Automated play, self-play, search, solvers, or RL may be used to **evaluate or optimize generated content**. That does not make a paper game-playing research when the final research object is the generated game, rule set, level, or world.
- A predictive world model is not automatically in scope. It is included only when the evaluated product is a human-controllable generated environment; it is excluded when its principal purpose is learning a policy, planning actions, or improving return.
- Repair work is included when it transforms generated code, executable rules, or playable content inside a generation pipeline. Standalone QA that only reports bugs remains excluded.
- Quests, rhythm charts, cards, settlements, and other components qualify only when they directly determine gameplay or form a navigable/playable structure. Cosmetic assets alone do not qualify.

- 自动试玩、自博弈、搜索、求解器或 RL 可以用于**评估或优化生成内容**；只要最终研究对象仍是生成的游戏、规则、关卡或世界，就不因此变成玩游戏论文。
- 预测式世界模型不会自动获得收录资格。只有当被评测的产物是供人控制的生成环境时才收录；若主要目标是学习策略、规划动作或提高回报，则排除。
- 修复工作只有在生成流水线中实际修改生成代码、可执行规则或可玩内容时才收录；只输出 bug 报告的独立 QA 仍排除。
- 任务、节奏谱面、卡牌、聚落等组件只有在直接决定玩法或构成可导航/可玩的结构时才收录；纯装饰资产不收录。

## Borderline rule / 边界规则

If the main research question is “How well can an agent play this game?”, exclude it. If it is “Can a system create a new playable game, rule set, level, or interactive world?”, include it.

如果论文的核心问题是“智能体能把这个游戏玩得多好”，则排除；如果核心问题是“系统能否创造新的可玩游戏、规则集、关卡或交互世界”，则收录。
