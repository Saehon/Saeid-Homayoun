import unittest
from asof_vintage_compact import select
P='inspection_vintage_events.csv'
class TestVintage(unittest.TestCase):
    def test_none_before_release(self): self.assertIsNone(select(P,'2024-02-27'))
    def test_2022_initial(self): self.assertEqual(select(P,'2024-03-01')['release'],'104-2024-035')
    def test_2022_amended(self): self.assertEqual(select(P,'2024-04-27')['release'],'104-2024-035a')
    def test_2023_before_cooper(self): self.assertEqual(select(P,'2024-12-06')['release'],'104-2024-109')
    def test_no_2024_at_report_date(self): self.assertEqual(select(P,'2025-02-27')['inspection_year'],2023)
    def test_2024_after_public_release(self): self.assertEqual(select(P,'2025-04-01')['release'],'104-2025-039')
    def test_no_retrospective_2022_rate(self): self.assertIsNone(select(P,'2024-03-01')['selected_sample_part_ia_rate'])
    def test_2023_rate(self): self.assertAlmostEqual(select(P,'2024-12-06')['selected_sample_part_ia_rate'],15/58)
    def test_2024_rate_future(self): self.assertAlmostEqual(select(P,'2025-04-01')['selected_sample_part_ia_rate'],13/64)
if __name__=='__main__': unittest.main()
