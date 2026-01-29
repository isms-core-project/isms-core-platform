# ISMS-POL-A.8.9-S2.4
## Configuration Management - Security Hardening Requirements

**Document ID**: ISMS-POL-A.8.9-S2.4  
**Title**: Security Hardening Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect / Configuration Manager | Initial security hardening requirements |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Date + 1 year]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Security Architect / Chief Technology Officer
- Operations Review: System Administrators Lead / Infrastructure Manager

**Distribution**: Security team, system administrators, DevOps engineers, cloud architects, application owners  
**Related Documents**: ISMS-POL-A.8.9-S1 (Definitions), ISMS-POL-A.8.9-S2.1 (Baseline Requirements), ISMS-POL-A.8.9-S2.3 (Monitoring), ISMS-POL-A.8.9-S5.A (Configuration Standards), ISMS-IMP-A.8.9.4 (Hardening Assessment)

---

## 2.4.1 Purpose

This document defines **mandatory and recommended requirements** for implementing security hardening across IT infrastructure. Security hardening is the process of reducing attack surface by:
- **Disabling unnecessary services** - Remove functionality not required for business operations
- **Closing unused ports** - Reduce network exposure
- **Enforcing strong authentication** - Prevent unauthorized access
- **Applying security patches** - Remediate known vulnerabilities
- **Configuring security controls** - Enable logging, encryption, access controls
- **Removing default configurations** - Eliminate vendor-supplied weaknesses

**The Anti-Pattern**: Organizations that deploy systems with vendor default settings ("works out of the box!"), never harden them, and wonder why they get compromised. Default configurations optimize for ease-of-deployment, not security.

**The Feynman Standard**: *"If your server's attack surface hasn't shrunk since installation, you haven't hardened it—you've just installed it. Hardening is surgery: remove what's not needed, strengthen what remains."*

---

## 2.4.2 Hardening Standard Frameworks

### 2.4.2.1 Framework Selection

**MUST Requirements**:
- [Organization] MUST adopt at least one recognized security hardening framework as the foundation for configuration standards
- The selected framework(s) MUST be documented and communicated to technical teams
- Framework selection MUST consider:
  - **Asset types in environment** - Does the framework cover our technology stack?
  - **Regulatory requirements** - Which frameworks satisfy our compliance obligations?
  - **Operational feasibility** - Can we implement and maintain this framework?
  - **Industry alignment** - What do our peers use?

**Primary Hardening Frameworks**:

**CIS Benchmarks** (Center for Internet Security)
- **Coverage**: 100+ benchmarks across 25+ vendor families (Windows, Linux, cloud platforms, databases, network devices, applications)
- **Levels**: 
  - Level 1 - Basic hardening, minimal operational impact
  - Level 2 - Defense-in-depth hardening, may affect functionality
- **Format**: PDF documentation, XCCDF (with CIS-CAT Pro scanning tool)
- **Best For**: Commercial organizations, international deployments, broad technology coverage
- **Cost**: Free (PDFs), paid (CIS-CAT Pro scanning tool, CIS SecureSuite membership)

**DISA STIGs** (Defense Information Systems Agency Security Technical Implementation Guides)
- **Coverage**: Operating systems, applications, network devices, databases, web servers
- **Stringency**: High - designed for defense and government environments
- **Format**: XCCDF (machine-readable), PDF documentation
- **Best For**: US Government, Department of Defense, defense contractors, CMMC compliance
- **Mandatory For**: Systems on DoDIN (DoD Information Networks)
- **Cost**: Free

**DISA SRGs** (Security Requirements Guides)
- **Purpose**: Generic guidance when no specific STIG exists
- **Coverage**: Cloud platforms, custom applications, emerging technologies
- **Use Case**: Organizations can create STIG-aligned configurations for non-STIGged systems

**NIST Publications**
- **NIST SP 800-53 Rev. 5** - Security and Privacy Controls (CM family for Configuration Management)
- **NIST SP 800-123** - Guide to General Server Security
- **NIST SP 800-128** - Security-Focused Configuration Management
- **NIST Cybersecurity Framework (CSF)** - PR.IP-1 (baseline configurations)
- **Best For**: Federal agencies, contractors, organizations seeking NIST alignment

