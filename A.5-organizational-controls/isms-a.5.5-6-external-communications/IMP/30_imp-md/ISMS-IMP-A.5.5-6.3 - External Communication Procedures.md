# ISMS-IMP-A.5.5-6.3 - External Communication Procedures

## Implementation Guide for ISO 27001:2022 Controls A.5.5 & A.5.6: Communication Procedures

**Document ID:** ISMS-IMP-A.5.5-6.3
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

This workbook provides a structured framework for documenting procedures governing external communications with authorities and special interest groups. It defines scenarios requiring external contact, mandatory notification requirements, escalation matrices, approval workflows, and communication templates to ensure consistent, compliant, and timely external communications.

### 1.2 Scope

The External Communication Procedures workbook covers:

- **Communication Scenarios**: When to contact which external party
- **Notification Requirements**: Mandatory regulatory notifications and timelines
- **Escalation Matrices**: Internal escalation paths before external contact
- **Approval Workflows**: Who must authorise external communications
- **Communication Templates**: Standardised message formats

### 1.3 Control Requirements

This workbook supports implementation of both ISO 27001:2022 Controls A.5.5 and A.5.6:

**Control A.5.5:**
> *"Appropriate contacts with relevant authorities should be maintained."*

**Control A.5.6:**
> *"Appropriate contacts with special interest groups or other specialist security forums and professional associations should be maintained."*

This workbook ensures that when contact is needed, proper procedures exist to execute communications correctly, securely, and in compliance with regulatory requirements.

### 1.4 Assessment Domains

This workbook is **Domain 3 of 5** in the A.5.5-6 External Communications assessment series:

| Domain | Workbook | Focus |
|--------|----------|-------|
| 1 | Authority Contacts Register | Documenting authority relationships |
| 2 | Special Interest Groups Register | SIG memberships and engagement |
| **3** | **External Communication Procedures** | **Notification and escalation processes** |
| 4 | Compliance Dashboard | KPIs and metrics monitoring |
| 5 | Consolidation Dashboard | Executive summary across domains |

---

## 2. Prerequisites

Before completing this assessment, ensure you have:

### 2.1 Documentation Requirements

- [ ] Completed Authority Contacts Register (A.5.5-6.1)
- [ ] Completed Special Interest Groups Register (A.5.5-6.2)
- [ ] Incident response procedures
- [ ] Data breach notification policy
- [ ] Crisis communication plan
- [ ] Regulatory compliance requirements mapping
- [ ] Legal department contact protocols

### 2.2 Stakeholder Involvement

| Role | Responsibility |
|------|----------------|
| **CISO** | Overall accountability, procedure approval |
| **Legal Counsel** | Notification requirements, regulatory compliance |
| **DPO** | Data protection notifications |
| **Communications/PR** | Media and public communications |
| **CEO** | Executive-level authorisations |
| **Compliance Officer** | Regulatory notification tracking |

### 2.3 Regulatory Mapping

Identify all applicable notification requirements:

| Regulation | Applies | Notification Type | Authority | Timeline |
|------------|---------|-------------------|-----------|----------|
| GDPR Art. 33 | If processing EU data | Data breach | Lead Supervisory Authority | 72 hours |
| Swiss nDSG Art. 24 | If processing Swiss data | Data breach | FDPIC | As soon as possible |
| NIS2 Art. 23 | If in scope | Significant incident | CSIRT | 24h/72h |
| FINMA (if applicable) | Financial services | Cyber incident | FINMA | 24 hours |
| [Add others] | | | | |

---

## 3. Workbook Structure

### 3.1 Sheet Overview

| Sheet | Purpose | Input Required |
|-------|---------|----------------|
| Instructions | Guidance for completing the workbook | Read only |
| Communication_Scenarios | When to contact which party | Manual entry |
| Notification_Requirements | Mandatory notification obligations | Manual entry |
| Escalation_Matrix | Internal escalation before external contact | Manual entry |
| Approval_Workflow | Who must approve communications | Manual entry |
| Communication_Templates | Standard message templates | Manual entry |
| Evidence_Register | Audit evidence documentation | Manual entry |
| Approval_SignOff | Management approval workflow | Manual entry |

### 3.2 Sheet Dependencies

