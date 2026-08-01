<!-- ISMS-CORE:IMP:CLD-SEC-IMP-A.8.35-TG:sec:TG:a.8.35 -->
**CLD-SEC-IMP-A.8.35-TG — Segregation in Virtual Computing Environments — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Segregation in Virtual Computing Environments — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-SEC-IMP-A.8.35-TG |
| **Related Policy** | CLD-SEC-POL-A.8.35 (Segregation in Virtual Computing Environments) |
| **Document Creator** | CISO / Cloud Security Manager |
| **Document Owner** | Cloud Engineering Lead |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial technical guide for ISO/IEC 27017:2026 Ed. 2 implementation |

**Review Cycle**: Annual (or upon significant change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-SEC-POL-A.8.35 (Segregation in Virtual Computing Environments — the governing policy)
- CLD-SEC-IMP-A.8.35-UG (Segregation in Virtual Computing Environments — User Guide)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for defining, verifying, and documenting tenant segregation under ISO/IEC 27017:2026, Clause 8.35. It covers:

- Segregation Requirements Statement schema (CSC role)
- CSP Segregation Verification Record schema (CSC role)
- Segregation Architecture Documentation template (CSP role)
- CSC-Supplied Software Risk Assessment schema (CSP role)

**Audience**: CISO, Cloud Security Manager, Cloud Engineering Lead.

---

## 1. Segregation Requirements Statement Schema

Completed by the Cloud Security Manager before selecting a cloud service.

| Field | Type | Description |
|-------|------|-------------|
| `requirement_id` | String (unique) | Internal reference: `SRS-YYYY-NNN` |
| `service_id` | String | Reference to the cloud service (cross-reference CLD-SEC-IMP-A.5.38-TG Shared Responsibility Matrix `service_id` where applicable) |
| `data_classification` | Enum | Public / Internal / Confidential / Restricted |
| `minimum_isolation_level` | Enum | Logical (shared hypervisor) / Logical with dedicated host / Physical (single-tenant) |
| `justification` | Text | Rationale for the required isolation level given the data classification |
| `defined_by` | String | Name/role of the person defining the requirement |
| `defined_date` | Date | Date the requirement was defined |

---

## 2. CSP Segregation Verification Record Schema

Completed by the Cloud Security Manager; reviewed at least annually.

| Field | Type | Description |
|-------|------|-------------|
| `verification_id` | String (unique) | Internal reference: `SVR-YYYY-NNN` |
| `requirement_id` | String | Reference to the Segregation Requirements Statement |
| `csp_name` | String | Name of the cloud service provider |
| `verification_date` | Date | Date verification was performed |
| `evidence_reviewed` | Text | List of evidence reviewed (CSP documentation, certifications, audit reports) |
| `requirement_met` | Boolean | Whether the CSP's segregation controls meet the stated requirement |
| `gap_description` | Text | Description of any gap identified |
| `next_verification_date` | Date | Date of next scheduled verification |
| `verified_by` | String | Name/role of the person performing verification |

---

## 3. Segregation Architecture Documentation Template

Used when [Organisation] operates multi-tenant infrastructure as a CSP.

---

**SEGREGATION ARCHITECTURE — [Service Name]**
**Version**: [Version] **Effective Date**: [Date]

### A. Segregation by Layer

| Layer | Segregation Mechanism | Description |
|-------|------------------------|-------------|
| CSC data | [e.g. Per-tenant encryption keys, logical database/schema isolation] | [Describe] |
| Virtualized applications | [e.g. Container namespace isolation, per-tenant application instances] | [Describe] |
| Operating systems | [e.g. Hypervisor-enforced VM boundaries] | [Describe] |
| Storage | [e.g. Per-tenant storage volumes, access-controlled object storage prefixes] | [Describe] |
| Network | [e.g. VPC/VLAN per tenant, security group policies, software-defined network policies] | [Describe] |

### B. Internal Administration Separation

| Control | Description |
|---------|-------------|
| Administrative access path | [Describe how internal admin access is separated from CSC-facing resources] |
| Access control mechanism | [e.g. Separate administrative network, jump host, privileged access management] |

### C. Testing and Assurance

| Test Type | Frequency | Last Performed | Result Reference |
|-----------|-----------|-----------------|-------------------|
| Tenant-boundary penetration test | [Frequency] | [Date] | [Reference] |
| Configuration audit (hypervisor/container isolation) | [Frequency] | [Date] | [Reference] |

---

## 4. CSC-Supplied Software Risk Assessment Schema

Completed by Cloud Service Delivery/Engineering before permitting CSC-supplied software to run in shared infrastructure.

| Field | Type | Description |
|-------|------|-------------|
| `assessment_id` | String (unique) | Internal reference: `CSA-YYYY-NNN` |
| `service_id` | String | Reference to the cloud service |
| `execution_model` | Enum | Container / Virtual machine / Serverless function / Other |
| `isolation_boundary_description` | Text | Description of the isolation boundary for the execution model |
| `isolation_sufficient` | Boolean | Whether the isolation boundary is assessed as sufficient |
| `compensating_controls` | Text | Additional controls applied if isolation is assessed as insufficient (e.g. quotas, runtime monitoring, sandboxing) |
| `assessed_by` | String | Name/role of the assessor |
| `assessment_date` | Date | Date of assessment |
| `approved_by` | String | Name/role of the approver permitting the software to run |

---

<!-- QA_VERIFIED: 2026-08-01 -->
