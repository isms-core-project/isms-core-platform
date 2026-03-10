<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.4.2-5-TG:privacy:TG:a.1.4.2-5 -->
**PRIV-IMP-A.1.4.2-5-TG — Data Minimisation — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Data Minimisation — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.1.4.2-5-TG |
| **Related Policy** | PRIV-POL-A.1.4.2-5 (Data Minimisation) |
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

- PRIV-POL-A.1.4.2-5 (Data Minimisation — the governing policy)
- PRIV-IMP-A.1.4.2-5-UG (Data Minimisation — User Guide)
- PRIV-IMP-A.1.2.6-9-TG (Privacy Governance and Records — RoPA schema)

---

## Purpose of This Guide

This guide provides the **technical structures, register schemas, and templates** for data minimisation compliance. It covers:

- Data Minimisation Objectives Document template
- PII Field Justification Register schema
- Pseudonymised Dataset Register schema
- Anonymisation Confirmation Record template
- Accuracy Review Checklist template (for significant-decision PII)
- Privacy-by-Default Settings Reference

**Audience**: DPO, Legal/Compliance, IT Security Team, Development Teams.

---

## 1. Data Minimisation Objectives Document

The Data Minimisation Objectives Document is the organisation's formal statement of minimisation commitments and mechanisms, as required by A.1.4.5. Maintained by the DPO. Reviewed annually.

```
DATA MINIMISATION OBJECTIVES DOCUMENT
[Organisation Legal Name]
Version: [X.X] | Effective: [Date] | Last Reviewed: [Date]
DPO: [Name]

---

OBJECTIVE 1 — COLLECTION MINIMISATION
Commitment: Collect only PII fields that are necessary for documented purposes.
Mechanism: DPO field justification review before any new collection point deployed.
Evidence: PII Field Justification Register; RoPA data fields section.
Status: [Implemented / In Progress / Planned]

OBJECTIVE 2 — PROCESSING MINIMISATION
Commitment: Restrict PII access and processing to documented purposes and authorised roles.
Mechanism: Role-based access controls; purpose compatibility assessment for secondary use.
Evidence: Access review records; purpose compatibility assessments per PRIV-IMP-A.1.2.2-5-TG.
Status: [Implemented / In Progress / Planned]

OBJECTIVE 3 — RETENTION MINIMISATION
Commitment: Retain PII only as long as necessary for the processing purpose.
Mechanism: Retention schedules per PRIV-POL-A.1.4.6-10; automated or scheduled deletion.
Evidence: Retention schedule documentation; disposal records.
Status: [Implemented / In Progress / Planned]

OBJECTIVE 4 — DE-IDENTIFICATION FOR SECONDARY USE
Commitment: Use pseudonymised or anonymised data for analytics, testing, and research
           where individual re-identification is not required.
Mechanism: Pseudonymisation process (key-based token replacement);
           anonymisation process (DPO confirmation required).
Evidence: Pseudonymised Dataset Register; Anonymisation Confirmation Records.
Status: [Implemented / In Progress / Planned]

OBJECTIVE 5 — AGGREGATION MINIMISATION
Commitment: Avoid creating aggregates that re-identify or over-identify data subjects
           beyond the stated purpose.
Mechanism: DPO assessment before deployment of analytics or profiling outputs.
Evidence: DPIA records where applicable; DPO review correspondence.
Status: [Implemented / In Progress / Planned]

---

ANNUAL REVIEW
Last full review: [Date]
Changes made: [Summary of changes or "No changes"]
Next review due: [Date]
DPO: _________________________ Date: _____________
```

---

## 2. PII Field Justification Register

Records each PII field approved by the DPO for collection, mapped to the processing activity and purpose. Supplements the RoPA. Maintained by the DPO.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Field ID | Text | Unique reference (e.g., FJR-001) |
| Collection Point | Text | Form, API endpoint, or integration where field is collected |
| RoPA Activity Reference | Text | Linked RoPA processing activity ID |
| Field Name | Text | Name of the PII field (e.g., "Date of Birth") |
| Data Type | Text | Text / Date / Number / Boolean / File / Other |
| PII Category | Enum | Basic / Contact / Financial / Health / Biometric / Other special category |
| Processing Purpose | Text | Specific documented purpose this field serves |
| Necessity Argument | Text | Why this field is necessary (not merely useful) for the purpose |
| DPO Review Date | Date | Date DPO reviewed and approved this field |
| DPO Decision | Enum | Approved / Rejected / Approved with Conditions |
| Conditions (if applicable) | Text | Any conditions attached to approval |
| Status | Enum | Active / Retired / Under Review |
| Notes | Text | Design changes, purpose evolution, review notes |

---

## 3. Pseudonymised Dataset Register

Tracks all pseudonymised datasets created for secondary processing purposes. Maintained by the DPO. Classified RESTRICTED.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Dataset ID | Text | Unique reference (e.g., PSD-001) |
| Source Dataset / System | Text | Origin of the PII before pseudonymisation |
| RoPA Activity Reference | Text | Linked original processing activity |
| Secondary Purpose | Text | Reason for creating the pseudonymised dataset |
| Pseudonymisation Method | Enum | Token replacement / Hashing / Encryption / Other |
| Fields Pseudonymised | Text | List of direct identifiers replaced with pseudonyms |
| Key Storage Location | Text | Where the pseudonymisation key is held (system + access control) |
| Key Custodian | Text | Named role responsible for the key |
| Key Access Log Reference | Text | Reference to access log for the key |
| Deployment Environment | Text | System or environment where pseudonymised dataset is used |
| Created Date | Date | Date pseudonymised dataset was created |
| Review Date | Date | Next scheduled review of continued need |
| Deletion Date | Date | Date pseudonymised dataset was deleted (if applicable) |
| DPO Approval Date | Date | Date DPO approved creation of this dataset |
| Status | Enum | Active / Deleted / Under Review |

