<!-- ISMS-CORE:IMP:CLD-IMP-A.5-TG:cloud:TG:a.5 -->
**CLD-IMP-A.5-TG — Data Minimisation — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Data Minimisation — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-IMP-A.5-TG |
| **Related Policy** | CLD-POL-A.5 (Data Minimisation) |
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

- CLD-POL-A.5 (Data Minimisation — the governing policy)
- CLD-IMP-A.5-UG (Data Minimisation — User Guide)
- CLD-POL-A.11 (Information Security — secure erasure and disposal standards)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for data minimisation implementation. It covers:

- Temporary File Scope Record schema (per service component)
- Data minimisation configuration checklist (per compute layer)
- Remanence test methodology
- Anonymisation Confirmation Record template

**Audience**: CISO, DPO, Cloud Engineering, Security Operations.

---

## 1. Temporary File Scope Record Schema

One record per service component. Maintained by Cloud Engineering; reviewed by DPO annually.

| Field | Type | Description |
|-------|------|-------------|
| Record ID | Text | Unique reference (e.g., TFSR-2026-001) |
| Service Component | Text | Name of the cloud service or component (e.g., Batch Processing Engine, API Gateway) |
| Compute Layer | Enum | Bare metal / VM / Container / Serverless |
| Temporary Storage Category | Enum | Cache / Swap / Work file / Application log / Ephemeral block storage |
| PII Categories That May Appear | Text | Categories of PII that may be present (e.g., identity data, contact data, processing payloads) |
| Technical Necessity Justification | Text | Why this PII must appear in this storage type (cannot be excluded) |
| Erasure Method | Enum | Cryptographic erasure / Multi-pass overwrite / Memory zeroing / Automated deletion |
| Erasure Trigger | Text | Event that triggers erasure (e.g., processing job completion, container termination, log rotation) |
| Erasure Automated? | Boolean | Yes / No |
| Manual Erasure Procedure Ref | Text | If not automated: reference to documented manual procedure |
| Regions Covered | Text | Geographic regions where this component operates |
| Last Reviewed | Date | Date of last DPO/CISO review |
| Remediation Actions Open | Text | Any outstanding gaps and target remediation date |

---

## 2. Data Minimisation Configuration Checklist (Per Service Component)

Completed by Cloud Engineering during service build and at each annual review. Signed off by CISO.

### 2.1 Compute Layer Controls

| Check | Compute Layer | Requirement | Status |
|-------|--------------|-------------|--------|
| Ephemeral block storage erased on instance termination | VM / Bare Metal | Automated cryptographic erasure or overwrite before deallocation | [ ] Pass / [ ] Fail |
| Container ephemeral storage cleared on container stop | Container | Overlay filesystem destroyed; no PII retained in image layer | [ ] Pass / [ ] Fail |
| Serverless function memory zeroed post-execution | Serverless | Runtime clears execution context; no PII persists in warm instance beyond execution scope | [ ] Pass / [ ] Fail |
| Swap / paging files encrypted and cleared | VM / Bare Metal | Swap encrypted; cleared on shutdown or job completion | [ ] Pass / [ ] Fail |
| Scratch / work directories purged post-job | All | Automated cleanup task triggered on job completion event | [ ] Pass / [ ] Fail |

### 2.2 Log Minimisation Controls

| Check | Requirement | Status |
|-------|-------------|--------|
| PII in request URLs masked or excluded | Log configuration applies masking to URL parameters containing PII | [ ] Pass / [ ] Fail |
| PII in request/response payloads excluded from logs | Application logging level set to exclude payload bodies containing PII unless debug mode explicitly authorised | [ ] Pass / [ ] Fail |
| PII in error traces masked | Exception handlers apply PII masking before writing to logs | [ ] Pass / [ ] Fail |
| Log retention automated | Automated deletion rule configured per log sink; retention period documented | [ ] Pass / [ ] Fail |
| Log retention ≤ service agreement maximum | Configured retention period confirmed against controller's service agreement | [ ] Pass / [ ] Fail |

