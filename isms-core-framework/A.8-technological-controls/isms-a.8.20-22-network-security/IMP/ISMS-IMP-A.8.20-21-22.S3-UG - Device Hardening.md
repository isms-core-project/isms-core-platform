<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.20-21-22.S3-UG:framework:UG:a.8.20-21-22 -->
**ISMS-IMP-A.8.20-21-22.S3-UG - Device Hardening Process**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Device Hardening |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.20-21-22.S3-UG |
| **Related Policy** | ISMS-POL-A.8.20-21-22 (Network Security) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.20 (Networks Security) |
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

- ISMS-POL-A.8.20-21-22 (Network Security)
- ISMS-IMP-A.8.20-21-22.S1 (Network Discovery)
- ISMS-IMP-A.8.20-21-22.S2 (Architecture Documentation)
- ISMS-IMP-A.8.20-21-22.S4 (Services Security)
- ISMS-IMP-A.8.20-21-22.S5 (Segmentation Implementation)

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Services Catalog | Catalogue all network services in use |
| 3 | DNS Security Assessment | Assess DNS service security configuration |
| 4 | DHCP Security Assessment | Assess DHCP service security configuration |
| 5 | NTP Security Assessment | Assess NTP service security configuration |
| 6 | Proxy Security Assessment | Assess proxy service security configuration |
| 7 | Additional Services | Document and assess additional network services |
| 8 | Gap Analysis | Identify network services security gaps |
| 9 | Service Dependencies | Map service dependencies and risks |
| 10 | Evidence Register | Store and reference evidence supporting assessments |
| 11 | Summary Dashboard | Compliance status and key metrics overview |
| 12 | Approval Sign-Off | Management review sign-off and certification |

---

# Purpose and Scope

## Purpose

This document provides **practical, step-by-step guidance** for hardening network devices to reduce their attack surface and improve security posture. Device hardening implements **Control A.8.20 (Networks Security)** requirements for securing network infrastructure.

**Device hardening** involves:

- Disabling unnecessary services and protocols
- Implementing strong authentication and access controls
- Configuring secure management interfaces
- Enabling logging and monitoring
- Applying security patches and firmware updates
- Following vendor and industry hardening baselines

## Scope

This guidance covers hardening for:

- **Routers** (Cisco, Juniper, MikroTik, etc.)
- **Switches** (Cisco, HP/Aruba, Juniper, etc.)
- **Firewalls** (Palo Alto, Fortinet, pfSense, etc.)
- **Wireless Access Points** (Cisco, Aruba, Ubiquiti, etc.)
- **Load Balancers** (F5, HAProxy, NGINX, cloud load balancers)
- **Network Security Appliances** (IDS/IPS, network monitoring)

## Applicability

This guidance is **technology-agnostic** with specific examples for:

- Cisco IOS/IOS-XE devices (routers, switches)
- Generic firewall hardening (applicable to any firewall platform)
- Cloud networking (AWS, Azure, GCP security groups and network ACLs)

## Who Should Use This Guidance

- Network engineers implementing device hardening
- Security teams auditing network device configurations
- ISMS implementers preparing for A.8.20 assessments
- Auditors verifying device hardening compliance

---

# Process Overview

## Hardening Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│              DEVICE HARDENING PROCESS                            │
└─────────────────────────────────────────────────────────────────┘

Phase 1: Baseline Development
├─ Identify hardening standards (CIS Benchmarks, vendor guides)
├─ Adapt standards to [Organisation] environment
├─ Document hardening baseline per device type
└─ Get baseline approved by security and network teams

Phase 2: Pre-Hardening Preparation
├─ Backup current device configurations
├─ Document current state (for rollback if needed)
├─ Schedule hardening window (maintenance window)
└─ Prepare rollback plan

Phase 3: Hardening Implementation
├─ Apply hardening configuration changes
├─ Verify device functionality after each change
├─ Document changes made
└─ Test connectivity and services

Phase 4: Validation and Testing
├─ Verify hardening configuration applied correctly
├─ Run compliance scan (compare against baseline)
├─ Test security controls (attempt unauthorised access)
└─ Document validation results

