# ISMS-IMP-A.5.12-13.S2 - Labelling Procedures and Standards

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.12-13.S2 |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.13 Labelling of Information |
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

This workbook defines the organisation's information labelling procedures and standards as required by ISO 27001:2022 Control A.5.13. Labelling ensures that classification is clearly communicated through visual markers, metadata, and physical identifiers.

The assessment serves multiple purposes:
- **Standardise**: Define consistent labelling formats across all information types
- **Enable Recognition**: Create easily recognisable visual indicators
- **Support Automation**: Enable automated processing through metadata
- **Ensure Compliance**: Meet regulatory requirements for data marking
- **Facilitate Handling**: Enable appropriate handling based on visible classification

### Scope

The Labelling Procedures Assessment covers:

| Labelling Domain | Coverage | Key Standards |
|------------------|----------|---------------|
| **Visual Standards** | Colours, fonts, banners | Display text, colour codes, icons |
| **Digital Labelling** | Electronic documents and data | Metadata, properties, headers/footers |
| **Physical Labelling** | Paper and removable media | Stamps, stickers, printed labels |
| **Automation Tools** | Software solutions | Microsoft Purview, DLP integration |
| **Procedures** | Labelling workflows | When, how, and who labels |

**Inclusions:**
- All electronic document types (Office, PDF, email, databases)
- Physical documents (paper, reports, folders)
- Removable media (USB, external drives, backup tapes)
- Communication channels (email headers, API responses)
- Storage containers (file folders, archive boxes)

**Exclusions:**
- Third-party systems where labelling is infeasible (document with compensating controls)
- Encrypted data where labelling would compromise security (document rationale)
- Public information where labelling adds no value (optional per policy)

### Business Value

| Value Area | Benefit |
|------------|---------|
| **Clear Communication** | Classification visible to all handlers |
| **Automated Enforcement** | DLP and access control based on metadata |
| **Audit Compliance** | Evidence of labelling implementation |
| **User Awareness** | Visual reminders of handling requirements |
| **Incident Prevention** | Clear marking reduces mishandling |

### Assessment Frequency

| Assessment Type | Frequency | Trigger Events |
|-----------------|-----------|----------------|
| Labelling Standards Review | Annual | Policy changes, tool updates |
| Digital Labelling Assessment | Quarterly | New applications, platform changes |
| Physical Labelling Review | Annual | Process changes |
| Automation Tools Evaluation | Annual | New solutions, licence renewals |

---

## 1.2 Control Requirements

### ISO 27001:2022 Control A.5.13

Per ISO/IEC 27001:2022 Control A.5.13:

> *"An appropriate set of procedures for information labelling should be developed and implemented in accordance with the information classification scheme adopted by the organization."*

**Control Type:** Preventive
**Security Properties:** Confidentiality
**Cybersecurity Concepts:** Identify, Protect
**Operational Capabilities:** Information Protection

### Key Control Objectives

| Objective | Description |
|-----------|-------------|
| **Visibility** | Labels clearly visible on all classified information |
| **Consistency** | Uniform labelling across all formats and systems |
| **Automation** | Metadata enables automated policy enforcement |
| **Usability** | Labels easily understood by all personnel |
| **Coverage** | All information types have appropriate labelling |

### What Auditors Look For

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Standards Existence** | Documented labelling standards per classification |
| **Digital Implementation** | Metadata and visual labels on electronic documents |
| **Physical Implementation** | Labels on paper documents and media |
| **Tool Deployment** | Automated labelling solutions in use |
| **Training** | Staff awareness of labelling requirements |
| **Monitoring** | Evidence of labelling compliance tracking |

---

## 1.3 Prerequisites

### Required Access

| System | Purpose | Access Level Needed |
|--------|---------|---------------------|
| Microsoft 365 Admin | Sensitivity label configuration | Admin or compliance role |
| Document Management | Document property configuration | Admin access |
| DLP Console | Label-based policy review | Security reader |
| Email System | Transport rules and headers | Admin access |

### Required Documents

- [ ] ISMS-IMP-A.5.12-13.S1 - Classification Scheme Definition (completed)
- [ ] ISMS-POL-A.5.12-13 - Information Classification and Labelling (approved)
- [ ] Current labelling tool inventory
- [ ] Brand guidelines (colours, fonts)
- [ ] Prior labelling assessments (if applicable)

