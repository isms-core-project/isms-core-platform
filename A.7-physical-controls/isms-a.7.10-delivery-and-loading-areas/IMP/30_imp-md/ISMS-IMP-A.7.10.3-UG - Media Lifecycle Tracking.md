**ISMS-IMP-A.7.10.3-UG - Media Lifecycle Tracking Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.10: Storage Media

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.10.3-UG |
| **Version** | 1.0 |
| **Assessment Area** | Media Lifecycle Management, Disposal & Re-use |
| **Related Policy** | ISMS-POL-A.7.10, Section 2.5-2.6 (Disposal & Paper Documents) |
| **Purpose** | Assess organisational compliance with storage media lifecycle management from acquisition through disposal, including secure destruction and re-use procedures |
| **Target Audience** | IT Operations, Asset Management, Procurement, Facilities, Compliance Officers, Auditors |
| **Assessment Type** | Lifecycle Process & Operational Compliance |
| **Review Cycle** | Annual (minimum) or After Regulatory Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Media Lifecycle Tracking assessment workbook | ISMS Implementation Team |

---

**Audience:** IT Operations, Asset Management, Procurement, Facilities Management, Compliance Officers

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organisation]'s implementation of **storage media lifecycle management** to ensure compliance with ISO/IEC 27001:2022 Control A.7.10 requirements for acquisition, use, and disposal of media.

**Scope:** Complete media lifecycle across 5 critical areas:

1. **Acquisition & Procurement** - Approved suppliers, procurement controls, registration
2. **Internal Re-use Procedures** - Secure erasure, verification, re-assignment
3. **Disposal Methods** - Destruction methods by classification level
4. **Third-Party Disposal** - Approved vendors, certificates, chain of custody
5. **Paper Document Lifecycle** - Physical media handling through shredding

**Assessment Output:** Excel workbook with ~120-180 data points documenting current lifecycle practices, disposal methods, and compliance with secure destruction requirements.

## Why This Matters

**ISO 27001:2022 Control A.7.10 Requirement:**
> *"Storage media should be managed through their life cycle of acquisition, use, transportation and disposal in accordance with the organisation's classification scheme and handling requirements."*

**Disposal Requirements (ISO 27002:2022):**

- CONFIDENTIAL data: Physical destruction or certified erasure
- Certificates of destruction required
- Internal re-use requires verified secure erasure
- Media should never be sold/donated with recoverable data

**Business Impact:**

- **Data Breach Prevention:** Improper disposal is leading cause of data exposure
- **Regulatory Compliance:** GDPR, PCI DSS mandate secure destruction
- **Legal Protection:** Certificates provide evidence of proper handling
- **Environmental Responsibility:** Proper e-waste disposal
- **Audit Evidence:** Documented lifecycle supports compliance verification

## Who Should Complete This Assessment

**Primary Responsibility:** IT Operations Manager / Asset Management Lead

**Required Knowledge:**

- [Organisation]'s media disposal procedures
- Approved disposal vendors and contracts
- Secure erasure methods and tools
- Certificate of destruction processes
- E-waste and environmental regulations

**Support Roles:**

- **Procurement:** For approved supplier management
- **Facilities:** For physical destruction capabilities
- **Legal/Compliance:** For certificate retention requirements
- **Information Security:** For erasure verification standards
- **Environmental/HSE:** For e-waste compliance

## Time Estimate

**Total Assessment Time:** 6-10 hours

**Breakdown:**

- **Acquisition Assessment (1-2 hours):** Review procurement and registration
- **Re-use Procedures (1-2 hours):** Assess internal media recycling
- **Disposal Methods (2-3 hours):** Evaluate destruction procedures
- **Third-Party Management (1-2 hours):** Review vendor compliance
- **Evidence Collection (1 hour):** Gather certificates and documentation

## Connection to Policy

This assessment implements **ISMS-POL-A.7.10, Section 2.5 (Disposal of Storage Media)** which defines mandatory requirements for:

