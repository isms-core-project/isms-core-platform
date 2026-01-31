# ISMS-POL-A.8.4-S2
## Source Code Access Control Policy

**Document ID**: ISMS-POL-A.8.4-S2  
**Title**: Source Code Access Control Policy - Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial policy requirements |

**Review Cycle**: Annual  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Chief Technology Officer (CTO)

**Distribution**: All personnel with source code access  
**Related Documents**: ISMS-POL-A.8.4-S1 (Purpose and Scope), ISMS-IMP-A.8.4 (Implementation Guides)

---

## 2.1 Access Control Framework

### 2.1.1 General Access Control Principles

**REQ-2.1.1-001**: All source code repositories SHALL implement role-based access control (RBAC) with the principle of least privilege.

**REQ-2.1.1-002**: Access to source code repositories SHALL be granted only based on documented business need and approved by the repository owner.

**REQ-2.1.1-003**: Default repository permissions SHALL be "no access" - explicit grant required for any access level.

**REQ-2.1.1-004**: Repository access SHALL be reviewed quarterly for continued business justification.

**REQ-2.1.1-005**: Repository access SHALL be automatically revoked upon employment termination, role change, or contract expiration.

**Audit Verification**:
- Evidence: Repository access logs showing RBAC implementation
- Evidence: Access request approval records
- Evidence: Quarterly access review completion records
- Evidence: Automated deprovisioning logs

### 2.1.2 Access Request and Approval Workflow

**REQ-2.1.2-001**: All repository access requests SHALL include:
- Requestor name and role
- Repository name and classification
- Access level requested (read/write/admin)
- Business justification
- Expected duration of access (if time-bound)

**REQ-2.1.2-002**: Repository access requests SHALL be approved by:
- Repository owner (mandatory)
- Development team lead (for write access or higher)
- CISO or delegate (for admin access to production repositories)

**REQ-2.1.2-003**: Access SHALL be provisioned within 24 hours of approval during business hours.

**REQ-2.1.2-004**: All access requests and approvals SHALL be documented and retained for audit purposes (minimum 3 years).

**REQ-2.1.2-005**: Emergency access requests SHALL follow expedited approval process with post-facto review within 48 hours.

**Audit Verification**:
- Evidence: Access request tickets/forms
- Evidence: Approval email records or workflow logs
- Evidence: Provisioning timestamps
- Evidence: Access request retention records

### 2.1.3 Access Deprovisioning

**REQ-2.1.3-001**: Repository access SHALL be removed within 24 hours of:
- Employment termination
- Role change (where access is no longer required)
- Contract expiration (for external personnel)
- Repository owner request
- Security incident involving the account

**REQ-2.1.3-002**: Automated deprovisioning SHALL be implemented where technically feasible through integration with HR systems or identity management platforms.

**REQ-2.1.3-003**: Manual deprovisioning processes SHALL include verification checklist to ensure complete access removal.

**REQ-2.1.3-004**: Deprovisioning SHALL be logged with timestamp, actor, and reason for access removal.

**Audit Verification**:
- Evidence: Deprovisioning logs showing timely access removal
- Evidence: HR system integration for automated deprovisioning
- Evidence: Deprovisioning checklist completion records

### 2.1.4 Access Reviews

**REQ-2.1.4-001**: Repository owners SHALL conduct access reviews quarterly for all repositories under their responsibility.

**REQ-2.1.4-002**: Access reviews SHALL verify:
- All users with access still require access based on current role
- Access level is appropriate (not excessive)
- No orphaned accounts (accounts of former employees)
- Service accounts are still active and required
- Third-party access is still within contract period

**REQ-2.1.4-003**: Access review results SHALL be documented with date, reviewer, findings, and remediation actions.

**REQ-2.1.4-004**: Excessive access identified during reviews SHALL be remediated within 14 days.

**REQ-2.1.4-005**: Orphaned accounts SHALL be disabled immediately and removed within 7 days.

**Audit Verification**:
- Evidence: Access review completion reports (quarterly)
- Evidence: Remediation records for excessive access
- Evidence: Orphaned account removal logs

