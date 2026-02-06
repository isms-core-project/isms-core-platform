**ISMS-IMP-A.8.12.1-TG - DLP Infrastructure Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention


---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.12.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | DLP Infrastructure and Technology Deployment |
| **Related Policy** | ISMS-POL-A.8.12 (Data Leakage Prevention Policy) |
| **Purpose** | Assess implementation of DLP technologies across network, endpoint, email, cloud, web, and database channels to verify coverage, capability maturity, and integration effectiveness |
| **Target Audience** | DLP Administrators, Security Engineers, IT Infrastructure Teams, SOC Analysts, CISO, Compliance Officers |
| **Assessment Type** | Technical & Operational Infrastructure Review |
| **Review Cycle** | Quarterly or After Major DLP Deployment Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for DLP Infrastructure assessment | ISMS Implementation Team |

---

# Technical Specification
**Audience:** Python Developers, Excel Workbook Developers, Quality Assurance, ISMS Implementation Team

---

# Workbook Structure Overview

## Sheet List

**Total Sheets:** 11

| # | Sheet Name | Rows (approx) | Purpose | User Input |
|---|------------|---------------|---------|------------|
| 1 | Instructions_Legend | 50 | User guidance, metadata, legend | Metadata only (yellow cells) |
| 2 | DLP_Technology_Inventory | 35 | Complete DLP inventory | Yes (data entry rows) |
| 3 | Network_DLP | 25 | Network appliance assessment | Yes (data entry rows) |
| 4 | Endpoint_DLP | 25 | Endpoint agent assessment | Yes (data entry rows) |
| 5 | Email_DLP | 20 | Email DLP assessment | Yes (data entry rows) |
| 6 | Cloud_CASB_DLP | 20 | Cloud/CASB DLP assessment | Yes (data entry rows) |
| 7 | Web_DLP | 20 | Web proxy DLP assessment | Yes (data entry rows) |
| 8 | Database_DAM | 20 | Database Activity Monitoring assessment | Yes (data entry rows) |
| 9 | Gap_Analysis | 45 | Gaps, remediation plans | Yes (gap details) |
| 10 | Evidence_Register | 105 | Evidence tracking | Yes (evidence entries) |
| 11 | Summary_Dashboard | 35 | KPIs, compliance metrics | No (automated formulas) |

**Total Assessment Items:** ~85 infrastructure checkpoints

---

# Detailed Sheet Specifications

## Sheet: Instructions_Legend

**Purpose:** Provide user guidance and assessment metadata

**Layout:** Read-only, informational content

**Sections:**

**A. Document Header (Rows 1-10)**

- Row 1-2: Workbook title and ID
  - Font: Calibri 18pt Bold
  - Cell A1: "ISMS-IMP-A.8.12.1: DLP Infrastructure Assessment"
  - Cell A2: "Assessment Workbook v2.0 - ISO/IEC 27001:2022 Control A.8.12"
- Row 3-10: Document metadata table
  - Columns: A (Field), B (Value)
  - Fields: Workbook ID, Assessment Area, Related Policy, Version, Date Created, Review Cycle

**B. Organization Metadata (Rows 12-20)**
**USER INPUT REQUIRED - Yellow Background**

| Row | Field | Column A | Column B (User Input) |
|-----|-------|----------|----------------------|
| 13 | Assessment Date | "Assessment Date:" | DD.MM.YYYY (data validation: date format) |
| 14 | Completed By | "Completed By:" | Text (name) |
| 15 | Organization Name | "Organization Name:" | Text |
| 16 | Review Cycle | "Review Cycle:" | Dropdown: Quarterly/Semi-Annual/Annual |

**C. How to Use This Workbook (Rows 22-38)**

- Numbered steps (1-10) matching Section 3 workflow from Part I
- Font: Calibri 11pt
- Key action items in bold

**D. Legend - Response Values (Rows 40-48)**

| Symbol | Meaning | Color | RGB |
|--------|---------|-------|-----|
| ✅ | Compliant | Green | 198, 239, 206 |
| ⚠️ | Partial | Yellow | 255, 235, 156 |
| ❌ | Non-Compliant | Red | 255, 199, 206 |
| 📋 | Planned | Blue | 180, 198, 231 |
| ⚪ | N/A | Gray | 217, 217, 217 |

**E. Color Coding Guide (Rows 50-55)**

- Yellow cells = User input required
- Green cells = Compliant status
- Red cells = Non-compliant status
- White cells = Assessment responses
- Gray cells = Informational/examples (to be deleted or overwritten)

**Cell Protection:**

- All cells protected (read-only)
- No user input on this sheet except metadata (rows 13-16)

**Print Settings:**

- Fit to 1 page wide
- Page orientation: Portrait

---

## Sheet: DLP_Technology_Inventory

**Purpose:** Complete inventory of all DLP solutions deployed

**Column Specifications:**

