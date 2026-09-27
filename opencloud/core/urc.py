"""Public Unified Request Contract for OpenCloud prototype."""
from dataclasses import dataclass
from enum import Enum
from typing import Any

class ProviderStrategy(Enum):
    PRIMARY_ONLY = "primary-only"
    MULTI_PROVIDER_COMPARISON = "multi-provider-comparison"

@dataclass
class Request:
    request_id: str
    project_id: str
    strategy: ProviderStrategy
    primary_provider: str
    challenger_providers: list[str]
    payload: dict[str, Any]
    human_gate_required: bool = True