Phase 5: Documentation and Change Management
├─ Update configuration management database (CMDB)
├─ Update network documentation
├─ Close change request
└─ Schedule next hardening review (quarterly/annual)

Phase 6: Ongoing Maintenance
├─ Periodic compliance checks (quarterly)
├─ Configuration drift detection and remediation
├─ Patch management (firmware/software updates)
└─ Baseline updates (as new threats emerge)
```

## Key Principles

- **Defense in Depth**: Multiple layers of security (not just one control)
- **Least Privilege**: Minimize permissions and access (only what's needed)
- **Secure by Default**: Default configurations should be secure
- **Minimize Attack Surface**: Disable unnecessary services, protocols, ports
- **Auditability**: All administrative actions must be logged
- **Maintainability**: Balance security with operational needs

---

# Prerequisites and Tools

## Required Access and Permissions

- **Administrative access** to network devices (privileged/enable mode)
- **Configuration backup access** (TFTP/SCP server, backup tool access)
- **Change management approval** (RFC approved for hardening changes)
- **Test environment** (lab for testing hardening changes before production)

## Hardening Baseline Sources

| Source | Description | URL / Access |
|--------|-------------|--------------|
| **CIS Benchmarks** | Industry-standard hardening guides | https://www.cisecurity.org/cis-benchmarks/ <br>(Free with registration) |
| **Vendor Hardening Guides** | Vendor-specific guides (Cisco, Juniper, etc.) | Vendor documentation portals |
| **NIST SP 800-123** | Guide to General Server Security | https://csrc.nist.gov/publications/ |
| **NSA Security Guides** | Government-published hardening guides | https://www.nsa.gov/Resources/Cybersecurity/ |
| **DISA STIGs** | Security Technical Implementation Guides | https://public.cyber.mil/stigs/ |

## Configuration Management Tools

| Tool | Purpose | Type |
|------|---------|------|
| **RANCID** | Router/switch config backup | Open-source |
| **Oxidized** | Network device config backup | Open-source |
| **Ansible** | Configuration automation | Open-source |
| **SolarWinds NCM** | Network Configuration Manager | Commercial |
| **Nessus / Qualys** | Configuration compliance scanning | Commercial |

---

# Step-by-Step Procedures

## Phase 1: Develop Hardening Baseline

### Identify Applicable Standards

**Action**: Determine which hardening standards apply to your device types.

**Common Standards**:

- **CIS Cisco IOS Benchmark**: For Cisco routers and switches
- **CIS Palo Alto Firewall Benchmark**: For Palo Alto firewalls
- **CIS Kubernetes Benchmark**: For container networking
- **Vendor Hardening Guides**: Check vendor documentation (Cisco, Juniper, Fortinet)

**Example**: For Cisco IOS devices, download:

- CIS Cisco IOS Benchmark (e.g., version 4.1.0)
- Cisco IOS Security Configuration Guide

### Adapt Standards to [Organisation] Environment

**Action**: Customize baseline to fit operational requirements.

**Example Customizations**:

- **SNMP**: CIS recommends SNMPv3 only, but [Organisation] may need SNMPv2c for legacy monitoring tools (document as exception)
- **SSH Version**: CIS recommends SSH v2 only → Adopt (no exceptions)
- **Banner Messages**: CIS provides generic banner → Customize with [Organisation] legal language

**Document Exceptions**:
```
Hardening Baseline Exceptions

1. SNMPv2c Allowed (Exception ID: NET-HARD-EXC-001)
   Reason: Legacy monitoring tool (SolarWinds NPM) requires SNMPv2c
   Risk: SNMPv2c is less secure than SNMPv3 (plaintext community string)
   Mitigation: SNMP community string is complex (32 characters), changed quarterly
   Approval: Network Manager, Security Manager
   Review Date: 2026-06-01 (re-evaluate when monitoring tool upgraded)
