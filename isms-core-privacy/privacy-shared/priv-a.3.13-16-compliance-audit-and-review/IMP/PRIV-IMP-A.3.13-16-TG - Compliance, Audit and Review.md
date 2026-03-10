<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.13-16-TG:privacy:TG:a.3.13-16 -->
**PRIV-IMP-A.3.13-16-TG — Compliance, Audit and Review — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Compliance, Audit and Review — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.3.13-16-TG |
| **Related Policy** | PRIV-POL-A.3.13-16 (Compliance, Audit and Review) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial technical guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.3.13-16 (Compliance, Audit and Review — the governing policy)
- PRIV-IMP-A.3.13-16-UG (Compliance, Audit and Review — User Guide)
- PRIV-POL-00 (Privacy Regulatory Applicability Framework)

---

## Purpose of This Guide

This guide provides the **technical structures, register schemas, and report templates** for compliance, audit, and review activities. It covers:

- Privacy Legal Requirements Register (PLRR) schema
- PIMS Compliance Self-Assessment Report template
- Independent Review Report structure
- PIMS Audit Programme template
- Record retention reference table

**Audience**: DPO, PIMS Internal Auditor, Legal/Compliance, CISO.

---

## 1. Privacy Legal Requirements Register (PLRR)

The PLRR is owned by the DPO. It is classified CONFIDENTIAL. Access: DPO, Legal/Compliance, Internal Auditor (on assignment), Certification Body (on audit).

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Req ID | Text | Unique reference (e.g., PLRR-GDPR-001) |
| Source | Text | Regulation / standard / contract name and version |
| Article / Clause | Text | Specific article or clause reference |
| Requirement Summary | Text | Plain-language summary of the obligation |
| Obligation Type | Enum | Legal / Regulatory / Contractual / Standard (normative) |
| Applicable Role | Enum | Controller / Processor / Both |
| Tier | Enum | Tier 1 Mandatory / Tier 2 Conditional / Tier 3 Informational |
| Condition (Tier 2) | Text | If Tier 2: applicability trigger |
| Applicable? | Enum | Yes / No / Conditional |
| Compliance Approach | Text | Policy, control, or procedure reference that addresses this requirement |
| Evidence Location | Text | Where compliance evidence is maintained |
| Compliance Status | Enum | Compliant / Partial / Non-Compliant / Not Assessed |
| Gap Description | Text | If non-compliant or partial: description of gap |
| Remediation Action | Text | Action to close gap |
| Remediation Target | Date | Target completion date |
| Last Review Date | Date | Date this entry was last reviewed |
| Reviewed By | Text | Name/role of reviewer |
| Next Review Date | Date | Scheduled next review |
| Notes | Text | DPA guidance references, enforcement decisions, open issues |

### Minimum Entries at First Certification

The following are the minimum PLRR entries required for EU GDPR and CH FADP Tier 1 compliance. Expand with all applicable articles per the organisation's actual processing scope:

| Req ID | Source | Key Article | Summary |
|--------|--------|-------------|---------|
| PLRR-GDPR-001 | EU GDPR | Art. 5 | Processing principles — lawfulness, fairness, transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity and confidentiality, accountability |
| PLRR-GDPR-002 | EU GDPR | Art. 6 | Lawful basis for processing |
| PLRR-GDPR-003 | EU GDPR | Art. 9 | Special category data processing conditions |
| PLRR-GDPR-004 | EU GDPR | Art. 13–14 | Privacy notice obligations |
| PLRR-GDPR-005 | EU GDPR | Art. 15–22 | Data subject rights |
| PLRR-GDPR-006 | EU GDPR | Art. 25 | Privacy by design and by default |
| PLRR-GDPR-007 | EU GDPR | Art. 28 | Processor agreement obligations |
| PLRR-GDPR-008 | EU GDPR | Art. 30 | Records of processing activities (RoPA) |
| PLRR-GDPR-009 | EU GDPR | Art. 32 | Security of processing |
| PLRR-GDPR-010 | EU GDPR | Art. 33–34 | Breach notification |
| PLRR-GDPR-011 | EU GDPR | Art. 35–36 | DPIA and prior consultation |
| PLRR-GDPR-012 | EU GDPR | Art. 37–39 | DPO obligations |
| PLRR-GDPR-013 | EU GDPR | Art. 44–49 | International transfers |
| PLRR-FADP-001 | CH FADP | Art. 6 | Processing principles |
| PLRR-FADP-002 | CH FADP | Art. 7 | Data security |
| PLRR-FADP-003 | CH FADP | Art. 8 | Processor agreements |
| PLRR-FADP-004 | CH FADP | Art. 9 | International transfers |
| PLRR-FADP-005 | CH FADP | Art. 12 | RoPA (>250 FTE or high-risk) |
| PLRR-FADP-006 | CH FADP | Art. 19–21 | Privacy notice obligations |
| PLRR-FADP-007 | CH FADP | Art. 22 | DPIA |
| PLRR-FADP-008 | CH FADP | Art. 24 | Breach notification to FDPIC |
| PLRR-FADP-009 | CH FADP | Art. 25 | Privacy by design |
| PLRR-FADP-010 | CH FADP | Art. 26 | Data subject rights |

---

## 2. PIMS Compliance Self-Assessment Report Template

```
PIMS COMPLIANCE SELF-ASSESSMENT REPORT

Assessment Period: [Start Date] to [End Date]
Conducted By: [DPO Name]
Date of Report: [Date]
Classification: CONFIDENTIAL

EXECUTIVE SUMMARY
Overall compliance status: [ ] Green (no major gaps) [ ] Amber (minor gaps, remediation in progress)
                           [ ] Red (major gaps requiring immediate action)
Number of control groups assessed: 21
Non-conformities identified: [Number]
  - Major: [Number]
  - Minor: [Number]
Remediation actions open: [Number]

ASSESSMENT BY CONTROL GROUP

| Control Group | Policy | Overall Status | Key Findings | Remediation Actions |
|--------------|--------|----------------|-------------|---------------------|
| A.3.3-4 Privacy Policy and Roles | PRIV-POL-A.3.3-4 | Compliant / Partial / Non-Compliant | | |
| A.3.5-7 Classification and Transfer | PRIV-POL-A.3.5-7 | | | |
| A.3.8-10 Identity, Access, Supplier | PRIV-POL-A.3.8-10 | | | |
| A.3.11-12 Incident Management | PRIV-POL-A.3.11-12 | | | |
| A.3.13-16 Compliance, Audit, Review | PRIV-POL-A.3.13-16 | | | |
| A.3.17-19 Awareness, NDAs, Clear Desk | PRIV-POL-A.3.17-19 | | | |
| A.3.20-22 Physical Media and Endpoint | PRIV-POL-A.3.20-22 | | | |
| A.3.23-31 Technical Security Controls | PRIV-POL-A.3.23-31 | | | |
| A.1.2.2-5 Lawful Basis and Consent | PRIV-POL-A.1.2.2-5 | | | |
| A.1.2.6-9 Privacy Governance and Records | PRIV-POL-A.1.2.6-9 | | | |
| A.1.3.2-4 Transparency | PRIV-POL-A.1.3.2-4 | | | |
| A.1.3.5-10 Data Subject Rights | PRIV-POL-A.1.3.5-10 | | | |
| A.1.3.11 Automated Decision Making | PRIV-POL-A.1.3.11 | | | |
| A.1.4.2-5 Data Minimisation | PRIV-POL-A.1.4.2-5 | | | |
| A.1.4.6-10 PII Lifecycle | PRIV-POL-A.1.4.6-10 | | | |
| A.1.5.2-5 PII Transfer and Disclosure | PRIV-POL-A.1.5.2-5 | | | |
| A.2.2.2-7 Processor Agreements | PRIV-POL-A.2.2.2-7 | | | |
| A.2.3.2 PII Principal Obligations | PRIV-POL-A.2.3.2 | | | |
| A.2.4.2-4 Processor Lifecycle | PRIV-POL-A.2.4.2-4 | | | |
| A.2.5.2-6 Transfer and Disclosure (Proc) | PRIV-POL-A.2.5.2-6 | | | |
| A.2.5.7-9 Sub-processor Management | PRIV-POL-A.2.5.7-9 | | | |

PLRR CURRENCY
PLRR last reviewed: [Date] — [ ] Current [ ] Requires update
Open PLRR gaps: [Number]

ROPA ACCURACY
Last quarterly RoPA review: [Date]
RoPA changes since last review: [Summary or "No changes"]
Open RoPA accuracy issues: [Number]

REMEDIATION TRACKING
[List all open remediation actions with owner and target date]

DPO SIGN-OFF
DPO: _________________________ Date: _____________
Reviewed by Executive Management: _________________________ Date: _____________
```

