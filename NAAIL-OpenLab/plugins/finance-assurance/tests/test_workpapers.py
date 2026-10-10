import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from naail_finance import finance_workpaper, money


class WorkpaperTests(unittest.TestCase):
    def test_journal_balances_and_evidence(self):
        data = {"lines":[{"account":"Rent expense","debit":250,"evidence_ref":"SYN-1"},
                         {"account":"Accrued payable","credit":250,"evidence_ref":"SYN-1"}]}
        x = finance_workpaper("journal-entry", data)
        self.assertTrue(x["result"]["ready_for_review"])
        self.assertEqual(x["status"], "DRAFT_REQUIRES_HUMAN_REVIEW")
        self.assertFalse(finance_workpaper("journal-entry",
            {"lines":[{"debit":100},{"credit":99}]} )["result"]["balanced"])

    def test_reconciliation_and_missing_evidence(self):
        data = {"bank_balance":1060,"gl_balance":1120,
                "deposits_in_transit":[{"amount":100,"evidence_ref":"SYN-DEPOSIT"}],
                "outstanding_checks":[{"amount":40,"evidence_ref":"SYN-CHECK"}]}
        x=finance_workpaper("reconciliation",data)["result"]
        self.assertTrue(x["numerically_reconciled"])
        self.assertEqual(x["unreconciled_difference"],"0.00")
        data["outstanding_checks"][0].pop("evidence_ref")
        self.assertFalse(finance_workpaper("reconciliation",data)["result"]["ready_for_review"])

    def test_income_statement(self):
        x=finance_workpaper("income-statement",{"accounts":[
            {"kind":"revenue","current":115,"prior":100},
            {"kind":"expense","current":70,"prior":65}]})["result"]
        self.assertEqual(x["income"],"45.00")
        self.assertEqual(x["prior_income"],"35.00")

    def test_variance_zero_base(self):
        x=finance_workpaper("variance-analysis",{"items":[
            {"account":"X","actual":10,"comparison":0}]})["result"]["items"][0]
        self.assertIsNone(x["difference_percent"])
        self.assertTrue(x["unexplained"])

    def test_sox_sample_reproducible(self):
        data={"control_id":"C1","sample_size":2,"seed":42,"population":[
            {"id":"a","evidence_ref":"SYN-A"}, {"id":"b","exception":True},
            {"id":"c","evidence_ref":"SYN-C"}]}
        a=finance_workpaper("sox-testing",data)
        b=finance_workpaper("sox-testing",data)
        self.assertEqual(a,b)
        self.assertEqual(a["result"]["conclusion"],"NO_CONTROL_EFFECTIVENESS_CONCLUSION")
        with self.assertRaises(ValueError):
            finance_workpaper("sox-testing",{**data,"sample_size":4})

    def test_input_guardrails(self):
        with self.assertRaises(ValueError):
            money("NaN")
        with self.assertRaises(ValueError):
            finance_workpaper("journal-entry",{"lines":[]})
        with self.assertRaises(ValueError):
            finance_workpaper("sox-testing",{"control_id":"C","sample_size":1,
              "population":[{"id":"a"},{"id":"a"}]})


if __name__ == "__main__":
    unittest.main()
