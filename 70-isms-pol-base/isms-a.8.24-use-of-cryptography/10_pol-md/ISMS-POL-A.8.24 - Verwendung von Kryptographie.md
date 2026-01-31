**ISMS-POL-A.8.24 — Verwendung von Kryptographie**

---

**Dokumentenlenkung**

| Feld | Wert |
|------|------|
| **Dokumenten Titel** | Verwendung von Kryptographie |
| **Dokumententyp** | Knozept |
| **Dokument-ID** | ISMS-POL-A.8.24 |
| **Ersteller/in** | Chief Information Security Officer (CISO) |
| **Dokumenteneigentümer/in** | Chief Executive Officer (CEO) |
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
- Compliance: Legal/Compliance Officer
- Finale Autorität: Geschäftsleitung (GL)



**Zugehörige Dokumente**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.24 (Implementation Guidance Suite)
- ISO/IEC 27001:2022 Control A.8.24



---

## Management Summary

Diese Richtlinie definiert die Anforderungen von [Organisation] für kryptographische Kontrollen zum Schutz der Vertraulichkeit, Integrität und Authentizität von Informationen gemäss ISO/IEC 27001:2022 Control A.8.24.

**Geltungsbereich**: Diese Richtlinie gilt für alle Informationsassets, Systeme und Mitarbeiter, die klassifizierte Informationen (Intern, Vertraulich oder Eingeschränkt) handhaben.

**Zweck**: Definition organisatorischer Anforderungen für Auswahl, Implementierung und Governance kryptographischer Kontrollen. Diese Richtlinie definiert WAS kryptographischer Schutz erforderlich ist und WER verantwortlich ist. Implementierungsprozeduren (WIE) sind separat in ISMS-IMP-A.8.24 dokumentiert.

**Regulatorisches Alignment**: Diese Richtlinie adressiert obligatorische Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatory Applicability Framework), einschliesslich Schweizer nDSG, EU DSGVO und ISO/IEC 27001:2022. Konditionale branchenspezifische Anforderungen (PCI DSS, FINMA, DORA, NIS2) gelten, wo Geschäftsaktivitäten der [Organisation] Anwendbarkeit auslösen.

---

**Control Alignment & Geltungsbereich**

**ISO/IEC 27001:2022 Control A.8.24**

**ISO/IEC 27001:2022 Annex A.8.24 - Use of Cryptography**

> *A policy on the use of cryptographic controls for protection of information should be developed and implemented.*

**Control-Zielsetzung**: Etablierung organisatorischer Richtlinie für kryptographische Kontrollen zum Schutz von Informationen während des gesamten Lebenszyklus.

**Diese Richtlinie adressiert**:

- Anforderungen an kryptographische Kontrollen basierend auf Datenklassifizierung
- Organisatorische Rollen und Verantwortlichkeiten für kryptographische Governance
- Frameworks für Exception Management und Incident Management
- Integration mit Risk Assessment und Treatment Prozessen der [Organisation]



## Was diese Richtlinie tut

Diese Richtlinie:

- **Definiert** Anforderungen an kryptographische Kontrollen ausgerichtet auf Datenklassifizierung
- **Etabliert** Governance-Framework für kryptographische Entscheidungsfindung
- **Spezifiziert** Verantwortlichkeit für Implementierung kryptographischer Kontrollen
- **Referenziert** anwendbare regulatorische Anforderungen gemäss ISMS-POL-00



## Was diese Richtlinie NICHT tut

Diese Richtlinie tut NICHT:

- **Spezifizieren technischer Implementierungsdetails** (siehe ISMS-IMP-A.8.24 Implementation Guides)
- **Definieren genehmigter Algorithmen oder Schlüssellängen** (siehe ISMS-IMP-A.8.24 Technical Standards)
- **Bereitstellen systemspezifischer Konfigurationsprozeduren** (siehe ISMS-IMP-A.8.24 Assessment Guides)
- **Ersetzen von Risk Assessment** (kryptographische Kontrollen werden basierend auf Risk Treatment der [Organisation] ausgewählt)



