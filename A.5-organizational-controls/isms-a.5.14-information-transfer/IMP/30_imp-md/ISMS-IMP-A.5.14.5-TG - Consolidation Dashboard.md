**ISMS-IMP-A.5.14.5-TG - Consolidation Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.14

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.14.5-TG |
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
- ISMS-IMP-A.5.14.4 (Compliance Monitoring Dashboard)

---

# Technical Specification

## 9. Workbook Technical Details

### 9.1 File Information

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.14.5 |
| **Generated Filename** | `ISMS-IMP-A.5.14.5_Consolidation_Dashboard_YYYYMMDD.xlsx` |
| **Generator Script** | `generate_a514_5_consolidation_dashboard.py` |
| **Sheet Count** | 12 |
| **Primary Control** | A.5.14 (Information Transfer) |

### 9.2 Sheet Specifications

#### Sheet 1: Instructions
- **Type**: Read-only guidance
- **Content**: Purpose, methodology, scoring
- **Column width**: A=90

#### Sheet 2: Executive_Summary
- **Type**: Summary display
- **Row 1**: Title banner (merged A1:H1)
- **Rows 3-5**: Reporting period
- **Rows 6-11**: Domain compliance table
- **Rows 13+**: Key metrics table
- **Column widths**: A=35, B=35, C=18, D=12, E=15, F=15

#### Sheet 3: Domain_Overview
- **Type**: Detailed breakdown
- **Row 1**: Title banner (merged A1:F1)
- **Sections**: Three domain sections with headers
- **Data validation**: Status dropdown
- **Column widths**: A=40, B=18, C=15, D=35, E=35

#### Sheet 4: Transfer_Compliance
- **Type**: Compliance matrix
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: Transfer method entries
- **Column widths**: A=22, B=16, C=18, D=18, E=16, F=18, G=30, H=18

#### Sheet 5: Channel_Compliance
- **Type**: Compliance matrix
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: Channel entries
- **Column widths**: A=22, B=22, C=16, D=15, E=12, F=18, G=30, H=18

#### Sheet 6: Agreements_Compliance
- **Type**: Compliance matrix
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: Third-party entries
- **Column widths**: A=25, B=20, C=18, D=15, E=15, F=18, G=30, H=18

#### Sheet 7: Cross_Domain_Gaps
- **Type**: Gap tracking
- **Row 1**: Title banner (merged A1:J1)
- **Row 3**: Column headers (10 columns)
- **Rows 4+**: Gap entries (15 rows)
- **Data validation**: Risk, Priority dropdowns
- **Column widths**: A=10, B=22, C=40, D=12, E=10, F=18, G=30, H=35, I=18, J=15

#### Sheet 8: Remediation_Tracker
- **Type**: Action tracking
- **Row 1**: Title banner (merged A1:K1)
- **Row 3**: Column headers (11 columns)
- **Rows 4+**: Action entries (15 rows)
- **Data validation**: Priority, Status dropdowns
- **Column widths**: A=10, B=12, C=20, D=40, E=10, F=18, G=12, H=12, I=12, J=10, K=30

#### Sheet 9: KPI_Summary
- **Type**: KPI display
- **Row 1**: Title banner (merged A1:F1)
- **Row 3**: Column headers (6 columns)
- **Rows 4+**: KPI entries
- **Column widths**: A=42, B=15, C=12, D=12, E=10, F=15

#### Sheet 10: Evidence_Index
- **Type**: Evidence reference
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: Evidence entries (15 rows)
- **Column widths**: A=12, B=25, C=22, D=18, E=40, F=30, G=15, H=18

#### Sheet 11: Trend_Dashboard
- **Type**: Historical data
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: Period entries (8 quarters)
- **Column widths**: A=12, B=16, C=14, D=14, E=12, F=12, G=18, H=35

#### Sheet 12: Approval_SignOff
- **Type**: Sign-off form
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
| Compliant Fill | Green (#C6EFCE) |
| Partial Fill | Amber (#FFEB9C) |
| Non-Compliant Fill | Red (#FFC7CE) |
| Title Font | Calibri 16pt Bold White |
| Header Font | Calibri 11pt Bold White |
| Body Font | Calibri 11pt |

### 9.4 Data Validation Rules

| Field | Type | Values |
|-------|------|--------|
| Compliance Status | List | Compliant, Partial, Non-Compliant, N/A |
| Risk Rating | List | Low, Medium, High, Critical |
| Priority | List | Critical, High, Medium, Low |
| Remediation Status | List | Not Started, Planning, In Progress, Testing, Completed, On Hold |
| KPI Trend | List | ↑, →, ↓ |
| Evidence Status | List | Pending, Collected, Verified, Expired |

---

## 10. Integration Points

### 10.1 Source Workbook Dependencies

| Source | Data Pulled |
|--------|-------------|
| A.5.14.1 | Transfer method policies, compliance status |
| A.5.14.2 | Channel assessments, security ratings |
| A.5.14.3 | Agreement status, third-party assessments |
| A.5.14.4 | KPIs, incidents, audit findings, remediation |

### 10.2 Data Flow

```
A.5.14.1 (Rules) ──────┐
                       │
A.5.14.2 (Channels) ───┼──► A.5.14.5 (This Consolidation)
                       │         │
A.5.14.3 (Agreements) ─┤         │
                       │         ▼
A.5.14.4 (Monitoring) ─┘    Executive Reports
                            Audit Evidence
                            Management Review
```

---

## 11. Audit Considerations

### 11.1 Stage 1 Evidence
- Consolidation methodology documented
- Source workbook availability
- Consolidation schedule established

### 11.2 Stage 2 Evidence
- 4 quarters of consolidated dashboards
- Trend analysis showing improvement
- Cross-domain gap remediation evidence
- Management review meeting minutes

### 11.3 Common Auditor Questions
1. "Show me how compliance has changed over the past year."
2. "How do you identify gaps that span multiple control areas?"
3. "What is your process for executive reporting on transfer security?"
4. "How does this consolidation support management review?"

---

## 12. Generator Script Reference

**Script**: `generate_a514_5_consolidation_dashboard.py`

**Location**: `10-isms-scr-base/isms-a.5.14-information-transfer/10_generator-master/`

**Key Functions**:
- `create_instructions_sheet()`: Methodology guidance
- `create_executive_summary_sheet()`: Management overview
- `create_domain_overview_sheet()`: Domain breakdown
- `create_transfer_compliance_sheet()`: Method compliance
- `create_channel_compliance_sheet()`: Channel status
- `create_agreements_compliance_sheet()`: Agreement status
- `create_cross_domain_gaps_sheet()`: Gap analysis
- `create_remediation_tracker_sheet()`: Action tracking
- `create_kpi_summary_sheet()`: KPI consolidation
- `create_evidence_index_sheet()`: Evidence cross-reference
- `create_trend_dashboard_sheet()`: Historical trends
- `create_approval_signoff_sheet()`: Executive approval

**Execution**:
```bash
cd 10-isms-scr-base/isms-a.5.14-information-transfer/10_generator-master
python3 generate_a514_5_consolidation_dashboard.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"The whole is greater than the sum of its parts."*
— Aristotle

<!-- QA_VERIFIED: 2026-02-06 -->
