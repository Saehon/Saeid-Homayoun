"""Synthetic fixtures only: no restricted financial data are included."""
from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from jkp_bridge import parse_date, validate


class JKPBridgeTest(unittest.TestCase):
    def write_csv(self, path: Path, records):
        with path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["date", "country", "MKT", "SMB"])
            w.writeheader()
            w.writerows(records)

    def test_2020_2024_window_and_missingness(self):
        with tempfile.TemporaryDirectory() as d:
            file = Path(d) / "fixture.csv"
            self.write_csv(file, [
                {"date": "201912", "country": "US", "MKT": "1.2", "SMB": "2"},
                {"date": "202001", "country": "US", "MKT": "3.0", "SMB": ""},
                {"date": "202001", "country": "SE", "MKT": "4.0", "SMB": "2.0"},
            ])
            result = validate(file, date_column="date", factors=["MKT", "SMB"], keys=["country"])
            self.assertEqual(result["rows_in_window"], 2)
            self.assertEqual(result["rows_outside_window"], 1)
            self.assertEqual(result["missing_by_factor"]["SMB"], 1)
            self.assertEqual(result["empirical_results"], "NOT_RUN")

    def test_duplicate_month_country_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            file = Path(d) / "fixture.csv"
            self.write_csv(file, [
                {"date": "2020-01-01", "country": "US", "MKT": "1", "SMB": "1"},
                {"date": "2020-01-31", "country": "US", "MKT": "1", "SMB": "1"},
            ])
            with self.assertRaisesRegex(ValueError, "duplicate"):
                validate(file, date_column="date", factors=["MKT", "SMB"], keys=["country"])

    def test_invalid_factor_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            file = Path(d) / "fixture.csv"
            self.write_csv(file, [{"date": "202001", "country": "US", "MKT": "inf", "SMB": "1"}])
            with self.assertRaisesRegex(ValueError, "Non-finite"):
                validate(file, date_column="date", factors=["MKT", "SMB"], keys=["country"])

    def test_invalid_date_rejected(self):
        with self.assertRaises(ValueError):
            parse_date("2020-13-40")


if __name__ == "__main__":
    unittest.main()
