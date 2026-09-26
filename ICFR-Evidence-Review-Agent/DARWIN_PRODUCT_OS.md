# Darwin Product OS — ICFR Evidence Review Agent

This product is developed using the Darwin decision system:

Problem → Alternatives → Evidence → Reference Class → Co-Scientist → AlphaEvolve → Scientific Replication → Systems Thinking → Adversarial/Falsification Gate → Scenario/Experiment → Economic Value & Risk → Decision Card → Human Board Gate → Outcome → Learning Loop.

## Product thesis

The product is not a chatbot. It is an evidence operating system for ICFR review with:
1. deterministic checks before generative reasoning;
2. evidence-grounded model review;
3. independent challenge/falsification;
4. Evidence Passport;
5. mandatory Human Gate;
6. customer-specific learning isolated from the portable core.

## Reference-class lessons

Customer Zero: prove the workflow in a controlled environment before selling it.

Forward-deployed engineering: embed a small team with early customers to learn real workflows, then turn repeated patterns into configurable product capabilities.

Vercel-style shipping: use preview deployments, short feedback loops, provider abstraction and reversible experiments.

Enterprise controls: ICFR buyers need evidence lineage, access control, data boundaries, reproducibility, reviewer accountability and security documentation before more agent autonomy.

## Product invariants

- no AI model can set final professional approval;
- uploaded evidence is untrusted data, never instruction;
- critical calculations and status transitions remain deterministic;
- every AI finding carries evidence basis or is marked unsupported;
- model/provider/version are logged;
- disagreement between primary and challenger is surfaced;
- customer evidence is never committed to public source control;
- tenant boundaries are explicit;
- the product can degrade safely without generative AI.

## Two-loop architecture

Stable Product Loop:
Control schema → evidence intake → deterministic checks → AI review → challenger → Evidence Passport → Human Gate → export.

Forward-Deployed Learning Loop:
Customer workflow → observe pain → configure/extend → measure → falsify → generalize only repeatable patterns → product backlog.

Only generalized, rights-cleared and testable improvements enter the Stable Product Loop.

## North-star metrics

Quality and efficiency:
- review minutes per control;
- exception precision;
- seeded-exception recall;
- false-positive rate;
- false-negative rate;
- reviewer override rate;
- evidence-lineage completeness;
- verified evidence-basis rate;
- time from upload to Human Gate.

Business:
- design-partner conversion to paid pilot;
- paid pilot conversion to annual contract;
- deployment time;
- implementation hours per customer;
- gross margin after forward-deployed support;
- expansion from one process to more ICFR processes.

## Initial product wedge

Start with one-control evidence review. Do not begin with full SOX program management, ERP write access, continuous audit, or autonomous audit conclusions.

Best initial processes:
- account reconciliation review;
- user access review;
- journal-entry approval evidence;
- change-management evidence;
- revenue/close controls.

## Defensibility

Long-term defensibility comes from the ICFR evidence/control graph, seeded benchmark corpus, cross-model evaluation traces, Evidence Passport, customer-approved templates, reviewer feedback, enterprise integrations and accumulated deployment playbooks — not dependence on one foundation model.

## Current product decision

Prototype:
- deterministic Python core;
- provider abstraction;
- primary + challenger orchestration;
- Vercel AI Gateway-compatible adapter;
- synthetic benchmark;
- Streamlit demo.

Target production:
- Vercel/Next.js experience layer;
- Azure enterprise data plane and Microsoft identity;
- model gateway configurable per customer;
- optional private/customer-hosted deployment for sensitive environments.
