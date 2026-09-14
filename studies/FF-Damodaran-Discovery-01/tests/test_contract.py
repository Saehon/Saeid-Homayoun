from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class StudyContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = json.loads((ROOT / "config" / "source_registry.json").read_text(encoding="utf-8"))

    def test_only_authoritative_primary_providers(self) -> None:
        providers = {x["provider"] for x in self.registry["sources"]}
        self.assertEqual(providers, {"Kenneth R. French Data Library", "Aswath Damodaran / NYU Stern"})
        self.assertTrue(all(x["source_level"] == "S1" for x in self.registry["sources"]))

    def test_required_sources_present(self) -> None:
        ids = {x["id"] for x in self.registry["sources"]}
        self.assertTrue({"FF5_MONTHLY", "MOM_MONTHLY", "FF49_MONTHLY", "DAM_BETA", "DAM_WACC", "DAM_EVA"}.issubset(ids))

    def test_archives_are_year_specific(self) -> None:
        dam = [x for x in self.registry["sources"] if x["id"].startswith("DAM_")]
        for src in dam:
            self.assertIn("{yy}", src["archive_template"])
            self.assertGreaterEqual(min(src["archive_years"]), 2012)
            self.assertEqual(max(src["archive_years"]), 2025)
            self.assertEqual(src["current_vintage"], 2026)

    def test_crosswalk_requires_governance_fields(self) -> None:
        path = ROOT / "crosswalk" / "reviewed_crosswalk.csv"
        with path.open(newline="", encoding="utf-8") as f:
            header = next(csv.reader(f))
        required = {"year", "ff49_industry", "damodaran_industry", "mapping_weight", "mapping_confidence", "manual_review", "approved"}
        self.assertTrue(required.issubset(set(header)))

    def test_raw_data_is_not_committed_by_default(self) -> None:
        ignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("data/raw/**", ignore)
        self.assertIn("download_manifest.json", ignore)

    def test_scientific_claim_is_gated(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("verified_candidate_discovery = false", readme)
        self.assertIn("human_gate_approved = false", readme)
        self.assertIn("No agent is permitted to force a positive result", readme)


if __name__ == "__main__":
    unittest.main()
