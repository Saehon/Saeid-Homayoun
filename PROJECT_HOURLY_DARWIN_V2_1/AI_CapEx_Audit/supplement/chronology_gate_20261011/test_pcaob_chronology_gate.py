"""Chronology unit tests: actual PCAOB report/publication dates; hypothetical cutoffs."""
import unittest
from pcaob_chronology_gate import classify

class TestChronology(unittest.TestCase):
    def test_crowe_report_not_public_on_report_date(self):
        # PCAOB July 31 2025 release: Crowe LLP report dated May 22 2025.
        x = classify(dict(auditor_id='Crowe LLP', report_date='2025-05-22',
                          first_public_date='2025-07-31', information_cutoff='2025-06-30'))
        self.assertEqual(x['inspection_public_asof'], 0)

    def test_crowe_available_after_publication(self):
        x = classify(dict(auditor_id='Crowe LLP', report_date='2025-05-22',
                          first_public_date='2025-07-31', information_cutoff='2025-08-01'))
        self.assertEqual(x['inspection_public_asof'], 1)

    def test_2026_report_not_public_in_june(self):
        # PCAOB July 22 2026 release: EisnerAmper report dated June 11 2026.
        x = classify(dict(auditor_id='EisnerAmper LLP', report_date='2026-06-11',
                          first_public_date='2026-07-22', information_cutoff='2026-06-30'))
        self.assertEqual(x['inspection_public_asof'], 0)

    def test_reject_inverted_publication_date(self):
        with self.assertRaises(ValueError):
            classify(dict(auditor_id='X', report_date='2026-07-22',
                          first_public_date='2026-06-11', information_cutoff='2026-08-01'))

    def test_missing_cutoff_rejected(self):
        with self.assertRaises(ValueError):
            classify(dict(auditor_id='X', report_date='2026-06-11', first_public_date='2026-07-22'))

if __name__ == '__main__':
    unittest.main()
