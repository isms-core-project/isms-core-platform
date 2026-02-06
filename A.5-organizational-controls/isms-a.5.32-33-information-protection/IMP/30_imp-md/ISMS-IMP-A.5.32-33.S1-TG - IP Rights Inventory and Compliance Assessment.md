**ISMS-IMP-A.5.32-33.S1-TG - IP Rights Inventory and Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.32: Intellectual Property Rights

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.32-33.S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Intellectual Property Identification, Classification, Protection, and Compliance |
| **Related Policy** | ISMS-POL-A.5.32-33, Section 2.1 (IP Identification and Classification) |
| **Purpose** | Guide users through systematic IP discovery, classification, protection assessment, and third-party IP compliance verification |
| **Target Audience** | Legal Counsel, CISO, IP Owners, System Owners, IT Teams, Compliance Officers, Auditors, Workbook Developers |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Annual or After Significant IP Changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for IP Rights Inventory assessment workbook | ISMS Implementation Team |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.32-33.S1-UG.

---

# Technical Specification

**Audience:** Workbook Developers, Python/Excel Script Maintainers

---

# Workbook Structure

## Generated File

**Filename:** `ISMS-IMP-A.5.32-33.S1_IP_Rights_Inventory_[YYYYMMDD].xlsx`

**Generator Script:** `generate_a532_33_1_ip_rights_inventory.py`

## Sheet Overview

| Sheet # | Sheet Name | Purpose | Rows (Est.) |
|---------|------------|---------|-------------|
| 1 | Instructions | Usage guidance and legends | ~50 |
| 2 | IP_Asset_Inventory | Core IP asset register | 100+ |
| 3 | IP_Protection_Assessment | Protection controls per asset | 100+ |
| 4 | Third_Party_IP_Register | Licensed software and content | 200+ |
| 5 | Software_License_Compliance | License reconciliation | 200+ |
| 6 | Gap_Analysis | Identified gaps and remediation | 50+ |
| 7 | Evidence_Register | Audit evidence tracking | 100+ |
| 8 | Approval_SignOff | Formal approval record | ~30 |

---

# Sheet-by-Sheet Specifications

## Sheet 1: Instructions

### Layout
- Row 1: Merged header with document title
- Row 2: Merged subheader with control reference
- Rows 4+: Instruction text

### Content Sections
1. Purpose statement
2. IP classification framework
3. Protection requirements by category
4. Completion workflow
5. Key stakeholders
6. Generated date

