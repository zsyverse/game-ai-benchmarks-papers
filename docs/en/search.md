# Search the collection

[Home](../../README.md) · [中文](../zh-CN/search.md) · [All papers](paper-list.md) · [Research guide](research-guide.md)

Search all three collections with Python 3.10+ from the repository root. No dependencies, network access or separate database are required: results are read directly from the bilingual Markdown tables.

## Examples

```bash
python3 scripts/search_index.py Godot --status Open
python3 scripts/search_index.py --category interactive-worlds --year 2026
python3 scripts/search_index.py "reinforcement learning" --category pcg
python3 scripts/search_index.py --lang zh-CN --json
```

## Options

| Option | Behavior |
| --- | --- |
| Keywords | Match text across both languages, regardless of the output language. All supplied keywords must match; quote a phrase to keep it together. Matching is case-insensitive and normalizes Unicode. |
| `--category` | Restrict results to `end-to-end`, `pcg` or `interactive-worlds`. |
| `--status` | Match `Open`, `Partial` or `Closed`; see the interpretation notes below. |
| `--year` | Match a year explicitly listed in the record, including revision years. |
| `--lang` | Choose `en` (default) or `zh-CN` for output descriptions and source locations; this does not restrict the search language. |
| `--json` | Print structured JSON instead of the compact text results. With no filters, export the whole index. |
| `--help` | Show the command's built-in help. |

Combine keywords and filters to narrow results. With no keywords or filters, the command returns every record.

## Reading results

Text results contain the record ID, title, listed years, artifact labels, primary paper link and source file/line. Open that source row for task descriptions, evaluation details and artifact caveats.

JSON results also include the complete title-cell links (`paper_urls`), descriptive cells (`details`), artifact Markdown with its links (`artifacts`), and the source dossier path (`evidence`). The source file and line identify the full public record; the dossier uses the same category and record number.

IDs such as `pcg:12` refer to current category/row numbers, not permanent paper identifiers. They may change after reordering. Use the primary paper URL when you need a durable reference.

## Interpreting filters

- **Years:** a record can list multiple years, such as an initial release and a revision. A match does not mean that every associated artifact was released or verified in that year.
- **Artifact labels:** filters match any version's label. A record marked `Partial / Closed` matches either `--status Partial` or `--status Closed`. Read its artifact cell to distinguish versions.
- **Availability:** `Open` does not mean an unrestricted license, a turnkey setup or independently successful reproduction. Labels describe the verified official release; see the [label definitions](../../README.md#artifact-labels).

## Finding benchmarks

Use the benchmark sections in [end-to-end generation](end-to-end.md#1-generation-benchmarks-10) and [interactive worlds](interactive-worlds.md#2-interactive-world-generation-benchmarks-4). PCG mixes methods and benchmarks; check each row's task and evaluation columns in the [PCG collection](pcg.md).

The [research guide](research-guide.md) compares evaluation setups. For hands-on work, the [experimental entry points](../../research/experiment-entry-points-2026-09-08.md) retain installation requirements and pinned artifact evidence; they are setup recommendations, not reproduction reports.
