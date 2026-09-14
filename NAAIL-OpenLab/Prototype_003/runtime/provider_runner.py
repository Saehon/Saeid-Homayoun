from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, List

import prototype003 as p003
from providers import BaseProvider, ProviderConfigurationError, build_provider


ARCHITECTURES = ("single_agent", "sequential_agents", "governed_multi_agent")

SYSTEM = """You are participating in a frozen synthetic audit-research benchmark.
Use only the evidence included in the prompt. Do not invent evidence IDs, facts, standards, or audit conclusions.
This is not a real audit and not an audit opinion. Return JSON only. Never approve the Human Gate.
Gold labels are withheld. Your task is to analyze the evidence independently."""

FINAL_SCHEMA = {
    "exceptions": ["string"],
    "proposed_adjustment": "number",
    "evidence_ids": ["string"],
    "risks": ["string"],
    "assertions": ["string"],
    "procedures": ["string"],
    "limitations": ["string"],
    "skepticism_checks": ["string"],
}


def public_case(case: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in case.items() if k != "gold"}


def _prompt(case: Dict[str, Any], task: str, context: Any | None = None) -> str:
    payload = {
        "task": task,
        "case": public_case(case),
        "prior_context": context,
        "required_final_schema": FINAL_SCHEMA,
        "rules": [
            "Use only evidence IDs present in the case.",
            "Do not infer or reconstruct hidden gold labels.",
            "proposed_adjustment must be numeric.",
            "Return only one JSON object.",
        ],
    }
    return json.dumps(payload, indent=2)


def single_agent(provider: BaseProvider, case: Dict[str, Any]) -> Dict[str, Any]:
    return provider.generate_json(
        SYSTEM,
        _prompt(
            case,
            "Act as a single audit-analysis agent. Identify supported exceptions, quantify any proposed adjustment, identify relevant risks/assertions/procedures, cite evidence IDs, record limitations and professional-skepticism checks, and return the required final schema.",
        ),
    )


def sequential_agents(provider: BaseProvider, case: Dict[str, Any]) -> Dict[str, Any]:
    evidence = provider.generate_json(
        SYSTEM,
        _prompt(
            case,
            "Evidence Agent: summarize relevant evidence, contradictions, timing facts and valid evidence IDs. Do not make the final audit conclusion.",
        ),
    )
    risk = provider.generate_json(
        SYSTEM,
        _prompt(
            case,
            "Risk/Accounting Agent: using the case and prior Evidence Agent output, identify candidate exceptions, risks, assertions, procedures and quantitative implications. Do not approve any conclusion.",
            evidence,
        ),
    )
    return provider.generate_json(
        SYSTEM,
        _prompt(
            case,
            "Review Agent: independently review the prior outputs against the original evidence, correct unsupported statements, and return only the required final schema.",
            {"evidence_agent": evidence, "risk_accounting_agent": risk},
        ),
    )


def governed_multi_agent(provider: BaseProvider, case: Dict[str, Any]) -> Dict[str, Any]:
    evidence = provider.generate_json(
        SYSTEM,
        _prompt(case, "Evidence Agent: create an evidence-grounded fact map with only valid evidence IDs."),
    )
    risk = provider.generate_json(
        SYSTEM,
        _prompt(case, "Audit Risk Agent: identify risks and assertions supported by the original case and Evidence Agent output.", evidence),
    )
    accounting = provider.generate_json(
        SYSTEM,
        _prompt(
            case,
            "Accounting/Procedure Agent: identify candidate exceptions, adjustment amount and audit procedures using the case plus prior evidence/risk outputs.",
            {"evidence_agent": evidence, "risk_agent": risk},
        ),
    )
    critic = provider.generate_json(
        SYSTEM,
        _prompt(
            case,
            "Critic/Falsifier Agent: attack unsupported conclusions, search for contradictory evidence, check arithmetic and evidence IDs, and list corrections. Do not produce an approval.",
            {"evidence_agent": evidence, "risk_agent": risk, "accounting_agent": accounting},
        ),
    )
    return provider.generate_json(
        SYSTEM,
        _prompt(
            case,
            "Supervisor Agent: adjudicate the specialist and critic outputs against the original evidence. Return only the required final schema. Preserve uncertainty and limitations. Do not approve the Human Gate.",
            {
                "evidence_agent": evidence,
                "risk_agent": risk,
                "accounting_agent": accounting,
                "critic_falsifier": critic,
            },
        ),
    )


def normalize(case: Dict[str, Any], raw: Dict[str, Any], provider: BaseProvider, architecture: str) -> Dict[str, Any]:
    allowed_evidence = {e["evidence_id"] for e in case["evidence"]}
    evidence_ids = [str(x) for x in raw.get("evidence_ids", [])]
    invalid_evidence = sorted(set(evidence_ids) - allowed_evidence)

    def list_of_strings(key: str) -> List[str]:
        value = raw.get(key, [])
        if not isinstance(value, list):
            return []
        return [str(x) for x in value]

    try:
        adjustment = float(raw.get("proposed_adjustment", 0))
    except (TypeError, ValueError):
        adjustment = 0.0

    artifact: Dict[str, Any] = {
        "case_id": case["case_id"],
        "architecture": architecture,
        "execution_status": "EXECUTED_REAL_PROVIDER",
        "provider": provider.info.provider,
        "model": provider.info.model,
        "exceptions": sorted(set(list_of_strings("exceptions"))),
        "proposed_adjustment": adjustment,
        "evidence_ids": evidence_ids,
        "invalid_evidence_ids": invalid_evidence,
        "risks": list_of_strings("risks"),
        "assertions": list_of_strings("assertions"),
        "procedures": list_of_strings("procedures"),
        "limitations": list_of_strings("limitations"),
        "skepticism_checks": list_of_strings("skepticism_checks"),
        "human_gate": "PENDING_HUMAN_APPROVAL",
        "claim_status": "PROVIDER_BENCHMARK_RESULT_PENDING_HUMAN_REVIEW",
        "input_hashes": p003.frozen_inputs(case),
        "evidence_passport": p003.evidence_passport(case),
        "provider_raw_final": raw,
    }
    artifact["decision_dag"] = p003.decision_dag(artifact)
    artifact["artifact_hash"] = p003.canonical_hash(artifact)
    return artifact


