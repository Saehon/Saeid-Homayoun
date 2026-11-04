"""Deterministic narrative indicators for the private CAM source.

The output describes language in already-selected CAM narratives. It is a
transparent companion to an NLP model, not an independent account-risk
measure, a probability of misstatement, or evidence that an unmentioned
account was CAM-absent.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import tokenizers
from tokenizers import Regex as HFRegex
from tokenizers import normalizers as hf_normalizers
from tokenizers import pre_tokenizers as hf_pre_tokenizers


TEXT_FIELDS = ("TITLE", "DESCRIPTION", "RESPONSE")
CONSTRUCT_STATUS = "post_selection_descriptive_proxy"
CANONICAL_ACCOUNT_DOMAINS = (
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
)
IDENTIFIER_FIELDS = (
    "CRITICAL_AUDIT_MATTER_KEY",
    "AUDIT_OPINION_FKEY",
    "COMPANY_KEY",
    "TOPIC_NAME",
)

# Terms are intentionally compact and reviewable. Categories distinguish
# risk-oriented wording from audit attention and procedures. They are not
# weights for a predictive or causal risk score.
LEXICON: Mapping[str, tuple[str, ...]] = {
    "estimation_uncertainty": (
        "estimation uncertainty",
        "significant estimate",
        "significant estimates",
        "uncertainty",
        "uncertain",
        "subjective",
        "judgment",
        "judgement",
        "assumption",
        "assumptions",
        "sensitivity",
    ),
    "adverse_outcome": (
        "material weakness",
        "going concern",
        "credit loss",
        "credit losses",
        "write down",
        "write downs",
        "write off",
        "write offs",
        "impairment",
        "impaired",
        "obsolete",
        "obsolescence",
        "default",
        "defaults",
        "delinquent",
        "litigation",
        "contingency",
        "contingencies",
        "misstatement",
        "misstatements",
        "fraud",
        "error",
        "errors",
    ),
    "valuation_complexity": (
        "discount rate",
        "discount rates",
        "terminal growth",
        "fair value",
        "valuation model",
        "valuation models",
        "complex",
        "complexity",
        "methodology",
        "methodologies",
        "model",
        "models",
    ),
    "forward_looking": (
        "future cash flow",
        "future cash flows",
        "future demand",
        "forecast",
        "forecasts",
        "forecasted",
        "forecasting",
        "projection",
        "projections",
        "projected",
        "macroeconomic",
        "market conditions",
        "volatility",
    ),
    "audit_attention": (
        "higher degree of auditor judgment",
        "significant auditor judgment",
        "subjective auditor judgment",
        "auditor judgment",
        "especially challenging",
        "specialized skill",
        "specialized skills",
        "specialized knowledge",
        "specialist",
        "specialists",
    ),
    "control_and_procedure": (
        "internal control",
        "internal controls",
        "operating effectiveness",
        "control deficiency",
        "control deficiencies",
        "information technology",
        "tested",
        "testing",
        "procedure",
        "procedures",
        "design",
    ),
}

RISK_LANGUAGE_CATEGORIES = (
    "estimation_uncertainty",
    "adverse_outcome",
    "valuation_complexity",
    "forward_looking",
)
TOKEN_RE = re.compile(r"[^\W_]+(?:'[^\W_]+)?", flags=re.UNICODE)
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")
HF_COMPONENT = (
    "tokenizers.normalizers.Sequence(NFKC,Lowercase,Replace)"
    "+tokenizers.pre_tokenizers.Split"
)
HF_COMPONENT_VERSION = tokenizers.__version__
HF_PRETRAINED_MODEL_INFERENCE_EXECUTED = False
HF_NORMALIZER = hf_normalizers.Sequence(
    [
        hf_normalizers.NFKC(),
        hf_normalizers.Lowercase(),
        hf_normalizers.Replace(HFRegex("[\u2018\u2019]"), "'"),
        hf_normalizers.Replace(HFRegex("[-\u2010\u2011\u2012\u2013\u2014\u2212]+"), " "),
    ]
)
HF_PRE_TOKENIZER = hf_pre_tokenizers.Split(
    HFRegex(r"(?:[^\w']|_)+"), behavior="removed"
)
HF_OUTPUT_METADATA: Mapping[str, str] = {
    "hf_component": HF_COMPONENT,
    "hf_component_version": HF_COMPONENT_VERSION,
    "hf_pretrained_model_inference_executed": "false",
}


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


def normalize_tokens(value: str | None) -> tuple[str, ...]:
    """Return reproducible local tokens through Hugging Face tokenizers."""

    normalized = HF_NORMALIZER.normalize_str(html.unescape(value or ""))
    tokens: list[str] = []
    for segment, _ in HF_PRE_TOKENIZER.pre_tokenize_str(normalized):
        # Split supplies local Unicode segmentation; this final extraction
        # retains possessives while excluding punctuation-only segments.
        tokens.extend(TOKEN_RE.findall(segment))
    return tuple(tokens)


def add_hf_metadata(target: dict[str, object]) -> None:
    target.update(HF_OUTPUT_METADATA)


def normalized_fingerprint(field_tokens: Mapping[str, Sequence[str]]) -> str:
    payload = "\x1e".join(" ".join(field_tokens[field]) for field in TEXT_FIELDS)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def compile_lexicon(
    lexicon: Mapping[str, Iterable[str]] = LEXICON,
) -> dict[str, tuple[tuple[tuple[str, ...], str, str], ...]]:
    """Index phrases by first token, longest-first, with duplicate checks."""

    indexed: dict[str, list[tuple[tuple[str, ...], str, str]]] = defaultdict(list)
    seen: dict[tuple[str, ...], str] = {}
    for category, terms in lexicon.items():
        for term in terms:
            tokens = normalize_tokens(term)
            if not tokens:
                raise ValueError(f"Lexicon term has no tokens: {term!r}")
            if tokens in seen:
                raise ValueError(
                    f"Duplicate normalized lexicon term {term!r} in "
                    f"{category!r} and {seen[tokens]!r}"
                )
            seen[tokens] = category
            indexed[tokens[0]].append((tokens, category, " ".join(tokens)))
    return {
        first: tuple(sorted(items, key=lambda x: (-len(x[0]), x[1], x[2])))
        for first, items in indexed.items()
    }


COMPILED_LEXICON = compile_lexicon()


def scan_tokens(
    tokens: Sequence[str],
    compiled: Mapping[str, Sequence[tuple[tuple[str, ...], str, str]]] = COMPILED_LEXICON,
) -> tuple[Counter[str], Counter[str]]:
    """Count non-overlapping lexicon matches using deterministic longest match."""

    categories: Counter[str] = Counter()
    terms: Counter[str] = Counter()
    position = 0
    while position < len(tokens):
        match = None
        for candidate in compiled.get(tokens[position], ()):  # longest first
            phrase, _, _ = candidate
            if tuple(tokens[position : position + len(phrase)]) == phrase:
                match = candidate
                break
        if match is None:
            position += 1
            continue
        phrase, category, term = match
        categories[category] += 1
        terms[f"{category}:{term}"] += 1
        position += len(phrase)
    return categories, terms


def safe_density(hits: int | float, tokens: int | float) -> float:
    return 0.0 if not tokens else float(hits) * 1000.0 / float(tokens)


def load_crosswalk(path: Path) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {"source_topic", "account_domains", "mapping_status", "mapping_version"}
    if not rows or not required.issubset(rows[0]):
        raise ValueError("Crosswalk does not have the expected controlled-topic fields.")
    topics = [row["source_topic"] for row in rows]
    if len(topics) != len(set(topics)):
        raise ValueError("Crosswalk contains duplicate source topics.")
    return {row["source_topic"]: row for row in rows}


def add_metric_fields(target: dict[str, object], categories: Counter[str]) -> None:
    for category in LEXICON:
        target[f"{category}_hits"] = int(categories[category])
    target["risk_language_hits"] = int(
        sum(categories[name] for name in RISK_LANGUAGE_CATEGORIES)
    )
    target["all_indicator_hits"] = int(sum(categories.values()))


def profile_record(
    row: Mapping[str, str], crosswalk_row: Mapping[str, str]
) -> tuple[dict[str, object], Counter[str]]:
    field_tokens = {field: normalize_tokens(row.get(field, "")) for field in TEXT_FIELDS}
    category_hits: Counter[str] = Counter()
    term_hits: Counter[str] = Counter()
    field_category_hits: dict[str, Counter[str]] = {}
    for field in TEXT_FIELDS:
        categories, terms = scan_tokens(field_tokens[field])
        field_category_hits[field] = categories
        category_hits.update(categories)
        term_hits.update(terms)

    result: dict[str, object] = {
        "critical_audit_matter_key": row["CRITICAL_AUDIT_MATTER_KEY"],
        "audit_opinion_fkey": row["AUDIT_OPINION_FKEY"],
        "company_key": row["COMPANY_KEY"],
        "source_topic": row["TOPIC_NAME"],
        "account_domains": crosswalk_row["account_domains"],
        "mapping_status": crosswalk_row["mapping_status"],
        "mapping_version": crosswalk_row["mapping_version"],
        "cam_status": "1",
        "icfr_status": "U",
        "construct_status": CONSTRUCT_STATUS,
        "risk_independent_eligible": "false",
    }
    total_tokens = 0
    for field in TEXT_FIELDS:
        count = len(field_tokens[field])
        total_tokens += count
        field_name = field.lower()
        result[f"{field_name}_missing"] = not bool((row.get(field) or "").strip())
        result[f"{field_name}_tokens"] = count
        for category in LEXICON:
            result[f"{field_name}_{category}_hits"] = int(
                field_category_hits[field][category]
            )
        field_risk_hits = sum(
            field_category_hits[field][name] for name in RISK_LANGUAGE_CATEGORIES
        )
        field_all_hits = sum(field_category_hits[field].values())
        result[f"{field_name}_risk_language_hits"] = int(field_risk_hits)
        result[f"{field_name}_all_indicator_hits"] = int(field_all_hits)
        result[f"{field_name}_risk_language_density_per_1000_tokens"] = safe_density(
            field_risk_hits, count
        )
        result[f"{field_name}_all_indicator_density_per_1000_tokens"] = safe_density(
            field_all_hits, count
        )
    result["total_tokens"] = total_tokens
    result["title_description_tokens"] = int(result["title_tokens"]) + int(
        result["description_tokens"]
    )
    result["title_description_risk_language_hits"] = int(
        result["title_risk_language_hits"]
    ) + int(result["description_risk_language_hits"])
    result["cam_narrative_risk_language_density_per_1000_tokens"] = safe_density(
        int(result["title_description_risk_language_hits"]),
        int(result["title_description_tokens"]),
    )
    result["text_fields_present"] = sum(
        not bool(result[f"{field.lower()}_missing"]) for field in TEXT_FIELDS
    )
    result["all_text_missing"] = result["text_fields_present"] == 0
    add_metric_fields(result, category_hits)
    result["risk_language_density_per_1000_tokens"] = safe_density(
        int(result["risk_language_hits"]), total_tokens
    )
    result["all_indicator_density_per_1000_tokens"] = safe_density(
        int(result["all_indicator_hits"]), total_tokens
    )
    result["normalized_narrative_sha256"] = normalized_fingerprint(field_tokens)
    add_hf_metadata(result)
    return result, term_hits


def new_aggregate() -> dict[str, object]:
    result: dict[str, object] = {
        "cam_records": 0,
        "companies": set(),
        "audit_opinions": set(),
        "source_topics": set(),
        "narrative_fingerprints": set(),
        "title_missing_records": 0,
        "description_missing_records": 0,
        "response_missing_records": 0,
        "all_text_missing_records": 0,
        "total_tokens": 0,
    }
    for field in TEXT_FIELDS:
        field_name = field.lower()
        result[f"{field_name}_tokens"] = 0
        result[f"{field_name}_risk_language_hits"] = 0
        result[f"{field_name}_all_indicator_hits"] = 0
    for category in LEXICON:
        result[f"{category}_hits"] = 0
    result["risk_language_hits"] = 0
    result["all_indicator_hits"] = 0
    return result


def update_aggregate(aggregate: dict[str, object], row: Mapping[str, object]) -> None:
    aggregate["cam_records"] = int(aggregate["cam_records"]) + 1
    aggregate["companies"].add(row["company_key"])
    aggregate["audit_opinions"].add(row["audit_opinion_fkey"])
    aggregate["source_topics"].add(row["source_topic"])
    aggregate["narrative_fingerprints"].add(row["normalized_narrative_sha256"])
    for field in TEXT_FIELDS:
        name = f"{field.lower()}_missing_records"
        aggregate[name] = int(aggregate[name]) + int(bool(row[f"{field.lower()}_missing"]))
    aggregate["all_text_missing_records"] = int(
        aggregate["all_text_missing_records"]
    ) + int(bool(row["all_text_missing"]))
    aggregate["total_tokens"] = int(aggregate["total_tokens"]) + int(row["total_tokens"])
    for field in TEXT_FIELDS:
        field_name = field.lower()
        for suffix in ("tokens", "risk_language_hits", "all_indicator_hits"):
            name = f"{field_name}_{suffix}"
            aggregate[name] = int(aggregate[name]) + int(row[name])
    for category in LEXICON:
        name = f"{category}_hits"
        aggregate[name] = int(aggregate[name]) + int(row[name])
    for name in ("risk_language_hits", "all_indicator_hits"):
        aggregate[name] = int(aggregate[name]) + int(row[name])


def flatten_aggregate(group_fields: Mapping[str, str], aggregate: dict[str, object]) -> dict[str, object]:
    result: dict[str, object] = dict(group_fields)
    for name, value in aggregate.items():
        if isinstance(value, set):
            result[f"distinct_{name}"] = len(value)
        else:
            result[name] = value
    result["risk_language_density_per_1000_tokens"] = safe_density(
        int(result["risk_language_hits"]), int(result["total_tokens"])
    )
    result["all_indicator_density_per_1000_tokens"] = safe_density(
        int(result["all_indicator_hits"]), int(result["total_tokens"])
    )
    for field in TEXT_FIELDS:
        field_name = field.lower()
        result[f"{field_name}_risk_language_density_per_1000_tokens"] = safe_density(
            int(result[f"{field_name}_risk_language_hits"]),
            int(result[f"{field_name}_tokens"]),
        )
        result[f"{field_name}_all_indicator_density_per_1000_tokens"] = safe_density(
            int(result[f"{field_name}_all_indicator_hits"]),
            int(result[f"{field_name}_tokens"]),
        )
    add_hf_metadata(result)
    return result


def write_csv(path: Path, rows: Sequence[Mapping[str, object]]) -> None:
    if not rows:
        raise ValueError("Refusing to write an empty private output.")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def analyze(
    cam_path: Path,
    crosswalk_path: Path,
    output_dir: Path,
    expected_cam_sha256: str,
) -> dict[str, object]:
    expected_digest = validate_expected_sha256(expected_cam_sha256)
    digest = file_sha256(cam_path)
    if digest != expected_digest:
        raise ValueError(
            "CAM source SHA-256 differs from the verified private source; "
            "review provenance before profiling."
        )
    crosswalk = load_crosswalk(crosswalk_path)

    rows: list[dict[str, object]] = []
    term_totals: Counter[str] = Counter()
    seen_keys: set[str] = set()
    source_topics: set[str] = set()
    source_columns: list[str] = []
    with cam_path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        source_columns = list(reader.fieldnames or ())
        required = set(IDENTIFIER_FIELDS) | set(TEXT_FIELDS)
        if not required.issubset(source_columns):
            raise ValueError(f"CAM source is missing required fields: {sorted(required-set(source_columns))}")
        for source_row in reader:
            key = source_row["CRITICAL_AUDIT_MATTER_KEY"].strip()
            if not key or key in seen_keys:
                raise ValueError("CAM matter keys must be nonblank and unique.")
            seen_keys.add(key)
            topic = source_row["TOPIC_NAME"]
            source_topics.add(topic)
            if topic not in crosswalk:
                raise ValueError("A source topic is missing from the controlled crosswalk.")
            row, term_hits = profile_record(source_row, crosswalk[topic])
            rows.append(row)
            term_totals.update(term_hits)
    unused_crosswalk_topics = set(crosswalk) - source_topics
    if unused_crosswalk_topics:
        raise ValueError("The crosswalk contains topics absent from the private source.")

    fingerprint_sizes = Counter(row["normalized_narrative_sha256"] for row in rows)
    for row in rows:
        size = fingerprint_sizes[str(row["normalized_narrative_sha256"])]
        row["normalized_narrative_reuse_count"] = size
        row["normalized_narrative_reused"] = size > 1

    topic_aggregates: dict[str, dict[str, object]] = defaultdict(new_aggregate)
    account_aggregates: dict[str, dict[str, object]] = defaultdict(new_aggregate)
    opinion_account_aggregates: dict[tuple[str, str, str], dict[str, object]] = defaultdict(new_aggregate)
    for row in rows:
        update_aggregate(topic_aggregates[str(row["source_topic"])], row)
        domains = str(row["account_domains"]).split("|")
        for account in domains:
            update_aggregate(account_aggregates[account], row)
            opinion_key = (
                str(row["company_key"]),
                str(row["audit_opinion_fkey"]),
                account,
            )
            update_aggregate(opinion_account_aggregates[opinion_key], row)

    topic_rows = [
        flatten_aggregate({"source_topic": topic}, aggregate)
        for topic, aggregate in sorted(topic_aggregates.items())
    ]
    for account in CANONICAL_ACCOUNT_DOMAINS:
        account_aggregates[account]
    account_rows = []
    for account, aggregate in sorted(account_aggregates.items()):
        coverage_status = (
            "unmapped_source_topics"
            if account == "UNMAPPED"
            else (
                "observed_controlled_topic_assignments"
                if int(aggregate["cam_records"]) > 0
                else "no_controlled_topic_assignments_not_zero_risk"
            )
        )
        account_rows.append(
            flatten_aggregate(
                {"account_domain": account, "coverage_status": coverage_status},
                aggregate,
            )
        )
    opinion_account_rows = [
        flatten_aggregate(
            {
                "company_key": key[0],
                "audit_opinion_fkey": key[1],
                "account_domain": key[2],
            },
            aggregate,
        )
        for key, aggregate in sorted(opinion_account_aggregates.items())
    ]
    overall = new_aggregate()
    for row in rows:
        update_aggregate(overall, row)
    overall_row = flatten_aggregate({"scope": "complete_private_CAM_source"}, overall)

    term_rows = []
    for key, hits in sorted(term_totals.items(), key=lambda x: (-x[1], x[0])):
        category, term = key.split(":", 1)
        term_row: dict[str, object] = {
            "category": category,
            "normalized_term": term,
            "hits": hits,
        }
        add_hf_metadata(term_row)
        term_rows.append(term_row)

    output_dir = prepare_private_output_dir(output_dir)
    write_csv(output_dir / "CAM_token_risk_profile_rows_PRIVATE.csv", rows)
    write_csv(output_dir / "CAM_token_risk_summary.csv", [overall_row])
    write_csv(output_dir / "CAM_token_risk_by_topic.csv", topic_rows)
    write_csv(output_dir / "CAM_token_risk_by_account.csv", account_rows)
    write_csv(output_dir / "CAM_token_risk_by_opinion_account_PRIVATE.csv", opinion_account_rows)
    write_csv(output_dir / "CAM_token_lexicon_counts.csv", term_rows)

    repeated_groups = [count for count in fingerprint_sizes.values() if count > 1]
    qa: dict[str, object] = {
        "method": "deterministic_longest_nonoverlapping_lexicon_match_v2_hf_tokenizers",
        "hf_component": HF_COMPONENT,
        "hf_component_version": HF_COMPONENT_VERSION,
        "hf_pretrained_model_inference_executed": HF_PRETRAINED_MODEL_INFERENCE_EXECUTED,
        "interpretation": (
            "Descriptive language intensity in selected CAM narratives; not independent risk, "
            "CAM likelihood, ICFR status, or causal evidence."
        ),
        "source_sha256": digest,
        "source_columns": len(source_columns),
        "cam_records": len(rows),
        "distinct_cam_keys": len(seen_keys),
        "distinct_companies": len({str(row["company_key"]) for row in rows}),
        "distinct_audit_opinions": len({str(row["audit_opinion_fkey"]) for row in rows}),
        "source_topics": len(source_topics),
        "mapped_records": sum(str(row["account_domains"]) != "UNMAPPED" for row in rows),
        "unmapped_records": sum(str(row["account_domains"]) == "UNMAPPED" for row in rows),
        "account_summary_rows_including_unmapped": len(account_rows),
        "canonical_accounts_without_controlled_topic_assignments": [
            row["account_domain"]
            for row in account_rows
            if row["coverage_status"] == "no_controlled_topic_assignments_not_zero_risk"
        ],
        "opinion_account_rows_including_unmapped": len(opinion_account_rows),
        "title_missing_records": sum(bool(row["title_missing"]) for row in rows),
        "description_missing_records": sum(bool(row["description_missing"]) for row in rows),
        "response_missing_records": sum(bool(row["response_missing"]) for row in rows),
        "all_text_missing_records": sum(bool(row["all_text_missing"]) for row in rows),
        "total_tokens": int(overall_row["total_tokens"]),
        "field_tokens": {
            field.lower(): int(overall_row[f"{field.lower()}_tokens"])
            for field in TEXT_FIELDS
        },
        "field_risk_language_hits": {
            field.lower(): int(overall_row[f"{field.lower()}_risk_language_hits"])
            for field in TEXT_FIELDS
        },
        "field_risk_language_density_per_1000_tokens": {
            field.lower(): overall_row[
                f"{field.lower()}_risk_language_density_per_1000_tokens"
            ]
            for field in TEXT_FIELDS
        },
        "risk_language_hits": int(overall_row["risk_language_hits"]),
        "risk_language_density_per_1000_tokens": overall_row[
            "risk_language_density_per_1000_tokens"
        ],
        "audit_attention_hits": int(overall_row["audit_attention_hits"]),
        "control_and_procedure_hits": int(overall_row["control_and_procedure_hits"]),
        "unique_normalized_narratives": len(fingerprint_sizes),
        "reused_normalized_narrative_groups": len(repeated_groups),
        "records_in_reused_normalized_narratives": sum(repeated_groups),
        "largest_normalized_narrative_reuse_count": max(fingerprint_sizes.values()),
        "lexicon_categories": list(LEXICON),
        "risk_language_categories": list(RISK_LANGUAGE_CATEGORIES),
        "crosswalk_versions": sorted({row["mapping_version"] for row in crosswalk.values()}),
        "private_row_level_outputs": [
            "CAM_token_risk_profile_rows_PRIVATE.csv",
            "CAM_token_risk_by_opinion_account_PRIVATE.csv",
        ],
    }
    (output_dir / "CAM_token_risk_QA.json").write_text(
        json.dumps(qa, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return qa


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cam", type=Path, required=True)
    parser.add_argument("--crosswalk", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--expected-cam-sha256", required=True)
    args = parser.parse_args()
    analyze(args.cam, args.crosswalk, args.out, args.expected_cam_sha256)
    print("Private token profile completed.")


if __name__ == "__main__":
    main()
