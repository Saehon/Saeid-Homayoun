"""Behavioral and adversarial tests for strictly synthetic review simulation."""
import copy
import json
import unittest
from pathlib import Path

from research.ai_evidence_evaluation.annotation_audit import (
    audit, agreement_metrics, validate_panel, validate_annotations,
    validate_resolutions,
)
from research.ai_evidence_evaluation.evaluate import index_records, load_jsonl

ROOT = Path(__file__).resolve().parents[1] / "examples"


class AnnotationAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads((ROOT/"annotation_manifest.json").read_text(encoding="utf-8"))
        cls.gold = index_records(load_jsonl(ROOT/"synthetic_gold.jsonl"), "gold")
        cls.rows = load_jsonl(ROOT/"synthetic_annotations.jsonl")
        cls.resolutions = load_jsonl(ROOT/"synthetic_adjudications.jsonl")

    def test_complete_synthetic_contract(self):
        result = audit(self.config, ROOT)
        self.assertEqual(result["summary"]["n_cases"], 5)
        self.assertEqual(result["summary"]["n_reviewer_records"], 10)
        self.assertEqual(result["summary"]["n_adjudicated"], 1)
        self.assertEqual(result["summary"]["n_agreements"], 4)
        self.assertFalse(result["actual_independent_human_review_verified"])
        self.assertFalse(result["model_evaluation_completed"])

    def test_expected_kappa_only_descriptive(self):
        result = audit(self.config, ROOT)
        self.assertEqual(result["summary"]["raw_agreement"], 0.8)
        self.assertAlmostEqual(result["summary"]["cohens_kappa"], 0.705882)

    def test_two_distinct_reviewers_required(self):
        bad = copy.deepcopy(self.config)
        bad["reviewers"][1]["reviewer_id"] = "SIMULATED_A"
        with self.assertRaises(ValueError):
            validate_panel(bad)

    def test_adjudicator_cannot_equal_reviewer(self):
        bad = copy.deepcopy(self.config)
        bad["adjudicator"]["reviewer_id"] = "SIMULATED_A"
        with self.assertRaises(ValueError):
            validate_panel(bad)

    def test_actual_reviewer_claim_blocked(self):
        bad = copy.deepcopy(self.config)
        bad["reviewers"][0]["source_type"] = "independent_professional"
        with self.assertRaises(ValueError):
            validate_panel(bad)

    def test_external_rights_claim_blocked(self):
        bad = copy.deepcopy(self.config)
        bad["rights_statement"] = "licensed_unverified"
        with self.assertRaises(ValueError):
            validate_panel(bad)

    def test_missing_second_label_blocks(self):
        with self.assertRaises(ValueError):
            validate_annotations(self.rows[:-1], list(self.gold),
                                 ("SIMULATED_A","SIMULATED_B"), self.gold)

    def test_duplicate_label_blocks(self):
        with self.assertRaises(ValueError):
            validate_annotations(self.rows+self.rows[:1], list(self.gold),
                                 ("SIMULATED_A","SIMULATED_B"), self.gold)

    def test_unsupported_evidence_id_blocks(self):
        bad = copy.deepcopy(self.rows)
        bad[0]["evaluated_evidence_ids"] = ["NOT-IN-GOLD"]
        with self.assertRaises(ValueError):
            validate_annotations(bad, list(self.gold),
                                 ("SIMULATED_A","SIMULATED_B"), self.gold)

    def test_unknown_case_blocks(self):
        bad = copy.deepcopy(self.rows)
        bad[0]["case_id"] = "UNKNOWN"
        with self.assertRaises(ValueError):
            validate_annotations(bad, list(self.gold),
                                 ("SIMULATED_A","SIMULATED_B"), self.gold)

    def test_unrecognized_label_blocks(self):
        bad = copy.deepcopy(self.rows)
        bad[0]["support_label"] = "certainly_true"
        with self.assertRaises(ValueError):
            validate_annotations(bad, list(self.gold),
                                 ("SIMULATED_A","SIMULATED_B"), self.gold)

    def test_blank_rationale_blocks(self):
        bad = copy.deepcopy(self.rows)
        bad[0]["rationale"] = " "
        with self.assertRaises(ValueError):
            validate_annotations(bad, list(self.gold),
                                 ("SIMULATED_A","SIMULATED_B"), self.gold)

    def test_missing_disagreement_resolution_blocks(self):
        with self.assertRaises(ValueError):
            validate_resolutions([], {"SYN-MARGIN-03"}, "SIMULATED_C")

    def test_resolution_on_agreement_blocks(self):
        bad = copy.deepcopy(self.resolutions)
        bad[0]["case_id"] = "SYN-MARGIN-01"
        with self.assertRaises(ValueError):
            validate_resolutions(bad, {"SYN-MARGIN-03"}, "SIMULATED_C")

    def test_wrong_adjudicator_blocks(self):
        bad = copy.deepcopy(self.resolutions)
        bad[0]["adjudicator_id"] = "SIMULATED_A"
        with self.assertRaises(ValueError):
            validate_resolutions(bad, {"SYN-MARGIN-03"}, "SIMULATED_C")

    def test_no_division_by_zero_for_homogeneous_panels(self):
        rows = {("X","A"):{"support_label":"supported"},
                ("X","B"):{"support_label":"supported"}}
        metrics = agreement_metrics(rows, ["X"], "A", "B")
        self.assertIsNone(metrics["cohens_kappa"])


if __name__ == "__main__":
    unittest.main()
