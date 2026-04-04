<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.1-7-18-19-DE:operational:OP-POL:a.8.1-7-18-19 -->
**ISMS-OP-POL-A.8.1-7-18-19 — Endgerätesicherheit**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Endgerätesicherheit |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.1-7-18-19 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstmalige operative Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt von**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Massnahmen A.8.1, A.8.7, A.8.18, A.8.19 — Benutzerendgeräte, Schutz vor Malware, Nutzung privilegierter Hilfsprogramme, Installation von Software auf Betriebssystemen

**Verwandte Annex-A-Massnahmen**:

| Massnahme | Bezug zur Endgerätesicherheit |
|-----------|-------------------------------|
| A.5.9 Inventar von Informationen und anderen zugehörigen Vermögenswerten | Endgeräteinventar und Asset-Register |
| A.5.15–18 Zugriffskontrolle und Identitätsmanagement | Benutzerauthentifizierung und Zugriffsrechte auf Endgeräten |
| A.8.2 Privilegierte Zugriffsrechte | Management privilegierter Zugänge auf Endgeräten |
| A.8.5 Sichere Authentifizierung | Authentifizierungsmechanismen für den Endgerätezugang |
| A.8.8 Management technischer Schwachstellen | Patch-Management für Endgeräte-Betriebssysteme und Anwendungen |
| A.8.9 Konfigurationsmanagement | Konfigurationsbaselines und Härtung von Endgeräten |
| A.8.20 Netzwerksicherheit | Netzwerkzulassungsanforderungen für Endgeräte |
| A.8.24 Verwendung von Kryptographie | Vollständige Festplattenverschlüsselung für Endgeräte |

**Verwandte interne Richtlinien**:

- Zugriffskontrollrichtlinie
- Richtlinie zur Verwendung von Kryptographie
- Netzwerksicherheitsrichtlinie
- Asset-Management-Richtlinie
- Richtlinie zur Informationsklassifizierung und -handhabung
- Incident-Management-Richtlinie

---

# Richtlinie zur Endgerätesicherheit

## Zweck

Diese Richtlinie dient dem Management und dem Schutz der Endgeräte der Organisation sowie der Minderung des Risikos von Malware, nicht autorisierter Software und dem Missbrauch privilegierter Hilfsprogramme.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) und die Datenschutzverordnung (DSV), indem sie technische und organisatorische Massnahmen entsprechend dem Risiko zum Schutz personenbezogener Daten (einschliesslich besonders schützenswerter Personendaten) auf Endgeräten umsetzt. Sofern die Organisation Daten von Personen in der EU/EWR verarbeitet, finden auch die DSGVO-Anforderungen Anwendung.

## Geltungsbereich

Alle Mitarbeitenden und Drittnutzer.

Alle organisationseigenen Geräte (Laptops, Desktops, Mobiltelefone, Tablets).

Alle Geräte, die für den Zugang zu, die Verarbeitung, Übertragung oder Speicherung von Organisationsinformationen verwendet werden, einschliesslich privater Geräte, soweit BYOD gestattet ist.

Virtuelle Geräte und cloud-gehostete Endpunkte, soweit anwendbar und durchführbar.

## Grundsatz

Die Geräte der Organisation müssen ausreichend vor dem Risiko von Malware, nicht autorisierter Software sowie Verlust oder Diebstahl geschützt sein. Endgeräte werden nach dem Prinzip der geringsten Berechtigung mit Security by Design und by Default verwaltet.

---

## Benutzerendgeräte

### Geräteregistrierung und -inventar

Alle Endgeräte müssen vor der Ausgabe an Benutzer im Asset-Register erfasst werden. Das Register muss Gerätetyp, Seriennummer, zugewiesenen Benutzer, Betriebssystem, Verschlüsselungsstatus und Ausgabedatum dokumentieren.

Geräte, die verloren gegangen, gestohlen, ausser Betrieb genommen oder neu zugewiesen wurden, müssen umgehend im Asset-Register aktualisiert werden.

### Endgeräte-Konfigurationsbaseline

