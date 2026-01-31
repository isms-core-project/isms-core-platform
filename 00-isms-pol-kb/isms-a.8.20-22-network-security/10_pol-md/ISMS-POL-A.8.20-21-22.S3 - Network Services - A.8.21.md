# ISMS-POL-A.8.20-21-22-S3
## Network Services Security Requirements (A.8.21)

**Document ID**: ISMS-POL-A.8.20-21-22-S3  
**Title**: Network Services Security Requirements (ISO/IEC 27001:2022 Control A.8.21)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Network Security Manager | Initial network services security requirements (A.8.21) |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Network Operations Manager
- Service Review: Service Owners

**Distribution**: Network team, service administrators, security team, IT operations, auditors  
**Related Documents**: ISMS-POL-A.8.20-21-22 (Master), ISMS-POL-A.8.20-21-22-S2 (A.8.20)

---

## 1. Control Objective and Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.21

**Official Control Text**:

> *Security mechanisms, service levels and service requirements of network services should be identified, implemented and monitored.*

**Control Purpose**: Ensure network services are secured, available, and monitored to support business operations while protecting against service-based attacks.

**Why This Matters**:

Network services (DNS, DHCP, NTP, proxy, load balancers, etc.) form critical infrastructure enabling network operations. Compromised or unavailable network services enable attackers to:
- **DNS attacks**: DNS poisoning, DNS hijacking, DNS tunneling for C2, data exfiltration
- **DHCP attacks**: Rogue DHCP servers, DHCP exhaustion, man-in-the-middle via malicious DHCP
- **NTP attacks**: Time manipulation affecting logging, certificates, authentication
- **Proxy attacks**: Bypass for data exfiltration, SSL/TLS downgrade attacks
- **Load balancer attacks**: DDoS amplification, session hijacking
- **Service disruption**: Denial-of-service causing business impact

Secure network services reduce these risks and provide reliable infrastructure.

### 1.2 Scope of A.8.21 Requirements

This section defines mandatory requirements for:

1. **Network Services Inventory**
2. **DNS Security**
3. **DHCP Security**
4. **NTP Security**
5. **Proxy Services Security**
6. **Load Balancer Security**
7. **Authentication Services Security**
8. **SNMP Security**
9. **Syslog Security**
10. **Service Availability and Monitoring**

---

## 2. Network Services Inventory

### 2.1 Requirement: Services Catalog

**REQ-A821-001**: [Organization] **MUST** maintain a comprehensive catalog of all network services.

**Services In-Scope**:
- DNS, DHCP, NTP, Proxy, Load Balancers, RADIUS, TACACS+, SNMP, Syslog, Email Security, VoIP/UC, others

**Catalog Attributes**: Service ID, type, location, owner, criticality, SLA, redundancy, monitoring status

**Audit Evidence**: Network services catalog (Workbook 3)

---

## 3. DNS Security

### 3.1 DNSSEC and Split DNS

**REQ-A821-002**: [Organization] **SHOULD** implement DNSSEC for authoritative zones.

**REQ-A821-003**: [Organization] **SHOULD** implement split DNS (internal/external separation).

### 3.2 DNS Logging and Filtering

**REQ-A821-004**: DNS services **MUST** log queries and integrate with SIEM.

**REQ-A821-005**: [Organization] **SHOULD** implement DNS filtering to block malicious domains.

### 3.3 DNS DDoS Protection

**REQ-A821-006**: Public DNS **MUST** implement rate limiting and DDoS protection.

---

## 4. DHCP Security

### 4.1 DHCP Snooping

**REQ-A821-007**: [Organization] **MUST** enable DHCP snooping on access switches (see A.8.20).

### 4.2 Rogue DHCP Detection

**REQ-A821-008**: [Organization] **MUST** implement rogue DHCP server detection.

### 4.3 DHCP Scope Management

**REQ-A821-009**: DHCP scopes **MUST** be documented and reviewed quarterly.

### 4.4 DHCP Redundancy

**REQ-A821-010**: Critical DHCP services **SHOULD** be configured for high availability.

---

## 5. NTP Security

### 5.1 NTP Authentication

**REQ-A821-011**: [Organization] **SHOULD** implement NTP authentication (NTS or symmetric keys).

### 5.2 NTP Stratum Hierarchy

