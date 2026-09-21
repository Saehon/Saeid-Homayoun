from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from .schemas import AuditFinding, DeterministicAuditResult

REQUIRED_COLUMNS = {
    "transaction_id", "timestamp", "vendor", "amount", "currency",
    "requester", "approver", "account", "cost_center",
}
SEVERITY_WEIGHT = {"low": 3, "medium": 7, "high": 15, "critical": 25}


def _text(value: Any) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


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
        bad = [int(i) + 2 for i in df.index[df["amount"].isna()].tolist()]
        raise ValueError(f"Non-numeric amount values at CSV rows: {bad}")
    df["parsed_timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)
    return df


def _evidence(idx: int, row: pd.Series) -> str:
    return (
        f"row={idx + 2}; transaction_id={_text(row['transaction_id'])}; "
        f"vendor={_text(row['vendor'])}; amount={row['amount']}; "
        f"timestamp={_text(row['timestamp'])}; requester={_text(row['requester'])}; "
        f"approver={_text(row['approver'])}"
    )


def _add(findings: list[AuditFinding], rule_id: str, severity: str, title: str,
         rows: pd.DataFrame, rationale: str) -> None:
    if rows.empty:
        return
    findings.append(AuditFinding(
        finding_id=f"F-{len(findings)+1:03d}",
        rule_id=rule_id,
        severity=severity,
        title=title,
        transaction_ids=sorted({_text(v) for v in rows["transaction_id"] if _text(v)}),
        evidence=[_evidence(int(i), row) for i, row in rows.iterrows()],
        rationale=rationale,
    ))


def analyze_transactions(csv_path: str | Path) -> DeterministicAuditResult:
    path = Path(csv_path)
    df = load_transactions(path)
    findings: list[AuditFinding] = []

    _add(findings, "DUPLICATE_ID", "high", "Duplicate transaction identifiers",
         df[df["transaction_id"].astype(str).duplicated(keep=False)],
         "Duplicate identifiers may indicate duplicate processing, resubmission, or data-integrity problems and require source-document validation.")

    approver = df["approver"].fillna("").astype(str).str.strip()
    requester = df["requester"].fillna("").astype(str).str.strip()
    _add(findings, "MISSING_APPROVER", "high", "Missing approval evidence",
         df[approver.eq("")],
         "Transactions without an identified approver may not satisfy the expected authorization control.")

    sod = requester.ne("") & approver.ne("") & requester.str.casefold().eq(approver.str.casefold())
    _add(findings, "SOD_CONFLICT", "critical", "Requester and approver are the same person",
         df[sod],
         "The same requester and approver is a segregation-of-duties indicator requiring corroborating workflow evidence.")

    valid_ts = df["parsed_timestamp"].notna()
    _add(findings, "WEEKEND_POSTING", "medium", "Weekend transaction posting",
         df[valid_ts & df["parsed_timestamp"].dt.dayofweek.ge(5)],
         "Weekend activity is not inherently improper but can be a useful contextual anomaly.")
    _add(findings, "OUT_OF_HOURS", "medium", "Out-of-hours transaction posting",
         df[valid_ts & (df["parsed_timestamp"].dt.hour.lt(6) | df["parsed_timestamp"].dt.hour.ge(22))],
         "Posting outside ordinary hours is a contextual anomaly requiring process context.")

    abs_amount = df["amount"].abs()
    median = float(abs_amount.median()) if len(df) else 0.0
    mad = float((abs_amount - median).abs().median()) if len(df) else 0.0
    threshold = median + 6 * mad if mad > 0 else max(median * 5, 10_000.0)
    _add(findings, "ROBUST_AMOUNT_OUTLIER", "high", "Robust amount outlier",
         df[abs_amount.gt(threshold)],
         f"Absolute amount exceeds the illustrative robust threshold of {threshold:,.2f}.")
    _add(findings, "LARGE_ROUND_AMOUNT", "medium", "Large round-value transaction",
         df[abs_amount.ge(10_000) & abs_amount.mod(1_000).abs().lt(1e-9)],
         "Large round amounts are screening indicators commonly used for follow-up, not proof of error or misconduct.")

    return DeterministicAuditResult(
        source_file=str(path),
        row_count=int(len(df)),
        total_absolute_value=float(abs_amount.sum()),
        risk_score=min(100, sum(SEVERITY_WEIGHT[f.severity] for f in findings)),
        findings=findings,
        limitations=[
            "Rule-based flags are risk indicators, not findings of fraud or control failure.",
            "The prototype does not inspect contracts, invoices, bank evidence, user-access logs, or ERP workflow history.",
            "Thresholds are illustrative and require entity-specific calibration to materiality and process design.",
            "All consequential conclusions require qualified human review and corroborating evidence.",
        ],
    )