Alle Endgeräte müssen vor der Bereitstellung auf eine dokumentierte Sicherheitsbaseline konfiguriert werden. Die Baseline muss Folgendes umfassen:

- Betriebssystem gehärtet gemäss Hersteller- und CIS-Benchmark-Vorgaben (mindestens Level 1; Level 2 für Systeme, die vertrauliche oder besonders schützenswerte Personendaten verarbeiten).
- Nicht benötigte Dienste, Ports und Standardkonten deaktiviert oder entfernt.
- Vollständige Festplattenverschlüsselung aktiviert (siehe Abschnitt Verschlüsselung).
- Malware-Schutz installiert und aktiv (siehe Abschnitt Malware-Schutz).
- Bildschirmsperre und Sitzungs-Timeout konfiguriert.
- Lokale Firewall aktiviert.
- Automatische Betriebssystem- und Anwendungsupdates aktiviert.

Die Konfigurationsbaseline muss dokumentiert und versioniert sein. Baseline-Standards müssen auf Hersteller-Härtungsanleitungen und CIS-Benchmarks verweisen. Die Baseline muss mindestens jährlich oder bei wesentlichen Änderungen am Betriebssystem oder der Bedrohungslandschaft überprüft werden.

### Endgeräteverwaltungstools

Folgende Kategorien von Verwaltungstools müssen zur Unterstützung der Endgerätesicherheit eingesetzt werden:

| Kategorie | Zweck | Beispiele |
|-----------|-------|-----------|
| **Endpoint Detection and Response (EDR)** | Bedrohungserkennung, -untersuchung und -reaktion auf Endgeräten | CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne oder gleichwertig |
| **Mobile Device Management (MDM)** | Geräteregistrierung, Konfiguration, Compliance, Remote-Löschung | Jamf Pro, Microsoft Intune, VMware Workspace ONE oder gleichwertig |
| **Patch-Management** | Automatisierte Bereitstellung und Compliance-Berichterstattung für Betriebssystem- und Anwendungs-Patches | WSUS, Jamf Pro, ManageEngine oder gleichwertig |
| **Verschlüsselungsschlüssel-Hinterlegung** | Zentralisierte Recovery-Key-Speicherung für die vollständige Festplattenverschlüsselung | MDM-integriert oder dediziertes Schlüsselmanagement |
| **Software-Freigabe** | Anwendungs-Allow-Listing und Installationskontrolle | AppLocker, Santa, MDM-Anwendungskatalog oder gleichwertig |

### Verschlüsselung

Alle Endgeräte (Laptops, Desktops, Mobilgeräte) müssen mit vollständiger Festplattenverschlüsselung ausgestattet sein:

| Plattform | Verschlüsselungstechnologie | Mindeststandard |
|-----------|----------------------------|-----------------|
| Windows | BitLocker | AES-XTS 256-Bit |
| macOS | FileVault | XTS-AES 128-Bit |
| Mobil (iOS/Android) | Native Geräteverschlüsselung | Standardmässig aktiviert; aktiv verifizieren |
| Linux | LUKS / dm-crypt | AES-XTS 256-Bit |

- Die Geräteverschlüsselung darf nicht durch den Endbenutzer deaktiviert werden.
- Recovery-Keys müssen zentral über MDM (z. B. Jamf Pro, Intune oder gleichwertig) oder eine gleichwertige, von der IT verwaltete Schlüsselhinterlegungslösung gespeichert werden. Der Zugang zu Recovery-Keys muss protokolliert und auf autorisiertes IT-Personal beschränkt sein.
- Der Verschlüsselungsstatus muss überprüft werden, bevor das Gerät zur Nutzung mit vertraulichen Daten freigegeben wird.

### Bildschirmsperre und Sitzungs-Timeout

- Geräte müssen sich nach **15 Minuten** Inaktivität automatisch sperren. Geräte mit Zugang zu vertraulichen oder besonders schützenswerten Personendaten müssen sich nach **5 Minuten** Inaktivität sperren.
- Benutzer müssen ihre Geräte manuell sperren, wenn sie diese unbeaufsichtigt lassen (Windows+L, Ctrl+Command+Q oder gleichwertig).
- Zur Entsperrung muss eine Authentifizierung (Passwort, PIN oder biometrisch) erforderlich sein.
- Sperrung beim Ruhezustand und beim Schliessen des Deckels muss auf allen Laptops aktiviert sein.

