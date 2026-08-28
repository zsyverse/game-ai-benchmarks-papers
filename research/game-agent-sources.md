# Game Agent benchmarks 与关键论文：一手来源核验稿

> 最后核验：2026-08-29。本文是供仓库中英文 README 二次整理的双语资料底稿，不是论文数量竞赛。仅收录论文官网、arXiv/OpenReview/正式 proceedings、作者项目页或官方 GitHub 可相互印证的条目。

## 口径 / Scope

- **[B] Benchmark / Environment**：有明确任务、评测协议或可运行环境，可用于横向比较。
- **[P] Platform / Framework**：提供研究接口，但没有唯一固定任务集或总指标；不应包装成排行榜 benchmark。
- **[A] Agent / Method paper**：提出并评估一个 agent/方法，但没有发布可独立复用的 benchmark。
- 指标写的是论文或官方实现定义的主要指标；同一环境的后续论文可能采用不同预算、随机种子和聚合方式，不能只看一个总分。
- “Game agent”限于真实游戏、明确的 game-like environment、文本冒险或游戏论环境。Habitat、AI2-THOR、ALFWorld、OSWorld 等通用机器人/GUI benchmark 未混入本清单。

## 1. LLM / VLM 游戏智能体 benchmarks

### BALROG — Benchmarking Agentic LLM and VLM Reasoning On Games [B]

