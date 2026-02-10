<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.10-11.S2-UG:framework:UG:a.5.10-11 -->
**ISMS-IMP-A.5.10-11.S2-UG - Usage Rules Inventory**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.10: Acceptable Use of Information and Other Associated Assets

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.S2-UG |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.10: Acceptable Use of Information and Other Associated Assets |
| **Parent Policy** | ISMS-POL-A.5.10-11 Asset Usage Lifecycle Policy |
| **Related IMPs** | ISMS-IMP-A.5.10-11.S1, ISMS-IMP-A.5.10-11.S3, ISMS-IMP-A.5.10-11.S4 |
| **Version** | 1.0 |
| **Classification** | Internal Use |
| **Owner** | Information Security Manager |
| **Last Review** | [Date to be set] |
| **Framework Version** | 1.0 |
| **Assessment Type** | Usage Rules Documentation and Inventory |

---

## Control Requirement

> "Rules for the acceptable use of information and other associated assets should be identified, documented and implemented."
>
> — ISO/IEC 27001:2022, Annex A Control 5.10

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.10-11.S2-TG.

---

## Assessment Overview

### Purpose

The Usage Rules Inventory workbook provides a comprehensive catalogue of specific usage rules by asset category. While the Acceptable Use Policy (AUP) provides high-level guidance, this inventory documents the detailed rules that govern day-to-day asset usage.

This workbook documents:
- **Permitted Activities**: What users ARE allowed to do
- **Prohibited Activities**: What users MUST NOT do
- **Conditions and Restrictions**: When and how activities are allowed
- **Handling Requirements**: How assets must be handled by classification
- **Enforcement Methods**: How compliance is monitored and enforced

### Scope

This inventory covers usage rules for:
- All asset categories defined in the asset inventory
- All personnel types (employees, contractors, temporary staff, third parties)
- All usage contexts (office, remote, mobile, travel)
- All data classifications (Public, Internal, Confidential, Restricted)

### Benefits

| Stakeholder | Benefit |
|-------------|---------|
| **ISM** | Comprehensive documentation of all usage rules |
| **Users** | Clear, specific guidance on what they can and cannot do |
| **IT Operations** | Reference for enforcement and monitoring configuration |
| **Legal/HR** | Documented basis for disciplinary actions |
| **Auditors** | Evidence of control implementation |
| **Training** | Content source for awareness materials |

### Assessment Frequency

| Activity | Frequency |
|----------|-----------|
| Full inventory review | Annual |
| Rule updates for new technologies | As needed |
| Enforcement verification | Quarterly |
| Stakeholder validation | Annual |

---

## Control Requirements

### ISO 27001:2022 A.5.10 Requirements

Control A.5.10 requires that acceptable use rules be identified, documented, and implemented:

| Requirement | Implementation |
|-------------|----------------|
| **Identified** | Rules defined for each asset category |
| **Documented** | Rules recorded in this inventory |
| **Implemented** | Rules enforced through technical and administrative controls |

### Rule Types

| Rule Type | Purpose | Example |
|-----------|---------|---------|
| **Permitted** | Defines allowed activities | "Email may be used for business communications" |
| **Permitted with Conditions** | Allowed activities with restrictions | "Personal use permitted during breaks only" |
| **Prohibited** | Explicitly forbidden activities | "Connecting personal storage devices prohibited" |
| **Handling** | Requirements for asset handling | "Confidential data must be encrypted at rest" |

### Rule Quality Criteria

| Criterion | Description | Example |
|-----------|-------------|---------|
| **Specific** | Clearly defined action or behaviour | "Do not share passwords" not "Be careful with passwords" |
| **Actionable** | User knows exactly what to do | "Lock workstation when leaving desk" |
| **Enforceable** | Can be monitored and enforced | Technical control or audit capability exists |
| **Proportionate** | Risk-appropriate | Critical asset rules more stringent |
| **Justified** | Clear reason for the rule | Links to risk or compliance requirement |

---

## Prerequisites

### Required Inputs

Before completing the inventory, gather:

| Prerequisite | Source | Purpose |
|--------------|--------|---------|
| **Approved AUP** | ISMS-POL-A.5.10-11 | Policy framework for rules |
| **Asset Inventory** | ISMS-IMP-A.5.9 | Asset categories requiring rules |
| **Data Classification Scheme** | ISMS-POL-A.5.12 | Classification-based handling |
| **Legal Requirements** | Legal counsel | Regulatory compliance rules |
| **Operational Input** | IT, HR, Operations | Practical rule validation |
| **Previous Inventory** | ISMS Evidence Library | Reference for updates |

### Stakeholder Input Required

| Stakeholder | Input Needed |
|-------------|--------------|
| **IT Security** | Technical enforcement capabilities |
| **IT Operations** | System-specific usage rules |
| **HR** | Employment-related rule implications |
| **Legal** | Regulatory and legal requirements |
| **Asset Owners** | Asset-specific rules |
| **User Representatives** | Practicality validation |

---

## Rule Classification Framework

### Rule Classifications

| Classification | Definition | Consequence Level |
|----------------|------------|-------------------|
| **Permitted** | Activity is allowed without restriction | N/A |
| **Permitted with Conditions** | Allowed under specific circumstances | Varies |
| **Prohibited** | Activity is not allowed under any circumstances | Defined by severity |
| **Not Applicable** | Rule not relevant to this context | N/A |

### Risk-Based Categorisation

For prohibited activities, categorise by risk level:

| Risk Level | Definition | Example | Typical Consequence |
|------------|------------|---------|---------------------|
| **Critical** | Could cause severe harm or legal violation | Data exfiltration | Immediate termination |
| **High** | Significant security or compliance risk | Sharing credentials | Final written warning |
| **Medium** | Moderate risk requiring correction | Unapproved software | Formal warning |
| **Low** | Minor policy deviation | Minor personal use | Verbal coaching |

### Applies-To Matrix

Rules should specify who they apply to:

| Personnel Type | Abbreviation | Notes |
|----------------|--------------|-------|
| All Personnel | ALL | Employees, contractors, temps, third parties |
| Employees | EMP | Full and part-time employees |
| Contractors | CON | External contractors |
| Temporary Staff | TMP | Temporary/agency workers |
| Third Parties | 3P | Vendors, partners, visitors |
| Privileged Users | PRV | System administrators, developers |

---

## Asset Category Rules

### Standard Asset Categories

| Category | Description | Typical Rules Focus |
|----------|-------------|---------------------|
| **Information Assets** | Data, documents, databases | Classification handling, sharing, retention |
| **Software Assets** | Applications, SaaS, tools | Installation, licensing, updates |
| **Hardware Assets** | Laptops, mobiles, peripherals | Physical security, care, loss reporting |
| **Network Assets** | WiFi, VPN, internet access | Usage limits, security requirements |
| **Cloud Services** | M365, AWS, SaaS platforms | Data storage, configuration, sharing |
| **Communication Tools** | Email, messaging, collaboration | Appropriate use, retention, privacy |
| **Physical Media** | USB drives, external storage | Encryption, prohibited use |
| **Authentication Assets** | Passwords, tokens, certificates | Protection, sharing prohibition |
| **Development Assets** | IDEs, repositories, test environments | Code handling, data protection |
| **Personal Devices (BYOD)** | Personal phones, laptops | Separation, security requirements |

### Rule Template Structure

For each asset category, document:

| Element | Description |
|---------|-------------|
| **Rule ID** | Unique identifier (UR-001) |
| **Asset Category** | Which asset type |
| **Rule Description** | Clear statement of the rule |
| **Classification** | Permitted/Permitted with Conditions/Prohibited |
| **Applies To** | Who the rule applies to |
| **Conditions** | Any restrictions or requirements |
| **Enforcement** | How compliance is verified |
| **Consequence** | What happens if violated |
| **Exception Process** | How to request an exception |

---

## Completion Walkthrough

### Step 1: Document Information (Instructions Sheet)

**Objective:** Establish inventory context

**Actions:**
1. Enter inventory date
2. Record author name and role
3. Enter organisation name
4. Specify review period
5. Note related policy version

### Step 2: Usage Rules Master List (Usage_Rules Sheet)

**Objective:** Document all usage rules in a master inventory

**Actions:**
1. Assign unique Rule_ID for each rule
2. Select asset category from dropdown
3. Write clear, specific rule description
4. Classify the rule (Permitted/Permitted with Conditions/Prohibited)
5. Specify who the rule applies to
6. Document enforcement method
7. Note whether monitoring is required
8. Reference the related AUP section

