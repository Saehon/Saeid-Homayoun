from __future__ import annotations

import argparse
import json
from pathlib import Path

MANDATORY_FOR_DISCOVERY = [
    "literature_validation",
    "hypothesis_tournament",
    "dag_governance",
    "empirical_conversion",
    "provenance",
    "replication_or_oos",
    "adversarial_review",
    "falsification",
    "chain_of_evidence",
    "coe_audit",
    "economic_significance",
    "reproducibility",
]

METHOD_GATES = {
    "alphaevolve_inspired": "search_integrity",
    "computational_discovery": "search_integrity",
    "alphafold_inspired_latent_structure": "latent_structure_validation",
    "science_one_chain_of_evidence": "chain_of_evidence",
    "coe_audit": "coe_audit",
}


def validate_schema(record: dict, schema: dict) -> list[str]:
    try:
        import jsonschema
    except ImportError:
        return []
    validator = jsonschema.Draft202012Validator(schema)
    return [
        f"schema: {err.message}"
        for err in sorted(validator.iter_errors(record), key=lambda e: list(e.path))
    ]


def validate_governance(record: dict) -> list[str]:
    errors: list[str] = []
    gates = record.get("gates", {})
    methods = set(record.get("methods", []))
    human = record.get("human_gate", {})
    claim_allowed = bool(record.get("discovery_claim_allowed", False))
    evidence_class = record.get("evidence_class")

    # Method-specific gates must never be represented as complete when their
    # corresponding method-specific validation is absent.
    for method, gate in METHOD_GATES.items():
        if method in methods and claim_allowed and not gates.get(gate, False):
            errors.append(f"discovery blocked: method '{method}' requires gate '{gate}'")

    if claim_allowed:
        for gate in MANDATORY_FOR_DISCOVERY:
            if not gates.get(gate, False):
                errors.append(f"discovery blocked: mandatory gate '{gate}' is false")

        if evidence_class in {"causal", "structural_equilibrium"} and not gates.get("identification", False):
            errors.append("discovery blocked: causal/structural evidence requires identification gate")

        if "alphafold_inspired_latent_structure" in methods and not gates.get("latent_structure_validation", False):
            errors.append("discovery blocked: latent-structure method requires latent_structure_validation")

        if not human.get("approved", False):
            errors.append("discovery blocked: Human Gate is not approved")
        if not str(human.get("reviewer", "")).strip():
            errors.append("discovery blocked: Human Gate reviewer is missing")
        if not human.get("decision_date"):
            errors.append("discovery blocked: Human Gate decision_date is missing")

    # Scientific class cannot be silently inflated.
    if evidence_class == "causal" and not gates.get("identification", False):
        errors.append("evidence class 'causal' requires identification=true")
    if evidence_class == "replicated" and not gates.get("replication_or_oos", False):
        errors.append("evidence class 'replicated' requires replication_or_oos=true")

    # Science One / CoE integrity requirements.
    artifacts = record.get("artifacts", {})
    if gates.get("chain_of_evidence", False) and not artifacts.get("chain_of_evidence"):
        errors.append("chain_of_evidence gate is true but no chain_of_evidence artifact is recorded")
    if gates.get("coe_audit", False) and not artifacts.get("coe_audit"):
        errors.append("coe_audit gate is true but no coe_audit artifact is recorded")
    if gates.get("replication_or_oos", False) and not artifacts.get("replication_report"):
        errors.append("replication_or_oos gate is true but no replication_report artifact is recorded")
    if gates.get("adversarial_review", False) and not artifacts.get("red_team_report"):
        errors.append("adversarial_review gate is true but no red_team_report artifact is recorded")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an ECONOVA-S scientific discovery study manifest.")
    parser.add_argument("manifest", nargs="?", default="discovery/sample_study_manifest.json")
    parser.add_argument("--schema", default="discovery/study_manifest.schema.json")
    args = parser.parse_args()

    record = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    schema = json.loads(Path(args.schema).read_text(encoding="utf-8"))
    errors = validate_schema(record, schema) + validate_governance(record)

    if errors:
        print("SCIENTIFIC DISCOVERY MANIFEST: BLOCKED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("SCIENTIFIC DISCOVERY MANIFEST: VALID")
    print(f"study_id={record['study_id']}")
    print(f"evidence_class={record['evidence_class']}")
    print(f"discovery_claim_allowed={record['discovery_claim_allowed']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
