# Game-specific interactive world / video generation — verified primary sources

> **Cutoff / 检索截止：2026-08-29 (Asia/Shanghai).** This note is deliberately about **generating a playable game world or its action-conditioned observations/states**, not about an agent learning to win a game. Every included item is backed by a paper, author project page, or official code/model/data release. / 本文只收录“生成可交互游戏世界、游戏画面或显式游戏状态”的工作，不收录以提高游戏通关率或 RL 分数为核心的 game-playing agent。

## Scope and labels / 范围与标签

An item is in scope when its central output is an autoregressive game/world rollout (pixels, latents, geometry, or explicit game state) that changes in response to player controls. Both prompt-to-new-world systems and learned simulators of an existing game qualify; the latter are marked so readers do not mistake “simulating Doom/Minecraft” for “authoring a wholly new game.”

- **Open** — official core training and inference code, runnable weights, and meaningful data/evaluation artifacts are available.
- **Partial** — some official artifacts are usable, but a material component (training code/data, paper checkpoint, strongest model, or evaluator) is missing.
- **Closed** — the official release is paper/project/demo only; no runnable author checkpoint and core implementation are available.
- These labels describe artifact availability, **not** whether a work has a standard leaderboard or whether its data licensing permits commercial use.

The 18 selected entries below are ordered chronologically within three groups. Matrix-Game and Hunyuan-GameCraft are grouped as series to expose their version progression without counting minor versions as unrelated projects.

## A. Foundational generative game engines / 基础生成式游戏引擎

### 1. Genie — Generative Interactive Environments