**Rule Writing Guidelines:**

| Good Rule | Why It's Good |
|-----------|---------------|
| "Corporate laptops must be encrypted with approved full-disk encryption" | Specific, actionable, measurable |
| "Email may be used for business communications; limited personal use is permitted during breaks" | Clear permission with defined boundary |
| "Installing software not approved by IT is prohibited" | Clear prohibition with defined scope |

| Poor Rule | Why It's Poor |
|-----------|---------------|
| "Use assets responsibly" | Vague, not actionable |
| "Don't do bad things" | Undefined, unenforceable |
| "Be careful with email" | No specific guidance |

### Step 3: Permitted Activities (Permitted_Activities Sheet)

**Objective:** Document what users ARE allowed to do

**Actions:**
1. For each permitted activity, assign Activity_ID
2. Select the asset category
3. Describe the permitted activity clearly
4. Document any conditions or restrictions
5. Note whether approval is required
6. Specify any time or location restrictions
7. Note documentation requirements

**Examples of Permitted Activities:**

| Asset | Activity | Conditions |
|-------|----------|------------|
| Email | Business communications | Standard business use |
| Email | Limited personal use | During breaks, not excessive |
| Laptop | Working from approved remote locations | VPN must be active |
| Internet | Access to business-related websites | Reasonable business use |
| Cloud Storage | Storing business documents | Use approved services only |

### Step 4: Prohibited Activities (Prohibited_Activities Sheet)

**Objective:** Document what users MUST NOT do

**Actions:**
1. Assign Prohibition_ID
2. Select asset category
3. Describe the prohibited activity clearly
4. Document WHY it's prohibited (risk basis)
5. Assign risk level (Critical/High/Medium/Low)
6. Specify detection method
7. Document consequence for violation
8. Note whether exceptions are possible

**Examples of Prohibited Activities:**

| Asset | Prohibited Activity | Risk Level | Consequence |
|-------|---------------------|------------|-------------|
| All | Sharing login credentials | Critical | Termination |
| Email | Sending Confidential data to personal email | High | Final warning |
| USB | Connecting personal storage devices | High | Written warning |
| Network | Bypassing security controls | Critical | Termination |
| Software | Installing unapproved software | Medium | Formal warning |

### Step 5: Handling Requirements (Handling_Requirements Sheet)

**Objective:** Define how assets must be handled by classification

**Actions:**
1. For each asset-classification combination
2. Define storage requirements
3. Define transmission requirements
4. Define disposal requirements
5. Specify access restrictions
6. Note encryption requirements
7. Specify labelling requirements
8. Note retention period if applicable

**Handling Matrix:**

| Classification | Storage | Transmission | Disposal |
|----------------|---------|--------------|----------|
| **Public** | No restrictions | No restrictions | Standard disposal |
| **Internal** | Access-controlled storage | Internal channels | Shred/secure delete |
| **Confidential** | Encrypted storage | Encrypted transmission | Certified destruction |
| **Restricted** | High-security storage | End-to-end encryption | Witnessed destruction |

### Step 6: Evidence Register (Evidence_Register Sheet)

**Objective:** Link supporting documentation

**Actions:**
1. Create evidence record for each supporting document
2. Link to the rules it supports
3. Record collection date and location
4. Note validity period

### Step 7: Approval (Approval_SignOff Sheet)

**Objective:** Obtain formal inventory approval

**Actions:**
1. Review summary metrics
2. Complete author section
3. Obtain ISM review
4. Obtain CISO approval

---

## Handling Requirements by Classification

### Public Information

| Aspect | Requirement |
|--------|-------------|
| **Storage** | No special requirements |
| **Transmission** | Any method acceptable |
| **Sharing** | May be shared freely |
| **Disposal** | Standard disposal |
| **Encryption** | Not required |
| **Labelling** | Recommended but not required |

### Internal Information

| Aspect | Requirement |
|--------|-------------|
| **Storage** | Access-controlled systems |
| **Transmission** | Internal channels; external with recipient verification |
| **Sharing** | Within organisation; external with business justification |
| **Disposal** | Secure deletion or shredding |
| **Encryption** | Required for external transmission |
| **Labelling** | "Internal" label recommended |

