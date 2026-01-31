**ISMS-IMP-A.8.20-21-22-S4 – Network Services Security Process**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.20-21-22-S4 |
| **Version** | 1.0 |
| **Assessment Area** | Network Services Security Implementation |
| **Related Policy** | ISMS-POL-A.8.20-21-22, Section 2.2 (Network Services Security - A.8.21), Section 2.1 (Network Infrastructure Security - A.8.20) |
| **Purpose** | Provide service-specific security implementation guidance for critical network services (DNS, DHCP, NTP, proxy, load balancers, authentication services) including hardening, monitoring, and redundancy |
| **Target Audience** | Network Administrators, System Administrators, Security Engineers, IT Operations, Service Owners, Auditors |
| **Assessment Type** | Service Security Configuration & Availability Assessment |
| **Review Cycle** | Quarterly or After Service Configuration Changes |
| **Total Sheets** | 11 |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guidance for network services security | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** Security assessors, Control owners, Compliance officers

---

# Purpose and Scope

## Purpose
This document provides **service-by-service security implementation guidance** for network services as required by ISO 27001:2022 Control A.8.21 (Security of Network Services). Each critical network service requires specific security configurations to protect confidentiality, integrity, and availability.

## Scope
This guidance covers implementation security for:

- **DNS** (Domain Name System): Authoritative and recursive DNS servers
- **DHCP** (Dynamic Host Configuration Protocol): IP address management
- **NTP** (Network Time Protocol): Time synchronization
- **Proxy Services**: Web proxies and content filtering
- **Load Balancers**: Application delivery and SSL/TLS termination
- **AAA Services**: RADIUS and TACACS+ authentication
- **SNMP** (Simple Network Management Protocol): Network management
- **Syslog**: Centralized logging


## Target Audience

- Network services administrators
- Security engineers
- ISMS implementation teams
- Service owners responsible for network infrastructure


## Prerequisites

- Administrative access to network services
- Understanding of service architecture (authoritative vs. recursive, centralized vs. distributed)
- Configuration backup capabilities
- Testing environment (recommended for validation before production deployment)


---

# Overview of Service Security

Each network service in this document follows a consistent implementation pattern:

1. **Service Overview**: Purpose and security focus
2. **Security Implementation**: Step-by-step configuration with examples
3. **Configuration Examples**: Multiple platforms where relevant (BIND, Unbound, Cisco, Juniper, etc.)
4. **Monitoring & Alerting**: Health checks and performance monitoring
5. **Security Testing**: Validation procedures
6. **Troubleshooting**: Common issues and solutions
7. **Integration Points**: How service integrates with other ISMS controls

This structured approach ensures consistent security implementation across all network services.

---

# DNS (Domain Name System) Security

## Service Overview

**Purpose**: DNS resolves domain names to IP addresses - fundamental internet service  
**Security Focus**: Authenticity (DNSSEC), integrity, availability, privacy  
**Common Implementations**: BIND9, Unbound, PowerDNS, Windows DNS Server  
**Attack Vectors**: DNS spoofing, cache poisoning, amplification attacks, tunneling  

## DNSSEC Implementation

DNSSEC (DNS Security Extensions) cryptographically signs DNS records to prevent spoofing.

**BIND9 DNSSEC Configuration**:

Step 1: Generate keys
```bash
cd /etc/bind/keys
dnssec-keygen -a RSASHA256 -b 2048 -n ZONE example.com  # ZSK
dnssec-keygen -a RSASHA256 -b 4096 -f KSK -n ZONE example.com  # KSK
```

Step 2: Sign zone
```bash
dnssec-signzone -A -3 $(head -c 1000 /dev/random | sha1sum | cut -b 1-16)   -N INCREMENT -o example.com -t /var/lib/bind/db.example.com
```

Step 3: Configure named
```bind
zone "example.com" {
    type master;
    file "/var/lib/bind/db.example.com.signed";
    auto-dnssec maintain;
    inline-signing yes;
};
```

Step 4: Publish DS record to parent zone
```bash
dnssec-dsfromkey Kexample.com.+008+12345.key
# Provide to registrar
```

## Split DNS Architecture

Separates internal and external DNS resolution.

```bind
acl "internal-networks" {
    10.0.0.0/8;
    172.16.0.0/12;
    192.168.0.0/16;
};

view "internal" {
    match-clients { internal-networks; };
    zone "example.com" {
        type master;
        file "/etc/bind/internal/db.example.com.internal";
    };
    recursion yes;
    forwarders { 8.8.8.8; 8.8.4.4; };
};

view "external" {
    match-clients { any; };
    zone "example.com" {
        type master;
        file "/etc/bind/external/db.example.com.external";
    };
    recursion no;
};
```

## DNS Rate Limiting

```bind
rate-limit {
    responses-per-second 10;
    window 15;
    log-only no;
    exempt-clients { 10.1.0.0/24; };
};
```

## DNS Query Logging

```bind
logging {
    channel query_log {
        file "/var/log/bind/query.log" versions 5 size 50m;
        severity info;
        print-time yes;
    };
    category queries { query_log; };
};
```

## DNS Security Testing

```bash
# DNSSEC validation
dig +dnssec +multi example.com

# Test rate limiting
for i in {1..100}; do dig example.com @dns-server & done

# Check for open recursion (should fail)
dig google.com @public-dns-ip
```

---

# DHCP (Dynamic Host Configuration Protocol) Security

