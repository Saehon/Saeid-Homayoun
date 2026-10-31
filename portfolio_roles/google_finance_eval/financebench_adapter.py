"""Offline, license-aware FinanceBench candidate-output evaluation.

Does not download benchmark assets or call any model.
Exact-string matching is intentionally conservative, not semantic grading.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

def read_jsonl(path):
    rows = []
    with Path(path).open(encoding="utf-8") as stream:
        for line_num, line in enumerate(stream, 1):
            if not line.strip():
                continue
            obj = json.loads(line)
            if not isinstance(obj, dict):
                raise ValueError(f"{path}:{line_num}: expected object")
            rows.append(obj)
    return rows

def normalize_text(value):
    return re.sub(r"\s+", " ", str(value).strip()).casefold()

def by_id(rows, field):
    result = {}
    for item in rows:
        key = str(item.get(field, "")).strip()
        if not key or key in result:
            raise ValueError(f"missing or duplicate {field}: {key!r}")
        result[key] = item
    return result

def evaluate(gold_rows, candidate_rows):
    gold = by_id(gold_rows, "financebench_id")
    cand = by_id(candidate_rows, "financebench_id")
    if not gold:
        raise ValueError("empty gold dataset")
    unknown = sorted(set(cand) - set(gold))
    if unknown:
        raise ValueError(f"unknown candidate IDs: {unknown[:5]}")
    details = []
    answered = exact = evidence_supported = citations_provided = 0
    by_question_type = {}
    for key, reference in gold.items():
        response = cand.get(key, {})
        answer = str(response["predicted_answer"]).strip() if response.get("predicted_answer") is not None else ""
        attempted = bool(answer)
        if attempted:
            answered += 1
        match = attempted and normalize_text(answer) == normalize_text(reference.get("answer", ""))
        exact += int(match)
        refs = set()
        for evidence in reference.get("evidence") or []:
            if isinstance(evidence, dict) and evidence.get("evidence_doc_name"):
                refs.add(str(evidence["evidence_doc_name"]))
        cited = {str(x) for x in (response.get("cited_evidence_doc_names") or []) if str(x)}
        has_citations = bool(cited)
        citations_provided += int(has_citations)
        cited_document_match = bool(refs and cited and cited.issubset(refs))
        evidence_supported += int(cited_document_match)
        bucket = str(reference.get("question_type") or "unknown")
        count = by_question_type.setdefault(bucket, {"n": 0, "exact_matches": 0, "answered": 0})
        count["n"] += 1
        count["exact_matches"] += int(match)
        count["answered"] += int(attempted)
        details.append({"financebench_id": key, "question_type": bucket, "answered": attempted,
                        "strict_exact_match": bool(match),
                        "cited_gold_document": cited_document_match,
                        "citation_document_provenance_checked": bool(refs)})
    n = len(gold)
    return {"n": n, "answered": answered, "coverage": round(answered / n, 5),
            "abstention_rate": round((n - answered) / n, 5),
            "strict_exact_match_overall": round(exact / n, 5),
            "strict_exact_match_answered": round(exact / answered, 5) if answered else None,
            "citation_present_rate": round(citations_provided / n, 5),
            "citation_doc_name_match_rate": round(evidence_supported / n, 5),
            "question_type": by_question_type, "records": details,
            "limitations": [
                "Strict string equality is not semantic or numerical equivalence.",
                "Document-name citation matching does not demonstrate textual entailment.",
                "No independent adjudication or model invocation.",
                "Scores depend on the authorized local benchmark and supplied predictions."]}

def main():
    parser = argparse.ArgumentParser(description="Offline FinanceBench evaluator")
    parser.add_argument("--gold", required=True, help="Locally authorized FinanceBench JSONL file")
    parser.add_argument("--pred", action="append", required=True, metavar="NAME=JSONL",
                        help="Repeat for multiple candidates; no LLM is called")
    parser.add_argument("--out", required=True, help="Local JSON report path")
    args = parser.parse_args()
    gold = read_jsonl(args.gold)
    reports = {}
    for pair in args.pred:
        name, sep, path = pair.partition("=")
        if not sep or not name or not path or name in reports:
            parser.error("--pred must be unique NAME=JSONL")
        reports[name] = evaluate(gold, read_jsonl(path))
    out = {"benchmark": "FinanceBench, Patronus AI, CC BY-NC 4.0",
           "source": "https://huggingface.co/datasets/PatronusAI/financebench",
           "comparison": reports, "data_embedded": False,
           "notes": "Not a model evaluation unless supplied files contain genuine model output."}
    p = Path(args.out); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {p} for {len(reports)} candidate(s)")

if __name__ == "__main__":
    main()
