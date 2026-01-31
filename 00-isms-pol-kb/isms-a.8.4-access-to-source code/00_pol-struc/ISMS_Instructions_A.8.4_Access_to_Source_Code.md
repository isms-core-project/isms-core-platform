# PROJECT BRIEF: ISMS Control A.8.4 - Access to Source Code

## Standalone Control Approach

You are implementing **ONE ISO 27001:2022 Annex A control**:

- **A.8.4 - Access to Source Code**: Protecting access to source code and related items

**Why Standalone:**
This control addresses a specific security concern: **protecting source code repositories and intellectual property**. While it relates to secure development (A.8.25/26/29), it focuses specifically on **WHO can access source code** rather than HOW to develop securely.

**Reference Implementation**: 
- **Quality level**: ISMS-A.8.23-Web-Filtering (standalone control)
- **Approach**: Focused policy on source code access control

**Integration Note**: This control integrates with:
- A.8.25-26-29 (Secure Development) - Development security framework
- A.5.15-16-18 (IAM) - Access control foundation
- A.8.2-3-5 (Auth-PAM) - Authentication and privileged access
- A.8.32 (Change Management) - Code deployment controls

## Context & Approach

You are implementing **Source Code Access Control** using Systems Engineering methodology. This framework must be **completely generic** - applicable to any organization's code repositories, regardless of development platform or repository technology.

**Implementation Philosophy**: 
- Apply Feynman's "don't fool yourself" principle - no security theater
- System Engineering approach: Intellectual Property → Access Control → Evidence
- Think with TWO hats simultaneously:
  * **ISMS Implementer**: Build practical source code protection
  * **ISMS Auditor**: Verify measurable access control effectiveness
- Focus on genuine IP protection, not checkbox compliance

**Applicability**:
- All content must be **completely generic and technology-agnostic**
- Use "[Organization]" as placeholder throughout
- No assumptions about repository technology (Git, SVN, Perforce, etc.)
- No assumptions about hosting (self-hosted, GitHub, GitLab, Bitbucket, Azure DevOps, etc.)
- Framework adapts to any code repository environment

## Core Requirements (Specific to A.8.4)

### 1. The Source Code Access Challenge

**Traditional approach (cargo cult):**
```
"Developers have access to the code repository. 
It's... GitHub? GitLab? Someone set it up a while ago."
[No access control policy, everyone has write access, no audit logs]
```
❌ This is meaningless checkbox compliance.

**What auditors and implementers actually need:**

**For A.8.4 (Access to Source Code):**
- Source code repository access control policy
  - Who can access source code (developers, security team, auditors)
  - Access levels (read-only, write/commit, admin)
  - Repository access approval process
  - Access review frequency (quarterly, semi-annual)
- Source code repository types and classification
  - Production code repositories (highest protection)
  - Internal tool repositories (moderate protection)
  - Open source contributions (public, but still controlled)
  - Archived/deprecated repositories (read-only)
- Access control by role
  - Developers: Read/write to assigned repositories
  - Security team: Read access to all repositories (for security reviews)
  - Auditors: Read-only access (time-bound for audits)
  - External contractors: Time-bound access, specific repositories only
  - Administrators: Repository configuration, but not necessarily code access
- Branch protection
  - Main/master branch protection (no direct commits)
  - Pull request requirements (code review before merge)
  - Status checks (CI/CD tests must pass before merge)
  - Signed commits (verify commit author identity)
- Secret management in repositories
  - Prohibition of hardcoded secrets (passwords, API keys, tokens)
  - Secret scanning (automated detection of exposed secrets)
  - Secret rotation if exposed
- Source code backup and recovery
  - Repository backup frequency (daily, real-time replication)
  - Backup retention (30-90 days typical)
  - Disaster recovery testing
- Source code audit logging
  - Repository access logs (who accessed what, when)
  - Commit logs (who changed what, when, why)
  - Access permission changes (who granted/revoked access)
  - Log retention (1-3 years typical)
- Source code intellectual property protection
  - Non-disclosure agreements (NDAs) for code access
  - Code ownership documentation
  - License compliance (open source dependencies)
  - Export control compliance (if applicable)
- Third-party and contractor access
  - Time-bound access (contract duration)
  - Specific repository access only (least privilege)
  - Access removal upon contract end
  - Contractor code contribution review

