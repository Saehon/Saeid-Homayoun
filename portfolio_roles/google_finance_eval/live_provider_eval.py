"""Opt-in, capped, provider-neutral model evaluation. Stdlib only.

No network call unless --execute, no secret persisted, and no dataset downloaded.
Usage-derived costs are estimates, not provider invoices.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

PROVIDERS = {
    "openai": ("OPENAI_API_KEY", "https://api.openai.com/v1/responses"),
    "anthropic": ("ANTHROPIC_API_KEY", "https://api.anthropic.com/v1/messages"),
    "gemini": ("GEMINI_API_KEY", "https://generativelanguage.googleapis.com/v1beta/models/"),
}
MODEL_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,99}$")

def as_number(v):
    if isinstance(v, bool) or not isinstance(v, (float, int)):
        raise ValueError("pricing and budgets must be numeric")
    if v < 0 or v != v or v == float("inf"):
        raise ValueError("pricing and budgets must be finite and nonnegative")
    return float(v)

def normalize_response(provider, data):
    """Return text and reported token usage without synthesizing missing counts."""
    if provider == "openai":
        texts = [c.get("text", "") for item in data.get("output", [])
                 if item.get("type") == "message"
                 for c in item.get("content", []) if c.get("type") == "output_text"]
        usage = data.get("usage") or {}
        counts = (usage.get("input_tokens"), usage.get("output_tokens"))
    elif provider == "anthropic":
        texts = [c.get("text", "") for c in data.get("content", []) if c.get("type") == "text"]
        usage = data.get("usage") or {}
        counts = (usage.get("input_tokens"), usage.get("output_tokens"))
    else:
        candidates = data.get("candidates", [])
        texts = [p.get("text", "") for c in candidates[:1]
                 for p in (c.get("content") or {}).get("parts", []) if "text" in p]
        usage = data.get("usageMetadata") or {}
        if usage.get("candidatesTokenCount") is None:
            counts = (usage.get("promptTokenCount"), None)
        else:
            counts = (usage.get("promptTokenCount"),
                      usage.get("candidatesTokenCount", 0) + usage.get("thoughtsTokenCount", 0))
    if any(type(n) is not int or n < 0 for n in counts):
        raise ValueError("Provider response has missing/invalid usage counters; cost not verifiable")
    return "".join(texts).strip(), counts[0], counts[1]

def request_payload(provider, model, prompt, max_output):
    if provider == "openai":
        return {"model": model, "input": prompt, "max_output_tokens": max_output, "store": False}
    if provider == "anthropic":
        return {"model": model, "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_output}
    return {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {"maxOutputTokens": max_output}}

def call_provider(provider, model, prompt, max_output, secret, transport=None):
    if not MODEL_RE.fullmatch(model):
        raise ValueError("Unsafe or invalid model identifier")
    key, root = PROVIDERS[provider]
    del key
    url = root + model + ":generateContent" if provider == "gemini" else root
    headers = {"Content-Type": "application/json"}
    if provider == "openai":
        headers["Authorization"] = "Bearer " + secret
    elif provider == "anthropic":
        headers.update({"x-api-key": secret, "anthropic-version": "2023-06-01"})
    else:
        headers["x-goog-api-key"] = secret
    payload = json.dumps(request_payload(provider, model, prompt, max_output)).encode()
    req = Request(url, data=payload, headers=headers, method="POST")
    opener = transport or urlopen
    try:
        with opener(req, timeout=35) as resp:
            data = json.load(resp)
    except HTTPError as exc:
        # NEVER include raw provider response body: it might contain request data.
        raise RuntimeError(f"{provider} HTTP status {exc.code}") from None
    except (URLError, TimeoutError) as exc:
        raise RuntimeError(f"{provider} transport failure: {type(exc).__name__}") from None
    return normalize_response(provider, data)

def load_cases(filename, schema):
    rows = []
    seen = set()
    for line_no, line in enumerate(Path(filename).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        if not isinstance(row, dict):
            raise ValueError(f"line {line_no}: expected object")
        ident = row.get("financebench_id" if schema == "financebench" else "case_id")
        if not isinstance(ident, str) or not ident or ident in seen:
            raise ValueError("Missing/duplicate case id")
        seen.add(ident)
        q = row.get("question" if schema == "financebench" else "prompt")
        if not isinstance(q, str) or not q.strip() or len(q.encode()) > 14000:
            raise ValueError("Missing or excessive question size")
        evidence = ""
        if schema == "financebench":
            parts = []
            for item in (row.get("evidence") or []):
                if isinstance(item, dict) and isinstance(item.get("evidence_text"), str):
                    parts.append(item["evidence_text"])
            evidence = "\n\n".join(parts)
            if not evidence:
                raise ValueError("FinanceBench open-book mode requires evidence_text")
        else:
            evidence = row.get("evidence_text") or ""
        if not isinstance(evidence, str) or len(evidence.encode()) > 40000:
            raise ValueError("Missing/oversize evidence")
        prompt = ("Answer the financial or assurance question only from the provided evidence. "
                  "If insufficient, answer ABSTAIN. Give only the short answer and an optional source ID.\n"
                  f"QUESTION:\n{q}\nEVIDENCE:\n{evidence}\n")
        if len(prompt.encode()) > 50000:
            raise ValueError("Prompt exceeds approved size")
        rows.append({"case_id": ident, "prompt": prompt, "gold": row.get("answer" if schema == "financebench" else "gold_answer")})
    if not rows:
        raise ValueError("No evaluation rows found")
    return rows

def preflight(args, cases, api_key_available):
    if args.max_cases < 1 or args.max_cases > 10:
        raise ValueError("--max-cases must be in 1..10")
    if args.max_output_tokens < 16 or args.max_output_tokens > 1024:
        raise ValueError("--max-output-tokens must be in 16..1024")
    if not MODEL_RE.fullmatch(args.model):
        raise ValueError("Invalid model identifier")
    in_price, out_price, budget = map(as_number,
                                     (args.input_usd_per_million, args.output_usd_per_million, args.max_usd))
    if budget <= 0:
        raise ValueError("Must specify a positive budget")
    rows = cases[:args.max_cases]
    # Very conservative preflight: upper-bound token count approximated as UTF-8 byte count.
    # Not a hard billing limit: provider reasoning, multimodal, cache or tool fees may differ.
    conservative = sum((len(r["prompt"].encode()) * in_price +
                        args.max_output_tokens * out_price) / 1_000_000 for r in rows)
    if conservative > budget:
        raise ValueError("Conservative upper-bound exceeds budget; reduce cases/tokens")
    if args.execute and not api_key_available:
        raise ValueError("Required provider credential is not configured")
    if args.execute and not args.authorize_data_transfer:
        raise ValueError("Explicit --authorize-data-transfer required for API transmission")
    return rows, conservative

def evaluate(args, transport=None):
    cases = load_cases(args.cases, args.schema)
    key_env = PROVIDERS[args.provider][0]
    secret = os.getenv(key_env, "")
    rows, upper = preflight(args, cases, bool(secret))
    report = {
        "provider": args.provider, "model": args.model, "schema": args.schema,
        "execution": "api_run" if args.execute else "dry_run_no_api_calls",
        "source_sha256": hashlib.sha256(Path(args.cases).read_bytes()).hexdigest(),
        "cases_selected": len(rows), "budget_cap_requested_usd": args.max_usd,
        "conservative_preflight_usd": round(upper, 8),
        "input_price_usd_per_million": args.input_usd_per_million,
        "output_price_usd_per_million": args.output_usd_per_million,
        "price_source": args.price_source,
        "cost_is_estimate_not_invoice": True,
        "notes": ["No financial question content or keys included in report",
                  "Dry run does not demonstrate model performance",
                  "Prompt byte heuristic and token estimates are not a hard billing cap",
                  "Quality claims require independent adjudication and licensed sources"],
        "records": []}
    if not args.execute:
        return report
    spent = 0.
    for record in rows:
        # Do not launch another paid request once billed estimate is at cap.
        if spent >= args.max_usd:
            report["records"].append({"case_id": record["case_id"], "status": "SKIPPED_BUDGET"})
            continue
        start = time.monotonic()
        try:
            answer, in_tokens, out_tokens = call_provider(args.provider, args.model,
                            record["prompt"], args.max_output_tokens, secret, transport=transport)
            charge = (in_tokens * args.input_usd_per_million +
                      out_tokens * args.output_usd_per_million) / 1_000_000
            spent += charge
            report["records"].append({
                "case_id": record["case_id"], "status": "ok", "predicted_answer": answer,
                "abstained": answer.strip().upper() == "ABSTAIN" or not answer.strip(),
                "input_tokens": in_tokens, "output_tokens": out_tokens,
                "cost_estimate_usd": round(charge, 8),
                "elapsed_ms": round((time.monotonic()-start)*1000),
                "strict_exact_match": answer.strip().casefold() == str(record["gold"]).strip().casefold()
                                     if record["gold"] is not None else None,
            })
        except (RuntimeError, ValueError, KeyError) as exc:
            # An unsuccessful request might still incur billable tokens; unknown cost.
            report["records"].append({"case_id": record["case_id"], "status": "ERROR",
                                      "error_type": type(exc).__name__, "cost_unknown": True})
            report["cost_incomplete_due_to_errors"] = True
            break
    report["estimated_usage_cost_usd"] = round(spent, 8)
    report["completed_requests"] = sum(r["status"] == "ok" for r in report["records"])
    return report

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--cases", required=True)
    p.add_argument("--schema", choices=("synthetic", "financebench"), default="synthetic")
    p.add_argument("--provider", choices=tuple(PROVIDERS), required=True)
    p.add_argument("--model", required=True)
    p.add_argument("--max-cases", type=int, default=2)
    p.add_argument("--max-output-tokens", type=int, default=200)
    p.add_argument("--input-usd-per-million", type=float, required=True)
    p.add_argument("--output-usd-per-million", type=float, required=True)
    p.add_argument("--max-usd", type=float, required=True)
    p.add_argument("--price-source", required=True, help="Provider pricing page and verified date")
    p.add_argument("--execute", action="store_true")
    p.add_argument("--authorize-data-transfer", action="store_true",
                   help="Confirm license, institutional approval, and provider data sharing")
    p.add_argument("--out", required=True)
    args = p.parse_args()
    report = evaluate(args)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"report: {out}; execution={report['execution']}; completed={report.get('completed_requests', 0)}")

if __name__ == "__main__":
    main()
