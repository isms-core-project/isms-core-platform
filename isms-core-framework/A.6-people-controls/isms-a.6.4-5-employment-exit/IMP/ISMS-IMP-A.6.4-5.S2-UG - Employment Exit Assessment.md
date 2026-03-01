<!-- ISMS-CORE:IMP:ISMS-IMP-A.6.4-5.S2-UG:framework:UG:a.6.4-5 -->
**ISMS-IMP-A.6.4-5.S2-UG - Employment Exit Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.6.4, A.6.5

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Employment Exit Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.6.4-5.S2-UG |
| **Related Policy** | ISMS-POL-A.6.4-5 (Employment Exit) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.6.4, A.6.5) |
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

- ISMS-POL-A.6.4-5 (Employment Exit)
- ISMS-IMP-A.6.4-5.S1 (Disciplinary Process Assessment)
- ISMS-IMP-A.6.4-5.S3 (Post Employment Obligations)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.6.4-5.S2-TG.

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Exit Procedures | Define exit procedures by termination type |
| 3 | Access Revocation | Track access revocation for departing personnel |
| 4 | Asset Recovery | Manage recovery of organisation-owned assets |
| 5 | Exit Tracker | Track exit process completion per departing individual |
| 6 | Leaver Reconciliation | Reconcile all access and assets after departure |
| 7 | Evidence Register | Store and reference evidence of exit process completion |
| 8 | Summary Dashboard | Compliance status and key metrics overview |
| 9 | Approval Sign-Off | Management review sign-off and certification |

---

## Assessment Overview

### Purpose

This workbook establishes and maintains the organisation's employment exit process framework, ensuring secure offboarding of personnel with complete access revocation and asset recovery. It serves as the operational tool for:

- **Exit Process Definition**: Standardised procedures by termination type
- **Access Revocation Tracking**: Timely removal of all access rights
- **Asset Recovery Management**: Complete return of organisational assets
- **Exit Interview Documentation**: Security-focused exit interview records
- **Compliance Verification**: Evidence that all exit requirements are met
- **Leaver Reconciliation**: Monthly verification that no orphaned accounts exist

The employment exit process is critical to preventing unauthorised access by former personnel. ISO 27001:2022 Control A.6.5 requires that information security responsibilities and duties that remain valid after termination be defined, enforced, and communicated.

### Scope

This assessment covers the following components:

**In Scope:**
- Exit process procedures by termination type
- Access revocation timelines and requirements
- Physical and logical asset recovery
- Exit interview procedures (security components)
- Leaver notification workflows
- Knowledge transfer requirements
- Offboarding checklists
- Exit clearance documentation
- Orphaned account detection and remediation
- Contractor and temporary worker exit procedures

**Out of Scope:**
- Disciplinary process leading to termination (covered in ISMS-IMP-A.6.4-5.S1)
- Post-employment obligations and NDA tracking (covered in ISMS-IMP-A.6.4-5.S3)
- General HR exit procedures not related to information security
- Third-party vendor offboarding (covered in A.5.19-23)

### Business Value

A well-defined employment exit process delivers:

| Value Area | Benefit |
|------------|---------|
| **Security** | Prevents unauthorised access by former personnel |
| **Compliance** | Demonstrates secure offboarding for ISO 27001 |
| **Asset Protection** | Ensures recovery of all organisational property |
| **Data Protection** | Confirms deletion of data on personal devices |
| **Risk Reduction** | Eliminates orphaned accounts and access |
| **Audit Readiness** | Clear evidence trail for all exits |

### Assessment Frequency

| Activity | Frequency | Responsible Party |
|----------|-----------|-------------------|
| Exit Process Review | Annual | HR Director with CISO |
| Access Revocation Audit | Monthly | IAM Team |
| Asset Recovery Audit | Quarterly | IT Operations |
| Orphaned Account Review | Monthly | IAM Team |
| Exit Interview Analysis | Quarterly | HR with Security |

---

## Control Requirements

### ISO 27001:2022 Control A.6.5

> *"Information security responsibilities and duties that remain valid after termination or change of employment should be defined, enforced and communicated to relevant personnel and other interested parties."*

**Control Type:** Preventive
**Security Properties:** Confidentiality, Integrity, Availability
**Cybersecurity Concepts:** Protect
**Operational Capabilities:** Human Resource Security, Identity and Access Management

