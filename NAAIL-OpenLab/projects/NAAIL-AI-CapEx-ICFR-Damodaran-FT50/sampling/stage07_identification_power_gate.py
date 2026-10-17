#!/usr/bin/env python3
"""Stage 07: provenance-preserving identification/power gate, no inferential claims."""
import argparse, csv, json, math, pathlib

def run(manifest_path, pilot_path):
    m=json.loads(pathlib.Path(manifest_path).read_text(encoding="utf-8"))
    with open(pilot_path, encoding="utf-8", newline="") as f:
        rows=list(csv.DictReader(f))
    sum_by=lambda k:sum(int(x[k]) for x in m["by_exposure_FY"])
    checks={
        "historical_nonfinancial_count_reconciles":sum_by("candidate_original_SEC_SIC_source")==m["main_fy2021_2024_nonfinancial_SIC_as_filed_and_source_gate"],
        "formAP_count_reconciles":sum_by("formAP_auditor_match")==m["main_period_and_formAP_single_registered_firm_issuer_years"],
        "CFO_capex_future_count_reconciles":sum_by("gaap_with_future_CFO_formAP")==m["main_CFO_and_cash_PPE_and_following_year_CFO_and_formAP"],
        "CFO_subset_of_auditor_matched":m["main_CFO_and_cash_PPE_and_following_year_CFO_and_formAP"]<=m["main_period_and_formAP_single_registered_firm_issuer_years"],
        "pilot_10_rows":len(rows)==10,
        "pilot_AI_only_spend_unobserved":all(not r["ai_capex_fy2025_usd_m"].strip() for r in rows),
        "pilot_riskCAM_mismatch_unobserved":all(not r["cam_risk_mismatch_score"].strip() for r in rows),
        "pilot_ICFR_opinion_no_variation":len({r["icfr_auditor_opinion"] for r in rows})==1,
        "pilot_only_three_auditor_firms":len({r["auditor_legal_name"] for r in rows})==3,
        "inspection_asof_unfinished":m["source_inspection_report_first_public_release_asof_complete"] is False,
        "historical_CAM_ICFR_unverified":m["CAM_eligibility_and_risk_verified"] is False and m["SOX_ICFR_material_weakness_verified"] is False,
        "causal_N_not_identified":m["full_FT50_causal_N"] is None,
    }
    if not all(checks.values()):
        raise RuntimeError("Source consistency/identification gate failed: "+str(checks))
    mde=lambda n:5.6/math.sqrt(n)
    return {"stage":"07","gate":"NO_GO_PRIMARY_CAUSAL_REGRESSION","source_consistency_checks":checks,
        "passed_checks":sum(checks.values()),"total_checks":len(checks),
        "observed": {"historical_issuer_years_auditor_matched":m["main_period_and_formAP_single_registered_firm_issuer_years"],
            "whole_company_CFO_PPE_futureCFO_issuer_years":m["main_CFO_and_cash_PPE_and_following_year_CFO_and_formAP"],
            "distinct_issuers":m["main_CFO_and_cash_PPE_and_following_year_CFO_unique_CIK"],
            "auditor_firms":m["main_distinct_registered_auditor_firms"],
            "pilot_rows":len(rows),"pilot_AI_only_CapEx_verified":0,
            "pilot_riskCAM_scores_verified":0,"pilot_ICFR_opinion_variation":False},
        "hypothetical_optimistic_standardized_MDE_not_valid_empirical_power":{
            "nominal_9487":round(mde(9487),6),"issuers_3157":round(mde(3157),6),
            "auditor_firms_305":round(mde(305),6),"pilot_10":round(mde(10),6)},
        "regression_executed":False,"causal_sample_N":None,
        "interpretation":"Checks prove primary identification is blocked. MDE values assume balanced independent randomized groups; no observed treatment assignment or ICC."
    }

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",required=True)
    ap.add_argument("--pilot",required=True)
    ap.add_argument("--output")
    a=ap.parse_args()
    result=run(a.manifest,a.pilot)
    payload=json.dumps(result,indent=2,ensure_ascii=False)+"\n"
    if a.output:pathlib.Path(a.output).write_text(payload,encoding="utf-8")
    print(payload)
