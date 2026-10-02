# Correction Entry — 2026-10-02

This entry is additive. Historical run logs remain immutable.

## CORR-001 — RUN 021 duplicate case
RUN 021 selected DOI 10.1287/mnsc.2023.4670 as Case 002.
Case 001 already uses DOI 10.1287/mnsc.2023.4670.
Disposition: RUN 021 is retained as historical evidence, but the selection is invalid for V1 case-count purposes.
V1 valid additional cases from RUN 021: 0.

Required control:
case DOI must be unique across Case 001/002/003. Duplicate DOI => selection failure.

## CORR-002 — Microsoft matched-quarter vector
Canonical comparison: each post-period quarter versus the SAME 2019 quarter.
Correct vector: [+5, -2, +4, -3, +3, -3].

## CORR-003 — Microsoft combined assurance state
FilingLag uses SEC filing date minus fiscal period end in current code/records.
The COVID binary rule is not fully frozen (keywords are described as covid/corona, but exact section scope and matching protocol are absent).
Disposition: do not label the combined Microsoft public reconstruction VERIFIED/COMPLETE until the COVID rule is frozen and independently rerun.

## CORR-004 — Canonical phase numbering
Canonical master-plan numbering:
POC P0–P8.
V1 V1.1–V1.11.
Legacy P9/V1-0 labels may remain in historical logs but should not define new canonical phases.
