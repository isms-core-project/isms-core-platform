# ISMS-IMP-A.7.4-5-11-S3: Utility Resilience Implementation

**Document Classification:** Internal - ISMS Implementation Guide  
**Version:** 1.0  
**Effective Date:** [To be defined]  
**Review Cycle:** Annual  
**Owner:** Facilities Manager / IT Operations  
**Approved By:** CISO

---

## Purpose

This implementation guide provides step-by-step procedures for deploying and operating utility resilience infrastructure to meet Control A.7.11 requirements (see POL-S4).

**Scope:** UPS systems, backup generators, HVAC infrastructure, ISP redundancy, utility monitoring.

**Target Audience:** Facilities Management, Electricians, HVAC Technicians, IT Operations, Network Engineers.

---

## Table of Contents

1. [UPS System Deployment](#1-ups-system-deployment)
2. [Backup Generator Deployment](#2-backup-generator-deployment)
3. [HVAC Infrastructure Deployment](#3-hvac-infrastructure-deployment)
4. [ISP Redundancy Deployment](#4-isp-redundancy-deployment)
5. [Utility Monitoring Deployment](#5-utility-monitoring-deployment)
6. [Common Issues and Troubleshooting](#6-common-issues-and-troubleshooting)

---

## 1. UPS System Deployment

### 1.1 UPS Sizing and Selection

**Step 1: Calculate Protected Load (see POL-S4, Section 2.2.2)**
```
1. List all equipment to be UPS-protected (servers, network equipment, storage)
2. Sum nameplate power ratings (or measure actual consumption with power meter)
3. Add 20% growth margin
4. Convert to VA: Watts ÷ Power Factor (typically 0.8-0.9 for IT equipment)
5. Select next standard UPS size

Example:
- Protected load: 5,800W
- Growth margin: 5,800W × 1.2 = 6,960W
- VA rating: 6,960W ÷ 0.8 PF = 8,700 VA
- Selected UPS: 10 kVA (next standard size)
```

**Step 2: Determine Runtime Requirement**
- Critical facilities: 15+ minutes at full load (allow generator startup)
- Standard facilities: 5+ minutes at full load (allow graceful shutdown)
- Calculate: Runtime = Battery Capacity (Wh) ÷ Load (W)

**Step 3: Select UPS Type**
- **Critical facilities:** Online double-conversion UPS (APC Smart-UPS, Eaton 9PX, Schneider Galaxy)
- **Standard facilities:** Line-interactive UPS (APC Back-UPS Pro, CyberPower)

**Step 4: Select Redundancy Level**
- Critical facilities: N+1 minimum (multiple UPS in parallel, can lose one UPS)
- Standard facilities: N configuration (single UPS)

### 1.2 UPS Installation (Requires Licensed Electrician)

**DANGER: UPS installation involves high voltage electricity. Licensed electrician required.**

**Power Distribution:**
```
Utility Power → UPS Input → UPS (Battery + Inverter) → UPS Output → Protected Load
```

**Installation Steps:**
1. **Position UPS:** Place UPS in equipment room near protected load (minimize cable length)
   - Clearance: 24 inches front (service access), 6 inches sides (airflow)
   - Floor loading: Verify floor can support UPS weight (100-500+ lbs depending on size)

2. **Install Input Circuit Breaker:**
   - Size per UPS specifications (typically 20-30A for 10 kVA UPS)
   - Install dedicated circuit breaker in electrical panel
   - Wire: 10 AWG or 12 AWG (depending on amperage, per NEC)

3. **Connect UPS Input:**
   - Licensed electrician connects UPS input to circuit breaker
   - Verify voltage: Use multimeter, verify 120V (US single-phase) or 208V/240V (US three-phase)

4. **Install Output Distribution (PDUs):**
   - PDU (Power Distribution Unit): Rack-mounted power strip with multiple outlets
   - Install PDUs in equipment racks (vertical PDU on rack side rails preferred)
   - Connect PDU input to UPS output (hardwired or plug into UPS output receptacle)

5. **Connect Protected Equipment:**
   - Connect servers, network equipment to PDU outlets
   - DO NOT overload UPS (verify total load < UPS capacity)

6. **Network Connection:**
   - Connect UPS network port to network switch (for SNMP monitoring)
   - Assign static IP address to UPS (or DHCP reservation)

### 1.3 UPS Configuration

**Step 1: Initial Configuration (via UPS Display Panel or Web Interface)**
- Set UPS name (Building A UPS 1)
- Set IP address (static recommended: 192.168.x.x)
- Set date/time

**Step 2: Configure Battery Settings**
- Battery type: Verify correct (VRLA or Lithium-Ion)
- Battery install date: Enter date (UPS tracks battery age)
- Battery replacement date: Enter date (UPS alerts when replacement due)

**Step 3: Configure Alarms**
- Enable all alarms: On battery, battery low, overload, UPS failure
- Set alarm thresholds: Battery low (5 minutes runtime remaining)

**Step 4: Configure SNMP Monitoring**
- SNMP community string: Set read-only community string (e.g., "public" or custom string)
- SNMP trap recipients: Enter monitoring server IP addresses (for alerts)

**Step 5: Configure Shutdown Agents (Optional)**
- For servers with UPS management software installed (APC PowerChute, Eaton Intelligent Power Manager):
  - Install software on servers
  - Configure shutdown sequence: When UPS battery <5 min runtime, initiate graceful server shutdown

### 1.4 UPS Testing

**Initial Testing (Before Production Use):**
- **Overload test:** Disconnect utility power, verify UPS transfers to battery, load servers, verify UPS can support load
- **Runtime test:** Run on battery until 50% discharge, measure runtime, verify meets requirement
- **Battery recharge:** After runtime test, reconnect utility, verify battery recharges to 100% within manufacturer-specified time (typically 4-8 hours)

**Monthly Testing (Per POL-S4, Section 2.2.6):**
- Battery self-test (automated): UPS performs 10-30 second discharge test, verify no alarms

**Quarterly Testing:**
- Runtime verification: Disconnect utility, run on battery to 50% discharge, measure runtime

---

## 2. Backup Generator Deployment

### 2.1 Generator Sizing and Selection

**Step 1: Calculate Critical Load (see POL-S4, Section 2.3.1)**
```
1. Calculate UPS-protected load (from UPS sizing above)
2. Add HVAC load (compressor + fans, typically 2-5 kW for small HVAC units)
3. Add lighting load (estimate 10-20W per sq meter × facility area)
4. Add safety factor (1.3-1.5× for motor starting inrush)
5. Select next standard generator size

Example:
- UPS load: 10 kW
- HVAC: 5 kW
- Lighting: 1 kW
- Subtotal: 16 kW
- Safety factor: 16 kW × 1.3 = 20.8 kW
- Selected generator: 25 kW (next standard size)
```

**Step 2: Determine Runtime Requirement**
- Critical facilities: 24+ hours at full load (48-72 hours recommended)
- Fuel tank sizing: 24-48 hours runtime (see POL-S4, Section 2.3.1 for fuel calculation)

**Step 3: Select Generator Type**
- **Diesel:** Most common for datacenters/critical facilities (reliable, efficient, long shelf life)
- **Natural gas:** Lower maintenance (no fuel storage), but vulnerable to same utility outage as electric
- **Propane:** Alternative to diesel (longer shelf life than diesel), requires propane tank

**Step 4: Select Generator Location**
- Outdoor (most common): Install on concrete pad adjacent to building
  - Setback requirements: Per local code (typically 5-10 feet from building, property line)
  - Noise: Consider noise impact on neighbors (acoustic enclosures available)
- Indoor (rare, special applications): Install in dedicated generator room
  - Ventilation: Requires substantial ventilation (exhaust gases, cooling air)
  - Fuel: Indoor diesel storage restricted by code (natural gas preferred for indoor)

### 2.2 Generator and ATS Installation (Requires Licensed Contractor)

**DANGER: Generator installation involves high voltage electricity and fuel systems. Licensed contractor required.**

**Installation Overview:**
```
Utility Power → Automatic Transfer Switch (ATS) → Protected Load
                    ↑
                Generator
```

**Installation Steps (Performed by Contractor):**

1. **Prepare Generator Pad:**
   - Pour concrete pad (typically 6-8 inches thick, reinforced)
   - Size: Generator footprint + 12 inches on all sides
   - Level: Must be level (use level during concrete pour)

2. **Install Generator:**
   - Crane or forklift places generator on pad
   - Bolt generator to pad (anchor bolts, vibration isolators optional)

3. **Install Fuel Tank:**
   - Above-ground tank: Place on separate concrete pad adjacent to generator (or skid-mounted tank integrated with generator)
   - Below-ground tank: Excavate, install tank per code (requires permits, inspections)
   - Fuel line: Connect tank to generator (typically 3/4" or 1" steel pipe)

4. **Install Automatic Transfer Switch (ATS):**
   - ATS location: Near electrical panel (indoor, dry location)
   - ATS wiring:
     - Utility input: Connect to main electrical panel
     - Generator input: Connect to generator output
     - Load output: Connect to protected loads (UPS, HVAC, critical lighting)

5. **Generator Output Wiring:**
   - Wire from generator to ATS input (large gauge wire, typically 6 AWG to 2/0 AWG depending on generator size)
   - Conduit: Run in conduit (underground or exterior wall-mounted)

6. **Start Battery:**
   - Generator has starting battery (12V automotive-style battery)
   - Connect and charge battery (generator cannot start without battery)

### 2.3 Generator Configuration

**Step 1: Initial Setup (via Generator Control Panel)**
- Set language, date/time
- Set exercise schedule: Weekly auto-start (e.g., every Monday at 10 AM, 15-minute no-load run)
- Set ATS auto-start: Enable (generator auto-starts on utility power loss)

**Step 2: Configure Alarms**
- Low oil pressure, high coolant temperature, overcrank (fails to start), low fuel

**Step 3: Connect Remote Monitoring (Optional)**
- Some generators support cellular or Ethernet remote monitoring
- Install monitoring module, configure alerts (email/SMS on generator alarms)

### 2.4 ATS Configuration

**Failover Settings:**
- Utility loss detection: ATS monitors utility voltage and frequency, triggers generator start if out of tolerance
- Transfer delay: 5-15 seconds (wait for generator to stabilize before transferring load)

**Failback Settings:**
- Utility restore detection: ATS monitors utility for 5-15 minutes (ensure stable) before transferring back
- Cool-down delay: Generator runs 5-10 minutes after transfer back to utility (cool down before shutdown)

### 2.5 Generator Testing

**Weekly Auto-Exercise (Per POL-S4, Section 2.3.3):**
- Generator automatically starts, runs 15-30 minutes (no load or minimal load), shuts down
- Verify: No alarms, oil pressure normal, coolant temperature normal

**Monthly Manual Test (No-Load):**
- Manually start generator (push start button)
- Run 15-30 minutes, monitor gauges (voltage, frequency, oil pressure, temperature)
- Shut down, document (date, runtime, any issues)

**Quarterly Load Test (50% Load):**
- Transfer load to generator via ATS (or manual transfer)
- Run under 50% load for 1-2 hours
- Monitor: Voltage, frequency, load %, fuel consumption
- Transfer back to utility, cool down, shut down

**Annual Load Test (100% Load):**
- Transfer load to generator, add load bank if facility load <80% generator capacity
- Run under 100% load for 4+ hours
- Monitor: Voltage, frequency, fuel consumption, temperature
- Verify: No alarms, stable operation at full load

---

## 3. HVAC Infrastructure Deployment

### 3.1 HVAC Sizing (Requires HVAC Professional)

**HVAC sizing is complex: Engage licensed HVAC contractor for datacenter/server room cooling.**

**Simplified Sizing (For Planning Only, see POL-S4, Section 3.1.1):**
```
Heat Load (BTU/hr) = IT Equipment Power (Watts) × 3.41 BTU/Watt × Overhead Factor

Example:
- IT equipment: 10 kW (10,000 W)
- Heat load: 10,000 W × 3.41 = 34,100 BTU/hr
- Overhead factor: 1.3 (well-insulated datacenter)
- Total cooling: 34,100 × 1.3 = 44,330 BTU/hr (3.7 tons)
- Selected HVAC: 4-ton unit (48,000 BTU/hr)
```

**Redundancy Selection:**
- Critical facilities: N+1 (example: 2× 3-ton units for 4-ton requirement)
- Standard facilities: N (single unit sized for load)

### 3.2 HVAC Installation (Requires Licensed Contractor)

**Installation Overview:**
- **Air-cooled precision HVAC** (most common for server rooms): Self-contained unit, air-cooled condenser, floor-mounted or ceiling-mounted
- **Split system** (standard offices): Outdoor condenser + indoor air handler
- **Chilled water** (large datacenters only): Chiller plant + air handlers

**Installation Steps (Performed by Contractor):**

1. **Position HVAC Unit:**
   - Floor-mounted: Place on equipment room floor (front of racks for cold aisle supply, back for hot aisle return)
   - Clearance: 24-36 inches front/back for service access

2. **Electrical Connection:**
   - Power requirements: Typically 208V or 240V three-phase (varies by unit size)
   - Licensed electrician installs dedicated circuit, connects HVAC unit

3. **Refrigerant Lines (Split Systems):**
   - Connect outdoor condenser to indoor air handler via refrigerant lines (copper tubing)
   - Insulate refrigerant lines (prevent condensation)

4. **Condensate Drain:**
   - Connect condensate drain (PVC pipe from HVAC unit to floor drain or sump)
   - Install condensate pan with overflow sensor (alert on clogged drain)

5. **Startup and Commissioning:**
   - Contractor starts HVAC, verifies cooling capacity
   - Checks refrigerant charge, airflow, electrical parameters

### 3.3 HVAC Configuration

**Set Temperature and Humidity:**
- Target temperature: 20-22°C (68-72°F) for server rooms (see POL-S3, Section 5.1.1)
- Target humidity: 50% RH (range 40-60% RH)

**Configure Alarms (If HVAC Unit Has Built-In Monitoring):**
- High temperature alarm: Alert if room temperature >28°C
- Low temperature alarm: Alert if room temperature <16°C
- Unit failure alarm: Alert if compressor failure, fan failure, low refrigerant

**Connect to Building Management System (If Available):**
- BMS can monitor HVAC status, control temperature setpoint, receive alarms
- Integration via BACnet or Modbus (see IMP-S2, Section 5.1)

---

## 4. ISP Redundancy Deployment

### 4.1 ISP Selection and Procurement

**Step 1: Identify ISP Bandwidth Requirements**
- Calculate current usage (average Mbps, peak Mbps)
- Add 50% growth margin
- Example: Current usage 50 Mbps peak → Provision 75-100 Mbps

**Step 2: Select Primary and Secondary ISPs (Critical Facilities)**
- **Diverse carriers:** Different companies (Comcast + Verizon, AT&T + Lumen)
- **Avoid:** Two circuits from same carrier (carrier outage affects both)

**Step 3: Request Diversity from ISPs**
- Ask ISPs to provide route diversity documentation (prove circuits enter building from different sides, route through different central offices)
- Diverse entry points: Primary circuit from north side of building, secondary from south side (different conduits, risers)

**Step 4: Procurement**
- Request quotes from multiple ISPs (2-3 ISPs for each circuit)
- Negotiate SLA (99.9% uptime minimum, MTTR <4 hours)
- Sign contracts (typically 1-3 year terms)

### 4.2 ISP Installation (Performed by ISP)

**Installation Overview:**
```
ISP 1 → Router Port 1 (Primary)
ISP 2 → Router Port 2 (Secondary)
```

**Installation Process:**
1. **ISP Schedules Installation:** Typically 30-90 days lead time (varies by ISP and location)
2. **ISP Installs Circuit:**
   - Fiber or copper cable from ISP network to building (ISP runs cable to demarcation point)
   - Demarcation equipment (ISP installs ONT for fiber, NID for copper)
3. **Customer Premise Equipment:**
   - Router: Customer provides router (or rents from ISP - customer-provided recommended for flexibility)
   - Router placement: Install in network equipment room (near servers/switches)
   - Connect: Ethernet cable from ISP demarcation equipment to router WAN port

### 4.3 Router Configuration for ISP Failover

**Dual ISP Configuration Options:**

**Option 1: Manual Failover (Simple, No BGP)**
- Primary ISP active, secondary ISP standby (not actively used)
- Configuration:
  - Router default route points to Primary ISP gateway
  - If Primary ISP down: Manually change default route to Secondary ISP gateway (15-minute manual procedure)
- Pros: Simple configuration, no BGP required
- Cons: Manual failover (downtime during failover)

**Option 2: BGP Automatic Failover (Advanced, Recommended for Critical Facilities)**
- Both ISPs active, automatic failover via BGP routing
- Requirements:
  - Organization must obtain AS (Autonomous System) number from regional registry (ARIN in North America)
  - Organization must have provider-independent IP address space
  - Router must support BGP (enterprise routers: Cisco, Juniper, Arista)
- Configuration (Requires Network Engineer):
  - Configure BGP peering with both ISPs
  - Advertise organization's IP prefixes via both ISPs
  - BGP automatically reroutes traffic to secondary ISP if primary ISP fails (1-5 minute failover)
- Pros: Automatic failover, seamless to end users
- Cons: Complex configuration, requires AS number and IP space

**Configuration Steps (Manual Failover - Simple):**

**Router Configuration (Example: pfSense Firewall/Router):**
1. **Configure WAN Interfaces:**
   - WAN1 (Primary ISP): Assign IP address from ISP (DHCP or static)
   - WAN2 (Secondary ISP): Assign IP address from ISP (DHCP or static)

2. **Configure Gateway:**
   - Gateway 1 (Primary): ISP1 gateway IP address, set as default gateway
   - Gateway 2 (Secondary): ISP2 gateway IP address

3. **Configure Gateway Monitoring:**
   - Monitor Primary ISP gateway (ping test every 30 seconds)
   - If Primary ISP unreachable for 3 consecutive pings (90 seconds), alert administrator

4. **Manual Failover Procedure (Documented):**
   - If Primary ISP down (detected by monitoring or outage notification from ISP):
     - Log in to router web interface
     - Change default gateway from Gateway 1 to Gateway 2
     - Save configuration
     - Verify connectivity (ping external sites)
   - When Primary ISP restored:
     - Change default gateway back to Gateway 1
     - Save configuration

**Configuration Steps (BGP Automatic Failover - Advanced, Requires Network Engineer):**
- Not covered in this guide (requires specialized BGP knowledge, engage network consultant if implementing)

### 4.4 ISP Failover Testing

**Quarterly Failover Test (Per POL-S4, Section 4.4):**

**Manual Failover Test Procedure:**
1. **Schedule Test:** Low-usage period (early morning, weekend), notify users (brief connectivity interruption possible)
2. **Disable Primary ISP:** Shutdown router WAN1 interface (or unplug Primary ISP circuit)
3. **Perform Manual Failover:** Change default gateway to Gateway 2 (Secondary ISP)
4. **Test Connectivity:** Ping external sites (8.8.8.8, organization website), access applications, VPN connectivity
5. **Measure Failover Time:** From Primary ISP down to Secondary ISP operational (target <15 minutes manual)
6. **Re-Enable Primary ISP:** Shutdown WAN2, change default gateway back to Gateway 1, bring up WAN1
7. **Verify Failback:** Ping external sites, verify traffic routing via Primary ISP
8. **Document:** Failover time, connectivity verification (pass/fail), issues

**BGP Automatic Failover Test Procedure:**
- Similar to above, but failover is automatic (no manual gateway change)
- Measure failover time (target <5 minutes automatic via BGP)

---

## 5. Utility Monitoring Deployment

### 5.1 Unified Monitoring Dashboard

**Monitoring Platform Selection (see POL-S4, Section 7.2):**
- **Building Management System (BMS):** If facility has BMS (Schneider, Siemens, Johnson Controls)
- **Network Monitoring System:** Nagios, Zabbix, PRTG, Datadog (can monitor UPS via SNMP, ISP via ping)
- **IoT Cloud Platform:** UPS manufacturer cloud platform (APC, Eaton) + environmental sensors
- **Hybrid:** Use multiple platforms, integrate into unified dashboard (Grafana)

**Dashboard Metrics (see POL-S4, Section 7.1):**
- Power: UPS status, battery health, generator status, fuel level
- HVAC: Unit status, temperature, humidity
- Telecommunications: ISP status, bandwidth utilization, latency

### 5.2 UPS Monitoring Configuration

**SNMP Monitoring (Most Common Method):**
- **Step 1:** Verify UPS SNMP enabled (see Section 1.3, Step 4)
- **Step 2:** Add UPS to monitoring system:
  - Nagios/Zabbix: Add UPS as host, assign UPS template (monitors standard UPS SNMP OIDs)
  - Datadog: Install agent on server, configure UPS integration (SNMP)
- **Step 3:** Verify metrics collected:
  - Input voltage, output voltage, load percentage, battery voltage, battery charge percentage, battery runtime remaining, UPS status (normal, on battery, bypass)
- **Step 4:** Configure alerts:
  - UPS on battery: Immediate email/SMS
  - Battery low (<5 min runtime): Critical alert
  - UPS overload (>90% capacity): Warning alert

**Cloud Monitoring (APC, Eaton):**
- APC: Install PowerChute Network Shutdown or use APC SmartConnect (cloud service)
- Eaton: Use Intelligent Power Manager or Eaton Brightlayer (cloud service)
- Configuration: Create account, register UPS (via serial number or network discovery), configure email/SMS alerts

### 5.3 Generator Monitoring Configuration

**Generator Monitoring (If Supported by Generator):**
- Some generators have Ethernet or cellular monitoring modules (optional add-on)
- Configuration: Install module, assign IP address (or configure cellular), add to monitoring platform via SNMP
- Metrics: Generator running/stopped, voltage, frequency, fuel level, alarms

**Manual Monitoring (If No Automated Monitoring):**
- Facilities staff manually checks generator weekly (during exercise test)
- Document: Generator status (ran successfully, any alarms), fuel level
- If generator alarm: Contact generator service company

### 5.4 ISP Monitoring Configuration

**Network Monitoring (Ping Test):**
- Configure monitoring system to ping ISP gateway every 30-60 seconds
- Metrics: ISP up/down, latency (round-trip time), packet loss
- Alert: ISP down (3 consecutive failed pings)

**SNMP Monitoring (Router Bandwidth):**
- Configure monitoring system to query router SNMP (interface statistics)
- Metrics: WAN interface bandwidth in/out (Mbps), utilization percentage
- Alert: Bandwidth >80% utilization (plan for bandwidth increase)

---

## 6. Common Issues and Troubleshooting

### 6.1 UPS Issues

**Issue: UPS frequently switching to battery (even though utility power seems OK)**
- Causes: Utility power quality poor (voltage sags, frequency deviations), UPS sensitivity too high
- Resolution: Check utility voltage with multimeter (should be 120V ±10%), check UPS sensitivity setting (some UPS have adjustable sensitivity - reduce if too sensitive), contact electrician if utility power quality persistently poor

**Issue: UPS runtime much shorter than expected**
- Causes: Batteries aged/degraded, load higher than expected, batteries not fully charged
- Resolution: Check battery health percentage (UPS display or SNMP), replace batteries if <80%, verify load not exceeding UPS capacity, allow 24+ hours for full battery recharge after deep discharge

**Issue: UPS alarms "battery replacement" or "battery service"**
- Cause: Batteries degraded (typically after 3-5 years for VRLA batteries)
- Resolution: Replace batteries (contact UPS vendor or purchase replacement battery pack), batteries are hot-swappable in most UPS (can replace without shutting down protected load)

### 6.2 Generator Issues

**Issue: Generator fails to start during utility outage**
- Causes: Starting battery dead, fuel empty, mechanical failure (engine seized)
- Resolution: Check starting battery voltage (should be >12V, jump-start if dead), check fuel level (refuel if empty), call generator service company if mechanical failure

**Issue: Generator starts but shuts down after 30 seconds**
- Causes: Low oil pressure (oil level low or oil pressure sensor failed), high coolant temperature (coolant leak)
- Resolution: Check oil level (dipstick - add oil if low), check coolant level (add coolant if low), call generator service if oil/coolant levels OK (sensor or mechanical failure)

**Issue: ATS not transferring load to generator (generator running but load still on utility)**
- Causes: ATS not receiving generator signal (wiring issue), ATS set to manual mode (not automatic)
- Resolution: Verify ATS in automatic mode (check ATS control panel), verify ATS sensing generator voltage (ATS should display generator voltage when generator running), call electrician if wiring issue

### 6.3 HVAC Issues

**Issue: HVAC running but room temperature rising**
- Causes: Insufficient HVAC capacity (IT load increased beyond HVAC capacity), refrigerant leak (cooling capacity degraded), airflow obstruction (dirty coils, clogged air filter)
- Resolution: Check IT load (compare to HVAC capacity - if load > capacity, reduce load or add HVAC capacity), check air filter (replace if dirty), call HVAC technician to check refrigerant charge and clean coils

**Issue: HVAC unit tripping circuit breaker**
- Causes: Electrical overload (compressor or fan motor failure causing high current draw), circuit breaker undersized
- Resolution: Reset circuit breaker (if trips again immediately, electrical fault - do not repeatedly reset), call electrician and HVAC technician (electrical fault or compressor failure)

### 6.4 ISP Issues

**Issue: ISP circuit down (no connectivity)**
- Causes: ISP network outage, ISP equipment failure (ONT, router), cable cut
- Resolution: Verify ISP equipment powered on (ONT, router), reboot ISP equipment (power cycle), contact ISP support (report outage), failover to secondary ISP if available

**Issue: Slow Internet speed (ISP circuit up but degraded performance)**
- Causes: ISP network congestion, router bandwidth limit misconfigured, DNS issues
- Resolution: Run speed test (speedtest.net - compare to ISP provisioned speed), verify router bandwidth configuration correct, try different DNS servers (Google 8.8.8.8, Cloudflare 1.1.1.1), contact ISP support if speed consistently below provisioned

---

**END OF ISMS-IMP-A.7.4-5-11-S3**

---

*"Utility resilience deployment is not just buying a UPS and generator. It's systematic infrastructure planning—proper sizing, redundancy configuration, automated failover, continuous monitoring, and regular testing—ensuring facilities remain operational during utility disruptions."*
