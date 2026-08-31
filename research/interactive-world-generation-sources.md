# Game-specific interactive world generation — verified primary sources

> **Cutoff / 检索截止：2026-08-31 (Asia/Shanghai).** This note covers systems and resources whose central purpose is **generating a game or its action-conditioned observations, geometry, or explicit state**. It excludes work whose primary evaluated product is a game-playing policy. / 本文只收录以“生成游戏、动作条件游戏画面、几何或显式状态”为核心的系统与资源，不收录主要评测对象是游戏策略的工作。

## Method and labels / 方法与标签

Claims were checked against primary sources: papers, author project pages, and official code/model/data releases. Submitted-date and last-updated-date arXiv searches for 2026-08-29 through 2026-08-31 found no additional paper family in scope. One artifact change did occur: Game2World's training, inference, evaluation, model, and datasets became publicly verifiable during that interval.

事实以论文、作者项目页及官方代码/模型/数据发布为准。针对 2026-08-29 至 2026-08-31 的 arXiv 首发日期与更新日期增量检索没有发现新的范围内论文族；该时段唯一需要补记的工件变化是 Game2World 的训练、推理、评测、模型及数据已可公开核验。

- **Open** — official core training and inference code, runnable weights, and meaningful data/evaluation artifacts are available.
- **Partial** — official artifacts are useful, but a material component such as training code/data, the paper checkpoint, strongest model, or evaluator is missing.
- **Closed** — no runnable official author checkpoint and core implementation were verified.
- **Paper-only by design** — a position/taxonomy paper intentionally proposes no generator; this is not a failed release.
- Labels describe availability, not commercial-use rights. Game footage, ROMs, engine assets, and upstream checkpoints may carry separate restrictions.

The 33 entries are partitioned as **23 core action-controlled generators + 5 generation-specific datasets/benchmarks + 5 framing or boundary systems**. Series are counted once. The partition prevents data papers and game-agent boundary cases from inflating the generator count.

## A. Core action-controlled generators / 核心动作控制生成器（23）

### 1. Promptable Game Models: Text-Guided Game Simulation via Masked Diffusion Models

