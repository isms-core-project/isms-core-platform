**ISMS-IMP-A.8.17-S3-TG - Exception Management**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Clock Synchronization Exception Management |
| **Related Policy** | ISMS-POL-A.8.17 (Clock Synchronization Policy - Section 3.3) |
| **Purpose** | Document and manage systems that cannot meet clock synchronization requirements, including air-gapped systems, legacy equipment, and special use cases |
| **Target Audience** | System Administrators, Network Engineers, Security Engineers, ISMS Officers, Risk Managers, Auditors |
| **Assessment Type** | Operational & Risk Management |
| **Review Cycle** | Quarterly or When Exceptions Change |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original Date] | Initial technical specification for exception management | ISMS Officer |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.17-S3-UG.

---

# Technical Specification

**Audience:** Workbook developers, Python script maintainers, technical implementers

**Note:** This section provides technical specifications for exception management workbook structure. Users completing the assessment should refer to Part I above.

---

# Implementation Requirement Mapping

**This section maps policy requirements (REQ-817-xxx codes) to ISMS-POL-A.8.17 sections for traceability.**

## S3 Requirements (REQ-817-017 through REQ-817-023)

| Requirement ID | Policy Section | Requirement Summary |
|---------------|----------------|---------------------|
| REQ-817-017 | Section 3.3 | Formal exception process required for non-compliant systems |
| REQ-817-018 | Section 3.3 | All exceptions require documented justification |
| REQ-817-019 | Section 3.3 | Compensating controls required for all exceptions |
| REQ-817-020 | Section 3.3 | Risk acceptance required from appropriate authority |
| REQ-817-021 | Section 3.3 | Exception review minimum quarterly |
| REQ-817-022 | Section 3.3 | Maximum exception duration 12 months |
| REQ-817-023 | Section 3.3 | Permanent exceptions require CISO and Executive approval |

---

# SECTION A: Implementation Guidance

## Introduction

This section provides technical guidance for managing clock synchronization exceptions, including categorization, risk assessment, and compensating control design.

**Purpose:** Enable ISMS Officers and System Administrators to implement a robust exception management process that maintains accountability while accommodating legitimate technical constraints.

**Scope:** Systems that cannot meet standard NTP synchronization requirements due to air-gap, legacy, vendor, or business constraints.

**Related Documents:**

- ISMS-POL-A.8.17 (Clock Synchronization Policy)
- ISMS-IMP-A.8.17-S1 (Time Source Configuration)
- ISMS-IMP-A.8.17-S2 (Synchronization Verification)
- ISMS-IMP-A.8.17-S4 (Compliance Dashboard)

---

## Exception Categories

### Air-Gapped Systems (No Network)

**Definition:** Systems intentionally isolated from network connectivity for security or safety reasons.

**Common Examples:**

- OT/ICS systems (PLCs, SCADA, HMIs) in manufacturing
- High-security classified systems
- Research systems with sensitive data
- Safety-critical systems per IEC 62443

**Typical Justification:**

> "System is air-gapped per [safety standard/security requirement]. Network connectivity would violate [standard] and create [safety/security] risk."

**Recommended Compensating Controls:**

1. **Local GPS Receiver** - Install dedicated GPS time receiver within air-gapped network
   - Stratum 0/1 accuracy
   - Independent of external network
   - Example: Meinberg, EndRun, Symmetricom appliances

2. **Manual Time Synchronization** - Periodic manual clock setting
   - Monthly or quarterly depending on drift tolerance
   - Documented procedure with verification
   - Audit trail of sync events

3. **Local Atomic Clock** - For highest accuracy requirements
   - Expensive but provides ultimate independence
   - Typically only for critical infrastructure

---

### Legacy Systems (No NTP Support)

**Definition:** Older systems that do not support NTP protocol or configuration.

**Common Examples:**

- Legacy ERP systems (pre-2010)
- Old mainframe applications
- Embedded systems with fixed firmware
- Proprietary industrial controllers

**Typical Justification:**

> "System is [Vendor] [Product] version [X.Y] from [Year]. Vendor confirmed no NTP support in this version. System is scheduled for replacement in [Quarter/Year]."

**Recommended Compensating Controls:**

