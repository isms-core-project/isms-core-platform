# ISMS-IMP-A.5.5-6.S1 - Authority Contacts Register

## Implementation Guide for ISO 27001:2022 Control A.5.5: Contact with Authorities

**Document ID:** ISMS-IMP-A.5.5-6.S1
**Version:** 1.0
**Classification:** Internal Use
**Owner:** CISO
**Last Review:** [Date to be set]
**Next Review:** [Date to be set]

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | ISMS Team | Initial release |

---

# PART I: USER COMPLETION GUIDE

## 1. Assessment Overview

### 1.1 Purpose

This workbook provides a structured framework for documenting and maintaining contacts with relevant authorities as required by ISO 27001:2022 Control A.5.5. Effective authority contacts ensure that your organisation can respond appropriately to security incidents, comply with regulatory notification obligations, and coordinate with external agencies when necessary.

### 1.2 Scope

The Authority Contacts Register covers:

- **Law Enforcement Agencies**: Local and national police, cybercrime units, and investigative bodies
- **Regulatory Bodies**: Data protection authorities, financial regulators, industry-specific regulators
- **Emergency Services**: Fire, medical, and civil protection services
- **Government Security Agencies**: National cybersecurity centres, intelligence agencies (if applicable)
- **Certification Bodies**: ISO certification auditors and accreditation bodies
- **Industry Regulators**: Sector-specific oversight bodies

### 1.3 Control Requirement

ISO 27001:2022 Control A.5.5 states:

> *"Appropriate contacts with relevant authorities should be maintained."*

This control ensures that the organisation establishes and maintains relationships with external authorities who may need to be contacted or who may need to contact the organisation in relation to information security matters.

### 1.4 Assessment Domains

This workbook is **Domain 1 of 5** in the A.5.5-6 External Communications assessment series:

| Domain | Workbook | Focus |
|--------|----------|-------|
| **1** | **Authority Contacts Register** | **Documenting authority relationships** |
| 2 | Special Interest Groups Register | SIG memberships and engagement |
| 3 | Communication Procedures | Notification and escalation processes |
| 4 | Compliance Dashboard | KPIs and metrics monitoring |
| 5 | Consolidation Dashboard | Executive summary across domains |

---

## 2. Prerequisites

Before completing this assessment, ensure you have:

### 2.1 Documentation Requirements

- [ ] List of applicable regulations requiring authority notification
- [ ] Current organisational contact lists
- [ ] Incident response procedures referencing external contacts
- [ ] Business continuity plans with emergency contact provisions
- [ ] Regulatory correspondence from the past 12 months

### 2.2 Stakeholder Involvement

| Role | Responsibility |
|------|----------------|
| **CISO** | Overall accountability, review and approval |
| **Legal Counsel** | Regulatory requirements, authority relationships |
| **DPO** | Data protection authority contacts |
| **Compliance Officer** | Regulatory body contacts |
| **Facility Manager** | Emergency services contacts |
| **Security Manager** | Law enforcement coordination |

### 2.3 Information Gathering

Collect the following information for each authority contact:

- Organisation name and official title
- Type of authority and jurisdiction
- Primary and secondary contact details
- Communication protocols and preferred methods
- Scenarios requiring contact
- Historical communication records
- Verification dates and methods

---

## 3. Workbook Structure

### 3.1 Sheet Overview

| Sheet | Purpose | Input Required |
|-------|---------|----------------|
| Instructions | Guidance for completing the workbook | Read only |
| Authority_Registry | Master list of all authority contacts | Manual entry |
| Contact_Types | Categorisation of authority types | Reference/customise |
| Communication_Log | Record of communications with authorities | Ongoing entry |
| Verification_Register | Contact verification tracking | Manual entry |
| Evidence_Register | Audit evidence documentation | Manual entry |
| Approval_SignOff | Management approval workflow | Manual entry |

### 3.2 Sheet Dependencies

```
Instructions (Read First)
        ↓
Contact_Types (Reference)
        ↓
Authority_Registry (Complete First)
        ↓
   ┌────┴────┐
   ↓         ↓
Communication_Log  Verification_Register
        ↓         ↓
   └────┬────┘
        ↓
Evidence_Register
        ↓
Approval_SignOff (Complete Last)
```

---

## 4. Completion Walkthrough

### 4.1 Authority_Registry Sheet

