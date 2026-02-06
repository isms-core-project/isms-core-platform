# ISMS-IMP-A.5.12-13.S1 - Classification Scheme Definition

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.12-13.S1 |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.12 Classification of Information |
| **Parent Policy** | ISMS-POL-A.5.12-13 - Information Classification and Labelling |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Workbook Structure](#14-workbook-structure)
   - [1.5 Completion Walkthrough](#15-completion-walkthrough)
   - [1.6 Evidence Collection](#16-evidence-collection)
   - [1.7 Common Pitfalls](#17-common-pitfalls)
   - [1.8 Quality Checklist](#18-quality-checklist)
   - [1.9 Review and Approval](#19-review-and-approval)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Technical Details](#21-workbook-technical-details)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Conditional Formatting](#23-conditional-formatting)
   - [2.4 Integration Points](#24-integration-points)
   - [2.5 Related Documents](#25-related-documents)

---

# PART I: USER COMPLETION GUIDE

---

## 1.1 Assessment Overview

### Purpose

This workbook establishes the organisation's information classification scheme as required by ISO 27001:2022 Control A.5.12. The classification scheme enables appropriate protection of information based on its sensitivity, value, criticality, and legal/regulatory requirements.

The assessment serves multiple purposes:
- **Define**: Establish clear classification levels with unambiguous definitions
- **Standardise**: Create consistent handling requirements across the organisation
- **Map**: Align classification levels with confidentiality, integrity, and availability (CIA) requirements
- **Comply**: Meet regulatory requirements for data categorisation
- **Enable**: Support access control, DLP, and data protection decisions

### Scope

The Classification Scheme Definition Assessment covers:

| Area | Coverage | Key Decisions |
|------|----------|---------------|
| **Classification Levels** | Four-tier scheme (Public to Restricted) | Level names, definitions, examples |
| **Handling Requirements** | Per-level security controls | Storage, transmission, disposal rules |
| **CIA Matrix** | Confidentiality, integrity, availability | Requirements per classification level |
| **Regulatory Mapping** | Legal and compliance alignment | Which regulations mandate which levels |
| **Governance** | Scheme ownership and review | Approval process, change management |

**Inclusions:**
- All information types created, processed, stored, or transmitted by the organisation
- Electronic, physical, and verbal information
- Internal and externally received information
- Aggregated information requiring elevated classification

**Exclusions:**
- Personal information held by employees for personal purposes
- Public information already in the public domain with no sensitivity
- Third-party classified information (apply their scheme or map to nearest higher level)

### Business Value

| Value Area | Benefit |
|------------|---------|
| **Risk Management** | Enables proportionate protection based on sensitivity |
| **Compliance** | Meets ISO 27001, GDPR, nDSG, FINMA data protection requirements |
| **Operational Efficiency** | Clear rules reduce uncertainty in handling decisions |
| **Audit Readiness** | Documented scheme supports Stage 1 and Stage 2 audits |
| **Cost Optimisation** | Avoids over-protection of low-sensitivity data |

### Assessment Frequency

| Assessment Type | Frequency | Trigger Events |
|-----------------|-----------|----------------|
| Full Scheme Review | Annual | Regulatory changes, business model changes |
| Handling Requirements Update | Annual | Technology changes, audit findings |
| CIA Matrix Review | Annual | Risk assessment updates |
| Ad-hoc Review | As needed | M&A activity, new regulations |

---

## 1.2 Control Requirements

### ISO 27001:2022 Control A.5.12

Per ISO/IEC 27001:2022 Control A.5.12:

> *"Information should be classified according to the information security needs of the organization based on confidentiality, integrity, availability and relevant interested party requirements."*

**Control Type:** Preventive
**Security Properties:** Confidentiality, Integrity, Availability
**Cybersecurity Concepts:** Identify, Protect
**Operational Capabilities:** Asset Management, Information Protection

### Key Control Objectives

| Objective | Description |
|-----------|-------------|
| **Consistency** | Ensure uniform classification across the organisation |
| **Appropriateness** | Match protection to actual sensitivity |
| **Legal Compliance** | Meet regulatory data categorisation requirements |
| **Decision Support** | Enable handling decisions based on classification |
| **Lifecycle Coverage** | Address classification from creation to disposal |

### What Auditors Look For

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Scheme Existence** | Documented classification scheme with defined levels |
| **Clear Definitions** | Unambiguous criteria for each classification level |
| **CIA Alignment** | Classification linked to confidentiality, integrity, availability |
| **Regulatory Mapping** | Legal requirements mapped to classification levels |
| **Handling Requirements** | Per-level security controls documented |
| **Governance** | Approval records, review schedule, scheme ownership |

---

## 1.3 Prerequisites

### Required Access

| System | Purpose | Access Level Needed |
|--------|---------|---------------------|
| Policy Repository | Review existing policies | Read access |
| Asset Inventory | Understand information types | Read access |
| Regulatory Register | Map compliance requirements | Read access |
| Risk Register | Align with risk assessment | Read access |

### Required Documents

- [ ] ISMS-POL-A.5.12-13 - Information Classification and Labelling (approved)
- [ ] Current asset inventory (ISMS-POL-A.5.9 output)
- [ ] Regulatory applicability framework (ISMS-POL-00)
- [ ] Risk assessment results
- [ ] Existing classification scheme (if any)
- [ ] Industry classification standards (for reference)

### Required Personnel

| Role | Responsibility | Time Commitment |
|------|----------------|-----------------|
| **Assessment Lead** | Coordinate scheme definition | 8-12 hours |
| **CISO** | Approve scheme, define handling requirements | 4-6 hours |
| **DPO** | Regulatory alignment, personal data requirements | 4-6 hours |
| **Legal Counsel** | Regulatory requirements, contractual obligations | 2-4 hours |
| **Business Unit Representatives** | Validate practical applicability | 2-3 hours each |

---

## 1.4 Workbook Structure

### Sheet Overview

| Sheet | Purpose | Assessor Action |
|-------|---------|-----------------|
| **Instructions** | Guidance and methodology | Read before starting |
| **Classification_Levels** | Define classification tiers | Complete level definitions |
| **Handling_Requirements** | Security controls per level | Specify required controls |
| **CIA_Matrix** | CIA requirements per level | Define CIA requirements |
| **Regulatory_Mapping** | Legal requirements mapping | Map regulations to levels |
| **Evidence_Register** | Audit evidence tracking | Document evidence sources |
| **Approval_SignOff** | Scheme authorisation | Obtain signatures |

### Data Flow

```
Regulatory Requirements ─────────► Classification_Levels
        │                                  │
        ▼                                  ▼
Risk Assessment ──────────────► Handling_Requirements
        │                                  │
        ▼                                  ▼
Business Requirements ────────► CIA_Matrix
                                          │
                                          ▼
                              Regulatory_Mapping
                                          │
                                          ▼
                              Evidence_Register
                                          │
                                          ▼
                              Approval_SignOff
```

---

## 1.5 Completion Walkthrough

### Step 1: Define Classification Levels

**Time allocation:** 3-4 hours

**Purpose:** Establish the organisation's classification tiers with clear definitions.

**Fields to Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| Level_ID | Unique identifier | L4, L3, L2, L1 |
| Level_Name | Classification name | RESTRICTED, CONFIDENTIAL, INTERNAL, PUBLIC |
| Display_Label | Visual indicator | RESTRICTED |
| Color_Code | Hex colour for visual identification | #FF6B6B |
| Description | Clear definition of what qualifies | Highly sensitive information requiring strictest controls |
| Impact_if_Disclosed | Consequence of unauthorised disclosure | Severe damage, regulatory penalties, existential threat |
| Examples | Common information types | Trade secrets, M&A data, cryptographic keys |
| Default_Retention | Standard retention period | 7 years |
| Review_Frequency | How often to review classification | Annual |
| Owner_Approval | Approval required to classify at this level | Yes - Executive |

**Standard Four-Tier Scheme:**

| Level | Name | Description | Examples |
|-------|------|-------------|----------|
| L4 | RESTRICTED | Highly sensitive, strictest controls, severe impact if disclosed | Trade secrets, M&A data, security configs, cryptographic keys |
| L3 | CONFIDENTIAL | Sensitive business information, significant impact | Customer data, contracts, financial reports, HR records |
| L2 | INTERNAL | Internal use only, minor impact if disclosed | Policies, procedures, org charts, internal communications |
| L1 | PUBLIC | Approved for unrestricted distribution | Marketing materials, public website, press releases |

**Decision Criteria:**
- What is the impact if this information is disclosed to unauthorised parties?
- What regulatory requirements apply to this information type?
- What is the business value of this information?
- Does aggregation with other information increase sensitivity?

### Step 2: Define Handling Requirements

**Time allocation:** 3-4 hours

**Purpose:** Specify security controls required for each classification level.

**Categories to Complete:**

| Category | RESTRICTED | CONFIDENTIAL | INTERNAL | PUBLIC |
|----------|------------|--------------|----------|--------|
| **Access Control** | Need-to-know, MFA required | Role-based, approval required | Department-based | Unrestricted |
| **Storage** | Encrypted (AES-256), access-logged | Encrypted (AES-256) | Corporate systems | Any |
| **Transmission** | Encrypted channel required | Encrypted preferred | Corporate email | Standard |
| **Printing** | Secure print only | Track copies | Normal | Normal |
| **Disposal** | Shredding (P-5) + witness | Shredding (P-4) | Shredding (P-3) | Recycling OK |
| **External Sharing** | Prohibited without GL approval | NDA required | Discretion | Permitted |
| **Labelling** | Mandatory, header/footer/watermark | Mandatory, header/footer | Footer recommended | Optional |

**For Each Handling Category:**
1. Define the requirement for RESTRICTED level (most stringent)
2. Define relaxed requirements for lower levels
3. Ensure requirements are technically achievable
4. Document any exceptions or special cases

### Step 3: Complete CIA Matrix

**Time allocation:** 2-3 hours

**Purpose:** Define confidentiality, integrity, and availability requirements per classification level.

**Confidentiality Requirements:**

| Level | Access Control | Encryption | Disclosure Impact | Monitoring |
|-------|---------------|------------|-------------------|------------|
| RESTRICTED | Need-to-know, MFA | AES-256 rest and transit | Severe - regulatory/legal | Real-time alerting |
| CONFIDENTIAL | Role-based, approval | AES-256 required | Significant - business impact | Daily review |
| INTERNAL | Department-based | Recommended | Minor - operational | Weekly review |
| PUBLIC | Unrestricted | Optional | None expected | None required |

**Integrity Requirements:**

| Level | Change Control | Version Control | Modification Impact | Validation |
|-------|---------------|-----------------|---------------------|------------|
| RESTRICTED | Dual approval | Full audit trail | Severe - legal issues | Digital signatures |
| CONFIDENTIAL | Manager approval | Version history | Significant - incorrect decisions | Checksums |
| INTERNAL | Owner approval | Recommended | Minor - process delays | Spot checks |
| PUBLIC | Standard process | Optional | Minimal | None required |

**Availability Requirements:**

| Level | Recovery Time | Backup Frequency | Unavailability Impact | Redundancy |
|-------|--------------|------------------|----------------------|------------|
| RESTRICTED | < 4 hours | Real-time/Hourly | Critical - operations halt | Active-active |
| CONFIDENTIAL | < 24 hours | Daily | Significant - major delays | Active-passive |
| INTERNAL | < 72 hours | Daily | Minor - workarounds exist | Standard backup |
| PUBLIC | Best effort | Weekly | Minimal | Basic backup |

### Step 4: Map Regulatory Requirements

**Time allocation:** 2-3 hours

**Purpose:** Align classification levels with legal and regulatory requirements.

**Mapping Process:**
1. List all applicable regulations from ISMS-POL-00
2. Identify data types covered by each regulation
3. Determine minimum classification level per data type
4. Document special handling requirements
5. Record retention requirements

**Example Regulatory Mapping:**

| Regulation | Data Types Covered | Minimum Classification | Special Handling | Retention |
|------------|-------------------|------------------------|------------------|-----------|
| GDPR Art. 32 | Personal data | CONFIDENTIAL | Pseudonymisation where possible | Per Art. 17 |
| GDPR Art. 9 | Special category data | RESTRICTED | Explicit consent required | Per Art. 17 |
| Swiss nDSG Art. 8 | Personal data (CH) | CONFIDENTIAL | Appropriate measures | Purpose-based |
| PCI DSS | Cardholder data | RESTRICTED | PCI controls required | Per PCI standards |
| SOX | Financial records | CONFIDENTIAL | Audit trail required | 7 years |
| Trade Secrets | Proprietary information | RESTRICTED | NDA required | Indefinite |

### Step 5: Document Evidence

**Time allocation:** 1-2 hours

**Purpose:** Track evidence supporting the classification scheme.

**Evidence Types:**

| Evidence Type | Description | Example |
|---------------|-------------|---------|
| Policy document | Approved classification policy | ISMS-POL-A.5.12-13 |
| Regulatory analysis | Mapping to legal requirements | Regulatory mapping worksheet |
| Stakeholder input | Business unit feedback | Meeting minutes, emails |
| Industry benchmarks | Reference to standards | ISO 27002, government schemes |
| Approval records | Scheme approval documentation | Signed approval sheet |
| Training materials | User guidance on classification | Classification quick reference |

### Step 6: Obtain Approvals

**Time allocation:** 1-2 hours

**Purpose:** Secure formal approval for the classification scheme.

**Required Approvals:**

| Approver | What They Approve | Criteria |
|----------|-------------------|----------|
| **CISO** | Technical adequacy, handling requirements | Controls appropriate for risk |
| **DPO** | Regulatory alignment | Meets data protection requirements |
| **Legal** | Legal compliance | Meets contractual obligations |
| **CIO** | Technical feasibility | Controls can be implemented |
| **Executive Management** | Business alignment | Scheme supports business needs |

---

## 1.6 Evidence Collection

### Evidence Requirements

| Evidence Type | Source | Retention |
|---------------|--------|-----------|
| This assessment workbook | Generated | 7 years |
| Policy document (ISMS-POL-A.5.12-13) | Policy repository | Duration + 2 years |
| Regulatory mapping analysis | This workbook | 7 years |
| Approval signatures | This workbook | Duration + 2 years |
| Stakeholder feedback | Meeting minutes | 3 years |
| Scheme review records | Annual reviews | 3 years |

### Evidence Storage

**Primary Location:** `[SharePoint/Evidence Library]/A.5.12-13/Classification-Scheme/[Year]/`

**Folder Structure:**
```
A.5.12-13/
|-- Classification-Scheme/
|   |-- 2026/
|   |   |-- Assessment-Workbooks/
|   |   |   |-- ISMS-IMP-A.5.12-13.S1_Classification_Scheme_20260204.xlsx
|   |   |-- Evidence/
|   |   |   |-- Regulatory-Analysis/
|   |   |   |-- Stakeholder-Feedback/
|   |   |   |-- Approvals/
|   |   |   |   |-- CISO-Approval-20260204.pdf
|   |   |   |   |-- Executive-Approval-20260204.pdf
```

**Naming Convention:**
```
EVD-A.5.12-13.1_[EvidenceType]_[YYYYMMDD].[ext]
```

---

## 1.7 Common Pitfalls

Avoid these common mistakes when defining the classification scheme:

### Scheme Design Pitfalls

❌ **MISTAKE**: Creating too many classification levels (5+ levels creates confusion)
✅ **CORRECT**: Use 4-tier scheme aligned with ISO 27002 guidance; sub-categories if needed

❌ **MISTAKE**: Vague level definitions like "moderately sensitive"
✅ **CORRECT**: Use concrete criteria: impact if disclosed, regulatory triggers, examples

❌ **MISTAKE**: Classification levels not aligned with handling capabilities
✅ **CORRECT**: Ensure each level's controls are technically implementable

❌ **MISTAKE**: Forgetting aggregation effects (multiple INTERNAL items = CONFIDENTIAL together)
✅ **CORRECT**: Include aggregation guidance in scheme documentation

### Handling Requirements Pitfalls

❌ **MISTAKE**: Requiring controls that don't exist in the environment
✅ **CORRECT**: Validate all handling requirements are technically feasible

❌ **MISTAKE**: Identical handling requirements across multiple levels
✅ **CORRECT**: Each level should have distinct, proportionate controls

❌ **MISTAKE**: Missing disposal requirements for physical media
✅ **CORRECT**: Address physical handling (paper, media, devices) not just digital

### Regulatory Mapping Pitfalls

❌ **MISTAKE**: Assuming all personal data requires RESTRICTED classification
✅ **CORRECT**: CONFIDENTIAL for standard personal data; RESTRICTED for special categories

❌ **MISTAKE**: Single regulation drives entire scheme (e.g., "everything is GDPR")
✅ **CORRECT**: Map multiple regulations; use most stringent requirement per data type

❌ **MISTAKE**: Forgetting contractual classification requirements (NDAs, customer requirements)
✅ **CORRECT**: Include contractual obligations in regulatory mapping

### Governance Pitfalls

❌ **MISTAKE**: No defined scheme owner or review schedule
✅ **CORRECT**: Assign clear ownership; schedule annual review minimum

❌ **MISTAKE**: Approval only from IT/security without business input
✅ **CORRECT**: Include business unit representatives in approval process

---

## 1.8 Quality Checklist

Before submitting the assessment, verify:

### Scheme Completeness Checks

- [ ] All four classification levels fully defined
- [ ] Each level has clear, unambiguous definition
- [ ] Examples provided for each classification level
- [ ] Impact criteria documented for classification decisions
- [ ] Default classification defined (INTERNAL until formally classified)

### Handling Requirements Checks

- [ ] All handling categories addressed (access, storage, transmission, disposal, sharing)
- [ ] Requirements differ appropriately between levels
- [ ] All requirements are technically achievable
- [ ] Physical and digital handling both addressed
- [ ] External sharing rules clear for each level

### CIA Matrix Checks

- [ ] Confidentiality requirements defined per level
- [ ] Integrity requirements defined per level
- [ ] Availability requirements defined per level
- [ ] Requirements align with risk assessment
- [ ] Recovery times realistic and achievable

### Regulatory Mapping Checks

- [ ] All applicable regulations identified
- [ ] Data types mapped to minimum classification levels
- [ ] Special handling requirements documented
- [ ] Retention requirements included
- [ ] Mapping reviewed by Legal/DPO

### Approval Readiness Checks

- [ ] All mandatory fields completed
- [ ] Evidence register populated
- [ ] Stakeholder review completed
- [ ] Documentation ready for signature

---

## 1.9 Review and Approval

### Review Workflow

```
Assessment Lead Completes Scheme Definition
        │
        ▼
Legal/DPO Review (Regulatory Alignment)
        │
        ▼
Business Unit Review (Practical Applicability)
        │
        ▼
IT Review (Technical Feasibility)
        │
        ▼
CISO Review (Security Adequacy)
        │
        ▼
Executive Approval
        │
        ▼
Scheme Published
        │
        ▼
Upload to ISMS Evidence Library
```

### Approval Signatures

The Approval_SignOff sheet requires:

1. **Assessment Lead Certification:**
   - Confirms methodology was followed
   - Confirms all elements complete
   - Date and signature

2. **DPO Validation:**
   - Confirms regulatory alignment
   - Confirms personal data classification adequate
   - Date and signature

3. **CISO Review:**
   - Confirms security controls appropriate
   - Confirms handling requirements adequate
   - Date and signature

4. **Executive Approval:**
   - Approves scheme for organisation-wide use
   - Authorises implementation
   - Date and signature

---

# PART II: TECHNICAL SPECIFICATION

---

## 2.1 Workbook Technical Details

### File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.12-13.S1_Classification_Scheme_Definition_YYYYMMDD.xlsx` |
| Generator | `generate_a512_13_1_classification_scheme.py` |
| Sheets | 7 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 8 |
| 2 | Classification_Levels | Level definitions | 20 | 10 |
| 3 | Handling_Requirements | Per-level controls | 30 | 5 |
| 4 | CIA_Matrix | CIA requirements | 30 | 5 |
| 5 | Regulatory_Mapping | Legal alignment | 30 | 7 |
| 6 | Evidence_Register | Audit evidence | 30 | 8 |
| 7 | Approval_SignOff | Authorisation | 20 | 6 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

| Row | Content | Purpose |
|-----|---------|---------|
| 1 | Title (merged A1:H1) | Document identification |
| 3-10 | Purpose and principles | Methodology guidance |
| 12-20 | Standard classification levels | Quick reference |
| 22-30 | How to use instructions | Step-by-step guidance |
| 32-40 | Key stakeholders | Role descriptions |

### Sheet 2: Classification_Levels

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Level_ID | 10 | Text | L1, L2, L3, L4 |
| B | Level_Name | 15 | Text | Required |
| C | Display_Label | 18 | Text | Visual format |
| D | Color_Code | 12 | Text | Hex colour |
| E | Description | 45 | Text | Required |
| F | Impact_if_Disclosed | 45 | Text | Required |
| G | Examples | 50 | Text | Required |
| H | Default_Retention | 15 | Text | None |
| I | Review_Frequency | 15 | List | Annual, Biennial, Triennial |
| J | Owner_Approval_Required | 20 | List | Yes - Executive, Yes - Manager, Yes - Owner, No |

### Sheet 3: Handling_Requirements

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Requirement_Category | 25 | Text | Pre-populated |
| B | RESTRICTED | 25 | Text | Input |
| C | CONFIDENTIAL | 25 | Text | Input |
| D | INTERNAL | 25 | Text | Input |
| E | PUBLIC | 25 | Text | Input |

**Pre-populated Categories:**
- Access Control (Need-to-know basis, Access approval, Access logging, Access review frequency)
- Storage (Encryption at rest, Storage location, Personal device storage, Cloud storage)
- Transmission (Encryption in transit, Email transmission, External sharing)
- Physical Handling (Printing, Clean desk, Secure disposal)
- Labelling (Document marking, Metadata tagging, Visual indicators)

### Sheet 4: CIA_Matrix

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Level | 15 | Text | Pre-populated |
| B | Access_Control | 25 | Text | Input |
| C | Encryption | 25 | Text | Input |
| D | Impact | 25 | Text | Input |
| E | Monitoring | 20 | Text | Input |

**Sections:**
- Confidentiality Requirements (rows 5-9)
- Integrity Requirements (rows 13-17)
- Availability Requirements (rows 21-25)

### Sheet 5: Regulatory_Mapping

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Regulation | 18 | Text | Input |
| B | Requirement | 25 | Text | Input |
| C | Data_Types_Covered | 25 | Text | Input |
| D | Min_Classification | 18 | List | RESTRICTED, CONFIDENTIAL, INTERNAL, PUBLIC |
| E | Special_Handling | 30 | Text | Input |
| F | Retention | 18 | Text | Input |
| G | Status | 18 | List | Compliant, Partial, Non-Compliant, N/A |

### Sheet 6: Evidence_Register

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Evidence_ID | 15 | Text | None |
| B | Description | 40 | Text | None |
| C | Evidence_Type | 20 | List | Policy document, Procedure, Configuration, Screenshot, Training record, Audit report, Other |
| D | Related_Requirement | 25 | Text | None |
| E | Location | 30 | Text | None |
| F | Collected_Date | 15 | Date | None |
| G | Collected_By | 15 | Text | None |
| H | Verification_Status | 18 | List | Verified, Pending Review, Not Verified, Expired |

### Sheet 7: Approval_SignOff

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Role | 35 | Text | Pre-populated |
| B | Name | 25 | Text | Input |
| C | Signature | 20 | Text | Input |
| D | Date | 15 | Date | Input |
| E | Decision | 22 | List | Approved, Approved with conditions, Rejected, Pending |
| F | Comments | 30 | Text | Input |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| Classification_Levels | B:B | ="RESTRICTED" | Red fill (#FF6B6B), White bold text |
| Classification_Levels | B:B | ="CONFIDENTIAL" | Orange fill (#FFA94D), Bold |
| Classification_Levels | B:B | ="INTERNAL" | Green fill (#69DB7C), Bold |
| Classification_Levels | B:B | ="PUBLIC" | Blue fill (#74C0FC), Bold |
| Handling_Requirements | B:B | Category headers (uppercase) | Bold |
| Regulatory_Mapping | G:G | ="Compliant" | Green fill (#C6EFCE) |
| Regulatory_Mapping | G:G | ="Partial" | Yellow fill (#FFEB9C) |
| Regulatory_Mapping | G:G | ="Non-Compliant" | Red fill (#FFC7CE) |
| Evidence_Register | H:H | ="Verified" | Green fill (#C6EFCE) |
| Evidence_Register | H:H | ="Pending Review" | Yellow fill (#FFEB9C) |
| Evidence_Register | H:H | ="Not Verified" | Red fill (#FFC7CE) |
| Approval_SignOff | E:E | ="Approved" | Green fill (#C6EFCE) |
| Approval_SignOff | E:E | ="Rejected" | Red fill (#FFC7CE) |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| ISMS-POL-A.5.12-13 | Policy requirements | Policy -> This workbook |
| Asset Inventory (A.5.9) | Information types | A.5.9 -> Examples/coverage |
| Regulatory Register | Compliance requirements | ISMS-POL-00 -> Regulatory_Mapping |
| A.5.12-13.2 Workbook | Labelling procedures | This workbook -> Labelling |
| A.5.12-13.3 Workbook | Asset classification | This workbook -> Asset inventory |
| A.5.12-13.4 Workbook | Compliance monitoring | This workbook -> Compliance |
| DLP Tools | Classification enforcement | This workbook -> DLP configuration |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.12-13 | Information Classification and Labelling | Parent policy |
| ISMS-IMP-A.5.12-13.S2 | Labelling Procedures and Standards | Labelling implementation |
| ISMS-IMP-A.5.12-13.S3 | Asset Classification Inventory | Asset tracking |
| ISMS-IMP-A.5.12-13.S4 | Compliance Dashboard | Compliance monitoring |
| ISMS-IMP-A.5.12-13.S5 | Consolidation Dashboard | Executive view |
| ISMS-POL-A.5.9 | Inventory of Information and Assets | Asset source |
| ISMS-POL-A.8.12 | Data Leakage Prevention | DLP enforcement |
| ISMS-POL-A.8.24 | Use of Cryptography | Encryption requirements |

---

**END OF SPECIFICATION**

---

*"Information is the oil of the 21st century, and analytics is the combustion engine."*
— Peter Sondergaard

<!-- QA_VERIFIED: 2026-02-04 -->
