# Vercel + Azure Production Architecture

## Design principle

Use the fastest layer for product experience and iteration, and a governed enterprise layer for evidence and identity.

Browser / Teams
→ Vercel / Next.js experience layer
→ Azure enterprise API/data plane
→ deterministic ICFR engine + model gateway
→ Evidence Passport
→ Human Gate.

## Vercel role

Use for:
- Next.js UI;
- preview deployments;
- design-partner feedback;
- lightweight orchestration;
- AI Gateway/provider routing where customer policy permits.

Do not assume the frontend platform should become the system of record for customer workpapers.

## Azure role

Use for:
- Microsoft Entra identity;
- enterprise tenant boundaries;
- evidence storage;
- private networking options;
- key/secrets management;
- Microsoft 365 / SharePoint / Graph integrations;
- Marketplace-aligned operations.

## Provider-neutral AI

Recommended policy:
- Primary reviewer: customer-approved high-capability model.
- Independent challenger: separate provider/model where practical.
- Deterministic engine: independent of both.
- Human Gate: final authority.

For the prototype, Vercel AI Gateway can provide an OpenAI-compatible interface with model IDs configured by environment variable. Production may route directly through Azure OpenAI, Anthropic, IBM, or a private model according to customer requirements.

## Environments

- local
- preview
- pilot
- production

Production customer evidence must not be copied into preview by default.

## Deployment gate

Every pull request:
1. unit tests;
2. benchmark regression;
3. security/static checks;
4. preview deployment;
5. human review.

Production:
1. immutable build artifact;
2. production configuration;
3. smoke test;
4. controlled promotion;
5. observability check;
6. rollback path.

## Current Vercel connection state

When this document was created, the connected Vercel account exposed no teams/projects. The repository can be prepared for Vercel now; deployment needs an authorized Vercel project/team.
