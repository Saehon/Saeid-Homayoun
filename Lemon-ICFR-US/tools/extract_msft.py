"""P05 — extract span-verified facts from stored Microsoft 10-K text files → facts.json"""
from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

from _common import ROOT, dump_json
from lemon_icfr.assurance.extract import extract_10k_facts, verify_span_fact

EVID = ROOT / "organized" / "evidence" / "msft"
OUT = ROOT / "organized" / "poc" / "msft" / "facts.json"
ENTITY = "MSFT"


def run(evid: Path = EVID, out: Path = OUT) -> dict:
    manifest = json.loads((evid / "manifest.json").read_text())
    by_id = {e["evidence_id"]: e for e in manifest}
    load = lambda eid: (evid / by_id[eid]["path"]).read_bytes() if eid in by_id else None
    facts, rejected, not_found = [], [], []
    for e in manifest:
        if e["kind"] != "derived_text" or e["form"] != "10-K":
            continue
        b = (evid / e["path"]).read_bytes()
        found = extract_10k_facts(b.decode("utf-8"), b, entity=ENTITY, source_evidence_id=e["evidence_id"],
                                  accession=e["accession"])
        preds = {f.predicate for f in found}
        not_found += [{"evidence_id": e["evidence_id"], "predicate": p}
                      for p in ("management_icfr_conclusion", "auditor_icfr_opinion", "auditor_name") if p not in preds]
        for f in found:
            try:
                verify_span_fact(f, load)
                d = asdict(f)
                d["excerpt"] = f.excerpt(b.decode("utf-8"))
                facts.append(d)
            except Exception as ex:  # recorded, never silently dropped
                rejected.append({"fact": asdict(f), "error": str(ex)})
    res = {"entity": ENTITY, "facts": facts, "rejected": rejected, "not_found": not_found,
           "note": "absence of a phrase is recorded as NOT_FOUND, never as a negative fact"}
    dump_json(res, out)
    return res


if __name__ == "__main__":
    r = run()
    for f in r["facts"]:
        print(f"{f['period_end']} {f['predicate']}={f['value']} [{f['accession']} {f['section']}] {f['excerpt']}")
    print(f"facts={len(r['facts'])} rejected={len(r['rejected'])} not_found={len(r['not_found'])}")
    sys.exit(1 if r["rejected"] else 0)