**REQ-A821-012**: [Organization] **MUST** document NTP stratum hierarchy and authoritative time sources.

**Time Sources**:
- Stratum 1: GPS/atomic clock, NIST time servers, vendor time services
- Stratum 2: [Organization] internal NTP servers synchronized to Stratum 1
- Stratum 3+: Network devices and systems synchronized to Stratum 2

### 5.3 NTP Access Controls

**REQ-A821-013**: NTP servers **MUST** restrict queries to authorized sources (ACLs).

### 5.4 NTP Monitoring

**REQ-A821-014**: [Organization] **MUST** monitor time synchronization status and alert on drift >1 second.

---

## 6. Proxy Services Security

### 6.1 Proxy Authentication

**REQ-A821-015**: Web proxies **SHOULD** require authentication (user-based or device-based).

**Authentication Methods**:
- LDAP/Active Directory integration (preferred)
- Kerberos authentication
- Certificate-based authentication
- NTLM/Basic authentication (legacy, less secure)

### 6.2 SSL/TLS Interception

**REQ-A821-016**: If SSL/TLS interception is implemented, users **MUST** be notified per legal requirements.

**SSL/TLS Interception Considerations**:
- **Privacy**: User notification and consent required per FADP/GDPR
- **Certificate trust**: Root CA certificate must be deployed to all endpoints
- **Exclusions**: Financial, healthcare sites may require bypass for legal/regulatory reasons
- **Monitoring**: Log SSL/TLS interception events

### 6.3 Proxy Logging

**REQ-A821-017**: Proxy services **MUST** log all web access (URL, user, timestamp, action).

### 6.4 Proxy Bypass Prevention

**REQ-A821-018**: [Organization] **MUST** prevent proxy bypass (direct internet access without proxy).

**Bypass Prevention Methods**:
- Firewall rules blocking direct HTTP/HTTPS (force through proxy)
- Proxy Auto-Configuration (PAC) file deployment
- Web Proxy Auto-Discovery (WPAD)
- DNS-based enforcement

### 6.5 Proxy Redundancy

**REQ-A821-019**: Critical proxy services **SHOULD** be deployed in high-availability configuration.

---

## 7. Load Balancer Security

### 7.1 SSL/TLS Termination

**REQ-A821-020**: Load balancers performing SSL/TLS termination **MUST** use strong ciphers and TLS 1.2+.

**SSL/TLS Configuration**:
- TLS 1.2 minimum, TLS 1.3 preferred
- Strong cipher suites (AES-256, ChaCha20)
- Disable weak ciphers (DES, 3DES, RC4, MD5)
- Certificate management (valid certificates, expiration monitoring)
- Perfect Forward Secrecy (PFS) enabled

### 7.2 Session Management

**REQ-A821-021**: Load balancers **MUST** implement secure session persistence mechanisms.

**Session Persistence Methods**:
- Cookie-based persistence (preferred - insert mode)
- Source IP persistence (less preferred - potential privacy issues)
- SSL session ID persistence

**Session Security**:
- Encrypted session cookies
- Secure and HttpOnly cookie flags
- Session timeout configuration
- Session fixation protection

### 7.3 Health Checks

**REQ-A821-022**: Load balancers **MUST** perform health checks on backend servers.

**Health Check Requirements**:
- Application-layer health checks (HTTP GET, TCP connect, etc.)
- Frequency: Every 10-30 seconds
- Failure threshold: Remove unhealthy servers from pool after 3 consecutive failures
- Success threshold: Re-add healthy servers after 2 consecutive successes

### 7.4 DDoS Protection

**REQ-A821-023**: Load balancers **SHOULD** implement DDoS protection capabilities.

**DDoS Protection Features**:
- Rate limiting (requests per second per IP)
- Connection limits (concurrent connections per IP)
- Geographic filtering (block traffic from high-risk regions)
- SYN flood protection
- HTTP flood protection (challenge-response, JavaScript challenge)

### 7.5 Load Balancer Logging

**REQ-A821-024**: Load balancers **MUST** log all traffic (source, destination, timestamp, action).

### 7.6 Load Balancer Redundancy

**REQ-A821-025**: Critical load balancers **MUST** be deployed in high-availability configuration.

---

## 8. Authentication Services Security

### 8.1 RADIUS/TACACS+ Security

**REQ-A821-026**: RADIUS and TACACS+ services **MUST** use strong shared secrets.

