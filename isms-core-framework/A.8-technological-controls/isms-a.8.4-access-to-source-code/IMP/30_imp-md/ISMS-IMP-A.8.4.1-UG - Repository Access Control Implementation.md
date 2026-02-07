**ISMS-IMP-A.8.4.1-UG - Repository Access Control Implementation**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.4: Access to Source Code

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.4.1-UG |
| **Version** | 1.0 |
| **Assessment Area** | Repository Access Control and Compliance |
| **Related Policy** | ISMS-POL-A.8.4, Section 2.1 (Repository Access Management), Section 2.2 (Repository Classification), Section 2.3 (Role-Based Access Control) |
| **Purpose** | Document repository inventory, access permissions, and access control compliance in a technology-independent manner |
| **Target Audience** | Repository Owners, Development Team Leads, Information Security Team, IT Operations, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Repository Access Control assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.4.1-TG.

---

**Audience:** Repository Owners, Development Team Leads, Security Team, IT Operations

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.4.1 - Repository Access Control Implementation

#### What This Assessment Covers

This assessment documents source code repository ACCESS CONTROL - WHO has access to WHICH repositories with WHAT permissions. This is the foundational assessment that answers:

- What repositories exist in the organization?
- Who has access to each repository?
- What access level does each user have? (read, write, admin)
- Is access appropriately justified?
- Are quarterly access reviews being completed?
- Is access being removed when people leave?

#### Key Principle

This assessment is **completely technology-agnostic and platform-independent**. You document YOUR specific repository platforms (GitHub, GitLab, Bitbucket, Azure DevOps, self-hosted Git, SVN, Perforce, whatever), and verify access controls against generic policy requirements.

**This is NOT about:**

- Branch protection rules (covered in IMP-S2)
- Code quality or secure coding (covered in A.8.25-26-29)
- Backup/recovery procedures (covered in policy)

**This IS about:**

- Repository inventory (do we know what repos exist?)
- User access management (who can access what?)
- Access appropriateness (should they have that access?)
- Access lifecycle (request → approval → provision → review → deprovision)

#### What You'll Document

- **Repository Inventory**: Every source code repository across all platforms
- **User Access Matrix**: Every user's access to every repository
- **Access Requests**: Approval records and justifications
- **Access Reviews**: Quarterly reviews and findings
- **Deprovisioning**: Access removal when people leave
- **Third-Party Access**: Contractors, auditors, offshore teams
- **Service Accounts**: CI/CD, automation, security scanners
- **Compliance Scoring**: Overall access control compliance metrics
- **Gaps**: Identified issues and remediation plans
- **Evidence**: Supporting documentation for audit

#### How This Relates to Other A.8.4 Assessments

| Assessment            | Focus                    | Relationship to A.8.4.1             |
|-----------------------|--------------------------|--------------------------------------|
| **ISMS-IMP-A.8.4.1** | **Access Control**       | **WHO can access WHAT repositories** |
| ISMS-IMP-A.8.4.2     | Branch Protection        | Code review and merge controls       |
| ISMS-IMP-A.8.4.3     | Overall Assessment       | Consolidated compliance view         |

This assessment (A.8.4.1) focuses specifically on ACCESS MANAGEMENT. Complete this first before assessing branch protection or consolidated compliance.

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Repository Owners** - Approve access, conduct reviews
2. **Development Team Leads** - Validate team access needs
3. **Information Security Team** - Audit access appropriateness
4. **IT Operations / DevOps** - Provision/deprovision access
5. **HR / People Ops** - Provide termination notifications

#### Required Skills

- Understanding of your organization's repository platforms
- Administrator access to repository platforms (for exports)
- Familiarity with organizational roles and teams
- Understanding of least privilege principle
- Ability to identify appropriate vs. excessive access

#### Time Commitment

- **Initial assessment:** 8-12 hours (gather data from all platforms)
- **Quarterly updates:** 2-4 hours (update access matrix, conduct reviews)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Complete repository inventory** - Every repo documented with classification
2. ✅ **User access matrix** - Every user → repository access level
3. ✅ **Access justifications** - Why each person has access
4. ✅ **Review records** - Quarterly reviews completed and documented
5. ✅ **Deprovisioning logs** - Access removal tracked
6. ✅ **Third-party tracking** - Contractor access managed
7. ✅ **Service account inventory** - Automation accounts documented
8. ✅ **Compliance score** - Overall access control compliance percentage
9. ✅ **Gap analysis** - Issues identified with remediation plans
10. ✅ **Evidence register** - Supporting documentation for audit
11. ✅ **Approved assessment** - Three-level approval completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Repository Platform Access

- **Administrator access** to all repository platforms (GitHub, GitLab, Bitbucket, Azure DevOps, etc.)
- **API access** or ability to export data (repository lists, user access)
- **Audit log access** for access change history
- **User management console** access

#### 2. Organizational Information

- **Organization chart** showing teams and reporting structure
- **Employee roster** with roles and departments
- **Contractor list** with contract dates and assigned repositories
- **HR termination list** (last 90 days) to verify deprovisioning

#### 3. Documentation

- **Repository classification scheme** (if exists)
- **Access request approval records** (tickets, emails)
- **Previous access review records** (if exists)
- **NDA signature records** for personnel with code access
- **Service account inventory** (CI/CD accounts, deployment tools)

#### 4. Tools You'll Use

- **Excel or compatible spreadsheet application**
- **Repository platform admin console** (GitHub Settings, GitLab Admin, etc.)
- **Command line tools** (GitHub CLI, GitLab CLI - optional but helpful)
- **API scripts** (optional - for large organizations with 100+ repos)

### Common Data Sources

#### GitHub

- Organization Settings → People (user list)
- Organization Settings → Repositories (repository list)
- Repository → Settings → Collaborators and teams (per-repo access)
- GitHub CLI: `gh repo list <org> --limit 1000`
- GitHub CLI: `gh api /orgs/<org>/repos` (API export)

#### GitLab

- Admin Area → Users (user list)
- Admin Area → Projects (project list)
- Project → Settings → Members (per-project access)
- GitLab CLI: `glab repo list`
- GitLab API: `/api/v4/projects`

#### Bitbucket

- Workspace settings → Users and groups
- Repository settings → User and group access
- Bitbucket API: `/2.0/repositories/<workspace>`

#### Azure DevOps

- Organization Settings → Users
- Project Settings → Repositories
- Azure DevOps CLI: `az repos list`

### Skills Assessment

**Before you begin, ensure you can:**

- [ ] Export repository list from your platform
- [ ] Export user access permissions from your platform
- [ ] Identify repository owners for each repository
- [ ] Access historical approval records
- [ ] Contact HR for termination records
- [ ] Navigate Excel and create simple formulas

**If you answered NO to any item**, get help from:

- Platform administrator (for exports)
- Repository owners (for ownership info)
- Security team (for guidance on least privilege)
- IT support (for Excel assistance)

---

## Assessment Workflow

### Overview of Process

```
Step 1: Gather Data
  ↓
Step 2: Create Repository Inventory
  ↓
Step 3: Build User Access Matrix
  ↓
Step 4: Document Access Justifications
  ↓
Step 5: Conduct Access Review
  ↓
Step 6: Verify Deprovisioning
  ↓
Step 7: Calculate Compliance
  ↓
Step 8: Identify Gaps
  ↓
Step 9: Collect Evidence
  ↓
Step 10: Obtain Approvals
```

### Detailed Workflow

#### Step 1: Gather Data (2-3 hours)

**What to do:**
1. Export repository lists from all platforms
2. Export user access permissions for all repositories
3. Gather access request approval records
4. Obtain HR termination list (last 90 days)
5. Identify service accounts in use
6. Collect contractor access records

**Outputs:**

