import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from darwin_token_risk import (
    COMPETITION_COMPLETENESS,
    add_descriptive_competition,
    classify_peer_groups,
    eligibility_reason,
    linear_quantile,
    matrix_state,
    normalize_sic,
    prepare_private_output_dir,
    split_account_domains,
    validate_expected_sha256,
)


def sample_row(company, score, account="REV", year=2024, sic2="73"):
    return {
        "company_key": company,
        "audit_opinion_fkey": f"op-{company}",
        "account_domain": account,
        "fiscal_year": year,
        "current_sic2": sic2,
        "title_description_tokens": 100,
        "cam_narrative_risk_language_density_per_1000_tokens": score,
    }


class DarwinTokenRiskTests(unittest.TestCase):
    def test_linear_quantile_matches_type7_interpolation(self):
        self.assertEqual(linear_quantile([0, 10], 0.7), 7.0)
        self.assertEqual(linear_quantile([0, 10, 20, 30], 0.5), 15.0)

    def test_sic_normalization_preserves_leading_division_zero(self):
        self.assertEqual(normalize_sic("111"), ("0111", "01"))
        self.assertEqual(normalize_sic("3720.0"), ("3720", "37"))
        self.assertEqual(normalize_sic("unknown"), ("", ""))

    def test_account_parser_handles_controlled_multi_domain_mapping(self):
        self.assertEqual(split_account_domains("GW|INT"), ("GW", "INT"))
        with self.assertRaises(ValueError):
            split_account_domains("REV|REV")
        with self.assertRaises(ValueError):
            split_account_domains("UNMAPPED|REV")

    def test_exact_q70_tie_is_high_and_small_groups_are_unknown(self):
        rows = [sample_row(str(index), float(index)) for index in range(20)]
        thresholds = classify_peer_groups(rows)
        threshold = linear_quantile(range(20), 0.7)
        self.assertEqual(thresholds[0]["peer_q70_threshold"], threshold)
        self.assertTrue(
            all(
                row["token_proxy_risk_level"]
                == ("H" if row["cam_narrative_risk_language_density_per_1000_tokens"] >= threshold else "L")
                for row in rows
            )
        )
        tied = [sample_row(str(index), 5.0) for index in range(20)]
        classify_peer_groups(tied)
        self.assertTrue(all(row["token_proxy_risk_level"] == "H" for row in tied))
        small = [sample_row(str(index), float(index)) for index in range(19)]
        classify_peer_groups(small)
        self.assertTrue(all(row["token_proxy_risk_level"] == "U" for row in small))

    def test_unknown_reasons_and_matrix_mapping(self):
        self.assertEqual(eligibility_reason(sample_row("x", 2.0, account="UNMAPPED")), "U_account_unmapped")
        self.assertEqual(eligibility_reason(sample_row("x", 2.0, year="")), "U_fiscal_year_unavailable")
        self.assertEqual(matrix_state("H"), "A3")
        self.assertEqual(matrix_state("L"), "C3")
        self.assertEqual(matrix_state("U"), "U5")

    def test_competition_metrics_are_observed_selected_cam_only(self):
        first = sample_row("1", 10.0, account="REV")
        second = sample_row("1", 20.0, account="INV")
        first["peer_q70_threshold"] = 12.0
        second["peer_q70_threshold"] = 15.0
        add_descriptive_competition([first, second])
        self.assertEqual(first["competitor_max_proxy"], 20.0)
        self.assertEqual(first["higher_proxy_account_count"], 1)
        self.assertEqual(first["competitor_tail_above_peer_q70"], 5.0)
        self.assertEqual(first["relative_proxy_distance"], -10.0)
        self.assertEqual(first["competition_completeness_status"], COMPETITION_COMPLETENESS)

    def test_sha_validation_and_private_output_guard(self):
        digest = "b" * 64
        self.assertEqual(validate_expected_sha256(digest.upper()), digest)
        with self.assertRaises(ValueError):
            validate_expected_sha256("not-a-sha")
        with TemporaryDirectory() as temporary:
            output = Path(temporary) / "new-private-output"
            self.assertEqual(prepare_private_output_dir(output), output.resolve())
            self.assertTrue(output.is_dir())
            with self.assertRaises(ValueError):
                prepare_private_output_dir(output)


if __name__ == "__main__":
    unittest.main()
