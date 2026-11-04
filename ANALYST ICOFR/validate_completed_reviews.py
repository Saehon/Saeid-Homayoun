#!/usr/bin/env python3
"""Validate completed CAM risk-language reviewer CSVs.

The validator checks the codebook scale, flags, exact evidence offsets, ORL
consistency, timestamps, and form metadata. Error output contains only case
IDs and field names; it never echoes private narrative text.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

from build_validation_sample import (
    CODEBOOK_VERSION,
    DIMENSIONS,
    FORM_SOFTWARE_VERSION,
    PROTOCOL_ID,
    REVIEW_FIELDS,
)


FORM_PREFIX_FIELDS = (
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
)
BINARY_FLAGS = (
    "audit_attention_only",
    "procedure_language_intrusion",
    "negation_or_resolution",
    "insufficient_context",
    "unable_to_code",
)
FORBIDDEN_REVIEWER_FIELDS = {
    "critical_audit_matter_key",
    "company_key",
    "audit_opinion_fkey",
    "source_topic",
    "assigned_account_domain",
    "all_mapped_account_domains",
    "score_band",
    "fiscal_year_link_status",
    "provisional_fiscal_year",
    "cam_narrative_risk_language_density_per_1000_tokens",
    "normalized_narrative_sha256",
    "hf_component",
    "hf_component_version",
    "hf_pretrained_model_inference_executed",
    "construct_status",
    "selection_seed",
}


def _error(
    errors: list[dict[str, object]],
    row_number: int,
    case_id: str,
    field: str,
    message: str,
) -> None:
    errors.append(
        {
            "row_number": row_number,
            "case_id": case_id,
            "field": field,
            "message": message,
        }
    )


def _parse_timestamp(value: str) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() != timezone.utc.utcoffset(parsed):
        return None
    return parsed


def validate_row(
    row: Mapping[str, str],
    *,
    row_number: int,
    expected_reviewer: str | None = None,
    expected_batch: str | None = None,
) -> list[dict[str, object]]:
    errors: list[dict[str, object]] = []
    case_id = (row.get("case_id") or "").strip()

    exact_metadata = {
        "protocol_id": PROTOCOL_ID,
        "codebook_version": CODEBOOK_VERSION,
        "form_software_version": FORM_SOFTWARE_VERSION,
    }
    for field, expected in exact_metadata.items():
        if (row.get(field) or "").strip() != expected:
            _error(errors, row_number, case_id, field, f"must equal {expected!r}")
    if not case_id:
        _error(errors, row_number, case_id, "case_id", "must not be blank")

    reviewer = (row.get("reviewer_id_pseudonym") or "").strip()
    if reviewer not in {"REVIEWER_A", "REVIEWER_B"}:
        _error(
            errors,
            row_number,
            case_id,
            "reviewer_id_pseudonym",
            "must be REVIEWER_A or REVIEWER_B",
        )
    if expected_reviewer and reviewer != expected_reviewer:
        _error(
            errors,
            row_number,
            case_id,
            "reviewer_id_pseudonym",
            f"must equal expected reviewer {expected_reviewer!r}",
        )

    batch = (row.get("assignment_batch") or "").strip()
    if batch not in {"pilot_round_1", "confirmatory_main"}:
        _error(
            errors,
            row_number,
            case_id,
            "assignment_batch",
            "must be pilot_round_1 or confirmatory_main",
        )
    if expected_batch and batch != expected_batch:
        _error(
            errors,
            row_number,
            case_id,
            "assignment_batch",
            f"must equal expected batch {expected_batch!r}",
        )

    try:
        display_order = int((row.get("display_order") or "").strip())
        if display_order < 1:
            raise ValueError
    except ValueError:
        _error(errors, row_number, case_id, "display_order", "must be a positive integer")

    started = _parse_timestamp((row.get("started_at_utc") or "").strip())
    submitted = _parse_timestamp((row.get("submitted_at_utc") or "").strip())
    if started is None:
        _error(
            errors,
            row_number,
            case_id,
            "started_at_utc",
            "must be a valid ISO-8601 UTC timestamp in a completed form",
        )
    if submitted is None:
        _error(
            errors,
            row_number,
            case_id,
            "submitted_at_utc",
            "must be a valid ISO-8601 UTC timestamp in a completed form",
        )
    if started and submitted and submitted < started:
        _error(
            errors,
            row_number,
            case_id,
            "submitted_at_utc",
            "must not precede started_at_utc",
        )

    for field in BINARY_FLAGS:
        if (row.get(field) or "").strip() not in {"0", "1"}:
            _error(errors, row_number, case_id, field, "must be 0 or 1")
    confidence = (row.get("confidence") or "").strip().lower()
    if confidence not in {"low", "medium", "high"}:
        _error(errors, row_number, case_id, "confidence", "must be low, medium, or high")
    note = row.get("reviewer_note") or ""
    if len(note) > 300:
        _error(errors, row_number, case_id, "reviewer_note", "must be 300 characters or fewer")

    unable = (row.get("unable_to_code") or "").strip() == "1"
    scores: dict[str, int | None] = {}
    for name, abbreviation in DIMENSIONS:
        score_field = f"{name}_{abbreviation}_0_to_3"
        raw_score = (row.get(score_field) or "").strip()
        score: int | None = None
        if unable:
            if raw_score:
                _error(
                    errors,
                    row_number,
                    case_id,
                    score_field,
                    "must be blank when unable_to_code=1",
                )
        else:
            try:
                score = int(raw_score)
                if score not in {0, 1, 2, 3}:
                    raise ValueError
            except ValueError:
                _error(errors, row_number, case_id, score_field, "must be an integer from 0 to 3")
                score = None
        scores[abbreviation] = score

        populated_spans = 0
        for span_number in (1, 2, 3):
            prefix = f"{name}_{abbreviation}_evidence_span_{span_number}"
            fields = {
                "source": f"{prefix}_source_field",
                "start": f"{prefix}_start_0_based_inclusive",
                "end": f"{prefix}_end_0_based_exclusive",
                "quote": f"{prefix}_exact_quote",
                "extended": f"{prefix}_extended_reason_if_over_40_tokens",
            }
            values = {key: row.get(field) or "" for key, field in fields.items()}
            core_present = [bool(values[key]) for key in ("source", "start", "end", "quote")]
            if not any(core_present):
                if values["extended"]:
                    _error(
                        errors,
                        row_number,
                        case_id,
                        fields["extended"],
                        "must be blank when the evidence span is blank",
                    )
                continue
            populated_spans += 1
            if not all(core_present):
                _error(
                    errors,
                    row_number,
                    case_id,
                    prefix,
                    "source, start, end, and exact quote must all be populated",
                )
                continue
            source = values["source"]
            if source not in {"TITLE", "DESCRIPTION"}:
                _error(
                    errors,
                    row_number,
                    case_id,
                    fields["source"],
                    "must be TITLE or DESCRIPTION",
                )
                continue
            source_text = row.get(source.lower()) or ""
            try:
                start = int(values["start"])
                end = int(values["end"])
            except ValueError:
                _error(
                    errors,
                    row_number,
                    case_id,
                    prefix,
                    "start and end must be integers",
                )
                continue
            if not (0 <= start < end <= len(source_text)):
                _error(
                    errors,
                    row_number,
                    case_id,
                    prefix,
                    "offsets are outside the selected source field",
                )
                continue
            if source_text[start:end] != values["quote"]:
                _error(
                    errors,
                    row_number,
                    case_id,
                    fields["quote"],
                    "does not exactly equal source_text[start:end]",
                )
            token_count = len(re.findall(r"\S+", values["quote"]))
            if token_count > 60:
                _error(
                    errors,
                    row_number,
                    case_id,
                    fields["quote"],
                    "evidence span exceeds the 60-token maximum",
                )
            if token_count > 40 and not values["extended"].strip():
                _error(
                    errors,
                    row_number,
                    case_id,
                    fields["extended"],
                    "is required for an evidence span over 40 tokens",
                )

        rationale_field = f"{name}_{abbreviation}_rationale_one_sentence"
        rationale = row.get(rationale_field) or ""
        if len(rationale) > 300:
            _error(
                errors,
                row_number,
                case_id,
                rationale_field,
                "must be 300 characters or fewer",
            )
        if unable:
            if populated_spans:
                _error(
                    errors,
                    row_number,
                    case_id,
                    score_field,
                    "evidence spans must be blank when unable_to_code=1",
                )
        elif score == 0 and populated_spans:
            _error(
                errors,
                row_number,
                case_id,
                score_field,
                "score 0 must have no evidence spans",
            )
        elif score is not None and score > 0:
            if populated_spans == 0:
                _error(
                    errors,
                    row_number,
                    case_id,
                    score_field,
                    "a nonzero score requires at least one exact evidence span",
                )
            if not rationale.strip():
                _error(
                    errors,
                    row_number,
                    case_id,
                    rationale_field,
                    "a nonzero score requires a one-sentence rationale",
                )

    if not unable and all(scores.get(code) is not None for code in ("EU", "AO", "VC", "FL", "ORL")):
        components = [int(scores[code]) for code in ("EU", "AO", "VC", "FL")]
        overall = int(scores["ORL"])
        if (overall == 0) != all(score == 0 for score in components):
            _error(
                errors,
                row_number,
                case_id,
                "overall_risk_language_ORL_0_to_3",
                "ORL=0 if and only if EU=AO=VC=FL=0",
            )
        if overall == 3 and not (
            any(score == 3 for score in components)
            or sum(score == 2 for score in components) >= 2
        ):
            _error(
                errors,
                row_number,
                case_id,
                "overall_risk_language_ORL_0_to_3",
                "ORL=3 requires one component at 3 or at least two components at 2",
            )
        if (row.get("audit_attention_only") or "").strip() == "1" and (
            any(score != 0 for score in components) or overall != 0
        ):
            _error(
                errors,
                row_number,
                case_id,
                "audit_attention_only",
                "must not be 1 when an included risk dimension is nonzero",
            )

    return errors


def validate_file(
    path: Path,
    *,
    expected_reviewer: str | None = None,
    expected_batch: str | None = None,
) -> dict[str, object]:
    required = set(FORM_PREFIX_FIELDS) | set(REVIEW_FIELDS)
    errors: list[dict[str, object]] = []
    case_ids: list[str] = []
    display_orders: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        actual_fields = set(reader.fieldnames or ())
        missing = sorted(required - actual_fields)
        if missing:
            return {
                "valid": False,
                "rows": 0,
                "errors": [
                    {
                        "row_number": 1,
                        "case_id": "",
                        "field": "header",
                        "message": f"missing required columns: {missing}",
                    }
                ],
            }
        forbidden = sorted(FORBIDDEN_REVIEWER_FIELDS & actual_fields)
        if forbidden:
            return {
                "valid": False,
                "rows": 0,
                "errors": [
                    {
                        "row_number": 1,
                        "case_id": "",
                        "field": "header",
                        "message": (
                            "reviewer export contains blinded source/design/model fields: "
                            f"{forbidden}"
                        ),
                    }
                ],
            }
        for row_number, row in enumerate(reader, start=2):
            case_ids.append((row.get("case_id") or "").strip())
            display_orders.append((row.get("display_order") or "").strip())
            errors.extend(
                validate_row(
                    row,
                    row_number=row_number,
                    expected_reviewer=expected_reviewer,
                    expected_batch=expected_batch,
                )
            )
    if len(case_ids) != len(set(case_ids)):
        _error(errors, 1, "", "case_id", "case IDs must be unique within a reviewer file")
    if len(display_orders) != len(set(display_orders)):
        _error(errors, 1, "", "display_order", "display orders must be unique")
    return {"valid": not errors, "rows": len(case_ids), "error_count": len(errors), "errors": errors}


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reviewer_csv", type=Path)
    parser.add_argument("--expected-reviewer", choices=("REVIEWER_A", "REVIEWER_B"))
    parser.add_argument("--expected-batch", choices=("pilot_round_1", "confirmatory_main"))
    parser.add_argument("--json-output", type=Path)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    result = validate_file(
        args.reviewer_csv,
        expected_reviewer=args.expected_reviewer,
        expected_batch=args.expected_batch,
    )
    rendered = json.dumps(result, indent=2)
    if args.json_output:
        args.json_output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
