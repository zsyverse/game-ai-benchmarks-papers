#!/usr/bin/env python3
"""Check that external links in the Markdown index still resolve.

This is a manual/scheduled maintenance tool, not part of ``validate_index.py``:
live checks depend on network conditions and on publisher bot policies, so they
must not gate pull requests. Run it from the repository root:

    python3 scripts/check_links.py            # report only
    python3 scripts/check_links.py --strict   # exit 1 when hard failures exist
    python3 scripts/check_links.py --json out.json

Classification:
- ``ok``          HTTP status < 400
- ``blocked``     403/429/503 from hosts known to reject scripted clients
                  (ACM/IEEE/Springer/Wiley DOIs, some university repositories);
                  these need a manual browser check, not an index edit
- ``gated``       401 (for example gated Hugging Face repositories)
- ``broken``      404/410 or another 4xx/5xx from a normal host
- ``error``       DNS/TLS/timeout failures

Only ``broken`` counts as a hard failure. ``error`` is reported but is often
transient; rerun before editing anything.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
BLOCKED_HOST_HINTS = (
    "doi.org/10.1145/",  # ACM Digital Library
    "doi.org/10.1109/",  # IEEE Xplore
    "doi.org/10.1007/",  # Springer
    "doi.org/10.1002/",  # Wiley
    "doi.org/10.36227/",  # TechRxiv
    "dl.acm.org",
    "ieeexplore.ieee.org",
    "link.springer.com",
    "cris.maastrichtuniversity.nl",
    "research.hva.nl",
    "discovery.ucl.ac.uk",
)
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept": "*/*",
}


def collect_links() -> dict[str, list[str]]:
    links: dict[str, list[str]] = {}
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            url = match.group(1).strip("<>")
            links.setdefault(url, []).append(str(path.relative_to(ROOT)))
    return links


def fetch_status(url: str, timeout: float) -> tuple[int | None, str]:
    context = ssl.create_default_context()
    last_error = ""
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=HEADERS, method=method)
        try:
            with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
                return response.status, ""
        except urllib.error.HTTPError as error:
            if method == "HEAD" and error.code in (400, 403, 404, 405, 429, 500, 501, 503):
                continue
            return error.code, ""
        except Exception as error:  # noqa: BLE001 - report every transport failure
            last_error = f"{type(error).__name__}: {str(error)[:100]}"
            if method == "HEAD":
                continue
    return None, last_error


def classify(url: str, status: int | None, error: str) -> str:
    if status is None:
        return "error"
    if status < 400:
        return "ok"
    if status == 401:
        return "gated"
    if status in (403, 429, 503) and any(hint in url for hint in BLOCKED_HOST_HINTS):
        return "blocked"
    return "broken"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--strict", action="store_true", help="exit 1 if any link is classified broken")
    parser.add_argument("--json", metavar="PATH", help="write the full report as JSON")
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--timeout", type=float, default=25.0)
    args = parser.parse_args()

    links = collect_links()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        statuses = list(executor.map(lambda u: (u, *fetch_status(u, args.timeout)), links))

    report = []
    for url, status, error in statuses:
        report.append(
            {
                "url": url,
                "status": status,
                "error": error,
                "class": classify(url, status, error),
                "files": sorted(set(links[url])),
            }
        )
    if args.json:
        Path(args.json).write_text(json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")

    counts: dict[str, int] = {}
    for item in report:
        counts[item["class"]] = counts.get(item["class"], 0) + 1
    print(
        f"checked {len(report)} unique external links: "
        + ", ".join(f"{name}={counts.get(name, 0)}" for name in ("ok", "blocked", "gated", "broken", "error"))
    )
    for name in ("broken", "error", "gated", "blocked"):
        items = [item for item in report if item["class"] == name]
        if not items:
            continue
        print(f"\n## {name} ({len(items)})")
        for item in sorted(items, key=lambda entry: entry["url"]):
            detail = item["status"] if item["status"] is not None else item["error"]
            print(f"- {detail} {item['url']}  <- {', '.join(item['files'])}")

    if args.strict and counts.get("broken"):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
