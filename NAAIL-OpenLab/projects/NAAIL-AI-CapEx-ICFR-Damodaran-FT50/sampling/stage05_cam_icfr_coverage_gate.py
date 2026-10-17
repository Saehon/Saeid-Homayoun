"""Stage 05: reproducible CAM/ICFR descriptive QA, NOT a causal estimator.

Inputs: existing public 10-issuer FY2025 audit pilot and V6 source summary.
The FY2025 pilot is not the FY2021–FY2024 V6 regression population.
Usage: python sampling/stage05_cam_icfr_coverage_gate.py data/public_FY2025_audit_panel.csv sampling/ACTUAL_SEC_GAAP_FORMAP_AUDITOR_JOINS_V6_2026-10-10.json
"""
import csv
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path


def run(pilot_path: Path, v6_path: Path):
    with pilot_path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    v6 = json.loads(v6_path.read_text(encoding="utf-8"))
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise ValueError("Stage05 gate failed: " + name)

    check("ten_distinct_issuers", len(rows) == 10 and len({r["ticker"] for r in rows}) == 10)
    check("five_each_economic_role",
          Counter(r["economic_role"] for r in rows) == {"Builder": 5, "Supplier": 5})
    check("cam_counts_match_topic_lists",
          all(int(r["cam_topic_count"]) == len(r["cam_topics"].split(";")) for r in rows))
    check("inventory_flags_match_topics",
          all(int(r["cam_inventory_topic"]) == int("inventory" in r["cam_topics"]) for r in rows))
    check("uncertain_tax_flags_match_topics",
          all(int(r["cam_uncertain_tax_topic"]) == int("uncertain_tax" in r["cam_topics"]) for r in rows))
    check("icfr_auditor_opinion_populated",
          all(r["icfr_auditor_opinion"].strip() for r in rows))
    check("public_inspection_asof_flags_match_dates",
          all(int(r["pcaob_prior_to_auditor_report"]) ==
              int(date.fromisoformat(r["pcaob_publication_date"]) <=
                  date.fromisoformat(r["auditor_report_date"])) for r in rows))
    check("future_inspection_rate_masked",
          all(not r["pcaob_selected_audit_deficiency_share"]
              for r in rows if r["pcaob_prior_to_auditor_report"] == "0"))
    check("ai_only_capex_missing_not_zero",
          all(not r["ai_capex_fy2025_usd_m"] for r in rows))
    check("risk_cam_scores_missing_not_zero",
          all(not r["cam_risk_mismatch_score"] for r in rows))
    check("original_sec_source_urls_present",
          all(r["sec_10k_source_url"].startswith("https://www.sec.gov/Archives/")
              for r in rows))
    result = {
        "stage": "05_CAM_ICFR",
        "status": "PARTIAL",
        "scope": "10 selected FY2025 pilot issuers; independent V6 FY2021–2024 summary",
        "tests_passed": len(checks),
        "checks": checks,
        "pilot_issuer_rows": len(rows),
        "pilot_cam_topic_mentions": sum(int(r["cam_topic_count"]) for r in rows),
        "pilot_effective_icfr_auditor_opinions":
            sum(r["icfr_auditor_opinion"] == "effective_unqualified" for r in rows),
        "pilot_distinct_audit_firms": len({r["auditor_legal_name"] for r in rows}),
        "pilot_missing_ai_only_capex": sum(not r["ai_capex_fy2025_usd_m"] for r in rows),
        "pilot_missing_independent_risk_cam": sum(not r["cam_risk_mismatch_score"] for r in rows),
        "pilot_prior_public_pcaob": sum(r["pcaob_prior_to_auditor_report"] == "1" for r in rows),
        "v6_fy2021_2024_issuer_years": v6["main_period_and_formAP_single_registered_firm_issuer_years"],
        "v6_cash_flow_candidate_issuer_years":
            v6["main_CFO_and_cash_PPE_and_following_year_CFO_and_formAP"],
        "v6_cam_eligibility_and_risk_verified": v6["CAM_eligibility_and_risk_verified"],
        "v6_icfr_mw_verified": v6["SOX_ICFR_material_weakness_verified"],
        "v6_row_level_cam_icfr_coverage": None,
        "v6_verified_regression_N": None,
        "caveats": [
            "FY2025 pilot is NOT linked to historical FY2021–2024 V6 sample.",
            "CAM topic list is first-pass coded, not independently second-coded.",
            "CAM eligibility and EGC/filer exceptions have not been validated.",
            "Auditor effective ICFR opinion is not a full 404(a)/404(b) longitudinal MW label.",
            "No independent account-level risk–CAM mismatch scores exist.",
            "Missing CAM/ICFR labels must never be coded as negative/zero.",
            "No AI-only CapEx, causal audit-oversight, or H1–H5 results."
        ]
    }
    return result


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: stage05_cam_icfr_coverage_gate.py PILOT.csv V6.json")
    print(json.dumps(run(Path(sys.argv[1]), Path(sys.argv[2])), indent=2))
