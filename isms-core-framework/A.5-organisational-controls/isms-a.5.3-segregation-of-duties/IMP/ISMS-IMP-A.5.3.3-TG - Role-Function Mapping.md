<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.3.3-TG:framework:TG:a.5.3.3 -->
**ISMS-IMP-A.5.3.3-TG - Role-Function Mapping**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.3: Policies for Segregation of Duties

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Role-Function Mapping |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.3.3-TG |
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
- ISMS-IMP-A.5.3.2 (Conflict Analysis)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a53_3_role_function_mapping.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.3.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Business Roles |
| 3 | Application Roles |
| 4 | Functions |
| 5 | Permissions |
| 6 | Role Function Map |
| 7 | Function Conflicts |
| 8 | Validation Status |
| 9 | Change Log |
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
| 1 | SAP ERP |
| 2 | T-Code FK01 |
| 3 | Risk Officer |
| 4 | Permission Added |
| 5 | Finance Director |
| 6 | FINAL DECISION: |
| 7 | Business Role ID |
| 8 | Role Name |
| 9 | Department |
| 10 | Process Domain |
| 11 | Role Owner |
| 12 | Description |
| 13 | Risk Level |
| 14 | Last Reviewed |
| 15 | App Role ID |
| 16 | Application |
| 17 | Role Type |
| 18 | Business Roles |
| 19 | Criticality |
| 20 | Review Frequency |
| 21 | Function ID |
| 22 | Function Name |
| 23 | Category |
| 24 | Process |
| 25 | SoD Sensitive |
| 26 | Permission ID |
| 27 | Permission Name |
| 28 | Permission Type |
| 29 | Data Scope |
| 30 | Special Conditions |
| 31 | Mapping ID |
| 32 | Grant Type |
| 33 | Justification |
| 34 | Effective Date |
| 35 | Expiry Date |
| 36 | Conflict ID |
| 37 | Function A |
| 38 | Function B |
| 39 | Conflict Type |
| 40 | Mitigation |
| 41 | Validation ID |
| 42 | Role ID |
| 43 | Validation Date |
| 44 | Validator |
| 45 | Documented Functions |
| 46 | Actual Functions |
| 47 | Discrepancies |
| 48 | Status |
| 49 | Resolution |
| 50 | Change ID |
| 51 | Change Date |
| 52 | Change Type |
| 53 | Requested By |
| 54 | Approved By |
| 55 | Ticket Reference |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Approved, Approved with Conditions, Rejected, Deferred, Draft, Final
Requires remediation, Re-assessment required
```

**Extracted:** 11 sheets, 55 columns, 10 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The devil is in the details."*
— Ludwig Mies van der Rohe

<!-- QA_VERIFIED: 2026-02-06 -->
