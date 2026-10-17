Who Assures the Agents? Evidence-Governed Multi-Agent Architectures for Audit Risk

Anonymous manuscript prepared for Management Science (Accounting)

Abstract

Artificial intelligence is moving from a tool used by auditors to autonomous or semi-autonomous agents that can generate evidence, assess controls, rank risks, recommend procedures, and challenge professional judgments. Existing research shows that formal controls and tone at the top jointly shape assurance, reporting systems can be stress-tested for resilience, automation can improve internal-control quality while reducing monitoring, AI can change audit production, and generative large language models can operationalize accounting constructs when construct validity is explicitly governed. Yet these literatures largely evaluate AI as an input to human decisions rather than as a decision-making actor that itself requires assurance. We develop an evidence-governed multi-agent architecture anchored in the classical audit-risk decomposition AR = IR × CR × DR. The architecture separates specialist risk estimation from evidence validation, independent falsification, and selective human approval. We derive conditions under which additional AI or human review layers reduce rather than introduce error, and show how evidence quality changes the error technology of a decision layer. We then specify a falsifiable research design comparing a generalist LLM, specialist agents, provenance controls, challenger agents, and human review, and instantiate the design in a bounded Microsoft FY2026 proof of concept. The contribution is an auditable architecture and empirical agenda for answering a new management question: who assures the agents when AI itself becomes part of the control and audit system?

Keywords: artificial intelligence; audit risk; internal control; multi-agent systems; human-AI governance

1. Introduction

Artificial intelligence (AI) is becoming embedded in accounting and auditing at the same time that the technology itself is becoming more agentic. Earlier generations of audit analytics largely retrieved, classified, or summarized information for human professionals. Newer systems can decompose tasks, call tools, retrieve evidence, reason across heterogeneous sources, initiate tests, critique other agents, and propose final judgments. This transition changes the governance problem. When an AI system merely supplies an input, the auditor can treat it as another analytical tool. When multiple AI agents generate and evaluate evidence across a decision process, the system itself becomes part of the assurance environment.

The emerging literature provides strong building blocks but leaves this assurance problem unresolved. Penno (2021) formalizes the relation between costly formal controls and tone at the top. Kim et al. (2022) show that internal-control weaknesses, restatements, untimely filings, amendments, and regulatory correspondence jointly reveal fragile reporting environments. deHaan et al. (2023) demonstrate that financial reporting can be studied as a resilient process by using COVID-19 as a stress test. Ashraf (2025) finds that automation is associated with fewer internal-control material weaknesses, while also documenting that monitoring can decline after automation and that failures, when they occur, can be more consequential. Law and Shen (2024) show that AI adoption in audit offices changes skill demand and is associated with more accurate going-concern and internal-control opinions. de Kok (2025) establishes the power of generative large language models (LLMs) for accounting textual analysis while emphasizing construct validity, bias, reproducibility, and validation. Krakowski et al. (2025) provide field evidence on human-centered AI, and Zhong (2025) shows theoretically that layers of humans and technologies can both correct existing errors and introduce new ones. Together, these studies move the frontier from control, to resilience, to automation, to AI-assisted judgment, and finally to multilayer human-machine decision architecture.

What is missing is an assurance theory and operating architecture for AI agents that themselves participate in accounting and audit judgments. The practical question is no longer only whether AI improves audit quality. It is also who verifies the evidence selected by an agent, who challenges its inference, how the system treats missing evidence, how errors propagate between agents, how human review is allocated, and how these mechanisms connect to the audit-risk model that auditors already use. These questions matter because algorithmic systems can simultaneously increase processing capacity and create new forms of opacity, correlated error, automation bias, and control displacement (Brown-Liburd et al. 2015; Kellogg et al. 2020; Raisch and Krakowski 2021).

We develop an evidence-governed multi-agent architecture anchored in the conventional audit-risk decomposition. The architecture does not replace audit risk with a proprietary AI score. Instead, it keeps the familiar relationship among inherent risk (IR), control risk (CR), and detection risk (DR) and assigns specialist agents to produce auditable evidence relevant to those components. A separate evidence layer maintains provenance and claim support; an independent challenger attempts to falsify the proposed conclusion; and a human gate makes or approves consequential decisions. This separation is designed to preserve professional accountability while taking advantage of specialized machine capabilities.

The paper makes four contributions. First, it links the accounting literature on assurance and internal control with the management literature on human-AI decision architecture. Second, it develops a simple error-transition model showing when an additional AI or human layer reduces expected error and how evidence quality changes that condition. Third, it provides a decision-theoretic interpretation of the classical audit-risk model: high IR and CR mechanically reduce allowable DR, thereby creating a principled trigger for additional procedures, stronger evidence, independent challenge, or human escalation. Fourth, it proposes a reproducible empirical program that compares a single generalist LLM, specialist agents, evidence governance, independent challenge, and human review on temporally held-out reporting failures. A bounded Microsoft FY2026 prototype demonstrates the workflow but is not presented as empirical validation.

For managers, audit firms, internal-audit functions, regulators, and enterprise AI developers, the central implication is that the durable capability is not a particular foundation model. The durable capability is an evidence and decision-control layer that can route tasks to replaceable models, preserve source lineage, separate risk assessment from assurance, measure disagreement and uncertainty, and allocate scarce human attention to cases where it has the greatest expected value.

Figure 1. Scientific foundation and the unresolved AI-assurance gap.

2. Scientific Foundation and Research Gap

2.1 Assurance, formal control, and observable reporting failure

Penno (2021) provides a useful starting point because assurance is fundamentally a control-allocation problem. Formal controls are costly, and their optimal intensity depends on other governance mechanisms, including tone at the top. The important implication for AI-mediated work is that technology does not enter a vacuum. It enters an existing control system in which formal procedures, managerial incentives, monitoring, and external assurance may operate as complements or substitutes. An AI control that appears strong in isolation can therefore reduce other monitoring effort, creating a displacement effect that must be measured rather than assumed away.