```

### Create Hardening Checklist per Device Type

**Example: Cisco Router Hardening Checklist**

| # | Requirement | Configuration Command(s) | Compliance Check |
|---|-------------|--------------------------|------------------|
| 1 | Disable HTTP (use HTTPS only) | `no ip http server`<br>`ip http secure-server` | Show: `show ip http server status` |
| 2 | Enable SSH v2 (disable Telnet) | `no line vty 0 4 transport input telnet`<br>`line vty 0 4 transport input ssh`<br>`ip ssh version 2` | Show: `show ip ssh` |
| 3 | Set enable secret (strong password) | `enable secret [strong_password]` | Config check (encrypted) |
| 4 | Configure login banner | `banner login ^Unauthorised access prohibited^` | Show: `show running-config \| include banner` |
| 5 | Enable NTP | `ntp server 10.1.0.30` | Show: `show ntp status` |
| 6 | Configure syslog | `logging host 10.1.0.100` | Show: `show logging` |
| 7 | Disable unused services | `no ip bootp server`<br>`no service dhcp`<br>`no ip domain-lookup` | Config check |
| 8 | Enable SNMP v3 (disable v1/v2c) | `no snmp-server community public`<br>`snmp-server group grp3 v3 priv` | Show: `show snmp group` |
| 9 | Configure VTY ACL (restrict management access) | `access-list 99 permit 192.168.100.0 0.0.0.255`<br>`line vty 0 4 access-class 99 in` | Show: `show access-lists 99` |
| 10 | Set session timeout | `line vty 0 4 exec-timeout 10 0` | Show: `show line vty 0` |
| 11 | Enable IP source verification | `interface GigabitEthernet0/1 ip verify unicast source reachable-via rx` | Show: `show ip interface GigabitEthernet0/1` |
| 12 | Disable CDP/LLDP on external interfaces | `interface GigabitEthernet0/0 no cdp enable` | Show: `show cdp interface` |
| 13 | Configure AAA (RADIUS/TACACS+) | `aaa new-model`<br>`tacacs-server host 10.1.0.50 key [key]` | Show: `show tacacs` |
| 14 | Enable password encryption | `service password-encryption` | Config check |
| 15 | Disable IP source routing | `no ip source-route` | Config check |

---

## Phase 2: Pre-Hardening Preparation

### Backup Current Configuration

**Action**: Backup device config before making changes.

**Methods**:

**1. Manual Backup (Cisco IOS)**:
```bash
# Telnet/SSH into device
enable
show running-config

# Copy output to text file
# OR use TFTP:
copy running-config tftp:
# Server IP: 192.168.100.50
# Filename: router-01-backup-20260108.cfg
```

**2. Automated Backup (Ansible)**:
```yaml
# backup-configs.yml
---

- name: Backup Cisco router configurations

  hosts: routers
  gather_facts: no
  tasks:

    - name: Backup running config

      ios_command:
        commands: show running-config
      register: config_output
    
    - name: Save config to file

      copy:
        content: "{{ config_output.stdout[0] }}"
        dest: "/backups/{{ inventory_hostname }}_{{ ansible_date_time.date }}.cfg"
```

**Run**: `ansible-playbook backup-configs.yml`

**3. Automated Backup (RANCID)**:
```bash
# RANCID setup (runs daily via cron)
rancid-run

# Backups stored in: /var/lib/rancid/[group]/configs/
```

### Document Current State

**Action**: Document device state before hardening (for comparison/rollback).

**Document**:

- Current IOS/firmware version
- Current services enabled (HTTP, Telnet, SNMP, etc.)
- Current access controls (VTY ACLs, SNMP community strings)
- Current logging configuration

**Example State Documentation**:
```
Device: router-hq-01 (10.1.0.1)
Current State ([Date]):

- IOS Version: 15.7(3)M5
- HTTP Server: Enabled (insecure)
- Telnet: Enabled on VTY 0-4
- SNMP: v2c enabled (community: public)
- Logging: Not configured (no syslog server)
- NTP: Not configured
- VTY ACL: None (accessible from any IP)

