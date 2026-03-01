<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.20-21-22.S5-TG:framework:TG:a.8.20-21-22 -->
**ISMS-IMP-A.8.20-21-22.S5-TG - Network Segmentation Implementation**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Segmentation Implementation |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.20-21-22.S5-TG |
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
- ISMS-IMP-A.8.20-21-22.S2 (Architecture Documentation)
- ISMS-IMP-A.8.20-21-22.S3 (Device Hardening)
- ISMS-IMP-A.8.20-21-22.S4 (Services Security)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a820_5_controls_coverage.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.20-21-22.S5`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Evidence Register |
| 2 | Approval Sign-Off |
| 3 | Instructions & Legend |
| 4 | Controls Coverage Matrix |
| 5 | Zone Control Assessment |
| 6 | Device Control Mapping |
| 7 | Service Control Mapping |
| 8 | Control Effectiveness |
| 9 | Gap Analysis |
| 10 | Defense In Depth |
| 11 | Summary Dashboard |
| 12 | Executive Summary |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #006100 | Dark Green (Pass) |
| #4472C4 | Medium Blue (Sub-headers) |
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
| 7 | Zone ID |
| 8 | Zone Name |
| 9 | Internet DMZ |
| 10 | ZONE CONTROL ASSESSMENT - EFFECTIVENESS BY ZONE |
| 11 | Partially Effective |
| 12 | Network Security Team |
| 13 | Traffic Filtering, IDS/IPS, VPN Termination |
| 14 | A.8.20, A.8.22 |
| 15 | OVERALL CONTROL EFFECTIVENESS ASSESSMENT |
| 16 | SECURITY CONTROL COVERAGE GAPS |
| 17 | Missing IDS/IPS Coverage |
| 18 | Security Team |
| 19 | DEFENSE-IN-DEPTH VALIDATION |
| 20 | What This Shows |
| 21 | Critical Finding Type |
| 22 | Filter Instructions |
| 23 | NETWORK SECURITY CONTROLS - EXECUTIVE SUMMARY |
| 24 | Risk Level |
| 25 | Controls Required |
| 26 | Controls Implemented |
| 27 | Control Coverage % |
| 28 | Effectiveness Rating |
| 29 | Gaps Identified |
| 30 | Last Assessment |
| 31 | Assessed By |
| 32 | Notes |
| 33 | Device ID |
| 34 | Device Type |
| 35 | Hostname |
| 36 | Security Zone |
| 37 | Controls Provided |
| 38 | Control Category |
| 39 | Hardening Score |
| 40 | Effectiveness |
| 41 | Last Assessed |
| 42 | Service ID |
| 43 | Service Type |
| 44 | Service Name |
| 45 | Security Score |
| 46 | Zones Served |
| 47 | Control Name |
| 48 | Zones Covered |
| 49 | Total Zones |
| 50 | Coverage % |
| 51 | Weaknesses |
| 52 | Improvement Actions |
| 53 | Gap ID |
| 54 | Zone/Asset |
| 55 | Missing Control |
| 56 | Risk |
| 57 | Severity |
| 58 | Remediation Plan |
| 59 | Owner |
| 60 | Target Date |
| 61 | Status |
| 62 | Layer 1 Control |
| 63 | Layer 2 Control |
| 64 | Layer 3 Control |
| 65 | Additional Layers |
| 66 | Defense-in-Depth OK |
| 67 | Evidence ID |
| 68 | Evidence Type |
| 69 | Description |
| 70 | Location/Path |
| 71 | Date Collected |
| 72 | Collected By |
| 73 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Covered, Not Covered, Partially Covered, N/A, Effective, Partially Effective
Ineffective, Not Assessed, Critical, High, Medium, Low
A.8.20 - Network Security, A.8.21 - Network Services
A.8.22 - Network Segmentation, Configuration file, Screenshot, Network scan
Documentation, Vendor spec, Certificate inventory, Audit log
Compliance report, Other, ✅ Verified, ⚠️ Pending, ❌ Not Verified, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 12 sheets, 73 columns, 35 validation values, 12 colors

---

**END OF SPECIFICATION**


---

*"The best ideas are the ones that show something unexpected, something that challenges the ordinary view."*
— John Nash

<!-- QA_VERIFIED: 2026-02-06 -->