### Required Personnel

| Role | Responsibility | Time Commitment |
|------|----------------|-----------------|
| **Assessment Lead** | Coordinate labelling standards | 8-10 hours |
| **IT Operations** | Digital labelling implementation | 6-8 hours |
| **Records Management** | Physical labelling standards | 4-6 hours |
| **Compliance Officer** | Regulatory alignment | 2-4 hours |
| **End Users (sample)** | Usability validation | 1-2 hours |

---

## 1.4 Workbook Structure

### Sheet Overview

| Sheet | Purpose | Assessor Action |
|-------|---------|-----------------|
| **Instructions** | Guidance and methodology | Read before starting |
| **Labelling_Standards** | Visual label formats per level | Define visual standards |
| **Digital_Labelling** | Electronic labelling requirements | Complete per asset type |
| **Physical_Labelling** | Paper and media labelling | Complete per asset type |
| **Automation_Tools** | Tool inventory and status | Document tool deployment |
| **Evidence_Register** | Audit evidence tracking | Document evidence sources |
| **Approval_SignOff** | Procedures authorisation | Obtain signatures |

### Data Flow

```
Classification_Scheme (A.5.12-13.1)
        │
        ▼
Labelling_Standards ────────► Visual format definitions
        │
        ├──────► Digital_Labelling
        │               │
        │               ▼
        │        Automation_Tools
        │
        └──────► Physical_Labelling
                        │
                        ▼
                Evidence_Register
                        │
                        ▼
                Approval_SignOff
```

---

## 1.5 Completion Walkthrough

### Step 1: Define Visual Labelling Standards

**Time allocation:** 2-3 hours

**Purpose:** Establish consistent visual indicators for each classification level.

**Fields to Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| Classification_Level | Level name | RESTRICTED |
| Display_Text | How label appears | RESTRICTED |
| Color_Hex | Colour code | #FF6B6B |
| Header_Format | Document header text | RESTRICTED - [Document Title] |
| Footer_Format | Document footer text | Classification: RESTRICTED \| Page X of Y \| [Date] |
| Watermark_Text | Watermark content | RESTRICTED - DO NOT DISTRIBUTE |
| Banner_Style | Visual banner description | Red banner, top and bottom |
| Icon_Symbol | Associated icon | Red circle or padlock |
| Font_Requirements | Text formatting | Bold, uppercase, red text |

**Standard Visual Elements:**

