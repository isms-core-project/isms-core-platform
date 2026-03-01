<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.16.2-TG:framework:TG:a.8.16.2 -->
**ISMS-IMP-A.8.16.2-TG - Baseline & Detection Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Baseline & Detection Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.16.2-TG |
| **Related Policy** | ISMS-POL-A.8.16 (Monitoring) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.16 (Monitoring Activities) |
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

- ISMS-POL-A.8.16 (Monitoring)
- ISMS-IMP-A.8.16.1 (Monitoring Infrastructure Assessment)
- ISMS-IMP-A.8.16.3 (Coverage Assessment)
- ISMS-IMP-A.8.16.4 (Alert Management & Response Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a816_2_baseline_detection.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.16.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 1. Baseline Inventory |
| 3 | 2. Detection Rules |
| 4 | 3. MITRE ATT&CK Coverage |
| 5 | 4. Rule Performance |
| 6 | 5. Testing Validation |
| 7 | Evidence Register |
| 8 | Summary Dashboard |
| 9 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #808080 | Gray (Disabled) |
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
| 1 | Baseline Name/ID |
| 2 | Baseline Type |
| 3 | Scope/Target |
| 4 | Data Source |
| 5 | Baseline Period |
| 6 | Established Date |
| 7 | Last Updated |
| 8 | Update Frequency |
| 9 | Anomaly Detection Method |
| 10 | Threshold/Criteria |
| 11 | Alert Rules Linked |
| 12 | Baseline Status |
| 13 | Days Since Update |
| 14 | Compliance Status |
| 15 | Issues/Gaps |
| 16 | Owner |
| 17 | Priority |
| 18 | Rule ID/Name |
| 19 | Rule Type |
| 20 | Description |
| 21 | Severity |
| 22 | Data Source(s) |
| 23 | Rule Logic Summary |
| 24 | MITRE Tactic |
| 25 | MITRE Technique |
| 26 | Created Date |
| 27 | Last Modified |
| 28 | Last Triggered |
| 29 | Trigger Count (30d) |
| 30 | True Positives (30d) |
| 31 | False Positives (30d) |
| 32 | Precision % |
| 33 | Rule Status |
| 34 | Tuning Status |
| 35 | Issues/Notes |
| 36 | MITRE Technique ID |
| 37 | Technique Name |
| 38 | Technique Description |
| 39 | Risk Level |
| 40 | Detection Rules |
| 41 | Rule Count |
| 42 | Data Sources Available |
| 43 | Coverage Status |
| 44 | Detection Quality |
| 45 | Last Tested |
| 46 | Test Result |
| 47 | Notes/Gaps |
| 48 | Total Triggers |
| 49 | True Positives |
| 50 | False Positives |
| 51 | False Negatives |
| 52 | Recall % |
| 53 | F1 Score |
| 54 | MTTD (minutes) |
| 55 | Tuning Actions |
| 56 | Last Tuned |
| 57 | Performance Trend |
| 58 | Issues |
| 59 | Test ID |
| 60 | Test Date |
| 61 | Test Type |
| 62 | Test Scenario |
| 63 | Expected Result |
| 64 | Actual Result |
| 65 | Detection Time |
| 66 | Issues Identified |
| 67 | Remediation Action |
| 68 | Retested |
| 69 | Tested By |
| 70 | Notes |
| 71 | Active Baselines |
| 72 | Active Detection Rules |
| 73 | Rules Needing Tuning |
| 74 | Critical/High Severity Rules |
| 75 | Stale Baselines |
| 76 | Critical MITRE Gaps |
| 77 | Example Metrics |
| 78 | Recommended Period |
| 79 | Date |
| 80 | Rule ID |
| 81 | Action Taken |
| 82 | Reason |
| 83 | Before Precision |
| 84 | After Precision |
| 85 | Performed By |
| 86 | Assessment Area |
| 87 | Total Items |
| 88 | Compliant |
| 89 | Partial |
| 90 | Non-Compliant |
| 91 | N/A |
| 92 | Compliance % |
| 93 | Evidence ID |
| 94 | Evidence Type |
| 95 | Location/Path |
| 96 | Date Collected |
| 97 | Collected By |
| 98 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Planned, Partial, N/A, User Activity, System Activity
Network Traffic, Application Behaviour, Security Events, Resource Usage, Other
\u2705 Active, \u26A0\uFE0F Stale, \u274C Missing, ↻ In Development, Daily
Weekly, Monthly, Quarterly, Annual, As Needed, Automated, Manual, Hybrid, None
Correlation, Anomaly Detection, Threshold, Signature, Machine Learning
Threat Intel, Critical, High, Medium, Low, Informational, \u26A0\uFE0F Testing
\u274C Disabled, ↻ Tuning, Reconnaissance, Resource Development
Initial Access, Execution, Persistence, Privilege Escalation, Defence Evasion
Credential Access, Discovery, Lateral Movement, Collection
Command and Control, Exfiltration, Impact, \u2705 Covered
\u26A0\uFE0F Partial, \u274C Not Covered, ↻ Planned, Excellent, Good, Fair
Poor, Optimized, Needs Tuning, Under Review, New Rule, Pass, Fail, Not Tested
\u2705 Compliant, \u274C Non-Compliant, Attack Simulation, Purple Team
Unit Test, Integration Test, Regression Test, Penetration Test
Configuration file, Screenshot, Log Export, Documentation, Report
Network scan, Audit log, Compliance report, Verified, Pending verification
Not verified, Requires update, Approved, Approved with Conditions, Rejected
Deferred
```

**Extracted:** 9 sheets, 98 columns, 93 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Those who can imagine anything, can create the impossible."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
