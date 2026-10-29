"""Fail-closed S2/S3 controls. Never infers SEC verification or writes to Drive."""
import csv
import io
import re
from datetime import date, datetime

CIK = re.compile(r"^[0-9]{10}$")
ROSTER_ROW = re.compile(r"^\s*(\d{1,4})\s*\|\s*([^|]+)\|\s*(\d{10})\s*\|")

def parse_roster(text):
    """Anchor to ordinal/ticker/CIK; company names may contain extra pipes."""
    out = []
    for line in text.splitlines():
        match = ROSTER_ROW.match(line)
        if match:
            out.append((int(match[1]), match[2].strip(), match[3]))
    if len({x[0] for x in out}) != len(out) or len({x[2] for x in out}) != len(out):
        raise ValueError("duplicate ordinal or CIK")
    return out

def parse_quoted_csv(text):
    return list(csv.DictReader(io.StringIO(text, newline="")))

def validate_pilot(rows, expected=100):
    errors = []
    if len(rows) != expected:
        errors.append("COUNT_MISMATCH")
    ciks = [str(row.get("CIK10", "")).strip() for row in rows]
    if any(not CIK.fullmatch(c) for c in ciks):
        errors.append("INVALID_CIK10")
    if len(set(ciks)) != len(ciks):
        errors.append("DUPLICATE_CIK10")
    for n, row in enumerate(rows, 1):
        a = str(row.get("CLAUDE_FIRST_FY") or "").strip()
        b = str(row.get("CLAUDE_LAST_FY") or "").strip()
        if bool(a) != bool(b):
            errors.append(f"{n}:ASYMMETRIC_CLAUDE_FY")
        if any(v and (not re.fullmatch(r"\d{4}", v) or not 1900 <= int(v) <= 2100) for v in (a, b)):
            errors.append(f"{n}:INVALID_CLAUDE_FY")
        if a and b and a > b:
            errors.append(f"{n}:REVERSED_CLAUDE_FY")
    return errors

def pit_filing_status(form, fiscal_end, accepted_at, observation_at):
    if form not in {"10-K", "10-K/A", "NT 10-K"}:
        return "WRONG_FORM"
    if not isinstance(fiscal_end, date) or isinstance(fiscal_end, datetime):
        return "UNKNOWN_FISCAL_END"
    if (accepted_at is None or observation_at is None
            or accepted_at.tzinfo is None or observation_at.tzinfo is None):
        return "UNKNOWN_ACCEPTANCE_TIME"
    if accepted_at.date() < fiscal_end:
        return "INCONSISTENT_FY_ACCEPTANCE"
    if accepted_at > observation_at:
        return "NOT_YET_PUBLIC_AS_OF"
    if form == "NT 10-K":
        return "NOTICE_ONLY_NOT_10K"
    if form == "10-K/A":
        return "AMENDMENT_REQUIRES_MATERIALITY_REVIEW"
    return "ELIGIBLE_ORIGINAL_10K_ONLY"

def index_membership_asof(events, observation_at):
    eligible = [e for e in events
                if e["announcement_at"] <= observation_at and e["effective_at"] <= observation_at]
    return max(eligible, key=lambda e: e["effective_at"])["membership"] if eligible else "UNKNOWN"

def validate_write_plan(rows, safety_block=False):
    if safety_block:
        raise PermissionError("SAFETY_BLOCK: STOP ALL WRITES; NO RETRY")
    if not 0 < len(rows) <= 20:
        raise ValueError("write must contain 1..20 rows")
    for row in rows:
        if (not CIK.fullmatch(str(row.get("CIK10", "")))
                or not row.get("destination") or not row.get("provenance")):
            raise ValueError("missing CIK10/destination/provenance")
    return True
