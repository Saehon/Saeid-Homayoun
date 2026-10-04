**Saeid Homayoun**  
University of Gävle, Sweden  
Working manuscript for Management Science  
October 2026

**Research status note**: Pre-results conceptual and empirical-design manuscript. No unexecuted experiment, model comparison, customer validation, or prototype output is reported as a finding.

**Keywords:** generative AI; multi-agent systems; assurance; human-AI collaboration; internal control; auditing; financial risk; evidence governance

# ABSTRACT

Generative artificial intelligence is moving from advisory chat interfaces toward agentic systems that retrieve evidence, invoke tools, generate analyses, and recommend actions in high-stakes professional work. This transition creates a second-order assurance problem: organizations must evaluate not only the underlying financial process, but also the AI agents that interpret evidence and influence decisions. We develop a theory of evidence-governed multi-agent decision systems and propose a research artifact for financial reporting and assurance. The architecture separates task orchestration, domain-risk analysis, evidence verification, adversarial challenge, assurance review, and human approval. Building on Management Science research on formal control, financial-reporting fragility, monitoring overload, AI-enabled audit quality, generative-LLM construct validity, human-centered AI, and multilayer decision authority, we argue that value arises from the design of the decision architecture rather than model capability alone. We define AI-agent assurance as an independent evaluation of an agent's evidence, reasoning trace, model/version, disagreement, and escalation decision before human authorization. We propose two preregistered studies. Study 1 compares conventional work, single-model generative AI, ungoverned multi-agent AI, and evidence-governed multi-agent AI in a controlled revenue-recognition and internal-control task. Study 2 evaluates the architecture in point-in-time prediction of future internal-control failure using public financial-reporting evidence. The design tests decision quality, unsupported-claim rates, calibration, contradictory-evidence use, review effort, abstention, and the predictive value of agent disagreement. The framework offers a general theory and testable design for governing increasingly autonomous AI in professional decision systems.

# 1. Introduction

Organizations are rapidly moving beyond conversational AI toward systems in which multiple AI agents retrieve data, invoke analytical tools, exchange intermediate conclusions, and recommend actions. This shift changes the managerial problem. The central question is no longer only whether an algorithm can perform a professional task. It is whether an organization can design a decision system in which autonomous or semi-autonomous agents remain evidence-grounded, mutually checkable, and accountable to human authority.

The problem is particularly acute in financial reporting, internal control, audit, and assurance. These settings combine noisy data, incomplete documentation, sequential judgments, regulatory constraints, asymmetric losses from false positives and false negatives, and explicit professional accountability. A model can be statistically capable yet operationally unsafe if its output cannot be traced to evidence, if it fails silently when sources conflict, or if several agents reproduce the same unsupported premise. The resulting governance problem is second order: the organization must assure the agents that are themselves performing assurance-related work.

Recent Management Science research provides the components of this problem but not yet an integrated solution. Penno (2021) formalizes the relationship between costly formal control and tone at the top, establishing that assurance design requires an allocation of control rather than a binary choice between trust and verification. Kim et al. (2022) show that weak financial-reporting environments manifest through multiple observable outcomes, including internal-control weaknesses, restatements, untimely filings, amendments, and extended regulatory scrutiny. deHaan et al. (2023) treat the reporting process as a system that can be stress tested for resilience. Ashraf et al. (2024) show that monitoring capacity is finite: adding noncore oversight responsibilities can impair financial-reporting oversight. Together, these studies imply that risk intelligence must be process-aware, multi-signal, and selective in how it allocates scarce human attention.

The AI literature then changes the design frontier. Law and Shen (2024) document that audit offices using AI exhibit more accurate going-concern and internal-control opinions, while their evidence is inconsistent with a simple replacement view of auditors. de Kok (2025) shows the potential of generative large language models for accounting textual analysis while emphasizing model selection, construct validity, bias, replicability, and data-sharing concerns. Krakowski et al. (2025) demonstrate in a field experiment that human-centered design of AI interaction matters for performance. Zhong (2025) provides the closest formal analogue to the problem studied here: in multilayer decision systems, each layer can correct prior errors but can also introduce new ones, making the sequencing of decision makers and the location of final authority central design choices.