```
Instructions (Read First)
        ↓
   ┌────┴────┐
   ↓         ↓
Communication    Notification
Scenarios        Requirements
   ↓         ↓
   └────┬────┘
        ↓
Escalation_Matrix
        ↓
Approval_Workflow
        ↓
Communication_Templates
        ↓
Evidence_Register
        ↓
Approval_SignOff (Complete Last)
```

---

## 4. Completion Walkthrough

### 4.1 Communication_Scenarios Sheet

Define when to contact external parties.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Scenario_ID | Unique identifier | SCEN-001 |
| Scenario_Name | Descriptive name | Personal Data Breach |
| Scenario_Category | Type of scenario | Regulatory |
| Trigger_Event | What initiates the scenario | Data breach affecting individuals |
| Primary_Authority | Main external contact | Data Protection Authority |
| Secondary_Authority | Alternative contact | Sector Regulator (if applicable) |
| SIG_Contact | Relevant SIG if applicable | None |
| Response_Time | Required response timeline | 72 hours |
| Approval_Level | Who must approve | DPO + Legal + CISO |
| Internal_Escalation_First | Must escalate internally before external | Yes |
| Documentation_Required | What documentation needed | Breach report, impact assessment |
| Template_Reference | Reference to template | TPL-DPA-001 |
| Procedure_Steps | Step-by-step process | 1. Contain 2. Assess 3. Prepare 4. Approve 5. Notify |

**Pre-populated Scenarios:**

| Scenario | Category | Primary Authority | Response Time |
|----------|----------|-------------------|---------------|
| Personal Data Breach | Regulatory | Data Protection Authority | 72 hours |
| Cyber Crime Incident | Law Enforcement | Cantonal Police / Fedpol | Immediate |
| Critical Vulnerability | Threat Intel | NCSC | 24 hours |
| Regulatory Inquiry | Regulatory | Requesting Regulator | Per deadline |
| Physical Security Incident | Emergency | Emergency Services | Immediate |

**Completion Steps:**

1. Review incident response and crisis management procedures
2. Map each incident type to external communication requirements
3. Identify applicable authorities and SIGs for each scenario
4. Define response timelines based on regulatory requirements
5. Document required approvals and procedure steps

### 4.2 Notification_Requirements Sheet

Document mandatory notification obligations.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Requirement_ID | Unique identifier | NOT-001 |
| Regulation | Source regulation | GDPR Art. 33 |
| Notification_Type | Category of notification | Data Breach Notification |
| Authority | Target authority | Lead Supervisory Authority |
| Trigger_Condition | When notification required | Personal data breach with risk to rights |
| Time_Limit | Notification deadline | 72 hours from awareness |
| Required_Information | What must be included | Nature of breach, categories affected, measures |
| Format | How to submit | Online portal or prescribed form |
| Penalty_for_Non_Compliance | Consequences | Up to EUR 10M or 2% global turnover |
| Internal_Owner | Responsible role | DPO |
| Procedure_Reference | Link to procedure | SCEN-001 |
| Last_Review_Date | When requirement reviewed | [Date] |
| Notes | Additional context | Applies to all personal data processing |

**Key Regulations to Document:**

| Regulation | Notification | Timeline | Authority |
|------------|--------------|----------|-----------|
| GDPR Art. 33 | Data breach | 72 hours | Supervisory Authority |
| GDPR Art. 34 | To data subjects | Without undue delay | Data subjects |
| Swiss nDSG Art. 24 | Data breach (high risk) | As soon as possible | FDPIC |
| NIS2 Art. 23 | Significant incident | 24h/72h | CSIRT |
| FINMA Circular | Cyber incident | 24 hours | FINMA |

### 4.3 Escalation_Matrix Sheet

Define internal escalation before external contact.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Level | Escalation level | L4 |
| Scenario_Type | Type of incident | Data Breach |
| First_Contact | Initial internal contact | DPO |
| Escalation_1 | First escalation level | CISO + Legal |
| Escalation_2 | Second escalation level | CEO |
| Escalation_3 | Third escalation level | Board |
| Time_to_Escalate | Maximum time at each level | 1 hour |
| External_Contact_Approval | Who approves external contact | DPO + Legal + CEO |
| Notes | Special considerations | 72h regulatory clock starts on awareness |

**Standard Escalation Levels:**

