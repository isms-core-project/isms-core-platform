# ISMS-IMP-A.5.14.3 — Transfer Agreements Register

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.14.3 |
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

# PART I: USER COMPLETION GUIDE

## 1. Assessment Overview

### 1.1 Purpose

The **Transfer Agreements Register Workbook** (ISMS-IMP-A.5.14.3) maintains a comprehensive record of all information transfer agreements with third parties. This register tracks data sharing agreements, interconnection security agreements (ISAs), memoranda of understanding (MOUs), data processing agreements (DPAs), and other contractual arrangements governing information exchange.

### 1.2 Scope

This register covers:
- **Agreement inventory**: Master list of all transfer agreements
- **Standard requirements**: Security clauses required in agreements
- **Third-party assessments**: Security posture of transfer partners
- **Review schedule**: Agreement renewal and review tracking
- **Compliance evidence**: Documentation supporting agreement management

### 1.3 Business Value

Maintaining this register delivers:
- **Complete visibility** into third-party transfer relationships
- **Contractual compliance** through documented requirements
- **Risk mitigation** via security assessments of partners
- **Audit readiness** with centralised agreement tracking
- **Renewal management** preventing agreement lapses

### 1.4 Control Requirement

> *ISO/IEC 27001:2022 Annex A.5.14 — Information Transfer*
>
> "Information transfer rules, procedures, or agreements should be in place for all types of transfer facilities within the organization and between the organization and other parties."

This register specifically addresses the "agreements" component for transfers with external parties.

---

## 2. Prerequisites

Before starting this assessment, ensure you have:

### 2.1 Required Documents
- [ ] ISMS-POL-A.5.14 (Information Transfer Policy)
- [ ] ISMS-POL-A.6.6 (NDA Policy) — standard NDA terms
- [ ] Legal contract templates (DPA, SCC, ISA)
- [ ] Vendor/supplier list
- [ ] Existing agreement inventory (if any)
- [ ] Data flow documentation showing external transfers

### 2.2 Required Access
- [ ] Contract management system
- [ ] Vendor management database
- [ ] Legal document repository
- [ ] Third-party risk management system
- [ ] Procurement records

### 2.3 Required Personnel
- [ ] Legal Counsel / Contract Manager
- [ ] Procurement/Vendor Manager
- [ ] Data Protection Officer
- [ ] Information Security Officer
- [ ] Business Relationship Owners

---

## 3. Workbook Structure

The workbook contains **7 sheets** organised as follows:

| Sheet | Purpose | Input Required |
|-------|---------|----------------|
| Instructions | Guidance and agreement type definitions | None (read-only) |
| Agreement_Register | Master list of all transfer agreements | All agreement details |
| Agreement_Requirements | Standard security clauses | Applicability notes |
| Third_Party_Assessment | Security posture of partners | Assessment data |
| Review_Schedule | Renewal and review tracking | Dates, Status |
| Evidence_Register | Supporting documentation | Location, Status |
| Approval_SignOff | Register approval workflow | Signatures, Dates |

---

## 4. Completion Walkthrough

### Sheet 1: Instructions

**Purpose**: Provides overview and agreement type definitions.

**Agreement Types Defined**:

| Type | Full Name | Purpose |
|------|-----------|---------|
| **DSA** | Data Sharing Agreement | Governs sharing of specific data sets between parties |
| **ISA** | Interconnection Security Agreement | Technical security requirements for system interconnections |
| **MOU** | Memorandum of Understanding | High-level agreement on information exchange purposes |
| **DPA** | Data Processing Agreement | GDPR-required agreement for data processors |
| **SCC** | Standard Contractual Clauses | EU-approved clauses for international data transfers |
| **NDA** | Non-Disclosure Agreement | Confidentiality obligations for information exchange |

**Actions**:
1. Review agreement type definitions
2. Understand the register purpose
3. Note which agreement types apply to your organisation
4. Proceed to Agreement_Register sheet

### Sheet 2: Agreement_Register

**Purpose**: Central inventory of all transfer agreements.

**For Each Agreement, Document**:

| Column | Description | Example |
|--------|-------------|---------|
| Agreement ID | Unique identifier | "AGR-001" |
| Agreement Type | Type code | "DSA", "DPA", "ISA" |
| Third Party | Organisation name | "Cloud Provider Inc" |
| Purpose/Scope | What data is transferred and why | "Customer analytics data sharing" |
| Data Classification | Highest classification transferred | "CONFIDENTIAL" |
| Transfer Direction | Flow direction | "Bi-directional", "Outbound", "Inbound" |
| Effective Date | When agreement starts | "01.01.2025" |
| Expiry Date | When agreement ends | "31.12.2026" |
| Review Date | Next review due | "01.07.2026" |
| Owner | Business relationship owner | "Marketing Director" |
| Status | Current state | "Active", "Expiring Soon", "Draft" |
| Notes | Additional context | "Auto-renews annually" |

**Status Options**:
- **Draft**: Agreement being negotiated
- **Under Review**: Awaiting approval
- **Active**: Current and valid
- **Expiring Soon**: Within 90 days of expiry
- **Expired**: Past expiry date
- **Terminated**: Ended before expiry

