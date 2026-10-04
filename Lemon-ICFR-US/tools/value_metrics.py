"""P18 — realized-value metrics, each with its source. Measured values only; missing = NOT_MEASURED."""
from __future__ import annotations

import json
import re
from pathlib import Path

from _common import ROOT, dump_json

POC = ROOT / "organized" / "poc" / "msft"


def _rel(p: Path) -> str:
    try:
        return p.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return p.as_posix()


def collect(poc: Path = POC, sheet: Path = ROOT / "governance" / "poc_steps" / "P10_HUMAN_REVIEW_SHEET.md") -> dict:
    m = {}
    s = poc / "pipeline_summary.json"
    if s.exists():
        d = json.loads(s.read_text())
        for k in ("runtime_seconds", "llm_calls", "evidence_items", "facts"):
            m[k] = {"value": d.get(k, "NOT_MEASURED"), "source": _rel(s)}
        m["api_cost_usd"] = {"value": 0 if d.get("llm_calls") == 0 else "NOT_MEASURED",
                             "source": f"{_rel(s)} (llm_calls)"}
    mf = ROOT / "organized" / "evidence" / "msft" / "manifest.json"
    if mf.exists():
        m["sec_documents"] = {"value": len(json.loads(mf.read_text())), "source": _rel(mf)}
    mins = "NOT_MEASURED"
    if sheet.exists():
        hit = re.search(r"reviewing:\s*(\d+)", sheet.read_text())
        mins = int(hit.group(1)) if hit else "NOT_MEASURED"
    m["human_review_minutes"] = {"value": mins, "source": _rel(sheet)}
    return m


if __name__ == "__main__":
    r = collect()
    dump_json(r, POC / "value_metrics.json")
    for k, v in r.items():
        print(f"{k}: {v['value']}  (source: {v['source']})")
