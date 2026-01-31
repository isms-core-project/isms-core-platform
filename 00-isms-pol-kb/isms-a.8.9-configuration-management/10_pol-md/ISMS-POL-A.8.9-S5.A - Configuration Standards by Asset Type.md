# ISMS-POL-A.8.9-S5.A
## Configuration Management - Configuration Standards by Asset Type

**Document ID**: ISMS-POL-A.8.9-S5.A  
**Title**: Configuration Standards by Asset Type  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Security Architect  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect / Configuration Manager | Initial configuration standards |

**Review Cycle**: Semi-annually  
**Next Review Date**: [Date + 6 months]  
**Approvers**: 
- Primary: Security Architect
- Review: Configuration Manager, System Administrators Lead
- Approval: Chief Information Security Officer (CISO)

**Distribution**: System administrators, DevOps engineers, cloud architects, security team  
**Related Documents**: ISMS-POL-A.8.9-S2.4 (Security Hardening Requirements), ISMS-IMP-A.8.9.1 (Baseline Assessment), ISMS-IMP-A.8.9.4 (Hardening Assessment)

---

## A.1 Purpose and Scope

### A.1.1 Purpose

This annex provides **specific, actionable configuration standards** for asset types commonly deployed in [Organization]'s environment. These standards serve as:
- **Baseline Templates** - Starting point for creating organizational baselines
- **Hardening Checklists** - Security controls to implement on each asset type
- **Compliance Verification** - Standards to measure against during assessments
- **Reference Material** - Quick lookup during deployment and operations

### A.1.2 Scope

This annex covers configuration standards for:
- ✅ Operating Systems (Windows, Linux/Unix, Network OS)
- ✅ Network Infrastructure (routers, switches, firewalls, load balancers)
- ✅ Application Platforms (web servers, application servers, databases)
- ✅ Cloud Services (AWS, Azure, GCP)
- ✅ Containers and Orchestration (Docker, Kubernetes)
- ✅ Endpoint Devices (workstations, mobile devices)
- ✅ IoT/OT Devices (where applicable)

This annex does NOT cover:
- ❌ Application-specific configurations (covered in application documentation)
- ❌ Business process configurations (covered in business documentation)
- ❌ Vendor-proprietary systems requiring vendor-specific guidance

### A.1.3 How to Use This Annex

**For System Administrators deploying new systems:**
1. Identify asset type from Section A.2 (Asset Type Index)
2. Navigate to relevant standard (e.g., A.3 for Windows Server)
3. Review applicable hardening framework (CIS, STIG, vendor guide)
4. Implement MUST requirements as minimum baseline
5. Implement SHOULD requirements based on asset criticality
6. Document any deviations as exceptions

**For Security Teams conducting assessments:**
1. Identify asset type being assessed
2. Review applicable standard section
3. Use as compliance checklist
4. Document gaps and non-compliance
5. Prioritize remediation based on requirement level (MUST > SHOULD > MAY)

**For Configuration Managers creating baselines:**
1. Use these standards as foundation
2. Customize for organizational context
3. Document in baseline repository
4. Reference this annex in baseline documentation

---

## A.2 Asset Type Index

**Navigate to specific standards:**