**Your SE Framework Must Provide:**
- **Access Control Policy** - who can access source code and how
- **Repository Security Configuration** - branch protection, secret scanning
- **Access Monitoring** - audit logs and access reviews
- **Evidence Collection Framework** - access logs, review results, security scan results

### 2. Document Length and Quality Guidelines

**Python Scripts:**
- Scripts should be **as long as required** to meet quality standards
- No arbitrary line limits - focus on correctness and robustness
- Source code access assessment may require API integration with Git platforms
- Quality > arbitrary length constraints

**Policy Document (POL):**
- Should be **comprehensive but not over-engineered**
- Include everything necessary for implementation and audit
- This is a single control, focused on access control
- Expected range: 400-600 lines total
- "Just right" - not too short (incomplete), not too long (overkill)

**Implementation Guide (IMP):**
- Should be **practical and focused**
- Step-by-step procedures without unnecessary elaboration
- Include examples for common Git platforms

**Annexes:**
- Git platform comparison (GitHub, GitLab, Bitbucket, Azure DevOps)
- Branch protection configuration examples
- Secret scanning tool comparison

### 3. Document Structure (Adapted for A.8.4)

```
ISMS-A.8.4-Access-to-Source-Code/
├── 00_pol-struc/
│   └── [Policy planning notes]
├── 10_pol-md/
│   ├── ISMS-POL-A.8.4-S1-Executive-Summary-Control-Alignment.md
│   ├── ISMS-POL-A.8.4-S2-Source-Code-Access-Control-Policy.md
│   ├── ISMS-POL-A.8.4-S3-Assessment-Evidence-Framework.md
│   └── ISMS-POL-A.8.4-Annex-[Topic].md [if needed]
├── 30_imp-md/
│   ├── ISMS-IMP-A.8.4-S1-Repository-Access-Control-Implementation.md
│   ├── ISMS-IMP-A.8.4-S2-Branch-Protection-Configuration.md
│   ├── ISMS-IMP-A.8.4-S3-Source-Code-Access-Assessment.md
│   └── ISMS-IMP-A.8.4-Annex-[Topic].md [if needed]
└── 50_scripts-excel/
    ├── generate_assessment_1_repository_access.py
    ├── generate_assessment_2_branch_protection.py
    └── generate_dashboard_source_code_security.py
```

### 4. Policy Content Requirements (Specific to A.8.4)

**Section 1 (S1): Executive Summary, Control Alignment, Scope**
- ISO 27001:2022 control text for A.8.4 (exact quote)
- Executive summary explaining source code access control
- Scope: All source code repositories
- Integration with other controls (IAM, secure development, change management)

**Section 2 (S2): Source Code Access Control Policy**
Focus on **A.8.4 - Access to Source Code** specifically:
- Access control policy (who, what, how)
- Repository classification (production, tools, open source)
- Access levels (read, write, admin)
- Branch protection requirements
- Secret management (prohibition, scanning, rotation)
- Backup and recovery
- Audit logging
- IP protection (NDAs, ownership)
- Third-party access (time-bound, least privilege)
- Measurable requirements with audit verification criteria

**Section 3 (S3): Assessment Methodology and Evidence Framework**
- Repository access review methodology
- Branch protection compliance assessment
- Secret scanning results analysis
- Access log analysis
- Evidence collection
- Compliance scoring

### 5. Implementation Guidance Requirements

**IMP-S1: Repository Access Control Implementation**
- Repository access approval workflow
- Access provisioning (GitHub, GitLab, Bitbucket, Azure DevOps)
- Access deprovisioning (leaver process)
- Access review procedures

**IMP-S2: Branch Protection Configuration**
- Branch protection rules (main/master, release branches)
- Pull request requirements (code review, approvals)
- Status checks (CI/CD integration)
- Signed commits configuration

**IMP-S3: Source Code Access Assessment**
- Access audit procedures
- Branch protection verification
- Secret scanning implementation and monitoring
- Continuous compliance validation

### 6. Assessment Tools (Specific to A.8.4)

**Assessment Workbook 1: Repository Access Compliance**
- Repository inventory (name, classification, owner)
- User access matrix (user → repositories → access level)
- Access justification documentation
- Last access review date
- Access compliance status (appropriate/excessive/orphaned)