**Agreement Register Checklist**:
- [ ] All third parties receiving organisational data are listed
- [ ] All suppliers processing data are included
- [ ] Agreement types are correctly categorised
- [ ] Effective and expiry dates are populated
- [ ] Review dates are set appropriately
- [ ] Owners are assigned for each agreement

### Sheet 3: Agreement_Requirements

**Purpose**: Document standard security clauses for agreements.

**Requirement Categories**:
1. **Data Protection**: Classification handling, encryption, retention
2. **Access Control**: Authorised users, authentication, logging
3. **Incident Response**: Notification requirements, coordination
4. **Compliance**: Audit rights, certifications, regulatory
5. **Liability**: Indemnification, insurance
6. **Termination**: Data return/destruction, transition
7. **Sub-Processing**: Approval and security for sub-contractors
8. **Transfer Mechanisms**: Legal basis for international transfers

**For Each Requirement, Review**:

| Column | Description | Action |
|--------|-------------|--------|
| Requirement Category | Security domain | Pre-populated |
| Clause/Requirement | Specific clause text | Pre-populated |
| Mandatory For | Which agreement types | Pre-populated |
| Rationale | Why required | Pre-populated |
| Template Reference | Where to find clause | Update with your template location |
| Applicability | Which classifications | Pre-populated |
| Notes | Organisation-specific notes | Document deviations |

**Key Requirements to Verify**:
- [ ] Data classification handling requirements
- [ ] Encryption requirements (at rest and in transit)
- [ ] Data retention and deletion obligations
- [ ] Security incident notification requirements
- [ ] Right to audit clause
- [ ] Certification requirements (ISO 27001, SOC 2)
- [ ] Data return/destruction on termination
- [ ] Sub-processor approval requirements

### Sheet 4: Third_Party_Assessment

**Purpose**: Track security posture of transfer partners.

**For Each Third Party, Document**:

| Column | Description | Example |
|--------|-------------|---------|
| Third Party | Organisation name | "Cloud Provider Inc" |
| Agreement ID | Link to agreement | "AGR-002" |
| Assessment Date | Last assessment date | "15.01.2026" |
| ISO 27001 Certified | Certification status | "Yes", "No", "In Progress" |
| SOC 2 Report | Report availability | "Type II", "Type I", "Not Available" |
| Security Questionnaire | Questionnaire status | "Completed", "Pending" |
| Penetration Test | Test recency | "Current (<12mo)", "Expired" |
| Risk Rating | Overall risk level | "Low", "Medium", "High" |
| Next Assessment | When reassessment due | "15.01.2027" |
| Notes | Assessment observations | "Strong security posture" |

**Assessment Criteria**:

| Rating | Criteria |
|--------|----------|
| Low Risk | ISO 27001 certified, SOC 2 Type II, clean questionnaire |
| Medium Risk | SOC 2 Type I or questionnaire only, minor findings |
| High Risk | No certifications, incomplete questionnaire, significant findings |
| Critical Risk | Security incidents, failed audits, non-responsive |

### Sheet 5: Review_Schedule

**Purpose**: Track agreement reviews and renewals.

**For Each Agreement, Track**:

| Column | Description | Example |
|--------|-------------|---------|
| Agreement ID | Reference to register | "AGR-001" |
| Third Party | Organisation name | "Example Partner Ltd" |
| Last Review Date | When last reviewed | "15.07.2025" |
| Next Review Date | When next review due | "15.07.2026" |
| Review Type | Type of review | "Annual", "Renewal", "Ad-hoc" |
| Reviewer | Assigned reviewer | "Contract Manager" |
| Review Status | Current status | "Scheduled", "In Progress", "Completed" |
| Action Required | Outcome needed | "Renew", "Update Clauses", "Terminate" |
| Notes | Review observations | "Security clauses need updating" |

**Review Types**:
- **Annual**: Standard yearly review
- **Semi-Annual**: For high-risk relationships
- **Quarterly**: For critical data sharing
- **Renewal**: Pre-expiry renewal review
- **Ad-hoc**: Triggered by incident or change

**Review Checklist**:
- [ ] Security clauses still adequate
- [ ] Third-party certification status current
- [ ] Data flows still as documented
- [ ] No reported security incidents
- [ ] Compliance obligations met
- [ ] Business need still exists

### Sheet 6: Evidence_Register

**Purpose**: Track supporting documentation.

**For Each Evidence Item**:

| Column | Action | Example |
|--------|--------|---------|
| Evidence ID | Unique identifier | "EV-514-AGR-001" |
| Evidence Type | Document category | "Signed Agreement" |
| Description | What it demonstrates | "Executed DSA with Example Partner" |
| Related Agreement | Link to register | "AGR-001" |
| Location/Link | Where stored | "Contract Repository/AGR-001" |
| Date Collected | When gathered | "01.01.2025" |
| Collected By | Who gathered | "Legal Counsel" |
| Status | Current status | "Verified" |

