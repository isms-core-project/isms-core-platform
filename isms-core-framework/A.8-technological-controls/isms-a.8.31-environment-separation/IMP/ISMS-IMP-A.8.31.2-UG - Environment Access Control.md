<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.31.2-UG:framework:UG:a.8.31.2 -->
**ISMS-IMP-A.8.31.2-UG - Environment Access Control Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.31: Separation of Development, Test and Production Environments

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Environment Access Control |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.31.2-UG |
| **Related Policy** | ISMS-POL-A.8.31 (Environment Separation) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.31 (Separation of Development, Test and Production Environments) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.8.31 (Environment Separation)
- ISMS-IMP-A.8.31.1 (Environment Architecture Implementation)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.31.2-TG.

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | User Environment Access Matrix | Map user access rights across development, test and production |
| 3 | Developer Production Access | Assess and control developer access to production environments |
| 4 | Production Credential Audit | Audit credentials with production environment access |
| 5 | Cross Environment Access Log | Log and review cross-environment access activities |
| 6 | Break Glass Access Log | Track and review emergency break glass access to production |
| 7 | MFA Enforcement | Assess MFA enforcement for environment access |
| 8 | Evidence Register | Store and reference evidence supporting assessments |
| 9 | Summary Dashboard | Compliance status and key metrics overview |
| 10 | Approval Sign-Off | Management review sign-off and certification |

---

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
- Verify unauthorised access attempts monitored and alerted
- Document access review frequency

**Outputs:**

- Audit logging status per environment
- Access monitoring procedures documented
- Alert configuration verified

**Common Pitfalls to Avoid:**

- ❌ Audit logs not retained (e.g., only 7 days - need 90+ days)
- ❌ Logs not monitored (collection without review is useless)
- ❌ No alerts for unauthorised access attempts

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
1. Fill in assessment metadata (date, completed by, organisation)
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
   - Who can activate? (authorised approvers)
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
   - Alerts configured? (unauthorised access attempts)
   - Access review frequency (weekly, monthly, quarterly)

**Time:** 1-2 hours

**Tips:**

- Audit logs must be enabled for production (MANDATORY)
- Retention period: minimum 90 days (regulatory requirement may be longer)
- Logs without monitoring = compliance checkbox (not security)
- Unauthorised access attempts should trigger alerts

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
- ✅ Alerts for unauthorised access

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

**Impact:** HIGH security risk - unauthorised access possible

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
- Configure alerts for unauthorised access attempts
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
- [ ] All evidence collected and organised

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
- [ ] Evidence organised in structured folder
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
- Security incident (unauthorised access) - document as gap
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

**END OF USER GUIDE**

---

*"The controls that protect production should never be tested in production."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
