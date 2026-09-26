# NAAIL Student Pilot 002 — Microsoft Agent Edition

**Status:** Planned executable milestone for the v0.2.4 target.  
**Current validated release remains:** NAAIL OpenLab v0.2.3 / Prototype 003.

## Purpose

Student Pilot 002 will connect the NAAIL Student Digital Twin to a real Microsoft-compatible agent surface while preserving the NAAIL evidence, evaluation, privacy, and Human Gate architecture.

The goal is to demonstrate a safe university–industry training environment in which students can practice AI-enabled audit judgment before entering professional practice without requiring an audit firm to disclose proprietary production systems, client data, prompts, methods, or confidential technology.

## Target architecture

```text
Microsoft 365 / Copilot-compatible Agent Surface
                 ↓
       NAAIL Adapter Boundary
                 ↓
      Educational Proxy Agent
                 ↓
 Synthetic Client XYZ Digital Twin
                 ↓
Student tests / challenges / documents AI advice
                 ↓
RPA + AA + EG + PS + DS + DIST
+ AIV + CER + HOR + ESC
                 ↓
     Professional Decision DAG™
                 ↓
             Human Gate
                 ↓
Student feedback + aggregate anonymized partner insight
```

## Initial cases

Pilot 002 should reuse the frozen Student Pilot 001 case family:

1. Revenue Recognition & Cut-off;
2. Goodwill Impairment;
3. ICFR / Control Deficiency.

Using the same evidence family enables controlled comparison between deterministic educational-proxy behavior and a real provider-backed agent condition.

## Required interfaces

### Student workspace
- case briefing;
- evidence inventory;
- agent recommendation;
- contradictory-evidence challenge;
- procedure design;
- accept / modify / reject / request-more-evidence / escalate decision states;
- rationale capture;
- Human Gate submission;
- formative feedback.

### Instructor workspace
- cohort progress;
- case completion;
- evidence-use patterns;
- professional-judgment metrics;
- AI-verification and skepticism metrics;
- common misconception analysis;
- intervention / review controls.

### Industry-partner view
Default partner reporting should be aggregate and anonymized, for example:
- cohort AI-readiness distribution;
- contradictory-evidence recognition;
- escalation behavior;
- common technical weaknesses;
- time-to-completion;
- learning gains across cases.

Individual student identities or scores must not be disclosed to a partner by default. Any optional recruitment pathway requires explicit student consent, institutional approval, appropriate privacy documentation, and separation from academic grading.

## Evaluation framework

Professional judgment:
- **RPA** — Risk–Procedure Alignment;
- **AA** — Assertion Alignment;
- **EG** — Evidence Grounding;
- **PS** — Professional Skepticism;
- **DS** — Documentation Sufficiency;
- **DIST** — Decision Integrity / Stability.

Human–AI readiness:
- **AIV** — AI Verification;
- **CER** — Contradictory Evidence Recognition;
- **HOR** — Human Override Reasoning;
- **ESC** — Escalation Judgment.

These scores are educational/research constructs and must not be represented as validated employment-selection instruments without separate psychometric, legal, fairness, and institutional validation.

## Release gates

Pilot 002 is not complete until:

- a real Microsoft-compatible provider/agent adapter is configured;
- provider/model identity and version are logged;
- frozen evidence is preserved;
- no confidential client or firm data are used;
- privacy/consent controls are approved for the pilot context;
- student and instructor workflows are tested;
- partner reporting is anonymized by default;
- regression/evaluation tests pass;
- Human Gate remains mandatory;
- results clearly distinguish deterministic, provider-backed, and human-reviewed conditions;
- no Microsoft or Big Four endorsement is implied without written authorization.

## Partnership model

An industry partner may contribute an approved challenge brief, educational learning objectives, guest teaching, synthetic case requirements, or an educational proxy-agent specification. NAAIL translates this into a governed simulation rather than reproducing the firm's production audit system.

## Non-claims

This roadmap does not state that Microsoft, Deloitte, EY, KPMG, PwC, or any other firm has partnered with, approved, certified, sponsored, or endorsed NAAIL OpenLab. Firm and Microsoft names may be used only to describe intended interoperability, target audiences, or potential partnership models until formal authorization exists.
