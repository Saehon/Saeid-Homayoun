# NAAIL OpenLab™ — AI Engineering Benchmark

NAAIL is independent and vendor-neutral. This document records public engineering patterns that inform NAAIL's research architecture; it does not copy proprietary implementations.

## Microsoft pattern
Current Microsoft Agent Framework / Foundry documentation emphasizes:
- explicit functional or graph-based workflows;
- specialist agents as workflow participants;
- sequential, concurrent, handoff, group-chat and other orchestration patterns;
- human-in-the-loop and checkpoint/resume for durable workflows;
- observability through spans, metrics, events and OpenTelemetry;
- production evaluation and monitoring of quality, safety, tool accuracy, task completion, latency and errors.

Public references:
- https://learn.microsoft.com/en-us/agent-framework/
- https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/
- https://learn.microsoft.com/en-us/azure/foundry/concepts/observability

## Google pattern
Current Google ADK / Agents CLI documentation emphasizes a lifecycle of:
`scaffold → build → test → evaluate → deploy → observe`

Relevant patterns include:
- expressive multi-agent orchestration;
- repeatable evaluation sets and iterative eval-fix loops;
- sandboxed code execution for agentic tasks;
- deployment-independent agent development;
- production tracing/observability and agent analytics;
- MCP/A2A-compatible ecosystem patterns.

Public references:
- https://google.github.io/adk-docs/
- https://google.github.io/agents-cli/guide/development/

## OpenAI pattern
Current OpenAI Agents SDK documentation emphasizes a deliberately small set of composable primitives:
- agents with instructions and tools;
- agents-as-tools and handoffs;
- input/output/tool guardrails;
- sessions and human-in-the-loop;
- built-in tracing of agent, model, tool, handoff and guardrail activity;
- evaluation of workflows and production behavior.

Public references:
- https://openai.github.io/openai-agents-python/
- https://openai.github.io/openai-agents-python/guardrails/
- https://openai.github.io/openai-agents-python/tracing/

## NAAIL synthesis
NAAIL translates these public patterns into a provider-neutral research architecture:
1. **Explicit workflow graphs** for complex/high-risk professional tasks.
2. **Small composable agents** rather than one unconstrained mega-agent.
3. **Scoped tools + guardrails + Human Gates** for material actions/conclusions.
4. **Checkpoint/resume and state isolation** for durable experiments.
5. **OpenTelemetry-compatible observability** without exposing private chain-of-thought.
6. **Eval-first promotion gates** using audit-specific metrics and frozen Digital Twin benchmarks.
7. **Provider adapters** so OpenAI, Google, Microsoft, local/open, and future models can compete under the same evidence and evaluation contract.
8. **Stable Knowledge Core™ / Replaceable Technology Core™** so model churn does not invalidate validated professional/scientific knowledge.

## What NAAIL adds
NAAIL's research contribution is the combination of enterprise agent engineering with:
- business-school curriculum intelligence;
- Audit Digital Twins;
- professional evidence hierarchies;
- FT50/AJG research intelligence;
- Research Decision DAG governance;
- falsification and replication;
- Chain-of-Evidence;
- human professional/scientific responsibility.
