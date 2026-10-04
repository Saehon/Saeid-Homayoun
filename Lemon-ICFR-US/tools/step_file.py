"""Validate a phase step file.  Usage: python tools/step_file.py governance/poc_steps/P02_x.md"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SECTIONS = ("What was done", "Files changed", "POC demonstration", "Tests", "Problems found",
            "Decisions made without review", "Phase status", "Labels")
FINAL = ("COMPLETE", "PARTIAL", "NOT_RUN_DEPENDENCY", "QUARANTINED")


def validate(text: str) -> tuple[list[str], str | None]:
    errs, status = [], None
    heads = [(m.start(), m.group(1).strip()) for m in re.finditer(r"^## (.+)$", text, re.M)]
    found = {}
    for i, (pos, title) in enumerate(heads):
        end = heads[i + 1][0] if i + 1 < len(heads) else len(text)
        body = text[pos:end].split("\n", 1)[1] if "\n" in text[pos:end] else ""
        for s in SECTIONS:
            if title.startswith(s):
                found[s] = (title, body.strip())
    for s in SECTIONS:
        if s not in found:
            errs.append(f"missing section: {s}")
            continue
        title, body = found[s]
        if s == "Phase status":
            m = re.search(r"(COMPLETE|PARTIAL|NOT_RUN_DEPENDENCY|QUARANTINED)", title + " " + body)
            status = m.group(1) if m else None
            if not status:
                errs.append("Phase status must be one of " + ", ".join(FINAL))
        elif s == "Labels":
            if "UNREVIEWED" not in body + title or "DEVELOPMENT_ONLY" not in body + title:
                errs.append("Labels must include UNREVIEWED and DEVELOPMENT_ONLY")
        elif not body and ":" not in title:
            errs.append(f"empty section: {s}")
    return errs, status


if __name__ == "__main__":
    e, st = validate(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print("OK" if not e else "INVALID", st or "-", *e, sep="\n")
    sys.exit(1 if e else 0)