```

### Prepare Rollback Plan

**Action**: Define rollback steps in case hardening causes issues.

**Rollback Plan**:
1. If device becomes unreachable after hardening:

   - Console access: Connect via console cable
   - Restore backup config: `copy tftp: running-config`
   - Server: 192.168.100.50, File: router-01-backup-20260108.cfg
   
2. If services break:

   - Re-enable specific service (e.g., if SNMP v3 breaks monitoring, temporarily re-enable v2c)
   - Document as exception (NET-HARD-EXC-XXX)
   
3. Emergency contact:

   - Network Manager: [Phone]
   - On-call Engineer: [Phone]

---

## Phase 3: Hardening Implementation

### Cisco Router/Switch Hardening

**Hardening Script** (apply via config mode):

```cisco
! ============================================================================
! Cisco Router/Switch Hardening Configuration
! Device: [HOSTNAME]
! Date: [Date]
! Operator: [Your Name]
! ============================================================================

! ----------------------------------
! 1. Management Security
! ----------------------------------

! Disable HTTP, enable HTTPS
no ip http server
ip http secure-server
ip http authentication local

! Disable Telnet, enable SSH v2
line vty 0 4
  transport input ssh
exit
ip ssh version 2
ip ssh time-out 60
ip ssh authentication-retries 3

! Configure strong enable secret
enable secret [STRONG_PASSWORD_HERE]

! Configure console password and timeout
line console 0
  password [CONSOLE_PASSWORD]
  login
  exec-timeout 10 0
  logging synchronous
exit

! Configure VTY password and timeout
line vty 0 4
  password [VTY_PASSWORD]
  login local
  exec-timeout 10 0
  logging synchronous
exit

! ----------------------------------
! 2. Access Control
! ----------------------------------

! Create management ACL (allow only from management network)
access-list 99 remark Management Access
access-list 99 permit 192.168.100.0 0.0.0.255
access-list 99 deny any log

! Apply ACL to VTY lines
line vty 0 4
  access-class 99 in
exit

! Create local admin user (for AAA fallback)
username admin privilege 15 secret [ADMIN_PASSWORD]

! ----------------------------------
! 3. Logging and Monitoring
! ----------------------------------

! Configure NTP
ntp server 10.1.0.30

! Configure syslog
logging host 10.1.0.100
logging trap informational
logging facility local6
logging source-interface Loopback0

! Enable login logging
login on-success log
login on-failure log

! ----------------------------------
! 4. SNMP Security
! ----------------------------------

! Disable SNMP v1/v2c (remove default community strings)
no snmp-server community public
no snmp-server community private

! Enable SNMP v3 (example)
snmp-server group SNMPv3Group v3 priv
snmp-server user snmpuser SNMPv3Group v3 auth sha [AUTH_PASSWORD] priv aes 128 [PRIV_PASSWORD]
snmp-server view ViewName iso included

! ----------------------------------
! 5. Disable Unnecessary Services
! ----------------------------------

no ip bootp server
no service dhcp
no ip domain-lookup
no service pad
no service finger
no service tcp-small-servers
no service udp-small-servers
no ip http server

! Disable CDP on external interfaces (configure per interface)
! interface GigabitEthernet0/0
!   no cdp enable

! ----------------------------------
! 6. Security Features
! ----------------------------------

! Enable password encryption
service password-encryption

! Disable IP source routing
no ip source-route

! Disable proxy ARP
no ip proxy-arp

! Enable TCP keepalives
service tcp-keepalives-in
service tcp-keepalives-out

! Set login banner
banner login ^
===============================================================================
                   UNAUTHORIZED ACCESS PROHIBITED
  
  This system is for authorised use only. All activity is monitored and
  logged. Unauthorised access is prohibited and will be prosecuted to the
  fullest extent of the law.
===============================================================================
^

banner motd ^
===============================================================================
             [ORGANIZATION NAME] - Network Infrastructure
  
  Maintenance Contact: [EMAIL]
  Emergency Contact: [PHONE]
===============================================================================
^

! ----------------------------------
! 7. AAA (if TACACS+ server available)
! ----------------------------------

