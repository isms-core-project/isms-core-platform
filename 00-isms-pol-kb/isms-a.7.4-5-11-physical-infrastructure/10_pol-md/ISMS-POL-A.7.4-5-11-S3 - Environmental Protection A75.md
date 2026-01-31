# ISMS-POL-A.7.4-5-11-S3: Environmental Protection (A.7.5)

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
| 1.0 | [Date] | Facilities Manager / CISO | Initial policy for environmental protection requirements |

**Review Schedule:** Annual review or upon significant environmental incidents, facility changes, or threat landscape updates  
**Next Review Date:** [Approval Date + 12 months]  
**Distribution:** CISO, Facilities Management, Security Operations, System Owners, Auditors

---

## Table of Contents

1. [Control Overview](#1-control-overview)
2. [Environmental Threat Risk Assessment](#2-environmental-threat-risk-assessment)
3. [Fire Detection and Suppression](#3-fire-detection-and-suppression)
4. [Flood and Water Damage Protection](#4-flood-and-water-damage-protection)
5. [Temperature and Humidity Control](#5-temperature-and-humidity-control)
6. [Structural Protection](#6-structural-protection)
7. [Physical Access Barriers](#7-physical-access-barriers)
8. [Environmental Protection Plan](#8-environmental-protection-plan)
9. [Measurable Requirements and Audit Verification](#9-measurable-requirements-and-audit-verification)
10. [Cloud and Colocation Considerations](#10-cloud-and-colocation-considerations)
11. [Related Documents](#11-related-documents)

---

## 1. Control Overview

### 1.1 ISO 27001:2022 Control A.7.5 Reference

**Control Text:** Protection against physical and environmental threats, such as natural disasters, malicious attack or accidents shall be designed and implemented.

**Purpose:** To prevent physical and environmental damage to information processing facilities and information assets.

**Scope of This Section:**
This policy section defines comprehensive requirements for protecting [Organization] facilities from environmental threats including:
- Environmental threat risk assessment (natural disasters, accidents, malicious acts)
- Fire detection and suppression (smoke detectors, sprinklers, gas suppression)
- Flood and water damage protection (sensors, drainage, equipment elevation)
- Temperature and humidity control (HVAC monitoring, environmental sensors)
- Structural protection (seismic, wind resistance, equipment anchoring)
- Physical access barriers (perimeter fencing, vehicle barriers, secure construction)
- Environmental protection plan (threat response procedures, equipment relocation)

### 1.2 Measurable Outcomes

Implementation of Control A.7.5 shall produce the following measurable outcomes:

**Environmental Risk Assessment:**
- Documented assessment of natural disaster risks (flood, earthquake, hurricane, tornado)
- Documented assessment of fire risks (electrical, equipment, external)
- Documented assessment of water damage risks (flooding, plumbing, roof leaks)
- Risk mitigation strategies documented and implemented
- Annual reassessment completed

**Fire Detection System:**
- Coverage: 100% of facility area with smoke/heat detectors
- Testing: Monthly detector tests, annual full system test
- Fire drill: Annual (critical facilities), biennial (standard facilities)

**Environmental Monitoring Data:**
- Temperature monitoring: Continuous (5-minute intervals)
- Humidity monitoring: Continuous (5-minute intervals)
- Temperature excursions: <5 per month (outside target range)
- Water detection: Sensors in all at-risk areas, alert on water detection

**Incident Reports:**
- Environmental incidents documented (fire, flood, temperature excursions)
- Response time documented
- Root cause analysis completed
- Corrective actions implemented

### 1.3 Facility Criticality and Control Requirements

Requirements vary by facility criticality tier (see POL-S1, Section 3.5):

**Tier 1 - Critical Facilities (Datacenters, Primary Server Rooms):**
- Fire suppression: Pre-action sprinklers or gas suppression (clean agent)
- Water detection: Mandatory in server rooms, under raised floors
- Temperature monitoring: Continuous, real-time alerting on excursions
- HVAC redundancy: N+1 minimum (see POL-S4)
- Structural protection: Equipment anchoring mandatory (seismic zones)

**Tier 2 - Standard Facilities (Offices, Branch Locations):**
- Fire suppression: Wet pipe sprinklers (standard)
- Water detection: Risk-based (below-grade facilities, near plumbing)
- Temperature monitoring: Business hours or threshold alerting
- HVAC redundancy: N configuration (no redundancy required)
- Structural protection: Building code compliance minimum

---

## 2. Environmental Threat Risk Assessment

### 2.1 Natural Disaster Risk Assessment

#### 2.1.1 Assessment Methodology

[Organization] SHALL conduct environmental threat risk assessment for each facility using the following methodology:

**Step 1: Threat Identification**
Identify potential natural disasters based on geographic location:
- Flood risk (floodplains, coastal areas, near rivers)
- Earthquake risk (seismic zones)
- Hurricane/typhoon risk (coastal zones, specific geographic regions)
- Tornado risk (tornado alley, specific geographic regions)
- Extreme temperature risk (heat waves, freezing temperatures)
- Wildfire risk (wildland-urban interface zones)
- Heavy snow/ice risk (northern climates)

**Step 2: Likelihood Assessment**
Assess likelihood of each threat occurring within next 12 months:
- **High:** >50% probability (e.g., annual flooding in floodplain)
- **Medium:** 10-50% probability (e.g., moderate earthquake in seismic zone)
- **Low:** <10% probability (e.g., rare tornado in low-risk area)

**Data Sources:**
- Historical disaster data (past 50 years in region)
- Government hazard maps (FEMA flood maps, USGS seismic maps, NOAA hurricane maps)
- Insurance actuarial data
- Local emergency management agency reports

**Step 3: Impact Assessment**
Assess potential impact if threat occurs:
- **High Impact:** Facility destroyed or uninhabitable for >1 month, data loss, injury/fatality risk
- **Medium Impact:** Facility damaged, 1-7 days downtime, equipment damage but data intact
- **Low Impact:** Minor damage, <1 day downtime, no equipment damage

**Step 4: Risk Rating**
Combine likelihood and impact to determine risk rating:

| Likelihood / Impact | Low Impact | Medium Impact | High Impact |
|---------------------|------------|---------------|-------------|
| High Likelihood | Medium Risk | High Risk | Critical Risk |
| Medium Likelihood | Low Risk | Medium Risk | High Risk |
| Low Likelihood | Low Risk | Low Risk | Medium Risk |

**Step 5: Risk Treatment**
For each identified risk, select treatment strategy:
- **Critical/High Risk:** Mitigate (implement controls to reduce likelihood or impact)
- **Medium Risk:** Mitigate or transfer (insurance coverage)
- **Low Risk:** Accept or monitor (document acceptance, monitor threat landscape)

#### 2.1.2 Flood Risk Assessment

**Flood Zone Determination:**
- Consult FEMA flood maps (US) or equivalent (international)
- Flood zones:
  - **High Risk (Zone A, AE, AO, AH):** 1% annual chance of flooding ("100-year floodplain")
  - **Moderate Risk (Zone B, X-shaded):** 0.2-1% annual chance
  - **Low Risk (Zone C, X-unshaded):** <0.2% annual chance

**Flood Risk Factors:**
- Proximity to rivers, lakes, oceans (coastal flooding, riverine flooding)
- Below-grade facilities (basement datacenters, ground-floor in flood zones)
- Storm surge risk (coastal facilities during hurricanes)
- Urban flooding (inadequate drainage, combined sewer systems)

**Mitigation Strategies:**
- Equipment elevation (raised floors, equipment racks 15-30 cm off floor minimum)
- Flood barriers (sandbags, temporary flood walls, permanent flood gates)
- Drainage systems (sump pumps, floor drains, backwater valves)
- Waterproofing (walls, floors, foundation in below-grade facilities)
- Relocation (move critical equipment to upper floors in high-risk facilities)

#### 2.1.3 Earthquake Risk Assessment

**Seismic Zone Determination:**
- Consult USGS seismic hazard maps (US) or equivalent (international)
- Seismic zones (US):
  - **Zone 4 (Highest):** California fault zones, Alaska
  - **Zone 3 (High):** Parts of Pacific Northwest, Central US (New Madrid)
  - **Zone 2 (Moderate):** Parts of Eastern US
  - **Zone 1-0 (Low):** Most of Central/Eastern US

**Earthquake Risk Factors:**
- Proximity to fault lines (active faults, fault rupture zones)
- Soil liquefaction risk (saturated loose soils)
- Building age and construction (older unreinforced masonry at higher risk)
- Equipment mounting (unanchored equipment can topple)

**Mitigation Strategies:**
- Seismic-resistant building design (seismic bracing, flexible connections)
- Equipment anchoring (bolt server racks to floor, seismic mounts for equipment)
- Flexible utility connections (allow for building movement)
- Post-earthquake inspection procedures (structural damage assessment)
- Seismic-rated equipment mounting (certified seismic brackets and rails)

#### 2.1.4 Hurricane/Typhoon Risk Assessment

**Hurricane Risk Determination:**
- Consult NOAA hurricane risk maps (US) or equivalent (international)
- Hurricane-prone regions:
  - **Atlantic Coast:** Florida, Gulf Coast, East Coast up to New England
  - **Pacific Coast:** Hawaii, Western Pacific territories
  - **Asia-Pacific:** Philippines, Japan, Taiwan, Southeast Asia

**Hurricane Risk Factors:**
- Coastal exposure (storm surge, high winds)
- Building wind resistance (design wind speed rating)
- Roof vulnerability (aging roofs, flat roofs)
- Window vulnerability (large windows, non-impact-resistant glass)
- Power outage duration (prolonged outages common after hurricanes)

**Mitigation Strategies:**
- Hurricane-rated building design (design wind speed 150+ mph in high-risk zones)
- Window protection (impact-resistant glass, hurricane shutters)
- Roof reinforcement (hurricane straps, proper fastening)
- Generator fuel supply (7-14 days for prolonged outages)
- Emergency generator pre-season testing (test before hurricane season starts)

#### 2.1.5 Assessment Frequency and Documentation

**Initial Assessment:**
- Conducted before facility occupancy (new facilities)
- Conducted within 6 months (existing facilities without prior assessment)

**Annual Reassessment:**
- Review threat landscape (any new hazards, changed risk ratings)
- Review mitigation effectiveness (were implemented controls effective)
- Update risk register (document changes)

**Triggered Reassessment:**
- After major environmental incident (actual occurrence of assessed threat)
- After facility changes (major renovations, equipment additions)
- After regulatory changes (new building codes, new hazard maps)

**Documentation:**
- Environmental Threat Risk Assessment Report (per facility)
- Risk register (all identified risks, ratings, mitigation strategies)
- Mitigation implementation plan (for high/critical risks)
- Annual reassessment records

### 2.2 Fire Risk Assessment

#### 2.2.1 Fire Risk Factors

**Electrical Fire Risk:**
- Aging electrical systems (>20 years old)
- Overloaded circuits (insufficient capacity for equipment load)
- Poor electrical maintenance (no regular inspections)
- Improper wiring (extension cords as permanent wiring, overloaded outlets)

**Equipment Overheating Risk:**
- Server room inadequate cooling (HVAC failure, insufficient capacity)
- Dust accumulation (poor airflow, infrequent cleaning)
- Equipment age (aging equipment more prone to overheating)
- High-density equipment (blade servers, high-wattage GPUs)

**External Fire Risk:**
- Nearby buildings (fire spread from adjacent buildings)
- Wildfire zones (wildland-urban interface)
- Storage of flammable materials (nearby fuel storage, chemical storage)

**Human Factors:**
- Smoking (if allowed near facilities)
- Kitchen/break room (cooking fires)
- Arson risk (disgruntled employees, external threats)

#### 2.2.2 Fire Risk Mitigation

**Electrical Safety:**
- Electrical inspection: Annual by licensed electrician
- Circuit capacity assessment: Verify capacity sufficient for equipment load
- No extension cords as permanent wiring (use properly installed outlets)
- Arc-fault circuit interrupters (AFCI) in electrical panels

**Equipment Cooling:**
- Adequate HVAC capacity (see POL-S4, Section 3)
- Regular equipment cleaning (dust removal, air filter replacement)
- Temperature monitoring (see Section 5)

**Flammable Material Management:**
- No storage of flammable materials in server rooms or datacenters
- Flammable material storage: Approved flammable cabinets, separate room

**Fire Safety Training:**
- Annual fire safety training for all employees
- Fire extinguisher training (hands-on training for designated personnel)

### 2.3 Water Damage Risk Assessment

#### 2.3.1 Water Damage Risk Factors

**External Flooding:**
- Flood risk (see Section 2.1.2)
- Storm water drainage (inadequate drainage, clogged drains)
- Groundwater seepage (below-grade facilities, high water table)

**Roof Leaks:**
- Roof age (>15 years, aging roofs more prone to leaks)
- Flat roofs (water pooling, membrane damage)
- Roof penetrations (HVAC units, skylights - leak points)
- Poor roof maintenance (no regular inspections)

**Plumbing Failures:**
- Aging plumbing (>30 years, galvanized steel pipes prone to corrosion)
- Freezing pipes (northern climates, inadequate heating)
- Plumbing above critical equipment (water pipes above server racks)
- No regular plumbing inspections

**HVAC Condensate:**
- HVAC condensate drainage (clogged drains, inadequate drainage)
- Condensate pan overflow (cracked pans, no overflow sensors)

#### 2.3.2 Water Damage Mitigation

**External Flooding:**
- Flood barriers (see Section 2.1.2)
- Equipment elevation (raised floors, equipment racks off floor)
- Drainage systems (sump pumps, floor drains)

**Roof Protection:**
- Annual roof inspection (professional roofer)
- Roof maintenance (repair leaks promptly, replace aging roofs)
- Roof drainage (clean gutters and downspouts, ensure proper drainage)

**Plumbing Protection:**
- Plumbing inspection: Every 3-5 years (pressure test, leak detection)
- Avoid plumbing above critical equipment (reroute pipes if feasible)
- Pipe insulation (prevent freezing in northern climates)

**HVAC Condensate Management:**
- Condensate drain cleaning (annual)
- Condensate pan inspection (annual, replace cracked pans)
- Overflow sensors (detect condensate pan overflow)

---

## 3. Fire Detection and Suppression

### 3.1 Fire Detection System Requirements

#### 3.1.1 Smoke Detector Coverage

[Organization] SHALL install smoke detectors with the following coverage:

**Coverage Requirements:**
- **All Facilities:** 100% coverage of all interior spaces
- Detector spacing: One detector per 50-100 square meters (per local fire code)
- Detector placement: Ceiling-mounted (heat rises), avoid corners (dead air space)
- Special coverage: High ceilings (use beam detectors or aspirating systems), air returns (detect smoke before diluted)

**Smoke Detector Types:**
- **Photoelectric detectors:** Detect smoldering fires (preferred for most applications)
- **Ionization detectors:** Detect fast-burning fires (less common, more false alarms)
- **Dual-sensor detectors:** Both photoelectric and ionization (best coverage)
- **Aspirating smoke detection (ASD):** High-sensitivity for datacenters (very early detection)

**Smoke Detector Placement by Area:**
- **Server rooms / datacenters:** Ceiling-level + under raised floor + in air returns
- **Office areas:** Ceiling-level (hallways, rooms, conference rooms)
- **Storage rooms:** Ceiling-level
- **Electrical rooms:** Ceiling-level
- **HVAC mechanical rooms:** Ceiling-level

#### 3.1.2 Heat Detector Coverage

**Heat Detector Use Cases:**
- Areas where smoke detectors would cause false alarms (kitchens, garages, dusty areas)
- Supplement to smoke detectors (not replacement)

**Heat Detector Types:**
- **Fixed temperature:** Trigger at specific temperature (typically 57-68°C / 135-155°F)
- **Rate-of-rise:** Trigger if temperature increases rapidly (typically 6-8°C per minute)

**Heat Detector Placement:**
- Kitchens and break rooms (replace or supplement smoke detectors)
- Parking garages (vehicle exhaust causes smoke detector false alarms)

#### 3.1.3 Fire Alarm System

**Fire Alarm Panel:**
- Centralized fire alarm control panel (FACP)
- Type: Addressable (each detector has unique ID, preferred) or conventional (detectors grouped by zone)
- Power: Primary (AC mains) + backup (battery, 24-hour minimum)
- Monitoring: 24/7 monitoring (see Section 3.1.5)

**Fire Alarm Notification:**
- Audible alarms (horns, bells - minimum 75 dBA at all locations)
- Visual alarms (strobes - ADA compliance for hearing impaired)
- Alarm duration: Until manually reset (after fire department clearance)

**Fire Alarm Zones:**
- Zones defined by area or floor (facilitate emergency responder navigation)
- Critical facilities: Individual zones for server rooms, electrical rooms, telecom closets
- Standard facilities: Zones by floor or building wing

#### 3.1.4 Fire Detection Integration

**Integration with Building Management System (BMS):**
- Fire alarm status visible in BMS dashboard
- Automatic HVAC shutdown on fire alarm (prevent smoke spread)
- Automatic door unlock (facilitate evacuation)

**Integration with Physical Security (see POL-S2):**
- Fire alarm events forwarded to Security Operations Center (SOC)
- CCTV review during fire alarm (verify not false alarm, assess situation)
- Access control override (unlock all doors for evacuation)

#### 3.1.5 Fire Alarm Monitoring

**24/7 Monitoring (Critical Facilities - Tier 1):**
- Fire alarm signals transmitted to monitoring center (UL-listed central station)
- Monitoring center notifies fire department (automatic dispatch)
- Monitoring center notifies facilities manager (immediate notification)

**Business Hours Monitoring (Standard Facilities - Tier 2):**
- Fire alarm audible/visual alerts on-site (occupants call fire department)
- After-hours: Fire alarm transmitted to monitoring center (as above)

**Fire Alarm Testing:**
- **Monthly:** Alarm panel functionality test (press test button, verify notification)
- **Semi-annual:** Smoke detector test (smoke detector test aerosol spray)
- **Annual:** Full system test (professional fire alarm company, notify monitoring center, test all detectors and notification devices)

### 3.2 Fire Suppression System Requirements

#### 3.2.1 Sprinkler System Types

**Wet Pipe Sprinklers (Standard Facilities):**
- Most common type (water-filled pipes at all times)
- Sprinkler head activation: Individual heads activate when heated (fusible link melts at 57-77°C)
- Water discharge: Immediate upon sprinkler head activation
- Pros: Simple, reliable, lowest cost
- Cons: Water damage risk to equipment, freezing risk in cold climates

**Dry Pipe Sprinklers (Cold Environments):**
- Pipes filled with pressurized air/nitrogen (no water in pipes)
- Sprinkler head activation triggers valve to release water into pipes
- Water discharge: Slight delay (pipes fill with water first, typically 30-60 seconds)
- Use case: Unheated areas (parking garages, loading docks in cold climates)

**Pre-Action Sprinklers (Datacenters - Preferred):**
- Pipes empty (no water) until fire detected
- Activation: Two-stage (1: Fire detector triggers valve to fill pipes, 2: Sprinkler head heat activates water discharge)
- Water discharge: Delay allows for false alarm verification, manual abort
- Pros: Reduced water damage risk (time to abort false alarms)
- Cons: More complex, higher cost
- Use case: Datacenters, server rooms, valuable equipment areas

**Deluge Sprinklers (High-Hazard Areas):**
- All sprinkler heads open (no fusible links)
- Activation: Fire detector triggers valve, all heads discharge simultaneously
- Water discharge: Immediate and massive (entire area flooded)
- Use case: Rare in datacenters (chemical storage, flammable liquid storage only)

#### 3.2.2 Gas Suppression Systems (Datacenters)

**Gas Suppression (Clean Agent Systems):**
- Use: Datacenters, server rooms (alternative to sprinklers)
- Mechanism: Fire suppression through oxygen displacement or heat absorption, no water damage
- Agent types:
  - **FM-200 (HFC-227ea):** Most common, fast suppression (10 seconds), safe for occupied spaces
  - **Novec 1230:** Environmentally friendly (low global warming potential), safe for occupied spaces
  - **Inergen (IG-541):** Nitrogen/argon/CO2 blend, safe for occupied spaces, no residue
- Activation: Automatic (fire detection) with manual abort capability

**Pre-Discharge Warning:**
- Audio/visual alarm: 30-60 seconds before gas discharge (allow evacuation)
- Manual abort: Abort button allows personnel to verify fire before discharge (reduce false alarms)
- Evacuation: All personnel must evacuate before gas discharge (even though agents are safe in designed concentrations, oxygen levels will drop)

**Gas Suppression Testing:**
- **Monthly:** Control panel functionality test
- **Semi-annual:** Fire detection system test (triggers pre-discharge alarm, do not discharge gas)
- **Annual:** Full functional test by certified technician (no agent discharge, verify all components)
- **Every 5 years:** Agent concentration test (verify agent quantity sufficient for room volume)

#### 3.2.3 Fire Extinguishers

**Fire Extinguisher Types:**
- **ABC (Multi-Purpose Dry Chemical):** Most common, suitable for most fires (wood, paper, electrical, flammable liquids)
- **CO2 (Carbon Dioxide):** Electrical fires, no residue (preferred for electrical rooms)
- **Class K (Wet Chemical):** Kitchen fires (cooking oils, grease)

**Fire Extinguisher Placement:**
- Spacing: One extinguisher per 15-20 meters of travel distance
- Placement: Visible, accessible, wall-mounted (standardized height)
- Areas: Hallways, exits, electrical rooms, server rooms, kitchens
- Size: Minimum 2.5 kg (5 lb) for ABC, 5 kg (10 lb) recommended

**Fire Extinguisher Inspection:**
- **Monthly:** Visual inspection (pressure gauge in green, no physical damage, accessible)
- **Annual:** Professional inspection and servicing (licensed fire extinguisher company)
- Tag: Inspection tag attached to extinguisher (record monthly and annual inspections)

#### 3.2.4 Fire Suppression System Testing and Maintenance

**Sprinkler System Inspection:**
- **Quarterly:** Visual inspection (no obstructions, no damage, no leaks)
- **Annual:** Professional inspection (licensed sprinkler company, flow test, valve functionality)
- **Every 5 years:** Internal piping inspection (check for corrosion, sediment)

**Gas Suppression System Maintenance:**
- **Monthly:** Control panel test (see Section 3.2.2)
- **Semi-annual:** Detector test (see Section 3.2.2)
- **Annual:** Full functional test (see Section 3.2.2)
- **Every 5 years:** Agent refill/recharge (if agent leakage or concentration test failure)

### 3.3 Fire Drill and Emergency Evacuation

#### 3.3.1 Fire Drill Frequency

**Critical Facilities (Tier 1):**
- Frequency: Annual minimum (semi-annual recommended for 24/7 facilities)
- Drill shifts: All shifts participate (day shift, night shift if 24/7)

**Standard Facilities (Tier 2):**
- Frequency: Annual minimum
- Drill during business hours (when maximum occupants present)

#### 3.3.2 Fire Drill Procedures

**Pre-Drill Planning:**
- Coordinate with fire department (notify them of drill, optional participation)
- Notify occupants (advance notice, typically 1 week, unless surprise drill desired)
- Identify drill observers (record attendance, timing, issues)

**Drill Execution:**
- Trigger fire alarm (manually activate pull station)
- Evacuation:
  1. Occupants hear alarm (audible and visual alerts)
  2. Occupants evacuate via nearest exit (do not use elevators)
  3. Occupants proceed to assembly point (pre-designated outdoor location)
  4. Floor wardens verify all occupants evacuated (check offices, restrooms)
- Assembly point:
  - Headcount (verify all occupants present)
  - Missing persons protocol (notify fire department or drill coordinator)
- All-clear signal: Return to building after drill complete

**Drill Duration:**
- Target: Full building evacuation within 5 minutes (for office buildings)
- Datacenters: May have staged evacuation (non-essential personnel first, essential personnel remain until systems shut down)

#### 3.3.3 Emergency Evacuation Plan

**Evacuation Route Maps:**
- Posted in all areas (hallways, rooms, elevators)
- Show current location, evacuation routes (primary and secondary), assembly points
- Updated annually (or after facility changes)

**Assembly Points:**
- Location: Outside building, minimum 50 meters from structure (safe distance from fire, smoke, structural collapse)
- Capacity: Sufficient space for all occupants
- Weather protection: Identify alternative indoor location (if available, for extended evacuations in bad weather)

**Emergency Contacts:**
- Fire department (9-1-1 in US, local emergency number)
- Facilities manager (mobile phone)
- Building management (if leased space)
- Executive management (for major incidents)

**Persons with Disabilities:**
- Evacuation assistance plan (identify individuals requiring assistance)
- Evacuation chairs (for multi-story buildings without elevator access during fire)
- Area of refuge (fire-rated stairwell landing for persons awaiting assistance)

#### 3.3.4 Fire Drill Documentation

**Drill Report Contents:**
- Date and time of drill
- Building/facility
- Participants (headcount, departments represented)
- Drill duration (alarm to full evacuation)
- Issues identified (obstructed exits, confusion, delayed evacuation)
- Corrective actions (address identified issues)

**Drill Report Distribution:**
- Facilities manager (review and approve)
- CISO (awareness of security implications)
- Management (awareness of life safety preparedness)

**Drill Records Retention:**
- Retain drill reports for 5 years (demonstrate annual drill compliance)

---

## 4. Flood and Water Damage Protection

### 4.1 Flood Risk Mitigation

#### 4.1.1 Equipment Elevation

**Raised Floors (Datacenters):**
- Raised floor height: 30-60 cm (12-24 inches) typical
- Benefits: Equipment cables run under floor, airflow for cooling, elevation above floor-level water
- Construction: Modular floor tiles on pedestals (removable for access to underfloor space)

**Equipment Rack Elevation:**
- Even with raised floors, equipment racks should be elevated off floor surface
- Elevation method: Rack feet with adjustable height, seismic-rated base
- Minimum elevation: 15 cm (6 inches) above finished floor

**Non-Datacenter Equipment:**
- Equipment in flood-prone areas (basements, ground floor in flood zones): Place on elevated platforms or shelves (minimum 30 cm / 12 inches above floor)

#### 4.1.2 Flood Barriers

**Permanent Flood Barriers:**
- Use case: Facilities in high-risk flood zones (Zone A, AE)
- Types: Flood gates for doors, flood walls around building perimeter
- Installation: Professional installation, engineered for flood depth

**Temporary Flood Barriers:**
- Sandbags: Traditional method, labor-intensive
- Inflatable flood barriers: Quick deployment, less labor
- Storage: Pre-positioned near facilities in flood zones (ready for deployment)

**Deployment Plan:**
- Trigger: Flood warning issued (typically 24-48 hours notice for riverine flooding)
- Deployment team: Facilities staff trained on barrier deployment
- Deployment time: Target 4-8 hours for full perimeter protection

#### 4.1.3 Drainage Systems

**Floor Drains:**
- Floor drains in all below-grade facilities (basements, ground floor in flood zones)
- Drain capacity: Sized for expected water intrusion
- Backwater valves: Prevent sewage backup (urban areas with combined sewer systems)

**Sump Pumps:**
- Sump pit: Lowest point in below-grade facility (collect water)
- Sump pump: Automatically activate when water level reaches threshold
- Discharge: Pump water to exterior (sanitary sewer or storm drain per local code)
- Backup: Battery backup sump pump (operate during power outage)
- Testing: Monthly test (pour water in sump pit, verify pump activates)

#### 4.1.4 Waterproofing

**Below-Grade Facility Waterproofing:**
- Exterior waterproofing: Foundation walls coated with waterproof membrane (during construction)
- Interior waterproofing: Walls and floors sealed with waterproof coating (retrofit option)
- Drainage: French drains around foundation perimeter (exterior drainage)

**Waterproofing Inspection:**
- Annual inspection: Check for cracks, leaks, water stains (signs of water intrusion)
- Repairs: Promptly repair any identified waterproofing failures

### 4.2 Water Detection Systems

#### 4.2.1 Water Detection Sensor Types

**Spot Detectors:**
- Type: Individual sensors placed at specific locations (floor level)
- Detection: Conductive probes detect water presence
- Use case: Point-based detection (under HVAC units, near sump pumps, under raised floors)

**Cable Sensors:**
- Type: Sensing cable (entire length detects water)
- Detection: Conductive cable or optical fiber detects water along its length
- Use case: Continuous detection (along walls, under raised floors in datacenters)
- Advantage: Detects water anywhere along cable (no blind spots)

#### 4.2.2 Water Detection Sensor Placement

**Mandatory Placement:**
- Server rooms: Under raised floors (if raised floor), at floor level (if slab floor)
- Under HVAC units (condensate pan overflow, refrigerant leaks)
- Below-grade facilities: Floor level in all areas
- Near sump pumps (detect pump failure or overflow)
- Under water pipes (if pipes above or near critical equipment)

**Sensor Spacing:**
- Spot detectors: One sensor per 4-9 square meters (based on risk level)
- Cable sensors: Run cable in grid pattern (1-2 meter spacing) under raised floors

#### 4.2.3 Water Detection Alerting

**Real-Time Alerts:**
- Notification: Email, SMS, phone call to facilities manager (immediate)
- Alert: Dashboard alert (integrate with BMS or physical security dashboard)
- Alarm: Audible alarm in affected area (if manned 24/7)

**Alert Response:**
- Response time target: 15 minutes (investigate and mitigate)
- Response actions:
  1. Identify water source (pipe leak, HVAC condensate, external flooding)
  2. Stop water source (shut off water valve, fix leak)
  3. Protect equipment (move equipment if water spreading, shut down equipment if necessary)
  4. Extract water (wet vacuum, mops, dehumidifiers)
  5. Document incident (water source, extent of damage, actions taken)

#### 4.2.4 Water Detection System Testing

**Monthly Testing:**
- Test all water sensors (pour small amount of water on sensor, verify alert)
- Document results (sensor ID, pass/fail, issues)

**Annual Testing:**
- Professional inspection (sensor cleaning, cable integrity check)
- Replace aging sensors (manufacturer recommended lifespan, typically 5-10 years)

### 4.3 Water Damage Response

#### 4.3.1 Immediate Response

**Stop Water Source:**
- Identify source: Plumbing leak, roof leak, flooding, HVAC condensate
- Shut off water: Water main valve, fixture valve (if plumbing leak)
- Fix leak: Temporary repair (plumber's tape, clamps), permanent repair (call plumber)

**Protect Equipment:**
- Move equipment (if water spreading and equipment movable)
- Shut down equipment (if water contact imminent, graceful shutdown preferred)
- Cover equipment (plastic sheeting if water from above)

**Extract Water:**
- Wet vacuum (immediate water extraction)
- Mops and towels (absorb remaining water)
- Fans and dehumidifiers (dry out affected area, prevent mold)

#### 4.3.2 Equipment Damage Assessment

**Do Not Power On Wet Equipment:**
- Water + electricity = damage and safety hazard
- Allow equipment to dry completely (24-72 hours, depending on extent of water contact)

**Damage Assessment:**
- Inspect equipment (signs of water contact, corrosion)
- Power on test (after drying, test equipment in non-production environment)
- Professional assessment (for expensive equipment, consider professional data recovery or repair evaluation)

**Equipment Replacement:**
- Document damaged equipment (serial numbers, replacement cost)
- Insurance claim (if insured, file claim promptly)
- Restore from backup (if data loss, restore from backup per POL-A.8.13)

#### 4.3.3 Mold Prevention

**Mold Growth Timeline:**
- Mold begins growing within 24-48 hours of water damage
- Prevention: Dry affected area within 24 hours

**Drying Methods:**
- Fans: Circulate air, accelerate evaporation
- Dehumidifiers: Remove moisture from air
- Heat: Increase temperature (accelerate evaporation, but avoid heat damage to equipment)

**Professional Restoration:**
- For significant water damage (flooding, large area affected): Call professional water damage restoration company
- Services: Water extraction, structural drying, mold remediation
- Timeline: Within 24-48 hours of water damage (prevent mold)

---

## 5. Temperature and Humidity Control

### 5.1 HVAC System Requirements (See Also POL-S4)

This section focuses on environmental monitoring aspects of HVAC. For HVAC capacity, redundancy, and utility resilience requirements, see POL-S4, Section 3.

#### 5.1.1 Target Temperature and Humidity Ranges

**Server Rooms / Datacenters:**
- **Temperature:** 18-27°C (64-80°F) recommended per ASHRAE TC 9.9
  - Optimal: 20-22°C (68-72°F) for energy efficiency
  - Allowable: 15-32°C (59-90°F) short-term (equipment rated range)
- **Humidity:** 40-60% RH (relative humidity) recommended
  - Allowable: 20-80% RH short-term
  - Avoid: <20% RH (static electricity risk), >80% RH (condensation risk)

**Office Areas:**
- **Temperature:** 20-24°C (68-75°F) for occupant comfort
- **Humidity:** 30-60% RH

#### 5.1.2 ASHRAE Guidelines

**ASHRAE TC 9.9 Classes (Data Centers):**
- **Class A1:** Tightly controlled (18-27°C, 5.5°C dew point to 60% RH and 15°C dew point)
- **Class A2:** Some control (10-35°C, wider humidity range)
- **Class A3/A4:** Minimal control (5-40°C/45°C, even wider humidity range)

Most datacenters target Class A1 or A2 (balance equipment longevity and energy efficiency).

### 5.2 Environmental Monitoring System

#### 5.2.1 Temperature and Humidity Sensors

**Sensor Placement:**
- **Server Rooms / Datacenters:** 
  - Minimum 2 sensors: Intake (cold aisle) and exhaust (hot aisle)
  - Large datacenters: 1 sensor per 50-100 square meters
  - Sensor height: Equipment intake level (not ceiling level)
- **Office Areas:** 1 sensor per zone (per thermostat typically)

**Sensor Types:**
- **Standalone IoT sensors:** Battery-powered or PoE-powered, wireless communication (Wi-Fi, LoRaWAN)
- **BMS-integrated sensors:** Wired to Building Management System
- **HVAC thermostat sensors:** Built-in to HVAC thermostats (limited visibility)

**Sensor Specifications:**
- **Accuracy:** ±0.5°C temperature, ±3% RH humidity
- **Refresh rate:** 5-minute intervals minimum (1-minute preferred for critical facilities)
- **Communication:** Real-time data transmission to monitoring platform

#### 5.2.2 Monitoring Platform

**Platform Options:**
- **Cloud-based:** Ubiquiti UniFi (sensors), Monnit (sensors), AWS IoT / Azure IoT (custom)
- **On-premises:** Zabbix, Nagios, PRTG (integrate with BMS or IoT sensors)
- **Building Management System (BMS):** If facility has existing BMS (Schneider Electric, Siemens, Johnson Controls)

**Platform Features:**
- Real-time dashboard (current temperature, humidity, historical trends)
- Alerting (threshold breaches, sensor offline)
- Data retention (12 months minimum raw data, 3 years aggregated)
- API access (integrate with SIEM, physical security dashboard)

#### 5.2.3 Alert Thresholds

**Temperature Alerts:**
- **Warning:** 28-30°C (hot) or 16-18°C (cold) - Investigate within 1 hour
- **Critical:** >30°C (hot) or <15°C (cold) - Immediate response
- **Prolonged:** Temperature outside target range for >1 hour - Escalate to facilities manager

**Humidity Alerts:**
- **Warning:** 25-30% RH (dry) or 65-70% RH (humid) - Investigate within 1 hour
- **Critical:** <20% RH (dry) or >80% RH (humid) - Immediate response

**Rate-of-Change Alerts:**
- Rapid temperature increase: >2°C per 10 minutes (indicates HVAC failure)
- Rapid humidity increase: >10% RH per 10 minutes (indicates water leak or HVAC failure)

#### 5.2.4 Monitoring Dashboard Integration

**Physical Security Dashboard (see POL-S2, Section 7.3):**
- Temperature/humidity status (current readings, alert status)
- Trend charts (hourly, daily, weekly)
- Excursion count (count of threshold breaches per month)

**SIEM Integration (see POL-S2, Section 7.1):**
- Environmental alerts forwarded to SIEM
- Correlation with utility alerts (HVAC failure + temperature rise)

### 5.3 Temperature and Humidity Excursion Response

#### 5.3.1 Minor Excursion Response (Warning Threshold)

**Actions:**
- Investigate cause (HVAC performance degradation, external temperature, equipment load increase)
- Adjust HVAC set point (if needed, temporary adjustment)
- Monitor trend (verify temperature returning to target range)
- Document excursion (date, time, duration, cause, resolution)

**Resolution Timeline:**
- Target: Return to normal within 2 hours

#### 5.3.2 Major Excursion Response (Critical Threshold)

**Immediate Actions:**
- Notify facilities manager (immediate, phone call)
- Investigate HVAC status (is HVAC running, any alarms)
- Reduce IT load (shutdown non-critical systems to reduce heat generation)
- Deploy backup cooling (portable HVAC units if available, see POL-S4, Section 3.5)

**If Temperature Continues Rising (>35°C):**
- Graceful shutdown (shutdown equipment to prevent heat damage)
- Notify stakeholders (management, IT operations, business units)
- Activate incident response (major incident, potential data center outage)

**Resolution Timeline:**
- Target: Resolve HVAC issue within 4 hours (before temperature reaches critical levels)

#### 5.3.3 Prolonged Excursion Response (>1 Hour Outside Target)

**Actions:**
- Escalate to facilities manager (if not already notified)
- Engage HVAC vendor (emergency service call if internal resolution unsuccessful)
- Notify management (awareness of prolonged environmental issue)
- Document prolonged excursion (incident report, root cause analysis)

**Post-Incident Review:**
- Root cause analysis (why did excursion occur, why was it prolonged)
- Corrective actions (prevent recurrence: HVAC maintenance, capacity increase, backup cooling)
- Testing: Test corrective actions (verify effectiveness)

### 5.4 Environmental Monitoring Testing

**Monthly Testing:**
- Verify sensor accuracy (compare to handheld thermometer/hygrometer)
- Verify alerting (manually trigger threshold breach, verify alert received)
- Document results (sensor ID, accuracy, alert test results)

**Quarterly Testing:**
- Sensor calibration check (compare all sensors to reference instrument)
- Replace sensors with significant drift (>1°C temperature, >5% RH humidity)

**Annual Testing:**
- Professional sensor calibration (if critical facility)
- Platform health check (verify data retention, API integration)

---

## 6. Structural Protection

### 6.1 Building Structural Integrity

#### 6.1.1 Structural Inspection

**Initial Inspection (New Facilities):**
- Professional structural engineer inspection before facility occupancy
- Assessment: Building structural integrity, seismic/wind resistance, foundation condition

**Periodic Inspection (Existing Facilities):**
- Frequency: Every 5 years minimum (every 3 years for aging buildings >30 years old)
- Professional: Licensed structural engineer
- Assessment: Cracks (walls, foundation), settlement (foundation movement), corrosion (steel structures), water damage (concrete spalling)

**Post-Event Inspection:**
- After earthquake (any magnitude felt at facility): Immediate inspection
- After hurricane/tornado: Inspection within 24 hours
- After significant water damage: Structural damage assessment

#### 6.1.2 Seismic Protection (Earthquake Zones)

**Building Seismic Design:**
- For new facilities in seismic zones (Zone 3-4): Seismic-resistant design per local building code
- Seismic bracing: Structural elements designed to withstand lateral forces
- Flexible connections: Utility connections allow for building movement (prevent rupture)

**Seismic Retrofit (Existing Facilities in Seismic Zones):**
- Assessment: Structural engineer evaluation of seismic vulnerability
- Retrofit measures: Foundation bolting, cripple wall bracing, soft-story strengthening
- Priority: Critical facilities in high-risk zones (Zone 4)

#### 6.1.3 Wind Resistance (Hurricane Zones)

**Building Wind Design:**
- For new facilities in hurricane zones: Design wind speed per local building code (typically 120-180 mph design wind speed)
- Roof structure: Hurricane straps (roof-to-wall connections), proper fastening
- Window protection: Impact-resistant glass or hurricane shutters

**Wind Retrofit (Existing Facilities in Hurricane Zones):**
- Assessment: Structural engineer evaluation of wind vulnerability
- Retrofit measures: Roof reinforcement, window protection, door bracing
- Priority: Critical facilities on coast or in high-wind zones

### 6.2 Equipment Anchoring and Racking

#### 6.2.1 Server Rack Anchoring

**Seismic Zones (Zone 2-4):**
- All server racks SHALL be bolted to floor (no free-standing racks)
- Bolt type: Expansion bolts or epoxy-set bolts into concrete slab
- Bolt spacing: Per rack manufacturer specifications (typically 4 bolts per rack, one at each corner)

**Non-Seismic Zones (Zone 0-1):**
- Free-standing racks acceptable (but anchoring recommended for tall/heavy racks)
- Anti-tip brackets recommended (prevent forward tip)

**Seismic Rack Certification:**
- For critical facilities in high-risk zones: Use seismic-rated racks (tested per GR-63-CORE or similar)
- Seismic rating: Withstand specific seismic zone acceleration (Zone 4: 2.0g typical)

#### 6.2.2 Equipment Mounting

**Rack-Mounted Equipment:**
- Secure mounting: All equipment properly mounted in rack (rack ears bolted to rack rails)
- Cable management: Cables secured (prevent strain on connections during shaking)
- Weight distribution: Heavier equipment at bottom of rack (lower center of gravity)

**Non-Rack Equipment:**
- Equipment >20 kg: Secure to floor or table (seismic mounts, anti-tip brackets)
- Equipment on shelves: Lip on shelf edge (prevent sliding), secure to shelf (straps, velcro)

#### 6.2.3 HVAC and UPS Anchoring

**Anchoring Requirements:**
- HVAC units (rooftop, floor-mounted): Bolted to structure or floor
- UPS systems (floor-standing): Bolted to floor (per manufacturer specifications)
- Large batteries (UPS, generator): Battery racks bolted to floor

**Seismic Isolators:**
- For sensitive equipment: Seismic isolators (vibration isolation + seismic restraint)
- Use case: High-performance computing, sensitive lab equipment

### 6.3 Structural Monitoring

#### 6.3.1 Crack Detection and Monitoring

**Visual Inspection:**
- Frequency: Semi-annual (during facility inspection)
- Areas: Foundation walls, structural walls, floors, ceilings
- Documentation: Photograph cracks (measure width, length), document location

**Crack Width Measurement:**
- Hairline cracks (<1 mm): Monitor, typically non-structural
- Minor cracks (1-5 mm): Monitor, investigate cause if growing
- Major cracks (>5 mm): Immediate structural engineer assessment

**Crack Monitoring:**
- For active cracks (growing): Install crack monitors (document crack movement over time)
- Frequency: Quarterly measurement

#### 6.3.2 Settlement Monitoring

**Foundation Settlement:**
- Visual signs: Cracks in walls, doors/windows not closing properly, sloped floors
- Measurement: Surveying (benchmark elevations, monitor settlement over time)
- Frequency: Every 3-5 years (or if visual signs observed)

**Excessive Settlement:**
- Differential settlement >1 inch: Structural engineer assessment
- Mitigation: Foundation underpinning (if settlement ongoing)

#### 6.3.3 Post-Earthquake Inspection

**Immediate Visual Inspection (After Any Felt Earthquake):**
- Inspect for cracks (walls, foundation), fallen objects, damaged equipment
- Document damage (photographs, written description)
- Do not re-occupy facility if major structural damage observed (unsafe)

**Professional Inspection (After Moderate/Major Earthquake):**
- Structural engineer inspection (verify structural integrity)
- Equipment inspection (verify anchoring intact, no equipment damage)
- Clearance required before re-occupancy (if major damage)

---

## 7. Physical Access Barriers

This section addresses physical barriers for environmental protection (perimeter security, secure construction). For access control monitoring, see POL-S2, Section 2-3.

### 7.1 Perimeter Protection

#### 7.1.1 Perimeter Fencing

**Fencing Requirements (Critical Facilities - Tier 1):**
- Fence height: 2-3 meters (6.5-10 feet)
- Fence type: Chain-link with barbed wire top (or anti-climb fence, architectural fence)
- Fence integrity: No gaps, no holes, maintained (no sagging, rust)

**Fencing Requirements (Standard Facilities - Tier 2):**
- Fencing optional (risk-based decision)
- If implemented: Same standards as Tier 1

#### 7.1.2 Vehicle Barriers

**Bollards and Vehicle Barriers:**
- Use case: Prevent vehicle-borne attacks (ramming), prevent accidental vehicle impact
- Placement: Around building perimeter (especially near critical infrastructure: generators, fuel tanks, utility connections)
- Type: Fixed bollards (concrete-filled steel pipes), crash-rated bollards (K4, K8, K12 rated per ASTM F2656)

**Vehicle Gates:**
- Controlled entry points for vehicles (parking, loading docks)
- Gate control: Manual (guard-operated), automatic with access control (RFID, license plate recognition)
- Emergency access: Fire department access (knox box key override)

#### 7.1.3 Controlled Entry Points

**Pedestrian Access:**
- Limited entry points (reduce perimeter monitoring burden)
- Main entrance: Manned reception or access control
- Secondary entrances: Access control only (no public access)

**Delivery and Loading Docks:**
- Separate from pedestrian entrances (security screening)
- Access control: Verify delivery personnel identity, escort if accessing interior
- Hours: Limited hours (business hours only, scheduled deliveries)

### 7.2 Building Security

#### 7.2.1 Secure Construction

**Walls:**
- Exterior walls: Solid construction (concrete, masonry, steel stud with drywall)
- Fire rating: Per building code (typically 1-2 hour fire rating)
- Floor-to-ceiling: Walls extend to structural deck above (no gaps above ceiling tiles)

**Doors:**
- Exterior doors: Metal (steel, aluminum), solid core wood minimum
- Locking hardware: Deadbolts, access control (card readers, keypad)
- Fire-rated doors: Per building code (fire exits, electrical rooms)

**Windows:**
- Ground floor windows: Security considerations (see Section 7.2.2)
- Upper floor windows: Standard construction acceptable

#### 7.2.2 Window Security

**Ground Floor Windows:**
- Security bars: Optional (risk-based, balance security vs. aesthetics vs. emergency egress)
- Impact-resistant glass: Laminated glass or polycarbonate (resist break-in, also hurricane protection)
- Window locks: Ensure all windows have functioning locks
- Window sensors: Integrate with intrusion detection (see POL-S2, Section 3)

**Upper Floor Windows:**
- Standard windows acceptable (lower break-in risk)
- Hurricane zones: Impact-resistant glass or hurricane shutters (wind protection)

#### 7.2.3 Roof Access

**Roof Access Control:**
- Roof access doors: Locked, access control or key-only (prevent unauthorized access)
- Roof hatch: Locked from interior (prevent exterior entry)
- Alarm: Roof access door alarmed (detect unauthorized access, see POL-S2, Section 3)

**Roof Inspections:**
- Frequency: Annual (roof condition, access control verification)
- After storms: Inspect for damage (membrane damage, water pooling)

### 7.3 Server Room and Datacenter Protection

#### 7.3.1 Server Room Construction

**Walls:**
- Floor-to-ceiling construction (extend to structural deck, no gaps above ceiling tiles)
- Fire rating: 1-hour minimum (2-hour preferred for critical datacenters)
- Construction: Drywall on metal studs minimum (concrete block or poured concrete for high-security)

**Doors:**
- Metal doors (steel, fire-rated)
- Access control: Card reader, keypad, or biometric (see POL-S2, Section 2)
- Self-closing: Doors automatically close and lock (no propping open)

**Windows:**
- No windows preferred (security and environmental control)
- If windows required: Impact-resistant glass, internal blinds/shades (privacy)

#### 7.3.2 Raised Floors

**Raised Floor Construction:**
- Modular floor tiles on adjustable pedestals (typically 30-60 cm / 12-24 inches height)
- Load rating: Per equipment load (typically 680-1360 kg/m² / 140-280 lb/ft²)
- Grounding: Ensure proper grounding (prevent static electricity buildup)

**Underfloor Cable Management:**
- Cables routed under raised floor (power, data)
- Cable management: Secure cables (prevent tangling, allow airflow)
- Airflow: Ensure cables do not block airflow (hot aisle / cold aisle design)

---

## 8. Environmental Protection Plan

### 8.1 Threat Response Procedures

#### 8.1.1 Fire Response Procedure

**Upon Fire Alarm Activation:**
1. **Evacuate:** All personnel evacuate immediately (do not investigate, do not fight fire unless trained and safe)
2. **Call fire department:** Dial emergency number (9-1-1 in US, local emergency number)
3. **Account for personnel:** Assemble at designated assembly point, headcount
4. **Do not re-enter building** until fire department clears (safe to enter)

**For Server Rooms with Gas Suppression:**
- Pre-discharge warning: 30-60 seconds (evacuate immediately upon hearing alarm)
- Manual abort: If false alarm and personnel able to verify, abort discharge (only if absolutely certain)
- Post-discharge: Do not enter until ventilated (low oxygen levels even though agent is safe)

**Post-Fire Actions:**
- Damage assessment (once cleared by fire department)
- Equipment salvage (coordinate with insurance, professional restoration)
- Restore from backup (see POL-A.8.13 if data loss)
- Root cause analysis (prevent recurrence)

#### 8.1.2 Flood Response Procedure

**Upon Flood Warning (24-48 Hours Notice):**
1. **Deploy flood barriers:** Install temporary flood barriers (sandbags, inflatable barriers)
2. **Elevate equipment:** Move portable equipment to upper floors or elevate on platforms
3. **Backup data:** Verify backups current, export critical data to off-site location
4. **Prepare for power outage:** Test generator, ensure fuel supply (floods often cause power outages)
5. **Monitor situation:** Monitor flood forecasts, be prepared for evacuation or shutdown

**Upon Active Flooding (Water Entering Facility):**
1. **Evacuate personnel:** If water levels dangerous or rising rapidly
2. **Shut down equipment:** Graceful shutdown if time permits, emergency shutdown if water contact imminent
3. **Disconnect power:** Shut off main power (prevent electrical hazards)
4. **Document:** Photograph extent of flooding (insurance documentation)

**Post-Flood Actions:**
- Water extraction (professional water damage restoration)
- Equipment damage assessment (see Section 4.3.2)
- Mold remediation (if drying not completed within 24-48 hours)
- Restore operations (repair, restore from backup)

#### 8.1.3 Temperature Excursion Response Procedure

**Upon Critical Temperature Alert (>30°C):**
1. **Investigate HVAC:** Check HVAC status (is it running, any alarms)
2. **Reduce load:** Shutdown non-critical systems (reduce heat generation)
3. **Deploy backup cooling:** If available (portable HVAC units)
4. **Notify stakeholders:** Facilities manager, IT operations, management
5. **Monitor temperature:** Continuous monitoring (every 5 minutes)

**If Temperature Continues Rising (>35°C):**
1. **Graceful shutdown:** Shutdown all equipment (prevent heat damage)
2. **Evacuate personnel:** If temperature becoming dangerous for personnel (>40°C)
3. **Activate incident response:** Major incident, potential extended outage
4. **Engage vendor:** Emergency HVAC repair (if internal resolution unsuccessful)

**Post-Incident:**
- Root cause analysis (HVAC capacity insufficient, equipment failure, maintenance overdue)
- Corrective actions (HVAC repair, capacity increase, redundancy implementation)
- Testing (verify corrective actions effective)

#### 8.1.4 Earthquake Response Procedure

**During Earthquake:**
1. **Drop, cover, hold:** Personnel drop to ground, take cover under desk/table, hold on
2. **Do not evacuate during shaking:** Stay in place until shaking stops (falling debris hazard)
3. **Stay away from windows:** Glass can shatter during shaking

**After Earthquake (Shaking Stopped):**
1. **Evacuate building:** Orderly evacuation (aftershocks possible)
2. **Assemble at assembly point:** Headcount, account for all personnel
3. **Do not re-enter building** until cleared by professional (structural damage assessment)

**Facility Assessment (After Clearance to Re-Enter):**
1. **Visual inspection:** Check for cracks, fallen objects, damaged equipment
2. **Equipment inspection:** Verify equipment anchoring intact, no visible damage
3. **System tests:** Power on equipment (in non-production environment), test functionality
4. **Professional inspection:** Structural engineer assessment (if moderate/major earthquake)

#### 8.1.5 Hurricane Response Procedure

**72 Hours Before Hurricane Landfall:**
1. **Review plan:** Review hurricane preparedness plan, notify all personnel
2. **Test generator:** Run generator test (verify functionality)
3. **Fuel supply:** Top off generator fuel, arrange fuel delivery (if needed)
4. **Backup data:** Verify backups current, export critical data to off-site location

**24 Hours Before Hurricane Landfall:**
1. **Secure loose items:** Secure or bring indoor any loose outdoor items (patio furniture, signage)
2. **Window protection:** Install hurricane shutters or plywood (if not permanently installed)
3. **Facility shutdown decision:** Decide whether to maintain operations or shutdown (risk-based)

**During Hurricane:**
1. **Personnel evacuation:** Evacuate non-essential personnel (essential personnel remain if facility staffed)
2. **Monitor conditions:** Monitor generator operation, environmental conditions
3. **Stay indoors:** Do not go outside during hurricane (flying debris hazard)

**After Hurricane:**
1. **Damage assessment:** Once safe to inspect (winds <40 mph), assess damage
2. **Generator monitoring:** If on generator power, monitor fuel supply, plan for extended outage (3-7 days possible)
3. **Roof inspection:** Check for roof damage (leaks, membrane damage)
4. **Restoration:** Coordinate repairs, restore from backup if data loss

### 8.2 Equipment Relocation Plans

#### 8.2.1 Trigger Conditions for Equipment Relocation

**Relocation Triggers:**
- Imminent environmental threat (flood warning, hurricane evacuation order, wildfire evacuation order)
- Prolonged facility unavailability (fire, major structural damage, extended power outage)
- Planned facility closure (decommissioning, renovation)

**Decision Criteria:**
- Criticality of equipment (Tier 1 critical systems: relocate, Tier 2 standard systems: risk-based)
- Relocation time available (48+ hours: orderly relocation, <24 hours: emergency relocation of most critical only)
- Alternate location availability (prepared alternate facility, cloud migration, hot site)

#### 8.2.2 Relocation Destinations

**Prepared Alternate Facilities:**
- Disaster recovery site (if available, see POL-A.8.13-14-5.30)
- Secondary facility (if multi-site organization)
- Colocation facility (contract for emergency space)

**Cloud Migration:**
- Emergency cloud migration (if cloud infrastructure available, see POL-A.5.19-23)
- Workload migration (migrate VMs/containers to cloud)
- Advantages: Rapid deployment (hours), scalable

**Hot Site / Warm Site:**
- Commercial hot site (contract with disaster recovery provider)
- Advantages: Pre-configured, ready for immediate use
- Disadvantages: Expensive (monthly fees)

#### 8.2.3 Relocation Logistics

**Pre-Relocation:**
1. **Data backup verification:** Ensure all backups current before relocation
2. **Inventory:** Document equipment being relocated (serial numbers, configuration)
3. **Transportation arrangement:** Secure transport (bonded carrier if sensitive equipment)
4. **Insurance:** Verify insurance coverage during transport

**During Relocation:**
1. **Graceful shutdown:** Proper shutdown of all equipment
2. **Secure packing:** Pack equipment in original boxes (if available) or secure packaging
3. **Chain of custody:** Document who has custody during transport
4. **Transport monitoring:** Track shipment (GPS tracking if high-value)

**Post-Relocation:**
1. **Equipment inspection:** Inspect for transport damage
2. **Installation:** Install and configure equipment at alternate location
3. **Testing:** Test functionality before production use
4. **Restore operations:** Bring systems online, restore from backup if needed

### 8.3 Insurance Coverage

#### 8.3.1 Property Insurance

**Building and Contents Insurance:**
- Coverage: Building structure, equipment, inventory
- Coverage limits: Sufficient to replace all assets (regularly reassess as equipment added)
- Deductible: Balance premium cost vs. deductible (typical: $5,000-$25,000)

**Valuation Method:**
- Replacement cost: Insurer pays to replace with new (preferred)
- Actual cash value: Replacement cost minus depreciation (less favorable)

#### 8.3.2 Business Interruption Insurance

**Coverage:**
- Lost revenue during facility downtime (fire, flood, major equipment failure)
- Extra expenses (equipment rental, alternate facility costs)
- Coverage period: Sufficient to rebuild/relocate (typically 6-12 months)

**Calculation:**
- Based on financial records (revenue, expenses)
- Regularly update (as business grows)

#### 8.3.3 Flood Insurance

**Standard Property Insurance Exclusion:**
- Most property insurance EXCLUDES flood coverage
- Separate flood insurance required (NFIP in US, private flood insurance)

**Flood Insurance Requirement:**
- Mandatory for facilities in high-risk flood zones (Zone A, AE) with mortgage
- Strongly recommended even if not required (flood damage very expensive)

**Coverage Limits:**
- Building coverage: Up to $500,000 (NFIP) or higher (private insurance)
- Contents coverage: Up to $500,000 (NFIP) or higher (private insurance)

#### 8.3.4 Insurance Policy Review

**Annual Review:**
- Review coverage limits (ensure sufficient as assets grow)
- Review deductibles (adjust if risk tolerance changes)
- Review exclusions (understand what is not covered)
- Shop quotes (compare premiums from multiple insurers)

**Post-Incident:**
- File claim promptly (typically within 30-60 days)
- Document damage thoroughly (photographs, inventory, repair estimates)
- Cooperate with adjuster (provide requested documentation)

---

## 9. Measurable Requirements and Audit Verification

### 9.1 Compliance Metrics

The following metrics SHALL be measured to demonstrate Control A.7.5 compliance:

#### 9.1.1 Fire Protection Coverage Metrics

**Fire Detection Coverage:**
- Metric: Percentage of facility area with smoke/heat detectors
- Target: 100%
- Measurement: Covered area (m²) / Total facility area (m²)
- Audit evidence: Fire detection system documentation, floor plans with detector locations

**Fire Suppression Coverage:**
- Metric: Percentage of facility area with fire suppression (sprinklers or gas suppression)
- Target: 100%
- Measurement: Protected area (m²) / Total facility area (m²)
- Audit evidence: Fire suppression system documentation, floor plans with sprinkler/nozzle locations

**Fire Detection Testing Compliance:**
- Metric: Percentage of required tests completed on time
- Target: 100%
- Measurement: Completed tests / Required tests (semi-annual detector tests, annual system tests)
- Audit evidence: Fire alarm test logs (past 12 months)

#### 9.1.2 Water Protection Coverage Metrics

**Water Detection Coverage:**
- Metric: Percentage of at-risk areas with water detection sensors
- Target: 100% of identified at-risk areas
- Measurement: Protected at-risk areas / Total at-risk areas
- Audit evidence: Water detection system documentation, floor plans with sensor locations

**Water Sensor Testing Compliance:**
- Metric: Percentage of required tests completed on time
- Target: 100%
- Measurement: Completed tests / Required tests (monthly sensor tests)
- Audit evidence: Water sensor test logs (past 12 months)

#### 9.1.3 Environmental Monitoring Metrics

**Temperature Monitoring Coverage:**
- Metric: Percentage of server rooms with continuous temperature monitoring
- Target: 100%
- Measurement: Monitored server rooms / Total server rooms
- Audit evidence: Environmental monitoring system configuration, sensor placement documentation

**Temperature Excursions:**
- Metric: Count of temperature excursions per month (outside target range 18-27°C)
- Target: <5 per month (per facility)
- Measurement: Query monitoring system (count threshold breaches)
- Audit evidence: Monthly temperature monitoring reports (past 12 months)

**Humidity Monitoring Coverage:**
- Metric: Percentage of server rooms with continuous humidity monitoring
- Target: 100%
- Measurement: Monitored server rooms / Total server rooms
- Audit evidence: Environmental monitoring system configuration

#### 9.1.4 Incident Metrics

**Environmental Incidents:**
- Metric: Count of environmental incidents per year (fire, flood, temperature causing damage)
- Target: 0 major incidents (incidents causing equipment damage or downtime)
- Measurement: Incident management system query (environmental incidents, severity)
- Audit evidence: Environmental incident reports (past 12 months)

**Fire Drills:**
- Metric: Fire drills conducted per year
- Target: 1 annual minimum (critical facilities), 1 biennial minimum (standard facilities)
- Measurement: Count of completed fire drills
- Audit evidence: Fire drill reports (past 24 months)

### 9.2 Audit Evidence

#### 9.2.1 Risk Assessment Evidence

**Environmental Threat Risk Assessment:**
- Assessment report (per facility, annual)
- Risk register (all identified risks, ratings, mitigation strategies)
- Annual reassessment documentation

**Flood Risk Assessment:**
- Flood zone determination (FEMA maps or equivalent)
- Flood risk mitigation measures documentation (equipment elevation, flood barriers, drainage)

**Seismic Risk Assessment (if applicable):**
- Seismic zone determination (USGS maps or equivalent)
- Seismic mitigation measures documentation (equipment anchoring, structural reinforcement)

#### 9.2.2 Fire Protection Evidence

**Fire Detection System:**
- System configuration documentation (detector types, locations, zones)
- Floor plans with detector placement
- Fire alarm panel configuration
- Monitoring service contract (if 24/7 monitoring)

**Fire Suppression System:**
- System type documentation (sprinkler type, gas suppression agent)
- Floor plans with sprinkler head / gas suppression nozzle locations
- Inspection reports (annual sprinkler inspection, annual gas suppression inspection)
- Professional service contracts

**Fire Testing Records:**
- Fire alarm test logs (semi-annual detector tests, annual full system tests, past 12 months)
- Fire drill reports (annual drills, past 24 months)

#### 9.2.3 Water Protection Evidence

**Water Detection System:**
- System configuration documentation (sensor types, locations)
- Floor plans with sensor placement
- Alert configuration (notification recipients, alert thresholds)

**Water Detection Testing:**
- Sensor test logs (monthly tests, past 12 months)

**Water Damage Incidents:**
- Water damage incident reports (past 12 months, if any)
- Incident response documentation (actions taken, equipment damage, resolution)

#### 9.2.4 Environmental Monitoring Evidence

**Temperature and Humidity Monitoring:**
- Monitoring system configuration (sensor types, locations, alert thresholds)
- Floor plans with sensor placement
- Historical monitoring data (12 months of temperature/humidity data)
- Excursion reports (monthly reports, count of excursions, past 12 months)

**Environmental Monitoring Testing:**
- Sensor test logs (monthly accuracy tests, past 12 months)

#### 9.2.5 Structural Protection Evidence

**Structural Inspection Reports:**
- Initial structural inspection (before facility occupancy)
- Periodic structural inspections (every 5 years)
- Post-event inspections (after earthquakes, hurricanes, if applicable)

**Equipment Anchoring Documentation:**
- Equipment anchoring installation records (server racks, HVAC, UPS)
- Photographs of anchored equipment
- Seismic certification (if seismic-rated racks used)

### 9.3 Testing Requirements

#### 9.3.1 Fire Protection Testing

**Semi-Annual Testing:**
- Smoke detector test (all detectors tested with smoke aerosol or magnet test)
- Document results (detector ID, pass/fail)

**Annual Testing:**
- Full fire alarm system test (professional fire alarm company)
- Sprinkler system inspection (professional sprinkler company, flow test, valve functionality)
- Gas suppression system test (professional, functional test no discharge, see Section 3.2.2)
- Fire drill (all occupants, see Section 3.3)

#### 9.3.2 Water Detection Testing

**Monthly Testing:**
- Water sensor test (all sensors tested with water, verify alert)
- Document results (sensor ID, pass/fail, issues)

**Annual Testing:**
- Professional inspection (sensor cleaning, cable integrity check)

#### 9.3.3 Environmental Monitoring Testing

**Monthly Testing:**
- Temperature/humidity sensor accuracy (compare to handheld thermometer/hygrometer)
- Alert testing (manually trigger threshold, verify alert received)
- Document results (sensor ID, accuracy, alert test results)

**Quarterly Testing:**
- Sensor calibration check (compare all sensors to reference instrument)

---

## 10. Cloud and Colocation Considerations

### 10.1 Cloud Environments

**Environmental Protection is Cloud Provider Responsibility:**

For organizations operating 100% in cloud environments (AWS, Azure, GCP) with no on-premises datacenters or information processing facilities:

- **Control A.7.5 applicability:** Not Applicable (mark as "Not Applicable" in Statement of Applicability)
- **Rationale:** Cloud providers manage physical infrastructure and environmental protection
- **Organization's responsibility:** Assess cloud provider environmental protection controls through supplier management (Control A.5.19-23)

**Supplier Assessment Approach:**

**Audit Report Review:**
- Obtain cloud provider SOC 2 Type II report (review physical and environmental protection controls section)
- Obtain cloud provider ISO 27001 certification (review environmental protection controls A.7.5)
- Verify environmental protection controls implemented:
  - Fire detection and suppression (datacenters)
  - Water damage protection
  - Temperature and humidity control (precision cooling)
  - Structural protection (seismic design, hurricane resistance)
  - Flood protection (site selection, equipment elevation)

**Environmental Protection Verification:**
- Review audit reports annually (when updated)
- Verify no adverse findings in environmental protection controls
- Review datacenter certifications (Uptime Institute Tier, TIA-942, EN 50600)
- Document supplier assessment (annual cloud provider security review)

**Office Environmental Protection:**
- Even cloud-only organizations typically have office premises
- Office environmental protection still required (fire detection, basic environmental controls)
- This control (A.7.5) primarily focuses on information processing facilities (datacenters), but basic protections apply to offices

### 10.2 Colocation Facilities

**Shared Responsibility Model:**

For organizations utilizing colocation datacenter facilities:

#### 10.2.1 Provider Responsibilities (Typical)

**Colocation Provider Manages:**
- Building-wide fire detection and suppression (facility level)
- Building HVAC and environmental control (facility level)
- Building structural protection (building design, seismic/wind resistance)
- Building flood protection (site selection, drainage systems)
- Building power and cooling infrastructure (see POL-S4)

**Provider Evidence:**
- SOC 2 Type II report (physical and environmental protection controls section)
- ISO 27001 certification (if available)
- Uptime Institute Tier Certification (datacenter reliability tier)
- TIA-942 or EN 50600 compliance (if available)
- Environmental incident reports (quarterly reports to customers)
- SLA reports (temperature/humidity compliance, environmental uptime)

#### 10.2.2 Customer Responsibilities (Typical)

**[Organization] Manages:**
- Equipment-level environmental monitoring (temperature sensors within cage/suite)
- Equipment-level fire suppression (optional, gas suppression within cage if provider does not provide)
- Equipment rack anchoring (seismic zones, see Section 6.2)
- Equipment water damage protection (equipment elevation within cage)

**Customer Implementation:**
- Install temperature/humidity sensors within cage (optional but recommended)
- Install equipment-level UPS (see POL-S4, customer UPS for network equipment)
- Anchor equipment racks (per Section 6.2, if in seismic zone)
- Elevate equipment off floor (if cage floor is slab, not raised floor)

#### 10.2.3 Responsibility Matrix Documentation

Maintain formal responsibility matrix in colocation contract:

| Environmental Control | Provider | Customer |
|----------------------|----------|----------|
| Building fire detection | ✅ | - |
| Building fire suppression | ✅ | - |
| Equipment-level gas suppression (in cage) | - | ✅ (optional) |
| Building HVAC | ✅ | - |
| Equipment-level temperature monitoring | - | ✅ (optional) |
| Building structural protection | ✅ | - |
| Equipment rack anchoring | - | ✅ |
| Building flood protection | ✅ | - |
| Equipment elevation (within cage) | - | ✅ |
| Environmental incident response | ✅ (building) | ✅ (equipment) |

#### 10.2.4 Verification and Audit

**Annual Provider Verification:**
- Request updated SOC 2 Type II report (annual)
- Review provider audit findings (verify no adverse environmental protection findings)
- Review provider SLA reports (temperature/humidity compliance, environmental incidents)
- Verify datacenter certifications (Uptime Institute, TIA-942)

**Customer Audit Evidence:**
- Responsibility matrix (documented in colocation contract)
- Provider audit reports (SOC 2, ISO 27001)
- Provider datacenter certifications (Uptime Institute Tier, TIA-942, EN 50600)
- Provider SLA reports (past 12 months)
- Customer-implemented controls evidence:
  - Temperature/humidity monitoring data (if customer sensors installed)
  - Equipment rack anchoring documentation (photos, installation records)
  - Equipment elevation documentation (if applicable)
- Annual provider verification documentation

---

## 11. Related Documents

**Framework Sections:**
- **ISMS-POL-A.7.4-5-11-S1:** Executive Summary, Control Alignment, Scope (framework foundation)
- **ISMS-POL-A.7.4-5-11-S2:** Physical Security Monitoring (A.7.4) - access control, CCTV, intrusion detection
- **ISMS-POL-A.7.4-5-11-S4:** Utility Resilience (A.7.11) - power, HVAC, telecommunications (HVAC capacity and redundancy)
- **ISMS-POL-A.7.4-5-11-S5:** Assessment Methodology and Evidence Framework
- **ISMS-IMP-A.7.4-5-11-S2:** Environmental Protection Implementation (fire detection/suppression, water detection, temperature monitoring deployment)
- **ISMS-IMP-A.7.4-5-11-S4:** Facilities Assessment (ongoing environmental compliance monitoring)

**Related ISMS Policies:**
- **ISMS-POL-A.8.13-14-5.30:** Business Continuity and Disaster Recovery (physical disaster recovery, backup/restore)
- **ISMS-POL-A.5.24-27:** Incident Management (environmental incident handling procedures)
- **ISMS-POL-A.5.19-23:** Information Security for Use of Cloud Services (cloud provider environmental protection assessment)

**External Standards:**
- **ISO/IEC 27001:2022:** Control A.7.5 - Protecting Against Physical and Environmental Threats
- **ISO/IEC 27002:2022:** Detailed guidance for Control A.7.5
- **NIST SP 800-53 Rev 5:** Physical and Environmental Protection (PE) family
- **ASHRAE TC 9.9:** Thermal Guidelines for Data Processing Environments
- **NFPA 75:** Standard for the Fire Protection of Information Technology Equipment (fire protection in datacenters)
- **NFPA 2001:** Standard on Clean Agent Fire Extinguishing Systems (gas suppression systems)

---

**END OF ISMS-POL-A.7.4-5-11-S3**

---

**Document Approval Signatures:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Author | [Name] | | |
| Facilities Manager | [Name] | | |
| Security Operations Manager | [Name] | | |
| CISO | [Name] | | |

---

*"Environmental protection is not just having fire alarms and sprinklers. It's systematic threat assessment, comprehensive fire and water protection, continuous environmental monitoring, structural integrity, and coordinated response procedures—all designed to protect information processing facilities from environmental threats that could cause catastrophic damage."*
