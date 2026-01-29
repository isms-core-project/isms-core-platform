# ISMS-POL-A.8.20-21-22 — Netzwerksicherheit

---

## Dokumentenlenkung

| Feld | Wert |
|------|------|
| **Dokumenten Titel** | Netzwerksicherheit |
| **Dokumententyp** | Konzept |
| **Dokument-ID** | ISMS-POL-A.8.20-21-22 |
| **Dokumenteneigentümer/in** | Chief Information Security Officer (CISO) |
| **Freigabe durch** | Geschäftsleitung (GL) |
| **Erstellt** | [Date] |
| **Version** | 1.0 |
| **Versionsdatum** | [Zu bestimmen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versions-Verzeichnis**:

| Version | Datum | Autor | Änderungsvermerk |
|---------|-------|-------|------------------|
| 1.0 | [Date] | CISO | Initiale Richtlinie für ISO 27001:2022 Erstzertifizierung |

**Review-Zyklus**: Jährlich  
**Nächstes Review-Datum**: [Inkraftsetzungsdatum + 12 Monate]  

**Freigabekette**:
- Primär: Chief Information Security Officer (CISO)
- Sekundär: Chief Information Officer (CIO)
- Technisch: Network Operations Manager
- Compliance: Legal/Compliance Officer
- Finale Autorität: Geschäftsleitung (GL)

**Zugehörige Dokumente**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.20-21-22 (Implementation Guidance Suite)
- ISO/IEC 27001:2022 Controls A.8.20, A.8.21, A.8.22
- ISMS-POL-A.8.15 (Logging)
- ISMS-POL-A.8.16 (Monitoring Activities)
- ISMS-POL-A.5.23 (Cloud Services)

---

## Management Summary

Diese Richtlinie definiert die Anforderungen von [Organisation] für Netzwerksicherheits-Kontrollen zum Schutz von Informationsassets durch sichere Netzwerkinfrastruktur, Services und Segmentierung gemäss ISO/IEC 27001:2022 Controls A.8.20, A.8.21 und A.8.22.

**Geltungsbereich**: Diese Richtlinie gilt für alle Netzwerkinfrastruktur, Netzwerkgeräte, Netzwerk-Services und Netzwerksegmente unabhängig vom Deployment-Modell (On-Premises, Cloud, Hybrid) oder Technologie (traditionelles Networking, Software-Defined Networking).

**Zweck**: Definition organisatorischer Anforderungen für Implementierung und Governance von Netzwerksicherheits-Kontrollen. Diese Richtlinie definiert WAS Netzwerksicherheits-Schutz erforderlich ist und WER verantwortlich ist. Implementierungsprozeduren (WIE) sind separat in ISMS-IMP-A.8.20-21-22 dokumentiert. Technische Standards und Konfigurationen sind bewusst ausserhalb dieser Richtlinie definiert, um technologische Agilität zu bewahren.

**Kombinierter Control-Ansatz**: Diese drei Controls werden als einheitliches Framework implementiert, da sie auf derselben Netzwerkinfrastruktur operieren und gemeinsame Discovery-, Assessment- und Evidence-Collection-Prozesse teilen. Trotz einheitlicher Implementierung behält jeder Control distinkte Anforderungen für Statement of Applicability (SoA) Zwecke bei.

**Regulatorisches Alignment**: Diese Richtlinie adressiert obligatorische Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatory Applicability Framework), einschliesslich Schweizer nDSG, EU DSGVO und ISO/IEC 27001:2022. Konditionale branchenspezifische Anforderungen (PCI DSS, FINMA, DORA, NIS2) gelten, wo Geschäftsaktivitäten der [Organisation] Anwendbarkeit auslösen.

---

## 1. Control Alignment & Geltungsbereich

### 1.1 ISO/IEC 27001:2022 Controls A.8.20, A.8.21, A.8.22

**ISO/IEC 27001:2022 Annex A.8.20 - Networks Security**

> *Networks and network devices should be secured, managed and controlled to protect information in systems and applications.*

**Control-Zielsetzung**: Sicherstellung, dass Netzwerkinfrastruktur und Geräte gehärtet, überwacht und konfiguriert sind, um unauthorisierten Zugriff zu verhindern und Informationen im Transit zu schützen.

**ISO/IEC 27001:2022 Annex A.8.21 - Security of Network Services**

> *Security mechanisms, service levels and service requirements of network services should be identified, implemented and monitored.*

**Control-Zielsetzung**: Sicherstellung, dass Netzwerk-Services gesichert, verfügbar und überwacht sind, um Business-Operationen zu unterstützen und gleichzeitig vor service-basierten Angriffen zu schützen.

**ISO/IEC 27001:2022 Annex A.8.22 - Segregation of Networks**

> *Groups of information services, users and information systems should be segregated in the organization's networks.*

**Control-Zielsetzung**: Implementierung von Netzwerk-Segmentierung, um Blast Radius zu limitieren, Least Privilege Network Access durchzusetzen und regulatorische Anforderungen für Datenisolation zu erfüllen.

**Statement of Applicability Unabhängigkeit**: Trotz einheitlicher Implementierung und Dokumentation werden Controls A.8.20, A.8.21 und A.8.22 unabhängig im Statement of Applicability bewertet. Jeder Control behält distinkte Anforderungen, Evidence Collection und Compliance Scoring für Audit-Zwecke bei.

**Diese Richtlinie adressiert**:
- Anforderungen an Netzwerkinfrastruktur-Sicherheit (A.8.20)
- Anforderungen an Netzwerk-Services-Sicherheit (A.8.21)
- Anforderungen an Netzwerk-Segmentierung (A.8.22)
- Organisatorische Rollen und Verantwortlichkeiten für Netzwerksicherheits-Governance
- Frameworks für Exception Management und Incident Management
- Integration mit Risk Assessment und Treatment Prozessen der [Organisation]

### 1.2 Was diese Richtlinie tut

Diese Richtlinie:
- **Definiert** Anforderungen an Netzwerksicherheits-Kontrollen ausgerichtet auf organisatorisches Risk Assessment
- **Etabliert** Governance-Framework für Netzwerksicherheits-Entscheidungsfindung
- **Spezifiziert** Verantwortlichkeit für Implementierung von Netzwerksicherheits-Kontrollen
- **Referenziert** anwendbare regulatorische Anforderungen gemäss ISMS-POL-00
- **Integriert** drei verwandte Controls in ein einheitliches Framework für Implementierungs-Effizienz

### 1.3 Was diese Richtlinie NICHT tut

Diese Richtlinie tut NICHT:
- **Spezifizieren technischer Implementierungsdetails** (siehe ISMS-IMP-A.8.20-21-22 Implementation Guides)
- **Definieren von Netzwerk-Topologie oder Architektur** (siehe ISMS-IMP-A.8.20-21-22-S2 Architecture Documentation)
- **Bereitstellen gerätespezifischer Konfigurationsprozeduren** (siehe ISMS-IMP-A.8.20-21-22-S3 Device Hardening)
- **Definieren von Firewall-Regeln oder ACLs** (siehe ISMS-IMP-A.8.20-21-22-S5 Segmentation Implementation)
- **Auswählen von Netzwerk-Technologien oder Anbietern** (Technologieauswahl basierend auf Risk Assessment der [Organisation])
- **Ersetzen von Risk Assessment** (Netzwerksicherheits-Kontrollen werden basierend auf Risk Treatment der [Organisation] ausgewählt)

