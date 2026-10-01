#!/usr/bin/env python3
"""NAAIL Research Assurance MCP POC core.

Pure-stdlib implementation for bounded POC use. It does not execute licensed
study data or infer methodological validity. All assurance states are scoped
to supplied evidence.
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

STATES = {"VERIFIED","CONSISTENT","PARTIAL","FLAGGED","HUMAN_REVIEW"}

def load_json(path: str | Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def inspect_package(root: str | Path) -> Dict[str, Any]:
    root = Path(root)
    files = [p for p in root.rglob("*") if p.is_file()]
    return {
        "root": str(root),
        "file_count": len(files),
        "extensions": sorted({p.suffix.lower() or "<none>" for p in files}),
        "files": [str(p.relative_to(root)) for p in files],
    }

def validate_evidence_graph(graph: Dict[str, Any]) -> Dict[str, Any]:
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    ids = [n.get("id") for n in nodes]
    idset = set(ids)
    unresolved = [e for e in edges if e.get("from") not in idset or e.get("to") not in idset]
    bad_states = [n.get("id") for n in nodes if n.get("assurance_state") and n.get("assurance_state") not in STATES]
    return {
        "node_count": len(nodes), "edge_count": len(edges),
        "all_node_ids_unique": len(ids) == len(idset),
        "unresolved_edges": unresolved, "invalid_state_nodes": bad_states,
        "pass": len(ids) == len(idset) and not unresolved and not bad_states,
    }

def map_table_to_code(graph: Dict[str, Any], table_id: str) -> Dict[str, Any]:
    edges = graph.get("edges", [])
    by_id = {n["id"]: n for n in graph.get("nodes", [])}
    frontier, seen, paths = [(table_id, [table_id])], set(), []
    while frontier:
        cur, path = frontier.pop(0)
        if cur in seen: continue
        seen.add(cur)
        node = by_id.get(cur, {})
        if node.get("type") == "code":
            paths.append({"code": node, "path": path})
            continue
        for e in edges:
            if e.get("from") == cur:
                frontier.append((e.get("to"), path + [e.get("to")]))
    return {"table_id": table_id, "code_paths": paths}

def trace_provenance(graph: Dict[str, Any], start_id: str) -> Dict[str, Any]:
    edges = graph.get("edges", [])
    by_id = {n["id"]: n for n in graph.get("nodes", [])}
    q, seen, trace = [start_id], set(), []
    while q:
        cur = q.pop(0)
        if cur in seen: continue
        seen.add(cur)
        if cur in by_id: trace.append(by_id[cur])
        for e in edges:
            if e.get("from") == cur: q.append(e.get("to"))
    return {"start_id": start_id, "nodes": trace}

def compare_reported_result(reported: float, regenerated: float, tolerance: float = 1e-9) -> Dict[str, Any]:
    delta = regenerated - reported
    ok = abs(delta) <= tolerance
    return {"reported": reported, "regenerated": regenerated, "delta": delta,
            "tolerance": tolerance, "match": ok,
            "assurance_state": "CONSISTENT" if ok else "FLAGGED"}

def score_detection(expected_ids: List[str], detected_ids: List[str]) -> Dict[str, Any]:
    exp, det = set(expected_ids), set(detected_ids)
    tp, fp, fn = len(exp & det), len(det-exp), len(exp-det)
    precision = tp/(tp+fp) if tp+fp else (1.0 if not exp else 0.0)
    recall = tp/(tp+fn) if tp+fn else 1.0
    f1 = 2*precision*recall/(precision+recall) if precision+recall else 0.0
    return {"tp":tp,"fp":fp,"fn":fn,"precision":precision,"recall":recall,"f1":f1}

def generate_assurance_report(graph: Dict[str, Any]) -> Dict[str, Any]:
    counts = {s:0 for s in STATES}
    findings = []
    for n in graph.get("nodes", []):
        s = n.get("assurance_state")
        if s in STATES:
            counts[s] += 1
            findings.append({"id":n.get("id"),"type":n.get("type"),"state":s,"label":n.get("label")})
    overall = "FLAGGED" if counts["FLAGGED"] else ("PARTIAL" if counts["PARTIAL"] else ("HUMAN_REVIEW" if counts["HUMAN_REVIEW"] else "CONSISTENT"))
    return {"graph_id":graph.get("graph_id"),"overall_state":overall,
            "state_counts":counts,"findings":findings,
            "governance":["Missing evidence is never VERIFIED.","CONSISTENT is not independent reproduction.","Methodological validity requires HUMAN_REVIEW when unresolved."]}

def run_case001(graph_path: str | Path) -> Dict[str, Any]:
    graph = load_json(graph_path)
    return {
        "graph_validation": validate_evidence_graph(graph),
        "table_to_code": map_table_to_code(graph, "TABLE_REG"),
        "author_provenance": trace_provenance(graph, "CLAIM_AOC"),
        "microsoft_provenance": trace_provenance(graph, "CLAIM_MSFT"),
        "assurance_report": generate_assurance_report(graph),
    }

if __name__ == "__main__":
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("graph")
    p.add_argument("--out")
    a=p.parse_args()
    result=run_case001(a.graph)
    text=json.dumps(result,indent=2)
    if a.out: Path(a.out).write_text(text+"\n",encoding="utf-8")
    else: print(text)