We integrate these streams into a theory of evidence-governed multi-agent systems. Our core construct is AI-agent assurance: an independent process that evaluates an agent's evidence provenance, decision trace, model and version, contradictory evidence, cross-agent disagreement, and escalation status before a high-stakes recommendation is authorized. This construct is distinct from model validation, which evaluates predictive performance of a model, and from financial-statement assurance, which evaluates an underlying reporting assertion. Agent assurance instead evaluates the reliability of the AI-enabled decision process itself.

We develop and propose to test this architecture in the context of internal control over financial reporting (ICFR). The research artifact, NAAIL/LEMON, is provider-neutral: the foundation model can be Claude, GPT, Gemini, an open-weight model, or a conventional statistical model. The durable design elements are separation of duties, evidence provenance, adversarial challenge, explicit uncertainty, abstention, reproducibility, and human approval. This distinction is important because foundation models are replaceable technologies, whereas the governance architecture and accumulated failure evidence can become organizational capabilities.

The paper makes four contributions. First, it extends the human-algorithm literature from dyadic interaction to governed multi-agent architectures. Second, it identifies evidence governance as a design variable distinct from raw model capability. Third, it develops testable predictions about disagreement, challenge, abstention, and human-review allocation in multilayer AI systems. Fourth, it connects the design of AI agents to the economics of assurance and monitoring capacity in a high-stakes professional setting.

## Table 1. Scientific foundation and the resulting design problem

| **Study**               | **Core insight used here**                                                                                        | **Design implication**                                                                                | **Role in theory**    |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-----------------------|
| Penno (2021)            | Formal control and tone at the top can be complements or substitutes.                                             | Assurance is an allocation problem, not blind automation.                                             | Control foundation    |
| Kim et al. (2022)       | Reporting failure is multi-indicator: ICFR weaknesses, restatements, timeliness, amendments, regulatory scrutiny. | Use multiple risk signals; avoid one opaque label.                                                    | Risk observability    |
| deHaan et al. (2023)    | Financial-reporting processes can be stress tested for resilience.                                                | Treat reporting as a process whose fragility can be monitored over time.                              | Process resilience    |
| Ashraf et al. (2024)    | Monitoring capacity can be overloaded; core ICFR oversight improves reporting quality.                            | Prioritize review and route scarce human attention.                                                   | Attention constraint  |
| Law & Shen (2024)       | AI use in audit offices is associated with more accurate going-concern and internal-control opinions.             | AI can augment professional judgment; replacement is not the only pathway.                            | AI value              |
| de Kok (2025)           | GLLMs expand accounting text analysis but require construct-valid, reproducible use.                              | Evidence, construct definitions, replication, and model/version control are first-class requirements. | LLM governance        |
| Krakowski et al. (2025) | Human-centered configuration of AI interaction affects performance.                                               | Interface and allocation of work should be designed around complementary strengths.                   | Human-AI augmentation |
| Zhong (2025)            | Each decision layer can correct errors and introduce new ones; final authority matters.                           | Sequence specialist, challenger, reviewer, and human layers deliberately.                             | Multilayer authority  |

# 2. Theory: From Assurance to Second-Order Agent Assurance

## 2.1 Formal control, reporting risk, and process resilience

Assurance systems exist because decision makers cannot costlessly observe all actions, evidence, and risks. Penno (2021) shows that formal controls and informal tone can either complement or substitute for one another depending on the environment. The broader implication for AI-enabled professional work is that autonomy and control should be jointly designed. Adding an AI agent does not remove the need for control; it changes where control is economically valuable.