! aaa new-model
! tacacs-server host 10.1.0.50 key [TACACS_KEY]
! aaa authentication login default group tacacs+ local
! aaa authorisation exec default group tacacs+ local
! aaa accounting exec default start-stop group tacacs+

! ----------------------------------
! END OF HARDENING CONFIGURATION
! ----------------------------------

! Save configuration
end
write memory
```

**Apply Configuration**:
```bash
# Copy hardening script to device via TFTP
copy tftp://192.168.100.50/router-hardening.cfg running-config

# OR paste configuration via SSH
# (SSH into device, enter config mode, paste commands)
```

**Verify Changes**:
```bash
# Verify HTTP disabled
show ip http server status
# Expected: HTTP server: Disabled

# Verify SSH enabled
show ip ssh
# Expected: SSH Enabled - version 2.0

# Verify SNMP v3 configured
show snmp group
# Expected: SNMPv3Group listed

# Verify VTY ACL applied
show line vty 0
# Expected: Access-class 99 in

# Verify logging configured
show logging
# Expected: Syslog logging: enabled, host 10.1.0.100
```

### Cisco Switch-Specific Hardening

**Additional Switch Hardening** (beyond router hardening):

```cisco
! ----------------------------------
! Switch-Specific Security
! ----------------------------------

! Enable port security (limit MAC addresses per port)
interface range GigabitEthernet1/0/1 - 48
  switchport mode access
  switchport port-security
  switchport port-security maximum 3
  switchport port-security violation restrict
  switchport port-security mac-address sticky
exit

! Enable DHCP snooping
ip dhcp snooping
ip dhcp snooping vlan 10,20,30
interface GigabitEthernet1/0/1
  ip dhcp snooping trust
exit

! Enable BPDU Guard (prevent rogue switches)
spanning-tree portfast bpduguard default

! Disable DTP (Dynamic Trunking Protocol) on access ports
interface range GigabitEthernet1/0/1 - 48
  switchport mode access
  switchport nonegotiate
exit

! Change native VLAN (security best practice)
vlan 999
  name Unused_VLAN
exit
interface GigabitEthernet1/0/1
  switchport trunk native vlan 999
exit

! Disable unused ports
interface range GigabitEthernet1/0/25 - 48
  shutdown
  description UNUSED_PORT
exit
```

### Firewall Hardening (Generic)

**Firewall Hardening Principles** (applicable to any firewall):

1. **Default Deny Policy**: All traffic denied unless explicitly allowed
   ```
   # Palo Alto example:
   security rule "deny-all" {
     from any;
     to any;
     action deny;
     log-end;
   }
   ```

2. **Management Interface Restrictions**:

   - Management interface should NOT be on production network
   - Use separate VLAN/subnet for management (e.g., 192.168.100.0/24)
   - Restrict management access to specific source IPs (admin workstations, jump hosts)

3. **Strong Authentication**:

   - Enforce MFA for administrative access
   - Use RADIUS/TACACS+ for centralized authentication

4. **Logging**:

   - Log all traffic (allowed and denied)
   - Send logs to centralized SIEM
   - Retain logs per regulatory requirements (90 days minimum)

5. **Firmware Updates**:

   - Apply security patches promptly (within 30 days of release)
   - Test in lab before production deployment

6. **Configuration Backup**:

   - Automated daily backups
   - Version control (Git for config-as-code)

### Wireless Access Point Hardening

**Wireless Hardening Checklist**:

| # | Requirement | Configuration |
|---|-------------|---------------|
| 1 | WPA3 Encryption | Use WPA3-Personal or WPA3-Enterprise (not WPA2, never WEP) |
| 2 | 802.1X Authentication | Integrate with RADIUS server for user authentication |
| 3 | Disable WPS | WPS is insecure (brute-forceable) |
| 4 | Change Default SSID | Do not use default SSID (e.g., "Linksys", "NETGEAR") |
| 5 | Disable SSID Broadcast (optional) | Hide SSID (security through obscurity, not strong defense) |
| 6 | MAC Address Filtering (optional) | Whitelist allowed MACs (bypassable, not primary defense) |
| 7 | Isolate Guest Network | Guest WiFi should be on separate VLAN, no access to internal |
| 8 | Disable Remote Management | Management only from wired network |
| 9 | Firmware Updates | Keep AP firmware up-to-date |
| 10 | Rogue AP Detection | Use wireless IDS/IPS (Cisco ISE, Aruba ClearPass) |

**Example (Cisco Wireless Controller)**:
```
# WPA3 Configuration
wlan 10 Corporate-WiFi
  security wpa akm psk
  security wpa akm 802.1x
  security wpa wpa3
  
