"""Hourly cycle mechanics (section 2-3 of POC_PROGRAM.md).

  python tools/poc_cycle.py begin --run-id R123
      → acquires the lock, prints the current phase and run count, or SKIP.
  python tools/poc_cycle.py end --run-id R123 --action "..." [--force-status PARTIAL]
      → validates the phase step file, updates POC_STATE.md, advances when allowed,
        releases the lock, prints the Drive log line.
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone

from _common import MAX_RUNS_PER_PHASE, ROOT
import operator_lock
import poc_state
import step_file

STEPS = ROOT / "governance" / "poc_steps"


def step_path(phase: str):
    hits = sorted(STEPS.glob(f"{phase}_*.md")) if STEPS.exists() else []
    hits = [h for h in hits if "HUMAN_REVIEW_SHEET" not in h.name]
    return hits[0] if hits else None


def begin(run_id: str) -> int:
    s = poc_state.load()
    if not operator_lock.acquire(run_id, s["current_phase"]):
        print("SKIP: lock held")
        return 2
    runs = int(s.get("runs_in_current_phase", "0"))
    print(f"PHASE {s['current_phase']} | run {runs + 1}/{MAX_RUNS_PER_PHASE}")
    if runs + 1 >= MAX_RUNS_PER_PHASE:
        print("TIME BOX: last run for this phase; finish the step file (PARTIAL if needed)")
    return 0


def end(run_id: str, action: str, force_status: str | None) -> int:
    s = poc_state.load()
    phase = s["current_phase"]
    runs = int(s.get("runs_in_current_phase", "0")) + 1
    s["runs_in_current_phase"] = str(runs)
    p = step_path(phase)
    errs, status = (["no step file"], None) if p is None else step_file.validate(p.read_text(encoding="utf-8"))
    if force_status:
        status = force_status
    if status and not errs:
        poc_state.set_status(s, phase, status)
        result, nxt = f"{phase} {status}", poc_state.advance(s)
    elif runs >= MAX_RUNS_PER_PHASE:
        poc_state.set_status(s, phase, "PARTIAL")
        result, nxt = f"{phase} PARTIAL (time box; step file: {'; '.join(errs)})", poc_state.advance(s)
    else:
        poc_state.set_status(s, phase, "IN_PROGRESS")
        result, nxt = f"{phase} IN_PROGRESS ({'; '.join(errs)})", phase
    poc_state.save(s)
    operator_lock.release(run_id)
    print(f"{datetime.now(timezone.utc).isoformat()} | {run_id} | {phase} | {action} | {result} | next={nxt}")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["begin", "end"])
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--action", default="")
    ap.add_argument("--force-status", choices=["PARTIAL", "QUARANTINED", "NOT_RUN_DEPENDENCY"])
    a = ap.parse_args()
    sys.exit(begin(a.run_id) if a.cmd == "begin" else end(a.run_id, a.action, a.force_status))
