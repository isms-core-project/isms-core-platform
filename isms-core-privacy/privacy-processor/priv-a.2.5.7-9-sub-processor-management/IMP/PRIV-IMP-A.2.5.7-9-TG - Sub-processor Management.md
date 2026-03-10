<!-- ISMS-CORE:IMP:PRIV-IMP-A.2.5.7-9-TG:privacy:TG:a.2.5.7-9 -->
**PRIV-IMP-A.2.5.7-9-TG — Sub-processor Management — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Sub-processor Management — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.2.5.7-9-TG |
| **Related Policy** | PRIV-POL-A.2.5.7-9 (Sub-processor Management) |
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

- PRIV-POL-A.2.5.7-9 (Sub-processor Management — the governing policy)
- PRIV-IMP-A.2.5.7-9-UG (Sub-processor Management — User Guide)
- PRIV-IMP-A.2.2.2-7-TG (Processor Agreements — Processor Agreement Register)

---

## Purpose of This Guide

This guide provides the **technical structures, register schemas, and templates** for sub-processor management. It covers:

- Sub-processor Register schema
- Sub-processor Agreement Clause Checklist
- Sub-processor Due Diligence Record schema
- Sub-processor Change Notification Log schema
- Sub-processor List (Customer-Facing) template

**Audience**: DPO, Legal/Compliance, Procurement.

---

## 1. Sub-processor Register

