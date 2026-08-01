<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.5.38:sec:POL:a.5.38 -->
**CLD-SEC-POL-A.5.38 — Shared Roles and Responsibilities within a Cloud Computing Environment**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Shared Roles and Responsibilities within a Cloud Computing Environment |
| **Document Type** | Policy |
| **Document ID** | CLD-SEC-POL-A.5.38 |
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

**Review Cycle**: Annual (or upon significant change to cloud service model or supplier relationships, or following any shared-responsibility incident or dispute)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Cloud Security Manager
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management

**Related Documents**:

- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles — parent ISMS policy for A.5.2 roles and responsibilities)
- ISMS-POL-A.5.19-23-S5 (Cloud Services Security — parent ISMS cloud policy)
- CLD-SEC-POL-A.5.39 (Agreement on the Roles and Responsibilities of the Cloud Service Partner — governs cascading of these responsibilities to cloud service partners)
- CLD-SEC-POL-A.8.35 (Segregation in Virtual Computing Environments)
- CLD-SEC-POL-A.8.36 (Detection and Prevention of Unauthorised Use of Cloud Services)
- CLD-SEC-IMP-A.5.38-TG (Shared Roles and Responsibilities — Technical Guide, holds the full Shared Responsibility Matrix schema)
- CLD-SEC-REF-A.5-A.8 (Cloud Security Guidance Addendum)
- ISO/IEC 27017:2026, Clause 5.38 (CLD — Shared roles and responsibilities within a cloud computing environment)
- ISO/IEC 27002:2022 (Information security controls)
- ISO/IEC 22123-3 (Cloud computing — Reference architecture)

---

## Executive Summary

This policy establishes how [Organisation] allocates, documents, communicates, and implements information security roles and responsibilities in every cloud computing relationship it participates in, in accordance with ISO/IEC 27017:2026, Clause 5.38.