Kim et al. (2022) shift attention from abstract control quality to observable manifestations of reporting failure. Their SPAC setting shows that internal-control weaknesses, restatements, untimely reporting, amended filings, and extended SEC comment-letter processes jointly signal lower reporting quality. For an AI assurance architecture, this suggests a critical design principle: risk scores should be linked to future observable outcomes rather than validated against the model's own labels. A system that labels an account high risk is scientifically useful only if the label predicts or explains outcomes that were not used to construct the score.

2.2 Resilience, automation, and monitoring substitution

deHaan et al. (2023) conceptualize financial reporting as a process that can be stress-tested. Their evidence that most firms maintained reporting timeliness and quality through the COVID shock implies that a useful risk engine should distinguish ordinary complexity from fragility revealed under stress. This motivates longitudinal and shock-based features rather than static cross-sectional scores. A company-level digital twin can therefore be viewed not as a visual metaphor but as a time-indexed state representation against which disruptions, control changes, disclosure shifts, and audit responses can be evaluated.

Ashraf (2025) provides a second important mechanism. Automation is associated with fewer internal-control material weaknesses, but monitoring declines after adoption, and failures that remain can be more material. This result cautions against treating automation as an unconditional reduction in control risk. In our framework, automated controls can reduce CR when their design and operating effectiveness are supported by evidence, but automation can also increase model dependence and reduce human monitoring. The architecture therefore separates control effectiveness from monitoring intensity and explicitly represents evidence gaps instead of coding missing evidence as low risk.

This monitoring-substitution mechanism is central to the RiskOS research design. The system should not infer that more automation necessarily implies lower control risk. Instead, automation intensity and residual human monitoring are distinct state variables. A firm can simultaneously exhibit stronger automated controls and greater dependence on a smaller set of monitoring points, creating concentration risk when the automated process, data pipeline, or supervising agent fails.

2.3 AI, construct validity, and human-machine decision architecture

Law and Shen (2024) provide direct evidence that AI changes the audit production function. Audit offices that hire AI employees exhibit more accurate going-concern and internal-control opinions and greater demand for cognitive skills, while their interview evidence indicates that practitioners do not view AI as simply replacing auditors. This pattern is consistent with an augmentation architecture in which machines alter task allocation and the marginal value of human judgment.

The measurement problem becomes sharper with generative AI. de Kok (2025) argues that LLMs can perform accounting textual-analysis tasks that previously required hand coding, but their usefulness depends on construct validity, prompt and model choices, bias assessment, and reproducibility. The implication for audit risk is fundamental: a plausible model output is not evidence merely because it is fluent. The system must preserve the source, transformation steps, model version, and claim-to-evidence relationship so that an auditor or reviewer can determine whether the output measures the intended construct.

The broader management literature explains why a simple 'human in the loop' statement is insufficient. Raisch and Krakowski (2021) show that automation and augmentation are interdependent rather than clean alternatives. Krakowski et al. (2025) provide field evidence on human-centered AI and decision outcomes. Human responses to algorithms are themselves unstable: people can become algorithm averse after observing errors (Dietvorst et al. 2015) yet also display algorithm appreciation in other contexts (Logg et al. 2019). Thus, human review must be designed as a decision policy, not treated as a universal corrective.

Zhong (2025) formalizes the key architectural issue: in multilayer decision processes, each layer may correct previous errors and introduce new errors. This insight is especially relevant for agentic accounting systems because a retrieval agent, risk-classification agent, control-testing agent, reviewer agent, and human can each improve the decision and can each contaminate it. The unresolved research gap is therefore an assurance architecture that connects multilayer error correction to recognized accounting risk constructs and observable evidence.

Table 1. Research chain and the incremental gap

| Study | Core insight | What it contributes here | Remaining issue |

| --- | --- | --- | --- |

| Penno (2021) | Formal controls and tone at the top can complement or substitute. | Assurance is a control-allocation problem. | No agentic AI or evidence-provenance layer. |

| Kim et al. (2022) | Reporting failure is observable through multiple outcomes. | Defines external validation targets. | Does not address AI-generated judgments. |

| deHaan et al. (2023) | Reporting processes can be stress-tested for resilience. | Motivates temporal stress testing. | No multilayer AI governance. |

| Ashraf (2025) | Automation can improve ICFR but monitoring can fall. | Separates control quality from monitoring. | Automation is not itself assured. |

| Law & Shen (2024) | AI changes audit labor and improves opinion accuracy. | AI can augment audit quality. | Who assures AI outputs is unresolved. |

| de Kok (2025) | LLM measurement requires construct validation. | Evidence and model provenance are necessary. | Focuses on research measurement, not audit-risk orchestration. |

| Krakowski et al. (2025) | Human-centered AI changes decision performance. | Motivates contingent human-AI design. | No audit-risk decomposition. |

| Zhong (2025) | Each decision layer corrects and creates errors. | Provides multilayer error logic. | No accounting-specific assurance architecture. |

3. An Evidence-Governed Multi-Agent Audit-Risk Model

3.1 Preserve the audit-risk spine

The framework begins with the audit-risk model rather than an AI-native composite score. PCAOB AS 1101 defines audit risk as a function of the risk of material misstatement and detection risk; inherent risk and control risk are assessed from the company, its environment, internal control, and evidence, whereas detection risk depends on the effectiveness and execution of audit procedures. The higher the assessed risk of material misstatement, the lower detection risk must be to reduce audit risk to an appropriately low level. This structure gives a natural place for specialist AI agents without changing the meaning of the audit constructs.

For an account or disclosure i, assertion a, and period t, write the research representation as follows:

ARᵢₐₜ = IRᵢₐₜ × CRᵢₐₜ × DRᵢₐₜ     (1)

Equation (1) is a structural decomposition, not a claim that practical audit-risk assessments are observed statistical probabilities. In the prototype and proposed tests, normalized indices can be used for ranking and decision rules, but their calibration must be established against external outcomes before they are interpreted probabilistically.

Given a target audit-risk level AR*, the allowable detection-risk level is:

