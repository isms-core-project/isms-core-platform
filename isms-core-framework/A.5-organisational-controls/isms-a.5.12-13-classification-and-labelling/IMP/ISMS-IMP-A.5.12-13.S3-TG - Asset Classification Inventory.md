<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.12-13.S3-TG:framework:TG:a.5.12-13 -->
**ISMS-IMP-A.5.12-13.S3-TG - Asset Classification Inventory**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.12-13: Classification and Labelling

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Asset Classification Inventory |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.12-13.S3-TG |
| **Related Policy** | ISMS-POL-A.5.12-13 (Classification and Labelling) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.12-13 (Classification and Labelling) |
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

- ISMS-POL-A.5.12-13 (Classification and Labelling)
- ISMS-IMP-A.5.12-13.S1 (Classification Scheme Definition)
- ISMS-IMP-A.5.12-13.S2 (Labelling Procedures and Standards)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a512_13_3_asset_classification_inventory.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.12-13.S3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Asset Inventory |
| 2 | Classification Summary |
| 3 | Reclassification Log |
| 4 | Gap Analysis |
| 5 | Evidence Register |
| 6 | Summary Dashboard |
| 7 | Approval Sign-Off |
| 8 | Instructions & Legend |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #69DB7C | Custom |
| #74C0FC | Custom |
| #C00000 | Dark Red (Blocked) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FF6B6B | Custom |
| #FFA94D | Custom |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | Asset ID |
| 2 | Asset Name |
| 3 | Asset Type |
| 4 | Description |
| 5 | Classification |
| 6 | Owner |
| 7 | Custodian |
| 8 | Location/System |
| 9 | Labelling Status |
| 10 | Last Review |
| 11 | Next Review |
| 12 | Regulatory Req |
| 13 | Notes |
| 14 | Count |
| 15 | Percentage |
| 16 | Labelled |
| 17 | Unlabelled |
| 18 | Compliance |
| 19 | Total |
| 20 | RESTRICTED |
| 21 | CONFIDENTIAL |
| 22 | INTERNAL |
| 23 | PUBLIC |
| 24 | Department |
| 25 | Compliance % |
| 26 | Change ID |
| 27 | Previous Class |
| 28 | New Class |
| 29 | Reason for Change |
| 30 | Requested By |
| 31 | Approved By |
| 32 | Change Date |
| 33 | Status |
| 34 | Gap ID |
| 35 | Asset/Area |
| 36 | Gap Type |
| 37 | Risk Level |
| 38 | Remediation Action |
| 39 | Due Date |
| 40 | Evidence ID |
| 41 | Assessment Area |
| 42 | Evidence Type |
| 43 | Location / Path |
| 44 | Date Collected |
| 45 | Collected By |
| 46 | Verification Status |
| 47 | Total Items |
| 48 | Compliant |
| 49 | Partial |
| 50 | Non-Compliant |
| 51 | N/A |
| 52 | Metric |
| 53 | Value |
| 54 | Category |
| 55 | Finding |
| 56 | Severity |
| 57 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Database, Document, Document Set, Application, System, Repository, Email
Media, Other, RESTRICTED, CONFIDENTIAL, INTERNAL, PUBLIC, Labelled, Partial
Not Labelled, N/A, Value change, Regulatory requirement, Business need
Data lifecycle, Merger/divestiture, Error correction, Periodic review
Complete, Pending Approval, Rejected, In Progress, Unclassified Assets
Incomplete Labelling, Misclassification, No Labelling Capability
Inconsistent Labels, Missing Metadata, Critical, High, Medium, Low, Resolved
Open, Accepted, Policy Document, Process Record, System Screenshot
Configuration Export, Audit Log, Training Record, Test Result, Risk Assessment
Meeting Minutes, ✅ Verified, ⚠️ Pending, ❌ Not Verified, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Deferred
```

**Extracted:** 8 sheets, 57 columns, 60 validation values, 13 colors

---

**END OF SPECIFICATION**


---

*"You can't protect what you don't know you have."*
— Security Industry Proverb

<!-- QA_VERIFIED: 2026-02-06 -->
