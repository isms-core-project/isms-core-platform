# ISMS-POL-A.8.32-S5.A
## Change Management Capability Standards

**Document ID**: ISMS-POL-A.8.32-S5.A  
**Title**: Change Management - Capability Standards (Annex A)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Change Manager / IT Operations | Initial capability standards |

**Review Cycle**: Annual  
**Approvers**: CISO, Change Manager, IT Operations Manager  
**Related Documents**: ISMS-POL-A.8.32-S2.1 (Change Process Requirements)

---

## A.1 Purpose

This annex defines minimum capabilities required from change management systems. Organizations SHALL implement systems (ITSM tools, ticketing systems, workflow platforms) meeting these capability requirements.

**Important:** This document specifies CAPABILITIES, not specific products or vendors. Organizations may use any system(s) meeting these requirements.

---

## A.2 Core Change Management Capabilities

### CAP-001: Change Request Management

**Capability:** System SHALL enable creation and management of change requests.

**Requirements:**
- Create change requests with unique identifiers
- Capture all required fields per ISMS-POL-A.8.32-S5.B (Form Template)
- Support rich text descriptions and file attachments
- Link related changes, incidents, problems
- Tag/categorize changes (by type, affected systems, priority)

**Assessment:** Can users submit complete change requests? Are all required fields captured?

---

### CAP-002: Change State Management

**Capability:** System SHALL track change state through defined lifecycle.

**Required states (minimum):**
- Requested / Draft
- Assessing / Review
- Scheduled / Approved
- Implementing
- Review (PIR)
- Closed
- Rejected
- Cancelled

**Requirements:**
- State transitions tracked with timestamp and user
- State-based workflows (certain actions only available in certain states)
- State history visible in change record

---

### CAP-003: Approval Workflow

**Capability:** System SHALL support configurable approval workflows.

**Requirements:**
- Multi-level approvals (Change Manager, CAB, E-CAB, Management)
- Role-based approval routing
- Approval notifications to approvers
- Approval deadline tracking
- Approval with comments/conditions
- Approval history with approver identity and timestamp
- Email integration for approval notifications

**Assessment:** Can changes be routed to appropriate approvers based on risk/type? Is approval history auditable?

---

### CAP-004: Change Calendar

**Capability:** System SHALL provide change calendar showing scheduled changes.

**Requirements:**
- Calendar view (day/week/month)
- Filter by system, category, risk level
- Identify change conflicts (multiple changes to same system)
- Display freeze periods and blackout windows
- Export calendar data
- Integration with team calendars (optional but recommended)

---

### CAP-005: Audit Trail

**Capability:** System SHALL maintain complete audit trail of all change activities.

**Requirements:**
- Record all changes to change request (what changed, who changed, when)
- State transition history
- Approval/rejection history
- Comment and attachment history
- Audit trail is immutable (write-only, no deletion/modification)
- Audit trail searchable and exportable

**Assessment:** Can you trace complete history of any change? Is audit trail tamper-proof?

---

## A.3 Workflow Automation Capabilities

### CAP-006: Automated Notifications

**Capability:** System SHALL send automated notifications for key events.

**Notification triggers (minimum):**
- Change submitted (notify Change Manager)
- Approval requested (notify approvers)
- Approval granted/rejected (notify requester)
- Change scheduled (notify implementers, stakeholders)
- Implementation starting (notify stakeholders)
- Implementation complete (notify requester, stakeholders)
- PIR required (notify change owner)
- Change closing approaching (notify owner if not closed)

**Notification methods:** Email (required), SMS/chat integration (optional)

---

### CAP-007: Escalation Management

**Capability:** System SHALL support automated escalations for missed deadlines.

**Escalation scenarios:**
- Approval not completed within timeframe
- PIR not completed within timeframe
- Change not closed within timeframe
- Overdue changes

**Escalation actions:**
- Notify escalation contacts
- Change visual indicators (highlight overdue items)
- Management reporting of escalations

---

### CAP-008: Change Classification Support

**Capability:** System SHALL support standard, normal, and emergency change types.

**Requirements:**
- Classify changes by type (Standard/Normal/Emergency)
- Standard change catalog with pre-approved changes
- Different workflow paths per change type
- Risk-based approval routing
- Emergency change fast-track process

---

## A.4 Integration Capabilities

### CAP-009: CMDB Integration

**Capability:** System SHOULD integrate with Configuration Management Database (CMDB).

**Benefits:**
- Auto-populate affected CIs (configuration items)
- Identify dependencies
- Impact assessment support
- Historical change data per CI

**Assessment:** Can change system query CMDB? Are dependencies visible?

---

### CAP-010: Monitoring/Incident Integration

**Capability:** System SHOULD integrate with monitoring and incident management.

**Requirements:**
- Link changes to incidents
- Associate monitoring events with changes
- Change-related incident correlation
- Rollback triggering from incident tickets

---

### CAP-011: API and Data Export

**Capability:** System SHALL provide API or data export capabilities.

**Requirements:**
- Export change data (CSV, JSON, XML)
- API for external integrations
- Reporting data extraction
- Compliance dashboard data feeds

