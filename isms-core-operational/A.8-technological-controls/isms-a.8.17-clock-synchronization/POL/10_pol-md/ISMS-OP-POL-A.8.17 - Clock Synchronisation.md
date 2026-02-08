**ISMS-OP-POL-A.8.17 — Clock Synchronisation**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Clock Synchronisation |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.17 |
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

- ISO/IEC 27001:2022 Control A.8.17 — Clock synchronisation

**Related Annex A Controls**:

| Control | Relationship to Clock Synchronisation |
|---------|---------------------------------------|
| A.8.15 Logging | Accurate timestamps are a prerequisite for meaningful log records |
| A.8.16 Monitoring activities | Event correlation depends on synchronised clocks across systems |
| A.5.24–28 Incident management | Forensic investigation requires a consistent timeline across all systems |
| A.5.28 Collection of evidence | Clock accuracy underpins the legal admissibility of digital evidence |
| A.8.20 Network security | Network devices must be time-synchronised for security event correlation |

**Related Internal Policies**:

- Logging Policy (A.8.15)
- Monitoring Activities Policy (A.8.16)

- Incident Management Policy
- Network Security Policy

---

# Clock Synchronisation Policy

## Purpose

The purpose of this policy is to ensure the clocks of all relevant information processing systems within the organisation are synchronised to a single, consistent reference time source. Accurate and consistent timestamps are essential for log correlation, incident investigation, forensic evidence, regulatory compliance, and distributed system integrity.

This policy supports Swiss nFADP (revDSG) Art. 8 by maintaining data integrity through verifiable timestamping. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32 (security of processing) also applies. DSV Art. 4 logging obligations for sensitive personal data processing require accurate timestamps to ensure log integrity and traceability.

## Scope

This policy applies to all systems that generate log data or time-sensitive records, including:

- Servers and workstations (physical and virtual).
- Network infrastructure (routers, switches, firewalls, load balancers, wireless controllers).
- Security devices (IDS/IPS, EDR agents, access control systems).
- Cloud services and SaaS platforms.
- Database servers and application servers.
- Physical security systems (CCTV, badge readers) where integrated with IT logging.
- IoT and operational technology (OT) devices within the ISMS scope.

All employees and third-party users responsible for system administration or deployment are accountable for ensuring time synchronisation on systems they manage.

## Principle

All clocks shall synchronise to a single, organisationally approved reference time source. Time data shall be protected from unauthorised modification. Timestamps shall be recorded in a consistent format to enable reliable correlation across systems, locations, and service providers.

---

## Authoritative Time Sources

### Primary Reference

The organisation shall designate a primary authoritative time source:

| Attribute | Requirement |
|-----------|-------------|
| **Primary source** | METAS (Swiss Federal Institute of Metrology) NTP servers: `ntp.metas.ch`, `ntp11.metas.ch`, `ntp12.metas.ch`, `ntp13.metas.ch` — Stratum 1, traceable to UTC(CH) |
| **Secondary source** | Swiss NTP Pool: `0.ch.pool.ntp.org`, `1.ch.pool.ntp.org`, `2.ch.pool.ntp.org`, `3.ch.pool.ntp.org` |
| **Minimum sources** | Each internal time server shall synchronise to at least **two** independent external sources (per CIS Control 8.4) |
| **Traceability** | The primary source shall be traceable to a national metrology institute or GPS/GNSS time signal |

### Internal Time Architecture

The organisation shall deploy internal NTP servers in a tiered architecture:

| Tier | Role | Configuration |
|------|------|---------------|
| **Internal Stratum 2** | Primary internal NTP servers synchronised directly to external Stratum 1 sources (METAS) | Minimum 2 servers for redundancy; geographically separated where feasible |
| **Internal Stratum 3** | Site-level or department-level servers (optional for larger environments) | Synchronise to internal Stratum 2; serve local clients |
| **Clients** | All endpoints, application servers, network devices | Synchronise to internal Stratum 2 or Stratum 3 via NTP |

For small organisations: the primary domain controller or a designated internal server may serve as the sole internal NTP server, synchronised to at least two external sources.

Where the organisation operates GPS-disciplined oscillators (GPSDOs) for Stratum 0/1 independence (e.g., air-gapped networks), these shall be documented and maintained per manufacturer specifications.

---

## Synchronisation Protocol

### NTP Configuration

Network Time Protocol (NTP) shall be used for time synchronisation across all standard enterprise systems.

| Requirement | Specification |
|-------------|---------------|
| **Protocol** | NTPv4 (RFC 5905) minimum |
| **Security** | Network Time Security (NTS, RFC 8915) shall be enabled where supported by both client and server. Where NTS is not supported, NTP communication shall be restricted to approved servers via firewall rules or access control lists. |
| **Authentication** | NTP symmetric key authentication or NTS shall be used between internal servers and external sources |
| **Polling interval** | Default (64–1024 seconds); shorter intervals for critical systems if required |
| **Firewall rules** | Outbound NTP (UDP 123) permitted only to approved external sources; inbound NTP restricted to internal servers |

