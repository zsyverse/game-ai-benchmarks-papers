# Game-generation repository QA recheck

- Audit date: **2026-08-29 (Asia/Shanghai)**
- Audited tree: local `main` at `260ef1c9685a18d3baf0a52b29dd41b471c15075`
- Remote comparison target: `origin/main`
- Mutation policy: existing files were read only; this report is the sole file created by this audit.
- Overall verdict: **FAIL (one definite status inconsistency; one additional label ambiguity).** Repository structure, bilingual parity, counts, syntax, relative links, remote/public metadata, legacy-path removal, and external-link reachability otherwise pass.

> **Resolution (2026-09-01):** This report audits base commit `260ef1c`. The ScriptDoctor and Playable Game Generation labels were normalized, all scope/source findings were addressed, later historical, benchmark, and final generation-only passes brought the index to 198 records, and automated bilingual/count/link validation was added. The original FAIL result remains below as historical evidence, not the current repository verdict.

Current post-resolution validation parses **50 end-to-end + 115 PCG + 33 interactive-world = 198** English records with exact Chinese row/URL parity and **505 unique HTTPS external URLs**. `scripts/validate_index.py` also checks section/README counts, complete numbered source headings, table widths, relative links, and removal of the legacy playing-only collection.

## Result summary

| Check | Result | Exact evidence |
| --- | --- | --- |
| Local `main` vs remote `main` | PASS | `git rev-parse HEAD` and `git ls-remote origin refs/heads/main` both returned `260ef1c9685a18d3baf0a52b29dd41b471c15075`. |
| GitHub visibility and metadata | PASS | `visibility=PUBLIC`, `isPrivate=false`, default branch `main`, not archived, not a fork; description and ten relevant topics are populated. |
| English/Chinese records and order | PASS | `29/29`, `35/35`, and `18/18` records; paired primary-source URL order is exactly equal in every collection. |
| English/Chinese external-link parity | PASS | README `25/25`, end-to-end `71/71`, PCG `73/73`, interactive worlds `83/83`; every paired sequence is exactly equal, not merely set-equal. |
| README claim: 82 category records | PASS | `29 + 35 + 18 = 82` English records, mirrored by 82 Chinese records. |
| README claim: more than 200 links | PASS | 202 unique external URLs in the English public index; 203 unique external URLs across all tracked Markdown. |
| Markdown, YAML, and JSON | PASS | Markdownlint: 14 tracked Markdown files, zero issues; PyYAML parsed the issue form; Python JSON parser parsed `.markdownlint.json`. |
| Relative links | PASS | 64 relative-link occurrences resolved; zero missing targets. |
| Table widths and identifiers | PASS with ordering note | 32 table blocks and 281 table lines have consistent widths. Numbered collections have complete, unique ID sets `1..29` and `1..35`, although display order is category-driven rather than ascending. |
| External HTTP reachability | PASS with known access restrictions | 203 unique URLs: 180 returned `200`, 15 returned `202`, one returned `401`, seven returned `403`; `000=0`, `404=0`, `410=0`, `429=0`. |
| Legacy game-agent paths | PASS | No current `HEAD` path contains a game-agent/playing collection. Three legacy files exist only as deleted history entries. |
| Duplicate/status consistency | FAIL | ScriptDoctor is `Closed for paper reproduction` in end-to-end but `Partial` in PCG for the same paper and artifact facts. |

## Git and GitHub metadata

The local checkout was clean when the audit began and reported `## main...origin/main`. Read-only remote resolution produced the same object ID as local `HEAD`:

```text
local HEAD:  260ef1c9685a18d3baf0a52b29dd41b471c15075
remote main: 260ef1c9685a18d3baf0a52b29dd41b471c15075
```

`gh repo view zsyverse/game-ai-benchmarks-papers` returned:

- visibility: `PUBLIC` (`isPrivate=false`);
- default branch: `main`;
- description: `Bilingual papers and benchmarks for AI game generation: end-to-end game/code, automated design, PCG, and interactive worlds | AI 游戏生成论文与基准`;
- topics: `benchmarks`, `game-ai`, `papers`, `procedural-content-generation`, `game-development`, `game-generation`, `generative-ai`, `text-to-game`, `world-models`, `automated-game-design`;
- `isArchived=false`, `isFork=false`.

`git fsck --no-dangling --no-reflogs`, `git diff --check`, and the initial working-tree status all passed without output.

