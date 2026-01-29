# ISMS-IMP-A.8.4-S2
## Branch Protection Configuration Guide
### Excel Workbook Layout Specification

**Document ID**: ISMS-IMP-A.8.4-S2  
**Assessment Area**: Branch Protection Compliance  
**Related Policy**: ISMS-POL-A.8.4-S2.4 (Branch Protection Requirements)  
**Purpose**: Document and assess branch protection configurations across all repository platforms

**Key Principle**: This implementation is **platform-agnostic**. Organizations configure branch protection according to their specific Git platform capabilities while meeting policy requirements.

---

## Implementation Overview

### Objectives

This implementation guide provides:
1. Platform-specific branch protection configuration procedures
2. Excel workbook specification for documenting protection rules
3. Pull request workflow implementation guidance
4. Compliance assessment methodology

### Scope

- Main branch protection configuration
- Release branch protection
- Pull request requirements
- Status check integration
- Signed commit configuration

---

## Section 1: Branch Protection Strategy

### 1.1 Protection Level Framework

**Production Code Repositories** (Maximum Protection):
- Main/master branch: Full protection (all rules enforced)
- Release branches: Same as main branch
- Development branches: Optional protection
- Feature branches: No required protection

**Internal Tools Repositories** (High Protection):
- Main/master branch: Core protection (PR required, 1 reviewer minimum)
- Release branches: Same as main
- Development branches: Optional
- Feature branches: No required protection

**Open Source Repositories** (Medium Protection):
- Main/master branch: Community-appropriate protection
- Release branches: Same as main
- Development branches: Variable based on project
- Feature branches: No required protection

**Archived Repositories** (Read-Only):
- All branches: Read-only mode
- No new commits allowed
- Exceptions require CISO approval

### 1.2 Protection Rule Selection Criteria

**When to enable each protection rule**:

1. **Direct Commits Blocked**: ALL production and internal tools repositories
2. **Pull Request Required**: ALL production and internal tools repositories
3. **Required Reviewers (2)**: Production code only
4. **Required Reviewers (1)**: Internal tools
5. **Dismiss Stale Approvals**: Production and internal tools
6. **Require Code Owner Review**: Production code with designated code owners
7. **Status Checks Required**: All repositories with CI/CD pipelines
8. **Signed Commits**: Production code (where technically feasible)
9. **Linear History**: Production code (optional for internal tools)

---

## Section 2: Platform-Specific Configuration

### 2.1 GitHub Branch Protection

#### Step-by-Step Configuration

**Navigate to Branch Protection**:
1. Go to Repository → Settings
2. Click "Branches" in left sidebar
3. Under "Branch protection rules", click "Add rule"

**Configure Rule Name**:
- Branch name pattern: `main` (or `master`)
- For multiple branches: `main,release/*,hotfix/*`

**Protection Settings** (for production repositories):

✅ **Require a pull request before merging**
- Required approvals: 2
- ✅ Dismiss stale pull request approvals when new commits are pushed
- ✅ Require review from Code Owners (if CODEOWNERS file exists)
- ✅ Restrict who can dismiss pull request reviews (admins only)
- ✅ Allow specified actors to bypass required pull requests: None
- ✅ Require approval of the most recent reviewable push

✅ **Require status checks to pass before merging**
- ✅ Require branches to be up to date before merging
- Status checks to require (select from list):
  - CI/Build (e.g., "build", "test")
  - Security scans (e.g., "CodeQL", "Snyk")
  - Linters (e.g., "ESLint", "pylint")

✅ **Require conversation resolution before merging**

✅ **Require signed commits** (if GPG infrastructure exists)

✅ **Require linear history** (prevents merge commits)

✅ **Require deployments to succeed before merging** (if using GitHub Deployments)

❌ **Lock branch** (do not enable - prevents all changes)

**Rules applied to administrators**:
- ✅ Include administrators (recommended - admins follow same rules)

**Restrict who can push to matching branches**:
- Option 1: Leave empty (no one can push directly)
- Option 2: Only CI/CD service accounts (for automated deployments)

**Allow force pushes**: ❌ Never enable
**Allow deletions**: ❌ Never enable

**Click "Create" to save rule**

#### Verification

```bash
# Verify branch protection via GitHub CLI
gh api repos/{owner}/{repo}/branches/main/protection

# Or via web UI:
# Repository → Settings → Branches → View rule details
```

