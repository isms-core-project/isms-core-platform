<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.19-23.S2-TG:framework:TG:a.5.19-23 -->
**ISMS-IMP-A.5.19-23.S2-TG - Vendor Due Diligence & Contracts**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Vendor Due Diligence & Contracts |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.19-23.S2-TG |
| **Related Policy** | ISMS-POL-A.5.19-23 (Cloud Services) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.23 (Information Security for Use of Cloud Services) |
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

- ISMS-POL-A.5.19-23 (Cloud Services)
- ISMS-IMP-A.5.19-23.S1 (Cloud Service Inventory & Classification)
- ISMS-IMP-A.5.19-23.S3 (Secure Configuration & Deployment)
- ISMS-IMP-A.5.19-23.S4 (Ongoing Governance & Risk Management)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a523_2_vendor_dd.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.19-23.S2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 2. Security Certifications |
| 3 | 3. Contract Terms |
| 4 | 4. SLA Performance |
| 5 | 5. Data Sovereignty |
| 6 | 6. Forensics & Audit |
| 7 | 7. Jurisdictional Risk |
| 8 | Evidence Register |
| 9 | Summary Dashboard |
| 10 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #666666 | Dark Gray (Secondary Text) |
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
| 1 | Requirement |
| 2 | Status |
| 3 | Evidence Type |
| 4 | Assessment Area |
| 5 | Total Vendors |
| 6 | {CHECK} Compliant |
| 7 | {WARNING} Partial |
| 8 | {XMARK} Non-Compliant |
| 9 | N/A |
| 10 | Compliance % |
| 11 | Certification |
| 12 | Yes (Current) |
| 13 | Expired/Pending |
| 14 | No/Unknown |
| 15 | Risk |
| 16 | Count |
| 17 | Severity |

### Data Validation Values

All dropdown/list values used across sheets:

```
SaaS, IaaS, PaaS, Security Service, Cloud Storage, Other, Critical, High
Medium, Low, Public, Internal, Confidential, Restricted, Mixed, MSA + DPA
Subscription Agreement, Pay-As-You-Go, Trial, Custom, Yes, No, Yes (Current)
Yes (Expired), Unknown, Yes (< 6 months), Yes (6-12 months), Yes (High)
Yes (Moderate), Yes (Low), N/A, Yes (Adequate), Yes (Weak), Under Negotiation
Yes (List Provided), Yes (Generic), Yes (Favorable), Yes (Limited), ≤30 days
31-60 days, 61-90 days, >90 days, Yes (30 days), Yes (60 days), Yes (90 days)
Yes (Opt-Out), Yes (Opt-In), Yes (Full), Yes (Partial), N/A (Not in scope)
' + ', '.join(PROVIDER_HQ_JURISDICTION) + ', '.join(CLOUD_ACT_EXPOSURE) + '
'.join(YES_NO_PARTIAL_UNKNOWN) + ', '.join(YES_NO_PLANNED) + '
'.join(TRANSFER_MECHANISM) + ', '.join(RISK_LEVEL) + ', Switzerland, EU/EEA
USA, Asia-Pacific, Global, Yes (Contractual), Yes (Technical), Yes (EU SCC)
Yes (Swiss SCC), Yes (Other), Adequacy Decision, SCC, BCR, Derogations, None
Yes (Certified), Yes (Self-Assessed), Yes (Unrestricted), Yes (With Notice)
No Notice, ≤7 days, 8-30 days, >30 days, <1 hour, 1-4 hours, 4-24 hours
>24 hours, Yes (72 hours), Yes (Custom), Upon Request, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 10 sheets, 17 columns, 95 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"The worthwhile problems are the ones you can really solve or help solve, the ones you can really contribute something to."*
--- Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
