**ISMS-REF-A.8.15 — Logging Standards Reference**
**Log Format Standards & Technical Specifications (Non-ISMS Technical Reference)**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Logging Standards Reference |
| **Document Type** | Internal - Technical Reference (Not ISMS) |
| **Document ID** | ISMS-REF-A.8.15 |
| **Document Creator** | Security Operations Center (SOC) / Security Architecture Team |
| **Document Owner** | Information Security Manager |
| **Approved By** | CISO (Technical Reference - No Executive Approval Required) |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | SOC / Security Architecture | Initial technical reference for ISO 27001:2022 certification |

**Review Cycle**: Quarterly (log format standards and technology evolve frequently)  
**Next Review Date**: [Date + 3 months]  
**Approvers**: SOC Lead / Security Architecture Team (technical reference, no ISMS approval required)

**Distribution**: SOC Team, Security Engineers, System Administrators, Application Developers (for technical implementation awareness)

---

⚠️ **IMPORTANT – NON-ISMS TECHNICAL SUPPORT DOCUMENT**

This document is provided for informational and awareness purposes only.

- This document is NOT part of the Information Security Management System (ISMS).
- This document does NOT define mandatory logging controls or requirements.
- This document does NOT establish binding requirements, deadlines, KPIs, or SLAs.
- This document does NOT mandate the use, prohibition, or configuration of specific log formats, tools, or platforms.
- This document does NOT override or extend any ISMS policy.

All binding logging requirements, obligations, and governance decisions are defined exclusively in **ISMS-POL-A.8.15 (Logging Policy)** and other approved ISMS documentation.

This document serves solely as a technical reference to:

- Describe commonly used log formats and standards
- Provide field naming conventions and encoding standards
- Support technical implementation planning
- Inform log format selection and parser development
- **This document must not be used as audit evidence of implementation**

Use of this document does not imply implementation, compliance, or operational maturity.

**Critical Positioning Statement**:
This document intentionally provides technical detail beyond what is required for ISO/IEC 27001 policy documentation. Its purpose is technical awareness only. No auditor conclusions shall be drawn from the presence, absence, or classification of any log format, field name, or technical specification listed herein.

---

# Document Purpose and Scope

## Purpose

This document provides technical reference for log format standards, field naming conventions, and encoding requirements commonly used in security logging implementations. It is intended to support:

- Technical implementation of logging requirements per ISMS-POL-A.8.15
- Selection of appropriate log formats based on system type and integration requirements
- Development of log parsing rules and SIEM integration
- Standardization of field names across organizational log sources
- Understanding of industry standard log formats (Syslog, CEF, JSON)
- Future log format evolution and parser maintenance

## What This Document Is NOT

This document does NOT:

- Define [Organization]'s approved or prohibited log formats
- Establish mandatory implementation requirements or technical controls
- Create compliance obligations or audit criteria
- Replace ISMS-POL-A.8.15 policy requirements
- Mandate specific SIEM platforms, log management tools, or vendors
- Define retention periods, review frequencies, or governance requirements

## Relationship to ISMS

This document is a **non-binding technical reference**. All logging control requirements are defined exclusively in ISMS-POL-A.8.15.

Implementation decisions are documented through ISMS-IMP-A.8.15 procedures based on risk assessment, operational context, and regulatory requirements.

## Content Organization

This reference organizes log format standards by:

- Syslog format (RFC 5424) for infrastructure and network devices
- Common Event Format (CEF) for security tools and SIEM integration
- JSON structured logging for applications and cloud services
- Field naming conventions and encoding standards
- Timestamp format requirements
- Character encoding and escaping rules

---

# Syslog Format Standards (RFC 5424)

## Overview

**Syslog (RFC 5424)** is the standard logging protocol for infrastructure components, operating systems, and network devices.

**Common Use Cases**:

- Network devices (routers, switches, firewalls)
- Unix/Linux operating systems
- Infrastructure services (DNS, DHCP, NTP)
- Legacy applications