**Vendor-Specific Security Guides**
- **Microsoft Security Baselines** - Windows, Windows Server, Office, Azure, Microsoft 365
- **AWS Security Best Practices** - CIS AWS Foundations Benchmark, AWS Well-Architected Framework
- **Azure Security Benchmark (ASB)** - Microsoft's cloud security baseline
- **Google Cloud Security Foundations** - GCP hardening guidance
- **VMware Hardening Guides** - vSphere, ESXi, NSX, Horizon
- **Cisco IOS Security Configuration Guide** - Routers, switches, firewalls
- **Red Hat Security Guide (RHSG)** - RHEL, OpenShift, Ansible security

**Industry/Regulatory Frameworks** (include configuration requirements):
- **PCI DSS** (Payment Card Industry) - Requirement 2: Default passwords and security parameters
- **HIPAA Security Rule** - Technical safeguards including access controls and encryption
- **CMMC** (Cybersecurity Maturity Model Certification) - Configuration management requirements for defense contractors
- **SWIFT Customer Security Controls (CSC)** - Financial messaging security
- **NERC-CIP** (North American Electric Reliability Corporation - Critical Infrastructure Protection)
- **Essential Eight** (Australian Cyber Security Centre) - Application hardening, OS hardening
- **Cloud Security Alliance (CSA) Cloud Controls Matrix (CCM)**

**SHOULD Requirements**:
- [Organization] SHOULD adopt CIS Benchmarks as the primary framework unless regulatory requirements mandate otherwise (e.g., DISA STIGs for DoD)
- Framework selection SHOULD be reviewed annually to ensure continued relevance
- [Organization] SHOULD map multiple frameworks where necessary (e.g., CIS Benchmarks + PCI DSS)

**MAY Requirements**:
- [Organization] MAY develop custom hardening standards for proprietary or niche systems
- Custom standards MAY supplement recognized frameworks but SHOULD NOT replace them entirely

---

### 2.4.2.2 Framework Implementation Approach

**MUST Requirements**:
- [Organization] MUST define which framework level or profile to implement:
  - **CIS Benchmarks**: Level 1 (baseline) vs. Level 2 (defense-in-depth)
  - **DISA STIGs**: CAT I (high severity) vs. CAT I+II vs. full compliance
  - **Custom frameworks**: Priority tiers based on risk
- The implementation approach MUST balance security and operational requirements
- Deviations from selected framework MUST be documented and risk-accepted

**SHOULD Requirements**:
- [Organization] SHOULD implement:
  - **CIS Level 1** for all systems as minimum baseline
  - **CIS Level 2** or **DISA STIGs** for Critical and High criticality assets
- Implementation approach SHOULD be phased:
  - Phase 1: Critical controls (authentication, access control, logging)
  - Phase 2: High-priority controls (encryption, patching, hardening)
  - Phase 3: Defense-in-depth controls (advanced configurations)

**The Pragmatic Reality**: 
*CIS Level 1 provides 80% of security benefit with 20% of operational friction. CIS Level 2 provides the remaining 20% of benefit with 80% of the friction. Start with Level 1 everywhere, then add Level 2 to critical assets.*

---

## 2.4.3 Operating System Hardening

### 2.4.3.1 Windows Server Hardening

**MUST Requirements**:
- All Windows Server systems MUST be hardened according to at least one of the following:
  - **CIS Microsoft Windows Server Benchmark** (Level 1 minimum, Level 2 for Critical assets)
  - **DISA Windows Server STIG** (if DoD or defense contractor)
  - **Microsoft Security Baselines** (minimum acceptable standard)
- Hardening MUST include:
  - **Account Policies**: Password complexity, lockout thresholds, Kerberos settings
  - **Local Policies**: Audit policies, user rights assignments, security options
  - **Windows Firewall**: Enabled with restrictive rules
  - **User Account Control (UAC)**: Enabled and properly configured
  - **Service Hardening**: Unnecessary services disabled
  - **SMB Protocol**: SMBv1 disabled, SMBv2/v3 configured securely
  - **NTLM Authentication**: Restricted or disabled where possible (prefer Kerberos)
  - **PowerShell**: Constrained Language Mode for unprivileged users, logging enabled
  - **Remote Desktop (RDP)**: Secured with Network Level Authentication (NLA), restricted access

