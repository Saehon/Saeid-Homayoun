"""P00 — Read/update governance/POC_STATE.md.  Usage: python tools/poc_state.py [current|show]"""
from __future__ import annotations

import sys
from pathlib import Path

from _common import PHASES, ROOT

STATE = ROOT / "governance" / "POC_STATE.md"
STATUSES = ("NOT_STARTED", "IN_PROGRESS", "COMPLETE", "PARTIAL", "NOT_RUN_DEPENDENCY", "QUARANTINED")


def template() -> dict:
    return {"program_version": "v3", "mode": "CONTINUOUS — Claude final review at P19",
            "program_branch": "", "start_point_sha": "", "current_phase": "P00",
            "owner_contact_email_for_sec": "", "owner_approved_cryptography": "no",
            "runs_in_current_phase": "0",
            "quarantined_science": "ORQ-001 SIZE, ORQ-002 RGROWTH (ACK2007 = SCIENTIFIC_HOLD)",
            "open_owner_items": "merge decisions deferred to end (section 8)",
            "phase_status": {p: "NOT_STARTED" for p in PHASES}}


def load(path: Path = STATE) -> dict:
    d, in_ps = {"phase_status": {}}, False
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("phase_status:"):
            in_ps = True
            continue
        if in_ps and raw.startswith("  "):
            k, v = raw.strip().split(":", 1)
            d["phase_status"][k.strip()] = v.strip()
            continue
        in_ps = False
        k, v = raw.split(":", 1)
        d[k.strip()] = v.strip()
    for p in PHASES:
        d["phase_status"].setdefault(p, "NOT_STARTED")
    return d


def save(d: dict, path: Path = STATE) -> None:
    lines = [f"{k}: {v}" for k, v in d.items() if k != "phase_status"]
    lines.append("phase_status:")
    lines += [f"  {p}: {d['phase_status'][p]}" for p in PHASES]
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def set_status(d: dict, phase: str, status: str) -> None:
    if status not in STATUSES:
        raise ValueError(f"invalid status {status}")
    d["phase_status"][phase] = status


def advance(d: dict) -> str:
    i = PHASES.index(d["current_phase"])
    d["current_phase"] = PHASES[min(i + 1, len(PHASES) - 1)]
    d["runs_in_current_phase"] = "0"
    return d["current_phase"]


if __name__ == "__main__":
    if not STATE.exists():
        save(template())
    s = load()
    print(s["current_phase"] if (sys.argv[1:] or ["current"])[0] == "current" else s)
