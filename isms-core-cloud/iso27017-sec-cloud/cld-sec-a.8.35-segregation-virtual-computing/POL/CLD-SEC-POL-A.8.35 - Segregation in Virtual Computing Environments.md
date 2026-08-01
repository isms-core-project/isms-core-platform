<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.8.35:sec:POL:a.8.35 -->
**CLD-SEC-POL-A.8.35 — Segregation in Virtual Computing Environments**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Segregation in Virtual Computing Environments |
| **Document Type** | Policy |
| **Document ID** | CLD-SEC-POL-A.8.35 |
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

**Review Cycle**: Annual (or upon significant change to virtualisation architecture, or following a segregation-related incident)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Cloud Security Manager
- Technical: Cloud Engineering Lead
- Final Authority: Executive Management

**Related Documents**:

- ISMS-POL-A.8.20-22 (Network Security — parent ISMS policy for A.8.22 segregation of networks)
- CLD-SEC-POL-A.5.38 (Shared Roles and Responsibilities within a Cloud Computing Environment)
- CLD-SEC-POL-A.8.36 (Detection and Prevention of Unauthorised Use of Cloud Services)
- CLD-SEC-IMP-A.8.35-TG (Segregation in Virtual Computing Environments — Technical Guide, holds the full segregation schemas and architecture template)
- CLD-SEC-REF-A.5-A.8 (Cloud Security Guidance Addendum)
- ISO/IEC 27017:2026, Clause 8.35 (CLD — Segregation in virtual computing environments)
- ISO/IEC 27040 (Storage security)

---

## Executive Summary

This policy establishes how [Organisation] protects tenant environments from unauthorised access within multi-tenant virtual computing environments, in accordance with ISO/IEC 27017:2026, Clause 8.35.

**Scope**: All virtual computing environments in which [Organisation] operates in a multi-tenant cloud service — whether [Organisation]'s own virtual environment running on a third-party CSP's cloud service (CSC role), or the multi-tenant infrastructure [Organisation] operates for its own CSCs (CSP role).

**Extended Control Note**: ISO/IEC 27017:2026, Clause 8.35 is one of four cloud-specific "CLD" extended controls introduced by the standard's second edition (alongside 5.38, 5.39, and 8.36). It is thematically closest to — and implemented alongside — the network segregation obligations of ISO/IEC 27001:2022 Annex A control 8.22, but addresses logical segregation of virtualized applications, storage, and network resources specifically, not only network traffic.

**Core Risk**: Inadequate segregation in a shared virtual computing environment can expose one tenant's data or workloads to another tenant, to third parties, or to unauthorised CSP personnel. Because tenant isolation is largely invisible to the CSC, [Organisation] must define its segregation requirements explicitly (as CSC) and enforce logical segregation rigorously (as CSP), rather than assuming isolation is automatically adequate. A segregation gap identified at any point — during onboarding, periodic verification, or testing — is treated as an information security risk requiring assessment, not a configuration note to be revisited later.

---

# Scope and Applicability

## ISO/IEC 27017:2026 — Clause 8.35

**Control statement (ISO/IEC 27017:2026, 8.35):**
> "A CSC's virtual environment running on a cloud service should be protected from unauthorized access."

**Purpose (ISO/IEC 27017:2026, 8.35):**
> "To prevent inappropriate access or disclosure of information through insecure virtualization."

## Applicability

This policy applies to:

- All [Organisation] virtual machine instances, containers, storage volumes, and virtual networks running on a third-party CSP's multi-tenant cloud service (CSC role)
- All multi-tenant virtualized infrastructure [Organisation] operates to deliver cloud services to its own CSCs (CSP role)
- All personnel with administrative access to virtualisation, hypervisor, or container orchestration layers

## Regulatory and Standards Framework

ISO/IEC 27017:2026 is an informative extension to ISO/IEC 27002:2022. Clause 8.35 does not correspond to a numbered ISO/IEC 27002:2022 control; it is new in the 2026 second edition, replacing and broadening the 2015 first edition's CLD.9.5.1 ("Segregation in virtual computing environments"). It is implemented alongside ISO/IEC 27001:2022 Annex A control 8.22 (Segregation of networks) and draws on the secure multi-tenancy guidance in ISO/IEC 27040.

---

# Policy Statements: Segregation in Virtual Computing Environments (8.35)

## Obligations as Cloud Service Customer (CSC)

Where [Organisation] acts as a cloud service customer, [Organisation] SHALL:

- Classify the data and workload to be run on the cloud service by sensitivity, and define its requirements for segregating [Organisation]'s environment to achieve tenant isolation, before the service is selected
- Set a minimum acceptable isolation level appropriate to that classification (e.g. hypervisor-enforced logical isolation for standard workloads, dedicated/single-tenant infrastructure for the most sensitive workloads), and document it in the Segregation Requirements Statement (schema in CLD-SEC-IMP-A.8.35-TG, Section 1)
- Verify, before and periodically during use of the service, that the CSP meets those segregation requirements, using CSP documentation cross-checked against independent assurance (certifications, audit reports) where available
- Re-verify at least annually, and whenever the CSP announces a material change to its virtualisation or multi-tenancy architecture
- Where verification identifies a gap between the CSP's segregation controls and [Organisation]'s stated requirement, treat it as an information security risk and feed it into [Organisation]'s documented risk assessment and treatment process

## Obligations as Cloud Service Provider (CSP)

Where [Organisation] acts as a cloud service provider, [Organisation] SHALL:

- Enforce logical segregation of CSC data, virtualized applications, operating systems, storage, and network resources, to ensure isolation of resources used by different tenants in a multi-tenant environment, documented per layer in the Segregation Architecture Documentation (template in CLD-SEC-IMP-A.8.35-TG, Section 3)
- Assess the risks associated with running CSC-supplied software within the cloud services [Organisation] offers, before permitting such software to run in shared infrastructure, applying compensating controls where the isolation boundary is assessed as insufficient
- Enforce separation of [Organisation]'s own internal administration functions from the resources used by CSCs, through a distinct administrative access path
- Schedule periodic testing of the segregation architecture (e.g. tenant-boundary penetration testing, hypervisor/container isolation configuration audits) to confirm the documented design remains effective in practice, not just correct on paper

## Technology-Dependent Implementation

[Organisation] recognises that the implementation of logical segregation depends on the virtualisation technologies applied. Network and storage configurations may be virtualized through a software virtualisation function that provides a virtual environment (for example, a virtual operating system or container isolation mechanism). Where such software virtualisation is used, [Organisation] SHALL design and implement segregation using the segregation functions native to that software, in addition to underlying physical or network-level controls.

## Legal and Regulatory Considerations

Where applicable laws or regulations require the segregation of networks or the isolation of network traffic for data [Organisation] processes, [Organisation] SHALL ensure its virtual computing segregation controls satisfy those requirements in addition to the baseline requirements of this policy, and confirm this as part of the annual review.

## Communication and Awareness

[Organisation] SHALL communicate segregation requirements and architecture decisions to the internal teams who design, operate, or rely on them (Cloud Engineering, Cloud Service Delivery, Security Operations), through the Segregation Architecture Documentation and inclusion in the organisation's information security awareness programme (see ISMS-POL-A.6.3). Where [Organisation] acts as CSP, the key segregation commitments relevant to a CSC SHALL be communicated to that CSC through onboarding materials or service documentation.

## Segregation Requirements Statement — Minimum Content

The Segregation Requirements Statement (full schema in CLD-SEC-IMP-A.8.35-TG, Section 1) SHALL record, per cloud service consumed: the service identifier; the data/workload classification; the minimum acceptable isolation level and its justification; and the date the requirement was defined.

## Segregation Architecture Documentation — Minimum Content

The Segregation Architecture Documentation (full template in CLD-SEC-IMP-A.8.35-TG, Section 3) SHALL record, per multi-tenant environment [Organisation] operates: the segregation mechanism applied at each layer (CSC data, virtualized applications, operating systems, storage, network); the design of the internal administration separation; and a summary of the most recent segregation testing and its results.

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Owns CLD-SEC-POL-A.8.35; approves the segregation architecture for multi-tenant environments [Organisation] operates (CSP role); approves acceptance of a CSP's segregation controls for critical workloads (CSC role); reviews segregation-related risk escalations |
| **Cloud Security Manager** | Defines segregation requirements for services consumed (CSC role); verifies CSP segregation controls periodically; reports segregation verification and testing metrics to the CISO |
| **Cloud Engineering Lead** | Designs and implements logical segregation controls (hypervisor, container, storage, network) for multi-tenant environments [Organisation] operates (CSP role); schedules and reviews periodic segregation testing |
| **Cloud Service Delivery / Engineering** | Assesses risk of CSC-supplied software before permitting execution in shared infrastructure; maintains separation of internal administration access from CSC resources |

---

# Evidence Requirements

| Evidence | Description | Owner | Retention |
|---------|-------------|-------|-----------|
| Segregation Requirements Statement (CSC role) | [Organisation]'s documented tenant isolation requirements for each cloud service consumed | Cloud Security Manager | Current + 3 years |
| CSP Segregation Verification Records | Records of periodic verification that a CSP's segregation controls meet [Organisation]'s requirements | Cloud Security Manager | Current + 3 years |
| Segregation Architecture Documentation (CSP role) | Technical documentation of logical segregation controls implemented across virtualized applications, storage, and network | Cloud Engineering Lead | Current version + previous versions for 3 years |
| CSC-Supplied Software Risk Assessments | Records of risk assessments performed before permitting CSC-supplied software to run in shared infrastructure | Cloud Service Delivery / Engineering | Current + 3 years |
| Segregation Testing Records | Results of periodic tenant-boundary testing and isolation configuration audits | Cloud Engineering Lead | Current + 3 years |
| Segregation Gap / Risk Records | Records of any segregation gap escalated into the risk assessment and treatment process, with resolution | CISO | Current + 3 years |

---

# Monitoring and Metrics

The Cloud Security Manager reports the following to the CISO at least quarterly:

- Proportion of cloud services (CSC role) with a current segregation verification within the last 12 months
- Results and remediation status of the most recent segregation testing (CSP role)
- Number of segregation gaps identified and escalated into the risk assessment and treatment process, and their resolution status

---

# Audit Considerations

Auditors verifying compliance with CLD-SEC-POL-A.8.35 should expect to find:

- Documented segregation requirements for every cloud service [Organisation] consumes as a CSC
- Evidence of periodic verification that CSP segregation controls meet those requirements, and of gaps being escalated as risks rather than left open
- Technical documentation of the logical segregation architecture for any multi-tenant environment [Organisation] operates as a CSP, covering data, virtualized applications, operating systems, storage, and network
- Evidence that [Organisation]'s internal administration access is separated from CSC-facing resources
- Risk assessment records for CSC-supplied software run within [Organisation]'s shared infrastructure
- Records of periodic segregation testing, not just a one-time architecture design review

---

<!-- QA_VERIFIED: 2026-08-01 -->