**Shared Secret Requirements**:
- Minimum 20 characters (randomly generated)
- Changed every 90 days
- Unique secrets per network device (not reused)
- Encrypted storage of secrets

**REQ-A821-027**: RADIUS/TACACS+ servers **SHOULD** be deployed in high-availability configuration.

**REQ-A821-028**: RADIUS/TACACS+ **MUST** log all authentication attempts (successful and failed).

### 8.2 AAA Integration

**REQ-A821-029**: Network devices **SHOULD** authenticate against centralized AAA servers (see A.8.20).

---

## 9. SNMP Security

### 9.1 SNMPv3 Requirement

**REQ-A821-030**: [Organization] **MUST** use SNMPv3 with authentication and encryption.

**SNMPv1/v2c Prohibition**: SNMPv1 and SNMPv2c **MUST** be disabled (no encryption, weak authentication).

**SNMPv3 Configuration**:
- Security level: authPriv (authentication + encryption)
- Authentication: SHA-256 minimum
- Encryption: AES-256 minimum
- Unique credentials per device or device group

**REQ-A821-031**: SNMP access **MUST** be restricted to authorized management systems (ACLs).

**REQ-A821-032**: SNMP **MUST** be read-only except for authorized configuration management systems.

---

## 10. Syslog Security

### 10.1 Centralized Logging

**REQ-A821-033**: [Organization] **MUST** operate centralized syslog servers (see A.8.15).

### 10.2 Encrypted Syslog

**REQ-A821-034**: Syslog **SHOULD** be encrypted in transit (syslog over TLS).

**Syslog Encryption Methods**:
- Syslog over TLS (RFC 5425)
- Syslog over DTLS (for UDP-based syslog)

### 10.3 Syslog Integrity

**REQ-A821-035**: Syslog servers **SHOULD** implement log integrity protection (signing, immutable storage).

### 10.4 Syslog Redundancy

**REQ-A821-036**: Syslog infrastructure **SHOULD** be redundant (multiple syslog servers).

---

## 11. Service Availability and Performance

### 11.1 Service Level Agreements (SLAs)

**REQ-A821-037**: Critical network services **MUST** have defined SLAs.

**SLA Components**:
- **Availability target**: e.g., 99.9% uptime (8.76 hours downtime/year max)
- **Performance target**: e.g., DNS query response time <50ms, DHCP lease time <5 seconds
- **Mean Time to Repair (MTTR)**: e.g., <4 hours for critical services
- **Maintenance windows**: Defined downtime for patches/upgrades

**Criticality-Based SLAs**:
- **Critical services**: 99.99% availability (52 minutes downtime/year)
- **High services**: 99.9% availability (8.76 hours downtime/year)
- **Medium services**: 99.5% availability (1.83 days downtime/year)
- **Low services**: 99.0% availability (3.65 days downtime/year)

**REQ-A821-038**: SLA compliance **MUST** be measured and reported monthly.

### 11.2 Service Redundancy

**REQ-A821-039**: Critical and high-criticality services **MUST** be deployed with redundancy.

**Redundancy Models**:
- **Active-Passive**: Primary service active, standby ready to takeover
- **Active-Active**: Multiple services active simultaneously (load sharing)
- **N+1 Redundancy**: N active services + 1 standby
- **Geographic Redundancy**: Services in multiple physical locations

**Failover Testing**: Redundancy **MUST** be tested quarterly (planned failover drill).

### 11.3 Capacity Planning

**REQ-A821-040**: [Organization] **MUST** perform capacity planning for network services.

**Capacity Metrics**:
- **DNS**: Queries per second (QPS), cache hit rate
- **DHCP**: Lease utilization percentage, lease exhaustion risk
- **Proxy**: Concurrent connections, bandwidth utilization
- **Load Balancer**: Connections per second, backend server load

**Capacity Thresholds**:
- **Warning**: 70% capacity utilization
- **Critical**: 85% capacity utilization
- **Action**: Scale up/out before reaching 90% capacity

---

## 12. Service Monitoring and Alerting

### 12.1 Service Health Monitoring

**REQ-A821-041**: All network services **MUST** be monitored for availability and performance.

**Monitoring Methods**:
- Synthetic transactions (automated test queries)
- Service heartbeat checks (ping, TCP connect)
- Performance metrics collection (response time, throughput)
- Log analysis (error patterns, anomalies)

