from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import pandas as pd

from .config import AuditConfig, DEFAULT_CONFIG
from .schemas import AuditFinding, DeterministicAuditResult, RiskDomain


REQUIRED_COLUMNS = {
    "transaction_id",
    "timestamp",
    "vendor",
    "amount",
    "currency",
    "requester",
    "approver",
    "account",
    "cost_center",
}

SEVERITY_WEIGHT = {"low": 3, "medium": 7, "high": 15, "critical": 25}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_text(value: Any) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


def _evidence(row_index: int, row: pd.Series) -> str:
    return (
        f"row={row_index + 2}; transaction_id={_safe_text(row['transaction_id'])}; "
        f"vendor={_safe_text(row['vendor'])}; amount={row['amount']}; "
        f"currency={_safe_text(row['currency'])}; timestamp={_safe_text(row['timestamp'])}; "
        f"requester={_safe_text(row['requester'])}; approver={_safe_text(row['approver'])}; "
        f"account={_safe_text(row['account'])}; cost_center={_safe_text(row['cost_center'])}"
    )


def load_transactions(csv_path: str | Path) -> pd.DataFrame:
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Transaction file not found: {path}")

    df = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    df = df.copy()
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    if df["amount"].isna().any():
        bad_rows = [int(i) + 2 for i in df.index[df["amount"].isna()].tolist()]
        raise ValueError(f"Non-numeric amount values at CSV rows: {bad_rows}")

    df["parsed_timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)
    return df


def _add_finding(
    findings: list[AuditFinding],
    rule_id: str,
    severity: str,
    title: str,
    rows: pd.DataFrame,
    rationale: str,
    domains: list[RiskDomain],
    control_objectives: list[str],
) -> None:
    if rows.empty:
        return
    evidence = [_evidence(int(idx), row) for idx, row in rows.iterrows()]
    tx_ids = sorted({_safe_text(v) for v in rows["transaction_id"].tolist() if _safe_text(v)})
    findings.append(
        AuditFinding(
            finding_id=f"F-{len(findings) + 1:03d}",
            rule_id=rule_id,
            severity=severity,
            title=title,
            transaction_ids=tx_ids,
            evidence=evidence,
            rationale=rationale,
            domains=domains,
            control_objectives=control_objectives,
        )
    )


def analyze_transactions(
    csv_path: str | Path,
    config: AuditConfig = DEFAULT_CONFIG,
) -> DeterministicAuditResult:
    """Run transparent, deterministic audit tests over a transaction population."""
    path = Path(csv_path)
    df = load_transactions(path)
    findings: list[AuditFinding] = []

    duplicate_mask = df["transaction_id"].astype(str).duplicated(keep=False)
    _add_finding(
        findings,
        "DUPLICATE_ID",
        "high",
        "Duplicate transaction identifiers",
        df[duplicate_mask],
        "Duplicate transaction identifiers can indicate duplicate processing, resubmission, or data-integrity problems and require source-document validation.",
        ["finance_controls", "forensic", "procurement_ap", "icfr"],
        ["transaction uniqueness", "completeness", "data integrity"],
    )

    approver = df["approver"].fillna("").astype(str).str.strip()
    requester = df["requester"].fillna("").astype(str).str.strip()

    _add_finding(
        findings,
        "MISSING_APPROVER",
        "high",
        "Missing approval evidence",
        df[approver.eq("")],
        "Transactions without an identified approver may not satisfy the expected authorization control.",
        ["finance_controls", "procurement_ap", "icfr", "operations_risk"],
        ["authorization", "management approval", "accountability"],
    )

    sod_mask = requester.ne("") & approver.ne("") & requester.str.casefold().eq(approver.str.casefold())
    _add_finding(
        findings,
        "SOD_CONFLICT",
        "critical",
        "Requester and approver are the same person",
        df[sod_mask],
        "The same requester and approver indicates a segregation-of-duties conflict that can enable control circumvention.",
        ["finance_controls", "forensic", "procurement_ap", "icfr", "operations_risk"],
        ["segregation of duties", "authorization", "fraud-risk mitigation"],
    )

    invalid_timestamp_mask = df["parsed_timestamp"].isna()
    _add_finding(
        findings,
        "INVALID_TIMESTAMP",
        "medium",
        "Invalid or unparseable transaction timestamp",
        df[invalid_timestamp_mask],
        "Unparseable timestamps weaken chronology, monitoring, cutoff testing, and data-lineage reliability.",
        ["ai_data_governance", "finance_controls", "icfr"],
        ["data quality", "lineage", "cutoff"],
    )

    valid_ts = df["parsed_timestamp"].notna()
    weekend_mask = valid_ts & df["parsed_timestamp"].dt.dayofweek.ge(5)
    _add_finding(
        findings,
        "WEEKEND_POSTING",
        "medium",
        "Weekend transaction posting",
        df[weekend_mask],
        "Weekend activity is not inherently improper, but it can be a useful contextual anomaly for follow-up.",
        ["forensic", "operations_risk", "finance_controls"],
        ["monitoring", "transaction legitimacy"],
    )

    out_of_hours_mask = valid_ts & (
        df["parsed_timestamp"].dt.hour.lt(config.working_hour_start)
        | df["parsed_timestamp"].dt.hour.ge(config.working_hour_end)
    )
    _add_finding(
        findings,
        "OUT_OF_HOURS",
        "medium",
        "Out-of-hours transaction posting",
        df[out_of_hours_mask],
        "Posting outside ordinary working hours is a contextual anomaly and should be corroborated with business-process evidence.",
        ["forensic", "operations_risk", "finance_controls"],
        ["monitoring", "transaction legitimacy"],
    )

    abs_amount = df["amount"].abs()
    median = float(abs_amount.median()) if len(df) else 0.0
    mad = float((abs_amount - median).abs().median()) if len(df) else 0.0
    if mad > 0:
        threshold = median + config.mad_multiplier * mad
    else:
        threshold = max(median * 5, config.approval_threshold)

    high_amount_mask = abs_amount.gt(threshold)
    _add_finding(
        findings,
        "ROBUST_AMOUNT_OUTLIER",
        "high",
        "Robust amount outlier",
        df[high_amount_mask],
        f"Absolute transaction amount exceeds the robust threshold of {threshold:,.2f}, based on median plus {config.mad_multiplier:g} median absolute deviations.",
        ["forensic", "treasury", "fpna", "finance_controls"],
        ["exception monitoring", "liquidity oversight", "budget variance review"],
    )

    round_amount_mask = abs_amount.ge(config.large_round_threshold) & (
        abs_amount.mod(1_000).abs().lt(1e-9)
    )
    _add_finding(
        findings,
        "LARGE_ROUND_AMOUNT",
        "medium",
        "Large round-value transaction",
        df[round_amount_mask],
        "Large round-value transactions can be legitimate but are commonly included in journal-entry and fraud-risk screening.",
        ["forensic", "treasury", "finance_controls"],
        ["journal-entry monitoring", "transaction legitimacy"],
    )

    blank_account = df["account"].fillna("").astype(str).str.strip().eq("")
    blank_cost_center = df["cost_center"].fillna("").astype(str).str.strip().eq("")
    _add_finding(
        findings,
        "MISSING_ACCOUNTING_DIMENSION",
        "high",
        "Missing account or cost-center coding",
        df[blank_account | blank_cost_center],
        "Missing accounting dimensions can impair classification, financial reporting, budget attribution, and downstream analytics.",
        ["finance_controls", "fpna", "icfr", "ai_data_governance"],
        ["classification", "completeness", "management reporting", "data quality"],
    )

    negative_amount_mask = df["amount"].lt(0)
    _add_finding(
        findings,
        "NEGATIVE_AMOUNT",
        "medium",
        "Negative-value transaction",
        df[negative_amount_mask],
        "Negative values may represent credits or reversals but require transaction-type and source-document context before interpretation.",
        ["revenue", "procurement_ap", "treasury", "forensic"],
        ["validity", "cutoff", "cash-flow classification"],
    )

    if valid_ts.any():
        transaction_day = df["parsed_timestamp"].dt.floor("D")
        combo = pd.DataFrame(
            {
                "vendor": df["vendor"].fillna("").astype(str).str.casefold(),
                "amount": df["amount"],
                "day": transaction_day,
            }
        )
        duplicate_vendor_amount_day = combo.duplicated(
            subset=["vendor", "amount", "day"],
            keep=False,
        ) & valid_ts
    else:
        duplicate_vendor_amount_day = pd.Series(False, index=df.index)

    _add_finding(
        findings,
        "DUPLICATE_VENDOR_AMOUNT_DAY",
        "high",
        "Repeated vendor/amount on the same day",
        df[duplicate_vendor_amount_day],
        "Repeated same-vendor, same-amount transactions on the same day can indicate duplicate processing and should be reconciled to invoices and payment records.",
        ["procurement_ap", "forensic", "treasury", "finance_controls"],
        ["duplicate-payment prevention", "validity", "cash disbursement control"],
    )

    high_value_missing_approval = abs_amount.ge(config.approval_threshold) & approver.eq("")
    _add_finding(
        findings,
        "HIGH_VALUE_NO_APPROVAL",
        "critical",
        "High-value transaction lacks approval evidence",
        df[high_value_missing_approval],
        f"Transactions at or above {config.approval_threshold:,.2f} without an identified approver represent a heightened authorization and control-risk combination.",
        ["finance_controls", "procurement_ap", "treasury", "icfr", "forensic"],
        ["authorization", "material transaction oversight", "fraud-risk mitigation"],
    )

    risk_score = min(100, sum(SEVERITY_WEIGHT[f.severity] for f in findings))
    limitations = [
        "Rule-based flags are risk indicators, not findings of fraud or control failure.",
        "The prototype does not inspect invoices, contracts, bank evidence, user-access logs, tax records, payroll records, forecasts, or ERP workflow history unless separately supplied.",
        "Thresholds are configurable research defaults and should be calibrated to entity materiality, process design, and transaction population.",
        "Domain labels route evidence to specialist agents; they do not establish that a domain-specific control failed.",
        "All material conclusions require qualified human review and corroborating evidence.",
    ]

    return DeterministicAuditResult(
        source_file=str(path),
        source_sha256=_sha256(path),
        row_count=int(len(df)),
        total_absolute_value=float(abs_amount.sum()),
        risk_score=risk_score,
        findings=findings,
        limitations=limitations,
    )


def result_as_json(csv_path: str | Path) -> str:
    return json.dumps(analyze_transactions(csv_path).model_dump(), indent=2)
