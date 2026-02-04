**ISMS-IMP-A.7.10.2 - Media Handling Procedures Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.10: Storage Media

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.10.2 |
| **Version** | 1.0 |
| **Assessment Area** | Media Handling, Transportation & Access Controls |
| **Related Policy** | ISMS-POL-A.7.10, Section 2.3-2.4 (Transportation & Storage) |
| **Purpose** | Assess organisational compliance with storage media handling procedures, transportation security, and access controls throughout the media lifecycle |
| **Target Audience** | IT Operations, Physical Security, Logistics, Compliance Officers, Business Unit Managers, Auditors |
| **Assessment Type** | Process & Operational Compliance |
| **Review Cycle** | Semi-annual (minimum) or After Security Incidents |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Media Handling Procedures assessment workbook | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** IT Operations, Physical Security, Logistics Managers, Compliance Officers

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organisation]'s implementation of **storage media handling procedures** to ensure compliance with ISO/IEC 27001:2022 Control A.7.10 requirements for secure use, transportation, and storage of media.

**Scope:** Complete media handling lifecycle across 5 critical areas:

1. **Media Access Controls** - Who can access media, under what conditions
2. **Transportation Security** - Secure courier, personal transport, chain of custody
3. **Physical Storage Controls** - Secure cabinets, environmental conditions
4. **Media Use Procedures** - Data transfer, scanning, return processes
5. **Incident Response** - Lost/stolen media procedures, escalation

**Assessment Output:** Excel workbook with ~120-180 data points documenting current media handling practices, security controls, and procedural gaps.

## Why This Matters

**ISO 27001:2022 Control A.7.10 Requirement:**
> *"Storage media should be managed through their life cycle of acquisition, use, transportation and disposal in accordance with the organisation's classification scheme and handling requirements."*

**Key Handling Requirements (ISO 27002:2022):**

- Secure transportation with tamper-evident packaging
- Chain of custody documentation
- Environmental protection during storage
- Access controls based on classification
- Malware scanning before use

**Business Impact:**

- **Data Loss Prevention:** Proper handling prevents accidental exposure
- **Chain of Custody:** Critical for legal proceedings and investigations
- **Regulatory Compliance:** GDPR, PCI DSS require handling controls
- **Operational Continuity:** Protected media ensures data availability
- **Audit Evidence:** Documented procedures demonstrate control implementation

## Who Should Complete This Assessment

**Primary Responsibility:** Physical Security Manager / IT Operations Manager

**Required Knowledge:**

- [Organisation]'s media handling procedures
- Physical security zones and access controls
- Transportation and logistics processes
- Incident response procedures
- Environmental monitoring systems

**Support Roles:**

- **IT Operations:** For technical handling procedures
- **Logistics/Facilities:** For transportation and storage
- **Information Security:** For classification-based requirements
- **Legal/Compliance:** For chain of custody requirements
- **HR:** For personnel vetting and training records

## Time Estimate

**Total Assessment Time:** 5-8 hours

**Breakdown:**

- **Access Controls Assessment (1-2 hours):** Document who can access media
- **Transportation Security (1-2 hours):** Review courier and transport procedures
- **Physical Storage Review (1-2 hours):** Inspect storage locations and conditions
- **Use Procedures Assessment (1 hour):** Review data transfer and handling processes
- **Evidence Collection (1 hour):** Gather supporting documentation

## Connection to Policy

This assessment implements **ISMS-POL-A.7.10, Sections 2.3-2.4 (Transportation & Storage)** which defines mandatory requirements for:

- **Courier Requirements:** Approved secure couriers for CONFIDENTIAL media
- **Chain of Custody:** Documentation of media transfers between personnel
- **Physical Storage:** Locked cabinets/safes based on classification
- **Environmental Controls:** Temperature, humidity, magnetic field protection
- **Transport Protocols:** Encryption, hand luggage, tamper-evident packaging

**Policy Authority:** Chief Information Security Officer (CISO)
**Compliance Status:** Mandatory for all storage media containing classified information

---

# Prerequisites

## Access Required

Before starting this assessment, ensure you have access to:

**Documentation:**

- [ ] Media handling procedures and work instructions
- [ ] Transportation security policy
- [ ] Physical security zone definitions
- [ ] Approved courier vendor list
- [ ] Chain of custody forms/templates
- [ ] Incident response procedures for lost media

**Systems:**

- [ ] Physical access control system
- [ ] Environmental monitoring system (temperature, humidity)
- [ ] Visitor management system
- [ ] Courier tracking system (if applicable)
- [ ] Incident management system

**Physical Access:**

- [ ] Secure storage locations (cabinets, safes, vaults)
- [ ] Data centre and server rooms
- [ ] Mailroom and loading dock
- [ ] Off-site storage facilities

