# ISMS-IMP-A.6.6.1 — NDA Template Registry and Inventory

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.6.1 |
| **Title** | NDA Template Registry and Inventory |
| **Control Reference** | ISO/IEC 27001:2022 A.6.6 |
| **Control Name** | Confidentiality or Non-Disclosure Agreements |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

## PART I: USER COMPLETION GUIDE

### Assessment Overview

**Purpose**

This workbook maintains the registry of NDA templates, version history, and applicability guidance for confidentiality agreements across all stakeholder categories.

**Scope**

This assessment covers:
- All NDA and confidentiality agreement templates
- Version control and change history
- Applicability matrix by stakeholder type
- Standard clause library for consistency

**Control Requirements**

ISO 27001:2022 Control A.6.6 states:
> *"Confidentiality or non-disclosure agreements reflecting the organisation's needs for the protection of information should be identified, documented, regularly reviewed and signed by personnel and other relevant interested parties."*

### Prerequisites

Before completing this assessment:

- [ ] Access to all current NDA templates
- [ ] Legal Counsel contact for template review dates
- [ ] Understanding of stakeholder categories
- [ ] Information classification scheme reference

### Workbook Structure

| Sheet | Purpose | Key Actions |
|-------|---------|-------------|
| Instructions | Guidance | Review before starting |
| Template_Registry | Master template list | Register all templates |
| Template_Versions | Version history | Track changes |
| Applicability_Matrix | When to use which | Define applicability |
| Clause_Library | Standard clauses | Document clauses |
| Evidence_Register | Evidence tracking | Link evidence |
| Approval_SignOff | Authorisation | Obtain approvals |

### Completion Walkthrough

**Step 1: Template_Registry Sheet**

Register all NDA templates:

1. **Template_ID** - Unique identifier (NDA-TMP-001)
2. **Template_Name** - Descriptive name
3. **Template_Type** - Standard/Mutual/One-Way/Employment/etc.
4. **Stakeholder_Category** - Primary intended audience
5. **Current_Version** - Version number
6. **Effective_Date** - When template became effective
7. **Legal_Review_Date** - Date of last legal review
8. **Legal_Reviewer** - Who conducted review
9. **Owner** - Template owner
10. **Storage_Location** - Where template is stored
11. **Status** - Active/Draft/Superseded/Archived

**Step 2: Template_Versions Sheet**

Track version history:

1. **Template_ID** - Link to registry
2. **Version** - Version number
3. **Version_Date** - When version created
4. **Change_Description** - What changed
5. **Change_Reason** - Why it changed
6. **Changed_By** - Who made changes
7. **Legal_Approved** - Yes/No/Pending
8. **Legal_Approver** - Who approved

**Step 3: Applicability_Matrix Sheet**

Define when each template applies:

1. **Stakeholder_Category** - Employee, Contractor, Vendor, etc.
2. **Access_Type** - What type of access they have
3. **Information_Classification** - What level they access
4. **Required_Template** - Which template to use
5. **Timing** - When NDA must be signed
6. **Duration** - How long NDA is valid
7. **Post_Termination** - Post-relationship period
8. **Mandatory** - Yes/No/Conditional

**Step 4: Clause_Library Sheet**

Document standard clauses:

1. **Clause_ID** - Unique identifier
2. **Clause_Name** - Descriptive name
3. **Clause_Category** - Definitions/Obligations/Exceptions/etc.
4. **Clause_Purpose** - What the clause achieves
5. **Standard_Text** - Approved wording
6. **Mandatory** - Yes/No/Recommended

### Evidence Collection

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Template Documents | All approved NDA templates | Legal/Contracts repository |
| Legal Review Records | Review and approval documentation | ISMS Evidence Library |
| Version History | Change logs and approvals | ISMS Evidence Library |

### Common Pitfalls

❌ **MISTAKE**: Using outdated templates without legal review
✅ **CORRECT**: Verify template currency before each use

❌ **MISTAKE**: No version control on templates
✅ **CORRECT**: Track all versions with change history

❌ **MISTAKE**: Unclear applicability guidance
✅ **CORRECT**: Explicit matrix defining which template for which situation

❌ **MISTAKE**: Templates stored in multiple locations
✅ **CORRECT**: Single authoritative location with controlled access

❌ **MISTAKE**: No legal review of template changes
✅ **CORRECT**: All substantive changes reviewed by Legal Counsel

❌ **MISTAKE**: Missing clauses for regulatory requirements
✅ **CORRECT**: Ensure GDPR/nDSG requirements included

❌ **MISTAKE**: Templates not covering post-termination
✅ **CORRECT**: Clear post-relationship confidentiality periods

❌ **MISTAKE**: No ownership assigned to templates
✅ **CORRECT**: Each template has designated owner

### Quality Checklist

Before submitting:

- [ ] All templates registered with current version
- [ ] Legal review dates within 12 months
- [ ] Applicability matrix covers all stakeholder types
- [ ] Standard clauses documented
- [ ] Storage locations verified and accessible
- [ ] Approval sign-offs obtained

---

## PART II: TECHNICAL SPECIFICATION

### Workbook Architecture

**File Details**:

- Filename: `ISMS-IMP-A.6.6.1_NDA_Template_Registry_and_Inventory_YYYYMMDD.xlsx`
- Format: Microsoft Excel (.xlsx)
- Sheets: 7

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Template_Type | Standard NDA, Mutual NDA, One-Way NDA, Employment, Contractor, Vendor, Customer, Partner |
| Stakeholder_Category | Employees, Contractors, Consultants, Vendors, Suppliers, Partners, Customers, Board Members, Visitors |
| Status | Active, Draft, Under Review, Superseded, Archived |
| Legal_Approved | Yes, No, Pending |
| Clause_Category | Definitions, Obligations, Exceptions, Term, Termination, Remedies, IP Rights, Legal, General |
| Mandatory | Yes, No, Recommended, Conditional |

### Generator Reference

**Script**: `generate_a66_1_nda_template_registry.py`

**Location**: `10-isms-scr-base/isms-a.6.6-confidentiality-nda/10_generator-master/`

---

**END OF SPECIFICATION**

---

*"The only real security that a man can have in this world is a reserve of knowledge, experience, and ability."*
— Henry Ford

<!-- QA_VERIFIED: 2026-02-01 -->