This is the core sheet documenting all authority contacts.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Authority_ID | Unique identifier | AUTH-001 |
| Authority_Name | Official organisation name | Swiss Federal Data Protection Authority (FDPIC) |
| Authority_Type | Category from Contact_Types | Data Protection Authority |
| Jurisdiction | Geographic/legal scope | Switzerland |
| Primary_Contact_Name | Named individual if applicable | [Name] |
| Primary_Contact_Title | Official role/position | Commissioner |
| Primary_Email | Official email address | info@edoeb.admin.ch |
| Primary_Phone | Official phone number | +41 58 462 43 95 |
| Secondary_Contact | Alternative contact details | [Secondary contact info] |
| Website | Official website URL | https://www.edoeb.admin.ch |
| Communication_Protocol | How to contact them | Online portal / Email / Letter |
| Scenarios | When to contact | Personal data breaches, regulatory inquiries |
| Relationship_Owner | Internal owner of relationship | DPO |
| Last_Verified | Date contact details verified | 2026-01-15 |
| Next_Verification | Scheduled verification date | 2026-07-15 |
| Notes | Additional information | 72-hour breach notification required |

**Completion Steps:**

1. **Identify Required Authorities**: Review regulatory requirements, incident response plans, and business continuity procedures
2. **Categorise by Type**: Assign appropriate authority type from Contact_Types
3. **Document Contact Details**: Enter complete, accurate contact information
4. **Assign Internal Owners**: Designate who maintains each relationship
5. **Set Verification Schedule**: Establish verification frequency (minimum annual)

### 4.2 Contact_Types Sheet

Pre-populated reference sheet for authority categorisation.

**Standard Categories:**

| Type_ID | Authority_Type | Description | Examples |
|---------|----------------|-------------|----------|
| TYPE-001 | Law Enforcement | Criminal investigation agencies | Cantonal Police, Fedpol |
| TYPE-002 | Data Protection Authority | Privacy regulators | FDPIC, ICO, CNIL |
| TYPE-003 | Financial Regulator | Financial services oversight | FINMA, SEC, FCA |
| TYPE-004 | Industry Regulator | Sector-specific oversight | OFCOM, health authorities |
| TYPE-005 | Emergency Services | Fire, medical, civil protection | Fire brigade, ambulance |
| TYPE-006 | Cybersecurity Agency | National cyber defence | NCSC, CISA, BSI |
| TYPE-007 | Certification Body | Standards certification | ISO registrars |
| TYPE-008 | Government Body | General government agencies | Tax authorities, customs |

**Customisation:**

- Add organisation-specific categories as needed
- Ensure all Authority_Registry entries reference valid types

### 4.3 Communication_Log Sheet

Track all communications with authorities.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Log_ID | Unique entry identifier | LOG-2026-001 |
| Date | Date of communication | 2026-01-20 |
| Authority_ID | Reference to Authority_Registry | AUTH-001 |
| Contact_Method | How communication occurred | Email |
| Direction | Inbound or Outbound | Outbound |
| Subject | Topic of communication | Data breach notification |
| Summary | Brief description of content | Notified FDPIC of breach affecting 500 individuals |
| Reference_Number | Authority's reference if applicable | FDPIC-2026-12345 |
| Initiated_By | Internal person who initiated | DPO |
| Follow_Up_Required | Whether action is pending | Yes |
| Follow_Up_Date | Deadline for follow-up | 2026-02-20 |
| Status | Current status | Awaiting response |
| Evidence_Reference | Link to stored evidence | EV-2026-001 |

**Logging Requirements:**

- Log ALL communications with authorities, not just incident-related
- Include routine enquiries and relationship maintenance contacts
- Update status as communications progress
- Link to evidence storage location

### 4.4 Verification_Register Sheet

Track periodic verification of contact details.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Verification_ID | Unique identifier | VER-2026-001 |
| Authority_ID | Reference to Authority_Registry | AUTH-001 |
| Verification_Date | Date verification performed | 2026-01-15 |
| Verified_By | Person who performed verification | Security Analyst |
| Verification_Method | How verification was done | Website check + test call |
| Previous_Details | Contact details before verification | [Previous info] |
| Current_Details | Contact details after verification | [Current info] |
| Changes_Found | Whether changes were identified | Yes - new phone number |
| Registry_Updated | Whether Authority_Registry was updated | Yes |
| Next_Verification | Scheduled next verification | 2026-07-15 |
| Notes | Additional observations | Automated email responder confirmed valid |

**Verification Frequency:**

- **Annual minimum** for all authority contacts
- **Semi-annual** for critical contacts (emergency services, regulators)
- **Immediate** re-verification after failed contact attempts

### 4.5 Evidence_Register Sheet

