**ISMS-IMP-A.5.17.4-TG - Compliance and Audit Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.17

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.17.4-TG |
| **Document Type** | Implementation Guide |
| **Parent Policy** | ISMS-POL-A.5.17 (Authentication Information) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.17 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Information Security Officer |
| **Last Updated** | [Date to be set] |

**Related Documents:**
- ISMS-POL-A.5.17 (Authentication Information Policy)
- ISMS-IMP-A.5.17.1 (Password Policy Implementation Guide)
- ISMS-IMP-A.5.17.2 (MFA Deployment Assessment)
- ISMS-IMP-A.5.17.3 (Authentication Management Procedures)
- ISMS-POL-A.5.24-28 (Incident Management)

---

# Technical Specification

## 9. Workbook Technical Details

### 9.1 File Information

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.17.4 |
| **Generated Filename** | `ISMS-IMP-A.5.17.4_Compliance_and_Audit_Dashboard_YYYYMMDD.xlsx` |
| **Generator Script** | `generate_a517_4_compliance_audit_dashboard.py` |
| **Sheet Count** | 8 |
| **Primary Control** | A.5.17 (Authentication Information) |

### 9.2 Sheet Specifications

#### Sheet 1: Instructions
- **Row 1**: Title banner (merged A1:H1)
- **Rows 3-6**: Document metadata
- **Rows 8+**: Sheet descriptions
- **Column widths**: A=25, B=50, C-H=20

#### Sheet 2: Executive_Summary
- **Row 1**: Title banner (merged A1:J1)
- **Rows 3-4**: Reporting period
- **Rows 5-10**: Key metric boxes (merged cells)
- **Rows 12+**: Compliance by area table, Key actions table
- **Column widths**: A=20, B=30, C-J=14

#### Sheet 3: Compliance_KPIs
- **Row 1**: Title banner (merged A1:I1)
- **Row 3**: Column headers (9 columns)
- **Rows 4+**: Pre-populated KPIs (12 entries)
- **Data validation**:
  - F4:F{n}: "On Target, At Risk, Below Target, Not Measured"
  - G4:G{n}: "↑ Improving, → Stable, ↓ Declining, New"
- **Column widths**: A=14, B=25, C=38, D=12, E=12, F=14, G=12, H=16, I=22

#### Sheet 4: Authentication_Events
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: Event categories (14 pre-populated)
- **Data validation**:
  - F4:F{n}: "Normal, Warning, Alert, Critical"
  - G4:G{n}: "None Required, In Progress, Completed, Escalated"
- **Column widths**: A=28, B=14, C=16, D=12, E=22, F=14, G=14, H=25

#### Sheet 5: Audit_Findings
- **Row 1**: Title banner (merged A1:K1)
- **Row 3**: Column headers (11 columns)
- **Rows 4+**: Empty rows for entries (15 rows)
- **Data validation**:
  - B4:B{n}: Audit type list
  - F4:F{n}: "Critical, High, Medium, Low, Observation"
  - J4:J{n}: Status list
- **Column widths**: A=12, B=14, C=12, D=32, E=18, F=10, G=28, H=16, I=12, J=12, K=22

#### Sheet 6: Remediation_Tracker
- **Row 1**: Title banner (merged A1:J1)
- **Row 3**: Column headers (10 columns)
- **Rows 4+**: Empty rows for entries (15 rows)
- **Data validation**:
  - B4:B{n}: Source list
  - D4:D{n}: Priority list
  - I4:I{n}: Status list
- **Column widths**: A=12, B=16, C=32, D=10, E=32, F=16, G=12, H=12, I=12, J=25

#### Sheet 7: Evidence_Register
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4-8**: Pre-populated entries
- **Rows 9+**: Empty rows (10 rows)
- **Data validation**: H4:H{n}: "Pending, Collected, Verified, Expired, N/A"
- **Column widths**: A=16, B=16, C=32, D=20, E=28, F=12, G=16, H=12

#### Sheet 8: Approval_SignOff
- **Row 1**: Title banner (merged A1:F1)
- **Rows 3-6**: Document information
- **Rows 8+**: Approval signatures
- **Data validation**: E column: "Pending, Approved, Rejected, Deferred"
- **Column widths**: A=25, B=22, C=18, D=14, E=14, F=28

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

---

## 10. Integration Points

### 10.1 Data Sources

| Data | Source |
|------|--------|
| Password compliance | A.5.17.1 assessment |
| MFA adoption | A.5.17.2 assessment |
| Process compliance | A.5.17.3 assessment |
| Authentication events | SIEM, Identity Provider |
| Audit findings | Audit management system |

### 10.2 Data Flow

```
A.5.17.1 (Password Policy) ─────┐
                                │
A.5.17.2 (MFA Deployment) ──────┼──► A.5.17.4 (This Dashboard)
                                │           │
A.5.17.3 (Auth Management) ─────┘           │
                                            ▼
                                    A.5.17.5 (Consolidation)
```

---

## 11. Generator Script Reference

**Script**: `generate_a517_4_compliance_audit_dashboard.py`

**Location**: `10-isms-scr-base/isms-a.5.17-authentication-information/10_generator-master/`

**Key Functions**:
- `create_instructions_sheet()`: Dashboard guidance
- `create_executive_summary_sheet()`: Management overview
- `create_compliance_kpis_sheet()`: KPI tracking
- `create_authentication_events_sheet()`: Event monitoring
- `create_audit_findings_sheet()`: Finding tracker
- `create_remediation_tracker_sheet()`: Gap remediation
- `create_evidence_register_sheet()`: Evidence management
- `create_approval_signoff_sheet()`: Monthly approval

**Execution**:
```bash
cd 10-isms-scr-base/isms-a.5.17-authentication-information/10_generator-master
python3 generate_a517_4_compliance_audit_dashboard.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"The only secure password is one you can't remember."*
— Troy Hunt

<!-- QA_VERIFIED: 2026-02-06 -->
