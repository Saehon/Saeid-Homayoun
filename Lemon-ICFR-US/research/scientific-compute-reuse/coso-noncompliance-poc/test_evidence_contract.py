import hashlib
import json
from pathlib import Path

from classifier import evaluate_noncompliance


CATALOG = json.loads(
    (Path(__file__).with_name("adversarial-case-catalog-v0.1.json")).read_text(
        encoding="utf-8"
    )
)


def excerpt_for(item):
    version = item.get("explicit_framework_version")
    polarity = item.get("assertion_polarity")
    if version == "AMBIGUOUS":
        return "Integrated Framework (1992) and Integrated Framework (2013)"
    if version == "UNVERSIONED":
        return "Management assessed ICFR using Internal Control—Integrated Framework."
    if item.get("third_party_quote"):
        return (
            "A peer stated: Internal Control—Integrated Framework "
            f"({version})."
        )
    if item.get("speaker") == "AUDITOR":
        return (
            "The auditor's report refers to Internal Control—Integrated "
            f"Framework ({version})."
        )
    if polarity == "HISTORICAL_ONLY":
        return (
            "The prior framework was Internal Control—Integrated Framework "
            f"({version}); management uses the updated framework."
        )
    if polarity == "BIBLIOGRAPHIC":
        return (
            "See COSO, Internal Control—Integrated Framework "
            f"({version}), for background."
        )
    if polarity == "NEGATED":
        return (
            "Management did not adopt Internal Control—Integrated Framework "
            f"({version})."
        )
    return (
        "Management assessed ICFR using Internal Control—Integrated Framework "
        f"({version})."
    )


def materialize(case):
    item = dict(CATALOG["base_fixture"])
    for key in case.get("remove", []):
        item.pop(key, None)
    item.update(case.get("overrides", {}))

    hash_matches = item.pop("excerpt_hash_matches", True)
    item.pop("quoted_issuer_differs", None)
    item["disclosure_excerpt"] = excerpt_for(item)
    digest = hashlib.sha256(
        item["disclosure_excerpt"].encode("utf-8")
    ).hexdigest()
    item["excerpt_sha256"] = digest if hash_matches else "0" * 64
    return item


results = []
for case in CATALOG["cases"]:
    actual = evaluate_noncompliance(materialize(case))
    expected = {
        "classification": case["expected_classification"],
        "reason": case["expected_reason"],
    }
    assert actual == expected, (
        f"{case['id']}: expected {expected!r}, got {actual!r}"
    )
    results.append({"id": case["id"], **actual})

assert len(results) == CATALOG["acceptance"]["total_cases"] == 16
assert len({result["id"] for result in results}) == 16