- Raw exports from GitHub/GitLab/Bitbucket/Azure DevOps
- Access approval tickets/emails
- HR termination notifications
- Service account list

#### Step 2: Create Repository Inventory (1-2 hours)

**What to do:**
1. List all repositories in Sheet 1: Repository_Inventory
2. For each repository, document:

   - Repository name
   - Platform (GitHub, GitLab, etc.)
   - Repository owner (accountable person)
   - Classification (Production, Internal Tools, Open Source, Archived)
   - Description/purpose
   - Primary programming language
   - Number of contributors
   - Last commit date (is it active?)

3. Verify completeness (did you capture ALL repos?)

**Quality check:**

- Every repository from platform exports is documented
- No duplicate entries
- Every repository has an owner assigned
- Classifications are appropriate

#### Step 3: Build User Access Matrix (3-4 hours)

**What to do:**
1. In Sheet 2: User_Access_Matrix, create one row per user-per-repository
2. For each access grant, document:

   - Username
   - Full name
   - Role/title
   - Employment type (employee, contractor, auditor)
   - Repository name
   - Access level (Read, Write, Admin)
   - Access grant date
   - Access expiration (if time-bound)
   - Access justification
   - Last access date (if available)

3. Mark access status: ✅ Appropriate / ⚠️ Excessive / ❌ Orphaned / 🕒 Expired

**Special cases:**

- **Service accounts**: Mark employment type as "Service Account"
- **Former employees**: Should be marked ❌ Orphaned
- **Contractors past end date**: Should be marked 🕒 Expired
- **Admin access without justification**: Should be marked ⚠️ Excessive

**Quality check:**

- Every user with access is documented
- Access levels match platform reality (not assumptions)
- Justifications are specific (not generic "needs access")
- Status assessments are honest

#### Step 4: Document Access Justifications (1-2 hours)

**What to do:**
1. For each access grant, verify justification
2. If no justification exists, contact repository owner
3. Document in Sheet 3: Access_Request_Log:

   - Request date
   - Requestor
   - Repository
   - Access level
   - Approver
   - Approval date
   - Ticket/email reference

**Missing approvals:**

- Flag as gap in Gap_Analysis sheet
- Work with repository owners to document retroactive justification
- For critical repositories, escalate to CISO

#### Step 5: Conduct Access Review (1-2 hours)

**What to do:**
1. Review User_Access_Matrix for appropriateness
2. Identify:

   - Users with excessive access (admin when write would suffice)
   - Users with access to multiple repos without justification
   - Users with write access who haven't committed in 90+ days
   - Orphaned accounts (former employees still having access)
   - Expired contractor access still active

3. Document findings in Sheet 4: Access_Review_Log:

   - Review date
   - Repository reviewed
   - Reviewer name
   - Number of users reviewed
   - Findings (excessive, orphaned, expired)
   - Actions taken (access reduced, removed)
   - Completion date

#### Step 6: Verify Deprovisioning (1 hour)

**What to do:**
1. Obtain HR termination list (last 90 days)
2. Cross-reference with User_Access_Matrix
3. For each terminated employee, verify:

   - Access was removed from ALL repositories
   - Removal happened within 24 hours of termination
   - Removal is documented

4. Document in Sheet 5: Deprovisioning_Log:

   - Termination date
   - Username
   - Repositories accessed (before termination)
   - Access removal date
   - Removal verification date
   - Compliant timeline? (✅ Yes if <24 hours, ❌ No if >24 hours)

**Red flags:**

- Terminated employee still has access (major gap)
- Access removed >24 hours after termination
- No documentation of removal

#### Step 7: Calculate Compliance (automated)

**What happens:**

- Sheet 7: Compliance_Scoring automatically calculates:
  - Repository inventory completeness (100% target)
  - Appropriate access rate (≥95% target)
  - Orphaned account rate (0% target)
  - Access review completion (100% target)
  - Deprovisioning SLA compliance (≥95% target)
  - **Overall Score** (weighted average)

**What you do:**

- Review calculated scores
- Understand what's driving low scores
- Plan remediation if score <85%

#### Step 8: Identify Gaps (1-2 hours)

**What to do:**
1. Review all sheets for non-compliant items
2. In Sheet 8: Gap_Analysis, document each gap:

   - What is the gap? (orphaned account, missing approval, etc.)
   - Which policy requirement is not met?
   - What is the risk?
   - How will it be remediated?
   - Who is responsible?
   - When will it be fixed?

3. Prioritize gaps: 🔴 Critical > 🟠 High > 🟡 Medium > 🟢 Low
4. Create remediation plan with target dates

**Critical gaps** (require immediate action):

- Former employees with production repository access
- External contractors with admin access
- No access reviews completed in 90+ days
- Multiple orphaned accounts

#### Step 9: Collect Evidence (1 hour)

**What to do:**
1. In Sheet 9: Evidence_Register, log all supporting evidence:

   - Platform exports (CSV, JSON)
   - Access approval tickets
   - Review completion reports
   - Deprovisioning logs
   - Configuration screenshots

2. Save evidence files in organized structure:
   ```
   Evidence/
   ├── Platform_Exports/
   │   ├── GitHub_repos_2026-01-25.csv
   │   ├── GitHub_access_2026-01-25.csv
   │   └── GitLab_projects_2026-01-25.json
   ├── Approvals/
   │   ├── Ticket_12345_access_request.pdf
   │   └── Email_approval_contractor.pdf
   ├── Reviews/
   │   └── Q4_2025_access_review_report.xlsx
   └── Deprovisioning/
       └── HR_terminations_Q4_2025.xlsx
   ```
3. Document file locations in Evidence_Register

#### Step 10: Obtain Approvals (1-2 days elapsed time)

**What to do:**
1. Complete Sheet 10: Approval_Sign_Off
2. Submit to approvers in sequence:

   - **Repository Owners** (first) - verify data accuracy
   - **Information Security Manager** - verify compliance
   - **CISO** - final approval

3. Each approver signs, dates, and provides comments
4. If rejected, address findings and resubmit
5. Once approved, file assessment as official record

**Approval criteria:**

- Repository inventory is complete and accurate
- User access matrix reflects current state
- Compliance score is calculated correctly
- Gaps are documented with remediation plans
- Evidence is collected and organized

---

## Completing Each Sheet

### Sheet 1: Repository_Inventory

**Purpose:** Document every source code repository across all platforms.

#### When to Complete
Complete this sheet FIRST - you need the repository inventory before assessing access.

#### How to Gather Data

**Option 1: Platform Web UI Export**

- GitHub: Organization Settings → Repositories → Export (if available)
- GitLab: Admin Area → Projects → Export list
- Bitbucket: Settings → Export projects
- Azure DevOps: Project Settings → Repositories → Export

**Option 2: API/CLI Export (Recommended for >50 repos)**
```bash
# GitHub
gh repo list myorg --limit 1000 --json name,owner,visibility,pushedAt > github_repos.json

# GitLab
glab repo list --output-format json > gitlab_projects.json

# Azure DevOps
az repos list --organization https://dev.azure.com/myorg --output table > azdo_repos.txt
```

**Option 3: Manual Inventory** (Only for small organizations <10 repos)

- Navigate to each platform
- List repositories manually in spreadsheet

#### Completing the Columns

**Column A - Repository Name**: Exact name as it appears in platform

- Example: `backend-api`, `mobile-app-ios`, `infrastructure-terraform`
- Use lowercase with hyphens (common convention)
- **Avoid:** Typos, abbreviations, nicknames

**Column B - Platform**: Where repository is hosted

- Dropdown: GitHub Cloud, GitHub Enterprise, GitLab SaaS, GitLab Self-Hosted, Bitbucket Cloud, Bitbucket Server, Azure DevOps, AWS CodeCommit, Other
- **Tip:** If you have multiple GitHub orgs, specify which org