Financial-reporting risk is also not a single latent condition revealed by one variable. Kim et al. (2022) show that poor reporting quality can appear through multiple observable channels. deHaan et al. (2023) further show that reporting processes can be analyzed as resilient or fragile systems under stress. These ideas motivate an evidence architecture in which the state of the firm is inferred from a portfolio of time-stamped signals, rather than from a single model score or narrative conclusion.

This process view matters because agentic AI can propagate an error across tasks. A weak source identification can contaminate an accounting classification, which can contaminate a risk score, which can influence a reviewer. The relevant unit of governance is therefore not only the model but also the path by which evidence becomes a decision.

## 2.2 Monitoring capacity and risk-based allocation of human attention

Evidence governance has a cost. Additional reviewers, challenge steps, and documentation can improve reliability but consume time and attention. Ashraf et al. (2024) provide direct evidence that monitoring responsibilities can overload audit committees and impair financial-reporting oversight when responsibilities expand beyond core duties. This result suggests that a safe AI architecture cannot simply add more review to every decision. It must allocate review intensity according to risk, disagreement, evidence quality, and expected loss.

Accordingly, the architecture includes abstention and escalation rather than a requirement that the AI always answer. Low-risk, well-supported tasks can pass through a light review path; high-risk or high-disagreement cases are routed to stronger challenge and human review. This creates a quality-efficiency frontier rather than assuming that maximal review is universally optimal.

## 2.3 AI augmentation, construct validity, and multilayer authority

Law and Shen (2024) suggest that AI can improve audit outcomes while changing the skill mix of professional work. The finding is important because it rejects a narrow automation framing. The relevant managerial choice is not simply human versus AI, but how AI changes the distribution of tasks, review, and judgment.

de Kok (2025) highlights a complementary challenge: a generative model can perform sophisticated accounting text tasks, but useful deployment requires construct validity, model selection, bias control, replicability, and data governance. In an agentic system, these concerns multiply because one agent's output becomes another agent's input. The architecture must therefore preserve source and model lineage across agents.

Krakowski et al. (2025) show that human-centered design affects realized performance from AI assistance. Zhong (2025) formalizes why this should matter in multilayer settings: a later decision maker can correct a previous error but can also introduce a new error. These insights motivate a separation-of-duties architecture in which different agents have bounded roles and where the last computational layer is not presumed to have unrestricted authority.

## 2.4 A simple model of error propagation

Let q_l denote the probability that the current recommendation is wrong after layer l. A new layer can correct an existing error with probability c_l and can introduce a new error into an otherwise correct recommendation with probability e_l. The post-layer error rate is:

**q_l = q\_{l-1}(1 - c_l) + (1 - q\_{l-1})e_l**

This expression captures the central trade-off. More layers are not automatically better. A layer creates value when its correction probability is sufficiently high relative to the new errors and costs it introduces. Evidence governance changes these parameters. Provenance and deterministic recomputation are expected to reduce e_l; an independent challenger is expected to increase c_l when the current recommendation conflicts with available evidence; and abstention prevents a low-quality layer from forcing a decision when its expected contribution is negative.

For a professional decision with asymmetric losses, expected organizational loss can be written as L = C_FN·P(FN) + C_FP·P(FP) + λT + μU, where C_FN and C_FP are the costs of false-negative and false-positive decisions, T is review time, and U is the incidence or severity of unsupported claims. An evidence-governed architecture is valuable if it lowers expected loss, not merely if it maximizes raw accuracy.

# 3. Hypotheses

**H1. Architecture effect.** Evidence-governed multi-agent assistance will produce higher professional decision quality than single-model generative-AI assistance.

**H2. Evidence-governance effect.** Relative to multi-agent assistance without explicit governance, evidence provenance, verification, and model/version traceability will reduce unsupported claims and improve confidence calibration.

**H3. Challenger effect.** An independent challenger/falsifier will increase the use of decision-relevant contradictory evidence and reduce error propagation, with a larger benefit when task complexity and evidence conflict are high.

