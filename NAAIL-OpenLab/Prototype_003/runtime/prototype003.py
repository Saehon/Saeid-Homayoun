from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List
import argparse
import hashlib
import json
import time

ARCHITECTURES = (
    "deterministic",
    "single_agent",
    "sequential_agents",
    "governed_multi_agent",
)

REQUIRED_ARTIFACT_FIELDS = {
    "case_id",
    "architecture",
    "exceptions",
    "proposed_adjustment",
    "evidence_ids",
    "risks",
    "assertions",
    "procedures",
    "limitations",
    "human_gate",
    "claim_status",
}


def canonical_hash(obj: Any) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load_case(path: Path) -> Dict[str, Any]:
    case = json.loads(path.read_text(encoding="utf-8"))
    required = {"case_id", "period_end", "materiality", "transactions", "evidence", "gold"}
    missing = required - set(case)
    if missing:
        raise ValueError(f"Case missing keys: {sorted(missing)}")
    return case


def frozen_inputs(case: Dict[str, Any]) -> Dict[str, str]:
    return {
        "case_hash": canonical_hash({k: v for k, v in case.items() if k != "gold"}),
        "gold_hash": canonical_hash(case["gold"]),
    }


def evidence_passport(case: Dict[str, Any]) -> Dict[str, Any]:
    items = []
    for evidence in case["evidence"]:
        items.append(
            {
                "evidence_id": evidence["evidence_id"],
                "source_type": evidence["source_type"],
                "rights": evidence["rights"],
                "content_hash": canonical_hash(evidence),
            }
        )
    return {
        "case_id": case["case_id"],
        "items": items,
        "passport_hash": canonical_hash(items),
    }


def detect_cutoff_exceptions(case: Dict[str, Any]) -> List[str]:
    period_end = case["period_end"]
    return sorted(
        tx["transaction_id"]
        for tx in case["transactions"]
        if tx["delivery_date"] > period_end
    )


def proposed_adjustment(case: Dict[str, Any], exceptions: List[str]) -> float:
    exception_set = set(exceptions)
    return float(
        sum(
            tx["amount"]
            for tx in case["transactions"]
            if tx["transaction_id"] in exception_set
        )
    )


def evidence_agent(case: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "agent": "EvidenceAgent",
        "evidence_ids": sorted(e["evidence_id"] for e in case["evidence"]),
        "traceable": all(bool(e.get("source_type")) for e in case["evidence"]),
    }


def risk_agent(case: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "agent": "AuditRiskAgent",
        "risks": ["revenue_cutoff", "premature_revenue_recognition"],
        "assertions": ["occurrence", "cutoff"],
        "procedures": [
            "inspect_delivery_evidence",
            "reconcile_year_end_transactions",
        ],
    }


def accounting_agent(case: Dict[str, Any]) -> Dict[str, Any]:
    exceptions = detect_cutoff_exceptions(case)
    return {
        "agent": "AccountingAgent",
        "exceptions": exceptions,
        "proposed_adjustment": proposed_adjustment(case, exceptions),
        "conclusion": "potential_cutoff_misstatement" if exceptions else "no_exception_detected",
    }


def rights_agent(case: Dict[str, Any]) -> Dict[str, Any]:
    allowed = all(e.get("rights") in {"synthetic", "public", "licensed"} for e in case["evidence"])
    return {"agent": "RightsLicenseAgent", "rights_gate_passed": allowed}


def critic_agent(artifact: Dict[str, Any]) -> Dict[str, Any]:
    critiques: List[str] = []
    if not artifact.get("evidence_ids"):
        critiques.append("No traceable evidence IDs.")
    if not artifact.get("limitations"):
        critiques.append("Limitations not documented.")
    if artifact.get("exceptions") and artifact.get("proposed_adjustment", 0) <= 0:
        critiques.append("Exception set is inconsistent with proposed adjustment.")
    return {
        "agent": "CriticAgent",
        "critiques": critiques,
        "passed": not critiques,
    }


