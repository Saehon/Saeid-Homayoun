import copy
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from research.ai_evidence_evaluation.validate_run import (
    check_sha256, inspect_manifest, parse_timestamp,
    validate_prediction_record, validate_record, nonnegative_number
)


ROOT = Path(__file__).resolve().parents[1] / "examples"


class ProvenanceValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = json.loads((ROOT / "provenance_manifest.json").read_text(encoding="utf-8"))

    def test_synthetic_manifest_passes(self):
        report = inspect_manifest(copy.deepcopy(self.original), ROOT)
        self.assertEqual(report["records_checked"], 2)
        self.assertEqual(report["run_summaries"][0]["n_predictions"], 2)
        self.assertTrue(report["local_file_integrity_checks_passed"])
        self.assertFalse(report["model_performance_claim_permitted"])

    def test_no_independent_validation_claim(self):
        report = inspect_manifest(self.original, ROOT)
        self.assertEqual(report["independent_validation_status"], "NOT_VERIFIED")
        self.assertTrue(all(not x["provider_execution_independently_attested"]
                            for x in report["run_summaries"]))

    def test_duplicate_run_id_rejected(self):
        bad = copy.deepcopy(self.original)
        bad["runs"][1]["run_id"] = bad["runs"][0]["run_id"]
        with self.assertRaises(ValueError):
            inspect_manifest(bad, ROOT)

    def test_manifest_schema_rejected(self):
        bad = copy.deepcopy(self.original)
        bad["schema_version"] = "0.0"
        with self.assertRaises(ValueError):
            inspect_manifest(bad, ROOT)

    def test_bad_digest_rejected(self):
        bad = copy.deepcopy(self.original)
        bad["runs"][0]["predictions_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            inspect_manifest(bad, ROOT)

    def test_absolute_file_path_rejected(self):
        bad = copy.deepcopy(self.original)
        bad["runs"][0]["predictions_path"] = str((ROOT / "provenance_fixture.jsonl").resolve())
        with self.assertRaises(ValueError):
            inspect_manifest(bad, ROOT)

    def test_path_traversal_rejected(self):
        bad = copy.deepcopy(self.original)
        bad["runs"][0]["predictions_path"] = "../README.md"
        with self.assertRaises(ValueError):
            inspect_manifest(bad, ROOT)

    def test_negative_token_count_rejected(self):
        bad = copy.deepcopy(self.original)
        bad["runs"][0]["input_tokens"] = -1
        with self.assertRaises(ValueError):
            inspect_manifest(bad, ROOT)

    def test_boolean_token_count_rejected(self):
        bad = copy.deepcopy(self.original)
        bad["runs"][0]["input_tokens"] = True
        with self.assertRaises(ValueError):
            inspect_manifest(bad, ROOT)

    def test_nonfinite_cost_rejected(self):
        for value in ("NaN", "Infinity", "-0.01"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    nonnegative_number(value, "cost")

    def test_invalid_sha_rejected(self):
        with self.assertRaises(ValueError):
            check_sha256("FAKE", "digest")

    def test_nonutc_timestamp_rejected(self):
        for value in ("2026-10-31T12:00:00+01:00", "tomorrow", 100):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_timestamp(value)

    def test_invented_vendor_fixture_rejected(self):
        bad = copy.deepcopy(self.original)
        bad["runs"][0]["provider"] = "openai"
        with self.assertRaises(ValueError):
            inspect_manifest(bad, ROOT)

    def test_provider_output_requires_opt_in(self):
        bad = copy.deepcopy(self.original)
        bad["runs"][0].update(source_type="declared_provider_output",
                              provider="google", data_transfer_authorized=True)
        with self.assertRaises(ValueError):
            inspect_manifest(bad, ROOT)

    def test_provider_output_requires_consent(self):
        bad = copy.deepcopy(self.original)
        bad["runs"][0].update(source_type="declared_provider_output", provider="anthropic",
                              data_transfer_authorized=False)
        with self.assertRaises(ValueError):
            validate_record(bad["runs"][0], ROOT, allow_observed=True)

    def test_declared_provider_never_becomes_attested(self):
        record = copy.deepcopy(self.original["runs"][0])
        record.update(source_type="declared_provider_output", provider="openai",
                      data_transfer_authorized=True)
        checked = validate_record(record, ROOT, allow_observed=True)
        self.assertFalse(checked["provider_execution_independently_attested"])
        self.assertFalse(checked["human_review_independently_verified"])

    def test_no_mixed_fixture_real_claims(self):
        bad = copy.deepcopy(self.original)
        bad["runs"][1].update(source_type="declared_provider_output",
                              provider="google", data_transfer_authorized=True)
        with self.assertRaisesRegex(ValueError, "mix"):
            inspect_manifest(bad, ROOT, allow_observed=True)

    def test_error_cannot_claim_answer(self):
        with self.assertRaises(ValueError):
            validate_prediction_record({"status": "error", "model_answer": "success"})

    def test_answer_requires_citations(self):
        with self.assertRaises(ValueError):
            validate_prediction_record({"status": "answered", "model_answer": "X"})

    def test_duplicate_prediction_case_ids_rejected(self):
        source = (ROOT / "provenance_fixture.jsonl").read_text(encoding="utf-8")
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            doubled = source.splitlines()[0] + "\n" + source.splitlines()[0] + "\n"
            (tmp_path / "duplicate.jsonl").write_text(doubled, encoding="utf-8")
            record = copy.deepcopy(self.original["runs"][0])
            record["predictions_path"] = "duplicate.jsonl"
            record["predictions_sha256"] = hashlib.sha256(doubled.encode()).hexdigest()
            with self.assertRaises(ValueError):
                validate_record(record, tmp_path)

    def test_missing_run_identity_rejected(self):
        bad = copy.deepcopy(self.original)
        bad["runs"][0]["model_version"] = ""
        with self.assertRaises(ValueError):
            inspect_manifest(bad, ROOT)


if __name__ == "__main__":
    unittest.main()
