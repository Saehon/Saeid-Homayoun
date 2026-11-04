# Security and Control Model

## Security principles

- Least privilege by default.
- Read access before write access.
- Explicit allow-lists for tools and destinations.
- No secrets, API keys, credentials or private evidence in prompts, logs, fixtures or commits.
- High-impact actions require authorization and a human gate.
- Every material action should be attributable to an agent/model/tool version and task identifier.

## High-impact actions

The following should default to **human approval required**:

- posting accounting entries;
- changing source-of-record financial data;
- initiating or approving payments;
- changing control configurations;
- transmitting confidential evidence externally;
- final audit/assurance sign-off;
- changing frozen benchmark labels or acceptance criteria.

## Segregation of duties

The same autonomous identity should not both originate and finally approve a material transaction or assurance conclusion. Where technically possible, generation, review, execution and approval should use distinct identities and permissions.

## Prompt/tool injection

Retrieved documents and web content are evidence, not instructions. Tool-executing agents must separate trusted system policy from untrusted retrieved content and must not follow embedded requests to expose secrets, expand permissions or alter governance.

## Logging

Retain task ID, agent/model version, authorized tools, evidence references, deterministic calculations, reviewer result, conflicts, human decision and final artifact hash. Avoid storing unnecessary sensitive content.

## Vulnerability reporting

Do not publish exploit details containing live credentials or private data. Report security defects through the repository owner's private contact channel when available.