## Bilingual parity and record counts

The audit parsed Markdown table data rows rather than trusting section headings.

| Collection | EN rows | ZH rows | Actual subsection counts | Entry columns | External-link occurrences per language | Exact external-link order |
| --- | ---: | ---: | --- | ---: | ---: | --- |
| End-to-end | 29 | 29 | `10 + 13 + 5 + 1` | 7 | 71 | Equal |
| Automated design / PCG | 35 | 35 | `15 + 15 + 2 + 3` | 7 | 73 | Equal |
| Interactive worlds | 18 | 18 | `8 + 8 + 2` | 5 | 83 | Equal |
| README | n/a | n/a | n/a | n/a | 25 | Equal |

For all three collections:

- English and Chinese row counts match.
- The first external URL in each paired row matches at the same ordinal position.
- The complete external URL sequence matches at every position.
- The section totals match the headings and both README files.

The 82-record claim is therefore exact: `29 + 35 + 18 = 82`. Those 82 records resolve to 75 distinct primary-work URLs because seven works are deliberately represented twice as benchmark/system or cross-collection records. This is consistent with the README's explicit “intentional cross-listing” qualification.

The link claim is also reproducible under two conservative definitions:

- `README.md` plus the three English collection pages contain **252 external-link occurrences and 202 unique external URLs**.
- All 14 Markdown files tracked at audited `HEAD` contain **732 external-link occurrences and 203 unique external URLs**.
- All 203 unique external URLs use HTTPS.

Thus “more than 200 links to papers and official artifacts” is true even without double-counting the Chinese mirror.

## Tables, numbering, relative links, and syntax

All 32 Markdown table blocks were checked row-by-row: 281 table lines have the same column width as their respective header block. In particular, every end-to-end and PCG record has seven cells, and every interactive-world record has five.

Numbering integrity passes:

- End-to-end contains 29 unique identifiers with range `1..29`, no gaps, no duplicates.
- PCG contains 35 unique identifiers with range `1..35`, no gaps, no duplicates.
- Chinese identifier order is byte-for-byte equivalent to the English identifier order.

The presentation is intentionally not numerically monotonic because rows are grouped by category. Exact display orders are:

```text
end-to-end: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,17,18,19,20,21,22,23,24,26,15,16,25,27,28,29
pcg:         1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,9,34,35
```

This is not a parity or uniqueness failure, but readers expecting ID sort order may find it surprising.

Syntax and local navigation evidence:

- `markdownlint-cli2 v0.23.2` / `markdownlint v0.41.1`: 14 tracked Markdown files, zero issues.
- `.markdownlint.json`: valid JSON.
- `.github/ISSUE_TEMPLATE/resource.yml`: valid YAML mapping with required top-level keys and seven unique body IDs (`scope`, `type`, `title`, `source`, `evidence`, `links`, `scope_check`).
- 64 Markdown relative-link occurrences: zero nonexistent resolved paths.

## External-link audit

Method: extract the 203 unique Markdown `http(s)` targets from tracked files, follow redirects with a browser-like user agent, issue `HEAD`, and recheck every exception or `>=400` result with a streamed `GET`. No body downloads were required beyond one streamed byte. Final results:

| Final HTTP result | Count | Interpretation |
| ---: | ---: | --- |
| `200` | 180 | Reachable |
| `202` | 15 | Reachable/accepted |
| `401` | 1 | Known unavailable model location |
| `403` | 7 | ACM automated-access denial after a valid DOI redirect |
| `000` | 0 | No transport/DNS/TLS/time-out failure |
| `404` | 0 | No not-found response |
| `410` | 0 | No gone response |
| `429` | 0 | No rate-limit response |

The single `401` is `https://huggingface.co/microsoft/mineworld`. This is not an unacknowledged surprise: `docs/en/interactive-worlds.md:18` and `docs/zh-CN/interactive-worlds.md:18` explicitly state that the MineWorld checkpoint was removed while inference/evaluation code remains public.

All seven `403` results are DOI links that first returned `302` from `doi.org` and then `403` from `dl.acm.org` for automated requests:

```text
10.1145/2282338.2282347
10.1145/3102071.3110566
10.1145/3205455.3205517
10.1145/3235765.3235820
10.1145/3582437.3587211
10.1145/3706598.3714233
10.1145/3723498.3723794
```

