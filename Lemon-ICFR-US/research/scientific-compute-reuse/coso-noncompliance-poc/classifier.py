"""Fail-closed Park et al. (2021) COSO noncompliance classifier."""

from datetime import date
import hashlib
import re

CUTOFF = date(2014, 12, 15)
_VERSION_1992 = re.compile(r"Integrated Framework\s*\(\s*1992\s*\)", re.I)
_VERSION_2013 = re.compile(r"Integrated Framework\s*\(\s*2013\s*\)", re.I)
_CIK = re.compile(r"^[0-9]{10}$")
_ACCESSION = re.compile(r"^[0-9]{10}-[0-9]{2}-[0-9]{6}$")


def _result(classification, reason):
    return {"classification": classification, "reason": reason}


def evaluate_noncompliance(evidence):
    """Evaluate a bounded management-ICFR evidence object.

    The function returns both the classification and the fail-closed reason.
    A classification is emitted only when every applicability, provenance,
    scope, polarity, and version check passes.
    """
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
    if evidence.get("source_section") != "MANAGEMENT_ICFR_ASSESSMENT":
        return _result(None, "UNVERIFIED_SOURCE_SECTION")
    if evidence.get("speaker") != "MANAGEMENT":
        return _result(None, "NON_MANAGEMENT_SPEAKER")

    excerpt = evidence.get("disclosure_excerpt")
    if not isinstance(excerpt, str) or not excerpt.strip():
        return _result(None, "EMPTY_EXCERPT")
    expected_hash = evidence.get("excerpt_sha256")
    actual_hash = hashlib.sha256(excerpt.encode("utf-8")).hexdigest()
    if not isinstance(expected_hash, str) or expected_hash != actual_hash:
        return _result(None, "EXCERPT_HASH_MISMATCH")

    has_1992 = bool(_VERSION_1992.search(excerpt))
    has_2013 = bool(_VERSION_2013.search(excerpt))
    annotated_version = evidence.get("explicit_framework_version")
    if has_1992 == has_2013 or annotated_version not in {"1992", "2013"}:
        return _result(None, "AMBIGUOUS_OR_UNVERSIONED_FRAMEWORK")
    derived_version = "1992" if has_1992 else "2013"
    if annotated_version != derived_version:
        return _result(None, "AMBIGUOUS_OR_UNVERSIONED_FRAMEWORK")

    if evidence.get("assertion_polarity") != "ADOPTED":
        return _result(
            None,
            "HISTORICAL_BIBLIOGRAPHIC_NEGATED_OR_UNCLEAR_ASSERTION",
        )
    if evidence.get("third_party_quote") is not False:
        return _result(None, "THIRD_PARTY_QUOTE")

    return _result(1 if derived_version == "1992" else 0, None)


def classify_noncompliance(evidence):
    """Return 1, 0, or None while preserving fail-closed behavior."""
    return evaluate_noncompliance(evidence)["classification"]
