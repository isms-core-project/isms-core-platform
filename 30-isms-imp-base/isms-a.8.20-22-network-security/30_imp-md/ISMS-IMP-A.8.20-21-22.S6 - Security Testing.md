**ISMS-IMP-A.8.20-21-22-S6 – Network Security Testing**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.20-21-22-S6 |
| **Version** | 1.0 |
| **Assessment Area** | Network Security Controls Testing & Validation |
| **Related Policy** | ISMS-POL-A.8.20-21-22, Section 3.2 (Monitoring & Reporting), Section 3.3 (Exception Management) |
| **Purpose** | Establish comprehensive testing methodologies for validating network security controls including segmentation effectiveness, firewall rules, device hardening, and service security configurations |
| **Target Audience** | Security Engineers, Network Administrators, Penetration Testers, Compliance Officers, ISMS Auditors |
| **Assessment Type** | Security Testing & Validation Assessment |
| **Review Cycle** | Semi-Annually or After Major Security Control Changes |
| **Total Sheets** | 11 |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guidance for network security testing | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** Security assessors, Control owners, Compliance officers

---

# Purpose and Scope

## Purpose

This document provides **practical, step-by-step guidance** for testing and validating network security controls to ensure compliance with **Controls A.8.20 (Networks Security), A.8.21 (Security of Network Services), and A.8.22 (Segregation of Networks)**.

**Network security testing** involves:

- Vulnerability scanning of network devices and services
- Penetration testing to validate security controls
- Segmentation effectiveness testing to verify isolation
- VLAN hopping testing to prevent layer 2 attacks
- Configuration auditing to detect drift and misconfigurations
- Service security testing to validate service hardening
- Continuous validation to maintain security posture


## Scope

This guidance covers:

- **Vulnerability Scanning** - Automated scanning of network devices, services, and configurations
- **Penetration Testing** - Manual testing of network controls, including external and internal testing
- **Segmentation Effectiveness Testing** - Validation of network segmentation and isolation
- **VLAN Hopping Testing** - Testing prevention of layer 2 attacks (double tagging, switch spoofing)
- **Configuration Auditing** - Automated and manual review of network device configurations
- **Network Service Testing** - Testing security of DNS, DHCP, NTP, proxy, and other services
- **Test Documentation** - Recording test procedures, results, and remediation


## Applicability

This guidance is **technology-agnostic** with specific examples for:

- Traditional networks (Cisco, Juniper, HP/Aruba, etc.)
- Software-defined networking (SDN) environments
- Cloud platforms (AWS, Azure, GCP)
- Hybrid and multi-cloud architectures
- Network security appliances (firewalls, IDS/IPS)


## Who Should Use This Guidance

- Security teams conducting network security assessments
- Penetration testers validating network controls
- Network engineers testing segmentation and device hardening
- ISMS implementers preparing for A.8.20/8.21/8.22 assessments
- Auditors verifying network security testing processes


---

# Process Overview

## Network Security Testing Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│           NETWORK SECURITY TESTING PROCESS                       │
└─────────────────────────────────────────────────────────────────┘

Phase 1: Test Planning
├─ Define test scope (which networks, devices, services to test)
├─ Identify test types (vulnerability scan, pentest, seg testing)
├─ Schedule testing windows (off-hours for disruptive tests)
├─ Obtain approvals (change management, stakeholder sign-off)
└─ Prepare test tools and environment

Phase 2: Vulnerability Scanning
├─ Scan network devices (routers, switches, firewalls, APs)
├─ Scan network services (DNS, DHCP, NTP, proxy, etc.)
├─ Scan for configuration issues (weak ciphers, default creds)
├─ Analyze scan results (prioritize critical/high findings)
└─ Generate vulnerability report

Phase 3: Penetration Testing
├─ External penetration testing (internet-facing perimeter)
├─ Internal penetration testing (assume breach scenario)
├─ Lateral movement testing (test segmentation boundaries)
├─ Privilege escalation testing (network device access)
└─ Document findings and recommendations

Phase 4: Segmentation Effectiveness Testing
├─ Inter-zone traffic testing (verify allow/deny policies)
├─ Firewall rule testing (test each rule for effectiveness)
├─ Packet capture verification (analyze traffic flows)
├─ Lateral movement simulation (simulate attacker movement)
└─ Document segmentation gaps

Phase 5: VLAN Hopping Testing
├─ Double tagging attack testing
├─ Switch spoofing (DTP) attack testing
├─ Verify VLAN security controls (native VLAN, DTP disabled)
└─ Document findings

Phase 6: Configuration Auditing
├─ Automated configuration compliance scanning
├─ Manual configuration review (spot checks)
├─ Drift detection (compare running config to baseline)
├─ Identify misconfigurations
└─ Generate compliance report

Phase 7: Network Service Testing
├─ DNS security testing (DNSSEC, DNS filtering, query logging)
├─ DHCP security testing (rogue DHCP detection, snooping)
├─ NTP security testing (authentication, access controls)
├─ Proxy security testing (authentication, SSL inspection)
└─ Document service security gaps

Phase 8: Test Documentation and Remediation
├─ Consolidate test results
├─ Prioritize findings (critical, high, medium, low)
├─ Develop remediation plan
├─ Track remediation progress
└─ Re-test after remediation (validation testing)
```

## Key Principles

**Non-Disruptive Testing**: Prefer passive testing (packet capture, log analysis) over active testing (port scanning) when possible.

**Risk-Based Approach**: Prioritize testing of high-value assets and high-risk areas (internet-facing, sensitive data).

**Realistic Scenarios**: Test real-world attack scenarios (lateral movement, privilege escalation).

**Continuous Testing**: Network security testing is not one-time; schedule regular testing (quarterly, annually).

**Safe Testing**: Use controlled environments (labs) for disruptive tests before production.

---

# Prerequisites and Tools

## Required Access and Permissions

- Network access to devices under test (management interfaces, CLI)
- Approval for testing activities (change management, stakeholder sign-off)
- Credentials for authenticated scanning (SNMP, SSH, API access)
- Test network or lab environment for disruptive tests


## Required Tools

**Vulnerability Scanning**:

- **Nessus** (commercial, comprehensive vulnerability scanner)
- **Qualys** (commercial, cloud-based vulnerability management)
- **OpenVAS** (open-source vulnerability scanner)
- **Nipper** (network device configuration auditor - Cisco, Juniper, etc.)


**Network Discovery and Reconnaissance**:

- **nmap** (open-source port scanner, service detection)
- **Masscan** (fast port scanner for large networks)
- **Shodan** (internet-connected device search engine)


**Penetration Testing**:

- **Metasploit** (open-source exploitation framework)
- **Burp Suite** (web application testing - for network services with web interfaces)
- **Cobalt Strike** (commercial, advanced threat emulation)
- **BloodHound** (Active Directory attack path analysis)


**Layer 2 Attacks (VLAN Hopping)**:

- **Yersinia** (layer 2 attack tool - DTP, DHCP, STP, etc.)
- **Scapy** (packet crafting for custom attacks)


**Traffic Analysis**:

- **Wireshark** (packet capture and analysis)
- **tcpdump** (command-line packet capture)
- **tshark** (command-line Wireshark)


**Configuration Management and Auditing**:

- **RANCID** (Really Awesome New Cisco confIg Differ - config backup and comparison)
- **Ansible** (configuration management, compliance checking)
- **Puppet/Chef** (configuration management)


**Cloud Security Testing**:

- **ScoutSuite** (multi-cloud security auditing tool - AWS, Azure, GCP)
- **Prowler** (AWS security best practices assessment)
- **CloudMapper** (AWS network diagram and security analysis)


**Network Service Testing**:

- **dig** (DNS query tool)
- **nslookup** (DNS query tool)
- **dnsenum** (DNS enumeration)
- **DHCPig** (DHCP exhaustion and testing)


## Required Skills and Knowledge

- Network security fundamentals (TCP/IP, routing, switching, firewalls)
- Vulnerability assessment methodologies (OWASP, PTES, OSSTMM)
- Penetration testing techniques (reconnaissance, exploitation, post-exploitation)
- Layer 2 attack techniques (VLAN hopping, ARP spoofing, etc.)
- Packet analysis (Wireshark, tcpdump)
- Scripting (Python, Bash) for automation


---

# Step-by-Step Procedures

## Phase 1: Test Planning

### Define Test Scope

**Objective**: Clearly define what will be tested and what will not.

**Steps**:

1. **Identify networks in scope**:

   - Production networks (internal, DMZ, management)
   - Development/test networks (if separate)
   - Cloud networks (AWS VPCs, Azure VNets, GCP VPCs)


2. **Identify devices in scope**:

   - Network devices (routers, switches, firewalls, wireless APs)
   - Network security appliances (IDS/IPS, network monitoring)
   - Load balancers, VPN concentrators


3. **Identify services in scope**:

   - DNS, DHCP, NTP, proxy, RADIUS/TACACS+, SNMP, syslog


4. **Identify exclusions** (out of scope):

   - Legacy systems (if can't be safely tested)
   - Third-party managed networks (if no access)
   - Production systems during business hours (if disruptive testing)


**Example Scope Statement**:
```
Scope: All production network devices and services in HQ and Branch Office 1
       AWS production VPC (us-east-1)
       Testing period: January 15-19, 2026 (off-hours: 10 PM - 6 AM)

Out of Scope: Branch Office 2 (third-party managed)
              Legacy Cisco Catalyst 2950 switches (end-of-life, no vendor support)
```

### Identify Test Types

**Select appropriate test types**:

| Test Type | Purpose | Frequency | Risk Level |
|-----------|---------|-----------|------------|
| **Vulnerability Scanning** | Identify known vulnerabilities | Monthly | Low |
| **Configuration Auditing** | Detect misconfigurations and drift | Monthly | Low |
| **External Penetration Testing** | Test perimeter defenses | Annual | Medium |
| **Internal Penetration Testing** | Test internal controls, lateral movement | Annual | Medium |
| **Segmentation Testing** | Verify network isolation | Quarterly | Low |
| **VLAN Hopping Testing** | Test layer 2 attack prevention | Quarterly | Medium |
| **Network Service Testing** | Validate service security | Quarterly | Low |

**Disruptive vs. Non-Disruptive**:

- **Non-Disruptive**: Vulnerability scanning (read-only), configuration auditing, packet capture
- **Disruptive**: Penetration testing (active exploitation), VLAN hopping attacks, DoS testing


**Risk Management**: For disruptive tests, use test/lab environments when possible.

### Obtain Approvals

**Required Approvals**:

1. **Change Management**: Submit change request (even for read-only testing)
2. **Stakeholder Sign-Off**: Get approval from:

   - Network team (may need to assist with testing)
   - Security team (oversight)
   - IT management (aware of testing activities)
   - Business stakeholders (if testing affects business systems)

3. **Legal/Compliance** (for penetration testing): Confirm testing is authorized

**Example Change Request**:
```
Change Request: Network Security Vulnerability Scan
Date: January 10, 2026
Requester: Security Team
Scope: All production network devices
Risk Level: Low (read-only scanning)
Schedule: January 15, 2026, 10 PM - 2 AM
Approvers: Network Manager, CISO
```

---

## Phase 2: Vulnerability Scanning

### Network Device Vulnerability Scanning

**Objective**: Identify known vulnerabilities in network devices (routers, switches, firewalls).

**Tools**: Nessus, Qualys, OpenVAS

**Nessus Example** (authenticated scan):

**Step 1: Create Scan Policy**

1. Log in to Nessus web interface
2. Navigate to **Policies** → **New Policy**
3. Select **Advanced Scan** policy
4. Configure settings:

   - **Name**: Network Device Vulnerability Scan
   - **Targets**: [List of device IP addresses or subnets]
   - **Credentials**: Add SSH credentials for authenticated scanning
   - **Plugins**: Enable all plugins (or focus on network device plugins)

5. Save policy

**Step 2: Launch Scan**

1. Navigate to **Scans** → **New Scan**
2. Select policy: **Network Device Vulnerability Scan**
3. Enter targets (IP ranges, subnets, or individual IPs):
   ```
   10.1.10.1-10.1.10.254   # DMZ devices
   10.1.20.1-10.1.20.254   # Internal devices
   10.1.40.1-10.1.40.254   # Management devices
   ```
4. Schedule scan (e.g., January 15, 2026, 10 PM)
5. Launch scan

**Step 3: Analyze Results**

After scan completes:

1. Review **Summary** tab:

   - Total vulnerabilities: [number]
   - Critical: [number]
   - High: [number]
   - Medium: [number]
   - Low: [number]
   - Info: [number]


2. Review **Vulnerabilities** tab:

   - Sort by **Severity** (Critical first)
   - Review each vulnerability:
     - CVE ID (e.g., CVE-2023-20198)
     - CVSS Score (e.g., 9.8 Critical)
     - Affected hosts
     - Solution (patch, workaround)


3. Prioritize remediation:

   - **Critical**: Immediate action (within 24-48 hours)
   - **High**: Urgent action (within 7 days)
   - **Medium**: Scheduled action (within 30 days)
   - **Low**: Tracked for future remediation


**Step 4: Generate Report**

1. Navigate to **Reports** → **Generate Report**
2. Select report type: **Executive Summary** or **Technical Report**
3. Export as PDF or CSV
4. Distribute to stakeholders (network team, security team, management)

**Example Vulnerability Report Summary**:
```
Network Device Vulnerability Scan Report
Date: January 16, 2026
Scan Duration: 4 hours
Devices Scanned: 45