### 2.2 GitLab Protected Branches

#### Step-by-Step Configuration

**Navigate to Protected Branches**:
1. Go to Project → Settings → Repository
2. Expand "Protected branches"
3. Select branch from dropdown (e.g., `main`)

**Protection Settings** (for production repositories):

**Allowed to merge**:
- Select: "Developers + Maintainers" (requires merge request)
- Uncheck: "Maintainers" (prevents direct push)

**Allowed to push and merge**:
- Select: "No one" (forces merge requests)

**Allowed to force push**: ❌ Unchecked

**Code owner approval**: ✅ Required (if CODEOWNERS file exists)

**Click "Protect" to save**

#### Merge Request Requirements

Navigate to Project → Settings → Merge requests:

**Merge checks**:
- ✅ Pipelines must succeed
- ✅ All threads must be resolved
- ✅ Merge requests approvals: 2 (production) or 1 (internal tools)

**Merge request approvals**:
- Navigate to Settings → Merge request approvals
- Set "Approval rules":
  - Rule name: "Code Review"
  - Approvals required: 2 (production) or 1 (internal tools)
  - ✅ Prevent approval by author
  - ✅ Prevent approvals by users who add commits
  - ✅ Prevent editing approval rules
  - ✅ Remove all approvals when commits are added

**Merge options**:
- ✅ Enable "Delete source branch" option by default
- Merge method: "Merge commit" (or "Fast-forward merge" for linear history)

#### Verification

```bash
# Verify via GitLab API
curl --header "PRIVATE-TOKEN: <token>" \
  "https://gitlab.com/api/v4/projects/{id}/protected_branches/main"

# Or via web UI:
# Settings → Repository → Protected branches
```

### 2.3 Bitbucket Branch Permissions

#### Step-by-Step Configuration

**Navigate to Branch Permissions**:
1. Go to Repository settings → Branch permissions
2. Click "Add a branch permission"

**Branch Pattern**: `main` (or `master`)

**Protection Settings** (for production repositories):

**Type**: Write access
- ✅ Prevent deletion
- ✅ Prevent changes without a pull request
- ✅ Require approvals: 2 (production) or 1 (internal tools)
- Users/Groups: Select who can approve (typically: Developers, Senior Engineers)

**Type**: Delete access
- Select: Administrators only

**Merge Checks**:
Navigate to Repository settings → Merge checks:
- ✅ Require approvals: 2 (production) or 1 (internal tools)
- ✅ Dismiss approvals when new changes are pushed
- ✅ All tasks must be resolved
- ✅ Builds must pass

**Branch Restrictions**:
- Create specific restrictions per branch pattern
- Prevent force push
- Prevent deletion
- Prevent direct commits (require PR)

**Click "Add" to save**

#### Verification

Via web UI:
- Repository settings → Branch permissions
- Verify each rule is listed correctly

### 2.4 Azure DevOps Branch Policies

#### Step-by-Step Configuration

**Navigate to Branch Policies**:
1. Go to Project Settings → Repositories → Policies
2. Select branch: `main`

**Protection Settings** (for production repositories):

**Require a minimum number of reviewers**:
- ✅ Enable
- Minimum number: 2 (production) or 1 (internal tools)
- ✅ Allow requestors to approve their own changes: ❌ Unchecked
- ✅ Prohibit the most recent pusher from approving: ✅ Checked
- ✅ Require at least one approval on the last iteration: ✅ Checked
- ✅ Reset all approval votes when new changes are pushed: ✅ Checked

**Check for linked work items**:
- Optional (✅ Enable if using Azure Boards)

**Check for comment resolution**:
- ✅ Required

**Build validation**:
- ✅ Enable
- Build pipeline: Select CI/CD pipeline
- ✅ Required
- Build expiration: 12 hours
- Display name: "CI Build"

**Status checks**:
- Add external status checks (optional)
- Security scanning, linting, etc.

**Automatically included reviewers**:
- Add code owners or required reviewers
- Policy: Required or Optional

**Limit merge types**:
- Allow: Basic merge, Squash merge, or Rebase and fast-forward
- Disallow: Rebase with merge commit (if linear history desired)

**Click "Save changes"**

#### Verification

```powershell
# Verify via Azure DevOps CLI
az repos policy list --repository {repo-name} --branch main

# Or via web UI:
# Project Settings → Repositories → Policies → Select branch
```

---

