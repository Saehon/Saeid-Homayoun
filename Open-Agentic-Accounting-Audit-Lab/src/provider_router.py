"""Minimal provider-neutral routing scaffold.

This file intentionally contains no API keys and no audit/accounting logic.
Domain procedures belong in versioned skills/tools; provider routing should not
change the accounting procedure being tested.
"""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class RunMetadata:
    provider: str
    model: str
    treatment: str
    case_id: str
    agent: str


SUPPORTED_FAMILIES = {
    "openai": "GPT",
    "anthropic": "Claude",
    "google": "Gemini",
    "microsoft": "Azure/OpenAI/Foundry",
    "moonshot": "Kimi",
    "deepseek": "DeepSeek",
    "local": "Ollama",
}


def validate_run(meta: RunMetadata) -> None:
    if meta.provider not in SUPPORTED_FAMILIES:
        raise ValueError(f"Unsupported provider alias: {meta.provider}")
    if not meta.model.strip():
        raise ValueError("Exact model/version must be recorded for reproducibility.")
    if meta.treatment not in {"T0", "T1", "T2", "T3", "T4", "T5", "T6"}:
        raise ValueError("Treatment must be T0–T6.")


def run_agent(meta: RunMetadata, task: str, evidence: list[dict[str, Any]]) -> dict[str, Any]:
    """Placeholder interface for a LiteLLM/ADK/Agent Framework implementation.

    Production/research code should:
    1. validate metadata;
    2. route to the frozen provider/model;
    3. expose only approved tools for the named agent;
    4. preserve citations/evidence IDs;
    5. run deterministic validators;
    6. invoke policy and human gates when required.
    """
    validate_run(meta)
    raise NotImplementedError("Connect this scaffold to the selected orchestration/runtime.")
