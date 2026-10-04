from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import json
from typing import Dict, Any, List

@dataclass
class AgentMessage:
    agent: str
    status: str
    summary: str
    evidence: List[str]
    next_actions: List[str]

def weighted_score(items: Dict[str, Dict[str, Any]]) -> float:
    total_weight = sum(float(v["weight"]) for v in items.values())
    if total_weight <= 0:
        raise ValueError("Weights must sum to a positive value.")
    return sum(float(v["score"]) * float(v["weight"]) for v in items.values()) / total_weight

class ApplicabilityAgent:
    name = "Applicability Agent"
    def run(self, case: Dict[str, Any]) -> AgentMessage:
        c = case["company"]
        notes = [
            f"Reporting basis: {c['reporting_basis']}",
            f"Audit regime: {c['audit_regime']}",
            "KAM is comparator-only for this Microsoft POC.",
            "IFRS is shadow/cross-framework mode, not Microsoft's primary reporting basis."
        ]
        return AgentMessage(self.name, "PASS_WITH_BOUNDARIES",
            "Determined which professional regimes are applicable before scoring.",
            notes, ["Keep jurisdiction and period gates machine-enforced."])

class InherentRiskAgent:
    name = "Inherent Risk Agent"
    def run(self, case: Dict[str, Any]) -> AgentMessage:
        score = weighted_score(case["illustrative_uncalibrated_inputs"]["IR"])
        facts = case["verified_poc_facts"]
        evidence = [
            f"{len(facts['cams'])} CAMs mapped; both high-judgment areas.",
            f"Revenue growth: {facts['revenue_growth']:.1%}.",
            f"R&D intensity: {facts['rd_intensity']:.1%}.",
            f"FY2026 simple price return: {facts['fy2026_simple_price_return']:.1%} (context, not audit evidence)."
        ]
        return AgentMessage(self.name, "ILLUSTRATIVE_UNCALIBRATED",
            f"IR index = {score:.4f}. This is a normalized research-demo index, not a calibrated probability.",
            evidence, ["Add company-specific AAER matching.", "Add dedicated cyber and ESG evidence before expanding IR inputs."])

class ControlRiskAgent:
    name = "Control Risk Agent"
    def run(self, case: Dict[str, Any]) -> AgentMessage:
        score = weighted_score(case["illustrative_uncalibrated_inputs"]["CR"])
        facts = case["verified_poc_facts"]
        return AgentMessage(self.name, "ILLUSTRATIVE_UNCALIBRATED",
            f"CR index = {score:.4f}. Unqualified ICFR lowers the current signal but does not imply zero control risk.",
            [f"ICFR opinion: {facts['icfr_opinion']}.",
             "Control-level operating-effectiveness evidence is incomplete in the current POC.",
             "Dedicated ITGC/cyber-control package is not yet executed."],
            ["Extend LEMON to control-by-control design and operating-effectiveness testing.",
             "Add ITGC and cyber-control evidence."])

class DetectionRiskAgent:
    name = "Detection Risk Agent"
    def run(self, case: Dict[str, Any], ir: float, cr: float) -> AgentMessage:
        score = weighted_score(case["illustrative_uncalibrated_inputs"]["DR"])
        target = float(case["audit_risk_model"]["target_ar_index"])
        allowable = min(1.0, target / (ir * cr)) if ir > 0 and cr > 0 else 1.0
        status = "ABOVE_ALLOWABLE_INDEX" if score > allowable else "WITHIN_TARGET_INDEX"
        return AgentMessage(self.name, status,
            f"DR index = {score:.4f}; allowable DR index at target AR={target:.4f} is {allowable:.4f}.",
            ["Evidence Passport exists.", "CAM procedures are mapped.", "Independent replication remains pending."],
            ["Increase procedure coverage and independent review until DR is at or below the chosen target index."])

