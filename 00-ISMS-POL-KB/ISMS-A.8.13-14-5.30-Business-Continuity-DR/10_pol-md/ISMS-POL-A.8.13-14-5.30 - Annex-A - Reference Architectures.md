# ISMS-POL-A.8.13-14-5.30-Annex-A: Reference Architectures

**Document Classification:** Internal - ISMS Policy  
**Version:** 1.0  
**Effective Date:** [To be defined]  
**Review Cycle:** Annual  
**Policy Owner:** Chief Information Security Officer (CISO)  
**Approved By:** [Approval Authority]

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Infrastructure Architect / CISO | Initial reference architectures for BC/DR |

---

## Table of Contents

1. [Purpose of Reference Architectures](#1-purpose-of-reference-architectures)
2. [Backup Architecture Patterns](#2-backup-architecture-patterns)
3. [Redundancy Architecture Patterns](#3-redundancy-architecture-patterns)
4. [Geographic Redundancy Patterns](#4-geographic-redundancy-patterns)
5. [Cloud DR Architecture Patterns](#5-cloud-dr-architecture-patterns)
6. [Ransomware-Resistant Architecture](#6-ransomware-resistant-architecture)
7. [Architecture Selection Framework](#7-architecture-selection-framework)

---

## 1. Purpose of Reference Architectures

### 1.1 Role of This Annex

This annex provides **reference architectures** (architectural patterns and examples) for implementing BC/DR controls. These are not prescriptive requirements but rather proven patterns that [Organization] can adapt to its specific context.

**Key Principles:**
- **Technology-Agnostic:** Patterns applicable regardless of specific vendors/technologies
- **Scalable:** Patterns work for small and large organizations
- **Adaptable:** Organizations select and modify patterns based on requirements
- **Proven:** Patterns based on industry best practices and real-world implementations

### 1.2 How to Use Reference Architectures

**Step 1:** Review BIA results (RPO/RTO requirements, system criticality)

**Step 2:** Select reference architecture patterns matching requirements:
- Critical systems (RTO < 4 hours) → Geographic redundancy patterns
- Important systems (RTO 4-24 hours) → Local redundancy or backup patterns
- Standard systems (RTO > 24 hours) → Backup-only patterns

**Step 3:** Adapt pattern to [Organization] context (infrastructure, budget, constraints)

**Step 4:** Document selected architecture in implementation plans

**Step 5:** Test architecture to verify it meets requirements

---

## 2. Backup Architecture Patterns

### 2.1 Pattern 1: Basic Local Backup

**Use Case:** Standard systems, RTO > 24 hours, minimal budget

**Architecture:**
```
┌─────────────────────┐
│  Production Server  │
│    (Primary Data)   │
└──────────┬──────────┘
           │ Backup Agent
           ↓
    ┌──────────────┐
    │ Backup Server│
    │  (On-Prem)   │
    └──────┬───────┘
           │ Store
           ↓
    ┌──────────────┐
    │ Local Storage│
    │  (Disk/NAS)  │
    └──────────────┘
```

**Characteristics:**
- Single backup copy (on-premises)
- No offsite protection
- No immutability
- Lowest cost

**RPO:** Backup frequency (typically daily = 24-hour RPO)

**RTO:** Restore time (typically 4-24 hours depending on data size)

**Risks:**
- Site-wide disaster destroys backup and production
- Ransomware can encrypt backup
- Single point of failure (backup infrastructure)

**Suitable For:** Non-critical systems, test/dev environments

**3-2-1-1-0 Compliance:** ❌ Does not meet (only 2 copies: production + 1 backup)

---

### 2.2 Pattern 2: 3-2-1 Backup (Cloud Offsite)

**Use Case:** Important systems, RTO 4-24 hours, moderate budget

**Architecture:**
```
┌─────────────────────┐
│  Production Server  │──┐
│    (Primary Data)   │  │ Copy 1: Production
└─────────────────────┘  │
                         │
    ┌────────────────┐   │
    │ Local Backup   │───┤ Copy 2: Local Backup (Disk)
    │  (Disk/NAS)    │   │
    └────────┬───────┘   │
             │ Replicate │
             ↓           │
    ┌────────────────┐   │
    │  Cloud Storage │───┘ Copy 3: Offsite (Cloud)
    │  (AWS S3, etc) │
    └────────────────┘

Storage Types: Disk (local) + Cloud (offsite) = 2 media types
```

**Characteristics:**
- 3 copies of data (production + local backup + cloud backup)
- 2 different media types (disk + cloud)
- 1 offsite copy (cloud)
- Geographic protection (cloud in different region)

**RPO:** Backup frequency (hourly to daily)

**RTO:** 
- Fast restore from local backup (hours)
- Slower restore from cloud if local unavailable (hours to days depending on data size and bandwidth)

**Risks:**
- No immutability (ransomware can delete cloud backups if credentials compromised)
- Cloud dependency (vendor lock-in, cost)

**Suitable For:** Important systems requiring geographic protection

**3-2-1-1-0 Compliance:** ⚠️ Partial (3-2-1 met, but missing 1 immutable and 0 errors requires testing)

---

### 2.3 Pattern 3: 3-2-1-1-0 Full Compliance (Immutable Cloud)

**Use Case:** Critical systems, RTO < 4 hours (with redundancy), regulatory compliance (DORA/NIS2)

**Architecture:**
```
┌─────────────────────┐
│  Production Server  │──┐ Copy 1: Production
└─────────────────────┘  │
                         │
    ┌────────────────┐   │
    │ Local Backup   │───┤ Copy 2: Local (Disk)
    │  (Disk/NAS)    │   │
    └────────┬───────┘   │
             │ Replicate │
             ↓           │
    ┌────────────────┐   │
    │ Cloud Standard │───┤ Copy 3: Cloud Standard
    │   (Mutable)    │   │
    └────────┬───────┘   │
             │ Copy      │
             ↓           │
    ┌────────────────┐   │
    │ Cloud Immutable│───┘ Copy 4 (Optional): Immutable
    │ (Object Lock)  │      OR Copy 3 is immutable
    └────────────────┘

Immutable: Cloud Object Lock (AWS S3, Azure Blob)
          or Offline Tape (air-gapped)
          
Testing (0): Regular restore tests verify recoverability
```

**Characteristics:**
- 3+ copies of data
- 2 different media types (disk + cloud, or disk + tape)
- 1 offsite copy (cloud or offsite vault)
- 1 immutable/offline copy (ransomware protection)
- 0 errors through testing (verified recoverability)

**RPO:** Frequent backups (hourly or continuous replication to cloud)

**RTO:** 
- Very fast from local (minutes to hours)
- Fast from cloud standard (hours)
- Slower from immutable (emergency fallback)

**Risks:** Higher cost (multiple backup copies, immutable storage)

**Suitable For:** Critical systems, DORA/NIS2 regulated systems

**3-2-1-1-0 Compliance:** ✅ Full compliance

**DORA/NIS2 Compliance:** ✅ Meets requirements (immutable, offsite, testable)

---

### 2.4 Pattern 4: Hybrid Multi-Tier Backup

**Use Case:** Mixed criticality, optimizing cost vs. protection

**Architecture:**
```
Critical Systems:      Important Systems:     Standard Systems:
3-2-1-1-0             3-2-1                  Basic Local
(Full protection)     (Geographic)           (Cost-optimized)

┌──────────┐          ┌──────────┐           ┌──────────┐
│ Critical │          │Important │           │ Standard │
└────┬─────┘          └────┬─────┘           └────┬─────┘
     │                     │                      │
     ↓                     ↓                      ↓
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│Local Backup │       │Local Backup │       │Local Backup │
│+ Cloud Std  │       │+ Cloud Std  │       │   (Only)    │
│+ Immutable  │       │             │       │             │
└─────────────┘       └─────────────┘       └─────────────┘
```

**Characteristics:**
- Different backup strategies per criticality tier
- Optimizes cost (expensive protection only for critical systems)
- Scales with business requirements

**Suitable For:** Organizations with diverse system portfolio and budget constraints

---

## 3. Redundancy Architecture Patterns

### 3.1 Pattern 5: Active-Passive (Hot Standby)

**Use Case:** Critical systems, RTO < 4 hours, moderate cost

**Architecture:**
```
┌─────────────────────────────────────────┐
│          Load Balancer / Failover       │
│         (Routes traffic to active)      │
└────────────┬────────────────────────────┘
             │
      ┌──────┴──────┐
      │             │
      ↓             ↓
┌───────────┐  ┌───────────┐
│  PRIMARY  │  │ SECONDARY │
│  (Active) │  │ (Standby) │
│           │  │           │
│  Serving  │  │  Ready,   │
│  Traffic  │  │ Not Used  │
└─────┬─────┘  └─────┬─────┘
      │              │
      └──────┬───────┘
             │ Data Replication
             ↓
      ┌─────────────┐
      │  Database   │
      │ (Replicated)│
      └─────────────┘

Failover: Automatic (health checks detect primary failure, route to secondary)
          or Manual (operator decision)
```

**Characteristics:**
- Primary handles all traffic
- Secondary fully running and ready (hot standby)
- Data continuously replicated to secondary
- Automatic or manual failover

**RPO:** Near-zero (continuous replication)

**RTO:** Minutes (automatic failover) to 1-2 hours (manual failover)

**Failover Process:**
1. Health check detects primary failure
2. Load balancer stops routing to primary
3. Load balancer routes to secondary
4. Secondary takes over (already running)

**Advantages:**
- Fast failover (secondary already running)
- Minimal data loss (continuous replication)

**Disadvantages:**
- Secondary resources underutilized (sitting idle)
- Higher cost (duplicate infrastructure)

**Suitable For:** Critical systems with RTO < 4 hours

---

### 3.2 Pattern 6: Active-Active (Load Balanced)

**Use Case:** Critical systems, RTO < 15 minutes, high availability required

**Architecture:**
```
          ┌─────────────────────┐
          │   Load Balancer     │
          │  (Distributes load) │
          └──────────┬──────────┘
                     │
            ┌────────┴────────┐
            │                 │
            ↓                 ↓
      ┌───────────┐     ┌───────────┐
      │  SERVER 1 │     │  SERVER 2 │
      │  (Active) │     │  (Active) │
      │           │     │           │
      │  Serving  │     │  Serving  │
      │  50% Load │     │  50% Load │
      └─────┬─────┘     └─────┬─────┘
            │                 │
            └────────┬────────┘
                     │ Shared Data Layer
                     ↓
            ┌─────────────────┐
            │ Database Cluster│
            │  (Synchronized) │
            └─────────────────┘
```

**Characteristics:**
- Both servers actively serving traffic
- Load distributed across both
- If one fails, other handles 100% load
- Database synchronized in real-time

**RPO:** Zero (real-time synchronization)

**RTO:** Seconds to minutes (automatic, no failover needed - just load redistribution)

**Failover Process:**
1. Health check detects Server 1 failure
2. Load balancer stops sending traffic to Server 1
3. Server 2 now handles 100% load (no failover, already active)

**Advantages:**
- Near-zero downtime
- Full resource utilization (both servers working)
- Seamless failover (no switchover)

**Disadvantages:**
- Highest cost (duplicate infrastructure fully utilized)
- Complex (data synchronization, load balancing)
- Both servers must be sized for full load (to handle failure scenario)

**Suitable For:** Critical systems requiring near-zero RTO, 24/7 operations

---

### 3.3 Pattern 7: N+1 Cluster

**Use Case:** Scalable systems, moderate RTO (< 1 hour), gradual degradation acceptable

**Architecture:**
```
       ┌─────────────────────┐
       │   Load Balancer     │
       └──────────┬──────────┘
                  │
       ┌──────────┼──────────┬──────────┐
       │          │          │          │
       ↓          ↓          ↓          ↓
   ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
   │Server1│ │Server2│ │Server3│ │Server4│
   │       │ │       │ │       │ │(Spare)│
   └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘
       │         │         │         │
       └─────────┴─────────┴─────────┘
                     │
                     ↓
           ┌─────────────────┐
           │ Shared Database │
           └─────────────────┘

Capacity: N servers required for full capacity
          +1 spare server for redundancy
          
Example: 3 servers handle normal load
         If 1 fails, remaining 3 handle load (including spare)
```

**Characteristics:**
- N servers required for capacity
- 1 additional server as spare
- If one fails, N servers continue (may be at reduced capacity)

**RPO:** Near-zero (shared database)

**RTO:** Seconds to minutes (automatic load redistribution)

**Performance During Failure:**
- May operate at reduced capacity (N instead of N+1)
- Acceptable for non-peak times
- May need to scale up during peak + failure

**Advantages:**
- Cost-effective redundancy
- Good balance of cost and availability
- Scalable (add more N+1 as needed)

**Disadvantages:**
- Reduced capacity during failure
- All servers must be able to handle higher load

**Suitable For:** Web applications, API services, scalable workloads

---

## 4. Geographic Redundancy Patterns

### 4.1 Pattern 8: Active-Passive Multi-Site

**Use Case:** Critical systems, site-wide disaster protection, RTO < 4 hours

**Architecture:**
```
┌─────────────────────────────────────────────────────┐
│              Global Load Balancer / DNS              │
│         (Routes to Primary, failover to DR)          │
└────────────────────┬────────────────────────────────┘
                     │
          ┌──────────┴──────────┐
          │                     │
          ↓                     ↓
┌─────────────────┐    ┌─────────────────┐
│  PRIMARY SITE   │    │    DR SITE      │
│   (Location A)  │    │  (Location B)   │
│                 │    │   (50+ km away) │
│  ┌───────────┐  │    │  ┌───────────┐  │
│  │Production │  │    │  │  Standby  │  │
│  │  Servers  │  │    │  │  Servers  │  │
│  └─────┬─────┘  │    │  └─────┬─────┘  │
│        │        │    │        │        │
│  ┌─────▼─────┐  │    │  ┌─────▼─────┐  │
│  │  Primary  │  │    │  │  Replica  │  │
│  │ Database  │──┼────┼─→│ Database  │  │
│  └───────────┘  │    │  └───────────┘  │
│                 │    │                 │
└─────────────────┘    └─────────────────┘
     Active Site           Standby Site
     Serving Traffic       Ready but Unused
     
Data Replication: Async (to minimize latency impact on primary)
Failover: Manual or automatic (depends on failure type)
```

**Characteristics:**
- Primary site serves all traffic
- DR site ready but not serving traffic
- Data replicated to DR site (asynchronous)
- Geographic separation (50-500 km typical)

**RPO:** Replication lag (seconds to minutes, depends on distance and bandwidth)

**RTO:** 1-4 hours (time to failover to DR site, including verification)

**Failover Scenarios:**
- **Site Loss (Fire/Flood/Disaster):** Automatic failover to DR site
- **Planned Maintenance:** Controlled failover to DR site

**Advantages:**
- Protects against site-wide disasters
- DR site can be used for testing (failover tests)
- Moderate cost (DR infrastructure exists but underutilized)

**Disadvantages:**
- Some data loss possible (async replication lag)
- DR resources underutilized
- Complex failover (requires coordination)

**Suitable For:** Critical systems requiring geographic protection

---

### 4.2 Pattern 9: Active-Active Multi-Region (Cloud)

**Use Case:** Global applications, near-zero RTO, cloud-native

**Architecture:**
```
                ┌────────────────────┐
                │ Global CDN / DNS   │
                │  (Geographic LB)   │
                └─────────┬──────────┘
                          │
              ┌───────────┴───────────┐
              │                       │
              ↓                       ↓
    ┌──────────────────┐    ┌──────────────────┐
    │   REGION US-EAST │    │   REGION EU-WEST │
    │                  │    │                  │
    │  ┌────────────┐  │    │  ┌────────────┐  │
    │  │Application │  │    │  │Application │  │
    │  │  Servers   │  │    │  │  Servers   │  │
    │  └──────┬─────┘  │    │  └──────┬─────┘  │
    │         │        │    │         │        │
    │  ┌──────▼─────┐  │    │  ┌──────▼─────┐  │
    │  │  Database  │◄─┼────┼─►│  Database  │  │
    │  │  (Active)  │  │    │  │  (Active)  │  │
    │  └────────────┘  │    │  └────────────┘  │
    │                  │    │                  │
    └──────────────────┘    └──────────────────┘
    Serves US Traffic        Serves EU Traffic
    (Can handle EU          (Can handle US
     if EU fails)            if US fails)
     
Both Regions Active, Database Bi-Directional Replication
```

**Characteristics:**
- Multiple regions actively serving traffic
- Traffic routed to nearest region (latency optimization)
- If one region fails, other regions absorb traffic
- Database multi-master replication (or eventual consistency)

**RPO:** Near-zero (continuous replication)

**RTO:** Seconds (automatic, DNS/CDN redirects traffic)

**Advantages:**
- Near-zero downtime
- Global performance (users routed to nearest region)
- Regional failure transparent to users

**Disadvantages:**
- Highest cost (multiple fully-active regions)
- Most complex (data consistency, conflict resolution)
- Requires cloud-native architecture

**Suitable For:** Global SaaS applications, critical 24/7 services

---

## 5. Cloud DR Architecture Patterns

### 5.1 Pattern 10: Pilot Light (Minimal DR Footprint)

**Use Case:** Important systems, RTO 4-12 hours, cost-optimized DR

**Architecture:**
```
PRIMARY (On-Premises):          DR (Cloud - Pilot Light):
Always Running                  Minimal Running, Scale on Demand

┌─────────────────┐            ┌─────────────────┐
│   Production    │            │   (Stopped)     │
│    Servers      │            │  DR Servers     │
│    (Active)     │            │  (Scale up on   │
│                 │            │   activation)   │
└────────┬────────┘            └────────┬────────┘
         │                              │
         │                              │
┌────────▼────────┐            ┌────────▼────────┐
│   Production    │  Replicate │    DR Database  │
│    Database     │───────────→│   (Synchronized │
│    (Active)     │            │    but minimal) │
└─────────────────┘            └─────────────────┘

DR Site: Core infrastructure minimal (database syncing)
         Application servers stopped (start on DR activation)
```

**Characteristics:**
- Core infrastructure minimal in DR (database syncing)
- Application servers not running (provision on demand)
- Data continuously replicated to DR database
- On DR activation: Provision servers, start applications

**RPO:** Near-zero (continuous database replication)

**RTO:** 4-12 hours (time to provision servers and start applications)

**Cost:** Low (minimal DR infrastructure, pay for compute only during DR)

**Advantages:**
- Very cost-effective DR
- Cloud elasticity (scale up only when needed)
- Data protection (database always synchronized)

**Disadvantages:**
- Longer RTO (time to provision infrastructure)
- Requires automation (to provision quickly)
- Untested provisioning may fail during actual DR

**Suitable For:** Important systems with moderate RTO requirements, budget-conscious DR

---

### 5.2 Pattern 11: Warm Standby (Cloud)

**Use Case:** Critical systems, RTO 1-4 hours, balanced cost/performance

**Architecture:**
```
PRIMARY (On-Premises):          DR (Cloud - Warm Standby):
Full Production                 Reduced Capacity, Always Running

┌─────────────────┐            ┌─────────────────┐
│   Production    │            │   DR Servers    │
│   Servers (10)  │            │  (Running, 2)   │
│   (Full Scale)  │            │  (Scale to 10   │
│                 │            │   on activation)│
└────────┬────────┘            └────────┬────────┘
         │                              │
┌────────▼────────┐            ┌────────▼────────┐
│   Production    │  Replicate │   DR Database   │
│    Database     │───────────→│  (Synchronized) │
└─────────────────┘            └─────────────────┘

DR Site: Minimal servers running (2 of 10)
         Scale up to full capacity on DR activation
```

**Characteristics:**
- DR infrastructure partially running (reduced capacity)
- Can handle limited load immediately
- Scale up to full capacity on DR activation
- Faster than Pilot Light (already running)

**RPO:** Near-zero (continuous replication)

**RTO:** 1-4 hours (time to scale up to full capacity)

**Cost:** Moderate (some infrastructure always running)

**Advantages:**
- Faster than Pilot Light (no cold start)
- Tested infrastructure (DR systems actually running)
- Can scale quickly (cloud auto-scaling)

**Disadvantages:**
- Higher cost than Pilot Light (always-on infrastructure)
- Still requires time to scale up

**Suitable For:** Critical systems with RTO < 4 hours, cloud-based workloads

---

## 6. Ransomware-Resistant Architecture

### 6.1 Pattern 12: Air-Gapped + Immutable Defense-in-Depth

**Use Case:** Critical systems, ransomware protection, regulatory compliance

**Architecture:**
```
┌─────────────────────────────────────────────────────────────┐
│                    PRODUCTION NETWORK                        │
│                                                              │
│  ┌──────────────┐          ┌──────────────┐                │
│  │  Production  │          │ Primary      │                │
│  │   Systems    │──────────│ Backup       │                │
│  └──────────────┘ Backup   │ (Connected)  │                │
│                             └──────┬───────┘                │
│                                    │                        │
└────────────────────────────────────┼────────────────────────┘
                                     │ Replicate
                                     ↓
         ┌───────────────────────────────────────────┐
         │         BACKUP ISOLATION ZONE             │
         │  (Limited network access, strict controls)│
         │                                            │
         │         ┌─────────────────┐                │
         │         │ Cloud Immutable │                │
         │         │  (Object Lock)  │                │
         │         │  30-day retain  │                │
         │         └─────────────────┘                │
         └───────────────────────────────────────────┘
         
         ┌───────────────────────────────────────────┐
         │           OFFLINE / AIR-GAP                │
         │       (NO network connectivity)            │
         │                                            │
         │         ┌─────────────────┐                │
         │         │  Tape Library   │                │
         │         │ (Physical copy) │                │
         │         │ (Offsite vault) │                │
         │         └─────────────────┘                │
         └───────────────────────────────────────────┘

Defense Layers:
1. Primary backup (fast restore, but vulnerable)
2. Immutable cloud (ransomware cannot delete, 30-day retention)
3. Offline tape (complete air-gap, ultimate protection)
```

**Characteristics:**
- **Layer 1:** Primary backup (connected, fast restore, vulnerable to ransomware)
- **Layer 2:** Immutable cloud (ransomware cannot delete/modify)
- **Layer 3:** Offline tape (complete air-gap, no network connectivity)

**Protection Against Ransomware:**
- Ransomware encrypts production → Restore from primary backup (if primary not encrypted)
- Ransomware encrypts production + primary backup → Restore from immutable cloud
- Ransomware encrypts all connected systems → Restore from offline tape

**RPO:** 
- Primary: Hours (frequent backups)
- Immutable: Hours to days (replicated from primary)
- Offline: Days to weeks (periodic tape creation)

**RTO:**
- Primary: Hours (fast restore)
- Immutable: Hours to days (cloud restore)
- Offline: Days to weeks (tape retrieval and restore)

**Cost:** Highest (three backup layers)

**Suitable For:** Critical systems, DORA/NIS2 compliance, high ransomware risk

---

## 7. Architecture Selection Framework

### 7.1 Decision Matrix: Backup Architecture

| System Criticality | RPO Requirement | RTO Requirement | Recommended Pattern | 3-2-1-1-0 |
|-------------------|-----------------|-----------------|---------------------|-----------|
| Low / Standard | > 24 hours | > 24 hours | Pattern 1: Basic Local | ❌ |
| Important | 4-24 hours | 4-24 hours | Pattern 2: 3-2-1 Cloud | ⚠️ |
| Critical | < 4 hours | < 4 hours (with redundancy) | Pattern 3: 3-2-1-1-0 | ✅ |
| Critical (Regulated) | < 4 hours | < 4 hours | Pattern 3 + Pattern 12 | ✅ |
| Mixed Portfolio | Varies | Varies | Pattern 4: Multi-Tier | Varies |

### 7.2 Decision Matrix: Redundancy Architecture

| System Criticality | RTO Requirement | Availability Required | Recommended Pattern |
|-------------------|-----------------|----------------------|---------------------|
| Important | 4-24 hours | 99-99.5% | None (restore from backup acceptable) |
| Critical | 1-4 hours | 99.5-99.9% | Pattern 5: Active-Passive |
| Critical | < 1 hour | 99.9-99.99% | Pattern 6: Active-Active |
| Critical (Scalable) | < 1 hour | 99.9%+ | Pattern 7: N+1 Cluster |

### 7.3 Decision Matrix: Geographic Redundancy

| Disaster Scenario Risk | RTO Requirement | Budget | Recommended Pattern |
|------------------------|-----------------|--------|---------------------|
| Low (single building) | 4-24 hours | Low | No geographic redundancy |
| Medium (city-wide) | 1-4 hours | Moderate | Pattern 8: Active-Passive Multi-Site |
| High (region-wide) | < 1 hour | High | Pattern 9: Active-Active Multi-Region |

### 7.4 Decision Matrix: Cloud DR

| Current Infrastructure | RTO Requirement | Budget | Recommended Pattern |
|-----------------------|-----------------|--------|---------------------|
| On-Prem | 4-12 hours | Low | Pattern 10: Pilot Light |
| On-Prem | 1-4 hours | Moderate | Pattern 11: Warm Standby |
| Cloud | < 1 hour | High | Pattern 9: Multi-Region Active-Active |

### 7.5 Cost vs. RTO Trade-Off

```
Cost
 ^
 │                                  ●  Active-Active Multi-Region
 │                                  
 │                          ●  Active-Active Single Site
 │                          
 │                  ●  Active-Passive Hot Standby
 │                  
 │          ●  Warm Standby (Cloud DR)
 │          
 │  ●  Pilot Light
 │  
 │●  Backup Only
 └──────────────────────────────────────────────────────> RTO
   Days    Hours    1-4h    <1h     Minutes   Seconds
   
Lower cost = Longer RTO
Higher availability/shorter RTO = Higher cost
```

---

## Conclusion

These reference architectures provide proven patterns for implementing BC/DR capabilities. Organizations should:

1. **Assess requirements** (BIA → RPO/RTO)
2. **Select appropriate patterns** (using decision matrices)
3. **Adapt to context** (infrastructure, budget, constraints)
4. **Document selected architecture**
5. **Implement and test**
6. **Evolve over time** (as requirements and technology change)

**Key Takeaways:**
- No single architecture fits all systems (multi-tier approach typical)
- Cost increases with shorter RTO and higher availability
- Testing is essential (architecture must be proven through testing)
- Cloud enables flexible, scalable DR (Pilot Light, Warm Standby patterns)
- Ransomware demands defense-in-depth (immutable + offline backups)

---

**Document End**

**APPROVAL SIGNATURES**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | | | |
| Infrastructure Architect | | | |
| Cloud Architect | | | |
| BC/DR Coordinator | | | |

**Next Review Date:** [One year from approval date]