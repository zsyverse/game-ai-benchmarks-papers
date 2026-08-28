# 交互式游戏世界生成：论文与资源索引

[返回首页](../../README.zh-CN.md) · [English](../en/interactive-worlds.md) · [端到端生成](end-to-end.md) · [自动设计与 PCG](pcg.md) · [收录范围](../../SCOPE.md)

> 检索截止：**2026-08-29（Asia/Shanghai）**。本索引界定的是 **learned/pixel world generation（学习式/像素式世界生成）边界**：系统生成受动作控制的游戏观察、视频、几何或显式状态。它与产出源代码、引擎工程、关卡或可执行规则描述的 **code/rules game generation（代码/规则游戏生成）** 分开，也不收录主要结果是策略或分数的玩游戏研究。

这里同时收录“提示到新世界”的系统与“学习既有游戏”的模拟器，但会在条目中明确区分。**Open** 表示官方训练/推理代码、可运行权重及有意义的数据/评测工件均已公开；**Partial** 表示缺少关键组件；**Closed** 表示未核验到可运行的官方 checkpoint 与核心实现。

## 1. 基础生成式引擎（8 条）

| 年份 | 论文/资源 | 生成范围/动作条件 | 评测 | 工件/状态 |
| :---: | --- | --- | --- | --- |
| 2024 | [Genie — Generative Interactive Environments](https://proceedings.mlr.press/v235/bruce24a.html) | 从无标注的平台游戏视频中学习 8 类隐动作，并由单张图片、草图或照片生成可玩的 2D 世界；生成以提示帧、历史 token 和用户选择的隐动作为条件。 | FVD、动作影响 `ΔPSNR`、缩放实验及分布外提示测试。 | **Closed** — [arXiv](https://arxiv.org/abs/2402.15391)、[项目](https://sites.google.com/view/genie-2024/home)；未公开数据集、权重或实现。 |
| 2024 | [GameNGen — Diffusion Models Are Real-Time Game Engines](https://arxiv.org/abs/2408.14837) | 用动作条件扩散模型替代 Doom 的渲染与状态转移循环，根据前 64 帧和离散动作历史以约 20 FPS 生成画面；它模拟既有游戏，而非创作新规则。 | teacher-forced 与自回归 PSNR/LPIPS、16/32 帧 FVD、速度及真人盲测。 | **Closed** — [项目](https://gamengen.github.io/)、[项目页源码](https://github.com/GameNGen/GameNGen.github.io)；只有展示素材，没有模型、数据、代码或权重。 |
| 2024 | [Oasis — A Universe in a Transformer](https://oasis-model.github.io/) | 从初始帧和离散键盘控制自回归生成类似 Minecraft 的世界；公开的 5 亿参数模型小于线上系统。 | 实时交互与定性 rollout；没有固定测试集或可复现排行榜。 | **Partial** — [推理代码](https://github.com/etched-ai/open-oasis)、[5 亿参数权重](https://huggingface.co/Etched/oasis-500m)；最强模型、训练栈/数据及 evaluator 未公开。 |
| 2025 | [GameGen-X — Interactive Open-world Game Video Generation](https://openreview.net/forum?id=8VG8tpPZhe) | 支持开放域文生游戏视频，也能按结构化指令/事件续写上下文视频，而非采用统一的底层键盘动作格式。 | FID/FVD、文视频对齐、质量/动态/一致性指标、OGameEval-Gen/OGameEval-Ins、用户偏好及控制成功率。 | **Partial** — [arXiv](https://arxiv.org/abs/2411.00769)、[项目](https://gamegen-x.github.io/)、[仓库与 OGameData 元数据](https://github.com/GameGen-X/GameGen-X)；模型代码/权重和内部指令子集未公开。 |
| 2025 | [GameFactory — Creating New Games with Generative Interactive Videos](https://arxiv.org/abs/2501.08325) | 利用开放域视频先验，把源自 Minecraft 的 W/S/A/D、跳跃/潜行/冲刺及连续鼠标控制迁移到视觉全新的第一人称场景。 | 相机位姿与光流误差、CLIP 相似度、FID/FVD、域分类分数、稀有动作组合及自回归 rollout。 | **Partial** — [项目](https://yujiwen.github.io/gamefactory/)、[仓库](https://github.com/KlingAIResearch/GameFactory)、[GF-Minecraft 数据集](https://huggingface.co/datasets/KwaiVGI/GameFactory-Dataset)；数据/小工具已公开，模型代码与权重未公开。 |
| 2025 | [MineWorld — a Real-Time and Open-Source Interactive World Model on Minecraft](https://arxiv.org/abs/2504.08388) | 交错建模视觉 token 与 11 类移动/相机/游戏控制 token，并以并行对角解码在 4–7 FPS 生成 Minecraft 观察。 | FVD/视觉指标、逆动力学动作分类、相机运动误差及解码吞吐。 | **Partial** — [代码与评测](https://github.com/microsoft/mineworld)、[模型位置](https://huggingface.co/microsoft/mineworld)；推理/指标代码仍公开，但 checkpoint 已下架，训练代码/数据也未发布。 |
| 2025–2026 | [Matrix-Game 1.0](https://arxiv.org/abs/2506.18701) / [2.0](https://arxiv.org/abs/2508.13009) / [3.0](https://arxiv.org/abs/2604.08995) | 从 Minecraft 生成演进到多游戏实时流式生成及 720p 长期记忆，以键盘状态和连续鼠标/相机运动为条件。 | GameWorld Score、用户偏好、重访/记忆测试、VAE PSNR/SSIM，以及 3.0 设置中最高约 40 FPS 的吞吐。 | **Partial** — [代码](https://github.com/SkyworkAI/Matrix-Game)、[1.0 模型](https://huggingface.co/Skywork/Matrix-Game)、[2.0 模型](https://huggingface.co/Skywork/Matrix-Game-2.0)、[3.0 模型](https://huggingface.co/Skywork/Matrix-Game-3.0)、[1.0 项目](https://matrix-game-homepage.github.io/)、[2.0 项目](https://matrix-game-v2.github.io/)、[3.0 项目](https://matrix-game-v3.github.io/)；推理与部分权重公开，完整训练/数据和 3.0 最强模型未公开。 |
| 2025–2026 | [Hunyuan-GameCraft 1.0](https://arxiv.org/abs/2506.17201) / [GameCraft-2](https://arxiv.org/abs/2511.23429) | 由参考图、文本及键鼠/相机信号生成高动态多游戏视频；2.0 新增“开门、触发爆炸”等自由形式、多轮指令。 | FVD、VBench 风格质量/动态/一致性、相机 RPE、速度和用户研究；2.0 另含 InterBench 的指令、流畅性、终态及物理分数。 | **Partial（1.0）/ Closed（2.0）** — [1.0 项目](https://hunyuan-gamecraft.github.io/)、[1.0 代码](https://github.com/Tencent-Hunyuan/Hunyuan-GameCraft-1.0)、[1.0 权重](https://huggingface.co/tencent/Hunyuan-GameCraft-1.0)、[2.0 项目](https://hunyuan-gamecraft-2.github.io/)、[2.0 在线 demo](https://hunyuan.tencent.com/game/game-craft)；1.0 缺完整训练/数据，2.0 没有可下载代码或 checkpoint。 |

## 2. 长时、多玩家、机制与 NPC 生成（8 条）

| 年份 | 论文/资源 | 生成范围/动作条件 | 评测 | 工件/状态 |
| :---: | --- | --- | --- | --- |
| 2026 | [Solaris — Building a Multiplayer Video World Model in Minecraft](https://arxiv.org/abs/2602.22208) | 根据成对初始观察和两名玩家各自的控制生成同步 Minecraft 第一人称流，显式暴露共享世界的移动、建造、记忆和跨视角一致性。 | 留出的 Movement、Grounding、Memory、Building、Consistency episode，FID 及已发布的 VLM 自一致性指标。 | **Open** — [项目](https://solaris-wm.github.io/)、[训练/推理/评测](https://github.com/solaris-wm/solaris)、[采集引擎](https://github.com/solaris-wm/solaris-engine)、[模型与数据](https://huggingface.co/collections/nyu-visionx/solaris-models)；完整预训练还依赖单独分发的 VPT 数据。 |
| 2026 | [WorldCam — Interactive Autoregressive 3D Gaming Worlds](https://arxiv.org/abs/2603.16871) | 用统一 6-DoF 相机位姿表示物理键鼠控制并检索历史视图，降低长期重访时的几何漂移。 | 平移/旋转 RPE、VBench++、PSNR/LPIPS/MEt3R/DINO、清晰度、200 帧测试、速度及盲测用户研究。 | **Partial** — [项目](https://cvlab-kaist.github.io/WorldCam/)、[推理](https://github.com/cvlab-kaist/WorldCam)、[权重](https://huggingface.co/worldcam/worldcam)、[开放游戏录像](https://huggingface.co/datasets/worldcam/worldcam-dataset)；训练代码和论文训练数据未公开。 |
| 2026 | [ReactiveGWM — Steering NPC in Reactive Game World Models](https://arxiv.org/abs/2605.15256) | 分别用玩家底层动作和提示级 NPC 策略控制 Street Fighter rollout，实现可引导的对手反应与跨游戏迁移。 | 玩家 Move/Attack 准确率、Gemini/Qwen 指令准确率、SSIM/LPIPS、零样本迁移及 19 人用户研究。 | **Open** — [项目](https://inv-wzq.github.io/ReactiveGWM/)、[训练/推理](https://github.com/INV-WZQ/ReactiveGWM)、[模型](https://huggingface.co/INV-WZQ/ReactiveGWM-Models)、[数据集](https://huggingface.co/datasets/INV-WZQ/ReactiveGWM-Datasets)。 |
| 2026 | [SCOPE — Simulating Cross-game Operations in Playable Environments](https://arxiv.org/abs/2605.23345) | 根据图像、提示词和逐帧 10-DoF 手柄遥测，为 7 款 FPS 生成 480×832 片段，并分离局部武器效果与全局移动/视角运动。 | CrossFPS 的 1,378 个片段、动态/光流、平滑度/深度、JEPA/FVD/LPIPS、动作组合、缩放及零样本场景。 | **Partial** — [项目](https://z2tong.github.io/SCOPE/)、[推理](https://github.com/z2tong/SCOPE)、[权重](https://huggingface.co/zizhaotong/SCOPE)、[CrossFPS](https://huggingface.co/collections/zizhaotong/crossfps)；没有训练代码。 |
| 2026 | [StatePlay — State-Aware Game World Models for Mechanics-Consistent Generation](https://arxiv.org/abs/2607.26754) | 联合预测 Street Fighter 画面与血量、计时、能量槽等 5 个同步变量，并以玩家动作和预测状态控制视觉生成。 | SSIM/LPIPS、Move/Attack 准确率、归一化状态距离/对齐，以及 Gemini/GPT 机制保真判断。 | **Open** — [项目](https://jimntu.github.io/stateplay_page/)、[训练/推理](https://github.com/Jimntu/StatePlay)、[模型](https://huggingface.co/onepiece1999/StatePlay)、[数据集](https://huggingface.co/datasets/onepiece1999/StatePlay-Dataset)；VLM judge 仍依赖专有模型版本。 |
| 2026 | [ForgeWM — Progressive Causal Training for Few-Step Action-Conditioned Video World Models](https://arxiv.org/abs/2608.14022) | 公开四阶段流程，把图像与键鼠流条件模型蒸馏为 1、2、4 步实时 Minecraft/FPS 模型，并支持回放时轨迹细化。 | VBench、LPIPS/光流、键鼠准确率、延迟/FPS、回放保真、41 人研究及 7 款游戏 CrossFPS 迁移。 | **Open** — [项目](https://asdfo123.github.io/ForgeWM/)、[完整代码](https://github.com/asdfo123/ForgeWM)、[模型](https://huggingface.co/ForgeWM/ForgeWM)、[预处理数据](https://huggingface.co/datasets/ForgeWM/ForgeWM-data)；仍须遵守上游许可。 |
| 2026 | [WorldMind — Decoupled Game World Model for State-Aware NPC Behavior](https://arxiv.org/abs/2608.21439) | 闭环连接状态重建、NPC 决策、动作转换和约 20 FPS 的 Boss 战视频，使 NPC 行为响应不断变化的生成状态。 | 状态重建、决策敏感性/有效性、成对偏好、动作有效性及战术序列适配度。 | **Closed** — [项目](https://teawhite.cn/WorldMind/)、[发布占位仓库](https://github.com/TeaWhiteBro/WorldMind)；代码、权重、BOSS-140K 和 evaluator 均不可下载。 |
| 2026 | [Marionette — Predicting World States, Rendering Geometry, Painting Appearance](https://arxiv.org/abs/2608.14530) | 根据动作 ID 预测 276 维多角色关节状态，确定性渲染几何，再仅用扩散模型绘制长时 RGB 观察。 | 关节误差、角色分离、地面穿透、规则式状态修复及观察 FVD。 | **Partial** — [项目](https://alayalab.github.io/Marionette/)、[推理/运行时](https://github.com/AlayaLab/Marionette)、[权重](https://huggingface.co/AlayaLab/Marionette)、[WildWorld 源语料](https://github.com/AlayaLab/WildWorld)；训练代码与完整派生语料未公开。 |

## 3. 生成支撑数据集与领域框架（2 条）

| 年份 | 论文/资源 | 生成范围/动作条件 | 评测 | 工件/状态 |
| :---: | --- | --- | --- | --- |
| 2026 | [PhysEditWorld — A Large-Scale Dataset Toward Physics-Editable World Models](https://arxiv.org/abs/2606.26694) | 在 UE5 中以不同重力重放完全相同的初始状态与动作，提供配对 RGB/深度/法线/音频/动作/相机/状态监督，用于物理与动作条件生成。 | 提出重力条件视频、动作条件 rollout 和重力感知视频语言任务；尚无已发布的固定 evaluator。 | **Partial** — [项目](https://yizhiqianbi.github.io/physeditworld/)、[发布仓库](https://github.com/yizhiqianbi/physeditworld)、[ModelScope 数据集](https://www.modelscope.cn/datasets/GelerCAT/PhysicalWorld)；demo 子集/schema 已公开，完整数据、UE5 流水线和脚本仍待发布。 |
| 2026 | [From Pixels to States — Rethinking Interactive World Models as Game Engines](https://arxiv.org/abs/2607.14076) | 这是框架论文而非新生成器：形式化“动作—状态—观察”闭环，并介绍含对齐动作、状态、观察和语义的 90+ 小时《黑神话：悟空》采集引擎。 | 从控制、状态动力学、持续性和实时生成四轴分析领域，而非设置排行榜。 | **Closed** — 截至检索日没有关联官方仓库、可下载数据集、权重或 evaluator；作为边界定义材料收录。 |

## 明确排除的 playing/RL 工作

以下工作即使会用学习模型预测游戏观察，也不进入这份“只看生成”的索引：

- **DIAMOND — Diffusion for World Modeling: Visual Details Matter in Atari**（[论文](https://arxiv.org/abs/2405.12399)、[代码](https://github.com/eloialonso/diamond)）以训练和评测 RL agent 为中心，核心结果按 Atari-100k return 比较。
- **Dreamer / DreamerV2 / DreamerV3、IRIS 与 SimPLe** 主要用预测模型提升策略学习、样本效率或控制回报；被评测的产品是玩家策略。
- **GameWAM — A World Action Model for Video Games**（[论文](https://arxiv.org/abs/2608.26200)）虽同时预测观察与可执行控制，但核心贡献是按任务成功率评测的闭环 gameplay/GUI policy。
- **ActSWM 及类似规划模型**若主要结果是动作选择或规划成功，而非人类可控制的生成环境，同样排除。
