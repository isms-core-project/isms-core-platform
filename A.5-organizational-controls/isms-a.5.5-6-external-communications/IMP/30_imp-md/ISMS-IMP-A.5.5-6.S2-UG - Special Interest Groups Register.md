**ISMS-IMP-A.5.5-6.S2-UG - Special Interest Groups Register**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.6: Contact with Special Interest Groups

## Implementation Guide for ISO 27001:2022 Control A.5.6: Contact with Special Interest Groups

**Document ID:** ISMS-IMP-A.5.5-6.S2-UG
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

## 1. Assessment Overview

### 1.1 Purpose

This workbook provides a structured framework for documenting and managing memberships in special interest groups (SIGs), security forums, and professional associations as required by ISO 27001:2022 Control A.5.6. Active participation in these groups helps organisations stay informed about emerging threats, best practices, and industry developments in information security.

### 1.2 Scope

The Special Interest Groups Register covers:

- **Information Sharing and Analysis Centres (ISACs)**: Sector-specific threat intelligence sharing
- **Security Forums**: Regional and national security communities
- **Professional Associations**: ISACA, (ISC)², ISSA, and similar bodies
- **Vendor Security Groups**: Technology-specific user groups
- **Academic and Research Networks**: Security research collaborations
- **Industry Working Groups**: Standards development and best practice groups

### 1.3 Control Requirement

ISO 27001:2022 Control A.5.6 states:

> *"Appropriate contacts with special interest groups or other specialist security forums and professional associations should be maintained."*

This control ensures that the organisation benefits from external knowledge networks, receives timely threat intelligence, and contributes to the broader security community.

### 1.4 Assessment Domains

This workbook is **Domain 2 of 5** in the A.5.5-6 External Communications assessment series:

| Domain | Workbook | Focus |
|--------|----------|-------|
| 1 | Authority Contacts Register | Documenting authority relationships |
| **2** | **Special Interest Groups Register** | **SIG memberships and engagement** |
| 3 | Communication Procedures | Notification and escalation processes |
| 4 | Compliance Dashboard | KPIs and metrics monitoring |
| 5 | Consolidation Dashboard | Executive summary across domains |

---

## 2. Prerequisites

Before completing this assessment, ensure you have:

### 2.1 Documentation Requirements

- [ ] List of current SIG memberships and subscriptions
- [ ] Membership agreements and contracts
- [ ] Intelligence sharing agreements (ISA)
- [ ] Meeting attendance records and minutes
- [ ] Contributions made to SIGs (presentations, reports, data)
- [ ] Threat intelligence received in past 12 months

### 2.2 Stakeholder Involvement

| Role | Responsibility |
|------|----------------|
| **CISO** | Overall accountability, value assessment approval |
| **Security Manager** | Day-to-day SIG engagement |
| **Threat Intelligence Analyst** | Intelligence handling and dissemination |
| **Legal Counsel** | Information sharing agreement review |
| **Budget Owner** | Membership cost approval |
| **Subject Matter Experts** | Domain-specific group participation |

### 2.3 Information Gathering

Collect the following information for each SIG membership:

- Organisation name and type
- Membership tier/level
- Membership cost and renewal date
- Primary contact details
- Engagement activities and frequency
- Intelligence received and actionability
- Contributions made
- Value assessment

---

## 3. Workbook Structure

### 3.1 Sheet Overview

| Sheet | Purpose | Input Required |
|-------|---------|----------------|
| Instructions | Guidance for completing the workbook | Read only |
| Groups_Registry | Master list of all SIG memberships | Manual entry |
| Membership_Details | Detailed membership information | Manual entry |
| Engagement_Log | Record of participation activities | Ongoing entry |
| Intelligence_Received | Threat intelligence tracking | Ongoing entry |
| Contribution_Log | Record of contributions made | Ongoing entry |
| Evidence_Register | Audit evidence documentation | Manual entry |
| Approval_SignOff | Management approval workflow | Manual entry |

### 3.2 Sheet Dependencies

```
Instructions (Read First)
        ↓
Groups_Registry (Complete First)
        ↓
Membership_Details (Expand Registry)
        ↓
   ┌────┼────┐
   ↓    ↓    ↓
Engagement  Intelligence  Contribution
   Log       Received        Log
   ↓    ↓    ↓
   └────┼────┘
        ↓
Evidence_Register
        ↓
Approval_SignOff (Complete Last)
```

---

## 4. Completion Walkthrough

### 4.1 Groups_Registry Sheet

This is the master list of all SIG memberships.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Group_ID | Unique identifier | SIG-001 |
| Group_Name | Official organisation name | FS-ISAC (Financial Services ISAC) |
| Group_Type | Category of group | ISAC |
| Membership_Status | Current membership state | Active |
| Membership_Tier | Level of membership | Full Member |
| Primary_Focus | Main area covered | Financial sector cyber threats |
| Geographic_Scope | Operational coverage | Global |
| Primary_Contact | Internal engagement owner | Security Manager |
| Join_Date | When membership started | 2024-03-15 |
| Renewal_Date | Next renewal due | 2026-03-15 |
| Annual_Cost | Membership fee | CHF 15,000 |
| Value_Rating | Assessed value to organisation | High |
| Last_Engagement | Most recent activity | 2026-01-20 |
| Notes | Additional information | Quarterly meetings, daily threat feeds |

