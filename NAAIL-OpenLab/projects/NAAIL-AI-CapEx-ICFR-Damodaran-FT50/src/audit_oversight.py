"""Point-in-time PCAOB firm exposure and independent CAM-risk alignment.

Only deterministic primitives for later empirical pipelines. No PCAOB input is
treated as a finding about the specific issuer being studied.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from math import isfinite
from typing import Iterable, Optional


@dataclass(frozen=True)
class PublishedInspection:
    auditor_firm_id: str
    report_id: str
    published_at: datetime
    inspected_audits: int
    audits_with_part_ia_findings: int

    def __post_init__(self) -> None:
        _check_datetime(self.published_at)
        if not self.auditor_firm_id or not self.report_id:
            raise ValueError("auditor_firm_id and report_id are required")
        if self.inspected_audits <= 0:
            raise ValueError("inspected_audits must be positive")
        if not 0 <= self.audits_with_part_ia_findings <= self.inspected_audits:
            raise ValueError("audits_with_part_ia_findings out of range")


def _check_datetime(value: datetime) -> None:
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("timestamp must be timezone-aware")


def published_auditor_exposure(
    auditor_firm_id: str,
    as_of: datetime,
    reports: Iterable[PublishedInspection],
) -> Optional[float]:
    """Most recently *public* inspection report's inspected-audit deficiency share.

    Rate refers solely to audits SELECTED by PCAOB, NOT to all auditor clients.
    Report dates, not inspection fiscal years, determine public availability.
    Missing auditor report = None, never numeric zero.
    """
    _check_datetime(as_of)
    matches = [
        r for r in reports
        if r.auditor_firm_id == auditor_firm_id and r.published_at <= as_of
    ]
    if not matches:
        return None
    latest = max(matches, key=lambda r: (r.published_at, r.report_id))
    return latest.audits_with_part_ia_findings / latest.inspected_audits


def cam_risk_cell(
    independent_account_risk: Optional[float],
    cam_disclosed: Optional[bool],
    *,
    high_risk_cutoff: float,
) -> str:
    """Four diagnostic risk×CAM states, or 'unknown'.

    The risk score MUST exclude CAM text and future PCAOB findings. The cutoff
    must be chosen on training observations. 'High risk/no CAM' is not evidence
    of a breach of auditing standards.
    """
    cutoff = float(high_risk_cutoff)
    if not isfinite(cutoff):
        raise ValueError("high_risk_cutoff must be finite")
    if independent_account_risk is None or cam_disclosed is None:
        return "unknown"
    risk = float(independent_account_risk)
    if not isfinite(risk):
        raise ValueError("independent_account_risk must be finite")
    if not isinstance(cam_disclosed, bool):
        raise TypeError("cam_disclosed must be boolean or None")
    return ("high_risk" if risk >= cutoff else "low_risk") + (
        "_cam" if cam_disclosed else "_no_cam"
    )