DR*ᵢₐₜ = AR* / (IRᵢₐₜ × CRᵢₐₜ)     (2)

Equation (2) transforms a risk dashboard into an audit-resource allocation rule. If inherent risk or control risk increases, allowable detection risk falls, requiring stronger procedures, better evidence, broader coverage, more specialist involvement, or additional review. This is also the conceptual bridge between risk assessment and the economics of audit effort.

3.2 Each assurance layer can correct and create errors

Let eₖ denote the probability that the case entering decision layer k contains a decision-relevant error. Let cₖ be the probability that layer k corrects an existing error, and let hₖ be the probability that the same layer introduces a new error when the incoming state is correct. The residual error after the layer is:

eₖ₊₁ = eₖ(1 − cₖ) + (1 − eₖ)hₖ     (3)

This expression intentionally treats AI agents and humans symmetrically: neither is assumed to be infallible. A layer is beneficial when eₖ₊₁ < eₖ, which occurs if:

eₖ > hₖ / (cₖ + hₖ)     (4)

Equation (4) yields a practical escalation principle. An extra challenger or human review layer is not automatically value increasing. It is useful when the incoming error risk is sufficiently high relative to the layer's own tendency to introduce error. This result is consistent with Zhong's (2025) emphasis on both correction capability and new-error generation, but it is adapted here to audit-risk governance and evidence review.

3.3 Evidence quality changes the error technology

Let z denote evidence quality, including source authority, completeness, temporal alignment, reproducibility, and claim-level traceability. We assume that better evidence weakly increases correction capability and weakly reduces new-error generation: dc/dz ≥ 0 and dh/dz ≤ 0. Differentiating Equation (3) gives:

∂eₖ₊₁/∂z = −eₖ(∂cₖ/∂z) + (1 − eₖ)(∂hₖ/∂z) ≤ 0     (5)

Evidence governance is therefore not a documentation afterthought; it changes the expected performance of the decision layer. In implementation, the evidence passport should store the source identifier, source date, retrieval date, transformation history, model/version, applicable jurisdiction, claim support, and unresolved limitations. Missing evidence should remain missing. Converting absence of evidence into a low-risk value would mechanically bias IR, CR, or DR downward.

3.4 Specialist agents versus a generalist model

A multi-agent architecture introduces a trade-off. Specialist agents can reduce domain-specific error, but routing and coordination can create additional error and cost. Let πd be the importance weight of domain d, ed its residual specialist error, eg the comparable generalist error, and κ the routing/coordination error. The specialist architecture has residual error:

eˢ = Σd πd eᵈ + κ     (6)

Specialization dominates a generalist model when Σd πd(eg − ed) > κ. This condition clarifies why simply adding agents is not a contribution. The architecture must demonstrate that the accuracy and evidence gains from specialization exceed orchestration error, latency, and cost.

3.5 Expected-loss escalation and the Human Gate

Human review is scarce and expensive. Let LFN and LFP denote the costs of false negatives and false positives, LU the cost of unsupported claims, and CH the cost of human review. A case should be escalated when the expected reduction in decision loss from human review exceeds CH. This policy makes the Human Gate contingent on materiality, uncertainty, agent disagreement, evidence quality, and the asymmetry of error costs. High-risk revenue recognition, fraud, or regulatory cases may justify review at much lower estimated error rates than routine classifications.

Figure 2. Evidence-governed multi-agent architecture anchored in the classical audit-risk model.

4. Testable Propositions and Hypotheses

Proposition 1 (Audit-effort response). For a fixed target audit risk AR*, allowable detection risk is strictly decreasing in inherent risk and control risk whenever IR > 0 and CR > 0. Thus, higher assessed IR or CR creates a mechanical requirement for stronger detection capability or greater audit evidence.

Proposition 2 (Value of an additional assurance layer). An additional AI or human review layer reduces expected decision error if and only if the incoming error probability exceeds h/(c+h), where c is the layer’s correction probability and h is its new-error probability.

Proposition 3 (Evidence governance). If higher evidence quality weakly increases correction capability and weakly decreases new-error generation, residual decision error is nonincreasing in evidence quality.

Proposition 4 (Specialization). A specialist multi-agent architecture outperforms a single generalist model when the weighted reduction in domain-specific error exceeds routing and coordination error.

The analytical propositions motivate eight empirical hypotheses that can be evaluated using held-out accounting outcomes and controlled human-review experiments.

H1: An evidence-governed specialist-agent system will produce a lower unsupported-claim rate than a single generalist LLM on the same audit-risk tasks.

H2: Specialist routing will improve out-of-time prediction and classification of reporting failures relative to a generalist LLM, after controlling for model family and information set.

H3: An independent challenger will produce the largest incremental reduction in false negatives when incoming inherent risk, control risk, or cross-agent disagreement is high.

H4: Evidence passports will improve calibration, claim-support precision, and run-to-run reproducibility relative to identical agents without enforced provenance.

H5: A selective Human Gate based on expected loss will achieve lower total decision cost than either no human review or universal human review.

H6: The value of multi-agent assurance will be greater when evidence is heterogeneous or conflicting, because specialist disagreement becomes an informative escalation signal.

H7: The incremental value of evidence-governed challenge will be greater in settings with higher automation intensity and lower residual human monitoring, because automation can improve controls while simultaneously reducing monitoring effort.

H8: Context-dependent allocation of final authority based on each layer’s correction capability relative to its new-error rate will outperform a universal “human-last” or “AI-last” rule.

5. Architecture: Mapping Accounting Risk to Specialist Agents

The architecture separates domain risk from assurance risk. Inherent-risk agents evaluate susceptibility to material misstatement before controls. Relevant sources include accounting-policy complexity, estimates and judgments, CAM/KAM topics, enforcement or fraud indicators, cybersecurity exposure, ESG measurement complexity, financial stress, and disclosure characteristics. Control-risk agents focus on whether relevant controls prevent or detect material misstatements on a timely basis, with ICFR, IT general controls, automated controls, governance, cybersecurity controls, and sustainability-reporting controls as key evidence. Detection-risk agents evaluate whether the planned or executed assurance procedures are likely to miss an existing material misstatement, including procedure design, evidence quality, population coverage, sampling, timing, AI model risk, reviewer risk, and compliance with applicable audit requirements.

