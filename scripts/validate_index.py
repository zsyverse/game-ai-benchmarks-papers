#!/usr/bin/env python3
"""Validate bilingual records, source coverage, counts, links, and tables."""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = (
    ("docs/en/end-to-end.md", "docs/zh-CN/end-to-end.md", "numbered"),
    ("docs/en/pcg.md", "docs/zh-CN/pcg.md", "numbered"),
    ("docs/en/interactive-worlds.md", "docs/zh-CN/interactive-worlds.md", "year"),
)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
YEAR_RE = re.compile(r"^20\d{2}(?:\s*(?:[-/–]|to)\s*20?\d{2})?$")
SECTION_COUNT_RE = re.compile(r"(?:\((\d+)(?:[^)]*)\)|（(\d+)(?:[^）]*)）)\s*$")
INTERNAL_LABEL_RE = re.compile(r"\bP[01]\b|omission[ -]audit|漏项审计", re.IGNORECASE)
SOURCE_HEADING_RE = re.compile(r"^### (\d+)\.", re.MULTILINE)
STATUS_RE = re.compile(r"\b(Open|Partial|Closed|Paper-only by design)\b")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def markdown_links(text: str) -> list[str]:
    return [match.group(1).strip().strip("<>") for match in LINK_RE.finditer(text)]


def external_urls(text: str) -> list[str]:
    return [url for url in markdown_links(text) if url.startswith(("https://", "http://"))]


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def record_ids(text: str, kind: str) -> list[int | str]:
    records: list[int | str] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = table_cells(line)
        if not cells:
            continue
        first = cells[0]
        if kind == "numbered" and first.isdigit():
            records.append(int(first))
        elif kind == "year" and YEAR_RE.fullmatch(first):
            records.append(first)
    return records


