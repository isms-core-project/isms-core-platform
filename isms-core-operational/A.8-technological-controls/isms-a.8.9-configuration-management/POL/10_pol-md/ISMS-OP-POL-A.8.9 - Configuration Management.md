**ISMS-OP-POL-A.8.9 — Configuration Management**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Configuration Management |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.9 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.8.9 — Configuration management
- ISO/IEC 27002:2022 Section 8.9 — Implementation guidance for configuration management
- NIST SP 800-128 — Guide for Security-Focused Configuration Management of Information Systems
- NIST SP 800-53 Rev 5 — CM-2 (Baseline Configuration), CM-3 (Configuration Change Control), CM-6 (Configuration Settings), CM-7 (Least Functionality)
- CIS Controls v8 — Control 4 (Secure Configuration of Enterprise Assets and Software)
- CIS Benchmarks — Platform-specific hardening guides

**Related Annex A Controls**:

| Control | Relationship to Configuration Management |
|---------|------------------------------------------|
| A.5.9 Inventory of information and other associated assets | Asset inventory provides the scope for configuration management; every configuration item traces to an inventoried asset |
| A.5.23 Information security for use of cloud services | Cloud service configurations managed under this policy; shared responsibility model defines configuration boundaries |
| A.5.24–28 Incident management | Configuration drift or unauthorised changes may trigger incident response; failed changes escalated as incidents |
| A.8.1–7–18–19 Endpoint security | Endpoint configuration baselines and hardening standards defined and enforced under this policy |
| A.8.8 Management of technical vulnerabilities | Vulnerability remediation may require configuration changes; hardening reduces vulnerability surface |
| A.8.15 Logging | Configuration change events logged for audit trail and drift detection |
| A.8.16 Monitoring activities | Monitoring tools detect configuration drift and unauthorised changes |
| A.8.20–22 Network security | Network device configurations (firewalls, switches, routers) managed as configuration items |
| A.8.32 Change management | Configuration changes follow the change management approval process; complementary disciplines |

**Related Internal Policies**:

- Asset Management Policy
- Change Management Policy
- Endpoint Security Policy
- Network Security Policy
- Logging Policy
- Monitoring Activities Policy (A.8.16)
- Vulnerability Management Policy
- Incident Management Policy

---

# Configuration Management Policy

## Purpose

The purpose of this policy is to ensure that configurations, including security configurations, of hardware, software, services, and networks are established, documented, implemented, monitored, and reviewed in a manner that reduces the risk of security incidents caused by misconfiguration, unauthorised changes, or configuration drift.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect personal data processed by systems under configuration management. Secure configuration of systems processing personal data is a fundamental technical measure demonstrating compliance with data protection obligations. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32 requirements also apply.

## Scope

All employees, contractors, and third-party users with responsibility for configuring, maintaining, or administering information systems.

All information systems, infrastructure, and services requiring configuration management, including:

- **Compute and infrastructure**: Servers (physical and virtual), containers, workstations, mobile devices.
- **Network devices**: Firewalls, routers, switches, load balancers, wireless access points, VPN gateways.
- **Cloud services**: IaaS, PaaS, and SaaS configurations within the organisation's control.
- **Operating systems**: Server and endpoint operating system configurations.
- **Applications and middleware**: Application servers, databases, web servers, message queues.
- **Security systems**: SIEM, endpoint protection, intrusion detection/prevention, identity providers.
- **IoT and OT systems**: Connected devices and operational technology under the organisation's management.

Across all environments: production, non-production (development, test, QA, staging), disaster recovery, and sandbox.

**Out of scope**: BYOD devices not managed by the organisation; SaaS platforms where the organisation has no configuration control (provider-managed only); temporary systems with a lifecycle of less than 24 hours (unless processing personal or sensitive data); systems explicitly excluded via documented risk assessment with CISO approval.

## Principle

All information systems shall be configured according to documented, approved security baselines before deployment to production. Default manufacturer configurations ("out of the box") are not acceptable for production use.

Configurations shall be:

- **Established**: Secure baselines defined for each asset type using recognised hardening standards.
- **Documented**: Baseline parameters recorded, version-controlled, and accessible to authorised personnel.
- **Implemented**: Systems deployed from approved baselines or golden images.
- **Monitored**: Actual configurations compared against approved baselines to detect drift.
- **Reviewed**: Baselines reviewed and updated at defined intervals and following significant changes.

The organisation shall apply the principle of least functionality: systems shall be configured to provide only the capabilities required for their intended purpose, with unnecessary services, ports, protocols, and accounts disabled or removed.

**Least functionality implementation** (specific requirements):

**Services (processes/daemons)**:
- Approach: Whitelist only required services for the system role.
- Example — Ubuntu Application Server baseline: Required services: sshd (remote management), systemd-resolved (DNS), chrony (time sync), application service (e.g., nginx, app process). Disabled/removed: cups (printing), avahi-daemon (mDNS), bluetooth, X11 (graphical services).
- Validation: `systemctl list-units --state=running` compared against baseline whitelist; unauthorised services flagged.

