import unittest

from benchmark import (
    assertion_alignment,
    evidence_grounding,
    risk_procedure_alignment,
    score_rows,
)


class BenchmarkTests(unittest.TestCase):
    def test_revenue_alignment_improves_with_relevant_procedures(self):
        risk = "Revenue recognition cutoff risk"
        weak = "We discussed the matter with management."
        strong = "We tested contracts and invoices, checked cutoff, confirmed balances, and recalculated amounts."
        self.assertGreater(risk_procedure_alignment(risk, strong), risk_procedure_alignment(risk, weak))

    def test_assertion_alignment_rewards_direct_assertion_reference(self):
        self.assertGreater(
            assertion_alignment("valuation accuracy", "We tested valuation and accuracy."),
            assertion_alignment("valuation accuracy", "We held a meeting."),
        )

    def test_evidence_grounding_rewards_named_evidence(self):
        strong = evidence_grounding("contracts invoices reconciliation schedule", "tested sample contracts")
        weak = evidence_grounding("", "considered the matter")
        self.assertGreater(strong, weak)

    def test_score_rows_returns_all_dimensions(self):
        rows = [{
            "id": "X",
            "risk_text": "Goodwill impairment valuation risk",
            "procedure_text": "We tested valuation, forecast, discount assumptions and sensitivity.",
            "evidence_text": "Forecast model specialist report calculation schedule",
            "assertion_text": "valuation accuracy",
        }]
        result = score_rows(rows)[0]
        self.assertEqual(set(result["scores"]), {"RPA", "AA", "EG", "PS", "DS", "DIST"})
        self.assertGreaterEqual(result["prototype_composite"], 0)
        self.assertLessEqual(result["prototype_composite"], 100)


if __name__ == "__main__":
    unittest.main()
