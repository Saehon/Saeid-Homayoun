"""Offline regression tests; no SEC requests, no Drive or GitHub writes."""
import unittest
from datetime import date, datetime, timezone
from pit_guards import *

class TestGuards(unittest.TestCase):
    def test_extra_pipe(self):
        s = "001 | A | 0001090872 | Agilent | P2\n326 | RMD | 0000943819 | ResMed | Incorporated | P2"
        self.assertEqual(len(parse_roster(s)), 2)
    def test_duplicate(self):
        rows = [{"CIK10":"0000000001"}, {"CIK10":"0000000001"}]
        self.assertIn("DUPLICATE_CIK10", validate_pilot(rows, expected=2))
    def test_claude_fy_is_only_structural(self):
        self.assertEqual(validate_pilot([{"CIK10":"0000000001","CLAUDE_FIRST_FY":"2020","CLAUDE_LAST_FY":"2024"}], expected=1), [])
    def test_quoted_csv(self):
        self.assertEqual(parse_quoted_csv('company,year\n"A, Inc.",2024\n')[0]["company"], "A, Inc.")
    def test_pit_no_lookahead(self):
        t = datetime(2025,2,20,tzinfo=timezone.utc)
        self.assertEqual(pit_filing_status("10-K", date(2024,12,31), t, datetime(2024,12,31,tzinfo=timezone.utc)), "NOT_YET_PUBLIC_AS_OF")
        self.assertEqual(pit_filing_status("10-K/A", date(2024,12,31), t, t), "AMENDMENT_REQUIRES_MATERIALITY_REVIEW")
        self.assertEqual(pit_filing_status("NT 10-K", date(2024,12,31), t, t), "NOTICE_ONLY_NOT_10K")
    def test_index_membership(self):
        e=[{"announcement_at":datetime(2025,9,5,tzinfo=timezone.utc),"effective_at":datetime(2025,9,22,tzinfo=timezone.utc),"membership":"SP500"}]
        self.assertEqual(index_membership_asof(e,datetime(2024,12,31,tzinfo=timezone.utc)),"UNKNOWN")
        self.assertEqual(index_membership_asof(e,datetime(2025,9,23,tzinfo=timezone.utc)),"SP500")
    def test_safety_block(self):
        row={"CIK10":"0000000001","destination":"M36","provenance":"SEC"}
        with self.assertRaises(PermissionError):
            validate_write_plan([row], safety_block=True)
        with self.assertRaises(ValueError):
            validate_write_plan([row]*21)

if __name__=="__main__":
    unittest.main()