**Protocol**:

- UDP port 514 (traditional, unencrypted - NOT RECOMMENDED for security logs)
- TCP port 514 or 6514 (recommended for reliability)
- TLS/TCP port 6514 (recommended for encrypted transmission per ISMS-POL-A.8.15 Section 2.2.3)

## Syslog Message Format

**RFC 5424 Message Structure**:

```
<PRI>VERSION TIMESTAMP HOSTNAME APP-NAME PROCID MSGID STRUCTURED-DATA MSG
```

**Example**:
```
<134>1 2026-01-21T14:32:15.003+01:00 server01.example.com sshd 1234 ID47 [exampleSDID@32473 iut="3" eventSource="Application" eventID="1011"] Failed password for invalid user admin from 10.0.1.50 port 22 ssh2
```

## Syslog Priority (PRI)

**Priority Calculation**: `PRI = (Facility * 8) + Severity`

**Facility Codes** (Common):

| Code | Facility | Usage |
|------|----------|-------|
| 0 | kernel | Kernel messages |
| 1 | user | User-level messages |
| 2 | mail | Mail system |
| 3 | daemon | System daemons |
| 4 | auth | Security/authentication |
| 5 | syslog | Syslog internal |
| 10 | authpriv | Security/authorization (private) |
| 16 | local0-7 | Local use (custom applications) |

**Severity Levels**:

| Code | Severity | Description | Usage Guideline |
|------|----------|-------------|----------------|
| 0 | Emergency | System is unusable | System panic, imminent crash |
| 1 | Alert | Action must be taken immediately | Critical resource failure, data corruption |
| 2 | Critical | Critical conditions | Hardware error, critical service failure |
| 3 | Error | Error conditions | Non-critical errors, application failures |
| 4 | Warning | Warning conditions | Recoverable errors, resource warnings |
| 5 | Notice | Normal but significant | Significant events (privilege escalation, config change) |
| 6 | Informational | Informational messages | Normal operations, successful authentications |
| 7 | Debug | Debug-level messages | Detailed troubleshooting information |

**Recommended Severity Mapping**:

- **Security events**: Notice (5) for successful operations, Warning (4) for policy violations, Error (3) for attacks
- **Authentication**: Info (6) for success, Warning (4) for failed attempts, Error (3) for account lockouts
- **System events**: Varies by context (Critical for service failures, Notice for configuration changes)

## Syslog Timestamp Format

**Required Format**: ISO 8601 with timezone

```
YYYY-MM-DDTHH:MM:SS.SSSSSS+TZ
```

**Examples**:

- `2026-01-21T14:32:15+01:00` (with timezone offset)
- `2026-01-21T13:32:15Z` (UTC notation)
- `2026-01-21T14:32:15.003+01:00` (with milliseconds)

**Best Practices**:

- Always include timezone information
- Use millisecond precision for high-volume systems where event ordering is critical
- Synchronize system clocks via NTP per ISMS-POL-A.8.17
- Use UTC for multi-site environments to simplify correlation

## Syslog Structured Data

**Format**: Key-value pairs in brackets

```
[SD-ID@PEN key1="value1" key2="value2"]
```

**Example**:
```
[secureAuth@123456 user="jdoe" src="10.0.1.50" action="login" result="success"]
```

**Recommended Structured Data Elements**:

- `user="username"` - User identifier
- `src="IP_address"` - Source IP
- `dst="IP_address"` - Destination IP
- `action="verb"` - Action performed
- `result="success|failure"` - Outcome
- `reason="description"` - Failure reason or additional context

## Syslog Configuration Example

**Linux rsyslog Configuration** (TCP with TLS):

```
# Send security logs to central SIEM
*.* @@(o)siem.example.com:6514
$ActionSendStreamDriverMode 1
$ActionSendStreamDriverAuthMode x509/name
$ActionSendStreamDriverPermittedPeer siem.example.com
```