### Confidential Information

| Aspect | Requirement |
|--------|-------------|
| **Storage** | Encrypted storage; limited access |
| **Transmission** | Encrypted channels only |
| **Sharing** | Need-to-know basis; authorisation required |
| **Disposal** | Certified secure destruction |
| **Encryption** | Required at rest and in transit |
| **Labelling** | "Confidential" label required |

### Restricted Information

| Aspect | Requirement |
|--------|-------------|
| **Storage** | High-security systems; dual control |
| **Transmission** | End-to-end encryption; recipient verification |
| **Sharing** | Explicit authorisation; recorded access |
| **Disposal** | Witnessed destruction; certificate |
| **Encryption** | Strong encryption mandatory |
| **Labelling** | "Restricted" label mandatory |

---

## Enforcement and Monitoring

### Enforcement Methods

| Method | Description | Example Use |
|--------|-------------|-------------|
| **Technical** | Automated control preventing violation | USB port blocking |
| **Detective** | Monitoring to identify violations | Log analysis |
| **Procedural** | Process controls | Approval workflows |
| **Physical** | Physical access restrictions | Locked server room |
| **Administrative** | Policy and training | AUP acknowledgement |

### Monitoring Requirements

| Rule Type | Monitoring Need | Method |
|-----------|-----------------|--------|
| **Critical Prohibitions** | Real-time monitoring | SIEM, DLP |
| **High-Risk Prohibitions** | Regular monitoring | Log review, reports |
| **Medium-Risk Rules** | Periodic sampling | Audit sampling |
| **Low-Risk Rules** | Incident-triggered | Complaint investigation |

### Exception Management

| Element | Requirement |
|---------|-------------|
| **Request Process** | Documented exception request form |
| **Approval Authority** | Defined by rule severity |
| **Risk Assessment** | Required for all exceptions |
| **Compensating Controls** | Must be documented |
| **Time Limit** | All exceptions have expiry date |
| **Review** | Periodic review of active exceptions |

---

## Evidence Collection

### Evidence Requirements

| Evidence Type | Description | Retention |
|---------------|-------------|-----------|
| **Inventory Document** | This completed inventory | 3 years |
| **Stakeholder Sign-offs** | Asset owner approvals | 3 years |
| **Legal Review** | Legal validation of rules | 3 years |
| **Technical Configurations** | Enforcement control configs | Current + 1 year |
| **Exception Records** | Approved exceptions | Duration + 2 years |

### Evidence Storage

| Evidence Type | Storage Location | Naming Convention |
|---------------|------------------|-------------------|
| Inventory | ISMS Evidence Library/A.5.10-11/Inventory/ | A.5.10-11.2_Inventory_YYYYMMDD.xlsx |
| Approvals | ISMS Evidence Library/A.5.10-11/Approvals/ | A.5.10-11.2_Approval_[Role]_YYYYMMDD.pdf |
| Exceptions | ISMS Evidence Library/A.5.10-11/Exceptions/ | Exception_[ID]_YYYYMMDD.pdf |

---

## Common Pitfalls

### Rule Quality Pitfalls

❌ **MISTAKE:** Writing vague rules like "use responsibly" or "be careful"
✅ **CORRECT:** Write specific, actionable rules with clear boundaries

❌ **MISTAKE:** Not specifying who the rule applies to
✅ **CORRECT:** Always state applicability (All Personnel, Employees only, etc.)

❌ **MISTAKE:** Rules that conflict with operational needs
✅ **CORRECT:** Validate rules with operational teams before finalising

❌ **MISTAKE:** No enforcement method specified
✅ **CORRECT:** Every rule should explain how compliance is verified

### Prohibited Activity Pitfalls

❌ **MISTAKE:** Missing risk justification for prohibitions
✅ **CORRECT:** Document WHY each activity is prohibited with risk basis

❌ **MISTAKE:** All prohibitions treated with same severity
✅ **CORRECT:** Risk-rate prohibitions; consequences should be proportionate

❌ **MISTAKE:** No exception process for prohibitions
✅ **CORRECT:** Document whether and how exceptions can be requested

❌ **MISTAKE:** Prohibitions without specified consequences
✅ **CORRECT:** Each prohibition should link to defined consequence

### Handling Requirement Pitfalls

