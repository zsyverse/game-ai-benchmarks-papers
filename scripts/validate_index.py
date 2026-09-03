#!/usr/bin/env python3
"""Validate strict scope structure, bilingual parity, evidence, and deduplication."""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = (
    (
        "docs/en/end-to-end.md",
        "docs/zh-CN/end-to-end.md",
        "research/end-to-end-generation-sources.md",
        39,
        (10, 29),
    ),
    (
        "docs/en/pcg.md",
        "docs/zh-CN/pcg.md",
        "research/pcg-automated-design-sources.md",
        89,
        (13, 76),
    ),
    (
        "docs/en/interactive-worlds.md",
        "docs/zh-CN/interactive-worlds.md",
        "research/interactive-world-generation-sources.md",
        23,
        (21, 2),
    ),
)
EXPECTED_TOTAL = 151
EXPECTED_SECTION_HEADINGS = {
    "docs/en/end-to-end.md": (
        "## 1. Generation benchmarks (10)",
        "## 2. Generation methods (29)",
    ),
    "docs/zh-CN/end-to-end.md": (
        "## 1. 生成 Benchmark（10 条）",
        "## 2. 生成方法（29 条）",
    ),
    "docs/en/pcg.md": (
        "## 1. Complete-game, rule, and mechanic generation methods (13)",
        "## 2. Level/playable-content methods and generation benchmarks (76)",
    ),
    "docs/zh-CN/pcg.md": (
        "## 1. 完整游戏、规则与机制生成方法（13 条）",
        "## 2. 关卡/可玩内容生成方法与 Benchmark（76 条）",
    ),
    "docs/en/interactive-worlds.md": (
        "## 1. Interactive-world generation methods (21)",
        "## 2. Interactive-world generation benchmarks (2)",
    ),
    "docs/zh-CN/interactive-worlds.md": (
        "## 1. 交互世界生成方法（21 条）",
        "## 2. 交互世界生成 Benchmark（2 条）",
    ),
}

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SECTION_COUNT_RE = re.compile(r"(?:\((\d+)(?:[^)]*)\)|（(\d+)(?:[^）]*)）)\s*$")
INTERNAL_LABEL_RE = re.compile(r"\bP[01]\b|omission[ -]audit|漏项审计", re.IGNORECASE)
STATUS_RE = re.compile(r"\b(Open|Partial|Closed)\b")
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/([^?#]+)", re.IGNORECASE)
DOI_RE = re.compile(
    r"(?:doi\.org/|/doi/(?:abs/|full/|pdf/)?)(10\.[^?#]+)",
    re.IGNORECASE,
)
DOSSIER_HEADING_RE = re.compile(r"^### (\d+)\.\s+(.+)$")
BANNED_COUNTED_HEADING_RE = re.compile(
    r"dataset|corpus|survey|taxonomy|boundary|framing|adjacent|"
    r"repair|infrastructure|component.only|数据集|语料|综述|分类|"
    r"边界|邻接|修复|基础设施|组件",
    re.IGNORECASE,
)


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def markdown_links(text: str) -> list[str]:
    return [match.group(1).strip().strip("<>") for match in LINK_RE.finditer(text)]


def external_urls(text: str) -> list[str]:
    return [url for url in markdown_links(text) if url.startswith(("https://", "http://"))]


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def record_ids(text: str) -> list[int]:
    records: list[int] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        current = table_cells(line)
        if current and current[0].isdigit():
            records.append(int(current[0]))
    return records


def record_rows(text: str) -> list[tuple[int, list[str]]]:
    rows: list[tuple[int, list[str]]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.startswith("|"):
            continue
        current = table_cells(line)
        if current and current[0].isdigit():
            rows.append((line_number, current))
    return rows


def primary_title(cells: list[str]) -> str:
    match = re.search(r"\[([^]]+)\]\(", cells[2])
    if not match:
        return ""
    title = unicodedata.normalize("NFKC", match.group(1))
    return re.sub(r"\s*([()])\s*", r"\1", title).strip()


def title_key(title: str) -> str:
    normalized = unicodedata.normalize("NFKC", title).casefold()
    return "".join(character for character in normalized if character.isalnum())


def year_signature(cells: list[str]) -> tuple[str, ...]:
    return tuple(re.findall(r"\d{4}", cells[1]))


def status_label(cells: list[str]) -> str:
    match = STATUS_RE.search(cells[-1])
    return match.group(1) if match else ""


def normalize_url(url: str) -> str:
    parsed = urlsplit(unquote(url))
    path = parsed.path.rstrip("/")
    return urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), path, parsed.query, ""))


