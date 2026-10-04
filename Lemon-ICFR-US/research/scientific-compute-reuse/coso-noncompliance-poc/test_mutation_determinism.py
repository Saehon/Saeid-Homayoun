import hashlib
import json

from classifier import evaluate_noncompliance


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


cases = [
    (
        evidence(
            "Management assessed ICFR using Internal Control - Integrated Framework (1992).",
            "1992",
        ),
        {"classification": 1, "reason": None},
    ),
    (
        evidence(
            "Management assessed ICFR using Internal Control - Integrated Framework (2013).",
            "2013",
        ),
        {"classification": 0, "reason": None},
    ),
    (
        evidence("Internal Control—Integrated Framework", "UNVERSIONED"),
        {
            "classification": None,
            "reason": "AMBIGUOUS_OR_UNVERSIONED_FRAMEWORK",
        },
    ),
    (
        evidence(
            "Integrated Framework (1992) and Integrated Framework (2013)",
            "AMBIGUOUS",
        ),
        {
            "classification": None,
            "reason": "AMBIGUOUS_OR_UNVERSIONED_FRAMEWORK",
        },
    ),
    (
        evidence("COSO framework", "UNVERSIONED"),
        {
            "classification": None,
            "reason": "AMBIGUOUS_OR_UNVERSIONED_FRAMEWORK",
        },
    ),
    (
        {},
        {"classification": None, "reason": "INVALID_PROVENANCE_METADATA"},
    ),
]

first = [evaluate_noncompliance(item) for item, _ in cases]
second = [evaluate_noncompliance(item) for item, _ in cases]
expected = [result for _, result in cases]

assert first == expected
assert second == expected
assert first == second
assert json.dumps(first, sort_keys=True) == json.dumps(second, sort_keys=True)
