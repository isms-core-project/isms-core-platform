**ISMS-IMP-A.8.31.2 - Environment Access Control Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.31: Separation of Development, Test and Production Environments

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.31.2 |
| **Version** | 1.0 |
| **Assessment Area** | Environment Access Control & Production Access Restrictions |
| **Related Policy** | ISMS-POL-A.8.31, Section 2.2 (Environment Access Control Requirements) |
| **Purpose** | Document access control implementation, verify production access restrictions (zero developer access), and assess compliance with environment-specific access requirements |
| **Target Audience** | IAM Administrators, IT Operations, Security Engineers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Access Control Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Environment Access Control assessment workbook | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Cell Styling Reference
  - Integration Points


---

# PART I: USER COMPLETION GUIDE

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.31.2 - Environment Access Control Assessment

#### What This Assessment Covers

This assessment documents the ACCESS CONTROL MECHANISMS for your environments and verifies **CRITICAL PRODUCTION ACCESS RESTRICTIONS**. This is the "WHO can access WHAT?" assessment that answers:

- Who has access to which environments? (user → environment matrix)
- Do developers have production access? (SHOULD BE ZERO except break-glass)
- Is production access restricted to operations team only?
- Are access controls enforced via IAM/RBAC?
- Is MFA required for production access?
- Are break-glass emergency access procedures documented and monitored?
- What gaps exist between access control implementation and policy requirements?


#### Key Principle

This assessment is **completely technology-agnostic and platform-independent**. You document YOUR specific access control system (whether Active Directory, AWS IAM, Azure RBAC, GCP IAM, Kubernetes RBAC, or on-premises), and verify access restrictions against generic policy requirements.

#### Critical Compliance Requirement

**ZERO DEVELOPER ACCESS TO PRODUCTION** (except via documented break-glass procedure)

This is a MANDATORY requirement. Developers having routine production access = MAJOR AUDIT FINDING.

#### What You'll Document

- User → environment access matrix (who can access what)
- Role-based access control (RBAC) per environment
- Production access restrictions (operations-only)
- Developer production access (SHOULD BE ZERO)
- MFA enforcement for production
- Break-glass emergency access procedures
- Access monitoring and audit logging
- Access control gaps and remediation plans
- Supporting evidence for audit


#### How This Relates to Other A.8.31 Assessments

| Assessment            | Focus                      | Relationship to A.8.31.2                |
|-----------------------|----------------------------|-----------------------------------------|
| ISMS-IMP-A.8.31.1     | Architecture Separation    | WHAT environments exist (input required) |
| **ISMS-IMP-A.8.31.2** | **Access Control**         | **WHO can access WHICH environment**    |
| ISMS-IMP-A.8.31.3     | Compliance Dashboard       | Consolidated view across architecture + access |

This assessment (A.8.31.2) requires A.8.31.1 to be completed first - you need the environment list from A.8.31.1 to build the access matrix.

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **IAM Administrators** - Access control policies, user provisioning
2. **IT Operations** - Production access management
3. **Security Engineers** - Access monitoring, compliance verification
4. **Identity Management** - User lifecycle, group membership
5. **Compliance Officers** - Policy enforcement, audit requirements
6. **HR/People Operations** - Joiner/mover/leaver processes

#### Required Skills

- Understanding of access control concepts (RBAC, least privilege, separation of duties)
- Familiarity with deployed IAM system (Active Directory, AWS IAM, Entra ID, etc.)
- Knowledge of user provisioning and de-provisioning procedures
- Understanding of production access restrictions
- Access to IAM admin consoles/tools


#### Time Commitment

- **Initial assessment:** 6-10 hours (for comprehensive access review)
- **Quarterly updates:** 2-3 hours (update user lists, verify access changes)


### Expected Outputs

Upon completion, you will have:

1. ✅ **Complete user inventory** - All users with environment access documented
2. ✅ **User → environment access matrix** - Who can access which environments
3. ✅ **Role-based access control (RBAC) documentation** - Roles and permissions per environment
4. ✅ **Production access verification** - Confirmed zero developer access (except break-glass)
5. ✅ **MFA enforcement verification** - Production access requires MFA
6. ✅ **Break-glass procedure documentation** - Emergency access tracked and monitored
7. ✅ **Access monitoring compliance** - Audit logging enabled and reviewed
8. ✅ **Access control gap analysis** - Identified violations with remediation plans
9. ✅ **Evidence register** - Supporting documentation for audit
10. ✅ **Approved assessment** - Multi-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. IAM System Access

- Administrator access to IAM system (Active Directory, AWS IAM, Entra ID, GCP IAM)
- Access to user provisioning tools
- Access to group membership data
- Access to role assignment data
- Access to audit logs (access attempts, permission changes)


#### 2. User Data

- Complete user inventory (all users with any environment access)
- User → group/role assignments
- User job titles and roles (developer, operations, QA, etc.)
- Joiners/movers/leavers data (recent access changes)


#### 3. Access Control Documentation

- IAM policies/RBAC role definitions
- Group membership lists
- Production access procedures
- Break-glass emergency access procedures
- MFA enforcement policies


#### 4. Environment Data (from A.8.31.1)

- Environment inventory (dev, test, staging, production)
- Environment names and purpose
- Required for building access matrix


#### 5. Policy Requirements

- ISMS-POL-A.8.31, Section 2.2 (Environment Access Control Requirements)
- ISMS-POL-A.8.31, Section 2.5 (Production Support Requirements)
- ISMS-POL-00 (Regulatory Applicability Framework)


### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Access to IAM admin console
- PowerShell/AWS CLI/Azure CLI/gcloud (for access data export)
- Audit log analysis tools
- Screen capture tools (for evidence screenshots)


### Dependencies

**CRITICAL DEPENDENCY**: ISMS-IMP-A.8.31.1 (Environment Architecture Assessment) MUST be completed first.

**Why**: You need the environment list from A.8.31.1 to build the user → environment access matrix in this assessment.

**Output from A.8.31.1 required**:

- Sheet 2: Environment_Inventory (environment names)


**Outputs to A.8.31.3**:

- Access control gaps (for consolidated compliance dashboard)
- Production access violations (critical findings)


---

## Workflow

### High-Level Process

```
1. PREPARE (verify A.8.31.1 complete)
   ↓
2. INVENTORY USERS (Sheet 1)
   ↓
3. BUILD ACCESS MATRIX (Sheet 2)
   ↓
4. VERIFY PRODUCTION ACCESS (Sheet 3)
   ↓
5. VERIFY MFA ENFORCEMENT (Sheet 4)
   ↓
6. DOCUMENT BREAK-GLASS (Sheet 5)
   ↓
7. VERIFY ACCESS MONITORING (Sheet 6)
   ↓
8. IDENTIFY GAPS (Sheet 7)
   ↓
9. COLLECT EVIDENCE (Sheet 8)
   ↓
10. REVIEW & APPROVE
   ↓
11. MAINTAIN & UPDATE
```

### Detailed Workflow

#### Phase 1: Preparation (30 minutes)

**Activities:**

- Verify A.8.31.1 (Environment Architecture) is complete
- Export environment list from A.8.31.1, Sheet 2
- Gather all prerequisite information
- Obtain IAM admin access
- Review policy requirements


**Outputs:**

- Environment list ready
- Assessment team identified
- IAM access obtained
- Timeline established


#### Phase 2: User Inventory (1-2 hours)

**Activities:**

- Complete Sheet 1: User Inventory
- Export all users with any environment access
- Document user roles (developer, operations, QA, etc.)
- Document user status (active, inactive, terminated)


**Outputs:**

- Complete user inventory
- User roles documented
- Active/inactive status tracked


**Common Pitfalls to Avoid:**

- ❌ Missing former employees (terminated users with lingering access)
- ❌ Service accounts not documented (non-human identities)
- ❌ Contractor accounts not tracked separately


#### Phase 3: Access Matrix Build (2-3 hours)

**Activities:**