### Physische Sicherheit

- Geräte dürfen nicht unbeaufsichtigt an öffentlichen Orten oder sichtbar in unbeaufsichtigten Fahrzeugen zurückgelassen werden.
- Kabelschlösser sollten für Desktop-Geräte in gemeinsam genutzten oder öffentlichen Bereichen verwendet werden.
- Tragbare Geräte müssen bei Nichtgebrauch sicher aufbewahrt werden (abgeschlossene Schublade oder Schrank).
- Der Verlust oder Diebstahl eines Geräts muss dem Informationssicherheits-Managementteam unverzüglich gemeldet werden.

### Remote-Löschung

Die Organisation muss die Fähigkeit aufrechterhalten, verlorene oder gestohlene Geräte über die MDM-Plattform oder ein gleichwertiges Verwaltungstool remote zu löschen oder zu sperren.

Remote-Löschungsprozess:

1. Gerät als verloren oder gestohlen gemeldet — Mitarbeitender benachrichtigt sofort IT und direkte Führungskraft.
2. IT initiiert **Remote-Sperre** innerhalb von **1 Stunde** nach der Meldung während der Geschäftszeiten (zu Beginn des nächsten Arbeitstages bei Meldungen ausserhalb der Geschäftszeiten).
3. Wird das Gerät nicht innerhalb von **24 Stunden** wiedergefunden, initiiert die IT die **Remote-Löschung**.
4. Die Bestätigung der Remote-Löschung muss dokumentiert werden, einschliesslich Datum, Geräte-ID, Löschstatus (bestätigt/ausstehend) und autorisierender Person.
5. Bei der Löschung eines BYOD-Geräts darf nur der Organisations-Container oder das Arbeitsprofil gelöscht werden (keine persönlichen Daten), es sei denn, der Mitarbeitende hat der vollständigen Löschung in der BYOD-Vereinbarung zugestimmt.

### BYOD (Bring Your Own Device)

Wenn die Organisation die Nutzung privater Geräte für den Zugang zu Organisationsinformationen gestattet, gelten folgende Anforderungen:

- Das Gerät muss in der MDM-Lösung (Mobile Device Management) der Organisation registriert sein.
- Geschäftsdaten müssen durch Containerisierung oder ein verwaltetes Arbeitsprofil von persönlichen Daten getrennt sein.
- Das Gerät muss dieselbe Sicherheitsbaseline wie organisationseigene Geräte erfüllen (Verschlüsselung, Bildschirmsperre, aktuelles Betriebssystem, Malware-Schutz).
- Die Organisation behält sich das Recht vor, Organisationsdaten (keine persönlichen Daten) remote vom Gerät zu löschen.
- Benutzer müssen ihre Verantwortlichkeiten anerkennen, einschliesslich physischer Schutz, Software-Updates und Zusammenarbeit bei Sicherheitsanforderungen.
- Der BYOD-Zugang muss bei Beendigung des Arbeitsverhältnisses oder Vertragsende gemäss der Zugriffskontrollrichtlinie widerrufen werden.

### BYOD-Registrierungsprozess

1. Mitarbeitender stellt IT-Antrag auf BYOD-Zugang unter Angabe von Gerätetyp, Betriebssystem und vorgesehenem geschäftlichen Verwendungsbereich.
2. IT überprüft, ob das Gerät die Mindestanforderungen erfüllt (unterstützte Betriebssystemversion, Verschlüsselungsfähigkeit, kein Jailbreak/Root).
3. Mitarbeitender unterzeichnet die BYOD-Vereinbarung mit Anerkennung der Sicherheitsanforderungen, Zustimmung zur Remote-Löschung von Organisationsdaten und Kooperationspflichten.
4. IT registriert das Gerät im MDM und konfiguriert das verwaltete Arbeitsprofil oder den Container.
5. IT überprüft die Einhaltung der Sicherheitsbaseline (Verschlüsselung aktiv, Bildschirmsperre konfiguriert, aktuelles Betriebssystem) vor der Zugangsgenehmigung.

