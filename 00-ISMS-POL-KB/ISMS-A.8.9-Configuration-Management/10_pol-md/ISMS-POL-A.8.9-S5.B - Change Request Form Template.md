# ISMS-POL-A.8.9-S5.B
## Configuration Management - Change Request Form Template

**Document ID**: ISMS-POL-A.8.9-S5.B  
**Title**: Change Request Form Template  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Configuration Manager  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Configuration Manager | Initial change request form template |

**Review Cycle**: Annually  
**Next Review Date**: [Date + 1 year]  
**Approvers**: 
- Primary: Configuration Manager
- Review: Change Advisory Board (CAB) Chair

**Distribution**: All technical staff  
**Related Documents**: ISMS-POL-A.8.9-S2.2 (Change Control Requirements), ISMS-IMP-A.8.9.2 (Change Control Assessment)

---

## B.1 Purpose

This annex provides a **standard template** for submitting configuration change requests. A consistent format ensures:
- All necessary information is captured
- CAB can evaluate changes efficiently
- Audit trail is complete
- Implementation teams have clear guidance

**Note**: This is a template. [Organization] should adapt it to integrate with existing change management systems (ServiceNow, Jira, etc.).

---

## B.2 Change Request Form Template
```
================================================================================
CONFIGURATION CHANGE REQUEST FORM
================================================================================

SECTION 1: CHANGE IDENTIFICATION
================================================================================

Change Request ID: [Auto-generated or CR-YYYY-####]
Date Submitted: [DD.MM.YYYY]
Submitted By: [Name, Department, Contact Info]

Change Title: [Brief descriptive title, max 100 characters]

Change Classification:
☐ Standard Change (Pre-approved, following documented procedure)
☐ Normal Change (Requires CAB approval)
☐ Emergency Change (Urgent, expedited approval required)

If Emergency Change, Justification:
[Explain why this cannot wait for normal approval process]

================================================================================
SECTION 2: CHANGE DESCRIPTION
================================================================================

Business Justification:
[Why is this change needed? What business problem does it solve?]


Technical Description:
[What specifically will be changed? Provide technical details.]


Configuration Items (CIs) Affected:
[List all systems, applications, network devices, or services affected]
- Asset ID: [ID from CMDB], Asset Name: [Name], Asset Type: [Type]
- Asset ID: [ID from CMDB], Asset Name: [Name], Asset Type: [Type]
[Add rows as needed]

Change Scope:
☐ Single system
☐ Multiple systems (same type)
☐ Multiple systems (different types)
☐ Network infrastructure
☐ Cloud services
☐ Application configuration
☐ Database configuration
☐ Other: _______________

================================================================================
SECTION 3: IMPACT AND RISK ASSESSMENT
================================================================================

Expected Impact:

Business Impact:
☐ No impact - Transparent to users
☐ Low impact - Minimal user impact, no service interruption
☐ Medium impact - Noticeable to users, brief service interruption
☐ High impact - Significant user impact, extended service interruption
☐ Critical impact - Service outage, major business disruption

Technical Impact:
☐ No impact - Configuration only, no functional change
☐ Low impact - Minor functional enhancement or bug fix
☐ Medium impact - Moderate functional change, limited scope
☐ High impact - Significant functional change or architectural change
☐ Critical impact - Major system upgrade or replacement

Users/Services Affected:
[Number of users affected, which business services impacted]


Risk Assessment:

Technical Risk:
☐ Low - Well-tested, minimal complexity, easy rollback
☐ Medium - Moderate complexity, standard rollback procedure
☐ High - Complex change, rollback challenging
☐ Critical - Untested configuration, difficult rollback, potential data loss

Security Risk:
☐ No security impact
☐ Security improvement
☐ Potential security impact (requires security review)
☐ Significant security impact (mandatory security approval)

Regulatory/Compliance Risk:
☐ No regulatory impact
☐ Supports compliance
☐ Potential compliance impact (requires compliance review)

Dependencies:
[List any systems, changes, or events this change depends on]


Potential Risks and Mitigation:
[What could go wrong? How will risks be mitigated?]


================================================================================
SECTION 4: IMPLEMENTATION PLAN
================================================================================

Proposed Implementation Date/Time:
Date: [DD.MM.YYYY]
Start Time: [HH:MM TimeZone]
Estimated Duration: [Hours/Minutes]

Implementation Team:
- Lead Implementer: [Name, Role, Contact]
- Backup: [Name, Role, Contact]
- Additional Team Members: [Names, Roles]

Implementation Steps:
[Provide step-by-step procedure]

1. Pre-Implementation Checks
   - [Action]
   - [Action]

2. Implementation
   - [Step 1]
   - [Step 2]
   - [Step N]

3. Verification
   - [Validation step 1]
   - [Validation step 2]

4. Post-Implementation Tasks
   - [Update documentation]
   - [Notify stakeholders]

Maintenance Window Required:
☐ Yes (Service interruption expected)
☐ No (Transparent change)

If Yes, Maintenance Window Details:
- Requested Window: [Date/Time]
- Duration: [Duration]
- Blackout Periods to Avoid: [Dates/times when change should NOT occur]

Testing Approach:
☐ Already tested in DEV/TEST environment (provide results)
☐ Will be tested in DEV/TEST before implementation (provide schedule)
☐ Production-only (justify why testing is not possible)

Testing Results Summary:
[If already tested, summarize results]


================================================================================
SECTION 5: ROLLBACK PLAN
================================================================================

Rollback Decision Criteria:
[Under what conditions should this change be rolled back?]
- [Criterion 1]
- [Criterion 2]

Rollback Procedure:
[Step-by-step instructions to revert to previous state]

1. [Rollback step 1]
2. [Rollback step 2]
3. [Rollback step N]

Rollback Time Estimate: [Duration]

Rollback Decision Authority: [Name/Role who can authorize rollback]

Backup/Snapshot Plan:
☐ Configuration backup taken before change
☐ VM snapshot created before change
☐ Database backup performed before change
☐ Code repository tagged before deployment
☐ Other: _______________

Backup Location: [Path/system where backup is stored]
Backup Verification: ☐ Backup integrity verified before change

================================================================================
SECTION 6: COMMUNICATION PLAN
================================================================================

Stakeholders to Notify:
☐ End users (via email/announcement)
☐ IT support teams
☐ Business owners
☐ Management
☐ External customers
☐ Other: _______________

Pre-Change Communication:
- To Whom: [Recipients]
- Method: [Email/Portal/Announcement]
- Timing: [When before change]
- Message: [Summary of what users need to know]

During-Change Communication:
- Status updates provided to: [Recipients]
- Update frequency: [Interval]
- Escalation contact: [Name, Contact]

Post-Change Communication:
- Success notification to: [Recipients]
- Method: [Email/Portal/Announcement]
- Timing: [When after change]

================================================================================
SECTION 7: CONFIGURATION BASELINE UPDATE
================================================================================

Baseline Documentation Update Required:
☐ Yes
☐ No

If Yes, Describe Updates:
[Which baselines need to be updated and by whom]


CMDB Update Required:
☐ Yes
☐ No

If Yes, Describe Updates:
[Which CIs need to be updated with new configuration details]


================================================================================
SECTION 8: APPROVALS
================================================================================

Technical Review:
Reviewer Name: _______________  Role: _______________
Recommendation: ☐ Approve  ☐ Approve with conditions  ☐ Reject  ☐ Defer
Comments:

Signature: _______________  Date: _______________


Security Review (if security impact):
Reviewer Name: _______________  Role: _______________
Recommendation: ☐ Approve  ☐ Approve with conditions  ☐ Reject  ☐ Defer
Comments:

Signature: _______________  Date: _______________


Change Advisory Board (CAB) Decision:
Decision: ☐ Approved  ☐ Approved with conditions  ☐ Rejected  ☐ Deferred
CAB Chair: _______________
Date: _______________
Conditions (if any):


CAB Member Signatures:
_______________  Date: _______________
_______________  Date: _______________
_______________  Date: _______________

================================================================================
SECTION 9: POST-IMPLEMENTATION REVIEW
================================================================================

Actual Implementation Date/Time: [DD.MM.YYYY HH:MM]
Actual Duration: [Duration]

Implementation Status:
☐ Successful (no issues)
☐ Successful with minor issues (describe below)
☐ Partial failure (describe below)
☐ Failed (rolled back)

Issues Encountered:
[Describe any problems during implementation]


Resolution of Issues:
[How were issues resolved?]


Post-Implementation Validation Results:
☐ All validation tests passed
☐ Some validation tests failed (describe below)

[Validation results summary]


Lessons Learned:
[What went well? What could be improved for future changes?]


Final Sign-Off:
Implementer: _______________  Date: _______________
Change Manager: _______________  Date: _______________

================================================================================
END OF CHANGE REQUEST FORM
================================================================================
```