## Section 3: Pull Request Workflow Implementation

### 3.1 Developer Workflow

**Creating a Pull Request**:

1. **Create Feature Branch**:
```bash
git checkout -b feature/new-feature
# Make changes
git add .
git commit -m "Implement new feature"
git push origin feature/new-feature
```

2. **Open Pull Request**:
- Navigate to repository in web UI
- Click "New Pull Request" or "Create Merge Request"
- Select source branch: `feature/new-feature`
- Select target branch: `main`
- Fill in PR template:
  - Title: Descriptive summary
  - Description: What changed and why
  - Link to issue/ticket (if applicable)
  - Testing performed

3. **Request Reviewers**:
- Add reviewers (minimum 2 for production)
- Add code owners if applicable
- Assign to yourself

4. **Address CI/CD Checks**:
- Wait for status checks to run
- Fix any failing tests or lints
- Push fixes to same branch (updates PR automatically)

5. **Respond to Review Comments**:
- Address reviewer feedback
- Make requested changes
- Reply to comments explaining changes
- Request re-review after changes

6. **Merge**:
- Once approved and all checks pass
- Click "Merge" (or "Squash and merge" / "Rebase and merge")
- Delete source branch

### 3.2 Code Review Best Practices

**Reviewer Responsibilities**:

✅ **Review for**:
- Functionality: Does code do what it's supposed to?
- Security: Are there vulnerabilities? (SQL injection, XSS, etc.)
- Code quality: Is it readable, maintainable?
- Tests: Are there adequate tests?
- Documentation: Is code properly documented?
- Standards compliance: Does it follow team coding standards?

✅ **Review checklist**:
- [ ] Code compiles/runs without errors
- [ ] Tests pass and provide adequate coverage
- [ ] No obvious security vulnerabilities
- [ ] No hardcoded secrets or credentials
- [ ] Error handling is appropriate
- [ ] Code is readable and well-documented
- [ ] Follows team coding standards
- [ ] No unnecessary complexity
- [ ] Performance considerations addressed

❌ **Do NOT approve**:
- Your own pull requests (self-approval)
- PRs you contributed commits to (unless explicitly allowed)
- PRs with failing status checks
- PRs with unresolved conversations
- PRs you don't fully understand

**Review timeline**:
- Respond to review requests within 24 hours
- Complete review within 48 hours for normal PRs
- Expedited review for hotfixes (<4 hours)

### 3.3 Status Check Integration

**CI/CD Pipeline Requirements**:

Every repository with production or internal tools code SHOULD have:

1. **Build Check**:
   - Compile code (if compiled language)
   - Build artifacts
   - Report build status to PR

2. **Test Check**:
   - Run unit tests
   - Run integration tests
   - Report test results and coverage
   - Fail if tests fail or coverage drops

3. **Linting Check**:
   - Run code linter (ESLint, Pylint, RuboCop, etc.)
   - Check code formatting (Prettier, Black, gofmt)
   - Fail if linting errors found

4. **Security Check**:
   - Run SAST scanner (CodeQL, Snyk, SonarQube)
   - Check for known vulnerabilities
   - Fail if critical vulnerabilities found

5. **Secret Scanning** (optional but recommended):
   - Scan for hardcoded secrets
   - Fail if secrets detected

**Status Check Configuration**:

Each platform allows configuring required status checks:
- **GitHub**: Settings → Branches → Branch protection → Required status checks
- **GitLab**: Settings → Merge requests → Merge checks → Pipelines must succeed
- **Bitbucket**: Repository settings → Merge checks → Builds must pass
- **Azure DevOps**: Branch policies → Build validation → Add build policy

---

## Section 4: Signed Commits Configuration

### 4.1 GPG Key Setup (Developers)

**Generate GPG Key**:

```bash
# Generate new GPG key
gpg --full-generate-key
# Select: RSA and RSA
# Key size: 4096
# Expiration: 2 years
# Enter name and email (must match Git config)

# List keys
gpg --list-secret-keys --keyid-format LONG

# Export public key
gpg --armor --export {KEY_ID}
```

**Add GPG Key to Git Platform**:

- **GitHub**: Settings → SSH and GPG keys → New GPG key → Paste public key
- **GitLab**: Preferences → GPG Keys → Add new key → Paste public key
- **Bitbucket**: Personal settings → GPG keys → Add key → Paste public key
- **Azure DevOps**: Not natively supported (use commit signing verification externally)