---

## 2.2 Repository Classification

### 2.2.1 Classification Framework

**REQ-2.2.1-001**: All source code repositories SHALL be classified according to sensitivity and criticality:

**Production Code Repositories**:
- Definition: Source code for customer-facing applications, critical internal systems, or revenue-generating services
- Classification: Confidential or higher
- Protection Level: Maximum (all controls apply)
- Examples: Customer web applications, mobile apps, payment processing systems, core business logic

**Internal Tools Repositories**:
- Definition: Source code for internal automation, utilities, or non-customer-facing tools
- Classification: Internal
- Protection Level: High (most controls apply)
- Examples: Deployment automation, internal dashboards, administrative tools, testing frameworks

**Open Source Contribution Repositories**:
- Definition: Organization's contributions to public open source projects or internally-developed open source
- Classification: Public (but access still controlled)
- Protection Level: Medium (access control and monitoring apply)
- Examples: Public GitHub repositories, contributions to third-party open source projects

**Archived/Deprecated Repositories**:
- Definition: Code no longer in active development, superseded by newer systems, or end-of-life applications
- Classification: Internal (minimum)
- Protection Level: Read-only access, limited monitoring
- Examples: Legacy applications, replaced systems, retired prototypes

**REQ-2.2.1-002**: Repository classification SHALL be documented in repository metadata (description, tags, or properties).

**REQ-2.2.1-003**: Repository classification SHALL be reviewed annually and updated when repository purpose changes.

**Audit Verification**:
- Evidence: Repository inventory with classification
- Evidence: Repository metadata showing classification
- Evidence: Annual classification review records

### 2.2.2 Classification-Based Access Controls

**REQ-2.2.2-001**: Production code repositories SHALL require:
- Minimum two-person review for all code merges
- Branch protection on main and release branches
- Signed commits (where technically feasible)
- Daily secret scanning
- Quarterly access reviews

**REQ-2.2.2-002**: Internal tools repositories SHALL require:
- Minimum one-person review for code merges to main branch
- Branch protection on main branch
- Weekly secret scanning
- Quarterly access reviews

**REQ-2.2.2-003**: Open source contribution repositories SHALL require:
- Access control (not publicly writable)
- Review process for contributions
- Secret scanning before public push
- No internal secrets or credentials in public repositories

**REQ-2.2.2-004**: Archived/deprecated repositories SHALL:
- Be set to read-only mode
- Have write access removed from all users
- Retain access logs
- Be documented as archived with deprecation date

**Audit Verification**:
- Evidence: Branch protection configuration per classification
- Evidence: Code review requirements enforcement
- Evidence: Secret scanning frequency logs
- Evidence: Archived repository read-only status

---

## 2.3 Role-Based Access Control

### 2.3.1 Access Roles and Permissions

**REQ-2.3.1-001**: Repository access SHALL be granted based on the following roles:

**Developers (Write Access)**:
- Clone and pull repositories
- Create branches and commits
- Push to non-protected branches
- Submit pull requests
- Assign reviewers
- **Restrictions**: Cannot push directly to protected branches, cannot approve own pull requests, cannot modify repository settings

**Security Team (Read Access to All Repositories)**:
- Clone and pull all repositories for security reviews
- Read source code and commit history
- Access for security audits and vulnerability assessments
- **Restrictions**: Cannot commit changes, cannot modify repository settings (unless specifically granted)

**Auditors (Time-Bound Read Access)**:
- Read-only access to repositories during audit period
- Access to audit logs and permission reports
- **Restrictions**: No write access, access automatically expires after audit completion, time-bound to specific audit timeframe

**External Contractors (Time-Bound, Repository-Specific Write Access)**:
- Access limited to specific repositories for contracted work
- Write access for contributions
- **Restrictions**: Access expires on contract end date, cannot access repositories outside project scope, all commits subject to enhanced review

**Repository Administrators**:
- Manage repository settings
- Configure branch protection
- Manage collaborator access
- **Restrictions**: Admin access does not automatically grant code write access (separation of duties), admin actions are logged

