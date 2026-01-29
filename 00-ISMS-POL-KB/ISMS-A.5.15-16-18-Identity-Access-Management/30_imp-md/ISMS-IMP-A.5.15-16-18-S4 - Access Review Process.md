# ISMS-IMP-A.5.15-16-18-S4: Access Review Process
## Implementation Guide for Periodic Access Certification

**Document ID**: ISMS-IMP-A.5.15-16-18-S4  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Security Manager / IAM Manager  
**Status**: Active

---

## Document Purpose

This implementation guide provides **step-by-step procedures** for implementing periodic access reviews (also called access certification or recertification) in accordance with ISO/IEC 27001:2022 Control A.5.18. It covers review planning, execution, remediation, and reporting.

**Target Audience**: Security team, IAM team, managers (reviewers), system owners

**Prerequisites**:
- Access control governance established (IMP-S1)
- User inventory complete (all users documented)
- Access rights matrix available (who has access to what)
- Roles defined (if RBAC implemented - IMP-S3)

---

## 1. Access Review Fundamentals

### 1.1 What is Access Review?

**Access Review Definition**: Periodic verification that users have appropriate access to systems and data.

**Purpose**:
- Detect **excessive access** (users have more access than needed)
- Detect **inappropriate access** (users have access they shouldn't have)
- Detect **orphaned access** (ex-employees still have access)
- Detect **privilege creep** (users accumulated access over time)

**Access Review is NOT**:
- ❌ One-time project
- ❌ IT operations task only
- ❌ Automated process (requires human judgment)

**Access Review IS**:
- ✅ Ongoing process (quarterly/annual cycles)
- ✅ Business owner responsibility (managers certify their teams' access)
- ✅ Accountability mechanism (managers sign off that access is appropriate)

---

### 1.2 Why Access Reviews Matter

**Without Access Reviews**:
- Alice was Sales Rep, promoted to Sales Manager → Still has Sales Rep access (excessive)
- Bob left company 6 months ago → Account still active (orphaned)
- Carol requested temporary project access → Project ended, access remains (forgotten)
- Dave has Admin access to 10 systems → Only uses 2 (excessive)

**With Access Reviews**:
- Manager reviews Alice's access → Removes Sales Rep access, keeps only Manager access ✓
- Monthly orphaned account scan detects Bob → Account disabled ✓
- Quarterly review catches Carol's project access → Removed ✓
- Annual review identifies Dave's excessive access → 8 unnecessary admin rights removed ✓

**Benefits**:
- **Security**: Reduce attack surface (fewer accounts with excessive access)
- **Compliance**: Demonstrate access control effectiveness (FADP, GDPR, FINMA)
- **Efficiency**: Remove unused access (reduce license costs)
- **Accountability**: Managers responsible for their teams' access

---

### 1.3 Access Review Frequency

**Review frequency depends on system criticality and risk**:

| System Criticality | Review Frequency | Examples |
|-------------------|------------------|----------|
| **Critical** | Quarterly | Core banking, payment processing, patient medical records |
| **High** | Semi-annual | CRM, ERP, financial systems, HR systems |
| **Medium** | Annual | Project management, collaboration tools, intranet |
| **Low** | Biennial (every 2 years) | Internal wiki, training portal |

**Regulatory Requirements**:
- **FINMA**: Access reviews required for critical systems (frequency not specified, typically quarterly)
- **GDPR Article 32**: Access reviews demonstrate "ongoing confidentiality, integrity, availability" (annual minimum)
- **ISO 27001:2022 A.5.18**: Reviews at "planned intervals" (organization-defined, typically annual)

---

## 2. Access Review Planning

### 2.1 Define Review Scope

**Objective**: Determine what will be reviewed and how often.

**Step 1: Identify Systems for Review**

**System Inventory** (from system criticality classification):

| System | Criticality | Review Frequency | Users | Reviewer |
|--------|-------------|------------------|-------|----------|
| Finance System | High | Semi-annual | 30 | CFO |
| CRM | High | Semi-annual | 100 | VP Sales |
| HR System | High | Semi-annual | 5 | HR Director |
| Email (Microsoft 365) | Medium | Annual | 500 | IT Manager |
| Intranet | Low | Biennial | 500 | IT Manager |
| File Server | Medium | Annual | 500 | IT Manager |

**Output**: List of systems, review frequency, reviewers

---

**Step 2: Define Review Scope Per System**

**What to Review**:
- ✅ User access (who has access to system?)
- ✅ Access level (Read, Write, Admin - is level appropriate?)
- ✅ Group memberships (is user in appropriate groups?)
- ✅ Last login date (is access being used?)
- ✅ Business justification (why does user have access?)

**What NOT to Review** (out of scope):
- ❌ Technical configuration (firewall rules, system settings)
- ❌ Data quality (accuracy of data in system)
- ❌ User activity logs (that's monitoring, not access review)

---

### 2.2 Identify Reviewers

**Objective**: Assign accountability for access reviews.

**Reviewer Types**:

| Reviewer Type | Responsibility | Example |
|---------------|---------------|---------|
| **Manager** | Review direct reports' access | Sales Manager reviews Sales Reps' CRM access |
| **System Owner** | Review all access to their system | Finance Manager reviews all Finance System access |
| **Security Team** | Review privileged access (admin, root) | Security Analyst reviews all admin access |
| **Internal Audit** | Sample reviews for verification | Auditor spot-checks 10% of reviews |

**Recommendation**: 
- Managers review their direct reports (best knowledge of job responsibilities)
- System owners review sensitive/critical systems (domain expertise)
- Security team reviews privileged access (elevated risk)

---

**Reviewer Assignment Matrix**:

| System | Primary Reviewer | Secondary Reviewer | Review Scope |
|--------|-----------------|-------------------|--------------|
| Finance System | CFO | Finance Manager | All users |
| CRM | VP Sales | Sales Managers | All users (Sales Managers review their teams) |
| HR System | HR Director | - | All users |
| Email | IT Manager | - | Distribution lists, shared mailboxes only |
| IT Systems | IT Manager | Security Manager | All admin access |

**Output**: Reviewer assignment document

---

### 2.3 Create Review Calendar

**Objective**: Schedule reviews throughout the year to avoid bottlenecks.

**Annual Review Calendar Example**:

| Quarter | Month | Systems to Review | Reviewer |
|---------|-------|------------------|----------|
| **Q1** | January | Finance System (H), Payroll System (H) | CFO, Finance Manager |
| | February | CRM (H) | VP Sales, Sales Managers |
| | March | HR System (H) | HR Director |
| **Q2** | April | Email (M), File Server (M) | IT Manager |
| | May | IT Infrastructure (M) | IT Manager, Security Manager |
| | June | Privileged Access (All systems) | Security Manager |
| **Q3** | July | Finance System (H) - Q3 Review | CFO |
| | August | CRM (H) - Q3 Review | VP Sales |
| | September | Project Management Tools (M) | IT Manager |
| **Q4** | October | Collaboration Tools (M) | IT Manager |
| | November | Intranet (L) - Biennial | IT Manager |
| | December | Finance System (H), CRM (H) - Year-end review | CFO, VP Sales |

**Note**: Critical systems reviewed quarterly (Q1, Q3, year-end mini-review)

**Output**: Annual review calendar (published to all reviewers)

---

## 3. Access Review Execution

### 3.1 Prepare Review Data

**Objective**: Extract access data for reviewers to review.

**Step 1: Extract User List**
```sql
-- Example: Extract users with access to Finance System
SELECT 
  user_id, 
  username, 
  full_name, 
  department, 
  job_title,
  manager_name,
  access_level,  -- Read, Write, Admin
  granted_date,
  last_login_date,
  status  -- Active, Disabled
FROM user_access
WHERE system_name = 'Finance System'
  AND status = 'Active'
ORDER BY department, username
```

**Output**: User access list (Excel or CSV)

---

**Step 2: Add Business Context**

Enrich access list with business context (from HR system, access request tickets):
- **Business Justification**: Why user has access (from access request ticket)
- **Access Granted By**: Who approved access
- **Last Access Request Date**: When access was last requested/renewed

**Enriched Access List Example**:

| Username | Full Name | Department | Job Title | Access Level | Granted Date | Business Justification | Last Login | Status |
|----------|-----------|------------|-----------|-------------|--------------|----------------------|------------|--------|
| alice.smith | Alice Smith | Finance | Finance Analyst | Read/Write | 2025-06-01 | Finance analyst role | 2026-01-10 | ✅ Active |
| bob.jones | Bob Jones | Finance | Finance Manager | Admin | 2023-01-15 | Finance manager role | 2026-01-09 | ✅ Active |
| carol.davis | Carol Davis | Sales | Sales Manager | Read | 2024-03-20 | Needs finance reports for sales forecasting | 2025-11-15 | ⚠️ Inactive (60 days) |

---

**Step 3: Flag Items for Review**

Highlight access that requires special attention:
- 🚩 **Inactive users** (no login in 90+ days) - likely no longer needed
- 🚩 **Admin access** (elevated risk) - verify still needed
- 🚩 **Orphaned accounts** (no manager, department = "Unknown") - who owns this?
- 🚩 **Time-bound access past expiration** (temporary access no longer temporary)

---

### 3.2 Conduct Review

**Objective**: Reviewers verify access is appropriate.

**Step 1: Distribute Review Data**

**Review Email Template**:
```
To: alice.manager@company.com
Subject: Action Required: Q1 2026 Access Review - Finance System

Dear Alice,

It's time for the quarterly access review for the Finance System.

**What you need to do**:
1. Review the attached list of users with Finance System access
2. For each user, verify:
   - Is this user still on your team?
   - Does this user still need this access for their job?
   - Is the access level appropriate (Read/Write/Admin)?
3. Mark your decisions:
   - ✅ Confirm (access is appropriate)
   - ❌ Remove (access should be removed)
   - ⚠️ Change (access level should be modified)
4. Return completed review by [Due Date]

**Attached**: Finance_System_Access_Review_Q1_2026.xlsx

**Questions?** Contact security@company.com

Thank you,
Security Team
```

---

**Step 2: Reviewer Completes Review**

**Review Spreadsheet Format**:

| Username | Full Name | Access Level | Last Login | Business Justification | ✅ Confirm | ❌ Remove | ⚠️ Change | Comments |
|----------|-----------|-------------|-----------|----------------------|----------|---------|----------|----------|
| alice.smith | Alice Smith | Read/Write | 2026-01-10 | Finance analyst role | ✅ | | | Access appropriate |
| bob.jones | Bob Jones | Admin | 2026-01-09 | Finance manager role | ✅ | | | Still needs admin |
| carol.davis | Carol Davis | Read | 2025-11-15 | Sales forecasting | | ❌ | | No longer needs access |
| dave.williams | Dave Williams | Admin | 2025-08-01 | Temporary project access | | | ⚠️ Read | Project ended, change to Read |

**Reviewer Actions**:
- **Confirm**: Access is appropriate, no change needed
- **Remove**: Access should be revoked (user no longer needs it)
- **Change**: Access level should be modified (e.g., Admin → Read)
- **Comments**: Explain decision (especially for Remove or Change)

---

**Step 3: Track Review Completion**

**Review Tracking Dashboard**:

| System | Review Period | Reviewer | Due Date | Status | Completion Date | Users Reviewed | Access Confirmed | Access Removed |
|--------|--------------|----------|----------|--------|----------------|---------------|-----------------|---------------|
| Finance System | Q1 2026 | CFO | 2026-01-31 | ✅ Complete | 2026-01-28 | 30 | 27 | 3 |
| CRM | Q1 2026 | VP Sales | 2026-02-15 | ⏳ In Progress | - | 100 | 85 | 5 |
| HR System | Q1 2026 | HR Director | 2026-03-15 | ❌ Overdue | - | 5 | 0 | 0 |

**Escalation**:
- **7 days before due**: Email reminder to reviewer
- **Due date**: Email reminder + manager notification
- **3 days overdue**: Escalate to reviewer's manager
- **7 days overdue**: Escalate to CISO

---

### 3.3 Review Tool Options

**Objective**: Select appropriate tool for access reviews.

**Option 1: Spreadsheet (Excel, Google Sheets)**

**Pros**:
- ✅ Simple, no tool required
- ✅ Works for small-medium orgs (50-200 users)
- ✅ Flexible (easy to customize)

**Cons**:
- ❌ Manual effort (prepare spreadsheet, distribute, collect)
- ❌ Error-prone (reviewer might edit wrong cells)
- ❌ No workflow (no automated reminders, escalations)

**When to Use**: Small org, first access review, limited budget

---

**Option 2: GRC Tool (Sailpoint, Saviynt, One Identity)**

**Pros**:
- ✅ Automated (generate review, distribute, collect responses)
- ✅ Workflow (reminders, escalations, approval chains)
- ✅ Reporting (real-time completion tracking)
- ✅ Scalable (handles 1000+ users)

**Cons**:
- ❌ Expensive ($100-200 per user per year)
- ❌ Implementation effort (3-6 months)
- ❌ Complexity (requires training)

**When to Use**: Large org (200+ users), mature IAM program, budget available

---

**Option 3: ServiceNow (ITSM Platform)**

**Pros**:
- ✅ Workflow automation (if already using ServiceNow)
- ✅ Integration (with ticketing, approvals)
- ✅ Reporting (dashboards)

**Cons**:
- ❌ Configuration effort (custom workflows)
- ❌ Cost (if not already using ServiceNow)

**When to Use**: Already using ServiceNow, want to integrate with ITSM processes

---

**Recommendation**:
- **Start simple**: Spreadsheet for first review
- **Evolve**: GRC tool as IAM program matures

---

## 4. Review Remediation

### 4.1 Process Review Findings

**Objective**: Execute access changes identified in review.

**Step 1: Categorize Findings**

| Finding Type | Action Required | Priority | Example |
|--------------|----------------|----------|---------|
| **Remove Access** | Revoke access immediately | High | User no longer needs access |
| **Change Access Level** | Modify access (Admin → Read) | Medium | User needs less privilege |
| **Justify Exception** | Document reason for retaining access | Low | User has elevated access with justification |
| **No Change** | No action (access confirmed) | - | Access appropriate |

---

**Step 2: Execute Access Removal**

**Process**:
```
Review identifies access to remove
  ↓
Create remediation ticket (ServiceNow, Jira)
  - User: carol.davis
  - System: Finance System
  - Action: Remove access
  - Justification: "No longer needs access per manager review"
  ↓
IT Operations revokes access
  ↓
Verify access removed (test login - should fail)
  ↓
Update review tracking (access removed ✓)
  ↓
Notify user (optional): "Your Finance System access has been removed"
```

**Remediation SLA**: Within 3 business days of review completion

---

**Step 3: Handle Unresponsive Reviewers**

**Problem**: Reviewer doesn't complete review by due date.

**Escalation Process**:

| Days Overdue | Action |
|--------------|--------|
| 0 (Due date) | Email reminder: "Review due today" |
| 1 | Email reminder + manager CC: "Review overdue" |
| 3 | Manager notified: "Your team member has not completed access review" |
| 7 | Escalate to CISO: "Reviewer non-responsive, access review incomplete" |
| 14 | **Automatic action**: Revoke all access for non-reviewed users (extreme measure) |

**Alternative Approach** (less extreme):
- Assume "Confirm" for all users (access retained) if reviewer doesn't respond
- Flag review as "Incomplete" (compliance risk documented)
- Follow up with reviewer post-deadline

---

### 4.2 Exception Handling

**Objective**: Document justifications for retaining access that appears excessive.

**Scenario**: User has Admin access, manager confirms it's needed.

**Exception Documentation**:
- **User**: dave.williams
- **System**: Finance System
- **Access Level**: Admin (elevated)
- **Justification**: "Temporary admin access for system migration project (Jan-Mar 2026). Access will be downgraded to Read after project completion."
- **Review Date**: 2026-04-01 (re-review after project ends)
- **Approved By**: CFO
- **Compensating Controls**: 
  - All admin actions logged
  - Monthly review of admin activity by Security Team

**Exception Register**: Track all justified exceptions, schedule re-review.

---

## 5. Privilege Creep Detection

### 5.1 What is Privilege Creep?

**Privilege Creep Definition**: User accumulates excess access over time.

**Common Causes**:
- User changes roles → Gets new role access → Retains old role access ❌
- User requests temporary access → Access never removed ❌
- User assigned to multiple projects → Access to all project folders remains ❌

**Example**:
- Alice starts as Sales Rep (CRM access)
- Alice promoted to Sales Manager (adds manager-level access)
- Alice later moves to Marketing Manager (adds marketing tools access)
- **Problem**: Alice now has Sales Rep + Sales Manager + Marketing access (excessive)

---

### 5.2 Detect Privilege Creep

**Method 1: Role-Based Detection** (if RBAC implemented)

**Compare**:
- **Current Access**: What access does user have today?
- **Role-Based Access**: What access should user have based on current role?
- **Diff**: Current - Role-Based = Excess access (privilege creep)

**Example**:
- User: Alice Smith
- Current Role: Marketing Manager
- **Should Have** (per role): Marketing tools, email, intranet
- **Actually Has**: Marketing tools, email, intranet, **CRM (Sales)**, **Finance reports (Sales Manager)**
- **Privilege Creep Detected**: CRM, Finance reports (from previous roles)

---

**Method 2: Last Login Analysis**

**Detect**: Access user hasn't used in 90+ days

**Logic**:
```sql
SELECT user_id, system_name, access_level, last_login_date
FROM user_access
WHERE last_login_date < DATE_SUB(NOW(), INTERVAL 90 DAY)
  OR last_login_date IS NULL
```

**Output**: List of unused access (likely privilege creep or forgotten access)

---

**Method 3: Peer Comparison**

**Compare**: User's access vs. peers in same role

**Example**:
- **Sales Reps** (10 users): Average 3 systems accessed (CRM, Sales Portal, Email)
- **Alice Smith** (Sales Rep): 8 systems accessed (CRM, Sales Portal, Email, Finance, HR, IT Admin, Marketing, Intranet)
- **Privilege Creep Detected**: Alice has 5 extra systems (Finance, HR, IT Admin, Marketing, Intranet)

---

### 5.3 Remediate Privilege Creep

**Process**:
```
Privilege creep detected (Alice has excess access)
  ↓
Notify Alice's manager: "Alice has access to 8 systems, peers average 3"
  ↓
Manager reviews: Which access is still needed?
  - CRM: ✅ Needed
  - Sales Portal: ✅ Needed
  - Email: ✅ Needed
  - Finance: ❌ No longer needed (from previous role)
  - HR: ❌ No longer needed (from previous role)
  - IT Admin: ❌ Never needed (error)
  - Marketing: ❌ No longer needed (changed departments)
  - Intranet: ✅ Needed (all employees)
  ↓
Remove excess access (Finance, HR, IT Admin, Marketing)
  ↓
Verify: Alice now has 4 systems (appropriate for Sales Rep)
```

---

## 6. Reporting and Metrics

### 6.1 Review Completion Metrics

**Key Metrics**:

| Metric | Calculation | Target | Current |
|--------|-------------|--------|---------|
| **Review Completion Rate** | (Completed Reviews / Total Reviews) × 100 | >95% | 92% |
| **On-Time Completion** | (Completed on Time / Total Reviews) × 100 | >90% | 87% |
| **Overdue Reviews** | # Reviews past due date | 0 | 2 |
| **Average Time to Complete** | Avg days from start to completion | <7 days | 8.5 days |

---

### 6.2 Access Review Findings

**Key Metrics**:

| Metric | Calculation | Current | Trend |
|--------|-------------|---------|-------|
| **Users Reviewed** | Total users reviewed | 145 | ↑ |
| **Access Confirmed** | # Users with access confirmed as appropriate | 130 (90%) | ↔ |
| **Access Removed** | # Users with access removed | 12 (8%) | ↓ |
| **Access Modified** | # Users with access level changed | 3 (2%) | ↔ |
| **Exceptions Documented** | # Users with justified exceptions | 5 | ↔ |

**Interpretation**:
- **High confirmation rate (90%)**: Good - most access is appropriate
- **Low removal rate (8%)**: Good - minimal excessive access
- **Exceptions documented (5)**: Good - justified exceptions tracked

---

### 6.3 Review Report Template

**Quarterly Access Review Report**:

```markdown
# Q1 2026 Access Review Report

## Executive Summary

- **Review Period**: January 1 - March 31, 2026
- **Systems Reviewed**: 5 (Finance, CRM, HR, Email, File Server)
- **Users Reviewed**: 145
- **Review Completion**: 92% (11 of 12 reviews completed)
- **Key Findings**: 12 users with excessive access identified, 10 remediated

## Review Completion

| System | Reviewer | Due Date | Status | Users Reviewed | Access Removed |
|--------|----------|----------|--------|---------------|---------------|
| Finance System | CFO | 2026-01-31 | ✅ Complete | 30 | 3 |
| CRM | VP Sales | 2026-02-15 | ✅ Complete | 100 | 5 |
| HR System | HR Director | 2026-03-15 | ✅ Complete | 5 | 0 |
| Email | IT Manager | 2026-03-30 | ✅ Complete | 500 | 0 (DLs only) |
| File Server | IT Manager | 2026-03-30 | ❌ Incomplete | - | - |

## Findings

### Access Removed (12 users)
- **Reason**: No longer need access (10 users)
- **Reason**: User left company (2 users - orphaned accounts)

### Access Modified (3 users)
- Downgraded Admin → Read (privilege creep)

### Exceptions Documented (5 users)
- Elevated access justified with compensating controls

## Privilege Creep Detected

- 8 users identified with access from previous roles
- 7 users remediated (access removed)
- 1 user access justified (exception documented)

## Recommendations

1. **Automate orphaned account detection** (2 orphaned accounts found manually - should be detected automatically)
2. **Implement role-based access reviews** (easier to review role than individual users)
3. **Quarterly privilege creep scans** (detect excessive access proactively)

## Next Review

- **Q2 2026**: Finance System (quarterly), IT Infrastructure (semi-annual)
- **Due**: June 30, 2026
```

---

## 7. Continuous Improvement

### 7.1 Review Process Optimization

**Objective**: Make reviews easier and more effective over time.

**Optimization Opportunities**:

1. **Pre-populate Review Data**
   - Current: Reviewer starts with blank spreadsheet
   - Improved: Pre-populate with last review decisions ("Confirm" from last time = likely "Confirm" this time)
   - Benefit: Reviewer only reviews changes (new users, changed access)

2. **Role-Based Reviews**
   - Current: Review individual users
   - Improved: Review role definitions → All users in role inherit review decision
   - Benefit: Review 10 roles instead of 100 users

3. **Risk-Based Review Frequency**
   - Current: All systems reviewed annually
   - Improved: Critical systems quarterly, high semi-annual, medium annual, low biennial
   - Benefit: Focus effort on high-risk systems

4. **Automated Privilege Creep Detection**
   - Current: Manual comparison of user access vs. role
   - Improved: Automated script flags excessive access weekly
   - Benefit: Proactive detection, not reactive (wait for annual review)

---

### 7.2 Reviewer Training

**Objective**: Train reviewers to conduct effective access reviews.

**Training Topics**:
- **Why access reviews matter** (security, compliance, accountability)
- **How to conduct review** (confirm vs. remove vs. change)
- **What to look for** (red flags: inactive users, admin access, orphaned accounts)
- **How to document exceptions** (justification + compensating controls)
- **What happens after review** (remediation, reporting)

**Training Format**:
- 30-minute session (annual, before review season)
- Hands-on exercise (review sample access list)
- Q&A

---

### 7.3 Access Review Metrics Dashboard

**Real-Time Dashboard** (for Security Team, CISO):

```
================================================================================
ACCESS REVIEW DASHBOARD - 2026
================================================================================

COMPLETION STATUS
- Reviews Due This Quarter: 5
- Reviews Completed: 4 (80%)
- Reviews In Progress: 1 (20%)
- Reviews Overdue: 0 ✓

FINDINGS (YTD)
- Users Reviewed: 245
- Access Confirmed: 220 (90%)
- Access Removed: 20 (8%)
- Access Modified: 5 (2%)
- Privilege Creep Detected: 15 users

UPCOMING REVIEWS
- Q2 2026: Finance System (due Jun 30)
- Q2 2026: IT Infrastructure (due Jun 30)

ALERTS
- ⚠️ File Server review incomplete (IT Manager unresponsive)
- ⚠️ 2 orphaned accounts detected (not caught by review - automation needed)
================================================================================
```

---

## 8. Common Pitfalls and Solutions

### 8.1 Pitfall: Reviewer Fatigue

**Problem**: Reviewing 500 users is overwhelming, reviewer gives up or rubber-stamps all access as "Confirm"

**Solution**:
- ✅ Break review into smaller chunks (review 50 users per week, not 500 at once)
- ✅ Pre-filter obvious "Confirm" cases (active users, recently reviewed, standard access)
- ✅ Focus reviewer attention on high-risk access (admin, privileged, inactive users)
- ✅ Role-based reviews (review role definition, not 100 individual users in role)

---

### 8.2 Pitfall: No Accountability

**Problem**: Reviewer rubber-stamps all access as "Confirm" without actually reviewing

**Solution**:
- ✅ Require reviewer sign-off (accountability)
- ✅ Audit sample of reviews (spot-check 10% for accuracy)
- ✅ Consequences for non-compliance (escalate to CISO, performance review impact)
- ✅ Educate on importance (security risk, compliance requirement)

---

### 8.3 Pitfall: Review Findings Not Remediated

**Problem**: Access review complete, excess access identified, but IT never removes access

**Solution**:
- ✅ Automated remediation tickets (review → ticket → IT operations)
- ✅ SLA for remediation (within 3 business days)
- ✅ Track remediation completion (% findings remediated)
- ✅ Escalate overdue remediations (after 7 days, escalate to IT manager)

---

## 9. Success Criteria

**How to Know Access Reviews are Working**:

✅ **Process Established**:
- Review calendar published (all systems, reviewers, frequencies)
- Reviewers trained (understand responsibilities)
- Review tool/process documented

✅ **Operational Excellence**:
- Review completion rate >95%
- Reviews completed on time (>90% on-time)
- Average time to complete <7 days

✅ **Effectiveness**:
- Access removed (8-15% of reviewed access removed as excessive)
- Privilege creep detected and remediated (quarterly scans)
- Orphaned accounts identified (0 orphaned accounts after review)

✅ **Compliance**:
- Audit-ready evidence (review documentation, sign-offs, remediation tracking)
- No open audit findings on access reviews
- Regulatory compliance demonstrated (FINMA, GDPR requirements met)

---

## 10. Next Steps

### 10.1 After Implementing Access Reviews

1. ✅ **Access review process established** (this implementation guide completed)
   
2. ➡️ **Next**: Implement IAM assessment (IMP-S5)
   - Generate access review workbook (track completion, findings)
   - Measure review effectiveness (completion rate, remediation rate)
   - Present dashboard to CISO
   
3. ➡️ **Then**: Generate assessment scripts
   - Script 3: Access Review Results workbook
   - Script 6: IAM Dashboard (consolidate all assessments)

---

## Document Approval

**Prepared By**: [Name], [Title] - [Date]  
**Reviewed By**: [Name], [Title] - [Date]  
**Approved By**: [Name], CISO - [Date]

**Next Review Date**: [Date + 12 months]

**Version History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial implementation guide for access reviews |

---

**END OF IMPLEMENTATION GUIDE S4 - ACCESS REVIEW PROCESS**

**Next Document**: ISMS-IMP-A.5.15-16-18-S5_IAM_Assessment_Procedures.md