**Use cases:** Custom reporting, compliance dashboards, data analysis, third-party integrations

---

## A.5 Reporting and Analytics Capabilities

### CAP-012: Standard Reports

**Capability:** System SHALL provide standard reports.

**Required reports (minimum):**
- Changes by status
- Changes by type (Standard/Normal/Emergency)
- Changes by risk level
- Failed changes
- Overdue changes
- PIR completion status
- Change volume trends
- Changes by system/category

**Report formats:** On-screen display, PDF export, CSV export

---

### CAP-013: Metrics Dashboard

**Capability:** System SHOULD provide metrics dashboard.

**Key metrics:**
- Change success rate
- Emergency change percentage
- Average change duration
- Failed change percentage
- Approval compliance
- PIR completion rate

**Dashboard features:** Real-time updates, drill-down capability, trend charts

---

### CAP-014: Custom Reporting

**Capability:** System SHOULD support custom report creation.

**Requirements:**
- Report builder interface
- Custom field selection
- Filtering and grouping
- Scheduled report generation
- Report distribution (email, portal)

---

## A.6 Security and Access Control Capabilities

### CAP-015: Role-Based Access Control

**Capability:** System SHALL implement role-based access control (RBAC).

**Required roles (minimum):**
- Change Requester (create/view own changes)
- Change Manager (full access, process administration)
- CAB Member (review/approve changes)
- Change Implementer (update implementation status)
- Read-Only (view changes, reports)

**Permissions:** Create, Read, Update, Delete, Approve per role

---

### CAP-016: Data Protection

**Capability:** System SHALL protect sensitive change data.

**Requirements:**
- Encrypted data in transit (HTTPS/TLS)
- Encrypted data at rest (for cloud/SaaS solutions)
- Access logging (who accessed what when)
- Data retention policies
- Data backup and recovery

---

## A.7 Usability and Accessibility

### CAP-017: User Interface

**Capability:** System SHALL provide intuitive user interface.

**Requirements:**
- Web-based interface (browser access)
- Mobile-responsive design (for mobile approvals)
- Clear navigation and search
- Contextual help and guidance
- Consistent terminology

---

### CAP-018: Self-Service Portal

**Capability:** System SHOULD provide self-service portal for requesters.

**Features:**
- Submit change requests
- Track change status
- View change history
- Standard change catalog (for self-service changes)
- Knowledge base / FAQ

---

## A.8 Scalability and Performance

### CAP-019: Performance Requirements

**Capability:** System SHALL meet performance requirements.

**Requirements:**
- Page load time <3 seconds
- Search results <5 seconds
- Support concurrent users (scale to organization size)
- 99.5% availability (for cloud/SaaS solutions)
- Scheduled maintenance windows communicated in advance

---

### CAP-020: Data Retention

**Capability:** System SHALL support data retention policies.

**Requirements:**
- Retain closed changes per retention policy (typically 3+ years)
- Archive old data without deletion
- Archived data remains searchable and accessible
- Restore archived data if needed
- Purge data after retention period (with audit trail)

---

## A.9 Compliance and Audit Support

### CAP-021: Compliance Reporting

**Capability:** System SHALL support compliance reporting for audits.

**Requirements:**
- Generate compliance reports (changes by status, approvals, testing)
- Evidence export (change tickets, approvals, documentation)
- Audit trail export
- ISO 27001 Control 8.32 compliance mapping

---

### CAP-022: Read-Only Audit Access

**Capability:** System SHALL provide read-only access for auditors.

**Requirements:**
- Auditor role with view-all permissions
- No modification capability
- Audit trail viewing
- Report generation
- Data export

---

## A.10 Implementation Guidance

### A.10.1 Selecting Change Management Systems

**Organizations SHOULD evaluate systems against these capabilities:**

**Critical capabilities (must-have):**
- CAP-001 through CAP-005 (Core capabilities)
- CAP-006, CAP-008 (Workflow and classification)
- CAP-012, CAP-015, CAP-016 (Reporting, security)

**Important capabilities (should-have):**
- CAP-009, CAP-010 (Integrations)
- CAP-013, CAP-014 (Advanced reporting)
- CAP-017, CAP-018 (Usability)

**Nice-to-have capabilities:**
- Advanced analytics
- AI-powered recommendations
- Mobile apps
- Chatbot integration

---

### A.10.2 Gap Assessment

**For existing systems:**
1. Assess current capabilities against requirements
2. Identify capability gaps
3. Prioritize gaps by risk and impact
4. Develop remediation plan (configuration, workarounds, replacement)
5. Implement improvements
6. Reassess quarterly

---

### A.10.3 Configuration

**After system selection:**
- Configure workflows per policy requirements
- Set up approval routing
- Define user roles and permissions
- Configure notifications
- Create standard reports
- Integrate with other systems (CMDB, monitoring, etc.)
- Test workflows before production use
- Train users

---

## A.11 Assessment

**Capability standards assessed in:** ISMS-IMP-A.8.32.1 (Change Process Assessment - Sheet 6: Change Management Tools)

---

**END OF ANNEX A**

*"The tool doesn't do change management. People do change management. The tool just helps them not forget things and provides evidence they actually did it."* 🛠️
