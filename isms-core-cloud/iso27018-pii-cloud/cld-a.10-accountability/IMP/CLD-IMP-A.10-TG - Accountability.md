<!-- ISMS-CORE:IMP:CLD-IMP-A.10-TG:cloud:TG:a.10 -->
**CLD-IMP-A.10-TG — Accountability — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Accountability — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-IMP-A.10-TG |
| **Related Policy** | CLD-POL-A.10 (Accountability) |
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

- CLD-POL-A.10 (Accountability — the governing policy)
- CLD-IMP-A.10-UG (Accountability — User Guide)
- CLD-POL-A.11 (Information Security — sub-processor and security control obligations)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for [Organisation]'s processor accountability obligations under ISO/IEC 27018:2025 A.10. It covers:

- Processor Records of Processing Activities (RoPA) schema
- Breach notification timeline checklist
- PII disposal / return confirmation templates
- Processor accountability register
- DPO Annual Accountability Review Report template

**Audience**: CISO, DPO, Cloud Engineering, Legal/Compliance.

---

## 1. Processor Records of Processing Activities (RoPA) Schema

One record per controller–service relationship. Fields marked * are mandatory under GDPR Article 30(2).

| Field | Type | Description |
|-------|------|-------------|
| `record_id` | String | Unique RoPA entry reference |
| `controller_name` *| String | Legal name of the PII controller |
| `controller_contact` *| String | Controller's DPO or data protection contact |
| `service_agreement_ref` | String | Internal service agreement or contract reference |
| `agreement_start_date` | Date | Date processing commenced under current agreement |
| `agreement_expiry_date` | Date | Scheduled agreement expiry or termination date |
| `processing_purposes` *| Text | Description of processing purposes as per DPA |
| `pii_categories` *| List | Categories of PII processed (identity, contact, financial, health, etc.) |
| `data_subject_categories` *| List | Categories of individuals whose PII is processed |
| `recipients` *| List | Categories of recipients (sub-processors, support teams) |
| `third_country_transfers` *| List | Countries outside EEA/Switzerland to which PII may be transferred, with transfer mechanism |
| `retention_periods` *| Text | Agreed retention periods for each PII category, or criteria used |
| `security_measures` *| Text | Reference to CLD-POL-A.11 controls implemented for this processing |
| `sub_processors` | List | Names and locations of engaged sub-processors |
| `data_residency_requirements` | Text | Controller-specified residency constraints (if any) |
| `last_updated` | Date | Date this record was last reviewed and confirmed current |
| `updated_by` | String | DPO or delegated staff member |

**Retention**: Duration of active processing + 5 years.

---

## 2. Breach Notification Timeline Checklist

Use this checklist for every PII security incident. Complete each row with actual timestamp on completion.

| Step | Responsible | Deadline | Actual Timestamp | Status |
|------|-------------|----------|------------------|--------|
| 1. Incident detected by Security Operations / Cloud Engineering | Security Operations | — | | |
| 2. CISO triages — confirms PII involvement | CISO | Within 2 hours of detection | | |
| 3. CISO escalates to DPO | CISO | Within 2 hours of determination | | |
| 4. DPO identifies affected controller(s) via RoPA | DPO | Within 4 hours of detection | | |
| 5. Initial breach notification drafted | DPO | Within 12 hours of detection | | |
| 6. Notification issued to affected controller(s) | DPO | Within 24 hours of detection | | |
| 7. Phased update #1 issued (if facts materially change) | DPO | Without undue delay | | |
| 8. Containment and investigation complete | CISO / Cloud Engineering | Per incident response plan | | |
| 9. Final incident report issued to controller | DPO | Within 15 business days of closure | | |

**24-hour clock compliance**: Step 6 timestamp must precede the 24-hour mark from Step 1. If Step 6 is delayed, the DPO must document the reason. Any notification exceeding 24 hours requires DPO sign-off and is flagged in the annual accountability review.

### Breach Notification Required Content (per CLD-POL-A.10.1)

| Element | Draft content |
|---------|--------------|
| Nature of the breach | |
| Categories of PII affected | |
| Approximate number of data subjects | |
| Likely consequences for data subjects | |
| Measures taken or proposed (containment/remediation) | |
| [Organisation] incident reference | |
| DPO / security contact for controller follow-up | |

---

## 3. PII Disposal Confirmation Template

Issue to the PII controller upon completion of end-of-contract disposal (Option B per CLD-POL-A.10.3).