- **Year / venue / status:** 2023 preprint; published in ACM Transactions on Graphics in 2024, DOI 10.1145/3635705.
- **EN:** Simulates Tennis and Minecraft video while accepting both atomic and compositional natural-language actions, predating the recent wave of neural game engines.
- **中文：** 以原子或组合式自然语言动作控制 Tennis 与 Minecraft 视频模拟，是近年神经游戏引擎浪潮之前的直接先驱。
- **Generates / action conditioning:** future gameplay frames from a context clip plus low-level or high-level text actions; it simulates existing game dynamics rather than creating executable rules.
- **Evaluation:** LPIPS, FID, and FVD for video; L2 and Fréchet distance for animation; datasets contain about 15.5 hours of Tennis and 1.21 hours of Minecraft.
- **Official artifacts:** [arXiv](https://arxiv.org/abs/2303.13472), [ACM DOI](https://doi.org/10.1145/3635705), [author project](https://snap-research.github.io/promptable-game-models/), [official repository](https://github.com/snap-research/promptable-game-models).
- **Openness:** **Closed.** The paper/project promise data, models, and a framework, but the official repository contains only an effectively empty README and no runnable release.

### 2. Genie — Generative Interactive Environments

- **Year / venue / status:** 2024, ICML 2024, peer-reviewed conference paper.
- **EN:** Learns an eight-way latent controller from unlabelled Internet platformer videos and turns one image, sketch, photograph, or generated picture into a playable 2D rollout.
- **中文：** 从无动作标注的互联网平台游戏视频中学习 8 类隐动作，把单张图片、草图、照片或生成图变成可逐帧操控的 2D 世界。
- **Generates / action conditioning:** next-frame video tokens conditioned on the prompt frame, generated history, and a user-selected discrete latent action rather than named keyboard labels.
- **Evaluation:** FVD, action-effect `ΔPSNR`, scaling studies, and qualitative out-of-distribution prompt tests. Agent imitation is downstream evidence, not the primary objective.
- **Official artifacts:** [PMLR paper](https://proceedings.mlr.press/v235/bruce24a.html), [arXiv](https://arxiv.org/abs/2402.15391), [author project](https://sites.google.com/view/genie-2024/home).
- **Openness:** **Closed.** DeepMind released the paper and demonstrations, but not the platformer dataset, weights, training code, or inference implementation.

### 3. GenieRedux — Exploration-Driven Generative Interactive Environments

- **Year / venue / status:** 2024 precursor and 2025 extended arXiv technical reports; no archival venue was verified.
- **EN:** Reproduces and extends the Genie recipe with AutoExplore, automatically collecting trajectories across many environments instead of relying on costly human play.
- **中文：** 用 AutoExplore 自动跨环境采集轨迹，开放复现并扩展 Genie 路线，减少对昂贵人工游玩的依赖。
- **Generates / action conditioning:** action-controlled CoinRun and RetroAct video rollouts; the extended release covers 974 environments and provides environment/data-generation tooling.
- **Evaluation:** `ΔPSNR`, FID, PSNR, SSIM, exploration coverage, rollout quality, and comparisons between random, trained-agent, and AutoExplore collection.
- **Official artifacts:** [precursor paper](https://arxiv.org/abs/2409.06445), [extended paper](https://arxiv.org/abs/2504.02515), [official training/inference/evaluation repository](https://github.com/insait-institute/GenieRedux), [official models](https://huggingface.co/INSAIT-Institute/GenieRedux).
- **Openness:** **Open.** Training, inference, evaluation, data generation, RetroAct metadata, and CoinRun/RetroAct checkpoints are public; legally obtained ROMs are still required separately.

### 4. GameNGen — Diffusion Models Are Real-Time Game Engines

- **Year / venue / status:** 2024, arXiv preprint/research project; no archival venue is stated in the paper.
- **EN:** Replaces Doom's renderer and transition loop with action-conditioned diffusion that produces playable frames at about 20 FPS over multi-minute autoregressive sessions.
- **中文：** 用动作条件扩散模型替代 Doom 的渲染与状态转移循环，以约 20 FPS 自回归生成可持续数分钟的交互画面。
- **Generates / action conditioning:** 320×240-padded Doom frames from 64 previous generated frames and their discrete key/action history; a separate RL agent collects trajectories but is not the evaluated product.
- **Evaluation:** teacher-forced/autoregressive PSNR and LPIPS, 16/32-frame FVD, sampling speed, and a blinded real-Doom-versus-simulation human study.
- **Official artifacts:** [paper](https://arxiv.org/abs/2408.14837), [author project](https://gamengen.github.io/), [official project-page source](https://github.com/GameNGen/GameNGen.github.io).
- **Openness:** **Closed.** The repository contains presentation assets, not model code, data, training/inference implementation, or weights.

### 5. Oasis — A Universe in a Transformer

- **Year / venue / status:** 2024, Decart × Etched official technical release; no peer-reviewed paper accompanied the release.
- **EN:** Autoregressively generates a Minecraft-like world from a prompt frame while responding to keyboard input, with a public 500M-parameter inference model.
- **中文：** 从提示帧出发，根据键盘输入持续生成类似 Minecraft 的世界，并公开了 5 亿参数推理模型。
- **Generates / action conditioning:** gameplay frames from the initial image, frame history, and discrete keyboard controls; the public model is smaller than the hosted system.
- **Evaluation:** official evidence is live interaction and qualitative rollouts; there is no fixed paper test suite or reproducible leaderboard.
- **Official artifacts:** [official technical page](https://oasis-model.github.io/), [official inference code](https://github.com/etched-ai/open-oasis), [official 500M weights](https://huggingface.co/Etched/oasis-500m).
- **Openness:** **Partial.** The 500M model and inference are runnable, but the strongest hosted model, training stack/data, and evaluator are not public.

### 6. GameFactory — Creating New Games with Generative Interactive Videos

- **Year / venue / status:** 2025, ICCV 2025 Highlight, peer-reviewed conference paper.
- **EN:** Decouples Minecraft visual style from keyboard/mouse control so an open-domain video prior can transfer those controls into visually new game scenes.
- **中文：** 将 Minecraft 画风与键鼠控制解耦，使开放域视频先验能把控制能力迁移到全新视觉风格的游戏场景。
- **Generates / action conditioning:** first-person open-domain interactive video from a scene image, W/S/A/D, jump/sneak/sprint, and continuous pitch/yaw mouse motion.
- **Evaluation:** camera-pose and optical-flow error, CLIP similarity, FID/FVD, domain classification, rare-action combinations, and autoregressive rollouts.
- **Official artifacts:** [paper](https://arxiv.org/abs/2501.08325), [author project](https://yujiwen.github.io/gamefactory/), [official repository](https://github.com/KlingAIResearch/GameFactory), [GF-Minecraft dataset](https://huggingface.co/datasets/KwaiVGI/GameFactory-Dataset).
- **Openness:** **Partial.** Roughly 70 hours of video/action data and small utilities are public, but model training/inference code and weights are not.

### 7. MineWorld — a Real-Time and Open-Source Interactive World Model on Minecraft

- **Year / venue / status:** 2025, arXiv technical report.
- **EN:** Uses interleaved visual/action tokens and parallel diagonal decoding to generate controllable Minecraft observations at 4–7 FPS.
- **中文：** 以交错的视觉/动作 token 和并行对角解码，在 4–7 FPS 下生成可操控的 Minecraft 后续画面。
- **Generates / action conditioning:** Minecraft frames from visual history and an 11-token vocabulary covering movement, camera, and game controls.
- **Evaluation:** FVD and visual metrics, inverse-dynamics discrete-action classification, camera-motion error, and decoding throughput; official scripts aggregate paper metrics.
- **Official artifacts:** [paper](https://arxiv.org/abs/2504.08388), [official code/evaluation](https://github.com/microsoft/mineworld), [official model location](https://huggingface.co/microsoft/mineworld).
- **Openness:** **Partial.** Inference, demo, decoding, and metric code remain public, but the README says checkpoints were removed; training code/data are absent.

### 8. Matrix-Game series

- **Year / venue / status:** 2025–2026, three arXiv technical reports.
- **EN:** Progresses from Minecraft action-conditioned generation and GameWorld Score to multi-game real-time streaming, then memory-augmented 720p long-horizon generation.
- **中文：** 从 Minecraft 动作条件生成与 GameWorld Score，演进到多游戏实时流式生成，再到带长期记忆的 720p 长时交互生成。
- **Generates / action conditioning:** image-to-interactive video from keyboard states and continuous mouse/camera motion; later versions add universal/GTA/Temple Run and Unreal-scene models plus camera-aware retrieval.
- **Evaluation:** GameWorld Score, human preferences, long-rollout revisitation/memory, VAE PSNR/SSIM, and throughput up to about 40 FPS in the 3.0 setup.
- **Official artifacts:** [1.0 paper](https://arxiv.org/abs/2506.18701), [2.0 paper](https://arxiv.org/abs/2508.13009), [3.0 paper](https://arxiv.org/abs/2604.08995), [unified repository](https://github.com/SkyworkAI/Matrix-Game), [1.0 models](https://huggingface.co/Skywork/Matrix-Game), [2.0 models](https://huggingface.co/Skywork/Matrix-Game-2.0), [3.0 models](https://huggingface.co/Skywork/Matrix-Game-3.0), [1.0 project](https://matrix-game-homepage.github.io/), [2.0 project](https://matrix-game-v2.github.io/), [3.0 project](https://matrix-game-v3.github.io/).
- **Openness:** **Partial.** Inference and selected weights exist for all versions, but full training/data are absent and the strongest mixed/28B 3.0 models remain withheld.

### 9. Hunyuan-GameCraft series

- **Year / venue / status:** 2025–2026, arXiv technical reports.
- **EN:** GameCraft maps keyboard/mouse input into camera-aware long game-video rollouts; GameCraft-2 adds mid-rollout natural-language interactions such as opening doors or triggering explosions.
- **中文：** 一代把键鼠输入映射到相机感知长视频生成；二代进一步支持“开门、触发爆炸”等运行中自然语言交互。
- **Generates / action conditioning:** reference-image/text-conditioned multi-game video with camera/keyboard/mouse signals; 2.0 adds free-form multi-turn instructions and event changes.
- **Evaluation:** FVD, VBench-style quality/dynamics/consistency, translation/rotation RPE, FPS, human study, and 2.0's InterBench trigger/alignment/fluency/end-state/physics criteria.
- **Official artifacts:** [1.0 paper](https://arxiv.org/abs/2506.17201), [2.0 paper](https://arxiv.org/abs/2511.23429), [1.0 project](https://hunyuan-gamecraft.github.io/), [1.0 code](https://github.com/Tencent-Hunyuan/Hunyuan-GameCraft-1.0), [1.0 weights](https://huggingface.co/tencent/Hunyuan-GameCraft-1.0), [2.0 project](https://hunyuan-gamecraft-2.github.io/), [official 2.0 demo](https://hunyuan.tencent.com/game/game-craft).
- **Openness:** **Partial (1.0) / Closed (2.0).** Version 1.0 provides inference and checkpoints but not its full trainer/corpus; 2.0 provides no downloadable code or checkpoint.

### 10. Scalable Generative Game Engine: Breaking the Resolution Wall via Hardware-Algorithm Co-Design

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Co-designs the generation algorithm and hardware execution path to move neural racing/platformer gameplay beyond low-resolution real-time generation.
- **中文：** 通过生成算法与硬件执行路径协同设计，把神经 racing/platformer gameplay 推进到更高分辨率实时生成。
- **Generates / action conditioning:** 720×480 racing and platformer frames conditioned on player actions, with a latency-oriented streaming pipeline.
- **Evaluation:** FPS, motion-to-photon latency and delay breakdown, FID/LPIPS, and control sensitivity; the paper reports 26.4 FPS racing, 48.3 FPS platformer, 2.7 ms amortized latency, PGG FID 28.5, and LPIPS 0.052.
- **Official artifacts:** [paper](https://arxiv.org/abs/2602.00608).
- **Openness:** **Closed.** No official project, repository, model, data, or evaluator was found by the cutoff.

### 11. Solaris — Building a Multiplayer Video World Model in Minecraft

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Generates synchronized Minecraft observations for two players so movement, building, memory, and shared-world consistency can be judged from multiple viewpoints.
- **中文：** 为两名玩家同步生成 Minecraft 观察，使移动、建造、记忆与共享世界的多视角一致性可以直接评测。
- **Generates / action conditioning:** two coordinated first-person streams from paired initial observations and each player's controls; the collection engine records synchronized video/action trajectories.
- **Evaluation:** held-out Movement, Grounding, Memory, Building, and cross-view Consistency episodes, FID, and an officially released VLM self-consistency metric.
- **Official artifacts:** [paper](https://arxiv.org/abs/2602.22208), [project](https://solaris-wm.github.io/), [training/inference/evaluation](https://github.com/solaris-wm/solaris), [collection engine](https://github.com/solaris-wm/solaris-engine), [model/data collections](https://huggingface.co/collections/nyu-visionx/solaris-models).
- **Openness:** **Open.** The trainer, GPU/TPU inference, weights, multiplayer data, and metric are public; full pretraining additionally depends on separately distributed VPT data.

### 12. MultiGen — Level-Design for Editable Multiplayer Worlds in Diffusion Game Engines

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Adds editable top-down level structure and persistent external memory to a diffusion game engine, making multiplayer spaces reproducible instead of trapped in recent video context.
- **中文：** 为扩散游戏引擎加入可编辑俯视关卡结构与持久外部记忆，使多人空间可复现，而不只依赖短期视频上下文。
- **Generates / action conditioning:** consistent first-person views for multiple players; player actions update shared pose/map memory, which conditions each generated observation and supports encounters, death, and respawn.
- **Evaluation:** SSIM, PSNR, and LPIPS against simulator frames; VLM opponent-presence accuracy/precision/recall; context/memory ablations; approximately 20 FPS on one A100 per player.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.06679), [author project](https://ryanpo.com/multigen/).
- **Openness:** **Closed.** The paper and project demonstrations are public, but no official code, model, data, or evaluator is downloadable.

### 13. WorldCam — Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Grounds immediate controls and long-term revisitation in one 6-DoF camera-pose representation to reduce geometric drift.
- **中文：** 用统一的 6-DoF 相机位姿同时约束即时操作与长期重访，降低交互游戏世界中的几何漂移。
- **Generates / action conditioning:** autoregressive first-person gaming video from an initial frame; keyboard/mouse controls update global camera pose, which retrieves relevant past observations.
- **Evaluation:** translation/rotation RPE, VBench++, PSNR/LPIPS/MEt3R/DINO similarity and sharpness, 200-frame tests, speed, and a blinded 30-person study.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.16871), [project](https://cvlab-kaist.github.io/WorldCam/), [official inference](https://github.com/cvlab-kaist/WorldCam), [official weights](https://huggingface.co/worldcam/worldcam), [open-game recordings](https://huggingface.co/datasets/worldcam/worldcam-dataset).
- **Openness:** **Partial.** A CS:GO-tuned checkpoint and inference are public, but training code and the paper's training corpus are not; the open Xonotic/Unvanquished recordings are a different release.

### 14. ActionParty — Multi-Subject Action Binding in Generative Video Games

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Extends action-conditioned video generation from one controllable subject to as many as seven, preserving which action belongs to which player.
- **中文：** 把动作条件视频从单一可控主体扩展到最多 7 名玩家，并保持每个动作与对应身份正确绑定。
- **Generates / action conditioning:** multiplayer Melting Pot video conditioned on subject-specific action streams; experiments span 46 games and 230 rollouts.
- **Evaluation:** Movement Accuracy, Effect Accuracy, PSNR, LPIPS, FVD, and subject/action identity binding; one reported setup reaches 87.2% movement accuracy and 91.3% detection.
- **Official artifacts:** [paper](https://arxiv.org/abs/2604.02330), [project](https://action-party.github.io/), [official repository](https://github.com/action-party/action-party).
- **Openness:** **Closed.** The repository states “Code coming soon” and provides no model, dataset, trainer, or evaluator.

### 15. ReactiveGWM — Steering NPC in Reactive Game World Models

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Generates fighting-game rollouts in which low-level player controls and high-level NPC strategies are separately conditioned, enabling prompt-steerable reactions.
- **中文：** 分离玩家底层控制与 NPC 高层策略条件，生成可由“进攻、控制、防守”等提示引导对手反应的格斗游戏过程。
- **Generates / action conditioning:** Street Fighter II/Alpha 3 video; player movement/attack enters as action bias while NPC strategy prompts enter through cross-attention and transfer across games.
- **Evaluation:** player Move/Attack accuracy, Gemini/Qwen instruction accuracy, SSIM/LPIPS, zero-shot strategy transfer, and a 19-person action/strategy study.
- **Official artifacts:** [paper](https://arxiv.org/abs/2605.15256), [project](https://inv-wzq.github.io/ReactiveGWM/), [training/inference](https://github.com/INV-WZQ/ReactiveGWM), [models](https://huggingface.co/INV-WZQ/ReactiveGWM-Models), [datasets](https://huggingface.co/datasets/INV-WZQ/ReactiveGWM-Datasets).
- **Openness:** **Open.** Bidirectional and causal training, inference, SF2/SF3/transfer checkpoints, examples, and strategy-aligned data are public.

### 16. SCOPE — Simulating Cross-game Operations in Playable Environments for FPS World Models

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Learns spatially selective responses to dense simultaneous FPS controls across seven games, separating local weapon effects from global movement/camera motion.
- **中文：** 在 7 款 FPS 上学习逐帧、可重叠的密集操作响应，把局部武器效果与全局移动/视角变化分开。
- **Generates / action conditioning:** 480×832, 81-frame clips from an initial image, prompt, and frame-aligned 10-DoF gamepad telemetry covering movement/look and six buttons.
- **Evaluation:** CrossFPS's 1,378 clips; dynamics/flow, photometric smoothness/depth, JEPA/FVD/LPIPS, action composition, scaling, and zero-shot scenes.
- **Official artifacts:** [paper](https://arxiv.org/abs/2605.23345), [project](https://z2tong.github.io/SCOPE/), [official inference](https://github.com/z2tong/SCOPE), [official weights](https://huggingface.co/zizhaotong/SCOPE), [CrossFPS collection](https://huggingface.co/collections/zizhaotong/crossfps).
- **Openness:** **Partial.** Checkpoint, inference examples, dependencies, and CrossFPS data are released, but training code is not.

### 17. MIRA — Multiplayer Interactive World Models with Representation Autoencoders

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Introduces a 5B representation-autoencoder world model for highly dynamic four-player Rocket League rather than treating other players as uncontrolled scenery.
- **中文：** 提出 5B representation-autoencoder 世界模型，同时建模 4 名 Rocket League 玩家，而非把其他玩家当作不可控背景。
- **Generates / action conditioning:** shared Rocket League video conditioned jointly on four players' control streams, trained on the 10K-hour Rocket Science corpus and run at about 20 FPS.
- **Evaluation:** per-player action response, multiplayer attribution and physical consistency, perceptual quality, real-time throughput, and stable recurrent rollouts demonstrated up to five minutes.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.05352), [project](https://mira-wm.com/), [official training/inference/evaluation repository](https://github.com/mira-wm/mira), [Rocket Science dataset](https://huggingface.co/datasets/kyutai/rocket-science).
- **Openness:** **Partial.** Training, inference, evaluation, and data are public, but no downloadable official model checkpoint was found; the live demo alone is not a reproducible weight release.

### 18. StatePlay — State-Aware Game World Models for Mechanics-Consistent Generation

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Jointly predicts video and explicit timers, health, and skill meters so fighting-game outcomes follow mechanics rather than only looking plausible.
- **中文：** 联合预测画面与计时、血量、能量槽等显式状态，使生成的格斗游戏结果遵守机制，而不只是视觉上像游戏。
- **Generates / action conditioning:** Street Fighter III video plus five state variables, conditioned on player movement/attack, prompt, initial frame, and the predicted state branch.
- **Evaluation:** SSIM/LPIPS, Move/Attack accuracy, normalized state distance/alignment, and Gemini/GPT mechanics fidelity on 100 held-out clips; average normalized state error is reported below 0.06.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.26754), [project](https://jimntu.github.io/stateplay_page/), [training/inference](https://github.com/Jimntu/StatePlay), [model](https://huggingface.co/onepiece1999/StatePlay), [dataset](https://huggingface.co/datasets/onepiece1999/StatePlay-Dataset).
- **Openness:** **Open.** Model, 10K-clip data, trainer, inference, and examples are public; VLM judging still depends on proprietary judge versions.

### 19. WanToFight — Real-Time Generative Game Engine for Multi-Player Combat Interaction

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Generates full two-player The King of Fighters '97 matches from both players' keyboard input at consumer-GPU frame rates.
- **中文：** 根据两名玩家的键盘输入，以消费级 GPU 的实时帧率生成完整《拳皇 97》双人对局。
- **Generates / action conditioning:** 512×384 KOF '97 video jointly conditioned on both action streams; a player-association module targets the correct character and DMD/pruned decoding sustains 30 FPS on one RTX 5090.
- **Evaluation:** LPIPS, SSIM, DINOv2, action accuracy, VLM identity-binding consistency under asymmetric probes, full-match rollout, and runtime.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.12592), [project](https://humanaigc.github.io/wantofight/), [official repository](https://github.com/HumanAIGC/wantofight).
- **Openness:** **Closed.** The repository contains the project-page source/assets only; training/inference code, model, data, and evaluator are absent.

### 20. MASS — Multiplayer World Models with Authoritative Shared State

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Predicts one typed authoritative world state from joint actions, then renders any requested camera, avoiding inconsistent per-view latent worlds.
- **中文：** 根据联合动作预测一个类型化权威世界状态，再按需渲染任意相机，避免各视角 latent 世界相互冲突。
- **Generates / action conditioning:** recurrent shared state plus view-specific images for multiplayer Snake and declaratively described games; every player action advances the same state.
- **Evaluation:** LPIPS, field accuracy/full-state exact match, parser-based state recovery, cross-view agreement, structural validity, six-renderer reconstruction, and scale tests with 1,024 players over 10,000 ticks. MASS reports 0.76 state recovery and LPIPS 0.098 on the matched benchmark.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.06257), [project](https://alaya-lab.github.io/MASS/).
- **Openness:** **Closed.** No official code, weights, matched benchmark data, or evaluator are downloadable.

### 21. ForgeWM — Progressive Causal Training for Few-Step Action-Conditioned Video World Models

- **Year / venue / status:** 2026, arXiv technical report.
- **EN:** Fully releases a four-stage recipe that turns a game-conditioned video generator into 1-, 2-, and 4-step real-time Minecraft/FPS world models.
- **中文：** 完整公开四阶段流程，把游戏动作条件视频生成器蒸馏成 1、2、4 步实时 Minecraft/FPS 世界模型。
- **Generates / action conditioning:** causal Minecraft video from an image and keyboard/mouse streams, plus a CrossFPS gamepad checkpoint; replay-time refinement improves saved trajectories.
- **Evaluation:** VBench, paired LPIPS/flow, keyboard sign-control and mouse accuracy, latency/FPS, replay fidelity, a 41-person study, and seven-game CrossFPS transfer.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.14022), [project](https://asdfo123.github.io/ForgeWM/), [full code](https://github.com/asdfo123/ForgeWM), [models](https://huggingface.co/ForgeWM/ForgeWM), [prepared data](https://huggingface.co/datasets/ForgeWM/ForgeWM-data).
- **Openness:** **Open.** Training/inference, stage 0–3 checkpoints, few-step students, CrossFPS checkpoint, and roughly 89 GB of prepared data are public; upstream licenses still apply.

### 22. Marionette — Predicting World States, Rendering Geometry, Painting Appearance

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Predicts an explicit 276-D articulated multi-character state, renders geometry deterministically, then uses diffusion only to paint appearance.
- **中文：** 先预测 276 维多角色关节世界状态，再确定性渲染几何，最后只让扩散模型负责外观绘制。
- **Generates / action conditioning:** long-horizon character-game rollouts; action IDs drive state dynamics, fixed kinematics/collision/rasterization creates control video, and a conditioned model renders RGB.
- **Evaluation:** root-aligned joint error, character separation, ground penetration, rule-based repair, and observation FVD; the abstract reports 66% less penetration after explicit rules.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.14530), [project](https://alayalab.github.io/Marionette/), [official inference/runtime](https://github.com/AlayaLab/Marionette), [official weights](https://huggingface.co/AlayaLab/Marionette), [source WildWorld corpus](https://github.com/AlayaLab/WildWorld).
- **Openness:** **Partial.** The three-stage inference path, weights, and reproducibility seeds are public, but training code and the full 2,241-segment derived corpus are not; assets are research-only.

### 23. Magpie — Real-Time World Renderer for Interactive Games

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Leaves rules, physics, and reproducible state transitions in a conventional engine while a learned renderer converts white-box frames into high-fidelity game visuals.
- **中文：** 把规则、物理与可复现状态转移留在传统引擎中，再由学习式渲染器把 white-box 帧转成高保真游戏画面。
- **Generates / action conditioning:** RGB video conditioned on stripped white-box engine frames; user input first advances the authoritative engine, so the learned model renders rather than invents logic.
- **Evaluation:** visual fidelity and persistence, mismatch to white-box conditions, compute throughput, and end-to-end interaction latency; the paper reports 32.2 FPS at 1024×768 and about 1.6 s input-to-visual latency. Training uses about 300 hours of paired 1080p/60-FPS recordings from 30+ Unreal scenes.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.27168), [author project](https://zhanxy.xyz/Magpie-website/).
- **Openness:** **Closed.** Project buttons do not lead to code, data, or weights; no runnable checkpoint or evaluator was released.

## B. Generation-specific datasets and benchmarks / 生成专用数据集与评测（5）

### 24. WildWorld / WildBench

- **Year / venue / status:** 2026, arXiv dataset/benchmark preprint.
- **EN:** Builds a large action/state-aligned ARPG corpus and a benchmark that directly checks whether generated worlds follow actions and preserve explicit state.
- **中文：** 构建大规模动作/状态对齐 ARPG 语料，并直接评测生成世界是否遵循动作、保持显式状态。
- **Generation/action task:** 108M frames with 450+ actions and 119 annotations support action-conditioned video/state modeling; WildBench targets Action Following and State Alignment rather than policy return.
- **Evaluation:** benchmark construction and validation include human agreement (85% reported) and coordinate-level accuracy (43.23% reported), alongside the two generation axes.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.23497), [correct author project](https://alaya-studio.github.io/wildworld-project/), [official repository](https://github.com/AlayaLab/WildWorld), [official dataset](https://huggingface.co/datasets/AlayaLab/WildWorld).
- **Openness:** **Partial.** Gated Part 1 currently exposes 574 hours, 3,434 samples, and 13,740 files; Parts 2/3 and WildBench code are pending. The older `shandaai.github.io` URL in the arXiv comment was unavailable at the cutoff.

### 25. EgoCS-400K — An Egocentric Gameplay Dataset for World Models

- **Year / venue / status:** 2026, arXiv dataset preprint.
- **EN:** Aligns egocentric CS/CS2 video with controls, camera motion, language, state, and events for training models that predict how gameplay changes next.
- **中文：** 对齐 CS/CS2 第一人称视频、控制、相机运动、语言、状态与事件，用于训练预测游戏下一步变化的世界模型。
- **Generation/action task:** announced scale is 400K videos, 10K hours, 1K matches, 40K rounds, and 13 maps, with temporal segments and action/event annotations for future-video generation.
- **Evaluation:** dataset scale, action/event/map coverage, temporal-alignment inspection, and downstream world-model motivation; no downloadable fixed benchmark/evaluator was available.
- **Official artifacts:** [paper](https://arxiv.org/abs/2606.18180), [project](https://egocs-400k.github.io/), [official processing repository](https://github.com/EgoCS-400K/Dataset), [official annotation viewer](https://huggingface.co/spaces/Cooler-Master/cs2-action-annotation-viewer-preview).
- **Openness:** **Partial.** Parsing, action extraction, and segment-processing code are substantive, but the project still says “Data coming soon” and no official Hugging Face dataset was found.

### 26. PhysEditWorld — A Large-Scale Dataset Toward Physics-Editable World Models

- **Year / venue / status:** 2026, arXiv dataset/resource preprint.
- **EN:** Replays identical UE5 initial states and actions under edited gravity so a model can be tested on following a requested physical rule, not just matching appearance.
- **中文：** 在 UE5 中固定初始状态与动作、只改变重力重放，从而检验模型是否真正遵循指定物理规则，而不只是复刻外观。
- **Generation/action task:** paired RGB, depth, normals, audio, actions, camera, engine state, and gravity supervision for gravity-conditioned video and action-conditioned first-person rollouts.
- **Evaluation:** proposed gravity-conditioned video, action-conditioned world-model, and gravity-aware video-language tasks; initial utility studies exist, but the fixed evaluator is not released.
- **Official artifacts:** [paper](https://arxiv.org/abs/2606.26694), [project](https://yizhiqianbi.github.io/physeditworld/), [official repository](https://github.com/yizhiqianbi/physeditworld), [official ModelScope entry](https://www.modelscope.cn/datasets/GelerCAT/PhysicalWorld).
- **Openness:** **Partial.** Schema and demo subsets are public; the full 100+ hour/60M-frame corpus, UE5 pipeline, and evaluation scripts remain planned and subject to asset-license review.

### 27. PlayWorld — Benchmarking World Models with Agent Players over Long-Horizon Objectives

- **Year / venue / status:** 2026, arXiv benchmark preprint.
- **EN:** Uses agent players as test probes that pursue long-horizon objectives inside a generated world; it evaluates the world model, not whether a new game-playing policy is strong.
- **中文：** 让 agent player 在生成世界内执行长时目标，把它作为测试探针；评分对象是世界模型，而不是新玩家策略的强弱。
- **Generation/action task:** 171 interactive scenarios exercise generated-world geometry, interactions, insight evolution, visible evolution, and out-of-sight evolution.
- **Evaluation:** scenario execution plus geometry, interaction, insight-evolution, and world-evolution judging; the benchmark packages prompts, assets, runners, and leaderboard logic.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.13552), [project](https://kxding.github.io/project/PlayWorld/), [official code](https://github.com/hku-sail/PlayWorld), [official benchmark data](https://huggingface.co/datasets/jocelynd/playworld-bench), [official leaderboard](https://huggingface.co/spaces/jocelynd/PlayWorld-Leaderboard).
- **Openness:** **Open.** Code, 178-file benchmark data, and evaluator/leaderboard assets are public; full execution and judging still depend on proprietary world services plus Claude/Gemini APIs.

### 28. Game2World Engine — Unlocking In-the-Wild Gameplay Videos for World Model Training

- **Year / venue / status:** 2026, arXiv data-engine preprint.
- **EN:** Removes game UI from raw gameplay while preserving the underlying world, turning abundant in-the-wild clips into cleaner training material for generative world models.
- **中文：** 从原始游戏视频中移除界面、保留底层世界，把大量野外 gameplay 片段转成更干净的生成式世界模型训练材料。
- **Generation/action task:** UI taxonomy, 96K paired HUD/no-HUD training examples, and a learned cleaning engine; it prepares downstream world-model data rather than training the world model itself.
- **Evaluation:** 1,079 clips from 303 games and a released 100-synthetic/100-wild benchmark; the paper reports +6.83% VideoReward, AAR 95.36 synthetic/80.05 wild, and 99.8 background preservation.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.24680), [official full code](https://github.com/Dongping-Chen/Game2World), [official LoRA models](https://huggingface.co/shuaishuaicdp/Game2World), [official benchmark](https://huggingface.co/datasets/shuaishuaicdp/Game2World-Benchmark), [official HUD-video data](https://huggingface.co/datasets/shuaishuaicdp/hud-video).
- **Openness:** **Open.** Training, inference, evaluation, two LoRAs, benchmark data, and 17 HUD-video archives were verified on 2026-08-31; this is an artifact-status change after the original 2026-08-29 audit.

## C. Field framing and boundary systems / 领域框架与边界系统（5）

### 29. Position: Interactive Generative Video as Next-Generation Game Engine

- **Year / venue / status:** 2025, arXiv position paper.
- **EN:** Defines interactive generative video's role in a game-engine stack and proposes an L0–L4 roadmap from passive clips to controllable, persistent worlds.
- **中文：** 界定交互式生成视频在游戏引擎栈中的位置，并提出从被动片段到可控、持久世界的 L0–L4 路线。
- **Generates / action conditioning:** no generator is introduced; the paper decomposes future systems into generation, control, memory/state, interaction, and production components.
- **Evaluation:** conceptual maturity levels and research requirements, not an empirical leaderboard.
- **Official artifacts:** [paper](https://arxiv.org/abs/2503.17359).
- **Openness:** **Paper-only by design.** It is included as field framing; there is no claimed model, dataset, code, weight, or evaluator to reproduce.

### 30. GameGen-X — Interactive Open-world Game Video Generation

- **Year / venue / status:** 2025, ICLR 2025, peer-reviewed conference paper.
- **EN:** Combines open-domain text-to-game-video synthesis with structured instruction/event-conditioned continuation for diverse game scenes.
- **中文：** 同时支持开放域文本生成游戏视频，以及依据结构化指令/事件继续生成多样游戏场景。
- **Generates / action conditioning:** text-to-video clips and context-video continuation; InstructNet uses structured events rather than a universal low-level keyboard schema, so it is a boundary system rather than a core low-level-action engine here.
- **Evaluation:** FID/FVD, text-video alignment, motion/quality/consistency, OGameEval-Gen/OGameEval-Ins, user preference, and instruction/control success.
- **Official artifacts:** [OpenReview](https://openreview.net/forum?id=8VG8tpPZhe), [arXiv](https://arxiv.org/abs/2411.00769), [project](https://gamegen-x.github.io/), [official repository/OGameData metadata](https://github.com/GameGen-X/GameGen-X).
- **Openness:** **Partial.** OGameData URL/timestamp/caption metadata are public, but model code/weights and the internally recorded 140K instruction subset are not.

### 31. From Pixels to States — Rethinking Interactive World Models as Game Engines

- **Year / venue / status:** 2026, arXiv perspective/survey and data-engine paper.
- **EN:** Frames a generative game engine as an action–state–observation loop and audits the field across control, state dynamics, persistence, and real-time generation.
- **中文：** 用“动作—状态—观察”闭环重新界定生成式游戏引擎，并从控制、状态动力学、持续性与实时生成四方面梳理缺口。
- **Generates / action conditioning:** no model is proposed; its concrete resource claim is a Black Myth: Wukong collection engine producing 90+ hours of aligned actions, states, observations, and semantics.
- **Evaluation:** conceptual four-axis comparison, useful for separating responsive-looking pixels from rule/state preservation; no model leaderboard is introduced.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.14076).
- **Openness:** **Closed.** No official repository, downloadable Wukong data, weights, or evaluator were linked by the cutoff.

### 32. Position: Profiling Game Worlds by Transition Complexity

- **Year / venue / status:** 2026, ICML 2026 position paper/poster.
- **EN:** Argues that game-world datasets and models should report how hard the underlying transition process is before comparing prediction quality.
- **中文：** 主张在比较游戏世界模型预测质量前，先报告底层状态转移过程本身有多难。
- **Generates / action conditioning:** no generator is proposed; the Transition Complexity Profile characterizes intrinsic branching, hidden interaction/opponent uncertainty, and temporal/spatial dependency at the declared interface.
- **Evaluation:** TCP metadata and temporal/spatial probe curves rather than a model score or playing return.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.18079), [official ICML record](https://icml.cc/virtual/2026/poster/67074).
- **Openness:** **Paper-only by design.** The paper provides framing and does not claim a model, dataset package, or evaluator release.

### 33. WorldMind — Decoupled Game World Model for State-Aware NPC Behavior

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Separates state reconstruction, NPC planning, action translation, and visual generation so boss behavior reacts to the generated world's changing state.
- **中文：** 将状态重建、NPC 决策、动作转换与画面生成分层并闭环连接，使 Boss 行为随生成世界状态变化而反应。
- **Generates / action conditioning:** about-20-FPS boss-fight video; player input and a state-aware internal NPC planner produce aligned action text for the visual generator. It is a boundary entry because planning is integral, although the displayed output is generated world behavior.
- **Evaluation:** boss/player state reconstruction, decision sensitivity/validity, pairwise preference, action validity, and tactical sequence fit; BOSS-140K provides internal annotations in the paper.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.21439), [project](https://teawhite.cn/WorldMind/), [official release stub](https://github.com/TeaWhiteBro/WorldMind).
- **Openness:** **Closed.** Code, weights, BOSS-140K, and evaluator remain unavailable; the repository says release materials are being prepared.

## Explicit exclusions and boundary decisions / 明确排除与边界判断

### Excluded because playing or planning is the core objective

- **DIAMOND — Diffusion for World Modeling: Visual Details Matter in Atari** ([paper](https://arxiv.org/abs/2405.12399), [official code](https://github.com/eloialonso/diamond)): its diffusion model produces observations, but the central product is an RL agent and the headline comparison is Atari-100k return.
- **SimPLe, IRIS, Dreamer / DreamerV2/V3, and related imagination-based RL:** the predictive model is a means to improve policy learning, sample efficiency, or control return; the evaluated product is the policy.
- **GameWAM — A World Action Model for Video Games** ([paper](https://arxiv.org/abs/2608.26200)): it predicts future observations and executable controls, but its central contribution is a closed-loop gameplay/GUI policy evaluated by task success.
- **ActSWM and similar planning models:** excluded when action selection or planning success, rather than a human-controllable generated environment, is the main result.

### Excluded because the domain is not specifically game generation

- **Driving:** GAIA-1, DriveDreamer/Drive-WM, Waymo World Model, and related autonomous-driving simulators.
- **Robotics/embodiment:** UniSim, DreamGen, DreamDojo, Cosmos robot/physical-AI models, and manipulation world models.
- **General interactive video/world models:** YUME, WorldPlay/HY-World, AlayaWorld, DreamX-World, LingBot-World, ReWorld, ActWorld, and comparable systems may show game-like demos or train partly on gameplay, but their declared scope and principal evaluations span real, stylized, or embodied scenes rather than specifically generating games.
- **Genie 2 / Genie 3:** relevant DeepMind demonstrations, but at the cutoff they remain announcements without a citable technical paper and reproducible artifacts. The peer-reviewed Genie entry is the defensible paper record.

## Comparison cautions / 横向比较注意事项

1. **New-world creation, existing-game simulation, and learned rendering differ.** Genie/GameFactory can transfer prompts or appearance; GameNGen/MineWorld/MIRA simulate existing titles; Magpie keeps logic in a conventional engine. They should not share one “best game creator” ranking.
2. **Pixel responsiveness is not game logic.** Keyboard/mouse accuracy may coexist with impossible health, cooldown, collision, or multiplayer state; StatePlay, MASS, Marionette, WorldMind, and PhysEditWorld expose these gaps.
3. **Reported scores are rarely directly comparable.** Resolution, rollout length, action vocabulary, initial conditions, proprietary games, and judge models differ. GameWorld Score, InterBench, CrossFPS, WildBench, and PlayWorld are separate protocols.
4. **Open inference is not open training.** Oasis, Matrix-Game, Hunyuan-GameCraft, and WorldCam run from official checkpoints but withhold headline training data or full trainers. MIRA is the reverse case: training/inference and data are open, but an author checkpoint was not found.
5. **Rights remain separate from artifact access.** YouTube IDs can link-rot; ROMs, AAA footage, Minecraft/Doom assets, UE5 marketplace scenes, and derived WildWorld checkpoints may restrict redistribution or commercial use even when code is public.
