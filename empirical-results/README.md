# 📊 Empirical Results Hub

**Saeid Homayoun — Accounting & Auditing Scholar | AI-Integrated Accounting, Auditing & Assurance Research**

This folder is the public evidence layer for executed empirical results, reproducibility checkpoints, validation tests, and research-status boundaries. It separates **verified empirical evidence** from the main academic profile and from forward-looking research architecture.

> **Evidence rule:** executed results are reported as executed; proof-of-mechanism evidence is not presented as population causality; blocked confirmatory tests remain explicitly blocked.

---

## 1. KIWI™ CAM/KAM — Dynamic Audit-Attention Reallocation

### Research question

When the relative importance of accounting risks changes within a company, does the auditor reallocate publicly disclosed professional attention across Critical Audit Matter (CAM) topics?

### Core mechanism

```text
Pre-disclosure accounting risk
        ↓
Relative topic risk
        ↓
Professional audit-attention allocation
        ↓
CAM ENTRY / PERSISTENCE / EXIT
```

The research treats the CAM report as a **capacity-constrained portfolio of professional audit attention**.

---

## 2. Main Executed Result — AAR Corp

The strongest currently executed proof-of-mechanism result comes from **AAR Corp, 2020–2024**.

| Year | CAM portfolio |
|---|---|
| 2020 | Inventory + Revenue |
| 2021 | Inventory + Revenue |
| 2022 | Inventory + Revenue |
| 2023 | Inventory + Revenue |
| 2024 | Inventory + Business Combinations / Acquired Intangibles |

### 2024 transition

| Outcome | Result |
|---|---|
| Revenue | **EXIT** |
| Business Combinations / Acquired Intangibles | **ENTRY** |
| Inventory | **PERSIST** |
| CAM count | **2 → 2** |
| CAM count change | **0** |
| CAM Attention Reallocation Score (CARS) | **0.667** |

### Main interpretation

**66.7% of the CAM portfolio composition changes even though the total number of CAMs does not change.**

This demonstrates why CAM **composition and reallocation** can contain information that CAM counts alone miss.

---

## 3. Independent Pre-CAM Risk Evidence

For AAR Corp, an independently measured acquisition shock of approximately **39.6% of prior-year assets** precedes the entry of the Business Combinations / Acquired Intangibles CAM.

At the same time:

- Inventory risk increases and the Inventory CAM persists.
- Revenue exits even though pre-CAM revenue-risk signals remain material.

This rejects the naive rule:

```text
Absolute topic risk falls → CAM exits
```

and motivates the stronger relative-risk mechanism:

```text
REL_RISK(i,j,t) =
Topic Risk(i,j,t)
− Mean Risk of competing topics within the same firm-year
```

**Scientific boundary:** this is proof-of-mechanism evidence, not population-level causal evidence.

---

## 4. Significant AAR Construct-Validity Result

The AAR falsification design compares the correct audit response with a same-year swapped response.

The correct risk–audit-response alignment wins in **all five independent years**.

| Test | Result |
|---|---:|
| Positive independent years | **5 / 5** |
| Independent unit | **Year** |
| Exact one-sided sign-test p-value | **0.03125** |
| Average reported correct SQI | **≈ 78.6** |
| Average reported wrong-response SQI | **≈ 35.1** |
| Average reported SQI after removing audit response | **≈ 7.9** |

This supports construct validity: the structural measure detects risk–procedure mismatch rather than merely professional wording or document length.

### AAR structural measures

- **RPA** — Risk–Procedure Alignment
- **EDS** — Evidence Depth Score
- **SIS** — Structural Integrity Score
- **SQI** — CAM Structural Quality Index
- **CIIS** — CAM Incremental Information Score
- **CARS** — CAM Attention Reallocation Score

**Important:** SQI measures CAM communication/structural quality. It is **not an audit-quality score**.

---

## 5. Current 50-Firm Measurement Architecture

The current SEC-verified measurement architecture contains:

