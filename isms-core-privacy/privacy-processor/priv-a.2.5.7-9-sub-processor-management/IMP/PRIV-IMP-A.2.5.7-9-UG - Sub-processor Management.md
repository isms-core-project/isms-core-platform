<!-- ISMS-CORE:IMP:PRIV-IMP-A.2.5.7-9-UG:privacy:UG:a.2.5.7-9 -->
**PRIV-IMP-A.2.5.7-9-UG — Sub-processor Management — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Sub-processor Management — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.2.5.7-9-UG |
| **Related Policy** | PRIV-POL-A.2.5.7-9 (Sub-processor Management) |
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

- PRIV-POL-A.2.5.7-9 (Sub-processor Management — the governing policy)
- PRIV-IMP-A.2.5.7-9-TG (Sub-processor Management — Technical Guide)
- PRIV-POL-A.2.5.2-6 (Transfer and Disclosure (Processor) — transfer basis for sub-processor jurisdictions)
- PRIV-POL-A.2.2.2-7 (Processor Agreements and Obligations — customer authorisation basis)

---

## Purpose of This Guide

This guide explains **how to implement** the sub-processor management obligations of PRIV-POL-A.2.5.7-9. It covers how to identify and disclose sub-processors to customers, how to engage new sub-processors, and how to manage sub-processor changes with the required customer notification.

**Who this guide is for**: DPO, Procurement, Legal/Compliance, Customer Success.

**Processor-only**: This guide applies to processing activities where [Organisation] acts as PII Processor on behalf of customer controllers.

---

## Part 1 — What Is a Sub-processor

### 1.1 Definition

A sub-processor is any third party engaged by [Organisation] (as processor) to process PII on behalf of [Organisation]'s customers. The key characteristic is that the third party processes PII that belongs to [Organisation]'s customers — not just [Organisation]'s own data.

**Sub-processor examples** in a typical SaaS or managed service context:

| Third Party | What They Do | Sub-processor? |
|-------------|-------------|----------------|
| AWS / Azure / GCP | Host [Organisation]'s platform; customer PII stored on their infrastructure | Yes |
| Email delivery platform | Send transactional emails triggered by customer data | Yes |
| Customer support tooling | Support agents see customer account data during tickets | Yes |
| Payment processor | Processes payment data for [Organisation]'s own billing | No — processes [Organisation]'s data, not customer's data |
| Office productivity tools | Internal email, calendar — no customer PII | No — not used for customer PII processing |
| Analytics platform receiving pseudonymised data only | Receives non-identifiable aggregates | Depends — confirm with DPO |

When in doubt about whether a third party is a sub-processor for a specific service, the DPO confirms.

---

## Part 2 — Disclosing Sub-processors Before Service Commencement (A.2.5.7)

### 2.1 Pre-Commencement Disclosure

Before [Organisation] begins processing PII on behalf of a new customer, the customer must be informed which sub-processors are used for that service. This disclosure occurs as part of the processor agreement process:

1. The DPO confirms the current Sub-processor Register entries applicable to the service being contracted
2. The sub-processor list is provided to the customer as part of the processor agreement — either in an appendix, a schedule, or by reference to a published URL maintained by [Organisation]
3. The processor agreement records the customer's authorisation: either **specific authorisation** (customer approves each sub-processor by name) or **general authorisation** (customer approves [Organisation]'s use of sub-processors subject to change notification rights)
4. The DPO confirms the authorisation model in the Processor Agreement Register

**General vs specific authorisation**: Most [Organisation] processor agreements use general written authorisation — i.e., the customer approves [Organisation]'s use of sub-processors as a class, with the right to object to changes. This is the norm for SaaS/cloud services. Specific authorisation (per sub-processor) may be required by some customers — this is more restrictive and should be flagged to Legal/Compliance.

---

## Part 3 — Engaging Sub-processors (A.2.5.8)

### 3.1 Sub-processor Onboarding Process

Before [Organisation] engages a new sub-processor with access to customer PII:

**Step 1 — Procurement gate**: Procurement identifies the proposed third party and triggers a DPO review before any contract is signed. The trigger is required for any supplier who will access customer PII.

**Step 2 — DPO assessment**:
- Confirm the third party is acting as a sub-processor (not as a controller in their own right)
- Identify what customer PII categories they will access and for what purpose
- Identify their jurisdiction (relevant for transfer mechanism — see PRIV-POL-A.2.5.2-6)
- Confirm customer authorisation covers this engagement (general authorisation in existing DPAs, or specific authorisation to be sought)

