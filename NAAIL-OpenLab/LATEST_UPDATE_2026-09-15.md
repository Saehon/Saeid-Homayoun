# NAAIL OpenLab™ — Latest GitHub Update

**Date:** 2026-09-15  
**Public release:** v0.2.3  
**Executable benchmark:** Prototype 003  
**Provider harness:** Prototype 004 infrastructure implemented; empirical provider execution remains credential-gated

## Prototype 003-C SEC integration

The Prototype 003-C evidence program is now frozen to exactly three SEC issuer anchors:

- Microsoft Corporation (`MSFT`, CIK `0000789019`)
- Alphabet Inc. (`GOOGL`, CIK `0001652044`)
- Amazon.com, Inc. (`AMZN`, CIK `0001018724`)

The real-company evidence layer is restricted to **SEC EDGAR / Form 10-K / iXBRL**. No fourth issuer may enter P003-C without an explicit versioned scope change.

## Implemented controls

```text
issuer scope lock                  = IMPLEMENTED
pinned filing accessions           = IMPLEMENTED
public SEC evidence snapshot       = IMPLEMENTED
private source manifest            = IMPLEMENTED
SEC ingestion scaffold             = IMPLEMENTED
SHA-256 hashing contract           = IMPLEMENTED
fourth-issuer rejection tests      = IMPLEMENTED
real/synthetic firewall tests      = IMPLEMENTED
GitHub Actions validation          = IMPLEMENTED
```

## Pending empirical gates

```text
live raw-source ingestion          = PENDING
persisted raw-source hashes        = PENDING
normalized evidence tables         = PENDING
controlled benchmark scenarios     = PENDING
frozen scenario gold labels        = PENDING
P003-C architecture comparison     = PENDING
```

## Interpretation firewall

SEC filings are immutable evidence anchors. Any planted impairment condition, altered threshold, synthetic exception, or benchmark gold label must be stored separately and explicitly marked as controlled/synthetic.

NAAIL must not convert a controlled research scenario into a claim that Microsoft, Alphabet, or Amazon has an undisclosed impairment, audit failure, ICFR deficiency, erroneous management estimate, or inferior audit quality.

## Canonical records

- `CURRENT_PROJECT_STATE.md`
- `PROTOTYPE_003C_SEC_EVIDENCE_SNAPSHOT.md`
- `PROTOTYPE_003C_SEC_SCOPE.md`
- `PROTOTYPE_003_EXECUTION_SPEC.md`
- `PROTOTYPE_004_PROVIDER_EXECUTION.md`
- `Prototype_003/runtime/README.md`

## Scientific invariant

**Same source evidence. Same controlled scenario. Same frozen gold labels. Same evaluator. Different execution architecture/provider.**

GitHub remains the canonical source of truth. Google Drive remains a mirror/archive.