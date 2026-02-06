**ISMS-IMP-A.5.14.4-TG - Compliance Monitoring Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.14

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.14.4-TG |
| **Document Type** | Implementation Guide |
| **Parent Policy** | ISMS-POL-A.5.14 (Information Transfer) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.14 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Information Security Officer |
| **Last Updated** | [Date to be set] |

**Related Documents:**
- ISMS-POL-A.5.14 (Information Transfer Policy)
- ISMS-IMP-A.5.14.1 (Transfer Rules and Procedures)
- ISMS-IMP-A.5.14.2 (Channel Security Assessment)
- ISMS-IMP-A.5.14.3 (Transfer Agreements Register)
- ISMS-POL-A.5.24-28 (Incident Management)

---

# Technical Specification

## 9. Workbook Technical Details

### 9.1 File Information

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.14.4 |
| **Generated Filename** | `ISMS-IMP-A.5.14.4_Compliance_Monitoring_Dashboard_YYYYMMDD.xlsx` |
| **Generator Script** | `generate_a514_4_compliance_monitoring_dashboard.py` |
| **Sheet Count** | 8 |
| **Primary Control** | A.5.14 (Information Transfer) |

### 9.2 Sheet Specifications

#### Sheet 1: Instructions
- **Type**: Read-only guidance
- **Row 1**: Title banner (merged A1:H1)
- **Rows 3-7**: Document metadata
- **Rows 9+**: Sheet descriptions, update frequencies
- **Column widths**: A=25, B=50, C-H=20

#### Sheet 2: Executive_Summary
- **Type**: Dashboard display
- **Row 1**: Section title (merged A1:J1)
- **Rows 3-4**: Reporting period
- **Rows 5-10**: Key metrics boxes (merged cells)
- **Rows 12+**: Channel compliance table, Risk summary, Key actions
- **Input fills**: Yellow for data entry cells
- **Column widths**: A=18, B=35, C-J=14

#### Sheet 3: Compliance_KPIs
- **Type**: KPI tracking
- **Row 1**: Section title (merged A1:I1)
- **Row 3**: Column headers (9 columns)
- **Rows 4+**: Pre-populated KPIs (12 entries)
- **Data validation**:
  - F4:F{n}: "On Target, At Risk, Below Target, Not Measured"
  - G4:G{n}: "↑ Improving, → Stable, ↓ Declining, New"
- **Input columns**: E, F, G, H, I - yellow fill
- **Column widths**: A=14, B=28, C=40, D=12, E=14, F=14, G=12, H=18, I=25

#### Sheet 4: Transfer_Incidents
- **Type**: Incident tracking
- **Row 1**: Section title (merged A1:L1)
- **Row 3**: Column headers (12 columns)
- **Rows 4-6**: Sample incident entries
- **Rows 7+**: Empty rows (12 rows)
- **Data validation**:
  - C4:C{n}: Channel type list
  - D4:D{n}: Incident type list
  - E4:E{n}: "Critical, High, Medium, Low"
  - F4:F{n}: Classification list
  - J4:J{n}: Status list
- **Input columns**: All except A - yellow fill
- **Column widths**: A=14, B=14, C=15, D=20, E=10, F=18, G=30, H=25, I=25, J=12, K=12, L=30

#### Sheet 5: Audit_Findings
- **Type**: Finding tracking
- **Row 1**: Section title (merged A1:K1)
- **Row 3**: Column headers (11 columns)
- **Rows 4-6**: Sample findings
- **Rows 7+**: Empty rows (12 rows)
- **Data validation**:
  - B4:B{n}: Audit type list
  - F4:F{n}: Severity list
  - J4:J{n}: Status list
- **Input columns**: C-K - yellow fill
- **Column widths**: A=14, B=16, C=12, D=35, E=18, F=12, G=30, H=18, I=12, J=14, K=30

#### Sheet 6: Remediation_Tracker
- **Type**: Remediation tracking
- **Row 1**: Section title (merged A1:J1)
- **Row 3**: Column headers (10 columns)
- **Rows 4-7**: Sample remediation items
- **Rows 8+**: Empty rows (11 rows)
- **Data validation**:
  - B4:B{n}: Source list
  - D4:D{n}: Priority list
  - I4:I{n}: Status list
- **Input columns**: D-J - yellow fill
- **Column widths**: A=12, B=18, C=35, D=10, E=35, F=18, G=12, H=12, I=14, J=30