**Rationale**: Trennung von Richtlinienanforderungen und Implementierungsleitlinien ermöglicht:

- Richtlinienstabilität trotz sich entwickelnder kryptographischer Standards
- Technische Agilität für Algorithmus-Updates ohne Richtlinienrevision
- Klare Unterscheidung zwischen Governance (Richtlinie) und Execution (Implementierung)



## Geltungsbereich

**Diese Richtlinie gilt für**:

- Alle Informationsassets, die als Intern, Vertraulich oder Eingeschränkt klassifiziert sind
- Alle Systeme, Applikationen, Netzwerke und Services, die organisatorische Informationen verarbeiten
- Alle kryptographischen Implementierungen (Verschlüsselung, Hashing, digitale Signaturen, Key Management)
- Alle Mitarbeiter (Angestellte, Auftragnehmer, Drittparteien) mit Zugang zu organisatorischen Informationen
- Alle Drittanbieter-Services, die organisatorische Daten handhaben



**Nicht im Geltungsbereich**:

- Öffentliche Informationen (kein kryptographischer Schutz erforderlich)
- Nicht-kryptographische Sicherheitskontrollen (durch andere ISMS-Richtlinien abgedeckt)



## Regulatorische Anwendbarkeit

Regulatorische Anforderungen sind gemäss **ISMS-POL-00 (Regulatory Applicability Framework)** kategorisiert.

**Tier 1: Obligatorische Compliance**

| Regulierung | Anwendbarkeit | Hauptanforderungen |
|-------------|---------------|-------------------|
| **Schweizer nDSG** | Alle Schweizer Operationen | Art. 8 - Angemessene technische Massnahmen inkl. Verschlüsselung |
| **EU DSGVO** | Bei Verarbeitung personenbezogener Daten von EU-Bürgern | Art. 32 - Verschlüsselung personenbezogener Daten als Sicherheitsmassnahme |
| **ISO/IEC 27001:2022** | Zertifizierungsbereich | Control A.8.24 - Dokumentierte Richtlinie und Implementierung |

**Tier 2: Konditionale Anwendbarkeit**

Gelten nur, wenn spezifische Geschäftsbedingungen Anwendbarkeit auslösen:

| Regulierung | Auslöse-Bedingung | Kryptographische Anforderungen |
|-------------|-------------------|-------------------------------|
| **PCI DSS v4.0** | Verarbeitung von Zahlungskartendaten | Starke Kryptographie für Karteninhaberdaten, Key Management Kontrollen |
| **FINMA** | Schweizer regulierte Finanzinstitution | Verschlüsselung gemäss FINMA Rundschreiben 2023/1 Margin 62 |
| **DORA** | EU-Finanzdienstleistungs-Entität | ICT-System-Verschlüsselung, Crypto Agility |
| **NIS2** | Essenzielle/wichtige Entität (EU) | Verschlüsselung als Cybersecurity-Risikomassnahme |

**Tier 3: Informationsleitlinien**

Diese Frameworks informieren Implementierung, stellen aber keine obligatorische Compliance dar, sofern nicht vertraglich gefordert:

- NIST SP 800-57 (Key Management)
- BSI TR-02102 (Kryptographische Mechanismen)
- ENISA (Algorithms and Key Sizes)
- OWASP (Cryptographic Storage)



**Compliance-Bestimmung**: [Organisation] bestimmt anwendbare Tier 2 Regulierungen durch periodische Geschäftsaktivitäts-Assessments. Die strengsten Anforderungen gelten bei Überschneidung mehrerer Regulierungen.

---

# Framework für kryptographische Anforderungen

## Anforderungen basierend auf Datenklassifizierung

[Organisation] implementiert kryptographische Kontrollen basierend auf Datenklassifizierung gemäss ISMS-POL-A.5.12 (Informationsklassifizierung).

**Schutzanforderungen nach Klassifizierung**:

