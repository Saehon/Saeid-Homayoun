import copy
import json
import unittest

from research.literature.evidence_quality_gate import (
    REGISTRY, LEDGER, PAGE, audit,
)


class ScholarlyEvidenceQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        cls.ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
        cls.page = PAGE.read_text(encoding="utf-8")

    def test_current_harvard_citations_and_claims_reconcile(self):
        result = audit(self.registry, self.ledger, self.page)
        self.assertEqual(result["bibliographic_records"], 21)
        self.assertEqual(result["public_harvard_references"], 21)
        self.assertEqual(result["tracked_project_claims"], 11)
        self.assertFalse(result["all_project_hypotheses_empirically_supported"])

    def test_doi_replacement_in_public_page_blocks_release(self):
        text = self.page.replace("10.1111/1475-679x.70050", "10.1111/fake-doi", 1)
        with self.assertRaisesRegex(ValueError, "DOI drift"):
            audit(self.registry, self.ledger, text)

    def test_title_mismatch_blocks_release(self):
        text = self.page.replace("‘Generative AI in Financial Reporting’",
                                 "‘Invented Publication’", 1)
        with self.assertRaisesRegex(ValueError, "article-title drift"):
            audit(self.registry, self.ledger, text)

    def test_author_mismatch_blocks_release(self):
        text = self.page.replace("Blankespoor, E.", "Someone, X.", 1)
        with self.assertRaisesRegex(ValueError, "Harvard author/year drift"):
            audit(self.registry, self.ledger, text)

    def test_duplicate_bibliographic_line_blocks(self):
        item = next(line for line in self.page.splitlines()
                    if line.startswith("- **JAR-2026-blankespoor:"))
        with self.assertRaises(ValueError):
            audit(self.registry, self.ledger, self.page + "\n" + item)

    def test_fabricated_source_in_claim_ledger_blocks(self):
        bad = copy.deepcopy(self.ledger)
        bad["project_claims"][0]["evidence_keys"].append("SOME-NONEXISTENT-PAPER")
        with self.assertRaisesRegex(ValueError, "unregistered academic reference"):
            audit(self.registry, bad, self.page)

    def test_claiming_empirical_support_without_replication_blocks(self):
        bad = copy.deepcopy(self.ledger)
        bad["project_claims"][0]["empirical_status"] = "PROVEN_BY_UNIT_TEST"
        with self.assertRaisesRegex(ValueError, "unverified experimental claim"):
            audit(self.registry, bad, self.page)

    def test_missing_uncertainty_blocks(self):
        bad = copy.deepcopy(self.ledger)
        bad["project_claims"][0]["uncertainty"] = ""
        with self.assertRaisesRegex(ValueError, "missing substantive uncertainty"):
            audit(self.registry, bad, self.page)

    def test_malicious_journal_rating_label_not_authoritative(self):
        report = audit(self.registry, self.ledger, self.page)
        self.assertFalse(report["official_ajg_ranking_verified"])
        self.assertFalse(report["bibliographic_metadata_verified_against_publisher_api"])

    def test_private_archive_disclosure_must_remain(self):
        text = self.page.replace("Google Drive", "private archive")
        with self.assertRaisesRegex(ValueError, "Google Drive"):
            audit(self.registry, self.ledger, text)

    def test_claims_cannot_represent_all_untested_research_as_verified(self):
        report = audit(self.registry, self.ledger, self.page)
        self.assertEqual(report["validation_scope"],
                         "OFFLINE_STRUCTURE_AND_CLAIM_GATES_ONLY")
        self.assertTrue(report["nonexhaustive_literature"])


if __name__ == "__main__":
    unittest.main()
