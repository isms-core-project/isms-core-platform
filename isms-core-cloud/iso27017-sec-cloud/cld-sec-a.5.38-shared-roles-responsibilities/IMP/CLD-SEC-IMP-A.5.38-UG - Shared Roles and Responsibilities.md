<!-- ISMS-CORE:IMP:CLD-SEC-IMP-A.5.38-UG:sec:UG:a.5.38 -->
**CLD-SEC-IMP-A.5.38-UG — Shared Roles and Responsibilities — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Shared Roles and Responsibilities — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-SEC-IMP-A.5.38-UG |
| **Related Policy** | CLD-SEC-POL-A.5.38 (Shared Roles and Responsibilities within a Cloud Computing Environment) |
| **Document Creator** | CISO / Cloud Security Manager |
| **Document Owner** | Cloud Security Manager |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial user guide for ISO/IEC 27017:2026 Ed. 2 implementation |

**Review Cycle**: Annual (or upon significant change to cloud service model or supplier relationships)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-SEC-POL-A.5.38 (Shared Roles and Responsibilities — the governing policy)
- CLD-SEC-IMP-A.5.38-TG (Shared Roles and Responsibilities — Technical Guide)
- CLD-SEC-POL-A.5.39 (Agreement on the Roles and Responsibilities of the Cloud Service Partner)

---

## Purpose of This Guide

This guide explains how [Organisation] identifies, documents, and communicates shared information security roles and responsibilities in its cloud service relationships, in both the cloud service customer (CSC) and cloud service provider (CSP) capacity, under ISO/IEC 27017:2026, Clause 5.38. It is intended for operational use by teams establishing new cloud service relationships or maintaining existing ones.

**Who this guide is for**: CISO, Cloud Security Manager, Legal/Compliance, Cloud Service Delivery/Engineering.

**Dual-role context**: [Organisation] can hold the CSC role, the CSP role, or both simultaneously depending on the service. This guide is organised by role — apply Part 1 when [Organisation] is the CSC, Part 2 when [Organisation] is the CSP, and Part 3 for ongoing maintenance regardless of role.

---

## Part 1 — Establishing the Shared Responsibility Matrix (CSC Role)

### 1.1 Reviewing the CSP's Proposed Allocation

Before a new cloud service is put into production use, the Cloud Security Manager reviews the CSP's published or contractually stated allocation of information security roles and responsibilities.

**Procedure — reviewing a CSP's proposed allocation:**

1. **Collect the CSP's documentation.** Request the CSP's shared responsibility model documentation, security whitepaper, or equivalent — most CSPs publish this per service tier (IaaS/PaaS/SaaS).
2. **Map to [Organisation]'s requirements.** The Cloud Security Manager maps each responsibility line (e.g. patching, encryption key management, access control configuration, backup) against [Organisation]'s own information security requirements for the data and workload involved.
3. **Identify gaps.** Where the CSP's proposed allocation leaves a responsibility unassigned, or assigns it to [Organisation] without [Organisation] having the capability to fulfil it, this is a gap that must be resolved before go-live — either by requesting a CSP capability, engaging a compensating control, or reconsidering the service selection.
4. **Confirm fulfilment capability.** The Cloud Security Manager confirms, in writing, that [Organisation] can fulfil every responsibility allocated to it before the service is approved for production use.
5. **Record the Shared Responsibility Matrix.** Complete the matrix using the schema in CLD-SEC-IMP-A.5.38-TG, Section 1.

### 1.2 Requiring the Allocation in the Written Agreement

The Legal/Compliance Officer ensures the agreed allocation of roles and responsibilities is reflected in the written agreement with the CSP — not left solely to the CSP's public documentation, which can change without notice to [Organisation].

**Minimum agreement content:**

- Reference to the specific service tier and the shared responsibility model version applicable at contract signature
- [Organisation]'s point of contact for information security matters within the CSP's customer support function
- The CSP's commitment to notify [Organisation] of material changes to the shared responsibility allocation

