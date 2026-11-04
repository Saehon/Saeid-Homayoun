import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import tokenizers

from token_risk_profile import (
    HF_COMPONENT,
    HF_COMPONENT_VERSION,
    HF_PRETRAINED_MODEL_INFERENCE_EXECUTED,
    LEXICON,
    compile_lexicon,
    normalize_tokens,
    normalized_fingerprint,
    profile_record,
    prepare_private_output_dir,
    safe_density,
    scan_tokens,
    validate_expected_sha256,
)


class TokenRiskProfileTests(unittest.TestCase):
    def test_normalization_is_unicode_html_and_hyphen_stable(self):
        left = normalize_tokens("Ｆａｉｒ‑value &amp; COMPANY’S estimates")
        right = normalize_tokens("fair value & company's estimates")
        self.assertEqual(left, right)
        self.assertEqual(left, ("fair", "value", "company's", "estimates"))

    def test_hugging_face_component_is_explicit_and_local(self):
        self.assertIn("tokenizers.normalizers.Sequence", HF_COMPONENT)
        self.assertIn("tokenizers.pre_tokenizers.Split", HF_COMPONENT)
        self.assertEqual(HF_COMPONENT_VERSION, tokenizers.__version__)
        self.assertIs(HF_PRETRAINED_MODEL_INFERENCE_EXECUTED, False)
        self.assertEqual(normalize_tokens("a_b — c"), ("a", "b", "c"))

    def test_longest_match_prevents_phrase_component_double_count(self):
        categories, terms = scan_tokens(
            normalize_tokens("Significant auditor judgment and judgment were required.")
        )
        self.assertEqual(categories["audit_attention"], 1)
        self.assertEqual(categories["estimation_uncertainty"], 1)
        self.assertEqual(sum(terms.values()), 2)

    def test_scan_does_not_create_phrase_across_text_fields(self):
        row = {
            "CRITICAL_AUDIT_MATTER_KEY": "1",
            "AUDIT_OPINION_FKEY": "2",
            "COMPANY_KEY": "3",
            "TOPIC_NAME": "Inventory",
            "TITLE": "fair",
            "DESCRIPTION": "value",
            "RESPONSE": "",
        }
        crosswalk = {
            "account_domains": "INV",
            "mapping_status": "controlled_topic_assignment",
            "mapping_version": "test",
        }
        profiled, _ = profile_record(row, crosswalk)
        self.assertEqual(profiled["valuation_complexity_hits"], 0)
        self.assertEqual(profiled["title_valuation_complexity_hits"], 0)
        self.assertEqual(profiled["description_valuation_complexity_hits"], 0)
        self.assertEqual(profiled["response_missing"], True)
        self.assertEqual(profiled["total_tokens"], 2)
        self.assertEqual(profiled["cam_status"], "1")
        self.assertEqual(profiled["icfr_status"], "U")
        self.assertEqual(profiled["construct_status"], "post_selection_descriptive_proxy")
        self.assertEqual(profiled["risk_independent_eligible"], "false")
        self.assertEqual(profiled["title_description_risk_language_hits"], 0)
        self.assertEqual(profiled["hf_component"], HF_COMPONENT)
        self.assertEqual(profiled["hf_component_version"], tokenizers.__version__)
        self.assertEqual(profiled["hf_pretrained_model_inference_executed"], "false")

    def test_fingerprint_uses_field_boundaries(self):
        first = {"TITLE": ("a",), "DESCRIPTION": ("b",), "RESPONSE": ()}
        second = {"TITLE": (), "DESCRIPTION": ("a", "b"), "RESPONSE": ()}
        self.assertNotEqual(normalized_fingerprint(first), normalized_fingerprint(second))

    def test_custom_lexicon_rejects_duplicate_normalized_term(self):
        with self.assertRaises(ValueError):
            compile_lexicon({"a": ("fair-value",), "b": ("fair value",)})

    def test_all_terms_compile_and_density_handles_zero(self):
        compiled = compile_lexicon(LEXICON)
        self.assertTrue(compiled)
        self.assertEqual(safe_density(4, 200), 20.0)
        self.assertEqual(safe_density(4, 0), 0.0)

    def test_response_is_excluded_from_primary_narrative_proxy(self):
        row = {
            "CRITICAL_AUDIT_MATTER_KEY": "1",
            "AUDIT_OPINION_FKEY": "2",
            "COMPANY_KEY": "3",
            "TOPIC_NAME": "Inventory",
            "TITLE": "Inventory",
            "DESCRIPTION": "Ordinary disclosure",
            "RESPONSE": "Material weakness and impairment",
        }
        crosswalk = {
            "account_domains": "INV",
            "mapping_status": "controlled_topic_assignment",
            "mapping_version": "test",
        }
        profiled, _ = profile_record(row, crosswalk)
        self.assertEqual(profiled["title_description_risk_language_hits"], 0)
        self.assertEqual(profiled["response_risk_language_hits"], 2)

    def test_sha_validation_and_private_output_guard(self):
        digest = "a" * 64
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
