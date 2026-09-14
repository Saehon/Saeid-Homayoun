# NAAIL OpenLab — IP & Patent-Readiness Protocol

**Owner / researcher:** Dr. Saeid Homayoun  
**ORCID:** https://orcid.org/0000-0002-2536-0446  
**Version:** 2026.1

> This document is an internal research-governance notice, not legal advice and not a patent filing.

## Critical rule: public GitHub disclosure is not patent protection

A GitHub commit can help establish a dated technical record and provenance, but it does **not** create patent rights, reserve patentability, or substitute for filing a patent application. Public disclosure can affect novelty/patentability depending on jurisdiction and timing.

Therefore, potentially patentable implementation details should be kept **private before publication** and reviewed with a qualified patent professional before being pushed to a public repository.

## NAAIL disclosure gate

Before releasing a new architecture, algorithm, evaluation method, agent workflow, scoring system, data structure, digital-twin mechanism, or other potentially protectable invention:

1. Record inventor(s), date, problem, technical contribution, alternatives, experiments, diagrams, and evidence in a private invention record.
2. Search prior art and relevant scientific/patent literature.
3. Separate third-party/open-source components from original inventive contributions.
4. Mark the artifact **PRIVATE — PATENT REVIEW PENDING**.
5. Obtain patent/legal review where protection is contemplated.
6. Decide explicitly: patent filing first, trade secret/private R&D, defensive publication, or public research release.
7. Only after that decision should public disclosure occur.

## Public repository notice

For original NAAIL research repositories, the following statement may be used where compatible with the governing license:

> **IP / Patent Notice:** This repository may describe research concepts, architectures, methods, or prototypes for which intellectual-property protection may be considered. Publication on GitHub does not constitute a patent filing and does not guarantee patentability. No patent, trademark, commercial, or endorsement rights are granted except as expressly stated in the applicable license. Patent-sensitive implementation details may be withheld from the public repository. Third-party components remain governed by their original rights and licenses.

## What should remain private pending review

- novel algorithmic implementation details;
- unpublished scoring/evaluation mechanisms;
- private benchmark/gold datasets;
- proprietary agent orchestration or verification mechanisms;
- patent claim drafts and invention analyses;
- confidential collaborator/client information;
- credentials, secrets, private API configuration;
- restricted standards or licensed data;
- unpublished experimental results when disclosure timing matters.

## Evidence record

For each potentially protectable project maintain a private record containing:

```text
invention_id
project_name
inventor_names
first_conception_date
technical_problem
technical_solution
novel_elements
prior_art_search
alternative_implementations
experiments_and_results
source_commit_hashes
figures_and_architecture
third_party_dependencies
public_disclosure_dates
patent_review_status
release_decision
human_approval
```

## Research integrity

Patent strategy must never weaken scientific integrity. NAAIL research claims still require literature validation, reproducibility, falsification, adversarial review, provenance, and human approval. Patentability and scientific validity are separate questions.
