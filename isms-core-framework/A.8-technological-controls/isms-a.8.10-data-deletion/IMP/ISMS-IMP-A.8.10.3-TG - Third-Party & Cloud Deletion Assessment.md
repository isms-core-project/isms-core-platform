<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.10.3-TG:framework:TG:a.8.10.3 -->
**ISMS-IMP-A.8.10.3-TG - Third-Party & Cloud Deletion Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Third-Party & Cloud Deletion Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.10.3-TG |
| **Related Policy** | ISMS-POL-A.8.10 (Data Deletion) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.10 (Information Deletion) |
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

- ISMS-POL-A.8.10 (Data Deletion)
- ISMS-IMP-A.8.10.1 (Retention Deletion Triggers)
- ISMS-IMP-A.8.10.2 (Deletion Methods Assessment)
- ISMS-IMP-A.8.10.4 (Verification & Evidence Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a810_3_third_party_cloud.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.10.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 2. Cloud Provider Deletion |
| 3 | 3. SaaS Application Deletion |
| 4 | 4. Vendor Contract Assessment |
| 5 | 5. Subprocessor Mapping |
| 6 | 6. Shadow IT Assessment |
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
| 1 | Provider / Vendor Name |
| 2 | Service Type |
| 3 | Business Owner |
| 4 | Data Categories Processed |
| 5 | Provider Tier |
| 6 | Status |
| 7 | Contract Start Date |
| 8 | Last Contract Review |
| 9 | Next Contract Review |
| 10 | Gap Identified |
| 11 | Remediation Plan |
| 12 | Target Completion |
| 13 | Risk Level |
| 14 | Evidence Reference |
| 15 | Notes / Comments |
| 16 | Remediation Owner |
| 17 | Budget Required |
| 18 | Deletion Method |
| 19 | Deletion SLA (Days) |
| 20 | Certificate Provided |
| 21 | Multi-Region Verified |
| 22 | Admin Portal Access |
| 23 | Data Export Available |
| 24 | Deletion Request Method |
| 25 | GDPR DPA Signed |
| 26 | Deletion Clause Present |
| 27 | Deletion Timeline Specified |
| 28 | Certificate of Deletion |
| 29 | Audit Rights |
| 30 | Subprocessor Count |
| 31 | Subprocessor List Current |
| 32 | Deletion Flow Documented |
| 33 | Subprocessor Deletion SLA |
| 34 | Deletion Requests (Last 12M) |
| 35 | Average Response Time (Days) |
| 36 | Certificates Received |
| 37 | Incidents / Failures |
| 38 | EXCEPTIONS / DEVIATIONS |
| 39 | EVIDENCE REGISTER |
| 40 | ASSESSMENT APPROVAL AND SIGN-OFF |
| 41 | ASSESSMENT SUMMARY |
| 42 | FINAL DECISION: |
| 43 | NEXT REVIEW DETAILS |
| 44 | Evidence ID |
| 45 | Category |
| 46 | Description |
| 47 | Source Document |
| 48 | Date Collected |
| 49 | Collected By |
| 50 | Notes |
| 51 | Assessment Area |
| 52 | Total Items |
| 53 | Compliant |
| 54 | Partial |
| 55 | Non-Compliant |
| 56 | N/A |
| 57 | Compliance % |
| 58 | Finding |
| 59 | Impact |
| 60 | Recommendation |
| 61 | Priority |

### Data Validation Values

All dropdown/list values used across sheets:

```
IaaS (Infrastructure as a Service), PaaS (Platform as a Service)
SaaS (Software as a Service), Data Processor (non-cloud), Subprocessor, Other
Tier 1, Tier 2, Tier 3, Tier 4, Tier 5, Tier 6, Tier 7, Tier 8, Tier 9
Tier 10, Critical, High, Medium, Low, Yes, No, Unknown, API Delete
Console Delete, Support Ticket, Account Closure, Yes - Automatic
Yes - On Request, N/A, Yes - Full, Yes - Limited, Yes - API, Yes - Manual
Self-Service, Email Request, Account Manager, Pending, Yes - Specific
Yes - Generic, Yes - Days Specified, Yes - Reasonable Time
Contractually Required, Available on Request, Not Mentioned
Yes - Deletion Audit, Yes - General Audit, Yes - Updated, Yes - Outdated
No - Unknown, Yes - Flowchart, Yes - Description, Covered by Prime
Separate Agreement, Data Processing Agreement (DPA), Vendor Contract
Deletion Clause Extract, Certificate of Deletion, Email Correspondence
Subprocessor List, Deletion Request Log, Performance Report, Audit Report
Meeting Minutes, Verified, Pending verification, Not verified, Requires update
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 61 columns, 76 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Trust your vendors to store your data. Verify that they delete it."*
— Third-party risk principle

<!-- QA_VERIFIED: 2026-03-01 -->
