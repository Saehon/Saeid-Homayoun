# Pilot 001 — Microsoft SEC/XBRL → Delta/MLflow → Multi-Agent Falsification

Status: reproducible pilot scaffold. Designed to run locally, in GitHub Actions, or in Databricks once a Databricks workspace is connected.

## Research question
Can an evidence-grounded AI workflow reproduce and verify selected Microsoft financial-statement facts from SEC/XBRL while preserving evidence lineage and exposing model disagreement before human approval?

## Company
Microsoft Corporation (CIK 0000789019).

## Pipeline
SEC CompanyFacts / filing evidence → deterministic extraction → Delta-compatible research table → accounting assertions → provider-neutral agent inputs → OpenAI / Anthropic / Gemini / Microsoft adapter slots → MLflow experiment/traces → deterministic verifier → Reviewer/Falsification → human approval.

## Evidence table
One row per fact: cik, entity, accession/filing, fiscal period, form, taxonomy, concept, unit, value, filing date, source, extraction timestamp, code commit.

Initial concepts: Assets; Liabilities; StockholdersEquity; Revenues; NetIncomeLoss; CashAndCashEquivalentsAtCarryingValue; NetCashProvidedByUsedInOperatingActivities.

Never hard-code accounting values. Pull them from a pinned SEC evidence snapshot.

## Deterministic checks
1. duplicate facts; 2. entity/time/form consistency; 3. unit consistency; 4. Assets ≈ Liabilities + Equity where applicable; 5. evidence completeness; 6. missing/contradictory fact flags.

## Accounting assertion tasks
Accuracy/Valuation; Completeness; Classification; Period/Cutoff; Consistency; Evidence support. Every conclusion must return evidence IDs.

## Provider-neutral output
Fields: claim, concept, period, value, unit, assertion, evidence_ids, confidence, limitations. Provider adapters stay separate from domain logic and receive identical evidence.

## MLflow
Experiment name: microsoft-sec-xbrl-pilot-001.
Log SEC snapshot/version, Git commit, provider/model/version, prompt hash, evidence hash, configuration, baseline, output, metrics, evidence coverage, citation correctness, unsupported-claim rate, latency, cost and failure taxonomy.

## Reviewer/Falsification gate
Provider identity is blinded. Fail claims with missing/unsupported evidence, number/unit/period/entity mismatch, unexplained deterministic violations, unsupported standards claims, or unjustified confidence under contradictory evidence.

## Human approval
Human sees source fact, deterministic result, anonymized agent result, falsification result and disagreement flags. Status: APPROVE / REJECT / NEEDS_MORE_EVIDENCE.

## Databricks/Delta layout
bronze_sec_companyfacts → silver_microsoft_xbrl_facts → gold_microsoft_assertion_benchmark → gold_agent_results → gold_falsification_results → gold_human_validation.

## Scientific controls
Pin evidence before model execution; immutable original facts; identical evidence/tasks; blind provider identity; separate deterministic/retrieval/reasoning errors; report negative results; preserve prompts/config/model versions.

## FT50/ABS4 extension
Published theory/prior evidence → reproducible SEC/XBRL baseline → controlled AI intervention → accounting assertions → cross-provider comparison → falsification → human validation → theory-relevant failure mechanisms.

Created: 2026-09-25.