A critical design rule is applicability gating. A U.S. issuer audited under PCAOB standards should not be treated as if KAM or IFRS were its primary reporting regime. Cross-framework modules can be used as comparative or shadow analyses, but their outputs must be labeled as such. Applicability gating prevents a particularly damaging class of LLM error: technically plausible reasoning that is attached to the wrong jurisdiction, period, reporting framework, or audit regime.

The architecture also separates the model provider from the assurance layer. GPT, Claude, Gemini, an open-source model, or a firm-specific model can be swapped behind the same interface. This modularity is important both scientifically and commercially: it permits model-family fixed effects in experiments, supports reproducibility across model upgrades, and prevents the system's claimed value from collapsing into the current performance of one foundation model.

Implementation labels are deliberately separated from theoretical constructs. In the current NAAIL RiskOS prototype, MANGO denotes accounting/IFRS judgment intelligence; APPLE denotes U.S. CAM intelligence; ORANGE denotes KAM intelligence for ISA/UK/EU comparator settings; POMELO denotes forensic and enforcement intelligence; LEMON denotes ICFR; GRAPE denotes audit-workflow and procedure intelligence; PEAR denotes evidence assurance; and KIWI denotes knowledge retrieval and challenge support. Cybersecurity, ESG, finance, ITGC, governance, PCAOB, and the independent CHALLENGER are specialist services. These names are replaceable software modules; the research claims concern the IR/CR/DR functions, evidence governance, challenge, and authority allocation rather than the branding of any agent.

Table 2. Mapping risk domains into IR, CR, and DR

| Component | Representative evidence/agents | Primary question | Examples of observable validation |

| --- | --- | --- | --- |

| IR | Accounting judgments; CAM/KAM; AAER/forensic; cyber exposure; ESG; finance; disclosure text | How susceptible is the assertion to material misstatement before controls? | Restatement, AAER/enforcement, future CAM persistence, material estimate error, late filing |

| CR | ICFR; ITGC; automated controls; cyber controls; ESG controls; governance | Will controls prevent or detect/correct the misstatement on time? | Material weakness, significant deficiency proxies, control-related restatement, remediation |

| DR | Audit procedures; evidence quality; sampling/coverage; PCAOB/ISA requirements; model risk; reviewer risk | Will assurance procedures detect an existing material misstatement? | Post-audit restatement, missed enforcement issue, unsupported conclusion, evidence coverage |

| Governance | Evidence passport; independent challenger; human gate | Can the risk assessment itself be trusted and reproduced? | Claim-support precision, calibration, disagreement resolution, inter-run stability |

6. Proof of Concept: Microsoft FY2026

We instantiate the architecture in a bounded research prototype using Microsoft Corporation's FY2026 public filing as a golden-anchor case. Microsoft is useful because the filing contains extensive structured and unstructured evidence, including XBRL financial facts, complex revenue recognition, tax uncertainty, an integrated audit report, and two critical audit matters. The 2026 Form 10-K reports total revenue of $331.839 billion. Deloitte & Touche LLP identifies revenue recognition and income taxes—uncertain tax positions—as critical audit matters, and the auditor expresses an unqualified opinion on internal control over financial reporting. These facts create a sufficiently rich case to demonstrate routing, applicability, evidence lineage, and audit-risk decomposition without using confidential engagement data.

The prototype assigns normalized research-demo indices to IR, CR, and DR only to demonstrate the orchestration logic. The current illustrative values are IR = 0.6525, CR = 0.3650, and DR = 0.3775, which imply AR = 0.0899 under Equation (1). If a demonstration target AR* = 0.0500 is selected, Equation (2) gives allowable DR* = 0.2099. Because the illustrative DR index exceeds the allowable level, the orchestrator returns 'more audit assurance required' and routes the case to stronger procedures, independent challenge, and the Human Gate.

These numerical values are not calibrated probabilities, are not Microsoft's actual audit risk, and are not an audit conclusion. They serve as test fixtures for the architecture. Their scientific role is analogous to a software harness: the system must preserve identities, apply the correct formula, route applicable evidence, refuse unsupported claims, and surface gaps. A future empirical version must estimate or learn calibrated mappings from evidence to outcomes on training data and evaluate them on temporally and organizationally independent holdouts.

Table 3. Microsoft FY2026 prototype illustration

| Item | Prototype state | Interpretation / boundary |

| --- | --- | --- |

| Reporting basis / regime | U.S. GAAP / PCAOB CAM | IFRS and KAM are comparator modes only. |

| Revenue | $331.839 billion | Public FY2026 10-K fact. |

| CAMs | Revenue recognition; uncertain tax positions | High-judgment audit areas informing IR and DR analysis. |

| ICFR opinion | Unqualified | Reduces the current control-risk signal but does not imply CR = 0. |

| Illustrative IR | 0.6525 | Uncalibrated research index. |

| Illustrative CR | 0.3650 | Uncalibrated research index. |

| Illustrative DR | 0.3775 | Uncalibrated research index. |

| Illustrative AR | 0.0899 | Product of IR × CR × DR; not a probability claim. |

| Target AR / allowable DR | 0.0500 / 0.2099 | Demonstrates audit-effort response. |

| Governance | Evidence passport + challenger + Human Gate | Production approval remains outside the POC. |

7. Empirical Evaluation Design

7.1 Data and unit of analysis

The empirical study should be designed as a retrospective, temporally ordered benchmark followed by a human-review experiment. For U.S. public companies, the core public data can include SEC 10-K and 10-Q filings, CompanyFacts/XBRL, filing dates, Item 1A risk factors, Item 1C cybersecurity disclosures, auditor reports, and CAM text. Where licensing permits, Audit Analytics can supply ICFR opinions and weaknesses, restatements, audit fees, and additional auditor characteristics. SEC Accounting and Auditing Enforcement Releases (AAERs) and other enforcement records provide high-specificity adverse outcomes. Public PCAOB standards and inspection data can supply requirement and firm-level context, but inspection findings must not be imputed to a specific engagement unless the evidence supports that link. Sustainability reports and structured ESG data can be added as a separate reporting-risk domain.

