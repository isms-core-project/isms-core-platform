**ISMS-IMP-A.5.34.6-TG - Cross-Border Data Transfer Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.34.6-TG |
| **Version** | 1.0 |
| **Assessment Area** | Cross-Border Data Transfer Assessment and GDPR Chapter V Compliance |
| **Related Policy** | ISMS-POL-A.5.34, Section 2.6 (Cross-Border Transfers) |
| **Purpose** | Guide users through transfer inventory, Transfer Impact Assessments (TIAs), and compliance with GDPR Chapter V (Articles 44-50) and post-Schrems II requirements |
| **Target Audience** | DPO/Privacy Officers, Legal Counsel, Procurement Teams, IT/Cloud Teams, Third-Party Risk Management, Compliance Officers, Auditors |
| **Assessment Type** | Legal & Technical Compliance |
| **Review Cycle** | Quarterly or upon new international transfers |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Cross-Border Transfer assessment workbook | ISMS Implementation Team |
---

## Purpose and Scope

### Purpose

This implementation guide provides comprehensive procedures for assessing, documenting, and managing international transfers of personal data per GDPR Chapter V (Articles 44-50), Swiss Federal Act on Data Protection (FADP) Article 16, and ISO/IEC 27001:2022 Control A.5.34 requirements.

### Assessment Objectives

1. **Transfer Inventory**: Identify and catalog ALL cross-border personal data transfers
2. **Legal Basis Validation**: Verify appropriate transfer mechanisms (Adequacy, SCCs, BCRs, DPF, Derogations)
3. **Transfer Impact Assessment (TIA)**: Evaluate risks to data subjects for non-adequate country transfers
4. **Processor Compliance**: Ensure Data Processing Agreements (DPAs) include transfer safeguards
5. **Gap Remediation**: Address unlawful or under-documented international transfers
6. **Regulatory Reporting**: Maintain audit-ready documentation for supervisory authorities

### Scope

**In Scope:**

- All personal data transfers crossing EU/EEA borders (GDPR jurisdiction)
- All personal data transfers from Switzerland (FADP jurisdiction)
- Transfers to processors, joint controllers, and independent third parties
- Automated transfers (APIs, integrations) and manual transfers (email, file sharing)
- Onward transfers (processor-to-subprocessor in third countries)
- Cloud services with multi-region data storage or processing
- Remote access to PII systems by personnel in third countries

**Out of Scope:**

- Purely domestic data transfers within EU/EEA or within Switzerland
- Transfers between EU/EEA member states (free movement of data per GDPR Article 45)
- Anonymized data (GDPR does not apply if truly anonymized per GDPR Recital 26)
- Data physically transported by data subjects themselves (e.g., employee traveling with laptop)

### Regulatory Context

**GDPR Chapter V Requirements:**

- **Article 44**: General principle - transfers only with adequate safeguards
- **Article 45**: Adequacy decisions (EU Commission approves countries with adequate protection)
- **Article 46**: Appropriate safeguards (SCCs, BCRs, codes of conduct, certifications)
- **Article 47**: Binding Corporate Rules (BCRs) for intra-group transfers
- **Article 49**: Derogations for specific situations (limited use, not routine transfers)
- **Article 50**: International cooperation for mutual administrative assistance

**Swiss FADP Requirements:**

- **Article 16**: Disclosure of personal data abroad (similar to GDPR but separate adequacy list)
- **Article 17**: Processor obligations (applies to processors outside Switzerland)
- Adequacy recognized by Swiss Federal Council (NOT identical to EU adequacy list)

**Post-Schrems II Landscape:**

- **Schrems II (2020)**: Invalidated EU-US Privacy Shield, requires case-by-case TIA for US transfers
- **Transfer Impact Assessment (TIA)**: Mandatory for transfers to countries without adequacy decision
- **Supplementary Measures**: Technical (encryption, pseudonymization) and contractual measures required
- **Continuous Monitoring**: Reassess TIAs if legal/political situation changes

---

# Technical Specification

---

## Sheet 1: Instructions & Legend

### Purpose
Pre-populated reference sheet with GDPR Chapter V guidance, transfer mechanism definitions, and adequacy decision lists.

### Structure

**Title Block (A1:P3):**