| Level | Scenario Type | Escalation Path | External Approval |
|-------|---------------|-----------------|-------------------|
| L1 | Security Incident (Low) | Analyst → Manager → CISO | CISO |
| L2 | Security Incident (Medium) | Manager → CISO → CEO | CEO |
| L3 | Security Incident (Critical) | CISO → CEO → Board | CEO |
| L4 | Data Breach | DPO → CISO+Legal → CEO | DPO+Legal+CEO |
| L5 | Criminal Activity | Security → CISO → Legal → CEO | CEO+Legal |
| L6 | Regulatory Inquiry | Compliance → Legal → CEO | Legal+CEO |
| L7 | Physical Emergency | Facility → HR → CEO | Facility Manager |

### 4.4 Approval_Workflow Sheet

Define approval requirements for external communications.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Workflow_ID | Unique identifier | WF-003 |
| Communication_Type | Type of communication | Data Breach Notification |
| Recipient_Type | Category of recipient | Data Protection Authority |
| Required_Approvers | Who must approve | DPO + Legal Counsel + CISO |
| Approval_Sequence | Order of approvals | Parallel then CEO |
| Max_Approval_Time | Deadline for approvals | 24 hours (within 72h window) |
| Delegate_When_Absent | Deputies for approvers | Deputies for each role |
| Documentation_Required | What must be prepared | Breach report, impact assessment |
| Post_Communication_Actions | Follow-up requirements | Track response, log evidence |

**Standard Workflows:**

| Communication Type | Recipient | Approvers | Sequence |
|-------------------|-----------|-----------|----------|
| Routine Info Sharing | SIG | Department Head | Single |
| Threat Intelligence | ISAC/NCSC | CISO | Single |
| Data Breach Notification | DPA | DPO+Legal+CISO → CEO | Parallel then CEO |
| Law Enforcement Contact | Police | CEO+Legal | Sequential |
| Regulatory Response | Regulator | Legal+CEO | Sequential |
| Media/Public Statement | Media | CEO+Communications | Parallel |

### 4.5 Communication_Templates Sheet

Reference standardised message templates.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Template_ID | Unique identifier | TPL-DPA-001 |
| Template_Name | Descriptive name | Data Breach Notification (DPA) |
| Purpose | When to use | Notify data protection authority of breach |
| Recipient_Type | Target audience | Data Protection Authority |
| Required_Sections | Content structure | Nature, categories, numbers, consequences, measures |
| Classification | Information classification | Confidential |
| Review_Date | Last template review | [Date] |
| Owner | Template owner | DPO |
| Storage_Location | Where template stored | [SharePoint path] |
| Notes | Usage guidance | Use within 72 hours of awareness |

**Standard Templates to Maintain:**

| Template ID | Purpose | Recipient |
|-------------|---------|-----------|
| TPL-DPA-001 | Data breach notification | Data Protection Authority |
| TPL-LE-001 | Law enforcement report | Police/Fedpol |
| TPL-VULN-001 | Vulnerability disclosure | NCSC |
| TPL-REG-001 | Regulatory response | Any Regulator |
| TPL-ISAC-001 | Threat report | ISAC |
| TPL-PHYS-001 | Physical incident report | Emergency Services |

### 4.6 Evidence_Register Sheet

Document evidence for audit purposes.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Evidence_ID | Unique identifier | EV-2026-001 |
| Evidence_Type | Category of evidence | Procedure Document |
| Description | What the evidence demonstrates | Approved escalation matrix |
| Related_Procedure | Linked procedure reference | Escalation_Matrix |
| Date_Created | When evidence was created | 2026-01-15 |
| Created_By | Who created evidence | CISO |
| Storage_Location | Where stored | SharePoint/ISMS/A.5.5-6/Procedures |
| Retention_Period | How long to retain | 5 years |
| Review_Date | Next review | 2027-01-15 |
| Status | Current status | Current |
| Notes | Additional context | Approved by executive team |

### 4.7 Approval_SignOff Sheet

Management approval for procedures.

**Approval Workflow:**

| Step | Role | Responsibility |
|------|------|----------------|
| 1 | Preparer | Document all procedures |
| 2 | Security Manager | Technical accuracy review |
| 3 | Legal Counsel | Regulatory compliance verification |
| 4 | DPO | Data protection requirements |
| 5 | CISO | Final approval and sign-off |

