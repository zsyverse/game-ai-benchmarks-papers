"""Regression checks for bilingual search and distinct-paper filtering."""

import unittest

from search_index import load_records, search
from validate_index import EXPECTED_TOTAL


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_records("en")

    def test_export_covers_each_canonical_record_once(self):
        result = search(self.records, [])
        self.assertEqual(len(result), EXPECTED_TOTAL)
        self.assertEqual(len({r["id"] for r in result}), EXPECTED_TOTAL)
        self.assertTrue(all(r["paper_urls"] and r["statuses"] for r in result))
        self.assertTrue(all("_search" not in r for r in result))

    def test_chinese_queries_work_with_english_output(self):
        self.assertTrue(search(self.records, ["可玩"]))
        self.assertEqual(
            [r["id"] for r in search(self.records, ["可玩"])],
            [r["id"] for r in search(load_records("zh-CN"), ["可玩"])],
        )

    def test_filters_compose(self):
        result = search(self.records, ["ＧＡＶＥＬ", "Ludii"], "end-to-end", "Open", 2024)
        self.assertEqual(len(result), 1)
        self.assertIn("GAVEL", result[0]["title"])
        self.assertEqual(search(self.records, ["GAVEL"], status="Closed"), [])

    def test_distinct_followups_keep_their_own_status(self):
        released = search(self.records, ["Hunyuan-GameCraft"], status="Partial")
        unreleased = search(self.records, ["Hunyuan-GameCraft"], status="Closed")
        self.assertEqual(len(released), 1)
        self.assertEqual(len(unreleased), 1)
        self.assertEqual(released[0]["statuses"], ["Partial"])
        self.assertEqual(unreleased[0]["statuses"], ["Closed"])
        self.assertNotEqual(released[0]["id"], unreleased[0]["id"])

    def test_matrix_followups_are_four_papers(self):
        records = search(self.records, ["Matrix-Game"], category="interactive-worlds")
        papers = [r for r in records if r["title"].startswith("Matrix-Game")]
        self.assertEqual(len(papers), 4)

    def test_version_year_and_empty_result(self):
        self.assertTrue(search(self.records, ["Matrix-Game"], year=2026))
        self.assertEqual(search(self.records, ["no-such-paper-xyz123"]), [])


if __name__ == "__main__":
    unittest.main()