- **CONFIDENTIAL Disposal:** Physical destruction with certificate
- **INTERNAL Disposal:** Secure overwriting (3+ passes) or destruction
- **Re-use Verification:** Erasure verification before reassignment
- **Third-Party Disposal:** Approved vendors with certificates
- **Paper Shredding:** Cross-cut shredding for CONFIDENTIAL documents

**Policy Authority:** Chief Information Security Officer (CISO)
**Compliance Status:** Mandatory for all storage media containing organisation information

---

# Prerequisites

## Access Required

Before starting this assessment, ensure you have access to:

**Documentation:**

- [ ] Media disposal procedures and work instructions
- [ ] Approved disposal vendor contracts
- [ ] Certificate of destruction templates and records
- [ ] Secure erasure tool documentation
- [ ] E-waste and environmental compliance records
- [ ] Procurement and approved supplier lists

**Systems:**

- [ ] Asset management system (disposal workflow)
- [ ] Procurement system (approved suppliers)
- [ ] Secure erasure tool reports
- [ ] Vendor certificate repository
- [ ] Environmental compliance tracking

**Physical Access:**

- [ ] IT staging area for disposal preparation
- [ ] On-site destruction equipment (degaussers, shredders)
- [ ] Secure holding area for pending disposal
- [ ] Paper shredding equipment and collection points

## Pre-Assessment Checklist

Complete these tasks before beginning the assessment:

- [ ] **Collect recent certificates** of destruction from vendors
- [ ] **Review disposal workflow** in asset management system
- [ ] **Verify secure erasure tools** are current and validated
- [ ] **Check vendor contracts** for disposal service providers
- [ ] **Obtain e-waste compliance** certificates/records
- [ ] **Review recent disposal** events and volumes
- [ ] **Inspect on-site destruction** equipment condition

---

# Assessment Workflow

## Workflow Overview

```
Step 1: Acquisition & Procurement (Sheet 2)
   |
Step 2: Internal Re-use Procedures (Sheet 3)
   |
Step 3: Disposal Methods (Sheet 4)
   |
Step 4: Third-Party Disposal (Sheet 5)
   |
Step 5: Paper Document Lifecycle (Sheet 6)
   |
Step 6: Evidence Collection (Sheet 8)
   |
Step 7: Review Summary Dashboard (Sheet 7)
   |
Step 8: Quality Check & Approval (Sheet 9)
```

## Step-by-Step Instructions

### Step 1: Acquisition & Procurement (Sheet 2)

**Objective:** Assess media procurement and registration controls

**Instructions:**
1. List each media procurement category in Column A
2. Document Approved Suppliers in Column R
3. Specify Registration Requirement in Column S
4. Record Quality Standards in Column T
5. Assess Status in Column F

**Acquisition Requirements:**

- **Approved Suppliers:** Media procured only from vetted vendors
- **Hardware-Encrypted Media:** Mandatory for CONFIDENTIAL removable devices
- **Registration:** New media registered before deployment
- **Quality Standards:** Media meets reliability requirements
- **Bulk Purchases:** Proper inventory and tracking

**Detailed Procurement Controls:**

**Vendor Assessment:**
- Security assessment of media suppliers
- Supply chain integrity verification
- Quality certifications (ISO 9001)
- Business continuity arrangements
- Price vs. quality evaluation

**Media Specifications:**
- Technical specifications documented
- Compatibility verified with systems
- Warranty and support terms
- End-of-life considerations
- Encryption capabilities verified

**Purchase Authorization:**
- Approval thresholds defined
- Budget allocation verified
- Standard vs. non-standard requests
- Emergency procurement procedures
- Audit trail of approvals

**Quality Check:**

- Are all media purchases from approved suppliers?
- Is hardware-encrypted media used for CONFIDENTIAL?
- Are new media items registered before distribution?
- Are procurement records retained?
- Is incoming quality inspection performed?
- Are specifications documented and verified?

### Step 2: Internal Re-use Procedures (Sheet 3)