**Network Device Syslog Configuration Example** (Cisco):

```
logging host 10.0.2.100 transport tcp port 6514
logging trap informational
logging origin-id hostname
logging source-interface Loopback0
```

---

# Common Event Format (CEF)

## Overview

**Common Event Format (CEF)** is a standardized log format for security events designed for SIEM integration.

**Developed By**: ArcSight (now Micro Focus), widely adopted industry standard

**Common Use Cases**:

- Security tools (firewalls, IDS/IPS, web application firewalls)
- Endpoint protection platforms
- Data loss prevention systems
- Authentication and access control systems
- SIEM integration from diverse security products

## CEF Message Format

**Structure**:

```
CEF:Version|Device Vendor|Device Product|Device Version|Signature ID|Name|Severity|Extension
```

**Example**:
```
CEF:0|Palo Alto Networks|PAN-OS|9.1.0|THREAT|URL Filtering|7|rt=Jan 21 2026 14:32:15 src=10.0.1.50 dst=93.184.216.34 spt=52341 dpt=443 request=https://malicious.example.com act=blocked
```

## CEF Header Fields

| Field | Description | Example |
|-------|-------------|---------|
| **Version** | CEF format version | 0 (current standard) |
| **Device Vendor** | Vendor name | Palo Alto Networks, Cisco, Check Point |
| **Device Product** | Product name | PAN-OS, ASA, FortiGate |
| **Device Version** | Product version | 9.1.0 |
| **Signature ID** | Event identifier | THREAT, AUTH, CONFIG |
| **Name** | Human-readable event name | URL Filtering, Login Failed |
| **Severity** | 0-10 scale | 0=Low, 5=Medium, 10=Critical |

**Severity Scale**:

- 0-3: Low (informational, minor issues)
- 4-6: Medium (warnings, policy violations)
- 7-8: High (security threats, attacks)
- 9-10: Critical (severe threats, successful breaches)

## CEF Extension Fields

**Standard Extension Keys** (Commonly Used):

| Key | Full Name | Description | Example |
|-----|-----------|-------------|---------|
| **src** | Source Address | Source IP address | 10.0.1.50 |
| **dst** | Destination Address | Destination IP address | 93.184.216.34 |
| **spt** | Source Port | Source TCP/UDP port | 52341 |
| **dpt** | Destination Port | Destination TCP/UDP port | 443 |
| **suser** | Source User Name | Source username | jdoe |
| **duser** | Destination User Name | Destination username | admin |
| **act** | Action | Action taken | blocked, allowed, alerted |
| **app** | Application Protocol | Application protocol | HTTP, HTTPS, SSH, FTP |
| **request** | Request URL | Full request URL or command | https://example.com/path |
| **requestMethod** | Request Method | HTTP method | GET, POST, PUT, DELETE |
| **cn1-cn3** | Custom Number 1-3 | Custom numeric fields | 1234 (bytes transferred) |
| **cs1-cs6** | Custom String 1-6 | Custom string fields | "User-Agent: Mozilla/5.0" |
| **rt** | Receipt Time | Event receipt time | Jan 21 2026 14:32:15 |
| **outcome** | Outcome | Event outcome | success, failure, unknown |
| **reason** | Reason | Reason for action or failure | Invalid credentials |
| **fileHash** | File Hash | File hash (MD5, SHA256) | a1b2c3d4e5f6... |
| **filePath** | File Path | Full file path | /var/log/suspicious.exe |

## CEF Examples by Event Type

**Authentication Event** (Failed Login):
```
CEF:0|Microsoft|Windows|Server 2019|4625|An account failed to log on|5|rt=Jan 21 2026 14:32:15 suser=admin src=10.0.1.50 outcome=failure reason=Unknown user name or bad password cs1Label=Domain cs1=EXAMPLE
```

