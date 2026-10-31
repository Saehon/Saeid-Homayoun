# Evidence-Grounding Review and Adjudication Protocol

**Status:** implemented offline scientific *calibration scaffold* using **simulated reviewers** and five hand-written synthetic cases. No third-party assessor, GPT/Claude/Gemini inference, licensed document testing or professional certification is claimed.

## Research purpose

Automated numerical correctness and citation-ID matching cannot establish whether a purported audit or finance answer is **actually supported by its cited evidence**. A transparent, separately auditable human-judgment protocol is needed to assess factual entailment, unsupported inferences and reviewer disagreement.

This protocol is aligned with OpenAI's [evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices), Anthropic's [testing and grading recommendations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests), and Google's [rubric-based and computed evaluation measures](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview). These sources explain evaluation methods; they neither authorize use of proprietary data nor endorse this laboratory.

## Three-label evidence-support rubric

| Label | Operational rule | Examples of inappropriate inferences |
|---|---|---|
| `supported` | The evidence, in its **actual document**, directly entails the material answer, including units, fiscal period, financial-statement entity and scope | A valid evidence ID alone is never enough |
| `contradicted` | The answer conflicts with relevant evidence or asserts an unsupported contradictory number | Arithmetic errors, opposite audit conclusion, stale period |
| `insufficient_evidence` | Evidence cannot establish the conclusion or the question requires further professional judgment | Missing note, disputed IFRS judgment, missing assurance report |

A pair of annotators independently applies the frozen rubric; disputed cases require a separate adjudicator and a reason. Pairwise raw agreement and descriptive Cohen's kappa highlight potential rubric disagreement; they **do not** prove answer correctness or the annotators' independence.

## Reproduce the simulation

From the root of the repository, with Python 3.11+ and no external dependencies:

```bash
python -m research.ai_evidence_evaluation.annotation_audit \
  --out reports/simulated_annotation_audit.json
python -m unittest discover -s research/ai_evidence_evaluation/tests -v
```

Five synthetic reference cases, **ten simulated reviewer records** and one synthetic disagreement-resolution record are deliberately constructed to challenge schema validation and calculation. The report includes SHA-256 digests, label counts, a complete confusion matrix, raw agreement, kappa and adjudication coverage.

**Never describe these synthetic simulated reviewer IDs as actual blind or independent human annotators.** The report sets `actual_independent_human_review_verified=false`, `model_evaluation_completed=false` and `source_document_entailment_independently_verified=false`.

## Empirical research requirements before publishing results

1. Obtain lawful, appropriately licensed and temporally valid annual reports, KAM/CAM, audit evidence, ESG material or SEC filings.
2. Define data units, issuer, jurisdiction, industry, year, sampling frame, approved rubric version, answer-comparison policy and evidence rights.
3. Separate model prediction production from a **frozen blind annotation set**; retain conflict disclosures and independent proof of reviewers and their qualifications.
4. Use source documents, not merely evidence identifiers, for the human evidence-entailment decision. Record citation text spans and interpretation ambiguities.
5. Reconcile ambiguous accounting cases through an independent adjudicator; preserve raw labels and disagreements, not just a final mean score.
6. Verify actual model/provider/version/configuration and billable cost through approved run records; do not infer vendor execution from an arbitrary model-name string.
7. Study correctness, groundedness, abstention, heterogeneity, statistically defensible uncertainty, biases and the effects of human oversight. Cite all source materials lawfully.

## Threat model

- **Annotation leakage:** gold labels exposed before model prediction or to adjudicators without a blind protocol.
- **Evidence spoofing:** fabricated citation IDs or source documents unrelated to the claimed date/entity.
- **Self-approval:** automatically calling the same analyst an independent evaluator.
- **Model identity spoofing:** treating hand-authored outputs as provider-backed GPT, Claude or Gemini observations.
- **Reporting inflation:** presenting a five-case demonstration and synthetic kappa as an empirical research publication.

## Relationship to the other research tools

- [Financial answer/evidence scorer](ai_evidence_evaluation/evaluate.py): numeric exactness and cited-ID presence.
- [Paired synthetic comparison](ai_evidence_evaluation/compare_runs.py): same reference cases, synthetic model fixture outputs.
- [Run provenance validator](ai_evidence_evaluation/validate_run.py): validates declared metadata and local digests but cannot independently attest actual providers.
- [Annotation-audit implementation](ai_evidence_evaluation/annotation_audit.py): input consistency and a synthetic double-rating/adjudication workflow.

These tools are **research software components**, not audit opinions, an externally published benchmark or a substitute for professional expertise.