1. **Manual Time Synchronization** - Documented manual sync procedure
   - Frequency based on system drift rate
   - Admin console or hardware clock access
   - Verification after each sync

2. **Planned Remediation** - Document replacement timeline
   - Link to project/budget approval
   - Track progress toward compliant replacement
   - Exception tied to remediation completion

3. **Log Correlation Adjustment** - If logs must be correlated
   - Document time offset from reference
   - Apply offset in SIEM during correlation
   - Accept reduced accuracy for forensics

---

### Vendor Restrictions

**Definition:** Systems where vendor configuration does not permit NTP customization.

**Common Examples:**

- SaaS appliances with locked-down OS
- Security appliances with vendor-managed time
- Cloud services with provider time sync
- Proprietary network devices

**Typical Justification:**

> "System is [Vendor] [Product]. Vendor does not expose NTP configuration per support case #[Number]. System uses vendor-managed time synchronization to [Vendor Cloud Service]."

**Recommended Compensating Controls:**

1. **Vendor-Managed Sync** - Accept vendor time source
   - Document vendor SLA for time accuracy
   - Monitor for drift using external validation
   - Retain vendor support case as evidence

2. **Drift Monitoring** - External validation of vendor sync
   - Compare system time against reference
   - Alert if drift exceeds threshold
   - Document acceptable variance

3. **Vendor Escalation** - Request feature enhancement
   - Document escalation request
   - Track vendor roadmap for NTP support
   - Re-evaluate at exception renewal

---

### Regulatory Requirements

**Definition:** Systems where regulations require specific time source or prohibit standard NTP.

**Common Examples:**

- Financial trading systems (MiFID II timestamp requirements)
- Healthcare systems (specific time source requirements)
- Government systems (certified time sources only)

**Typical Justification:**

> "System must use [Specific Time Source] per [Regulation] Article [X]. Standard organizational NTP infrastructure does not meet regulatory requirements for [accuracy/auditability/certification]."

**Recommended Compensating Controls:**

1. **Regulatory-Compliant Time Source** - Use required time source
   - Document regulatory requirement
   - Implement compliant time infrastructure
   - May require dedicated NTP path

2. **Audit Trail** - Enhanced logging for regulated systems
   - Capture time source information in logs
   - Retain for regulatory retention period
   - Support audit inquiries

---

### Business Requirements

**Definition:** Systems where business need prevents standard NTP implementation.

**Common Examples:**

- Test/lab environments requiring time manipulation
- Development systems with clock testing requirements
- Demonstration systems with specific time scenarios

**Typical Justification:**

> "System is [purpose] requiring [time manipulation/specific time/isolated operation]. Standard NTP would [interfere with testing/break functionality]."

**Recommended Compensating Controls:**

1. **Isolated Time Management** - Controlled time within environment
   - Document purpose and scope
   - Limit exception to specific systems
   - Prevent cross-contamination with production

2. **Periodic Resync** - Reset to accurate time periodically
   - After testing cycles
   - Before production deployment
   - Documented procedure

---

## Risk Assessment Guidance

### Risk Factors to Consider

**Impact of Unsynchronized Time:**

1. **Log Correlation** - Can logs be correlated with other systems?
   - Critical: Forensic investigation capability
   - High: SIEM correlation, incident response
   - Medium: Operational troubleshooting
   - Low: Isolated systems with local-only logs

2. **Authentication** - Does time affect authentication?
   - Critical: Kerberos (5-minute tolerance)
   - High: Certificate validation
   - Medium: Token expiration
   - Low: No time-dependent authentication

3. **Compliance** - Does non-compliance create regulatory risk?
   - Critical: Financial/healthcare regulations
   - High: Audit findings
   - Medium: Policy variance
   - Low: Internal guidance only

4. **Operations** - Does time affect operations?
   - Critical: Scheduling, batch processing
   - High: Reporting accuracy
   - Medium: User convenience
   - Low: No operational impact

### Risk Rating Matrix

| Impact | Compensating Control Effectiveness | Risk Rating |
|--------|-------------------------------------|-------------|
| Critical | Strong (GPS, atomic) | High - CISO approval |
| Critical | Moderate (manual sync) | Critical - May not be acceptable |
| High | Strong | Medium - Risk owner approval |
| High | Moderate | High - CISO approval |
| Medium | Any | Low-Medium - Risk owner approval |
| Low | Any | Low - Standard exception |

