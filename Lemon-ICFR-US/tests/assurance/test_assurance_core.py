"""LEMON assurance core: minimum test suite (sections 28, 1-35).

Stdlib unittest (also collected by pytest). Synthetic entity DEMO-CO only:
no real-company facts are asserted. No network, no paid API.
"""
import dataclasses
import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path

from lemon_icfr.assurance.benchmark import BenchmarkArtifact, BenchmarkCase, BenchmarkRegistry
from lemon_icfr.assurance.claim import Claim, Proposition
from lemon_icfr.assurance.enums import (FalsificationOutcome as FO, FinalStatus, HumanDecision, Independence,
                                        ReviewOutcome as RO, Rights, ScientificStatus, SourceTier, SupportClass as SC,
                                        VariableStatus as VS)
from lemon_icfr.assurance.errors import (IntegrityError, LeakageError, PathSecurityError, PromotionError,
                                         ScientificHoldError, SelfApprovalError, SelfReviewError)
from lemon_icfr.assurance.evidence import EvidenceStore, Fact, make_evidence
from lemon_icfr.assurance.falsify import Falsifier
from lemon_icfr.assurance.grounding import Control, ICFRScope, Risk, TestProcedure, validate_scope
from lemon_icfr.assurance.human_gate import HumanDisposition, HumanGate, HumanRegistry, sign_disposition
from lemon_icfr.assurance.independence import AgentRun
from lemon_icfr.assurance.passport import EvidencePassport
from lemon_icfr.assurance.providers import FakeProvider
from lemon_icfr.assurance.review import Alternative, Hypothesis, ReproRef, Reviewer
from lemon_icfr.assurance.science import (PrimarySourceCitation, ScientificModel, VariableRegistry,
                                          fixture_arithmetic, load_coefficient_contract)
from lemon_icfr.assurance.support import assess_support
from lemon_icfr.assurance.twin import TwinControl, TwinModel, TwinRisk, run_scenario

E, P = "DEMO-CO", "2025-12-31"
KEY = b"test-only-human-ui-key"


def run(rid, role, provider="prov-a", model="m1", ctx=None):
    return AgentRun(rid, role, provider, model, "v1", "p1", "c1", "d1", "2026-10-04T00:00:00Z", ctx or rid)


def ev(eid, value="effective", tier=SourceTier.SEC_FILING, entity=E, period=P, **kw):
    return make_evidence(eid, content=f"{eid}:{value}".encode(), source="synthetic", tier=tier,
                         provenance=kw.pop("provenance", f"synthetic fixture {eid}"),
                         facts=[Fact(entity, period, "icfr_conclusion", value)], **kw)


def claim(ids=("E1",), value="effective", material=True, **kw):
    return Claim("C1", "Management concluded ICFR effective", kw.pop("entity", E), kw.pop("period", P),
                 kw.pop("assertion", "existence_occurrence"), (Proposition("icfr_conclusion", value),),
                 tuple(ids), material, **kw)


def scope(**kw):
    risk = Risk("R1", "fictitious revenue", kw.pop("risk_assertion", "existence_occurrence"))
    ctl = Control("K1", "revenue recognised only for delivered orders", ("existence_occurrence",),
                  "preventive", "daily", "controller", kw.pop("coso_component", "control_activities"),
                  kw.pop("coso_principle", 10))
    test = TestProcedure("T1", "K1", "order system extract", 1200, "random 25", ("E1",))
    base = dict(entity=E, period_end=P, process="revenue", subprocess="order-to-cash", account="revenue",
                fsli="Revenue", assertion="existence_occurrence", risk=risk, control=ctl, test=test,
                authority_refs=("PCAOB AS 2201",))
    base.update(kw)
    return ICFRScope(**base)


REPRO = ReproRef("code@1", "abc123", "data@1", "cfg-hash", "py3.12", "prov-a", "m1", "p1", 7)


def hyp(c=None, alts=True, gen=None):
    alts_t = (Alternative("restatement risk", ("E1",)),) if alts else ()
    return Hypothesis("H1", c or claim(), gen or run("G1", "generator"), ("filing is final",), alts_t,
                      ("synthetic",))


def store(*items):
    s = EvidenceStore()
    for i in items:
        s.add(i)
    return s