The preferred unit is account-assertion-year because the audit-risk model is assertion specific. When evidence cannot be reliably mapped to an account and assertion, the unit can fall back to firm-year, but the aggregation rule should be explicit. Temporal ordering is essential: only information available as of the risk-assessment date may enter a prediction, and all labels must occur after that date. This prevents hindsight leakage, which is especially serious when LLMs can infer later events from text or metadata.

7.2 Experimental arms

The benchmark should hold the underlying foundation model and information set constant where possible and vary the assurance architecture. This permits attribution of gains to governance rather than to model scale. We propose the following arms:

A. Generalist LLM: One model receives all evidence and produces the final risk assessment.

B. Specialist agents: Separate IR, CR, and DR agents with an orchestrator, but no evidence passport or challenger.

C. Specialist + evidence governance: Arm B plus mandatory provenance, claim support, temporal checks, and applicability gating.

D. Full multi-agent assurance: Arm C plus an independent challenger/falsifier and disagreement-based escalation.

E. Human only: Experienced accountants/auditors assess a stratified case subset without AI assistance.

F. Human + full system: Humans receive Arm D outputs, evidence lineage, disagreement, and escalation recommendations.

7.3 Outcomes and metrics

Primary predictive outcomes should be adverse reporting events that were not available to the model at the decision date: future restatements, subsequently disclosed material weaknesses, enforcement events, materially late filings, and other pre-specified failure indicators. The objective is not to claim that any one outcome equals audit risk. Rather, these outcomes provide external tests of whether the architecture identifies cases with elevated reporting and assurance risk.

Performance metrics should include precision-recall area under the curve for rare events, Brier score and calibration slope/intercept, recall at a fixed review budget, false-negative cost, and expected loss under pre-specified cost weights. Agentic assurance requires additional metrics that standard prediction studies often omit: claim-support precision, percentage of conclusions with valid evidence lineage, rate of jurisdiction/framework errors, inter-run stability, model-version sensitivity, contradiction detection, and reviewer disagreement. Latency and compute cost should be measured because a multi-agent system that is marginally more accurate but prohibitively expensive may not be managerially dominant.

Validation should use nested temporal holdouts, firm holdouts, and industry holdouts. Any prompt tuning, rule adjustment, or detector repair performed after observing a failure consumes that case for development and requires fresh holdout cases for evaluation. This is particularly important for agentic systems because the boundary between 'model improvement' and test-set memorization can be subtle.

7.4 Human-review experiment

A second study can randomize experienced auditors, accountants, or advanced audit students to human-only, generalist-AI, and evidence-governed multi-agent conditions. Cases should vary ex ante in IR, CR, evidence conflict, and materiality. The main dependent variables would be decision accuracy against adjudicated case labels, calibration, evidence selection, time, confidence, override behavior, and the ability to identify deliberately planted unsupported claims. This design directly tests whether the Human Gate creates augmentation rather than automation bias. It also allows estimation of when selective escalation dominates universal review.

Table 4. Proposed evaluation matrix

| Question | Comparison | Primary metric | Falsification criterion |

| --- | --- | --- | --- |

| Does specialization help? | A vs. B | PR-AUC, Brier, Recall@k | No gain after coordination cost or out-of-time holdout. |

| Does provenance help? | B vs. C | Claim-support precision; framework errors | Evidence layer fails to improve support or reproducibility. |

| Does challenge help? | C vs. D | False negatives; contradiction detection | Challenger adds as many new errors as it corrects. |

| Does human review add value? | D vs. F; E vs. F | Expected loss; time; calibration | Human+AI does not beat the better standalone condition. |

| Is escalation efficient? | Universal vs. selective review | Loss + review cost | Selective policy does not reduce total cost. |

| Does the system generalize? | Within-time vs. future/industry holdouts | Calibration drift; performance decay | Performance collapses outside development distribution. |

8. Managerial Implications and the Source of Defensible Advantage

The framework has a direct managerial interpretation. For an audit firm, IR and CR estimates determine the detection capability required from the audit plan. The system can therefore function as an audit-effort allocator rather than as a black-box risk label: when IR or CR rises, the allowable DR threshold falls and the system must specify what additional procedures, coverage, evidence, specialist review, or timing changes are needed. PCAOB AS 2301 is consistent with this logic because it links higher assessed risk to more persuasive substantive evidence and changes in the nature, timing, and extent of procedures.

For controllers and internal-audit functions, the architecture separates the value of automation from the strength of controls over automation. An automated reconciliation or AI classification system can improve operating effectiveness while simultaneously creating concentration risk, data-dependence, and monitoring substitution. The control-risk layer can therefore record both the automated control and the ITGC/model-governance evidence on which reliance depends.

For regulators and audit committees, the most useful output may be the audit trail rather than the score. A regulator should be able to reconstruct which data were used, which agent produced a conclusion, which other agent challenged it, whether disagreement remained, which human approved the decision, and whether the model or prompt changed. This architecture is closer to inspectable assurance than to conversational AI.

For a startup or platform provider, the defensible advantage is consequently not the chat interface and not any particular LLM. The durable assets are the applicability ontology, account-assertion risk graph, evidence passports, longitudinal outcome labels, domain-specific benchmarks, falsification suite, and human-decision logs. These assets can survive model substitution and can compound as new validated cases accumulate. In economic terms, the platform creates switching costs through evidence and governance infrastructure rather than through model access.

The architecture also creates a natural product boundary. Accounting-standard interpretation, CAM/KAM intelligence, ICFR, forensic/AAER, cybersecurity, ESG, PCAOB requirements, and financial-risk modules may be separate specialist services, but they should not produce independent opaque scores. Their outputs should be normalized into the IR/CR/DR decision structure with evidence provenance and applicability metadata. This permits modular innovation while preserving a stable assurance grammar.

