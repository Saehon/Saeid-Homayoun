"""Independent CAM–ICFR risk matrix calculations; no fitted empirical results.

Required columns: firm, account, fiscal_year, industry, risk_score,
risk_independent, decision_date, available_date, eligible,
eligible_set_complete. Optional columns: icfr_state (E/I/U),
cam_positive_confirmed, report_applicable, period_verified,
cam_capture_complete, mapping_complete. Evidence flags accept True/False or
0/1, with missing values meaning unknown; strings are deliberately rejected.

Each row represents one firm/account/year. The caller must supply an exhaustive
eligible-account roster before setting eligible_set_complete=True. A CSV alone
cannot prove that absent accounts are ineligible. Independent risk scores and
confirmed positive CAM mappings are upstream evidence, not inferred here.

Peer thresholds use eligible, independently measured, temporally admissible
scores within industry/account/year, including the focal firm. Every threshold
is evaluated as of the focal decision date. Linear 70th percentiles, at least
20 distinct firms, and variation are required. Equality belongs to H. Ties are
not broken. This preserves temporal validity when decision dates differ.

The original 12 cell IDs remain A1/B1/A2/B2/A3/B3/C1/D1/C2/D2/C3/D3.
The other 15 states use U1..U6 and CAMU_<ICFR>_<risk> IDs. Unknown evidence
never becomes a zero. Fixtures in the companion tests are synthetic.
"""

from __future__ import annotations

from typing import Any
import math

import numpy as np
import pandas as pd


REQUIRED_COLUMNS = (
    "firm", "account", "fiscal_year", "industry", "risk_score",
    "risk_independent", "decision_date", "available_date", "eligible",
    "eligible_set_complete",
)
CAM_NEGATIVE_GATES = (
    "eligible", "report_applicable", "period_verified",
    "cam_capture_complete", "mapping_complete",
)
_ORIGINAL_IDS = {
    ("H", "E", "1"): "A1", ("H", "E", "0"): "B1",
    ("H", "I", "1"): "A2", ("H", "I", "0"): "B2",
    ("H", "U", "1"): "A3", ("H", "U", "0"): "B3",
    ("L", "E", "1"): "C1", ("L", "E", "0"): "D1",
    ("L", "I", "1"): "C2", ("L", "I", "0"): "D2",
    ("L", "U", "1"): "C3", ("L", "U", "0"): "D3",
}
_RISK_UNKNOWN_IDS = {
    ("E", "1"): "U1", ("E", "0"): "U2",
    ("I", "1"): "U3", ("I", "0"): "U4",
    ("U", "1"): "U5", ("U", "0"): "U6",
}


def state_id(risk: str, icfr: str, cam: str | int) -> str:
    """Return a distinct, stable ID for each of the 27 possible states."""
    cam = str(cam)
    if risk not in {"H", "L", "U"} or icfr not in {"E", "I", "U"} or cam not in {"1", "0", "U"}:
        raise ValueError("States must be risk H/L/U, ICFR E/I/U, CAM 1/0/U")
    if cam == "U":
        return f"CAMU_{icfr}_{risk}"
    if risk == "U":
        return _RISK_UNKNOWN_IDS[icfr, cam]
    return _ORIGINAL_IDS[risk, icfr, cam]


def _evidence_flag(value: Any, column: str) -> bool | None:
    if pd.isna(value):
        return None
    if isinstance(value, (bool, np.bool_)):
        return bool(value)
    if isinstance(value, (int, float, np.integer, np.floating)) and value in (0, 1):
        return bool(value)
    raise ValueError(f"{column} must contain boolean/0/1/missing evidence flags")