def strong_identity_keys(text: str) -> set[str]:
    """Extract arXiv and DOI identities, including publisher DOI URL forms."""
    keys: set[str] = set()
    for url in external_urls(text):
        arxiv = ARXIV_RE.search(url)
        if arxiv:
            identifier = re.sub(r"\.pdf$", "", arxiv.group(1), flags=re.IGNORECASE)
            identifier = re.sub(r"v\d+$", "", identifier, flags=re.IGNORECASE)
            keys.add(f"arxiv:{identifier.casefold()}")
        doi = DOI_RE.search(url)
        if doi:
            keys.add(f"doi:{doi.group(1).rstrip('/').casefold()}")
    return keys


def paper_identity_keys(title_cell: str) -> set[str]:
    """Return canonical paper keys without treating artifact links as papers."""
    urls = external_urls(title_cell)
    keys = strong_identity_keys(title_cell)
    if urls:
        keys.add(f"url:{normalize_url(urls[0])}")
    return keys


def source_identity_keys(text: str) -> set[str]:
    keys = strong_identity_keys(text)
    for url in external_urls(text):
        keys.add(f"url:{normalize_url(url)}")
    return keys


def dossier_blocks(text: str) -> list[tuple[int, int, str, str]]:
    """Return (line, id, title, body) for every numbered evidence block."""
    lines = text.splitlines()
    blocks: list[tuple[int, int, str, str]] = []
    for start, line in enumerate(lines):
        match = DOSSIER_HEADING_RE.fullmatch(line)
        if not match:
            continue
        end = start + 1
        while end < len(lines) and not lines[end].startswith(("## ", "### ")):
            end += 1
        blocks.append(
            (
                start + 1,
                int(match.group(1)),
                match.group(2),
                "\n".join(lines[start + 1 : end]),
            )
        )
    return blocks


def section_record_groups(text: str) -> list[list[int]]:
    lines = text.splitlines()
    headings = [index for index, line in enumerate(lines) if line.startswith("## ")]
    groups: list[list[int]] = []
    for position, start in enumerate(headings):
        if not SECTION_COUNT_RE.search(lines[start]):
            continue
        end = headings[position + 1] if position + 1 < len(headings) else len(lines)
        groups.append(record_ids("\n".join(lines[start + 1 : end])))
    return groups


def counted_section_claims(text: str) -> tuple[int, ...]:
    claims: list[int] = []
    for line in text.splitlines():
        if not line.startswith("## "):
            continue
        match = SECTION_COUNT_RE.search(line)
        if match:
            claims.append(int(match.group(1) or match.group(2)))
    return tuple(claims)


def counted_section_headings(text: str) -> tuple[str, ...]:
    return tuple(
        line
        for line in text.splitlines()
        if line.startswith("## ") and SECTION_COUNT_RE.search(line)
    )


def backtick_tags(text: str) -> tuple[str, ...]:
    return tuple(re.findall(r"`([^`]+)`", text))


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
                    f"{path.relative_to(ROOT)}:{line_number}: table has "
                    f"{actual} cells; expected {expected}",
                    errors,
                )

    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.startswith("|"):
            block.append((line_number, line))
        else:
            check(block)
            block = []
    check(block)


def validate_section_counts(path: Path, text: str, errors: list[str]) -> None:
    lines = text.splitlines()
    headings = [index for index, line in enumerate(lines) if line.startswith("## ")]
    for position, start in enumerate(headings):
        match = SECTION_COUNT_RE.search(lines[start])
        if not match:
            continue
        if BANNED_COUNTED_HEADING_RE.search(lines[start]):
            fail(
                f"{path.relative_to(ROOT)}:{start + 1}: out-of-scope counted section: "
                f"{lines[start]}",
                errors,
            )
        expected = int(match.group(1) or match.group(2))
        end = headings[position + 1] if position + 1 < len(headings) else len(lines)
        actual = len(record_ids("\n".join(lines[start + 1 : end])))
        if actual != expected:
            fail(
                f"{path.relative_to(ROOT)}:{start + 1}: section claims "
                f"{expected} records; found {actual}",
                errors,
            )


def claimed_count(readme: str, target: str) -> int | None:
    match = re.search(rf"\[(\d+)[^\]]*\]\({re.escape(target)}\)", readme)
    return int(match.group(1)) if match else None