Findings:

- Critical: 2 (outdated firmware on 2 routers - CVE-2023-XXXXX)
- High: 8 (weak SNMP community strings, default credentials on 3 switches)
- Medium: 15 (SSH protocol v1 enabled, weak SSL ciphers)
- Low: 22 (banner message missing, unnecessary services enabled)


Recommended Actions:
1. Upgrade firmware on routers (Critical priority)
2. Change SNMP community strings to strong values (High priority)
3. Disable default credentials and create unique admin accounts (High priority)
```

### Configuration Vulnerability Scanning

**Objective**: Identify configuration issues (weak ciphers, default credentials, unnecessary services).

**Tools**: Nipper, Nessus Policy Compliance scanning

**Nipper Example** (Cisco configuration audit):

**Step 1: Export Device Configuration**

```bash
# SSH to Cisco device and export config
ssh admin@10.1.10.1
show running-config > /tmp/router-config.txt
exit

# Copy config to local machine
scp admin@10.1.10.1:/tmp/router-config.txt .
```

**Step 2: Run Nipper**

```bash
# Install Nipper (if not already installed)
# Nipper is commercial software; trial version available

# Run Nipper on config file
nipper --ios --input=router-config.txt --output=router-audit-report.html

# Nipper analyzes config and generates HTML report
```

**Step 3: Review Report**

Open `router-audit-report.html` in browser:

- **Security Audit**: Lists configuration issues
  - Weak passwords (if detectable)
  - Unnecessary services (HTTP server enabled, CDP enabled, etc.)
  - Weak encryption (SSH v1, weak SSL ciphers)
  - Access control issues (overly permissive ACLs)
  
- **Recommendations**: Specific config commands to fix issues


**Example Nipper Findings**:
```
Finding: HTTP server enabled (insecure management interface)
Severity: High
Recommendation: Disable HTTP, use HTTPS only
  no ip http server
  ip http secure-server

Finding: CDP enabled on all interfaces (information disclosure)
Severity: Medium
Recommendation: Disable CDP on external-facing interfaces
  interface GigabitEthernet0/0
   no cdp enable
```

### Vulnerability Scan Automation

**Automate regular scans** using Nessus API or command-line tools.

**Example: Automated Weekly Scan (Python + Nessus API)**

```python
#!/usr/bin/env python3
"""
Automated Nessus vulnerability scan
Scans network devices weekly and emails report
"""

import requests
import json
from datetime import datetime

# Nessus API configuration
NESSUS_URL = "https://nessus.example.com:8834"
API_KEY = "your-api-key"
SECRET_KEY = "your-secret-key"

headers = {
    "X-ApiKeys": f"accessKey={API_KEY}; secretKey={SECRET_KEY}",
    "Content-Type": "application/json"
}

# Launch scan
def launch_scan(scan_id):
    url = f"{NESSUS_URL}/scans/{scan_id}/launch"
    response = requests.post(url, headers=headers, verify=False)
    if response.status_code == 200:
        print(f"Scan {scan_id} launched successfully")
    else:
        print(f"Error launching scan: {response.status_code}")

# Check scan status
def check_scan_status(scan_id):
    url = f"{NESSUS_URL}/scans/{scan_id}"
    response = requests.get(url, headers=headers, verify=False)
    data = response.json()
    return data['info']['status']

# Export scan results
def export_scan(scan_id):
    url = f"{NESSUS_URL}/scans/{scan_id}/export"
    data = {"format": "pdf"}
    response = requests.post(url, headers=headers, json=data, verify=False)
    file_id = response.json()['file']
    
    # Download exported file
    url = f"{NESSUS_URL}/scans/{scan_id}/export/{file_id}/download"
    response = requests.get(url, headers=headers, verify=False)
    
    filename = f"nessus-report-{datetime.now().strftime('%Y-%m-%d')}.pdf"
    with open(filename, 'wb') as f:
        f.write(response.content)
    
    print(f"Report exported: {filename}")
    return filename

# Main
if __name__ == "__main__":
    SCAN_ID = 123  # Replace with your scan ID
    
    # Launch scan
    launch_scan(SCAN_ID)
    
    # Wait for scan to complete (check every 5 minutes)
    import time
    while True:
        status = check_scan_status(SCAN_ID)
        print(f"Scan status: {status}")
        if status == "completed":
            break
        time.sleep(300)  # Wait 5 minutes
    
    # Export and email report
    report_file = export_scan(SCAN_ID)
    # Implementation: Add email notification to security team
```

---

## Phase 3: Penetration Testing

### External Penetration Testing

**Objective**: Test perimeter defenses (internet-facing systems).

**Methodology**: OWASP Testing Guide, PTES (Penetration Testing Execution Standard)

**Phases**:

1. **Reconnaissance**: Gather information about target (IP ranges, domain names, services)
2. **Scanning**: Identify open ports, services, versions
3. **Exploitation**: Attempt to exploit vulnerabilities
4. **Post-Exploitation**: Access internal network (if perimeter breached)
5. **Reporting**: Document findings and recommendations

**Example: External Perimeter Test**

**Phase 1: Reconnaissance**

```bash
# DNS reconnaissance (find subdomains, IP addresses)
dig example.com ANY
nslookup -type=ANY example.com

# WHOIS lookup (organization info, IP ranges)
whois example.com

# Shodan search (internet-facing devices)
# Visit: shodan.io
# Search: org:"Example Corp"
# Identify exposed devices (routers, firewalls, cameras, etc.)
```

**Phase 2: Port Scanning**

```bash
# TCP SYN scan (stealth scan) of perimeter
sudo nmap -sS -p- -T4 -v 203.0.113.0/24

# Service version detection
sudo nmap -sV -p22,80,443 203.0.113.0/24

# OS detection
sudo nmap -O 203.0.113.0/24

# Example output:
# 203.0.113.10:
#   22/tcp open  ssh     OpenSSH 7.4 (protocol 2.0)
#   443/tcp open https   nginx 1.18.0
#   OS: Linux 3.X
```

**Phase 3: Vulnerability Assessment**

```bash
# NSE (Nmap Scripting Engine) vulnerability scan
sudo nmap --script vuln 203.0.113.10

# Test for common vulnerabilities:
# - SSL/TLS issues (weak ciphers, expired certs)
# - SSH vulnerabilities
# - Web server vulnerabilities
```

**Phase 4: Exploitation** (Controlled Environment)

**Example: SSH brute force (to test password policy)**

```bash
# Use Metasploit for SSH brute force
msfconsole
use auxiliary/scanner/ssh/ssh_login
set RHOSTS 203.0.113.10
set USERNAME admin
set PASS_FILE /usr/share/wordlists/rockyou.txt
set THREADS 5
run

# Expected: Brute force should FAIL (strong password policy prevents)
# If successful: CRITICAL finding (weak password)
```

**Phase 5: Report Findings**

Example Finding:
```
Finding: SSH Accessible from Internet (Port 22)
Severity: High
Description: SSH service is accessible from the internet on 203.0.113.10.
             While SSH is encrypted, it may be subject to brute force attacks.
Risk: Brute force attacks, credential stuffing
Recommendation: 
  1. Restrict SSH access to VPN or trusted IPs (firewall rule)
  2. Implement SSH key-based authentication (disable password auth)
  3. Enable fail2ban (automatic IP blocking after failed attempts)
  4. Use non-standard SSH port (security through obscurity - minor benefit)
```

### Internal Penetration Testing

**Objective**: Test internal controls, simulate lateral movement after initial compromise.

**Assumption**: Attacker has initial foothold (compromised workstation).

**Methodology**:

1. **Initial Access**: Assume attacker has access to internal workstation
2. **Reconnaissance**: Scan internal network (identify targets)
3. **Lateral Movement**: Attempt to move to other zones (test segmentation)
4. **Privilege Escalation**: Attempt to gain administrative access to network devices
5. **Data Exfiltration**: Attempt to access sensitive data (databases, file servers)
6. **Persistence**: Attempt to maintain access (backdoors, scheduled tasks)
7. **Reporting**: Document attack paths and segmentation gaps

**Example: Internal Pentest Scenario**

**Phase 1: Internal Reconnaissance**

```bash
# From compromised workstation (10.1.30.50 - Internal zone)
# Scan internal network
nmap -sn 10.1.0.0/16
# Identify live hosts (servers, network devices)

# Scan for interesting services
nmap -p- -T4 10.1.20.0/24
# Identify databases (3306, 5432), file shares (445), admin interfaces (22, 3389)
```

**Phase 2: Test Segmentation (Lateral Movement)**

```bash
# Attempt to access Management zone (should be DENIED)
telnet 10.1.40.10 22
# Expected: Connection timeout or refused (firewall blocks)

# Attempt to access DMZ zone (should be DENIED)
curl http://10.1.10.10
# Expected: Connection timeout (firewall blocks Internal → DMZ)

# Verify firewall logs show denied attempts
```

**Phase 3: Privilege Escalation**

```bash
# Attempt to access network device (router)
telnet 10.1.20.1 23
# Try default credentials: admin/admin, cisco/cisco, etc.
# Expected: Authentication fails (strong password policy, unique credentials)

# Attempt SSH with common credentials
ssh admin@10.1.20.1
# Password: [try common passwords]
# Expected: Authentication fails
```

**Phase 4: Data Exfiltration Test**

```bash
# Attempt to access database (if accessible from workstation)
mysql -h 10.1.20.50 -u root -p
# Try common passwords: root, password, admin, etc.
# Expected: Authentication fails (strong DB password, firewall rules limit access)

# If accessible: Attempt to query sensitive data
# Check if data is encrypted (verify encryption in transit and at rest)
```

**Phase 5: Report Findings**

Example Finding:
```
Finding: Lateral Movement Blocked by Segmentation
Severity: Pass (Control Working)
Description: From compromised workstation in Internal zone, attempts to access
             Management zone (10.1.40.0/24) were blocked by firewall.
Evidence: tcpdump capture shows SYN packets sent to 10.1.40.10:22, but no SYN-ACK
          received (firewall dropped packets). Firewall logs show denied traffic.
Conclusion: Segmentation is effective. Lateral movement is prevented.
```

Example Finding (Gap):
```
Finding: Database Accessible from All Internal Workstations
Severity: High
Description: Database server (10.1.20.50:3306) is accessible from all workstations
             in Internal zone. Only web servers (10.1.10.0/24) should access DB.
