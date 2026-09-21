# FRANKENSTEIN Architecture

FRANKENSTEIN is a specialist programme inside NAAIL OpenLab. It does not alter the frozen two-core constitution.

```mermaid
flowchart LR
    A[ERP / GL / Transactions / ESG Evidence] --> B[Deterministic Audit Engine]
    B --> C[Evidence Ledger]
    X[IFRS / AuditData / BERT / TimesFM adapters] --> C
    S[GAN / Synthetic Scenarios] --> R[Adversarial Challenge]
    C --> D1[Finance Controls]
    C --> D2[Internal Audit]
    C --> D3[IFRS Reporting]
    C --> D4[ICFR]
    C --> D5[Forensic]
    C --> D6[ESG Assurance]
    C --> D7[Cost & AI FinOps]
    C --> D8[Operations Risk]
    C --> D9[AI & Data Governance]
    D1 --> L[FRANKENSTEIN Leader]
    D2 --> L
    D3 --> L
    D4 --> L
    D5 --> L
    D6 --> L
    D7 --> L
    D8 --> L
    D9 --> L
    R --> L
    L --> P[Evidence Passport / Report]
    P --> H{Human Approval Gate}
```

## Invariants

1. Deterministic tests precede generative interpretation where feasible.
2. Evidence and inference are stored and described separately.
3. Specialist consensus is not professional authority.
4. Missing evidence must be surfaced, not invented.
5. Model providers and agent SDKs are replaceable; the professional architecture must not depend on one vendor.
6. Cost optimization cannot override required evidence quality, reproducibility or professional judgment.
7. Consequential conclusions require a Human Approval Gate.


## Replaceable provider profiles

The public FRANKENSTEIN programme may contain multiple technology profiles under the same professional governance. Current examples include the Claude-enabled base implementation and the [OpenAI Finance & Operations Audit profile](openai_finops/README.md). Provider-specific code belongs to the Replaceable Technology Core; professional evidence and Human Gate requirements do not change with provider.