### 2.3 Multi-Tenant Isolation Controls

| Check | Requirement | Status |
|-------|-------------|--------|
| Storage allocation is per-tenant isolated | No shared persistent temporary store between tenants during active processing | [ ] Pass / [ ] Fail |
| Erasure triggered before reallocation | Automated erasure confirmed as pre-condition in deallocation pipeline | [ ] Pass / [ ] Fail |
| Reallocation events logged | Storage deallocation and reallocation events written to audit log | [ ] Pass / [ ] Fail |

**Checklist completed by**: _________________________ Date: _____________
**CISO sign-off**: _________________________ Date: _____________

---

## 3. Remanence Test Methodology

Conducted by Security Operations as part of the annual minimisation review.

**Objective**: Confirm that no PII is recoverable from temporary storage after processing job completion.

**Procedure**:

1. Select a representative processing job from each service component category (cache-heavy, log-intensive, batch)
2. Execute the job in a controlled test environment using synthetic or pseudonymised test PII
3. Upon job completion, capture a forensic image of the temporary storage volumes used by that job (before any subsequent reallocation)
4. Analyse the forensic image for PII remnants using string matching against known test PII values
5. Record outcome in the Remanence Test Record (below)
6. If PII remnants are found: raise remediation action in the Temporary File Scope Record; Cloud Engineering implements fix before re-test

**Remanence Test Record Schema**:

| Field | Description |
|-------|-------------|
| Test ID | Unique reference (e.g., RT-2026-001) |
| Service Component | Name of the tested component |
| Storage Category Tested | Cache / Swap / Work file / Log / Ephemeral block |
| Test Date | Date of test |
| Test PII Used | Description of synthetic/pseudonymised PII used |
| Forensic Method | Tool and method used to inspect storage image |
| Outcome | Pass (no PII found) / Fail (PII found — describe) |
| Remediation Action (if Fail) | Reference to remediation action and owner |
| Tested By | Security Operations engineer name |
| Reviewed By | CISO |

---

## 4. Anonymisation Confirmation Record Template

Issued by the DPO before any controller PII processed by [Organisation] is treated as anonymised for secondary use (e.g., analytics, telemetry aggregation, reporting).

```
ANONYMISATION CONFIRMATION RECORD

Record Reference: ACR-[YYYY]-[NNN]
Date: _____________
DPO: _____________

DATASET DETAILS

Dataset Description: _____________________________________________
Source Service Component: _____________________________________________
Original PII Categories: _____________________________________________
Intended Secondary Use: _____________________________________________
Techniques Applied: [ ] Aggregation  [ ] Generalisation  [ ] Suppression
                    [ ] Pseudonymisation (NOTE: not anonymisation — see below)
                    [ ] Other: _____________

THREE-PART RE-IDENTIFICATION RISK ASSESSMENT

Singling out risk:
Can an individual be singled out from this dataset alone?
[ ] No — dataset is sufficiently aggregated / generalised
[ ] Residual risk — describe mitigation: ______________________________

Linkability risk:
Can records in this dataset be linked to other available datasets
to re-identify individuals?
[ ] No — insufficient linking attributes
[ ] Residual risk — describe mitigation: ______________________________

Inference risk:
Can attributes of an identifiable individual be inferred from
this dataset?
[ ] No — no inferential identifiers present
[ ] Residual risk — describe mitigation: ______________________________

CONCLUSION

[ ] CONFIRMED ANONYMISED — all three risks adequately mitigated.
    This dataset is not PII. GDPR does not apply.
[ ] NOT CONFIRMED — residual re-identification risk. Apply pseudonymisation
    and treat as PII.

DPO: _________________________ Date: _____________

NOTE: Pseudonymised datasets are PII. This record does not apply to
pseudonymised datasets. A dataset is only anonymised when the DPO
has confirmed all three risks are mitigated.
```

---

<!-- QA_VERIFIED: [Date] -->
