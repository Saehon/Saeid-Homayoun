# Microsoft Distribution Package

**Target surfaces:** Microsoft Marketplace and Microsoft 365 Copilot  
**Recommended offer model:** centrally hosted SaaS agent with Microsoft 365/Copilot distribution where appropriate  
**Status:** Public scaffold only; not submitted or approved.

## Recommended NAAIL offer

**Name:** NAAIL OpenLab™ Research Intelligence Agent

**Primary job:** Deliver governed research workflows inside Microsoft environments while preserving evidence provenance, reproducibility, privacy, and mandatory Human Gate controls.

## Recommended distribution model

Microsoft currently supports AI Apps and Agents in Marketplace and provides paths for Azure agents as well as Microsoft 365/Copilot agents. For NAAIL, a centrally hosted multitenant SaaS model is the preferred starting point because it preserves one controlled NAAIL core and lets the distribution layer integrate with Microsoft 365/Copilot without exposing proprietary orchestration.

## Initial Microsoft surfaces

- Microsoft Marketplace listing;
- Microsoft 365 Copilot agent surface;
- Teams as a research-workspace channel where appropriate;
- optional Word/Excel integration for governed research artifacts and analysis workflows.

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
- Human Gate before consequential research/professional outputs are finalized.

## Recommended marketplace category

Use the current Microsoft **AI Apps and Agents** category where applicable, with secondary categorization aligned to analytics, productivity, research, or professional services depending on the final offer taxonomy available in Partner Center.

## Monetization architecture

Keep commercial configuration separate from the research-safe public code. The production design can support entitlement-based subscriptions, flat-rate access, usage-based metering, or combinations permitted by the selected Microsoft offer type.

## Microsoft-specific release gates

- applicable Partner Center programs enrolled;
- selected offer type confirmed;
- app/agent package validated;
- SaaS lifecycle/fulfillment integration tested if transactable;
- responsible-AI checks passed;
- marketplace certification requirements satisfied;
- privacy and security documentation live;
- support process live;
- no public claim of Microsoft approval before certification is complete.

## Non-claims

NAAIL is an independent research initiative. Microsoft, Azure, Microsoft 365, Teams, and Copilot names are used only to identify target interoperability/distribution surfaces and do not imply affiliation, sponsorship, endorsement, or approval.
