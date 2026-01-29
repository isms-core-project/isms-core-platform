# PROJECT BRIEF: ISMS Controls A.7.4/5/11 - Physical Infrastructure Security

## Combined Control Approach

You are implementing **THREE related ISO 27001:2022 Annex A controls as a unified framework**:

- **A.7.4 - Physical Security Monitoring**: Monitoring of physical access and facilities
- **A.7.5 - Protecting Against Physical and Environmental Threats**: Protection from environmental hazards
- **A.7.11 - Supporting Utilities**: Utility infrastructure security (power, cooling, communications)

**Why Combined:**
These three controls form the **Physical Infrastructure Security Framework**:
- A.7.4 monitors WHO enters physical facilities and WHAT happens inside
- A.7.5 protects facilities from ENVIRONMENTAL threats (fire, flood, temperature, etc.)
- A.7.11 ensures UTILITIES supporting facilities are secure and resilient (power, HVAC, connectivity)

Attempting to implement them separately would result in:
- Disconnected physical security and environmental monitoring
- Redundant facilities risk assessments
- Fragmented utility management
- Inefficient evidence collection

**Reference Implementation**: 
- **Structure model**: ISMS-A.8.20-22-Network-Security (combined controls)
- **Quality level**: ISMS-A.8.23-Web-Filtering
- **Approach**: Unified physical infrastructure framework with distinct sections per control

**IMPORTANT NOTE - Cloud-Only Organizations:**
If your organization operates **100% in cloud environments** (AWS, Azure, GCP) with **no on-premises datacenters or offices**:
- These controls may be **NOT APPLICABLE** to your ISMS
- Cloud providers manage physical infrastructure (your responsibility is supplier management via A.5.19-23)
- Focus on **office physical security** only (if you have offices)
- Consider marking these controls as "Not Applicable - Cloud Environment" in Statement of Applicability

**Integration Note**: This stack integrates with:
- A.7.1-3 (Physical Access Control) - Entry/exit security
- A.5.19-23 (Cloud Services) - Cloud provider physical security via supplier assessment
- A.8.13-14-5.30 (BC/DR) - Physical disaster recovery
- A.8.6 (Capacity Management) - Utility capacity planning

## Context & Approach

You are implementing a comprehensive **Physical Infrastructure Security Framework** using Systems Engineering methodology. This framework must be **completely generic** - applicable to any organization's physical footprint, whether datacenters, offices, or hybrid environments.

**Implementation Philosophy**: 
- Apply Feynman's "don't fool yourself" principle - no security theater
- System Engineering approach: Threats → Controls → Monitoring → Evidence
- Think with TWO hats simultaneously:
  * **ISMS Implementer**: Build practical physical security framework
  * **ISMS Auditor**: Verify measurable physical security effectiveness
- Focus on genuine security improvement, not checkbox compliance

**Applicability**:
- All content must be **completely generic and location-agnostic**
- Use "[Organization]" as placeholder throughout
- Framework adapts to: on-premises datacenters, offices, colocation facilities, cloud (via supplier management)
- No assumptions about facility size or criticality

## Core Requirements (Specific to A.7.4/5/11)

### 1. The Physical Infrastructure Security Challenge

**Traditional approach (cargo cult):**
```
"We have a badge system. There's a fire alarm. 
The UPS is... somewhere? IT handles that stuff."
[No monitoring, no environmental protection plan, utility single points of failure]
```
❌ This is meaningless checkbox compliance.

**What auditors and implementers actually need:**

**For A.7.4 (Physical Security Monitoring):**
- Physical access monitoring
  - Access control system (badge/card readers)
  - Access logs (who entered where, when)
  - Visitor management (sign-in, escort requirements)
  - Failed access attempts (tailgating detection, forced entry)
  - Access review (periodic verification of authorized personnel)
- Physical intrusion detection
  - Motion sensors in restricted areas
  - Door/window sensors
  - Glass break detectors
  - Perimeter intrusion detection (fences, barriers)
