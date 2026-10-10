import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path

MOD = Path(__file__).resolve().parents[1] / "src" / "journal_task.py"
spec = importlib.util.spec_from_file_location("naail_journal_task", MOD)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class JournalTaskTests(unittest.TestCase):
    def write_registry(self, path, rows):
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=module.COLUMNS)
            writer.writeheader()
            writer.writerows(rows)

    def test_empty_registry_does_not_invent_articles(self):
        with tempfile.TemporaryDirectory() as td:
            registry, output = Path(td)/"registry.csv", Path(td)/"output"
            self.write_registry(registry, [])
            result = module.run("systematic-review", "ALL", registry, output)
            self.assertEqual(result["candidate_count"], 0)
            self.assertFalse(result["retrieval_performed"])
            self.assertFalse(result["empirical_claims_verified"])
            self.assertIn("NOT PERFORMED", (output/"weekly_research_report.md").read_text())

    def test_duplicate_study_blocked(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)/"registry.csv"
            record = dict.fromkeys(module.COLUMNS, "")
            record.update(study_id="A", title="Example only", journal="Test", year="2025")
            self.write_registry(p, [record, record])
            rows, problems = module.validate_registry(p)
            self.assertEqual(len(rows), 2)
            self.assertTrue(any("duplicate" in p for p in problems))

    def test_unverified_claim_requires_url(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)/"registry.csv"
            record = dict.fromkeys(module.COLUMNS, "")
            record.update(study_id="B", title="Example only", journal="Test",
                          year="2025", evidence_status="VERIFIED")
            self.write_registry(p, [record])
            _, problems = module.validate_registry(p)
            self.assertTrue(any("without source_url" in x for x in problems))

    def test_invalid_registry_schema_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)/"registry.csv"
            p.write_text("study_id,title\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                module.validate_registry(p)

if __name__ == "__main__":
    unittest.main()
