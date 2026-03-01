<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.23.S4-TG:framework:TG:a.5.23 -->
**ISMS-IMP-A.5.23.S4-TG - Ongoing Governance & Risk Management**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Ongoing Governance & Risk Management |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.23.S4-TG |
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
- ISMS-IMP-A.5.23.S3 (Secure Configuration & Deployment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a523_4_governance.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.23.S4`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 2. Access Review |
| 3 | 3. Change Management |
| 4 | 4. Incident Management |
| 5 | 5. Business Continuity |
| 6 | 6. Vendor Risk Monitoring |
| 7 | 7. Exit Strategy Review |
| 8 | 8. Jurisdictional Risk |
| 9 | Evidence Register |
| 10 | Summary Dashboard |
| 11 | Approval Sign-Off |
| 12 | ),
        ( |
| 13 | ,  |
| 14 | access_review |
| 15 | change_mgmt |
| 16 | incident_mgmt |
| 17 | business_continuity |
| 18 | vendor_risk |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #0000FF | Custom |
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #666666 | Dark Gray (Secondary Text) |
| #808080 | Gray (Disabled) |
| #C00000 | Dark Red (Blocked) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FF0000 | Red (Critical/Alert) |
| #FFC000 | Custom |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFF00 | Yellow (Warning) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | Service Name |
| 2 | Provider |
| 3 | Criticality |
| 4 | Exit Strategy Type (Current) |
| 5 | Last Review Date |
| 6 | Next Review Date |
| 7 | Review Status |
| 8 | PoC Testing Required? |
| 9 | PoC Test Date (Last) |
| 10 | PoC Test Result |
| 11 | PoC Test Next Due |
| 12 | Exit Strategy Changed? |
| 13 | Reviewer Name |
| 14 | Notes |
| 15 | Assessment Area |
| 16 | Total Items |
| 17 | {CHECK} Compliant |
| 18 | {WARNING} Partial |
| 19 | {XMARK} Non-Compliant |
| 20 | N/A |
| 21 | Compliance % |
| 22 | Metric |
| 23 | Count |
| 24 | Status |
| 25 | Evidence ID |
| 26 | Evidence Type |
| 27 | Description |
| 28 | Location/Path |
| 29 | Date Collected |
| 30 | Collected By |
| 31 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, N/A, Critical, High, Medium, Low, Cloud-to-Cloud, Hybrid, On-Premises
Not Yet Determined, Current, Overdue, In Progress, Not Started, Yes (Critical)
No (Not Critical), Not Applicable, Pass, Fail, Not Tested, Unknown
Access review report, Change ticket, Incident report, BC/DR test report
Risk assessment, Audit log, Screenshot, Configuration export
Certification document, Contract/SLA, Meeting minutes, Email confirmation
Policy document, Quarterly ICT risk review (DORA)
Vendor concentration risk assessment, NIS2 incident notification record
AI system monitoring log, Jurisdictional risk assessment, Risk acceptance form
DPA with SCCs/BCRs, Other, Access Review, Change Management
Incident Management, Business Continuity, Vendor Risk Monitoring
Jurisdictional Risk, DORA Compliance, NIS2 Compliance, AI Act Compliance
Verified, Pending Review, Not Verified, Expired, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 18 sheets, 31 columns, 64 validation values, 15 colors

---

**END OF SPECIFICATION**


---

*"Nature uses only the longest threads to weave her patterns, so that each small piece of her fabric reveals the organisation of the entire tapestry."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