| Klassifizierung | Data in Transit | Data at Rest | Authentifizierung | Key Management |
|-----------------|-----------------|--------------|-------------------|----------------|
| **Öffentlich** | Nicht erforderlich | Nicht erforderlich | Standard | N/A |
| **Intern** | Empfohlen | Empfohlen | Standard | Standard |
| **Vertraulich** | **Erforderlich** | **Erforderlich** | Stark | Erweitert |
| **Eingeschränkt** | **Erforderlich (Stark)** | **Erforderlich (Stark)** | Stark + MFA | HSM/KMS Erforderlich |

**Implementierungs-Hinweis**: Spezifische kryptographische Algorithmen, Schlüssellängen und technische Konfigurationen sind in ISMS-IMP-A.8.24 Technical Standards definiert. [Organisation] pflegt technische Standards separat von der Richtlinie zur Ermöglichung kryptographischer Agilität.

## Kategorien kryptographischer Kontrollen

[Organisation] implementiert kryptographische Kontrollen in folgenden Kategorien:

**Data Transmission Protection**:

- Netzwerkkommunikations-Verschlüsselung (TLS/SSL mit Cipher Suites, die Perfect Forward Secrecy unterstützen wo technisch machbar, VPN, Wireless)
- Applikations-Level-Verschlüsselung (HTTPS, SFTP, Secure E-Mail)
- Datenbank-Verbindungs-Verschlüsselung
- API-Sicherheit



**Data Storage Protection**:

- Full Disk Encryption (mobile Geräte, Laptops)
- Datenbank-Verschlüsselung (Transparent Data Encryption, Column-Level)
- Backup-Verschlüsselung (Keys separat von Backup-Medien und Produktions-Keys gespeichert)
- Cloud Storage Verschlüsselung
- Wechselmedien-Verschlüsselung



**Authentifizierung & Identität**:

- Passwort-Hashing (keine Klartext-Speicherung)
- Multi-Faktor-Authentifizierungs-Mechanismen
- Digitale Signaturen
- Certificate-basierte Authentifizierung



**Key Management**:

- Kryptographischer Key-Lebenszyklus (Generierung, Speicherung, Verteilung, Rotation, Vernichtung)
- Key-Daten-Trennung
- Hardware Security Modules (HSM) oder Key Management Services (KMS) für hochsichere Keys



**Drittanbieter-Kryptographische-Anforderungen**: 
Drittanbieter-Services, die Vertrauliche oder Eingeschränkte Daten handhaben, müssen kryptographische Kontrollen nachweisen, die dieser Richtlinie entsprechen. "Verifizierung erfolgt während Lieferanten-Security-Assessment gemäss ISMS-POL-A.5.19 (Lieferantensicherheit). Vertragliche Anforderungen werden basierend auf Datenklassifizierung definiert.

**Implementierungsleitlinien**: Detaillierte Prozeduren für jede Kategorie sind dokumentiert in ISMS-IMP-A.8.24 Implementation Guides (Data Transmission, Data Storage, Authentication, Key Management).

## Kryptographische Agilität

Systeme der [Organisation] sollen so konzipiert sein, dass Algorithmus-Austausch ohne umfassende System-Neuarchitektur möglich ist.

**Anforderungen**:

- Kryptographische Algorithmen sollen konfigurierbar sein (nicht hardcodiert wo machbar)
- Systeme sollen mehrere Algorithmus-Versionen während Migrationsperioden unterstützen
- [Organisation] pflegt Algorithmus-Lebenszyklus-Zustände (Approved, Deprecated, Prohibited)
- Algorithmus-Deprecation löst formalen Migrationsprozess aus
- System Owners erhalten formale Notifikation minimum 180 Tage vor Algorithmus-Verbot zur Ermöglichung von Migrationsplanung. Kritische Systeme, die Eingeschränkte Daten unterstützen, erhalten 270-Tage-Vorlaufzeit.



**Rationale**: Kryptographische Standards entwickeln sich aufgrund von Kryptanalyse-Fortschritten, regulatorischen Änderungen und Post-Quantum-Kryptographie-Migration. Crypto-agile Systeme reduzieren Risiko und Kosten von Algorithmus-Transitionen.