---

## 5. Evidence Collection

### 5.1 Required Evidence

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Procedure Documents | Formal documented procedures | ISMS Evidence Library |
| Template Library | Communication templates | ISMS Evidence Library |
| Escalation Matrix | Approved escalation paths | ISMS Evidence Library |
| Approval Records | Sign-off documentation | ISMS Evidence Library |
| Training Records | Staff trained on procedures | ISMS Evidence Library |
| Test Records | Procedure test/drill results | ISMS Evidence Library |

### 5.2 Evidence Storage Guidelines

- Use consistent naming: `PROC-[Category]-[Year]-[Seq].pdf`
- Store in ISMS Evidence Library
- Version control all templates
- Maintain approval records
- Retain for minimum 5 years

---

## 6. Common Pitfalls

### 6.1 Mistakes to Avoid

❌ **MISTAKE:** Creating procedures without testing them through tabletop exercises
✅ **CORRECT:** Conduct annual tabletop exercises to validate procedures work under pressure

❌ **MISTAKE:** Not accounting for weekends/holidays in notification timelines
✅ **CORRECT:** 72-hour and 24-hour deadlines include weekends; ensure 24/7 coverage for critical scenarios

❌ **MISTAKE:** Assuming verbal approval is sufficient for regulatory notifications
✅ **CORRECT:** Document all approvals in writing before sending; maintain audit trail

❌ **MISTAKE:** Using personal email for external authority communications
✅ **CORRECT:** Use official corporate channels; maintain records in central repository

❌ **MISTAKE:** Not identifying delegates for key approvers
✅ **CORRECT:** Document deputies for all approval roles; ensure delegates are trained

❌ **MISTAKE:** Generic templates that don't meet specific regulatory requirements
✅ **CORRECT:** Tailor templates to each authority's specific format requirements

❌ **MISTAKE:** Procedures only cover incident scenarios, not routine communications
✅ **CORRECT:** Include procedures for routine regulatory inquiries and SIG engagement

❌ **MISTAKE:** Not considering cross-border notification requirements
✅ **CORRECT:** Map all jurisdictions; understand lead authority concept (GDPR) and local requirements

❌ **MISTAKE:** Escalation matrix doesn't account for simultaneous incidents
✅ **CORRECT:** Define parallel escalation paths and prioritisation when multiple incidents occur

❌ **MISTAKE:** Templates not reviewed after regulatory changes
✅ **CORRECT:** Review templates whenever regulations change; maintain version control

---

## 7. Quality Checklist

Before submitting for approval, verify:

### 7.1 Completeness

- [ ] All applicable notification requirements documented
- [ ] Scenarios cover all incident types in IRP
- [ ] Escalation paths defined for all scenario levels
- [ ] Approval workflows documented for all communication types
- [ ] Templates available for all standard communications

### 7.2 Accuracy

- [ ] Notification timelines align with current regulations
- [ ] Approval authorities match organisational structure
- [ ] Contact references link to Authority/SIG registers
- [ ] Templates meet regulatory format requirements

### 7.3 Operability

- [ ] Procedures tested through tabletop exercise
- [ ] Staff trained on procedures
- [ ] Out-of-hours coverage established
- [ ] Delegate authorities documented and briefed

### 7.4 Evidence

- [ ] All procedures formally approved
- [ ] Training records available
- [ ] Test/drill records documented
- [ ] Templates version-controlled

---

## 8. Review and Approval

### 8.1 Review Frequency

| Review Type | Frequency | Triggered By |
|-------------|-----------|--------------|
| Full Assessment | Annual | Scheduled review |
| Template Review | Semi-annual | Regulatory change |
| Procedure Test | Annual | Tabletop exercise |
| Ad-hoc Update | As needed | Regulatory change, incident learning |

### 8.2 Approval Authority

| Action | Approval Required |
|--------|-------------------|
| New procedure | CISO + Legal |
| Template update | Procedure Owner |
| Escalation matrix change | CEO |
| Full assessment sign-off | CISO |

---

# PART II: TECHNICAL SPECIFICATION

## 9. Workbook Technical Structure

