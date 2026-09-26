from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class SyntheticScenario:
    scenario_id: str
    scenario_type: str
    description: str
    generator: str
    generator_version: str
    seed: int | None
    evidence_class: str = "synthetic"


class SyntheticScenarioProvider(Protocol):
    """Replaceable interface for GAN/diffusion/rule-based scenario generators."""

    name: str

    def generate(self, *, scenario_type: str, count: int, seed: int | None = None) -> list[SyntheticScenario]:
        ...


class DeterministicScenarioProvider:
    """Dependency-free baseline used to benchmark future GAN/synthetic providers."""

    name = "deterministic-baseline"

    def generate(self, *, scenario_type: str, count: int, seed: int | None = None) -> list[SyntheticScenario]:
        return [
            SyntheticScenario(
                scenario_id=f"{scenario_type}-{i+1:04d}",
                scenario_type=scenario_type,
                description=f"Synthetic ICFR stress scenario {i+1} for {scenario_type}.",
                generator=self.name,
                generator_version="1",
                seed=seed,
            )
            for i in range(count)
        ]
