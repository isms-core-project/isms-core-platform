<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.5.39:sec:POL:a.5.39 -->
**CLD-SEC-POL-A.5.39 — Agreement on the Roles and Responsibilities of the Cloud Service Partner**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Agreement on the Roles and Responsibilities of the Cloud Service Partner |
| **Document Type** | Policy |
| **Document ID** | CLD-SEC-POL-A.5.39 |
| **Document Creator** | CISO / Cloud Security Manager |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial policy for ISO/IEC 27017:2026 Ed. 2 implementation |

**Review Cycle**: Annual (or upon onboarding/change of a cloud service partner, or following any scope-conflict escalation)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Cloud Security Manager
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management

**Related Documents**:

- CLD-SEC-POL-A.5.38 (Shared Roles and Responsibilities within a Cloud Computing Environment — the CSC/CSP allocation this policy must remain consistent with)
- ISMS-POL-A.5.19-23-S1 (Supplier Relationship Fundamentals)
- ISMS-POL-A.5.19-23-S2 (Supplier Agreement Requirements)
- ISMS-POL-A.5.19-23-S5 (Cloud Services Security)
- CLD-SEC-IMP-A.5.39-TG (Agreement on Cloud Service Partner Roles and Responsibilities — Technical Guide, holds the full CSN Role Register and consistency-check schemas)
- CLD-SEC-REF-A.5-A.8 (Cloud Security Guidance Addendum)
- ISO/IEC 27017:2026, Clause 5.39 (CLD — Agreement on the roles and responsibilities of the cloud service partner)
- ISO/IEC 22123-3 (Cloud computing — Reference architecture)

---

## Executive Summary

This policy establishes how [Organisation] classifies, defines, and agrees the information security roles and responsibilities of any **cloud service partner (CSN)** it engages or is engaged by, in accordance with ISO/IEC 27017:2026, Clause 5.39.

**Scope**: All cloud service partners — third parties whose activities support or are auxiliary to [Organisation]'s cloud service customer (CSC) role, [Organisation]'s cloud service provider (CSP) role, or both. Per ISO/IEC 22123-3, a CSN's activities typically fall into one or more of three sub-roles: cloud service developer, cloud auditor, and cloud service broker.

**Extended Control Note**: ISO/IEC 27017:2026, Clause 5.39 is one of four cloud-specific "CLD" extended controls introduced by the standard's second edition (alongside 5.38, 8.35, and 8.36). It is entirely new — it has no equivalent in the 2015 first edition of ISO/IEC 27017 and no direct equivalent in ISO/IEC 27002:2022. [Organisation] implements it as an informative extension to its ISO/IEC 27001:2022-based ISMS.

**Relationship to CLD-SEC-POL-A.5.38**: The CSC and the CSP already have shared roles and responsibilities between them under CLD-SEC-POL-A.5.38. Any agreement [Organisation] reaches with a cloud service partner SHALL be consistent with that pre-existing shared allocation — a CSN agreement cannot reassign a responsibility away from the CSC or the CSP without both of their consent. A CSN engagement that would create such a reassignment is treated as an information security risk requiring escalation before signature, not a matter to be resolved after the fact.

---

# Scope and Applicability

## ISO/IEC 27017:2026 — Clause 5.39

**Control statement (ISO/IEC 27017:2026, 5.39):**
> "Information security roles and responsibilities of the CSN should be defined and agreed with the CSC or CSP that uses the CSN's service."

**Purpose (ISO/IEC 27017:2026, 5.39):**
> "To delineate the roles and responsibilities of the CSC and the CSP when using a CSN."

## Cloud Service Partner Sub-Roles (per ISO/IEC 22123-3)

| Sub-role | Description | Typical [Organisation] Examples |
|----------|-------------|-----------------------------------|
| **Cloud service developer** | Designs, develops, tests, or maintains components used to deliver a cloud service | Contracted engineering firm building a module used in a delivered service; managed CI/CD pipeline provider |
| **Cloud auditor** | Performs independent assessment of cloud service operation, controls, or compliance | External ISO/IEC 27001 or SOC 2 auditor; independent penetration testing firm |
| **Cloud service broker** | Manages the use, performance, or delivery of cloud services, and negotiates relationships between CSCs and CSPs | Cloud reseller; managed service provider aggregating multiple CSPs on [Organisation]'s behalf |

A CSN may hold a single sub-role, several sub-roles, or — in some engagements — act as a stand-alone CSN in one relationship while acting as a CSP in another. [Organisation] SHALL determine and document which sub-role(s) apply for each cloud service partner it engages, using the classification procedure in CLD-SEC-IMP-A.5.39-UG, Part 1.

## Applicability

This policy applies to:

- All third parties [Organisation] engages, in either its CSC or CSP capacity, whose activities meet the ISO/IEC 22123-3 definition of a cloud service partner (developer, auditor, or broker sub-role)
- All internal teams responsible for selecting, contracting, or overseeing such partners

---

# Policy Statements: Agreement on Cloud Service Partner Roles (5.39)

## Classifying and Agreeing the CSN's Roles

[Organisation] SHALL, before a cloud service partner begins any activity affecting a cloud service [Organisation] consumes (as CSC) or delivers (as CSP):