| Level | Colour | Banner | Watermark | Email Subject |
|-------|--------|--------|-----------|---------------|
| RESTRICTED | Red (#FF6B6B) | Red, top and bottom | RESTRICTED - DO NOT DISTRIBUTE | [RESTRICTED] |
| CONFIDENTIAL | Orange (#FFA94D) | Orange, top only | CONFIDENTIAL | [CONFIDENTIAL] |
| INTERNAL | Green (#69DB7C) | Green footer line | INTERNAL USE ONLY | [INTERNAL] (optional) |
| PUBLIC | Blue (#74C0FC) | Optional blue indicator | None required | None |

**Design Principles:**
- High contrast for visibility
- Consistent colour scheme across all applications
- Clear visual hierarchy (RESTRICTED most prominent)
- Accessible for colour-blind users (include text, not just colour)

### Step 2: Define Digital Labelling Requirements

**Time allocation:** 3-4 hours

**Purpose:** Specify labelling methods for each digital asset type.

**Digital Asset Types to Address:**

| Asset Type | Labelling Method | Metadata Fields | Automation |
|------------|------------------|-----------------|------------|
| **Microsoft Office Documents** | Document properties + Header/Footer | Classification, Author, Created, Modified, Keywords | Microsoft Purview (MIP) |
| **PDF Documents** | Document properties + Watermark | Classification, Creator, Custom metadata | Adobe Acrobat automation |
| **Emails** | X-headers + Visual banner + Subject prefix | X-Classification, X-Sensitivity, X-Retention | Exchange transport rules |
| **SharePoint/OneDrive** | Sensitivity labels + Metadata columns | Classification column, Retention label | Microsoft Purview |
| **Database Records** | Classification column + Row-level security | data_classification, sensitivity_level | Database triggers |
| **Source Code** | File headers + Repository metadata | Classification comment, .gitattributes | Pre-commit hooks |
| **Images/Media** | EXIF/XMP metadata + Visible watermark | Classification, Copyright, Creator | DAM system |
| **API Responses** | Response headers + Payload metadata | X-Data-Classification header | API gateway rules |

**For Each Asset Type Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| Asset_Type | Category of digital asset | Microsoft Office Documents |
| Labelling_Method | How label is applied | Document properties + Header/Footer |
| Metadata_Fields | Which metadata fields | Classification, Author, Created, Modified |
| Automation | Tool/method for auto-labelling | Microsoft Purview (MIP) |
| Validation | How to verify labelling | DLP policy check |
| Responsibility | Who is responsible | Document author |
| Implementation_Status | Current state | Implemented, In Progress, Not Implemented |

### Step 3: Define Physical Labelling Requirements

**Time allocation:** 2-3 hours

**Purpose:** Specify labelling methods for physical assets.

**Physical Asset Types to Address:**

| Asset Type | Labelling Method | Label Location | Durability |
|------------|------------------|----------------|------------|
| **Paper Documents** | Stamp + Header/Footer printing | Top right corner + Page footer | Indelible stamp ink |
| **Printed Reports** | Automatic header/footer + Cover page | Every page header + Report cover | Print-time application |
| **USB Drives** | Permanent label + Engraving | External surface visible | Tamper-evident label |
| **External Hard Drives** | Asset label + Classification sticker | Top surface + Visible when stored | Durable adhesive label |
| **Backup Tapes** | Barcode label + Classification indicator | Spine and front face | Tape-specific labels |
| **CD/DVD Media** | Permanent marker + Printed label | Top surface (non-data side) | CD-safe permanent marker |
| **File Folders** | Tab label + Cover stamp | Tab edge + Front cover | Adhesive label or stamp |
| **Storage Boxes** | Box label + Seal | Front and top of box | Weatherproof label |

**For Each Physical Asset Type Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| Asset_Type | Category of physical asset | Paper Documents |
| Labelling_Method | How label is applied | Stamp + Header/Footer printing |
| Label_Location | Where label appears | Top right corner + Page footer |
| Label_Format | Content of label | Classification level + Date + Page number |
| Durability | Label permanence | Indelible stamp ink |
| Responsible_Party | Who applies label | Document creator |
| Implementation_Status | Current state | Implemented |

### Step 4: Document Automation Tools

**Time allocation:** 2-3 hours

**Purpose:** Inventory and assess labelling automation solutions.

**Common Labelling Tools:**

| Tool | Vendor | Scope | Key Features |
|------|--------|-------|--------------|
| **Microsoft Purview** | Microsoft | M365, Azure, Windows | Sensitivity labels, Auto-labelling, DLP |
| **Titus Classification Suite** | HelpSystems | Cross-platform documents | User-driven + automated, Visual marking |
| **Boldon James Classifier** | GRCI Group | Enterprise documents | Policy-based, Watermarking, Metadata |
| **Varonis Data Classification** | Varonis | File servers, cloud | Content inspection, Sensitive data discovery |
| **Digital Guardian** | Fortra | Endpoints, network, cloud | Data discovery, Classification, DLP |
| **Custom Scripts** | Internal | Specific use cases | PowerShell, Python automation |

**For Each Tool Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| Tool_Name | Solution name | Microsoft Purview Information Protection |
| Vendor | Provider | Microsoft |
| Scope_Coverage | What it covers | M365, Azure, Windows endpoints |
| Key_Features | Main capabilities | Sensitivity labels, Auto-labelling, DLP integration |
| Integration_Points | System connections | M365, SharePoint, Exchange, Teams |
| Licence_Type | Licensing model | M365 E5 / EMS E5 |
| Implementation_Status | Deployment state | Deployed, Pilot, Evaluating, Not Implemented |
| Owner | Responsible team | IT Security |

### Step 5: Document Evidence

**Time allocation:** 1-2 hours

**Purpose:** Track evidence supporting labelling procedures implementation.

**Evidence Types:**

| Evidence Type | Description | Example |
|---------------|-------------|---------|
| Procedure document | Labelling procedures | Labelling SOP |
| Configuration screenshot | Tool configuration | MIP sensitivity label settings |
| Label sample | Example of labelled document | Sample CONFIDENTIAL document |
| Training record | User training | Classification training completion |
| Tool export | Automated labelling report | MIP labelling activity report |
| Audit report | Compliance assessment | Labelling audit findings |

### Step 6: Obtain Approvals

**Time allocation:** 1-2 hours

**Purpose:** Secure formal approval for labelling procedures.

**Required Approvals:**

| Approver | What They Approve | Criteria |
|----------|-------------------|----------|
| **CISO** | Security adequacy | Procedures support classification scheme |
| **IT Operations Manager** | Technical feasibility | Procedures can be implemented |
| **Records Management Lead** | Physical labelling | Procedures meet records requirements |
| **Compliance Officer** | Regulatory alignment | Procedures meet legal requirements |

---

## 1.6 Evidence Collection

### Evidence Requirements

| Evidence Type | Source | Retention |
|---------------|--------|-----------|
| This assessment workbook | Generated | 7 years |
| Labelling standards document | This workbook | Duration + 2 years |
| Tool configuration exports | Various tools | 3 years |
| Sample labelled documents | Various sources | Current version |
| Training completion records | LMS | Duration + 2 years |
| Labelling audit reports | Internal audit | 3 years |

### Evidence Storage

**Primary Location:** `[SharePoint/Evidence Library]/A.5.12-13/Labelling-Procedures/[Year]/`

**Folder Structure:**
```
A.5.12-13/
|-- Labelling-Procedures/
|   |-- 2026/
|   |   |-- Assessment-Workbooks/
|   |   |   |-- ISMS-IMP-A.5.12-13.S2_Labelling_Procedures_20260204.xlsx
|   |   |-- Evidence/
|   |   |   |-- Standards/
|   |   |   |   |-- Visual-Labelling-Standards.pdf
|   |   |   |-- Digital-Labelling/
|   |   |   |   |-- MIP-Configuration-Export.pdf
|   |   |   |   |-- Sample-CONFIDENTIAL-Document.docx
|   |   |   |-- Physical-Labelling/
|   |   |   |   |-- Label-Templates.pdf
|   |   |   |-- Tools/
|   |   |   |   |-- Tool-Inventory.xlsx
|   |   |   |-- Approvals/
```

---

## 1.7 Common Pitfalls

Avoid these common mistakes when defining labelling procedures:

### Visual Standards Pitfalls

❌ **MISTAKE**: Using colour only to indicate classification (accessibility issue)
✅ **CORRECT**: Always include text with colour; design for colour-blind users

❌ **MISTAKE**: Inconsistent colours across applications (red in Word, orange in email)
✅ **CORRECT**: Define exact hex codes and enforce consistently across all platforms

❌ **MISTAKE**: Labels too small or low contrast to be easily visible
✅ **CORRECT**: Ensure labels are prominent and readable in all viewing conditions

❌ **MISTAKE**: Different label formats for same classification level across documents
✅ **CORRECT**: Standardise format: "Classification: CONFIDENTIAL | Page X of Y"

### Digital Labelling Pitfalls

❌ **MISTAKE**: Relying only on visible labels without metadata
✅ **CORRECT**: Always set metadata properties for automated processing

❌ **MISTAKE**: Assuming sensitivity labels cascade to all file types
✅ **CORRECT**: Verify labelling works for each file type (some may not support metadata)

❌ **MISTAKE**: Not labelling emails with sensitive attachments
✅ **CORRECT**: Email classification should reflect highest classification of content including attachments

❌ **MISTAKE**: Forgetting database record-level classification
✅ **CORRECT**: Include database classification columns and row-level security

### Physical Labelling Pitfalls

❌ **MISTAKE**: Labels that can be easily removed or fall off
✅ **CORRECT**: Use tamper-evident or permanent labels for sensitive materials

❌ **MISTAKE**: Only labelling cover page, not each page
✅ **CORRECT**: Every page should have classification visible

❌ **MISTAKE**: Using erasable markers on removable media
✅ **CORRECT**: Use permanent markers or engraved labels

### Automation Pitfalls

❌ **MISTAKE**: Deploying auto-classification without user override option
✅ **CORRECT**: Allow users to upgrade (but not downgrade without approval) auto-applied labels

❌ **MISTAKE**: Not training users on manual labelling when automation fails
✅ **CORRECT**: Ensure users can manually apply labels when automation is unavailable

---

## 1.8 Quality Checklist

Before submitting the assessment, verify:

### Visual Standards Checks

- [ ] All four classification levels have defined visual standards
- [ ] Colour codes specified (hex values)
- [ ] Header, footer, and watermark formats defined
- [ ] Accessibility considered (not colour-only)
- [ ] Standards documented for print and screen

### Digital Labelling Checks

- [ ] All digital asset types addressed
- [ ] Metadata fields specified per asset type
- [ ] Automation tools identified where applicable
- [ ] Validation methods defined
- [ ] Responsibilities assigned

### Physical Labelling Checks

- [ ] All physical asset types addressed
- [ ] Label formats and locations specified
- [ ] Durability requirements defined
- [ ] Responsibilities assigned
- [ ] Labels available (stamps, stickers, templates)

### Automation Tool Checks

- [ ] All deployed tools documented
- [ ] Implementation status accurate
- [ ] Integration points identified
- [ ] Gaps in automation coverage noted
- [ ] Owners assigned

### Approval Readiness Checks

- [ ] All mandatory fields completed
- [ ] Evidence register populated
- [ ] Sample labels prepared for review
- [ ] Documentation ready for signature

---

## 1.9 Review and Approval

### Review Workflow

```
Assessment Lead Completes Procedures
        │
        ▼
IT Operations Review (Technical Feasibility)
        │
        ▼
Records Management Review (Physical Labelling)
        │
        ▼
End User Validation (Usability)
        │
        ▼
Compliance Review (Regulatory Alignment)
        │
        ▼
CISO Approval
        │
        ▼
Procedures Published
```

### Approval Signatures

The Approval_SignOff sheet requires:

1. **Assessment Lead Certification:**
   - Confirms methodology was followed
   - Confirms all asset types covered
   - Date and signature

2. **IT Operations Validation:**
   - Confirms digital labelling achievable
   - Confirms tool capabilities verified
   - Date and signature

3. **Records Management Validation:**
   - Confirms physical labelling standards appropriate
   - Confirms supplies available
   - Date and signature

4. **CISO Approval:**
   - Approves overall procedures
   - Authorises implementation
   - Date and signature

---

# PART II: TECHNICAL SPECIFICATION

---

## 2.1 Workbook Technical Details

### File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.12-13.S2_Labelling_Procedures_and_Standards_YYYYMMDD.xlsx` |
| Generator | `generate_a512_13_2_labelling_procedures.py` |
| Sheets | 7 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 40 | 8 |
| 2 | Labelling_Standards | Visual formats | 20 | 9 |
| 3 | Digital_Labelling | Electronic labelling | 30 | 7 |
| 4 | Physical_Labelling | Paper and media | 30 | 7 |
| 5 | Automation_Tools | Tool inventory | 20 | 8 |
| 6 | Evidence_Register | Audit evidence | 30 | 8 |
| 7 | Approval_SignOff | Authorisation | 20 | 6 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

| Row | Content | Purpose |
|-----|---------|---------|
| 1 | Title (merged A1:H1) | Document identification |
| 3-10 | Purpose and principles | Methodology guidance |
| 12-20 | Labelling methods overview | Quick reference |
| 22-30 | How to use instructions | Step-by-step guidance |

### Sheet 2: Labelling_Standards

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Classification_Level | 18 | Text | Pre-populated |
| B | Display_Text | 18 | Text | Input |
| C | Color_Hex | 12 | Text | Hex format |
| D | Header_Format | 30 | Text | Input |
| E | Footer_Format | 40 | Text | Input |
| F | Watermark_Text | 25 | Text | Input |
| G | Banner_Style | 25 | Text | Input |
| H | Icon_Symbol | 20 | Text | Input |
| I | Font_Requirements | 25 | Text | Input |

### Sheet 3: Digital_Labelling

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Asset_Type | 25 | Text | Pre-populated |
| B | Labelling_Method | 35 | Text | Input |
| C | Metadata_Fields | 40 | Text | Input |
| D | Automation | 30 | Text | Input |
| E | Validation | 20 | Text | Input |
| F | Responsibility | 18 | Text | Input |
| G | Implementation_Status | 18 | List | Implemented, In Progress, Not Implemented, N/A |

### Sheet 4: Physical_Labelling

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Asset_Type | 20 | Text | Pre-populated |
| B | Labelling_Method | 35 | Text | Input |
| C | Label_Location | 30 | Text | Input |
| D | Label_Format | 40 | Text | Input |
| E | Durability | 20 | Text | Input |
| F | Responsible_Party | 20 | Text | Input |
| G | Implementation_Status | 18 | List | Implemented, In Progress, Not Implemented, N/A |

### Sheet 5: Automation_Tools

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Tool_Name | 35 | Text | Input |
| B | Vendor | 15 | Text | Input |
| C | Scope_Coverage | 25 | Text | Input |
| D | Key_Features | 45 | Text | Input |
| E | Integration_Points | 30 | Text | Input |
| F | Licence_Type | 18 | Text | Input |
| G | Implementation_Status | 20 | List | Deployed, Pilot, Evaluating, Not Implemented, Planned |
| H | Owner | 15 | Text | Input |

### Sheet 6: Evidence_Register

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Evidence_ID | 15 | Text | None |
| B | Description | 40 | Text | None |
| C | Evidence_Type | 22 | List | Procedure document, Configuration screenshot, Label sample, Training record, Tool export, Audit report, Other |
| D | Related_Procedure | 25 | Text | None |
| E | Location | 30 | Text | None |
| F | Collected_Date | 15 | Date | None |
| G | Collected_By | 15 | Text | None |
| H | Verification_Status | 18 | List | Verified, Pending Review, Not Verified, Expired |

### Sheet 7: Approval_SignOff

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Role | 30 | Text | Pre-populated |
| B | Name | 25 | Text | Input |
| C | Signature | 20 | Text | Input |
| D | Date | 15 | Date | Input |
| E | Decision | 22 | List | Approved, Approved with conditions, Rejected, Pending |
| F | Comments | 30 | Text | Input |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| Labelling_Standards | A:A | ="RESTRICTED" | Red fill (#FF6B6B), White bold |
| Labelling_Standards | A:A | ="CONFIDENTIAL" | Orange fill (#FFA94D) |
| Labelling_Standards | A:A | ="INTERNAL" | Green fill (#69DB7C) |
| Labelling_Standards | A:A | ="PUBLIC" | Blue fill (#74C0FC) |
| Digital_Labelling | G:G | ="Implemented" | Green fill (#C6EFCE) |
| Digital_Labelling | G:G | ="In Progress" | Yellow fill (#FFEB9C) |
| Digital_Labelling | G:G | ="Not Implemented" | Red fill (#FFC7CE) |
| Physical_Labelling | G:G | ="Implemented" | Green fill (#C6EFCE) |
| Physical_Labelling | G:G | ="Not Implemented" | Red fill (#FFC7CE) |
| Automation_Tools | G:G | ="Deployed" | Green fill (#C6EFCE) |
| Automation_Tools | G:G | ="Pilot" | Yellow fill (#FFEB9C) |
| Automation_Tools | G:G | ="Not Implemented" | Red fill (#FFC7CE) |
| Evidence_Register | H:H | ="Verified" | Green fill (#C6EFCE) |
| Evidence_Register | H:H | ="Not Verified" | Red fill (#FFC7CE) |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| A.5.12-13.1 Workbook | Classification scheme | A.5.12-13.1 -> Labelling_Standards |
| Microsoft Purview | Sensitivity labels | This workbook -> MIP configuration |
| Email System | Transport rules | This workbook -> Exchange rules |
| DLP Solution | Label-based policies | This workbook -> DLP rules |
| Document Management | Metadata standards | This workbook -> DMS configuration |
| A.5.12-13.3 Workbook | Asset classification | Bidirectional |
| A.5.12-13.4 Workbook | Compliance monitoring | This workbook -> Compliance |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.12-13 | Information Classification and Labelling | Parent policy |
| ISMS-IMP-A.5.12-13.S1 | Classification Scheme Definition | Classification scheme |
| ISMS-IMP-A.5.12-13.S3 | Asset Classification Inventory | Asset tracking |
| ISMS-IMP-A.5.12-13.S4 | Compliance Dashboard | Compliance monitoring |
| ISMS-IMP-A.5.12-13.S5 | Consolidation Dashboard | Executive view |
| ISMS-POL-A.8.12 | Data Leakage Prevention | DLP integration |

---

**END OF SPECIFICATION**

---

*"The single biggest problem in communication is the illusion that it has taken place."*
— George Bernard Shaw

<!-- QA_VERIFIED: 2026-02-04 -->