**Firewall Event** (Blocked Connection):
```
CEF:0|Palo Alto Networks|PAN-OS|9.1.0|TRAFFIC|deny|8|rt=Jan 21 2026 14:32:15 src=10.0.1.50 dst=203.0.113.100 spt=52341 dpt=22 proto=TCP act=deny app=SSH
```

**Malware Detection**:
```
CEF:0|CrowdStrike|Falcon|6.42|MALWARE|Malware Detected|9|rt=Jan 21 2026 14:32:15 src=10.0.2.15 filePath=C:\\Users\\jdoe\\Downloads\\malware.exe fileHash=a1b2c3d4e5f6 act=quarantined outcome=success
```

**Web Application Firewall** (SQL Injection Blocked):
```
CEF:0|F5 Networks|BIG-IP ASM|15.1.0|SQL_INJECTION|SQL Injection Attack|9|rt=Jan 21 2026 14:32:15 src=203.0.113.50 request=https://webapp.example.com/login?id=1' OR '1'='1 requestMethod=GET act=blocked
```

## CEF Best Practices

1. **Use standard extension keys** where applicable (src, dst, suser) for SIEM compatibility
2. **Custom fields for non-standard data** (cs1-cs6 for strings, cn1-cn3 for numbers)
3. **Always include timestamp** (rt field) for accurate event correlation
4. **Escape pipe characters** in extension values (use backslash: \|)
5. **Escape backslashes** in extension values (use double backslash: \\)
6. **Escape equals signs** in custom field values (use backslash: \=)

---

# JSON Structured Logging

## Overview

**JSON (JavaScript Object Notation)** is the modern standard for application logging and cloud service logs.

**Common Use Cases**:

- Modern web applications and microservices
- Container and Kubernetes environments
- Cloud-native applications (AWS, Azure, GCP)
- API gateways and serverless functions
- SaaS application logs

**Advantages**:

- Human-readable and machine-parseable
- Native support in modern SIEM and log aggregation platforms
- Flexible schema (can accommodate any field structure)
- Easy to generate from application code (libraries available for all languages)

## JSON Log Structure

**Minimum Required Fields**:

```json
{
  "timestamp": "2026-01-21T14:32:15.003+01:00",
  "level": "INFO",
  "message": "User login successful",
  "logger": "auth.service",
  "context": {
    "user": "jdoe",
    "source_ip": "10.0.1.50",
    "action": "login",
    "outcome": "success"
  }
}
```

## Standard Field Names

**Recommended JSON Field Naming Convention** (snake_case):

| Field Name | Type | Description | Example |
|-----------|------|-------------|---------|
| **timestamp** | string (ISO 8601) | Event timestamp with timezone | "2026-01-21T14:32:15+01:00" |
| **level** | string | Log level | "INFO", "WARN", "ERROR", "DEBUG" |
| **message** | string | Human-readable message | "User login successful" |
| **logger** | string | Logger name or module | "auth.service", "app.controller" |
| **user_id** | string | User identifier | "jdoe", "user@example.com" |
| **session_id** | string | Session identifier | "abc123def456" |
| **request_id** | string | Request trace ID | "req-7f8a9b0c" |
| **source_ip** | string | Source IP address | "10.0.1.50" |
| **destination_ip** | string | Destination IP address | "93.184.216.34" |
| **action** | string | Action performed | "login", "create", "delete", "read" |
| **resource** | string | Resource affected | "/api/users", "file.txt" |
| **outcome** | string | Result of action | "success", "failure", "error" |
| **error_code** | string | Error code or exception type | "AUTH001", "NullPointerException" |
| **duration_ms** | number | Duration in milliseconds | 250 |
| **http_method** | string | HTTP method | "GET", "POST", "PUT", "DELETE" |
| **http_status** | number | HTTP status code | 200, 404, 500 |
| **user_agent** | string | User agent string | "Mozilla/5.0..." |

## Log Levels

**Standard Log Levels** (RFC 5424 equivalence):

