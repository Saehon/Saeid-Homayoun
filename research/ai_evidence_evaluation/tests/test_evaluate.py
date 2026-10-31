import unittest
from research.ai_evidence_evaluation.evaluate import run_evaluation, score, validate_reference

BASE = {"case_id": "X", "domain": "finance", "question": "Synthetic question",
        "answer_type": "numeric", "answer": "0.25", "absolute_tolerance": "0.001",
        "evidence_ids": ["SYN-01"], "reference_provenance": "synthetic_case",
        "label_provenance": "not_independent", "source_rights": "original_synthetic"}
PASS = {"case_id": "X", "status": "answered", "model_answer": "0.250",
        "cited_evidence_ids": ["SYN-01"]}

class EvidenceEvaluationTests(unittest.TestCase):
    def test_correct_grounded_numeric(self):
        self.assertTrue(score(BASE, PASS)["grounded_correct"])

    def test_wrong_number_rejected(self):
        p = {**PASS, "model_answer": "0.50"}
        self.assertEqual(score(BASE, p)["status"], "answer_mismatch")

    def test_unsupported_citation_rejected(self):
        p = {**PASS, "cited_evidence_ids": ["MADE-UP"]}
        self.assertEqual(score(BASE, p)["status"], "citation_id_missing_or_unsupported")

    def test_missing_citation_rejected(self):
        self.assertFalse(score(BASE, {**PASS, "cited_evidence_ids": []})["grounded_correct"])

    def test_abstention_in_denominator(self):
        report = run_evaluation([BASE], [{"case_id":"X","status":"abstained"}])
        self.assertEqual(report["summary"]["n"], 1)
        self.assertEqual(report["summary"]["coverage"], 0)
        self.assertIsNone(report["summary"]["answer_accuracy_answered"])

    def test_duplicate_case_rejected(self):
        with self.assertRaises(ValueError):
            run_evaluation([BASE, BASE], [PASS])

    def test_holdout_contamination_blocks(self):
        with self.assertRaises(ValueError):
            run_evaluation([BASE], [PASS], development_ids=["X"])

    def test_nonfinite_gold_blocks(self):
        with self.assertRaises(ValueError):
            validate_reference({**BASE, "answer":"NaN"})

    def test_negative_tolerance_blocks(self):
        with self.assertRaises(ValueError):
            validate_reference({**BASE, "absolute_tolerance":"-0.01"})

    def test_unknown_prediction_blocks(self):
        with self.assertRaises(ValueError):
            run_evaluation([BASE], [{**PASS, "case_id":"UNKNOWN"}])

    def test_exact_text_case(self):
        ref = {**BASE, "answer_type":"text", "answer":"Not documented"}
        p = {**PASS, "model_answer":" not   DOCUMENTED "}
        self.assertTrue(score(ref,p)["answer_correct"])

    def test_missing_prediction_is_not_success(self):
        report = run_evaluation([BASE], [])
        self.assertEqual(report["summary"]["missing_or_invalid"], 1)
        self.assertEqual(report["summary"]["grounded_correct_rate_all"], 0)

if __name__ == "__main__":
    unittest.main()