### Implementation Requirements

Control A.6.5 requires organisations to establish:

**1. Access Revocation**
- Timely removal of all access rights
- Defined timelines by termination type
- Complete scope including all systems, physical access, third-party access
- Verification that access has been removed

**2. Asset Return**
- Recovery of all physical assets (devices, badges, keys)
- Verification of data deletion on personal devices
- Recovery of logical assets (licenses, credentials)
- Documentation of unreturned assets

**3. Knowledge Transfer**
- Handover of responsibilities
- Documentation of critical knowledge
- Transfer of system access to successors
- Update of shared credentials

**4. Continuing Obligations**
- Communication of ongoing confidentiality requirements
- Exit interview covering security obligations
- Signed acknowledgement of continuing duties
- NDA reinforcement

### What Auditors Look For

ISO 27001 auditors examining Control A.6.5 will verify:

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Documented Procedures** | Exit process by termination type |
| **Access Revocation Timelines** | Defined SLAs by scenario |
| **Asset Return Records** | Completed exit checklists |
| **Exit Interview Records** | Security component documentation |
| **Leaver Reconciliation** | Monthly orphaned account reports |
| **Process Compliance** | Sample completed exits demonstrating compliance |
| **Timeliness Metrics** | Evidence that SLAs are met |

---

## Prerequisites

### Before Starting This Assessment

Complete the following prerequisites:

#### Required Access

| System/Resource | Access Level | Purpose |
|-----------------|--------------|---------|
| HR Information System | Read/Write | Access to leaver records |
| Identity Management System | Read | Access review and revocation records |
| IT Asset Management | Read | Asset assignment records |
| Physical Access Control | Read | Badge deactivation records |
| ISMS Evidence Library | Write | Upload evidence |

#### Required Information

| Information | Source | Why Needed |
|-------------|--------|------------|
| Current exit procedures | HR Department | Baseline review |
| Access revocation SLAs | IT/IAM | Timeline verification |
| Asset inventory templates | IT Operations | Asset tracking |
| Exit interview templates | HR Department | Security content review |
| Recent leaver records | HR/IT | Compliance verification |
| Orphaned account reports | IAM | Gap identification |

#### Prerequisite Checklist

Before proceeding, verify:

- [ ] Current exit procedures obtained from HR
- [ ] Access revocation timelines documented
- [ ] Asset tracking system accessible
- [ ] Exit interview templates available
- [ ] Sample leaver records available for review
- [ ] IAM Team contact established
- [ ] IT Operations contact established

---

## Exit Scenarios

### Understanding Exit Types

Different exit scenarios require different procedures and timelines:

#### Voluntary Resignation

| Aspect | Requirement |
|--------|-------------|
| **Notice Period** | Per employment contract (typically 1-3 months) |
| **Access Revocation** | End of last working day |
| **Asset Return** | By last working day |
| **Exit Interview** | During notice period |
| **Knowledge Transfer** | During notice period |
| **Risk Level** | Standard |

#### Involuntary Termination (For Cause)

| Aspect | Requirement |
|--------|-------------|
| **Notice Period** | May be immediate for gross misconduct |
| **Access Revocation** | Same business day, before notification if possible |
| **Asset Return** | Immediately |
| **Exit Interview** | Abbreviated, security focus |
| **Knowledge Transfer** | Limited or none |
| **Risk Level** | Elevated - potential hostile leaver |

#### Immediate Dismissal (Gross Misconduct)

| Aspect | Requirement |
|--------|-------------|
| **Notice Period** | None |
| **Access Revocation** | Within 1 hour of decision |
| **Asset Return** | Immediately, supervised |
| **Exit Interview** | Not conducted |
| **Knowledge Transfer** | None |
| **Risk Level** | High - escort off premises |

#### Retirement

| Aspect | Requirement |
|--------|-------------|
| **Notice Period** | Extended (typically 3+ months) |
| **Access Revocation** | End of last working day |
| **Asset Return** | By last working day |
| **Exit Interview** | Comprehensive |
| **Knowledge Transfer** | Extended period |
| **Risk Level** | Low |

#### Contract End (Contractors)