| Col | Header | Type | Width | Data Validation | Formula/Notes |
|-----|--------|------|-------|-----------------|---------------|
| A | Technology ID | Text | 15 | None | User input (e.g., DLP-001) |
| B | Technology Name | Text | 30 | None | User input (vendor + product) |
| C | Deployment Type | Dropdown | 18 | List: Network, Endpoint, Cloud, Email, Web, Database | Dropdown |
| D | Vendor | Text | 20 | None | User input |
| E | Version | Text | 15 | None | User input (specific version) |
| F | Deployment Architecture | Dropdown | 20 | List: Inline, Monitor, Hybrid, Cloud-based | Dropdown |
| G | Deployment Status | Dropdown | 18 | List: Production, Staging, Test, Decommissioned | Dropdown |
| H | License Type | Dropdown | 18 | List: Perpetual, Subscription, Open Source | Dropdown |
| I | License Expiry | Date | 15 | Date format (DD.MM.YYYY) | User input |
| J | Support Contract | Dropdown | 15 | List: Active, Expired, N/A | Dropdown |
| K | EOL Date | Date | 15 | Date format (DD.MM.YYYY) or Text "Not announced" | User input |
| L | Primary Use Case | Text | 35 | None | User input |
| M | Integration Status | Dropdown | 18 | List: Integrated, Standalone, Partial | Dropdown |
| N | SIEM Integration | Dropdown | 15 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| O | SOC Integration | Dropdown | 15 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| P | Status | Dropdown | 18 | List: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Dropdown, conditional formatting |
| Q | Evidence ID | Text | 18 | None | User input (e.g., A812-1-INF-001) |

**Header Row:** Row 5 (Rows 1-4 reserved for sheet title, instructions)

- Font: Calibri 11pt Bold
- Fill: Dark Blue (RGB: 68, 114, 196)
- Text: White
- Border: All borders, medium weight

**Data Rows:** Rows 6-35 (30 rows total)

- Rows 6-10: Pre-populated example rows (Gray fill RGB: 242, 242, 242)
  - Example 1: Forcepoint DLP (Network)
  - Example 2: Forcepoint Endpoint DLP (Endpoint)
  - Example 3: Microsoft Purview DLP (Cloud)
  - Example 4: Symantec DLP (Email)
  - Example 5: Netskope CASB (Cloud)
- Rows 11-35: Blank for user input (White fill)
- Row height: 20

**Conditional Formatting:**

**Status Column (P):**

- Rule 1: If "✅ Compliant" → Green fill (RGB: 198, 239, 206), Green text
- Rule 2: If "⚠️ Partial" → Yellow fill (RGB: 255, 235, 156), Dark orange text
- Rule 3: If "❌ Non-Compliant" → Red fill (RGB: 255, 199, 206), Dark red text
- Rule 4: If "N/A" → Gray fill (RGB: 217, 217, 217), Gray text

**License Expiry Column (I):**

- Rule 1: If date < TODAY() → Red fill (expired)
- Rule 2: If date < TODAY()+180 → Yellow fill (expiring <6 months)
- Rule 3: If date >= TODAY()+180 → Green fill (valid)

**EOL Date Column (K):**

- Rule 1: If date < TODAY() → Red fill (past EOL)
- Rule 2: If date < TODAY()+365 → Yellow fill (approaching EOL <12 months)
- Rule 3: If date >= TODAY()+365 → Green fill (current)

**Cell Protection:**

- Header row (5): Protected
- Example rows (6-10): Protected (users can view but not edit examples)
- Data rows (11-35): Columns A-O Unprotected (user input), Column P (Status) Unprotected, Column Q (Evidence) Unprotected
- Allow: Insert rows, Sort, Filter

**Print Settings:**

- Fit to 1 page wide (landscape orientation)
- Repeat header row on all pages
- Page breaks: After row 20, after row 35

**Formulas:**
None in this sheet (data entry only). Summary calculations in Summary_Dashboard sheet.

---

## Sheet: Network_DLP

**Purpose:** Assess network-based DLP appliances

**Column Specifications:**

| Col | Header | Type | Width | Data Validation | Notes |
|-----|--------|------|-------|-----------------|-------|
| A | Appliance Name | Text | 30 | None | User input |
| B | Deployment Mode | Dropdown | 20 | List: Inline, TAP, SPAN, Cloud Gateway | Dropdown |
| C | Network Segments Covered | Text | 30 | None | CSV list (e.g., "DMZ, Internal") |
| D | Protocols Inspected | Text | 30 | None | CSV list (e.g., "HTTP, HTTPS, SMTP") |
| E | SSL/TLS Inspection | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| F | Throughput Capacity | Text | 18 | None | User input (e.g., "10 Gbps") |
| G | Current Utilization % | Number | 15 | 0-100 | User input numeric |
| H | Content Inspection | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| I | Pattern Matching (Regex) | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| J | Fingerprinting | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| K | Machine Learning/AI | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| L | Blocking Capability | Dropdown | 18 | List: Yes, No, Partial, N/A | Dropdown |
| M | High Availability | Dropdown | 15 | List: Yes, No, N/A | Dropdown |
| N | Status | Dropdown | 18 | List: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Conditional formatting |
| O | Evidence ID | Text | 18 | None | User input |

**Header Row:** Row 5
**Data Rows:** Rows 6-25 (20 rows total)

- Rows 6-8: Pre-populated examples (Gray fill)
- Rows 9-25: Blank for user input

**Conditional Formatting:**

**Status Column (N):**

- Same as DLP_Technology_Inventory sheet Status column

**Utilization Column (G):**

- Rule 1: If >90 → Red fill (critical, over-capacity)
- Rule 2: If 70-90 → Yellow fill (warning, approaching capacity)
- Rule 3: If <70 → Green fill (acceptable)

**Cell Protection:** Same pattern as previous sheet

---

## Sheet: Endpoint_DLP

**Purpose:** Assess endpoint DLP agent deployment

**Column Specifications:**

