<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.1-7-18-19-DE:framework:POL:a.8.1-7-18-19 -->
**ISMS-POL-A.8.1-7-18-19 — Endgerätesicherheit**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Endgerätesicherheit |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.1-7-18-19 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] | |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Date to be set] | ISB / Endgerätesicherheitsmanager | Erstfassung — Kombinierte Massnahmen A.8.1, A.8.7, A.8.18, A.8.19 |

**Überprüfungsrhythmus**: Jährlich (oder bei wesentlichen organisatorischen, regulatorischen oder technologischen Änderungen)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL) oder IT-Direktor
- Technische Überprüfung: IT-Betriebsleiter / Endgeräteverwaltungsverantwortlicher
- Compliance: Rechts-/Compliance-Officer (für regulatorische Ausrichtung)
- Letzte Instanz: Geschäftsleitung (GF)

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-IMP-A.8.1-7-18-19-S1-UG/TG (Endgeräteerkennung)
- ISMS-IMP-A.8.1-7-18-19-S2-UG/TG (Deployment Malware-Schutz)
- ISMS-IMP-A.8.1-7-18-19-S3-UG/TG (Softwarekontrollprozess)
- ISMS-IMP-A.8.1-7-18-19-S4-UG/TG (Verwaltung privilegierter Hilfsprogramme)
- ISMS-POL-A.5.9 (Asset-Inventar)
- ISMS-POL-A.8.2 (Privilegierte Zugriffsrechte)
- ISMS-POL-A.8.8 (Schwachstellenmanagement)
- ISMS-POL-A.8.15 (Protokollierung)
- ISMS-POL-A.8.16 (Überwachungsaktivitäten)
- ISMS-POL-A.8.20-22 (Netzwerksicherheit)
- ISO/IEC 27001:2022 Massnahmen A.8.1, A.8.7, A.8.18, A.8.19

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] für die Endgerätesicherheit fest und implementiert die ISO/IEC 27001:2022 Massnahmen A.8.1 (Benutzer-Endgeräte), A.8.7 (Schutz vor Schadsoftware), A.8.18 (Verwendung privilegierter Hilfsprogramme) und A.8.19 (Installation von Software auf Betriebssystemen) als einheitliches Sicherheitsframework.

**Geltungsbereich**: Diese Richtlinie gilt für alle Benutzer-Endgeräte unabhängig von Typ (Laptops, Desktops, mobile Geräte, Tablets, IoT-Geräte), Betriebssystem (Windows, macOS, Linux, iOS, Android, ChromeOS) oder Eigentumsmodell (organisationseigen, BYOD, Auftragnehmer, Gäste).

**Zweck**: Organisatorische Anforderungen für die Implementierung und Governance von Endgerätesicherheitsmassnahmen festlegen. Diese Richtlinie legt fest, WAS an Endgerätesicherheitsschutz erforderlich ist, WANN er implementiert werden muss und WER dafür verantwortlich ist. Implementierungsverfahren (WIE Massnahmen umgesetzt werden) sind separat in ISMS-IMP-A.8.1-7-18-19 (UG/TG-Varianten) dokumentiert.

**Begründung für den kombinierten Massnahmenansatz**: A.8.1 (Endgeräte), A.8.7 (Malware-Schutz), A.8.18 (privilegierte Hilfsprogramme) und A.8.19 (Software-Installation) werden als einheitliches Framework implementiert, weil:

- Sie auf derselben Endgeräteinfrastruktur operieren
- Endgeräteerkennung allen vier Massnahmen dient
- Beweisnachweise erheblich überlappen (Endgeräteinventar, Software-Inventar, Sicherheitstool-Telemetrie)
- Endgerätesicherheit eine ganzheitliche Implementierung erfordert (kein isoliertes Sicherheitskonzept)
- Der kombinierte Ansatz 4-mal effizienter ist als separate Implementierungen

**Unabhängigkeit der Anwendbarkeitserklärung**: Trotz einheitlicher Implementierung und Dokumentation werden die Massnahmen A.8.1, A.8.7, A.8.18 und A.8.19 in der Anwendbarkeitserklärung (SoA) unabhängig bewertet. Jede Massnahme behält für Prüfungszwecke eigene Anforderungen, Nachweiserhebung und Compliance-Bewertung.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen), darunter das schweizerische Bundesgesetz über den Datenschutz (nDSG/DSG), die EU DSGVO wo anwendbar und ISO/IEC 27001:2022. Bedingt anwendbare sektorspezifische Anforderungen (PCI DSS v4.0.1, HIPAA, FINMA, DORA, NIS2) gelten, wenn die Geschäftstätigkeit von [Organisation] deren Anwendbarkeit auslöst.

---

# Massnahmenausrichtung und Geltungsbereich

## ISO/IEC 27001:2022 Massnahmenausrichtung

**ISO/IEC 27001:2022 Anhang A.8.1, A.8.7, A.8.18, A.8.19 — Endgerätesicherheit**

Dieses Richtlinienframework stellt organisatorische Governance für vier verwandte Massnahmen bereit, die das gesamte Endgerätesicherheits-Ökosystem abdecken:

### A.8.1 — Benutzer-Endgeräte

> *Auf Benutzer-Endgeräten gespeicherte, von diesen verarbeitete oder über diese zugängliche Informationen müssen geschützt werden.*

**Massnahmenziel**: Sicherstellen, dass Informationen auf Benutzer-Endgeräten gegen Risiken aus der Gerätenutzung geschützt sind, einschliesslich Verlust, Diebstahl, unbefugtem Zugriff, Malware-Infektionen und unzureichenden Sicherheitskonfigurationen.

**Diese Richtlinie adressiert** (A.8.1):

- Anforderungen an Endgeräteinventar und Asset-Management
- Endgeräteklassifikation und Kritikalitätsbestimmung
- Sicherheits-Baseline-Anforderungen je Endgerätetyp und Eigentumsmodell
- Verschlüsselungsanforderungen für ruhende Daten
- Anforderungen an Endgeräteverwaltung und -registrierung (MDM, agentenbasiert)
- Anforderungen an physische Sicherheit und Reaktion bei Verlust/Diebstahl
- Anforderungen für die sichere Entsorgung
- Sicherheitsanforderungen für das BYOD-Programm und Datenschutzmassnahmen

### A.8.7 — Schutz vor Schadsoftware

> *Schutz vor Schadsoftware muss implementiert und durch angemessene Sensibilisierung der Nutzer unterstützt werden.*

**Massnahmenziel**: Erkennung, Prävention und Wiederherstellung nach Schadsoftwareangriffen durch technische Massnahmen und Nutzersensibilisierung sicherstellen.

**Diese Richtlinie adressiert** (A.8.7):

- Anforderungen an Anti-Malware/EDR-Lösungen und Erkennungsfähigkeiten
- Abdeckungsanforderungen über die gesamte Endgerätelandschaft
- Anforderungen an Echtzeitschutz und Scanning
- Anforderungen an Signatur-/Definitions-Updates
- Anforderungen an Quarantäne und Behebung
- Anforderungen für die Reaktion auf Schadsoftware-Vorfälle
- Anforderungen an die Nutzersensibilisierung

### A.8.18 — Verwendung privilegierter Hilfsprogramme

> *Die Verwendung von Hilfsprogrammen, die System- und Anwendungskontrollen übersteuern könnten, muss eingeschränkt und streng kontrolliert werden.*

**Massnahmenziel**: Sicherstellen, dass privilegierte Hilfsprogramme, die Sicherheitsmassnahmen umgehen oder übersteuern können, identifiziert, auf autorisierte Nutzer beschränkt, sachgemäss verwendet sowie deren Nutzung überwacht und protokolliert wird.

**Diese Richtlinie adressiert** (A.8.18):

- Anforderungen an Identifikation und Inventar privilegierter Hilfsprogramme
- Zugangskontrollanforderungen für privilegierte Hilfsprogramme
- Anforderungen an Genehmigungsworkflows für privilegierten Zugang
- Anforderungen an Nutzungsüberwachung und -protokollierung
- Anforderungen an die Verwaltung von Sicherheitsumgehungswerkzeugen

### A.8.19 — Installation von Software auf Betriebssystemen

> *Verfahren und Massnahmen müssen implementiert werden, um die Installation von Software auf Betriebssystemen sicher zu verwalten.*