class T01_04_Evidence(unittest.TestCase):
    def test_01_missing_provenance(self):
        r = assess_support(claim(), store(ev("E1", provenance="  ")))
        self.assertIs(r.classification, SC.INSUFFICIENT_EVIDENCE)
        self.assertIn("missing provenance", r.findings[0].issues)

    def test_02_missing_rights(self):
        r = assess_support(claim(), store(ev("E1", rights=Rights.UNKNOWN)))
        self.assertIs(r.classification, SC.INSUFFICIENT_EVIDENCE)

    def test_03_fake_evidence_id(self):
        r = assess_support(claim(ids=("E1", "FAKE-9")), store(ev("E1")))
        self.assertIs(r.classification, SC.UNSUPPORTED)

    def test_04_evidence_exists_but_does_not_support(self):
        e = make_evidence("E1", content=b"x", provenance="p", facts=[Fact(E, P, "revenue", "100")])
        self.assertIs(assess_support(claim(), store(e)).classification, SC.UNSUPPORTED)


class T05_08_Review(unittest.TestCase):
    def _review(self, s, c=None, scope_issues=(), repro=REPRO, provider=None, h=None):
        c = c or claim()
        h = h or hyp(c)
        return Reviewer(run("RV", "reviewer", "prov-b"), provider).review(h, assess_support(c, s), list(scope_issues), repro)

    def test_05_unsupported_claim(self):
        self.assertIs(assess_support(claim(ids=()), store()).classification, SC.INSUFFICIENT_EVIDENCE)

    def test_06_reviewer_fail(self):
        self.assertIs(self._review(store(ev("E1")), scope_issues=["control does not address"]).outcome, RO.FAIL)

    def test_07_reviewer_insufficient(self):
        self.assertIs(self._review(store(ev("E1", rights=Rights.UNKNOWN))).outcome, RO.INSUFFICIENT_EVIDENCE)

    def test_08_reviewer_contradicted(self):
        s = store(ev("E1"), ev("E2", value="ineffective"))
        self.assertIs(self._review(s, c=claim(ids=("E1", "E2"))).outcome, RO.CONTRADICTED)

    def test_pass_only_with_real_support(self):
        self.assertIs(self._review(store(ev("E1"))).outcome, RO.PASS)

    def test_hypothesis_cannot_review_itself(self):
        g = run("G1", "generator")
        with self.assertRaises(SelfReviewError):
            Reviewer(AgentRun("G1", "reviewer", "prov-a", "m1", "v1", "p1", "c1", "d1", "t", "G1")).review(
                hyp(gen=g), assess_support(claim(), store(ev("E1"))), [], REPRO)


class T09_12_Falsification_Independence(unittest.TestCase):
    def _f(self, s, c=None, provider=None, replay=lambda: "h", sc=None):
        c = c or claim()
        return Falsifier(run("FZ", "falsifier", "prov-c"), s, provider).falsify(
            hyp(c), sc or scope(), assess_support(c, s), replay=replay)

    def test_09_falsifier_finds_omitted_contradiction(self):
        s = store(ev("E1"), ev("E9", value="ineffective", tier=SourceTier.SEC_FILING))
        r = self._f(s)   # claim cites only E1; E9 is omitted but contradicts
        self.assertIs(r.outcome, FO.REFUTED)

    def test_10_meaningless_falsifier_response(self):
        p = FakeProvider("prov-c", "m3", json.dumps([{"name": "x", "outcome": "SURVIVED", "detail": "ok", "evidence_ids": []}]))
        r = self._f(store(ev("E1")), provider=p)
        self.assertNotEqual(r.outcome, FO.SURVIVED)
        self.assertIn("meaningless", [c for c in r.challenges if c.name == "provider:x"][0].detail)

    def test_10b_empty_or_failing_falsifier_provider(self):
        self.assertIs(self._f(store(ev("E1")), provider=FakeProvider("c", "m", "[]")).outcome, FO.INCONCLUSIVE)
        self.assertIs(self._f(store(ev("E1")), provider=FakeProvider("c", "m", "", fail=TimeoutError())).outcome,
                      FO.INCONCLUSIVE)

    def test_challenges_existing_is_not_survival(self):
        self.assertIs(self._f(store(ev("E1")), replay=None).outcome, FO.INCONCLUSIVE)

    def test_survives_when_all_challenges_pass(self):
        self.assertIs(self._f(store(ev("E1"))).outcome, FO.SURVIVED)

    def test_11_same_provider_downgraded(self):
        r = Reviewer(run("RV", "reviewer", "prov-a", "m1")).review(hyp(), assess_support(claim(), store(ev("E1"))), [], REPRO)
        self.assertIs(r.independence, Independence.LOW)

    def test_12_cross_provider_recorded(self):
        r = Reviewer(run("RV", "reviewer", "prov-b")).review(hyp(), assess_support(claim(), store(ev("E1"))), [], REPRO)
        self.assertIs(r.independence, Independence.HIGH)


