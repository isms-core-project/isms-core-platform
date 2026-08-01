<!-- ISMS-CORE:IMP:CLD-SEC-IMP-A.8.35-UG:sec:UG:a.8.35 -->
**CLD-SEC-IMP-A.8.35-UG — Segregation in Virtual Computing Environments — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Segregation in Virtual Computing Environments — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-SEC-IMP-A.8.35-UG |
| **Related Policy** | CLD-SEC-POL-A.8.35 (Segregation in Virtual Computing Environments) |
| **Document Creator** | CISO / Cloud Security Manager |
| **Document Owner** | Cloud Engineering Lead |
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

**Review Cycle**: Annual (or upon significant change to virtualisation architecture)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-SEC-POL-A.8.35 (Segregation in Virtual Computing Environments — the governing policy)
- CLD-SEC-IMP-A.8.35-TG (Segregation in Virtual Computing Environments — Technical Guide)
- CLD-SEC-POL-A.8.36 (Detection and Prevention of Unauthorised Use of Cloud Services)

---

## Purpose of This Guide

This guide explains how [Organisation] defines, verifies, and enforces tenant segregation in virtual computing environments under ISO/IEC 27017:2026, Clause 8.35. It is intended for operational use by teams selecting cloud services (CSC role) and teams designing multi-tenant infrastructure (CSP role).

**Who this guide is for**: CISO, Cloud Security Manager, Cloud Engineering Lead, Cloud Service Delivery/Engineering.

---

## Part 1 — Defining and Verifying Segregation Requirements (CSC Role)

### 1.1 Defining Tenant Isolation Requirements

**Procedure — defining segregation requirements for a new cloud service:**

1. **Classify the workload.** The Cloud Security Manager classifies the data and workload to be run on the cloud service by sensitivity, using the organisation's standard data classification scheme.
2. **Set the isolation requirement.** Based on the classification, define the minimum acceptable tenant isolation level — for example, logical isolation via hypervisor-enforced virtual machine boundaries, or a higher requirement such as dedicated/single-tenant infrastructure for the most sensitive workloads.
3. **Record the requirement.** Document the segregation requirement in the Segregation Requirements Statement (schema in CLD-SEC-IMP-A.8.35-TG, Section 1) before the service is selected.

### 1.2 Verifying the CSP Meets the Requirement

**Procedure — verifying CSP segregation controls:**

1. **Request CSP documentation.** Obtain the CSP's published documentation on tenant isolation — hypervisor security, storage segregation, network segregation (VPCs, security groups, or equivalent).
2. **Cross-check against certifications.** Where available, cross-check the CSP's claims against independent assurance (ISO/IEC 27001 certification scope, SOC 2 report, CSA STAR entry).
3. **Record the verification.** Record the outcome in the CSP Segregation Verification Record (CLD-SEC-IMP-A.8.35-TG, Section 2), including any gaps identified.
4. **Re-verify periodically.** Repeat verification at least annually, and whenever the CSP announces a material change to its virtualisation or multi-tenancy architecture.

---

## Part 2 — Enforcing Logical Segregation (CSP Role)

### 2.1 Designing the Segregation Architecture

**Procedure — designing multi-tenant segregation:**

1. **Enumerate resource layers.** The Cloud Engineering Lead enumerates the layers requiring tenant segregation: CSC data, virtualized applications, operating systems, storage, and network.
2. **Select segregation mechanisms per layer.** For each layer, select and document the segregation mechanism — for example, hypervisor-level VM isolation, container namespace/cgroup isolation, storage volume encryption with per-tenant keys, and network-level segmentation (VLANs, security groups, or software-defined network policies).
3. **Separate internal administration.** Design access paths so that [Organisation]'s own internal administration functions (platform management, support tooling) are separated from — and cannot be reached through — CSC-facing resources.
4. **Document the architecture.** Record the completed design in the Segregation Architecture Documentation (CLD-SEC-IMP-A.8.35-TG, Section 3).

### 2.2 Assessing Risk of CSC-Supplied Software

Where [Organisation]'s cloud service permits CSCs to run their own software within shared infrastructure (e.g. a PaaS or IaaS offering), Cloud Service Delivery/Engineering performs a risk assessment before permitting this:

1. Identify the execution model (e.g. containerised, VM-based, serverless) and its isolation boundary.
2. Assess whether the isolation boundary is sufficient to contain a compromise of the CSC-supplied software.
3. Where the assessment identifies insufficient isolation, apply additional compensating controls (e.g. stricter resource quotas, runtime monitoring, sandboxing) before permitting the software to run.
4. Record the assessment outcome in the CSC-Supplied Software Risk Assessment (CLD-SEC-IMP-A.8.35-TG, Section 4).

---

## Part 3 — Ongoing Verification

### 3.1 Periodic Testing

The Cloud Engineering Lead schedules periodic testing of the segregation architecture (for example, tenant-boundary penetration testing, or configuration audits of hypervisor/container isolation settings) to confirm the documented design remains effective in practice.

### 3.2 Regulatory Segregation Requirements

Where applicable law or regulation requires network segregation or traffic isolation for data [Organisation] processes, the Cloud Security Manager confirms — as part of the annual review — that the segregation architecture satisfies those requirements in addition to this policy's baseline.

---

## Evidence Checklist

- [ ] Segregation Requirements Statement defined for every cloud service [Organisation] consumes (CSC role)
- [ ] CSP Segregation Verification Record current for every cloud service consumed, reviewed within the last 12 months
- [ ] Segregation Architecture Documentation complete and current for every multi-tenant environment [Organisation] operates (CSP role)
- [ ] CSC-Supplied Software Risk Assessments completed before permitting CSC software execution in shared infrastructure
- [ ] Periodic segregation testing performed and results recorded

---

<!-- QA_VERIFIED: 2026-08-01 -->
