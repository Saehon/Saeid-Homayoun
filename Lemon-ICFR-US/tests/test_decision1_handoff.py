"""Synthetic-only integration contract: Decision-1 triage → unchanged Lemon Human Gate."""
import importlib.util
import sys
import unittest
from pathlib import Path

HOME = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HOME))  # pytest runs from Lemon package root, not repo root
ROOT = HOME.parent / "NAAIL" / "research-assurance-mcp" / "decision1-pilot"
spec = importlib.util.spec_from_file_location("decision1_pilot", ROOT / "decision1_pilot.py")
pilot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pilot)

from integrations.decision1_icfr_triage_bridge import build_submission, run_independent_lemon_review
from lemon_icfr.models import Finding

class IndependentTestReviewer:
    name = "mock-separate-reviewer"
    def lineage(self):
        return "synthetic-review-fixture/1"
    def generate_hypotheses(self, case_id, evidence, question):
        return [Finding(agent=self.name,claim="Request corroborating controls evidence, no audit conclusion.",
                        evidence_refs=[evidence[0].evidence_id],model_tool_version=self.lineage())]
    def challenge_claim(self, case_id, evidence, finding):
        return Finding(agent="mock-falsification",claim="Control population may be incomplete.",
                       evidence_refs=[evidence[0].evidence_id],model_tool_version=self.lineage())

class LemonBridgeTests(unittest.TestCase):
    def setUp(self):
        self.case=pilot.fixtures()[0]
        self.triage=pilot.assess(self.case)

    def test_handoff_only(self):
        doc=build_submission(self.case,self.triage)
        self.assertEqual(len(doc["evidence"]),2)
        self.assertNotIn("gold_label",str(doc))

    def test_rejects_unreviewed_evidence(self):
        with self.assertRaises(ValueError):
            build_submission(self.case,dict(self.triage,evidence_status="MISSING_EVIDENCE"))

    def test_rejects_auto_approved(self):
        with self.assertRaises(ValueError):
            build_submission(self.case,dict(self.triage,approved=True))

    def test_existing_lemon_human_gate_remains_closed(self):
        out=run_independent_lemon_review(
            self.case,self.triage,independent_provider=IndependentTestReviewer(),
            coso_context_supplied=True,reproducibility_ref="synthetic-fixture/test")
        self.assertEqual(out.status,"AWAITING_HUMAN_APPROVAL")
        self.assertFalse([g for g in out.gates if g.gate=="human_approval"][0].passed)

    def test_missing_coso_blocks(self):
        out=run_independent_lemon_review(
            self.case,self.triage,independent_provider=IndependentTestReviewer(),
            coso_context_supplied=False,reproducibility_ref="synthetic-fixture/test")
        self.assertTrue(out.status.startswith("BLOCKED:"))

if __name__=="__main__":
    unittest.main()