| Level | Severity | Usage | Example |
|-------|----------|-------|---------|
| **TRACE** | Debug | Very detailed debugging | Variable values, function entry/exit |
| **DEBUG** | Debug | Detailed debugging | Logic flow, intermediate results |
| **INFO** | Informational | Normal operations | Service started, user logged in, transaction completed |
| **WARN** | Warning | Potential issues | Deprecated API used, retry attempt, threshold approaching |
| **ERROR** | Error | Error conditions | Database connection failed, API call failed, validation error |
| **FATAL/CRITICAL** | Critical | Severe errors | Application crash, unrecoverable error, data corruption |

**Production Logging Recommendation**:

- **Security logs**: INFO and above (INFO for success, WARN for policy violations, ERROR for attacks)
- **Application logs**: WARN and above (minimize noise while capturing issues)
- **DEBUG/TRACE**: Disabled in production (enable temporarily for troubleshooting with performance consideration)

## Structured Context

**Nested Context for Related Fields**:

```json
{
  "timestamp": "2026-01-21T14:32:15.003+01:00",
  "level": "ERROR",
  "message": "Authentication failed",
  "logger": "auth.service",
  "user": {
    "id": "jdoe",
    "email": "jdoe@example.com",
    "role": "user"
  },
  "request": {
    "id": "req-7f8a9b0c",
    "method": "POST",
    "path": "/api/auth/login",
    "source_ip": "10.0.1.50",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
  },
  "auth": {
    "method": "password",
    "outcome": "failure",
    "reason": "invalid_credentials",
    "attempts": 3
  },
  "error": {
    "code": "AUTH001",
    "type": "AuthenticationException",
    "message": "Invalid username or password"
  }
}
```

## JSON Examples by Event Type

**Authentication Success**:
```json
{
  "timestamp": "2026-01-21T14:32:15.003+01:00",
  "level": "INFO",
  "message": "User authenticated successfully",
  "logger": "auth.service",
  "user_id": "jdoe",
  "session_id": "sess-abc123",
  "source_ip": "10.0.1.50",
  "action": "login",
  "outcome": "success",
  "auth_method": "password_mfa",
  "duration_ms": 125
}
```

**API Request Log**:
```json
{
  "timestamp": "2026-01-21T14:32:16.120+01:00",
  "level": "INFO",
  "message": "API request processed",
  "logger": "api.gateway",
  "request_id": "req-7f8a9b0c",
  "http_method": "GET",
  "http_path": "/api/users/jdoe",
  "http_status": 200,
  "source_ip": "10.0.1.50",
  "user_id": "admin",
  "duration_ms": 45,
  "response_size_bytes": 1024
}
```

**Database Query Log**:
```json
{
  "timestamp": "2026-01-21T14:32:17.250+01:00",
  "level": "INFO",
  "message": "Database query executed",
  "logger": "database.service",
  "query_type": "SELECT",
  "table": "users",
  "user_id": "system",
  "duration_ms": 15,
  "rows_returned": 1,
  "query_hash": "a1b2c3d4"
}
```

**Error with Stack Trace**:
```json
{
  "timestamp": "2026-01-21T14:32:18.500+01:00",
  "level": "ERROR",
  "message": "Unhandled exception in payment processing",
  "logger": "payment.service",
  "request_id": "req-payment-001",
  "user_id": "customer123",
  "error": {
    "type": "PaymentGatewayException",
    "message": "Payment gateway timeout",
    "code": "GATEWAY_TIMEOUT",
    "stack_trace": "PaymentGatewayException: Gateway timeout\n  at PaymentService.processPayment(PaymentService.java:123)\n  at PaymentController.handlePayment(PaymentController.java:45)"
  },
  "transaction": {
    "id": "txn-789xyz",
    "amount": 99.99,
    "currency": "CHF"
  }
}
```

## JSON Best Practices