## Service Overview

**Purpose**: Dynamically assigns IP addresses to network clients  
**Security Focus**: Rogue server prevention, availability, configuration integrity  
**Common Implementations**: ISC DHCP, Windows DHCP Server, Infoblox  
**Attack Vectors**: Rogue DHCP servers, DHCP starvation, man-in-the-middle  

## DHCP Snooping (Switch-Level Protection)

**Cisco IOS Configuration**:
```cisco
ip dhcp snooping
ip dhcp snooping vlan 10,20,30

interface GigabitEthernet0/24
 description Uplink to DHCP server
 ip dhcp snooping trust

interface range GigabitEthernet0/1-23
 ip dhcp snooping limit rate 10
```

## DHCP Server Hardening

**ISC DHCP Configuration**:
```dhcp
authoritative;
default-lease-time 86400;      # 24 hours
max-lease-time 604800;         # 7 days

subnet 10.1.10.0 netmask 255.255.255.0 {
    range 10.1.10.100 10.1.10.200;
    option routers 10.1.10.1;
    option domain-name-servers 10.1.0.10, 10.1.0.11;
    option ntp-servers 10.1.0.30;
    log-facility local7;
}

host server01 {
    hardware ethernet 00:11:22:33:44:55;
    fixed-address 10.1.10.50;
}
```

## DHCP Scope Management

Proper scope sizing prevents exhaustion:
```
Scope size = (Peak devices * 1.2) + Growth buffer

Example:
Peak: 250 devices
Buffer: 20%
Total: 250 * 1.2 = 300 IPs needed
```

## Rogue DHCP Detection

```bash
# Active testing
sudo dhclient -v eth0
# Look for multiple DHCPOFFER packets from different IPs

# Passive monitoring
sudo tcpdump -i eth0 -n port 67 or port 68
```

---

# NTP (Network Time Protocol) Security

## Service Overview

**Purpose**: Synchronizes system clocks across network  
**Security Focus**: Time source integrity, authentication, availability  
**Common Implementations**: ntpd, chronyd, Windows Time Service  
**Attack Vectors**: Time manipulation, DDoS amplification  

## NTP Authentication

```ntp
# /etc/ntp.keys

1 M a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6


# /etc/ntp.conf (server)
keys /etc/ntp.keys
trustedkey 1
requestkey 1
controlkey 1

server 0.pool.ntp.org iburst
server 1.pool.ntp.org iburst

# /etc/ntp.conf (client)
keys /etc/ntp.keys
trustedkey 1
requestkey 1
server ntp-01.example.com key 1 iburst prefer
```

## NTP Access Control

```ntp
restrict default kod nomodify notrap nopeer noquery
restrict -6 default kod nomodify notrap nopeer noquery
restrict 127.0.0.1
restrict ::1
restrict 10.0.0.0 mask 255.0.0.0 nomodify notrap nopeer
```

## NTP Monitoring

```bash
# Check sync status
ntpq -p

# Check offset
ntpq -p | grep '^\*' | awk '{print $9}'
# Acceptable: < 50ms
# Warning: 50-100ms
# Critical: > 100ms
```

---

# Proxy Service Security

## Service Overview

**Purpose**: Centralizes web access control and content filtering  
**Security Focus**: Authentication, SSL inspection, bypass prevention  
**Common Implementations**: Squid, Blue Coat, Zscaler, Microsoft Forefront  
**Attack Vectors**: Authentication bypass, certificate trust issues, proxy chaining  

## Proxy Authentication (LDAP)

```squid
# /etc/squid/squid.conf
auth_param basic program /usr/lib/squid/basic_ldap_auth     -b "ou=users,dc=example,dc=com"     -D "cn=squid,ou=services,dc=example,dc=com"     -w "password"     -f "uid=%s"     -h ldap.example.com

auth_param basic children 5
auth_param basic realm Proxy Authentication

acl authenticated proxy_auth REQUIRED
http_access allow authenticated
http_access deny all
```

## SSL/TLS Inspection

**Generate CA certificate**:
```bash
openssl req -new -x509 -days 3650 -key proxy-ca.key -out proxy-ca.crt
```

**Configure SSL bump**:
```squid
http_port 3128 ssl-bump     cert=/etc/squid/proxy-ca.pem     generate-host-certificates=on     dynamic_cert_mem_cache_size=16MB

acl sensitive_sites ssl::server_name_regex "/etc/squid/sensitive_sites.txt"
ssl_bump splice sensitive_sites
ssl_bump peek step1 all
ssl_bump bump step2 all
```

## Bypass Prevention

```bash
# iptables rules
iptables -A FORWARD -s 10.1.0.40 -j ACCEPT  # Allow proxy server
iptables -A FORWARD -p tcp --dport 80 -j REJECT
iptables -A FORWARD -p tcp --dport 443 -j REJECT
iptables -A FORWARD -d 10.1.0.40 -p tcp --dport 3128 -j ACCEPT
```

---

# Load Balancer Security

## Service Overview

**Purpose**: Distributes traffic across backend servers  
**Security Focus**: SSL termination, session security, DDoS mitigation  
**Common Implementations**: HAProxy, NGINX, F5 BIG-IP, AWS ELB/ALB  
**Attack Vectors**: SSL attacks, session hijacking, backend discovery  

## SSL/TLS Termination

