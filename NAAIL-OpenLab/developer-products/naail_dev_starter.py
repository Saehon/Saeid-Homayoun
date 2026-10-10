"""Offline NAAIL developer concept baselines: illustrative, not AI inference.

No production audit decision, empirical estimate, model calibration, or published
finding may be inferred from these deterministic synthetic fixtures.
"""
from __future__ import annotations
from datetime import date
from typing import Iterable, Mapping


def evidence_gate(evidence: Iterable[Mapping], as_of: str) -> dict:
    """Check elementary claim provenance; approval always requires a person."""
    cutoff = date.fromisoformat(as_of)
    flags = []
    items = list(evidence)
    if not items:
        flags.append("NO_EVIDENCE")
    for i, item in enumerate(items):
        source_id = item.get("source_id")
        observed = item.get("source_date")
        if not source_id or not observed:
            flags.append(f"MISSING_PROVENANCE:{i}")
            continue
        try:
            if date.fromisoformat(str(observed)) > cutoff:
                flags.append(f"FUTURE_SOURCE:{i}")
        except ValueError:
            flags.append(f"INVALID_SOURCE_DATE:{i}")
        if item.get("independently_verified") is not True:
            flags.append(f"UNVERIFIED_SOURCE:{i}")
        if item.get("supports_claim") is not True:
            flags.append(f"UNSUPPORTED_CLAIM:{i}")
    return {"evidence_checks_passed": not flags, "flags": flags,
            "human_review_required": True, "autonomous_approval": False}


def icfr_rule_baseline(filing_lag_days: int, loss_indicator: bool,
                       prior_restatement: bool) -> dict:
    """An uncalibrated rule score, deliberately not an ICFR probability."""
    if filing_lag_days < 0:
        raise ValueError("filing_lag_days cannot be negative")
    score = min(filing_lag_days / 30, 1.0) * 0.5
    score += 0.2 if loss_indicator else 0.0
    score += 0.3 if prior_restatement else 0.0
    return {"rule_score": round(min(score, 1.0), 4),
            "calibrated_probability": False, "autonomous_approval": False}


def cam_reallocation(previous_topics: Iterable[str], current_topics: Iterable[str]) -> dict:
    """Jaccard composition change, not evidence of underlying audit quality."""
    previous, current = set(previous_topics), set(current_topics)
    union = previous | current
    return {"entered": sorted(current - previous), "exited": sorted(previous - current),
            "persisted": sorted(previous & current),
            "composition_change": round(1 - len(previous & current) / len(union), 4)
            if union else 0.0}


def ai_capex_rule(text: str) -> dict:
    """Primitive disclosure keyword tagging; requires manual accounting validation."""
    s = text.lower()
    ai = any(x in s for x in ("artificial intelligence", " ai ", "generative ai"))
    capital = any(x in s for x in ("capital expenditure", "capital spending", "capex"))
    operating = any(x in s for x in ("operating expense", "opex"))
    label = "AI_CAPEX_CANDIDATE" if ai and capital else (
        "AI_OPEX_CANDIDATE" if ai and operating else (
            "AI_CLAIM_ONLY" if ai else "NO_AI_SIGNAL"))
    return {"label": label, "accounting_verified": False}


def token_cost_twin(input_tokens: int, output_tokens: int,
                    usd_per_million_input: float, usd_per_million_output: float,
                    energy_kwh: float, usd_per_kwh: float,
                    grams_co2_per_kwh: float, reviewer_minutes: float,
                    reviewer_usd_per_hour: float) -> dict:
    """Illustrative activity-based cost accounting; not provider usage data."""
    vals = (input_tokens, output_tokens, usd_per_million_input,
            usd_per_million_output, energy_kwh, usd_per_kwh,
            grams_co2_per_kwh, reviewer_minutes, reviewer_usd_per_hour)
    if any(v < 0 for v in vals):
        raise ValueError("all costs and activity drivers must be nonnegative")
    api = (input_tokens * usd_per_million_input +
           output_tokens * usd_per_million_output) / 1_000_000
    energy = energy_kwh * usd_per_kwh
    review = reviewer_minutes * reviewer_usd_per_hour / 60
    return {"api_usd": round(api, 6), "energy_usd": round(energy, 6),
            "review_usd": round(review, 6),
            "total_usd": round(api + energy + review, 6),
            "carbon_grams": round(energy_kwh * grams_co2_per_kwh, 4),
            "assumptions_observed": False}