| Aspect | Requirement |
|--------|-------------|
| **Notice Period** | Per contract terms |
| **Access Revocation** | Contract end date |
| **Asset Return** | By contract end |
| **Exit Interview** | Per contract value |
| **Knowledge Transfer** | Per statement of work |
| **Risk Level** | Standard |

#### Role Change (Internal Mover)

| Aspect | Requirement |
|--------|-------------|
| **Notice Period** | Per internal policy |
| **Access Revocation** | Previous role access within 2 business days |
| **Asset Return** | Role-specific assets returned |
| **Exit Interview** | Not required |
| **Knowledge Transfer** | Required |
| **Risk Level** | Low |

### Exit Scenario Decision Tree

```
Is the person leaving the organisation?
├── YES → Continue to exit type...
│   │
│   └── Is this voluntary?
│       ├── YES → Standard exit process (resignation/retirement)
│       └── NO → Continue...
│           │
│           └── Is this gross misconduct?
│               ├── YES → Immediate exit with escort
│               └── NO → Accelerated exit (same day revocation)
│
└── NO → Internal mover process
    │
    └── Revoke previous role access
        └── Grant new role access
```

---

## Completion Walkthrough

### Step 1: Review Instructions Sheet

**Time estimate:** 10-15 minutes

1. Read the document purpose and scope
2. Understand exit type classifications
3. Review regulatory requirements
4. Identify stakeholders

### Step 2: Complete Exit_Procedures Sheet

**Time estimate:** 2-3 hours

Document exit procedures for each scenario:

#### Column A: Exit_Type

- **Options:** Voluntary Resignation, Involuntary Termination, Immediate Dismissal, Retirement, Contract End, Role Change

#### Column B: Notification_Trigger

- **Format:** Event that initiates exit process
- **Example:** HR receives resignation letter

#### Column C: HR_Actions

- **Format:** HR responsibilities during exit
- **Example:** Update HRIS, schedule exit interview, initiate checklist

#### Column D: IT_Actions

- **Format:** IT/IAM responsibilities
- **Example:** Disable accounts, revoke VPN, remove from groups

#### Column E: Manager_Actions

- **Format:** Line manager responsibilities
- **Example:** Coordinate knowledge transfer, approve asset return

#### Column F: Security_Actions

- **Format:** Security team responsibilities
- **Example:** Review access logs, verify no data exfiltration

#### Column G: Timeline

- **Format:** When each action must occur
- **Example:** Access revocation within 24 hours of last day

#### Column H: Documentation_Required

- **Format:** Required documentation
- **Example:** Exit checklist, asset return form, exit interview notes

### Step 3: Complete Access_Revocation Sheet

**Time estimate:** 2-3 hours

Document access revocation requirements:

#### Column A: Access_Type

- **Options:** Physical Access, AD/Directory, Email, VPN, Applications, Cloud Services, Third-Party Systems, Shared Accounts, API Keys

#### Column B: System_Examples

- **Format:** Specific systems of this type
- **Example:** AD, Microsoft Entra ID (formerly Azure AD), Okta

#### Column C: Revocation_Method

- **Format:** How to revoke
- **Example:** Disable in AD, remove from groups

#### Column D: Timeline_Standard

- **Format:** Timeline for standard exits
- **Example:** End of last working day

#### Column E: Timeline_Immediate

- **Format:** Timeline for immediate/hostile exits
- **Example:** Within 1 hour

#### Column F: Verification_Method

- **Format:** How to verify revocation
- **Example:** Login attempt test, access report review

#### Column G: Responsible_Party

- **Format:** Who performs revocation
- **Example:** IAM Team, IT Operations

#### Column H: Dependencies

- **Format:** Other systems affected
- **Example:** SSO-integrated applications automatically disabled

### Step 4: Complete Asset_Recovery Sheet

**Time estimate:** 1-2 hours

Document asset types and recovery process:

#### Column A: Asset_Category

- **Options:** Computing Devices, Mobile Devices, Storage Media, Access Devices, Documentation, Software Licenses

#### Column B: Asset_Examples

- **Format:** Specific asset types
- **Example:** Laptop, desktop, monitor

#### Column C: Return_Method

- **Format:** How asset is returned
- **Example:** In-person handover, courier, drop-off

#### Column D: Verification_Required

- **Format:** What to verify
- **Example:** Serial number match, condition assessment