**Repository Owners**:
- Ultimate responsibility for repository
- Approve access requests
- Conduct access reviews
- Set repository classification
- May or may not have write access to code (role-dependent)

**REQ-2.3.1-002**: Service accounts (CI/CD, deployment automation, security scanners) SHALL:
- Be created with descriptive names indicating purpose
- Have access limited to specific repositories required for automation
- Use token-based authentication with expiration
- Be reviewed quarterly for continued need
- Be documented with owner and purpose

**Audit Verification**:
- Evidence: Repository permission reports showing role-based access
- Evidence: Service account inventory with purpose documentation
- Evidence: Quarterly service account reviews

### 2.3.2 Least Privilege Enforcement

**REQ-2.3.2-001**: Users SHALL be granted the minimum access level required for their role:
- Read access for code reviews or reference only
- Write access only if contributing code
- Admin access only for repository management responsibilities

**REQ-2.3.2-002**: Users with write access to multiple repositories SHALL have access justified individually per repository.

**REQ-2.3.2-003**: Admin access SHALL be granted sparingly and limited to personnel with repository management responsibilities.

**REQ-2.3.2-004**: "Admin" or "owner" access SHALL NOT be granted to external contractors except in documented exceptional cases with CISO approval.

**Audit Verification**:
- Evidence: Access justification documentation per user per repository
- Evidence: Admin access audit showing minimal admin users
- Evidence: CISO approval for exceptional admin access grants

---

## 2.4 Branch Protection Requirements

### 2.4.1 Main Branch Protection

**REQ-2.4.1-001**: The main branch (master/main/trunk) of production and internal tools repositories SHALL be protected with:
- Direct commits blocked (no force push)
- Pull request required before merging
- Minimum number of reviewers: 2 for production, 1 for internal tools
- Dismiss stale pull request approvals when new commits pushed
- Require review from code owners (where code owners defined)
- Status checks must pass before merge (CI/CD tests, linters, security scans)
- Signed commits required (where technically feasible)
- Linear history enforced (no merge commits, rebase required)
- Restrictions on who can dismiss reviews or push to branch

**REQ-2.4.1-002**: Only repository administrators SHALL be able to modify branch protection rules.

**REQ-2.4.1-003**: Temporary branch protection rule removal SHALL require documented justification, CISO approval, and automatic re-enablement after specified time period.

**Audit Verification**:
- Evidence: Branch protection configuration exports
- Evidence: Branch protection rule modification logs
- Evidence: Temporary protection removal approval records

### 2.4.2 Release Branch Protection