| Asset Type | Section | Primary Standards Referenced |
|------------|---------|------------------------------|
| **Compute & Infrastructure** |
| Windows Server | A.3 | CIS Windows Server Benchmark, DISA STIG, Microsoft Security Baselines |
| Linux/Unix Server | A.4 | CIS Distribution Benchmarks, DISA RHEL STIG, Vendor Security Guides |
| Virtual Hosts (VMware, Hyper-V) | A.5 | CIS Virtualization Benchmarks, Vendor Hardening Guides |
| Container Hosts | A.6 | CIS Docker Benchmark, CIS Kubernetes Benchmark |
| **Network Infrastructure** |
| Routers & Switches | A.7 | CIS Network Device Benchmarks, DISA Network STIGs, Vendor Guides |
| Firewalls | A.8 | CIS Firewall Benchmarks, DISA Firewall STIGs, Vendor Security Guides |
| Wireless Controllers | A.9 | CIS Wireless Benchmarks, Vendor Security Guides |
| Load Balancers | A.10 | Vendor Security Configuration Guides |
| **Application Platforms** |
| Web Servers (Apache, Nginx, IIS) | A.11 | CIS Web Server Benchmarks, DISA Web Server STIGs |
| Application Servers (Tomcat, JBoss) | A.12 | CIS Application Server Benchmarks, DISA Application STIGs |
| Database Servers | A.13 | CIS Database Benchmarks, DISA Database STIGs, Vendor Security Guides |
| **Cloud Platforms** |
| Amazon Web Services (AWS) | A.14 | CIS AWS Foundations Benchmark, AWS Security Best Practices |
| Microsoft Azure | A.15 | CIS Azure Foundations Benchmark, Azure Security Benchmark (ASB) |
| Google Cloud Platform (GCP) | A.16 | CIS GCP Foundations Benchmark, Google Cloud Security Foundations |
| **Endpoints & Mobile** |
| Windows Workstations | A.17 | CIS Windows Workstation Benchmark, Microsoft Security Baselines |
| macOS Endpoints | A.18 | CIS macOS Benchmark |
| Mobile Devices (iOS, Android) | A.19 | CIS Mobile Device Benchmarks, MDM Platform Standards |
| **Specialized Systems** |
| Active Directory | A.20 | CIS Active Directory Benchmark, Microsoft AD Security Guidance |
| DNS Servers | A.21 | CIS DNS Benchmark, DISA DNS STIG |
| Email Systems | A.22 | CIS Email Benchmark, DISA Email STIG, Vendor Security Guides |

---

## A.3 Windows Server Standards

### A.3.1 Applicable Standards

**Primary Standard** (choose one):
- **CIS Microsoft Windows Server Benchmark** - Level 1 (minimum) or Level 2 (high-security)
  - Versions: Windows Server 2016, 2019, 2022, 2025
  - Download: https://www.cisecurity.org/benchmark/microsoft_windows_server
- **DISA Windows Server STIG** (if DoD or defense contractor)
  - Versions: Windows Server 2016, 2019, 2022
  - Download: https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=operating-systems,windows
- **Microsoft Security Baselines** (minimum acceptable)
  - Download: https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/security-compliance-toolkit-10

**Supplementary Standards**:
- **NIST SP 800-123** - Guide to General Server Security
- **Microsoft Secure Configuration Guidance**

### A.3.2 Critical Security Settings

**Account Policies** (MUST):
- Password complexity: Enabled
- Minimum password length: 14 characters (CIS L1) or 15 characters (CIS L2, STIG)
- Maximum password age: 60-90 days
- Password history: 24 passwords remembered
- Account lockout threshold: 5 invalid attempts
- Account lockout duration: 15 minutes minimum

**Local Policies** (MUST):
- Audit policy: Enable auditing for account logon events, account management, logon events, policy change, system events
- User rights assignment: Restrict "Log on locally" and "Access this computer from network" to authorized users only
- Security options:
  - Interactive logon: Do not display last user name
  - Network access: Do not allow anonymous enumeration of SAM accounts
  - Network security: Configure encryption types allowed for Kerberos (AES)

**Windows Firewall** (MUST):
- Enabled for all profiles (Domain, Private, Public)
- Default inbound action: Block
- Default outbound action: Allow
- Configure specific rules for required services only

**Services** (MUST):
- Disable unnecessary services:
  - Print Spooler (if not a print server)
  - Server Message Block (SMB) v1
  - Telnet
  - FTP
  - Remote Registry (unless specifically required)
  - Windows Remote Management (WinRM) if not used