**Objective:** Assess procedures for media re-assignment within the organisation

**Instructions:**
1. List each re-use scenario in Column A
2. Document Erasure Method in Column R
3. Specify Verification Requirement in Column S
4. Record Documentation Required in Column T
5. Assess Status in Column F

**Re-use Requirements:**

Before media is re-used internally:
- All sensitive data securely erased
- Erasure verified and documented
- Media inspected for physical integrity
- Asset records updated with new assignment
- Previous classification cleared

**Secure Erasure Methods:**

| Method | Suitable For | Verification |
|--------|-------------|--------------|
| Cryptographic Erasure | SSDs with encryption | Key destruction confirmed |
| NIST 800-88 Clear | Standard re-use | Read verification |
| NIST 800-88 Purge | High-security re-use | Forensic verification |
| Physical Destruction | No re-use intended | Visual confirmation |

**Detailed Erasure Procedures:**

**Hard Disk Drives (HDD):**
- Overwrite method selection (1-pass vs. 3-pass)
- Block-level verification
- Bad sector handling
- Firmware area consideration
- Time requirements and scheduling

**Solid State Drives (SSD):**
- TRIM command limitations
- Encryption-based erasure preferred
- Vendor-specific secure erase
- Over-provisioning area handling
- Wear levelling considerations

**Removable Media:**
- USB drive erasure tools
- Memory card specific methods
- Optical media handling
- Tape degaussing requirements
- Media-specific verification

**Quality Check:**

- Is erasure verified before re-assignment?
- Are appropriate methods used for media type?
- Is documentation maintained for audit?
- Is physical integrity verified?
- Are erasure tools validated and current?
- Is the erasure process logged and timestamped?

### Step 3: Disposal Methods (Sheet 4)

**Objective:** Assess disposal methods by classification level

**Instructions:**
1. List each disposal scenario by classification in Column A
2. Document Required Destruction Method in Column R
3. Specify Witness Requirement in Column S
4. Record Certificate Required in Column T
5. Assess Status in Column F

**Disposal Methods by Classification:**

**CONFIDENTIAL Data:**
- Physical destruction (shredding, degaussing, incineration)
- Approved third-party destruction service
- Certificate of destruction mandatory
- Witnessed destruction for highly sensitive data

**INTERNAL Data:**
- Secure overwriting (minimum 3 passes) OR physical destruction
- Verification of successful erasure
- Documentation of disposal method

**PUBLIC Data:**
- Standard deletion acceptable
- Format and dispose through appropriate channels

**Destruction Methods:**

| Media Type | CONFIDENTIAL | INTERNAL | PUBLIC |
|-----------|-------------|----------|--------|
| HDD | Shred/Degauss | 3-pass overwrite | Delete/Format |
| SSD | Shred/Crypto-erase | Crypto-erase | Delete/Format |
| USB | Shred | Crypto-erase | Delete |
| Tape | Degauss + Shred | Degauss | Overwrite |
| Optical | Shred | Shred | Scratch/Break |
| Paper | Cross-cut shred | Strip shred | Recycle |

**Detailed Destruction Requirements:**

**On-Site Destruction:**
- Equipment maintenance schedule
- Operator training verification
- Safety procedures documented
- Particle size compliance (DIN 66399)
- Waste handling procedures

**Off-Site Destruction:**
- Secure transport arrangements
- Chain of custody documentation
- Destruction witnessing options
- Certificate requirements
- Audit rights in contract

**Special Considerations:**
- Failed drive handling (warranty vs. security)
- Encrypted drive destruction
- Defective media handling
- Prototype/development media
- Historical/archive media

**Quality Check:**

- Are disposal methods appropriate for classification?
- Are certificates obtained for CONFIDENTIAL media?
- Is witness required for highly sensitive destruction?
- Are disposal records maintained?
- Is on-site equipment properly maintained?
- Are off-site processes adequately controlled?

### Step 4: Third-Party Disposal (Sheet 5)

**Objective:** Assess third-party disposal vendor management