**SHOULD Requirements**:
- Windows Server hardening SHOULD include:
  - BitLocker encryption for system and data volumes
  - AppLocker or Windows Defender Application Control (WDAC) for application whitelisting
  - Credential Guard and Device Guard on supported systems
  - Secure Boot and UEFI enabled
  - Windows Defender or third-party antivirus/EDR
- Domain Controllers SHOULD receive additional hardening (CIS Domain Controller Benchmark, STIG)

**MAY Requirements**:
- [Organization] MAY implement Just Enough Administration (JEA) for delegated administrative access
- [Organization] MAY deploy Local Administrator Password Solution (LAPS)

---

### 2.4.3.2 Linux and Unix Hardening

**MUST Requirements**:
- All Linux/Unix systems MUST be hardened according to applicable standards:
  - **CIS Distribution-Specific Benchmarks** (RHEL, Ubuntu, Debian, SUSE, Oracle Linux, Amazon Linux)
  - **DISA RHEL STIG** (for Red Hat Enterprise Linux in defense environments)
  - **Vendor Security Guides** (Red Hat Security Guide, Ubuntu Security Features)
- Hardening MUST include:
  - **Account Management**: Disable root login via SSH, enforce sudo, password policies
  - **SSH Configuration**: Disable protocol 1, disable root login, use key-based authentication, restrict ciphers
  - **Filesystem Permissions**: Proper ownership and permissions on critical files (/etc/passwd, /etc/shadow, /etc/sudoers)
  - **Filesystem Mounting**: Secure mount options (noexec, nosuid, nodev on /tmp, /var, /home)
  - **Service Hardening**: Disable unnecessary services (xinetd, telnet, FTP, legacy protocols)
  - **Firewall**: iptables/nftables or firewalld configured and enabled
  - **SELinux or AppArmor**: Enabled and in enforcing mode (not permissive)
  - **Kernel Parameters**: Security-relevant sysctl settings (network hardening, ASLR, kernel protections)
  - **Logging and Auditing**: auditd configured, centralized logging enabled

**SHOULD Requirements**:
- Linux/Unix hardening SHOULD include:
  - Disk encryption (LUKS, dm-crypt)
  - File integrity monitoring (AIDE, Tripwire, OSSEC)
  - Centralized authentication (LDAP, Active Directory integration)
  - Intrusion detection (OSSEC, Fail2Ban)
  - Regular vulnerability scanning
- Bastion/jump hosts SHOULD receive enhanced hardening (CIS Level 2, multi-factor authentication)

**MAY Requirements**:
- [Organization] MAY implement mandatory access controls (SELinux policies, AppArmor profiles)
- [Organization] MAY deploy host-based intrusion prevention systems (HIPS)

---

### 2.4.3.3 Network Operating System Hardening

**MUST Requirements**:
- Network devices (routers, switches, wireless controllers) MUST be hardened according to:
  - **CIS Network Device Benchmarks** (Cisco IOS, Juniper JunOS, Palo Alto, Fortinet)
  - **DISA Network Device STIGs** (if applicable)
  - **Vendor Security Configuration Guides**
- Hardening MUST include:
  - **Access Control**: Console password, enable secret, VTY line passwords
  - **Authentication**: Local users with strong passwords, or centralized (TACACS+, RADIUS)
  - **Authorization**: Privilege levels, command authorization
  - **Accounting**: Logging of administrative actions
  - **Management Protocols**: SSH enabled (disable Telnet), HTTPS for web management (disable HTTP), SNMP v3 only (disable v1/v2c)
  - **Service Hardening**: Disable unnecessary services (CDP, LLDP on edge ports, HTTP server, finger, bootp)
  - **Routing Protocols**: Authentication (MD5 or stronger), filter advertisements
  - **Time Synchronization**: NTP configured with authentication
  - **Logging**: Send logs to centralized syslog server, buffer logs locally

**SHOULD Requirements**:
- Network device hardening SHOULD include:
  - Control plane policing (rate limiting)
  - Management plane protection
  - Banner messages (legal warnings)
  - Encrypted management (SSH keys, HTTPS certificates)
- Wireless controllers SHOULD implement WPA3, 802.1X authentication, rogue AP detection

---

## 2.4.4 Application Hardening

### 2.4.4.1 Web Server Hardening

