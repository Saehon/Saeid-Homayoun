"""Fail-closed tests for the Decision-1 synthetic research pilot."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

P = Path(__file__).with_name("decision1_pilot.py")
spec = importlib.util.spec_from_file_location("decision1_pilot", P)
pilot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pilot)

class Decision1PilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = pilot.fixtures()

    def test_unique_labels_and_synthetic(self):
        self.assertGreaterEqual(len(self.cases), 18)
        self.assertEqual(len({c["case_id"] for c in self.cases}), len(self.cases))
        self.assertTrue(all(c["gold_label"] in pilot.CLASSES for c in self.cases))

    def test_no_gold_label_sent_to_candidate(self):
        s = pilot.candidate_state(self.cases[0])
        blob = json.dumps(s).lower()
        self.assertNotIn("gold_label", blob)
        self.assertNotIn("expected_label", blob)

    def test_all_offline_decisions_retain_human_gate(self):
        result = [pilot.assess(c) for c in self.cases]
        self.assertTrue(all(r["approved"] is False and r["production_action"] is None for r in result))
        self.assertEqual(pilot.summarize(result)["human_approval_count"], 0)
        self.assertTrue(all(r["confidence"] is None for r in result))

    def test_missing_evidence_fails_closed(self):
        x = dict(self.cases[0], evidence=[])
        r = pilot.assess(x)
        self.assertEqual(r["review_queue"], "EVIDENCE_GAP_REVIEW")
        self.assertEqual(r["model_prediction"], "INSUFFICIENT")
        self.assertFalse(r["approved"])

    def test_missing_provenance_fails_closed(self):
        x = dict(self.cases[0], evidence=[{"evidence_id":"Z", "fact":"Test", "source_uri":""}])
        self.assertEqual(pilot.assess(x)["evidence_status"], "MISSING_PROVENANCE")

    def test_contradiction_fails_closed(self):
        e = dict(self.cases[0]["evidence"][0], contradicts=True)
        x = dict(self.cases[0], evidence=[e])
        self.assertEqual(pilot.assess(x)["evidence_status"], "CONTRADICTORY_EVIDENCE")

    def test_non_synthetic_rejected(self):
        with self.assertRaises(pilot.ContractError):
            pilot.assess(dict(self.cases[0], data_class="CLIENT"))

    def test_gateway_requires_explicit_paid_opt_in(self):
        with self.assertRaises(pilot.ContractError):
            pilot.assess(self.cases[0], provider="gateway")

    def test_baseline_repeatability(self):
        x = pilot.candidate_state(self.cases[0])
        self.assertEqual(pilot.offline_baseline(x), pilot.offline_baseline(x))

    def test_no_fake_calibration(self):
        records=[pilot.assess(c) for c in self.cases]
        self.assertIsNone(pilot.summarize(records)["high_risk_brier_if_calibrated"])

if __name__ == "__main__":
    unittest.main()