**Evidence Types**:
- Signed Agreement (executed contract)
- Security Certificate (ISO 27001, SOC 2)
- SOC 2 Report
- Legal Review (sign-off on terms)
- Assessment Report (security questionnaire)
- Review Record (annual review documentation)
- Termination Notice

### Sheet 7: Approval_SignOff

**Purpose**: Formal approval for the register.

**Complete**:
1. **Document Information**: Verify pre-filled data
2. **Register Summary**:
   - Total Agreements count
   - Active Agreements count
   - Expiring Within 90 Days
   - Expired Agreements
   - Agreements Requiring Review

3. **Approval Signatures**:

| Role | Responsibility |
|------|----------------|
| Register Owner | Maintains accuracy and completeness |
| Legal Representative | Validates legal compliance |
| Information Security Officer | Approves security requirements |
| Data Protection Officer | Validates data protection compliance |

---

## 5. Evidence Collection

### 5.1 Evidence by Agreement Type

| Agreement Type | Required Evidence |
|----------------|-------------------|
| DSA | Signed agreement, data classification record |
| ISA | Signed agreement, technical architecture |
| DPA | Signed agreement, GDPR compliance check |
| SCC | Executed SCCs, TIA documentation |
| NDA | Signed NDA, scope documentation |
| All | Third-party security certificates |

### 5.2 Evidence Storage

Store all evidence in:
```
/ISMS/Evidence/A.5.14-Information-Transfer/
├── A.5.14.3-Agreements/
│   ├── Executed-Agreements/
│   ├── Security-Certificates/
│   ├── SOC-Reports/
│   ├── Assessment-Records/
│   └── Review-Documentation/
```

### 5.3 Evidence Naming

Format: `EV-514-AGR-[AgreementID]-[Type]-[YYYYMMDD].[ext]`

Examples:
- `EV-514-AGR-001-Signed-DSA-20250101.pdf`
- `EV-514-AGR-002-ISO27001-Cert-20250115.pdf`
- `EV-514-AGR-003-SOC2-TypeII-20250201.pdf`

---

## 6. Common Pitfalls

### ❌ MISTAKE: Tracking only formal agreements, missing informal data sharing
✅ CORRECT: Include all data sharing relationships, even those pending formalisation

### ❌ MISTAKE: Not linking agreements to specific data classifications
✅ CORRECT: Document the highest classification level in each agreement

### ❌ MISTAKE: Setting all review dates to the same month
✅ CORRECT: Stagger review dates to spread workload throughout the year

### ❌ MISTAKE: Accepting expired certifications as valid evidence
✅ CORRECT: Verify certification validity dates and flag expired certificates

### ❌ MISTAKE: Not tracking agreements with "free" SaaS tools
✅ CORRECT: Cloud services processing organisational data need agreements

### ❌ MISTAKE: Missing DPA for suppliers processing personal data
✅ CORRECT: GDPR requires DPAs with all data processors

### ❌ MISTAKE: Not documenting sub-processor chains
✅ CORRECT: Track primary and sub-processors in agreement scope

### ❌ MISTAKE: Treating one-time transfers as not requiring agreements
✅ CORRECT: Even single transfers need documented confidentiality requirements

### ❌ MISTAKE: Not involving Legal in agreement reviews
✅ CORRECT: Legal review required for all agreement changes

### ❌ MISTAKE: Storing agreements without version control
✅ CORRECT: Maintain signed copies with clear version identification

---

## 7. Quality Checklist

Before submitting the register, verify:

### Agreement Register
- [ ] All third parties receiving data are listed
- [ ] All data processors have DPAs
- [ ] Agreement types are correctly categorised
- [ ] Status reflects actual agreement state
- [ ] Owners are assigned and current
- [ ] Dates are accurate and monitored

### Agreement Requirements
- [ ] All mandatory clauses documented
- [ ] Template references are accurate
- [ ] Applicability guidance is clear
- [ ] Deviations are documented

### Third-Party Assessments
- [ ] All active third parties assessed
- [ ] Assessment dates are current
- [ ] Risk ratings reflect actual posture
- [ ] Reassessment dates scheduled
- [ ] High-risk parties have remediation plans

### Review Schedule
- [ ] All agreements have review dates
- [ ] Reviewers are assigned
- [ ] Overdue reviews are flagged
- [ ] Actions are documented

### Evidence and Approval
- [ ] Signed agreements available for all active entries
- [ ] Certificates validated and current
- [ ] All approvals obtained
- [ ] Summary metrics accurate

---

## 8. Review and Approval

### 8.1 Register Maintenance
- **Frequency**: Continuous (update as agreements change)
- **Full review**: Quarterly
- **Triggers**: New agreements, renewals, terminations, incidents

### 8.2 Approval Workflow
1. **Register Owner** maintains entries
2. **Legal Representative** validates compliance
3. **ISO** approves security requirements
4. **DPO** validates data protection aspects

### 8.3 Post-Approval Actions
- Notify stakeholders of new agreements
- Update risk register for high-risk relationships
- Schedule assessments for new third parties
- Configure monitoring for expiring agreements

---

# PART II: TECHNICAL SPECIFICATION

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

<!-- QA_VERIFIED: 2026-02-04 -->
