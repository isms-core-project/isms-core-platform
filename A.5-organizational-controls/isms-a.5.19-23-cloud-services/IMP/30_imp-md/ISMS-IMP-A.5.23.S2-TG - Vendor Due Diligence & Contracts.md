**ISMS-IMP-A.5.23.S2-TG - Vendor Due Diligence & Contracts**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Vendor Due Diligence & Contracts |
| **Related Policy** | ISMS-POL-A.5.19-23-S2 (Supplier Agreement Requirements), ISMS-POL-A.5.19-23-S5 (Cloud Services Security) |
| **Purpose** | Assess vendor security posture, contract adequacy, SLA compliance, data sovereignty, audit rights, and jurisdictional risks for all cloud service providers |
| **Target Audience** | Legal, Procurement, Security Teams, Compliance Officers, Risk Managers |
| **Assessment Type** | Vendor Due Diligence & Contract Analysis |
| **Review Cycle** | Quarterly (with annual comprehensive review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial Excel workbook specification | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.23.S2-UG.

---

# Technical Specification

## Workbook Structure Overview

**File:** `ISMS-IMP-A.5.23.S2_VendorDD_YYYYMMDD.xlsx`

**Total Sheets:** 10

**Architecture:**
```
Sheet 1:  Instructions & Legend (read-only reference)
Sheet 2:  Vendor Security Certifications (data collection)
Sheet 3:  Contract Terms Analysis (data collection)
Sheet 4:  SLA Requirements & Performance (data collection)
Sheet 5:  Data Sovereignty Compliance (data collection)
Sheet 6:  Forensics & Audit Rights (data collection)
Sheet 7:  Jurisdictional Risk Assessment (data collection)
Sheet 8:  Summary Dashboard (formulas, auto-calculated)
Sheet 9:  Evidence Register (central evidence tracking)
Sheet 10: Approval Sign-Off (workflow, signatures)
```

---

## Standard Column Definitions (A-Q)

**Present in ALL data collection sheets (Sheets 2-7):**

| Col | Header | Type | Validation | Default/Formula |
|-----|--------|------|------------|-----------------|
| A | Cloud Service Name | Text | Dropdown (from IMP-5.23.1) | - |
| B | Vendor Name | Text | Dropdown (from IMP-5.23.1) | - |
| C | Service Type | Text | Dropdown: SaaS, IaaS, PaaS, Security Service, Storage | - |
| D | Service Criticality | Text | Dropdown: Critical, High, Medium, Low | From IMP-5.23.1 |
| E | Data Classification | Text | Dropdown: Restricted, Confidential, Internal, Public | From IMP-5.23.1 |
| F | Contract Type | Text | Dropdown: MSA+DPA, Subscription, Enterprise Agreement, Trial/Free | - |
| G | Contract Start Date | Date | Date picker (DD.MM.YYYY) | - |
| H | Status | Text | Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | - |
| I | Evidence Location | Text | Hyperlink or file path | - |
| J | Gap Description | Text | Free text (required if H ≠ ✅) | - |
| K | Remediation Needed | Text | Dropdown: Yes, No | - |
| L | Exception ID | Text | Pattern: EXC-YYYY-NNN | - |
| M | Risk ID | Text | Pattern: RISK-YYYY-NNN | - |
| N | Compensating Controls | Text | Free text | - |
| O | Vendor Contact (Legal) | Email | Email format validation | - |
| P | Target Remediation Date | Date | Date picker (DD.MM.YYYY) | - |
| Q | Contract Owner | Text | Free text | - |

**Conditional Formatting (Applied to All Data Sheets):**

- Row with H = ❌ → Red background (#FFCCCC)
- Row with H = ⚠️ → Yellow background (#FFFFCC)
- Row with H = ✅ → Green background (#CCFFCC)
- Row with H = N/A → Gray background (#EEEEEE)

---

## Sheet-Specific Extended Columns

### Sheet 2: Vendor Security Certifications (Columns R-Y)

| Col | Header | Type | Validation | Purpose |
|-----|--------|------|------------|---------|
| R | ISO 27001 Status | Text | Dropdown: Yes, No, Expired, In Progress | Certification presence |
| S | ISO 27001 Cert Number | Text | Free text | Certificate ID |
| T | ISO 27001 Expiry Date | Date | Date picker | Validity end |
| U | ISO 27001 Scope Verified | Text | Dropdown: Yes, No, Partial | Service in scope? |
| V | SOC 2 Type II Status | Text | Dropdown: Yes, No, Type I Only, Expired | Audit report type |
| W | SOC 2 Audit Period | Text | Pattern: DD.MM.YYYY - DD.MM.YYYY | Report period |
| X | SOC 2 Opinion | Text | Dropdown: Unqualified, Qualified, Adverse | Auditor opinion |
| Y | Penetration Testing | Text | Dropdown: Annual, Semi-Annual, Quarterly, None | Test frequency |

---

### Sheet 3: Contract Terms Analysis (Columns R-Z)

| Col | Header | Type | Validation | Purpose |
|-----|--------|------|------------|---------|
| R | DPA Status | Text | Dropdown: Present, Absent, Under Negotiation | DPA existence |
| S | DPA Adequate? | Text | Dropdown: Yes, No, Partial | DPA quality |
| T | Security Reqs in Contract | Text | Dropdown: Yes, No, Generic | Security clauses |
| U | Liability Cap (€) | Number | Numeric (currency) | Liability limit |
| V | Liability Adequate? | Text | Dropdown: Yes (≥€1M), No (<€1M), None | Cap assessment |
| W | Subprocessor Notification | Text | Dropdown: Prior Notice, Post-Notice, None | Subprocessor control |
| X | Subprocessor Approval | Text | Dropdown: Opt-Out Right, No Control | Approval mechanism |
| Y | Exit Clause Present | Text | Dropdown: Yes, No | Termination terms |
| Z | Data Portability Guaranteed | Text | Dropdown: Yes, No, On Request | Export rights |

---

### Sheet 4: SLA Requirements & Performance (Columns R-X)

| Col | Header | Type | Validation | Purpose |
|-----|--------|------|------------|---------|
| R | SLA Uptime Commitment | Percentage | Range: 0-100% | Contractual SLA |
| S | Actual Uptime (Last Quarter) | Percentage | Range: 0-100% | Measured uptime |
| T | SLA Breaches (Count) | Integer | Numeric (≥0) | Breach instances |
| U | Total Downtime (Minutes) | Integer | Numeric (≥0) | Cumulative downtime |
| V | SLA Credits Owed (€) | Number | Numeric (currency) | Credits due |
| W | SLA Credits Claimed (€) | Number | Numeric (currency) | Credits requested |
| X | SLA Credits Received (€) | Number | Numeric (currency) | Credits paid |

**Formula (Auto-Calculate):**

- Column T: `=COUNTIF([monthly_data], "<"&R:R)` (count months below SLA)

---

### Sheet 5: Data Sovereignty Compliance (Columns R-Z)

| Col | Header | Type | Validation | Purpose |
|-----|--------|------|------------|---------|
| R | Data Storage Location | Text | Free text (e.g., "EU Multi-Geo (DE, NL)") | Where data stored |
| S | Data Processing Location | Text | Free text | Where data processed |
| T | Cross-Border Transfer | Text | Dropdown: Yes, No | Transfer occurs? |
| U | Transfer Mechanism | Text | Dropdown: SCCs, BCRs, Adequacy, None | Legal basis |
| V | SCCs Present in DPA | Text | Dropdown: Yes, No, N/A | SCCs included? |
| W | TIA Completed (if US transfer) | Text | Dropdown: Yes, No, N/A | Assessment done? |
| X | Encryption At-Rest | Text | Dropdown: Yes, No, Partial | Data at rest |
| Y | Encryption In-Transit | Text | Dropdown: Yes (TLS 1.2+), No | Data in transit |
| Z | Key Management | Text | Dropdown: Vendor, Customer (BYOK), Hybrid | Key control |

---

### Sheet 6: Forensics & Audit Rights (Columns R-X)

| Col | Header | Type | Validation | Purpose |
|-----|--------|------|------------|---------|
| R | Audit Rights in Contract | Text | Dropdown: Yes, Limited, No | Contractual rights |
| S | Audit Frequency Allowed | Text | Dropdown: Annual, On-Cause, None | Audit frequency |
| T | SOC 2 Type II Available | Text | Dropdown: Yes, Type I Only, No | Report access |
| U | SOC 2 Report Date | Date | Date picker | Report period end |
| V | On-Site Audit Feasible | Text | Dropdown: Yes, Virtual Only, No | Physical audit |
| W | Incident Investigation Support | Text | Dropdown: Strong, Adequate, Weak, None | Forensics help |
| X | Log Retention Period | Text | Dropdown: <90 days, 90-365 days, >365 days | Log availability |

---

### Sheet 7: Jurisdictional Risk Assessment (Columns R-AA)

| Col | Header | Type | Validation | Purpose |
|-----|--------|------|------------|---------|
| R | Vendor HQ Jurisdiction | Text | Dropdown: Switzerland, EU/EEA, UK, USA, Other | Legal HQ |
| S | Parent Company | Text | Free text | Ultimate owner |
| T | US CLOUD Act Exposure | Text | Dropdown: Yes, No, Unclear | CLOUD Act risk |
| U | TIA Completed | Text | Dropdown: Yes, No, N/A | Assessment done |
| V | TIA Risk Level | Text | Dropdown: Low, Medium, High, N/A | Risk rating |
| W | EU Data Residency Enabled | Text | Dropdown: Yes, No, N/A | Data boundary |
| X | Customer-Managed Keys | Text | Dropdown: Yes, No, N/A | BYOK/HYOK |
| Y | Residual Risk Accepted By | Text | Free text (Name, Title, Date) | Approver |
| Z | Risk Exception ID | Text | Pattern: RISK-YYYY-NNN | Risk register ref |
| AA | Mitigation Review Date | Date | Date picker (auto: +12 months) | Next review |

---

## Sheet 8: Summary Dashboard (Formulas)

**Auto-Calculated Metrics:**

| Metric | Formula Example | Description |
|--------|-----------------|-------------|
| Total Vendors Assessed | `=COUNTA(Sheet2!A:A)-1` | Row count |
| Critical Services Count | `=COUNTIF(Sheet2!D:D,"Critical")` | Criticality filter |
| Overall Compliance % | `=(COUNTIF(Sheet2!H:H,"✅")/COUNTA(Sheet2!H:H))*100` | % Compliant |
| High-Risk Vendors | `=COUNTIF(Sheet7!V:V,"High")` | TIA high risk |
| Pending SLA Credits (€) | `=SUM(Sheet4!V:V)-SUM(Sheet4!X:X)` | Unclaimed credits |
| Vendors Without ISO 27001 | `=COUNTIF(Sheet2!R:R,"No")` | Missing cert |
| Vendors Without DPA | `=COUNTIF(Sheet3!R:R,"Absent")` | Missing DPA |
| US CLOUD Act Exposure Count | `=COUNTIF(Sheet7!T:T,"Yes")` | US jurisdiction |

**Conditional Formatting:**

- Overall Compliance % <90%: Red
- Overall Compliance % 90-95%: Yellow
- Overall Compliance % >95%: Green

---

## Sheet 9: Evidence Register (Columns A-H)

| Col | Header | Type | Validation | Purpose |
|-----|--------|------|------------|---------|
| A | Evidence ID | Text | Pattern: EV-NNN | Unique ID |
| B | Vendor Name | Text | Dropdown (from Sheet 2) | Vendor link |
| C | Evidence Type | Text | Dropdown: ISO Cert, SOC 2, Contract, DPA, TIA, Screenshot, Other | Doc type |
| D | File Name | Text | Free text | Filename |
| E | File Location | Hyperlink | File path or URL | Link to file |
| F | Collection Date | Date | Date picker | When collected |
| G | Expiry Date (if applicable) | Date | Date picker | Validity end |
| H | Notes | Text | Free text | Additional info |

**Auto-Numbering:** Evidence ID auto-increments (EV-001, EV-002, ...)

---

## Sheet 10: Approval Sign-Off (Workflow)

| Section | Fields | Type | Purpose |
|---------|--------|------|---------|
| **ISMS Coordinator** | Name, Date, Decision, Comments | Text, Date, Dropdown | Quality check |
| **Legal** | Name, Date, Decision, Comments | Text, Date, Dropdown | Contract review |
| **Security / CISO** | Name, Date, Decision, Comments | Text, Date, Dropdown | Security review |
| **DPO / Compliance** | Name, Date, Decision, Comments | Text, Date, Dropdown | Regulatory review |
| **CISO Final** | Name, Date, Decision, Comments | Text, Date, Dropdown | Final approval |
| **Next Review Date** | Auto-calculate: Date + 90 days | Date | Calendar trigger |

**Decision Dropdown:** Approved, Conditionally Approved, Rejected

---

## Cell Protection & Workbook Security

**Protected Cells (Read-Only):**

- Base columns A-E (populated from IMP-5.23.1 - don't edit here)
- Sheet 8 formula cells (auto-calculated)
- Sheet 10 header rows

**Unprotected Cells (User Input):**

- Extended columns (R+) in Sheets 2-7
- Columns F-Q in all data sheets
- Sheet 9 evidence register
- Sheet 10 approval fields

**Workbook Password:** Optional (recommend if sharing externally)

---

## Integration Points

**Data Import (From IMP-5.23.1):**

- Import columns A-E for all services
- Maintain service order consistency
- Update quarterly (sync with inventory)

**Data Export (To Downstream Systems):**

- Sheet 8 Dashboard → IMP-5.23.5 (Compliance Dashboard)
- Sheet 9 Evidence → Audit repository
- Sheet 3 Contract Renewal Dates → Procurement calendar
- Sheet 7 TIA Results → Risk Register

**API Integration (Future Enhancement):**

- ITSM: Auto-import SLA performance (Sheet 4)
- Contract Management: Auto-populate contract data (Sheet 3)
- Monitoring: Real-time uptime % (Sheet 4)

---

## Python Generator Script Notes

**Script:** `generate_reg_a523_2_vendor_dd.py`

**Key Functions:**

- `create_styles()` - Define fonts, fills, borders
- `create_1_instructions()` - Sheet 1 setup
- `create_2_vendor_certs()` - Sheet 2 with dropdowns
- `create_3_contracts()` - Sheet 3 with validations
- `create_4_sla_performance()` - Sheet 4 with formulas
- `create_5_data_sovereignty()` - Sheet 5 with conditional formatting
- `create_6_audit_rights()` - Sheet 6 setup
- `create_7_jurisdictional_risk()` - Sheet 7 (CLOUD Act assessment)
- `create_8_dashboard()` - Sheet 8 with aggregation formulas
- `create_9_evidence_register()` - Sheet 9 with auto-numbering
- `create_10_approval()` - Sheet 10 workflow

**Customization Points:**

- Dropdown lists (modify vendor names, service types)
- Formula ranges (adjust for more/fewer rows)
- Conditional formatting rules (risk thresholds)
- Dashboard metrics (add custom KPIs)

**Usage:**
```bash
python3 generate_reg_a523_2_vendor_dd.py
# Output: ISMS-IMP-A.5.23.S2_VendorDD_20260120.xlsx
```

---

## Appendix: Complete Column Reference

**Full Column Matrix (All Sheets):**

See Part I, Section 4 for detailed column-by-column guidance.

**Quick Reference:**

- Sheets 2-7: Base columns A-Q + Extended columns R-AA
- Sheet 8: Dashboard (formulas)
- Sheet 9: Evidence register A-H
- Sheet 10: Approval workflow (custom layout)

**Total Workbook Columns:** 27 columns max (Sheet 7)

---

**END OF SPECIFICATION**

---

*"The worthwhile problems are the ones you can really solve or help solve, the ones you can really contribute something to."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