#### Column E: Data_Handling

- **Format:** Data wiping requirements
- **Example:** Secure erase, factory reset

#### Column F: Timeline

- **Format:** When asset must be returned
- **Example:** By last working day

#### Column G: Non_Return_Action

- **Format:** Action if not returned
- **Example:** Escalate to manager, deduct from final pay, report as lost

### Step 5: Complete Exit_Tracker Sheet

**Time estimate:** Ongoing

Track individual exits:

#### Column A: Exit_ID

- **Format:** EXIT-YYYY-XXX
- **Example:** EXIT-2026-001

#### Column B: Employee_ID

- **Format:** Employee identifier (may be anonymised)

#### Column C: Exit_Type

- Link to Exit_Procedures

#### Column D: Last_Working_Day

- **Format:** DD.MM.YYYY

#### Column E: Access_Revoked_Date

- **Format:** DD.MM.YYYY

#### Column F: Assets_Returned_Date

- **Format:** DD.MM.YYYY

#### Column G: Exit_Interview_Date

- **Format:** DD.MM.YYYY

#### Column H: Checklist_Complete

- **Options:** Yes, Partial, No

#### Column I: Status

- **Options:** In Progress, Complete, Issues Outstanding

#### Column J: Notes

- **Format:** Any issues or exceptions

### Step 6: Complete Leaver_Reconciliation Sheet

**Time estimate:** Monthly (30-60 minutes)

Verify no orphaned accounts:

#### Column A: Review_Date

- **Format:** DD.MM.YYYY

#### Column B: HR_Leavers

- **Format:** Count of HR-recorded leavers in period

#### Column C: Accounts_Disabled

- **Format:** Count of accounts disabled in period

#### Column D: Discrepancies

- **Format:** Number of orphaned accounts found

#### Column E: Orphaned_Accounts

- **Format:** List of orphaned account IDs

#### Column F: Remediation_Action

- **Format:** Action taken for each orphan

#### Column G: Remediation_Date

- **Format:** DD.MM.YYYY

#### Column H: Reviewer

- **Format:** Name of person conducting review

### Step 7: Complete Evidence_Register and Approval Sheets

Follow standard evidence collection and approval processes as per Section 1.9 and 1.12.

---

## Access Revocation Framework

### Access Revocation Scope

Complete access revocation must cover all of the following:

| Access Category | Components | Revocation Method |
|-----------------|------------|-------------------|
| **Physical Access** | Building badges, keys, biometrics | Disable badge, collect keys, remove biometric template |
| **Network Access** | AD/LDAP accounts, VPN, WiFi | Disable account, revoke certificates |
| **Email** | Email account, distribution lists | Disable account, set auto-forward/OOO, remove from lists |
| **Applications** | Business applications, SaaS | Disable/remove user from each application |
| **Cloud Services** | IaaS/PaaS/SaaS (personal and shared) | Remove from tenants, revoke API keys |
| **Remote Access** | VPN, remote desktop, MDM-managed devices | Revoke VPN access, remote wipe if needed |
| **Third-Party Access** | Partner portals, customer systems | Notify partners, request removal |
| **Delegated Access** | Shared mailboxes, service accounts | Remove delegated access |
| **Privileged Access** | Admin accounts, PAM | Immediate revocation, password rotation |

### Access Revocation Timelines

| Exit Type | Physical | Network | Applications | Third-Party |
|-----------|----------|---------|--------------|-------------|
| **Immediate Dismissal** | 1 hour | 1 hour | 1 hour | 24 hours |
| **Termination for Cause** | Same day | Same day | Same day | 24 hours |
| **Voluntary Resignation** | Last day | Last day | Last day | 48 hours |
| **Retirement** | Last day | Last day | Last day | 48 hours |
| **Contract End** | End date | End date | End date | 48 hours |
| **Role Change** | N/A | 2 days | 2 days | As needed |

### Verification Procedures

After revocation, verify access has been removed:

1. **Login Attempt Test** - Attempt login with revoked credentials
2. **Access Report Review** - Generate access report showing no active access
3. **Badge Log Review** - Verify no physical access attempts
4. **Manager Confirmation** - Line manager confirms no residual access needed

---

## Asset Recovery Process

### Asset Categories

