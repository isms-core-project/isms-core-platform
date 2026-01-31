# ISMS-POL-A.7.4-5-11-S2: Physical Security Monitoring (A.7.4)

**Document Classification:** Internal - ISMS Policy  
**Version:** 1.0  
**Effective Date:** [To be defined]  
**Review Cycle:** Annual  
**Policy Owner:** Security Operations Manager / CISO  
**Approved By:** [Approval Authority]

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Operations Manager / CISO | Initial policy for physical security monitoring requirements |

**Review Schedule:** Annual review or upon significant security incidents, facility changes, or technology updates  
**Next Review Date:** [Approval Date + 12 months]  
**Distribution:** CISO, Security Operations, Facilities Management, System Owners, Security Personnel, Auditors

---

## Table of Contents

1. [Control Overview](#1-control-overview)
2. [Physical Access Monitoring](#2-physical-access-monitoring)
3. [Physical Intrusion Detection](#3-physical-intrusion-detection)
4. [Video Surveillance (CCTV)](#4-video-surveillance-cctv)
5. [Security Personnel Monitoring](#5-security-personnel-monitoring)
6. [Physical Security Alarm System](#6-physical-security-alarm-system)
7. [Integration with Security Operations](#7-integration-with-security-operations)
8. [Measurable Requirements and Audit Verification](#8-measurable-requirements-and-audit-verification)
9. [Cloud and Colocation Considerations](#9-cloud-and-colocation-considerations)
10. [Related Documents](#10-related-documents)

---

## 1. Control Overview

### 1.1 ISO 27001:2022 Control A.7.4 Reference

**Control Text:** Premises shall be continuously monitored for unauthorized physical access.

**Purpose:** To detect and respond to unauthorized physical access to premises, facilities and information processing areas.

**Scope of This Section:**
This policy section defines comprehensive requirements for monitoring physical access to [Organization] facilities including:
- Access control systems (badge readers, logs, visitor management)
- Video surveillance (CCTV coverage, retention, review)
- Intrusion detection systems (motion sensors, door/window sensors, alarms)
- Security personnel (guards, patrols, Security Operations Center)
- Alarm systems (types, monitoring, response procedures)
- Integration with security operations (SIEM, incident management, dashboards)

### 1.2 Measurable Outcomes

Implementation of Control A.7.4 shall produce the following measurable outcomes:

**Access Logs:**
- Who entered which facility or area
- When access occurred (date, time)
- Success or failure of access attempt
- After-hours access events
- Retention: 90 days minimum (critical facilities), 30 days minimum (standard facilities)

**CCTV Footage:**
- Video coverage of all entry/exit points
- Video coverage of sensitive areas (server rooms, storage)
- Recording retention per policy
- Video available for incident investigation

**Incident Reports:**
- Physical security incidents documented
- Unauthorized access attempts documented
- Response time and resolution documented
- Root cause analysis completed

**Testing Records:**
- Access control system testing (quarterly)
- CCTV system testing (monthly)
- Intrusion detection testing (monthly)
- End-to-end security test (annual)

### 1.3 Facility Criticality and Control Requirements

Requirements vary by facility criticality tier (see POL-S1, Section 3.5):

**Tier 1 - Critical Facilities (Datacenters, Primary Server Rooms):**
- Access control: 24/7 badge system, multi-factor authentication for sensitive areas
- CCTV: 24/7 recording, 90-day retention, real-time monitoring
- Intrusion detection: 100% coverage, 24/7 monitoring, armed 24/7
- Security personnel: 24/7 presence or Security Operations Center monitoring
- Response time: <5 minutes for alarms

**Tier 2 - Standard Facilities (Offices, Branch Locations):**
- Access control: Business hours badge system, after-hours alarm
- CCTV: Business hours or motion-triggered recording, 30-day retention
- Intrusion detection: Entry points and sensitive areas, armed after-hours
- Security personnel: Business hours or contracted response
- Response time: <15 minutes for alarms

---

## 2. Physical Access Monitoring

### 2.1 Access Control System Requirements

#### 2.1.1 System Capabilities

[Organization] SHALL implement access control systems with the following capabilities:

**Badge/Card Reader Systems:**
- Electronic access control at all facility entry/exit points
- Technology: Proximity card (e.g., HID), smart card (e.g., PIV), or biometric (fingerprint, facial recognition)
- Multi-factor authentication for highly sensitive areas (e.g., server rooms in Tier 1 facilities)
- Integration with identity management system (automated badge provisioning/revocation upon hire/termination)

**Access Authorization:**
- Access rights assigned based on role and business need (principle of least privilege)
- Access levels: Public areas, general office, restricted areas (server rooms, storage), highly sensitive (executive areas, security operations)
- Temporary access for contractors and visitors (time-limited badges)
- Emergency access override (break-glass procedure with audit trail)

**Anti-Passback:**
- Anti-passback enabled for critical facilities (prevent badge sharing)
- Entry and exit readers at controlled points
- Timeout period configurable (typically 15-30 minutes)

**Door Control:**
- Automatic locking of doors after access granted (3-5 second hold time)
- Fail-safe vs. fail-secure configuration per door type:
  - Fail-safe (unlocked on power loss): Emergency exits, life safety egress
  - Fail-secure (locked on power loss): Server rooms, storage, perimeter doors
- Door position monitoring (detect door held open, forced entry)

#### 2.1.2 Access Log Requirements

All access events SHALL be logged with the following information:

**Required Log Fields:**
- User identity (name, employee ID, badge number)
- Location (building, floor, door ID, area name)
- Timestamp (date and time, timezone-aware)
- Access result (granted, denied)
- Access type (badge, PIN, biometric, manual override)
- Reason for denial (if denied): Invalid badge, insufficient privileges, anti-passback violation

**Access Log Retention:**
- Critical facilities (Tier 1): 365 days minimum
- Standard facilities (Tier 2): 90 days minimum
- Logs stored securely with access controls (read-only for auditors, full access for security operations)
- Logs backed up off-site (weekly minimum)

**Access Log Review:**
- Automated analysis: Daily (anomaly detection, unusual access patterns)
- Manual review:
  - Critical facilities: Weekly review of high-privilege access, after-hours access
  - Standard facilities: Monthly review of after-hours access
- Alert thresholds:
  - Failed access attempts: >3 attempts by same user within 5 minutes
  - After-hours access: Any access outside business hours (configurable per area)
  - Unusual patterns: Access to multiple buildings in short time, access from terminated employees (stale accounts)

#### 2.1.3 Visitor Management

**Visitor Sign-In Requirements:**
- All visitors SHALL sign in at reception or security desk
- Required information: Name, company, purpose of visit, host employee, expected duration
- Visitor badge issuance: Temporary badge (different color/design from employee badges), clearly marked "VISITOR"
- Photo ID verification for visitor identity (government-issued ID)

**Visitor Escort Requirements:**
- Escort required for visitors accessing:
  - Restricted areas (server rooms, storage, labs)
  - Any area beyond public reception/conference rooms (optional, risk-based)
- Escort responsibilities: Remain with visitor at all times, ensure visitor does not access unauthorized areas
- Escort assignment: Host employee or designated security personnel

**Visitor Badge Return:**
- Visitor SHALL return badge upon exit (verified by reception/security)
- Visitor sign-out: Record exit time
- Lost visitor badges: Deactivate immediately, investigate unauthorized access risk

**Contractor Access:**
- Long-term contractors (>30 days): Issue temporary employee badge with expiration date
- Background checks for contractors with access to sensitive areas (IT, facilities, security)
- Contractor access review: Monthly review of active contractor badges, revoke expired access

#### 2.1.4 Access Review and Recertification

**Quarterly Access Review:**
- Review all user access rights quarterly
- Identify stale accounts (no access activity in 90 days)
- Identify orphaned accounts (employees no longer with organization)
- Revoke unnecessary or excessive access

**Annual Access Recertification:**
- System owners certify access rights for their areas annually
- Managers certify direct report access rights annually
- Document recertification (approval records, revocation records)

**Automated Provisioning/Deprovisioning:**
- Integrate access control system with HR system
- New hire: Automatic badge provisioning upon hire date
- Termination: Automatic badge revocation upon termination date (immediate, no delay)
- Role change: Automatic access adjustment based on new role

### 2.2 Failed Access Attempt Detection

#### 2.2.1 Unauthorized Access Attempt Types

The access control system SHALL detect and alert on:

**Badge-Based Attempts:**
- Invalid badge (not in system, revoked, expired)
- Insufficient privileges (attempting to access area without authorization)
- Anti-passback violation (attempting to enter without prior exit)
- Tailgating detection (where available): Multiple persons entering on single badge swipe

**Physical Forced Entry:**
- Door forced open (door opened without valid badge swipe)
- Door held open beyond timeout (typically 30 seconds)
- Door propped open (continuous open state)

**Tampering:**
- Reader tampering (physical damage to card reader)
- System tampering (access control panel opened, power disconnected)

#### 2.2.2 Alert and Response Procedures

**Real-Time Alerts:**
- Failed access attempts: Alert to Security Operations Center (SOC) or security personnel
- Forced entry: Immediate alert with audio/visual alarm at security desk
- Multiple failed attempts (>3 in 5 minutes): Escalate to security personnel for investigation

**Incident Investigation:**
- Document all unauthorized access attempts (incident report)
- Review CCTV footage for visual confirmation (if available)
- Interview individuals involved (if identified)
- Determine root cause: Mistake (wrong door, forgotten badge), malicious attempt, system malfunction
- Take corrective action: Additional training, badge revocation, criminal charges (if applicable)

**Response Time Targets:**
- Critical facilities (Tier 1): Security personnel on-site within 5 minutes
- Standard facilities (Tier 2): Security personnel or contracted security on-site within 15 minutes

---

## 3. Physical Intrusion Detection

### 3.1 Intrusion Detection System (IDS) Requirements

#### 3.1.1 Sensor Types and Coverage

[Organization] SHALL implement intrusion detection systems with appropriate sensor types:

**Motion Sensors (PIR - Passive Infrared):**
- Purpose: Detect movement in interior spaces
- Placement: Ceiling-mounted or wall-mounted in corners for maximum coverage
- Coverage: Server rooms, telecom closets, storage rooms, sensitive areas
- Detection range: Typically 10-15 meters, 90-110 degree field of view
- Pet immunity: Configure to ignore small animals (if applicable, typically <25 kg)

**Door and Window Sensors (Magnetic Reed Switches):**
- Purpose: Detect opening of doors and windows
- Placement: All perimeter doors and ground-floor windows, doors to restricted areas
- Type: Surface-mount or recessed (recessed preferred for aesthetic and tamper resistance)
- Alarm on: Door/window opened while system armed

**Glass Break Detectors (Acoustic Sensors):**
- Purpose: Detect breaking of windows
- Placement: Ground floor windows, large glass panels, skylights
- Detection method: Acoustic signature of breaking glass
- Range: Typically 7-10 meters radius per detector

**Perimeter Intrusion Detection (Outdoor):**
- Purpose: Detect intrusion at facility perimeter (fences, barriers)
- Technology options:
  - Fence-mounted sensors (vibration, fiber optic)
  - Buried cable sensors (under ground near fence)
  - Infrared beam sensors (outdoor PIR)
  - Video analytics (CCTV-based motion detection)
- Coverage: Critical facilities (Tier 1) with high-value assets

#### 3.1.2 Sensor Coverage Requirements

**Critical Facilities (Tier 1):**
- Coverage: 100% of interior restricted areas (server rooms, storage, telecom)
- Coverage: 100% of perimeter entry points (all doors, ground-floor windows)
- Coverage: Perimeter intrusion detection (fence line, vehicle barriers)
- No blind spots (overlapping sensor coverage where feasible)

**Standard Facilities (Tier 2):**
- Coverage: All entry points (perimeter doors, accessible windows)
- Coverage: Sensitive areas (if any, e.g., small server room in office)
- Perimeter intrusion detection: Risk-based (optional for most office buildings)

#### 3.1.3 Arming Schedules and Zones

**Arming Zones:**
- Define zones based on areas (e.g., Zone 1: Building perimeter, Zone 2: Server room, Zone 3: Office areas)
- Independent arming per zone (allow partial arming: arm perimeter while office occupied)

**Arming Schedules:**
- Critical facilities (Tier 1): Armed 24/7 (perimeter and restricted areas)
- Standard facilities (Tier 2): Armed after business hours (perimeter), restricted areas armed 24/7 or when unoccupied

**Arming/Disarming:**
- Authorized personnel only (security personnel, facilities manager, system owners)
- Authentication required: PIN code + badge, or biometric
- Audit trail: Log all arm/disarm events (who, when, which zone)

### 3.2 Intrusion Detection Testing

#### 3.2.1 Testing Frequency

**Monthly Testing:**
- Walk test: Activate each motion sensor by walking through coverage area
- Door/window test: Open each door/window with system armed (trigger alarm)
- Verify alarm notifications received (email, SMS, security panel)
- Document test results (date, sensor ID, pass/fail, issues)

**Quarterly Testing:**
- End-to-end test: Trigger alarm, verify response procedure (security personnel dispatch, verification, reset)
- Test backup communication path (if cellular backup installed)

**Annual Testing:**
- Professional inspection by certified technician
- Sensor calibration and adjustment
- Battery backup test (verify sensors operate on battery during power loss)

#### 3.2.2 False Alarm Management

**False Alarm Causes:**
- User error (improper arming/disarming, forgot to disarm)
- Environmental factors (HVAC airflow triggering motion sensors, small animals)
- Equipment malfunction (sensor sensitivity too high, aging sensors)

**False Alarm Reduction:**
- Proper user training (arming/disarming procedures)
- Sensor adjustment (reduce sensitivity if frequent false alarms)
- Sensor replacement (aging sensors more prone to false alarms)
- Pet immunity configuration (if applicable)

**False Alarm Tracking:**
- Log all false alarms (date, time, zone, root cause)
- Target: <5 false alarms per month per facility
- If exceeding target: Investigate root cause, implement corrective action

---

## 4. Video Surveillance (CCTV)

### 4.1 Camera Coverage Requirements

#### 4.1.1 Mandatory Camera Coverage Areas

[Organization] SHALL provide CCTV coverage for the following areas:

**All Facilities (Tier 1 and Tier 2):**
- All building entrances and exits (exterior and interior views)
- All facility perimeter entry points (vehicle gates, pedestrian gates)
- Reception areas and visitor waiting areas
- Server rooms (interior view of racks and access door)
- Telecom closets and equipment rooms
- Parking areas (vehicular access points, not entire parking lot unless high-risk)

**Critical Facilities (Tier 1) Additional Coverage:**
- Building perimeter (exterior views of all sides)
- Loading docks and delivery areas
- Sensitive storage areas
- Emergency exits (interior and exterior views)
- Roof access points (if accessible)

**Optional Coverage (Risk-Based):**
- Interior office corridors (privacy considerations)
- Conference rooms (privacy considerations, typically NOT recorded)
- Outdoor perimeter (fence line continuous coverage)

#### 4.1.2 Camera Placement Principles

**Elimination of Blind Spots:**
- Overlapping camera coverage where feasible
- Multiple camera angles for critical areas (entrances: interior + exterior)
- Coverage of access paths (cannot bypass cameras to reach sensitive areas)

**Lighting Considerations:**
- Cameras positioned to avoid direct sunlight (backlight)
- Supplemental lighting for low-light areas (infrared illuminators, outdoor lighting)
- Camera low-light capability (see Section 4.2)

**Camera Height and Angle:**
- Face capture: 1.5-2 meters height, angled for facial recognition
- Overview coverage: Ceiling-mounted, wide-angle view
- License plate capture (if applicable): Positioned for plate reading (3-6 meters from vehicle path)

**Weatherproofing:**
- Outdoor cameras: IP66 or IP67 rated (weather-resistant)
- Indoor cameras: IP20 rated (basic protection)

### 4.2 Camera Specifications

#### 4.2.1 Resolution and Image Quality

**Minimum Resolution:**
- Critical areas (entrances, server rooms): 1080p (1920x1080, 2 megapixels) minimum
- High-security areas: 4K (3840x2160, 8 megapixels) for facial recognition
- General coverage (parking, perimeter): 720p (1280x720, 1 megapixel) acceptable

**Frame Rate:**
- Critical areas: 30 frames per second (fps) minimum (smooth motion)
- General coverage: 15 fps minimum (acceptable for most applications)
- Storage optimization: Lower frame rate reduces storage requirements (balance quality vs. storage)

**Low-Light Capability:**
- Day/night cameras: Automatic infrared (IR) cut filter switching
- Infrared illumination: Built-in IR LEDs for night vision (range: 10-30 meters typical)
- Low-lux sensors: Minimum illumination <0.1 lux (near darkness)
- Wide Dynamic Range (WDR): Compensate for bright and dark areas in same scene (e.g., entrance with bright sunlight outside)

#### 4.2.2 Camera Types

**Dome Cameras:**
- Use: Indoor applications, aesthetically pleasing
- Vandal resistance: Vandal-resistant dome housing (IK10 rating)
- Mounting: Ceiling-mounted or wall-mounted

**Bullet Cameras:**
- Use: Outdoor applications, long-range coverage
- Weatherproofing: IP66/IP67 rated
- Mounting: Wall-mounted with adjustable bracket

**PTZ (Pan-Tilt-Zoom) Cameras:**
- Use: Large areas requiring active monitoring (parking lots, perimeters)
- Features: Remote control (pan 360°, tilt ±90°, optical zoom 10-30×)
- Limitations: Cannot monitor entire area simultaneously (active monitoring only)
- Use cases: Security Operations Center with active monitoring, supplemental to fixed cameras

### 4.3 Video Recording and Retention

#### 4.3.1 Recording Infrastructure

**Network Video Recorder (NVR) or Video Management System (VMS):**
- Centralized recording system (NVR: standalone appliance, VMS: server-based software)
- Redundancy: RAID storage (RAID 5 or RAID 6 for fault tolerance)
- Backup: Off-site backup for critical facilities (weekly full backup, daily incremental)

**Storage Capacity Calculation:**
```
Storage (GB) = Number of Cameras × Bitrate (Mbps) × Recording Hours per Day × Retention Days × 0.0108

Example: 10 cameras × 4 Mbps × 24 hours × 90 days × 0.0108 = 933 GB (~1 TB)
```

**Storage Sizing Factors:**
- Resolution: Higher resolution = higher bitrate (1080p ~2-6 Mbps, 4K ~8-20 Mbps)
- Frame rate: 30 fps = 2× storage vs. 15 fps
- Compression: H.264 (standard) vs. H.265 (50% smaller, newer)
- Motion detection: Recording only on motion reduces storage (not recommended for critical areas)

#### 4.3.2 Retention Requirements

**Minimum Retention Periods:**
- Critical facilities (Tier 1): 90 days
- Standard facilities (Tier 2): 30 days
- Incident footage: Retain until incident resolved + 12 months (legal hold)

**Retention Extension:**
- Extend retention for ongoing investigations (legal, criminal, internal)
- Export incident footage to separate storage (preserve chain of custody)

**Automatic Deletion:**
- Oldest footage automatically overwritten when storage full (circular recording)
- No manual deletion without documented justification (audit trail)

### 4.4 Video Review and Access

#### 4.4.1 Authorized Access to Video Footage

**Access Controls:**
- Read-only access: Security operations, security manager, facilities manager, HR (incident investigations)
- Full access (delete, export): Security operations manager, CISO (strictly limited)
- Audit trail: Log all video access (who accessed which camera, when, what footage)

**Privacy Considerations:**
- Video review only for legitimate security or investigation purposes
- No surveillance of areas where privacy is expected (restrooms, locker rooms, private offices - these SHALL NOT be recorded)
- Employee awareness: Notify employees of CCTV coverage (signage, employee handbook)

#### 4.4.2 Video Review Procedures

**Incident Investigation:**
- Review footage within 24 hours of incident report
- Export relevant footage (incident evidence)
- Document review findings (who, what, when, evidence)

**Periodic Quality Assurance:**
- Monthly sampling: Review random footage samples (verify recording quality, camera alignment, coverage)
- Camera health check: Verify all cameras recording, no offline cameras
- Documentation: Monthly CCTV system health report

**Proactive Monitoring:**
- Security Operations Center (if applicable): Real-time monitoring of select cameras (entrances, high-risk areas)
- Video analytics (optional): Motion detection, loitering detection, perimeter breach detection
- Alert triggers: Unusual activity patterns, after-hours movement in restricted areas

### 4.5 CCTV System Testing

**Monthly Testing:**
- Verify recording: Check that all cameras are recording
- Verify retention: Check that footage from 30-90 days ago is still available
- Spot-check camera views: Ensure cameras not moved or obstructed

**Quarterly Testing:**
- Video quality review: Review footage from all cameras (assess image quality, lighting)
- NVR/VMS health check: Verify storage capacity, no disk errors

**Annual Testing:**
- Professional inspection: Camera cleaning, lens adjustment, cabling inspection
- Firmware updates: Update camera and NVR/VMS firmware (security patches)

---

## 5. Security Personnel Monitoring

### 5.1 Security Guard Duties (If Applicable)

For facilities with on-site security personnel:

#### 5.1.1 Patrol Schedules

**Critical Facilities (Tier 1):**
- Patrol frequency: Hourly patrols of all interior and exterior areas
- Patrol checkpoints: Physical checkpoints or electronic tracking (guard tour system)
- Patrol areas: Perimeter, parking, entrances, restricted areas (exterior check only)

**Standard Facilities (Tier 2):**
- Patrol frequency: Every 4 hours or as needed (business hours)
- After-hours: Contracted security response (alarm triggers only)

#### 5.1.2 Access Control Duties

**Visitor Management:**
- Verify visitor identity (photo ID check)
- Issue visitor badge
- Notify host employee of visitor arrival
- Escort visitors to/from secure areas (if escort required)
- Verify visitor badge return upon exit

**Employee Badge Verification:**
- Verify employee badges at entrance (visual check)
- Challenge individuals without visible badges
- Report lost or damaged badges to security operations

**Tailgating Prevention:**
- Monitor entrances for tailgating (multiple persons entering on single badge)
- Challenge individuals attempting to tailgate
- Educate employees on tailgating risks

#### 5.1.3 Incident Response

**First Responder:**
- Security guards are first responders to physical security incidents
- Incident types: Unauthorized access, intrusion alarm, fire alarm, medical emergency, disturbance

**Response Procedures:**
- Assess situation (observe, do not engage if dangerous)
- Notify appropriate authorities (police, fire, management)
- Secure area (prevent further access)
- Preserve evidence (do not disturb crime scene)
- Document incident (detailed incident report)

#### 5.1.4 Daily Security Log

**Log Contents:**
- Date and time
- Security personnel on duty (name, shift)
- Patrol completion times
- Visitor log (all visitors during shift)
- Incidents (all security incidents, no matter how minor)
- Alarm events (all alarms triggered, even false alarms)
- Observations (anything unusual, maintenance issues)

**Log Retention:**
- Security logs retained for 12 months minimum
- Log review: Security operations manager reviews logs weekly

### 5.2 Security Operations Center (SOC) Integration

#### 5.2.1 SOC Monitoring Scope

For organizations with a Security Operations Center (physical or logical security SOC):

**Physical Security Monitoring:**
- Access control events (failed access, forced entry, after-hours access)
- Intrusion alarm events (motion sensors, door/window sensors)
- CCTV alerts (motion detection, video analytics alerts)
- Environmental alarms (fire, water, temperature - see POL-S3)
- Utility alarms (power, HVAC, ISP - see POL-S4)

**Monitoring Hours:**
- Critical facilities: 24/7 SOC monitoring
- Standard facilities: Business hours SOC monitoring + after-hours escalation (on-call)

#### 5.2.2 SOC Response Procedures

**Alert Triage:**
- Classify alerts: Critical (immediate response), Warning (investigate within 1 hour), Informational (log only)
- Verify alert: Review CCTV footage, check access logs, confirm not false alarm

**Incident Escalation:**
- Critical incidents: Notify security manager, CISO, facilities manager (immediate)
- Standard incidents: Document, investigate, report in daily summary
- External escalation: Contact law enforcement (criminal activity), fire department (fire/medical), facilities (utility/environmental)

**Incident Documentation:**
- All incidents documented in incident management system
- Link physical security incidents to logical security events (correlation)
- Post-incident review: Root cause analysis, corrective actions

---

## 6. Physical Security Alarm System

### 6.1 Alarm Types

#### 6.1.1 Intrusion Alarms

**Source:** Intrusion detection system (see Section 3)
- Motion sensor triggered (movement detected)
- Door/window sensor triggered (opened while armed)
- Glass break sensor triggered (window broken)
- Perimeter sensor triggered (fence breach)

**Response:**
- Immediate alert to security personnel or SOC
- CCTV review (verify not false alarm)
- Security personnel dispatch (on-site verification)

#### 6.1.2 Access Control Alarms

**Source:** Access control system (see Section 2)
- Door forced open (opened without valid badge)
- Door held open (timeout exceeded)
- Multiple failed access attempts (>3 in 5 minutes)
- Anti-passback violation

**Response:**
- Alert to security personnel or SOC
- CCTV review (identify individual)
- Security personnel dispatch (if forced entry)

#### 6.1.3 Environmental Alarms

**Source:** Environmental monitoring systems (see POL-S3)
- Fire alarm (smoke/heat detected)
- Water alarm (water detected)
- Temperature alarm (too hot or too cold)

**Response:**
- Immediate alert to facilities manager and security personnel
- Response procedures per POL-S3

#### 6.1.4 Utility Alarms

**Source:** Utility monitoring systems (see POL-S4)
- Power alarm (UPS on battery, generator started, utility power loss)
- HVAC alarm (cooling unit failed, temperature rising)
- Network alarm (ISP circuit down)

**Response:**
- Immediate alert to facilities manager and IT operations
- Response procedures per POL-S4

#### 6.1.5 Duress Alarms

**Source:** Panic buttons or duress codes
- Panic button pressed (physical emergency button)
- Duress code entered (access control PIN code indicating duress)

**Response:**
- Immediate silent alarm to security personnel (do not alert perpetrator)
- Emergency services contacted (police, ambulance)
- CCTV review (assess situation)

### 6.2 Alarm Monitoring

#### 6.2.1 Monitoring Methods

**On-Site Monitoring:**
- Security personnel on-site respond to alarms
- Alarm panel at security desk with audio/visual alerts

**Central Station Monitoring:**
- Third-party monitoring service (UL-listed central station)
- Alarm signals transmitted to monitoring center (IP, cellular, phone line)
- Monitoring center dispatches security personnel or emergency services

**Security Operations Center (SOC) Monitoring:**
- Alarms integrated into SOC monitoring platform
- SOC analysts respond to alarms per procedures

#### 6.2.2 Monitoring Coverage

**Critical Facilities (Tier 1):**
- 24/7 alarm monitoring (no gaps)
- Primary method: SOC or central station monitoring
- Backup method: On-call security personnel (if SOC/central station unavailable)

**Standard Facilities (Tier 2):**
- Business hours: On-site security or SOC monitoring
- After-hours: Central station monitoring or on-call security personnel

#### 6.2.3 Alarm Communication Paths

**Primary Communication:**
- IP-based (network connection to monitoring center or SOC)
- Advantages: Fast, real-time, supports rich data (video, access logs)

**Backup Communication:**
- Cellular (4G/5G modem backup)
- Advantages: Independent of facility network, works during network outage
- Automatic failover: If IP connection lost, switch to cellular

**Testing:**
- Weekly: Test alarm transmission (automated test signal)
- Monthly: Test backup communication path (manually disable primary, verify backup)

### 6.3 Alarm Response Procedures

#### 6.3.1 Response Time Targets

**Critical Alarms (Intrusion, Duress, Fire):**
- Critical facilities (Tier 1): Security personnel on-site within 5 minutes
- Standard facilities (Tier 2): Security personnel or contracted response within 15 minutes

**Warning Alarms (Door Held Open, After-Hours Access):**
- Investigate within 1 hour
- CCTV review and documentation

**Informational Alarms (Successful Access, Patrol Checkpoint):**
- Log only, no immediate response

#### 6.3.2 Alarm Verification

**Before Dispatching Security Personnel:**
- Verify alarm via CCTV (if available)
- Check access logs (correlation with access events)
- Attempt contact with on-site personnel (if business hours)

**False Alarm Prevention:**
- Verify before dispatching law enforcement (avoid false alarm fees)
- Document all alarms (including false alarms, root cause)

#### 6.3.3 Alarm Resolution

**On-Site Verification:**
- Security personnel verify alarm condition (intrusion confirmed, false alarm, equipment malfunction)
- Secure area (if intrusion confirmed)
- Reset alarm system (after verification)

**Incident Documentation:**
- Document alarm event (date, time, alarm type, location)
- Document response (who responded, verification results)
- Document resolution (alarm reset, incident escalated, law enforcement contacted)

### 6.4 Alarm Testing

**Monthly Testing:**
- Test all alarm zones (trigger each sensor, verify alarm received)
- Document test results (date, zone ID, pass/fail)

**Quarterly Testing:**
- End-to-end test (trigger alarm, verify monitoring center receives signal, verify security personnel dispatched)
- Test backup communication path (disable primary, verify alarm via cellular)

**Annual Testing:**
- Professional inspection (certified alarm technician)
- Replace batteries (control panel, sensors)
- Update firmware (control panel, communication modules)

---

## 7. Integration with Security Operations

### 7.1 SIEM Integration

#### 7.1.1 Physical Security Event Logging

Physical security events SHALL be forwarded to Security Information and Event Management (SIEM) system:

**Access Control Events:**
- All access events (granted, denied)
- Failed access attempts
- After-hours access
- Administrative events (user added, badge revoked)

**Intrusion Detection Events:**
- All alarm events (motion sensor, door/window sensor)
- Arm/disarm events
- System tampering events

**CCTV Events:**
- Camera offline/online events
- Recording started/stopped events
- Video analytics alerts (if applicable)

#### 7.1.2 Event Correlation

**Cross-Domain Correlation:**
- Physical access events + Logical access events (same user, same timeframe)
  - Example: Badge swipe at server room door + RDP login to server (verify authorized access)
- Physical intrusion + Network anomaly (potential insider threat)
  - Example: After-hours intrusion alarm + unusual network traffic (investigate data exfiltration)
- Failed physical access + Failed logical access (potential attack)
  - Example: Multiple failed badge swipes + multiple failed login attempts (brute force attack)

**Alert Rules:**
- After-hours access to restricted areas (generate SIEM alert for investigation)
- Unusual access patterns (access to multiple buildings in short timeframe)
- Terminated employee physical or logical access attempt (high-priority alert)

### 7.2 Incident Management Integration

#### 7.2.1 Physical Security Incident Classification

Physical security incidents SHALL be classified and managed per ISMS incident management procedures:

**Incident Severity:**
- **Critical:** Unauthorized access to restricted areas, physical breach, theft, violence
- **High:** Repeated failed access attempts, tailgating, lost/stolen badges
- **Medium:** Door held open, false alarm (if frequent), visitor policy violation
- **Low:** Single failed access (user error), minor policy violation

**Incident Response:**
- Critical/High incidents: Immediate response per incident management plan (POL-A.5.24-27)
- Medium/Low incidents: Document, investigate, corrective action

#### 7.2.2 Forensic Evidence Collection

For physical security incidents requiring investigation:

**Evidence Types:**
- Access control logs (before, during, and after incident)
- CCTV footage (multiple camera angles, extended timeframe)
- Intrusion alarm logs
- Security guard logs (observations, actions taken)
- Physical evidence (damaged equipment, missing items)

**Chain of Custody:**
- Document evidence collection (who, when, what, where)
- Secure evidence storage (prevent tampering)
- Maintain chain of custody (all persons accessing evidence)
- Preserve evidence (no deletion, no alteration)

**Evidence Retention:**
- Incident evidence retained for duration of investigation + 12 months
- Legal hold: Retain indefinitely if litigation or criminal prosecution

### 7.3 Physical Security Dashboard

#### 7.3.1 Dashboard Metrics

Real-time dashboard SHALL display key physical security metrics:

**Access Monitoring:**
- Total access events (today, this week)
- Failed access attempts (count, trend)
- After-hours access events (count, areas accessed)
- Active visitor count (visitors currently on-site)

**Intrusion Detection:**
- Alarm events (today, this week)
- False alarm rate (target: <5 per month)
- Active alarms (currently unresolved)

**CCTV:**
- Camera status (online, offline, total)
- Recording status (all cameras recording: yes/no)
- Storage capacity (GB used, GB available, days remaining)

**Incidents:**
- Open incidents (unresolved physical security incidents)
- Incident trend (incidents per month, severity distribution)

#### 7.3.2 Dashboard Access

**Authorized Viewers:**
- Security Operations Center (real-time monitoring)
- Security Operations Manager (daily review)
- CISO (weekly review)
- Facilities Manager (daily review of environmental/utility alarms)
- Executive Management (monthly summary)

**Dashboard Locations:**
- SOC monitoring wall (large display)
- Security operations manager workstation
- Web-based access (secure portal, role-based access)

---

## 8. Measurable Requirements and Audit Verification

### 8.1 Compliance Metrics

The following metrics SHALL be measured to demonstrate Control A.7.4 compliance:

#### 8.1.1 Coverage Metrics

**Access Control Coverage:**
- Metric: Percentage of entry/exit points with electronic access control
- Target: 100% (critical facilities), 100% perimeter + sensitive areas (standard facilities)
- Measurement: Count of doors with badge readers / Total count of entry/exit points
- Audit evidence: Access control system configuration, facility floor plans

**CCTV Coverage:**
- Metric: Percentage of required areas with CCTV coverage
- Target: 100% of required areas (see Section 4.1)
- Measurement: Count of covered areas / Total count of required areas
- Audit evidence: Camera coverage map, camera placement documentation

**Intrusion Detection Coverage:**
- Metric: Percentage of sensitive areas with intrusion detection
- Target: 100% (critical facilities), 100% entry points + sensitive areas (standard facilities)
- Measurement: Count of protected areas / Total count of sensitive areas
- Audit evidence: Intrusion detection system configuration, sensor placement map

#### 8.1.2 Operational Metrics

**Access Log Retention:**
- Metric: Days of access logs retained
- Target: 365 days (critical facilities), 90 days (standard facilities)
- Measurement: Date of oldest access log record
- Audit evidence: Access control system backup logs, sample access log export

**CCTV Retention:**
- Metric: Days of CCTV footage retained
- Target: 90 days (critical facilities), 30 days (standard facilities)
- Measurement: Date of oldest video footage
- Audit evidence: NVR/VMS storage report, sample video file dates

**Failed Access Attempts:**
- Metric: Count of failed access attempts per month
- Target: <5 per month (legitimate failures, not attacks)
- Measurement: Access log analysis (failed attempts count)
- Audit evidence: Monthly failed access attempt report

**Incident Response Time:**
- Metric: Average time from alarm to security personnel on-site
- Target: <5 minutes (critical facilities), <15 minutes (standard facilities)
- Measurement: Alarm timestamp to security arrival timestamp
- Audit evidence: Incident reports, security guard logs

**Physical Security Incidents:**
- Metric: Count of physical security incidents per year
- Target: <2 per year (excluding false alarms)
- Measurement: Incident management system query (physical security incidents)
- Audit evidence: Incident reports (past 12 months)

#### 8.1.3 Testing Compliance Metrics

**Access Control Testing:**
- Metric: Percentage of required tests completed on time
- Target: 100%
- Measurement: Count of completed tests / Count of required tests (quarterly)
- Audit evidence: Access control test logs (past 12 months)

**CCTV Testing:**
- Metric: Percentage of required tests completed on time
- Target: 100%
- Measurement: Count of completed tests / Count of required tests (monthly)
- Audit evidence: CCTV test logs (past 12 months)

**Intrusion Detection Testing:**
- Metric: Percentage of required tests completed on time
- Target: 100%
- Measurement: Count of completed tests / Count of required tests (monthly)
- Audit evidence: Intrusion detection test logs (past 12 months)

### 8.2 Audit Evidence

#### 8.2.1 Configuration Evidence

**Access Control System:**
- System configuration documentation (access levels, user groups, door assignments)
- Network diagram (access control panel, readers, network topology)
- Integration documentation (HR system integration, SIEM integration)

**CCTV System:**
- Camera coverage map (floor plans with camera locations and coverage areas)
- Camera specifications (model, resolution, frame rate per camera)
- NVR/VMS configuration (retention settings, storage capacity, backup configuration)

**Intrusion Detection System:**
- Sensor placement map (floor plans with sensor locations)
- System configuration (zones, arming schedules, notification settings)
- Alarm response procedures

#### 8.2.2 Operational Evidence

**Access Logs:**
- Sample access logs (30-day sample from past 12 months)
- Failed access attempt reports (monthly reports, past 12 months)
- Access review records (quarterly access recertification approvals)

**CCTV Footage:**
- Sample video footage (verify retention, quality)
- Video review logs (incident investigation video reviews)
- Camera health reports (monthly reports, past 12 months)

**Intrusion Detection Logs:**
- Alarm event logs (past 12 months)
- False alarm investigation reports
- Sensor test logs (monthly, past 12 months)

**Incident Reports:**
- Physical security incident reports (past 12 months)
- Root cause analysis (for major incidents)
- Corrective action completion verification

#### 8.2.3 Testing Evidence

**Testing Records:**
- Access control test logs (quarterly tests, past 12 months)
- CCTV test logs (monthly tests, past 12 months)
- Intrusion detection test logs (monthly tests, past 12 months)
- End-to-end security test reports (annual test)

**Maintenance Records:**
- Maintenance logs (routine maintenance, repairs)
- Vendor service reports (annual inspections)
- Firmware update logs (security patches applied)

### 8.3 Testing Requirements

#### 8.3.1 Quarterly Testing

**Access Control System Test:**
- Test badge access (all doors, all user groups)
- Test denied access (revoked badge, insufficient privileges)
- Test alerts (failed access, forced entry)
- Document results (pass/fail, issues)

**End-to-End Physical Security Test:**
- Trigger intrusion alarm (motion sensor or door sensor)
- Verify alarm notification (SOC, security personnel, monitoring center)
- Verify CCTV review (security personnel reviews footage)
- Verify response (security personnel dispatched, alarm verified, incident documented)
- Document results (response time, issues)

#### 8.3.2 Monthly Testing

**CCTV System Test:**
- Verify recording (all cameras recording)
- Verify retention (footage from 30-90 days ago available)
- Spot-check camera views (verify camera alignment, no obstructions)
- Document results

**Intrusion Detection System Test:**
- Walk test (trigger each motion sensor)
- Door/window test (trigger each door/window sensor)
- Verify alarm notification
- Document results

#### 8.3.3 Annual Testing

**Professional Inspection:**
- Access control system: Professional inspection by certified technician
- CCTV system: Professional inspection (camera cleaning, lens adjustment)
- Intrusion detection system: Professional inspection (sensor calibration)
- Documentation: Inspection reports, maintenance recommendations

---

## 9. Cloud and Colocation Considerations

### 9.1 Cloud Environments

**Physical Security Monitoring is Cloud Provider Responsibility:**

For organizations operating 100% in cloud environments (AWS, Azure, GCP) with no on-premises datacenters or information processing facilities:

- **Control A.7.4 applicability:** Not Applicable (mark as "Not Applicable" in Statement of Applicability)
- **Rationale:** Cloud providers manage physical infrastructure and physical security monitoring
- **Organization's responsibility:** Assess cloud provider physical security controls through supplier management (Control A.5.19-23)

**Supplier Assessment Approach:**

**Audit Report Review:**
- Obtain cloud provider SOC 2 Type II report (review physical security controls section)
- Obtain cloud provider ISO 27001 certification (review physical security controls A.7.1-7.14)
- Verify physical security controls implemented:
  - Physical access control (badge systems, biometric authentication)
  - Video surveillance (CCTV coverage, retention)
  - Intrusion detection (perimeter security, interior monitoring)
  - Security personnel (24/7 guards, Security Operations Centers)
  - Alarm systems (integrated monitoring)

**Physical Security Verification:**
- Review audit reports annually (when updated)
- Verify no adverse findings in physical security controls
- Document supplier assessment (annual cloud provider security review)

**Office Physical Security:**
- Even cloud-only organizations typically have office premises
- Office physical security addressed via Control A.7.1-3 (Physical Access Control)
- This control (A.7.4) focuses on information processing facilities, not general offices

### 9.2 Colocation Facilities

**Shared Responsibility Model:**

For organizations utilizing colocation datacenter facilities:

#### 9.2.1 Provider Responsibilities (Typical)

**Colocation Provider Manages:**
- Building perimeter security (fencing, vehicle barriers, exterior access control)
- Building-wide CCTV (exterior and common areas)
- Building intrusion detection (perimeter and common areas)
- 24/7 security personnel (reception, patrols, monitoring)
- Visitor management (sign-in, escort from lobby to cage)
- Physical security monitoring (Security Operations Center for building)

**Provider Evidence:**
- SOC 2 Type II report (physical security controls section)
- ISO 27001 certification (if available)
- Uptime Institute Tier Certification (if available)
- Physical security incident reports (quarterly reports to customers)
- SLA reports (physical security uptime, incident response times)

#### 9.2.2 Customer Responsibilities (Typical)

**[Organization] Manages:**
- Cage/suite access control (secondary access layer: badge readers, locks)
- Internal CCTV within cage/suite (optional but recommended for audit evidence)
- Equipment physical security (rack locks, cable locks, equipment anchoring)
- Visitor escort within cage/suite (after provider escort to cage entrance)
- Equipment-level intrusion detection (optional, for highly sensitive equipment)

**Customer Implementation:**
- Install cage-level access control (badge readers on cage door)
- Install internal CCTV cameras (coverage of equipment racks)
- Maintain access logs (who accessed cage, when)
- Review provider incident reports (monthly review of provider SLA reports)

#### 9.2.3 Responsibility Matrix Documentation

Maintain formal responsibility matrix in colocation contract:

| Physical Security Control | Provider | Customer |
|---------------------------|----------|----------|
| Perimeter security (fence, gates) | ✅ | - |
| Building access control | ✅ | - |
| Building CCTV (exterior, common areas) | ✅ | - |
| Building intrusion detection | ✅ | - |
| Security personnel (24/7) | ✅ | - |
| Visitor management (lobby sign-in) | ✅ | - |
| Cage/suite access control | - | ✅ |
| Cage/suite CCTV (interior) | - | ✅ (optional) |
| Equipment rack locks | - | ✅ |
| Visitor escort (within cage) | - | ✅ |
| Physical security incident response | ✅ (building) | ✅ (cage/equipment) |

#### 9.2.4 Verification and Audit

**Annual Provider Verification:**
- Request updated SOC 2 Type II report (annual)
- Review provider audit findings (verify no adverse physical security findings)
- Review provider SLA reports (physical security incident count, response times)
- Site visit (annual or biennial): Physical inspection of provider security controls

**Customer Audit Evidence:**
- Responsibility matrix (documented in colocation contract)
- Provider audit reports (SOC 2, ISO 27001)
- Provider SLA reports (past 12 months)
- Customer-implemented controls evidence:
  - Cage access logs (sample 30 days)
  - Cage CCTV footage (if implemented)
  - Equipment physical security documentation (rack locks, cable locks)
- Annual provider verification documentation

---

## 10. Related Documents

**Framework Sections:**
- **ISMS-POL-A.7.4-5-11-S1:** Executive Summary, Control Alignment, Scope (this framework foundation)
- **ISMS-POL-A.7.4-5-11-S3:** Environmental Protection (A.7.5) - fire, flood, temperature protection
- **ISMS-POL-A.7.4-5-11-S4:** Utility Resilience (A.7.11) - power, HVAC, telecommunications
- **ISMS-POL-A.7.4-5-11-S5:** Assessment Methodology and Evidence Framework
- **ISMS-IMP-A.7.4-5-11-S1:** Physical Monitoring Implementation (access control, CCTV, intrusion detection deployment)
- **ISMS-IMP-A.7.4-5-11-S4:** Facilities Assessment (ongoing compliance monitoring)

**Related ISMS Policies:**
- **ISMS-POL-A.7.1-3:** Physical Access Control (entry/exit security baseline, prerequisite for monitoring)
- **ISMS-POL-A.5.24-27:** Incident Management (physical security incident handling procedures)
- **ISMS-POL-A.5.19-23:** Information Security for Use of Cloud Services (cloud provider physical security assessment)

**External Standards:**
- **ISO/IEC 27001:2022:** Control A.7.4 - Physical Security Monitoring
- **ISO/IEC 27002:2022:** Detailed guidance for Control A.7.4
- **NIST SP 800-53 Rev 5:** Physical and Environmental Protection (PE) family

---

**END OF ISMS-POL-A.7.4-5-11-S2**

---

**Document Approval Signatures:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Author | [Name] | | |
| Security Operations Manager | [Name] | | |
| Facilities Manager | [Name] | | |
| CISO | [Name] | | |

---

*"Physical security monitoring is not surveillance theater. It's systematic detection of unauthorized access through access control logs, video surveillance, intrusion detection, and security personnel—all integrated into a unified security operations framework that enables rapid detection and response."*