Wenn BYOD nicht gestattet ist, muss dies festgehalten und durch technische Massnahmen durchgesetzt werden.

---

## Malware- und Antivirenschutz

### Zugelassene Software

Auf Organisationsgeräten darf nur von der Organisation genehmigte und lizenzierte Software installiert werden.

Nicht autorisierte Software, heruntergeladene Software, Freeware oder nicht genehmigte Hilfsprogramme dürfen nicht installiert werden.

### Anforderungen an den Malware-Schutz

Malware-Schutzsoftware (Endpoint Detection and Response — EDR oder Next-Generation-Antivirus — NGAV, entsprechend dem Risikoprofil der Organisation) muss auf jedem Gerät installiert sein, das diese ausführen kann.

Malware-Schutzsoftware muss:

- Erkennungsdefinitionen und Engines automatisch aktualisieren, sobald diese vom Hersteller veröffentlicht werden.
- Nicht durch den Endbenutzer modifiziert, deaktiviert oder deinstalliert werden.
- Bei einer Infektion oder einem Infektionsverdacht eine Meldung erzeugen.
- Auf automatische Reparatur oder Quarantäne verdächtiger Dateien eingestellt sein.
- Lokalen Speicher und angeschlossene Speichergeräte automatisch scannen.
- Jede aufgerufene, geänderte oder ausgeführte Datei automatisch scannen.
- Audit-Protokolle aufbewahren, die an das zentrale Protokollierungssystem weitergeleitet werden.

Infektionsverdachte müssen über den Incident-Management-Prozess behandelt werden. Folgende Ereignisse müssen eine Incident-Meldung auslösen:

- EDR-/Antivirenmeldung über bestätigte Malware-Erkennung (kein False Positive).
- Ransomware-Indikatoren (Dateiverschlüsselungsaktivität, Erpressungsdateien).
- Nicht autorisierte ausgehende Verbindungen zu bekannter Command-and-Control-Infrastruktur.
- Vom Benutzer gemeldetes verdächtiges Verhalten (unerwartete Pop-ups, Leistungsabfall, unbekannte Prozesse).
- Erkennung nicht autorisierter Software oder Tools auf dem Gerät.

### E-Mail-Schutz

E-Mail-Server und -Gateways müssen einen Malware-Scan haben, der alle ein- und ausgehenden E-Mails, einschliesslich Anhänge, überprüft.

### Web-Gateway-Schutz

Internet-Proxies oder sichere Web-Gateways müssen konfiguriert sein, um:

- Websites mit bekannt bösartigem Ruf zu blockieren.
- Inhalte auf Websites mit mittlerem Ruf auf Bedrohungen zu scannen.
- Alle Erkennungen zu protokollieren.
- Definitionsupdates automatisch zu überprüfen.

Allow-Listing und Deny-Listing müssen eingesetzt werden, um den Zugang zu genehmigten und verbotenen Web-Ressourcen zu kontrollieren.

### Dateiintegritätsüberwachung

Die Dateiintegritätsüberwachung muss für systemkritische Dateien und Dateien, die personenbezogene oder vertrauliche Daten enthalten oder den Zugang dazu ermöglichen, risikobasiert und nach Geschäftsbedarf implementiert werden.

### Kontrollen für Wechselmedien

- Autorun und Autoplay müssen für alle Wechselmedien deaktiviert sein.
- Wechselmedien müssen beim Anschluss automatisch auf Malware gescannt werden.
- Nur organisationseigene, verschlüsselte Wechselmedien dürfen für den Umgang mit vertraulichen Daten zugelassen sein, entsprechend der Richtlinie zum Informationstransfer.

---

## Schulung

Benutzer müssen im Rahmen des Sicherheitsbewusstseinsprogramms regelmässig geschult werden über:

- Erkennung von Phishing-E-Mails und Social-Engineering-Angriffen.
- Sichere Nutzung von Internet und E-Mail.
- Verwendung genehmigter Software und das Verbot nicht genehmigter Software.
- Vorgehensweise bei einem Infektionsverdacht.
- Physische Sicherheit von Geräten (Sperren, Aufbewahrung, Meldung von Verlust/Diebstahl).

---

## Privilegierte Hilfsprogramme

### Geltungsbereich

Privilegierte Hilfsprogramme sind Tools, die System- oder Anwendungskontrollen übersteuern können. Dazu gehören unter anderem:

- Systemadministrationstools (Benutzer-/Gruppenmanagement, Dienstverwaltung).
- Registry-Editoren, PowerShell (uneingeschränkte Ausführungsrichtlinie) und Befehlszeilentools mit erhöhten Berechtigungen.
- Diagnose-, Debugger- und Disk-Utilities.
- Sicherungs- und Wiederherstellungs-Utilities mit Zugang zu Rohdaten.
- Netzwerkverwaltungs- und -scan-Tools.

### Massnahmen

- Der Zugang zu privilegierten Hilfsprogrammen muss auf autorisiertes Personal beschränkt sein, basierend auf dem Prinzip der geringsten Berechtigung.
- Für den Zugang zu privilegierten Hilfsprogrammen auf kritischen Systemen muss Multi-Faktor-Authentifizierung erforderlich sein.
- Jede Ausführung privilegierter Hilfsprogramme muss protokolliert werden, einschliesslich Benutzer, Zeitstempel, Name des Hilfsprogramms und Zielsystem.
- Privilegierte Hilfsprogramme, die nicht für betriebliche Zwecke benötigt werden, müssen entfernt oder deaktiviert werden.
- Die Nutzung privilegierter Hilfsprogramme muss mindestens vierteljährlich überprüft werden, um die fortwährende Geschäftsbegründung zu verifizieren.
- Die Organisation muss eine dokumentierte Liste genehmigter privilegierter Hilfsprogramme nach Rolle führen.

---

## Installation von Software auf Betriebssystemen

### Softwareinstallationskontrollen

- Die Softwareinstallation auf Betriebssystemen darf nur durch autorisiertes Personal (IT-Administratoren oder designierte Supportmitarbeitende) durchgeführt werden.
- Standardbenutzer dürfen keine lokalen Administratorrechte haben. Wenn eine Rechteerweiterung erforderlich ist, muss ein verwalteter Mechanismus zur Berechtigungseskalation verwendet werden:
  - **Just-in-time (JIT)-Zugang**: Temporäre Rechteerweiterung für einen definierten Zeitraum (maximal 4 Stunden), automatisch nach Ablauf widerrufen.
  - **Genehmigungsworkflow**: Benutzer stellt Antrag mit geschäftlicher Begründung; IT oder direkte Führungskraft genehmigt; Rechteerweiterung wird gewährt und protokolliert.
  - Alle Berechtigungseskalationen müssen protokolliert werden (Benutzer, Zeitstempel, Begründung, Dauer, Genehmigender).
- Alle Softwareinstallationen müssen dem Änderungsmanagementprozess der Organisation folgen, einschliesslich Tests, Genehmigung und Dokumentation.
- Nur genehmigte Software aus dem Softwarekatalog der Organisation darf installiert werden. Neue Softwareanfragen müssen über einen formellen Genehmigungsprozess eingereicht werden.

### Patch-Management

Betriebssysteme, Anwendungen und Browser-Software auf Endgeräten müssen auf dem neuesten Stand gehalten werden. Sicherheits-Patches müssen gemäss folgenden Zeitrahmen angewendet werden:

| Schweregrad | Zeitrahmen |
|-------------|------------|
| Kritische Schwachstellen (CVSS 9.0+, aktive Ausnutzung) | Innerhalb von 14 Tagen |
| Hohe Schwachstellen (CVSS 7.0–8.9) | Innerhalb von 30 Tagen |
| Mittlere Schwachstellen (CVSS 4.0–6.9) | Innerhalb von 90 Tagen |
| Geringe Schwachstellen (CVSS 0.1–3.9) | Nächstes geplantes Wartungsfenster |