**Network ports**:
- Approach: Whitelist only required listening ports.
- Example — Windows Server 2022 Domain Controller: Required ports: 53 (DNS), 88 (Kerberos), 135 (RPC), 389/636 (LDAP/LDAPS), 445 (SMB), 3389 (RDP — restricted to admin subnet). Blocked: All other ports via host firewall.
- Validation: `netstat -an` or `ss -tuln` compared against baseline; unexpected listeners flagged.

**Protocols**:
- Disable legacy/insecure protocols: SMBv1 (disabled), TLS below 1.2 (disabled), SSHv1 (disabled), Telnet (removed), FTP (replaced with SFTP/FTPS).
- Enable secure alternatives only: SSH (v2 minimum), TLS 1.2/1.3 only, HTTPS mandatory.

**Default accounts**:
- Remove or disable: Guest accounts, vendor default accounts (Administrator renamed, default passwords changed), unused service accounts.
- Baseline requirement: Document all accounts in baseline with justification (why the account exists, what it is used for).

**Unnecessary features/roles**:
- Windows: Remove unused server roles (e.g., remove Print Services if not a print server, remove IIS if not a web server).
- Linux: Remove unused packages (`apt autoremove`, `yum remove`).
- Cloud: Disable unused cloud services (e.g., disable AWS EC2 serial console if not needed, disable Azure Bastion if not used).

Documentation: Each baseline shall include a "Required Services and Ports" table listing whitelisted items with justification.

---

## Configuration Baselines

### Baseline Definition

The organisation shall define and maintain secure configuration baselines at the **asset-type level** (e.g., "Windows Server 2022 — Domain Controller", "Ubuntu 24.04 — Application Server", "Cisco IOS-XE — Core Switch"), not at the individual asset level.

Baselines shall be defined for all asset types in active production use.

**Baseline coverage requirements**:

Coverage shall be measured by:

- **Asset type coverage**: Percentage of distinct asset types (OS + role combinations) with documented baselines.
- **Instance coverage**: Percentage of total production asset instances covered by baselines.

**Coverage targets**:

| Asset Tier | Asset Type Coverage | Instance Coverage | Timeline |
|------------|-------------------|------------------|----------|
| **Tier 1 (Critical)** | 100% | 100% | Immediate (no exceptions) |
| **Tier 2 (High)** | 100% | 95% | Within 6 months of production deployment |
| **Tier 3 (Medium)** | 90% | 90% | Within 12 months of production deployment |
| **Tier 4 (Low)** | 80% | 80% | Best effort |

**Gap handling**:

- **Tier 1/2 assets without baselines**: Deployment to production shall be blocked until a baseline is created (enforced via change approval).
- **Tier 3/4 gaps**: Document in baseline gap register with remediation plan (target: baseline created within 90 days of production deployment).
- **Exception**: Legacy systems nearing decommission (less than 12 months remaining life) may waive the baseline requirement with CISO risk acceptance and enhanced monitoring.

Each baseline shall document:

- **Baseline identifier** (e.g., BASE-WIN2022-DC-v1.2) and version.
- **Asset type** and applicable environments.
- **Operating system settings**: Security settings, enabled/disabled services, kernel parameters, registry settings.
- **Application configurations**: Default settings, security parameters, integration points.
- **Network settings**: IP configuration, firewall rules, access control lists, routing.
- **Security configurations**: Authentication settings, encryption parameters, logging and audit settings, password policies.
- **Hardening standard applied**: CIS Benchmark level, vendor guide, or custom standard with rationale.
- **Exceptions and deviations**: Any departure from the hardening standard, with documented justification and risk acceptance.
- **Validation criteria**: How to verify that a system conforms to the baseline.

### Baseline Approval

New baselines and baseline updates shall follow a defined approval workflow:

| Action | Approval Authority | Timeline |
|--------|--------------------|----------|
| **New baseline** | Technical Lead (validates accuracy) + CISO or delegate (validates security) | 14 business days |
| **Baseline update** | Technical Lead + CISO or delegate | 7 business days |
| **Emergency baseline change** | CISO (expedited) | 24 hours; retrospective review within 5 business days |

### Baseline Review

Baselines shall be reviewed and updated:

- **Annually** (minimum) for all baselines.
- **Quarterly** for Tier 1 (critical) system baselines.
- **Ad hoc** when triggered by: new vulnerability disclosures affecting baseline settings, technology upgrades or version changes, regulatory or compliance requirement changes, lessons learned from security incidents.

### Baseline Deprecation

When an asset type is decommissioned or replaced:

- The baseline shall be marked "DEPRECATED" with an effective date.
- The baseline shall be retained in the repository for 3 years for historical reference.
- The baseline shall be removed from active compliance monitoring.
- A replacement baseline (if applicable) shall be linked in the repository.

---

## Standard Builds and Golden Images

The organisation should adopt standard builds and golden images to ensure consistent, repeatable deployment of securely configured systems.

### Golden Image Requirements

Golden images shall:

- Implement the approved baseline for the relevant asset type.
- Contain only approved and licensed software.
- Include current security patches at time of image creation.
- Be tested in a non-production environment before approval for production use.
- Be versioned and tracked in a configuration repository.
**Golden image refresh policy** (risk-based):

