from __future__ import annotations

from dataclasses import dataclass

from ifrs_value_os.contracts import RiskLevel


@dataclass(frozen=True, slots=True)
class RoutePlan:
    primary_provider: str
    reviewer_provider: str | None
    falsifier_provider: str | None
    human_gate: bool


class AgenticRouter:
    """Risk-aware, model-agnostic routing policy."""

    def route(self, risk: RiskLevel) -> RoutePlan:
        if risk is RiskLevel.LOW:
            return RoutePlan("economy", None, None, False)
        if risk is RiskLevel.MEDIUM:
            return RoutePlan("primary", None, None, True)
        if risk is RiskLevel.HIGH:
            return RoutePlan("primary", "reviewer", None, True)
        return RoutePlan("primary", "reviewer", "falsifier", True)
