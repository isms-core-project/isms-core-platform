<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.30.1-TG:framework:TG:a.8.30.1 -->
**ISMS-IMP-A.8.30.1-TG - Vendor Assessment and Registry**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.30: Outsourced Development

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Vendor Assessment and Registry |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.30.1-TG |
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
- ISMS-IMP-A.8.30.2 (Contract Compliance)
- ISMS-IMP-A.8.30.3 (Security Testing and Acceptance)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a830_1_vendor_assessment.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.30.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Vendor Registry |
| 3 | Security Assessment |
| 4 | Due Diligence |
| 5 | Environment Security |
| 6 | Summary Dashboard |
| 7 | Evidence Register |
| 8 | Approval Sign-Off |

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
| 1 | Last Assessment Date |
| 2 | Next Review Due |
| 3 | Assessment Owner |
| 4 | Overall Risk Rating |
| 5 | EVIDENCE REGISTER |
| 6 | ASSESSMENT APPROVAL AND SIGN-OFF |
| 7 | ASSESSMENT SUMMARY |
| 8 | FINAL DECISION: |
| 9 | NEXT REVIEW DETAILS |
| 10 | Vendor ID |
| 11 | Vendor Name |
| 12 | Registry Status |
| 13 | Risk Tier |
| 14 | Initial Assessment Date |
| 15 | Next Assessment Due |
| 16 | ISO 27001 Certified |
| 17 | SOC2 Type2 |
| 18 | Primary Contact |
| 19 | Approved Project Types |
| 20 | Approved By |
| 21 | Notes |
| 22 | Assessment ID |
| 23 | Assessment Date |
| 24 | Assessment Type |
| 25 | Assessor |
| 26 | Security Certification |
| 27 | Cert Expiry Date |
| 28 | SDLC Maturity |
| 29 | Security Incident History |
| 30 | SAST DAST Tooling |
| 31 | Personnel Screening |
| 32 | Dev Environment Security |
| 33 | Recommendation |
| 34 | Conditions |
| 35 | Evidence Location |
| 36 | Check Category |
| 37 | Check Item |
| 38 | Status |
| 39 | Evidence Type |
| 40 | Evidence Reference |
| 41 | Verified By |
| 42 | Verified Date |
| 43 | MFA Enabled |
| 44 | Network Isolation |
| 45 | Endpoint Security |
| 46 | Code Repository |
| 47 | Secret Scanning |
| 48 | Branch Protection |
| 49 | Data Handling |
| 50 | Attestation Received |
| 51 | Attestation Date |
| 52 | Compliance Status |
| 53 | Assessment Area |
| 54 | Total Items |
| 55 | Compliant |
| 56 | Partial |
| 57 | Non-Compliant |
| 58 | N/A |
| 59 | Compliance % |
| 60 | Evidence ID |
| 61 | Evidence Title |
| 62 | Description |
| 63 | Source / Location |
| 64 | Date Collected |
| 65 | Collected By |

### Data Validation Values

All dropdown/list values used across sheets:

```
Approved, Pending, Suspended, Removed, Critical, High, Standard, Yes, No
In Progress, Initial, Annual, Triggered, ISO 27001, SOC 2, Both, None, Mature
Developing, Basic, Unknown, Minor, Major, Verified, Attested, Compliant
Partial, Non-Compliant, Low, Medium, Approve, Conditional, Reject, Complete
N/A, Certificate, Attestation, Document, Interview, Isolated, Segmented
Shared, Secure, Unsecure, No Prod Data, Masked, Raw, Policy Document
Process Document, Screenshot, Log Extract, Configuration Export, Audit Report
Training Record, Signed Attestation, Tool Output, Other, Collected
Not Available, Expired, Draft, Final, Requires remediation
Re-assessment required, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 8 sheets, 65 columns, 67 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->