**MUST Requirements**:
- All web servers MUST be hardened according to applicable standards:
  - **CIS Apache HTTP Server Benchmark**
  - **CIS NGINX Benchmark**
  - **CIS Microsoft IIS Benchmark**
  - **DISA Apache or IIS STIG** (if applicable)
- Hardening MUST include:
  - **Remove Default Content**: Delete default pages, sample files, documentation
  - **Disable Directory Listing**: Prevent enumeration
  - **HTTP Methods**: Allow only necessary methods (GET, POST, HEAD), disable TRACE, OPTIONS, DELETE
  - **Error Handling**: Custom error pages (avoid verbose errors leaking information)
  - **TLS/SSL Configuration**: Enforce HTTPS, disable weak protocols (SSLv3, TLS 1.0/1.1), disable weak ciphers
  - **HTTP Security Headers**: Implement X-Frame-Options, X-Content-Type-Options, Content-Security-Policy, Strict-Transport-Security (HSTS)
  - **Server Tokens**: Disable or minimize server version disclosure
  - **Request Limits**: Limit request size, timeout configurations
  - **Logging**: Access logs and error logs enabled, sent to centralized logging

**SHOULD Requirements**:
- Web server hardening SHOULD include:
  - Web Application Firewall (WAF) integration
  - Rate limiting and DDoS protection
  - Separate user for web server process (not root)
  - File permission hardening (web root read-only)
  - ModSecurity or equivalent (for Apache/NGINX)

---

### 2.4.4.2 Application Server Hardening

**MUST Requirements**:
- Application servers (Tomcat, JBoss, WebSphere, WebLogic) MUST be hardened according to:
  - **CIS Benchmarks** (Tomcat)
  - **DISA STIGs** (Tomcat, JBoss, WebSphere, WebLogic)
  - **Vendor Security Guides**
- Hardening MUST include:
  - **Remove Default Applications**: Delete manager apps, sample applications
  - **Authentication**: Enforce strong authentication for admin interfaces
  - **Access Control**: Restrict access to management interfaces (localhost or specific IPs)
  - **TLS/SSL**: Enforce encrypted connections
  - **Logging**: Enable detailed logging, centralized log forwarding
  - **Service Account**: Run under dedicated service account (not root/administrator)

---

### 2.4.4.3 Database Hardening

**MUST Requirements**:
- All database systems MUST be hardened according to applicable standards:
  - **CIS Benchmarks**: SQL Server, Oracle Database, PostgreSQL, MySQL, MariaDB, MongoDB
  - **DISA STIGs**: SQL Server, Oracle Database, PostgreSQL, MySQL
  - **Vendor Security Guides**
- Hardening MUST include:
  - **Authentication**: Disable default accounts (sa, root, postgres), enforce strong passwords
  - **Access Control**: Least privilege principle, role-based access control (RBAC)
  - **Network Security**: Bind to specific interfaces (not 0.0.0.0), firewall rules restricting access
  - **Encryption**: 
    - Encrypt data at rest (Transparent Data Encryption, filesystem encryption)
    - Encrypt data in transit (TLS/SSL for client connections)
  - **Auditing**: Enable database audit logs, log administrative actions and sensitive data access
  - **Patch Management**: Apply security patches regularly
  - **Remove Sample Databases**: Delete test/sample databases

**SHOULD Requirements**:
- Database hardening SHOULD include:
  - Separate service accounts for each database instance
  - Database activity monitoring (DAM) tools
  - Vulnerability scanning for database configurations
  - Backup encryption

---

## 2.4.5 Network Infrastructure Hardening

### 2.4.5.1 Firewall Hardening

**MUST Requirements**:
- All firewalls MUST be hardened according to:
  - **CIS Benchmarks** (Cisco ASA, Palo Alto, Fortinet, Check Point)
  - **DISA STIGs** (Cisco ASA, Palo Alto, Fortinet)
  - **Vendor Security Best Practices**
- Hardening MUST include:
  - **Default Deny**: Implement implicit deny-all rules at the end of rulesets
  - **Rule Review**: Regular review and cleanup of firewall rules (quarterly minimum)
  - **Rule Documentation**: Every rule must have a business justification
  - **Administrative Access**: Restrict management access to specific IPs/networks, use multi-factor authentication
  - **Logging**: Enable comprehensive logging of allowed and denied traffic
  - **High Availability**: Configure redundancy where critical
  - **Firmware Updates**: Maintain current firmware versions

