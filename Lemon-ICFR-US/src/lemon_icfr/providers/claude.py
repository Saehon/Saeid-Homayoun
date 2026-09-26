from __future__ import annotations

from collections.abc import Callable
from typing import Any

from lemon_icfr.models import EvidenceItem, Finding


class ClaudeFinanceAdapter:
    """
    Thin provider adapter for Claude-backed financial/ICFR workflows.

    The adapter deliberately receives a callable rather than embedding credentials
    or binding Lemon's assurance logic to one SDK. The callable can wrap Claude
    Code, an Anthropic API client, an MCP-enabled service, or a test double.
    """

    name = "claude-finance-adapter"

    def __init__(self, call_fn: Callable[[dict[str, Any]], dict[str, Any]], model_version: str):
        self._call_fn = call_fn
        self._model_version = model_version

    def lineage(self) -> str:
        return f"{self.name}:{self._model_version}"

    def generate_hypotheses(
        self, case_id: str, evidence: list[EvidenceItem], question: str
    ) -> list[Finding]:
        payload = {
            "task": "generate_competing_icfr_hypotheses",
            "case_id": case_id,
            "question": question,
            "evidence": [
                {
                    "evidence_id": e.evidence_id,
                    "source": e.source,
                    "provenance": e.provenance,
                    "rights_status": e.rights_status,
                    "content": e.content,
                    "version": e.version,
                }
                for e in evidence
            ],
            "requirements": {
                "multiple_competing_hypotheses": True,
                "cite_evidence_ids": True,
                "separate_fact_from_inference": True,
                "human_review_required": True,
            },
        }
        response = self._call_fn(payload)
        findings: list[Finding] = []
        for item in response.get("hypotheses", []):
            findings.append(
                Finding(
                    agent="co-scientist",
                    claim=str(item.get("claim", "")),
                    evidence_refs=list(item.get("evidence_refs", [])),
                    assumptions=list(item.get("assumptions", [])),
                    alternative_explanations=list(item.get("alternatives", [])),
                    limitations=list(item.get("limitations", [])),
                    model_tool_version=self.lineage(),
                    requires_human_review=True,
                )
            )
        return findings

    def challenge_claim(
        self, case_id: str, evidence: list[EvidenceItem], finding: Finding
    ) -> Finding:
        payload = {
            "task": "falsify_icfr_claim",
            "case_id": case_id,
            "claim": finding.claim,
            "evidence_refs": finding.evidence_refs,
            "evidence": [
                {"evidence_id": e.evidence_id, "content": e.content, "source": e.source}
                for e in evidence
            ],
            "requirements": {
                "seek_contradictions": True,
                "seek_missing_evidence": True,
                "test_alternative_explanations": True,
                "do_not_approve_final_conclusion": True,
            },
        }
        response = self._call_fn(payload)
        return Finding(
            agent="independent-falsification",
            claim=str(response.get("challenge", "No challenge returned.")),
            evidence_refs=list(response.get("evidence_refs", [])),
            assumptions=list(response.get("assumptions", [])),
            alternative_explanations=list(response.get("alternatives", [])),
            limitations=list(response.get("limitations", [])),
            model_tool_version=self.lineage(),
            requires_human_review=True,
        )
