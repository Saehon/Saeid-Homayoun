import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHASE3 = ROOT / "phase3_agents"


def load(name):
    return json.loads((PHASE3 / name).read_text(encoding="utf-8"))


agents = load("agents.json")
tools = load("tool_registry.json")

assert agents["invariant"]["evidence_before_narrative"] is True
assert agents["invariant"]["orchestrator_may_bypass_gate"] is False
assert len(agents["agents"]) == 10

for name, cfg in agents["agents"].items():
    for tool in cfg["tools"]:
        assert tool in tools["tools"], f"{name} references unknown tool {tool}"

cmd = [
    sys.executable,
    str(PHASE3 / "router.py"),
    "--agent", "financial_accounting",
    "--task", "Reconcile a financial-reporting evidence packet",
    "--evidence", "DEMO-EVIDENCE-001",
]
out = subprocess.check_output(cmd, text=True)
plan = json.loads(out)
assert plan["phase"] == 3
assert plan["mode"] == "dry_run"
assert plan["human_gate"] == "material_judgment"
assert any(t["tool_id"] == "finance_skills" for t in plan["approved_tools"])

print("Phase 3 registry and dry-run router validation passed.")