**HAProxy Configuration**:
```haproxy
frontend https-in
    bind *:443 ssl crt /etc/haproxy/certs/example.com.pem alpn h2,http/1.1
    
    http-response set-header Strict-Transport-Security "max-age=31536000"
    http-response set-header X-Frame-Options "SAMEORIGIN"
    http-response set-header X-Content-Type-Options "nosniff"
    
    stick-table type ip size 100k expire 30s store http_req_rate(10s)
    http-request track-sc0 src
    http-request deny deny_status 429 if { sc_http_req_rate(0) gt 100 }
    
    default_backend webservers

backend webservers
    balance roundrobin
    option httpchk GET /health
    server web01 10.1.20.10:80 check
    server web02 10.1.20.11:80 check
```

## Session Persistence

```haproxy
backend webservers
    balance roundrobin
    cookie SERVERID insert indirect nocache
    server web01 10.1.20.10:80 check cookie web01
    server web02 10.1.20.11:80 check cookie web02
```

## Health Checks

```haproxy
backend webservers
    option httpchk GET /health HTTP/1.1\r\nHost:\ example.com
    http-check expect status 200
    http-check expect string "OK"
    server web01 10.1.20.10:80 check inter 5s rise 2 fall 3
```

---

# RADIUS/TACACS+ (AAA Services) Security

## Service Overview

**Purpose**: Centralized authentication, authorization, accounting  
**Security Focus**: Shared secret protection, encrypted communication  
**Common Implementations**: FreeRADIUS, Cisco ISE, Microsoft NPS  
**Attack Vectors**: Shared secret compromise, replay attacks  

## FreeRADIUS Configuration

```radius
# /etc/freeradius/3.0/clients.conf
client switch-core-01 {
    ipaddr = 10.1.0.1
    secret = Str0ngS3cr3t!ABC123
    require_message_authenticator = yes
    nastype = cisco
}

# /etc/freeradius/3.0/mods-available/ldap
ldap {
    server = 'ldap.example.com'
    identity = 'cn=radius,ou=services,dc=example,dc=com'
    password = 'password'
    base_dn = 'ou=users,dc=example,dc=com'
    user {
        filter = "(uid=%{User-Name})"
    }
}
```

## Network Device Configuration

**Cisco IOS**:
```cisco
radius server RADIUS-01
 address ipv4 10.1.0.30 auth-port 1812
 key Str0ngS3cr3t!ABC123

aaa new-model
aaa authentication login default group radius local
aaa authorization exec default group radius local
aaa accounting exec default start-stop group radius
```

## TACACS+ Command Authorization

```tacacs
# /etc/tacacs+/tac_plus.conf
key = TAC@C$S3cr3tK3y!2026

user = netadmin {
    login = PAM
    member = admin-group
}

group = admin-group {
    default service = permit
    service = exec {
        priv-lvl = 15
    }
    cmd = show { permit .* }
    cmd = configure { permit .* }
}
```

---

# SNMP (Simple Network Management Protocol) Security

## Service Overview

**Purpose**: Network monitoring and management  
**Security Focus**: SNMPv3 authentication/encryption, access control  
**Common Implementations**: net-snmp, Cisco/Juniper embedded SNMP  
**Attack Vectors**: Community string exposure (v1/v2c), amplification attacks  

## SNMPv3 Configuration

**Linux (net-snmp)**:
```snmp
# /etc/snmp/snmpd.conf
createUser snmpuser SHA authPassword AES privPassword
rouser snmpuser authPriv

restrict default kod nomodify notrap nopeer noquery
restrict 10.0.0.0 mask 255.0.0.0 nomodify notrap nopeer
```

**Cisco IOS**:
```cisco
snmp-server group SNMPV3-GROUP v3 priv
snmp-server user snmpuser SNMPV3-GROUP v3 auth sha authPassword priv aes 128 privPassword
no snmp-server community public
no snmp-server community private
```

## SNMP Testing

```bash
# SNMPv3 query (should work)
snmpget -v3 -l authPriv -u snmpuser -a SHA -A authPassword -x AES -X privPassword 10.1.0.50 sysDescr.0

# SNMPv2c query (should fail)
snmpget -v2c -c public 10.1.0.50 sysDescr.0
# Expected: Timeout
```

---

# Syslog Security

## Service Overview

**Purpose**: Centralized log collection and storage  
**Security Focus**: Encrypted transmission, log integrity, retention  
**Common Implementations**: rsyslog, syslog-ng, Splunk  
**Attack Vectors**: Log injection, eavesdropping, tampering  

## TLS-Encrypted Syslog

**rsyslog Server**:
```rsyslog
# /etc/rsyslog.d/tls.conf
$ModLoad imtcp
$DefaultNetstreamDriver gtls
$DefaultNetstreamDriverCAFile /etc/ssl/certs/ca-cert.pem
$DefaultNetstreamDriverCertFile /etc/ssl/certs/syslog-server.pem
$DefaultNetstreamDriverKeyFile /etc/ssl/private/syslog-server.key
$InputTCPServerStreamDriverMode 1
$InputTCPServerStreamDriverAuthMode x509/name
$InputTCPServerRun 6514
```

**rsyslog Client**:
```rsyslog
$DefaultNetstreamDriverCAFile /etc/ssl/certs/ca-cert.pem
*.* @@(o)syslog.example.com:6514
```

## Log Retention and Rotation

```logrotate
# /etc/logrotate.d/rsyslog
/var/log/syslog {
    rotate 90
    daily
    missingok
    compress
    delaycompress
    notifempty
    postrotate
        /usr/lib/rsyslog/rsyslog-rotate
    endscript
}
```

