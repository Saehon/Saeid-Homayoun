"""Deterministic smoke, temporal isolation and governance tests."""
import math
import tempfile
import unittest
from pathlib import Path
from pilot import fixture, run, WEIGHTS, risk, read_csv, main

class PilotTests(unittest.TestCase):
    def test_fixture_and_split(self):
        rows=fixture()
        result=run(rows,"synthetic","fixture")
        self.assertEqual(len(rows),80)
        self.assertEqual(result["splits"]["train_n"],50)
        self.assertEqual(result["splits"]["validation_n"],10)
        self.assertEqual(result["splits"]["test_n"],20)
        self.assertFalse(result["scientific_discovery_claim_allowed"])
        self.assertEqual(result["human_approval_status"],"REQUIRED_NOT_GRANTED")
        self.assertTrue(result["not_bao_replication"])
    def test_no_holdout_leakage(self):
        rows=fixture()
        first=run(rows,"synthetic","original")
        for r in rows:
            if r["year"] >= 2024:
                r["fraud_label"]=1-r["fraud_label"]
        second=run(rows,"synthetic","mutated_test")
        self.assertEqual(first["arms"]["A2"]["weights"],second["arms"]["A2"]["weights"])
        self.assertEqual(first["arms"]["A3"]["weights"],second["arms"]["A3"]["weights"])
        self.assertNotEqual(first["arms"]["A3"]["test_metrics"]["brier"],
                            second["arms"]["A3"]["test_metrics"]["brier"])
    def test_gates_do_not_change_prediction(self):
        result=run(fixture(),"synthetic","fixture")
        a0=result["arms"]["A0"]["test_metrics"]
        a1=result["arms"]["A1"]["test_metrics"]
        self.assertEqual(a0["brier"],a1["brier"])
        self.assertLess(a1["reviewable_count"],a0["reviewable_count"])
        self.assertEqual(a0["n"],a1["n"])
    def test_no_invalid_probability(self):
        for row in fixture():
            for w in WEIGHTS:
                self.assertTrue(0<=risk(row,w)<=1)
    def test_cli_exports_json(self):
        with tempfile.TemporaryDirectory() as temp:
            outfile=Path(temp)/"results.json"
            main(["--demo","--out",str(outfile)])
            self.assertIn("SYNTHETIC_DEMONSTRATION",outfile.read_text())
    def test_rejects_invalid_schema(self):
        with tempfile.TemporaryDirectory() as temp:
            bad=Path(temp)/"bad.csv"
            bad.write_text("case_id,year\nabc,2025\n")
            with self.assertRaises(ValueError):
                read_csv(bad)

if __name__=="__main__":
    unittest.main()