# 802.1X with RADIUS
radius auth-server 10.1.0.60
  secret [RADIUS_SECRET]
  
# Guest Network Isolation
wlan 20 Guest-WiFi
  vlan 50
  security open
  no security web-auth
  interface-name guest-vlan
```

---

## Phase 4: Validation and Testing

### Configuration Compliance Scan

**Tool**: Use Nessus, Qualys, or Nipper to scan device configuration.

**Example (Nessus)**:
1. Create Policy Compliance Scan
2. Upload CIS Cisco IOS Benchmark audit file (.audit)
3. Scan device (provide SSH credentials)
4. Review compliance report

**Manual Validation** (if no scanning tool):
```bash
# SSH into device
ssh admin@10.1.0.1

# Check each hardening requirement manually
show ip http server status
show ip ssh
show snmp group
show logging
show line vty 0
show access-lists 99
```

### Penetration Testing

**Test Unauthorised Access**:

- Attempt to Telnet to device → Should be refused (Telnet disabled)
- Attempt to access HTTP → Should be refused (HTTP disabled)
- Attempt to SSH from unauthorised IP → Should be denied (VTY ACL)
- Attempt to brute-force SSH login → Should lock out after 3 attempts

**Example Test Commands**:
```bash
# From test machine (not in management network)
telnet 10.1.0.1
# Expected: Connection refused

curl http://10.1.0.1
# Expected: Connection refused

ssh admin@10.1.0.1
# Expected: Connection denied (if source IP not in ACL 99)
```

### Functional Testing

**Verify Device Still Functions**:

- Can legitimate administrators SSH into device?
- Is routing/switching still working? (ping tests, traceroute)
- Are monitoring tools still receiving SNMP data?
- Are logs being sent to syslog server?

**Example Tests**:
```bash
# From management workstation (192.168.100.x)
ssh admin@10.1.0.1
# Expected: Successfully connects

# Ping test
ping 10.1.10.5
# Expected: Success (routing working)

# Check syslog server
# On syslog server:
tail -f /var/log/syslog | grep 10.1.0.1
# Expected: Logs appearing
```

---

## Phase 5: Documentation and Change Management

### Update CMDB

**Action**: Update device records in CMDB to reflect hardening status.

**Fields to Update**:

- Hardening Status: "Hardened" (was "Not Hardened")
- Hardening Date: [Date]
- Hardening Baseline Version: CIS Cisco IOS Benchmark v4.1.0
- Compliance Score: 95% (from compliance scan)
- Next Review Date: 2026-04-08 (quarterly)

### Update Configuration Management System

**Action**: Commit hardened configuration to Git/RANCID.

```bash
# If using Git for config management
cd /config-backups/routers
cp /backups/router-hq-01_20260108_hardened.cfg router-hq-01.cfg
git add router-hq-01.cfg
git commit -m "Hardened router-hq-01 per CIS Benchmark"
git push origin main
```

### Close Change Request

**Action**: Update RFC (Request for Change) to "Complete".

**RFC Closure Notes**:
```
Change Request: RFC-2026-0108-HARDENING
Status: Complete
Completion Date: [Date]

Summary:

- Device hardened per CIS Cisco IOS Benchmark v4.1.0
- Configuration changes applied successfully
- Validation tests passed (compliance scan 95%)
- No service disruptions
- Configuration backed up and version controlled

Post-Implementation Review:

- Device still accessible from management network
- Routing/switching functionality confirmed
- SNMP monitoring working (SNMPv3)
- Syslog logging working