| Measure | Current status |
|---|---:|
| SEC-verified company-years | **87** |
| Frozen candidate topics per company-year | **7** |
| Company-year-topic rows | **609** |
| CAM-present topic-years | **111** |
| Valid CAM persistence events | **49** |
| Valid CAM entry events | **5** |
| Valid CAM exit events | **7** |
| Exact auditor-report-date coverage | **12 / 87 company-years** |
| Topic-years with ≥2 frozen MAIN risk features + temporal PASS | **11** |
| Confirmatory H1/H2 | **BLOCKED pending final measurement gates** |

### Frozen seven-topic universe

1. Revenue / contract estimates
2. Inventory
3. Goodwill / business combinations / intangibles
4. Pension / postretirement
5. Income tax / uncertain tax positions
6. Contingencies / litigation
7. Long-lived assets / impairment

The topic universe is frozen before confirmatory H1/H2 estimation.

---

## 6. Frozen Risk Architecture

For each firm *i*, topic *j*, and year *t*:

```text
R_TOPIC(i,j,t)
= mean(valid standardized MAIN risk features)

REL_RISK(i,j,t)
= R_TOPIC(i,j,t)
− mean R_TOPIC across eligible competing topics within the same firm-year

RISK_RANK(i,j,t)
= descending within-firm rank of R_TOPIC
```

### Integrity rules

- Risk inputs must be observable before the auditor-report date.
- CAM title, description, response, and same-report CAM narrative are excluded from risk construction.
- Missing XBRL values remain missing.
- Missing values are never automatically coded as zero.
- A publication-grade topic score requires at least two independent MAIN feature channels.
- Confirmatory model selection cannot be tuned using final outcomes.

---

## 7. Research Abstract

### *Pre-Disclosure Accounting Risk and the Reallocation of Critical Audit Matters*

Critical Audit Matters (CAMs) reveal a subset of the professional attention auditors allocate across competing accounting risks. We develop a capacity-constrained attention framework in which changes in relative accounting risk can induce auditors to reallocate CAM attention across topics without changing the total number of reported CAMs. Our design combines a fixed seven-topic choice set with independently measured pre-disclosure SEC/XBRL risk signals, explicit CAM entry–persistence–exit transitions, and outcome-blind falsification. CAM text is excluded from risk construction, and all risk evidence must precede the auditor-report date.

AAR Corp provides the primary proof of mechanism. Between 2023 and 2024, total CAM count remains unchanged at two, yet Revenue exits, Business Combinations/Acquired Intangibles enters, and Inventory persists, producing a CAM Attention Reallocation Score of 0.667. The entering acquisition-related CAM is preceded by an independently measured acquisition shock of approximately 39.6% of prior-year assets, whereas Revenue exits despite remaining material in absolute risk terms. In construct-validity tests, the correct risk–audit-response alignment dominates a same-year swapped response in all five independent years (exact one-sided p = 0.03125). The broader measurement architecture contains 87 SEC-verified company-years and 609 company-year-topic observations, including 111 CAM-present observations and 61 valid entry, persistence, or exit transitions.

The evidence supports a dynamic view of audit reporting in which professional attention is allocated according to the relative salience of competing risks rather than CAM quantity alone. The study contributes a temporally disciplined and falsifiable framework for examining professional attention allocation and provides a reproducible foundation for AI-assisted accounting and auditing research.

---

## 8. FT50 / AJG Research Connection

The research is designed to connect to substantive accounting and management-science streams rather than treating AI itself as the theoretical contribution.

### Management Science

Methodological relevance:
- machine-learning and LLM measurement;
- construct validation;
- reproducibility;
- decision-allocation systems.

Key methodological anchor:

de Kok, T. (2025). *ChatGPT for Textual Analysis? How to Use Generative LLMs in Accounting Research*. **Management Science**, 71(9), 7888–7906.  
https://doi.org/10.1287/mnsc.2023.03253

### The Accounting Review

Institutional and audit-attention relevance:

Burke, J. J., Hoitash, R., Hoitash, U., & Xiao, X. (2023). *The Disclosure and Consequences of U.S. Critical Audit Matters*. **The Accounting Review**.  
https://doi.org/10.2308/TAR-2021-0013

