# ISMS-POL-A.7.4-5-11-S4: Utility Resilience (A.7.11)

**Document Classification:** Internal - ISMS Policy  
**Version:** 1.0  
**Effective Date:** [To be defined]  
**Review Cycle:** Annual  
**Policy Owner:** Facilities Manager / CISO  
**Approved By:** [Approval Authority]

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Facilities Manager / IT Operations / CISO | Initial policy for utility resilience requirements |

**Review Schedule:** Annual review or upon significant utility incidents, facility changes, or capacity updates  
**Next Review Date:** [Approval Date + 12 months]  
**Distribution:** CISO, Facilities Management, IT Operations, System Owners, Auditors

---

## Table of Contents

1. [Control Overview](#1-control-overview)
2. [Power Supply Resilience](#2-power-supply-resilience)
3. [HVAC and Cooling](#3-hvac-and-cooling)
4. [Telecommunications Infrastructure](#4-telecommunications-infrastructure)
5. [Water Supply (If Applicable)](#5-water-supply-if-applicable)
6. [Utility Failure Procedures](#6-utility-failure-procedures)
7. [Utility Monitoring](#7-utility-monitoring)
8. [Measurable Requirements and Audit Verification](#8-measurable-requirements-and-audit-verification)
9. [Cloud and Colocation Considerations](#9-cloud-and-colocation-considerations)
10. [Related Documents](#10-related-documents)

---

## 1. Control Overview

### 1.1 ISO 27001:2022 Control A.7.11 Reference

**Control Text:** Information processing facilities shall be protected from power failures and other disruptions caused by failures in supporting utilities.

**Purpose:** To ensure the continued availability of information processing facilities in the event of utility disruptions.

**Scope of This Section:**
This policy section defines comprehensive requirements for utility resilience in [Organization] facilities including:
- Power supply resilience (primary power, UPS, backup generators, redundancy levels)
- HVAC and cooling (capacity planning, redundancy, monitoring, failure response)
- Telecommunications infrastructure (ISP redundancy, diverse paths, failover mechanisms)
- Water supply (if applicable for cooling systems)
- Utility failure procedures (power loss, HVAC failure, telecommunications outage response)
- Utility monitoring (real-time status, alerting, performance dashboards)

### 1.2 Measurable Outcomes

Implementation of Control A.7.11 shall produce the following measurable outcomes:

**Power Uptime:**
- Power uptime: 99.99% minimum (critical facilities), 99.9% minimum (standard facilities)
- UPS runtime: Meets requirement (15 minutes critical, 5 minutes standard)
- Generator availability: 99% minimum (critical facilities with generators)

**HVAC Uptime:**
- HVAC uptime: 99.9% minimum (critical facilities), 99% minimum (standard facilities)
- Temperature excursions: <5 per month (outside target range, see POL-S3, Section 5)

**Telecommunications Uptime:**
- ISP uptime: Meets SLA (typically 99.9% per ISP)
- Failover success rate: 100% of quarterly failover tests successful

**Testing Compliance:**
- UPS battery testing: 100% compliance (monthly self-tests, quarterly load tests)
- Generator testing: 100% compliance (monthly no-load, quarterly load, annual full load)
- ISP failover testing: 100% compliance (quarterly tests)

**Incident Reports:**
- Utility failure events documented (power, HVAC, telecommunications)
- Response time documented
- Root cause analysis completed
- Corrective actions implemented

### 1.3 Facility Criticality and Control Requirements

Requirements vary by facility criticality tier (see POL-S1, Section 3.5):

**Tier 1 - Critical Facilities (Datacenters, Primary Server Rooms):**
- UPS: 15+ minutes runtime, N+1 redundancy
- Generator: 24+ hours runtime at full load, monthly testing
- HVAC: N+1 redundancy, continuous monitoring
- Telecommunications: Dual ISP (diverse carriers, diverse paths), automatic failover
- Utility monitoring: Real-time, 24/7 alerting

**Tier 2 - Standard Facilities (Offices, Branch Locations):**
- UPS: 5+ minutes runtime, N configuration (no redundancy required)
- Generator: Optional (risk-based decision)
- HVAC: N configuration (no redundancy required), threshold alerting
- Telecommunications: Single ISP with SLA
- Utility monitoring: Business hours or threshold alerting

---

## 2. Power Supply Resilience

### 2.1 Primary Power Source

#### 2.1.1 Utility Power Connection

[Organization] SHALL ensure adequate primary power supply:

**Power Capacity:**
- Capacity assessment: Calculate total facility load (IT equipment + HVAC + lighting + other)
- Growth margin: 20% minimum (accommodate future equipment additions)
- Verification: Annual load calculation review (update as equipment changes)

**Power Quality:**
- Voltage: Within utility standard (±10% of nominal, typically 120V ±12V or 208V/240V ±24V in US)
- Frequency: Within utility standard (±1% of nominal, 60 Hz ±0.6 Hz in US, 50 Hz ±0.5 Hz in EU)
- Power factor: >0.9 (minimize reactive power, reduce electrical costs)

**Redundant Utility Feeds (Critical Facilities - Optional but Recommended):**
- Dual utility feeds: Two separate utility service entrances (from different substations if available)
- Automatic transfer switch (ATS): Failover between utility feeds
- Benefits: Eliminates single point of failure (utility outage, maintenance)
- Cost: Significant (separate transformers, switchgear, ATS)

#### 2.1.2 Power Quality Monitoring

**Monitoring Requirements:**
- Voltage monitoring: Continuous (detect sags, surges, transients)
- Frequency monitoring: Continuous (detect deviations from 50/60 Hz)
- Power factor monitoring: Continuous (optimize power efficiency)

**Alert Thresholds:**
- Voltage: Alert if outside ±10% of nominal (sag or surge)
- Frequency: Alert if outside ±1% of nominal
- Power quality events: Log and alert on transients, harmonics

**Power Quality Issues:**
- Voltage sag (brownout): Can cause equipment malfunction (reboot, data loss)
- Voltage surge: Can damage equipment (power supplies, sensitive electronics)
- Frequency deviation: Indicates utility grid instability (potential outage)
- Transients: Brief voltage spikes (lightning, switching events)

**Mitigation:**
- UPS provides power conditioning (voltage regulation, frequency regulation, surge protection)
- Surge protectors for non-UPS-protected equipment

### 2.2 Uninterruptible Power Supply (UPS)

#### 2.2.1 UPS Requirements

**UPS Type:**
- **Critical Facilities (Tier 1):** Online double-conversion UPS (provides continuous power conditioning, zero transfer time)
- **Standard Facilities (Tier 2):** Line-interactive UPS minimum (provides voltage regulation, <5ms transfer time)

**Online Double-Conversion UPS:**
- Operation: AC → DC (rectifier) → DC → AC (inverter) - continuous operation
- Benefits: Perfect power conditioning (voltage regulation, frequency regulation, zero transfer time), galvanic isolation
- Use case: Datacenters, server rooms, critical equipment

**Line-Interactive UPS:**
- Operation: Normally bypass (utility power direct to load), transfer to battery during outage
- Benefits: Lower cost, higher efficiency (no conversion losses in normal operation)
- Use case: Office workstations, network equipment, non-critical servers
- Transfer time: <5ms (acceptable for most equipment)

#### 2.2.2 UPS Sizing

**Load Calculation:**
```
Step 1: Calculate Protected Load (Watts)
- Sum of all equipment to be protected
- IT equipment nameplate ratings (or measure actual consumption)
- Example: 10 servers × 500W + 2 switches × 100W + storage × 800W = 5,800W

Step 2: Add Growth Margin
- Add 20% for future equipment additions
- Example: 5,800W × 1.2 = 6,960W

Step 3: Calculate VA Rating
- VA = Watts / Power Factor (PF)
- Typical power factor: 0.8 - 0.9 for IT equipment
- Example: 6,960W / 0.8 = 8,700 VA (8.7 kVA)

Step 4: Select UPS Capacity
- Choose next standard UPS size: 10 kVA UPS (in this example)
```

**Runtime Calculation:**
```
Runtime = (Battery Capacity (Wh)) / (Load (W))

Battery Capacity (Wh) = Battery Voltage (V) × Battery Amp-Hours (Ah)

Example:
- UPS: 10 kVA with 192V battery bank, 100 Ah batteries
- Battery capacity: 192V × 100 Ah = 19,200 Wh
- Load: 6,960W (from above)
- Runtime: 19,200 Wh / 6,960W = 2.76 hours (~165 minutes) at full load
- Note: Runtime decreases non-linearly as load increases (Peukert effect)
```

**Runtime Requirements:**
- **Critical Facilities (Tier 1):** 15 minutes minimum at full load (allow time for generator startup and stabilization)
- **Standard Facilities (Tier 2):** 5 minutes minimum at full load (allow time for graceful shutdown)

**Sizing Tools:**
- UPS manufacturer online sizing tools (APC, Eaton, Schneider Electric)
- Professional assessment for large installations (>50 kVA)

#### 2.2.3 UPS Redundancy

**Redundancy Levels:**

**N (No Redundancy):**
- Single UPS, single power path
- Capacity: 100% of load
- Risk: UPS failure or maintenance causes downtime
- Use case: Standard facilities (Tier 2) where brief downtime acceptable

**N+1 (Basic Redundancy):**
- Multiple UPS units, single power path
- Capacity: N units to support load, +1 additional unit for redundancy
- Example: 3× 10 kVA UPS to support 20 kVA load (each UPS 50% loaded, can lose 1 UPS)
- Risk: Maintenance on UPS requires careful load management
- Use case: Critical facilities (Tier 1) basic redundancy

**2N (Full Redundancy):**
- Dual independent power paths (A and B)
- Each path has 100% capacity (full N capacity on each path)
- Capacity: 2× 100% of load (Path A: 100%, Path B: 100%)
- Equipment: Dual power supply servers (PDU A + PDU B)
- Risk: Extremely low (both paths must fail simultaneously)
- Use case: Mission-critical datacenters (Tier III/IV per Uptime Institute)

**2N+1 (High Redundancy):**
- Dual independent power paths, each with N+1 redundancy
- Path A: N+1 UPS, Path B: N+1 UPS
- Use case: Tier IV datacenters (fault-tolerant)

**[Organization] Requirements:**
- Critical facilities (Tier 1): N+1 minimum (2N for mission-critical)
- Standard facilities (Tier 2): N configuration acceptable

#### 2.2.4 UPS Monitoring

**Real-Time Monitoring Parameters:**
- Input voltage and frequency (utility power quality)
- Output voltage and frequency (power to protected load)
- Load percentage (current load / UPS capacity × 100%)
- Battery status:
  - Battery voltage
  - Battery charge percentage
  - Battery health (estimated remaining capacity vs. new)
  - Battery runtime remaining (at current load)
- UPS operating mode: Normal (on utility), on battery, bypass
- Alarms: Overload, battery low, battery failure, UPS failure

**Monitoring Methods:**
- SNMP: UPS SNMP agent (integrate with network monitoring system)
- Web interface: UPS built-in web server (browser access)
- Serial/USB: Direct connection to UPS (legacy monitoring)
- Cloud-based: UPS manufacturer cloud monitoring (Schneider EcoStruxure, Eaton Intelligent Power Manager)

**Alert Configuration:**
- **Critical Alerts (Immediate Notification):**
  - UPS on battery (utility power lost)
  - Battery low (<5 minutes runtime remaining)
  - UPS overload (load >100% capacity)
  - UPS failure or bypass mode
- **Warning Alerts (Investigate Within 1 Hour):**
  - Battery health degraded (<80% of original capacity)
  - Input voltage outside normal range (not triggering transfer to battery, but poor power quality)
  - UPS load high (>80% capacity, plan for capacity increase)

#### 2.2.5 UPS Battery Maintenance

**Battery Type:**
- **VRLA (Valve-Regulated Lead-Acid):** Most common, sealed (no maintenance), 3-5 year lifespan, sensitive to temperature
- **Lithium-Ion:** Longer lifespan (10+ years), smaller/lighter, wider temperature tolerance, higher cost (2-3× VRLA)

**Battery Lifespan Factors:**
- **Temperature:** VRLA battery life halves for every 10°C above 25°C (reason for HVAC in datacenters)
- **Cycling:** Frequent discharge/recharge cycles reduce lifespan
- **Voltage:** Overcharging or undercharging reduces lifespan
- **Age:** Batteries degrade over time even if not used

**Battery Replacement:**
- **VRLA batteries:** 3-5 years typical (3 years in hot environments, 5 years in controlled temperature)
- **Lithium-Ion batteries:** 10+ years typical
- **Replace when:** Battery health <80% of original capacity, or manufacturer recommended interval

**Battery Replacement Cost:**
- VRLA battery replacement: $100-300 per kVA UPS capacity (example: 10 kVA UPS = $1,000-3,000 battery replacement)
- Budget: Annual budget for battery replacement (replace 1/3 to 1/5 of UPS population per year on rotating basis)

#### 2.2.6 UPS Testing

**Monthly Testing:**
- **Battery self-test:** Automated (UPS performs self-test, verifies battery capacity)
  - Duration: 10-30 seconds (brief discharge test)
  - Verify: No alarms, battery health acceptable
- **Document:** Test date, UPS ID, pass/fail, battery health percentage

**Quarterly Testing:**
- **Load test (runtime verification):**
  - Procedure: Disconnect utility power (transfer UPS to battery), run on battery until 50% discharge
  - Duration: Varies (calculate based on UPS capacity and load)
  - Verify: Runtime meets requirement (15 min for Tier 1, 5 min for Tier 2)
- **Coordination:** Schedule during maintenance window (impacts protected equipment if UPS fails)
- **Document:** Test date, UPS ID, load percentage, runtime achieved, pass/fail

**Annual Testing:**
- **Full discharge test (optional, for critical facilities):**
  - Discharge battery to 100% (until UPS shuts down)
  - Verify: Total runtime, battery capacity
  - Risk: Stress on batteries (only perform if critical to verify full runtime)
- **Professional inspection:**
  - Licensed electrician or UPS technician
  - Inspect: Battery terminals (corrosion), connections (tightness), cabinet (cleanliness)
  - Replace batteries if health <80% or age exceeds manufacturer recommendation

**Testing Documentation:**
- Test logs: All monthly, quarterly, annual tests (past 12 months minimum)
- Test failures: Documented with corrective actions (battery replacement, UPS repair)

### 2.3 Backup Generator

#### 2.3.1 Generator Requirements

**Generator Necessity:**
- **Critical Facilities (Tier 1):** Backup generator mandatory (cannot rely on 15-min UPS runtime alone)
- **Standard Facilities (Tier 2):** Generator optional (risk-based decision - consider outage frequency, acceptable downtime)

**Generator Sizing:**
```
Step 1: Calculate Critical Load (Watts)
- UPS-protected load + HVAC + lighting + other critical systems
- Example: 10 kW (UPS load) + 5 kW (HVAC) + 1 kW (lighting) = 16 kW

Step 2: Add Growth Margin
- Add 20% for future load growth
- Example: 16 kW × 1.2 = 19.2 kW

Step 3: Apply Safety Factor (Motor Starting)
- Motors (HVAC compressors) require 1.5-3× running current to start
- Safety factor: 1.3-1.5× calculated load
- Example: 19.2 kW × 1.3 = 24.96 kW

Step 4: Select Generator Capacity
- Choose next standard generator size: 25 kW generator (in this example)
```

**Runtime Requirements:**
- **Critical Facilities (Tier 1):** 24+ hours at full load minimum (48-72 hours recommended)
- **Standard Facilities (Tier 2) (if generator installed):** 8+ hours at full load minimum

**Fuel Calculation:**
```
Fuel Consumption (typical diesel generator):
- Full load: ~0.3-0.4 gallons per kWh (varies by generator efficiency)
- 50% load: ~0.2-0.3 gallons per kWh (better efficiency at partial load)

Example (25 kW generator, 24-hour runtime at 50% load):
- Load: 12.5 kW
- Runtime: 24 hours
- Energy: 12.5 kW × 24 hours = 300 kWh
- Fuel: 300 kWh × 0.25 gal/kWh = 75 gallons

Fuel tank sizing: 100 gallons provides ~32 hours at 50% load (includes safety margin)
```

**Fuel Type:**
- **Diesel:** Most common (datacenters), long shelf life, reliable
- **Natural Gas:** Lower maintenance (no fuel storage), utility-supplied (vulnerable to same outage as electric)
- **Propane:** Alternative to diesel, longer shelf life than diesel, requires storage tank

#### 2.3.2 Automatic Transfer Switch (ATS)

**ATS Function:**
- Monitors utility power quality
- Starts generator on utility power loss
- Transfers load from utility to generator (after generator stabilizes)
- Transfers load from generator back to utility (after utility power restored)

**Transfer Time:**
- Transfer time: <10 seconds typical (from utility loss to generator power delivery)
- UPS runtime must exceed transfer time (15-min UPS runtime provides ample margin)

**Transfer Types:**
- **Open-transition (break-before-make):** Brief power interruption during transfer (<100ms) - most common, less expensive
- **Closed-transition (make-before-break):** No power interruption (generator synchronized with utility before transfer) - more expensive, used for sensitive loads

**Failover Sequence:**
```
1. Utility power lost (voltage sag or complete loss)
2. ATS detects loss (within 1-2 seconds)
3. ATS signals generator to start
4. Generator starts (cranks until running, 5-15 seconds typical)
5. Generator warms up and stabilizes (voltage and frequency, 5-15 seconds)
6. ATS transfers load to generator (total time: <10 seconds from utility loss)
7. Generator powers load (duration: until fuel exhausted or utility restored)
```

**Failback Sequence:**
```
1. Utility power restored (voltage and frequency normal)
2. ATS detects utility restoration (monitors for 5-15 minutes to ensure stable)
3. ATS transfers load back to utility
4. Generator continues running (cool-down period, 5-10 minutes)
5. Generator shuts down automatically
```

**ATS Configuration:**
- Failover: Automatic (on utility loss)
- Failback: Manual or delayed automatic (prevent thrashing if utility unstable)
  - Manual failback: Operator verifies utility stable before transferring back
  - Delayed automatic: ATS waits 15-30 minutes after utility restoration before transferring back

#### 2.3.3 Generator Testing

**Monthly Testing - No-Load Test:**
- **Procedure:**
  1. Manual start generator (push start button or remote start)
  2. Run generator 15-30 minutes (no load or minimal load)
  3. Monitor: Voltage, frequency, oil pressure, coolant temperature, no alarms
  4. Shut down generator
- **Purpose:** Verify generator starts and runs, keep engine lubricated, prevent "wet stacking" (diesel)
- **Wet Stacking:** Carbon buildup in diesel engine (occurs with frequent no-load or light-load operation) - mitigated by monthly load testing

**Quarterly Testing - Load Test (50% Load):**
- **Procedure:**
  1. Transfer load to generator (via ATS or manual transfer)
  2. Run generator under 50% load for 1-2 hours
  3. Monitor: Voltage, frequency, load percentage, fuel consumption, no alarms
  4. Transfer load back to utility
  5. Shut down generator
- **Purpose:** Verify generator can support load, prevent wet stacking, verify ATS functionality
- **Coordination:** Schedule during low-usage period (early morning, weekend)

**Annual Testing - Full Load Test (100% Load):**
- **Procedure:**
  1. Transfer load to generator (via ATS)
  2. Add load bank if facility load <80% generator capacity (ensure full load test)
  3. Run generator under 100% load for 4+ hours
  4. Monitor: Voltage, frequency, load percentage, fuel consumption, temperature, no alarms
  5. Transfer load back to utility
  6. Shut down generator
- **Purpose:** Verify generator can sustain full load for extended period, burn off carbon deposits (wet stacking), verify capacity
- **Load Bank:** Portable resistive load (if facility load insufficient for full load test)

**Testing Documentation:**
- **Test Log Contents:**
  - Date and time
  - Test type (no-load, 50% load, 100% load)
  - Runtime (minutes/hours)
  - Load percentage (if load test)
  - Fuel consumption (gallons)
  - Voltage and frequency readings
  - Oil pressure, coolant temperature
  - Alarms or issues
  - Pass/fail
  - Technician name

#### 2.3.4 Generator Maintenance

**Maintenance Schedule:**

**Monthly:**
- Visual inspection (oil leaks, coolant leaks, fuel leaks, loose connections)
- Oil level check (add oil if low)
- Coolant level check (add coolant if low)
- Fuel level check (refuel if <50%)
- Battery voltage check (generator starting battery, replace if <12.4V)

**Semi-Annual:**
- Oil change (or per manufacturer recommendation, typically 100-200 hours of operation)
- Oil filter replacement
- Fuel filter replacement
- Air filter inspection (replace if dirty)

**Annual:**
- Professional inspection (licensed generator technician)
- Coolant change (or per manufacturer, typically every 2 years)
- Spark plugs replacement (natural gas/propane generators)
- Battery replacement (generator starting battery, every 3-5 years)
- Belts and hoses inspection (replace if cracked or worn)

**Manufacturer Maintenance Schedule:**
- Follow generator manufacturer maintenance schedule (diesel, natural gas, propane have different requirements)
- Manufacturer service contract: Consider for critical facilities (scheduled maintenance, priority service)

#### 2.3.5 Fuel Supply Management

**On-Site Fuel Tank:**
- Tank size: 24-72 hours runtime at 50% load (see Section 2.3.1 fuel calculation)
- Tank type: Above-ground (easier inspection, maintenance) or below-ground (aesthetic, space savings)
- Tank material: Steel (most common) or fiberglass (corrosion-resistant)
- Tank location: Adjacent to generator, secure area

**Fuel Quality:**
- Diesel fuel shelf life: 6-12 months (degrades over time, algae growth)
- Fuel additives: Stabilizers (extend shelf life), biocides (prevent algae growth)
- Fuel testing: Annual (test for contamination, water content)
- Fuel polishing: If contamination detected (filter fuel to remove water and particulates)

**Fuel Delivery Contract:**
- Emergency fuel delivery: Contract with fuel supplier for emergency delivery (<24 hours)
- Use case: Prolonged utility outage (hurricane, major grid failure)
- Fuel capacity: 100-200 gallons typical emergency delivery

**Fuel Monitoring:**
- Fuel level sensor: Monitor fuel level (gauge on tank or electronic sensor)
- Alert: Alert when fuel <25% (allows time to refuel before running out)
- Refueling procedure: Schedule refueling when fuel <50% (routine) or emergency refueling during prolonged outage

**Fuel Safety:**
- Fuel storage regulations: Comply with local fire code (tank size limits, setback requirements, spill containment)
- Spill containment: Secondary containment (berm or double-wall tank)
- Fire suppression: Fire extinguisher near generator and fuel tank

### 2.4 Power Redundancy Levels

Summary of power redundancy architectures (aligned with Uptime Institute Tier classifications):

**N (No Redundancy) - Uptime Tier I:**
- Single utility feed
- Single UPS (or no UPS)
- No generator (or single generator)
- No redundancy
- Availability: 99.671% (28.8 hours downtime per year)

**N+1 (Component Redundancy) - Uptime Tier II:**
- Single utility feed
- Multiple UPS in parallel (N+1 configuration)
- Single generator (or N+1 generators)
- Component redundancy (can lose one UPS or generator)
- Availability: 99.741% (22.7 hours downtime per year)

**N+1 Concurrently Maintainable - Uptime Tier III:**
- Single utility feed (or dual feeds)
- Multiple UPS in parallel (N+1)
- Multiple generators (N+1)
- Concurrent maintenance (can maintain equipment without downtime)
- Availability: 99.982% (1.6 hours downtime per year)

**2N or 2N+1 (Fault Tolerant) - Uptime Tier IV:**
- Dual utility feeds (diverse substations)
- Dual UPS paths (A and B, each path N+1)
- Dual generators (A and B, each path N+1)
- Fully redundant (can lose entire path without downtime)
- Availability: 99.995% (0.4 hours downtime per year)

**[Organization] Requirements:**
- Critical facilities (Tier 1): N+1 minimum (Uptime Tier II/III)
- Standard facilities (Tier 2): N configuration (Uptime Tier I)
- Mission-critical: 2N (Uptime Tier IV) if business requires 99.99%+ availability

### 2.5 Power Failure Procedures

#### 2.5.1 UPS Transition to Battery (Utility Power Loss)

**Automatic Sequence:**
1. Utility power lost (or voltage out of tolerance)
2. UPS transfers to battery power (instantaneous for online double-conversion, <5ms for line-interactive)
3. Protected equipment continues operating (uninterrupted)
4. UPS monitoring system generates alert: "UPS on battery" (immediate notification to facilities manager, IT operations)
5. If utility power restored within UPS runtime: UPS returns to normal operation, battery recharges
6. If utility power NOT restored within UPS runtime: Proceed to generator startup (if generator available) or graceful shutdown

**Personnel Actions:**
- Monitor situation (utility power restoration estimate, UPS runtime remaining)
- If generator available: Verify generator starts automatically (see Section 2.5.2)
- If no generator: Prepare for graceful shutdown (see Section 2.5.4)

#### 2.5.2 Generator Startup (Prolonged Utility Power Loss)

**Automatic Sequence (via ATS):**
1. UPS on battery (utility power lost)
2. ATS detects utility loss (1-2 seconds)
3. ATS signals generator to start
4. Generator cranks and starts (5-15 seconds)
5. Generator warms up (5-15 seconds, voltage and frequency stabilize)
6. ATS transfers load to generator (total time <10 seconds from utility loss)
7. Generator powers facility (UPS switches back to normal operation, using generator as utility)
8. UPS batteries recharge (from generator power)

**Personnel Actions:**
- Verify generator started and stabilized (check generator status, voltage, frequency, no alarms)
- Monitor generator operation (fuel level, oil pressure, temperature)
- Estimate outage duration (contact utility, check outage map)
- Arrange fuel delivery if prolonged outage expected (>24 hours)
- Notify stakeholders (management, business units) if extended outage expected

#### 2.5.3 Prolonged Outage Management (>1 Hour on Generator)

**Hourly Monitoring:**
- Generator status (running normally, no alarms)
- Fuel level (refuel if <50%, arrange emergency delivery if <25%)
- Load (ensure not overloaded)
- Environmental (temperature, HVAC status - HVAC powered by generator)

**Stakeholder Communication:**
- Notify stakeholders every 4 hours (status update, estimated restoration time)
- Escalate to executive management if outage >8 hours

**Fuel Management:**
- Monitor fuel consumption rate (gallons per hour)
- Calculate remaining runtime (fuel remaining / consumption rate)
- Arrange emergency fuel delivery if runtime <12 hours remaining

#### 2.5.4 Graceful Shutdown (No Generator or Generator Failure)

**If UPS Battery Depleting and No Generator:**

**Trigger:** UPS runtime remaining <10 minutes (or appropriate threshold based on shutdown time required)

**Shutdown Sequence:**
1. **Alert personnel:** Broadcast announcement (email, Slack, overhead paging if available)
2. **Save work:** Personnel save all work immediately
3. **Shutdown non-critical systems:** Shut down development environments, test systems, non-critical services
4. **Shutdown critical systems (prioritized):**
   - Applications (graceful shutdown, save state)
   - Databases (flush buffers, consistent state)
   - Virtual machine hosts (shut down VMs, then hosts)
   - Storage systems (flush cache, shut down)
   - Network equipment (last to shut down - leave connectivity for monitoring)
5. **UPS depletes:** Equipment loses power (hard shutdown if not shut down gracefully)

**Shutdown Time Estimate:**
- Typical shutdown time: 5-15 minutes (depending on number of systems and dependencies)
- UPS runtime threshold: Set to 10-15 minutes (provides buffer for graceful shutdown)

**Startup After Power Restoration:**
1. Verify utility power stable (wait 15-30 minutes after restoration)
2. Verify HVAC operational (environmental conditions acceptable)
3. Start equipment in reverse order (infrastructure first, applications last):
   - Storage systems
   - Network equipment
   - Virtual machine hosts
   - Databases
   - Applications
4. Verify systems operational (test applications, verify data integrity)
5. Notify stakeholders (systems restored, normal operations resumed)

---

## 3. HVAC and Cooling

### 3.1 HVAC Capacity Requirements

#### 3.1.1 Cooling Load Calculation

**Heat Load Sources:**
- IT equipment (servers, network, storage) - primary heat source
- Lighting
- Personnel (human body heat)
- Solar gain (windows, skylights)
- Building envelope (heat transfer through walls, roof)

**IT Equipment Heat Load:**
```
Heat load (BTU/hr) = IT equipment power consumption (Watts) × 3.41 BTU/Watt

Example:
- IT equipment: 10 kW (10,000 W)
- Heat load: 10,000 W × 3.41 = 34,100 BTU/hr (2.84 tons)

Note: 1 ton of cooling = 12,000 BTU/hr
```

**Total Cooling Requirement:**
```
Total cooling = IT equipment heat + Lighting heat + Personnel heat + Solar gain + Envelope heat

Simplified estimate:
Total cooling = IT equipment heat × Overhead factor

Overhead factor:
- Well-insulated datacenter, no windows: 1.2-1.3×
- Office with windows: 1.4-1.6×

Example (datacenter):
- IT heat: 34,100 BTU/hr
- Overhead factor: 1.3×
- Total cooling: 34,100 × 1.3 = 44,330 BTU/hr (3.69 tons)
- Select: 4-ton (48,000 BTU/hr) HVAC unit
```

**Cooling Capacity Verification:**
- Perform detailed load calculation for critical facilities (HVAC professional)
- Simple calculation acceptable for small server rooms (<10 kW IT load)

#### 3.1.2 HVAC Redundancy

**Redundancy Levels:**

**N (No Redundancy):**
- Single HVAC unit, 100% capacity
- Risk: HVAC failure causes temperature rise, potential equipment shutdown
- Use case: Standard facilities (Tier 2) where brief temperature excursion acceptable

**N+1 (Basic Redundancy):**
- Multiple HVAC units, total capacity >100% of required
- Example: 2× 3-ton units for 4-ton cooling requirement (each unit 75% loaded, can lose 1 unit)
- Benefits: One unit can fail or be maintained without loss of cooling
- Use case: Critical facilities (Tier 1) minimum requirement

**2N (Full Redundancy):**
- Dual independent HVAC systems, each 100% capacity
- Example: System A: 4-ton capacity, System B: 4-ton capacity (for 4-ton requirement)
- Benefits: Entire system can fail without loss of cooling
- Use case: Tier IV datacenters (fault-tolerant)

**[Organization] Requirements:**
- Critical facilities (Tier 1): N+1 minimum
- Standard facilities (Tier 2): N configuration acceptable

#### 3.1.3 Hot Aisle / Cold Aisle Containment (Datacenters)

**Hot Aisle / Cold Aisle Design:**
- Server racks arranged in alternating rows
- **Cold aisle:** Front of servers face cold aisle (intake cool air from HVAC)
- **Hot aisle:** Back of servers face hot aisle (exhaust hot air)
- HVAC supplies cool air to cold aisles, returns hot air from hot aisles

**Containment (Advanced):**
- **Cold aisle containment:** Enclose cold aisles (doors, roof) - contain cool air, prevent mixing with hot air
- **Hot aisle containment:** Enclose hot aisles (doors, roof) - contain hot air, return directly to HVAC
- Benefits: Increased efficiency (reduce mixing, allow higher return air temperature), increased capacity (more effective cooling)

**Equipment Placement:**
- High-density equipment (blade servers, GPU servers): Locate near HVAC supply (maximum cooling)
- Low-density equipment: Locate further from HVAC supply (less cooling required)

### 3.2 HVAC Monitoring and Alerting

**Monitoring Parameters:**
- **Temperature:** Intake (cold aisle), exhaust (hot aisle), return air (to HVAC)
- **Humidity:** Relative humidity percentage (target 40-60% RH, see POL-S3, Section 5.1.1)
- **HVAC unit status:** Running/stopped, compressor status, fan status, alarms
- **Airflow:** Airflow sensors (optional, detect obstructions or fan failure)

**Monitoring Integration:**
- Environmental monitoring system (see POL-S3, Section 5.2) - temperature and humidity sensors
- Building Management System (BMS) - HVAC unit status, controls
- Physical security dashboard (see POL-S2, Section 7.3) - unified view of environmental status

**Alert Thresholds:**
- **Temperature:**
  - Warning: 28-30°C (investigate within 1 hour)
  - Critical: >30°C (immediate response, see POL-S3, Section 5.3)
  - Rate-of-rise: >2°C per 10 minutes (indicates HVAC failure, immediate alert)
- **HVAC Unit Status:**
  - HVAC unit stopped: Immediate alert (critical)
  - HVAC alarm (compressor failure, low refrigerant, etc.): Immediate alert
- **Humidity:**
  - Warning: <30% RH or >70% RH (investigate within 1 hour)
  - Critical: <20% RH or >80% RH (immediate response, see POL-S3, Section 5.1.1)

### 3.3 HVAC Maintenance

**Maintenance Schedule:**

**Monthly:**
- Visual inspection (no unusual noises, no leaks, no alarms)
- Air filter replacement (or per manufacturer, typically monthly-quarterly depending on environment)
- Condensate drain check (ensure draining properly, not clogged)

**Quarterly:**
- Coil cleaning (evaporator coils, condenser coils - dust and debris reduce efficiency)
- Refrigerant level check (low refrigerant reduces cooling capacity)
- Belt inspection (if belt-driven fans - replace if cracked or worn)

**Semi-Annual:**
- Professional inspection (licensed HVAC technician)
- Refrigerant charge verification (measure superheat/subcooling)
- Electrical connections inspection (tightness, corrosion)

**Annual:**
- Comprehensive professional inspection
- Compressor oil level check (if applicable)
- Controls calibration (thermostats, pressure switches)

**Manufacturer Maintenance Schedule:**
- Follow HVAC manufacturer maintenance schedule (varies by unit type, age)
- Manufacturer service contract: Recommended for critical facilities (scheduled maintenance, priority service, discounted repairs)

### 3.4 HVAC Failure Response

**Upon HVAC Failure:**

**Immediate Actions:**
1. **Alert facilities manager:** Immediate notification (phone call)
2. **Verify failure:** Check HVAC unit (is it running, any alarms, circuit breaker tripped)
3. **Reduce IT load:** Shutdown non-critical systems (reduce heat generation)
4. **Deploy backup cooling:** If available (portable HVAC units, see Section 3.5)
5. **Monitor temperature:** Continuous monitoring (every 5 minutes)

**If Temperature Rising Rapidly (>2°C per 10 minutes):**
1. **Escalate:** Notify IT operations, management
2. **Engage HVAC vendor:** Emergency service call (if internal resolution unsuccessful)
3. **Prepare for shutdown:** If temperature approaching critical (>35°C), prepare for graceful shutdown (see Section 2.5.4)

**If Multiple HVAC Units (N+1 Redundancy):**
- Remaining units should handle load (verify temperature stable)
- Repair failed unit promptly (restore redundancy)

**Post-Incident:**
- Root cause analysis (why did HVAC fail - age, maintenance neglect, component failure, insufficient capacity)
- Corrective actions (repair, capacity increase, redundancy implementation, maintenance frequency increase)
- Testing (verify repair effective, test backup cooling deployment if used)

### 3.5 Backup Cooling (Emergency)

**Portable HVAC Units:**
- Use case: Emergency cooling during HVAC failure (short-term, hours to days)
- Capacity: Typically 1-5 tons (12,000-60,000 BTU/hr) portable units
- Deployment: Roll into room, vent exhaust outside (window, temporary duct)
- Limitations: Noisy, requires exhaust venting, requires power (ensure generator capacity if on generator)

**Portable HVAC Procurement:**
- Option 1: Own portable units (stored on-site, ready for deployment)
- Option 2: Rental contract (rent from equipment rental company, 24-hour delivery)
- Recommendation: Critical facilities (Tier 1) should own at least one portable unit (25-50% of primary HVAC capacity)

**Deployment Plan:**
- Deployment time: Target <2 hours from HVAC failure to backup cooling operational
- Deployment team: Facilities staff trained on portable HVAC deployment
- Testing: Annual deployment drill (verify equipment functional, staff trained)

---

## 4. Telecommunications Infrastructure

### 4.1 Internet Connectivity Resilience

#### 4.1.1 ISP Redundancy Requirements

**Critical Facilities (Tier 1):**
- Dual ISP (two independent Internet Service Providers)
- Diverse carriers (different providers, not just different circuits from same provider)
- Diverse paths (different physical routes - different streets, different buildings, different Point of Presence)
- Bandwidth: 100% of normal load per ISP (not load-balanced - each ISP can handle full load independently)
- Failover: Automatic (BGP preferred) or manual (within 15 minutes)

**Standard Facilities (Tier 2):**
- Single ISP with SLA (Service Level Agreement)
- Bandwidth: Sized for normal load
- Backup ISP: Optional (risk-based decision)

#### 4.1.2 ISP Diversity

**Diverse Carriers:**
- Primary ISP: Carrier A (e.g., Comcast Business)
- Secondary ISP: Carrier B (e.g., Verizon Business, AT&T) - different company
- Avoid: Two circuits from same carrier (carrier outage affects both circuits)

**Diverse Paths:**
- Physical diversity: Circuits enter building from different sides (different conduits, different risers)
- Geographic diversity: Circuits route through different central offices / Points of Presence (PoPs)
- Verification: Request ISP provide route diversity documentation (prove paths are diverse)

**Diverse Technologies (Optional):**
- Primary ISP: Fiber (high bandwidth, high reliability)
- Secondary ISP: Cable/DSL (different infrastructure, lower cost)
- Backup ISP: 4G/5G cellular (different infrastructure, wireless)
- Benefits: Different infrastructures reduce common failure modes (fiber cut does not affect cellular)

#### 4.1.3 Failover Mechanisms

**BGP (Border Gateway Protocol) Failover (Automatic):**
- Organization has own AS (Autonomous System) number and IP address space
- Both ISPs advertise organization's IP prefixes via BGP
- Failover: Automatic (routing protocols detect ISP failure, reroute traffic to backup ISP, typically 1-5 minutes)
- Benefits: Seamless failover, no IP address changes (same IP space usable on both ISPs)
- Complexity: Requires BGP knowledge, router configuration, coordination with ISPs
- Use case: Large organizations (datacenters, enterprises with >100 users)

**Manual Failover (15 Minutes):**
- Primary ISP provides primary IP addressing (default route)
- Secondary ISP on standby (not actively used)
- Failover procedure:
  1. Detect primary ISP failure (monitoring system alerts)
  2. Manually change router configuration (switch default route to secondary ISP)
  3. Change DNS records (if IP address changes) - propagation delay 5-60 minutes
  4. Notify users (some may need to reconnect VPNs, etc.)
- Benefits: Simpler than BGP (no AS number required, less complex routing)
- Drawbacks: Manual intervention required, slower failover (15 minutes+ depending on DNS propagation)
- Use case: Small to medium organizations

**Load-Balanced Configuration (NOT Recommended for Resilience):**
- Both ISPs actively used (traffic split 50/50)
- Failure: If one ISP fails, remaining ISP handles 100% of traffic (must have sufficient bandwidth)
- Issues: Often implemented incorrectly (both ISPs do not have full capacity, congestion during failover)
- Recommendation: Use active/standby (BGP or manual) rather than active/active for resilience

#### 4.1.4 Telecommunications Monitoring

**Circuit Monitoring:**
- **Circuit status:** Up/down monitoring (ICMP ping to ISP gateway, SNMP monitoring)
- **Bandwidth utilization:** Current usage vs. total bandwidth (identify congestion)
- **Latency:** Round-trip time to Internet destinations (detect performance degradation)
- **Packet loss:** Percentage of packets lost (detect link quality issues)

**Monitoring Tools:**
- Network monitoring system (Nagios, Zabbix, PRTG, SolarWinds, Datadog)
- ISP-provided monitoring (some ISPs provide portal with circuit status, performance)

**Alert Thresholds:**
- Circuit down: Immediate alert (critical)
- High utilization (>80%): Warning (plan for bandwidth increase)
- High latency (>100ms to nearby Internet destinations): Warning (investigate)
- Packet loss (>1%): Warning (investigate link quality)

### 4.2 ISP Service Level Agreements (SLAs)

#### 4.2.1 SLA Components

**Uptime SLA:**
- Typical: 99.9% uptime (8.76 hours downtime per year acceptable)
- Premium: 99.99% uptime (52.56 minutes downtime per year acceptable)
- Calculation: Uptime % = (Total time - Downtime) / Total time × 100%

**Mean Time To Repair (MTTR):**
- Typical: <4 hours (ISP will restore service within 4 hours of outage)
- Premium: <2 hours or <1 hour (faster restoration for critical circuits)

**Latency (Optional):**
- Some ISPs guarantee latency to specific Internet exchange points (IXPs)
- Example: <10ms latency to local IXP

**Support Response Time:**
- Typical: 4-hour response (ISP acknowledges trouble ticket within 4 hours)
- Premium: 1-hour response or 24/7 NOC phone support

#### 4.2.2 SLA Verification and Penalties

**SLA Reporting:**
- ISPs provide monthly SLA reports (uptime, MTTR for incidents, SLA compliance)
- Review reports: Facilities manager or IT operations reviews monthly (verify SLA met)

**SLA Penalties (Credits):**
- If SLA not met: ISP provides service credit (percentage of monthly bill)
- Example: 99.9% SLA, actual 99.5% uptime → 10-20% monthly credit
- Credits are NOT automatic: Must request credit based on SLA report

**SLA Exclusions:**
- Scheduled maintenance: Does not count against SLA (if proper notice given, typically 5-7 days)
- Force majeure: Natural disasters, acts of war, etc. (excluded from SLA)

### 4.3 Network Equipment Power Protection

**UPS Protection for Network Equipment:**
- All network equipment (routers, switches, firewalls, wireless controllers) SHALL be UPS-protected
- Rationale: Network equipment is critical infrastructure (required for telecommunications, physical security systems, environmental monitoring)

**Dual Power Supply Equipment (Optional):**
- Some network equipment has dual power supplies (A and B)
- Configuration: PSU A → PDU A (UPS A), PSU B → PDU B (UPS B)
- Benefits: Equipment survives single UPS failure or single PDU failure
- Use case: Core network equipment in critical facilities (Tier 1)

### 4.4 Telecommunications Failover Testing

**Quarterly Failover Testing:**
- **Procedure:**
  1. Schedule test during low-usage period (early morning, weekend)
  2. Disable primary ISP (shutdown router interface or unplug circuit)
  3. Verify failover to secondary ISP (automatic via BGP or manual reconfiguration)
  4. Test connectivity (ping external sites, access applications, VPN connectivity)
  5. Measure failover time (from primary ISP down to secondary ISP operational)
  6. Re-enable primary ISP, verify failback
- **Target Failover Time:**
  - BGP automatic failover: <5 minutes
  - Manual failover: <15 minutes
- **Document:**
  - Test date, time
  - Failover time (actual)
  - Connectivity verification (pass/fail)
  - Issues (if any)

**Testing Coordination:**
- Notify users (brief connectivity interruption possible during failover test)
- Coordinate with IT operations (verify applications accessible after failover)

### 4.5 Telephone System Resilience

**VoIP System (Modern Approach):**
- Voice over IP (VoIP) phone system (Cisco, Avaya, Microsoft Teams, Zoom Phone, etc.)
- Resilience: VoIP system runs on servers (UPS-protected, VM for easy DR)
- Internet dependency: VoIP calls route over Internet (requires ISP redundancy, see Section 4.1)

**Analog Lines (Legacy/Backup):**
- Traditional telephone lines (POTS - Plain Old Telephone Service)
- Use case: Emergency backup (if VoIP fails), elevators (emergency phone), fire alarm (monitoring connection)
- Number: 1-2 analog lines sufficient for emergency use
- Benefits: Independent of power (line-powered), independent of Internet

**Mobile Phones (Backup Communication):**
- Employees use mobile phones during facility telecommunications outage
- Emergency contact list: All key personnel have mobile phones listed (facilities manager, IT operations, management)

---

## 5. Water Supply (If Applicable)

### 5.1 Water for Cooling Systems

**Water-Cooled HVAC (Chilled Water Systems):**
- Some large datacenters use chilled water cooling (more efficient than air-cooled for high-density)
- Water supply: Municipal water or on-site cooling tower (evaporative cooling)

**Water Supply Resilience:**
- Municipal water: Typically reliable (utility-supplied, redundant sources)
- Cooling tower: Requires water makeup (evaporation loss), pump redundancy (N+1)

**Backup Water Supply (Critical Facilities with Water-Cooled HVAC):**
- Water storage tank: 24-48 hours of makeup water (for cooling tower evaporation loss)
- Emergency water delivery: Contract with water hauler (if prolonged municipal water outage)

### 5.2 Water Supply Monitoring

**Monitoring Parameters:**
- Water pressure (adequate pressure for cooling system operation)
- Water flow (detect flow loss, pump failure)
- Water level (if storage tank - alert when level low)

**Alerts:**
- Low water pressure: Warning (investigate within 1 hour)
- No water flow: Critical (immediate alert - HVAC may fail)
- Low water level (storage tank): Warning (<25%, arrange water delivery)

---

## 6. Utility Failure Procedures

### 6.1 Power Failure Response

**Immediate Response (UPS on Battery):**
1. **Alert generated:** "UPS on battery" alert sent to facilities manager, IT operations (email, SMS)
2. **Monitor situation:** Check UPS runtime remaining, verify generator starting (if applicable)
3. **Notify stakeholders:** If utility outage expected to be prolonged (>30 minutes), notify management

**Generator Running (Utility Outage >10 Seconds):**
1. **Verify generator operational:** Check generator status (running, voltage/frequency normal, no alarms)
2. **Monitor fuel level:** Calculate runtime based on fuel remaining and consumption rate
3. **Arrange fuel delivery:** If outage expected >24 hours and fuel <50%
4. **Notify stakeholders:** Update every 4 hours (status, estimated restoration time)

**No Generator or Generator Failure:**
1. **Prepare for graceful shutdown:** Trigger graceful shutdown when UPS runtime <10 minutes remaining (see Section 2.5.4)
2. **Save all work:** Alert personnel to save work immediately
3. **Shutdown systems:** Prioritized shutdown (non-critical first, then critical in reverse-dependency order)

**Post-Restoration:**
1. **Verify utility power stable:** Wait 15-30 minutes after restoration (ensure not transient restoration)
2. **Transfer from generator to utility:** ATS transfers automatically (or manual transfer if manual ATS)
3. **Start systems:** Reverse-order startup (infrastructure first, then applications)
4. **Document incident:** Power outage duration, generator operation (if applicable), issues, lessons learned

### 6.2 HVAC Failure Response

**Immediate Response (HVAC Unit Stopped):**
1. **Alert generated:** HVAC failure alert (BMS, environmental monitoring system)
2. **Facilities manager notified:** Immediate (phone call)
3. **Investigate cause:** Check HVAC unit (is it running, circuit breaker, thermostat, refrigerant, alarms)
4. **Reduce IT load:** Shutdown non-critical systems (reduce heat generation)
5. **Deploy backup cooling:** If available (portable HVAC units, see Section 3.5)
6. **Monitor temperature:** Continuous (every 5 minutes)

**If Temperature Rising Rapidly:**
1. **Engage HVAC vendor:** Emergency service call (if internal troubleshooting unsuccessful)
2. **Escalate:** Notify IT operations, management
3. **Prepare for shutdown:** If temperature approaching critical (>35°C), prepare for graceful shutdown

**N+1 Redundancy (Multiple HVAC Units):**
- If one unit fails and N+1 redundancy: Remaining units should handle load
- Verify temperature stable (if stable, urgency reduced but still repair failed unit promptly)

**Post-Incident:**
- Root cause analysis (component failure, refrigerant loss, electrical issue, maintenance neglect)
- Corrective actions (repair, preventive maintenance schedule review, capacity assessment)
- Testing (verify repair, test backup cooling if used)

### 6.3 Telecommunications Failure Response

**Immediate Response (ISP Circuit Down):**
1. **Alert generated:** Circuit down alert (network monitoring system)
2. **Investigate cause:** Verify circuit actually down (not internal router/switch issue)
3. **Contact ISP:** Report outage (ISP trouble ticket), request estimated restoration time
4. **Failover to backup ISP:** If available (automatic via BGP or manual failover, see Section 4.1.3)
5. **Notify users:** If backup ISP not available or users need to reconnect VPNs

**Single ISP (No Backup):**
- Users unable to access Internet/cloud services until ISP restores circuit
- Work offline (local applications, saved documents)
- Mobile hotspots (temporary Internet access for critical users)

**Dual ISP (Backup Available):**
- Failover to backup ISP (automatic or manual)
- Verify connectivity restored (test applications, VPN)
- Monitor backup ISP (ensure not overloaded, sufficient bandwidth)
- Continue operations normally (minimal disruption)

**Post-Restoration:**
1. **Verify primary ISP restored:** Test connectivity
2. **Failback to primary ISP:** If using backup ISP (automatic via BGP or manual)
3. **Document incident:** ISP outage duration, cause (if known), failover success/failure
4. **Review ISP SLA:** If outage duration exceeds SLA, request credit

---

## 7. Utility Monitoring

### 7.1 Unified Utility Monitoring Dashboard

**Dashboard Purpose:**
- Real-time visibility into utility infrastructure status (power, HVAC, telecommunications)
- Proactive alerting on utility failures or degradation
- Historical trending (identify patterns, plan capacity upgrades)

**Dashboard Metrics:**

**Power:**
- Utility power status (normal, out of tolerance, lost)
- UPS status (normal, on battery, bypass)
- UPS load percentage (current load / capacity)
- UPS battery health (percentage of original capacity)
- UPS runtime remaining (minutes at current load)
- Generator status (off, running, alarms)
- Generator fuel level (gallons remaining, runtime remaining)

**HVAC:**
- HVAC unit status (running, stopped, alarms) per unit
- Temperature (intake, exhaust, return air) per zone
- Humidity (percentage RH) per zone
- Temperature excursions (count this month)

**Telecommunications:**
- ISP circuit status (up, down) per circuit
- Bandwidth utilization (percentage) per circuit
- Latency (ms) to key Internet destinations
- Packet loss (percentage)

**Utility Incidents:**
- Open utility incidents (unresolved power/HVAC/telecom failures)
- Incident count (this month, trend)
- Mean time to repair (MTTR) - average incident resolution time

### 7.2 Monitoring Platform Options

**Building Management System (BMS):**
- Integrated platform for HVAC, lighting, power monitoring (Schneider Electric, Siemens, Johnson Controls)
- Pros: Single platform, professional integration, building-wide view
- Cons: Expensive (enterprise-grade systems), requires professional installation/configuration

**Network Monitoring System:**
- Nagios, Zabbix, PRTG, SolarWinds, Datadog - network-focused, can monitor utilities via SNMP
- Pros: IT-friendly (familiar tools), integrate with existing network monitoring
- Cons: May require additional sensors/gateways for HVAC/power monitoring

**IoT Monitoring Platforms:**
- Cloud-based (Ubiquiti UniFi sensors, Monnit, AWS IoT, Azure IoT)
- Pros: Low cost, easy deployment (wireless sensors), cloud-based (accessible anywhere)
- Cons: Subscription cost (per sensor), Internet-dependent

**Hybrid Approach:**
- Use multiple platforms, integrate via APIs
- Example: BMS for HVAC, UPS manufacturer cloud platform for power, network monitoring for ISP
- Integrate into unified dashboard (Grafana, Power BI, custom web dashboard)

### 7.3 Alerting Configuration

**Alert Recipients:**
- **Critical alerts (immediate):** Facilities manager (SMS, phone call), IT operations (email, SMS)
- **Warning alerts (1-hour response):** Facilities manager (email), IT operations (email)
- **Informational alerts:** Dashboard only (no notification)

**Alert Examples:**

**Power - Critical:**
- UPS on battery
- UPS battery low (<5 min runtime remaining)
- UPS failure or bypass mode
- Generator failure to start
- Generator fuel low (<25%)

**Power - Warning:**
- UPS load high (>80%)
- UPS battery health degraded (<80%)
- Generator fuel level (<50%)

**HVAC - Critical:**
- HVAC unit stopped
- Temperature >30°C (see POL-S3)
- Rate-of-rise >2°C per 10 minutes

**HVAC - Warning:**
- HVAC alarm (any unit alarm)
- Temperature 28-30°C (see POL-S3)

**Telecommunications - Critical:**
- ISP circuit down
- Both ISPs down (if dual ISP)

**Telecommunications - Warning:**
- ISP circuit high latency (>100ms)
- ISP circuit packet loss (>1%)
- ISP bandwidth utilization high (>80%)

### 7.4 Monitoring Data Retention

**Raw Data:**
- Retention: 12 months minimum
- Resolution: 5-minute intervals (power, HVAC), 1-minute intervals (telecommunications)
- Storage: Time-series database (InfluxDB, Prometheus) or BMS/monitoring platform storage

**Aggregated Data:**
- Retention: 3 years
- Resolution: 1-hour averages
- Purpose: Long-term trending, capacity planning

**Incident Data:**
- Retention: 5 years
- Contents: All utility failure events (duration, cause, resolution, impact)
- Purpose: Compliance (audit evidence), trend analysis, root cause analysis

---

## 8. Measurable Requirements and Audit Verification

### 8.1 Compliance Metrics

The following metrics SHALL be measured to demonstrate Control A.7.11 compliance:

#### 8.1.1 Power Uptime Metrics

**Power Uptime:**
- Metric: Percentage of time utility or generator power available to protected load
- Target: 99.99% (critical facilities - 52.56 min downtime/year), 99.9% (standard facilities - 8.76 hours downtime/year)
- Measurement: (Total time - Downtime) / Total time × 100%
- Audit evidence: UPS monitoring logs, power outage incident reports (past 12 months)

**UPS Runtime:**
- Metric: Minutes of UPS runtime at current load (measured during quarterly load test)
- Target: 15 minutes minimum (critical facilities), 5 minutes minimum (standard facilities)
- Measurement: Quarterly load test (discharge UPS to 50%, measure runtime)
- Audit evidence: UPS test logs (quarterly tests, past 12 months)

**Generator Availability:**
- Metric: Percentage of time generator available (operational, not failed)
- Target: 99% minimum (critical facilities with generators)
- Measurement: (Total time - Generator downtime for failures) / Total time × 100%
- Audit evidence: Generator test logs, generator failure incident reports (past 12 months)

**UPS Battery Health:**
- Metric: Battery capacity as percentage of original capacity
- Target: >80% (replace batteries when <80%)
- Measurement: UPS battery self-test (monthly) or load test (quarterly)
- Audit evidence: UPS monitoring logs showing battery health percentage

#### 8.1.2 HVAC Uptime Metrics

**HVAC Uptime:**
- Metric: Percentage of time HVAC operational (providing adequate cooling)
- Target: 99.9% (critical facilities - 8.76 hours downtime/year), 99% (standard facilities - 3.65 days downtime/year)
- Measurement: (Total time - HVAC downtime) / Total time × 100%
- Audit evidence: HVAC monitoring logs, temperature monitoring logs (past 12 months)

**Temperature Excursions:**
- Metric: Count of temperature excursions per month (outside target range 18-27°C)
- Target: <5 per month (per facility)
- Measurement: Query environmental monitoring system (threshold breach count)
- Audit evidence: Monthly temperature monitoring reports (past 12 months)

#### 8.1.3 Telecommunications Uptime Metrics

**ISP Uptime:**
- Metric: Percentage of time ISP circuit operational
- Target: Meets ISP SLA (typically 99.9% per ISP)
- Measurement: (Total time - Circuit downtime) / Total time × 100%
- Audit evidence: ISP SLA reports (monthly, past 12 months), network monitoring logs

**ISP Failover Success Rate:**
- Metric: Percentage of failover tests successful (for dual ISP configurations)
- Target: 100%
- Measurement: Successful failover tests / Total failover tests × 100%
- Audit evidence: ISP failover test reports (quarterly tests, past 12 months)

#### 8.1.4 Testing Compliance Metrics

**UPS Battery Testing:**
- Metric: Percentage of required tests completed on time
- Target: 100%
- Measurement: Completed tests / Required tests (monthly self-tests, quarterly load tests)
- Audit evidence: UPS test logs (past 12 months)

**Generator Testing:**
- Metric: Percentage of required tests completed on time
- Target: 100%
- Measurement: Completed tests / Required tests (monthly no-load, quarterly load, annual full load)
- Audit evidence: Generator test logs (past 12 months)

**ISP Failover Testing:**
- Metric: Percentage of required tests completed on time
- Target: 100%
- Measurement: Completed tests / Required tests (quarterly failover tests)
- Audit evidence: ISP failover test reports (past 12 months)

### 8.2 Audit Evidence

#### 8.2.1 Power Infrastructure Evidence

**UPS Documentation:**
- UPS specifications (capacity kVA/kW, runtime, battery type, redundancy configuration)
- UPS configuration documentation (load distribution, battery count, monitoring integration)
- UPS sizing calculation (load calculation, growth margin, runtime calculation)

**Generator Documentation (if applicable):**
- Generator specifications (capacity kW, fuel type, runtime at load)
- Generator sizing calculation (load calculation, safety factor)
- ATS configuration (transfer time, failover/failback settings)
- Fuel supply documentation (tank capacity, fuel delivery contract)

**Power Redundancy Architecture:**
- Single-line electrical diagram (utility → UPS → generator → protected load)
- Redundancy level documentation (N, N+1, 2N)

#### 8.2.2 HVAC Infrastructure Evidence

**HVAC System Documentation:**
- HVAC specifications (capacity tons/BTU, redundancy configuration)
- HVAC sizing calculation (cooling load calculation, overhead factor)
- HVAC redundancy architecture (N, N+1, 2N)

**Hot/Cold Aisle Design (if applicable):**
- Datacenter floor plan (rack layout, cold aisles, hot aisles, HVAC supply/return)
- Containment documentation (if containment implemented)

#### 8.2.3 Telecommunications Infrastructure Evidence

**ISP Configuration:**
- ISP contracts (bandwidth, SLA, MTTR)
- ISP diversity documentation (diverse carriers, diverse paths verification)
- Failover mechanism documentation (BGP configuration or manual failover procedure)

**Network Equipment:**
- Network diagram (routers, switches, firewalls, ISP connections)
- Power protection documentation (all network equipment on UPS)

#### 8.2.4 Operational Evidence

**UPS Monitoring Data:**
- UPS status logs (past 12 months)
- Battery health trends (monthly data, past 12 months)
- Power outage events (count, duration, cause)

**UPS Testing Records:**
- Monthly battery self-test logs (past 12 months)
- Quarterly load test logs (past 12 months)
- Annual professional inspection reports

**Generator Testing Records:**
- Monthly no-load test logs (past 12 months)
- Quarterly 50% load test logs (past 12 months)
- Annual 100% load test logs
- Generator maintenance logs (oil changes, fuel quality tests)

**HVAC Monitoring Data:**
- Temperature and humidity monitoring data (past 12 months)
- HVAC status logs (running/stopped, alarms)
- Temperature excursion reports (monthly, past 12 months)

**HVAC Maintenance Records:**
- Monthly filter replacement logs
- Quarterly coil cleaning logs
- Semi-annual professional inspection reports

**ISP Performance Data:**
- ISP SLA reports (monthly, past 12 months)
- Network monitoring data (uptime, latency, packet loss, past 12 months)

**ISP Failover Testing:**
- Quarterly failover test reports (past 12 months)
- Failover time measurements, connectivity verification

**Utility Incident Reports:**
- Power failure incident reports (past 12 months)
- HVAC failure incident reports (past 12 months)
- ISP outage incident reports (past 12 months)
- Root cause analysis for major incidents

### 8.3 Testing Requirements Summary

**Monthly Testing:**
- UPS battery self-test (all UPS)
- Generator no-load test (all generators)
- HVAC filter replacement/inspection
- Water detection sensor test (see POL-S3)

**Quarterly Testing:**
- UPS load test (runtime verification)
- Generator 50% load test
- ISP failover test (if dual ISP)
- HVAC coil cleaning

**Semi-Annual:**
- HVAC professional inspection

**Annual Testing:**
- UPS professional inspection
- Generator 100% full load test
- Generator professional inspection
- HVAC comprehensive professional inspection
- Backup cooling deployment drill (if portable HVAC)

---

## 9. Cloud and Colocation Considerations

### 9.1 Cloud Environments

**Utility Resilience is Cloud Provider Responsibility:**

For organizations operating 100% in cloud environments (AWS, Azure, GCP) with no on-premises datacenters or information processing facilities:

- **Control A.7.11 applicability:** Not Applicable (mark as "Not Applicable" in Statement of Applicability)
- **Rationale:** Cloud providers manage physical infrastructure including power, cooling, and network connectivity
- **Organization's responsibility:** Assess cloud provider utility resilience controls through supplier management (Control A.5.19-23)

**Supplier Assessment Approach:**

**Audit Report Review:**
- Obtain cloud provider SOC 2 Type II report (review physical and environmental protection controls section)
- Obtain cloud provider ISO 27001 certification (review utility resilience controls A.7.11)
- Verify utility resilience controls implemented:
  - Power: UPS, generators, N+1 or 2N redundancy
  - HVAC: Precision cooling, N+1 or 2N redundancy, continuous monitoring
  - Telecommunications: Multiple ISPs, diverse paths, redundant network architecture

**Cloud Provider SLAs:**
- Review cloud provider SLAs (uptime guarantees, typically 99.9-99.99% per service)
- Verify SLA covers utility-related outages (power, cooling, network)
- Monitor SLA compliance (monthly SLA reports from provider, service health dashboards)

**Datacenter Certifications:**
- Review cloud provider datacenter certifications:
  - Uptime Institute Tier III or Tier IV (fault-tolerant, 99.982-99.995% availability)
  - ISO 27001 certification (information security management)
  - SOC 2 Type II (security, availability, processing integrity)

**Office Utility Resilience:**
- Even cloud-only organizations typically have office premises
- Office utility resilience requirements:
  - UPS for network equipment, workstations (optional but recommended)
  - Generator (optional, risk-based decision - typically not required for offices)
  - ISP redundancy (optional for offices, recommended for critical functions like customer support)

### 9.2 Colocation Facilities

**Shared Responsibility Model:**

For organizations utilizing colocation datacenter facilities:

#### 9.2.1 Provider Responsibilities (Typical)

**Colocation Provider Manages:**
- Building power infrastructure (utility connections, transformers, switchgear)
- UPS systems (building-level, typically N+1 or 2N redundancy)
- Backup generators (building-level, 24-72 hours fuel capacity)
- HVAC systems (building-level cooling, N+1 or 2N redundancy)
- Network connectivity (carrier-neutral meet-me room, multiple ISP options)
- Utility monitoring (24/7 monitoring, BMS integration)

**Provider Evidence:**
- SOC 2 Type II report (physical and environmental protection, utility resilience)
- ISO 27001 certification (if available)
- Uptime Institute Tier Certification (Tier II, III, or IV)
- TIA-942 or EN 50600 compliance (if available)
- Utility SLA reports (power uptime, HVAC uptime, quarterly reports to customers)
- Generator test reports (monthly/quarterly/annual tests)

#### 9.2.2 Customer Responsibilities (Typical)

**[Organization] Manages:**
- Equipment-level UPS (optional, for network equipment requiring extended runtime beyond provider UPS)
- ISP circuit procurement (customer procures ISP service, provider provides meet-me room cross-connects)
- Equipment power consumption monitoring (customer monitors own equipment load)
- Utility capacity planning (customer ensures colocation space has adequate power/cooling for equipment)

**Customer Implementation:**
- Deploy equipment-level UPS (if needed for network equipment, typically 1-2 kVA capacity)
- Procure ISP circuits (dual ISP recommended for critical applications)
- Monitor equipment power consumption (via PDU monitoring, inline power meters)
- Coordinate with provider on capacity planning (notify provider before deploying high-density equipment)

#### 9.2.3 Responsibility Matrix Documentation

Maintain formal responsibility matrix in colocation contract:

| Utility Control | Provider | Customer |
|-----------------|----------|----------|
| Utility power (building) | ✅ | - |
| Building UPS | ✅ | - |
| Equipment-level UPS | - | ✅ (optional) |
| Backup generator (building) | ✅ | - |
| Generator testing | ✅ | - |
| Generator fuel supply | ✅ | - |
| Building HVAC | ✅ | - |
| Equipment power monitoring | - | ✅ |
| Network connectivity (meet-me room) | ✅ | - |
| ISP circuit procurement | - | ✅ |
| ISP redundancy configuration | - | ✅ |
| Utility monitoring (building) | ✅ | - |
| Utility incident response (building) | ✅ | - |
| Utility incident response (equipment) | - | ✅ |

#### 9.2.4 Verification and Audit

**Annual Provider Verification:**
- Request updated SOC 2 Type II report (annual)
- Review provider audit findings (verify no adverse utility resilience findings)
- Review provider utility SLA reports (power uptime, HVAC uptime, past 12 months)
- Verify datacenter certifications current (Uptime Institute Tier, TIA-942)
- Review provider generator test reports (verify monthly/quarterly/annual tests completed)

**Customer Audit Evidence:**
- Responsibility matrix (documented in colocation contract)
- Provider audit reports (SOC 2, ISO 27001)
- Provider datacenter certifications (Uptime Institute Tier, TIA-942, EN 50600)
- Provider utility SLA reports (past 12 months)
- Provider generator test reports (past 12 months, if available)
- Customer-implemented controls evidence:
  - Equipment-level UPS documentation (if implemented)
  - ISP contracts and SLA reports (customer-procured circuits)
  - Equipment power consumption monitoring data (if implemented)
- Annual provider verification documentation

**Power Capacity Verification:**
- Verify allocated power capacity (kW contracted vs. kW available)
- Monitor actual power consumption (ensure not exceeding contracted capacity)
- Plan for capacity increase (coordinate with provider before equipment additions)

---

## 10. Related Documents

**Framework Sections:**
- **ISMS-POL-A.7.4-5-11-S1:** Executive Summary, Control Alignment, Scope (framework foundation)
- **ISMS-POL-A.7.4-5-11-S2:** Physical Security Monitoring (A.7.4) - access control, CCTV, intrusion detection (integration with utility monitoring)
- **ISMS-POL-A.7.4-5-11-S3:** Environmental Protection (A.7.5) - fire detection/suppression, water detection, temperature/humidity monitoring (HVAC environmental aspects)
- **ISMS-POL-A.7.4-5-11-S5:** Assessment Methodology and Evidence Framework
- **ISMS-IMP-A.7.4-5-11-S3:** Utility Resilience Implementation (UPS, generator, HVAC, ISP deployment)
- **ISMS-IMP-A.7.4-5-11-S4:** Facilities Assessment (ongoing utility resilience monitoring)

**Related ISMS Policies:**
- **ISMS-POL-A.8.13-14-5.30:** Business Continuity and Disaster Recovery (utility failure as disaster scenario, backup/restore procedures)
- **ISMS-POL-A.8.6:** Capacity Management (utility capacity planning, power/cooling capacity)
- **ISMS-POL-A.5.24-27:** Incident Management (utility failure incident handling procedures)
- **ISMS-POL-A.5.19-23:** Information Security for Use of Cloud Services (cloud provider utility resilience assessment)

**External Standards:**
- **ISO/IEC 27001:2022:** Control A.7.11 - Supporting Utilities
- **ISO/IEC 27002:2022:** Detailed guidance for Control A.7.11
- **NIST SP 800-53 Rev 5:** Physical and Environmental Protection (PE) family (PE-9 Emergency Shutoff, PE-10 Emergency Power, PE-11 Emergency Power - Long Term, PE-12 Emergency Lighting, PE-13 Fire Protection, PE-14 Environmental Controls)
- **Uptime Institute Tier Standards:** Datacenter power and cooling redundancy classification (Tier I-IV)
- **TIA-942:** Telecommunications Infrastructure Standard for Data Centers (power distribution, cooling, redundancy)
- **EN 50600:** Data Centre Facilities and Infrastructures (European standard for power, cooling, redundancy)
- **ASHRAE TC 9.9:** Thermal Guidelines for Data Processing Environments (temperature and humidity guidelines)

---

**END OF ISMS-POL-A.7.4-5-11-S4**

---

**Document Approval Signatures:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Author | [Name] | | |
| Facilities Manager | [Name] | | |
| IT Operations Manager | [Name] | | |
| CISO | [Name] | | |

---

*"Utility resilience is not just having a UPS and a generator. It's systematic capacity planning, redundant power and cooling infrastructure, diverse telecommunications, continuous monitoring, and tested failover procedures—all designed to ensure information processing facilities remain operational during utility disruptions."*
