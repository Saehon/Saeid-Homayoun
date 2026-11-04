#!/usr/bin/env python3
"""Build blinded CAM narrative validation samples.

The script joins the private CAM source, the matter-account DARWIN output, and
the Hugging Face Tokenizers profile.  It assigns every matter to one account,
forms within-account score tertiles, and draws a deterministic pilot and main
sample while preventing reuse of a CAM, company, or normalized narrative.

Raw narrative text is written only to the reviewer files.  The private key
contains identifiers, design variables, and model metadata, but no raw text.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import tempfile
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence


SEED = 20261014
PROTOCOL_ID = "CAM-RL-HVA"
CODEBOOK_VERSION = "0.9.0"
FORM_SOFTWARE_VERSION = "csv-1.0.0"
SAMPLER_VERSION = "1.0.0"
CANONICAL_DOMAINS = (
    "EQ",
    "FIN",
    "GW",
    "INT",
    "INV",
    "LEASE",
    "OTHER",
    "PPE",
    "PROV",
    "REC",
    "REV",
    "TAX",
)
BANDS = ("LOW", "MID", "HIGH")
TARGET_YEARS = (2020, 2021, 2022, 2023, 2024)
DIMENSIONS = (
    ("estimation_uncertainty", "EU"),
    ("adverse_outcome", "AO"),
    ("valuation_complexity", "VC"),
    ("forward_looking_risk", "FL"),
    ("overall_risk_language", "ORL"),
)
REVIEW_FIELDS = tuple(
    field
    for name, abbreviation in DIMENSIONS
    for field in (
        f"{name}_{abbreviation}_0_to_3",
        *(
            evidence_field
            for span_number in (1, 2, 3)
            for evidence_field in (
                f"{name}_{abbreviation}_evidence_span_{span_number}_source_field",
                f"{name}_{abbreviation}_evidence_span_{span_number}_start_0_based_inclusive",
                f"{name}_{abbreviation}_evidence_span_{span_number}_end_0_based_exclusive",
                f"{name}_{abbreviation}_evidence_span_{span_number}_exact_quote",
                f"{name}_{abbreviation}_evidence_span_{span_number}_extended_reason_if_over_40_tokens",
            )
        ),
        f"{name}_{abbreviation}_rationale_one_sentence",
    )
) + (
    "audit_attention_only",
    "procedure_language_intrusion",
    "negation_or_resolution",
    "insufficient_context",
    "unable_to_code",
    "confidence",
    "reviewer_note",
)


class ValidationSampleError(RuntimeError):
    """Raised when inputs or required sampling constraints are invalid."""


def _inside_git_worktree(path: Path) -> bool:
    """Return True when path is at or below a directory containing .git."""

    resolved = path.resolve(strict=False)
    start = resolved if resolved.is_dir() else resolved.parent
    for directory in (start, *start.parents):
        marker = directory / ".git"
        # A real worktree uses either a .git file or a directory containing
        # HEAD. Some managed runtimes expose an empty read-only .git sentinel
        # at the workspace root; that sentinel is not a Git worktree.
        if marker.is_file() or (marker.is_dir() and (marker / "HEAD").exists()):
            return True
    return False


def prepare_private_output_dir(path: Path) -> Path:
    """Create or accept an empty private output directory outside Git."""

    resolved = path.resolve(strict=False)
    if _inside_git_worktree(resolved):
        raise ValidationSampleError(
            f"refusing private raw-text output inside a Git worktree: {resolved}"
        )
    if resolved.exists():
        if not resolved.is_dir():
            raise ValidationSampleError(f"output path is not a directory: {resolved}")
        if any(resolved.iterdir()):
            raise ValidationSampleError(
                f"output directory must be new or empty to prevent stale artifacts: {resolved}"
            )
    else:
        resolved.mkdir(parents=True, mode=0o700)
    try:
        resolved.chmod(0o700)
    except OSError:
        # POSIX mode bits may be unavailable on some filesystems. The Git and
        # emptiness guards still apply, and the OS controls effective access.
        pass
    return resolved


@dataclass(frozen=True)
class Candidate:
    matter_key: str
    company_key: str
    opinion_key: str
    source_topic: str
    title: str
    description: str
    assigned_domain: str
    all_mapped_domains: tuple[str, ...]
    assignment_domain_frequency: int
    band: str
    score: float
    linked: bool
    fiscal_year: int | None
    fiscal_year_status: str
    fingerprint: str
    hf_component: str
    hf_component_version: str
    hf_pretrained_model_inference_executed: str

    @property
    def stratum(self) -> tuple[str, str, str]:
        return (
            self.assigned_domain,
            self.band,
            "LINKED" if self.linked else "UNLINKED",
        )


def _required_columns(path: Path, actual: Sequence[str] | None, required: set[str]) -> None:
    missing = sorted(required - set(actual or ()))
    if missing:
        raise ValidationSampleError(f"{path}: missing required columns: {missing}")


def _read_unique_csv(path: Path, key: str, required: set[str]) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        _required_columns(path, reader.fieldnames, required | {key})
        for line_number, row in enumerate(reader, start=2):
            value = (row.get(key) or "").strip()
            if not value:
                raise ValidationSampleError(f"{path}:{line_number}: blank {key}")
            if value in rows:
                raise ValidationSampleError(f"{path}:{line_number}: duplicate {key}={value}")
            rows[value] = row
    return rows


def _read_matter_accounts(path: Path) -> dict[str, list[dict[str, str]]]:
    required = {
        "critical_audit_matter_key",
        "company_key",
        "audit_opinion_fkey",
        "source_topic",
        "account_domain",
        "fiscal_year",
        "fiscal_year_status",
        "cam_narrative_risk_language_density_per_1000_tokens",
        "normalized_narrative_sha256",
    }
    by_matter: dict[str, list[dict[str, str]]] = defaultdict(list)
    seen_pairs: set[tuple[str, str]] = set()
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        _required_columns(path, reader.fieldnames, required)
        for line_number, row in enumerate(reader, start=2):
            key = (row.get("critical_audit_matter_key") or "").strip()
            domain = (row.get("account_domain") or "").strip()
            if not key or not domain:
                raise ValidationSampleError(
                    f"{path}:{line_number}: blank matter key or account domain"
                )
            pair = (key, domain)
            if pair in seen_pairs:
                raise ValidationSampleError(
                    f"{path}:{line_number}: duplicate matter-domain pair {pair}"
                )
            seen_pairs.add(pair)
            by_matter[key].append(row)
    return dict(by_matter)


def quantile_linear(values: Sequence[float], probability: float) -> float:
    """Return the linearly interpolated empirical quantile (NumPy default)."""

    if not values:
        raise ValidationSampleError("cannot calculate a quantile of an empty sequence")
    if not 0 <= probability <= 1:
        raise ValueError("probability must be in [0, 1]")
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    fraction = position - lower
    return ordered[lower] + fraction * (ordered[upper] - ordered[lower])


def assign_band(score: float, low_threshold: float, high_threshold: float) -> str:
    """Assign a score to LOW/MID/HIGH, keeping threshold ties in the lower band."""

    if score <= low_threshold:
        return "LOW"
    if score <= high_threshold:
        return "MID"
    return "HIGH"


def assign_rarest_domain(
    rows: Sequence[Mapping[str, str]], domain_frequency: Mapping[str, int]
) -> tuple[str, tuple[str, ...]]:
    """Assign a matter to its globally rarest mapped domain.

    Alphabetical order breaks frequency ties.  A matter with no canonical
    mapped domain is assigned to UNMAPPED.
    """

    mapped = sorted(
        {
            (row.get("account_domain") or "").strip()
            for row in rows
            if (row.get("account_domain") or "").strip() in CANONICAL_DOMAINS
        }
    )
    if not mapped:
        return "UNMAPPED", ()
    assigned = min(mapped, key=lambda domain: (domain_frequency[domain], domain))
    return assigned, tuple(mapped)


def _safe_float(value: str, field: str, matter_key: str) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError) as exc:
        raise ValidationSampleError(
            f"matter {matter_key}: invalid {field}={value!r}"
        ) from exc
    if not math.isfinite(result):
        raise ValidationSampleError(f"matter {matter_key}: non-finite {field}")
    return result


def _parse_link(row: Mapping[str, str], matter_key: str) -> tuple[bool, int | None]:
    status = (row.get("fiscal_year_status") or "").strip()
    raw_year = (row.get("fiscal_year") or "").strip()
    linked = status == "provisional_opinion_year_crosswalk"
    if linked:
        try:
            year = int(raw_year)
        except ValueError as exc:
            raise ValidationSampleError(
                f"matter {matter_key}: linked row has invalid fiscal_year={raw_year!r}"
            ) from exc
        if year not in TARGET_YEARS:
            raise ValidationSampleError(
                f"matter {matter_key}: linked fiscal year {year} outside 2020-2024"
            )
        return True, year
    if raw_year:
        raise ValidationSampleError(
            f"matter {matter_key}: unlinked row unexpectedly has fiscal_year={raw_year!r}"
        )
    return False, None


def build_candidates(
    cam_path: Path,
    matter_account_path: Path,
    profile_path: Path,
    excluded_matter_keys: frozenset[str] = frozenset(),
) -> tuple[list[Candidate], dict[str, object]]:
    """Join and validate the three private inputs, then create candidates."""

    cam = _read_unique_csv(
        cam_path,
        "CRITICAL_AUDIT_MATTER_KEY",
        {
            "TITLE",
            "DESCRIPTION",
            "AUDIT_OPINION_FKEY",
            "COMPANY_KEY",
            "TOPIC_NAME",
        },
    )
    profile = _read_unique_csv(
        profile_path,
        "critical_audit_matter_key",
        {
            "normalized_narrative_sha256",
            "hf_component",
            "hf_component_version",
            "hf_pretrained_model_inference_executed",
        },
    )
    accounts = _read_matter_accounts(matter_account_path)

    cam_keys, profile_keys, account_keys = set(cam), set(profile), set(accounts)
    if not (cam_keys == profile_keys == account_keys):
        raise ValidationSampleError(
            "input matter keys do not match exactly: "
            f"CAM={len(cam_keys)}, profile={len(profile_keys)}, accounts={len(account_keys)}, "
            f"CAM-only={len(cam_keys - profile_keys - account_keys)}, "
            f"profile-only={len(profile_keys - cam_keys)}, "
            f"accounts-only={len(account_keys - cam_keys)}"
        )

    domain_frequency: Counter[str] = Counter()
    for rows in accounts.values():
        for domain in {
            (row.get("account_domain") or "").strip()
            for row in rows
            if (row.get("account_domain") or "").strip() in CANONICAL_DOMAINS
        }:
            domain_frequency[domain] += 1

    staged: list[dict[str, object]] = []
    multi_account_count = 0
    for matter_key in sorted(cam_keys, key=lambda value: (len(value), value)):
        if matter_key in excluded_matter_keys:
            continue
        account_rows = accounts[matter_key]
        assigned, mapped_domains = assign_rarest_domain(account_rows, domain_frequency)
        if len(mapped_domains) > 1:
            multi_account_count += 1
        selected = next(
            (row for row in account_rows if row["account_domain"] == assigned),
            account_rows[0],
        )
        source = cam[matter_key]
        prof = profile[matter_key]

        cross_checks = {
            "company_key": (source.get("COMPANY_KEY", ""), selected.get("company_key", "")),
            "opinion_key": (
                source.get("AUDIT_OPINION_FKEY", ""),
                selected.get("audit_opinion_fkey", ""),
            ),
            "source_topic": (source.get("TOPIC_NAME", ""), selected.get("source_topic", "")),
            "fingerprint": (
                selected.get("normalized_narrative_sha256", ""),
                prof.get("normalized_narrative_sha256", ""),
            ),
        }
        for field, (left, right) in cross_checks.items():
            if left.strip() != right.strip():
                raise ValidationSampleError(
                    f"matter {matter_key}: {field} mismatch {left!r} != {right!r}"
                )

        fingerprint = (prof.get("normalized_narrative_sha256") or "").strip().lower()
        if len(fingerprint) != 64 or any(ch not in "0123456789abcdef" for ch in fingerprint):
            raise ValidationSampleError(
                f"matter {matter_key}: invalid normalized narrative SHA-256"
            )
        company_key = (selected.get("company_key") or "").strip()
        if not company_key:
            raise ValidationSampleError(f"matter {matter_key}: blank company key")
        linked, year = _parse_link(selected, matter_key)
        score = _safe_float(
            selected.get("cam_narrative_risk_language_density_per_1000_tokens", ""),
            "cam_narrative_risk_language_density_per_1000_tokens",
            matter_key,
        )
        staged.append(
            {
                "matter_key": matter_key,
                "company_key": company_key,
                "opinion_key": (selected.get("audit_opinion_fkey") or "").strip(),
                "source_topic": (selected.get("source_topic") or "").strip(),
                "title": source.get("TITLE") or "",
                "description": source.get("DESCRIPTION") or "",
                "assigned_domain": assigned,
                "all_mapped_domains": mapped_domains,
                "assignment_domain_frequency": domain_frequency.get(assigned, 0),
                "score": score,
                "linked": linked,
                "fiscal_year": year,
                "fiscal_year_status": (selected.get("fiscal_year_status") or "").strip(),
                "fingerprint": fingerprint,
                "hf_component": (prof.get("hf_component") or "").strip(),
                "hf_component_version": (prof.get("hf_component_version") or "").strip(),
                "hf_pretrained_model_inference_executed": (
                    prof.get("hf_pretrained_model_inference_executed") or ""
                ).strip().lower(),
            }
        )

    scores_by_domain: dict[str, list[float]] = defaultdict(list)
    for row in staged:
        scores_by_domain[str(row["assigned_domain"])].append(float(row["score"]))
    expected_domains = set(CANONICAL_DOMAINS) | {"UNMAPPED"}
    missing_domains = sorted(expected_domains - set(scores_by_domain))
    if missing_domains:
        raise ValidationSampleError(f"no candidates for domains: {missing_domains}")

    thresholds = {
        domain: {
            "q33_333333": quantile_linear(scores, 1 / 3),
            "q66_666667": quantile_linear(scores, 2 / 3),
        }
        for domain, scores in scores_by_domain.items()
    }
    candidates: list[Candidate] = []
    for row in staged:
        domain = str(row["assigned_domain"])
        band = assign_band(
            float(row["score"]),
            thresholds[domain]["q33_333333"],
            thresholds[domain]["q66_666667"],
        )
        candidates.append(Candidate(band=band, **row))

    eligible_digest = hashlib.sha256()
    for candidate in sorted(candidates, key=lambda item: item.matter_key):
        eligible_digest.update(
            json.dumps(
                [
                    candidate.matter_key,
                    candidate.company_key,
                    candidate.fingerprint,
                    candidate.assigned_domain,
                    candidate.band,
                    candidate.linked,
                    candidate.fiscal_year,
                    format(candidate.score, ".17g"),
                ],
                ensure_ascii=False,
                separators=(",", ":"),
            ).encode("utf-8")
        )
        eligible_digest.update(b"\n")

    qa = {
        "input_rows": {
            "cam_matters": len(cam),
            "token_profile_matters": len(profile),
            "matter_account_rows": sum(len(rows) for rows in accounts.values()),
            "matter_account_unique_matters": len(accounts),
        },
        "join_key_sets_match_exactly": True,
        "multi_account_matters_assigned_to_rarest_domain": multi_account_count,
        "global_mapped_domain_frequencies": dict(sorted(domain_frequency.items())),
        "assigned_domain_counts": dict(
            sorted(Counter(candidate.assigned_domain for candidate in candidates).items())
        ),
        "within_account_score_band_thresholds": thresholds,
        "hf_components": sorted({candidate.hf_component for candidate in candidates}),
        "hf_component_versions": sorted(
            {candidate.hf_component_version for candidate in candidates}
        ),
        "hf_pretrained_model_inference_executed_values": sorted(
            {candidate.hf_pretrained_model_inference_executed for candidate in candidates}
        ),
        "excluded_matter_keys": sorted(excluded_matter_keys),
        "eligible_population_count_after_exclusions": len(candidates),
        "eligible_population_design_sha256": eligible_digest.hexdigest(),
    }
    return candidates, qa


def main_quotas() -> dict[tuple[str, str, str], int]:
    quotas: dict[tuple[str, str, str], int] = {}
    for domain in CANONICAL_DOMAINS:
        for band in BANDS:
            quotas[(domain, band, "LINKED")] = 8
            quotas[(domain, band, "UNLINKED")] = 12
    unmapped_linked = {"LOW": 11, "MID": 10, "HIGH": 11}
    for band in BANDS:
        quotas[("UNMAPPED", band, "LINKED")] = unmapped_linked[band]
        quotas[("UNMAPPED", band, "UNLINKED")] = 16
    assert sum(quotas.values()) == 800
    return quotas


def pilot_quotas() -> dict[tuple[str, str, str], int]:
    """Return a 30-case design: 2/domain plus 6 UNMAPPED, balanced overall."""

    quotas: dict[tuple[str, str, str], int] = {}
    for index, domain in enumerate(CANONICAL_DOMAINS):
        linked_band = BANDS[index % 3]
        unlinked_band = BANDS[(index + 1) % 3]
        quotas[(domain, linked_band, "LINKED")] = 1
        quotas[(domain, unlinked_band, "UNLINKED")] = 1
    for band in BANDS:
        quotas[("UNMAPPED", band, "LINKED")] = 1
        quotas[("UNMAPPED", band, "UNLINKED")] = 1
    assert sum(quotas.values()) == 30
    return quotas


def _priority(seed: int, salt: str, matter_key: str) -> str:
    return hashlib.sha256(f"{seed}|{salt}|{matter_key}".encode("utf-8")).hexdigest()


def _available(
    candidates: Iterable[Candidate],
    used_matters: set[str],
    used_companies: set[str],
    used_fingerprints: set[str],
) -> list[Candidate]:
    return [
        candidate
        for candidate in candidates
        if candidate.matter_key not in used_matters
        and candidate.company_key not in used_companies
        and candidate.fingerprint not in used_fingerprints
    ]


def _year_coverage(
    selected: Sequence[Candidate], quotas: Mapping[tuple[str, str, str], int]
) -> dict[str, list[int]]:
    result: dict[str, list[int]] = {}
    for stratum in quotas:
        if stratum[2] != "LINKED":
            continue
        years = {
            candidate.fiscal_year
            for candidate in selected
            if candidate.stratum == stratum and candidate.fiscal_year is not None
        }
        result["|".join(stratum)] = sorted(years)
    return result


def select_with_quotas(
    candidates: Sequence[Candidate],
    quotas: Mapping[tuple[str, str, str], int],
    *,
    seed: int,
    phase: str,
    reserved: Sequence[Candidate] = (),
    year_mode: str,
    attempts: int = 80,
) -> tuple[list[Candidate], dict[str, object]]:
    """Select an exact quota sample under global matter/company/text uniqueness.

    ``year_mode='per_stratum'`` tries to cover all 2020-2024 years in every
    linked stratum. ``year_mode='global'`` tries to cover all five years over
    the linked sample as a whole (used for the 30-case pilot).
    """

    if year_mode not in {"per_stratum", "global"}:
        raise ValueError("year_mode must be 'per_stratum' or 'global'")
    by_stratum: dict[tuple[str, str, str], list[Candidate]] = defaultdict(list)
    for candidate in candidates:
        by_stratum[candidate.stratum].append(candidate)
    unavailable = {
        "|".join(stratum): {"required": quota, "available_rows": len(by_stratum[stratum])}
        for stratum, quota in quotas.items()
        if len(by_stratum[stratum]) < quota
    }
    if unavailable:
        raise ValidationSampleError(f"strata lack raw candidates: {unavailable}")

    reserved_matters = {candidate.matter_key for candidate in reserved}
    reserved_companies = {candidate.company_key for candidate in reserved}
    reserved_fingerprints = {candidate.fingerprint for candidate in reserved}
    best: list[Candidate] = []
    best_metric: tuple[int, int] | None = None
    best_coverage: dict[str, list[int]] = {}
    best_shortfalls: dict[str, int] = {}

    for attempt in range(attempts):
        used_matters = set(reserved_matters)
        used_companies = set(reserved_companies)
        used_fingerprints = set(reserved_fingerprints)
        chosen: list[Candidate] = []
        global_years: set[int] = set()

        # Scarce strata go first. A deterministic attempt-specific hash breaks ties.
        strata = list(quotas)
        strata.sort(
            key=lambda stratum: (
                len({candidate.company_key for candidate in by_stratum[stratum]})
                / quotas[stratum],
                _priority(seed, f"{phase}|stratum|{attempt}", "|".join(stratum)),
            )
        )
        for stratum in strata:
            needed = quotas[stratum]
            pool = by_stratum[stratum]
            selected_here: list[Candidate] = []

            if stratum[2] == "LINKED" and year_mode == "per_stratum":
                year_order = sorted(
                    TARGET_YEARS,
                    key=lambda year: (
                        len({c.company_key for c in pool if c.fiscal_year == year}),
                        _priority(seed, f"{phase}|year|{attempt}|{stratum}", str(year)),
                    ),
                )
                for year in year_order:
                    if len(selected_here) >= needed:
                        break
                    options = _available(
                        (c for c in pool if c.fiscal_year == year),
                        used_matters,
                        used_companies,
                        used_fingerprints,
                    )
                    options.sort(
                        key=lambda c: _priority(
                            seed, f"{phase}|cover|{attempt}|{stratum}|{year}", c.matter_key
                        )
                    )
                    if options:
                        picked = options[0]
                        selected_here.append(picked)
                        used_matters.add(picked.matter_key)
                        used_companies.add(picked.company_key)
                        used_fingerprints.add(picked.fingerprint)

            if stratum[2] == "LINKED" and year_mode == "global" and len(selected_here) < needed:
                missing_years = set(TARGET_YEARS) - global_years
                options = _available(
                    (c for c in pool if c.fiscal_year in missing_years),
                    used_matters,
                    used_companies,
                    used_fingerprints,
                )
                options.sort(
                    key=lambda c: (
                        len([x for x in pool if x.fiscal_year == c.fiscal_year]),
                        _priority(seed, f"{phase}|global-year|{attempt}|{stratum}", c.matter_key),
                    )
                )
                if options:
                    picked = options[0]
                    selected_here.append(picked)
                    global_years.add(int(picked.fiscal_year))
                    used_matters.add(picked.matter_key)
                    used_companies.add(picked.company_key)
                    used_fingerprints.add(picked.fingerprint)

            remaining = needed - len(selected_here)
            if remaining:
                options = _available(
                    pool, used_matters, used_companies, used_fingerprints
                )
                options.sort(
                    key=lambda c: _priority(
                        seed, f"{phase}|fill|{attempt}|{stratum}", c.matter_key
                    )
                )
                for picked in options:
                    if len(selected_here) >= needed:
                        break
                    # Options were built as a batch. Recheck uniqueness here so
                    # two rows in that batch cannot share a company or text.
                    if (
                        picked.matter_key in used_matters
                        or picked.company_key in used_companies
                        or picked.fingerprint in used_fingerprints
                    ):
                        continue
                    selected_here.append(picked)
                    if picked.fiscal_year is not None:
                        global_years.add(picked.fiscal_year)
                    used_matters.add(picked.matter_key)
                    used_companies.add(picked.company_key)
                    used_fingerprints.add(picked.fingerprint)
            chosen.extend(selected_here)

        counts = Counter(candidate.stratum for candidate in chosen)
        shortfalls = {
            "|".join(stratum): quotas[stratum] - counts[stratum]
            for stratum in quotas
            if counts[stratum] != quotas[stratum]
        }
        coverage = _year_coverage(chosen, quotas)
        if year_mode == "per_stratum":
            missing_year_units = sum(
                len(set(TARGET_YEARS) - set(years)) for years in coverage.values()
            )
        else:
            all_years = {year for years in coverage.values() for year in years}
            missing_year_units = len(set(TARGET_YEARS) - all_years)
        metric = (sum(shortfalls.values()), missing_year_units)
        if best_metric is None or metric < best_metric:
            best = chosen
            best_metric = metric
            best_coverage = coverage
            best_shortfalls = shortfalls
        if metric == (0, 0):
            break

    if best_metric is None or best_metric[0] != 0:
        raise ValidationSampleError(
            f"unable to satisfy exact {phase} quotas after {attempts} attempts; "
            f"shortfalls={best_shortfalls}"
        )
    if best_metric[1] != 0:
        raise ValidationSampleError(
            f"unable to cover requested 2020-2024 linked years for {phase}; "
            f"coverage={best_coverage}"
        )

    actual = Counter(candidate.stratum for candidate in best)
    qa = {
        "phase": phase,
        "requested_total": sum(quotas.values()),
        "selected_total": len(best),
        "requested_quotas": {"|".join(key): value for key, value in sorted(quotas.items())},
        "actual_quotas": {"|".join(key): value for key, value in sorted(actual.items())},
        "exact_quotas_met": all(actual[key] == value for key, value in quotas.items()),
        "year_coverage_mode": year_mode,
        "linked_year_coverage": best_coverage,
        "all_target_years_covered": True,
    }
    return best, qa


def spreadsheet_safe_text(value: str) -> tuple[str, bool]:
    """Normalize a narrative cell and neutralize spreadsheet formula prefixes."""

    text = unicodedata.normalize("NFC", value or "")
    text = text.replace("\x00", "").replace("\r\n", "\n").replace("\r", "\n")
    first = text.lstrip()[:1]
    if first in {"=", "+", "-", "@"}:
        return "'" + text, True
    return text, False


def _case_id(phase: str, matter_key: str, seed: int) -> str:
    prefix = "P" if phase == "pilot" else "M"
    digest = hashlib.sha256(f"{seed}|case|{phase}|{matter_key}".encode()).hexdigest()[:14]
    return f"{prefix}-{digest.upper()}"


def _atomic_csv(path: Path, fieldnames: Sequence[str], rows: Iterable[Mapping[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent, text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="raise")
            writer.writeheader()
            writer.writerows(rows)
        os.replace(temporary, path)
        try:
            path.chmod(0o600)
        except OSError:
            pass
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def write_reviewer_files(
    selected: Sequence[Candidate], output_dir: Path, phase: str, seed: int
) -> tuple[dict[str, object], dict[str, dict[str, int]]]:
    fieldnames = (
        "protocol_id",
        "codebook_version",
        "case_id",
        "reviewer_id_pseudonym",
        "assignment_batch",
        "display_order",
        "started_at_utc",
        "submitted_at_utc",
        "form_software_version",
        "title",
        "description",
    ) + REVIEW_FIELDS
    case_ids = {candidate.matter_key: _case_id(phase, candidate.matter_key, seed) for candidate in selected}
    if len(set(case_ids.values())) != len(case_ids):
        raise ValidationSampleError(f"{phase}: blind case ID collision")
    sanitized_count = 0
    row_maps: dict[str, dict[str, int]] = {}
    output_meta: dict[str, object] = {}
    for reviewer in ("A", "B"):
        ordered = sorted(
            selected,
            key=lambda candidate: _priority(
                seed, f"{phase}|reviewer-{reviewer}-order", candidate.matter_key
            ),
        )
        rows = []
        row_map: dict[str, int] = {}
        for number, candidate in enumerate(ordered, start=1):
            title, title_changed = spreadsheet_safe_text(candidate.title)
            description, description_changed = spreadsheet_safe_text(candidate.description)
            sanitized_count += int(title_changed) + int(description_changed)
            case_id = case_ids[candidate.matter_key]
            row_map[candidate.matter_key] = number
            row = {
                "protocol_id": PROTOCOL_ID,
                "codebook_version": CODEBOOK_VERSION,
                "case_id": case_id,
                "reviewer_id_pseudonym": f"REVIEWER_{reviewer}",
                "assignment_batch": "pilot_round_1"
                if phase == "pilot"
                else "confirmatory_main",
                "display_order": number,
                "started_at_utc": "",
                "submitted_at_utc": "",
                "form_software_version": FORM_SOFTWARE_VERSION,
                "title": title,
                "description": description,
            }
            row.update({field: "" for field in REVIEW_FIELDS})
            rows.append(row)
        filename = f"CAM_validation_{phase}_reviewer_{reviewer}_PRIVATE.csv"
        path = output_dir / filename
        _atomic_csv(path, fieldnames, rows)
        row_maps[reviewer] = row_map
        output_meta[reviewer] = {
            "filename": filename,
            "rows": len(rows),
            "sha256": file_sha256(path),
        }
    output_meta["formula_prefix_cells_neutralized_across_both_reviewer_files"] = sanitized_count
    return output_meta, row_maps


def write_private_key(
    selected: Sequence[Candidate],
    output_dir: Path,
    phase: str,
    seed: int,
    reviewer_rows: Mapping[str, Mapping[str, int]],
) -> Path:
    fields = (
        "sample_phase",
        "case_id",
        "reviewer_A_display_order",
        "reviewer_B_display_order",
        "critical_audit_matter_key",
        "company_key",
        "audit_opinion_fkey",
        "source_topic",
        "assigned_account_domain",
        "all_mapped_account_domains",
        "domain_assignment_rule",
        "assigned_domain_global_frequency",
        "score_band",
        "band_definition",
        "fiscal_year_link_status",
        "provisional_fiscal_year",
        "cam_narrative_risk_language_density_per_1000_tokens",
        "normalized_narrative_sha256",
        "hf_component",
        "hf_component_version",
        "hf_pretrained_model_inference_executed",
        "construct_status",
        "selection_seed",
        "label_status",
    )
    rows = []
    for candidate in sorted(selected, key=lambda c: _case_id(phase, c.matter_key, seed)):
        rows.append(
            {
                "sample_phase": phase,
                "case_id": _case_id(phase, candidate.matter_key, seed),
                "reviewer_A_display_order": reviewer_rows["A"][candidate.matter_key],
                "reviewer_B_display_order": reviewer_rows["B"][candidate.matter_key],
                "critical_audit_matter_key": candidate.matter_key,
                "company_key": candidate.company_key,
                "audit_opinion_fkey": candidate.opinion_key,
                "source_topic": candidate.source_topic,
                "assigned_account_domain": candidate.assigned_domain,
                "all_mapped_account_domains": ";".join(candidate.all_mapped_domains)
                if candidate.all_mapped_domains
                else "UNMAPPED",
                "domain_assignment_rule": "globally_rarest_mapped_domain_then_alphabetical_tie_break",
                "assigned_domain_global_frequency": candidate.assignment_domain_frequency,
                "score_band": candidate.band,
                "band_definition": "within_assigned_account_q33_q67_continuous_score",
                "fiscal_year_link_status": "PROVISIONAL_LINKED"
                if candidate.linked
                else "UNLINKED",
                "provisional_fiscal_year": candidate.fiscal_year or "",
                "cam_narrative_risk_language_density_per_1000_tokens": format(
                    candidate.score, ".17g"
                ),
                "normalized_narrative_sha256": candidate.fingerprint,
                "hf_component": candidate.hf_component,
                "hf_component_version": candidate.hf_component_version,
                "hf_pretrained_model_inference_executed": candidate.hf_pretrained_model_inference_executed,
                "construct_status": "post_selection_descriptive_proxy",
                "selection_seed": seed,
                "label_status": "awaiting_independent_human_review",
            }
        )
    path = output_dir / f"CAM_validation_{phase}_private_key_NO_RAW_TEXT.csv"
    _atomic_csv(path, fields, rows)
    return path


def write_adjudication_template(
    selected: Sequence[Candidate], output_dir: Path, phase: str, seed: int
) -> Path:
    fields = (
        "protocol_id",
        "codebook_version",
        "case_id",
        "form_software_version",
        "reviewer_A_complete_0_or_1",
        "reviewer_B_complete_0_or_1",
        "dimension_code",
        "reviewer_A_score_0_to_3",
        "reviewer_B_score_0_to_3",
        "reviewer_A_evidence_summary",
        "reviewer_B_evidence_summary",
        "decision_select_A_select_B_or_third",
        "adjudicated_score_0_to_3",
        *(
            evidence_field
            for span_number in (1, 2, 3)
            for evidence_field in (
                f"adjudicated_evidence_span_{span_number}_source_field",
                f"adjudicated_evidence_span_{span_number}_start_0_based_inclusive",
                f"adjudicated_evidence_span_{span_number}_end_0_based_exclusive",
                f"adjudicated_evidence_span_{span_number}_exact_quote",
                f"adjudicated_evidence_span_{span_number}_extended_reason_if_over_40_tokens",
            )
        ),
        "controlling_anchor_or_exclusion_max_300_chars",
        "disagreement_type",
        "adjudicator_confidence_low_medium_high",
        "exclude_from_validation_0_or_1",
        "exclusion_reason",
    )
    rows = []
    for candidate in sorted(selected, key=lambda c: _case_id(phase, c.matter_key, seed)):
        for _, abbreviation in DIMENSIONS:
            row = {field: "" for field in fields}
            row["protocol_id"] = PROTOCOL_ID
            row["codebook_version"] = CODEBOOK_VERSION
            row["case_id"] = _case_id(phase, candidate.matter_key, seed)
            row["form_software_version"] = FORM_SOFTWARE_VERSION
            row["dimension_code"] = abbreviation
            rows.append(row)
    path = output_dir / f"CAM_validation_{phase}_adjudication_PRIVATE.csv"
    _atomic_csv(path, fields, rows)
    return path


def write_worked_example(output_dir: Path) -> dict[str, object]:
    """Write a synthetic, explicitly non-validation coding example."""

    common = {
        "protocol_id": PROTOCOL_ID,
        "codebook_version": CODEBOOK_VERSION,
        "case_id": "DEMO-SYNTHETIC-001",
        "reviewer_id_pseudonym": "DEMONSTRATION_ONLY",
        "assignment_batch": "synthetic_training_demonstration",
        "display_order": 1,
        "started_at_utc": "",
        "submitted_at_utc": "",
        "form_software_version": FORM_SOFTWARE_VERSION,
        "title": "Impairment evaluation of goodwill",
        "description": (
            "The annual goodwill impairment test depended on forecast revenue and "
            "operating margins, the terminal growth rate, and the discount rate. These "
            "assumptions were sensitive to changing market conditions. A reasonably "
            "possible decrease in forecast cash flows could result in a material "
            "impairment charge."
        ),
        "label_status": "demonstration_only_not_human_validation",
    }
    fields = (
        "protocol_id",
        "codebook_version",
        "case_id",
        "reviewer_id_pseudonym",
        "assignment_batch",
        "display_order",
        "started_at_utc",
        "submitted_at_utc",
        "form_software_version",
        "title",
        "description",
        "label_status",
    ) + REVIEW_FIELDS
    blank = dict(common)
    blank.update({field: "" for field in REVIEW_FIELDS})
    completed = dict(common)
    evidence = {
        "estimation_uncertainty": [
            "These assumptions were sensitive to changing market conditions."
        ],
        "adverse_outcome": [
            "A reasonably possible decrease in forecast cash flows could result in a "
            "material impairment charge."
        ],
        "valuation_complexity": ["the terminal growth rate, and the discount rate"],
        "forward_looking_risk": [
            "forecast revenue and operating margins",
            "These assumptions were sensitive to changing market conditions.",
        ],
        "overall_risk_language": [
            "These assumptions were sensitive to changing market conditions.",
            "A reasonably possible decrease in forecast cash flows could result in a "
            "material impairment charge.",
        ],
    }
    ratings = {
        "estimation_uncertainty": 3,
        "adverse_outcome": 2,
        "valuation_complexity": 2,
        "forward_looking_risk": 3,
        "overall_risk_language": 3,
    }
    description = common["description"]
    for name, abbreviation in DIMENSIONS:
        completed[f"{name}_{abbreviation}_0_to_3"] = ratings[name]
        for span_number, quote in enumerate(evidence[name], start=1):
            start = description.index(quote)
            end = start + len(quote)
            prefix = f"{name}_{abbreviation}_evidence_span_{span_number}"
            completed[f"{prefix}_source_field"] = "DESCRIPTION"
            completed[f"{prefix}_start_0_based_inclusive"] = start
            completed[f"{prefix}_end_0_based_exclusive"] = end
            completed[f"{prefix}_exact_quote"] = quote
        completed[f"{name}_{abbreviation}_rationale_one_sentence"] = (
            "Demonstration only; apply the operational anchor to the exact quoted text."
        )
    completed.update(
        {
            "audit_attention_only": 0,
            "procedure_language_intrusion": 0,
            "negation_or_resolution": 0,
            "insufficient_context": 0,
            "unable_to_code": 0,
            "confidence": "high",
            "reviewer_note": (
                "Demonstration: exact quotes and zero-based half-open offsets are "
                "illustrative, not ground truth."
            ),
        }
    )
    input_path = output_dir / "CAM_validation_worked_example_INPUT_PRIVATE.csv"
    output_path = output_dir / "CAM_validation_worked_example_OUTPUT_PRIVATE.csv"
    _atomic_csv(input_path, fields, [blank])
    _atomic_csv(output_path, fields, [completed])
    return {
        "input": {"filename": input_path.name, "rows": 1, "sha256": file_sha256(input_path)},
        "output": {
            "filename": output_path.name,
            "rows": 1,
            "sha256": file_sha256(output_path),
        },
        "label_status": "demonstration_only_not_human_validation",
        "synthetic_not_from_cam_source": True,
    }


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _selection_checks(
    pilot: Sequence[Candidate],
    main: Sequence[Candidate],
    excluded_matter_keys: frozenset[str] = frozenset(),
) -> dict[str, object]:
    combined = list(pilot) + list(main)
    checks = {
        "pilot_matters_unique": len({c.matter_key for c in pilot}) == len(pilot),
        "main_matters_unique": len({c.matter_key for c in main}) == len(main),
        "combined_matters_unique": len({c.matter_key for c in combined}) == len(combined),
        "combined_companies_unique": len({c.company_key for c in combined}) == len(combined),
        "combined_normalized_narratives_unique": len({c.fingerprint for c in combined})
        == len(combined),
        "pilot_excluded_from_main": not ({c.matter_key for c in pilot} & {c.matter_key for c in main}),
        "pilot_size_30": len(pilot) == 30,
        "main_size_800": len(main) == 800,
        "supplied_excluded_matters_absent": not (
            excluded_matter_keys & {c.matter_key for c in combined}
        ),
    }
    if not all(checks.values()):
        raise ValidationSampleError(f"selection QA failed: {checks}")
    return checks


def _pilot_only_checks(
    pilot: Sequence[Candidate], excluded_matter_keys: frozenset[str] = frozenset()
) -> dict[str, object]:
    checks = {
        "pilot_matters_unique": len({c.matter_key for c in pilot}) == len(pilot),
        "pilot_companies_unique": len({c.company_key for c in pilot}) == len(pilot),
        "pilot_normalized_narratives_unique": len({c.fingerprint for c in pilot})
        == len(pilot),
        "pilot_size_30": len(pilot) == 30,
        "supplied_excluded_matters_absent": not (
            excluded_matter_keys & {c.matter_key for c in pilot}
        ),
    }
    if not all(checks.values()):
        raise ValidationSampleError(f"pilot selection QA failed: {checks}")
    return checks


def _write_json(path: Path, payload: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent, text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temporary, path)
        try:
            path.chmod(0o600)
        except OSError:
            pass
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cam", type=Path, required=True, help="Private CAM.csv")
    parser.add_argument(
        "--matter-account", type=Path, required=True, help="Matter-account token-risk CSV"
    )
    parser.add_argument("--profile", type=Path, required=True, help="Token-risk profile CSV")
    parser.add_argument(
        "--codebook",
        type=Path,
        help="Optional frozen annotation codebook to hash into QA provenance",
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--attempts", type=int, default=80)
    parser.add_argument(
        "--pilot-only",
        action="store_true",
        help="Build the 30-case pilot, worked example, and QA without selecting the main 800",
    )
    parser.add_argument(
        "--exclude-matter-key",
        action="append",
        default=[],
        metavar="KEY",
        help="Exclude a private CAM matter key; repeat this option for multiple keys",
    )
    return parser.parse_args(argv)


def run(args: argparse.Namespace) -> dict[str, object]:
    if args.attempts < 1:
        raise ValidationSampleError("--attempts must be positive")
    excluded_matter_keys = frozenset(
        str(key).strip() for key in args.exclude_matter_key if str(key).strip()
    )
    args.output_dir = prepare_private_output_dir(args.output_dir)
    candidates, input_qa = build_candidates(
        args.cam,
        args.matter_account,
        args.profile,
        excluded_matter_keys=excluded_matter_keys,
    )

    # The pilot is selected first and reserved. Main-sample selection therefore
    # cannot reuse any pilot matter, company, or normalized narrative.
    pilot, pilot_qa = select_with_quotas(
        candidates,
        pilot_quotas(),
        seed=args.seed,
        phase="pilot",
        year_mode="global",
        attempts=args.attempts,
    )
    if args.pilot_only:
        main: list[Candidate] = []
        main_qa: dict[str, object] = {
            "status": "not_built_pilot_only",
            "selected_total": 0,
        }
        invariant_checks = _pilot_only_checks(pilot, excluded_matter_keys)
    else:
        main, main_qa = select_with_quotas(
            candidates,
            main_quotas(),
            seed=args.seed,
            phase="main",
            reserved=pilot,
            year_mode="per_stratum",
            attempts=args.attempts,
        )
        invariant_checks = _selection_checks(pilot, main, excluded_matter_keys)

    output_files: dict[str, object] = {}
    phases: list[tuple[str, Sequence[Candidate]]] = [("pilot", pilot)]
    if not args.pilot_only:
        phases.append(("main", main))
    for phase, selected in phases:
        reviewer_meta, row_maps = write_reviewer_files(
            selected, args.output_dir, phase, args.seed
        )
        key_path = write_private_key(
            selected, args.output_dir, phase, args.seed, row_maps
        )
        adjudication_path = write_adjudication_template(
            selected, args.output_dir, phase, args.seed
        )
        output_files[phase] = {
            "reviewer_files": reviewer_meta,
            "private_key": {
                "filename": key_path.name,
                "rows": len(selected),
                "sha256": file_sha256(key_path),
                "contains_raw_title_or_description": False,
            },
            "adjudication": {
                "filename": adjudication_path.name,
                "rows": len(selected) * len(DIMENSIONS),
                "sha256": file_sha256(adjudication_path),
            },
        }
    output_files["worked_example"] = write_worked_example(args.output_dir)

    qa = {
        "artifact": "CAM narrative human-validation sampling package",
        "sampler_version": SAMPLER_VERSION,
        "sampler_script_sha256": file_sha256(Path(__file__).resolve()),
        "protocol_id": PROTOCOL_ID,
        "codebook_version": CODEBOOK_VERSION,
        "codebook_sha256": file_sha256(args.codebook) if args.codebook else None,
        "run_mode": "pilot_only" if args.pilot_only else "pilot_and_main",
        "selection_seed": args.seed,
        "construct_status": "post_selection_descriptive_proxy",
        "labels_are_ground_truth": False,
        "source_text_fields_exposed_to_reviewers": ["TITLE", "DESCRIPTION"],
        "response_text_exposed_to_reviewers": False,
        "inputs": {
            "cam": {"path": str(args.cam), "sha256": file_sha256(args.cam)},
            "matter_account": {
                "path": str(args.matter_account),
                "sha256": file_sha256(args.matter_account),
            },
            "profile": {"path": str(args.profile), "sha256": file_sha256(args.profile)},
            "codebook": {
                "path": str(args.codebook) if args.codebook else None,
                "sha256": file_sha256(args.codebook) if args.codebook else None,
            },
        },
        "input_validation": input_qa,
        "pilot": pilot_qa,
        "main": main_qa,
        "invariant_checks": invariant_checks,
        "outputs": output_files,
    }
    qa_path = args.output_dir / "CAM_validation_sampling_QA_PRIVATE.json"
    _write_json(qa_path, qa)
    qa["qa_file"] = {
        "filename": qa_path.name,
        "sha256": file_sha256(qa_path),
    }
    return qa


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    qa = run(args)
    print(
        json.dumps(
            {
                "pilot_selected": qa["pilot"]["selected_total"],
                "main_selected": qa["main"]["selected_total"],
                "output_dir": str(args.output_dir),
                "qa_file": qa["qa_file"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
