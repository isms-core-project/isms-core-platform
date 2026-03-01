<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.20-21-22.S2-TG:framework:TG:a.8.20-21-22 -->
**ISMS-IMP-A.8.20-21-22.S2-TG - Network Architecture Documentation**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Architecture Documentation |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.20-21-22.S2-TG |
| **Related Policy** | ISMS-POL-A.8.20-21-22 (Network Security) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.20 (Networks Security) |
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

- ISMS-POL-A.8.20-21-22 (Network Security)
- ISMS-IMP-A.8.20-21-22.S1 (Network Discovery)
- ISMS-IMP-A.8.20-21-22.S3 (Device Hardening)
- ISMS-IMP-A.8.20-21-22.S4 (Services Security)
- ISMS-IMP-A.8.20-21-22.S5 (Segmentation Implementation)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a820_2_device_security_assessment.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.20-21-22.S2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Evidence Register |
| 2 | Approval Sign-Off |
| 3 | Instructions & Legend |
| 4 | Device Hardening Assessment |
| 5 | Hardening Baseline Reference |
| 6 | Gap Analysis |
| 7 | Summary Dashboard |
| 8 | Device Type Compliance |
| 9 | Average Compliance Score by Device Type |
| 10 | Compliance Score (%) |
| 11 | Device Type |
| 12 | Top Gaps Analysis |
| 13 | Most Common Hardening Failures |
| 14 | Failure Count |
| 15 | Requirement |
| 16 | Remediation Roadmap |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #006100 | Dark Green (Pass) |
| #4472C4 | Medium Blue (Sub-headers) |
| #7F7F7F | Custom |
| #808080 | Gray (Disabled) |
| #9C0006 | Dark Red (Error) |
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
| 1 | Assessment Area |
| 2 | Total |
| 3 | Yes |
| 4 | Partial |
| 5 | N-A |
| 6 | Compliance % |
| 7 | DEVICE HARDENING BASELINE REFERENCE |
| 8 | DEVICE HARDENING GAPS - SUMMARY & REMEDIATION TRACKING |
| 9 | Network Security Team |
| 10 | What This Shows |
| 11 | Critical Finding Type |
| 12 | Filter Instructions |
| 13 | COMPLIANCE ANALYSIS BY DEVICE TYPE |
| 14 | TOP HARDENING GAPS - MOST COMMON FAILURES |
| 15 | HARDENING REMEDIATION ROADMAP |
| 16 | Device ID |
| 17 | Device Type |
| 18 | Hostname |
| 19 | Primary IP |
| 20 | Criticality |
| 21 | Gap ID |
| 22 | Hardening Requirement |
| 23 | Current State |
| 24 | Gap Severity |
| 25 | Remediation Plan |
| 26 | Owner |
| 27 | Status |
| 28 | Target Date |
| 29 | Priority |
| 30 | Severity |
| 31 | Gap Description |
| 32 | Affected Devices |
| 33 | Remediation Action |
| 34 | Evidence ID |
| 35 | Evidence Type |
| 36 | Description |
| 37 | Location/Path |
| 38 | Date Collected |
| 39 | Collected By |
| 40 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, N/A, Router, Switch, Firewall, Wireless AP, Load Balancer
VPN Concentrator, IDS/IPS, Network Management, Other, Critical, High, Medium
Low, Open, In Progress, Completed, Accepted Risk, Deferred, Compliant
Non-Compliant, Partially Compliant, Not Assessed, Configuration file
Screenshot, Network scan, Documentation, Vendor spec, Certificate inventory
Audit log, Compliance report, ✅ Verified, ⚠️ Pending, ❌ Not Verified, Draft
Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected
```

**Extracted:** 16 sheets, 40 columns, 43 validation values, 13 colors

---

**END OF SPECIFICATION**


---

*"In attempting to construct such machines we should not be irreverently usurping His power of creating souls, any more than we are in the procreation of children."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
