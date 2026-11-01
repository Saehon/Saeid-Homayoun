"""Reproduce descriptive SEC CAM–ICFR–PCAOB pilot diagnostics; no causal tests.
Usage: python analysis/run_fy2025_cam_pcaob_feasibility.py data/public_FY2025_audit_panel.csv
"""
import argparse
import json
from pathlib import Path

import pandas as pd
from scipy.stats import fisher_exact


def analyze(path):
    d = pd.read_csv(path)
    needed = {"ticker", "economic_role", "cam_topic_count", "cam_inventory_topic",
              "cam_uncertain_tax_topic", "auditor_legal_name", "icfr_auditor_opinion",
              "pcaob_publication_date", "auditor_report_date",
              "pcaob_prior_to_auditor_report", "pcaob_selected_audit_deficiency_share",
              "ai_capex_fy2025_usd_m", "cam_risk_mismatch_score"}
    if needed.difference(d.columns):
        raise ValueError(f"Missing fields: {needed.difference(d.columns)}")
    if len(d) != 10 or d.ticker.nunique() != 10:
        raise ValueError("Expected ten distinct issuers")
    if sorted(d.economic_role.value_counts().tolist()) != [5, 5]:
        raise ValueError("Expected five builders and five suppliers")
    release = pd.to_datetime(d.pcaob_publication_date)
    report = pd.to_datetime(d.auditor_report_date)
    known = release <= report
    if not (known.astype(int).to_numpy() == d.pcaob_prior_to_auditor_report.to_numpy()).all():
        raise ValueError("PCAOB publication date leakage detected")
    if not d.loc[~known, 'pcaob_selected_audit_deficiency_share'].isna().all():
        raise ValueError("Future inspection treated as available")
    def test(col):
        tab = pd.crosstab(d.economic_role,d[col]).reindex(
            index=["Builder","Supplier"],columns=[1,0],fill_value=0)
        return {"builder_yes":int(tab.iloc[0,0]),
                "supplier_yes":int(tab.iloc[1,0]),
                "fisher_p_two_sided":float(fisher_exact(tab.values).pvalue)}
    n_unique = d.loc[known].groupby("auditor_legal_name")["pcaob_selected_audit_deficiency_share"].nunique()
    if not n_unique.eq(1).all():
        raise ValueError("Inconsistent PCAOB exposure within auditor")
    return {
        "n_issuers":len(d), "n_cam_topics":int(d.cam_topic_count.sum()),
        "cam_by_role":d.groupby("economic_role").cam_topic_count.sum().to_dict(),
        "inventory_cam":test("cam_inventory_topic"),
        "uncertain_tax_cam":test("cam_uncertain_tax_topic"),
        "n_prior_public_pcaob":int(known.sum()),
        "n_auditors":int(d.auditor_legal_name.nunique()),
        "n_effective_icfr":int((d.icfr_auditor_opinion=="effective_unqualified").sum()),
        "n_verified_ai_capex_values":int(d.ai_capex_fy2025_usd_m.notna().sum()),
        "n_valid_risk_cam_mismatch_scores":int(d.cam_risk_mismatch_score.notna().sum()),
        "causal_oversight_model_estimable":False,
        "disclaimer":"This selected ten-firm pilot is descriptive. PCAOB Part I.A rate is auditor-level selected-audit exposure; it is NOT evidence of a deficiency in the issuer's audit. Missing AI-specific CapEx, zero ICFR MW variation, and three audit-firm clusters preclude the planned FT50 interaction model."
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("public_audit_panel_csv",type=Path)
    print(json.dumps(analyze(parser.parse_args().public_audit_panel_csv),indent=2))
