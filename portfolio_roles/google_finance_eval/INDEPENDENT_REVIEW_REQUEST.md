# Independent reviewer request: Google Finance model evaluator

**Review state: OPEN / NOT YET APPROVED.** This is not a documented external scientific peer review.

## Reviewer qualifications
Prefer **two independent reviewers** with complementary skills: (1) Python / API reliability and security, and (2) financial-domain evidence or assurance / research-methods validation. Reviewers should not be the code author, should record affiliations and conflicts, and should not access unpublished POMELO, private financial data, credentials, or the full FinanceBench dataset unless appropriately licensed.

## Review objectives
Check numeric/financial question correctness, no gold leakage, source document provenance, price/usage computation, license and data transfer permissions.

## Mandatory checks
- [ ] Evaluate pull-request diff, authorship boundaries, third-party license and any unrelated changes.
- [ ] Reproduce all unit tests on a clean Python 3.11 environment; record commit SHA, run URL and any environmental exceptions.
- [ ] Independently inspect all three provider payload builders and usage parsers; verify model identifiers, 401/429/5xx and empty/blocked outputs.
- [ ] Check no credentials, unpublished data, copyrighted source corpus, student records or customer information are committed or logged.
- [ ] Confirm `--execute` and `--authorize-data-transfer` are both required for API use; dry-run must never call external services.
- [ ] Review the budget limitations: an estimated cap is **not** a guaranteed provider billing limit.
- [ ] Review test coverage and challenge at least three new failure cases not written by the author.
- [ ] Independently annotate a small, admissibly licensed blind test set and disclose inter-rater disagreement before publishing accuracy claims.
- [ ] Check error taxonomy, model/version drift, abstention and unknown-cost failures.
- [ ] Sign decision (Approve / Request changes), name reviewer and date, cite GitHub review permalink.

## Reviewer signoff
**Independent review complete?** NO.  
**Approved for use on real financial/client data?** NO.  
**Real model inference with licensed data completed?** NO.  
**Approved for production or compliance claims?** NO.

Do not change any NO to YES without the corresponding independently verified evidence.

## References
- Dataset: https://huggingface.co/datasets/PatronusAI/financebench — public sample CC BY-NC 4.0, not embedded.
- Google Gemini: https://ai.google.dev/api/generate-content
- Anthropic: https://platform.claude.com/docs/en/api/messages
- OpenAI: https://platform.openai.com/docs/api-reference/responses
