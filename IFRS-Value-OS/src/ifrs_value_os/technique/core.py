from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class TechniqueResult:
    name: str
    value: float | str | None
    trace: str


class TechniqueCore:
    """Deterministic accounting, valuation and analytical tools."""

    def run(self, name: str, **inputs: float) -> TechniqueResult:
        if name == "sum":
            value = sum(inputs.values())
            return TechniqueResult(name=name, value=value, trace=f"sum({sorted(inputs)})")
        return TechniqueResult(name=name, value=None, trace="technique_not_implemented")