**Configure Git to Sign Commits**:

```bash
# Tell Git to use GPG key
git config --global user.signingkey {KEY_ID}

# Sign all commits by default
git config --global commit.gpgsign true

# Sign all tags
git config --global tag.gpgsign true
```

**Commit with Signature**:

```bash
# Commits are now signed automatically
git commit -m "Feature implementation"

# Verify signature
git log --show-signature
```

### 4.2 Enforcing Signed Commits

**GitHub**:
- Branch protection rules → ✅ Require signed commits

**GitLab**:
- Settings → Repository → Push Rules (Premium/Ultimate only)
- ✅ Reject unsigned commits

**Bitbucket**:
- Not natively supported
- Use pre-receive hooks or external validation

**Azure DevOps**:
- Not natively supported for enforcement
- Can verify signatures externally

**Verification**:
- Signed commits show "Verified" badge in web UI
- Can query via API for signature status

---

## Section 5: Excel Workbook Specification

### Workbook Structure

**Sheet 1: Instructions & Legend**

Similar to Repository Access workbook:
- Document ID, assessment date, organization
- How to use the workbook
- Status legend
- Acceptable evidence

**Sheet 2: Repository_Branch_Inventory**

Document all branches requiring protection.

### Column Definitions

| Column | Field Name | Type | Description |
|--------|-----------|------|-------------|
| A | Repository Name | Text | Repository being assessed |
| B | Repository Platform | Dropdown | GitHub, GitLab, Bitbucket, Azure DevOps |
| C | Repository Classification | Dropdown | Production Code, Internal Tools, Open Source, Archived |
| D | Branch Name | Text | Branch name (e.g., main, master, release/v1.0) |
| E | Branch Type | Dropdown | Main, Release, Development, Feature, Hotfix |
| F | Protection Required | Dropdown | ✅ Yes, ❌ No, ➖ N/A |
| G | Protection Configured | Dropdown | ✅ Yes, ❌ No, ⚠️ Partial |
| H | Status | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |

**Sheet 3: Branch_Protection_Details**

Document specific protection rules for each branch.

### Column Definitions

| Column | Field Name | Type | Description |
|--------|-----------|------|-------------|
| A | Repository Name | Text | Repository name |
| B | Branch Name | Text | Branch name |
| C | Direct Commits Blocked | Dropdown | ✅ Yes, ❌ No |
| D | Pull Request Required | Dropdown | ✅ Yes, ❌ No |
| E | Required Approvals | Number | Count (0, 1, 2, etc.) |
| F | Dismiss Stale Reviews | Dropdown | ✅ Yes, ❌ No |
| G | Code Owner Review Required | Dropdown | ✅ Yes, ❌ No, ➖ N/A |
| H | Status Checks Required | Dropdown | ✅ Yes, ❌ No, ⚠️ Partial |
| I | Status Check List | Text | Comma-separated list of checks |
| J | Signed Commits Required | Dropdown | ✅ Yes, ❌ No, ➖ N/A |
| K | Linear History Enforced | Dropdown | ✅ Yes, ❌ No |
| L | Compliance Score | Formula | % of rules configured correctly |
| M | Status | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |

**Sheet 4: Pull_Request_Configuration**

Assess pull request workflow configuration.

| Column | Field Name | Type | Description |
|--------|-----------|------|-------------|
| A | Repository Name | Text | Repository name |
| B | Minimum Reviewers | Number | Required approval count |
| C | Code Owner Review | Dropdown | ✅ Required, ⚠️ Optional, ❌ No |
| D | Dismiss Stale Approvals | Dropdown | ✅ Yes, ❌ No |
| E | Restrict Dismiss | Dropdown | ✅ Yes, ❌ No |
| F | Conversation Resolution | Dropdown | ✅ Required, ⚠️ Optional, ❌ No |
| G | Self-Approval Blocked | Dropdown | ✅ Yes, ❌ No |
| H | Compliance Status | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |

**Sheet 5: Status_Check_Verification**

Document CI/CD status checks.

