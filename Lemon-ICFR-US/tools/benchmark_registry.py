"""P11 — classify benchmark-like artifacts and report duplicates. Classification only; never deletes."""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from _common import ROOT, dump_json, sha256_bytes

EXTS = {".csv", ".json", ".jsonl", ".parquet", ".tsv", ".xlsx"}
GENERATED = {"organized/benchmarks/REGISTRY.json", "organized/benchmarks/DUPLICATES.json"}
ALLOWED = {"CANONICAL", "DERIVED_COPY", "ARCHIVAL_COPY", "EXTERNAL_EXPORT", "DEPRECATED",
           "NON_EXECUTABLE_REFERENCE"}


def classify(rel: str) -> str:
    low = rel.lower()
    if any(token in low for token in ("mock", "fake", "dummy", "stub")):
        return "NON_EXECUTABLE_REFERENCE"
    if low.startswith("copies-from-original/"):
        return "ARCHIVAL_COPY"
    if any(token in low for token in ("/huggingface/", "/kaggle/", "/open-data/")):
        return "EXTERNAL_EXPORT"
    if "naail-openlab/" in low and "fy2026-release/ai_cost_benchmark.csv" not in low:
        return "DERIVED_COPY"
    if low.startswith("organized/benchmarks/"):
        return "CANONICAL"
    raise ValueError(f"benchmark-like artifact has no classification rule: {rel}")


def benchmark_like(rel: str) -> bool:
    low = rel.lower()
    return (low.startswith("organized/benchmarks/") or low.startswith("copies-from-original/")
            or "benchmark" in Path(low).name or "mock" in Path(low).name)


def benchmark_name(rel: str) -> str:
    """Stable logical names; classification is copy status, never evidence admissibility."""
    name = Path(rel).stem.lower()
    if name == "case_002_microsoft_sec_2026":
        return "frankenstein-phase4-case-002"
    if name == "mock_case_002_microsoft_response":
        return "frankenstein-phase4-mock-response"
    if name == "ai_cost_benchmark":
        return "naail-ai-cost-benchmark"
    return name


def scan(root: Path = ROOT) -> dict:
    entries, by_hash = [], defaultdict(list)
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in EXTS or ".git" in p.parts:
            continue
        rel = p.relative_to(root).as_posix()
        if rel in GENERATED or not benchmark_like(rel):
            continue
        h = sha256_bytes(p.read_bytes())
        cls = classify(rel)
        entries.append({"benchmark_name": benchmark_name(rel), "path": rel, "sha256": h, "class": cls,
                        "scientific_status": "DEVELOPMENT_ONLY"})
        by_hash[h].append(rel)
    dups = {h: ps for h, ps in by_hash.items() if len(ps) > 1}
    executable_names = {e["benchmark_name"] for e in entries if e["class"] != "NON_EXECUTABLE_REFERENCE"
                        and any(x["benchmark_name"] == e["benchmark_name"] and x["class"] == "CANONICAL"
                                for x in entries)}
    canonical_counts = {name: sum(e["benchmark_name"] == name and e["class"] == "CANONICAL"
                                  for e in entries) for name in sorted(executable_names)}
    return {"note": "CANONICAL means authoritative benchmark representation, not admissible source evidence. "
                    "Mocks are never evidence. Sprint 1 metrics and all registry content remain DEVELOPMENT_ONLY.",
            "allowed_classes": sorted(ALLOWED), "canonical_counts": canonical_counts,
            "entries": entries, "duplicates": dups}


def validate(registry: dict) -> None:
    bad = [e for e in registry["entries"] if e["class"] not in ALLOWED]
    if bad:
        raise ValueError(f"invalid classifications: {bad[:3]}")
    wrong = {name: count for name, count in registry["canonical_counts"].items() if count != 1}
    if wrong:
        raise ValueError(f"benchmark names require exactly one CANONICAL representation: {wrong}")
    for e in registry["entries"]:
        if any(token in e["path"].lower() for token in ("mock", "fake")) \
                and e["class"] != "NON_EXECUTABLE_REFERENCE":
            raise ValueError(f"mock/fake artifact is executable: {e['path']}")


if __name__ == "__main__":
    r = scan()
    validate(r)
    dump_json(r, ROOT / "organized" / "benchmarks" / "REGISTRY.json")
    dump_json({"duplicate_groups": r["duplicates"]}, ROOT / "organized" / "benchmarks" / "DUPLICATES.json")
    print(f"entries={len(r['entries'])} duplicate_groups={len(r['duplicates'])}")
    print("canonical_counts", r["canonical_counts"])
    for h, ps in list(r["duplicates"].items())[:20]:
        print(h[:12], *ps, sep="\n  ")