**Rationale**: Trennung von Richtlinienanforderungen und Implementierungsleitlinien ermöglicht:
- Richtlinienstabilität trotz sich entwickelnder Netzwerk-Technologien (SDN, Cloud Networking, etc.)
- Technische Agilität für Technologie-Updates ohne Richtlinienrevision
- Klare Unterscheidung zwischen Governance (Richtlinie) und Execution (Implementierung)
- Technologie-agnostischer Ansatz anwendbar auf jede Netzwerk-Architektur

### 1.4 Geltungsbereich

**Diese Richtlinie gilt für**:

**Netzwerkinfrastruktur** (A.8.20):
- On-Premises-Netzwerke (Rechenzentren, Büros, Filialen)
- Cloud-Netzwerke (AWS VPC, Azure VNet, GCP VPC, andere Cloud-Provider)
- Hybrid-Netzwerke (On-Premises + Cloud-Integration)
- Software-Defined Networks (SDN, SD-WAN)
- Traditionelle Netzwerke (Router, Switches, Firewalls)
- Wireless-Netzwerke (Corporate WLANs, Gast-Netzwerke)
- Remote-Access-Netzwerke (VPN, Remote Desktop)

**Netzwerkgeräte** (A.8.20):
- Router, Switches, Firewalls, Wireless Access Points
- Load Balancers, VPN Concentrators
- Network Security Appliances (IPS/IDS, DLP)
- Network Management Systems
- Cloud Virtual Network Devices

**Netzwerk-Services** (A.8.21):
- DNS, DHCP, NTP
- Proxy Services, Load Balancing Services
- Authentication Services (RADIUS, TACACS+)
- SNMP, Syslog, andere kritische Netzwerk-Services

**Netzwerksegmente** (A.8.22):
- Security Zones (DMZ, Internal, Management, Guest, Server, etc.)
- VLANs und Subnets
- Trust Boundaries und Inter-Zone Controls
- Cloud Security Groups und Network ACLs

**Personal**:
- Network Administrators, Security Team, IT Operations
- Cloud Administrators, System Owners
- Alle Angestellten (Netzwerk-Zugangs-Richtlinien)

**Diese Richtlinie gilt NICHT für**:
- Application-Layer-Security (adressiert unter anderen Controls)
- Endpoint-Security (adressiert unter A.8.1 User Endpoint Devices)
- Physische Sicherheit von Netzwerk-Equipment (adressiert unter Physical Security Controls)

**Cloud Environment Geltungsbereich**:

Referenzen auf spezifische Cloud-Provider (AWS, Azure, GCP) in dieser Richtlinie sind illustrativ für Cloud-Networking-Konzepte. Anwendbare Cloud-Environments sind im Netzwerkinfrastruktur-Inventar (Workbook 1) dokumentiert. Mit Stand Inkraftsetzungsdatum dieser Richtlinie sind in-scope Cloud-Environments der [Organisation]:

- **Primärer Cloud-Provider**: [Spezifizieren: AWS / Azure / GCP / Andere]
- **Sekundärer Cloud-Provider** (falls anwendbar): [Spezifizieren oder "Keine"]
- **SaaS mit Netzwerk-Integration**: [Auflisten aller SaaS, die VPN/Private Connectivity erfordern]

Cloud-Provider-Hinzufügungen oder Änderungen werden im Netzwerkinfrastruktur-Inventar reflektiert und erfordern keine Richtlinienrevision. Neue Cloud-Environments MÜSSEN äquivalente Controls gemäss dieser Richtlinie implementieren vor Production-Deployment.

### 1.5 Regulatorisches Alignment

Diese Richtlinie implementiert Netzwerksicherheits-Anforderungen zur Compliance mit Regulations gemäss **ISMS-POL-00 (Regulatory Applicability Framework)**:

**Tier 1: Mandatory Compliance**

| Regulation | Anforderung | Anwendbarkeit |
|------------|-------------|---------------|
| **Schweizer nDSG (Bundesgesetz über den Datenschutz)** | Technische und organisatorische Massnahmen zum Schutz personenbezogener Daten | Alle Verarbeitung personenbezogener Daten der [Organisation] |
| **EU DSGVO** | Technische und organisatorische Massnahmen (Art. 32) | Bei Verarbeitung EU-personenbezogener Daten |
| **ISO/IEC 27001:2022** | Controls A.8.20, A.8.21, A.8.22 | Zertifizierungs-Scope |

**Tier 2: Conditional Applicability**

| Regulation | Anforderung | Trigger-Bedingung |
|------------|-------------|-------------------|
| **PCI DSS** | Netzwerk-Segmentierung (Req. 1), sichere Netzwerk-Services | Verarbeitung von Payment Card Data |
| **FINMA** | Netzwerksicherheits-Kontrollen für Finanzinstitutionen | Schweizer Finanzdienstleistungs-Operationen |
| **DORA** | ICT-Netzwerksicherheit und Resilienz | EU-Finanzdienstleistungs-Operationen |
| **NIS2** | Netzwerksicherheits-Massnahmen für essentielle/wichtige Entities | Critical Infrastructure Designation |

**Tier 3: Informational Guidance**

Best-Practice-Frameworks referenziert, aber keine obligatorischen Compliance-Anforderungen:
- ISO/IEC 27033 (Network Security)
- NIST CSF (Cybersecurity Framework)
- CIS Controls (Network Device Hardening Benchmarks)

**United States Federal Requirements**: Referenzen auf US Federal Frameworks (FISMA, FIPS, FedRAMP, NIST Cybersecurity Requirements) gelten nur, wo [Organisation] explizite US Federal vertragliche Verpflichtungen hat, wie definiert in ISMS-POL-00.

**Compliance-Bestimmung**: Legal/Compliance Officer bestimmt Anwendbarkeit von Tier 2 Regulations basierend auf Geschäftsaktivitäten und regulatorischem Status der [Organisation].

---

## 2. Requirements Framework

### 2.1 Netzwerkinfrastruktur-Sicherheit (A.8.20)

[Organisation] MUSS folgende Netzwerkinfrastruktur-Sicherheits-Kontrollen implementieren:

| Anforderungs-Kategorie | Obligatorische Kontrollen | Implementierungs-Referenz |
|------------------------|---------------------------|---------------------------|
| **Netzwerk-Topologie-Dokumentation** | Aktuelle Netzwerk-Diagramme pflegen (physisch, logisch, Security Views); Dokumentation aktualisieren basierend auf organisatorischem Change Management | ISMS-IMP-A.8.20-21-22-S2 |
| **Netzwerkgeräte-Inventar** | Umfassendes Inventar aller Netzwerkgeräte mit Ownership, Criticality, Compliance-Status; Aktualisiert durch automatisierte Discovery | ISMS-IMP-A.8.20-21-22-S1 |
| **Device Hardening** | Default Credentials deaktivieren; Unnötige Services entfernen; Sichere Konfigurationen implementieren gemäss CIS Benchmarks oder Vendor Hardening Guides | ISMS-IMP-A.8.20-21-22-S3 |
| **Perimeter Controls** | Firewalls an Netzwerk-Perimeter; IPS/IDS für Threat Detection; DDoS-Protection für internet-facing Services | ISMS-IMP-A.8.20-21-22-S3 |
| **Network Access Controls** | Industry-Standard Network Access Control Mechanismen; Port Security auf Switches; Authentication-basierte Access Control | ISMS-IMP-A.8.20-21-22-S3 |
| **Monitoring & Logging** | Alle Netzwerkgeräte loggen zu zentralisiertem System; Netzwerk-Traffic-Analyse; SIEM-Integration für Korrelation | ISMS-IMP-A.8.20-21-22-S6 |
| **Configuration Management** | Configuration Baselines; Change Control für Configuration Changes; Automatisierte Backups gemäss Implementierungs-Leitlinien | ISMS-IMP-A.8.20-21-22-S3 |
| **Wireless Security** | Starke Verschlüsselung und Authentifizierung; Rogue AP Detection; Guest Network Isolation | ISMS-IMP-A.8.20-21-22-S3 |
| **Remote Access Security** | VPN mit MFA; Split-Tunnel-Policies; Session Logging und Monitoring | ISMS-IMP-A.8.20-21-22-S3 |

**Implementierungs-Hinweis**: Spezifische technische Standards (Cipher Suites, Protokoll-Versionen, Konfigurations-Parameter) sind in ISMS-IMP-A.8.20-21-22 Implementierungs-Leitlinien definiert und können ohne Richtlinienrevision aktualisiert werden.

**Cloud-Anwendbarkeit**: Cloud-Netzwerksicherheit (AWS VPC, Azure VNet, GCP VPC) MUSS äquivalente Kontrollen implementieren unter Verwendung cloud-nativer Capabilities (Security Groups, Network ACLs, Virtual Firewalls, Cloud Monitoring). Siehe ISMS-IMP-A.8.20-21-22-S3 für cloud-spezifische Leitlinien.

### 2.2 Netzwerk-Services-Sicherheit (A.8.21)

[Organisation] MUSS folgende Netzwerk-Services-Sicherheits-Kontrollen implementieren:

| Service-Typ | Obligatorische Sicherheits-Mechanismen | Implementierungs-Referenz |
|-------------|----------------------------------------|---------------------------|
| **DNS** | Industry-Standard DNS-Sicherheits-Mechanismen; Split DNS Architektur; DNS Query Logging; DNS Filtering für malicious Domains; DDoS-Protection für öffentliches DNS | ISMS-IMP-A.8.20-21-22-S4 |
| **DHCP** | DHCP-Sicherheits-Mechanismen auf Switches; Rogue DHCP Detection; Dokumentierte Scopes mit periodischer Review; High Availability für kritische DHCP Services | ISMS-IMP-A.8.20-21-22-S4 |
| **NTP** | NTP-Authentifizierungs-Mechanismen; Dokumentierte Time Source Hierarchie; Access Control Restrictions; Time Synchronization Monitoring | ISMS-IMP-A.8.20-21-22-S4 |
| **Proxy Services** | Authentifizierung erforderlich; SSL/TLS Interception (falls anwendbar); Umfassendes Logging; Bypass Prevention | ISMS-IMP-A.8.20-21-22-S4 |
| **Load Balancers** | SSL/TLS Termination mit starken Ciphers; Session Management; DDoS Protection; Health Check Monitoring | ISMS-IMP-A.8.20-21-22-S4 |
| **Authentication Services** | RADIUS/TACACS+ mit MFA Support; AAA Logging; Verschlüsselte Kommunikation; Redundanz für kritische Authentifizierung | ISMS-IMP-A.8.20-21-22-S4 |
| **Alle Netzwerk-Services** | Services-Katalog gepflegt; Service-spezifisches Monitoring; Availability SLA definiert; Hardening gemäss Vendor-Leitlinien; Reguläres Patching | ISMS-IMP-A.8.20-21-22-S1, S4 |

**Service-Availability-Anforderungen**: Kritische Netzwerk-Services MÜSSEN Availability SLA (Service Level Agreement) definieren basierend auf Business-Anforderungen und operationalem Kontext.

**Implementierungs-Hinweis**: Service-spezifische Sicherheits-Konfigurationen sind in ISMS-IMP-A.8.20-21-22-S4 dokumentiert und können basierend auf Threat Intelligence ohne Richtlinienrevision aktualisiert werden.

**Cloud-Anwendbarkeit**: Cloud-bereitgestellte Netzwerk-Services (Route 53, Azure DNS, Cloud Load Balancing) MÜSSEN äquivalente Sicherheits-Mechanismen implementieren unter Verwendung cloud-nativer Capabilities. Siehe ISMS-IMP-A.8.20-21-22-S4 für cloud-spezifische Leitlinien.

### 2.3 Netzwerk-Segmentierung (A.8.22)

[Organisation] MUSS folgende Netzwerk-Segmentierungs-Kontrollen implementieren:

| Anforderungs-Kategorie | Obligatorische Kontrollen | Implementierungs-Referenz |
|------------------------|---------------------------|---------------------------|
| **Security Zones** | Security Zones definieren und dokumentieren; Trust Levels zuweisen (Untrusted, Semi-Trusted, Trusted); Zonen-Zweck, Netzwerke, VLANs, erlaubte Traffic Flows dokumentieren | ISMS-IMP-A.8.20-21-22-S5 |
| **Segmentierungs-Architektur** | Minimum Zones: DMZ, Internal, Management, Guest; Zusätzliche Zones basierend auf Datenklassifizierung und regulatorischen Anforderungen (Server, Development, OT/ICS, Cloud) | ISMS-IMP-A.8.20-21-22-S5 |
| **VLAN-Segregation** | VLANs für logische Segmentierung; VLAN-Sicherheits-Mechanismen; VLAN-to-Zone Mapping dokumentiert | ISMS-IMP-A.8.20-21-22-S5 |
| **Inter-Zone Traffic Controls** | Firewalls oder ACLs an Trust Boundaries; Default Deny Policy (explizit Allow nur); Stateful Inspection für allen Inter-Zone Traffic; Traffic Flow Dokumentation | ISMS-IMP-A.8.20-21-22-S5 |
| **Trust Boundaries** | Trust Boundaries zwischen Zones definieren; Controls an jeder Boundary durchsetzen; Denied Traffic loggen; Reguläre Firewall Rule Review | ISMS-IMP-A.8.20-21-22-S5 |
| **Segmentierungs-Testing** | Periodisches Segmentierungs-Effectiveness-Testing; VLAN-Security-Testing; Traffic Flow Verification; Penetration Testing von Inter-Zone Controls | ISMS-IMP-A.8.20-21-22-S6 |
| **Flat Network Remediation** | Flat Networks (keine Segmentierung) identifizieren; Risk Assessment von Flat Networks; Remediation Plan basierend auf Risk-Priorisierung | ISMS-IMP-A.8.20-21-22-S5 |
| **Microsegmentation** | Application-Level-Segmentierung für High-Security-Anforderungen (SOLLTE); Zero Trust Network Approaches wo anwendbar | ISMS-IMP-A.8.20-21-22-S5 |