def evaluate_risk_matrix(
    data: pd.DataFrame, *, quantile: float = 0.70, min_peer_firms: int = 20,
) -> pd.DataFrame:
    """Return validated row-level states, competition measures and evidence flags.

    Cmax=max(other eligible-account risks), Crank=count(other risks > own),
    Ctail=sum(max(other risk - that other account's peer threshold, 0)),
    D=own-Cmax. Complete rosters must contain >=2 eligible accounts and every
    risk must be known, independent and available by the focal decision date.
    Ctail additionally requires all other-account peer thresholds. Cmax, Crank
    and D do not require those thresholds. Unknown competition remains NaN.

    cam_model_eligible records all negative-proof gates independently of CAM
    status. A confirmed positive mapping yields CAM=1 even when those gates
    fail; it does not make the record model-eligible. ICFR is never inferred.
    """
    missing = set(REQUIRED_COLUMNS) - set(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if not 0 < quantile < 1:
        raise ValueError("quantile must be strictly between zero and one")
    if isinstance(min_peer_firms, bool) or not isinstance(min_peer_firms, int) or min_peer_firms < 20:
        raise ValueError("min_peer_firms must be an integer >=20")
    d = data.copy().reset_index(drop=True)
    if d.empty:
        raise ValueError("At least one input row is required")
    for column in ("firm", "account", "fiscal_year"):
        if d[column].isna().any() or d[column].astype(str).str.strip().eq("").any():
            raise ValueError(f"Missing grain identifier: {column}")
    if d.duplicated(["firm", "account", "fiscal_year"]).any():
        raise ValueError("Duplicate firm/account/fiscal_year grain")

    flag_columns = set(CAM_NEGATIVE_GATES) | {"risk_independent", "eligible_set_complete", "cam_positive_confirmed"}
    flags: dict[str, list[bool | None]] = {}
    for column in flag_columns:
        values = d[column] if column in d else pd.Series([None] * len(d))
        flags[column] = [_evidence_flag(value, column) for value in values]

    scores = pd.to_numeric(d.risk_score, errors="coerce")
    invalid_numeric = d.risk_score.notna() & scores.isna()
    if invalid_numeric.any():
        raise ValueError("Non-numeric risk_score; use a missing value for unknown risk")
    if d.risk_score.map(lambda v: isinstance(v, (bool, np.bool_))).any():
        raise ValueError("Boolean risk_score is not a quantitative risk measure")
    finite = scores.notna() & np.isfinite(scores)
    decisions = pd.to_datetime(d.decision_date, errors="coerce", utc=True)
    available = pd.to_datetime(d.available_date, errors="coerce", utc=True)
    date_unknown = decisions.isna() | available.isna()
    temporal_violation = (~date_unknown) & (available > decisions)
    base_valid = np.array([
        flags["eligible"][i] is True and flags["risk_independent"][i] is True
        and bool(finite.iloc[i]) and not bool(date_unknown.iloc[i])
        and not bool(temporal_violation.iloc[i])
        for i in range(len(d))
    ], dtype=bool)
    d["risk_score_missing"] = ~finite
    d["risk_temporal_unknown"] = date_unknown
    d["risk_temporal_violation"] = temporal_violation
    d["risk_independent_confirmed"] = [v is True for v in flags["risk_independent"]]
    d["risk_independence_unknown"] = [v is None for v in flags["risk_independent"]]
    d["risk_eligibility_unknown"] = [v is None for v in flags["eligible"]]
    d["risk_measure_admissible"] = base_valid

    peers: dict[tuple[Any, Any, Any], list[int]] = {}
    roster: dict[tuple[Any, Any], list[int]] = {}
    group_keys: list[tuple[Any, Any, Any] | None] = []
    for i, row in d.iterrows():
        industry = row.industry
        group = None if pd.isna(industry) or str(industry).strip() == "" else (industry, row.account, row.fiscal_year)
        group_keys.append(group)
        if group is not None:
            peers.setdefault(group, []).append(i)
        roster.setdefault((row.firm, row.fiscal_year), []).append(i)

    threshold_cache: dict[tuple[Any, ...], tuple[float, int, bool, bool]] = {}

    def threshold(i: int, cutoff: pd.Timestamp) -> tuple[float, int, bool, bool]:
        group = group_keys[i]
        if group is None or pd.isna(cutoff):
            return math.nan, 0, False, False
        key = (*group, cutoff)
        if key not in threshold_cache:
            positions = [j for j in peers[group] if base_valid[j] and available.iloc[j] <= cutoff]
            count = int(d.iloc[positions].firm.nunique())
            values = scores.iloc[positions]
            constant = count > 0 and values.nunique() <= 1
            insufficient = count < min_peer_firms
            value = math.nan if insufficient or constant else float(values.quantile(quantile, interpolation="linear"))
            threshold_cache[key] = value, count, insufficient, constant
        return threshold_cache[key]

    thresholds = [threshold(i, decisions.iloc[i]) for i in range(len(d))]
    d["peer_threshold"] = [t[0] for t in thresholds]
    d["peer_distinct_firms"] = [t[1] for t in thresholds]
    d["peer_insufficient"] = [t[2] for t in thresholds]
    d["peer_no_variation"] = [t[3] for t in thresholds]
    d["peer_group_missing"] = [g is None for g in group_keys]
    d["risk_model_eligible"] = base_valid & d.peer_threshold.notna().to_numpy()
    d["risk_state"] = [
        "U" if not d.risk_model_eligible.iloc[i]
        else "H" if scores.iloc[i] >= d.peer_threshold.iloc[i] else "L"
        for i in range(len(d))
    ]

    competition: list[dict[str, Any]] = []
    for i, row in d.iterrows():
        all_positions = roster[row.firm, row.fiscal_year]
        eligible_positions = [j for j in all_positions if flags["eligible"][j] is True]
        # An unknown eligibility flag can hide an eligible competitor.
        eligibility_known = all(flags["eligible"][j] is not None for j in all_positions)
        complete = eligibility_known and all(flags["eligible_set_complete"][j] is True for j in all_positions)
        cutoff = decisions.iloc[i]
        all_known = bool(eligible_positions) and not pd.isna(cutoff) and all(base_valid[j] and available.iloc[j] <= cutoff for j in eligible_positions)
        valid = complete and len(eligible_positions) >= 2 and i in eligible_positions and all_known
        result = {"competitor_set_complete": complete, "eligible_account_count": len(eligible_positions),
                  "competitor_risks_all_known": all_known, "competition_score_eligible": valid,
                  "competition_tail_eligible": False, "Cmax": math.nan, "Crank": math.nan,
                  "Ctail": math.nan, "D": math.nan}
        if valid:
            others = [j for j in eligible_positions if j != i]
            maximum = float(scores.iloc[others].max())
            result.update(Cmax=maximum, Crank=int((scores.iloc[others] > scores.iloc[i]).sum()), D=float(scores.iloc[i] - maximum))
            other_thresholds = [threshold(j, cutoff)[0] for j in others]
            if all(math.isfinite(t) for t in other_thresholds):
                result["Ctail"] = float(sum(max(float(scores.iloc[j]) - t, 0.0) for j, t in zip(others, other_thresholds)))
                result["competition_tail_eligible"] = True
        competition.append(result)
    for column in ("competitor_set_complete", "eligible_account_count", "competitor_risks_all_known", "competition_score_eligible", "competition_tail_eligible", "Cmax", "Crank", "Ctail", "D"):
        d[column] = [result[column] for result in competition]

    icfr_values = d.icfr_state if "icfr_state" in d else pd.Series(["U"] * len(d))
    icfr = ["U" if pd.isna(v) or str(v).strip() == "" else str(v).strip().upper() for v in icfr_values]
    if any(v not in {"E", "I", "U"} for v in icfr):
        raise ValueError("icfr_state must be E, I or U")
    d["icfr_state"] = icfr
    proof_complete = [all(flags[column][i] is True for column in CAM_NEGATIVE_GATES) for i in range(len(d))]
    d["cam_model_eligible"] = proof_complete
    d["cam_positive_confirmed"] = [v is True for v in flags["cam_positive_confirmed"]]
    d["cam_state"] = ["1" if d.cam_positive_confirmed.iloc[i] else "0" if proof_complete[i] else "U" for i in range(len(d))]
    d["cam_negative_proven"] = d.cam_state.eq("0")
    d["joint_model_eligible"] = d.risk_model_eligible & d.cam_model_eligible & d.icfr_state.ne("U")
    d["state_id"] = [state_id(r, i, c) for r, i, c in zip(d.risk_state, d.icfr_state, d.cam_state)]
    d["state_key"] = d.risk_state + "|" + d.icfr_state + "|" + d.cam_state
    d.attrs.update(quantile=quantile, quantile_interpolation="linear", min_peer_firms=min_peer_firms,
                   peer_group=["industry", "account", "fiscal_year"], threshold_cutoff="decision_date",
                   peer_includes_focal=True, evidence_type="independent inputs; no fitted results")
    return d
