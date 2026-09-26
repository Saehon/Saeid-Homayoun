"""Minimal oTree-style design skeleton; not executed with participants."""
CONDITIONS = {
    "T0":"Human only",
    "T1":"Human + AI recommendation",
    "T2":"Human + AI recommendation + explanation",
    "T3":"Human + AI + contradictory evidence",
}
OUTCOMES = ["accuracy","confidence","calibration","ai_reliance","ai_override",
            "evidence_requests","professional_skepticism","decision_revision","completion_time"]

def treatment_for(participant_code: str):
    # Development helper only; confirmatory study should use oTree randomization.
    idx=sum(map(ord,participant_code)) % 4
    return list(CONDITIONS)[idx]
