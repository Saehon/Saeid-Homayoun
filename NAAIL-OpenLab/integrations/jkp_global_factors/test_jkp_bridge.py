"""No real vendor data are used in these deterministic unit tests."""
import csv
import tempfile
import unittest
from pathlib import Path
from jkp_bridge import run


class BridgeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.factors = self.base / "factors.csv"
        self.returns = self.base / "returns.csv"
        with self.factors.open("w", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(["date", "MKT", "SMB"])
            for t in range(1, 13):
                writer.writerow([f"2025-{t:02d}-28", (t % 5) - 2, ((t * t) % 7) - 3])
        with self.returns.open("w", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(["date", "entity_id", "excess_return"])
            for t in range(1, 13):
                mkt = ((t % 5) - 2) / 100
                smb = (((t * t) % 7) - 3) / 100
                writer.writerow([f"2025-{t:02d}-28", "TEST", 0.002 + 1.5 * mkt - 0.7 * smb])

    def params(self):
        return dict(factors=self.factors, returns=self.returns,
                    output_dir=self.base / "result", factor_cols=["MKT", "SMB"],
                    factor_unit="percent", return_unit="decimal", source_version="synthetic-v1",
                    universe="TEST", license_confirmed=False, synthetic=True)

    def test_deterministic_regression(self):
        import json
        meta = run(**self.params())
        self.assertEqual(meta["n_estimated_entities"], 1)
        self.assertEqual(meta["scientific_status"], "SIMULATED")
        out = json.loads((self.base / "result" / "factor_exposures.json").read_text())[0]
        self.assertAlmostEqual(out["alpha_decimal_per_period"], 0.002)
        self.assertAlmostEqual(out["betas"]["MKT"], 1.5)
        self.assertAlmostEqual(out["betas"]["SMB"], -0.7)
        self.assertEqual(out["status"], "ESTIMATED_REVIEW_REQUIRED")

    def test_rights_gate(self):
        args = self.params()
        args["synthetic"] = False
        with self.assertRaisesRegex(ValueError, "attestation"):
            run(**args)

    def test_duplicate_factor_dates(self):
        with self.factors.open("a") as fh:
            fh.write("2025-01-28,0,0\n")
        with self.assertRaisesRegex(ValueError, "Duplicate factor date"):
            run(**self.params())

    def test_unmatched_rows_retained_in_manifest(self):
        with self.returns.open("a") as fh:
            fh.write("2024-01-28,TEST,0.02\n")
        self.assertEqual(run(**self.params())["n_unmatched_returns"], 1)


if __name__ == "__main__":
    unittest.main()