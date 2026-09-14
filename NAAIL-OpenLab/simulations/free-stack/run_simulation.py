from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def load_case(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("evidence_class") not in {"synthetic", "public", "licensed"}:
        raise ValueError("evidence_class must be synthetic, public, or licensed")
    return data


def classify_ifrs(case: dict[str, Any]) -> list[dict[str, Any]]:
    text = " ".join(str(v) for v in case.values()).lower()
    checks = [
        ("revenue", "Revenue recognition / contract accounting", "IFRS 15 family"),
        ("goodwill", "Goodwill impairment / valuation", "IAS 36 / IFRS 3 family"),
        ("lease", "Lease recognition / measurement", "IFRS 16 family"),
        ("provision", "Provision / contingency", "IAS 37 family"),
        ("fair value", "Fair-value measurement", "IFRS 13 family"),
        ("credit loss", "Expected credit loss", "IFRS 9 family"),
    ]
    findings = []
    for keyword, issue, domain in checks:
        if keyword in text:
            findings.append({"issue": issue, "domain": domain, "basis": f"keyword:{keyword}"})
    if not findings:
        findings.append({"issue": "General financial-reporting judgment", "domain": "Cross-standard review", "basis": "fallback"})
    return findings


def classify_pcaob(case: dict[str, Any]) -> list[dict[str, Any]]:
    text = " ".join(str(v) for v in case.values()).lower()
    checks = [
        ("revenue", "Revenue audit-procedure risk", "audit procedure / evidence"),
        ("inventory", "Inventory observation/testing risk", "audit procedure / evidence"),
        ("control", "ICFR / control-testing risk", "controls / ICFR"),
        ("estimate", "Accounting-estimate audit risk", "estimates / specialist evidence"),
        ("sampling", "Sampling / test-design risk", "audit methodology"),
        ("documentation", "Audit-documentation risk", "documentation / supervision"),
    ]
    findings = []
    for keyword, issue, domain in checks:
        if keyword in text:
            findings.append({"issue": issue, "domain": domain, "basis": f"keyword:{keyword}"})
    if not findings:
        findings.append({"issue": "General inspection-risk review", "domain": "public-evidence inspection simulation", "basis": "fallback"})
    return findings


def simulate(agent: str, case: dict[str, Any]) -> dict[str, Any]:
    canonical = json.dumps(case, sort_keys=True, separators=(",", ":"))
    if agent == "ifrs":
        findings = classify_ifrs(case)
        authority_boundary = "Simulation does not replace authoritative IFRS material or professional judgment."
    elif agent == "pcaob":
        findings = classify_pcaob(case)
        authority_boundary = "Simulation uses only synthetic/public/licensed evidence and does not imply non-public PCAOB access."
    else:
        raise ValueError("agent must be ifrs or pcaob")

    return {
        "naail_platform": "NAAIL OpenLab V2026.3 Multi-Agent Digital Twin",
        "agent": agent,
        "simulation_mode": "deterministic_free_core",
        "input_sha256": sha256_text(canonical),
        "evidence_class": case["evidence_class"],
        "case_id": case.get("case_id"),
        "findings": findings,
        "authority_boundary": authority_boundary,
        "adversarial_questions": [
            "What evidence would falsify each finding?",
            "What alternative explanation is plausible?",
            "Is any model-generated statement being treated as authority?",
            "Are chronology, rights, and provenance complete?",
        ],
        "decision_dag_status": "REVIEW_REQUIRED",
        "human_gate": "PENDING_HUMAN_APPROVAL",
        "discovery_claim_allowed": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run NAAIL free deterministic IFRS/PCAOB simulation")
    parser.add_argument("--agent", choices=["ifrs", "pcaob"], required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = simulate(args.agent, load_case(args.input))
    rendered = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
