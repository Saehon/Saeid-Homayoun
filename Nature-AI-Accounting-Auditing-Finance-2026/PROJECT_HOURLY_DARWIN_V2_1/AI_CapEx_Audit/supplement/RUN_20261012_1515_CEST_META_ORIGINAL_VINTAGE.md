# DARWIN V5: META original SEC 10-K vintage FCF reconciliation
Run: AI_CAPEX_DARWIN_V5_20261012_1515_CEST_META_ORIGINAL_FCF_VINTAGE
Time: 2026-10-12 15:15 CEST. Scientific status PARTIAL.
Original Drive input: secondary cashflow CSV ID 14RunpgmXgv8NIpUGfcM6pEdIO-ZONavy. Previous Meta QA 14:20 used only FY2025 filing. NEW task compares original FY2023 and FY2024 10-K filings with subsequent comparative vintages.
Primary SEC:
2023 filing 2024-02-02 accession 0001326801-24-000012 https://www.sec.gov/Archives/edgar/data/1326801/000132680124000012/meta-20231231.htm
2024 filing 2025-01-30 accession 0001326801-25-000017 https://www.sec.gov/Archives/edgar/data/1326801/000132680125000017/meta-20241231.htm
2025 filing 2026-01-29 accession 0001628280-26-003942 https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
One issuer CIK 0001326801, three firm-years, six filing-vintage rows. USD millions CFO / cash PPE / finance lease principal / company FCF:
FY2023 71113/27045/1058/43010 (3 vintages agree);
FY2024 91328/37256/1969/52103 (2 vintages agree);
FY2025 115800/69691/2524/43585 (1 vintage).
12 cross-vintage numeric comparisons; 0 discrepancies. 6/6 FCF arithmetic identities. Executed local python -m unittest: 18/18 PASS; py_compile PASS. Input data manually transcribed from official SEC pages, not independent source-byte reproduction. AI-specific CapEx NULL, not 0. 0 causal models. Do not infer issuer-specific PCAOB inspections.
Five living outputs: manuscript unchanged; canonical sample unchanged; results QA only; variables/methods point-in-time FCF rule documented locally; local executable code and CSV/JSON tests. 8 scientific evidence gates incomplete, independent reproduction NOT_RUN, human review pending, Nature35 method NOT_USED. OPEN REPAIR QUEUE: SEC source byte hashes, AI-specific CapEx, Form AP 131274, PCAOB PDF hashes, writer lock unknown, CI prior SKIPPED, stale latest-status file quarantined. No merge or submission. Next independent task: original SEC-vintage lease/FCF check for another issuer.