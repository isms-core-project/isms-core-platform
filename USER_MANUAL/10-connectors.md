# Automated Evidence Connectors

<!-- ISMS-CORE:USER-MANUAL:10-connectors:v1.0:2026-04-16 -->

---

## What Connectors Do

Connectors are the evidence automation layer. Each connector integrates with an external system — your cloud provider, identity platform, vulnerability scanner, EDR, or ITSM tool — and automatically pulls evidence into the platform on a scheduled basis.

This means your compliance posture is continuously updated from real infrastructure data, not just from manual assessments done once a year.

---

## The Connector Dashboard

Navigate to **Evidence → Connectors** in the sidebar.

The Connectors dashboard shows all 44 available connectors with their current status:

| Status | Meaning |
|--------|---------|
| **Active / Healthy** | Connector is configured, running, and last run was successful |
| **Active / Warning** | Connector is configured but last run had non-fatal issues |
| **Active / Error** | Connector is configured but last run failed — check configuration |
| **Not configured** | Connector is available but credentials have not been provided |

---

## Supported Connectors (44 systems)

### Microsoft

| Connector | ISO Controls | Evidence type |
|-----------|-------------|---------------|
| Microsoft Entra ID | A.5.15, A.5.16, A.5.17, A.8.2 | User accounts, group memberships, MFA status, conditional access policies |
| Microsoft Defender XDR | A.8.7, A.8.8, A.8.16 | Endpoint threat detections, vulnerability findings, patch status |
| Microsoft Sentinel | A.8.15, A.8.16 | SIEM alert summary, log ingestion status |
| Microsoft Intune | A.8.9, A.8.10 | Device compliance status, MDM policy deployment |
| Microsoft 365 | A.5.14, A.5.15 | Licence assignments, secure score summary |
| Microsoft Purview | A.5.12, A.5.33 | Data classification labels, retention policy status |
| Azure CSPM | A.8.9, A.8.23 | Cloud security posture score, misconfiguration findings |

### Network & Firewall

| Connector | ISO Controls | Evidence type |
|-----------|-------------|---------------|
| FortiGate | A.8.20, A.8.21 | Firewall policy summary, traffic logs |
| FortiAnalyzer | A.8.15, A.8.16 | Log aggregation status, event summary |
| FortiManager | A.8.9 | Configuration compliance |
| Palo Alto PAN-OS | A.8.20, A.8.21 | Security policy status, threat logs |
| Cisco ASA | A.8.20 | Access control policy export |
| Cisco ISE | A.5.15, A.8.20 | Network access control policy status |
| Zscaler | A.8.23 | Web filtering policy, user activity summary |

### ITSM

| Connector | ISO Controls | Evidence type |
|-----------|-------------|---------------|
| ServiceNow | A.5.26, A.5.37 | Incident tickets, change records, CMDB asset counts |
| Jira / Jira Service Management | A.5.26 | Issue counts by status, security-tagged ticket summary |
| GLPI | A.5.26, A.8.10 | Asset inventory, incident records |

### Vulnerability & EDR

| Connector | ISO Controls | Evidence type |
|-----------|-------------|---------------|
| Qualys | A.8.8 | Vulnerability scan results, patch compliance |
| Tenable.sc | A.8.8 | Vulnerability scan results |
| Tenable.io | A.8.8 | Cloud vulnerability scan results |
| CrowdStrike Falcon | A.8.7, A.8.16 | Endpoint protection status, threat detections |
| SentinelOne | A.8.7 | Endpoint detection summary |
| Wazuh | A.8.7, A.8.15 | HIDS alert summary, file integrity monitoring |
| OpenVAS | A.8.8 | Vulnerability scan results |

### Identity & PAM

| Connector | ISO Controls | Evidence type |
|-----------|-------------|---------------|
| Windows Active Directory | A.5.15, A.5.16 | User account status, group membership, password policy |
| LDAP | A.5.15 | Directory service health, user account counts |
| FreeIPA | A.5.15 | Identity management status |
| Authentik | A.5.15, A.5.16 | SSO provider health, MFA enrolment stats |
| Keycloak | A.5.15, A.5.16 | Realm configuration, user session stats |
| CyberArk | A.5.17 | Privileged account counts, vault health |
| HashiCorp Vault | A.5.17, A.8.24 | Secret rotation status, policy compliance |
| Devolutions Server | A.5.17 | PAM vault health |

### Monitoring & SIEM

| Connector | ISO Controls | Evidence type |
|-----------|-------------|---------------|
| PRTG Network Monitor | A.8.16 | Sensor health, uptime statistics |
| Graylog | A.8.15 | Log stream status, retention policy |
| Zabbix | A.8.16 | Host monitoring status, alert summary |
| Generic SIEM | A.8.15 | Configurable — log ingestion counts and alert summary |

### Cloud Security

| Connector | ISO Controls | Evidence type |
|-----------|-------------|---------------|
| AWS Security Hub | A.8.23, A.8.9 | Security Hub findings, compliance score |
| Google Cloud SCC | A.8.23 | Security Command Center findings |

### Threat Intelligence

| Connector | ISO Controls | Evidence type |
|-----------|-------------|---------------|
| OpenCTI | A.5.7 | Threat intelligence platform status, indicator counts |
| OpenAEV | A.5.7 | External threat feed summary |
| Threat Intel Feed | A.5.7 | Generic threat intelligence feed |

### DevOps

| Connector | ISO Controls | Evidence type |
|-----------|-------------|---------------|
| GitHub | A.8.25, A.8.28 | Repository security settings, secret scanning alerts |
| GitLab | A.8.25, A.8.28 | Repository security settings, CI/CD pipeline status |

---

## Configuring a Connector

Connector configuration is done by the platform administrator in the Admin panel. As a user you can view connector status and collected evidence, but you cannot modify connector credentials.

If a connector you need is showing "Not configured" or "Error":
1. Note the connector name and the error message shown
2. Contact your platform administrator with the connector name and the credentials or API tokens required

Connector credential requirements are documented in the Admin panel for each connector.

---

## Evidence Refresh

Connectors run on a schedule set by the administrator (default: every 6 hours for most connectors). The last run timestamp and status are shown on the connector card.

If you need fresh evidence immediately — for example, immediately before an audit check — the administrator can trigger a manual connector run from **Admin → Connectors → Run now**.

---

## Bidirectional: Jira and ServiceNow

Jira and ServiceNow are the two bidirectional connectors. In addition to pulling evidence inbound, they support outbound ticket creation for gaps and remediation actions.

See [Gap Management](08-gap-management.md) for how to push gaps to Jira or ServiceNow.

<!-- QA_VERIFIED: 2026-04-16 -->
