"""Synthetic-only assertions; they do not validate SEC or PCAOB empirical data."""
from datetime import datetime, timezone, timedelta

import pytest

from src.audit_oversight import (
    PublishedInspection, cam_risk_cell, published_auditor_exposure
)


def utc(yr: int, mon: int = 1, day: int = 1) -> datetime:
    return datetime(yr, mon, day, tzinfo=timezone.utc)


def test_future_inspection_not_available_in_past():
    reports = [PublishedInspection("auditor-a", "r1", utc(2025), 20, 10)]
    assert published_auditor_exposure("auditor-a", utc(2024), reports) is None
    assert published_auditor_exposure("auditor-a", utc(2025), reports) == 0.5


def test_latest_public_report_and_firm_are_matched():
    reports = [
        PublishedInspection("auditor-a", "r1", utc(2023), 10, 2),
        PublishedInspection("auditor-a", "r2", utc(2025), 20, 6),
        PublishedInspection("auditor-b", "r3", utc(2025), 5, 5),
    ]
    assert published_auditor_exposure("auditor-a", utc(2024), reports) == 0.2
    assert published_auditor_exposure("auditor-a", utc(2026), reports) == 0.3
    assert published_auditor_exposure("auditor-c", utc(2026), reports) is None


@pytest.mark.parametrize("risk,cam,expected", [
    (0.8, True, "high_risk_cam"),
    (0.8, False, "high_risk_no_cam"),
    (0.2, True, "low_risk_cam"),
    (0.2, False, "low_risk_no_cam"),
    (None, True, "unknown"),
    (0.8, None, "unknown"),
])
def test_four_cam_risk_states(risk, cam, expected):
    assert cam_risk_cell(risk, cam, high_risk_cutoff=0.7) == expected


def test_naive_inspection_timestamp_is_prohibited():
    report = PublishedInspection("auditor-a", "r", utc(2025), 10, 1)
    with pytest.raises(ValueError, match="timezone"):
        published_auditor_exposure("auditor-a", datetime(2025, 1, 1), [report])


def test_invalid_rate_denominator_rejected():
    with pytest.raises(ValueError, match="positive"):
        PublishedInspection("auditor-a", "r", utc(2025), 0, 0)