**Prozess**: Algorithmus-Lifecycle-Management-Prozeduren sind definiert in ISMS-IMP-A.8.24 Technical Standards.

## Certificate Lifecycle Management

[Organisation] verwaltet TLS/SSL und andere digitale Zertifikate gemäss Industriestandards und Certificate Authority Anforderungen.

**Anforderungen**:

- Öffentlich zugängliche TLS-Zertifikate entsprechen CA/Browser Forum Baseline Requirements für Gültigkeitsperioden. Interne Zertifikats-Gültigkeitsperioden sind in ISMS-IMP-A.8.24 basierend auf Risikobewertung und operationellen Anforderungen definiert.
- Zertifikatserneuerungs-Prozesse angemessen zur Zertifikatsgültigkeitsdauer (automatisierte Erneuerung für kurzlebige Zertifikate)
- Zertifikatsablauf-Monitoring und Alerting
- Private Key Schutz
- Zertifikatsrevokations-Fähigkeit (OCSP/CRL)



**Industrie-Kontext**: Zertifikatsgültigkeits-Anforderungen ändern sich periodisch aufgrund von CA/Browser Forum Policy-Updates und Browser-Vendor-Anforderungen. [Organisation] monitort Industrie-Entwicklungen und passt Certificate Management Prozesse entsprechend an.

**Implementierung**: Certificate Management Prozeduren sind definiert in ISMS-IMP-A.8.24 Key Management Assessment.

## Verbotene Praktiken

Folgende Praktiken sind **streng verboten**:

- Klartext-Speicherung von Passwörtern oder kryptographischen Keys
- Verwendung kryptographisch gebrochener Algorithmen (MD5, DES, RC4 für Vertraulichkeit)
- Übertragung vertraulicher oder eingeschränkter Daten ohne Verschlüsselung
- Speicherung von Verschlüsselungs-Keys zusammen mit verschlüsselten Daten ohne Trennung
- Entwicklung eigener kryptographischer Algorithmen ohne kryptographische Expertise
- Umgehen oder Deaktivieren kryptographischer Kontrollen ohne formale Exception-Genehmigung



---

# Governance & Verantwortlichkeit

## Rollen & Verantwortlichkeiten

**Chief Information Security Officer (CISO)**:

- Richtlinien-Eigentümerschaft und strategische Ausrichtung
- Genehmigung kryptographischer Exceptions (technisch)
- Regulatorische Compliance-Überwachung
- Algorithmus-Deprecation-Autorität



**Information Security Manager**:

- Tägliche Richtlinien-Implementierungs-Koordination
- Technische Leitlinien für System Owners
- Assessment-Programm-Management
- Incident-Koordination



**System Owners**:

- Implementierung kryptographischer Kontrollen für ihre Systeme
- Risk Assessment Teilnahme
- Assessment- und Audit-Teilnahme
- Remediationsplan-Ausführung



**IT Security Team**:

- Technischer Implementierungs-Support
- Key Management Infrastruktur (HSM/KMS)
- Kryptographische Assessment-Ausführung
- Algorithmus-Monitoring



**Development Teams**:

- Sichere kryptographische Implementierung in Applikationen
- Verwendung genehmigter kryptographischer Libraries
- Security Code Review Teilnahme
- Schwachstellen-Remediation



**Legal/Compliance**:

- Regulatorische Anforderungs-Interpretation
- Externe Audit-Koordination
- Regulatorische Notifikation (bei Incidents)



**Key Ownership vs System Ownership**:

[Organisation] unterscheidet zwischen:

- **Key Owners**: Autorisieren Key-Erzeugung und definieren Key-Nutzungs-Policies (Governance)
- **Key Custodians**: Führen physisches Key Management aus (HSM-Administration, Key-Generierung)
- **System Owners**: Betreiben Systeme, die Keys verwenden (verwalten Keys nicht direkt)



Diese Trennung gewährleistet Verantwortlichkeit, Aufgabentrennung und klare Audit-Trails.

## Assessment & Compliance-Verifizierung

