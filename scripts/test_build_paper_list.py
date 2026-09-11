"""Regression checks for the derived, compact bilingual paper views."""

import contextlib
import copy
import io
import re
import sys
import unittest
from unittest.mock import patch

import build_paper_list as build
from search_index import load_records
from validate_index import (
    COLLECTIONS,
    EXPECTED_TOTAL,
    ROOT,
    STATUS_RE,
    counted_section_headings,
    dossier_blocks,
    external_urls,
    markdown_links,
    read,
    section_record_groups,
)


def compact_groups(text):
    """Read rendered groups independently of the builder's internal state."""
    groups = []
    for line in text.splitlines():
        if line.startswith("### "):
            groups.append((line[4:], []))
        elif line.startswith("- **"):
            if not groups:
                raise AssertionError("A paper appeared outside a method/benchmark section")
            groups[-1][1].append(line)
    return groups


class PaperListTests(unittest.TestCase):
    def test_complete_bilingual_views_preserve_identity_sections_and_links(self):
        bilingual_primary_urls = []
        for language in ("en", "zh-CN"):
            with self.subTest(language=language):
                rendered = build.render(language)
                self.assertEqual(
                    rendered,
                    (ROOT / "docs" / language / "paper-list.md").read_text(encoding="utf-8"),
                )
                records = load_records(language)
                expected_groups = []
                for en_path, zh_path, evidence, _, _ in COLLECTIONS:
                    source = zh_path if language == "zh-CN" else en_path
                    canonical = read(source)
                    by_number = {r["number"]: r for r in records if r["source"] == source}
                    titles = {number: title for _, number, title, _ in dossier_blocks(read(evidence))}
                    for heading, numbers in zip(
                        counted_section_headings(canonical),
                        section_record_groups(canonical),
                        strict=True,
                    ):
                        ordered = sorted(
                            (by_number[number] for number in numbers),
                            key=lambda record: (-max(record["years"]), record["number"]),
                        )
                        expected_groups.append((re.sub(r"^## \d+\.\s+", "", heading), ordered, titles))

                actual_groups = compact_groups(rendered)
                self.assertEqual(len(actual_groups), 6)
                self.assertEqual([len(lines) for _, lines in actual_groups], [10, 28, 18, 102, 41, 4])
                identities = []
                primary_urls = []
                for (heading, lines), (expected_heading, ordered, titles) in zip(
                    actual_groups, expected_groups, strict=True
                ):
                    self.assertEqual(heading, expected_heading)
                    self.assertEqual(len(lines), len(ordered))
                    for line, record in zip(lines, ordered, strict=True):
                        self.assertEqual(external_urls(line), [record["paper_urls"][0]])
                        self.assertIn(f"**{record['year']}**", line)
                        self.assertIn(f"[{titles[record['number']]}]({record['paper_urls'][0]})", line)
                        notes = (
                            f"../../{record['evidence']}#"
                            + build.heading_slug(f"{record['number']}. {titles[record['number']]}")
                        )
                        self.assertEqual(markdown_links(line), [record["paper_urls"][0], notes])
                        declarations = [
                            label for label in re.findall(r"\*\*(.*?)\*\*", record["artifacts"])
                            if STATUS_RE.search(label)
                        ]
                        self.assertIn("`" + " / ".join(declarations) + "`", line)
                        identities.append(notes)
                        primary_urls.append(record["paper_urls"][0])
                self.assertEqual(len(identities), EXPECTED_TOTAL)
                self.assertEqual(len(set(identities)), EXPECTED_TOTAL)
                bilingual_primary_urls.append(primary_urls)
        self.assertEqual(len(bilingual_primary_urls), 2)
        self.assertEqual(bilingual_primary_urls[0], bilingual_primary_urls[1])

    def test_gfm_slug_keeps_repeated_hyphens_and_removes_title_punctuation(self):
        # Fixtures cross-checked against pandoc's GFM reader; no runtime dependency.
        fixtures = {
            "1. V-GameGym (SKYLENAGE-GameCodeGym)": "1-v-gamegym-skylenage-gamecodegym",
            "4. JamBench / JamSet (JAMER)": "4-jambench--jamset-jamer",
            "2. Genie — Generative Interactive Environments": "2-genie--generative-interactive-environments",
            "18. UniGen — 90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development": (
                "18-unigen--90-faster-100-code-free-mllm-driven-zero-code-3d-game-development"
            ),
            "81. PCGRL+: Scaling, Control and Generalization in Reinforcement Learning Level Generators": (
                "81-pcgrl-scaling-control-and-generalization-in-reinforcement-learning-level-generators"
            ),
            "36. Game Development as Human–LLM Interaction (ChatGE)": (
                "36-game-development-as-humanllm-interaction-chatge"
            ),
            "9. Matrix-Game 2.0: An Open-Source Real-Time and Streaming Interactive World Model": (
                "9-matrix-game-20-an-open-source-real-time-and-streaming-interactive-world-model"
            ),
        }
        for title, expected in fixtures.items():
            with self.subTest(title=title):
                self.assertEqual(build.heading_slug(title), expected)

    def test_version_year_sorting_and_mixed_availability_keep_qualifiers(self):
        records = copy.deepcopy(load_records("en"))
        first, second, third = records[:3]
        first.update(year="2020, rev. 2028", years=[2020, 2028])
        second.update(year="2027", years=[2027])
        third.update(year="2028", years=[2028])
        first.update(
            statuses=["Closed", "Open", "Partial"],
            artifacts=(
                "**Closed for the original release**; **Open, environment-heavy**; "
                "**Partial demo only** — supporting materials."
            ),
        )
        first["paper_urls"].append("https://example.org/not-the-primary-paper")
        with patch.object(build, "load_records", return_value=records):
            first_group = compact_groups(build.render("en"))[0][1]
        self.assertEqual(
            [external_urls(line)[0] for line in first_group[:3]],
            [first["paper_urls"][0], third["paper_urls"][0], second["paper_urls"][0]],
        )
        self.assertIn("**2020, rev. 2028**", first_group[0])
        self.assertIn(
            "`Closed for the original release / Open, environment-heavy / Partial demo only`",
            first_group[0],
        )
        self.assertNotIn("https://example.org/not-the-primary-paper", first_group[0])
        invalid = copy.deepcopy(first)
        invalid["statuses"] = ["Open"]
        with self.assertRaisesRegex(ValueError, "inconsistent availability"):
            build.record_line(invalid, invalid["title"], "en")
        with self.assertRaisesRegex(ValueError, "Evidence title mismatch"):
            build.record_line(first, "A different paper", "en")

    def test_check_detects_stale_or_missing_outputs_without_writing(self):
        generated = {"en": "fresh English\n", "zh-CN": "fresh Chinese\n"}
        scenarios = (
            ([True, True], list(generated.values()), 0),
            ([True, True], [generated["en"], "stale Chinese\n"], 1),
            ([False, True], [generated["zh-CN"]], 1),
        )
        for exists, contents, expected_exit in scenarios:
            with self.subTest(exists=exists, contents=contents):
                with (
                    patch.object(sys, "argv", ["build_paper_list.py", "--check"]),
                    patch.object(build, "render", side_effect=generated.__getitem__),
                    patch.object(build.Path, "exists", side_effect=exists),
                    patch.object(build.Path, "read_text", side_effect=contents),
                    patch.object(build.Path, "write_text") as write,
                    contextlib.redirect_stdout(io.StringIO()),
                ):
                    self.assertEqual(build.main(), expected_exit)
                    write.assert_not_called()


if __name__ == "__main__":
    unittest.main()