**Scheduled refresh** (baseline):
- **Tier 1/2 images**: Monthly refresh.
- **Tier 3/4 images**: Quarterly refresh.

**Triggered refresh** (immediate, overrides schedule):
- **Critical vulnerability patch**: Within 7 days of patch release (for vulnerabilities affecting baseline software with CVSS >= 9.0 or active exploitation).
- **Baseline update**: Within 14 days of approved baseline change.
- **Security incident**: Immediately if golden image may be compromised or contains vulnerable configuration.

**Refresh procedure**:
1. Update base image with latest patches.
2. Apply current baseline configuration.
3. Test in non-production: Deploy test instance, run validation suite (functional tests, security scan).
4. Security Team validation: Scan for misconfigurations, verify hardening compliance.
5. Approval: IT Operations Manager + Security Team sign-off.
6. Publish: Replace old image in repository, mark old image "DEPRECATED".
7. Notify: Inform system administrators of new image version.

**Old image retention**:
- Previous version: Retained 90 days (rollback capability if new image has issues).
- Older versions: Archived for 1 year (historical reference).

**Deployment enforcement**:
- Deployments using images older than 60 days: Flagged for review (why not using current image?).
- Deployments using images older than 90 days: Rejected (must use current image or document exception).

**Image age tracking**: [Asset Management System] shall record image creation date per deployed instance; report monthly on "stale deployments" (instances from images older than 30 days).

Golden image creation shall be restricted to authorised personnel (system administrators or DevOps engineers). New or updated golden images shall be validated by the security team before approval.

### Infrastructure as Code

Where feasible, the organisation should define configuration baselines as code (e.g., Terraform, Ansible, CloudFormation, Kubernetes manifests, Puppet, Chef) and manage them through version control:

- **Version control**: IaC definitions stored in Git or equivalent with full change history.
- **Code review**: Configuration changes submitted via pull request and reviewed before merge.
- **Automated testing**: IaC validated through automated testing (linting, policy-as-code scanning, dry-run) before deployment.
- **Change control integration**: IaC deployments subject to the organisation's change management process.
- **Misconfiguration scanning**: IaC templates scanned for security misconfigurations before deployment (e.g., Checkov, tfsec, or equivalent).

**IaC security scanning requirements**:

**Scanning tools**: [Checkov / tfsec / Terraform Sentinel / Open Policy Agent] configured per organisation standards.

**Mandatory scan rules** (all IaC templates):

| Category | Rule Examples | Enforcement Level |
|----------|---------------|------------------|
| **Encryption** | S3 buckets encrypted at rest, RDS encryption enabled, EBS volumes encrypted, TLS in transit | Blocking (deployment fails if violated) |
| **Access control** | No public S3 buckets (unless explicitly approved), security groups no 0.0.0.0/0 ingress on sensitive ports (22, 3389), IAM policies follow least privilege | Blocking |
| **Logging** | CloudTrail enabled, VPC flow logs enabled, RDS/database logging enabled | Blocking |
| **Secrets management** | No hardcoded credentials in IaC (must use secret manager references), no API keys in plain text | Blocking |
| **Network security** | Default VPC not used, subnets properly segmented (public/private), NACLs configured | Warning (review required, can override with justification) |
| **Least functionality** | Default security group rules removed, unnecessary services disabled in launch configs | Warning |

**Custom rules** (organisation-specific):
- Mandatory tags: All resources tagged with Owner, Environment, CostCenter, DataClassification.
- Approved instance types: Only organisation-approved instance families (no exotic types without approval).
- Approved regions: Deployments only to approved cloud regions (e.g., eu-central-1, westeurope).

**Scan execution**:
- **Pre-commit**: Developers run scans locally before committing IaC changes (recommended, not enforced).
- **CI/CD pipeline**: Automated scan on pull request (required); blocking violations prevent merge.
- **Exception process**: If blocking violation cannot be remediated (legitimate business need), developer documents exception in [Exception Tracker], CISO approves, exception added to IaC as comment + suppression rule.

**Scan result handling**:
- Blocking violations: Deployment halted, remediate before retry.
- Warning violations: Logged, reviewed by Security Team weekly, escalated if pattern emerges.
- Exceptions: Reviewed quarterly, revoked if no longer justified.

**Ruleset maintenance**:
- Security Team maintains IaC scan ruleset in [Git Repository].
- Ruleset reviewed quarterly, updated for new threats and best practices.
- Version-controlled with changelog.

IaC does not replace the need for documented baselines; it is the preferred method for implementing and enforcing them.

---

## Configuration Change Control

All changes to system configurations shall follow the organisation's change management process (see **Change Management Policy — A.8.32**). This section addresses configuration-specific requirements that complement change management.

### Change Classification

Configuration changes shall be classified according to risk and impact:

| Type | Definition | Approval | Examples |
|------|------------|----------|----------|
| **Standard** | Pre-approved, low-risk, repeatable configuration change per documented procedure | Pre-approved (catalogue) | Certificate renewal, DNS record addition, standard firewall rule |
| **Normal** | Requires assessment, testing, and formal approval | Service Owner / CAB | Baseline update, new hardening standard, network topology change |
| **Emergency** | Urgent change to resolve critical incident or vulnerability | CISO or IT Operations Manager (expedited) | Disabling compromised service, emergency firewall rule, critical patch |

