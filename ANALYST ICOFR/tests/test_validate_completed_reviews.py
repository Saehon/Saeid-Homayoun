import csv
import tempfile
import unittest
from pathlib import Path

import build_validation_sample as sample
import validate_completed_reviews as validator


class CompletedReviewValidatorTests(unittest.TestCase):
    def _valid_row_and_fields(self, directory: Path):
        metadata = sample.write_worked_example(directory)
        source = directory / metadata["output"]["filename"]
        with source.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            row = next(reader)
            fields = reader.fieldnames
        row["reviewer_id_pseudonym"] = "REVIEWER_A"
        row["assignment_batch"] = "pilot_round_1"
        row["started_at_utc"] = "2026-10-14T08:00:00Z"
        row["submitted_at_utc"] = "2026-10-14T08:10:00Z"
        return row, fields

    def _write(self, path: Path, row, fields):
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerow(row)

    def test_valid_completed_form_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            row, fields = self._valid_row_and_fields(tmp_path)
            path = tmp_path / "completed.csv"
            self._write(path, row, fields)
            result = validator.validate_file(
                path,
                expected_reviewer="REVIEWER_A",
                expected_batch="pilot_round_1",
            )
            self.assertTrue(result["valid"], result["errors"])

    def test_quote_mismatch_and_invalid_scale_are_rejected_without_echoing_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            row, fields = self._valid_row_and_fields(tmp_path)
            row["estimation_uncertainty_EU_0_to_3"] = "4"
            row["adverse_outcome_AO_evidence_span_1_exact_quote"] = "mismatch"
            row["reviewer_note"] = "x" * 301
            path = tmp_path / "invalid.csv"
            self._write(path, row, fields)
            result = validator.validate_file(path)
            self.assertFalse(result["valid"])
            error_fields = {error["field"] for error in result["errors"]}
            self.assertIn("estimation_uncertainty_EU_0_to_3", error_fields)
            self.assertIn("adverse_outcome_AO_evidence_span_1_exact_quote", error_fields)
            self.assertIn("reviewer_note", error_fields)
            self.assertNotIn("mismatch", str(result["errors"]))

    def test_blinded_reviewer_file_rejects_source_and_model_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            row, fields = self._valid_row_and_fields(tmp_path)
            row["company_key"] = "synthetic-company"
            fields = list(fields) + ["company_key"]
            path = tmp_path / "unblinded.csv"
            self._write(path, row, fields)
            result = validator.validate_file(path)
            self.assertFalse(result["valid"])
            self.assertEqual(result["errors"][0]["field"], "header")
            self.assertIn("company_key", result["errors"][0]["message"])


if __name__ == "__main__":
    unittest.main()
