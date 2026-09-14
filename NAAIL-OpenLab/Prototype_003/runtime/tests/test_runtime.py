import importlib.util
from pathlib import Path
import unittest

RUNTIME_DIR = Path(__file__).resolve().parents[1]
MODULE_PATH = RUNTIME_DIR / "prototype003.py"
CASE_PATH = RUNTIME_DIR / "data" / "revenue_case.json"
REGISTRY_PATH = RUNTIME_DIR / "data" / "case_registry.json"

spec = importlib.util.spec_from_file_location("prototype003", MODULE_PATH)
p003 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(p003)


class Prototype003RuntimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = p003.load_case(CASE_PATH)
        cls.registry = p003.load_json(REGISTRY_PATH)

    def test_release_registry_is_current(self):
        self.assertEqual(self.registry["public_release"], "0.2.3")
        self.assertEqual(len(self.registry["cases"]), 3)

    def test_frozen_revenue_gold_state(self):
        self.assertEqual(self.case["gold"]["exceptions"], ["TX-002", "TX-003"])
        self.assertEqual(self.case["gold"]["proposed_adjustment"], 190000)
        self.assertEqual(self.case["materiality"], 120000)

    def test_cutoff_detection_reproduces_frozen_exceptions(self):
        self.assertEqual(
            p003.detect_cutoff_exceptions(self.case),
            ["TX-002", "TX-003"],
        )

    def test_adjustment_reproduces_frozen_amount(self):
        exceptions = p003.detect_cutoff_exceptions(self.case)
        self.assertEqual(p003.proposed_adjustment(self.case, exceptions), 190000.0)

    def test_deterministic_run_enforces_human_gate(self):
        artifact = p003.run_deterministic(self.case)
        self.assertEqual(artifact["execution_status"], "EXECUTED")
        self.assertEqual(artifact["human_gate"], "PENDING_HUMAN_APPROVAL")
        self.assertEqual(artifact["claim_status"], "BENCHMARK_RESULT_ONLY")

    def test_deterministic_replay_is_stable(self):
        one = p003.run_deterministic(self.case)
        two = p003.run_deterministic(self.case)
        self.assertEqual(one["exceptions"], two["exceptions"])
        self.assertEqual(one["proposed_adjustment"], two["proposed_adjustment"])
        self.assertEqual(one["input_hashes"], two["input_hashes"])

    def test_provider_modes_are_not_fabricated(self):
        for architecture in p003.PROVIDER_ARCHITECTURES:
            row = p003.registered_provider_run(self.case, architecture)
            self.assertEqual(row["execution_status"], "NOT_EXECUTED_PROVIDER_REQUIRED")
            self.assertIsNone(row["provider"])
            self.assertIsNone(row["model"])
            self.assertIsNone(row["exceptions"])
            self.assertIsNone(row["metrics"])
            self.assertEqual(row["claim_status"], "NO_EMPIRICAL_RESULT")

    def test_evaluator_is_bounded(self):
        artifact = p003.run_deterministic(self.case)
        metrics = p003.evaluate_deterministic(self.case, artifact)
        for metric in ("RPA", "AA", "EG", "PS", "DS", "DIST", "precision", "recall"):
            self.assertGreaterEqual(metrics[metric], 0.0)
            self.assertLessEqual(metrics[metric], 1.0)
        self.assertTrue(metrics["adjustment_matches_gold"])
        self.assertTrue(metrics["human_gate_enforced"])
        self.assertFalse(metrics["unsupported_discovery_claim"])

    def test_public_benchmark_preserves_scientific_integrity(self):
        result = p003.run_public_benchmark(CASE_PATH, REGISTRY_PATH)
        self.assertEqual(set(result["runs"]), set(p003.ARCHITECTURES))
        self.assertEqual(result["runs"]["deterministic"]["artifact"]["execution_status"], "EXECUTED")
        for architecture in p003.PROVIDER_ARCHITECTURES:
            self.assertEqual(
                result["runs"][architecture]["execution_status"],
                "NOT_EXECUTED_PROVIDER_REQUIRED",
            )
        self.assertIn("NO_SUPERIORITY_CLAIM", result["research_claim"])


if __name__ == "__main__":
    unittest.main()