class T13_16_Provider_Grounding_Repro(unittest.TestCase):
    def _rv(self, raw=None, fail=None):
        p = FakeProvider("prov-b", "m2", raw or "", fail=fail)
        return Reviewer(run("RV", "reviewer", "prov-b"), p).review(hyp(), assess_support(claim(), store(ev("E1"))), [], REPRO)

    def test_13_malformed_provider_responses_fail_closed(self):
        good = {"outcome": "PASS", "reasoning": "ok", "evidence_refs": ["E1"], "entity": E, "period_end": P}
        bads = ["{not json", json.dumps({**good, "approve_human_gate": True}),
                json.dumps({k: v for k, v in good.items() if k != "reasoning"}),
                json.dumps({**good, "outcome": "LGTM"}), json.dumps({**good, "evidence_refs": ["E77"]}),
                json.dumps({**good, "entity": "OTHER"}), json.dumps({**good, "period_end": "2019-12-31"})]
        for raw in bads:
            with self.subTest(raw=raw[:40]):
                r = self._rv(raw)
                self.assertIs(r.outcome, RO.ESCALATE)
                self.assertEqual(r.provider_outcome, "PROVIDER_FAILURE")
        self.assertIs(self._rv(fail=TimeoutError("t")).outcome, RO.ESCALATE)
        self.assertIs(self._rv(json.dumps(good)).outcome, RO.PASS)

    def test_14_missing_coso_grounding(self):
        issues = validate_scope(scope(coso_component="vibes"))
        self.assertTrue(any("COSO" in i for i in issues))
        self.assertTrue(any("principle" in i for i in validate_scope(scope(coso_principle=16))))

    def test_15_wrong_assertion_mapping(self):
        self.assertIn("risk assertion does not match scope assertion",
                      validate_scope(scope(risk_assertion="completeness")))
        self.assertIn("control does not address the scoped assertion", validate_scope(scope(assertion="completeness",
                      risk_assertion="completeness")))

    def test_16_missing_repro_reference(self):
        r = Reviewer(run("RV", "reviewer", "prov-b")).review(hyp(), assess_support(claim(), store(ev("E1"))), [],
                                                             dataclasses.replace(REPRO, repo_commit=""))
        self.assertIs(r.outcome, RO.FAIL)


def build_passport(s=None, human=None):
    s = s or store(ev("E1"))
    c, sc = claim(), scope()
    sup = assess_support(c, s)
    rv = Reviewer(run("RV", "reviewer", "prov-b")).review(hyp(c), sup, validate_scope(sc), REPRO)
    fz = Falsifier(run("FZ", "falsifier", "prov-c"), s).falsify(hyp(c), sc, sup, replay=lambda: "h")
    return EvidencePassport("PP1", "CASE1", "2026-10-04T00:00:00Z", E, P, "Is ICFR effective?",
                            EvidencePassport.records_from(s, c.evidence_ids), sc, hyp(c), sup, rv, fz, REPRO, human=human), s


def gate():
    return HumanGate(HumanRegistry({"saeid": "owner"}, {"G1", "RV", "FZ"}), KEY)


def disposition(pp, decision=HumanDecision.APPROVED, rid="saeid", role="owner", **kw):
    d = HumanDisposition(rid, role, decision, "2026-10-04T10:00:00Z", "reviewed", ("F1",), ("E1",),
                         kw.pop("override_reason", ""), kw.pop("conditions", ()), pp.content_hash())
    return d