9. Limitations and Boundary Conditions

Several limitations are fundamental rather than temporary. First, audit risk, inherent risk, control risk, and detection risk are professional judgment constructs; they are not directly observed probabilities. The prototype's normalized indices must therefore not be interpreted as calibrated failure probabilities without external validation. Second, realized adverse outcomes are incomplete labels. Many material risks never result in restatement or enforcement, while some restatements arise from conditions that were not reasonably detectable at the original audit date. Evaluation must therefore combine outcome prediction with case-level expert adjudication and evidence-quality metrics.

Third, public filings reveal only part of the audit process. They do not expose the full population of audit procedures, control testing, consultations, internal firm tools, or engagement-level PCAOB inspection evidence. A public-data benchmark can test risk identification and evidence governance but cannot fully estimate engagement detection risk. Field partnerships would be required for that step. Fourth, CAMs and KAMs are themselves auditor outputs and may be endogenous to the audit process; they should be treated as evidence about attention and judgment, not as exogenous ground truth.

Fifth, multi-agent systems can create correlated errors. Agents that share the same foundation model, retrieval corpus, or prompt assumptions may agree for the wrong reason. Independent challenge should therefore vary model, prompt, evidence path, or rule set where feasible. Disagreement is informative only if the agents are genuinely capable of producing partially independent error. Sixth, human review can fail through overload, anchoring, automation bias, or algorithm aversion. The Human Gate must be evaluated empirically rather than assumed to solve model error.

Finally, an evidence-governed architecture can create a false sense of precision if the governance interface is stronger than the underlying data. The appropriate scientific standard is falsifiability: every claimed improvement should be tested on fresh cases, and every repair made after observing a failure should be evaluated on new holdouts. The system should be allowed to remain unresolved when evidence is insufficient.

10. Conclusion

The scientific chain from formal control to reporting resilience, automation, AI-enabled audit quality, LLM measurement, human-AI augmentation, and multilayer decision theory leads to a specific unanswered question: who assures the AI agents that increasingly participate in accounting and audit decisions? We propose that the answer should not be another opaque AI score. It should be an evidence-governed architecture that preserves the classical audit-risk decomposition, assigns specialist agents to IR, CR, and DR tasks, records claim-level provenance, introduces independent challenge, and allocates human review according to expected value.

The analytical model yields simple but actionable conditions. High IR and CR require lower allowable DR. An extra assurance layer reduces expected error only when its correction capability is large enough relative to the new errors it introduces. Better evidence lowers residual error when it improves correction and reduces new-error generation. Specialist agents are valuable only when their domain gains exceed orchestration costs. These conditions convert broad calls for 'human oversight' and 'responsible AI' into testable management policies.

The Microsoft prototype demonstrates how such a system can operate without claiming that a research index is an audit probability. The next step is empirical: benchmark the architecture on temporally held-out reporting outcomes, test claim-level evidence support, and measure whether independent challenge and selective human escalation reduce expected decision loss. If these tests succeed, the contribution extends beyond auditing. Any high-stakes enterprise process in which AI agents create, evaluate, and authorize evidence faces the same management problem: assurance must become an explicit layer of the AI operating model.

References

Ashraf M (2025) Does automation improve financial reporting? Evidence from internal controls. Review of Accounting Studies 30:436–479. https://doi.org/10.1007/s11142-024-09822-y

Brown-Liburd H, Issa H, Lombardi D (2015) Behavioral implications of Big Data’s impact on audit judgment and decision making and future research directions. Accounting Horizons 29(2):451–468. https://doi.org/10.2308/acch-51023

deHaan E, de Kok T, Matsumoto D, Rodriguez-Vazquez E (2023) How resilient are firms’ financial reporting processes? Management Science 69(4):2536–2545. https://doi.org/10.1287/mnsc.2023.4670

de Kok T (2025) ChatGPT for textual analysis? How to use generative LLMs in accounting research. Management Science. Published online January 13, 2025. https://doi.org/10.1287/mnsc.2023.03253

Dietvorst BJ, Simmons JP, Massey C (2015) Algorithm aversion: People erroneously avoid algorithms after seeing them err. Journal of Experimental Psychology: General 144(1):114–126. https://doi.org/10.1037/xge0000033

Kellogg KC, Valentine MA, Christin A (2020) Algorithms at work: The new contested terrain of control. Academy of Management Annals 14(1):366–410. https://doi.org/10.5465/annals.2018.0174

Kim J, Park S, Peterson K, Wilson R (2022) Not ready for prime time: Financial reporting quality after SPAC mergers. Management Science 68(9):7054–7064. https://doi.org/10.1287/mnsc.2022.4478

Kokina J, Davenport TH (2017) The emergence of artificial intelligence: How automation is changing auditing. Journal of Emerging Technologies in Accounting 14(1):115–122. https://doi.org/10.2308/jeta-51730

Krakowski S, Haftor D, Luger J, Pashkevich N, Raisch S (2025) Human-centered artificial intelligence: A field experiment. Management Science 72(1):57–72. https://doi.org/10.1287/mnsc.2022.03849

Law KKF, Shen M (2024) How does artificial intelligence shape audit firms? Management Science 71(5):3641–3666. https://doi.org/10.1287/mnsc.2022.04040

Logg JM, Minson JA, Moore DA (2019) Algorithm appreciation: People prefer algorithmic to human judgment. Organizational Behavior and Human Decision Processes 151:90–103. https://doi.org/10.1016/j.obhdp.2018.12.005

Microsoft Corporation (2026) Annual Report on Form 10-K for the fiscal year ended June 30, 2026. U.S. Securities and Exchange Commission, accession 0001193125-26-323660. https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm

PCAOB (Public Company Accounting Oversight Board) AS 1101: Audit Risk. https://pcaobus.org/oversight/standards/auditing-standards/details/AS1101

PCAOB (Public Company Accounting Oversight Board) AS 2301: The Auditor’s Responses to the Risks of Material Misstatement. https://pcaobus.org/oversight/standards/auditing-standards/details/AS2301