**Column C - Repository URL**: Full HTTPS URL to repository

- Example: `https://github.com/myorg/backend-api`
- **Why:** Auditors need direct link to verify existence

**Column D - Repository Owner**: Person accountable for this repository

- Format: Full Name (email@company.com)
- **Not:** Generic "Dev Team" - need specific person
- **Who:** Usually tech lead, product owner, or architect
- **Role:** Approves access requests, conducts reviews

**Column E - Classification**: Repository sensitivity level

- Dropdown: 🔴 Production, 🟡 Internal Tools, 🟢 Open Source, ⚪ Archived
- **Production:** Code deployed to customer-facing systems
- **Internal Tools:** Internal automation, utilities, scripts
- **Open Source:** Public or open source contributions
- **Archived:** No longer actively developed
- **Tip:** When in doubt, classify as Production (safer)

**Column F - Description**: Brief purpose of repository

- Example: "Customer-facing REST API for order management"
- **Good:** Specific, explains business purpose
- **Bad:** "API" (too vague), "Code" (useless)

**Column G - Primary Language**: Main programming language

- Dropdown: JavaScript, Python, Java, C#, Go, Ruby, PHP, Other
- **Why:** Helps identify repositories needing specific skills

**Column H - Number of Contributors**: How many people commit code

- Number: Count of unique contributors in last 12 months
- **Source:** GitHub Insights, GitLab Contributors
- **Why:** High contributor count = more access to review

**Column I - Last Commit Date**: When was code last changed

- Date format: YYYY-MM-DD
- **Source:** Repository main branch last commit
- **Why:** Identifies dead repositories that should be archived

**Column J - Active Status**: Is repository actively developed?

- Dropdown: ✅ Active, 🕒 Maintenance, ❌ Archived, ❓ Unknown
- **Active:** Commits in last 30 days
- **Maintenance:** Commits every 60-90 days
- **Archived:** No commits in 180+ days
- **Unknown:** Can't determine (investigate)

**Column K - Branch Protection Enabled**: Are protected branches configured?

- Dropdown: ✅ Yes, ❌ No, N/A (single-person repo)
- **Source:** Repository Settings → Branches → Protected branches
- **Note:** Detailed branch protection assessed in IMP-S2

**Column L - Secret Scanning Enabled**: Is automated secret detection active?

- Dropdown: ✅ Yes, ❌ No
- **Source:** Repository Settings → Security → Secret scanning
- **Why:** Critical for preventing credential leaks

**Column M - Backup Status**: Is repository backed up?

- Dropdown: ✅ Yes, ❌ No, ❓ Unknown
- **Source:** IT Operations backup documentation
- **Why:** Disaster recovery requirement

**Column N - Notes**: Any additional relevant information

- Free text: Exceptions, special considerations, planned changes

**Quality Checks:**

- [ ] Every repository from platform exports is listed
- [ ] No duplicate entries
- [ ] Every repository has an owner assigned (no blanks)
- [ ] Classifications are appropriate (ask repository owner if unsure)
- [ ] All URLs are valid (test a few randomly)
- [ ] Active status matches last commit date
- [ ] Backup status verified with IT Operations

---

### Sheet 2: User_Access_Matrix

**Purpose:** Document WHO has access to WHICH repositories with WHAT permissions.

#### When to Complete
Complete AFTER Sheet 1 (Repository_Inventory) is done.

#### How to Gather Data

**Option 1: Platform Access Export**
```bash
# GitHub - export org members and repo access
gh api /orgs/myorg/members > members.json
for repo in $(gh repo list myorg --json name -q '.[].name'); do
  gh api /repos/myorg/$repo/collaborators > ${repo}_collaborators.json
done

# GitLab - export project members
glab api /projects/:id/members --paginate > project_members.json

# Manual consolidation required - no single export
```

**Option 2: Manual Platform Review** (Small organizations)

- For each repository, navigate to Settings → Access
- List each user with their permission level
- Consolidate into spreadsheet

**Important:** This sheet can become VERY large (users × repositories). For organizations with 100+ users and 100+ repositories, consider breaking into multiple sheets by platform or team.

#### Completing the Columns

**Column A - Username**: Platform username

- Example: `jsmith`, `john.smith@company.com`
- **Exact match** to platform username
- **Why:** Used for lookup and correlation

**Column B - Full Name**: Employee's legal/preferred name

- Example: John Smith
- **Source:** HR system, Active Directory
- **Why:** Auditors need to identify people

**Column C - Email**: Primary work email

- Example: john.smith@company.com
- **Why:** Contact for access verification

**Column D - Role/Title**: Job title or role

- Example: Senior Backend Developer, DevOps Engineer
- **Source:** HR system, org chart
- **Why:** Helps justify access level

**Column E - Department/Team**: Organizational unit

- Example: Engineering - Platform Team
- **Why:** Team-based access patterns

**Column F - Employment Type**: Employment relationship

- Dropdown: 👤 Employee, 🤝 Contractor, 🔍 Auditor, ⚙️ Service Account, 🏢 Third-Party
- **Employee:** Full-time, part-time, intern
- **Contractor:** External individual or agency staff
- **Auditor:** Security auditors, ISO auditors
- **Service Account:** CI/CD, automation, bots
- **Third-Party:** Offshore teams, partner companies

**Column G - Contract End Date** (for contractors): When contract expires

- Date format: YYYY-MM-DD
- **Source:** Procurement, contractor agreements
- **Critical:** Access should be removed on this date
- Leave blank for employees (permanent access)

**Column H - Repository Name**: Which repository does user access

- **Must match** Sheet 1 Repository_Inventory Column A exactly
- **Why:** Used for VLOOKUP formulas in compliance scoring

**Column I - Access Level**: What permissions does user have

- Dropdown: 👁️ Read, ✏️ Write, 🔧 Admin
- **Read:** View-only (clone, browse)
- **Write:** Commit, push, create branches, submit PRs
- **Admin:** Repository settings, access management, deletion
- **Map platform-specific roles:**
  - GitHub: Read = Read, Triage = Read, Write = Write, Maintain = Admin, Admin = Admin
  - GitLab: Guest = Read, Reporter = Read, Developer = Write, Maintainer = Admin, Owner = Admin
  - Bitbucket: Read = Read, Write = Write, Admin = Admin

**Column J - Access Grant Date**: When was access first granted

- Date format: YYYY-MM-DD
- **Source:** Approval ticket creation date, platform audit log
- **If unknown:** Use estimate (better than blank)

**Column K - Access Expiration Date** (if time-bound): When access should end

- Date format: YYYY-MM-DD
- **For contractors:** Should match Column G (Contract End Date)
- **For auditors:** Audit completion date + 7 days
- **For employees:** Leave blank (permanent access)

**Column L - Access Justification**: Why does user need this access

- Free text: Specific business reason
- **Good examples:**
  - "Backend developer working on authentication service"
  - "DevOps engineer - deploys to production via CI/CD"
  - "Security auditor - Q4 2025 ISO 27001 certification audit"
- **Bad examples:**
  - "Needs access" (too generic)
  - "Developer" (obvious, not specific)
  - "Request approved" (circular logic)
- **If missing:** Contact repository owner for clarification

**Column M - Approval Reference**: Where is approval documented

- Format: Ticket ID, email subject, or document reference
- Example: "JIRA TICKET-1234", "Email from Jane Doe 2025-11-15", "Approved in Slack #dev-access"
- **Why:** Auditors will verify approvals exist

**Column N - Last Access Date** (if available): When user last accessed repo

- Date format: YYYY-MM-DD
- **Source:** Platform analytics (GitHub Insights, GitLab Usage)
- **Not always available:** Some platforms don't track
- **Why:** Identifies dormant access (write access, no commits in 90+ days)