- Merge cells A1:P3
- Title: "Cross-Border Data Transfer Assessment - Instructions & Legend"
- Font: Arial 16pt Bold, White text
- Background: Dark Blue (#1F4E78)
- Alignment: Center, Middle

**Section 1: GDPR Chapter V Overview (A5:P25)**

| Row | Content | Formatting |
|-----|---------|------------|
| 5 | **"GDPR Chapter V: Transfers to Third Countries"** | Bold, 14pt, Dark Blue background |
| 6-10 | Article summaries (Art. 44-49) | Wrapped text, left-aligned |
| 12 | **"Transfer Mechanism Decision Tree"** | Bold, 14pt |
| 13-20 | Decision tree flowchart (text-based) | Indented, bullet points |

**Section 2: EU Adequacy Decisions List (A27:D45)**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Country | 25 | List of adequate countries |
| B | Adequacy Type | 20 | Full / Limited (e.g., Canada commercial) |
| C | Decision Date | 15 | When EU Commission granted adequacy |
| D | Status | 12 | Valid / Under Review |

**Named Range:** Create named range "EUAdequacyCountries" = Sheet1!$A$28:$A$45

**Adequacy List (as of 2025):**
```
Andorra
Argentina
Canada (Commercial Organizations)
Faroe Islands
Guernsey
Israel
Isle of Man
Japan
Jersey
New Zealand
Republic of Korea
Switzerland
United Kingdom
Uruguay
EU/EEA Member States (27 + 3 EEA)
```

**Section 3: Transfer Mechanism Definitions (A47:P70)**

| Row | Definition | Content |
|-----|------------|---------|
| 47 | **Adequacy Decision (Art. 45)** | "EU Commission recognizes country provides adequate protection. No additional safeguards needed." |
| 50 | **Standard Contractual Clauses (Art. 46)** | "Commission-approved contractual clauses. 2021 version with 4 modules (C2C, C2P, P2P, P2C)." |
| 53 | **Binding Corporate Rules (Art. 47)** | "Intra-group transfers for multinationals. Requires SA approval (2-3 year process)." |
| 56 | **EU-US Data Privacy Framework** | "US companies self-certify. Check https://www.dataprivacyframework.gov/s/participant-search" |
| 59 | **Derogations (Art. 49)** | "LAST RESORT for non-routine, occasional transfers. Cannot be systematic." |
| 62 | **Transfer Impact Assessment (TIA)** | "Required post-Schrems II for non-adequate countries. Assess surveillance laws, implement supplementary measures." |

**Section 4: Red Flags Checklist (A72:P85)**

Formatted as checklist table:

- ❌ Transfer without mechanism documented
- ❌ Using 2010 SCCs (invalid since Sept 2022)
- ❌ US transfer without TIA
- ❌ Derogation for routine transfers
- ❌ No DPA with processor
- ❌ Processor uses subprocessor without SCCs

**Worksheet Protection:**

- Entire sheet protected (read-only)
- No password required (reference material)

---

## Sheet 2: Cross-Border Transfer Register

### Purpose
Comprehensive inventory of all international personal data transfers.

### Column Definitions

| Col | Column Name | Data Type | Width | Validation | Formula/Notes |
|-----|------------|-----------|-------|------------|---------------|
| A | Transfer ID | Text | 12 | Auto-generated | `="XFER-" & TEXT(ROW()-1, "0000")` |
| B | Status | Dropdown | 12 | Required | {Not Started, In Progress, Complete, Validated} |
| C | Transfer Name | Text | 30 | Required | Descriptive name (e.g., "CRM to Email Marketing") |
| D | Source System | Text | 25 | Required | Where data originates (link to A.5.34.1 Sheet 1) |
| E | Destination System | Text | 25 | Required | Where data is sent |
| F | Destination Country | Dropdown | 20 | Required | Country list (ALL countries, not just adequate) |
| G | Adequacy Status | Formula | 18 | Calculated | `=IF(COUNTIF(EUAdequacyCountries,F2)>0,"Adequate","NOT Adequate")` |
| H | Transfer Mechanism | Dropdown | 30 | Conditional | See Section 3.2 below |
| I | SCC Version | Dropdown | 20 | Conditional | {2021 Module 1 (C2C), 2021 Module 2 (C2P), 2021 Module 3 (P2P), 2021 Module 4 (P2C), N/A} |
| J | SCC Signature Date | Date | 15 | Conditional | If mechanism = SCCs |
| K | DPF Certification? | Boolean | 15 | Conditional | Checkbox: If destination = US |
| L | DPF Cert Number | Text | 18 | Conditional | If DPF = TRUE |
| M | TIA Required? | Formula | 12 | Calculated | `=IF(G2="NOT Adequate","YES","NO")` |
| N | TIA ID | Text | 15 | Conditional | Link to Sheet 3 (e.g., "TIA-2025-001") |
| O | TIA Completion Date | Date | 15 | Conditional | When TIA approved |
| P | Data Flow Type | Dropdown | 25 | Required | {Controller-to-Processor, Controller-to-Controller, Processor-to-Processor, Controller-to-Data-Subject} |
| Q | PII Categories | Text | 35 | Required | What PII transferred (Name, Email, etc.) |
| R | Data Subject Types | Dropdown | 20 | Required | {Customers, Employees, Website Visitors, Suppliers, Other} |
| S | Transfer Volume | Text | 18 | Required | # of records (e.g., "5,000/month") |
| T | Transfer Frequency | Dropdown | 15 | Required | {Real-time, Hourly, Daily, Weekly, Monthly, On-Demand} |
| U | Transfer Method | Dropdown | 18 | Required | {API (HTTPS), SFTP, Email, Manual, Database Replication} |
| V | Purpose of Transfer | Text | 35 | Required | Business justification |
| W | Legal Basis (Art. 6) | Dropdown | 25 | Required | {Consent, Contract, Legal Obligation, Vital Interests, Public Task, Legitimate Interest} |
| X | Security Measures | Text | 40 | Required | TLS version, encryption, access controls |
| Y | Processor Name | Text | 25 | Conditional | If P="Controller-to-Processor" |
| Z | DPA Reference | Text | 20 | Conditional | Link to Sheet 4 or file path |
| AA | Last Updated | Date | 12 | Auto | `=TODAY()` when row edited |
| AB | Updated By | Text | 20 | Manual | Who last modified |
| AC | Notes | Text | 40 | Optional | Additional context |
| AD | Evidence Link | Text | 25 | Optional | Link to Sheet 5 evidence |
| AE | Review Comments | Text | 30 | Optional | Auditor/DPO feedback |

### Dropdowns and Validation

**B: Status Dropdown**
```
Values: "Not Started, In Progress, Complete, Validated"
Error Style: Stop
Error Message: "Select valid status"
```

**F: Destination Country Dropdown**
```
Source: All countries list (too long to hardcode, use separate reference sheet or allow free text)
Note: For production, maintain country list on hidden sheet
```

**H: Transfer Mechanism Dropdown** (Conditional on Adequacy Status)
```
If G (Adequacy Status) = "Adequate":
    Values: "Adequacy Decision, EU-US Data Privacy Framework"
    
If G (Adequacy Status) = "NOT Adequate":
    Values: "Standard Contractual Clauses (SCCs), Binding Corporate Rules (BCRs), Derogation - Explicit Consent, Derogation - Contract Necessity, Derogation - Legal Claims, Derogation - Vital Interests, Derogation - Legitimate Interest (Occasional)"
```

**Implementation Note:** Excel data validation doesn't support dynamic conditional dropdowns natively. Python script creates two separate validations and uses VBA or instructs user to select appropriate dropdown based on adequacy status.

**P: Data Flow Type Dropdown**
```
Values: "Controller-to-Processor, Controller-to-Controller, Processor-to-Processor, Controller-to-Data-Subject"
```

**R: Data Subject Types Dropdown**
```
Values: "Customers, Employees, Website Visitors, Suppliers, Job Applicants, Business Partners, Other"
Allow Blank: No
```

**T: Transfer Frequency Dropdown**
```
Values: "Real-time, Hourly, Daily, Weekly, Monthly, On-Demand, One-Time"
```

**U: Transfer Method Dropdown**
```
Values: "API (HTTPS), API (Other), SFTP, FTPS, Email, Manual Upload, Database Replication, Backup, Other"
```

**W: Legal Basis Dropdown**
```
Values: "Consent (GDPR Art. 6(1)(a)), Contract (Art. 6(1)(b)), Legal Obligation (Art. 6(1)(c)), Vital Interests (Art. 6(1)(d)), Public Task (Art. 6(1)(e)), Legitimate Interest (Art. 6(1)(f))"
```

### Conditional Formatting

**Rule 1: Missing Transfer Mechanism**
```
Applies to: H2:H1000
Condition: =$G2="NOT Adequate" AND $H2=""
Format: Red fill (#FFC7CE), Red text (#9C0006), Bold
Purpose: Highlight critical gap - non-adequate transfer without mechanism
```

**Rule 2: Missing TIA**
```
Applies to: N2:N1000
Condition: =$M2="YES" AND $N2=""
Format: Orange fill (#FFD966), Dark Orange text (#9C5700)
Purpose: Highlight missing TIA for non-adequate transfer
```

**Rule 3: Old SCCs**
```
Applies to: I2:I1000
Condition: =AND($I2<>"", NOT(ISNUMBER(SEARCH("2021",$I2))))
Format: Red fill, Red text, Bold
Purpose: Flag 2010 SCCs (invalid)
```

**Rule 4: Status Color-Coding**
```
Applies to: B2:B1000
Condition: ="Not Started" → Light Red (#FFE6E6)
Condition: ="In Progress" → Light Yellow (#FFF3CD)
Condition: ="Complete" → Light Green (#E9F7E9)
Condition: ="Validated" → Dark Green fill (#70AD47), White text
```

**Rule 5: Derogation Alert**
```
Applies to: H2:H1000
Condition: =ISNUMBER(SEARCH("Derogation",$H2))
Format: Yellow fill (#FFFF99), Red text, Bold
Purpose: Draw attention to derogations (should be rare)
```

### Formulas

**Column A (Transfer ID):**
```excel
=TEXT(ROW()-1,"XFER-0000")
```

**Column G (Adequacy Status):**
```excel
=IF(F2="","",IF(COUNTIF(EUAdequacyCountries,F2)>0,"Adequate","NOT Adequate"))
```
Logic: Check if destination country in adequacy list

**Column M (TIA Required?):**
```excel
=IF(G2="NOT Adequate","YES",IF(G2="Adequate","NO",""))
```

**Column AA (Last Updated):**
```excel
=TODAY()
```
Note: This will update every time workbook recalculates. For true "last edited" tracking, use VBA or instruct user to manually update.

### Row Height and Wrapping

- Header row (Row 1): Height 40, Wrap text enabled
- Data rows: Height 30 (increased for wrapped text in multi-line fields)
- Wrap text enabled for: C, Q, V, X, AC, AD, AE

### Freeze Panes
```
Freeze at: B2 (freeze row 1 header + column A Transfer ID)
```

### Worksheet Protection

- **Protection ON** with password "privacy2024"
- **Allow users to:**
  - Select locked/unlocked cells: YES
  - Format cells: NO
  - Insert rows: NO (prevent accidental insertion breaking formulas)
  - Delete rows: NO
  - Sort: YES
  - Use AutoFilter: YES
- **Unlock ranges:** B2:F1000, H2:L1000, N2:AB1000 (input fields only)
- **Lock ranges:** A2:A1000 (Transfer ID), G2:G1000 (Adequacy Status), M2:M1000 (TIA Required) - calculated fields

---

## Sheet 3: Transfer Impact Assessment (TIA) Register

### Purpose
Document Transfer Impact Assessments per Schrems II requirements for non-adequate country transfers.

### Column Definitions

| Col | Column Name | Data Type | Width | Validation | Formula/Notes |
|-----|------------|-----------|-------|------------|---------------|
| A | TIA ID | Text | 12 | Auto-generated | `="TIA-" & TEXT(ROW()-1, "0000")` |
| B | Transfer ID | Dropdown | 12 | Required | Link to Sheet 2 (only non-adequate transfers) |
| C | TIA Status | Dropdown | 15 | Required | {Not Started, In Progress, Complete, Approved} |
| D | Destination Country | Formula | 20 | Calculated | `=VLOOKUP(B2,Sheet2!A:F,6,FALSE)` pulls from Sheet 2 |
| E | Assessment Date | Date | 12 | Required | When TIA conducted |
| F | Assessor Name | Text | 20 | Required | Who conducted TIA (usually DPO or Legal) |
| G | Surveillance Laws Identified | Text | 40 | Required | List applicable laws (e.g., "FISA 702, EO 12333, CLOUD Act") |
| H | Government Access Risk Level | Dropdown | 18 | Required | {Low, Medium, High, Critical} |
| I | Risk Level Justification | Text | 50 | Required | Explain risk assessment |
| J | Importer Type | Dropdown | 20 | Required | {Cloud Provider, SaaS Platform, Processor (Other), Controller} |
| K | Importer Subject to Surveillance Laws? | Boolean | 15 | Required | Checkbox |
| L | Data Access Requests (History) | Text | 30 | Optional | Check importer transparency report |
| M | Supplementary Measures (Technical) | Text | 50 | Required | Encryption, pseudonymization, etc. |
| N | Supplementary Measures (Contractual) | Text | 50 | Required | DPA clauses (challenge obligation, notification) |
| O | Supplementary Measures (Organizational) | Text | 50 | Required | Governance, monitoring, training |
| P | Residual Risk Level | Dropdown | 15 | Required | {Low, Medium, High, Critical} AFTER mitigation |
| Q | TIA Conclusion | Dropdown | 20 | Required | {PASS, PASS with Conditions, FAIL} |
| R | Conditions (if PASS with Conditions) | Text | 50 | Conditional | What conditions must be maintained |
| S | DPO Approval | Text | 20 | Required | DPO name + approval date |
| T | Legal Counsel Review | Text | 20 | Optional | Legal name + review date |
| U | Review Frequency | Dropdown | 15 | Required | {Quarterly, Semi-Annually, Annually} |
| V | Next Review Date | Date | 12 | Required | When to reassess TIA |
| W | Review Triggers | Text | 40 | Optional | Events triggering early review (e.g., "If FISA 702 amended") |
| X | Evidence Links | Text | 30 | Optional | Link to Sheet 5 evidence |
| Y | Notes | Text | 40 | Optional | Additional context |

### Dropdowns and Validation

**B: Transfer ID Dropdown**
```
Source: =Sheet2!$A$2:$A$1000
Only show: Transfers where Sheet2 Column G = "NOT Adequate"
Note: Excel limitation - cannot filter dropdown by formula. Python script generates filtered list.
```

**C: TIA Status**
```
Values: "Not Started, In Progress, Complete, Approved"
```

**H: Government Access Risk Level**
```
Values: "Low, Medium, High, Critical"
```

**J: Importer Type**
```
Values: "Cloud Infrastructure Provider, SaaS Platform, Data Processor (Other), Joint Controller, Independent Third Party, Telecommunications Provider"
```

**P: Residual Risk Level**
```
Values: "Low, Medium, High, Critical"
Note: Should generally be LOWER than column H (Government Access Risk) after mitigation
```

**Q: TIA Conclusion**
```
Values: "PASS, PASS with Conditions, FAIL"
```

**U: Review Frequency**
```
Values: "Quarterly, Semi-Annually, Annually"
Default: Annually
```

### Conditional Formatting

**Rule 1: High/Critical Residual Risk**
```
Applies to: P2:P1000
Condition: =OR($P2="High",$P2="Critical")
Format: Red fill (#FFC7CE), Red text, Bold
Purpose: Flag high residual risk (may require SA consultation per GDPR Art. 36)
```

**Rule 2: TIA Overdue**
```
Applies to: V2:V1000
Condition: =$V2<TODAY()
Format: Orange fill (#FFD966), Dark Orange text
Purpose: Highlight TIAs past review date
```

**Rule 3: FAIL Conclusion**
```
Applies to: Q2:Q1000
Condition: ="FAIL"
Format: Red fill, White text, Bold
Purpose: Transfer should be suspended if TIA fails
```

**Rule 4: Status Color-Coding**
```
Applies to: C2:C1000
Condition: ="Not Started" → Light Red
Condition: ="In Progress" → Light Yellow
Condition: ="Complete" → Light Blue (#B4C6E7)
Condition: ="Approved" → Light Green
```

### Formulas

**Column A (TIA ID):**
```excel
=TEXT(ROW()-1,"TIA-0000")
```

**Column D (Destination Country):**
```excel
=IF(B2="","",VLOOKUP(B2,Sheet2!A:F,6,FALSE))
```
Logic: Lookup Transfer ID in Sheet 2, return Destination Country

**Column V (Next Review Date):**
```excel
=IF(E2="","",
  IF(U2="Quarterly",DATE(YEAR(E2),MONTH(E2)+3,DAY(E2)),
  IF(U2="Semi-Annually",DATE(YEAR(E2),MONTH(E2)+6,DAY(E2)),
  DATE(YEAR(E2)+1,MONTH(E2),DAY(E2)))))
```
Logic: Calculate next review based on frequency

### Row Height and Wrapping

- Header row: Height 40, Wrap text
- Data rows: Height 35 (taller for multi-line fields)
- Wrap text: G, I, M, N, O, R, W, X, Y

### Freeze Panes
```
Freeze at: B2
```

### Worksheet Protection

- Protected with password "privacy2024"
- Unlock: B2:C1000, E2:F1000, G2:Y1000 (input fields)
- Lock: A2:A1000 (TIA ID), D2:D1000 (Destination Country - calculated)

---

## Sheet 4: Processor Agreement Tracker

### Purpose
Track Data Processing Agreements (DPAs) and verify transfer safeguards for processor relationships.

### Column Definitions

| Col | Column Name | Data Type | Width | Validation | Formula/Notes |
|-----|------------|-----------|-------|------------|---------------|
| A | Processor ID | Text | 12 | Auto-generated | `="PROC-" & TEXT(ROW()-1, "0000")` |
| B | Transfer ID | Dropdown | 12 | Required | Link to Sheet 2 transfers |
| C | Processor Name | Text | 30 | Required | Legal entity name |
| D | Processor Country/Region | Text | 25 | Required | Where processor incorporated/operates |
| E | Processor Data Locations | Text | 35 | Required | All countries where data processed/stored |
| F | DPA Exists? | Boolean | 12 | Required | Checkbox |
| G | DPA Signature Date | Date | 15 | Conditional | If DPA=TRUE |
| H | DPA File Location | Text | 40 | Conditional | File path or document management system link |
| I | DPA GDPR Art. 28 Compliant? | Boolean | 15 | Required | Checkbox - does DPA meet Art. 28 requirements? |
| J | SCCs Included in DPA? | Boolean | 15 | Conditional | If processor in non-adequate country |
| K | SCC Version | Dropdown | 20 | Conditional | {2021 Module 2, 2021 Module 3, 2010 (Invalid)} |
| L | SCC Signature Date | Date | 15 | Conditional | When both parties signed SCCs |
| M | Subprocessor List Provided? | Boolean | 15 | Required | Checkbox |
| N | Number of Subprocessors | Number | 12 | Optional | Count |
| O | Subprocessor Authorization | Dropdown | 20 | Required | {General Authorization, Specific Authorization} |
| P | Subprocessor Notification Received? | Boolean | 15 | Optional | Checkbox - did processor notify of subprocessor changes? |
| Q | Subprocessor SCCs Flow Down? | Boolean | 15 | Conditional | If subprocessor in non-adequate country |
| R | TIA Reference | Text | 15 | Conditional | Link to Sheet 3 TIA ID |
| S | Audit Rights in DPA? | Boolean | 12 | Required | Checkbox |
| T | Last Audit Date | Date | 12 | Optional | When processor last audited |
| U | Next Audit Date | Date | 12 | Optional | Scheduled audit |
| V | SOC 2 / ISO 27001 Certified? | Boolean | 15 | Optional | Checkbox |
| W | Certification Date | Date | 12 | Conditional | If certified |
| X | Data Return/Deletion Clause? | Boolean | 15 | Required | Checkbox |
| Y | Breach Notification Clause? | Boolean | 15 | Required | Checkbox - 72hr notification required |
| Z | Compliance Status | Dropdown | 15 | Required | {Compliant, Partially Compliant, Non-Compliant} |
| AA | Gap Description | Text | 40 | Conditional | If non-compliant, what's missing |
| AB | Remediation Action | Text | 40 | Conditional | What needs to be done |
| AC | Remediation Owner | Text | 20 | Conditional | Who responsible |
| AD | Remediation Deadline | Date | 12 | Conditional | Target date |
| AE | Notes | Text | 40 | Optional | Additional context |

### Dropdowns and Validation

**B: Transfer ID Dropdown**
```
Source: =Sheet2!$A$2:$A$1000
Filter: Only show transfers where Sheet2 Column P = "Controller-to-Processor"
```

**K: SCC Version**
```
Values: "2021 Module 2 (Controller-to-Processor), 2021 Module 3 (Processor-to-Processor), 2010 Version (INVALID - Must Update)"
```

**O: Subprocessor Authorization**
```
Values: "General Authorization (Art. 28(2)), Specific Authorization (Art. 28(2))"
```

**Z: Compliance Status**
```
Values: "Compliant, Partially Compliant, Non-Compliant"
```

### Conditional Formatting

**Rule 1: No DPA**
```
Applies to: F2:F1000
Condition: =F2=FALSE
Format: Red fill, Red text, Bold
Purpose: Critical gap - processor without DPA violates GDPR Art. 28
```

**Rule 2: Old SCCs**
```
Applies to: K2:K1000
Condition: =ISNUMBER(SEARCH("2010",K2))
Format: Red fill, Red text, Bold
Purpose: Invalid SCCs (deadline passed Sept 2022)
```

**Rule 3: Missing SCCs for Non-Adequate**
```
Applies to: J2:J1000
Condition: =AND(VLOOKUP($B2,Sheet2!$A:$G,7,FALSE)="NOT Adequate",$J2=FALSE)
Format: Red fill, Red text, Bold
Purpose: Non-adequate processor without SCCs
```

**Rule 4: Overdue Audit**
```
Applies to: U2:U1000
Condition: =AND($U2<TODAY(),$U2<>"")
Format: Orange fill, Dark Orange text
Purpose: Audit overdue per DPA
```

**Rule 5: Compliance Status**
```
Applies to: Z2:Z1000
Condition: ="Compliant" → Light Green
Condition: ="Partially Compliant" → Light Yellow
Condition: ="Non-Compliant" → Light Red
```

### Formulas

**Column A (Processor ID):**
```excel
=TEXT(ROW()-1,"PROC-0000")
```

### Row Height and Wrapping

- Header row: Height 40, Wrap text
- Data rows: Height 30
- Wrap text: D, E, H, AA, AB, AE

### Freeze Panes
```
Freeze at: B2
```

### Worksheet Protection

- Protected with password "privacy2024"
- Unlock: B2:H1000, I2:AE1000 (all input fields)
- Lock: A2:A1000 (Processor ID - auto-generated)

---

**END OF PART II: Technical Specifications (Sheets 1-4)**

## PART III: Technical Specifications (Sheets 5-8) + Python Implementation

---

## Sheet 5: Evidence Repository

### Purpose
Centralized storage of audit evidence supporting cross-border transfer compliance.

### Column Definitions

| Col | Column Name | Data Type | Width | Validation | Notes |
|-----|------------|-----------|-------|------------|-------|
| A | Evidence ID | Text | 12 | Auto-generated | `="EVID-" & TEXT(ROW()-1, "0000")` |
| B | Transfer ID | Dropdown | 12 | Optional | Link to Sheet 2 |
| C | TIA ID | Dropdown | 12 | Optional | Link to Sheet 3 |
| D | Processor ID | Dropdown | 12 | Optional | Link to Sheet 4 |
| E | Evidence Type | Dropdown | 25 | Required | See dropdown values below |
| F | Evidence Description | Text | 50 | Required | What this evidence proves |
| G | Document Name | Text | 40 | Required | File name |
| H | File Location | Text | 50 | Required | Full path or DMS link |
| I | Upload Date | Date | 12 | Required | When evidence collected |
| J | Evidence Owner | Text | 20 | Required | Who maintains evidence |
| K | Last Verified | Date | 12 | Optional | When last checked for validity |
| L | Expiry Date | Date | 12 | Conditional | If evidence has expiration (e.g., DPF certification) |
| M | Status | Dropdown | 12 | Required | {Current, Expired, Superseded} |
| N | Notes | Text | 40 | Optional | Additional context |

### Dropdowns

**E: Evidence Type**
```
Values:

- Adequacy Decision (EU Commission)
- EU-US DPF Certification
- Standard Contractual Clauses (Signed)
- Data Processing Agreement (Signed)
- Transfer Impact Assessment (TIA)
- Legal Assessment Memo
- Supplementary Measures Documentation
- Encryption Configuration Screenshots
- Transparency Report (Processor)
- SOC 2 / ISO 27001 Certificate
- Audit Report (Processor Audit)
- Subprocessor List
- DPO Approval Email
- Legal Counsel Review
- Government Access Request (if any)
- Breach Notification Record
- Training Materials
- Policy Document
- Other

```

**M: Status**
```
Values: "Current, Expired, Superseded, Under Review"
```

### Conditional Formatting

**Rule 1: Expired Evidence**
```
Applies to: M2:M1000
Condition: ="Expired"
Format: Red fill, Red text, Bold
```

**Rule 2: Expiry Warning (30 days)**
```
Applies to: L2:L1000
Condition: =AND($L2<>"", $L2-TODAY()<=30, $L2-TODAY()>0)
Format: Orange fill, Dark Orange text
Purpose: Warn of upcoming expiry (e.g., DPF cert renewal needed)
```

### Row Height and Wrapping

- Header row: Height 40, Wrap text
- Data rows: Height 25
- Wrap text: F, G, H, N

### Freeze Panes
```
Freeze at: B2
```

### Worksheet Protection

- Protected with password "privacy2024"
- Unlock: B2:N1000 (all input fields)
- Lock: A2:A1000 (Evidence ID)

---

## Sheet 6: Gap Analysis

### Purpose
Identify and track remediation of cross-border transfer compliance gaps.

### Column Definitions

| Col | Column Name | Data Type | Width | Validation | Notes |
|-----|------------|-----------|-------|------------|-------|
| A | Gap ID | Text | 12 | Auto-generated | `="GAP-" & TEXT(ROW()-1, "0000")` |
| B | Transfer ID | Dropdown | 12 | Required | Link to Sheet 2 |
| C | Gap Type | Dropdown | 25 | Required | See dropdown values below |
| D | Gap Description | Text | 50 | Required | Clear explanation of gap |
| E | Affected Systems | Text | 30 | Required | Which systems/transfers impacted |
| F | Affected Data Subjects | Text | 25 | Required | Who is impacted (e.g., "~5,000 customers") |
| G | Risk Level | Dropdown | 12 | Required | {Critical, High, Medium, Low} |
| H | Likelihood | Dropdown | 12 | Required | {Certain, High, Medium, Low} |
| I | Impact | Dropdown | 12 | Required | {Severe, High, Moderate, Low} |
| J | Risk Score | Formula | 10 | Calculated | Likelihood × Impact numeric |
| K | GDPR Article Violated | Text | 20 | Optional | E.g., "Art. 44, Art. 46(1)" |
| L | Potential Penalties | Text | 35 | Optional | "Up to 4% annual revenue" |
| M | Discovery Date | Date | 12 | Required | When gap identified |
| N | Remediation Action | Text | 50 | Required | What needs to be done |
| O | Remediation Owner | Text | 20 | Required | Responsible person/team |
| P | Estimated Effort | Text | 15 | Optional | Time/resources (e.g., "8 hours") |
| Q | Target Completion Date | Date | 12 | Required | Deadline |
| R | Actual Completion Date | Date | 12 | Optional | When actually completed |
| S | Status | Dropdown | 12 | Required | {Open, In Progress, Completed, Blocked} |
| T | Blocking Issue | Text | 35 | Conditional | If status = Blocked |
| U | Escalation Level | Dropdown | 15 | Optional | {None, CISO, DPO, Legal, Board} |
| V | Verification Method | Text | 30 | Optional | How completion will be verified |
| W | Verification Date | Date | 12 | Optional | When verified |
| X | Verified By | Text | 20 | Optional | Who verified closure |
| Y | Notes | Text | 40 | Optional | Additional context |

### Dropdowns

**C: Gap Type**
```
Values:

- Undocumented Transfer
- Missing Transfer Mechanism
- Missing SCCs
- Old SCCs (2010 version)
- Missing TIA
- Inadequate Supplementary Measures
- No DPA with Processor
- DPA Not GDPR-Compliant
- Subprocessor Without SCCs
- Unlawful Derogation Use
- Expired DPF Certification
- Missing Processor Audit
- Incomplete Evidence
- No DPO Approval
- Other

```

**G: Risk Level**
```
Values: "Critical, High, Medium, Low"
```

**H: Likelihood**
```
Values: "Certain (5), High (4), Medium (3), Low (2), Very Low (1)"
Note: Include numeric values for risk score calculation
```

**I: Impact**
```
Values: "Severe (5), High (4), Moderate (3), Minor (2), Negligible (1)"
```

**S: Status**
```
Values: "Open, In Progress, Completed, Blocked, Deferred"
```

**U: Escalation Level**
```
Values: "None, DPO, Legal Counsel, CISO, Privacy Committee, Executive Team"
```

### Formulas

**Column A (Gap ID):**
```excel
=TEXT(ROW()-1,"GAP-0000")
```

**Column J (Risk Score):**
```excel
=VALUE(LEFT(H2,1)) * VALUE(LEFT(I2,1))
```
Logic: Extract numeric value from Likelihood × Impact (result 1-25)

Risk Score Interpretation:

- 20-25 = Critical
- 12-19 = High
- 5-11 = Medium
- 1-4 = Low

### Conditional Formatting

**Rule 1: Critical Gaps**
```
Applies to: G2:G1000
Condition: ="Critical"
Format: Red fill (#FFC7CE), Red text, Bold
```

**Rule 2: High Gaps**
```
Applies to: G2:G1000
Condition: ="High"
Format: Orange fill (#FFD966), Dark Orange text
```

**Rule 3: Overdue Remediation**
```
Applies to: Q2:Q1000
Condition: =AND($Q2<TODAY(), $S2<>"Completed")
Format: Red fill, White text, Bold
Purpose: Deadline passed but gap still open
```

**Rule 4: Status Color-Coding**
```
Applies to: S2:S1000
Condition: ="Open" → Light Red
Condition: ="In Progress" → Light Yellow
Condition: ="Completed" → Light Green
Condition: ="Blocked" → Gray (#D9D9D9)
```

**Rule 5: Risk Score Heat Map**
```
Applies to: J2:J1000
Condition: >=20 → Dark Red (#C00000), White text
Condition: >=12 → Orange (#FFA500)
Condition: >=5 → Yellow (#FFD966)
Condition: <5 → Light Green (#C6EFCE)
```

### Row Height and Wrapping

- Header row: Height 40, Wrap text
- Data rows: Height 35
- Wrap text: D, E, N, T, V, Y

### Freeze Panes
```
Freeze at: B2
```

### Worksheet Protection

- Protected with password "privacy2024"
- Unlock: B2:Y1000 (all input fields)
- Lock: A2:A1000 (Gap ID), J2:J1000 (Risk Score - calculated)

---

## Sheet 7: Compliance Dashboard

### Purpose
Auto-calculated metrics for executive oversight of cross-border transfer compliance.

### Structure

**Title Block (A1:L3):**

- Merge A1:L3
- Title: "Cross-Border Transfer Compliance Dashboard"
- Font: Arial 18pt Bold, White
- Background: Dark Blue (#1F4E78)

### Metrics Section (A5:L40)

| Metric | Formula | Target | Cell Range |
|--------|---------|--------|------------|
| **Total Transfers** | `=COUNTA(Sheet2!A:A)-1` | N/A | B6 |
| **Transfers to Adequate Countries** | `=COUNTIF(Sheet2!G:G,"Adequate")` | Maximize | B8 |
| **Transfers to Non-Adequate Countries** | `=COUNTIF(Sheet2!G:G,"NOT Adequate")` | Minimize | B9 |
| **% Non-Adequate** | `=B9/B6` | <50% | B10 (percentage format) |
| **Transfers with Valid Mechanism** | `=COUNTA(Sheet2!H:H)-COUNTBLANK(Sheet2!H:H)-1` | 100% | B12 |
| **Transfers Missing Mechanism** | `=B6-B12` | 0 | B13 |
| **% Transfers Compliant** | `=B12/B6` | 100% | B14 (percentage, red if <100%) |
| **TIAs Required** | `=COUNTIF(Sheet2!M:M,"YES")` | = B9 | B16 |
| **TIAs Completed** | `=COUNTA(Sheet3!A:A)-1` | = B16 | B17 |
| **TIAs Missing** | `=B16-B17` | 0 | B18 (red if >0) |
| **TIAs Overdue for Review** | `=COUNTIF(Sheet3!V:V,"<"&TODAY())` | 0 | B19 (orange if >0) |
| **DPAs with Processors** | `=COUNTIF(Sheet4!F:F,TRUE)` | = Processor count | B21 |
| **Processors Without DPA** | `=COUNTIF(Sheet4!F:F,FALSE)` | 0 | B22 (red if >0) |
| **SCCs Signed (2021 Version)** | `=COUNTIF(Sheet4!K:K,"2021*")` | = Non-adequate processors | B23 |
| **Old SCCs (2010)** | `=COUNTIF(Sheet4!K:K,"*2010*")` | 0 | B24 (red if >0) |
| **Critical Gaps** | `=COUNTIF(Sheet6!G:G,"Critical")` | 0 | B26 (red if >0) |
| **High Gaps** | `=COUNTIF(Sheet6!G:G,"High")` | 0 | B27 (orange if >0) |
| **Medium Gaps** | `=COUNTIF(Sheet6!G:G,"Medium")` | <3 | B28 |
| **Low Gaps** | `=COUNTIF(Sheet6!G:G,"Low")` | N/A | B29 |
| **Gaps Completed** | `=COUNTIF(Sheet6!S:S,"Completed")` | N/A | B31 |
| **Gaps In Progress** | `=COUNTIF(Sheet6!S:S,"In Progress")` | N/A | B32 |
| **Gaps Open** | `=COUNTIF(Sheet6!S:S,"Open")` | 0 | B33 (orange if >5) |
| **Average Gap Age (Days)** | `=AVERAGE(TODAY()-Sheet6!M:M)` | <30 | B34 (orange if >60) |
| **Evidence Documents Collected** | `=COUNTA(Sheet5!A:A)-1` | N/A | B36 |
| **Evidence Items Expired** | `=COUNTIF(Sheet5!M:M,"Expired")` | 0 | B37 (red if >0) |
| **Evidence Expiring in 30 Days** | `=COUNTIF(Sheet5!L:L,"<="&TODAY()+30)` | 0 | B38 (orange if >0) |

### Conditional Formatting for Dashboard Metrics

**Critical Alerts (Red):**

- B13 (Transfers Missing Mechanism) > 0
- B18 (TIAs Missing) > 0
- B22 (Processors Without DPA) > 0
- B24 (Old SCCs) > 0
- B26 (Critical Gaps) > 0
- B37 (Evidence Expired) > 0

**Warnings (Orange):**

- B10 (% Non-Adequate) >= 50%
- B19 (TIAs Overdue) > 0
- B27 (High Gaps) > 0
- B33 (Open Gaps) > 5
- B34 (Average Gap Age) > 60 days
- B38 (Evidence Expiring) > 0

**Good Status (Green):**

- B14 (% Transfers Compliant) = 100%

### Charts

**Chart 1: Transfer Mechanisms (Pie Chart)**

- Location: D6:K15
- Data source: Count by transfer mechanism from Sheet 2 Column H
- Labels: Adequacy, EU-US DPF, SCCs, BCRs, Derogations, Missing
- Colors: Green (Adequacy/DPF), Blue (SCCs/BCRs), Yellow (Derogations), Red (Missing)

**Chart 2: Transfer Destinations (Bar Chart - Top 10)**

- Location: D17:K27
- Data source: Count by destination country from Sheet 2 Column F
- X-axis: Top 10 countries
- Y-axis: Number of transfers
- Colors: Green bars if adequate, Red bars if non-adequate

**Chart 3: Gap Status (Stacked Bar Chart)**

- Location: D29:K39
- Data source: Sheet 6 Risk Level × Status
- Bars: Critical/High/Medium/Low
- Stack segments: Open, In Progress, Completed
- Colors: Red (Critical Open), Orange (High Open), Yellow (Medium Open), Green (Completed)

### Dashboard Notes Section (A42:L50)

Pre-populated guidance:
```
DASHBOARD INTERPRETATION:

GREEN = Good

- All transfers have valid mechanisms
- All TIAs completed
- All DPAs in place
- Zero critical/high gaps

ORANGE = Warning

- Some non-adequate transfers without TIA
- TIAs overdue for review
- High-risk gaps present
- Evidence expiring soon

RED = Critical Issue

- Transfers without mechanism (unlawful)
- Processors without DPA (Art. 28 violation)
- Old SCCs (invalid)
- Critical gaps unresolved

ACTION REQUIRED:

- Red metrics: Immediate action (1-2 weeks)
- Orange metrics: Short-term action (1-3 months)

```

### Worksheet Protection

- Entire sheet protected (all formulas locked)
- No user editing allowed (read-only dashboard)
- No password required (calculations only)

---

## Sheet 8: Approval & Sign-Off

### Purpose
Document stakeholder approvals for cross-border transfer assessment and remediation plan.

### Column Definitions

| Col | Column Name | Data Type | Width | Validation | Notes |
|-----|------------|-----------|-------|------------|-------|
| A | Approval ID | Text | 12 | Auto-generated | `="APPR-" & TEXT(ROW()-1, "0000")` |
| B | Approval Type | Dropdown | 25 | Required | See dropdown values below |
| C | Transfer ID / TIA ID / Gap ID | Dropdown | 15 | Optional | Link to related assessment |
| D | What is Being Approved | Text | 50 | Required | Description |
| E | Approver Name | Text | 25 | Required | Who is approving |
| F | Approver Role | Dropdown | 25 | Required | Title/responsibility |
| G | Approval Date | Date | 12 | Required | When approved |
| H | Approval Method | Dropdown | 20 | Required | How approval obtained |
| I | Approval Status | Dropdown | 15 | Required | {Pending, Approved, Rejected, Conditional} |
| J | Conditions / Caveats | Text | 50 | Conditional | If status = Conditional |
| K | Rejection Reason | Text | 50 | Conditional | If status = Rejected |
| L | Approval Expiry Date | Date | 12 | Optional | If approval time-limited |
| M | Evidence Reference | Text | 25 | Optional | Link to approval email/document |
| N | Notes | Text | 40 | Optional | Additional context |

### Dropdowns

**B: Approval Type**
```
Values:

- DPO Approval (TIA)
- DPO Approval (Transfer Mechanism)
- Legal Counsel Review (SCCs)
- Legal Counsel Review (Derogation)
- CISO Approval (Technical Measures)
- Business Owner Acceptance (Transfer)
- Privacy Committee Review (Annual Assessment)
- Executive Approval (High-Risk Transfer)
- CFO Approval (Budget for Remediation)
- Supervisory Authority Consultation (Art. 36)

```

**F: Approver Role**
```
Values: "DPO, Legal Counsel, CISO, Privacy Officer, Business Owner, CFO, CEO, Privacy Committee, Supervisory Authority"
```

**H: Approval Method**
```
Values: "Email, Meeting Minutes, Digital Signature, Written Memo, Verbal (Documented), Form Submission"
```

**I: Approval Status**
```
Values: "Pending, Approved, Rejected, Conditional, Withdrawn"
```

### Conditional Formatting

**Rule 1: Pending Approvals**
```
Applies to: I2:I1000
Condition: ="Pending"
Format: Orange fill, Dark Orange text
```

**Rule 2: Rejected Approvals**
```
Applies to: I2:I1000
Condition: ="Rejected"
Format: Red fill, Red text, Bold
```

**Rule 3: Approved**
```
Applies to: I2:I1000
Condition: ="Approved"
Format: Light Green (#C6EFCE), Dark Green text
```

**Rule 4: Expired Approvals**
```
Applies to: L2:L1000
Condition: =AND($L2<>"", $L2<TODAY())
Format: Red fill, White text
Purpose: Time-limited approval expired (e.g., annual TIA approval)
```

### Row Height and Wrapping

- Header row: Height 40, Wrap text
- Data rows: Height 25
- Wrap text: D, J, K, M, N

### Freeze Panes
```
Freeze at: B2
```

### Worksheet Protection

- Protected with password "privacy2024"
- Unlock: B2:N1000 (all input fields)
- Lock: A2:A1000 (Approval ID)

---

## Python Script Implementation Architecture

### Script Name
```
generate_a5346_cross_border_transfer_assessment.py
```

### Command-Line Usage
```bash
# Basic usage
python3 generate_a5346_cross_border_transfer_assessment.py

# Custom output directory
python3 generate_a5346_cross_border_transfer_assessment.py --output /path/to/output

# Custom date suffix
python3 generate_a5346_cross_border_transfer_assessment.py --date 20250130
```

### Script Structure

#### 1. Header (Lines 1-250)
**REFERENCE QUALITY HEADER** per A.8.24/A.5.34.1 standard:

- Encoding declaration: `# -*- coding: utf-8 -*-`
- Title banner (80 chars, ===)
- Control + Domain identification
- SAMPLE SCRIPT warning (5+ customization areas)
- DESCRIPTION section (Purpose, Scope, Structure, Features, Integration)
- REQUIREMENTS section
- USAGE section (Basic, Advanced, 12+ Post-Generation Steps)
- METADATA section (Control, Domain, Version, Author, Date, Related Docs)
- CHANGE HISTORY
- IMPORTANT NOTES (6+ subsections)
- Closing banner

#### 2. Imports (Lines 252-260)
```python
import argparse
import os
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, Protection
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.utils import get_column_letter
```

#### 3. Configuration Constants (Lines 262-350)

**Color Palette:**
```python
COLORS = {
    'header_blue': 'FF1F4E78',
    'header_orange': 'FFC00000',
    'white': 'FFFFFFFF',
    'black': 'FF000000',
    'light_green': 'FFC6EFCE',
    'dark_green': 'FF006100',
    'light_yellow': 'FFFFEB9C',
    'dark_orange': 'FF9C5700',
    'light_red': 'FFFFC7CE',
    'dark_red': 'FF9C0006',
    'light_blue': 'FFB4C6E7',
    'dark_blue': 'FF002060',
    'light_gray': 'FFD9D9D9',
    'light_orange': 'FFFFD966',
}
```

**Dropdown Lists:**
```python
# CUSTOMIZE: Modify based on your organization
STATUS_OPTIONS = ["Not Started", "In Progress", "Complete", "Validated"]

TRANSFER_MECHANISMS_ADEQUATE = [
    "Adequacy Decision (GDPR Art. 45)",
    "EU-US Data Privacy Framework (DPF)",
]

TRANSFER_MECHANISMS_NON_ADEQUATE = [
    "Standard Contractual Clauses (SCCs)",
    "Binding Corporate Rules (BCRs)",
    "Derogation - Explicit Consent (Art. 49(1)(a))",
    "Derogation - Contract Necessity (Art. 49(1)(b))",
    "Derogation - Legal Claims (Art. 49(1)(c))",
    "Derogation - Vital Interests (Art. 49(1)(d))",
    "Derogation - Public Interest (Art. 49(1)(e))",
    "Derogation - Legitimate Interest - Occasional (Art. 49(1)(f))",
]

# EU Adequacy Decisions (as of 2025)
EU_ADEQUACY_COUNTRIES = [
    "Andorra",
    "Argentina",
    "Canada (Commercial Organizations)",
    "Faroe Islands",
    "Guernsey",
    "Israel",
    "Isle of Man",
    "Japan",
    "Jersey",
    "New Zealand",
    "Republic of Korea",
    "Switzerland",
    "United Kingdom",
    "Uruguay",
    # Note: EU/EEA member states not listed (within EU, no cross-border transfer)
]

SCC_VERSIONS = [
    "2021 Module 1 (Controller-to-Controller)",
    "2021 Module 2 (Controller-to-Processor)",
    "2021 Module 3 (Processor-to-Processor)",
    "2021 Module 4 (Processor-to-Controller)",
    "2010 Version (INVALID - Must Update)",
]

RISK_LEVELS = ["Low", "Medium", "High", "Critical"]

# Protection password
PROTECTION_PASSWORD = "privacy2024"

# Output filename prefix
FILE_PREFIX = "ISMS_A_5_34_6_Cross_Border_Transfer_Assessment"
```

#### 4. Utility Functions (Lines 352-450)

```python
def style_header_row(ws, row_num, color_hex, num_columns):
    """Apply consistent header styling."""
    # Implementation as per A.5.34.1 pattern

def add_dropdown(ws, cell_range, options, error_msg, allow_blank=False):
    """Add dropdown data validation."""
    # Implementation

def add_conditional_formatting_risk(ws, column_letter, start_row, end_row):
    """Apply risk level color coding."""
    # Critical=Red, High=Orange, Medium=Yellow, Low=Green

def protect_sheet(ws, password=None, unlock_ranges=None):
    """Protect worksheet with specified unlocked ranges."""
    # Implementation

def create_named_range(wb, name, sheet_name, range_ref):
    """Create named range for formulas."""
    wb.defined_names[name] = f"{sheet_name}!{range_ref}"
```

#### 5. Sheet Creation Functions (Lines 452-1800)

**create_instructions_sheet(wb)**

- Populate Sheet 1 with GDPR Chapter V guidance
- Add adequacy decisions list
- Add transfer mechanism definitions
- Create named range "EUAdequacyCountries"
- Format as reference material (no inputs)

**create_transfer_register_sheet(wb)**

- Create Sheet 2 with 31 columns (A-AE)
- Add formula in Column A (Transfer ID)
- Add formula in Column G (Adequacy Status = VLOOKUP vs adequacy list)
- Add formula in Column M (TIA Required?)
- Add dropdowns for all validated columns
- Add conditional formatting (5 rules: missing mechanism, missing TIA, old SCCs, status colors, derogation alert)
- Protect sheet with unlocked input ranges

**create_tia_register_sheet(wb)**

- Create Sheet 3 with 25 columns (A-Y)
- Add formula in Column A (TIA ID)
- Add formula in Column D (Destination Country = VLOOKUP from Sheet 2)
- Add formula in Column V (Next Review Date based on frequency)
- Add dropdowns
- Add conditional formatting (4 rules: high residual risk, TIA overdue, FAIL conclusion, status colors)
- Protect sheet

**create_processor_tracker_sheet(wb)**

- Create Sheet 4 with 31 columns (A-AE)
- Add formula in Column A (Processor ID)
- Add dropdowns
- Add conditional formatting (5 rules: no DPA, old SCCs, missing SCCs for non-adequate, overdue audit, compliance status)
- Protect sheet

**create_evidence_repository_sheet(wb)**

- Create Sheet 5 with 14 columns (A-N)
- Add formula in Column A (Evidence ID)
- Add dropdowns
- Add conditional formatting (2 rules: expired evidence, expiry warning)
- Protect sheet

**create_gap_analysis_sheet(wb)**

- Create Sheet 6 with 25 columns (A-Y)
- Add formula in Column A (Gap ID)
- Add formula in Column J (Risk Score = Likelihood × Impact)
- Add dropdowns
- Add conditional formatting (5 rules: critical gaps, high gaps, overdue remediation, status colors, risk score heat map)
- Protect sheet

**create_dashboard_sheet(wb)**

- Create Sheet 7 with metrics (B6:B38)
- All metrics are formulas pulling from Sheets 2-6
- Add charts:
  - Pie chart: Transfer mechanisms
  - Bar chart: Top 10 destination countries
  - Stacked bar: Gap status by risk level
- Add conditional formatting to metric cells (red/orange/green alerts)
- Add dashboard notes section
- Protect entire sheet (read-only)

**create_approval_sheet(wb)**

- Create Sheet 8 with 14 columns (A-N)
- Add formula in Column A (Approval ID)
- Add dropdowns
- Add conditional formatting (4 rules: pending, rejected, approved, expired)
- Protect sheet

#### 6. Main Function (Lines 1802-1900)

```python
def main():
    """Generate Cross-Border Transfer Assessment workbook."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description='Generate ISMS A.5.34.6 Cross-Border Transfer Assessment workbook'
    )
    parser.add_argument('--output', type=str, default='.',
                        help='Output directory path')
    parser.add_argument('--date', type=str, default=None,
                        help='Date suffix (YYYYMMDD), defaults to today')
    args = parser.parse_args()
    
    # Determine output filename
    date_suffix = args.date if args.date else datetime.now().strftime('%Y%m%d')
    filename = f"{FILE_PREFIX}_{date_suffix}.xlsx"
    output_path = os.path.join(args.output, filename)
    
    # Create workbook
    wb = Workbook()
    wb.remove(wb.active)  # Remove default sheet
    
    # Create all sheets
    print("Creating Sheet 1: Instructions & Legend...")
    create_instructions_sheet(wb)
    
    print("Creating Sheet 2: Cross-Border Transfer Register...")
    create_transfer_register_sheet(wb)
    
    print("Creating Sheet 3: TIA Register...")
    create_tia_register_sheet(wb)
    
    print("Creating Sheet 4: Processor Agreement Tracker...")
    create_processor_tracker_sheet(wb)
    
    print("Creating Sheet 5: Evidence Repository...")
    create_evidence_repository_sheet(wb)
    
    print("Creating Sheet 6: Gap Analysis...")
    create_gap_analysis_sheet(wb)
    
    print("Creating Sheet 7: Compliance Dashboard...")
    create_dashboard_sheet(wb)
    
    print("Creating Sheet 8: Approval & Sign-Off...")
    create_approval_sheet(wb)
    
    # Save workbook
    print(f"Saving workbook to {output_path}...")
    wb.save(output_path)
    
    print(f"\nSuccess! Workbook created: {output_path}")
    print("\nNext steps:")
    print("1. Open workbook and review Sheet 1 (Instructions)")
    print("2. Complete Sheet 2 (Transfer Register) - identify all cross-border transfers")
    print("3. Conduct TIAs in Sheet 3 for non-adequate country transfers")
    print("4. Verify processor agreements in Sheet 4")
    print("5. Collect evidence in Sheet 5")
    print("6. Document gaps in Sheet 6 and create remediation plan")
    print("7. Review Sheet 7 (Dashboard) for compliance metrics")
    print("8. Obtain approvals in Sheet 8")
    print("9. Feed results into A.5.34.7 Privacy Compliance Dashboard")

if __name__ == '__main__':
    main()
```

### Script Deliverable

**Filename:** `generate_a5346_cross_border_transfer_assessment.py`  
**Total Lines:** ~1,900 lines  
**Header:** 250 lines (REFERENCE QUALITY per A.8.24/A.5.34.1 standard)  
**Code:** 1,650 lines

### Integration with A.5.34.7 (BIG DASHBOARD)

The A.5.34.7 consolidation script will use `openpyxl` to read this workbook:

```python
# In consolidate_a534_privacy_dashboard.py

from openpyxl import load_workbook

def extract_a5346_metrics(workbook_path):
    """Extract A.5.34.6 Cross-Border Transfer metrics."""
    wb = load_workbook(workbook_path, data_only=True)
    ws = wb['Dashboard']
    
    metrics = {
        'total_transfers': ws['B6'].value,
        'non_adequate_transfers': ws['B9'].value,
        'transfers_compliant_pct': ws['B14'].value,
        'tias_required': ws['B16'].value,
        'tias_completed': ws['B17'].value,
        'tias_missing': ws['B18'].value,
        'critical_gaps': ws['B26'].value,
        'high_gaps': ws['B27'].value,
    }
    
    wb.close()
    return metrics
```

---

**END OF PART III: Technical Specifications (Sheets 5-8) + Python Implementation**

**END OF ISMS-IMP-A.5.34.6**

---

**END OF SPECIFICATION**

---

*"The problems of language here are really serious. We wish to speak in some way about the structure of the atoms. But we cannot speak about atoms in ordinary language."*
— Werner Heisenberg

<!-- QA_VERIFIED: 2026-02-06 -->
