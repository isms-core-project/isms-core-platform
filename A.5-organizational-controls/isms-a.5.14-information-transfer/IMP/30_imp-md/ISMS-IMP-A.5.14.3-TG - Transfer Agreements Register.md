**ISMS-IMP-A.5.14.3-TG - Transfer Agreements Register**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.14

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.14.3-TG |
| **Document Type** | Implementation Guide |
| **Parent Policy** | ISMS-POL-A.5.14 (Information Transfer) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.14 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Information Security Officer |
| **Last Updated** | [Date to be set] |

**Related Documents:**
- ISMS-POL-A.5.14 (Information Transfer Policy)
- ISMS-POL-A.6.6 (Confidentiality and Non-Disclosure Agreements)
- ISMS-POL-A.5.19-23 (Supplier Relationships)
- ISMS-IMP-A.5.14.1 (Transfer Rules and Procedures)
- Legal/Procurement Contract Templates

---

# Technical Specification

## 9. Workbook Technical Details

### 9.1 File Information

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.14.3 |
| **Generated Filename** | `ISMS-IMP-A.5.14.3_Transfer_Agreements_Register_YYYYMMDD.xlsx` |
| **Generator Script** | `generate_a514_3_transfer_agreements_register.py` |
| **Sheet Count** | 7 |
| **Primary Control** | A.5.14 (Information Transfer) |

### 9.2 Sheet Specifications

#### Sheet 1: Instructions
- **Type**: Read-only guidance
- **Row 1**: Title banner (merged A1:H1)
- **Rows 3-7**: Document metadata
- **Rows 9+**: Sheet descriptions, agreement type definitions
- **Column widths**: A=35, B=55, C-H=20

#### Sheet 2: Agreement_Register
- **Type**: Master register
- **Row 1**: Section title (merged A1:L1)
- **Row 3**: Column headers (12 columns)
- **Rows 4-8**: Sample agreement entries
- **Rows 9+**: Empty rows for additional entries (15 rows)
- **Data validation**:
  - B4:B{n}: "DSA, ISA, MOU, DPA, SCC, NDA, Other"
  - E4:E{n}: "PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED"
  - F4:F{n}: "Inbound, Outbound, Bi-directional"
  - K4:K{n}: "Draft, Under Review, Active, Expiring Soon, Expired, Terminated"
- **Input columns**: G-L - yellow fill
- **Column widths**: A=14, B=16, C=22, D=30, E=18, F=16, G-I=14, J=18, K=14, L=25

#### Sheet 3: Agreement_Requirements
- **Type**: Requirements reference
- **Row 1**: Section title (merged A1:G1)
- **Row 3**: Column headers (7 columns)
- **Rows 4+**: Pre-populated requirements (18 entries)
- **Input column**: G (Notes) - yellow fill
- **Column widths**: A=20, B=40, C=18, D=30, E=20, F=18, G=25

#### Sheet 4: Third_Party_Assessment
- **Type**: Assessment tracking
- **Row 1**: Section title (merged A1:J1)
- **Row 3**: Column headers (10 columns)
- **Rows 4-8**: Sample third-party entries
- **Rows 9+**: Empty rows for additional entries (10 rows)
- **Data validation**:
  - D4:D{n}: "Yes, No, In Progress, N/A"
  - E4:E{n}: "Type I, Type II, Not Available, N/A"
  - F4:F{n}: "Completed, Pending, Not Required"
  - G4:G{n}: "Current (<12mo), Expired, Not Available, N/A"
  - H4:H{n}: "Low, Medium, High, Critical"
- **Input columns**: C-J - yellow fill
- **Column widths**: A=22, B=14, C=16, D=18, E=15, F=20, G=18, H=14, I=16, J=25

#### Sheet 5: Review_Schedule
- **Type**: Review tracking
- **Row 1**: Section title (merged A1:I1)
- **Row 3**: Column headers (9 columns)
- **Rows 4-8**: Sample review entries
- **Rows 9+**: Empty rows (10 rows)
- **Data validation**:
  - E4:E{n}: "Annual, Semi-Annual, Quarterly, Ad-hoc, Renewal"
  - G4:G{n}: "Scheduled, In Progress, Completed, Overdue"
  - H4:H{n}: "None, Update Clauses, Renegotiate, Terminate, Renew"
- **Input columns**: C-I - yellow fill
- **Column widths**: A=14, B=22, C=16, D=16, E=14, F=20, G=14, H=18, I=30

