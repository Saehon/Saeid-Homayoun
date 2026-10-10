"""Five fully synthetic test cases for deterministic development scaffolds."""
import unittest
from naail_dev_starter import (
    evidence_gate, icfr_rule_baseline, cam_reallocation,
    ai_capex_rule, token_cost_twin,
)


class ConceptBaselineTests(unittest.TestCase):
    def test_evidence_gate_never_self_approves(self):
        v = evidence_gate([{"source_id": "s1", "source_date": "2026-01-01",
                            "supports_claim": False,
                            "independently_verified": True}], "2026-10-10")
        self.assertIn("UNSUPPORTED_CLAIM:0", v["flags"])
        self.assertFalse(v["autonomous_approval"])
        self.assertTrue(v["human_review_required"])

    def test_icfr_lag_monotonicity(self):
        low = icfr_rule_baseline(2, False, False)
        high = icfr_rule_baseline(20, False, False)
        self.assertLess(low["rule_score"], high["rule_score"])
        self.assertFalse(high["calibrated_probability"])

    def test_cam_composition_swaps(self):
        v = cam_reallocation(["Revenue", "Inventory"], ["Inventory", "Goodwill"])
        self.assertEqual(v["entered"], ["Goodwill"])
        self.assertEqual(v["exited"], ["Revenue"])
        self.assertAlmostEqual(v["composition_change"], 2 / 3, places=4)

    def test_capex_claim_needs_verification(self):
        v = ai_capex_rule("We disclosed capital expenditure for AI compute facilities.")
        self.assertEqual(v["label"], "AI_CAPEX_CANDIDATE")
        self.assertFalse(v["accounting_verified"])

    def test_token_cost_reconciles(self):
        v = token_cost_twin(1_000_000, 2_000_000, 1.0, 2.0, 0.5, 0.2,
                            400, 6, 30)
        self.assertAlmostEqual(v["total_usd"], 8.1)
        self.assertEqual(v["carbon_grams"], 200.0)


if __name__ == "__main__":
    unittest.main()