- **Year / venue / status:** 2024, ICML 2024, peer-reviewed conference paper.
- **EN:** Learns an eight-way latent controller from unlabelled Internet platformer videos and turns a single image, sketch, photograph, or generated picture into an autoregressive playable 2D world.
- **中文：** 从无动作标注的互联网平台游戏视频中学习 8 类隐动作，把单张图片、手绘草图、照片或生成图变成可逐帧操控的 2D 可玩世界。
- **Generates / action conditioning:** next-frame video tokens for platformer-like worlds; inference is conditioned on the prompt frame, prior generated tokens, and a user-selected discrete latent action rather than named keyboard labels.
- **Evaluation:** FVD for video fidelity; `ΔPSNR` for how strongly changing the latent action changes the rollout; scaling studies and qualitative out-of-distribution prompt tests. Agent imitation is only a downstream demonstration, not the paper's primary objective.
- **Official artifacts:** [PMLR paper](https://proceedings.mlr.press/v235/bruce24a.html), [arXiv](https://arxiv.org/abs/2402.15391), [author project page](https://sites.google.com/view/genie-2024/home).
- **Openness:** **Closed.** DeepMind released the paper and demonstrations, but not the platformer dataset, weights, training code, or inference implementation.

### 2. GameNGen — Diffusion Models Are Real-Time Game Engines

- **Year / venue / status:** 2024, arXiv preprint / research project; no archival venue stated on the paper.
- **EN:** Replaces Doom's renderer and transition loop with an action-conditioned diffusion model that produces playable frames at about 20 FPS over multi-minute autoregressive sessions.
- **中文：** 用动作条件扩散模型替代 Doom 的渲染与状态转移循环，以约 20 FPS 自回归生成可持续数分钟交互的游戏画面。
- **Generates / action conditioning:** 320×240-padded Doom frames from 64 past generated frames plus the corresponding discrete key/action history; trajectories used for training are collected by a separate RL agent.
- **Evaluation:** teacher-forced PSNR/LPIPS, autoregressive PSNR/LPIPS decay, 16/32-frame FVD, sampling speed, and a blinded real-Doom-versus-simulation human study.
- **Official artifacts:** [paper](https://arxiv.org/abs/2408.14837), [author project page](https://gamengen.github.io/), [official project-page source repository](https://github.com/GameNGen/GameNGen.github.io).
- **Openness:** **Closed.** The website repository contains presentation assets, not the model, dataset, training/inference code, or weights. This is an existing-game neural simulator, not a system for designing a new game's rules.

### 3. Oasis — A Universe in a Transformer

- **Year / venue / status:** 2024, Decart × Etched official technical release; no peer-reviewed paper was published with the release.
- **EN:** Autoregressively generates a Minecraft-like world from a prompt frame while responding to keyboard input, with a public 500M-parameter inference model.
- **中文：** 从提示帧出发，根据键盘输入持续生成类似 Minecraft 的可交互世界，并公开了 5 亿参数推理模型。
- **Generates / action conditioning:** action-conditioned gameplay frames from the initial image and discrete keyboard controls; the public model is a smaller version of the hosted system.
- **Evaluation:** the official release emphasizes live interaction and qualitative rollouts; it does not define a fixed test suite or reproducible paper leaderboard.
- **Official artifacts:** [official project/technical page](https://oasis-model.github.io/), [official inference code](https://github.com/etched-ai/open-oasis), [official 500M weights](https://huggingface.co/Etched/oasis-500m).
- **Openness:** **Partial.** The 500M weights and inference code are runnable, but the strongest hosted model, training code/data, and a standard evaluator are not public.

### 4. GameGen-X — Interactive Open-world Game Video Generation

- **Year / venue / status:** 2025, ICLR 2025, peer-reviewed conference paper.
- **EN:** Combines open-domain text-to-game-video synthesis with instruction/action-conditioned continuation for diverse open-world game scenes.
- **中文：** 同时支持开放域文本生成游戏视频，以及依据指令/动作继续生成可交互的开放世界游戏片段。
- **Generates / action conditioning:** text-to-video game clips and continuation from a context clip; InstructNet conditions continuation on structured game instructions/events rather than a universal low-level keyboard schema.
- **Evaluation:** FID, FVD, text-video alignment, user preference, motion smoothness, dynamic degree, subject consistency, imaging quality, plus OGameEval-Gen/OGameEval-Ins and human/control-success evaluation.
- **Official artifacts:** [OpenReview paper](https://openreview.net/forum?id=8VG8tpPZhe), [arXiv](https://arxiv.org/abs/2411.00769), [project page](https://gamegen-x.github.io/), [official repository and OGameData metadata](https://github.com/GameGen-X/GameGen-X).
- **Openness:** **Partial.** The repository releases OGameData URL/timestamp/caption metadata (including the 860K generation subset), but contains no GameGen-X model code or weights; the 140K internally recorded instruction subset is not redistributed.

### 5. GameFactory — Creating New Games with Generative Interactive Videos

- **Year / venue / status:** 2025, ICCV 2025 Highlight, peer-reviewed conference paper.
- **EN:** Decouples Minecraft style from keyboard/mouse control so an open-domain video prior can transfer learned controls into visually new game scenes.
- **中文：** 将 Minecraft 画风与键鼠控制解耦，使开放域视频生成先验能把学到的控制迁移到全新视觉风格的游戏场景。
- **Generates / action conditioning:** first-person open-domain interactive video, autoregressively extended from a scene image; conditions include W/S/A/D, jump/sneak/sprint and continuous pitch/yaw mouse motion.
- **Evaluation:** camera-pose error (`Cam`), optical-flow error, CLIP similarity, FID/FVD, a domain-classification score, qualitative rare-action combinations, and autoregressive rollouts.
- **Official artifacts:** [paper](https://arxiv.org/abs/2501.08325), [author project page](https://yujiwen.github.io/gamefactory/), [official repository](https://github.com/KlingAIResearch/GameFactory), [official GF-Minecraft dataset](https://huggingface.co/datasets/KwaiVGI/GameFactory-Dataset).
- **Openness:** **Partial.** Roughly 70 hours of GF-Minecraft video/action data and small data utilities are public, but the repository does not release GameFactory training/inference code or model weights.

### 6. MineWorld — a Real-Time and Open-Source Interactive World Model on Minecraft

- **Year / venue / status:** 2025, arXiv technical report.
- **EN:** Uses interleaved visual and action tokens plus parallel diagonal decoding to generate controllable Minecraft observations at 4–7 FPS.
- **中文：** 以交错的视觉/动作 token 和并行对角解码，在 4–7 FPS 下生成可操控的 Minecraft 后续画面。
- **Generates / action conditioning:** Minecraft frames from prior visual tokens and an 11-token action vocabulary covering movement, camera, and game controls.
- **Evaluation:** FVD/visual metrics, inverse-dynamics discrete-action classification, camera-movement error, and decoding throughput; official scripts aggregate the paper metrics.
- **Official artifacts:** [paper](https://arxiv.org/abs/2504.08388), [official code/evaluation repository](https://github.com/microsoft/mineworld), [official model location referenced by the authors](https://huggingface.co/microsoft/mineworld).
- **Openness:** **Partial.** Inference, demo, diagonal decoding and metric code are public, but the official README says the checkpoints were taken down and the linked model repository remained unavailable at the cutoff; training data/code are also absent.

### 7. Matrix-Game series

- **Titles / years / status:** [Matrix-Game: Interactive World Foundation Model](https://arxiv.org/abs/2506.18701) (2025, arXiv); [Matrix-Game 2.0: An Open-Source Real-Time and Streaming Interactive World Model](https://arxiv.org/abs/2508.13009) (2025, arXiv); [Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory](https://arxiv.org/abs/2604.08995) (2026, arXiv).
- **EN:** Progresses from a Minecraft action-conditioned generator and GameWorld Score to real-time streaming across game scenes, then to memory-augmented 720p long-horizon generation.
- **中文：** 从 Minecraft 动作条件生成与 GameWorld Score，演进到多游戏场景实时流式生成，再到带长期记忆的 720p 长时交互生成。
- **Generates / action conditioning:** image-to-interactive-video from discrete keyboard states and continuous mouse/camera motion; 2.0 adds universal/GTA/Temple Run checkpoints, while 3.0 uses camera-aware retrieval and publishes 5B Unreal-scene models.
- **Evaluation:** GameWorld Score (image/aesthetic quality, temporal/motion quality, keyboard/mouse accuracy, object/scenario consistency), human preferences, long-rollout revisitation/memory tests, PSNR/SSIM for VAE reconstruction, and reported throughput (up to about 40 FPS for the 3.0 setup).
- **Official artifacts:** [unified official repository](https://github.com/SkyworkAI/Matrix-Game), [1.0 models](https://huggingface.co/Skywork/Matrix-Game), [2.0 models](https://huggingface.co/Skywork/Matrix-Game-2.0), [3.0 models](https://huggingface.co/Skywork/Matrix-Game-3.0), [1.0 project](https://matrix-game-homepage.github.io/), [2.0 project](https://matrix-game-v2.github.io/), [3.0 project](https://matrix-game-v3.github.io/).
- **Openness:** **Partial.** All three versions provide official inference code and selected weights. Training pipelines/data are not fully released; 3.0 explicitly withholds the mixed Unreal/real model and 28B MoE model at the cutoff.

### 8. Hunyuan-GameCraft series

- **Titles / years / status:** [Hunyuan-GameCraft: High-dynamic Interactive Game Video Generation with Hybrid History Condition](https://arxiv.org/abs/2506.17201) (2025, arXiv); [Hunyuan-GameCraft-2: Instruction-following Interactive Game World Model](https://arxiv.org/abs/2511.23429) (2025/2026 revision, technical report).
- **EN:** GameCraft maps keyboard/mouse input into camera trajectories for long game-video rollouts; GameCraft-2 adds natural-language interaction such as opening doors, drawing items, or triggering explosions.
- **中文：** 一代把键鼠输入映射为相机轨迹来生成长游戏视频；二代进一步支持“开门、取出火把、触发爆炸”等自然语言交互。
- **Generates / action conditioning:** high-dynamic multi-game video from a reference image, text prompt and camera/keyboard/mouse signals; 2.0 additionally accepts free-form mid-rollout interaction instructions and multi-turn control.
- **Evaluation:** GameCraft reports FVD, VBench-style quality/dynamics/consistency, translational/rotational RPE, FPS and a 30-person study. GameCraft-2 adds InterBench's trigger, prompt alignment, fluency, scope, end-state consistency and object-physics scores.
- **Official artifacts:** [GameCraft project](https://hunyuan-gamecraft.github.io/), [GameCraft code](https://github.com/Tencent-Hunyuan/Hunyuan-GameCraft-1.0), [GameCraft weights](https://huggingface.co/tencent/Hunyuan-GameCraft-1.0), [GameCraft-2 project](https://hunyuan-gamecraft-2.github.io/), [official hosted GameCraft-2 demo](https://hunyuan.tencent.com/game/game-craft).
- **Openness:** **Partial (1.0) / Closed (2.0).** The first release includes inference, distilled/full checkpoints and Gradio, but not its million-recording training corpus or full trainer. The second exposes a paper/project/hosted demo but no official training or inference repository and no downloadable checkpoint.

## B. Long-horizon, multiplayer, mechanics and NPC generation / 长时、多玩家、机制与 NPC 生成

### 9. Solaris — Building a Multiplayer Video World Model in Minecraft

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Generates synchronized Minecraft observations for two players, making movement, building and shared-world consistency evaluable from multiple viewpoints.
- **中文：** 为两名玩家同步生成 Minecraft 观察画面，使移动、建造、记忆与共享世界的多视角一致性可以被直接评测。
- **Generates / action conditioning:** two coordinated, action-conditioned first-person streams from paired initial observations and each player's controls; the collection engine records synchronized video/actions.
- **Evaluation:** held-out Movement, Grounding, Memory, Building and cross-view Consistency episodes, FID, and an officially released VLM-as-judge self-consistency metric.
- **Official artifacts:** [paper](https://arxiv.org/abs/2602.22208), [project page](https://solaris-wm.github.io/), [training/inference/evaluation code](https://github.com/solaris-wm/solaris), [multiplayer collection engine](https://github.com/solaris-wm/solaris-engine), [official model/data collections](https://huggingface.co/collections/nyu-visionx/solaris-models).
- **Openness:** **Open.** The authors release the four-stage trainer, GPU/TPU inference, weights, multiplayer training/evaluation data and VLM metric; full pretraining additionally depends on OpenAI's separately distributed VPT data.

### 10. WorldCam — Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Grounds immediate game controls and long-term revisitation in a shared 6-DoF camera-pose representation to reduce geometric drift.
- **中文：** 用统一的 6-DoF 相机位姿同时约束即时操作与长期重访，降低交互游戏世界中的几何漂移。
- **Generates / action conditioning:** autoregressive first-person gaming video from an initial frame; physics-based keyboard/mouse controls are integrated into global camera poses and used to retrieve relevant past observations.
- **Evaluation:** translation/rotation RPE, VBench++ visual/temporal metrics, PSNR/LPIPS/MEt3R/DINO similarity/sharpness for 3D revisitation, 200-frame tests, speed and a blinded 30-person study.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.16871), [project page](https://cvlab-kaist.github.io/WorldCam/), [official inference code](https://github.com/cvlab-kaist/WorldCam), [official weights](https://huggingface.co/worldcam/worldcam), [released open-game recordings](https://huggingface.co/datasets/worldcam/worldcam-dataset).
- **Openness:** **Partial.** A CS:GO-tuned checkpoint and inference are public. The released Xonotic/Unvanquished recordings are explicitly not the paper training set and omit extracted poses/captions; training code is not released.

### 11. ReactiveGWM — Steering NPC in Reactive Game World Models

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Generates Street Fighter rollouts in which player controls and high-level NPC strategies are separately conditioned, enabling prompt-steerable opponent reactions.
- **中文：** 分离玩家控制与 NPC 高层策略条件，生成可用“进攻、控制、防守”等提示操控对手反应的 Street Fighter 对战过程。
- **Generates / action conditioning:** Street Fighter II / Alpha 3 video; low-level player movement/attack signals enter as action bias, while NPC strategy prompts enter through cross-attention and can transfer to another game's vanilla world model.
- **Evaluation:** player Move/Attack accuracy, Gemini and Qwen NPC-instruction accuracy, SSIM/LPIPS, zero-shot strategy transfer, and a 19-person action/strategy study.
- **Official artifacts:** [paper](https://arxiv.org/abs/2605.15256), [project page](https://inv-wzq.github.io/ReactiveGWM/), [official training/inference code](https://github.com/INV-WZQ/ReactiveGWM), [official models](https://huggingface.co/INV-WZQ/ReactiveGWM-Models), [official datasets](https://huggingface.co/datasets/INV-WZQ/ReactiveGWM-Datasets).
- **Openness:** **Open.** Bidirectional and three-stage causal training, inference, SF2/SF3/transfer checkpoints, examples and strategy-aligned data are public.

### 12. SCOPE — Simulating Cross-game Operations in Playable Environments for FPS World Models

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Learns spatially selective responses to dense, simultaneous FPS controls across seven games, separating local weapon effects from global movement and camera motion.
- **中文：** 在 7 款 FPS 上学习逐帧、可重叠的密集操作响应，把局部武器效果与全局移动/视角变化解耦。
- **Generates / action conditioning:** 480×832, 81-frame first-person clips from an initial image, prompt and frame-aligned 10-DoF gamepad telemetry (movement/look sticks plus fire, aim, jump, reload, switch and melee buttons).
- **Evaluation:** CrossFPS's 1,378-clip test set; Dynamic Degree and Flow Score, photometric smoothness and depth accuracy, JEPA/FVD/LPIPS visual scores, multi-action composition, scaling and zero-shot scene generalization.
- **Official artifacts:** [paper](https://arxiv.org/abs/2605.23345), [project page](https://z2tong.github.io/SCOPE/), [official inference code](https://github.com/z2tong/SCOPE), [official weights](https://huggingface.co/zizhaotong/SCOPE), [CrossFPS collection](https://huggingface.co/collections/zizhaotong/crossfps).
- **Openness:** **Partial.** The checkpoint, packaged dependencies, inference examples and CrossFPS data are released under an official repository, but no training code is provided.

### 13. StatePlay — State-Aware Game World Models for Mechanics-Consistent Generation

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Jointly predicts video and explicit timers, health and skill meters so generated fighting-game outcomes obey mechanics rather than merely looking plausible.
- **中文：** 联合预测画面与计时、血量、能量槽等显式状态，使生成的格斗游戏结果遵守机制，而不只是视觉上像游戏。
- **Generates / action conditioning:** Street Fighter III video plus five synchronized state variables; player movement/attack actions, prompt, initial frame and predicted state branch condition a mixture-of-transformers visual branch.
- **Evaluation:** SSIM/LPIPS, Move/Attack accuracy, normalized state distance/alignment, and Gemini/GPT visual-judge mechanics fidelity on 100 held-out clips; the paper reports average normalized state error below 0.06 and an 18.6-point mechanics-fidelity gain over visual-only modeling.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.26754), [project page](https://jimntu.github.io/stateplay_page/), [official training/inference code](https://github.com/Jimntu/StatePlay), [official model](https://huggingface.co/onepiece1999/StatePlay), [official dataset](https://huggingface.co/datasets/onepiece1999/StatePlay-Dataset).
- **Openness:** **Open.** The model, 10K-clip state/action dataset, trainer, inference pipeline and examples are public; its VLM-judge protocol still depends on external proprietary judge versions.

### 14. ForgeWM — Progressive Causal Training for Few-Step Action-Conditioned Video World Models

- **Year / venue / status:** 2026, arXiv technical report.
- **EN:** Provides a fully released four-stage recipe that turns a game-conditioned video generator into 1-, 2- and 4-step real-time Minecraft/FPS world models.
- **中文：** 完整公开四阶段训练流程，把游戏动作条件视频模型蒸馏为 1、2、4 步的实时 Minecraft/FPS 世界模型。
- **Generates / action conditioning:** causal Minecraft video from an image plus keyboard/mouse streams, with a separately trained CrossFPS gamepad checkpoint; replay-time refinement improves a saved experienced trajectory instead of resampling it from scratch.
- **Evaluation:** VBench imaging/aesthetic/subject consistency, paired LPIPS and optical-flow profile, keyboard sign-control and mouse accuracy, latency/FPS, replay-to-reference/draft LPIPS, 41-person preference study and seven-game CrossFPS transfer.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.14022), [project page](https://asdfo123.github.io/ForgeWM/), [official full code](https://github.com/asdfo123/ForgeWM), [all stage/few-step models](https://huggingface.co/ForgeWM/ForgeWM), [pre-encoded training data](https://huggingface.co/datasets/ForgeWM/ForgeWM-data).
- **Openness:** **Open.** Training/inference, stage 0–3 checkpoints, 1/2/4-step students, CrossFPS checkpoint and roughly 89 GB of prepared data are public; upstream base-model/data licenses still apply.

### 15. WorldMind — Decoupled Game World Model for State-Aware NPC Behavior

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Separates state reconstruction, NPC planning, action translation and visual generation so boss behavior responds to the generated world's evolving state.
- **中文：** 将状态重建、NPC 决策、动作条件和画面生成分层，再闭环连接，使 Boss 行为随生成世界的状态变化而反应。
- **Generates / action conditioning:** approximately 20-FPS boss-fight video; player input and a state-aware NPC planner jointly feed temporally aligned action text into the visual generator, trained/evaluated with BOSS-140K internal-state annotations.
- **Evaluation:** boss-player distance/angle and binned state reconstruction, decision sensitivity/validity, pairwise preference, action validity and sequence tactical fit; the paper reports roughly 70% preference over its baselines for NPC behavior.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.21439), [project page](https://teawhite.cn/WorldMind/), [official release stub](https://github.com/TeaWhiteBro/WorldMind).
- **Openness:** **Closed.** The official repository says code and weights are still being prepared; BOSS-140K and the evaluator are not downloadable at the cutoff. It is included because the generated NPC reaction is the central world-model output, not a player agent's task score.

### 16. Marionette — Predicting World States, Rendering Geometry, Painting Appearance

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Predicts an explicit 276-D articulated multi-character state, renders geometry deterministically, then uses diffusion only to paint the game's appearance.
- **中文：** 先预测 276 维多角色关节世界状态，再用确定性渲染器生成几何控制，最后仅让扩散模型负责游戏外观。
- **Generates / action conditioning:** long-horizon articulated-character game rollouts; action IDs drive state dynamics, fixed forward kinematics/terrain collision/rasterization produce pose-control video, and a control-conditioned video model renders RGB.
- **Evaluation:** forced-action controllability via root-aligned joint error, character separation and ground penetration over long rollouts, rule-based state repair, and observation FVD; the abstract reports 66% less penetration after explicit terrain/separation rules.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.14530), [project page](https://alayalab.github.io/Marionette/), [official inference/runtime code](https://github.com/AlayaLab/Marionette), [official dynamics and observation weights](https://huggingface.co/AlayaLab/Marionette), [source WildWorld corpus](https://github.com/AlayaLab/WildWorld).
- **Openness:** **Partial.** The complete three-stage inference path, weights and two reproducibility seeds are available, but training code and the full 2,241-segment derived corpus are not; weights/assets are research-only.

## C. Generation-enabling datasets and field framing / 生成数据与领域框架

### 17. PhysEditWorld — A Large-Scale Dataset Toward Physics-Editable World Models

- **Year / venue / status:** 2026, arXiv preprint; dataset/resource paper rather than a complete game engine.
- **EN:** Replays identical UE5 actions and initial states under edited gravity to isolate whether a generated game world actually follows a requested physical rule.
- **中文：** 在 UE5 中固定初始状态与动作轨迹、只改变重力重放，从而检验生成游戏世界是否真正遵循指定物理规则。
- **Generates / action conditioning:** the release itself is paired multimodal supervision (RGB, depth, normals, audio, actions, camera, engine state and gravity), designed for gravity-conditioned video generation and action-conditioned first-person rollout models.
- **Evaluation:** proposed tasks cover gravity-conditioned video, action-conditioned world modeling and gravity-aware video-language understanding; the paper reports initial utility studies, but the fixed evaluator is not yet released.
- **Official artifacts:** [paper](https://arxiv.org/abs/2606.26694), [project page](https://yizhiqianbi.github.io/physeditworld/), [official release repository](https://github.com/yizhiqianbi/physeditworld), [official ModelScope dataset entry](https://www.modelscope.cn/datasets/GelerCAT/PhysicalWorld).
- **Openness:** **Partial.** Schema and demo subsets are public, but the official release table marks the full 100+ hour/60M-frame dataset, UE5 pipeline and evaluation scripts as planned and subject to asset-license review.

### 18. From Pixels to States — Rethinking Interactive World Models as Game Engines

- **Year / venue / status:** 2026, arXiv perspective/survey and data-engine paper; not a new generator.
- **EN:** Frames a generative game engine as an action–state–observation loop and audits the field across control, state dynamics, persistence and real-time generation.
- **中文：** 用“动作—状态—观察”闭环重新界定生成式游戏引擎，并从控制、状态动力学、持续性和实时性四方面梳理研究缺口。
- **Generates / action conditioning:** no model is proposed; its concrete resource is a Black Myth: Wukong collection engine producing 90+ hours of frame-aligned actions, ground-truth states, observations and semantic annotations.
- **Evaluation:** conceptual four-axis comparison rather than a leaderboard; useful for checking whether a paper generates only plausible pixels or also preserves rules and state.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.14076).
- **Openness:** **Closed.** No official repository, downloadable Wukong dataset, weights or evaluator was linked at the cutoff. Included as scope-defining reading, not as a model claim.

## Explicit exclusions and boundary decisions / 明确排除与边界判断

### Excluded because the core objective is playing, not generating

- **DIAMOND — Diffusion for World Modeling: Visual Details Matter in Atari** ([paper](https://arxiv.org/abs/2405.12399), [official code](https://github.com/eloialonso/diamond)): technically produces playable Atari/CS:GO observations and is highly reproducible, but its stated central contribution is an RL agent trained in a diffusion world model and its headline comparison is Atari-100k return. It therefore belongs in a game-playing/world-model-agent list, not this generation-only list.
- **SimPLe, IRIS, Dreamer / DreamerV2/V3 and related imagination-based RL:** their predictive models are means to improve sample efficiency or control return; the evaluated product is the policy, not an authored/playable generative game world.
- **GameWAM — A World Action Model for Video Games** ([paper](https://arxiv.org/abs/2608.26200)): jointly predicts future observations and executable keyboard/mouse trajectories, but is explicitly a closed-loop gameplay/GUI policy evaluated by task success. The action generator makes it a game agent boundary case, so it is excluded.
- **ActSWM and similar open-world planning models:** excluded when the core result is action selection or planning success rather than a human-controllable generated environment.

### Excluded because the domain is not specifically game generation

- **Driving:** GAIA-1, DriveDreamer/Drive-WM, Waymo World Model and related autonomous-driving simulators.
- **Robotics/embodiment:** UniSim, DreamGen, DreamDojo, Cosmos robot/physical-AI models and manipulation world models.
- **General interactive video/world models:** YUME, WorldPlay/HY-World, AlayaWorld, DreamX-World, LingBot-World, ReWorld, ActWorld and comparable systems may show game-like demos or train partly on gameplay, but their declared scope and principal evaluations span real/stylized/embodied scenes rather than specifically generating games. They should live in a broader interactive-world-model bibliography, not silently inflate this game-only list.
- **Genie 2 / Genie 3:** official DeepMind demos are relevant continuations, but as of the cutoff they are product/research announcements without a citable technical paper or reproducible artifacts. The peer-reviewed Genie paper above is the defensible paper entry.

## Comparison cautions / 横向比较注意事项

1. **New-game creation and learned simulation are different.** GameFactory/GameGen-X/Genie emphasize new visual worlds; GameNGen/MineWorld/Solaris reproduce the dynamics of an existing title. Both generate rather than play, but they should not share a single “best game creator” ranking.
2. **Pixel responsiveness is not game logic.** Keyboard/mouse accuracy can coexist with impossible health, cooldown or collision behavior; StatePlay, WorldMind, Marionette and PhysEditWorld specifically expose this gap.
3. **Most reported scores are not directly comparable.** Resolutions, rollout lengths, action vocabularies, initial frames, proprietary training games and judge models differ. GameWorld Score, InterBench, CrossFPS and each paper's private test split are separate protocols.
4. **Open inference is not open training.** Oasis, Matrix-Game, Hunyuan-GameCraft and WorldCam can be run from official checkpoints, yet their headline training corpus or complete trainer is unavailable.
5. **Game footage and assets carry rights constraints.** YouTube-ID datasets can link-rot; AAA footage, Doom/Atari/Minecraft assets, UE5 marketplace scenes and WildWorld-derived checkpoints may restrict redistribution or commercial use even when code is public.