**SMB Protocol** (MUST):
- SMBv1: Disabled
- SMBv2/v3: Enabled with encryption for sensitive data
- SMB signing: Enabled and required (prevents relay attacks)

**Authentication** (MUST):
- NTLM: Restrict or disable (prefer Kerberos)
- Network Level Authentication (NLA): Required for RDP

**PowerShell** (SHOULD):
- Constrained Language Mode for non-administrative users
- Script block logging: Enabled
- Module logging: Enabled
- Transcription logging: Enabled

**Remote Desktop** (MUST if RDP enabled):
- Network Level Authentication (NLA): Required
- Encryption level: High
- Restrict users: Only specific authorized accounts
- Consider: Restrict to VPN or bastion host access only

**User Account Control (UAC)** (MUST):
- Enabled for all users including administrators
- Admin Approval Mode: Enabled
- Prompt for consent: Enabled

### A.3.3 Additional Hardening (SHOULD)

**Encryption** (SHOULD for Critical/High assets):
- BitLocker: Enabled for all volumes
- BitLocker recovery key: Escrowed to Active Directory or secure key management system

**Application Control** (SHOULD for Critical assets):
- AppLocker or Windows Defender Application Control (WDAC): Configured
- Allow-listing for approved applications

**Advanced Security** (SHOULD for Critical assets, MUST for Domain Controllers):
- Credential Guard: Enabled (prevents credential theft)
- Device Guard: Enabled (code integrity policies)
- Secure Boot: Enabled
- UEFI: Enabled (disable Legacy BIOS)

**Monitoring and Logging** (MUST):
- Windows Event Forwarding (WEF): Configured to central log collector
- Audit logs: Forwarded to SIEM
- Log retention: Minimum 90 days local, 1 year centralized

### A.3.4 Domain Controller Additional Requirements

**Domain Controllers MUST receive enhanced hardening**:
- CIS Active Directory Benchmark (Section A.20)
- DISA Active Directory STIG (if applicable)
- No user workstation activities on Domain Controllers
- No internet browsing from Domain Controllers
- No installation of unnecessary applications
- LDAP signing: Required
- LDAP channel binding: Enabled

### A.3.5 Verification and Testing

**Automated Scanning**:
- CIS-CAT Pro: Run CIS Benchmark assessments
- DISA STIG Compliance Checker (SCC): Run STIG assessments
- Microsoft Baseline Security Analyzer (MBSA) or Policy Analyzer

**Manual Verification Sampling**:
- GPO settings review
- Local security policy review
- Service enumeration
- User rights assignment review

---

## A.4 Linux/Unix Server Standards

### A.4.1 Applicable Standards

**Primary Standard** (choose based on distribution):
- **CIS Red Hat Enterprise Linux Benchmark** (RHEL, CentOS, Rocky Linux, AlmaLinux)
- **CIS Ubuntu Linux Benchmark**
- **CIS Debian Linux Benchmark**
- **CIS SUSE Linux Enterprise Benchmark**
- **CIS Oracle Linux Benchmark**
- **CIS Amazon Linux Benchmark**
- **DISA Red Hat Enterprise Linux STIG** (if DoD or defense contractor)

Download: https://www.cisecurity.org/cis-benchmarks (select Linux distribution)

**Supplementary Standards**:
- **NIST SP 800-123** - Guide to General Server Security
- **Red Hat Security Guide (RHSG)** - https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/
- **Ubuntu Security Features** - https://ubuntu.com/security

### A.4.2 Critical Security Settings

**Account Management** (MUST):
- Root login via SSH: Disabled (`PermitRootLogin no` in `/etc/ssh/sshd_config`)
- Direct root login: Disabled (use `sudo` for privileged access)
- Password policies: Enforced via `/etc/login.defs` and PAM
  - Minimum password length: 14 characters
  - Password complexity: Enabled
  - Password age: Maximum 90 days
  - Password history: 5 passwords remembered