## Pre-Assessment Checklist

Complete these tasks before beginning the assessment:

- [ ] **Review current handling procedures** documentation
- [ ] **Obtain approved courier list** from procurement/logistics
- [ ] **Schedule physical walkthrough** of storage locations
- [ ] **Collect chain of custody** form samples
- [ ] **Review incident reports** for media-related events
- [ ] **Check environmental monitoring** logs/reports
- [ ] **Verify personnel authorisation** lists for secure areas

---

# Assessment Workflow

## Workflow Overview

```
Step 1: Media Access Controls (Sheet 2)
   |
Step 2: Transportation Security (Sheet 3)
   |
Step 3: Physical Storage Controls (Sheet 4)
   |
Step 4: Media Use Procedures (Sheet 5)
   |
Step 5: Incident Response (Sheet 6)
   |
Step 6: Evidence Collection (Sheet 8)
   |
Step 7: Review Summary Dashboard (Sheet 7)
   |
Step 8: Quality Check & Approval (Sheet 9)
```

## Step-by-Step Instructions

### Step 1: Media Access Controls (Sheet 2)

**Objective:** Document access control requirements by media classification

**Instructions:**
1. List each access control zone/location in Column A
2. Document Media Classifications Stored in Column B
3. Specify Access Control Type in Column R (Key, Card, Biometric, Combination)
4. List Authorised Personnel/Roles in Column S
5. Document Access Review Frequency in Column T
6. Assess Status in Column F

**Access Control Requirements by Classification:**

| Classification | Storage | Access Control | Access Review |
|----------------|---------|---------------|---------------|
| **CONFIDENTIAL** | Locked safe/cabinet | Named individuals only | Quarterly |
| **INTERNAL** | Locked cabinet | Authorised staff | Semi-annual |
| **PUBLIC** | Standard storage | General access | Annual |

**Detailed Access Control Categories:**

**Physical Key Controls:**
- Key inventory maintained with sign-out log
- Keys returned when access no longer required
- Lost key procedures documented
- Key duplication controlled
- Master key access restricted to security personnel

**Card Access Controls:**
- Access cards programmed per role/classification
- Card access logged automatically
- Lost card reporting and deactivation
- Visitor cards time-limited
- Tailgating prevention measures

**Biometric Controls:**
- Biometric enrollment documented
- Template security (encryption, storage)
- Anti-spoofing measures verified
- Fallback access procedures
- Biometric data retention policy

**Quality Check:**

- Is access appropriate for classification level?
- Are access lists current and reviewed regularly?
- Is segregation of duties maintained?
- Are temporary access procedures defined?
- Is visitor access logged and supervised?
- Are after-hours access procedures documented?

### Step 2: Transportation Security (Sheet 3)

**Objective:** Assess security controls for media in transit

**Instructions:**
1. Document each transportation scenario in Column A
2. Specify Transportation Method in Column R (Courier, Personal, Internal Mail)
3. Document Chain of Custody Requirements in Column S
4. Assess Packaging Requirements in Column T
5. Evaluate Status in Column F

**Transportation Requirements:**

**Secure Courier (CONFIDENTIAL):**
- Approved courier vendors only
- Tamper-evident packaging
- Tracking and delivery confirmation
- Recipient acknowledgment required

**Personal Transport:**
- Media carried in hand luggage (not checked)
- Encryption mandatory
- Not left unattended
- Avoid high-risk areas

**Internal Transfer:**
- Chain of custody documentation
- Secure internal pouch/container
- Direct handoff preferred

**Detailed Transportation Scenarios:**

**International Shipments:**
- Export control compliance verification
- Customs declaration requirements
- Country-specific regulations
- Encryption laws in destination country
- Extended transit time considerations

**Domestic Shipments:**
- Standard vs. expedited delivery options
- Insurance requirements
- Signature requirements
- Weekend/holiday procedures
- Rural vs. urban delivery considerations

**Intra-Office Transfers:**
- Same-building procedures
- Different-building procedures
- Campus delivery procedures
- Secure mail room usage
- Interoffice envelope security

**Quality Check:**

- Are approved couriers documented and used?
- Is chain of custody maintained for all transfers?
- Are packaging requirements followed?
- Is encryption applied for transported CONFIDENTIAL media?
- Are international transfers compliant with export regulations?
- Is insurance adequate for media value?

### Step 3: Physical Storage Controls (Sheet 4)

**Objective:** Assess physical storage security and environmental controls

**Instructions:**
1. List each storage location in Column A
2. Document Storage Type in Column R (Cabinet, Safe, Vault, Server Room)
3. Specify Environmental Monitoring in Column S
4. Record Fire Suppression Type in Column T
5. Assess Status in Column F

**Storage Requirements by Classification:**