**Column O - Access Status**: Is access appropriate?

- Dropdown: ✅ Appropriate, ⚠️ Excessive, ❌ Orphaned, 🕒 Expired
- **Appropriate:** User needs this access, level is correct
- **Excessive:** Access level too high (admin when write would suffice)
- **Orphaned:** Former employee still has access
- **Expired:** Time-bound access past end date
- **How to assess:**

  1. Does user's role justify access? (Backend dev accessing backend repo = appropriate)
  2. Is access level minimum required? (Admin only for repo config, not for code changes)
  3. Is user still employed? (Check HR records)
  4. Is access expired? (Check Column K vs. current date)

**Column P - Review Date**: When was this access last reviewed

- Date format: YYYY-MM-DD
- **Source:** Sheet 4 Access_Review_Log
- **Target:** Quarterly (every 90 days)
- **If blank:** Access has never been reviewed (gap)

**Column Q - Notes**: Additional context

- Free text: Exceptions, special circumstances, planned changes

**Quality Checks:**

- [ ] Every user with platform access is listed
- [ ] Repository names match Sheet 1 exactly (no typos)
- [ ] Access levels match platform reality (verify sample)
- [ ] Employment type is accurate (check HR records)
- [ ] Contractor end dates are documented
- [ ] Justifications are specific (not generic)
- [ ] Approval references exist for high-privilege access (admin to production)
- [ ] Access status assessments are honest (not all "appropriate")
- [ ] Former employees are marked "Orphaned" if access remains

**Common Errors to Avoid:**
1. ❌ Assuming access is appropriate without verification
2. ❌ Marking admin access as appropriate without strong justification
3. ❌ Missing orphaned accounts (not cross-checking with HR terminations)
4. ❌ Ignoring expired contractor access
5. ❌ Blanket "developer" justifications (be specific)

---

### Sheet 3: Access_Request_Log

**Purpose:** Document access request and approval workflow compliance.

#### When to Complete
Complete this AS YOU DOCUMENT access requests found in ticketing system, email, etc.

#### How to Gather Data

- Search ticketing system (ServiceNow, Jira) for repository access requests
- Search email for access approval communications
- Check repository platform notification history
- Interview repository owners for recent access grants

#### Completing the Columns

**Column A - Request ID**: Unique identifier for this request

- Format: REQ-001, REQ-002, etc. OR platform ticket ID
- Example: "JIRA-1234" or "REQ-045"

**Column B - Request Date**: When access was requested

- Date format: YYYY-MM-DD
- Source: Ticket creation date, email timestamp

**Column C - Requestor**: Who requested access

- Format: Full Name (username)
- Should match Column B in User_Access_Matrix

**Column D - Repository Name**: Which repository

- Must match Sheet 1 Column A exactly

**Column E - Access Level Requested**: What permission level

- Dropdown: Read, Write, Admin

**Column F - Business Justification**: Why access is needed

- Copy from request ticket or email
- Should be specific (not generic "needs access")

**Column G - Approver**: Who approved the request

- Format: Full Name (repository owner, manager)
- Should match repository owner from Sheet 1 or manager

**Column H - Approval Date**: When request was approved

- Date format: YYYY-MM-DD
- Should be AFTER request date

**Column I - Provisioned By**: Who granted the access

- Format: Full Name (IT Operations, DevOps)

**Column J - Provisioned Date**: When access was actually granted

- Date format: YYYY-MM-DD
- Should be within 24 hours of approval date

**Column K - Approval Reference**: Where is approval documented

- Format: Ticket URL, email subject, document location
- Example: "https://jira.company.com/browse/ACCESS-1234"

**Column L - Compliant Timeline**: Was provisioning within SLA?

- Dropdown: ✅ Yes (if <24 hours), ❌ No (if >24 hours)
- Formula: =IF((Column J - Column H)<=1,"✅ Yes","❌ No")

**Column M - Notes**: Any exceptions or special circumstances

**Quality Checks:**

- [ ] Request dates are before approval dates
- [ ] Approval dates are before provisioning dates
- [ ] Provisioning within 24 hours for 95%+ of requests
- [ ] Approvers are appropriate (repository owners, managers)
- [ ] Business justifications are documented (not blank)

---

### Sheet 4: Access_Review_Log

**Purpose:** Document quarterly access review completion.

#### When to Complete
Complete this DURING and AFTER quarterly access reviews.

#### Quarterly Access Review Process

**What is an access review?**

- Systematic review of WHO has access to WHICH repositories
- Goal: Identify excessive, orphaned, or inappropriate access
- Frequency: Every 90 days (quarterly)

**How to conduct:**
1. Generate User_Access_Matrix for repository
2. Repository owner reviews each user's access
3. For each user, ask: "Should they still have this access? Is the level appropriate?"
4. Document findings (excessive, orphaned, inappropriate)
5. Remove/reduce access as needed
6. Document completion in Access_Review_Log

#### Completing the Columns

**Column A - Review ID**: Unique identifier

- Format: REV-2025-Q4-001, REV-2025-Q4-002

**Column B - Review Period**: Which quarter

- Format: Q1 2025, Q2 2025, Q3 2025, Q4 2025

**Column C - Repository Name**: Which repository was reviewed

- Must match Sheet 1 Column A

**Column D - Repository Owner**: Who conducted review

- Should match repository owner from Sheet 1

**Column E - Review Date**: When review was completed

- Date format: YYYY-MM-DD

**Column F - Number of Users Reviewed**: How many users had access

- Number: Count from User_Access_Matrix for this repository

**Column G - Findings - Appropriate Access**: Users with correct access

- Number: Count of ✅ Appropriate in User_Access_Matrix

**Column H - Findings - Excessive Access**: Users with too much access

- Number: Count of ⚠️ Excessive
- Example: User has Admin but only needs Write

**Column I - Findings - Orphaned Accounts**: Former employees still with access

- Number: Count of ❌ Orphaned
- Critical finding - should be 0

**Column J - Findings - Expired Access**: Time-bound access past end date

- Number: Count of 🕒 Expired

**Column K - Actions Taken**: What was done to address findings

- Free text: "Removed access for 2 former employees, reduced 1 admin to write"

**Column L - Completion Status**: Is review complete?

- Dropdown: ✅ Complete, 🕒 In Progress, ❌ Overdue

**Column M - Next Review Due Date**: When is next review due

- Date format: YYYY-MM-DD
- Formula: =Column E + 90 days

**Column N - Evidence Reference**: Where is review documented

- File name or location of review report

**Quality Checks:**

- [ ] Reviews completed every 90 days (quarterly)
- [ ] All repositories have been reviewed
- [ ] Findings are documented (not just "all appropriate")
- [ ] Actions taken for excessive/orphaned/expired access
- [ ] Evidence is saved

---

### Sheet 5: Deprovisioning_Log

**Purpose:** Verify access is removed when people leave the organization.

#### When to Complete
Complete this AFTER obtaining HR termination list and verifying access removal.

#### Completing the Columns

**Column A - Termination ID**: Unique identifier

- Format: TERM-001, TERM-002

**Column B - Termination Date**: Date of employment end

- Date format: YYYY-MM-DD
- Source: HR notification

**Column C - Employee Name**: Who left

- Format: Full Name

**Column D - Username**: Platform username

- Should match User_Access_Matrix Column A

**Column E - Employment Type**: What type of worker

- Dropdown: Employee, Contractor, Auditor

**Column F - Reason for Departure**: Why they left

- Dropdown: Resignation, Termination, Contract End, Retirement, Other

**Column G - Repositories Accessed**: How many repos did they have access to

- Number: Count from User_Access_Matrix