**Scope**: All cloud services in which [Organisation] participates — whether as a cloud service customer (CSC) consuming a third-party cloud service, or as a cloud service provider (CSP) delivering a cloud service to its own customers. Where [Organisation] holds both roles simultaneously (for example, building on a CSP's infrastructure to deliver its own cloud service), this policy applies to each role independently. It covers public, private, hybrid, and multi-cloud deployments across IaaS, PaaS, and SaaS models, including layered relationships where responsibilities cascade through a supply chain.

**Extended Control Note**: ISO/IEC 27017:2026, Clause 5.38 is one of four cloud-specific "CLD" extended controls introduced by the standard's second edition (alongside 5.39, 8.35, and 8.36) that have no direct equivalent in ISO/IEC 27002:2022 or ISO/IEC 27001:2022 Annex A. [Organisation] implements it as an informative extension to its ISO/IEC 27001:2022-based ISMS, consistent with how ISO/IEC 27017:2026 itself frames these controls.

**Core Principle**: Information security in cloud computing is never solely the CSP's responsibility or solely the CSC's responsibility — it is shared, and the shared allocation must be identified, documented, communicated, and implemented by both parties before it can be relied upon. Ambiguity in that allocation is treated as an information security risk, not a formality to be resolved later.

---

# Scope and Applicability

## ISO/IEC 27017:2026 — Clause 5.38

**Control statement (ISO/IEC 27017:2026, 5.38):**
> "Responsibilities for shared information security roles in the use of the cloud service should be allocated to identified parties, documented, communicated and implemented by both the CSC and the CSP."

**Purpose (ISO/IEC 27017:2026, 5.38):**
> "To clarify the relationship regarding shared roles and responsibilities between the CSC and the CSP for information security management."

## Applicability

This policy applies to:

- All cloud services [Organisation] consumes as a cloud service customer (CSC), across all deployment models (public, private, hybrid, multi-cloud) and service models (IaaS, PaaS, SaaS)
- All cloud services [Organisation] delivers as a cloud service provider (CSP) to its own customers
- All personnel involved in selecting, configuring, operating, or delivering cloud services on [Organisation]'s behalf

## Regulatory and Standards Framework

ISO/IEC 27017:2026 is an informative extension to ISO/IEC 27002:2022, providing cloud-specific guidance for controls the organisation already implements under its ISO/IEC 27001:2022-based ISMS. Clause 5.38 does not correspond to a numbered ISO/IEC 27002:2022 control; it is a new control introduced in the 2026 second edition, thematically closest to — and implemented alongside — the roles and responsibilities obligations of ISO/IEC 27001:2022 Annex A control 5.2.

---

# Policy Statements: Shared Roles and Responsibilities (5.38)

## Obligations as Cloud Service Customer (CSC)

Where [Organisation] acts as a cloud service customer, [Organisation] SHALL:

- Obtain the CSP's proposed allocation of information security roles and responsibilities during service selection and onboarding, and review it against [Organisation]'s own capabilities and risk appetite before the service is put into production use
- Ensure the information security roles and responsibilities of both [Organisation] and the CSP are stated in a written agreement — not left to the CSP's public documentation alone, which can change without notice
- Identify and maintain a named point of contact within the CSP's customer support function for escalation of information security matters
- Request information from the CSP regarding the CSP's information security capabilities — including authentication, cryptography, backup, and logging — and use third-party or independent-body frameworks (e.g. ISO/IEC 27001 certification scope, SOC 2 report, CSA STAR entry) to complement that information where the CSP's own disclosures are insufficient
- Assess any gap between the CSP's proposed allocation and [Organisation]'s ability to fulfil its own allocated responsibilities as an information security risk, feeding it into [Organisation]'s documented risk assessment and treatment process where it cannot be closed before go-live
- Maintain staff awareness of the agreed allocation for cloud services they use, through the organisation's information security awareness programme (see ISMS-POL-A.6.3) and inclusion in cloud architecture review activity

## Obligations as Cloud Service Provider (CSP)

Where [Organisation] acts as a cloud service provider, [Organisation] SHALL:

- Define and document the allocation of information security roles and responsibilities that its CSCs, [Organisation] itself, and [Organisation]'s own suppliers or cloud service partners are each expected to implement
- Communicate the allocation to prospective and existing CSCs before contract signature and after any material change — via the service agreement, customer-facing security documentation, or onboarding materials, as appropriate to the service
- Establish and maintain the relationship with each CSC regarding information security issues, including a defined escalation path documented in the agreement
- Provide CSCs with information regarding the information security capabilities of the cloud service and the information security measures [Organisation] has taken, at a level of clarity sufficient for the CSC to understand them adequately — using recognised third-party or independent-body frameworks where useful to convey this information
- Where the service relies on an underlying CSP (a layered or supply-chain relationship), assess and document how responsibilities cascade, and ensure this is consistent with the agreements [Organisation] holds with its own cloud service partners under CLD-SEC-POL-A.5.39
- Treat a dispute or persistent ambiguity over responsibility allocation, raised by a CSC or identified internally, as an information security event requiring escalation, not a routine support query

## Shared Allocation Principle

Roles and responsibilities in cloud computing are typically divided between the CSC and the CSP. [Organisation] SHALL take into account, when allocating roles and responsibilities in either capacity, the CSC's data and the CSC's applications for which [Organisation] (as CSP) is a custodian, or for which [Organisation] (as CSC) remains accountable notwithstanding the CSP's technical custody.

## Shared Responsibility Matrix — Minimum Content

Every cloud service relationship in scope of this policy SHALL be supported by a current Shared Responsibility Matrix. At minimum, the matrix records, per responsibility area (e.g. authentication, cryptography, backup, logging, patching, network segmentation): which party it is allocated to (CSC, CSP, or shared); what action each party must take to fulfil its portion; whether [Organisation] has confirmed it can fulfil its own allocated portion; and the date of last review. The full schema is maintained in CLD-SEC-IMP-A.5.38-TG, Section 1. The matrix SHALL be reviewed by the Cloud Security Manager before a new cloud service relationship goes into production use, and at least annually thereafter.

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Owns CLD-SEC-POL-A.5.38; approves the shared responsibility allocation for strategic or high-risk cloud service relationships; escalates unresolved allocation gaps to Executive Management; reviews policy effectiveness at management review |
| **Cloud Security Manager** | Reviews CSP-provided role/responsibility documentation for services consumed (CSC role); creates and maintains the role/responsibility documentation published to CSCs for services delivered (CSP role); maintains the Shared Responsibility Matrix for every active relationship; reports allocation-gap and matrix-coverage metrics to the CISO |
| **Legal/Compliance Officer** | Ensures the agreed allocation of roles and responsibilities is reflected in the written agreement with each CSC or CSP counterparty |
| **Cloud Service Delivery / Engineering** | Implements the technical controls corresponding to [Organisation]'s allocated responsibilities; escalates any responsibility [Organisation] cannot fulfil |
| **All Personnel** | Operate only within the roles and responsibilities allocated to their function; report any ambiguity in shared responsibility allocation to the Cloud Security Manager |

---

# Evidence Requirements

| Evidence | Description | Owner | Retention |
|---------|-------------|-------|-----------|
| Shared Responsibility Matrix | Per cloud service relationship, documenting which security responsibilities sit with [Organisation] and which sit with the counterparty (CSC or CSP), per the minimum content above | Cloud Security Manager | Current + 3 years from relationship end |
| Agreement Clauses | Extract of the written agreement stating the agreed roles and responsibilities | Legal/Compliance Officer | Duration of agreement + 3 years |
| Review and Sign-Off Records | Records showing the matrix was actively reviewed and approved before go-live, not passively accepted | Cloud Security Manager | Current + 3 years |
| CSP Capability Disclosures (CSC role) | Records of information requested from and provided by CSPs regarding their security capabilities | Cloud Security Manager | Current + 3 years |
| CSC-Facing Capability Documentation (CSP role) | Documentation published to CSCs describing [Organisation]'s security capabilities and measures | Cloud Security Manager | Current version + previous versions for 3 years |
| Allocation Gap / Risk Records | Records of any allocation gap escalated into the risk assessment and treatment process, with resolution | CISO | Current + 3 years |

> **Retention basis**: 3-year periods align with the retention approach used across the ISMS Core cloud product suite for contract-related and agreement-related evidence.

---

# Monitoring and Metrics

The Cloud Security Manager reports the following to the CISO at least quarterly:

- Proportion of active cloud service relationships (CSC and CSP roles) with a current, reviewed Shared Responsibility Matrix
- Number of allocation gaps identified and escalated into the risk assessment and treatment process, and their resolution status
- Number of disputes or ambiguities over responsibility allocation raised by CSCs or internal teams

The effectiveness of this policy is assessed as part of management review, and after any cloud-related security incident where the shared responsibility allocation is relevant to root cause.

---

# Audit Considerations

Auditors verifying compliance with CLD-SEC-POL-A.5.38 should expect to find:

- A Shared Responsibility Matrix for every active cloud service relationship, in either the CSC or CSP role, meeting the minimum content requirements above
- Written agreements that state, rather than imply, the allocation of information security roles and responsibilities
- Evidence that [Organisation], where acting as CSC, actively reviewed and confirmed the CSP's proposed allocation rather than accepting it by default
- Evidence that [Organisation], where acting as CSP, proactively documented and communicated its allocation to CSCs rather than waiting for CSCs to ask
- Evidence that allocation gaps were fed into the risk assessment and treatment process, not just noted and left open
- Quarterly monitoring metrics demonstrating active oversight of matrix coverage, not a one-time exercise

---

<!-- QA_VERIFIED: 2026-08-01 -->
