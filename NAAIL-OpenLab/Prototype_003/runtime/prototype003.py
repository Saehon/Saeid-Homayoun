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

PROVIDER_ARCHITECTURES = ARCHITECTURES[1:]
PROVIDER_REQUIRED_STATUS = "NOT_EXECUTED_PROVIDER_REQUIRED"


def canonical_hash(obj: Any) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_case(path: Path) -> Dict[str, Any]:
    case = load_json(path)
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
    items = [
        {
            "evidence_id": evidence["evidence_id"],
            "source_type": evidence["source_type"],
            "rights": evidence["rights"],
            "content_hash": canonical_hash(evidence),
        }
        for evidence in case["evidence"]
    ]
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


def decision_dag(artifact: Dict[str, Any]) -> Dict[str, Any]:
    nodes = [
        {"id": "evidence", "status": "complete"},
        {"id": "risk", "depends_on": ["evidence"], "status": "complete"},
        {"id": "procedure", "depends_on": ["risk"], "status": "complete"},
        {"id": "conclusion", "depends_on": ["procedure"], "status": "complete"},
        {"id": "human_gate", "depends_on": ["conclusion"], "status": "pending"},
    ]
    return {"nodes": nodes, "dag_hash": canonical_hash(nodes)}


def run_deterministic(case: Dict[str, Any]) -> Dict[str, Any]:
    exceptions = detect_cutoff_exceptions(case)
    evidence_ids = sorted(e["evidence_id"] for e in case["evidence"])

    artifact: Dict[str, Any] = {
        "case_id": case["case_id"],
        "architecture": "deterministic",
        "execution_status": "EXECUTED",
        "exceptions": exceptions,
        "proposed_adjustment": proposed_adjustment(case, exceptions),
        "evidence_ids": evidence_ids,
        "risks": ["revenue_cutoff", "premature_revenue_recognition"],
        "assertions": ["occurrence", "cutoff"],
        "procedures": [
            "inspect_delivery_evidence",
            "reconcile_year_end_transactions",
        ],
        "limitations": [
            "Synthetic benchmark only; not an audit opinion or real-world assurance conclusion."
        ],
        "human_gate": "PENDING_HUMAN_APPROVAL",
        "claim_status": "BENCHMARK_RESULT_ONLY",
        "evidence_passport": evidence_passport(case),
        "input_hashes": frozen_inputs(case),
    }
    artifact["decision_dag"] = decision_dag(artifact)
    artifact["artifact_hash"] = canonical_hash(artifact)
    return artifact


def registered_provider_run(case: Dict[str, Any], architecture: str) -> Dict[str, Any]:
    if architecture not in PROVIDER_ARCHITECTURES:
        raise ValueError(f"Provider architecture expected, got: {architecture}")
    return {
        "case_id": case["case_id"],
        "architecture": architecture,
        "execution_status": PROVIDER_REQUIRED_STATUS,
        "provider": None,
        "model": None,
        "exceptions": None,
        "proposed_adjustment": None,
        "metrics": None,
        "human_gate": "PENDING_HUMAN_APPROVAL",
        "claim_status": "NO_EMPIRICAL_RESULT",
        "input_hashes": frozen_inputs(case),
        "scientific_integrity_note": (
            "No simulated or placeholder AI output is substituted for a real provider/model run."
        ),
    }


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


def evaluate_deterministic(case: Dict[str, Any], artifact: Dict[str, Any]) -> Dict[str, Any]:
    core = classification_metrics(artifact["exceptions"], case["gold"]["exceptions"])
    replay = run_deterministic(case)

    rpa = min(1.0, len(artifact["procedures"]) / max(1, len(artifact["risks"])))
    aa = min(
        1.0,
        len(set(artifact["assertions"]) & set(case["gold"]["expected_assertions"]))
        / max(1, len(case["gold"]["expected_assertions"])),
    )
    eg = min(1.0, len(set(artifact["evidence_ids"])) / max(1, len(case["evidence"])))
    dist = 1.0 if (
        replay["exceptions"] == artifact["exceptions"]
        and replay["proposed_adjustment"] == artifact["proposed_adjustment"]
    ) else 0.0

    return {
        "RPA": round(rpa, 4),
        "AA": round(aa, 4),
        "EG": round(eg, 4),
        "PS": 0.5,
        "DS": 1.0,
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


def run_public_benchmark(case_path: Path, registry_path: Path) -> Dict[str, Any]:
    case = load_case(case_path)
    registry = load_json(registry_path)
    frozen = frozen_inputs(case)

    start = time.perf_counter()
    deterministic = run_deterministic(case)
    deterministic_metrics = evaluate_deterministic(case, deterministic)
    deterministic_elapsed = round((time.perf_counter() - start) * 1000, 3)

    runs: Dict[str, Any] = {
        "deterministic": {
            "artifact": deterministic,
            "metrics": deterministic_metrics,
            "elapsed_ms": deterministic_elapsed,
        }
    }

    for architecture in PROVIDER_ARCHITECTURES:
        runs[architecture] = registered_provider_run(case, architecture)
        if runs[architecture]["input_hashes"] != frozen:
            raise AssertionError("Frozen input hash changed across registered architectures.")

    return {
        "benchmark": "Prototype 003 public runtime checkpoint",
        "public_release": registry["public_release"],
        "case_id": case["case_id"],
        "case_registry": registry["cases"],
        "input_hashes": frozen,
        "architectures": list(ARCHITECTURES),
        "runs": runs,
        "research_claim": "NO_SUPERIORITY_CLAIM; provider AI modes not yet executed",
        "next_milestone": "Prototype 004 real-provider blinded comparison",
    }


def main() -> None:
    base = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Run the public NAAIL Prototype 003 deterministic checkpoint."
    )
    parser.add_argument("--case", default=str(base / "data" / "revenue_case.json"))
    parser.add_argument("--registry", default=str(base / "data" / "case_registry.json"))
    parser.add_argument("--out", default=str(base / "outputs" / "latest_results.json"))
    args = parser.parse_args()

    result = run_public_benchmark(Path(args.case), Path(args.registry))
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")

    det = result["runs"]["deterministic"]
    metrics = det["metrics"]
    print("Prototype 003 public checkpoint complete")
    print(
        "deterministic          "
        f"precision={metrics['precision']:.2f} "
        f"recall={metrics['recall']:.2f} "
        f"EG={metrics['EG']:.2f} "
        f"DIST={metrics['DIST']:.2f}"
    )
    for architecture in PROVIDER_ARCHITECTURES:
        print(f"{architecture:22s} {result['runs'][architecture]['execution_status']}")
    print("Human Gate: PENDING_HUMAN_APPROVAL")
    print(f"Saved: {output}")


if __name__ == "__main__":
    main()
