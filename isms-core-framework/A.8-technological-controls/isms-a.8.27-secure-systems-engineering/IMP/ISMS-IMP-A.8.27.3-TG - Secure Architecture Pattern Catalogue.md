<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.27.3-TG:framework:TG:a.8.27.3 -->
**ISMS-IMP-A.8.27.3-TG - Secure Architecture Pattern Catalogue**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Secure Architecture Pattern Catalogue |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.3-TG |
| **Related Policy** | ISMS-POL-A.8.27 (Secure Systems Engineering) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.27 (Secure System Architecture and Engineering Principles) |
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

- ISMS-POL-A.8.27 (Secure Systems Engineering)
- ISMS-IMP-A.8.27.1 (Security Architecture Review Process)
- ISMS-IMP-A.8.27.2 (Threat Modelling Methodology)
- ISMS-IMP-A.8.27.4 (Zero Trust Implementation Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a827_3_pattern_catalogue.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.27.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Pattern Inventory |
| 2 | PatternInventory |
| 3 | E |
| 4 | Approved |
| 5 | Draft |
| 6 | Deprecated |
| 7 | Under Review |
| 8 | Pattern Quality |
| 9 | PatternQuality |
| 10 | C |
| 11 | ✅ Yes |
| 12 | ⚠️ Partial |
| 13 | ❌ No |
| 14 | N/A |
| 15 | Adoption |
| 16 | F |
| 17 | Increasing |
| 18 | Stable |
| 19 | Decreasing |
| 20 | Governance |
| 21 | ✅ Implemented |
| 22 | ❌ Not Implemented |
| 23 | Deviations |
| 24 | J |
| 25 | Closed |
| 26 | Active |
| 27 | Expired |
| 28 | Effectiveness |
| 29 | High |
| 30 | Medium |
| 31 | Low |
| 32 | Compliance |
| 33 | D |
| 34 | Instructions & Legend |
| 35 | Evidence Register |
| 36 | Summary Dashboard |
| 37 | Approval Sign-Off |

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
| 1 | What This Shows |
| 2 | Critical Finding Type |
| 3 | Filter Instructions |
| 4 | Security Team |
| 5 | Customer Portal Upgrade |
| 6 | Legacy System |
| 7 | Security Architect |
| 8 | Overall Compliance: |
| 9 | Evidence ID |
| 10 | Assessment Area |
| 11 | Evidence Type |
| 12 | Description |
| 13 | Location / Path |
| 14 | Date Collected |
| 15 | Collected By |
| 16 | Verification Status |
| 17 | Total Items |
| 18 | Compliant |
| 19 | Partial |
| 20 | Non-Compliant |
| 21 | N/A |
| 22 | Compliance % |
| 23 | Pat-ID |
| 24 | Category |
| 25 | Name |
| 26 | Version |
| 27 | Status |
| 28 | Owner |
| 29 | LastReview |
| 30 | NextReview |
| 31 | DocumentRef |
| 32 | Notes |
| 33 | Element |
| 34 | Present |
| 35 | Quality |
| 36 | ProjectCount |
| 37 | TotalApplicable |
| 38 | AdoptionRate |
| 39 | Trend |
| 40 | Barriers |
| 41 | Action |
| 42 | Gov-ID |
| 43 | Requirement |
| 44 | Evidence |
| 45 | Gap |
| 46 | Dev-ID |
| 47 | Pattern |
| 48 | Project |
| 49 | Justification |
| 50 | Approved |
| 51 | ApprovedBy |
| 52 | Compensating |
| 53 | Expiry |
| 54 | SecurityIncidents |
| 55 | VulnFindings |
| 56 | AuditFindings |
| 57 | UserFeedback |
| 58 | Effectiveness |
| 59 | Comp-ID |
| 60 | Source |
| 61 | Score |

### Data Validation Values

All dropdown/list values used across sheets:

```
Policy Document, Process Record, System Screenshot, Configuration Export
Audit Log, Training Record, Test Result, Risk Assessment, Meeting Minutes
Other, ✅ Verified, ⚠️ Pending, ❌ Not Verified, N/A, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred, Authentication, Authorisation
DataProtection, NetworkSecurity, Integration, Cloud, LoggingMonitoring
Identity, Container, Serverless, Deprecated, Under Review, ✅ Yes, ⚠️ Partial
❌ No, 1, 2, 3, 4, 5, Increasing, Stable, Decreasing, ✅ Implemented
❌ Not Implemented, Technical Constraint, Legacy System, Vendor Limitation
Cost/Time, Performance, Yes, No, Pending, Active, Closed, Expired, High
Medium, Low
```

**Extracted:** 37 sheets, 61 columns, 61 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Good judgment comes from experience, and experience comes from bad judgment. Architecture patterns capture good judgment so others need not repeat the bad."*
— Fred Brooks (paraphrased)

<!-- QA_VERIFIED: [Date] -->
