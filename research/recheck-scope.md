# Generation-only scope recheck / 纯游戏生成范围复核

> Audit date / 复核日期：**2026-08-29 (Asia/Shanghai)**
> Audited source / 审查对象：[`SCOPE.md`](../SCOPE.md)、`docs/en/end-to-end.md`、`docs/en/pcg.md`、`docs/en/interactive-worlds.md` 里的全部表格行。
> This is an audit note only. It does not change the public indexes. / 本文件只记录审计结论，不修改公开索引。

**Resolution / 处理状态（2026-09-01）：** This report audits base commit `260ef1c`. The standalone bug-detection paper was removed, the seven boundary items were separated or relabelled, and later omission passes expanded the public index to 198 records. The original findings remain below as an audit trail. / 本报告审计的是基线提交 `260ef1c`；独立 bug-detection 论文已移除，7 个边界项已分区或重标，后续漏项复核将公开索引扩展为 198 条。以下保留原始发现作为审计轨迹。

## Executive finding / 核心结论

本次共审查 **82 个表格条目**（按出现次数计；跨页面重复论文仍分别计行）：

| Verdict | Count | 含义 |
| --- | ---: | --- |
| `in-scope` | 74 | 核心输出是游戏、规则/机制、关卡/可玩内容、游戏代码/工程，或专门服务于这些输出的 benchmark、数据集、评估器与基础综述。 |
| `borderline` | 7 | 与生成直接相关，但论文主体或条目粒度同时落在通用基础设施、混合玩游戏框架、纯组件、受控视频、NPC 决策或下游训练数据上。应放入明确的边界/资源分区，不能计作核心“生成完整游戏”论文。 |
| `out-of-scope` | 1 | 核心输出不属于 `SCOPE.md` 的生成类别，也不满足其中的评测例外。 |

因此有 **8 个需要编辑决策的范围问题**：7 个边界项和 1 个应移出项。没有发现以胜率、RL return 或固定游戏任务成功率为核心结果的 playing-only 论文仍混在三张主表中；唯一明确越界项是独立的游戏 bug 检测论文，而不是 game-playing 论文。

最重要的处置建议：

1. 将 *Automatic Bug Detection in LLM-Powered Text-Based Games Using LLMs* 从收录索引移出。它从玩家日志生成 bug 报告，是独立 QA 研究，并非游戏生成 benchmark 的 evaluator 或生成流程阶段。
2. 将 Ludii、GVGAI、WaveFunctionCollapse、AI Settlement Challenge、GameGen-X、WorldMind、RLHEV trajectory paper 保留在显式的 `infrastructure / mixed-framework / boundary` 区域，或在采用更严格“论文主体必须生成游戏”口径时移出核心计数。
3. GameDevBench 和 GameEngineBench 按现有 `SCOPE.md` 都可收录，因为输出是游戏工程代码修改且用运行时行为验证；但必须标成 **repository/project editing**，不能和从空目录生成完整游戏的 benchmark 混排比较。
4. GameNGen、ReactiveGWM 和 PCGRL 可以保留：GameNGen/ReactiveGWM 的产物是人类动作可控的生成式模拟世界，PCGRL 的 RL policy 本身是内容生成器；三者都不是以玩家 policy 的 return 或胜率为最终产物。

## Decision rule / 判定口径

- `in-scope`：主要研究问题是“能否生成/修改新的游戏、规则、机制、关卡、可玩内容、代码/工程或人类动作可控的游戏世界”；或者条目是专门评估上述任务的 benchmark、dataset、corpus、verifier；或者是直接组织这些方向的少量基础综述。
- `borderline`：生成只占混合系统的一部分，或产物虽有帮助但不是自身可玩的内容；保留时必须用小节和说明防止读者把它当成端到端生成论文。
- `out-of-scope`：主要产物是玩家 policy、胜率、return、任务成功率、NPC AI、独立 bug 报告或与可玩游戏流程无关的资产；其中纯测试/bug finding 只有在它是游戏生成 benchmark 的 evaluator 或生成流水线阶段时才例外。
- 自动 play、自博弈、solver、GUI agent 或 RL 只是方法时不自动越界；最终研究对象和主要评价量才决定范围。

