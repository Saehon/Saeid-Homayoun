"""Offline, non-evidentiary journal registry check and run manifest."""
from __future__ import annotations
import argparse
import csv
import datetime as dt
import hashlib
import json
import os
from pathlib import Path

PHASES = ("systematic-review", "meta-analysis", "replication", "hypothesis-test", "digital-twin")
TIERS = ("ALL", "FT50", "AJG-4-star", "AJG-4", "AJG-3")
COLUMNS = ("study_id", "title", "doi", "journal", "year", "journal_tier", "source_url",
           "code_url", "data_url", "license_status", "evidence_status")

def validate_registry(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    if not path.is_file():
        raise FileNotFoundError(f"Registry not found: {path}")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = set(COLUMNS).difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing registry columns: {sorted(missing)}")
        records = list(reader)
    problems: list[str] = []
    ids: set[str] = set()
    for idx, record in enumerate(records, start=2):
        identifier = (record.get("study_id") or "").strip()
        if not identifier:
            problems.append(f"row {idx}: missing study_id")
        if identifier in ids:
            problems.append(f"row {idx}: duplicate study_id {identifier!r}")
        ids.add(identifier)
        for field in ("title", "journal", "year"):
            if not (record.get(field) or "").strip():
                problems.append(f"row {idx}: missing {field}")
        if record.get("year") and not str(record["year"]).isdigit():
            problems.append(f"row {idx}: invalid year")
        if (record.get("evidence_status") or "").strip().upper() == "VERIFIED" and not record.get("source_url"):
            problems.append(f"row {idx}: claimed verification without source_url")
    return records, problems

def run(phase: str, journal_tier: str, registry: Path, output_dir: Path) -> dict:
    if phase not in PHASES or journal_tier not in TIERS:
        raise ValueError("Unrecognized phase or tier")
    records, problems = validate_registry(registry)
    included = [r for r in records if journal_tier == "ALL" or r["journal_tier"] == journal_tier]
    digest = hashlib.sha256(registry.read_bytes()).hexdigest()
    output_dir.mkdir(parents=True, exist_ok=True)
    status = "SCHEMA_BLOCKED" if problems else "AWAITING_HUMAN_SCREENING"
    manifest = {
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "git_commit": os.getenv("GITHUB_SHA", "local-uncommitted"),
        "phase": phase, "journal_tier": journal_tier,
        "status": status,
        "candidate_count": len(included),
        "registry_sha256": digest,
        "problems": problems,
        "retrieval_performed": False, "replication_executed": False,
        "hosted_model_called": False, "real_data_tested": False,
        "empirical_claims_verified": False, "human_approval": "REQUIRED"
    }
    (output_dir / "execution_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    lines = [
        "# NAAIL Journal Co-Scientist — offline registry report",
        "", f"- Phase: {phase}", f"- Tier: {journal_tier}",
        f"- Candidate registry records: {len(included)}",
        f"- Validation: {status}", "- Automated external literature search: NOT PERFORMED",
        "- Numerical replication: NOT PERFORMED",
        "- Microsoft/hosted AI calls: NOT PERFORMED",
        "- Independent human article verification: PENDING",
        "- Empirical or publication-ready conclusions: NONE",
        "", "## Required next action", "",
        ("Repair the registry schema errors: " + "; ".join(problems))
        if problems else
        ("Record full search strategy and import lawful, human-checkable metadata for screening."
         if not included else "Verify each retrieved study and its permissions; document inclusion decisions."),
        ""
    ]
    (output_dir / "weekly_research_report.md").write_text("\n".join(lines), encoding="utf-8")
    return manifest

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", choices=PHASES, default="systematic-review")
    parser.add_argument("--journal-tier", choices=TIERS, default="ALL")
    parser.add_argument("--registry", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.phase, args.journal_tier, args.registry, args.output_dir)
    print(json.dumps(result, indent=2))
    if result["problems"]:
        raise SystemExit(2)

if __name__ == "__main__":
    main()
