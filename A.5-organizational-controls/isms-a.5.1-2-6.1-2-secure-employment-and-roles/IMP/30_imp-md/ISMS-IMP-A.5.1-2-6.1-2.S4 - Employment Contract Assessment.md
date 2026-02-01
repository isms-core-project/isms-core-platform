# ISMS-IMP-A.5.1-2-6.1-2.S4 — Employment Contract Assessment

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Employment Contract Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.1-2-6.1-2.S4 |
| **Related Policy** | ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.6.2 (Terms and Conditions of Employment) |
| **Linked Control** | ISO/IEC 27001:2022 Annex A.6.5 (Responsibilities at Termination or Change of Employment) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO / Chief Human Resources Officer (CHRO) — joint ownership |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:
- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) — Section 7 (Employment Contract Requirements)
- ISMS-IMP-A.5.1-2-6.1-2.S1 (Policy Framework Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S2 (Roles & Responsibilities Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S3 (Screening & Vetting Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S5 (Governance Compliance Dashboard)
- Swiss Code of Obligations (OR) — Articles 328, 328b, 730a
- Swiss Federal Data Protection Act (FADP / nDSG) — Articles 6, 19
- ISMS-POL-A.8.12 (Data Leakage Prevention) — Annex A (monitoring transparency in employment contracts)

**Note on Linked Controls**: This assessment covers both A.6.2 (what security obligations are IN the contract) and A.6.5 (that post-employment obligations are specified and enforced). These are assessed together because A.6.5 obligations (confidentiality surviving termination, IP assignment, device return) must be contractually established by A.6.2.

---

## PART I: USER GUIDE
**Audience:** HR managers, CISO, Legal/Compliance, recruitment team, DPO, department heads

---

## 1. Purpose and Scope

### 1.1 Assessment Objective

This assessment verifies [Organization]'s compliance with ISO/IEC 27001:2022 Controls A.6.2 (Terms and Conditions of Employment) and A.6.5 (Responsibilities at Termination or Change of Employment).

**Control A.6.2 Requirement:**
> *The employment contractual agreements should state the personnel's and the organisation's responsibilities for information security.*

**Control A.6.5 Requirement:**
> *Information security responsibilities and duties that remain valid after termination or change of employment should be defined, enforced and communicated to relevant personnel and other interested parties.*

**Two-dimensional assessment:**
- **Horizontal (A.6.2)**: Verify the RIGHT clauses exist in the contract templates and that all individuals have signed compliant contracts
- **Vertical (A.6.5)**: Verify post-employment obligations are specified, communicated, and tracked after individuals leave

**What This Assessment Covers:**
- Contract template completeness (do templates contain all required security clauses?)
- Required security clause identification and verification
- Per-individual contract compliance (has everyone signed a current, compliant contract?)
- Confidentiality / NDA coverage and status
- Post-employment obligation tracking (ongoing duties after termination)
- Contractor and third-party agreement compliance
- Legal alignment (Swiss OR, FADP transparency requirements)

### 1.2 Relationship to Parent Policy

This assessment implements verification procedures for **ISMS-POL-A.5.1-2-6.1-2, Section 7: Employment Contract Requirements**.

**Policy Requirements Being Assessed:**
- **Section 7.1**: Contract Security Clauses (what must be in every employment contract)
- **Section 7.2**: Role-Specific Contract Provisions (additional clauses for sensitive roles)
- **Section 7.3**: Confidentiality and NDA Requirements (standalone or embedded)
- **Section 7.4**: Intellectual Property Assignment
- **Section 7.5**: Monitoring Acknowledgment (transparency obligation per FADP)
- **Section 7.6**: Disciplinary Process Clause
- **Section 7.7**: Post-Employment Obligations (what survives termination)
- **Section 7.8**: Contractor and Third-Party Agreements

### 1.3 Assessment Frequency

- **Quarterly**: Routine compliance verification (are new hires' contracts compliant? Are post-employment obligations being tracked?)
- **Annual**: Full template review and legal alignment re-assessment
- **Triggered**: After contract template changes, new regulatory requirements, or audit findings

### 1.4 Assessment Ownership

**Primary Owner**: CISO and CHRO (joint ownership)

**Participants:**
- CISO (security clause requirements, risk assessment)
- CHRO / HR Manager (contract template management, employee records)
- Legal / Compliance Officer (contract legality, Swiss OR compliance, enforceability)
- DPO (FADP transparency obligations in contracts, monitoring acknowledgment)
- Recruitment Manager (new hire contract issuance)
- Department Heads (role-specific provision requirements)

**Time Investment:** 4-6 hours initial assessment, 2-3 hours quarterly updates

---

## 2. Assessment Methodology

### 2.1 Assessment Approach

**Template-first, then person-level:** First verify the contract templates are correct, then verify every individual has signed a current template.

**Step 1: Template Assessment**
- Identify all contract templates in use (full-time, part-time, contractor, consultant)
- Verify each template contains all required security clauses
- Confirm templates are current (reviewed within 12 months)
- Check legal review sign-off on templates

**Step 2: Required Clause Registry**
- Enumerate all security-related clauses that must appear in contracts
- Map each clause to its policy requirement, legal basis, and applicable role scope
- Verify each required clause is present in the correct template(s)
- Flag missing or incomplete clauses

**Step 3: Individual Contract Compliance**
- For each employee and contractor, verify they have signed a current compliant contract
- Identify individuals with: missing contracts, outdated contracts, contracts missing required clauses
- Track contract signature dates and versions

**Step 4: Confidentiality / NDA Verification**
- Verify NDA or confidentiality clause coverage per individual
- Determine if NDA is embedded in employment contract or standalone
- Track NDA status for contractors and individuals with access to Confidential/Restricted data

**Step 5: Post-Employment Obligation Tracking**
- Verify post-employment obligations are specified in contracts
- Track individuals who have left the organization — are obligations being enforced?
- Monitor ongoing confidentiality obligations

**Step 6: Contractor & Third-Party Agreement Verification**
- Verify all contractors and vendors have compliant agreements
- Check for required security clauses specific to external parties
- Verify NDA status

**Step 7: Gap Analysis**
- Consolidate all gaps from Steps 1–6
- Assess risk levels
- Define remediation actions

### 2.2 Compliance Criteria

**Compliant Contract** meets ALL criteria:
- ✅ Contract template is current (reviewed within 12 months, legally signed off)
- ✅ Contract contains all required security clauses for the individual's role
- ✅ Individual has signed the contract (signature documented)
- ✅ Contract signed before or at start of employment
- ✅ NDA / confidentiality clause in place (embedded or standalone)
- ✅ Post-employment obligations clearly specified
- ✅ Monitoring acknowledgment included (FADP transparency)

**Partial Compliance** when:
- ⚠️ Contract signed but one clause is missing or incomplete
- ⚠️ Contract version is outdated but individual has not yet been asked to sign updated version (within 90-day remediation window)
- ⚠️ NDA is standalone and not yet signed but in process
- ⚠️ Post-employment obligations specified but communication to departing employee not confirmed

**Non-Compliant** when:
- ❌ Individual has no signed contract
- ❌ Contract missing confidentiality / NDA clause for an individual with access to Confidential or Restricted data
- ❌ Contract missing security responsibility clause
- ❌ Contractor/vendor with system access and no security agreement
- ❌ Post-employment obligations not specified in contract for roles with sensitive access

### 2.3 Scoring Methodology

**Domain Weights:**
- Contract Template Completeness: 20%
- Required Clause Coverage: 25%
- Individual Contract Compliance: 30%
- Post-Employment Obligation Coverage: 15%
- Contractor Agreement Compliance: 10%

**Score Interpretation:**
- **90–100%**: Excellent
- **80–89%**: Good
- **70–79%**: Acceptable
- **60–69%**: Needs Improvement
- **< 60%**: Critical

---

## 3. Required Security Clauses

### 3.1 Universal Clauses (All Employment Contracts)

Every employment contract at [Organization] must contain the following security-related clauses, regardless of role:

**Clause 1: Information Security Responsibilities**
- Employee acknowledges responsibility to protect organizational information
- Employee agrees to comply with all information security policies, procedures, and guidelines
- Employee acknowledges that information security policies will be communicated and must be followed
- Policy Reference: ISMS-POL-A.5.1-2-6.1-2, Section 7.1

**Clause 2: Confidentiality**
- Employee agrees to maintain confidentiality of all organizational information encountered during employment
- Defines what constitutes confidential information (organizational data, trade secrets, customer information, personal data of colleagues)
- Specifies that confidentiality obligation survives termination (see Post-Employment section)
- Policy Reference: ISMS-POL-A.5.1-2-6.1-2, Section 7.3

**Clause 3: Acceptable Use**
- Employee agrees to use organizational information systems and resources only for authorized business purposes
- References the organization's Acceptable Use Policy
- Employee acknowledges consequences of violation
- Policy Reference: ISMS-POL-A.5.1-2-6.1-2, Section 7.1

**Clause 4: Monitoring Acknowledgment**
- Employee is informed that organizational systems may be monitored for security purposes
- Scope of monitoring disclosed (in general terms — specific details in privacy notice)
- Legal Basis: Swiss FADP Art. 19 (transparency), Swiss OR Art. 328b (protection of employee personality)
- Policy Reference: ISMS-POL-A.8.12, Annex A.4

**Clause 5: Disciplinary Consequences**
- Employee acknowledges that information security policy violations may result in disciplinary action
- States that disciplinary action may range from warning to termination depending on severity
- References the organization's disciplinary / sanctions process
- Policy Reference: ISMS-POL-A.5.1-2-6.1-2, Section 7.6

**Clause 6: Post-Employment Obligations**
- Confidentiality obligation survives termination (duration specified — typically indefinite for trade secrets, defined period for other confidential information)
- Obligation to return all organizational assets (devices, documents, access credentials) upon termination
- Policy Reference: ISMS-POL-A.5.1-2-6.1-2, Section 7.7

### 3.2 Role-Specific Clauses

**For Roles with Access to Confidential or Restricted Data (Tier 1–3):**

**Clause 7: Intellectual Property Assignment**
- All work product, inventions, and intellectual property created in connection with employment belong to [Organization]
- Specifies scope (during employment and for a defined period after, where legally permissible under Swiss OR)
- Swiss OR Note: IP assignment clauses must comply with Swiss law — assignment of inventions made outside working hours and unrelated to employer business is generally not permissible
- Policy Reference: ISMS-POL-A.5.1-2-6.1-2, Section 7.4

**Clause 8: Non-Solicitation (where applicable)**
- Employee agrees not to solicit customers, partners, or colleagues for a defined period after termination
- Duration must be reasonable under Swiss law (typically 6–12 months maximum)
- Policy Reference: ISMS-POL-A.5.1-2-6.1-2, Section 7.7

**For Security Leadership Roles (Tier 1):**

**Clause 9: Conflict of Interest Disclosure**
- Employee agrees to disclose any financial interests or relationships that could create conflicts with organizational security decisions
- Defines what constitutes a reportable conflict
- Policy Reference: ISMS-POL-A.5.1-2-6.1-2, Section 7.2

### 3.3 Contractor-Specific Clauses

**For All Contractors and Consultants:**

**Clause 10: Contractor Security Obligations**
- Contractor agrees to comply with all applicable organizational security policies during engagement
- Contractor acknowledges that access will be revoked upon engagement termination
- Contractor agrees to return all organizational assets upon termination
- Policy Reference: ISMS-POL-A.5.1-2-6.1-2, Section 7.8

**Clause 11: Contractor NDA / Confidentiality**
- Standalone NDA or equivalent confidentiality clause
- Covers organizational information, customer data, and technical details
- Survives contract termination
- Policy Reference: ISMS-POL-A.5.1-2-6.1-2, Section 7.3

**Clause 12: Contractor Data Processing (if applicable)**
- If contractor processes personal data on behalf of [Organization], a Data Processing Agreement (DPA) must be in place
- DPA covers processing scope, security measures, sub-processor restrictions, breach notification
- Legal Basis: Swiss FADP Art. 9; GDPR Art. 28
- Policy Reference: ISMS-POL-A.5.1-2-6.1-2, Section 7.8

---

## 4. Assessment Workbook Structure

### 4.1 Workbook Overview

**File Name**: `ISMS-IMP-A.5.1-2-6.1-2.S4_Employment_Contract_YYYYMMDD.xlsx`

**Sheet Count**: 10 sheets

| Sheet # | Sheet Name | Purpose | Rows (Approx) |
|---------|------------|---------|---------------|
| 1 | Dashboard | Executive summary and metrics | 80 |
| 2 | Contract_Template_Assessment | Verify contract templates are complete and current | 40 |
| 3 | Required_Clause_Registry | Master list of required clauses and template coverage | 30 |
| 4 | Personnel_Contract_Compliance | Per-person contract status verification | 150 |
| 5 | Confidentiality_NDA_Tracking | NDA / confidentiality status per individual | 150 |
| 6 | Post_Employment_Obligations | Track individuals with ongoing obligations | 80 |
| 7 | Contractor_Agreement_Assessment | Third-party agreement verification | 60 |
| 8 | Gap_Analysis | Consolidated gaps with risk and remediation | 80 |
| 9 | Evidence_Register | Supporting evidence documentation | 80 |
| 10 | Approval_Sign_Off | Three-level approval workflow | 60 |

**Assessment Flow:**
1. Complete **Sheet 2** — verify contract templates
2. Complete **Sheet 3** — verify all required clauses are in templates
3. Complete **Sheet 4** — verify each individual's contract
4. Complete **Sheet 5** — verify NDA/confidentiality for each individual
5. Complete **Sheet 6** — verify post-employment obligations are tracked
6. Complete **Sheet 7** — verify contractor/third-party agreements
7. Review **Sheet 8** — consolidated gaps
8. Document **Sheet 9** — evidence
9. Review **Sheet 1** — auto-calculated dashboard
10. Obtain **Sheet 10** — approval sign-off

---

## 5. Sheet-by-Sheet Completion Guide

### Sheet 1: Dashboard

**Purpose**: Executive summary auto-calculated from all other sheets.

**User Action**: **READ ONLY**

**Key Metrics:**
- Overall compliance score (weighted average)
- Total contract templates in use vs. compliant templates
- Personnel with compliant contracts (count and %)
- Personnel with NDA/confidentiality gaps (count)
- Post-employment obligations currently tracked (count)
- Contractor agreements compliant (count and %)
- Critical gaps count
- Next contract renewal / update deadline (earliest)

**Domain Compliance Breakdown (rows 32–37):**
- Contract Template Completeness: 20% weight
- Required Clause Coverage: 25% weight
- Individual Contract Compliance: 30% weight
- Post-Employment Obligation Coverage: 15% weight
- Contractor Agreement Compliance: 10% weight

---

### Sheet 2: Contract_Template_Assessment

**Purpose**: Verify that all contract templates in use contain the required security clauses and are legally current.

**Structure**: One section per contract template type. Each template assessed across 12 verification questions.

**Section A: Template Inventory (Rows 5–12)**

| Column | Header | Description |
|--------|--------|-------------|
| A | Template_ID | TMPL-001 through TMPL-006 |
| B | Template_Name | Descriptive name |
| C | Template_Scope | Who uses this template |
| D | Template_Version | Current version number |
| E | Template_Date | Date of current version |
| F | Template_Owner | Who manages this template |
| G | Last_Legal_Review_Date | When legal last reviewed |
| H | Legal_Review_Status | Current / Overdue-<6-Months / Overdue->6-Months |
| I | Template_In_Use | Yes / No / Deprecated |
| J | Template_Compliance_Rating | Auto-calculated |

**Pre-filled Template Rows:**

| ID | Template_Name | Template_Scope |
|----|---------------|----------------|
| TMPL-001 | Full-Time Employee Contract | All full-time employees |
| TMPL-002 | Part-Time Employee Contract | All part-time employees |
| TMPL-003 | Fixed-Term Employee Contract | Fixed-term (project) employees |
| TMPL-004 | Contractor Agreement | Independent contractors |
| TMPL-005 | Consultant Agreement | External consultants |
| TMPL-006 | Vendor Security Agreement | Third-party vendors with system access |

**Section B: Clause Presence Verification (Rows 16–40)**

For each template in use, verify the presence of each required clause:

| Column | Header | Description |
|--------|--------|-------------|
| A | Template_ID | Reference to Section A |
| B | Clause_ID | Reference to Required_Clause_Registry (Sheet 3) |
| C | Clause_Required_for_Template | Yes / No (auto from Sheet 3 mapping) |
| D | Clause_Present_in_Template | Yes / No / Partial |
| E | Clause_Location_in_Template | Section/Article reference (e.g., "Section 8, Paragraph 2") |
| F | Clause_Adequate | Yes / No (is the clause substantively complete?) |
| G | Gap_Description | Required if D = "No" or F = "No" |

**Assessment Logic:**
- For each template × clause combination, the assessor verifies whether the clause is present, where it is located, and whether the wording is substantively adequate
- "Partial" means the clause exists but is incomplete (e.g., confidentiality clause present but does not specify survival after termination)
- Cross-reference with Sheet 3 (Required_Clause_Registry) to determine which clauses apply to each template

---

### Sheet 3: Required_Clause_Registry

**Purpose**: Master registry of all required security clauses, their applicability scope, and current coverage status.

**Structure**: 25 clause rows (rows 5–29), 12 columns (A–L).

**Columns:**

| Col | Header | Type | Description |
|-----|--------|------|-------------|
| A | Clause_ID | Text | CLAUSE-01 through CLAUSE-12 (per Section 3) |
| B | Clause_Name | Text | Short descriptive name |
| C | Clause_Description | Text | Full description of what the clause must contain |
| D | Policy_Reference | Text | ISMS-POL section reference |
| E | Legal_Basis | Text | Swiss OR / FADP / ISO 27001 reference |
| F | Applies_To | Dropdown | All-Employees / Tier1-3-Only / Tier1-Only / Contractors-Only / All |
| G | Required_in_TMPL001 | Dropdown | Yes / No |
| H | Required_in_TMPL002 | Dropdown | Yes / No |
| I | Required_in_TMPL003 | Dropdown | Yes / No |
| J | Required_in_TMPL004 | Dropdown | Yes / No |
| K | Required_in_TMPL005 | Dropdown | Yes / No |
| L | Required_in_TMPL006 | Dropdown | Yes / No |

**Pre-filled Clause Registry:**

| ID | Clause_Name | Applies_To | TMPL-001 | TMPL-002 | TMPL-003 | TMPL-004 | TMPL-005 | TMPL-006 |
|----|-------------|------------|----------|----------|----------|----------|----------|----------|
| CLAUSE-01 | Information Security Responsibilities | All-Employees | Yes | Yes | Yes | — | — | — |
| CLAUSE-02 | Confidentiality | All-Employees | Yes | Yes | Yes | — | — | — |
| CLAUSE-03 | Acceptable Use | All-Employees | Yes | Yes | Yes | — | — | — |
| CLAUSE-04 | Monitoring Acknowledgment | All-Employees | Yes | Yes | Yes | — | — | — |
| CLAUSE-05 | Disciplinary Consequences | All-Employees | Yes | Yes | Yes | — | — | — |
| CLAUSE-06 | Post-Employment Obligations | All-Employees | Yes | Yes | Yes | — | — | — |
| CLAUSE-07 | Intellectual Property Assignment | Tier1-3-Only | Yes | Yes | Yes | — | — | — |
| CLAUSE-08 | Non-Solicitation | Tier1-3-Only | Yes | Yes | Yes | — | — | — |
| CLAUSE-09 | Conflict of Interest Disclosure | Tier1-Only | Yes | Yes | Yes | — | — | — |
| CLAUSE-10 | Contractor Security Obligations | Contractors-Only | — | — | — | Yes | Yes | Yes |
| CLAUSE-11 | Contractor NDA / Confidentiality | Contractors-Only | — | — | — | Yes | Yes | Yes |
| CLAUSE-12 | Contractor Data Processing (DPA) | Contractors-Only | — | — | — | Yes | Yes | Yes |

**Note on Column Scope:** Columns G–L indicate whether each clause is required in each template type. "—" means not applicable. The Applies_To field drives this mapping — assessors should verify it matches the clause requirements in Section 3 of this specification.

---

### Sheet 4: Personnel_Contract_Compliance

**Purpose**: Per-individual verification that each employee/contractor has signed a current, compliant contract.

**Structure**: 150 data rows (rows 5–154), 16 columns (A–P).

**Columns:**

| Col | Header | Type | Description |
|-----|--------|------|-------------|
| A | Personnel_ID | Text | Unique ID (cross-reference with .S3 Personnel_Screening_Registry) |
| B | Full_Name | Text | Legal full name |
| C | Role_ID | Text | From .S2 Role Inventory |
| D | Role_Tier | Text | Auto-populated from .S2 |
| E | Employment_Type | Dropdown | Full-Time / Part-Time / Fixed-Term / Contractor / Consultant |
| F | Contract_Template_Used | Text | Template ID (e.g., TMPL-001) |
| G | Contract_Version_Signed | Text | Version of template signed |
| H | Contract_Current_Version | Text | Auto-populated: current version from Sheet 2 |
| I | Contract_Signature_Date | Date | When the individual signed |
| J | Contract_Start_Date | Date | Employment/engagement start date |
| K | Contract_Signed_Before_Start | Dropdown | Yes / No / Same-Day |
| L | Contract_Up_to_Date | Text | Auto-calculated: current version signed? |
| M | All_Required_Clauses_Present | Text | Auto-calculated: based on role tier and template clause mapping |
| N | Contract_Compliance_Rating | Text | Auto-calculated: Compliant / Partial / Non-Compliant |
| O | Gap_Description | Text | Free text |
| P | Evidence_Reference | Text | Evidence IDs from Sheet 9 |

**Auto-Calculate Formulas:**

**D (Role_Tier):** VLOOKUP from .S2 using Role_ID

**H (Contract_Current_Version):**
```excel
=IF(F5="","",VLOOKUP(F5,Screening_Level_Matrix!$A$5:$D$10,4,FALSE))
```
*(References Sheet 2 template inventory for current version)*

**L (Contract_Up_to_Date):**
```excel
=IF(G5="","Unknown",IF(G5=H5,"Yes","No"))
```

**M (All_Required_Clauses_Present):**
```excel
=IF(F5="","","See Sheet 2 Section B for clause verification")
```
*(This field is a reference — detailed clause presence is verified in Sheet 2. The formula checks whether any gaps were flagged in Sheet 2 for this individual's template.)*

**N (Contract_Compliance_Rating):**
```excel
=IF(B5="","",IF(AND(L5="Yes",K5<>"No",M5="Yes"),"Compliant",IF(OR(F5="",G5=""),"Non-Compliant","Partial")))
```

**Dropdowns:**
- Employment_Type: Full-Time / Part-Time / Fixed-Term / Contractor / Consultant
- Contract_Signed_Before_Start: Yes / No / Same-Day

**Named Range:** `Personnel_Contract_ID_List` = Personnel_Contract_Compliance!$A$5:$A$154

---

### Sheet 5: Confidentiality_NDA_Tracking

**Purpose**: Track confidentiality / NDA status for each individual. This is critical because confidentiality protection is one of the most auditable aspects of employment contract compliance — auditors will specifically request NDA evidence.

**Structure**: 150 data rows (rows 5–154), 14 columns (A–N).

**Columns:**

| Col | Header | Type | Description |
|-----|--------|------|-------------|
| A | Personnel_ID | Text | Auto-populated from Sheet 4 |
| B | Full_Name | Text | Auto-populated from Sheet 4 |
| C | Role_Tier | Text | Auto-populated from Sheet 4 |
| D | Information_Access_Classification | Dropdown | Internal / Confidential / Restricted |
| E | NDA_Required | Text | Auto-calculated: Yes if access ≥ Confidential, or if Tier 1–3 |
| F | NDA_Type | Dropdown | Embedded-in-Contract / Standalone-NDA / Not-Required / Missing |
| G | NDA_Signature_Date | Date | When NDA was signed |
| H | NDA_Signed_Before_Access | Dropdown | Yes / No / Same-Day / N/A |
| I | NDA_Duration | Text | Duration of confidentiality obligation (e.g., "Indefinite" or "5 years post-termination") |
| J | NDA_Survival_Clause | Dropdown | Yes / No / N/A (does confidentiality survive termination?) |
| K | NDA_Document_Location | Text | File path or URL to signed NDA |
| L | NDA_Compliance_Rating | Text | Auto-calculated: Compliant / Partial / Non-Compliant |
| M | Gap_Description | Text | Free text |
| N | Evidence_Reference | Text | Evidence IDs |

**Auto-Calculate Formulas:**

**E (NDA_Required):**
```excel
=IF(B5="","",IF(OR(D5="Confidential",D5="Restricted",C5="Tier-1-Leadership",C5="Tier-2-Management",C5="Tier-3-Operational"),"Yes","No"))
```

**L (NDA_Compliance_Rating):**
```excel
=IF(B5="","",IF(E5="No","N/A",IF(AND(OR(F5="Embedded-in-Contract",F5="Standalone-NDA"),G5<>"",H5<>"No",J5="Yes"),"Compliant",IF(F5="Missing","Non-Compliant","Partial"))))
```

**Dropdowns:**
- Information_Access_Classification: Internal / Confidential / Restricted
- NDA_Type: Embedded-in-Contract / Standalone-NDA / Not-Required / Missing
- NDA_Signed_Before_Access: Yes / No / Same-Day / N/A
- NDA_Survival_Clause: Yes / No / N/A

---

### Sheet 6: Post_Employment_Obligations

**Purpose**: Track individuals who have left the organization and verify that post-employment security obligations (confidentiality, non-solicitation, device return) are being enforced. Also track current employees' post-employment clauses for completeness.

**Structure**: Two sections.

**Section A: Current Employees — Post-Employment Clause Verification (Rows 5–54, 50 rows)**

For current employees, verify that their contracts include the necessary post-employment obligations:

| Col | Header | Type | Description |
|-----|--------|------|-------------|
| A | Personnel_ID | Text | Employee ID |
| B | Full_Name | Text | Name |
| C | Role_Tier | Text | From .S2 |
| D | Confidentiality_Survives_Termination | Dropdown | Yes / No |
| E | Confidentiality_Duration | Text | "Indefinite" or defined period |
| F | Device_Return_Clause | Dropdown | Yes / No |
| G | Non_Solicitation_Clause | Dropdown | Yes / No / N/A |
| H | Non_Solicitation_Duration | Text | Duration (e.g., "12 months") or N/A |
| I | IP_Assignment_Post_Employment | Dropdown | Yes / No / N/A |
| J | Post_Employment_Clause_Rating | Text | Auto-calculated |

**J (Post_Employment_Clause_Rating):**
```excel
=IF(B5="","",IF(AND(D5="Yes",F5="Yes",IF(OR(C5="Tier-1-Leadership",C5="Tier-2-Management",C5="Tier-3-Operational"),G5="Yes",TRUE)),"Compliant",IF(OR(D5="No",F5="No"),"Non-Compliant","Partial")))
```

**Section B: Former Employees — Obligation Enforcement Tracking (Rows 58–108, 50 rows)**

For individuals who have left, track whether post-employment obligations are being enforced:

| Col | Header | Type | Description |
|-----|--------|------|-------------|
| A | Personnel_ID | Text | Former employee ID |
| B | Full_Name | Text | Name |
| C | Departure_Date | Date | When they left |
| D | Departure_Reason | Dropdown | Resignation / Termination / Retirement / Contract-End / Restructuring |
| E | Exit_Interview_Completed | Dropdown | Yes / No / N/A |
| F | Device_Return_Confirmed | Dropdown | Yes / No / Partial / N/A |
| G | Access_Revoked | Dropdown | Yes / No |
| H | Access_Revocation_Date | Date | When access was revoked |
| I | Confidentiality_Obligation_Active | Dropdown | Yes / No / Expired |
| J | Confidentiality_Expiry_Date | Date | When confidentiality obligation expires (or blank if indefinite) |
| K | Non_Solicitation_Active | Dropdown | Yes / No / Expired / N/A |
| L | Non_Solicitation_Expiry_Date | Date | Expiry date |
| M | Post_Employment_Tracking_Rating | Text | Auto-calculated |
| N | Notes | Text | Free text |

**M (Post_Employment_Tracking_Rating):**
```excel
=IF(B5="","",IF(AND(G5="Yes",F5<>"No",IF(I5="Yes",TRUE,I5="Expired")),"Compliant",IF(OR(G5="No",F5="No"),"Non-Compliant","Partial")))
```

**Critical Checks:**
- Access must be revoked on departure date (or before) — any delay is a gap
- Device return should be confirmed at exit
- Confidentiality obligation status must be tracked for the duration specified in the contract
- Former employees who violate post-employment obligations must be escalated to Legal

**Dropdowns (Section B):**
- Departure_Reason: Resignation / Termination / Retirement / Contract-End / Restructuring
- Exit_Interview_Completed: Yes / No / N/A
- Device_Return_Confirmed: Yes / No / Partial / N/A
- Access_Revoked: Yes / No
- Confidentiality_Obligation_Active: Yes / No / Expired
- Non_Solicitation_Active: Yes / No / Expired / N/A

---

### Sheet 7: Contractor_Agreement_Assessment

**Purpose**: Verify security agreements for all contractors, consultants, and vendors with system or facility access.

**Structure**: 60 data rows (rows 5–64), 18 columns (A–R).

**Columns:**

| Col | Header | Type | Description |
|-----|--------|------|-------------|
| A | Party_ID | Text | Unique ID (e.g., CTR-001, VND-001) |
| B | Party_Name | Text | Name of contractor/vendor |
| C | Party_Type | Dropdown | Contractor / Consultant / Vendor |
| D | Agreement_Template_Used | Text | Template ID from Sheet 2 |
| E | Agreement_Signed | Dropdown | Yes / No |
| F | Agreement_Signature_Date | Date | Date signed |
| G | Agreement_Start_Date | Date | Engagement start date |
| H | Agreement_End_Date | Date | Engagement end date (or blank if ongoing) |
| I | Security_Obligations_Clause | Dropdown | Yes / No |
| J | NDA_In_Place | Dropdown | Yes / No |
| K | NDA_Signature_Date | Date | Date NDA signed |
| L | DPA_Required | Dropdown | Yes / No |
| M | DPA_In_Place | Dropdown | Yes / No / N/A |
| N | DPA_Covers_Required_Elements | Dropdown | Yes / Partial / No / N/A |
| O | Access_Scope_Documented | Dropdown | Yes / No |
| P | Access_Revocation_on_End_Clause | Dropdown | Yes / No |
| Q | Agreement_Compliance_Rating | Text | Auto-calculated |
| R | Notes | Text | Free text |

**Q (Agreement_Compliance_Rating):**
```excel
=IF(B5="","",IF(AND(E5="Yes",I5="Yes",J5="Yes",IF(L5="Yes",AND(M5="Yes",N5="Yes"),TRUE),O5="Yes",P5="Yes"),"Compliant",IF(OR(E5="No",I5="No",J5="No",AND(L5="Yes",M5="No")),"Non-Compliant","Partial")))
```

**DPA Required Criteria:**
- DPA is required if the contractor/vendor processes personal data on behalf of [Organization]
- Examples: HR outsourcing, payroll processing, cloud services storing organizational data, background check providers
- DPA_Required = "Yes" if the party handles personal data; "No" if access is limited to non-personal operational systems

**DPA Required Elements (for N column assessment):**
1. Processing scope and purposes
2. Data subject rights facilitation
3. Security measures (FADP Art. 8 / GDPR Art. 32)
4. Sub-processor restrictions
5. Breach notification obligation (within 24 hours to [Organization])
6. Data return or deletion on termination
7. Audit rights for [Organization]

**Dropdowns:**
- Party_Type: Contractor / Consultant / Vendor
- Agreement_Signed: Yes / No
- Security_Obligations_Clause: Yes / No
- NDA_In_Place: Yes / No
- DPA_Required: Yes / No
- DPA_In_Place: Yes / No / N/A
- DPA_Covers_Required_Elements: Yes / Partial / No / N/A
- Access_Scope_Documented: Yes / No
- Access_Revocation_on_End_Clause: Yes / No

---

### Sheet 8: Gap_Analysis

**Purpose**: Consolidated gaps from all assessment sheets. Same structure as .S1, .S2, .S3.

**Structure**: 80 gap rows (rows 5–84), 16 columns (A–P).

| Col | Header | Type | Source |
|-----|--------|------|--------|
| A | Gap_ID | Text | Auto-generated: GAP-001 through GAP-080 |
| B | Source_Sheet | Dropdown | Template / Clause-Registry / Personnel / NDA / Post-Employment / Contractor |
| C | Personnel_ID | Text | From source sheet (or "N/A" for template-level gaps) |
| D | Gap_Category | Dropdown | Template-Gap / Clause-Gap / Contract-Gap / NDA-Gap / Post-Employment-Gap / Contractor-Gap |
| E | Gap_Description | Text | From source sheet |
| F | Risk_Level | Dropdown | Critical / High / Medium / Low |
| G | Impact_Assessment | Text | Free text |
| H | Affected_Stakeholders | Text | Free text |
| I | Remediation_Action | Text | Free text |
| J | Responsible_Party | Text | Free text |
| K | Target_Completion_Date | Date | DD.MM.YYYY |
| L | Estimated_Effort | Dropdown | <1hr / 1-4hrs / 1day / 2-5days / >1week |
| M | Dependencies | Text | Free text |
| N | Status | Dropdown | Not-Started / In-Progress / Blocked / Completed / Accepted-Risk |
| O | Completion_Evidence | Text | Required if Status = Completed |
| P | Risk_Acceptance | Text | Required if Status = Accepted-Risk |

**Risk Level Criteria for Contract Gaps:**
- **Critical**: Individual with Confidential/Restricted data access and no signed contract or no NDA; contractor with system access and no security agreement; access not revoked after departure
- **High**: Contract template missing required clause for Tier 1–3 roles; NDA missing for individual with Confidential data access; DPA missing for party processing personal data
- **Medium**: Contract outdated but individual still employed (remediation in progress); NDA incomplete; post-employment obligation not tracked
- **Low**: Documentation gaps (contract signed but records incomplete); template review overdue; minor clause wording issues

**Dropdowns:**
- Source_Sheet: Template / Clause-Registry / Personnel / NDA / Post-Employment / Contractor
- Gap_Category: Template-Gap / Clause-Gap / Contract-Gap / NDA-Gap / Post-Employment-Gap / Contractor-Gap
- Risk_Level: Critical / High / Medium / Low
- Estimated_Effort: <1hr / 1-4hrs / 1day / 2-5days / >1week
- Status: Not-Started / In-Progress / Blocked / Completed / Accepted-Risk

---

### Sheet 9: Evidence_Register

**Purpose**: Document all supporting evidence for the employment contract assessment.

**Structure**: 80 evidence rows (rows 5–84), 10 columns (A–J). Consistent with .S1–.S3 structure.

| Col | Header | Type | Description |
|-----|--------|------|-------------|
| A | Evidence_ID | Text | Auto-generated: EVD-001 through EVD-080 |
| B | Evidence_Type | Dropdown | See list below |
| C | Description | Text | Free text |
| D | Related_Personnel_ID | Text | Personnel ID or "All" or "Template" |
| E | Related_Assessment_Sheet | Text | Sheet name reference |
| F | File_Location | Text | URL or file path |
| G | Date_Collected | Date | DD.MM.YYYY |
| H | Collected_By | Text | Name and Role |
| I | Verification_Status | Dropdown | Verified / Pending / Not-Verified / Expired |
| J | Notes | Text | Free text |

**Evidence_Type Dropdown:**
Employment-Contract / Contract-Template / NDA-Agreement / DPA-Agreement / IP-Assignment-Agreement / Exit-Checklist / Access-Revocation-Record / Device-Return-Record / Legal-Review-Sign-Off / Template-Review-Record / Disciplinary-Policy / Acceptable-Use-Policy / Monitoring-Privacy-Notice / Post-Employment-Obligation-Letter / Other

**Verification_Status Dropdown:** Verified / Pending / Not-Verified / Expired

---

### Sheet 10: Approval_Sign_Off

**Purpose**: Three-level approval workflow. Consistent with .S1–.S3 structure.

**Section A: Assessment Summary (Rows 3–18)**

| Row | Label | Value | Source |
|-----|-------|-------|--------|
| 4 | Document | ISMS-IMP-A.5.1-2-6.1-2.S4 | Static |
| 5 | Assessment Period | [User input] | Yellow cell |
| 6 | Overall Compliance Score | [Formula] | Dashboard |
| 7 | Contract Templates Assessed | [Formula] | COUNTA from Sheet 2 |
| 8 | Compliant Templates | [Formula] | COUNTIF from Sheet 2 |
| 9 | Personnel Contracts Verified | [Formula] | COUNTA from Sheet 4 |
| 10 | Compliant Individual Contracts | [Formula] | COUNTIF from Sheet 4 |
| 11 | NDA Gaps | [Formula] | COUNTIF from Sheet 5 |
| 12 | Former Employees Tracked | [Formula] | COUNTA from Sheet 6 Section B |
| 13 | Contractor Agreements Assessed | [Formula] | COUNTA from Sheet 7 |
| 14 | Compliant Contractor Agreements | [Formula] | COUNTIF from Sheet 7 |
| 15 | Critical Gaps | [Formula] | COUNTIF from Sheet 8 |

**Section B: Level 1 — Prepared By (Rows 20–28)**
- Name, Role, Date, Signature
- Certification: "I certify that this employment contract assessment has been completed accurately and all contract records have been verified."
- Comments

**Section C: Level 2 — Reviewed By (Rows 30–48)**
- Name, Role, Date, Signature
- Review Checklist (10 items):
  1. All contract templates assessed and current
  2. Required clause registry complete and accurate
  3. All personnel contracts verified (no missing individuals)
  4. NDA/confidentiality status verified for all individuals with Confidential+ access
  5. Post-employment obligations specified in all Tier 1–3 contracts
  6. Former employee tracking current (access revoked, devices returned)
  7. Contractor/vendor agreements verified (NDA and DPA where required)
  8. Gap risk levels appropriately assessed
  9. Evidence sufficient and accessible
  10. Remediation actions tracked with responsible parties
- Comments

**Section D: Level 3 — Approved By (CISO / CHRO Joint Sign-Off) (Rows 50–62)**
- CISO Name, Role, Date, Signature
- CHRO Name, Role, Date, Signature
- Final Approval statement
- Risk Acceptance for any Accepted-Risk gaps
- Comments

**Section E: Assessment Metadata (Rows 64–72)**
- Next Review Date
- Assessment Status: Draft / Under-Review / Approved / Audit-Ready
- Audit Readiness Checklist (5 items):
  1. All three approval levels completed
  2. Evidence 100% verified
  3. All critical gaps have remediation plans
  4. All Tier 1–3 NDAs in place
  5. Assessment audit-ready

---

## 6. Quality Checklist

**Before submitting for approval, verify:**

### Contract Templates
- [ ] All contract templates identified (full-time, part-time, fixed-term, contractor, consultant, vendor)
- [ ] Each template reviewed for security clause completeness
- [ ] All templates have current legal review sign-off (within 12 months)
- [ ] Deprecated templates identified and not in use

### Required Clauses
- [ ] All 12 required clauses mapped to correct templates
- [ ] Clause presence verified for each template
- [ ] Missing clauses escalated for template update

### Individual Contracts
- [ ] All employees and contractors with system access verified
- [ ] Contract signature dates confirmed (before start date preferred)
- [ ] Current template version confirmed for all individuals
- [ ] Gaps identified for individuals with outdated or missing contracts

### NDA / Confidentiality
- [ ] All individuals with Confidential or Restricted data access have NDA in place
- [ ] NDA type confirmed (embedded or standalone)
- [ ] Survival clause confirmed (confidentiality survives termination)
- [ ] Signed NDA documents accessible

### Post-Employment Obligations
- [ ] All Tier 1–3 contracts include post-employment clauses
- [ ] All former employees tracked in Section B of Sheet 6
- [ ] Access revocation confirmed for all departed individuals
- [ ] Device return confirmed where applicable
- [ ] Ongoing confidentiality obligations tracked

### Contractor Agreements
- [ ] All contractors/vendors with access have signed agreements
- [ ] Security obligation clauses present
- [ ] NDAs in place for all contractors
- [ ] DPAs in place for parties processing personal data
- [ ] Access scope documented

### Evidence
- [ ] Signed contracts accessible for all individuals
- [ ] Signed NDAs documented (particularly critical for audit)
- [ ] Legal review sign-offs documented
- [ ] Exit checklists for departed individuals

---

## 7. Evidence Collection Guide

### 7.1 Evidence Organization

**Folder Structure:**
```
Evidence/A.6.2_Employment_Contracts/
├── 01_Contract_Templates/
│   ├── TMPL-001_FullTime_Employee_v2.0.pdf
│   ├── TMPL-002_PartTime_Employee_v1.1.pdf
│   ├── TMPL-003_FixedTerm_Employee_v1.0.pdf
│   ├── TMPL-004_Contractor_Agreement_v1.2.pdf
│   ├── TMPL-005_Consultant_Agreement_v1.0.pdf
│   ├── TMPL-006_Vendor_Security_Agreement_v1.0.pdf
│   └── Legal_Review_Sign_Offs/
│       └── ...
├── 02_Signed_Contracts/
│   ├── [PersonnelID]-Employment-Contract-Signed.pdf
│   └── ...
├── 03_NDAs/
│   ├── [PersonnelID]-NDA-Signed.pdf  ← CRITICAL FOR AUDIT
│   └── ...
├── 04_DPAs/
│   ├── [PartyID]-DPA-Signed.pdf
│   └── ...
├── 05_Exit_Documentation/
│   ├── [PersonnelID]-Exit-Checklist.pdf
│   ├── [PersonnelID]-Device-Return-Confirmation.pdf
│   ├── [PersonnelID]-Access-Revocation-Record.pdf
│   └── ...
├── 06_Post_Employment/
│   ├── [PersonnelID]-Post-Employment-Obligation-Letter.pdf
│   └── ...
└── 07_Other/
    └── ...
```

**Audit Priority**: Folder 03 (NDAs) is the most frequently requested by external auditors for A.6.2 compliance verification. Ensure all NDAs are scanned, signed originals stored securely, and digital copies are accessible.

---

## 8. Integration with Other Assessments

**Input from .S2 (Roles & Responsibilities):**
- Role Inventory provides role tiers, which drive which clauses are required (e.g., Tier 1 requires conflict of interest clause)
- Changes to role tiers trigger re-evaluation of required contract clauses

**Input from .S3 (Screening & Vetting):**
- Screening consent in .S3 must be consistent with contract terms in .S4
- .S3 screening consent is NOT the same as employment contract signature — they are separate documents with different legal purposes

**Output to .S5 (Governance Dashboard):**
- All contract gaps flow to consolidated dashboard
- NDA compliance rate is a key governance KPI
- Post-employment obligation tracking status included

**Critical Cross-Reference:**
- A new hire in .S3 (screening complete) must also have a signed contract in .S4 before starting work
- The .S4 contract must contain monitoring acknowledgment consistent with .S3 screening transparency requirements and ISMS-POL-A.8.12 DLP monitoring disclosure

---

**[END OF PART I: USER GUIDE]**

---

## PART II: TECHNICAL SPECIFICATION
**Audience:** Workbook developers, Python script maintainers

---

## 9. Workbook Technical Specification

### 9.1 Workbook Metadata

**File Name:** `ISMS-IMP-A.5.1-2-6.1-2.S4_Employment_Contract_YYYYMMDD.xlsx`

**Workbook Properties:**
- **Title**: ISMS-IMP-A.5.1-2-6.1-2.S4 — Employment Contract Assessment
- **Subject**: ISO/IEC 27001:2022 Controls A.6.2 & A.6.5 Assessment
- **Keywords**: Employment, Contract, NDA, Confidentiality, Post-Employment, ISMS, ISO27001, A.6.2, A.6.5
- **Comments**: Generated via `generate_a5_1_2_6_1_2_s4_employment_contract.py`

---

### 9.2 Sheet Structure Summary

| Sheet # | Sheet Name | Rows | Input | Formulas | Dropdowns |
|---------|------------|------|-------|----------|-----------|
| 1 | Dashboard | 80 | 6 | 35+ | 1 |
| 2 | Contract_Template_Assessment | 40 | 30+ | 8 | 10 |
| 3 | Required_Clause_Registry | 30 | 50+ | 0 | 8 |
| 4 | Personnel_Contract_Compliance | 154 | 900+ | 600 | 3 |
| 5 | Confidentiality_NDA_Tracking | 154 | 750+ | 450 | 5 |
| 6 | Post_Employment_Obligations | 110 | 600+ | 200 | 8 |
| 7 | Contractor_Agreement_Assessment | 64 | 900+ | 60 | 10 |
| 8 | Gap_Analysis | 84 | 640 | 80 | 5 |
| 9 | Evidence_Register | 84 | 640 | 80 | 2 |
| 10 | Approval_Sign_Off | 72 | 25 | 15 | 2 |

**Estimated Python Script Length:** ~900 lines

---

### 9.3 Color Scheme & Styling

**Consistent with .S1–.S3:**

| Element | Fill | Font |
|---------|------|------|
| User Input | Yellow (FFFF00) | Arial 10pt |
| Auto-Calculated | Light Blue (DCE6F1) | Arial 10pt |
| Labels | Gray (D9D9D9) | Arial 10pt Bold |
| Main Title | Dark Blue (003366) | Arial 18pt Bold White |
| Section Headers | Dark Blue (003366) | Arial 12pt White |

**Conditional Formatting — Status Fields:**

| Value | Fill | Font |
|-------|------|------|
| Compliant | Green (92D050) | Black |
| Partial | Yellow (FFFF00) | Black |
| Non-Compliant | Red (FF0000) | White |
| Yes (NDA) | Green (92D050) | Black |
| No (NDA — when required) | Red (FF0000) | White |
| Missing (NDA) | Red (FF0000) | White |
| Critical (Risk) | Red (FF0000) | White |
| High (Risk) | Orange (FFC000) | Black |
| Medium (Risk) | Yellow (FFFF00) | Black |
| Low (Risk) | Light Green (C6EFCE) | Black |

**Special Styling — NDA Column (Sheet 5, Col F):**
- "Missing" in NDA_Type column: Red fill with bold white text — draws immediate attention
- "Standalone-NDA": Light green fill — indicates NDA exists but is separate from contract (worth verifying)

---

### 9.4 Key Formula Patterns

**Contract Up-to-Date Check (Sheet 4, Col L):**
```excel
=IF(G5="","Unknown",IF(G5=H5,"Yes","No"))
```

**Contract Compliance Rating (Sheet 4, Col N):**
```excel
=IF(B5="","",IF(AND(F5<>"",G5<>"",L5="Yes",K5<>"No"),"Compliant",IF(OR(F5="",G5=""),"Non-Compliant","Partial")))
```

**NDA Required (Sheet 5, Col E):**
```excel
=IF(B5="","",IF(OR(D5="Confidential",D5="Restricted",C5="Tier-1-Leadership",C5="Tier-2-Management",C5="Tier-3-Operational"),"Yes","No"))
```

**NDA Compliance Rating (Sheet 5, Col L):**
```excel
=IF(B5="","",IF(E5="No","N/A",IF(AND(OR(F5="Embedded-in-Contract",F5="Standalone-NDA"),G5<>"",H5<>"No",J5="Yes"),"Compliant",IF(F5="Missing","Non-Compliant","Partial"))))
```

**Post-Employment Clause Rating — Current Employees (Sheet 6, Section A, Col J):**
```excel
=IF(B5="","",IF(AND(D5="Yes",F5="Yes",IF(OR(C5="Tier-1-Leadership",C5="Tier-2-Management",C5="Tier-3-Operational"),G5="Yes",TRUE)),"Compliant",IF(OR(D5="No",F5="No"),"Non-Compliant","Partial")))
```

**Post-Employment Tracking Rating — Former Employees (Sheet 6, Section B, Col M):**
```excel
=IF(B5="","",IF(AND(G5="Yes",F5<>"No",OR(I5="Yes",I5="Expired")),"Compliant",IF(OR(G5="No",F5="No"),"Non-Compliant","Partial")))
```

**Contractor Agreement Compliance (Sheet 7, Col Q):**
```excel
=IF(B5="","",IF(AND(E5="Yes",I5="Yes",J5="Yes",IF(L5="Yes",AND(M5="Yes",N5="Yes"),TRUE),O5="Yes",P5="Yes"),"Compliant",IF(OR(E5="No",I5="No",J5="No",AND(L5="Yes",M5="No")),"Non-Compliant","Partial")))
```

**Dashboard Overall Score:**
```excel
=B30*0.20 + B31*0.25 + B32*0.30 + B33*0.15 + B34*0.10
```

---

### 9.5 Data Validation Rules

**Sheet 2:**
- Template_In_Use: `List: Yes,No,Deprecated`
- Legal_Review_Status: `List: Current,Overdue-<6-Months,Overdue->6-Months`
- Clause_Present_in_Template: `List: Yes,No,Partial`
- Clause_Adequate: `List: Yes,No`

**Sheet 3:**
- Applies_To: `List: All-Employees,Tier1-3-Only,Tier1-Only,Contractors-Only,All`
- Required_in_TMPLxxx: `List: Yes,No`

**Sheet 4:**
- Employment_Type: `List: Full-Time,Part-Time,Fixed-Term,Contractor,Consultant`
- Contract_Signed_Before_Start: `List: Yes,No,Same-Day`

**Sheet 5:**
- Information_Access_Classification: `List: Internal,Confidential,Restricted`
- NDA_Type: `List: Embedded-in-Contract,Standalone-NDA,Not-Required,Missing`
- NDA_Signed_Before_Access: `List: Yes,No,Same-Day,N/A`
- NDA_Survival_Clause: `List: Yes,No,N/A`

**Sheet 6 (Section B):**
- Departure_Reason: `List: Resignation,Termination,Retirement,Contract-End,Restructuring`
- Exit_Interview_Completed: `List: Yes,No,N/A`
- Device_Return_Confirmed: `List: Yes,No,Partial,N/A`
- Access_Revoked: `List: Yes,No`
- Confidentiality_Obligation_Active: `List: Yes,No,Expired`
- Non_Solicitation_Active: `List: Yes,No,Expired,N/A`

**Sheet 7:**
- Party_Type: `List: Contractor,Consultant,Vendor`
- Agreement_Signed: `List: Yes,No`
- Security_Obligations_Clause: `List: Yes,No`
- NDA_In_Place: `List: Yes,No`
- DPA_Required: `List: Yes,No`
- DPA_In_Place: `List: Yes,No,N/A`
- DPA_Covers_Required_Elements: `List: Yes,Partial,No,N/A`
- Access_Scope_Documented: `List: Yes,No`
- Access_Revocation_on_End_Clause: `List: Yes,No`

**Sheet 8 (Gap_Analysis):**
- Source_Sheet: `List: Template,Clause-Registry,Personnel,NDA,Post-Employment,Contractor`
- Gap_Category: `List: Template-Gap,Clause-Gap,Contract-Gap,NDA-Gap,Post-Employment-Gap,Contractor-Gap`
- Risk_Level: `List: Critical,High,Medium,Low`
- Estimated_Effort: `List: <1hr,1-4hrs,1day,2-5days,>1week`
- Status: `List: Not-Started,In-Progress,Blocked,Completed,Accepted-Risk`

**Sheet 9 (Evidence_Register):**
- Evidence_Type: `List: Employment-Contract,Contract-Template,NDA-Agreement,DPA-Agreement,IP-Assignment-Agreement,Exit-Checklist,Access-Revocation-Record,Device-Return-Record,Legal-Review-Sign-Off,Template-Review-Record,Disciplinary-Policy,Acceptable-Use-Policy,Monitoring-Privacy-Notice,Post-Employment-Obligation-Letter,Other`
- Verification_Status: `List: Verified,Pending,Not-Verified,Expired`

---

### 9.6 Named Ranges

| Named Range | Reference | Purpose |
|-------------|-----------|---------|
| `Personnel_Contract_ID_List` | Personnel_Contract_Compliance!$A$5:$A$154 | Cross-sheet Personnel ID reference |
| `Template_ID_List` | Contract_Template_Assessment!$A$5:$A$10 | Template ID validation |
| `Clause_ID_List` | Required_Clause_Registry!$A$5:$A$29 | Clause ID validation |

---

### 9.7 Sheet Protection

**All sheets protected.** Unlocked: yellow input cells, date fields, dropdowns, free text fields.

**Special Note — Sheet 6 Section B (Former Employees):**
Access to former employee departure details should be restricted to HR, CISO, and Legal. Sheet protection enforces formula integrity; access to the workbook file should be controlled at the file-share level.

---

### 9.8 Conditional Formatting Rules

**Sheet 2, Col D (Clause_Present_in_Template):**
- Yes: Green fill
- No: Red fill
- Partial: Yellow fill

**Sheet 4, Col L (Contract_Up_to_Date):**
- Yes: Green fill
- No: Red fill
- Unknown: Orange fill

**Sheet 4, Col N (Contract_Compliance_Rating):**
- Compliant: Green / Partial: Yellow / Non-Compliant: Red

**Sheet 5, Col F (NDA_Type):**
- Embedded-in-Contract: Green fill
- Standalone-NDA: Light green fill
- Missing: Red fill, Bold white text
- Not-Required: No fill

**Sheet 5, Col L (NDA_Compliance_Rating):**
- Compliant: Green / Partial: Yellow / Non-Compliant: Red / N/A: No fill

**Sheet 6 Section B, Col G (Access_Revoked):**
- Yes: Green fill
- No: Red fill (critical — access should be revoked immediately on departure)

**Sheet 7, Col Q (Agreement_Compliance_Rating):**
- Compliant: Green / Partial: Yellow / Non-Compliant: Red

**Sheet 8, Col F (Risk_Level):**
- Critical: Red fill, White text / High: Orange / Medium: Yellow / Low: Light green

---

### 9.9 Freeze Panes

| Sheet | Freeze At | Rationale |
|-------|-----------|-----------|
| Dashboard | None | Full view |
| Contract_Template_Assessment | None | Two-section layout |
| Required_Clause_Registry | A5 | Keep headers visible |
| Personnel_Contract_Compliance | A5 | 150 rows — keep headers |
| Confidentiality_NDA_Tracking | A5 | 150 rows — keep headers |
| Post_Employment_Obligations | None | Two distinct sections |
| Contractor_Agreement_Assessment | A5 | Keep headers visible |
| Gap_Analysis | A5 | Keep headers visible |
| Evidence_Register | A5 | Keep headers visible |
| Approval_Sign_Off | A3 | Keep title visible |

---

### 9.10 Print Settings

All sheets: Landscape, fit 1 page wide × auto tall, narrow margins (0.5"), header (sheet name + date), footer (page X of Y + filename), repeat row 4 on every page for tabular sheets.

**Special:** Sheet 6 header includes "INTERNAL — CONTAINS HR AND DEPARTURE DATA"

---

### 9.11 Python Script Generation

**Script:** `generate_a5_1_2_6_1_2_s4_employment_contract.py`

**Execution:**
```bash
python generate_a5_1_2_6_1_2_s4_employment_contract.py
```

**Output:** `ISMS-IMP-A.5.1-2-6.1-2.S4_Employment_Contract_20260130.xlsx`

---

**[END OF PART II: TECHNICAL SPECIFICATION]**

---

**Document Summary:**
- **Part I: User Guide** (~900 lines)
- **Part II: Technical Specification** (~500 lines)
- **Total:** ~1,600 lines

**Key Differentiators from .S1–.S3:**
- **Linked control coverage**: Assesses both A.6.2 (contract content) and A.6.5 (post-termination obligations) — the only assessment in the stacked framework covering two distinct ISO controls
- **Template-first approach**: Starts at the template level before drilling to individual level — fixes at the template propagate to all future hires
- **Two-section Sheet 6**: Current employees (clause verification) and former employees (obligation enforcement) in one sheet — provides the complete lifecycle view
- **Contractor/vendor DPA assessment**: Sheet 7 bridges A.6.2 employment contracts with third-party processor obligations (FADP Art. 9)
- **NDA as audit focal point**: Explicit guidance that NDAs are the most auditable element — prioritizes evidence accessibility for this clause type

**Next Steps:**
1. Review and approve this specification
2. Proceed to: ISMS-IMP-A.5.1-2-6.1-2.S5 (Governance Compliance Dashboard)

---

**END OF SPECIFICATION**

---

*"A verbal contract isn't worth the paper it's written on."*
— Samuel Goldwyn

<!-- QA_VERIFIED: 2026-02-01 -->
