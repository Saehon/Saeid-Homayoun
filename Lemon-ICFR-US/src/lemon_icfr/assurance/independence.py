"""Reviewer independence (P0-3)."""
from __future__ import annotations

from dataclasses import dataclass

from .enums import Independence
from .errors import SelfReviewError

ROLES = frozenset({"generator", "reviewer", "falsifier"})


@dataclass(frozen=True)
class AgentRun:
    run_id: str
    role: str
    provider: str
    model: str
    model_version: str
    prompt_version: str
    code_version: str
    data_version: str
    timestamp: str
    context_id: str

    def __post_init__(self):
        if self.role not in ROLES:
            raise ValueError(f"unknown agent role {self.role!r}")


def assess_independence(generator: AgentRun, checker: AgentRun) -> Independence:
    if checker.run_id == generator.run_id or checker.context_id == generator.context_id:
        raise SelfReviewError("checker shares run/context with generator: a hypothesis cannot review itself")
    if checker.role == "generator":
        raise SelfReviewError("a generator run cannot act as reviewer/falsifier")
    if checker.provider != generator.provider:
        return Independence.HIGH
    if checker.model != generator.model:
        return Independence.MEDIUM
    return Independence.LOW   # same provider + model: development fallback only
