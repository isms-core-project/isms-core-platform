**ISMS-IMP-A.5.17.5-TG - Consolidation Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.17

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.17.5-TG |
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
- ISMS-IMP-A.5.17.4 (Compliance and Audit Dashboard)

---

# Technical Specification

## 9. Workbook Technical Details

### 9.1 File Information

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.17.5 |
| **Generated Filename** | `ISMS-IMP-A.5.17.5_Consolidation_Dashboard_YYYYMMDD.xlsx` |
| **Generator Script** | `generate_a517_5_consolidation_dashboard.py` |
| **Sheet Count** | 12 |
| **Primary Control** | A.5.17 (Authentication Information) |

### 9.2 Sheet Specifications

#### Sheet 1: Instructions
- **Content**: Purpose, methodology, scoring
- **Column width**: A=90

#### Sheet 2: Executive_Summary
- **Row 1**: Title banner (merged A1:H1)
- **Rows 3-5**: Reporting period
- **Rows 6-11**: Domain compliance table
- **Rows 13+**: Key metrics table
- **Column widths**: A=35, B=35, C=18, D=12, E=15, F=15

#### Sheet 3: Domain_Overview
- **Row 1**: Title banner (merged A1:F1)
- **Sections**: Three domain sections with headers
- **Column widths**: A=40, B=18, C=15, D=35, E=35

#### Sheet 4: Policy_Compliance
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: Policy element entries
- **Column widths**: A=22, B=30, C=20, D=15, E=15, F=18, G=30, H=18

#### Sheet 5: Lifecycle_Compliance
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: Lifecycle phase entries
- **Column widths**: A=28, B=18, C=18, D=15, E=15, F=18, G=30, H=18

#### Sheet 6: System_Compliance
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: System entries
- **Column widths**: A=25, B=18, C=15, D=18, E=15, F=18, G=30, H=18

#### Sheet 7: Cross_Domain_Gaps
- **Row 1**: Title banner (merged A1:J1)
- **Row 3**: Column headers (10 columns)
- **Rows 4+**: Gap entries (15 rows)
- **Column widths**: A=10, B=22, C=40, D=12, E=10, F=18, G=30, H=35, I=18, J=15

#### Sheet 8: Remediation_Tracker
- **Row 1**: Title banner (merged A1:K1)
- **Row 3**: Column headers (11 columns)
- **Rows 4+**: Action entries (15 rows)
- **Column widths**: A=10, B=12, C=20, D=40, E=10, F=18, G=12, H=12, I=12, J=10, K=30

#### Sheet 9: KPI_Summary
- **Row 1**: Title banner (merged A1:F1)
- **Row 3**: Column headers (6 columns)
- **Rows 4+**: KPI entries
- **Column widths**: A=42, B=15, C=12, D=12, E=10, F=15

#### Sheet 10: Evidence_Index
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: Evidence entries (15 rows)
- **Column widths**: A=12, B=25, C=22, D=18, E=40, F=30, G=15, H=18

#### Sheet 11: Trend_Dashboard
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: Period entries (8 quarters)
- **Column widths**: A=12, B=12, C=14, D=12, E=12, F=14, G=12, H=35

#### Sheet 12: Approval_SignOff
- **Row 1**: Title banner (merged A1:E1)
- **Rows 3-5**: Document information
- **Rows 6+**: Approval table
- **Column widths**: A=30, B=25, C=15, D=20, E=40

### 9.3 Styling Specifications

| Style Element | Specification |
|--------------|---------------|
| Title Fill | Dark Navy (#002060) |
| Header Fill | Navy (#1F4E79) |
| Section Font | Blue Bold (#1F4E79) |
| Input Fill | Light Yellow (#FFFFCC) |
| Border | Thin black all sides |

---

## 10. Integration Points

### 10.1 Source Workbook Dependencies

| Source | Data Pulled |
|--------|-------------|
| A.5.17.1 | Password policy compliance |
| A.5.17.2 | MFA adoption, lifecycle compliance |
| A.5.17.3 | System assessment results |
| A.5.17.4 | KPIs, incidents, remediation |

### 10.2 Data Flow

```
A.5.17.1 (Password Policy) ─────┐
                                │
A.5.17.2 (MFA/Lifecycle) ───────┼──► A.5.17.5 (This Consolidation)
                                │           │
A.5.17.3 (System Assessment) ───┤           │
                                │           ▼
A.5.17.4 (Compliance) ──────────┘    Executive Reports
                                     Audit Evidence
                                     Management Review
```

---

## 11. Generator Script Reference

**Script**: `generate_a517_5_consolidation_dashboard.py`

**Location**: `10-isms-scr-base/isms-a.5.17-authentication-information/10_generator-master/`

**Key Functions**:
- `create_instructions_sheet()`: Methodology guidance
- `create_executive_summary_sheet()`: Management overview
- `create_domain_overview_sheet()`: Domain breakdown
- `create_policy_compliance_sheet()`: Policy element compliance
- `create_lifecycle_compliance_sheet()`: Lifecycle process compliance
- `create_system_compliance_sheet()`: System authentication
- `create_cross_domain_gaps_sheet()`: Gap analysis
- `create_remediation_tracker_sheet()`: Action tracking
- `create_kpi_summary_sheet()`: KPI consolidation
- `create_evidence_index_sheet()`: Evidence cross-reference
- `create_trend_dashboard_sheet()`: Historical trends
- `create_approval_signoff_sheet()`: Executive approval

**Execution**:
```bash
cd 10-isms-scr-base/isms-a.5.17-authentication-information/10_generator-master
python3 generate_a517_5_consolidation_dashboard.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"Identity is the new perimeter."*
— John Kindervag

<!-- QA_VERIFIED: 2026-02-06 -->
