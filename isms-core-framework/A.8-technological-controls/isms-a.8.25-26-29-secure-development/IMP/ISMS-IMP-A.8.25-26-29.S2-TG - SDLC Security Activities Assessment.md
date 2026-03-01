<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.25-26-29.S2-TG:framework:TG:a.8.25-26-29 -->
**ISMS-IMP-A.8.25-26-29.S2-TG - SDLC Security Activities Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.25: Secure Development Life Cycle

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | SDLC Security Activities Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.25-26-29.S2-TG |
| **Related Policy** | ISMS-POL-A.8.25-26-29 (Secure Development) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.25 (Secure Development Life Cycle) |
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

- ISMS-POL-A.8.25-26-29 (Secure Development)
- ISMS-IMP-A.8.25-26-29.S1 (Security Requirements Assessment)
- ISMS-IMP-A.8.25-26-29.S3 (Security Testing Results Assessment)
- ISMS-IMP-A.8.25-26-29.S4 (Vulnerability Remediation Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a825_26_29_2_sdlc_security_activities.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.25-26-29.S2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | SDLC Phase Activities |
| 3 | Secure Coding Standards |
| 4 | Code Review Metrics |
| 5 | Security Tools Deployment |
| 6 | Security Tools Usage |
| 7 | Developer Training |
| 8 | Security Defect Mgmt |
| 9 | Evidence Register |
| 10 | Summary Dashboard |
| 11 | Approval Sign-Off |

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
| 1 | SDLC SECURITY ACTIVITIES BY PHASE |
| 2 | TRACK SECURITY ACTIVITY COMPLETION FOR EACH SDLC PHASE PER APPLICATION |
| 3 | SECURE CODING STANDARDS ADOPTION |
| 4 | ASSESS SECURE CODING STANDARDS ADOPTION PER APPLICATION |
| 5 | CODE REVIEW METRICS |
| 6 | TRACK CODE REVIEW PROCESS AND SECURITY FOCUS |
| 7 | SECURITY TOOLS DEPLOYMENT STATUS |
| 8 | TRACK SECURITY TOOL DEPLOYMENT ACROSS ORGANISATION |
| 9 | SECURITY TOOLS USAGE METRICS |
| 10 | TRACK SECURITY TOOL USAGE PER APPLICATION |
| 11 | DEVELOPER SECURITY TRAINING COMPLIANCE |
| 12 | TRACK DEVELOPER SECURITY TRAINING COMPLETION AND COMPLIANCE |
| 13 | SECURITY DEFECT MANAGEMENT |
| 14 | TRACK OPEN SECURITY DEFECTS AND REMEDIATION COMPLIANCE |
| 15 | App-ID |
| 16 | Application Name |
| 17 | SDLC Methodology |
| 18 | Requirements: Sec Req Defined |
| 19 | Requirements: Risk Classification |
| 20 | Design: Threat Modeling |
| 21 | Design: Architecture Review |
| 22 | Development: SAST Enabled |
| 23 | Development: Code Review |
| 24 | Testing: DAST Scan |
| 25 | Testing: Security Testing |
| 26 | Deployment: Security Checklist |
| 27 | Maintenance: Vulnerability Monitoring |
| 28 | Phase Compliance (%) |
| 29 | Standard Adopted |
| 30 | Standard Documented? |
| 31 | Developers Trained? |
| 32 | Enforced via Tools? |
| 33 | Enforced via Code Review? |
| 34 | Last Standard Update |
| 35 | Compliance Score (%) |
| 36 | Code Review Process Documented? |
| 37 | Code Review Coverage (%) |
| 38 | Security Checklist Used? |
| 39 | Security Champion Involved? |
| 40 | Avg Review Turnaround (days) |
| 41 | Security Findings Count |
| 42 | Review Compliance Score (%) |
| 43 | Tool Type |
| 44 | Tool Name/Vendor |
| 45 | Deployment Status |
| 46 | Applications Covered |
| 47 | Integration Point |
| 48 | Config Reviewed? |
| 49 | Findings Per Month (Avg) |
| 50 | False Positive Rate (%) |
| 51 | SAST Scans Per Month |
| 52 | SCA Scans Per Month |
| 53 | Secret Scanning Enabled? |
| 54 | DAST Scans Per Release |
| 55 | Avg Remediation Time (days) |
| 56 | Tool Integration Score |
| 57 | Usage Compliance (%) |
| 58 | Developer/Team Name |
| 59 | Initial Training Date |
| 60 | Annual Refresher Date |
| 61 | Language-Specific Training |
| 62 | Security Champion Training |
| 63 | Training Quiz Score (%) |
| 64 | Training Overdue? |
| 65 | Training Status |
| 66 | Critical Defects |
| 67 | High Defects |
| 68 | Medium Defects |
| 69 | Low Defects |
| 70 | Total Open Defects |
| 71 | Avg Age (days) |
| 72 | SLA Compliance (%) |
| 73 | Security Tech Debt |
| 74 | Monthly Trend |
| 75 | Assessment Area |
| 76 | Total Assessed |
| 77 | Complete |
| 78 | Partial |
| 79 | Missing |
| 80 | N/A |
| 81 | Completion % |
| 82 | Finding |
| 83 | Count |
| 84 | Severity |
| 85 | Affected Area |
| 86 | Recommended Action |
| 87 | Owner |
| 88 | Evidence ID |
| 89 | Evidence Type |
| 90 | Description |
| 91 | Location / Path |
| 92 | Date Collected |
| 93 | Collected By |
| 94 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, N/A, Complete, In Progress, Not Done, Waterfall, Agile, Scrum, DevOps
DevSecOps, Hybrid, Deployed, Not Deployed, Current, Outdated, Missing
Compliant, ⚠️ Partial Compliance, Non-Compliant, SDLC process doc
Code review report, Training record, Tool configuration, Security policy
Test report, Screenshot, Other, \u2705 Verified, \u26a0\ufe0f Pending
\u274c Not Verified, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 11 sheets, 94 columns, 39 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Mathematics is the queen of the sciences and number theory is the queen of mathematics."*
— Attributed to Ramanujan, after Gauss

<!-- QA_VERIFIED: 2026-02-06 -->