### Styling
- Header: Dark blue (#1F4E79), white text, 14pt bold
- Subheader: Medium blue (#2E75B6), white text, 11pt bold
- Section headers: Bold, 11pt
- Body text: Calibri 10pt

## Sheet 2: IP_Asset_Inventory

### Column Structure

| Column | Header | Width | Data Validation | Style |
|--------|--------|-------|-----------------|-------|
| A | IP Asset ID | 12 | - | Text |
| B | IP Asset Name | 35 | - | Text |
| C | IP Category | 18 | List: Trade Secret, Patent, Copyright, Trademark | Dropdown |
| D | Description | 50 | - | Wrap text |
| E | IP Owner | 25 | - | Text |
| F | Custodian | 25 | - | Text |
| G | Legal Protection Status | 18 | List: Registered, Pending, Unregistered, N/A | Dropdown |
| H | Business Value | 12 | List: High, Medium, Low | Dropdown |
| I | Classification | 15 | List: Restricted, Confidential, Internal, Public | Dropdown |
| J | Creation Date | 12 | Date format | Date |
| K | Last Review | 12 | Date format | Date |
| L | Notes | 40 | - | Wrap text |

### Data Validation Rules
```
IP Category: "Trade Secret,Patent,Copyright,Trademark"
Legal Protection Status: "Registered,Pending,Unregistered,N/A"
Business Value: "High,Medium,Low"
Classification: "Restricted,Confidential,Internal,Public"
```

### Conditional Formatting
- Business Value "High": Red fill (#FF6B6B)
- Business Value "Medium": Orange fill (#FFA94D)
- Business Value "Low": Green fill (#69DB7C)

## Sheet 3: IP_Protection_Assessment

### Column Structure

| Column | Header | Width | Data Validation | Style |
|--------|--------|-------|-----------------|-------|
| A | IP Asset ID | 12 | Reference to Sheet 2 | Text |
| B | IP Asset Name | 30 | - | Text |
| C | Access Control | 30 | - | Wrap text |
| D | Technical Controls | 30 | - | Wrap text |
| E | Administrative Controls | 30 | - | Wrap text |
| F | Physical Controls | 25 | - | Wrap text |
| G | Legal Protection | 25 | - | Wrap text |
| H | Control Effectiveness | 15 | List: Effective, Partial, Ineffective | Dropdown |
| I | Gap Description | 35 | - | Wrap text |
| J | Remediation Needed | 35 | - | Wrap text |
| K | Status | 12 | List: Complete, In Progress, Not Started | Dropdown |

### Conditional Formatting
- Control Effectiveness "Effective": Green fill (#C6EFCE)
- Control Effectiveness "Partial": Yellow fill (#FFEB9C)
- Control Effectiveness "Ineffective": Red fill (#FFC7CE)

## Sheet 4: Third_Party_IP_Register

### Column Structure

| Column | Header | Width | Data Validation | Style |
|--------|--------|-------|-----------------|-------|
| A | Third-Party IP ID | 15 | - | Text |
| B | Software/Content Name | 30 | - | Text |
| C | Vendor | 25 | - | Text |
| D | License Type | 18 | List: Perpetual, Subscription, Open Source, Freeware | Dropdown |
| E | License Quantity | 15 | Number | Number |
| F | Deployed Quantity | 15 | Number | Number |
| G | Compliance Status | 18 | List: Compliant, Over-deployed, Under-utilised | Dropdown |
| H | Contract Reference | 20 | - | Text |
| I | Renewal Date | 12 | Date format | Date |
| J | Open Source License | 15 | List: GPL, Apache, MIT, BSD, LGPL, Other, N/A | Dropdown |
| K | Notes | 35 | - | Wrap text |

### Conditional Formatting
- Compliance Status "Over-deployed": Red fill (#FFC7CE)
- Compliance Status "Under-utilised": Yellow fill (#FFEB9C)
- Compliance Status "Compliant": Green fill (#C6EFCE)

## Sheet 5: Software_License_Compliance

### Column Structure

| Column | Header | Width | Data Validation | Style |
|--------|--------|-------|-----------------|-------|
| A | Software Name | 30 | - | Text |
| B | Vendor | 20 | - | Text |
| C | License Model | 18 | List: Named User, Device, Enterprise, Per Core, Subscription | Dropdown |
| D | Entitled | 12 | Number | Number |
| E | Deployed | 12 | Number | Number |
| F | Variance | 12 | Formula: =E-D | Number |
| G | Compliance Risk | 15 | List: High, Medium, Low, None | Dropdown |
| H | Remediation Action | 35 | - | Wrap text |
| I | Due Date | 12 | Date format | Date |
| J | Status | 15 | List: Open, In Progress, Complete, N/A | Dropdown |

### Formulas
- Column F (Variance): `=E[row]-D[row]`

### Conditional Formatting
- Variance > 0: Red fill (over-deployed)
- Variance < 0: Yellow fill (under-utilised)
- Variance = 0: Green fill (compliant)

## Sheet 6: Gap_Analysis

### Column Structure

| Column | Header | Width | Data Validation | Style |
|--------|--------|-------|-----------------|-------|
| A | Gap ID | 10 | - | Text |
| B | Gap Category | 18 | List: Protection, Compliance, Documentation, Process | Dropdown |
| C | Description | 45 | - | Wrap text |
| D | Related IP | 15 | - | Text |
| E | Risk Rating | 12 | List: High, Medium, Low | Dropdown |
| F | Remediation Action | 40 | - | Wrap text |
| G | Owner | 20 | - | Text |
| H | Due Date | 12 | Date format | Date |
| I | Status | 15 | List: Open, In Progress, Complete, Accepted | Dropdown |
| J | Notes | 30 | - | Wrap text |

### Conditional Formatting
- Risk Rating "High": Red fill (#FF6B6B)
- Risk Rating "Medium": Orange fill (#FFA94D)
- Risk Rating "Low": Green fill (#69DB7C)

## Sheet 7: Evidence_Register

### Column Structure

| Column | Header | Width | Data Validation | Style |
|--------|--------|-------|-----------------|-------|
| A | Evidence ID | 12 | - | Text |
| B | Description | 40 | - | Wrap text |
| C | Evidence Type | 18 | List: Document, Screenshot, Report, Configuration, Other | Dropdown |
| D | Related Item | 15 | - | Text |
| E | Storage Location | 35 | - | Text |
| F | Collected Date | 12 | Date format | Date |
| G | Collected By | 20 | - | Text |
| H | Verification Status | 18 | List: Verified, Pending Review, Not Verified, Expired | Dropdown |

### Conditional Formatting
- Verification Status "Verified": Green fill (#C6EFCE)
- Verification Status "Pending Review": Yellow fill (#FFEB9C)
- Verification Status "Not Verified": Red fill (#FFC7CE)

## Sheet 8: Approval_SignOff

### Layout
- Rows 1-2: Headers
- Rows 4-7: Assessment metadata (period, status, summary)
- Row 10: Approval section header
- Row 12: Approval table headers
- Rows 13+: Approver rows

### Assessment Metadata Fields
| Field | Cell | Style |
|-------|------|-------|
| Assessment Period | B4 | Input cell |
| Overall Compliance | B5 | Input cell |
| IP Assets Documented | B6 | Input cell |
| Open Gaps | B7 | Input cell |

### Approval Table
| Column | Header | Width |
|--------|--------|-------|
| A | Role | 35 |
| B | Name | 25 |
| C | Signature | 20 |
| D | Date | 15 |
| E | Decision | 22 |
| F | Comments | 30 |

### Approver Roles
1. Legal Counsel
2. Chief Information Security Officer
3. Data Protection Officer (if applicable)
4. Compliance Officer
5. Business Unit Representative

---

# Cell Styling Reference

## Colour Palette

| Style Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| Header Fill | #1F4E79 | 31,78,121 | Sheet headers |
| Subheader Fill | #2E75B6 | 46,117,182 | Secondary headers |
| Column Header | #D6DCE4 | 214,220,228 | Table headers |
| Input Cell | #FFFFCC | 255,255,204 | User input cells |
| High Risk | #FF6B6B | 255,107,107 | High priority items |
| Medium Risk | #FFA94D | 255,169,77 | Medium priority |
| Low Risk | #69DB7C | 105,219,124 | Low priority |
| Compliant | #C6EFCE | 198,239,206 | Compliant status |
| Warning | #FFEB9C | 255,235,156 | Attention needed |
| Non-Compliant | #FFC7CE | 255,199,206 | Non-compliant |

## Font Standards

| Element | Font | Size | Bold | Colour |
|---------|------|------|------|--------|
| Main Header | Calibri | 14 | Yes | White |
| Subheader | Calibri | 11 | Yes | White |
| Column Header | Calibri | 10 | Yes | Black |
| Body Text | Calibri | 10 | No | Black |
| Section Title | Calibri | 11 | Yes | Black |

## Border Standards

| Element | Border Style |
|---------|-------------|
| Data cells | Thin all sides |
| Headers | Thin all sides |
| Merged cells | Thin all sides |

---

# Integration Points

## Related Workbooks

| Workbook | Integration Type | Data Exchange |
|----------|-----------------|---------------|
| ISMS-IMP-A.5.32-33.S2 | Forward reference | IP classification informs records protection |
| ISMS-IMP-A.5.32-33.S3 | Forward reference | IP assets inform retention requirements |
| ISMS-IMP-A.5.32-33.S4 | Dashboard aggregation | Metrics feed compliance dashboard |
| ISMS-IMP-A.5.12-13 | Classification alignment | Information classification scheme |
| ISMS-IMP-A.5.9 | Asset reference | Asset inventory baseline |

## External System Integrations

| System | Data Source | Format |
|--------|-------------|--------|
| SAM Tools | License entitlements | CSV/Excel export |
| Patent Databases | Registration status | Manual verification |
| Contract Management | License agreements | Document reference |
| Source Code Repos | Software inventory | API/Export |

---

**END OF SPECIFICATION**

---

*"The only thing worse than training employees and losing them is not training them and keeping them."*
-- Zig Ziglar

<!-- QA_VERIFIED: 2026-02-06 -->