| Column | Field Name | Type | Description |
|--------|-----------|------|-------------|
| A | Repository Name | Text | Repository name |
| B | Status Checks Configured | Dropdown | ✅ Yes, ❌ No |
| C | Build Check | Dropdown | ✅ Configured, ❌ Missing |
| D | Test Check | Dropdown | ✅ Configured, ❌ Missing |
| E | Lint Check | Dropdown | ✅ Configured, ❌ Missing |
| F | Security Check | Dropdown | ✅ Configured, ❌ Missing |
| G | All Checks Must Pass | Dropdown | ✅ Yes, ❌ No |
| H | Up-to-Date Before Merge | Dropdown | ✅ Yes, ❌ No |
| I | Compliance Status | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |

**Sheet 6: Signed_Commits_Audit**

Track signed commit adoption.

| Column | Field Name | Type | Description |
|--------|-----------|------|-------------|
| A | Repository Name | Text | Repository name |
| B | Signed Commits Required | Dropdown | ✅ Yes, ❌ No, ➖ N/A |
| C | % Commits Signed (Last 30 days) | Number | Calculated percentage |
| D | GPG Infrastructure | Dropdown | ✅ Implemented, ⚠️ Partial, ❌ Missing |
| E | Developer Training | Dropdown | ✅ Completed, ⚠️ In Progress, ❌ Not Started |
| F | Compliance Status | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |

**Sheet 7: Exception_Management**

Track branch protection exceptions.

| Column | Field Name | Type | Description |
|--------|-----------|------|-------------|
| A | Exception ID | Text | Unique identifier |
| B | Repository/Branch | Text | Affected repository and branch |
| C | Exception Reason | Text | Business justification |
| D | Granted By | Text | Approver name |
| E | Grant Date | Date | When exception granted |
| F | Expiration Date | Date | When exception expires |
| G | Review Date | Date | Next review date |
| H | Status | Dropdown | 🟢 Active, 🔴 Expired, ⚪ Revoked |

**Sheet 8: Compliance_Scoring**

Calculate branch protection compliance metrics.

### Metrics Calculated

```
Branch Protection Configuration Rate:
= (Repositories with full protection / Total production repos) × 100%
Target: 100%

Pull Request Enforcement Rate:
= (Merges via PR / Total merges) × 100%
Target: ≥95%

Status Check Compliance Rate:
= (Repos with status checks / Repos with CI/CD) × 100%
Target: 100%

Signed Commit Adoption Rate:
= (Signed commits / Total commits) × 100%
Target: ≥80%

Overall Branch Protection Score:
= (Configuration Rate × 40%) +
  (PR Enforcement × 30%) +
  (Status Checks × 20%) +
  (Signed Commits × 10%)
Target: ≥85%
```

**Sheet 9: Gap_Analysis**

Standard gap analysis sheet (similar to previous workbook).

**Sheet 10: Evidence_Register**

Standard evidence register (configuration screenshots, CI/CD logs, etc.).

**Sheet 11: Approval_Sign_Off**

Standard approval sheet with sign-off section.

---

## Section 6: Continuous Compliance Monitoring

### 6.1 Automated Monitoring

**GitHub Actions Example**:

```yaml
# .github/workflows/branch-protection-audit.yml
name: Branch Protection Audit

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sunday
  workflow_dispatch:

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - name: Check Branch Protection
        run: |
          gh api repos/${{ github.repository }}/branches/main/protection \
            | jq '.required_pull_request_reviews.required_approving_review_count'
      
      - name: Alert if Misconfigured
        if: steps.check.outputs.approvals < 2
        run: echo "::warning::Branch protection misconfigured"
```

**GitLab CI Example**:

```yaml
# .gitlab-ci.yml
branch_protection_audit:
  script:
    - |
      curl --header "PRIVATE-TOKEN: $CI_JOB_TOKEN" \
        "$CI_API_V4_URL/projects/$CI_PROJECT_ID/protected_branches/main" \
        | jq '.merge_access_levels[].access_level'
  only:
    - schedules
```

### 6.2 Monthly Review Checklist

- [ ] All production repositories have branch protection enabled
- [ ] All protection rules are correctly configured
- [ ] Pull request enforcement is working (no direct commits)
- [ ] Status checks are running and required
- [ ] Exceptions are reviewed and justified
- [ ] No expired exceptions exist
- [ ] Compliance score ≥85%

---

**END OF IMPLEMENTATION GUIDE**

**Related Documents**:
- ISMS-POL-A.8.4-S2.4 (Branch Protection Requirements)
- ISMS-IMP-A.8.4-S1 (Repository Access Control)
- ISMS-IMP-A.8.4-S3 (Source Code Access Assessment)