**Column H - Repository List**: Which repositories (comma-separated)

- Text: repo1, repo2, repo3

**Column I - Access Level**: What access did they have

- Text: Read (5 repos), Write (3 repos), Admin (1 repo)

**Column J - Deprovisioning Ticket**: Ticket tracking access removal

- Ticket ID or reference

**Column K - Access Removal Date**: When access was actually removed

- Date format: YYYY-MM-DD
- Source: Platform audit logs

**Column L - Removal Verified By**: Who verified removal

- Name of person who checked

**Column M - Verification Date**: When verification completed

- Date format: YYYY-MM-DD

**Column N - Compliant Timeline**: Was removal within 24 hours?

- Dropdown: ✅ Yes (if <24 hours), ❌ No (if >24 hours)
- Formula: =IF((Column K - Column B)<=1,"✅ Yes","❌ No")

**Column O - Notes**: Any issues or delays

**Quality Checks:**

- [ ] All HR terminations (last 90 days) are listed
- [ ] Access removal dates are documented (not blank)
- [ ] 95%+ removals within 24 hours
- [ ] Verification completed for all
- [ ] No former employees still have access

---

### Sheet 6: Third_Party_Access

**Purpose:** Track contractor, auditor, and third-party access with time-bound expiration.

#### When to Complete
Complete this CONCURRENTLY with User_Access_Matrix for all non-employee access.

#### Completing the Columns

**Column A - Third Party ID**: Unique identifier

- Format: TP-001, TP-002

**Column B - Company Name**: Contracting organization

- Example: Acme Consulting, ISO Auditing Services

**Column C - Individual Name**: Specific person

- Format: Full Name

**Column D - Username**: Platform username

**Column E - Role/Purpose**: Why do they need access

- Example: "Backend development contractor", "ISO 27001 certification auditor"

**Column F - Contract Start Date**: When contract began

- Date format: YYYY-MM-DD

**Column G - Contract End Date**: When contract ends

- Date format: YYYY-MM-DD

**Column H - Repository Name**: Which repository

**Column I - Access Level**: What permission

- Dropdown: Read, Write, Admin

**Column J - NDA Signed**: Is confidentiality agreement in place?

- Dropdown: ✅ Yes, ❌ No
- Required for ALL third-party access

**Column K - NDA Date**: When NDA was signed

- Date format: YYYY-MM-DD

**Column L - NDA File Location**: Where is NDA stored

- Path or file reference

**Column M - Access Status**: Current status

- Dropdown: ✅ Active, 🕒 Expired, ❌ Revoked

**Column N - Auto-Expire Date**: When will access auto-expire

- Date format: YYYY-MM-DD
- Should match Contract End Date

**Column O - Access Reviewed**: Last review date

- Date format: YYYY-MM-DD
- Should be monthly (more frequent than quarterly for third-parties)

**Column P - Notes**: Special conditions or requirements

**Quality Checks:**

- [ ] All contractors have NDAs signed
- [ ] Contract end dates are documented
- [ ] Access expires automatically on contract end date
- [ ] Monthly reviews completed (more frequent than standard quarterly)
- [ ] No access extended past contract without new approval

---

### Sheet 7: Service_Accounts

**Purpose:** Inventory automation accounts (CI/CD, deployment, security scanners).

#### When to Complete
Complete this BY IDENTIFYING all non-human accounts in User_Access_Matrix and documenting their purpose.

#### Completing the Columns

**Column A - Account ID**: Unique identifier

- Format: SA-001, SA-002

**Column B - Account Name**: Service account username

- Example: cicd-bot, deploy-automation, security-scanner

**Column C - Account Type**: What kind of automation

- Dropdown: CI/CD, Deployment, Security Scanner, Backup, Monitoring, Other

**Column D - Purpose**: What does this account do

- Example: "GitHub Actions CI/CD pipeline for backend-api"

**Column E - Repository Name**: Which repository

**Column F - Access Level**: What permission

- Dropdown: Read, Write, Admin

**Column G - Access Justification**: Why this access level

- Example: "Write required to push tags, Admin for branch protection updates"

**Column H - Owner**: Who is responsible for this account

- Name of person/team

**Column I - Authentication Method**: How does account authenticate

- Dropdown: Personal Access Token, SSH Key, OAuth App, GitHub App, Deploy Key

**Column J - Token/Key Expiration**: When does credential expire

- Date format: YYYY-MM-DD
- Target: Annual rotation minimum

**Column K - Secret Storage Location**: Where is credential stored

- Example: "GitHub Secrets", "Azure Key Vault", "HashiCorp Vault"

**Column L - Last Rotation Date**: When was credential last rotated

- Date format: YYYY-MM-DD

**Column M - Next Rotation Due**: When is rotation required

- Date format: YYYY-MM-DD
- Formula: =Column L + 365 days (annual)

**Column N - Quarterly Review Date**: When was account last reviewed

- Date format: YYYY-MM-DD

**Column O - Still Required**: Is account still needed?

- Dropdown: ✅ Yes, ❌ No (remove if No)

**Column P - Notes**: Additional information

**Quality Checks:**

- [ ] All service accounts are documented (not mixed with human users)
- [ ] Each account has a clear purpose
- [ ] Each account has an owner
- [ ] Credentials are stored securely (not hardcoded)
- [ ] Credentials rotated annually minimum
- [ ] Quarterly reviews confirm continued need

---

### Sheet 8: Compliance_Scoring

**Purpose:** Calculate overall access control compliance score (automated).

#### What Happens Here
This sheet contains FORMULAS that automatically calculate compliance metrics based on data in other sheets. You don't manually enter data here - just review the calculated scores.

#### Metrics Calculated

**1. Repository Inventory Completeness**

- Formula: (Repos in Sheet 1 / Total repos in platforms) × 100%
- Target: 100%
- Why: Ensures all repositories are tracked

**2. Access Control Compliance**

- Formula: (Repos with RBAC / Total repos) × 100%
- Target: 100%
- Why: Ensures access control is implemented

**3. Appropriate Access Rate**

- Formula: (✅ Appropriate / Total access grants) × 100%
- Target: ≥95%
- Why: Measures access appropriateness

**4. Orphaned Account Rate**

- Formula: (❌ Orphaned / Total users) × 100%
- Target: 0%
- Why: Former employees shouldn't have access

**5. Access Review Completion Rate**

- Formula: (Reviews completed / Total repos) × 100%
- Target: 100%
- Why: Quarterly reviews required for all repos

**6. Deprovisioning SLA Compliance**

- Formula: (Removals <24hrs / Total removals) × 100%
- Target: ≥95%
- Why: Access removed promptly when people leave

**7. Overall Compliance Score**

- Formula: Weighted average of above metrics
- Weights: Inventory 15%, Access Control 20%, Appropriate Access 25%, Orphaned 15%, Reviews 15%, Deprovisioning 10%
- Target: ≥85%

#### Risk Categorization

- 🟢 Low Risk: Score ≥85%
- 🟡 Medium Risk: Score 70-84%
- 🔴 High Risk: Score <70%

#### What To Do
1. Review calculated scores
2. Identify metrics below target
3. Understand root causes (check source sheets)
4. Plan remediation for low scores
5. Document in Gap_Analysis sheet

---

### Sheet 9: Gap_Analysis

**Purpose:** Document gaps and remediation plans.

#### When to Complete
Complete this AFTER reviewing all other sheets and identifying non-compliant items.

#### Completing the Columns

**Column A - Gap ID**: Unique identifier

- Format: GAP-001, GAP-002

**Column B - Gap Category**: Type of gap

- Dropdown: Access Control, Inventory, Reviews, Deprovisioning, Documentation

**Column C - Gap Description**: What is the problem

- Example: "5 former employees still have write access to production repositories"