def replicator_agent(case: Dict[str, Any], artifact: Dict[str, Any]) -> Dict[str, Any]:
    replay = detect_cutoff_exceptions(case)
    return {
        "agent": "ReplicatorAgent",
        "replay_exceptions": replay,
        "reproduced": replay == sorted(artifact.get("exceptions", [])),
    }


def falsifier_agent(case: Dict[str, Any]) -> Dict[str, Any]:
    counterfactual = json.loads(json.dumps(case))
    for tx in counterfactual["transactions"]:
        tx["delivery_date"] = min(tx["delivery_date"], case["period_end"])
    exceptions = detect_cutoff_exceptions(counterfactual)
    return {
        "agent": "FalsifierAgent",
        "counterfactual_exceptions": exceptions,
        "passed": exceptions == [],
    }


def decision_dag(artifact: Dict[str, Any]) -> Dict[str, Any]:
    nodes = [
        {
            "id": "evidence",
            "status": "complete" if artifact.get("evidence_ids") else "blocked",
        },
        {
            "id": "risk",
            "depends_on": ["evidence"],
            "status": "complete" if artifact.get("risks") else "blocked",
        },
        {
            "id": "procedure",
            "depends_on": ["risk"],
            "status": "complete" if artifact.get("procedures") else "blocked",
        },
        {
            "id": "conclusion",
            "depends_on": ["procedure"],
            "status": "complete",
        },
        {
            "id": "human_gate",
            "depends_on": ["conclusion"],
            "status": "pending",
        },
    ]
    return {"nodes": nodes, "dag_hash": canonical_hash(nodes)}


def base_artifact(case: Dict[str, Any], architecture: str) -> Dict[str, Any]:
    return {
        "case_id": case["case_id"],
        "architecture": architecture,
        "exceptions": [],
        "proposed_adjustment": 0.0,
        "evidence_ids": [],
        "risks": [],
        "assertions": [],
        "procedures": [],
        "limitations": [
            "Synthetic benchmark; not an audit opinion or real-world assurance conclusion."
        ],
        "human_gate": "PENDING_HUMAN_APPROVAL",
        "claim_status": "BENCHMARK_RESULT_ONLY",
        "agent_trace": [],
    }


def run_architecture(case: Dict[str, Any], architecture: str) -> Dict[str, Any]:
    if architecture not in ARCHITECTURES:
        raise ValueError(f"Unknown architecture: {architecture}")

    artifact = base_artifact(case, architecture)
    evidence = evidence_agent(case)
    risk = risk_agent(case)
    accounting = accounting_agent(case)

    common = {
        "exceptions": accounting["exceptions"],
        "proposed_adjustment": accounting["proposed_adjustment"],
        "evidence_ids": evidence["evidence_ids"],
        "risks": risk["risks"],
        "assertions": risk["assertions"],
        "procedures": risk["procedures"],
    }
    artifact.update(common)

    if architecture == "deterministic":
        artifact["agent_trace"] = ["DeterministicRuleEngine"]

    elif architecture == "single_agent":
        artifact["agent_trace"] = ["CombinedAuditAgent"]

    elif architecture == "sequential_agents":
        artifact["agent_trace"] = [
            "EvidenceAgent",
            "AuditRiskAgent",
            "AccountingAgent",
        ]

    else:
        rights = rights_agent(case)
        if not rights["rights_gate_passed"]:
            raise PermissionError("Rights/license gate failed.")
        artifact["agent_trace"] = [
            "RightsLicenseAgent",
            "EvidenceAgent",
            "AuditRiskAgent",
            "AccountingAgent",
        ]
        artifact["critic"] = critic_agent(artifact)
        artifact["replication"] = replicator_agent(case, artifact)
        artifact["falsification"] = falsifier_agent(case)
        artifact["agent_trace"] += [
            "CriticAgent",
            "ReplicatorAgent",
            "FalsifierAgent",
            "HumanGate",
        ]

    artifact["evidence_passport"] = evidence_passport(case)
    artifact["decision_dag"] = decision_dag(artifact)
    artifact["input_hashes"] = frozen_inputs(case)
    artifact["artifact_hash"] = canonical_hash(artifact)
    return artifact


