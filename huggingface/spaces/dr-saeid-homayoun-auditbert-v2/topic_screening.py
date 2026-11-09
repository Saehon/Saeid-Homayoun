"""Transparent, synthetic-safe CAM/KAM topic screening — Dr. Saeid Homayoun.

Rule-based research demonstration. NOT a fine-tuned FinBERT model, not an audit.
No remote processing, no private datasets, no credentials.
"""
from __future__ import annotations
import re

TOPIC_PATTERNS = {
    "Revenue recognition": (
        "revenue recognition", "revenue", "contract assets", "performance obligation",
        "variable consideration", "contract modification", "sales returns",
    ),
    "Goodwill and impairment": (
        "goodwill", "impairment", "cash-generating unit", "discount rate",
        "recoverable amount", "value in use", "long-term growth",
    ),
    "Inventory": (
        "inventory", "inventories", "obsolescence", "net realizable value",
        "net realisable value", "stock valuation", "slow-moving",
    ),
    "Going concern and liquidity": (
        "going concern", "liquidity", "covenant", "cash flow forecast",
        "refinancing", "solvency", "material uncertainty",
    ),
    "Fair value estimates": (
        "fair value", "valuation model", "level 3", "unobservable input",
        "market approach", "valuation techniques",
    ),
    "Financial instruments": (
        "financial instruments", "expected credit loss", "credit losses",
        "derivative", "hedging", "loan loss",
    ),
    "Tax accounting": (
        "deferred tax", "income tax", "tax uncertainty", "tax provision",
        "tax assets", "transfer pricing",
    ),
    "Business combinations": (
        "business combination", "acquisition", "purchase price allocation",
        "acquired intangible", "contingent consideration",
    ),
    "Provisions and litigation": (
        "provision", "litigation", "legal claims", "contingent liability",
        "restructuring", "warranty obligation",
    ),
    "Technology and cybersecurity": (
        "cybersecurity", "cyber", "information technology", "data breach",
        "system access", "information security",
    ),
}
STANDARDS = {
    "Revenue recognition": ("ASC 606", "IFRS 15"),
    "Goodwill and impairment": ("ASC 350 / ASC 360", "IAS 36"),
    "Inventory": ("ASC 330", "IAS 2"),
    "Going concern and liquidity": ("ASC 205-40", "IAS 1"),
    "Financial instruments": ("ASC 326 / ASC 815", "IFRS 9"),
    "Business combinations": ("ASC 805", "IFRS 3"),
    "Provisions and litigation": ("ASC 450", "IAS 37"),
}
JURISDICTIONS = ("US CAM (US GAAP)", "UK/EU KAM (IFRS)")

def screen(text: str, jurisdiction: str = JURISDICTIONS[0]) -> list[dict]:
    """Find matching accounting topics, ranking integer keyword counts only.

    Integer counts are not probabilities, classifier accuracy, CAM significance,
    reporting-compliance assessments, or conclusions about audit quality.
    """
    if not isinstance(text, str):
        raise TypeError("Matter text must be a string.")
    if len(text) > 30000:
        raise ValueError("Text exceeds the 30,000-character demo limit.")
    if jurisdiction not in JURISDICTIONS:
        raise ValueError("Unsupported jurisdiction.")
    normalized = re.sub(r"\s+", " ", text.lower()).strip()
    if not normalized:
        return []
    matches = []
    for topic, expressions in TOPIC_PATTERNS.items():
        hits = [term for term in expressions if re.search(
            r"(?<![a-z0-9])" + re.escape(term) + r"(?![a-z0-9])", normalized)]
        if hits:
            standard = STANDARDS.get(topic)
            reference = standard[0 if jurisdiction.startswith("US") else 1] if standard else "Professional review required"
            matches.append({
                "topic": topic,
                "keyword_hits": len(hits),
                "matched_terms": hits,
                "illustrative_reference": reference,
            })
    return sorted(matches, key=lambda z: (-z["keyword_hits"], z["topic"]))[:5]