---

## B.3 Instructions for Completing the Form

### B.3.1 General Guidelines

**Before Submitting**:
- Review ISMS-POL-A.8.9-S2.2 (Change Control Requirements) to understand change classifications
- Consult with Configuration Manager if unsure about classification
- Gather all necessary information before starting the form
- Have CMDB asset IDs ready
- Prepare implementation and rollback plans

**Completeness**:
- Fill in ALL required sections (marked with asterisk if form is electronic)
- Provide sufficient detail for CAB to make informed decision
- Attach supporting documentation as needed (test results, vendor documentation, diagrams)

**Timeliness**:
- Submit change requests at least 5 business days before desired implementation date (for Normal Changes)
- Standard Changes: Follow documented procedure, no advance submission needed
- Emergency Changes: Submit immediately but follow up with complete documentation

### B.3.2 Section-by-Section Guidance

**Section 1: Change Identification**
- Change Request ID: Leave blank if using automated system; otherwise use format CR-YYYY-####
- Change Classification: Critical decision - determines approval workflow
  - **Standard Change**: Pre-approved repeatable changes (reference Standard Change Catalog)
  - **Normal Change**: Everything else requiring CAB approval
  - **Emergency Change**: Only for genuine emergencies (critical incident, security vulnerability)
- Emergency Justification: Be specific - "business wants it done quickly" is NOT an emergency