Risk: Compromised workstation can access database directly (SQL injection, data theft)
Recommendation: Implement firewall rule to restrict DB access:

  - Allow: 10.1.10.0/24 (web servers) → 10.1.20.50:3306
  - Deny: 10.1.30.0/22 (workstations) → 10.1.20.50:3306

```

---

## Phase 4: Segmentation Effectiveness Testing

### Inter-Zone Traffic Testing

**Objective**: Verify firewall rules allow authorized traffic and block unauthorized traffic.

**Procedure**:

1. **Identify inter-zone traffic policies** (from Segmentation Matrix - WB4)
2. **Test allowed traffic** (should succeed)
3. **Test denied traffic** (should fail)
4. **Verify firewall logs** (denied traffic logged)

**Example Test Cases**:

| Test ID | Source Zone | Source IP | Dest Zone | Dest IP | Protocol/Port | Expected Result |
|---------|-------------|-----------|-----------|---------|---------------|-----------------|
| TC-001 | Internal | 10.1.30.50 | Internet | 8.8.8.8 | UDP/53 (DNS) | ALLOW |
| TC-002 | Internal | 10.1.30.50 | DMZ | 10.1.10.10 | TCP/443 (HTTPS) | ALLOW |
| TC-003 | Internal | 10.1.30.50 | Management | 10.1.40.10 | TCP/22 (SSH) | DENY |
| TC-004 | DMZ | 10.1.10.10 | Internal | 10.1.20.50 | TCP/3306 (MySQL) | ALLOW |
| TC-005 | DMZ | 10.1.10.10 | Internet | 0.0.0.0/0 | Any | ALLOW (outbound) |
| TC-006 | Guest | 10.1.50.50 | Internal | 10.1.20.0/24 | Any | DENY |

**Test Execution**:

**TC-001: Internal → Internet (DNS) - ALLOW**
```bash
# From workstation 10.1.30.50
dig @8.8.8.8 example.com

# Expected: DNS response received (success)
```

**TC-003: Internal → Management (SSH) - DENY**
```bash
# From workstation 10.1.30.50
telnet 10.1.40.10 22

# Expected: Connection timeout (firewall blocks)
# Verify in firewall logs: denied connection logged
```

**TC-004: DMZ → Internal (MySQL) - ALLOW**
```bash
# From web server 10.1.10.10
mysql -h 10.1.20.50 -u webapp -p

# Expected: Connection successful, can query database
```

**TC-006: Guest → Internal (Any) - DENY**
```bash
# From guest device 10.1.50.50
ping 10.1.20.50

# Expected: No ping response (firewall blocks ICMP)

telnet 10.1.20.50 445

# Expected: Connection timeout (firewall blocks SMB)
```

### Packet Capture Verification

**Objective**: Capture traffic at zone boundaries and verify only authorized traffic flows.

**Procedure**:

1. **Capture traffic** at firewall or router interface
2. **Analyze captured traffic** (Wireshark, tcpdump)
3. **Verify traffic matches firewall rules** (only authorized traffic passes)

**Example: Capture DMZ → Internal Traffic**

```bash
# On firewall or router, capture traffic between DMZ and Internal
sudo tcpdump -i eth0 -n 'src net 10.1.10.0/24 and dst net 10.1.20.0/24' -w dmz-internal.pcap -v

# Let capture run for 5-10 minutes (or during business hours)
# Stop capture (Ctrl+C)

# Analyze capture
tcpdump -r dmz-internal.pcap -n

# Example output:
# 10:15:30.123456 IP 10.1.10.10.54321 > 10.1.20.50.3306: Flags [S], seq 12345
# 10:15:30.123789 IP 10.1.20.50.3306 > 10.1.10.10.54321: Flags [S.], seq 67890, ack 12346
# (MySQL traffic between web server and database)

# Verify:
# - Traffic is TCP/3306 (MySQL) - matches firewall rule
# - No other protocols/ports (e.g., no SSH, RDP, ICMP)
# - Source IPs are web servers (10.1.10.0/24)
# - Destination IPs are database servers (10.1.20.50)
```

**Wireshark Analysis**:
1. Open `dmz-internal.pcap` in Wireshark
2. Apply display filter: `ip.src == 10.1.10.0/24 && ip.dst == 10.1.20.0/24`
3. View **Statistics → Protocol Hierarchy** - verify only authorized protocols
4. View **Statistics → Conversations** - verify authorized IP pairs only

---

## Phase 5: VLAN Hopping Testing

### Double Tagging Attack Testing

**Objective**: Verify prevention of VLAN hopping via double tagging.

**Attack Explanation**:

- Attacker sends double-tagged 802.1Q frame (outer tag = native VLAN, inner tag = target VLAN)
- If native VLAN = VLAN 1 (default), outer tag is stripped by first switch, inner tag is processed by second switch
- Attacker can access target VLAN without authorization


**Prevention** (implemented in ISMS-IMP-A.8.20-21-22-S5):

- Change native VLAN to unused VLAN (not VLAN 1)


**Testing Procedure**:

```bash
# Use Scapy to craft double-tagged frame
sudo scapy

>>> from scapy.all import *

# Craft double-tagged frame
# Outer tag: VLAN 1 (native VLAN), Inner tag: VLAN 20 (Servers)
>>> packet = Ether()/Dot1Q(vlan=1)/Dot1Q(vlan=20)/IP(dst="10.1.20.50")/ICMP()

# Send packet
>>> sendp(packet, iface="eth0")

# Monitor destination (10.1.20.50) for ICMP packet
# Expected: ICMP packet NOT received (attack failed)
# Reason: Native VLAN changed from 1 to 999; double tagging fails
```

**Verification**:

- **If attack fails**: Native VLAN is NOT VLAN 1 → Control working
- **If attack succeeds**: Native VLAN is still VLAN 1 → CRITICAL vulnerability, change native VLAN immediately


### Switch Spoofing (DTP) Attack Testing

**Objective**: Verify prevention of VLAN hopping via DTP (Dynamic Trunking Protocol).

**Attack Explanation**:

- Attacker sends DTP packets to negotiate trunk with switch
- If DTP enabled and switch accepts, attacker gains access to all VLANs


**Prevention** (implemented in ISMS-IMP-A.8.20-21-22-S5):

- Disable DTP (`switchport nonegotiate`)
- Hardcode switchport mode (`switchport mode access` or `switchport mode trunk`)


**Testing Procedure**:

```bash
# Use Yersinia to attempt DTP negotiation
sudo yersinia -G   # Launch GUI

# In Yersinia GUI:
# Select "DTP" attack
# Click "Attack" → "Enabling trunking"
# Select interface (e.g., eth0)
# Launch attack

# Monitor switch logs for DTP messages
# Expected: Switch REJECTS DTP negotiation (DTP disabled)
# Reason: switchport nonegotiate configured on all ports
```

**Verification**:

- **If attack fails**: DTP disabled → Control working
- **If attack succeeds**: DTP still enabled → HIGH vulnerability, disable DTP immediately


---

## Phase 6: Configuration Auditing

### Automated Configuration Compliance Scanning

**Objective**: Verify device configurations match hardening baselines.

**Tools**: Nessus Policy Compliance, Ansible

**Nessus Policy Compliance Example**:

**Step 1: Create Compliance Policy**

1. Navigate to **Policies** → **Policy Compliance Auditing**
2. Select **Cisco IOS Compliance Audit** template
3. Configure:

   - **Policy Name**: Cisco Router Hardening Compliance
   - **Audit File**: Upload custom audit file (defines checks)
   - **Credentials**: Add SSH credentials


**Example Audit File** (Nessus .audit format):
```
<check_type:"Unix">
<group_title:"Cisco IOS Hardening Baseline">

<custom_item>
  type: CMD_EXEC
  description: "Verify HTTP server is disabled"
  cmd: "show running-config | include ip http server"
  expect: "no ip http server"
</custom_item>

<custom_item>
  type: CMD_EXEC
  description: "Verify SSH version 2 only"
  cmd: "show ip ssh"
  regex: "SSH Enabled.*version 2"
</custom_item>

<custom_item>
  type: CMD_EXEC
  description: "Verify banner message configured"
  cmd: "show running-config | section banner"
  expect: "banner"
</custom_item>
```

**Step 2: Run Compliance Scan**

1. Launch scan with compliance policy
2. Scan completes → Review results

**Step 3: Review Compliance Results**

Nessus reports compliance status per check:

- **PASSED**: Configuration matches baseline
- **FAILED**: Configuration does not match baseline (gap identified)


Example Output:
```
Compliance Scan Results: Cisco Router 10.1.10.1

PASSED: HTTP server disabled
FAILED: SSH version 2 only (SSH v1 still enabled)
FAILED: Banner message configured (no banner configured)
PASSED: SNMP v3 only (v1/v2c disabled)
```

### Configuration Drift Detection

**Objective**: Detect changes to configurations over time (unauthorized changes).

**Tools**: RANCID, Git, Ansible

**RANCID Example** (Really Awesome New Cisco confIg Differ):

**Step 1: Install RANCID**

```bash
# Install RANCID (on Ubuntu/Debian)
sudo apt-get install rancid

# Configure RANCID
sudo vi /etc/rancid/rancid.conf
# Set: LIST_OF_GROUPS="network-devices"
```

**Step 2: Add Devices to RANCID**

```bash
# Create router.db file (list of devices)
sudo vi /var/lib/rancid/network-devices/router.db

# Add devices (one per line):
10.1.10.1:cisco:up
10.1.20.1:cisco:up
10.1.40.1:cisco:up
```

**Step 3: Configure Credentials**

```bash
# Create .cloginrc file (credentials)
sudo vi /var/lib/rancid/.cloginrc

add user * admin
add password * {strong-password}
add method * ssh
```

**Step 4: Run RANCID**

```bash
# Run initial backup
sudo -u rancid /usr/lib/rancid/bin/rancid-run

# RANCID connects to devices, downloads configs, stores in CVS/Git
# Subsequent runs detect config changes
```

**Step 5: Review Changes**

```bash
# View change log
sudo cat /var/lib/rancid/network-devices/logs/network-devices.YYYYMMDD.log

# Example output:
# Config changed: 10.1.10.1
# - interface GigabitEthernet0/1
# -  description Server-DB01
# +  description Server-DB01-Production
```

**Alerting**: Configure RANCID to email on config changes.

---

## Phase 7: Network Service Testing

### DNS Security Testing

**Test 1: DNSSEC Validation**

```bash
# Test if DNSSEC is enabled and working
dig @10.1.10.5 example.com +dnssec

# Look for:
# - RRSIG records (DNSSEC signatures)
# - ad flag (authenticated data)

# If DNSSEC working:
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1
```

**Test 2: DNS Filtering (Malicious Domain Blocking)**

```bash
# Test if DNS filtering blocks known malicious domains
dig @10.1.10.5 malware.example.com

# Expected: NXDOMAIN or redirect to block page (DNS filtering active)
# If resolved: DNS filtering may not be working
```

**Test 3: DNS Query Logging**

```bash
# Verify DNS query logs are enabled
# SSH to DNS server
ssh admin@10.1.10.5

# Check DNS logs
tail -f /var/log/named/query.log

# Expected: DNS queries logged (source IP, query, timestamp)
```

### DHCP Security Testing

**Test 1: Rogue DHCP Detection**

```bash
# Attempt to run rogue DHCP server (from attacker workstation)
sudo dhcpd -cf /tmp/rogue-dhcp.conf eth0

# Monitor network for DHCP snooping alerts
# Expected: DHCP snooping detects rogue server, blocks DHCP offers from unauthorized source

# Verify DHCP snooping is working:
# SSH to switch
show ip dhcp snooping
# Look for: DHCP snooping enabled, trusted ports configured
```

**Test 2: DHCP Exhaustion**

```bash
# Use DHCPig to exhaust DHCP scope (DoS test)
sudo dhcpig --interface eth0 --count 100

