import csv
import tempfile
import unittest
from pathlib import Path

import build_validation_sample as sample


def candidate(
    key: str,
    *,
    domain: str = "EQ",
    band: str = "LOW",
    linked: bool = False,
    year: int | None = None,
    company: str | None = None,
    fingerprint: str | None = None,
) -> sample.Candidate:
    return sample.Candidate(
        matter_key=key,
        company_key=company or f"company-{key}",
        opinion_key=f"opinion-{key}",
        source_topic="Synthetic topic",
        title="Synthetic title",
        description="Synthetic description",
        assigned_domain=domain,
        all_mapped_domains=(domain,) if domain != "UNMAPPED" else (),
        assignment_domain_frequency=10,
        band=band,
        score=float(key.strip("x") or 0) if key.strip("x").isdigit() else 1.0,
        linked=linked,
        fiscal_year=year,
        fiscal_year_status="provisional_opinion_year_crosswalk" if linked else "unavailable",
        fingerprint=fingerprint or (key.encode().hex() + "0" * 64)[:64],
        hf_component="tokenizers.synthetic",
        hf_component_version="test",
        hf_pretrained_model_inference_executed="false",
    )


class ValidationSampleTests(unittest.TestCase):
    def test_rarest_domain_and_alphabetical_tie_break(self):
        rows = [{"account_domain": "REV"}, {"account_domain": "EQ"}]
        assigned, mapped = sample.assign_rarest_domain(rows, {"REV": 20, "EQ": 3})
        self.assertEqual(assigned, "EQ")
        self.assertEqual(mapped, ("EQ", "REV"))

        assigned, _ = sample.assign_rarest_domain(rows, {"REV": 3, "EQ": 3})
        self.assertEqual(assigned, "EQ")

    def test_quantiles_and_threshold_ties_stay_in_lower_band(self):
        self.assertEqual(sample.quantile_linear([0.0, 3.0], 1 / 3), 1.0)
        self.assertEqual(sample.assign_band(1.0, 1.0, 2.0), "LOW")
        self.assertEqual(sample.assign_band(2.0, 1.0, 2.0), "MID")
        self.assertEqual(sample.assign_band(2.0001, 1.0, 2.0), "HIGH")

    def test_spreadsheet_formula_prefix_is_neutralized(self):
        for unsafe in ("=1+1", " +cmd", "\t@SUM(A1:A2)", "-2"):
            safe, changed = sample.spreadsheet_safe_text(unsafe)
            self.assertTrue(changed)
            self.assertTrue(safe.startswith("'"))
        safe, changed = sample.spreadsheet_safe_text("Ordinary narrative")
        self.assertFalse(changed)
        self.assertEqual(safe, "Ordinary narrative")

    def test_exact_selection_covers_years_and_enforces_uniqueness(self):
        rows = [
            candidate(str(year), linked=True, year=year, company=f"c{year}")
            for year in sample.TARGET_YEARS
        ]
        # Two early candidates share a company and fingerprint. The fill loop
        # must skip one and still meet the unlinked quota from later rows.
        rows.extend(
            [
                candidate("x1", band="MID", company="dup", fingerprint="a" * 64),
                candidate("x2", band="MID", company="dup", fingerprint="b" * 64),
                candidate("x3", band="MID", company="unique", fingerprint="c" * 64),
            ]
        )
        quotas = {("EQ", "LOW", "LINKED"): 5, ("EQ", "MID", "UNLINKED"): 2}
        chosen, qa = sample.select_with_quotas(
            rows,
            quotas,
            seed=sample.SEED,
            phase="synthetic",
            year_mode="per_stratum",
            attempts=10,
        )
        self.assertEqual(len(chosen), 7)
        self.assertEqual(len({row.company_key for row in chosen}), 7)
        self.assertEqual(len({row.fingerprint for row in chosen}), 7)
        self.assertTrue(qa["exact_quotas_met"])
        self.assertEqual(
            qa["linked_year_coverage"]["EQ|LOW|LINKED"], list(sample.TARGET_YEARS)
        )

    def test_quota_totals_and_required_design(self):
        main = sample.main_quotas()
        pilot = sample.pilot_quotas()
        self.assertEqual(sum(main.values()), 800)
        self.assertEqual(sum(pilot.values()), 30)
        for domain in sample.CANONICAL_DOMAINS:
            for band in sample.BANDS:
                self.assertEqual(main[(domain, band, "LINKED")], 8)
                self.assertEqual(main[(domain, band, "UNLINKED")], 12)
        self.assertEqual(
            [
                main[("UNMAPPED", band, "LINKED")]
                + main[("UNMAPPED", band, "UNLINKED")]
                for band in sample.BANDS
            ],
            [27, 26, 27],
        )

    def test_reviewer_codebook_uses_zero_to_three_and_evidence_offsets(self):
        rating_fields = [field for field in sample.REVIEW_FIELDS if field.endswith("_0_to_3")]
        self.assertEqual(len(rating_fields), 5)
        self.assertFalse(any("overall_risk_language_1_to_5" in f for f in sample.REVIEW_FIELDS))
        for name, abbreviation in sample.DIMENSIONS:
            for span_number in (1, 2, 3):
                prefix = f"{name}_{abbreviation}_evidence_span_{span_number}"
                self.assertIn(f"{prefix}_source_field", sample.REVIEW_FIELDS)
                self.assertIn(
                    f"{prefix}_start_0_based_inclusive", sample.REVIEW_FIELDS
                )
                self.assertIn(
                    f"{prefix}_end_0_based_exclusive", sample.REVIEW_FIELDS
                )
                self.assertIn(f"{prefix}_exact_quote", sample.REVIEW_FIELDS)
                self.assertIn(
                    f"{prefix}_extended_reason_if_over_40_tokens",
                    sample.REVIEW_FIELDS,
                )
            self.assertIn(
                f"{name}_{abbreviation}_rationale_one_sentence",
                sample.REVIEW_FIELDS,
            )
        for field in (
            "audit_attention_only",
            "procedure_language_intrusion",
            "negation_or_resolution",
            "insufficient_context",
            "unable_to_code",
            "confidence",
            "reviewer_note",
        ):
            self.assertIn(field, sample.REVIEW_FIELDS)
        self.assertNotIn("cannot_rate_0_or_1", sample.REVIEW_FIELDS)
        self.assertNotIn("coder_confidence_1_to_5", sample.REVIEW_FIELDS)

    def test_worked_example_quotes_match_half_open_offsets(self):
        with tempfile.TemporaryDirectory() as tmp:
            metadata = sample.write_worked_example(Path(tmp))
            output = Path(tmp) / metadata["output"]["filename"]
            with output.open(encoding="utf-8", newline="") as handle:
                row = next(csv.DictReader(handle))
            self.assertEqual(
                row["label_status"], "demonstration_only_not_human_validation"
            )
            self.assertEqual(row["valuation_complexity_VC_0_to_3"], "2")
            for name, abbreviation in sample.DIMENSIONS:
                populated = 0
                for span_number in (1, 2, 3):
                    prefix = f"{name}_{abbreviation}_evidence_span_{span_number}"
                    quote = row[f"{prefix}_exact_quote"]
                    if not quote:
                        continue
                    populated += 1
                    field = row[f"{prefix}_source_field"]
                    start = int(row[f"{prefix}_start_0_based_inclusive"])
                    end = int(row[f"{prefix}_end_0_based_exclusive"])
                    source_text = row[field.lower()]
                    self.assertEqual(source_text[start:end], quote)
                self.assertGreaterEqual(populated, 1)

    def test_adjudication_template_has_three_exact_span_slots(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = sample.write_adjudication_template(
                [candidate("1")], Path(tmp), "pilot", sample.SEED
            )
            with path.open(encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                rows = list(reader)
            self.assertEqual(len(rows), 5)
            self.assertEqual({row["dimension_code"] for row in rows}, {"EU", "AO", "VC", "FL", "ORL"})
            for span_number in (1, 2, 3):
                prefix = f"adjudicated_evidence_span_{span_number}"
                self.assertIn(f"{prefix}_source_field", reader.fieldnames)
                self.assertIn(f"{prefix}_start_0_based_inclusive", reader.fieldnames)
                self.assertIn(f"{prefix}_end_0_based_exclusive", reader.fieldnames)
                self.assertIn(f"{prefix}_exact_quote", reader.fieldnames)
                self.assertIn(
                    f"{prefix}_extended_reason_if_over_40_tokens", reader.fieldnames
                )
            self.assertIn("controlling_anchor_or_exclusion_max_300_chars", reader.fieldnames)
            self.assertIn("disagreement_type", reader.fieldnames)

    def test_reviewer_form_has_protocol_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            selected = [candidate("1")]
            sample.write_reviewer_files(selected, Path(tmp), "pilot", sample.SEED)
            path = Path(tmp) / "CAM_validation_pilot_reviewer_A_PRIVATE.csv"
            with path.open(encoding="utf-8", newline="") as handle:
                row = next(csv.DictReader(handle))
            self.assertEqual(row["protocol_id"], "CAM-RL-HVA")
            self.assertEqual(row["codebook_version"], "0.9.0")
            self.assertTrue(row["case_id"].startswith("P-"))
            self.assertEqual(row["reviewer_id_pseudonym"], "REVIEWER_A")
            self.assertEqual(row["assignment_batch"], "pilot_round_1")
            self.assertEqual(row["display_order"], "1")
            self.assertEqual(row["started_at_utc"], "")
            self.assertEqual(row["submitted_at_utc"], "")
            self.assertEqual(row["form_software_version"], "csv-1.0.0")

    def test_supplied_exclusions_are_checked_without_embedding_private_key(self):
        rows = [candidate(str(i)) for i in range(30)]
        checks = sample._pilot_only_checks(rows, frozenset({"reserved-private-key"}))
        self.assertTrue(checks["supplied_excluded_matters_absent"])

    def test_private_output_guard_ignores_empty_runtime_sentinel_but_blocks_git(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            empty_marker = root / ".git"
            empty_marker.mkdir()
            private_output = root / "private-output"
            self.assertEqual(
                sample.prepare_private_output_dir(private_output),
                private_output.resolve(),
            )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            marker = root / ".git"
            marker.mkdir()
            (marker / "HEAD").write_text("ref: refs/heads/main\n", encoding="utf-8")
            with self.assertRaises(sample.ValidationSampleError):
                sample.prepare_private_output_dir(root / "private-output")


if __name__ == "__main__":
    unittest.main()
