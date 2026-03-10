<!-- ISMS-CORE:IMP:CLD-IMP-A.11-TG:cloud:TG:a.11 -->
**CLD-IMP-A.11-TG — Information Security — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Security — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-IMP-A.11-TG |
| **Related Policy** | CLD-POL-A.11 (Information Security) |
| **Document Creator** | CISO / Data Protection Officer (DPO) |
| **Document Owner** | CISO / Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial technical guide for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant regulatory change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-POL-A.11 (Information Security — the governing policy)
- CLD-IMP-A.11-UG (Information Security — User Guide)
- CLD-POL-A.10 (Accountability — breach notification and disposal)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for implementing and documenting [Organisation]'s 13 ISO/IEC 27018:2025 A.11 security controls. It covers:

- Security control implementation matrix (all A.11 sub-controls vs service tier)
- Encryption specification (at rest / in transit / key management)
- Access control matrix for cloud PII processing environments
- Backup restoration log schema
- PII security incident classification for A.11-related events

**Audience**: CISO, DPO, Cloud Engineering, IT/Identity Management, Legal/Compliance.

---

## 1. Security Control Implementation Matrix

For each A.11 sub-control, record the implementation status and evidence reference per service tier. Review and update at least annually.

| Control | Description | Tier 1 (Core Cloud) | Tier 2 (Managed Services) | Tier 3 (Support Access) | Evidence Reference |
|---------|-------------|--------------------|--------------------------|--------------------------|--------------------|
| A.11.1 | Confidentiality / NDA | ☐ Implemented | ☐ Implemented | ☐ Implemented | NDA Register |
| A.11.2 | Restriction of hardcopy | ☐ Implemented | ☐ Implemented | ☐ N/A | Print Auth Log |
| A.11.3 | Logging of data restoration | ☐ Implemented | ☐ Implemented | ☐ N/A | Restoration Log |
| A.11.4 | Physical media leaving premises | ☐ Implemented | ☐ Implemented | ☐ N/A | Media Movement Register |
| A.11.5 | No unencrypted portable storage | ☐ Implemented | ☐ Implemented | ☐ Implemented | Device Register / MDM |
| A.11.6 | Encryption in transit (TLS) | ☐ Implemented | ☐ Implemented | ☐ Implemented | TLS Config Record |
| A.11.7 | Secure hardcopy disposal | ☐ Implemented | ☐ Implemented | ☐ Implemented | Disposal Certificates |
| A.11.8 | Unique user IDs | ☐ Implemented | ☐ Implemented | ☐ Implemented | IAM System |
| A.11.9 | User ID management | ☐ Implemented | ☐ Implemented | ☐ Implemented | IAM Lifecycle Log |
| A.11.10 | Records of authorised users | ☐ Implemented | ☐ Implemented | ☐ Implemented | Authorised User Register |
| A.11.11 | Contract measures | ☐ Implemented | ☐ N/A | ☐ N/A | DPA Template |
| A.11.12 | Sub-contracted PII processing | ☐ Implemented | ☐ Implemented | ☐ N/A | Sub-processor Register |
| A.11.13 | Pre-used data storage space | ☐ Implemented | ☐ Implemented | ☐ N/A | Decommissioning Records |

**Assessed by (CISO)**: \_\_\_\_\_\_\_\_\_\_\_\_ **Date**: \_\_\_\_\_\_\_\_\_\_\_\_

---

## 2. Encryption Specification

### 2.1 Encryption at Rest

| Data Store Type | Minimum Standard | Preferred Standard | Key Management |
|-----------------|------------------|--------------------|----------------|
| Block storage (EBS / volumes) | AES-256 | AES-256 | Customer-managed keys (CMK) via KMS |
| Object storage (S3 / blob) | AES-256 | AES-256 with per-object keys | CMK via KMS |
| Database storage (RDS, managed DB) | AES-256 (storage-level) | AES-256 + TDE | CMK via KMS |
| Backup and archive | AES-256 | AES-256 | Separate backup encryption key; rotated annually |
| Ephemeral instance storage | AES-256 or cryptographic erasure on deallocation | AES-256 | Host-managed; documented in decommissioning procedure |

### 2.2 Encryption in Transit

| Connection Type | Minimum Standard | Notes |
|-----------------|-----------------|-------|
| External API / web interface | TLS 1.2 | TLS 1.3 required for new deployments |
| Inter-region replication | TLS 1.2 | TLS 1.3 preferred |
| Database connections (application to DB) | TLS 1.2 | Certificate pinning recommended |
| Internal service-to-service (same VPC) | TLS 1.2 | mTLS preferred for PII-bearing services |
| Backup transfer | TLS 1.2 | |

**Prohibited protocols**: SSL 3.0, TLS 1.0, TLS 1.1, plain HTTP for PII endpoints, FTP without TLS.

### 2.3 Key Management