def evaluate(case: Dict[str, Any], artifact: Dict[str, Any]) -> Dict[str, Any]:
    core = p003.classification_metrics(artifact["exceptions"], case["gold"]["exceptions"])
    expected_assertions = set(case["gold"].get("expected_assertions", []))
    allowed_evidence = {e["evidence_id"] for e in case["evidence"]}
    valid_evidence = set(artifact["evidence_ids"]) & allowed_evidence
    aa = len(set(artifact["assertions"]) & expected_assertions) / max(1, len(expected_assertions))
    eg = len(valid_evidence) / max(1, len(allowed_evidence))
    rpa = min(1.0, len(artifact["procedures"]) / max(1, len(artifact["risks"])))
    ps = min(1.0, 0.5 * bool(artifact["limitations"]) + 0.5 * bool(artifact["skepticism_checks"]))
    required = ("exceptions", "evidence_ids", "risks", "assertions", "procedures", "limitations")
    ds = sum(bool(artifact.get(k)) for k in required) / len(required)
    return {
        "RPA": round(rpa, 4),
        "AA": round(aa, 4),
        "EG": round(eg, 4),
        "PS": round(ps, 4),
        "DS": round(ds, 4),
        "DIST": None,
        **core,
        "adjustment_matches_gold": artifact["proposed_adjustment"] == float(case["gold"]["proposed_adjustment"]),
        "invalid_evidence_count": len(artifact["invalid_evidence_ids"]),
        "human_gate_enforced": artifact["human_gate"] == "PENDING_HUMAN_APPROVAL",
        "unsupported_discovery_claim": False,
    }


def run_architecture(provider: BaseProvider, case: Dict[str, Any], architecture: str) -> Dict[str, Any]:
    if architecture == "single_agent":
        raw = single_agent(provider, case)
    elif architecture == "sequential_agents":
        raw = sequential_agents(provider, case)
    elif architecture == "governed_multi_agent":
        raw = governed_multi_agent(provider, case)
    else:
        raise ValueError(f"Unsupported architecture: {architecture}")
    artifact = normalize(case, raw, provider, architecture)
    return {"artifact": artifact, "metrics": evaluate(case, artifact)}


def missing_configuration(provider_name: str) -> List[str]:
    if provider_name == "gemini":
        return [] if os.getenv("GEMINI_API_KEY") else ["GEMINI_API_KEY"]
    names = ("AZURE_INFERENCE_ENDPOINT", "AZURE_INFERENCE_CREDENTIAL", "AZURE_INFERENCE_MODEL")
    return [name for name in names if not os.getenv(name)]


def main() -> None:
    base = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="Run Prototype 004 real-provider comparison on the frozen Revenue benchmark.")
    parser.add_argument("--provider", choices=("gemini", "foundry"), required=True)
    parser.add_argument("--architecture", choices=ARCHITECTURES + ("all",), default="all")
    parser.add_argument("--case", default=str(base / "data" / "revenue_case.json"))
    parser.add_argument("--out", default=None)
    parser.add_argument("--allow-missing", action="store_true")
    args = parser.parse_args()

    case = p003.load_case(Path(args.case))
    missing = missing_configuration(args.provider)
    output = Path(args.out or (base / "outputs" / f"provider_{args.provider}.json"))
    output.parent.mkdir(parents=True, exist_ok=True)

    if missing and args.allow_missing:
        result = {
            "provider": args.provider,
            "execution_status": "NOT_EXECUTED_PROVIDER_REQUIRED",
            "missing_configuration": missing,
            "input_hashes": p003.frozen_inputs(case),
            "research_claim": "NO_PROVIDER_RESULT",
        }
        output.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(json.dumps(result, indent=2))
        return

    try:
        provider = build_provider(args.provider)
    except ProviderConfigurationError:
        if args.allow_missing:
            raise AssertionError("Configuration precheck and provider construction disagree.")
        raise

    architectures = ARCHITECTURES if args.architecture == "all" else (args.architecture,)
    runs = {architecture: run_architecture(provider, case, architecture) for architecture in architectures}
    result = {
        "provider": provider.info.provider,
        "model": provider.info.model,
        "case_id": case["case_id"],
        "input_hashes": p003.frozen_inputs(case),
        "runs": runs,
        "research_claim": "NO_SUPERIORITY_CLAIM_UNTIL_CROSS_PROVIDER_REPLICATION_AND_HUMAN_REVIEW",
        "human_gate": "PENDING_HUMAN_APPROVAL",
    }
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"Executed {len(runs)} real-provider architecture run(s): {provider.info.provider}/{provider.info.model}")
    print(f"Saved: {output}")


if __name__ == "__main__":
    main()