#### Sheet 6: Evidence_Register
- **Type**: Evidence tracking
- **Row 1**: Section title (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4-8**: Sample evidence entries
- **Rows 9+**: Empty rows (10 rows)
- **Data validation**:
  - H4:H{n}: "Pending, Collected, Verified, Expired, N/A"
  - B4:B{n}: Evidence type dropdown
- **Input columns**: E, F, G, H - yellow fill
- **Column widths**: A=18, B=20, C=35, D=18, E=30, F=15, G=18, H=12

#### Sheet 7: Approval_SignOff
- **Type**: Sign-off form
- **Row 1**: Section title (merged A1:F1)
- **Rows 3-6**: Document information
- **Rows 8-13**: Register summary metrics
- **Rows 15+**: Approval signatures
- **Data validation**: E column: "Pending, Approved, Rejected, Deferred"
- **Column widths**: A=28, B=25, C=20, D=15, E=15, F=30

### 9.3 Styling Specifications

| Style Element | Specification |
|--------------|---------------|
| Header Fill | Navy (#003366) |
| Subheader Fill | Blue (#4472C4) |
| Input Fill | Light Yellow (#FFFFCC) |
| Active Fill | Green (#C6EFCE) |
| Expiring Fill | Amber (#FFEB9C) |
| Expired Fill | Red (#FFC7CE) |
| Header Font | Calibri 14pt Bold White |
| Body Font | Calibri 11pt |
| Border | Thin black all sides |

### 9.4 Data Validation Rules

| Field | Type | Values |
|-------|------|--------|
| Agreement Type | List | DSA, ISA, MOU, DPA, SCC, NDA, Other |
| Data Classification | List | PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED |
| Transfer Direction | List | Inbound, Outbound, Bi-directional |
| Agreement Status | List | Draft, Under Review, Active, Expiring Soon, Expired, Terminated |
| ISO Certification | List | Yes, No, In Progress, N/A |
| SOC Report | List | Type I, Type II, Not Available, N/A |
| Risk Rating | List | Low, Medium, High, Critical |
| Review Status | List | Scheduled, In Progress, Completed, Overdue |
| Review Action | List | None, Update Clauses, Renegotiate, Terminate, Renew |

---

## 10. Integration Points

### 10.1 Related Controls

| Control | Integration |
|---------|-------------|
| A.5.19-23 | Supplier relationship management informs agreement needs |
| A.6.6 | NDA policy provides standard confidentiality terms |
| A.5.14.1 | Transfer rules define what agreements must contain |
| A.5.14.4 | Monitoring tracks agreement compliance |

### 10.2 Data Flow

```
A.5.19-23 (Suppliers) ────► A.5.14.3 (This Register)
    │                             │
    │  Supplier list              │  Agreement inventory
    │  informs register           │  feeds monitoring
    │                             ▼
A.6.6 (NDAs) ─────────────► A.5.14.4 (Monitoring)
    │                             │
    │  NDA terms inform           │
    │  agreement clauses          │
    │                             ▼
    └─────────────────────► A.5.14.5 (Consolidation)
```

---

## 11. Audit Considerations

### 11.1 Stage 1 Evidence
- Agreement register maintained
- Standard requirements documented
- Review schedule established

### 11.2 Stage 2 Evidence
- Signed agreements for all active relationships
- Third-party security assessments current
- Review records demonstrating ongoing management
- Evidence of agreement compliance

### 11.3 Common Auditor Questions
1. "Show me the agreement governing data transfers with [supplier]."
2. "How do you ensure third parties meet security requirements?"
3. "What happens when an agreement expires?"
4. "How are agreement changes managed?"

---

## 12. Generator Script Reference

**Script**: `generate_a514_3_transfer_agreements_register.py`

**Location**: `10-isms-scr-base/isms-a.5.14-information-transfer/10_generator-master/`

**Key Functions**:
- `create_instructions_sheet()`: Overview and definitions
- `create_agreement_register_sheet()`: Master agreement list
- `create_agreement_requirements_sheet()`: Standard clauses
- `create_third_party_assessment_sheet()`: Partner security
- `create_review_schedule_sheet()`: Review tracking
- `create_evidence_register_sheet()`: Evidence management
- `create_approval_signoff_sheet()`: Register approval

**Execution**:
```bash
cd 10-isms-scr-base/isms-a.5.14-information-transfer/10_generator-master
python3 generate_a514_3_transfer_agreements_register.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"A verbal contract isn't worth the paper it's written on."*
— Samuel Goldwyn

<!-- QA_VERIFIED: 2026-02-06 -->