## Log Analysis

```bash
# Top log sources
cat /var/log/syslog | awk '{print $4}' | sort | uniq -c | sort -rn | head -20

# Authentication failures
grep "authentication failure" /var/log/auth.log

# Failed login attempts
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn
```

---

# Service Integration and Testing

## Integration with A.8.20 (Network Security)

- Services run on network devices discovered in IMP-S1
- Service configurations align with device hardening (IMP-S3)


## Integration with A.8.22 (Network Segregation)

- Services deployed in appropriate security zones
- Inter-zone service access controlled by firewalls


## Integration with Other Controls

- **A.8.15 (Logging)**: All services must log
- **A.8.16 (Monitoring)**: Services monitored for availability
- **A.8.8 (Vulnerability Management)**: Services patched regularly


## Security Testing Matrix

| Service | Test | Expected Result |
|---------|------|-----------------|
| DNS | DNSSEC validation | dig +dnssec returns RRSIG records |
| DNS | Rate limiting | Rapid queries rate limited |
| DHCP | Rogue server detection | DHCP snooping blocks rogue offers |
| NTP | Time sync accuracy | Offset < 50ms |
| Proxy | Authentication | Unauthenticated requests denied |
| Proxy | SSL inspection | HTTPS sites accessible with proxy CA |
| Load Balancer | Health checks | Failed backends removed from pool |
| RADIUS | Authentication | radtest succeeds with valid credentials |
| TACACS+ | Command authorization | Restricted users denied config commands |
| SNMP | SNMPv3 works | v3 queries succeed |
| SNMP | v1/v2c disabled | v2c queries fail/timeout |
| Syslog | TLS encryption | tcpdump shows encrypted traffic |
| Syslog | Log retention | Logs rotated per schedule |

---

# Common Pitfalls and Solutions

## DNS

- **DNSSEC validation failures** → Verify DS record published, check clock sync
- **Split DNS misconfiguration** → Verify forwarders in internal view


## DHCP

- **IP exhaustion** → Monitor utilization, increase scope size
- **Rogue DHCP not detected** → Enable DHCP snooping on all switches


## NTP

- **Time drift** → Ensure redundant NTP servers, verify connectivity
- **Authentication failures** → Check key ID matches, verify key value identical


## Proxy

- **SSL inspection breaks apps** → Exempt pinned domains, deploy proxy CA
- **Users bypass proxy** → Implement firewall rules, transparent proxy


## Load Balancer

- **False health check failures** → Adjust intervals/thresholds
- **SSL/TLS grade low** → Update cipher suites, disable TLS 1.0/1.1


## AAA

- **RADIUS auth fails** → Verify shared secret, check LDAP integration
- **TACACS+ authorization inconsistent** → Review tac_plus.conf syntax


## SNMP

- **SNMPv3 auth failures** → Verify username, auth password, priv password
- **v1/v2c still enabled** → Explicitly disable community strings


## Syslog

- **Logs not reaching server** → Check firewall allows port, verify rsyslog running
- **TLS connection fails** → Verify certificates valid, CA deployed


---

# Documentation Requirements

## Service Inventory
Each service must have:

- Service name, purpose, hosting location
- IP addresses, DNS names
- Criticality classification
- Service owner/responsible team
- Integration dependencies


## Configuration Documentation

- Security configuration details
- Configuration backup location/schedule
- Configuration baseline
- Change management process


## Access Credentials

- Service accounts (username, purpose, permissions)
- Shared secrets (stored securely encrypted)
- Certificate information (issuer, expiry)
- Credential rotation schedule


## Monitoring Documentation

- Health check configuration
- Alerting thresholds
- Performance baselines
- Monitoring tool integration


## Backup and Recovery

- Configuration backup procedures
- Service recovery procedures
- RTO/RPO


---

# Metrics and Continuous Improvement

## Service Metrics

- **DNS**: Query volume, DNSSEC validation rate, response time
- **DHCP**: Scope utilization %, lease conflicts, rogue detections
- **NTP**: Time offset, stratum level, peer reachability
- **Proxy**: User count, bandwidth per user, blocked requests
- **Load Balancer**: Backend health, request rate, error rate
- **AAA**: Auth success/failure rate, command denials
- **SNMP**: Query volume, auth failures
- **Syslog**: Log volume, disk utilization, TLS failures


## Review Schedule

- **Quarterly**: Review security configs, update threat intelligence
- **Annually**: Review architecture, update documentation
- **After incidents**: Root cause analysis, update procedures


---

# Service Security Checklist

| Service | Control | Status |
|---------|---------|--------|
| DNS | DNSSEC enabled | ☐ |
| DNS | Split DNS configured | ☐ |
| DNS | Rate limiting enabled | ☐ |
| DNS | Query logging enabled | ☐ |
| DHCP | DHCP snooping enabled | ☐ |
| DHCP | Scope monitoring | ☐ |
| NTP | Authentication enabled | ☐ |
| NTP | Access control configured | ☐ |
| Proxy | Authentication required | ☐ |
| Proxy | SSL inspection enabled | ☐ |
| Proxy | Bypass prevention (firewall) | ☐ |
| Load Balancer | SSL termination (strong ciphers) | ☐ |
| Load Balancer | Health checks enabled | ☐ |
| RADIUS | Shared secrets strong | ☐ |
| RADIUS | LDAP integration | ☐ |
| TACACS+ | Command authorization | ☐ |
| SNMP | SNMPv3 only | ☐ |
| SNMP | v1/v2c disabled | ☐ |
| Syslog | TLS encryption | ☐ |
| Syslog | 90+ day retention | ☐ |

