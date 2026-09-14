# NAAIL OpenLab™ — Prototype 003-C SEC Evidence Snapshot

**Status:** Public research-safe evidence checkpoint  
**Current public release:** v0.2.2  
**Development milestone:** Prototype 003-C  
**Verified:** 2026-09-14

## Scope

Prototype 003-C uses exactly three real-company SEC filing anchors:

1. Microsoft Corporation (`MSFT`, CIK `0000789019`)
2. Alphabet Inc. (`GOOGL`, CIK `0001652044`)
3. Amazon.com, Inc. (`AMZN`, CIK `0001018724`)

The real-company evidence layer is restricted to SEC EDGAR / Form 10-K / iXBRL. No fourth issuer is permitted without a versioned scope change.

## Verified filing anchors

| Issuer | Form | Period of report | Filing date | SEC accession | Primary iXBRL document |
|---|---|---|---|---|---|
| Microsoft | 10-K | 2026-06-30 | 2026-07-29 | `0001193125-26-323660` | `msft-20260630.htm` |
| Alphabet | 10-K | 2025-12-31 | 2026-02-05 | `0001652044-26-000018` | `goog-20251231.htm` |
| Amazon | 10-K | 2025-12-31 | 2026-02-06 | `0001018724-26-000004` | `amzn-20251231.htm` |

Canonical SEC filing indexes:

- Microsoft: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm
- Alphabet: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/0001652044-26-000018-index.htm
- Amazon: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/0001018724-26-000004-index.htm

## Selected accounting evidence

The following items are direct filing observations used only to seed the evidence-normalization contract.

### Microsoft

- Goodwill is tested annually at the reporting-unit level on May 1 and between annual tests when triggering events occur.
- No goodwill impairment was identified in the May 1, 2024, May 1, 2025, or May 1, 2026 annual tests.
- Accumulated goodwill impairment was reported as **$11.3 billion** as of June 30, 2026 and 2025.
- Net finite-lived intangible assets at June 30, 2026 were reported as **$18.609 billion**.

### Alphabet

- Goodwill is tested at least annually, or more frequently when events or changes in circumstances indicate potential impairment.
- Goodwill impairments were reported as not material for the periods presented.
- Total goodwill at December 31, 2025 was **$33.380 billion**.

### Amazon

- The required annual goodwill and indefinite-lived intangible-asset impairment test was completed as of April 1, 2025 and resulted in **no impairments**.
- Amazon reported that the fair value of its reporting units substantially exceeded carrying value for that test.
- Total goodwill at December 31, 2025 was **$23.273 billion**.

## Research firewall

These filings are **evidence anchors**, not benchmark gold labels.

Prototype 003-C may create controlled or synthetic transformations for research, but those transformations must live in a separate namespace and must never be represented as real-company facts.

The project must not infer or claim, without direct authoritative evidence:

- an undisclosed goodwill impairment;
- an audit failure;
- an ICFR deficiency;
- that management estimates are wrong; or
- a cross-company audit-quality ranking.

## Engineering status

The private R&D implementation now includes:

- frozen three-company configuration;
- SEC CompanyFacts/filing ingestion scaffold;
- SHA-256 evidence hashing;
- tests that reject any fourth issuer;
- tests that preserve the real-evidence / controlled-scenario boundary;
- `source_manifest_v1.json` with pinned accessions and public accounting observations;
- GitHub Actions CI for the P003-C scope and firewall tests.

This checkpoint does **not** mean that the full Prototype 003-C benchmark has been completed. The next gate is to execute the live SEC ingestion, persist reproducible raw-source hashes and normalized evidence records, then construct the controlled scenarios and frozen gold labels.

## Scientific invariant

**Same source evidence. Same scenario. Same gold labels. Same evaluator. Different execution architecture.**

Real-company evidence remains immutable; benchmark perturbations remain explicitly synthetic or controlled.