### Precision Time Protocol (PTP)

Where sub-microsecond accuracy is required (e.g., financial trading, industrial control, high-frequency data processing), IEEE 1588 Precision Time Protocol (PTPv2) shall be deployed:

- PTP-aware network switches (boundary or transparent clocks) are required.
- A PTP grandmaster clock (GPS-disciplined) shall be deployed.
- PTP is an addition to — not a replacement for — NTP across the general enterprise.

PTP applicability is determined during system design and documented in the system architecture.

---

## Timestamp Format

### Standard Format

All systems shall record timestamps in one of the following formats:

| Format | Example | Use Case |
|--------|---------|----------|
| **UTC** (preferred) | `2026-02-07T14:30:00Z` | Servers, databases, network devices, SIEM, all infrastructure |
| **Local time with UTC offset** | `2026-02-07T15:30:00+01:00` | Application logs, user-facing reports (where UTC is impractical) |

**Mandatory rules:**

- ISO 8601 / RFC 3339 format shall be used for all machine-generated timestamps.
- **UTC is the standard** for all infrastructure, logging, and security systems.
- Local time with explicit UTC offset is permitted only at the application/presentation layer.
- Local time **without** UTC offset (e.g., `15:30:00 CET`) is **not acceptable** — timezone abbreviations are ambiguous (CET/CEST transitions create duplicate hours).
- Named timezone abbreviations shall not be used in log timestamps.

### Daylight Saving Time

UTC eliminates daylight saving time (DST) ambiguity. During the autumn transition (CEST → CET), the hour 02:00–03:00 repeats. Systems using local time without offset cannot distinguish between the two occurrences. Systems recording in UTC are unaffected.

All systems shall use UTC or explicit offset to prevent DST-related timestamp ambiguity.

---

## Clock Drift Tolerances

### Maximum Acceptable Offset

Systems shall maintain clock accuracy within the following tolerances:

| System Tier | Maximum Offset | Monitoring Threshold | Action |
|-------------|---------------|---------------------|--------|
| **Critical** (authentication, SIEM, financial, databases) | < 1 ms | Alert at > 1 ms | Investigate and resynchronise immediately |
| **Standard enterprise** (servers, network devices) | < 50 ms | Alert at > 50 ms | Investigate within 4 hours |
| **General** (workstations, printers) | < 500 ms | Alert at > 500 ms | Resynchronise at next polling cycle |
| **Alarm** (any system) | > 128 ms | NTP step threshold | NTP client will step (jump) clock; log event |
| **Panic** (any system) | > 1000 seconds | NTP panic threshold | NTP daemon exits; manual intervention required |

### Drift Monitoring

Clock drift shall be monitored continuously using system monitoring tools (e.g., Prometheus, Nagios, CloudWatch, or equivalent):

- NTP offset, jitter, and stratum metrics shall be collected from all monitored systems.
- Alert on offset exceeding the system tier threshold.
- Alert on stratum changes (e.g., a server dropping from Stratum 2 to Stratum 16 indicates loss of upstream synchronisation).
- Clock drift alerts shall be forwarded to the centralised monitoring platform.
- Monthly trend analysis of clock drift across the estate.

---

## Cloud Service Time Synchronisation

### Provider-Specific Time Sources

Where systems run in cloud environments, the provider's time synchronisation service shall be used:

| Provider | Time Service | Access | Notes |
|----------|-------------|--------|-------|
| **AWS** | Amazon Time Sync Service | `169.254.169.123` (link-local) | Atomic clocks + GPS per region; pre-configured on Amazon Linux; uses leap second smearing |
| **Azure** | VMICTimeSync (hypervisor PTP) | PTP device within VM | Time delivered via hypervisor, not network NTP; chrony recommended |
| **GCP** | Google Public NTP | `time.google.com` | Pre-configured on Compute Engine; uses leap second smearing (24-hour) |

### Hybrid Environment Requirements

Where the organisation operates across on-premises and cloud environments:

- **Do not mix smeared and non-smeared time sources** within the same environment. Cloud providers (AWS, GCP) smear leap seconds over 24 hours; traditional NTP sources (METAS, pool.ntp.org) step. Mixing creates time discrepancies during leap second events.
- Document which time source each environment uses.
- For hybrid architectures, designate whether cloud or on-premises time is authoritative, and configure synchronisation direction accordingly.
- Monitor cloud VM time drift — virtualisation scheduling and live migration can introduce clock skew.

---

## Leap Second Handling

A leap second is a one-second adjustment (positive or negative) applied to UTC to keep it aligned with Earth's rotation. 27 leap seconds have been added since 1972; the practice is expected to be abolished by or before 2035 (per CGPM Resolution 4, November 2022).