| Classification | Storage Type | Environmental | Fire Protection |
|----------------|-------------|---------------|-----------------|
| **CONFIDENTIAL** | Fire-rated safe | Temperature/Humidity monitored | Gas suppression |
| **INTERNAL** | Locked cabinet | Standard office conditions | Sprinkler acceptable |
| **PUBLIC** | Standard storage | N/A | Standard protection |

**Environmental Protection:**
- Temperature: 18-24°C (64-75°F) optimal
- Humidity: 30-50% relative humidity
- Magnetic fields: Away from strong magnetic sources
- Backup media: Stored separately from primary systems

**Detailed Storage Considerations:**

**Media Room Requirements:**
- Dedicated media storage room for CONFIDENTIAL
- Controlled access with logging
- No food or beverages permitted
- Anti-static flooring/mats
- Adequate lighting for inspection
- Emergency lighting provisions

**Cabinet Specifications:**
- Fire rating (minimum 1-hour for CONFIDENTIAL)
- Lock type and key control
- Capacity management
- Labelling requirements
- Cabinet location security

**Vault Requirements (Highly Sensitive):**
- Construction specifications (walls, door, ceiling)
- Combination management
- Dual control access
- Intrusion detection
- CCTV monitoring

**Quality Check:**

- Are storage locations appropriate for classification?
- Is environmental monitoring in place for sensitive media?
- Are fire suppression systems appropriate?
- Is backup media stored off-site or separately?
- Are storage capacities adequate?
- Is labelling consistent and accurate?

### Step 4: Media Use Procedures (Sheet 5)

**Objective:** Assess operational procedures for media use

**Instructions:**
1. Document each use procedure in Column A
2. Specify Applicable Media Type in Column R
3. Document Procedure Owner in Column S
4. Record Last Review Date in Column H
5. Assess Status in Column F

**Key Use Procedures:**

**Data Transfer:**
- Encryption before transfer to removable media
- Management approval for CONFIDENTIAL transfers
- Transfer logs maintained
- Data removed when no longer required

**Media Receipt:**
- Malware scan before use
- Verify sender authenticity
- Document in chain of custody
- Store appropriately based on content

**Media Return:**
- Verify data no longer required
- Secure erase or return for secure disposal
- Update asset records
- Close chain of custody

**Detailed Use Procedure Scenarios:**

**Workstation Connection:**
- Authorised USB port usage
- Endpoint protection interaction
- Data loss prevention controls
- Audit logging of connections

**Server/System Backup:**
- Rotation schedule compliance
- Label application and verification
- Off-site transport timing
- Verification of successful backup

**Archive Retrieval:**
- Request and approval process
- Media condition verification
- Read verification before release
- Return and re-archive procedures

**Quality Check:**

- Are data transfer procedures documented and followed?
- Is malware scanning performed on incoming media?
- Are return procedures enforced?
- Is encryption applied before transfer?
- Are use procedures reviewed regularly?
- Is training provided on handling procedures?

### Step 5: Incident Response (Sheet 6)

**Objective:** Assess lost/stolen media procedures and incident response

**Instructions:**
1. Document each incident scenario in Column A
2. Specify Response Procedure in Column R
3. Document Escalation Path in Column S
4. Record Notification Requirements in Column T
5. Assess Status in Column F

**Incident Types:**

- **Lost Media:** Accidental loss during transit or use
- **Stolen Media:** Theft from person or location
- **Damaged Media:** Physical or data corruption
- **Unauthorised Access:** Improper access to media
- **Breach Discovery:** Evidence of data compromise

**Response Requirements:**

1. Immediate report to IT Operations + Line Manager
2. Escalation to CISO for CONFIDENTIAL media
3. Breach assessment (data types affected)
4. Regulatory notification evaluation
5. Documentation and lessons learned

**Detailed Incident Response Procedures:**

**Lost Media Response:**
- Immediate search and recovery attempts
- Timeline documentation (last known location/time)
- Data classification determination
- Encryption status verification
- Regulatory notification assessment

**Stolen Media Response:**
- Police report filing (if warranted)
- Insurance claim initiation
- Remote wipe capability (if applicable)
- Physical security review
- Pattern analysis (targeted vs. opportunistic)

**Damaged Media Response:**
- Damage assessment and documentation
- Data recovery attempts
- Forensic analysis (if suspicious)
- Replacement procurement
- Root cause analysis

**Quality Check:**

- Are incident response procedures documented?
- Is escalation path clear for different scenarios?
- Are notification requirements understood?
- Are incidents logged and reviewed?
- Are lessons learned incorporated?
- Is incident response tested periodically?

---

# Common Pitfalls

## 1. No Chain of Custody Documentation

**❌ MISTAKE:** Transferring media without documenting handoffs

