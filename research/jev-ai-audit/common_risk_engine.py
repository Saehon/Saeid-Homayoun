"""DARWIN-JEV common ex-ante accounting risk feature engine.

Author: Dr. Saeid Homayoun | 2026-10-16
FT50-supported FEATURE definitions only. No fitted model, proprietary Jev weights,
calibration, empirical effect, or audit-quality verdict is supplied here.

A row's evidence_available_date is the *latest* public availability date among
inputs actually used. A production build must validate field-level source dates.
"""
from datetime import date
from math import isfinite, log1p
from typing import Mapping

ICFR = frozenset({"effective", "ineffective", "unknown"})
STANDARDS = frozenset({"US_GAAP", "IFRS", "other"})
ACCOUNT_DOMAINS = frozenset({"revenue", "inventory", "goodwill", "tax", "other"})
INPUT_FIELDS = (
    "assets", "assets_prior", "net_income", "operating_cash_flow",
    "receivables", "receivables_prior", "revenue", "revenue_prior",
    "inventory", "inventory_prior", "goodwill", "liabilities",
    "segment_count",
)
FEATURE_SOURCES = {
    "accrual_intensity": "Dechow et al. (2011), CAR; accounting accrual risk proxy",
    "receivable_sales_gap": "Dechow et al. (2011), CAR; revenue/receivables indicators",
    "inventory_sales_gap": "Dechow et al. (2011), CAR; inventory indicators",
    "goodwill_asset_share": "Accounting estimate exposure; not a copied journal coefficient",
    "leverage": "Financial structure control; not a copied journal coefficient",
    "revenue_growth": "Financial reporting growth pressure proxy",
    "segment_log_count": "Complexity proxy requiring independently verified segment data",
    "loss_indicator": "Financial distress/control proxy",
}

def _day(value, field):
    try:
        return date.fromisoformat(str(value))
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be ISO YYYY-MM-DD") from exc

def _num(row, name):
    value = row.get(name)
    if value is None or value == "":
        return None
    try:
        val = float(value)
    except (ValueError, TypeError) as exc:
        raise ValueError(f"{name} must be numeric or missing") from exc
    if not isfinite(val):
        raise ValueError(f"{name} must be finite")
    return val

def _ratio(numer, denom):
    if numer is None or denom is None or denom <= 0:
        return None
    return numer / denom

def _gap(curr_num, curr_den, prev_num, prev_den):
    a = _ratio(curr_num, curr_den)
    b = _ratio(prev_num, prev_den)
    return a - b if a is not None and b is not None else None

def validate_metadata(row: Mapping):
    required = (
        "firm_id", "fiscal_year", "industry", "domain", "accounting_standard",
        "cutoff_date", "evidence_available_date", "icfr_status",
    )
    for name in required:
        if row.get(name) in (None, ""):
            raise ValueError(f"Missing required metadata: {name}")
    if str(row["icfr_status"]).lower() not in ICFR:
        raise ValueError("ICFR must be effective/ineffective/unknown; do not infer from silence")
    if row["accounting_standard"] not in STANDARDS:
        raise ValueError("Unknown accounting standard; US revenue uses ASC 606, IFRS uses IFRS 15")
    if row["domain"] not in ACCOUNT_DOMAINS:
        raise ValueError("Unsupported accounting domain")
    try:
        fy = int(row["fiscal_year"])
    except (TypeError, ValueError) as exc:
        raise ValueError("Invalid fiscal year") from exc
    if fy < 1900 or fy > 2100:
        raise ValueError("Fiscal year outside supported interval")
    cutoff = _day(row["cutoff_date"], "cutoff_date")
    evidence = _day(row["evidence_available_date"], "evidence_available_date")
    if evidence > cutoff:
        raise ValueError("Leakage: evidence not publicly available by prediction cutoff")
    if row.get("outcome_observed_date"):
        outcome = _day(row["outcome_observed_date"], "outcome_observed_date")
        if outcome <= cutoff:
            raise ValueError("Outcome must be observed strictly AFTER risk prediction cutoff")
    return cutoff

def build_features(row: Mapping):
    """Return only ex-ante accounting predictors; NEVER ingest CAM/ICFR/PCAOB labels.

    Requires point-in-time, provenance-verified raw inputs. Missing or zero-denominator
    ratios are None, never silently imputed to zero. Any actual risk probability
    must be fitted, calibrated and evaluated separately on chronological splits.
    """
    validate_metadata(row)
    v = {key: _num(row, key) for key in INPUT_FIELDS}
    assets, prev = v["assets"], v["assets_prior"]
    asset_avg = (assets + prev) / 2 if assets is not None and prev is not None and assets > 0 and prev > 0 else None
    ni, ocf = v["net_income"], v["operating_cash_flow"]
    accruals = ni - ocf if ni is not None and ocf is not None else None
    seg = v["segment_count"]
    if seg is not None and (seg < 0 or seg != int(seg)):
        raise ValueError("segment_count must be a nonnegative integer")
    return {
        "accrual_intensity": _ratio(accruals, asset_avg),
        "receivable_sales_gap": _gap(v["receivables"], v["revenue"], v["receivables_prior"], v["revenue_prior"]),
        "inventory_sales_gap": _gap(v["inventory"], v["revenue"], v["inventory_prior"], v["revenue_prior"]),
        "goodwill_asset_share": _ratio(v["goodwill"], assets),
        "leverage": _ratio(v["liabilities"], assets),
        "revenue_growth": ((v["revenue"] / v["revenue_prior"]) - 1) if v["revenue"] is not None and v["revenue_prior"] is not None and v["revenue_prior"] > 0 else None,
        "segment_log_count": log1p(seg) if seg is not None else None,
        "loss_indicator": int(ni < 0) if ni is not None else None,
    }

def classification_scope(row):
    """Never conflate CAM selection or ICFR labels with an ex-ante risk probability."""
    validate_metadata(row)
    return {
        "firm_id": str(row["firm_id"]),
        "fiscal_year": int(row["fiscal_year"]),
        "industry": str(row["industry"]),
        "domain": row["domain"],
        "icfr_status": row["icfr_status"],
        "accounting_standard": row["accounting_standard"],
        "revenue_standard": ("ASC 606" if row["domain"] == "revenue" and row["accounting_standard"] == "US_GAAP"
                             else "IFRS 15" if row["domain"] == "revenue" and row["accounting_standard"] == "IFRS"
                             else "not_applicable"),
        "risk_probability": None,
        "risk_model_status": "UNTRAINED",
    }

if __name__ == "__main__":
    print("FT50-informed common risk feature definitions loaded; no fitted risk scores.")
