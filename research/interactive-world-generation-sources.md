# Interactive game-world generation: verified primary sources

> Research cutoff / 检索截止: **2026-09-04 (Asia/Shanghai)**.

This dossier contains exactly the **45 canonical records** in the public interactive-world index: 41 direct generation methods and four formal generation benchmarks.

本底稿与公开交互世界索引严格一一对应，共 **45 条 canonical 记录**：41 条直接生成方法与 4 条正式生成 benchmark。

**2026-09-05 targeted expansion / 定向补充:** 17 papers were added across two passes (current records 27–41 and 44–45), and five additional records were separated from previously merged Matrix-Game, Hunyuan-GameCraft and GenieRedux papers. Other records retain the 2026-09-04 audit date; no full re-audit is claimed. 两轮共新增 17 篇论文（现编号 27–41、44–45），并从原合并的三个系列拆出 5 条独立论文记录；其他记录保留原核验日期。

Every numbered dossier record corresponds to the same public ID. Only direct generation methods and formal generation benchmarks appear here; rejected and unresolved candidates are documented in the strict audit and coverage notes.

每条底稿记录与同编号公开条目对应。这里只保留直接生成方法与正式生成 benchmark；被拒与未决候选记录在严格审计和覆盖增补笔记中。

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

### 3. Learning Generative Interactive Environments By Trained Agent Exploration