**SHOULD Requirements**:
- Firewall hardening SHOULD include:
  - Next-Generation Firewall (NGFW) features: IPS, application control, threat intelligence
  - Segmentation: Internal network segmentation using firewalls or VLANs
  - Geo-blocking: Block traffic from non-business-relevant countries

---

### 2.4.5.2 Load Balancer and Proxy Hardening

**MUST Requirements**:
- Load balancers and proxies MUST be hardened according to vendor security guides and applicable benchmarks
- Hardening MUST include:
  - **TLS/SSL Offloading**: Use strong ciphers, disable weak protocols
  - **Access Control**: Restrict administrative access
  - **Health Checks**: Properly configure backend health monitoring
  - **Logging**: Enable access and security logs

---

## 2.4.6 Cloud Service Hardening

### 2.4.6.1 Cloud Infrastructure (IaaS) Hardening

**MUST Requirements**:
- Cloud infrastructure configurations MUST be hardened according to:
  - **CIS Amazon Web Services Foundations Benchmark**
  - **CIS Microsoft Azure Foundations Benchmark**
  - **CIS Google Cloud Platform Foundations Benchmark**
  - **Azure Security Benchmark (ASB)** - Microsoft's recommended baseline
  - **AWS Well-Architected Framework** - Security pillar
- Hardening MUST include:
  - **Identity and Access Management (IAM)**:
    - Disable root account usage (AWS) or break-glass accounts (Azure)
    - Enforce multi-factor authentication (MFA) for all users
    - Implement least privilege access
    - Regularly review and remove unused permissions
  - **Network Security**:
    - Security groups / network security groups (NSGs) configured with least privilege
    - No 0.0.0.0/0 ingress rules except where absolutely necessary (load balancers)
    - Private subnets for backend systems
    - Network flow logs enabled
  - **Storage Security**:
    - Block public access to storage buckets/accounts by default (AWS S3 Block Public Access, Azure Storage)
    - Encryption at rest enabled (SSE-S3, SSE-KMS, Azure Storage Service Encryption)
    - Versioning enabled for critical data
    - Access logging enabled
  - **Compute Security**:
    - Instance/VM hardening per OS standards (Section 2.4.3)
    - No public IP addresses on backend instances
    - Instance metadata service protections (IMDSv2 for AWS)
    - Security agents installed (antivirus, EDR)
  - **Logging and Monitoring**:
    - CloudTrail (AWS), Activity Log (Azure), Cloud Audit Logs (GCP) enabled in all regions
    - Log retention for compliance period (minimum 90 days, 1 year recommended)
    - Centralized log aggregation (CloudWatch, Azure Monitor, Cloud Logging)
    - Alerting on security events (unauthorized access attempts, configuration changes)
  - **Data Protection**:
    - Encryption in transit (TLS/SSL)
    - Encryption at rest (native cloud encryption or bring-your-own-key)
    - Backup and disaster recovery configured

**SHOULD Requirements**:
- Cloud hardening SHOULD include:
  - Cloud Security Posture Management (CSPM) tools (AWS Security Hub, Azure Security Center, GCP Security Command Center, or third-party)
  - Automated compliance scanning (AWS Config Rules, Azure Policy)
  - Tagging standards for resource organization and cost allocation
  - Service Control Policies (AWS Organizations) or Azure Policy for governance

**MAY Requirements**:
- [Organization] MAY implement cloud-native security services (AWS GuardDuty, Azure Sentinel, GCP Chronicle)
- [Organization] MAY use Infrastructure as Code (Terraform, CloudFormation) with security scanning

---

### 2.4.6.2 Platform as a Service (PaaS) Hardening

**MUST Requirements**:
- PaaS configurations (Azure App Services, AWS Lambda, GCP App Engine, managed databases) MUST be hardened:
  - Authentication enabled (Azure AD, AWS IAM, GCP IAM)
  - Network isolation where supported (VNet integration, VPC endpoints)
  - Encryption enabled
  - Logging enabled
  - Vulnerability scanning enabled (container scanning for containers)

---

### 2.4.6.3 Software as a Service (SaaS) Hardening

