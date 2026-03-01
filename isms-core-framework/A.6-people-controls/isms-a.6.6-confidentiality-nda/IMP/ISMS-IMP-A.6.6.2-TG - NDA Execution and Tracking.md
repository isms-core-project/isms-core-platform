<!-- ISMS-CORE:IMP:ISMS-IMP-A.6.6.2-TG:framework:TG:a.6.6.2 -->
**ISMS-IMP-A.6.6.2-TG - NDA Execution and Tracking**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.6

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | NDA Execution and Tracking |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.6.6.2-TG |
| **Related Policy** | ISMS-POL-A.6.6 (Confidentiality Nda) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.6.6) |
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

- ISMS-POL-A.6.6 (Confidentiality Nda)
- ISMS-IMP-A.6.6.1 (NDA Template Registry and Inventory)
- ISMS-IMP-A.6.6.3 (NDA Review and Compliance)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a66_2_nda_execution_tracking.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.6.6.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Summary Dashboard |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | NDA ID |
| 2 | Template Ref |
| 3 | NDA Title |
| 4 | Counterparty |
| 5 | Counterparty Type |
| 6 | Execution Date |
| 7 | Effective Date |
| 8 | Expiration Date |
| 9 | Post Term Period |
| 10 | Post Term Expiry |
| 11 | Signatories Count |
| 12 | Storage Location |
| 13 | Status |
| 14 | Notes |
| 15 | Signatory ID |
| 16 | NDA Ref |
| 17 | Signatory Name |
| 18 | Signatory Type |
| 19 | Organisation |
| 20 | Role Title |
| 21 | Email |
| 22 | Signature Date |
| 23 | Signature Method |
| 24 | Termination Date |
| 25 | Days Until Expiry |
| 26 | Alert Status |
| 27 | Renewal Required |
| 28 | Renewal Owner |
| 29 | Renewal Started |
| 30 | Action Required |
| 31 | Renewal ID |
| 32 | Original NDA |
| 33 | Original Expiry |
| 34 | Renewal Initiated |
| 35 | New Terms Required |
| 36 | Legal Review |
| 37 | Counterparty Agreed |
| 38 | New NDA ID |
| 39 | New Expiry |
| 40 | Evidence ID |
| 41 | Evidence Type |
| 42 | Description |
| 43 | Source / Location |
| 44 | Collected By |
| 45 | Collection Date |
| 46 | Retention Date |
| 47 | Assessment Area |
| 48 | Total Items |
| 49 | Compliant |
| 50 | Partial |
| 51 | Non-Compliant |
| 52 | N/A |
| 53 | Compliance % |
| 54 | Category |
| 55 | Finding |
| 56 | Count |
| 57 | Severity |

### Data Validation Values

All dropdown/list values used across sheets:

```
Employee, Contractor, Consultant, Vendor, Supplier, Partner, Customer
Board Member, Visitor, Other, Active, Expired, Terminated, Renewed, Superseded
Vendor Rep, Partner Rep, Customer Rep, Witness, Authorised Signatory
Wet Signature, Digital Signature, Electronic Signature, DocuSign, Adobe Sign
Green (>90 days), Amber (30-90 days), Red (<30 days), Yes, No, Under Review
Pending, Not Started, In Progress, Legal Review, Awaiting Signature, Completed
Cancelled, Policy Document, Procedure, Record, Certificate, Report, Screenshot
Log, Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 2 sheets, 57 columns, 53 validation values, 6 colors

---

**END OF SPECIFICATION**


---

*"A verbal contract isn't worth the paper it's written on."*
— Samuel Goldwyn

*Where bamboo antennas actually work.* 🎋

<!-- QA_VERIFIED: 2026-03-01 -->
