# Anthropic / Claude integration candidates

Status: **Registry only; no upstream code installed or executed.**

- https://github.com/anthropics/financial-services
- https://github.com/anthropics/claude-cookbooks
- https://github.com/anthropics/skills
- https://github.com/anthropics/knowledge-work-plugins
- https://github.com/anthropics/claude-plugins-official
- https://github.com/anthropics/claude-code
- https://github.com/anthropics/courses
- https://github.com/anthropics/claude-code-action
- https://github.com/anthropics/claude-for-financial-advisors
- https://github.com/anthropics/claude-code-playground

## Research mapping
DARWIN: cookbooks, Claude Code, courses. POMELO/ICFR: financial-services, skills. JEV/CAM: skills, cookbooks. Valuation/MACEI: financial-services. SME: knowledge-work-plugins.

## Installation gates
Verify upstream ownership, repository existence and license; pin commit SHAs; review dependencies and secrets; import only necessary modules; run tests; require human approval before deployment. Do not grant autonomous write access to financial datasets or production pipelines.