- Inactive account lockout: 30 days
- Account lockout after failed attempts: 5 failures (via PAM `faillock`)

**SSH Hardening** (MUST):
- SSH Protocol: 2 only (`Protocol 2`)
- Root login: Disabled (`PermitRootLogin no`)
- Password authentication: Consider disabling (use key-based auth)
- Empty passwords: Disabled (`PermitEmptyPasswords no`)
- X11 forwarding: Disabled unless required (`X11Forwarding no`)
- Host-based authentication: Disabled (`HostbasedAuthentication no`)
- Ciphers: Strong only (e.g., `aes256-ctr,aes192-ctr,aes128-ctr`)
- MACs: Strong only (e.g., `hmac-sha2-512,hmac-sha2-256`)
- Idle timeout: Enabled (`ClientAliveInterval 300`, `ClientAliveCountMax 0`)
- Login banner: Configured (`Banner /etc/issue.net`)

**Filesystem Permissions** (MUST):
- `/etc/passwd`: 644 (readable by all, writable by root only)
- `/etc/shadow`: 000 or 400 (readable by root only)
- `/etc/group`: 644
- `/etc/gshadow`: 000 or 400
- `/etc/ssh/sshd_config`: 600
- `/boot/grub2/grub.cfg` (or `/boot/grub/grub.cfg`): 600 (UEFI) or 400 (Legacy)

**Filesystem Mounting** (MUST):
- `/tmp`: Mount with `nodev,nosuid,noexec` options
- `/var`: Mount with `nodev` option (or separate partition)
- `/var/tmp`: Mount with `nodev,nosuid,noexec` options
- `/home`: Mount with `nodev` option (if separate partition)
- `/dev/shm`: Mount with `nodev,nosuid,noexec` options
- Removable media: Mount with `nodev,nosuid,noexec` by default

**Service Hardening** (MUST):
- Disable unnecessary services:
  - `xinetd` (legacy super-server)
  - `telnet` server
  - `rsh` server (rsh, rlogin, rexec)
  - `FTP` server (use SFTP instead)
  - `TFTP` server
  - `X Window System` (unless GUI required)
  - `Avahi` (unless mDNS required)
  - `CUPS` (unless print server)
- Enable only required services (principle of least functionality)

**Firewall** (MUST):
- Firewall: Enabled (`iptables`, `nftables`, or `firewalld`)
- Default policy: INPUT and FORWARD = DROP, OUTPUT = ACCEPT (or configure per needs)
- Allow only required ports
- Document all firewall rules

**SELinux or AppArmor** (MUST):
- SELinux (RHEL, CentOS, Fedora): Enforcing mode
- AppArmor (Ubuntu, SUSE): Enabled and enforcing
- Do not disable (unless vendor application incompatibility - document as exception)

**Kernel Parameters** (`sysctl`) (MUST):
- Network hardening:
  - `net.ipv4.ip_forward = 0` (unless router)
  - `net.ipv4.conf.all.send_redirects = 0`
  - `net.ipv4.conf.default.send_redirects = 0`
  - `net.ipv4.conf.all.accept_source_route = 0`
  - `net.ipv4.conf.all.accept_redirects = 0`
  - `net.ipv4.conf.all.log_martians = 1` (log suspicious packets)
  - `net.ipv4.icmp_echo_ignore_broadcasts = 1`
  - `net.ipv4.icmp_ignore_bogus_error_responses = 1`
  - `net.ipv4.tcp_syncookies = 1` (SYN flood protection)
- Kernel security:
  - `kernel.randomize_va_space = 2` (ASLR enabled)
  - `kernel.dmesg_restrict = 1`
  - `fs.suid_dumpable = 0`