Next Steps:

- Schedule quarterly compliance review (2026-04-08)
- Monitor for configuration drift

```

---

## Phase 6: Ongoing Maintenance

### Periodic Compliance Checks (Quarterly)

**Action**: Run compliance scan every quarter to detect configuration drift.

**Configuration Drift**: Unauthorised changes to device configuration.

**Detection Methods**:
1. **Automated**: RANCID/Oxidized emails diffs daily
2. **Manual**: Compare current config to baseline
3. **Scanning**: Run Nessus/Qualys compliance scan quarterly

**Example (RANCID drift detection)**:
```bash
# RANCID automatically emails diffs
# Email example:
Subject: router-hq-01 config change detected

Diff:

+ line vty 0 4
+   no access-class 99 in

# Analysis: VTY ACL removed (security issue!)
# Action: Restore VTY ACL immediately
```

### Patch Management

**Action**: Apply firmware/software updates regularly.

**Patch Schedule**:

- **Critical Security Patches**: Within 7 days of vendor release
- **Important Patches**: Within 30 days
- **General Updates**: Quarterly (during maintenance windows)

**Patch Process**:
1. Review vendor security advisories (subscribe to mailing lists)
2. Test patch in lab environment
3. Schedule maintenance window
4. Backup config before patching
5. Apply patch
6. Verify device functionality
7. Document patch application

**Example (Cisco IOS upgrade)**:
```bash
# Backup config
copy running-config tftp://192.168.100.50/router-hq-01-pre-upgrade.cfg

# Download new IOS image to device
copy tftp://192.168.100.50/c2900-universalk9-mz.SPA.157-3.M6.bin flash:

# Verify file integrity (MD5 checksum)
verify /md5 flash:c2900-universalk9-mz.SPA.157-3.M6.bin

# Set boot variable
config t
boot system flash:c2900-universalk9-mz.SPA.157-3.M6.bin
exit

# Reload device
reload
# Device will boot with new IOS

# Verify new version
show version
```

### Baseline Updates

**Action**: Update hardening baseline when new threats emerge or standards are updated.

**Triggers for Baseline Updates**:

- New CIS Benchmark version released
- New vulnerabilities discovered (e.g., CVE affecting SSH)
- Regulatory requirement changes
- Internal security policy changes

---

# Automation Opportunities

## Ansible Playbook for Bulk Hardening

**Example Ansible Playbook** (apply hardening to multiple devices):

```yaml
# cisco-hardening.yml
---

- name: Cisco Device Hardening

  hosts: cisco_routers
  gather_facts: no
  tasks:

    - name: Backup current config

      ios_command:
        commands: show running-config
      register: config_backup
    
    - name: Save backup to file

      copy:
        content: "{{ config_backup.stdout[0] }}"
        dest: "/backups/{{ inventory_hostname }}_{{ ansible_date_time.date }}.cfg"
    
    - name: Apply hardening configuration

      ios_config:
        src: templates/cisco-hardening.j2
        save_when: modified
    
    - name: Verify hardening applied

      ios_command:
        commands:

          - show ip http server status
          - show ip ssh
          - show snmp group

      register: verification
    
    - name: Display verification results

      debug:
        var: verification.stdout_lines
```

**Run Playbook**:
```bash
ansible-playbook -i inventory cisco-hardening.yml
```

## Configuration Compliance Automation

**Script**: Automatically check device compliance and generate report.

```python
#!/usr/bin/env python3
"""
Network Device Compliance Checker

Checks device configurations against hardening baseline and generates report.

Requirements: netmiko, pandas
"""

from netmiko import ConnectHandler
import pandas as pd

