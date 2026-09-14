# NAAIL Account-Wide Research Standard

**Owner:** Dr. Saeid Homayoun  
**ORCID:** https://orcid.org/0000-0002-2536-0446  
**GitHub:** https://github.com/Saehon  
**Effective date:** 14 September 2026

This standard defines how original research repositories in the Saehon GitHub portfolio should be presented, governed, cited, licensed, and evaluated.

## 1. Repository classes

Every repository should be classified as one of:

1. **Flagship original research system** — original NAAIL architecture or research product.
2. **Original supporting laboratory / empirical project** — original experiments, notebooks, data pipelines, or study artifacts.
3. **Private / proprietary R&D** — patent-sensitive, restricted, confidential, or pre-commercial work.
4. **Third-party / upstream / fork / dependency** — external code retained under its original license and attribution.
5. **Legacy / tutorial / sandbox** — non-flagship material that should not be presented as a core research contribution.

Third-party repositories must never be relicensed, rebranded as original work, or cited as though authored by Saeid Homayoun unless the original contribution is clearly separated.

## 2. Required identity for original research repositories

Each original research repository should contain or clearly display:

- project title;
- project year/version;
- author: **Saeid Homayoun**;
- ORCID: **0000-0002-2536-0446**;
- relationship to NAAIL OpenLab;
- research purpose and scope;
- public/private status;
- responsible-use disclaimer;
- citation metadata (`CITATION.cff`) where appropriate;
- rights/license statement;
- reproducibility expectations;
- scientific discovery protocol.

## 3. Canonical scientific protocol

All serious studies use:

**Research Question → Literature Validation → Competing Hypotheses → Co-Scientist Critique/Ranking → ERA Empirical Object → Real Data + Code → AlphaEvolve / Computational Discovery → Latent-Structure Analysis → AI-to-AI Adversarial Review → Robustness/Falsification → Replication/OOS → Science One-style Chain-of-Evidence → DAG Governance → Human Gate**

### Co-Scientist
Generate, critique, rank, debate, and improve competing hypotheses before testing.

### ERA
Convert each surviving hypothesis into a reproducible design with data, variables, estimands, identification, code, evaluation metrics, robustness tests, and replication artifacts.

### AlphaEvolve + Computational Discovery
Compare and evolve models, algorithms, constructs, prompts, estimators, measures, and specifications using frozen scientific fitness criteria. Never optimize for p-values alone.

### AlphaFold-inspired latent-structure reasoning
Search for latent factors, regimes, representations, networks, mechanisms, or hidden structures in high-dimensional data, subject to domain interpretation and external validation.

### AI-to-AI review
Use critic, defender, replicator, and evaluator roles where appropriate. Agent agreement is not scientific truth.

### Science One-style Chain-of-Evidence
Preserve traceability from question to theory, literature, data, variable construction, model, identification, result, robustness, replication, interpretation, and human decision.

### DAG governance
A claim is blocked when required theory, data, identification, provenance, code, evidence, or validation dependencies are incomplete.

### Mirendil-inspired autonomous R&D
Use controlled propose → pretest → execute → evaluate → critique → mutate → retest cycles while retaining failed runs and preserving scientific gates.

## 4. Mandatory research gates

No repository may claim a scientific discovery based only on statistical significance, model confidence, benchmark performance, or multi-agent consensus.

Where applicable, discovery claims require:

- relevant literature validation;
- contradictory-evidence search;
- source and data provenance;
- construct validation;
- leakage review;
- identification review;
- robustness analysis;
- falsification tests;
- temporal / out-of-sample validation;
- reproducible code;
- independent replication where feasible;
- AI-to-AI adversarial review;
- completed Chain-of-Evidence;
- human approval.

## 5. Citation standard

For original NAAIL projects, use machine-readable `CITATION.cff` when technically appropriate. The default author identity is:

```yaml
authors:
  - family-names: "Homayoun"
    given-names: "Saeid"
    orcid: "https://orcid.org/0000-0002-2536-0446"
```

A project citation should identify at minimum:

**Homayoun, S. (YEAR). Project Name [Research software / Research framework / Dataset / Repository as appropriate]. GitHub. Repository URL.**

Do not overwrite authorship metadata inherited from an upstream third-party repository.

## 6. Licensing standard

### Original NAAIL research
Original projects may use the **NAAIL Research and Non-Commercial License** or another explicitly selected research/non-commercial license. Commercial use must require separate written permission if that is the chosen licensing policy.

### Third-party or forked repositories
Original upstream licenses remain controlling. Do not replace them with the NAAIL license. Any original NAAIL additions must be separately identified and may carry a compatible supplemental notice only where legally appropriate.

### Non-commercial intent
For repositories released under the NAAIL research/non-commercial model, permitted use is limited to bona fide non-commercial academic research, teaching, study, evaluation, and experimentation as stated in the applicable repository license.

For-profit production use, paid SaaS, commercial deployment, consulting deliverables, resale, commercial model training, or commercial incorporation requires separate authorization where the applicable NAAIL license so provides.

## 7. Required independence statement

Original NAAIL repositories should state:

> This is an independent research project. References to Google, Google Research, Google DeepMind, OpenAI, Microsoft, Mirendil, audit firms, regulators, standard setters, or other organizations describe public research inspiration, interoperability, benchmark context, model providers, or professional context only and do not imply sponsorship, employment, endorsement, partnership, certification, or affiliation unless explicitly documented.

## 8. Reproducibility target

```text
project/
├── README.md
├── CITATION.cff
├── LICENSE / rights notice
├── RESEARCH_PROTOCOL.md
├── data_manifest/
├── schemas/
├── src/
├── tests/
├── notebooks/
├── configs/
├── results/
└── run_manifest.json
```

## 9. Scientific invariants

```text
agent_consensus_is_truth = false
model_confidence_is_truth = false
optimize_for_p_value = false
failed_runs_are_deleted = false
human_gate_required = true
discovery_claim_allowed = false  # default
```

## 10. Portfolio principle

**One professional identity. One public research hub. Clear flagship systems. Clear supporting laboratories. Clear third-party boundaries. Consistent citation. Consistent scientific governance. No unsupported affiliation claims.**