### Configuration Change Categorisation

**Requires formal change approval** (Change Management Policy A.8.32):
- Security-relevant configuration changes: Authentication settings, encryption parameters, firewall rules, access controls, logging levels (security events), user/group permissions.
- Baseline changes: Any modification to approved baseline definition.
- Production system changes: Any configuration change to Tier 1/2 production systems (regardless of security relevance).
- Network topology changes: Routing, VLANs, subnetting, firewall policies.
- Multi-system changes: Configuration changes affecting more than 5 systems simultaneously.

**Pre-approved** (standard change catalogue, no CAB):
- Parameter tuning within documented ranges: Log rotation days (7–30 days), cache sizes (within defined limits), timeout values (within safe ranges).
- Certificate renewals: TLS/SSL certificate replacement with same parameters.
- DNS record additions: Adding A/AAAA/CNAME records (not changing authoritative servers).
- User provisioning/deprovisioning: Following documented joiner/mover/leaver procedures.

**Does not require change approval** (operational adjustment):
- Cosmetic changes: UI labels, non-functional descriptions, comment fields.
- Monitoring threshold tuning: Adjusting alert thresholds based on observed baselines (documented in monitoring tool).
- Non-production systems: Configuration changes to Tier 3/4 development/test systems (logged but not formally approved, unless security-relevant).

Guideline: If uncertain whether a change requires approval, default to **yes** (submit change request).

Documentation: Standard change catalogue shall be maintained in [Change Management System] with pre-approved procedures and risk assessments.

### Configuration Documentation Update

Following any approved configuration change, the following shall be updated within **5 business days**:

- Configuration baseline documentation (if the baseline itself changed).
- Configuration management database (CMDB) or equivalent asset records.
- Network diagrams and topology documentation (if network configuration changed).
- Operational procedures and runbooks (if operational steps changed).
- Disaster recovery procedures (if the change affects critical systems or RTO/RPO).

### Unauthorised Configuration Changes

Configuration changes made outside the approved change management process shall be treated as security events:

- Detected through configuration monitoring and drift detection.
- Investigated to determine root cause (malicious, accidental, or process gap).
- Reported to the CISO.
- Subject to corrective action, which may include disciplinary action.
- The affected system shall be remediated to the approved baseline or a new baseline formally approved through the standard process.

---

## Configuration Drift Detection and Monitoring

### Monitoring Requirements

The organisation shall implement configuration monitoring to detect deviations from approved baselines.

**Coverage targets by asset criticality**:

| Asset Tier | Coverage Target | Monitoring Frequency | Acceptable Coverage Gap |
|------------|----------------|----------------------|-------------------------|
| **Tier 1 (Critical)** | 100% | Real-time or hourly | 0% |
| **Tier 2 (High)** | 95% or greater | Daily | Less than 5% |
| **Tier 3 (Medium)** | 85% or greater | Weekly | Less than 15% |
| **Tier 4 (Low)** | 70% or greater | Monthly | Less than 30% |

Monitoring tools shall:

- Compare actual system configuration against the approved baseline.
- Generate alerts when configuration deviations are detected.
- Retain monitoring results for a minimum of 90 days.
- Integrate with [SIEM] for centralised alerting and correlation where practicable.

**Tool selection**: The organisation shall select configuration monitoring tools appropriate to its technical environment. Tools shall support baseline comparison and drift detection. Examples include: file integrity monitoring (FIM) tools, cloud configuration assessment tools (e.g., AWS Config, Azure Policy, GCP Security Command Center), endpoint management platforms, and configuration compliance scanners.

Asset types not yet under automated monitoring shall be documented with a planned deployment date and interim manual controls (e.g., quarterly manual audits). Coverage gaps shall be risk-accepted by the CISO and recorded in the risk register.

### Monitoring Coverage Gap Management

**Gap documentation requirements**:
- Asset type/instance not yet monitored: Logged in Monitoring Gap Register.
- Register fields: Asset ID, Tier, Gap reason (tool limitation, pending budget, technical constraint), Interim control (manual audit, enhanced logging, restricted access), Owner (who will remediate), Planned deployment date, Actual deployment date, Status (Open/In Progress/Closed).

**Gap closure SLAs** (from identification to monitoring deployment):

| Asset Tier | Maximum Gap Duration | Interim Control Requirement | Escalation if SLA Missed |
|------------|---------------------|----------------------------|--------------------------|
| **Tier 1** | 30 days | Enhanced manual audit (weekly config review + monthly full audit) | CISO (immediate); may require production freeze until monitoring deployed |
| **Tier 2** | 90 days | Manual audit (monthly config review) | IT Operations Manager then CISO at 60 days |
| **Tier 3** | 180 days | Manual audit (quarterly) | IT Operations Manager at 120 days |
| **Tier 4** | 365 days | Annual manual audit acceptable | IT Operations Manager at 270 days |

