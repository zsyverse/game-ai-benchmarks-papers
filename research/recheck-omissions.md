# Generation-only omission audit / 纯游戏生成漏项复核

> Audit date / 复核日期：**2026-08-29 (Asia/Shanghai)**
> Audited source / 审查对象：`docs/en/*.md`、对应中文页面及三份现有 research source notes。
> This is an audit note only. It does not modify the public index. / 本文件只记录审计结果，不修改公开索引。

**Resolution / 处理状态（2026-09-01）：** All 50 direct-scope (`P0`) and 12 adjacent (`P1`) version families identified below were independently rechecked and integrated into explicit core/resource/boundary sections. Together with removal of one out-of-scope QA paper, that pass produced 143 category records. Three historical passes recovered 26 more families, two targeted primary-source passes recovered another 27, and the final independent audit recovered two more, bringing the current public index to 198 records. / 下列 50 个直接范围（`P0`）与 12 个相邻（`P1`）版本族均已独立复核，并按核心生成器、生成资源或边界分区补入；同时移除 1 篇越界 QA 论文，该轮形成 143 条分类记录。随后三轮经典文献复核补入 26 个版本族，两轮定向一手来源复核再补 27 个，最终独立审计又补入 2 个，当前公开索引为 198 条。

**First historical addendum / 第一轮历史补核：** [Launchpad](https://doi.org/10.1109/TCIAIG.2010.2095855) directly generates guaranteed-playable 2-D platform levels, and [Variations Forever](https://doi.org/10.1109/ITW.2010.5593343) directly generates executable mini-game rulesets. Both were verified from publisher metadata and author manuscripts, are generation—not playing—research, and are now source records 61–62 in the PCG collection. / Launchpad 直接生成保证可玩的二维平台关卡，Variations Forever 直接生成可执行小游戏规则集；二者均已通过出版元数据与作者稿复核，属于生成而非游玩研究，现作为 PCG 来源编号 61–62 收录。

**Second historical addendum / 第二轮历史补核：** A saturation pass over 2000–2015 primary records recovered ten independent version families, now PCG sources 63–72: EGGG; the 2006 platform-level prototype; balanced board-game design; *Towards Automated Game Design*; personalized racing and Mario generation; Polymorph; Tanagra; Sentient Sketchbook; and the Markov-map series. Three generate complete games or executable rules and seven generate levels/playable content. / 对 2000–2015 年一手记录做饱和复核后，新增十个独立版本族，现为 PCG 来源 63–72：EGGG、2006 平台关原型、平衡棋类自动设计、*Towards Automated Game Design*、个性化赛车与 Mario 生成、Polymorph、Tanagra、Sentient Sketchbook，以及 Markov 地图生成系列；其中 3 个生成完整游戏或可执行规则，7 个生成关卡/可玩内容。

Version-family aliases were merged rather than double-counted: *Evolutionary Game Design* extends Ludi; *Answer Set Programming for Procedural Content Generation* extends the Variations Forever design-space method; *Generating Map Sketches for Strategy Games* belongs with Sentient Sketchbook; five early Markov papers count once; and the paired multiobjective-map, mission–space, generic-challenge, and grammatical-evolution papers each count as one lineage. *Towards Automated Game Design* (semantic assembly of J2ME micro-games) is not an alias of the separate 2008 evolutionary experiment. METAGAME/METAGAMER remains excluded because random board-game generation is only a test domain for its central general-game-playing contribution and evaluation. / 版本扩展均合并而不重复计数：*Evolutionary Game Design* 并入 Ludi；ASP for PCG 并入 Variations Forever 方法族；*Generating Map Sketches for Strategy Games* 并入 Sentient Sketchbook；五篇早期 Markov 工作合并一次；多目标地图、任务—空间、通用挑战度和语法进化的成对论文也各计一个版本族。语义装配 J2ME 微游戏的 *Towards Automated Game Design* 与 2008 年进化式实验并非同一工作。METAGAME/METAGAMER 仍排除，因为随机棋类生成只是其通用玩游戏研究的测试域。

**Third historical addendum / 第三轮历史补核：** A second saturation check of 2010–2015 playable-content work recovered 14 further version families, now PCG sources 73–86: occupancy-regulated platform generation; multiobjective RTS/StarCraft maps; coupled mission–space generation; generic challenge-constrained generation; maze and FPS evolution; grammatical-evolution and design-pattern Mario generators; vertical-slice n-grams; MCMCTS; Sampling Hyrule; evolutionary puzzle generation; NMF combination of five Mario generators; and real-time infinite cave generation. All directly generate playable levels or puzzle instances. Automated play, bots, solvers, and MCTS appear only as construction or evaluation mechanisms. / 对 2010–2015 可玩内容文献再次做饱和复核后，又补入 14 个版本族，现为 PCG 来源 73–86：占用调节平台关、多目标 RTS/StarCraft 地图、任务—空间联合生成、通用挑战度约束生成、进化式迷宫与 FPS 地图、语法进化和设计模式 Mario 关卡、纵向切片 n-gram、MCMCTS、Sampling Hyrule、进化式谜题、组合五个 Mario 生成器的 NMF 方法，以及实时无限洞穴生成。它们都直接生成可玩关卡或谜题实例；自动试玩、bot、求解器和 MCTS 只负责构造或评价。

**Targeted primary-source addendum / 定向一手来源补核：** Two targeted passes added PCG sources 87–113: constrained/domain-transfer/multilayer MdMC branches; generator-specific training-data evaluation; video-conditioned and video-extracted Mario generation; autoencoder, constructive-primitive, common-latent, self-supervised, and mutation-model level generation; the PPLGG/ASP/GVGAI/Marahel/WFC metageneration lineage; the Mario and AIBIRDS comparison benchmarks; four classic evaluation frameworks; Danesh generator tuning; and a unified Sokoban generator study. Extension papers and duplicate DOI records were merged, while independent generation contributions remained separate. / 两轮定向一手来源复核新增 PCG 来源 87–113：约束、域迁移和多层 MdMC 分支，训练数据评价，视频条件/视频提取 Mario 生成，autoencoder、构造原语、共享潜空间、自监督及 mutation-model 关卡生成，PPLGG/ASP/GVGAI/Marahel/WFC 元生成谱系，Mario 与 AIBIRDS benchmark，四项经典评价框架，Danesh 生成器调优，以及统一 Sokoban 生成器研究。扩展论文和重复 DOI 合并，独立生成贡献则分列。

**Final independent-audit addendum / 最终独立审计补核：** The 2026-09-01 generation-only audit added sources 114–115: the *Corpus for Angry Birds Level Generation* and *Using Unconditional Diffusion Models in Level Generation for Super Mario Bros*. Both directly support level generation rather than gameplay-agent evaluation. Their first-party artifacts were inspected down to archive contents, training data, evaluator code, missing files, and licensing; both are conservatively labelled **Partial**. / 2026-09-01 的纯生成最终审计补入来源 114–115：*Corpus for Angry Birds Level Generation* 与 *Using Unconditional Diffusion Models in Level Generation for Super Mario Bros*。二者都直接服务关卡生成，而非评测玩游戏智能体。已对一手工件的压缩包内容、训练数据、evaluator 代码、缺失文件及许可证进行深核验，两者均保守标为 **Partial**。

## Executive finding / 核心结论

这次复核发现了**多项高置信漏项**，因此不能把当时的 82 条基线索引称为“全面检索完成”。漏项不是以玩游戏为目标的 agent paper，而是直接生成或修改以下对象的论文：完整游戏、可执行规则/机制、游戏工程代码、关卡/可玩内容、动作条件游戏世界，以及专门评估这些输出的 benchmark、dataset 或 evaluator。

下表中的论文题名或唯一标识均未出现在当前英文索引和三份既有 source notes 中。`P0` 表示产物和仓库范围直接重合，建议优先补；`P1` 表示仍符合现有 `SCOPE.md`，但属于共创、修复、数据、评估或领域框架，宜放在独立相邻分区。发现同一工作有扩展版时已合并为一个版本族，未重复计算成两个独立漏项。

## Method / 检索方法

1. 对当前索引抽取题名、arXiv ID、DOI 和项目链接，建立 exact-match 去重基线。
2. 通过 arXiv API 按提交时间倒序组合检索：`game generation`、`game development + LLM/agent`、`game code/coding`、`text-to-game`、`automated game design`、`game rule/mechanic generation`、`procedural content generation`、`level generation`、`game world model`、`action-conditioned + game/video`、`generative game engine`、`playable world`、`Minecraft + world model`。
3. 重点逐条阅读 2024–2026 年候选的官方 arXiv 摘要；同时用 DBLP 反查 CoG、AIIDE、FDG、IEEE Transactions on Games 等 proceedings/journal 记录，以发现无 arXiv 或题名不含常用关键词的工作。
4. 只接受作者 arXiv、官方 proceedings/DOI、作者项目页或作者仓库作为主来源。摘要中以 return、胜率、策略或任务成功率为中心的 playing paper 被排除；孤立美术/3D 资产、纯 QA、通用机器人/驾驶 world model 也被排除。
5. 检索截止为 2026-08-29；这是一轮高召回审计，不声称覆盖所有非英语数据库或尚未进入公开索引的 workshop 页面。

## 1. End-to-end games, code, rules, and generation evaluation

| Priority | Year | Missing paper/resource | Why it is in scope | Difference from current entries / alias check |
| --- | :---: | --- | --- | --- |
| P0 | 2024 | [Instruction-Driven Game Engines on Large Language Models](https://arxiv.org/abs/2404.00276) | 从自由文本规则预测后续游戏状态，形成可定制 Poker 规则的可执行 game engine；输出是游戏模拟器而非玩家策略。 | 当前无该 ID。后续 [Poker case study](https://arxiv.org/abs/2410.13441) 是同一 IDGE 版本族，宜合并引用，不算第二项。 |
| P0 | 2024 | [Word2World: Generating Stories and Worlds through Large Language Models](https://arxiv.org/abs/2405.06686) | 从故事生成 tile world、叙事和可玩游戏；作者明确以 playable games 和关卡消融评估。 | 当前无该 ID；[official code](https://github.com/umair-nasir14/Word2World)。与 Word2Minecraft 是 2D/3D 不同系统，不是别名。 |
| P1 | 2024 | [Open Role-Playing with Delta-Engines](https://arxiv.org/abs/2408.05842) | LLM 在既有 base engine 上逐步生成代码，改变角色成长和运行时玩法。 | 当前无该 ID；是受控 runtime mechanic/code editing，不是完整从零生成，也不是 NPC playing agent。 |
| P0 | 2024 | [Mechanic Maker: Accessible Game Development Via Symbolic Learning Program Synthesis](https://arxiv.org/abs/2410.01096) | 从用户示例合成可执行游戏机制，直接对应规则/机制生成。 | 当前无该 ID。与 2023 年 Mechanic Maker 2.0 名称相近但任务和实现不同，不是版本别名。 |
| P0 | 2025 | [Grammar and Gameplay-Aligned RL for Game Description Generation with LLMs](https://arxiv.org/abs/2503.15783) | 用 grammar/concept rewards 训练模型从自然语言生成可执行 GDL。 | 是现有 GGDG 的后续研究而非同一论文别名；[official code](https://github.com/tsunehiko/rlgdg)。 |
| P0 | 2025 | [STORY2GAME: Generating (Almost) Everything in an Interactive Fiction Game](https://arxiv.org/abs/2505.03547) | 生成故事、世界状态、动作前置条件/效果和 game-engine action code，并以能否完整交互通关验证。 | 当前无该 ID；不同于纯故事生成，也不同于现有 Zagii。 |
| P1 | 2025 | [Fly, Fail, Fix: Iterative Game Repair with Reinforcement Learning and Large Multimodal Models](https://arxiv.org/abs/2507.12666) | RL 只负责 playtest；LMM 根据轨迹反复修改游戏配置和机制以满足设计目标。 | 当前无该 ID；是生成/修复闭环，不是以 RL return 为最终产物。 |
| P0 | 2025 | [Multi-Agent Game Generation and Evaluation via Audio-Visual Recordings](https://arxiv.org/abs/2508.00632) | AVR-Agent 生成 JavaScript 游戏，AVR-Eval 用音视频运行记录选择和迭代生成物。 | 当前无该 ID；[official code](https://github.com/SamsungSAILMontreal/AVR-Eval-Agent)。不是现有 V-GameGym/PlaytestArena 的别名。 |
| P1 | 2025 | [Repairing General Game Descriptions (extended version)](https://arxiv.org/abs/2508.10438) | 自动寻找并修复违反形式要求的 GDL 规则描述。 | 当前无该 ID；属于规则生成后的 formal repair，而非纯游戏 QA。 |
| P0 | 2025 | [Automated Unity Game Template Generation from GDDs via NLP and Multi-Modal LLMs](https://arxiv.org/abs/2509.08847) | 从 GDD 抽取规范并生成 Unity C#、核心机制、系统和可运行 prototype template。 | 当前无该 ID；不同于 UniGen，后者从自然语言做更完整的 Unity 装配/调试。 |
| P0 | 2025 | [Real-Time World Crafting: Generating Structured Game Behaviors from Natural Language with Large Language Models](https://arxiv.org/abs/2510.16952) | 将自然语言编译为受限 DSL，在 ECS 游戏引擎中实时生成新行为和 spell mechanics。 | 当前无该 ID；是行为/机制生成，不是动作策略。 |
| P0 | 2026 | [Mortar: Evolving Mechanics for Automatic Game Design](https://arxiv.org/abs/2601.00105) | LLM + quality diversity 演化机制，并组合成完整可玩游戏进行评价。 | 当前无该 ID；与 GAVEL 都属 AGD，但生成表示、机制组合和评价协议不同。 |
| P0 | 2026 | [RuleSmith: Multi-Agent LLMs for Automated Game Balancing](https://arxiv.org/abs/2602.06232) | 搜索并输出可直接应用的规则参数/平衡修改；self-play 只是设计 evaluator。 | 当前无该 ID；不是以 LLM agent 的胜率为贡献，最终产物是平衡后的 rule configuration。 |
| P0 | 2026 | [Grounding Machine Creativity in Game Design Knowledge Representations](https://arxiv.org/abs/2603.07101) | 根据 goal playable patterns 合成 Unity C# 和可执行 game artifacts，并通过 Unity replay 检查编译。 | 当前无该 ID；比现有 DreamGarden 更偏受约束的可执行 pattern synthesis。 |
| P0 | 2026 | [GamED.AI: A Hierarchical Multi-Agent Framework for Automated Educational Game Generation](https://arxiv.org/abs/2604.23947) | 从教师题目生成完整可玩教育游戏，并用 mechanic contracts 和 deterministic quality gates 验证。 | 当前无该 ID；已有[官方 ACL demo record](https://doi.org/10.18653/v1/2026.acl-demo.84)，不是一般“教育活动生成”。 |
| P0 | 2026 | [WebGameBench: Requirement-to-Application Evaluation for Coding Agents via Browser-Native Games](https://arxiv.org/abs/2605.17637) | 111 个 specification-to-browser-game 任务，真实构建、部署、浏览器交互并经人工 gameplay 对齐验证。 | 当前 benchmark 表未收录；不同于 OpenGame-Bench 和 PlaytestArena，任务/标签/部署协议均独立。 |
| P0 | 2026 | [Distilling Game Code World Model Generation into Lightweight Large Language Models](https://arxiv.org/abs/2605.24375) | 从自然语言规则生成包含状态转移、合法动作、观察和奖励的可执行 Python 游戏环境，并提供 30-game 数据集和 verifier。 | 当前无该 ID；虽承接 Code World Models，但本论文的主要产物和评价是 GameCWM generation，而非玩家成绩。 |
| P1 | 2026 | [AutoBG: A Board Game Design Assistant](https://arxiv.org/abs/2606.01976) | 端到端生成并迭代修订完整桌游规则书，critic 和玩家 persona 只评估设计。 | 当前无该 ID；规则书不一定是可执行代码，宜放 human-in-the-loop rule design，而非完整游戏代码榜。 |
| P0 | 2026 | [The Verifier is the Curriculum: Execution-Gated Self-Distillation for Cross-Family Game Generation](https://arxiv.org/abs/2607.09709) | 用 Godot strict-launch verifier 自蒸馏从 brief 生成完整游戏，核心结果是未见 game family 的可启动生成率。 | 复用现有 GameCraft-Bench，但这是独立的训练方法论文，不是 benchmark 论文别名。 |
| P0 | 2026 | [MAGIC: Transition-Aware Generation of Navigable Multi-Scene Game Worlds](https://arxiv.org/abs/2607.11594) | 单提示生成可运行多场景 game project、portal scripts 和可导航布局，并提供 100-case transition benchmark。 | 当前无该 ID；[official code](https://github.com/sereneee1201/MAGIC)。不同于 AutoUE/单场景生成。 |

### Older rule-generation gaps / 较早但明确的规则生成漏项

| Priority | Year | Missing paper/resource | Why it is in scope | Difference / alias check |
| --- | :---: | --- | --- | --- |
| P0 | 2019 | [General Video Game Rule Generation](https://arxiv.org/abs/1906.05160) | 定义 GVGAI rule-generation track，从给定关卡生成 VGDL 规则，并提供 random/constructive/search generators。 | 现有索引只收录 GVGAI multitrack framework，没有这篇专门的 rule-generation 论文。 |
| P0 | 2023 | [Mechanic Maker 2.0: Reinforcement Learning for Evaluating Generated Rules](https://arxiv.org/abs/2309.09476) | 开源 rule-generation framework；RL 只是评估候选规则，产物是新规则集。 | 不是 2024 Mechanic Maker 的别名；二者任务、代码路径和用户研究不同。 |

## 2. Level and playable-content generation

| Priority | Year | Missing paper/resource | Why it is in scope | Difference from current entries / alias check |
| --- | :---: | --- | --- | --- |
| P0 | 2023 | [PCGPT: Procedural Content Generation via Transformers](https://arxiv.org/abs/2310.02405) | 用 offline-RL trajectories 和 transformer 迭代生成 Sokoban 关卡。 | 当前无该 ID；不是 MarioGPT 的别名，游戏域和建模方法不同。 |
| P0 | 2023/2024 | [ChatGPT4PCG Competition](https://arxiv.org/abs/2303.15662) / [second competition](https://arxiv.org/abs/2403.02610) | 专门评测 prompt/program 对 Science Birds 稳定、字符相似且多样的关卡生成。 | 同一竞赛版本族，建议一条记录同时引用两届，不计作两个独立 benchmark。 |
| P0 | 2024 | [Procedural Level Generation in Educational Games From Natural Language Instruction](https://doi.org/10.1109/TG.2024.3392670) | 官方 Transactions on Games 论文；从自然语言教学目标生成教育游戏关卡。 | 当前无 DOI；不同于 GamED.AI 的完整教育游戏生成。 |
| P0 | 2024 | [Improving Conditional Level Generation Using Automated Validation in Match-3 Games](https://doi.org/10.1109/TG.2024.3440214) | 生成并自动验证满足条件的 Match-3 关卡。 | 当前无 DOI；不是通用 PCG benchmark。 |
| P0 | 2024 | [Making New Connections: LLMs as Puzzle Generators](https://arxiv.org/abs/2407.11240) | 生成完整可玩的 Connections word puzzles，并与人工发表谜题做用户比较。 | 当前无该 ID；不是玩/解 Connections 的 agent paper。 |
| P0 | 2024 | [Moonshine: Distilling Game Content Generators into Steerable Generative Models](https://arxiv.org/abs/2408.09594) | 定义 text-to-game-map 任务，用合成标签蒸馏可控地图生成器。 | 当前无该 ID；不是 MarioGPT 的别名。 |
| P0 | 2024 | [PCGRL+: Scaling, Control and Generalisation in Reinforcement Learning Level Generators](https://arxiv.org/abs/2408.12525) | GPU/JAX PCGRL 生成器支持不同地图大小、pinpoints 和 OOD 尺寸泛化。 | 是现有 PCGRL 的实质扩展论文，不应被基础 PCGRL 条目替代。 |
| P0 | 2024/2025 | [ChatPCG](https://arxiv.org/abs/2406.11875) → [PCGRLLM](https://arxiv.org/abs/2502.10906) | LLM 生成 PCGRL reward，并在 2D 内容/故事条件任务中驱动关卡生成。 | PCGRLLM 摘要明确称为 ChatPCG 的 extended architecture；应合并版本族而非重复计数。 |
| P0 | 2025 | [Word2Minecraft: Generating 3D Game Levels through Large Language Models](https://arxiv.org/abs/2503.16536) | 将结构化故事转为带空间和玩法约束的可玩 Minecraft 关卡。 | 当前无该 ID；[official code](https://github.com/JMZ-kk/Word2Minecraft/tree/word2mc_v0)。与 Word2World 是不同 3D 系统。 |
| P0 | 2025 | [IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation](https://arxiv.org/abs/2503.12358) | 文本指令控制 RL 关卡生成器，评价未见指令的 controllability/generalization。 | 当前无该 ID；与 PCGRLLM 的“生成 reward”任务不同。 |
| P1 | 2025 | [Evolutionary Level Repair](https://arxiv.org/abs/2506.19359) | 对 PCGML 生成但不可用的关卡做搜索/QD 修复，使其功能完整。 | 当前无该 ID；属于 generation-pipeline repair，不是独立 bug-finding。 |
| P0 | 2025 | [Human-Aligned Procedural Level Generation RL via Text-Level-Sketch Shared Representation](https://arxiv.org/abs/2508.09860) | 文本、关卡和草图共同控制 PCGRL 输出，并发布生成代码/数据。 | 当前无该 ID；[official code/data](https://github.com/bic4907/VIPCGRL)。 |
| P0 | 2025 | [A Database-Driven Framework for 3D Level Generation with LLMs](https://arxiv.org/abs/2508.18533) | 生成多层 3D 关卡、房间布局、gameplay progression，并进行可导航性修复。 | 当前无该 ID；不是孤立 3D asset generation。 |
| P1 | 2025 | [From Unstable to Playable: Stabilizing Angry Birds Levels via Object Segmentation](https://arxiv.org/abs/2509.23787) | 检测并修复已有 PCG 生成的结构不稳定关卡，直接提升 playability。 | 当前无该 ID；应放 level repair，而不是 image segmentation。 |
| P0 | 2025 | [Zero-shot 3D Map Generation with LLM Agents](https://arxiv.org/abs/2512.10501) | Actor/Critic 以自然语言配置 PCG 工具生成结构有效的 3D maps，并提出 instruction-following benchmark。 | 当前无该 ID；不是一般软件操作 agent。 |
| P0 | 2025 | [From Generation to Gameplay: Authoring Race Tracks With Repulsive Curves](https://doi.org/10.1109/TG.2025.3561107) | 官方 Transactions on Games 论文，输出可驾驶赛道并评价从生成到 gameplay 的可用性。 | 当前无 DOI；不是 racing agent paper。 |
| P0 | 2026 | [STRUM: End-to-End Generation of Playable Rhythm-Game Charts](https://arxiv.org/abs/2605.12135) | 从原始音频生成 Clone Hero/YARG 多乐器可玩谱面，并发布 benchmark manifest。 | 当前无该 ID；谱面直接决定玩法，不是孤立音乐生成。 |
| P0 | 2026 | [Multiverse: Language-Conditioned Multi-Game Level Blending](https://arxiv.org/abs/2603.26782) | 文本控制跨游戏关卡混合和组合提示的 zero-shot level generation。 | 当前无该 ID；是 MarioGPT/单域 text-to-level 的多游戏扩展，不是别名。 |
| P1 | 2026 | [From World-Gen to Quest-Line](https://arxiv.org/abs/2604.25482) | 结构化生成 RPG world、角色、campaign quest 和 quest expansion；quest 属于可玩内容。 | 当前无该 ID；不生成完整 engine，宜放 playable-content/quest generation。 |
| P0 | 2026 | [From LLM-Driven Trading Card Generation to Procedural Relatedness](https://arxiv.org/abs/2604.27972) | 同时生成个性化卡牌视觉与 mechanics，并以玩家共创和机制表征评估。 | 当前无该 ID；因包含玩法机制，不属于孤立 image asset。 |
| P0 | 2026 | [Representing and Generating Levels Over Time through Playtrace Reconstructive Partitioning](https://arxiv.org/abs/2607.12097) | 用 playtrace-aware representation 生成有效 Sokoban 关卡并比较六种 PCG 方法。 | 当前无该 ID；不是 playing-agent paper。 |
| P0 | 2026 | [Procedural Content Metageneration via Program Search and Continual Abstraction Discovery](https://arxiv.org/abs/2608.17947) | 搜索完整 Python content-generator programs，在四种游戏中输出新的关卡生成器。 | 当前无该 ID；生成的是 generator 本身，仍直接服务关卡生成。 |

### Scope/evaluation readings that are also absent

| Priority | Year | Missing paper/resource | Why it matters | Difference / alias check |
| --- | :---: | --- | --- | --- |
| P1 | 2024 | [On the Evaluation of Procedural Level Generation Systems](https://arxiv.org/abs/2404.18657) | 建立 PCG level evaluation taxonomy，并系统审查现有评价实践。 | 当前 survey 区只有 2011/2018 奠基综述；这是专门的现代 evaluation reading。 |
| P1 | 2024 | [Procedural Content Generation via Generative Artificial Intelligence](https://arxiv.org/abs/2407.09013) | 直接综述 generative-AI PCG 和数据稀缺问题。 | 与 2018 PCGML survey 时间和模型范围不同。 |
| P1 | 2024 | [Procedural Content Generation in Games: A Survey with Insights on Emerging LLM Integration](https://arxiv.org/abs/2410.15644) | 覆盖 search、ML、hybrid 和 LLM PCG。 | 不是上条的别名；二者作者、taxonomy 和覆盖范围不同。 |

## 3. Game-specific interactive world generation

| Priority | Year | Missing paper/resource | Why it is in scope | Difference from current entries / alias check |
| --- | :---: | --- | --- | --- |
| P0 | 2023 | [Promptable Game Models: Text-Guided Game Simulation via Masked Diffusion Models](https://arxiv.org/abs/2303.13472) | 用低层/高层文本动作控制 Tennis/Minecraft 生成式模拟，并发布数据、模型和框架。 | 当前 interactive-world 页缺失这一前 Genie/GameNGen 的直接先驱；[official project](https://snap-research.github.io/promptable-game-models/)。 |
| P0 | 2024/2025 | [Learning Generative Interactive Environments by Trained Agent Exploration](https://arxiv.org/abs/2409.06445) / [Exploration-Driven Generative Interactive Environments](https://arxiv.org/abs/2504.02515) | GenieRedux 是 Genie 的开放实现；扩展版提供 AutoExplore、974-environment RetroAct 数据和 action-controlled generation。 | 同一 GenieRedux 版本族，建议以 2025 扩展版为主、2024 版为先行稿；[official code/data](https://github.com/insait-institute/GenieRedux)。 |
| P1 | 2025 | [Position: Interactive Generative Video as Next-Generation Game Engine](https://arxiv.org/abs/2503.17359) | 直接提出 generative game engine 的模块与 L0–L4 maturity roadmap。 | 不是生成模型，适合 field framing；当前只有 2026 Pixels-to-States perspective。 |
| P0 | 2026 | [Scalable Generative Game Engine: Breaking the Resolution Wall via Hardware-Algorithm Co-Design](https://arxiv.org/abs/2602.00608) | 在 racing/platformer action-conditioned benchmarks 上实现实时高分辨率 neural gameplay。 | 当前无该 ID；是系统/推理扩展，不是 Matrix-Game 别名。 |
| P0 | 2026 | [MultiGen: Level-Design for Editable Multiplayer Worlds in Diffusion Game Engines](https://arxiv.org/abs/2603.06679) | 外部 persistent memory 允许编辑环境结构并保持多人共享世界一致性。 | 当前无该 ID；与 Solaris 的双视角 Minecraft 模拟不同。 |
| P0 | 2026 | [WildWorld / WildBench](https://arxiv.org/abs/2603.23497) | 1.08 亿帧 ARPG action/state dataset，并专门评测 Action Following 与 State Alignment。 | 当前只在 Marionette 工件列顺带链接 WildWorld，没有把独立 dataset/benchmark paper 收为条目；[official project](https://shandaai.github.io/wildworld-project/)。 |
| P0 | 2026 | [ActionParty: Multi-Subject Action Binding in Generative Video Games](https://arxiv.org/abs/2604.02330) | 同时控制最多七名玩家的动作条件视频世界，评价 action binding 和 identity consistency。 | 当前无该 ID；与 ReactiveGWM 的玩家/NPC 双条件不同。 |
| P0 | 2026 | [EgoCS-400K: An Egocentric Gameplay Dataset for World Models](https://arxiv.org/abs/2606.18180) | 10,000 小时 CS/CS2 视频—动作—状态—事件对齐数据，专供 action-conditioned future/world modeling。 | 当前无该 ID；不是 game-agent behavior dataset，主用途是生成 world model。 |
| P0 | 2026 | [Multiplayer Interactive World Models with Representation Autoencoders](https://arxiv.org/abs/2607.05352) | 从四名玩家动作生成 Rocket League 实时视频，并评估长时稳定和物理一致性。 | 当前无该 ID；与 Solaris/MASS 不同模型、游戏和状态表示。 |
| P0 | 2026 | [WanToFight: Real-Time Generative Game Engine for Multi-Player Combat Interaction](https://arxiv.org/abs/2607.12592) | 两人键盘动作驱动 KOF'97 生成式引擎，30 FPS 完整对局 rollout。 | 当前无该 ID；不是 fighting-game policy paper。 |
| P0 | 2026 | [MASS: Multiplayer World Models with Authoritative Shared State](https://arxiv.org/abs/2608.06257) | 从 joint actions 学习 authoritative typed state，再按相机生成一致视角；在多人 Snake 上评测。 | 当前无该 ID；与 Rocket League latent-video model 不是别名。 |
| P0 | 2026 | [PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives](https://arxiv.org/abs/2608.13552) | 171 个交互场景，以 agent player 追求目标来评测几何、交互和状态演化；评分对象是生成世界。 | 当前无该 ID；agent 只是 evaluator，不以 agent task-success 作为玩家能力结论；[official code/data](https://github.com/kxding/PlayWorld)。 |
| P1 | 2026 | [Position: Profiling Game Worlds by Transition Complexity](https://arxiv.org/abs/2608.18079) | 为 game-world datasets/models 定义 transition-complexity benchmark metadata。 | 不是 generator；适合 field framing，不应进入模型排行榜。 |
| P0 | 2026 | [Game2World Engine](https://arxiv.org/abs/2608.24680) | 建立 gameplay-UI taxonomy、96K 成对视频和 303-game in-the-wild evaluation set，用于清洗 world-model 训练视频。 | 当前无该 ID；是生成数据工程/数据集，不是游戏 UI asset generator。 |
| P0 | 2026 | [Magpie: Real-Time World Renderer for Interactive Games](https://arxiv.org/abs/2608.27168) | 传统 game engine 维护规则/状态，生成模型把 white-box frames 实时渲染成游戏画面，保持可复现交互结果。 | 2026-08-27 发布，早于截止日两天；当前无该 ID。不同于纯视频 next-frame game engine。 |

## 4. Borderline candidates deliberately not promoted as omissions

以下候选在关键词检索中出现，但按现有严格口径不建议直接加入核心索引：

| Candidate | Decision | Reason |
| --- | --- | --- |
| [GameWAM](https://arxiv.org/abs/2608.26200)、[ActSWM](https://arxiv.org/abs/2607.26712)、[AgentOdyssey](https://arxiv.org/abs/2606.24893)、[Code World Models for General Game Playing](https://arxiv.org/abs/2510.04542) | Exclude from generation core | 主要结论是 action/policy、规划或任务成功；即使内部生成 world model，也以玩游戏为目标。GameCWM distillation 之所以列入，是因为其论文主体改为环境生成和 verifier。 |
| [GBQA](https://arxiv.org/abs/2604.02648)、VideoGameQA-Bench、一般自动 game testing papers | Exclude | 独立 QA/bug finding；不是生成 benchmark 的 evaluator 或生成—修复闭环。 |
| [PlayCoder / PlayEval](https://arxiv.org/abs/2604.19742) | Borderline | benchmark 覆盖六类通用 GUI application，不是 game-generation-specific；可在 broad coding appendix 引用，但不应作为专用游戏 benchmark 计数。 |
| [Beyond Asking: Personalized Game Generation](https://arxiv.org/abs/2608.16196) | Borderline | 核心贡献是从玩家行为推断 profile；最终只做 difficulty adaptation，没有证明生成完整新游戏/关卡。 |
| [PANGeA](https://arxiv.org/abs/2404.19721)、纯剧情/对话/NPC 生成 | Exclude from strict core | 主要产物是 narrative/dialogue；除非索引单独扩展到叙事 PCG，不应与可执行游戏/关卡混排。 |
| CrawLLM、GameTileNet、DreamCraft、Minecraft building、cutscene/UI/sprite-only papers | Exclude or component appendix | 主要产物是孤立 asset、建筑或呈现组件；不满足“直接决定玩法/构成可玩关卡”的门槛。 |
| The Matrix、ABot-World-0、MultiWorld、WorldRoamBench、WBench、WorldMark、ReWorld、AlayaWorld 等 | Exclude from game-specific core | 声明范围横跨现实、机器人、驾驶或通用交互场景；即使使用游戏数据/演示，也不是 game-specific generator/evaluator。 |
| [Toward Stable World Models](https://arxiv.org/abs/2503.08122) | Borderline framing | 评价方法与 generative environments 有关，但论文不是游戏专用；若收录，应放通用 IWM evaluation reading，而非游戏 benchmark。 |
| [IF:CARGO](https://arxiv.org/abs/2608.12195) | Borderline co-creation | LLM 是固定游戏内的语义编译器，由玩家编写 IF/THEN 规则；属于 AI-native mechanic authoring，但不是自动生成新游戏。 |

## Recommended update order / 建议补录顺序

1. 先补专用 benchmark/dataset：WebGameBench、WildWorld/WildBench、EgoCS-400K、PlayWorld、Game2World、ChatGPT4PCG。
2. 再补端到端/代码/规则：STORY2GAME、AVR-Agent、Automated Unity Template、GameCWM distillation、RLGDG、Mortar、RuleSmith、MAGIC、GamED.AI。
3. 再补 2024–2026 关卡生成主线：Word2World/Word2Minecraft、Moonshine、PCGRL+、IPCGRL、VIPCGRL、Multiverse、PRP、PCG metageneration。
4. 最后补 interactive-world models 与 field framing，并继续维持“新世界生成”与“既有游戏模拟”分栏。

## Audit limitation / 局限

QA snapshot：本报告引用的 **73 个唯一 arXiv ID** 已在同一批 arXiv API 请求中全部返回；**4 个 DOI** 均由 DOI resolver 成功解析；本文件通过仓库的 Markdown lint（0 issues）。这些数字包含版本族和“明确排除”表里的对照论文，因此不等于建议新增条目数。

本报告核验的是“论文/资源是否存在、是否符合生成范围、是否在现有索引中缺失”。它没有替代逐项 artifact availability 审计；在正式补入公开表格前，仍应分别检查作者仓库、权重、数据、license 和 evaluator 在截止日是否真实可用，并同步更新中英文页面。