---

# Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Organization] ISMS Team | Initial comprehensive release |

---

**END OF DOCUMENT**

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

# Purpose and Scope

## Purpose
This document provides **service-by-service security implementation guidance** for network services as required by ISO 27001:2022 Control A.8.21 (Security of Network Services). Each critical network service requires specific security configurations to protect confidentiality, integrity, and availability.

## Scope
This guidance covers implementation security for:

- **DNS** (Domain Name System): Authoritative and recursive DNS servers
- **DHCP** (Dynamic Host Configuration Protocol): IP address management
- **NTP** (Network Time Protocol): Time synchronization
- **Proxy Services**: Web proxies and content filtering
- **Load Balancers**: Application delivery and SSL/TLS termination
- **AAA Services**: RADIUS and TACACS+ authentication
- **SNMP** (Simple Network Management Protocol): Network management
- **Syslog**: Centralized logging


## Target Audience

- Network services administrators
- Security engineers
- ISMS implementation teams
- Service owners responsible for network infrastructure


## Prerequisites

- Administrative access to network services
- Understanding of service architecture (authoritative vs. recursive, centralized vs. distributed)
- Configuration backup capabilities
- Testing environment (recommended for validation before production deployment)


---

# Overview of Service Security

Each network service in this document follows a consistent implementation pattern:

1. **Service Overview**: Purpose and security focus
2. **Security Implementation**: Step-by-step configuration with examples
3. **Configuration Examples**: Multiple platforms where relevant (BIND, Unbound, Cisco, Juniper, etc.)
4. **Monitoring & Alerting**: Health checks and performance monitoring
5. **Security Testing**: Validation procedures
6. **Troubleshooting**: Common issues and solutions
7. **Integration Points**: How service integrates with other ISMS controls

This structured approach ensures consistent security implementation across all network services.

---

# DNS (Domain Name System) Security

## Service Overview

**Purpose**: DNS resolves domain names to IP addresses - fundamental internet service  
**Security Focus**: Authenticity (DNSSEC), integrity, availability, privacy  
**Common Implementations**: BIND9, Unbound, PowerDNS, Windows DNS Server  
**Attack Vectors**: DNS spoofing, cache poisoning, amplification attacks, tunneling  

## DNSSEC Implementation

DNSSEC (DNS Security Extensions) cryptographically signs DNS records to prevent spoofing.

**BIND9 DNSSEC Configuration**:

Step 1: Generate keys
```bash
cd /etc/bind/keys
dnssec-keygen -a RSASHA256 -b 2048 -n ZONE example.com  # ZSK
dnssec-keygen -a RSASHA256 -b 4096 -f KSK -n ZONE example.com  # KSK
```

Step 2: Sign zone
```bash
dnssec-signzone -A -3 $(head -c 1000 /dev/random | sha1sum | cut -b 1-16)   -N INCREMENT -o example.com -t /var/lib/bind/db.example.com
```

Step 3: Configure named
```bind
zone "example.com" {
    type master;
    file "/var/lib/bind/db.example.com.signed";
    auto-dnssec maintain;
    inline-signing yes;
};
```

Step 4: Publish DS record to parent zone
```bash
dnssec-dsfromkey Kexample.com.+008+12345.key
# Provide to registrar
```

## Split DNS Architecture

Separates internal and external DNS resolution.

```bind
acl "internal-networks" {
    10.0.0.0/8;
    172.16.0.0/12;
    192.168.0.0/16;
};

view "internal" {
    match-clients { internal-networks; };
    zone "example.com" {
        type master;
        file "/etc/bind/internal/db.example.com.internal";
    };
    recursion yes;
    forwarders { 8.8.8.8; 8.8.4.4; };
};

view "external" {
    match-clients { any; };
    zone "example.com" {
        type master;
        file "/etc/bind/external/db.example.com.external";
    };
    recursion no;
};
```

## DNS Rate Limiting

```bind
rate-limit {
    responses-per-second 10;
    window 15;
    log-only no;
    exempt-clients { 10.1.0.0/24; };
};
```

## DNS Query Logging

```bind
logging {
    channel query_log {
        file "/var/log/bind/query.log" versions 5 size 50m;
        severity info;
        print-time yes;
    };
    category queries { query_log; };
};
```

## DNS Security Testing

```bash
# DNSSEC validation
dig +dnssec +multi example.com

# Test rate limiting
for i in {1..100}; do dig example.com @dns-server & done

# Check for open recursion (should fail)
dig google.com @public-dns-ip
```

---

# DHCP (Dynamic Host Configuration Protocol) Security

## Service Overview

**Purpose**: Dynamically assigns IP addresses to network clients  
**Security Focus**: Rogue server prevention, availability, configuration integrity  
**Common Implementations**: ISC DHCP, Windows DHCP Server, Infoblox  
**Attack Vectors**: Rogue DHCP servers, DHCP starvation, man-in-the-middle  

## DHCP Snooping (Switch-Level Protection)

**Cisco IOS Configuration**:
```cisco
ip dhcp snooping
ip dhcp snooping vlan 10,20,30

interface GigabitEthernet0/24
 description Uplink to DHCP server
 ip dhcp snooping trust

interface range GigabitEthernet0/1-23
 ip dhcp snooping limit rate 10
```

