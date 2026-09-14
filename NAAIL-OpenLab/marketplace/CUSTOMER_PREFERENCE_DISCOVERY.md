# NAAIL Discovery™ — Customer Preference Feed

**Platform:** NAAIL™ Marketplace Edition / NAAIL OpenLab™  
**Status:** Product-design specification — not yet an executable recommendation engine  
**Design inspiration:** short-card discovery and preference-feedback patterns used by modern consumer platforms. This is an independent NAAIL design and does not copy, reproduce, or claim affiliation with TikTok or any other platform.

> **Complex intelligence underneath. Simple professional discovery on top.**

## Purpose

NAAIL Discovery™ is the personalized customer-experience layer for NAAIL. Instead of asking users to choose among many agents, models, standards, tools, and research modules, NAAIL presents a short sequence of relevant professional cards based on the user's declared role, selected interests, current projects, interaction history, and explicit feedback.

The objective is not entertainment engagement. The objective is **professional relevance, evidence quality, learning value, and decision usefulness**.

## Core experience

```text
Open NAAIL
    ↓
Select role + interests
    ↓
Personalized professional feed
    ↓
One problem / opportunity per card
    ↓
ASK | ANALYZE | SIMULATE | EVIDENCE | SAVE
    ↓
USEFUL | NOT RELEVANT | WHY RECOMMENDED?
    ↓
Preference profile updates
    ↓
Next better-matched professional card
```

## Customer roles

### Student
Recommended content may include:
- audit simulations;
- IFRS problems;
- CAM/KAM cases;
- ICFR control cases;
- CPA-style questions;
- AI-versus-human judgment exercises;
- Big Four-style synthetic professional scenarios.

### Auditor / assurance professional
Recommended content may include:
- audit risks;
- CAM/KAM candidates;
- evidence gaps;
- control deficiencies;
- IFRS / SEC / PCAOB issues;
- unusual transactions;
- professional-review challenges.

### Researcher / professor
Recommended content may include:
- FT50 / AJG research opportunities;
- competing hypotheses;
- datasets;
- replication packages;
- causal-identification problems;
- model-comparison opportunities;
- robustness and falsification tasks.

### CFO / controller
Recommended content may include:
- reporting risks;
- disclosure issues;
- ICFR weaknesses;
- ESG / sustainability questions;
- unusual financial patterns;
- evidence-supported scenarios;
- governance and control alerts.

### Finance / economics user
Recommended content may include:
- SEC / XBRL signals;
- valuation questions;
- asset-pricing research;
- Fama–French evidence;
- scenario analysis;
- economic-data anomalies;
- ECONOVA-S™ research opportunities.

## Professional card design

Each card should contain one clear professional object.

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TODAY'S AUDIT CASE

XYZ Manufacturing — Revenue Cut-off

Risk score:       84 / 100
Evidence quality: 91 / 100
CAM probability:  76 / 100

KIWI™ signals
• Year-end revenue concentration
• Cut-off exception
• Management-estimate exposure

[ ANALYZE ] [ SIMULATE ] [ EVIDENCE ]
[ SAVE ] [ USEFUL ] [ NOT RELEVANT ]
[ WHY RECOMMENDED? ]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

GitHub documentation cards are static design examples only. A production interface would require a separate application layer.

## Preference signals

NAAIL should distinguish between **explicit** and **implicit** preference signals.

### Explicit signals — highest authority

- selected role;
- selected discipline;
- selected industry;
- selected jurisdiction;
- selected research method;
- selected learning objective;
- Useful;
- Not relevant;
- Save;
- Follow topic;
- Hide topic;
- Reset preferences.

### Professional interaction signals

- ANALYZE;
- SIMULATE;
- VIEW EVIDENCE;
- ASK AGENT;
- EXPORT;
- COMPLETE CASE;
- REPLICATE;
- RUN ROBUSTNESS;
- HUMAN APPROVAL / MODIFY / REJECT.

These signals can improve ranking, but NAAIL should not assume that a click proves professional agreement or scientific validity.

## Why am I seeing this?

Every recommended professional card should support an explanation such as:

```text
Why recommended?

✓ Role: Audit Researcher
✓ Topic preference: CAM/KAM
✓ Current project: Audit quality
✓ Industry preference: Manufacturing
✓ Previously saved: Revenue-recognition case
✓ New evidence available: CAM / filing / control signal
```

NAAIL should expose the strongest recommendation drivers and allow the user to change them.

## Recommendation objective

NAAIL must not optimize purely for attention, session length, clicks, or engagement.

The ranking objective should combine professional value and safety:

```text
RecommendationScore =
    RoleFit
  + TopicFit
  + ProjectFit
  + EvidenceQuality
  + LearningValue
  + ProfessionalRelevance
  + Novelty
  + UserExplicitPreference
  - DuplicationPenalty
  - WeakEvidencePenalty
  - RightsRiskPenalty
  - SafetyRiskPenalty
  - FatiguePenalty
```

The exact production weighting remains a future implementation decision and should be benchmarked rather than asserted.

## Scientific recommendation rules

A research card must not be ranked higher merely because it is more likely to produce a statistically significant result.

```text
optimize_for_p_value = false
optimize_for_clicks_only = false
hide_null_results = false
agent_consensus_is_truth = false
```