**MUST Requirements**:
- SaaS application configurations (Office 365, Salesforce, ServiceNow, etc.) MUST be hardened:
  - **Authentication**: Multi-factor authentication (MFA) enforced
  - **Authorization**: Role-based access control (RBAC), least privilege
  - **Data Protection**: Encryption enabled where available, Data Loss Prevention (DLP) policies configured
  - **Logging**: Audit logs enabled and retained
  - **Integrations**: Third-party app permissions reviewed and restricted

**SHOULD Requirements**:
- SaaS hardening SHOULD include:
  - Conditional access policies (IP restrictions, device compliance)
  - Cloud Access Security Broker (CASB) for visibility and control
  - Regular access reviews (quarterly)

---

## 2.4.7 Container and Orchestration Hardening

### 2.4.7.1 Container Image Hardening

**MUST Requirements**:
- Container images MUST be hardened according to:
  - **CIS Docker Benchmark**
  - **CIS Kubernetes Benchmark**
  - **DISA Container Platform STIGs** (if applicable)
- Hardening MUST include:
  - **Base Image Selection**: Use minimal base images (Alpine, Distroless)
  - **Vulnerability Scanning**: Scan images for vulnerabilities before deployment
  - **No Root User**: Run containers as non-root user
  - **Read-Only Filesystem**: Where feasible, mount root filesystem as read-only
  - **Remove Unnecessary Tools**: No shells, compilers, or debugging tools in production images
  - **Secrets Management**: No hardcoded secrets in images (use secrets management tools)

---

### 2.4.7.2 Kubernetes Hardening

**MUST Requirements**:
- Kubernetes clusters MUST be hardened according to CIS Kubernetes Benchmark
- Hardening MUST include:
  - **API Server**: Authentication, authorization (RBAC), admission control
  - **etcd**: Encrypted, restricted access, backed up
  - **Network Policies**: Implement pod-to-pod network segmentation
  - **Pod Security**: Pod Security Standards enforced (restricted profile for production)
  - **RBAC**: Least privilege access, no cluster-admin for applications
  - **Secrets**: Use Kubernetes Secrets or external secret management (HashiCorp Vault)

---

## 2.4.8 IoT and Operational Technology (OT) Hardening

**MUST Requirements** (if applicable):
- IoT and OT systems MUST be hardened where technically feasible
- Hardening MUST include:
  - **Network Segmentation**: Isolate IoT/OT networks from corporate IT
  - **Authentication**: Change default credentials, enforce strong passwords
  - **Firmware Updates**: Apply security patches when available
  - **Disable Unnecessary Services**: Disable unused protocols and ports
  - **Monitoring**: Implement anomaly detection for unusual behavior

**SHOULD Requirements**:
- OT environments SHOULD follow NIST SP 800-82 (Guide to Industrial Control Systems Security)
- IoT devices SHOULD be inventoried and tracked in the CMDB

**The Reality Check**: *Many IoT/OT devices cannot be hardened to IT standards—they're vendor-managed, proprietary, or lack security features. Focus on network segmentation, monitoring, and compensating controls.*

---

## 2.4.9 Hardening Verification and Testing

### 2.4.9.1 Automated Compliance Scanning

**MUST Requirements**:
- [Organization] MUST implement automated scanning to verify hardening compliance
- Scanning MUST occur:
  - After initial system deployment (pre-production)
  - After configuration changes
  - Periodically (monthly minimum for critical systems, quarterly for others)
- Scan results MUST be reviewed and remediation tracked

**SHOULD Requirements**:
- [Organization] SHOULD use automated scanning tools:
  - **CIS-CAT Pro** (CIS Benchmarks)
  - **DISA STIG Compliance Checker (SCC)** (DISA STIGs)
  - **OpenSCAP** (open-source SCAP scanner)
  - **Qualys Policy Compliance, Tenable.sc, Rapid7 InsightVM** (commercial scanners)
  - **Cloud-native tools** (AWS Config, Azure Policy, GCP Security Command Center)

---

### 2.4.9.2 Penetration Testing

**SHOULD Requirements**:
- [Organization] SHOULD conduct penetration testing to validate hardening effectiveness
- Penetration tests SHOULD include configuration weakness assessments
- Tests SHOULD occur annually or after major infrastructure changes

---

### 2.4.9.3 Security Validation in CI/CD

