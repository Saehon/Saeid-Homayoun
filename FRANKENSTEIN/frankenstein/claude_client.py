from __future__ import annotations

import json
import os
from typing import Any

from anthropic import Anthropic
from pydantic import ValidationError

from .agents import AgentSpec, LEADER_NAME
from .schemas import FrankensteinReport, SpecialistAssessment

DEFAULT_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-5")


def _message_text(message: Any) -> str:
    return "\n".join(
        getattr(block, "text", "")
        for block in getattr(message, "content", [])
        if getattr(block, "type", None) == "text"
    ).strip()


def _json_object(text: str) -> dict[str, Any]:
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise ValueError("Model response did not contain a JSON object.")
    return json.loads(text[start:end + 1])


class ClaudeClient:
    def __init__(self, model: str | None = None) -> None:
        self.model = model or DEFAULT_MODEL
        self.client = Anthropic()

    def specialist(self, spec: AgentSpec, objective: str, evidence: dict[str, Any]) -> SpecialistAssessment:
        system = f"""You are the {spec.name}, a specialist in FRANKENSTEIN, an evidence-governed NAAIL programme.
Domain: {spec.domain}
Mandate: {spec.mandate}

Rules:
1. Treat deterministic findings as risk indicators, not proof of fraud, error, noncompliance, or control failure.
2. Tie each material statement to supplied finding IDs/rule IDs or explicitly state that evidence is missing.
3. Never invent accounting standards, regulatory requirements, source documents, or facts.
4. Request corroborating evidence when needed.
5. Do not issue an audit opinion or make autonomous accounting/control changes.
6. Return one JSON object only with keys: agent_name, domain, risk_summary, key_risks, evidence_references, tests_requested, recommended_actions, limitations.
"""
        message = self.client.messages.create(
            model=self.model,
            max_tokens=2200,
            system=system,
            messages=[{"role": "user", "content": json.dumps({"objective": objective, "evidence": evidence}, indent=2)}],
        )
        raw = _message_text(message)
        try:
            obj = _json_object(raw)
            obj["agent_name"] = spec.name
            obj["domain"] = spec.domain
            return SpecialistAssessment.model_validate(obj)
        except (ValueError, json.JSONDecodeError, ValidationError):
            return SpecialistAssessment(
                agent_name=spec.name,
                domain=spec.domain,
                risk_summary=raw or "No usable structured specialist output.",
                limitations=["Specialist output failed structured validation; human review is required."],
            )

    def leader(self, objective: str, risk_score: int, specialists: list[SpecialistAssessment],
               evidence_refs: list[str], limitations: list[str]) -> FrankensteinReport:
        system = f"""You are the {LEADER_NAME}.
Synthesize specialist work into a concise evidence-grounded decision-support report.
Do not issue an audit opinion, conclude fraud, declare IFRS/regulatory compliance, or independently declare a material weakness.
Preserve uncertainty and disagreement. Set human_review_required=true.
Return one JSON object with keys: executive_summary, audit_objective, deterministic_risk_score, cross_domain_risks, evidence_references, recommended_actions, limitations, human_review_required.
"""
        payload = {
            "audit_objective": objective,
            "deterministic_risk_score": risk_score,
            "specialists": [s.model_dump() for s in specialists],
            "evidence_references": evidence_refs,
            "deterministic_limitations": limitations,
        }
        message = self.client.messages.create(
            model=self.model,
            max_tokens=3000,
            system=system,
            messages=[{"role": "user", "content": json.dumps(payload, indent=2)}],
        )
        raw = _message_text(message)
        try:
            obj = _json_object(raw)
            obj["audit_objective"] = objective
            obj["deterministic_risk_score"] = risk_score
            obj["specialist_assessments"] = specialists
            obj["human_review_required"] = True
            return FrankensteinReport.model_validate(obj)
        except (ValueError, json.JSONDecodeError, ValidationError):
            return FrankensteinReport(
                executive_summary=raw or "Leader synthesis failed structured validation.",
                audit_objective=objective,
                deterministic_risk_score=risk_score,
                specialist_assessments=specialists,
                evidence_references=evidence_refs,
                limitations=limitations + ["Leader output failed structured validation; human review is required."],
                human_review_required=True,
            )