**REQ-2.4.2-001**: Release branches (release/*, hotfix/*) SHALL have protection rules equivalent to main branch.

**REQ-2.4.2-002**: Hotfix branches MAY have expedited review process but SHALL NOT bypass review entirely.

**Audit Verification**:
- Evidence: Branch protection rules for release branches
- Evidence: Hotfix review process documentation

### 2.4.3 Development and Feature Branch Protection

**REQ-2.4.3-001**: Development and feature branches MAY have lighter protection based on repository classification:
- Production repositories: Optional branch protection, recommended for long-lived development branches
- Internal tools: No required protection
- Open source: Protection rules as defined by project governance

**REQ-2.4.3-002**: Branches SHALL be deleted after merge to reduce clutter and attack surface.

**Audit Verification**:
- Evidence: Branch cleanup policies
- Evidence: Stale branch reports

### 2.4.4 Pull Request Requirements

**REQ-2.4.4-001**: Pull requests SHALL include:
- Descriptive title and description of changes
- Link to relevant ticket/issue (where applicable)
- Test results (unit tests, integration tests)
- Security scan results (no critical vulnerabilities)
- Documentation updates (if applicable)

**REQ-2.4.4-002**: Code reviewers SHALL:
- Review code for functionality, security, and adherence to standards
- Verify tests are included and passing
- Check for potential security issues
- Approve only when satisfied with code quality
- NOT approve their own pull requests

**REQ-2.4.4-003**: Pull request approvals SHALL be dismissed if new commits are pushed after approval.

**REQ-2.4.4-004**: All conversations in pull requests SHALL be resolved before merge.

**Audit Verification**:
- Evidence: Pull request review records
- Evidence: Pull request approval logs
- Evidence: Conversation resolution enforcement

---

## 2.5 Secret Management

### 2.5.1 Secret Prohibition

**REQ-2.5.1-001**: The following items SHALL NOT be stored in source code repositories:
- Passwords, passphrases, or password hashes
- API keys, tokens, or access credentials
- Private keys, certificates, or cryptographic secrets
- Database connection strings with embedded credentials
- Cloud provider credentials (AWS keys, Azure secrets, GCP service account keys)
- Third-party service credentials
- Personally Identifiable Information (PII)
- Payment card data
- Any other sensitive information defined in the organization's data classification policy

**REQ-2.5.1-002**: Configuration files containing secrets SHALL use environment variables, secret management services, or encrypted configuration stores instead of hardcoded values.

**REQ-2.5.1-003**: Test data SHALL NOT contain real production secrets or sensitive data.

**Audit Verification**:
- Evidence: Secret scanning results showing zero findings
- Evidence: Configuration file reviews
- Evidence: Test data sanitization procedures

### 2.5.2 Secret Scanning

**REQ-2.5.2-001**: All active repositories SHALL have automated secret scanning enabled.

**REQ-2.5.2-002**: Secret scanning SHALL run:
- On every commit (pre-commit hooks where feasible)
- Daily server-side scans for all repositories
- Full historical scan quarterly

**REQ-2.5.2-003**: Secret scanning SHALL detect:
- Common patterns (AWS keys, GitHub tokens, private keys, etc.)
- Organization-specific secret patterns (custom API keys, internal credentials)
- High-entropy strings that may be secrets

**REQ-2.5.2-004**: Secret scanning tools SHALL be configured with:
- Low false-positive rate (tuned patterns)
- Automatic alerts to security team and repository owners
- Integration with incident management system

**Audit Verification**:
- Evidence: Secret scanning configuration
- Evidence: Scan execution logs (daily scans)
- Evidence: Alert delivery confirmation

### 2.5.3 Secret Exposure Response

**REQ-2.5.3-001**: When a secret is detected in a repository:
1. Security team SHALL be alerted immediately
2. Secret SHALL be rotated within 4 hours (critical secrets) or 24 hours (non-critical)
3. Repository access logs SHALL be reviewed for unauthorized access
4. Incident SHALL be documented and root cause analysis conducted
5. Developer SHALL be trained on proper secret management

**REQ-2.5.3-002**: Secrets in commit history SHALL be removed using git history rewriting tools with caution and proper backups.

**REQ-2.5.3-003**: If a secret was exposed in a public repository:
- Assume secret is compromised immediately
- Rotate secret within 1 hour
- Assess impact and potential exposure
- Notify affected parties if required
- File security incident report

**Audit Verification**:
- Evidence: Secret exposure incident records
- Evidence: Secret rotation logs with timestamps
- Evidence: Developer training completion records

---

## 2.6 Authentication and Multi-Factor Authentication (MFA)

### 2.6.1 Authentication Requirements

**REQ-2.6.1-001**: Access to source code repositories SHALL require authentication using:
- Corporate single sign-on (SSO) where available
- Strong passwords (minimum 12 characters, complexity requirements) if SSO not available
- SSH keys (minimum 2048-bit RSA or equivalent) for git operations
- Personal access tokens (PATs) for API or automation access

**REQ-2.6.1-002**: Shared credentials SHALL NOT be used for repository access - each individual SHALL have unique credentials.

**REQ-2.6.1-003**: Service account credentials SHALL:
- Be stored securely (secret management system)
- Have limited scope (access only required repositories)
- Be rotated quarterly or when personnel changes occur

**Audit Verification**:
- Evidence: Authentication method configuration
- Evidence: Absence of shared credentials
- Evidence: Service account credential rotation logs

### 2.6.2 Multi-Factor Authentication (MFA)

**REQ-2.6.2-001**: Multi-factor authentication SHALL be required for:
- All human users accessing repositories (developers, security team, auditors, contractors)
- Repository administrative access
- Repository access from external networks

**REQ-2.6.2-002**: MFA methods SHALL include at least one of:
- Time-based one-time password (TOTP) apps (Google Authenticator, Authy, etc.)
- Hardware security keys (YubiKey, etc.)
- Push notification to registered mobile device
- SMS-based codes (least preferred, only if other methods unavailable)

**REQ-2.6.2-003**: MFA SHALL NOT be bypassable through alternative authentication methods.

**REQ-2.6.2-004**: Service accounts and automation tools SHALL use token-based authentication with restricted scopes instead of MFA.

**Audit Verification**:
- Evidence: MFA enrollment reports showing 100% coverage
- Evidence: MFA enforcement configuration
- Evidence: Failed MFA attempts logs

---

## 2.7 Audit Logging and Monitoring

### 2.7.1 Logging Requirements

**REQ-2.7.1-001**: Repository platforms SHALL log the following activities:
- **Access Events**: Login attempts (successful and failed), logout events, session duration
- **Repository Access**: Clone operations, pull operations, repository browsing
- **Code Changes**: Commits (author, timestamp, commit message, files changed), pushes, force pushes
- **Branch Operations**: Branch creation, branch deletion, branch protection changes
- **Pull Request Activities**: PR creation, review, approval, merge, rejection
- **Permission Changes**: Access granted, access revoked, role changes, permission modifications
- **Administrative Actions**: Repository settings changes, collaborator management, integration configurations
- **Security Events**: Secret scanning alerts, failed authentication, suspicious access patterns

**REQ-2.7.1-002**: Logs SHALL include minimum metadata:
- Timestamp (UTC)
- User identity (username or service account)
- Source IP address
- Action performed
- Repository affected
- Success or failure status

**REQ-2.7.1-003**: Logs SHALL be tamper-evident and protected from unauthorized modification or deletion.

**Audit Verification**:
- Evidence: Log configuration showing required events
- Evidence: Sample logs demonstrating metadata completeness
- Evidence: Log integrity controls

### 2.7.2 Log Retention

**REQ-2.7.2-001**: Repository access logs SHALL be retained for minimum:
- Access events: 1 year
- Code change events: 3 years (or life of repository if shorter)
- Permission changes: 3 years
- Security events: 3 years
- Administrative actions: 3 years

**REQ-2.7.2-002**: Logs for production repositories SHALL be retained for longer periods based on regulatory requirements.

**REQ-2.7.2-003**: Archived repositories SHALL retain logs even after repository archival.

**Audit Verification**:
- Evidence: Log retention configuration
- Evidence: Log archive storage showing retention periods
- Evidence: Log purging policies and execution

### 2.7.3 Log Monitoring and Alerting

**REQ-2.7.3-001**: Repository access logs SHALL be monitored for:
- Multiple failed authentication attempts (brute force)
- Access from unusual geographic locations
- Access outside normal business hours (for role-based anomalies)
- Bulk download operations
- Permission elevation attempts
- Force pushes to protected branches
- Secret scanning alerts
- Large-scale access pattern changes

**REQ-2.7.3-002**: Security alerts SHALL be generated and sent to security operations team within 15 minutes of detection.

**REQ-2.7.3-003**: Critical security events (confirmed unauthorized access, mass permission changes) SHALL trigger immediate incident response.

**Audit Verification**:
- Evidence: Log monitoring rules configuration
- Evidence: Alert delivery testing results
- Evidence: Security event response records

---

## 2.8 Backup and Recovery

### 2.8.1 Backup Requirements

**REQ-2.8.1-001**: All source code repositories SHALL be backed up:
- Frequency: Daily incremental backups, weekly full backups
- Retention: Minimum 90 days for active repositories, minimum 7 years for production repositories
- Geographic redundancy: Backups stored in different geographic location than primary repository

**REQ-2.8.1-002**: Backups SHALL include:
- Source code (all branches, all commits, full history)
- Repository metadata (permissions, settings, configurations)
- Pull request history and discussions
- Issue tracking data (if integrated)
- Wikis and documentation

**REQ-2.8.1-003**: Backups SHALL be encrypted at rest using organizationally-approved encryption standards.

**REQ-2.8.1-004**: Backup access SHALL be restricted to authorized backup administrators and require MFA.

**Audit Verification**:
- Evidence: Backup schedule and execution logs
- Evidence: Backup retention records
- Evidence: Backup encryption configuration
- Evidence: Backup access control lists

### 2.8.2 Recovery Testing

**REQ-2.8.2-001**: Repository recovery procedures SHALL be tested:
- Quarterly for production repositories
- Annually for internal tools repositories
- After major platform upgrades or configuration changes

**REQ-2.8.2-002**: Recovery testing SHALL verify:
- Repository restoration within Recovery Time Objective (RTO: 4 hours for production, 24 hours for non-production)
- Data integrity (all commits, branches, history intact)
- Permission restoration
- Functionality of restored repository

**REQ-2.8.2-003**: Recovery test results SHALL be documented including success/failure, time to recover, and issues identified.

**Audit Verification**:
- Evidence: Recovery test schedule
- Evidence: Recovery test results with timestamps
- Evidence: Issues identified and remediation

---

## 2.9 Intellectual Property Protection

### 2.9.1 Confidentiality Agreements

**REQ-2.9.1-001**: All personnel with source code access SHALL sign:
- Non-Disclosure Agreement (NDA) prior to repository access
- Intellectual Property Assignment Agreement (transferring code ownership to organization)
- Acceptable Use Policy acknowledgment

**REQ-2.9.1-002**: External contractors and third parties SHALL sign:
- NDA specific to project and code access
- Contract terms explicitly addressing code ownership and usage restrictions
- Acceptable use terms prohibiting unauthorized code distribution

**REQ-2.9.1-003**: NDAs SHALL remain in effect for minimum 5 years after access termination.

**Audit Verification**:
- Evidence: Signed NDA repository for all personnel with access
- Evidence: Contractor agreement library
- Evidence: IP assignment documentation

### 2.9.2 Code Ownership Documentation

**REQ-2.9.2-001**: Repository metadata SHALL clearly document:
- Code ownership (organization or third party)
- Licensing terms (proprietary, open source license type)
- Copyright statements
- Contribution guidelines

**REQ-2.9.2-002**: Third-party code integrated into repositories SHALL be:
- Documented with source and license information
- License-compatible with organization's usage
- Tracked in software bill of materials (SBOM)

**Audit Verification**:
- Evidence: Repository LICENSE files
- Evidence: THIRD-PARTY-NOTICES documentation
- Evidence: Software Bill of Materials (SBOM)

### 2.9.3 Export Control Compliance

**REQ-2.9.3-001**: Source code containing controlled technologies (cryptography, dual-use technologies) SHALL:
- Be clearly marked with export control classification
- Have access restricted based on nationality requirements (if applicable)
- Require export compliance review before sharing outside approved jurisdictions

**REQ-2.9.3-002**: Repositories subject to export control SHALL maintain access logs showing only authorized personnel accessed controlled code.

**Audit Verification**:
- Evidence: Export control classification documentation
- Evidence: Access logs for controlled repositories
- Evidence: Export compliance reviews

---

## 2.10 Third-Party and Contractor Access

### 2.10.1 Contractor Access Provisioning

**REQ-2.10.1-001**: External contractor access SHALL be:
- Time-bound to contract period with automatic expiration
- Limited to specific repositories required for contracted work
- Granted only after contract execution and NDA signature
- Documented with contract reference number and business justification

**REQ-2.10.1-002**: Contractor accounts SHALL be clearly identifiable (naming convention, account metadata).

**REQ-2.10.1-003**: Contractor access requests SHALL require additional approval from:
- Repository owner
- Contracting manager
- Legal/compliance (if sensitive repositories)

**Audit Verification**:
- Evidence: Contractor access inventory with contract references
- Evidence: Contractor access approval records
- Evidence: Time-bound access expiration logs

### 2.10.2 Contractor Contribution Review

**REQ-2.10.2-001**: Code contributions from external contractors SHALL undergo enhanced review:
- Minimum two internal employee reviewers (not just contractor peers)
- Security-focused review for potential backdoors or malicious code
- Code quality and standards compliance verification
- Intellectual property review (ensuring no third-party code introduced without proper licensing)

**REQ-2.10.2-002**: Contractor commits SHALL be signed to verify author identity.

**Audit Verification**:
- Evidence: Pull request reviews showing multiple internal reviewers
- Evidence: Signed commit verification for contractor contributions

### 2.10.3 Access Removal Upon Contract End

**REQ-2.10.3-001**: Contractor access SHALL be automatically revoked on contract end date.

**REQ-2.10.3-002**: Manual verification SHALL occur within 48 hours of contract end to confirm access removal.

**REQ-2.10.3-003**: If contractor relationship extends, access renewal SHALL require updated contract and new access request approval.

**Audit Verification**:
- Evidence: Automated contractor access expiration logs
- Evidence: Post-contract access verification reports
- Evidence: Access renewal approvals

---

## 2.11 Compliance Monitoring and Enforcement

### 2.11.1 Continuous Compliance Monitoring

**REQ-2.11.1-001**: Automated monitoring SHALL track:
- Repository access compliance (% repositories with proper access controls)
- Branch protection compliance (% production repositories with required protection)
- Secret scanning coverage (% repositories with active scanning)
- MFA adoption rate (% users with MFA enabled)
- Access review completion rate (% on-time quarterly reviews)

**REQ-2.11.1-002**: Compliance dashboards SHALL be available to CISO, repository owners, and audit team.

**REQ-2.11.1-003**: Non-compliance SHALL trigger automated alerts to responsible parties.

**Audit Verification**:
- Evidence: Compliance monitoring dashboard
- Evidence: Automated alert logs
- Evidence: Compliance trend reports

### 2.11.2 Violation Response

**REQ-2.11.2-001**: Policy violations SHALL be categorized:
- **Critical**: Unauthorized code modification in production, intellectual property theft, malicious code insertion
- **High**: Secret exposure, policy circumvention, repeated access violations
- **Medium**: Excessive access not remediated timely, missed access reviews
- **Low**: Documentation gaps, minor configuration deviations

**REQ-2.11.2-002**: Critical violations SHALL trigger immediate incident response and account suspension pending investigation.

**REQ-2.11.2-003**: Repeated violations SHALL result in progressive discipline up to access revocation and employment termination.

**Audit Verification**:
- Evidence: Violation incident records
- Evidence: Disciplinary action records
- Evidence: Account suspension logs

---

## 2.12 Policy Exceptions

### 2.12.1 Exception Request Process

**REQ-2.12.1-001**: Exception requests SHALL include:
- Requirement being excepted
- Business justification
- Risk assessment
- Compensating controls
- Requested exception duration
- Approval from repository owner and CISO

**REQ-2.12.1-002**: Exceptions SHALL be time-bound with defined expiration dates (maximum 12 months).

**REQ-2.12.1-003**: Exception approvals and denials SHALL be documented in exception register.

**Audit Verification**:
- Evidence: Exception register
- Evidence: CISO exception approval records
- Evidence: Compensating control implementation

### 2.12.2 Exception Monitoring

**REQ-2.12.2-001**: Active exceptions SHALL be reviewed quarterly for:
- Continued business need
- Effectiveness of compensating controls
- Opportunities to eliminate exception

**REQ-2.12.2-002**: Expired exceptions SHALL be automatically flagged and require renewal approval or exception closure.

**Audit Verification**:
- Evidence: Quarterly exception review records
- Evidence: Exception renewal or closure logs

---

**END OF SECTION 2**

**Next Document**: ISMS-POL-A.8.4-S3 (Assessment and Evidence Framework)