Penno M (2021) A theory of assurance: Balancing costly formal control with tone at the top. Management Science 68(1):654–668. https://doi.org/10.1287/mnsc.2020.3861

Raisch S, Krakowski S (2021) Artificial intelligence and management: The automation–augmentation paradox. Academy of Management Review 46(1):192–210. https://doi.org/10.5465/amr.2018.0072

Vasarhelyi MA, Kogan A, Tuttle BM (2015) Big Data in accounting: An overview. Accounting Horizons 29(2):381–396. https://doi.org/10.2308/acch-51071

Zhong H (2025) Optimal integration: Human, machine, and generative AI. Management Science 72(5):3720–3739. https://doi.org/10.1287/mnsc.2024.07401

PCAOB (Public Company Accounting Oversight Board) AS 3101: The Auditor’s Report on an Audit of Financial Statements When the Auditor Expresses an Unqualified Opinion. https://pcaobus.org/oversight/standards/auditing-standards/details/AS3101

PCAOB (Public Company Accounting Oversight Board) AS 2315: Audit Sampling. https://pcaobus.org/oversight/standards/auditing-standards/details/AS2315

PCAOB (Public Company Accounting Oversight Board) AS 2201: An Audit of Internal Control Over Financial Reporting That Is Integrated with An Audit of Financial Statements. https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201

PCAOB (Public Company Accounting Oversight Board) AS 2110: Identifying and Assessing Risks of Material Misstatement. https://pcaobus.org/oversight/standards/auditing-standards/details/AS2110

PCAOB (Public Company Accounting Oversight Board) AS 1220: Engagement Quality Review. https://pcaobus.org/oversight/standards/auditing-standards/details/AS1220

PCAOB (Public Company Accounting Oversight Board) AS 1105: Audit Evidence. https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105

Online Appendix A. Proposed Reproducibility Package

A submission-ready empirical version should archive the following items: (1) source registry with license and provenance status; (2) data dictionary at firm-year and account-assertion-year levels; (3) chronology-safe feature builder; (4) frozen prompts and model identifiers; (5) deterministic calculation code for AR, allowable DR, and escalation rules; (6) gold labels separated from development labels; (7) blinded holdout cases; (8) agent transcripts or hashed execution traces; (9) evidence-passport schema; (10) falsification probes; (11) calibration and expected-loss scripts; and (12) a human-review protocol with adjudication rules.

The code repository should distinguish development examples from test data. Once a failure case is observed and used to modify the system, that case is consumed for development and must not be used to claim out-of-sample improvement. This rule is essential for scientifically credible agent assurance because iterative prompt and rule changes can otherwise overfit a small set of known failures.

Draft status: analytical framework + research design + bounded proof of concept. No empirical causal or audit-opinion claim is made.

## Online Appendix B. Operational Multi-Agent Architecture

This appendix translates the theoretical architecture into an implementable service catalog. It reconciles the prototype labels with the canonical project taxonomy so that software names do not drift across versions. The empirical design should treat the agent label as an implementation detail and the risk function as the unit of theory.

| Layer | Service | Primary function | Representative outputs | Validation anchor |

| --- | --- | --- | --- | --- |

| IR | MANGO | Accounting / IFRS judgment and reporting complexity | Accounting-policy complexity, estimates, recognition/measurement judgments, cross-framework comparison | ISA 315 concepts; applicable GAAP/IFRS requirements |

| IR | APPLE | U.S. CAM intelligence | CAM topics, associated accounts/assertions, audit effort and recurring judgment areas | PCAOB AS 3101 |

| IR | ORANGE | KAM comparator intelligence | KAM topics for ISA/UK/EU settings; comparator-only when not applicable | ISA 701 / jurisdiction gate |

| IR | POMELO | Forensic / AAER / enforcement intelligence | Fraud and misstatement indicators, enforcement history, anomaly evidence | Fraud-risk framework; enforcement provenance |

| IR | FINANCE | Financial stress / going concern | Liquidity, leverage, cash-flow stress, scenario analysis | PCAOB AS 2415 / ISA 570 |

| IR/CR | CYBER | Cyber exposure and cyber-control intelligence | Reporting-system exposure (IR) and IT/cyber controls (CR) | NIST/COBIT as control references; applicable SEC/PCAOB requirements |

| IR/CR | ESG | Sustainability reporting risk and controls | Measurement complexity (IR), data governance and reporting controls (CR) | Applicable sustainability standards and assurance criteria |

| CR | LEMON | ICFR design and operating effectiveness | Control design, operation, deficiencies, material-weakness indicators | PCAOB AS 2201; COSO |

| CR | ITGC | IT general controls | Access, change management, operations, interfaces, service-organization controls | PCAOB integrated-audit requirements; COBIT/ISO references |

| CR | Governance | Board / audit-committee and monitoring environment | Oversight, tone at top, internal audit, whistleblowing, monitoring concentration | COSO control environment; PCAOB AS 1301 communications |

| DR | GRAPE | Audit procedure design and execution | Response to assessed risk, procedure coverage, timing, population testing, exceptions | PCAOB AS 2301; ISA 330 |

| DR | PEAR | Evidence quality and sufficiency | Reliability, relevance, contradictions, traceability, Evidence Passport | PCAOB AS 1105; ISA 500 |

| DR | PCAOB | Standards applicability / inspection-readiness context | Applicable requirements, procedure-to-standard mapping, compliance gaps | Applicable PCAOB auditing standards |

| Governance | KIWI | Knowledge retrieval and challenge support | Source retrieval, provenance checks, cross-agent contradiction discovery | Source authority and temporal validity |

| Governance | CHALLENGER | Independent falsification | Alternative hypotheses, benchmark challenges, contradiction matrix, re-estimation | Pre-specified challenge protocols |

| Governance | NAAIL BOARD / Human Gate | Final authority and override governance | Approve, modify, reject, escalate; documented override rationale | Engagement quality review and professional judgment requirements |

