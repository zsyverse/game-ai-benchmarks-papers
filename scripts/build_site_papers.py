#!/usr/bin/env python3
"""Export the canonical Markdown tables as a small, display-only Pages dataset."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from search_index import load_records  # noqa: E402


def paper_url(record: dict) -> str:
    return record["paper_urls"][0]


def details_url(record: dict) -> str:
    source = Path(record["source"])
    return f"../docs/zh-CN/{source.name}"


def export() -> list[dict]:
    rows: list[dict] = []
    for record in load_records("zh-CN"):
        details = record["details"]
        category = {"end-to-end": "end", "pcg": "pcg", "interactive-worlds": "world"}[record["category"]]
        if category == "end":
            task, output, evaluation = details
        elif category == "pcg":
            output, task, evaluation = details
        else:
            task, evaluation = details
            output = ""
        rows.append(
            {
                "id": record["id"],
                "number": record["number"],
                "category": category,
                "year": record["year"],
                "title": record["title"],
                "paper": paper_url(record),
                "task": task,
                "output": output,
                "evaluation": evaluation,
                "status": " / ".join(record["statuses"]),
                "artifacts": record["artifacts"],
                "details": details_url(record),
                "source": record["source"],
                "line": record["line"],
            }
        )
    if len(rows) != 203:
        raise SystemExit(f"Expected 203 records, got {len(rows)}")
    return rows


if __name__ == "__main__":
    out = ROOT / "site" / "papers.json"
    out.write_text(json.dumps(export(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size} bytes)")
