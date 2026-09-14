# NAAIL OpenLab™ Marketplace Submission Checklist

This checklist is a common gate for OpenAI, Google, and Microsoft distribution. Provider-specific requirements may change and must be re-verified immediately before submission.

## 1. Product identity

- [ ] Product name frozen for the release.
- [ ] Short description and long description reviewed.
- [ ] Screenshots/demo assets use only rights-cleared or synthetic material.
- [ ] NAAIL independence/non-affiliation statement included.
- [ ] Trademark and naming review completed.

## 2. Production service

- [ ] Stable HTTPS production endpoint available.
- [ ] Health monitoring configured.
- [ ] Authentication/authorization implemented.
- [ ] Tenant/user isolation tested.
- [ ] Rate limiting and abuse controls implemented.
- [ ] Secrets stored outside source control.
- [ ] Provider outages/failures handled explicitly.

## 3. Research workflow controls

- [ ] Evidence provenance recorded.
- [ ] Data-rights/license gate active.
- [ ] Competing hypotheses supported where applicable.
- [ ] Empirical designs preserve variable/model specifications.
- [ ] Analysis runs are reproducible or clearly marked otherwise.
- [ ] Robustness/falsification step available.
- [ ] Chain-of-Evidence generated for material conclusions.
- [ ] Human Gate enforced before final consequential output.
- [ ] `NOT_EXECUTED` states preserved for unavailable tools/models.

## 4. Privacy and security

- [ ] Public privacy policy URL live.
- [ ] Terms of use URL live.
- [ ] Support/contact URL live.
- [ ] Data deletion/request process documented.
- [ ] Retention policy documented.
- [ ] Logging/redaction reviewed.
- [ ] Prompt-injection/tool-abuse tests completed.
- [ ] Incident-response process documented.
- [ ] No credentials, restricted standards, or private gold labels in public package.

## 5. OpenAI gate

- [ ] Apps SDK implementation tested in the current supported environment.
- [ ] MCP-compatible tools use narrow, auditable schemas.
- [ ] App behavior complies with current OpenAI usage/developer policies.
- [ ] Privacy policy satisfies current app-submission requirements.
- [ ] Submission metadata and functional demo prepared.
- [ ] No claim of directory approval before OpenAI approval.

## 6. Google gate

- [ ] Cloud Marketplace vendor onboarding completed.
- [ ] Correct Producer Portal project confirmed.
- [ ] Product details submitted/reviewed.
- [ ] Pricing submitted/reviewed.
- [ ] Technical integration submitted/reviewed.
- [ ] Agent Card validated.
- [ ] Support/issue handling operational.
- [ ] No claim of Cloud Marketplace/Gemini Enterprise listing before Google publishes it.

## 7. Microsoft gate

- [ ] Required Partner Center programs enrolled.
- [ ] Offer type selected (SaaS / Microsoft 365-Copilot / other applicable type).
- [ ] Agent/app manifest package validated where required.
- [ ] SaaS fulfillment/lifecycle integration tested if transactable.
- [ ] Responsible-AI/store validation completed.
- [ ] Marketplace certification requirements satisfied.
- [ ] No claim of Marketplace/Copilot approval before Microsoft approval.

## 8. Commercial/IP gate

- [ ] Public research license and commercial terms do not conflict.
- [ ] Patent-sensitive enabling details reviewed before disclosure.
- [ ] Restricted third-party datasets are never redistributed without rights.
- [ ] Pricing/entitlements are configured only in production/private commercial systems.
- [ ] Revenue, billing and tax responsibilities assigned to the appropriate legal entity before paid launch.

## 9. Final release gate

A marketplace release is authorized only when all required boxes for the target provider are complete and the Principal Investigator/Product Owner approves the release.

**Human Gate:** `PENDING_HUMAN_APPROVAL` until provider-specific pre-submission review is complete.
