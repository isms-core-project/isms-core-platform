# ISMS-IMP-A.7.4-5-11-S2: Environmental Protection Implementation

**Document Classification:** Internal - ISMS Implementation Guide  
**Version:** 1.0  
**Effective Date:** [To be defined]  
**Review Cycle:** Annual  
**Owner:** Facilities Manager  
**Approved By:** CISO

---

## Purpose

This implementation guide provides step-by-step procedures for deploying and operating environmental protection systems to meet Control A.7.5 requirements (see POL-S3).

**Scope:** Fire detection/suppression, water damage protection, temperature/humidity monitoring, structural protection.

**Target Audience:** Facilities Management, Fire/Life Safety Technicians, HVAC Technicians, System Integrators.

---

## Table of Contents

1. [Fire Detection System Deployment](#1-fire-detection-system-deployment)
2. [Fire Suppression System Deployment](#2-fire-suppression-system-deployment)
3. [Water Detection System Deployment](#3-water-detection-system-deployment)
4. [Temperature and Humidity Monitoring Deployment](#4-temperature-and-humidity-monitoring-deployment)
5. [Environmental Monitoring Integration](#5-environmental-monitoring-integration)
6. [Common Issues and Troubleshooting](#6-common-issues-and-troubleshooting)

---

## 1. Fire Detection System Deployment

### 1.1 Pre-Deployment Planning

**Step 1: Determine Coverage Requirements**
- 100% of facility area requires smoke/heat detection (see POL-S3, Section 3.1.1)
- Calculate detector count: Facility area (sq ft) ÷ Detector coverage (typically 500-1000 sq ft per detector per fire code)
- Example: 10,000 sq ft office = 10-20 smoke detectors

**Step 2: Select Fire Alarm System**
- **Addressable system** (preferred): Each detector has unique ID, panel identifies exactly which detector triggered alarm
  - Use for: Medium to large facilities (>20 detectors), facilities with complex layouts
  - Brands: Simplex, Notifier, Edwards, EST
- **Conventional system** (older technology): Detectors grouped by zone, panel identifies zone but not individual detector
  - Use for: Small facilities (<20 detectors), simple layouts, budget-constrained
  - Brands: Simplex, Honeywell Fire, Fire-Lite

**Step 3: Verify Local Fire Code Requirements**
- Contact local fire marshal or building department
- Obtain copy of applicable fire code (NFPA 72 in US, local amendments)
- Requirements vary: Detector spacing, alarm notification (horns/strobes), monitoring connection to fire department

### 1.2 Fire Alarm Panel Installation

**Panel Location:**
- Install near main entrance (fire department access)
- Install in secured area (not public access - prevent tampering)
- Typical location: Electrical room, security office, main corridor near entrance

**Power and Backup:**
- Primary power: Dedicated 120V circuit (not shared with other loads)
- Backup power: 24V battery (minimum 24-hour backup per fire code)
- Supervision: Panel monitors battery voltage, alerts if battery fails

**Network Connection:**
- Ethernet: Connect to network for remote monitoring (optional but recommended)
- Phone line or cellular: Connection to monitoring center (required if monitoring service used)

### 1.3 Smoke Detector Installation

**Detector Placement:**
- Ceiling-mounted (smoke rises - ceiling is optimal detection point)
- Spacing: Per fire code (typically 30-foot spacing for smooth ceilings, closer spacing for high ceilings or obstructions)
- Special locations:
  - **Server rooms:** Ceiling-level detectors PLUS under raised floor detectors PLUS in-rack detectors (optional, for very early detection)
  - **High ceilings (>10 feet):** Beam detectors or aspirating smoke detection (ASD) - more sensitive than standard detectors
  - **Return air plenums:** Detectors in air returns (detect smoke before it dilutes throughout room)

**Detector Types:**
- **Photoelectric:** General-purpose (most areas), best for smoldering fires
- **Ionization:** Fast-burning fires (less common in datacenters/offices)
- **Dual-sensor:** Both photoelectric and ionization (comprehensive coverage)
- **Aspirating (ASD):** Very early detection (datacenters), samples air continuously through network of pipes

**Wiring:**
- Addressable detectors: 4-wire (power +, power -, data +, data -)
- Conventional detectors: 2-wire (power + signal on same pair)
- Wire type: FPLR (fire alarm plenum-rated), typically 18 AWG or 16 AWG
- Conduit: Required in some jurisdictions, recommended for protection

### 1.4 Fire Alarm Notification Devices

**Audible Alarms (Horns/Bells):**
- Install throughout facility (minimum 75 dBA at all locations per ADA)
- Spacing: Per fire code (typically one horn per floor, additional horns if large floor)
- Mounting: Wall-mounted, 80-96 inches above floor

**Visual Alarms (Strobes):**
- Required for ADA compliance (hearing-impaired occupants)
- Install with horns (combination horn/strobe units) or separately
- Flash rate: 1-2 Hz (per ADA specifications)
- Intensity: Candela rating per room size (small rooms: 15 cd, large rooms: 75-177 cd)

### 1.5 Fire Alarm System Programming

**Step 1: Add Devices to Panel**
- Addressable: Auto-discover detectors (panel scans network, adds all connected devices) or manually assign addresses
- Program device types (smoke detector, heat detector, horn, strobe)
- Name devices (Building A - Room 101 Smoke Detector)

**Step 2: Create Alarm Zones**
- Zone 1: Floor 1, Zone 2: Floor 2, etc. (floor-based) OR
- Zone 1: Building A, Zone 2: Building B (building-based)
- Granular zones help first responders locate fire quickly

**Step 3: Configure Alarm Sequences**
- Alarm verification (optional): Detector triggers alarm twice within 60 seconds before activating notification devices (reduce false alarms)
- Pre-alarm (optional): Silent alarm to monitoring center first, full alarm if not reset within 2 minutes (allow investigation)
- Standard: Detector triggers alarm → Immediate notification devices activation → Monitoring center notified

**Step 4: Configure Monitoring Connection**
- If using monitoring center: Enter monitoring center phone number or IP address
- Test communication: Trigger alarm (press panel test button), verify monitoring center receives signal

### 1.6 Testing and Commissioning

**Detector Testing (Required Before Occupancy):**
- Smoke test: Use aerosol smoke tester (UL-listed product, simulates smoke), spray under detector, verify alarm triggers
- Test ALL detectors (100% coverage)
- Document: Detector address/location, test date, pass/fail

**Notification Device Testing:**
- Trigger alarm, verify all horns sound and strobes flash
- Measure sound level: Verify >75 dBA at all locations (use sound level meter)

**Communication Testing:**
- Trigger alarm, call monitoring center, verify they received alarm signal
- Document: Monitoring center name, signal received time, phone call confirmation

**Fire Department Inspection:**
- Required: Most jurisdictions require fire department inspection and approval before occupancy
- Schedule: Contact fire marshal, schedule inspection after installation complete
- Inspection: Fire marshal tests random detectors, verifies panel configuration, approves system

---

## 2. Fire Suppression System Deployment

### 2.1 Sprinkler System Deployment

**Sprinkler System Design (Requires Licensed Professional):**
- Fire sprinkler design is specialized: MUST be designed by licensed fire protection engineer
- Do NOT attempt DIY sprinkler design (life safety system, strict code requirements)

**Sprinkler Type Selection:**
- **Wet pipe** (standard offices): Water in pipes at all times, simplest and most reliable
- **Dry pipe** (unheated areas): Air/nitrogen in pipes, water releases when sprinkler head activates, prevents freezing
- **Pre-action** (datacenters): Pipes empty until fire detected, two-stage activation (reduces accidental discharge risk)

**Sprinkler Head Spacing:**
- Coverage: Typically 130-200 sq ft per head (depending on head type, hazard classification)
- Placement: Grid pattern on ceiling, avoid obstructions (walls, ductwork, light fixtures)
- Distance from walls: Minimum 4 inches, maximum 6 feet (per NFPA 13)

**Installation (Requires Licensed Contractor):**
- Fire sprinkler installation requires licensed sprinkler contractor (certification required)
- Pipe sizing, hydraulic calculations, pressure testing all per NFPA 13 standards
- Inspection: Fire marshal inspects and approves sprinkler system before occupancy

### 2.2 Gas Suppression System Deployment (Datacenters)

**When to Use Gas Suppression:**
- Datacenters, server rooms, telecommunications equipment rooms (water damage from sprinklers unacceptable)
- Archive/records storage (water damage to documents)
- High-value equipment areas

**Gas Suppression System Design (Requires Licensed Professional):**
- Design by licensed fire protection engineer (specialized system)
- Agent selection: FM-200 (most common), Novec 1230 (environmentally friendly), Inergen (inert gas)

**Pre-Discharge Alarm Sequence:**
1. Fire detected (smoke detector or heat detector)
2. Pre-discharge alarm activates (loud horn, flashing lights)
3. Pre-discharge delay: 30-60 seconds (allow personnel evacuation and manual abort if false alarm)
4. Gas discharge: Agent floods room (suppress fire within 10 seconds)

**Manual Abort Station:**
- Install abort button outside protected area (near entrance)
- Purpose: Allow manual abort if fire alarm is false (prevent unnecessary gas discharge)
- Training: Train personnel on when to abort (only if absolutely certain no fire)

**Installation Requirements:**
- Room sealing: Gas suppression requires room to be sealed (gaps around doors, cable penetrations sealed)
- Ventilation interlocks: HVAC shuts down during discharge (prevent agent venting out)
- Pressure relief vents: Prevent room over-pressurization during discharge (walls/ceiling could blow out otherwise)

**Nozzle Placement:**
- Calculate nozzle count based on room volume, agent type
- Mount on ceiling or high on walls (agent disperses evenly from nozzles)

**Testing (Requires Certified Technician):**
- Discharge test: Typically NOT performed (expensive to refill agent)
- Functional test: Verify detection system triggers pre-discharge alarm, verify abort button functions, verify all interlocks (HVAC shutdown)

### 2.3 Fire Extinguisher Deployment

**Fire Extinguisher Placement (Simple, DIY-Friendly):**
- Spacing: One extinguisher per 75 feet of travel distance (per NFPA 10)
- Locations: Near exits, hallways, kitchens, electrical rooms, server rooms
- Mounting: Wall-mounted bracket, 3-5 feet above floor (top of extinguisher)

**Fire Extinguisher Types:**
- **ABC (multi-purpose):** Most common, suitable for offices, general areas (wood, paper, electrical, flammable liquids)
- **CO2:** Electrical rooms (no residue, safe for electronics)
- **Class K:** Kitchen (cooking oils/grease)

**Fire Extinguisher Sizing:**
- Offices: Minimum 2.5 kg (5 lb) ABC, 5 kg (10 lb) recommended
- Server rooms: 5 kg (10 lb) ABC or 5 kg CO2
- Kitchens: 6 kg Class K

**Inspection (Monthly - Easy):**
- Visual check: Pressure gauge in green zone, no physical damage, access unobstructed
- Tag: Record inspection date on tag attached to extinguisher

**Annual Professional Inspection (Required):**
- Certified fire extinguisher company inspects and services extinguisher (verify pressure, refill if needed)
- Company attaches annual inspection tag to extinguisher

---

## 3. Water Detection System Deployment

### 3.1 Pre-Deployment Planning

**Step 1: Identify At-Risk Areas**
- Mandatory: Server rooms (under raised floors, near HVAC units), telecom closets, below-grade facilities
- Optional: Storage areas, under plumbing, near water heaters

**Step 2: Select Water Detection System**
- **Standalone sensors** (simple): Individual battery-powered sensors with local alarms (Amazon, Home Depot brands)
  - Pros: Low cost ($20-50 per sensor), easy installation (no wiring)
  - Cons: No central monitoring (must be near sensor to hear alarm), battery replacement required
- **Wired system** (professional): Sensors wired to central panel with email/SMS alerts
  - Pros: Central monitoring, integration with BMS/SIEM
  - Cons: Higher cost ($500-2000 for system), requires wiring
  - Brands: Dorlen (LeakAlarm), Winland (FloodSentry), Honeywell (Water Leak Detection)

**Step 3: Select Sensor Type**
- **Spot sensors:** Single point detection (place under HVAC, near sump pump)
- **Cable sensors:** Continuous detection along cable length (run along walls, under raised floors)

### 3.2 Sensor Installation

**Spot Sensor Placement:**
- Floor level (water accumulates at low point)
- Under HVAC units (condensate pan overflow)
- Near sump pumps (detect pump failure)
- Below water heaters
- Near floor drains (detect drain backup)

**Cable Sensor Installation:**
- Run cable in grid pattern under raised floors (1-2 meter spacing)
- Run cable along walls (baseboard level) in below-grade facilities
- Cable attachment: Cable clips or adhesive cable holders

**Wiring (for Wired Systems):**
- Sensors connect to control panel via 2-wire or 4-wire (depending on system)
- Wire type: 22 AWG 2-conductor (low voltage, no special fire rating required)
- Maximum wire length: Varies by system (typically 1000-2000 feet)

### 3.3 System Configuration

**Add Sensors to Control Panel:**
- Auto-discover (if IP-based sensors) or manually configure zone numbers

**Configure Alerts:**
- Email: Enter email addresses (facilities manager, IT operations)
- SMS: Enter phone numbers for text alerts
- Phone call: Some systems support automated phone call alerts (expensive but effective for critical facilities)

**Name Sensors:**
- Example: "Server Room 1 - Under Raised Floor", "HVAC Unit 3 - Condensate Pan"

### 3.4 Testing

**Monthly Testing (Required per POL-S3):**
- Pour small amount of water on sensor (or wet cable sensor)
- Verify alarm triggers (local alarm sounds, alert sent to monitoring panel, email/SMS sent)
- Wipe sensor dry, verify alarm clears

**Document Test:**
- Sensor ID, test date, pass/fail

---

## 4. Temperature and Humidity Monitoring Deployment

### 4.1 Pre-Deployment Planning

**Step 1: Determine Sensor Locations**
- Mandatory: All server rooms, datacenters, telecom closets (100% coverage per POL-S3)
- Sensor placement: Intake (cold aisle), exhaust (hot aisle), return air (to HVAC)
- Sensor count: Small server room (1-2 sensors), large datacenter (1 sensor per 50-100 sq meters)

**Step 2: Select Monitoring Platform**
- **IoT sensors + cloud platform** (modern, recommended):
  - Sensors: Ubiquiti UniFi Environmental Sensor ($99), Monnit sensors ($50-150), SensorPush ($50)
  - Platform: Manufacturer cloud platform (Ubiquiti UniFi Controller, Monnit iMonnit, SensorPush app)
  - Pros: Easy installation (wireless), low cost, cloud-based (accessible anywhere)
  - Cons: Subscription cost (some platforms), Internet-dependent
- **BMS integration** (enterprise):
  - Sensors: BMS-compatible sensors (Honeywell, Siemens, Johnson Controls)
  - Platform: Building Management System (if facility already has BMS)
  - Pros: Professional-grade, integrated with HVAC controls
  - Cons: Expensive ($$$), requires BMS infrastructure

**Step 3: Determine Alert Thresholds**
- Temperature: Warning at 28°C / 82°F (high) or 16°C / 61°F (low), Critical at 30°C / 86°F (high) or 15°C / 59°F (low)
- Humidity: Warning at 25% RH (dry) or 70% RH (humid), Critical at 20% RH (dry) or 80% RH (humid)
- Rate-of-change: Alert if temperature rises >2°C per 10 minutes (indicates HVAC failure)

### 4.2 Sensor Installation

**IoT Sensor Installation (Wireless):**
- Mount sensor on wall or equipment rack (screw mount or adhesive mount)
- Mounting height: Equipment intake level (NOT ceiling level - want temperature where equipment breathes)
- Power: Battery-powered (replace batteries annually) or PoE-powered (if sensor supports PoE)

**BMS Sensor Installation (Wired):**
- Mount sensor per above (wall or rack mount)
- Wiring: Typically 2-wire or 4-wire to BMS controller (varies by BMS brand)
- Wire type: 18 AWG shielded pair (shield reduces electrical interference)

### 4.3 Platform Configuration

**Add Sensors to Platform:**
- IoT sensors: Typically auto-discover via Bluetooth or Wi-Fi (scan for sensors, add to platform)
- BMS sensors: Manually configure in BMS (assign sensor address, name, calibration)

**Configure Alert Thresholds:**
- Set thresholds per Step 4.1.3 above
- Set alert recipients: Email (facilities manager, IT operations), SMS (critical alerts only - avoid SMS fatigue)

**Configure Data Retention:**
- Raw data: 12 months minimum (5-minute intervals)
- Aggregated data: 3 years (hourly averages)

**Dashboard Configuration:**
- Create dashboard: Real-time temperature/humidity display, trend charts (past 24 hours, past 7 days)
- Public display (optional): Large screen in Network Operations Center or facilities office (real-time monitoring)

### 4.4 Testing and Validation

**Sensor Accuracy Verification:**
- Use calibrated handheld thermometer/hygrometer (buy from Fluke, Extech, or similar - $50-200)
- Place handheld device next to sensor, compare readings
- Acceptable accuracy: ±0.5°C temperature, ±3% RH humidity
- If sensor outside accuracy range: Calibrate sensor (if calibration feature available) or replace sensor

**Alert Testing:**
- Manually trigger threshold (heat sensor with hair dryer or heat gun - carefully!)
- Verify alert sent (email, SMS)
- Verify alert contains: Sensor name, location, threshold exceeded, current reading

---

## 5. Environmental Monitoring Integration

### 5.1 Integration with Building Management System (BMS)

**If Facility Has BMS:**
- Fire alarm panel → BMS: Fire alarm status visible in BMS, HVAC shutdown on fire alarm (prevent smoke spread)
- Environmental sensors → BMS: Temperature/humidity data in BMS, HVAC auto-adjust based on temperature
- Water detection → BMS: Water alarm visible in BMS

**Integration Method:**
- BACnet protocol (most common for BMS integration): Fire alarm panels and sensors communicate with BMS via BACnet/IP
- Modbus protocol (alternative): Some older systems use Modbus RTU or Modbus TCP

### 5.2 Integration with Physical Security Dashboard

**Forward Environmental Events to Security Dashboard:**
- Fire alarms → Dashboard (critical alert, visible to Security Operations Center)
- Water detection alarms → Dashboard (warning alert)
- Temperature critical alerts → Dashboard (critical alert)

**Integration Method:**
- SIEM integration: Forward environmental events to SIEM via syslog (see IMP-S1, Section 5.1)
- API integration: Poll environmental monitoring platform API every 5-15 minutes (retrieve current temperature, alerts)

**Dashboard Metrics (see POL-S2, Section 7.3):**
- Current temperature/humidity (all server rooms)
- Temperature excursions this month (count)
- Fire alarms this month (count)
- Water detection alarms this month (count)

---

## 6. Common Issues and Troubleshooting

### 6.1 Fire Alarm Issues

**Issue: Frequent false alarms (smoke detectors)**
- Causes: Dust accumulation, cooking smoke, steam, aging detectors
- Resolution:
  - Clean detectors (compressed air or vacuum, per manufacturer instructions)
  - Relocate detector (away from kitchen, bathroom)
  - Replace aging detectors (>10 years old - replace even if functional)

**Issue: Low battery alarm (fire alarm panel)**
- Cause: Backup battery depleted or failed
- Resolution: Replace backup battery (typically 12V 7Ah battery, purchase from fire alarm supplier)

**Issue: Communication failure (monitoring center not receiving alarms)**
- Causes: Phone line disconnected, network cable unplugged, monitoring center phone number incorrect
- Resolution: Verify phone line/network cable connected, test communication (press panel test button), verify monitoring center phone number in panel configuration

### 6.2 Water Detection Issues

**Issue: Sensor triggering false alarms**
- Causes: Condensation on sensor (high humidity), wet floor (cleaning, spill)
- Resolution: Verify no actual water leak (check HVAC, plumbing), wipe sensor dry, monitor for recurrence (if recurring, relocate sensor or adjust humidity control)

**Issue: Sensor not detecting water**
- Causes: Battery dead (battery-powered sensor), sensor failed, sensor not placed in water path
- Resolution: Replace battery (battery-powered sensors), test sensor (pour water on sensor, verify alarm), relocate sensor (ensure in low point where water will flow)

### 6.3 Temperature Monitoring Issues

**Issue: Temperature reading inaccurate**
- Causes: Sensor not calibrated, sensor placed in bad location (near heat source, in airflow obstruction)
- Resolution: Verify with handheld thermometer (calibrate sensor if drift >0.5°C), relocate sensor (away from heat sources, in representative location)

**Issue: Temperature alerts not being sent**
- Causes: Email/SMS configuration incorrect, Internet connection down (cloud platform), threshold not configured
- Resolution: Verify email addresses/phone numbers correct in platform, verify Internet connectivity, verify thresholds configured

**Issue: Sensor offline (no data)**
- Causes: Battery dead (wireless sensor), network connection lost (wired sensor, cloud platform)
- Resolution: Replace battery (wireless), verify network cable connected (wired), verify Wi-Fi connectivity (wireless cloud sensors)

---

**END OF ISMS-IMP-A.7.4-5-11-S2**

---

*"Environmental protection deployment is not just installing fire alarms and thermometers. It's systematic planning—coverage requirements, code compliance, integration with monitoring platforms, and regular testing—ensuring facilities are protected from fire, water, and temperature threats."*