---

## 3. PIMS Independent Review (Audit) Programme Template

```
PIMS INTERNAL AUDIT PROGRAMME

Audit Reference: PIMS-AUDIT-[Year]-[Number]
Audit Type: [ ] Full PIMS audit [ ] Targeted audit (scope: _____________)
Auditor: [Name] — Independence confirmed: [ ] Yes
Audit Period: [Start] to [End]
Report Due: [Date]

SCOPE
Control groups in scope: [List]
Out of scope: [List with rationale]
Excluded activities: [List with rationale]

AUDIT CRITERIA
- ISO/IEC 27701:2025 normative requirements (Annexes A.1/A.2/A.3 as applicable)
- PRIV-POL-A.x.x policies (listed in scope)
- Applicable regulatory requirements per PLRR

AUDIT APPROACH
[ ] Document review
[ ] Personnel interviews
[ ] Technical control testing
[ ] Record sampling
[ ] Process observation

DOCUMENTS REQUESTED
- PIMS Policy Register
- Privacy Roles Register
- RoPA (current)
- Privacy Breach Register
- PLRR (current)
- Independent review report from previous cycle
- Access rights review records
- Training records
- Consent records (sampled)
- DPIA register

AUDIT SCHEDULE
[Date] — Opening meeting with DPO and CISO
[Dates] — Evidence review and interviews
[Date] — Preliminary findings review with DPO
[Date] — Draft report issued
[Date] — Final report issued

FINDINGS CLASSIFICATION
Major non-conformity: PIMS requirement not implemented; significant regulatory compliance gap
Minor non-conformity: PIMS requirement partially implemented; evidence incomplete
Observation: Not a non-conformity; recommendation for improvement

REPORT DISTRIBUTION
Final report: DPO, CISO, Executive Management
Working papers: Auditor retains (3 years); copy to DPO on request
```

---

## 4. Record Retention Reference Table

Summary of mandatory retention periods for PII processing records:

| Record Type | Minimum Retention | Owner |
|------------|------------------|-------|
| Record of Processing Activities (RoPA) | Duration of processing + 3 years | DPO |
| Consent records | Duration of processing + 3 years | Data Owner / DPO |
| DPIA documentation | Duration of processing + 3 years | DPO |
| DPO appointment record | Duration of appointment + 3 years | Executive Management / DPO |
| Supervisory authority notifications (Art. 33 / FADP Art. 24) | 5 years | DPO |
| Data subject rights response records | 3 years from response | DPO |
| Processor agreements (DPAs) | Duration of agreement + 3 years | DPO / Legal |
| International Transfer Register (TIA records) | Duration of transfer + 3 years | DPO |
| Privacy Breach Register | 5 years | DPO |
| Training and acknowledgment records | Duration of employment + 3 years | HR / DPO |
| PIMS internal audit reports | 3 years | PIMS Auditor / DPO |
| PIMS management review records | 3 years | DPO |
| PLRR and review records | 3 years | DPO |
| Compliance self-assessment reports | 3 years | DPO |
| Independent review reports | 3 years | DPO |
| Policy approval and review records | 3 years | DPO |
| Access rights review records | 3 years | IT Security / DPO |
| Identity decommissioning records | 3 years | IT Security |
| Transfer agreement inventory | Duration of agreement + 3 years | DPO / Procurement |

---

<!-- QA_VERIFIED: [Date] -->
