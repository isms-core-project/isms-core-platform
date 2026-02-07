**ISMS-IMP-A.7.10.2-UG - Media Handling Procedures Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.10: Storage Media

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.10.2-UG |
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

## No Chain of Custody Documentation

**❌ MISTAKE:** Transferring media without documenting handoffs

**Why This Fails:**
- Cannot prove who had media at time of incident
- Legal admissibility of evidence compromised
- Audit finding for missing controls

**✅ Prevention:**
- Use chain of custody forms for all transfers
- Digital tracking for courier shipments
- Acknowledgment of receipt required

## Inadequate Transportation Security

**❌ MISTAKE:** Using standard mail or unauthorised couriers for CONFIDENTIAL media

**Why This Fails:**
- Media may be lost, delayed, or intercepted
- No tamper evidence or tracking
- Policy violation

**✅ Prevention:**
- Maintain approved courier list
- Use tamper-evident packaging
- Require tracking and delivery confirmation

## Environmental Control Gaps

**❌ MISTAKE:** Storing backup tapes in unsuitable conditions

**Why This Fails:**
- Magnetic media degrades in improper conditions
- Data loss from environmental damage
- Recovery may fail when needed

**✅ Prevention:**
- Monitor temperature and humidity
- Use appropriate storage containers
- Regular media integrity verification

## Missing Access Reviews

**❌ MISTAKE:** Access lists not reviewed after personnel changes

**Why This Fails:**
- Former employees may retain access
- Excessive privileges accumulate
- Segregation of duties compromised

**✅ Prevention:**
- Quarterly access reviews for CONFIDENTIAL storage
- Immediate revocation on personnel change
- Least privilege principle enforced

## No Malware Scanning

**❌ MISTAKE:** Using received media without scanning

**Why This Fails:**
- Malware introduction to network
- AutoRun exploits
- Compliance violation

**✅ Prevention:**
- Mandatory scanning of all incoming media
- Disable AutoRun/AutoPlay
- Quarantine procedures for suspicious media

## Incident Response Not Tested

**❌ MISTAKE:** Lost media procedures exist but never exercised

**Why This Fails:**
- Staff unsure of actions during real incident
- Response delays increase damage
- Notification deadlines may be missed

**✅ Prevention:**
- Annual tabletop exercises
- Clear escalation contacts
- Regular procedure reviews

## Personal Transport Violations

**❌ MISTAKE:** Media in checked baggage during travel

**Why This Fails:**
- Theft and loss risk in baggage handling
- Temperature extremes in cargo hold
- No visibility during transit

**✅ Prevention:**
- Policy requiring hand luggage only
- Encryption mandatory for travel
- Travel notification to security

## Inconsistent Packaging

**❌ MISTAKE:** Different packaging standards used by departments

**Why This Fails:**
- Some media inadequately protected
- Tamper evidence inconsistent
- Confusion about requirements

**✅ Prevention:**
- Standardised packaging supplies
- Packaging guidance by classification
- Centralised media shipping function

## Uncontrolled Key Distribution

**❌ MISTAKE:** Cabinet keys duplicated without authorisation

**Why This Fails:**
- Access control circumvented
- No accountability for key holders
- Unauthorised access possible

**✅ Prevention:**
- Key duplication prohibited (controlled blanks)
- Key sign-out register maintained
- Regular key inventory audits

## Missing Visitor Escort Procedures

**❌ MISTAKE:** Visitors left unescorted in media storage areas

**Why This Fails:**
- Unauthorised access opportunity
- Theft or tampering risk
- No accountability for visitor actions

**✅ Prevention:**
- Mandatory escort in secure areas
- Visitor badges clearly visible
- Sign-in/sign-out logging

## Inadequate After-Hours Security

**❌ MISTAKE:** Storage areas accessible after business hours without additional controls

**Why This Fails:**
- Reduced surveillance during off-hours
- Delayed incident detection
- Opportunistic theft risk

**✅ Prevention:**
- After-hours access logging and alerting
- Additional approval required
- CCTV review of off-hours access

## No Emergency Evacuation Procedures for Media

**❌ MISTAKE:** No plan for protecting media during emergency evacuations

**Why This Fails:**
- Media left unsecured during evacuation
- Recovery planning impaired
- Business continuity compromised

**✅ Prevention:**
- Media protection in emergency procedures
- Designated personnel for media security
- Post-incident media verification

## Cross-Contamination of Classifications

**❌ MISTAKE:** CONFIDENTIAL and PUBLIC media stored in same location

**Why This Fails:**
- Handling confusion
- Misapplication of controls
- Audit finding for control weakness

**✅ Prevention:**
- Physically separate storage by classification
- Clear labelling of storage areas
- Regular storage audits

## Unverified Courier Credentials

**❌ MISTAKE:** Releasing media to couriers without verifying identity

**Why This Fails:**
- Social engineering attack vector
- Media diverted to unauthorised parties
- Chain of custody broken

**✅ Prevention:**
- Courier identification verification
- Known courier personnel where possible
- Photo ID and company verification

## Missing Insurance Documentation

**❌ MISTAKE:** Media transported without adequate insurance coverage

**Why This Fails:**
- Financial loss if media lost/damaged
- Data recovery costs not covered
- Business impact unmitigated

**✅ Prevention:**
- Insurance requirements in courier contracts
- Coverage verification before shipment
- Claims process documented

## No Media Handling Training

**❌ MISTAKE:** Staff handling media without formal training

**Why This Fails:**
- Procedures unknown or ignored
- Inconsistent handling practices
- Increased incident risk

**✅ Prevention:**
- Mandatory handling training for relevant staff
- Training records maintained
- Refresher training scheduled

## Uncontrolled Media Pooling

**❌ MISTAKE:** Shared media pools without individual accountability

**Why This Fails:**
- Cannot track who used specific media
- No accountability for data on media
- Chain of custody impossible

**✅ Prevention:**
- Individual media assignment
- Check-out/check-in logging
- Regular pool inventory

## Delayed Incident Reporting

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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
