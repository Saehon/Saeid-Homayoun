#!/usr/bin/env python3
"""Probe free/public SEC XBRL availability for the NAAIL replication cohort.

This script is intentionally narrow: it validates public SEC access and writes a
machine-readable status file. It does not treat data accessibility as scientific
execution or validation.
"""
from __future__ import annotations

import csv
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "company_registry_free_public_v1.csv"
OUT = ROOT / "sec_free_public_probe_results.json"
USER_AGENT = os.environ.get(
    "SEC_USER_AGENT",
    "NAAIL-OpenLab academic research contact: repository-owner",
)


def get_json(url: str) -> tuple[str, dict | None, str | None]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept-Encoding": "gzip, deflate"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            payload = json.loads(r.read().decode("utf-8"))
            return "PASS", payload, None
    except urllib.error.HTTPError as exc:
        return "FAIL", None, f"HTTP {exc.code}"
    except Exception as exc:  # preserve exact failure instead of hiding it
        return "BLOCKED", None, f"{type(exc).__name__}: {exc}"


def main() -> int:
    rows = list(csv.DictReader(REGISTRY.open(encoding="utf-8")))
    results = []
    for row in rows:
        cik = row["cik"]
        companyfacts = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
        submissions = f"https://data.sec.gov/submissions/CIK{cik}.json"
        cf_status, cf, cf_error = get_json(companyfacts)
        time.sleep(0.15)
        sub_status, sub, sub_error = get_json(submissions)
        time.sleep(0.15)

        latest_forms = []
        if sub:
            latest_forms = sub.get("filings", {}).get("recent", {}).get("form", [])[:25]

        results.append(
            {
                "company": row["company"],
                "ticker": row["ticker"],
                "cik": cik,
                "cohort": row["cohort"],
                "companyfacts_status": cf_status,
                "companyfacts_entity_name": (cf or {}).get("entityName"),
                "companyfacts_taxonomies": sorted(list((cf or {}).get("facts", {}).keys())),
                "companyfacts_error": cf_error,
                "submissions_status": sub_status,
                "recent_annual_form_present": row["annual_form"] in latest_forms,
                "submissions_error": sub_error,
                "interpretation": (
                    "FREE_PUBLIC_SOURCE_VERIFIED"
                    if cf_status == "PASS" and sub_status == "PASS"
                    else "REQUIRES_REVIEW"
                ),
            }
        )

    OUT.write_text(json.dumps({"results": results}, indent=2), encoding="utf-8")
    failures = [r for r in results if r["interpretation"] != "FREE_PUBLIC_SOURCE_VERIFIED"]
    print(f"Probed {len(results)} companies; review required: {len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