---

## 4. Anonymisation Confirmation Record

Completed by the DPO before any dataset is declared anonymised and treated as no longer subject to GDPR.

```
ANONYMISATION CONFIRMATION RECORD

Record ID: ANR-[NNN]
Date: _____________
DPO: _____________

DATASET DESCRIPTION
Dataset Name / Reference: _____________________________________________
Source System: _____________________________________________
Number of Records (approx.): _____________________________________________
PII Categories Originally Present: _____________________________________________
Intended Use After Anonymisation: _____________________________________________

DE-IDENTIFICATION TECHNIQUES APPLIED
(Check all that apply)
[ ] Suppression — removed fields: _____________________________________________
[ ] Generalisation — generalised fields: _____________________________________________
[ ] Aggregation — data aggregated to level: _____________________________________________
[ ] Noise addition — applied to fields: _____________________________________________
[ ] Tokenisation / pseudonymisation (key destroyed) — fields: _______________________
[ ] Other: _____________________________________________

RE-IDENTIFICATION RISK ASSESSMENT

1. SINGLING OUT TEST
   Can an individual be identified from this dataset alone
   (e.g., unique combination of values points to one person)?
   [ ] No — singling out risk adequately mitigated
   [ ] Yes / Uncertain — anonymisation insufficient; use pseudonymisation instead
   Evidence / reasoning: _____________________________________________

2. LINKABILITY TEST
   Can records in this dataset be linked to another available dataset
   (internal or publicly available) to re-identify individuals?
   [ ] No — linkability risk adequately mitigated
   [ ] Yes / Uncertain — anonymisation insufficient; use pseudonymisation instead
   Evidence / reasoning: _____________________________________________

3. INFERENCE TEST
   Can attributes of an individual be inferred from this dataset,
   even without direct identification?
   [ ] No — inference risk adequately mitigated
   [ ] Yes / Uncertain — anonymisation insufficient; use pseudonymisation instead
   Evidence / reasoning: _____________________________________________

CONFIRMATION
[ ] All three tests passed — this dataset is confirmed as anonymised.
    GDPR data subject rights do not apply to this dataset.
    The dataset may be used for the stated purpose.

[ ] One or more tests failed — this dataset is NOT anonymised.
    Pseudonymisation or further de-identification required before secondary use.

DPO Signature: _________________________ Date: _____________

---
IMPORTANT: This record must be retained as evidence of the anonymisation assessment.
A dataset treated as anonymised without a signed Anonymisation Confirmation Record
is not compliant with PRIV-POL-A.1.4.2-5.
```

---

## 5. Accuracy Review Checklist (Significant-Decision PII)

Used when PII is to be used in a significant decision (financial, health, legal, employment). The Data Owner must complete this before the decision is made.

```
ACCURACY REVIEW CHECKLIST — SIGNIFICANT DECISION PII

Processing Activity: _____________________________________________
Decision Type: _____________________________________________
Data Owner: _____________________________________________
Review Date: _____________________________________________
Data Subject ID / Reference: _____________________________________________

FIELDS USED IN THE DECISION

| Field Name | Data Source | Date Last Updated | Verified Accurate? | Method of Verification |
|------------|-------------|-------------------|--------------------|------------------------|
| | | | Yes / No / Unknown | |
| | | | Yes / No / Unknown | |
| | | | Yes / No / Unknown | |

ACCURACY ASSESSMENT
[ ] All fields verified as accurate and current — proceed with decision
[ ] One or more fields are uncertain or out of date:
    Fields requiring update/verification: _____________________________________________
    Action taken before decision: _____________________________________________

[ ] Accuracy cannot be confirmed — decision deferred pending verification
    Reason: _____________________________________________
    Next review date: _____________________________________________

DATA OWNER SIGN-OFF
Data Owner: _________________________ Date: _____________
```

---

## 6. Privacy-by-Default Settings Reference

Records the technically enforced privacy-by-default settings per system or product. Maintained by the DPO in coordination with Development. Reviewed at each product release.

| System / Feature | Default Setting (Privacy-Protective) | Alternative (Requires Active Choice) | Confirmed in Code Review | Date |
|-----------------|--------------------------------------|--------------------------------------|--------------------------|------|
| User account sharing settings | Private (not visible to other users) | Shared / Public (requires explicit opt-in) | [ ] Yes | |
| Marketing preferences | Not subscribed | Subscribed (requires explicit opt-in) | [ ] Yes | |
| Analytics instrumentation | Pseudonymised user ID only | Full identity (requires documented justification + DPO approval) | [ ] Yes | |
| API token scope | Minimum required scope | Broader scope (requires documented justification) | [ ] Yes | |
| Third-party data sharing | Not shared | Shared (requires separate lawful basis) | [ ] Yes | |

---

<!-- QA_VERIFIED: [Date] -->