### Documentation Requirements by Risk Level

**Low Risk:**

- Basic justification
- Compensating control description
- Risk owner approval

**Medium Risk:**

- Detailed justification with technical assessment
- Compensating control implementation evidence
- Risk owner approval
- Quarterly review

**High Risk:**

- Formal risk assessment document
- Compensating control effectiveness validation
- Risk owner AND CISO approval
- Monthly review

**Critical Risk:**

- Full risk analysis with executive summary
- Compensating control proof of effectiveness
- Risk owner, CISO, AND Executive approval
- Or: Do not approve exception

---

## Compensating Control Implementation

### Local GPS Receiver Installation

**Purpose:** Provide Stratum 0/1 time source for air-gapped networks.

**Hardware Options:**

| Product | Stratum | Typical Cost | Notes |
|---------|---------|--------------|-------|
| Meinberg LANTIME M300 | 1 | €3,000-5,000 | Enterprise grade |
| EndRun Meridian II | 1 | $2,000-4,000 | Good accuracy |
| Microsemi/Symmetricom | 1 | $3,000-8,000 | High precision |
| Budget GPS (ublox-based) | 1 | €200-500 | Hobbyist, less reliable |

**Installation Requirements:**

1. GPS antenna with clear sky view (roof mount typically)
2. Lightning protection for outdoor antenna
3. Network connectivity within air-gapped zone
4. Power with UPS backup

**Configuration:**

- Configure as NTP server for air-gapped network
- Air-gapped systems point to local GPS NTP
- Monitor GPS signal lock status

**Verification:**

```bash
# On GPS NTP appliance
chronyc tracking   # Should show refid = GPS or PPS
chronyc sources    # Should show GPS source selected

# On air-gapped systems
chronyc tracking   # Should show local GPS NTP as source
```

---

### Manual Time Synchronization Procedure

**Purpose:** Periodic manual clock setting for systems without NTP.

**Procedure Template:**

1. **Preparation**
   - Access authoritative time reference (time.nist.gov, GPS receiver)
   - Document current system time before sync
   - Note offset for audit trail

2. **Synchronization**
   - Access system clock settings (admin console, BIOS, CLI)
   - Set time to match reference
   - Set date if required
   - Apply changes

3. **Verification**
   - Confirm system time matches reference (within tolerance)
   - Document post-sync time
   - Calculate and record sync offset

4. **Documentation**
   - Record sync event in exception log
   - Sign-off by authorized personnel
   - File evidence (screenshot, log entry)

**Frequency Guidance:**

| System Drift Rate | Sync Frequency |
|-------------------|----------------|
| <1 second/day | Monthly |
| 1-5 seconds/day | Weekly |
| >5 seconds/day | Daily (or remediate) |

---

### Drift Monitoring for Vendor-Managed Systems

**Purpose:** Validate vendor time synchronization is working.

**Monitoring Approach:**

1. **External Time Comparison**
   - Query vendor system time via API or log timestamp
   - Compare to authoritative reference
   - Alert if delta exceeds threshold

2. **Log Timestamp Analysis**
   - Monitor logs for timestamp anomalies
   - Compare log timestamps to correlated events
   - Flag significant discrepancies

3. **Periodic Manual Validation**
   - Monthly manual check of system time
   - Document comparison to reference
   - Escalate to vendor if drift exceeds SLA

**Alert Thresholds:**

| System Criticality | Alert Threshold | Action |
|--------------------|-----------------|--------|
| Critical | >100ms | Immediate investigation |
| High | >500ms | Same-day review |
| Medium | >1 second | Next business day |
| Low | >5 seconds | Weekly review |

---

# SECTION B: Assessment Workbook Specification

## Workbook Overview

**Filename:** ISMS-IMP-A.8.17-S3_Exception_Management_[YYYYMMDD].xlsx

**Generated By:** `generate_a817_s3_exception_management.py`

**Purpose:** Template for documenting and managing clock synchronization exceptions