**Monitoring Tools**: Nagios, Zabbix, PRTG, SolarWinds, commercial monitoring platforms, cloud-native monitoring (AWS CloudWatch, Azure Monitor, GCP Monitoring)

### 12.2 Security Event Monitoring

**REQ-A821-042**: Network services **MUST** forward security events to SIEM (see A.8.16).

**Security Events to Monitor**:
- Authentication failures (repeated failed logins)
- Unauthorized access attempts
- Service abuse (DNS tunneling, DHCP exhaustion attempts)
- Configuration changes
- Service crashes or restarts
- Resource exhaustion (CPU, memory, disk)

### 12.3 Alerting

**REQ-A821-043**: Network services **MUST** generate alerts on critical events.

**Alerting Criteria**:
- Service unavailable (down status)
- Performance degradation (response time >3x baseline)
- Security events (authentication failures, unauthorized access)
- Capacity thresholds exceeded (>85% utilization)
- Configuration drift (unauthorized changes)

**Alert Routing**:
- Critical alerts: Immediate (SMS, phone call, PagerDuty)
- High alerts: 15-minute delay (email, Slack, Teams)
- Medium alerts: Hourly digest
- Low alerts: Daily digest

---

## 13. Service Hardening and Patching

### 13.1 Service-Specific Hardening

**REQ-A821-044**: Network services **MUST** be hardened per vendor-specific hardening guides.

**Hardening Sources**:
- CIS Benchmarks (where available)
- Vendor hardening guides (Microsoft DNS, BIND, ISC DHCP, etc.)
- Industry best practices

**Service Hardening Examples**:
- **BIND DNS**: Disable version disclosure, restrict zone transfers, rate limiting
- **Microsoft DNS**: Secure cache against pollution, disable recursion on authoritative servers
- **ISC DHCP**: Secure OMAPI, restrict lease queries
- **Squid Proxy**: Disable CONNECT to non-standard ports, implement ACLs
- **F5/NGINX Load Balancer**: Disable unnecessary modules, implement rate limiting

### 13.2 Service Patching

**REQ-A821-045**: Network services **MUST** be patched per vulnerability management policy (see A.8.8).

**Patching Schedule**:
- Critical vulnerabilities: 30 days
- High vulnerabilities: 90 days
- Medium/Low vulnerabilities: 180 days or risk-accepted

**Patch Testing**: Patches **MUST** be tested in non-production environment before production deployment.

---

## 14. Compliance Verification

### 14.1 Service Security Assessment

**REQ-A821-046**: Network services security (A.8.21) **MUST** be assessed for compliance.

**Assessment Methods**:
- Service inventory validation (quarterly)
- Service-specific security configuration audits (annual)
- Service availability reporting (monthly)
- Security testing (penetration testing annual)

**Assessment Outputs**:
- Network services catalog (Workbook 3)
- Service-specific security assessment tabs
- Compliance scoring (percentage of requirements met)
- Gap identification and remediation tracking

**Audit Evidence**: Assessment reports (Workbook 3), compliance scores, remediation plans

### 14.2 Non-Compliance Handling

**REQ-A821-047**: Network services non-compliance **MUST** be addressed through remediation or risk acceptance.

**Non-Compliance Response**: Same process as A.8.20 (risk assessment, remediation plan, risk acceptance if needed, CISO approval)

---

## 15. Summary of Requirements

**Total Requirements**: 47 (REQ-A821-001 through REQ-A821-047)

**Requirement Breakdown by Service**:
- Inventory: 1 requirement
- DNS: 6 requirements
- DHCP: 4 requirements
- NTP: 4 requirements
- Proxy: 5 requirements
- Load Balancer: 6 requirements
- Authentication Services: 4 requirements
- SNMP: 3 requirements
- Syslog: 4 requirements
- Availability & Monitoring: 8 requirements
- Hardening & Patching: 2 requirements

**Criticality Classification**:
- **MUST** requirements: 31 (mandatory)
- **SHOULD** requirements: 16 (strongly recommended, risk-based)

---

**END OF SECTION 3 (A.8.21)**

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Network Security Manager | Initial network services security requirements (A.8.21) |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**

**Next Document**: ISMS-POL-A.8.20-21-22-S4 (Network Segregation Requirements - A.8.22)