**Step 3 — Security due diligence**:
- Procurement and IT Security conduct security due diligence (ISO 27001 certificate or equivalent, SOC 2 report, security questionnaire)
- Due diligence is documented and filed in the Sub-processor Register

**Step 4 — Sub-processor agreement**:
- Legal/Compliance drafts or reviews the sub-processor agreement — it must impose the same data protection obligations as [Organisation]'s own processor agreement with customers
- DPO reviews for Article 28(4) compliance — same obligations imposed on sub-processor
- Agreement is executed before sub-processor access to customer PII is enabled

**Step 5 — Register update**:
- DPO adds the sub-processor to the Sub-processor Register
- Customer notification is prepared per Part 4 (if customers already exist on the service)
- Transfer Destination Register is updated if the sub-processor introduces a new transfer destination (per PRIV-IMP-A.2.5.2-6-UG)

### 3.2 Obligations Flowing Down to Sub-processors

The sub-processor agreement must impose (at minimum):

1. Processing only on [Organisation]'s instructions
2. Appropriate technical and organisational security measures (equivalent to GDPR Article 32 standard)
3. Confidentiality obligations on personnel with PII access
4. Sub-sub-processor engagement restrictions (same rules as [Organisation] applying to their sub-processors)
5. Breach notification to [Organisation] without undue delay (enabling [Organisation] to meet its own notification obligations to customers)
6. Return or deletion of all PII at end of engagement
7. Cooperation with [Organisation]'s audits and inspections
8. International transfer compliance where applicable

### 3.3 [Organisation]'s Liability

[Organisation] remains fully liable to customers for sub-processor compliance with data protection obligations. If a sub-processor causes a breach or compliance failure, [Organisation] is responsible to the customer as if it had committed the failure itself. This is the primary reason for rigorous sub-processor onboarding and ongoing monitoring.

---

## Part 4 — Managing Sub-processor Changes (A.2.5.9)

### 4.1 What Constitutes a Change

Sub-processor changes requiring customer notification include:

- Adding a new sub-processor not previously on the list
- Replacing an existing sub-processor with a different provider
- A sub-processor materially changes the jurisdiction in which they process PII (e.g., data centre migration)

Changes that do NOT require notification (typically):
- Routine security updates or software upgrades to existing sub-processors
- [Organisation]'s internal infrastructure changes that do not introduce new third parties

When uncertain, the DPO confirms whether customer notification is required.

### 4.2 Change Notification Process

1. The DPO is notified of the intended change (by Procurement, IT Security, or the relevant business team)
2. DPO assesses the compliance impact:
   - New jurisdiction → Transfer Destination Register update + transfer mechanism needed?
   - New PII categories → Does the processor agreement scope cover this?
   - Risk profile of new sub-processor → Due diligence required before notification
3. DPO confirms the change can proceed (from a compliance perspective) and sets the effective date
4. Customer notification is prepared: brief description of the change, name of new/replacement sub-processor, jurisdiction, processing context, effective date, and how to object
5. Notification is sent to all affected customers' data protection contacts via Customer Success, with the minimum notice period per the processor agreement (typically 30 days)
6. Notification and responses are logged in the Sub-processor Change Notification Log (see TG)

### 4.3 Handling Customer Objections

If a customer objects to a planned sub-processor change:

1. Customer Success logs the objection and notifies the DPO immediately
2. DPO and Legal/Compliance assess the objection:
   - Can [Organisation] fulfil the service for this customer without the new sub-processor? If yes: consider maintaining the existing arrangement for the objecting customer
   - If not: are there alternative technical measures that achieve the same outcome without the objected sub-processor?
3. If no accommodation is possible, the customer's contract terms determine the outcome — typically the customer has the right to terminate the contract without penalty
4. The objection and resolution are documented in the Sub-processor Change Notification Log

---

## Evidence Checklist

- [ ] Sub-processor Register — current list of all sub-processors; applicable services and customers documented
- [ ] Sub-processor agreements — executed agreements with same obligations as main processor agreements
- [ ] Pre-commencement disclosure records — sub-processor list provided to each customer before service start
- [ ] Customer authorisation records — general or specific authorisation confirmed in each processor agreement
- [ ] Security due diligence records — due diligence conducted and documented for each sub-processor
- [ ] Sub-processor Change Notification Log — advance notifications for all changes; customer responses and objection outcomes
- [ ] Annual sub-processor register review — DPO confirms currency and accuracy

---

<!-- QA_VERIFIED: [Date] -->