**Massnahmenziel**: Sicherstellen, dass Software-Installationen auf Betriebssystemen kontrolliert, autorisiert sind und keine Sicherheitslücken oder Schadsoftware einführen.

**Diese Richtlinie adressiert** (A.8.19):

- Anforderungen an die Liste zugelassener Software
- Anforderungen an den Software-Genehmigungsprozess
- Anforderungen an die Integration der Änderungskontrolle
- Anforderungen an Erkennung und Entfernung nicht autorisierter Software
- Anforderungen an Technologien zur Anwendungskontrolle
- Anforderungen an Software-Schwachstellenmanagement
- Anforderungen an Softwarekontrolle für BYOD

## Was diese Richtlinie regelt

Diese Richtlinie:

- **Definiert** Anforderungen für Endgerätesicherheitsmassnahmen, ausgerichtet an Datenklassifikation, Risikobereitschaft der Organisation und regulatorischen Verpflichtungen
- **Legt fest** den Governance-Rahmen für Entscheidungsfindung und Verantwortlichkeit in der Endgerätesicherheit
- **Spezifiziert** verbindliche Anforderungen für die Massnahmenimplementierung (WAS implementiert werden muss)
- **Verweist** auf anwendbare regulatorische Anforderungen gemäss ISMS-POL-00
- **Identifiziert** organisatorische Rollen und Verantwortlichkeiten für die Governance der Endgerätesicherheit
- **Bietet** Rahmen für die Verwaltung von Ausnahmen und Vorfällen

## Was diese Richtlinie NICHT regelt

Diese Richtlinie regelt NICHT:

- **Technische Implementierungsverfahren** (siehe ISMS-IMP-A.8.1-7-18-19 Implementierungsleitfäden)
- **Spezifische Endgeräteerkennung** (siehe ISMS-IMP-A.8.1-7-18-19-S1)
- **Auflistung von Sicherheits-Baseline-Konfigurationen** (siehe ISMS-IMP-A.8.1-7-18-19-S1)
- **Deployment-Verfahren für Anti-Malware** (siehe ISMS-IMP-A.8.1-7-18-19-S2)
- **Detaillierte Software-Genehmigungsworkflows** (siehe ISMS-IMP-A.8.1-7-18-19-S3)
- **Spezifische Zugangsmassnahmen für privilegierte Hilfsprogramme** (siehe ISMS-IMP-A.8.1-7-18-19-S4)
- **Auswahl spezifischer Technologien oder Anbieter** (Technologieauswahl basiert auf Risikobeurteilung, technischer Umgebung und Budget von [Organisation])
- **Ersatz der Risikobeurteilung** (Endgerätesicherheitsmassnahmen werden auf Basis der Risikobehandlungsentscheidungen von [Organisation] ausgewählt)

**Begründung**: Die Trennung von Richtlinienanforderungen und Implementierungshinweisen ermöglicht:

- Stabilität der Richtlinie trotz sich wandelnder Technologielandschaft
- Technologische Agilität für Updates ohne Richtlinienrevision
- Klare Unterscheidung zwischen Governance (Richtlinie) und Ausführung (Implementierung)

## Geltungsbereich

**Diese Richtlinie gilt für**:

**Endgerätetypen**:

- Laptops und Desktops (organisationseigen und BYOD, alle Betriebssysteme)
- Mobile Geräte (Smartphones und Tablets — iOS, Android, andere mobile Betriebssysteme)
- Spezialisierte Endgeräte (Thin Clients, Chromebooks, Kioskterminals, Point-of-Sale-Terminals)
- IoT-Geräte, die Organisationsinformationen speichern, verarbeiten oder darauf zugreifen
- Virtual Desktop Infrastructure (VDI/DaaS clientseitige Sicherheitskomponenten)

**Betriebssysteme**:

- Windows (Windows 10, Windows 11, Windows Server Endgeräteanwendungsfälle)
- macOS (macOS 12 Monterey und neuere Versionen)
- Linux (Ubuntu, Red Hat, CentOS, Debian und andere Distributionen)
- iOS (iOS 15 und neuere Versionen)
- Android (Android 11 und neuere Versionen)
- ChromeOS und andere Betriebssysteme auf Benutzer-Endgeräten

**Eigentumsmodelle**:

- Organisationseigen: Von [Organisation] beschaffte und verwaltete Geräte
- BYOD (Bring Your Own Device): Persönliche Geräte für berufliche Zwecke
- Auftragnehmergeräte: Geräte von Auftragnehmern, Beratern, Zeitarbeitskräften
- Gastgeräte: Temporäre Besuchergeräte mit eingeschränktem Netzwerkzugang
- Labor-/Testgeräte: Entwicklungs-, Test- und Qualitätssicherungsendgeräte

**Personal**:

- Mitarbeitende (Vollzeit, Teilzeit, temporär)
- Auftragnehmer und Berater
- Drittanbieter mit Endgerätezugang
- Gäste und Besucher (eingeschränkte Zugangsszenarios)

**Netzwerkstandorte**:

- Vor Ort (Büros, Rechenzentren, Konferenzräume)
- Remote/Heimbüro (Homeoffice-Endgeräte)
- Mobil (reisende Mitarbeitende, Aussendienst)
- Niederlassungen und Satellitenstandorte
- Kundenstandorte und Drittanbieterstandorte

## Nicht im Geltungsbereich

Diese Richtlinie gilt **NICHT** für folgende Bereiche (durch separate ISMS-Richtlinien abgedeckt):

- **Serverinfrastruktur**: Abgedeckt durch Serversicherheitsmassnahmen und Härtungsrichtlinien
- **Netzwerkinfrastruktur**: Abgedeckt durch ISMS-POL-A.8.20-22 (Netzwerksicherheit)
- **Cloud-Infrastruktur**: Abgedeckt durch ISMS-POL-A.5.23 (Cloud-Dienste-Sicherheit)
- **Physische Sicherheit**: Abgedeckt durch ISMS-POL-A.7.x (Physische und umgebungsbezogene Sicherheit)
- **Identitäts- und Zugriffsmanagement**: Abgedeckt durch ISMS-POL-A.5.15-16-18 (IAM)
- **Datenklassifikation und -handhabung**: Abgedeckt durch ISMS-POL-A.5.12-13

Diese Richtlinie **integriert** sich jedoch mit diesen Massnahmenbereichen, wo sich Endgerätesicherheit mit anderen Massnahmen überschneidet (siehe Abschnitt 4).

## Technologieneutralität

Diese Richtlinie ist **vollständig technologieneutral**:

- Kompatibel mit jeder Endgeräteverwaltungsplattform (Intune, Jamf, SCCM, Google Workspace MDM, VMware Workspace ONE usw.)
- Unterstützt jeden Anti-Malware/EDR-Anbieter (CrowdStrike, Microsoft Defender, SentinelOne, Carbon Black usw.)
- Kompatibel mit jeder Anwendungskontrolltechnologie (AppLocker, Gatekeeper, Whitelisting-Lösungen)
- Anpassbar an jede Privileged Access Management (PAM)-Lösung
- Anbieterspezifische Auswahl ist von dem Richtlinienrahmen getrennt
- Grundsätze und Anforderungen bleiben unabhängig von der Technologiewahl konstant

Die Implementierungshinweise (ISMS-IMP-A.8.1-7-18-19-Suite) liefern technologiespezifische Beispiele unter Beibehaltung der technologieneutralen Richtlinienebene.

## Regulatorische Anwendbarkeit

Regulatorische Anforderungen werden gemäss **ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)** kategorisiert.

**Stufe 1: Verbindliche Compliance**

| Regulierung | Anwendbarkeit | Wesentliche Anforderungen |
|-------------|---------------|--------------------------|
| **Schweizerisches nDSG** | Alle Schweizer Betriebe | Art. 8 — Geeignete technische und organisatorische Massnahmen zum Datenschutz |
| **EU DSGVO** | Bei Bearbeitung von EU-Personendaten | Art. 32 — Sicherheitsmassnahmen einschliesslich Verschlüsselung, Zugangsmassnahmen, Malware-Schutz |
| **ISO/IEC 27001:2022** | Zertifizierungsumfang | Massnahmen A.8.1, A.8.7, A.8.18, A.8.19 — Dokumentierte Richtlinie und Implementierung |

**Stufe 2: Bedingte Anwendbarkeit**