❌ **MISTAKE:** Inconsistent handling requirements across classifications
✅ **CORRECT:** Ensure logical progression from Public to Restricted

❌ **MISTAKE:** Requirements that can't be implemented
✅ **CORRECT:** Verify technical and operational feasibility

❌ **MISTAKE:** No encryption requirements for sensitive data
✅ **CORRECT:** Confidential and Restricted must require encryption

❌ **MISTAKE:** Same disposal requirements for all classifications
✅ **CORRECT:** Disposal requirements should increase with sensitivity

### Documentation Pitfalls

❌ **MISTAKE:** Not considering all user types
✅ **CORRECT:** Explicitly address employees, contractors, temps, third parties

❌ **MISTAKE:** Rules that only apply to outdated technology
✅ **CORRECT:** Include current technology (cloud, mobile, remote work)

❌ **MISTAKE:** No review or update cycle defined
✅ **CORRECT:** Define when rules should be reviewed and updated

❌ **MISTAKE:** Not linking rules to AUP policy sections
✅ **CORRECT:** Every rule should reference the supporting AUP section

---

## Quality Checklist

### Pre-Submission Checklist

#### Rule Completeness
- [ ] All asset categories have defined rules
- [ ] Every rule has a unique ID assigned
- [ ] Each rule is specific and actionable
- [ ] Applicability (who) is specified for all rules
- [ ] Enforcement method documented for all rules

#### Permitted Activities
- [ ] Permitted activities have clear conditions documented
- [ ] Approval requirements specified where applicable
- [ ] Time/location restrictions documented where applicable

#### Prohibited Activities
- [ ] Risk justification provided for all prohibitions
- [ ] Risk level assigned to all prohibited activities
- [ ] Detection method specified for each prohibition
- [ ] Consequences documented for all violations
- [ ] Exception possibility indicated for each

#### Handling Requirements
- [ ] All classification levels have handling rules
- [ ] Storage, transmission, disposal requirements defined
- [ ] Encryption requirements clearly specified
- [ ] Labelling requirements documented
- [ ] Requirements are technically feasible

#### Approval
- [ ] Summary metrics reviewed for accuracy
- [ ] Author signature obtained
- [ ] ISM review completed
- [ ] CISO approval obtained
- [ ] Evidence register complete

---

## Review and Approval

### Approval Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    INVENTORY APPROVAL WORKFLOW                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────────┐   │
│  │ Author       │      │ Stakeholder  │      │ ISM/CISO     │   │
│  │ Documents    │─────▶│ Validation   │─────▶│ Approval     │   │
│  │ Rules        │      │ (IT, HR,     │      │              │   │
│  │              │      │  Legal)      │      │              │   │
│  └──────────────┘      └──────────────┘      └──────────────┘   │
│        │                      │                      │          │
│        ▼                      ▼                      ▼          │
│  Draft rules          Validated rules         Final inventory   │
│  documented           confirmed               approved          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Approval Authorities

| Inventory Component | Consulted | Approver |
|---------------------|-----------|----------|
| Usage Rules | Asset Owners | ISM |
| Permitted Activities | IT, Operations | ISM |
| Prohibited Activities | Legal, HR | CISO |
| Handling Requirements | IT, Data Owners | ISM |
| Overall Inventory | All stakeholders | CISO |

### Sign-off Record

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Author | | | |
| IT Review | | | |
| Legal Review | | | |
| HR Review | | | |
| ISM Approval | | | |
| CISO Approval | | | |

---

## Related Controls

### Primary Dependencies

| Control | Relationship | Integration |
|---------|--------------|-------------|
| **A.5.10-11.1** | AUP Assessment | Policy that these rules support |
| **A.5.9** | Asset Inventory | Asset categories requiring rules |
| **A.5.12** | Classification | Classification-based handling |
| **A.5.10-11.3** | Asset Return | Rules for offboarding |
| **A.5.10-11.4** | Compliance Dashboard | Aggregates compliance metrics |

### Related Controls

| Control | Relevance |
|---------|-----------|
| **A.5.1** | Information Security Policy | Parent policy framework |
| **A.6.3** | Awareness and Training | Training on rules |
| **A.8.3** | Information Access Restriction | Technical enforcement |
| **A.8.12** | Data Leakage Prevention | DLP rule enforcement |

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
