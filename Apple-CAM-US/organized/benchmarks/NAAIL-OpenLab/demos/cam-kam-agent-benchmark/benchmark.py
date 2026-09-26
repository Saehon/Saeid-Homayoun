from __future__ import annotations

import argparse
import csv
import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Dict, Iterable, List, Set

TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_-]+")

RISK_PROCEDURE_MAP = {
    "revenue": {"test", "sample", "contract", "cutoff", "invoice", "confirmation", "recalculate"},
    "impairment": {"forecast", "valuation", "discount", "sensitivity", "assumption", "recalculate"},
    "goodwill": {"valuation", "discount", "forecast", "sensitivity", "specialist", "assumption"},
    "inventory": {"count", "observe", "valuation", "sample", "obsolescence", "recalculate"},
    "tax": {"recalculate", "specialist", "assumption", "forecast", "documentation"},
    "credit": {"model", "recalculate", "sample", "assumption", "forecast", "sensitivity"},
}

ASSERTION_TERMS = {
    "existence", "occurrence", "completeness", "valuation", "accuracy", "cutoff",
    "rights", "obligations", "presentation", "classification", "allocation"
}

EVIDENCE_TERMS = {
    "invoice", "contract", "confirmation", "minutes", "ledger", "reconciliation",
    "model", "forecast", "report", "sample", "document", "documentation", "specialist",
    "data", "schedule", "calculation", "calculated"
}

PROFESSIONAL_TERMS = {
    "management", "estimate", "assumption", "material", "judgment", "sensitivity",
    "discount", "margin", "growth", "control", "specialist", "valuation", "threshold"
}

BOILERPLATE_TERMS = {
    "we", "our", "audit", "procedures", "included", "assessed", "evaluated", "considered",
    "performed", "obtained", "management", "financial", "statements"
}


def tokenize(text: str) -> List[str]:
    return [m.group(0).lower() for m in TOKEN_RE.finditer(text or "")]


def pct(x: float) -> float:
    return round(max(0.0, min(100.0, x)), 2)


def jaccard(a: Set[str], b: Set[str]) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def risk_procedure_alignment(risk: str, procedures: str) -> float:
    r = set(tokenize(risk))
    p = set(tokenize(procedures))
    active = [k for k in RISK_PROCEDURE_MAP if k in r]
    if not active:
        return pct(35 + 65 * jaccard(r - BOILERPLATE_TERMS, p - BOILERPLATE_TERMS))
    expected = set().union(*(RISK_PROCEDURE_MAP[k] for k in active))
    coverage = len(expected & p) / max(1, min(len(expected), 5))
    lexical = jaccard(r - BOILERPLATE_TERMS, p - BOILERPLATE_TERMS)
    return pct(75 * min(1.0, coverage) + 25 * lexical)


def assertion_alignment(assertion_text: str, procedures: str) -> float:
    a = set(tokenize(assertion_text)) & ASSERTION_TERMS
    p = set(tokenize(procedures))
    if not a:
        return 25.0
    direct = len(a & p) / len(a)
    assertion_density = len(a) / min(4, len(ASSERTION_TERMS))
    return pct(80 * direct + 20 * min(1.0, assertion_density))


def evidence_grounding(evidence: str, procedures: str) -> float:
    e = set(tokenize(evidence))
    p = set(tokenize(procedures))
    evidence_hits = len(e & EVIDENCE_TERMS)
    procedure_hits = len(p & EVIDENCE_TERMS)
    specificity = min(1.0, len(e) / 35.0)
    return pct(45 * min(1.0, evidence_hits / 4) + 35 * min(1.0, procedure_hits / 4) + 20 * specificity)


def professional_specificity(*parts: str) -> float:
    tokens = tokenize(" ".join(parts))
    t = set(tokens)
    term_hits = len(t & PROFESSIONAL_TERMS)
    numeric_hits = len(re.findall(r"\b\d+(?:\.\d+)?%?\b", " ".join(parts)))
    length_component = min(1.0, len(tokens) / 100.0)
    return pct(55 * min(1.0, term_hits / 5) + 25 * min(1.0, numeric_hits / 2) + 20 * length_component)


