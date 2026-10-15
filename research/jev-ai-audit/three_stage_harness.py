"""Three-stage, dependency-free CAM -> ICFR -> PCAOB research harness.

Synthetic data only. Does not install/run Jev or draw assurance conclusions.
Run: python research/jev-ai-audit/three_stage_harness.py
"""
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Case:
    case_id: str
    industry: str
    domain: str
    cam_present: Optional[bool]
    icfr_status: str
    risk_probability: Optional[float]
    evidence_verified: bool

def validate(case):
    if case.icfr_status not in {"effective", "ineffective", "unknown"}:
        raise ValueError("Invalid ICFR taxonomy")
    if case.risk_probability is not None and not 0 <= case.risk_probability <= 1:
        raise ValueError("Invalid probability")
    if not case.industry or not case.domain or not case.case_id:
        raise ValueError("Missing provenance fields")

def cam_stage(case):
    validate(case)
    return {
        "case_id": case.case_id, "stage": "CAM",
        "cam_present": case.cam_present, "domain": case.domain,
        "risk_probability": case.risk_probability,
        "cam_effectiveness": "unverified",
        "decision": "needs_review" if not case.evidence_verified else "risk_screen_only",
    }

def icfr_stage(case, cam):
    validate(case)
    assert cam["case_id"] == case.case_id
    return {
        "case_id": case.case_id, "stage": "ICFR",
        "icfr_status": case.icfr_status,
        "risk_probability": case.risk_probability,
        "decision": "abstain" if case.icfr_status == "unknown" or not case.evidence_verified else "review_label",
    }

def pcaob_stage(case, cam, icfr):
    assert cam["case_id"] == icfr["case_id"] == case.case_id
    # This is a human-controlled inspection TRIAGE, not a PCAOB inspection finding.
    needs_human = (not case.evidence_verified or
                   case.icfr_status == "unknown" or
                   case.risk_probability is None or
                   case.risk_probability >= 0.7)
    return {
        "case_id": case.case_id, "stage": "PCAOB",
        "inspection_finding": None,
        "decision": "escalate_to_human" if needs_human else "routine_human_review",
        "human_approval_required": True,
    }

def run(case):
    cam = cam_stage(case)
    icfr = icfr_stage(case, cam)
    pcaob = pcaob_stage(case, cam, icfr)
    return [cam, icfr, pcaob]

def smoke_test():
    # Synthetic example, not an observation about AAR or any actual SEC filer.
    sample = Case("SYNTHETIC-001", "Manufacturing", "revenue",
                  True, "unknown", 0.78, False)
    stages = run(sample)
    assert [s["stage"] for s in stages] == ["CAM", "ICFR", "PCAOB"]
    assert stages[0]["cam_effectiveness"] == "unverified"
    assert stages[1]["decision"] == "abstain"
    assert stages[2]["human_approval_required"] is True
    assert stages[2]["inspection_finding"] is None
    return stages

if __name__ == "__main__":
    import json
    print(json.dumps(smoke_test(), indent=2))