1. **Always include timestamp** with timezone (ISO 8601 format)
2. **Use snake_case** for field names (consistent convention)
3. **Minimize nesting** (1-2 levels maximum for readability and parsing efficiency)
4. **Avoid logging sensitive data** (no passwords, full credit cards, PII unless necessary)
5. **Include context identifiers** (request_id, session_id, user_id) for correlation
6. **Use structured data** instead of concatenating strings in message field
7. **Consistent schema** across application (use logging library with schema validation)
8. **One log event per line** (newline-delimited JSON for easy parsing)

---

# Timestamp Standards

## Required Format: ISO 8601

**Standard**: ISO 8601 with timezone information

**Format**: `YYYY-MM-DDTHH:MM:SS.SSSSSS±HH:MM` or `YYYY-MM-DDTHH:MM:SS.SSSZ`

**Examples**:

- `2026-01-21T14:32:15+01:00` (Central European Time with offset)
- `2026-01-21T13:32:15Z` (UTC, 'Z' suffix indicates UTC)
- `2026-01-21T14:32:15.003+01:00` (with milliseconds)
- `2026-01-21T14:32:15.123456+01:00` (with microseconds)

## Timezone Handling

**Recommendation**: Use UTC for all centralized log storage

**Rationale**:

- Eliminates timezone conversion errors
- Simplifies correlation across geographic locations
- Avoids daylight saving time complications
- Universal reference for multi-site organizations

**Local Time with Offset** (Alternative):

- Acceptable for single-site deployments
- MUST include timezone offset (e.g., +01:00, -05:00)
- SIEM must normalize to UTC for correlation

## Precision Requirements

**Minimum**: Second precision (`YYYY-MM-DDTHH:MM:SS`)

**Recommended**: Millisecond precision (`YYYY-MM-DDTHH:MM:SS.SSS`)

- Required for high-volume systems (hundreds of events per second)
- Enables accurate event ordering within same second
- Necessary for correlation of rapid event sequences

**Optional**: Microsecond precision (`YYYY-MM-DDTHH:MM:SS.SSSSSS`)

- Useful for very high-performance systems
- Database transaction logging with sub-millisecond granularity

## Time Synchronization

**Requirement**: All log sources MUST synchronize time with authoritative time source per ISMS-POL-A.8.17 (Clock Synchronization).

**NTP Configuration**:

- Primary NTP server (Stratum 1 or 2)
- Secondary NTP servers for redundancy
- Maximum clock drift threshold: ±100ms
- Alert on NTP synchronization failure

**Importance**: Accurate timestamps are critical for:

- Event correlation across multiple systems
- Incident timeline reconstruction
- Forensic analysis and legal evidence
- Compliance verification

---

# Field Naming Conventions

## Naming Standards

**Use Consistent Naming Convention**:

| Convention | Example | Use Case |
|------------|---------|----------|
| **snake_case** | `source_ip`, `user_id`, `event_type` | JSON logs, Python applications |
| **camelCase** | `sourceIp`, `userId`, `eventType` | JavaScript applications, some SIEMs |
| **dot.notation** | `event.type`, `user.id`, `source.ip` | ECS (Elastic Common Schema), nested fields |

**Recommendation**: Choose ONE convention and use consistently across organization. snake_case is increasingly common for security logging.

## Standard Field Names

**Identity Fields**:

- `user_id` / `user` / `username` - User identifier
- `user_email` - User email address
- `service_account` - Service account identifier
- `session_id` - Session identifier
- `request_id` / `trace_id` - Request trace identifier
- `transaction_id` - Transaction identifier

**Network Fields**:

- `source_ip` / `src_ip` - Source IP address
- `destination_ip` / `dst_ip` - Destination IP address
- `source_port` / `src_port` - Source TCP/UDP port
- `destination_port` / `dst_port` - Destination TCP/UDP port
- `protocol` - Network protocol (TCP, UDP, ICMP)
- `hostname` - System hostname