def record_rows(text: str, kind: str) -> list[tuple[int, list[str]]]:
    rows: list[tuple[int, list[str]]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.startswith("|"):
            continue
        cells = table_cells(line)
        if not cells:
            continue
        first = cells[0]
        if (kind == "numbered" and first.isdigit()) or (
            kind == "year" and YEAR_RE.fullmatch(first)
        ):
            rows.append((line_number, cells))
    return rows


def primary_title(cells: list[str], kind: str) -> str:
    title_cell = cells[2] if kind == "numbered" else cells[1]
    match = re.search(r"\[([^]]+)\]\(", title_cell)
    if not match:
        return ""
    title = unicodedata.normalize("NFKC", match.group(1))
    return re.sub(r"\s*([()])\s*", r"\1", title).strip()


def year_signature(cells: list[str], kind: str) -> tuple[str, ...]:
    year_cell = cells[1] if kind == "numbered" else cells[0]
    return tuple(re.findall(r"\d{4}", year_cell))


def status_label(cells: list[str]) -> str:
    match = STATUS_RE.search(cells[-1])
    return match.group(1) if match else ""


def section_record_groups(text: str, kind: str) -> list[list[int | str]]:
    lines = text.splitlines()
    headings = [index for index, line in enumerate(lines) if line.startswith("## ")]
    groups: list[list[int | str]] = []
    for position, start in enumerate(headings):
        if not SECTION_COUNT_RE.search(lines[start]):
            continue
        end = headings[position + 1] if position + 1 < len(headings) else len(lines)
        groups.append(record_ids("\n".join(lines[start + 1 : end]), kind))
    return groups


def validate_table_widths(path: Path, text: str, errors: list[str]) -> None:
    block: list[tuple[int, str]] = []

    def check(current: list[tuple[int, str]]) -> None:
        if len(current) < 2:
            return
        expected = len(table_cells(current[0][1]))
        for line_number, line in current[1:]:
            actual = len(table_cells(line))
            if actual != expected:
                fail(
                    f"{path.relative_to(ROOT)}:{line_number}: table has {actual} cells; expected {expected}",
                    errors,
                )

    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.startswith("|"):
            block.append((line_number, line))
        else:
            check(block)
            block = []
    check(block)


def validate_section_counts(path: Path, text: str, kind: str, errors: list[str]) -> None:
    """Check the count declared at the end of each numbered H2 heading."""
    lines = text.splitlines()
    headings = [index for index, line in enumerate(lines) if line.startswith("## ")]
    for position, start in enumerate(headings):
        match = SECTION_COUNT_RE.search(lines[start])
        if not match:
            continue
        expected = int(match.group(1) or match.group(2))
        end = headings[position + 1] if position + 1 < len(headings) else len(lines)
        actual = len(record_ids("\n".join(lines[start + 1 : end]), kind))
        if actual != expected:
            fail(
                f"{path.relative_to(ROOT)}:{start + 1}: section claims {expected} records; found {actual}",
                errors,
            )


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def claimed_count(readme: str, target: str) -> int | None:
    pattern = re.compile(rf"\[(\d+)[^\]]*\]\({re.escape(target)}\)")
    match = pattern.search(readme)
    return int(match.group(1)) if match else None


def main() -> int:
    errors: list[str] = []
    counts: dict[str, int] = {}

    for en_name, zh_name, kind in COLLECTIONS:
        en_text = read(en_name)
        zh_text = read(zh_name)
        en_records = record_ids(en_text, kind)
        zh_records = record_ids(zh_text, kind)
        en_rows = record_rows(en_text, kind)
        zh_rows = record_rows(zh_text, kind)
        counts[en_name] = len(en_records)

        if len(en_records) != len(zh_records):
            fail(f"record-count mismatch: {en_name}={len(en_records)}, {zh_name}={len(zh_records)}", errors)
        if kind == "numbered":
            expected = list(range(1, len(en_records) + 1))
            if sorted(en_records) != expected:
                fail(f"{en_name}: IDs are not a complete unique 1..{len(en_records)} set", errors)
            if en_records != zh_records:
                fail(f"number/order mismatch: {en_name} vs {zh_name}", errors)

        if section_record_groups(en_text, kind) != section_record_groups(zh_text, kind):
            fail(f"section-membership mismatch: {en_name} vs {zh_name}", errors)

        for position, ((en_line, en_cells), (zh_line, zh_cells)) in enumerate(
            zip(en_rows, zh_rows), start=1
        ):
            en_title = primary_title(en_cells, kind)
            zh_title = primary_title(zh_cells, kind)
            if not en_title or not zh_title:
                fail(
                    f"missing primary linked title at record {position}: "
                    f"{en_name}:{en_line} or {zh_name}:{zh_line}",
                    errors,
                )
            elif en_title != zh_title:
                fail(
                    f"title mismatch at record {position}: {en_name}:{en_line} vs {zh_name}:{zh_line}",
                    errors,
                )

            if year_signature(en_cells, kind) != year_signature(zh_cells, kind):
                fail(
                    f"year mismatch at record {position}: {en_name}:{en_line} vs {zh_name}:{zh_line}",
                    errors,
                )

            en_status = status_label(en_cells)
            zh_status = status_label(zh_cells)
            if not en_status or not zh_status:
                fail(
                    f"missing availability status at record {position}: "
                    f"{en_name}:{en_line} or {zh_name}:{zh_line}",
                    errors,
                )
            elif en_status != zh_status:
                fail(
                    f"availability-status mismatch at record {position}: "
                    f"{en_name}:{en_line} vs {zh_name}:{zh_line}",
                    errors,
                )

        en_urls = external_urls(en_text)
        zh_urls = external_urls(zh_text)
        if en_urls != zh_urls:
            limit = min(len(en_urls), len(zh_urls))
            first = next((index for index in range(limit) if en_urls[index] != zh_urls[index]), limit)
            fail(
                f"external-URL parity mismatch: {en_name} vs {zh_name} at index {first} "
                f"({len(en_urls)} vs {len(zh_urls)} URLs)",
                errors,
            )

        validate_table_widths(ROOT / en_name, en_text, errors)
        validate_table_widths(ROOT / zh_name, zh_text, errors)
        validate_section_counts(ROOT / en_name, en_text, kind, errors)
        validate_section_counts(ROOT / zh_name, zh_text, kind, errors)

        for path, text in ((ROOT / en_name, en_text), (ROOT / zh_name, zh_text)):
            match = INTERNAL_LABEL_RE.search(text)
            if match:
                line_number = text.count("\n", 0, match.start()) + 1
                fail(
                    f"{path.relative_to(ROOT)}:{line_number}: internal audit label leaked into public index: "
                    f"{match.group(0)}",
                    errors,
                )

    readme_en = read("README.md")
    readme_zh = read("README.zh-CN.md")
    if external_urls(readme_en) != external_urls(readme_zh):
        fail("external-URL parity mismatch: README.md vs README.zh-CN.md", errors)

    en_date = re.search(r"Last fully verified: \*\*(\d{4}-\d{2}-\d{2})\*\*", readme_en)
    zh_date = re.search(r"最近一次完整核验：\*\*(\d{4}-\d{2}-\d{2})\*\*", readme_zh)
    if not en_date or not zh_date or en_date.group(1) != zh_date.group(1):
        fail("README verification-date parity mismatch", errors)

    for en_name, zh_name, _ in COLLECTIONS:
        actual = counts[en_name]
        for readme, target, label in (
            (readme_en, en_name, "README.md"),
            (readme_zh, zh_name, "README.zh-CN.md"),
        ):
            claim = claimed_count(readme, target)
            if claim is None:
                fail(f"{label}: no linked count found for {target}", errors)
            elif claim != actual:
                fail(f"{label}: claims {claim} for {target}; actual count is {actual}", errors)

    total = sum(counts.values())
    en_total = re.search(r"\*\*(\d+) detailed category records\*\*", readme_en)
    zh_total = re.search(r"\*\*(\d+) 条详细分类记录\*\*", readme_zh)
    for match, label in ((en_total, "README.md"), (zh_total, "README.zh-CN.md")):
        if not match:
            fail(f"{label}: total record claim not found", errors)
        elif int(match.group(1)) != total:
            fail(f"{label}: claims {match.group(1)} total records; actual count is {total}", errors)

    source_notes = (
        ("research/end-to-end-generation-sources.md", "docs/en/end-to-end.md"),
        ("research/pcg-automated-design-sources.md", "docs/en/pcg.md"),
        ("research/interactive-world-generation-sources.md", "docs/en/interactive-worlds.md"),
    )
    for source_name, collection_name in source_notes:
        source_ids = [
            int(match.group(1)) for match in SOURCE_HEADING_RE.finditer(read(source_name))
        ]
        expected_sources = list(range(1, counts[collection_name] + 1))
        if source_ids != expected_sources:
            fail(
                f"{source_name}: numbered source headings must be the complete ordered "
                f"1..{counts[collection_name]} set",
                errors,
            )

    markdown_files = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
    all_external: set[str] = set()
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        validate_table_widths(path, text, errors)
        for target in markdown_links(text):
            if target.startswith(("https://", "http://")):
                all_external.add(target)
                if target.startswith("http://"):
                    fail(f"{path.relative_to(ROOT)}: non-HTTPS external link: {target}", errors)
                continue
            if target.startswith(("#", "mailto:", "data:")):
                continue
            relative = unquote(target.split("#", 1)[0])
            if relative and not (path.parent / relative).resolve().exists():
                fail(f"{path.relative_to(ROOT)}: missing relative link target: {target}", errors)

    en_link_claim = re.search(r"more than \*\*(\d+) links", readme_en)
    zh_link_claim = re.search(r"\*\*(\d+) 多个[^*]*链接\*\*", readme_zh)
    if not en_link_claim or not zh_link_claim:
        fail("README external-link claim not found", errors)
    elif en_link_claim.group(1) != zh_link_claim.group(1):
        fail("README external-link claim parity mismatch", errors)
    elif len(all_external) <= int(en_link_claim.group(1)):
        fail(
            f"README claims more than {en_link_claim.group(1)} external links; "
            f"only {len(all_external)} unique URLs found",
            errors,
        )

    legacy = [
        ROOT / "docs/en/game-agents.md",
        ROOT / "docs/zh-CN/game-agents.md",
        ROOT / "research/game-agent-sources.md",
    ]
    for path in legacy:
        if path.exists():
            fail(f"legacy playing-only path exists: {path.relative_to(ROOT)}", errors)

    if errors:
        print("Index validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Index validation passed: "
        + ", ".join(f"{Path(name).stem}={count}" for name, count in counts.items())
        + f", total={total}, unique_external_urls={len(all_external)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
