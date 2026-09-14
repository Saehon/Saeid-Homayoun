# OpenAI Distribution Package

**Target surface:** ChatGPT App Directory  
**Integration model:** OpenAI Apps SDK with MCP-compatible backend tools  
**Status:** Public scaffold only; not submitted or approved.

## Recommended NAAIL app

**Name:** NAAIL OpenLab™ Research Co-Scientist

**Primary job:** Turn a research question into an evidence-governed workflow that can generate competing hypotheses, design empirical tests, inspect evidence provenance, execute approved tools, challenge conclusions, and produce a Human-Gated research artifact.

## Initial tool surface

Expose only narrow, auditable tools from the public application layer:

1. `frame_research_question`
2. `generate_competing_hypotheses`
3. `retrieve_evidence_metadata`
4. `build_empirical_design`
5. `run_reproducible_analysis`
6. `evaluate_robustness`
7. `build_chain_of_evidence`
8. `request_human_gate`
9. `export_research_artifact`

No tool should expose private prompts, provider credentials, restricted corpora, private benchmark labels, or patent-sensitive orchestration.

## Required production components

- production HTTPS backend;
- Apps SDK-compatible app UI;
- MCP-compatible tool server;
- user authentication/authorization where required;
- privacy policy;
- support/contact endpoint;
- data-deletion/request process;
- usage-policy and safety compliance;
- prompt-injection/tool-abuse controls;
- logging with minimization/redaction;
- clear confirmation for consequential actions;
- Human Gate before professional/scientific claims are finalized.

## Submission positioning

The application should be presented as a focused research workflow rather than as a generic chatbot. Core value proposition:

> Evidence-governed research from question to reproducible empirical design, adversarial validation, Chain-of-Evidence, and human-approved output.

## Recommended first demo

Use a synthetic accounting/audit research case. The demo should show:

- a research question;
- two or more competing hypotheses;
- evidence provenance rather than copied restricted text;
- a reproducible empirical specification;
- one robustness/falsification step;
- a Chain-of-Evidence summary;
- an explicit Human Gate.

## Non-claims

Do not describe this package as listed, approved, certified, partnered with, endorsed by, or sponsored by OpenAI unless OpenAI has actually completed the applicable review and approval process.