**Default Deny Principle**: Aller Inter-Zone Traffic MUSS standardmässig blockiert sein. Nur explizit genehmigte Traffic Flows erlaubt. Jede Permit Rule MUSS dokumentierte Business-Justifikation haben.

**Firewall Rule Justifikations-Dokumentation**:

Business-Justifikation für alle Inter-Zone Permit Rules ist dokumentiert mittels folgender Mechanismen:

- **Neue Rules**: Firewall Rule Change Request (Template in ISMS-IMP-A.8.20-21-22-S5) komplettiert und genehmigt vor Implementierung
- **Existierende Rules**: Business-Justifikation aufgezeichnet in Network Segmentation Matrix (Workbook 4) während periodischer Firewall Rule Review
- **Emergency Rules**: Dokumentiert innerhalb 48 Stunden nach Implementierung gemäss Incident Response Procedures

Rules ohne dokumentierte Business-Justifikation, die während Review identifiziert werden, müssen entweder gerechtfertigt und dokumentiert oder entfernt werden innerhalb eines Zeitrahmens proportional zur Trust Boundary Criticality. Für kritische Trust Boundaries sollte Resolution 7 Tage nicht überschreiten; für andere Boundaries 30 Tage.

**Implementierungs-Hinweis**: Spezifische VLAN-Assignments, Subnet-Designs und Firewall Rule Templates sind in ISMS-IMP-A.8.20-21-22-S5 dokumentiert und können basierend auf Architektur-Änderungen ohne Richtlinienrevision aktualisiert werden.

**Cloud-Anwendbarkeit**: Cloud-Netzwerk-Segmentierung (VPCs, VNets, Subnets, Security Groups, Network ACLs) MUSS äquivalente Kontrollen implementieren. Public Cloud Flat Networks (einzelne VPC ohne interne Segmentierung) MÜSSEN remediiert werden gemäss Risk Assessment. Siehe ISMS-IMP-A.8.20-21-22-S5 für cloud-spezifische Leitlinien.

---

## 3. Governance & Operations

### 3.1 Rollen & Verantwortlichkeiten

**Chief Information Security Officer (CISO)**:
- Richtlinien-Owner und ultimative Verantwortlichkeit für Netzwerksicherheits-Kontrollen
- Genehmigung von Netzwerksicherheits-Anforderungen und Risk Treatment Entscheidungen
- Genehmigung von Exceptions zu Netzwerksicherheits-Anforderungen
- Reporting Netzwerksicherheits-Posture an Executive Management
- Sicherstellung adäquater Ressourcen für Netzwerksicherheits-Implementierung

**Chief Information Officer (CIO) / IT Director**:
- Operationale Verantwortlichkeit für Netzwerkinfrastruktur und Services
- Ressourcen-Allokation für Netzwerksicherheits-Implementierung
- Sicherstellung, dass Netzwerk-Änderungen Sicherheits-Anforderungen folgen
- Genehmigung von Netzwerk-Architektur- und Design-Änderungen

**Network Operations Manager**:
- Technische Verantwortlichkeit für Netzwerksicherheits-Implementierung
- Management von Netzwerksicherheits-Konfigurationen und Changes
- Koordination mit Security Team zu Sicherheits-Anforderungen
- Sicherstellung von Netzwerk-Team Training und Kompetenz
- Pflege von Netzwerk-Dokumentation und Topologie-Diagrammen

**Network Administrators**:
- Implementierung von Netzwerksicherheits-Kontrollen auf Geräten und Services
- Befolgen von Device Hardening Procedures und sicheren Konfigurationen
- Implementierung von Firewall Rules und ACLs gemäss genehmigten Anforderungen
- Monitoring von Netzwerkgeräten und Response auf Alerts
- Dokumentation von Netzwerk-Änderungen und Pflege von Configuration Backups

**Security Team / Information Security Manager**:
- Definition von Netzwerksicherheits-Anforderungen basierend auf Risk Assessment
- Durchführung von Netzwerksicherheits-Assessments (unter Verwendung von Assessment Workbooks)
- Review und Genehmigung von Firewall Rule Changes
- Monitoring von Netzwerksicherheits-Events via SIEM
- Durchführung von Segmentierungs-Effectiveness-Testing
- Reporting Compliance-Status und Gaps

**Cloud Administrators** (falls anwendbar):
- Implementierung von Cloud-Netzwerksicherheits-Kontrollen (Security Groups, NACLs, etc.)
- Sicherstellung, dass Cloud-Netzwerke äquivalente Sicherheits-Anforderungen erfüllen
- Koordination mit Netzwerk-Team zu Hybrid-Netzwerk-Integration
- Dokumentation von Cloud-Netzwerk-Architektur

**System Owners**:
- Definition von Netzwerk-Access-Anforderungen für ihre Systeme
- Sicherstellung, dass Systeme Netzwerksicherheits-Richtlinien erfüllen
- Koordination mit Netzwerk-Team zu Segmentierungs-Anforderungen
- Teilnahme an Incident Response für ihre Systeme

**Legal/Compliance Officer**:
- Bestimmung regulatorischer Anwendbarkeit (Tier 2 Anforderungen)
- Sicherstellung, dass Netzwerksicherheits-Kontrollen regulatorische Anforderungen erfüllen
- Review von Netzwerksicherheit für Compliance mit Datenschutz-Gesetzen

**Verantwortlichkeits-Matrix**:

| Aktivität | CISO | CIO/IT Director | Network Ops Mgr | Network Admins | Security Team | Cloud Admins |
|-----------|------|-----------------|-----------------|----------------|---------------|--------------|
| Richtlinien-Genehmigung | A | C | C | I | C | I |
| Anforderungs-Definition | A | C | C | I | R | I |
| Netzwerk-Architektur | A | A | R | C | C | C |
| Device Hardening | A | A | R | R | C | R |
| Segmentierungs-Implementierung | A | A | R | R | C | R |
| Firewall Rule Changes | C | C | R | R | A | R |
| Security Assessments | A | I | C | I | R | C |
| Exception Genehmigung | A | C | C | I | C | I |
| Incident Response | A | A | R | R | R | R |

*R=Responsible (Durchführungsverantwortung), A=Accountable (Rechenschaftspflicht), C=Consulted (Konsultiert), I=Informed (Informiert)*

### 3.2 Monitoring & Reporting

**Continuous Monitoring**:
- Netzwerksicherheits-Kontrollen überwacht durch automatisierte und manuelle Mechanismen
- Netzwerkgeräte-Logs überwacht via zentralisiertes Logging-System
- Netzwerk-Traffic analysiert für Security-Anomalien
- Security Events triggern Alerts und Incident Response Procedures

**Periodisches Reporting**:
- Netzwerksicherheits-Compliance periodisch bewertet
- Netzwerk-Discovery und Inventar aktuell gehalten
- Firewall Rules und ACLs regulär reviewt
- Umfassende Netzwerksicherheits-Assessments durchgeführt
- Segmentierungs-Effectiveness validiert durch Testing
- Netzwerk-Architektur-Dokumentation reviewt und aktualisiert