**Gap closure accountability**:
- Gap Owner: Responsible for implementing monitoring solution by planned deployment date.
- Monthly review: IT Operations Manager reviews Monitoring Gap Register, tracks progress, escalates overdue gaps.
- Quarterly reporting: Gap register summary reported to CISO (number of open gaps by tier, average closure time, overdue gaps).

**Interim controls** (while gap persists):
- Manual configuration review: System administrator exports configuration, compares to baseline manually, documents findings.
- Enhanced access logging: Privileged account access to unmonitored systems logged and reviewed weekly.
- Change freeze (Tier 1 only): If monitoring cannot be deployed within SLA, consider freezing non-emergency changes until monitoring available.

**Gap risk acceptance**:
- If gap cannot be closed (e.g., legacy system incompatible with monitoring tools, budget constraints): CISO approves risk acceptance with documented justification, compensating controls, and annual review.
- Risk acceptance does not waive interim controls — manual audits shall continue.

**Success criteria**: Target less than 5% of Tier 1/2 assets in Monitoring Gap Register at any time.

### Drift Classification and Response

When configuration drift is detected, it shall be classified by severity and responded to within defined timelines:

| Severity | Definition | Response SLA | Examples |
|----------|------------|--------------|---------|
| **Critical** | Security control disabled or compromised | Less than 1 hour | Firewall disabled, unauthorised admin account created, encryption turned off, logging disabled on critical system |
| **High** | Security-relevant configuration changed | Less than 4 hours | Password policy weakened, unnecessary service enabled, access control list modified without approval |
| **Medium** | Non-security configuration drift | Less than 24 hours | Service port changed, non-critical application setting modified, documentation mismatch |
| **Low** | Informational deviation | Less than 5 business days | Cosmetic changes, non-functional settings, minor parameter differences |

**Alert routing**:

- **Critical and High**: Security operations team + CISO + System Owner.
- **Medium**: IT Operations Manager + System Owner.
- **Low**: IT Operations (consolidated daily report).

### Drift Remediation

Drift remediation shall follow a structured workflow:

1. **Detection**: Automated monitoring identifies configuration deviation.
2. **Triage**: IT Operations investigates the cause and determines whether the change was authorised, unauthorised, or a false positive.
3. **Action**:
   - **Authorised change** (approved but baseline not yet updated): Update baseline documentation; close the alert.
   - **Unauthorised change**: Remediate system to approved baseline; investigate root cause; report to CISO; close after resolution.
   - **False positive**: Tune monitoring rules; close the alert.
4. **Documentation**: All drift incidents logged, tracked to closure, and retained for audit.

**Drift remediation verification** (mandatory):

Remediation procedure:
1. **Identify drift**: Monitoring tool detects deviation (e.g., firewall rule added, service enabled, parameter changed).
2. **Investigate**: Determine if authorised (approved change not yet documented) or unauthorised.
3. **Remediate**: If unauthorised, restore to baseline:
   - Manual: System administrator reverts configuration parameter to baseline value.
   - Automated: Configuration management tool (Ansible, Puppet, Chef) re-applies baseline.
   - Re-image: For severe drift or compromise, rebuild from golden image.
4. **Verify remediation** (within 24 hours of remediation):
   - Re-scan system with same monitoring tool that detected drift.
   - Confirm drift alert cleared.
   - Document: Remediation ticket updated with verification timestamp, scan results, and sign-off.
5. **Root cause analysis** (for Critical/High drift):
   - Why did drift occur? (Process gap, unauthorised access, automation failure, baseline error.)
   - Preventive action: Update baseline, improve automation, enhance access controls, train personnel.
6. **Close ticket**: Only after verification confirms baseline compliance.

**Failed verification**:
- If re-scan shows drift persists: Escalate to IT Operations Manager, repeat remediation, consider system isolation if security control drift.
- If drift recurs within 30 days: Root cause investigation mandatory, CISO notified.

**Drift remediation metrics** tracked:
- Percentage of drift remediations with completed verification: Target 100%.
- Time from remediation to verification: Target less than 24 hours.
- Recurring drift (same system, same parameter, more than 2 occurrences): Target 0.

Reported monthly to CISO.

**Remediation SLAs**:

| Severity | Remediation SLA | Escalation if SLA Not Met |
|----------|----------------|---------------------------|
| **Critical** | Less than 4 hours | CISO — may isolate system from production |
| **High** | Less than 24 hours | CISO |
| **Medium** | Less than 5 business days | IT Operations Manager |
| **Low** | Less than 30 days | Best effort |

Recurring drift on the same system or asset type shall trigger a root cause analysis. If the root cause is a baseline that is impractical to maintain, the baseline shall be reviewed and updated through the standard approval process rather than repeatedly accepting exceptions.

---

## Security Hardening Standards

### Hardening Standard Selection

The organisation shall select and apply recognised security hardening standards for all production asset types.

**Recognised standards** (in order of preference):