- Video surveillance (CCTV)
  - Camera placement (entrances, exits, server rooms, restricted areas)
  - Camera coverage (no blind spots)
  - Video retention (30-90 days typical)
  - Video review procedures (incident investigation)
- Security personnel monitoring
  - Security guard duties (patrols, monitoring, incident response)
  - Security operations center (SOC) if applicable
  - Security incident logging
- Physical security alarm system
  - Alarm types (intrusion, fire, flood, environmental)
  - Alarm monitoring (24/7 if critical facilities)
  - Alarm response procedures
  - False alarm management
- Physical security monitoring integration
  - Integration with security operations (SIEM, SOC)
  - Integration with incident management
  - Monitoring dashboard (physical security events)

**For A.7.5 (Protecting Against Physical and Environmental Threats):**
- Environmental threat risk assessment
  - Natural disasters (flood, earthquake, hurricane, tornado)
  - Fire risk (electrical, equipment overheating, external)
  - Water damage (flooding, plumbing failures, roof leaks)
  - Temperature extremes (overheating, freezing)
  - Humidity (condensation, corrosion)
  - Physical intrusion (theft, vandalism, terrorism)
- Fire detection and suppression
  - Smoke detectors (early warning)
  - Heat detectors
  - Fire alarm system
  - Fire suppression system (sprinklers, gas suppression for datacenters)
  - Fire extinguishers (type and placement)
  - Fire drill frequency
  - Emergency evacuation plan
- Flood and water damage protection
  - Flood risk assessment (location-based)
  - Water detection sensors (server rooms, below-grade facilities)
  - Drainage systems
  - Waterproofing (walls, floors, ceilings)
  - Equipment elevation (off floor in flood-prone areas)
- Temperature and humidity control
  - HVAC monitoring
  - Temperature alarms (too hot or too cold)
  - Humidity alarms (too humid or too dry)
  - Redundant cooling (N+1 or 2N)
- Structural protection
  - Building structural integrity
  - Seismic protection (earthquake zones)
  - Wind resistance (hurricane zones)
  - Equipment anchoring and racking
- Physical access barriers
  - Perimeter fencing
  - Vehicle barriers (bollards, gates)
  - Secure construction (walls, doors, windows)
  - Reinforced server rooms/datacenters
- Environmental protection plan
  - Threat response procedures
  - Equipment relocation plans (if environmental threat imminent)
  - Insurance coverage

**For A.7.11 (Supporting Utilities):**
- Power supply resilience
  - Primary power source (utility power)
  - Uninterruptible Power Supply (UPS)
    - UPS capacity (minutes to hours of backup)
    - UPS testing frequency
    - Battery replacement schedule
  - Backup generator
    - Generator capacity (full load hours)
    - Generator testing frequency (monthly load testing)
    - Fuel supply and refueling
    - Automatic transfer switch (ATS)
  - Power redundancy (N+1, 2N, or higher)
  - Power quality monitoring (voltage, frequency)
- HVAC and cooling
  - Cooling capacity (BTU/kW)
  - Redundant cooling units (N+1 or 2N)
  - HVAC monitoring and alarms
  - Temperature set points (typical: 18-27°C / 64-80°F)
  - Humidity set points (typical: 40-60% RH)
  - Hot aisle / cold aisle containment (datacenter best practice)
- Telecommunications infrastructure
  - Internet connectivity resilience (dual ISPs, diverse paths)
  - Telephone system resilience
  - Network equipment power protection (UPS)
- Water supply (if applicable)
  - Water for cooling systems
  - Water supply redundancy
- Utility failure procedures
  - Power failure response (UPS → generator → graceful shutdown)
  - HVAC failure response (temperature monitoring, emergency cooling)
  - Telecommunications failure response (failover to backup ISP)
- Utility monitoring
  - Real-time monitoring of power, cooling, connectivity
  - Alerting on utility failures or degradation
  - Utility performance dashboards

