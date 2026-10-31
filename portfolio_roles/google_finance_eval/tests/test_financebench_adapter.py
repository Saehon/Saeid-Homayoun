import unittest
from portfolio_roles.google_finance_eval.financebench_adapter import evaluate

class TestFinancebenchOfflineAdapter(unittest.TestCase):
    def setUp(self):
        self.gold = [{"financebench_id": "SYN-1", "answer": "100 USD", "question_type": "metrics-generated",
                     "evidence": [{"evidence_doc_name": "SYN-10K"}]},
                     {"financebench_id": "SYN-2", "answer": "No", "question_type": "domain-relevant",
                     "evidence": [{"evidence_doc_name": "SYN-10K"}]}]

    def test_correct_answer_and_document(self):
        candidates = [{"financebench_id": "SYN-1", "predicted_answer": "100 USD",
                       "cited_evidence_doc_names": ["SYN-10K"]}]
        result = evaluate(self.gold, candidates)
        self.assertEqual(result["answered"], 1)
        self.assertEqual(result["strict_exact_match_overall"], 0.5)
        self.assertEqual(result["citation_doc_name_match_rate"], 0.5)

    def test_unverified_citation_not_credited(self):
        response = [{"financebench_id": "SYN-1", "predicted_answer": "100 USD",
                     "cited_evidence_doc_names": ["MADE-UP"]}]
        self.assertEqual(evaluate(self.gold, response)["citation_doc_name_match_rate"], 0)

    def test_numeric_zero_is_not_abstention(self):
        test_gold = [{"financebench_id":"ZERO", "answer":"0", "question_type":"metrics-generated"}]
        result = evaluate(test_gold, [{"financebench_id":"ZERO","predicted_answer":0}])
        self.assertEqual(result["answered"], 1)
        self.assertEqual(result["strict_exact_match_overall"], 1)

    def test_duplicate_gold_rejected(self):
        with self.assertRaises(ValueError):
            evaluate([self.gold[0], self.gold[0]], [])

    def test_unknown_candidate_id_rejected(self):
        with self.assertRaises(ValueError):
            evaluate(self.gold, [{"financebench_id": "UNKNOWN", "predicted_answer": "100 USD"}])

if __name__ == "__main__":
    unittest.main()
