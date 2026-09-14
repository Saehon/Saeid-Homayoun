from pathlib import Path
import unittest
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
CROSSWALK = ROOT / "crosswalk" / "gpt56sol_reviewed_crosswalk_2026.csv"

EXPECTED_FF49 = {
    "Agric","Food","Soda","Beer","Smoke","Toys","Fun","Books","Hshld","Clths",
    "Hlth","MedEq","Drugs","Chems","Rubbr","Txtls","BldMt","Cnstr","Steel","FabPr",
    "Mach","ElcEq","Autos","Aero","Ships","Guns","Gold","Mines","Coal","Oil","Util",
    "Telcm","PerSv","BusSv","Hardw","Softw","Chips","LabEq","Paper","Boxes","Trans",
    "Whlsl","Rtail","Meals","Banks","Insur","RlEst","Fin","Other"
}


class GPTCrosswalk2026Tests(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv(CROSSWALK)

    def test_all_ff49_industries_covered(self):
        self.assertEqual(set(self.df["ff49_industry"]), EXPECTED_FF49)
        self.assertEqual(self.df["ff49_industry"].nunique(), 49)

    def test_weights_sum_to_one(self):
        sums = self.df.groupby(["year", "ff49_industry"])["mapping_weight"].sum()
        self.assertTrue(np.allclose(sums.values, 1.0, atol=1e-9), sums)

    def test_2026_only(self):
        self.assertEqual(set(self.df["year"]), {2026})

    def test_ai_review_not_human_approval(self):
        self.assertEqual(set(self.df["reviewer"]), {"GPT-5.6 Sol"})
        self.assertEqual(set(self.df["review_status"]), {"AI_REVIEWED"})
        approved = self.df["human_gate_approved"].astype(str).str.lower().isin({"true", "1", "yes"})
        self.assertFalse(approved.any())

    def test_confidence_labels(self):
        self.assertTrue(set(self.df["mapping_confidence"]).issubset({"HIGH", "MEDIUM", "LOW"}))


if __name__ == "__main__":
    unittest.main()
