#!/usr/bin/env python3
"""Search the bilingual Markdown index without maintaining a second dataset."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata

from validate_index import COLLECTIONS, external_urls, primary_title, read, record_rows


def normalize(text: str) -> str:
    return unicodedata.normalize("NFKC", text).casefold()


def load_records(language: str) -> list[dict]:
    records = []
    for en_path, zh_path, evidence, _, _ in COLLECTIONS:
        en_rows = record_rows(read(en_path))
        zh_rows = record_rows(read(zh_path))
        path = zh_path if language == "zh-CN" else en_path
        category = en_path.rsplit("/", 1)[-1].removesuffix(".md")
        for (en_line, en), (zh_line, zh) in zip(en_rows, zh_rows, strict=True):
            if en[0] != zh[0]:
                raise ValueError("Bilingual IDs differ; run scripts/validate_index.py")
            cells = zh if language == "zh-CN" else en
            # Read the bold availability declaration, preserving mixed-version labels.
            declarations = re.findall(r"\*\*(.*?)\*\*", en[-1])
            statuses = sorted(set(re.findall(
                r"\b(?:Open|Partial|Closed)\b", " ".join(declarations)
            )))
            records.append({
                "id": f"{category}:{cells[0]}",
                "category": category,
                "number": int(cells[0]),
                "title": primary_title(cells),
                "year": cells[1],
                "years": sorted(set(int(y) for y in re.findall(r"\d{4}", cells[1]))),
                "statuses": statuses,
                "paper_urls": external_urls(cells[2]),
                "details": cells[3:-1],
                "artifacts": cells[-1],
                "source": path,
                "line": zh_line if language == "zh-CN" else en_line,
                "evidence": evidence,
                "_search": normalize(" ".join(en + zh)),
            })
    return records


def search(records: list[dict], terms: list[str], category: str | None = None,
           status: str | None = None, year: int | None = None) -> list[dict]:
    return [
        {key: value for key, value in record.items() if key != "_search"}
        for record in records
        if (category is None or record["category"] == category)
        and (status is None or status in record["statuses"])
        and (year is None or year in record["years"])
        and all(normalize(term) in record["_search"] for term in terms)
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("terms", nargs="*", help="Keywords matched across both languages (AND)")
    parser.add_argument("--category", choices=["end-to-end", "pcg", "interactive-worlds"])
    parser.add_argument("--status", choices=["Open", "Partial", "Closed"])
    parser.add_argument("--year", type=int, help="Match any year explicitly listed in the year column")
    parser.add_argument("--lang", choices=["en", "zh-CN"], default="en")
    parser.add_argument("--json", action="store_true", help="Print structured JSON instead of text")
    args = parser.parse_args()
    records = search(load_records(args.lang), args.terms, args.category, args.status, args.year)
    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
    else:
        print(f"{len(records)} records" if args.lang == "en" else f"找到 {len(records)} 条记录")
        for record in records:
            print(f"\n[{record['id']}] {record['title']}")
            print(f"  {record['year']} | {' / '.join(record['statuses'])}")
            print(f"  {record['paper_urls'][0]}")
            print(f"  {record['source']}:{record['line']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
