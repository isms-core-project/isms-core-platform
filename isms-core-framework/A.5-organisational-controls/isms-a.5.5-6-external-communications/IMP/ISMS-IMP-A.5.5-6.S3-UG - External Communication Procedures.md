<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.5-6.S3-UG:framework:UG:a.5.5-6 -->
**ISMS-IMP-A.5.5-6.S3-UG - External Communication Procedures**
**User Completion Guide**
### ISO/IEC 27001:2022 Controls A.5.5 & A.5.6: Communication Procedures

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | External Communication Procedures |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.5-6.S3-UG |
| **Related Policy** | ISMS-POL-A.5.5-6 (External Communications) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.5 & A.5.6 (Communication Procedures) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
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

- ISMS-POL-A.5.5-6 (External Communications)
- ISMS-IMP-A.5.5-6.S1 (Authority Contacts Register)
- ISMS-IMP-A.5.5-6.S2 (Special Interest Groups Register)

---

## Implementation Guide for ISO 27001:2022 Controls A.5.5 & A.5.6: Communication Procedures

**Document ID:** ISMS-IMP-A.5.5-6.S3-UG
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

## Assessment Overview

### Purpose

This workbook provides a structured framework for documenting procedures governing external communications with authorities and special interest groups. It defines scenarios requiring external contact, mandatory notification requirements, escalation matrices, approval workflows, and communication templates to ensure consistent, compliant, and timely external communications.

### Scope

The External Communication Procedures workbook covers:

- **Communication Scenarios**: When to contact which external party
- **Notification Requirements**: Mandatory regulatory notifications and timelines
- **Escalation Matrices**: Internal escalation paths before external contact
- **Approval Workflows**: Who must authorise external communications
- **Communication Templates**: Standardised message formats

### Control Requirements

This workbook supports implementation of both ISO 27001:2022 Controls A.5.5 and A.5.6:

**Control A.5.5:**
> *"Appropriate contacts with relevant authorities should be maintained."*

**Control A.5.6:**
> *"Appropriate contacts with special interest groups or other specialist security forums and professional associations should be maintained."*

This workbook ensures that when contact is needed, proper procedures exist to execute communications correctly, securely, and in compliance with regulatory requirements.

### Assessment Domains

This workbook is **Domain 3 of 3** in the A.5.5-6 External Communications assessment series:

| Domain | Workbook | Focus |
|--------|----------|-------|
| 1 | Authority Contacts Register | Documenting authority relationships |
| 2 | Special Interest Groups Register | SIG memberships and engagement |
| **3** | **External Communication Procedures** | **Notification and escalation processes** |

---

## Prerequisites

Before completing this assessment, ensure you have:

### Documentation Requirements

- [ ] Completed Authority Contacts Register (A.5.5-6.1)
- [ ] Completed Special Interest Groups Register (A.5.5-6.2)
- [ ] Incident response procedures
- [ ] Data breach notification policy
- [ ] Crisis communication plan
- [ ] Regulatory compliance requirements mapping
- [ ] Legal department contact protocols

### Stakeholder Involvement

| Role | Responsibility |
|------|----------------|
| **CISO** | Overall accountability, procedure approval |
| **Legal Counsel** | Notification requirements, regulatory compliance |
| **DPO** | Data protection notifications |
| **Communications/PR** | Media and public communications |
| **CEO** | Executive-level authorisations |
| **Compliance Officer** | Regulatory notification tracking |

### Regulatory Mapping

Identify all applicable notification requirements:

| Regulation | Applies | Notification Type | Authority | Timeline |
|------------|---------|-------------------|-----------|----------|
| GDPR Art. 33 | If processing EU data | Data breach | Lead Supervisory Authority | 72 hours |
| Swiss nDSG Art. 24 | If processing Swiss data | Data breach | FDPIC | As soon as possible |
| NIS2 Art. 23 | If in scope | Significant incident | CSIRT | 24h/72h |
| FINMA (if applicable) | Financial services | Cyber incident | FINMA | 24 hours |
| [Add others] | | | | |

---

### Workbook at a Glance

This workbook contains the following sheets:

| Sheet | Purpose |
|-------|---------|
| **Instructions & Legend** | Assessment guidance, control requirements, and field descriptions |
| **Communication Scenarios** | When to contact which external party and required response timelines |
| **Notification Requirements** | Mandatory regulatory notifications, timelines, and format requirements |
| **Escalation Matrix** | Internal escalation paths before external contact is made |
| **Approval Workflow** | Approval requirements for each type of external communication |
| **Communication Templates** | Standardised message formats for each communication scenario |
| **Evidence Register** | Tracking of supporting evidence for procedures and approvals |
| **Approval Sign-Off** | Stakeholder sign-off and approval workflow |
| **Summary Dashboard** | Compliance overview auto-populated from your input data |

---

## Completion Walkthrough

### Communication_Scenarios Sheet

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

### Notification_Requirements Sheet

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

### Escalation_Matrix Sheet

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

### Approval_Workflow Sheet

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

### Communication_Templates Sheet

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

### Evidence_Register Sheet

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

### Approval_SignOff Sheet

Management approval for procedures.

**Approval Workflow:**

| Step | Role | Responsibility |
|------|------|----------------|
| 1 | Preparer | Document all procedures |
| 2 | Security Manager | Technical accuracy review |
| 3 | Legal Counsel | Regulatory compliance verification |
| 4 | DPO | Data protection requirements |
| 5 | CISO | Final approval and sign-off |

### Summary_Dashboard Sheet

The Summary Dashboard automatically aggregates data from your completed sheets and provides a compliance overview. No data entry is required.

Review the dashboard after completing all sheets above to confirm:
- Communication scenario coverage across all incident categories
- Notification requirement completeness and timeline accuracy
- Escalation matrix coverage for all defined scenario levels
- Approval workflow documentation status
- Template availability for all standard communication types

Use the dashboard output to support your management review discussion and sign-off process.

---

## Evidence Collection

### Required Evidence

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Procedure Documents | Formal documented procedures | ISMS Evidence Library |
| Template Library | Communication templates | ISMS Evidence Library |
| Escalation Matrix | Approved escalation paths | ISMS Evidence Library |
| Approval Records | Sign-off documentation | ISMS Evidence Library |
| Training Records | Staff trained on procedures | ISMS Evidence Library |
| Test Records | Procedure test/drill results | ISMS Evidence Library |

### Evidence Storage Guidelines

- Use consistent naming: `PROC-[Category]-[Year]-[Seq].pdf`
- Store in ISMS Evidence Library
- Version control all templates
- Maintain approval records
- Retain for minimum 5 years

---

## Common Pitfalls

### Mistakes to Avoid

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

## Quality Checklist

Before submitting for approval, verify:

### Completeness

- [ ] All applicable notification requirements documented
- [ ] Scenarios cover all incident types in IRP
- [ ] Escalation paths defined for all scenario levels
- [ ] Approval workflows documented for all communication types
- [ ] Templates available for all standard communications

### Accuracy

- [ ] Notification timelines align with current regulations
- [ ] Approval authorities match organisational structure
- [ ] Contact references link to Authority/SIG registers
- [ ] Templates meet regulatory format requirements

### Operability

- [ ] Procedures tested through tabletop exercise
- [ ] Staff trained on procedures
- [ ] Out-of-hours coverage established
- [ ] Delegate authorities documented and briefed

### Evidence

- [ ] All procedures formally approved
- [ ] Training records available
- [ ] Test/drill records documented
- [ ] Templates version-controlled

---

## Review and Approval

### Review Frequency

| Review Type | Frequency | Triggered By |
|-------------|-----------|--------------|
| Full Assessment | Annual | Scheduled review |
| Template Review | Semi-annual | Regulatory change |
| Procedure Test | Annual | Tabletop exercise |
| Ad-hoc Update | As needed | Regulatory change, incident learning |

### Approval Authority

| Action | Approval Required |
|--------|-------------------|
| New procedure | CISO + Legal |
| Template update | Procedure Owner |
| Escalation matrix change | CEO |
| Full assessment sign-off | CISO |

---

**END OF USER GUIDE**

---

*"The single biggest problem in communication is the illusion that it has taken place."*
— George Bernard Shaw

<!-- QA_VERIFIED: 2026-03-01 -->
