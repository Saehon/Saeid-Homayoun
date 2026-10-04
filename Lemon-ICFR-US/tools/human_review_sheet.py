"""P10 — prepare the owner's review sheet from a passport. AI never creates the disposition."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from _common import ROOT

OUT = ROOT / "governance" / "poc_steps" / "P10_HUMAN_REVIEW_SHEET.md"


def build(passport_path: Path) -> str:
    p = json.loads(passport_path.read_text())
    ev = "\n".join(f"- {e['evidence_id']} · {e['source']} · sha256 {e['sha256'][:16]}…" for e in p["evidence"])
    reasons = "\n".join(f"- {r}" for r in p["review"]["reasons"])
    fz = "\n".join(f"- {c['name']}: {c['outcome']} — {c['detail']}" for c in p["falsification"]["challenges"]
                   if c["outcome"] != "SURVIVED") or "- none"
    return f"""# HUMAN REVIEW SHEET — {p['case_id']}
Passport content hash to sign: `{p['content_hash']}`
Machine status: {p['final_status']} · Support: {p['support']['classification']} · Review: {p['review']['outcome']} (independence {p['review']['independence']}) · Falsification: {p['falsification']['outcome']}

## Claim
{p['hypothesis']['claim']['text']}

## Evidence
{ev}

## Reviewer reasons
{reasons}

## Falsification challenges not survived
{fz}

## Decision (owner only — sign in the human approval UI, never by AI)
APPROVED · APPROVED_WITH_CONDITIONS · REJECTED · RETURN_FOR_MORE_EVIDENCE · ESCALATED
Approving over a non-PASS review or non-SURVIVED falsification requires an override reason.
Record the minutes you spent reviewing: ____ (used in P18 value metrics)
"""


if __name__ == "__main__":
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "organized" / "poc" / "msft" / "passports" / "h1_run1.json"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build(src))
    print(f"wrote {OUT}")