**Action Fields**:

- `action` / `event_action` - Action performed (login, create, delete, read, update)
- `event_type` / `event_category` - Event category (authentication, authorization, configuration)
- `outcome` / `result` - Result (success, failure, error)
- `reason` - Reason for outcome or action
- `severity` / `level` - Severity level

**Resource Fields**:

- `resource` / `object` - Affected resource
- `file_path` - File path
- `file_hash` - File hash (MD5, SHA256)
- `url` / `request_url` - URL or endpoint
- `api_endpoint` - API endpoint

**Temporal Fields**:

- `timestamp` / `event_time` - Event timestamp
- `duration` / `duration_ms` - Duration in milliseconds
- `start_time` - Start timestamp
- `end_time` - End timestamp

**Application Fields**:

- `application` / `app_name` - Application name
- `environment` - Environment (production, staging, development)
- `version` / `app_version` - Application version
- `component` / `module` - Component or module name

**Error Fields**:

- `error_code` - Error code
- `error_type` / `exception_type` - Exception class name
- `error_message` / `exception_message` - Error description
- `stack_trace` - Stack trace (for errors)

## Avoid Ambiguous Names

**DON'T USE**:

- `data` - Too generic, use specific name (e.g., `user_data`, `request_data`)
- `info` - Ambiguous, use specific name (e.g., `user_info` → `user_email`)
- `value` - Non-descriptive, use semantic name
- `temp` - Unclear purpose, use descriptive name

**USE**:

- Descriptive, self-documenting names
- Consistent terminology across organization
- Standard names from ECS (Elastic Common Schema) where applicable

---

# Character Encoding and Escaping

## Character Encoding

**Standard**: UTF-8 encoding for all logs

**Rationale**:

- Universal support for international characters
- Efficient for ASCII (1 byte per character)
- Compatible with JSON, XML, modern applications

**Implementation**:

- Configure log sources to output UTF-8
- Configure SIEM parsers to expect UTF-8
- Test with non-ASCII characters (ä, ö, ü, é, ñ, 中文)

## Special Character Escaping

**Syslog (RFC 5424)**:

- No special escaping required in MSG field
- Use structured data format for key-value pairs (automatic escaping)

**CEF**:

- Escape pipe characters: `|` → `\|`
- Escape backslashes: `\` → `\\`
- Escape equals in extension values: `=` → `\=`
- Escape newlines: `\n` → `\\n`

**Example**:
```
# Original message: User logged in from C:\Program Files\Application
# Escaped for CEF:
cs1=C:\\Program Files\\Application
```

**JSON**:

- JSON libraries automatically escape special characters
- Manual escaping (if needed):
  - Double quotes: `"` → `\"`
  - Backslashes: `\` → `\\`
  - Newlines: newline character → `\n`
  - Tabs: tab character → `\t`

**Example**:
```json
{
  "message": "User logged in from \"C:\\Program Files\\Application\""
}
```

## Maximum Field Lengths

**Recommendations** (SIEM compatibility):

| Field Type | Maximum Length | Rationale |
|-----------|---------------|-----------|
| **String fields** | 1024 characters | SIEM database field limits |
| **Message field** | 8192 characters | Log message may include stack traces |
| **URL fields** | 2048 characters | Modern URL length support |
| **File path** | 4096 characters | Unix/Linux path maximum |
| **User identifier** | 256 characters | Email addresses, LDAP DN |

**Truncation Strategy**:

- Truncate from end for narrative fields (messages, descriptions)
- Truncate from middle for URLs (preserve domain and parameters)
- Never truncate identifiers (user IDs, transaction IDs) - reject if too long

---

# Implementation Guidance

## Log Format Selection Matrix

**Decision Guide**: Choose log format based on system type

| System Type | Recommended Format | Rationale |
|-------------|-------------------|-----------|
| **Network Devices** (Firewall, Router, Switch) | Syslog (RFC 5424) | Native support, minimal configuration |
| **Unix/Linux OS** | Syslog (RFC 5424) | Native support, standard infrastructure |
| **Windows OS** | Windows Event Log (native) | Native support, convert to CEF or JSON for SIEM |
| **Security Tools** (IDS, Firewall, WAF) | CEF | SIEM integration, standardized security events |
| **Web Applications** | JSON | Easy to generate, flexible schema |
| **Microservices** | JSON | Cloud-native, container-friendly |
| **Cloud Services** (AWS, Azure, GCP) | JSON (CloudWatch, Azure Monitor, Cloud Logging) | Native format, seamless integration |
| **Database Logs** | JSON or Syslog | Application-specific, JSON preferred for structured queries |

## SIEM Integration Considerations

**Parser Development**:

- Syslog: Use built-in parsers, customize for structured data extraction
- CEF: Use built-in CEF parsers, map extension fields to SIEM schema
- JSON: Configure JSON parser, define field mappings

**Field Mapping**:

- Map log source fields to SIEM common schema (normalize field names)
- Create calculated fields for derived data (e.g., geo-location from IP)
- Enrich events with threat intelligence (malicious IP lookups)

**Performance Optimization**:

- Use appropriate log level filtering (INFO and above for production)
- Implement sampling for high-volume, low-value logs (debug logs)
- Compress logs before transmission (gzip, if SIEM supports)
- Batch log forwarding (collect-and-forward vs. real-time)

## Logging Library Recommendations

**By Programming Language**:

| Language | Recommended Library | Structured Logging Support |
|----------|-------------------|---------------------------|
| **Python** | `structlog`, `python-json-logger` | Yes (JSON output) |
| **Java** | `Logback`, `Log4j2` | Yes (JSON encoder available) |
| **JavaScript/Node.js** | `winston`, `pino` | Yes (JSON native) |
| **Go** | `zap`, `logrus` | Yes (JSON native) |
| **C#/.NET** | `Serilog`, `NLog` | Yes (JSON formatter) |
| **Ruby** | `Lograge`, `semantic_logger` | Yes (JSON output) |
| **PHP** | `Monolog` | Yes (JSON formatter) |

**Configuration Example** (Python structlog):

```python
import structlog

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    logger_factory=structlog.stdlib.LoggerFactory(),
)

log = structlog.get_logger()
log.info("user_login", user_id="jdoe", source_ip="10.0.1.50", outcome="success")
```

---

# Document Maintenance

## Update Triggers

This reference document may be updated when:

- New log format standards emerge or existing standards updated
- SIEM platform changes requiring new format support
- Log parsing issues identified requiring format clarification
- Application development teams request guidance on new log formats
- Industry best practices evolve (e.g., ECS schema updates)

## Responsibility

**Document Owner**: SOC Lead / Security Architecture Team  
**Review Frequency**: Quarterly or as needed  
**Update Authority**: Technical update (no ISMS approval process required)

## Version Control

All versions retained for reference. Major changes documented in version history table. Previous versions available in document repository.

---

# Relationship to ISMS-POL-A.8.15

This document provides **technical implementation guidance** that may inform:

- Log format selection during system onboarding (ISMS-IMP-A.8.15.1)
- Log parser development for SIEM integration (ISMS-IMP-A.8.15.2)
- Field name standardization across organizational log sources
- Training for developers and system administrators on logging standards

This document does NOT:

- Override or extend ISMS-POL-A.8.15 requirements
- Establish mandatory log format selections
- Create compliance obligations
- Define audit criteria

All logging control requirements are defined exclusively in ISMS-POL-A.8.15 and implemented through ISMS-IMP-A.8.15 procedures based on risk assessment and operational context.

---

**END OF DOCUMENT**

*This is a technical reference document for awareness purposes only. It does not establish ISMS requirements or create compliance obligations.*
<!-- QA_VERIFIED: 2026-02-01 -->