**H4. Disagreement signal.** Cross-agent disagreement will positively predict decision error and therefore identify cases in which human review has higher expected value.

**H5. Risk-based review allocation.** Routing human review toward high-risk, high-disagreement, or low-evidence cases will improve the joint quality-efficiency frontier relative to uniform review.

**H6. Human authority and abstention.** A system that can abstain and route unresolved cases to a human gate will have lower expected decision loss than a system required to issue a recommendation on every case.

# 4. Research Artifact: NAAIL/LEMON as an Evidence-Governed Multi-Agent System

The research artifact is designed as a provider-neutral multi-agent system. NAAIL denotes the common assurance and governance layer; LEMON denotes the first domain implementation for ICFR and financial-reporting risk intelligence. The architecture is intentionally modular so that the model provider can change without changing the scientific test of governance mechanisms.

The system separates six functions. The Orchestrator decomposes the task and records the execution path. The ICFR/Risk Agent evaluates structured and textual risk signals but is prohibited from independently declaring a material weakness. The Evidence Agent links each material claim to source documents, dates, transformations, and calculations. The Challenger/Falsifier searches for contradictory facts, alternative explanations, leakage, and unsupported assumptions. The Assurance Reviewer integrates the primary analysis and challenge, decides whether the case is verified, inferred, or unresolved, and determines whether escalation is required. The Human Approval Gate retains final authority for high-stakes actions.

Across these functions, the Evidence Passport records source, observation date, information cutoff, model/version, calculation, agent, supporting evidence, contradictory evidence, confidence, status, and final human disposition. A Failure Memory records recurring error patterns and the conditions under which they occur. These records turn agent failures from ephemeral chat events into analyzable organizational data.

<img src="media/image1.png" style="width:6.8in;height:2.68414in" />

Figure 1. Evidence-governed multi-agent decision architecture. The architecture separates risk analysis, evidence verification, challenge, assurance review, and final human authority.

## 4.1 Why this is not simply a multi-agent chatbot

The theoretical treatment is functional rather than anthropomorphic. An 'agent' is a bounded decision function with specified inputs, allowed tools, outputs, and escalation rules. Some agents may be deterministic software rather than generative models. This is essential because using more LLM calls is not itself a governance mechanism.

Three design choices distinguish the artifact from generic orchestration. First, the Challenger is independent of the primary analyst and is rewarded for identifying failure rather than consensus. Second, the Assurance Reviewer receives both supporting and contradictory evidence. Third, the Human Gate receives an explicit unresolved-items list rather than only a synthesized recommendation.

# 5. Empirical Design

## 5.1 Study 1: Controlled professional-decision experiment

Study 1 is a preregistered 4 × 2 between-participants experiment. The first factor varies decision architecture: (1) conventional digital workpapers with no generative AI; (2) a single general-purpose generative-AI assistant; (3) specialized multi-agent assistance without independent challenge, provenance requirements, or an explicit human gate; and (4) the full evidence-governed architecture. The second factor varies case complexity and evidence conflict (lower versus higher).

The experimental task concerns year-end revenue recognition, cutoff, and related internal-control implications. Participants inspect an ERP-grounded evidence package containing sales orders, invoices, delivery records, cash receipts, accounts-receivable aging, inventory movements, journal entries, general-ledger balances, contract terms, and financial-statement extracts. The case is constructed so that several explanations remain plausible until participants integrate contradictory evidence. Ground truth is fixed ex ante by the case design and is not generated by the AI system.

The preferred participant pool is practicing auditors, internal auditors, controllers, or experienced accounting professionals. If professional recruitment constrains sample size, the design will use a preregistered two-sample strategy in which professionals provide the primary confirmatory sample and advanced accounting participants provide a replication sample. The current planning value is approximately 320 participants, but the final sample will be determined by simulation-based power analysis before data collection.

## Table 2. Experimental conditions