**Instructions:**
1. List each disposal vendor in Column A
2. Document Contract Status in Column R
3. Specify Certification Requirements in Column S
4. Record SLA/Performance Metrics in Column T
5. Assess Status in Column F

**Third-Party Requirements:**

- **Approved Vendors:** Vetted and contracted disposal providers
- **Certifications:** ISO 27001, R2, e-Stewards, NAID certification
- **Chain of Custody:** Documented from handoff to destruction
- **Certificates:** Individual or batch certificates provided
- **Audit Rights:** Contract allows customer audit of facilities
- **Insurance:** Adequate liability coverage

**Vendor Evaluation Criteria:**

- Data destruction certifications held
- Environmental compliance (e-waste regulations)
- Security clearances for personnel
- Physical security of facilities
- Certificate turnaround time
- Geographic coverage

**Detailed Vendor Management:**

**Initial Assessment:**
- Security questionnaire completion
- Site visit and facility inspection
- Reference verification
- Financial stability check
- Insurance verification

**Ongoing Monitoring:**
- Certification renewal tracking
- Performance metrics review
- Incident reporting requirements
- Annual audit or assessment
- Contract compliance verification

**Contract Requirements:**
- Data protection clauses
- Liability and indemnification
- Certificate requirements specified
- Audit rights included
- Termination procedures
- Data breach notification

**Quality Check:**

- Are all disposal vendors approved and contracted?
- Do vendors hold appropriate certifications?
- Are certificates received for all destructions?
- Is chain of custody documented?
- Are vendor audits performed regularly?
- Is insurance coverage verified?

### Step 5: Paper Document Lifecycle (Sheet 6)

**Objective:** Assess physical document handling and destruction

**Instructions:**
1. List each paper document category in Column A
2. Document Shredding Requirement in Column R
3. Specify Collection Process in Column S
4. Record Destruction Frequency in Column T
5. Assess Status in Column F

**Paper Document Requirements:**

**CONFIDENTIAL Documents:**
- Cross-cut shredding (minimum DIN 66399 P-4)
- On-site shredding or secure contractor
- Shredding bin access controls
- Mass destruction witnessed or certified

**INTERNAL Documents:**
- Strip shredding or cross-cut acceptable
- Secure collection bins
- Regular destruction schedule

**Clean Desk Policy:**
- Documents secured when unattended
- Locked storage for sensitive documents
- End-of-day desk clearance

**Detailed Paper Handling:**

**Collection Bins:**
- Bin specifications (locked, slot size)
- Placement locations documented
- Labelling requirements
- Capacity management
- Overflow procedures

**Shredding Standards (DIN 66399):**
- P-1 to P-7 particle sizes
- Classification mapping to shred level
- Verification of shred quality
- Equipment certification
- Residue handling

**Contractor Management:**
- Secure collection procedures
- Transport vehicle security
- Personnel vetting
- Certificate provision
- Frequency and scheduling

**Quality Check:**

- Is appropriate shredding method used for classification?
- Are secure collection bins deployed?
- Is shredding performed regularly?
- Is clean desk policy enforced?
- Are contractor procedures adequate?
- Is shredder maintenance current?

---

# Common Pitfalls

## No Certificates of Destruction

**❌ MISTAKE:** Disposing of CONFIDENTIAL media without obtaining certificates

**Why This Fails:**
- No proof of proper destruction
- Cannot demonstrate compliance during audit
- Potential liability if data recovered later

**✅ Prevention:**
- Require certificates for all CONFIDENTIAL media
- Track certificate receipt in asset management
- Retain certificates per retention schedule

## SSD Overwriting Ineffective

**❌ MISTAKE:** Using traditional overwrite methods on SSDs

**Why This Fails:**
- Wear levelling prevents complete overwriting
- Hidden areas may retain data
- Forensic recovery possible

**✅ Prevention:**
- Use cryptographic erasure for SSDs
- Or physical destruction (shredding)
- Verify with manufacturer guidance

