"""NAAIL Finance & Assurance: offline, synthetic-first draft workpaper validator."""
from __future__ import annotations
import argparse
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path

STATUS = "DRAFT_REQUIRES_HUMAN_REVIEW"


def money(value):
    """Fixed-point arithmetic; reject non-finite monetary values."""
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError(f"Invalid monetary amount: {value!r}") from exc
    if not amount.is_finite():
        raise ValueError("Non-finite monetary amount")
    return amount.quantize(Decimal("0.01"))


def fmt(value):
    return str(money(value))


def envelope(command, data, result):
    raw = json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return {"workflow": command, "status": STATUS,
            "input_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
            "source_type": "synthetic_or_user_supplied_unverified", "result": result,
            "caution": "Draft only. Qualified professional must verify source evidence and approve conclusions."}


def journal_entry(data):
    lines = data["lines"]
    if not lines:
        raise ValueError("At least one journal line is required")
    debits = sum((money(x.get("debit", 0)) for x in lines), Decimal(0))
    credits = sum((money(x.get("credit", 0)) for x in lines), Decimal(0))
    invalid = [i + 1 for i, x in enumerate(lines)
               if (money(x.get("debit", 0)) < 0 or money(x.get("credit", 0)) < 0
                   or (money(x.get("debit", 0)) > 0 and money(x.get("credit", 0)) > 0))]
    missing_evidence = [i + 1 for i, x in enumerate(lines) if not x.get("evidence_ref")]
    return {"debits": fmt(debits), "credits": fmt(credits),
            "balanced": debits == credits and debits > 0,
            "invalid_line_numbers": invalid, "missing_evidence_line_numbers": missing_evidence,
            "ready_for_review": debits == credits and debits > 0 and not invalid and not missing_evidence}


def reconciliation(data):
    bank = money(data["bank_balance"])
    ledger = money(data["gl_balance"])
    deposits = sum((money(x["amount"]) for x in data.get("deposits_in_transit", [])), Decimal(0))
    checks = sum((money(x["amount"]) for x in data.get("outstanding_checks", [])), Decimal(0))
    gl_credits = sum((money(x["amount"]) for x in data.get("gl_additions", [])), Decimal(0))
    gl_debits = sum((money(x["amount"]) for x in data.get("gl_deductions", [])), Decimal(0))
    if any(x < 0 for x in (deposits, checks, gl_credits, gl_debits)):
        raise ValueError("Reconciliation line amounts must be unsigned; categories supply direction")
    adjusted_bank = bank + deposits - checks
    adjusted_gl = ledger + gl_credits - gl_debits
    missing = [x.get("item_id", "UNKNOWN") for cat in
               ("deposits_in_transit", "outstanding_checks", "gl_additions", "gl_deductions")
               for x in data.get(cat, []) if not x.get("evidence_ref")]
    return {"adjusted_bank": fmt(adjusted_bank), "adjusted_gl": fmt(adjusted_gl),
            "unreconciled_difference": fmt(adjusted_bank-adjusted_gl),
            "numerically_reconciled": adjusted_bank == adjusted_gl,
            "items_missing_evidence": missing,
            "ready_for_review": adjusted_bank == adjusted_gl and not missing}


def income_statement(data):
    rows = data["accounts"]
    if not rows:
        raise ValueError("Income statement requires accounts")
    if any(x["kind"] not in ("revenue", "expense") for x in rows):
        raise ValueError("Account kind must be revenue or expense")
    def calculate(column, kind):
        return sum((money(x.get(column, 0)) for x in rows if x["kind"] == kind), Decimal(0))
    rev, exp = calculate("current", "revenue"), calculate("current", "expense")
    prev_rev, prev_exp = calculate("prior", "revenue"), calculate("prior", "expense")
    return {"revenue": fmt(rev), "expenses": fmt(exp), "income": fmt(rev-exp),
            "prior_revenue": fmt(prev_rev), "prior_expenses": fmt(prev_exp),
            "prior_income": fmt(prev_rev-prev_exp),
            "income_change": fmt((rev-exp)-(prev_rev-prev_exp)),
            "note": "Unaudited subtotal illustration; classifications, taxes and presentation require review."}


def variance_analysis(data):
    output = []
    for row in data["items"]:
        current, reference = money(row["actual"]), money(row["comparison"])
        delta = current-reference
        pct = None if reference == 0 else str((delta/reference*100).quantize(Decimal("0.01")))
        output.append({"account": row["account"], "actual": fmt(current),
                       "comparison": fmt(reference), "difference": fmt(delta),
                       "difference_percent": pct,
                       "evidence_ref": row.get("evidence_ref"),
                       "unexplained": not bool(row.get("explanation"))})
    return {"items": output, "comparison_label": data.get("comparison_label", "reference"),
            "note": "Variance is descriptive, not causal attribution."}


def sox_testing(data):
    population = data["population"]
    ids = [str(x["id"]) for x in population]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate population IDs")
    n = int(data["sample_size"])
    if n < 1 or n > len(population):
        raise ValueError("Sample size outside population")
    seed = str(data.get("seed", "0"))
    # Deterministic, reproducible priority; not a statistical audit sampling method.
    chosen = sorted(population, key=lambda x:
                    hashlib.sha256((seed + "|" + str(x["id"])).encode()).hexdigest())[:n]
    return {"control_id": data["control_id"], "population_size": len(population),
            "sample_size": n, "selected_ids": [str(x["id"]) for x in chosen],
            "sample_exceptions": [str(x["id"]) for x in chosen if x.get("exception")],
            "selected_missing_evidence": [str(x["id"]) for x in chosen if not x.get("evidence_ref")],
            "sampling_method": "deterministic illustrative hash ordering",
            "conclusion": "NO_CONTROL_EFFECTIVENESS_CONCLUSION",
            "note": "Not a representative statistical audit sample; investigate full population and selection bias."}


WORKFLOWS = {"journal-entry": journal_entry, "reconciliation": reconciliation,
             "income-statement": income_statement, "variance-analysis": variance_analysis,
             "sox-testing": sox_testing}


def finance_workpaper(command, data):
    if command not in WORKFLOWS:
        raise ValueError("Unknown workflow")
    return envelope(command, data, WORKFLOWS[command](data))


def main():
    parser = argparse.ArgumentParser(description="Offline draft finance workpapers; no automated approval")
    parser.add_argument("workflow", choices=sorted(WORKFLOWS))
    parser.add_argument("input_json", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input_json.read_text(encoding="utf-8"))
    print(json.dumps(finance_workpaper(args.workflow, data), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
