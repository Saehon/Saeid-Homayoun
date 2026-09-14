from __future__ import annotations

import argparse
import hashlib
import json
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Protocol, Any

ROLE_SEQUENCE = [
    "explorer",
    "theory_dag",
    "empirical_design",
    "independent_replicator",
    "scientific_red_team",
    "welfare_reviewer",
    "evidence_passport",
]

STOP_REASONS = {
    "missing_evidence",
    "provenance_failed",
    "chronology_failed",
    "construct_invalid",
    "identification_invalid",
    "replication_failed",
    "red_team_unresolved",
    "welfare_incomplete",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def canonical_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_json(obj: Any) -> str:
    return hashlib.sha256(canonical_json(obj).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class AgentResult:
    claim: str
    method: str
    assumptions: list[str]
    confidence: float
    contradictions: list[str]
    failed: bool = False
    failure_reasons: list[str] | None = None
    evidence: list[dict] | None = None
    required_next_action: str = "continue"


class AgentAdapter(Protocol):
    name: str
    version: str

    def run(self, role: str, payload: dict) -> AgentResult:
        ...


class DeterministicDemoAdapter:
    """Offline adapter used only to test orchestration and governance."""

    name = "deterministic-demo-adapter"
    version = "1.0"

    def run(self, role: str, payload: dict) -> AgentResult:
        question = payload["question"]
        evidence = payload.get("evidence", [])
        base = f"{role} processed: {question}"
        if role == "explorer":
            return AgentResult(base + " | generated competing hypotheses", "deterministic hypothesis enumeration", ["research question is non-empty"], 0.55, [], evidence=evidence)
        if role == "theory_dag":
            return AgentResult(base + " | mapped constructs and causal paths", "rule-based DAG mapping", ["causal language remains provisional"], 0.60, [], evidence=evidence)
        if role == "empirical_design":
            return AgentResult(base + " | specified variables, chronology, estimators, and falsification", "frozen empirical-design template", ["authoritative data sources will be used"], 0.62, [], evidence=evidence)
        if role == "independent_replicator":
            return AgentResult(base + " | independent reconstruction feasible", "isolated reconstruction from prior handoff contract", ["replicator does not receive hidden generator reasoning"], 0.58, [], evidence=evidence)
        if role == "scientific_red_team":
            return AgentResult(base + " | no blocking governance defect detected in demo", "adversarial checklist", ["demo validates orchestration, not scientific truth"], 0.52, ["agent agreement is not scientific validation"], evidence=evidence)
        if role == "welfare_reviewer":
            return AgentResult(base + " | private/social value distinction required", "economic welfare checklist", ["welfare analysis may be not-applicable for some studies"], 0.50, [], evidence=evidence)
        if role == "evidence_passport":
            return AgentResult(base + " | provenance chain sealed", "deterministic evidence-passport assembly", ["human gate remains external"], 0.99, [], evidence=evidence, required_next_action="human_gate")
        raise ValueError(f"Unknown role: {role}")


class Orchestrator:
    def __init__(self, adapters: dict[str, AgentAdapter] | None = None):
        self.adapters = adapters or {role: DeterministicDemoAdapter() for role in ROLE_SEQUENCE}

    @staticmethod
    def _check_independence(role: str, previous_role: str | None, adapter: AgentAdapter, previous_adapter: AgentAdapter | None) -> dict:
        criteria = {
            "separate_role": previous_role is None or role != previous_role,
            "isolated_contract_only": role in {"independent_replicator", "scientific_red_team"},
            "different_model_or_tool": previous_adapter is None or (adapter.name != previous_adapter.name or adapter.version != previous_adapter.version),
        }
        independence_class = "role_independent_only" if not criteria["different_model_or_tool"] else "role_and_tool_independent"
        return {"class": independence_class, "criteria": criteria}

    def run(self, question: str, evidence: list[dict] | None = None, run_id: str | None = None) -> dict:
        if not question or not question.strip():
            raise ValueError("question must be non-empty")

        run_id = run_id or str(uuid.uuid4())
        task_id = "econova-scientific-run"
        evidence = evidence or []
        handoffs: list[dict] = []
        parent_hash: str | None = None
        previous_role: str | None = None
        previous_adapter: AgentAdapter | None = None
        stop = False

        for role in ROLE_SEQUENCE:
            if stop:
                break
            adapter = self.adapters[role]
            payload = {"question": question, "evidence": evidence, "prior_handoffs": handoffs, "run_id": run_id}
            result = adapter.run(role, payload)
            receiver = ROLE_SEQUENCE[ROLE_SEQUENCE.index(role) + 1] if role != ROLE_SEQUENCE[-1] else "human_gate"
            failure_reasons = result.failure_reasons or []
            risk_flags = [reason for reason in failure_reasons if reason in STOP_REASONS]
            record = {
                "task_id": task_id,
                "run_id": run_id,
                "sender": role,
                "receiver": receiver,
                "claim": result.claim,
                "evidence": result.evidence or evidence,
                "method": result.method,
                "assumptions": result.assumptions,
                "confidence": result.confidence,
                "contradictions": result.contradictions,
                "failure_status": {"failed": bool(result.failed), "reasons": failure_reasons},
                "provenance": {"model_or_tool": adapter.name, "version": adapter.version, "timestamp_utc": utc_now(), "prompt_or_config_sha256": None, "code_commit": None},
                "required_next_action": result.required_next_action,
                "parent_content_sha256": parent_hash,
                "independence": self._check_independence(role, previous_role, adapter, previous_adapter),
                "risk_flags": risk_flags,
                "content_sha256": "",
            }
            record["content_sha256"] = sha256_json({key: value for key, value in record.items() if key != "content_sha256"})
            handoffs.append(record)
            parent_hash = record["content_sha256"]
            previous_role = role
            previous_adapter = adapter
            stop = bool(result.failed and risk_flags)

        chain = {
            "project": "ECONOVA-S",
            "run_id": run_id,
            "question": question,
            "handoffs": handoffs,
            "chain_length": len(handoffs),
            "stopped": stop,
            "human_gate_required": True,
            "human_gate_approved": False,
            "agent_consensus_is_scientific_truth": False,
            "discovery_claim_allowed": False,
        }
        chain["chain_sha256"] = sha256_json({key: value for key, value in chain.items() if key != "chain_sha256"})
        return chain


def validate_chain(chain: dict) -> list[str]:
    errors: list[str] = []
    handoffs = chain.get("handoffs", [])
    if not isinstance(handoffs, list) or not handoffs:
        return ["handoffs must be a non-empty list"]

    expected_parent = None
    for index, record in enumerate(handoffs):
        actual = sha256_json({key: value for key, value in record.items() if key != "content_sha256"})
        if actual != record.get("content_sha256"):
            errors.append(f"handoff[{index}] content hash mismatch")
        if record.get("parent_content_sha256") != expected_parent:
            errors.append(f"handoff[{index}] parent hash mismatch")
        if record.get("sender") == record.get("receiver"):
            errors.append(f"handoff[{index}] sender and receiver must differ")
        expected_parent = record.get("content_sha256")

    expected_chain = sha256_json({key: value for key, value in chain.items() if key != "chain_sha256"})
    if expected_chain != chain.get("chain_sha256"):
        errors.append("chain hash mismatch")
    if chain.get("human_gate_required") is not True:
        errors.append("human gate must be required")
    if chain.get("discovery_claim_allowed") is not False:
        errors.append("discovery claim must remain false in automation")
    if chain.get("agent_consensus_is_scientific_truth") is not False:
        errors.append("agent consensus must not be treated as scientific truth")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the ECONOVA-S deterministic AI-to-AI orchestration demo.")
    parser.add_argument("--question", default="When does data become information and economic value?")
    parser.add_argument("--output", default="automation/artifacts/demo_chain.json")
    args = parser.parse_args()

    chain = Orchestrator().run(args.question)
    errors = validate_chain(chain)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(chain, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {output}")
    print(f"chain_sha256={chain['chain_sha256']}")
    print("discovery_claim_allowed=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