The authoritative list of all sub-processors engaged by [Organisation] to process customer PII. Maintained by DPO. Published or made available to customers.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Sub-processor ID | Text | Unique reference (e.g., SP-001) |
| Sub-processor Name | Text | Legal entity name |
| Parent Company (if applicable) | Text | Parent group or holding company |
| Jurisdiction | Text | Country of incorporation and data processing location(s) |
| Data Processing Location(s) | Text | Specific countries/regions where PII is processed (including DR) |
| Transfer Mechanism | Enum | Adequacy / SCCs Module 3 / BCRs / Other |
| SCC Reference (if applicable) | Text | Reference to the SCC appendix in the sub-processor agreement |
| Nature of Processing | Text | What the sub-processor does with customer PII |
| PII Categories Processed | Text | Categories of customer PII the sub-processor accesses |
| Data Subject Categories | Text | Whose data (e.g., customer's end-users, employees) |
| Applicable Services | Text | Which [Organisation] services use this sub-processor |
| Sub-processor Agreement Ref | Text | Reference to the executed sub-processor DPA |
| Agreement Execution Date | Date | Date sub-processor DPA was signed |
| Agreement Review Date | Date | Next scheduled agreement review |
| Customer Disclosure Method | Enum | Processor Agreement Appendix / Published URL / Both |
| First Disclosed Date | Date | Date this sub-processor was first disclosed to customers |
| Due Diligence Record Ref | Text | Linked due diligence record |
| Due Diligence Last Completed | Date | Date of most recent due diligence |
| Status | Enum | Active / Decommissioned / Under Review |
| Notes | Text | Pending changes, escalations, contractual notes |

---

## 2. Sub-processor Agreement Clause Checklist

Use when reviewing a new sub-processor agreement for Article 28(4) compliance — the agreement must impose the same obligations on the sub-processor as [Organisation]'s own processor agreement with its customers.

```
SUB-PROCESSOR AGREEMENT COMPLIANCE CHECKLIST

Sub-processor: _____________________________________________
Agreement Reference: _____________________________________________
Reviewer: _____________________________________________
Date: _____________________________________________

MANDATORY CLAUSES (must mirror [Organisation]'s main processor agreement obligations)

[ ] 1. Processing only on [Organisation]'s documented instructions
        — including prohibition on own-purpose use
        Agreement clause: _____________________________________________

[ ] 2. Personnel confidentiality obligations
        — persons processing PII are subject to confidentiality
        Agreement clause: _____________________________________________

[ ] 3. Appropriate technical and organisational security measures
        — equivalent to GDPR Article 32 standard
        Agreement clause: _____________________________________________

[ ] 4. Sub-sub-processor restrictions
        — sub-processor may not engage further sub-processors without [Organisation]'s
          prior written authorisation; same obligations imposed on any sub-sub-processors
        Agreement clause: _____________________________________________

[ ] 5. Assistance with data subject rights
        — sub-processor assists [Organisation] in fulfilling data subject rights
          (access, rectification, erasure, restriction, portability, objection)
        Agreement clause: _____________________________________________

[ ] 6. Breach notification to [Organisation] without undue delay
        — enables [Organisation] to meet its own breach notification obligations to customers
        Agreement clause: _____________________________________________

[ ] 7. Return or deletion of PII at end of engagement
        — at [Organisation]'s choice; confirmation of deletion provided
        Agreement clause: _____________________________________________

[ ] 8. Cooperation with [Organisation]'s audits and inspections
        — sub-processor makes available information demonstrating compliance;
          supports on-site audits where required
        Agreement clause: _____________________________________________

[ ] 9. International transfer compliance
        — if sub-processor transfers PII to a further third country, appropriate
          mechanism is in place (adequacy, SCCs Module 3-to-3, etc.)
        Agreement clause: _____________________________________________

CONCLUSION
[ ] Agreement is compliant — all mandatory clauses present; proceed with execution
[ ] Agreement requires the following amendments before execution:
    _____________________________________________

DPO: _________________________ Date: _____________
Legal/Compliance: _________________________ Date: _____________
```

---

## 3. Sub-processor Due Diligence Record

Completed before engaging a new sub-processor. Filed by Procurement with DPO copy. Maintained per sub-processor.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| DDR ID | Text | Unique reference (e.g., SPDD-001) |
| Sub-processor Name | Text | Name of the sub-processor assessed |
| Assessment Date | Date | Date due diligence was completed |
| Assessed By | Text | Role / person completing the assessment |
| ISO 27001 Certified | Enum | Yes (cert ref + expiry) / No / Pending |
| SOC 2 Type II Available | Enum | Yes (report date) / No / Not Applicable |
| Security Questionnaire Completed | Boolean | Yes / No |
| Questionnaire Response Summary | Text | Summary of key security posture findings |
| Data Centre Locations Confirmed | Text | Jurisdictions confirmed by the sub-processor |
| Breach History | Text | Any known data breaches or incidents disclosed |
| Risk Assessment Outcome | Enum | Low Risk / Medium Risk / High Risk |
| Risk Rationale | Text | Summary basis for risk rating |
| Conditions for Approval | Text | Any conditions attached to proceeding (e.g., specific contractual requirements) |
| DPO Approval | Boolean | Yes / No |
| DPO Approval Date | Date | Date DPO approved engagement |
| Next Review Date | Date | Date scheduled for next due diligence review |
| Notes | Text | Open items, follow-up requirements |

---

## 4. Sub-processor Change Notification Log

Records all customer notifications regarding sub-processor changes (additions and replacements). Maintained by DPO / Customer Success.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Notification ID | Text | Unique reference (e.g., SPCN-2026-001) |
| Change Type | Enum | Addition / Replacement / Decommission |
| Sub-processor Affected | Text | Name of new or departing sub-processor |
| Replacement Sub-processor (if applicable) | Text | Name of the incoming replacement |
| Change Rationale | Text | Brief reason for the change |
| Planned Effective Date | Date | When the change will take effect |
| Notification Sent Date | Date | Date notification was sent to customers |
| Customers Notified | Text | List or category of customers notified |
| Notification Content Summary | Text | Brief summary of what was communicated |
| Objection Deadline | Date | Last date for customers to object |
| Objections Received | Boolean | Yes / No |
| Objecting Customers | Text | Names of customers who objected |
| Objection Resolution | Text | How each objection was resolved |
| Change Proceeded | Boolean | Yes / No |
| Actual Effective Date | Date | Date change was implemented |
| Sub-processor Register Updated | Boolean | Yes / No |
| Transfer Destination Register Updated | Boolean | Yes / No / Not Applicable |
| Notes | Text | Exceptional circumstances, legal drivers |

---

## 5. Sub-processor List (Customer-Facing Template)

This is the version of the sub-processor list published to or provided to customers. Personal and commercially sensitive operational details are excluded. Maintained by DPO, published or provided per processor agreement.

```
[ORGANISATION] — SUB-PROCESSOR LIST
Last Updated: [Date] | Version: [X.X]

This list identifies the sub-processors engaged by [Organisation] to assist in
providing services to customers. Sub-processors may access customer personal data
in the course of delivering these services.

Changes to this list are communicated to customers in advance per the notification
process described in our Data Processing Agreement.

---

| Sub-processor | Location | Processing Activity | PII Categories |
|---------------|----------|---------------------|----------------|
| [Name] | [Country] | [e.g., Cloud infrastructure hosting] | [e.g., All customer PII stored on the platform] |
| [Name] | [Country] | [e.g., Transactional email delivery] | [e.g., Email address, name] |
| [Name] | [Country] | [e.g., Customer support platform] | [e.g., Account data, support ticket content] |

---

For the current version of this list, or to raise an objection to a sub-processor
change, contact: privacy@[domain]

[Organisation Legal Name] | [Date]
```

---

<!-- QA_VERIFIED: [Date] -->
