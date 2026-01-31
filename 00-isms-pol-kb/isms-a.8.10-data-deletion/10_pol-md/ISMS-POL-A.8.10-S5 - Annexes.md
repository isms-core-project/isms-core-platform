# ISMS-POL-A.8.10-S5
## Information Deletion - Annexes

**Document ID**: ISMS-POL-A.8.10-S5
**Title**: Information Deletion - Annexes  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Data Protection Officer / Information Security Manager | Initial annexes and reference materials |

**Review Cycle**: Semi-annually (more frequent than policy sections due to tool/form updates)  
**Next Review Date**: [Approval Date + 6 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Operational Review: Data Protection Officer (DPO)
- Technical Review: IT Operations Manager

**Distribution**: All staff (practical reference), IT operations, data owners, DPO  
**Related Documents**: ISMS-POL-A.8.10-S2.x (Requirements), ISMS-IMP-A.8.10.x (Implementation Workbooks)

---

## 5.1 Purpose and Scope

This section provides **practical tools and reference materials** to support implementation of the Information Deletion Policy. Annexes are designed for day-to-day use by practitioners and are updated more frequently than core policy sections to reflect tool changes, process improvements, and lessons learned.

**In Scope**: Deletion methods matrix, forms/templates, checklists, quick reference guides, tool lists  
**Primary Users**: IT Operations, Data Owners, DPO, Records Managers  
**Key Principle**: "If the policy is the map, the annexes are the GPS with turn-by-turn directions."

---

## 5.2 Annex Index

This section contains the following annexes:

| Annex | Title | Purpose | Primary Users |
|-------|-------|---------|---------------|
| **S5.A** | Approved Deletion Methods Matrix | Media-specific deletion method selection | IT Operations, InfoSec |
| **S5.B** | Data Subject Erasure Request Form | GDPR Article 17 request handling | DPO, Customer Service |
| **S5.C** | Deletion Verification Checklist | Quality assurance for deletion activities | IT Operations, Audit |
| **S5.D** | Quick Reference Guide | One-page deletion decision tree | All staff |
| **S5.E** | Policy Exception Request Form | Exception management workflow | Data Owners, DPO |
| **S5.F** | Deletion Log Template | Standardized deletion logging | IT Operations |
| **S5.G** | Certificate of Destruction Template | Third-party vendor evidence | Procurement, Asset Mgmt |
| **S5.H** | Approved Deletion Tools List | Validated tools by media type | IT Operations |
| **S5.I** | Cloud Provider Deletion Procedures | Quick reference for major cloud providers | IT Operations, Cloud Ops |

**Note**: Annexes are **living documents** — updated as tools evolve, forms improve, and lessons are learned.

---

## Annex S5.A: Approved Deletion Methods Matrix

### Purpose
Provides media-specific deletion method selection guidance aligned with NIST SP 800-88 (informational reference) and data sensitivity classifications.

### Deletion Methods Matrix

| Media Type | Data Sensitivity | Destination | Recommended Method | Verification | Approved Tools/Vendors |
|------------|------------------|-------------|-------------------|--------------|------------------------|
| **HDD (Magnetic)** | Low-Medium | Internal reuse | Single-pass overwrite | Tool log | DBAN, shred, Blancco |
| **HDD (Magnetic)** | High | Internal reuse | ATA Secure Erase | SMART data | hdparm, Parted Magic |
| **HDD (Magnetic)** | Any | External/disposal | ATA Secure Erase or Degauss | Certificate | Degausser (NSA EPL), Blancco |
| **HDD (Magnetic)** | Any | End-of-life | Physical destruction (shred to ≤2mm) | Certificate + visual | [Certified Vendor List] |
| **SSD (Flash)** | Low | Internal reuse | ATA Secure Erase (verify vendor) | Tool log + spot check | nvme-cli, vendor tools |
| **SSD (Flash)** | Medium-High | Internal reuse | Cryptographic erase (SED) | Key deletion log | Vendor SED tools |
| **SSD (Flash)** | Any | External/disposal | Crypto erase + physical destruction | Certificate | [Certified Vendor List] |
| **SSD (Flash)** | Any | End-of-life | Physical destruction (shred to ≤2mm) | Certificate + visual | [Certified Vendor List] |
| **NVMe SSD** | Any | Any | NVMe Sanitize (Crypto/Block Erase) | Tool log | nvme-cli, vendor tools |
| **Tape (Magnetic)** | Low-Medium | Internal reuse | Overwrite (full tape) | Tape drive log | Tape system native |
| **Tape (Magnetic)** | High | Disposal | Degauss (NSA EPL degausser) | Certificate | [Certified Vendor List] |
| **Tape (Magnetic)** | Any | End-of-life | Physical destruction (shred/incinerate) | Certificate | [Certified Vendor List] |
| **Cloud Storage (S3/Blob/GCS)** | Any | Logical deletion | API deletion + crypto erase | API response + key deletion | AWS CLI, Azure CLI, gcloud |
| **Cloud Compute (VM/Container)** | Any | Decommission | Terminate instance + delete volumes | API response | Cloud console/API |
| **Cloud Database** | Any | Decommission | Delete instance + snapshots | API response | Cloud console/API |
| **Mobile Device (Phone/Tablet)** | Any | Reuse/disposal | Factory reset (encrypted device) + MDM wipe | MDM console | Intune, Jamf, MobileIron |
| **Laptop/Desktop** | Low-Medium | Internal reuse | OS reinstall + disk overwrite | Installation log | OS media + DBAN/shred |
| **Laptop/Desktop** | High | External/disposal | Disk removal + separate destruction | Certificate | Separate HDD/SSD method |
| **Paper (Confidential)** | Medium | Disposal | Cross-cut shred (DIN 66399 P-4) | Certificate | [Certified Vendor List] |
| **Paper (Highly Sensitive)** | High | Disposal | Cross-cut shred (DIN 66399 P-5) | Certificate | [Certified Vendor List] |
| **Optical Media (CD/DVD)** | Any | Disposal | Physical destruction (shred/incinerate) | Certificate | [Certified Vendor List] |
| **USB/Flash Drive** | Any | Disposal | Physical destruction (same as SSD) | Certificate | [Certified Vendor List] |

### Decision Flowchart
```
Is media staying in organization?
├─ YES → Is data sensitivity HIGH?
│         ├─ YES → Use Purge method (secure erase, crypto erase)
│         └─ NO → Use Clear method (overwrite, factory reset)
└─ NO → Is this end-of-life disposal?
          ├─ YES → Use Destroy method (physical destruction)
          └─ NO (external transfer) → Use Purge method minimum
```

### Notes
- **[Certified Vendor List]**: Maintain separate list of approved destruction vendors with certifications (NAID AAA, ISO 27001, R2/e-Stewards)
- **Crypto Erase**: Only effective if drive was encrypted from deployment; verify encryption status before relying on key deletion
- **Degaussing**: Renders magnetic media permanently unusable; cannot be reused after degaussing
- **Cloud Deletion**: Always combine API deletion with cryptographic erasure (customer-managed keys) for high-sensitivity data

---

## Annex S5.B: Data Subject Erasure Request Form

### Purpose
Standardized form for handling GDPR Article 17 "Right to Erasure" requests from data subjects.

### Form Template
```
DATA SUBJECT ERASURE REQUEST
ISMS-POL-A.8.10-S5.B

Request Information
─────────────────────────────────────────────────────────────
Request ID: [Auto-generated: ESR-YYYY-NNNN]
Receipt Date: [DD.MM.YYYY]
Receipt Method: ☐ Email  ☐ Portal  ☐ Phone  ☐ Mail  ☐ In-person
GDPR Deadline: [Receipt Date + 30 days]

Data Subject Information
─────────────────────────────────────────────────────────────
Full Name: _________________________________________________
Email Address: _____________________________________________
Phone Number: ______________________________________________
Customer/Employee ID: ______________________________________
Relationship to Organization: ☐ Customer  ☐ Employee  ☐ Contractor  
                              ☐ Marketing Contact  ☐ Other: _______

Identity Verification
─────────────────────────────────────────────────────────────
Verification Method: ☐ Account login  ☐ ID document  ☐ Knowledge-based auth
                     ☐ Email confirmation  ☐ Other: ________________
Verified By: _______________________________________________
Verification Date: _________________________________________
Identity Confirmed: ☐ YES  ☐ NO (do not proceed if NO)

Request Scope
─────────────────────────────────────────────────────────────
Data Categories Requested for Deletion (check all that apply):
☐ Account information (username, profile)
☐ Contact information (email, phone, address)
☐ Transaction history
☐ Communication records (emails, chat logs)
☐ Marketing preferences and history
☐ Technical data (IP addresses, cookies, device IDs)
☐ Financial information (payment methods, billing history)
☐ All personal data (complete erasure)
☐ Other (specify): _________________________________________

Special Circumstances:
☐ Active contract/service (deletion may impact service)
☐ Outstanding financial obligations (may affect deletion eligibility)
☐ Legal hold or litigation (deletion prohibited)
☐ Regulatory retention requirement (deletion may be denied)

Legal Basis Assessment
─────────────────────────────────────────────────────────────
Assessed By (DPO/Legal): ___________________________________
Assessment Date: ___________________________________________

Can request be fulfilled? ☐ YES (proceed)  ☐ NO (denial justified below)

If NO, grounds for denial (GDPR Article 17(3)):
☐ Legal obligation requires retention
☐ Exercise or defense of legal claims (litigation)
☐ Public interest/official authority task
☐ Archiving in public interest (with safeguards)
☐ Other: ___________________________________________________

Justification for Denial:
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________

Systems Searched
─────────────────────────────────────────────────────────────
☐ CRM System          Found: ☐ Yes ☐ No  Deleted: ☐ Yes ☐ No ☐ N/A
☐ Email System        Found: ☐ Yes ☐ No  Deleted: ☐ Yes ☐ No ☐ N/A
☐ Database (prod)     Found: ☐ Yes ☐ No  Deleted: ☐ Yes ☐ No ☐ N/A
☐ Database (archive)  Found: ☐ Yes ☐ No  Deleted: ☐ Yes ☐ No ☐ N/A
☐ Backup Systems      Found: ☐ Yes ☐ No  Deleted: ☐ See backup schedule
☐ Marketing Platform  Found: ☐ Yes ☐ No  Deleted: ☐ Yes ☐ No ☐ N/A
☐ File Storage        Found: ☐ Yes ☐ No  Deleted: ☐ Yes ☐ No ☐ N/A
☐ Analytics/Logs      Found: ☐ Yes ☐ No  Deleted: ☐ Yes ☐ No ☐ N/A
☐ Third-Party Systems (list): _____________________________
  _________________________________________________________

Deletion Actions Taken
─────────────────────────────────────────────────────────────
Action                          System         Date       Performed By
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________

Backup Deletion Timeline:
☐ Deleted from production immediately
☐ Will be deleted from backups on next rotation (date: ________)
☐ Backup retention: ___ days (deletion complete by: ________)

Third-Party Processor Notifications
─────────────────────────────────────────────────────────────
Third Party                 Notified (Date)    Confirmation Received
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________

Response to Data Subject
─────────────────────────────────────────────────────────────
Response Date: _____________________________________________
Response Method: ☐ Email  ☐ Portal  ☐ Mail
Response Type: ☐ Deletion confirmed  ☐ Deletion denied (with justification)
               ☐ Partial deletion (with explanation)

Within GDPR Timeline? ☐ YES (<30 days)  ☐ NO (extension notified: _____)

Attachments
─────────────────────────────────────────────────────────────
☐ Deletion logs (attached)
☐ Third-party deletion confirmations (attached)
☐ Denial justification letter (if applicable)
☐ Data subject communication (response email/letter)

Approval and Sign-Off
─────────────────────────────────────────────────────────────
DPO Review and Approval:
Signature: ______________________ Date: ___________________

Quality Assurance Review (if applicable):
Signature: ______________________ Date: ___________________

Case Closure:
☐ Request fulfilled and closed
☐ Request denied and closed (with documented justification)
Closure Date: ______________________________________________

Archive Location: __________________________________________
Retention Period: 3 years from closure date
```

### Usage Instructions
1. Complete form for every data subject erasure request
2. Attach deletion logs, certificates, and communications
3. Retain completed form for 3 years (evidence of GDPR compliance)
4. Store in secure, access-controlled repository

---

## Annex S5.C: Deletion Verification Checklist

### Purpose
Quality assurance checklist to ensure deletion activities are complete, verified, and documented.

### Checklist Template
```
DELETION VERIFICATION CHECKLIST
ISMS-POL-A.8.10-S5.C

Project/Request Information
─────────────────────────────────────────────────────────────
Deletion ID: _______________________________________________
Deletion Type: ☐ Scheduled  ☐ Data Subject Request  
               ☐ Legal Hold Release  ☐ Service Termination
               ☐ Media Disposal  ☐ Other: __________________
Date Initiated: ____________________________________________
Completed By: ______________________________________________
Verification Date: _________________________________________

Pre-Deletion Verification
─────────────────────────────────────────────────────────────
☐ Retention period expired (or other valid trigger)
☐ NO active legal hold on this data
☐ Deletion approved by appropriate authority
☐ Backup plan exists (if accidental deletion possible)
☐ Data export completed (if required for migration/transition)
☐ Stakeholders notified (if business-impacting deletion)

Deletion Execution Verification
─────────────────────────────────────────────────────────────
☐ Approved deletion method used (per ISMS-POL-A.8.10-S2.2)
☐ Deletion tool logs generated
☐ Deletion completed without errors
☐ If errors occurred: documented and resolved
☐ All copies deleted (production, backup, DR, test/dev)
☐ All regions/locations addressed (multi-region cloud)

Evidence Collection
─────────────────────────────────────────────────────────────
☐ Deletion logs collected and stored
☐ Tool output reports saved
☐ API responses captured (cloud deletion)
☐ Certificates of Destruction obtained (physical media)
☐ Chain of custody documented (physical media)
☐ Screenshots/photos captured (if applicable)
☐ Witness signatures obtained (high-sensitivity media)

Technical Verification
─────────────────────────────────────────────────────────────
☐ Data no longer accessible via normal means
☐ Database queries return zero results (if applicable)
☐ File system shows files deleted (if applicable)
☐ Cloud console/API shows resources deleted
☐ Backup systems show deletion scheduled/completed
☐ Forensic spot check performed (if required per sampling schedule)
   - Recovery attempt made: ☐ YES  ☐ NO  ☐ N/A
   - Data recovered: ☐ NONE (pass)  ☐ FRAGMENTS  ☐ SIGNIFICANT (fail)

Third-Party Verification (if applicable)
─────────────────────────────────────────────────────────────
☐ Third-party deletion requested
☐ Third-party deletion confirmed (certificate/email)
☐ Subprocessor deletion confirmed (if applicable)
☐ Vendor SLA met (deletion within agreed timeline)

Documentation and Compliance
─────────────────────────────────────────────────────────────
☐ Deletion logged in central deletion log
☐ Evidence stored in evidence repository
☐ Data subject notified (if GDPR request)
☐ Exception register updated (if exception was active)
☐ Compliance metrics updated
☐ Audit trail complete (who, what, when, where, why, how)

Data Subject Request Specific (if applicable)
─────────────────────────────────────────────────────────────
☐ All requested systems searched
☐ All personal data identified and deleted
☐ Third-party processors notified
☐ Response sent within 30 days (GDPR)
☐ Backup deletion timeline communicated

Quality Assurance Sign-Off
─────────────────────────────────────────────────────────────
Verifier Name: _____________________________________________
Verifier Role: _____________________________________________
Verification Result: ☐ PASS (deletion complete and verified)
                     ☐ FAIL (issues identified - see notes)

Issues Identified (if FAIL):
_____________________________________________________________
_____________________________________________________________

Remediation Actions:
_____________________________________________________________
_____________________________________________________________

Final Approval:
DPO/CISO Signature: __________________ Date: ______________

Checklist Archive Location: ________________________________
```

### Usage Instructions
- Complete checklist for all high-sensitivity deletions
- Use sampling for routine deletions (per verification schedule)
- Attach to deletion logs in evidence repository
- Review failures to identify systemic issues

---

## Annex S5.D: Quick Reference Guide

### Purpose
One-page decision guide for common deletion scenarios.

### Quick Deletion Decision Tree
```
┌─────────────────────────────────────────────────────────────┐
│         INFORMATION DELETION QUICK REFERENCE                 │
│              ISMS-POL-A.8.10-S5.D                           │
└─────────────────────────────────────────────────────────────┘

STEP 1: DETERMINE IF DELETION IS REQUIRED
─────────────────────────────────────────────────────────────
✓ Retention period expired? → Proceed to deletion
✓ Data subject erasure request? → Contact DPO immediately
✓ Legal hold active? → DO NOT DELETE (contact Legal)
✓ Unsure? → Contact DPO or Records Manager

STEP 2: SELECT DELETION METHOD
─────────────────────────────────────────────────────────────
Media Type          Low Sensitivity      High Sensitivity
──────────────────────────────────────────────────────────────
HDD                 Overwrite            Secure Erase
SSD                 Secure Erase         Crypto Erase + Destroy
Cloud Storage       API Delete           API Delete + Key Delete
Mobile Device       Factory Reset        MDM Wipe + Factory Reset
Paper               Cross-cut P-4        Cross-cut P-5
End-of-Life         Physical Destruction Physical Destruction

STEP 3: VERIFY DELETION
─────────────────────────────────────────────────────────────
☑ Check deletion tool logs (no errors)
☑ Verify data no longer accessible
☑ Collect certificates (physical destruction)
☑ Log deletion in central system

STEP 4: DOCUMENT
─────────────────────────────────────────────────────────────
Required Documentation:
- Deletion log entry (what, when, who, how)
- Tool output/certificate
- Verification result

COMMON SCENARIOS - QUICK ACTIONS
─────────────────────────────────────────────────────────────
Scenario                         Action
──────────────────────────────────────────────────────────────
Customer requests data deletion  → Use Form S5.B, contact DPO
Decommissioning cloud VM         → Delete instance + volumes via API
Disposing of old laptop          → Remove HDD/SSD, destroy separately
Deleting database records        → Hard delete + vacuum/optimize
Terminating SaaS contract        → Export data, request account deletion
Legal hold released              → Resume normal deletion schedule
Backup retention expired         → Automatic deletion per schedule

EMERGENCY CONTACTS
─────────────────────────────────────────────────────────────
DPO (Data Protection):    [Email/Phone]
CISO (Security):          [Email/Phone]
IT Operations:            [Email/Phone]
Legal (Legal Holds):      [Email/Phone]

POLICY LOCATION
─────────────────────────────────────────────────────────────
Full Policy: [Intranet/SharePoint URL]
Forms: [Forms Repository URL]
Training: [LMS URL]

Remember: When in doubt, ASK. Better to delay deletion than
delete incorrectly or retain improperly.
```

---

## Annex S5.E: Policy Exception Request Form

### Purpose
Standardized form for requesting exceptions to retention and deletion requirements.

### Form Template
```
POLICY EXCEPTION REQUEST
ISMS-POL-A.8.10-S5.E

Request Information
─────────────────────────────────────────────────────────────
Exception ID: [Auto-generated: EXC-YYYY-NNNN]
Request Date: ______________________________________________
Requested By: ______________________________________________
Department: ________________________________________________
Contact Email/Phone: _______________________________________

Data and Policy Information
─────────────────────────────────────────────────────────────
Data Category: _____________________________________________
Current Retention Period: __________________________________
Policy Requirement Being Excepted:
_____________________________________________________________
_____________________________________________________________

Exception Details
─────────────────────────────────────────────────────────────
Requested Exception:
☐ Extend retention period to: _____ [years/months]
☐ Delay deletion until: _____ [date/event]
☐ Use alternative deletion method: _________________________
☐ Other: ___________________________________________________

Duration of Exception:
☐ Temporary (specify end date): ____________________________
☐ Ongoing (review annually)

Business/Legal Justification (required - be specific)
─────────────────────────────────────────────────────────────
Reason for Exception:
☐ Legal/regulatory requirement (specify law/regulation):
  _________________________________________________________
☐ Active litigation (case number): _________________________
☐ Regulatory investigation (authority): ____________________
☐ Technical infeasibility (explain): _______________________
☐ Business continuity (explain impact if denied):
  _________________________________________________________
☐ Other (explain): _________________________________________

Detailed Justification:
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________

Impact if Exception Denied:
_____________________________________________________________
_____________________________________________________________

Risk Assessment
─────────────────────────────────────────────────────────────
Data Volume Affected: ______________________________________
Number of Data Subjects (if personal data): ________________
Data Sensitivity: ☐ Low  ☐ Medium  ☐ High  ☐ Restricted

Risks of Granting Exception:
_____________________________________________________________
_____________________________________________________________

Proposed Compensating Controls (required for approval):
☐ Enhanced encryption
☐ Restricted access (specify): _____________________________
☐ Increased monitoring/logging
☐ Periodic review (frequency): _____________________________
☐ Physical isolation
☐ Other: ___________________________________________________

Review and Approval
─────────────────────────────────────────────────────────────
CISO Technical Review:
☐ Approved  ☐ Denied  ☐ Approved with conditions
Comments: __________________________________________________
Signature: _______________________ Date: __________________

DPO Compliance Review (personal data only):
☐ Approved  ☐ Denied  ☐ Approved with conditions
Comments: __________________________________________________
Signature: _______________________ Date: __________________

Legal Review (if legal basis claimed):
☐ Approved  ☐ Denied  ☐ Approved with conditions
Comments: __________________________________________________
Signature: _______________________ Date: __________________

Final Approval Authority:
☐ CISO (non-personal data, <12 months)
☐ DPO + CISO (personal data or high-risk)
☐ DPO + CISO + General Counsel (legal basis)

Approval Decision: ☐ APPROVED  ☐ DENIED
Approver Signature: __________________ Date: ______________

Exception Terms (if approved)
─────────────────────────────────────────────────────────────
Exception Valid From: ______________________________________
Exception Valid Until: _____________________________________
Review Date: _______________________________________________
Compensating Controls Required:
_____________________________________________________________

Conditions of Approval:
_____________________________________________________________
_____________________________________________________________

Exception Monitoring and Closure
─────────────────────────────────────────────────────────────
Exception Logged in Register: ☐ YES  Entry ID: ____________
Quarterly Review Dates: ____________________________________
Exception Closed/Revoked: Date: ____________________________
Reason for Closure: ________________________________________
```

---

## Annex S5.F: Deletion Log Template

### Purpose
Standardized log entry format for central deletion logging.

### Log Entry Template (JSON Format)
```json
{
  "deletion_log_entry": {
    "log_id": "DEL-2026-00001234",
    "timestamp": "2026-01-05T14:32:17Z",
    "deletion_metadata": {
      "data_id": "customer_record_847392",
      "data_category": "customer_personal_data",
      "data_sensitivity": "medium",
      "record_count": 1,
      "data_volume_mb": 0.5
    },
    "trigger": {
      "type": "retention_period_expired",
      "details": "Customer account closed 3 years ago, retention period = 3 years",
      "retention_period_days": 1095,
      "legal_basis": "contract_performance_ended"
    },
    "deletion_execution": {
      "method": "database_hard_delete",
      "tool": "PostgreSQL_14.2",
      "operator": "automated_retention_job",
      "system": "production_crm_database",
      "location": "eu-central-1"
    },
    "result": {
      "status": "success",
      "completion_time": "2026-01-05T14:32:18Z",
      "errors": null,
      "warnings": null
    },
    "verification": {
      "method": "database_query_verification",
      "result": "record_not_found",
      "verified_by": "automated_verification_script",
      "verification_timestamp": "2026-01-05T14:32:20Z"
    },
    "evidence": {
      "log_file": "/logs/deletions/2026/01/DEL-2026-00001234.log",
      "certificate_id": null,
      "screenshots": null
    },
    "compliance": {
      "gdpr_applicable": true,
      "legal_hold_checked": true,
      "legal_hold_active": false,
      "data_subject_request": false
    },
    "backup_handling": {
      "backups_affected": true,
      "backup_deletion_method": "rotation_schedule",
      "backup_deletion_eta": "2026-02-01"
    }
  }
}
```

### Usage Instructions
- Use this structure for automated deletion logging
- Manual deletions can use simplified CSV format
- Store logs in tamper-evident repository (WORM, cryptographic signing)
- Retain logs for minimum 3 years

---

## Annex S5.G: Certificate of Destruction Template

### Purpose
Template for third-party vendors providing deletion/destruction services.

### Certificate Template
```
═══════════════════════════════════════════════════════════
               CERTIFICATE OF DESTRUCTION
               ISMS-POL-A.8.10-S5.G
═══════════════════════════════════════════════════════════

Vendor Information
─────────────────────────────────────────────────────────────
Company Name: ______________________________________________
Address: ___________________________________________________
Contact Person: ____________________________________________
Phone/Email: _______________________________________________
Certifications: ☐ NAID AAA  ☐ ISO 27001  ☐ R2  ☐ e-Stewards
License Number (if applicable): ____________________________

Customer Information
─────────────────────────────────────────────────────────────
Organization: ______________________________________________
Contact Person: ____________________________________________
Service Order Number: ______________________________________

Destruction Details
─────────────────────────────────────────────────────────────
Destruction Date: __________________________________________
Destruction Location: ______________________________________
Destruction Method: ☐ Shredding  ☐ Incineration  ☐ Degaussing
                    ☐ Crushing   ☐ Disintegration  ☐ Other: ___
Standard Compliance: ☐ NIST SP 800-88  ☐ DIN 66399 P-___
                     ☐ DoD 5220.22-M   ☐ Other: ____________

Media Inventory
─────────────────────────────────────────────────────────────
Media Type    Quantity    Serial Numbers/Asset Tags
─────────────────────────────────────────────────────────────
Hard Drives   _______     ________________________________
SSDs          _______     ________________________________
Tapes         _______     ________________________________
Paper (boxes) _______     ________________________________
Optical Media _______     ________________________________
Other         _______     ________________________________

Total Items Destroyed: _____________________________________

Destruction Specifics
─────────────────────────────────────────────────────────────
Shredder Model (if applicable): ____________________________
Particle Size Achieved: ____________________________________
Degausser Model (if applicable): ___________________________
Magnetic Field Strength: ___________________________________

Witness Information
─────────────────────────────────────────────────────────────
Customer Witness Present: ☐ YES  ☐ NO
Witness Name: ______________________________________________
Witness Signature: __________________ Date: _______________

Photographic/Video Evidence: ☐ Attached  ☐ Available upon request

Chain of Custody
─────────────────────────────────────────────────────────────
Pickup Date: _______________________________________________
Pickup Location: ___________________________________________
Transport Method: ☐ Secure truck  ☐ Customer delivery  ☐ Other
Tamper-Evident Seals: ☐ YES (Seal #: _______)  ☐ NO
Arrival at Destruction Facility: __________________________
Destruction Delay (if any): ________________________________

Environmental Compliance
─────────────────────────────────────────────────────────────
Recycling Performed: ☐ YES  ☐ NO
Material Recycled: _________________________________________
Disposal Method (non-recyclable): __________________________
Environmental Certifications: ☐ R2  ☐ e-Stewards  ☐ Other: ___

Certification Statement
─────────────────────────────────────────────────────────────
I hereby certify that the media and materials listed above
have been destroyed in accordance with the specified method
and industry standards. All data has been rendered
irrecoverable by commercially available means.

Authorized Representative
Name: ______________________________________________________
Title: _____________________________________________________
Signature: ____________________ Date: _____________________
Company Seal/Stamp: [SPACE FOR SEAL]

Certificate ID: CER-DEST-____________________________________
Issue Date: ________________________________________________

For questions regarding this certificate, contact:
[Vendor Contact Information]

═══════════════════════════════════════════════════════════
     This certificate shall be retained for 3 years
═══════════════════════════════════════════════════════════
```

---

## Annex S5.H: Approved Deletion Tools List

### Purpose
Current list of validated and approved deletion tools by media type.

### Approved Tools Registry

**Last Updated**: [Update Date]  
**Review Frequency**: Quarterly  
**Tool Validation Process**: See ISMS-POL-A.8.10-S2.2 §2.2.10

| Tool Name | Media Type | Method | License | Validated Version | Approval Date | Notes |
|-----------|------------|--------|---------|-------------------|---------------|-------|
| **DBAN** | HDD | Overwrite | Free (GPL) | 2.3.0 | [Date] | Bootable, multiple passes |
| **Blancco Drive Eraser** | HDD, SSD | Secure Erase | Commercial | 7.x | [Date] | Generates certificates |
| **BitRaser** | HDD, SSD, Mobile | Secure Erase | Commercial | 6.x | [Date] | Enterprise management |
| **hdparm** | HDD, SSD | ATA Secure Erase | Free | 9.x | [Date] | Linux CLI, verify vendor support |
| **nvme-cli** | NVMe SSD | NVMe Sanitize | Free | 1.x | [Date] | Linux CLI for NVMe drives |
| **Parted Magic** | HDD, SSD | Secure Erase | Commercial | 2024.x | [Date] | GUI, bootable, includes hdparm |
| **shred** | Files (HDD only) | Overwrite | Free (GNU) | Latest | [Date] | NOT for SSD, per-file deletion |
| **AWS CLI** | AWS S3, EBS | API Deletion | Free | 2.x | [Date] | Cloud storage deletion |
| **Azure CLI** | Azure Blob, Disk | API Deletion | Free | 2.x | [Date] | Cloud storage deletion |
| **gcloud** | GCS, GCE | API Deletion | Free | Latest | [Date] | Google Cloud deletion |
| **Intune/MDM** | Mobile devices | Remote Wipe | Commercial | Latest | [Date] | Enterprise mobile management |
| **Vendor SED Tools** | Self-Encrypting Drives | Crypto Erase | Varies | Varies | [Date] | Manufacturer-specific tools |

### Physical Destruction Vendors

| Vendor Name | Services | Certifications | Service Area | Approval Date |
|-------------|----------|----------------|--------------|---------------|
| [Vendor 1] | Shredding, degaussing | NAID AAA, ISO 27001 | [Region] | [Date] |
| [Vendor 2] | On-site shredding | NAID AAA, R2 | [Region] | [Date] |
| [Vendor 3] | Incineration | ISO 27001 | [Region] | [Date] |

### Tool Validation Checklist

Before adding a new tool:
☐ Vendor reputation verified
☐ Tool effectiveness tested (forensic recovery attempt)
☐ Documentation reviewed (user manual, security white paper)
☐ Compliance alignment verified (NIST SP 800-88, DIN 66399)
☐ Support availability confirmed (vendor support, community)
☐ License cost acceptable (budget approval)
☐ Training requirements identified
☐ CISO approval obtained

---

## Annex S5.I: Cloud Provider Deletion Procedures

### Purpose
Quick reference for deletion procedures across major cloud providers.

### AWS (Amazon Web Services)

**Object Storage (S3)**:
```bash
# Delete single object
aws s3 rm s3://bucket-name/object-key

# Delete all objects in bucket (empty bucket)
aws s3 rm s3://bucket-name --recursive

# Delete all versions (versioned bucket)
aws s3api delete-objects --bucket bucket-name \
  --delete "$(aws s3api list-object-versions \
  --bucket bucket-name --output=json \
  --query='{Objects: Versions[].{Key:Key,VersionId:VersionId}}')"

# Delete bucket (after emptying)
aws s3 rb s3://bucket-name
```

**Compute (EC2)**:
```bash
# Terminate instance (will delete ephemeral storage)
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0

# Delete EBS volume
aws ec2 delete-volume --volume-id vol-1234567890abcdef0

# Delete snapshot
aws ec2 delete-snapshot --snapshot-id snap-1234567890abcdef0
```

**Database (RDS)**:
```bash
# Delete RDS instance without final snapshot
aws rds delete-db-instance --db-instance-identifier mydb \
  --skip-final-snapshot

# Delete manual snapshot
aws rds delete-db-snapshot --db-snapshot-identifier mydbsnapshot
```

**Cryptographic Erasure**:
```bash
# Schedule KMS key deletion (7-30 days waiting period)
aws kms schedule-key-deletion --key-id alias/my-key \
  --pending-window-in-days 7
```

### Microsoft Azure

**Object Storage (Blob)**:
```bash
# Delete blob
az storage blob delete --account-name mystorageaccount \
  --container-name mycontainer --name myblob

# Delete container
az storage container delete --account-name mystorageaccount \
  --name mycontainer

# Delete storage account
az storage account delete --name mystorageaccount --resource-group mygroup
```

**Compute (VM)**:
```bash
# Delete VM
az vm delete --resource-group mygroup --name myvm --yes

# Delete disk
az disk delete --resource-group mygroup --name mydisk --yes

# Delete snapshot
az snapshot delete --resource-group mygroup --name mysnapshot --yes
```

**Database (SQL Database)**:
```bash
# Delete database
az sql db delete --resource-group mygroup --server myserver \
  --name mydb --yes
```

**Cryptographic Erasure**:
```bash
# Delete key (immediate, purge required for permanent)
az keyvault key delete --vault-name myvault --name mykey

# Purge deleted key (permanent, irreversible)
az keyvault key purge --vault-name myvault --name mykey
```

### Google Cloud Platform (GCP)

**Object Storage (GCS)**:
```bash
# Delete object
gsutil rm gs://bucket-name/object-name

# Delete all objects in bucket
gsutil -m rm -r gs://bucket-name/*

# Delete bucket
gsutil rb gs://bucket-name
```

**Compute (GCE)**:
```bash
# Delete instance
gcloud compute instances delete instance-name --zone=us-central1-a

# Delete disk
gcloud compute disks delete disk-name --zone=us-central1-a

# Delete snapshot
gcloud compute snapshots delete snapshot-name
```

**Database (Cloud SQL)**:
```bash
# Delete Cloud SQL instance
gcloud sql instances delete instance-name
```

**Cryptographic Erasure**:
```bash
# Delete Cloud KMS key version (cannot delete entire key, only versions)
gcloud kms keys versions destroy 1 --key=my-key \
  --keyring=my-keyring --location=global
```

### Verification Commands

After deletion, verify removal:

**AWS**:
```bash
aws s3 ls s3://bucket-name  # Should return empty or NoSuchBucket
aws ec2 describe-volumes --volume-ids vol-xxx  # Should return error
```

**Azure**:
```bash
az storage blob list --account-name xxx --container-name xxx  # Empty
az vm show --resource-group xxx --name xxx  # Should return error
```

**GCP**:
```bash
gsutil ls gs://bucket-name  # Should return BucketNotFoundException
gcloud compute instances describe xxx  # Should return error
```

### Notes
- Always verify deletion through API/CLI (don't trust console alone)
- Check ALL regions where data may exist
- Delete snapshots and backups separately (not auto-deleted)
- For crypto-erasure: Delete encryption keys AFTER data deletion
- Wait for confirmation before considering deletion complete

---

## 5.3 Annex Maintenance

### 5.3.1 Update Process

Annexes **SHALL** be updated:

- **Tools List (S5.H)**: Quarterly review, updates within 30 days of new tool approval
- **Forms (S5.B, S5.E, S5.F)**: As needed based on user feedback, annual review minimum
- **Checklists (S5.C)**: As needed based on audit findings, annual review minimum
- **Quick Reference (S5.D)**: Annual review, updates when policy requirements change
- **Cloud Procedures (S5.I)**: Quarterly review (cloud providers change frequently)
- **Deletion Matrix (S5.A)**: Annual review, updates when new media types emerge

### 5.3.2 Version Control

Annex updates **SHALL**:
- Increment patch version (e.g., S5.A v1.0.1 → v1.0.2)
- Document changes in version history
- Notify affected users (IT Ops for tool changes, DPO for form changes)
- Retain previous versions for reference (minimum 2 versions)

### 5.3.3 User Feedback

Organizations **SHOULD** collect feedback on annexes:
- Annual survey: "Are the tools/forms practical and helpful?"
- Issue tracking: Report problems with forms/procedures
- Continuous improvement: Incorporate lessons learned quarterly

---

**END OF DOCUMENT**

*"A policy without practical tools is like a recipe without ingredients — technically correct but utterly useless."* — Every frustrated policy implementer