Patches müssen vor der Bereitstellung gemäss folgendem Ansatz getestet werden:

| Systemtyp | Testanforderung |
|-----------|-----------------|
| Standard-Endgeräte (Laptops, Desktops) | Bereitstellung auf einer **Pilotgruppe** (5–10 % der Geräte) für **48 Stunden** vor dem vollständigen Rollout |
| Mobilgeräte | Bereitstellung auf einer Pilotgruppe via MDM für 48 Stunden vor dem vollständigen Rollout |
| Spezialisierte Endgeräte (Kioske, Laborsysteme) | Test in Nicht-Produktionsumgebung vor der Bereitstellung |

- **P0-Notfall-Patches** (aktive Ausnutzung bestätigt) können mit ISB-Genehmigung den Pilottest umgehen. Für 48 Stunden nach der Bereitstellung ist erhöhte Überwachung und ein dokumentierter Rollback-Plan erforderlich.
- **Patch-Fehlerbehandlung**: Wenn ein Patch bei der Pilotgruppe betriebliche Probleme verursacht, muss die Bereitstellung gestoppt, das Problem dokumentiert und der Hersteller kontaktiert werden. Eine Übergangslösung oder kompensierende Massnahme muss angewendet werden, bis ein stabiler Patch verfügbar ist.

Automatische Updates müssen für Betriebssysteme und unterstützte Anwendungen aktiviert sein. Geräte, die kritische Patches nicht innerhalb des definierten Zeitrahmens angewendet haben, müssen zur Behebung markiert oder vom Netzwerkzugang ausgeschlossen werden.

### Rollback

Vor der Anwendung von Updates oder Installationen auf Betriebssystemen muss eine Rollback-Strategie vereinbart werden, um die Geschäftskontinuität sicherzustellen, falls ein Patch Probleme verursacht.

### Audit-Trail

Eine Aufzeichnung aller Softwareänderungen auf Betriebssystemen muss geführt werden, einschliesslich Softwarename, Version, Installationsdatum und durchführende Person.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|----------------------|
| **ISB** | Richtlinienverantwortung; Genehmigung von Ausnahmen und Notfall-Patch-Umgehungen; Eskalationsstelle bei Nichteinhaltung |
| **IT-Betrieb / Endgeräteteam** | Gerätebereitstellung, Baseline-Konfiguration, MDM-Management, Patch-Bereitstellung, Remote-Löschungsausführung |
| **Informationssicherheits-Managementteam** | EDR-Überwachung, Malware-Incident-Triage, Überprüfungen privilegierter Hilfsprogramme, Compliance-Berichterstattung |
| **Asset-Eigentümer / direkte Führungskraft** | Genehmigung von Gerätezuteilung, BYOD-Anfragen und Softwareanfragen für ihr Team |
| **Alle Benutzer** | Physische Sicherheit der Geräte, sofortige Meldung von Verlust/Diebstahl, Zusammenarbeit bei Sicherheitsanforderungen, keine Deaktivierung von Sicherheitskontrollen |

---

## Nachweise

Die folgenden Nachweise belegen die Einhaltung dieser Richtlinie:

| # | Nachweis | Eigentümer | Häufigkeit |
|---|----------|------------|------------|
| 1 | **Endgeräteinventar** (Asset-Register mit Verschlüsselungsstatus, Betriebssystemversion, zugewiesenem Benutzer) | IT-Betrieb | *Ereignisbasiert aktualisiert; vollständige Prüfung jährlich* |
| 2 | **Dokumentation der Endgeräte-Konfigurationsbaseline** und Compliance-Scan-Berichte | IT-Betrieb | *Baseline jährlich überprüft; Compliance-Scans monatlich* |
| 3 | **Berichte zur Malware-Schutzbereitstellung** und Aktualisierungsstatus (Abdeckungsprozentsatz, Aktualität der Definitionen) | Informationssicherheit | *Monatliche Berichte; Ziel: 100 % Abdeckung* |
| 4 | **Malware-Erkennungs- und Incident-Protokolle** (Erkennungen, Quarantäneaktionen, Incident-Eskalationen) | Informationssicherheit | *Monatlich überprüft; 12 Monate aufbewahrt* |
| 5 | **Softwareinstallationsnachweise** und Änderungsmanagement-Genehmigungen | IT-Betrieb | *Ereignisbasiert; vierteljährlich geprüft* |
| 6 | **Liste der genehmigten privilegierten Hilfsprogramme** und Nutzungsprotokolle | Informationssicherheit | *Liste vierteljährlich überprüft; Protokolle 12 Monate aufbewahrt* |
| 7 | **Patch-Compliance-Berichte** (Prozentsatz aktueller Geräte, überfällige Patches nach Schweregrad) | IT-Betrieb | *Monatlich; Ziel: ≥95 % innerhalb der SLA aktuell* |
| 8 | **BYOD-Registrierungsnachweise** und MDM-Compliance-Status (falls zutreffend) | IT-Betrieb | *Ereignisbasiert aktualisiert; halbjährlich überprüft* |
| 9 | **Remote-Löschungsnachweise** (Geräte-ID, Datum, Löschstatus, autorisierende Person) | IT-Betrieb | *Ereignisbasiert; 3 Jahre aufbewahrt* |
| 10 | **Pilotgruppen-Patch-Testnachweise** (Testergebnisse, identifizierte Probleme, Rollout-Entscheidungen) | IT-Betrieb | *Pro Patch-Zyklus* |

---

# Richtlinien-Compliance

## Compliance-Messung

Das Informationssicherheits-Managementteam wird die Einhaltung dieser Richtlinie durch verschiedene Methoden überprüfen, einschliesslich, aber nicht beschränkt auf, Endgeräte-Compliance-Scans, Malware-Erkennungsberichte, Patch-Statusberichte, Software-Inventarprüfungen, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vorab vom Informationssicherheitsmanager genehmigt und dokumentiert werden, mit dokumentierter Risikoakzeptanz, kompensierenden Massnahmen und einem definierten Überprüfungsdatum. Ausnahmen müssen dem Management Review Team gemeldet werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstösst, kann disziplinarisch massregelt werden, bis hin zur Beendigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen berücksichtigen Änderungen der Endgeräte-Sicherheitsstandards, neue Bedrohungen (einschliesslich neuer Malware-Techniken und Angriffsvektoren), regulatorische Änderungen und Erkenntnisse aus Incidents.

---

# Abgedeckte Bereiche des ISO 27001-Standards

Endgerätesicherheitsrichtlinie — Zuordnung der ISO 27001-Massnahmen

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Engagement | 5.1 Richtlinien zur Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Verantwortlichkeiten des Managements |
| Klausel 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| Klausel 7.3 Bewusstsein | 6.3 Bewusstsein, Schulung und Training zur Informationssicherheit |
| | 6.4 Disziplinarverfahren |
| | **8.1 Benutzerendgeräte** |
| | **8.7 Schutz vor Malware** |
| | **8.18 Nutzung privilegierter Hilfsprogramme** |
| | **8.19 Installation von Software auf Betriebssystemen** |
| | 8.23 Web-Filterung |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmenwerk | Relevanz |
|------------|----------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen für den Datenschutz |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (soweit anwendbar) | Art. 32 — Sicherheit der Verarbeitung (Endgerätekontrollen als angemessene Massnahme) |
| ISO/IEC 27001:2022 | Annex-A-Massnahmen 8.1, 8.7, 8.18, 8.19 |
| ISO/IEC 27002:2022 | Abschnitte 8.1, 8.7, 8.18, 8.19 — Implementierungsanleitung |
| NIST SP 800-53 Rev 5 | SC-28 (Schutz ruhender Informationen), SI-3 (Schutz vor Schadcode), CM-11 (Benutzerseitig installierte Software) |
| CIS Controls v8 | Massnahme 2 (Inventar und Kontrolle von Software-Assets), Massnahme 4 (Sichere Konfiguration), Massnahme 10 (Malware-Abwehr) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