class T17_22_HumanGate_Passport(unittest.TestCase):
    def test_17_ai_cannot_self_approve(self):
        pp, _ = build_passport()
        g = gate()
        unsigned = disposition(pp)
        forged = dataclasses.replace(disposition(pp), signature="0" * 64)
        ai = sign_disposition(disposition(pp, rid="RV", role="owner"), KEY)
        wrong_key = sign_disposition(disposition(pp), b"agent-guessed-key")
        for d in (unsigned, forged, ai, wrong_key):
            with self.subTest(d=d.reviewer_id + d.signature[:4]), self.assertRaises(SelfApprovalError):
                g.accept(d, passport_hash=pp.content_hash(), review=pp.review.outcome, falsification=pp.falsification.outcome)
        self.assertIs(pp.final_status(), FinalStatus.AWAITING_HUMAN_APPROVAL)

    def test_18_authorised_human_approval(self):
        pp, s = build_passport()
        d = gate().accept(sign_disposition(disposition(pp), KEY), passport_hash=pp.content_hash(),
                          review=pp.review.outcome, falsification=pp.falsification.outcome)
        self.assertIs(dataclasses.replace(pp, human=d).final_status(s), FinalStatus.APPROVED)

    def test_19_human_rejection(self):
        pp, _ = build_passport()
        d = gate().accept(sign_disposition(disposition(pp, HumanDecision.REJECTED), KEY), passport_hash=pp.content_hash(),
                          review=pp.review.outcome, falsification=pp.falsification.outcome)
        self.assertIs(dataclasses.replace(pp, human=d).final_status(), FinalStatus.REJECTED)

    def test_approval_over_failed_review_needs_override(self):
        pp, _ = build_passport()
        with self.assertRaises(SelfApprovalError):
            gate().accept(sign_disposition(disposition(pp), KEY), passport_hash=pp.content_hash(),
                          review=RO.FAIL, falsification=FO.SURVIVED)

    def test_20_evidence_removed_after_analysis(self):
        pp, s = build_passport()
        s.remove("E1")
        self.assertIs(pp.final_status(s), FinalStatus.INVALIDATED)

    def test_21_deterministic_replay(self):
        a, _ = build_passport()
        b, _ = build_passport()
        self.assertEqual(a.content_hash(), b.content_hash())
        self.assertEqual(a.to_json(), b.to_json())

    def test_22_passport_serialisation_and_fail_closed(self):
        pp, _ = build_passport()
        d = json.loads(pp.to_json())
        self.assertEqual(d["final_status"], "AWAITING_HUMAN_APPROVAL")
        self.assertEqual(d["review"]["independence"], "HIGH")
        self.assertNotIn("content", json.dumps(d["evidence"]))
        self.assertIs(dataclasses.replace(pp, repro=None).final_status(), FinalStatus.BLOCKED)
        self.assertIs(dataclasses.replace(pp, review=None).final_status(), FinalStatus.BLOCKED)

    def test_approval_bound_to_passport_version(self):
        pp, _ = build_passport()
        d = sign_disposition(disposition(pp), KEY)
        changed = dataclasses.replace(pp, question="a different question")
        with self.assertRaises(SelfApprovalError):
            gate().accept(d, passport_hash=changed.content_hash(), review=RO.PASS, falsification=FO.SURVIVED)
        self.assertIs(dataclasses.replace(changed, human=d).final_status(), FinalStatus.INVALIDATED)


