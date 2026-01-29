# ISMS-IMP-A.8.4.2 - Branch Protection Configuration
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Control A.8.4: Access to Source Code

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.4.2 |
| **Version** | 1.0 |
| **Assessment Area** | Branch Protection and Code Review Compliance |
| **Related Policy** | ISMS-POL-A.8.4, Section 2.4 (Branch Protection and Code Review) |
| **Purpose** | Document and assess branch protection configurations across all repository platforms to enforce code review and prevent unauthorized code changes |
| **Target Audience** | Repository Owners, DevOps Engineers, Security Team, Development Team Leads, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Branch Protection assessment workbook | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE** (THIS PART)
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Completing Each Sheet
  - Platform-Specific Configuration Guidance
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION** (SEPARATE FILE)
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Cell Styling Reference
  - Formula Specifications

**Target Audiences:**
- **Part I:** Assessment users (Repository Owners, DevOps, Security Team)
- **Part II:** Workbook developers (Python/Excel script maintainers)

---

# PART I: USER COMPLETION GUIDE

**Audience:** Repository Owners, DevOps Engineers, Development Team Leads, Security Team

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.4.2 - Branch Protection Configuration

#### What This Assessment Covers

This assessment documents BRANCH PROTECTION - technical controls that enforce code review and prevent unauthorized code changes. This answers:

- Are protected branches configured for production repositories?
- What protection rules are enabled? (PR required, reviewers, status checks)
- Are pull requests enforced? (no direct commits to main)
- Are status checks running? (CI/CD tests must pass)
- Is code review happening? (required approvals)
- Are signed commits configured? (commit author verification)

#### Key Principle

This assessment is **completely platform-agnostic**. You document YOUR branch protection configurations on YOUR platform (GitHub, GitLab, Bitbucket, Azure DevOps, etc.) and verify against generic policy requirements.

