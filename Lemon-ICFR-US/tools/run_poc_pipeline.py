"""P07 — run the entity-level pipeline twice and save passports.

Config: organized/poc/msft/config.json (template written on first run). Fixed created_at
makes the run deterministic. Reviewer/falsifier/extractor are the same rule-based codebase,
so independence is honestly recorded as LOW (development fallback).
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

from _common import ROOT, dump_json
from lemon_icfr.assurance.entity_scope import EntityScope, assure_entity_case, entity_level_support
from lemon_icfr.assurance.enums import Rights, SourceTier
from lemon_icfr.assurance.evidence import EvidenceStore, Fact, make_evidence
from lemon_icfr.assurance.falsify import Falsifier
from lemon_icfr.assurance.independence import AgentRun
from lemon_icfr.assurance.passport import _jsonable
from lemon_icfr.assurance.review import ReproRef, Reviewer

POC = ROOT / "organized" / "poc" / "msft"
EVID = ROOT / "organized" / "evidence" / "msft"
CONFIG_TEMPLATE = {
    "case_id": "MSFT-ICFR-POC-1", "question": "Did management conclude that ICFR was effective at period end?",
    "created_at": "SET-FIXED-ISO-UTC-TIMESTAMP", "authority_refs": ["SEC Rule 13a-15(c)", "SOX Section 404(a)/(b)",
                                                                   "PCAOB AS 2201"],
    "repro": {"code_version": "", "repo_commit": "", "data_version": "", "config_hash": "", "environment": ""}}


def _git_commit() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:
        return ""   # missing → ReproRef incomplete → reviewer FAIL (honest)


def _run(i, role, ctx):
    return AgentRun(f"{ctx}:{role}", role, "lemon-deterministic", "rules-v1", "v1", "p-none", "c", "d",
                    "fixed", f"{ctx}:{role}:ctx")


def build_store(facts_doc: dict) -> EvidenceStore:
    manifest = json.loads((EVID / "manifest.json").read_text())
    store = EvidenceStore()
    for e in manifest:
        if e["kind"] != "derived_text":
            continue
        facts = [Fact(f["entity"], f["period_end"], f["predicate"], f["value"])
                 for f in facts_doc["facts"] if f["source_evidence_id"] == e["evidence_id"]]
        store.add(make_evidence(e["evidence_id"], content=(EVID / e["path"]).read_bytes(), facts=facts,
                                source=e["url"], source_type=e["form"], tier=SourceTier.SEC_FILING,
                                provenance=f"SEC EDGAR {e['url']} accession {e['accession']}",
                                rights=Rights.PUBLIC_DOMAIN, version=e["accession"], retrieved_at=e["retrieved_at"]))
    return store


def run_case(cfg: dict, hyps: list, store: EvidenceStore, case_suffix: str):
    sel = [h for h in hyps if h.get("selected")][0]
    scope = EntityScope(sel["entity"], sel["period_end"], tuple(cfg["authority_refs"]))
    r = cfg["repro"]
    repro = ReproRef(r["code_version"] or _git_commit(), r["repo_commit"] or _git_commit(), r["data_version"],
                     r["config_hash"], r["environment"], "lemon-deterministic", "rules-v1", "p-none")
    ctx = cfg["case_id"] + case_suffix
    gen = _run(0, "generator", ctx)

    def replay():
        from lemon_icfr.assurance.adapter import legacy_to_hypothesis
        h = legacy_to_hypothesis(sel, [x for x in hyps if x is not sel], gen)
        b = json.dumps(_jsonable(entity_level_support(h.claim, store)), sort_keys=True).encode()
        return hashlib.sha256(b).hexdigest()

    return assure_entity_case(case_id=ctx, question=cfg["question"], created_at=cfg["created_at"], hypotheses=hyps,
                              store=store, scope=scope, repro=repro, generator=gen,
                              reviewer=Reviewer(_run(0, "reviewer", ctx)),
                              falsifier=Falsifier(_run(0, "falsifier", ctx), store), replay=replay)


def main() -> int:
    cfg_p = POC / "config.json"
    if not cfg_p.exists():
        dump_json(CONFIG_TEMPLATE, cfg_p)
        print(f"NOT_RUN: wrote {cfg_p}; owner/operator must set created_at and repro fields")
        return 1
    cfg = json.loads(cfg_p.read_text())
    facts = json.loads((POC / "facts.json").read_text())
    t0 = time.perf_counter()
    store = build_store(facts)
    out = {}
    for name in ("h1", "control"):
        hyps = json.loads((POC / f"hypotheses_{name}.json").read_text())
        hashes = []
        for run_no in (1, 2):
            d = run_case(cfg, hyps, store, f"-{name}")
            if d.passport is None:
                out[name] = {"status": "FAIL_CLOSED", "reasons": list(d.reasons)}
                break
            (POC / "passports").mkdir(parents=True, exist_ok=True)
            (POC / "passports" / f"{name}_run{run_no}.json").write_text(d.passport.to_json())
            hashes.append(d.passport.content_hash())
            out[name] = {"support": d.passport.support.classification.value,
                         "review": d.passport.review.outcome.value,
                         "independence": d.passport.review.independence.value,
                         "falsification": d.passport.falsification.outcome.value,
                         "final_status": d.passport.final_status(store).value,
                         "gates": {"support_ok": d.support_ok, "reviewer_ok": d.reviewer_ok,
                                   "falsification_ok": d.falsification_ok}, "reasons": list(d.reasons)}
        out[name]["content_hashes"] = hashes
        out[name]["deterministic"] = len(hashes) == 2 and hashes[0] == hashes[1]
    out["runtime_seconds"] = round(time.perf_counter() - t0, 3)
    out["llm_calls"] = 0
    out["evidence_items"] = len(store.all())
    out["facts"] = len(facts["facts"])
    dump_json(out, POC / "pipeline_summary.json")
    print(json.dumps({k: (v if not isinstance(v, dict) else {kk: v[kk] for kk in v if kk != "reasons"})
                      for k, v in out.items()}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