## DHCP Server Hardening

**ISC DHCP Configuration**:
```dhcp
authoritative;
default-lease-time 86400;      # 24 hours
max-lease-time 604800;         # 7 days

subnet 10.1.10.0 netmask 255.255.255.0 {
    range 10.1.10.100 10.1.10.200;
    option routers 10.1.10.1;
    option domain-name-servers 10.1.0.10, 10.1.0.11;
    option ntp-servers 10.1.0.30;
    log-facility local7;
}

host server01 {
    hardware ethernet 00:11:22:33:44:55;
    fixed-address 10.1.10.50;
}
```

## DHCP Scope Management

Proper scope sizing prevents exhaustion:
```
Scope size = (Peak devices * 1.2) + Growth buffer

Example:
Peak: 250 devices
Buffer: 20%
Total: 250 * 1.2 = 300 IPs needed
```

## Rogue DHCP Detection

```bash
# Active testing
sudo dhclient -v eth0
# Look for multiple DHCPOFFER packets from different IPs

# Passive monitoring
sudo tcpdump -i eth0 -n port 67 or port 68
```

---

# NTP (Network Time Protocol) Security

## Service Overview

**Purpose**: Synchronizes system clocks across network  
**Security Focus**: Time source integrity, authentication, availability  
**Common Implementations**: ntpd, chronyd, Windows Time Service  
**Attack Vectors**: Time manipulation, DDoS amplification  

## NTP Authentication

```ntp
# /etc/ntp.keys

1 M a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6


# /etc/ntp.conf (server)
keys /etc/ntp.keys
trustedkey 1
requestkey 1
controlkey 1

server 0.pool.ntp.org iburst
server 1.pool.ntp.org iburst

# /etc/ntp.conf (client)
keys /etc/ntp.keys
trustedkey 1
requestkey 1
server ntp-01.example.com key 1 iburst prefer
```

## NTP Access Control

```ntp
restrict default kod nomodify notrap nopeer noquery
restrict -6 default kod nomodify notrap nopeer noquery
restrict 127.0.0.1
restrict ::1
restrict 10.0.0.0 mask 255.0.0.0 nomodify notrap nopeer
```

## NTP Monitoring

```bash
# Check sync status
ntpq -p

# Check offset
ntpq -p | grep '^\*' | awk '{print $9}'
# Acceptable: < 50ms
# Warning: 50-100ms
# Critical: > 100ms
```

---

# Proxy Service Security

## Service Overview

**Purpose**: Centralizes web access control and content filtering  
**Security Focus**: Authentication, SSL inspection, bypass prevention  
**Common Implementations**: Squid, Blue Coat, Zscaler, Microsoft Forefront  
**Attack Vectors**: Authentication bypass, certificate trust issues, proxy chaining  

## Proxy Authentication (LDAP)

```squid
# /etc/squid/squid.conf
auth_param basic program /usr/lib/squid/basic_ldap_auth     -b "ou=users,dc=example,dc=com"     -D "cn=squid,ou=services,dc=example,dc=com"     -w "password"     -f "uid=%s"     -h ldap.example.com

auth_param basic children 5
auth_param basic realm Proxy Authentication

acl authenticated proxy_auth REQUIRED
http_access allow authenticated
http_access deny all
```

## SSL/TLS Inspection

**Generate CA certificate**:
```bash
openssl req -new -x509 -days 3650 -key proxy-ca.key -out proxy-ca.crt
```

**Configure SSL bump**:
```squid
http_port 3128 ssl-bump     cert=/etc/squid/proxy-ca.pem     generate-host-certificates=on     dynamic_cert_mem_cache_size=16MB

acl sensitive_sites ssl::server_name_regex "/etc/squid/sensitive_sites.txt"
ssl_bump splice sensitive_sites
ssl_bump peek step1 all
ssl_bump bump step2 all
```

## Bypass Prevention

```bash
# iptables rules
iptables -A FORWARD -s 10.1.0.40 -j ACCEPT  # Allow proxy server
iptables -A FORWARD -p tcp --dport 80 -j REJECT
iptables -A FORWARD -p tcp --dport 443 -j REJECT
iptables -A FORWARD -d 10.1.0.40 -p tcp --dport 3128 -j ACCEPT
```

---

# Load Balancer Security

## Service Overview

**Purpose**: Distributes traffic across backend servers  
**Security Focus**: SSL termination, session security, DDoS mitigation  
**Common Implementations**: HAProxy, NGINX, F5 BIG-IP, AWS ELB/ALB  
**Attack Vectors**: SSL attacks, session hijacking, backend discovery  

## SSL/TLS Termination

**HAProxy Configuration**:
```haproxy
frontend https-in
    bind *:443 ssl crt /etc/haproxy/certs/example.com.pem alpn h2,http/1.1
    
    http-response set-header Strict-Transport-Security "max-age=31536000"
    http-response set-header X-Frame-Options "SAMEORIGIN"
    http-response set-header X-Content-Type-Options "nosniff"
    
    stick-table type ip size 100k expire 30s store http_req_rate(10s)
    http-request track-sc0 src
    http-request deny deny_status 429 if { sc_http_req_rate(0) gt 100 }
    
    default_backend webservers

backend webservers
    balance roundrobin
    option httpchk GET /health
    server web01 10.1.20.10:80 check
    server web02 10.1.20.11:80 check
```

