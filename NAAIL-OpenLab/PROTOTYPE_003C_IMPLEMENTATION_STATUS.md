# NAAIL OpenLab™ — Prototype 003-C Implementation Status

**Public-safe engineering checkpoint**  
**Date:** 2026-09-14  
**Current public release:** v0.2.2  
**Development target:** Prototype 003-C  

## Scope

Prototype 003-C is restricted to exactly three SEC public-company anchors:

1. Microsoft Corporation;
2. Alphabet Inc. (Google);
3. Amazon.com, Inc.

The real-company evidence layer is restricted to SEC EDGAR / Form 10-K / iXBRL CompanyFacts. No fourth issuer may enter the benchmark without an explicit versioned scope change.

## Current filing anchors

- Microsoft — FY ended 2026-06-30, Form 10-K.
- Alphabet — FY ended 2025-12-31, Form 10-K.
- Amazon — FY ended 2025-12-31, Form 10-K.

## Implementation completed in private R&D

The private Prototype 003-C scaffold now includes:

- a frozen three-issuer configuration;
- pinned filing accessions;
- a provider-neutral SEC CompanyFacts ingestor;
- a frozen goodwill/intangible/acquisition XBRL concept allowlist;
- canonical SHA-256 source/evidence hashing;
- one evidence-bundle contract per issuer;
- an explicit interpretation firewall separating real SEC evidence from controlled benchmark gold labels;
- automated tests that reject a fourth issuer.

Local scaffold validation passed **3/3 tests** on 2026-09-14.

## What is not yet claimed complete

This checkpoint does **not** claim that the full live three-company SEC ingestion, normalization, controlled scenario construction, Blind Gold creation, or four-architecture benchmark matrix is complete.

The next engineering gate is:

**live SEC ingestion → source manifests → concept-coverage review → normalized evidence tables → controlled scenario construction → frozen gold labels → four-architecture evaluation.**

## Research boundary

Microsoft, Alphabet, and Amazon filings are evidence anchors only. Any planted impairment issue, contradiction, exception, or gold conclusion belongs to a controlled research transformation and must never be described as an actual undisclosed impairment, audit failure, ICFR deficiency, or audit-quality finding for the registrant.

## Experimental invariant

**Same case. Same evidence. Same gold labels. Same evaluator. Different execution architecture.**

The execution architectures remain:

1. deterministic baseline;
2. single-agent AI;
3. sequential-agent AI;
4. governed multi-agent AI.

Every material run remains subject to Evidence Passport™, Professional Decision DAG™, Human Gate, provenance, reproducibility, and frozen evaluation rules.

## Release rule

Prototype 003-C is still development work. **v0.2.2 remains the current public release.** Candidate v0.3.0 must not be promoted until the full Prototype 003 release gates pass.
