from __future__ import annotations

from collections.abc import Callable
from typing import Any

from lemon_icfr.assurance.adapter import assure_case
from lemon_icfr.assurance.evidence import EvidenceStore
from lemon_icfr.assurance.falsify import Falsifier
from lemon_icfr.assurance.grounding import Control, ICFRScope, Risk, validate_scope
from lemon_icfr.assurance.independence import AgentRun
from lemon_icfr.assurance.review import ReproRef, Reviewer
from lemon_icfr.models import EvidenceItem, Finding, GateResult, LemonCaseResult
from lemon_icfr.providers.base import ModelProvider


_REQUIRED_GATES = (
    "provenance",
    "rights_license",
    "icfr_coso_grounding",
    "evidence_sufficiency",
    "independent_review",
    "falsification",
    "reproducibility",
    "human_approval",
)


class LemonOrchestrator:
    """Legacy-compatible shell whose scientific gates are derived from the R1 assurance core."""

    def _evidence_gates(self, evidence: list[EvidenceItem]) -> list[GateResult]:
        provenance_ok = bool(evidence) and all(e.provenance.strip() for e in evidence)
        rights_ok = bool(evidence) and all(e.rights_status.strip() for e in evidence)
        return [
            GateResult("provenance", provenance_ok, [] if provenance_ok else ["Missing evidence provenance."]),
            GateResult("rights_license", rights_ok, [] if rights_ok else ["Missing rights/license status."]),
        ]

    @staticmethod
    def _missing_scope() -> ICFRScope:
        """Represent unavailable legacy scope as missing values; never invent accounting facts."""
        return ICFRScope(
            entity="",
            period_end="",
            process="",
            subprocess="",
            account="",
            fsli="",
            assertion="",
            risk=Risk(risk_id="", description="", assertion=""),
            control=Control(
                control_id="",
                objective="",
                addresses_assertions=(),
                control_type="",
                frequency="",
                owner="",
                coso_component="",
                coso_principle=0,
            ),
            test=None,
            authority_refs=(),
        )

    @staticmethod
    def _legacy_hypothesis_records(hypotheses: list[Finding]) -> list[dict[str, Any]]:
        """Map only fields the legacy Finding actually contains; missing structure stays missing."""
        records: list[dict[str, Any]] = []
        structured = (
            "hypothesis_id",
            "selected",
            "entity",
            "period_end",
            "assertion",
            "propositions",
            "rebuttal_evidence_ids",
            "material",
            "causal",
            "identification_strategy",
        )
        for finding in hypotheses:
            row: dict[str, Any] = {
                "claim_text": finding.claim,
                "evidence_ids": list(finding.evidence_refs),
                "assumptions": list(finding.assumptions),
                "limitations": list(finding.limitations),
            }
            metadata = finding.metadata if isinstance(finding.metadata, dict) else {}
            for key in structured:
                if key in metadata:
                    row[key] = metadata[key]
            records.append(row)
        return records

    @staticmethod
    def _default_runs(case_id: str, provider: ModelProvider, created_at: str) -> tuple[AgentRun, AgentRun, AgentRun]:
        """Same-provider development fallback with separate run/context identities (LOW independence)."""
        provider_name = str(getattr(provider, "name", type(provider).__name__))
        lineage = str(provider.lineage())
        model_name = provider_name
        model_version = lineage

        def make(role: str) -> AgentRun:
            return AgentRun(
                run_id=f"{case_id}:{role}",
                role=role,
                provider=provider_name,
                model=model_name,
                model_version=model_version,
                prompt_version="",
                code_version="",
                data_version="",
                timestamp=created_at,
                context_id=f"{case_id}:{role}:context",
            )

        return make("generator"), make("reviewer"), make("falsifier")

    def run(
        self,
        *,
        case_id: str,
        question: str,
        evidence: list[EvidenceItem],
        provider: ModelProvider,
        coso_context_supplied: bool,
        reproducibility_ref: str | None,
        evidence_store: EvidenceStore | None = None,
        icfr_scope: ICFRScope | None = None,
        repro_ref: ReproRef | None = None,
        generator_run: AgentRun | None = None,
        reviewer: Reviewer | None = None,
        falsifier: Falsifier | None = None,
        replay_fn: Callable[[], str] | None = None,
        created_at: str = "",
    ) -> LemonCaseResult:
        gates = self._evidence_gates(evidence)

        # ORQ-010: the legacy Boolean is retained for API compatibility but can no longer
        # establish COSO/ICFR grounding. Only a structured ICFRScope validated by the R1
        # assurance core can pass this gate.
        scope = icfr_scope if icfr_scope is not None else self._missing_scope()
        scope_issues = validate_scope(scope)
        grounding_ok = icfr_scope is not None and not scope_issues
        grounding_notes: list[str] = []
        if not grounding_ok:
            grounding_notes.append("Structured ICFR/COSO scope is required; legacy Boolean context is not sufficient.")
            grounding_notes.extend(scope_issues)
            if coso_context_supplied:
                grounding_notes.append("Legacy Boolean COSO context flag was ignored for scientific gating.")
        gates.append(GateResult("icfr_coso_grounding", grounding_ok, grounding_notes))

        if not all(g.passed for g in gates):
            missing = [g.gate for g in gates if not g.passed]
            result = LemonCaseResult(
                case_id=case_id,
                findings=[],
                gates=gates,
                contradictions=[],
                status=f"BLOCKED:{','.join(missing)}",
            )
            result.assurance_passport = None
            result.assurance_reasons = tuple(grounding_notes)
            return result

        hypotheses = provider.generate_hypotheses(case_id, evidence, question)
        legacy_hypotheses = self._legacy_hypothesis_records(hypotheses)

        store = evidence_store if evidence_store is not None else EvidenceStore()
        default_generator, default_reviewer_run, default_falsifier_run = self._default_runs(case_id, provider, created_at)
        generator = generator_run if generator_run is not None else default_generator
        reviewer_obj = reviewer if reviewer is not None else Reviewer(default_reviewer_run)
        falsifier_obj = falsifier if falsifier is not None else Falsifier(default_falsifier_run, store)

        decision = assure_case(
            case_id=case_id,
            question=question,
            created_at=created_at,
            legacy_hypotheses=legacy_hypotheses,
            store=store,
            scope=scope,
            repro=repro_ref,
            generator=generator,
            reviewer=reviewer_obj,
            falsifier=falsifier_obj,
            replay=replay_fn,
        )
        support_ok, reviewer_ok, falsification_ok = (
            decision.support_ok,
            decision.reviewer_ok,
            decision.falsification_ok,
        )
        decision_notes = list(decision.reasons)

        gates.append(
            GateResult(
                "evidence_sufficiency",
                support_ok,
                [] if support_ok else ["Assurance-core support assessment did not pass.", *decision_notes],
            )
        )

        # Legacy challenges remain output data only. They no longer determine any gate.
        challenges: list[Finding] = []
        if hypotheses:
            challenges = [provider.challenge_claim(case_id, evidence, h) for h in hypotheses]

        gates.extend(
            [
                GateResult(
                    "independent_review",
                    reviewer_ok,
                    [] if reviewer_ok else ["Assurance-core independent review did not pass.", *decision_notes],
                ),
                GateResult(
                    "falsification",
                    falsification_ok,
                    [] if falsification_ok else ["Assurance-core falsification did not survive.", *decision_notes],
                ),
                GateResult(
                    "reproducibility",
                    bool(reproducibility_ref),
                    [] if reproducibility_ref else ["Missing legacy reproducibility reference."],
                ),
                # A machine run can never pass this gate by itself.
                GateResult("human_approval", False, ["Authorized human disposition required."]),
            ]
        )

        contradictions = [c.claim for c in challenges if c.claim]
        status = "AWAITING_HUMAN_APPROVAL"
        if any(not g.passed for g in gates if g.gate != "human_approval"):
            status = "REVIEW_REQUIRED"

        result = LemonCaseResult(
            case_id=case_id,
            findings=hypotheses + challenges,
            gates=gates,
            contradictions=contradictions,
            status=status,
        )
        result.assurance_passport = decision.passport
        result.assurance_reasons = decision.reasons
        return result

    @staticmethod
    def required_gates() -> tuple[str, ...]:
        return _REQUIRED_GATES