A central architectural rule is non-substitution across layers. A CAM/KAM, forensic, cyber, or ESG signal may inform inherent risk; it does not automatically establish control failure. An unqualified ICFR opinion may reduce a control-risk signal; it does not establish zero control risk. PCAOB inspection themes may inform detection-risk procedure design; firm-level inspection findings must not be represented as engagement-level findings without direct evidence.

## Online Appendix C. Evidence Passport, Construct-Validity Gate, and Falsification Protocol

Every material claim is represented as a versioned Evidence Passport. At minimum, the object should contain the claim, source identifier, source date, retrieval date, transformation lineage, reporting framework, audit regime, account/assertion mapping, model and prompt version, confidence or uncertainty statement, validation status, challenger disposition, and human-gate status. Missing evidence is represented as PENDING or UNRESOLVED, never as a low-risk PASS.

| Evidence_ID: unique immutable identifier Source_Agent: specialist service and version Risk_Component: IR / CR / DR / Governance Claim: atomic decision-relevant statement Sources: identifiers, dates, authority, rights/provenance Applicability: entity, period, jurisdiction, reporting basis, audit regime Transformations: extraction, calculations, mappings, model/prompt version Construct_Validity: definition, measurement method, bias checks, replicability Challenge_Status: supported / contested / unresolved / overturned Human_Gate: reviewer, decision, rationale, timestamp Audit_Trail: every state transition and modification |

| --- |

The CHALLENGER is deliberately independent of the originating agent. It applies at least five pre-specified protocols: (1) factual consistency across agents; (2) source verification; (3) alternative-hypothesis construction; (4) peer or benchmark comparison; and (5) historical or outcome validation. Additional assumption and contradiction tests are permitted, but the protocol applied to each case must be logged before a claimed test result is evaluated.

A challenged conclusion can be supported, contested, unresolved, or overturned. The original agent may supply additional evidence or accept the challenge, but unresolved disagreement is not averaged away. It is routed to a human gate according to expected decision loss, materiality, and the cost of further review.

## Online Appendix D. Minimal Executable POC and Scientific Boundaries

The companion prototype supplied with the project demonstrates the mechanics of a specialist risk agent, an independent challenger, a Human Gate, and machine-readable evidence logging. Its purpose is software falsifiability: a third party can execute the same inputs and inspect the resulting state transitions. It is not presented as a validated audit methodology.

| Step | Control | Required behavior |

| --- | --- | --- |

| 1 | Ingest | Load a reconciled GL or public-company evidence bundle. Record source and period. |

| 2 | Specialist estimate | A domain agent produces a bounded risk index and Evidence Passport. |

| 3 | Construct-validity gate | Check operational definition, measurement logic, data quality, bias, assumptions, and replicability. |

| 4 | Independent challenge | Attempt to falsify the estimate using alternative hypotheses, source checks, and benchmark logic. |

| 5 | Human Gate | Approve, modify, reject, or escalate. Any override requires a documented rationale. |

| 6 | Risk decomposition | Map approved evidence into IR, CR, or DR and preserve AR = IR × CR × DR as the structural spine. |

| 7 | Export | Write the full decision history to JSON/workpaper format with no hidden state transitions. |

The initial heuristic code should not be used to make professional audit decisions. In particular, fixed dollar thresholds and signed-balance aggregation are pedagogical shortcuts. A scientific implementation must use reconciled populations, absolute-value or assertion-appropriate exposure measures, entity-specific materiality/performance materiality, temporal holdouts, and documented exception handling. Confidence values must be calibrated against external outcomes before they are interpreted probabilistically.

## Online Appendix E. Validation Roadmap from Prototype to Field Study

The roadmap below converts the product-oriented development plan into a research-validity sequence appropriate for a Management Science project. Commercial pricing, regulator acceptance, and claimed time savings are treated as future managerial outcomes rather than assumed facts.

| Phase | Objective | Core activities | Scientific gate |

| --- | --- | --- | --- |

| Phase 1 | POC freeze and reproducibility | Freeze schemas, agent interfaces, prompts/rules, evidence-state transitions, and a development-case registry. | Executable replay; deterministic formulas; no unsupported PASS states. |

| Phase 2 | Fresh benchmark construction | Build temporally held-out SEC/XBRL, CAM, ICFR, AAER/enforcement, filing-delay, cyber-disclosure, and ESG cases. | Independent fixture authorship; firm/industry/time holdouts; leakage audit. |

| Phase 3 | Architecture experiment | Compare generalist LLM, specialists, provenance, challenger, and Human Gate under a common information set. | PR-AUC/Brier/Recall@k; unsupported-claim rate; correction vs new-error rate; latency/cost. |

| Phase 4 | Human-review experiment | Randomize professional or advanced participants to human-only, AI-only, and evidence-governed human+AI conditions. | Accuracy, calibration, override quality, review time, evidence traceability, cognitive load. |

| Phase 5 | Field pilot and external replication | Deploy on bounded non-production or retrospective cases with independent replication. | Out-of-sample stability, cross-model robustness, auditability, and regulator/audit-partner feedback. |

## Online Appendix F. Claims Discipline for the Startup and the Paper

| Claim class | Treatment |

| --- | --- |

| Research claim permitted now | The architecture is executable; it preserves provenance; it supports explicit challenge and human approval; the Microsoft case demonstrates orchestration and formula integrity. |

| Research claim requiring benchmark evidence | Specialists outperform a generalist model; CHALLENGER reduces false negatives; evidence passports improve calibration; Human Gate lowers expected loss. |

| Production claim requiring field evidence | 20-30% time savings; professional-grade risk estimates; stable performance across engagements; production reliability. |

| Regulatory claim not assumed | PCAOB or another regulator “accepts,” “certifies,” or “recognizes” agent-generated evidence. Such recognition is an external institutional outcome and cannot be a current success metric. |

| Startup moat hypothesis | The durable asset is the evidence/risk graph, applicability ontology, longitudinal labels, falsification protocols, calibration data, and human-approval audit trail—not a particular foundation model. |