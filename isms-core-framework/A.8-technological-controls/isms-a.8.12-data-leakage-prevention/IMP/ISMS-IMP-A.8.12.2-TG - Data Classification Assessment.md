<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.12.2-TG:framework:TG:a.8.12.2 -->
**ISMS-IMP-A.8.12.2-TG - Data Classification Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Data Classification Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.12.2-TG |
| **Related Policy** | ISMS-POL-A.8.12 (Data Leakage Prevention) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.12 (Data Leakage Prevention) |
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

- ISMS-POL-A.8.12 (Data Leakage Prevention)
- ISMS-IMP-A.8.12.1 (DLP Infrastructure Assessment)
- ISMS-IMP-A.8.12.3 (Channel Coverage Assessment)
- ISMS-IMP-A.8.12.4 (Monitoring & Response Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a812_2_data_classification.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.12.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Classification Schema |
| 3 | Sensitive Data Inventory |
| 4 | Data Location Mapping |
| 5 | Data Owner Assignment |
| 6 | Regulatory Mapping |
| 7 | Labelling Methods |
| 8 | Discovery Results |
| 9 | Gap Analysis |
| 10 | Evidence Register |
| 11 | Summary Dashboard |
| 12 | Approval Sign-Off |

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
| 1 | Classification Level |
| 2 | Definition |
| 3 | Examples |
| 4 | Handling Requirements |
| 5 | Access Controls |
| 6 | Encryption Required |
| 7 | DLP Monitoring |
| 8 | Retention Period |
| 9 | Disposal Method |
| 10 | Evidence ID |
| 11 | Data Category |
| 12 | Data Type |
| 13 | Regulatory Requirement |
| 14 | Data Examples |
| 15 | Business Owner |
| 16 | Data Steward |
| 17 | Estimated Volume |
| 18 | Discovery Status |
| 19 | DLP Protection |
| 20 | Storage Location Type |
| 21 | Specific Location |
| 22 | Path/Schema |
| 23 | Estimated Records/Files |
| 24 | Last Discovery Scan |
| 25 | DLP Coverage |
| 26 | Encryption at Rest |
| 27 | Data Owner Notified |
| 28 | Business Owner Name |
| 29 | Business Owner Department |
| 30 | Business Owner Email |
| 31 | Data Steward Name |
| 32 | Data Steward Department |
| 33 | Data Steward Email |
| 34 | Ownership Documented |
| 35 | Owner Training Complete |
| 36 | Last Review Date |
| 37 | Regulation |
| 38 | Specific Article/Section |
| 39 | Requirement Summary |
| 40 | Compliance Status |
| 41 | DLP Controls Required |
| 42 | Breach Notification Required |
| 43 | Data Subject Rights |
| 44 | System/Application |
| 45 | Labeling Method |
| 46 | Classification Tool |
| 47 | Supported Labels |
| 48 | User Training Provided |
| 49 | Enforcement Capability |
| 50 | DLP Integration |
| 51 | Adoption Rate % |
| 52 | Discovery Tool |
| 53 | Scan Target |
| 54 | Scan Date |
| 55 | Data Categories Found |
| 56 | Total Findings |
| 57 | Critical Findings |
| 58 | False Positive Rate % |
| 59 | Remediation Status |
| 60 | Gap ID |
| 61 | Gap Description |
| 62 | Affected Data Category |
| 63 | Risk Level |
| 64 | Business Impact |
| 65 | Root Cause |
| 66 | Remediation Plan |
| 67 | Owner |
| 68 | Target Date |
| 69 | Status |
| 70 | Assessment Area |
| 71 | Evidence Type |
| 72 | Description |
| 73 | Location/Path |
| 74 | Date Collected |
| 75 | Collected By |
| 76 | Verification Status |
| 77 | Total Items |
| 78 | Compliant |
| 79 | Partial |
| 80 | Non-Compliant |
| 81 | N/A |
| 82 | Compliance % |
| 83 | Metric |
| 84 | Value |
| 85 | Target |
| 86 | Finding |
| 87 | Impact |
| 88 | Recommendation |
| 89 | Priority |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Partial, Planned, N/A, Pending, Public, Internal, Confidential
Restricted, PII, Financial, IP, Credentials, Business Confidential, Other
FADP, GDPR, PCI-DSS, FADP/GDPR, Multiple, None, Discovered, In Progress
Not Started, File Server, Database, Endpoint, Cloud, Email, Backup, Manual
Automated, Metadata, Compliant, Non-Compliant, Complete, Critical, High
Medium, Low, Open, Resolved, Accepted, Closed, Screenshot, Configuration File
Policy Document, Log Export, Report, Certificate, Meeting Minutes, Verified
Rejected, Approved, HIPAA, SOX, Draft, In Review, Approved with Conditions
Deferred
```

**Extracted:** 12 sheets, 89 columns, 61 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The important thing is not to stop questioning. Curiosity has its own reason for existing."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
