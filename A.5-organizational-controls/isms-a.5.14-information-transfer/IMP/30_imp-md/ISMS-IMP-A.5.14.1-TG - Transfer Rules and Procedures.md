**ISMS-IMP-A.5.14.1-TG - Transfer Rules and Procedures**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.14

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.14.1-TG |
| **Document Type** | Implementation Guide |
| **Parent Policy** | ISMS-POL-A.5.14 (Information Transfer) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.14 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Information Security Officer |
| **Last Updated** | [Date to be set] |

**Related Documents:**
- ISMS-POL-A.5.14 (Information Transfer Policy)
- ISMS-IMP-A.5.14.2 (Channel Security Assessment)
- ISMS-IMP-A.5.14.3 (Transfer Agreements Register)
- ISMS-POL-A.5.12-13 (Information Classification and Labelling)
- ISMS-POL-A.8.24 (Use of Cryptography)

---

# Technical Specification

## 9. Workbook Technical Details

### 9.1 File Information

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.14.1 |
| **Generated Filename** | `ISMS-IMP-A.5.14.1_Transfer_Rules_and_Procedures_YYYYMMDD.xlsx` |
| **Generator Script** | `generate_a514_1_transfer_rules_procedures.py` |
| **Sheet Count** | 8 |
| **Primary Control** | A.5.14 (Information Transfer) |

### 9.2 Sheet Specifications

#### Sheet 1: Instructions
- **Type**: Read-only guidance
- **Row 1**: Title banner (merged A1:H1)
- **Rows 3-7**: Document metadata
- **Rows 9+**: Sheet descriptions, colour legend
- **Column widths**: A=25, B=60, C-H=20

#### Sheet 2: Transfer_Policy
- **Type**: Data entry
- **Row 1**: Section title (merged A1:F1)
- **Row 3**: Column headers
- **Rows 4+**: Policy element entries
- **Data validation**: Status dropdown (Draft, Under Review, Approved, Needs Update)
- **Input columns**: D (Owner), F (Status) - yellow fill
- **Column widths**: A=30, B=50, C=15, D=25, E=18, F=15

#### Sheet 3: Transfer_Methods
- **Type**: Matrix entry
- **Row 1**: Section title (merged A1:H1)
- **Row 3**: Column headers with classification colours
- **Rows 4+**: Transfer method entries
- **Data validation**:
  - B4:E{n}: "Allowed, Conditional, Not Allowed"
  - G4:G{n}: "Yes, No, Varies, Technical Review"
- **Conditional formatting**: Allowed=green, Conditional=amber, Not Allowed=red
- **Column widths**: A=30, B-E=12, F=30, G=18, H=30

#### Sheet 4: Electronic_Transfer
- **Type**: Data entry
- **Row 1**: Section title (merged A1:H1)
- **Row 3**: Column headers
- **Rows 4+**: Channel entries with pre-populated examples
- **Data validation**:
  - F4:F{n}: "PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED"
  - G4:G{n}: "Yes, No, Manual, Custom, N/A"
- **Input column**: H (Notes) - yellow fill
- **Column widths**: A=28, B=30, C=25, D=22, E=20, F=18, G=15, H=30

#### Sheet 5: Physical_Transfer
- **Type**: Data entry
- **Row 1**: Section title (merged A1:H1)
- **Row 3**: Column headers
- **Rows 4+**: Transfer type entries
- **Data validation**: F4:F{n}: "PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED"
- **Input column**: H (Notes) - yellow fill
- **Column widths**: A=25, B=28, C=30, D=25, E=28, F=18, G=25, H=30

#### Sheet 6: Verbal_Transfer
- **Type**: Data entry
- **Row 1**: Section title (merged A1:G1)
- **Row 3**: Column headers
- **Rows 4+**: Communication type entries
- **Data validation**: E4:E{n}: "PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED"
- **Input column**: G (Notes) - yellow fill
- **Column widths**: A=30, B=35, C=28, D=28, E=18, F=28, G=30

#### Sheet 7: Evidence_Register
- **Type**: Data entry
- **Row 1**: Section title (merged A1:H1)
- **Row 3**: Column headers
- **Rows 4-8**: Pre-populated evidence entries
- **Rows 9+**: Empty rows for additional entries
- **Data validation**:
  - H4:H{n}: "Pending, Collected, Verified, Expired, N/A"
  - B4:B{n}: Evidence type dropdown
- **Input columns**: E, F, G, H - yellow fill
- **Column widths**: A=15, B=20, C=35, D=20, E=30, F=15, G=18, H=12