| **Condition**        | **AI support**                                 | **Specialization** | **Challenge / verification**                                 | **Human gate**                                |
|----------------------|------------------------------------------------|--------------------|--------------------------------------------------------------|-----------------------------------------------|
| C1 Conventional      | None                                           | No                 | Conventional workpaper review                                | Professional decision                         |
| C2 Single AI         | One general-purpose GAI assistant              | No                 | No independent challenge                                     | Professional may override                     |
| C3 Multi-agent       | Orchestrator + specialist agents               | Yes                | No independent challenger or evidence passport               | Professional may override                     |
| C4 Evidence-governed | Specialists + evidence + challenger + reviewer | Yes                | Independent challenge, provenance, recomputation, abstention | Explicit approval / request evidence / reject |

## 5.2 Measures

| **Construct / measure**    | **Operationalization**                                                                                              |
|----------------------------|---------------------------------------------------------------------------------------------------------------------|
| Decision quality           | Distance from preregistered ground truth; correctness of identified accounting/control issue; severity calibration. |
| Unsupported-claim rate     | Proportion of material statements not traceable to evidence available before the decision cutoff.                   |
| Contradictory-evidence use | Whether and how participants/agents incorporate evidence inconsistent with the leading explanation.                 |
| Confidence calibration     | Brier-style calibration between expressed confidence and correctness.                                               |
| Appropriate reliance       | Extent to which humans accept correct AI recommendations and reject incorrect ones.                                 |
| Review effort              | Elapsed time, evidence items inspected, revisits, and number of escalations.                                        |
| Human override quality     | Whether overrides improve or worsen the recommendation relative to the pre-override state.                          |
| Disagreement               | Pairwise and aggregate divergence across agents/models before the reviewer stage.                                   |
| Evidence completeness      | Share of required decision-relevant evidence represented in the Evidence Passport.                                  |

## 5.3 Study 2: Point-in-time ICFR risk validation

Study 2 evaluates external validity using a longitudinal public-data setting. The outcome is future ICFR failure or a closely defined ineffective-control outcome, with all predictors frozen at a firm-specific information cutoff. The data architecture uses rights-cleared public SEC filings and structured XBRL/CompanyFacts information, together with historical ICFR disclosures and other sources only when their rights and timing are defensible.

The design compares four model families: M1, executable published-science models; M2, conventional machine learning; M3, foundation-model/agent predictions; and M4, a hybrid in which machine learning estimates residual structure after the published-science component is executed. The purpose is not to presume that journal-published models are transportable. Every model must pass variable-definition, estimand, timing, and out-of-sample gates before comparison.

Primary predictive metrics are PR-AUC, Brier score, calibration slope/intercept, recall at a fixed review budget, false-positive burden, and stability across time. Operational metrics are inference cost, human validation time, evidence completeness, and abstention frequency. Crucially, Study 2 also tests whether governance variables that are not conventional predictors—agent disagreement, challenger findings, evidence gaps, and provenance failures—predict model error and therefore improve routing to human review.

The holdout is temporal rather than random. Feature construction must use only information publicly available by the firm-specific cutoff. No realized future financials, later restatements, later ICFR conclusions, or post-cutoff explanatory text may enter features. Any detector tuning informed by a known falsification probe must be evaluated on fresh, independently authored probes before being described as improved validation performance.

## 5.4 Analysis plan and falsification logic

Study 1 will estimate planned contrasts among the four architecture conditions and interactions with complexity. The primary contrast compares C4 with C2; a second contrast compares C4 with C3 to isolate governance from specialization. Mediation analyses will test whether contradictory-evidence use and unsupported-claim reduction explain improvements in decision quality. We will report effect sizes and uncertainty rather than relying only on statistical significance.

Study 2 will use out-of-time evaluation and calibration analysis. Model selection and threshold selection will be performed without access to the locked holdout. We will separately test whether disagreement and evidence-quality signals add incremental information about model error after controlling for the underlying risk score.