**Sheets:**
1. **Instructions** - Workbook usage instructions and legend
2. **Exception_Requests** - New exception request workflow
3. **Active_Exceptions** - Currently approved exceptions
4. **Expired_Exceptions** - Historical expired exceptions
5. **Summary_Dashboard** - Exception metrics overview

**Total Sheets:** 5

---

## Common Styling Definitions

**Header Style:**

- Font: Bold, White (FFFFFF), Size 11
- Fill: Dark Blue (366092)
- Alignment: Center, Vertical Center, Wrap Text
- Border: Thin borders all sides

**Title Style:**

- Font: Bold, Size 14, Dark Blue (366092)
- Alignment: Left, Vertical Center

**Data Cell Style:**

- Alignment: Left, Vertical Center, Wrap Text
- Border: Thin borders all sides

**Center Style:**

- Alignment: Center, Vertical Center
- Border: Thin borders all sides

---

## Sheet 1: Instructions

**Purpose:** Provide workbook usage instructions, status legend, and navigation guidance.

**Layout:**

**Row 1-2:** Title Block

- A1: "ISMS A.8.17-S3 - Exception Management" (Font: Bold 16, Dark Blue, Merged A1:F1)
- A2: "Generated: [Timestamp]" (Font: Italic 10, Merged A2:F2)

**Row 4-5:** Document Metadata

- A4: "Document ID:" (Bold) | B4: "ISMS-IMP-A.8.17-S3" (Bold, Dark Blue)
- A5: "Title:" (Bold) | B5: "Clock Synchronization Exception Management"

**Row 7+:** Instructions Content

- Purpose statement
- Sheet descriptions
- Status legend (Exception_Requests, Active_Exceptions)
- Approval workflow summary
- Compensating control guidance
- Link to ISMS-POL-A.8.17 Section 3.3

**Column Widths:**

- A: 15
- B: 80
- C-F: 15 each

---

## Sheet 2: Exception_Requests

**Purpose:** Document pending exception requests requiring approval.

**Headers (Row 1):**

| Column | Header | Width | Required | Data Type | Dropdown/Validation |
|--------|--------|-------|----------|-----------|---------------------|
| A | Request ID [*] | 18 | Yes | Text | None |
| B | System Name [*] | 22 | Yes | Text | None |
| C | System Type [*] | 18 | Yes | Dropdown | OT/ICS System, Legacy System, Vendor Appliance, Air-Gapped System, Embedded Device, Test/Lab System, Other |
| D | Business Owner [*] | 20 | Yes | Text | None |
| E | Exception Category [*] | 22 | Yes | Dropdown | Air-Gapped (No Network), Legacy (No NTP Support), Vendor Restriction, Regulatory Requirement, Business Requirement, Other |
| F | Justification [*] | 40 | Yes | Text | None |
| G | Risk Assessment [*] | 35 | Yes | Text | None |
| H | Compensating Controls [*] | 40 | Yes | Text | None |
| I | Requested Duration [*] | 15 | Yes | Dropdown | 3 months, 6 months, 12 months, Permanent |
| J | Request Date [*] | 12 | Yes | Date | None |
| K | Requested By [*] | 18 | Yes | Text | None |
| L | Risk Owner Approval | 15 | No | Dropdown | Pending, Approved, Rejected |
| M | Risk Owner Date | 12 | No | Date | None |
| N | CISO Approval | 15 | No | Dropdown | Not Required, Pending, Approved, Rejected |
| O | CISO Date | 12 | No | Date | None |
| P | Request Status [*] | 18 | Yes | Dropdown | Draft, Submitted, Risk Owner Review, CISO Review, Approved, Rejected, Withdrawn |
| Q | Notes | 35 | No | Text | None |

**Data Validation:**

**Column C (System Type):**

- Type: List
- Formula: `"OT/ICS System,Legacy System,Vendor Appliance,Air-Gapped System,Embedded Device,Test/Lab System,Other"`
- Applies To: C2:C100

**Column E (Exception Category):**

- Type: List
- Formula: `"Air-Gapped (No Network),Legacy (No NTP Support),Vendor Restriction,Regulatory Requirement,Business Requirement,Other"`
- Applies To: E2:E100

