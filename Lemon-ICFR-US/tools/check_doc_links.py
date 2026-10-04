"""P16 POC — every repo path referenced in README.md / ARCHITECTURE.md must exist."""
from __future__ import annotations

import re
import sys
from pathlib import Path

from _common import ROOT

PATHLIKE = re.compile(r"^[\w.\-]+(/[\w.\-]*)+/?$|^[\w.\-]+\.(md|py|json|toml|yml|yaml)$")


def broken(root: Path = ROOT, docs=("README.md", "ARCHITECTURE.md")) -> list[str]:
    out = []
    for d in docs:
        p = root / d
        if not p.exists():
            out.append(f"{d}: file missing")
            continue
        text = p.read_text(encoding="utf-8")
        refs = set(re.findall(r"`([^`\s]+)`", text)) | set(re.findall(r"\]\(([^)\s#]+)\)", text))
        for r in sorted(refs):
            if r.startswith(("http", "mailto")) or "*" in r or "<" in r or not PATHLIKE.match(r):
                continue
            target = r[len("Lemon-ICFR-US/"):] if r.startswith("Lemon-ICFR-US/") else r
            if not (root / target).exists() and not (root.parent / target).exists():
                out.append(f"{d}: {r}")
    return out


if __name__ == "__main__":
    b = broken()
    print("NO BROKEN REFERENCES" if not b else "BROKEN:\n" + "\n".join(b))
    sys.exit(1 if b else 0)