def validate_dossier(
    source_name: str,
    rows: list[tuple[int, list[str]]],
    expected_count: int,
    seen_strong_identities: dict[str, tuple[str, int, str]],
    errors: list[str],
) -> None:
    text = read(source_name)
    blocks = dossier_blocks(text)
    block_ids = [block[1] for block in blocks]
    expected_ids = list(range(1, expected_count + 1))
    if block_ids != expected_ids:
        fail(
            f"{source_name}: evidence blocks are not the ordered unique set "
            f"1..{expected_count}",
            errors,
        )
    if f"**{expected_count} canonical records**" not in text:
        fail(f"{source_name}: English dossier count claim is missing or stale", errors)
    if f"**{expected_count} 条 canonical 记录**" not in text:
        fail(f"{source_name}: Chinese dossier count claim is missing or stale", errors)

    blocks_by_id = {block[1]: block for block in blocks}
    for _, cells in rows:
        public_id = int(cells[0])
        block = blocks_by_id.get(public_id)
        if block is None:
            continue
        source_line, _, source_title, body = block
        public_title = primary_title(cells)
        if title_key(source_title) != title_key(public_title):
            fail(
                f"{source_name}:{source_line}: evidence title '{source_title}' "
                f"does not match public #{public_id} '{public_title}'",
                errors,
            )
        public_identities = paper_identity_keys(cells[2])
        evidence_identities = source_identity_keys(body)
        if not public_identities or not public_identities.intersection(evidence_identities):
            fail(
                f"{source_name}:{source_line}: evidence block for public "
                f"#{public_id} '{public_title}' lacks its paper identity",
                errors,
            )
        for identity in strong_identity_keys(body):
            previous = seen_strong_identities.get(identity)
            if previous:
                fail(
                    f"duplicate evidence paper identity {identity}: "
                    f"{source_name}:{source_line} '{source_title}' matches "
                    f"{previous[0]}:{previous[1]} '{previous[2]}'",
                    errors,
                )
            else:
                seen_strong_identities[identity] = (
                    source_name,
                    source_line,
                    source_title,
                )


def validate_canonical_uniqueness(
    records: list[tuple[str, int, list[str]]], errors: list[str]
) -> None:
    seen_titles: dict[str, tuple[str, int, str]] = {}
    seen_identities: dict[str, tuple[str, int, str]] = {}
    for path, line_number, cells in records:
        title = primary_title(cells)
        normalized_title = title_key(title)
        previous = seen_titles.get(normalized_title)
        if previous:
            fail(
                f"duplicate canonical title: {path}:{line_number} '{title}' "
                f"matches {previous[0]}:{previous[1]} '{previous[2]}'",
                errors,
            )
        else:
            seen_titles[normalized_title] = (path, line_number, title)

        for identity in paper_identity_keys(cells[2]):
            previous = seen_identities.get(identity)
            if previous:
                fail(
                    f"duplicate canonical paper identity {identity}: "
                    f"{path}:{line_number} '{title}' matches "
                    f"{previous[0]}:{previous[1]} '{previous[2]}'",
                    errors,
                )
            else:
                seen_identities[identity] = (path, line_number, title)


def issue_form_fields(text: str) -> list[tuple[str, str]]:
    """Extract real issue-form field blocks; YAML comments cannot spoof these."""
    lines = text.splitlines()
    starts: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        match = re.fullmatch(r"    id: ([a-z][a-z0-9_]*)", line)
        if match:
            starts.append((index, match.group(1)))
    fields: list[tuple[str, str]] = []
    for position, (start, identifier) in enumerate(starts):
        end = starts[position + 1][0] if position + 1 < len(starts) else len(lines)
        fields.append((identifier, "\n".join(lines[start:end])))
    return fields


def issue_form_options(block: str) -> tuple[str, ...]:
    lines = block.splitlines()
    try:
        start = lines.index("      options:") + 1
    except ValueError:
        return ()
    options: list[str] = []
    for line in lines[start:]:
        if not line.startswith("        "):
            break
        match = re.fullmatch(r"        - (?!label:)(.+)", line)
        if match:
            options.append(match.group(1))
    return tuple(options)


