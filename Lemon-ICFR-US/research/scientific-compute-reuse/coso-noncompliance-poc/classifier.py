"""Fail-closed Park et al. (2021) classifier using a trusted SEC extraction registry."""

from datetime import date
import hashlib
import json
from pathlib import Path
import re

CUTOFF = date(2014, 12, 15)
_VERSION_1992 = re.compile(r"Integrated Framework\s*\(\s*1992\s*\)", re.I)
_VERSION_2013 = re.compile(r"Integrated Framework\s*\(\s*2013\s*\)", re.I)
_CIK = re.compile(r"^[0-9]{10}$")
_ACCESSION = re.compile(r"^[0-9]{10}-[0-9]{2}-[0-9]{6}$")
_REGISTRY_PATH = Path(__file__).with_name("trusted-extraction-records-v0.1.json")
_BOUND_FIELDS = (
    "issuer_cik", "accession", "form_type", "period_end", "source_section",
    "speaker", "disclosure_excerpt", "excerpt_sha256",
    "explicit_framework_version", "assertion_polarity", "third_party_quote",
)


def _result(classification, reason):
    return {"classification": classification, "reason": reason}


def _trusted_records():
    payload = json.loads(_REGISTRY_PATH.read_text(encoding="utf-8"))
    return {record["record_id"]: record for record in payload["records"]}


def evaluate_noncompliance(evidence):
    if not isinstance(evidence, dict):
        return _result(None, "INVALID_PROVENANCE_METADATA")

    issuer_cik = evidence.get("issuer_cik")
    accession = evidence.get("accession")
    if (
        not isinstance(issuer_cik, str)
        or not _CIK.fullmatch(issuer_cik)
        or not isinstance(accession, str)
        or not _ACCESSION.fullmatch(accession)
    ):
        return _result(None, "INVALID_PROVENANCE_METADATA")

    period_end = evidence.get("period_end")
    if not isinstance(period_end, str):
        return _result(None, "MISSING_OR_INVALID_PERIOD_END")
    try:
        parsed_period_end = date.fromisoformat(period_end)
    except ValueError:
        return _result(None, "MISSING_OR_INVALID_PERIOD_END")
    if parsed_period_end <= CUTOFF:
        return _result(None, "PERIOD_END_NOT_AFTER_CUTOFF")
    if evidence.get("form_type") not in {"10-K", "10-K/A"}:
        return _result(None, "UNSUPPORTED_FORM_TYPE")

    excerpt = evidence.get("disclosure_excerpt")
    if not isinstance(excerpt, str) or not excerpt.strip():
        return _result(None, "EMPTY_EXCERPT")
    actual_hash = hashlib.sha256(excerpt.encode("utf-8")).hexdigest()
    if evidence.get("excerpt_sha256") != actual_hash:
        return _result(None, "EXCERPT_HASH_MISMATCH")

    record = _trusted_records().get(evidence.get("extraction_record_id"))
    if not record or record.get("verification_status") != "PRIMARY_SOURCE_MANUAL_VERIFIED":
        return _result(None, "UNTRUSTED_EXTRACTION_RECORD")
    if not record.get("source_url", "").startswith("https://www.sec.gov/Archives/"):
        return _result(None, "UNTRUSTED_EXTRACTION_RECORD")
    if any(evidence.get(field) != record.get(field) for field in _BOUND_FIELDS):
        return _result(None, "EVIDENCE_RECORD_MISMATCH")

    has_1992 = bool(_VERSION_1992.search(record["disclosure_excerpt"]))
    has_2013 = bool(_VERSION_2013.search(record["disclosure_excerpt"]))
    if has_1992 == has_2013:
        return _result(None, "AMBIGUOUS_OR_UNVERSIONED_FRAMEWORK")
    derived_version = "1992" if has_1992 else "2013"
    if record["explicit_framework_version"] != derived_version:
        return _result(None, "AMBIGUOUS_OR_UNVERSIONED_FRAMEWORK")
    if record["source_section"] != "MANAGEMENT_ICFR_ASSESSMENT" or record["speaker"] != "MANAGEMENT":
        return _result(None, "UNVERIFIED_SOURCE_SECTION")
    if record["assertion_polarity"] != "ADOPTED":
        return _result(None, "HISTORICAL_BIBLIOGRAPHIC_NEGATED_OR_UNCLEAR_ASSERTION")
    if record["third_party_quote"] is not False:
        return _result(None, "THIRD_PARTY_QUOTE")
    return _result(1 if derived_version == "1992" else 0, None)


def classify_noncompliance(evidence):
    return evaluate_noncompliance(evidence)["classification"]