**Assessment-Ansatz**: [Organisation] führt kryptographische Control-Assessments durch unter Verwendung strukturierter Methodik, die folgendes abdeckt:

- Data Transmission Controls
- Data Storage Controls
- Authentifizierungs-Mechanismen
- Key Management Praktiken



**Assessment-Frequenz**:

- **Initial**: Innerhalb 90 Tagen nach Richtlinien-Genehmigung oder neuem System-Deployment
- **Regulär**: Jährlich Minimum
- **Triggered**: Nach signifikanten System-Änderungen, Security-Incidents oder Algorithmus-Deprecations



**Assessment-Tools**: [Organisation] verwendet ISMS-IMP-A.8.24 Assessment Workbooks zur systematischen Compliance-Verifizierung, Nachweis-Dokumentation und Remediation-Tracking.

**Non-Compliance Management**: Assessment-Findings werden nach Schweregrad klassifiziert (Critical, High, Medium, Low) mit definierten Remediations-Timelines. Lücken, die Risikoakzeptanz erfordern, folgen dem Exception-Prozess (Abschnitt 3.3).

## Exception Management

**Exception Request Anforderungen**:

Exceptions zu kryptographischen Richtlinienanforderungen erfordern:

- Dokumentierte geschäftliche oder technische Begründung
- Risk Assessment (Wahrscheinlichkeit, Impact, Restrisiko)
- Kompensierende Kontrollen (wo machbar)
- Timeline für Erreichung vollständiger Compliance
- Formale Genehmigung gemäss Autoritäts-Matrix



**Genehmigungs-Autorität**:

- **Technische Exceptions** (Algorithmus, Konfiguration): CISO-Genehmigung
- **Richtlinien-Level Exceptions** (Anforderungs-Verzicht): Geschäftsleitung-Genehmigung
- **Maximale Dauer**: 12 Monate
- **Erneuerung**: Erfordert aktualisiertes Risk Assessment und Begründung



**Monitoring**: Aktive Exceptions werden vierteljährlich vom CISO überprüft. Effektivität kompensierender Kontrollen wird verifiziert. Exceptions werden widerrufen, wenn sich Risikoprofil ändert oder kompensierende Kontrollen versagen.

**Exception Template**: ISMS-IMP-A.8.24 Exception Request Form stellt standardisiertes Dokumentations-Format bereit.

## Incident Response

**Kryptographische Incidents** beinhalten:

- Key-Kompromittierung oder Kompromittierungsverdacht
- Certificate Private Key Exposure
- Unautorisierten Zugriff auf verschlüsselte Daten
- Entdeckung verbotener Algorithmen in Produktion
- Kryptographische Control-Ausfälle



**Schweregrad-Klassifizierung**:

- **Critical**: Bestätigte Kompromittierung von Produktions-Verschlüsselungs-Keys, Certificate Private Keys oder HSM/KMS-Zugangsdaten. Response: 4 Stunden.
- **High**: Verdacht auf Key-Kompromittierung, Entdeckung verbotener Algorithmen für Vertrauliche/Eingeschränkte Daten oder kryptographischer Control-Ausfall, der mehrere Systeme betrifft. Response: 24 Stunden.
- **Medium**: Entdeckung veralteter Algorithmen, Zertifikatsablauf mit Service-Disruption oder isolierte Control-Ausfälle. Response: 48 Stunden.
- **Low**: Richtlinienabweichungen ohne aktive Ausnutzung, geringfügige Konfigurations-Abweichungen. Response: 72 Stunden.



Falls Response-Timelines nicht eingehalten werden können, Eskalation an CISO (für High/Medium/Low Schweregrad) oder CEO (für Critical Schweregrad) innerhalb des ursprünglichen Timeline-Fensters.

**Response-Prozess**:
1. **Detection & Reporting**: Sofortige Notifikation an IT Security Team
2. **Assessment**: Schweregrad-Bestimmung (Critical, High, Medium, Low)
3. **Containment**: Key-Rotations-Timeline basierend auf Schweregrad (4 Stunden bis 72 Stunden)
4. **Recovery**: Neue Key-Generierung, Daten-Re-Encryption, System-Updates
5. **Post-Incident**: Root Cause Analysis, präventive Massnahmen, regulatorische Notifikation (falls anwendbar)