class EvidenceAgent:
    name = "Evidence Agent"
    def run(self, case: Dict[str, Any]) -> AgentMessage:
        f = case["verified_poc_facts"]
        return AgentMessage(self.name, "PASS_WITH_GAPS",
            "Verified current POC evidence and identified non-executed specialist modules.",
            [f"Evidence Passport: {f['evidence_passport']}",
             f"Artifact validation: {f['artifact_validation']}",
             "AAER match, dedicated cyber, ESG analytics, and engagement-level PCAOB mapping remain incomplete."],
            ["Preserve source, timestamp, rights, transformation lineage and status for every new signal."])

class ChallengerAgent:
    name = "Independent Challenger"
    def run(self, case: Dict[str, Any], ar: float, dr: float, allowable: float) -> AgentMessage:
        findings = [
            "Do not describe the normalized AR index as a literal probability of audit failure.",
            "Do not convert missing AAER/cyber/ESG evidence into low risk.",
            "Do not treat firm-level PCAOB inspection findings as Microsoft engagement findings."
        ]
        if dr > allowable:
            findings.append("Current illustrative DR index exceeds the allowable index implied by the selected target.")
        return AgentMessage(self.name, "CHALLENGE_RAISED",
            f"Challenged aggregation and claim boundaries for AR index {ar:.4f}.",
            findings, ["Require explicit Human Gate disposition for every unresolved challenge."])

class HumanGateAgent:
    name = "Human Gate"
    def run(self, case: Dict[str, Any], dr: float, allowable: float) -> AgentMessage:
        prod = case["verified_poc_facts"]["production_approval"]
        if prod == "NO" or dr > allowable:
            status = "RESEARCH_ONLY_ESCALATE"
            summary = "Research prototype may be demonstrated with limitations; production/professional use is not approved."
        else:
            status = "REVIEW_REQUIRED"
            summary = "Human professional review remains mandatory."
        return AgentMessage(self.name, status, summary,
            [f"Production approval in source POC: {prod}.",
             f"Scientific validation: {case['verified_poc_facts']['scientific_validation']}."],
            ["Obtain independent replication and calibrated validation before any production risk rating."])

class RiskOSOrchestrator:
    name = "RiskOS Orchestrator"
    def __init__(self, case: Dict[str, Any]):
        self.case = case

    def run(self) -> Dict[str, Any]:
        ir = weighted_score(self.case["illustrative_uncalibrated_inputs"]["IR"])
        cr = weighted_score(self.case["illustrative_uncalibrated_inputs"]["CR"])
        dr = weighted_score(self.case["illustrative_uncalibrated_inputs"]["DR"])
        ar = ir * cr * dr
        target = float(self.case["audit_risk_model"]["target_ar_index"])
        allowable = min(1.0, target / (ir * cr)) if ir > 0 and cr > 0 else 1.0
        agents = [
            ApplicabilityAgent().run(self.case),
            InherentRiskAgent().run(self.case),
            ControlRiskAgent().run(self.case),
            DetectionRiskAgent().run(self.case, ir, cr),
            EvidenceAgent().run(self.case),
            ChallengerAgent().run(self.case, ar, dr, allowable),
            HumanGateAgent().run(self.case, dr, allowable)
        ]
        return {
            "project": self.case["project"],
            "company": self.case["company"],
            "audit_risk_decomposition": {
                "IR_index": round(ir, 4), "CR_index": round(cr, 4), "DR_index": round(dr, 4),
                "AR_index": round(ar, 4), "target_AR_index": target, "allowed_DR_index": round(allowable, 4),
                "formula": "AR_index = IR_index * CR_index * DR_index",
                "boundary": "Normalized, illustrative, uncalibrated research-demo indices only."
            },
            "agents": [asdict(a) for a in agents],
            "final_state": "HUMAN_REVIEW_REQUIRED"
        }

def load_case(path: str | Path = "microsoft_case.json") -> Dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))

if __name__ == "__main__":
    case = load_case(Path(__file__).with_name("microsoft_case.json"))
    result = RiskOSOrchestrator(case).run()
    print(json.dumps(result, indent=2, ensure_ascii=False))
