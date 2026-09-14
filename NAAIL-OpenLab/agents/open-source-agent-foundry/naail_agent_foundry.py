"""NAAIL OpenLab™ — Open-Source Academic Agent Foundry scaffold.

Research-safe public code. This module does not execute external LLMs or transmit
client data. It provides dependency discovery plus a provider-neutral plan for
NAAIL Professional Swarm™ simulations.

Validated NAAIL release remains v0.2.3. This file is a v0.2.4 target capability.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from importlib.util import find_spec
from pathlib import Path
from typing import Iterable
import json


@dataclass(frozen=True)
class DependencyStatus:
    name: str
    import_name: str
    available: bool
    intended_role: str


@dataclass(frozen=True)
class SwarmRole:
    role: str
    responsibility: str
    material_conclusion_authority: bool = False


DEFAULT_ROLES: tuple[SwarmRole, ...] = (
    SwarmRole("planner", "Decompose the professional or research problem."),
    SwarmRole("researcher", "Collect traceable evidence within the approved evidence policy."),
    SwarmRole("analyst", "Perform reproducible quantitative or qualitative analysis."),
    SwarmRole("specialist", "Apply domain-specific professional knowledge."),
    SwarmRole("critic", "Challenge assumptions, evidence sufficiency, and reasoning."),
    SwarmRole("defender", "Respond to criticism using traceable evidence rather than rhetoric."),
    SwarmRole("falsifier", "Search for counter-evidence and conditions that overturn the conclusion."),
    SwarmRole("professional_reviewer", "Review the evidence chain and unresolved disagreements."),
    SwarmRole(
        "human_gate",
        "Human approval/rejection/escalation for material scientific or professional conclusions.",
        material_conclusion_authority=True,
    ),
)


OPTIONAL_DEPENDENCIES: tuple[tuple[str, str, str], ...] = (
    ("Stanford DSPy", "dspy", "LM-program/RAG optimization and evaluation-driven comparison"),
    ("Stanford STORM / Co-STORM", "knowledge_storm", "multi-perspective evidence curation"),
    ("Hugging Face smolagents", "smolagents", "tool-calling/code-agent and managed-agent execution"),
)


def dependency_status() -> list[DependencyStatus]:
    """Return local availability of optional executable dependencies."""
    return [
        DependencyStatus(
            name=name,
            import_name=import_name,
            available=find_spec(import_name) is not None,
            intended_role=role,
        )
        for name, import_name, role in OPTIONAL_DEPENDENCIES
    ]


def build_swarm_plan(
    case_id: str,
    domain: str,
    evidence_ids: Iterable[str],
    initial_human_judgment: str,
) -> dict:
    """Build a deterministic, provider-neutral NAAIL Professional Swarm plan.

    This function deliberately does not call an LLM. External agent frameworks
    can be connected later behind the same evidence and Human Gate contract.
    """
    evidence = sorted({item.strip() for item in evidence_ids if item.strip()})
    if not evidence:
        raise ValueError("At least one approved evidence_id is required.")
    if not initial_human_judgment.strip():
        raise ValueError("An initial human/student judgment is required before agent advice.")

    return {
        "case_id": case_id,
        "domain": domain,
        "initial_human_judgment": initial_human_judgment,
        "approved_evidence_ids": evidence,
        "roles": [asdict(role) for role in DEFAULT_ROLES],
        "decision_rule": "EVIDENCE_GOVERNED_NOT_CONSENSUS_GOVERNED",
        "required_artifacts": [
            "Evidence Passport",
            "Professional Decision DAG",
            "critic_defender_disagreement_log",
            "falsification_record",
            "limitations",
            "human_gate_status",
        ],
        "human_gate_status": "PENDING_HUMAN_APPROVAL",
    }


def load_registry() -> dict:
    """Load the upstream dependency/research-inspiration registry."""
    path = Path(__file__).with_name("registry.json")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    print("NAAIL OpenLab™ — Open-Source Academic Agent Foundry")
    print("Optional dependency status:")
    for dep in dependency_status():
        marker = "READY" if dep.available else "NOT_INSTALLED"
        print(f"- {dep.name}: {marker} — {dep.intended_role}")

    registry = load_registry()
    print(f"Registry schema: {registry['schema_version']}")
    print(f"NAAIL target: {registry['naail_target']}")
    print(f"Validated release unchanged: {registry['validated_release_unchanged']}")


if __name__ == "__main__":
    main()
