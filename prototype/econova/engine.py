from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import hashlib
import json
import os
from typing import Any

from .prompts import STABLE_CORE, DISCOVERY_TASK, ERA_TASK, RED_TEAM_TASK


@dataclass
class StageRecord:
    name: str
    response_id: str | None
    model: str
    reasoning_effort: str
    output: str


@dataclass
class HumanDecision:
    decision: str
    reviewer: str
    note: str


class EconovaEngine:
    """GPT-5.6 Sol backend for the ECONOVA-S governed scientific workflow."""

    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
        reasoning_effort: str | None = None,
        allow_web_search: bool = False,
    ):
        from openai import OpenAI
        self.model = model or os.getenv("ECONOVA_MODEL", "gpt-5.6-sol")
        self.reasoning_effort = reasoning_effort or os.getenv("ECONOVA_REASONING", "high")
        self.allow_web_search = allow_web_search
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))

    def _call(self, stage: str, prompt: str) -> StageRecord:
        kwargs: dict[str, Any] = {
            "model": self.model,
            "reasoning": {"effort": self.reasoning_effort},
            "instructions": STABLE_CORE,
            "input": prompt,
        }
        if self.allow_web_search:
            kwargs["tools"] = [{"type": "web_search_preview"}]

        response = self.client.responses.create(**kwargs)
        return StageRecord(
            name=stage,
            response_id=getattr(response, "id", None),
            model=getattr(response, "model", self.model),
            reasoning_effort=self.reasoning_effort,
            output=response.output_text,
        )

    def discovery(self, question: str, context: str = "") -> StageRecord:
        return self._call(
            "systems_map_and_hypothesis_tournament",
            DISCOVERY_TASK.format(question=question.strip(), context=context.strip() or "None supplied."),
        )

    def empirical_design(self, question: str, discovery_output: str) -> StageRecord:
        return self._call(
            "era_empirical_design",
            ERA_TASK.format(question=question.strip(), discovery=discovery_output),
        )

    def red_team(self, question: str, discovery_output: str, era_output: str) -> StageRecord:
        return self._call(
            "independent_scientific_red_team",
            RED_TEAM_TASK.format(
                question=question.strip(),
                discovery=discovery_output,
                era=era_output,
            ),
        )


def make_evidence_passport(
    question: str,
    context: str,
    stages: list[StageRecord],
    human: HumanDecision,
    web_search_enabled: bool,
) -> dict[str, Any]:
    """Deterministic Evidence Passport. The model cannot approve itself."""
    now = datetime.now(timezone.utc).isoformat()
    content = "\n".join([question, context] + [s.output for s in stages])
    fingerprint = hashlib.sha256(content.encode("utf-8")).hexdigest()

    approved = human.decision.upper() == "APPROVE FOR NEXT STAGE"
    return {
        "project": "ECONOVA-S",
        "prototype": "GPT-5.6 Sol Product Prototype v0.1",
        "created_at_utc": now,
        "research_question": question,
        "input_context_supplied": bool(context.strip()),
        "model_backend": stages[0].model if stages else None,
        "reasoning_effort": stages[0].reasoning_effort if stages else None,
        "web_search_enabled": web_search_enabled,
        "stages": [asdict(s) for s in stages],
        "scientific_classification": "design-stage / no empirical finding",
        "gates": {
            "systems_map": True,
            "hypothesis_tournament": True,
            "era_design": True,
            "independent_red_team": True,
            "real_data_provenance": False,
            "construct_validation": False,
            "credible_identification": False,
            "external_replication": False,
            "oos_validation": False,
            "economic_significance": False,
            "welfare_validation": False,
            "human_gate": approved,
        },
        "human_decision": asdict(human),
        "discovery_claim_allowed": False,
        "next_stage_allowed": approved,
        "content_sha256": fingerprint,
        "governing_rule": "AI explores; economics constrains; evidence verifies; humans approve.",
    }


def passport_json(passport: dict[str, Any]) -> str:
    return json.dumps(passport, indent=2, ensure_ascii=False)