## Session Persistence

```haproxy
backend webservers
    balance roundrobin
    cookie SERVERID insert indirect nocache
    server web01 10.1.20.10:80 check cookie web01
    server web02 10.1.20.11:80 check cookie web02
```

## Health Checks

```haproxy
backend webservers
    option httpchk GET /health HTTP/1.1\r\nHost:\ example.com
    http-check expect status 200
    http-check expect string "OK"
    server web01 10.1.20.10:80 check inter 5s rise 2 fall 3
```

---

# RADIUS/TACACS+ (AAA Services) Security

## Service Overview

**Purpose**: Centralized authentication, authorization, accounting  
**Security Focus**: Shared secret protection, encrypted communication  
**Common Implementations**: FreeRADIUS, Cisco ISE, Microsoft NPS  
**Attack Vectors**: Shared secret compromise, replay attacks  

## FreeRADIUS Configuration

```radius
# /etc/freeradius/3.0/clients.conf
client switch-core-01 {
    ipaddr = 10.1.0.1
    secret = Str0ngS3cr3t!ABC123
    require_message_authenticator = yes
    nastype = cisco
}

# /etc/freeradius/3.0/mods-available/ldap
ldap {
    server = 'ldap.example.com'
    identity = 'cn=radius,ou=services,dc=example,dc=com'
    password = 'password'
    base_dn = 'ou=users,dc=example,dc=com'
    user {
        filter = "(uid=%{User-Name})"
    }
}
```

## Network Device Configuration

**Cisco IOS**:
```cisco
radius server RADIUS-01
 address ipv4 10.1.0.30 auth-port 1812
 key Str0ngS3cr3t!ABC123

aaa new-model
aaa authentication login default group radius local
aaa authorization exec default group radius local
aaa accounting exec default start-stop group radius
```

## TACACS+ Command Authorization

```tacacs
# /etc/tacacs+/tac_plus.conf
key = TAC@C$S3cr3tK3y!2026

user = netadmin {
    login = PAM
    member = admin-group
}

group = admin-group {
    default service = permit
    service = exec {
        priv-lvl = 15
    }
    cmd = show { permit .* }
    cmd = configure { permit .* }
}
```

---

# SNMP (Simple Network Management Protocol) Security

## Service Overview

**Purpose**: Network monitoring and management  
**Security Focus**: SNMPv3 authentication/encryption, access control  
**Common Implementations**: net-snmp, Cisco/Juniper embedded SNMP  
**Attack Vectors**: Community string exposure (v1/v2c), amplification attacks  

## SNMPv3 Configuration

**Linux (net-snmp)**:
```snmp
# /etc/snmp/snmpd.conf
createUser snmpuser SHA authPassword AES privPassword
rouser snmpuser authPriv

restrict default kod nomodify notrap nopeer noquery
restrict 10.0.0.0 mask 255.0.0.0 nomodify notrap nopeer
```

**Cisco IOS**:
```cisco
snmp-server group SNMPV3-GROUP v3 priv
snmp-server user snmpuser SNMPV3-GROUP v3 auth sha authPassword priv aes 128 privPassword
no snmp-server community public
no snmp-server community private
```

## SNMP Testing

```bash
# SNMPv3 query (should work)
snmpget -v3 -l authPriv -u snmpuser -a SHA -A authPassword -x AES -X privPassword 10.1.0.50 sysDescr.0

# SNMPv2c query (should fail)
snmpget -v2c -c public 10.1.0.50 sysDescr.0
# Expected: Timeout
```

---

# Syslog Security

## Service Overview

**Purpose**: Centralized log collection and storage  
**Security Focus**: Encrypted transmission, log integrity, retention  
**Common Implementations**: rsyslog, syslog-ng, Splunk  
**Attack Vectors**: Log injection, eavesdropping, tampering  

## TLS-Encrypted Syslog

**rsyslog Server**:
```rsyslog
# /etc/rsyslog.d/tls.conf
$ModLoad imtcp
$DefaultNetstreamDriver gtls
$DefaultNetstreamDriverCAFile /etc/ssl/certs/ca-cert.pem
$DefaultNetstreamDriverCertFile /etc/ssl/certs/syslog-server.pem
$DefaultNetstreamDriverKeyFile /etc/ssl/private/syslog-server.key
$InputTCPServerStreamDriverMode 1
$InputTCPServerStreamDriverAuthMode x509/name
$InputTCPServerRun 6514
```

**rsyslog Client**:
```rsyslog
$DefaultNetstreamDriverCAFile /etc/ssl/certs/ca-cert.pem
*.* @@(o)syslog.example.com:6514
```

## Log Retention and Rotation

```logrotate
# /etc/logrotate.d/rsyslog
/var/log/syslog {
    rotate 90
    daily
    missingok
    compress
    delaycompress
    notifempty
    postrotate
        /usr/lib/rsyslog/rsyslog-rotate
    endscript
}
```

## Log Analysis

```bash
# Top log sources
cat /var/log/syslog | awk '{print $4}' | sort | uniq -c | sort -rn | head -20

# Authentication failures
grep "authentication failure" /var/log/auth.log

# Failed login attempts
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn
```

---

# Service Integration and Testing

## Integration with A.8.20 (Network Security)

- Services run on network devices discovered in IMP-S1
- Service configurations align with device hardening (IMP-S3)