Gilt nur, wenn spezifische Geschäftsbedingungen die Anwendbarkeit auslösen:

| Regulierung | Auslösebedingung | Endgerätesicherheitsanforderungen |
|------------|-----------------|----------------------------------|
| **PCI DSS v4.0.1** | Bearbeitung von Zahlungskartendaten | Endgerätesicherheit für Systeme mit Zugang zu Karteninhaberdaten (Anforderungen 2, 5, 6, 10, 11) |
| **HIPAA** | Bearbeitung von geschützten Gesundheitsinformationen (ePHI) | Technische Schutzmassnahmen einschliesslich Verschlüsselung, Zugangsmassnahmen, Prüfprotokollierung (45 CFR § 164.312) |
| **FINMA** | Reguliertes Schweizer Finanzinstitut | Technische und organisatorische Massnahmen basierend auf Risikobeurteilung, operatives Risikomanagement |
| **DORA** | EU-Finanzdienstleistungsunternehmen | IKT-Risikomanagement einschliesslich Endgerätesicherheitsmassnahmen |
| **NIS2** | Wesentliche/wichtige Einrichtung (EU) | Sicherheitsmassnahmen für Netz- und Informationssysteme einschliesslich Endgeräte |

**Stufe 3: Informationsleitlinien**

Diese Rahmenwerke informieren die Implementierung, stellen jedoch keine verbindlichen Compliance-Anforderungen dar, es sei denn, sie sind vertraglich vorgeschrieben:

- NIST Cybersecurity Framework 2.0
- NIST SP 800-53 Rev. 5
- CIS Controls v8.1 (Massnahmen 1, 2, 4, 5, 7, 10, 16)
- MITRE ATT&CK Framework

**Compliance-Bestimmung**: [Organisation] ermittelt anwendbare Stufe-2-Regulierungen durch periodische, in ISMS-POL-00 dokumentierte Bewertung der Geschäftstätigkeit. Bei Überschneidung mehrerer Regulierungen gelten die strengsten Anforderungen.

---

# Endgerätesicherheits-Anforderungsrahmen

## Endgerätesicherheit (A.8.1)

**Ziel**: Schutz von Informationen, die auf Benutzer-Endgeräten gespeichert, von diesen verarbeitet oder über diese zugänglich sind.

### Endgeräteinventar (Verbindlich)

[Organisation] muss ein vollständiges und aktuelles Inventar aller Benutzer-Endgeräte führen, die Organisationsinformationen speichern, verarbeiten oder auf diese zugreifen.

**Mindestabdeckung Inventar**: ≥ 95 % der netzwerkverbundenen Endgeräte (Ziel: 100 %)

**Aktualisierungsfrequenz Inventar**: Wöchentliche automatisierte Erkennung mindestens (täglich bevorzugt), monatlicher Abgleich

**Implementierungshinweis**: Endgeräteerkennungsverfahren, Inventarattribute und Abgleichsmethoden sind in ISMS-IMP-A.8.1-7-18-19-S1 definiert.

### Endgeräteklassifikation (Verbindlich)

[Organisation] muss Endgeräte nach Gerätetyp, Eigentumsmodell und Kritikalität klassifizieren, um geeignete Sicherheitsmassnahmen anzuwenden.

**Klassifikationsdimensionen**:

- Gerätetyp (Laptop, Desktop, mobiles Gerät, Tablet, IoT, VDI-Client)
- Eigentumsmodell (organisationseigen, BYOD, Auftragnehmer, Gast, Labor/Test)
- Kritikalität (kritisch, hoch, mittel, niedrig — basierend auf verarbeiteten Daten und Geschäftsauswirkungen)

**Implementierungshinweis**: Klassifikationskriterien, -verfahren und Sicherheitsmassnahmen-Mapping sind in ISMS-IMP-A.8.1-7-18-19-S1 definiert.

### Sicherheits-Baselines (Verbindlich)

[Organisation] muss Sicherheits-Baselines geeignet für Endgerätetyp und Eigentumsmodell implementieren.

**Universelle Baseline-Anforderungen** (alle Endgeräte):

- Betriebssystem-Härtung (aktuelle Sicherheitsupdates, Firewall aktiviert, unnötige Dienste deaktiviert)
- Authentifizierungsmassnahmen (starke Passwörter, Bildschirmsperre, MFA wo anwendbar)
- Netzwerksicherheit (sicheres WLAN, Bluetooth-Einschränkungen)
- Protokollierung und Überwachung (Protokollierung von Sicherheitsereignissen, SIEM-Integration wo anwendbar)

**Plattformspezifische Baselines**: Windows-, macOS-, Linux-, iOS/Android-Baselines müssen basierend auf Anbietersicherheitsleitlinien (Microsoft Security Baselines, Apple Platform Security Guide) und Branchenstandards (CIS Benchmarks) definiert werden.

**Baseline-Compliance-Überwachung**: Wöchentliche automatisierte Compliance-Scans mindestens (täglich bevorzugt), monatliche Compliance-Berichte, ≥ 90 % Compliance-Ziel über alle Endgeräte.

**Implementierungshinweis**: Detaillierte Baseline-Spezifikationen, Durchsetzungsmechanismen und Compliance-Überwachungsverfahren sind in ISMS-IMP-A.8.1-7-18-19-S1 definiert.

### Verschlüsselung (Verbindlich)

[Organisation] muss Verschlüsselung zum Schutz ruhender Daten auf Endgeräten implementieren.

**Anforderungen Vollständige Festplattenverschlüsselung**:

- Alle organisationseigenen Laptops und Desktops: Vollständige Festplattenverschlüsselung (FDE) erforderlich (≥ 98 % Abdeckung)
- Verschlüsselungsalgorithmus: Mindestens AES-256
- Pre-Boot-Authentifizierung: Erforderlich
- Hinterlegung von Verschlüsselungsschlüsseln: Erforderlich für organisationseigene Geräte (Wiederherstellungsschlüssel zentral gespeichert)

**Anforderungen Verschlüsselung mobiler Geräte**:

- Alle organisationseigenen mobilen Geräte: Geräteverschlüsselung aktiviert (≥ 95 % Abdeckung)
- BYOD mobile Geräte: Container-Verschlüsselung erforderlich (nur corporate Apps/Daten)

**Zeitrahmen Verschlüsselungsimplementierung**:

- Neue Geräte: Verschlüsselung vor Inbetriebnahme aktiviert (100 % Compliance)
- Bestehende Geräte: Kritische Endgeräte innerhalb von 30 Tagen, hohe Priorität innerhalb von 90 Tagen, mittlere Priorität innerhalb von 180 Tagen

**Ausnahmen**: Desktop-Computer in gesicherten Einrichtungen können mit ISB-Genehmigung und kompensierenden Massnahmen ausgenommen werden. Gesicherte Einrichtungen sind definiert als: (a) physisch zugangskontrollierte Bereiche mit Badge-/biometrischem Eingang; (b) 24/7-Überwachung oder besetzte Rezeption; (c) kein öffentlicher Zugang; (d) dokumentiert im physischen Sicherheitsregister gemäss A.7.1-4.

**Implementierungshinweis**: Verfahren für Verschlüsselungsimplementierung, Schlüsselverwaltung und Verifikation sind in ISMS-IMP-A.8.1-7-18-19-S1 definiert.

### Endgeräteverwaltung (Verbindlich)

[Organisation] muss alle organisationseigenen Endgeräte in einem Endgeräteverwaltungssystem registrieren (MDM für mobile Geräte, agentenbasiert für Laptops/Desktops).

**Erforderliche Verwaltungsfähigkeiten**:

- Konfigurationsmanagement (Sicherheits-Baselines implementieren und durchsetzen)
- Software-Deployment (zentralisierte Softwareverteilung und Updates)
- Compliance-Überwachung (Baseline-Compliance, Verschlüsselungsstatus, Software-Inventar überwachen)
- Remote-Wipe-Fähigkeit (für verlorene/gestohlene Geräte)
- Inventarsynchronisation (Endgeräteinventar automatisch aktualisieren)

**Registrierungsanforderungen**:

- Zeitpunkt: Registrierung vor Geräteübergabe an Nutzer erforderlich (Pre-Deployment)
- Abdeckung: 100 % Ziel für organisationseigene Laptops, Desktops, mobile Geräte
- BYOD: Containerisierte Verwaltung (MAM) via MDM — eingeschränkter Umfang (nur Corporate Apps/Daten)