- Complete Sheet 2: User → Environment Access Matrix
- For each user, document access to each environment
- Verify access via IAM system (don't assume)
- Document access level (read-only, read-write, admin)


**Outputs:**

- Comprehensive access matrix
- User → environment relationships documented
- Access levels verified


**Common Pitfalls to Avoid:**

- ❌ Assuming access based on job title (verify actual permissions)
- ❌ Missing inherited group access (check group memberships)
- ❌ Not documenting service account access


#### Phase 4: Production Access Verification (1-2 hours) - CRITICAL

**Activities:**

- Complete Sheet 3: Production Access Verification
- List ALL users with production access
- Verify each user is operations/support role (NOT developer)
- **CRITICAL CHECK**: Count developers with production access (SHOULD BE ZERO)
- Document any developer production access as VIOLATION


**Outputs:**

- Production access user list
- Developer production access count (TARGET: 0)
- Violations documented


**Common Pitfalls to Avoid:**

- ❌ Developers with "read-only" production access (STILL VIOLATION - should be zero access)
- ❌ Former developers now in operations (verify actual job title)
- ❌ "Senior developers" with production access (STILL VIOLATION unless they're now operations)


**CRITICAL FINDING**: If ANY developers have production access (except break-glass), this is a MAJOR AUDIT FINDING requiring immediate remediation.

#### Phase 5: MFA Enforcement Verification (1 hour)

**Activities:**

- Complete Sheet 4: MFA Enforcement
- Verify MFA required for ALL production access
- Document MFA enrollment status per user
- Verify MFA cannot be bypassed


**Outputs:**

- MFA enforcement status
- User MFA enrollment verification
- MFA bypass check complete


**Common Pitfalls to Avoid:**

- ❌ MFA optional, not mandatory (VIOLATION)
- ❌ Service accounts exempt from MFA (acceptable if documented)
- ❌ MFA bypass procedures undocumented


#### Phase 6: Break-Glass Documentation (1-2 hours)

**Activities:**

- Complete Sheet 5: Break-Glass Emergency Access
- Document break-glass procedures
- Verify break-glass accounts tracked
- Review recent break-glass usage (if any)
- Verify post-incident review process


**Outputs:**

- Break-glass procedure documentation
- Break-glass account inventory
- Usage log (historical)
- Post-incident review verification


**Common Pitfalls to Avoid:**

- ❌ Break-glass accounts used routinely (should be emergency-only)
- ❌ No audit trail of break-glass usage
- ❌ Break-glass accounts without time limits (access should expire)


#### Phase 7: Access Monitoring Verification (1-2 hours)

**Activities:**

- Complete Sheet 6: Access Monitoring & Audit Logging
- Verify audit logging enabled for all environments
- Verify access attempts logged (successful and failed)
- Verify unauthorized access attempts monitored and alerted
- Document access review frequency


**Outputs:**

- Audit logging status per environment
- Access monitoring procedures documented
- Alert configuration verified


**Common Pitfalls to Avoid:**

- ❌ Audit logs not retained (e.g., only 7 days - need 90+ days)
- ❌ Logs not monitored (collection without review is useless)
- ❌ No alerts for unauthorized access attempts


#### Phase 8: Gap Analysis (1-2 hours)

**Activities:**

- Complete Sheet 7: Gap Analysis
- Review all previous sheets for non-compliance
- Document each gap with severity rating
- **CRITICAL**: Developer production access = High severity
- Propose remediation for each gap
- Estimate remediation effort and timeline


**Outputs:**

- Comprehensive gap analysis
- Risk-prioritized remediation plan
- Timeline for gap closure


#### Phase 9: Evidence Collection (1-2 hours)

**Activities:**

- Complete Sheet 8: Evidence Register
- Export IAM policy configurations
- Screenshot access control configurations
- Export user → group/role assignments
- Export audit logs (production access)
- Document access review records


**Outputs:**

- Complete evidence package
- Audit-ready documentation


#### Phase 10: Review & Approval (variable)

**Activities:**

- Internal team review
- IAM Administrator approval
- Security Team approval
- CISO approval


**Outputs:**

- Approved assessment
- Action items assigned


#### Phase 11: Maintenance (ongoing)

**Activities:**

- Quarterly assessment updates
- Update after joiner/mover/leaver events
- Track gap remediation progress
- Monitor continuous compliance


**Outputs:**

- Up-to-date assessment
- Compliance trend analysis


---

## Completing Each Sheet

### Sheet 1: Instructions & Legend

**What to do:**
1. Fill in assessment metadata (date, completed by, organization)
2. Review the status legend
3. Review acceptable evidence examples
4. Understand the workflow

**Time:** 5-10 minutes

**Tips:**

- Use current date for "Assessment Date"
- Include your name and role for "Completed By"
- Read the full instructions before starting


---

### Sheet 2: User Inventory

**What to do:**
1. List every user with access to ANY environment
2. For each user, document:

   - User ID / username
   - Full name
   - Job title / role (developer, operations, QA, etc.)
   - Department
   - Status (active, inactive, terminated)
   - Account type (human, service account)


**Time:** 1-2 hours

**Tips:**

- Export complete user list from IAM system (don't manually type)
- Include service accounts (non-human identities)
- Mark terminated users (they should have zero access)
- Verify status against HR records


**Example Entry:**
| User ID | Full Name | Job Title | Department | Status | Account Type |
|---------|-----------|-----------|------------|--------|--------------|
| jdoe | John Doe | Senior Developer | Engineering | Active | Human |
| jsmith | Jane Smith | Operations Engineer | IT Operations | Active | Human |
| svc_backup | Backup Service | Service Account | IT Operations | Active | Service Account |
| bjones | Bob Jones | Developer | Engineering | Terminated (2023-12-15) | Human |

**CRITICAL CHECK**: Terminated users should have ZERO access (verify in access matrix)

---

### Sheet 3: User → Environment Access Matrix

**What to do:**
1. For each user (from Sheet 2), document access to each environment
2. Use environment list from A.8.31.1, Sheet 2 (Environment Inventory)
3. For each user + environment combination, document:

   - Access granted? (Yes / No)
   - Access level (None, Read-Only, Read-Write, Admin)
   - Access method (IAM role, AD group, RBAC, etc.)
   - Last verified date


**Time:** 2-3 hours

**Tips:**

- Export access data from IAM system (don't guess)
- Verify inherited group access (user may not have direct access but has it via group)
- Check for orphaned access (old permissions not removed)
- Use conditional formatting to highlight production access


**Example Entry:**
| User ID | Development | Testing | Staging | Production | Production Access? |
|---------|-------------|---------|---------|------------|-------------------|
| jdoe (Developer) | Admin | Read-Write | Read-Only | ❌ None | ✅ Correct (no access) |
| jsmith (Operations) | Read-Only | Read-Only | Admin | Admin (via PAM) | ✅ Correct (operations role) |
| bjones (Terminated) | ❌ VIOLATION: Still has Read-Write | ❌ VIOLATION: Still has Read-Only | ❌ None | ❌ None | ❌ VIOLATION (access not removed) |

**CRITICAL COLUMNS**:

- **Production column**: Only operations/support should have access
- **Production Access? column**: Flags any non-operations access


---

### Sheet 4: Production Access Verification

**What to do:**
1. List ALL users with production access (from access matrix)
2. For each user, document:

   - User ID
   - Job title / role
   - Is role operations/support? (Yes / No)
   - If No → VIOLATION
   - Access justification
   - Approval record


**Time:** 1-2 hours (CRITICAL ASSESSMENT)

**Tips:**

- This is the MOST CRITICAL sheet in the assessment
- Count developers with production access (target: ZERO)
- "Read-only" production access for developers = STILL VIOLATION
- "Senior developers" with production access = STILL VIOLATION
- Break-glass access documented separately (Sheet 5)


**Example Entry:**
| User ID | Full Name | Job Title | Operations/Support Role? | Production Access Justified? | Compliance | Evidence |
|---------|-----------|-----------|-------------------------|------------------------------|------------|----------|
| jsmith | Jane Smith | Operations Engineer | ✅ Yes | ✅ Yes (operational necessity) | ✅ Compliant | iam-policy-ops-team.json |
| svc_monitoring | Monitoring Service | Service Account (Monitoring) | ✅ Yes | ✅ Yes (read-only monitoring) | ✅ Compliant | iam-policy-monitoring.json |
| jdoe | John Doe | Senior Developer | ❌ No | ❌ No | ❌ MAJOR VIOLATION | FINDING: Developer has production access |

**CRITICAL METRICS**:

- **Target**: ZERO developers with production access
- **Actual**: [Count from this sheet]
- **If > 0**: MAJOR AUDIT FINDING


---

### Sheet 5: MFA Enforcement

**What to do:**
1. Document MFA enforcement policy
2. List all users with production access (from Sheet 4)
3. For each user, verify:

   - MFA enrolled? (Yes / No)
   - MFA required? (Yes / No / Optional)
   - MFA device type (Authenticator app, hardware token, SMS)
   - MFA cannot be bypassed? (Verified)


**Time:** 1 hour

**Tips:**

- MFA should be MANDATORY for production, not optional
- Service accounts may use alternative auth (API keys, certificates)
- Document MFA enrollment from IAM system
- Test MFA bypass (should fail)


**Example Entry:**
| User ID | Production Access | MFA Enrolled? | MFA Required? | MFA Device | MFA Bypass Possible? | Compliance |
|---------|-------------------|---------------|---------------|------------|---------------------|------------|
| jsmith | ✅ Yes (Admin) | ✅ Yes | ✅ Required (mandatory) | Authenticator app | ❌ No (verified) | ✅ Compliant |
| svc_monitoring | ✅ Yes (Read-Only) | N/A (service account) | N/A (API key auth) | API key (rotated monthly) | N/A | ✅ Compliant |

**CRITICAL VIOLATIONS**:

- ❌ MFA optional, not mandatory (production access without MFA)
- ❌ MFA bypass allowed (emergency access not documented)


---

### Sheet 6: Break-Glass Emergency Access

**What to do:**
1. Document break-glass procedure
2. List break-glass accounts
3. For each break-glass account:

   - Account purpose
   - Who can activate? (authorized approvers)
   - Time limit (how long access granted)
   - Monitoring (how usage tracked)
   - Post-incident review process

4. Document recent break-glass usage (last 90 days)

**Time:** 1-2 hours

**Tips:**

- Break-glass should be emergency-only (not routine)
- Usage should be rare (monthly usage = something wrong)
- Post-incident review mandatory
- Time-limited access (hours, not days)


**Example Entry:**
| Break-Glass Account | Purpose | Activation Approval | Time Limit | Last Used | Post-Incident Review? | Compliance |
|---------------------|---------|---------------------|------------|-----------|----------------------|------------|
| breakglass-dev-001 | Emergency production fix | CISO + IT Operations Manager | 4 hours (auto-revoke) | 2024-01-10 (critical bug fix) | ✅ Yes (completed 2024-01-12) | ✅ Compliant |

**RECENT USAGE LOG** (last 90 days):
| Date | User | Duration | Purpose | Incident Ticket | Post-Review Completed? |
|------|------|----------|---------|----------------|----------------------|
| 2024-01-10 | dev_user1 (via breakglass-dev-001) | 2 hours | Critical production bug fix | INC-2024-001 | ✅ Yes |

**CRITICAL VIOLATIONS**:

- ❌ Break-glass used routinely (weekly/monthly usage)
- ❌ No post-incident review
- ❌ Break-glass access not time-limited


---

### Sheet 7: Access Monitoring & Audit Logging

**What to do:**
1. Document audit logging configuration per environment
2. Verify:

   - Audit logging enabled? (Yes / No)
   - What events logged? (login, permission changes, access attempts)
   - Log retention period (days)
   - Logs monitored? (Yes / No)
   - Alerts configured? (unauthorized access attempts)
   - Access review frequency (weekly, monthly, quarterly)


**Time:** 1-2 hours

**Tips:**

- Audit logs must be enabled for production (MANDATORY)
- Retention period: minimum 90 days (regulatory requirement may be longer)
- Logs without monitoring = compliance checkbox (not security)
- Unauthorized access attempts should trigger alerts


**Example Entry:**
| Environment | Logging Enabled? | Events Logged | Retention | Monitored? | Alerts | Access Review Frequency | Compliance |
|-------------|------------------|---------------|-----------|------------|--------|------------------------|------------|
| Production | ✅ Yes | Login, permission changes, resource access, failed attempts | 365 days | ✅ Yes (SIEM) | ✅ Yes (failed access → alert) | Weekly (Operations Manager) | ✅ Compliant |
| Staging | ✅ Yes | Login, permission changes | 90 days | ⚠️ Partial (manual review) | ❌ No | Monthly | ⚠️ Partial |
| Testing | ✅ Yes | Login attempts only | 30 days | ❌ No | ❌ No | Quarterly | ⚠️ Partial |
| Development | ⚠️ Partial (login only) | Login attempts only | 7 days | ❌ No | ❌ No | None | ❌ Non-Compliant |

**CRITICAL REQUIREMENTS** (Production):

- ✅ Logging enabled
- ✅ Retention ≥ 90 days
- ✅ Monitored regularly
- ✅ Alerts for unauthorized access


---

### Sheet 8: Gap Analysis

**What to do:**
1. Review all previous sheets
2. Identify any non-compliance with policy requirements
3. Document each gap with:

   - Description of gap
   - Policy requirement violated
   - Risk severity (High/Medium/Low)
   - Proposed remediation
   - Estimated effort
   - Target completion date

4. Prioritize gaps by risk severity

**Time:** 1-2 hours

**Tips:**

- Be honest about gaps (audit will find them anyway)
- Developer production access = HIGH severity (immediate remediation)
- Prioritize High severity gaps first
- Include compensating controls if remediation delayed


**Example Entry:**
| Gap ID | Description | Policy Violated | Severity | Remediation | Effort | Target Date | Owner |
|--------|-------------|-----------------|----------|-------------|--------|-------------|-------|
| GAP-001 | 3 developers have production access (read-only) | ISMS-POL-A.8.31, Section 2.2 | 🔴 High | Revoke production access, provide read-only staging access instead | 4 hours | 2024-01-30 | IAM Admin |
| GAP-002 | Terminated user (bjones) still has dev/test access | ISMS-POL-A.8.31, Section 2.2 | 🔴 High | Disable account immediately, review offboarding process | 1 hour | 2024-01-25 | IAM Admin |
| GAP-003 | MFA optional for production access (not mandatory) | ISMS-POL-A.8.31, Section 2.2 | 🔴 High | Enforce MFA policy (make mandatory), enroll all operations users | 8 hours | 2024-02-15 | Security Eng |
| GAP-004 | Break-glass used 12 times last quarter (excessive) | ISMS-POL-A.8.31, Section 2.5 | 🟡 Medium | Review break-glass usage, implement read-only production access for troubleshooting | 16 hours | 2024-03-31 | DevOps Lead |
| GAP-005 | Development environment audit logs only retained 7 days | ISMS-POL-A.8.31, Section 2.2 | 🟢 Low | Increase retention to 90 days | 2 hours | 2024-04-30 | Security Eng |

---

### Sheet 9: Evidence Register

**What to do:**
1. Document all supporting evidence
2. For each evidence item, record:

   - Evidence type (IAM export, screenshot, audit log, etc.)
   - Description
   - File name/location
   - Date collected
   - Related requirement

3. Attach evidence files or provide accessible links

**Time:** 1-2 hours

**Tips:**

- Export IAM policies/RBAC configurations
- Screenshot access control settings
- Export user → group/role assignments
- Export audit logs (production access attempts)
- Document access review records


**Example Entry:**
| Evidence ID | Type | Description | File Name | Date | Related Requirement | Sheet | Location |
|-------------|------|-------------|-----------|------|---------------------|-------|----------|
| EVD-001 | IAM Export | AWS IAM policy showing production role restrictions | aws-iam-prod-policy-2024-01.json | 2024-01-20 | ISMS-POL-A.8.31, Section 2.2 | Sheet 3, 4 | ./evidence/EVD-001/ |
| EVD-002 | User Export | Complete user list with group memberships | ad-users-groups-2024-01.csv | 2024-01-20 | ISMS-POL-A.8.31, Section 2.2 | Sheet 2, 3 | ./evidence/EVD-002/ |
| EVD-003 | Screenshot | MFA enforcement policy configuration | mfa-policy-screenshot-2024-01.png | 2024-01-21 | ISMS-POL-A.8.31, Section 2.2 | Sheet 5 | ./evidence/EVD-003/ |
| EVD-004 | Audit Log | Production access audit log (last 90 days) | prod-access-log-2024-01.csv | 2024-01-21 | ISMS-POL-A.8.31, Section 2.2 | Sheet 7 | ./evidence/EVD-004/ |
| EVD-005 | Procedure Doc | Break-glass emergency access procedure | breakglass-procedure-v1.2.pdf | 2024-01-22 | ISMS-POL-A.8.31, Section 2.5 | Sheet 6 | ./evidence/EVD-005/ |

---

## Evidence Collection

### Required Evidence Types

| Requirement Area | Evidence Type | Examples | How to Collect |
|------------------|---------------|----------|----------------|
| **User Inventory** | User list export | AD users, IAM users, Entra ID users | `Get-ADUser`, `aws iam list-users`, `az ad user list` |
| **Access Matrix** | Access assignment export | IAM policies, RBAC roles, AD group memberships | `aws iam list-attached-user-policies`, `az role assignment list` |
| **Production Access** | IAM policy configurations | Production role policies, AD group memberships | Export production IAM policies, AD group members |
| **MFA Enforcement** | MFA enrollment status | User MFA devices, conditional access policies | `aws iam list-mfa-devices`, Azure Conditional Access export |
| **Break-Glass** | Break-glass procedure document | Emergency access workflow, approval forms | Document repository, incident management system |
| **Audit Logging** | Log configuration + samples | CloudTrail, Azure Monitor, AD audit logs | `aws cloudtrail describe-trails`, Azure Monitor config |

### Evidence Collection Commands

**AWS IAM:**
```bash
# Export all users
aws iam list-users --output json > aws-users-2024-01.json

# Export production role policy
aws iam get-role-policy --role-name ProdOpsAccess --policy-name ProdAccess --output json > prod-policy-2024-01.json

# Export user MFA devices
aws iam list-mfa-devices --user-name ops-user1 > mfa-devices-2024-01.json

# Export CloudTrail configuration
aws cloudtrail describe-trails > cloudtrail-config-2024-01.json
```

**Entra ID:**
```bash
# Export all users
az ad user list --output table > azure-users-2024-01.txt

# Export role assignments (production subscription)
az role assignment list --scope /subscriptions/prod-subscription-id --output json > azure-rbac-prod-2024-01.json

# Export conditional access policies (MFA)
az rest --method GET --uri "https://graph.microsoft.com/v1.0/identity/conditionalAccess/policies" > conditional-access-2024-01.json
```

**Active Directory:**
```powershell
# Export all users
Get-ADUser -Filter * -Properties Title, Department, Enabled | Export-Csv ad-users-2024-01.csv

# Export production group members
Get-ADGroupMember -Identity "PROD-Ops-Admins" | Export-Csv prod-ops-members-2024-01.csv

# Export user group memberships
Get-ADUser -Identity jsmith -Properties MemberOf | Select-Object -ExpandProperty MemberOf
```

---

## Common Pitfalls

### Pitfall 1: Developers with Production Access

**Problem:** Developers have "read-only" or "monitoring" production access

**Impact:** MAJOR COMPLIANCE VIOLATION - zero developer access required

**Solution:**

- Revoke ALL developer production access (including read-only)
- Provide staging environment access instead (staging mirrors production)
- Implement read-only production dashboards (no direct access)
- Document break-glass for emergencies only


---

### Pitfall 2: Terminated Users with Lingering Access

**Problem:** Former employees still have access in IAM system

**Impact:** HIGH security risk - unauthorized access possible

**Solution:**
```bash
# Identify terminated users with active access
# Compare HR termination list with IAM active users
# Immediate account disable for all terminated users

# AWS example:
aws iam delete-login-profile --user-name terminated-user
aws iam delete-access-key --user-name terminated-user --access-key-id AKIA...
```

---

### Pitfall 3: MFA Optional, Not Mandatory

**Problem:** MFA enabled but not enforced (users can bypass)

**Impact:** MAJOR VULNERABILITY - production access without MFA

**Solution:**

- Change policy from "MFA enabled" to "MFA required"
- Block access if MFA not enrolled
- Test bypass attempts (should fail)


**AWS IAM Policy (enforce MFA):**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "BoolIfExists": {
          "aws:MultiFactorAuthPresent": "false"
        }
      }
    }
  ]
}
```

---

### Pitfall 4: Service Accounts Not Documented

**Problem:** Service accounts (non-human identities) missing from inventory

**Impact:** Incomplete access assessment, missing privileged accounts

**Solution:**

- Include ALL account types (human + service accounts)
- Mark account type clearly in inventory
- Document service account purpose
- Verify service account credentials rotated


---

### Pitfall 5: Break-Glass Used Routinely

**Problem:** Break-glass emergency access used weekly/monthly

**Impact:** Emergency access becoming routine = policy violation

**Solution:**

- Review break-glass usage frequency (should be rare: quarterly or less)
- If frequent usage, implement proper read-only production access for troubleshooting
- Reserve break-glass for true emergencies only
- Mandatory post-incident review for each use


---

### Pitfall 6: Audit Logs Not Monitored

**Problem:** Audit logging enabled but no one reviews logs

**Impact:** False sense of security - violations not detected

**Solution:**

- Implement automated log monitoring (SIEM)
- Configure alerts for unauthorized access attempts
- Schedule regular access reviews (weekly for production)
- Document monitoring procedures


---

## Quality Checklist

Before submitting your assessment for approval, verify:

### Completeness

- [ ] All sheets completed (1-9)
- [ ] All users documented (including service accounts, terminated users)
- [ ] Access matrix complete (all user + environment combinations)
- [ ] Production access verified (developer count = 0 or documented violations)
- [ ] All gaps identified and documented
- [ ] All evidence collected and organized


### Accuracy

- [ ] User inventory matches IAM system (exported, not manually typed)
- [ ] Access matrix verified by actual IAM policies (not assumptions)
- [ ] Production access list verified (cross-checked with job titles)
- [ ] MFA enrollment verified (checked in IAM system)
- [ ] Break-glass usage verified (checked incident logs)
- [ ] Audit logging verified (checked actual log retention)


### Critical Compliance Checks

- [ ] **ZERO developers with production access** (or documented violations)
- [ ] Terminated users have ZERO access (verified)
- [ ] MFA MANDATORY for production access (not optional)
- [ ] Break-glass usage rare (not routine)
- [ ] Audit logging enabled for production (minimum 90 days retention)


### Evidence Quality

- [ ] All evidence files time-stamped
- [ ] Evidence organized in structured folder
- [ ] Evidence file names descriptive and dated
- [ ] Evidence register complete with file locations
- [ ] Evidence accessible to reviewers/auditors


### Policy Compliance

- [ ] Assessment addresses all requirements from ISMS-POL-A.8.31, Section 2.2
- [ ] Any policy deviations documented as gaps
- [ ] Exceptions properly documented with approvals
- [ ] Regulatory requirements addressed (FINMA, DORA, NIS2 if applicable)


---

## Review & Approval

### Three-Level Approval Workflow

#### Level 1: Technical Review

- **Reviewer:** IAM Administrator or Identity Management Lead
- **Focus:** Access control accuracy, completeness
- **Timeline:** 2-3 business days
- **Outcome:** Approve, Request Changes, or Reject


**Review Criteria:**

- Is the user inventory complete and accurate?
- Is the access matrix verified against IAM system?
- Are production access restrictions enforced?
- Is evidence sufficient and verifiable?


#### Level 2: Security Review

- **Reviewer:** CISO or Information Security Manager
- **Focus:** Security compliance, risk assessment
- **Timeline:** 2-3 business days
- **Outcome:** Approve, Request Changes, or Reject


**Review Criteria:**

- Is zero developer production access enforced (or violations documented)?
- Are gaps realistic and properly prioritized?
- Are remediation timelines appropriate for risk severity?
- Is evidence sufficient for audit?


#### Level 3: Executive Approval

- **Reviewer:** CTO or VP Engineering
- **Focus:** Strategic alignment, resource allocation
- **Timeline:** 1-2 business days
- **Outcome:** Approve or Request Changes


**Review Criteria:**

- Are remediation resource requirements acceptable?
- Do timelines align with business priorities?
- Is risk posture acceptable?
- Are there budget implications?


### Approval Documentation

Document approvals in Sheet 9 (Evidence Register):

| Role | Name | Date | Signature | Comments |
|------|------|------|-----------|----------|
| Assessment Completed By | [Your Name] | [Date] | _____________ | Initial assessment |
| IAM Administrator | [Name] | [Date] | _____________ | Technical review approved |
| CISO | [Name] | [Date] | _____________ | Security review approved |
| CTO | [Name] | [Date] | _____________ | Executive approval |

---

## Maintenance & Updates

### Quarterly Updates

**Every 3 months, update:**

- Sheet 2: User Inventory (new hires, terminations, role changes)
- Sheet 3: Access Matrix (access changes)
- Sheet 4: Production Access (verify still zero developers)
- Sheet 5: MFA Enforcement (new user MFA enrollment)
- Sheet 7: Gap Analysis (gaps remediated? new gaps?)
- Sheet 9: Evidence Register (refresh dated evidence)


**Time required:** 2-3 hours

### Trigger-Based Updates

**Update immediately after:**

- Joiner event (new employee) - add to inventory, verify access
- Mover event (role change) - update access, verify production restrictions
- Leaver event (termination) - verify access removed
- Access control change (new IAM policy, group membership change)
- Security incident (unauthorized access) - document as gap
- Audit finding (document as gap, track remediation)


### Continuous Compliance Monitoring

**Automated monitoring:**

- IAM policy changes (CloudTrail, Azure Monitor)
- User provisioning/de-provisioning (HR system integration)
- Production access attempts (alert on developer access)
- MFA enrollment changes (alert if user disables MFA)
- Break-glass usage (alert on activation)


**Manual spot checks:**

- Monthly: Review production access list (verify still operations-only)
- Monthly: Review break-glass usage (should be rare)
- Quarterly: Full access matrix verification
- Quarterly: Terminated user access audit (should be zero)


---

**END OF PART I: USER COMPLETION GUIDE**

# PART II: TECHNICAL SPECIFICATION

## Workbook Structure

### Overview

The Environment Access Control Assessment workbook consists of 10 sheets:

1. **Instructions_Legend** - Metadata, instructions, status legend
2. **User_Environment_Access_Matrix** - All users with environment access and user → environment access mapping
3. **Developer_Production_Access** - CRITICAL: Zero developer production access check
4. **Production_Credential_Audit** - Production credential verification and PAM vault compliance
5. **Cross_Environment_Access_Log** - Tracking of cross-environment access requests and approvals
6. **Break_Glass_Access_Log** - Emergency access procedures and usage tracking
7. **MFA_Enforcement** - Multi-factor authentication compliance
8. **Access_Compliance_Scorecard** - Audit logging, access reviews, and compliance scoring
9. **Evidence_Register** - Supporting documentation inventory
10. **Approval_Sign_Off** - Multi-level approval workflow and signatures

---

## Sheet 1: Instructions & Legend

### Header Section

- **Row 1 (Merged A1:G1):** Title
  - Text: "ISMS-IMP-A.8.31.2 — Environment Access Control Assessment"
  - Style: Dark blue header (003366), white text, bold, centered, 40px height
  
- **Row 2 (Merged A2:G2):** Subtitle
  - Text: "ISO/IEC 27001:2022 - Control A.8.31: Separation of Development, Test and Production Environments"
  - Style: Medium blue header (4472C4), white text, centered, 30px height


### Document Information Block (Rows 4-12)

| Row | Column A (Label) | Column B (Value) | Column B Style |
|-----|------------------|------------------|----------------|
| 4 | Document ID: | ISMS-IMP-A.8.31.2 | Plain text |
| 5 | Assessment Area: | Environment Access Control & Production Restrictions | Plain text |
| 6 | Related Policy: | ISMS-POL-A.8.31, Section 2.2 | Plain text |
| 7 | Version: | 1.0 | Plain text |
| 8 | Assessment Date: | [USER INPUT] | Yellow fill (FFEB9C), bold |
| 9 | Completed By: | [USER INPUT] | Yellow fill (FFEB9C), bold |
| 10 | Organization: | [USER INPUT] | Yellow fill (FFEB9C), bold |
| 11 | Review Cycle: | Quarterly | Plain text |

**Column A:** Bold labels  
**Column B:** User input cells (rows 8-10) with yellow fill

### How to Use This Workbook (Rows 14-25)

- **Row 14:** "How to Use This Workbook" (bold, underlined)
- **Rows 15-25:** Numbered instructions (1-11)


```
1. PREREQUISITE: Complete ISMS-IMP-A.8.31.1 (Environment Architecture) FIRST
2. Export environment list from A.8.31.1, Sheet 2 (needed for access matrix)
3. Complete User_Inventory for ALL users (human + service accounts, including terminated)
4. Build Access_Matrix (user → environment access mapping)
5. Complete Production_Access_Verification (CRITICAL: verify zero developer access)
6. Verify MFA_Enforcement (mandatory for production)
7. Document BreakGlass_Emergency_Access (emergency procedures and usage)
8. Verify Access_Monitoring (audit logging, access reviews)
9. Complete Gap_Analysis for all non-compliance areas
10. Collect Evidence (IAM exports, audit logs, screenshots)
11. Obtain three-level approval (IAM Admin → Security → Executive)
```

### Critical Compliance Requirement (Rows 27-30)

- **Row 27:** "CRITICAL COMPLIANCE REQUIREMENT" (bold, red text, yellow background)
- **Row 28:** "ZERO DEVELOPER ACCESS TO PRODUCTION (except documented break-glass emergencies)"
- **Row 29:** "Developer production access = MAJOR AUDIT FINDING"
- **Row 30:** "Target: 0 developers with production access"


### Status Legend (Rows 32-38)

| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Compliant | Fully compliant with policy requirement | Green (C6EFCE) |
| ⚠️ | Partial | Partially compliant or compensating controls | Yellow (FFEB9C) |
| ❌ | Non-Compliant | Not compliant, remediation required | Red (FFC7CE) |
| 🔴 | MAJOR VIOLATION | Developer production access (immediate remediation) | Dark Red (8B0000) |
| 📋 | Planned | Remediation planned with target date | Blue (B4C7E7) |
| N/A | Not Applicable | Requirement not applicable | Gray (D9D9D9) |

### Acceptable Evidence (Rows 40-54)

- **Row 40:** "Acceptable Evidence (Examples)" (bold, underlined)
- **Rows 41-54:** Bulleted list with checkmarks


```
✓ IAM policy exports (AWS IAM, Azure RBAC, GCP IAM)
✓ User → group/role assignment exports
✓ Active Directory user lists with group memberships
✓ Production access restriction configurations
✓ MFA enforcement policy configurations
✓ MFA enrollment status per user
✓ Break-glass emergency access procedures
✓ Break-glass usage logs (last 90 days)
✓ Audit log configurations (CloudTrail, Azure Monitor, AD audit logs)
✓ Access review records (production access reviews)
✓ Access monitoring dashboards (SIEM alerts)
✓ Terminated user access verification (should be zero)
✓ Developer production access count (should be zero)
✓ Compliance violation remediation plans
```

---

## Sheet 2: User_Inventory

### Purpose
Document all users with access to ANY environment (human users + service accounts, including terminated users).

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:H1):** "USER INVENTORY"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:H2):** "Document ALL users with environment access - include human users, service accounts, and TERMINATED users"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height


### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | User ID / Username | 20 | Text |
| B | Full Name | 25 | Text |
| C | Job Title / Role | 25 | Dropdown |
| D | Department | 20 | Text |
| E | Account Type | 18 | Dropdown |
| F | Employment Status | 18 | Dropdown |
| G | Termination Date | 15 | Date |
| H | Notes | 40 | Text |

**Row 4 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column C: Job Title / Role**

- Developer
- Senior Developer
- Lead Developer
- QA Engineer / Tester
- DevOps Engineer
- Operations Engineer
- System Administrator
- Security Analyst
- Database Administrator
- Business Analyst
- Manager
- Service Account
- Other


**Column E: Account Type**

- Human (regular employee)
- Human (contractor)
- Service Account
- Break-Glass Account
- Shared Account (discouraged)


**Column F: Employment Status**

- Active
- Inactive (leave of absence)
- Terminated
- Contractor (active)
- Contractor (ended)


### Sample Data (Rows 5-10)

| User ID | Full Name | Job Title | Department | Account Type | Status | Termination Date | Notes |
|---------|-----------|-----------|------------|--------------|--------|------------------|-------|
| jdoe | John Doe | Senior Developer | Engineering | Human (employee) | Active | N/A | Full-stack developer |
| jsmith | Jane Smith | Operations Engineer | IT Operations | Human (employee) | Active | N/A | Production ops lead |
| tchen | Tom Chen | QA Engineer | Quality Assurance | Human (employee) | Active | N/A | Test automation |
| svc_backup | Backup Service | Service Account | IT Operations | Service Account | Active | N/A | Automated backup system |
| breakglass_001 | Emergency Access 001 | Break-Glass Account | Security | Break-Glass Account | Active | N/A | Emergency production access |
| bjones | Bob Jones | Developer | Engineering | Human (employee) | Terminated | 2023-12-15 | ⚠️ VERIFY ACCESS REMOVED |

### User Input Rows (11+)

Yellow-filled cells (FFEB9C) for user data entry.

**Critical Notes:**

- Include ALL users (active + terminated + service accounts)
- Terminated users should have ZERO access (verify in access matrix)
- Service accounts must be documented (non-human identities)
- Break-glass accounts tracked separately


---

## Sheet 3: Access_Matrix

### Purpose
Document user → environment access mapping (who can access which environments).

### Header Section (Rows 1-3)

- **Row 1 (Merged A1:J1):** "USER → ENVIRONMENT ACCESS MATRIX"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:J2):** "For each user, document access to EACH environment - verify via IAM system (do NOT assume)"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

- **Row 3:** "CRITICAL: Production column should show ZERO developers"
  - Style: Red background (FFC7CE), dark text, bold, centered, 25px height


### Column Headers (Row 5)

**Dynamic columns based on environments from A.8.31.1:**

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | User ID | 20 | Dropdown (from Sheet 2) |
| B | Full Name | 25 | Text (auto-populated from Sheet 2) |
| C | Job Title | 25 | Text (auto-populated from Sheet 2) |
| D | Development Access | 20 | Dropdown |
| E | Testing Access | 20 | Dropdown |
| F | Staging Access | 20 | Dropdown |
| G | Production Access | 20 | Dropdown |
| H | Production Access Justified? | 25 | Dropdown |
| I | Access Verification Method | 30 | Text |
| J | Last Verified Date | 15 | Date |

**NOTE**: Columns D-G are DYNAMIC based on environments from A.8.31.1, Sheet 2. Above shows standard 4-environment setup.

**Row 5 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

**Column G (Production Access) Special Formatting:**

- Header: Dark red background (8B0000), white text
- Cells with "Admin" or "Read-Write": Red fill (FFC7CE) - triggers production access verification


### Data Validation (Dropdowns)

**Columns D-G: Environment Access Level**

- ❌ None (no access)
- Read-Only
- Read-Write
- Admin (full control)
- Via Break-Glass Only


**Column H: Production Access Justified? (only if Column G ≠ None)**

- ✅ Yes (Operations/Support role)
- ❌ No (Developer role - VIOLATION)
- ⚠️ Break-Glass Only
- N/A (no production access)


### Sample Data (Rows 6-11)

| User ID | Full Name | Job Title | Development | Testing | Staging | Production | Prod Justified? | Verification | Last Verified |
|---------|-----------|-----------|-------------|---------|---------|------------|----------------|--------------|---------------|
| jdoe | John Doe | Senior Developer | Admin | Read-Write | Read-Only | ❌ None | N/A | AWS IAM policy review | 2024-01-20 |
| jsmith | Jane Smith | Operations Engineer | Read-Only | Read-Only | Admin | Admin (via PAM) | ✅ Yes (Operations) | AWS IAM policy review | 2024-01-20 |
| tchen | Tom Chen | QA Engineer | Read-Only | Admin | Read-Only | ❌ None | N/A | AWS IAM policy review | 2024-01-20 |
| svc_backup | Backup Service | Service Account | Read-Only | Read-Only | Read-Only | Read-Only | ✅ Yes (Backup) | AWS IAM policy review | 2024-01-20 |
| bjones | Bob Jones | Developer (TERMINATED) | ❌ VIOLATION: Read-Write | ❌ VIOLATION: Read-Only | ❌ None | ❌ None | N/A | AWS IAM user list | 2024-01-20 |

### Conditional Formatting Rules

**Production Access Column (Column G):**

- If value = "Admin" or "Read-Write" → Red fill (FFC7CE)
- If value = "Read-Only" AND Job Title contains "Developer" → Red fill (FFC7CE)
- If value = "❌ None" → Green fill (C6EFCE)


**Terminated Users:**

- If Employment Status (from Sheet 2) = "Terminated" AND any access column ≠ "❌ None" → Red fill (FFC7CE)


### Critical Verification

**After completing matrix:**
1. Filter Production Access column for any value except "❌ None"
2. For each user with production access, verify Job Title is Operations/Support
3. Count developers with production access → **TARGET: 0**

---

## Sheet 4: Production_Access_Verification

### Purpose
Verify zero developer production access (CRITICAL COMPLIANCE CHECK).

### Header Section (Rows 1-3)

- **Row 1 (Merged A1:H1):** "PRODUCTION ACCESS VERIFICATION"
  - Style: Dark red (8B0000), white text, bold, centered, 40px height
  
- **Row 2 (Merged A2:H2):** "CRITICAL: Zero developer access to production (except break-glass emergencies)"
  - Style: Light red (FFC7CE), dark text, bold, centered, 30px height

- **Row 3 (Merged A3:H3):** "List ALL users with production access - verify each is Operations/Support role"
  - Style: Light red (FFC7CE), dark text, centered, 25px height


### Summary Metrics (Rows 5-10)

| Row | Metric | Value Formula | Color Code |
|-----|--------|---------------|------------|
| 5 | **Total Users with Production Access:** | =COUNTA(A12:A1000)-1 | Bold |
| 6 | **Operations/Support Users (Compliant):** | =COUNTIF(F12:F1000,"✅ Yes") | Green if >0 |
| 7 | **Developers with Production Access:** | =COUNTIF(F12:F1000,"❌ No") | Red if >0 |
| 8 | **TARGET - Developers with Prod Access:** | 0 | Green |
| 9 | **ACTUAL - Developers with Prod Access:** | =COUNTIF(F12:F1000,"❌ No") | Red if >0, Green if =0 |
| 10 | **Compliance Status:** | =IF(COUNTIF(F12:F1000,"❌ No")=0,"✅ COMPLIANT","🔴 MAJOR VIOLATION") | Conditional |

### Column Headers (Row 12)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | User ID | 20 | Dropdown (from Sheet 2) |
| B | Full Name | 25 | Text (auto-populated) |
| C | Job Title | 25 | Text (auto-populated) |
| D | Production Access Level | 20 | Dropdown (from Sheet 3) |
| E | Access Method | 30 | Text |
| F | Operations/Support Role? | 22 | Dropdown |
| G | Compliance Status | 18 | Dropdown |
| H | Evidence | 35 | Text |

**Row 12 Style:** Dark red header (8B0000), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column D: Production Access Level**

- Admin (full control)
- Read-Write
- Read-Only
- Via Break-Glass Only


**Column F: Operations/Support Role?**

- ✅ Yes (Operations, SysAdmin, DBA, Security, Monitoring)
- ❌ No (Developer, QA, Business Analyst) - VIOLATION
- ⚠️ Service Account (acceptable if documented)


**Column G: Compliance Status**

- ✅ Compliant (Operations/Support role)
- 🔴 MAJOR VIOLATION (Developer with production access)
- ⚠️ Service Account (acceptable)
- ⚠️ Break-Glass Only (acceptable if monitored)


### Sample Data (Rows 13-17)

| User ID | Full Name | Job Title | Prod Access | Access Method | Ops/Support? | Compliance | Evidence |
|---------|-----------|-----------|-------------|---------------|--------------|------------|----------|
| jsmith | Jane Smith | Operations Engineer | Admin (via PAM) | AWS IAM role: ProdOpsAccess | ✅ Yes | ✅ Compliant | aws-iam-prod-policy.json |
| svc_monitoring | Monitoring Service | Service Account | Read-Only | AWS IAM role: MonitoringReadOnly | ⚠️ Service Account | ⚠️ Service Account | aws-iam-monitoring-policy.json |
| svc_backup | Backup Service | Service Account | Read-Only | AWS IAM role: BackupService | ⚠️ Service Account | ⚠️ Service Account | aws-iam-backup-policy.json |
| jdoe | John Doe | Senior Developer | Read-Only | AWS IAM role: DevReadOnly | ❌ No | 🔴 MAJOR VIOLATION | FINDING: Developer has production access |

### Critical Alerts

**If any row has Compliance Status = "🔴 MAJOR VIOLATION":**

- Entire row highlighted in red (FFC7CE)
- Alert icon in Summary Metrics (Row 9)
- Gap automatically created in Sheet 8 (Gap Analysis)


---

## Sheet 5: MFA_Enforcement

### Purpose
Verify MFA (Multi-Factor Authentication) is MANDATORY for production access.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:H1):** "MFA ENFORCEMENT VERIFICATION"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:H2):** "Verify MFA is MANDATORY (not optional) for ALL production access"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height


### MFA Policy Summary (Rows 4-8)

| Row | Attribute | Value | Notes |
|-----|-------|-------|-------|
| 4 | **MFA Required for Production?** | [USER INPUT: Yes/No] | Yellow cell |
| 5 | **MFA Policy Type:** | [USER INPUT: Mandatory/Optional/Recommended] | Yellow cell |
| 6 | **MFA Enforcement Method:** | [USER INPUT: IAM Policy/Conditional Access/Other] | Yellow cell |
| 7 | **MFA Bypass Possible?** | [USER INPUT: Yes/No/Unknown] | Yellow cell (Red if Yes) |
| 8 | **MFA Policy Evidence:** | [USER INPUT: File location] | Yellow cell |

### Column Headers (Row 10)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | User ID | 20 | Dropdown (from Sheet 4 - production users only) |
| B | Full Name | 25 | Text |
| C | Job Title | 25 | Text |
| D | MFA Enrolled? | 18 | Dropdown |
| E | MFA Device Type | 25 | Dropdown |
| F | MFA Required or Optional? | 22 | Dropdown |
| G | MFA Bypass Possible? | 20 | Dropdown |
| H | Compliance Status | 18 | Dropdown |
| I | Evidence | 30 | Text |

**Row 10 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column D: MFA Enrolled?**

- ✅ Yes (enrolled and active)
- ❌ No (not enrolled) - VIOLATION
- ⚠️ Pending (enrollment in progress)
- N/A (service account - alternative auth)


**Column E: MFA Device Type**

- Authenticator App (Google Authenticator, Microsoft Authenticator)
- Hardware Token (YubiKey, RSA SecurID)
- SMS (discouraged - phishing risk)
- Biometric (fingerprint, face recognition)
- API Key (service accounts only)
- N/A


**Column F: MFA Required or Optional?**

- ✅ Required (mandatory - cannot bypass)
- ⚠️ Optional (user can choose - VIOLATION)
- ⚠️ Recommended (not enforced - VIOLATION)
- N/A


**Column G: MFA Bypass Possible?**

- ❌ No (bypass blocked - correct)
- ⚠️ Yes (bypass allowed - VIOLATION)
- ⚠️ Unknown (needs testing)
- N/A


**Column H: Compliance Status**

- ✅ Compliant (MFA enrolled + required + no bypass)
- ❌ Non-Compliant (MFA not enrolled or optional or bypass possible)
- ⚠️ Service Account (alternative auth acceptable)
- 📋 Remediation Planned


### Sample Data (Rows 11-15)

| User ID | Full Name | Job Title | MFA Enrolled? | MFA Device | Required? | Bypass? | Compliance | Evidence |
|---------|-----------|-----------|---------------|------------|-----------|---------|------------|----------|
| jsmith | Jane Smith | Operations Engineer | ✅ Yes | Authenticator App | ✅ Required | ❌ No | ✅ Compliant | aws-mfa-enrollment.json |
| svc_monitoring | Monitoring Service | Service Account | N/A | API Key (rotated monthly) | N/A | N/A | ⚠️ Service Account | aws-api-key-rotation.log |
| jdoe | John Doe | Senior Developer | ❌ No | N/A | ⚠️ Optional | ⚠️ Yes | ❌ Non-Compliant | FINDING: Developer with prod access (from Sheet 4) |

### Critical Requirements

**For compliance:**

- [ ] MFA policy = "Mandatory" (not "Optional")
- [ ] MFA bypass = "No" (cannot be bypassed)
- [ ] All production users enrolled (except service accounts with alternative auth)


---

## Sheet 6: BreakGlass_Emergency_Access

### Purpose
Document break-glass emergency access procedures and usage tracking.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:H1):** "BREAK-GLASS EMERGENCY ACCESS"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:H2):** "Document emergency access procedures - usage should be RARE (monthly usage = process problem)"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height


### Break-Glass Policy Summary (Rows 4-10)

| Row | Attribute | Value | Notes |
|-----|-------|-------|-------|
| 4 | **Break-Glass Procedure Documented?** | [USER INPUT: Yes/No] | Yellow cell |
| 5 | **Activation Approval Required?** | [USER INPUT: Yes/No/Who] | Yellow cell |
| 6 | **Time Limit (auto-revoke)?** | [USER INPUT: Hours] | Yellow cell |
| 7 | **Post-Incident Review Mandatory?** | [USER INPUT: Yes/No] | Yellow cell |
| 8 | **Break-Glass Usage (Last 90 days):** | [CALCULATED] | Auto-count from usage log |
| 9 | **Usage Frequency Assessment:** | [CALCULATED: Rare/Occasional/Frequent] | Green/Yellow/Red |
| 10 | **Break-Glass Procedure Document:** | [USER INPUT: File location] | Yellow cell |

### Break-Glass Accounts (Rows 12+)

**Column Headers (Row 12):**

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Account ID | 20 | Text |
| B | Account Purpose | 30 | Text |
| C | Authorized Approvers | 30 | Text (comma-separated) |
| D | Time Limit (hours) | 15 | Number |
| E | Auto-Revoke? | 15 | Dropdown |
| F | Last Used Date | 15 | Date |
| G | Usage Count (90 days) | 15 | Number |
| H | Status | 15 | Dropdown |

**Sample Data (Rows 13-15):**

| Account ID | Purpose | Authorized Approvers | Time Limit | Auto-Revoke | Last Used | Usage Count | Status |
|------------|---------|---------------------|------------|-------------|-----------|-------------|--------|
| breakglass_dev_001 | Emergency production fix (developers) | CISO, IT Ops Manager | 4 hours | ✅ Yes | 2024-01-10 | 1 | ✅ Active |
| breakglass_ops_001 | Emergency operations access | CISO | 8 hours | ✅ Yes | Never used | 0 | ✅ Active |

### Break-Glass Usage Log (Last 90 Days)

**Column Headers (Row 20):**

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Date/Time | 18 | DateTime |
| B | User (who activated) | 20 | Text |
| C | Break-Glass Account Used | 25 | Text |
| D | Duration (hours) | 15 | Number |
| E | Purpose / Incident | 40 | Text |
| F | Incident Ticket | 15 | Text |
| G | Post-Review Completed? | 20 | Dropdown |
| H | Review Date | 15 | Date |

**Sample Data (Rows 21-22):**

| Date/Time | User | Account | Duration | Purpose | Incident | Post-Review? | Review Date |
|-----------|------|---------|----------|---------|----------|--------------|-------------|
| 2024-01-10 14:23 | jdoe | breakglass_dev_001 | 2 hours | Critical production bug fix (payment API down) | INC-2024-001 | ✅ Yes | 2024-01-12 |

### Usage Frequency Assessment

**Formula for Row 9:**
```
=IF(H8=0,"✅ Rare (none)",IF(H8<=3,"✅ Rare (acceptable)",IF(H8<=10,"⚠️ Occasional (review needed)","❌ Frequent (process issue)")))
```

**Interpretation:**

- 0 uses: ✅ Rare (perfect - none needed)
- 1-3 uses: ✅ Rare (acceptable for emergencies)
- 4-10 uses: ⚠️ Occasional (review why so frequent)
- 11+ uses: ❌ Frequent (becoming routine - process issue)


---

## Sheet 7: Access_Monitoring

### Purpose
Verify audit logging and access review processes.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:I1):** "ACCESS MONITORING & AUDIT LOGGING"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:I2):** "Verify audit logging enabled, logs monitored, and access reviews performed regularly"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height


### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Environment | 18 | Dropdown (from A.8.31.1 Sheet 2) |
| B | Logging Enabled? | 18 | Dropdown |
| C | Events Logged | 40 | Text |
| D | Retention Period (days) | 18 | Number |
| E | Logs Monitored? | 18 | Dropdown |
| F | Monitoring Method | 30 | Text |
| G | Alerts Configured? | 18 | Dropdown |
| H | Access Review Frequency | 22 | Dropdown |
| I | Compliance Status | 18 | Dropdown |
| J | Evidence | 30 | Text |

**Row 4 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column B: Logging Enabled?**

- ✅ Yes (full logging)
- ⚠️ Partial (some events only)
- ❌ No (not enabled) - VIOLATION


**Column E: Logs Monitored?**

- ✅ Yes (automated + manual review)
- ⚠️ Partial (manual review only)
- ❌ No (collection only, no review) - VIOLATION


**Column G: Alerts Configured?**

- ✅ Yes (unauthorized access → alert)
- ⚠️ Partial (some alerts only)
- ❌ No (no alerts) - VIOLATION


**Column H: Access Review Frequency**

- Daily (production recommended)
- Weekly
- Monthly
- Quarterly
- ❌ None (no reviews) - VIOLATION


**Column I: Compliance Status**

- ✅ Compliant (logging + monitoring + alerts + reviews)
- ⚠️ Partial (missing some requirements)
- ❌ Non-Compliant (critical gaps)


### Sample Data (Rows 5-8)

| Environment | Logging? | Events | Retention | Monitored? | Method | Alerts? | Review Freq | Compliance | Evidence |
|-------------|----------|--------|-----------|------------|--------|---------|-------------|------------|----------|
| Production | ✅ Yes | Login, permission changes, resource access, failed attempts | 365 days | ✅ Yes | SIEM (Splunk) | ✅ Yes | Weekly | ✅ Compliant | cloudtrail-config.json |
| Staging | ✅ Yes | Login, permission changes | 90 days | ⚠️ Partial | Manual review | ❌ No | Monthly | ⚠️ Partial | cloudtrail-config.json |
| Testing | ✅ Yes | Login attempts only | 30 days | ❌ No | None | ❌ No | Quarterly | ⚠️ Partial | cloudtrail-config.json |
| Development | ⚠️ Partial | Login only | 7 days | ❌ No | None | ❌ No | None | ❌ Non-Compliant | FINDING: Inadequate logging |

### Critical Requirements (Production)

**Minimum requirements for production:**

- ✅ Logging enabled (full event logging)
- ✅ Retention ≥ 90 days (regulatory requirement)
- ✅ Logs monitored (automated + manual)
- ✅ Alerts configured (unauthorized access)
- ✅ Access reviews (minimum monthly, recommended weekly)


---

## Sheet 8: Gap_Analysis

### Purpose
Document all access control non-compliance areas, risk severity, and remediation plans.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:J1):** "GAP ANALYSIS & REMEDIATION PLANNING"
  - Style: Dark red (8B0000), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:J2):** "Document ALL access control gaps - prioritize by risk (developer production access = HIGH)"
  - Style: Light red (FFC7CE), dark text, bold, centered, 25px height


### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Gap ID | 10 | Text |
| B | Gap Description | 45 | Text |
| C | Policy Requirement Violated | 35 | Text |
| D | Risk Severity | 15 | Dropdown |
| E | Current Risk | 35 | Text |
| F | Proposed Remediation | 45 | Text |
| G | Estimated Effort (hours) | 15 | Number |
| H | Target Completion Date | 18 | Date |
| I | Assigned Owner | 20 | Text |
| J | Status | 15 | Dropdown |

**Row 4 Style:** Dark red header (8B0000), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column D: Risk Severity**

- 🔴 High (developer production access, MFA not mandatory, terminated user access)
- 🟡 Medium (audit logging gaps, excessive break-glass usage)
- 🟢 Low (documentation gaps, manual processes)
- ⚪ Info (awareness, no remediation)


**Column J: Status**

- 📋 Identified (not started)
- 🔄 In Progress (remediation underway)
- ✅ Remediated (completed, verified)
- ⏸️ On Hold (dependencies or approvals)
- ❌ Risk Accepted (executive decision)


### Sample Data (Rows 5-10)

| Gap ID | Description | Policy Violated | Severity | Current Risk | Remediation | Effort | Target Date | Owner | Status |
|--------|-------------|-----------------|----------|--------------|-------------|--------|-------------|-------|--------|
| GAP-001 | 1 developer (jdoe) has production read-only access | ISMS-POL-A.8.31, Section 2.2 | 🔴 High | Developer can view production data | Revoke production access, provide staging read-only instead | 2h | 2024-01-25 | IAM Admin | 🔄 In Progress |
| GAP-002 | Terminated user (bjones) still has dev/test access | ISMS-POL-A.8.31, Section 2.2 | 🔴 High | Former employee unauthorized access | Disable account immediately, review offboarding checklist | 1h | 2024-01-25 | IAM Admin | 📋 Identified |
| GAP-003 | MFA optional for production access (not mandatory) | ISMS-POL-A.8.31, Section 2.2 | 🔴 High | Production access without MFA possible | Change policy to mandatory, enforce via IAM policy | 8h | 2024-02-01 | Security Eng | 📋 Identified |
| GAP-004 | Break-glass used 12 times in last 90 days (frequent) | ISMS-POL-A.8.31, Section 2.5 | 🟡 Medium | Emergency access becoming routine | Implement read-only production troubleshooting access | 16h | 2024-03-15 | DevOps Lead | 📋 Identified |
| GAP-005 | Development environment audit logs only retained 7 days | ISMS-POL-A.8.31, Section 2.2 | 🟢 Low | Limited audit trail for dev environment | Increase retention to 90 days | 2h | 2024-04-30 | Security Eng | 📋 Identified |

### Gap Prioritization Matrix

| Severity | Examples | Remediation Timeline |
|----------|----------|---------------------|
| 🔴 High | Developer production access, terminated user access, MFA not mandatory | Immediate (within 30 days) |
| 🟡 Medium | Audit logging gaps, excessive break-glass usage, weak monitoring | Within 90 days |
| 🟢 Low | Documentation gaps, manual access reviews, short log retention | Within 180 days |

---

## Sheet 9: Evidence_Register

### Purpose
Central registry of all supporting evidence for audit traceability.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:H1):** "EVIDENCE REGISTER"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:H2):** "Document ALL supporting evidence - IAM exports, audit logs, screenshots, access review records"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height


### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Evidence ID | 12 | Text |
| B | Evidence Type | 20 | Dropdown |
| C | Description | 50 | Text |
| D | File Name | 35 | Text |
| E | Date Collected | 15 | Date |
| F | Related Requirement | 30 | Text |
| G | Related Sheet | 15 | Dropdown |
| H | File Location | 40 | Text |

**Row 4 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column B: Evidence Type**

- IAM Policy Export
- User List Export
- Access Assignment Export
- Screenshot
- Audit Log Export
- Access Review Record
- Break-Glass Procedure
- MFA Configuration
- Approval Record
- Other


**Column G: Related Sheet**

- Sheet 2: User_Inventory
- Sheet 3: Access_Matrix
- Sheet 4: Production_Access_Verification
- Sheet 5: MFA_Enforcement
- Sheet 6: BreakGlass_Emergency_Access
- Sheet 7: Access_Monitoring
- Sheet 8: Gap_Analysis
- Multiple Sheets


### Sample Data (Rows 5-15)

| Evidence ID | Type | Description | File Name | Date | Related Requirement | Sheet | Location |
|-------------|------|-------------|-----------|------|---------------------|-------|----------|
| EVD-001 | IAM Policy Export | AWS IAM production role policy | aws-iam-prod-policy-2024-01.json | 2024-01-20 | ISMS-POL-A.8.31, Section 2.2 | Sheet 4 | ./evidence/EVD-001/ |
| EVD-002 | User List Export | Complete AWS IAM user list | aws-iam-users-2024-01.json | 2024-01-20 | ISMS-POL-A.8.31, Section 2.2 | Sheet 2 | ./evidence/EVD-002/ |
| EVD-003 | Access Assignment Export | IAM role → user assignments | aws-iam-role-assignments-2024-01.csv | 2024-01-20 | ISMS-POL-A.8.31, Section 2.2 | Sheet 3 | ./evidence/EVD-003/ |
| EVD-004 | Screenshot | MFA enforcement policy configuration | mfa-policy-screenshot-2024-01.png | 2024-01-21 | ISMS-POL-A.8.31, Section 2.2 | Sheet 5 | ./evidence/EVD-004/ |
| EVD-005 | Break-Glass Procedure | Emergency access procedure document | breakglass-procedure-v1.2.pdf | 2024-01-22 | ISMS-POL-A.8.31, Section 2.5 | Sheet 6 | ./evidence/EVD-005/ |
| EVD-006 | Audit Log Export | Production access audit log (90 days) | cloudtrail-prod-access-2024-01.csv | 2024-01-22 | ISMS-POL-A.8.31, Section 2.2 | Sheet 7 | ./evidence/EVD-006/ |
| EVD-007 | Access Review Record | Production access review (January 2024) | prod-access-review-2024-01.xlsx | 2024-01-25 | ISMS-POL-A.8.31, Section 2.2 | Sheet 7 | ./evidence/EVD-007/ |
| EVD-008 | User List Export | Active Directory user list with groups | ad-users-groups-2024-01.csv | 2024-01-20 | ISMS-POL-A.8.31, Section 2.2 | Sheet 2, 3 | ./evidence/EVD-008/ |
| EVD-009 | MFA Configuration | Azure Conditional Access MFA policy | azure-ca-mfa-policy-2024-01.json | 2024-01-21 | ISMS-POL-A.8.31, Section 2.2 | Sheet 5 | ./evidence/EVD-009/ |
| EVD-010 | Approval Record | Access control assessment approval | assessment-approval-2024-01.pdf | 2024-01-28 | ISO 27001 audit requirement | Multiple | ./evidence/EVD-010/ |

### Evidence Organization

**Folder Structure:**
```
evidence/
├── EVD-001-aws-iam-prod-policy-2024-01.json
├── EVD-002-aws-iam-users-2024-01.json
├── EVD-003-aws-iam-role-assignments-2024-01.csv
├── EVD-004-mfa-policy-screenshot-2024-01.png
├── EVD-005-breakglass-procedure-v1.2.pdf
├── EVD-006-cloudtrail-prod-access-2024-01.csv
├── EVD-007-prod-access-review-2024-01.xlsx
├── EVD-008-ad-users-groups-2024-01.csv
├── EVD-009-azure-ca-mfa-policy-2024-01.json
└── EVD-010-assessment-approval-2024-01.pdf
```

**File Naming Convention:**
`[Evidence-ID]-[description]-[YYYY-MM].[extension]`

---

## Sheet 10: Approval_Sign_Off

### Purpose
Multi-level approval workflow and formal sign-off for the assessment.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:F1):** "APPROVAL & SIGN-OFF"
  - Style: Dark blue (003366), white text, bold, centered, 35px height

- **Row 2 (Merged A2:F2):** "Formal approval workflow - Assessment requires three-level approval before finalization"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height


### Assessment Summary (Rows 4-11)

| Row | Attribute | Value |
|-----|-----------|-------|
| 4 | Assessment ID: | ISMS-IMP-A.8.31.2 |
| 5 | Assessment Name: | Environment Access Control Assessment |
| 6 | Assessment Date: | [From Sheet 1] |
| 7 | Completed By: | [From Sheet 1] |
| 8 | Total Users Assessed: | [Count from Sheet 2] |
| 9 | Developers with Production Access: | [Count from Sheet 3 - TARGET: 0] |
| 10 | Total Gaps Identified: | [Count from Sheet 8] |
| 11 | Overall Compliance Status: | [Summary status] |


### Critical Compliance Check (Rows 13-16)

**Row 13:** "CRITICAL COMPLIANCE VERIFICATION" (bold, red background)

| Check | Target | Actual | Status |
|-------|--------|--------|--------|
| Developer Production Access Count | 0 | [From Sheet 3] | [✅ if 0, 🔴 MAJOR VIOLATION if >0] |
| MFA Enforcement for Production | 100% | [From Sheet 7] | [✅/⚠️/❌] |
| Terminated Users with Access | 0 | [Calculated] | [✅ if 0, 🔴 VIOLATION if >0] |


### Approval Workflow (Rows 18-31)

**Level 1: Technical Review (Rows 20-23)**

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Reviewer Role | 25 | Text |
| B | Reviewer Name | 25 | Text (user input) |
| C | Review Date | 15 | Date (user input) |
| D | Decision | 15 | Dropdown |
| E | Comments | 50 | Text (user input) |
| F | Signature | 20 | Text (user input) |

**Dropdown for Decision:**
- Approved
- Approved with Comments
- Request Changes
- Rejected


**Level 1 Reviewers:**
| Role | Name | Date | Decision | Comments | Signature |
|------|------|------|----------|----------|-----------|
| IAM Administrator | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |
| Identity Management Lead | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |

**Level 2: Security Review (Rows 25-27)**

| Role | Name | Date | Decision | Comments | Signature |
|------|------|------|----------|----------|-----------|
| Information Security Manager | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |
| CISO | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |

**Level 3: Executive Approval (Rows 29-31)**

| Role | Name | Date | Decision | Comments | Signature |
|------|------|------|----------|----------|-----------|
| CTO / VP Engineering | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |


### Approval Status Summary (Rows 33-36)

| Metric | Value | Status |
|--------|-------|--------|
| Level 1 (Technical) Status | [Auto-calculated] | [✅/⚠️/❌] |
| Level 2 (Security) Status | [Auto-calculated] | [✅/⚠️/❌] |
| Level 3 (Executive) Status | [Auto-calculated] | [✅/⚠️/❌] |
| **Overall Approval Status** | [Auto-calculated] | [✅ Approved / ⚠️ Pending / ❌ Not Approved] |


### Conditional Approval Notes (Rows 38-44)

**Row 38:** "Conditional Approval Notes" (bold, underlined)

**Rows 39-44:** User input text area (yellow fill)
- Document any conditions attached to approval
- Document required follow-up actions for developer production access (if any violations)
- Document timeline for MFA enforcement completion
- Document terminated user access remediation


### Next Assessment Date (Rows 46-48)

| Attribute | Value |
|-----------|-------|
| Next Scheduled Assessment: | [User Input: Date] |
| Assessment Frequency: | Quarterly |
| Trigger-Based Review: | After joiner/mover/leaver events, access control changes |

---

## Cell Styling Reference

### Color Codes

| Style | Background | Font Color | Usage |
|-------|------------|------------|-------|
| Header (dark blue) | #003366 | White (#FFFFFF) | Sheet titles, major headers |
| Header (medium blue) | #4472C4 | White (#FFFFFF) | Column headers |
| Header (dark red) | #8B0000 | White (#FFFFFF) | Critical sheets (Production Access, Gaps) |
| Subheader (light blue) | #B4C7E7 | Dark (#000000) | Sheet instructions |
| Subheader (light red) | #FFC7CE | Dark (#000000) | Critical requirement warnings |
| User Input | #FFEB9C (yellow) | Dark (#000000) | Cells user must complete |
| Compliant | #C6EFCE (green) | Dark (#000000) | ✅ status |
| Partial | #FFEB9C (yellow) | Dark (#000000) | ⚠️ status |
| Non-Compliant | #FFC7CE (red) | Dark (#000000) | ❌ status |
| MAJOR VIOLATION | #8B0000 (dark red) | White (#FFFFFF) | 🔴 status (developer prod access) |
| Planned | #B4C7E7 (blue) | Dark (#000000) | 📋 status |
| Read-Only | #D9D9D9 (gray) | Dark (#000000) | Calculated or locked cells |

### Font Styles

| Element | Font | Size | Weight | Alignment |
|---------|------|------|--------|-----------|
| Sheet Title (Row 1) | Calibri | 18pt | Bold | Center |
| Subtitle (Row 2) | Calibri | 12pt | Regular | Center |
| Critical Warning (Row 3) | Calibri | 11pt | Bold | Center |
| Column Headers | Calibri | 11pt | Bold | Center |
| Data Cells | Calibri | 10pt | Regular | Left |
| User Input | Calibri | 10pt | Bold | Left |
| Summary Metrics | Calibri | 11pt | Bold | Left |

### Conditional Formatting Rules

**Sheet 3: Access_Matrix**

- Production Access column: Red fill if ≠ "❌ None" AND Job Title contains "Developer"
- Terminated users: Red fill if any access ≠ "❌ None"


**Sheet 4: Production_Access_Verification**

- Row 9 (Actual Developer Count): Red if >0, Green if =0
- Any row with "🔴 MAJOR VIOLATION": Entire row red fill


**Sheet 6: BreakGlass_Emergency_Access**

- Row 9 (Usage Frequency): Green if "Rare", Yellow if "Occasional", Red if "Frequent"


---

## Integration Points

### Input from Other Assessments

**From ISMS-IMP-A.8.31.1 (Environment Architecture):**

- Sheet 2: Environment_Inventory → Environment list
- Required for Access_Matrix (columns D-G are dynamic based on environments)


### Output to Other Assessments

**To ISMS-IMP-A.8.31.3 (Compliance Dashboard):**

- Sheet 4: Developer production access count (critical metric)
- Sheet 8: All gap data (for consolidated compliance scoring)
- Sheet 4, 5, 6, 7: Compliance status (for overall compliance score)


### Output to Python Scripts

**generate_a831_2_environment_access.py** generates this workbook:

- Creates all 9 sheets with proper structure
- Applies cell styling and conditional formatting
- Includes data validation and sample data
- Exports to `.xlsx` format


---

## Workbook Metadata

**File Name:** `A831-2-Environment-Access-Control-Assessment-YYYY-MM-DD.xlsx`

**Properties:**

- Title: ISMS-IMP-A.8.31.2 - Environment Access Control Assessment
- Subject: ISO/IEC 27001:2022 Control A.8.31
- Author: [Organization] ISMS Team
- Comments: Technology-agnostic environment access control assessment - ZERO DEVELOPER PRODUCTION ACCESS
- Keywords: ISO27001, A.8.31, access control, production access, IAM, RBAC, MFA


**Protection:**

- Sheet structure protected (prevent accidental deletion)
- User input cells unlocked (yellow cells editable)
- Formula cells locked (summary metrics, conditional formatting)
- Header rows locked


---

**END OF SPECIFICATION**

---

*"We should be careful to get out of an experience only the wisdom that is in it."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-01-31 -->