def check_device_compliance(device_ip, username, password):
    """Connect to device and check hardening compliance."""
    
    device = {
        'device_type': 'cisco_ios',
        'host': device_ip,
        'username': username,
        'password': password,
    }
    
    connection = ConnectHandler(**device)
    
    checks = {
        'HTTP Disabled': 'show ip http server status',
        'SSH v2 Enabled': 'show ip ssh',
        'SNMP v3 Configured': 'show snmp group',
        'VTY ACL Applied': 'show line vty 0',
        'Logging Configured': 'show logging',
    }
    
    results = []
    for check_name, command in checks.items():
        output = connection.send_command(command)
        
        # Simple compliance check (can be enhanced)
        if 'HTTP server: Disabled' in output and check_name == 'HTTP Disabled':
            status = 'PASS'
        elif 'version 2.0' in output and check_name == 'SSH v2 Enabled':
            status = 'PASS'
        else:
            status = 'FAIL'  # Simplistic check (enhance with proper parsing)
        
        results.append({'Check': check_name, 'Status': status, 'Output': output[:100]})
    
    connection.disconnect()
    return results

# Example usage
devices = ['10.1.0.1', '10.1.0.2', '10.1.0.3']
all_results = []

for device_ip in devices:
    print(f"Checking {device_ip}...")
    results = check_device_compliance(device_ip, 'admin', 'password')
    for result in results:
        result['Device'] = device_ip
    all_results.extend(results)

# Generate report
df = pd.DataFrame(all_results)
df.to_csv('compliance_report.csv', index=False)
print("Report generated: compliance_report.csv")
```

---

# Integration with Other Processes

## Integration with IMP-S1 (Network Discovery)

- Discovered devices → added to hardening queue
- Hardening status tracked per device

## Integration with IMP-S6 (Security Testing)

- Hardened devices → tested via penetration testing
- Vulnerabilities found → remediated via re-hardening

## Integration with Change Management

- Hardening changes → require RFC approval
- Configuration changes → trigger hardening re-validation

---

# Quality Assurance

## Hardening Quality Checklist

- [ ] Hardening baseline documented and approved
- [ ] Pre-hardening backup completed
- [ ] Hardening configuration applied
- [ ] Post-hardening validation passed (compliance scan)
- [ ] Functional testing passed (device still works)
- [ ] Security testing passed (unauthorised access denied)
- [ ] CMDB updated (hardening status, date)
- [ ] Configuration version controlled (Git/RANCID)
- [ ] RFC closed with success notes

---

# Common Pitfalls and Solutions

## Pitfall: Device Becomes Unreachable After Hardening

**Cause**: VTY ACL too restrictive, SSH misconfigured, or management IP changed.

**Solution**:

- Always test SSH access from management network BEFORE disconnecting console
- Keep console cable connected during hardening
- If locked out: Connect via console, remove VTY ACL temporarily, fix issue

## Pitfall: SNMP Monitoring Breaks

**Cause**: SNMPv3 misconfigured, monitoring tool doesn't support SNMPv3.

**Solution**:

- Test SNMPv3 with monitoring tool BEFORE disabling SNMPv2c
- If monitoring tool doesn't support v3: Document as exception, keep v2c with strong community string

## Pitfall: Configuration Drift (Changes Revert)

**Cause**: Changes applied to running-config but not saved to startup-config.

**Solution**:

- Always `write memory` or `copy running-config startup-config` after changes
- Use configuration management tools (RANCID) to detect drift

---

# Documentation Requirements

## Hardening Documentation Artifacts

- [ ] Hardening baseline document (per device type)
- [ ] Pre-hardening device state documentation
- [ ] Hardening configuration script
- [ ] Post-hardening validation report (compliance scan results)
- [ ] Exception documentation (for any baseline deviations)

---

# Continuous Improvement

## Metrics to Track

- **Hardening Coverage**: % of devices hardened (target: 100%)
- **Compliance Score**: Average compliance score across all devices (target: >90%)
- **Patch Timeliness**: Days from patch release to deployment (target: <30 days)

---

# Appendix

## Additional Resources

- CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks/
- Cisco IOS Security Configuration Guide: https://www.cisco.com/c/en/us/support/security/
- NIST SP 800-123: https://csrc.nist.gov/publications/

---

# Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISMS Implementation Team | Initial release |

---

**END OF DOCUMENT**

---

**END OF USER GUIDE**

---

*"A default configuration is a known vulnerability."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