**Verwaltung von Konfigurationsabweichungen**: Wöchentliche Konfigurationskonformitätsscans, automatische Behebung wo möglich, Abweichungen innerhalb von 7 Tagen behoben.

**Implementierungshinweis**: Plattformauswahl, Registrierungsverfahren und Erkennung von Konfigurationsabweichungen sind in ISMS-IMP-A.8.1-7-18-19-S1 definiert.

### Reaktion bei Verlust/Diebstahl (Verbindlich)

[Organisation] muss Verfahren für die Reaktion auf verlorene oder gestohlene Endgeräte implementieren.

**Meldeanforderungen**: Nutzer müssen verlorene/gestohlene Geräte unverzüglich melden (Ziel: innerhalb von 1 Stunde nach Entdeckung).

**Remote-Wipe-Anforderungen**: Remote-Wipe-Fähigkeit muss für alle organisationseigenen Endgeräte verfügbar sein, Initiierung innerhalb von 4 Stunden nach Meldung (1 Stunde für kritische Geräte).

**Implementierungshinweis**: Verfahren für Meldung verlorener/gestohlener Geräte, Remote-Wipe-Workflows und Incident-Response sind in ISMS-IMP-A.8.1-7-18-19-S1 definiert.

### Sichere Entsorgung (Verbindlich)

[Organisation] muss Endgeräte bei Ausserbetriebnahme sicher entsorgen, um Datenverlust zu verhindern.

**Entsorgungsanforderungen**:

- Datensanitisierung: Sicheres Löschen (NIST SP 800-88 Rev. 2 konform) oder physische Vernichtung
- Vernichtungsnachweis: Für alle entsorgten Endgeräte erforderlich
- Inventaraktualisierung: Endgerät im Inventar als "Entsorgt" markiert mit beigefügtem Zertifikat

**Entsorgungsmethoden**:

- Sicheres Überschreiben: DoD 5220.22-M oder NIST SP 800-88 Rev. 2 Clear/Purge
- Entmagnetisierung: Für magnetische Festplatten
- Physische Vernichtung: Schreddern, Zerquetschen oder Verbrennen (zertifizierter Anbieter)

**Implementierungshinweis**: Entsorgungsverfahren, Sanitisierungsmethoden und Anbieterauswahl sind in ISMS-IMP-A.8.1-7-18-19-S1 und ISMS-REF-A.8.10 definiert.

### BYOD-Programm (Bedingt)

[Organisation] kann ein BYOD-Programm für persönliche Geräte für berufliche Zwecke implementieren, vorbehaltlich Sicherheitsanforderungen und Datenschutzmassnahmen.

**BYOD-Sicherheitsanforderungen**:

- BYOD-Nutzungsvereinbarung: Erforderlich (Nutzer anerkennt Sicherheitsanforderungen und Remote-Container-Wipe)
- Mindest-Gerätesicherheit: Gerätepsscode, Verschlüsselung (oder Container-Verschlüsselung), automatische Sperre, unterstütztes Betriebssystem
- Containerisierte Verwaltung (MAM): Corporate Apps im verwalteten Container, getrennt von persönlichen Daten
- Remote-Wipe-Umfang: Nur Container-Wipe (kein vollständiges Geräte-Wipe)

**BYOD-Datenschutzmassnahmen**: Kein Zugang zu persönlichen Daten, kein Inventar persönlicher Apps, keine vollständige Gerätekontrolle, nur Container-Verwaltung, transparente Datenschutzhinweise.

**Implementierungshinweis**: BYOD-Programmgestaltung, Nutzungsvereinbarungsvorlagen, MAM-Konfiguration und Datenschutzmassnahmen sind in ISMS-IMP-A.8.1-7-18-19-S1 definiert.

## Malware-Schutz (A.8.7)

**Ziel**: Schutz von Endgeräten vor Schadsoftware durch Erkennungs-, Präventions- und Wiederherstellungsmassnahmen, unterstützt durch Nutzersensibilisierung.

### Anti-Malware/EDR-Lösung (Verbindlich)

[Organisation] muss Anti-Malware- oder EDR-Lösungen mit mehrschichtigen Erkennungsfähigkeiten implementieren.

**Erforderliche Erkennungsmechanismen**:

- Signaturbasierte Erkennung: Klassische Antivirus-Signaturen für bekannte Schadsoftware
- Verhaltensbasierte Erkennung (Heuristik): Überwacht Programmverhalten auf verdächtige Aktivitäten
- Machine-Learning-Erkennung: KI/ML-Modelle für Identifikation unbekannter Bedrohungen (dringend empfohlen)
- Exploit-Prävention: Blockiert Exploit-Techniken
- Ransomware-spezifischer Schutz: Verhaltensanalyse, geschützter Ordnerzugriff, Rollback-Fähigkeit

**Cloudbasierter Schutz**: Anti-Malware/EDR-Lösungen sollten cloudbasierten Schutz für Echtzeit-Bedrohungsintelligenz nutzen.

**Manipulationsschutz**: Anti-Malware/EDR-Agenten müssen Manipulationsschutz aktiviert haben, um zu verhindern, dass Schadsoftware den Schutz deaktiviert.

**Implementierungshinweis**: Lösungsauswahl, Deployment-Architektur und Funktionskonfiguration sind in ISMS-IMP-A.8.1-7-18-19-S2 definiert.

### Schutzabdeckung (Verbindlich)

[Organisation] muss Malware-Schutzabdeckung über die gesamte Endgerätelandschaft erreichen.

**Abdeckungsanforderungen**:

- Organisationseigene Endgeräte: ≥ 98 % Schutzabdeckung (Ziel: 100 %)
- BYOD-Endgeräte: ≥ 80 % Schutzabdeckung (geringer wegen freiwilliger Teilnahme und eingeschränkter Verwaltung)

**Abdeckungsüberwachung**: Tägliche Abdeckungsberichte aus der Anti-Malware-Managementkonsole, sofortige Alarmierung wenn Abdeckung unter 95 % fällt.

**Lückenbehebung**: Ungeschütztes Endgerät identifiziert → Schutz innerhalb von 24 Stunden implementiert.

**Implementierungshinweis**: Abdeckungsüberwachungsverfahren, Lückenidentifikation und Behebungsworkflows sind in ISMS-IMP-A.8.1-7-18-19-S2 definiert.

### Echtzeitschutz und Scanning (Verbindlich)

[Organisation] muss Echtzeitschutz und regelmässige Scans implementieren.

**Echtzeitschutz**: On-Access-Scanning muss auf allen geschützten Endgeräten aktiviert sein (Dateien werden beim Öffnen, Ausführen oder Kopieren gescannt).

**Vollständige Systemscans**: Vollständige Systemscans müssen wöchentlich auf allen geschützten Endgeräten durchgeführt werden.

**Schnellscans**: Schnellscans sollten täglich auf allen geschützten Endgeräten durchgeführt werden.

**Implementierungshinweis**: Scan-Konfiguration, Zeitplanung und Ergebnisüberwachung sind in ISMS-IMP-A.8.1-7-18-19-S2 definiert.

### Signatur-Updates (Verbindlich)

[Organisation] muss Anti-Malware-Signaturen/Definitionen aktuell halten.

**Aktualisierungsfrequenz**: Täglich mindestens (Echtzeit-Updates dringend bevorzugt für cloudbasierten Schutz).

**Verifikation Updates**: Veraltete Signaturen markiert (Gelb: > 24 Stunden veraltet, Rot: > 48 Stunden veraltet), Behebung innerhalb von 24 Stunden.

**Aktualität Agent**: Anti-Malware/EDR-Agentensoftware muss aktuell gehalten werden (neueste Version oder N-1), ≥ 90 % der Endgeräte auf neuester oder N-1-Version.

**Implementierungshinweis**: Update-Deployment, Verifikationsverfahren und Agentenversionsmanagement sind in ISMS-IMP-A.8.1-7-18-19-S2 definiert.

### Quarantäne und Behebung (Verbindlich)

[Organisation] muss automatische Malware-Quarantäne und Behebungsverfahren implementieren.

**Automatische Quarantäne**: Erkannte Schadsoftware muss automatisch ohne Nutzerinteraktion unter Quarantäne gestellt werden.

