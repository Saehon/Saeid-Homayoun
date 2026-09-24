"""FRANKENSTEIN Phase 3 specialist-agent router.

This is deliberately a dry-run orchestration/control layer. It does not copy
third-party code and does not call paid model APIs. It validates which external
tools an agent is allowed to use, records the evidence requirement, and emits
the human-gate rule for reproducible research runs.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AGENTS_PATH = ROOT / "agents.json"
TOOLS_PATH = ROOT / "tool_registry.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_registry(agents_doc: dict, tools_doc: dict) -> list[str]:
    errors: list[str] = []
    registered = set(tools_doc["tools"])

    for agent_name, cfg in agents_doc["agents"].items():
        for tool in cfg.get("tools", []):
            if tool not in registered:
                errors.append(f"{agent_name}: unregistered tool '{tool}'")
        if agent_name != "evidence" and "human_gate" not in cfg:
            errors.append(f"{agent_name}: missing human_gate")
        if cfg.get("authoritative_source_required") and "authoritative_sources" not in cfg.get("tools", []):
            errors.append(f"{agent_name}: authoritative source required but no authoritative_sources tool")

    inv = agents_doc.get("invariant", {})
    if inv.get("orchestrator_may_bypass_gate") is not False:
        errors.append("orchestrator_may_bypass_gate must remain false")
    if inv.get("evidence_before_narrative") is not True:
        errors.append("evidence_before_narrative must remain true")
    return errors


def build_plan(agent_name: str, task: str, evidence_ids: list[str]) -> dict:
    agents_doc = load_json(AGENTS_PATH)
    tools_doc = load_json(TOOLS_PATH)
    errors = validate_registry(agents_doc, tools_doc)
    if errors:
        raise SystemExit("Registry validation failed:\n- " + "\n- ".join(errors))

    if agent_name not in agents_doc["agents"]:
        valid = ", ".join(sorted(agents_doc["agents"]))
        raise SystemExit(f"Unknown agent '{agent_name}'. Valid agents: {valid}")

    cfg = agents_doc["agents"][agent_name]
    if cfg.get("evidence_required") and not evidence_ids:
        raise SystemExit(f"Agent '{agent_name}' requires at least one evidence ID.")

    tool_plan = []
    for tool_id in cfg["tools"]:
        tool = tools_doc["tools"][tool_id]
        tool_plan.append(
            {
                "tool_id": tool_id,
                "name": tool["name"],
                "source": tool["source"],
                "license": tool["license"],
                "status": tool["status"],
                "integration": tool["integration"],
            }
        )

    return {
        "mode": "dry_run",
        "phase": 3,
        "agent": agent_name,
        "mission": cfg["mission"],
        "task": task,
        "evidence_ids": evidence_ids,
        "evidence_required": cfg.get("evidence_required", False),
        "approved_tools": tool_plan,
        "human_gate": cfg.get("human_gate"),
        "authoritative_source_required": cfg.get("authoritative_source_required", False),
        "professional_boundary": (
            "No material accounting/audit/IFRS/assurance conclusion is final "
            "until the configured human gate is satisfied."
        ),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--agent", required=True)
    p.add_argument("--task", required=True)
    p.add_argument("--evidence", action="append", default=[])
    args = p.parse_args()
    print(json.dumps(build_plan(args.agent, args.task, args.evidence), indent=2))


if __name__ == "__main__":
    main()
