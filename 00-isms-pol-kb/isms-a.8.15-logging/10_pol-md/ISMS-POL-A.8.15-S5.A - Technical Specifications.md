# ISMS-POL-A.8.15-S5.A
## Logging Standards - Technical Specifications

**Document ID**: ISMS-POL-A.8.15-S5.A  
**Title**: Logging Standards - Technical Specifications  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect / Log Administrator | Initial technical standards |

**Review Cycle**: Annual (or upon significant technology changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: Information Security Manager, Security Architect  
**Distribution**: System administrators, developers, security engineers, log administrators

---

## A.1 Log Format Standards

### A.1.1 Supported Log Formats

Organizations **SHALL** use one of the following standard log formats:

**Primary Formats** (preferred):
1. **Syslog** (RFC 5424) - Universal protocol
2. **Common Event Format (CEF)** - Structured security events
3. **JSON** (JavaScript Object Notation) - Modern structured format

**Secondary Formats** (acceptable):
4. **Legacy Syslog** (RFC 3164) - Older systems only
5. **Windows Event Log** (EVTX) - Windows-native format
6. **Vendor-specific structured formats** (with documented schema)

**Unacceptable Formats**:
- Unstructured free-text logs (no consistent parsing)
- Proprietary binary formats (without export capability)
- Formats without timestamp or source identification

---

## A.2 Syslog Configuration Standard (RFC 5424)

### A.2.1 Syslog Protocol Overview

**RFC 5424** defines modern syslog protocol with:
- Structured data elements
- Explicit character encoding (UTF-8)
- Timestamp with timezone
- Application name and process ID
- Message ID for event classification

### A.2.2 Syslog Message Format

**Standard Structure**:
```
<Priority>Version Timestamp Hostname App-Name ProcID MsgID [Structured-Data] Message
```

**Example**:
```
<134>1 2026-01-06T15:30:45.123+01:00 webserver01 nginx 1234 access [user@12345 userId="jdoe" sessionId="abc123"] 192.168.1.100 GET /api/data HTTP/1.1 200
```

### A.2.3 Priority Calculation

**Priority** = (Facility × 8) + Severity

**Severity Levels** (use for filtering and alerting):
- 0: Emergency - system unusable
- 1: Alert - action must be taken immediately
- 2: Critical - critical conditions
- 3: Error - error conditions
- 4: Warning - warning conditions
- 5: Notice - normal but significant
- 6: Informational - informational messages
- 7: Debug - debug-level messages

**Facility Codes** (use to identify log source type):
- 0: Kernel messages
- 1: User-level messages
- 2: Mail system
- 3: System daemons
- 4: Security/authentication messages
- 10: Security/authentication messages (alternate)
- 16-23: Local use (local0-local7)

**Common Mappings**:
- Authentication logs: Facility 4 or 10
- Security events: Facility 4, Severity 2-4
- Application logs: Facility 16-23, Severity varies

### A.2.4 Structured Data

**Format**: `[SD-ID SD-PARAM="value" ...]`

**Standard SD-IDs**:
- `[user@<enterprise-id>]` - User-related data
- `[security@<enterprise-id>]` - Security events
- `[session@<enterprise-id>]` - Session information

**Example**:
```
[security@12345 eventType="authentication" outcome="failure" userId="jdoe" sourceIP="192.168.1.100"]
```

### A.2.5 Syslog Transport

**Preferred Transport**: TLS over TCP (RFC 5425)
- Port 6514 (IANA assigned for syslog over TLS)
- Encryption: TLS 1.2+ (TLS 1.3 recommended)
- Certificate validation: Required

**Acceptable Transport**: TCP (RFC 6587)
- Port 1468 or 601
- No encryption (use only within secure networks)

**Legacy Transport**: UDP (RFC 5426)
- Port 514
- No reliability guarantees (messages may be lost)
- Use only for non-critical logs or legacy systems

### A.2.6 Syslog Configuration Examples

**Linux rsyslog configuration** (`/etc/rsyslog.conf`):
```
# Send all logs to central syslog server via TLS
*.* @@(o)logserver.example.com:6514

# Alternative: TCP without TLS (internal network only)
*.* @@logserver.example.com:601

# Legacy: UDP (not recommended)
*.* @logserver.example.com:514
```

**Cisco network device**:
```
logging host logserver.example.com transport tcp port 601
logging trap informational
logging source-interface Loopback0
```

---

## A.3 Common Event Format (CEF)

### A.3.1 CEF Overview

**Common Event Format (CEF)** developed by ArcSight (now OpenText), widely supported by SIEM platforms.

**Use CEF for**: Security events, alerts, audit records

### A.3.2 CEF Message Structure

**Format**:
```
CEF:Version|Device Vendor|Device Product|Device Version|Signature ID|Name|Severity|Extension
```

**Example**:
```
CEF:0|Fortinet|FortiGate|6.4.0|100|Traffic Denied|5|src=192.168.1.100 dst=10.0.0.50 spt=54321 dpt=445 proto=TCP act=deny
```

### A.3.3 CEF Header Fields

1. **CEF Version**: Always "0" (current version)
2. **Device Vendor**: Manufacturer (e.g., "Fortinet", "Palo Alto Networks")
3. **Device Product**: Product name (e.g., "FortiGate", "PA-Series")
4. **Device Version**: Software version
5. **Signature ID**: Event type identifier (numeric or string)
6. **Name**: Human-readable event name
7. **Severity**: 0-10 (0=lowest, 10=highest)

### A.3.4 CEF Extension Fields

**Standard Fields** (use these for interoperability):

**Network Fields**:
- `src` - Source IP address
- `dst` - Destination IP address
- `spt` - Source port
- `dpt` - Destination port
- `proto` - Protocol (TCP, UDP, ICMP)

**User Fields**:
- `suser` - Source user
- `duser` - Destination user
- `suid` - Source user ID

**Event Fields**:
- `act` - Action taken (allow, deny, alert, block)
- `outcome` - Outcome (success, failure)
- `msg` - Message or additional information

**Time Fields**:
- `rt` - Event receive time (epoch milliseconds)
- `start` - Event start time
- `end` - Event end time

**File Fields**:
- `fname` - File name
- `fsize` - File size
- `fileHash` - File hash

**Example with extensions**:
```
CEF:0|Microsoft|Windows|10|4625|Failed Login|8|suser=jdoe src=192.168.1.100 outcome=failure rt=1704553845000
```

---

## A.4 JSON Logging Standard

### A.4.1 JSON Overview

**JSON** (JavaScript Object Notation) is modern, widely-supported structured format.

**Use JSON for**: Application logs, API logs, cloud services, microservices

### A.4.2 JSON Log Structure

**Minimum Required Fields**:
```json
{
  "timestamp": "2026-01-06T15:30:45.123Z",
  "level": "INFO",
  "source": "application-name",
  "message": "Event description",
  "event_type": "authentication.login"
}
```

**Extended Example**:
```json
{
  "timestamp": "2026-01-06T15:30:45.123Z",
  "level": "WARN",
  "source": "web-api",
  "event_type": "authentication.failure",
  "user": {
    "id": "jdoe",
    "email": "jdoe@example.com"
  },
  "request": {
    "method": "POST",
    "path": "/api/auth/login",
    "source_ip": "192.168.1.100",
    "user_agent": "Mozilla/5.0..."
  },
  "outcome": "failure",
  "reason": "invalid_password",
  "message": "Authentication failed for user jdoe"
}
```

### A.4.3 JSON Field Naming Conventions

**Standards**:
- Use `snake_case` for field names (consistent with Python/Unix conventions)
- Avoid camelCase (harder to parse with some tools)
- Use lowercase for all field names
- Use underscores to separate words

**Examples**:
- ✅ `user_id`, `source_ip`, `event_type`
- ❌ `userId`, `sourceIP`, `EventType`

### A.4.4 JSON Log Levels

**Standard Levels** (align with syslog severity):
- `EMERGENCY` / `FATAL` - System unusable (severity 0)
- `ALERT` - Action required immediately (severity 1)
- `CRITICAL` / `CRIT` - Critical conditions (severity 2)
- `ERROR` - Error conditions (severity 3)
- `WARNING` / `WARN` - Warning conditions (severity 4)
- `NOTICE` - Normal but significant (severity 5)
- `INFO` / `INFORMATION` - Informational (severity 6)
- `DEBUG` / `TRACE` - Debug messages (severity 7)

---

## A.5 Timestamp Standards

### A.5.1 Timestamp Format

**Standard**: ISO 8601 format with timezone

**Format**: `YYYY-MM-DDTHH:MM:SS.sssZ` or `YYYY-MM-DDTHH:MM:SS.sss±HH:MM`

**Examples**:
- UTC: `2026-01-06T14:30:45.123Z`
- CET: `2026-01-06T15:30:45.123+01:00`
- EST: `2026-01-06T09:30:45.123-05:00`

**Requirements**:
- Include date (YYYY-MM-DD)
- Include time (HH:MM:SS)
- Include milliseconds (`.sss`) for high-precision
- Include timezone (`Z` for UTC or `±HH:MM` for offset)
- Use 24-hour time format

### A.5.2 Timezone Policy

**Recommendation**: Use UTC (Coordinated Universal Time) for all logs
- Eliminates timezone confusion
- Simplifies correlation across global systems
- No daylight saving time issues

**Alternative**: Use local time with explicit timezone offset
- Acceptable for systems in single timezone
- MUST include timezone offset (not just timezone name)
- Example: `+01:00` not just "CET"

**Forbidden**: Timezone-ambiguous timestamps
- ❌ `2026-01-06 15:30:45` (no timezone)
- ❌ `01/06/2026 3:30:45 PM` (ambiguous date format, no timezone)

### A.5.3 Time Synchronization

**Requirement**: All systems MUST synchronize time via NTP (see ISMS-POL-A.8.17)

**NTP Configuration**:
- Use organizational NTP servers or public NTP pool
- Synchronize at least hourly (more frequent for critical systems)
- Monitor NTP synchronization status
- Alert on synchronization failures

**Acceptable Time Drift**: ±1 second (±100ms preferred for high-volume systems)

---

## A.6 Character Encoding

### A.6.1 Standard Encoding

**Required**: UTF-8 (Unicode Transformation Format - 8-bit)

**Rationale**:
- Universal character support (international characters, emojis)
- Backward compatible with ASCII
- Widely supported across platforms

**Configuration**:
- All log files: UTF-8 encoding
- Syslog messages: UTF-8 (RFC 5424 requirement)
- JSON logs: UTF-8 (JSON standard)

### A.6.2 Forbidden Encodings

Do NOT use:
- ASCII (insufficient character support)
- ISO-8859-1 / Latin-1 (limited character set)
- Windows-1252 (platform-specific)
- EBCDIC (legacy mainframe encoding)

---

## A.7 Log Field Standards

### A.7.1 Mandatory Fields

Every log event **MUST** include:

1. **Timestamp** (ISO 8601 with timezone)
2. **Event Source** (hostname, IP, or system identifier)
3. **Event Type** (category/classification)
4. **Severity/Level** (priority indicator)
5. **Message** (human-readable description)

### A.7.2 Recommended Fields

Logs **SHOULD** include where applicable:

**User Context**:
- `user_id` / `username` - User performing action
- `user_email` - User email address
- `user_role` - User role or privilege level

**Network Context**:
- `source_ip` - Source IP address
- `source_port` - Source TCP/UDP port
- `dest_ip` - Destination IP address
- `dest_port` - Destination TCP/UDP port
- `protocol` - Network protocol (TCP, UDP, HTTP, HTTPS)

**Action Context**:
- `action` - Action performed (login, access, modify, delete)
- `object` - Object acted upon (file, record, resource)
- `outcome` - Result (success, failure, error)
- `reason` - Reason for outcome (especially for failures)

**Request Context** (for web/API logs):
- `request_method` - HTTP method (GET, POST, PUT, DELETE)
- `request_path` - URL path
- `request_query` - Query parameters (sanitize sensitive data)
- `response_code` - HTTP response code (200, 404, 500)
- `response_time` - Request processing time (milliseconds)

**Session Context**:
- `session_id` - Session identifier
- `correlation_id` - Request correlation ID (for distributed tracing)
- `transaction_id` - Transaction identifier

### A.7.3 Fields to Exclude

**Never log**:
- Passwords (plaintext or hashed)
- API keys, tokens, secrets
- Full credit card numbers (PCI DSS violation)
- Social Security Numbers
- Full health records (HIPAA violation)
- Encryption keys or certificates

**Sanitize** (mask sensitive portions):
- Credit cards: Log last 4 digits only (`****-****-****-1234`)
- Emails: Mask username (`j***@example.com`)
- Phone numbers: Mask middle digits (`+1-555-***-7890`)

---

## A.8 Log Message Content Standards

### A.8.1 Message Clarity

Log messages **SHOULD**:
- Be human-readable and understandable
- Include sufficient context for investigation
- Avoid excessive technical jargon
- Use consistent terminology

**Good Examples**:
- ✅ "User jdoe failed authentication from 192.168.1.100 - invalid password"
- ✅ "File /data/sensitive.csv accessed by user admin at 2026-01-06T15:30:45Z"

**Bad Examples**:
- ❌ "Auth fail" (insufficient context)
- ❌ "ERR_CODE_12345" (no human-readable description)

### A.8.2 Message Structure

**Recommended Structure**: `[Subject] [Action] [Object] [Context]`

**Examples**:
- "User jdoe logged in successfully from 192.168.1.100"
- "Administrator admin deleted user account bob"
- "Firewall blocked connection from 203.0.113.5 to 10.0.0.50 port 22"

---

## A.9 Implementation Guidance

### A.9.1 Configuration Management

**Document** all log configurations:
- Which standard is used (syslog, CEF, JSON)
- Timestamp format and timezone
- Log level/severity mapping
- Custom field definitions

**Version Control**: Store configurations in version control (Git)

### A.9.2 Testing and Validation

**Test** log formats before production deployment:
- Generate sample log events
- Verify parsing in SIEM/log management system
- Confirm all required fields present
- Validate timestamp accuracy

### A.9.3 Monitoring

**Monitor** log format compliance:
- Parse errors in SIEM (indicates format issues)
- Missing required fields
- Character encoding errors
- Timestamp inconsistencies

---

## A.10 Standards References

**RFCs**:
- RFC 5424: The Syslog Protocol
- RFC 5425: Transport Layer Security (TLS) Transport Mapping for Syslog
- RFC 3164: The BSD Syslog Protocol (legacy)
- RFC 8259: JSON Data Interchange Format

**ISO Standards**:
- ISO 8601: Date and time format

**Industry Standards**:
- CEF Format Specification (OpenText ArcSight)
- NIST SP 800-92: Guide to Computer Security Log Management

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-POL-A.8.15-S5.A |
| **Document Type** | Annex - Technical Standards |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Line Count** | ~395 lines |
| **Parent Policy** | ISMS-POL-A.8.15 (Master) |

---

**END OF ANNEX A**