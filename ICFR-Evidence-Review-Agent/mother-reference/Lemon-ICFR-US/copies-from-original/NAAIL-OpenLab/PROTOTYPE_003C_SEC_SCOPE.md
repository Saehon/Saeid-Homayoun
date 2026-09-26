# NAAIL OpenLab™ — Prototype 003-C SEC Scope

**Status:** Canonical public scope rule for Prototype 003-C  
**Updated:** 2026-09-14  
**Parent milestone:** Prototype 003  
**Case:** Goodwill Impairment / valuation-and-estimate evidence benchmark

## Hard scope rule

Prototype 003-C will use **only three public-company SEC anchors**:

1. **Microsoft Corporation**
2. **Alphabet Inc. (Google)**
3. **Amazon.com, Inc.**

No additional company should be added to Prototype 003-C unless this scope is explicitly changed in a later versioned decision.

## Authoritative data source

Use **SEC EDGAR only** for the real-company evidence layer.

Permitted primary evidence includes:
- Form 10-K;
- Inline XBRL / extracted XBRL;
- financial statements and notes contained in the filing;
- goodwill and intangible-asset disclosures;
- acquisition/business-combination disclosures;
- impairment-related disclosures where present;
- segment disclosures;
- accounting-policy disclosures;
- management estimates/judgments disclosed in the filing;
- auditor report / CAM information contained in the filed annual report where applicable.

Do not use blogs, news articles, analyst reports, social media, or vendor summaries as benchmark evidence.

## Current SEC anchor filings

At the time of this scope freeze, use the latest available annual filing for each anchor:

- **Microsoft Corporation** — Form 10-K for fiscal year ended **June 30, 2026**.
- **Alphabet Inc.** — Form 10-K for fiscal year ended **December 31, 2025**.
- **Amazon.com, Inc.** — Form 10-K for fiscal year ended **December 31, 2025**.

Each ingested filing must preserve accession number, filing date, period of report, CIK, source URL, filing hash, retrieval timestamp, and XBRL provenance where available.

## Research-safe transformation rule

The three SEC filings provide **real evidence anchors**, but the benchmark must not claim that any of the three companies has an undisclosed goodwill impairment, control deficiency, audit failure, or misstatement.

Prototype 003-C should transform the SEC evidence into controlled research objects such as:

1. **SEC Evidence Layer** — verbatim-source identifiers and structured filing facts;
2. **Normalized Accounting Layer** — comparable fields for goodwill, intangibles, acquisitions, segments, estimates, and impairment-related disclosures;
3. **Controlled Scenario Layer** — synthetic or perturbed assumptions used to create testable audit judgments;
4. **Frozen Gold Layer** — benchmark labels defined from the controlled scenario, not from unsupported conclusions about the real registrant;
5. **Agent Evaluation Layer** — identical evidence/gold/evaluation contract across execution architectures.

## Three-company evidence schema

For each company, capture at minimum:

- `company_id`
- `company_name`
- `cik`
- `fiscal_year_end`
- `filing_date`
- `accession_number`
- `sec_source_url`
- `filing_sha256`
- `goodwill_balance`
- `intangible_assets`
- `acquisition_activity`
- `segment_structure`
- `impairment_disclosure_present`
- `impairment_amount_if_reported`
- `critical_estimate_or_judgment_text_ref`
- `auditor_report_ref`
- `cam_or_critical_audit_evidence_ref_if_present`
- `xbrl_fact_refs`
- `evidence_passport_id`

Missing values must remain explicitly missing; do not infer undisclosed values.

## Prototype 003-C comparison design

The three companies are **evidence anchors**, not treatment groups for claims about audit quality.

The primary experiment remains architectural:

> Same evidence object. Same controlled scenario. Same frozen gold labels. Same evaluator. Different execution architecture.

Execution architectures:
1. deterministic baseline;
2. single-agent AI;
3. sequential-agent AI;
4. governed multi-agent AI.

The company dimension may be used for cross-context robustness, but the scientific target remains the effect of orchestration architecture on evidence grounding and professional judgment.

## Governance

Every completed P003-C run must preserve:

- Evidence Passport™;
- Professional Decision DAG™;
- Human Gate;
- SEC accession/source provenance;
- case and evidence hashes;
- model/provider/tool/agent metadata;
- frozen evaluator version;
- limitations and uncertainty;
- reviewer/critic output;
- run manifest.

## Prohibited interpretations

Prototype 003-C must not state or imply, without direct authoritative support, that:

- Microsoft, Alphabet, or Amazon should have recorded an impairment;
- their auditors failed to detect a misstatement;
- a disclosed estimate is incorrect;
- a CAM or audit conclusion is deficient;
- one company has better or worse audit quality than another.

Any controlled benchmark exception must be clearly labeled **synthetic / transformed research scenario**.

## Definition of done

P003-C is complete when the SEC evidence for all three companies is provenance-locked, normalized into a common schema, transformed into controlled frozen scenarios, evaluated under the four architectures, reproducible from the preserved filing sources, and safe for manuscript use without turning research simulation into unsupported company-specific claims.

## Scope invariant

```text
companies = [Microsoft, Alphabet, Amazon]
company_count = 3
primary_source = SEC_EDGAR
non_SEC_company_evidence_allowed = false
unsupported_real_company_audit_claims_allowed = false
```