- **年份 / 状态**：2025，ICLR 2025 conference paper。
- **环境与任务 / Environments & tasks**：统一接入 BabyAI、Crafter、TextWorld、Baba Is AI、MiniHack、NetHack 六个程序生成环境；同时测试纯文本 LLM 与视觉语言模型的长程交互、探索、空间推理和规划。
- **指标 / Metrics**：每项映射到 `0–100` progression；MiniHack、BabyAI、Baba Is AI 为完成即 100，否则 0；TextWorld、Crafter、NetHack 使用连续进度。NetHack 另以人类轨迹统计构建 dungeon/experience level 到通关概率的进度指标。
- **代码 / Code**：[balrog-ai/BALROG](https://github.com/balrog-ai/BALROG)；[leaderboard/project](https://balrogai.com/)。
- **一手证据 / Primary evidence**：[论文](https://arxiv.org/abs/2411.13543)明确列出六个环境、指标和 ICLR 2025 状态；官方代码树中也分别存在六个 environment wrapper。

### VideoGameBench — Can Vision-Language Models Complete Popular Video Games? [B]

- **年份 / 状态**：2025，arXiv preprint（2026-05 更新；截至核验日未在作者页标注正式 venue）。
- **环境与任务 / Environments & tasks**：VLM 只看原始画面、目标和通用控制说明，实时游玩并尝试完整通关 10 个 1990 年代游戏；测试集含 7 个公开游戏和 3 个保密游戏。Lite 版本在模型思考时暂停游戏。
- **指标 / Metrics**：按人工确定的剧情/关卡 checkpoint 与完整 walkthrough 的相对位置计算每局完成百分比；各游戏等权平均。秘密游戏用于检验 unseen-game generalization。
- **代码与限制 / Code & caveat**：[alexzhang13/videogamebench](https://github.com/alexzhang13/videogamebench)；代码 MIT，但 ROM/商业游戏不随代码授权，用户须合法持有。
- **一手证据 / Primary evidence**：[论文](https://arxiv.org/abs/2505.18134)给出 10-game test、3 个秘密游戏、checkpoint scoring 和 Lite 协议；官方 README 列出 Game Boy/MS-DOS 实现与游戏清单。

### SmartPlay — A Benchmark for LLMs as Intelligent Agents [B]

- **年份 / 状态**：2024，ICLR 2024。
- **环境与任务 / Environments & tasks**：6 类游戏（Rock–Paper–Scissors、two-armed bandit、Tower of Hanoi、Messenger、Crafter、MineDojo creative tasks），最多 20 个设置和无限程序化变体；覆盖 9 种能力，如规划、空间推理、对象依赖和从历史学习。
- **指标 / Metrics**：reward、completion rate、game-specific score；论文再以人类分数归一化，并按每个游戏对九种能力的权重计算 capability score。
- **代码 / Code**：[microsoft/SmartPlay](https://github.com/microsoft/SmartPlay)。
- **一手证据 / Primary evidence**：[论文](https://arxiv.org/abs/2310.01557)第 4.2 节定义三类指标与 human-normalized capability score；官方 README 给出六类游戏和 ICLR 引用。

### GameBench — Evaluating Strategic Reasoning Abilities of LLM Agents [B]

- **年份 / 状态**：2024，arXiv preprint。
- **环境与任务 / Environments & tasks**：9 个较冷门的桌游、卡牌和社交推理游戏，覆盖抽象策略、随机性、隐藏信息、语言交流、合作与社会推断；让模型、scaffold、随机基线和人类互赛。
- **指标 / Metrics**：单局得分位于 `[0,1]` 且双方和为 1；跨局主要使用 exponential Bradley–Terry rating，并以 bootstrap 给置信区间，也报告逐游戏平均分。
- **代码与数据 / Code & data**：[Joshuaclymer/GameBench](https://github.com/Joshuaclymer/GameBench)，代码 MIT、match data CC-BY。
- **一手证据 / Primary evidence**：[论文](https://arxiv.org/abs/2406.06613)明确给出 9 games、Bradley–Terry 聚合及人类/随机基线；官方仓库包含 `matches.json` 和复现实验脚本。

### MACHIAVELLI — Reward 与伦理行为权衡的交互小说 benchmark [B]

- **年份 / 状态**：2023，ICML 2023；论文题为 *Do the Rewards Justify the Means? Measuring Trade-Offs Between Rewards and Ethical Behavior in the MACHIAVELLI Benchmark*。
- **环境与任务 / Environments & tasks**：基于人类创作的 Choose-Your-Own-Adventure 文本游戏；完整环境超过 50 万 scenes，官方固定 test set 为 30 个困难游戏，重点评估长程规划、社会决策及“高回报但不道德”的权衡。
- **指标 / Metrics**：游戏 reward/achievement 与分场景 behavioral annotations（伤害、欺骗、权力等）并列报告；官方脚本从轨迹生成统一 results，而非只用 reward 排名。
- **代码与数据 / Code & data**：[aypan17/machiavelli](https://github.com/aypan17/machiavelli)（数据另行下载）。
- **一手证据 / Primary evidence**：[论文](https://arxiv.org/abs/2304.03279)与官方 README 均说明 30-game test、轨迹评估和行为标注；这是 game-agent safety benchmark，不是一般伦理问答集。

## 2. Minecraft 与开放世界

### Project Malmo [P]

- **年份 / 状态**：2016，IJCAI demo/platform；官方仓库现已 archived。
- **环境与任务 / Environment & task**：在 Minecraft 上提供任务定义、观测、动作和奖励接口，适合导航、建造、协作及 RL 实验。
- **指标 / Metrics**：平台没有唯一总指标；由 mission XML/实验定义 reward、success 和 episode statistics。
- **代码 / Code**：[microsoft/malmo](https://github.com/microsoft/malmo)；[Microsoft Research 项目页](https://www.microsoft.com/en-us/research/project/project-malmo/)。
- **一手证据 / Primary evidence**：官方项目页与仓库均把 Malmo 定义为 Minecraft 上的 AI experimentation platform，因此应标作平台而不是固定 benchmark。

### MineRL — A Large-Scale Dataset of Minecraft Demonstrations [B]

- **年份 / 状态**：2019，IJCAI 2019。
- **环境与任务 / Environment & task**：Minecraft simulator-paired human demonstration dataset，覆盖多个层级任务；论文发布超过 **60 million** 自动标注 state–action pairs。
- **指标 / Metrics**：任务级 episode return、success rate 与样本效率；具体交互预算须跟随所采用的 MineRL competition/protocol 报告，不能跨年份直接混分。
- **代码 / Code**：[minerllabs/minerl](https://github.com/minerllabs/minerl)。
- **一手证据 / Primary evidence**：[论文](https://arxiv.org/abs/1907.13440)摘要明确给出 60M+ state–action pairs、模拟器配对和多任务定位；官方代码提供环境与数据接口。

### MineRL BASALT — Learning from Human Feedback [B]

- **年份 / 状态**：2021，NeurIPS 2021 Competition Track。
- **环境与任务 / Environment & task**：4 个难以写出硬编码 reward 的自然语言 Minecraft 任务，例如“建造瀑布并拍一张有景观感的照片”；每项配人类 demonstrations。
- **指标 / Metrics**：读过任务描述的人类评审比较 agent 行为，核心是 human preference / pairwise ranking，而不是可被 reward hacking 的脚本分数。
- **代码 / Code**：[MineRL BASALT 论文](https://arxiv.org/abs/2107.01969)；后续固定资源见 BEDD。
- **一手证据 / Primary evidence**：论文摘要明确说明 4 tasks、单任务单 agent、human evaluation 和 demonstration baseline。

### BEDD — BASALT Evaluation and Demonstrations Dataset [B]

- **年份 / 状态**：2023，NeurIPS 2023 Datasets and Benchmarks，Oral。
- **环境与任务 / Environment & task**：把两届 BASALT 固化成可复用数据：约 14,000 条 human videos、26 million image–action pairs，以及 3,000+ dense pairwise human evaluations。
- **指标 / Metrics**：新 agent 与固定 pairwise-human-evaluation leaderboard 比较；适合训练/评估 preference model 与 fuzzy-task agent。
- **代码与数据 / Code & data**：[minerllabs/basalt-benchmark](https://github.com/minerllabs/basalt-benchmark)。
- **一手证据 / Primary evidence**：[论文](https://arxiv.org/abs/2312.02405)摘要给出数据规模、pairwise evaluations 和 fixed preliminary leaderboard；官方仓库提供数据与评测代码。

### MineDojo — Building Open-Ended Embodied Agents with Internet-Scale Knowledge [B]

- **年份 / 状态**：2022，NeurIPS 2022 Datasets and Benchmarks；Outstanding Paper。
- **环境与任务 / Environment & task**：当前发布含 **3,142 tasks**：1,581 programmatic、1,560 creative、1 个 Ender Dragon playthrough；另开放 730K YouTube videos、约 7K Wiki pages、340K Reddit posts。
- **指标 / Metrics**：programmatic tasks 可按 simulator ground truth 自动判定；creative tasks 没有天然精确成功条件，可用 MineCLIP learned reward/人工评估；playthrough 看最终 achievement。不存在适用于 3,142 项的单一无损总分。
- **代码与数据 / Code & data**：[MineDojo/MineDojo](https://github.com/MineDojo/MineDojo)；[OpenReview](https://openreview.net/forum?id=rc8o_j8I8PX)。
- **一手证据 / Primary evidence**：官方 README 给出三类任务的精确数量、数据规模和许可；OpenReview 证明 NeurIPS D&B 状态。

## 3. 通用游戏智能、经典 RL 与交互式环境

### Arcade Learning Environment (ALE) [B]

- **年份 / 状态**：2013，JAIR；2018 年 JAIR 评测协议修订。
- **任务 / Task**：统一 Atari 2600 屏幕输入与离散动作，用数十款差异很大的游戏检验 domain-independent agent。
- **指标 / Metrics**：逐游戏 episode return、human-normalized score，再做 mean/median 等聚合；应说明 no-op starts、frame skip、训练预算和 sticky actions。2018 修订专门指出协议不一致会破坏可比性。
- **代码 / Code**：[Farama ALE](https://github.com/Farama-Foundation/Arcade-Learning-Environment)。
- **一手证据 / Primary evidence**：[原始论文](https://arxiv.org/abs/1207.4708)报告 55+ games；[协议修订](https://arxiv.org/abs/1709.06009)引入 sticky actions 与 best practices。

### Procgen Benchmark [B]

- **年份 / 状态**：2020，ICML 2020。
- **任务 / Task**：16 个高速、程序生成的 game-like environments；用有限训练 levels 与未见 levels 区分 sample efficiency 和 generalization。
- **指标 / Metrics**：每个环境的 episode return/level completion，并按论文给出的区间归一化后跨 16 环境汇总；须同时报告 train 与 test distribution。
- **代码 / Code**：[openai/procgen](https://github.com/openai/procgen)（官方标注 maintenance mode）。
- **一手证据 / Primary evidence**：[PMLR 论文页](https://proceedings.mlr.press/v119/cobbe20a.html)和[arXiv](https://arxiv.org/abs/1912.01588)明确给出 16 environments 与 sample-efficiency/generalization 目标。

### General Video Game AI (GVGAI) [B]

- **年份 / 状态**：框架始于 2014；综述/框架论文 2018，IEEE Transactions on Games。
- **任务 / Task**：用 Video Game Description Language 生成大量未知游戏；tracks 包括有/无 forward model 的通用游玩、level generation 和 rule generation。
- **指标 / Metrics**：playing tracks 通常按 win、game score 和跨游戏 competition rank；生成 tracks 使用各 track 当年规则，不能混成一个永久指标。
- **代码 / Code**：[GAIGResearch/GVGAI](https://github.com/GAIGResearch/GVGAI)；[competition site](https://gvgai.net/)。
- **一手证据 / Primary evidence**：[框架论文](https://arxiv.org/abs/1802.10363)说明未知多游戏、VGDL 与多个 agent/content-generation tracks。

### DeepMind Lab [P]

- **年份 / 状态**：2016 technical report；持续作为 3D first-person research platform 使用。
- **任务 / Task**：像素输入下的部分可观测 3D 导航、记忆、探索和任务学习；任务可定制。常见 DMLab-30 是后续固定的 30-task protocol，不等于平台本身只有 30 项。
- **指标 / Metrics**：环境/任务原始 score；DMLab-30 常做人类归一化跨任务聚合，须同时声明 protocol。
- **代码 / Code**：[google-deepmind/lab](https://github.com/google-deepmind/lab)。
- **一手证据 / Primary evidence**：[DeepMind Lab 论文](https://arxiv.org/abs/1612.03801)把它定义为 customizable 3D platform；[IMPALA](https://arxiv.org/abs/1802.01561)是一手的 DMLab-30 使用来源。

### NetHack Learning Environment (NLE) [B]

- **年份 / 状态**：2020，NeurIPS 2020；维护已从 archived 的 Facebook repo 转至 NetHack-LE 组织。
- **任务 / Task**：程序生成、随机、部分可观测的终端 roguelike；官方任务从 score/staircase 等子目标到完整 NetHack，考验探索、规划、技能习得和长程生存。
- **指标 / Metrics**：任务 success/episode return、NetHack score、dungeon/experience progression 或 ascension rate；采用哪一个必须明示。
- **代码 / Code**：[NetHack-LE/nle](https://github.com/NetHack-LE/nle)。
- **一手证据 / Primary evidence**：[论文](https://arxiv.org/abs/2006.13760)明确给出 NeurIPS 2020、开放源码及复杂度定位；当前官方 README 说明 NetHack 3.6.7 和标准任务接口。

### MiniHack [P/B]

- **年份 / 状态**：2021，NeurIPS 2021 Datasets and Benchmarks。
- **任务 / Task**：基于 NetHack 实体与动力学，用人类可读 description files 或 Python 快速构造从小房间到复杂程序世界的 RL testbed；随附多组 navigation、skill acquisition、exploration 等任务。
- **指标 / Metrics**：由具体 task 的 success/return 和 train–test variations 决定；框架本身没有唯一总分。
- **代码 / Code**：[NetHack-LE/minihack](https://github.com/NetHack-LE/minihack)。
- **一手证据 / Primary evidence**：[OpenReview](https://openreview.net/forum?id=skFwlyefkWJ)和[论文](https://arxiv.org/abs/2109.13202)说明 sandbox 定位及 D&B 状态。

### Crafter [B]

- **年份 / 状态**：2022，ICLR 2022。
- **任务 / Task**：单个程序生成 2D open-world survival game 同时测试采集、制作、战斗、探索、泛化和长程信用分配。
- **指标 / Metrics**：固定 **22 achievements**；官方要求 1M environment-step budget，报告每项 achievement success rate 与其 geometric-mean **Crafter score**，不应只报 reward。
- **代码 / Code**：[danijar/crafter](https://github.com/danijar/crafter)。
- **一手证据 / Primary evidence**：[论文](https://arxiv.org/abs/2109.06780)与官方 README 明确列出 22 achievements、1M budget 和几何平均公式。

### TextWorld [P/B] 与 Jericho [P/B]

- **年份 / 状态**：TextWorld 2018，IJCAI Computer Games Workshop；Jericho 2019，CoRR/arXiv technical report。
- **任务 / Task**：TextWorld 可自动生成或手工制作 text games，控制 world size、quest length、语言和难度；Jericho 封装人类创作的 interactive fiction，突出组合动作空间、语言理解和常识推理。
- **指标 / Metrics**：game score、quest success、steps/moves；Jericho 论文在 32 个受支持游戏上给 baseline，而不是声称所有 IF 游戏共享一个归一总分。
- **代码 / Code**：[microsoft/TextWorld](https://github.com/microsoft/TextWorld)、[microsoft/jericho](https://github.com/microsoft/jericho)。
- **一手证据 / Primary evidence**：[TextWorld](https://arxiv.org/abs/1806.11532)和[Jericho](https://arxiv.org/abs/1909.05398)论文分别说明生成式 benchmark 与 32-game evaluation。

### OpenSpiel [P]、PettingZoo [P]、Hanabi Learning Environment [B]

- **年份 / 状态**：OpenSpiel 2019 technical report；PettingZoo 2021 NeurIPS；Hanabi Challenge 2020 *Artificial Intelligence*。
- **任务 / Task**：OpenSpiel 覆盖 perfect/imperfect-information、zero/general-sum、顺序/同时行动游戏与规划算法；PettingZoo 用 AEC/parallel API 标准化多智能体环境；Hanabi 是 2–5 人、纯合作、信息不完备的固定 challenge。
- **指标 / Metrics**：OpenSpiel 常用 return、exploitability/NashConv、best-response gap 等；PettingZoo 没有统一指标；Hanabi 用 team score、perfect-game rate 及与固定/未知队友的表现。
- **代码 / Code**：[OpenSpiel](https://github.com/google-deepmind/open_spiel)、[PettingZoo](https://github.com/Farama-Foundation/PettingZoo)、[Hanabi Learning Environment](https://github.com/google-deepmind/hanabi-learning-environment)。
- **一手证据 / Primary evidence**：[OpenSpiel](https://arxiv.org/abs/1908.09453)、[PettingZoo](https://arxiv.org/abs/2009.14471)、[Hanabi Challenge](https://arxiv.org/abs/1902.00506)分别界定 framework/API/challenge；不能把前两者冒充单一排行榜。

### Melting Pot 2.0 [B]

- **年份 / 状态**：2022 technical report；官方 suite 持续维护。
- **任务 / Task**：每个 scenario = substrate + background population，覆盖合作、竞争、混合激励、非对称角色；重点测与训练时未见 social partners 互动的泛化。
- **指标 / Metrics**：每个 scenario 的 focal-population return，再按官方 evaluation protocol 聚合为 social-generalization score；不能只在熟悉队友上测试。
- **代码 / Code**：[google-deepmind/meltingpot](https://github.com/google-deepmind/meltingpot)。
- **一手证据 / Primary evidence**：[Melting Pot 2.0 report](https://arxiv.org/abs/2211.13746)定义 substrate/background-population、novel-partner protocol 和 mixed incentives。

## 4. RTS / MOBA / FPS 与竞技游戏

### StarCraft II Learning Environment (SC2LE / PySC2) [P/B]

- **年份 / 状态**：2017，DeepMind–Blizzard technical paper。
- **任务 / Task**：StarCraft II feature planes/raw interface、完整对局、官方 mini-games 与人类 expert replay data；同时包含大动作空间、部分可观测和超长时程。
- **指标 / Metrics**：mini-game task score；完整游戏 win/loss 与 league/opponent-conditioned win rate；replay imitation 可报 action/outcome prediction。没有跨三类任务的唯一总分。
- **代码 / Code**：[google-deepmind/pysc2](https://github.com/google-deepmind/pysc2)。
- **一手证据 / Primary evidence**：[论文](https://arxiv.org/abs/1708.04782)明确描述 mini-games、main maps、replays、observations/actions/rewards。

### SMAC 与 SMACv2 [B]

- **年份 / 状态**：SMAC 2019，AAMAS 2019；SMACv2 2022 technical paper/benchmark release。
- **任务 / Task**：SMAC 将 StarCraft II micromanagement 做成 cooperative MARL，每个 unit 是只见 local observation 的 agent；SMACv2 改用程序生成 team/unit/start configurations，并加入 Extended Partial Observability，要求对未见实例做 closed-loop control。
- **指标 / Metrics**：各 map/distribution 的 test win rate 与 episode return，跨 seeds 报均值/中位数和不确定性；SMACv2 必须在 held-out generated scenarios 上测试。
- **代码 / Code**：[oxwhirl/smac](https://github.com/oxwhirl/smac)、[oxwhirl/smacv2](https://github.com/oxwhirl/smacv2)。
- **一手证据 / Primary evidence**：[SMAC](https://arxiv.org/abs/1902.04043)论文定义 unit-level cooperative micromanagement；[SMACv2](https://arxiv.org/abs/2212.07489)明确指出原版可被 open-loop policy 利用，并定义 procedural generalization/EPO。

### ViZDoom [P/B]

- **年份 / 状态**：2016，IEEE CIG 2016。
- **任务 / Task**：基于 Doom 的第一人称 raw-screen RL platform；支持可定制 scenarios，原论文给出 move-and-shoot 与 maze navigation。
- **指标 / Metrics**：由 scenario 定义的 return、kills/frags、survival、navigation success；竞赛 track 另用各年规则，没有跨所有场景的永久总分。
- **代码 / Code**：[Farama-Foundation/ViZDoom](https://github.com/Farama-Foundation/ViZDoom)。
- **一手证据 / Primary evidence**：[论文](https://arxiv.org/abs/1605.02097)明确 raw visual input、两类实验和 customizable scenarios。

### Google Research Football [B]

- **年份 / 状态**：2020，AAAI 2020；原 `google-research/football` 仓库已 archived，复现时需记录版本。
- **任务 / Task**：物理驱动 3D football simulator，含 Football Benchmarks 的三个不同难度 full games 与 Football Academy 小场景；支持 multiplayer/MARL。
- **指标 / Metrics**：episode return、scoring reward、win rate/goal difference，以及 Academy scenario completion；应按固定 opponent 与 difficulty 报告。
- **代码 / Code**：[google-research/football](https://github.com/google-research/football)。
- **一手证据 / Primary evidence**：[论文](https://arxiv.org/abs/1907.11180)明确给出 three full-game scenarios、Academy 和 IMPALA/PPO/Ape-X baselines。

### Honor of Kings Arena [B]

- **年份 / 状态**：2022，NeurIPS 2022。
- **任务 / Task**：开放的 Honor of Kings 1v1 competitive RL environment，提供 20 个 target heroes，专门测试跨英雄与跨 opponent generalization。
- **指标 / Metrics**：对固定/未见 opponent 与 hero combinations 的 win rate、episode reward；泛化结果必须分 seen/unseen target/opponent 报告。
- **代码 / Code**：[tencent-ailab/hok_env](https://github.com/tencent-ailab/hok_env)；[官方文档](https://aiarena.tencent.com/hok/doc/)。
- **一手证据 / Primary evidence**：[论文](https://arxiv.org/abs/2209.08483)摘要明确标注 NeurIPS 2022、20 heroes、competitive generalization 和开放 Python interface。

## 5. 关键 agent / 方法论文（不是 benchmark）

下表中的工作很重要，但均应放在 **Papers / Agents**，不能计入“可下载 benchmark 数量”。“主要评测”只说明论文在哪些游戏上证明方法，不代表这些论文创建了新环境。

| 年份 | 论文 / Paper | 状态 | 主要游戏与指标 / Games & metrics | 代码与一手证据 / Code & primary evidence |
|---:|---|---|---|---|
| 2015 | *Human-level control through deep reinforcement learning* (DQN) | Nature | ALE Atari；raw score / human-normalized score | [Nature](https://www.nature.com/articles/nature14236)；未发布官方完整训练代码 |
| 2016 | *Mastering the game of Go with deep neural networks and tree search* (AlphaGo) | Nature | Go；对职业棋手胜率与对局结果 | [Nature](https://www.nature.com/articles/nature16961)；agent paper，不是 Go benchmark |
| 2018 | *A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play* (AlphaZero) | Science | chess/shogi/Go；match win/draw/loss 与 Elo-like strength | [Science](https://www.science.org/doi/10.1126/science.aar6404)；无官方训练实现 |
| 2020 | *Mastering Atari, Go, chess and shogi by planning with a learned model* (MuZero) | Nature | 57 Atari games + board games；human-normalized Atari score / match strength | [Nature](https://www.nature.com/articles/s41586-020-03051-4)；无官方训练实现 |
| 2021 | *Agent57: Outperforming the Atari Human Benchmark* / Nature title *First return, then explore* | Nature | 57 Atari games；逐游戏 human-normalized performance | [Nature](https://www.nature.com/articles/s41586-020-03157-9)；论文提出 agent，不发布新 suite |
| 2019 | *Grandmaster level in StarCraft II using multi-agent reinforcement learning* (AlphaStar) | Nature | StarCraft II ladder；race-conditioned league/MMR 与 grandmaster-level evaluation | [Nature](https://www.nature.com/articles/s41586-019-1724-z)；环境接口另见 PySC2 |
| 2019 | *Dota 2 with Large Scale Deep Reinforcement Learning* (OpenAI Five) | arXiv technical report | Dota 2；与职业队/世界冠军系列赛胜负 | [论文](https://arxiv.org/abs/1912.06680)；没有发布可复用 Dota benchmark |
| 2019 | *Human-level performance in first-person multiplayer games with population-based deep reinforcement learning* | Science | Quake III Arena Capture the Flag；tournament win rate、human teammate/opponent evaluation | [论文预印本](https://arxiv.org/abs/1807.01281)；无完整公开训练环境包 |
| 2021 | *Open-Ended Learning Leads to Generally Capable Agents* (XLand) | arXiv technical report | 大规模程序生成多人游戏；held-out tasks 与人类归一表现 | [论文](https://arxiv.org/abs/2107.12808)、[DeepMind 项目说明](https://deepmind.google/blog/generally-capable-agents-emerge-from-open-ended-play/)；研究系统未作为公共 benchmark 发布 |
| 2022 | *A Generalist Agent* (Gato) | arXiv technical report | Atari、模拟控制、对话等多域；逐域原生指标 | [论文](https://arxiv.org/abs/2205.06175)；多域 agent，不是统一 game benchmark |
| 2022 | *Video PreTraining (VPT): Learning to Act by Watching Unlabeled Online Videos* | technical report | Minecraft 原生键鼠 20 Hz；zero-shot tasks、crafting success | [论文](https://arxiv.org/abs/2206.11795)、[官方代码/weights](https://github.com/openai/Video-Pre-Training) |
| 2023 | *Voyager: An Open-Ended Embodied Agent with Large Language Models* | arXiv technical report | Minecraft lifelong exploration；unique items、distance、tech-tree milestone speed | [论文](https://arxiv.org/abs/2305.16291)、[代码](https://github.com/MineDojo/Voyager) |
| 2023 | *STEVE-1: A Generative Model for Text-to-Behavior in Minecraft* | arXiv technical report | Minecraft raw pixels + keyboard/mouse；13 early-game instruction tasks 的 success | [论文](https://arxiv.org/abs/2306.00937)、[代码](https://github.com/Shalev-Lifshitz/STEVE-1) |
| 2023 | *JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal Language Models* | arXiv technical report | Minecraft 200+ tasks；short/long-horizon success，ObtainDiamondPickaxe reliability | [论文](https://arxiv.org/abs/2311.05997)、[代码](https://github.com/CraftJarvis/JARVIS-1) |
| 2023 | *Ghost in the Minecraft* (GITM) | arXiv technical report | Minecraft tech tree/ObtainDiamond；success rate 与 items obtained | [论文](https://arxiv.org/abs/2305.17144)、[代码](https://github.com/OpenGVLab/GITM) |
| 2024 | *Scaling Instructable Agents Across Many Simulated Worlds* (SIMA 1) | arXiv technical report | 多个研究世界与商业 3D 游戏；image + language → keyboard/mouse，instruction success | [论文](https://arxiv.org/abs/2404.10179)；未发布可复用 benchmark/code，商业游戏结果不可等同开放 suite |
| 2025 | *SIMA 2: A Generalist Embodied Agent for Virtual Worlds* | arXiv technical report | 多个 3D virtual worlds；复杂指令、unseen-world generalization、与人类差距 | [论文](https://arxiv.org/abs/2512.04797)；截至核验日未发布公共评测包 |
| 2025 | *Mastering diverse control tasks through world models* (DreamerV3) | Nature | Atari、Crafter 等多域；各环境原生 score，Crafter achievement score | [Nature](https://www.nature.com/articles/s41586-025-08744-2)、[官方代码](https://github.com/danijar/dreamerv3) |

## 6. 推荐的仓库数据字段 / Recommended schema

每个 README 条目至少保留下列字段，才能避免“看似齐全、实则不可复现”：

```yaml
title: exact paper or benchmark title
year: 2025
venue_or_status: ICLR 2025 | arXiv preprint | technical report
kind: benchmark | environment | platform | agent-paper
games_or_environments: []
observation_and_action: pixels/text/state -> controller/API actions
task: bilingual one-line task definition
metrics: []
evaluation_protocol: seeds, budget, train/test split, opponents, aggregation
paper: primary URL
project_or_code: official URL or null
data: official URL or null
license_or_access_note: ROM/game/client/account requirements
last_verified: 2026-08-29
```

## 7. 评测与维护注意事项

1. **环境分数不可跨协议直接比较**：ALE 的 sticky actions、Procgen 的 train/test levels、SMACv2 的 held-out scenario、Minecraft 的版本和交互预算都会显著改变结果。
2. **跨任务聚合不能只给 arithmetic mean**：建议同时提供逐任务结果、median、IQM/置信区间和失败率；Crafter 则遵守其官方 geometric-mean score。
3. **商业游戏可访问性要单列**：VideoGameBench、StarCraft II、Honor of Kings、Minecraft 等可能需要用户合法持有游戏、下载 client/ROM、接受特定 EULA 或使用指定版本。
4. **公开代码不等于公开 benchmark**：AlphaStar、OpenAI Five、SIMA、XLand 等是重要研究成果，但没有公开完整训练/评测资产时只能列为 agent paper。
5. **旧仓库状态要写清楚**：Malmo、原 Google Research Football、旧 Facebook NLE/MiniHack 等存在 archived/moved 情况；README 应链接当前维护位置，并固定 commit/version 用于复现。