| Standard | Provider | Typical Usage |
|----------|----------|---------------|
| **CIS Benchmarks** | Center for Internet Security | Primary reference for common platforms (Windows, Linux, cloud, network devices, databases) |
| **Vendor Security Guides** | Microsoft, AWS, Azure, GCP, Cisco, etc. | Cloud platforms, vendor-specific products |
| **DISA STIGs** | Defense Information Systems Agency | High-security environments, government-aligned |
| **NIST Baselines** | NIST SP 800-53, SP 800-128 | Framework alignment, supplemental guidance |

Where multiple standards exist for an asset type, the organisation shall select the standard most appropriate to its risk profile and document the selection rationale.

### Hardening Implementation

All production systems shall be hardened before deployment. Hardening shall include, at minimum:

- **Remove or disable unnecessary services, ports, and protocols** (principle of least functionality — NIST CM-7).
- **Remove or disable default accounts** or change all default passwords.
- **Disable unnecessary features** and software components.
- **Configure authentication** in accordance with the organisation's authentication policy.
- **Enable logging and audit trails** for security-relevant events.
- **Apply current security patches** before production placement.
- **Configure encryption** for data at rest and in transit where applicable.
- **Restrict administrative access** to authorised personnel with MFA.

### Hardening Compliance Targets

| Asset Tier | Critical Security Controls | Overall Hardening Compliance | Acceptable Gaps |
|------------|---------------------------|------------------------------|-----------------|
| **Tier 1 (Critical)** | 100% | 95% or greater | 0 critical gaps |
| **Tier 2 (High)** | 95% or greater | 90% or greater | Less than 5 critical gaps |
| **Tier 3 (Medium)** | 90% or greater | 80% or greater | Less than 10 critical gaps |
| **Tier 4 (Low)** | 80% or greater | 70% or greater | Best effort |

**Critical security controls**: Authentication enforcement, encryption settings, logging configuration, access control enforcement, and patch currency.

### Hardening Verification

Hardening compliance shall be verified through periodic scanning:

| Asset Tier | Automated Scan Frequency | Manual Verification (if automation unavailable) |
|------------|--------------------------|------------------------------------------------|
| **Tier 1 (Critical)** | Quarterly | Semi-annually |
| **Tier 2 (High)** | Semi-annually | Annually |
| **Tier 3/4 (Medium/Low)** | Annually | Annually |

Verification tools may include: OpenSCAP, Nessus, Qualys, Tenable, cloud-native compliance tools (e.g., AWS Security Hub, Azure Defender for Cloud), or equivalent platforms.

Scan results and compliance reports shall be retained for a minimum of **3 years** for audit purposes.

### Gap Remediation

Hardening gaps identified through verification shall be remediated according to risk:

| Gap Risk | Remediation Timeline | Exception Approval |
|----------|----------------------|--------------------|
| **Critical** | Less than 30 days | CISO only |
| **High** | Less than 90 days | CISO or IT Operations Manager |
| **Medium** | Less than 180 days | IT Operations Manager |
| **Low** | Best effort | IT Operations Manager |

Gaps that cannot be remediated due to technical constraints or business requirements shall be documented as exceptions with compensating controls (see Exception Management below).

**Hardening exception compensating controls** (specific requirements):

Exception scenario: A hardening recommendation cannot be implemented (e.g., cannot disable legacy protocol, cannot remove default account, cannot patch vulnerable component).

**Compensating control framework** (layered defence):

Example 1 — Cannot disable SMBv1 (legacy application dependency):
- Compensating controls:
  1. Network isolation: System in isolated VLAN, firewall rules block SMB from untrusted networks.
  2. Access restriction: Only specific legacy client IPs whitelisted for SMB access (ACL).
  3. Enhanced monitoring: IDS/IPS signatures for SMBv1 exploit attempts, alerts on unusual SMB traffic.
  4. Patch currency: Ensure all other available patches applied (even if SMBv1 cannot be disabled, patch MS17-010 and similar).
  5. Decommission plan: Document plan to migrate off legacy application within 12 months (exception not indefinite).

Example 2 — Cannot remove default administrator account (application hardcoded dependency):
- Compensating controls:
  1. Rename account: Change account name from "Administrator" to non-obvious name.
  2. Strong password: 20+ character random password stored in [Password Vault].
  3. MFA enforcement: Require MFA for account logon.
  4. Monitoring: Alert on any use of account, log all actions.
  5. Regular password rotation: Every 90 days.

Example 3 — Cannot patch vulnerable component (vendor no longer provides patches, decommission planned):
- Compensating controls:
  1. Network isolation: Air-gapped or dedicated network segment.
  2. Disable remote access: No RDP/SSH from outside isolated network.
  3. Virtual patching: Deploy IPS rule to block known exploit attempts.
  4. Minimise data: Do not store CONFIDENTIAL data on system if possible.
  5. Decommission timeline: Documented plan to replace system within 6 months.

**Compensating control adequacy assessment**:
- Controls shall reduce risk to an acceptable level (CISO determination).
- Layered defence: Minimum 3 compensating controls required for Critical/High gaps.
- Controls shall be verifiable and auditable (not merely "we will be careful").

