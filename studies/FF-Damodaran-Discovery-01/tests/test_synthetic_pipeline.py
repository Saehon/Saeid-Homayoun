from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

STUDY = Path(__file__).resolve().parents[1]
SRC = STUDY / "src"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class SyntheticPipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.processed = self.root / "data" / "processed"
        self.crosswalk = self.root / "crosswalk"
        self.results = self.root / "results" / "baseline"
        self.evidence = self.root / "evidence"
        for p in [self.processed, self.crosswalk, self.results, self.evidence]:
            p.mkdir(parents=True, exist_ok=True)

        rng = np.random.default_rng(20260914)
        years = list(range(2012, 2024))
        industries = [f"FF{i:02d}" for i in range(10)]

        ff_rows = []
        exposure_rows = []
        dam_rows = []
        cw_rows = []
        factor_rows = []

        for year in years:
            factor_rows.append({"year": year, "Mkt-RF": rng.normal(0.08, 0.15), "SMB": rng.normal(), "HML": rng.normal()})
            for i, industry in enumerate(industries):
                beta_mkt = 0.75 + 0.035 * i + rng.normal(0, 0.03)
                beta_smb = -0.20 + 0.04 * i + rng.normal(0, 0.03)
                beta_hml = 0.10 + rng.normal(0, 0.04)
                beta_rmw = 0.05 + rng.normal(0, 0.03)
                beta_cma = -0.03 + rng.normal(0, 0.03)
                beta_mom = 0.02 + rng.normal(0, 0.03)

                de = 0.20 + 0.025 * i + rng.normal(0, 0.02)
                wacc = 0.07 + 0.002 * i + rng.normal(0, 0.004)
                roe = 0.12 + 0.004 * i + rng.normal(0, 0.01)
                roc = 0.10 + 0.003 * i + rng.normal(0, 0.01)
                spread = roc - wacc

                current_return = (
                    0.03
                    + 0.035 * beta_mkt
                    - 0.025 * de
                    + 0.10 * spread
                    + rng.normal(0, 0.035)
                )
                ff_rows.append({"year": year, "ff49_industry": industry, "industry_return": current_return})
                exposure_rows.append({
                    "year": year,
                    "ff49_industry": industry,
                    "factor_window_months": 60,
                    "factor_regression_r2": 0.55 + rng.normal(0, 0.03),
                    "ff_beta_mkt_rf": beta_mkt,
                    "ff_beta_smb": beta_smb,
                    "ff_beta_hml": beta_hml,
                    "ff_beta_rmw": beta_rmw,
                    "ff_beta_cma": beta_cma,
                    "ff_beta_mom": beta_mom,
                })

                dam_name = f"DAM_{industry}"
                dam_rows.append({
                    "year": year,
                    "damodaran_industry": dam_name,
                    "beta_beta": beta_mkt + rng.normal(0, 0.02),
                    "beta_d_e_ratio": de,
                    "beta_unlevered_beta": beta_mkt / (1 + 0.7 * de),
                    "wacc_cost_of_capital": wacc,
                    "wacc_cost_of_equity": wacc + 0.035,
                    "eva_roe": roe,
                    "eva_roc": roc,
                    "eva_roc_wacc": spread,
                })
                cw_rows.append({
                    "year": year,
                    "ff49_industry": industry,
                    "damodaran_industry": dam_name,
                    "mapping_weight": 1.0,
                    "mapping_confidence": "SYNTHETIC_HIGH",
                    "manual_review": True,
                    "approved": True,
                })

        pd.DataFrame(ff_rows).to_csv(self.processed / "ff49_industry_year.csv", index=False)
        pd.DataFrame(exposure_rows).to_csv(self.processed / "ff49_factor_exposures_year.csv", index=False)
        pd.DataFrame(dam_rows).to_csv(self.processed / "damodaran_industry_year.csv", index=False)
        pd.DataFrame(cw_rows).to_csv(self.crosswalk / "reviewed_crosswalk.csv", index=False)
        pd.DataFrame(factor_rows).to_csv(self.processed / "ff_factors_year.csv", index=False)
        (self.evidence / "download_manifest.json").write_text(
            json.dumps({"study_id": "SYNTHETIC", "files": []}), encoding="utf-8"
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_full_synthetic_pipeline(self) -> None:
        merge_panel = load_module("merge_panel_test", SRC / "merge_panel.py")
        merge_panel.P = self.processed
        merge_panel.CW = self.crosswalk / "reviewed_crosswalk.csv"
        merge_panel.OUT = self.processed / "econova_ff_damodaran_panel.csv"
        merge_panel.main()

        panel = pd.read_csv(merge_panel.OUT)
        self.assertEqual(len(panel), 120)
        self.assertTrue({"ff_beta_mkt_rf", "beta_d_e_ratio", "future_industry_return_1y"}.issubset(panel.columns))

        # Verify the t -> t+1 construction within each industry and no cross-industry shift.
        for _, g in panel.groupby("ff49_industry"):
            g = g.sort_values("year").reset_index(drop=True)
            lhs = g["future_industry_return_1y"].iloc[:-1].to_numpy()
            rhs = g["industry_return"].iloc[1:].to_numpy()
            self.assertTrue(np.allclose(lhs, rhs, equal_nan=True))
            self.assertTrue(pd.isna(g.iloc[-1]["future_industry_return_1y"]))

        baseline = load_module("baseline_tables_test", SRC / "baseline_tables.py")
        baseline.PANEL = merge_panel.OUT
        baseline.OUT = self.results
        baseline.main()

        expected_tables = [
            "table1_variable_definitions.csv",
            "table2_descriptive_statistics.csv",
            "table3_correlations.csv",
            "table4_main_regressions.csv",
            "table5_temporal_oos_and_data_value.csv",
        ]
        for name in expected_tables:
            path = self.results / name
            self.assertTrue(path.exists(), name)
            self.assertGreater(path.stat().st_size, 0, name)

        t4 = pd.read_csv(self.results / "table4_main_regressions.csv")
        self.assertTrue({"Factor-exposure-only", "Fundamentals-only", "Combined"}.issubset(set(t4["model"])))
        self.assertIn("p_value_descriptive_not_fitness", t4.columns)
        self.assertTrue(t4["industry_fe"].all())
        self.assertTrue(t4["year_fe"].all())

        t5 = pd.read_csv(self.results / "table5_temporal_oos_and_data_value.csv")
        self.assertEqual(set(t5["model"]), {"Factor-exposure-only", "Fundamentals-only", "Combined"})
        self.assertIn("incremental_oos_r2_vs_factor_only", t5.columns)
        self.assertTrue((t5["n_oos"] > 0).all())

        passport = load_module("make_data_passport_test", SRC / "make_data_passport.py")
        passport.MANIFEST = self.evidence / "download_manifest.json"
        passport.PROCESSED = self.processed
        passport.OUT = self.evidence / "data_passport.json"
        passport.ROOT = self.root
        passport.main()

        p = json.loads(passport.OUT.read_text(encoding="utf-8"))
        self.assertTrue(p["authoritative_source_policy"])
        self.assertTrue(p["scientific_controls"]["future_outcome_constructed_after_time_sort"])
        self.assertTrue(p["scientific_controls"]["human_gate_required"])
        artifact_names = {x["path"].split("/")[-1] for x in p["processed_artifacts"]}
        self.assertIn("ff49_factor_exposures_year.csv", artifact_names)
        self.assertIn("econova_ff_damodaran_panel.csv", artifact_names)

    def test_crosswalk_weights_must_sum_to_one(self) -> None:
        cw_path = self.crosswalk / "reviewed_crosswalk.csv"
        cw = pd.read_csv(cw_path)
        mask = (cw["year"] == cw["year"].min()) & (cw["ff49_industry"] == "FF00")
        cw.loc[mask, "mapping_weight"] = 0.8
        cw.to_csv(cw_path, index=False)

        merge_panel = load_module("merge_panel_bad_weight_test", SRC / "merge_panel.py")
        merge_panel.P = self.processed
        merge_panel.CW = cw_path
        merge_panel.OUT = self.processed / "should_not_exist.csv"
        with self.assertRaises(ValueError):
            merge_panel.main()


if __name__ == "__main__":
    unittest.main()