## Integration with A.8.22 (Network Segregation)

- Services deployed in appropriate security zones
- Inter-zone service access controlled by firewalls


## Integration with Other Controls

- **A.8.15 (Logging)**: All services must log
- **A.8.16 (Monitoring)**: Services monitored for availability
- **A.8.8 (Vulnerability Management)**: Services patched regularly


## Security Testing Matrix

| Service | Test | Expected Result |
|---------|------|-----------------|
| DNS | DNSSEC validation | dig +dnssec returns RRSIG records |
| DNS | Rate limiting | Rapid queries rate limited |
| DHCP | Rogue server detection | DHCP snooping blocks rogue offers |
| NTP | Time sync accuracy | Offset < 50ms |
| Proxy | Authentication | Unauthenticated requests denied |
| Proxy | SSL inspection | HTTPS sites accessible with proxy CA |
| Load Balancer | Health checks | Failed backends removed from pool |
| RADIUS | Authentication | radtest succeeds with valid credentials |
| TACACS+ | Command authorization | Restricted users denied config commands |
| SNMP | SNMPv3 works | v3 queries succeed |
| SNMP | v1/v2c disabled | v2c queries fail/timeout |
| Syslog | TLS encryption | tcpdump shows encrypted traffic |
| Syslog | Log retention | Logs rotated per schedule |

---

# Common Pitfalls and Solutions

## DNS

- **DNSSEC validation failures** → Verify DS record published, check clock sync
- **Split DNS misconfiguration** → Verify forwarders in internal view


## DHCP

- **IP exhaustion** → Monitor utilization, increase scope size
- **Rogue DHCP not detected** → Enable DHCP snooping on all switches


## NTP

- **Time drift** → Ensure redundant NTP servers, verify connectivity
- **Authentication failures** → Check key ID matches, verify key value identical


## Proxy

- **SSL inspection breaks apps** → Exempt pinned domains, deploy proxy CA
- **Users bypass proxy** → Implement firewall rules, transparent proxy


## Load Balancer

- **False health check failures** → Adjust intervals/thresholds
- **SSL/TLS grade low** → Update cipher suites, disable TLS 1.0/1.1


## AAA

- **RADIUS auth fails** → Verify shared secret, check LDAP integration
- **TACACS+ authorization inconsistent** → Review tac_plus.conf syntax


## SNMP

- **SNMPv3 auth failures** → Verify username, auth password, priv password
- **v1/v2c still enabled** → Explicitly disable community strings


## Syslog

- **Logs not reaching server** → Check firewall allows port, verify rsyslog running
- **TLS connection fails** → Verify certificates valid, CA deployed


---

# Documentation Requirements

## Service Inventory
Each service must have:

- Service name, purpose, hosting location
- IP addresses, DNS names
- Criticality classification
- Service owner/responsible team
- Integration dependencies


## Configuration Documentation

- Security configuration details
- Configuration backup location/schedule
- Configuration baseline
- Change management process


## Access Credentials

- Service accounts (username, purpose, permissions)
- Shared secrets (stored securely encrypted)
- Certificate information (issuer, expiry)
- Credential rotation schedule


## Monitoring Documentation

- Health check configuration
- Alerting thresholds
- Performance baselines
- Monitoring tool integration


## Backup and Recovery

- Configuration backup procedures
- Service recovery procedures
- RTO/RPO


---

# Metrics and Continuous Improvement

## Service Metrics

- **DNS**: Query volume, DNSSEC validation rate, response time
- **DHCP**: Scope utilization %, lease conflicts, rogue detections
- **NTP**: Time offset, stratum level, peer reachability
- **Proxy**: User count, bandwidth per user, blocked requests
- **Load Balancer**: Backend health, request rate, error rate
- **AAA**: Auth success/failure rate, command denials
- **SNMP**: Query volume, auth failures
- **Syslog**: Log volume, disk utilization, TLS failures


## Review Schedule

- **Quarterly**: Review security configs, update threat intelligence
- **Annually**: Review architecture, update documentation
- **After incidents**: Root cause analysis, update procedures


---

# Service Security Checklist

| Service | Control | Status |
|---------|---------|--------|
| DNS | DNSSEC enabled | ☐ |
| DNS | Split DNS configured | ☐ |
| DNS | Rate limiting enabled | ☐ |
| DNS | Query logging enabled | ☐ |
| DHCP | DHCP snooping enabled | ☐ |
| DHCP | Scope monitoring | ☐ |
| NTP | Authentication enabled | ☐ |
| NTP | Access control configured | ☐ |
| Proxy | Authentication required | ☐ |
| Proxy | SSL inspection enabled | ☐ |
| Proxy | Bypass prevention (firewall) | ☐ |
| Load Balancer | SSL termination (strong ciphers) | ☐ |
| Load Balancer | Health checks enabled | ☐ |
| RADIUS | Shared secrets strong | ☐ |
| RADIUS | LDAP integration | ☐ |
| TACACS+ | Command authorization | ☐ |
| SNMP | SNMPv3 only | ☐ |
| SNMP | v1/v2c disabled | ☐ |
| Syslog | TLS encryption | ☐ |
| Syslog | 90+ day retention | ☐ |

---

# Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Organization] ISMS Team | Initial comprehensive release |

---

**END OF SPECIFICATION**

---

*"People are always selling the idea that people with mental illness are suffering. I think madness can be an escape."*
— John Nash
*Where bamboo antennas actually work.* 🎋