- Classify the third party against the three ISO/IEC 22123-3 sub-roles, and confirm whether the engagement also independently makes the third party a CSP in its own right (in which case CLD-SEC-POL-A.5.38 additionally applies to that portion of the relationship)
- Clearly define the roles and responsibilities the CSN is expected to assume, tied to its classified sub-role(s), before contract negotiation concludes
- Retrieve and check the CSN's proposed responsibilities against the Shared Responsibility Matrix (CLD-SEC-IMP-A.5.38-TG, Section 1) for the cloud service relationship the CSN will support
- Reach written agreement with the CSN on those roles and responsibilities before the CSN begins work — an informal or verbal understanding does not satisfy this requirement
- Where the consistency check identifies a conflict with the existing CSC/CSP allocation, obtain the counterparty's (CSC's or CSP's) written consent before proceeding, or decline the engagement

## Contractual Requirements

Every cloud service partner engagement in scope of this policy SHALL be governed by a written agreement, negotiated per ISMS-POL-A.5.19-23-S2 (Supplier Agreement Requirements), that at minimum:

- Identifies the CSN's sub-role(s) (developer, auditor, broker, or combination)
- States the specific information security responsibilities assigned to the CSN, as contract text — not as an informal side understanding
- Confirms the CSN's obligations do not conflict with [Organisation]'s existing CSC/CSP shared responsibility commitments, referencing the consistency check performed

## Communicating Agreed Roles

[Organisation] SHALL communicate the CSN's agreed roles and responsibilities to the internal teams who work with the CSN (Cloud Service Delivery, Engineering, relevant project staff) via the CSN Role Register and the organisation's information security awareness programme (see ISMS-POL-A.6.3), and to the CSN's own operational personnel via the signed agreement, supplemented by a joint responsibility discussion for engagements with information-security-relevant scope.

## CSN Role Register — Minimum Content

The CSN Role Register (full schema in CLD-SEC-IMP-A.5.39-TG, Section 1) SHALL record, per cloud service partner, at minimum: the CSN's name; its classified sub-role(s) and whether it also independently acts as a CSP; the responsibilities assigned to it; the related cloud service relationship and Shared Responsibility Matrix reference; the agreement reference and date; the outcome of the consistency check; and the date of last review. The register SHALL be maintained by the Cloud Security Manager and reviewed at least annually.

## Ongoing Oversight and Scope Changes

[Organisation] SHALL:

- Review the CSN Role Register at least annually, confirming each CSN's classification, agreed responsibilities, and continued consistency with the relevant Shared Responsibility Matrix remain accurate
- Re-assess classification and consistency, and amend the agreement accordingly, whenever a CSN's actual activity materially changes from its originally agreed scope
- Escalate to the Cloud Security Manager, and where unresolved to the CISO, any instance where a CSN's activity is found to exceed its agreed scope, treating this as an information security risk requiring assessment, not merely a contractual housekeeping item

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Owns CLD-SEC-POL-A.5.39; approves CSN engagements with information-security-relevant scope; resolves conflicts between CSN agreements and existing CSC/CSP allocations; reviews CSN-related risk escalations |
| **Cloud Security Manager** | Classifies each prospective CSN by sub-role; performs and records the consistency check against the applicable Shared Responsibility Matrix before the CSN agreement is signed; maintains the CSN Role Register; reports CSN coverage metrics to the CISO |
| **Legal/Compliance Officer** | Negotiates and executes CSN agreements per ISMS-POL-A.5.19-23-S2; ensures agreed roles and responsibilities are captured in contract text |
| **Cloud Service Delivery / Engineering** | Operates within the boundaries of the CSN's agreed roles; escalates any CSN activity exceeding its agreed scope |

---

# Evidence Requirements

| Evidence | Description | Owner | Retention |
|---------|-------------|-------|-----------|
| CSN Role Register | List of all active cloud service partners with assigned sub-role(s), scope, and agreement reference | Cloud Security Manager | Current + 3 years from engagement end |
| CSN Agreement Extracts | Extract of each CSN's written agreement stating agreed roles and responsibilities | Legal/Compliance Officer | Duration of agreement + 3 years |
| Consistency Check Records | Records confirming each CSN agreement was checked against the applicable Shared Responsibility Matrix before signature, including outcome and any counterparty consent obtained | Cloud Security Manager | Current + 3 years |
| Scope-Change Amendment Records | Records of CSN scope re-classification and agreement amendment where a CSN's activity materially changed | Cloud Security Manager | Current + 3 years |
| CSN Risk Escalation Records | Records of any CSN-related conflict or scope exceedance escalated into the risk assessment and treatment process, with resolution | CISO | Current + 3 years |

---

# Monitoring and Metrics

The Cloud Security Manager reports the following to the CISO at least quarterly:

- Proportion of active cloud service partners with a current, classified CSN Role Register entry and a completed consistency check
- Number of CSN engagements where a conflict with the existing CSC/CSP allocation was identified, and how it was resolved
- Number of scope-exceedance escalations and their resolution status

---

# Audit Considerations

Auditors verifying compliance with CLD-SEC-POL-A.5.39 should expect to find:

- A CSN Role Register covering every third party meeting the ISO/IEC 22123-3 cloud service partner definition
- Written agreements that explicitly state the CSN's assigned sub-role(s) and information security responsibilities
- Documented evidence that each CSN agreement was cross-checked against the relevant Shared Responsibility Matrix under CLD-SEC-POL-A.5.38 before execution, including how any conflicts were resolved
- Evidence that scope changes triggered re-classification and agreement amendment, not silent drift
- Quarterly monitoring metrics demonstrating active oversight, not a one-time onboarding exercise

---

<!-- QA_VERIFIED: 2026-08-01 -->