class T23_28_Twin_Disagreement_Hierarchy(unittest.TestCase):
    def test_23_digital_twin_scenarios(self):
        m = TwinModel((TwinRisk("R1", "existence_occurrence", 0.5),),
                      (TwinControl("K0", ("R1",), evidence_reliability=0.9),
                       TwinControl("K1", ("R1",), evidence_reliability=0.8, depends_on=("K0",), capacity=1000)))
        cases = [("control_failure", "K1"), ("evidence_removal", "K1"), ("override_increase", 0.5),
                 ("population_growth", 4000), ("sod_removal", "K1"), ("reliability_change", "K1", 0.2),
                 ("competing_explanation", "R1", 0.9), ("key_control_dependency_failure", "K0")]
        for name, *args in cases:
            with self.subTest(name=name):
                r = run_scenario(m, name, *args)
                self.assertGreater(r.delta["R1"], 0)
                self.assertIn("ANALYTICAL_SIMULATION", r.evidence_type)

    def test_24_model_disagreement_downgrades(self):
        p = FakeProvider("prov-b", "m2", json.dumps({"outcome": "FAIL", "reasoning": "disagree", "evidence_refs": ["E1"],
                                                    "entity": E, "period_end": P}))
        r = Reviewer(run("RV", "reviewer", "prov-b"), p).review(hyp(), assess_support(claim(), store(ev("E1"))), [], REPRO)
        self.assertIs(r.outcome, RO.FAIL)
        p2 = FakeProvider("prov-b", "m2", json.dumps({"outcome": "PASS", "reasoning": "fine", "evidence_refs": [],
                                                     "entity": E, "period_end": P}))
        r2 = Reviewer(run("RV", "reviewer", "prov-b"), p2).review(hyp(), assess_support(claim(), store(ev("E1", rights=Rights.UNKNOWN))), [], REPRO)
        self.assertIs(r2.outcome, RO.INSUFFICIENT_EVIDENCE)   # provider PASS cannot upgrade

    def test_25_source_hierarchy_conflict_recorded_not_silent(self):
        s = store(ev("E1"), ev("E2", value="ineffective", tier=SourceTier.SECONDARY))
        r = assess_support(claim(ids=("E1", "E2")), s)
        self.assertIs(r.classification, SC.SUPPORTED)
        self.assertTrue(r.conflicts)
        rv = Reviewer(run("RV", "reviewer", "prov-b")).review(hyp(claim(ids=("E1", "E2"))), r, [], REPRO)
        self.assertIs(rv.outcome, RO.ESCALATE)

    def test_25b_secondary_cannot_outrank_primary(self):
        s = store(ev("E1", value="ineffective"), ev("E2", value="effective", tier=SourceTier.SECONDARY))
        self.assertIs(assess_support(claim(ids=("E1", "E2")), s).classification, SC.CONTRADICTED)

    def test_26_contradictory_authoritative_evidence(self):
        s = store(ev("E1"), ev("E2", value="ineffective", tier=SourceTier.SEC_FILING))
        self.assertIs(assess_support(claim(ids=("E1", "E2")), s).classification, SC.CONTRADICTED)

    def test_27_wrong_period(self):
        self.assertIs(assess_support(claim(), store(ev("E1", period="2019-12-31"))).classification, SC.UNSUPPORTED)
        f = Falsifier(run("FZ", "falsifier", "prov-c"), store(ev("E1"))).falsify(
            hyp(), scope(period_end="2024-12-31"), assess_support(claim(), store(ev("E1"))), replay=lambda: "h")
        self.assertIs(f.outcome, FO.REFUTED)

    def test_28_wrong_entity(self):
        self.assertIs(assess_support(claim(), store(ev("E1", entity="OTHER-CO"))).classification, SC.UNSUPPORTED)


