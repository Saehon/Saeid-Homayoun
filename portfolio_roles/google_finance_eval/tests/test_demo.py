import unittest
from portfolio_roles.google_finance_eval.demo import score_case

class TestFinanceEval(unittest.TestCase):
    def setUp(self):
        self.case = {"case_id": "synthetic", "gold_value": "1.25", "model_value": "1.25",
                     "tolerance": "0", "allowed_evidence_ids": ["EV-1"],
                     "cited_evidence_ids": ["EV-1"]}

    def test_grounded_numeric_answer_passes(self):
        self.assertTrue(score_case(self.case)["pass"])

    def test_numeric_hallucination_fails(self):
        self.case["model_value"] = "999"
        self.assertIn("calculation_or_tolerance_error", score_case(self.case)["failure_modes"])

    def test_unsupported_source_fails(self):
        self.case["cited_evidence_ids"] = ["NOT-IN-GOLD"]
        self.assertFalse(score_case(self.case)["pass"])

    def test_missing_contract_fails_closed(self):
        del self.case["gold_value"]
        self.assertFalse(score_case(self.case)["pass"])

if __name__ == "__main__":
    unittest.main()
