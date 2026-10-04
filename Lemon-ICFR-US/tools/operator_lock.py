"""Single-operator lock (governance/OPERATOR_LOCK.md). A lock older than 90 minutes is stale."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

from _common import ROOT

LOCK = ROOT / "governance" / "OPERATOR_LOCK.md"
STALE = timedelta(minutes=90)


def acquire(run_id: str, phase: str, now: datetime | None = None, path: Path = LOCK) -> bool:
    now = now or datetime.now(timezone.utc)
    if path.exists():
        fields = dict(l.split(": ", 1) for l in path.read_text().splitlines() if ": " in l)
        if fields.get("state") == "HELD":
            held_at = datetime.fromisoformat(fields["utc"])
            if now - held_at < STALE and fields.get("run_id") != run_id:
                return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"state: HELD\nrun_id: {run_id}\nutc: {now.isoformat()}\nphase: {phase}\n")
    return True


def release(run_id: str, path: Path = LOCK) -> None:
    if path.exists() and f"run_id: {run_id}" in path.read_text():
        path.write_text(f"state: FREE\nrun_id: {run_id}\nutc: {datetime.now(timezone.utc).isoformat()}\n")