#### Sheet 8: Approval_SignOff
- **Type**: Sign-off form
- **Row 1**: Section title (merged A1:F1)
- **Rows 3-6**: Document information
- **Rows 8+**: Approval signature table
- **Rows {n}+**: Version history table
- **Data validation**: Status column: "Pending, Approved, Rejected, Deferred"
- **Input columns**: B-F in approval rows - yellow fill
- **Column widths**: A=25, B=25, C=20, D=15, E=15, F=30

### 9.3 Styling Specifications

| Style Element | Specification |
|--------------|---------------|
| Header Fill | Navy (#003366) |
| Subheader Fill | Blue (#4472C4) |
| Input Fill | Light Yellow (#FFFFCC) |
| Locked Fill | Light Grey (#F2F2F2) |
| PUBLIC colour | Light Blue (#74C0FC) |
| INTERNAL colour | Light Green (#69DB7C) |
| CONFIDENTIAL colour | Orange (#FFA94D) |
| RESTRICTED colour | Red (#FF6B6B) |
| Allowed colour | Green (#C6EFCE) |
| Conditional colour | Amber (#FFEB9C) |
| Not Allowed colour | Red (#FFC7CE) |
| Header Font | Calibri 14pt Bold White |
| Body Font | Calibri 11pt |
| Border | Thin black all sides |

### 9.4 Data Validation Rules

| Field | Type | Values |
|-------|------|--------|
| Policy Status | List | Draft, Under Review, Approved, Needs Update |
| Transfer Permission | List | Allowed, Conditional, Not Allowed |
| Approval Required | List | Yes, No, Varies, Technical Review |
| Max Classification | List | PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED |
| DLP Integration | List | Yes, No, Manual, Custom, N/A |
| Evidence Status | List | Pending, Collected, Verified, Expired, N/A |
| Approval Status | List | Pending, Approved, Rejected, Deferred |

---

## 10. Integration Points

### 10.1 Stacked Control Dependencies

| Control | Integration |
|---------|-------------|
| A.5.12-13 | Classification levels from this control determine transfer method permissions |
| A.8.24 | Encryption requirements referenced in Electronic_Transfer sheet |
| A.8.12 | DLP integration status aligns with Data Leakage Prevention control |
| A.8.15 | Logging requirements support this control's audit trail needs |

### 10.2 Data Flow to Other A.5.14 Workbooks

```
A.5.14.1 (Transfer Rules) ──► A.5.14.2 (Channel Assessment)
    │                              │
    │  Rules define what          │  Assessment verifies
    │  channels must support      │  channels meet rules
    │                              │
    └──────────────────────────────┼──► A.5.14.5 (Consolidation)
                                   │
A.5.14.3 (Agreements) ─────────────┘
    │
    │  Agreements reference
    │  transfer rules for
    │  third parties
    │
A.5.14.4 (Monitoring) ─────────────────► A.5.14.5
    │
    │  Incidents tracked against
    │  rule violations
```

---

## 11. Audit Considerations

### 11.1 Stage 1 Evidence (Documentation Review)
- Completed Transfer_Policy sheet showing all mandatory elements
- Transfer_Methods matrix with clear permissions per classification
- Evidence_Register with policy document references

### 11.2 Stage 2 Evidence (Operational Effectiveness)
- Sample transfer audit logs (30-day period)
- DLP incident reports showing policy enforcement
- User awareness training completion records
- Chain of custody documentation samples

### 11.3 Common Auditor Questions
1. "How do you ensure CONFIDENTIAL data isn't sent via unauthorised channels?"
2. "What happens if someone needs to transfer RESTRICTED information urgently?"
3. "How are third-party transfer requirements communicated to external partners?"
4. "Show me evidence that users are trained on these transfer rules."

---

## 12. Generator Script Reference

**Script**: `generate_a514_1_transfer_rules_procedures.py`

**Location**: `10-isms-scr-base/isms-a.5.14-information-transfer/10_generator-master/`

**Key Functions**:
- `create_instructions_sheet()`: Instructions and colour legend
- `create_transfer_policy_sheet()`: Policy element documentation
- `create_transfer_methods_sheet()`: Classification-method matrix
- `create_electronic_transfer_sheet()`: Electronic channel rules
- `create_physical_transfer_sheet()`: Physical transfer procedures
- `create_verbal_transfer_sheet()`: Verbal communication protocols
- `create_evidence_register_sheet()`: Evidence tracking
- `create_approval_signoff_sheet()`: Sign-off and version history

**Execution**:
```bash
cd 10-isms-scr-base/isms-a.5.14-information-transfer/10_generator-master
python3 generate_a514_1_transfer_rules_procedures.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"The single biggest problem in communication is the illusion that it has taken place."*
— George Bernard Shaw

<!-- QA_VERIFIED: 2026-02-06 -->
