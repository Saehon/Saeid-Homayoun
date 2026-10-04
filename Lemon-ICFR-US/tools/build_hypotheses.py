"""P06 — build hypothesis files in the adapter schema from verified facts (nothing invented).

Outputs organized/poc/msft/hypotheses_h1.json and hypotheses_control.json.
Competitors without extractable rebuttal evidence stay UNREBUTTED on purpose.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from _common import ROOT, dump_json

POC = ROOT / "organized" / "poc" / "msft"


def build(facts_path: Path = POC / "facts.json", out: Path = POC) -> dict:
    d = json.loads(facts_path.read_text())
    mg = [f for f in d["facts"] if f["predicate"] == "management_icfr_conclusion"]
    if not mg:
        raise SystemExit("NOT_RUN: no management ICFR conclusion fact was extracted (see facts.json not_found)")
    period = max(f["period_end"] for f in mg)
    at = lambda pred, val=None: sorted({f["source_evidence_id"] for f in d["facts"] if f["predicate"] == pred
                                        and f["period_end"] == period and (val is None or f["value"] == val)})
    h1_ids = at("management_icfr_conclusion")
    aud_eff = at("auditor_icfr_opinion", "effective")
    h1 = {"hypothesis_id": "H1", "selected": True, "entity": d["entity"], "period_end": period,
          "claim_text": f"Management concluded ICFR effective as of {period}.",
          "assertion": "entity_level_icfr", "material": True,
          "propositions": [{"predicate": "management_icfr_conclusion", "value": "effective"}],
          "evidence_ids": h1_ids, "assumptions": ["10-K text as filed is the authoritative statement"],
          "limitations": ["entity-level only; controls NOT_PUBLICLY_OBSERVABLE", "regex extraction v1"]}
    comps = [
        {"hypothesis_id": "A1", "selected": False, "claim_text": "Auditor issued an adverse ICFR opinion",
         "rebuttal_evidence_ids": aud_eff},
        {"hypothesis_id": "A2", "selected": False, "claim_text": "A material weakness existed at period end",
         "rebuttal_evidence_ids": sorted(set(aud_eff) & set(at("management_icfr_conclusion", "effective")))},
        {"hypothesis_id": "A3", "selected": False, "claim_text": "Auditor scope limitation",
         "rebuttal_evidence_ids": []},
        {"hypothesis_id": "A4", "selected": False, "claim_text": "Restatement / non-reliance (8-K Item 4.02)",
         "rebuttal_evidence_ids": []},
    ]
    control = {"hypothesis_id": "C1", "selected": True, "entity": d["entity"], "period_end": period,
               "claim_text": "A specific revenue control operated effectively throughout the period.",
               "assertion": "entity_level_icfr", "material": True,
               "propositions": [{"predicate": "control_operating_effective", "value": "effective"}],
               "evidence_ids": h1_ids, "assumptions": [], "limitations": ["control details NOT_PUBLICLY_OBSERVABLE"]}
    dump_json([h1, *comps], out / "hypotheses_h1.json")
    dump_json([control], out / "hypotheses_control.json")
    return {"period_end": period, "h1_evidence": h1_ids,
            "unrebutted": [c["hypothesis_id"] for c in comps if not c["rebuttal_evidence_ids"]]}


if __name__ == "__main__":
    print(json.dumps(build(), indent=2))
