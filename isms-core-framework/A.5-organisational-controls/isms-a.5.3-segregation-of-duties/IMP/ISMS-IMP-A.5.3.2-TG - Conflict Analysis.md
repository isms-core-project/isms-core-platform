<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.3.2-TG:framework:TG:a.5.3.2 -->
**ISMS-IMP-A.5.3.2-TG - Conflict Analysis**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.3: Policies for Segregation of Duties

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Conflict Analysis |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.3.2-TG |
| **Related Policy** | ISMS-POL-A.5.3 (Segregation of Duties) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.3 (Policies for Segregation of Duties) |
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

- ISMS-POL-A.5.3 (Segregation of Duties)
- ISMS-IMP-A.5.3.1 (SoD Matrix Assessment)
- ISMS-IMP-A.5.3.3 (Role-Function Mapping)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a53_2_conflict_analysis.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.3.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Conflict Register |
| 3 | Impact Assessment |
| 4 | Exploitation Scenarios |
| 5 | Control Mapping |
| 6 | Trend Analysis |
| 7 | Prioritisation Matrix |
| 8 | Evidence Register |
| 9 | Summary Dashboard |
| 10 | Approval Sign-Off |

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
| 1 | Risk Officer |
| 2 | Fictitious Vendor Fraud |
| 3 | Dual Authorisation |
| 4 | Risk Owner |
| 5 | FINAL DECISION: |
| 6 | Conflict ID |
| 7 | Gap ID |
| 8 | Conflict Category |
| 9 | Role A |
| 10 | Role B |
| 11 | Process |
| 12 | Conflict Type |
| 13 | Persons Affected |
| 14 | Analysis Status |
| 15 | Financial Impact |
| 16 | Operational Impact |
| 17 | Reputational Impact |
| 18 | Compliance Impact |
| 19 | Data Impact |
| 20 | Overall Impact |
| 21 | Justification |
| 22 | Assessor |
| 23 | Assessment Date |
| 24 | Scenario ID |
| 25 | Scenario Name |
| 26 | Threat Actor |
| 27 | Motivation |
| 28 | Method |
| 29 | Detection Difficulty |
| 30 | Historical Precedent |
| 31 | Reference |
| 32 | Mapping ID |
| 33 | Control ID |
| 34 | Control Name |
| 35 | Control Type |
| 36 | Effectiveness |
| 37 | Implementation Status |
| 38 | Gap Notes |
| 39 | Period |
| 40 | Total Conflicts |
| 41 | Critical Conflicts |
| 42 | High Conflicts |
| 43 | Resolved Count |
| 44 | New Conflicts |
| 45 | Resolution Rate |
| 46 | Trend Notes |
| 47 | Impact Score |
| 48 | Likelihood Score |
| 49 | Control Effectiveness |
| 50 | Priority Score |
| 51 | Priority Level |
| 52 | Action Timeline |
| 53 | Assigned To |
| 54 | Evidence ID |
| 55 | Assessment Area |
| 56 | Evidence Type |
| 57 | Description |
| 58 | Location / Path |
| 59 | Date Collected |
| 60 | Collected By |
| 61 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Unknown, Policy Document, Process Record, System Screenshot
Configuration Export, Audit Log, Training Record, Test Result, Risk Assessment
Meeting Minutes, Other, ✅ Verified, ⚠️ Pending, ❌ Not Verified, N/A, Approved
Approved with Conditions, Rejected, Deferred, Draft, Final
Requires remediation, Re-assessment required
```

**Extracted:** 10 sheets, 61 columns, 25 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The price of liberty is eternal vigilance."*
— Thomas Jefferson

<!-- QA_VERIFIED: 2026-02-06 -->
