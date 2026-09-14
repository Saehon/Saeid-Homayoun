# NAAIL OpenLab — Professional Product Repository Standard

This standard defines the minimum GitHub structure for NAAIL research products, scientific software, professional-intelligence prototypes, and agentic AI systems.

The goal is to make every repository understandable to a researcher, software engineer, auditor, reviewer, collaborator, or employer within a few minutes while preserving scientific provenance, IP boundaries, and human accountability.

## 1. Mandatory top-level files

Every NAAIL product repository should contain, where applicable:

```text
README.md
CITATION.cff
LICENSE or explicit RIGHTS / LICENSING file
CONTRIBUTING.md
SECURITY.md
ROADMAP.md
CHANGELOG.md                 # for actively versioned products
REPRODUCIBILITY.md           # for empirical/scientific products
DATA_SOURCES.md or DATA.md   # when data are used
THIRD_PARTY_NOTICES.md       # when external software/models/data matter
```

## 2. Professional README contract

The README should answer these questions in this order:

1. **What is the product?**
2. **Who owns / maintains it?**
3. **What is its maturity status?**
4. **What problem does it solve or research?**
5. **What is the architecture?**
6. **How can a researcher or developer run or inspect it?**
7. **How is it evaluated?**
8. **What evidence / data / standards does it use?**
9. **What are the limitations and human-review gates?**
10. **How should it be cited?**
11. **What license / IP / third-party restrictions apply?**
12. **What organizations are referenced only as inspirations, providers, standards bodies, or comparison targets?**

## 3. Recommended repository structure

```text
product-name/
├── README.md
├── CITATION.cff
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
├── ROADMAP.md
├── CHANGELOG.md
├── pyproject.toml / requirements.txt
├── src/
├── tests/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── RESEARCH_PROTOCOL.md
│   ├── EVALUATION.md
│   └── GOVERNANCE.md
├── examples/ or notebooks/
├── data_manifest/           # not necessarily raw data
├── eval/
├── configs/
├── .github/
│   ├── workflows/
│   └── ISSUE_TEMPLATE/
└── run_manifest.json        # where relevant
```

## 4. Scientific and professional evidence rules

NAAIL products should preserve these invariants:

```text
model_output_is_evidence = false
agent_consensus_is_truth = false
optimize_for_p_value = false
human_gate_required = true
failed_runs_are_evidence = true
unsupported_compliance_claims_allowed = false
third_party_affiliation_assumed = false
```

Material claims should be linked to data, code, evaluation, provenance, assumptions, robustness tests, and reviewer status.

## 5. Product maturity labels

Use one of the following labels clearly in the README:

- **Concept** — architecture or idea under design;
- **Research Prototype** — executable or partially executable research artifact;
- **Benchmark Prototype** — supports reproducible evaluation on frozen tasks;
- **Validated Research Prototype** — independently replicated / reviewed within a defined research scope;
- **Pre-Production** — engineering and governance work toward deployment, but not yet approved for real professional use;
- **Production** — only after documented security, legal, regulatory, model-risk, professional, and organizational approval.

Do not describe a project as certified, compliant, validated, production-ready, or regulator-approved without evidence that supports that exact claim.

## 6. Third-party and fork transparency

Forks and copied/reference repositories must be clearly labelled as such.

A NAAIL portfolio page should distinguish:

- **Original NAAIL product / research software**;
- **Private NAAIL R&D**;
- **Fork / upstream reference**;
- **External benchmark / dependency**;
- **Teaching or experimentation repository**.

Do not present an upstream project, model, framework, dataset, or trademark as a NAAIL invention.

## 7. Licensing and IP

- Existing MIT, Apache, BSD, or other permissive grants should be represented accurately.
- A public permissive license cannot later be treated as if it had always prohibited commercial reuse.
- Patent-sensitive or proprietary implementations should be separated before public release.
- Private-repository access controls do not replace an explicit license or collaboration agreement.
- Third-party standards, datasets, software, papers, trademarks, and models retain their original rights.
- Patentability, freedom to operate, trademark ownership, or legal compliance should not be claimed without appropriate professional review.

## 8. Citation and research identity

Every original research product should include `CITATION.cff` with:

- product title;
- author/maintainer;
- ORCID where appropriate;
- release/version or year;
- repository URL;
- license when unambiguous;
- keywords relevant to the product.

## 9. Quality gates before a public release

A professional public release should pass:

**Repository hygiene → provenance check → third-party rights check → reproducibility check → test/evaluation check → security review → claim review → citation review → IP/publication review → human approval.**

## 10. Current NAAIL application

This standard should be applied to:

- ECONOVA-S™ / NAAIL OpenLab hub;
- AAA — Audit & Accounting AI Laboratory;
- IFRS-AI Inspector;
- Multi-Agent Accounting AI Framework;
- POMELO™ / POMELO VERA™ private R&D;
- PCAOB Inspection Agent private R&D;
- future KIWI™, ICFR/time-series, sustainability, forensic, and data-economy products.

Reference forks such as TimesFM should remain clearly attributed to their upstream owners and used as dependencies, benchmarks, or integration sandboxes rather than represented as original NAAIL products.