def validate_issue_template(text: str, errors: list[str]) -> None:
    fields = issue_form_fields(text)
    field_ids = tuple(identifier for identifier, _ in fields)
    expected_ids = (
        "role",
        "scope",
        "title",
        "source",
        "generation_evidence",
        "evaluation",
        "artifacts",
        "availability",
        "scope_check",
    )
    if field_ids != expected_ids:
        fail(
            f"issue template field schema mismatch: expected {expected_ids}, "
            f"found {field_ids}",
            errors,
        )
    blocks = dict(fields)
    expected_options = {
        "role": (
            "Generation method paper / 生成方法论文",
            "Generation benchmark paper / 生成 Benchmark 论文",
        ),
        "scope": (
            "Complete runnable game / 完整可运行游戏",
            "Executable code or engine project / 可执行代码或引擎工程",
            "Executable rules or mechanics / 可执行规则或机制",
            "Playable level, map, task, or chart / 可玩关卡、地图、任务或谱面",
            "Player-controllable generated game world / 玩家可控制的生成式游戏世界",
        ),
        "availability": (
            "Open / 核心工件已公开",
            "Partial / 仅部分工件公开",
            "Closed / 未核验到可运行核心发布",
        ),
    }
    for identifier, expected in expected_options.items():
        actual = issue_form_options(blocks.get(identifier, ""))
        if actual != expected:
            fail(
                f"issue template {identifier}.options mismatch: "
                f"expected {expected}, found {actual}",
                errors,
            )
    for identifier in (
        "role",
        "scope",
        "title",
        "source",
        "generation_evidence",
        "evaluation",
        "availability",
    ):
        if "      required: true" not in blocks.get(identifier, ""):
            fail(f"issue template field '{identifier}' is not required", errors)
    if blocks.get("scope_check", "").count("          required: true") != 4:
        fail("issue template must require all four scope/duplicate confirmations", errors)