| Col | Header | Type | Width | Data Validation | Formula/Notes |
|-----|--------|------|-------|-----------------|---------------|
| A | Endpoint Solution Name | Text | 35 | None | User input |
| B | Operating Systems Supported | Text | 35 | None | CSV list (e.g., "Windows 10/11, macOS 13+") |
| C | Total Endpoints | Number | 15 | Integer >0 | User input |
| D | Agents Deployed | Number | 15 | Integer ≥0 | User input |
| E | Deployment Coverage % | Calculated | 18 | Read-only | Formula: =(D/C)*100 |
| F | Offline Protection | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| G | Agent Update Mechanism | Dropdown | 20 | List: Automatic, Manual, Scheduled | Dropdown |
| H | Channels Monitored | Text | 40 | None | CSV list (e.g., "USB, Clipboard, Print") |
| I | USB Blocking | Dropdown | 18 | List: Block, Monitor, Allow with justification, N/A | Dropdown |
| J | Cloud App Detection | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| K | Application Control | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| L | Status | Dropdown | 18 | List: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Conditional formatting |
| M | Evidence ID | Text | 18 | None | User input |

**Header Row:** Row 5
**Data Rows:** Rows 6-25 (20 rows total)

**Formulas:**

**Column E (Deployment Coverage %):**
```excel
Row 6: =IF(C6>0, ROUND((D6/C6)*100, 1), 0)
Copy down to row 25
```

**Conditional Formatting:**

**Coverage Column (E):**

- Rule 1: If ≥95 → Green fill (excellent coverage)
- Rule 2: If 80-94 → Yellow fill (acceptable coverage)
- Rule 3: If <80 → Red fill (insufficient coverage)

**Status Column (L):**

- Same as previous sheets

**Cell Protection:**

- Column E (Coverage %): Protected (calculated field)
- Other data columns: Unprotected

---

## Sheet: Email_DLP

**Purpose:** Assess email DLP integration

**Column Specifications:**

| Col | Header | Type | Width | Data Validation | Notes |
|-----|--------|------|-------|-----------------|-------|
| A | Email System | Text | 30 | None | E.g., "Microsoft Exchange 2019", "M365", "Google Workspace" |
| B | DLP Integration Point | Dropdown | 25 | List: Gateway, Cloud Service, API-based, Hybrid | Dropdown |
| C | Content Inspection | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| D | Attachment Scanning | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| E | Supported File Types | Text | 35 | None | CSV list (e.g., "PDF, DOCX, XLSX, ZIP") |
| F | Maximum Attachment Size | Text | 18 | None | E.g., "25 MB", "50 MB" |
| G | Encryption Support (S/MIME, PGP) | Dropdown | 25 | List: Yes, No, Partial, N/A | Dropdown |
| H | External Email Monitoring | Dropdown | 20 | List: Yes, No, Partial, N/A | Dropdown |
| I | Test Email Blocking Verified | Dropdown | 22 | List: Yes, No, Not Tested | Dropdown |
| J | Status | Dropdown | 18 | List: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Conditional formatting |
| K | Evidence ID | Text | 18 | None | User input |

**Header Row:** Row 5
**Data Rows:** Rows 6-20 (15 rows total)

---

## Sheet: Cloud_CASB_DLP

**Purpose:** Assess cloud and CASB DLP capabilities

**Column Specifications:**

| Col | Header | Type | Width | Data Validation | Notes |
|-----|--------|------|-------|-----------------|-------|
| A | CASB/Cloud DLP Solution | Text | 35 | None | E.g., "Microsoft Purview", "Netskope", "Zscaler" |
| B | Connected SaaS Applications | Text | 40 | None | CSV list (e.g., "M365, Salesforce, Dropbox") |
| C | Deployment Model | Dropdown | 20 | List: API-based, Proxy-based, Inline, Hybrid | Dropdown |
| D | Data Classification Integration | Dropdown | 25 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| E | Policy Enforcement Mode | Dropdown | 22 | List: Monitor Only, Block, Prompt User, Quarantine | Dropdown |
| F | Cloud Storage Monitoring | Dropdown | 22 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| G | File Sharing Control | Dropdown | 20 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| H | API Security Monitoring | Dropdown | 22 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| I | Status | Dropdown | 18 | List: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Conditional formatting |
| J | Evidence ID | Text | 18 | None | User input |

**Header Row:** Row 5
**Data Rows:** Rows 6-20 (15 rows total)

---

## Sheet: Web_Database_DLP

**Purpose:** Assess web proxy and database DLP

**Sections:**

**Section A: Web Proxy DLP (Rows 5-15)**

| Col | Header | Type | Width | Data Validation |
|-----|--------|------|-------|-----------------|
| A | Web Proxy Solution | Text | 30 | None |
| B | DLP Integration | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A |
| C | SSL Inspection (Web Uploads) | Dropdown | 22 | List: Yes, No, Partial, Planned, N/A |
| D | Cloud Storage Blocking | Dropdown | 22 | List: Block, Monitor, Allow, N/A |
| E | Blocked Services | Text | 40 | CSV list (e.g., "Dropbox Personal, Google Drive Personal") |
| F | Status | Dropdown | 18 | ✅/⚠️/❌/N/A |
| G | Evidence ID | Text | 18 | User input |

**Section B: Database Activity Monitoring (Rows 17-27)**

| Col | Header | Type | Width | Data Validation |
|-----|--------|------|-------|-----------------|
| A | Database System | Text | 30 | E.g., "SQL Server 2019", "Oracle 19c", "PostgreSQL" |
| B | DAM Solution | Text | 30 | E.g., "Imperva DAM", "Oracle Audit Vault", "Native Audit" |
| C | Query Logging | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A |
| D | Bulk Export Detection | Dropdown | 20 | List: Yes, No, Partial, Planned, N/A |
| E | Alert Threshold | Text | 18 | E.g., ">10,000 rows", ">100 MB" |
| F | Status | Dropdown | 18 | ✅/⚠️/❌/N/A |
| G | Evidence ID | Text | 18 | User input |

