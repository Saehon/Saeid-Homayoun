import importlib.util
from pathlib import Path
import unittest

RUNTIME_DIR = Path(__file__).resolve().parents[1]
MODULE_PATH = RUNTIME_DIR / "prototype003.py"
CASE_PATH = RUNTIME_DIR / "data" / "revenue_case.json"

spec = importlib.util.spec_from_file_location("prototype003", MODULE_PATH)
p003 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(p003)


class Prototype003RuntimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = p003.load_case(CASE_PATH)

    def test_frozen_gold_state(self):
        self.assertEqual(self.case["gold"]["exceptions"], ["TX-002", "TX-003"])
        self.assertEqual(self.case["gold"]["proposed_adjustment"], 190000)
        self.assertEqual(self.case["materiality"], 120000)

    def test_all_architectures_share_frozen_input_hashes(self):
        frozen = p003.frozen_inputs(self.case)
        for architecture in p003.ARCHITECTURES:
            artifact = p003.run_architecture(self.case, architecture)
            self.assertEqual(artifact["input_hashes"], frozen)

    def test_cutoff_detection_reproduces_frozen_exceptions(self):
        self.assertEqual(
            p003.detect_cutoff_exceptions(self.case),
            ["TX-002", "TX-003"],
        )

    def test_adjustment_reproduces_frozen_amount(self):
        exceptions = p003.detect_cutoff_exceptions(self.case)
        self.assertEqual(p003.proposed_adjustment(self.case, exceptions), 190000.0)

    def test_human_gate_is_mandatory(self):
        for architecture in p003.ARCHITECTURES:
            artifact = p003.run_architecture(self.case, architecture)
            self.assertEqual(artifact["human_gate"], "PENDING_HUMAN_APPROVAL")
            self.assertNotEqual(artifact["claim_status"], "SCIENTIFIC_DISCOVERY")

    def test_governed_multi_agent_has_adversarial_controls(self):
        artifact = p003.run_architecture(self.case, "governed_multi_agent")
        trace = set(artifact["agent_trace"])
        for required in {
            "RightsLicenseAgent",
            "EvidenceAgent",
            "AuditRiskAgent",
            "AccountingAgent",
            "CriticAgent",
            "ReplicatorAgent",
            "FalsifierAgent",
            "HumanGate",
        }:
            self.assertIn(required, trace)
        self.assertTrue(artifact["replication"]["reproduced"])
        self.assertTrue(artifact["falsification"]["passed"])

    def test_evaluator_is_bounded_and_common(self):
        for architecture in p003.ARCHITECTURES:
            artifact = p003.run_architecture(self.case, architecture)
            metrics = p003.evaluate(self.case, artifact)
            for metric in ("RPA", "AA", "EG", "PS", "DS", "DIST", "precision", "recall"):
                self.assertGreaterEqual(metrics[metric], 0.0)
                self.assertLessEqual(metrics[metric], 1.0)
            self.assertFalse(metrics["unsupported_discovery_claim"])

    def test_full_benchmark_has_four_architectures(self):
        result = p003.run_benchmark(CASE_PATH)
        self.assertEqual(set(result["runs"]), set(p003.ARCHITECTURES))
        self.assertIn("NO_SUPERIORITY_CLAIM", result["research_claim"])


if __name__ == "__main__":
    unittest.main()