### 9.1 File Specifications

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.5-6.3 |
| **Workbook Name** | External Communication Procedures |
| **File Format** | .xlsx (Excel 2007+) |
| **Generated By** | generate_a55_6_3_communication_procedures.py |
| **Sheets** | 8 |

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
- Key scenarios requiring external contact
- Approval requirements
- Data validation guidance
- Generated date and control reference

#### 9.2.2 Communication_Scenarios Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Communication_Scenarios |
| **Purpose** | Scenario definitions |
| **Header Row** | 1 |
| **Pre-populated** | 5 standard scenarios |
| **Input Cells** | Yellow fill (FFFFCC) |

**Column Structure:**

| Column | Header | Width | Validation | Required |
|--------|--------|-------|------------|----------|
| A | Scenario_ID | 12 | None | Yes |
| B | Scenario_Name | 25 | None | Yes |
| C | Scenario_Category | 15 | Dropdown | Yes |
| D | Trigger_Event | 35 | None | Yes |
| E | Primary_Authority | 25 | None | Yes |
| F | Secondary_Authority | 25 | None | No |
| G | SIG_Contact | 20 | None | No |
| H | Response_Time | 15 | None | Yes |
| I | Approval_Level | 22 | Dropdown | Yes |
| J | Internal_Escalation_First | 20 | Dropdown | Yes |
| K | Documentation_Required | 40 | None | Yes |
| L | Template_Reference | 15 | None | No |
| M | Procedure_Steps | 50 | None | Yes |

**Data Validations:**
- Scenario_Category: "Regulatory,Law Enforcement,Emergency,Threat Intel,Standards,Other"
- Approval_Level: "Department Head,CISO,Legal,DPO + Legal + CISO,CEO + Legal,CEO"
- Internal_Escalation_First: "Yes,No"

#### 9.2.3 Notification_Requirements Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Notification_Requirements |
| **Purpose** | Regulatory obligations |
| **Header Row** | 1 |
| **Pre-populated** | 4 key regulations |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Required |
|--------|--------|-------|----------|
| A | Requirement_ID | 12 | Yes |
| B | Regulation | 20 | Yes |
| C | Notification_Type | 25 | Yes |
| D | Authority | 30 | Yes |
| E | Trigger_Condition | 40 | Yes |
| F | Time_Limit | 25 | Yes |
| G | Required_Information | 50 | Yes |
| H | Format | 25 | No |
| I | Penalty_for_Non_Compliance | 35 | No |
| J | Internal_Owner | 15 | Yes |
| K | Procedure_Reference | 15 | No |
| L | Last_Review_Date | 15 | No |
| M | Notes | 35 | No |

#### 9.2.4 Escalation_Matrix Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Escalation_Matrix |
| **Purpose** | Internal escalation paths |
| **Header Row** | 1 |
| **Pre-populated** | 7 escalation levels |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width |
|--------|--------|-------|
| A | Level | 8 |
| B | Scenario_Type | 30 |
| C | First_Contact | 20 |
| D | Escalation_1 | 20 |
| E | Escalation_2 | 15 |
| F | Escalation_3 | 12 |
| G | Time_to_Escalate | 18 |
| H | External_Contact_Approval | 25 |
| I | Notes | 35 |

#### 9.2.5 Approval_Workflow Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Approval_Workflow |
| **Purpose** | Communication approvals |
| **Header Row** | 1 |
| **Pre-populated** | 6 workflows |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Workflow_ID | 12 | None |
| B | Communication_Type | 30 | None |
| C | Recipient_Type | 25 | None |
| D | Required_Approvers | 30 | None |
| E | Approval_Sequence | 20 | Dropdown |
| F | Max_Approval_Time | 25 | None |
| G | Delegate_When_Absent | 25 | None |
| H | Documentation_Required | 40 | None |
| I | Post_Communication_Actions | 40 | None |

**Data Validations:**
- Approval_Sequence: "Single,Sequential,Parallel,Parallel then CEO"

#### 9.2.6 Communication_Templates Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Communication_Templates |
| **Purpose** | Template reference |
| **Header Row** | 1 |
| **Pre-populated** | 5 templates |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Template_ID | 12 | None |
| B | Template_Name | 35 | None |
| C | Purpose | 45 | None |
| D | Recipient_Type | 25 | None |
| E | Required_Sections | 60 | None |
| F | Classification | 15 | Dropdown |
| G | Review_Date | 15 | Date |
| H | Owner | 15 | None |
| I | Storage_Location | 30 | None |
| J | Notes | 35 | None |