**SHOULD Requirements**:
- [Organization] SHOULD integrate security scanning into CI/CD pipelines:
  - Infrastructure as Code (IaC) scanning (Terraform, CloudFormation)
  - Container image scanning
  - Configuration drift detection
- Failed security checks SHOULD block deployments or require approval

---

## 2.4.10 Hardening Documentation

**MUST Requirements**:
- All hardening configurations MUST be documented in configuration baselines (per ISMS-POL-A.8.9-S2.1)
- Documentation MUST include:
  - Hardening standard applied (CIS Level 1, DISA STIG, etc.)
  - Controls implemented
  - Deviations from standard (with justification)
  - Compensating controls (if any)
- Documentation MUST be maintained as systems evolve

---

## 2.4.11 Deviations and Risk Acceptance

**MUST Requirements**:
- Any deviation from hardening standards MUST be:
  - Documented with business or technical justification
  - Risk-assessed for security impact
  - Approved by CISO or designated authority
  - Compensating controls implemented where feasible
  - Reviewed periodically (quarterly minimum)
- High-risk deviations MUST be tracked and escalated to senior management

**SHOULD Requirements**:
- Deviations SHOULD be minimized
- Long-standing deviations SHOULD trigger re-evaluation (can we now implement the control?)

**Common Legitimate Deviations**:
- Legacy application compatibility requirements
- Vendor-supported configurations that conflict with standards
- Operational requirements (e.g., monitoring tools needing specific access)
- Performance constraints in specific environments

---

## 2.4.12 Hardening and Patching Integration

**MUST Requirements**:
- Security hardening MUST NOT be considered a substitute for security patching
- Patching MUST follow [Organization]'s patch management policy
- Critical vulnerabilities MUST be patched within defined SLAs regardless of hardening status

**The Reality**: *Hardening reduces attack surface. Patching remediates known vulnerabilities. Both are necessary. A hardened but unpatched system is still vulnerable.*

---

## 2.4.13 Hardening for New Technologies

**SHOULD Requirements**:
- [Organization] SHOULD establish a process for hardening emerging technologies:
  - Research available hardening guidance (vendor, CIS, NIST)
  - Conduct security assessment if no guidance exists
  - Document custom hardening standards
  - Submit recommendations to standards bodies (CIS, DISA) for inclusion

**MAY Requirements**:
- [Organization] MAY participate in security community efforts to develop hardening standards

---

## 2.4.14 Training and Awareness

**SHOULD Requirements**:
- System administrators, DevOps engineers, and cloud architects SHOULD receive training on:
  - Hardening standards applicable to their technologies
  - Using compliance scanning tools
  - Secure configuration practices
  - Recognizing security misconfigurations
- Training SHOULD occur upon hiring and annually thereafter

---

## 2.4.15 The Reality of Security Hardening

**Feynman's Final Word**: 

*"Security hardening is not a one-time checkbox. Systems drift, administrators make changes, new vulnerabilities emerge, and standards evolve. The organizations that succeed are those that:*

*1. Start with a good baseline (CIS Level 1 or equivalent)
2. Automate compliance scanning (you can't fix what you don't measure)
3. Prioritize critical systems (100% perfection on 10 systems beats 10% perfection on 1000)
4. Document deviations honestly (hiding risk doesn't eliminate it)
5. Integrate hardening into deployment workflows (shift left)*

*Aim for 95% compliance on critical controls across critical systems. That's achievable and defensible. Chasing 100% compliance on every control across every system is cargo cult security—expensive, distracting, and ultimately less secure than focusing effort where it matters."*

---

**END OF DOCUMENT**

**Cross-References**:
- ISMS-POL-A.8.9-S1: Purpose, Scope, Definitions
- ISMS-POL-A.8.9-S2: Requirements Overview
- ISMS-POL-A.8.9-S2.1: Baseline Configuration Requirements
- ISMS-POL-A.8.9-S2.2: Change Control Requirements
- ISMS-POL-A.8.9-S2.3: Configuration Monitoring Requirements
- ISMS-POL-A.8.9-S3: Roles and Responsibilities (next)
- ISMS-POL-A.8.9-S5.A: Configuration Standards by Asset Type
- ISMS-IMP-A.8.9.4: Security Hardening Assessment Specification

---