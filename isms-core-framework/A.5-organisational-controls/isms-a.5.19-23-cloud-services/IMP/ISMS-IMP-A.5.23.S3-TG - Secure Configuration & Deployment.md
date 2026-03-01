<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.23.S3-TG:framework:TG:a.5.23 -->
**ISMS-IMP-A.5.23.S3-TG - Secure Configuration & Deployment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Secure Configuration & Deployment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.23.S3-TG |
| **Related Policy** | ISMS-POL-A.5.23 (Cloud Services) |
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

- ISMS-POL-A.5.23 (Cloud Services)
- ISMS-IMP-A.5.23.S1 (Cloud Service Inventory & Classification)
- ISMS-IMP-A.5.23.S2 (Vendor Due Diligence & Contracts)
- ISMS-IMP-A.5.23.S4 (Ongoing Governance & Risk Management)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a523_3_secure_config.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.23.S3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 2. Configuration Baseline |
| 3 | 3. Access Control Setup |
| 4 | 4. Network Security |
| 5 | 5. Encryption Configuration |
| 6 | 6. Deployment Checklist |
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
| 1 | Configuration Area |
| 2 | Total Items |
| 3 | {CHECK} Compliant |
| 4 | {WARNING} Partial |
| 5 | {XMARK} Non-Compliant |
| 6 | N/A |
| 7 | Compliance % |
| 8 | Metric |
| 9 | Count |
| 10 | Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
SaaS, IaaS, PaaS, Security Service, Cloud Storage, Other, Production, Staging
Development, Test, All, Critical, High, Medium, Low, Restricted, Confidential
Internal, Public, N/A, Yes, No, DevOpsSec, DevOps, Cloud Teams, IT Operations
Security, Switzerland, EU/EEA, United Kingdom, United States
Other Adequate Country, Non-Adequate Country, No Exposure
Potential Exposure (US HQ), Mitigated (EU Data Boundary)
Mitigated (Encryption + Key Control), Accepted Risk (Documented)
Under Assessment, SCCs, BCRs, Adequacy Decision, None, Partial, Unknown
Planned, Full Compliance, Partial Compliance, Non-Compliant
N/A (Not in scope), Compliant, Partial (In Progress), No AI Systems
Low-Risk AI Only, High-Risk AI (Assessed), High-Risk AI (Assessment Pending)
Yes (All Users), Yes (Admins Only), Yes (Allowlist), Yes (Geo)
Yes (Private Link), Yes (VPN), Public Only, Yes (Advanced), Yes (Basic)
Yes (Provider Key), Yes (CMK), Yes (TLS 1.3), Yes (TLS 1.2), AES-256, AES-128
ChaCha20, Provider Managed, Customer Managed (HSM)
Customer Managed (Software), 90 days, 180 days, 365 days, Manual, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 10 sheets, 10 columns, 87 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Know how to solve every problem that has been solved."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