**Column I (Requested Duration):**

- Type: List
- Formula: `"3 months,6 months,12 months,Permanent"`
- Applies To: I2:I100

**Column L (Risk Owner Approval):**

- Type: List
- Formula: `"Pending,Approved,Rejected"`
- Applies To: L2:L100

**Column N (CISO Approval):**

- Type: List
- Formula: `"Not Required,Pending,Approved,Rejected"`
- Applies To: N2:N100

**Column P (Request Status):**

- Type: List
- Formula: `"Draft,Submitted,Risk Owner Review,CISO Review,Approved,Rejected,Withdrawn"`
- Applies To: P2:P100

**Empty Template Rows:** Rows 2-20 (formatted with borders, no data)

**Freeze Panes:** A2 (freeze header row)

---

## Sheet 3: Active_Exceptions

**Purpose:** Document currently approved and active exceptions.

**Headers (Row 1):**

| Column | Header | Width | Required | Data Type | Dropdown/Validation |
|--------|--------|-------|----------|-----------|---------------------|
| A | Exception ID [*] | 18 | Yes | Text | None |
| B | System Name [*] | 22 | Yes | Text | None |
| C | System Type [*] | 18 | Yes | Dropdown | (same as Exception_Requests) |
| D | Business Owner [*] | 20 | Yes | Text | None |
| E | Exception Category [*] | 22 | Yes | Dropdown | (same as Exception_Requests) |
| F | Approved Justification [*] | 40 | Yes | Text | None |
| G | Compensating Controls [*] | 40 | Yes | Text | None |
| H | Approval Date [*] | 12 | Yes | Date | None |
| I | Approved By [*] | 25 | Yes | Text | None |
| J | Expiration Date [*] | 12 | Yes | Date | None |
| K | Review Schedule [*] | 15 | Yes | Dropdown | Monthly, Quarterly, Semi-annually |
| L | Last Review Date | 12 | No | Date | None |
| M | Review Status | 15 | No | Dropdown | Current, Overdue, Review Scheduled |
| N | Responsible Party [*] | 20 | Yes | Text | None |
| O | Renewal Status | 15 | No | Dropdown | Not Due, In Progress, Renewed, Expiring Soon |
| P | Notes | 35 | No | Text | None |

**Data Validation:**

**Column K (Review Schedule):**

- Type: List
- Formula: `"Monthly,Quarterly,Semi-annually"`
- Applies To: K2:K100

**Column M (Review Status):**

- Type: List
- Formula: `"Current,Overdue,Review Scheduled"`
- Applies To: M2:M100

**Column O (Renewal Status):**

- Type: List
- Formula: `"Not Due,In Progress,Renewed,Expiring Soon"`
- Applies To: O2:O100

**Conditional Formatting:**

- Expiration Date < TODAY(): Red fill (expired)
- Expiration Date < TODAY()+30: Yellow fill (expiring soon)
- Review Status = "Overdue": Red text

**Empty Template Rows:** Rows 2-20 (formatted with borders, no data)

**Freeze Panes:** A2 (freeze header row)

---

## Sheet 4: Expired_Exceptions

**Purpose:** Archive previously approved exceptions for historical tracking.

**Headers (Row 1):**

| Column | Header | Width | Required | Data Type | Dropdown/Validation |
|--------|--------|-------|----------|-----------|---------------------|
| A | Exception ID [*] | 18 | Yes | Text | None |
| B | System Name [*] | 22 | Yes | Text | None |
| C | System Type [*] | 18 | Yes | Text | None |
| D | Exception Category [*] | 22 | Yes | Text | None |
| E | Original Approval Date [*] | 15 | Yes | Date | None |
| F | Expiration Date [*] | 12 | Yes | Date | None |
| G | Expiration Reason [*] | 22 | Yes | Dropdown | Remediated (Now Compliant), Renewed (New Exception), System Decommissioned, Rejected on Renewal, Risk Accepted Permanently |
| H | Final Compensating Controls | 40 | No | Text | None |
| I | Successor Exception ID | 18 | No | Text | None |
| J | Lessons Learned | 40 | No | Text | None |
| K | Archived By [*] | 18 | Yes | Text | None |
| L | Archive Date [*] | 12 | Yes | Date | None |
| M | Notes | 35 | No | Text | None |

