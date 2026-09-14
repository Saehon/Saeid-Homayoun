from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from typing import Dict, List, Set


ALLOWED_DECISIONS = {
    "ACCEPT_AGENT",
    "MODIFY_AGENT",
    "REJECT_AGENT",
    "REQUEST_MORE_EVIDENCE",
    "ESCALATE_TO_HUMAN",
}


@dataclass(frozen=True)
class Case:
    case_id: str
    title: str
    risk_statement: str
    assertions: List[str]
    evidence_ids: List[str]
    contradictory_evidence_ids: List[str]
    expected_procedure_terms: List[str]
    hidden_exception_ids: List[str]
    synthetic_amount_eur: int


@dataclass
class StudentDecision:
    decision: str
    assertions: List[str]
    selected_evidence_ids: List[str]
    contradictory_evidence_ids: List[str]
    procedure_text: str
    rationale: str
    independently_verified_ai: bool
    requested_human_review: bool


CASES: Dict[str, Case] = {
    "revenue": Case(
        case_id="REV-001",
        title="Revenue Recognition & Cut-off",
        risk_statement="Revenue may have been recognized before the earnings process was complete or before control transferred.",
        assertions=["occurrence", "cut-off"],
        evidence_ids=["TX-001", "TX-002", "TX-003", "CONTRACT-17", "INVOICE-884", "SHIP-552"],
        contradictory_evidence_ids=["SHIP-552", "TX-002", "TX-003"],
        expected_procedure_terms=["contract", "invoice", "shipping", "cut-off", "trace"],
        hidden_exception_ids=["TX-002", "TX-003"],
        synthetic_amount_eur=190000,
    ),
    "goodwill": Case(
        case_id="GW-001",
        title="Goodwill Impairment",
        risk_statement="Management assumptions may overstate recoverable amount and delay recognition of impairment.",
        assertions=["valuation", "accuracy"],
        evidence_ids=["GW-DR", "GW-MAR", "FORECAST-01", "WACC-01", "SENS-01", "BOARD-02"],
        contradictory_evidence_ids=["GW-DR", "GW-MAR", "SENS-01"],
        expected_procedure_terms=["sensitivity", "forecast", "discount", "assumption", "specialist"],
        hidden_exception_ids=["GW-DR", "GW-MAR"],
        synthetic_amount_eur=440000,
    ),
    "icfr": Case(
        case_id="ICFR-001",
        title="ICFR / Control Deficiency",
        risk_statement="Journal-entry and IT controls may not prevent or detect material misstatement on a timely basis.",
        assertions=["completeness", "accuracy", "authorization"],
        evidence_ids=["CTRL-JE-01", "CTRL-JE-02", "CTRL-IT-01", "CTRL-IT-03", "LOG-11", "REVIEW-07"],
        contradictory_evidence_ids=["CTRL-JE-02", "CTRL-IT-03", "LOG-11"],
        expected_procedure_terms=["design", "operating", "journal", "access", "compensating"],
        hidden_exception_ids=["CTRL-JE-02", "CTRL-IT-03"],
        synthetic_amount_eur=530000,
    ),
}


class EducationalProxyAgent:
    """Deterministic teaching proxy. Not a production audit agent."""

    def advise(self, case: Case) -> dict:
        suggested_evidence = case.evidence_ids[:3]
        suggested_procedure = {
            "revenue": "Inspect contracts and invoices and perform year-end cut-off testing.",
            "goodwill": "Review forecasts and key assumptions and perform sensitivity analysis.",
            "icfr": "Evaluate control design and operating effectiveness and inspect compensating controls.",
        }[self._key(case.case_id)]

        return {
            "case_id": case.case_id,
            "risk_statement": case.risk_statement,
            "assertions": case.assertions,
            "recommended_procedure": suggested_procedure,
            "evidence_ids": suggested_evidence,
            "contradictory_evidence_ids": [],
            "uncertainties": ["Educational proxy may omit relevant contradictory evidence."],
            "alternative_explanations": ["Additional evidence may change the conclusion."],
            "required_human_review": True,
            "status": "EDUCATIONAL_SIMULATION_ONLY",
        }

    @staticmethod
    def _key(case_id: str) -> str:
        if case_id.startswith("REV"):
            return "revenue"
        if case_id.startswith("GW"):
            return "goodwill"
        return "icfr"


def _overlap_score(actual: Set[str], expected: Set[str]) -> int:
    if not expected:
        return 100
    return round(100 * len(actual & expected) / len(expected))


def _procedure_score(text: str, expected_terms: List[str]) -> int:
    lowered = text.lower()
    hits = sum(term.lower() in lowered for term in expected_terms)
    return round(100 * hits / len(expected_terms)) if expected_terms else 100


def _documentation_score(rationale: str) -> int:
    words = [w for w in rationale.strip().split() if w]
    if len(words) >= 45:
        return 100
    if len(words) >= 30:
        return 85
    if len(words) >= 20:
        return 70
    if len(words) >= 10:
        return 50
    return 25 if words else 0


