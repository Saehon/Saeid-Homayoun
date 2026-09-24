"""FRANKENSTEIN Phase 4 cross-model benchmark harness."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import time
from pathlib import Path

from adapters import call_provider

ROOT = Path(__file__).resolve().parent
CASE_PATH = ROOT / "case_001_bank_reconciliation.json"
PROVIDERS_PATH = ROOT / "providers.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def prompt_for(case: dict) -> str:
    evidence = "\n".join(f"{x['id']}: {x['fact']}" for x in case["evidence"])
    tasks = "\n".join(f"- {x}" for x in case["task"])
    schema = json.dumps(case["required_output_schema"], indent=2)
    return f"""CASE {case['case_id']}: {case['title']}

Use ONLY the evidence below. If you need a fact that is not present, put it in unsupported_claims rather than inventing it.

EVIDENCE
{evidence}

TASKS
{tasks}

RETURN EXACTLY ONE JSON OBJECT MATCHING THIS SCHEMA
{schema}

Allowed item labels:
service_fee, interest_income, outstanding_checks, deposit_in_transit

Allowed journal-entry account labels:
bank_service_fee_expense, cash, interest_income
"""


def extract_json(text: str) -> dict:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, flags=re.S)
        if not match:
            raise
        return json.loads(match.group(0))


def normalized_entries(entries: list[dict]) -> set[tuple]:
    return {
        (
            str(x.get("debit_account", "")).strip().lower(),
            str(x.get("credit_account", "")).strip().lower(),
            float(x.get("amount", 0)),
        )
        for x in entries
    }


def score(case: dict, answer: dict) -> dict:
    gold = case["gold_standard"]
    components = {}

    components["adjusted_bank_balance"] = float(answer.get("adjusted_bank_balance", float("nan"))) == float(gold["adjusted_bank_balance"])
    components["adjusted_book_balance"] = float(answer.get("adjusted_book_balance", float("nan"))) == float(gold["adjusted_book_balance"])
    components["book_entry_items"] = set(answer.get("book_entry_items", [])) == set(gold["book_entry_items"])
    components["bank_only_items"] = set(answer.get("bank_only_items", [])) == set(gold["bank_only_items"])
    components["journal_entries"] = normalized_entries(answer.get("journal_entries", [])) == normalized_entries(gold["journal_entries"])
    components["balances"] = answer.get("balances") is gold["balances"]
    components["evidence_complete"] = set(answer.get("evidence_ids_used", [])) == set(gold["required_evidence_ids"])
    components["unsupported_claims_empty"] = answer.get("unsupported_claims", []) == []

    accuracy = sum(bool(v) for v in components.values()) / len(components)
    return {
        "accuracy": accuracy,
        "components": components,
        "unsupported_claim_count": len(answer.get("unsupported_claims", [])),
        "passed": accuracy == 1.0,
    }


def provider_ready(cfg: dict) -> tuple[bool, list[str]]:
    required = [cfg["api_key_env"], cfg["model_env"]]
    if not (os.environ.get(cfg["url_env"]) or cfg.get("default_url")):
        required.append(cfg["url_env"])
    missing = [x for x in required if not os.environ.get(x)]
    return not missing, missing


def run_one(provider_id: str, cfg: dict, case: dict) -> dict:
    ready, missing = provider_ready(cfg)
    if not ready:
        return {
            "provider": provider_id,
            "family": cfg["family"],
            "status": "skipped_missing_configuration",
            "missing_env": missing,
        }

    prompt = prompt_for(case)
    started = time.perf_counter()
    raw = call_provider(cfg, prompt)
    elapsed = time.perf_counter() - started
    answer = extract_json(raw)
    scored = score(case, answer)

    return {
        "provider": provider_id,
        "family": cfg["family"],
        "status": "completed",
        "model": os.environ.get(cfg["model_env"]),
        "endpoint_env": cfg["url_env"],
        "elapsed_seconds": round(elapsed, 4),
        "answer": answer,
        "score": scored,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["dry-run", "live", "score-mock"], default="dry-run")
    parser.add_argument("--provider", action="append", default=[])
    parser.add_argument("--output")
    args = parser.parse_args()

    case = load(CASE_PATH)
    providers_doc = load(PROVIDERS_PATH)
    selected = args.provider or list(providers_doc["providers"])

    if args.mode == "dry-run":
        result = {
            "case_id": case["case_id"],
            "providers": [
                {
                    "provider": pid,
                    "family": providers_doc["providers"][pid]["family"],
                    "ready": provider_ready(providers_doc["providers"][pid])[0],
                    "missing_env": provider_ready(providers_doc["providers"][pid])[1],
                }
                for pid in selected
            ],
            "prompt": prompt_for(case),
        }
    elif args.mode == "score-mock":
        mock = load(ROOT / "mock_perfect_response.json")
        result = {"case_id": case["case_id"], "score": score(case, mock)}
    else:
        result = {
            "case_id": case["case_id"],
            "run_timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "results": [
                run_one(pid, providers_doc["providers"][pid], case)
                for pid in selected
            ],
        }

    rendered = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
