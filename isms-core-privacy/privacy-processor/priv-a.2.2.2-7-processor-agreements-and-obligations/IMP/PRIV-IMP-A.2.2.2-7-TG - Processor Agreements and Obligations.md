<!-- ISMS-CORE:IMP:PRIV-IMP-A.2.2.2-7-TG:privacy:TG:a.2.2.2-7 -->
**PRIV-IMP-A.2.2.2-7-TG — Processor Agreements and Obligations — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Processor Agreements and Obligations — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.2.2.2-7-TG |
| **Related Policy** | PRIV-POL-A.2.2.2-7 (Processor Agreements and Obligations) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial technical guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.2.2.2-7 (Processor Agreements and Obligations — the governing policy)
- PRIV-IMP-A.2.2.2-7-UG (Processor Agreements and Obligations — User Guide)

---

## Purpose of This Guide

This guide provides the **technical structures, register schemas, and templates** for processor agreement management. It covers:

- Processor Agreement Register schema
- Article 28(3) DPA mandatory content checklist
- [Organisation] standard DPA structural outline
- Infringing Instruction Register schema
- Customer Compliance Support Register schema
- Processor RoPA schema (Article 30(2))

**Audience**: DPO, Legal/Compliance.

---

## 1. Processor Agreement Register

Tracks all executed Data Processing Agreements with customers. Maintained by DPO. Classified RESTRICTED.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Agreement ID | Text | Unique reference (e.g., DPA-CUST-001) |
| Customer Name | Text | Name of the customer (controller) |
| Customer DPO / Legal Contact | Text | Customer's data protection contact |
| Agreement Type | Enum | [Organisation] Standard DPA / Customer DPA / Addendum to Master Agreement |
| Execution Date | Date | Date agreement was fully executed |
| Review Date | Date | Next scheduled review |
| Scope of Processing | Text | Services covered and categories of processing |
| PII Categories | Text | Categories of PII processed under the agreement |
| Data Subject Categories | Text | Whose data is processed (e.g., customer's end-users, employees) |
| Special Category PII | Boolean | Yes / No |
| International Transfers | Boolean | Yes / No |
| Transfer Mechanism (if applicable) | Text | SCCs module, adequacy, BCRs |
| Sub-processor List Reference | Text | Reference to sub-processor disclosure for this customer |
| DPO Review Date | Date | Date DPO reviewed this agreement |
| DPO Sign-Off | Boolean | Yes / No |
| Agreement Status | Enum | Active / Expired / Terminated / Under Renewal |
| Termination Date | Date | If terminated: date |
| Notes | Text | Exceptions, customer-specific terms, pending amendments |

---

## 2. Article 28(3) DPA Mandatory Content Checklist

Use this checklist when reviewing any incoming customer DPA or when preparing [Organisation]'s standard DPA for a new customer.

```
ARTICLE 28(3) DPA REVIEW CHECKLIST

Customer: _____________________________________________
Agreement Ref: _____________________________________________
DPO Reviewer: _____________________________________________
Review Date: _____________________________________________

MANDATORY CONTENT (GDPR Art. 28(3))

[ ] 1. Process only on documented instructions of the controller
        — including transfers to third countries (Art. 28(3)(a))
        Notes: _____________________________________________

[ ] 2. Ensure that persons authorised to process PII are subject to
        confidentiality obligations (Art. 28(3)(b))
        Notes: _____________________________________________

[ ] 3. Implement appropriate technical and organisational security measures
        per Article 32 (Art. 28(3)(c))
        Notes: _____________________________________________

[ ] 4. Respect conditions for engaging sub-processors: controller consent required;
        sub-processors subject to equivalent obligations (Art. 28(3)(d) / 28(2))
        Notes: _____________________________________________

[ ] 5. Assist the controller with fulfilling data subject rights requests
        (access, rectification, erasure, restriction, portability, objection)
        taking into account the nature of processing (Art. 28(3)(e))
        Notes: _____________________________________________

[ ] 6. Assist the controller with security obligations (Art. 32), breach
        notification (Art. 33/34), DPIA (Art. 35), and prior consultation (Art. 36)
        taking into account the nature of processing and information available
        (Art. 28(3)(f))
        Notes: _____________________________________________

[ ] 7. At the choice of the controller: delete or return all PII upon end of service;
        delete existing copies unless law requires retention (Art. 28(3)(g))
        Notes: _____________________________________________

[ ] 8. Make available all information necessary to demonstrate compliance with
        Article 28 obligations; allow and contribute to audits and inspections
        (Art. 28(3)(h))
        Notes: _____________________________________________

ADDITIONAL CHECKS

[ ] 9. Sub-processor list: is the initial list attached or referenced?
[ ] 10. Prior general authorisation vs specific authorisation for sub-processors?
[ ] 11. International transfer mechanism addressed where applicable?
[ ] 12. Security measures schedule: is Annex II / Schedule of measures present?
[ ] 13. Duration / subject matter of processing: described adequately?

CONCLUSION
[ ] DPA compliant with Art. 28(3) — approve for execution
[ ] DPA requires the following additions / amendments before execution:
    _____________________________________________
[ ] DPA is deficient in a material way — do not execute without remediation

DPO: _________________________ Date: _____________
```

---

## 3. [Organisation] Standard DPA Structural Outline

The standard DPA template (full text maintained separately by Legal/Compliance with DPO input) follows this structure:

```
DATA PROCESSING AGREEMENT
Between: [Customer Name] (Controller)
And: [Organisation] (Processor)
Effective Date: [Date]

RECITALS
[Background: service agreement reference; processor engagement basis]

1. DEFINITIONS
   [Standard GDPR definitions; [Organisation]-specific service definitions]

2. SUBJECT MATTER AND DURATION
   Subject matter: [Service description]
   Duration: [Aligned to service agreement]

3. NATURE AND PURPOSE OF PROCESSING
   [Specific description of what [Organisation] does with the PII]

4. TYPE OF PERSONAL DATA
   [Categories of PII — list]

5. CATEGORIES OF DATA SUBJECTS
   [Who the data subjects are]

6. OBLIGATIONS AND RIGHTS OF THE CONTROLLER
   [Controller's role; obligation to provide lawful instructions]

7. OBLIGATIONS OF THE PROCESSOR
   7.1 Process only on documented instructions
   7.2 Confidentiality obligations on personnel
   7.3 Security measures (reference to Schedule / Annex)
   7.4 Sub-processor engagement (general authorisation with notification)
   7.5 Data subject rights assistance
   7.6 Security, breach notification, DPIA assistance
   7.7 Return or deletion of PII upon termination
   7.8 Audit and inspection cooperation

8. INTERNATIONAL TRANSFERS
   [Transfer mechanism: adequacy / SCCs — reference to applicable schedule]

9. SUB-PROCESSORS
   [Current sub-processor list — Schedule A / Annex I]
   [Notification mechanism for changes]

10. SECURITY MEASURES
    [Schedule of technical and organisational measures — Schedule B / Annex II]

11. DURATION AND TERMINATION
    [Aligned to service agreement; obligations on termination]

12. GOVERNING LAW AND JURISDICTION

SCHEDULES
Schedule A: Sub-processor List
Schedule B: Technical and Organisational Security Measures
[Schedule C: Standard Contractual Clauses (if international transfer applies)]
```

---

## 4. Infringing Instruction Register

Records all infringing instruction events. Maintained by DPO. Classified RESTRICTED.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Event ID | Text | Unique reference (e.g., INF-2026-001) |
| Customer Name | Text | Customer (controller) who issued the instruction |
| Date Instruction Received | Date | Date [Organisation] received the instruction |
| Instruction Description | Text | Description of the instruction and the proposed processing |
| Nature of Concern | Text | Which legal requirement the instruction would infringe and how |
| DPO Assessment Date | Date | Date DPO completed assessment |
| Legal/Compliance Input | Boolean | Yes / No |
| Customer Notification Date | Date | Date DPO notified customer in writing |
| Customer Response | Text | Summary of customer's response |
| Customer Response Date | Date | Date of customer response |
| Resolution | Enum | Customer Withdrew Instruction / Instruction Revised / Instruction Maintained / Engagement Suspended / Engagement Terminated |
| Resolution Date | Date | Date resolution was reached |
| DPO Notes | Text | Assessment reasoning, escalation records |

---

## 5. Customer Compliance Support Register

Tracks compliance documentation provided to each customer. Maintained by DPO.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Record ID | Text | Unique reference (e.g., CSR-2026-001) |
| Customer Name | Text | Customer receiving the documentation |
| DPA Reference | Text | Linked Processor Agreement Register entry |
| Document / Information Provided | Text | Description of what was provided (e.g., "ISO 27001 certificate", "Sub-processor list", "Pen test summary Q1 2026") |
| Request Date | Date | Date customer requested the documentation (if applicable) |
| Provision Date | Date | Date documentation was sent to customer |
| Method of Provision | Text | Email / Secure portal / Physical |
| DPO Confirmed | Boolean | Yes / No |
| Notes | Text | Confidentiality conditions, redactions, follow-up actions |

---

## 6. Processor RoPA (Article 30(2))

The processor-side RoPA. One entry per category of processing carried out on behalf of customers. Maintained by DPO.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Activity ID | Text | Unique reference (e.g., PROPA-001) |
| Processing Category | Text | Category of processing (e.g., "Cloud-hosted CRM data storage", "Email delivery for customer communications") |
| Customer Name(s) | Text | Customers for whom this processing is performed (may be by category if confidential) |
| Nature of Processing | Text | What [Organisation] does with the PII |
| PII Categories | Text | Categories of PII processed |
| Data Subject Categories | Text | Categories of individuals |
| Purpose (as instructed) | Text | Purpose per customer instruction |
| Sub-processors Used | Text | Sub-processors involved in this processing category |
| International Transfers | Boolean | Yes / No |
| Transfer Destinations | Text | Countries to which PII is transferred |
| Transfer Mechanism | Text | Adequacy / SCCs / BCRs |
| Security Measures Summary | Text | High-level description of TOM applied |
| Last Updated | Date | Date this entry was last reviewed |

---

<!-- QA_VERIFIED: [Date] -->