**Data Validation:**

**Column G (Expiration Reason):**

- Type: List
- Formula: `"Remediated (Now Compliant),Renewed (New Exception),System Decommissioned,Rejected on Renewal,Risk Accepted Permanently"`
- Applies To: G2:G100

**Empty Template Rows:** Rows 2-20 (formatted with borders, no data)

**Freeze Panes:** A2 (freeze header row)

---

## Sheet 5: Summary_Dashboard

**Purpose:** Provide management overview of exception status and trends.

**Layout:**

**Section 1: Exception Counts (Rows 1-8)**

| Row | Column A | Column B | Column C |
|-----|----------|----------|----------|
| 1 | "Exception Management Dashboard" (Title, merged A1:C1) | | |
| 2 | "Last Updated:" | [Date] | |
| 4 | "Metric" (Header) | "Count" (Header) | "Notes" (Header) |
| 5 | "Total Active Exceptions" | =COUNTA(Active_Exceptions!A2:A100) | |
| 6 | "Pending Requests" | =COUNTIF(Exception_Requests!P2:P100,"Submitted")+... | |
| 7 | "Expiring Next 30 Days" | =COUNTIFS(...) | Requires renewal action |
| 8 | "Expiring Next 90 Days" | =COUNTIFS(...) | Plan renewal process |

**Section 2: Exception Categories (Rows 10-18)**

| Row | Column A | Column B | Column C |
|-----|----------|----------|----------|
| 10 | "Exception Categories" (Header, merged) | | |
| 11 | "Category" (Header) | "Count" (Header) | "Percentage" (Header) |
| 12 | "Air-Gapped (No Network)" | =COUNTIF(Active_Exceptions!E:E,"Air-Gapped*") | =B12/B5 |
| 13 | "Legacy (No NTP Support)" | =COUNTIF(...) | =B13/B5 |
| ... | ... | ... | ... |

**Section 3: System Types (Rows 20-28)**

Similar structure to Section 2.

**Section 4: Review Status (Rows 30-35)**

| Row | Column A | Column B | Column C |
|-----|----------|----------|----------|
| 30 | "Review Status Summary" (Header, merged) | | |
| 31 | "Status" (Header) | "Count" (Header) | "Action Required" (Header) |
| 32 | "Current" | =COUNTIF(Active_Exceptions!M:M,"Current") | "None" |
| 33 | "Overdue" | =COUNTIF(Active_Exceptions!M:M,"Overdue") | "Immediate review required" |
| 34 | "Review Scheduled" | =COUNTIF(Active_Exceptions!M:M,"Review Scheduled") | "Per schedule" |

**Section 5: Upcoming Expirations (Rows 37-50)**

Auto-filtered list of exceptions expiring within 90 days.

**Section 6: Trend Analysis (Rows 52-60)**

Manual entry table for quarterly trends.

**Section 7: Key Observations (Rows 62+)**

Free-form text area for management comments.

---

## Python Script Reference

**Script File:** `generate_a817_s3_exception_management.py`

**Script Location:** `10-isms-scr-base/isms-a.8.17-clock-synchronization/10_generator-master/`

**Key Functions:**

- `create_styles()` - Defines all styling
- `create_instructions_sheet()` - Generates Instructions sheet
- `create_exception_requests_sheet()` - Generates Exception_Requests sheet
- `create_active_exceptions_sheet()` - Generates Active_Exceptions sheet
- `create_expired_exceptions_sheet()` - Generates Expired_Exceptions sheet
- `create_summary_dashboard_sheet()` - Generates Summary_Dashboard sheet
- `main()` - Orchestrates workbook generation

**To regenerate workbook:**

```bash
cd 10-isms-scr-base/isms-a.8.17-clock-synchronization/10_generator-master
python3 generate_a817_s3_exception_management.py
mv *.xlsx ../90_workbooks/
```

**Output:** Excel workbook ready for user completion per Part I User Guide.

---

**END OF SPECIFICATION**

---

*"Lost time is never found again."*
— Benjamin Franklin

<!-- QA_VERIFIED: 2026-02-06 -->
