# P0.2 Governance, Human Approval, and Data Rules

Status: FROZEN v1.0  
Gate: P0.2  
Date: 2026-10-04  
Scope: NAAIL Trust Finance / Multi-LLM Financial Disagreement

## 1. Purpose and authority

This constitution defines who may act, which data may be used or released, and where human approval is mandatory. It governs the research branch, Google Drive archive, model experiments, evidence graph, empirical outputs, and manuscript claims.

The human owner is the final scientific and governance authority. Automated operators may execute bounded work under the canonical plan but may not self-approve protected decisions.

## 2. Roles and decision rights

| Role | Permitted actions | Prohibited without human approval |
|---|---|---|
| Human owner / principal investigator | Approve protocol freezes and amendments; authorize restricted-data use; open sealed test; approve public release, manuscript claims, submission, and merge | None within lawful and contractual limits |
| Primary project operator | Work on the authorized branch; use development data; prepare code, schemas, documentation and evidence; run prespecified checks; maintain ledger and repair queue | Merge protected `main`; publish restricted material; open or tune on sealed test; approve its own scientific claims; fabricate model or test results |
| Independent reviewer | Review evidence, code, outputs, deviations and claims; request correction or falsification | Rewrite provenance; convert unresolved findings to PASS; merge or release without authority |
| Human domain reviewer | Review high-disagreement, high-materiality and ambiguous cases; record accept/modify/reject/escalate decision | Silent approval; undocumented override; alteration of raw model output |

One primary writer may own a branch/scope at a time. An active, unexpired writer lock requires other operators to perform a mutation NO-OP. No concurrent operator may overwrite edits. The project uses one active branch/scope and one PR per scope.

## 3. Mandatory human approval gates

Human approval is required before any of the following:

1. merging into protected `main`;
2. changing a frozen research question, estimand, hypothesis family, construct objective, partition rule, or primary specification;
3. accessing restricted/licensed or personal/sensitive data when prior authorization is absent;
4. sending non-public evidence to an external model provider;
5. opening the sealed test partition or viewing sealed outcomes;
6. reopening a dependency-critical quarantine without genuinely new actionable evidence;
7. making causal, novelty, performance, validation, or economic-value claims for external use;
8. releasing a public dataset, model-output corpus, replication package, manuscript, press material, or product claim;
9. submitting the manuscript to a journal; and
10. accepting a high-materiality financial judgment as decision-ready.

Approval must identify the approver, timestamp, object/version, decision, conditions, and supporting evidence. Absence of a recorded decision is not approval.

## 4. Data classification and permitted locations

| Class | Examples | Public GitHub | Controlled Drive | External model/API |
|---|---|---|---|---|
| D0 Public | SEC filings, public XBRL, public papers, public replication code/data under compatible terms | Allowed with source, date, license/terms where applicable, and provenance | Allowed | Allowed subject to provider terms and logging |
| D1 Synthetic / pseudo-data | Generated stand-ins that do not reproduce confidential records | Allowed when clearly labelled synthetic and generation method is documented | Allowed | Allowed |
| D2 Internal / unpublished | Drafts, preliminary results, reviewer notes, unpublished model outputs | Only deliberately approved, non-sensitive subsets | Allowed with access control | Only with authorization and provider-use review |
| D3 Restricted / licensed | CRSP/Compustat or other non-redistributable data; licensed vendor datasets | Raw or reconstructable records prohibited; publish only schemas, hashes, code, acquisition instructions, and lawful pseudo-data | Allowed only under license and access restrictions | Prohibited unless license and provider terms explicitly allow it and human approval is recorded |
| D4 Personal / sensitive | Direct identifiers, confidential company records, credentials, secrets, regulated or special-category data | Prohibited | Prohibited until lawful basis, minimization, security, retention, and ethics/privacy review are documented | Prohibited absent explicit lawful authorization and approved safeguards |

Raw credentials, API keys, access tokens, private keys, secrets, and authentication artifacts are never research data and must never be committed, uploaded into evidence files, or included in prompts.

## 5. Public-repository rule

The public repository may contain:

- source code and tests that contain no secrets or restricted data;
- public-source citations and acquisition instructions;
- schemas, data dictionaries, hashes and provenance manifests;
- synthetic or pseudo-data that are labelled and disclosure-checked;
- aggregate results cleared for release; and
- documentation of limitations, failures and repair actions.

It must not contain raw restricted/licensed records, confidential evidence, personal data, reconstructable proprietary extracts, credentials, embargoed results, or raw prompts/outputs containing those materials.

## 6. Evidence and model-governance rules

Every evidentiary observation must be traceable, where applicable, through source, access date, document/filing date, firm/entity, period, extraction method, transformation version and content hash.

Every model execution that counts as evidence must record provider, exact model/version if exposed, execution date/time, prompt/protocol version, parameter settings, input-evidence identifiers, raw output, parser/version, errors/retries and human-review state. Unexecuted or unavailable model outputs must never be represented as observations.

Model output inherits the highest classification of its input and may be more sensitive if it exposes protected attributes or memorized content. Restricted inputs may not be sent to external providers without explicit authorization and a documented terms/privacy assessment.

## 7. Privacy, ethics, licensing, and retention

- Prefer public corporate evidence and data minimized to the research purpose.
- Do not infer that public availability alone resolves copyright, licensing, privacy, ethics, or redistribution duties.
- Before ingesting personal/sensitive or non-public human-related data, record the applicable ethics/IRB and privacy determination; until then, quarantine the data and dependent analysis.
- Respect source licenses, database contracts, robots/rate limits, attribution duties and journal replication rules.
- Retain immutable raw evidence separately from derived data; corrections create a new version and preserve lineage.
- Remove data when authorization expires or a lawful retention rule requires removal, while retaining a non-sensitive audit record where permitted.

## 8. Scientific and release controls

- Development work, construct search and AlphaEvolve-inspired optimization are confined to development data.
- Validation diagnoses generalization but may not drive iterative selection unless a governed amendment creates a new untouched validation set.
- Sealed-test outcomes remain inaccessible until the preregistered opening decision.
- Microsoft FY2026 remains a proof of concept until prespecified empirical validation is completed.
- Engineering success, documentation, elapsed time, commits and CI do not establish scientific validity.
- `PASS` requires evidence for the specific gate; `CLOSED` is never equivalent to `PASS`.
- Two persistent failures trigger a stable blocker record and the OPEN REPAIR QUEUE; unresolved dependency-critical outputs remain quarantined.

## 9. P0.2 acceptance test

P0.2 may be marked PASS only if the frozen record includes: role authority; mandatory human decisions; public/private classification; location and external-provider rules; secrets prohibition; evidence/model provenance; privacy/ethics/licensing controls; writer-lock/concurrency rule; sealed-test protection; and release/merge restrictions.

All elements are present in v1.0. This PASS freezes governance design only; it does not validate data, models, empirical results, or manuscript claims.

## 10. Change control

Any material amendment requires a new version, rationale, affected gates/outputs, human approval, effective date, and an assessment of whether earlier outputs must be rerun or quarantined. Historical versions remain auditable.