**Behebungsanforderungen**: Malware-Behebung muss Bereinigung, Verifikation und Wiederherstellung umfassen (Dateien aus Backup wiederherstellen, kompromittierte Zugangsdaten zurücksetzen, bei schwerwiegenden Infektionen Image neu erstellen).

**Implementierungshinweis**: Quarantänekonfiguration, Behebungsworkflows und Wiederherstellungsverfahren sind in ISMS-IMP-A.8.1-7-18-19-S2 definiert.

### Reaktion auf Schadsoftware-Vorfälle (Verbindlich)

[Organisation] muss Incident-Response-Verfahren für Schadsoftware-Infektionen implementieren.

**Erkennungsauslöser**: Schadsoftware erkannt durch Anti-Malware/EDR (automatische Alarmierung), erkannte Verhaltensanomalien, Nutzer meldet verdächtiges Verhalten.

**Reaktionszeitrahmen**: Triage innerhalb von 1 Stunde, sofortige Eindämmung bei kritischer Lage (aktive Ransomware, Datenexfiltration), innerhalb von 4 Stunden bei hohem Schweregrad.

**Vorfallprotokollierung**: Alle Malware-Erkennungen zentral protokolliert (SIEM gemäss ISMS-POL-A.8.15), Vorfalltickets erstellt, mindestens 12 Monate Aufbewahrung.

**Implementierungshinweis**: Vorfallklassifikation, Reaktionsworkflows und Eskalationsverfahren sind in ISMS-IMP-A.8.1-7-18-19-S2 definiert.

### Nutzersensibilisierung (Verbindlich)

[Organisation] muss Sicherheitssensibilisierungsschulungen zu Schadsoftwarebedrohungen für Nutzer bereitstellen.

**Schulungsanforderungen**:

- Themen: Erkennung von Phishing, sicherer Umgang mit E-Mail/Internet, Risiken bei USB/Wechselmedien, Meldung verdächtiger Aktivitäten
- Häufigkeit: Erstschulung bei Onboarding, jährliche Auffrischung mindestens (vierteljährlich empfohlen)
- Phishing-Simulationen: Vierteljährliche simulierte Phishing-Kampagnen
- Wirksamkeitsmessung: ≥ 95 % Schulungsabschluss jährlich, ≤ 10 % Klickrate bei Phishing-Simulationen
- Nachschulung bei Wiederholungsfehlern: Personal, das zwei aufeinanderfolgende Phishing-Simulationen nicht besteht, erhält innerhalb von 14 Tagen gezielte Nachschulung; bei drei oder mehr aufeinanderfolgenden Misserfolgen erfolgt Managerbenachrichtigung und verstärkte Überwachung gemäss HR-Richtlinie

**Implementierungshinweis**: Schulungsinhalte, Bereitstellungsmethoden und Wirksamkeitsmessung sind in ISMS-IMP-A.8.1-7-18-19-S2 definiert.

## Verwaltung privilegierter Hilfsprogramme (A.8.18)

**Ziel**: Privilegierte Hilfsprogramme, die System- und Anwendungsmassnahmen übersteuern können, einschränken und streng kontrollieren.

### Inventar privilegierter Hilfsprogramme (Verbindlich)

[Organisation] muss ein Inventar privilegierter Hilfsprogramme führen, die System- und Anwendungsmassnahmen übersteuern können.

**Privilegierte Hilfsprogramme umfassen**:

- Systemadministrationswerkzeuge (Task Manager, Registrierungseditor, Dienste-Manager, MMC)
- Fernzugriffswerkzeuge (Remote Desktop, VNC, TeamViewer, SSH-Clients)
- Debug- und Entwicklungswerkzeuge (Debugger, Dekompilierer, Hex-Editoren)
- Festplatten- und Dateiprogramme (Festplattenformatierer, Partitionsmanager, Tools zum sicheren Löschen)
- Passwort- und Sicherheitswerkzeuge (Passwort-Wiederherstellung, Verschlüsselungsumgehungswerkzeuge)
- Netzwerkprogramme (Packet Sniffer, Port-Scanner, Netzwerkanalysatoren)
- Virtualisierungswerkzeuge (Hypervisoren, VM-Verwaltungswerkzeuge)
- Alle Tools, die Sicherheitsmassnahmen umgehen können (Antivirus deaktivieren, Prüfprotokolle ändern)

**Inventarpflege**: Vierteljährliche Überprüfung des Inventars privilegierter Hilfsprogramme, neue Hilfsprogramme vor Deployment bewertet.

**Implementierungshinweis**: Identifikation privilegierter Hilfsprogramme, Inventarverfahren und Klassifikation sind in ISMS-IMP-A.8.1-7-18-19-S4 definiert.

### Zugangskontrolle (Verbindlich)

[Organisation] muss den Zugang zu privilegierten Hilfsprogrammen auf autorisiertes Personal beschränken.

**Rollenbasierte Zugangskontrolle (RBAC)**: Zugang zu privilegierten Hilfsprogrammen muss basierend auf Arbeitsstelle und geschäftlichem Bedarf eingeschränkt werden.

**Zugangskontrollmechanismen**:

- Anwendungs-Whitelisting: Privilegierte Hilfsprogramme für Standardnutzer gesperrt
- Privileged Access Management (PAM): Just-in-Time-Zugang, Sitzungsaufzeichnung für hochprivilegierte Hilfsprogramme
- Gruppenrichtlinie (Windows): Task Manager, Registrierungseditor für Standardnutzer deaktivieren
- MDM-Einschränkungen (macOS/mobil): Zugang zu Entwicklerwerkzeugen, Systemeinstellungen einschränken
- Sudo-Einschränkungen (Linux): Sudo-Zugang auf autorisierte Nutzer beschränken

**Multi-Faktor-Authentifizierung**: Zugang zu kritischen privilegierten Hilfsprogrammen erfordert Multi-Faktor-Authentifizierung (MFA).

**Implementierungshinweis**: Zugangsmassnahmen, RBAC-Konfiguration und MFA-Durchsetzung sind in ISMS-IMP-A.8.1-7-18-19-S4 definiert.

### Genehmigungsworkflows (Verbindlich)

[Organisation] muss Genehmigungsworkflows für Zugriffsanfragen zu privilegierten Hilfsprogrammen implementieren.

**Zugriffsanfragetypen**:

- Dauerhafter Zugang (permanente Zuweisung): Managergenehmigung + ISB-Genehmigung (kritische Hilfsprogramme), jährliche Rezertifizierung
- Temporärer Zugang (zeitlich begrenzt): Managergenehmigung, automatischer Widerruf nach Ablauf, maximal 1–90 Tage
- Notfallzugang (Break-Glass): Nachträgliche Genehmigung (Zugang sofort gewährt, Manager benachrichtigt), Überprüfung innerhalb von 24 Stunden

**Genehmigungsdokumentation**: Anforderungsticket, geschäftliche Begründung, Genehmigungsbehörde, Genehmigungsdatum, Zugangsdauer (bei temporär).

**Implementierungshinweis**: Design des Genehmigungsworkflows, Antragsformulare und Rezertifizierungsverfahren sind in ISMS-IMP-A.8.1-7-18-19-S4 definiert.

### Nutzungsüberwachung und -protokollierung (Verbindlich)

[Organisation] muss die Nutzung privilegierter Hilfsprogramme protokollieren und überwachen.

**Protokollierungsanforderungen**: Nutzeridentität, Name des Hilfsprogramms, Zeitstempel, Dauer, Endgerätkennung, durchgeführte Aktionen (sofern verfügbar — Sitzungsaufzeichnung).

**Protokollaufbewahrung**: Mindestens 12 Monate.

**Überwachungsanforderungen**: Echtzeit-Alarmierung bei nicht autorisierten Zugriffsversuchen auf privilegierte Hilfsprogramme, tägliche Überprüfung der Protokolle (automatisierte Anomalieerkennung), vierteljährliche Nutzungsprüfung.

**SIEM-Integration**: Protokolle der Nutzung privilegierter Hilfsprogramme werden an das zentrale SIEM weitergeleitet (gemäss ISMS-POL-A.8.15).

**Implementierungshinweis**: Protokollierungskonfiguration, Überwachungsverfahren und SIEM-Integration sind in ISMS-IMP-A.8.1-7-18-19-S4 definiert.

### Verwaltung von Sicherheitsumgehungswerkzeugen (Verbindlich)

