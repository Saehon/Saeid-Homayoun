from pathlib import Path
import sys
import unittest

RUNTIME_DIR = Path(__file__).resolve().parents[1]
CASE_PATH = RUNTIME_DIR / "data" / "revenue_case.json"
sys.path.insert(0, str(RUNTIME_DIR))

import prototype003 as p003
import providers
import provider_runner as runner


class FakeProvider(providers.BaseProvider):
    def __init__(self):
        self.info = providers.ProviderInfo(provider="fake_real_provider_contract", model="fake-model")
        self.prompts = []

    def generate_json(self, system, user):
        self.prompts.append((system, user))
        return {
            "exceptions": ["TX-002", "TX-003"],
            "proposed_adjustment": 190000,
            "evidence_ids": ["EV-DELIVERY", "EV-LEDGER", "EV-CONTRACT"],
            "risks": ["revenue_cutoff", "premature_revenue_recognition"],
            "assertions": ["occurrence", "cutoff"],
            "procedures": ["inspect delivery evidence", "reconcile year-end transactions"],
            "limitations": ["Synthetic benchmark only"],
            "skepticism_checks": ["challenge timing assumptions"],
        }


class ProviderContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = p003.load_case(CASE_PATH)

    def test_public_case_withholds_gold(self):
        public = runner.public_case(self.case)
        self.assertNotIn("gold", public)

    def test_prompt_does_not_include_gold_object(self):
        prompt = runner._prompt(self.case, "test")
        self.assertNotIn('"gold"', prompt)

    def test_single_agent_contract_executes_with_fake_provider(self):
        provider = FakeProvider()
        result = runner.run_architecture(provider, self.case, "single_agent")
        self.assertEqual(result["artifact"]["execution_status"], "EXECUTED_REAL_PROVIDER")
        self.assertEqual(result["artifact"]["human_gate"], "PENDING_HUMAN_APPROVAL")
        self.assertEqual(result["metrics"]["precision"], 1.0)
        self.assertEqual(result["metrics"]["recall"], 1.0)

    def test_sequential_contract_uses_multiple_calls(self):
        provider = FakeProvider()
        runner.run_architecture(provider, self.case, "sequential_agents")
        self.assertEqual(len(provider.prompts), 3)

    def test_governed_contract_uses_critic_before_supervisor(self):
        provider = FakeProvider()
        runner.run_architecture(provider, self.case, "governed_multi_agent")
        self.assertEqual(len(provider.prompts), 5)
        self.assertIn("Critic/Falsifier Agent", provider.prompts[-2][1])
        self.assertIn("Supervisor Agent", provider.prompts[-1][1])

    def test_invalid_evidence_is_flagged_not_silently_accepted(self):
        provider = FakeProvider()
        raw = provider.generate_json("", "")
        raw["evidence_ids"].append("HALLUCINATED-EVIDENCE")
        artifact = runner.normalize(self.case, raw, provider, "single_agent")
        self.assertEqual(artifact["invalid_evidence_ids"], ["HALLUCINATED-EVIDENCE"])
        metrics = runner.evaluate(self.case, artifact)
        self.assertEqual(metrics["invalid_evidence_count"], 1)

    def test_human_gate_cannot_be_approved_by_provider(self):
        provider = FakeProvider()
        raw = provider.generate_json("", "")
        raw["human_gate"] = "APPROVED"
        artifact = runner.normalize(self.case, raw, provider, "single_agent")
        self.assertEqual(artifact["human_gate"], "PENDING_HUMAN_APPROVAL")


if __name__ == "__main__":
    unittest.main()
