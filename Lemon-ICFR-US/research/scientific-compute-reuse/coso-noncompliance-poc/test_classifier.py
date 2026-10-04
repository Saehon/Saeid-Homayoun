import hashlib

from classifier import classify_noncompliance, evaluate_noncompliance


def evidence(text, version, **overrides):
    item = {
        "issuer_cik": "0000789019",
        "accession": "0001193125-15-272806",
        "form_type": "10-K",
        "period_end": "2015-06-30",
        "source_section": "MANAGEMENT_ICFR_ASSESSMENT",
        "speaker": "MANAGEMENT",
        "disclosure_excerpt": text,
        "explicit_framework_version": version,
        "assertion_polarity": "ADOPTED",
        "third_party_quote": False,
    }
    item.update(overrides)
    item["excerpt_sha256"] = hashlib.sha256(
        item["disclosure_excerpt"].encode("utf-8")
    ).hexdigest()
    return item


explicit_1992 = evidence(
    "Management assessed ICFR using Internal Control—Integrated Framework (1992).",
    "1992",
)
explicit_2013 = evidence(
    "Management assessed ICFR using Internal Control—Integrated Framework (2013).",
    "2013",
)
unversioned = evidence(
    "Management assessed ICFR using Internal Control—Integrated Framework.",
    "UNVERSIONED",
)
both_versions = evidence(
    "Integrated Framework (1992) and Integrated Framework (2013)",
    "AMBIGUOUS",
)

assert classify_noncompliance(explicit_1992) == 1
assert classify_noncompliance(explicit_2013) == 0
assert classify_noncompliance(unversioned) is None
assert classify_noncompliance(both_versions) is None
assert classify_noncompliance("") is None
assert evaluate_noncompliance("")["reason"] == "INVALID_PROVENANCE_METADATA"