**Your SE Framework Must Provide:**
- **Physical Monitoring Framework** - comprehensive visibility into physical access and events
- **Environmental Protection Framework** - systematic protection against environmental threats
- **Utility Resilience Framework** - reliable power, cooling, and connectivity
- **Evidence Collection Framework** - access logs, environmental data, utility monitoring

### 2. Document Length and Quality Guidelines

**Python Scripts:**
- Scripts should be **as long as required** to meet quality standards
- No arbitrary line limits - focus on correctness and robustness
- Physical infrastructure assessment may involve IoT sensor data parsing
- Quality > arbitrary length constraints

**Policy Documents (POLs):**
- Should be **comprehensive but not over-engineered**
- Include everything necessary for implementation and audit
- Avoid excessive theoretical content
- Practical and actionable guidance
- This is a 3-control stack with facilities management focus
- Expected range: 1,200-1,600 lines total
- "Just right" - not too short (incomplete), not too long (overkill)

**Implementation Guides (IMPs):**
- Should be **practical and focused**
- Step-by-step procedures without unnecessary elaboration
- Include examples and common pitfalls
- Don't repeat policy content - reference it

**Annexes:**
- Physical security best practices
- Environmental threat assessment templates
- UPS and generator sizing guides
- HVAC capacity calculation examples

### 3. Document Structure (Adapted for A.7.4/5/11)

```
ISMS-A.7.4-5-11-Physical-Infrastructure/
├── 00_pol-struc/
│   └── [Framework planning, how three controls integrate]
├── 10_pol-md/
│   ├── ISMS-POL-A.7.4-5-11-S1-Executive-Control-Alignment.md
│   ├── ISMS-POL-A.7.4-5-11-S2-Physical-Monitoring-A74.md
│   ├── ISMS-POL-A.7.4-5-11-S3-Environmental-Protection-A75.md
│   ├── ISMS-POL-A.7.4-5-11-S4-Utility-Resilience-A711.md
│   ├── ISMS-POL-A.7.4-5-11-S5-Assessment-Evidence-Framework.md
│   └── ISMS-POL-A.7.4-5-11-Annex-[Topic].md [if needed]
├── 30_imp-md/
│   ├── ISMS-IMP-A.7.4-5-11-S1-Physical-Monitoring-Implementation.md
│   ├── ISMS-IMP-A.7.4-5-11-S2-Environmental-Protection-Implementation.md
│   ├── ISMS-IMP-A.7.4-5-11-S3-Utility-Resilience-Implementation.md
│   ├── ISMS-IMP-A.7.4-5-11-S4-Facilities-Assessment.md
│   └── ISMS-IMP-A.7.4-5-11-Annex-[Topic].md [if needed]
└── 50_scripts-excel/
    ├── generate_assessment_1_access_monitoring.py
    ├── generate_assessment_2_environmental_protection.py
    ├── generate_assessment_3_utility_resilience.py
    └── generate_dashboard_physical_infrastructure.py
```

### 4. Policy Content Requirements (Specific to A.7.4/5/11)

**Section 1 (S1): Executive Summary, Control Alignment, Scope**
- ISO 27001:2022 control text for ALL THREE controls (exact quotes)
- Executive summary explaining unified physical infrastructure framework
- Scope: Framework covers monitoring, environmental protection, utility resilience
- **Cloud applicability note**: If organization is cloud-only, how these controls apply (via A.5.19-23 supplier management)
- Integration approach: How three controls work together
- Relationship to other physical controls (A.7.1-3) and BC/DR (A.8.13-14-5.30)

**Section 2 (S2): Physical Security Monitoring (A.7.4)**
Focus on **A.7.4 - Physical Security Monitoring** specifically:
- Access monitoring (badge systems, logs, visitors)
- Intrusion detection (sensors, alarms)
- Video surveillance (CCTV coverage, retention)
- Security personnel (guards, patrols)
- Alarm systems (types, monitoring, response)
- Integration with security operations
- Measurable requirements with audit verification criteria