### 1.3 Requesting CSP Capability Information

The Cloud Security Manager requests information from the CSP regarding its information security capabilities — at minimum: authentication mechanisms, cryptographic capabilities, backup capabilities, and logging capabilities — as part of onboarding any new cloud service.

Where the CSP's own disclosures are insufficient to assess a capability, the Cloud Security Manager uses third-party or independent-body frameworks (for example, published CSP certifications, CSA STAR entries, or SOC 2 reports) to complement the assessment, per CLD-SEC-POL-A.5.38.

---

## Part 2 — Documenting and Publishing the Allocation (CSP Role)

### 2.1 Defining the Allocation for a Delivered Service

Where [Organisation] delivers a cloud service to its own CSCs, the Cloud Security Manager defines and documents the allocation of information security roles and responsibilities among the CSC, [Organisation] (as CSP), and any suppliers to [Organisation] involved in delivering the service.

**Procedure — defining the allocation for a new or changed service:**

1. **Enumerate the service's security-relevant responsibilities** (e.g. tenant data encryption, access control configuration, patching of the underlying platform, logging, incident notification).
2. **Assign each responsibility** to the CSC, to [Organisation], or as shared — using the Shared Responsibility Matrix schema in CLD-SEC-IMP-A.5.38-TG, Section 1.
3. **Validate against suppliers.** Where [Organisation] itself relies on suppliers (e.g. an underlying IaaS provider) to deliver the service, confirm the allocation is consistent with the responsibilities those suppliers have accepted toward [Organisation].
4. **Publish CSC-facing documentation.** Produce the capability and responsibility documentation described in Part 2.2 for distribution to CSCs.

### 2.2 Publishing CSC-Facing Capability Documentation

[Organisation] provides CSCs with information about its information security capabilities and measures at a level of clarity sufficient for the CSC to understand them adequately, without disclosing internal architecture details that would create a security risk if disclosed.

**Content requirements** (template in CLD-SEC-IMP-A.5.38-TG, Section 2):

- Summary of authentication, cryptography, backup, and logging capabilities relevant to the CSC
- The CSC-facing statement of the shared responsibility allocation for the service tier
- Reference to any third-party or independent-body framework [Organisation] uses to substantiate its capabilities (certifications, audit reports)

### 2.3 Maintaining the Customer Support Relationship

The Cloud Security Manager establishes and maintains a defined point of contact and escalation path for CSCs raising information security issues related to the shared responsibility allocation, and ensures this is documented in the CSC-facing materials.

---

## Part 3 — Ongoing Maintenance (Both Roles)

### 3.1 Review Triggers

The Shared Responsibility Matrix for a given cloud service relationship is reviewed:

- Annually, at minimum, as part of the standard policy review cycle
- Whenever the CSP (in the CSC relationship) or [Organisation] (in the CSP relationship) materially changes the service tier, architecture, or published shared responsibility model
- Whenever a security incident reveals that the actual allocation of responsibility did not match the documented allocation

### 3.2 Escalation of Allocation Gaps

Where a gap in the shared responsibility allocation is identified — a responsibility that neither party has clearly accepted, or that [Organisation] cannot fulfil — the Cloud Security Manager escalates to the CISO. The CISO determines whether the gap requires a compensating control, a contractual amendment, or reconsideration of the service relationship, and records the resolution.

---

## Evidence Checklist

- [ ] Shared Responsibility Matrix completed and current for every active cloud service relationship (CSC and CSP roles)
- [ ] Written agreements reference the agreed allocation of information security roles and responsibilities
- [ ] CSP capability information requested and recorded for every cloud service [Organisation] consumes
- [ ] CSC-facing capability documentation published and current for every cloud service [Organisation] delivers
- [ ] Allocation gaps, where identified, are recorded with resolution and sign-off

---

<!-- QA_VERIFIED: 2026-08-01 -->