Each DOI independently returned `200` from Crossref's official `works/{doi}` registration endpoint. These are therefore classified as known publisher access restrictions, not broken DOI registrations.

## Legacy game-agent path check

`git ls-tree -r --name-only HEAD` contains no path matching `game-agent`, `game_agent`, `agent` collection naming, or `playing` collection naming. The previous paths are deleted from the current tree:

```text
docs/en/game-agents.md
docs/zh-CN/game-agents.md
research/game-agent-sources.md
```

They remain visible only in Git history: commit `dde6e71b54a6694137ea9dd2183b3b293019a4a5` added them, and audited commit `260ef1c9685a18d3baf0a52b29dd41b471c15075` deleted them. Current mentions of DQN, AlphaGo, Voyager, BALROG, MineRL, DIAMOND, Dreamer, GameWAM, and similar playing work occur in explicit exclusion/boundary text (`README.md:54-62`, `SCOPE.md:20-34`, `docs/en/interactive-worlds.md:42-49`, and `docs/en/pcg.md:66-70`), not as included game-agent records.

## Duplicate and status-consistency audit

There are seven duplicated primary-work URLs among the 82 English category records:

| Primary work | Locations | Status pair | Assessment |
| --- | --- | --- | --- |
| `arXiv:2604.18394` OpenGame/OpenGame-Bench | `docs/en/end-to-end.md:20`, `:35` | `Partial` / `Partial` | Consistent |
| `arXiv:2605.28258` PlaytestArena/Play2Code | `docs/en/end-to-end.md:21`, `:38` | `Partial` / `Partial` | Consistent |
| `arXiv:2603.07106` PlayGen-20/AutoUE | `docs/en/end-to-end.md:22`, `:40` | `Open, environment-heavy` / same | Consistent |
| `arXiv:2404.08706` Game Generation via LLMs | `docs/en/end-to-end.md:28`, `docs/en/pcg.md:25` | `Closed` / `Paper-only` | Semantically consistent because `README.md:70` defines `Closed / Paper-only` together |
| `arXiv:2407.09388` GAVEL | `docs/en/end-to-end.md:30`, `docs/en/pcg.md:23` | `Open` / `Open` | Consistent |
| `arXiv:2506.06524` ScriptDoctor | `docs/en/end-to-end.md:32`, `docs/en/pcg.md:26` | `Closed for paper reproduction` / `Partial` | **Inconsistent** |
| ACL 2025 EMNLP main 1511 Cardiverse | `docs/en/end-to-end.md:33`, `docs/en/pcg.md:27` | `Open` / `Open` | Consistent |

The same facts and inconsistency are mirrored in the Chinese files at the same line numbers, so bilingual parity is intact while cross-collection semantics are not.

### Definite defect: ScriptDoctor

`docs/en/end-to-end.md:32` says no ScriptDoctor/corpus release was verified and assigns **Closed for paper reproduction**. `docs/en/pcg.md:26` reports the same missing ScriptDoctor code and corpus but assigns **Partial** solely because the upstream PuzzleScript runtime is open. The upstream runtime is not a released ScriptDoctor implementation, task set, output corpus, or evaluator. Under the repository's own definition in `README.md:68-72`, both records should use one consistent top-level availability classification. Chinese lines `docs/zh-CN/end-to-end.md:32` and `docs/zh-CN/pcg.md:26` reproduce the discrepancy.

### Additional ambiguity: Playable Game Generation

`docs/en/end-to-end.md:60` and its Chinese mirror use the single bold label **Partial/Open for the learned-engine pipeline**. This combines two mutually different top-level labels without separating which artifact is Open and which is Partial. The following prose mentions training-data reproducibility, but the leading classification remains ambiguous under `README.md:68-72`. A fully normalized index should choose one top-level label and leave the component-level nuance after the dash.

Other composite labels inspected in PCG and interactive worlds explicitly separate scopes or versions (for example, open dataset vs partial benchmark, or Hunyuan 1.0 vs 2.0) and were not treated as contradictions.

## Required change for a clean pass

Normalize ScriptDoctor to the same availability status in both collections, based on whether upstream PuzzleScript alone qualifies as a meaningful official artifact of the paper. Also normalize the Playable Game Generation leading label to one of `Open`, `Partial`, or `Closed / Paper-only`, preserving details in the explanatory text. No other blocking QA defect was found.
