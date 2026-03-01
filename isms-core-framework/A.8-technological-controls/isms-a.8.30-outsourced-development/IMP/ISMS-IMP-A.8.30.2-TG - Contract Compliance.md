<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.30.2-TG:framework:TG:a.8.30.2 -->
**ISMS-IMP-A.8.30.2-TG - Contract Compliance**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.30: Outsourced Development

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Contract Compliance |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.30.2-TG |
| **Related Policy** | ISMS-POL-A.8.30 (Outsourced Development) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.30 (Outsourced Development) |
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

- ISMS-POL-A.8.30 (Outsourced Development)
- ISMS-IMP-A.8.30.1 (Vendor Assessment and Registry)
- ISMS-IMP-A.8.30.3 (Security Testing and Acceptance)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a830_2_contract_compliance.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.30.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Contract Inventory |
| 3 | Security Clauses |
| 4 | SLA Compliance |
| 5 | Subcontractor Approvals |
| 6 | Termination Checklist |
| 7 | Summary Dashboard |
| 8 | Evidence Register |
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
| 1 | Total Active Contracts |
| 2 | Total Subcontractors |
| 3 | Active Critical Projects |
| 4 | SLA Compliance Rate |
| 5 | Security Clauses Met |
| 6 | Pending Terminations |
| 7 | Contract ID |
| 8 | Vendor ID |
| 9 | Contract Name |
| 10 | Contract Type |
| 11 | Start Date |
| 12 | End Date |
| 13 | Project Classification |
| 14 | Contract Value CHF |
| 15 | Primary Contact |
| 16 | Legal Review Date |
| 17 | Security Review Date |
| 18 | Status |
| 19 | Clause Category |
| 20 | Clause Description |
| 21 | Included |
| 22 | Clause Reference |
| 23 | Modification Notes |
| 24 | Reviewed By |
| 25 | Review Date |
| 26 | SLA ID |
| 27 | Vulnerability ID |
| 28 | Severity |
| 29 | Discovery Date |
| 30 | SLA Days |
| 31 | SLA Due Date |
| 32 | Remediation Date |
| 33 | SLA Met |
| 34 | Exception Approved |
| 35 | Exception Approver |
| 36 | Notes |
| 37 | Approval ID |
| 38 | Primary Vendor ID |
| 39 | Subcontractor Name |
| 40 | Subcontractor Scope |
| 41 | Access Level |
| 42 | Assessment Level |
| 43 | Risk Classification |
| 44 | Approval Status |
| 45 | Approved By |
| 46 | Approval Date |
| 47 | Expiry Date |
| 48 | Flow Down Verified |
| 49 | Termination Type |
| 50 | Termination Date |
| 51 | Check Item |
| 52 | Completion Date |
| 53 | Verified By |
| 54 | Evidence Reference |
| 55 | Assessment Area |
| 56 | Total Items |
| 57 | Compliant |
| 58 | Partial |
| 59 | Non-Compliant |
| 60 | N/A |
| 61 | Compliance % |
| 62 | Finding |
| 63 | Affected Area |
| 64 | Recommended Action |
| 65 | Owner |
| 66 | Due Date |
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
Fixed-price, T&M, Staff Aug, Managed Service, Critical, High, Standard, Active
Completed, Terminated, Yes, No, N/A, Modified, Medium, Low, 7, 30, 90, 180
Met, Missed, Pending, Exception, Direct, Via Vendor, None, Full, Abbreviated
Vendor Attested, Approved, Rejected, Completion, Early, Breach, Complete
Configuration file, Screenshot, Network scan, Documentation, Vendor spec
Certificate inventory, Audit log, Compliance report, Other, Verified
Pending verification, Not verified, Requires update, Draft, Final
Requires remediation, Re-assessment required, Approved with Conditions
Deferred
```

**Extracted:** 9 sheets, 73 columns, 55 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"A verbal contract isn't worth the paper it's written on."*
— Samuel Goldwyn

<!-- QA_VERIFIED: 2026-02-06 -->