**Section 3 (S3): Environmental Protection (A.7.5)**
Focus on **A.7.5 - Protecting Against Physical and Environmental Threats** specifically:
- Environmental risk assessment (natural disasters, fire, flood, temperature)
- Fire detection and suppression
- Flood and water damage protection
- Temperature and humidity control
- Structural protection
- Physical access barriers
- Environmental protection plan
- Measurable requirements with audit verification criteria

**Section 4 (S4): Utility Resilience (A.7.11)**
Focus on **A.7.11 - Supporting Utilities** specifically:
- Power supply resilience (UPS, generators, redundancy)
- HVAC and cooling (capacity, redundancy, monitoring)
- Telecommunications (ISP redundancy, diverse paths)
- Water supply (if applicable)
- Utility failure procedures
- Utility monitoring and alerting
- Measurable requirements with audit verification criteria

**Section 5 (S5): Assessment Methodology and Evidence Framework**
- Physical access log analysis
- Environmental monitoring data analysis
- Utility uptime and performance tracking
- Evidence collection per control
- Compliance scoring methodology

### 5. Implementation Guidance Requirements

**IMP-S1: Physical Monitoring Implementation**
- Access control system deployment
- CCTV system design and deployment
- Intrusion detection system installation
- Monitoring integration (dashboards, alerting)

**IMP-S2: Environmental Protection Implementation**
- Fire detection/suppression system deployment
- Water detection system installation
- Temperature/humidity monitoring
- Environmental threat response procedures

**IMP-S3: Utility Resilience Implementation**
- UPS sizing and installation
- Generator sizing and installation
- HVAC capacity planning and redundancy
- ISP redundancy configuration
- Utility monitoring system deployment

**IMP-S4: Facilities Assessment**
- Physical security audit procedures
- Environmental risk assessment
- Utility resilience testing
- Continuous monitoring approach

### 6. Assessment Tools (Specific to A.7.4/5/11)

**Assessment Workbook 1: Physical Access Monitoring (A.7.4)**
- Access log analysis (entries per day, failed attempts, after-hours access)
- CCTV coverage (cameras per area, retention compliance)
- Intrusion detection coverage (sensors per area, alarm events)
- Visitor management compliance
- Physical security incident tracking

**Assessment Workbook 2: Environmental Protection (A.7.5)**
- Fire detection system status (detectors per area, testing frequency)
- Fire suppression system status (testing, inspection)
- Water detection sensors (coverage, alarm events)
- Temperature/humidity monitoring (excursions, alarms)
- Environmental threat incidents

**Assessment Workbook 3: Utility Resilience (A.7.11)**
- Power infrastructure (UPS capacity, battery age, generator testing)
- HVAC infrastructure (cooling capacity, redundancy, uptime)
- Telecommunications infrastructure (ISP SLAs, failover testing)
- Utility failure events (frequency, duration, impact)
- Utility monitoring coverage

**Dashboard: Physical Infrastructure Health**
- Overall physical security score
- Access monitoring metrics
- Environmental protection metrics
- Utility uptime and resilience metrics
- Incident trends

### 7. Python Scripts Approach

Scripts should:
- Parse access control logs
- Parse environmental sensor data
- Parse utility monitoring data (power, HVAC, ISP)
- Calculate uptime and reliability metrics
- Generate compliance dashboards

**No arbitrary line limits** - IoT data parsing can be complex.

### 8. Key Integration Points

**Integrates with:**
- A.7.1-3 (Physical Access Control) - Entry/exit security
- A.5.19-23 (Cloud Services) - Cloud provider physical security assessment
- A.8.13-14-5.30 (BC/DR) - Physical disaster recovery
- A.8.6 (Capacity Management) - Utility capacity planning
- A.5.24-27 (Incident Management) - Physical security incidents