**This is NOT about:**
- User access permissions (covered in IMP-S1)
- Secure coding practices (covered in A.8.25-26-29)
- What code changes were made (that's development work)

**This IS about:**
- Branch protection RULES (what technical controls exist)
- Pull request ENFORCEMENT (are direct commits blocked)
- Code review REQUIREMENTS (minimum approvals)
- CI/CD INTEGRATION (status checks)

#### What You'll Document

- **Repository Branch Inventory**: Which repositories have which branches requiring protection
- **Branch Protection Details**: Specific protection rules per branch (PR required, approvals, status checks)
- **Pull Request Configuration**: Review requirements and workflow
- **Status Check Verification**: CI/CD integration and test requirements
- **Signed Commit Audit**: GPG signature adoption
- **Exception Management**: Temporary exceptions to protection rules
- **Compliance Scoring**: Overall branch protection compliance metrics
- **Gaps**: Configuration issues and remediation plans
- **Evidence**: Screenshots, configuration exports, PR logs

#### How This Relates to Other A.8.4 Assessments

| Assessment            | Focus                    | Relationship to A.8.4.2             |
|-----------------------|--------------------------|--------------------------------------|
| ISMS-IMP-A.8.4.1     | Access Control           | WHO can access repositories          |
| **ISMS-IMP-A.8.4.2** | **Branch Protection**    | **HOW code changes are controlled**  |
| ISMS-IMP-A.8.4.3     | Overall Assessment       | Consolidated compliance view         |

This assessment (A.8.4.2) focuses specifically on TECHNICAL CONTROLS for code changes. You can have perfect access control (S1) but still have security gaps if developers can push directly to production without review.

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Repository Owners** - Responsible for branch protection configuration
2. **DevOps Engineers** - Implement and maintain CI/CD integrations
3. **Development Team Leads** - Enforce pull request workflows
4. **Security Team** - Audit protection configurations
5. **Platform Administrators** - Manage organization-level defaults

#### Required Skills

- Administrator access to repository platforms
- Understanding of Git branching workflows
- Familiarity with pull request/merge request processes
- Knowledge of CI/CD pipelines and status checks
- Ability to read platform configuration settings

#### Time Commitment

- **Initial assessment:** 6-8 hours (configure + document all repositories)
- **Quarterly updates:** 1-2 hours (verify configurations, update changes)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Branch inventory** - All protected branches documented
2. ✅ **Protection rule matrix** - Every rule documented per repository
3. ✅ **Pull request compliance** - Review requirements verified
4. ✅ **Status check verification** - CI/CD integration confirmed
5. ✅ **Signed commit status** - GPG adoption measured
6. ✅ **Exception tracking** - Temporary exceptions managed
7. ✅ **Compliance score** - Overall protection compliance percentage
8. ✅ **Gap analysis** - Issues identified with remediation plans
9. ✅ **Evidence register** - Configuration screenshots and exports
10. ✅ **Approved assessment** - Three-level approval completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Repository Platform Access

- **Administrator access** to all repository platforms
- **Branch protection configuration access**
- **Ability to view protection rules**
- **API access** for exports (optional but helpful)

#### 2. Repository Information

- **Repository list** from IMP-S1 (Repository_Inventory)
- **Repository classifications** (Production, Internal Tools, etc.)
- **Main branch names** (main, master, develop)
- **Release branch patterns** (release/*, hotfix/*)

#### 3. CI/CD Information

- **CI/CD platform** (GitHub Actions, GitLab CI, Jenkins, etc.)
- **Status check names** (build, test, lint, security-scan)
- **Required checks** per repository type
- **Status check logs** (for verification)

#### 4. Code Review Workflow

- **Pull request templates** (if exists)
- **Code owner files** (CODEOWNERS, .gitlab/CODEOWNERS)
- **Review approval requirements** per repository type
- **Historical PR data** (for enforcement verification)

#### 5. Documentation

- **Platform configuration guides**
- **Organization branch protection policies**
- **Developer workflow documentation**
- **Exception requests** (if any exist)

### Tools You'll Use

- **Excel or compatible spreadsheet application**
- **Repository platform web UI** (GitHub, GitLab, etc.)
- **Command line tools** (gh CLI, glab CLI - optional)
- **Screenshot tool** (for configuration evidence)
- **API clients** (Postman, curl - optional for large orgs)

### Common Data Sources

#### GitHub
- Repository → Settings → Branches → Branch protection rules
- GitHub CLI: `gh api repos/{owner}/{repo}/branches/main/protection`
- Organization → Settings → Repository defaults

#### GitLab
- Project → Settings → Repository → Protected branches
- Project → Settings → Merge requests → Merge request approvals
- GitLab API: `/api/v4/projects/{id}/protected_branches`

#### Bitbucket
- Repository settings → Branch permissions
- Repository settings → Merge checks
- Bitbucket API: `/2.0/repositories/{workspace}/{repo}/branch-restrictions`

#### Azure DevOps
- Project Settings → Repositories → Policies
- Branch policies per branch
- Azure DevOps API: `GET https://dev.azure.com/{org}/{project}/_apis/policy/configurations`

### Skills Assessment

**Before you begin, ensure you can:**
- [ ] Access branch protection settings on your platform
- [ ] Identify main and release branches
- [ ] Understand pull request workflow
- [ ] Navigate CI/CD status check configurations
- [ ] Take screenshots of configurations
- [ ] Export protection rules (via UI or API)

**If you answered NO to any item**, get help from:
- Platform administrator (for access)
- DevOps team (for CI/CD integration)
- Development leads (for PR workflow)

---

## Assessment Workflow

### Overview of Process

```
Step 1: Inventory Protected Branches
  ↓
Step 2: Document Protection Rules
  ↓
Step 3: Assess Pull Request Configuration
  ↓
Step 4: Verify Status Checks
  ↓
Step 5: Audit Signed Commits
  ↓
Step 6: Track Exceptions
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

#### Step 1: Inventory Protected Branches (1-2 hours)

**What to do:**
1. Review Repository_Inventory from IMP-S1 (all repositories)
2. For each repository, identify branches requiring protection:
   - Main/master branch
   - Release branches (release/*, hotfix/*)
   - Other critical branches (develop, staging)
3. Document in Sheet 1: Repository_Branch_Inventory
4. Mark which branches REQUIRE protection per policy

**Outputs:**
- Complete list of repositories with branches
- Classification of branch types (Main, Release, Development)
- Protection requirements per branch type

#### Step 2: Document Protection Rules (2-3 hours)

**What to do:**
1. For each protected branch, navigate to branch protection settings
2. Document enabled protection rules:
   - Direct commits blocked? (Yes/No)
   - Pull request required? (Yes/No)
   - Required approvals? (count: 0, 1, 2+)
   - Dismiss stale reviews? (Yes/No)
   - Code owner review? (Yes/No/N/A)
   - Status checks required? (Yes/No/Partial)
   - Signed commits? (Yes/No/N/A)
   - Linear history? (Yes/No)
3. Enter data in Sheet 2: Branch_Protection_Details
4. Calculate compliance score per branch

**Outputs:**
- Complete protection rule matrix
- Per-branch compliance scores
- Gaps identified (missing rules)

#### Step 3: Assess Pull Request Configuration (1 hour)

**What to do:**
1. Review pull request/merge request settings
2. Document:
   - Minimum reviewers required
   - Code owner review requirement
   - Stale approval dismissal
   - Conversation resolution requirement
   - Self-approval blocking
3. Enter in Sheet 3: Pull_Request_Configuration
4. Verify with recent PR history (spot-check)

**Outputs:**
- PR configuration matrix
- Compliance status per repository

#### Step 4: Verify Status Checks (1-2 hours)

**What to do:**
1. Identify CI/CD pipelines per repository
2. Document required status checks:
   - Build check (compile, build)
   - Test check (unit tests, integration tests)
   - Lint check (code quality)
   - Security check (SAST, SCA, secret scanning)
3. Verify checks are:
   - Configured as required (not optional)
   - Running on every PR
   - Blocking merge if fail
4. Enter in Sheet 4: Status_Check_Verification

**Outputs:**
- Status check inventory
- CI/CD integration compliance
- Missing checks identified

#### Step 5: Audit Signed Commits (1 hour)

**What to do:**
1. Check if signed commits are required
2. For repositories requiring signatures:
   - Sample recent commits (last 30 days)
   - Calculate % of commits that are signed
   - Document GPG infrastructure status
   - Check developer training completion
3. Enter in Sheet 5: Signed_Commits_Audit

**Outputs:**
- Signed commit adoption rate
- GPG infrastructure status
- Training completion status

#### Step 6: Track Exceptions (30 minutes)

**What to do:**
1. Identify any exceptions to branch protection
2. For each exception, document:
   - Which repository/branch
   - Why exception granted
   - Who approved
   - When it expires
   - Next review date
3. Enter in Sheet 6: Exception_Management
4. Flag expired exceptions

**Outputs:**
- Exception register
- Expired exceptions identified
- Review schedule

#### Step 7: Calculate Compliance (automated)

**What happens:**
- Sheet 7: Compliance_Scoring automatically calculates:
  - Branch protection configuration rate (100% target)
  - PR enforcement rate (≥95% target)
  - Status check compliance (100% target)
  - Signed commit adoption (≥80% target)
  - **Overall Score** (weighted average)

**What you do:**
- Review calculated scores
- Understand drivers of low scores
- Plan remediation if score <85%

#### Step 8: Identify Gaps (1 hour)

**What to do:**
1. Review all sheets for non-compliant items
2. In Sheet 8: Gap_Analysis, document each gap:
   - What is missing? (no PR requirement, missing status checks)
   - Which policy requirement not met?
   - What is the risk?
   - How will it be fixed?
   - Who is responsible?
   - When will it be fixed?
3. Prioritize gaps: 🔴 Critical > 🟠 High > 🟡 Medium > 🟢 Low

**Critical gaps** (require immediate action):
- Production repository with no branch protection
- Main branch allows direct commits (no PR requirement)
- No code review required (0 approvals)
- CI/CD tests not blocking merge

#### Step 9: Collect Evidence (1 hour)

**What to do:**
1. Take screenshots of branch protection settings
2. Export protection rules (API or CSV export)
3. Capture recent PR examples showing enforcement
4. Save CI/CD test results
5. Document in Sheet 9: Evidence_Register
6. Organize files in folder structure

**Evidence to collect:**
- Branch protection configuration screenshots
- Protection rule exports (JSON/CSV)
- Recent PR with review enforcement
- CI/CD test logs showing required checks
- Signed commit examples (if applicable)

#### Step 10: Obtain Approvals (1-2 days elapsed time)

**What to do:**
1. Complete Sheet 10: Approval_Sign_Off
2. Submit to approvers:
   - Repository Owners (verify configurations)
   - Information Security Manager (compliance review)
   - CISO (final approval)
3. Address feedback and resubmit if needed

---

## Completing Each Sheet

### Sheet 1: Repository_Branch_Inventory

**Purpose:** Document all branches requiring protection across all repositories.

#### How to Gather Data

**Option 1: Platform Web UI**
- Navigate to each repository
- Identify active branches (not just default branch)
- List main, release, and development branches

**Option 2: Command Line / API**
```bash
# GitHub - list branches
gh api repos/{owner}/{repo}/branches

# GitLab - list protected branches
glab api projects/{id}/protected_branches

# Extract main and release branches
```

#### Completing the Columns

**Column A - Repository Name**: From IMP-S1 Repository_Inventory
- Must match exactly (no typos)

**Column B - Repository Platform**: GitHub, GitLab, Bitbucket, Azure DevOps
- Dropdown selection

**Column C - Repository Classification**: Production Code, Internal Tools, Open Source, Archived
- From IMP-S1 (consistency critical)
- Drives protection requirements

**Column D - Branch Name**: Exact branch name
- Examples: `main`, `master`, `release/v2.1`, `develop`
- Match platform exactly (case-sensitive)

**Column E - Branch Type**: Main, Release, Development, Feature, Hotfix
- **Main**: Primary development branch (main, master)
- **Release**: Production release branches (release/*, hotfix/*)
- **Development**: Integration branch (develop, staging)
- **Feature**: Short-lived feature branches (typically no protection)
- **Hotfix**: Emergency fix branches (release/* pattern)

**Column F - Protection Required**: ✅ Yes, ❌ No, ➖ N/A
- **Per Policy Requirements:**
  - Production + Main branch = ✅ Yes (mandatory)
  - Production + Release branch = ✅ Yes (mandatory)
  - Internal Tools + Main branch = ✅ Yes (mandatory)
  - Internal Tools + Release branch = ✅ Yes
  - Development branches = ❌ No (optional)
  - Feature branches = ➖ N/A (typically not protected)

**Column G - Protection Configured**: ✅ Yes, ❌ No, ⚠️ Partial
- **Check in platform:**
  - GitHub: Settings → Branches → Protected (shows lock icon)
  - GitLab: Settings → Repository → Protected branches (listed)
  - Bitbucket: Settings → Branch permissions (rules exist)
  - Azure DevOps: Policies → Branch policies (policies configured)
- **✅ Yes**: Full protection configured
- **⚠️ Partial**: Some rules enabled, not all
- **❌ No**: No protection configured

**Column H - Status**: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant
- **✅ Compliant**: Protection required AND protection configured
- **⚠️ Partial**: Protection required BUT only partial configuration
- **❌ Non-Compliant**: Protection required BUT not configured
- **Auto-formula**: =IF(F="✅ Yes", IF(G="✅ Yes","✅ Compliant",IF(G="⚠️ Partial","⚠️ Partial","❌ Non-Compliant")),"➖ N/A")

**Quality Checks:**
- [ ] All repositories from IMP-S1 are listed
- [ ] Main branches documented for ALL repos
- [ ] Release branches identified (if exist)
- [ ] Classifications match IMP-S1
- [ ] Protection requirements align with policy
- [ ] All production + main = "Protection Required: ✅ Yes"

---

### Sheet 2: Branch_Protection_Details

**Purpose:** Document specific protection rules for each protected branch.

#### How to Gather Data

**GitHub:**
```bash
# CLI export
gh api repos/{owner}/{repo}/branches/main/protection

# Web UI: Repository → Settings → Branches → [Branch] → Edit
```

**GitLab:**
```bash
# API export
curl --header "PRIVATE-TOKEN: <token>" \
  "https://gitlab.com/api/v4/projects/{id}/protected_branches/main"

# Web UI: Project → Settings → Repository → Protected branches
```

**Bitbucket:**
- Web UI: Repository settings → Branch permissions
- Note: Bitbucket combines permissions in single UI

**Azure DevOps:**
- Web UI: Project Settings → Repositories → Policies → [Branch]

#### Completing the Columns

**Column A - Repository Name**: From Sheet 1

**Column B - Branch Name**: From Sheet 1

**Column C - Direct Commits Blocked**: ✅ Yes, ❌ No
- **What this means**: Can users push directly without PR?
- **GitHub**: "Require a pull request before merging" enabled
- **GitLab**: "Allowed to push" = "No one"
- **Bitbucket**: "Prevent changes without a pull request" checked
- **Azure DevOps**: "Require a minimum number of reviewers" enabled
- **Should be ✅ Yes** for all production main/release branches

**Column D - Pull Request Required**: ✅ Yes, ❌ No
- **Same as Column C** (different phrasing for clarity)
- If direct commits blocked → PR required

**Column E - Required Approvals**: Number (0, 1, 2, 3+)
- **Policy requirements:**
  - Production code: 2 approvals minimum
  - Internal tools: 1 approval minimum
- **GitHub**: "Required approving reviewers"
- **GitLab**: "Approvals required" in merge request settings
- **Bitbucket**: "Require approvals"
- **Azure DevOps**: "Minimum number of reviewers"

**Column F - Dismiss Stale Reviews**: ✅ Yes, ❌ No
- **What this means**: When new commits pushed, old approvals invalidated?
- **GitHub**: "Dismiss stale pull request approvals when new commits are pushed"
- **GitLab**: "Remove all approvals when commits are added"
- **Bitbucket**: "Dismiss approvals when new changes are pushed"
- **Azure DevOps**: "Reset code reviewer votes when there are new changes"
- **Should be ✅ Yes** to prevent approval bypass

**Column G - Code Owner Review Required**: ✅ Yes, ❌ No, ➖ N/A
- **What this means**: Must designated code owner approve?
- **GitHub**: "Require review from Code Owners" + CODEOWNERS file exists
- **GitLab**: "Code owner approval" + CODEOWNERS file exists
- **Bitbucket**: Not natively supported
- **Azure DevOps**: "Automatically include code reviewers"
- **➖ N/A** if no CODEOWNERS file (can't enforce)

**Column H - Status Checks Required**: ✅ Yes, ❌ No, ⚠️ Partial
- **What this means**: Must CI/CD tests pass before merge?
- **GitHub**: "Require status checks to pass before merging" + checks selected
- **GitLab**: "Pipelines must succeed" in merge checks
- **Bitbucket**: "Builds must pass" in merge checks
- **Azure DevOps**: "Build validation" policy
- **⚠️ Partial**: Some checks required, but not all (e.g., only build, not security)

**Column I - Status Check List**: Text (comma-separated)
- **List required checks**:
  - Examples: "build, test, lint, CodeQL"
  - GitHub: Listed in "Status checks found in the last week"
  - GitLab: Pipeline job names required for merge
- **Leave blank if Column H = ❌ No**

**Column J - Signed Commits Required**: ✅ Yes, ❌ No, ➖ N/A
- **What this means**: Must commits be GPG-signed?
- **GitHub**: "Require signed commits"
- **GitLab**: "Reject unsigned commits" (Premium/Ultimate only)
- **Bitbucket**: ➖ N/A (not natively supported)
- **Azure DevOps**: ➖ N/A (not natively supported)
- **➖ N/A** if platform doesn't support OR organization hasn't implemented GPG

**Column K - Linear History Enforced**: ✅ Yes, ❌ No
- **What this means**: Merge commits prevented (squash/rebase only)?
- **GitHub**: "Require linear history"
- **GitLab**: Merge method = "Fast-forward merge"
- **Bitbucket**: Merge strategy setting
- **Azure DevOps**: Branch policies → Merge type
- **Optional** for most organizations (stylistic preference)

**Column L - Compliance Score**: Formula (automated)
- **Calculation**: (Rules enabled / Rules required) × 100%
- **Example for Production Code:**
  - Required: Direct commits blocked, PR required, 2 approvals, dismiss stale, status checks
  - Total: 5 rules
  - Enabled: 4 rules
  - Score: 80%
- **Formula**: See PART II Technical Specification

**Column M - Status**: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant
- **Based on Compliance Score:**
  - ✅ Compliant: 100% (all required rules enabled)
  - ⚠️ Partial: 50-99% (some rules missing)
  - ❌ Non-Compliant: <50% (major gaps)

**Quality Checks:**
- [ ] Every protected branch from Sheet 1 is documented
- [ ] Production main branches have ≥2 required approvals
- [ ] Direct commits blocked for all production branches
- [ ] Status checks required where CI/CD exists
- [ ] Compliance scores calculated correctly

---

### Sheet 3: Pull_Request_Configuration

**Purpose:** Assess pull request workflow configuration.

#### Completing the Columns

**Column A - Repository Name**: From Sheet 1

**Column B - Minimum Reviewers**: Number
- Same as Sheet 2 Column E (Required Approvals)
- Verify consistency

**Column C - Code Owner Review**: ✅ Required, ⚠️ Optional, ❌ No
- **✅ Required**: Enforced via branch protection + CODEOWNERS
- **⚠️ Optional**: CODEOWNERS exists but not enforced
- **❌ No**: No CODEOWNERS file

**Column D - Dismiss Stale Approvals**: ✅ Yes, ❌ No
- Same as Sheet 2 Column F

**Column E - Restrict Dismiss**: ✅ Yes, ❌ No
- **What this means**: Only admins can dismiss reviews?
- **GitHub**: "Restrict who can dismiss pull request reviews"
- **GitLab**: "Prevent approval by author"
- **Purpose**: Prevent developers from dismissing negative reviews

**Column F - Conversation Resolution**: ✅ Required, ⚠️ Optional, ❌ No
- **GitHub**: "Require conversation resolution before merging"
- **GitLab**: "All discussions must be resolved"
- **Bitbucket**: "All tasks must be resolved"
- **Ensures comments addressed before merge**

**Column G - Self-Approval Blocked**: ✅ Yes, ❌ No
- **GitHub**: Pull request author cannot approve own PR (enforced by reviewer count)
- **GitLab**: "Prevent approval by author"
- **Bitbucket**: Author cannot self-approve (default)
- **Should be ✅ Yes** (basic code review principle)

**Column H - Compliance Status**: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant
- **Assessment:**
  - ✅ Compliant: All critical settings correct (reviewers, no self-approval, stale dismiss)
  - ⚠️ Partial: Some settings missing
  - ❌ Non-Compliant: Major gaps (0 reviewers, self-approval allowed)

---

### Sheet 4: Status_Check_Verification

**Purpose:** Document CI/CD status checks.

#### How to Gather Data

**Check CI/CD Platform:**
- GitHub Actions: `.github/workflows/*.yml`
- GitLab CI: `.gitlab-ci.yml`
- Bitbucket Pipelines: `bitbucket-pipelines.yml`
- Azure Pipelines: `azure-pipelines.yml`
- Jenkins: `Jenkinsfile`

**Verify in Branch Protection:**
- Which checks are REQUIRED (not just running)

#### Completing the Columns

**Column A - Repository Name**: From Sheet 1

**Column B - Status Checks Configured**: ✅ Yes, ❌ No
- **✅ Yes**: CI/CD pipeline exists AND at least one check is required
- **❌ No**: No CI/CD OR checks not required

**Column C - Build Check**: ✅ Configured, ❌ Missing
- **Build/Compile check** exists and required?
- Common names: "build", "compile", "ci"

**Column D - Test Check**: ✅ Configured, ❌ Missing
- **Unit test / integration test** check exists and required?
- Common names: "test", "unit-tests", "integration-tests"

**Column E - Lint Check**: ✅ Configured, ❌ Missing
- **Code quality / linter** check exists and required?
- Common names: "lint", "eslint", "pylint", "rubocop"

**Column F - Security Check**: ✅ Configured, ❌ Missing
- **Security scanning** check exists and required?
- Common names: "CodeQL", "Snyk", "security-scan", "SAST"

**Column G - All Checks Must Pass**: ✅ Yes, ❌ No
- **Are checks BLOCKING merge?**
- GitHub: "Require status checks to pass" enabled
- GitLab: "Pipelines must succeed" enabled
- If ❌ No, checks are advisory only (not enforced)

**Column H - Up-to-Date Before Merge**: ✅ Yes, ❌ No
- **Must branch be up-to-date with main before merge?**
- GitHub: "Require branches to be up to date before merging"
- GitLab: Handled by merge method
- Prevents merge conflicts

**Column I - Compliance Status**: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant
- **Assessment:**
  - ✅ Compliant: Build + Test configured, checks blocking
  - ⚠️ Partial: Some checks missing (no security scan)
  - ❌ Non-Compliant: No checks OR not blocking

---

### Sheet 5: Signed_Commits_Audit

**Purpose:** Track signed commit adoption.

#### How to Gather Data

**Check Platform Support:**
- GitHub: Native GPG support
- GitLab: Native GPG support
- Bitbucket: Limited support
- Azure DevOps: Not natively supported

**Sample Recent Commits:**
```bash
# GitHub - check commit signatures
gh api repos/{owner}/{repo}/commits --paginate | jq '.[] | {sha: .sha, verified: .commit.verification.verified}'

# GitLab - check signatures
curl --header "PRIVATE-TOKEN: <token>" \
  "https://gitlab.com/api/v4/projects/{id}/repository/commits" \
  | jq '.[] | {id: .id, signature: .signature}'
```

#### Completing the Columns

**Column A - Repository Name**: From Sheet 1

**Column B - Signed Commits Required**: ✅ Yes, ❌ No, ➖ N/A
- Same as Sheet 2 Column J
- **➖ N/A** if platform doesn't support

**Column C - % Commits Signed (Last 30 days)**: Number (0-100%)
- **Sample last 50-100 commits**
- **Count verified signatures**
- **Calculate percentage**
- **Target: ≥80%** if required

**Column D - GPG Infrastructure**: ✅ Implemented, ⚠️ Partial, ❌ Missing
- **✅ Implemented**: GPG keys distributed, developers trained, enforcement active
- **⚠️ Partial**: Keys distributed but not enforced, or partial adoption
- **❌ Missing**: No GPG infrastructure

**Column E - Developer Training**: ✅ Completed, ⚠️ In Progress, ❌ Not Started
- **Training on:**
  - GPG key generation
  - Key upload to platform
  - Git configuration for auto-signing
  - Troubleshooting signature issues

**Column F - Compliance Status**: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant
- **Assessment:**
  - ✅ Compliant: Required AND ≥80% signed
  - ⚠️ Partial: Required BUT 50-79% signed
  - ❌ Non-Compliant: Required BUT <50% signed

---

### Sheet 6: Exception_Management

**Purpose:** Track branch protection exceptions.

#### When Exceptions Are Granted

**Valid reasons:**
- Emergency production hotfix (time-bound, <24 hours)
- Platform migration (temporary during cutover)
- Legacy repository being decommissioned (archive instead)
- Technical limitation (platform doesn't support feature)

**Invalid reasons:**
- "Too much work to configure" (not acceptable)
- "Developers don't like it" (not acceptable)
- "We've always done it this way" (not acceptable)

#### Completing the Columns

**Column A - Exception ID**: Unique identifier
- Format: EXC-001, EXC-002

**Column B - Repository/Branch**: Which repository and branch
- Format: "backend-api / main"

**Column C - Exception Reason**: Business justification
- **Be specific**: "Emergency hotfix for production outage - direct commit allowed for 4 hours"
- **Not acceptable**: "Need to bypass protection"

**Column D - Granted By**: Approver name
- CISO approval required for production exceptions

**Column E - Grant Date**: When exception granted
- Date format: YYYY-MM-DD

**Column F - Expiration Date**: When exception expires
- **All exceptions must expire** (no permanent exceptions)
- Emergency: <24 hours
- Technical workaround: <90 days
- Migration: <30 days

**Column G - Review Date**: Next review date
- **Before expiration** (monthly for long exceptions)

**Column H - Status**: 🟢 Active, 🔴 Expired, ⚪ Revoked
- **🔴 Expired**: Expiration date passed (CRITICAL - must remediate)
- **🟢 Active**: Current and valid
- **⚪ Revoked**: Ended early (remediation completed)

**Quality Checks:**
- [ ] No expired exceptions (all 🔴 must be addressed)
- [ ] All exceptions have expiration dates (no "permanent")
- [ ] CISO approval documented for production exceptions
- [ ] Monthly review scheduled for active exceptions

---

### Sheet 7: Compliance_Scoring

**Purpose:** Calculate overall branch protection compliance score (automated).

#### Metrics Calculated

**1. Branch Protection Configuration Rate**
- Formula: (Repositories with full protection / Total production repos) × 100%
- Target: 100%
- Source: Sheet 2 (Column M = ✅ Compliant)

**2. Pull Request Enforcement Rate**
- Formula: (Repositories with PR enforcement / Total repos) × 100%
- Target: ≥95%
- Source: Sheet 2 (Column D = ✅ Yes)

**3. Status Check Compliance Rate**
- Formula: (Repos with status checks / Repos with CI/CD) × 100%
- Target: 100%
- Source: Sheet 4 (Column I = ✅ Compliant)

**4. Signed Commit Adoption Rate**
- Formula: Average of Column C across all repos requiring signatures
- Target: ≥80%
- Source: Sheet 5 (Column C)

**5. Overall Branch Protection Score**
- Formula: (Configuration Rate × 40%) + (PR Enforcement × 30%) + (Status Checks × 20%) + (Signed Commits × 10%)
- Target: ≥85%

#### Risk Categorization
- 🟢 Low Risk: Score ≥85%
- 🟡 Medium Risk: Score 70-84%
- 🔴 High Risk: Score <70%

---

### Sheet 8: Gap_Analysis

**Purpose:** Document gaps and remediation plans.

#### Common Gaps

**Gap 1: No Branch Protection on Production Repository**
- Risk: 🔴 Critical
- Impact: Developers can push directly to production without review
- Remediation: Enable branch protection on main branch immediately

**Gap 2: Zero Required Approvals**
- Risk: 🔴 Critical
- Impact: No code review happening
- Remediation: Set minimum 2 reviewers for production, 1 for internal tools

**Gap 3: Status Checks Not Blocking**
- Risk: 🟠 High
- Impact: Tests can fail but merge proceeds
- Remediation: Enable "Require status checks to pass"

**Gap 4: Stale Reviews Not Dismissed**
- Risk: 🟡 Medium
- Impact: Approval given for v1 of code, v2 merged without re-review
- Remediation: Enable "Dismiss stale approvals"

**Gap 5: No Security Checks**
- Risk: 🟠 High
- Impact: Security vulnerabilities not caught before merge
- Remediation: Add CodeQL, Snyk, or similar to required checks

#### Completing the Columns

Same structure as IMP-S1 Gap_Analysis sheet:
- Gap ID, Description, Policy Requirement
- Risk Level, Impact, Remediation Plan
- Responsible Party, Target Date, Status

---

### Sheet 9: Evidence_Register

**Purpose:** Track evidence for audit.

#### Required Evidence

**Configuration Evidence:**
- Branch protection settings screenshots (per platform)
- Protection rule exports (JSON/CSV)
- Organization-level defaults (if applicable)

**Enforcement Evidence:**
- Recent PR showing review enforcement (attempt to merge without approval = blocked)
- CI/CD test logs showing required checks
- Example of stale approval dismissal

**Signed Commit Evidence:**
- Sample signed commits (with "Verified" badge)
- GPG key registry
- Developer training records

**Exception Evidence:**
- Exception request approvals
- Exception review meeting notes
- Remediation completion records

#### Evidence Naming

```
Format: [Platform]_[Type]_[RepoName]_[Date].[ext]

Examples:
GitHub_BranchProtection_backend-api_2025-12-31.png
GitLab_ProtectedBranches_Export_2025-12-31.json
GitHub_PR_ReviewEnforcement_Example_2025-12-15.png
Jenkins_StatusChecks_Build_Log_2025-12-20.pdf
```

---

### Sheet 10: Approval_Sign_Off

**Purpose:** Final approval workflow.

Same structure as IMP-S1:
- Assessment summary with overall score
- Completed by (your signature)
- Repository Owner approvals
- Information Security Manager review
- CISO final approval
- Next review date (90 days)

---

## Platform-Specific Configuration Guidance

### GitHub Branch Protection

**Navigate to Settings:**
1. Repository → Settings → Branches
2. "Add rule" or edit existing rule
3. Branch name pattern: `main`

**Critical Settings for Production:**
- ✅ Require a pull request before merging
  - Required approvals: 2
  - ✅ Dismiss stale pull request approvals
  - ✅ Require review from Code Owners (if CODEOWNERS exists)
- ✅ Require status checks to pass before merging
  - Select checks: build, test, lint, security
  - ✅ Require branches to be up to date
- ✅ Require conversation resolution before merging
- ✅ Require signed commits (if GPG implemented)
- ✅ Include administrators

**Verification:**
```bash
gh api repos/{owner}/{repo}/branches/main/protection
```

### GitLab Protected Branches

**Navigate to Settings:**
1. Project → Settings → Repository
2. Protected branches → Expand
3. Select branch: `main`

**Critical Settings for Production:**
- Allowed to merge: Developers + Maintainers
- Allowed to push: No one
- ✅ Code owner approval (if CODEOWNERS exists)

**Merge Request Settings:**
1. Settings → Merge requests
2. Merge checks:
   - ✅ Pipelines must succeed
   - ✅ All threads must be resolved
3. Merge request approvals:
   - Approvals required: 2 (production), 1 (internal tools)
   - ✅ Prevent approval by author
   - ✅ Remove all approvals when commits are added

**Verification:**
```bash
glab api projects/{id}/protected_branches/main
```

### Bitbucket Branch Permissions

**Navigate to Settings:**
1. Repository settings → Branch permissions
2. Add a branch permission
3. Branch pattern: `main`

**Critical Settings:**
- Type: Write access
- ✅ Prevent deletion
- ✅ Prevent changes without a pull request
- ✅ Require approvals: 2
- ✅ Dismiss approvals when new changes are pushed

**Merge Checks:**
- Repository settings → Merge checks
- ✅ Builds must pass
- ✅ All tasks must be resolved

### Azure DevOps Branch Policies

**Navigate to Settings:**
1. Project Settings → Repositories → Policies
2. Select branch: `main`

**Critical Settings:**
- ✅ Require a minimum number of reviewers: 2
- ✅ Prohibit the most recent pusher from approving
- ✅ Require at least one approval
- ✅ Build validation (select pipeline)
- ✅ Automatically include code reviewers (if configured)

---

## Evidence Collection

### Evidence Categories

1. **Branch Protection Configuration**
   - Screenshots of protection settings
   - JSON/CSV exports of rules
   - Organization defaults

2. **Pull Request Enforcement**
   - Blocked merge attempts (no approval)
   - Review workflow examples
   - Code owner review examples

3. **Status Check Integration**
   - CI/CD pipeline configurations
   - Required check lists
   - Test result examples

4. **Signed Commits**
   - Verified commit examples
   - GPG key registry
   - Training completion records

5. **Exception Management**
   - Exception requests with approvals
   - Review meeting notes
   - Remediation records

### Evidence Storage

```
Evidence_A.8.4_Branch_Protection/
├── Quarter_Q4_2025/
│   ├── 1_Configurations/
│   │   ├── GitHub_Protection_backend-api_2025-12-31.png
│   │   ├── GitLab_Protection_Export_2025-12-31.json
│   │   └── Bitbucket_Permissions_2025-12-31.png
│   ├── 2_PR_Enforcement/
│   │   ├── GitHub_PR_ReviewRequired_Example.png
│   │   ├── GitLab_MR_ApprovalBlocked_Example.png
│   │   └── PR_Statistics_2025-Q4.xlsx
│   ├── 3_Status_Checks/
│   │   ├── GitHub_Actions_RequiredChecks.png
│   │   ├── GitLab_CI_PipelineRequired.png
│   │   └── CI_Test_Results_Sample.pdf
│   ├── 4_Signed_Commits/
│   │   ├── GPG_Verified_Commit_Examples.png
│   │   ├── GPG_Key_Registry_2025-12-31.xlsx
│   │   └── Developer_Training_Records.pdf
│   └── Assessment_Workbook_Q4-2025.xlsx
```

---

## Common Pitfalls

### Pitfall 1: Confusing "Protected" with "Fully Protected"

**Problem:** Branch shows as "protected" but critical rules missing.

**Example:**
- GitHub shows lock icon (protected)
- But NO required reviewers configured (anyone can approve own PR)
- Or status checks exist but NOT required (can merge with failing tests)

**How to Avoid:**
- Check EACH protection rule individually
- Don't assume platform defaults are sufficient
- Verify with test (try to bypass protection)

---

### Pitfall 2: Administrators Bypass Everything

**Problem:** Protection rules don't apply to repository administrators.

**Reality Check:**
- Default on many platforms: Admins can bypass ALL protection
- GitHub: "Include administrators" is UNCHECKED by default
- GitLab: Maintainers can bypass by default

**How to Fix:**
- GitHub: ✅ "Include administrators"
- GitLab: Set "Allowed to push" = "No one" (even maintainers)
- Document any admin bypass in exceptions

**Consequence:** Admin bypasses = protection theater (not real protection)

---

### Pitfall 3: Status Checks Not Actually Required

**Problem:** CI/CD tests run but don't block merge.

**Example:**
- GitHub Actions running on every PR
- Tests fail → PR still mergeable (checks are advisory only)
- Need to ENABLE "Require status checks to pass"

**How to Verify:**
- Create test PR with failing tests
- Attempt to merge
- Should be BLOCKED

---

### Pitfall 4: Stale Approvals Not Dismissed

**Problem:** Code approved yesterday, new commits today, merge proceeds without re-review.

**Attack Scenario:**
1. Developer submits PR with benign code
2. Reviewer approves
3. Developer pushes malicious code
4. Merge proceeds with old approval (reviewer never saw malicious code)

**How to Fix:**
- GitHub: ✅ "Dismiss stale pull request approvals when new commits are pushed"
- GitLab: ✅ "Remove all approvals when commits are added"
- Bitbucket: ✅ "Dismiss approvals when new changes are pushed"

---

### Pitfall 5: Missing Release Branch Protection

**Problem:** Main branch protected, release branches unprotected.

**Why It Matters:**
- Release branches deploy to production
- Unprotected release = backdoor to production

**How to Fix:**
- Use branch patterns: `main`, `release/*`, `hotfix/*`
- Apply same protection to release as main

---

### Pitfall 6: Self-Approval Allowed

**Problem:** Developer can approve own PR (defeats code review purpose).

**Platforms:**
- GitHub: If "Required approvals: 1", author can be that 1 reviewer (!)
- GitLab: "Prevent approval by author" must be ENABLED
- Bitbucket: Author cannot self-approve (default, but verify)

**How to Fix:**
- GitHub: Require 2+ reviewers (author can't be all reviewers)
- GitLab: ✅ "Prevent approval by author"
- Test: Create PR as developer, try to approve

---

### Pitfall 7: No Code Owner Enforcement

**Problem:** CODEOWNERS file exists but not enforced.

**Example:**
- Backend code owned by backend team
- Frontend developer can approve backend PR (no backend owner review)

**How to Fix:**
- GitHub: ✅ "Require review from Code Owners"
- GitLab: ✅ "Code owner approval"
- Verify CODEOWNERS file syntax is correct

---

### Pitfall 8: Security Checks Missing

**Problem:** Build and test checks required, but no security scanning.

**Gap:**
- Code quality checked
- Functionality tested
- Security vulnerabilities NOT scanned (CodeQL, Snyk, etc.)

**How to Fix:**
- Add security scanner to CI/CD
- Require security check in branch protection
- Examples: CodeQL, Snyk, SonarQube, Checkmarx

---

### Pitfall 9: Permanent Exceptions

**Problem:** "Temporary" exception granted 2 years ago, still active.

**Reality:**
- Exceptions should be time-bound (<90 days)
- Must be reviewed monthly
- Expired exceptions = non-compliance

**How to Fix:**
- Set expiration dates for ALL exceptions
- Monthly exception review meeting
- Auto-alert on expiration

---

### Pitfall 10: Documenting What You WANT vs. What EXISTS

**Problem:** Documenting planned protection (not actual current state).

**Example:**
- Assessment says "✅ 2 required reviewers"
- Actual platform configuration: 0 required reviewers
- Auditor spot-checks → Finds discrepancy → Audit finding

**How to Avoid:**
- Document ACTUAL current state (not aspirational)
- Screenshot configurations as evidence
- Spot-check random repositories

---

## Quality Checklist

Before submitting assessment for approval:

### Completeness

**Repository Branch Inventory:**
- [ ] All repositories from IMP-S1 documented
- [ ] Main branches identified for ALL repos
- [ ] Release branches identified (if exist)
- [ ] Protection requirements align with policy

**Branch Protection Details:**
- [ ] Every protected branch has rule details documented
- [ ] Production main branches have 2+ required approvals
- [ ] Direct commits blocked for production
- [ ] Status checks required where CI/CD exists

**Pull Request Configuration:**
- [ ] PR settings documented for all repos
- [ ] Self-approval blocked
- [ ] Stale approval dismissal enabled

**Status Check Verification:**
- [ ] CI/CD integration documented
- [ ] Required checks identified
- [ ] Blocking enforcement verified

**Signed Commits:**
- [ ] Signature requirements documented
- [ ] Adoption percentages calculated
- [ ] GPG infrastructure status assessed

**Exceptions:**
- [ ] All exceptions documented
- [ ] No expired exceptions (or remediation plan)
- [ ] CISO approvals present

**Compliance Scoring:**
- [ ] All formulas calculate correctly
- [ ] Overall score is accurate
- [ ] Risk categorization appropriate

**Gap Analysis:**
- [ ] All non-compliant items documented
- [ ] Remediation plans are specific
- [ ] Critical gaps have near-term dates

**Evidence:**
- [ ] Configuration screenshots collected
- [ ] PR enforcement examples captured
- [ ] CI/CD logs saved
- [ ] Files organized in structure

**Approval:**
- [ ] All signatures obtained
- [ ] Next review date scheduled

### Accuracy

- [ ] Protection rules match platform reality (spot-check 5 repos)
- [ ] Required approvals match configurations
- [ ] Status checks verified (test with failing PR)
- [ ] Signed commit percentages accurate (sample verification)

### Honesty

- [ ] Documented actual state (not aspirational)
- [ ] Gaps documented honestly (not hidden)
- [ ] Compliance scores reflect reality

### Auditability

- [ ] All claims backed by evidence
- [ ] Screenshots show current dates
- [ ] Evidence is organized and labeled

---

## Review & Approval

Same process as IMP-S1:

1. **Self-Review**: Complete quality checklist
2. **Repository Owner Review**: Verify configurations
3. **Information Security Manager**: Compliance review
4. **CISO**: Final approval

**Approval Criteria:**
- Branch protection configured for all production repos
- Compliance score ≥85% OR remediation plan for gaps
- Evidence collected and organized
- No critical gaps OR immediate remediation planned

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Python/Excel Script Maintainers, Assessment Workbook Developers

---

## Instructions for Workbook Development

### Workbook Generation

**Primary Script:** `generate_a84_2_branch_protection.py`

**Purpose:** Generate Excel workbook (`ISMS-IMP-A.8.4.2_Branch_Protection_YYYYMMDD.xlsx`) with pre-configured sheets, data validation, conditional formatting, and formulas.

**Key Functions:**
- `create_workbook()`: Initialize workbook and sheets
- `setup_styles()`: Cell styles, fonts, fills, borders
- `create_branch_protection_sheets()`: Generate assessment sheets
- `create_compliance_formulas()`: Compliance calculations
- `create_evidence_register()`: Evidence tracking
- `create_approval_signoff()`: Approval workflow

**File Naming:** `ISMS-IMP-A.8.4.2_Branch_Protection_YYYYMMDD.xlsx`

---

## Workbook Structure Overview

### Sheet List (10 Sheets Total)

| Sheet # | Sheet Name | Purpose | Rows | Columns | Entry Type |
|---------|------------|---------|------|---------|------------|
| 1 | Instructions_Legend | User guide | ~50 | A-B | Read-only |
| 2 | Repository_Branch_Inventory | Branch inventory | Variable | A-H | User input |
| 3 | Branch_Protection_Details | Protection rules | Variable | A-M | User input |
| 4 | Pull_Request_Configuration | PR settings | Variable | A-H | User input |
| 5 | Status_Check_Verification | CI/CD checks | Variable | A-I | User input |
| 6 | Signed_Commits_Audit | GPG adoption | Variable | A-F | User input |
| 7 | Exception_Management | Exception tracking | Variable | A-H | User input |
| 8 | Compliance_Scoring | Automated metrics | ~50 | A-D | Formula |
| 9 | Gap_Analysis | Gap remediation | Variable | A-S | User input |
| 10 | Evidence_Register | Evidence docs | Variable | A-P | User input |
| 11 | Approval_Sign_Off | Final approval | ~40 | A-B | User input |

---

## Sheet 2: Repository_Branch_Inventory

### Purpose
Document all branches requiring protection.

### Column Definitions

| Col | Field Name | Width | Type | Validation | Description |
|-----|------------|-------|------|------------|-------------|
| A | Repository Name | 30 | Text | From IMP-S1 | Repository being assessed |
| B | Repository Platform | 20 | Dropdown | GitHub Cloud, GitHub Enterprise, GitLab SaaS, GitLab Self-Hosted, Bitbucket Cloud, Bitbucket Server, Azure DevOps | Hosting platform |
| C | Repository Classification | 20 | Dropdown | 🔴 Production, 🟡 Internal Tools, 🟢 Open Source, ⚪ Archived | From IMP-S1 |
| D | Branch Name | 25 | Text | None | Exact branch name (main, release/v1.0) |
| E | Branch Type | 18 | Dropdown | Main, Release, Development, Feature, Hotfix | Branch category |
| F | Protection Required | 18 | Dropdown | ✅ Yes, ❌ No, ➖ N/A | Per policy requirements |
| G | Protection Configured | 20 | Dropdown | ✅ Yes, ❌ No, ⚠️ Partial | Current platform status |
| H | Status | 18 | Formula | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant | Compliance status |

### Data Validation

**Column B (Repository Platform):**
```
Values: GitHub Cloud, GitHub Enterprise, GitLab SaaS, GitLab Self-Hosted, Bitbucket Cloud, Bitbucket Server, Azure DevOps, AWS CodeCommit, Other
Allow blank: No
```

**Column C (Repository Classification):**
```
Values: 🔴 Production, 🟡 Internal Tools, 🟢 Open Source, ⚪ Archived
Allow blank: No
```

**Column E (Branch Type):**
```
Values: Main, Release, Development, Feature, Hotfix
Allow blank: No
```

**Column F (Protection Required):**
```
Values: ✅ Yes, ❌ No, ➖ N/A
Allow blank: No
```

**Column G (Protection Configured):**
```
Values: ✅ Yes, ❌ No, ⚠️ Partial
Allow blank: No
```

### Formulas

**Column H (Status):**
```excel
=IF(F4="✅ Yes",
  IF(G4="✅ Yes", "✅ Compliant",
    IF(G4="⚠️ Partial", "⚠️ Partial", "❌ Non-Compliant")),
  "➖ N/A")
```

### Conditional Formatting

**Column C (Classification):**
- 🔴 Production: Red fill (#FFC7CE)
- 🟡 Internal Tools: Yellow fill (#FFEB9C)
- 🟢 Open Source: Green fill (#C6EFCE)
- ⚪ Archived: Gray fill (#D9D9D9)

**Column H (Status):**
- ✅ Compliant: Green background
- ⚠️ Partial: Yellow background
- ❌ Non-Compliant: Red background

---

## Sheet 3: Branch_Protection_Details

### Purpose
Document specific protection rules per branch.

### Column Definitions

| Col | Field Name | Width | Type | Validation | Description |
|-----|------------|-------|------|------------|-------------|
| A | Repository Name | 30 | Text | From Sheet 2 | Repository name |
| B | Branch Name | 25 | Text | From Sheet 2 | Branch name |
| C | Direct Commits Blocked | 20 | Dropdown | ✅ Yes, ❌ No | PR required enforcement |
| D | Pull Request Required | 20 | Dropdown | ✅ Yes, ❌ No | Same as Column C |
| E | Required Approvals | 12 | Number | 0-5 | Minimum reviewer count |
| F | Dismiss Stale Reviews | 20 | Dropdown | ✅ Yes, ❌ No | Invalidate old approvals |
| G | Code Owner Review | 20 | Dropdown | ✅ Yes, ❌ No, ➖ N/A | CODEOWNERS enforcement |
| H | Status Checks Required | 20 | Dropdown | ✅ Yes, ❌ No, ⚠️ Partial | CI/CD enforcement |
| I | Status Check List | 40 | Text | None | Comma-separated checks |
| J | Signed Commits | 20 | Dropdown | ✅ Yes, ❌ No, ➖ N/A | GPG requirement |
| K | Linear History | 18 | Dropdown | ✅ Yes, ❌ No | Merge commit prevention |
| L | Compliance Score | 12 | Formula | Percentage | % rules configured |
| M | Status | 18 | Formula | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant | Overall status |

### Data Validation

**Columns C, D, F, K:**
```
Values: ✅ Yes, ❌ No
Allow blank: No
```

**Columns G, J:**
```
Values: ✅ Yes, ❌ No, ➖ N/A
Allow blank: No
```

**Column H:**
```
Values: ✅ Yes, ❌ No, ⚠️ Partial
Allow blank: No
```

**Column E (Required Approvals):**
```
Type: Whole number
Minimum: 0
Maximum: 5
Allow blank: No
```

### Formulas

**Column L (Compliance Score) - Production Code:**
```excel
=IF(C4="", "",
  (IF(C4="✅ Yes",1,0) +
   IF(D4="✅ Yes",1,0) +
   IF(E4>=2,1,IF(E4>=1,0.5,0)) +
   IF(F4="✅ Yes",1,0) +
   IF(H4="✅ Yes",1,IF(H4="⚠️ Partial",0.5,0))
  ) / 5 * 100)
```

**Column M (Status):**
```excel
=IF(L4="", "",
  IF(L4=100, "✅ Compliant",
    IF(L4>=50, "⚠️ Partial", "❌ Non-Compliant")))
```

### Conditional Formatting

**Column E (Required Approvals):**
- ≥2: Green background (production standard)
- 1: Yellow background (internal tools standard)
- 0: Red background (non-compliant)

**Column L (Compliance Score):**
- 100%: Green background
- 50-99%: Yellow background
- <50%: Red background

**Column M (Status):**
- ✅ Compliant: Green background
- ⚠️ Partial: Yellow background
- ❌ Non-Compliant: Red background

---

## Sheet 4: Pull_Request_Configuration

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Repository Name | 30 | Text | From Sheet 2 |
| B | Minimum Reviewers | 12 | Number | 0-5 |
| C | Code Owner Review | 20 | Dropdown | ✅ Required, ⚠️ Optional, ❌ No |
| D | Dismiss Stale Approvals | 20 | Dropdown | ✅ Yes, ❌ No |
| E | Restrict Dismiss | 20 | Dropdown | ✅ Yes, ❌ No |
| F | Conversation Resolution | 20 | Dropdown | ✅ Required, ⚠️ Optional, ❌ No |
| G | Self-Approval Blocked | 20 | Dropdown | ✅ Yes, ❌ No |
| H | Compliance Status | 18 | Formula | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |

### Formulas

**Column H (Compliance Status):**
```excel
=IF(B4>=1,
  IF(AND(D4="✅ Yes", G4="✅ Yes"), "✅ Compliant",
    IF(OR(D4="✅ Yes", G4="✅ Yes"), "⚠️ Partial", "❌ Non-Compliant")),
  "❌ Non-Compliant")
```

---

## Sheet 5: Status_Check_Verification

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Repository Name | 30 | Text | From Sheet 2 |
| B | Status Checks Configured | 22 | Dropdown | ✅ Yes, ❌ No |
| C | Build Check | 18 | Dropdown | ✅ Configured, ❌ Missing |
| D | Test Check | 18 | Dropdown | ✅ Configured, ❌ Missing |
| E | Lint Check | 18 | Dropdown | ✅ Configured, ❌ Missing |
| F | Security Check | 18 | Dropdown | ✅ Configured, ❌ Missing |
| G | All Checks Must Pass | 20 | Dropdown | ✅ Yes, ❌ No |
| H | Up-to-Date Before Merge | 22 | Dropdown | ✅ Yes, ❌ No |
| I | Compliance Status | 18 | Formula | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |

### Formulas

**Column I (Compliance Status):**
```excel
=IF(B4="✅ Yes",
  IF(AND(C4="✅ Configured", D4="✅ Configured", G4="✅ Yes"),
    "✅ Compliant",
    IF(OR(C4="✅ Configured", D4="✅ Configured"), "⚠️ Partial", "❌ Non-Compliant")),
  "❌ Non-Compliant")
```

---

## Sheet 6: Signed_Commits_Audit

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Repository Name | 30 | Text | From Sheet 2 |
| B | Signed Commits Required | 22 | Dropdown | ✅ Yes, ❌ No, ➖ N/A |
| C | % Commits Signed (Last 30d) | 22 | Number | 0-100% |
| D | GPG Infrastructure | 20 | Dropdown | ✅ Implemented, ⚠️ Partial, ❌ Missing |
| E | Developer Training | 20 | Dropdown | ✅ Completed, ⚠️ In Progress, ❌ Not Started |
| F | Compliance Status | 18 | Formula | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |

### Formulas

**Column F (Compliance Status):**
```excel
=IF(B4="✅ Yes",
  IF(C4>=80, "✅ Compliant",
    IF(C4>=50, "⚠️ Partial", "❌ Non-Compliant")),
  IF(B4="➖ N/A", "➖ N/A", "✅ Compliant"))
```

### Conditional Formatting

**Column C (% Commits Signed):**
- ≥80%: Green background
- 50-79%: Yellow background
- <50%: Red background

---

## Sheet 7: Exception_Management

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Exception ID | 15 | Text | Format: EXC-001 |
| B | Repository/Branch | 30 | Text | "repo / branch" |
| C | Exception Reason | 40 | Text | Justification |
| D | Granted By | 25 | Text | Approver name |
| E | Grant Date | 15 | Date | Date format |
| F | Expiration Date | 15 | Date | Date format |
| G | Review Date | 15 | Date | Date format |
| H | Status | 15 | Formula | 🟢 Active, 🔴 Expired, ⚪ Revoked |

### Formulas

**Column H (Status):**
```excel
=IF(F4<TODAY(), "🔴 Expired",
  IF(F4="", "⚪ Revoked", "🟢 Active"))
```

### Conditional Formatting

**Column H (Status):**
- 🔴 Expired: Red background (CRITICAL)
- 🟢 Active: Green background
- ⚪ Revoked: Gray background

**Column F (Expiration Date):**
```
=F4<TODAY()
Format: Red fill (expired)
```

---

## Sheet 8: Compliance_Scoring

### Purpose
Calculate overall branch protection compliance (automated).

### Metrics Calculated

**Row 5: Branch Protection Configuration Rate**
```excel
Cell B5: =COUNTIF(Repository_Branch_Inventory!H:H,"✅ Compliant")/
         COUNTIF(Repository_Branch_Inventory!F:F,"✅ Yes")*100
Target C5: 100%
Status D5: =IF(B5>=100,"🟢","🔴")
```

**Row 8: Pull Request Enforcement Rate**
```excel
Cell B8: =COUNTIF(Branch_Protection_Details!D:D,"✅ Yes")/
         COUNTA(Branch_Protection_Details!A:A)*100
Target C8: ≥95%
Status D8: =IF(B8>=95,"🟢",IF(B8>=80,"🟡","🔴"))
```

**Row 11: Status Check Compliance Rate**
```excel
Cell B11: =COUNTIF(Status_Check_Verification!I:I,"✅ Compliant")/
          COUNTIF(Status_Check_Verification!B:B,"✅ Yes")*100
Target C11: 100%
Status D11: =IF(B11>=100,"🟢","🔴")
```

**Row 14: Signed Commit Adoption Rate**
```excel
Cell B14: =AVERAGE(Signed_Commits_Audit!C:C)
Target C14: ≥80%
Status D14: =IF(B14>=80,"🟢",IF(B14>=50,"🟡","🔴"))
```

**Row 17: Overall Branch Protection Score**
```excel
Cell B17: =(B5*0.40)+(B8*0.30)+(B11*0.20)+(B14*0.10)
Target C17: ≥85%
```

**Row 20: Risk Categorization**
```excel
Cell B20: =IF(B17>=85,"🟢 Low Risk",
              IF(B17>=70,"🟡 Medium Risk","🔴 High Risk"))
```

### Conditional Formatting

**Column B (Current Score):**
- ≥Target: Green background
- <Target: Red background

**Row 20 (Risk Level):**
- 🟢 Low Risk: Green background
- 🟡 Medium Risk: Yellow background
- 🔴 High Risk: Red background

---

## Sheet 9: Gap_Analysis

### Structure

Same as IMP-S1 Gap_Analysis with standard columns:
- Gap ID, Gap Category, Gap Description
- Policy Requirement, Current State, Desired State
- Risk Level, Impact, Affected Repos
- Root Cause, Remediation Plan
- Responsible Party, Target Date, Estimated Effort
- Status, Actual Completion, Verification Method, Verification Date
- Notes

**Reference IMP-S1 PART II for detailed specifications**

---

## Sheet 10: Evidence_Register

### Structure

Same as IMP-S1 Evidence_Register with standard columns:
- Evidence ID, Evidence Type, Description
- Related Requirement, Evidence Date, Evidence Source
- File Name, File Location
- Collected By, Collection Date, Format
- Retention Period, Retention End, Auditor Reviewed
- Auditor Comments, Notes

**Reference IMP-S1 PART II for detailed specifications**

---

## Sheet 11: Approval_Sign_Off

### Structure

Same as IMP-S1 Approval_Sign_Off:
- Assessment Summary (links to Compliance_Scoring)
- Assessment Completed By
- Repository Owner Approvals (3-5 blocks)
- Information Security Manager Review
- CISO Approval
- Next Review Date (+90 days)

**Reference IMP-S1 PART II for detailed specifications**

---

## Cell Styling Reference

### Header Styles

**Main Header (Row 1):**
- Font: Calibri 14pt bold white
- Fill: #003366 (dark blue)
- Alignment: Center
- Height: 40px

**Subheader (Row 2):**
- Font: Calibri 11pt bold white
- Fill: #4472C4 (medium blue)
- Alignment: Center
- Height: 30px

**Column Header (Row 3):**
- Font: Calibri 10pt bold black
- Fill: #D9D9D9 (light gray)
- Alignment: Center, text wrap
- Border: Thin black

### Input Cell Styles

**User Input:**
- Fill: #FFFFCC (light yellow)
- Border: Thin gray
- Font: Calibri 10pt

**Formula (Read-only):**
- Fill: #E7F3FF (light blue)
- Protection: Locked
- Font: Calibri 10pt

### Status Colors

**Green (Compliant):**
- Fill: #C6EFCE
- Text: #006100

**Yellow (Partial/Warning):**
- Fill: #FFEB9C
- Text: #9C6500

**Red (Non-Compliant):**
- Fill: #FFC7CE
- Text: #9C0006

**Blue (In Progress):**
- Fill: #B4C7E7
- Text: #002060

**Gray (N/A):**
- Fill: #D9D9D9
- Text: #404040

---

## Freeze Panes

**All Assessment Sheets (2-10):**
- Freeze at **A4** (headers visible when scrolling)

**Approval Sheet (11):**
- Freeze at **A3**

---

## Cell Protection

**Protected:**
- Header rows (1-3)
- Formula cells (Compliance_Scoring)
- Instructions sheet

**Unprotected:**
- User input cells (light yellow)
- Data entry rows (4+)

**Sheet Protection:**
- Allow: Select unlocked, format cells, insert rows, delete rows, sort, filter
- Disallow: Edit locked cells, modify formulas

---

## Quality Assurance

### Validation Script

**Script:** `excel_sanity_check_a84_2.py`

**Checks:**
1. All 11 sheets exist
2. Column counts match specification
3. Data validation configured
4. Conditional formatting applied
5. Formulas syntactically correct
6. Freeze panes configured
7. Cell protection enabled
8. Styling consistent

**Usage:**
```bash
python excel_sanity_check_a84_2.py ISMS-IMP-A.8.4.2_Branch_Protection_20260125.xlsx
```

---

## Version Control

**Filename:** `ISMS-IMP-A.8.4.2_Branch_Protection_YYYYMMDD.xlsx`

**Change Log:**
- v1.0: Initial workbook structure

---

**END OF PART II: TECHNICAL SPECIFICATION**