- **Year / venue / status:** 2024, research paper / technical report.
- **EN:** GenieRedux/GenieRedux-G learn controllable CoinRun worlds using trained-agent exploration.
- **中文：** GenieRedux/GenieRedux-G 用训练后智能体探索数据学习可控 CoinRun 世界。
- **Generates / action conditioning:** GenieRedux/GenieRedux-G learn controllable CoinRun worlds using trained-agent exploration.
- **Evaluation:** CoinRun visual fidelity and controllability; trained-agent versus random exploration.
- **Official artifacts:** [paper](https://arxiv.org/abs/2409.06445), [full text](https://arxiv.org/html/2409.06445), [artifact 1](https://github.com/insait-institute/GenieRedux), [artifact 2](https://huggingface.co/INSAIT-Institute/GenieRedux).
- **Openness:** **Partial.** Shared implementation and models; historical paper configuration not pinned.
- **Independent audit:** [paper evidence and canonical split](independent-world-audit-2026-09-05.md).

### 4. Exploration-Driven Generative Interactive Environments

- **Year / venue / status:** 2025, research paper / technical report.
- **EN:** Reward-independent, uncertainty-driven AutoExplore improves controllable generated environments using RetroAct grouping.
- **中文：** 不依赖环境奖励、由不确定性驱动的 AutoExplore 结合 RetroAct 分组改进可控环境生成。
- **Generates / action conditioning:** Reward-independent, uncertainty-driven AutoExplore improves controllable generated environments using RetroAct grouping.
- **Evaluation:** Visual/action metrics, exploration and adaptation; RetroAct annotates 974 environments.
- **Official artifacts:** [paper](https://arxiv.org/abs/2504.02515), [full text](https://arxiv.org/html/2504.02515), [artifact 1](https://github.com/insait-institute/GenieRedux), [artifact 2](https://huggingface.co/INSAIT-Institute/GenieRedux).
- **Openness:** **Open.** Training/generation/evaluation public; ROMs obtained separately.
- **Independent audit:** [paper evidence and canonical split](independent-world-audit-2026-09-05.md).

### 5. GameNGen — Diffusion Models Are Real-Time Game Engines

- **Year / venue / status:** 2024, arXiv preprint/research project; no archival venue is stated in the paper.
- **EN:** Replaces Doom's renderer and transition loop with action-conditioned diffusion that produces playable frames at about 20 FPS over multi-minute autoregressive sessions.
- **中文：** 用动作条件扩散模型替代 Doom 的渲染与状态转移循环，以约 20 FPS 自回归生成可持续数分钟的交互画面。
- **Generates / action conditioning:** 320×240-padded Doom frames from 64 previous generated frames and their discrete key/action history; a separate RL agent collects trajectories but is not the evaluated product.
- **Evaluation:** teacher-forced/autoregressive PSNR and LPIPS, 16/32-frame FVD, sampling speed, and a blinded real-Doom-versus-simulation human study.
- **Official artifacts:** [paper](https://arxiv.org/abs/2408.14837), [author project](https://gamengen.github.io/), [official project-page source](https://github.com/GameNGen/GameNGen.github.io).
- **Openness:** **Closed.** The repository contains presentation assets, not model code, data, training/inference implementation, or weights.

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

### 8. Matrix-Game: Interactive World Foundation Model

- **Year / venue / status:** 2025, research paper / technical report.
- **EN:** Two-stage Minecraft training generates worlds from images and keyboard/mouse controls.
- **中文：** 以两阶段 Minecraft 训练从图像及键鼠控制生成世界。
- **Generates / action conditioning:** Two-stage Minecraft training generates worlds from images and keyboard/mouse controls.
- **Evaluation:** GameWorld Score, Oasis/MineWorld comparisons and human preference; training FPS is not inference speed.
- **Official artifacts:** [paper](https://arxiv.org/abs/2506.18701), [full text](https://arxiv.org/html/2506.18701), [artifact 1](https://github.com/SkyworkAI/Matrix-Game/tree/main/Matrix-Game-1), [artifact 2](https://huggingface.co/Skywork/Matrix-Game).
- **Openness:** **Partial.** Inference/weights public; full matched training/data not verified.
- **Targeted release-document check, 2026-09-08:** the first-version README specifies A100/H100 and at least 80 GB GPU memory for a single 65-frame inference; this is an author-stated configuration, not a measured lower bound. [Pinned evidence](experiment-entry-points-2026-09-08.md) keeps this separate from version 2/3 real-time claims. No inference was run.
- **Independent audit:** [paper evidence and canonical split](independent-world-audit-2026-09-05.md).

### 9. Matrix-Game 2.0: An Open-Source Real-Time and Streaming Interactive World Model

- **Year / venue / status:** 2025, research paper / technical report.
- **EN:** Few-step autoregressive diffusion and action modules generate streaming UE/GTA5-trained worlds.
- **中文：** 少步自回归扩散与动作模块生成基于 UE/GTA5 训练的流式世界。
- **Generates / action conditioning:** Few-step autoregressive diffusion and action modules generate streaming UE/GTA5-trained worlds.
- **Evaluation:** Minecraft/GameWorld and wild-scene tests; 25 FPS on one H100; Minecraft action metrics do not transfer directly.
- **Official artifacts:** [paper](https://arxiv.org/abs/2508.13009), [full text](https://arxiv.org/html/2508.13009), [artifact 1](https://github.com/SkyworkAI/Matrix-Game/tree/main/Matrix-Game-2), [artifact 2](https://huggingface.co/Skywork/Matrix-Game-2.0).
- **Openness:** **Partial.** Inference/weights public; full training/corpus not verified.
- **Independent audit:** [paper evidence and canonical split](independent-world-audit-2026-09-05.md).

### 10. Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory

- **Year / venue / status:** 2026, research paper / technical report.
- **EN:** Self-correction, camera-aware retrieval and multi-segment DMD enable long-horizon generated worlds.
- **中文：** 自纠正、相机感知检索与多段 DMD 支持长时世界生成。
- **Generates / action conditioning:** Self-correction, camera-aware retrieval and multi-segment DMD enable long-horizon generated worlds.
- **Evaluation:** Memory/revisit and VAE ablations; up to 40 FPS/720p uses eight DiT GPUs plus one VAE GPU.
- **Official artifacts:** [paper](https://arxiv.org/abs/2604.08995), [full text](https://arxiv.org/html/2604.08995), [artifact 1](https://github.com/SkyworkAI/Matrix-Game/tree/main/Matrix-Game-3), [artifact 2](https://huggingface.co/Skywork/Matrix-Game-3.0).
- **Openness:** **Partial.** Two 5B Unreal first-person models released; mixed/28B models and full training/data unavailable.
- **Independent audit:** [paper evidence and canonical split](independent-world-audit-2026-09-05.md).

### 11. Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory

- **Year / venue / status:** 2026, research paper / technical report.
- **EN:** Geometry-aware patch memory, static/dynamic separation and progressive causal distillation.
- **中文：** 几何感知 patch 记忆、静动态分离与渐进因果蒸馏。
- **Generates / action conditioning:** Geometry-aware patch memory, static/dynamic separation and progressive causal distillation.
- **Evaluation:** One-minute base-model control/revisit tests; separately INT8 three-step student reaches 20 FPS/1280×704 on one H100.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.29910), [full text](https://arxiv.org/html/2608.29910), [artifact 1](https://github.com/Riemann-Dynamics/Matrix-Game-3.5), [artifact 2](https://huggingface.co/RiemannDynamics/Matrix-Game-3.5-Base), [artifact 3](https://huggingface.co/RiemannDynamics/Matrix-Game-3.5-Distilled).
- **Openness:** **Partial.** First-/third-person base and first-person causal weights released; full training/corpus not verified.
- **Independent audit:** [paper evidence and canonical split](independent-world-audit-2026-09-05.md).

### 12. Hunyuan-GameCraft: High-dynamic Interactive Game Video Generation with Hybrid History Condition

- **Year / venue / status:** 2025, research paper / technical report.
- **EN:** Keyboard/mouse-to-camera mapping and hybrid history conditioning generate autoregressive game video.
- **中文：** 键鼠到相机映射及混合历史条件实现自回归游戏视频生成。
- **Generates / action conditioning:** Keyboard/mouse-to-camera mapping and hybrid history conditioning generate autoregressive game video.
- **Evaluation:** FVD, visual/dynamic/temporal quality, camera RPE and preference; PCM 6.6 FPS versus base 0.25 FPS.
- **Official artifacts:** [paper](https://arxiv.org/abs/2506.17201), [full text](https://arxiv.org/html/2506.17201), [artifact 1](https://github.com/Tencent-Hunyuan/Hunyuan-GameCraft-1.0), [artifact 2](https://huggingface.co/tencent/Hunyuan-GameCraft-1.0).
- **Openness:** **Partial.** Inference, weights and Gradio demo public; full trainer/corpus unavailable.
- **Independent audit:** [paper evidence and canonical split](independent-world-audit-2026-09-05.md).

### 13. Hunyuan-GameCraft-2: Instruction-following Interactive Game World Model

- **Year / venue / status:** 2025, rev. 2026, research paper / technical report.
- **EN:** Instruction-conditioned interactions, autoregressive distillation and KV recaching enable multi-turn control.
- **中文：** 指令条件交互、自回归蒸馏与 KV 重缓存支持多轮控制。
- **Generates / action conditioning:** Instruction-conditioned interactions, autoregressive distillation and KV recaching enable multi-turn control.
- **Evaluation:** InterBench trigger/alignment/fluency/scope/end-state/physics and video/camera metrics; 16 FPS reported.
- **Official artifacts:** [paper](https://arxiv.org/abs/2511.23429), [full text](https://arxiv.org/html/2511.23429), [artifact 1](https://hunyuan-gamecraft-2.github.io/), [artifact 2](https://hunyuan.tencent.com/game/game-craft).
- **Openness:** **Closed.** No downloadable official code or checkpoint verified.
- **Independent audit:** [paper evidence and canonical split](independent-world-audit-2026-09-05.md).

### 14. Scalable Generative Game Engine

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Co-designs the generation algorithm and hardware execution path to move neural racing/platformer gameplay beyond low-resolution real-time generation.
- **中文：** 通过生成算法与硬件执行路径协同设计，把神经 racing/platformer gameplay 推进到更高分辨率实时生成。
- **Generates / action conditioning:** 720×480 racing and platformer frames conditioned on player actions, with a latency-oriented streaming pipeline.
- **Evaluation:** FPS, motion-to-photon latency and delay breakdown, FID/LPIPS, and control sensitivity; the paper reports 26.4 FPS racing, 48.3 FPS platformer, 2.7 ms amortized latency, PGG FID 28.5, and LPIPS 0.052.
- **Official artifacts:** [paper](https://arxiv.org/abs/2602.00608).
- **Openness:** **Closed.** No official project, repository, model, data, or evaluator was found by the cutoff.

### 15. Solaris — Building a Multiplayer Video World Model in Minecraft

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Generates synchronized Minecraft observations for two players so movement, building, memory, and shared-world consistency can be judged from multiple viewpoints.
- **中文：** 为两名玩家同步生成 Minecraft 观察，使移动、建造、记忆与共享世界的多视角一致性可以直接评测。
- **Generates / action conditioning:** two coordinated first-person streams from paired initial observations and each player's controls; the collection engine records synchronized video/action trajectories.
- **Evaluation:** held-out Movement, Grounding, Memory, Building, and cross-view Consistency episodes, FID, and an officially released VLM self-consistency metric.
- **Official artifacts:** [paper](https://arxiv.org/abs/2602.22208), [project](https://solaris-wm.github.io/), [training/inference/evaluation](https://github.com/solaris-wm/solaris), [collection engine](https://github.com/solaris-wm/solaris-engine), [model/data collections](https://huggingface.co/collections/nyu-visionx/solaris-models).
- **Openness:** **Open.** The trainer, GPU/TPU inference, weights, multiplayer data, and metric are public; full pretraining additionally depends on separately distributed VPT data.

### 16. MultiGen — Editable Multiplayer Worlds

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Adds editable top-down level structure and persistent external memory to a diffusion game engine, making multiplayer spaces reproducible instead of trapped in recent video context.
- **中文：** 为扩散游戏引擎加入可编辑俯视关卡结构与持久外部记忆，使多人空间可复现，而不只依赖短期视频上下文。
- **Generates / action conditioning:** consistent first-person views for multiple players; player actions update shared pose/map memory, which conditions each generated observation and supports encounters, death, and respawn.
- **Evaluation:** SSIM, PSNR, and LPIPS against simulator frames; VLM opponent-presence accuracy/precision/recall; context/memory ablations; approximately 20 FPS on one A100 per player.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.06679), [author project](https://ryanpo.com/multigen/).
- **Openness:** **Closed.** The paper and project demonstrations are public, but no official code, model, data, or evaluator is downloadable.

### 17. WorldCam — Interactive Autoregressive 3D Gaming Worlds

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Grounds immediate controls and long-term revisitation in one 6-DoF camera-pose representation to reduce geometric drift.
- **中文：** 用统一的 6-DoF 相机位姿同时约束即时操作与长期重访，降低交互游戏世界中的几何漂移。
- **Generates / action conditioning:** autoregressive first-person gaming video from an initial frame; keyboard/mouse controls update global camera pose, which retrieves relevant past observations.
- **Evaluation:** translation/rotation RPE, VBench++, PSNR/LPIPS/MEt3R/DINO similarity and sharpness, 200-frame tests, speed, and a blinded 30-person study.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.16871), [project](https://cvlab-kaist.github.io/WorldCam/), [official inference](https://github.com/cvlab-kaist/WorldCam), [official weights](https://huggingface.co/worldcam/worldcam), [open-game recordings](https://huggingface.co/datasets/worldcam/worldcam-dataset).
- **Openness:** **Partial.** A CS:GO-tuned checkpoint and inference are public, but training code and the paper's training corpus are not; the open Xonotic/Unvanquished recordings are a different release.

### 18. ActionParty — Multi-Subject Action Binding

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Extends action-conditioned video generation from one controllable subject to as many as seven, preserving which action belongs to which player.
- **中文：** 把动作条件视频从单一可控主体扩展到最多 7 名玩家，并保持每个动作与对应身份正确绑定。
- **Generates / action conditioning:** multiplayer Melting Pot video conditioned on subject-specific action streams; experiments span 46 games and 230 rollouts.
- **Evaluation:** Movement Accuracy, Effect Accuracy, PSNR, LPIPS, FVD, and subject/action identity binding; one reported setup reaches 87.2% movement accuracy and 91.3% detection.
- **Official artifacts:** [paper](https://arxiv.org/abs/2604.02330), [project](https://action-party.github.io/), [official repository](https://github.com/action-party/action-party).
- **Openness:** **Closed.** The repository states “Code coming soon” and provides no model, dataset, trainer, or evaluator.

### 19. SCOPE — Simulating Cross-game Operations

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Learns spatially selective responses to dense simultaneous FPS controls across seven games, separating local weapon effects from global movement/camera motion.
- **中文：** 在 7 款 FPS 上学习逐帧、可重叠的密集操作响应，把局部武器效果与全局移动/视角变化分开。
- **Generates / action conditioning:** 480×832, 81-frame clips from an initial image, prompt, and frame-aligned 10-DoF gamepad telemetry covering movement/look and six buttons.
- **Evaluation:** CrossFPS's 1,378 clips; dynamics/flow, photometric smoothness/depth, JEPA/FVD/LPIPS, action composition, scaling, and zero-shot scenes.
- **Official artifacts:** [paper](https://arxiv.org/abs/2605.23345), [project](https://z2tong.github.io/SCOPE/), [official inference](https://github.com/z2tong/SCOPE), [official weights](https://huggingface.co/zizhaotong/SCOPE), [CrossFPS collection](https://huggingface.co/collections/zizhaotong/crossfps).
- **Openness:** **Partial.** Checkpoint, inference examples, dependencies, and CrossFPS data are released, but training code is not.

### 20. MIRA — Multiplayer Interactive World Models

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Introduces a 5B representation-autoencoder world model for highly dynamic four-player Rocket League rather than treating other players as uncontrolled scenery.
- **中文：** 提出 5B representation-autoencoder 世界模型，同时建模 4 名 Rocket League 玩家，而非把其他玩家当作不可控背景。
- **Generates / action conditioning:** shared Rocket League video conditioned jointly on four players' control streams, trained on the 10K-hour Rocket Science corpus and run at about 20 FPS.
- **Evaluation:** per-player action response, multiplayer attribution and physical consistency, perceptual quality, real-time throughput, and stable recurrent rollouts demonstrated up to five minutes.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.05352), [project](https://mira-wm.com/), [official training/inference/evaluation repository](https://github.com/mira-wm/mira), [Rocket Science dataset](https://huggingface.co/datasets/kyutai/rocket-science).
- **Openness:** **Partial.** Training, inference, evaluation, and data are public, but no downloadable official model checkpoint was found; the live demo alone is not a reproducible weight release.

### 21. StatePlay — State-Aware Game World Models

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Jointly predicts video and explicit timers, health, and skill meters so fighting-game outcomes follow mechanics rather than only looking plausible.
- **中文：** 联合预测画面与计时、血量、能量槽等显式状态，使生成的格斗游戏结果遵守机制，而不只是视觉上像游戏。
- **Generates / action conditioning:** Street Fighter III video plus five state variables, conditioned on player movement/attack, prompt, initial frame, and the predicted state branch.
- **Evaluation:** SSIM/LPIPS, Move/Attack accuracy, normalized state distance/alignment, and Gemini/GPT mechanics fidelity on 100 held-out clips; average normalized state error is reported below 0.06.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.26754), [project](https://jimntu.github.io/stateplay_page/), [training/inference](https://github.com/Jimntu/StatePlay), [model](https://huggingface.co/onepiece1999/StatePlay), [dataset](https://huggingface.co/datasets/onepiece1999/StatePlay-Dataset).
- **Openness:** **Open.** Model, 10K-clip data, trainer, inference, and examples are public; VLM judging still depends on proprietary judge versions.

### 22. WanToFight — Real-Time Multi-Player Combat

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Generates full two-player The King of Fighters '97 matches from both players' keyboard input at consumer-GPU frame rates.
- **中文：** 根据两名玩家的键盘输入，以消费级 GPU 的实时帧率生成完整《拳皇 97》双人对局。
- **Generates / action conditioning:** 512×384 KOF '97 video jointly conditioned on both action streams; a player-association module targets the correct character and DMD/pruned decoding sustains 30 FPS on one RTX 5090.
- **Evaluation:** LPIPS, SSIM, DINOv2, action accuracy, VLM identity-binding consistency under asymmetric probes, full-match rollout, and runtime.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.12592), [project](https://humanaigc.github.io/wantofight/), [official repository](https://github.com/HumanAIGC/wantofight).
- **Openness:** **Closed.** The repository contains the project-page source/assets only; training/inference code, model, data, and evaluator are absent.

### 23. MASS — Multiplayer World Models with Authoritative Shared State

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Predicts one typed authoritative world state from joint actions, then renders any requested camera, avoiding inconsistent per-view latent worlds.
- **中文：** 根据联合动作预测一个类型化权威世界状态，再按需渲染任意相机，避免各视角 latent 世界相互冲突。
- **Generates / action conditioning:** recurrent shared state plus view-specific images for multiplayer Snake and declaratively described games; every player action advances the same state.
- **Evaluation:** LPIPS, field accuracy/full-state exact match, parser-based state recovery, cross-view agreement, structural validity, six-renderer reconstruction, and scale tests with 1,024 players over 10,000 ticks. MASS reports 0.76 state recovery and LPIPS 0.098 on the matched benchmark.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.06257), [project](https://alaya-lab.github.io/MASS/).
- **Openness:** **Closed.** No official code, weights, matched benchmark data, or evaluator are downloadable.

### 24. ForgeWM — Progressive Causal Training

- **Year / venue / status:** 2026, arXiv technical report.
- **EN:** Fully releases a four-stage recipe that turns a game-conditioned video generator into 1-, 2-, and 4-step real-time Minecraft/FPS world models.
- **中文：** 完整公开四阶段流程，把游戏动作条件视频生成器蒸馏成 1、2、4 步实时 Minecraft/FPS 世界模型。
- **Generates / action conditioning:** causal Minecraft video from an image and keyboard/mouse streams, plus a CrossFPS gamepad checkpoint; replay-time refinement improves saved trajectories.
- **Evaluation:** VBench, paired LPIPS/flow, keyboard sign-control and mouse accuracy, latency/FPS, replay fidelity, a 41-person study, and seven-game CrossFPS transfer.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.14022), [project](https://asdfo123.github.io/ForgeWM/), [full code](https://github.com/asdfo123/ForgeWM), [models](https://huggingface.co/ForgeWM/ForgeWM), [prepared data](https://huggingface.co/datasets/ForgeWM/ForgeWM-data).
- **Openness:** **Open.** Training/inference, stage 0–3 checkpoints, few-step students, CrossFPS checkpoint, and roughly 89 GB of prepared data are public; upstream licenses still apply.

### 25. Marionette — Predicting World States, Rendering Geometry, Painting Appearance

- **Year / venue / status:** 2026, arXiv preprint.
- **EN:** Predicts an explicit 276-D articulated multi-character state, renders geometry deterministically, then uses diffusion only to paint appearance.
- **中文：** 先预测 276 维多角色关节世界状态，再确定性渲染几何，最后只让扩散模型负责外观绘制。
- **Generates / action conditioning:** long-horizon character-game rollouts; action IDs drive state dynamics, fixed kinematics/collision/rasterization creates control video, and a conditioned model renders RGB.
- **Evaluation:** root-aligned joint error, character separation, ground penetration, rule-based repair, and observation FVD; the abstract reports 66% less penetration after explicit rules.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.14530), [project](https://alayalab.github.io/Marionette/), [official inference/runtime](https://github.com/AlayaLab/Marionette), [official weights](https://huggingface.co/AlayaLab/Marionette), [source WildWorld corpus](https://github.com/AlayaLab/WildWorld).
- **Openness:** **Partial.** The three-stage inference path, weights, and reproducibility seeds are public, but training code and the full 2,241-segment derived corpus are not; assets are research-only.

### 26. Playable Game Generation

- **Year / venue / status:** 2024, arXiv preprint.
- **EN:** Learns an action-conditioned latent-dynamics engine from game video and action data and emits real-time, player-controllable game frames.
- **中文：** 从游戏视频与动作数据学习动作条件 latent-dynamics 引擎，实时生成可由玩家控制的游戏画面。
- **Generates / action conditioning:** player actions advance an autoregressive learned game world step by step; the output is a playable visual experience rather than source code or a conventional engine project.
- **Evaluation:** visual fidelity, dynamics/action alignment, long-horizon consistency, and real-time playability experiments.
- **Official artifacts:** [paper](https://arxiv.org/abs/2412.00887), [official implementation](https://github.com/GreatX3/Playable-Game-Generation).
- **Openness:** **Partial.** Implementation material is public, but the complete training-data and reproduction path is not.
- **Strict-scope decision:** **KEEP.** The player controls the generated world directly, so this is an interactive-world generation method rather than a game-playing policy.

### 27. Learning to Simulate Dynamic Environments with GameGAN

- **Year / venue / status:** 2020, paper / technical report; targeted source and artifact check 2026-09-05.
- **EN:** Learns keyboard-conditioned Pac-Man/VizDoom transitions and next-screen generation, with external memory for revisited layouts.
- **中文：** 学习键盘控制的 Pac-Man/VizDoom 状态转移和下一帧生成，以外部记忆保持重访地图。
- **Generates / action conditioning:** Learns keyboard-conditioned Pac-Man/VizDoom transitions and next-screen generation, with external memory for revisited layouts.
- **Evaluation:** Rule/event behavior, simulator-transfer fidelity and come-back-home pixel consistency.
- **Primary-source evidence:** Figure 3 explicitly shows human play; project states all videos/GIFs are people playing the learned simulator. The neural dynamics engine, not an external conventional game engine, updates the generated state.
- **Official artifacts:** [paper](https://arxiv.org/abs/2005.12126), [full text](https://arxiv.org/html/2005.12126). [project](https://research.nvidia.com/labs/toronto-ai/gameGAN/), [training/data extraction](https://github.com/nv-tlabs/GameGAN_code); no pretrained weights or complete Pac-Man corpus found.
- **Openness:** **Partial.** Availability limitations are recorded above.

### 28. Playable Video Generation (CADDY)

- **Year / venue / status:** 2021, paper / technical report; targeted source and artifact check 2026-09-05.
- **EN:** Discovers discrete actions from unlabelled video and lets users control generated Atari Breakout and Tennis observations at every step.
- **中文：** 从无标注视频发现离散动作，让用户逐步控制生成的 Atari Breakout 与网球观察。
- **Generates / action conditioning:** Discovers discrete actions from unlabelled video and lets users control generated Atari Breakout and Tennis observations at every step.
- **Evaluation:** LPIPS/FID/FVD, action-space displacement prediction and human action-consistency judgments.
- **Primary-source evidence:** The paper defines a discrete action at every time step; the official Breakout live demo and README play/training commands establish game output. BAIR is an auxiliary robotics experiment, not a game.
- **Official artifacts:** [paper](https://arxiv.org/abs/2101.12195), [full text](https://arxiv.org/html/2101.12195). [project/live demos](https://willi-menapace.github.io/playable-video-generation-website/), [training/play/evaluation](https://github.com/willi-menapace/PlayableVideoGeneration); author-linked data/weights, with separate Tennis video acquisition.
- **Openness:** **Open.** Core implementation and meaningful reproduction artifacts are public; binaries were not executed in this audit.

### 29. Playable Environments: Video Manipulation in Space and Time

- **Year / venue / status:** 2022, paper / technical report; targeted source and artifact check 2026-09-05.
- **EN:** Generates Minecraft/Tennis scene states from user actions, independently controlling player movement and camera in 3D.
- **中文：** 按用户动作生成 Minecraft/网球场景状态，在三维空间中分别控制角色运动与相机。
- **Generates / action conditioning:** Generates Minecraft/Tennis scene states from user actions, independently controlling player movement and camera in 3D.
- **Evaluation:** LPIPS/FID/FVD, action Δ-MSE/Δ-Acc, camera manipulation, missing detections and a user study.
- **Primary-source evidence:** The paper evaluates one hour of two sparring Minecraft players plus Minecraft Camera and Tennis; its action module updates environment state before volumetric rendering. Official release contains play.py and three training phases, not only a renderer.
- **Official artifacts:** [paper](https://arxiv.org/abs/2203.01914), [full text](https://arxiv.org/html/2203.01914). [project](https://willi-menapace.github.io/playable-environments-website/), [training/play/evaluation](https://github.com/willi-menapace/PlayableEnvironments); author-linked Minecraft data/models and ReplayMod collection, with external game/video dependencies.
- **Openness:** **Open.** Core implementation and meaningful reproduction artifacts are public; binaries were not executed in this audit.

### 30. Model as a Game: On Numerical and Spatial Consistency for Generative Games

- **Year / venue / status:** 2025, paper / technical report; targeted source and artifact check 2026-09-05.
- **EN:** Adds LogicNet event triggers, explicit numerical records and map retrieval to action-conditioned Traveler, Pong and Pac-Man generation.
- **中文：** 将 LogicNet 事件触发、显式数值记录与地图检索集成进动作控制的 Traveler、Pong 和 Pac-Man 生成。
- **Generates / action conditioning:** Adds LogicNet event triggers, explicit numerical records and map retrieval to action-conditioned Traveler, Pong and Pac-Man generation.
- **Evaluation:** ActAcc, numerical-event F-measure (NumCon), spatial consistency, digit-rendering accuracy and runtime overhead.
- **Primary-source evidence:** Sections 3–4 propose and evaluate generator modules on three games. The action/numerical validators evaluate generated behavior; external arithmetic is an internal generator component, not a standalone repair task.
- **Official artifacts:** [paper](https://arxiv.org/abs/2503.21172), [full text](https://arxiv.org/html/2503.21172). Paper only; no official implementation, model or data release located.
- **Openness:** **Closed.** Availability limitations are recorded above.

### 31. Vid2World: Crafting Video Diffusion Models to Interactive World Models

- **Year / venue / status:** 2025, paper / technical report; targeted source and artifact check 2026-09-05.
- **EN:** Causalizes pretrained video diffusion for frame-aligned, action-controlled CS:GO generation; also studies separate robotics/navigation tracks.
- **中文：** 将预训练视频扩散模型因果化，生成与逐帧动作对齐的 CS:GO 画面；另含机器人/导航实验。
- **Generates / action conditioning:** Causalizes pretrained video diffusion for frame-aligned, action-controlled CS:GO generation; also studies separate robotics/navigation tracks.
- **Evaluation:** CS:GO FID/FVD/SSIM/PSNR/LPIPS/DreamSim versus DIAMOND, autoregressive rollouts and action-guidance ablations.
- **Primary-source evidence:** Section 5.2 and Appendix C.5 evaluate the game generator on four context frames followed by 12 predicted frames (16 total, not 16 predictions); the separate navigation setup uses four plus 16. The author release includes CSGO utilities and model_checkpoint_100000.ckpt; the substantive game track is distinct from downstream robot-policy evaluation.
- **Official artifacts:** [paper](https://arxiv.org/abs/2505.14357), [full text](https://arxiv.org/html/2505.14357). [project](https://knightnemo.github.io/vid2world/), [training/inference/evaluation](https://github.com/thuml/Vid2World), [CS:GO weights](https://huggingface.co/thuml/Vid2World-CSGO); game data preparation depends on separately obtained source data.
- **Openness:** **Open.** Core implementation and meaningful reproduction artifacts are public; binaries were not executed in this audit.

### 32. Advancing Open-source World Models (LingBot-World)

- **Year / venue / status:** 2026, paper / technical report; targeted source and artifact check 2026-09-05.
- **EN:** Generates first/third-person worlds under action/camera controls with minute-long context and a 16-FPS streaming model (480p on one GPU node, not a single GPU).
- **中文：** 按动作/相机控制生成第一、第三人称世界，支持分钟级上下文；快速版在单 GPU 节点（非单卡）以 480p 达到 16 FPS。
- **Generates / action conditioning:** Generates first/third-person worlds under action/camera controls with minute-long context and a 16-FPS streaming model (480p on one GPU node, not a single GPU).
- **Evaluation:** Visual dynamics, long-horizon consistency, action-conditioned comparisons and runtime/latency.
- **Primary-source evidence:** Paper describes synchronized native game controls and game RGB/camera collection, streaming action response under one second, and generated first/third-person worlds. The release contains action-to-camera and fast autoregressive scripts; weight-bearing model repositories were checked.
- **Official artifacts:** [paper](https://arxiv.org/abs/2601.20540), [full text](https://arxiv.org/html/2601.20540). [code](https://github.com/robbyant/lingbot-world), [base weights](https://huggingface.co/robbyant/lingbot-world-base-cam), [fast weights](https://huggingface.co/robbyant/lingbot-world-fast); inference is public, full trainer/corpus absent.
- **Openness:** **Partial.** Availability limitations are recorded above.

### 33. ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU

- **Year / venue / status:** 2026, paper / technical report; targeted source and artifact check 2026-09-05.
- **EN:** Uses frame-synchronous keyboard input and persistent character memory for generated world roaming and third-person character control.
- **中文：** 用逐帧键盘输入与持久角色记忆，实现生成世界漫游和第三人称角色控制。
- **Generates / action conditioning:** Uses frame-synchronous keyboard input and persistent character memory for generated world roaming and third-person character control.
- **Evaluation:** WorldRoamBench, long-rollout drift, LongForcing ablations; up to 16 FPS and 1.2-second input latency on one RTX 5090.
- **Primary-source evidence:** The paper defines observer-style roaming and actor-style character motion in a frame-synchronous keyboard interface trained on AAA games and other sources. Official Gradio client and safetensors establish an interactive release; FPS is throughput, not action latency.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.19191), [full text](https://arxiv.org/html/2607.19191). [code/demo](https://github.com/amap-cvlab/ABot-World), [weights](https://huggingface.co/acvlab/ABot-World-0-5B-LF), [500-hour data](https://huggingface.co/datasets/acvlab/ABot-World-Explorer-500h); full training/corpus equivalence is not established.
- **Openness:** **Partial.** Availability limitations are recorded above.

### 34. ReWorld: An Interactive World Model with Long-Horizon Memory

- **Year / venue / status:** 2026, paper / technical report; targeted source and artifact check 2026-09-05.
- **EN:** Streams action-driven game-style roaming worlds using bounded KV memory and a pose-indexed landmark bank.
- **中文：** 用有界 KV 记忆与按位姿检索的地标库，流式生成动作驱动的游戏风格漫游世界。
- **Generates / action conditioning:** Streams action-driven game-style roaming worlds using bounded KV memory and a pose-indexed landmark bank.
- **Evaluation:** Camera control against six baselines, seven VBench dimensions, 64-second revisits and cache/training ablations.
- **Primary-source evidence:** The paper explicitly generates game-style worlds with real-time input-driven continuation; its curated game source contains 18,387 roaming clips from 79 games. Scope is navigable interactive worlds, not generation of combat rules or one-shot camera clips.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.23565), [full text](https://arxiv.org/html/2608.23565). [project](https://zhifeichen097.github.io/ReWorld/); paper/videos only, without downloadable code, weights or data.
- **Openness:** **Closed.** Availability limitations are recorded above.

### 35. WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling

- **Year / venue / status:** 2025, paper / technical report; targeted source and artifact check 2026-09-05.
- **EN:** Uses dual keyboard/mouse–camera actions and reconstructed context memory for streaming first/third-person worlds and promptable events.
- **中文：** 以键鼠—相机双动作表示和重建上下文记忆，流式生成第一/第三人称世界及可提示事件。
- **Generates / action conditioning:** Uses dual keyboard/mouse–camera actions and reconstructed context memory for streaming first/third-person worlds and promptable events.
- **Evaluation:** Control error, VBench, revisit geometry/MEt3R, human study with 300 cases, 300 custom trajectories and 30 assessors (v2, June 2026) and 720p/24-FPS runtime.
- **Primary-source evidence:** Abstract and Section 3 specify instant visual feedback for streaming keyboard/mouse commands; qualitative evaluation explicitly extends third-person agent control, with real/stylized worlds and promptable events. This is a navigable generated game-world method, not the separately indexed PlayWorld benchmark.
- **Official artifacts:** [paper](https://arxiv.org/abs/2512.14614), [full text](https://arxiv.org/html/2512.14614). [code/training](https://github.com/Tencent-Hunyuan/HY-WorldPlay), [weights](https://huggingface.co/tencent/HY-WorldPlay), [project](https://3d-models.hunyuan.tencent.com/world/); full training corpus not released.
- **Openness:** **Partial.** Availability limitations are recorded above.

### 36. DreamX-World 1.0: A General-Purpose Interactive World Model

- **Year / venue / status:** 2026, paper / technical report; targeted source and artifact check 2026-09-05.
- **EN:** Generates real-time, first/third-person game-style worlds with navigation, camera-indexed revisits and composable text-triggered events.
- **中文：** 实时生成第一/第三人称游戏风格世界，支持导航、按相机位姿重访及可组合文本事件。
- **Generates / action conditioning:** Generates real-time, first/third-person game-style worlds with navigation, camera-indexed revisits and composable text-triggered events.
- **Evaluation:** Camera/visual scores, long-horizon drift, multilevel revisit consistency, human preference and up to 16 FPS on eight RTX 5090s.
- **Primary-source evidence:** Sections 3–4 turn a bidirectional model into a causal student using generated history and streaming controls; first/third-person game-style domains, WASD/IJKL actions and event instruction tuning establish live navigable interaction rather than only offline camera rendering.
- **Official artifacts:** [paper](https://arxiv.org/abs/2606.16993), [full text](https://arxiv.org/html/2606.16993). [project](https://amap-ml.github.io/DreamX_World/), [inference](https://github.com/AMAP-ML/DreamX-World), [5B model](https://huggingface.co/GD-ML/DreamX-World-5B), [5B-Cam model](https://huggingface.co/GD-ML/DreamX-World-5B-Cam); 5B is autoregressive; 5B-Cam is bidirectional and generates five-second clips; full 1.0 reproduction is not established.
- **Openness:** **Partial.** Availability limitations are recorded above.

### 37. Neural Game Engine: Accurate learning of generalizable forward models from pixels

- **Year / venue / status:** 2020, paper / technical report; targeted source and artifact check 2026-09-05.
- **EN:** Learns action-conditioned pixel/state transitions and rewards for GVGAI games, with directly keyboard-playable neural environments.
- **中文：** 学习 GVGAI 游戏的动作条件像素/状态转移与奖励，生成可直接用键盘游玩的神经环境。
- **Generates / action conditioning:** Learns action-conditioned pixel/state transitions and rewards for GVGAI games, with directly keyboard-playable neural environments.
- **Evaluation:** Ten-game pixel/tile/reward evaluation: 100 steps, three repeats (Table II); separately Sokoban grid extrapolation up to 100×100: 500 steps, ten repeats (Table I); gating ablations.
- **Primary-source evidence:** Full paper Sections III–V define and evaluate a learned simulator, with policy/planning only downstream applications. Official README explicitly maps W/A/S/D/space to play.py and enumerates ten pretrained game environments. Negative rewards and hidden nonvisual state are documented limitations.
- **Official artifacts:** [paper](https://arxiv.org/abs/2003.10520), [full text](https://arxiv.org/pdf/2003.10520). [training/play/pretrained models](https://github.com/Bam4d/Neural-Game-Engine); requires the author's GVGAI Gym dependency. Stochastic/hidden-state dynamics remain limited.
- **Openness:** **Open.** Core implementation and meaningful reproduction artifacts are public; binaries were not executed in this audit.

### 38. Yume: An Interactive World Generation Model

- **Year / venue / status:** 2025, arXiv paper; targeted primary-source check 2026-09-05.
- **EN:** Quantized keyboard/camera control, masked autoregressive diffusion and memory generate explorable worlds; explicit video-game generalization.
- **中文：** 用量化键盘/相机控制、掩码自回归扩散与记忆生成可探索世界；明确展示电子游戏泛化。
- **Generates / action conditioning:** Quantized keyboard/camera control, masked autoregressive diffusion and memory generate explorable worlds; explicit video-game generalization.
- **Evaluation:** 70-input Yume-Bench control/visual scores, Wan/MatrixGame comparisons, 18-second rollouts and sampler/distillation ablations; game evidence is qualitative.
- **Primary-source evidence:** Full text §5.5.1 explicitly demonstrates generalization to video-game imagery despite real-world training. Fig. 1 and §§4.2/5 specify continuous keyboard control and history-conditioned autoregressive generation. The quantitative 70-input benchmark is predominantly real-world, so game-specific results must not be inferred from its aggregate scores. Actual original 14B weight shards and training/inference scripts were verified; later Yume-1.5 is a distinct paper.
- **Official artifacts:** [paper](https://arxiv.org/abs/2507.17744), [full text](https://arxiv.org/html/2507.17744). [training/inference](https://github.com/stdstu12/YUME), [14B/540p weights](https://huggingface.co/stdstu123/Yume-I2V-540P); processed corpus and complete matched evaluator not verified.
- **Openness:** **Partial.** See the availability limitations above; no full reproduction was run.
- **Detailed audit:** [Second-pass discovery](further-world-discovery-2026-09-05.md).

### 39. SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer

- **Year / venue / status:** 2026, arXiv paper; targeted primary-source check 2026-09-05.
- **EN:** Hybrid GDN/softmax and 6-DoF camera conditioning generate minute-scale worlds, including game-style scenes; chunk-causal/distilled variants support sequential rollout.
- **中文：** 用 GDN/softmax 混合架构及 6-DoF 相机条件生成分钟级世界，含游戏风格场景；分块因果/蒸馏变体支持逐步续生成。
- **Generates / action conditioning:** Hybrid GDN/softmax and 6-DoF camera conditioning generate minute-scale worlds, including game-style scenes; chunk-causal/distilled variants support sequential rollout.
- **Evaluation:** 80 scenes per Simple/Hard split, including 20 game-style scenes; 60-second camera, VBench and revisit tests, separate bidirectional/AR comparison.
- **Primary-source evidence:** Full text §5.2 and Appendix D explicitly include 20 game-style scenes among 80, with Simple/Hard revisit trajectories. §§1/3.1 and Table 9 establish and separately evaluate chunk-causal generation, not merely an offline bidirectional clip. Current streaming release contains causal DiT/refiner/VAE components; its CLI takes camera arrays, and a live keyboard front end was not independently demonstrated. The 34-second RTX-5090 claim is 60-second-clip denoising time, not input latency.
- **Official artifacts:** [paper](https://arxiv.org/abs/2605.15178), [full text](https://arxiv.org/html/2605.15178). [code](https://github.com/NVlabs/Sana), [WM docs](https://nvlabs.github.io/Sana/docs/sana_wm/), [streaming weights](https://huggingface.co/Efficient-Large-Model/SANA-WM_streaming); Stage-1 training released, full matched pipeline/corpus not verified.
- **Openness:** **Partial.** See the availability limitations above; no full reproduction was run.
- **Detailed audit:** [Second-pass discovery](further-world-discovery-2026-09-05.md).

### 40. Wonder: Video World Model Done Better

- **Year / venue / status:** 2026, arXiv paper; targeted primary-source check 2026-09-05.
- **EN:** Camera-controlled image/video-to-world generation, including gaming scenes, with sparse memory and a few-step causal student.
- **中文：** 以相机控制从图像/视频生成世界，包含游戏场景，并用稀疏记忆和少步因果学生持续生成。
- **Generates / action conditioning:** Camera-controlled image/video-to-world generation, including gaming scenes, with sparse memory and a few-step causal student.
- **Evaluation:** 1,000-image/five-trajectory and 500-video/six-trajectory benchmarks; visual/RPE metrics, revisit memory and claimed native 16 FPS.
- **Primary-source evidence:** Full text §5.1 explicitly includes gaming scenes among 1,000 initial images, each with five trajectories; §5.2 tests 500 dynamic videos with six trajectories each. §4 distinguishes the noninteractive bidirectional teacher from a sparse-memory causal student and resident streaming runtime. Project code/Hugging Face buttons remain coming soon. Website playback is interpolated from native 16 to 32 FPS; 32 H200s is training hardware, not verified inference hardware.
- **Official artifacts:** [paper](https://arxiv.org/abs/2607.26037), [full text](https://arxiv.org/html/2607.26037). [project](https://wonder-world-model.github.io/); code/weights remain coming soon, no downloadable official reproduction package verified.
- **Openness:** **Closed.** See the availability limitations above; no full reproduction was run.
- **Detailed audit:** [Second-pass discovery](further-world-discovery-2026-09-05.md).

### 41. Unbounded: A Generative Infinite Game of Character Life Simulation

- **Year / venue / status:** 2024, arXiv paper; targeted primary-source check 2026-09-05.
- **EN:** Natural-language player input drives a distilled LLM life-simulator's environment, character and four state meters, coupled to consistent scene images.
- **中文：** 玩家自然语言输入驱动蒸馏 LLM 生活模拟器，更新环境、角色与四项状态，并联动生成一致场景图像。
- **Generates / action conditioning:** Natural-language player input drives a distilled LLM life-simulator's environment, character and four state meters, coupled to consistent scene images.
- **Evaluation:** 100 five-round interaction samples with GPT-4 pairwise judging; 5,000 visual triplets, character/environment consistency and distillation ablations.
- **Primary-source evidence:** Full text §3.3 specifies a player-input-driven life-sim: natural-language actions change environment/character descriptions and hunger, energy, fun and hygiene states, which condition scene images. §4.1 evaluates 100 five-round interaction samples; Table 3 compares distilled Gemma-2B game-engine outputs using GPT-4 judging. This evaluates an integrated generated world, not an isolated NPC policy or visual asset. Judged state-update quality is not proof of arbitrary rule invention or exact numeric correctness.
- **Official artifacts:** [paper](https://arxiv.org/abs/2410.18975), [full text](https://arxiv.org/html/2410.18975). [project](https://generative-infinite-game.github.io/); no downloadable official code, models or data verified.
- **Openness:** **Closed.** See the availability limitations above; no full reproduction was run.
- **Detailed audit:** [Second-pass discovery](further-world-discovery-2026-09-05.md).

## Generation benchmarks / 生成 Benchmark

### 42. WildWorld / WildBench

- **Year / venue / status:** 2026, arXiv dataset/benchmark preprint.
- **EN:** Builds a large action/state-aligned ARPG corpus and a benchmark that directly checks whether generated worlds follow actions and preserve explicit state.
- **中文：** 构建大规模动作/状态对齐 ARPG 语料，并直接评测生成世界是否遵循动作、保持显式状态。
- **Generation/action task:** 108M frames with 450+ actions and 119 annotations support action-conditioned video/state modeling; WildBench targets Action Following and State Alignment rather than policy return.
- **Evaluation:** benchmark construction and validation include human agreement (85% reported) and coordinate-level accuracy (43.23% reported), alongside the two generation axes.
- **Official artifacts:** [paper](https://arxiv.org/abs/2603.23497), [correct author project](https://alaya-studio.github.io/wildworld-project/), [official repository](https://github.com/AlayaLab/WildWorld), [official dataset](https://huggingface.co/datasets/AlayaLab/WildWorld).
- **Openness:** **Partial.** Gated Part 1 currently exposes 574 hours, 3,434 samples, and 13,740 files; Parts 2/3 and WildBench code are pending. The older `shandaai.github.io` URL in the arXiv comment was unavailable at the cutoff.

### 43. PlayWorld

- **Year / venue / status:** 2026, arXiv benchmark preprint.
- **EN:** Uses agent players as test probes that pursue long-horizon objectives inside a generated world; it evaluates the world model, not whether a new game-playing policy is strong.
- **中文：** 让 agent player 在生成世界内执行长时目标，把它作为测试探针；评分对象是世界模型，而不是新玩家策略的强弱。
- **Generation/action task:** 171 interactive scenarios exercise generated-world geometry, interactions, insight evolution, visible evolution, and out-of-sight evolution.
- **Evaluation:** scenario execution plus geometry, interaction, insight-evolution, and world-evolution judging; the benchmark packages prompts, assets, runners, and leaderboard logic.
- **Official artifacts:** [paper](https://arxiv.org/abs/2608.13552), [project](https://kxding.github.io/project/PlayWorld/), [official code](https://github.com/hku-sail/PlayWorld), [official benchmark data](https://huggingface.co/datasets/jocelynd/playworld-bench), [official leaderboard](https://huggingface.co/spaces/jocelynd/PlayWorld-Leaderboard).
- **Openness:** **Open.** Code, 178-file benchmark data, and evaluator/leaderboard assets are public; full execution and judging still depend on proprietary world services plus Claude/Gemini APIs.

### 44. WorldMark: A Unified Benchmark Suite for Interactive Video World Models

- **Year / venue / status:** 2026, paper / technical report; targeted source and artifact check 2026-09-05.
- **EN:** Defines shared key programs and per-model adapters for comparing ten interactive world generators across 500 cases.
- **中文：** 定义统一按键程序与模型适配器，在 500 个案例上比较十个交互世界生成器。
- **Generates / action conditioning:** Defines shared key programs and per-model adapters for comparing ten interactive world generators across 500 cases.
- **Evaluation:** Per-axis action direction/purity, response latency, motion stability, memory and visual quality over first/third-person worlds.
- **Primary-source evidence:** The paper defines 15 W/S/A/D/L/R programs, a standardized input set and empirical generator comparison including game-world models. The official repository has arena_inputs, generation and evaluation. Model scores assess generated worlds, not player policies.
- **Official artifacts:** [paper](https://arxiv.org/abs/2604.21686), [full text](https://arxiv.org/html/2604.21686). [project](https://alayalab.github.io/WorldMark/), [inputs/generation/evaluation](https://github.com/AlayaLab/WorldMark); external generators require their own installations.
- **Openness:** **Open.** Core implementation and meaningful reproduction artifacts are public; binaries were not executed in this audit.

### 45. WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models

- **Year / venue / status:** 2026, paper / technical report; targeted source and artifact check 2026-09-05.
- **EN:** Benchmarks 600+ first/third-person generated-world navigation cases using 10–60-second WASD/IJKL programs.
- **中文：** 以 10–60 秒 WASD/IJKL 程序评测 600 多个第一/第三人称生成世界漫游案例。
- **Generates / action conditioning:** Benchmarks 600+ first/third-person generated-world navigation cases using 10–60-second WASD/IJKL programs.
- **Evaluation:** Per-frame action following, visual drift, controllability-gated interaction physics and scene/subject memory; ten models.
- **Primary-source evidence:** Full paper provides cases, control adapters and empirical comparison including Matrix-Game and interactive commercial worlds, satisfying benchmark-role requirements. The page's hidden fallback text was misleading: its JavaScript configures a live ZIP download. HTTP Range inspection verified 1,006 action.json/image pairs (648 action/vision, 211 memory, 147 physics), distinct from the paper's 600+ cases; no Python evaluators were present in the archive. See the independent audit note.
- **Official artifacts:** [paper](https://arxiv.org/abs/2606.31672), [full text](https://arxiv.org/html/2606.31672). [project/leaderboard](https://worldroam.amap.com), [released inputs ZIP](https://amap-cvlab.oss-cn-zhangjiakou.aliyuncs.com/worldroambench/worldroam.zip); verified 1,006 action/image pairs; evaluator code not verified.
- **Openness:** **Partial.** Availability limitations are recorded above.
