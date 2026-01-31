# ISMS-POL-A.8.31-S2.4
## Environment Separation - Environment Promotion Requirements

**Document ID**: ISMS-POL-A.8.31-S2.4  
**Title**: Environment Promotion Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager / DevOps Lead | Initial promotion requirements |

**Review Cycle**: Annual (or upon SDLC process changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: IT Operations Manager / DevOps Lead
- Change Management: Change Advisory Board (CAB) Chair

**Distribution**: Security team, IT operations, development, DevOps, QA, change management  
**Related Documents**: 
- ISMS-POL-A.8.31-S1 (Executive Summary)
- ISMS-POL-A.8.32 (Change Management)
- ISMS-POL-A.8.25-26-29 (Secure Development)
- ISMS-POL-A.8.31-Annex-C (CI/CD Pipeline Integration)

---

## 2.4.1 Purpose and Scope

This section establishes **mandatory requirements** for promoting code, configurations, and changes between environments.

**Core Principle**: **Changes flow through environments in order (Dev → Test → Staging → Production). Direct deployment to production is PROHIBITED.**

**Why Environment Promotion Matters**:
- Enforces testing before production (reduces production incidents)
- Integrates with change management (each promotion is a change control gate)
- Provides audit trail (who deployed what, when, to which environment)
- Enables rollback (previous version available if deployment fails)
- Prevents configuration drift (staging matches production)

**In Scope**: All code, configuration, infrastructure, and data migration changes  
**Primary Stakeholder**: DevOps, Operations, Development, Change Management  
**Implementation Evidence**: ISMS-IMP-A.8.31 (Promotion Process Assessment)

---

## 2.4.2 Promotion Workflow Requirements

### 2.4.2.1 Mandatory Promotion Path

[Organization] **SHALL** enforce the following promotion path for all changes:

**Standard Promotion Flow**:

```
Development → Testing → Staging → Production
    ↓            ↓         ↓          ↓
  (Auto)     (Auto/Semi)  (Manual)  (Manual + CAB)
```

**Promotion Path Requirements**:
- Changes MUST start in Development environment
- Changes MUST pass Testing before reaching Staging
- Changes MUST be validated in Staging before Production
- Direct deployment to Production is PROHIBITED (except emergency hot-fixes with CISO approval)

**Environment Skip Prohibition**:
- Cannot skip Testing (Dev → Staging directly) without documented exception
- Cannot skip Staging (Dev → Production directly) - ABSOLUTE PROHIBITION
- Cannot deploy different code to Production than validated in Staging

**Audit Verification Criteria**:
- ✅ Deployment pipeline enforces promotion path
- ✅ Zero direct deployments to Production (except approved emergencies)
- ✅ All production deployments preceded by staging validation
- ✅ Environment skip requests documented and approved (if allowed)

### 2.4.2.2 Promotion Approval Gates

[Organization] **SHALL** implement approval gates per environment tier:

**Approval Requirements by Environment**:

| Promotion | Approval Required | Approver | Automation |
|-----------|------------------|----------|------------|
| Dev → Test | Optional (recommended: peer review) | Developer / Tech Lead | Automated (CI pipeline) |
| Test → Staging | Required (QA sign-off) | QA Manager | Semi-automated (manual trigger) |
| Staging → Production | Required (CAB approval) | Change Advisory Board | Manual (operations team) |
| Emergency Production | Required (CISO + Incident Commander) | CISO | Manual (break-glass) |

**Development → Testing Promotion**:
- Code review completed (peer reviewed and approved)
- Automated tests pass (unit tests, integration tests)
- Security scan pass (SAST, dependency vulnerability scan)
- Approval: Tech Lead or Senior Developer (optional but recommended)

**Testing → Staging Promotion**:
- Functional testing complete (test cases pass)
- Security testing complete (DAST, penetration test for major changes)
- Performance testing complete (if applicable)
- Approval: QA Manager (mandatory)

**Staging → Production Promotion**:
- UAT sign-off (business users approve functionality)
- Production deployment plan reviewed
- Rollback plan documented and tested
- Change management approval (CAB or equivalent)
- Approval: Change Advisory Board + IT Operations Manager (mandatory)

**Audit Verification Criteria**:
- ✅ All promotions have required approvals (100% compliance)
- ✅ Approval records retained for audit (12 months minimum)
- ✅ Unapproved deployments blocked automatically
- ✅ Approval process documented in SDLC documentation

---

## 2.4.3 Automated Deployment Pipeline Requirements

### 2.4.3.1 CI/CD Pipeline Configuration

[Organization] **SHALL** use automated deployment pipelines to enforce environment separation:

**Pipeline Architecture Requirements**:
- Separate pipeline jobs per environment (dev pipeline, test pipeline, staging pipeline, prod pipeline)
- Environment-specific configuration injected at deploy time (not hardcoded)
- Promotion triggers explicit (manual approval required for staging → prod)
- Deployment artifacts versioned and tagged (artifact version matches environment deployment)

**Pipeline Stages** (typical):

**Development Pipeline**:
1. Code commit (developer pushes to feature branch)
2. Automated build (compile, package)
3. Automated tests (unit tests, static analysis)
4. Security scan (SAST, dependency check)
5. Deploy to Development environment (automatic if tests pass)

**Testing Pipeline**:
1. Trigger: Development pipeline success + approval (optional)
2. Deploy to Testing environment
3. Automated integration tests
4. Automated security tests (DAST)
5. QA notification (manual testing begins)

**Staging Pipeline**:
1. Trigger: QA approval (manual)
2. Deploy to Staging environment
3. Smoke tests (automated post-deployment validation)
4. UAT notification (business users test)

**Production Pipeline**:
1. Trigger: CAB approval (manual)
2. Pre-deployment checks (staging validation confirmed, rollback plan ready)
3. Deploy to Production environment (controlled deployment window)
4. Smoke tests (automated post-deployment validation)
5. Monitoring (alert if deployment causes issues)

**Audit Verification Criteria**:
- ✅ CI/CD pipelines documented and version controlled
- ✅ Pipeline enforces promotion path (cannot skip environments)
- ✅ Production deployment requires manual approval
- ✅ Pipeline logs retained for audit (12 months)

### 2.4.3.2 Deployment Artifact Management

[Organization] **SHALL** manage deployment artifacts to ensure consistency:

**Artifact Requirements**:
- Build artifacts once, deploy to all environments (same artifact promoted, not rebuilt)
- Artifacts versioned (semantic versioning: major.minor.patch)
- Artifacts tagged with environment (dev-v1.2.3, test-v1.2.3, prod-v1.2.3)
- Artifacts stored in artifact repository (Artifactory, Nexus, container registry)
- Artifacts immutable (cannot modify after build)

**Artifact Promotion**:
- Same artifact deployed to all environments (dev artifact becomes test artifact becomes prod artifact)
- Configuration differences injected at deployment (not baked into artifact)
- Artifact checksum verified at deployment (integrity validation)

**Audit Verification Criteria**:
- ✅ Artifact repository configured and used
- ✅ Same artifact deployed across environments (verified by checksum)
- ✅ Artifact version matches deployment records
- ✅ Artifacts retained per retention policy

---

## 2.4.4 Configuration Management During Promotion

### 2.4.4.1 Environment-Specific Configuration

[Organization] **SHALL** manage configuration separately from code:

**Configuration Separation**:
- Application code (business logic) separate from configuration (environment-specific settings)
- Configuration stored outside artifact (injected at deployment time)
- Configuration version controlled (separate repo or separate branch)
- Configuration changes follow same promotion path as code

**Configuration Storage Options**:
- **Environment variables**: Set by deployment pipeline (DATABASE_URL=...)
- **Configuration files**: Separate files per environment (config.dev.yaml, config.prod.yaml)
- **Configuration management systems**: Ansible, Chef, Puppet (environment-specific playbooks)
- **Secret management**: Vault, AWS Secrets Manager, Azure Key Vault (credentials injected)

**Configuration Promotion**:
- Configuration tested in lower environments before production
- Staging configuration mirrors production (except for environment-specific values like URLs)
- Configuration drift detection (alert if prod config deviates from approved baseline)

**Audit Verification Criteria**:
- ✅ Configuration separate from code
- ✅ Configuration version controlled
- ✅ Configuration changes approved (like code changes)
- ✅ Staging configuration mirrors production

### 2.4.4.2 Secret and Credential Management

[Organization] **SHALL** manage secrets securely during promotion:

**Secret Handling**:
- Secrets NEVER in source code (enforced by pre-commit hooks)
- Secrets NEVER in artifact (injected at deployment)
- Secrets stored in secret management system (Vault, cloud secret managers)
- Secrets separate per environment (dev secrets ≠ prod secrets)

**Secret Injection at Deployment**:
- Deployment pipeline retrieves secrets from secret manager
- Secrets injected as environment variables or configuration files
- Secrets never logged or displayed (masked in pipeline logs)
- Secrets rotated after exposure or personnel change

**Audit Verification Criteria**:
- ✅ No secrets in source code (scanned on every commit)
- ✅ Secrets stored in secret management system
- ✅ Secret injection automated (no manual copy-paste)
- ✅ Secret rotation schedule documented and followed

---

## 2.4.5 Testing and Validation Requirements

### 2.4.5.1 Pre-Promotion Testing

[Organization] **SHALL** execute testing before promoting to next environment:

**Development → Testing Promotion Testing**:
- Unit tests (100% pass required)
- Code coverage (minimum threshold defined per project)
- Static application security testing (SAST)
- Dependency vulnerability scanning
- Linting and code quality checks

**Testing → Staging Promotion Testing**:
- Functional testing (test cases documented and executed)
- Integration testing (system components work together)
- Dynamic application security testing (DAST)
- API testing (if applicable)
- QA sign-off (manual testing complete)

**Staging → Production Promotion Testing**:
- User acceptance testing (UAT) - business users approve
- Performance testing (load testing, stress testing if applicable)
- Security validation (penetration test for major changes)
- Regression testing (existing functionality not broken)
- Smoke tests in staging (automated post-deployment validation)

**Audit Verification Criteria**:
- ✅ Test execution documented (test results logged)
- ✅ Test failures block promotion (deployment does not proceed)
- ✅ Test coverage meets minimum thresholds
- ✅ Security testing included in promotion gates

### 2.4.5.2 Post-Deployment Validation

[Organization] **SHALL** validate successful deployment after promotion:

**Smoke Tests** (automated, fast validation):
- Application starts successfully
- Health check endpoints respond (HTTP 200 OK)
- Database connections successful
- Critical functionality works (login, basic operations)

**Deployment Verification**:
- Correct version deployed (version number matches expected)
- Configuration applied correctly (environment-specific settings active)
- No errors in application logs (first 5 minutes post-deployment)
- Monitoring dashboards show normal metrics

**Rollback Trigger**:
- Smoke tests fail → Automatic rollback (or alert operations team)
- Error rate spike post-deployment → Investigate and potentially rollback
- Performance degradation → Investigate and potentially rollback
- Business critical functionality broken → Emergency rollback

**Audit Verification Criteria**:
- ✅ Smoke tests executed post-deployment (100% of deployments)
- ✅ Smoke test failures trigger rollback or alert
- ✅ Deployment verification checklist completed
- ✅ Post-deployment issues documented and tracked

---

## 2.4.6 Rollback and Recovery

### 2.4.6.1 Rollback Planning

[Organization] **SHALL** plan for rollback before production deployment:

**Rollback Plan Requirements**:
- Rollback procedure documented before production deployment
- Rollback tested in staging (practice rollback before production)
- Rollback time estimated (how long to revert to previous version)
- Data migration rollback considered (can database changes be reversed?)

**Rollback Triggers**:
- Deployment validation failures (smoke tests fail)
- Critical functionality broken (show-stopper bugs)
- Performance degradation (application unusably slow)
- Security incident (deployment introduces vulnerability)
- Business decision (stakeholders reject deployed changes)

**Audit Verification Criteria**:
- ✅ Rollback plan documented for all production deployments
- ✅ Rollback tested in staging
- ✅ Rollback time estimated and acceptable
- ✅ Rollback decision authority defined (who can call for rollback)

### 2.4.6.2 Rollback Execution

[Organization] **SHALL** execute rollback efficiently when needed:

**Rollback Methods**:
- **Code Rollback**: Deploy previous artifact version (fastest)
- **Configuration Rollback**: Revert configuration to previous version
- **Database Rollback**: Restore database backup (slowest, most risky)
- **Feature Flag Disable**: Turn off new feature without redeploying (fastest for feature-based changes)

**Rollback Process**:
1. **Decision**: Incident Commander or Operations Manager authorizes rollback
2. **Communication**: Stakeholders notified (rollback in progress)
3. **Execution**: Automated rollback (if available) or manual rollback
4. **Validation**: Smoke tests confirm system operational after rollback
5. **Post-Mortem**: Incident review (why was rollback necessary, how to prevent)

**Rollback Time Objectives**:
- Code rollback: <30 minutes (deploy previous version)
- Configuration rollback: <15 minutes (revert config file)
- Database rollback: <2 hours (restore from backup)
- Feature flag disable: <5 minutes (toggle flag)

**Audit Verification Criteria**:
- ✅ Rollback execution documented (when, who, why)
- ✅ Rollback time met objectives
- ✅ Post-rollback system validated
- ✅ Post-mortem completed within 48 hours

---

## 2.4.7 Change Management Integration

### 2.4.7.1 Promotion as Change Control

[Organization] **SHALL** integrate environment promotion with formal change management:

**Change Management Alignment**:
- Each promotion to staging/production is a **change request**
- Change requests follow standard change management process
- Change Advisory Board (CAB) reviews production promotions
- Emergency changes follow expedited process (but still documented)

**Change Request Content** (for production deployment):
- Change description (what is being deployed)
- Change justification (why is this needed)
- Risk assessment (what could go wrong)
- Rollback plan (how to revert if issues)
- Testing evidence (QA sign-off, UAT approval)
- Deployment window (when will deployment occur)
- Impact assessment (which systems/users affected)

**CAB Approval for Production**:
- CAB meets regularly (weekly or biweekly)
- CAB reviews all production deployment requests
- CAB can approve, defer, or reject changes
- Approved changes scheduled in deployment calendar
- Emergency changes approved via emergency CAB process

**Audit Verification Criteria**:
- ✅ All production deployments have change request (100%)
- ✅ CAB approval documented for production changes
- ✅ Change requests include rollback plans
- ✅ Emergency changes follow expedited approval (but still documented)

---

## 2.4.8 Deployment Windows and Scheduling

### 2.4.8.1 Production Deployment Windows

[Organization] **SHALL** schedule production deployments within approved windows:

**Deployment Window Requirements**:
- Production deployments during **change windows** (predefined low-traffic periods)
- Change windows communicated in advance (stakeholders aware)
- High-availability systems: Rolling deployments (no downtime)
- Maintenance windows: Scheduled downtime (for major changes)

**Typical Change Windows**:
- **Standard changes**: Tuesday-Thursday, 6pm-10pm (low user traffic)
- **Emergency changes**: Anytime (with CISO approval)
- **Major changes**: Weekend maintenance window (Saturday 12am-6am)
- **No-change periods**: Freeze before holidays, end-of-quarter, etc.

**Deployment Blackout Periods**:
- Holiday seasons (no changes during peak shopping/usage)
- Critical business periods (month-end/quarter-end financial processing)
- Major events (company conferences, product launches)

**Audit Verification Criteria**:
- ✅ Deployment windows defined and communicated
- ✅ Production deployments within approved windows (>95%)
- ✅ Out-of-window deployments approved as exceptions
- ✅ Blackout periods enforced (zero deployments during blackout)

---

## 2.4.9 Database and Data Migration Promotion

### 2.4.9.1 Database Schema Changes

[Organization] **SHALL** promote database changes following same path as code:

**Database Change Promotion**:
- Database changes (schema, stored procedures) follow Dev → Test → Staging → Prod path
- Database changes version controlled (migration scripts in source control)
- Database changes tested in each environment before production
- Database rollback scripts prepared and tested

**Database Migration Tools**:
- Database migration frameworks (Flyway, Liquibase, Django migrations, Rails migrations)
- Migration scripts versioned (numbered sequentially)
- Migrations applied automatically during deployment
- Migration failures prevent deployment (rollback triggered)

**Backward Compatibility**:
- Database changes should be backward compatible (old code can run with new schema)
- Breaking schema changes require coordinated code + database deployment
- Blue-green deployment for zero-downtime schema changes

**Audit Verification Criteria**:
- ✅ Database changes version controlled
- ✅ Database migrations tested in test/staging before production
- ✅ Rollback scripts tested and available
- ✅ Database changes follow promotion path (like code)

---

## 2.4.10 Infrastructure and Platform Promotion

### 2.4.10.1 Infrastructure as Code Promotion

[Organization] **SHALL** promote infrastructure changes following same rigor as application code:

**IaC Promotion Requirements**:
- Infrastructure defined as code (Terraform, CloudFormation, Ansible, etc.)
- Infrastructure code version controlled
- Infrastructure changes tested in dev/test/staging before production
- Infrastructure changes peer-reviewed (like code review)

**IaC Deployment**:
- Terraform workspaces or separate state files per environment
- Infrastructure changes applied via CI/CD pipeline (not manual)
- Infrastructure drift detection (alert if actual infrastructure differs from IaC)
- Infrastructure validation post-deployment (ensure resources created correctly)

**Audit Verification Criteria**:
- ✅ Infrastructure defined as code (IaC coverage >90%)
- ✅ Infrastructure changes version controlled
- ✅ Infrastructure promotion follows dev → test → staging → prod
- ✅ Drift detection alerts reviewed monthly

---

## 2.4.11 Audit Trail and Deployment Logging

### 2.4.11.1 Deployment Audit Requirements

[Organization] **SHALL** maintain comprehensive audit trail of all promotions:

**Deployment Logging Requirements**:
- WHO deployed (user identity, service account)
- WHAT was deployed (artifact version, configuration changes)
- WHERE was it deployed (environment, systems affected)
- WHEN was it deployed (timestamp, timezone)
- WHY was it deployed (change request number, business justification)
- HOW was it deployed (automated pipeline, manual execution, emergency process)
- OUTCOME (success/failure, rollback triggered, post-deployment validation)

**Deployment Log Retention**:
- Production deployments: 3 years (regulatory requirement)
- Staging deployments: 1 year
- Development/testing deployments: 6 months

**Deployment Log Access**:
- Operations team: Full access
- Security team: Read-only access for audit
- Auditors: Read-only access on request
- Developers: Limited access (their own deployments only)

**Audit Verification Criteria**:
- ✅ All deployments logged (100% coverage)
- ✅ Logs include WHO, WHAT, WHERE, WHEN, WHY, HOW, OUTCOME
- ✅ Logs retained per retention policy
- ✅ Log access controls enforced

---

## 2.4.12 Emergency Production Hot-Fix Process

### 2.4.12.1 Hot-Fix Exception Process

[Organization] **MAY** bypass normal promotion path for critical production hot-fixes:

**Hot-Fix Criteria** (when allowed):
- Severity 1 incident (production down or critical functionality broken)
- Security vulnerability requiring immediate patching
- Data corruption risk requiring immediate fix
- Business-critical functionality broken (financial loss, regulatory violation)

**Hot-Fix Approval**:
- CISO approval required (or delegate if CISO unavailable)
- Incident Commander approval
- Risk acceptance documented (bypassing normal testing)
- Post-deployment testing plan (how will fix be validated)

**Hot-Fix Process**:
1. **Incident Declared**: Severity 1 incident requires hot-fix
2. **Hot-Fix Development**: Developer creates fix in isolated branch
3. **Minimal Testing**: Targeted testing of fix (time-boxed)
4. **Approval**: CISO + Incident Commander approve
5. **Production Deployment**: Hot-fix deployed to production (bypassing staging)
6. **Post-Deployment Validation**: Immediate testing in production
7. **Retrospective Promotion**: Fix promoted to dev/test/staging after production (to align environments)

**Hot-Fix Documentation**:
- Hot-fix justification (why normal process bypassed)
- Risk assessment (what could go wrong)
- Approval signatures (CISO, Incident Commander)
- Post-deployment validation results
- Retrospective promotion completion

**Audit Verification Criteria**:
- ✅ Hot-fixes documented and approved (100%)
- ✅ Hot-fix criteria met (Severity 1 incident)
- ✅ Post-deployment validation completed
- ✅ Retrospective promotion completed within 48 hours

---

## 2.4.13 Measurable Compliance Criteria

For audit and compliance verification, [Organization] must demonstrate:

**Promotion Compliance Metrics**:
- **0** direct deployments to production (bypassing staging) except approved hot-fixes
- **100%** of production deployments have CAB approval
- **100%** of promotions follow defined path (dev → test → staging → prod)
- **>95%** of deployments successful (smoke tests pass)
- **<5%** rollback rate (indicates quality promotion process)
- **100%** of production deployments have rollback plan
- **<10** hot-fixes per year (trending down - indicates improving quality)
- **100%** deployment audit logs complete and retained

**Verification Methods**:
- Monthly deployment audit (verify approvals and promotion path)
- Quarterly rollback analysis (why rollbacks occurred, trends)
- Semi-annual change management audit (CAB effectiveness)
- Annual promotion process review (efficiency and effectiveness)
- Continuous pipeline monitoring (deployment success rates)

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | [Name] | ________________ | [Date] |
| IT Operations Manager | [Name] | ________________ | [Date] |
| DevOps Lead | [Name] | ________________ | [Date] |
| CAB Chair | [Name] | ________________ | [Date] |
| Information Security Manager | [Name] | ________________ | [Date] |

---

*End of Document ISMS-POL-A.8.31-S2.4*
