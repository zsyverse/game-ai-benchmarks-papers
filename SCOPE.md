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

## Excluded / 不收录

| Excluded topic | Reason |
| --- | --- |
| Game-playing agents, policies, or gameplay benchmarks / 游戏智能体、策略与游玩 benchmark | The output is an action policy or score, not a generated game. / 输出是动作策略或游戏得分，而不是新游戏。 |
| DQN, AlphaGo, AlphaZero, MuZero, Voyager, SIMA, BALROG, MineDojo-agent evaluations, and similar work | These systems primarily learn to play, plan, or act in an existing environment. / 核心任务是在已有环境中游玩、规划或行动。 |
| NPC AI, player modeling, matchmaking, cheat detection, or game analytics | They operate on an existing game without generating the game itself. / 它们处理已有游戏，但不生成游戏本身。 |
| Standalone image, texture, 3D-asset, music, dialogue, or story generation | The field is too broad; include it only when the work integrates the component into a playable-game generation pipeline. / 范围过宽；只有直接集成到可玩游戏生成流程时才收录。 |
| General-purpose world models for driving or robotics | Included only when the work explicitly targets games or playable virtual worlds. / 只有明确面向游戏或可玩虚拟世界时才收录。 |
| Pure game testing or bug finding | Included only when it is an evaluator or stage of a game-generation benchmark. / 只有作为游戏生成 benchmark 的评分器或流程阶段时才收录。 |

## Borderline rule / 边界规则

If the main research question is “How well can an agent play this game?”, exclude it. If it is “Can a system create a new playable game, rule set, level, or interactive world?”, include it.

如果论文的核心问题是“智能体能把这个游戏玩得多好”，则排除；如果核心问题是“系统能否创造新的可玩游戏、规则集、关卡或交互世界”，则收录。
