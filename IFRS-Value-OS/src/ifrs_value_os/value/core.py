from __future__ import annotations

from dataclasses import dataclass, field


CAPITALS = (
    "financial",
    "manufactured",
    "intellectual",
    "human",
    "social_relationship",
    "natural",
)


@dataclass(slots=True)
class ValueAssessment:
    impacts: dict[str, float | None] = field(
        default_factory=lambda: {capital: None for capital in CAPITALS}
    )
    notes: list[str] = field(default_factory=list)


class ValueCore:
    """Maps a defensible accounting alternative to value consequences."""

    def assess(self) -> ValueAssessment:
        return ValueAssessment(notes=["Value model awaiting case-specific metrics."])