**Metriken und Performance-Indikatoren**:
- Netzwerksicherheits-Compliance-Metriken definiert in Assessment Framework
- Key Performance Indicators (KPIs) dokumentiert in Implementierungs-Leitlinien
- Targets und Thresholds etabliert basierend auf organisatorischer Risk-Toleranz
- Gap-Remediation priorisiert basierend auf Risk Assessment
- Trend-Analyse durchgeführt zur Identifikation von Security-Verbesserungen

**Netzwerksicherheits-Performance-Targets**:

| Metrik | Target | Mess-Frequenz | Eskalations-Threshold |
|--------|--------|---------------|----------------------|
| Network Device Hardening Compliance | ≥95% | Vierteljährlich | <90% triggert Remediation Plan |
| Network Device Inventar-Genauigkeit | ≥98% | Vierteljährlich | <95% triggert Discovery Review |
| Firewall Rule Review Completion | 100% innerhalb Review Cycle | Gemäss definiertem Review Cycle | Jede überfällige Review eskaliert zu CISO |
| Segmentierungs-Effectiveness Test Pass Rate | 100% kritische Zones | Jährlich minimum | Jedes Critical Zone Failure triggert sofortige Remediation |
| Netzwerk-Services Availability (kritisch) | ≥99.9% | Monatlich | <99.5% triggert Incident Review |
| Mean Time to Patch Critical Vulnerabilities (Netzwerkgeräte) | ≤14 Tage | Monatlich | >30 Tage triggert Exception Request |
| Exception Backlog | ≤5 aktive Exceptions | Vierteljährlich | >10 triggert Executive Review |

**Metrik-Governance**: Detaillierte Metrik-Definitionen, Collection Methods und Trending-Analyse dokumentiert in ISMS-IMP-A.8.20-21-22-S6. Targets jährlich reviewt und adjustiert basierend auf organisatorischer Risk-Toleranz und operationaler Maturität.

**Reporting-Audience**:
- **Executive Management**: Executive Summary von Netzwerksicherheits-Posture, kritische Risiken, strategische Initiativen
- **CISO**: Detaillierte Compliance Reports, Security Event Summaries, Gap-Analyse
- **IT Management**: Operational Metriken, Service Availability, Infrastructure Status
- **Auditoren**: Zugang zu Assessment Workbooks, Evidence und Compliance-Dokumentation

### 3.3 Exception Management

**Exception Request Prozess**:

Wenn Netzwerksicherheits-Anforderungen nicht erfüllt werden können aufgrund technischer, operationaler oder Business-Constraints, gilt formaler Exception-Prozess:

1. **Exception Request**: Eingereicht von System Owner oder Network Operations Manager
2. **Risk Assessment**: Security Team evaluiert Sicherheitsrisiko der Exception
3. **Compensating Controls**: Alternative Controls identifizieren zur Risiko-Mitigation (falls möglich)
4. **Business-Justifikation**: Business-Need und Impact von Non-Exception dokumentieren
5. **Genehmigung**: CISO genehmigt/lehnt Exception ab basierend auf Risk-Toleranz
6. **Time Limit**: Exceptions gewährt für maximum 12 Monate (erneuerbar)
7. **Monitoring**: Exceptions vierteljährlich reviewt; Compensating Controls verifiziert
8. **Remediation Plan**: Erforderlich für alle Exceptions (Timeline zur Compliance-Erreichung)

**Exception-Genehmigungs-Autorität**:
- **Low Risk**: Information Security Manager
- **Medium Risk**: CISO
- **High Risk**: CISO + CIO (gemeinsame Genehmigung)
- **Critical Risk**: CISO + Executive Management

**Exception-Dokumentation**:
- Exception ID und Datum
- Anforderung(en) nicht erfüllt
- Risk Assessment Resultate
- Implementierte Compensating Controls
- Business-Justifikation
- Genehmigungs-Kette
- Ablaufdatum
- Remediation Plan und Timeline

**Häufige Exception-Szenarien**:
- Legacy-Systeme unfähig moderne Authentifizierung zu unterstützen (z.B. 802.1X)
- Cloud-Provider-Limitationen verhindern spezifische Control-Implementierung
- Temporäre Exception während Migration oder Major Project
- Operationaler Impact überwiegt Security-Benefit (mit Compensating Controls)

**Exception-Ablehnung**: Falls Exception Request abgelehnt wird, System/Netzwerk MUSS in Compliance gebracht oder dekommissioniert werden basierend auf Risk Assessment.

**Referenz**: Detaillierte Exception Procedures in ISMS-IMP-A.8.20-21-22-S6.

### 3.4 Incident Response

**Netzwerksicherheits-Incidents** (diese Richtlinie triggernd):
- Unauthorisierter Zugang zu Netzwerkgeräten oder Management-Interfaces
- Netzwerkgeräte-Compromise (Malware, Backdoor, unauthorisierte Änderungen)
- Netzwerk-basierte Angriffe (DDoS, ARP Poisoning, VLAN Hopping, Man-in-the-Middle)
- Netzwerk-Service-Compromise (DNS Poisoning, Rogue DHCP, NTP Attacks)
- Segmentierungs-Bypass oder Flat Network Exploitation
- Configuration Tampering oder unauthorisierte Firewall Rule Changes
- Netzwerk-Traffic-Anomalien indizierend Data Exfiltration oder Lateral Movement

**Incident-Severity-Klassifikation**:

| Severity | Definition | Scope-Indikatoren | Daten-Impact | Service-Impact |
|----------|------------|-------------------|--------------|----------------|
| **Low** | Begrenztes Issue mit minimalem Security-Impact | Einzelnes Gerät oder User betroffen | Keine Daten-Exposition bestätigt | Keine Service-Degradation |
| **Medium** | Potential für Spread oder Eskalation; erfordert prompte Attention | Multiple Geräte oder einzelnes Netzwerksegment betroffen | Potentielle Daten-Exposition; keine Bestätigung | Minor Service-Degradation (<10% Users) |
| **High** | Aktive Bedrohung oder bestätigter unauthorisierter Zugang erfordert dringende Response | Multiple Segmente betroffen oder kritische Systeme targeted | Bestätigte Daten-Exposition (limitierter Scope) oder Zugang zu sensitiven Systemen | Signifikante Service-Degradation (10-50% Users) |
| **Critical** | Schwerer Incident mit organisationsweitem Impact oder aktiver Data Exfiltration | Netzwerkweiter Impact oder Management-Infrastruktur kompromittiert | Aktive Data Exfiltration oder Exposition hochsensitiver Daten | Major Service-Disruption (>50% Users) |

**Severity-Beispiele (Netzwerksicherheit)**:

| Severity | Beispiel-Szenarien |
|----------|--------------------|
| **Low** | Failed Authentication Attempts auf einzelnem Netzwerkgerät; minor Configuration Drift detektiert; einzelner Rogue AP detektiert und containiert |
| **Medium** | Fehlkonfigurierte Firewall Rule erlaubt unbeabsichtigten Traffic (keine Exploitation bestätigt); VLAN-Fehlkonfiguration betrifft non-kritisches Segment; Netzwerk-Service-Degradation durch Capacity-Issue |
| **High** | Kompromittiertes Netzwerkgerät mit Evidence von Reconnaissance; erfolgreicher VLAN Hopping Attempt; unauthorisierter Zugang zu Network Management Interface; Segmentierungs-Bypass bestätigt |
| **Critical** | Netzwerkgeräte-Compromise betrifft kritische Infrastruktur; aktives Lateral Movement across Segments; Compromise von zentralisierter Authentifizierung (RADIUS/TACACS+); netzwerkweites DDoS mit sustained Impact; Evidence von Data Exfiltration via Netzwerk-Channels |

