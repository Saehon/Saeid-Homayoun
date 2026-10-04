"""P19 — assemble the final Claude review package, split into ≤ 60 KB parts."""
from __future__ import annotations

import re
from pathlib import Path

from _common import ROOT

STEPS = ROOT / "governance" / "poc_steps"
LIMIT = 60_000


def sources() -> list[Path]:
    fixed = [ROOT / "governance" / "POC_STATE.md", ROOT / "governance" / "OPEN_REPAIR_QUEUE.md",
             ROOT / "organized" / "poc" / "msft" / "pipeline_summary.json",
             ROOT / "organized" / "poc" / "msft" / "passports" / "h1_run1.json",
             ROOT / "organized" / "poc" / "msft" / "value_metrics.json",
             ROOT / "organized" / "evidence" / "msft" / "manifest.json"]
    steps = sorted(p for p in STEPS.glob("P*.md") if not p.name.startswith("P19")) if STEPS.exists() else []
    return steps + [p for p in fixed if p.exists()]


def decisions(steps: list[Path]) -> str:
    out = []
    for p in steps:
        m = re.search(r"^## Decisions made without review\s*\n(.*?)(?=^## |\Z)", p.read_text(), re.M | re.S)
        if m and m.group(1).strip():
            out.append(f"### {p.stem}\n{m.group(1).strip()}")
    return "\n\n".join(out) or "none recorded"


def build() -> list[Path]:
    srcs = sources()
    head = ("# P19 — CLAUDE FINAL REVIEW PACKAGE\nAll content UNREVIEWED / DEVELOPMENT_ONLY.\n\n"
            "## All decisions made without review\n" + decisions([p for p in srcs if p.parent == STEPS]) + "\n")
    blocks = [head] + [f"\n\n---\n## FILE: {p.relative_to(ROOT).as_posix()}\n````\n{p.read_text()}\n````\n" for p in srcs]
    parts, cur = [], ""
    for b in blocks:
        if cur and len((cur + b).encode()) > LIMIT:
            parts.append(cur)
            cur = ""
        cur += b
    parts.append(cur)
    STEPS.mkdir(parents=True, exist_ok=True)
    paths = []
    for i, txt in enumerate(parts, 1):
        name = "P19_CLAUDE_FINAL_REVIEW.md" if len(parts) == 1 else f"P19_part{i}_of_{len(parts)}.md"
        (STEPS / name).write_text(txt)
        paths.append(STEPS / name)
    return paths


if __name__ == "__main__":
    for p in build():
        print(p.relative_to(ROOT), p.stat().st_size, "bytes")