**Exception documentation** (in Exception Register):
- Hardening recommendation that cannot be met.
- Business/technical reason (why remediation is not possible).
- Risk assessment (what is the risk of not remediating).
- Compensating controls (specific, measurable).
- Approval: CISO signature.
- Review frequency: Quarterly for Critical gaps, semi-annually for High/Medium.
- Expiry: 12 months maximum; shall be re-justified if still needed.

**Exception metrics**:
- Total active exceptions: Trend down over time.
- Exceptions older than 12 months: Target 0 (requires re-approval or remediation).
- Exceptions without adequate compensating controls: 0 (remediate or strengthen controls).

---

## Configuration Audit

### Internal Configuration Audits

The organisation shall conduct periodic configuration audits to verify that:

- Systems conform to approved baselines.
- Configuration documentation is accurate and current.
- Change control processes were followed for configuration changes.
- Monitoring coverage meets defined targets.
- Hardening compliance meets defined thresholds.

**Audit frequency**:

- **Annual**: Full configuration audit across all asset tiers.
- **Quarterly**: Targeted audit of Tier 1 and Tier 2 assets.
- **Ad hoc**: Following significant incidents, major technology changes, or regulatory findings.

### Audit Evidence

Configuration audits shall produce documented evidence including:

- Baseline compliance scan results.
- Configuration change records for the audit period.
- Drift detection reports and remediation records.
- Hardening compliance scores per asset type.
- Exception register review.
- Monitoring coverage assessment.

Audit results shall be reported to the CISO and included in the management review process.

---

## Emergency Configuration Changes

Emergency configuration changes are addressed primarily under the **Change Management Policy (A.8.32)**. Configuration-specific requirements for emergency changes include:

- The system shall be restored to a documented, known-good configuration state as quickly as possible.
- If the emergency change results in a new configuration state (not a return to baseline), the baseline shall be updated through the standard approval process within **5 business days**.
- All emergency configuration changes shall be logged with: the specific configuration parameters changed, the previous values, the new values, the person who made the change, and the business justification.
- Retrospective review by the CISO or delegate shall occur within **48 hours**.

Emergency configuration changes shall not exceed **10%** of all configuration changes in any calendar month. Exceeding this threshold triggers a process review.

---

## Definitions

| Term | Definition |
|------|------------|
| **Baseline configuration** | Documented set of security and operational configuration parameters for an asset type, serving as the reference for deployment, compliance verification, and drift detection |
| **Configuration drift** | Deviation of actual system configuration from the approved baseline, potentially indicating unauthorised changes, process gaps, or documentation errors |
| **Configuration item (CI)** | Any asset, service, or component managed through configuration management, tracked with defined attributes and relationships |
| **CMDB** | Configuration management database — repository storing configuration baselines, asset configurations, change history, and relationships between configuration items |
| **CIS Benchmark** | Consensus-based best practice security configuration guide published by the Center for Internet Security for specific platforms and technologies |
| **Golden image** | Pre-configured system image implementing the approved baseline, used for rapid, consistent deployment of new systems |
| **Hardening** | Process of securing system configurations by implementing recognised security standards and removing unnecessary services, accounts, ports, and features |
| **Infrastructure as Code (IaC)** | Practice of managing configuration baselines and infrastructure provisioning through machine-readable code stored in version control |
| **Least functionality** | Principle of configuring systems to provide only the capabilities required for their intended purpose |
| **Standard build** | Approved, tested, and documented system configuration used as the basis for deploying new instances of a specific asset type |

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; baseline and exception approval authority; drift escalation point; hardening compliance oversight; reporting to Executive Management |
| **IT Operations Manager** | Day-to-day configuration management operations; baseline repository maintenance; monitoring coordination; metrics reporting to CISO |
| **Security Team** | Hardening standard selection and review; baseline security validation; drift alert investigation; compliance scanning; audit support |
| **System Owners** | Accountability for configuration compliance of owned systems; change approval for owned systems; timely drift remediation; resource allocation for hardening |
| **System Administrators / DevOps Engineers** | Baseline implementation; golden image creation and maintenance; configuration monitoring setup; approved change execution; drift triage and remediation |
| **Change Manager / CAB** | Configuration change approval (normal and emergency); post-implementation review; change success tracking |
| **Internal / External Auditors** | Independent verification of configuration compliance; evidence review; findings reporting |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency | Retention |
|---|----------|-------|-----------|-----------|
| 1 | **Configuration baseline repository** with version history, approval records, and review dates per asset type | IT Operations Manager | Maintained continuously; reviewed annually (quarterly for Tier 1) | Life of asset type + 3 years |
| 2 | **Golden image inventory** with version, creation date, patch level, and validation records | System Administrators / DevOps | Maintained continuously; refreshed monthly (Tier 1/2) or quarterly (Tier 3/4) | Life of image + 1 year |
| 3 | **CMDB or configuration inventory** showing configuration items, baselines applied, and current compliance status | IT Operations Manager | Maintained continuously; audited quarterly | Active + 3 years |
| 4 | **Configuration change records** (change requests, approvals, implementation logs, post-change verification) | Change Manager | Per change; audited quarterly | 3 years (7 years for audit evidence) |
| 5 | **Drift detection reports** and alert logs with triage outcomes, remediation records, and post-remediation verification results | Security Team / IT Operations | Continuous; reviewed monthly | 3 years |
| 6 | **Hardening compliance scan results** per asset type showing compliance percentage and identified gaps | Security Team | Per scan schedule (quarterly to annually by tier) | 3 years |
| 7 | **Gap remediation register** with gap description, risk rating, owner, due date, status, and closure evidence | IT Operations Manager | Maintained continuously; reviewed monthly | Gap duration + 3 years |
| 8 | **Exception register** for configuration deviations (request, justification, compensating controls, approval, expiry date) | CISO | Maintained continuously; reviewed quarterly | Exception duration + 3 years |
| 9 | **Configuration audit reports** (internal and external) with findings and corrective actions | CISO / Auditors | Annual (full) + quarterly (targeted) | 3 years |
| 10 | **Emergency configuration change records** with justification, approval, retrospective review, and baseline update confirmation | CISO | Per event; retrospective within 48 hours | 3 years |
| 11 | **IaC repository access and change logs** (commit history, pull request reviews, deployment records) | DevOps / IT Operations | Continuous | 3 years |
| 12 | **Monitoring coverage report** showing percentage of assets under automated configuration monitoring by tier, including Monitoring Gap Register status | IT Operations Manager | Monthly | 1 year |
| 13 | **SOC 2 configuration compliance evidence** — Quarterly reports showing Tier 1/2 systems meet hardening baselines, with sample configuration exports and scan results | Security Team | Quarterly before SOC 2 audit | 3 years |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, baseline coverage assessments, configuration monitoring reports, hardening compliance scans, drift detection and remediation records, change documentation audits, internal and external audits, and feedback to the policy owner.