## 1. `docs/en/end-to-end.md` — 29 rows

| Row | Verdict | 依据 | 建议位置 |
| --- | --- | --- | --- |
| 1. [V-GameGym](https://arxiv.org/abs/2509.20136) | `in-scope` | 从自然语言需求生成可运行 Pygame 工程；评分对象是生成代码、截图和运行视频。 | `Benchmarks → from-scratch game generation`。 |
| 2. [GameDevBench](https://arxiv.org/abs/2602.11103) | `in-scope` | 产物是 Godot 游戏工程中的 gameplay、UI、图形和动画修改，主指标是确定性运行时测试，不是 agent 的游玩得分。符合 `game code and project generation` 中的 “create or edit”。 | `Benchmarks → existing-project/repository editing`；与 from-scratch benchmark 分开。 |
| 3. [GameCraft-Bench](https://arxiv.org/abs/2606.17861) | `in-scope` | 从 brief 生成完整 Godot 游戏和可回放输入轨迹；轨迹用于验证生成物。 | `Benchmarks → from-scratch game generation`。 |
| 4. [GameEngineBench](https://arxiv.org/abs/2607.03525) | `in-scope` | 输出是在真实 UE5 游戏仓库中的 C++ 实现，覆盖 gameplay、网络、动画、UI、持久化和渲染，并由引擎行为测试验收；没有 player-policy/return 目标。它比“生成新游戏”更偏工程实现，但仍落入现有 SCOPE 的游戏代码/工程编辑。 | `Benchmarks → game-engine/repository editing`；不要纳入 prompt-to-complete-game 排名。 |
| 5. [GameXpert-Bench](https://arxiv.org/abs/2608.21833) | `in-scope` | GameGen 直接生成游戏，GameFix/GameOpt 修改生成或既有游戏；评价对象始终是游戏工件的完整性、缺陷和体验。 | `Benchmarks → game-development lifecycle`。 |
| 6. [JamBench / JamSet](https://arxiv.org/abs/2606.19830) | `in-scope` | 以 Godot game-jam 工程构建主题生成和函数/脚本/完整脚本补全任务，输出是游戏工程。 | `Benchmarks → project generation/completion datasets`。 |
| 7. [VeriGame / GameGen-Verifier](https://arxiv.org/abs/2605.07442) | `in-scope` | 本身不生成游戏，但明确验证 LLM 生成游戏对 specification 的符合度；状态注入和短交互是生成 benchmark 的 evaluator，满足 SCOPE 的验证例外。 | `Evaluation resources → generated-game verification`，不要列作生成模型。 |
| 8. [OpenGame-Bench](https://arxiv.org/abs/2604.18394) | `in-scope` | 从空 workspace 生成完整浏览器游戏，评价 build、视觉可用性和需求对齐。 | `Benchmarks → from-scratch browser games`。 |
| 9. [PlaytestArena](https://arxiv.org/abs/2605.28258) | `in-scope` | GUI agent 的游玩只用于评测和修复新生成游戏；没有比较其胜率或固定游戏任务能力。满足生成 evaluator 例外。 | `Evaluation resources → GUI playtesting of generated games`。 |
| 10. [PlayGen-20](https://arxiv.org/abs/2603.07106) | `in-scope` | 从自然语言生成 UE5 场景、PCG graph、C++ 玩法/交互模块和可运行游戏。 | `Benchmarks → from-scratch 3D/engine games`。 |
| 11. [Game Generation via Large Language Models](https://arxiv.org/abs/2404.08706) | `in-scope` | 联合生成 VGDL 规则和关卡，产物是可执行游戏描述。 | `Core papers → full rules + levels`。 |
| 12. [Grammar-Based Game Description Generation](https://arxiv.org/abs/2407.17404) | `in-scope` | 将自然语言意图转换为语法有效、可执行的 Ludii 游戏程序。 | `Core papers → rule/program generation`。 |
| 13. [GAVEL](https://arxiv.org/abs/2407.09388) | `in-scope` | 生成新颖、可执行的 Ludii 棋类规则程序；self-play 是设计评价器，不是最终玩家 agent。 | `Core papers → automated rule/full-game design`。 |
| 14. [GameGPT](https://arxiv.org/abs/2310.08067) | `in-scope` | 研究目标是自动化游戏开发，输出规划、任务和实现代码；虽缺少标准化生成质量评测，但不是范围越界。 | `Core papers → agentic game development systems`；注明证据偏 case study。 |
| 17. [ScriptDoctor](https://arxiv.org/abs/2506.06524) | `in-scope` | 生成并迭代修复完整 PuzzleScript 规则和关卡；solver 只验证可解性。 | `Core papers → full game/rule generation`。 |
| 18. [Cardiverse](https://aclanthology.org/2025.emnlp-main.1511/) | `in-scope` | 核心输出是新卡牌机制、可执行代码和原型；锦标赛只辅助验证设计。 | `Core papers → mechanics + executable prototypes`。 |
| 19. [Zagii text-to-game engine](https://arxiv.org/abs/2407.08195) | `in-scope` | 端到端生成 RPG 叙事、角色、环境、视听资产和玩法机制，资产不是孤立产物。 | `Core papers → runtime text-to-game`。 |
| 20. [OpenGame](https://arxiv.org/abs/2604.18394) | `in-scope` | 从 brief 和空 workspace 生成完整多文件 Phaser/TypeScript 游戏。 | `Core papers → agentic game coding`。 |
| 21. [CreativeGame](https://arxiv.org/abs/2604.19926) | `in-scope` | 生成 HTML5 游戏、明确的 mechanic delta 和版本谱系，评测机制实现与运行稳健性。 | `Core papers → mechanic-aware game evolution`。 |
| 22. [UniGen](https://arxiv.org/abs/2509.26161) | `in-scope` | 输出 Unity blueprint、C#、组件绑定、场景和可运行 3D prototype。 | `Core papers → engine project generation`。 |
| 23. [Play2Code](https://arxiv.org/abs/2605.28258) | `in-scope` | 最终产物是连续修复后的浏览器游戏；GUI play 是生成—试玩—修复闭环中的 tester。 | `Core papers → generation with automated playtesting`。 |
| 24. [Boardwalk](https://arxiv.org/abs/2508.16447) | `in-scope` | 将自然语言桌游规则实现为可玩的 Python 游戏；不是让 LLM 玩桌游。 | `Core papers → rules-to-code`。 |
| 26. [AutoUE](https://arxiv.org/abs/2603.07106) | `in-scope` | 从 brief 生成 UE5 场景、PCG、C++ 玩法逻辑和运行游戏。 | `Core papers → end-to-end 3D engine generation`。 |
| 15. [DreamGarden](https://arxiv.org/abs/2410.01791) | `in-scope` | 单提示被分解并实现为 Unreal 游戏环境模块；主要问题是人机共创工作流，不是玩游戏。场景/工程生成符合 SCOPE，但不等于自主完整游戏。 | `Adjacent generation → human-in-the-loop co-creation`。 |
| 16. [ChatGE](https://aclanthology.org/2025.acl-long.218/) | `in-scope` | 每轮生成 game-script segment 和对应代码片段以开发 custom poker game；代码正确性而非扑克胜率是评价对象。输出粒度较局部。 | `Adjacent generation → conversational co-development`；不要列作端到端完整游戏基准。 |
| 25. [Automatic Bug Detection in LLM-Powered Text-Based Games](https://aclanthology.org/2024.findings-acl.907/) | `out-of-scope` | 论文从现有 DejaBoom! 的玩家日志识别逻辑/设计 bug，核心输出是 bug 报告。它既不是游戏生成 benchmark 的 evaluator，也不是生成 pipeline 的一个实证阶段；正中 SCOPE 的 “pure game testing or bug finding” 排除条款。 | 从索引移除；若要保留背景，只放 `research/` 的 `Excluded / related QA` 说明。 |
| 27. [Agentic Game Development as a Verifiable Trajectory Data Engine](https://arxiv.org/abs/2608.25518) | `borderline` | 会产生 engine edits 和 executable artifacts，但主论点是用游戏开发轨迹和 engine reward 扩展 world models/RLHEV；主要研究产物不是一组新游戏。 | `Boundary resources → game-development trajectory/data engines`；不计入核心生成论文数。严格口径可移出。 |
| 28. [Lottery and Sprint Arcade](https://arxiv.org/abs/2607.10711) | `in-scope` | 用语音修改固定游戏约 100 个 mechanics、visuals、interaction、audio 配置字段；SCOPE 明确允许编辑规则和运行时行为。 | `Adjacent generation → constrained co-editing`；注明不是 from-scratch generation。 |
| 29. [Playable Game Generation](https://arxiv.org/abs/2412.00887) | `in-scope` | 输出人类动作条件的实时可玩视频/latent dynamics engine，而非 policy；符合 `interactive-world generation`。 | 仅放 `interactive worlds → learned existing-game simulators`；当前 end-to-end 页的 learned-engine boundary 可作为指针，不参与代码生成排名。 |

### End-to-end subtotal

- `in-scope`: **27**
- `borderline`: **1**
- `out-of-scope`: **1**

## 2. `docs/en/pcg.md` — 35 rows

| Row | Verdict | 依据 | 建议位置 |
| --- | --- | --- | --- |
| 1. [An Experiment in Automatic Game Design](https://doi.org/10.1109/CIG.2008.5035629) | `in-scope` | 进化完整双人游戏规则和棋盘配置；learning agents 只给生成设计打分。 | `Complete games / automated design`。 |
| 2. [Automatic Generation and Evaluation of Recombination Games](https://eprints.qut.edu.au/17025/) | `in-scope` | Ludi 组合并进化棋类规则；self-play 只过滤候选规则。 | `Rules / automated design`。 |
| 3. [Multi-faceted Evolution of Simple Arcade Games](https://doi.org/10.1109/CIG.2011.6032019) | `in-scope` | 联合生成街机游戏 mechanics、rules 和 level layouts。 | `Complete games / automated design`。 |
| 4. [The Micro-Rhetorics of Game-o-Matic](https://doi.org/10.1145/2282338.2282347) | `in-scope` | 将概念关系图映射成 entities、rules、mechanic patterns 和可玩小游戏。 | `Complete games / automated design`。 |
| 5. [Mechanic Miner](https://doi.org/10.1007/978-3-642-37192-9_29) | `in-scope` | 发现规则变化并生成展示该机制的关卡；模拟 play 用于区分新机制。 | `Rules + supporting levels`。 |
| 6. [Automatic Game Design via Mechanic Generation](https://doi.org/10.1609/aaai.v28i1.8788) | `in-scope` | 搜索并合成满足设计约束的可执行 mechanics/rules。 | `Rules / mechanics`。 |
| 7. [A Rogue Dream](https://doi.org/10.1609/aiide.v10i3.12745) | `in-scope` | 根据主题选择内容、搜索机制并装配完整小型游戏。 | `Complete games / automated design`。 |
| 8. [Automated Game Design via Conceptual Expansion](https://arxiv.org/abs/1809.02232) | `in-scope` | 学习并重组既有游戏结构以创造新游戏；复原旧游戏只是方法验证。 | `Complete games / automated design`。 |
| 10. [Puck](https://doi.org/10.1609/aiide.v18i1.21968) | `in-scope` | 长期生成并积累个性化的完整可玩设计。 | `Complete games / mixed-initiative design`。 |
| 11. [Ludii](https://arxiv.org/abs/1905.05013) | `borderline` | Ludii 本身是 game-description language、runtime 和传统游戏 corpus，不是生成器；论文还服务 General Game Playing。它对 GAVEL/GGDG 等规则生成非常重要，但不应计作一篇生成算法论文。 | `Infrastructure / executable rule languages`，作为上下文资源；不计入 generator paper 数。 |
| 12. [GAVEL](https://arxiv.org/abs/2407.09388) | `in-scope` | 生成可执行的全新 Ludii board-game programs；play simulation 是 fitness。 | `Complete games / rule generation`。 |
| 13. [Grammar-Based Game Description Generation](https://arxiv.org/abs/2407.17404) | `in-scope` | 生成语法合法、可执行的完整游戏描述。 | `Rules / program generation`。 |
| 14. [Game Generation via Large Language Models](https://arxiv.org/abs/2404.08706) | `in-scope` | 联合生成 VGDL 规则和关卡。 | `Complete games / rules + levels`。 |
| 15. [ScriptDoctor](https://arxiv.org/abs/2506.06524) | `in-scope` | 生成并修复完整 PuzzleScript 规则和关卡；BFS 是生成 verifier。 | `Complete games / rules + levels`。 |
| 16. [Cardiverse](https://aclanthology.org/2025.emnlp-main.1511/) | `in-scope` | 生成新机制、可执行 card-game code 和 prototypes。 | `Complete games / mechanics + code`。 |
| 17. [The Procedural Content Generation Benchmark](https://arxiv.org/abs/2503.21474) | `in-scope` | 专门评测 level、dungeon、puzzle、bullet-hell 和简单规则等内容生成器。 | `Level/content generation benchmarks`。 |
| 18. [VGLC](https://arxiv.org/abs/1606.07487) | `in-scope` | 不生成关卡，但官方摘要明确把人类关卡 corpus 建成面向 ML level generation 的训练资源；满足 generation-specific corpus 条款。 | `Datasets for level generation`，不要标为生成模型或统一 benchmark。 |
| 19. [Mario AI Championship — Level Generation Track](https://doi.org/10.1109/TCIAIG.2011.2166267) | `in-scope` | 收录对象明确限定为生成 Mario-style levels 的 competition track；player traces/偏好用于条件和评价。 | `Level-generation competitions`；标题始终带 `Level Generation Track`。 |
| 20. [General Video Game AI multitrack framework](https://doi.org/10.1109/TG.2019.2901021) | `borderline` | 论文/框架同时包含 game-playing agents、games 和 content-generation algorithms；只有 level/rule-generation tracks 与本仓库相符。当前行已排除 playing tracks，但引用整个 multitrack resource 容易被理解为收录 GVGAI agent benchmark。 | `Mixed framework → GVGAI generation tracks only`；链接到具体生成接口/track，并明确不统计整个 GVGAI 为生成 paper。 |
| 21. [Evolving Mario Levels in a DCGAN Latent Space](https://doi.org/10.1145/3205455.3205517) | `in-scope` | 优化 latent vectors 以生成新的 Mario levels；playability 是内容质量指标。 | `Level generation papers`。 |
| 22. [TOAD-GAN](https://arxiv.org/abs/2008.01531) | `in-scope` | 从单个示例生成新的 tile levels；风格、diversity、playability 评价生成物。 | `Level generation papers`。 |
| 23. [PCGRL](https://doi.org/10.1609/aiide.v16i1.7416) | `in-scope` | RL policy 的动作是编辑 tiles，最终产物是新关卡；论文比较 validity、quality 和 diversity，而不是玩家 return。RL 是生成算法，不是 playing agent。 | `Level generation methods → RL content generators`。 |
| 24. [Learning Controllable Content Generators](https://arxiv.org/abs/2105.02993) | `in-scope` | 在 PCGRL 上按设计属性目标生成可控关卡。 | `Level generation methods → controllable RL generators`。 |
| 25. [Talakat](https://arxiv.org/abs/1806.04718) | `in-scope` | 生成可执行且行为多样的 bullet-hell attack patterns，直接决定玩法。 | `Playable-content generation`。 |
| 26. [Generating Levels That Teach Mechanics](https://arxiv.org/abs/1807.06734) | `in-scope` | 输出 Mario tutorial levels；受限 A* players 只是差分可解性 evaluator。 | `Level generation papers`。 |
| 27. [Level Generation Through Large Language Models](https://arxiv.org/abs/2302.05817) | `in-scope` | 采样新的 Sokoban grid levels，并评估可解性和控制性。 | `Level generation papers`。 |
| 28. [MarioGPT](https://arxiv.org/abs/2302.05981) | `in-scope` | 从文字属性提示生成 Mario tile layouts；输出是关卡。 | `Text-to-level generation`。 |
| 29. [Super Mario as a String](https://arxiv.org/abs/1603.00930) | `in-scope` | 用 LSTM 采样新的 Mario level sequences。 | `Level generation papers`。 |
| 30. [DOOM Level Generation Using GANs](https://arxiv.org/abs/1804.09154) | `in-scope` | 生成带空间、墙、高度和物件的 DOOM layouts。 | `Level generation papers`。 |
| 31. [WaveFunctionCollapse Is Constraint Solving in the Wild](https://doi.org/10.1145/3102071.3110566) | `borderline` | WFC 是通用 tile/image constraint generator；可生成地图，但论文自身不专门提出游戏关卡任务，也不保证 gameplay/solvability。它是 PCG 常用技术，而非纯游戏生成 paper。 | `Adjacent techniques / constraint-based map generation`；核心论文计数中移除或单独标边界。 |
| 32. [World-GAN](https://doi.org/10.1109/COG52621.2021.9619133) | `in-scope` | 生成 Minecraft voxel world regions/structures；这些是可进入的游戏世界内容而非孤立 3D asset，但不生成规则。 | `Component-only → playable world/map content`。 |
| 33. [AI Settlement Generation Challenge](https://doi.org/10.1007/s13218-020-00635-0) | `borderline` | 生成 Minecraft 道路、建筑和 settlements，且有 functionality 评价；但主要产物也可被视为建筑/审美组件，不生成规则或完整关卡目标，位于“可玩世界内容”和“独立 3D asset”边界。 | `Component-only / peripheral PCG challenge`；不计入完整游戏或规则论文。 |
| 9. [Orchestrating Game Generation](https://doi.org/10.1109/TG.2018.2870876) | `in-scope` | 直接组织规则、关卡、视觉、音频等生成器如何协同；属于 SCOPE 允许的 foundational architecture/survey。 | `Surveys / architectures`。 |
| 34. [Search-Based PCG survey](https://doi.org/10.1109/TCIAIG.2011.2148116) | `in-scope` | 直接梳理关卡、规则、地图、谜题等 game-content generation。 | `Foundational surveys`。 |
| 35. [PCG via Machine Learning survey](https://arxiv.org/abs/1702.00539) | `in-scope` | 明确定义并梳理用 ML 生成 functional game content，区分 cosmetic assets。 | `Foundational surveys`。 |

### PCG subtotal

- `in-scope`: **31**
- `borderline`: **4**
- `out-of-scope`: **0**

## 3. `docs/en/interactive-worlds.md` — 18 rows

| Row | Verdict | 依据 | 建议位置 |
| --- | --- | --- | --- |
| [Genie](https://proceedings.mlr.press/v235/bruce24a.html) | `in-scope` | 从图像/草图和用户 latent action 生成可操作的 2D world rollout；输出是 action-conditioned world，而非 policy。 | `Interactive worlds → prompt-to-playable worlds`。 |
| [GameNGen](https://arxiv.org/abs/2408.14837) | `in-scope` | 论文明确以神经模型替代 DOOM renderer/transition loop，并以用户动作实时生成新轨迹。前置 RL agent 只收集训练数据；核心评价是视觉、动力学、速度和人类辨别，不是 RL return。符合 SCOPE 明示的 “learned game simulators”。 | `Interactive worlds → existing-game neural simulators`；醒目标注 “simulates, does not author new rules”。 |
| [Oasis](https://oasis-model.github.io/) | `in-scope` | 根据初始帧和键盘动作自回归生成 Minecraft-like 可交互世界。 | `Interactive worlds → action-controlled worlds`。 |
| [GameGen-X](https://openreview.net/forum?id=8VG8tpPZhe) | `borderline` | 主要能力包含 text-to-game-video 和按结构化 instruction/event 的 continuation；官方摘要称可交互控制和 gameplay simulation，但它没有通用低层玩家动作 schema，也未证明传统意义的实时可玩游戏循环。它比纯视频更强、比 learned game engine 更弱。 | `Boundary → instruction-controlled game video`；不要与 GameNGen/键鼠实时 world model 共用 “playable engine” 标签。 |
| [GameFactory](https://arxiv.org/abs/2501.08325) | `in-scope` | 通过 W/S/A/D、跳跃、鼠标等动作控制新场景中的自回归无限视频，研究问题就是创建新的 action-controllable game videos。 | `Interactive worlds → prompt-to-new action-controlled worlds`。 |
| [MineWorld](https://arxiv.org/abs/2504.08388) | `in-scope` | 同时建模视觉 token 和移动/相机控制，实时生成 Minecraft observations；无玩家 policy 评价。 | `Interactive worlds → existing-game neural simulators`。 |
| [Matrix-Game 1.0–3.0](https://arxiv.org/abs/2604.08995) | `in-scope` | 根据键盘、鼠标和相机输入实时生成多游戏长时 rollout；评价生成质量、控制和记忆。 | `Interactive worlds → action-controlled world models`。 |
| [Hunyuan-GameCraft 1.0/2.0](https://arxiv.org/abs/2506.17201) | `in-scope` | 参考图/文本加键鼠相机条件生成游戏视频，2.0 还支持多轮世界交互指令；输出是受控世界生成。 | `Interactive worlds → action/instruction-controlled worlds`。 |
| [Solaris](https://arxiv.org/abs/2602.22208) | `in-scope` | 按两名玩家各自动作生成同步 Minecraft 视角，评价共享世界的一致性、建造和记忆。 | `Interactive worlds → multiplayer simulators`。 |
| [WorldCam](https://arxiv.org/abs/2603.16871) | `in-scope` | 用键鼠和 6-DoF pose 驱动 autoregressive gaming world，并评价长时重访。 | `Interactive worlds → long-horizon simulators`。 |
| [ReactiveGWM](https://arxiv.org/abs/2605.15256) | `in-scope` | 产物是同时受玩家低层动作和 NPC 策略提示控制的 Street Fighter 生成式 rollout；NPC strategy 是 world-generation condition，没有输出 player policy，也不以胜率/return 评价。它不是 SCOPE 所排除的“只在既有引擎运行的 NPC AI”。 | `Interactive worlds → existing-game, NPC-conditioned simulators`；保留边界说明，勿放 game-agent 列表。 |
| [SCOPE](https://arxiv.org/abs/2605.23345) | `in-scope` | 根据图像、prompt 和逐帧 gamepad telemetry 生成多游戏 FPS clips；核心量是动作响应和生成质量。 | `Interactive worlds → action-conditioned simulators`。 |
| [StatePlay](https://arxiv.org/abs/2607.26754) | `in-scope` | 联合生成 Street Fighter 视频与 health/timer/meter state，玩家动作是条件，不是要学习的 policy。 | `Interactive worlds → state-aware simulators`。 |
| [ForgeWM](https://arxiv.org/abs/2608.14022) | `in-scope` | 生成键鼠动作条件的实时 Minecraft/FPS 视频世界；指标是控制准确、视频质量、速度和 replay fidelity。 | `Interactive worlds → real-time simulators`。 |
| [WorldMind](https://arxiv.org/abs/2608.21439) | `borderline` | 框架既重建/生成视频世界，也显式规划 NPC 下一动作；论文的核心卖点和多项指标是 state-aware NPC behavior。它不以 player win/return 为目标，因此不是 playing-agent paper，但与 SCOPE 的 NPC AI 排除项重叠。生成层使它不宜直接判为范围外。 | `Boundary → generated worlds with embedded NPC planning`；不计作纯 world generator，说明保留原因。严格排除 NPC-AI 口径可移出。 |
| [Marionette](https://arxiv.org/abs/2608.14530) | `in-scope` | 从 action IDs 生成显式多角色状态、几何和 RGB 长时 rollout；主要产物是可控 world simulation。 | `Interactive worlds → state/geometry-aware simulators`。 |
| [PhysEditWorld](https://arxiv.org/abs/2606.26694) | `in-scope` | 数据集本身不生成游戏，但专门提供重力和动作条件 world generation 的 paired engine supervision，满足 generation-enabling dataset 条款。 | `Datasets for interactive-world generation`；注明并非模型。 |
| [From Pixels to States](https://arxiv.org/abs/2607.14076) | `in-scope` | 是 perspective/data-engine paper，不是 generator；但它直接用 action–state–observation loop 梳理 interactive game world generation，符合 foundational survey/framing 例外。 | `Field framing / foundational perspectives`；不计入生成模型排行榜。 |

### Interactive-world subtotal

- `in-scope`: **16**
- `borderline`: **2**
- `out-of-scope`: **0**

## Focused boundary answers / 指定重点项结论

| Item | Final verdict | 一句话理由 |
| --- | --- | --- |
| GameDevBench | `in-scope` | 生成/修改 Godot 游戏工程代码；不是玩游戏，但应归入 repo editing。 |
| GameEngineBench | `in-scope` | 生成 UE5 C++ 工程修改并由行为测试验收；不是 from-scratch game generation。 |
| VeriGame / PlaytestArena / Play2Code | `in-scope` | “玩”是生成游戏的 verifier/repair signal，满足 SCOPE 的 evaluator 例外。 |
| DreamGarden / ChatGE / Lottery and Sprint Arcade | `in-scope` | 输出场景、游戏代码或规则/运行时修改；应明确标成 co-creation，不声称全自动端到端。 |
| Standalone LLM game bug detection | `out-of-scope` | 纯 bug finding，且不是生成 benchmark/pipeline 的 evaluator。 |
| GameNGen | `in-scope` | 学习式、人类动作可控的现有游戏模拟器；RL agent 只采集数据。 |
| ReactiveGWM | `in-scope` | 核心输出仍是动作/NPC 条件生成世界，不输出玩家 policy。 |
| WorldMind | `borderline` | 世界生成和 NPC planning 同为核心，碰到 NPC AI 排除边界。 |
| Ludii | `borderline` | 是规则语言/runtime/corpus，不是生成器。 |
| VGLC | `in-scope` | 是专门为 level generation 提供的 corpus，满足资源例外。 |
| GVGAI | `borderline` | 只有 generation tracks 可收；完整 multitrack framework 包含大量 playing-agent 任务。 |
| PCGRL | `in-scope` | RL policy 直接编辑并生成内容；return 不是玩家游戏成绩。 |

## Recommended editorial action / 建议编辑动作

本审计不改索引；后续若执行修订，建议按优先级处理：

1. **Remove:** end-to-end #25 standalone bug detection。
2. **Relabel or move to boundary/resource sections:** end-to-end #27；PCG #11、#20、#31、#33；interactive worlds GameGen-X、WorldMind。
3. **Keep but preserve subtype labels:** GameDevBench/GameEngineBench = project editing；VeriGame/PlaytestArena = verification；DreamGarden/ChatGE/Lottery and Sprint Arcade = co-creation；GameNGen/MineWorld/ReactiveGWM = simulation of existing games rather than new rule authoring。
4. **Do not compare across output types:** from-scratch code/project generation、repository editing、rule/level PCG 和 pixel world simulation 应继续保持分区，不能用同一 “best game generator” 排名。

## Primary-source basis / 一手来源依据

判定基于每行链接的作者论文、官方 proceedings/project/repository，以及仓库现有三份逐项一手来源底稿：

- [End-to-end game and game-code generation sources](end-to-end-generation-sources.md)
- [Automated game design and PCG sources](pcg-automated-design-sources.md)
- [Interactive game-world generation sources](interactive-world-generation-sources.md)

特别核对了几条容易因方法名误判的规则：GameNGen 论文将 RL agent 用作训练数据采集而非最终产品；PCGRL 的 policy 是 tile editor/content generator；GAVEL、Ludi、教程关卡生成中的 self-play/solver 是设计评价器；PlaytestArena/Play2Code 的 GUI play 是生成游戏的验证和修复阶段。相反，独立 bug detection 的最终产物就是 QA 报告，因此不因对象是 “LLM-powered game” 自动获得收录资格。