The design is explicitly falsifiable. Evidence-governed multi-agent systems would fail to support the theory if they do not improve expected decision loss relative to simpler alternatives, if the Challenger mainly introduces noise, if disagreement fails to identify elevated error risk, or if review costs dominate quality gains. Such results would imply that the architecture should be narrowed rather than expanded.

# 6. Expected Contributions to Management Science

**Architecture rather than model comparison.** Most human-AI studies compare a human with an algorithm or examine reliance on one model. We study a governed system of differentiated computational and human roles.

**Second-order assurance as a new design construct.** The paper distinguishes assurance over an underlying business assertion from assurance over the AI decision process that evaluates that assertion.

**Evidence governance as an endogenous source of value.** The architecture treats provenance, contradiction, recomputation, and abstention as mechanisms that can change error propagation, not merely as compliance documentation.

**Monitoring capacity and routing.** The framework links AI governance to scarce human attention. The objective is not maximum review but optimal review intensity conditional on risk and disagreement.

**Error disagreement as a decision signal.** The paper tests whether disagreement among agents is itself informative about when human intervention creates value.

**A high-stakes testbed with objective evidence.** Financial reporting and ICFR provide unusually clear requirements for point-in-time evidence, traceability, and asymmetric error costs, making them a strong setting for general theories of professional AI governance.

# 7. Managerial and Entrepreneurial Implications

The managerial implication is that organizations should not ask only which foundation model is best. They should ask which decisions require specialization, what evidence must be preserved, when a challenger should be invoked, which disagreements warrant escalation, and who retains final authority. This changes procurement and system design from model acquisition to decision-architecture design.

For AI providers and professional-service firms, the framework suggests a distinct product category: independent agent assurance. An assurance layer can remain model-provider neutral and evaluate outputs from multiple foundation models, enterprise agents, or deterministic systems using the same evidence and governance contract. Its defensibility would come less from prompts than from domain ontologies, benchmark cases, evidence lineage, failure memory, cross-model disagreement histories, and human correction outcomes.

The research artifact translates this logic into a staged commercialization path. LEMON-ICFR is the first specialist implementation because ICFR has observable risk outcomes, public regulatory evidence, and a direct need for prioritized human review. CAM/KAM, PCAOB-style inspection readiness, forensic/AAER, IFRS judgment, ESG assurance, and cybersecurity can later become modules if they pass separate scientific and market validation. The research design therefore treats the startup as an empirical vehicle, not as evidence of scientific validity.

# 8. Boundary Conditions and Risks

First, multi-agent systems can create correlated rather than independent errors because agents may share training data, retrieval sources, prompts, or upstream assumptions. Apparent consensus is therefore not evidence of independence. The design must record model family and evidence overlap.

Second, an independent challenger can create false conflict and increase review burden. Its contribution is conditional on its ability to discover genuinely decision-relevant counterevidence. Third, the human gate can become ceremonial if professionals routinely approve AI recommendations without inspection. Appropriate reliance must therefore be measured behaviorally rather than inferred from the presence of a button.

Fourth, public-data ICFR prediction does not equal audit assurance. A risk score can prioritize review but cannot independently establish a material weakness, compliance failure, or audit opinion. Fifth, model drift and regulatory change mean that performance and rule mappings require versioning and periodic revalidation. Finally, the theory may not generalize to low-stakes domains where the costs of provenance, challenge, and human review exceed expected error losses.

# 9. Conclusion

The move from AI assistants to AI agents changes the locus of governance. When agents gather evidence, invoke tools, generate hypotheses, and pass conclusions to one another, assurance can no longer focus only on a final model output. It must address the architecture through which evidence becomes action.

This paper proposes evidence-governed multi-agent systems as a testable response to that problem. The framework integrates formal control, process resilience, monitoring capacity, AI-enabled professional judgment, construct-valid use of generative models, human-centered design, and multilayer decision authority. Its central prediction is deliberately conditional: more agents are not necessarily better. Value arises when specialization, evidence governance, challenge, abstention, and human authority reduce expected decision loss by more than they increase coordination and review costs.

