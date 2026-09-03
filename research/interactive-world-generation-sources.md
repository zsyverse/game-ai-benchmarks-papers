# Interactive game-world generation: verified primary sources

> Research cutoff / 检索截止: **2026-09-04 (Asia/Shanghai)**.

This dossier contains exactly the **23 canonical records** in the public interactive-world index: 21 direct generation methods and two formal generation benchmarks.

本底稿与公开交互世界索引严格一一对应，共 **23 条 canonical 记录**：21 条直接生成方法与 2 条正式生成 benchmark。

Every numbered dossier record corresponds to the same public ID. Only direct generation methods and formal generation benchmarks appear here; rejected candidates are documented solely in the strict audit.

每条底稿记录与同编号公开条目对应。这里只保留直接生成方法与正式生成 benchmark；被拒候选仅记录在严格审计中。

## Interactive-world generation methods / 交互世界生成方法

### 1. Promptable Game Models

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

### 5. GameFactory — Creating New Games with Generative Interactive Videos

- **Year / venue / status:** 2025, ICCV 2025 Highlight, peer-reviewed conference paper.
- **EN:** Decouples Minecraft visual style from keyboard/mouse control so an open-domain video prior can transfer those controls into visually new game scenes.
- **中文：** 将 Minecraft 画风与键鼠控制解耦，使开放域视频先验能把控制能力迁移到全新视觉风格的游戏场景。
- **Generates / action conditioning:** first-person open-domain interactive video from a scene image, W/S/A/D, jump/sneak/sprint, and continuous pitch/yaw mouse motion.
- **Evaluation:** camera-pose and optical-flow error, CLIP similarity, FID/FVD, domain classification, rare-action combinations, and autoregressive rollouts.
- **Official artifacts:** [paper](https://arxiv.org/abs/2501.08325), [author project](https://yujiwen.github.io/gamefactory/), [official repository](https://github.com/KlingAIResearch/GameFactory), [GF-Minecraft dataset](https://huggingface.co/datasets/KwaiVGI/GameFactory-Dataset).
- **Openness:** **Partial.** Roughly 70 hours of video/action data and small utilities are public, but model training/inference code and weights are not.

### 6. MineWorld — a Real-Time and Open-Source Interactive World Model on Minecraft

- **Year / venue / status:** 2025, arXiv technical report.
- **EN:** Uses interleaved visual/action tokens and parallel diagonal decoding to generate controllable Minecraft observations at 4–7 FPS.
- **中文：** 以交错的视觉/动作 token 和并行对角解码，在 4–7 FPS 下生成可操控的 Minecraft 后续画面。
- **Generates / action conditioning:** Minecraft frames from visual history and an 11-token vocabulary covering movement, camera, and game controls.
- **Evaluation:** FVD and visual metrics, inverse-dynamics discrete-action classification, camera-motion error, and decoding throughput; official scripts aggregate paper metrics.
- **Official artifacts:** [paper](https://arxiv.org/abs/2504.08388), [official code/evaluation](https://github.com/microsoft/mineworld), [official model location](https://huggingface.co/microsoft/mineworld).
- **Openness:** **Partial.** Inference, demo, decoding, and metric code remain public, but the README says checkpoints were removed; training code/data are absent.

### 7. Matrix-Game 1.0

- **Year / venue / status:** 2025–2026, three arXiv technical reports.
- **EN:** Progresses from Minecraft action-conditioned generation and GameWorld Score to multi-game real-time streaming, then memory-augmented 720p long-horizon generation.
- **中文：** 从 Minecraft 动作条件生成与 GameWorld Score，演进到多游戏实时流式生成，再到带长期记忆的 720p 长时交互生成。
- **Generates / action conditioning:** image-to-interactive video from keyboard states and continuous mouse/camera motion; later versions add universal/GTA/Temple Run and Unreal-scene models plus camera-aware retrieval.
- **Evaluation:** GameWorld Score, human preferences, long-rollout revisitation/memory, VAE PSNR/SSIM, and throughput up to about 40 FPS in the 3.0 setup.
- **Official artifacts:** [1.0 paper](https://arxiv.org/abs/2506.18701), [2.0 paper](https://arxiv.org/abs/2508.13009), [3.0 paper](https://arxiv.org/abs/2604.08995), [unified repository](https://github.com/SkyworkAI/Matrix-Game), [1.0 models](https://huggingface.co/Skywork/Matrix-Game), [2.0 models](https://huggingface.co/Skywork/Matrix-Game-2.0), [3.0 models](https://huggingface.co/Skywork/Matrix-Game-3.0), [1.0 project](https://matrix-game-homepage.github.io/), [2.0 project](https://matrix-game-v2.github.io/), [3.0 project](https://matrix-game-v3.github.io/).
- **Openness:** **Partial.** Inference and selected weights exist for all versions, but full training/data are absent and the strongest mixed/28B 3.0 models remain withheld.

### 8. Hunyuan-GameCraft 1.0

- **Year / venue / status:** 2025–2026, arXiv technical reports.
- **EN:** GameCraft maps keyboard/mouse input into camera-aware long game-video rollouts; GameCraft-2 adds mid-rollout natural-language interactions such as opening doors or triggering explosions.
- **中文：** 一代把键鼠输入映射到相机感知长视频生成；二代进一步支持“开门、触发爆炸”等运行中自然语言交互。
- **Generates / action conditioning:** reference-image/text-conditioned multi-game video with camera/keyboard/mouse signals; 2.0 adds free-form multi-turn instructions and event changes.
- **Evaluation:** FVD, VBench-style quality/dynamics/consistency, translation/rotation RPE, FPS, human study, and 2.0's InterBench trigger/alignment/fluency/end-state/physics criteria.
- **Official artifacts:** [1.0 paper](https://arxiv.org/abs/2506.17201), [2.0 paper](https://arxiv.org/abs/2511.23429), [1.0 project](https://hunyuan-gamecraft.github.io/), [1.0 code](https://github.com/Tencent-Hunyuan/Hunyuan-GameCraft-1.0), [1.0 weights](https://huggingface.co/tencent/Hunyuan-GameCraft-1.0), [2.0 project](https://hunyuan-gamecraft-2.github.io/), [official 2.0 demo](https://hunyuan.tencent.com/game/game-craft).
- **Openness:** **Partial (1.0) / Closed (2.0).** Version 1.0 provides inference and checkpoints but not its full trainer/corpus; 2.0 provides no downloadable code or checkpoint.

### 9. Scalable Generative Game Engine

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Co-designs the generation algorithm and hardware execution path to move neural racing/platformer gameplay beyond low-resolution real-time generation.
- **中文：** 通过生成算法与硬件执行路径协同设计，把神经 racing/platformer gameplay 推进到更高分辨率实时生成。
- **Generates / action conditioning:** 720×480 racing and platformer frames conditioned on player actions, with a latency-oriented streaming pipeline.
- **Evaluation:** FPS, motion-to-photon latency and delay breakdown, FID/LPIPS, and control sensitivity; the paper reports 26.4 FPS racing, 48.3 FPS platformer, 2.7 ms amortized latency, PGG FID 28.5, and LPIPS 0.052.
- **Official artifacts:** [paper](https://arxiv.org/abs/2602.00608).
- **Openness:** **Closed.** No official project, repository, model, data, or evaluator was found by the cutoff.

### 10. Solaris — Building a Multiplayer Video World Model in Minecraft

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Generates synchronized Minecraft observations for two players so movement, building, memory, and shared-world consistency can be judged from multiple viewpoints.
- **中文：** 为两名玩家同步生成 Minecraft 观察，使移动、建造、记忆与共享世界的多视角一致性可以直接评测。
- **Generates / action conditioning:** two coordinated first-person streams from paired initial observations and each player's controls; the collection engine records synchronized video/action trajectories.
- **Evaluation:** held-out Movement, Grounding, Memory, Building, and cross-view Consistency episodes, FID, and an officially released VLM self-consistency metric.
- **Official artifacts:** [paper](https://arxiv.org/abs/2602.22208), [project](https://solaris-wm.github.io/), [training/inference/evaluation](https://github.com/solaris-wm/solaris), [collection engine](https://github.com/solaris-wm/solaris-engine), [model/data collections](https://huggingface.co/collections/nyu-visionx/solaris-models).
- **Openness:** **Open.** The trainer, GPU/TPU inference, weights, multiplayer data, and metric are public; full pretraining additionally depends on separately distributed VPT data.

### 11. MultiGen — Editable Multiplayer Worlds

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Adds editable top-down level structure and persistent external memory to a diffusion game engine, making multiplayer spaces reproducible instead of trapped in recent video context.
- **中文：** 为扩散游戏引擎加入可编辑俯视关卡结构与持久外部记忆，使多人空间可复现，而不只依赖短期视频上下文。
- **Generates / action conditioning:** consistent first-person views for multiple players; player actions update shared pose/map memory, which conditions each generated observation and supports encounters, death, and respawn.
- **Evaluation:** SSIM, PSNR, and LPIPS against simulator frames; VLM opponent-presence accuracy/precision/recall; context/memory ablations; approximately 20 FPS on one A100 per player.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.06679), [author project](https://ryanpo.com/multigen/).
- **Openness:** **Closed.** The paper and project demonstrations are public, but no official code, model, data, or evaluator is downloadable.

### 12. WorldCam — Interactive Autoregressive 3D Gaming Worlds

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Grounds immediate controls and long-term revisitation in one 6-DoF camera-pose representation to reduce geometric drift.
- **中文：** 用统一的 6-DoF 相机位姿同时约束即时操作与长期重访，降低交互游戏世界中的几何漂移。
- **Generates / action conditioning:** autoregressive first-person gaming video from an initial frame; keyboard/mouse controls update global camera pose, which retrieves relevant past observations.
- **Evaluation:** translation/rotation RPE, VBench++, PSNR/LPIPS/MEt3R/DINO similarity and sharpness, 200-frame tests, speed, and a blinded 30-person study.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.16871), [project](https://cvlab-kaist.github.io/WorldCam/), [official inference](https://github.com/cvlab-kaist/WorldCam), [official weights](https://huggingface.co/worldcam/worldcam), [open-game recordings](https://huggingface.co/datasets/worldcam/worldcam-dataset).
- **Openness:** **Partial.** A CS:GO-tuned checkpoint and inference are public, but training code and the paper's training corpus are not; the open Xonotic/Unvanquished recordings are a different release.

### 13. ActionParty — Multi-Subject Action Binding

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Extends action-conditioned video generation from one controllable subject to as many as seven, preserving which action belongs to which player.
- **中文：** 把动作条件视频从单一可控主体扩展到最多 7 名玩家，并保持每个动作与对应身份正确绑定。
- **Generates / action conditioning:** multiplayer Melting Pot video conditioned on subject-specific action streams; experiments span 46 games and 230 rollouts.
- **Evaluation:** Movement Accuracy, Effect Accuracy, PSNR, LPIPS, FVD, and subject/action identity binding; one reported setup reaches 87.2% movement accuracy and 91.3% detection.
- **Official artifacts:** [paper](https://arxiv.org/abs/2604.02330), [project](https://action-party.github.io/), [official repository](https://github.com/action-party/action-party).
- **Openness:** **Closed.** The repository states “Code coming soon” and provides no model, dataset, trainer, or evaluator.

### 14. SCOPE — Simulating Cross-game Operations

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Learns spatially selective responses to dense simultaneous FPS controls across seven games, separating local weapon effects from global movement/camera motion.
- **中文：** 在 7 款 FPS 上学习逐帧、可重叠的密集操作响应，把局部武器效果与全局移动/视角变化分开。
- **Generates / action conditioning:** 480×832, 81-frame clips from an initial image, prompt, and frame-aligned 10-DoF gamepad telemetry covering movement/look and six buttons.
- **Evaluation:** CrossFPS's 1,378 clips; dynamics/flow, photometric smoothness/depth, JEPA/FVD/LPIPS, action composition, scaling, and zero-shot scenes.
- **Official artifacts:** [paper](https://arxiv.org/abs/2605.23345), [project](https://z2tong.github.io/SCOPE/), [official inference](https://github.com/z2tong/SCOPE), [official weights](https://huggingface.co/zizhaotong/SCOPE), [CrossFPS collection](https://huggingface.co/collections/zizhaotong/crossfps).
- **Openness:** **Partial.** Checkpoint, inference examples, dependencies, and CrossFPS data are released, but training code is not.

### 15. MIRA — Multiplayer Interactive World Models

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Introduces a 5B representation-autoencoder world model for highly dynamic four-player Rocket League rather than treating other players as uncontrolled scenery.
- **中文：** 提出 5B representation-autoencoder 世界模型，同时建模 4 名 Rocket League 玩家，而非把其他玩家当作不可控背景。
- **Generates / action conditioning:** shared Rocket League video conditioned jointly on four players' control streams, trained on the 10K-hour Rocket Science corpus and run at about 20 FPS.
- **Evaluation:** per-player action response, multiplayer attribution and physical consistency, perceptual quality, real-time throughput, and stable recurrent rollouts demonstrated up to five minutes.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.05352), [project](https://mira-wm.com/), [official training/inference/evaluation repository](https://github.com/mira-wm/mira), [Rocket Science dataset](https://huggingface.co/datasets/kyutai/rocket-science).
- **Openness:** **Partial.** Training, inference, evaluation, and data are public, but no downloadable official model checkpoint was found; the live demo alone is not a reproducible weight release.

### 16. StatePlay — State-Aware Game World Models

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Jointly predicts video and explicit timers, health, and skill meters so fighting-game outcomes follow mechanics rather than only looking plausible.
- **中文：** 联合预测画面与计时、血量、能量槽等显式状态，使生成的格斗游戏结果遵守机制，而不只是视觉上像游戏。
- **Generates / action conditioning:** Street Fighter III video plus five state variables, conditioned on player movement/attack, prompt, initial frame, and the predicted state branch.
- **Evaluation:** SSIM/LPIPS, Move/Attack accuracy, normalized state distance/alignment, and Gemini/GPT mechanics fidelity on 100 held-out clips; average normalized state error is reported below 0.06.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.26754), [project](https://jimntu.github.io/stateplay_page/), [training/inference](https://github.com/Jimntu/StatePlay), [model](https://huggingface.co/onepiece1999/StatePlay), [dataset](https://huggingface.co/datasets/onepiece1999/StatePlay-Dataset).
- **Openness:** **Open.** Model, 10K-clip data, trainer, inference, and examples are public; VLM judging still depends on proprietary judge versions.

### 17. WanToFight — Real-Time Multi-Player Combat

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Generates full two-player The King of Fighters '97 matches from both players' keyboard input at consumer-GPU frame rates.
- **中文：** 根据两名玩家的键盘输入，以消费级 GPU 的实时帧率生成完整《拳皇 97》双人对局。
- **Generates / action conditioning:** 512×384 KOF '97 video jointly conditioned on both action streams; a player-association module targets the correct character and DMD/pruned decoding sustains 30 FPS on one RTX 5090.
- **Evaluation:** LPIPS, SSIM, DINOv2, action accuracy, VLM identity-binding consistency under asymmetric probes, full-match rollout, and runtime.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.12592), [project](https://humanaigc.github.io/wantofight/), [official repository](https://github.com/HumanAIGC/wantofight).
- **Openness:** **Closed.** The repository contains the project-page source/assets only; training/inference code, model, data, and evaluator are absent.

### 18. MASS — Multiplayer World Models with Authoritative Shared State

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Predicts one typed authoritative world state from joint actions, then renders any requested camera, avoiding inconsistent per-view latent worlds.
- **中文：** 根据联合动作预测一个类型化权威世界状态，再按需渲染任意相机，避免各视角 latent 世界相互冲突。
- **Generates / action conditioning:** recurrent shared state plus view-specific images for multiplayer Snake and declaratively described games; every player action advances the same state.
- **Evaluation:** LPIPS, field accuracy/full-state exact match, parser-based state recovery, cross-view agreement, structural validity, six-renderer reconstruction, and scale tests with 1,024 players over 10,000 ticks. MASS reports 0.76 state recovery and LPIPS 0.098 on the matched benchmark.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.06257), [project](https://alaya-lab.github.io/MASS/).
- **Openness:** **Closed.** No official code, weights, matched benchmark data, or evaluator are downloadable.

### 19. ForgeWM — Progressive Causal Training

- **Year / venue / status:** 2026, arXiv technical report.
- **EN:** Fully releases a four-stage recipe that turns a game-conditioned video generator into 1-, 2-, and 4-step real-time Minecraft/FPS world models.
- **中文：** 完整公开四阶段流程，把游戏动作条件视频生成器蒸馏成 1、2、4 步实时 Minecraft/FPS 世界模型。
- **Generates / action conditioning:** causal Minecraft video from an image and keyboard/mouse streams, plus a CrossFPS gamepad checkpoint; replay-time refinement improves saved trajectories.
- **Evaluation:** VBench, paired LPIPS/flow, keyboard sign-control and mouse accuracy, latency/FPS, replay fidelity, a 41-person study, and seven-game CrossFPS transfer.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.14022), [project](https://asdfo123.github.io/ForgeWM/), [full code](https://github.com/asdfo123/ForgeWM), [models](https://huggingface.co/ForgeWM/ForgeWM), [prepared data](https://huggingface.co/datasets/ForgeWM/ForgeWM-data).
- **Openness:** **Open.** Training/inference, stage 0–3 checkpoints, few-step students, CrossFPS checkpoint, and roughly 89 GB of prepared data are public; upstream licenses still apply.

### 20. Marionette — Predicting World States, Rendering Geometry, Painting Appearance

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Predicts an explicit 276-D articulated multi-character state, renders geometry deterministically, then uses diffusion only to paint appearance.
- **中文：** 先预测 276 维多角色关节世界状态，再确定性渲染几何，最后只让扩散模型负责外观绘制。
- **Generates / action conditioning:** long-horizon character-game rollouts; action IDs drive state dynamics, fixed kinematics/collision/rasterization creates control video, and a conditioned model renders RGB.
- **Evaluation:** root-aligned joint error, character separation, ground penetration, rule-based repair, and observation FVD; the abstract reports 66% less penetration after explicit rules.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.14530), [project](https://alayalab.github.io/Marionette/), [official inference/runtime](https://github.com/AlayaLab/Marionette), [official weights](https://huggingface.co/AlayaLab/Marionette), [source WildWorld corpus](https://github.com/AlayaLab/WildWorld).
- **Openness:** **Partial.** The three-stage inference path, weights, and reproducibility seeds are public, but training code and the full 2,241-segment derived corpus are not; assets are research-only.

### 21. Playable Game Generation

- **Year / venue / status:** 2024, arXiv preprint.
- **EN:** Learns an action-conditioned latent-dynamics engine from game video and action data and emits real-time, player-controllable game frames.
- **中文：** 从游戏视频与动作数据学习动作条件 latent-dynamics 引擎，实时生成可由玩家控制的游戏画面。
- **Generates / action conditioning:** player actions advance an autoregressive learned game world step by step; the output is a playable visual experience rather than source code or a conventional engine project.
- **Evaluation:** visual fidelity, dynamics/action alignment, long-horizon consistency, and real-time playability experiments.
- **Official artifacts:** [paper](https://arxiv.org/abs/2412.00887), [official implementation](https://github.com/GreatX3/Playable-Game-Generation).
- **Openness:** **Partial.** Implementation material is public, but the complete training-data and reproduction path is not.
- **Strict-scope decision:** **KEEP.** The player controls the generated world directly, so this is an interactive-world generation method rather than a game-playing policy.

## Generation benchmarks / 生成 Benchmark

### 22. WildWorld / WildBench

- **Year / venue / status:** 2026, arXiv dataset/benchmark preprint.
- **EN:** Builds a large action/state-aligned ARPG corpus and a benchmark that directly checks whether generated worlds follow actions and preserve explicit state.
- **中文：** 构建大规模动作/状态对齐 ARPG 语料，并直接评测生成世界是否遵循动作、保持显式状态。
- **Generation/action task:** 108M frames with 450+ actions and 119 annotations support action-conditioned video/state modeling; WildBench targets Action Following and State Alignment rather than policy return.
- **Evaluation:** benchmark construction and validation include human agreement (85% reported) and coordinate-level accuracy (43.23% reported), alongside the two generation axes.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.23497), [correct author project](https://alaya-studio.github.io/wildworld-project/), [official repository](https://github.com/AlayaLab/WildWorld), [official dataset](https://huggingface.co/datasets/AlayaLab/WildWorld).
- **Openness:** **Partial.** Gated Part 1 currently exposes 574 hours, 3,434 samples, and 13,740 files; Parts 2/3 and WildBench code are pending. The older `shandaai.github.io` URL in the arXiv comment was unavailable at the cutoff.

### 23. PlayWorld

- **Year / venue / status:** 2026, arXiv benchmark preprint.
- **EN:** Uses agent players as test probes that pursue long-horizon objectives inside a generated world; it evaluates the world model, not whether a new game-playing policy is strong.
- **中文：** 让 agent player 在生成世界内执行长时目标，把它作为测试探针；评分对象是世界模型，而不是新玩家策略的强弱。
- **Generation/action task:** 171 interactive scenarios exercise generated-world geometry, interactions, insight evolution, visible evolution, and out-of-sight evolution.
- **Evaluation:** scenario execution plus geometry, interaction, insight-evolution, and world-evolution judging; the benchmark packages prompts, assets, runners, and leaderboard logic.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.13552), [project](https://kxding.github.io/project/PlayWorld/), [official code](https://github.com/hku-sail/PlayWorld), [official benchmark data](https://huggingface.co/datasets/jocelynd/playworld-bench), [official leaderboard](https://huggingface.co/spaces/jocelynd/PlayWorld-Leaderboard).
- **Openness:** **Open.** Code, 178-file benchmark data, and evaluator/leaderboard assets are public; full execution and judging still depend on proprietary world services plus Claude/Gemini APIs.
