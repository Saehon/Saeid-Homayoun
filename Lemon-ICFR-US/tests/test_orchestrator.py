import dataclasses
import json

from lemon_icfr.assurance.enums import FinalStatus, SourceTier
from lemon_icfr.assurance.evidence import EvidenceStore, Fact, make_evidence
from lemon_icfr.assurance.falsify import Falsifier
from lemon_icfr.assurance.grounding import Control, ICFRScope, Risk, TestProcedure
from lemon_icfr.assurance.independence import AgentRun
from lemon_icfr.assurance.review import ReproRef, Reviewer
from lemon_icfr.models import EvidenceItem, Finding
from lemon_icfr.orchestrator import LemonOrchestrator

ENTITY = "DEMO-CO"
PERIOD = "2025-12-31"


def agent(rid, role, provider):
    return AgentRun(rid, role, provider, "model", "v1", "prompt-v1", "code-v1", "data-v1",
                    "2026-10-04T00:00:00Z", f"{rid}-ctx")


def make_scope():
    return ICFRScope(
        entity=ENTITY,
        period_end=PERIOD,
        process="revenue",
        subprocess="order-to-cash",
        account="revenue",
        fsli="Revenue",
        assertion="existence_occurrence",
        risk=Risk("R1", "synthetic fictitious-revenue risk", "existence_occurrence"),
        control=Control("K1", "orders require delivery evidence", ("existence_occurrence",),
                        "preventive", "daily", "controller", "control_activities", 10),
        test=TestProcedure("T1", "K1", "synthetic population", 100, "deterministic 10", ("E-001",)),
        authority_refs=("PCAOB AS 2201",),
    )


def evidence_item(eid):
    return EvidenceItem(
        evidence_id=eid,
        source="synthetic test fixture",
        provenance=f"tests/test_orchestrator.py::{eid}",
        rights_status="test-only",
        content=f"synthetic {eid}",
    )


def store_item(eid):
    return make_evidence(
        eid,
        content=f"{eid}:effective".encode(),
        source="synthetic",
        tier=SourceTier.SEC_FILING,
        provenance=f"tests/test_orchestrator.py::{eid}",
        facts=[Fact(ENTITY, PERIOD, "icfr_conclusion", "effective")],
    )


def evidence_store(*ids):
    s = EvidenceStore()
    for eid in ids:
        s.add(store_item(eid))
    return s


REPRO = ReproRef("code-v1", "commit-v1", "data-v1", "cfg-v1", "python-test",
                 "provider-gen", "model", "prompt-v1", 7)


class StructuredProvider:
    name = "provider-gen"

    def lineage(self):
        return "provider-gen:model-v1"

    def generate_hypotheses(self, case_id, evidence, question):
        selected = Finding(
            agent="co-scientist",
            claim="Synthetic ICFR conclusion is effective.",
            evidence_refs=["E-001"],
            assumptions=["synthetic filing final"],
            limitations=["synthetic fixture only"],
            model_tool_version=self.lineage(),
            metadata={
                "hypothesis_id": "H1",
                "selected": True,
                "entity": ENTITY,
                "period_end": PERIOD,
                "assertion": "existence_occurrence",
                "propositions": [{"predicate": "icfr_conclusion", "value": "effective"}],
                "material": True,
            },
        )
        competitor = Finding(
            agent="co-scientist",
            claim="Synthetic alternative explanation.",
            evidence_refs=["E-002"],
            limitations=["synthetic fixture only"],
            model_tool_version=self.lineage(),
            metadata={
                "hypothesis_id": "H2",
                "selected": False,
                "entity": ENTITY,
                "period_end": PERIOD,
                "assertion": "existence_occurrence",
                "propositions": [{"predicate": "icfr_conclusion", "value": "effective"}],
                "rebuttal_evidence_ids": ["E-002"],
                "material": True,
            },
        )
        return [selected, competitor]

    def challenge_claim(self, case_id, evidence, finding):
        return Finding(
            agent="legacy-independent-falsification-output",
            claim="Legacy provider challenge present but it cannot promote an assurance gate.",
            evidence_refs=["E-001"],
            model_tool_version=self.lineage(),
        )