**Column D - Policy Requirement**: Which requirement is not met

- Example: "ISMS-POL-A.8.4 Section 2.1 - Access revoked upon termination"

**Column E - Current State**: What is happening now

- Example: "HR sends termination notice, but no process to remove repository access"

**Column F - Desired State**: What should happen

- Example: "Automated deprovisioning within 24 hours of HR notification"

**Column G - Risk Level**: Severity of gap

- Dropdown: 🔴 Critical, 🟠 High, 🟡 Medium, 🟢 Low

**Column H - Impact**: What is the risk

- Example: "Former employees could access confidential source code or commit malicious code"

**Column I - Affected Repositories**: Which repos

- List: repo1, repo2, repo3 or "All production repositories"

**Column J - Root Cause**: Why does gap exist

- Example: "No integration between HR system and repository platforms"

**Column K - Remediation Plan**: How will it be fixed

- Example: "Implement automated deprovisioning script triggered by HR termination webhook"

**Column L - Responsible Party**: Who will fix it

- Name: John Smith (DevOps Lead)

**Column M - Target Completion Date**: When will it be fixed

- Date format: YYYY-MM-DD

**Column N - Estimated Effort**: How long will it take

- Dropdown: 1-2 hours, 1 day, 1 week, 2-4 weeks, >1 month

**Column O - Status**: Current progress

- Dropdown: 🔴 Open, 🟡 In Progress, 🟢 Completed, ⚪ Deferred

**Column P - Actual Completion Date**: When was it actually fixed

- Date format: YYYY-MM-DD

**Column Q - Verification Method**: How was fix verified

- Example: "Tested HR termination workflow, verified access removed within 2 hours"

**Column R - Verification Date**: When was verification completed

- Date format: YYYY-MM-DD

**Column S - Notes**: Additional information

**Quality Checks:**