Research recommendations should favor:
- construct validity;
- identification quality;
- data provenance;
- falsifiability;
- replication potential;
- external validity;
- theoretical relevance;
- evidence quality;
- methodological diversity.

## Discovery feed architecture

```text
Customer / Student / Researcher
              ↓
      Preference Profile
              ↓
  NAAIL Discovery Router™
              ↓
┌─────────────┼─────────────┐
│             │             │
KIWI™      POMELO™      ECONOVA-S™
│             │             │
Audit       Accounting      Finance
CAM/KAM     Assurance       Economics
ICFR        ESG             Data Economy
└─────────────┼─────────────┘
              ↓
      Evidence / Rights Gate
              ↓
      Recommendation Ranker
              ↓
     Explainability Layer
              ↓
        Professional Card
              ↓
 Useful / Not Relevant / Save / Simulate
              ↓
     Preference Update
```

## Role-based starter feeds

| Role | First feed priorities |
|---|---|
| Student | simulations, guided cases, learning challenges, feedback |
| Auditor | risk, evidence, CAM/KAM, ICFR, standards, review |
| Researcher | literature, hypotheses, datasets, replications, methods |
| CFO / Controller | reporting, controls, ESG, disclosure, scenarios |
| Finance / Economics | filings, valuation, asset pricing, economic evidence |

## User control

The user should be able to:
- change role;
- change topics;
- change industry;
- change jurisdiction;
- hide a topic;
- reset preference history;
- disable personalization;
- inspect why an item was recommended;
- switch to chronological / latest-evidence mode where appropriate.

## Privacy-by-design requirements

Preference data is potentially sensitive behavioral data. A production system should therefore require:

- clear consent and privacy disclosures;
- data minimization;
- role-based access;
- purpose limitation;
- retention rules;
- deletion / reset capability;
- separation between learning analytics and recruitment decisions;
- no sale of personal preference data;
- no hidden use of individual student performance for partner recruitment;
- audit logs for enterprise use;
- institution-specific governance where required.

## Education safeguard

For NAAIL University / Student Agent Academy:

```text
Student preference profile
        ≠
Recruitment profile
```

Student learning behavior, mistakes, case performance, and AI interaction history should not automatically become employer-selection data. Any such use would require explicit governance, consent, institutional approval, and a separate lawful purpose.

## Buyer / enterprise value

The preference layer gives NAAIL a simple customer front end while keeping the scientific architecture underneath.

### For universities
- personalized cases by course level;
- targeted remediation;
- recommended simulations;
- evidence-based learning progression.

### For audit / professional firms
- role-specific training;
- industry-specific cases;
- control / audit-risk updates;
- standards-aware learning feeds.

### For researchers
- personalized literature / dataset / replication opportunities;
- hypothesis and method recommendations;
- research-workflow continuation.

### For finance teams
- relevant filing, valuation, risk, and economic-analysis cards.

## Metrics for the preference system

A professional recommendation system should be evaluated with more than engagement.

Recommended measures:

- Relevant@K;
- Save@K;
- ProfessionalAction@K;
- EvidenceView@K;
- CaseCompletion@K;
- NotRelevant rate;
- duplicate-content rate;
- diversity / coverage;
- evidence-quality score;
- user override rate;
- explanation usefulness;
- learning improvement;
- professional-review acceptance;
- calibration by role / discipline;
- privacy / governance incidents.

## Marketplace positioning

NAAIL Discovery™ should be presented as:

> **A personalized professional-intelligence feed that learns what work is relevant to you while keeping evidence, explainability, and human control visible.**

It should not be presented as a TikTok integration, TikTok partnership, or reproduction of TikTok's proprietary recommendation algorithm.

## Implementation sequence

### Phase 1 — GitHub / static design
- role cards;
- sample professional feed;
- preference taxonomy;
- recommendation-governance rules;
- explainability examples;
- privacy requirements.

### Phase 2 — prototype
- explicit role / topic selection;
- static content ranking;
- Useful / Not relevant / Save actions;
- Why recommended? explanation;
- local preference store.

### Phase 3 — governed recommendation engine
- learned ranking;
- cross-product routing;
- evidence-aware scoring;
- diversity controls;
- evaluation dashboard;
- privacy / deletion controls;
- Human Gate for high-risk recommendations.

### Phase 4 — marketplace experience
- ChatGPT / agent surface;
- Gemini / Google Cloud surface;
- Microsoft Copilot / Marketplace surface;
- Claude / MCP evidence connector;
- institution / enterprise configuration.

## Relationship to NAAIL scientific governance

The discovery layer decides **what to show next**. It does not decide what is scientifically true.

Every material research or professional conclusion remains subject to:

**Literature Validation → Evidence / Rights Gate → Specialist Analysis → Adversarial Review → Robustness / Falsification → Replication where applicable → Chain-of-Evidence → Evidence Passport™ → Human Gate™**

## Current status

This document is a public product-design specification. It does not claim that the preference engine is already implemented, validated, deployed, or approved by any external marketplace.

## Principal Investigator

**Dr. Saeid Homayoun**  
ORCID: https://orcid.org/0000-0002-2536-0446

---

**Independent-project notice:** NAAIL™ / NAAIL OpenLab™ is an independent research initiative. TikTok and other third-party names are referenced only as public design inspiration or comparison context and do not imply affiliation, endorsement, sponsorship, authorization, technical integration, or access to proprietary algorithms.