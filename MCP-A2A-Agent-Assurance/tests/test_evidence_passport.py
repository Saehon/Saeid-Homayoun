import copy
import json
import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from naail_agent_assurance.evidence import compute_content_hash, validate_passport  # noqa: E402


class EvidencePassportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = ROOT / "examples" / "evidence_passport.example.json"
        cls.example = json.loads(path.read_text(encoding="utf-8"))

    def test_example_passes(self):
        self.assertEqual(validate_passport(self.example), [])

    def test_hash_is_reproducible(self):
        self.assertEqual(compute_content_hash(self.example), self.example["content_sha256"])

    def test_unknown_evidence_is_rejected(self):
        item = copy.deepcopy(self.example)
        item["claims"][0]["evidence_refs"] = ["NOT-A-SOURCE"]
        item["content_sha256"] = compute_content_hash(item)
        errors = validate_passport(item)
        self.assertTrue(any("unknown evidence" in error for error in errors))

    def test_required_human_gate_cannot_be_bypassed(self):
        item = copy.deepcopy(self.example)
        item["human_approval"]["status"] = "not_required"
        item["content_sha256"] = compute_content_hash(item)
        errors = validate_passport(item)
        self.assertTrue(any("cannot be not_required" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