**Completion Steps:**

1. **Inventory Current Memberships**: List all active SIG memberships
2. **Identify Potential Memberships**: Consider gaps in coverage
3. **Categorise Appropriately**: Assign correct group type
4. **Assign Engagement Owners**: Each membership needs an internal champion
5. **Assess Value**: Rate each membership's contribution to security posture

### 4.2 Membership_Details Sheet

Expanded information for each membership.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Group_ID | Reference to Groups_Registry | SIG-001 |
| Membership_Agreement | Agreement reference/location | FS-ISAC-MSA-2024 |
| Information_Sharing_Agreement | ISA details | TLP-based sharing agreement |
| Services_Included | What membership provides | Threat feeds, portal access, alerts |
| Events_Access | Conference/meeting access | Annual summit, quarterly calls |
| Intelligence_Feeds | Automated feeds received | Daily IOC feed, weekly threat briefs |
| Portal_Access | Online resources available | Member portal, document library |
| Classified_Access | If applicable, clearance requirements | None required |
| Contact_Name | Primary SIG contact | [Name] |
| Contact_Email | SIG contact email | member.services@fs-isac.com |
| Contact_Phone | SIG contact phone | +1 XXX XXX XXXX |
| Escalation_Contact | For urgent matters | [Name, contact] |
| Payment_Method | How fees are paid | Annual invoice |
| Budget_Code | Internal budget reference | SEC-001-EXT |

### 4.3 Engagement_Log Sheet

Track all participation activities.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Engagement_ID | Unique entry identifier | ENG-2026-001 |
| Date | Date of engagement | 2026-01-20 |
| Group_ID | Reference to Groups_Registry | SIG-001 |
| Engagement_Type | Category of activity | Meeting |
| Description | Details of engagement | Q1 Threat Briefing Call |
| Participants | Internal attendees | CISO, Security Manager |
| Duration | Time spent | 2 hours |
| Key_Topics | Main discussion points | Ransomware trends, supply chain attacks |
| Action_Items | Follow-up required | Review detection rules for new TTPs |
| Value_Assessment | Rating of engagement value | High |
| Evidence_Reference | Supporting documentation | Meeting minutes EV-2026-001 |

**Engagement Types:**
- Meeting (virtual or in-person)
- Conference/Summit
- Training/Workshop
- Working Group Session
- Intelligence Briefing
- Incident Coordination
- Social Event/Networking

### 4.4 Intelligence_Received Sheet

Track threat intelligence received from SIGs.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Intel_ID | Unique identifier | INTEL-2026-001 |
| Date_Received | Date intelligence arrived | 2026-01-18 |
| Group_ID | Source SIG reference | SIG-001 |
| Intelligence_Type | Category of intelligence | IOC Alert |
| Classification | Traffic Light Protocol | TLP:AMBER |
| Subject | Brief description | New ransomware variant targeting financial sector |
| Relevance | Applicability to organisation | High |
| Actionability | Ability to act on intel | High |
| Actions_Taken | What was done with intel | Updated SIEM rules, blocked IOCs |
| Time_to_Action | Hours from receipt to action | 4 hours |
| Internal_Distribution | Who received the intel | SOC, Infrastructure Team |
| Evidence_Reference | Link to stored intel | INTEL-FS-2026-0118 |
| Notes | Additional observations | Confirmed IOCs in our environment - false positive |

**Intelligence Types:**
- IOC Alert (Indicators of Compromise)
- Threat Report
- Vulnerability Advisory
- TTP Update (Tactics, Techniques, Procedures)
- Incident Notification
- Strategic Intelligence
- Research Paper

### 4.5 Contribution_Log Sheet

Track contributions made to SIGs.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Contribution_ID | Unique identifier | CONTRIB-2026-001 |
| Date | Date of contribution | 2026-01-25 |
| Group_ID | Target SIG reference | SIG-001 |
| Contribution_Type | Category of contribution | Incident Report |
| Description | What was contributed | Shared anonymised ransomware incident details |
| Classification | TLP of contribution | TLP:AMBER |
| Approval_Level | Who approved sharing | CISO |
| Approval_Date | When approved | 2026-01-24 |
| Recipient_Feedback | Response from SIG | Shared with members, thanked for contribution |
| Value_to_Community | Assessed impact | High - helped other members detect similar activity |
| Evidence_Reference | Documentation reference | CONTRIB-EV-2026-001 |
| Notes | Additional context | First contribution in 2026 |

**Contribution Types:**
- Incident Report (anonymised)
- IOC Sharing
- Presentation/Speaking
- Research Contribution
- Working Group Participation
- Document/Guide Authorship
- Mentoring/Training
- Committee Service

### 4.6 Evidence_Register Sheet