**Why This Fails:**
- Cannot prove who had media at time of incident
- Legal admissibility of evidence compromised
- Audit finding for missing controls

**✅ Prevention:**
- Use chain of custody forms for all transfers
- Digital tracking for courier shipments
- Acknowledgment of receipt required

## 2. Inadequate Transportation Security

**❌ MISTAKE:** Using standard mail or unauthorised couriers for CONFIDENTIAL media

**Why This Fails:**
- Media may be lost, delayed, or intercepted
- No tamper evidence or tracking
- Policy violation

**✅ Prevention:**
- Maintain approved courier list
- Use tamper-evident packaging
- Require tracking and delivery confirmation

## 3. Environmental Control Gaps

**❌ MISTAKE:** Storing backup tapes in unsuitable conditions

**Why This Fails:**
- Magnetic media degrades in improper conditions
- Data loss from environmental damage
- Recovery may fail when needed

**✅ Prevention:**
- Monitor temperature and humidity
- Use appropriate storage containers
- Regular media integrity verification

## 4. Missing Access Reviews

**❌ MISTAKE:** Access lists not reviewed after personnel changes

**Why This Fails:**
- Former employees may retain access
- Excessive privileges accumulate
- Segregation of duties compromised

**✅ Prevention:**
- Quarterly access reviews for CONFIDENTIAL storage
- Immediate revocation on personnel change
- Least privilege principle enforced

## 5. No Malware Scanning

**❌ MISTAKE:** Using received media without scanning

**Why This Fails:**
- Malware introduction to network
- AutoRun exploits
- Compliance violation

**✅ Prevention:**
- Mandatory scanning of all incoming media
- Disable AutoRun/AutoPlay
- Quarantine procedures for suspicious media

## 6. Incident Response Not Tested

**❌ MISTAKE:** Lost media procedures exist but never exercised

**Why This Fails:**
- Staff unsure of actions during real incident
- Response delays increase damage
- Notification deadlines may be missed

**✅ Prevention:**
- Annual tabletop exercises
- Clear escalation contacts
- Regular procedure reviews

## 7. Personal Transport Violations

**❌ MISTAKE:** Media in checked baggage during travel

**Why This Fails:**
- Theft and loss risk in baggage handling
- Temperature extremes in cargo hold
- No visibility during transit

**✅ Prevention:**
- Policy requiring hand luggage only
- Encryption mandatory for travel
- Travel notification to security

## 8. Inconsistent Packaging

**❌ MISTAKE:** Different packaging standards used by departments

**Why This Fails:**
- Some media inadequately protected
- Tamper evidence inconsistent
- Confusion about requirements

**✅ Prevention:**
- Standardised packaging supplies
- Packaging guidance by classification
- Centralised media shipping function

## 9. Uncontrolled Key Distribution

**❌ MISTAKE:** Cabinet keys duplicated without authorisation

**Why This Fails:**
- Access control circumvented
- No accountability for key holders
- Unauthorised access possible

**✅ Prevention:**
- Key duplication prohibited (controlled blanks)
- Key sign-out register maintained
- Regular key inventory audits

## 10. Missing Visitor Escort Procedures

**❌ MISTAKE:** Visitors left unescorted in media storage areas

**Why This Fails:**
- Unauthorised access opportunity
- Theft or tampering risk
- No accountability for visitor actions

**✅ Prevention:**
- Mandatory escort in secure areas
- Visitor badges clearly visible
- Sign-in/sign-out logging

## 11. Inadequate After-Hours Security

**❌ MISTAKE:** Storage areas accessible after business hours without additional controls

**Why This Fails:**
- Reduced surveillance during off-hours
- Delayed incident detection
- Opportunistic theft risk

**✅ Prevention:**
- After-hours access logging and alerting
- Additional approval required
- CCTV review of off-hours access

## 12. No Emergency Evacuation Procedures for Media

**❌ MISTAKE:** No plan for protecting media during emergency evacuations

**Why This Fails:**
- Media left unsecured during evacuation
- Recovery planning impaired
- Business continuity compromised

**✅ Prevention:**
- Media protection in emergency procedures
- Designated personnel for media security
- Post-incident media verification

## 13. Cross-Contamination of Classifications

**❌ MISTAKE:** CONFIDENTIAL and PUBLIC media stored in same location

**Why This Fails:**
- Handling confusion
- Misapplication of controls
- Audit finding for control weakness

**✅ Prevention:**
- Physically separate storage by classification
- Clear labelling of storage areas
- Regular storage audits

## 14. Unverified Courier Credentials

**❌ MISTAKE:** Releasing media to couriers without verifying identity

**Why This Fails:**
- Social engineering attack vector
- Media diverted to unauthorised parties
- Chain of custody broken

