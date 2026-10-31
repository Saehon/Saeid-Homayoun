"""Offline financial AI answer and evidence evaluation (synthetic reference).

This deterministic grader is a research demonstration, not an LLM or an
independently validated financial reasoning benchmark.

Python 3.10+. No external dependency, model call, or network request.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path

def load_jsonl(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    result = []
    for position, line in enumerate(lines, 1):
        if not line.strip():
            continue
        data = json.loads(line)
        if not isinstance(data, dict):
            raise ValueError(f"line {position}: expected JSON object")
        result.append(data)
    if not result:
        raise ValueError("no evaluation cases")
    return result

def index_records(rows, kind):
    result = {}
    for row in rows:
        key = row.get("case_id")
        if not isinstance(key, str) or not key or key in result:
            raise ValueError(f"{kind}: missing or duplicate case_id")
        result[key] = row
    return result

def validate_reference(gold):
    for key in ("question", "domain", "answer", "answer_type", "evidence_ids",
                "reference_provenance", "label_provenance", "source_rights"):
        if key not in gold:
            raise ValueError("reference missing " + key)
    if not gold["question"] or not gold["reference_provenance"] or not gold["source_rights"]:
        raise ValueError("reference provenance fields must be nonempty")
    if gold["answer_type"] not in ("numeric", "text"):
        raise ValueError("unsupported answer type")
    ids = gold["evidence_ids"]
    if (not isinstance(ids, list) or not ids or
        not all(isinstance(e, str) and e for e in ids) or len(ids) != len(set(ids))):
        raise ValueError("reference evidence IDs must be unique nonempty strings")
    if gold["answer_type"] == "numeric":
        numeric(gold["answer"])
        if "absolute_tolerance" not in gold:
            raise ValueError("numeric reference requires absolute_tolerance")
        if numeric(gold["absolute_tolerance"]) < 0:
            raise ValueError("tolerance must be nonnegative")

def numeric(value):
    if value is None or isinstance(value, bool):
        raise ValueError("missing/boolean numerical value")
    try:
        result = Decimal(str(value))
    except (ValueError, InvalidOperation, TypeError) as exc:
        raise ValueError("unparseable numerical value") from exc
    if not result.is_finite():
        raise ValueError("non-finite numerical value")
    return result

def answer_matches(reference, predicted):
    if reference["answer_type"] == "numeric":
        try:
            return abs(numeric(reference["answer"]) - numeric(predicted)) <= numeric(reference["absolute_tolerance"])
        except ValueError:
            return False
    return " ".join(str(reference["answer"]).split()).casefold() == " ".join(str(predicted).split()).casefold()

def score(reference, prediction):
    if prediction is None:
        return {"status": "missing_prediction", "answered": False, "answer_correct": False,
                "citation_id_match": False, "grounded_correct": False}
    state = prediction.get("status")
    if state not in ("answered", "abstained"):
        return {"status": "invalid_prediction", "answered": False, "answer_correct": False,
                "citation_id_match": False, "grounded_correct": False}
    if state == "abstained":
        return {"status": "abstained", "answered": False, "answer_correct": False,
                "citation_id_match": False, "grounded_correct": False}
    answer = prediction.get("model_answer")
    citations = prediction.get("cited_evidence_ids")
    if answer is None or not isinstance(citations, list) or not all(isinstance(x, str) and x for x in citations):
        return {"status": "invalid_prediction", "answered": False, "answer_correct": False,
                "citation_id_match": False, "grounded_correct": False}
    correct = answer_matches(reference, answer)
    allowed = set(reference["evidence_ids"])
    citation_match = bool(citations) and set(citations).issubset(allowed)
    if not citation_match:
        status = "citation_id_missing_or_unsupported"
    elif not correct:
        status = "answer_mismatch"
    else:
        status = "passed_synthetic_contract"
    return {"status": status, "answered": True, "answer_correct": bool(correct),
            "citation_id_match": bool(citation_match),
            "grounded_correct": bool(correct and citation_match)}

def run_evaluation(gold_rows, model_rows, development_ids=()):
    gold = index_records(gold_rows, "reference")
    predictions = index_records(model_rows, "prediction") if model_rows else {}
    if set(predictions) - set(gold):
        raise ValueError("predictions include unregistered case IDs")
    overlap = set(gold).intersection(set(development_ids))
    if overlap:
        raise ValueError("development/holdout ID overlap: " + str(len(overlap)))
    for case in gold.values():
        validate_reference(case)
    results = [{"case_id":case_id, "domain":case["domain"],
                **score(case, predictions.get(case_id))}
               for case_id, case in gold.items()]
    total = len(results)
    answered = sum(r["answered"] for r in results)
    answer_correct = sum(r["answer_correct"] for r in results)
    grounded = sum(r["grounded_correct"] for r in results)
    citations_ok = sum(r["citation_id_match"] for r in results)
    summary = {
        "n": total, "answered": answered, "abstentions": sum(r["status"] == "abstained" for r in results),
        "missing_or_invalid": sum(r["status"] in ("missing_prediction", "invalid_prediction") for r in results),
        "coverage": round(answered / total, 5),
        "answer_accuracy_all_cases": round(answer_correct / total, 5),
        "answer_accuracy_answered": round(answer_correct / answered, 5) if answered else None,
        "citation_id_match_rate_all": round(citations_ok / total, 5),
        "grounded_correct_rate_all": round(grounded / total, 5),
        "error_counts": {name: sum(r["status"] == name for r in results)
                         for name in sorted(set(r["status"] for r in results))},
    }
    return {"scope": "deterministic synthetic_contract_validation",
            "summary": summary, "records": results,
            "limitations": [
                "References and predictions may be deliberately synthetic; no actual model evaluation is implied.",
                "Citation ID inclusion is not evidence-text entailment or source reliability.",
                "No independent labeling or holdout secrecy is authenticated by this script.",
                "Strict text matching is not semantic grading.",
                "Statistical inference and human validation are required for externally valid empirical claims."
            ]}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    here = Path(__file__).resolve().parent
    parser.add_argument("--gold", default=str(here / "examples" / "synthetic_gold.jsonl"))
    parser.add_argument("--predictions", default=str(here / "examples" / "synthetic_predictions.jsonl"))
    parser.add_argument("--dev-ids", default=None, help="Optional JSON file containing development case IDs")
    parser.add_argument("--out", default=None, help="Optional local JSON report output")
    args = parser.parse_args()
    gold_bytes = Path(args.gold).read_bytes()
    prediction_bytes = Path(args.predictions).read_bytes()
    dev_ids = json.loads(Path(args.dev_ids).read_text(encoding="utf-8")) if args.dev_ids else []
    if not isinstance(dev_ids, list) or not all(isinstance(x, str) for x in dev_ids):
        parser.error("--dev-ids must be a JSON array of case ID strings")
    report = run_evaluation(load_jsonl(args.gold), load_jsonl(args.predictions), dev_ids)
    report["reference_sha256"] = hashlib.sha256(gold_bytes).hexdigest()
    report["predictions_sha256"] = hashlib.sha256(prediction_bytes).hexdigest()
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        dest = Path(args.out)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(rendered, encoding="utf-8")
        print("Wrote synthetic evaluation report to", dest)
    else:
        print(rendered)

if __name__ == "__main__":
    main()
