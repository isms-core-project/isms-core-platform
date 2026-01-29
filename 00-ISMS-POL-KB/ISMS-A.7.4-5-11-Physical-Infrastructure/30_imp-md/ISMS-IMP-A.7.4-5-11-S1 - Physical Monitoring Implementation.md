# ISMS-IMP-A.7.4-5-11-S1: Physical Monitoring Implementation

**Document Classification:** Internal - ISMS Implementation Guide  
**Version:** 1.0  
**Effective Date:** [To be defined]  
**Review Cycle:** Annual  
**Owner:** Security Operations Manager / Facilities Manager  
**Approved By:** CISO

---

## Purpose

This implementation guide provides step-by-step procedures for deploying and operating physical security monitoring systems to meet Control A.7.4 requirements (see POL-S2).

**Scope:** Access control systems, CCTV surveillance, intrusion detection, security personnel operations, alarm systems.

**Target Audience:** Security Operations staff, Facilities Management, IT Operations, System Integrators.

---

## Table of Contents

1. [Access Control System Deployment](#1-access-control-system-deployment)
2. [CCTV System Deployment](#2-cctv-system-deployment)
3. [Intrusion Detection System Deployment](#3-intrusion-detection-system-deployment)
4. [Security Personnel Operations](#4-security-personnel-operations)
5. [Monitoring Integration](#5-monitoring-integration)
6. [Common Issues and Troubleshooting](#6-common-issues-and-troubleshooting)

---

## 1. Access Control System Deployment

### 1.1 Pre-Deployment Planning

**Step 1: Facility Survey**
- Walk facility perimeter and identify all entry/exit points (main entrance, emergency exits, loading dock, roof access)
- Document: List of doors requiring access control (prioritize: perimeter doors, server room doors, storage room doors)
- Consider: Employee flow patterns, visitor flow, delivery access

**Step 2: Select Access Control System**
- **Small facilities (<20 doors):** Cloud-based system (Verkada, Kastle, Brivo) - lower upfront cost, subscription model
- **Medium facilities (20-100 doors):** Hybrid system (HID, Honeywell) - mix of local controllers and cloud management
- **Large facilities (>100 doors):** Enterprise system (Lenel, AMAG, Software House) - on-premises servers, scalable

**Key Selection Criteria:**
- Integration with HR system (automatic badge provisioning/revocation)
- Integration with SIEM (log forwarding, see Section 5)
- Mobile credentials support (phone as badge - optional but convenient)
- Scalability (can add doors/facilities as organization grows)

**Step 3: Design Access Levels**
- Public areas: No access control (lobby, reception)
- General office: All employees
- Restricted areas: Server rooms (IT staff only), storage (authorized personnel), executive suite (executives + assistants)
- Highly sensitive: Security operations, evidence room (SOC staff only)

### 1.2 Hardware Installation

**Badge Readers:**
- Install card readers at all identified entry/exit points (exterior and interior side for anti-passback)
- Mounting height: 42-48 inches (wheelchair accessible)
- Reader type: Proximity (HID Prox), smart card (HID iCLASS), mobile (HID Mobile Access)
- Wiring: Cat6 cable from reader to access control panel (max 500 feet, use fiber for longer runs)

**Door Strikes/Locks:**
- Electric strike (for wooden doors) - install in door frame, replace mechanical strike plate
- Magnetic lock (for metal/glass doors) - mount on door frame, install magnet on door
- Fail-safe (unlocks on power loss - emergency exits) vs. Fail-secure (locks on power loss - perimeter/server rooms)

**Access Control Panels:**
- Install panels in secure location (electrical room, server room - not publicly accessible)
- Power: Dedicated circuit (15A minimum), UPS-protected (see POL-S4)
- Network: Ethernet connection to network switch (VLAN for security systems recommended)

**Request-to-Exit (REX) Sensors:**
- Install motion sensor on interior side of door (allows exit without badge, prevents tailgating alarm)
- Mounting: Above door on interior side, coverage of door approach path

### 1.3 Software Configuration

**Step 1: System Commissioning**
- Power on access control panels, verify network connectivity
- Install management software (if on-premises) or access cloud portal (if cloud-based)
- Add access control panels to system (discover via network scan or manual entry)

**Step 2: Configure Doors**
- Add all doors to system (name: "Building A - Main Entrance", "Server Room Door 1")
- Configure door properties:
  - Fail-safe or fail-secure
  - Auto-relock time (3-5 seconds typical)
  - Anti-passback (enable for critical facilities, 15-30 min timeout)
  - Door held open alarm (30 seconds)

**Step 3: Create Access Levels**
- Define access levels per Step 1.1 (Public, General Office, Restricted, Highly Sensitive)
- Assign doors to access levels (General Office level = all office doors, Restricted level = server room doors)

**Step 4: Add Users**
- Import users from HR system (if integration available) or manually enter
- Assign badge numbers (print/encode cards)
- Assign access levels to users (based on role)
- Set temporary access (contractors - expiration date)

**Step 5: Configure Logging**
- Enable all event logging (access granted, access denied, door forced, door held open)
- Set log retention (365 days critical facilities, 90 days standard - see POL-S2, Section 2.1.2)
- Configure log forwarding to SIEM (if available, see Section 5)

### 1.4 Testing and Validation

**Functional Testing:**
- Test each door: Badge swipe → Door unlocks → Door relocks after timeout
- Test denied access: Invalid badge → Door remains locked → Alarm logged
- Test anti-passback (if enabled): Enter without exit → Attempt re-entry → Denied → Alarm logged
- Test door forced: Open door without badge → Alarm triggered → Logged
- Test REX sensor: Approach door from interior → Door unlocks → No alarm

**User Acceptance Testing:**
- Select sample users from each access level → Test access to authorized doors (success) and unauthorized doors (denied)
- Test visitor workflow: Sign in → Temporary badge → Access lobby/conference rooms → Sign out → Badge disabled

**Performance Testing:**
- Peak load: Simulate multiple users accessing doors simultaneously (shift change, emergency evacuation)
- Network latency: Verify door unlock time <2 seconds (from badge swipe to unlock)

### 1.5 User Training and Rollout

**Employee Training:**
- Badge use: How to swipe badge, wear badge visibly, do not share badge
- Lost badge: Report immediately to security/HR, badge will be revoked and replaced
- Tailgating: Do not allow others to follow through door without badge ("buddy door" is security violation)

**Visitor Management Training:**
- Reception staff: How to issue visitor badges, verify photo ID, record visitor information, ensure badge return

**Go-Live:**
- Phase 1 (Week 1): Deploy to main entrances only (test high-traffic areas)
- Phase 2 (Week 2-3): Deploy to remaining perimeter doors
- Phase 3 (Week 4): Deploy to interior restricted areas (server rooms, storage)

---

## 2. CCTV System Deployment

### 2.1 Pre-Deployment Planning

**Step 1: Identify Coverage Requirements**
- Mandatory areas (see POL-S2, Section 4.1.1): All building entrances/exits, server rooms, parking entrances, reception
- Optional areas: Hallways, perimeter, loading dock (risk-based)

**Step 2: Camera Count and Placement**
- Entrances: Minimum 2 cameras per entrance (interior + exterior view)
- Server rooms: 1-2 cameras (view of door + view of racks)
- Parking: Cameras at vehicle entry/exit points (license plate capture if desired - requires specialized camera)
- Estimate total camera count: Small office (10-20 cameras), medium office (20-50), datacenter (50-200)

**Step 3: Select CCTV System**
- **Cloud-based NVR:** Verkada, Meraki, Eagle Eye (subscription model, no on-premises servers)
- **On-premises NVR:** Milestone, Genetec, Hanwha (upfront cost for servers, perpetual license)
- Hybrid: Some systems offer both (Axis Camera Station)

**Step 4: Calculate Storage**
```
Storage (TB) = Cameras × Bitrate (Mbps) × Recording Hours/Day × Retention Days × 0.0108

Example: 20 cameras × 4 Mbps × 24 hrs × 90 days × 0.0108 = 1.86 TB (~2 TB)

Add 50% buffer for growth: 2 TB × 1.5 = 3 TB recommended
```

### 2.2 Hardware Installation

**Camera Installation:**
- Mount cameras per placement plan (wall-mount for bullet cameras, ceiling-mount for dome cameras)
- Mounting height: 8-12 feet (above tampering reach, below light fixture glare)
- Camera aiming: Test field of view before final mounting (use laptop to view camera, adjust angle)
- Cabling: Cat6 (PoE cameras - power and data over single cable), max 300 feet (use fiber for longer runs)

**PoE Network Switches:**
- Install PoE switches to power cameras (24-port or 48-port PoE switches, calculate PoE budget: cameras × 15-30W per camera)
- UPS-protect switches (see POL-S4 - cameras inoperable during power loss otherwise)

**NVR (Network Video Recorder) Server:**
- On-premises NVR: Install server in secure location (server room), RAID storage (RAID 5/6 for fault tolerance)
- Storage capacity: Per calculation above (3 TB in example, use 4× 2TB drives in RAID 5)
- UPS-protect NVR server (see POL-S4)

### 2.3 Software Configuration

**Step 1: Add Cameras to NVR**
- Discover cameras on network (auto-discovery or manual IP entry)
- Configure camera settings:
  - Resolution: 1080p minimum (4K for critical areas like server room entrance)
  - Frame rate: 30 fps critical areas, 15 fps general areas (balance quality vs. storage)
  - Compression: H.264 (standard) or H.265 (50% smaller files, newer cameras)
  - Low-light mode: Auto IR (infrared) for outdoor or dark areas

**Step 2: Configure Recording**
- Continuous recording: 24/7 (recommended for critical areas - entrances, server rooms)
- Motion-triggered recording: Record only on motion (saves storage, acceptable for low-traffic areas like parking)
- Set retention: 90 days (critical facilities), 30 days (standard facilities - see POL-S2, Section 4.3.2)

**Step 3: Configure Access Control**
- User accounts: Create accounts for security personnel (view/export), facilities manager (view/export), CISO (view/export/admin)
- Audit logging: Enable login/logout logging, video export logging

**Step 4: Configure Alerts (Optional)**
- Motion detection alerts: Alert on motion in after-hours areas (server rooms, storage)
- Camera offline alerts: Alert if camera loses connection (immediate notification to facilities)

### 2.4 Testing and Validation

**Image Quality Testing:**
- Daytime: Verify clear image quality, no glare, proper framing
- Nighttime: Verify IR illumination adequate, no excessive noise
- Walk test: Person walks through camera view, verify face identifiable (if camera purpose is identification)

**Recording Verification:**
- Verify all cameras recording to NVR (check recording status indicator)
- Verify motion triggers recording (if motion-triggered)
- Playback test: Select timestamp, verify playback smooth (no stuttering, no dropped frames)

**Retention Verification:**
- After 30/90 days (depending on retention setting), verify oldest footage still available
- Test circular recording: Verify oldest footage overwritten when storage full (no recording stoppage)

---

## 3. Intrusion Detection System Deployment

### 3.1 Pre-Deployment Planning

**Step 1: Identify Protected Areas**
- Critical facilities: All perimeter doors/windows, all interior restricted areas (server rooms, storage, telecom closets)
- Standard facilities: All perimeter doors, ground-floor windows, interior restricted areas (if any)

**Step 2: Select Intrusion Detection System**
- Wired system (traditional): Hardwired sensors to alarm panel (most reliable, installation labor-intensive)
- Wireless system (modern): Wireless sensors communicate with hub (easier installation, battery-powered sensors require battery replacement)
- Hybrid: Mix of wired (perimeter) and wireless (interior)

**Common Systems:** Honeywell (Vista), DSC (PowerSeries), Bosch, 2GIG (wireless)

**Step 3: Design Zones**
- Zone 1: Building perimeter (all exterior doors, ground-floor windows)
- Zone 2: Server room (motion sensors, door sensor)
- Zone 3: Office areas (interior doors if applicable)
- Zone design allows independent arming (arm perimeter 24/7, arm office areas after-hours only)

### 3.2 Hardware Installation

**Door/Window Sensors:**
- Install magnetic reed switch on all perimeter doors and ground-floor windows (sensor on frame, magnet on door/window)
- Wiring: Run sensor wires back to alarm panel (22 AWG 2-conductor wire), or use wireless sensors (no wiring)

**Motion Sensors (PIR):**
- Install in corners of rooms for maximum coverage (90-110 degree field of view, 10-15 meter range)
- Mounting height: 6-8 feet (wall-mount or ceiling-mount depending on room geometry)
- Avoid: Heating vents (false alarms from hot air), windows (false alarms from sunlight), pets (if present, use pet-immune sensors)

**Glass Break Detectors:**
- Install within 7-10 meters of large windows or glass doors (acoustic sensor detects breaking glass sound signature)
- Mounting: On wall or ceiling facing windows

**Alarm Panel:**
- Install in secure location (server room, electrical room - not publicly accessible)
- Power: Dedicated circuit + backup battery (12V 7Ah battery, 24-hour backup minimum)
- Network: Ethernet or cellular for monitoring connection (dual-path recommended for critical facilities)

**Keypads:**
- Install keypad near entrances (interior side) for arming/disarming (1-2 keypads for small facilities, 3-5 for large)
- Mounting height: 48-60 inches

### 3.3 Software Configuration

**Step 1: Program Alarm Panel**
- Add sensors to panel (wired: auto-enroll or manually configure zone numbers, wireless: enroll via learn mode)
- Configure sensor types: Entry/exit delay (entrance doors - 30-60 sec delay), instant (windows, interior doors, motion sensors)
- Configure zones (Zone 1 = Perimeter, Zone 2 = Server Room, etc.)

**Step 2: Configure Arming Schedules**
- Critical facilities: Zone 1 (Perimeter) armed 24/7, Zone 2 (Server Room) armed 24/7 or when unoccupied
- Standard facilities: Arm all zones after business hours (auto-arm at 6 PM, disarm at 7 AM)

**Step 3: Create User Codes**
- Master code: Facilities manager, security manager (all privileges)
- User codes: Employees authorized to arm/disarm (unique codes for audit trail)
- Duress code: Appears to disarm but triggers silent alarm to monitoring center

**Step 4: Configure Monitoring**
- If using monitoring service: Enter monitoring center phone number or IP address, test communication path
- If self-monitoring: Configure alarm output to Security Operations Center or on-call personnel (email, SMS, phone call)

### 3.4 Testing and Validation

**Sensor Testing (Walk Test):**
- Trigger each motion sensor (walk through coverage area), verify alarm panel registers trigger
- Open each door/window with system armed, verify alarm triggered
- Test glass break detector (use glass break simulator tool or app), verify alarm triggered

**Communication Testing:**
- Trigger alarm, verify monitoring center receives signal (call monitoring center to confirm)
- Test backup communication path (disconnect primary Ethernet, verify cellular backup transmits alarm)

**False Alarm Testing:**
- Identify potential false alarm sources (HVAC airflow, pets, user error)
- Adjust sensor sensitivity or placement if excessive false alarms

---

## 4. Security Personnel Operations

### 4.1 Security Guard Duties (If Applicable)

**Reception Duties:**
- Greet visitors, verify photo ID, issue visitor badge
- Log visitor information (name, company, host employee, time in/out)
- Notify host employee of visitor arrival
- Escort visitors if required (to/from restricted areas)

**Patrol Duties:**
- Hourly patrols of facility perimeter and interior (critical facilities)
- Use guard tour system (physical checkpoints or electronic wand) to document patrols
- Check for: Unlocked doors, lights left on, suspicious activity, safety hazards

**Monitoring Duties:**
- Monitor CCTV cameras (live view of high-risk areas - entrances, parking, server rooms)
- Respond to alarms (access control, intrusion detection, environmental - see POL-S3)
- Document all events in daily security log

### 4.2 Daily Security Log

**Log Contents:**
- Date, shift (day/evening/night), security personnel on duty
- Patrol completion times (Patrol 1: 08:00, Patrol 2: 09:00, etc.)
- Visitor log (all visitors during shift)
- Alarm events (access denied, intrusion alarm, environmental alarm)
- Incidents (unauthorized access attempt, disturbance, medical emergency)
- Observations (damaged fence, lighting out, maintenance needed)

**Log Retention:** 12 months (see POL-S2, Section 5.1.4)

### 4.3 Incident Response Procedures

**Intrusion Alarm Response:**
1. Receive alarm notification (alarm panel, phone call from monitoring center, dashboard alert)
2. Verify alarm via CCTV (review cameras near alarm zone)
3. If false alarm: Reset alarm, document in log
4. If intrusion confirmed: Do NOT confront intruder (call police), secure area, preserve evidence

**After-Hours Access:**
1. Receive alert (after-hours badge swipe)
2. Verify authorized (check after-hours access list or call employee to confirm)
3. If unauthorized: Challenge employee (in person or via phone), escalate to security manager

---

## 5. Monitoring Integration

### 5.1 SIEM Integration

**Physical Security Events to Forward:**
- Access control: All access denied events, forced door events, after-hours access (successful)
- Intrusion detection: All alarm events (motion sensor, door/window, glass break)
- CCTV: Camera offline events, video export events

**Integration Method:**
- Syslog forwarding (most common): Access control system and intrusion alarm panel send syslog to SIEM server
- API integration: Some systems provide REST API for event retrieval (poll every 5-15 minutes)

**Configuration:**
- Access control system: Configure syslog server IP (SIEM server), port 514 (UDP) or 6514 (TCP)
- SIEM: Create parser for physical security events (extract user, door, timestamp, result)

### 5.2 Physical Security Dashboard

**Dashboard Platform Options:**
- Building Management System (BMS): If available, integrate physical security into BMS dashboard
- SIEM dashboard: Create physical security dashboard in SIEM (Splunk, Elastic, Datadog)
- Standalone: Grafana + InfluxDB (time-series database for metrics)

**Dashboard Metrics (see POL-S2, Section 7.3):**
- Access events today (count, trend chart)
- Failed access attempts (count, top users with failures)
- After-hours access (count, list of users)
- Active visitors (count)
- Camera status (online/offline count)
- Alarm events today (count, trend chart)

**Update Frequency:** Real-time (dashboard refreshes every 30-60 seconds)

---

## 6. Common Issues and Troubleshooting

### 6.1 Access Control Issues

**Issue: Badge not working (access denied)**
- Check: Is badge activated in system? Is user assigned correct access level? Is door configured correctly?
- Resolution: Verify badge number matches system, verify user has access to this door, verify door online

**Issue: Door not unlocking after badge swipe**
- Check: Is door strike/lock powered? Is strike/lock functioning? Is network connection to panel working?
- Resolution: Verify power to strike/lock (multimeter), test strike/lock manually (apply power directly), verify panel network connectivity

**Issue: Anti-passback violations (user cannot enter)**
- Check: Did user enter without exiting (forgot to badge out)?
- Resolution: Clear anti-passback violation in system (administrative override), remind user to badge in AND out

### 6.2 CCTV Issues

**Issue: Camera offline (no video)**
- Check: Is camera powered (PoE)? Is network cable connected? Is camera IP address correct?
- Resolution: Verify PoE switch port active (LED on switch), verify cable not damaged, ping camera IP address, reboot camera (power cycle PoE port)

**Issue: Poor nighttime image quality**
- Check: Is IR enabled? Is IR illuminator functioning? Is lens dirty?
- Resolution: Enable IR in camera settings, verify IR LEDs glowing (visible on other camera or phone camera), clean lens

**Issue: NVR storage full (not recording)**
- Check: Is retention setting too long for available storage? Is circular recording enabled?
- Resolution: Reduce retention (90 days → 60 days) or add storage capacity (install additional hard drives), verify circular recording enabled (oldest footage overwritten)

### 6.3 Intrusion Detection Issues

**Issue: Frequent false alarms**
- Check: What is triggering alarms (motion sensor, door sensor)? What time do alarms occur?
- Resolution: Adjust motion sensor sensitivity (reduce if too sensitive), reposition sensor (avoid HVAC vents, sunlight), verify doors/windows close properly (adjust door/window alignment if needed)

**Issue: Alarm panel not communicating with monitoring center**
- Check: Is network connection working? Is cellular backup functioning (if dual-path)?
- Resolution: Verify Ethernet cable connected, ping monitoring center IP, test cellular module (disconnect Ethernet, verify cellular backup works)

**Issue: Keypad not responding**
- Check: Is keypad powered? Is keypad wiring intact?
- Resolution: Verify power at keypad (multimeter on keypad wires), check for damaged wiring, replace keypad if faulty

---

**END OF ISMS-IMP-A.7.4-5-11-S1**

---

*"Implementation is not just installing equipment. It's systematic deployment—proper planning, tested configuration, integrated monitoring, and troubleshooting procedures—ensuring physical security systems function reliably and deliver measurable security value."*
