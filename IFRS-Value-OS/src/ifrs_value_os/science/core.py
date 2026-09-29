from __future__ import annotations

from ifrs_value_os.contracts import DecisionCase, Hypothesis


class ScienceCore:
    """Hypothesis, validation and scientific-testing layer."""

    def generate_hypotheses(self, case: DecisionCase) -> list[Hypothesis]:
        return [
            Hypothesis(
                hypothesis_id=f"{case.case_id}-H1",
                statement=f"Primary treatment candidate for: {case.question}",
                score=0.50,
            ),
            Hypothesis(
                hypothesis_id=f"{case.case_id}-H2",
                statement=f"Alternative treatment candidate for: {case.question}",
                score=0.40,
            ),
        ]