Chan & Liu (2023). *The Effects of Critical Audit Matter Disclosure on Audit Effort, Investor Scrutiny, and Investment Efficiency*. **The Accounting Review**.

### Contemporary Accounting Research

Relevant streams:
- accounting textual analysis;
- financial NLP;
- construct measurement;
- CAM/KAM semantic analysis;
- validation of AI-based measures.

### Positioning principle

```text
Accounting/Auditing Theory
        ↓
Independent Financial Evidence
        ↓
AI-Assisted Measurement
        ↓
Falsification / Reproducibility
        ↓
Human Scientific Judgment
```

AI is the **measurement, discovery, falsification, and reproducibility infrastructure**.  
The theoretical contribution is the **allocation of scarce professional audit attention across competing accounting risks**.

---

## 9. Earnings-Information Validation Layer

The separate CAM–earnings bridge currently verifies AAR Corp across **five company-years, 2020–2024**, with **19 earnings-announcement events**.

This layer is treated as downstream economic validation:

```text
Pre-CAM risk
→ CAM portfolio
→ later earnings-information environment
```

It is **not** currently used to infer earnings management, and later earnings information cannot enter the construction of pre-CAM risk.

---

## 10. Reproducibility

Public AAR unit test:

[KIWI™ AAR Corp CAM Unit Test](../NAAIL-OpenLab/demos/aar-cam-unit-test/README.md)

The public runner reproduces:

- AAR 2020–2024 frozen CAM structure;
- 2024 Revenue exit;
- acquisition-related CAM entry;
- Inventory persistence;
- zero CAM-count change;
- CARS = 0.667;
- exact year-level sign test;
- weight-robustness checks;
- explicit non-claims and scientific boundaries.

---

## 11. Open Research Platforms

### GitHub

Code, architecture, provenance, tests, and reproducible research pipelines:  
https://github.com/Saehon/Saeid-Homayoun

### Hugging Face

Datasets, models, model cards, and public AI research artifacts:  
https://huggingface.co/SADHON

CAM/KAM AuditBERT Public Demo:  
https://huggingface.co/datasets/SADHON/cam-kam-auditbert-public-demo

### Kaggle

Benchmark datasets and executable notebooks:  
https://www.kaggle.com/sadhon

CAM/KAM AuditBERT Public Demo:  
https://www.kaggle.com/datasets/sadhon/cam-kam-auditbert-public-demo

SEC 10-Company Accounting Panel:  
https://www.kaggle.com/datasets/sadhon/sec-10-company-accounting-panel

---

## 12. Citation

**APA**

> Homayoun, S. (2026). *Pre-Disclosure Accounting Risk and the Reallocation of Critical Audit Matters: A Prospective KIWI Design with an Earnings-Information Validation Layer*. Working paper, University of Gävle.

**Repository**

> Homayoun, S. (2026). *KIWI™ CAM/KAM Research Program: AI-integrated accounting and auditing research, datasets, code, and reproducible benchmarks*. GitHub. https://github.com/Saehon/Saeid-Homayoun

```bibtex
@unpublished{homayoun2026kiwi,
  author      = {Homayoun, Saeid},
  title       = {Pre-Disclosure Accounting Risk and the Reallocation of Critical Audit Matters: A Prospective KIWI Design with an Earnings-Information Validation Layer},
  year        = {2026},
  institution = {University of Gävle},
  note        = {Working paper},
  url         = {https://github.com/Saehon/Saeid-Homayoun}
}
```

---

## 13. Current Scientific Status

| Component | Status |
|---|---|
| Research architecture | **PASS** |
| Public SEC identifier architecture | **PASS** |
| AAR lifecycle | **PASS** |
| AAR falsification architecture | **PASS** |
| Seven-topic universe | **PASS / FROZEN** |
| 50-firm choice set | **PASS** |
| Independent pre-CAM risk panel | **PARTIAL** |
| R normalization | **BLOCKED pending sufficient coverage** |
| Final falsification gate | **BLOCKED** |
| Confirmatory H1/H2 | **BLOCKED** |
| Population causal claim | **NOT CLAIMED** |

The project follows a simple rule:

> **Evidence before claims. Verification before estimation. Falsification before confirmation.**