# Expected: DHCP server has rate limiting, blocks excessive requests
# If successful (all IPs exhausted): Implement rate limiting, increase scope size
```

### NTP Security Testing

**Test 1: NTP Authentication**

```bash
# Attempt to query NTP without authentication
ntpq -c peers 10.1.10.6

# Expected: Query blocked (authentication required)
# If successful without auth: NTP authentication NOT enabled (gap)
```

**Test 2: Time Synchronization**

```bash
# Verify system time is synchronized with NTP
ntpstat

# Expected: synchronised to NTP server 10.1.10.6 at stratum 2
```

### Proxy Security Testing

**Test 1: Proxy Bypass Attempt**

```bash
# Attempt to access internet directly (bypass proxy)
curl http://example.com

# Expected: Connection fails (firewall blocks direct internet access, forces proxy)
# If successful: Proxy bypass possible (implement firewall rules to force proxy)
```

**Test 2: SSL Interception Verification**

```bash
# Access HTTPS site through proxy
curl https://example.com --proxy http://10.1.10.7:3128

# Check SSL certificate
curl -v https://example.com --proxy http://10.1.10.7:3128 2>&1 | grep "issuer"

# Expected: Certificate issuer is proxy CA (SSL inspection working)
# Example: issuer: CN=Example-Proxy-CA
```

---

## Phase 8: Test Documentation and Remediation

### Consolidate Test Results

**Create Master Test Report**:

```
Network Security Testing Report
Test Period: January 15-19, 2026
Tester: Security Team
Scope: HQ Network (10.1.0.0/16), AWS VPC (10.100.0.0/16)

Summary:

- Vulnerability Scan: 45 devices scanned, 27 findings (2 critical, 8 high)
- Penetration Test: 5 findings (1 critical, 2 high, 2 medium)
- Segmentation Test: PASSED (segmentation effective, no lateral movement)
- VLAN Hopping Test: PASSED (double tagging failed, DTP negotiation failed)
- Configuration Audit: 15 devices audited, 10 gaps identified
- Service Testing: 5 services tested, 2 gaps (DNS filtering, DHCP rate limiting)


Critical Findings:
1. Outdated firmware on 2 routers (CVE-2023-XXXXX) - Remote code execution
2. Database accessible from all workstations (should be restricted to web servers)

High Findings:
1. Default credentials on 3 switches (admin/admin)
2. SSH v1 enabled on 5 devices (should be v2 only)
3. HTTP management interface enabled on 4 devices (should be HTTPS only)
...

Recommendations:
1. Upgrade router firmware immediately (Critical)
2. Implement firewall rule to restrict database access (Critical)
3. Change default credentials on switches (High)
4. Disable SSH v1 on all devices (High)
...
```

### Prioritize Findings

**Severity Matrix**:

| Severity | Criteria | Remediation Timeframe |
|----------|----------|------------------------|
| **Critical** | Remote code execution, default credentials, unencrypted sensitive data | Immediate (24-48 hours) |
| **High** | Weak authentication, unnecessary services, segmentation gaps | Urgent (7 days) |
| **Medium** | Configuration issues, missing logging, weak encryption | Scheduled (30 days) |
| **Low** | Informational, best practices | Tracked for future (90 days) |

### Develop Remediation Plan

**For Each Finding**:

1. **Assign Owner**: Who is responsible for remediation?
2. **Develop Fix**: What actions are required?
3. **Schedule Fix**: When will it be done?
4. **Track Progress**: Is remediation on schedule?
5. **Validate Fix**: Re-test after remediation

**Example Remediation Plan**:

| Finding ID | Severity | Description | Owner | Fix | Target Date | Status |
|------------|----------|-------------|-------|-----|-------------|--------|
| VULN-001 | Critical | Outdated firmware on routers | Network Team | Upgrade firmware to latest version | Jan 20, 2026 | In Progress |
| VULN-002 | Critical | Database accessible from all workstations | Security Team | Implement firewall rule to restrict DB access | Jan 22, 2026 | Open |
| VULN-003 | High | Default credentials on switches | Network Team | Change credentials, document new passwords | Jan 25, 2026 | Open |

### Re-Test After Remediation

**Validation Testing**:

After remediation, re-test to verify fix:

```bash
# Example: Verify router firmware upgraded
ssh admin@10.1.10.1
show version
# Expected: Firmware version = latest (e.g., 16.12.05)

# Example: Verify database access restricted
# From workstation (should fail)
telnet 10.1.20.50 3306
# Expected: Connection timeout (firewall blocks)

# From web server (should succeed)
mysql -h 10.1.20.50 -u webapp -p
# Expected: Connection successful
```

---

# Automation Opportunities

## Automated Vulnerability Scanning

**Schedule regular scans** using cron or Task Scheduler.

```bash
# Cron job to run Nessus scan weekly (Sundays at 2 AM)

0 2 * * 0 /usr/local/bin/run-nessus-scan.sh


# run-nessus-scan.sh:
#!/bin/bash
python3 /opt/scripts/nessus_scan.py
mail -s "Weekly Vulnerability Scan Complete" security@example.com < /tmp/scan-summary.txt
```

## Continuous Configuration Monitoring

**RANCID** + **Git** + **Webhooks** = Real-time config change notifications.

```bash
# Configure RANCID to push to Git repo
# Configure Git webhook to notify security team on commits
# Result: Immediate notification when network config changes
```

## Automated Compliance Reporting

**Python script** to consolidate test results and generate compliance report.

```python
#!/usr/bin/env python3
"""
Generate network security compliance report
Consolidates vulnerability scan, pentest, segmentation test results
"""

import json
from datetime import datetime

# Load test results (JSON files from various tools)
with open('vuln-scan-results.json') as f:
    vuln_results = json.load(f)

with open('pentest-results.json') as f:
    pentest_results = json.load(f)

with open('segmentation-test-results.json') as f:
    seg_results = json.load(f)

# Calculate compliance scores
total_findings = len(vuln_results) + len(pentest_results)
critical_findings = sum(1 for f in vuln_results if f['severity'] == 'Critical')
high_findings = sum(1 for f in vuln_results if f['severity'] == 'High')

# Generate report
report = f"""
Network Security Compliance Report
Date: {datetime.now().strftime('%Y-%m-%d')}

Overall Compliance: {"PASS" if critical_findings == 0 else "FAIL"}

Findings Summary:

- Total Findings: {total_findings}
- Critical: {critical_findings}
- High: {high_findings}


Segmentation Status: {"PASS" if seg_results['status'] == 'pass' else "FAIL"}
"""

print(report)

# Email report to stakeholders
# Implementation: Add email sending functionality
```

---

# Integration with Other Processes

## Vulnerability Management (A.8.8)

**Integration**: Network security testing findings feed into vulnerability management process.

- Vulnerability scan results → vulnerability tracking system (Jira, ServiceNow)
- Track remediation progress
- Re-scan to verify fixes


## Incident Response (A.6.8)

**Integration**: Testing may uncover security incidents (e.g., rogue devices, unauthorized changes).

- If testing finds compromised device → trigger incident response
- Penetration testing simulates real attacks → informs incident response playbooks


## Change Management (A.8.32)

**Integration**: Configuration auditing detects unauthorized changes.

- Unexpected config changes → investigate (authorized change or security incident?)
- Configuration drift → submit change request to bring back to baseline


## Logging and Monitoring (A.8.15, A.8.16)

**Integration**: Testing validates logging and monitoring effectiveness.

- Verify firewall logs capture denied traffic
- Verify SIEM alerts on suspicious network activity
- Testing generates test data for SIEM tuning


---

# Quality Assurance

## Testing Quality Checks

- [ ] Test plan approved by stakeholders
- [ ] Test scope clearly defined (inclusions and exclusions)
- [ ] Test tools validated (ensure tools work as expected)
- [ ] Credentials configured (authenticated scanning where possible)
- [ ] Test environment prepared (if using lab for disruptive tests)
- [ ] Backup configurations before testing (rollback if issues occur)
- [ ] Testing completed within scheduled window
- [ ] Test results documented (findings, evidence, recommendations)
- [ ] Findings prioritized (severity-based)
- [ ] Remediation plan developed (owner, timeline, validation)
- [ ] Test report distributed to stakeholders


---

# Common Pitfalls and Solutions

## Testing Mistakes

**Mistake 1: Testing Production During Business Hours**

- **Problem**: Disruptive testing (port scanning, exploitation) affects business
- **Solution**: Schedule testing during off-hours (nights, weekends)


**Mistake 2: No Test Plan**

- **Problem**: Ad-hoc testing, missing scope, stakeholders unaware
- **Solution**: Always create test plan, get approvals


**Mistake 3: Not Validating Fixes**

- **Problem**: Assume fix worked, but vulnerability still present
- **Solution**: Always re-test after remediation


**Mistake 4: Over-Reliance on Automated Scanning**

- **Problem**: Scanners miss complex issues (logic flaws, custom configs)
- **Solution**: Combine automated + manual testing


## False Positives

**Issue**: Vulnerability scanner reports vulnerability, but it's not exploitable (false positive).

**Solution**:

- Manually verify findings (attempt exploitation)
- Mark false positives in scanner (so they're not reported again)
- Tune scanner settings (reduce false positive rate)


---

# Documentation Requirements

## Test Plan Documentation

- Test scope (what will be tested)
- Test methodology (what types of tests)
- Test schedule (when testing will occur)
- Test approvals (who approved testing)


## Test Results Documentation

- Test execution log (what was done, when, by whom)
- Findings (vulnerabilities, gaps, observations)
- Evidence (screenshots, packet captures, logs)
- Recommendations (how to fix findings)


## Remediation Documentation

- Remediation plan (owner, timeline, status)
- Remediation evidence (configs after fix, re-test results)
- Lessons learned (what went wrong, how to improve)


---

# Continuous Improvement

## Periodic Testing Schedule

- **Monthly**: Vulnerability scanning, configuration auditing
- **Quarterly**: Segmentation testing, VLAN hopping testing, service testing
- **Annual**: Full penetration testing (external + internal)


## Metrics to Track

- **Vulnerability Trends**: Are vulnerabilities decreasing over time?
- **Mean Time to Remediate (MTTR)**: How long to fix findings?
- **Critical/High Findings**: Count of severe findings (goal: 0)
- **Segmentation Effectiveness**: Percentage of successful lateral movement tests (goal: 0%)
- **Configuration Drift**: Count of unauthorized config changes (goal: 0)


## Testing Process Improvement

After each testing cycle:

- Review testing procedures (what went well, what didn't)
- Update test plan based on lessons learned
- Tune tools (reduce false positives, improve coverage)
- Train team (new techniques, tools)


---

# Annexes

## Annex A: Network Security Testing Checklist

[See detailed checklist in ISMS-IMP-A.8.20-21-22-S5 Annex C]

## Annex B: Common Vulnerabilities and Exploits

**Common Network Device Vulnerabilities**:
1. Default credentials (admin/admin, cisco/cisco)
2. Outdated firmware (unpatched CVEs)
3. Weak encryption (SSH v1, weak SSL ciphers)
4. Unnecessary services (HTTP, Telnet, CDP, LLDP on external interfaces)
5. Weak SNMP community strings (public/private)

**Common Exploitation Techniques**:
1. SSH brute force (Hydra, Metasploit)
2. SNMP enumeration (snmpwalk, snmp-check)
3. Firewall rule bypass (packet fragmentation, IP spoofing)
4. VLAN hopping (double tagging, DTP negotiation)
5. ARP spoofing (man-in-the-middle on flat networks)

## Annex C: Testing Tools Comparison

| Tool | Type | Cost | Strengths | Weaknesses |
|------|------|------|-----------|------------|
| Nessus | Vuln Scanner | Commercial | Comprehensive, accurate | Expensive |
| OpenVAS | Vuln Scanner | Free | Open-source, no cost | Slower, fewer plugins |
| nmap | Port Scanner | Free | Fast, versatile | Not a full vuln scanner |
| Metasploit | Pentest | Free/Commercial | Exploitation framework | Requires expertise |
| Nipper | Config Auditor | Commercial | Network device-specific | Limited to certain vendors |

---

# Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISMS Implementation Team | Initial release |

---

**END OF DOCUMENT**

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

# Purpose and Scope

## Purpose

This document provides **practical, step-by-step guidance** for testing and validating network security controls to ensure compliance with **Controls A.8.20 (Networks Security), A.8.21 (Security of Network Services), and A.8.22 (Segregation of Networks)**.

**Network security testing** involves:

- Vulnerability scanning of network devices and services
- Penetration testing to validate security controls
- Segmentation effectiveness testing to verify isolation
- VLAN hopping testing to prevent layer 2 attacks
- Configuration auditing to detect drift and misconfigurations
- Service security testing to validate service hardening
- Continuous validation to maintain security posture


## Scope

This guidance covers:

- **Vulnerability Scanning** - Automated scanning of network devices, services, and configurations
- **Penetration Testing** - Manual testing of network controls, including external and internal testing
- **Segmentation Effectiveness Testing** - Validation of network segmentation and isolation
- **VLAN Hopping Testing** - Testing prevention of layer 2 attacks (double tagging, switch spoofing)
- **Configuration Auditing** - Automated and manual review of network device configurations
- **Network Service Testing** - Testing security of DNS, DHCP, NTP, proxy, and other services
- **Test Documentation** - Recording test procedures, results, and remediation


## Applicability

This guidance is **technology-agnostic** with specific examples for:

- Traditional networks (Cisco, Juniper, HP/Aruba, etc.)
- Software-defined networking (SDN) environments
- Cloud platforms (AWS, Azure, GCP)
- Hybrid and multi-cloud architectures
- Network security appliances (firewalls, IDS/IPS)


## Who Should Use This Guidance

- Security teams conducting network security assessments
- Penetration testers validating network controls
- Network engineers testing segmentation and device hardening
- ISMS implementers preparing for A.8.20/8.21/8.22 assessments
- Auditors verifying network security testing processes


---

# Process Overview

## Network Security Testing Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│           NETWORK SECURITY TESTING PROCESS                       │
└─────────────────────────────────────────────────────────────────┘

Phase 1: Test Planning
├─ Define test scope (which networks, devices, services to test)
├─ Identify test types (vulnerability scan, pentest, seg testing)
├─ Schedule testing windows (off-hours for disruptive tests)
├─ Obtain approvals (change management, stakeholder sign-off)
└─ Prepare test tools and environment

Phase 2: Vulnerability Scanning
├─ Scan network devices (routers, switches, firewalls, APs)
├─ Scan network services (DNS, DHCP, NTP, proxy, etc.)
├─ Scan for configuration issues (weak ciphers, default creds)
├─ Analyze scan results (prioritize critical/high findings)
└─ Generate vulnerability report

Phase 3: Penetration Testing
├─ External penetration testing (internet-facing perimeter)
├─ Internal penetration testing (assume breach scenario)
├─ Lateral movement testing (test segmentation boundaries)
├─ Privilege escalation testing (network device access)
└─ Document findings and recommendations

Phase 4: Segmentation Effectiveness Testing
├─ Inter-zone traffic testing (verify allow/deny policies)
├─ Firewall rule testing (test each rule for effectiveness)
├─ Packet capture verification (analyze traffic flows)
├─ Lateral movement simulation (simulate attacker movement)
└─ Document segmentation gaps

Phase 5: VLAN Hopping Testing
├─ Double tagging attack testing
├─ Switch spoofing (DTP) attack testing
├─ Verify VLAN security controls (native VLAN, DTP disabled)
└─ Document findings

Phase 6: Configuration Auditing
├─ Automated configuration compliance scanning
├─ Manual configuration review (spot checks)
├─ Drift detection (compare running config to baseline)
├─ Identify misconfigurations
└─ Generate compliance report

Phase 7: Network Service Testing
├─ DNS security testing (DNSSEC, DNS filtering, query logging)
├─ DHCP security testing (rogue DHCP detection, snooping)
├─ NTP security testing (authentication, access controls)
├─ Proxy security testing (authentication, SSL inspection)
└─ Document service security gaps

Phase 8: Test Documentation and Remediation
├─ Consolidate test results
├─ Prioritize findings (critical, high, medium, low)
├─ Develop remediation plan
├─ Track remediation progress
└─ Re-test after remediation (validation testing)
```