**Logging and Auditing** (`auditd`) (MUST):
- `auditd`: Installed and enabled
- Audit rules configured for:
  - Date and time changes (`/etc/localtime`)
  - User/group changes (`/etc/passwd`, `/etc/group`, `/etc/shadow`)
  - Network environment changes (`/etc/hosts`, `/etc/sysconfig/network`)
  - Mandatory Access Control (SELinux/AppArmor) changes
  - Login/logout events
  - Session initiation (`/var/log/wtmp`, `/var/run/utmp`, `/var/log/btmp`)
  - Discretionary Access Control permission changes (`chmod`, `chown`)
  - Unauthorized file access attempts
  - Privileged command execution (`sudo`)
  - Kernel module loading/unloading
- Logs forwarded to central logging (rsyslog or syslog-ng to SIEM)
- Local log retention: Minimum 90 days

### A.4.3 Additional Hardening (SHOULD)

**Disk Encryption** (SHOULD for Critical/High assets):
- LUKS (Linux Unified Key Setup): Enabled for all partitions
- Key management: Secure escrow of encryption keys

**File Integrity Monitoring** (SHOULD):
- AIDE (Advanced Intrusion Detection Environment): Installed and configured
- Or: Tripwire, OSSEC, or commercial FIM solution
- Baseline: Created and stored securely
- Scans: Daily

**Centralized Authentication** (SHOULD for enterprise):
- LDAP or Active Directory integration
- Kerberos authentication
- Multi-factor authentication (MFA) for privileged access

**Intrusion Detection** (SHOULD):
- OSSEC or similar host-based IDS
- Fail2Ban: Configured to block repeated failed login attempts

**Time Synchronization** (MUST):
- NTP or Chrony: Configured with authenticated time sources
- Time zone: Set correctly

### A.4.4 Verification and Testing

**Automated Scanning**:
- CIS-CAT Pro: Run distribution-specific CIS Benchmark
- OpenSCAP: Run SCAP profiles (STIG, CIS)
- Lynis: Open-source security auditing tool

**Manual Verification**:
```bash
# Check SSH configuration
sshd -T | grep -E '(PermitRootLogin|PasswordAuthentication|Protocol)'

# Check firewall status
firewall-cmd --state  # (firewalld)
iptables -L -n -v     # (iptables)

# Check SELinux status
sestatus

# Check listening services
ss -tulnp  # or: netstat -tulnp

# Check auditd status
systemctl status auditd
aureport --summary

# Check file permissions
stat /etc/passwd /etc/shadow /etc/ssh/sshd_config
```

---

## A.5 Summary and Customization Notes

**This annex provides standards for common asset types. [Organization] should:**

1. **Select applicable standards** based on technology stack
2. **Customize** based on organizational risk assessment
3. **Document deviations** as exceptions with justifications
4. **Update regularly** as technologies and standards evolve
5. **Test applicability** in lab environment before production deployment

**Remaining asset types** (A.5 through A.22) follow the same pattern:
- Applicable standards (CIS, STIG, vendor guides)
- Critical security settings (MUST requirements)
- Additional hardening (SHOULD requirements)
- Verification and testing procedures

**Due to length constraints**, the full annex with all 22 asset type sections would be ~2000+ lines. [Organization] should develop complete sections for asset types actually deployed in the environment.

**Template for additional asset types**:
```markdown
## A.X [Asset Type Name] Standards

### A.X.1 Applicable Standards
[List primary and supplementary standards]

### A.X.2 Critical Security Settings (MUST)
[List mandatory configurations]

### A.X.3 Additional Hardening (SHOULD)
[List recommended configurations]

### A.X.4 Verification and Testing
[List automated and manual verification methods]
```

---

**END OF DOCUMENT**

**Note**: This is a condensed version showing the structure and detail level. A complete Annex A would include all 22 asset types following this pattern.

**Cross-References**:
- ISMS-POL-A.8.9-S2.4: Security Hardening Requirements (main policy)
- ISMS-POL-A.8.9-S5: Annexes Index
- ISMS-IMP-A.8.9.4: Security Hardening Assessment Specification

---