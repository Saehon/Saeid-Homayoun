"""R2: legacy gate booleans must be derived from real assessments (ORQ-007)."""
import unittest

from lemon_icfr.assurance.adapter import assure_case
from lemon_icfr.assurance.enums import FinalStatus, SourceTier
from lemon_icfr.assurance.falsify import Falsifier
from lemon_icfr.assurance.review import Reviewer

from test_assurance_core import E, P, REPRO, ev, run, scope, store

GEN = run("G1", "generator")


def H(hid="H1", selected=True, ids=("E1",), value="effective", **kw):
    d = {"hypothesis_id": hid, "selected": selected, "claim_text": f"ICFR {value}", "entity": E, "period_end": P,
         "assertion": "existence_occurrence", "propositions": [{"predicate": "icfr_conclusion", "value": value}],
         "evidence_ids": list(ids), "assumptions": ["filing final"], "limitations": ["synthetic"]}
    d.update(kw)
    return d


def COMP(rebut=("E1",)):
    return {"hypothesis_id": "H2", "selected": False, "claim_text": "restatement pending",
            "rebuttal_evidence_ids": list(rebut)}


def go(hyps, s=None, replay=lambda: "h"):
    s = s or store(ev("E1"))
    return assure_case(case_id="CASE1", question="Is ICFR effective?", created_at="2026-10-04T00:00:00Z",
                       legacy_hypotheses=hyps, store=s, scope=scope(), repro=REPRO, generator=GEN,
                       reviewer=Reviewer(run("RV", "reviewer", "prov-b")),
                       falsifier=Falsifier(run("FZ", "falsifier", "prov-c"), s), replay=replay)


def closed(d):
    return not (d.support_ok or d.reviewer_ok or d.falsification_ok)


class R2Adapter(unittest.TestCase):
    def test_r2_01_no_hypotheses(self):
        self.assertTrue(closed(go([])))

    def test_r2_02_hypotheses_exist_but_none_selected(self):
        # legacy bool(hypotheses) would have returned True here
        d = go([H(selected=False), COMP()])
        self.assertTrue(closed(d))
        self.assertIn("found 0", d.reasons[0])

    def test_r2_03_two_selected(self):
        self.assertTrue(closed(go([H(), H(hid="H9")])))

    def test_r2_04_unstructured_legacy_hypothesis_fails_closed(self):
        d = go([{"selected": True, "text": "controls look fine"}])
        self.assertTrue(closed(d))
        self.assertIn("structured field", d.reasons[0])

    def test_r2_05_genuine_support_still_awaits_human(self):
        d = go([H(), COMP()])
        self.assertTrue(d.support_ok and d.reviewer_ok and d.falsification_ok, d.reasons)
        self.assertIs(d.passport.final_status(), FinalStatus.AWAITING_HUMAN_APPROVAL)

    def test_r2_06_omitted_contradiction_blocks_falsification(self):
        s = store(ev("E1"), ev("E9", value="ineffective", tier=SourceTier.SEC_FILING))
        d = go([H(), COMP()], s=s)
        self.assertTrue(d.support_ok)
        self.assertFalse(d.falsification_ok)

    def test_r2_07_unrebutted_competitor_blocks_falsification(self):
        d = go([H(), COMP(rebut=())])
        self.assertFalse(d.falsification_ok)

    def test_r2_08_fake_evidence_id(self):
        d = go([H(ids=("E1", "FAKE"))])
        self.assertFalse(d.support_ok)
        self.assertFalse(d.reviewer_ok)

    def test_r2_09_malformed_proposition(self):
        self.assertTrue(closed(go([H(propositions=[{"predicate": "x"}])])))

    def test_r2_10_no_replay_no_survival(self):
        self.assertFalse(go([H(), COMP()], replay=None).falsification_ok)

    def test_r2_11_material_must_be_bool(self):
        self.assertTrue(closed(go([H(material="yes")])))


if __name__ == "__main__":
    unittest.main()