<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.2-3-5.S4-TG:framework:TG:a.8.2-3-5 -->
**ISMS-IMP-A.8.2-3-5.S4-TG - Privileged Monitoring Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Privileged Monitoring |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.2-3-5.S4-TG |
| **Related Policy** | ISMS-POL-A.8.2-3-5 (Authentication Privileged Access) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.2 (Privileged Access Rights) |
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

- ISMS-POL-A.8.2-3-5 (Authentication Privileged Access)
- ISMS-IMP-A.8.2-3-5.S1 (Authentication Inventory)
- ISMS-IMP-A.8.2-3-5.S2 (MFA Coverage)
- ISMS-IMP-A.8.2-3-5.S3 (Privileged Accounts)
- ISMS-IMP-A.8.2-3-5.S5 (Access Restrictions)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a8235_4_privileged_monitoring.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.2-3-5.S4`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Session Recording Coverage |
| 3 | Privileged Command Logging |
| 4 | Anomaly Detection Rules |
| 5 | Privileged Access Activity |
| 6 | Alert Response Tracking |
| 7 | Off Hours Access Log |
| 8 | Failed Login Analysis |
| 9 | Tier Violation Incidents |
| 10 | Evidence Register |
| 11 | Summary Dashboard |
| 12 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
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
| 1 | Total Systems Not Recording: |
| 2 | Evidence ID |
| 3 | Control Ref |
| 4 | Evidence Type |
| 5 | Description |
| 6 | Location / Reference |
| 7 | Date Collected |
| 8 | Collected By |
| 9 | Verification Status |
| 10 | Account / System |
| 11 | Admin Tier |
| 12 | Environment |
| 13 | Recording Status |
| 14 | Recording Method |
| 15 | Storage Location |
| 16 | Retention Period |
| 17 | Last Recording Date |
| 18 | Playback Tested |
| 19 | Compliance Target |
| 20 | Compliance Status |
| 21 | Notes |
| 22 | System / Platform |
| 23 | Logging Type |
| 24 | Status |
| 25 | Log Destination |
| 26 | Retention |
| 27 | SIEM Integrated |
| 28 | Compliance |
| 29 | Alert Rule Name |
| 30 | Anomaly Type |
| 31 | Severity |
| 32 | Detection Logic |
| 33 | Alert Destination |
| 34 | Response SLA |
| 35 | Date/Time |
| 36 | Account |
| 37 | User |
| 38 | System |
| 39 | Action |
| 40 | Duration |
| 41 | Location |
| 42 | Anomaly Detected |
| 43 | Review Status |
| 44 | Alert ID |
| 45 | Alert Time |
| 46 | Alert Type |
| 47 | Assigned To |
| 48 | Response Time (min) |
| 49 | Resolution |
| 50 | Tier |
| 51 | Business Justification |
| 52 | Approved By |
| 53 | Source IP |
| 54 | Failure Count |
| 55 | Time Window |
| 56 | Alert Generated |
| 57 | Investigation |
| 58 | Date |
| 59 | Account Tier |
| 60 | System Tier |
| 61 | Violation Type |
| 62 | Action Taken |
| 63 | Root Cause |

### Data Validation Values

All dropdown/list values used across sheets:

```
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred, Production, Non-Production, Test
Development, Video Recording, Keystroke Logging, Both (Video + Keystroke)
None, Yes, No, Tier 0: 100%, Tier 1 Prod: 90%+, Tier 1 Non-Prod: 50%+
Optional
```

**Extracted:** 12 sheets, 63 columns, 22 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"What privileged accounts do in the dark must be brought to light."*
— Monitoring principle

<!-- QA_VERIFIED: 2026-03-01 -->