Document evidence for audit purposes.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Evidence_ID | Unique identifier | EV-2026-001 |
| Evidence_Type | Category of evidence | Communication Record |
| Description | What the evidence demonstrates | Email to FDPIC notifying data breach |
| Related_Authority | Authority ID reference | AUTH-001 |
| Date_Created | When evidence was created | 2026-01-20 |
| Created_By | Who created/captured evidence | DPO |
| Storage_Location | Where evidence is stored | SharePoint/ISMS/A.5.5-6/Evidence/2026 |
| Retention_Period | How long to retain | 7 years |
| Review_Date | Next review date | 2027-01-20 |
| Status | Current evidence status | Current |
| Notes | Additional information | Includes delivery confirmation |

### 4.6 Approval_SignOff Sheet

Management approval for the assessment.

**Approval Workflow:**

| Step | Role | Responsibility |
|------|------|----------------|
| 1 | Preparer | Complete all sheets, compile evidence |
| 2 | Security Manager | Technical review and validation |
| 3 | Compliance Officer | Regulatory completeness check |
| 4 | CISO | Final approval and sign-off |

---

## 5. Evidence Collection

### 5.1 Required Evidence

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Authority Registry Export | Complete list of authority contacts | ISMS Evidence Library |
| Communication Records | Emails, letters, portal submissions | ISMS Evidence Library |
| Verification Documentation | Screenshots, call logs, confirmation emails | ISMS Evidence Library |
| Notification Acknowledgements | Confirmation from authorities | ISMS Evidence Library |
| Relationship Review Minutes | Annual relationship review records | ISMS Evidence Library |

### 5.2 Evidence Storage Guidelines

- Use consistent naming: `EV-[YEAR]-[SEQ]_[Authority]_[Type].pdf`
- Store in ISMS Evidence Library (SharePoint/Confluence or equivalent)
- Maintain version control for updated documents
- Apply appropriate access controls
- Retain for minimum 3 years (7 years for regulated industries)

---

## 6. Common Pitfalls

### 6.1 Mistakes to Avoid

❌ **MISTAKE:** Using generic department emails instead of specific contact addresses
✅ **CORRECT:** Document official, verified contact channels including named contacts where possible

❌ **MISTAKE:** Failing to verify contact details after a communication fails
✅ **CORRECT:** Implement immediate verification process when contact attempts fail

❌ **MISTAKE:** Only documenting authorities required for incident response
✅ **CORRECT:** Include ALL relevant authorities: emergency services, certification bodies, government agencies

❌ **MISTAKE:** Not assigning internal owners to authority relationships
✅ **CORRECT:** Each authority must have a designated relationship owner responsible for maintenance

❌ **MISTAKE:** Annual verification at year-end only
✅ **CORRECT:** Stagger verifications throughout the year; verify immediately when changes suspected

❌ **MISTAKE:** Logging only incident-related communications
✅ **CORRECT:** Log ALL communications including routine enquiries and relationship maintenance

❌ **MISTAKE:** Storing evidence only in individual email inboxes
✅ **CORRECT:** Centralise evidence in ISMS Evidence Library with proper categorisation

❌ **MISTAKE:** Not considering authorities across all jurisdictions
✅ **CORRECT:** Document authorities for all jurisdictions where organisation operates

❌ **MISTAKE:** Assuming contact details remain valid between verifications
✅ **CORRECT:** Check authority websites before any communication; update registry if changes found

❌ **MISTAKE:** Missing secondary/after-hours contacts for emergency services
✅ **CORRECT:** Document 24/7 emergency contact procedures including out-of-hours numbers

---

## 7. Quality Checklist

Before submitting for approval, verify:

### 7.1 Completeness

- [ ] All applicable authority types have at least one contact documented
- [ ] All mandatory fields in Authority_Registry are completed
- [ ] Contact details verified within last 12 months
- [ ] Internal relationship owners assigned for all authorities
- [ ] Communication log includes recent entries (evidence of active management)

### 7.2 Accuracy

- [ ] Contact details verified against official sources
- [ ] Authority types correctly categorised
- [ ] Jurisdiction information accurate
- [ ] Communication protocols align with authority requirements

### 7.3 Evidence

- [ ] Evidence exists for all documented communications
- [ ] Evidence properly stored and accessible
- [ ] Evidence naming convention followed
- [ ] Evidence retention periods applied

### 7.4 Governance

- [ ] All required approvals obtained
- [ ] Review schedule established
- [ ] Escalation procedures documented

---

## 8. Review and Approval

### 8.1 Review Frequency

| Review Type | Frequency | Triggered By |
|-------------|-----------|--------------|
| Full Assessment | Annual | Scheduled review |
| Contact Verification | Semi-annual | Scheduled verification |
| Ad-hoc Update | As needed | Regulatory change, incident, failed contact |