def main() -> int:
    errors: list[str] = []
    counts: dict[str, int] = {}
    english_records: list[tuple[str, int, list[str]]] = []
    seen_evidence_strong: dict[str, tuple[str, int, str]] = {}

    for en_name, zh_name, source_name, expected_count, expected_sections in COLLECTIONS:
        en_text = read(en_name)
        zh_text = read(zh_name)
        en_records = record_ids(en_text)
        zh_records = record_ids(zh_text)
        en_rows = record_rows(en_text)
        zh_rows = record_rows(zh_text)
        counts[en_name] = len(en_records)
        english_records.extend((en_name, line, cells) for line, cells in en_rows)

        if f"**{expected_count} canonical records**" not in en_text:
            fail(f"{en_name}: lead canonical-record count is missing or stale", errors)
        if f"**{expected_count} 条 canonical 记录**" not in zh_text:
            fail(f"{zh_name}: lead canonical-record count is missing or stale", errors)

        if len(en_records) != expected_count:
            fail(f"{en_name}: expected {expected_count} records; found {len(en_records)}", errors)
        if len(zh_records) != expected_count:
            fail(f"{zh_name}: expected {expected_count} records; found {len(zh_records)}", errors)

        expected_ids = list(range(1, expected_count + 1))
        if en_records != expected_ids:
            fail(f"{en_name}: IDs are not the ordered unique set 1..{expected_count}", errors)
        if zh_records != expected_ids:
            fail(f"{zh_name}: IDs are not the ordered unique set 1..{expected_count}", errors)
        if en_records != zh_records:
            fail(f"number/order mismatch: {en_name} vs {zh_name}", errors)

        en_sections = counted_section_claims(en_text)
        zh_sections = counted_section_claims(zh_text)
        if en_sections != expected_sections:
            fail(f"{en_name}: expected section counts {expected_sections}; found {en_sections}", errors)
        if zh_sections != expected_sections:
            fail(f"{zh_name}: expected section counts {expected_sections}; found {zh_sections}", errors)
        if counted_section_headings(en_text) != EXPECTED_SECTION_HEADINGS[en_name]:
            fail(f"{en_name}: counted section headings do not match the strict schema", errors)
        if counted_section_headings(zh_text) != EXPECTED_SECTION_HEADINGS[zh_name]:
            fail(f"{zh_name}: counted section headings do not match the strict schema", errors)
        if section_record_groups(en_text) != section_record_groups(zh_text):
            fail(f"section-membership mismatch: {en_name} vs {zh_name}", errors)

        for position, ((en_line, en_cells), (zh_line, zh_cells)) in enumerate(
            zip(en_rows, zh_rows), start=1
        ):
            en_title = primary_title(en_cells)
            zh_title = primary_title(zh_cells)
            if not en_title or not zh_title:
                fail(
                    f"missing primary linked title at record {position}: "
                    f"{en_name}:{en_line} or {zh_name}:{zh_line}",
                    errors,
                )
            elif en_title != zh_title:
                fail(
                    f"title mismatch at record {position}: "
                    f"{en_name}:{en_line} vs {zh_name}:{zh_line}",
                    errors,
                )

            if year_signature(en_cells) != year_signature(zh_cells):
                fail(
                    f"year mismatch at record {position}: "
                    f"{en_name}:{en_line} vs {zh_name}:{zh_line}",
                    errors,
                )

            if external_urls(" | ".join(en_cells)) != external_urls(" | ".join(zh_cells)):
                fail(
                    f"row-local URL mismatch at record {position}: "
                    f"{en_name}:{en_line} vs {zh_name}:{zh_line}",
                    errors,
                )
            if backtick_tags(en_cells[3]) != backtick_tags(zh_cells[3]):
                fail(
                    f"machine-readable output-tag mismatch at record {position}: "
                    f"{en_name}:{en_line} vs {zh_name}:{zh_line}",
                    errors,
                )

            en_status = status_label(en_cells)
            zh_status = status_label(zh_cells)
            if not en_status or not zh_status:
                fail(
                    f"missing Open/Partial/Closed status at record {position}: "
                    f"{en_name}:{en_line} or {zh_name}:{zh_line}",
                    errors,
                )
            elif en_status != zh_status:
                fail(
                    f"availability-status mismatch at record {position}: "
                    f"{en_name}:{en_line} vs {zh_name}:{zh_line}",
                    errors,
                )
            if "Paper-only by design" in en_cells[-1] or "Paper-only by design" in zh_cells[-1]:
                fail(f"paper-only entry is forbidden at {en_name}:{en_line}", errors)

        if external_urls(en_text) != external_urls(zh_text):
            fail(f"external-URL parity mismatch: {en_name} vs {zh_name}", errors)

        validate_table_widths(ROOT / en_name, en_text, errors)
        validate_table_widths(ROOT / zh_name, zh_text, errors)
        validate_section_counts(ROOT / en_name, en_text, errors)
        validate_section_counts(ROOT / zh_name, zh_text, errors)

        for path, text in ((ROOT / en_name, en_text), (ROOT / zh_name, zh_text)):
            match = INTERNAL_LABEL_RE.search(text)
            if match:
                line_number = text.count("\n", 0, match.start()) + 1
                fail(
                    f"{path.relative_to(ROOT)}:{line_number}: internal audit label "
                    f"leaked into public index: {match.group(0)}",
                    errors,
                )

        validate_dossier(
            source_name,
            en_rows,
            expected_count,
            seen_evidence_strong,
            errors,
        )

    validate_canonical_uniqueness(english_records, errors)

    total = sum(counts.values())
    if total != EXPECTED_TOTAL:
        fail(f"expected {EXPECTED_TOTAL} canonical records; found {total}", errors)

    readme_en = read("README.md")
    readme_zh = read("README.zh-CN.md")
    if external_urls(readme_en) != external_urls(readme_zh):
        fail("external-URL parity mismatch: README.md vs README.zh-CN.md", errors)

    en_date = re.search(r"Last fully verified: \*\*(\d{4}-\d{2}-\d{2})\*\*", readme_en)
    zh_date = re.search(r"最近一次完整核验：\*\*(\d{4}-\d{2}-\d{2})\*\*", readme_zh)
    if not en_date or not zh_date or en_date.group(1) != zh_date.group(1):
        fail("README verification-date parity mismatch", errors)

    for en_name, zh_name, _, expected_count, _ in COLLECTIONS:
        for readme, target, label in (
            (readme_en, en_name, "README.md"),
            (readme_zh, zh_name, "README.zh-CN.md"),
        ):
            claim = claimed_count(readme, target)
            if claim is None:
                fail(f"{label}: no linked count found for {target}", errors)
            elif claim != expected_count:
                fail(f"{label}: claims {claim} for {target}; expected {expected_count}", errors)

    en_total = re.search(r"\*\*(\d+) canonical records\*\*", readme_en)
    zh_total = re.search(r"\*\*(\d+) 条 canonical 记录\*\*", readme_zh)
    for match, label in ((en_total, "README.md"), (zh_total, "README.zh-CN.md")):
        if not match:
            fail(f"{label}: canonical-record total claim not found", errors)
        elif int(match.group(1)) != EXPECTED_TOTAL:
            fail(f"{label}: claims {match.group(1)} total records; expected {EXPECTED_TOTAL}", errors)

    issue_template = read(".github/ISSUE_TEMPLATE/resource.yml")
    validate_issue_template(issue_template, errors)

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

    legacy = (
        ROOT / "docs/en/game-agents.md",
        ROOT / "docs/zh-CN/game-agents.md",
        ROOT / "research/game-agent-sources.md",
    )
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
