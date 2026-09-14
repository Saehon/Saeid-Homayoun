import unittest

from student_digital_twin import CASES, ALLOWED_DECISIONS, EducationalProxyAgent, demo_decision, score_decision


class StudentDigitalTwinTests(unittest.TestCase):
    def test_three_cases_exist(self):
        self.assertEqual(set(CASES), {"revenue", "goodwill", "icfr"})

    def test_proxy_requires_human_review(self):
        agent = EducationalProxyAgent()
        for case in CASES.values():
            advice = agent.advise(case)
            self.assertTrue(advice["required_human_review"])
            self.assertEqual(advice["status"], "EDUCATIONAL_SIMULATION_ONLY")

    def test_demo_decisions_are_valid(self):
        for key, case in CASES.items():
            decision = demo_decision(key)
            self.assertIn(decision.decision, ALLOWED_DECISIONS)
            result = score_decision(case, decision)
            self.assertEqual(result["human_gate"], "PENDING_HUMAN_APPROVAL")
            self.assertEqual(
                result["score_status"],
                "ILLUSTRATIVE_NOT_VALIDATED_FOR_EMPLOYMENT_DECISIONS",
            )

    def test_scores_are_bounded(self):
        for key, case in CASES.items():
            result = score_decision(case, demo_decision(key))
            for value in result["metrics"].values():
                self.assertGreaterEqual(value, 0)
                self.assertLessEqual(value, 100)
            self.assertGreaterEqual(result["professional_judgment_core"], 0)
            self.assertLessEqual(result["professional_judgment_core"], 100)
            self.assertGreaterEqual(result["ai_readiness_core"], 0)
            self.assertLessEqual(result["ai_readiness_core"], 100)


if __name__ == "__main__":
    unittest.main()
