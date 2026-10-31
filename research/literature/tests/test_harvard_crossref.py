"""Unit tests: formatting, integrity, and metadata mismatch detection, no network."""
import copy
import json
import unittest
from pathlib import Path

from research.literature.harvard_crossref import (
    ROOT, build, citation, compare_metadata, harvard_authors,
    validate_registry
)


class HarvardRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "llm_agentic_ai_seed_registry.json").read_text("utf-8"))

    def test_catalogue_contract(self):
        records = validate_registry(self.data)
        self.assertGreaterEqual(len(records), 20)

    def test_no_duplicate_dois(self):
        bad = copy.deepcopy(self.data)
        bad["records"].append(copy.deepcopy(bad["records"][0]))
        with self.assertRaises(ValueError):
            validate_registry(bad)

    def test_bad_doi_rejected(self):
        bad = copy.deepcopy(self.data)
        bad["records"][0]["doi"] = "invalid.github/doi"
        with self.assertRaises(ValueError):
            validate_registry(bad)

    def test_missing_author_rejected(self):
        bad = copy.deepcopy(self.data)
        bad["records"][0]["authors"] = []
        with self.assertRaises(ValueError):
            validate_registry(bad)

    def test_year_validation(self):
        bad = copy.deepcopy(self.data)
        bad["records"][0]["year"] = "2026"
        with self.assertRaises(ValueError):
            validate_registry(bad)

    def test_harvard_order_and_doi_link(self):
        rec = self.data["records"][0]
        text = citation(rec)
        self.assertIn("Blankespoor, E.", text)
        self.assertIn("(2026)", text)
        self.assertIn("‘Generative AI in Financial Reporting’", text)
        self.assertIn("https://doi.org/10.1111/1475-679x.70050", text)

    def test_two_author_harvard(self):
        self.assertEqual(harvard_authors(["Jung Ho Choi", "Chloe L. Xie"]),
                         "Choi, J. H. and Xie, C. L.")

    def test_single_author_harvard(self):
        self.assertEqual(harvard_authors(["Hongda Zhong"]), "Zhong, H.")

    def test_offline_does_not_claim_crossref_verification(self):
        result = build(self.data)
        self.assertEqual(result["mode"], "offline_reviewed_seed_only")
        self.assertFalse(result["crossref_api_accessed"])
        self.assertFalse(any(x["metadata_api_verified"] for x in result["records"]))

    def test_offline_does_not_claim_completeness(self):
        result = build(self.data)
        self.assertTrue(result["no_claim_of_exhaustiveness"])
        self.assertTrue(result["tiers_not_verified_by_api"])

    def test_exact_fake_crossref_matching(self):
        record = self.data["records"][0]
        metadata = {"title":[record["title"]],
                    "container-title":[record["journal"]],
                    "published":{"date-parts":[[record["year"], 1, 1]]},
                    "author":[{"family":"Blankespoor"}]}
        result = compare_metadata(record, metadata)
        self.assertFalse(result["metadata_needs_manual_review"])
        self.assertFalse(result["research_conclusion_verified_by_crossref"])
        self.assertFalse(result["tier_verified_by_crossref"])

    def test_mismatched_fake_crossref_title_flags(self):
        record = self.data["records"][0]
        metadata = {"title":["Another completely unrelated article"],
                    "container-title":[record["journal"]],
                    "issued":{"date-parts":[[2026]]},
                    "author":[{"family":"Blankespoor"}]}
        result = compare_metadata(record, metadata)
        self.assertTrue(result["metadata_needs_manual_review"])

    def test_crossref_cannot_verify_ajg(self):
        result = build(self.data)
        self.assertTrue(result["tiers_not_verified_by_api"])
        self.assertTrue(all(r["requires_scholarly_content_review"] for r in result["records"]))


if __name__ == "__main__":
    unittest.main()
