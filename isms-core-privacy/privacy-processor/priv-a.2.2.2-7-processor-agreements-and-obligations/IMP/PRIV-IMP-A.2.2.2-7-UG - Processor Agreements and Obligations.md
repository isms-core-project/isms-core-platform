<!-- ISMS-CORE:IMP:PRIV-IMP-A.2.2.2-7-UG:privacy:UG:a.2.2.2-7 -->
**PRIV-IMP-A.2.2.2-7-UG — Processor Agreements and Obligations — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Processor Agreements and Obligations — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.2.2.2-7-UG |
| **Related Policy** | PRIV-POL-A.2.2.2-7 (Processor Agreements and Obligations) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial user guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.2.2.2-7 (Processor Agreements and Obligations — the governing policy)
- PRIV-IMP-A.2.2.2-7-TG (Processor Agreements and Obligations — Technical Guide)
- PRIV-POL-A.2.5.7-9 (Sub-processor Management — sub-processor obligations)
- PRIV-POL-A.3.11-12 (Breach Notification — processor breach notification to customers)

---

## Purpose of This Guide

This guide explains **how to implement** the processor obligations of PRIV-POL-A.2.2.2-7. It covers how to review and execute processor agreements with customer controllers, how to enforce instruction compliance, how to handle suspected infringing instructions, and how to maintain processor records.

**Who this guide is for**: DPO, Legal/Compliance, Customer Success / Account Management, IT Security Team.

**Processor-only**: This guide applies to processing activities where [Organisation] acts as PII Processor on behalf of customer controllers.

---

## Part 1 — Processor Agreement Review and Execution (A.2.2.2)

### 1.1 DPO Review Before Agreement Execution

No processor agreement (Data Processing Agreement / DPA) may be executed without DPO review. The process:

1. Legal/Compliance or Account Management receives a draft DPA from the customer (or prepares [Organisation]'s standard DPA for customer signature)
2. The DPA is submitted to the DPO for review before execution
3. DPO reviews the DPA against the Article 28(3) mandatory content checklist (see PRIV-IMP-A.2.2.2-7-TG)
4. DPO confirms whether [Organisation]'s standard DPA template is being used (preferred) or whether a customer's own form is presented
5. For customer-drafted DPAs: DPO marks any gaps or issues for Legal/Compliance to negotiate
6. DPO signs off before Legal/Compliance or senior management executes

**Timeline target**: DPO review completed within 5 business days of receipt of draft.

### 1.2 Mandatory Agreement Content

The DPA must address [Organisation]'s role in assisting the customer with:

- Implementing appropriate technical and organisational security measures (Article 32)
- Responding to data subject rights requests (access, rectification, erasure, restriction, portability, objection, human review)
- Security incident investigation and breach notification
- DPIA and prior consultation (Article 35/36)
- Providing information to demonstrate compliance and enabling audits

The DPO reviews these obligations taking into account the nature of the specific processing engagement — not all obligations will be identical across all DPAs, but all must be meaningfully addressed.

### 1.3 [Organisation]'s Standard DPA

[Organisation] maintains a standard Data Processing Agreement template (see PRIV-IMP-A.2.2.2-7-TG). This template is the preferred basis for all processor engagements. When a customer insists on their own DPA form, Legal/Compliance and the DPO conduct a gap analysis against [Organisation]'s standard to ensure nothing material is absent.

---

## Part 2 — Processing Only on Customer Instructions (A.2.2.3)

### 2.1 What "Instructions" Means in Practice

[Organisation] must process customer PII only for the purposes expressed in the customer's documented instructions. Instructions are documented in:

- The main service agreement or SoW (Statement of Work)
- The Data Processing Agreement
- Documented written instructions issued by the customer during the service

**Implicit instructions** are generally not valid — if the customer has not explicitly authorised a processing operation, it should not be carried out. Where there is doubt about whether a processing operation falls within the agreed scope, the DPO is consulted before proceeding.

### 2.2 Prohibited Own-Purpose Processing

The following are examples of own-purpose use that is prohibited without explicit customer written authorisation:

| Prohibited Use | Why Prohibited |
|---------------|---------------|
| Training or improving [Organisation]'s AI/ML models using customer PII | Own-purpose — not in customer's instruction |
| Benchmarking [Organisation]'s service performance using customer-identified data | Own-purpose analytics |
| Building aggregate market insights from multiple customers' PII | Beyond any individual customer's instruction |
| Sharing customer PII between [Organisation]'s customer contracts | Cross-customer processing without either customer's instruction |

Personnel who identify a proposed use of customer PII that is not covered by the contract must escalate to the DPO immediately.

### 2.3 Personnel Instruction Discipline

All [Organisation] personnel who access customer PII are briefed at onboarding and in annual refresher training on the instruction-only processing principle. The briefing covers:

- What constitutes customer-instructed processing vs own-purpose use
- The prohibition on using customer PII for [Organisation]'s own purposes
- The escalation route when the scope of an instruction is unclear
- The consequences of instruction violation (disciplinary, contractual, and regulatory)

---

## Part 3 — Marketing and Advertising Prohibition (A.2.2.4)

### 3.1 The Prohibition

[Organisation] must not use PII processed under a customer contract for marketing or advertising of [Organisation]'s own products or services, unless:

- The PII principal (the individual data subject) has separately and explicitly consented to such marketing from [Organisation], AND
- That consent was obtained independently of, and not as a condition of, receiving the service

This prohibition protects data subjects who have not chosen to have a direct marketing relationship with [Organisation] — they are the customer's data subjects, not [Organisation]'s.

### 3.2 If Customer PII Marketing Consent Is Sought

If [Organisation] wishes to conduct its own marketing to individuals whose PII it processes as a processor (for example, end-users of a SaaS platform), the following apply:

1. A separate consent mechanism must be designed — not embedded in the customer's service flow
2. Consent must be freely given: opting out cannot affect the individual's access to the service
3. The DPO must approve the consent mechanism before deployment
4. Consent records must be maintained separately from the service relationship records
5. Marketing must only be sent to individuals with a valid, documented consent record

---

## Part 4 — Handling Infringing Instructions (A.2.2.5)

### 4.1 Identifying a Potentially Infringing Instruction

An infringing instruction is one that, if followed, would cause [Organisation] to breach applicable data protection law. Examples:

| Instruction Type | Why It May Infringe |
|-----------------|---------------------|
| Instruct [Organisation] to share PII with a third party without a legal basis | No lawful basis for the onward transfer |
| Instruct [Organisation] to retain PII indefinitely | Violates storage limitation principle |
| Instruct [Organisation] to ignore a data subject erasure request | Interferes with data subject rights |
| Instruct [Organisation] to transfer PII to a country without an adequate transfer mechanism | Unlawful international transfer |
| Instruct [Organisation] to process special category PII without a valid Article 9(2) condition | No basis for special category processing |

### 4.2 Infringing Instruction Escalation Process

When a potentially infringing instruction is identified:

1. The person identifying the issue escalates to the DPO **immediately** — do not proceed with the instruction while it is under assessment
2. The DPO assesses the instruction with Legal/Compliance input where uncertain; this assessment is documented
3. The DPO notifies the customer in writing of the concern and the legal basis for it — the notification must be sent to the customer's data protection contact or legal counsel
4. While the matter is under discussion, the instruction is not executed
5. If the customer confirms the instruction after notification, the DPO documents [Organisation]'s position and escalates to Executive Management; if the instruction remains infringing, [Organisation] shall not execute it and may invoke contractual suspension/termination rights
6. All infringing instruction events are logged in the Infringing Instruction Register (see TG)

**The duty to notify the customer is firm** — [Organisation] has a legal obligation to speak up when a customer instruction would cause a legal breach. Silence is not an option.

---

## Part 5 — Supporting Customer Compliance (A.2.2.6)

### 5.1 Types of Compliance Support

[Organisation] provides customers with the information they need to demonstrate compliance with their obligations as controller. This includes:

**Security documentation**:
- ISO 27001 / 27701 certificates of conformity (when certified)
- Summary of security measures implemented (encryption, access control, backup)
- Annual penetration test report summary (non-confidential findings)
- SOC 2 Type II report (if available)

**Sub-processor transparency**:
- Current sub-processor list and notification of changes (per PRIV-POL-A.2.5.7-9)
- Sub-processor DPAs (on request, subject to confidentiality redaction)

**Audit cooperation**:
- Response to customer audit questionnaires (standard security assessments)
- Cooperation with on-site audits where contractually agreed
- Cooperation with supervisory authority inspections relating to [Organisation]'s processing

**Breach support**:
- Timely breach notifications enabling the customer to meet their Article 33/34 obligations
- Incident investigation reports

### 5.2 Customer Compliance Support Register

The DPO maintains a register of all compliance documentation provided to customers (see PRIV-IMP-A.2.2.2-7-TG for schema). This creates an audit trail demonstrating that [Organisation] has fulfilled its A.2.2.6 obligations.

When a customer requests compliance documentation, Account Management routes the request to the DPO. The DPO confirms what can be provided, prepares or coordinates the documentation, and records the provision.

---

## Part 6 — Maintaining Processor Records (A.2.2.7)

### 6.1 Processor RoPA (Article 30(2))

[Organisation] maintains a processor-side Record of Processing Activities covering all processing carried out on behalf of customers. The processor RoPA is maintained by the DPO and includes:

- [Organisation]'s name and DPO contact details
- Categories of processing performed on behalf of each customer (by type, not customer-identified detail where customer confidentiality requires)
- Transfers to third countries and safeguards
- General description of security measures

The processor RoPA is available to supervisory authorities on request.

### 6.2 Additional Processor Registers

Beyond the RoPA, the DPO maintains:

| Register | Description |
|---------|-------------|
| Processor Agreement Register | All executed customer DPAs — status, review date, key terms |
| Infringing Instruction Register | All infringing instruction events and outcomes |
| Customer Compliance Support Register | Documentation provided to each customer |
| Sub-processor Register | Per PRIV-POL-A.2.5.7-9 |

Register schemas are in PRIV-IMP-A.2.2.2-7-TG.

---

## Evidence Checklist

- [ ] Processor Agreement Register — all active customer DPAs with DPO review date
- [ ] Signed DPAs — executed and filed for all processor engagements
- [ ] Processor RoPA — current, covering all customer processing activities
- [ ] Instruction compliance records — evidence of processing only on documented instructions
- [ ] Infringing Instruction Register — all escalations documented
- [ ] Customer Compliance Support Register — documentation provided per customer and date
- [ ] Marketing consent records — if [Organisation] markets to any customer data subjects
- [ ] Annual processor records review

---

<!-- QA_VERIFIED: [Date] -->
