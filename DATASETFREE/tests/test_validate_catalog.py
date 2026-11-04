"""Offline unit tests for the free-data registry validator."""
from __future__ import annotations
import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "validate_catalog.py"
spec = importlib.util.spec_from_file_location("datasetfree_validate", SCRIPT)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

FIELDS = validator.REGISTRIES[0][1]
SAMPLE = {
    "source": "Example", "discipline": "Accounting",
    "url": "https://example.org/data", "data_fields": "CIK and reporting year",
    "license_access": "Rights unverified", "caveat": "Metadata only",
}

class ManifestTests(unittest.TestCase):
    def create_csv(self, rows):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        path = Path(temp.name) / "sources.csv"
        with path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=FIELDS)
            w.writeheader()
            w.writerows(rows)
        return path

    def test_valid_sample(self):
        self.assertEqual(validator.validate(self.create_csv([SAMPLE]), FIELDS, "source"), [])

    def test_duplicate_source(self):
        path = self.create_csv([SAMPLE, dict(SAMPLE, url="https://example.org/other")])
        self.assertTrue(any("duplicate" in x for x in validator.validate(path, FIELDS, "source")))

    def test_http_rejected(self):
        path = self.create_csv([dict(SAMPLE, url="http://example.org")])
        self.assertTrue(any("invalid HTTPS" in x for x in validator.validate(path, FIELDS, "source")))

    def test_missing_rights(self):
        path = self.create_csv([dict(SAMPLE, license_access="")])
        self.assertTrue(any("empty license_access" in x for x in validator.validate(path, FIELDS, "source")))

    def test_project_registries(self):
        for path, fields, unique in validator.REGISTRIES:
            with self.subTest(path=path):
                self.assertEqual(validator.validate(path, fields, unique), [])

if __name__ == "__main__":
    unittest.main()
