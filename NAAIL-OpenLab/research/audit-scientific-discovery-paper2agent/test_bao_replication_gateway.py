import tempfile
import unittest
from pathlib import Path
from bao_replication_gateway import assess, git_blob, main, EXPECTED_BLOBS

class AuthorGateTests(unittest.TestCase):
    def test_missing_author_data_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            result=assess(tmp)
            self.assertFalse(result["all_original_code_blobs_match"])
            self.assertEqual(result["empirical_replication_status"],"BLOCKED_PENDING_RIGHTS_ENVIRONMENT_AND_REVIEW")
    def test_git_blob_algorithm(self):
        self.assertEqual(git_blob(b"hello\n"),"ce013625030ba8dba906f756967f9e9ca394464a")
    def test_dry_run_export(self):
        with tempfile.TemporaryDirectory() as tmp:
            result=main(["--source-dir",tmp,"--out",str(Path(tmp)/"gate.json")])
            self.assertEqual(result["execution"]["status"],"DRY_RUN_ONLY")
            self.assertTrue((Path(tmp)/"gate.json").is_file())
    def test_executing_without_rights_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            result=main(["--source-dir",tmp,"--execute","--out",str(Path(tmp)/"gate.json")])
            self.assertEqual(result["execution"]["status"],"BLOCKED")
            self.assertTrue(any("rights" in s for s in result["execution"]["reasons"]))

if __name__=="__main__":
    unittest.main()