def disclosure_specificity(risk: str, procedures: str, evidence: str) -> float:
    tokens = tokenize(" ".join([risk, procedures, evidence]))
    if not tokens:
        return 0.0
    counts = Counter(tokens)
    content = [t for t in tokens if t not in BOILERPLATE_TERMS]
    unique_ratio = len(set(content)) / max(1, len(content))
    boilerplate_ratio = sum(counts[t] for t in BOILERPLATE_TERMS) / len(tokens)
    length_component = min(1.0, len(tokens) / 120.0)
    return pct(50 * unique_ratio + 30 * (1 - boilerplate_ratio) + 20 * length_component)


def distinctiveness(index: int, combined_texts: List[str]) -> float:
    current = set(tokenize(combined_texts[index])) - BOILERPLATE_TERMS
    if len(combined_texts) <= 1:
        return 100.0
    similarities = []
    for j, text in enumerate(combined_texts):
        if j == index:
            continue
        other = set(tokenize(text)) - BOILERPLATE_TERMS
        similarities.append(jaccard(current, other))
    return pct(100 * (1 - max(similarities, default=0.0)))


def score_rows(rows: List[Dict[str, str]]) -> List[Dict[str, object]]:
    combined = [" ".join([r.get("risk_text", ""), r.get("procedure_text", ""), r.get("evidence_text", "")]) for r in rows]
    results = []
    weights = {"RPA": 0.25, "AA": 0.15, "EG": 0.20, "PS": 0.15, "DS": 0.15, "DIST": 0.10}

    for i, r in enumerate(rows):
        scores = {
            "RPA": risk_procedure_alignment(r.get("risk_text", ""), r.get("procedure_text", "")),
            "AA": assertion_alignment(r.get("assertion_text", ""), r.get("procedure_text", "")),
            "EG": evidence_grounding(r.get("evidence_text", ""), r.get("procedure_text", "")),
            "PS": professional_specificity(r.get("risk_text", ""), r.get("procedure_text", ""), r.get("evidence_text", "")),
            "DS": disclosure_specificity(r.get("risk_text", ""), r.get("procedure_text", ""), r.get("evidence_text", "")),
            "DIST": distinctiveness(i, combined),
        }
        composite = pct(sum(scores[k] * weights[k] for k in weights))
        results.append({"id": r.get("id", str(i + 1)), "scores": scores, "prototype_composite": composite})
    return results


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    required = {"id", "risk_text", "procedure_text", "evidence_text", "assertion_text"}
    if not rows:
        raise ValueError("Input CSV is empty")
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="NAAIL CAM/KAM prototype benchmark")
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--output", type=Path, default=Path("results.json"))
    args = parser.parse_args()

    rows = read_csv(args.csv_path)
    results = score_rows(rows)

    print("ID\tRPA\tAA\tEG\tPS\tDS\tDIST\tCOMPOSITE")
    for row in results:
        s = row["scores"]
        print(f"{row['id']}\t{s['RPA']:.1f}\t{s['AA']:.1f}\t{s['EG']:.1f}\t{s['PS']:.1f}\t{s['DS']:.1f}\t{s['DIST']:.1f}\t{row['prototype_composite']:.1f}")

    artifact = {
        "benchmark": "NAAIL CAM/KAM Agentic Audit Intelligence prototype",
        "status": "research-demo-not-validated-measure",
        "weights": {"RPA": 0.25, "AA": 0.15, "EG": 0.20, "PS": 0.15, "DS": 0.15, "DIST": 0.10},
        "results": results,
    }
    args.output.write_text(json.dumps(artifact, indent=2), encoding="utf-8")
    print(f"\nWrote {args.output}")


if __name__ == "__main__":
    main()
