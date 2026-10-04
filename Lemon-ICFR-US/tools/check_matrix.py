"""P15 POC — every top-level path under Lemon-ICFR-US/ must appear in PUBLIC_PRIVATE_MATRIX.md (backticked)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

from _common import ROOT

IGNORE = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".venv"}


def missing(root: Path = ROOT, matrix: Path | None = None) -> list[str]:
    matrix = matrix or root / "governance" / "PUBLIC_PRIVATE_MATRIX.md"
    listed = {m.strip("/") for m in re.findall(r"`([^`]+)`", matrix.read_text())} if matrix.exists() else set()
    tops = sorted(p.name for p in root.iterdir() if p.name not in IGNORE and not p.name.startswith(".~"))
    return [t for t in tops if t not in listed]


if __name__ == "__main__":
    m = missing()
    print("ALL CLASSIFIED" if not m else "UNCLASSIFIED:\n" + "\n".join(m))
    sys.exit(1 if m else 0)
