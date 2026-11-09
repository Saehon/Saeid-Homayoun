"""Damodaran FT50: fail-closed SEC/PIT gate. No external calls."""
from datetime import date, datetime, timezone
from collections import Counter
import re

def utc(s):
    d = datetime.fromisoformat(s.replace("Z", "+00:00"))
    if d.tzinfo is None: raise ValueError("timezone required")
    return d.astimezone(timezone.utc)

def verify(row):
    issues = []
    cik, acc = str(row.get("cik10","")), str(row.get("accession",""))
    if not re.fullmatch(r"\d{10}",cik): issues.append("CIK10")
    if not re.fullmatch(r"\d{10}-\d{2}-\d{6}",acc): issues.append("accession")
    # Accession prefix identifies the submitting CIK, which can be a filing agent.
    try:
        fy=row["fiscal_year_end"]
        if date.fromisoformat(fy).isoformat()!=fy: raise ValueError()
    except (ValueError,KeyError,TypeError): issues.append("exact FY missing")
    url=row.get("sec_original_url","")
    if not re.fullmatch(r"https://www\.sec\.gov/Archives/edgar/data/\d+/\d{18}/[^?#]+",url): issues.append("SEC original pointer")
    elif acc.replace("-","") not in url: issues.append("SEC accession pointer mismatch")
    elif (not cik.isdigit()) or int(re.search(r"/data/(\d+)/", url).group(1)) != int(cik): issues.append("SEC archive issuer CIK mismatch")
    if not re.fullmatch(r"[a-fA-F0-9]{64}",str(row.get("xbrl_sha256",""))): issues.append("XBRL SHA256")
    for key in ("xbrl_fact","xbrl_context","xbrl_unit","historical_sic","ff_industry_source","damodaran_vintage"):
        if not row.get(key): issues.append("missing " + key)
    for flag in ("sec_original_verified","xbrl_hash_verified","historical_ff_verified","damodaran_vintage_verified","holdout_sealed","falsification_pass"):
        if row.get(flag) is not True: issues.append(flag)
    if row.get("licensing_status")!="verified": issues.append("license")
    try:
        a,p,d=[utc(row[k]) for k in ("sec_acceptance_utc","first_public_release_utc","decision_clock_utc")]
        if p<a and not row.get("pre_filing_release_evidence_url"): issues.append("unsubstantiated pre-filing release")
        if d<max(a,p): issues.append("PIT lookahead")
    except (KeyError,ValueError,AttributeError,TypeError): issues.append("PIT clock")
    if row.get("ai_capex") is not None and not row.get("ai_capex_source_url"): issues.append("AI-specific CapEx evidence")
    return sorted(set(issues))

def batch(rows):
    keys=[(r.get("cik10"),r.get("fiscal_year_end"),r.get("accession")) for r in rows]
    counts=Counter(keys)
    out=[]
    for r,k in zip(rows,keys):
        issues=verify(r)
        if counts[k]>1: issues.append("duplicate key")
        out.append({"key":k,"status":"pending" if issues else "done","issues":issues})
    return out

def retry(attempts,failed=False,new_remedy=False):
    if attempts>=3: return "needs_manual_review"
    return "failed" if failed and not new_remedy else "pending"