**Assessment Workbook 2: Branch Protection Compliance**
- Repository → branch protection status
- Pull request requirements (enabled/disabled)
- Required approvals (count)
- Status checks (CI/CD tests)
- Signed commits (enabled/disabled)
- Protection rule compliance score

**Dashboard: Source Code Security Overview**
- Overall source code access compliance score
- Repositories with branch protection (%)
- Users with excessive access (count)
- Secret scanning findings (count by severity)
- Access review completion rate (%)
- Trend analysis

### 7. Python Scripts Approach

Scripts should:
- Parse Git platform APIs (GitHub, GitLab, Bitbucket, Azure DevOps)
- Generate repository access matrices
- Verify branch protection configurations
- Parse secret scanning results
- Calculate compliance scores
- Generate dashboards

**No arbitrary line limits** - Git API integration can be complex.

### 8. Key Integration Points

**Integrates with:**
- A.8.25-26-29 (Secure Development) - Development security framework
- A.5.15-16-18 (IAM) - Access control foundation
- A.8.2-3-5 (Auth-PAM) - Authentication (MFA for repository access)
- A.8.32 (Change Management) - Code deployment
- A.5.24-27 (Incident Management) - Code compromise incidents

### 9. Quality Checks

- [ ] Control text quoted correctly (A.8.4)
- [ ] Framework works for any Git platform
- [ ] No assumptions about technology stack
- [ ] Assessment workbooks comprehensive
- [ ] Branch protection guidance clear
- [ ] Secret scanning covered

### 10. Regulatory Framework (per ISMS-POL-00)

**Mandatory Compliance (Tier 1):**
- ISO/IEC 27001:2022: Control A.8.4

**Conditional Compliance (Tier 2):**
- **FINMA** (if Swiss financial institution):
  - FINMA Circular 2023/1 Margin 50-62: Information security includes source code protection
- **DORA** (if EU financial entity):
  - Article 9: ICT asset management includes source code
- **NIS2** (if essential/important entity):
  - Article 21(2): Asset management includes source code

**Informational Reference (Tier 3):**
- NIST SP 800-218: Secure Software Development Framework (source code security)
- CIS Control 16: Application Software Security

For complete regulatory categorization, refer to ISMS-POL-00.

### 11. Special Considerations

**Git Platform Diversity:**
- GitHub (most popular, SaaS)
- GitLab (self-hosted or SaaS)
- Bitbucket (Atlassian ecosystem)
- Azure DevOps (Microsoft ecosystem)
- AWS CodeCommit, Google Cloud Source Repositories
- Framework must be platform-neutral

**Open Source Considerations:**
- Public repositories (intentionally public code)
- Private repositories (proprietary code)
- Open source contributions (public but controlled process)
- Forked repositories (external code, internal modifications)

**Branch Protection Best Practices:**
- Main/master branch: Require pull requests, 1-2 approvals, status checks
- Release branches: Same as main
- Development branches: Lighter protection or none
- Hotfix branches: Fast-track approval process

**Secret Scanning:**
- Pre-commit hooks (prevent secrets from entering repository)
- Server-side scanning (detect secrets already in repository)
- Secret rotation procedures (if secret exposed)

### 12. Autonomous Work Requirements

Follow standard autonomous work requirements:
- READ reference implementations
- UPDATE with source code access context
- TEST (UTF-8, formulas, scripts)
- PRESENT complete deliverables

### 13. Deliverable Sequence

1. **Structure Plan** - Confirm approach
2. **Policy Sections** (S1→S2→S3) - Wait for approval
3. **Implementation Sections** (S1→S2→S3) - Wait for approval
4. **Assessment Scripts** - Test thoroughly
5. **Quality Review** - Self-assessment

---

## Your Mission for A.8.4

Create the **Source Code Access Control Framework** that provides:
- Clear access control policy for source code repositories
- Branch protection and security configuration guidance
- Secret management and scanning
- Comprehensive access monitoring and review
- Technology and platform-agnostic principles

Use Systems Engineering methodology for **systematic source code access assessment**.

Make it completely generic - works for any Git platform, any organization.

Think like a security architect AND an auditor.

**Ready? Let's start with the structure plan.**