def classification_metrics(predicted: List[str], gold: List[str]) -> Dict[str, float]:
    pred, truth = set(predicted), set(gold)
    tp = len(pred & truth)
    fp = len(pred - truth)
    fn = len(truth - pred)
    precision = tp / (tp + fp) if tp + fp else (1.0 if not truth else 0.0)
    recall = tp / (tp + fn) if tp + fn else 1.0
    return {
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "precision": precision,
        "recall": recall,
    }


def evaluate(case: Dict[str, Any], artifact: Dict[str, Any]) -> Dict[str, Any]:
    core = classification_metrics(artifact["exceptions"], case["gold"]["exceptions"])

    rpa = min(1.0, len(artifact["procedures"]) / max(1, len(artifact["risks"])))
    aa = min(
        1.0,
        len(set(artifact["assertions"]) & set(case["gold"]["expected_assertions"]))
        / max(1, len(case["gold"]["expected_assertions"])),
    )
    eg = min(1.0, len(set(artifact["evidence_ids"])) / max(1, len(case["evidence"])))
    ps = 1.0 if {"CriticAgent", "FalsifierAgent"}.issubset(set(artifact["agent_trace"])) else 0.5
    complete = sum(
        1
        for key in REQUIRED_ARTIFACT_FIELDS
        if key in artifact and artifact[key] not in (None, "", [])
    )
    ds = complete / len(REQUIRED_ARTIFACT_FIELDS)

    replay = run_architecture(case, artifact["architecture"])
    dist = 1.0 if (
        replay["exceptions"] == artifact["exceptions"]
        and replay["proposed_adjustment"] == artifact["proposed_adjustment"]
    ) else 0.0

    return {
        "RPA": round(rpa, 4),
        "AA": round(aa, 4),
        "EG": round(eg, 4),
        "PS": round(ps, 4),
        "DS": round(ds, 4),
        "DIST": round(dist, 4),
        **core,
        "adjustment_matches_gold": (
            artifact["proposed_adjustment"]
            == float(case["gold"]["proposed_adjustment"])
        ),
        "human_gate_enforced": (
            artifact["human_gate"] == case["gold"]["expected_human_gate"]
        ),
        "unsupported_discovery_claim": False,
    }


def run_benchmark(case_path: Path) -> Dict[str, Any]:
    case = load_case(case_path)
    frozen = frozen_inputs(case)
    runs: Dict[str, Any] = {}

    for architecture in ARCHITECTURES:
        start = time.perf_counter()
        artifact = run_architecture(case, architecture)
        metrics = evaluate(case, artifact)
        if artifact["input_hashes"] != frozen:
            raise AssertionError("Frozen input hash changed across architectures.")
        runs[architecture] = {
            "artifact": artifact,
            "metrics": metrics,
            "elapsed_ms": round((time.perf_counter() - start) * 1000, 3),
        }

    return {
        "benchmark": "Prototype 003 Revenue Recognition migration",
        "case_id": case["case_id"],
        "input_hashes": frozen,
        "architectures": list(ARCHITECTURES),
        "runs": runs,
        "research_claim": "NO_SUPERIORITY_CLAIM; engineering benchmark scaffold only",
    }


def main() -> None:
    base = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Run the NAAIL Prototype 003 frozen synthetic benchmark."
    )
    parser.add_argument("--case", default=str(base / "data" / "revenue_case.json"))
    parser.add_argument("--out", default=str(base / "outputs" / "latest_results.json"))
    args = parser.parse_args()

    result = run_benchmark(Path(args.case))
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("Prototype 003 benchmark complete")
    for architecture, row in result["runs"].items():
        metrics = row["metrics"]
        print(
            f"{architecture:22s} "
            f"precision={metrics['precision']:.2f} "
            f"recall={metrics['recall']:.2f} "
            f"EG={metrics['EG']:.2f} "
            f"PS={metrics['PS']:.2f} "
            f"DIST={metrics['DIST']:.2f}"
        )
    print("Human Gate: PENDING_HUMAN_APPROVAL")
    print(f"Saved: {output}")


if __name__ == "__main__":
    main()