**✅ Prevention:**
- Courier identification verification
- Known courier personnel where possible
- Photo ID and company verification

## 15. Missing Insurance Documentation

**❌ MISTAKE:** Media transported without adequate insurance coverage

**Why This Fails:**
- Financial loss if media lost/damaged
- Data recovery costs not covered
- Business impact unmitigated

**✅ Prevention:**
- Insurance requirements in courier contracts
- Coverage verification before shipment
- Claims process documented

## 16. No Media Handling Training

**❌ MISTAKE:** Staff handling media without formal training

**Why This Fails:**
- Procedures unknown or ignored
- Inconsistent handling practices
- Increased incident risk

**✅ Prevention:**
- Mandatory handling training for relevant staff
- Training records maintained
- Refresher training scheduled

## 17. Uncontrolled Media Pooling

**❌ MISTAKE:** Shared media pools without individual accountability

**Why This Fails:**
- Cannot track who used specific media
- No accountability for data on media
- Chain of custody impossible

**✅ Prevention:**
- Individual media assignment
- Check-out/check-in logging
- Regular pool inventory

## 18. Delayed Incident Reporting

**❌ MISTAKE:** Media loss not reported promptly

**Why This Fails:**
- Notification deadlines missed
- Recovery opportunities lost
- Investigation compromised

**✅ Prevention:**
- Clear reporting timelines (e.g., within 1 hour)
- Multiple reporting channels
- No-blame reporting culture

---

# Quality Checklist

Before submitting assessment for approval, verify:

## Completeness

- [ ] All handling scenarios documented
- [ ] All sheets completed (no "TBD" or blank sections)
- [ ] Evidence Register populated
- [ ] Summary Dashboard reviewed
- [ ] All access control zones identified
- [ ] All transportation methods documented
- [ ] All storage locations assessed

## Accuracy

- [ ] Procedures verified against actual practice
- [ ] Access lists current and validated
- [ ] Environmental monitoring verified
- [ ] Courier vendors confirmed approved
- [ ] Key inventory reconciled
- [ ] Storage capacities verified
- [ ] Insurance coverage confirmed

## Compliance

- [ ] Chain of custody procedures in place
- [ ] Transportation security appropriate for classification
- [ ] Physical storage meets requirements
- [ ] Incident response procedures documented
- [ ] Access review schedule documented
- [ ] Visitor procedures verified
- [ ] Emergency procedures address media

## Remediation Planning

- [ ] Gaps identified with remediation timeline
- [ ] Procedure updates scheduled
- [ ] Training needs identified
- [ ] Budget/resource requirements flagged
- [ ] Quick wins identified
- [ ] Long-term improvements planned

## Evidence Quality

- [ ] All evidence properly referenced
- [ ] Evidence dated and attributed
- [ ] Evidence accessible for audit
- [ ] Photographic evidence where appropriate
- [ ] Procedure documents version controlled
- [ ] Training records current

## Stakeholder Input

- [ ] Physical Security input obtained
- [ ] IT Operations input obtained
- [ ] Facilities input obtained
- [ ] Logistics input obtained
- [ ] Legal/Compliance input obtained

---

# Review & Approval

## Approval Workflow (Sheet 9)

**Level 1: Technical/Operational Approval**

- **Approver:** Physical Security Manager / IT Operations Manager
- **Validates:** Procedure accuracy, practical applicability
- **Approval Criteria:** Assessment reflects current handling practices

**Level 2: Management Approval**

- **Approver:** CISO / COO
- **Validates:** Compliance posture, remediation plans
- **Approval Criteria:** Gaps have realistic remediation plans

**Level 3: Executive Approval**

- **Approver:** Executive Management
- **Validates:** Overall handling posture, risk acceptance
- **Approval Criteria:** Executive acknowledges handling compliance status

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Python Developers, Excel Workbook Designers, ISMS Implementation Technical Teams

---

# Workbook Structure Overview

## Sheet Organisation (9 Sheets Total)

| Sheet # | Sheet Name | Purpose | Rows | User Entry |
|---------|------------|---------|------|------------|
| 1 | Instructions & Legend | Assessment guidance, colour coding | ~60 | Read-only |
| 2 | 2. Media Access Controls | Access requirements by zone/classification | ~25-50 | 13 data rows |
| 3 | 3. Transportation Security | Courier, transport, chain of custody | ~25-50 | 13 data rows |
| 4 | 4. Physical Storage Controls | Storage locations, environmental | ~25-50 | 13 data rows |
| 5 | 5. Media Use Procedures | Operational handling procedures | ~25-50 | 13 data rows |
| 6 | 6. Incident Response | Lost/stolen media procedures | ~25-50 | 13 data rows |
| 7 | Summary Dashboard | Compliance metrics overview | ~60 | Formula-driven |
| 8 | Evidence Register | Supporting documentation | ~110 | 100 data rows |
| 9 | Approval Sign-Off | Three-level approval workflow | ~75 | Text entry |