#### Computing Devices

| Asset Type | Return Method | Data Handling |
|------------|---------------|---------------|
| Laptop | In-person handover | Secure erase or reimage |
| Desktop | IT collection | Secure erase or reimage |
| Monitor | IT collection | N/A |
| Peripherals | In-person handover | N/A |

#### Mobile Devices

| Asset Type | Return Method | Data Handling |
|------------|---------------|---------------|
| Company Phone | In-person handover | Factory reset |
| Company Tablet | In-person handover | Factory reset |
| BYOD (if MDM) | MDM unenrollment | Selective wipe via MDM |

#### Storage Media

| Asset Type | Return Method | Data Handling |
|------------|---------------|---------------|
| USB Drives | In-person handover | Secure erase or destroy |
| External Drives | In-person handover | Secure erase or destroy |
| Backup Media | In-person handover | Secure erase or destroy |

#### Access Devices

| Asset Type | Return Method | Data Handling |
|------------|---------------|---------------|
| Access Badge | In-person handover | Disable immediately |
| Keys | In-person handover | Re-key if high security |
| Security Tokens | In-person handover | De-provision |
| Smart Cards | In-person handover | Revoke certificates |

#### Documentation

| Asset Type | Return Method | Data Handling |
|------------|---------------|---------------|
| Printed Documents | In-person handover | Secure destruction |
| Technical Manuals | In-person handover | Return to library |
| Customer Materials | In-person handover | Return or destroy |

### Non-Return Procedures

If assets are not returned by the deadline:

1. **Day 1-5 Post-Deadline**: Manager follow-up with former employee
2. **Day 6-10**: HR formal request via registered mail
3. **Day 11-20**: Deduction from final pay (where legal)
4. **Day 21+**: Report as lost/stolen, involve Legal if appropriate
5. **For High-Risk**: Remote wipe, report to authorities

---

## Evidence Collection

### Evidence Requirements

| Evidence Type | Description | Retention Period |
|---------------|-------------|------------------|
| **Exit Procedures** | Documented procedures by type | Current version |
| **Completed Checklists** | Sample completed exit checklists | 7 years |
| **Access Revocation Logs** | System logs showing disablement | 7 years |
| **Asset Return Forms** | Signed asset return acknowledgements | 7 years |
| **Leaver Reconciliation** | Monthly reconciliation reports | 3 years |
| **Exit Interview Records** | Security-related interview notes | 7 years |

### Evidence Storage

**Naming Convention:**
```
EVD-A.6.4-5.2_[EvidenceType]_[YYYYMMDD].[ext]
```

**Examples:**
- `EVD-A.6.4-5.2_ExitChecklist_Sample_20260203.pdf`
- `EVD-A.6.4-5.2_LeaverReconciliation_202601.xlsx`
- `EVD-A.6.4-5.2_AccessRevocationLog_20260203.pdf`

---

## Common Pitfalls

Avoid these common mistakes when implementing employment exit processes:

### Process Design Pitfalls

**MISTAKE**: One process for all exit types
**CORRECT**: Define differentiated processes for voluntary, involuntary, immediate, and role change scenarios; immediate dismissals require accelerated timelines; voluntary resignations allow for knowledge transfer

**MISTAKE**: No defined access revocation timelines
**CORRECT**: Establish SLAs for each access type and exit scenario; document in Access_Revocation sheet; measure and report compliance; escalate breaches

**MISTAKE**: Incomplete access scope
**CORRECT**: Document ALL access types including third-party systems, shared accounts, API keys, and delegated access; maintain complete access inventory; verify all are covered in revocation process

**MISTAKE**: No verification of access revocation
**CORRECT**: Implement verification procedures for each access type; test login attempts; review access reports; document verification in exit checklist

### Asset Management Pitfalls

**MISTAKE**: No tracking of assets assigned to employees
**CORRECT**: Maintain accurate asset inventory linked to employees; update in real-time; include all asset types; reconcile regularly

**MISTAKE**: No data wiping procedures
**CORRECT**: Define data handling requirements for each asset type; implement secure erase for storage devices; verify wiping before reissue; document wiping completion

**MISTAKE**: No procedure for unreturned assets
**CORRECT**: Define escalation process with timelines; include payroll deduction where legal; establish remote wipe capability; involve Legal for high-value items

