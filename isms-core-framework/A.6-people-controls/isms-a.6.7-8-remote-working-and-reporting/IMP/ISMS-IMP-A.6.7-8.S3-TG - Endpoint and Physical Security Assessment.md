<!-- ISMS-CORE:IMP:ISMS-IMP-A.6.7-8.S3-TG:framework:TG:a.6.7-8 -->
**ISMS-IMP-A.6.7-8.S3-TG - Endpoint and Physical Security Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Endpoint and Physical Security Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.6.7-8.S3-TG |
| **Related Policy** | ISMS-POL-A.6.7-8 (Remote Working and Reporting) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.6.7-8 (Remote Working and Reporting)
- ISMS-IMP-A.6.7-8.S1 (Remote Work Authorisation Assessment)
- ISMS-IMP-A.6.7-8.S2 (Technical Controls Assessment)
- ISMS-IMP-A.6.7-8.S4 (Event Reporting Mechanisms Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a678_s3_endpoint_physical_security.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.6.7-8.S3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Device Inventory |
| 3 | Encryption Status |
| 4 | Endpoint Protection |
| 5 | Patch Compliance |
| 6 | BYOD Assessment |
| 7 | Physical Security |
| 8 | Lost Stolen Procedures |
| 9 | Gap Analysis |
| 10 | Evidence Register |
| 11 | Summary Dashboard |
| 12 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #666666 | Dark Gray (Secondary Text) |
| #C00000 | Dark Red (Blocked) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | Device ID |
| 2 | Device Type |
| 3 | Ownership |
| 4 | OS Version |
| 5 | Assigned User |
| 6 | Department |
| 7 | Remote Enabled |
| 8 | MDM Enrolled |
| 9 | Last Check-in |
| 10 | Status |
| 11 | Encryption Type |
| 12 | Full-Disk |
| 13 | Key Escrowed |
| 14 | Last Verified |
| 15 | Compliant |
| 16 | Notes |
| 17 | Protection Solution |
| 18 | Agent Installed |
| 19 | Agent Version |
| 20 | Definitions Date |
| 21 | Last Scan |
| 22 | Threats (90d) |
| 23 | OS Patch Level |
| 24 | Critical Missing |
| 25 | High Missing |
| 26 | Medium Missing |
| 27 | Days Since Patch |
| 28 | Owner |
| 29 | OS/Version |
| 30 | Min OS Met |
| 31 | Container |
| 32 | Encrypted |
| 33 | Remote Wipe |
| 34 | Agreement Signed |
| 35 | Category |
| 36 | Requirement |
| 37 | Level |
| 38 | Documented |
| 39 | Communicated |
| 40 | Ack Required |
| 41 | Ack Captured |
| 42 | Verification |
| 43 | Procedure Element |
| 44 | SLA |
| 45 | Implemented |
| 46 | Documentation |
| 47 | Last Tested |
| 48 | Responsible |
| 49 | Evidence |
| 50 | Gap ID |
| 51 | Source |
| 52 | Description |
| 53 | Scope |
| 54 | Risk |
| 55 | Remediation |
| 56 | Target |
| 57 | Evidence ID |
| 58 | Evidence Type |
| 59 | Source / Owner |
| 60 | Date Collected |
| 61 | Retention Period |
| 62 | Storage Location |
| 63 | Assessment Area |
| 64 | Total Items |
| 65 | Partial |
| 66 | Non-Compliant |
| 67 | N/A |
| 68 | Compliance % |
| 69 | Finding |
| 70 | Count |
| 71 | Severity |
| 72 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Active, Inactive, Lost, Retired, Suspended, Not Configured, Collected
Pending, Not Available, Superseded, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 12 sheets, 72 columns, 20 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Physical security is the foundation upon which all other security measures are built."*
— ASIS International

<!-- QA_VERIFIED: 2026-03-01 -->