Document evidence for audit purposes.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Evidence_ID | Unique identifier | EV-2026-001 |
| Evidence_Type | Category of evidence | Engagement Record |
| Description | What the evidence demonstrates | Q1 FS-ISAC meeting attendance confirmation |
| Related_Group | Group ID reference | SIG-001 |
| Date_Created | When evidence was created | 2026-01-20 |
| Created_By | Who created/captured evidence | Security Manager |
| Storage_Location | Where evidence is stored | SharePoint/ISMS/A.5.5-6/SIG-Evidence |
| Retention_Period | How long to retain | 3 years |
| Review_Date | Next review date | 2027-01-20 |
| Status | Current evidence status | Current |
| Notes | Additional information | Includes attendee list and topics |

### 4.7 Approval_SignOff Sheet

Management approval for the assessment.

**Approval Workflow:**

| Step | Role | Responsibility |
|------|------|----------------|
| 1 | Preparer | Complete all sheets, compile evidence |
| 2 | Security Manager | Engagement quality review |
| 3 | Budget Owner | Cost-benefit validation |
| 4 | CISO | Final approval and sign-off |

---

## 5. Evidence Collection

### 5.1 Required Evidence

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Membership Certificates | Proof of active membership | ISMS Evidence Library |
| Membership Agreements | Signed contracts/agreements | Legal Document Store |
| Meeting Attendance Records | Participation evidence | ISMS Evidence Library |
| Intelligence Samples | Redacted/approved examples | ISMS Evidence Library |
| Contribution Records | Approved sharing documentation | ISMS Evidence Library |
| Value Assessment Reports | ROI analysis | ISMS Evidence Library |

### 5.2 Evidence Storage Guidelines

- Use consistent naming: `SIG-[GroupID]-[Year]-[Type]-[Seq].pdf`
- Store in ISMS Evidence Library (SharePoint/Confluence or equivalent)
- Apply TLP classifications appropriately
- Maintain confidentiality of shared intelligence
- Retain for minimum 3 years

---

## 6. Common Pitfalls

### 6.1 Mistakes to Avoid

❌ **MISTAKE:** Joining SIGs without assigning an engagement owner
✅ **CORRECT:** Every membership must have a designated internal champion responsible for active participation

❌ **MISTAKE:** Passively receiving intelligence without acting on it
✅ **CORRECT:** Track actionability metrics; ensure received intel is assessed, distributed, and acted upon

❌ **MISTAKE:** Never contributing back to SIGs (being a "free rider")
✅ **CORRECT:** Maintain reciprocal relationships; plan and track contributions to the community

❌ **MISTAKE:** Not tracking the value/ROI of memberships
✅ **CORRECT:** Conduct annual value assessments; discontinue memberships that don't provide benefit

❌ **MISTAKE:** Sharing information without proper classification and approval
✅ **CORRECT:** Apply TLP classifications; obtain CISO approval before sharing sensitive information

❌ **MISTAKE:** Joining duplicate groups covering the same threat landscape
✅ **CORRECT:** Map coverage areas; ensure memberships complement rather than overlap

❌ **MISTAKE:** Only senior staff attending SIG events
✅ **CORRECT:** Rotate attendance to develop team capabilities and increase coverage

❌ **MISTAKE:** Not integrating received intelligence into security operations
✅ **CORRECT:** Establish workflows to feed SIG intelligence into SIEM, threat hunting, and detection engineering

❌ **MISTAKE:** Letting memberships lapse due to missed renewals
✅ **CORRECT:** Track renewal dates; set calendar reminders; include in budget planning cycle

❌ **MISTAKE:** Storing intelligence in personal email or local drives
✅ **CORRECT:** Centralise intelligence storage with appropriate access controls and classification handling

---

## 7. Quality Checklist

Before submitting for approval, verify:

### 7.1 Completeness

- [ ] All active memberships documented in Groups_Registry
- [ ] Membership details complete for all groups
- [ ] Engagement log shows activity within last 90 days
- [ ] Intelligence received log is current
- [ ] Contribution log demonstrates reciprocal participation

### 7.2 Value Assessment

- [ ] All memberships have value rating assigned
- [ ] Low-value memberships flagged for review
- [ ] Cost-benefit analysis available for high-cost memberships
- [ ] Coverage gaps identified and addressed

### 7.3 Evidence

- [ ] Membership proof available for all active groups
- [ ] Engagement evidence documented
- [ ] Intelligence handling properly classified
- [ ] Contribution approvals documented

### 7.4 Governance

- [ ] All required approvals obtained
- [ ] Renewal schedule maintained
- [ ] Budget allocations current
- [ ] Information sharing agreements reviewed

---

## 8. Review and Approval

### 8.1 Review Frequency

| Review Type | Frequency | Triggered By |
|-------------|-----------|--------------|
| Full Assessment | Annual | Scheduled review |
| Value Assessment | Semi-annual | Budget planning |
| Membership Renewal | As per renewal dates | Calendar reminder |
| Ad-hoc Update | As needed | New membership, change in value |

### 8.2 Approval Authority

| Action | Approval Required |
|--------|-------------------|
| New membership | CISO + Budget Owner |
| Membership renewal | Security Manager |
| Intelligence sharing | CISO |
| Contribution approval | CISO |
| Membership discontinuation | CISO |

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