**MISTAKE**: Ignoring BYOD devices
**CORRECT**: Include BYOD in exit procedures; implement MDM selective wipe; verify company data removed; document employee acknowledgement of data deletion

### Operational Pitfalls

**MISTAKE**: Delayed notification to IT
**CORRECT**: Automate leaver notification from HRIS to IAM; establish SLA for notification (same day for all terminations); include all relevant teams in notification

**MISTAKE**: No orphaned account detection
**CORRECT**: Implement monthly leaver reconciliation; compare HR termination records to active accounts; remediate discrepancies immediately; report metrics to management

**MISTAKE**: Exit interview skipped or incomplete
**CORRECT**: Conduct security-focused exit interview for all voluntary leavers; cover continuing obligations, data deletion confirmation, and badge/key return; document and retain records

**MISTAKE**: Knowledge transfer neglected
**CORRECT**: Identify critical knowledge holders; plan knowledge transfer during notice period; document system access and credentials; update shared account passwords

### Legal Compliance Pitfalls

**MISTAKE**: Ignoring employment law requirements
**CORRECT**: Ensure exit procedures comply with Swiss OR notice periods and termination requirements; consult Legal for involuntary terminations; respect employee rights

**MISTAKE**: No communication of continuing obligations
**CORRECT**: Include NDA reminder in exit interview; provide written summary of continuing obligations; obtain signed acknowledgement; reference ISMS-IMP-A.6.4-5.S3

---

## Quality Checklist

Before submitting the completed assessment:

### Process Framework Checks

- [ ] Exit procedures defined for all exit types
- [ ] Access revocation timelines documented for each scenario
- [ ] Asset recovery procedures comprehensive
- [ ] Knowledge transfer requirements documented
- [ ] Exit interview procedures include security components

### Access Revocation Checks

- [ ] All access types included (physical, network, applications, cloud, third-party)
- [ ] Verification procedures defined
- [ ] Responsible parties assigned
- [ ] Timeline SLAs documented

### Asset Recovery Checks

- [ ] All asset categories covered
- [ ] Data handling requirements defined
- [ ] Non-return escalation procedures documented
- [ ] BYOD exit procedures included

### Compliance Checks

- [ ] Monthly leaver reconciliation process established
- [ ] Orphaned account remediation procedure defined
- [ ] Metrics and reporting defined
- [ ] Integration with HR termination process verified

### Evidence Checks

- [ ] All framework documents stored in Evidence Library
- [ ] Sample completed exits available
- [ ] Leaver reconciliation reports available
- [ ] Evidence naming convention followed

---

## Review and Approval

### Review Process

#### Step 1: Self-Review by Assessor

- Complete Quality Checklist
- Verify all sheets complete
- Check evidence links

#### Step 2: IT/IAM Review

**Reviewer:** IAM Manager
**Timeframe:** 5 business days
**Scope:** Access revocation procedures, technical accuracy

#### Step 3: HR Review

**Reviewer:** HR Director
**Timeframe:** 5 business days
**Scope:** Process integration, employment law compliance

#### Step 4: CISO Approval

**Approver:** CISO
**Timeframe:** 5 business days
**Scope:** Overall security effectiveness

---

## Regulatory Compliance

### Swiss Employment Law

| Requirement | Exit Process Implication |
|-------------|--------------------------|
| **Notice Periods (OR Art. 335)** | Respect contractual notice periods |
| **Certificate of Employment** | Provide upon request |
| **Final Pay** | Settle within legal timeframes |
| **Data Access Rights (nDSG)** | Respond to data subject requests |

### Data Protection

| Requirement | Exit Process Implication |
|-------------|--------------------------|
| **Data Deletion** | Delete personal data no longer needed |
| **BYOD Data** | Remove company data from personal devices |
| **Email Forwarding** | Respect privacy in email handling |

---

## Related Controls

| Control | Relationship |
|---------|--------------|
| **A.5.15-18** IAM | Access revocation integration |
| **A.6.4** Disciplinary | Termination following discipline |
| **A.6.6** NDAs | Post-employment confidentiality |
| **A.8.1** User Endpoints | Asset recovery |

---

**END OF USER GUIDE**

---

*"Beginnings and endings are merely stages in the continuing cycle."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