[Organisation] muss Werkzeuge, die Sicherheitsmassnahmen umgehen können, identifizieren und streng einschränken.

**Sicherheitsumgehungswerkzeuge umfassen**: Anti-Malware-Deaktivatoren, Tools zur Bearbeitung von Prüfprotokollen, Verschlüsselungsumgehungswerkzeuge (Passwort-Cracker), Rootkit-Tools, Tools zur Deaktivierung von Windows Defender oder des Manipulationsschutzes, Tools zur Änderung des System Integrity Protection (macOS SIP).

**Massnahmenansatz**:

- Verboten: Sicherheitsumgehungswerkzeuge auf Produktionsendgeräten untersagt (sofern nicht für Sicherheitstests autorisiert)
- Erkennung: Anwendungskontrolle erkennt nicht autorisierte Sicherheitsumgehungswerkzeuge
- Automatische Behebung: Erkannte Tools automatisch unter Quarantäne gestellt/entfernt
- Autorisierte Nutzung: Nur Sicherheitsteam, isolierte Sicherheitslaborumgebung, Genehmigung erforderlich

**Implementierungshinweis**: Identifikation von Sicherheitsumgehungswerkzeugen, Erkennungsregeln und autorisierte Nutzungsverfahren sind in ISMS-IMP-A.8.1-7-18-19-S4 definiert.

## Softwareinstallationsmassnahmen (A.8.19)

**Ziel**: Software-Installationen auf Betriebssystemen durch Massnahmen, Autorisierung und Schwachstellenmanagement sicher verwalten.

### Liste zugelassener Software (Verbindlich)

[Organisation] muss eine Liste zugelassener Software führen.

**Inhalt der Liste zugelassener Software**: Softwarename und Anbieter, zugelassene Version(en), Zweck/geschäftliche Begründung, Status der Sicherheitsüberprüfung, Installationsmethode, Genehmigungsbehörde, Lizenz-Compliance-Status.

**Softwarekategorien**:

- Verbindliche Unternehmenssoftware: Für alle Nutzer erforderlich (Betriebssystem, Anti-Malware, Produktivitätssuite)
- Rollenspezifische Software: Für spezifische Rollen erforderlich (Entwicklungswerkzeuge für Entwickler)
- Optional zugelassene Software: Für Nutzerinstallation verfügbar (zugelassene Browser, Hilfsprogramme)
- Verbotene Software: Explizit untersagt (Sicherheitsrisiken, Lizenzprobleme)

**Listenpflege**: Jährliche Überprüfung der Liste zugelassener Software, vierteljährliche Ergänzungen/Entfernungen bei Bedarf, Sicherheitsüberprüfung vor Genehmigung erforderlich.

**Implementierungshinweis**: Verwaltung der Liste zugelassener Software, Kategoriedefinitionen und Überprüfungsverfahren sind in ISMS-IMP-A.8.1-7-18-19-S3 definiert.

### Software-Genehmigungsprozess (Verbindlich)

[Organisation] muss einen Software-Genehmigungsprozess vor dem Deployment implementieren.

**Komponenten des Genehmigungsprozesses**:

- Softwareanfrage mit geschäftlicher Begründung
- Sicherheitsüberprüfung (Schwachstellenbeurteilung, Anbieterreputation, Datenschutzprüfung, Lizenz-Compliance)
- Genehmigungsentscheidung (genehmigt, genehmigt mit Auflagen, abgelehnt)
- Deployment (zentralisiertes Deployment bevorzugt, Selbstinstallation durch Nutzer wenn genehmigt)

**Genehmigungsfrist**: Standardanfrage 5 Arbeitstage, dringende Anfrage 2 Arbeitstage (Managergenehmigung), Notfallanfrage 1 Arbeitstag (ISB-Genehmigung). Bei Abwesenheit des ISB delegiert die Notfallgenehmigungsbehörde an: (1) Stellvertretenden ISB, (2) IT-Direktor oder (3) designierten Sicherheitsmanager, mit nachträglicher ISB-Überprüfung innerhalb von 5 Arbeitstagen.

**Implementierungshinweis**: Design des Genehmigungsworkflows, Sicherheitsüberprüfungsverfahren und Deployment-Methoden sind in ISMS-IMP-A.8.1-7-18-19-S3 definiert.

### Integration der Änderungskontrolle (Verbindlich)

[Organisation] muss Software-Installationen auf Produktionssystemen dem Änderungskontrollverfahren unterwerfen.

**Anforderungen Änderungskontrolle**: Software-Deployment als Änderung klassifiziert, Änderungsantrag eingereicht, Folgenabschätzung erforderlich, Genehmigung erforderlich (Change Advisory Board bei wesentlichen Änderungen), Tests erforderlich (Pilot-Deployment), Rollback-Plan dokumentiert.

**Ausnahmen**: Notfall-Sicherheits-Patches (beschleunigter Prozess), vorab genehmigte Standardänderungen (Betriebssystem-Updates, Anti-Malware-Updates), durch Nutzer installierte zugelassene Software (bereits genehmigt, geringe Auswirkung).

**Implementierungshinweis**: Integration der Änderungskontrolle, Änderungsklassifikation und Genehmigungsworkflows sind in ISMS-IMP-A.8.1-7-18-19-S3 definiert.

### Erkennung nicht autorisierter Software (Verbindlich)

[Organisation] muss nicht autorisierte Software erkennen und entfernen.

**Erkennungsmethoden**: Software-Inventarscans (täglich via Endgeräteverwaltungsplattform), Anwendungsmassnahmen-Alarme (nicht autorisierte Ausführungsversuche), Netzwerkverkehrsanalyse, Nutzerberichte.

**Nicht autorisierte Software umfasst**: Software ausserhalb der Liste zugelassener Software, verbotene Software (explizit untersagt), Schadsoftware, nicht genehmigte Versionen zugelassener Software, Schatten-IT (nicht genehmigte Cloud-Dienste).

**Behebungszeitrahmen**: Verbotene/schädliche Software innerhalb von 24 Stunden entfernt, nicht autorisierte Software innerhalb von 7 Tagen entfernt (oder genehmigt bei legitimem geschäftlichem Bedarf).

**Implementierungshinweis**: Erkennungsverfahren, Behebungsworkflows und Ursachenanalyse sind in ISMS-IMP-A.8.1-7-18-19-S3 definiert.

### Anwendungskontrolltechnologie (Verbindlich)

[Organisation] muss Anwendungskontrolltechnologien zur Einschränkung der Softwareausführung implementieren.

**Anwendungskontrollansätze**:

- Whitelisting (bevorzugt): Nur zugelassene Software darf ausgeführt werden, Standard-Verweigerung für alle anderen ausführbaren Dateien
- Blacklisting (ergänzend): Bekannte schädliche/verbotene Software gesperrt, Standard-Erlaubnis für alles andere

**Geltungsbereich Anwendungskontrolle**: Ausführbare Dateien (.exe, .com, .bat, .ps1), Skripte (PowerShell, VBScript, JavaScript), Bibliotheken (DLLs, dylibs, .so-Dateien), Installationspakete (MSI, PKG, DEB, RPM), Browser-Erweiterungen und Add-ons.

**Durchsetzung**:

- Organisationseigene Laptops/Desktops: Whitelisting durchgesetzt (verbindlich)
- BYOD-Geräte: Nur containerisierte Apps (Corporate-Container-Whitelisting)
- Server: Striktes Whitelisting (Änderungskontrolle für neue Software erforderlich)

**Implementierungshinweis**: Auswahl der Anwendungskontrolltechnologie, Whitelisting-Regelkonfiguration und Durchsetzungsmechanismen sind in ISMS-IMP-A.8.1-7-18-19-S3 definiert.

### Software-Schwachstellenmanagement (Verbindlich)

[Organisation] muss installierte Software mit Sicherheits-Patches und Updates aktuell halten.

**Patch-Anforderungen**:

- Kritische Sicherheits-Patches: Innerhalb von 7 Tagen nach Veröffentlichung installiert
- Hochgradige Patches: Innerhalb von 30 Tagen nach Veröffentlichung installiert
- Mittlere/niedrige Patches: Innerhalb von 90 Tagen nach Veröffentlichung installiert
- Zero-Day-Exploits: Notfall-Patching (innerhalb von 24–48 Stunden)