## Key Principles

**Non-Disruptive Testing**: Prefer passive testing (packet capture, log analysis) over active testing (port scanning) when possible.

**Risk-Based Approach**: Prioritize testing of high-value assets and high-risk areas (internet-facing, sensitive data).

**Realistic Scenarios**: Test real-world attack scenarios (lateral movement, privilege escalation).

**Continuous Testing**: Network security testing is not one-time; schedule regular testing (quarterly, annually).

**Safe Testing**: Use controlled environments (labs) for disruptive tests before production.

---

# Prerequisites and Tools

## Required Access and Permissions

- Network access to devices under test (management interfaces, CLI)
- Approval for testing activities (change management, stakeholder sign-off)
- Credentials for authenticated scanning (SNMP, SSH, API access)
- Test network or lab environment for disruptive tests


## Required Tools

**Vulnerability Scanning**:

- **Nessus** (commercial, comprehensive vulnerability scanner)
- **Qualys** (commercial, cloud-based vulnerability management)
- **OpenVAS** (open-source vulnerability scanner)
- **Nipper** (network device configuration auditor - Cisco, Juniper, etc.)


**Network Discovery and Reconnaissance**:

- **nmap** (open-source port scanner, service detection)
- **Masscan** (fast port scanner for large networks)
- **Shodan** (internet-connected device search engine)


**Penetration Testing**:

- **Metasploit** (open-source exploitation framework)
- **Burp Suite** (web application testing - for network services with web interfaces)
- **Cobalt Strike** (commercial, advanced threat emulation)
- **BloodHound** (Active Directory attack path analysis)


**Layer 2 Attacks (VLAN Hopping)**:

- **Yersinia** (layer 2 attack tool - DTP, DHCP, STP, etc.)
- **Scapy** (packet crafting for custom attacks)


**Traffic Analysis**:

- **Wireshark** (packet capture and analysis)
- **tcpdump** (command-line packet capture)
- **tshark** (command-line Wireshark)


**Configuration Management and Auditing**:

- **RANCID** (Really Awesome New Cisco confIg Differ - config backup and comparison)
- **Ansible** (configuration management, compliance checking)
- **Puppet/Chef** (configuration management)


**Cloud Security Testing**:

- **ScoutSuite** (multi-cloud security auditing tool - AWS, Azure, GCP)
- **Prowler** (AWS security best practices assessment)
- **CloudMapper** (AWS network diagram and security analysis)


**Network Service Testing**:

- **dig** (DNS query tool)
- **nslookup** (DNS query tool)
- **dnsenum** (DNS enumeration)
- **DHCPig** (DHCP exhaustion and testing)


## Required Skills and Knowledge

- Network security fundamentals (TCP/IP, routing, switching, firewalls)
- Vulnerability assessment methodologies (OWASP, PTES, OSSTMM)
- Penetration testing techniques (reconnaissance, exploitation, post-exploitation)
- Layer 2 attack techniques (VLAN hopping, ARP spoofing, etc.)
- Packet analysis (Wireshark, tcpdump)
- Scripting (Python, Bash) for automation


---

# Step-by-Step Procedures

## Phase 1: Test Planning

### Define Test Scope

**Objective**: Clearly define what will be tested and what will not.

**Steps**:

1. **Identify networks in scope**:

   - Production networks (internal, DMZ, management)
   - Development/test networks (if separate)
   - Cloud networks (AWS VPCs, Azure VNets, GCP VPCs)


2. **Identify devices in scope**:

   - Network devices (routers, switches, firewalls, wireless APs)
   - Network security appliances (IDS/IPS, network monitoring)
   - Load balancers, VPN concentrators


3. **Identify services in scope**:

   - DNS, DHCP, NTP, proxy, RADIUS/TACACS+, SNMP, syslog