**Compliance Metrics**:

| Metric | Target | Measurement Frequency |
|--------|--------|-----------------------|
| Tier 1 asset types with documented, approved baselines | 100% | Quarterly |
| Tier 2 asset types with documented, approved baselines | 100% | Quarterly |
| Tier 3/4 asset types with documented, approved baselines | >= 80% | Quarterly |
| Tier 1 and Tier 2 assets under automated configuration monitoring | >= 95% | Monthly |
| Drift alerts remediated within SLA | >= 90% | Monthly |
| Drift remediations with completed post-remediation verification | 100% | Monthly |
| Hardening compliance for critical security controls (Tier 1) | >= 95% | Quarterly |
| Emergency configuration changes as percentage of all changes | < 10% | Monthly |
| Configuration audit findings closed within agreed timelines | >= 90% | Quarterly |
| Golden images refreshed within schedule (monthly for Tier 1/2, quarterly for Tier 3/4) | 100% | Monthly |
| Monitoring gap closure within SLA by tier | >= 90% | Quarterly |
| Hardening exceptions older than 12 months | 0 | Quarterly |

**Non-Compliance Handling**: Metrics below 70% require immediate CISO escalation and a remediation plan with defined timelines. Metrics between 70% and 89% require IT Operations Manager oversight with monthly progress reviews. Metrics at 90% and above follow standard quarterly monitoring.

## Exceptions

Any exception to this policy shall be approved and recorded by the CISO in advance, with documented risk acceptance, compensating controls, and a defined expiry date (maximum 12 months). Exceptions shall be reviewed quarterly and reported to the Management Review Team. Expired exceptions shall trigger remediation or formal renewal through the standard approval process.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Making unauthorised configuration changes to production systems, disabling security controls, bypassing change management, or concealing configuration drift are considered severe violations.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to industry hardening standards (new CIS Benchmark versions, vendor security guide updates), emerging threats and attack techniques targeting misconfigurations, technology changes (new platforms, cloud service adoption, containerisation), regulatory changes, audit findings, and lessons learned from configuration-related incidents.

---

# Areas of the ISO 27001 Standard Addressed

Configuration Management Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 5.37 Documented operating procedures |
| Clause 8.1 Operational planning and control | 6.3 Information security awareness, education, and training |
| | **8.9 Configuration management** |
| | 8.8 Management of technical vulnerabilities |
| | 8.32 Change management |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures for data security; secure configuration as a fundamental technical measure protecting systems that process personal data |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security; configuration management supports access control, logging, and system integrity requirements |
| EU GDPR (where applicable) | Art. 32 — Security of processing; secure configuration management as an appropriate technical and organisational measure |
| ISO/IEC 27001:2022 | Annex A Control 8.9 — Configuration management |
| ISO/IEC 27002:2022 | Section 8.9 — Implementation guidance for configuration management (new control in 2022 edition) |
| NIST SP 800-128 | Guide for Security-Focused Configuration Management of Information Systems |
| NIST SP 800-53 Rev 5 | CM-2 (Baseline Configuration), CM-3 (Configuration Change Control), CM-6 (Configuration Settings), CM-7 (Least Functionality), CM-8 (System Component Inventory) |
| CIS Controls v8 | Control 4: Secure Configuration of Enterprise Assets and Software (Safeguards 4.1–4.12) |
| CIS Benchmarks | Platform-specific hardening guides (Windows, Linux, macOS, cloud platforms, network devices, databases) |

---

<!-- QA_VERIFIED: 2026-02-08 -->
