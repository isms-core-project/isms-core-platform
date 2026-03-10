<!-- ISMS-CORE:IMP:CLD-IMP-A.5-UG:cloud:UG:a.5 -->
**CLD-IMP-A.5-UG — Data Minimisation — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Data Minimisation — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-IMP-A.5-UG |
| **Related Policy** | CLD-POL-A.5 (Data Minimisation) |
| **Document Creator** | CISO / Data Protection Officer (DPO) |
| **Document Owner** | CISO / Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial user guide for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant regulatory or service architecture change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-POL-A.5 (Data Minimisation — the governing policy)
- CLD-IMP-A.5-TG (Data Minimisation — Technical Guide)
- CLD-POL-A.4 (Collection Limitation — scope of PII collected from controllers)
- CLD-POL-A.6 (Use, Retention and Disclosure Limitation — retention and deletion schedules)
- CLD-POL-A.11 (Information Security — secure disposal of physical storage media)

---

## Purpose of This Guide

This guide explains how [Organisation] implements the data minimisation obligations of CLD-POL-A.5 in day-to-day cloud service operations. It covers how to configure services to collect the minimum necessary PII, how to conduct periodic minimisation reviews of existing services, and how to handle controller requests to expand collection scope.

**Who this guide is for**: Cloud Engineering, Cloud Service Delivery, Security Operations, and the DPO.

**Cloud processor context**: This guide applies to [Organisation] acting as a public cloud PII processor under ISO/IEC 27018:2025. PII minimisation obligations apply to temporary files, logs, and working storage generated during cloud processing on behalf of PII controllers.

---

## Part 1 — Configuring Minimum-Necessary Collection Scopes

### 1.1 Principle: Processor Minimisation Scope

[Organisation] does not determine what PII controllers collect from their data subjects. [Organisation]'s minimisation obligation applies to the ephemeral and working PII generated within cloud infrastructure during processing — cache files, swap files, work files, application logs, and ephemeral compute storage.

For each cloud service component, Cloud Engineering SHALL document:

1. **What PII categories may appear in temporary storage** during normal processing operations
2. **Why that PII is technically necessary** in that storage location (i.e., cannot be excluded without breaking the processing function)
3. **Erasure trigger** — the event that causes secure erasure of that temporary store

This documentation forms the Temporary File Scope Record (see CLD-IMP-A.5-TG for schema).

### 1.2 Log Minimisation Configuration

Application and infrastructure logs present the greatest risk of PII persistence beyond the active processing window. Cloud Engineering SHALL apply the following controls at service build and configuration review:

1. **Identify log sinks** — map all log outputs per service component (application logs, access logs, audit logs, debug logs)
2. **Classify PII risk per sink** — for each sink, determine whether PII appears in: request headers, URL parameters, request/response payloads, error traces, or stack dumps
3. **Apply masking or exclusion** — PII that is not operationally necessary in logs SHALL be masked at point of emission (e.g., replace email addresses with `[MASKED]`, truncate PII fields in error traces)
4. **Set retention limits** — each log sink containing PII SHALL have an automated retention period set to the minimum operationally necessary and no longer than the controller's service agreement maximum

Cloud Service Delivery confirms log minimisation configuration with the controller during onboarding and records the agreed log retention period in the service agreement schedule.

### 1.3 Pseudonymisation and Anonymisation for Processing Functions

Where [Organisation] can fulfil a processing function on pseudonymised or aggregated data rather than identifiable PII, Cloud Engineering SHALL implement this by design. Common scenarios:

| Processing Function | Minimum-Necessary Form |
|--------------------|----------------------|
| Usage analytics and telemetry | Aggregated or pseudonymised identifiers |
| Performance monitoring | Pseudonymised session IDs |
| Debugging and error tracing | Masked PII in stack traces |
| Test and development environments | Synthetic or anonymised datasets |
| Batch reporting | Aggregated outputs; no record-level PII in report files |

Before applying any anonymisation technique to controller PII, the DPO SHALL confirm that the output is genuinely anonymised and that re-identification risk is acceptably low. The DPO issues an Anonymisation Confirmation Record (see CLD-IMP-A.5-TG).

---

## Part 2 — Data Minimisation Reviews for Existing Services

### 2.1 When a Review Is Required

Cloud Engineering and the DPO conduct a data minimisation review:

- **Annually** — as part of the scheduled cloud service security review
- **When a service component is substantially modified** — particularly if changes affect data flow, storage, or logging
- **When a new PII category is observed** in temporary storage that was not previously documented
- **Following a security or data quality incident** where PII remanence was identified

### 2.2 Review Process

1. **Inventory current temporary stores** — Cloud Engineering produces an updated Temporary File Scope Record listing all storage categories in use, the PII categories that may appear in each, and the erasure mechanism configured
2. **Test erasure effectiveness** — Security Operations runs a remanence test: following completion of a representative processing job, confirm that no residual PII is recoverable from storage allocated to that job (see CLD-IMP-A.5-TG for test methodology)
3. **Review log configurations** — confirm that masking and retention rules are still correctly applied; check for new log sinks introduced since the last review
4. **Identify minimisation opportunities** — review whether any PII currently captured in temporary storage could be excluded or replaced with a less identifying substitute without affecting service function
5. **Record findings** — the DPO and CISO co-sign the review outcome; gaps are logged as remediation actions with owner and deadline

### 2.3 Multi-Tenant Isolation Verification

In multi-tenant environments, the minimisation review SHALL include confirmation that storage reallocated between tenants contains no residual PII from prior processing. Cloud Engineering confirms:

- Automated erasure is triggered before reallocation
- Reallocation events are logged and auditable
- A sample of reallocation events from the period is inspected to confirm erasure completion

---

## Part 3 — Handling Controller Requests to Expand Collection Scope

### 3.1 Assessing Expansion Requests

Where a PII controller requests that [Organisation] expand the scope of PII processed on its behalf (e.g., adding a new PII category to a processing pipeline, enabling a new log type, or activating a feature that processes additional PII), [Organisation] SHALL assess the request before implementation.

Cloud Service Delivery receives the request and forwards it to Cloud Engineering and the DPO for assessment. The DPO confirms whether the expanded scope:

1. Falls within the purposes stated in the controller's service agreement and DPA
2. Requires updating the controller's DPA or data processing schedule
3. Introduces new temporary storage requirements that must be documented in the Temporary File Scope Record

Processing of expanded PII scope SHALL NOT commence until the DPA is updated (if required) and the DPO confirms in writing.

### 3.2 Scope Reduction and Controller Instructions

Where a controller requests reduction of PII in scope (e.g., ceasing capture of a log field, reducing retention periods), Cloud Engineering SHALL implement the change promptly. Cloud Service Delivery confirms completion to the controller in writing within 5 business days of implementation.

---

## Evidence Checklist

- [ ] Temporary File Scope Records — per service component, current and complete
- [ ] Automated erasure configuration records — technical evidence erasure is implemented for each storage category
- [ ] Log minimisation configuration records — masking and retention rules per log sink, reviewed and current
- [ ] Multi-tenant isolation test records — remanence test results from each annual review
- [ ] DPO Anonymisation Confirmation Records — issued before any controller PII is treated as anonymised
- [ ] Annual minimisation review sign-off — DPO and CISO co-signature on review findings
- [ ] DPA update records — where controller expansion of scope required DPA amendment

---

<!-- QA_VERIFIED: [Date] -->