**Incident Response Prozess**:

1. **Detection**: Incident detektiert via Monitoring, Alerts oder User Report
2. **Triage**: Security Team bewertet Severity und Impact
3. **Containment**: Sofortige Aktionen zur Schadens-Limitierung (isoliere kompromittiertes Device/Segment, blockiere Traffic, deaktiviere kompromittierte Accounts)
4. **Investigation**: Root Cause, Scope und Impact bestimmen unter Verwendung von Logs und Network Forensics
5. **Eradication**: Bedrohung entfernen (patche Vulnerabilities, restore Configurations, rebuilde kompromittierte Devices)
6. **Recovery**: Rückkehr zu normalem Betrieb mit enhanced Monitoring
7. **Post-Incident**: Lessons Learned, update Security Controls, improve Detection

**Eskalations-Anforderungen**:

| Severity | Initial Response | Notification Timeline | Notification Recipients |
|----------|-----------------|---------------------|------------------------|
| **Low** | Network/Security Team handhabt | Innerhalb 24 Stunden | Network Operations Manager |
| **Medium** | Network/Security Team handhabt mit Management Awareness | Innerhalb 4 Stunden | Network Operations Manager, Information Security Manager |
| **High** | Incident Response Team engaged | Innerhalb 1 Stunde | CISO, CIO, Network Operations Manager |
| **Critical** | Full Incident Response Activation | Sofort | CISO, CIO, Executive Management, Legal/Compliance (bei Data Breach) |

**Severity-Eskalation**: Incidents können zu höherer Severity eskaliert werden falls:
- Scope expandiert über initial Assessment hinaus
- Daten-Impact bestätigt oder erhöht
- Containment-Massnahmen erweisen sich als ineffektiv
- Dauer überschreitet erwartete Resolution Time

**Incident Logging**: Alle Netzwerksicherheits-Incidents geloggt in Incident Management System mit Timeline, Actions Taken, Root Cause und Remediation.

**Referenz**: Detaillierte Incident Response Procedures im organisatorischen Incident Response Plan und ISMS-IMP-A.8.20-21-22-S6.

### 3.5 Richtlinien-Governance

**Richtlinien-Review**:
- **Frequenz**: Jährlicher Review-Cycle
- **Trigger**: Regulatorische Änderungen, signifikante Security-Incidents, Technologie-Änderungen, organisatorische Änderungen, Audit-Findings
- **Reviewer**: CISO (primär), CIO, Network Operations Manager, Legal/Compliance Officer
- **Genehmigung**: Executive Management (finale Autorität)

**Implementation Standards Review** (separater Lifecycle von Richtlinie):
- **Frequenz**: Vierteljährlich oder bei Bedarf für Technologie-Updates
- **Scope**: ISMS-IMP-A.8.20-21-22 Implementierungs-Leitlinien (technische Standards, Procedures, Configurations)
- **Autorität**: CISO genehmigt Implementation Standard Updates ohne Richtlinienrevision zu erfordern
- **Rationale**: Trennt stabile Governance (Richtlinie) von evolvierenden technischen Details (Implementation Standards)

**Richtlinien-Updates**:

**Minor Updates** (keine materielle Änderung zu Anforderungen):
- Typographische Korrekturen, Formatierung, Klarstellungen
- Aktualisierte Referenzen zu anderen Dokumenten
- Aktualisierte regulatorische Referenzen (keine neuen Anforderungen)
- Genehmigung: CISO
- Notification: Update Versionsnummer (z.B. 1.0 → 1.1)

**Major Updates** (materielle Änderung zu Anforderungen):
- Neue Sicherheits-Anforderungen oder Controls
- Änderungen zu Rollen/Verantwortlichkeiten
- Änderungen zu Exception-Genehmigungs-Autorität
- Scope-Änderungen
- Genehmigung: Executive Management (volle Genehmigungs-Kette)
- Notification: Update Versionsnummer (z.B. 1.0 → 2.0)
- Kommunikation: Notification an alle Stakeholder, Training falls erforderlich

**Emergency Updates** (dringendes Sicherheitsrisiko):
- Kritische Vulnerability oder Bedrohung erfordert sofortige Richtlinien-Änderung
- Regulatorisches Mandat erfordert sofortige Compliance
- Genehmigung: CISO (mit Executive Management Notification innerhalb 24 Stunden)
- Notification: Sofortige Kommunikation an betroffene Parteien
- Formalisierung: Retroaktive Genehmigung bei nächster Richtlinien-Review

**Kommunikation**:
- Richtlinien-Updates kommuniziert via Email an alle betroffenen Stakeholder
- Aktualisierte Richtlinie publiziert auf internem Richtlinien-Portal
- Training bereitgestellt falls Richtlinien-Änderungen operationale Procedures betreffen
- Obsolete Versionen klar markiert und entfernt aus Zirkulation

---

## 4. Implementierung & Referenzen

### 4.1 Integration mit ISMS

**ISO/IEC 27001:2022 Clause 6.1 - Risk Assessment**:

Netzwerksicherheits-Kontrollen implementiert basierend auf Risk Assessment der [Organisation]:
- Netzwerkinfrastruktur-Risiken (A.8.20) identifiziert und bewertet
- Netzwerk-Services-Risiken (A.8.21) identifiziert und bewertet
- Netzwerk-Segmentierungs-Risiken (A.8.22) identifiziert und bewertet
- Risk Treatment Entscheidungen dokumentieren welche Controls implementiert werden und auf welchem Level

**ISO/IEC 27001:2022 Clause 6.1.3 - Statement of Applicability**:

Diese Richtlinie unterstützt folgende SoA-Einträge:

| Control | Status | Justifikation | Implementierung |
|---------|--------|---------------|-----------------|
| **A.8.20 - Networks Security** | ☑ Anwendbar | [Organisation] betreibt Netzwerkinfrastruktur, die Sicherheits-Kontrollen erfordert | Abschnitt 2.1, ISMS-IMP-A.8.20-21-22 |
| **A.8.21 - Security of Network Services** | ☑ Anwendbar | [Organisation] betreibt kritische Netzwerk-Services, die Sicherheits-Kontrollen erfordern | Abschnitt 2.2, ISMS-IMP-A.8.20-21-22 |
| **A.8.22 - Segregation of Networks** | ☑ Anwendbar | [Organisation] erfordert Netzwerk-Segmentierung zur Risiko-Limitierung und zur Erfüllung regulatorischer Anforderungen | Abschnitt 2.3, ISMS-IMP-A.8.20-21-22 |

**Verwandte Controls** (Integrations-Punkte):

