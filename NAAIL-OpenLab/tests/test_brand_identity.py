from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NAAIL = ROOT / "NAAIL-OpenLab"

NEW_NAME = "Next-Generation Accounting, Audit & Assurance Intelligence Lab"
TAGLINE = (
    "A Global Evidence-Governed Multi-Agent Digital Twin Platform for "
    "Accounting, Audit, Finance, Sustainability and Scientific Discovery"
)
OLD_NAMES = (
    "Nordic Accounting, Audit & Assurance Intelligence Lab",
    "Nordic Accounting, Audit and Assurance Intelligence Lab",
)

CANONICAL_ENTRY_POINTS = (
    ROOT / "README.md",
    NAAIL / "README.md",
    NAAIL / "BRAND_IDENTITY.md",
    NAAIL / "00_SCIENTIFIC_DISCOVERY_START_HERE.md",
    NAAIL / "OPEN_SOURCE_INTEGRATION_HUB.md",
    NAAIL / "GOOGLE_SCIENTIFIC_DISCOVERY_ORCHESTRATION.md",
    NAAIL / "agents" / "README.md",
)

TEXT_SUFFIXES = {".md", ".txt", ".json", ".yml", ".yaml", ".py", ".toml", ".cff"}

# BRAND_IDENTITY.md intentionally documents the historical name; the migration
# workflow constructs it from fragments so it does not need a source exemption.
HISTORICAL_EXEMPTIONS = {
    NAAIL / "BRAND_IDENTITY.md",
}


def test_canonical_entry_points_use_global_identity():
    for path in CANONICAL_ENTRY_POINTS:
        assert path.exists(), f"Missing canonical NAAIL entry point: {path}"
        text = path.read_text(encoding="utf-8")
        assert NEW_NAME in text, f"New NAAIL name missing from {path}"
        assert TAGLINE in text, f"Global NAAIL tagline missing from {path}"


def test_retired_geographic_expansion_is_not_in_current_naail_sources():
    offenders = []
    for path in NAAIL.rglob("*"):
        if not path.is_file() or path in HISTORICAL_EXEMPTIONS:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        # Preserve explicitly historical release/change records rather than
        # silently rewriting provenance.
        lower_parts = {p.lower() for p in path.parts}
        if (
            path.name.upper().startswith("CHANGELOG")
            or "archive" in lower_parts
            or ("docs" in lower_parts and "activity" in lower_parts)
        ):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(old in text for old in OLD_NAMES):
            offenders.append(str(path.relative_to(ROOT)))

    assert not offenders, "Retired NAAIL expansion remains in current sources: " + ", ".join(offenders)
