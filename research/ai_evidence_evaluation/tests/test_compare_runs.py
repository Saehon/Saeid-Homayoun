import copy
import json
import tempfile
import unittest
from pathlib import Path

from research.ai_evidence_evaluation.compare_runs import (
    compare, pairwise, validate_manifest, resolve_case_path
)


ROOT = Path(__file__).resolve().parents[1] / "examples"


class CompareRunsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(
            (ROOT / "synthetic_comparison_manifest.json").read_text(encoding="utf-8")
        )

    def test_two_synthetic_runs(self):
        result = compare(self.manifest, ROOT)
        self.assertEqual(result["reference_count"], 5)
        self.assertEqual(len(result["run_summaries"]), 2)
        self.assertEqual(len(result["paired"]), 1)
        self.assertFalse(result["empirical_model_benchmark"])
        self.assertFalse(result["independent_gold_validation"])

    def test_pairwise_counts_reconcile(self):
        result = compare(self.manifest, ROOT)
        totals = result["paired"][0]["comparison"]
        self.assertEqual(sum(totals.values()), 5)

    def test_duplicate_run_ids_rejected(self):
        bad = copy.deepcopy(self.manifest)
        bad["runs"][1]["run_id"] = bad["runs"][0]["run_id"]
        with self.assertRaises(ValueError):
            validate_manifest(bad)

    def test_unverified_real_model_claim_rejected(self):
        bad = copy.deepcopy(self.manifest)
        bad["runs"][0]["source_type"] = "real_model"
        with self.assertRaises(ValueError):
            validate_manifest(bad)

    def test_research_source_rights_not_assumed(self):
        bad = copy.deepcopy(self.manifest)
        bad["rights_statement"] = ""
        with self.assertRaises(ValueError):
            validate_manifest(bad)

    def test_duplicate_reference_input_detected(self):
        # Distinct wrong IDs cannot be silently dropped from baseline comparisons.
        bad = copy.deepcopy(self.manifest)
        bad["reference_path"] = "synthetic_predictions.jsonl"
        with self.assertRaises(ValueError):
            compare(bad, ROOT)

    def test_path_traversal_is_blocked(self):
        with self.assertRaises(ValueError):
            resolve_case_path(ROOT, "../README.md")

    def test_absolute_path_blocked(self):
        with self.assertRaises(ValueError):
            resolve_case_path(ROOT, str(ROOT.resolve() / "synthetic_gold.jsonl"))

    def test_pairstatus_requires_same_cases(self):
        a = [{"case_id": "A", "grounded_correct": True}]
        b = [{"case_id": "B", "grounded_correct": False}]
        with self.assertRaises(ValueError):
            pairwise(a, b)

    def test_synthetic_metadata_is_visible(self):
        result = compare(self.manifest, ROOT)
        self.assertFalse(result["real_model_inference"])
        self.assertTrue(all(x["source_type"] == "synthetic_fixture"
                            for x in result["run_summaries"]))


if __name__ == "__main__":
    unittest.main()