**A.8.15 - Logging**:
- Netzwerkgeräte generieren Security Logs
- Netzwerk-Services loggen kritische Events
- Logs zentralisiert in SIEM für Korrelation
- Integration: Netzwerkgeräte konfiguriert zu loggen gemäss A.8.15 Anforderungen

**A.8.16 - Monitoring Activities**:
- Netzwerk-Traffic überwacht für Anomalien (NetFlow/sFlow, IDS/IPS)
- Netzwerk-Services überwacht für Availability und Performance
- Security Events triggern Alerts
- Integration: Netzwerk-Monitoring integriert mit organisatorischem Monitoring Framework gemäss A.8.16

**A.8.8 - Technical Vulnerability Management**:
- Netzwerkgeräte gescannt für Vulnerabilities
- Firmware/Software gepatcht basierend auf Vulnerability Severity
- Integration: Netzwerkgeräte inkludiert in Vulnerability Management Scope gemäss A.8.8

**A.8.9 - Configuration Management**:
- Netzwerkgeräte-Konfigurationen baselined
- Configuration Changes kontrolliert via Change Management
- Configuration Backups automatisiert und getestet
- Integration: Netzwerk-Configurations gemanaged gemäss A.8.9 Anforderungen

**A.5.23 - Cloud Services**:
- Cloud-Netzwerksicherheit bewertet (AWS VPC, Azure VNet, GCP VPC)
- Hybrid-Netzwerk-Integration evaluiert
- Integration: Cloud Networking unterliegt dieser Richtlinie und bewertet gemäss A.5.23

**A.8.23 - Web Filtering**:
- Web Filtering implementiert unter Verwendung von Netzwerk-Controls (Proxy, DNS Filtering)
- Integration: Web Filtering Infrastruktur gesichert gemäss dieser Richtlinie

**A.8.1 - User Endpoint Devices**:
- Endpoint Network Access kontrolliert via 802.1X oder NAC
- Integration: Endpoint Network Access Policies durchgesetzt durch Netzwerk-Controls

### 4.2 Implementierungs-Ressourcen

**Implementierungs-Leitlinien** (ISMS-IMP-A.8.20-21-22):

| Dokument | Zweck | Scope |
|----------|-------|-------|
| **ISMS-IMP-A.8.20-21-22-S1** | Network Discovery Process | Automatisierte und manuelle Netzwerk-Discovery-Procedures; Tools und Methodologien; Discovery-Validation |
| **ISMS-IMP-A.8.20-21-22-S2** | Network Architecture Documentation | Topologie-Diagramm-Anforderungen; Dokumentations-Standards; Update-Procedures |
| **ISMS-IMP-A.8.20-21-22-S3** | Device Hardening Process | Gerätespezifische Hardening-Procedures; CIS Benchmark Anwendung; Configuration Templates; Wireless und VPN Security |
| **ISMS-IMP-A.8.20-21-22-S4** | Network Services Security Process | Service-by-Service Security-Implementierung (DNS, DHCP, NTP, Proxy, Load Balancers); Monitoring und Availability |
| **ISMS-IMP-A.8.20-21-22-S5** | Segmentation Implementation | Zonen-Design-Prozess; VLAN-Konfiguration; Firewall Rule Development; ACL-Implementierung; Cloud-Segmentierung |
| **ISMS-IMP-A.8.20-21-22-S6** | Network Security Testing | Segmentierungs-Effectiveness-Testing; Penetration Testing; VLAN Hopping Tests; Service Security Testing |

**Assessment Tools** (Python-generierte Excel Workbooks):

| Workbook | Zweck | Update-Frequenz |
|----------|-------|-----------------|
| **Workbook 1 - Network Infrastructure Inventory** | Geräte-Inventar mit Location, Ownership, Criticality, Compliance-Status | Gemäss Implementierungs-Leitlinien |
| **Workbook 2 - Network Device Security Assessment** | Device-by-Device Hardening Compliance, Gap-Identifikation | Gemäss Implementierungs-Leitlinien |
| **Workbook 3 - Network Services Catalog** | Services-Inventar mit Sicherheits-Mechanismen, Availability, Monitoring-Status | Gemäss Implementierungs-Leitlinien |
| **Workbook 4 - Network Segmentation Matrix** | Security Zones, Trust Relationships, Inter-Zone Policies, Effectiveness Tests | Gemäss Implementierungs-Leitlinien |
| **Workbook 5 - Security Controls Coverage** | Master Controls Matrix zeigend welche Controls welche Segmente schützen | Gemäss Implementierungs-Leitlinien |
| **Dashboard - Network Security Compliance** | Konsolidierte Compliance-View mit Metriken und Trends | Gemäss Implementierungs-Leitlinien |

**Unterstützende Materialien**:
- Netzwerk-Topologie-Diagramm-Templates
- CIS Benchmarks für Netzwerkgeräte
- Vendor Hardening Guides (Cisco, Juniper, Palo Alto, AWS, Azure, etc.)
- Firewall Rule Change Request Templates
- Segmentierungs-Effectiveness-Test-Procedures

### 4.3 Regulatorisches Mapping

**Regulatorische Anforderungs-Matrix**:

| Regulation | Spezifische Anforderungen | Implementierungs-Abschnitt | Evidence |
|------------|--------------------------|----------------------------|----------|
| **Schweizer nDSG** | Technische Massnahmen zum Schutz personenbezogener Daten; Access Controls; Logging | Abschnitt 2.1, 2.2, 2.3 | Netzwerksicherheits-Assessments, Logs, Segmentierungs-Dokumentation |
| **EU DSGVO (Art. 32)** | Technische Massnahmen inkl. Netzwerksicherheit; Access Controls; Verschlüsselung von Daten im Transit | Abschnitt 2.1, 2.2, 2.3 | Netzwerksicherheits-Assessments, Verschlüsselungs-Configs |
| **ISO 27001:2022** | A.8.20 Network Device Security; A.8.21 Network Services Security; A.8.22 Network Segmentation | Abschnitt 2.1, 2.2, 2.3 | Alle Assessment Workbooks |
| **PCI DSS (Req. 1)** | Firewall und Router Configuration Standards; Netzwerk-Segmentierung für Cardholder Data | Abschnitt 2.3 | Segmentation Matrix (Workbook 4), Firewall Configs |
| **FINMA** | Netzwerksicherheits-Kontrollen; Segregation von Environments; Monitoring | Abschnitt 2.1, 2.2, 2.3 | Netzwerksicherheits-Assessments, Monitoring Logs |
| **DORA** | Network und Information Systems Security; Network Segmentation | Abschnitt 2.1, 2.3 | Netzwerksicherheits-Assessments, Segmentierungs-Dokumentation |
| **NIS2** | Netzwerksicherheits-Massnahmen; Network Segmentation; Security Monitoring | Abschnitt 2.1, 2.2, 2.3 | Alle Assessment Workbooks, Monitoring Evidence |

**Compliance-Verification**: Regulatorische Compliance verifiziert durch:
- Vierteljährliche Netzwerksicherheits-Assessments
- Jährliche Internal Audits
- Externe Zertifizierungs-Audits (ISO 27001, branchenspezifisch)
- Regulatorische Examinations (FINMA, NIS2 Authorities als anwendbar)

### 4.4 Training & Awareness