def score_decision(case: Case, decision: StudentDecision) -> dict:
    if decision.decision not in ALLOWED_DECISIONS:
        raise ValueError(f"Unsupported decision state: {decision.decision}")

    assertion_score = _overlap_score(set(a.lower() for a in decision.assertions), set(case.assertions))
    evidence_score = _overlap_score(set(decision.selected_evidence_ids), set(case.hidden_exception_ids))
    contradiction_score = _overlap_score(
        set(decision.contradictory_evidence_ids), set(case.contradictory_evidence_ids)
    )
    procedure_score = _procedure_score(decision.procedure_text, case.expected_procedure_terms)
    documentation_score = _documentation_score(decision.rationale)

    skepticism_components = [contradiction_score]
    skepticism_components.append(100 if decision.decision != "ACCEPT_AGENT" else 40)
    skepticism_components.append(100 if decision.independently_verified_ai else 0)
    skepticism_score = round(sum(skepticism_components) / len(skepticism_components))

    hor = 100 if decision.decision in {"MODIFY_AGENT", "REJECT_AGENT", "REQUEST_MORE_EVIDENCE", "ESCALATE_TO_HUMAN"} else 50
    esc = 100 if decision.requested_human_review or decision.decision == "ESCALATE_TO_HUMAN" else 40
    aiv = 100 if decision.independently_verified_ai else 0

    dist = round((assertion_score + evidence_score + procedure_score + documentation_score) / 4)

    metrics = {
        "RPA": procedure_score,
        "AA": assertion_score,
        "EG": evidence_score,
        "PS": skepticism_score,
        "DS": documentation_score,
        "DIST": dist,
        "AIV": aiv,
        "CER": contradiction_score,
        "HOR": hor,
        "ESC": esc,
    }

    professional_core = round(sum(metrics[k] for k in ["RPA", "AA", "EG", "PS", "DS", "DIST"]) / 6)
    ai_readiness_core = round(sum(metrics[k] for k in ["AIV", "CER", "HOR", "ESC"]) / 4)

    return {
        "case_id": case.case_id,
        "case_title": case.title,
        "decision": decision.decision,
        "metrics": metrics,
        "professional_judgment_core": professional_core,
        "ai_readiness_core": ai_readiness_core,
        "human_gate": "PENDING_HUMAN_APPROVAL",
        "score_status": "ILLUSTRATIVE_NOT_VALIDATED_FOR_EMPLOYMENT_DECISIONS",
    }


def demo_decision(case_key: str) -> StudentDecision:
    case = CASES[case_key]
    procedure_text = {
        "revenue": "Trace shipping evidence to invoices and contracts, inspect year-end cut-off, and investigate exceptions.",
        "goodwill": "Challenge forecasts, discount assumptions and sensitivity analysis, and consider specialist review.",
        "icfr": "Test control design and operating effectiveness, inspect journal access and compensating controls.",
    }[case_key]

    return StudentDecision(
        decision="MODIFY_AGENT",
        assertions=list(case.assertions),
        selected_evidence_ids=list(case.hidden_exception_ids),
        contradictory_evidence_ids=list(case.contradictory_evidence_ids),
        procedure_text=procedure_text,
        rationale=(
            "I independently checked the evidence instead of relying on the proxy recommendation. "
            "The listed exception evidence is inconsistent with an unqualified acceptance of the agent output. "
            "I would modify the proposed procedure, retain the contradictory evidence in the file, document the alternative explanation, "
            "and escalate the final simulated conclusion for human review before closing the case."
        ),
        independently_verified_ai=True,
        requested_human_review=True,
    )


def run_demo() -> None:
    agent = EducationalProxyAgent()
    outputs = []
    for key, case in CASES.items():
        outputs.append(
            {
                "case": asdict(case),
                "proxy_agent": agent.advise(case),
                "student_decision": asdict(demo_decision(key)),
                "evaluation": score_decision(case, demo_decision(key)),
            }
        )
    print(json.dumps(outputs, indent=2))


def _csv_list(prompt: str) -> List[str]:
    raw = input(prompt).strip()
    return [item.strip() for item in raw.split(",") if item.strip()]


def run_interactive(case_key: str) -> None:
    case = CASES[case_key]
    agent = EducationalProxyAgent()
    print("\n=== NAAIL Student Digital Twin — Educational Simulation Only ===")
    print(json.dumps(agent.advise(case), indent=2))
    print("\nAvailable evidence IDs:", ", ".join(case.evidence_ids))

    decision_state = input("Decision state: ").strip().upper()
    assertions = _csv_list("Assertions (comma separated): ")
    evidence = _csv_list("Evidence IDs selected (comma separated): ")
    contradictions = _csv_list("Contradictory evidence IDs (comma separated): ")
    procedure = input("Proposed audit procedure: ").strip()
    rationale = input("Rationale: ").strip()
    verify = input("Did you independently verify the AI recommendation? [y/N]: ").strip().lower() == "y"
    human = input("Request human review? [y/N]: ").strip().lower() == "y"

    student = StudentDecision(
        decision=decision_state,
        assertions=assertions,
        selected_evidence_ids=evidence,
        contradictory_evidence_ids=contradictions,
        procedure_text=procedure,
        rationale=rationale,
        independently_verified_ai=verify,
        requested_human_review=human,
    )

    print("\n=== Illustrative Evaluation ===")
    print(json.dumps(score_decision(case, student), indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="NAAIL synthetic Student Digital Twin pilot")
    parser.add_argument("--demo", action="store_true", help="run all three cases with transparent demo decisions")
    parser.add_argument("--case", choices=sorted(CASES), help="run one interactive case")
    args = parser.parse_args()

    if args.demo:
        run_demo()
        return
    if args.case:
        run_interactive(args.case)
        return
    parser.print_help()


if __name__ == "__main__":
    main()
