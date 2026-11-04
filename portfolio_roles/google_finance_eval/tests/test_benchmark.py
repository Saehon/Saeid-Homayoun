import json
import unittest
from pathlib import Path
from portfolio_roles.google_finance_eval.benchmark import evaluate

class TestSyntheticBenchmark(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = json.loads((Path(__file__).parent.parent / "fixtures" / "cases.json").read_text(encoding="utf-8"))

    def test_curated_contract_cases(self):
        report = evaluate(self.rows)
        self.assertEqual(report["candidate_metrics"]["accuracy"], 1.0)
        self.assertEqual(report["candidate_metrics"]["n"], 10)

    def test_naive_baseline_not_as_good(self):
        report = evaluate(self.rows)
        self.assertLess(report["baseline_metrics"]["accuracy"], report["candidate_metrics"]["accuracy"])

    def test_duplicate_ids_rejected(self):
        with self.assertRaises(ValueError):
            evaluate([self.rows[0], self.rows[0]])

if __name__ == "__main__":
    unittest.main()