---

**Certificate of Secure Destruction — PII Disposal Confirmation**

**To**: [Controller organisation name and DPO contact]
**From**: [Organisation] Data Protection Officer
**Date**: [Date of issue]
**Reference**: EOC-[YYYY]-[NNN] / Controller Agreement Ref: [ref]

This certificate confirms that [Organisation] has completed the secure disposal of all PII processed on behalf of **[Controller name]** under service agreement **[ref]**, in accordance with CLD-POL-A.10.3 and ISO/IEC 27018:2025 Control A.10.3.

| Item | Detail |
|------|--------|
| **PII Categories Destroyed** | [List categories: identity, contact, financial, etc.] |
| **Approximate Volume** | [Approximate record count or data volume] |
| **Primary Store Disposal Date** | [Date] |
| **Disposal Method — Primary Stores** | [Cryptographic erasure / Secure overwrite / Physical destruction] |
| **Backup Copies Disposed** | Yes / Pending (see below) |
| **Backup Disposal Date** | [Date completed or expected date] |
| **Backup Disposal Method** | [Cryptographic erasure of backup encryption keys / Secure overwrite] |
| **Sub-processor Disposal Confirmed** | Yes / N/A |
| **Sub-processor(s) Confirmed** | [Names and confirmation references] |

[Organisation] confirms that no copies of the above PII remain in [Organisation]'s systems or under [Organisation]'s control following the disposal operations described above.

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (Data Protection Officer)
Date: \_\_\_\_\_\_\_\_\_\_\_\_

---

## 4. Processor Accountability Register

Maintain this register as a single-page index of [Organisation]'s accountability obligations and current compliance status. Review at least annually as part of the DPO Accountability Review.

| Obligation | Policy Reference | Owner | Last Verified | Status | Notes |
|------------|-----------------|-------|---------------|--------|-------|
| Processor RoPA current and complete | CLD-POL-A.10 | DPO | | | |
| All incidents notified within 24 hours | CLD-POL-A.10.1 | DPO | | | |
| Breach notification records retained 5 years | CLD-POL-A.10.2 | DPO | | | |
| CLD-POL-A.X policy version history maintained | CLD-POL-A.10.2 | DPO | | | |
| All terminated agreements have return/disposal confirmation | CLD-POL-A.10.3 | DPO | | | |
| Certificates of destruction on file for all disposal cases | CLD-POL-A.10.3 | DPO | | | |
| Sub-processor disposal confirmed for all terminated agreements | CLD-POL-A.10.3 | CISO | | | |
| Annual DPO Accountability Review completed | CLD-IMP-A.10-UG | DPO | | | |

**Status values**: Compliant / Minor gap / Material gap — escalate

---

## 5. DPO Annual Accountability Review Report — Structure

The DPO completes this report once per year (or within 30 days of the anniversary of the last review).

```
DPO ANNUAL ACCOUNTABILITY REVIEW REPORT
Period: [YYYY-MM-DD] to [YYYY-MM-DD]
Completed by: [DPO name]
Review date: [Date]

1. PROCESSOR ROPA STATUS
   - Total active controller agreements: [N]
   - RoPA entries reviewed and confirmed current: [N]
   - Gaps identified: [description or "None"]

2. BREACH NOTIFICATION COMPLIANCE
   - PII incidents in period: [N]
   - Notifications issued within 24 hours: [N]
   - Notifications exceeding 24 hours: [N] (list with reasons)

3. DOCUMENT RETENTION COMPLIANCE
   - CLD-POL-A.X versions archived per schedule: Yes / Gaps noted
   - Incidents and notifications retained: Yes / Gaps noted

4. END-OF-CONTRACT OBLIGATIONS
   - Agreements terminated in period: [N]
   - Return confirmations issued: [N]
   - Disposal certificates issued: [N]
   - Outstanding / overdue: [N] (list with reasons)

5. SUB-PROCESSOR REGISTER
   - Sub-processors active: [N]
   - Sub-processors audited in period: [N]
   - Gaps in audit coverage: [description or "None"]

6. OVERALL ACCOUNTABILITY POSTURE
   - Rating: [Compliant / Minor gaps / Material gaps — remediation required]
   - Remediation items raised: [N] (list references)

Signed: _________________________ (DPO)
Date: _________________________
```

---

<!-- QA_VERIFIED: [Date] -->