4. **Identify exclusions** (out of scope):

   - Legacy systems (if can't be safely tested)
   - Third-party managed networks (if no access)
   - Production systems during business hours (if disruptive testing)


**Example Scope Statement**:
```
Scope: All production network devices and services in HQ and Branch Office 1
       AWS production VPC (us-east-1)
       Testing period: January 15-19, 2026 (off-hours: 10 PM - 6 AM)

Out of Scope: Branch Office 2 (third-party managed)
              Legacy Cisco Catalyst 2950 switches (end-of-life, no vendor support)
```

### Identify Test Types

**Select appropriate test types**:

| Test Type | Purpose | Frequency | Risk Level |
|-----------|---------|-----------|------------|
| **Vulnerability Scanning** | Identify known vulnerabilities | Monthly | Low |
| **Configuration Auditing** | Detect misconfigurations and drift | Monthly | Low |
| **External Penetration Testing** | Test perimeter defenses | Annual | Medium |
| **Internal Penetration Testing** | Test internal controls, lateral movement | Annual | Medium |
| **Segmentation Testing** | Verify network isolation | Quarterly | Low |
| **VLAN Hopping Testing** | Test layer 2 attack prevention | Quarterly | Medium |
| **Network Service Testing** | Validate service security | Quarterly | Low |

**Disruptive vs. Non-Disruptive**:

- **Non-Disruptive**: Vulnerability scanning (read-only), configuration auditing, packet capture
- **Disruptive**: Penetration testing (active exploitation), VLAN hopping attacks, DoS testing


**Risk Management**: For disruptive tests, use test/lab environments when possible.

### Obtain Approvals

**Required Approvals**:

1. **Change Management**: Submit change request (even for read-only testing)
2. **Stakeholder Sign-Off**: Get approval from:

   - Network team (may need to assist with testing)
   - Security team (oversight)
   - IT management (aware of testing activities)
   - Business stakeholders (if testing affects business systems)

3. **Legal/Compliance** (for penetration testing): Confirm testing is authorized

**Example Change Request**:
```
Change Request: Network Security Vulnerability Scan
Date: January 10, 2026
Requester: Security Team
Scope: All production network devices
Risk Level: Low (read-only scanning)
Schedule: January 15, 2026, 10 PM - 2 AM
Approvers: Network Manager, CISO
```

---

## Phase 2: Vulnerability Scanning

### Network Device Vulnerability Scanning

**Objective**: Identify known vulnerabilities in network devices (routers, switches, firewalls).

**Tools**: Nessus, Qualys, OpenVAS

**Nessus Example** (authenticated scan):

**Step 1: Create Scan Policy**

1. Log in to Nessus web interface
2. Navigate to **Policies** → **New Policy**
3. Select **Advanced Scan** policy
4. Configure settings:

   - **Name**: Network Device Vulnerability Scan
   - **Targets**: [List of device IP addresses or subnets]
   - **Credentials**: Add SSH credentials for authenticated scanning
   - **Plugins**: Enable all plugins (or focus on network device plugins)

5. Save policy

**Step 2: Launch Scan**

1. Navigate to **Scans** → **New Scan**
2. Select policy: **Network Device Vulnerability Scan**
3. Enter targets (IP ranges, subnets, or individual IPs):
   ```
   10.1.10.1-10.1.10.254   # DMZ devices
   10.1.20.1-10.1.20.254   # Internal devices
   10.1.40.1-10.1.40.254   # Management devices
   ```
4. Schedule scan (e.g., January 15, 2026, 10 PM)
5. Launch scan

**Step 3: Analyze Results**

After scan completes:

1. Review **Summary** tab:

   - Total vulnerabilities: [number]
   - Critical: [number]
   - High: [number]
   - Medium: [number]
   - Low: [number]
   - Info: [number]


2. Review **Vulnerabilities** tab:

   - Sort by **Severity** (Critical first)
   - Review each vulnerability:
     - CVE ID (e.g., CVE-2023-20198)
     - CVSS Score (e.g., 9.8 Critical)
     - Affected hosts
     - Solution (patch, workaround)


3. Prioritize remediation:

   - **Critical**: Immediate action (within 24-48 hours)
   - **High**: Urgent action (within 7 days)
   - **Medium**: Scheduled action (within 30 days)
   - **Low**: Tracked for future remediation


**Step 4: Generate Report**

1. Navigate to **Reports** → **Generate Report**
2. Select report type: **Executive Summary** or **Technical Report**
3. Export as PDF or CSV
4. Distribute to stakeholders (network team, security team, management)

**Example Vulnerability Report Summary**:
```
Network Device Vulnerability Scan Report
Date: January 16, 2026
Scan Duration: 4 hours
Devices Scanned: 45

Findings:

- Critical: 2 (outdated firmware on 2 routers - CVE-2023-XXXXX)
- High: 8 (weak SNMP community strings, default credentials on 3 switches)
- Medium: 15 (SSH protocol v1 enabled, weak SSL ciphers)
- Low: 22 (banner message missing, unnecessary services enabled)


Recommended Actions:
1. Upgrade firmware on routers (Critical priority)
2. Change SNMP community strings to strong values (High priority)
3. Disable default credentials and create unique admin accounts (High priority)
```

### Configuration Vulnerability Scanning

**Objective**: Identify configuration issues (weak ciphers, default credentials, unnecessary services).

**Tools**: Nipper, Nessus Policy Compliance scanning

**Nipper Example** (Cisco configuration audit):

**Step 1: Export Device Configuration**

```bash
# SSH to Cisco device and export config
ssh admin@10.1.10.1
show running-config > /tmp/router-config.txt
exit

# Copy config to local machine
scp admin@10.1.10.1:/tmp/router-config.txt .
```

**Step 2: Run Nipper**

```bash
# Install Nipper (if not already installed)
# Nipper is commercial software; trial version available

# Run Nipper on config file
nipper --ios --input=router-config.txt --output=router-audit-report.html

# Nipper analyzes config and generates HTML report
```

**Step 3: Review Report**

Open `router-audit-report.html` in browser:

- **Security Audit**: Lists configuration issues
  - Weak passwords (if detectable)
  - Unnecessary services (HTTP server enabled, CDP enabled, etc.)
  - Weak encryption (SSH v1, weak SSL ciphers)
  - Access control issues (overly permissive ACLs)
  
- **Recommendations**: Specific config commands to fix issues


**Example Nipper Findings**:
```
Finding: HTTP server enabled (insecure management interface)
Severity: High
Recommendation: Disable HTTP, use HTTPS only
  no ip http server
  ip http secure-server

Finding: CDP enabled on all interfaces (information disclosure)
Severity: Medium
Recommendation: Disable CDP on external-facing interfaces
  interface GigabitEthernet0/0
   no cdp enable
```

### Vulnerability Scan Automation

**Automate regular scans** using Nessus API or command-line tools.

**Example: Automated Weekly Scan (Python + Nessus API)**

```python
#!/usr/bin/env python3
"""
Automated Nessus vulnerability scan
Scans network devices weekly and emails report
"""

import requests
import json
from datetime import datetime

# Nessus API configuration
NESSUS_URL = "https://nessus.example.com:8834"
API_KEY = "your-api-key"
SECRET_KEY = "your-secret-key"

headers = {
    "X-ApiKeys": f"accessKey={API_KEY}; secretKey={SECRET_KEY}",
    "Content-Type": "application/json"
}

# Launch scan
def launch_scan(scan_id):
    url = f"{NESSUS_URL}/scans/{scan_id}/launch"
    response = requests.post(url, headers=headers, verify=False)
    if response.status_code == 200:
        print(f"Scan {scan_id} launched successfully")
    else:
        print(f"Error launching scan: {response.status_code}")

# Check scan status
def check_scan_status(scan_id):
    url = f"{NESSUS_URL}/scans/{scan_id}"
    response = requests.get(url, headers=headers, verify=False)
    data = response.json()
    return data['info']['status']

# Export scan results
def export_scan(scan_id):
    url = f"{NESSUS_URL}/scans/{scan_id}/export"
    data = {"format": "pdf"}
    response = requests.post(url, headers=headers, json=data, verify=False)
    file_id = response.json()['file']
    
    # Download exported file
    url = f"{NESSUS_URL}/scans/{scan_id}/export/{file_id}/download"
    response = requests.get(url, headers=headers, verify=False)
    
    filename = f"nessus-report-{datetime.now().strftime('%Y-%m-%d')}.pdf"
    with open(filename, 'wb') as f:
        f.write(response.content)
    
    print(f"Report exported: {filename}")
    return filename

# Main
if __name__ == "__main__":
    SCAN_ID = 123  # Replace with your scan ID
    
    # Launch scan
    launch_scan(SCAN_ID)
    
    # Wait for scan to complete (check every 5 minutes)
    import time
    while True:
        status = check_scan_status(SCAN_ID)
        print(f"Scan status: {status}")
        if status == "completed":
            break
        time.sleep(300)  # Wait 5 minutes
    
    # Export and email report
    report_file = export_scan(SCAN_ID)
    # Implementation: Add email notification to security team
```

---

## Phase 3: Penetration Testing

### External Penetration Testing

**Objective**: Test perimeter defenses (internet-facing systems).

**Methodology**: OWASP Testing Guide, PTES (Penetration Testing Execution Standard)

**Phases**:

1. **Reconnaissance**: Gather information about target (IP ranges, domain names, services)
2. **Scanning**: Identify open ports, services, versions
3. **Exploitation**: Attempt to exploit vulnerabilities
4. **Post-Exploitation**: Access internal network (if perimeter breached)
5. **Reporting**: Document findings and recommendations

**Example: External Perimeter Test**

**Phase 1: Reconnaissance**

```bash
# DNS reconnaissance (find subdomains, IP addresses)
dig example.com ANY
nslookup -type=ANY example.com

# WHOIS lookup (organization info, IP ranges)
whois example.com

# Shodan search (internet-facing devices)
# Visit: shodan.io
# Search: org:"Example Corp"
# Identify exposed devices (routers, firewalls, cameras, etc.)
```

**Phase 2: Port Scanning**

```bash
# TCP SYN scan (stealth scan) of perimeter
sudo nmap -sS -p- -T4 -v 203.0.113.0/24

# Service version detection
sudo nmap -sV -p22,80,443 203.0.113.0/24

# OS detection
sudo nmap -O 203.0.113.0/24

# Example output:
# 203.0.113.10:
#   22/tcp open  ssh     OpenSSH 7.4 (protocol 2.0)
#   443/tcp open https   nginx 1.18.0
#   OS: Linux 3.X
```

**Phase 3: Vulnerability Assessment**

```bash
# NSE (Nmap Scripting Engine) vulnerability scan
sudo nmap --script vuln 203.0.113.10

# Test for common vulnerabilities:
# - SSL/TLS issues (weak ciphers, expired certs)
# - SSH vulnerabilities
# - Web server vulnerabilities
```

**Phase 4: Exploitation** (Controlled Environment)

**Example: SSH brute force (to test password policy)**

```bash
# Use Metasploit for SSH brute force
msfconsole
use auxiliary/scanner/ssh/ssh_login
set RHOSTS 203.0.113.10
set USERNAME admin
set PASS_FILE /usr/share/wordlists/rockyou.txt
set THREADS 5
run

# Expected: Brute force should FAIL (strong password policy prevents)
# If successful: CRITICAL finding (weak password)
```

**Phase 5: Report Findings**

Example Finding:
```
Finding: SSH Accessible from Internet (Port 22)
Severity: High
Description: SSH service is accessible from the internet on 203.0.113.10.
             While SSH is encrypted, it may be subject to brute force attacks.
Risk: Brute force attacks, credential stuffing
Recommendation: 
  1. Restrict SSH access to VPN or trusted IPs (firewall rule)
  2. Implement SSH key-based authentication (disable password auth)
  3. Enable fail2ban (automatic IP blocking after failed attempts)
  4. Use non-standard SSH port (security through obscurity - minor benefit)
```

### Internal Penetration Testing

**Objective**: Test internal controls, simulate lateral movement after initial compromise.

**Assumption**: Attacker has initial foothold (compromised workstation).

**Methodology**:

1. **Initial Access**: Assume attacker has access to internal workstation
2. **Reconnaissance**: Scan internal network (identify targets)
3. **Lateral Movement**: Attempt to move to other zones (test segmentation)
4. **Privilege Escalation**: Attempt to gain administrative access to network devices
5. **Data Exfiltration**: Attempt to access sensitive data (databases, file servers)
6. **Persistence**: Attempt to maintain access (backdoors, scheduled tasks)
7. **Reporting**: Document attack paths and segmentation gaps

**Example: Internal Pentest Scenario**

**Phase 1: Internal Reconnaissance**

```bash
# From compromised workstation (10.1.30.50 - Internal zone)
# Scan internal network
nmap -sn 10.1.0.0/16
# Identify live hosts (servers, network devices)

# Scan for interesting services
nmap -p- -T4 10.1.20.0/24
# Identify databases (3306, 5432), file shares (445), admin interfaces (22, 3389)
```

**Phase 2: Test Segmentation (Lateral Movement)**

```bash
# Attempt to access Management zone (should be DENIED)
telnet 10.1.40.10 22
# Expected: Connection timeout or refused (firewall blocks)

# Attempt to access DMZ zone (should be DENIED)
curl http://10.1.10.10
# Expected: Connection timeout (firewall blocks Internal → DMZ)

# Verify firewall logs show denied attempts
```

**Phase 3: Privilege Escalation**

```bash
# Attempt to access network device (router)
telnet 10.1.20.1 23
# Try default credentials: admin/admin, cisco/cisco, etc.
# Expected: Authentication fails (strong password policy, unique credentials)

# Attempt SSH with common credentials
ssh admin@10.1.20.1
# Password: [try common passwords]
# Expected: Authentication fails
```

**Phase 4: Data Exfiltration Test**

```bash
# Attempt to access database (if accessible from workstation)
mysql -h 10.1.20.50 -u root -p
# Try common passwords: root, password, admin, etc.
# Expected: Authentication fails (strong DB password, firewall rules limit access)

# If accessible: Attempt to query sensitive data
# Check if data is encrypted (verify encryption in transit and at rest)
```

**Phase 5: Report Findings**

Example Finding:
```
Finding: Lateral Movement Blocked by Segmentation
Severity: Pass (Control Working)
Description: From compromised workstation in Internal zone, attempts to access
             Management zone (10.1.40.0/24) were blocked by firewall.
Evidence: tcpdump capture shows SYN packets sent to 10.1.40.10:22, but no SYN-ACK
          received (firewall dropped packets). Firewall logs show denied traffic.
Conclusion: Segmentation is effective. Lateral movement is prevented.
```

Example Finding (Gap):
```
Finding: Database Accessible from All Internal Workstations
Severity: High
Description: Database server (10.1.20.50:3306) is accessible from all workstations
             in Internal zone. Only web servers (10.1.10.0/24) should access DB.
Risk: Compromised workstation can access database directly (SQL injection, data theft)
Recommendation: Implement firewall rule to restrict DB access:

  - Allow: 10.1.10.0/24 (web servers) → 10.1.20.50:3306
  - Deny: 10.1.30.0/22 (workstations) → 10.1.20.50:3306

```

---

## Phase 4: Segmentation Effectiveness Testing

### Inter-Zone Traffic Testing

**Objective**: Verify firewall rules allow authorized traffic and block unauthorized traffic.

**Procedure**:

1. **Identify inter-zone traffic policies** (from Segmentation Matrix - WB4)
2. **Test allowed traffic** (should succeed)
3. **Test denied traffic** (should fail)
4. **Verify firewall logs** (denied traffic logged)

**Example Test Cases**:

| Test ID | Source Zone | Source IP | Dest Zone | Dest IP | Protocol/Port | Expected Result |
|---------|-------------|-----------|-----------|---------|---------------|-----------------|
| TC-001 | Internal | 10.1.30.50 | Internet | 8.8.8.8 | UDP/53 (DNS) | ALLOW |
| TC-002 | Internal | 10.1.30.50 | DMZ | 10.1.10.10 | TCP/443 (HTTPS) | ALLOW |
| TC-003 | Internal | 10.1.30.50 | Management | 10.1.40.10 | TCP/22 (SSH) | DENY |
| TC-004 | DMZ | 10.1.10.10 | Internal | 10.1.20.50 | TCP/3306 (MySQL) | ALLOW |
| TC-005 | DMZ | 10.1.10.10 | Internet | 0.0.0.0/0 | Any | ALLOW (outbound) |
| TC-006 | Guest | 10.1.50.50 | Internal | 10.1.20.0/24 | Any | DENY |

**Test Execution**:

**TC-001: Internal → Internet (DNS) - ALLOW**
```bash
# From workstation 10.1.30.50
dig @8.8.8.8 example.com

# Expected: DNS response received (success)
```

**TC-003: Internal → Management (SSH) - DENY**
```bash
# From workstation 10.1.30.50
telnet 10.1.40.10 22

# Expected: Connection timeout (firewall blocks)
# Verify in firewall logs: denied connection logged
```

**TC-004: DMZ → Internal (MySQL) - ALLOW**
```bash
# From web server 10.1.10.10
mysql -h 10.1.20.50 -u webapp -p

# Expected: Connection successful, can query database
```

**TC-006: Guest → Internal (Any) - DENY**
```bash
# From guest device 10.1.50.50
ping 10.1.20.50

# Expected: No ping response (firewall blocks ICMP)

telnet 10.1.20.50 445

# Expected: Connection timeout (firewall blocks SMB)
```

### Packet Capture Verification

**Objective**: Capture traffic at zone boundaries and verify only authorized traffic flows.

**Procedure**:

1. **Capture traffic** at firewall or router interface
2. **Analyze captured traffic** (Wireshark, tcpdump)
3. **Verify traffic matches firewall rules** (only authorized traffic passes)

**Example: Capture DMZ → Internal Traffic**

```bash
# On firewall or router, capture traffic between DMZ and Internal
sudo tcpdump -i eth0 -n 'src net 10.1.10.0/24 and dst net 10.1.20.0/24' -w dmz-internal.pcap -v

# Let capture run for 5-10 minutes (or during business hours)
# Stop capture (Ctrl+C)

# Analyze capture
tcpdump -r dmz-internal.pcap -n

# Example output:
# 10:15:30.123456 IP 10.1.10.10.54321 > 10.1.20.50.3306: Flags [S], seq 12345
# 10:15:30.123789 IP 10.1.20.50.3306 > 10.1.10.10.54321: Flags [S.], seq 67890, ack 12346
# (MySQL traffic between web server and database)

# Verify:
# - Traffic is TCP/3306 (MySQL) - matches firewall rule
# - No other protocols/ports (e.g., no SSH, RDP, ICMP)
# - Source IPs are web servers (10.1.10.0/24)
# - Destination IPs are database servers (10.1.20.50)
```

**Wireshark Analysis**:
1. Open `dmz-internal.pcap` in Wireshark
2. Apply display filter: `ip.src == 10.1.10.0/24 && ip.dst == 10.1.20.0/24`
3. View **Statistics → Protocol Hierarchy** - verify only authorized protocols
4. View **Statistics → Conversations** - verify authorized IP pairs only

---

## Phase 5: VLAN Hopping Testing

### Double Tagging Attack Testing

**Objective**: Verify prevention of VLAN hopping via double tagging.

**Attack Explanation**:

- Attacker sends double-tagged 802.1Q frame (outer tag = native VLAN, inner tag = target VLAN)
- If native VLAN = VLAN 1 (default), outer tag is stripped by first switch, inner tag is processed by second switch
- Attacker can access target VLAN without authorization


**Prevention** (implemented in ISMS-IMP-A.8.20-21-22-S5):

- Change native VLAN to unused VLAN (not VLAN 1)


**Testing Procedure**:

```bash
# Use Scapy to craft double-tagged frame
sudo scapy

>>> from scapy.all import *

# Craft double-tagged frame
# Outer tag: VLAN 1 (native VLAN), Inner tag: VLAN 20 (Servers)
>>> packet = Ether()/Dot1Q(vlan=1)/Dot1Q(vlan=20)/IP(dst="10.1.20.50")/ICMP()

# Send packet
>>> sendp(packet, iface="eth0")

# Monitor destination (10.1.20.50) for ICMP packet
# Expected: ICMP packet NOT received (attack failed)
# Reason: Native VLAN changed from 1 to 999; double tagging fails
```

**Verification**:

- **If attack fails**: Native VLAN is NOT VLAN 1 → Control working
- **If attack succeeds**: Native VLAN is still VLAN 1 → CRITICAL vulnerability, change native VLAN immediately


### Switch Spoofing (DTP) Attack Testing

**Objective**: Verify prevention of VLAN hopping via DTP (Dynamic Trunking Protocol).

**Attack Explanation**:

- Attacker sends DTP packets to negotiate trunk with switch
- If DTP enabled and switch accepts, attacker gains access to all VLANs


**Prevention** (implemented in ISMS-IMP-A.8.20-21-22-S5):

- Disable DTP (`switchport nonegotiate`)
- Hardcode switchport mode (`switchport mode access` or `switchport mode trunk`)


**Testing Procedure**:

```bash
# Use Yersinia to attempt DTP negotiation
sudo yersinia -G   # Launch GUI

# In Yersinia GUI:
# Select "DTP" attack
# Click "Attack" → "Enabling trunking"
# Select interface (e.g., eth0)
# Launch attack

# Monitor switch logs for DTP messages
# Expected: Switch REJECTS DTP negotiation (DTP disabled)
# Reason: switchport nonegotiate configured on all ports
```

**Verification**:

- **If attack fails**: DTP disabled → Control working
- **If attack succeeds**: DTP still enabled → HIGH vulnerability, disable DTP immediately


---

## Phase 6: Configuration Auditing

### Automated Configuration Compliance Scanning

**Objective**: Verify device configurations match hardening baselines.

**Tools**: Nessus Policy Compliance, Ansible

**Nessus Policy Compliance Example**:

**Step 1: Create Compliance Policy**

1. Navigate to **Policies** → **Policy Compliance Auditing**
2. Select **Cisco IOS Compliance Audit** template
3. Configure:

   - **Policy Name**: Cisco Router Hardening Compliance
   - **Audit File**: Upload custom audit file (defines checks)
   - **Credentials**: Add SSH credentials


**Example Audit File** (Nessus .audit format):
```
<check_type:"Unix">
<group_title:"Cisco IOS Hardening Baseline">

<custom_item>
  type: CMD_EXEC
  description: "Verify HTTP server is disabled"
  cmd: "show running-config | include ip http server"
  expect: "no ip http server"
</custom_item>

<custom_item>
  type: CMD_EXEC
  description: "Verify SSH version 2 only"
  cmd: "show ip ssh"
  regex: "SSH Enabled.*version 2"
</custom_item>

<custom_item>
  type: CMD_EXEC
  description: "Verify banner message configured"
  cmd: "show running-config | section banner"
  expect: "banner"
</custom_item>
```

**Step 2: Run Compliance Scan**

1. Launch scan with compliance policy
2. Scan completes → Review results

**Step 3: Review Compliance Results**

Nessus reports compliance status per check:

- **PASSED**: Configuration matches baseline
- **FAILED**: Configuration does not match baseline (gap identified)


Example Output:
```
Compliance Scan Results: Cisco Router 10.1.10.1

PASSED: HTTP server disabled
FAILED: SSH version 2 only (SSH v1 still enabled)
FAILED: Banner message configured (no banner configured)
PASSED: SNMP v3 only (v1/v2c disabled)
```

### Configuration Drift Detection

**Objective**: Detect changes to configurations over time (unauthorized changes).

**Tools**: RANCID, Git, Ansible

**RANCID Example** (Really Awesome New Cisco confIg Differ):

**Step 1: Install RANCID**

```bash
# Install RANCID (on Ubuntu/Debian)
sudo apt-get install rancid

# Configure RANCID
sudo vi /etc/rancid/rancid.conf
# Set: LIST_OF_GROUPS="network-devices"
```

**Step 2: Add Devices to RANCID**

```bash
# Create router.db file (list of devices)
sudo vi /var/lib/rancid/network-devices/router.db

# Add devices (one per line):
10.1.10.1:cisco:up
10.1.20.1:cisco:up
10.1.40.1:cisco:up
```

**Step 3: Configure Credentials**

```bash
# Create .cloginrc file (credentials)
sudo vi /var/lib/rancid/.cloginrc

add user * admin
add password * {strong-password}
add method * ssh
```

**Step 4: Run RANCID**

```bash
# Run initial backup
sudo -u rancid /usr/lib/rancid/bin/rancid-run

# RANCID connects to devices, downloads configs, stores in CVS/Git
# Subsequent runs detect config changes
```

**Step 5: Review Changes**

```bash
# View change log
sudo cat /var/lib/rancid/network-devices/logs/network-devices.YYYYMMDD.log

# Example output:
# Config changed: 10.1.10.1
# - interface GigabitEthernet0/1
# -  description Server-DB01
# +  description Server-DB01-Production
```

**Alerting**: Configure RANCID to email on config changes.

---

## Phase 7: Network Service Testing

### DNS Security Testing

**Test 1: DNSSEC Validation**

```bash
# Test if DNSSEC is enabled and working
dig @10.1.10.5 example.com +dnssec

# Look for:
# - RRSIG records (DNSSEC signatures)
# - ad flag (authenticated data)

# If DNSSEC working:
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1
```

**Test 2: DNS Filtering (Malicious Domain Blocking)**

```bash
# Test if DNS filtering blocks known malicious domains
dig @10.1.10.5 malware.example.com

# Expected: NXDOMAIN or redirect to block page (DNS filtering active)
# If resolved: DNS filtering may not be working
```

**Test 3: DNS Query Logging**

```bash
# Verify DNS query logs are enabled
# SSH to DNS server
ssh admin@10.1.10.5

# Check DNS logs
tail -f /var/log/named/query.log

# Expected: DNS queries logged (source IP, query, timestamp)
```

### DHCP Security Testing

**Test 1: Rogue DHCP Detection**

```bash
# Attempt to run rogue DHCP server (from attacker workstation)
sudo dhcpd -cf /tmp/rogue-dhcp.conf eth0

# Monitor network for DHCP snooping alerts
# Expected: DHCP snooping detects rogue server, blocks DHCP offers from unauthorized source

# Verify DHCP snooping is working:
# SSH to switch
show ip dhcp snooping
# Look for: DHCP snooping enabled, trusted ports configured
```

**Test 2: DHCP Exhaustion**

```bash
# Use DHCPig to exhaust DHCP scope (DoS test)
sudo dhcpig --interface eth0 --count 100

# Expected: DHCP server has rate limiting, blocks excessive requests
# If successful (all IPs exhausted): Implement rate limiting, increase scope size
```

### NTP Security Testing

**Test 1: NTP Authentication**

```bash
# Attempt to query NTP without authentication
ntpq -c peers 10.1.10.6

# Expected: Query blocked (authentication required)
# If successful without auth: NTP authentication NOT enabled (gap)
```

**Test 2: Time Synchronization**

```bash
# Verify system time is synchronized with NTP
ntpstat

# Expected: synchronised to NTP server 10.1.10.6 at stratum 2
```

### Proxy Security Testing

**Test 1: Proxy Bypass Attempt**

```bash
# Attempt to access internet directly (bypass proxy)
curl http://example.com

# Expected: Connection fails (firewall blocks direct internet access, forces proxy)
# If successful: Proxy bypass possible (implement firewall rules to force proxy)
```

**Test 2: SSL Interception Verification**

```bash
# Access HTTPS site through proxy
curl https://example.com --proxy http://10.1.10.7:3128

# Check SSL certificate
curl -v https://example.com --proxy http://10.1.10.7:3128 2>&1 | grep "issuer"

# Expected: Certificate issuer is proxy CA (SSL inspection working)
# Example: issuer: CN=Example-Proxy-CA
```

---

## Phase 8: Test Documentation and Remediation

### Consolidate Test Results

**Create Master Test Report**:

```
Network Security Testing Report
Test Period: January 15-19, 2026
Tester: Security Team
Scope: HQ Network (10.1.0.0/16), AWS VPC (10.100.0.0/16)

Summary:

- Vulnerability Scan: 45 devices scanned, 27 findings (2 critical, 8 high)
- Penetration Test: 5 findings (1 critical, 2 high, 2 medium)
- Segmentation Test: PASSED (segmentation effective, no lateral movement)
- VLAN Hopping Test: PASSED (double tagging failed, DTP negotiation failed)
- Configuration Audit: 15 devices audited, 10 gaps identified
- Service Testing: 5 services tested, 2 gaps (DNS filtering, DHCP rate limiting)


Critical Findings:
1. Outdated firmware on 2 routers (CVE-2023-XXXXX) - Remote code execution
2. Database accessible from all workstations (should be restricted to web servers)

High Findings:
1. Default credentials on 3 switches (admin/admin)
2. SSH v1 enabled on 5 devices (should be v2 only)
3. HTTP management interface enabled on 4 devices (should be HTTPS only)
...

Recommendations:
1. Upgrade router firmware immediately (Critical)
2. Implement firewall rule to restrict database access (Critical)
3. Change default credentials on switches (High)
4. Disable SSH v1 on all devices (High)
...
```

### Prioritize Findings

**Severity Matrix**:

| Severity | Criteria | Remediation Timeframe |
|----------|----------|------------------------|
| **Critical** | Remote code execution, default credentials, unencrypted sensitive data | Immediate (24-48 hours) |
| **High** | Weak authentication, unnecessary services, segmentation gaps | Urgent (7 days) |
| **Medium** | Configuration issues, missing logging, weak encryption | Scheduled (30 days) |
| **Low** | Informational, best practices | Tracked for future (90 days) |

### Develop Remediation Plan

**For Each Finding**:

1. **Assign Owner**: Who is responsible for remediation?
2. **Develop Fix**: What actions are required?
3. **Schedule Fix**: When will it be done?
4. **Track Progress**: Is remediation on schedule?
5. **Validate Fix**: Re-test after remediation

**Example Remediation Plan**:

| Finding ID | Severity | Description | Owner | Fix | Target Date | Status |
|------------|----------|-------------|-------|-----|-------------|--------|
| VULN-001 | Critical | Outdated firmware on routers | Network Team | Upgrade firmware to latest version | Jan 20, 2026 | In Progress |
| VULN-002 | Critical | Database accessible from all workstations | Security Team | Implement firewall rule to restrict DB access | Jan 22, 2026 | Open |
| VULN-003 | High | Default credentials on switches | Network Team | Change credentials, document new passwords | Jan 25, 2026 | Open |

### Re-Test After Remediation

**Validation Testing**:

After remediation, re-test to verify fix:

```bash
# Example: Verify router firmware upgraded
ssh admin@10.1.10.1
show version
# Expected: Firmware version = latest (e.g., 16.12.05)

# Example: Verify database access restricted
# From workstation (should fail)
telnet 10.1.20.50 3306
# Expected: Connection timeout (firewall blocks)

# From web server (should succeed)
mysql -h 10.1.20.50 -u webapp -p
# Expected: Connection successful
```

---

# Automation Opportunities

## Automated Vulnerability Scanning

**Schedule regular scans** using cron or Task Scheduler.

```bash
# Cron job to run Nessus scan weekly (Sundays at 2 AM)

0 2 * * 0 /usr/local/bin/run-nessus-scan.sh


# run-nessus-scan.sh:
#!/bin/bash
python3 /opt/scripts/nessus_scan.py
mail -s "Weekly Vulnerability Scan Complete" security@example.com < /tmp/scan-summary.txt
```

## Continuous Configuration Monitoring

**RANCID** + **Git** + **Webhooks** = Real-time config change notifications.

```bash
# Configure RANCID to push to Git repo
# Configure Git webhook to notify security team on commits
# Result: Immediate notification when network config changes
```

## Automated Compliance Reporting

**Python script** to consolidate test results and generate compliance report.

```python
#!/usr/bin/env python3
"""
Generate network security compliance report
Consolidates vulnerability scan, pentest, segmentation test results
"""

import json
from datetime import datetime

# Load test results (JSON files from various tools)
with open('vuln-scan-results.json') as f:
    vuln_results = json.load(f)

with open('pentest-results.json') as f:
    pentest_results = json.load(f)

with open('segmentation-test-results.json') as f:
    seg_results = json.load(f)

# Calculate compliance scores
total_findings = len(vuln_results) + len(pentest_results)
critical_findings = sum(1 for f in vuln_results if f['severity'] == 'Critical')
high_findings = sum(1 for f in vuln_results if f['severity'] == 'High')

# Generate report
report = f"""
Network Security Compliance Report
Date: {datetime.now().strftime('%Y-%m-%d')}

Overall Compliance: {"PASS" if critical_findings == 0 else "FAIL"}

Findings Summary:

- Total Findings: {total_findings}
- Critical: {critical_findings}
- High: {high_findings}


Segmentation Status: {"PASS" if seg_results['status'] == 'pass' else "FAIL"}
"""

print(report)

# Email report to stakeholders
# Implementation: Add email sending functionality
```

---

# Integration with Other Processes

## Vulnerability Management (A.8.8)

**Integration**: Network security testing findings feed into vulnerability management process.

- Vulnerability scan results → vulnerability tracking system (Jira, ServiceNow)
- Track remediation progress
- Re-scan to verify fixes


## Incident Response (A.6.8)

**Integration**: Testing may uncover security incidents (e.g., rogue devices, unauthorized changes).

- If testing finds compromised device → trigger incident response
- Penetration testing simulates real attacks → informs incident response playbooks


## Change Management (A.8.32)

**Integration**: Configuration auditing detects unauthorized changes.

- Unexpected config changes → investigate (authorized change or security incident?)
- Configuration drift → submit change request to bring back to baseline


## Logging and Monitoring (A.8.15, A.8.16)

**Integration**: Testing validates logging and monitoring effectiveness.

- Verify firewall logs capture denied traffic
- Verify SIEM alerts on suspicious network activity
- Testing generates test data for SIEM tuning


---

# Quality Assurance

## Testing Quality Checks

- [ ] Test plan approved by stakeholders
- [ ] Test scope clearly defined (inclusions and exclusions)
- [ ] Test tools validated (ensure tools work as expected)
- [ ] Credentials configured (authenticated scanning where possible)
- [ ] Test environment prepared (if using lab for disruptive tests)
- [ ] Backup configurations before testing (rollback if issues occur)
- [ ] Testing completed within scheduled window
- [ ] Test results documented (findings, evidence, recommendations)
- [ ] Findings prioritized (severity-based)
- [ ] Remediation plan developed (owner, timeline, validation)
- [ ] Test report distributed to stakeholders


---

# Common Pitfalls and Solutions

## Testing Mistakes

**Mistake 1: Testing Production During Business Hours**

- **Problem**: Disruptive testing (port scanning, exploitation) affects business
- **Solution**: Schedule testing during off-hours (nights, weekends)


**Mistake 2: No Test Plan**

- **Problem**: Ad-hoc testing, missing scope, stakeholders unaware
- **Solution**: Always create test plan, get approvals


**Mistake 3: Not Validating Fixes**

- **Problem**: Assume fix worked, but vulnerability still present
- **Solution**: Always re-test after remediation


**Mistake 4: Over-Reliance on Automated Scanning**

- **Problem**: Scanners miss complex issues (logic flaws, custom configs)
- **Solution**: Combine automated + manual testing


## False Positives

**Issue**: Vulnerability scanner reports vulnerability, but it's not exploitable (false positive).

**Solution**:

- Manually verify findings (attempt exploitation)
- Mark false positives in scanner (so they're not reported again)
- Tune scanner settings (reduce false positive rate)


---

# Documentation Requirements

## Test Plan Documentation

- Test scope (what will be tested)
- Test methodology (what types of tests)
- Test schedule (when testing will occur)
- Test approvals (who approved testing)


## Test Results Documentation

- Test execution log (what was done, when, by whom)
- Findings (vulnerabilities, gaps, observations)
- Evidence (screenshots, packet captures, logs)
- Recommendations (how to fix findings)


## Remediation Documentation

- Remediation plan (owner, timeline, status)
- Remediation evidence (configs after fix, re-test results)
- Lessons learned (what went wrong, how to improve)


---

# Continuous Improvement

## Periodic Testing Schedule

- **Monthly**: Vulnerability scanning, configuration auditing
- **Quarterly**: Segmentation testing, VLAN hopping testing, service testing
- **Annual**: Full penetration testing (external + internal)


## Metrics to Track

- **Vulnerability Trends**: Are vulnerabilities decreasing over time?
- **Mean Time to Remediate (MTTR)**: How long to fix findings?
- **Critical/High Findings**: Count of severe findings (goal: 0)
- **Segmentation Effectiveness**: Percentage of successful lateral movement tests (goal: 0%)
- **Configuration Drift**: Count of unauthorized config changes (goal: 0)


## Testing Process Improvement

After each testing cycle:

- Review testing procedures (what went well, what didn't)
- Update test plan based on lessons learned
- Tune tools (reduce false positives, improve coverage)
- Train team (new techniques, tools)


---

# Annexes

## Annex A: Network Security Testing Checklist

[See detailed checklist in ISMS-IMP-A.8.20-21-22-S5 Annex C]

## Annex B: Common Vulnerabilities and Exploits

**Common Network Device Vulnerabilities**:
1. Default credentials (admin/admin, cisco/cisco)
2. Outdated firmware (unpatched CVEs)
3. Weak encryption (SSH v1, weak SSL ciphers)
4. Unnecessary services (HTTP, Telnet, CDP, LLDP on external interfaces)
5. Weak SNMP community strings (public/private)

**Common Exploitation Techniques**:
1. SSH brute force (Hydra, Metasploit)
2. SNMP enumeration (snmpwalk, snmp-check)
3. Firewall rule bypass (packet fragmentation, IP spoofing)
4. VLAN hopping (double tagging, DTP negotiation)
5. ARP spoofing (man-in-the-middle on flat networks)

## Annex C: Testing Tools Comparison

| Tool | Type | Cost | Strengths | Weaknesses |
|------|------|------|-----------|------------|
| Nessus | Vuln Scanner | Commercial | Comprehensive, accurate | Expensive |
| OpenVAS | Vuln Scanner | Free | Open-source, no cost | Slower, fewer plugins |
| nmap | Port Scanner | Free | Fast, versatile | Not a full vuln scanner |
| Metasploit | Pentest | Free/Commercial | Exploitation framework | Requires expertise |
| Nipper | Config Auditor | Commercial | Network device-specific | Limited to certain vendors |

---

# Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISMS Implementation Team | Initial release |

---

**END OF SPECIFICATION**

---

*"Classes will dull your mind, destroy the potential for authentic creativity."*
— John Nash

<!-- QA_VERIFIED: 2026-01-31 -->