**Security Awareness** (alle Mitarbeiter):
- **Audience**: Alle Angestellten, Auftragnehmer, Temporäres Personal
- **Content**: Netzwerk-Access-Policies; Acceptable Use; Incident Reporting; Social Engineering Awareness
- **Frequenz**: Jährliches Security Awareness Training
- **Delivery**: E-Learning Modules, obligatorische Completion
- **Verification**: Training Completion getrackt in HR-System

**Technisches Training** (IT/Security Personal):

**Network Administrators**:
- **Content**: Device Hardening Procedures; Sichere Configurations; Firewall Rule Management; VLAN Configuration; Wireless Security; VPN Security
- **Frequenz**: Jährlich, plus ad-hoc für neue Technologien oder Richtlinien-Updates
- **Delivery**: Hands-on Workshops, Vendor Training, interne Knowledge Transfer
- **Verification**: Competency Assessment, Certification Programs (z.B. CCNA Security, Netzwerk-Vendor-Zertifizierungen)

**Security Team**:
- **Content**: Netzwerksicherheits-Assessment-Methodologien; Segmentierungs-Effectiveness-Testing; Penetration Testing Techniques; Cloud Network Security; Security Monitoring und SIEM
- **Frequenz**: Jährlich, plus kontinuierliches Learning für emerging Threats
- **Delivery**: Security Conferences, spezialisierte Training Courses, Certification Programs
- **Verification**: Security Certifications (CISSP, GIAC, Vendor Security Certifications)

**Cloud Administrators**:
- **Content**: Cloud Network Security (AWS, Azure, GCP); Security Groups und NACLs; Cloud Monitoring; Hybrid Network Security
- **Frequenz**: Jährlich, plus Updates für neue Cloud Services
- **Delivery**: Cloud Vendor Training, Certification Programs (AWS Certified Security, Azure Security Engineer, etc.)
- **Verification**: Cloud Security Certifications

**Operationales Training** (IT Operations, Help Desk):
- **Content**: Netzwerksicherheits-Basics; Security-Incidents erkennen; Eskalations-Procedures; Change Management Procedures
- **Frequenz**: Jährlich
- **Delivery**: Interne Training Sessions, Dokumentations-Review
- **Verification**: Training Completion und Knowledge Checks

**Spezialisiertes Training** (bei Bedarf):
- Software-Defined Networking (SDN) Security
- Zero Trust Network Architecture
- Advanced Threat Detection und Response
- Network Forensics und Incident Investigation

---

## 5. Definitionen

**Periodische Aktivitäts-Frequenz-Standards**:

Sofern nicht explizit anders in dieser Richtlinie oder referenzierten Implementierungs-Leitlinien angegeben, gelten folgende Mindest-Frequenzen:

| Begriff | Mindest-Frequenz | Anwendbare Aktivitäten |
|---------|------------------|------------------------|
| **Continuous** | Real-time oder near-real-time automatisiertes Monitoring | Netzwerkgeräte-Monitoring, Traffic-Analyse, Security Event Logging |
| **Regular** | Monatlich | Patching Review, Configuration Backup Verification, Service Availability Review |
| **Periodic** | Vierteljährlich | Security Assessments, Inventar-Validation, Firewall Rule Review, Metriken-Reporting |
| **Annual** | Einmal pro Kalenderjahr (innerhalb 12 Monate vom vorherigen) | Segmentierungs-Effectiveness-Testing, Richtlinien-Review, umfassende Architektur-Review, Penetration Testing |

**Frequenz-Anpassungen**: Aktivitäts-Frequenzen können erhöht werden basierend auf:
- Risk Assessment Findings indizierend erhöhte Threat Levels
- Regulatorische Anforderungen mandatierend spezifische Frequenzen
- Audit Findings erfordern enhanced Monitoring
- Signifikante Änderungen zu Netzwerkinfrastruktur oder Threat Landscape

Frequenz-Reduktionen erfordern CISO-Genehmigung und dokumentierte Risk Acceptance.

**Schlüssel-Begriffe**:

**Defense in Depth**: Layered Security Approach verwendend multiple Sicherheits-Kontrollen auf verschiedenen Levels zum Schutz von Informationsassets. Im Netzwerksicherheits-Kontext: Perimeter Controls + Segmentierung + Device Hardening + Monitoring.

**DMZ (Demilitarized Zone)**: Netzwerksegment isoliert sowohl von internen Netzwerken als auch vom Internet, typischerweise hostend internet-facing Services (Web Server, Mail Relays, VPN Concentrators).

**Flat Network**: Netzwerk ohne Segmentierung - alle Systeme können mit allen anderen Systemen kommunizieren ohne Firewall oder ACL Controls. Gilt als High-Risk-Architektur.

**Microsegmentation**: Fine-grained Netzwerk-Segmentierung auf Application- oder Workload-Level, oft implementiert unter Verwendung von Software-Defined Networking oder Host-based Firewalls.

**NAC (Network Access Control)**: Technologie, die Sicherheits-Policies auf Geräten durchsetzt, die Netzwerk-Access suchen, typischerweise checkend Device-Compliance vor Erlaubnis von Netzwerk-Connectivity.

**SDN (Software-Defined Networking)**: Netzwerk-Architektur-Ansatz, der programmatische Netzwerk-Kontrolle ermöglicht durch Separation der Control Plane von der Data Plane.

**Security Zone**: Logisches oder physisches Netzwerksegment mit gemeinsamen Sicherheits-Anforderungen, Trust Level und Datenklassifizierung. Beispiele: DMZ, Internal, Management, Guest.

**Trust Boundary**: Netzwerk-Perimeter wo Trust Level ändert, erfordert Sicherheits-Kontrollen (Firewall, ACLs) zur Durchsetzung von Access Policies zwischen Zones.

**VLAN (Virtual Local Area Network)**: Logisches Netzwerksegment kreiert auf physischer Netzwerkinfrastruktur unter Verwendung von IEEE 802.1Q Standard, ermöglicht Netzwerk-Segregation ohne separate physische Netzwerke.

**Zero Trust Network**: Sicherheits-Modell annehmend kein implizites Vertrauen basierend auf Netzwerk-Location. Alle Access Requests verifiziert unabhängig von Source, emphasierend "never trust, always verify".

---

## Genehmigungs-Record

| Rolle | Name | Datum | Unterschrift |
|-------|------|-------|--------------|
| **Dokumenteneigentümer/in (CISO)** | [Name] | [Datum] | [Unterschrift] |
| **Technisches Review (CIO)** | [Name] | [Datum] | [Unterschrift] |
| **Technisches Review (Network Ops Mgr)** | [Name] | [Datum] | [Unterschrift] |
| **Compliance Review (Legal/Compliance)** | [Name] | [Datum] | [Unterschrift] |
| **Finale Genehmigung (Geschäftsleitung)** | [Name] | [Datum] | [Unterschrift] |

---

**ENDE DES DOKUMENTS**

**Dokumenten-Status**: Entwurf - Genehmigung ausstehend  
**Nächstes Review-Datum**: [Inkraftsetzungsdatum + 12 Monate]  
**Dokumenten-Location**: [Organisation] Internes Richtlinien-Portal

---