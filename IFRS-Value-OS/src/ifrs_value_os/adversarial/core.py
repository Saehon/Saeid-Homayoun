from __future__ import annotations

from ifrs_value_os.contracts import Hypothesis


class AdversarialCore:
    """Challenge, falsification, counterfactual and GAN/synthetic-case boundary."""

    def challenge(self, hypothesis: Hypothesis) -> Hypothesis:
        hypothesis.challenges.append(
            "Identify contradictory evidence, boundary conditions, and assumptions that would falsify this treatment."
        )
        hypothesis.score = max(0.0, hypothesis.score - 0.05)
        return hypothesis

    def generate_synthetic_case(self, seed_label: str) -> dict[str, str]:
        return {"seed": seed_label, "status": "synthetic_case_stub"}
