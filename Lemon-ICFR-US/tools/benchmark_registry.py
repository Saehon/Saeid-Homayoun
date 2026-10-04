"""P11 — classify benchmark-like artifacts and report duplicates. Classification only; never deletes."""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

from _common import ROOT, dump_json, sha256_bytes

EXTS = {".csv", ".json", ".jsonl", ".parquet", ".tsv", ".xlsx"}
RULES = [("mock", "NON_EXECUTABLE_REFERENCE"), ("fake", "NON_EXECUTABLE_REFERENCE"),
         ("organized/benchmarks/", "CANONICAL_CANDIDATE"), ("copies-from-original/", "ARCHIVAL_COPY"),
         ("FRANKENSTEIN/", "DERIVED_COPY"), ("NAAIL-OpenLab/", "DERIVED_COPY"), ("huggingface/", "EXTERNAL_EXPORT"),
         ("kaggle/", "EXTERNAL_EXPORT"), ("open-data/", "EXTERNAL_EXPORT")]


def classify(rel: str) -> str:
    low = rel.lower()
    for pat, cls in RULES:
        if pat.lower() in low:
            return cls
    return "UNCLASSIFIED"


def scan(root: Path = ROOT) -> dict:
    entries, by_hash = [], defaultdict(list)
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in EXTS or ".git" in p.parts or "evidence/msft" in p.as_posix():
            continue
        rel = p.relative_to(root).as_posix()
        h = sha256_bytes(p.read_bytes())
        entries.append({"path": rel, "sha256": h, "class": classify(rel)})
        by_hash[h].append(rel)
    dups = {h: ps for h, ps in by_hash.items() if len(ps) > 1}
    return {"note": "CANONICAL_CANDIDATE requires owner confirmation; mock = never evidence; Sprint 1 metrics = "
                    "DEVELOPMENT_ONLY", "entries": entries, "duplicates": dups}


if __name__ == "__main__":
    r = scan()
    dump_json(r, ROOT / "organized" / "benchmarks" / "REGISTRY.json")
    print(f"entries={len(r['entries'])} duplicate_groups={len(r['duplicates'])}")
    for h, ps in list(r["duplicates"].items())[:20]:
        print(h[:12], *ps, sep="\n  ")