**Detaillierte Prozeduren**: ISMS-IMP-A.8.24 Incident Response Guide stellt Incident-Klassifikationskriterien, Response-Workflows und regulatorische Notifikations-Anforderungen bereit.

## Richtlinien-Governance

**Richtlinien-Review**:

- **Frequenz**: Jährlich Minimum
- **Trigger**: Regulatorische Änderungen, Major Incidents, Algorithmus-Deprecations, CA/Browser Forum Baseline Changes, organisatorische Änderungen
- **Reviewer**: CISO, IT Security Team, Legal/Compliance, ausgewählte System Owners
- **Genehmigung**: CISO (technisch), Geschäftsleitung (strategisch)



**Technical Standards Review**:

- **Frequenz**: Halbjährlich (kryptographische Landschaft entwickelt sich schnell)
- **Autorität**: IT Security Team schlägt Updates vor, CISO genehmigt
- **Hinweis**: Technical Standard Updates (ISMS-IMP-A.8.24) erfordern keine Richtlinien-Revision



**Richtlinien-Updates**:

- **Minor** (Klarstellungen, Referenzen): CISO-Genehmigung, 30-Tage-Kommunikation
- **Major** (Scope-Änderungen, neue Anforderungen): Vollständige Freigabekette, 90-Tage-Implementierung
- **Emergency** (kritische Schwachstellen): CISO-Genehmigung, sofortige Kommunikation



**Kommunikation**: Richtlinie publiziert in ISMS-Dokumenten-Repository. Änderungen organisationsweit kommuniziert. Training für signifikante Änderungen bereitgestellt.

---

# Implementierung & Referenzen

## Integration mit ISMS

Diese Richtlinie integriert mit dem Informationssicherheits-Managementsystem der [Organisation]:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Kryptographische Kontrollen ausgewählt basierend auf Risk Assessment der [Organisation]
- Datenklassifizierung bestimmt minimale kryptographische Anforderungen
- Risk Treatment Plans dokumentieren kryptographische Control-Implementierung



**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Control A.8.24 Anwendbarkeit in SoA der [Organisation] begründet
- Implementierungs-Status getrackt und berichtet



**Zugehörige Controls**:

- A.5.10 (Acceptable Use of Information): Definiert Datenklassifizierung
- A.5.14 (Informationsübertragung): Verschlüsselungsanforderungen für Datenübertragung
- A.5.15 (Access Control): Integriert mit Key Access Controls
- A.8.9 (Configuration Management): Kryptographisches Configuration Management
- A.8.15 (Logging): Kryptographisches Event Logging
- A.8.23 (Web Filtering): Sichere Kommunikation für Web-Traffic



## Implementierungs-Ressourcen

**Implementation Guidance** (ISMS-IMP-A.8.24 Suite):

- Data Transmission Assessment: TLS/SSL, VPN, Wireless, API-Verschlüsselung
- Data Storage Assessment: Disk-, Datenbank-, Backup-, Cloud-Verschlüsselung
- Authentication Assessment: Passwort-Hashing, MFA, Certificates
- Key Management Assessment: Key-Lebenszyklus, HSM/KMS, Zugriffs-Kontrollen
- Compliance Summary Dashboard: Konsolidiertes Compliance-Reporting



**Technical Standards**:

- Genehmigte kryptographische Algorithmen und Schlüssellängen
- TLS/SSL Cipher Suite Konfigurationen
- Passwort-Hashing-Parameter
- Certificate-Gültigkeits- und Lebenszyklus-Anforderungen
- Algorithmus-Deprecation-Schedules



**Assessment-Tools**:

- Excel-basierte Assessment Workbooks mit automatisierten Compliance-Berechnungen
- Evidence-Register
- Gap Analysis Templates
- Remediation-Tracking



## Regulatorisches Mapping

Diese Richtlinie adressiert kryptographische Anforderungen von:

| Anforderungs-Kategorie | Schweizer nDSG | EU DSGVO | ISO 27001 | PCI DSS* | FINMA* | DORA/NIS2* |
|------------------------|----------------|----------|-----------|---------|---------|------------|
| Verschlüsselung at Rest | Art. 8 | Art. 32 | A.8.24 | Req. 3.5 | Rundschr. 2023/1 | ICT Risk Mgmt |
| Verschlüsselung in Transit | Art. 8 | Art. 32 | A.8.24 | Req. 4.2 | Rundschr. 2023/1 | Secure Comms |
| Key Management | Art. 8 | Art. 32 | A.8.24 | Req. 3.6 | Rundschr. 2023/1 | Key Controls |
| Algorithmus-Stärke | Best Practice | Art. 32 | A.8.24 | Strong Crypto | Risikobasiert | Crypto Agility |

*Konditionale Anwendbarkeit gemäss ISMS-POL-00

**Hinweis**: Spezifische regulatorische Interpretation und Compliance-Verifizierungs-Prozeduren sind dokumentiert in ISMS-IMP-A.8.24 Compliance Summary Dashboard.

## Training & Awareness

**Security Awareness** (Alle Mitarbeiter):

- Jährliches Training-Modul zu kryptographischen Kontrollen
- Datenklassifizierung und Verschlüsselungsanforderungen
- Incident-Reporting-Prozeduren



**Technisches Training** (Entwickler, IT-Personal):

- Sichere kryptographische Implementierung
- Genehmigte kryptographische Libraries und APIs
- Häufige kryptographische Schwachstellen



**Operatives Training** (IT Operations):

- Key Management Prozeduren
- Certificate Lifecycle Management
- Kryptographische Incident Response



---

# Definitionen

**Kryptographische Kontrolle**: Hardware- oder Software-Mechanismus, der kryptographische Algorithmen zum Schutz von Informations-Vertraulichkeit, -Integrität oder -Authentizität verwendet.

**Genehmigter Algorithmus**: Kryptographischer Algorithmus, der Sicherheitsstandards der [Organisation] erfüllt, wie definiert in ISMS-IMP-A.8.24 Technical Standards.

**Key Management**: Prozesse für kryptographischen Key-Lebenszyklus inkl. Generierung, Speicherung, Verteilung, Rotation, Backup und Vernichtung.

**Hardware Security Module (HSM)**: Manipulationsresistentes Hardware-Gerät für sichere kryptographische Key-Speicherung und -Operationen.

**Key Management Service (KMS)**: Software oder Cloud Service für zentralisiertes kryptographisches Key Management.

**Crypto Agility**: Organisatorische Fähigkeit, kryptographische Algorithmen schnell zu ändern ohne umfassende System-Neuarchitektur.

**Datenklassifizierung**: Kategorisierung von Informationen der [Organisation] basierend auf Vertraulichkeits-, Integritäts- und Verfügbarkeitsanforderungen (Öffentlich, Intern, Vertraulich, Eingeschränkt).

**Perfect Forward Secrecy (PFS)**: Kryptographische Eigenschaft, bei der Kompromittierung von Langzeit-Keys vergangene Session-Keys nicht kompromittiert.

**Certificate Authority (CA)**: Vertrauenswürdige Entität, die digitale Zertifikate für Public Key Infrastructure ausstellt.

---

# Freigabe-Protokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Chief Information Security Officer (CISO)** | [Name] | [Datum] |
| **Chief Information Officer (CIO)** | [Name] | [Datum] |
| **Legal/Compliance Officer** | [Name] | [Datum] |
| **Geschäftsleitung (GL)** | [Name] | [Datum] |

---

**ENDE DES RICHTLINIEN-DOKUMENTS**

---

*ISMS-POL-A.8.24 v1.0 | Verwendung von Kryptographie*
*Diese Richtlinie definiert Anforderungen. Implementierungs-Prozeduren sind dokumentiert in ISMS-IMP-A.8.24.*

<!-- QA_VERIFIED: 2026-01-31 -->