# Further executable-game discovery — 2026-09-05

This pass starts from the corrected 37-record end-to-end index, not the earlier uncorrected expansion. It searches title/abstract variants of game generation, game development, code generation, program synthesis and generating games, then follows primary full texts and official releases. Mathematical game-theory results, already indexed identities, playing policies and ordinary development studies are not counted as discoveries. No third-party implementation was executed.

## Accepted: ByteSized32 (2023)

Primary sources: [EMNLP 2023 paper](https://aclanthology.org/2023.emnlp-main.830/), [full text](https://arxiv.org/html/2305.14879), [official code](https://github.com/cognitiveailab/BYTESIZED32).

- **Scope evidence, §3/Figures 2–3:** generated Python implements objects, valid actions, `step`, score, and win/loss state. The paper proposes a generation challenge and empirically evaluates generated programs, not merely a corpus or a benchmark of game-playing agents.
- **Actual task count, §5.2–5.3:** 32 reference games, **16 unseen task specifications**, six reference pairings per target, **96 generated games**. The corpus name is not the number of evaluation tasks.
- **Generation, §5:** single-reference GPT-4-32k in-context generation with greedy decoding; up to three iterations of interpreter-feedback reflection. Reflection is internal to full-game generation, not a standalone repair-only task.
- **Technical validity, §4/Table 2:** a bounded three-step trajectory crawl with action subsampling. Runtime pass rises **28.1%→57.3%**, not a guarantee over all trajectories or long playthroughs.
- **Human winnability, §4/Table 3:** **30.2%→37.5%**, separately measured across the 96 generated games. GPT-4 winnability labels agree poorly with humans (**κ=0.43**), so the paper reports human evaluation. An unsuccessful search for a solution does not prove it impossible.
- **Negative results, §6:** action compliance stays 93.8%, distractor compliance falls 21.9%→18.8%; automatic physical-alignment gain partly reflects fewer invalid outputs. Excluding zero scores reduces that gain from eight to four points. Do not summarize reflection as improving every semantic dimension.
- **Artifact verification:** retrieved official README, recursive repository manifest and `bytes32/validity.py`. The release includes programs, test prompts, pairing CSVs, generation/reflection/evaluation scripts and saved outputs. The validity code resets the game for a bounded DFS, subsamples actions, and uses Unix `SIGALRM`; no code was run. **Open**, but historical OpenAI model/API access and platform-specific timeout behavior affect replay.

Inserted as a generation benchmark in the bilingual end-to-end index. The collection becomes 38 records: ten benchmarks and 28 methods. Current source-dossier IDs were renumbered to match; older research notes retain historical snapshot references.

## Cross-track accepted lead: Unbounded (2024)

Primary sources: [full text](https://arxiv.org/html/2410.18975), [official project](https://generative-infinite-game.github.io/).

Sections 3.3–4.1 establish a turn-based language/image life simulator: player inputs change environments, actions and hunger/energy/fun/hygiene state, and those outputs condition subsequent images. Five-round simulator/user trajectories train a distilled Gemma-2B engine; the held-out LLM evaluation uses 100 five-round trajectories, with GPT-4 pairwise scoring of state updates, environment relevance, story coherence and instruction following (Table 3). This is evaluated interactive-world generation, not just NPC prose or isolated images. It does not establish arbitrary rule invention or deterministic state correctness.

An independent world-track reviewer confirmed the same scope interpretation. The official page provides the paper and demonstrations but no verified author implementation, model weights or data download. The paper's AI-tamago link is a baseline, and the website's Nerfies repository link is its page template, not the Unbounded release. Use **Closed** for unverified core release; do not mistake commented “Data (Coming Soon)” markup for the active download state. Canonical integration is in the world collection only; detailed evidence is in the [world discovery note](further-world-discovery-2026-09-05.md).

## Screened but not counted

| Candidate | Primary evidence inspected | Decision |
| --- | --- | --- |
| ChatGPT and Other Large Language Models as Evolutionary Engines for Online Interactive Collaborative Game Design, 2023 | [Full text](https://arxiv.org/html/2303.02155), §4–5: evolutionary operations act on textual concepts; Telegram participants score ideas and brainstorm during a game jam. | Exclude concept-only authoring. Human discussion of mechanics is not an automatically executable rule generator. |
| Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models, 2026 | [Full text](https://arxiv.org/html/2608.25518), §§5–6 and Appendix A: real pilot experiments on asset classification/generation, edits and cross-engine transfer; gameplay-agent integration is identified as a next step. | Hold for demonstrated qualifying playable-output task. Do not call it experiment-free, but do not convert asset-quality or embodied-policy improvements into evidence of complete game generation. |
| Mazocarta, 2026 | [Full text](https://arxiv.org/html/2605.08319), §§1/4/6: instrumented deterministic game rules, reusable simulation, tests and QR/WebRTC networking are stated contributions. | Exclude infrastructure/QA-oriented reference artifact. A game containing seeded content does not automatically make its paper a substantive generator study. |
| Large Language Models in Game Development: Implications for Gameplay, Playability, and Player Experience, 2026 | [Full text](https://arxiv.org/html/2603.27896), §§2–4: two game projects serve a collaborative autoethnographic investigation of developer experiences. | Exclude analytical experience study from the method/benchmark count; retain as contextual reading if needed. No new generator benchmark is established. |
| GameGen-Verifier, 2026 | [Primary abstract](https://arxiv.org/abs/2605.07442) and existing strict audit: runtime-state injection and bounded keypoint verification of generated games. | Retain previous verifier-only exclusion; this pass adds no new contradictory generation evidence. |
| From Pixels to States, 2026 | [Primary abstract](https://arxiv.org/abs/2607.14076): organizing analysis of world models plus 90-hour action/state/video data engine. | Do not count a survey/resource as a generator. Useful for citation discovery, but no newly established formal generation task in the inspected evidence. |

## Coverage limit

Finding ByteSized32 shows that keyword saturation in the earlier search did not establish completeness. Titles containing “corpus” can still define a qualifying benchmark; titles containing “game development” may not. This pass does not claim every title/venue was inspected, that all historical canonical relationships are settled, or that any reported result was independently reproduced.
