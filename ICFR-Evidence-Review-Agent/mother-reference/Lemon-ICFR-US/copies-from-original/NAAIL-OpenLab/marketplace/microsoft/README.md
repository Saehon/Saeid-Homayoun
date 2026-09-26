# Microsoft Distribution Package

**Target surfaces:** Microsoft Marketplace and Microsoft 365 Copilot  
**Recommended offer model:** centrally hosted SaaS agent with Microsoft 365/Copilot distribution where appropriate  
**Status:** Public scaffold only; not submitted or approved.

## Recommended NAAIL offer

**Name:** NAAIL OpenLab™ Research Intelligence Agent

**Primary job:** Deliver governed research workflows inside Microsoft environments while preserving evidence provenance, reproducibility, privacy, and mandatory Human Gate controls.

A second education-facing product path is now defined as **NAAIL Student Pilot 002 — Microsoft Agent Edition**, connecting a Microsoft-compatible agent surface to the NAAIL Student Digital Twin for accounting/audit education, AI-readiness training, and privacy-governed university–industry collaboration.

See: **[Student Pilot 002 — Microsoft Agent Edition](../../Student_Pilot_002_Microsoft/README.md)**.

## Recommended distribution model

Microsoft currently supports AI Apps and Agents in Marketplace and provides paths for Azure agents as well as Microsoft 365/Copilot agents. For NAAIL, a centrally hosted multitenant SaaS model is the preferred starting point because it preserves one controlled NAAIL core and lets the distribution layer integrate with Microsoft 365/Copilot without exposing proprietary orchestration.

## Initial Microsoft surfaces

- Microsoft Marketplace listing;
- Microsoft 365 Copilot agent surface;
- Teams as a research-workspace and student-learning channel where appropriate;
- optional Word/Excel integration for governed research artifacts, case documentation, and analysis workflows;
- optional instructor/cohort dashboard linked to NAAIL Student Learning Twin data;
- optional anonymized industry-partner dashboard for aggregate pilot insights.

## Student Agent Academy use case

The Microsoft route should support a safe education architecture rather than attempting to reproduce a Big Four production audit platform.

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
```

The first Microsoft student pilot should reuse the same frozen synthetic cases as Student Pilot 001: Revenue Recognition & Cut-off, Goodwill Impairment, and ICFR / Control Deficiency. This allows transparent comparison between deterministic educational-proxy behavior and a real provider-backed agent condition.

## Required production components

- Partner Center enrollment in applicable Microsoft programs;
- production SaaS endpoint;
- identity/authentication integration;
- Microsoft 365/Copilot app or agent package/manifest where required;
- marketplace listing metadata;
- privacy policy and support URL;
- fulfillment/billing integration if a transactable SaaS offer is used;
- responsible-AI and validation compliance;
- multitenancy isolation tests;
- audit logs and data-retention policy;
- Human Gate before consequential research/professional outputs are finalized;
- institutional consent/privacy controls for any student pilot;
- anonymized partner reporting by default;
- explicit separation between academic grading and recruitment use.

## Recommended marketplace category

Use the current Microsoft **AI Apps and Agents** category where applicable, with secondary categorization aligned to analytics, productivity, research, education, or professional services depending on the final offer taxonomy available in Partner Center.

## Monetization architecture

Keep commercial configuration separate from the research-safe public code. The production design can support entitlement-based subscriptions, flat-rate access, usage-based metering, or combinations permitted by the selected Microsoft offer type.

For early university–industry pilots, a non-commercial or separately contracted research/education arrangement may be preferable until privacy, institutional, support, pricing, and commercial-use terms are finalized.

## Microsoft-specific release gates

- applicable Partner Center programs enrolled;
- selected offer type confirmed;
- app/agent package validated;
- SaaS lifecycle/fulfillment integration tested if transactable;
- responsible-AI checks passed;
- marketplace certification requirements satisfied;
- privacy and security documentation live;
- support process live;
- Microsoft-compatible provider/model identity logged for every material run;
- frozen case evidence and Human Gate preserved;
- no confidential client or partner IP in the public/student environment;
- no public claim of Microsoft approval before certification is complete;
- no public claim of Big Four partnership, sponsorship, or system equivalence without written authorization.

## Non-claims

NAAIL is an independent research initiative. Microsoft, Azure, Microsoft 365, Teams, Copilot, Deloitte, EY, KPMG, and PwC names are used only to identify target interoperability/distribution surfaces, public comparison targets, or potential partner categories. They do not imply affiliation, sponsorship, endorsement, approval, certification, or access to proprietary firm systems.
