import math
import unittest
from pathlib import Path

from aar_cam_unit_test import (
    build_artifact,
    exact_one_sided_sign_p,
    portfolio_transitions,
    read_rows,
    validate_frozen_structure,
)

HERE = Path(__file__).resolve().parent
DATA = HERE / "aar_cam_frozen_results.csv"


class AARCamUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = read_rows(DATA)

    def test_frozen_structure(self):
        self.assertEqual(validate_frozen_structure(self.rows), [])

    def test_2024_attention_reallocation(self):
        t = portfolio_transitions(self.rows)[2024]
        self.assertTrue(math.isclose(t["cars"], 2 / 3, rel_tol=1e-6, abs_tol=1e-6))
        self.assertEqual(t["cam_count_change"], 0)
        self.assertEqual(t["entry"], ["Acquired Intangibles / Business Combination"])
        self.assertEqual(t["exit"], ["Revenue"])
        self.assertEqual(t["persist"], ["Inventory"])

    def test_sign_test_uses_year_as_independent_unit(self):
        self.assertEqual(exact_one_sided_sign_p(5, 5), 0.03125)

    def test_new_topic_ciis_is_missing(self):
        row = next(r for r in self.rows if r["year"] == "2024" and r["new_topic"] == "1")
        self.assertEqual(row["ciis"], "")

    def test_artifact_boundary(self):
        artifact = build_artifact(self.rows, draws=1000, seed=7)
        self.assertTrue(artifact["validation"]["structure_pass"])
        self.assertEqual(artifact["company"], "AAR Corp")
        self.assertIn("not population inference", artifact["status"])
        self.assertGreater(artifact["weight_robustness"]["top_rank_share"], 0.95)


if __name__ == "__main__":
    unittest.main()