---

# Sheet 1: Instructions & Legend

## Layout Structure

**Header Section (Rows 1-5)**
- Document title and ID
- Assessment date and version
- Organisation name placeholder

**Purpose Section (Rows 7-15)**
- Assessment objectives
- Scope definition
- Related policy reference

**Legend Section (Rows 17-35)**
- Status dropdown values and meanings
- Colour coding explanation
- Column header definitions

**Completion Guidelines (Rows 37-55)**
- Step-by-step workflow
- Time estimates
- Support contacts

**Column Width Specifications:**
| Column | Width | Content |
|--------|-------|---------|
| A | 15 | Section headers |
| B | 60 | Description text |
| C | 15 | Status/Values |

---

# Sheet 2: Media Access Controls

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Zone/Location | 25 | Text | Storage area identifier |
| B | Classification Stored | 18 | Dropdown | CONFIDENTIAL/INTERNAL/PUBLIC |
| C | Control Description | 35 | Text | Access control description |
| D | Requirement Reference | 15 | Text | Policy reference |
| E | Assessment Criteria | 30 | Text | How compliance measured |
| F | Status | 15 | Dropdown | Compliant/Partial/Non-Compliant/N/A |
| G | Assessor | 15 | Text | Who assessed |
| H | Assessment Date | 12 | Date | When assessed |
| I | Evidence Reference | 15 | Text | Evidence ID |
| J | Gap Description | 30 | Text | If non-compliant |
| K | Risk Level | 12 | Dropdown | Critical/High/Medium/Low |
| L | Remediation Action | 30 | Text | Planned fix |
| M | Remediation Owner | 15 | Text | Who responsible |
| N | Target Date | 12 | Date | Planned completion |
| O | Remediation Status | 15 | Dropdown | Not Started/In Progress/Complete |
| P | Verification | 20 | Text | How verified |
| Q | Notes | 25 | Text | Additional comments |
| R | Access Control Type | 22 | Dropdown | Key Lock / Card Access / Biometric / Combination |
| S | Authorised Personnel | 25 | Text | Roles or named individuals |
| T | Review Frequency | 18 | Dropdown | Monthly / Quarterly / Semi-annual / Annual |

## Data Validation Rules

**Column B - Classification:**
```
Dropdown: CONFIDENTIAL, INTERNAL, PUBLIC, MIXED, N/A
```

**Column F - Status:**
```
Dropdown: Compliant, Partially Compliant, Non-Compliant, Not Assessed, N/A
```

**Column K - Risk Level:**
```
Dropdown: Critical, High, Medium, Low, N/A
```

**Column O - Remediation Status:**
```
Dropdown: Not Started, In Progress, On Hold, Complete, Verified
```

**Column R - Access Control Type:**
```
Dropdown: Key Lock, Card Access, Biometric, Combination Lock, Multi-Factor, PIN Code, None
```

**Column T - Review Frequency:**
```
Dropdown: Monthly, Quarterly, Semi-annual, Annual, Ad-hoc
```

## Conditional Formatting