### 8.2 Approval Authority

| Action | Approval Required |
|--------|-------------------|
| New authority added | Security Manager |
| Contact details updated | Relationship Owner |
| Full assessment sign-off | CISO |
| Regulatory notification | DPO + Legal + CISO |

---

# PART II: TECHNICAL SPECIFICATION

## 9. Workbook Technical Structure

### 9.1 File Specifications

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.5-6.S1 |
| **Workbook Name** | Authority Contacts Register |
| **File Format** | .xlsx (Excel 2007+) |
| **Generated By** | generate_a55_6_1_authority_contacts.py |
| **Sheets** | 7 |

### 9.2 Sheet Specifications

#### 9.2.1 Instructions Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Instructions |
| **Purpose** | User guidance |
| **Protection** | Read-only recommended |
| **Column A Width** | 90 |

**Content Sections:**
- Document title and identifier
- Purpose statement
- Sheet descriptions
- Key authority types covered
- Data entry guidelines
- Generated date and control reference

#### 9.2.2 Authority_Registry Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Authority_Registry |
| **Purpose** | Master authority contact list |
| **Header Row** | 1 |
| **Data Rows** | 2-100+ |
| **Input Cells** | Yellow fill (FFFFCC) |

**Column Structure:**

| Column | Header | Width | Validation | Required |
|--------|--------|-------|------------|----------|
| A | Authority_ID | 12 | None | Yes |
| B | Authority_Name | 35 | None | Yes |
| C | Authority_Type | 25 | Dropdown list | Yes |
| D | Jurisdiction | 20 | None | Yes |
| E | Primary_Contact_Name | 25 | None | No |
| F | Primary_Email | 35 | None | Yes |
| G | Primary_Phone | 20 | None | Yes |
| H | Secondary_Contact | 35 | None | No |
| I | Website | 40 | None | No |
| J | Communication_Protocol | 25 | Dropdown list | Yes |
| K | Scenarios | 45 | None | Yes |
| L | Relationship_Owner | 20 | None | Yes |
| M | Last_Verified | 15 | Date | Yes |
| N | Next_Verification | 15 | Date | Yes |
| O | Notes | 40 | None | No |

**Data Validations:**
- Authority_Type: "Law Enforcement,Data Protection Authority,Financial Regulator,Industry Regulator,Emergency Services,Cybersecurity Agency,Certification Body,Government Body,Other"
- Communication_Protocol: "Email,Phone,Online Portal,Letter,In Person,Multiple"

#### 9.2.3 Contact_Types Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Contact_Types |
| **Purpose** | Reference categorisation |
| **Header Row** | 1 |
| **Pre-populated** | Yes |

**Column Structure:**

| Column | Header | Width |
|--------|--------|-------|
| A | Type_ID | 12 |
| B | Authority_Type | 30 |
| C | Description | 50 |
| D | Example_Authorities | 45 |
| E | Notification_Scenarios | 50 |
| F | Typical_Response_Times | 20 |
| G | Notes | 35 |

#### 9.2.4 Communication_Log Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Communication_Log |
| **Purpose** | Communication tracking |
| **Header Row** | 1 |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Log_ID | 15 | None |
| B | Date | 12 | Date |
| C | Authority_ID | 12 | None |
| D | Contact_Method | 15 | Dropdown |
| E | Direction | 12 | Dropdown |
| F | Subject | 40 | None |
| G | Summary | 60 | None |
| H | Reference_Number | 20 | None |
| I | Initiated_By | 20 | None |
| J | Follow_Up_Required | 18 | Dropdown |
| K | Follow_Up_Date | 15 | Date |
| L | Status | 15 | Dropdown |
| M | Evidence_Reference | 15 | None |

**Data Validations:**
- Contact_Method: "Email,Phone,Online Portal,Letter,In Person,Video Call"
- Direction: "Inbound,Outbound"
- Follow_Up_Required: "Yes,No"
- Status: "Open,Pending Response,Closed,Escalated"

#### 9.2.5 Verification_Register Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Verification_Register |
| **Purpose** | Contact verification tracking |
| **Header Row** | 1 |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Verification_ID | 15 | None |
| B | Authority_ID | 12 | None |
| C | Verification_Date | 15 | Date |
| D | Verified_By | 20 | None |
| E | Verification_Method | 25 | Dropdown |
| F | Previous_Details | 40 | None |
| G | Current_Details | 40 | None |
| H | Changes_Found | 15 | Dropdown |
| I | Registry_Updated | 15 | Dropdown |
| J | Next_Verification | 15 | Date |
| K | Notes | 40 | None |

