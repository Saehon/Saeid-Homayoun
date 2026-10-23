# Pseudocode and Systems Thinking — Saehon/Saeid-Homayoun

## Method adopted for future work

Version 1.0.0 | Adopted 23 October 2026 | Workflow owner: Dr Saeid Homayoun.

This is a reusable design and evidence standard. A documented algorithm is a design artifact; it is not proof that code, an experiment, a model or an external deployment has run. Apply the method to each selected project and work packet. Preserve upstream authorship, existing interfaces, data permissions, project boundaries and any active project pause.

## 1. Frame the whole system

State the decision or research question, stakeholder, unit of analysis, jurisdiction, time horizon and success criterion. Identify what is inside the system and outside it. Map actors, data sources, transformations, stores, decisions and outcomes. Name each dependency and interface. For research, distinguish the proposed causal mechanism from an operational data flow; an arrow in a diagram is not identification.

Identify at least one relevant stock (an accumulated quantity or backlog), flow (a rate of addition/removal), feedback loop, delay, bottleneck and unintended consequence. Specify a measurable signal for each claimed feedback loop. Avoid forcing irrelevant numerical stocks into purely documentary work; record why a concept is not applicable. Examine a rival explanation and the system-wide consequence of optimizing a local metric.

## 2. Write numbered pseudocode before material implementation

For a new or materially changed workflow, first complete the project contract. For a trivial editorial change, update only the affected step or state why the algorithm is unaffected.

```text
ALGORITHM ProjectWorkPacket(project, authorized_inputs, current_version)
P01 READ canonical scope, previous decisions, permissions and pause state
    IF project is paused: retain pause; do only explicitly authorized metadata work
P02 DEFINE boundary, actors, unit, dates, objective and acceptance criterion
P03 MAP inputs, outputs, dependencies, feedback, delays and failure paths
P04 VERIFY source identity, rights, key grain, time cutoff and required coverage
    IF a required dependency is missing: RETURN BLOCKED with the exact evidence gap
P05 REGISTER primary design, baselines, validation split and search budget
    KEEP null results, rival hypotheses and all attempted specifications
P06 TRANSFORM only authorized inputs using recorded rules and provenance
    PRESERVE missingness, UNKNOWN labels and excluded-record reasons
P07 EXECUTE the mapped code or documented analysis in the authorized environment
    RECORD actual commands, versions, inputs, outputs, uncertainty and errors
P08 VERIFY output against independent expectations and relevant negative cases
    IF a required check fails: isolate dependent output; record FAILED or BLOCKED
P09 REVIEW system-wide effects, bottlenecks, feedback and unintended consequences
    DO NOT feed frozen holdout results into the same model/design being evaluated
P10 SAVE to the authorized canonical destination; read back external writes
    REPORT design, implementation and execution status separately
    RETURN verified outputs, limitations, unresolved dependencies and next action
ON SAFETY_BLOCK: stop all writes in the affected run; record the block if permitted
ON second failed repair of the same blocker: log it; advance only to an independent task
END
```

## 3. Connect design to executable evidence

Maintain bidirectional traceability: requirement → pseudocode step → actual function/script or documentary procedure → verification check → output artifact. Fill the following fields for every material step: step_id, inputs, outputs, dependencies, implementation_ref, verification_ref, failure_behavior and status. A source path or directory alone does not prove an implementation. Use an actual function, section or command when it has been inspected. Keep unfilled references null and mark the step PROPOSED; never create a PASS by filling a template.

Use `research-method/contract.template.json` as the starting structure. Add a project-scoped contract to the existing project record rather than creating a new workbook for every run. A GitHub root guide applies across its subprojects; each substantive project still needs its own boundary and algorithm instantiation. Follow the nearest project instructions, and record unresolved conflicts before dependent work.

## 4. Evidence and interpretation

Keep VERIFIED EXECUTION, SOURCE-REPORTED, PROPOSED, SIMULATED, NOT TESTED, BLOCKED and FAILED distinct. Preserve existing scientific results and all null or contradictory findings. Do not select hypotheses solely for statistical significance. Separate causal claims, prediction, description, interpretation and normative design. Published regression tables can inform prior evidence and replication design; they do not supply unseen raw observations or guarantee transportability.