class T29_35_Integrity_Science(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        # SYNTHETIC_TEST_ONLY coefficients: NOT ACK2007 values
        self.names = tuple(f"b{i}" for i in range(14))
        contract = json.dumps({"scale": "raw", "coefficients": {n: float(i) / 10 for i, n in enumerate(self.names)}},
                              sort_keys=True).encode()
        (self.base / "contract.json").write_bytes(contract)
        self.csha = hashlib.sha256(contract).hexdigest()
        fixture = json.dumps([{n: 1.0 for n in self.names[1:]}]).encode()
        (self.base / "fixture.json").write_bytes(fixture)
        self.fsha = hashlib.sha256(fixture).hexdigest()

    def tearDown(self):
        self.tmp.cleanup()

    def test_29_checksum_mismatch(self):
        with self.assertRaises(IntegrityError):
            load_coefficient_contract(self.base, "contract.json", "0" * 64, self.names)

    def test_30_frozen_fixture_modified(self):
        (self.base / "fixture.json").write_bytes(b'[{"b1": 999}]')
        with self.assertRaises(IntegrityError):
            fixture_arithmetic(self.base, "fixture.json", self.fsha, {}, "b0")

    def test_fixture_arithmetic_is_development_only(self):
        c = load_coefficient_contract(self.base, "contract.json", self.csha, self.names)
        r = fixture_arithmetic(self.base, "fixture.json", self.fsha, c, "b0")
        self.assertEqual(r["status"], "DEVELOPMENT_ONLY")
        self.assertAlmostEqual(r["linear_predictor"][0], sum(i / 10 for i in range(14)))
        with self.assertRaises(TypeError):
            c["b1"] = 5.0   # immutable runtime mapping

    def test_path_traversal_and_symlink(self):
        with self.assertRaises(PathSecurityError):
            load_coefficient_contract(self.base, "../contract.json", self.csha, self.names)
        os.symlink(self.base / "contract.json", self.base / "link.json")
        with self.assertRaises(PathSecurityError):
            load_coefficient_contract(self.base, "link.json", self.csha, self.names)

    def test_31_benchmark_leakage(self):
        reg = BenchmarkRegistry()
        reg.add_case(BenchmarkCase("D1", "h1", "DEVELOPMENT", "gpt"))
        with self.assertRaises(LeakageError):
            reg.add_case(BenchmarkCase("H1", "h1", "HOLDOUT", "human", "2026-10-01"))
        a = BenchmarkArtifact("icfr", "organized/benchmarks/x", "CANONICAL", "1", "s", "l", "e", "py", "p", "r")
        reg.add_artifact(a)
        with self.assertRaises(LeakageError):
            reg.add_artifact(dataclasses.replace(a, path="copies-from-original/x"))

    def test_32_dev_probe_mislabelled_holdout(self):
        reg = BenchmarkRegistry()
        reg.add_case(BenchmarkCase("D1", "h1", "DEVELOPMENT", "gpt"))
        with self.assertRaises(LeakageError):
            reg.relabel("D1", "HOLDOUT")
        reg.add_case(BenchmarkCase("H2", "h2", "HOLDOUT", "human", "2026-10-01"))
        reg.inspect("H2", "claude")
        with self.assertRaises(LeakageError):
            reg.assert_confirmatory(["H2"], "gpt", "2026-10-05")
        reg.add_case(BenchmarkCase("H3", "h3", "HOLDOUT", "gpt", "2026-10-01"))
        with self.assertRaises(LeakageError):
            reg.assert_confirmatory(["H3"], "gpt", "2026-10-05")
        reg.add_case(BenchmarkCase("H4", "h4", "HOLDOUT", "human", "2026-10-01"))
        reg.assert_confirmatory(["H4"], "gpt", "2026-10-05")   # genuine holdout passes

    def test_33_coefficient_mutation(self):
        for mutate in ({"drop": "b13"}, {"add": "b99"}, {"bool": "b3"}, {"scale": "standardised"}):
            with self.subTest(mutate=mutate):
                d = {"scale": "raw", "coefficients": {n: 0.1 for n in self.names}}
                if "drop" in mutate: d["coefficients"].pop(mutate["drop"])
                if "add" in mutate: d["coefficients"][mutate["add"]] = 0.1
                if "bool" in mutate: d["coefficients"][mutate["bool"]] = True
                if "scale" in mutate: d["scale"] = mutate["scale"]
                b = json.dumps(d).encode()
                (self.base / "m.json").write_bytes(b)
                with self.assertRaises(IntegrityError):
                    load_coefficient_contract(self.base, "m.json", hashlib.sha256(b).hexdigest(), self.names)

    def test_34_unauthorised_variable_promotion(self):
        reg = VariableRegistry({"SIZE": VS.PENDING, "RGROWTH": VS.UNVERIFIED})
        secondary = PrimarySourceCitation("S1", False, "p.5", "p.6")
        no_rule = PrimarySourceCitation("P1", True, "Table 2", "")
        for cit in (None, secondary, no_rule):
            with self.subTest(cit=cit), self.assertRaises(PromotionError):
                reg.promote("SIZE", VS.VERIFIED, citation=cit, accepted_disposition=None)
        self.assertFalse(reg.executable("SIZE"))

    def test_35_no_bypass_around_scientific_hold(self):
        reg = VariableRegistry({"SIZE": VS.PENDING, "RGROWTH": VS.UNVERIFIED})
        m = ScientificModel("ACK2007", reg, ("SIZE", "RGROWTH"))
        self.assertIs(m.status, ScientificStatus.SCIENTIFIC_HOLD)
        with self.assertRaises(ScientificHoldError):
            m.predict({"SIZE": 1.0, "RGROWTH": 0.1})
        with self.assertRaises(PromotionError):
            m.promote_status(ScientificStatus.VERIFIED, accepted_disposition=None, confirmatory_evidence_id="X")
        with self.assertRaises(AttributeError):
            m.status = ScientificStatus.VERIFIED
        self.assertIs(m.status, ScientificStatus.SCIENTIFIC_HOLD)


if __name__ == "__main__":
    unittest.main()