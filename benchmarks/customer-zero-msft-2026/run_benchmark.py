"""Free-first Customer-Zero benchmark orchestrator.

Adapters intentionally fail closed until their upstream packages are installed
and pinned. The canonical SEC filing remains the source of truth.
"""
from dataclasses import dataclass, asdict
import json
from pathlib import Path

@dataclass
class Result:
    adapter: str
    status: str
    provenance_coverage: float = 0.0
    unsupported_claims: int = 0
    notes: str = ""

ADAPTERS = [
    "sec-data",
    "edgar-mcp",
    "sec-10-k-structured-extraction",
    "verified-credit-research-agent",
]

def run_adapter(name: str) -> Result:
    # Safe default: registration is not evidence of successful execution.
    return Result(name, "NOT_RUN", notes="Install/pin upstream adapter in isolated environment, then execute.")

def falsification_gate(results):
    failures = [r.adapter for r in results if r.status not in {"PASS"}]
    return {
        "status": "REVIEW" if failures else "PASS",
        "challenges": failures,
        "human_approval": "PENDING",
    }

def main():
    results = [run_adapter(x) for x in ADAPTERS]
    out = {"results":[asdict(r) for r in results], "gate":falsification_gate(results)}
    p=Path(__file__).with_name("results.json")
    p.write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