## Vendor Certifications Expired

**❌ MISTAKE:** Using disposal vendors with lapsed certifications

**Why This Fails:**
- Security practices may have degraded
- Insurance coverage may be void
- Audit finding for unvalidated vendors

**✅ Prevention:**
- Track vendor certification expiry dates
- Annual vendor review process
- Contract renewal tied to certification

## No Re-use Verification

**❌ MISTAKE:** Re-assigning media without erasure verification

**Why This Fails:**
- Previous owner's data accessible
- Classification mismatch risk
- Data breach if media later lost

**✅ Prevention:**
- Mandatory verification step in re-use workflow
- Documentation of erasure and verification
- Spot audits of re-used media

## Incomplete Chain of Custody

**❌ MISTAKE:** Media disposal without documented handoffs

**Why This Fails:**
- Cannot prove media reached destruction
- Theft or diversion possible
- Legal evidence issues

**✅ Prevention:**
- Serial number tracking to destruction
- Signed handoff at each transfer
- Reconciliation of media sent vs. certificates received

## Paper Shredding Gaps

**❌ MISTAKE:** CONFIDENTIAL paper in standard recycling

**Why This Fails:**
- Documents recovered from recycling stream
- Data breach from physical documents
- Policy violation

**✅ Prevention:**
- Deploy secure shredding bins at all locations
- Regular collection schedule
- Awareness training on document handling

## Delayed Disposal

**❌ MISTAKE:** Media awaiting disposal for extended periods

**Why This Fails:**
- Theft risk during staging
- Asset tracking gaps
- Storage space consumed

**✅ Prevention:**
- Maximum staging period (e.g., 30 days)
- Secure holding area with access controls
- Regular disposal batches scheduled

## No Environmental Compliance

**❌ MISTAKE:** E-waste disposed without proper handling

**Why This Fails:**
- Environmental regulation violation
- Reputational damage
- Fines and penalties

**✅ Prevention:**
- Use certified e-waste recyclers
- Obtain environmental compliance certificates
- Track disposal through proper channels

## Erasure Tool Not Validated

**❌ MISTAKE:** Using erasure software without verification of effectiveness

**Why This Fails:**
- Erasure may be incomplete
- False sense of security
- Audit finding for inadequate controls

**✅ Prevention:**
- Use NIST-approved erasure tools
- Validate tool effectiveness periodically
- Document tool version and settings

## Failed Drive Warranty Conflicts

**❌ MISTAKE:** Returning failed drives to vendor without data removal

**Why This Fails:**
- Data may be recoverable from failed drives
- Data leaves organisational control
- Potential data breach

**✅ Prevention:**
- Negotiate "keep your drive" warranty terms
- Destroy failed drives internally
- Document warranty vs. security decisions

## No Procurement Tracking

**❌ MISTAKE:** Media purchased outside approved channels

**Why This Fails:**
- Unknown media quality and security
- No asset registration
- Lifecycle tracking impossible

**✅ Prevention:**
- Centralised media procurement
- Approved supplier list enforced
- Registration requirement before deployment

## Incomplete Asset Disposal Records

**❌ MISTAKE:** Disposing media without updating asset management system

**Why This Fails:**
- Ghost assets in inventory
- Cannot reconcile physical with records
- Audit finding for poor asset management

**✅ Prevention:**
- Disposal workflow includes asset update
- Regular reconciliation audits
- Mandatory closure step in process

## Cross-Cut Shredder Misconfigured

**❌ MISTAKE:** Shredder particle size not appropriate for classification

**Why This Fails:**
- Larger particles allow document reconstruction
- Non-compliance with DIN 66399
- Security control ineffective

**✅ Prevention:**
- Verify shredder specification vs. requirement
- Regular maintenance and blade checks
- Periodic particle size verification

## No Degausser for Magnetic Media

**❌ MISTAKE:** Disposing magnetic tapes without degaussing

**Why This Fails:**
- Data remains on tape surface
- Physical destruction may be incomplete
- Forensic recovery possible

