"""Build a DARWIN-aligned, post-selection CAM token-language proxy.

The source contains already-selected critical audit matters.  This module
therefore describes narrative risk language among observed CAMs; it does not
estimate independent account risk or the probability that an account becomes
a CAM.  It creates no CAM-absent observations.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable, Mapping, Sequence


CONSTRUCT_STATUS = "post_selection_descriptive_proxy"
INDUSTRY_STATUS = "current_snapshot_not_historical"
COMPETITION_SCOPE = "observed_selected_CAM_accounts_only"
COMPETITION_COMPLETENESS = (
    "incomplete_selected_CAM_accounts_only_absent_and_unmapped_accounts_unknown"
)
MIN_DISTINCT_COMPANIES = 20
PEER_QUANTILE = 0.70
MIN_FISCAL_YEAR = 2010
MAX_FISCAL_YEAR = 2025
CANONICAL_ACCOUNT_DOMAINS = {
    "REV",
    "INV",
    "REC",
    "GW",
    "TAX",
    "LEASE",
    "FIN",
    "PROV",
    "PPE",
    "INT",
    "EQ",
    "IT",
    "OTHER",
}

PROFILE_REQUIRED = {
    "critical_audit_matter_key",
    "audit_opinion_fkey",
    "company_key",
    "source_topic",
    "account_domains",
    "mapping_status",
    "mapping_version",
    "title_tokens",
    "title_risk_language_hits",
    "description_tokens",
    "description_risk_language_hits",
    "response_tokens",
    "response_risk_language_hits",
    "normalized_narrative_sha256",
}
CAM_REQUIRED = {
    "CRITICAL_AUDIT_MATTER_KEY",
    "COMPANY_KEY",
    "AUDIT_OPINION_FKEY",
    "SIC_CODE_FKEY",
}
DATE_REQUIRED = {
    "COMPANY_KEY",
    "AUDIT_OPINION_FKEY",
    "FYE_YEAR",
    "FYE_DATE",
    "DATE_VERIFIED",
    "date_status",
    "formap_mapping_status",
}
SIC_RE = re.compile(r"^(\d+)(?:\.0+)?$")
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_expected_sha256(value: str) -> str:
    if not SHA256_RE.fullmatch(value):
        raise ValueError("Expected source SHA-256 must be exactly 64 hexadecimal characters.")
    return value.lower()


def prepare_private_output_dir(path: Path) -> Path:
    """Create a new owner-only output directory outside every Git tree."""

    resolved = path.expanduser().resolve()
    if resolved.exists():
        raise ValueError("Private output directory must be new.")
    git_markers = (parent / ".git" for parent in resolved.parents)
    if any(
        marker.is_file() or (marker.is_dir() and (marker / "HEAD").is_file())
        for marker in git_markers
    ):
        raise ValueError("Private output directory must be outside a Git working tree.")
    resolved.mkdir(parents=True, mode=0o700)
    return resolved


def require_columns(fieldnames: Sequence[str] | None, required: set[str], label: str) -> None:
    present = set(fieldnames or ())
    missing = required - present
    if missing:
        raise ValueError(f"{label} is missing required columns: {sorted(missing)}")


def parse_nonnegative_int(value: str, field: str) -> int:
    try:
        result = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be an integer.") from exc
    if result < 0:
        raise ValueError(f"{field} must be nonnegative.")
    return result


def safe_density(hits: int, tokens: int) -> float | None:
    if tokens <= 0:
        return None
    return hits * 1000.0 / tokens


def linear_quantile(values: Iterable[float], quantile: float) -> float:
    """Return the type-7/NumPy-default linear quantile."""

    ordered = sorted(float(value) for value in values)
    if not ordered:
        raise ValueError("Cannot calculate a quantile for an empty collection.")
    if not 0.0 <= quantile <= 1.0:
        raise ValueError("Quantile must be between zero and one.")
    position = (len(ordered) - 1) * quantile
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] + weight * (ordered[upper] - ordered[lower])


def normalize_sic(raw: str | None) -> tuple[str, str]:
    value = (raw or "").strip()
    match = SIC_RE.fullmatch(value)
    if not match:
        return "", ""
    digits = match.group(1)
    if len(digits) > 4:
        return "", ""
    sic4 = digits.zfill(4)
    return sic4, sic4[:2]


def split_account_domains(raw: str) -> tuple[str, ...]:
    domains = tuple(part.strip() for part in raw.split("|") if part.strip())
    if not domains:
        raise ValueError("Account-domain assignment is blank.")
    if len(domains) != len(set(domains)):
        raise ValueError("An account-domain assignment contains duplicates.")
    invalid = set(domains) - CANONICAL_ACCOUNT_DOMAINS - {"UNMAPPED"}
    if invalid:
        raise ValueError("An account-domain assignment is unrecognized.")
    if "UNMAPPED" in domains and len(domains) != 1:
        raise ValueError("UNMAPPED cannot be combined with a canonical account domain.")
    return domains


def parse_fiscal_year(raw: str | None) -> int | None:
    value = (raw or "").strip()
    if not value:
        return None
    try:
        year = int(value)
    except ValueError:
        return None
    return year


def matrix_state(token_proxy_risk_level: str) -> str:
    """ICFR is U and CAM is present for every output row."""

    return {"H": "A3", "L": "C3", "U": "U5"}[token_proxy_risk_level]


def eligibility_reason(row: Mapping[str, object]) -> str:
    account = str(row["account_domain"])
    year = row["fiscal_year"]
    if account == "UNMAPPED":
        return "U_account_unmapped"
    if account not in CANONICAL_ACCOUNT_DOMAINS:
        return "U_account_not_canonical"
    if year in (None, ""):
        return "U_fiscal_year_unavailable"
    if not isinstance(year, int) or not MIN_FISCAL_YEAR <= year <= MAX_FISCAL_YEAR:
        return "U_fiscal_year_outside_2010_2025"
    if not row["current_sic2"]:
        return "U_current_sic2_unavailable"
    if not row["cam_narrative_risk_language_density_per_1000_tokens"] and int(
        row["title_description_tokens"]
    ) == 0:
        return "U_no_title_description_tokens"
    return "candidate_for_peer_threshold"


def write_csv(path: Path, rows: Sequence[Mapping[str, object]]) -> None:
    if not rows:
        raise ValueError("Refusing to write an empty private output.")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def read_cam_snapshot(path: Path) -> tuple[dict[str, dict[str, str]], int]:
    result: dict[str, dict[str, str]] = {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        require_columns(reader.fieldnames, CAM_REQUIRED, "CAM source")
        for row in reader:
            matter = row["CRITICAL_AUDIT_MATTER_KEY"].strip()
            if not matter or matter in result:
                raise ValueError("CAM matter keys must be nonblank and unique.")
            sic4, sic2 = normalize_sic(row["SIC_CODE_FKEY"])
            result[matter] = {
                "company_key": row["COMPANY_KEY"].strip(),
                "audit_opinion_fkey": row["AUDIT_OPINION_FKEY"].strip(),
                "current_sic": sic4,
                "current_sic2": sic2,
            }
        columns = len(reader.fieldnames or ())
    return result, columns


def read_dates(path: Path) -> dict[tuple[str, str], dict[str, str]]:
    result: dict[tuple[str, str], dict[str, str]] = {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        require_columns(reader.fieldnames, DATE_REQUIRED, "opinion-year crosswalk")
        for row in reader:
            key = (row["COMPANY_KEY"].strip(), row["AUDIT_OPINION_FKEY"].strip())
            if not all(key) or key in result:
                raise ValueError("Opinion-year keys must be nonblank and unique.")
            result[key] = {name: row[name].strip() for name in DATE_REQUIRED}
    return result


def read_profile(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        require_columns(reader.fieldnames, PROFILE_REQUIRED, "token profile")
        for row in reader:
            matter = row["critical_audit_matter_key"].strip()
            if not matter or matter in seen:
                raise ValueError("Token-profile CAM matter keys must be nonblank and unique.")
            seen.add(matter)
            rows.append(row)
    return rows


def build_matter_account_rows(
    profile_rows: Sequence[Mapping[str, str]],
    cam_snapshot: Mapping[str, Mapping[str, str]],
    date_rows: Mapping[tuple[str, str], Mapping[str, str]],
) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    if set(cam_snapshot) != {row["critical_audit_matter_key"].strip() for row in profile_rows}:
        raise ValueError("CAM source and token profile do not contain the same matter keys.")

    for profile in profile_rows:
        matter = profile["critical_audit_matter_key"].strip()
        snapshot = cam_snapshot[matter]
        company = profile["company_key"].strip()
        opinion = profile["audit_opinion_fkey"].strip()
        if company != snapshot["company_key"] or opinion != snapshot["audit_opinion_fkey"]:
            raise ValueError("A CAM matter has inconsistent identifiers across private inputs.")

        title_tokens = parse_nonnegative_int(profile["title_tokens"], "title_tokens")
        description_tokens = parse_nonnegative_int(
            profile["description_tokens"], "description_tokens"
        )
        narrative_tokens = title_tokens + description_tokens
        narrative_hits = parse_nonnegative_int(
            profile["title_risk_language_hits"], "title_risk_language_hits"
        ) + parse_nonnegative_int(
            profile["description_risk_language_hits"],
            "description_risk_language_hits",
        )
        response_tokens = parse_nonnegative_int(profile["response_tokens"], "response_tokens")
        response_hits = parse_nonnegative_int(
            profile["response_risk_language_hits"], "response_risk_language_hits"
        )
        narrative_density = safe_density(narrative_hits, narrative_tokens)
        response_density = safe_density(response_hits, response_tokens)

        date = date_rows.get((company, opinion))
        fiscal_year = parse_fiscal_year(date["FYE_YEAR"]) if date else None
        if date and date["FYE_YEAR"] and fiscal_year is None:
            raise ValueError("A private opinion-year row has an invalid FYE_YEAR.")
        fiscal_year_status = (
            "provisional_opinion_year_crosswalk"
            if fiscal_year is not None
            else "unavailable_no_provisional_opinion_year_link"
        )

        for account in split_account_domains(profile["account_domains"]):
            result.append(
                {
                    "critical_audit_matter_key": matter,
                    "company_key": company,
                    "audit_opinion_fkey": opinion,
                    "source_topic": profile["source_topic"],
                    "account_domain": account,
                    "account_mapping_status": profile["mapping_status"],
                    "account_mapping_version": profile["mapping_version"],
                    "current_sic": snapshot["current_sic"],
                    "current_sic2": snapshot["current_sic2"],
                    "industry_status": INDUSTRY_STATUS,
                    "fiscal_year": fiscal_year if fiscal_year is not None else "",
                    "fiscal_year_status": fiscal_year_status,
                    "fye_date_provisional": date["FYE_DATE"] if date else "",
                    "opinion_year_date_status": date["date_status"] if date else "",
                    "formap_mapping_status": date["formap_mapping_status"] if date else "",
                    "cam_status": "1",
                    "icfr_status": "U",
                    "construct_status": CONSTRUCT_STATUS,
                    "title_description_tokens": narrative_tokens,
                    "title_description_risk_language_hits": narrative_hits,
                    "cam_narrative_risk_language_density_per_1000_tokens": narrative_density
                    if narrative_density is not None
                    else "",
                    "auditor_response_tokens": response_tokens,
                    "auditor_response_risk_language_hits": response_hits,
                    "auditor_response_risk_language_density_per_1000_tokens": response_density
                    if response_density is not None
                    else "",
                    "normalized_narrative_sha256": profile[
                        "normalized_narrative_sha256"
                    ],
                }
            )
    return result


def aggregate_opinion_account_year(
    matter_rows: Sequence[Mapping[str, object]],
) -> tuple[list[dict[str, object]], dict[tuple[str, str, str, object], dict[str, object]]]:
    grouped: dict[tuple[str, str, str, object], dict[str, object]] = {}
    for row in matter_rows:
        key = (
            str(row["company_key"]),
            str(row["audit_opinion_fkey"]),
            str(row["account_domain"]),
            row["fiscal_year"],
        )
        if key not in grouped:
            grouped[key] = {
                "company_key": key[0],
                "audit_opinion_fkey": key[1],
                "account_domain": key[2],
                "fiscal_year": key[3],
                "matter_keys": set(),
                "topics": set(),
                "account_mapping_statuses": set(),
                "account_mapping_versions": set(),
                "current_sics": set(),
                "current_sic2s": set(),
                "fiscal_year_statuses": set(),
                "fye_dates": set(),
                "date_statuses": set(),
                "formap_statuses": set(),
                "title_description_tokens": 0,
                "title_description_risk_language_hits": 0,
                "matter_densities": [],
                "auditor_response_tokens": 0,
                "auditor_response_risk_language_hits": 0,
            }
        aggregate = grouped[key]
        aggregate["matter_keys"].add(row["critical_audit_matter_key"])
        aggregate["topics"].add(row["source_topic"])
        aggregate["account_mapping_statuses"].add(row["account_mapping_status"])
        aggregate["account_mapping_versions"].add(row["account_mapping_version"])
        if row["current_sic"]:
            aggregate["current_sics"].add(row["current_sic"])
        if row["current_sic2"]:
            aggregate["current_sic2s"].add(row["current_sic2"])
        aggregate["fiscal_year_statuses"].add(row["fiscal_year_status"])
        if row["fye_date_provisional"]:
            aggregate["fye_dates"].add(row["fye_date_provisional"])
        if row["opinion_year_date_status"]:
            aggregate["date_statuses"].add(row["opinion_year_date_status"])
        if row["formap_mapping_status"]:
            aggregate["formap_statuses"].add(row["formap_mapping_status"])
        aggregate["title_description_tokens"] += int(row["title_description_tokens"])
        aggregate["title_description_risk_language_hits"] += int(
            row["title_description_risk_language_hits"]
        )
        if row["cam_narrative_risk_language_density_per_1000_tokens"] != "":
            aggregate["matter_densities"].append(
                float(row["cam_narrative_risk_language_density_per_1000_tokens"])
            )
        aggregate["auditor_response_tokens"] += int(row["auditor_response_tokens"])
        aggregate["auditor_response_risk_language_hits"] += int(
            row["auditor_response_risk_language_hits"]
        )

    rows: list[dict[str, object]] = []
    row_by_key: dict[tuple[str, str, str, object], dict[str, object]] = {}
    for key, aggregate in sorted(grouped.items(), key=lambda item: tuple(map(str, item[0]))):
        singleton_fields = (
            "current_sics",
            "current_sic2s",
            "fiscal_year_statuses",
            "fye_dates",
            "date_statuses",
            "formap_statuses",
        )
        for field in singleton_fields:
            if len(aggregate[field]) > 1:
                raise ValueError("A private opinion-account-year contains inconsistent fields.")
        matter_densities = aggregate["matter_densities"]
        primary_density = max(matter_densities) if matter_densities else None
        pooled_density = safe_density(
            int(aggregate["title_description_risk_language_hits"]),
            int(aggregate["title_description_tokens"]),
        )
        response_density = safe_density(
            int(aggregate["auditor_response_risk_language_hits"]),
            int(aggregate["auditor_response_tokens"]),
        )
        row: dict[str, object] = {
            "company_key": key[0],
            "audit_opinion_fkey": key[1],
            "account_domain": key[2],
            "fiscal_year": key[3],
            "current_sic": next(iter(aggregate["current_sics"]), ""),
            "current_sic2": next(iter(aggregate["current_sic2s"]), ""),
            "industry_status": INDUSTRY_STATUS,
            "fiscal_year_status": next(iter(aggregate["fiscal_year_statuses"]), ""),
            "fye_date_provisional": next(iter(aggregate["fye_dates"]), ""),
            "opinion_year_date_status": next(iter(aggregate["date_statuses"]), ""),
            "formap_mapping_status": next(iter(aggregate["formap_statuses"]), ""),
            "cam_status": "1",
            "icfr_status": "U",
            "construct_status": CONSTRUCT_STATUS,
            "account_aggregation_method": "maximum_matter_level_title_description_density",
            "cam_matter_count": len(aggregate["matter_keys"]),
            "distinct_source_topics": len(aggregate["topics"]),
            "source_topics": "|".join(sorted(aggregate["topics"])),
            "account_mapping_statuses": "|".join(
                sorted(aggregate["account_mapping_statuses"])
            ),
            "account_mapping_versions": "|".join(
                sorted(aggregate["account_mapping_versions"])
            ),
            "title_description_tokens": aggregate["title_description_tokens"],
            "title_description_risk_language_hits": aggregate[
                "title_description_risk_language_hits"
            ],
            "cam_narrative_risk_language_density_per_1000_tokens": primary_density
            if primary_density is not None
            else "",
            "pooled_matter_risk_language_density_per_1000_tokens": pooled_density
            if pooled_density is not None
            else "",
            "auditor_response_tokens": aggregate["auditor_response_tokens"],
            "auditor_response_risk_language_hits": aggregate[
                "auditor_response_risk_language_hits"
            ],
            "auditor_response_risk_language_density_per_1000_tokens": response_density
            if response_density is not None
            else "",
        }
        rows.append(row)
        row_by_key[key] = row
    return rows, row_by_key


def classify_peer_groups(
    rows: Sequence[dict[str, object]],
) -> list[dict[str, object]]:
    candidate_groups: dict[tuple[str, str, int], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        reason = eligibility_reason(row)
        row["token_proxy_eligibility_status"] = reason
        if reason == "candidate_for_peer_threshold":
            key = (
                str(row["current_sic2"]),
                str(row["account_domain"]),
                int(row["fiscal_year"]),
            )
            candidate_groups[key].append(row)

    threshold_rows: list[dict[str, object]] = []
    for key, members in sorted(candidate_groups.items()):
        companies = {str(row["company_key"]) for row in members}
        distinct_companies = len(companies)
        eligible = distinct_companies >= MIN_DISTINCT_COMPANIES
        threshold = (
            linear_quantile(
                (
                    float(row["cam_narrative_risk_language_density_per_1000_tokens"])
                    for row in members
                ),
                PEER_QUANTILE,
            )
            if eligible
            else None
        )
        high_count = 0
        low_count = 0
        for row in members:
            row["peer_group_observations"] = len(members)
            row["peer_group_distinct_companies"] = distinct_companies
            row["peer_q70_threshold"] = threshold if threshold is not None else ""
            if threshold is None:
                row["token_proxy_eligibility_status"] = (
                    "U_peer_group_below_20_distinct_companies"
                )
                row["token_proxy_risk_level"] = "U"
            elif float(
                row["cam_narrative_risk_language_density_per_1000_tokens"]
            ) >= threshold:
                row["token_proxy_eligibility_status"] = "eligible_classified"
                row["token_proxy_risk_level"] = "H"
                high_count += 1
            else:
                row["token_proxy_eligibility_status"] = "eligible_classified"
                row["token_proxy_risk_level"] = "L"
                low_count += 1
        threshold_rows.append(
            {
                "current_sic2": key[0],
                "account_domain": key[1],
                "fiscal_year": key[2],
                "industry_status": INDUSTRY_STATUS,
                "construct_status": CONSTRUCT_STATUS,
                "peer_group_observations": len(members),
                "peer_group_distinct_companies": distinct_companies,
                "minimum_distinct_companies": MIN_DISTINCT_COMPANIES,
                "quantile": PEER_QUANTILE,
                "peer_q70_threshold": threshold if threshold is not None else "",
                "threshold_status": "eligible_q70_linear_ties_high"
                if eligible
                else "unverified_below_20_distinct_companies",
                "high_rows": high_count,
                "low_rows": low_count,
                "unknown_rows": 0 if eligible else len(members),
            }
        )

    for row in rows:
        if "token_proxy_risk_level" not in row:
            row["peer_group_observations"] = ""
            row["peer_group_distinct_companies"] = ""
            row["peer_q70_threshold"] = ""
            row["token_proxy_risk_level"] = "U"
        row["darwin_matrix_state"] = matrix_state(str(row["token_proxy_risk_level"]))
    return threshold_rows


def add_descriptive_competition(rows: Sequence[dict[str, object]]) -> None:
    by_firm_opinion_year: dict[tuple[str, str, int], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        row["competition_scope"] = COMPETITION_SCOPE
        row["competition_completeness_status"] = COMPETITION_COMPLETENESS
        row["observed_mapped_cam_account_count"] = ""
        row["competitor_max_proxy"] = ""
        row["higher_proxy_account_count"] = ""
        row["competitor_tail_above_peer_q70"] = ""
        row["competitor_tail_threshold_available_count"] = ""
        row["relative_proxy_distance"] = ""
        if (
            row["account_domain"] in CANONICAL_ACCOUNT_DOMAINS
            and isinstance(row["fiscal_year"], int)
            and row["cam_narrative_risk_language_density_per_1000_tokens"] != ""
        ):
            key = (
                str(row["company_key"]),
                str(row["audit_opinion_fkey"]),
                int(row["fiscal_year"]),
            )
            by_firm_opinion_year[key].append(row)

    for members in by_firm_opinion_year.values():
        accounts = {str(row["account_domain"]) for row in members}
        if len(accounts) != len(members):
            raise ValueError("Duplicate account in a company-opinion-year competition set.")
        for own in members:
            competitors = [row for row in members if row is not own]
            own["observed_mapped_cam_account_count"] = len(members)
            own["higher_proxy_account_count"] = sum(
                float(row["cam_narrative_risk_language_density_per_1000_tokens"])
                > float(own["cam_narrative_risk_language_density_per_1000_tokens"])
                for row in competitors
            )
            if competitors:
                competitor_max = max(
                    float(row["cam_narrative_risk_language_density_per_1000_tokens"])
                    for row in competitors
                )
                own["competitor_max_proxy"] = competitor_max
                own["relative_proxy_distance"] = (
                    float(own["cam_narrative_risk_language_density_per_1000_tokens"])
                    - competitor_max
                )
            tail_members = [
                row
                for row in competitors
                if row["peer_q70_threshold"] != ""
            ]
            own["competitor_tail_threshold_available_count"] = len(tail_members)
            if tail_members:
                own["competitor_tail_above_peer_q70"] = sum(
                    max(
                        float(row["cam_narrative_risk_language_density_per_1000_tokens"])
                        - float(row["peer_q70_threshold"]),
                        0.0,
                    )
                    for row in tail_members
                )


def attach_oay_fields(
    matter_rows: Sequence[dict[str, object]],
    oay_by_key: Mapping[tuple[str, str, str, object], Mapping[str, object]],
) -> None:
    names = (
        "account_aggregation_method",
        "cam_matter_count",
        "pooled_matter_risk_language_density_per_1000_tokens",
        "token_proxy_eligibility_status",
        "peer_group_observations",
        "peer_group_distinct_companies",
        "peer_q70_threshold",
        "token_proxy_risk_level",
        "darwin_matrix_state",
        "competition_scope",
        "competition_completeness_status",
        "observed_mapped_cam_account_count",
        "competitor_max_proxy",
        "higher_proxy_account_count",
        "competitor_tail_above_peer_q70",
        "competitor_tail_threshold_available_count",
        "relative_proxy_distance",
    )
    for row in matter_rows:
        key = (
            str(row["company_key"]),
            str(row["audit_opinion_fkey"]),
            str(row["account_domain"]),
            row["fiscal_year"],
        )
        oay = oay_by_key[key]
        for name in names:
            row[f"opinion_account_year_{name}"] = oay[name]


def build_count_rows(rows: Sequence[Mapping[str, object]]) -> list[dict[str, object]]:
    groups: dict[tuple[object, ...], dict[str, object]] = {}
    for row in rows:
        key = (
            row["fiscal_year"],
            row["current_sic2"],
            row["account_domain"],
            row["token_proxy_risk_level"],
            row["darwin_matrix_state"],
            row["token_proxy_eligibility_status"],
        )
        if key not in groups:
            groups[key] = {"companies": set(), "rows": 0, "matters": 0}
        groups[key]["companies"].add(row["company_key"])
        groups[key]["rows"] += 1
        groups[key]["matters"] += int(row["cam_matter_count"])
    return [
        {
            "fiscal_year": key[0],
            "current_sic2": key[1],
            "account_domain": key[2],
            "token_proxy_risk_level": key[3],
            "darwin_matrix_state": key[4],
            "token_proxy_eligibility_status": key[5],
            "construct_status": CONSTRUCT_STATUS,
            "opinion_account_year_rows": value["rows"],
            "distinct_companies": len(value["companies"]),
            "cam_matters": value["matters"],
        }
        for key, value in sorted(groups.items(), key=lambda item: tuple(map(str, item[0])))
    ]


def validate_outputs(
    matter_rows: Sequence[Mapping[str, object]],
    oay_rows: Sequence[Mapping[str, object]],
    thresholds: Sequence[Mapping[str, object]],
) -> list[str]:
    failures: list[str] = []
    if any(row["cam_status"] != "1" for row in matter_rows):
        failures.append("Every matter-account row must be CAM present.")
    if any(row["icfr_status"] != "U" for row in matter_rows):
        failures.append("ICFR must remain unknown for every matter-account row.")
    if any(row["cam_status"] != "1" for row in oay_rows):
        failures.append("Every opinion-account-year row must be CAM present.")
    if any(row["icfr_status"] != "U" for row in oay_rows):
        failures.append("ICFR must remain unknown for every opinion-account-year row.")
    if any(
        row["darwin_matrix_state"] != matrix_state(str(row["token_proxy_risk_level"]))
        for row in oay_rows
    ):
        failures.append("DARWIN state is inconsistent with proxy risk level.")
    if any(
        row["token_proxy_risk_level"] in {"H", "L"}
        and row["token_proxy_eligibility_status"] != "eligible_classified"
        for row in oay_rows
    ):
        failures.append("A classified row is not marked eligible.")
    if any(
        row["token_proxy_risk_level"] == "H"
        and float(row["cam_narrative_risk_language_density_per_1000_tokens"])
        < float(row["peer_q70_threshold"])
        for row in oay_rows
    ):
        failures.append("A high row is below its q70 threshold.")
    if any(
        row["token_proxy_risk_level"] == "L"
        and float(row["cam_narrative_risk_language_density_per_1000_tokens"])
        >= float(row["peer_q70_threshold"])
        for row in oay_rows
    ):
        failures.append("A low row is at or above its q70 threshold.")
    if any(
        row["threshold_status"] == "eligible_q70_linear_ties_high"
        and int(row["peer_group_distinct_companies"]) < MIN_DISTINCT_COMPANIES
        for row in thresholds
    ):
        failures.append("An eligible threshold group has fewer than 20 firms.")
    if any(
        row["construct_status"] != CONSTRUCT_STATUS for row in oay_rows
    ):
        failures.append("Construct status differs from the declared post-selection proxy.")
    return failures


def analyze(
    cam_path: Path,
    profile_path: Path,
    date_path: Path,
    output_dir: Path,
    expected_cam_sha256: str,
) -> dict[str, object]:
    expected_digest = validate_expected_sha256(expected_cam_sha256)
    cam_digest = file_sha256(cam_path)
    if cam_digest != expected_digest:
        raise ValueError(
            "CAM source SHA-256 differs from the verified private source; review provenance."
        )
    profile_digest = file_sha256(profile_path)
    date_digest = file_sha256(date_path)
    cam_snapshot, source_columns = read_cam_snapshot(cam_path)
    dates = read_dates(date_path)
    profile = read_profile(profile_path)
    matter_rows = build_matter_account_rows(profile, cam_snapshot, dates)
    oay_rows, oay_by_key = aggregate_opinion_account_year(matter_rows)
    threshold_rows = classify_peer_groups(oay_rows)
    add_descriptive_competition(oay_rows)
    attach_oay_fields(matter_rows, oay_by_key)
    count_rows = build_count_rows(oay_rows)
    failures = validate_outputs(matter_rows, oay_rows, threshold_rows)
    if failures:
        raise ValueError("Output validation failed: " + " ".join(failures))

    output_dir = prepare_private_output_dir(output_dir)
    write_csv(output_dir / "CAM_token_risk_matter_account_PRIVATE.csv", matter_rows)
    write_csv(
        output_dir / "CAM_token_risk_opinion_account_year_PRIVATE.csv", oay_rows
    )
    write_csv(output_dir / "CAM_token_risk_peer_thresholds_PRIVATE.csv", threshold_rows)
    write_csv(output_dir / "CAM_token_risk_DARWIN_counts_PRIVATE.csv", count_rows)

    levels = Counter(str(row["token_proxy_risk_level"]) for row in oay_rows)
    states = Counter(str(row["darwin_matrix_state"]) for row in oay_rows)
    eligibility = Counter(str(row["token_proxy_eligibility_status"]) for row in oay_rows)
    year_linked_matters = {
        str(row["critical_audit_matter_key"])
        for row in matter_rows
        if row["fiscal_year"] != ""
    }
    mapped_matters = {
        str(row["critical_audit_matter_key"])
        for row in matter_rows
        if row["account_domain"] != "UNMAPPED"
    }
    eligible_thresholds = [
        row
        for row in threshold_rows
        if row["threshold_status"] == "eligible_q70_linear_ties_high"
    ]
    qa: dict[str, object] = {
        "method": "DARWIN_post_selection_CAM_narrative_proxy_v1",
        "construct_status": CONSTRUCT_STATUS,
        "interpretation": (
            "Risk-language density in already-selected CAM titles and descriptions; "
            "not independent account risk, CAM probability, ICFR evidence, or causal evidence."
        ),
        "source_cam_sha256": cam_digest,
        "source_token_profile_sha256": profile_digest,
        "source_opinion_year_crosswalk_sha256": date_digest,
        "source_cam_columns": source_columns,
        "source_cam_matters": len(cam_snapshot),
        "token_profile_matters": len(profile),
        "expanded_matter_account_rows": len(matter_rows),
        "mapped_source_matters": len(mapped_matters),
        "unmapped_source_matters": len(cam_snapshot) - len(mapped_matters),
        "matters_with_provisional_fiscal_year": len(year_linked_matters),
        "matters_without_provisional_fiscal_year": len(cam_snapshot)
        - len(year_linked_matters),
        "opinion_account_year_rows": len(oay_rows),
        "peer_groups_with_candidate_rows": len(threshold_rows),
        "eligible_peer_groups": len(eligible_thresholds),
        "ineligible_peer_groups": len(threshold_rows) - len(eligible_thresholds),
        "minimum_distinct_companies": MIN_DISTINCT_COMPANIES,
        "peer_quantile": PEER_QUANTILE,
        "quantile_method": "linear_type7_ties_at_or_above_are_H",
        "account_aggregation_method": "maximum_matter_level_title_description_density",
        "risk_level_counts": dict(sorted(levels.items())),
        "darwin_matrix_state_counts": dict(sorted(states.items())),
        "eligibility_status_counts": dict(sorted(eligibility.items())),
        "all_cam_status_present": all(row["cam_status"] == "1" for row in oay_rows),
        "all_icfr_status_unknown": all(row["icfr_status"] == "U" for row in oay_rows),
        "industry_status": INDUSTRY_STATUS,
        "competition_scope": COMPETITION_SCOPE,
        "competition_completeness_status": COMPETITION_COMPLETENESS,
        "competition_metrics_are_canonical_DARWIN_measures": False,
        "response_metric_role": (
            "separate auditor-response language diagnostic; excluded from proxy and threshold"
        ),
        "cam_absent_rows_created": 0,
        "raw_narrative_text_exported": False,
        "validation_failures": failures,
        "private_outputs": [
            "CAM_token_risk_matter_account_PRIVATE.csv",
            "CAM_token_risk_opinion_account_year_PRIVATE.csv",
            "CAM_token_risk_peer_thresholds_PRIVATE.csv",
            "CAM_token_risk_DARWIN_counts_PRIVATE.csv",
        ],
    }
    (output_dir / "CAM_token_risk_DARWIN_QA.json").write_text(
        json.dumps(qa, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return qa


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cam", type=Path, required=True)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--opinion-year-crosswalk", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--expected-cam-sha256", required=True)
    args = parser.parse_args()
    analyze(
        args.cam,
        args.profile,
        args.opinion_year_crosswalk,
        args.out,
        args.expected_cam_sha256,
    )
    print("Private DARWIN token-risk proxy completed.")


if __name__ == "__main__":
    main()