#### Sheet 7: Evidence_Register
- **Type**: Evidence tracking
- **Row 1**: Section title (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4-8**: Sample evidence entries
- **Rows 9+**: Empty rows (10 rows)
- **Data validation**: H4:H{n}: "Pending, Collected, Verified, Expired, N/A"
- **Input columns**: E, F, G, H - yellow fill
- **Column widths**: A=18, B=18, C=35, D=20, E=30, F=15, G=18, H=12

#### Sheet 8: Approval_SignOff
- **Type**: Sign-off form
- **Row 1**: Section title (merged A1:F1)
- **Rows 3-7**: Document information
- **Rows 9+**: Approval signatures
- **Rows {n}+**: Distribution list
- **Data validation**: E column: "Pending, Approved, Rejected, Deferred"
- **Column widths**: A=25, B=25, C=22, D=15, E=15, F=30

### 9.3 Styling Specifications

| Style Element | Specification |
|--------------|---------------|
| Header Fill | Navy (#003366) |
| Subheader Fill | Blue (#4472C4) |
| Input Fill | Light Yellow (#FFFFCC) |
| Metric Fill | Light Blue (#D9E1F2) |
| Green Status | Green (#C6EFCE) |
| Yellow Status | Amber (#FFEB9C) |
| Red Status | Red (#FFC7CE) |
| Header Font | Calibri 14pt Bold White |
| Metric Font | Calibri 16pt Bold |
| Body Font | Calibri 11pt |

### 9.4 Data Validation Rules

| Field | Type | Values |
|-------|------|--------|
| KPI Status | List | On Target, At Risk, Below Target, Not Measured |
| KPI Trend | List | ↑ Improving, → Stable, ↓ Declining, New |
| Channel Type | List | Email, Cloud Storage, File Transfer, USB/Media, API, Physical, Verbal, Other |
| Incident Type | List | Data Leakage, Unauthorised Sharing, Lost Device, Interception, Policy Violation, Malware, Unauthorised Access, Other |
| Severity | List | Critical, High, Medium, Low |
| Incident Status | List | Open, Investigating, Remediation, Closed, Accepted |
| Audit Type | List | Internal Audit, ISO 27001 Audit, Penetration Test, Vulnerability Assessment, SOC 2 Audit, GDPR Audit, Customer Audit, Other |
| Finding Severity | List | Critical, High, Medium, Low, Observation |
| Finding Status | List | Open, In Progress, Remediated, Verified Closed, Risk Accepted, Overdue |
| Remediation Source | List | Channel Assessment, Audit Finding, Incident RCA, Risk Assessment, Management Review, Self-Assessment, Other |
| Remediation Priority | List | Critical, High, Medium, Low |
| Remediation Status | List | Not Started, Planning, In Progress, Testing, Completed, On Hold, Cancelled |

---

## 10. Integration Points

### 10.1 Data Sources

| Data | Source Workbook |
|------|-----------------|
| Channel compliance | A.5.14.2 (Channel Assessment) |
| Agreement status | A.5.14.3 (Agreements Register) |
| Transfer rules | A.5.14.1 (Transfer Rules) |
| Incidents | SIEM/Incident Management System |
| Audit findings | Audit Management System |

### 10.2 Data Flow

```
A.5.14.1 (Rules) ───────┐
                        │
A.5.14.2 (Channels) ────┼──► A.5.14.4 (This Dashboard)
                        │           │
A.5.14.3 (Agreements) ──┘           │
                                    ▼
                            A.5.14.5 (Consolidation)
```

---

## 11. Audit Considerations

### 11.1 Stage 1 Evidence
- Dashboard update schedule documented
- KPI definitions and methodology
- Incident classification criteria

### 11.2 Stage 2 Evidence
- 12 months of dashboard reports
- Incident investigation records
- Audit finding closure evidence
- Remediation completion proof

### 11.3 Common Auditor Questions
1. "Show me the trend of transfer security incidents."
2. "How are audit findings tracked to closure?"
3. "What is your mean time to resolve transfer incidents?"
4. "How do you measure transfer policy compliance?"

---

## 12. Generator Script Reference

**Script**: `generate_a514_4_compliance_monitoring_dashboard.py`

**Location**: `10-isms-scr-base/isms-a.5.14-information-transfer/10_generator-master/`

**Key Functions**:
- `create_instructions_sheet()`: Dashboard guidance
- `create_executive_summary_sheet()`: Management overview
- `create_compliance_kpis_sheet()`: KPI tracking
- `create_transfer_incidents_sheet()`: Incident register
- `create_audit_findings_sheet()`: Finding tracker
- `create_remediation_tracker_sheet()`: Gap remediation
- `create_evidence_register_sheet()`: Evidence management
- `create_approval_signoff_sheet()`: Monthly approval

**Execution**:
```bash
cd 10-isms-scr-base/isms-a.5.14-information-transfer/10_generator-master
python3 generate_a514_4_compliance_monitoring_dashboard.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"You can't manage what you can't measure."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