| Key Type | Rotation Frequency | Storage | Revocation Procedure |
|----------|--------------------|---------|----------------------|
| Customer data encryption keys (CMK) | Annual or on compromise | KMS (HSM-backed) | Immediate revocation via KMS on suspected compromise |
| Backup encryption keys | Annual | Separate KMS key store from primary | Revoke on compromise; re-encrypt backups with new key |
| TLS certificates | Per validity period (max 1 year) | Certificate Manager | Automated via ACME / cloud certificate manager |
| Sub-processor data keys (where applicable) | Per sub-processor agreement | Sub-processor KMS | Confirmed revoked on sub-processor engagement termination |

### 2.4 Approved Cipher Suites (TLS)

Approved (as at 2026-03-10; review annually against BSI TR-02102 / NIST SP 800-52):

- `TLS_AES_256_GCM_SHA384` (TLS 1.3)
- `TLS_CHACHA20_POLY1305_SHA256` (TLS 1.3)
- `TLS_AES_128_GCM_SHA256` (TLS 1.3)
- `ECDHE-RSA-AES256-GCM-SHA384` (TLS 1.2)
- `ECDHE-RSA-AES128-GCM-SHA256` (TLS 1.2)

Explicitly disable: RC4, DES, 3DES, NULL ciphers, EXPORT ciphers, anonymous DH.

---

## 3. Access Control Matrix for Cloud PII Processing Environments

Define access levels per role for each PII system. Populate one matrix per service deployment. Example structure:

| Role | PII System Access | Access Level | Authorisation Basis | Review Frequency |
|------|-------------------|--------------|---------------------|-----------------|
| Cloud Engineering (senior) | Primary DB (production) | Read + Admin | CISO approval | Quarterly |
| Cloud Engineering (junior) | Primary DB (production) | Read only | Team lead + CISO approval | Quarterly |
| Cloud Engineering | Backup systems | Read + Restore | Team lead + CISO approval | Quarterly |
| Cloud Service Delivery | Export tooling | Execute (DSR operations) | DPO + team lead approval | Quarterly |
| DPO | Audit view — all PII systems | Read only | CISO approval | Quarterly |
| Support personnel | Support tool (filtered view) | Read only (masked fields) | Team lead approval | Monthly |
| Sub-processors | Designated service scope only | As defined in sub-processor agreement | DPO + CISO approval | Quarterly |

- No role has write access to PII data outside documented, authorised operational procedures
- Admin access to production PII systems requires two-person rule (CISO + senior engineer) for any write or delete operation

---

## 4. Backup Restoration Log Schema

Log every PII backup restoration event. Retain for 3 years.

| Field | Type | Description |
|-------|------|-------------|
| `restoration_id` | String | Unique restoration event reference |
| `date_time` | Timestamp | Date and time restoration commenced |
| `operator_id` | String | Unique user ID of the engineer performing the restoration |
| `authorised_by` | String | Name and role of the team lead or incident commander who authorised the restoration |
| `authorisation_ref` | String | Ticket or written authorisation reference |
| `backup_source` | String | Identifier of the backup set or snapshot being restored |
| `backup_date` | Date | Date the backup was taken |
| `scope_of_data` | Text | Description of what data is included in the restoration (service, data categories) |
| `restoration_destination` | String | Target environment (e.g., production, staging, isolated recovery environment) |
| `pii_involved` | Boolean | Whether the restored data is confirmed to contain PII |
| `controller_name` | String | PII controller whose data is included (if known) |
| `restoration_purpose` | Text | Reason for restoration (incident recovery, compliance export, testing) |
| `completion_time` | Timestamp | Date and time restoration completed |
| `outcome` | Enum | Successful / Failed / Partial |
| `reviewed_by_ciso` | Boolean | Whether included in quarterly CISO log review |

---

## 5. PII Security Incident Classification for A.11 Events

Use this classification table when triaging A.11-related security events. Classification determines urgency of breach notification under CLD-POL-A.10.1.

| Event | A.11 Control | Classification | Controller Notification |
|-------|-------------|----------------|------------------------|
| Unencrypted PII transmitted over public network | A.11.6 | High | Within 24 hours if controller PII involved |
| Unencrypted portable device lost / stolen with PII | A.11.5 | High | Within 24 hours |
| Unauthorised backup restoration of PII | A.11.3 | High | Within 24 hours |
| Physical media lost in transit | A.11.4 | High | Within 24 hours if unencrypted |
| Physical media lost in transit (encrypted) | A.11.4 | Medium | Within 24 hours (risk-based notification) |
| Cross-tenant data remanence detected | A.11.13 | Critical | Within 24 hours — may require supervisory authority notification by controller |
| Shared / generic account used to access PII system | A.11.8 | Medium | DPO assessment; notify controller if PII access confirmed |
| Terminated employee account not deactivated promptly | A.11.9 | Medium | DPO assessment; notify controller if PII access occurred |
| Sub-processor PII breach (reported to [Organisation]) | A.11.12 | High | Within 24 hours of [Organisation] receipt of sub-processor notification |

---

<!-- QA_VERIFIED: [Date] -->