def valid_kwargs(*, created_at="2026-10-04T00:00:00Z", replay_fn=lambda: "same", store=None,
                 explicit_independence=True):
    st = store if store is not None else evidence_store("E-001", "E-002")
    kw = dict(
        case_id="CASE-001",
        question="Is the synthetic approval control operating effectively?",
        evidence=[evidence_item("E-001"), evidence_item("E-002")],
        provider=StructuredProvider(),
        coso_context_supplied=True,
        reproducibility_ref="tests/test_orchestrator.py",
        evidence_store=st,
        icfr_scope=make_scope(),
        repro_ref=REPRO,
        replay_fn=replay_fn,
        created_at=created_at,
    )
    if explicit_independence:
        kw.update(
            generator_run=agent("GEN", "generator", "provider-gen"),
            reviewer=Reviewer(agent("REV", "reviewer", "provider-review")),
            falsifier=Falsifier(agent("FAL", "falsifier", "provider-falsify"), st),
        )
    return kw


def gate(result, name):
    return next(g for g in result.gates if g.gate == name)


def test_human_gate_is_never_auto_approved():
    st = evidence_store("E-001", "E-002")
    result = LemonOrchestrator().run(**valid_kwargs(store=st))

    non_human = [g for g in result.gates if g.gate != "human_approval"]
    assert non_human and all(g.passed for g in non_human), [(g.gate, g.notes) for g in non_human]
    assert gate(result, "human_approval").passed is False
    assert result.status == "AWAITING_HUMAN_APPROVAL"
    assert result.assurance_passport is not None
    assert result.assurance_passport.final_status(st) is FinalStatus.AWAITING_HUMAN_APPROVAL


def test_assurance_passport_survives_result_serialization():
    result = LemonOrchestrator().run(**valid_kwargs())
    serialized = dataclasses.asdict(result)
    assert serialized["assurance_passport"]["passport_id"] == "PP-CASE-001"
    assert tuple(serialized["assurance_reasons"]) == result.assurance_reasons
    # EvidencePassport's existing serializer remains JSON-safe when reached through the formal field.
    json.dumps(result.assurance_passport.to_dict())


def test_boolean_coso_only_is_blocked():
    result = LemonOrchestrator().run(
        case_id="CASE-BOOL", question="synthetic",
        evidence=[evidence_item("E-001")], provider=StructuredProvider(),
        coso_context_supplied=True, reproducibility_ref="tests/test_orchestrator.py",
        evidence_store=evidence_store("E-001"), created_at="2026-10-04T00:00:00Z",
    )
    assert result.status.startswith("BLOCKED:")
    assert "icfr_coso_grounding" in result.status
    assert gate(result, "icfr_coso_grounding").passed is False


def test_evidence_store_mismatch_blocks():
    result = LemonOrchestrator().run(**valid_kwargs(store=evidence_store("E-001")))
    assert result.status.startswith("BLOCKED:")
    assert gate(result, "evidence_consistency").passed is False


def test_empty_created_at_fails_passport_gate():
    result = LemonOrchestrator().run(**valid_kwargs(created_at=""))
    assert gate(result, "evidence_passport").passed is False
    assert result.status != "AWAITING_HUMAN_APPROVAL"


def test_legacy_challenges_cannot_promote():
    result = LemonOrchestrator().run(**valid_kwargs(replay_fn=None))
    assert len(result.findings) > 2  # legacy challenge output exists
    assert gate(result, "falsification").passed is False
    assert result.status != "AWAITING_HUMAN_APPROVAL"


def test_low_independence_is_labelled():
    result = LemonOrchestrator().run(**valid_kwargs(explicit_independence=False))
    review = gate(result, "independent_review")
    assert review.passed is True
    assert any("LOW independence" in note for note in review.notes), review.notes

def test_legacy_reproducibility_ref_is_informational_only():
    kw = valid_kwargs()
    kw["repro_ref"] = None
    kw["reproducibility_ref"] = "legacy-string-is-present"
    result = LemonOrchestrator().run(**kw)
    repro = gate(result, "reproducibility")
    assert repro.passed is False
    assert any("ReproRef incomplete: absent" in note for note in repro.notes)
    assert any("legacy reproducibility_ref='legacy-string-is-present' is informational only" in note
               for note in repro.notes)
    assert result.status != "AWAITING_HUMAN_APPROVAL"


def test_legacy_challenges_are_labelled_unvalidated():
    result = LemonOrchestrator().run(**valid_kwargs())
    challenges = [f for f in result.findings if f.agent == "legacy-independent-falsification-output"]
    assert challenges
    assert all(f.metadata.get("status") == "LEGACY_UNVALIDATED_CHALLENGE" for f in challenges)