**✅ Prevention:**
- Degauss before physical destruction
- Verify degausser field strength
- Document degaussing in disposal record

## Missing Retention Period Consideration

**❌ MISTAKE:** Disposing media before retention period expires

**Why This Fails:**
- Regulatory or legal non-compliance
- Loss of required records
- Potential litigation exposure

**✅ Prevention:**
- Check retention requirements before disposal
- Legal hold verification process
- Retention schedule integration

## No Disposal Approval Workflow

**❌ MISTAKE:** IT staff disposing media without management approval

**Why This Fails:**
- No oversight of disposal decisions
- Premature disposal possible
- Accountability gaps

**✅ Prevention:**
- Formal approval workflow for disposal
- Approval levels based on classification/value
- Audit trail of approvals

## Uncontrolled Media Donation

**❌ MISTAKE:** Donating old equipment without proper data erasure

**Why This Fails:**
- Data recovered by donation recipients
- Reputational damage
- Potential breach notification required

**✅ Prevention:**
- Donation requires same erasure as disposal
- Verification before release
- Consider physical destruction instead

## Paper Shredding Overflow

**❌ MISTAKE:** Overfull shredding bins with documents visible

**Why This Fails:**
- Unauthorised access to documents
- Clean desk policy compromised
- Security incident possible

**✅ Prevention:**
- Adequate bin capacity
- Regular collection schedule
- Overflow procedures documented

---

# Quality Checklist

Before submitting assessment for approval, verify:

## Completeness

- [ ] All lifecycle stages documented
- [ ] All sheets completed (no "TBD" or blank sections)
- [ ] Evidence Register populated with certificates
- [ ] Summary Dashboard reviewed
- [ ] All media types addressed
- [ ] All destruction methods documented
- [ ] All vendors listed and assessed

## Accuracy

- [ ] Disposal methods aligned with classification
- [ ] Vendor certifications current and verified
- [ ] Erasure methods appropriate for media types
- [ ] Certificate records match disposal events
- [ ] Asset system reflects disposals
- [ ] Destruction dates verified
- [ ] Serial numbers reconciled

## Compliance

- [ ] Certificates obtained for CONFIDENTIAL disposal
- [ ] Third-party vendors properly vetted
- [ ] Re-use procedures include verification
- [ ] E-waste compliance documented
- [ ] Paper shredding standards met
- [ ] Retention requirements verified
- [ ] Environmental regulations addressed

## Remediation Planning

- [ ] Gaps identified with remediation timeline
- [ ] Vendor renewals/replacements planned
- [ ] Procedure updates scheduled
- [ ] Training needs identified
- [ ] Equipment upgrades planned
- [ ] Budget requirements flagged

## Evidence Quality

- [ ] All certificates properly filed
- [ ] Vendor contracts accessible
- [ ] Erasure reports retained
- [ ] Disposal logs complete
- [ ] Photographic evidence where appropriate
- [ ] Chain of custody forms retained

## Process Verification

- [ ] Disposal workflow tested
- [ ] Approval workflow functional
- [ ] Asset system integration verified
- [ ] Certificate tracking operational
- [ ] Vendor SLAs monitored
- [ ] Equipment maintenance current

---

# Review & Approval

## Approval Workflow (Sheet 9)

**Level 1: Technical/Operational Approval**

- **Approver:** IT Operations Manager / Asset Management Lead
- **Validates:** Procedure accuracy, disposal method appropriateness
- **Approval Criteria:** Assessment reflects current lifecycle practices

**Level 2: Management Approval**

- **Approver:** CISO / IT Director
- **Validates:** Compliance posture, vendor management, remediation plans
- **Approval Criteria:** Gaps have realistic remediation plans

**Level 3: Executive Approval**

- **Approver:** COO / CRO / Executive Management
- **Validates:** Overall lifecycle management posture, risk acceptance
- **Approval Criteria:** Executive acknowledges lifecycle compliance status

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
