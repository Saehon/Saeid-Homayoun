import unittest
from integrated_case import run_integrated_case

class IntegratedPipelineTests(unittest.TestCase):
    def test_existing_lemon_and_cam_modules_execute(self):
        p=run_integrated_case("SYN-2024-00")
        self.assertEqual(p["data_class"],"SYNTHETIC")
        self.assertEqual(p["lemon_status"],"AWAITING_HUMAN_APPROVAL")
        self.assertFalse(p["human_approval_granted"])
        self.assertFalse(p["independent_reviewer_executed"])
        self.assertIn("prototype_composite",p["synthetic_cam_scoring"])
        self.assertEqual(p["source_module"]["lemon"],"Lemon-ICFR-US/src/lemon_icfr/orchestrator.py")
    def test_gate_does_not_self_approve(self):
        p=run_integrated_case("SYN-2024-01")
        self.assertEqual(p["lemon_gates"][-1]["gate"],"human_approval")
        self.assertFalse(p["lemon_gates"][-1]["passed"])
        self.assertFalse(p["scientific_discovery_claim_allowed"])
    def test_refuse_unregistered_case(self):
        with self.assertRaises(ValueError):
            run_integrated_case("AAPL")

if __name__=="__main__":
    unittest.main()