**Data Validations:**
- Classification: "TLP:RED,TLP:AMBER,TLP:GREEN,TLP:CLEAR,Confidential,Internal,Public"

#### 9.2.7 Evidence_Register Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Evidence_Register |
| **Purpose** | Audit evidence |
| **Header Row** | 1 |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Evidence_ID | 12 | None |
| B | Evidence_Type | 22 | Dropdown |
| C | Description | 40 | None |
| D | Related_Procedure | 18 | None |
| E | Date_Created | 15 | Date |
| F | Created_By | 20 | None |
| G | Storage_Location | 40 | None |
| H | Retention_Period | 15 | None |
| I | Review_Date | 15 | Date |
| J | Status | 15 | Dropdown |
| K | Notes | 35 | None |

**Data Validations:**
- Evidence_Type: "Procedure Document,Template,Approval Record,Training Record,Test Record,Other"
- Status: "Current,Archived,Pending Review"

#### 9.2.8 Approval_SignOff Sheet

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
| F | Procedures_Complete | 20 | Dropdown |
| G | Templates_Current | 18 | Dropdown |
| H | Training_Complete | 18 | Dropdown |
| I | Approval_Status | 15 | Dropdown |
| J | Signature_Date | 15 | Date |
| K | Next_Review_Date | 18 | Date |
| L | Comments | 40 | None |

**Data Validations:**
- Reviewer_Role: "CISO,Legal Counsel,DPO,Compliance Officer,CEO"
- Procedures_Complete: "Yes,No,Partial"
- Templates_Current: "Yes,No,Partial"
- Training_Complete: "Yes,No,Partial"
- Approval_Status: "Approved,Rejected,Pending,Conditional"

---

## 10. Styling Specifications

### 10.1 Colour Palette

| Element | Colour | Hex Code |
|---------|--------|----------|
| Header Background | Dark Blue | 2F5496 |
| Header Font | White | FFFFFF |
| Input Cells | Light Yellow | FFFFCC |
| Pre-populated Data | White | FFFFFF |
| Calculated Cells | Light Green | E2EFDA |

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
- Text alignment: Wrap text, vertical top

---

## 11. Integration Points

### 11.1 Related Workbooks

| Workbook | Relationship |
|----------|--------------|
| A.5.5-6.1 Authority Contacts | Primary_Authority references |
| A.5.5-6.2 SIG Register | SIG_Contact references |
| A.5.5-6.4 Compliance Dashboard | Procedure compliance metrics |
| A.5.5-6.5 Consolidation | Cross-domain procedure status |

### 11.2 Data Flow

```
A.5.5-6.1 (Authorities)    A.5.5-6.2 (SIGs)
         ↓                      ↓
         └──────────┬───────────┘
                    ↓
        Communication_Scenarios
                    ↓
              ┌─────┼─────┐
              ↓     ↓     ↓
      Notification  Escalation  Approval
      Requirements  Matrix      Workflow
              ↓     ↓     ↓
              └─────┼─────┘
                    ↓
        Communication_Templates
                    ↓
        A.5.5-6.4 Dashboard
                    ↓
        A.5.5-6.5 Consolidation
```

---

## 12. Generator Script Reference

**Script:** `generate_a55_6_3_communication_procedures.py`

**Key Functions:**
- `create_instructions_sheet(ws)` - Creates guidance sheet
- `create_communication_scenarios_sheet(ws)` - Creates scenario definitions
- `create_notification_requirements_sheet(ws)` - Creates regulatory obligations
- `create_escalation_matrix_sheet(ws)` - Creates escalation paths
- `create_approval_workflow_sheet(ws)` - Creates approval requirements
- `create_communication_templates_sheet(ws)` - Creates template reference
- `create_evidence_register_sheet(ws)` - Creates evidence documentation
- `create_approval_signoff_sheet(ws)` - Creates approval workflow

**Output:** `ISMS-IMP-A.5.5-6.3_External_Communication_Procedures_YYYYMMDD.xlsx`

---

**END OF SPECIFICATION**

---

*"The single biggest problem in communication is the illusion that it has taken place."*
— George Bernard Shaw

<!-- QA_VERIFIED: 2026-02-04 -->