**Section 2: Change Description**
- Business Justification: Explain in business terms, not technical jargon
- Technical Description: Provide enough detail for implementers to execute
- Configuration Items: List ALL affected assets with CMDB IDs (if available)
- Change Scope: Check all that apply

**Section 3: Impact and Risk Assessment**
- Be realistic about impact and risk - underestimating creates surprises
- Security Risk: When in doubt, mark "Potential security impact" and security team will review
- Dependencies: Include external dependencies (vendor, other teams, scheduled maintenance)
- Mitigation: For each identified risk, describe how it will be mitigated

**Section 4: Implementation Plan**
- Implementation Steps: Should be detailed enough that backup person could execute
- Testing: CAB strongly prefers changes tested in non-production first
- Maintenance Window: Coordinate with Change Manager for scheduling
- Blackout Periods: Be aware of fiscal year-end, major events, holidays

**Section 5: Rollback Plan**
- Decision Criteria: Be specific (e.g., "If application response time exceeds 5 seconds")
- Rollback Procedure: Must be as detailed as implementation procedure
- Backup/Snapshot: Always required - no exceptions
- Backup Verification: Prove the backup is good BEFORE making the change

**Section 6: Communication Plan**
- Consider all stakeholders - internal and external
- Coordinate with Communications team for customer-facing changes
- Provide draft communication messages for review

**Section 7: Configuration Baseline Update**
- If change modifies configuration, baseline documentation must be updated
- Assign responsibility for updates
- Set deadline for documentation updates (within 5 days of change implementation)

**Section 8: Approvals**
- Technical Review: Typically performed by system owner or technical lead
- Security Review: Required if security impact indicated
- CAB Decision: Formal approval by Change Advisory Board

**Section 9: Post-Implementation Review**
- Complete within 2 business days of change implementation
- Honest assessment of what happened
- Lessons learned improve future changes

---

## B.4 Example Completed Form

**[Organization should include a realistic example change request showing a properly completed form]**

Example Scenario: Upgrade firewall firmware from v5.2 to v5.3 to patch security vulnerability
```
[Example would show all sections filled in with realistic data]
```

---

## B.5 Submission Process

**How to Submit**:
1. Complete this form (or equivalent form in change management system)
2. Attach supporting documentation:
   - Test results (if already tested)
   - Vendor documentation
   - Network diagrams or configuration files (if applicable)
   - Risk assessment (if high-risk change)
3. Submit to Configuration Manager via:
   - [Change management system] (preferred)
   - Email to: [email address]
   - Service desk ticket
4. Configuration Manager will:
   - Validate completeness
   - Assign to appropriate reviewers
   - Schedule for CAB review (Normal Changes)
   - Track through approval and implementation

**Timeline**:
- Normal Changes: Submit at least 5 business days before desired implementation
- Emergency Changes: Submit immediately, emergency approval process followed by post-implementation documentation

---

## B.6 Change Status Tracking

**After submission, requesters can track change status**:
- [Change management system dashboard] (if applicable)
- Email notifications at key milestones:
  - Received
  - Under review
  - Approved/rejected/deferred
  - Scheduled
  - Implemented
  - Closed
- Contact Configuration Manager for status inquiries

---

**END OF DOCUMENT**

**Cross-References**:
- ISMS-POL-A.8.9-S2.2: Change Control Requirements
- ISMS-POL-A.8.9-S3: Roles and Responsibilities (CAB composition)
- ISMS-IMP-A.8.9.2: Change Control Assessment Specification

---