---

## Sheet: Gap_Analysis

**Purpose:** Document gaps and remediation plans

**Column Specifications:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Gap ID | Text | 12 | Auto-generated: GAP-001, GAP-002, etc. |
| B | Domain | Dropdown | 20 | List: Technology Inventory, Network DLP, Endpoint DLP, Email DLP, Cloud/CASB DLP, Web/Database DLP |
| C | Gap Description | Text | 50 | User input (what's missing or inadequate) |
| D | Risk Level | Dropdown | 15 | List: Critical, High, Medium, Low |
| E | Impact if Not Remediated | Text | 40 | User input (business/security impact) |
| F | Remediation Action | Text | 50 | User input (what needs to be done) |
| G | Owner | Text | 25 | User input (person/team responsible) |
| H | Target Date | Date | 15 | DD.MM.YYYY |
| I | Status | Dropdown | 18 | List: Open, In Progress, Completed, Deferred |
| J | Evidence ID (Remediation) | Text | 22 | Evidence after remediation |

**Header Row:** Row 5
**Data Rows:** Rows 6-45 (40 rows for gaps)

**Conditional Formatting:**

**Risk Level Column (D):**

- If "Critical" → Red fill, white text
- If "High" → Orange fill, dark text
- If "Medium" → Yellow fill, dark text
- If "Low" → Light yellow fill, dark text

**Target Date Column (H):**

- If past due (< TODAY()) → Red fill
- If due soon (< TODAY()+30) → Yellow fill
- If future (>= TODAY()+30) → Green fill

**Status Column (I):**

- If "Open" → Red fill
- If "In Progress" → Yellow fill
- If "Completed" → Green fill
- If "Deferred" → Gray fill

**Cell Protection:**

- Column A (Gap ID): Protected (auto-generated)
- Other columns: Unprotected

---

## Sheet: Evidence_Register

**Purpose:** Track all evidence collected

**Column Specifications:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Evidence ID | Text | 15 | User input or auto-generated |
| B | Domain | Dropdown | 20 | List: Technology Inventory, Network DLP, Endpoint DLP, Email DLP, Cloud/CASB DLP, Web/Database DLP, Gap Remediation |
| C | Evidence Type | Dropdown | 25 | List: Screenshot, Configuration Export, Test Result, Architecture Diagram, Report, Documentation |
| D | Description | Text | 50 | User input (what evidence shows) |
| E | File Name | Text | 40 | Actual file name in repository |
| F | File Location | Text | 60 | Path or URL |
| G | Collection Date | Date | 15 | DD.MM.YYYY |
| H | Collected By | Text | 25 | Person who collected |
| I | Classification | Dropdown | 15 | List: Public, Internal, Confidential |

**Header Row:** Row 5
**Data Rows:** Rows 6-105 (100 rows for evidence)

**Formula for Evidence ID Auto-Generation:**
```excel
Row 6: =IF(B6<>"", "EV-"&TEXT(ROW()-5, "000"), "")
Copy down to row 105
```

**Cell Protection:**

- Column A (Evidence ID): Protected if formula present
- Other columns: Unprotected

---

## Sheet: Summary_Dashboard

**Purpose:** Executive summary and compliance KPIs

**Layout:** Not tabular, dashboard style with KPI boxes

**Key Metrics (Calculated):**

**A. Overall Compliance Rate (Cell B5):**
```excel
=ROUND(
  (COUNTIF(DLP_Technology_Inventory!P:P,"✅ Compliant") + 
   COUNTIF(Network_DLP!N:N,"✅ Compliant") + 
   COUNTIF(Endpoint_DLP!L:L,"✅ Compliant") + 
   COUNTIF(Email_DLP!J:J,"✅ Compliant") + 
   COUNTIF(Cloud_CASB_DLP!I:I,"✅ Compliant") + 
   COUNTIF(Web_Database_DLP!F:F,"✅ Compliant")) /
  (COUNTA(DLP_Technology_Inventory!P:P) - 1 + 
   COUNTA(Network_DLP!N:N) - 1 + 
   COUNTA(Endpoint_DLP!L:L) - 1 + 
   COUNTA(Email_DLP!J:J) - 1 + 
   COUNTA(Cloud_CASB_DLP!I:I) - 1 + 
   COUNTA(Web_Database_DLP!F:F) - 1) * 100,
1)
```

**B. Total DLP Technologies (Cell B7):**
```excel
=COUNTIF(DLP_Technology_Inventory!G:G, "Production")
```

**C. Critical Gaps Count (Cell B9):**
```excel
=COUNTIF(Gap_Analysis!D:D, "Critical")
```

**D. High Priority Gaps (Cell B10):**
```excel
=COUNTIF(Gap_Analysis!D:D, "High")
```

**E. Endpoint Coverage % (Cell B12):**
```excel
=AVERAGE(Endpoint_DLP!E:E)
```
(Average of all endpoint coverage percentages)

**F. SIEM Integration Rate (Cell B14):**
```excel
=ROUND(
  COUNTIF(DLP_Technology_Inventory!N:N, "Yes") /
  (COUNTIF(DLP_Technology_Inventory!G:G, "Production")) * 100,
1)
```

**Conditional Formatting for KPIs:**

**Overall Compliance Rate (B5):**

- If ≥90% → Green fill, dark green text
- If 70-89% → Yellow fill, dark orange text
- If <70% → Red fill, dark red text

**Critical Gaps Count (B9):**

- If =0 → Green fill
- If 1-3 → Yellow fill
- If >3 → Red fill

**Dashboard Layout:**

```
Row 2-3: Title "DLP Infrastructure Assessment - Summary Dashboard"
Row 5: Overall Compliance Rate: [XX%] [Conditional color]
Row 7: Total DLP Technologies: [XX]
Row 9: Critical Gaps: [XX] [Conditional color]
Row 10: High Priority Gaps: [XX]
Row 12: Average Endpoint Coverage: [XX%]
Row 14: SIEM Integration Rate: [XX%]
Row 16-20: Top 5 Critical Gaps (pulled from Gap_Analysis sheet)
Row 22-27: Recommended Immediate Actions
```

**Cell Protection:**

- All cells protected (dashboard is read-only, calculated)

---

## Sheet: Approval_Sign-Off

**Purpose:** Document approval workflow

**Layout:** Form-style, not tabular

**Sections:**

**Assessment Metadata (Rows 5-12):**

- Assessment Period: From [Date] to [Date]
- Assessment Date: [DD.MM.YYYY]
- Assessment Type: [Dropdown: Initial/Quarterly/Ad-Hoc/Post-Remediation]

**Completed By (Rows 14-20):**

- Name: [Text field]
- Role: [Text field]
- Email: [Text field]
- Date Completed: [Date field]
- Signature: [Text field or digital signature]
- Time Invested: [Number] hours

**Reviewed By (Rows 22-28):**

- Name, Date, Signature fields
- Review Outcome: [Dropdown: Approved/Approved with corrections/Requires revision]
- Comments: [Large text area]

**Approved By (CISO) (Rows 30-40):**

- Name, Date, Signature fields
- Approval Decision: [Dropdown: Approved/Approved with conditions/Rejected]
- Risk Acceptance: [Checkbox: Yes/No]
- Budget Approval: [Dropdown: Approved/Requires justification/Deferred]
- Budget Amount: CHF [Number]

**Next Review Date (Row 42):**

- Date: [DD.MM.YYYY]

**Cell Protection:**

- Field labels: Protected
- Input fields (dates, names, dropdowns): Unprotected

---

# Data Validation Rules Summary

## Dropdown Lists

**Status (All Assessment Sheets):**
```
List: ✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A
```

**Yes/No/Partial Response:**
```
List: Yes,No,Partial,Planned,N/A
```

**Deployment Type (Technology Inventory):**
```
List: Network,Endpoint,Cloud,Email,Web,Database
```

**Deployment Architecture:**
```
List: Inline,Monitor,Hybrid,Cloud-based
```

**Deployment Status:**
```
List: Production,Staging,Test,Decommissioned
```

**License Type:**
```
List: Perpetual,Subscription,Open Source
```

**Risk Level (Gap Analysis):**
```
List: Critical,High,Medium,Low
```

**Remediation Status:**
```
List: Open,In Progress,Completed,Deferred
```

## Date Validation

**Format:** DD.MM.YYYY (Swiss/European format)

**Validation Rule:**
```
Type: Date
Data: Between 01.01.2020 and 31.12.2030
Error Message: "Please enter a valid date in DD.MM.YYYY format"
```

## Number Validation

**Utilization Percentage:**
```
Type: Decimal
Data: Between 0 and 100
Error Message: "Enter a percentage between 0 and 100"
```

**Endpoint Counts:**
```
Type: Whole Number
Data: Greater than or equal to 0
Error Message: "Enter a valid endpoint count (0 or positive integer)"
```

---

# Conditional Formatting Rules

## Status Column Formatting

**Applied to:** All Status columns across assessment sheets

**Rule 1: Compliant**
```
Formula: =$P6="✅ Compliant"
Format: Fill RGB(198,239,206), Font Color Dark Green
```

**Rule 2: Partial**
```
Formula: =$P6="⚠️ Partial"
Format: Fill RGB(255,235,156), Font Color Dark Orange
```

**Rule 3: Non-Compliant**
```
Formula: =$P6="❌ Non-Compliant"
Format: Fill RGB(255,199,206), Font Color Dark Red
```

**Rule 4: N/A**
```
Formula: =$P6="N/A"
Format: Fill RGB(217,217,217), Font Color Gray
```

## Date-Based Formatting

**License Expiry:**
```
Rule 1: =I6<TODAY() → Red fill (expired)
Rule 2: =AND(I6>=TODAY(), I6<TODAY()+180) → Yellow fill (expiring soon)
Rule 3: =I6>=TODAY()+180 → Green fill (valid)
```

**EOL Date:**
```
Rule 1: =K6<TODAY() → Red fill (past EOL)
Rule 2: =AND(K6>=TODAY(), K6<TODAY()+365) → Yellow fill (approaching EOL)
Rule 3: =K6>=TODAY()+365 → Green fill (current)
```

**Gap Target Date:**
```
Rule 1: =H6<TODAY() → Red fill (overdue)
Rule 2: =AND(H6>=TODAY(), H6<TODAY()+30) → Yellow fill (due soon)
Rule 3: =H6>=TODAY()+30 → Green fill (on track)
```

## KPI Formatting (Summary Dashboard)

**Compliance Percentage:**
```
Rule 1: >=90 → Green fill
Rule 2: 70-89 → Yellow fill
Rule 3: <70 → Red fill
```

**Critical Gaps Count:**
```
Rule 1: =0 → Green fill
Rule 2: 1-3 → Yellow fill
Rule 3: >3 → Red fill
```

---

# Cell Protection Configuration

## Protected Cells (Locked)

**Across All Sheets:**

- Column headers (header row)
- Instructional text cells
- Example rows (gray fill)
- Formula cells (calculations in Summary Dashboard, Coverage % in Endpoint DLP)
- Auto-generated cells (Evidence ID if formula present, Gap ID)

## Unprotected Cells (Unlocked)

**User Input Areas:**

- Data entry rows in all assessment sheets
- Dropdown selection cells
- Text input fields
- Date input fields
- Evidence descriptions and file locations
- Gap analysis details
- Approval workflow fields

## Sheet Protection Settings

**For Each Sheet:**
```
Protection Enabled: Yes
Password: [To be set during workbook generation - recommend strong password]

Allow Users To:

- Select locked cells: Yes
- Select unlocked cells: Yes
- Format cells: Yes (for user notes)
- Insert rows: Yes (in assessment sheets for additional entries)
- Delete rows: No (prevent accidental deletion)
- Sort: Yes
- Use AutoFilter: Yes
- Use PivotTable reports: No

```

**Exceptions:**

- Instructions_Legend: Fully protected except metadata cells
- Summary_Dashboard: Fully protected (all calculated)
- Approval_Sign-Off: Only input fields unprotected

---

# Summary Dashboard Formulas (Detailed)

## Overall Compliance Rate

**Purpose:** Calculate percentage of compliant items across all assessment sheets

**Formula (Cell B5):**
```excel
=IFERROR(
  ROUND(
    (COUNTIF(DLP_Technology_Inventory!P6:P35,"✅ Compliant") + 
     COUNTIF(Network_DLP!N6:N25,"✅ Compliant") + 
     COUNTIF(Endpoint_DLP!L6:L25,"✅ Compliant") + 
     COUNTIF(Email_DLP!J6:J20,"✅ Compliant") + 
     COUNTIF(Cloud_CASB_DLP!I6:I20,"✅ Compliant") + 
     COUNTIF(Web_Database_DLP!F6:F15,"✅ Compliant") + 
     COUNTIF(Web_Database_DLP!F18:F27,"✅ Compliant")) /
    (COUNTA(DLP_Technology_Inventory!P6:P35) + 
     COUNTA(Network_DLP!N6:N25) + 
     COUNTA(Endpoint_DLP!L6:L25) + 
     COUNTA(Email_DLP!J6:J20) + 
     COUNTA(Cloud_CASB_DLP!I6:I20) + 
     COUNTA(Web_Database_DLP!F6:F15) + 
     COUNTA(Web_Database_DLP!F18:F27)) * 100,
  1),
0)
```

**Explanation:**

- Numerator: Count of ✅ Compliant across all Status columns
- Denominator: Count of all populated Status cells (excluding headers)
- ROUND to 1 decimal place
- IFERROR returns 0 if division by zero (empty workbook)

## Technology Count

**Formula (Cell B7):**
```excel
=COUNTIF(DLP_Technology_Inventory!G6:G35, "Production")
```

**Explanation:** Count only Production status (exclude Staging, Test, Decommissioned)

## Critical Gaps

**Formula (Cell B9):**
```excel
=COUNTIF(Gap_Analysis!D6:D45, "Critical")
```

## High Priority Gaps

**Formula (Cell B10):**
```excel
=COUNTIF(Gap_Analysis!D6:D45, "High")
```

## Average Endpoint Coverage

**Formula (Cell B12):**
```excel
=IFERROR(
  ROUND(
    AVERAGE(Endpoint_DLP!E6:E25),
  1),
"N/A")
```

**Explanation:** Average of Coverage % column (Column E in Endpoint_DLP)

## SIEM Integration Rate

**Formula (Cell B14):**
```excel
=IFERROR(
  ROUND(
    COUNTIF(DLP_Technology_Inventory!N6:N35, "Yes") /
    COUNTIF(DLP_Technology_Inventory!G6:G35, "Production") * 100,
  1),
0)
```

**Explanation:**

- Numerator: Count of "Yes" in SIEM Integration column for Production systems
- Denominator: Total Production systems
- Percentage calculation

---

# Python Script Integration Points

## Workbook Generation Script

**Script Name:** `generate_a812_1_dlp_infrastructure_assessment.py`

**Key Functions:**

```python
def create_workbook():
    """Initialize workbook and create all 11 sheets"""
    wb = openpyxl.Workbook()
    # Remove default sheet
    wb.remove(wb.active)
    # Create sheets in order
    sheets = [
        "Instructions_Legend",
        "DLP_Technology_Inventory",
        "Network_DLP",
        "Endpoint_DLP",
        "Email_DLP",
        "Cloud_CASB_DLP",
        "Web_Database_DLP",
        "Gap_Analysis",
        "Evidence_Register",
        "Summary_Dashboard",
        "Approval_Sign-Off"
    ]
    for sheet_name in sheets:
        wb.create_sheet(sheet_name)
    return wb

def setup_styles():
    """Define cell styles, fonts, fills"""
    # Header style
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    # Compliant style
    compliant_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    # Partial style
    partial_fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
    # Non-compliant style
    noncompliant_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
    # Return style dictionary
    return {
        'header': {'fill': header_fill, 'font': header_font},
        'compliant': {'fill': compliant_fill},
        'partial': {'fill': partial_fill},
        'noncompliant': {'fill': noncompliant_fill}
    }

def get_column_definitions(sheet_key):
    """Return column widths and headers for each sheet type"""
    # CUSTOMIZE: Adjust column definitions per sheet
    definitions = {
        'DLP_Technology_Inventory': {
            'widths': [15, 30, 18, 20, 15, 20, 18, 18, 15, 15, 15, 35, 18, 15, 15, 18, 18],
            'headers': ['Technology ID', 'Technology Name', 'Deployment Type', ...]
        },
        'Network_DLP': {
            'widths': [30, 20, 30, 30, 18, 18, 15, 18, 18, 18, 18, 18, 15, 18, 18],
            'headers': ['Appliance Name', 'Deployment Mode', ...]
        },
        # ... other sheets
    }
    return definitions.get(sheet_key, {})

def create_assessment_sheet(wb, sheet_name, config):
    """Generic function to create assessment sheet with validation"""
    ws = wb[sheet_name]
    # Set column widths
    for idx, width in enumerate(config['widths'], start=1):
        ws.column_dimensions[get_column_letter(idx)].width = width
    # Create headers (row 5)
    for idx, header in enumerate(config['headers'], start=1):
        cell = ws.cell(row=5, column=idx, value=header)
        cell.fill = config['styles']['header']['fill']
        cell.font = config['styles']['header']['font']
    # Add data validation dropdowns
    for validation_def in config['validations']:
        # Apply validation to range
        dv = DataValidation(type="list", formula1=validation_def['formula'], allow_blank=False)
        ws.add_data_validation(dv)
        dv.add(validation_def['range'])
    # Apply conditional formatting
    for cf_rule in config['conditional_formatting']:
        ws.conditional_formatting.add(cf_rule['range'], cf_rule['rule'])
    # Protect sheet
    ws.protection.sheet = True
    ws.protection.password = config.get('password', '')
    ws.protection.formatCells = True
    ws.protection.insertRows = True
    ws.protection.sort = True
    ws.protection.autoFilter = True

def create_summary_dashboard(wb):
    """Create Summary Dashboard with formulas"""
    ws = wb['Summary_Dashboard']
    # Overall Compliance Rate (B5)
    ws['B5'] = '=IFERROR(ROUND((COUNTIF(DLP_Technology_Inventory!P6:P35,"✅ Compliant")+...'
    # Other KPI formulas
    ws['B7'] = '=COUNTIF(DLP_Technology_Inventory!G6:G35, "Production")'
    ws['B9'] = '=COUNTIF(Gap_Analysis!D6:D45, "Critical")'
    # Apply conditional formatting to KPIs
    # ... (per specification above)

def create_evidence_register(wb):
    """Create Evidence Register with auto-numbering"""
    ws = wb['Evidence_Register']
    # Formula for Evidence ID (Column A)
    for row in range(6, 106):
        ws.cell(row=row, column=1, value=f'=IF(B{row}<>"", "EV-"&TEXT(ROW()-5, "000"), "")')

def save_workbook(wb, filename):
    """Save with proper filename format"""
    # CUSTOMIZE: Organization-specific output path
    today = datetime.now().strftime("%Y%m%d")
    output_filename = f"ISMS-IMP-A.8.12.1_DLP_Infrastructure_Assessment_{today}.xlsx"
    wb.save(output_filename)
    print(f"✅ Workbook created: {output_filename}")
```

## Quality Assurance Script

**Script Name:** `excel_sanity_check_a812_1.py`

**Purpose:** Validate generated workbook matches specification

```python
def validate_workbook_structure(filename):
    """Check sheet names, column counts, headers"""
    wb = openpyxl.load_workbook(filename)
    expected_sheets = ["Instructions_Legend", "DLP_Technology_Inventory", ...]
    assert wb.sheetnames == expected_sheets, "Sheet structure mismatch"

def validate_data_validation(filename):
    """Verify dropdown validations applied correctly"""
    wb = openpyxl.load_workbook(filename)
    ws = wb['DLP_Technology_Inventory']
    # Check column P has Status dropdown
    validations = ws.data_validations.dataValidation
    assert any("✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A" in str(dv.formula1) for dv in validations)

def validate_conditional_formatting(filename):
    """Verify conditional formatting rules present"""
    wb = openpyxl.load_workbook(filename)
    ws = wb['DLP_Technology_Inventory']
    # Check Status column has 4 rules (Compliant, Partial, Non-Compliant, N/A)
    cf_rules = ws.conditional_formatting
    assert len(cf_rules) >= 4, "Missing conditional formatting rules"

def validate_formulas(filename):
    """Test formula accuracy"""
    wb = openpyxl.load_workbook(filename)
    ws = wb['Summary_Dashboard']
    # Check Overall Compliance Rate formula present
    assert ws['B5'].value.startswith('=IFERROR(ROUND'), "Compliance formula missing"

def run_all_checks(filename):
    """Execute full validation suite"""
    print("Running quality checks...")
    validate_workbook_structure(filename)
    validate_data_validation(filename)
    validate_conditional_formatting(filename)
    validate_formulas(filename)
    print("✅ All checks passed")
```

---

# Version Control and Change Management

## Workbook Versioning

**Filename Format:**
```
ISMS-IMP-A.8.12.1_DLP_Infrastructure_Assessment_YYYYMMDD.xlsx
```

**Example:**
```
ISMS-IMP-A.8.12.1_DLP_Infrastructure_Assessment_20260119.xlsx
```

**Version Tracking:**

- Version number embedded in Instructions_Legend sheet (Document Control section)
- Version history table documenting changes between versions
- Change log maintained in separate CHANGELOG.md

## Workbook Updates

**When to Increment Version:**

- **Major version (1.0 → 2.0):** Structural changes (new sheets, column reordering, formula changes)
- **Minor version (2.0 → 2.1):** Content updates (dropdown options added, examples updated)
- **Patch version (2.1.0 → 2.1.1):** Bug fixes (typo corrections, formula fixes)

## Backward Compatibility

**Maintaining Compatibility:**

- Column additions: Always add to the right (don't insert in middle)
- Dropdown updates: Only add options (don't remove existing options used in data)
- Formula changes: Test against sample data before deploying

**Migration Path:**

- v1.0 workbooks can be migrated to v2.0 using `normalize_assessment_files_a812.py` script
- Migration script maps old column structure to new structure
- Data loss warnings if v2.0 removes features from v1.0

---

# Appendix: Technical Notes for Developers

## Color Palette (RGB Values)

**Status Colors:**

- Compliant Green: RGB(198, 239, 206)
- Partial Yellow: RGB(255, 235, 156)
- Non-Compliant Red: RGB(255, 199, 206)
- N/A Gray: RGB(217, 217, 217)
- Planned Blue: RGB(180, 198, 231)

**UI Colors:**

- Header Dark Blue: RGB(68, 114, 196)
- Header Text White: RGB(255, 255, 255)
- Example Row Gray: RGB(242, 242, 242)
- User Input Yellow: RGB(255, 255, 204)

## Font Standards

**Workbook-Wide:**

- Font Family: Calibri
- Header Font Size: 11pt Bold
- Data Font Size: 11pt Regular
- Title Font Size: 14-18pt Bold

## Excel Formula Best Practices

**IFERROR Usage:**

- Wrap division operations to handle #DIV/0 errors
- Return meaningful defaults (0 for percentages, "N/A" for text)

**Named Ranges:**

- Consider using named ranges for frequently referenced cells
- Example: Name cell Instructions_Legend!B13 as "AssessmentDate"

**Absolute vs Relative References:**

- Use absolute references ($A$1) for constant cells (headers, lookup tables)
- Use relative references (A1) for cells that change when copied

## Performance Optimization

**For Large Datasets:**

- Avoid volatile functions (NOW(), TODAY(), OFFSET()) in frequently recalculated cells
- Use structured references for table data
- Minimize conditional formatting ranges (apply only to data rows, not entire columns)
- Disable automatic calculation if workbook becomes slow (File > Options > Formulas > Manual calculation)

## Known Limitations and Workarounds

**Limitation 1: Excel Date Formats (DD.MM.YYYY vs MM/DD/YYYY)**

- Issue: Excel interprets dates based on system locale
- Workaround: Use TEXT() function to force DD.MM.YYYY display format
- Example: `=TEXT(I6, "DD.MM.YYYY")`

**Limitation 2: Emoji in Dropdowns (✅, ⚠️, ❌)**

- Issue: Some Excel versions don't display emoji in dropdowns
- Workaround: Provide text alternative: "Compliant [✅]", "Partial [⚠️]", etc.
- Test on target Excel versions before deployment

**Limitation 3: Sheet Protection Prevents Some Macros**

- Issue: Protected sheets block VBA automation
- Workaround: Unprotect sheet programmatically in macro, perform operation, re-protect
- Example: `ws.Unprotect Password:="password"` then `ws.Protect Password:="password"`

---

# Testing and Validation Checklist

**Pre-Deployment Testing:**

- [ ] Workbook opens in Excel 2016, 2019, Microsoft 365 without errors
- [ ] All 11 sheets present and correctly named
- [ ] Data validation dropdowns functional in all assessment sheets
- [ ] Conditional formatting displays correctly (colors match specification)
- [ ] Formulas calculate correctly (test with sample data)
- [ ] Summary Dashboard KPIs update when data entered in assessment sheets
- [ ] Evidence Register auto-numbering works
- [ ] Cell protection configured (locked cells cannot be edited, unlocked cells can)
- [ ] Sheet protection password set and documented
- [ ] Print settings configured (landscape for wide sheets, portrait for forms)
- [ ] No broken cell references (#REF!, #NAME? errors)
- [ ] File size reasonable (<5 MB for empty workbook)

**User Acceptance Testing:**

- [ ] Security team can complete assessment within estimated time (4-6 hours)
- [ ] Dropdown options are comprehensive (no "Other" needed excessively)
- [ ] Instructions clear (users don't require additional guidance)
- [ ] Evidence naming convention practical (users can follow consistently)
- [ ] Gap Analysis captures all necessary remediation details
- [ ] Approval workflow meets organizational approval process

**Quality Assurance:**

- [ ] No spelling errors in headers, instructions, dropdown options
- [ ] Dates in DD.MM.YYYY format throughout
- [ ] Colors consistent with organizational style guide (if applicable)
- [ ] Accessibility: Color contrast sufficient for color-blind users
- [ ] Examples realistic and helpful (not Lorem Ipsum placeholders)

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Document Assembly Instructions

**To create the complete ISMS-IMP-A.8.12.1 specification:**

1. **Combine PART I and PART II:**

   - Part I (separate file): User Completion Guide
   - Part II (this file): Technical Specification

2. **Generate Excel Workbook:**

   - Run: `python3 generate_a812_1_dlp_infrastructure_assessment.py`
   - Output: `ISMS-IMP-A.8.12.1_DLP_Infrastructure_Assessment_YYYYMMDD.xlsx`

3. **Validate Workbook:**

   - Run: `python3 excel_sanity_check_a812_1.py ISMS-IMP-A.8.12.1_DLP_Infrastructure_Assessment_YYYYMMDD.xlsx`
   - Verify: All checks pass

4. **Deploy:**

   - Distribute workbook to assessment team
   - Provide Part I User Guide as reference
   - Collect completed assessments
   - Consolidate into ISMS-IMP-A.8.12.5 Compliance Dashboard

---

**Status:** Technical Specification Complete  
**Next Action:** Implement Python workbook generator per specification  
**Dependencies:** openpyxl library (install: `pip install openpyxl`)

---

**END OF SPECIFICATION**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