**Software-Lebenszyklusmanagement**: End-of-Life-Software identifiziert und vor Ende des Anbietersupports ersetzt, nicht unterstützte Software als hohes Risiko markiert mit erforderlichen kompensierenden Massnahmen.

**Integration**: Software-Schwachstellenmanagement integriert sich mit ISMS-POL-A.8.8 (Schwachstellenmanagement).

**Implementierungshinweis**: Patch-Management-Verfahren, Testanforderungen und Lebenszyklusverfolgung sind in ISMS-IMP-A.8.1-7-18-19-S3 und ISMS-POL-A.8.8 definiert.

### BYOD-Softwarekontrolle (Bedingt)

[Organisation] muss Softwaremassnahmen für den Zugriff auf Unternehmensdaten auf BYOD-Geräten implementieren (falls BYOD-Programm implementiert).

**BYOD-Softwareansatz**:

- Containerisierte Apps: Corporate Apps im verwalteten Container installiert (MAM-Lösung)
- Kein persönliches App-Inventar: [Organisation] inventarisiert oder kontrolliert keine persönlichen Apps (Datenschutz)
- Nur Container-Massnahmen: Anwendungskontrolle nur auf Corporate-Container angewendet
- Einschränkungen persönlicher Apps: Keine Einschränkungen bei der Installation persönlicher Apps (Nutzerprivatsphäre), Unternehmensdaten können nicht in persönliche Apps kopiert werden (DLP-Massnahmen)

**Implementierungshinweis**: BYOD-Softwarekontrollgestaltung, MAM-Konfiguration und DLP-Integration sind in ISMS-IMP-A.8.1-7-18-19-S3 definiert.

---

# Rollen und Verantwortlichkeiten

## Verantwortlichkeitsmatrix (RACI)

| Rolle | A.8.1 Endgeräte | A.8.7 Malware | A.8.18 Hilfsprogramme | A.8.19 Software | Gesamtrahmen |
|-------|----------------|---------------|----------------------|-----------------|--------------|
| **ISB** | Accountable | Accountable | Accountable | Accountable | Accountable |
| **IT-Sicherheitsmanager** | Verantwortlich | Verantwortlich | Verantwortlich | Verantwortlich | Verantwortlich |
| **Endgeräteadministratoren** | Verantwortlich | Verantwortlich | Beratend | Beratend | Verantwortlich |
| **Security Operations (SOC)** | Beratend | Verantwortlich | Verantwortlich | Beratend | Beratend |
| **IT-Servicedesk** | Informiert | Informiert | Informiert | Informiert | Informiert |
| **Endnutzer** | Verantwortlich (Compliance) | Informiert | Informiert | Informiert | Verantwortlich (Compliance) |
| **Asset Management** | Beratend | Informiert | Informiert | Informiert | Beratend |
| **Änderungsmanagement** | Beratend | Informiert | Beratend | Verantwortlich (Genehmigungen) | Beratend |

**RACI-Legende**: V = Verantwortlich (führt aus), A = Accountable (Entscheidungsbefugnis), B = Beratend (Input eingeholt), I = Informiert (wird informiert)

## Schlüsselrollen

**Informationssicherheitsbeauftragter (ISB)**:

- Gesamtverantwortung für den Endgerätesicherheitsrahmen
- Genehmigung der Endgerätesicherheitsrichtlinie und wesentlicher Ausnahmen
- Ressourcenzuweisung für die Implementierung der Endgerätesicherheit
- Executive-Reporting über den Sicherheitsstatus der Endgeräte
- Risikoakzeptanz für Endgerätesicherheitslücken

**IT-Sicherheitsmanager**:

- Tägliches Management der Endgerätesicherheitsmassnahmen
- Implementierung und Wartung des Endgerätesicherheitsrahmens
- Koordination von Endgerätesicherheitsbewertungen
- Management von Endgerätesicherheitsvorfällen
- Compliance-Status-Reporting an ISB
- Empfehlung von Richtlinienaktualisierungen und Massnahmenverbesserungen

**Endgeräteadministratoren**:

- Deployment und Konfiguration von Endgeräteverwaltungsplattformen
- Durchsetzung von Sicherheits-Baselines und -konfigurationen
- Management der Verschlüsselungsimplementierung auf Endgeräten
- Durchführung von Endgeräteinventarmanagement
- Behebung von Endgerätesicherheitsproblemen
- Implementierung von Sicherheits-Patches und Updates

**Security Operations Center (SOC)**:

- Überwachung von Anti-Malware/EDR-Alarmen
- Triage und Reaktion auf Schadsoftware-Vorfälle
- Untersuchung von Sicherheitsereignissen auf Endgeräten
- Koordination der Incident-Response bei Endgeräte-Kompromittierungen
- Überwachung der Nutzung privilegierter Hilfsprogramme auf Anomalien
- Eskalation kritischer Endgerätesicherheitsereignisse

**Endnutzer**:

- Einhaltung der Endgerätesicherheitsanforderungen
- Unverzügliche Meldung verlorener/gestohlener Geräte
- Meldung vermuteter Schadsoftware oder Sicherheitsvorfälle
- Teilnahme an Sicherheitssensibilisierungsschulungen
- Aufrechterhaltung der physischen Sicherheit zugewiesener Endgeräte
- Keine Versuche, Sicherheitsmassnahmen zu umgehen

---

# Integration und Implementierung

## Integration mit anderen ISMS-Massnahmen

**Kritische Integrationspunkte**:

| Verwandte Massnahme | Integrationspunkt | Abhängigkeit |
|--------------------|-------------------|--------------|
| **A.5.9 — Asset-Inventar** | Endgeräteinventar fliesst in Asset-Inventar ein | Endgeräte = Informationswerte |
| **A.8.2 — Privilegierte Zugriffsrechte** | Zugang zu privilegierten Hilfsprogrammen ist Teilmenge des PAM | Nutzer privilegierter Hilfsprogramme benötigen Governance |
| **A.8.3 — Einschränkung des Informationszugangs** | Endgeräteauthentifizierung erzwingt Zugangsbeschränkungen | BYOD-Containerisierung trennt Daten |
| **A.8.5 — Sichere Authentifizierung** | Endgeräteauthentifizierung implementiert sichere Authentifizierung | MFA für Endgeräte und privilegierte Hilfsprogramme |
| **A.8.8 — Schwachstellenmanagement** | Software-Patching behebt Endgeräteschwachstellen | Schwachstellen-Scans identifizieren ungepatchte Software |
| **A.8.9 — Konfigurationsmanagement** | Endgeräte-Baselines sind verwaltete Konfigurationen | Baseline-Abweichung = Konfigurationsabweichung |
| **A.8.15 — Protokollierung** | Endgerätesicherheitsereignisse zentral protokolliert | Nutzungsprotokolle privilegierter Hilfsprogramme fliessen ins SIEM |
| **A.8.16 — Überwachung** | Endgerätesicherheitsüberwachung implementiert Überwachungsaktivitäten | SOC überwacht Endgerätesicherheitsereignisse |
| **A.8.20-22 — Netzwerksicherheit** | Endgerät-Netzwerksicherheit ergänzt Netzwerkinfrastruktursicherheit | NAC verifiziert Endgeräte-Compliance |
| **A.6.7 — Mobiles Arbeiten** | Remote-Endgeräte haben zusätzliche Sicherheitsanforderungen | VPN-Durchsetzung, stärkere Verschlüsselung |
| **A.5.23 — Cloud-Dienste** | Cloudbasierte Anti-Malware/EDR sind Cloud-Dienste | Cloud-Sicherheitsrichtlinie definiert Genehmigungsprozess |

## Implementierungsressourcen

**Implementierungshinweise** (ISMS-IMP-A.8.1-7-18-19-Suite):

- **ISMS-IMP-A.8.1-7-18-19-S1**: Endgeräteerkennung
- **ISMS-IMP-A.8.1-7-18-19-S2**: Deployment Malware-Schutz
- **ISMS-IMP-A.8.1-7-18-19-S3**: Softwarekontrollprozess
- **ISMS-IMP-A.8.1-7-18-19-S4**: Verwaltung privilegierter Hilfsprogramme

## Bewertung und Verifikation

**Bewertungshäufigkeit**:

- Kontinuierlich: Automatisierte Compliance-Überwachung via MDM (täglich)
- Wöchentlich: Baseline-Compliance-Scans, Inventaraktualisierungen, Signaturverifikation
- Monatlich: Umfassendes Compliance-Reporting (alle Kennzahlen)
- Vierteljährlich: Executive Dashboard und Trendanalyse
- Jährlich: Vollständige Bewertung, Prüferüberprüfung, Richtlinienüberprüfung