**Status Column (F):**
- Compliant: Green fill (#C6EFCE)
- Partially Compliant: Yellow fill (#FFEB9C)
- Non-Compliant: Red fill (#FFC7CE)
- Not Assessed: Grey fill (#D9D9D9)

**Risk Level Column (K):**
- Critical: Dark red fill (#8B0000), white text
- High: Red fill (#FF0000)
- Medium: Orange fill (#FFA500)
- Low: Yellow fill (#FFFF00)

---

# Sheet 3: Transportation Security

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Transportation Scenario | 30 | Text | Scenario description |
| B | Classification Level | 18 | Dropdown | Media classification |
| C | Control Description | 35 | Text | Required controls |
| D | Requirement Reference | 15 | Text | Policy reference |
| E | Assessment Criteria | 30 | Text | How compliance measured |
| F | Status | 15 | Dropdown | Compliant/Partial/Non-Compliant/N/A |
| G | Assessor | 15 | Text | Who assessed |
| H | Assessment Date | 12 | Date | When assessed |
| I | Evidence Reference | 15 | Text | Evidence ID |
| J | Gap Description | 30 | Text | If non-compliant |
| K | Risk Level | 12 | Dropdown | Critical/High/Medium/Low |
| L | Remediation Action | 30 | Text | Planned fix |
| M | Remediation Owner | 15 | Text | Who responsible |
| N | Target Date | 12 | Date | Planned completion |
| O | Remediation Status | 15 | Dropdown | Status |
| P | Verification | 20 | Text | How verified |
| Q | Notes | 25 | Text | Additional comments |
| R | Transport Method | 22 | Dropdown | Transport type |
| S | Chain of Custody Required | 20 | Dropdown | Yes/No/Partial |
| T | Packaging Requirement | 25 | Dropdown | Packaging type |

## Data Validation Rules

**Column R - Transport Method:**
```
Dropdown: Secure Courier, Standard Courier, Personal Transport, Internal Mail, Hand Delivery, Digital Transfer, N/A
```

**Column S - Chain of Custody Required:**
```
Dropdown: Yes - Full Documentation, Yes - Basic Log, No, N/A
```

**Column T - Packaging Requirement:**
```
Dropdown: Tamper-Evident Packaging, Sealed Container, Locked Case, Standard Packaging, N/A
```

---

# Sheet 4: Physical Storage Controls

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Storage Location | 25 | Text | Location identifier |
| B | Classification Stored | 18 | Dropdown | Classification level |
| C | Control Description | 35 | Text | Storage controls |
| D | Requirement Reference | 15 | Text | Policy reference |
| E | Assessment Criteria | 30 | Text | How compliance measured |
| F | Status | 15 | Dropdown | Compliant/Partial/Non-Compliant/N/A |
| G | Assessor | 15 | Text | Who assessed |
| H | Assessment Date | 12 | Date | When assessed |
| I | Evidence Reference | 15 | Text | Evidence ID |
| J | Gap Description | 30 | Text | If non-compliant |
| K | Risk Level | 12 | Dropdown | Critical/High/Medium/Low |
| L | Remediation Action | 30 | Text | Planned fix |
| M | Remediation Owner | 15 | Text | Who responsible |
| N | Target Date | 12 | Date | Planned completion |
| O | Remediation Status | 15 | Dropdown | Status |
| P | Verification | 20 | Text | How verified |
| Q | Notes | 25 | Text | Additional comments |
| R | Storage Type | 22 | Dropdown | Cabinet/Safe/Vault |
| S | Environmental Monitoring | 22 | Dropdown | Monitoring type |
| T | Fire Suppression | 20 | Dropdown | Suppression type |

## Data Validation Rules

**Column R - Storage Type:**
```
Dropdown: Locked Cabinet, Fire-Rated Safe, Secure Vault, Server Room, Archive Room, Standard Shelf, Secure Disposal Bin
```

**Column S - Environmental Monitoring:**
```
Dropdown: Temperature Only, Humidity Only, Temperature + Humidity, Full Environmental, None
```

**Column T - Fire Suppression:**
```
Dropdown: Gas Suppression, Wet Sprinkler, Dry Sprinkler, Fire Extinguisher, None
```

---

# Sheet 5: Media Use Procedures

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Use Procedure | 30 | Text | Procedure description |
| B | Procedure Type | 18 | Dropdown | Data Transfer/Receipt/Return/Archive |
| C | Control Description | 35 | Text | Required controls |
| D | Requirement Reference | 15 | Text | Policy reference |
| E | Assessment Criteria | 30 | Text | How compliance measured |
| F | Status | 15 | Dropdown | Compliant/Partial/Non-Compliant/N/A |
| G | Assessor | 15 | Text | Who assessed |
| H | Assessment Date | 12 | Date | When assessed |
| I | Evidence Reference | 15 | Text | Evidence ID |
| J | Gap Description | 30 | Text | If non-compliant |
| K | Risk Level | 12 | Dropdown | Critical/High/Medium/Low |
| L | Remediation Action | 30 | Text | Planned fix |
| M | Remediation Owner | 15 | Text | Who responsible |
| N | Target Date | 12 | Date | Planned completion |
| O | Remediation Status | 15 | Dropdown | Status |
| P | Verification | 20 | Text | How verified |
| Q | Notes | 25 | Text | Additional comments |
| R | Applicable Media Type | 22 | Dropdown | Media type |
| S | Procedure Owner | 20 | Text | Role responsible |
| T | Training Required | 18 | Dropdown | Training needs |

## Data Validation Rules

**Column R - Applicable Media Type:**
```
Dropdown: Removable Media, Fixed Storage, Cloud Storage, Paper Documents, All Media Types
```

**Column T - Training Required:**
```
Dropdown: Yes - Initial Only, Yes - Annual Refresh, Yes - Quarterly, No, Role-Specific
```

---

# Sheet 6: Incident Response

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Incident Scenario | 30 | Text | Scenario description |
| B | Incident Type | 18 | Dropdown | Lost/Stolen/Damaged/Breach |
| C | Control Description | 35 | Text | Response requirements |
| D | Requirement Reference | 15 | Text | Policy reference |
| E | Assessment Criteria | 30 | Text | How compliance measured |
| F | Status | 15 | Dropdown | Compliant/Partial/Non-Compliant/N/A |
| G | Assessor | 15 | Text | Who assessed |
| H | Assessment Date | 12 | Date | When assessed |
| I | Evidence Reference | 15 | Text | Evidence ID |
| J | Gap Description | 30 | Text | If non-compliant |
| K | Risk Level | 12 | Dropdown | Critical/High/Medium/Low |
| L | Remediation Action | 30 | Text | Planned fix |
| M | Remediation Owner | 15 | Text | Who responsible |
| N | Target Date | 12 | Date | Planned completion |
| O | Remediation Status | 15 | Dropdown | Status |
| P | Verification | 20 | Text | How verified |
| Q | Notes | 25 | Text | Additional comments |
| R | Response Procedure | 25 | Text | Procedure reference |
| S | Escalation Path | 25 | Text | Escalation contacts |
| T | Notification Required | 22 | Dropdown | Notification needs |

## Data Validation Rules

**Column B - Incident Type:**
```
Dropdown: Lost Media, Stolen Media, Damaged Media, Unauthorised Access, Data Breach, Multiple
```

**Column T - Notification Required:**
```
Dropdown: Regulatory (GDPR/FINMA), Internal Only, Both Internal + Regulatory, None, To Be Determined
```

---

# Sheet 7: Summary Dashboard

## Dashboard Sections

**Section 1: Control Status Overview (Rows 3-12)**
- Access controls assessed
- Transportation controls assessed
- Storage controls assessed
- Use procedures assessed
- Incident procedures assessed

**Section 2: Compliance Metrics (Rows 14-25)**
- Procedures with documentation %
- Procedures with training %
- Procedures tested/exercised %
- Gap remediation in progress

**Section 3: Risk Distribution (Rows 27-35)**
- Critical gaps count
- High-risk gaps count
- Medium-risk gaps count
- Low-risk gaps count

**Section 4: Key Indicators (Rows 37-50)**
- Chain of custody compliance %
- Approved courier usage %
- Environmental monitoring coverage %
- Incident response tested (date)

**Formula Examples:**

**Compliance Percentage:**
```
=COUNTIF('2. Media Access Controls'!$F$4:$F$16,"Compliant")/COUNTA('2. Media Access Controls'!$F$4:$F$16)
```

**Risk Count:**
```
=COUNTIF('2. Media Access Controls'!$K$4:$K$16,"Critical")
```

## Dashboard Styling

**Header Row:**
- Font: Calibri 14pt Bold
- Fill: Navy Blue (#003366)
- Text: White

**Metric Labels:**
- Font: Calibri 11pt
- Fill: Light Grey (#F2F2F2)

**Metric Values:**
- Font: Calibri 12pt Bold
- Conditional formatting by threshold

---

# Sheet 8: Evidence Register

## Column Structure

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Evidence ID | 12 | Text | Unique identifier (EV-001) |
| B | Evidence Type | 18 | Dropdown | Document/Screenshot/Photo/Log |
| C | Description | 35 | Text | What evidence shows |
| D | Related Control | 15 | Text | Control reference |
| E | Source Sheet | 15 | Text | Assessment sheet |
| F | Date Collected | 12 | Date | Collection date |
| G | Collected By | 15 | Text | Who collected |
| H | File Name | 25 | Text | Document name |
| I | Location | 30 | Text | Storage location/link |
| J | Retention | 12 | Text | Retention period |
| K | Notes | 25 | Text | Additional context |

## Data Validation

**Column B - Evidence Type:**
```
Dropdown: Policy Document, Procedure Document, Screenshot, Photograph, System Log, Certificate, Training Record, Audit Report, Other
```

---

# Sheet 9: Approval Sign-Off

## Layout Structure

**Document Control (Rows 3-12)**
- Assessment title and ID
- Assessment date
- Period covered
- Prepared by

**Assessment Summary (Rows 14-25)**
- Overall compliance status
- Critical findings
- Key recommendations

**Approval Section (Rows 27-60)**

**Level 1 Approval:**
- Title: Technical/Operational Approval
- Statement: "I confirm this assessment accurately reflects current handling practices."
- Fields: Name, Title, Signature, Date, Comments

**Level 2 Approval:**
- Title: Management Approval
- Statement: "I approve this assessment and the remediation plan."
- Fields: Name, Title, Signature, Date, Comments

**Level 3 Approval:**
- Title: Executive Approval
- Statement: "Executive Management acknowledges the handling compliance status."
- Fields: Name, Title, Signature, Date, Risk Acceptance

**Next Review (Rows 62-70)**
- Scheduled review date
- Review owner
- Review scope

---

**END OF SPECIFICATION**

---

*"Security is not a product, but a process."*
— Bruce Schneier

<!-- QA_VERIFIED: 2026-02-03 -->
