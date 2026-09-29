"""Provider-neutral local-first model router."""
from dataclasses import dataclass
from enum import Enum

class Risk(str, Enum):
    ROUTINE = "routine"
    COMPLEX = "complex"
    HIGH = "high"

@dataclass
class Route:
    provider: str
    model_family: str
    human_approval: bool = False

def choose_route(risk: Risk, failed_validation: bool = False) -> Route:
    if risk == Risk.ROUTINE and not failed_validation:
        return Route("ollama", "ibm-granite")
    if risk == Risk.COMPLEX and not failed_validation:
        return Route("gemini", "frontier")
    return Route("multi-provider", "claude|openai|gemini", human_approval=True)