**Compliance-Bewertung**: Massnahmenspezifische Bewertung für A.8.1, A.8.7, A.8.18, A.8.19 ermöglicht unabhängige SoA-Bewertung. Gesamtpunktzahl Endgerätesicherheit wird im Summary Dashboard für Executive-Reporting verfolgt.

**Compliance-Schwellenwerte**:

- Compliant (Grün): ≥ 90 %
- Teilweise compliant (Gelb): 70–89 %
- Nicht compliant (Rot): < 70 %

## Ausnahmenmanagement

**Wann Ausnahmen erforderlich**: Technische Einschränkung verhindert Compliance, geschäftliche Anforderung kollidiert mit Sicherheitsmassnahme, Kosten-Nutzen-Analyse bevorzugt alternative Massnahme, vorübergehende Ausnahme während Migration/Upgrade.

**Genehmigungsbehörde für Ausnahmen**:

- Geringes Risiko: IT-Sicherheitsmanager
- Mittleres Risiko: ISB (Risikobewertung erforderlich)
- Hohes Risiko: ISB + Risikoausschuss (kompensierende Massnahmen verbindlich, Executive-Benachrichtigung)
- Dauerhafte Ausnahmen: ISB + Risikoausschuss (jährliche Rezertifizierung erforderlich)

**Kompensierende Massnahmen**: Für alle Ausnahmen erforderlich. Kompensierende Massnahmen verringern das Risiko, wenn die primäre Massnahme nicht implementiert werden kann.

**Ausnahmenverfolgung und -überprüfung**: Alle genehmigten Ausnahmen im zentralen Ausnahmenregister dokumentiert, temporäre Ausnahmen monatlich überprüft, dauerhafte Ausnahmen jährlich überprüft, Hochrisiko-Ausnahmen vierteljährlich überprüft.

## Regulatorisches Mapping

Diese Richtlinie adressiert Endgerätesicherheitsanforderungen aus mehreren regulatorischen Rahmenwerken:

| Anforderungskategorie | Schweizerisches nDSG | EU DSGVO | ISO 27001 | PCI DSS v4.0.1* | HIPAA* | FINMA* | DORA/NIS2* |
|----------------------|---------------------|---------|-----------|---------|--------|--------|------------|
| **Endgeräteinventar** | Art. 8 | Art. 32 | A.8.1 | Anf. 2, 11 | §164.310(d)(1) | Risikobasiert | Asset Management |
| **Verschlüsselung** | Art. 8 | Art. 32 | A.8.1 | Anf. 3 | §164.312(a)(2)(iv) | Risikobasiert | Datenschutz |
| **Malware-Schutz** | Art. 8 | Art. 32 | A.8.7 | Anf. 5 | §164.308(a)(5)(ii)(B) | Risikobasiert | Cyber-Resilienz |
| **Zugangsmassnahmen** | Art. 8 | Art. 32 | A.8.18 | Anf. 7, 8 | §164.312(a)(1) | Risikobasiert | Zugriffsmanagement |
| **Softwaremassnahmen** | Art. 8 | Art. 32 | A.8.19 | Anf. 6 | §164.308(a)(5)(ii)(B) | Risikobasiert | Änderungsmanagement |
| **Protokollierung und Überwachung** | Art. 8 | Art. 32 | A.8.15, A.8.16 | Anf. 10 | §164.308(a)(1)(ii)(D) | Risikobasiert | Sicherheitsüberwachung |

*Bedingte Anwendbarkeit gemäss ISMS-POL-00

## Schulung und Sensibilisierung

**Sicherheitssensibilisierung** (Alle Mitarbeitenden):

- Jährliches Schulungsmodul zu Endgerätesicherheit und Nutzerverantwortlichkeiten
- Nutzerverantwortlichkeiten für physische Sicherheit, Meldung verlorener/gestohlener Geräte, Erkennung von Schadsoftware
- Schulungsabschluss: ≥ 95 % jährlich

**Technische Schulung** (IT-Betrieb, Endgeräteadministratoren):

- Konfiguration und Betrieb der Endgeräteverwaltungsplattform
- Deployment und Durchsetzung von Sicherheits-Baselines
- Konfiguration und Überwachung von Anti-Malware/EDR
- Incident-Response-Verfahren
- Bewertung von Ausnahmeanfragen

**Datenschutzschulung** (Datenschutzbeauftragter, Rechts-/Compliance):

- Datenschutzmassnahmen des BYOD-Programms
- Datenschutzrechte der Nutzer und organisatorische Grenzen
- Handhabung von Betroffenenanfragen (Datenlöschung auf Endgeräten)

**Management-Schulung** (Dateneigentümer, Systemeigentümer, Management):

- Governance und Risikobewertung der Endgerätesicherheit
- Entscheidungsfindung bei Ausnahmegenehmigungen
- Interpretation von Compliance-Berichten

---

# Definitionen

| Begriff | Definition |
|---------|------------|
| **Endgerät** | Jedes benutzerseitige Gerät, das Organisationsinformationen speichert, verarbeitet oder darauf zugreift (Laptops, Desktops, mobile Geräte, Tablets, IoT-Geräte) |
| **EDR (Endpoint Detection and Response)** | Erweiterte Endgerätesicherheitslösung mit Echtzeit-Überwachung, Bedrohungserkennung, Untersuchung und automatisierten Reaktionsfähigkeiten über klassisches Antivirus hinaus |
| **MAM (Mobile Application Management)** | Verwaltung von Unternehmensanwendungen auf mobilen Geräten, insbesondere in BYOD-Szenarien, mit Unternehmens-App/-Datenkontrolle unter Wahrung der Nutzerprivatsphäre |
| **MDM (Mobile Device Management)** | Zentralisierte Verwaltung mobiler Geräte, Durchsetzung von Sicherheitsrichtlinien, Deployment von Konfigurationen und Remote-Wipe-Fähigkeiten |
| **Privilegiertes Hilfsprogramm** | Softwarewerkzeug, das System- und Anwendungssicherheitsmassnahmen übersteuern oder umgehen kann (z. B. Registrierungseditoren, Debugger, Administratorenwerkzeuge) |
| **BYOD (Bring Your Own Device)** | Programm, das Mitarbeitenden ermöglicht, persönliche Geräte für berufliche Zwecke zu verwenden, vorbehaltlich Sicherheits- und Datenschutzmassnahmen |
| **Sicherheits-Baseline** | Mindestanforderungen für die Sicherheitskonfiguration von Endgeräten, typischerweise ausgerichtet an Anbietersicherheitsleitlinien (Microsoft, Apple) und CIS Benchmarks |
| **Anwendungskontrolle (Whitelisting)** | Sicherheitsmassnahme, die nur explizit zugelassener Software die Ausführung erlaubt, alle anderen ausführbaren Dateien standardmässig blockiert |
| **Vollständige Festplattenverschlüsselung (FDE)** | Verschlüsselung vollständiger Festplatten-Volumes zum Schutz ruhender Daten vor unbefugtem physischem Zugriff |
| **Manipulationsschutz** | Anti-Malware-Funktion, die verhindert, dass Schadsoftware oder unbefugte Nutzer Sicherheitssoftware deaktivieren, ändern oder deinstallieren |
| **Zero-Day-Bedrohung** | Zuvor unbekannte Schadsoftware oder Exploit, noch nicht durch signaturbasiertes Antivirus erkannt, erfordert verhaltens- oder ML-basierte Erkennung |
| **Konfigurationsabweichung** | Abweichung von der genehmigten Sicherheits-Baseline-Konfiguration, typischerweise durch manuelle Änderungen, Software-Updates oder Richtlinieninkonsistenzen verursacht |

---

# Genehmigungsnachweis

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date to be set] |
| **IT-Leiter (ITL)** | [Name] | [Date to be set] |
| **IT-Betriebsleiter** | [Name] | [Date to be set] |
| **Rechts-/Compliance-Officer** | [Name] | [Date to be set] |
| **Geschäftsleitung (GF)** | [Name] | [Date to be set] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt die Anforderungen fest. Implementierungsverfahren sind in ISMS-IMP-A.8.1-7-18-19 (UG/TG) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