The resulting research question is therefore broader than auditing: as organizations delegate more professional work to autonomous systems, who assures the agents themselves? The answer is unlikely to be another unconstrained agent. It is a governed decision architecture in which evidence, dissent, verification, and accountable authority are designed together.

# References

Ashraf, M., Choudhary, P., & Jaggi, J. (2024). Are Audit Committees Overloaded? Evidence from the Effect of Financial Risk Management Oversight on Financial Reporting Quality. Management Science, 70(12), 8414-8447. https://doi.org/10.1287/mnsc.2022.00360

deHaan, E., de Kok, T., Matsumoto, D., & Rodriguez-Vazquez, E. (2023). How Resilient Are Firms' Financial Reporting Processes? Management Science, 69(4), 2536-2545. https://doi.org/10.1287/mnsc.2023.4670

de Kok, T. (2025). ChatGPT for Textual Analysis? How to Use Generative LLMs in Accounting Research. Management Science, 71(9), 7888-7906. https://doi.org/10.1287/mnsc.2023.03253

Kim, J., Park, S., Peterson, K., & Ryan, W. (2022). Not Ready for Prime Time: Financial Reporting Quality After SPAC Mergers. Management Science, 68(9), 7054-7064. https://doi.org/10.1287/mnsc.2022.4478

Krakowski, S., Haftor, D., Luger, J., Pashkevich, N., & Raisch, S. (2025). Human-Centered Artificial Intelligence: A Field Experiment. Management Science, 72(1), 57-72. https://doi.org/10.1287/mnsc.2022.03849

Law, K. K. F., & Shen, M. (2024). How Does Artificial Intelligence Shape Audit Firms? Management Science, 71(5), 3641-3666. https://doi.org/10.1287/mnsc.2022.04040

Penno, M. (2021). A Theory of Assurance: Balancing Costly Formal Control with Tone at the Top. Management Science, 68(1), 654-668. https://doi.org/10.1287/mnsc.2020.3861

Zhong, H. (2025). Optimal Integration: Human, Machine, and Generative AI. Management Science, 72(5), 3720-3739. https://doi.org/10.1287/mnsc.2024.07401

# Appendix A. Agent Roles and Governance Contract

| **Role**             | **Function**                                                                           | **Hard boundary**                                                                |
|----------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Orchestrator         | Decompose task; assign bounded roles; preserve execution trace.                        | May not silently suppress unresolved objections.                                 |
| ICFR/Risk Agent      | Estimate risk and identify drivers using point-in-time evidence.                       | May not declare a material weakness or audit opinion.                            |
| Evidence Agent       | Map material claims to sources, dates, calculations, and rights status.                | May not convert missing evidence into inferred support.                          |
| Challenger/Falsifier | Search for contradictions, alternative explanations, leakage, and brittle assumptions. | Must report both successful and unsuccessful challenges.                         |
| Assurance Reviewer   | Integrate primary and challenger outputs; classify VERIFIED / INFERRED / UNRESOLVED.   | Must preserve material disagreement.                                             |
| Human Gate           | Approve, request more evidence, modify, or reject.                                     | Final authority for high-stakes action remains accountable to a qualified human. |

# Appendix B. Pre-Results Integrity Rules

1\. No model or agent receives information dated after the decision cutoff in historical prediction tests.

2\. No benchmark probe is reused as an independent test after the system has been modified in response to that probe.

3\. Model agreement is not coded as independent verification when agents share the same source, model family, or upstream premise.

4\. A prototype execution is not treated as evidence of scientific validity or product-market fit.

5\. Performance claims are reported only after preregistered evaluation on a locked holdout or independent replication set.

6\. Regulatory, accounting, and audit conclusions remain bounded by applicable professional authority and human judgment.