### 9. Quality Checks

- [ ] All THREE control texts quoted correctly
- [ ] Each control's requirements distinctly addressed
- [ ] Cloud applicability clearly documented
- [ ] Framework works for datacenters, offices, colocation
- [ ] Assessment workbooks cover all three controls
- [ ] UPS/generator/HVAC sizing guidance included

### 10. Regulatory Framework (per ISMS-POL-00)

**Mandatory Compliance (Tier 1):**
- ISO/IEC 27001:2022: Controls A.7.4, A.7.5, A.7.11

**Conditional Compliance (Tier 2):**
- **FINMA** (if Swiss financial institution):
  - FINMA Circular 2023/1 Margin 50-62: Physical security requirements
- **DORA** (if EU financial entity):
  - Article 12: Physical security and environmental controls for ICT infrastructure
- **NIS2** (if essential/important entity):
  - Article 21(2): Physical security and environmental protection

**Informational Reference (Tier 3):**
- Uptime Institute Tier Standards (Tier I-IV datacenter classification)
- TIA-942 (Telecommunications Infrastructure Standard for Data Centers)
- EN 50600 (European standard for data centre facilities and infrastructures)

For complete regulatory categorization, refer to ISMS-POL-00.

### 11. Special Considerations

**Cloud-Only Organizations:**
- If 100% cloud (no on-premises infrastructure):
  - Physical infrastructure is cloud provider's responsibility
  - Your controls: A.5.19-23 (Cloud Services) supplier assessment
  - Statement of Applicability: Mark A.7.4/5/11 as "Not Applicable - Cloud Environment"
  - Focus on office physical security only (if applicable)

**Colocation Facilities:**
- If using colocation (leased datacenter space):
  - Some controls shared with colocation provider
  - Document responsibility matrix (customer vs. provider)
  - Verify provider controls through audits/certifications

**Office vs. Datacenter:**
- Office physical security (lower criticality)
- Datacenter physical security (higher criticality, 24/7 monitoring)
- Framework must address both

**Geographic Diversity:**
- Natural disaster risks vary by location
- Earthquake zones: structural requirements
- Hurricane zones: wind resistance, generator fuel
- Flood zones: elevation, drainage
- Framework must be location-adaptable

### 12. Autonomous Work Requirements

**READ Phase:**
- Review reference implementations
- Understand physical infrastructure context
- Identify facilities security patterns

**UPDATE Phase:**
- Adapt to physical infrastructure context
- Ensure all three controls distinctly addressed
- Address cloud applicability clearly
- Maintain quality

**TEST Phase:**
- Fix UTF-8 encoding proactively
- Keep emojis in Excel workbooks
- Test formulas carefully
- Verify conditional formatting
- Test scripts mentally

**PRESENT Phase:**
- Deliver complete sections
- Self-assess against checklist
- Flag uncertainties

### 13. Deliverable Sequence

1. **Structure Plan** - Confirm approach, sections, workbooks
2. **Policy Sections** (S1→S2→S3→S4→S5) - Wait for approval between each
3. **Implementation Sections** (S1→S2→S3→S4) - Wait for approval
4. **Assessment Scripts** - Test thoroughly before delivery
5. **Quality Review** - Self-assessment

---

## Your Mission for A.7.4/5/11

Create the **Physical Infrastructure Security Framework** that provides:
- Comprehensive physical monitoring (A.7.4)
- Systematic environmental protection (A.7.5)
- Reliable utility infrastructure (A.7.11)
- Unified physical infrastructure evidence collection
- Applicable to datacenters, offices, colocation, and cloud (via supplier management)

Use Systems Engineering methodology for **systematic physical infrastructure assessment**.

Make it completely generic - works for any facility type, any location, any organization.

Think like a facilities manager AND an auditor.

**Important**: Clearly document cloud applicability - many organizations can mark these NOT APPLICABLE.

**Ready? Let's start with the structure plan.**