For predictive work, use point-in-time features and independent entity/time holdouts where appropriate. For causal work, state the estimand, identification assumptions, selection and robustness. For qualitative work, retain passage-level evidence, rival readings, reflexive notes and negative cases. Human review must be real; simulated reviewers do not establish independent annotation or professional approval.

## 5. Feedback and change control

At the end of a work packet, reconcile intended and observed outputs. Record the error signal, responsible reviewer, response, date and affected next version. Feedback may improve a later model or specification; preserve the frozen evaluation set and the full search record. Record bottleneck changes, spillovers and costs alongside the local metric. Preserve pause states, project-specific quotas and schedules. This method does not start background jobs or resume paused work.

## 6. Destinations and information boundaries

Google Drive remains authoritative where configured; reuse existing Docs and workbooks, adding a run tab where needed. GitHub stores the permitted code, design and version history. Hugging Face and Kaggle receive only explicitly authorized artifacts through authenticated write access and verified readback. Do not transfer restricted source data, confidential manuscripts, credentials or patent-sensitive details to public repositories. A generic method document can be shared separately from private project instantiations. Updating one platform does not update another automatically.

## Acceptance scenarios

| Scenario | Required response |
|---|---|
| Missing source date, unresolved identity or unapproved destination | BLOCKED; preserve uncertainty and avoid dependent execution/export |
| Hypothesis has a null or contradictory estimate | Retain it with uncertainty and the full tested specification |
| CAM is absent, or no material weakness is disclosed | Preserve the observed label; do not infer effectiveness |
| Project is paused, or current run reports SAFETY_BLOCK | Preserve the pause; stop dependent work and affected writes |
| Algorithm written but code not executed | PROPOSED / NOT TESTED; no trained-model or empirical-result claim |
| Output is technically correct but harms the wider objective | Record the tradeoff and system feedback; review before the next version |

## Method references

- NASA, *Systems Engineering Handbook*: system boundaries, stakeholder needs, interfaces, verification, validation and iterative feedback. https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/ and https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/
- Wilkinson et al. (2016), *The FAIR Guiding Principles for scientific data management and stewardship*, Scientific Data, 3, 160018. https://doi.org/10.1038/sdata.2016.18

These sources support the method; adopting it does not establish journal acceptance, empirical validity or repository-wide compliance.

## Project instantiation: Saehon/Saeid-Homayoun

Status: PROPOSED operational design; implementation and result verification are separate.

| Element | Project definition |
|---|---|
| Boundary | Existing software interface, caller-visible outcome and upstream compatibility |
| Inputs | Existing repository documentation, authorized change request, supported inputs and expected outcomes |
| Core transformation | Write the smallest coherent algorithm; preserve interface and attribution; map state changes, failure paths and verification to existing code |
| Outputs | Reviewable change or documented method with focused verification and unresolved limits |
| Stock | Open defects and unreviewed change requests |
| Flow | Request intake, implementation, review and verified closure |
| Delay | Implementation, integration and deployment/release timing |
| Feedback | Observed failures and user review → a separate, versioned correction |

Domain rule: Owner workflow additions do not imply ownership of upstream code or upstream endorsement; preserve runtime and release policies.

```text
D01 CONFIRM the above boundary, unit, cutoff, sources and active instructions
D02 INGEST and verify: Existing repository documentation, authorized change request, supported inputs and expected outcomes
D03 TRANSFORM: Write the smallest coherent algorithm; preserve interface and attribution; map state changes, failure paths and verification to existing code
D04 VALIDATE with prespecified baselines, rival explanations and independent evidence
D05 OUTPUT: Reviewable change or documented method with focused verification and unresolved limits
D06 CLOSE the loop: Observed failures and user review → a separate, versioned correction
```

Map D01–D06 to P01–P10 and actual code/documentary procedures before claiming execution. Keep individual manuscript targets, source populations and evidence statuses separate.

## Public repository scope

This is owner workflow guidance only. The original README, upstream purpose and repository instructions define the actual task. Instantiate domain-specific research designs in their authorized project records; do not reinterpret this repository as an ICFR, CAM, valuation or asset-pricing study merely because this method is present.
