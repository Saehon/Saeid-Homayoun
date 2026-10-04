"""Shared helpers for LEMON POC tools. Run tools from Lemon-ICFR-US/ with PYTHONPATH=src."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

PHASES = [f"P{i:02d}" for i in range(20)]   # P00 .. P19
MAX_RUNS_PER_PHASE = 4


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_file(p: Path) -> str:
    return sha256_bytes(Path(p).read_bytes())


def dump_json(obj, path: Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, sort_keys=True, indent=2) + "\n", encoding="utf-8")