**Data Validations:**
- Verification_Method: "Website Check,Phone Call,Email Confirmation,Portal Login,Other"
- Changes_Found: "Yes,No"
- Registry_Updated: "Yes,No,N/A"

#### 9.2.6 Evidence_Register Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Evidence_Register |
| **Purpose** | Audit evidence tracking |
| **Header Row** | 1 |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Evidence_ID | 12 | None |
| B | Evidence_Type | 22 | Dropdown |
| C | Description | 45 | None |
| D | Related_Authority | 15 | None |
| E | Date_Created | 15 | Date |
| F | Created_By | 20 | None |
| G | Storage_Location | 45 | None |
| H | Retention_Period | 15 | None |
| I | Review_Date | 15 | Date |
| J | Status | 15 | Dropdown |
| K | Notes | 35 | None |

**Data Validations:**
- Evidence_Type: "Communication Record,Verification Record,Notification Acknowledgement,Relationship Review,Other"
- Status: "Current,Archived,Pending Review"

#### 9.2.7 Approval_SignOff Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Approval_SignOff |
| **Purpose** | Management approval |
| **Header Row** | 1 |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Approval_ID | 12 | None |
| B | Review_Period | 15 | None |
| C | Review_Date | 15 | Date |
| D | Reviewer_Name | 25 | None |
| E | Reviewer_Role | 20 | Dropdown |
| F | Registry_Complete | 18 | Dropdown |
| G | Verifications_Current | 20 | Dropdown |
| H | Communications_Logged | 22 | Dropdown |
| I | Approval_Status | 15 | Dropdown |
| J | Signature_Date | 15 | Date |
| K | Next_Review_Date | 18 | Date |
| L | Comments | 40 | None |

**Data Validations:**
- Reviewer_Role: "CISO,Security Manager,Compliance Officer,DPO,Legal Counsel"
- Registry_Complete: "Yes,No,Partial"
- Verifications_Current: "Yes,No,Partial"
- Communications_Logged: "Yes,No,Partial"
- Approval_Status: "Approved,Rejected,Pending,Conditional"

---

## 10. Styling Specifications

### 10.1 Colour Palette

| Element | Colour | Hex Code |
|---------|--------|----------|
| Header Background | Dark Blue | 2F5496 |
| Header Font | White | FFFFFF |
| Input Cells | Light Yellow | FFFFCC |
| Calculated Cells | Light Green | E2EFDA |
| Compliant Status | Green | C6EFCE |
| Warning Status | Amber | FFEB9C |
| Non-Compliant Status | Red | FFC7CE |

### 10.2 Font Specifications

| Element | Font | Size | Style |
|---------|------|------|-------|
| Title | Default | 14pt | Bold |
| Section Header | Default | 11pt | Bold |
| Column Headers | Default | 11pt | Bold, White |
| Data Cells | Default | 11pt | Normal |

### 10.3 Border Specifications

- All data cells: Thin border (all sides)
- Header cells: Thin border (all sides)

---

## 11. Integration Points

### 11.1 Related Workbooks

| Workbook | Relationship |
|----------|--------------|
| A.5.5-6.2 SIG Register | Complementary (A.5.6 control) |
| A.5.5-6.3 Procedures | References authority contacts for escalation |
| A.5.5-6.4 Compliance Dashboard | Aggregates KPIs from this workbook |
| A.5.5-6.5 Consolidation | Consolidates data for executive reporting |

### 11.2 Data Flow

```
Authority_Registry
        ↓
    ┌───┴───┐
    ↓       ↓
A.5.5-6.3   A.5.5-6.4
Procedures  Dashboard
    ↓       ↓
    └───┬───┘
        ↓
A.5.5-6.5 Consolidation
```

---

## 12. Generator Script Reference

**Script:** `generate_a55_6_1_authority_contacts.py`

**Key Functions:**
- `create_instructions_sheet(ws)` - Creates guidance sheet
- `create_authority_registry_sheet(ws)` - Creates master registry
- `create_contact_types_sheet(ws)` - Creates reference sheet
- `create_communication_log_sheet(ws)` - Creates log sheet
- `create_verification_register_sheet(ws)` - Creates verification tracking
- `create_evidence_register_sheet(ws)` - Creates evidence documentation
- `create_approval_signoff_sheet(ws)` - Creates approval workflow

**Output:** `ISMS-IMP-A.5.5-6.S1_Authority_Contacts_Register_YYYYMMDD.xlsx`

---

**END OF SPECIFICATION**

---

*"In a crisis, the first thing you need is a number you can call."*
— Unknown

<!-- QA_VERIFIED: 2026-02-04 -->
