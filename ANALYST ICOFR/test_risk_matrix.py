"""Synthetic fixtures only: these tests are not empirical CAM–ICFR results."""

import itertools
import unittest

import numpy as np
import pandas as pd

from risk_matrix import evaluate_risk_matrix, state_id


def synthetic_row(firm, account="A", risk=0.0, **updates):
    row = dict(firm=firm, account=account, fiscal_year=2024, industry="synthetic",
               risk_score=risk, risk_independent=True, decision_date="2025-01-15",
               available_date="2025-01-01", eligible=True,
               eligible_set_complete=False, icfr_state="E",
               cam_positive_confirmed=False, report_applicable=True,
               period_verified=True, cam_capture_complete=True, mapping_complete=True)
    row.update(updates)
    return row


class RiskMatrixSyntheticTests(unittest.TestCase):
    def test_linear_threshold_keeps_all_ties_high(self):
        # 20 scores: indices 13 and 14 both equal 14, so linear q=.7 is 14.
        values = list(range(13)) + [14, 14] + list(range(15, 20))
        result = evaluate_risk_matrix(pd.DataFrame([
            synthetic_row(f"s{i}", risk=value) for i, value in enumerate(values)
        ]))
        self.assertTrue(result.peer_threshold.eq(14).all())
        self.assertTrue(result.peer_distinct_firms.eq(20).all())
        self.assertEqual(result.loc[result.risk_score.eq(14), "risk_state"].tolist(), ["H", "H"])
        self.assertEqual(result.risk_state.value_counts().to_dict(), {"L": 13, "H": 7})

    def test_nineteen_admissible_peers_remain_unknown(self):
        rows = [synthetic_row(f"s{i}", risk=i) for i in range(20)]
        rows[-1]["risk_independent"] = False
        result = evaluate_risk_matrix(pd.DataFrame(rows))
        self.assertTrue(result.peer_distinct_firms.eq(19).all())
        self.assertTrue(result.peer_insufficient.all())
        self.assertTrue(result.risk_state.eq("U").all())
        self.assertTrue(result.peer_threshold.isna().all())

    def test_constant_group_is_unknown_with_explicit_flag(self):
        result = evaluate_risk_matrix(pd.DataFrame([
            synthetic_row(f"s{i}", risk=0) for i in range(20)
        ]))
        self.assertTrue(result.peer_no_variation.all())
        self.assertFalse(result.peer_insufficient.any())
        self.assertTrue(result.risk_state.eq("U").all())
        self.assertTrue(result.peer_threshold.isna().all())

    def test_missing_industry_and_missing_risk_are_unknown(self):
        rows = [synthetic_row(f"s{i}", risk=i) for i in range(20)]
        rows[0]["industry"] = None
        rows[1]["risk_score"] = np.nan
        result = evaluate_risk_matrix(pd.DataFrame(rows))
        self.assertTrue(result.iloc[0].peer_group_missing)
        self.assertTrue(result.iloc[1].risk_score_missing)
        self.assertEqual(result.iloc[0].risk_state, "U")
        self.assertEqual(result.iloc[1].risk_state, "U")

    def test_future_peer_is_not_used_by_earlier_decision(self):
        rows = [synthetic_row(f"s{i}", risk=i) for i in range(20)]
        rows[-1].update(available_date="2025-02-01", decision_date="2025-02-15")
        result = evaluate_risk_matrix(pd.DataFrame(rows))
        self.assertEqual(result.iloc[0].peer_distinct_firms, 19)
        self.assertEqual(result.iloc[0].risk_state, "U")
        self.assertEqual(result.iloc[-1].peer_distinct_firms, 20)
        self.assertFalse(result.iloc[-1].risk_temporal_violation)

    def test_future_own_risk_is_flagged_and_not_classified(self):
        rows = [synthetic_row(f"s{i}", risk=i) for i in range(21)]
        rows[0]["available_date"] = "2025-01-16"
        result = evaluate_risk_matrix(pd.DataFrame(rows))
        self.assertTrue(result.iloc[0].risk_temporal_violation)
        self.assertFalse(result.iloc[0].risk_measure_admissible)
        self.assertEqual(result.iloc[0].risk_state, "U")
        self.assertEqual(result.iloc[1].peer_distinct_firms, 20)

    def competitor_fixture(self, other_score=20):
        rows = [synthetic_row(f"peer{i}", account=account, risk=i)
                for account in ("A", "B") for i in range(20)]
        rows.extend([synthetic_row("focal", account="A", risk=10, eligible_set_complete=True),
                     synthetic_row("focal", account="B", risk=other_score, eligible_set_complete=True)])
        return pd.DataFrame(rows)

    def test_competition_uses_account_specific_thresholds(self):
        result = evaluate_risk_matrix(self.competitor_fixture())
        focal = result.loc[result.firm.eq("focal")].set_index("account")
        self.assertEqual(focal.loc["A", "peer_threshold"], 13)
        self.assertEqual(focal.loc["B", "peer_threshold"], 14)
        self.assertEqual(focal.loc["A", "Cmax"], 20)
        self.assertEqual(focal.loc["A", "Crank"], 1)
        self.assertEqual(focal.loc["A", "Ctail"], 6)
        self.assertEqual(focal.loc["A", "D"], -10)
        self.assertEqual(focal.loc["B", "Ctail"], 0)
        self.assertEqual(focal.loc["B", "D"], 10)

    def test_competition_rank_is_strict_and_ties_remain_zero_rank(self):
        result = evaluate_risk_matrix(self.competitor_fixture(other_score=10))
        focal = result.loc[result.firm.eq("focal")]
        self.assertTrue(focal.Crank.eq(0).all())
        self.assertTrue(focal.D.eq(0).all())

    def test_missing_competitor_does_not_create_zero(self):
        result = evaluate_risk_matrix(self.competitor_fixture(other_score=np.nan))
        focal = result.loc[result.firm.eq("focal")]
        self.assertFalse(focal.competition_score_eligible.any())
        self.assertTrue(focal[["Cmax", "Crank", "Ctail", "D"]].isna().all().all())

    def test_incomplete_roster_and_single_account_do_not_create_zero(self):
        data = self.competitor_fixture()
        data.loc[data.firm.eq("focal"), "eligible_set_complete"] = False
        result = evaluate_risk_matrix(data)
        self.assertTrue(result.loc[result.firm.eq("focal"), "Cmax"].isna().all())
        one = pd.DataFrame([synthetic_row("only", eligible_set_complete=True)])
        self.assertTrue(evaluate_risk_matrix(one).Cmax.isna().all())

    def test_future_competitor_blocks_earlier_focal_metrics(self):
        data = self.competitor_fixture()
        target = data.firm.eq("focal") & data.account.eq("B")
        data.loc[target, ["available_date", "decision_date"]] = ["2025-02-01", "2025-02-15"]
        result = evaluate_risk_matrix(data)
        early = result.loc[result.firm.eq("focal") & result.account.eq("A")].iloc[0]
        late = result.loc[result.firm.eq("focal") & result.account.eq("B")].iloc[0]
        self.assertFalse(early.competition_score_eligible)
        self.assertTrue(pd.isna(early.Cmax))
        self.assertTrue(late.competition_score_eligible)

    def test_unknown_eligibility_can_hide_competitor(self):
        data = self.competitor_fixture()
        data = pd.concat([data, pd.DataFrame([synthetic_row("focal", "C", risk=30,
                          eligible=None, eligible_set_complete=True)])], ignore_index=True)
        focal = evaluate_risk_matrix(data).query("firm == 'focal'")
        self.assertFalse(focal.competitor_set_complete.any())
        self.assertTrue(focal.Cmax.isna().all())

    def test_cam_zero_requires_every_negative_proof_gate(self):
        row = synthetic_row("synthetic")
        self.assertEqual(evaluate_risk_matrix(pd.DataFrame([row])).iloc[0].cam_state, "0")
        for gate in ("eligible", "report_applicable", "period_verified", "cam_capture_complete", "mapping_complete"):
            for unknown in (False, None):
                with self.subTest(gate=gate, unknown=unknown):
                    row = synthetic_row("synthetic", **{gate: unknown})
                    output = evaluate_risk_matrix(pd.DataFrame([row])).iloc[0]
                    self.assertEqual(output.cam_state, "U")
                    self.assertFalse(output.cam_negative_proven)

    def test_positive_precedence_does_not_bypass_model_gates(self):
        row = synthetic_row("synthetic", cam_positive_confirmed=True,
                            eligible=False, period_verified=False, mapping_complete=False)
        result = evaluate_risk_matrix(pd.DataFrame([row])).iloc[0]
        self.assertEqual(result.cam_state, "1")
        self.assertFalse(result.cam_model_eligible)
        self.assertFalse(result.joint_model_eligible)
        self.assertEqual(result.state_id, "U1")

    def test_all_27_states_are_distinct_and_original_ids_preserved(self):
        states = list(itertools.product(("H", "L", "U"), ("E", "I", "U"), ("1", "0", "U")))
        self.assertEqual(len({state_id(*state) for state in states}), 27)
        expected = {( "H", "E", "1"): "A1", ("H", "E", "0"): "B1",
                    ("H", "I", "1"): "A2", ("H", "I", "0"): "B2",
                    ("H", "U", "1"): "A3", ("H", "U", "0"): "B3",
                    ("L", "E", "1"): "C1", ("L", "E", "0"): "D1",
                    ("L", "I", "1"): "C2", ("L", "I", "0"): "D2",
                    ("L", "U", "1"): "C3", ("L", "U", "0"): "D3"}
        for state, identifier in expected.items():
            self.assertEqual(state_id(*state), identifier)
        unknown_risk = {("E", "1"): "U1", ("E", "0"): "U2",
                        ("I", "1"): "U3", ("I", "0"): "U4",
                        ("U", "1"): "U5", ("U", "0"): "U6"}
        for (icfr, cam), identifier in unknown_risk.items():
            self.assertEqual(state_id("U", icfr, cam), identifier)
        for risk, icfr in itertools.product(("H", "L", "U"), ("E", "I", "U")):
            self.assertEqual(state_id(risk, icfr, "U"), f"CAMU_{icfr}_{risk}")

    def test_duplicate_grain_and_invalid_flags_are_rejected(self):
        row = synthetic_row("synthetic")
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            evaluate_risk_matrix(pd.DataFrame([row, row]))
        with self.assertRaisesRegex(ValueError, "evidence flags"):
            evaluate_risk_matrix(pd.DataFrame([synthetic_row("synthetic", eligible="false")]))
        with self.assertRaisesRegex(ValueError, "icfr_state"):
            evaluate_risk_matrix(pd.DataFrame([synthetic_row("synthetic", icfr_state="effective")]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