- [ ] All gaps from Compliance_Scoring are documented
- [ ] Risk levels are accurate (don't downplay critical issues)
- [ ] Remediation plans are specific and actionable
- [ ] Target dates are realistic
- [ ] Responsible parties are assigned
- [ ] Critical gaps have near-term target dates (<30 days)

---

### Sheet 10: Evidence_Register

**Purpose:** Track evidence for audit purposes.

#### Completing the Columns

**Column A - Evidence ID**: Unique identifier

- Format: EV-001, EV-002

**Column B - Evidence Type**: What kind of evidence

- Dropdown: Access Report, Approval Record, Review Report, Deprovisioning Log, Configuration Screenshot, NDA, Other

**Column C - Evidence Description**: What is this evidence

- Example: "GitHub organization user access export for Q4 2025"

**Column D - Related Requirement**: Which policy requirement

- Example: "ISMS-POL-A.8.4 Section 2.3 - Role-based access control"

**Column E - Evidence Date**: When was evidence created

- Date format: YYYY-MM-DD

**Column F - Evidence Source**: Where did it come from

- Example: "GitHub API export", "ServiceNow ticket system"

**Column G - File Name**: Name of file

- Example: `github_access_export_2025-12-31.csv`

**Column H - File Location**: Where is it stored

- Path: `\\fileserver\ISMS\Evidence\A.8.4\Q4-2025\` or SharePoint URL

**Column I - Collected By**: Who collected it

- Name

**Column J - Collection Date**: When was it collected

- Date format: YYYY-MM-DD

**Column K - Evidence Format**: File type

- Dropdown: Excel, PDF, CSV, Screenshot, Email, JSON, Other

**Column L - Retention Period**: How long to keep

- Text: "3 years" (per policy requirement)

**Column M - Retention End Date**: When can it be purged

- Date format: YYYY-MM-DD

**Column N - Auditor Reviewed**: Has auditor seen this

- Dropdown: ✅ Yes, ❌ No, ⏳ Pending

**Column O - Auditor Comments**: What did auditor say

**Column P - Notes**: Additional information

**Required Evidence:**

- Repository inventory exports (GitHub, GitLab, etc.)
- User access permission exports
- Access request approval tickets
- Quarterly access review reports
- HR termination notifications
- Deprovisioning logs with timestamps
- NDA signatures for all code access
- Branch protection configuration screenshots
- MFA enforcement screenshots
- Service account token rotation logs

---

### Sheet 11: Approval_Sign_Off

**Purpose:** Formal approval of completed assessment.

#### When to Complete
Complete this LAST, after all other sheets are finished and reviewed.

#### Approval Process

**Step 1: Self-Review**
Before submitting for approval, complete quality checklist (see section below).

**Step 2: Repository Owner Review**

- Submit assessment to all repository owners whose repos are included
- Repository owners verify:
  - Repository information is accurate
  - User access matrix is current
  - Access justifications are documented
  - Gaps identified are valid
- Repository owners sign and date

**Step 3: Information Security Manager Review**

- Information Security Manager verifies:
  - Assessment is complete (no missing data)
  - Compliance scoring is calculated correctly
  - Gaps are appropriately categorized by risk
  - Remediation plans are reasonable
  - Evidence is collected
- Information Security Manager provides recommendation: Approve / Approve with Conditions / Reject

**Step 4: CISO Final Approval**

- CISO reviews overall compliance status
- CISO approves or rejects with conditions
- If score <70% (High Risk), CISO may require immediate remediation before approval

#### Completing the Approval Section

**Assessment Summary:**

- Assessment Period: Q4 2025
- Assessment Completion Date: 2025-12-31
- Overall Compliance Score: 87% (from Sheet 8)
- Risk Level: 🟢 Low Risk

**Assessment Completed By:**

- Name: [Your name]
- Role/Title: [Your title]
- Department: [Your department]
- Date: [Completion date]
- Signature: [Your signature]

**Repository Owner Approvals** (3-5 signature blocks):

- Name: [Repository owner name]
- Date: [Approval date]
- Signature: [Signature]

**Information Security Manager Review:**

- Name: [ISM name]
- Date: [Review date]
- Review Notes: [Comments]
- Recommendation: [Approve / Approve with Conditions / Reject]

**CISO Approval:**

- Name: [CISO name]
- Date: [Approval date]
- Approval Decision: [Approved / Approved with Conditions / Rejected]
- Conditions/Notes: [Any conditions]

**Next Scheduled Review:** [Completion Date + 90 days]

---

## Evidence Collection

### Evidence Categories

**1. Platform Exports**

- Repository lists (GitHub, GitLab, Bitbucket, Azure DevOps)
- User access permissions (who has access to what)
- Audit logs (access changes, permission modifications)
- Branch protection configurations
- MFA enrollment status

**2. Approval Records**

- Access request tickets (ServiceNow, Jira)
- Email approvals from repository owners
- Approval workflows from platforms

**3. Review Documentation**

- Quarterly access review reports
- Finding documentation (excessive, orphaned, expired access)
- Remediation records showing fixes

**4. Deprovisioning Evidence**

- HR termination notifications
- Access removal logs with timestamps
- Verification of removal completion

**5. Configuration Evidence**

- Screenshots of branch protection settings
- Screenshots of MFA enforcement
- Service account credential rotation logs

**6. Contractual Documentation**

- NDA signatures for ALL personnel with code access
- Contractor agreements showing access dates
- Third-party service agreements

### Evidence Naming Conventions

Use consistent naming for easy organization:

```
Format: [Platform]_[Type]_[Date].[ext]

Examples:
GitHub_RepoList_2025-12-31.csv
GitHub_AccessMatrix_2025-12-31.json
GitLab_Projects_2025-12-31.json
Approval_Ticket_JIRA-1234.pdf
AccessReview_Q4-2025_backend-api.xlsx
Deprovisioning_2025-12-31_JohnSmith.pdf
NDA_JaneSmith_2025-01-15.pdf
BranchProtection_backend-api_2025-12-31.png
```

### Evidence Storage Structure

Organize evidence in folders:

```
Evidence_A.8.4_Repository_Access_Control/
├── Quarter_Q4_2025/
│   ├── 1_Platform_Exports/
│   │   ├── GitHub_RepoList_2025-12-31.csv
│   │   ├── GitHub_AccessMatrix_2025-12-31.json
│   │   ├── GitLab_Projects_2025-12-31.json
│   │   └── Bitbucket_Repositories_2025-12-31.csv
│   ├── 2_Approvals/
│   │   ├── Approval_Ticket_JIRA-1234.pdf
│   │   ├── Approval_Email_RepoAccess_2025-11-15.pdf
│   │   └── EmergencyAccess_Approval_2025-12-20.pdf
│   ├── 3_Reviews/
│   │   ├── AccessReview_Q4-2025_backend-api.xlsx
│   │   ├── AccessReview_Q4-2025_mobile-app.xlsx
│   │   └── ReviewSummary_Q4-2025.pdf
│   ├── 4_Deprovisioning/
│   │   ├── HR_Terminations_Q4-2025.xlsx
│   │   ├── Deprovisioning_2025-12-15_JohnSmith.pdf
│   │   └── DeproVERIFICATION_Q4-2025.xlsx
│   ├── 5_Configurations/
│   │   ├── BranchProtection_backend-api_2025-12-31.png
│   │   ├── MFA_Enforcement_GitHub_2025-12-31.png
│   │   └── ServiceAccount_Tokens_2025-12-31.xlsx
│   ├── 6_NDAs/
│   │   ├── NDA_JaneSmith_2025-01-15.pdf
│   │   ├── NDA_AcmeConsulting_2025-03-01.pdf
│   │   └── NDA_Register_2025.xlsx
│   └── Assessment_Workbook_Q4-2025.xlsx
└── [Previous quarters follow same structure]
```

### Evidence Quality Criteria

**Good Evidence:**

- ✅ Complete (no missing data)
- ✅ Current (dated within assessment period)
- ✅ Authentic (from official systems)
- ✅ Traceable (can verify source)
- ✅ Understandable (clear labels/context)

**Poor Evidence:**

- ❌ Partial exports (missing data)
- ❌ Outdated (from months ago)
- ❌ Screenshots of screenshots (low quality)
- ❌ Unlabeled files (what is this?)
- ❌ Personal interpretations (not raw data)

### Evidence Collection Tips

**Platform Exports:**

- Export in CSV or JSON (not just screenshots)
- Include all columns (don't filter)
- Export with timestamps
- Document export method (UI, CLI, API)

**Approval Records:**

- Capture full ticket (not just approval)
- Include approval chain (all approvers)
- Preserve timestamps
- Screenshot AND save PDF

**Reviews:**

- Save completed review workbooks
- Document reviewer identity
- Timestamp completion
- Keep before/after access reports

---

## Common Pitfalls

### Pitfall 1: Incomplete Repository Inventory

**Problem:** Only documenting "known" or "active" repositories, missing archived, personal, or test repositories.

**Why It Happens:**

- Only checking main organization
- Missing personal forks
- Forgetting archived repos
- Not checking all platforms (GitHub AND GitLab AND Bitbucket)

**How to Avoid:**

- Use API exports (don't rely on manual lists)
- Check ALL repository platforms
- Include archived repositories
- Cross-check with IT asset inventory

**Consequence:** Auditors find repositories not in inventory = inventory incomplete = audit finding.

---

### Pitfall 2: "Everyone's Access Is Appropriate"

**Problem:** Marking all access as "✅ Appropriate" without actually verifying.

**Why It Happens:**

- Assuming current state is correct
- Not wanting to create work (finding issues)
- Trust that "someone checked it before"
- Fear of questioning developers

**Reality Check:**
In every organization with >50 employees:

- ~10-20% of access is excessive (admin when write would do)
- ~5-10% of orphaned accounts exist (former employees)
- ~15-25% of justifications are generic ("developer")

**How to Avoid:**

- Actually ask "Does this person NEED this access?"
- Challenge admin access (should be rare)
- Cross-check with HR termination lists
- Require specific justifications

**Consequence:** False sense of security, audit finding when auditor spot-checks and finds issues.

---

### Pitfall 3: Missing Deprovisioning Verification

**Problem:** Assuming access was removed when employee left, not actually verifying.

**Why It Happens:**

- Trust that "IT handles it"
- No process to verify
- HR doesn't notify repository administrators
- Manual process prone to error

**Reality Check:**
In organizations WITHOUT automated deprovisioning:

- ~50% of terminations result in repository access NOT being removed
- Access lingers for weeks or months
- Former employees CAN still access code

**How to Avoid:**

- Obtain HR termination list
- ACTUALLY CHECK platform access
- Cross-reference with User_Access_Matrix
- Document findings honestly

**Consequence:** Former employees with active access = critical security gap = major audit finding.

---

### Pitfall 4: Generic Justifications

**Problem:** Access justifications like "Developer" or "Needs access" that don't explain WHY.

**Why It Happens:**

- Copy-paste justifications
- Lazy approval process
- No understanding of least privilege

**Examples of Bad Justifications:**

- "Developer" (what are they developing?)
- "Needs access" (why?)
- "Team member" (which team, what role?)
- "Request approved" (circular logic)

**Examples of Good Justifications:**

- "Backend developer - implements authentication features in backend-api repository"
- "DevOps engineer - deploys backend-api to production via GitHub Actions"
- "Security auditor - Q4 2025 ISO 27001 certification audit, read-only access expires 2026-01-15"

**How to Avoid:**

- Require specific justifications in access request process
- Train repository owners on least privilege
- Review justifications during quarterly access reviews
- Flag generic justifications as gaps

**Consequence:** Can't defend access appropriateness to auditors.

---

### Pitfall 5: Not Tracking Service Accounts

**Problem:** Service accounts (CI/CD, bots) not documented separately, mixed with human users, or completely missing.

**Why It Happens:**

- Service accounts look like users (have usernames)
- Created ad-hoc by developers
- No central tracking
- "It's just automation"

**Reality Check:**
Service accounts often have ADMIN access (most privileged). If compromised, attacker has full control. Must be:

- Documented separately
- Reviewed quarterly
- Credentials rotated annually
- Stored securely (not hardcoded)

**How to Avoid:**

- Identify service accounts in User_Access_Matrix (employment type = Service Account)
- Document in dedicated Service_Accounts sheet
- Include in quarterly reviews
- Verify credential rotation

**Consequence:** Undocumented service accounts with admin access = critical gap.

---

### Pitfall 6: Quarterly Reviews "On Paper Only"

**Problem:** Documenting that reviews were "completed" but not actually reviewing access.

**Why It Happens:**

- Checkbox compliance mentality
- Time pressure
- "Trust but don't verify"

**Red Flags That Review Wasn't Real:**

- 100% appropriate access (unrealistic)
- No findings (always some findings)
- Review completed in 5 minutes for repo with 50 users
- Same findings every quarter (not addressing issues)

**How to Do Real Reviews:**

- Export current access matrix
- Go through user-by-user
- Ask "Should they still have this? Is level appropriate?"
- Document findings honestly
- Take action on findings

**Consequence:** Auditors spot-check review quality, ask detailed questions, find review was superficial = audit finding.

---

### Pitfall 7: Approval Records "Somewhere"

**Problem:** Access approvals exist "somewhere" but can't produce them for audit.

**Why It Happens:**

- Approvals in email (not searchable)
- Old ticketing system
- Verbal approvals (no record)
- "We had a Slack conversation"

**How to Avoid:**

- Centralize approval records (ticketing system)
- Save approval emails to Evidence folder
- Screenshot Slack approvals
- Document verbal approvals in writing (post-facto)
- Reference approval in Access_Request_Log

**Consequence:** Can't prove access was approved = audit finding (improper access grant).

---

### Pitfall 8: Contractor Access Without End Dates

**Problem:** Contractors granted "permanent" access without time-bound expiration.

**Why It Happens:**

- Don't want to track expiration manually
- Platforms don't support automatic expiration (Bitbucket)
- "We'll remove it when contract ends" (but forget)

**Reality Check:**

- Contractors MUST have time-bound access per policy
- Access MUST expire on contract end date
- Manual calendar reminders often forgotten

**How to Avoid:**

- Use platform auto-expiration features (GitHub Enterprise, GitLab)
- If not available, calendar reminders
- Document expiration in Third_Party_Access sheet
- Monthly reviews for third-party access (more frequent than quarterly)

**Consequence:** Contractors with permanent access = policy violation = audit finding.

---

### Pitfall 9: "We'll Fix Gaps After Certification"

**Problem:** Documenting critical gaps but deferring remediation.

**Why It Happens:**

- Resource constraints
- "Let's just get certified first"
- Underestimating audit rigor

**Reality Check:**

- Auditors won't certify if critical gaps exist
- "Compliant with exceptions" is not real compliance
- Critical gaps must be remediated BEFORE certification

**Critical Gaps That MUST Be Fixed:**

- Former employees with production access
- No access reviews in 180+ days
- No deprovisioning process
- Orphaned accounts with admin access

**How to Avoid:**

- Prioritize critical gaps
- Remediate before audit
- Be realistic about readiness
- Don't schedule audit until critical gaps closed

**Consequence:** Audit failure, delayed certification, wasted audit fees.

---

### Pitfall 10: Copy-Paste From Other Organizations

**Problem:** Using another organization's assessment without adapting to YOUR environment.

**Why It Happens:**

- Looking for "shortcut"
- Don't understand assessment purpose
- Think it's just filling in a template

**Reality Check:**

- Auditors verify data accuracy (they'll spot-check)
- Copy-paste generic data = inaccurate assessment
- Your platforms, users, repositories are unique

**How to Avoid:**

- Actually export YOUR data from YOUR platforms
- Document YOUR access, not generic examples
- Verify data accuracy (spot-check repositories)

**Consequence:** Inaccurate assessment = audit finding = loss of credibility.

---

## Quality Checklist

Before submitting assessment for approval, verify:

### Completeness

**Repository Inventory:**

- [ ] All repositories from all platforms are listed
- [ ] No duplicate entries
- [ ] Every repository has an owner assigned
- [ ] Repository classifications are appropriate
- [ ] Active status matches last commit dates
- [ ] URLs are valid

**User Access Matrix:**

- [ ] Every user with access is documented
- [ ] Repository names match Sheet 1 exactly
- [ ] Access levels match platform reality (spot-checked)
- [ ] Employment types are accurate
- [ ] Contractor end dates are documented
- [ ] Justifications are specific (not generic)
- [ ] Approval references exist for high-privilege access
- [ ] Access status assessments are honest

**Access Requests:**

- [ ] High-privilege access requests (admin to production) have approval records
- [ ] Approval chain is documented
- [ ] Provisioning timelines are compliant (95%+ within 24 hours)

**Access Reviews:**

- [ ] All repositories have been reviewed in last 90 days
- [ ] Reviews document findings (not just "all appropriate")
- [ ] Actions taken on findings
- [ ] Evidence saved

**Deprovisioning:**

- [ ] All HR terminations (last 90 days) are listed
- [ ] Access removal verified for each
- [ ] 95%+ removals within 24 hours
- [ ] No former employees still have access

**Third-Party Access:**

- [ ] All contractors/auditors have NDA signatures
- [ ] Contract end dates documented
- [ ] Access expires on contract end
- [ ] Monthly reviews completed

**Service Accounts:**

- [ ] All service accounts identified and documented
- [ ] Each has clear purpose and owner
- [ ] Credentials rotated annually
- [ ] Quarterly reviews confirm continued need

**Compliance Scoring:**

- [ ] All formulas calculate correctly
- [ ] Overall score is accurate
- [ ] Risk categorization is appropriate

**Gap Analysis:**

- [ ] All gaps from compliance scoring are documented
- [ ] Risk levels are accurate
- [ ] Remediation plans are specific and actionable
- [ ] Critical gaps have near-term target dates

**Evidence Register:**

- [ ] All required evidence is collected
- [ ] Files are saved in organized structure
- [ ] File locations are documented
- [ ] Evidence is dated within assessment period

**Approval Sign-Off:**

- [ ] All required signatures obtained
- [ ] Dates are filled in
- [ ] Next review date is scheduled

### Accuracy

- [ ] Repository counts match platform reality
- [ ] User access permissions verified (spot-check 10 users)
- [ ] Employment status verified with HR
- [ ] Termination dates match HR records
- [ ] Contractor end dates match contracts
- [ ] NDA signatures verified
- [ ] Service account credentials are current

### Honesty

- [ ] Access status assessments are realistic (not all "appropriate")
- [ ] Gaps are documented honestly (not hidden)
- [ ] Compliance score reflects reality (not inflated)
- [ ] Findings are documented (not suppressed)

### Auditability

- [ ] All claims can be verified with evidence
- [ ] Evidence is organized and labeled
- [ ] Approval records are accessible
- [ ] Formulas and calculations are transparent
- [ ] Assessment tells coherent story

---

## Review & Approval

### Pre-Submission Checklist

Before submitting for approval:

1. **Self-Review:**

   - [ ] Complete Quality Checklist above
   - [ ] Review all sheets for completeness
   - [ ] Verify formulas calculate correctly
   - [ ] Check for typos, formatting issues
   - [ ] Ensure all evidence is collected

2. **Peer Review** (optional but recommended):

   - [ ] Have colleague review for accuracy
   - [ ] Spot-check 10 random users in User_Access_Matrix
   - [ ] Verify repository inventory completeness
   - [ ] Review gap analysis for realism

3. **Evidence Organization:**

   - [ ] All evidence files saved in folder structure
   - [ ] Evidence_Register sheet is complete
   - [ ] File locations are correct

### Submission Process

**Step 1: Submit to Repository Owners**

- Email assessment workbook to all repository owners whose repos are included
- Request review within 5 business days
- Provide guidance on what to verify

**Step 2: Incorporate Repository Owner Feedback**

- Make corrections as needed
- Document any disputes
- Re-submit if significant changes

**Step 3: Submit to Information Security Manager**

- Once repository owners approve
- ISM reviews for policy compliance
- ISM provides recommendation

**Step 4: Submit to CISO**

- Once ISM approves
- CISO final approval
- If score <70%, CISO may require remediation first

### Approval Timeline

**Typical Timeline:**

- Repository Owner Review: 5 business days
- Information Security Manager Review: 3 business days
- CISO Approval: 2 business days
- **Total: ~2 weeks**

**Expedited Timeline** (if critical gaps exist):

- CISO may require immediate remediation
- Re-submission after gap closure
- Additional 1-2 weeks

### Post-Approval

Once approved:
1. **File Assessment:**

   - Save approved workbook as official record
   - File in ISMS document repository
   - Retain for audit (minimum 3 years)

2. **Communicate Results:**

   - Share compliance score with stakeholders
   - Present gap analysis to leadership
   - Update repository owners on remediation plans

3. **Schedule Next Review:**

   - Calendar reminder for next quarterly review (90 days)
   - Assign responsibility for next assessment
   - Update Review Cycle tracker

4. **Track Remediation:**

   - Monitor gap remediation progress
   - Update Gap_Analysis sheet as gaps close
   - Report progress to CISO monthly

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