### Organisational Strategy

The organisation shall adopt a **single, consistent leap second handling strategy** across all environments:

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| **Step** (traditional) | Insert or remove one second at 23:59:60 UTC | On-premises systems using traditional NTP sources (METAS, pool.ntp.org) |
| **Smear** | Spread the extra second over 24 hours by slightly adjusting clock rate | Cloud environments using provider time services (AWS, GCP) |

**Rules:**

- Never mix stepped and smeared time sources in the same environment.
- Document the chosen strategy and communicate to system administrators.
- Test leap second handling in advance of any scheduled leap second event.
- Monitor systems for 24 hours following a leap second event.
- Once leap seconds are abolished (expected by 2035), update configurations to remove leap second handling logic.

---

## NTP Security

### Protection Against Time-Based Attacks

NTP infrastructure shall be protected against spoofing, replay, and denial-of-service attacks:

| Threat | Mitigation |
|--------|-----------|
| **NTP spoofing** | Enable NTS (RFC 8915) or NTP symmetric key authentication; restrict NTP sources to approved servers |
| **Replay attacks** | NTS provides replay protection via unique cookies per exchange |
| **DDoS amplification** | Disable NTP monlist (`restrict ... noquery`); restrict NTP access to internal clients |
| **Unauthorised modification** | NTP server configurations protected by access controls; changes require change management approval |
| **Single point of failure** | Minimum two independent external sources; internal server redundancy |

### Configuration Protection

- NTP configuration files shall be protected from unauthorised modification (file permissions, integrity monitoring).
- Changes to NTP configuration shall follow the change management process.
- NTP service status shall be monitored; service failure shall generate an alert.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; approval of time synchronisation architecture; escalation point for persistent drift issues |
| **IT Operations / Platform Team** | NTP server deployment and maintenance; monitoring configuration; cloud time source configuration; leap second event management |
| **System Administrators** | Ensuring NTP is configured on managed systems; reporting synchronisation failures; verifying time settings during system deployment |
| **Network Administrators** | NTP configuration on network devices; firewall rules for NTP traffic; NTS deployment on supported devices |
| **Cloud Engineers** | Cloud-specific time source configuration; hybrid architecture time source documentation; cloud VM drift monitoring |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **NTP architecture documentation** (internal servers, external sources, stratum hierarchy, protocol/security settings) | IT Operations | *Documented; reviewed annually and upon architecture changes* |
| 2 | **NTP compliance coverage metric** (percentage of in-scope systems with verified NTP configuration and approved time sources) | IT Operations | *Quarterly; target: 100% of critical systems, ≥95% of all in-scope* |
| 3 | **Clock drift monitoring records** (offset, jitter, stratum metrics; alerts generated and resolved) | IT Operations | *Continuous monitoring; monthly trend report; alerts retained 12 months* |
| 4 | **Cloud time source documentation** (provider service, configuration, smearing strategy, hybrid considerations) | Cloud Engineers | *Documented per cloud service; reviewed annually* |
| 5 | **NTP security configuration** (NTS status, authentication, firewall rules, access restrictions) | IT Operations / Network | *Configuration documented; reviewed annually* |
| 6 | **Timestamp format compliance** (sample log entries from 5+ systems demonstrating UTC or offset format) | Information Security | *Verified annually during audit* |
| 7 | **Leap second strategy documentation** (chosen approach, testing records, monitoring during events) | IT Operations | *Documented; tested before each leap second event (or annually if none scheduled)* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through NTP configuration audits, drift monitoring reviews, timestamp format verification, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team.

Systems that cannot support NTP (e.g., legacy OT devices, isolated test environments) shall be documented with justification, and manual time verification shall be performed at a defined frequency.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to NTP standards, time source availability, cloud provider time services, leap second policy developments, and lessons learned from clock drift incidents or forensic investigations.

---

# Areas of the ISO 27001 Standard Addressed

Clock Synchronisation Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| | 5.37 Documented operating procedures |
| | 6.3 Information security awareness, education, and training |
| | **8.17 Clock synchronisation** |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures (data integrity) |
| Swiss DSV (Data Protection Ordinance) | Art. 4 — Logging obligations (accurate timestamps required) |
| EU GDPR (where applicable) | Art. 32 — Security of processing |
| ISO/IEC 27001:2022 | Annex A Control 8.17 |
| ISO/IEC 27002:2022 | Section 8.17 — Implementation guidance |
| NIST SP 800-53 Rev 5 | AU-8 (Time Stamps), AU-8(1) (Synchronisation with Authoritative Source), SC-45 (System Time Synchronisation) |
| NIST CSF 2.0 | PR.PS-04 (Log records generated for continuous monitoring) |
| CIS Controls v8 | Control 8.4 (Standardise Time Synchronisation) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
