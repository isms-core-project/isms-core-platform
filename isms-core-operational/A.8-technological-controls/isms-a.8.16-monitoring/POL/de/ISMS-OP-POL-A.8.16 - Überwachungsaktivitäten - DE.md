<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.16-DE:operational:OP-POL:a.8.16 -->
**ISMS-OP-POL-A.8.16 — Überwachungsaktivitäten**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Überwachungsaktivitäten |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.16 |
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
| 1.0 | [Datum] | ISB | Erstversion der operativen Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt von**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Massnahme A.8.16 — Überwachungsaktivitäten

**Verwandte Annex-A-Massnahmen**:

| Massnahme | Bezug zu Überwachungsaktivitäten |
|-----------|----------------------------------|
| A.5.7 Bedrohungsintelligenz | Bedrohungsintelligenz informiert Überwachungsregeln und Erkennungsmuster |
| A.5.24–28 Vorfallmanagement | Überwachung löst Vorfallserkennung und Eskalation aus |
| A.5.28 Sammlung von Beweisen | Überwachungsdaten dienen als forensische Beweise |
| A.5.34 Datenschutz und Schutz personenbezogener Daten | Mitarbeiterüberwachung muss Datenschutzanforderungen einhalten |
| A.8.7 Schutz vor Malware | Malware-Erkennungsereignisse fliessen in Überwachung ein |
| A.8.15 Protokollierung | Protokolle liefern die Rohdaten, die die Überwachung analysiert |
| A.8.17 Zeitsynchronisation | Genaue Zeitstempel sind für die Ereigniskorrelation unerlässlich |
| A.8.20 Netzwerksicherheit | Netzwerkverkehr ist eine primäre Überwachungsdatenquelle |

**Verwandte interne Richtlinien**:

- Protokollierungsrichtlinie (A.8.15)
- Richtlinie zum Vorfallmanagement
- Netzwerksicherheitsrichtlinie
- Endpunkt-Sicherheitsrichtlinie
- Zugangskontrollrichtlinie
- Richtlinie zum Datenschutz und Schutz personenbezogener Daten

---

# Richtlinie zu Überwachungsaktivitäten

## Zweck

Zweck dieser Richtlinie ist es, die Anforderungen für die aktive Überwachung von Netzwerken, Systemen und Anwendungen zur Erkennung anomalen Verhaltens, Sicherheitsbedrohungen und Richtlinienverletzungen zu definieren. Während Protokollierung (A.8.15) Ereignisse erfasst und aufbewahrt, analysiert Überwachung diese Ereignisse in Echtzeit oder nahezu in Echtzeit, um Bedrohungen zu identifizieren und darauf zu reagieren, bevor sie Schaden anrichten.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 8 durch die Implementierung von Überwachung als technische und organisatorische Massnahme, die dem Risiko angemessen ist. Überwachungsaktivitäten sollen dem schweizerischen Arbeitsrecht (OR Art. 328/328b) und dem Verbot der Verhaltensüberwachung (ArGV3 Art. 26) entsprechen. Soweit die Organisation Daten von Personen im EU/EWR-Raum verarbeitet, gelten zudem DSGVO-Art.-32-Anforderungen.

## Geltungsbereich

Diese Richtlinie gilt für:

- Alle Netzwerke, Systeme, Anwendungen und Cloud-Dienste im ISMS-Geltungsbereich.
- Alle Überwachungstechnologien: SIEM, EDR/XDR, NDR, IDS/IPS, UEBA und gleichwertige Tools.
- Alle Mitarbeitenden und Drittbenutzer, deren Aktivitäten sicherheitsrelevante Ereignisse erzeugen.
- Alle Umgebungen: Produktion, Staging und externe Systeme.

Die Überwachung physischer Sicherheitssysteme (CCTV, Zugangsleser) wird durch die Richtlinie zur physischen Zugangskontrolle geregelt. Protokollierungskonfiguration und Protokollaufbewahrung werden durch die Protokollierungsrichtlinie (A.8.15) geregelt.

## Grundsatz

Überwachung ist eine aktive, detektive Kontrolle. Netzwerke, Systeme und Anwendungen sollen auf anomales Verhalten überwacht und angemessene Massnahmen ergriffen werden, um potenzielle Informationssicherheitsvorfälle zu bewerten. Überwachung soll auf Basis etablierter Verhaltensgrundsätze, definierter Erkennungsregeln und Bedrohungsintelligenz betrieben werden — nicht als unterschiedslose Überwachung.

---

## Was zu überwachen ist

### Überwachungsumfang

Folgendes soll auf anomales Verhalten und Sicherheitsereignisse überwacht werden:

| # | Überwachungsdomäne | Was zu überwachen ist |
|---|-------------------|----------------------|
| 1 | **Netzwerkverkehr** | Ein- und ausgehende Datenflüsse, Ost-West-(Lateral-)Verkehr zwischen Segmenten, Verbindungen zu bekannten bösartigen IPs/Domains |
| 2 | **Authentifizierung und Zugang** | Fehlgeschlagene Anmeldeversuche, unmögliche Reisebewegungen, Credential-Stuffing-Muster, Zugang von unerwarteten Standorten oder Geräten |
| 3 | **Privilegierte Aktivitäten** | Administrative Massnahmen, Privilege-Eskalationen, Nutzung von Dienstkonten, privilegierter Zugang ausserhalb der Geschäftszeiten |
| 4 | **Endpunktverhalten** | Prozessausführungsanomalien, nicht signierte Binärdateien, Skriptausführung, Persistenzmechanismen, Memory-Injection |
| 5 | **Anwendungsaktivität** | Ungewöhnliche Transaktionsvolumina, Massenoperationen, API-Missbrauchsmuster, Anwendungsfehlerspitzen |
| 6 | **Konfigurationsänderungen** | Änderungen an Sicherheitseinstellungen, Firewall-Regeln, Gruppenrichtlinien, DNS-Einträgen, Zertifikatskonfigurationen |
| 7 | **Status von Sicherheits-Tools** | Antivirus/EDR-Deaktivierung, Firewall-Regeländerungen, Protokollierungsdienst-Unterbrechungen, IDS/IPS-Umgehungsversuche |
| 8 | **Cloud-Dienste** | Administrative Konsolenzugang, Tenant-Konfigurationsänderungen, übermässige API-Aufrufe, Datenexportoperationen |
| 9 | **Datenbewegung** | Grosse Dateiübertragungen, Massendownloads, USB-Gerätenutzung, Cloud-Speicher-Uploads, E-Mail-Anhänge über Schwellenwerten |
| 10 | **Ressourcenauslastung** | CPU/Speicher/Festplatten-/Bandbreite-Anomalien, die auf Cryptomining, DDoS-Teilnahme oder Systemkompromittierung hinweisen können |

### Priorisierung kritischer Systeme

Systeme sollen basierend auf Risiko für die Überwachung priorisiert werden:

| Priorität | Systemtyp | Überwachungsgrad |
|-----------|-----------|-----------------|
| **Kritisch** | Authentifizierungsinfrastruktur, Firewalls, VPN, Domain-Controller, Zahlungssysteme | Echtzeit mit automatischer Alarmierung |
| **Hoch** | Server mit vertraulichen/personenbezogenen Daten, E-Mail-Gateways, Cloud-Admin-Konsolen | Echtzeit oder nahezu in Echtzeit (innerhalb 15 Minuten) |
| **Mittel** | Interne Anwendungsserver, Entwicklungsinfrastruktur, interne Dateifreigaben | Nahezu in Echtzeit (innerhalb 1 Stunde) |
| **Standard** | Workstations, Drucker, unkritische Infrastruktur | Periodische Überprüfung (tägliche oder wöchentliche Aggregation) |

---

## Verhaltensgrundsätze

### Einrichten von Grundsätzen

Bevor die Anomalieerkennung effektiv ist, soll die Organisation Grundsätze des normalen Verhaltens einrichten. Initiale Grundsätze sollen innerhalb von 30 Tagen nach dem Einsatz der Überwachung für jedes System oder jede Systemgruppe festgestellt werden. Während der Grundsatz-Einrichtungsphase soll Überwachung im „Lernmodus" betrieben werden — Alarme sollen generiert, aber mit erhöhter Toleranz für Falsch-Positive überprüft werden, bis die Grundsätze validiert sind.

Grundsätze sollen dokumentieren:

- Systemauslastung während Standard- und Spitzenbetriebs-Zeiträumen.
- Typische Zugriffsmuster: Zeitpunkt, Standort, Häufigkeit und Volumen nach Benutzergruppe.
- Erwartete Netzwerkverkehrsflüsse: Quell-Ziel-Paare, Protokolle, Datenvolumina.
- Standardmässige Anwendungstransaktionsraten und Fehlerstufen.

Grundsätze sollen überprüft und aktualisiert werden:

- **Vierteljährlich** für allgemeine Systeme.
- **Nach wesentlichen Änderungen** (neue Systeme, Reorganisationen, Cloud-Migrationen, saisonale Geschäftszyklen).
- **Nach Vorfällen**, wo der Vorfall eine Lücke in der Grundsatzdefinition aufgedeckt hat.

### Abweichungserkennung

Überwachungssysteme sollen konfiguriert werden, Abweichungen von etablierten Grundsätzen zu erkennen, einschliesslich:

- Verkehr von oder zu bekannten bösartigen Quellen (C2-Server, Botnet-Infrastruktur, bedrohungsintelligenz-markierte IPs/Domains).
- Erkannte Angriffssignaturen und -muster (Brute Force, DDoS, Buffer Overflow, SQL-Injection, Credential Stuffing).
- Ungewöhnliches Systemverhalten: unerwartete Prozessbeendigungen, nicht autorisierte Prozessausführung, Keystroke-Logging-Indikatoren, Protokollabweichungen.
- Benutzerverhalten-Anomalien: Zugang ausserhalb normaler Arbeitszeiten, Zugang auf zuvor nicht zugegriffene Ressourcen, unmögliche Reisebewegungen zwischen geografischen Standorten. **Unmögliche Reisebewegungen** sind definiert als Authentifizierungsereignisse von zwei geografischen Standorten innerhalb eines Zeitrahmens, der physisches Reisen zwischen ihnen unplausibel macht (z. B. Anmeldungen aus Zürich und Tokio innerhalb von 2 Stunden). Die Organisation soll unmögliche Reisebewegungsparameter definieren basierend auf: maximaler plausibler Reisegeschwindigkeit, VPN/Proxy-Ausschlüssen für bekannte Corporate-Exit-Punkte und Toleranz für mobile Geräte-Standortungenauigkeit.
- Netzwerkleistungs-Anomalien: unerwartete Latenz, Bandbreitenüberlastung, ungewöhnliche DNS-Abfragevolumina.
- Ressourcenverbrauch-Anomalien: CPU-Spitzen, unerwartete Festplatten-I/O, Speichererschöpfung ohne entsprechende Arbeitslast.

---

## Überwachungsarchitektur

### Überwachungsplattform

Die Organisation soll eine zentralisierte Überwachungsplattform einsetzen, die Folgendes ermöglicht:

| Fähigkeit | Anforderung |
|-----------|-------------|
| **Ereigniskorrelation** | Ereignisse aus mehreren Quellen (Protokolle, Netzwerk, Endpunkt, Cloud, Identität) in einer einheitlichen Ansicht korrelieren |
| **Automatische Alarmierung** | Alarme basierend auf vordefinierten Regeln, Schwellenwerten und Anomalieerkennung generieren |
| **Bedrohungsintelligenz-Integration** | Externe Bedrohungsintelligenz-Feeds einlesen, um Erkennungsregeln anzureichern und bekannte Kompromittierungsindikatoren zu identifizieren |
| **Dashboards** | Echtzeitsichtbarkeit auf Sicherheitslage, Alarmvolumina und Trends bereitstellen |
| **Untersuchungsunterstützung** | Drill-Down von Alarm zu Rohereignissen für Vorfalluntersuchung ermöglichen |
| **Aufbewahrung** | Überwachungsdaten gemäss Aufbewahrungsplan der Protokollierungsrichtlinie (A.8.15) aufbewahren |

Plattformbeispiele: SIEM (z. B. Microsoft Sentinel, Splunk, Elastic SIEM, Wazuh), XDR oder gleichwertig.

### Erkennungsschichten

Ein geschichteter Überwachungsansatz soll implementiert werden:

| Schicht | Technologie | Abdeckung |
|---------|-------------|-----------|
| **Netzwerk** | NDR, IDS/IPS, Firewall-Protokolle, DNS-Überwachung | Nord-Süd- und Ost-West-Traffic-Sichtbarkeit |
| **Endpunkt** | EDR/XDR-Agenten auf allen verwalteten Geräten | Prozessausführung, Dateioperationen, Speicheranalyse |
| **Identität** | Identitätsanbieter-Überwachung, UEBA | Authentifizierungs-Anomalien, Missbrauch von Zugangsdaten, Insider-Bedrohungsindikatoren |
| **Anwendung** | An SIEM weitergeleitete Anwendungsprotokolle, WAF | Transaktions-Anomalien, Eingabevalidierungsfehler, API-Missbrauch |
| **Cloud** | Cloud-native Überwachung (z. B. AWS CloudTrail, Azure Monitor, GCP Cloud Audit Logs) | Administrative Massnahmen, Konfigurationsänderungen, Datenzugang |

Wo der Organisation die Ressourcen für ein vollständiges internes Security Operations Centre (SOC) fehlen, sollte ein Managed-Detection-and-Response-(MDR-)Dienst in Betracht gezogen werden, um 24/7-Überwachungsabdeckung zu bieten.

### Cloud-spezifische Überwachung

Für Cloud-Umgebungen (IaaS, PaaS, SaaS) gelten zusätzliche Überwachungsanforderungen:

- **Cloud-Audit-Protokolle** (AWS CloudTrail, Azure Activity Log, GCP Cloud Audit Logs) sollen an die zentralisierte Überwachungsplattform weitergeleitet werden.
- **Cloud-Sicherheitslage**-Änderungen (z. B. Erstellung öffentlicher S3-Buckets, Sicherheitsgruppen-Änderung, IAM-Richtlinienänderungen) sollen sofortige Alarme generieren.
- **Cloud-native Bedrohungserkennungsdienste** (AWS GuardDuty, Azure Defender, GCP Security Command Center) sollten aktiviert und mit der zentralisierten Überwachungsplattform integriert werden.
- **SaaS-Administrative Massnahmen** (M365-Admin-Portal, Google-Workspace-Admin, Salesforce-Setup-Änderungen) sollen auf nicht autorisierte Konfigurationsänderungen überwacht werden.
- **Cloud-API-Aktivität** soll auf ungewöhnliche Volumina, Zugang von unerwarteten Standorten und Nutzung veralteter oder hochrisikobehafteter API-Endpunkte überwacht werden.

### Überwachungssystem-Gesundheit (SOC 2: CC4.1)

Die Überwachungsinfrastruktur selbst soll überwacht werden, um kontinuierliche Verfügbarkeit sicherzustellen:

- **Dateneinnahme**: Alarm, wenn die Protokollquellen-Einnahme stoppt oder für mehr als 15 Minuten unter das Baseline-Volumen fällt.
- **Agenten-Gesundheit**: EDR/Überwachungsagenten-Status über alle Endpunkte überwachen; Alarm bei Agenten-Trennung länger als 1 Stunde.
- **Speicherkapazität**: Alarm bei 80 % Speicherauslastung mit Kapazitätsplanung für mindestens 30-tägiges Wachstum.
- **Plattformverfügbarkeit**: Ziel 99,9 % Betriebszeit für die Überwachungsplattform; Failover oder Redundanz für kritische Komponenten.
- **Monatlicher Gesundheitsbericht**: IT-Betrieb soll monatlich einen Überwachungsplattform-Gesundheitsbericht mit Betriebszeit, Einnahmeraten, Agenten-Abdeckung und Kapazitätsprojektionen erstellen.

### Phasierte Implementierungsleitfaden

Organisationen, die zum ersten Mal Überwachungsfähigkeiten einsetzen oder den Umfang erweitern, sollen einem phasierten Ansatz folgen:

| Phase | Dauer | Umfang | Ziel |
|-------|-------|--------|------|
| **Phase 1 — Fundament** | Monate 1–3 | Authentifizierungsprotokolle, Firewall-Protokolle, Endpunktschutz-Ereignisse an SIEM weitergeleitet | Grundlegende Bedrohungserkennung; Protokollkorrelationsfähigkeit |
| **Phase 2 — Erweiterung** | Monate 4–6 | Netzwerkverkehrsüberwachung, Cloud-Audit-Protokolle, Anwendungsprotokolle hinzufügen | Breitere Sichtbarkeit; Grundsatz-Einrichtung für zusätzliche Systeme |
| **Phase 3 — Reifung** | Monate 7–12 | UEBA, automatisierte Reaktions-Playbooks, MITRE-ATT&CK-Abdeckungszuordnung, erweiterte Analytik | Proaktive Bedrohungssuche; reduzierte MTTD |
| **Phase 4 — Optimierung** | Laufend | Kontinuierliches Abstimmen, Bedrohungsintelligenz-Anreicherung, Red-Team/Purple-Team-Übungen zur Validierung der Erkennung | Nachhaltige Effektivität; reduzierte Falsch-Positive |

---

## Alarmmanagement

### Alarmklassifizierung

Alarme sollen nach Schweregrad klassifiziert werden, um Reaktionszeitpläne zu steuern:

| Schweregrad | Beschreibung | Reaktionszeit | Beispiele |
|-------------|--------------|---------------|-----------|
| **Kritisch** | Aktive Kompromittierung oder unmittelbare Bedrohung | **15 Minuten** (Geschäftszeiten), **1 Stunde** (ausserhalb) | Bestätigte Malware-Ausführung, aktive Datenexfiltration, Ransomware-Indikatoren |
| **Hoch** | Wahrscheinliches Sicherheitsereignis, das Untersuchung erfordert | **1 Stunde** (Geschäftszeiten), **4 Stunden** (ausserhalb) | Mehrfache fehlgeschlagene Authentifizierungen von einer Quelle, Deaktivierung von Sicherheitskontrollen, Massendownload |
| **Mittel** | Verdächtige Aktivität, die Analyse erfordert | **4 Stunden** (Geschäftszeiten), **nächster Arbeitstag** (ausserhalb) | Einzelner fehlgeschlagener Login von ungewöhnlichem Standort, geringfügige Richtlinienverletzung, unerwartete Konfigurationsänderung |
| **Niedrig** | Informatorisch oder geringfügige Anomalie | **Nächster Arbeitstag** | Port-Scan von externer IP, blockierte Web-Anfrage an verdächtige Kategorie, geringfügige Schwellenwertüberschreitung |

### Alarm-Triage-Prozess

**Alarmreaktions-Personaleinsatzmodell**: Die Organisation soll ihren Alarmreaktions-Personaleinsatzansatz definieren:

| Modell | Abdeckung | Geeignet für |
|--------|----------|-------------|
| **Internes SOC** | Dedizierte Sicherheitsanalysten während der Geschäftszeiten; Bereitschaftsdienst-Rotation für ausserhalb | Organisationen mit ≥3 Sicherheitsmitarbeitenden; Hochrisikoumgebungen |
| **Managed Detection and Response (MDR)** | 24/7-Überwachung durch externen Anbieter; Eskalation an internes Team bei bestätigten Ereignissen | Organisationen mit begrenztem Sicherheitspersonal; kosteneffektive 24/7-Abdeckung |
| **Hybrid** | MDR für 24/7-Erst-Triage; internes Team für Untersuchung und Reaktion | Ausgewogener Ansatz; häufigste Lösung für KMU |
| **Bereitschaftsdienst-Rotation** | Überwachung während der Geschäftszeiten mit Bereitschaftsdienst für Kritische/Hohe Alarme nur ausserhalb | Minimal tragfähiger Ansatz für kleine Teams; erfordert gut abgestimmte Alarmierung |

Das gewählte Modell soll dokumentiert und vom ISB genehmigt werden. Die Reaktionsfähigkeit ausserhalb der Geschäftszeiten soll vierteljährlich getestet werden.

Wenn ein Alarm generiert wird:

1. **Empfangen**: Alarm wird von Informationssicherheitsanalyst (oder MDR-Anbieter) empfangen.
2. **Triage**: Analyst bewertet, ob der Alarm ein echtes Positiv, Falsch-Positiv ist oder weitere Untersuchung erfordert.
3. **Anreichern**: Zusätzlichen Kontext sammeln — Asset-Kritikalität, Benutzerprofil, Bedrohungsintelligenz, verwandte Ereignisse.
4. **Entscheiden**: Bei echtem Positiv oder wahrscheinlichem Sicherheitsereignis Vorfallsprotokoll gemäss Richtlinie zum Vorfallmanagement erstellen.
5. **Eskalieren**: Kritische und hohe Schweregrad-Vorfälle sofort an ISB eskalieren. Mittlere Vorfälle eskalieren, wenn nicht innerhalb definierter Zeitrahmen gelöst.
6. **Dokumentieren**: Alle Triage-Entscheidungen dokumentieren — einschliesslich Falsch-Positiver mit Begründung.

### Alarmabstimmung

Um Überwachungseffektivität zu erhalten und Alarmmüdigkeit zu minimieren:

- Erkennungsregeln sollen **monatlich** überprüft und abgestimmt werden, um Falsch-Positiv-Raten zu reduzieren.
- Unterdrückungsregeln sollen mit Begründung dokumentiert und **vierteljährlich** überprüft werden.
- Neue Erkennungsregeln sollen hinzugefügt werden, wenn: Bedrohungsintelligenz neue Angriffsmuster identifiziert, Vorfälle Erkennungslücken aufdecken oder neue Systeme/Anwendungen eingesetzt werden.
- **Änderungskontrolle für Erkennungsregeln**: Alle Änderungen an Erkennungsregeln (neue Regeln, Änderungen, Unterdrückungen, Löschungen) sollen einem dokumentierten Prozess folgen: Änderungsantrag mit Begründung, Peer-Review durch einen zweiten Analysten, Test in einer Nicht-Produktions-/Staging-Umgebung soweit machbar, Genehmigung durch den Informationssicherheitsleiter und Einsatz mit Rollback-Fähigkeit. Notfall-Regeländerungen (z. B. als Reaktion auf eine aktive Bedrohung) können den Peer-Review umgehen, sollen aber innerhalb von 48 Stunden rückwirkend überprüft werden.
- Alarmvolumina und Falsch-Positiv-Raten sollen als Schlüsselleistungsindikatoren verfolgt werden.
- Ziel: Falsch-Positiv-Rate unter **20 %** für hochgradige Alarme.
- **Falsch-Positiv-Managementprozess**: Wenn ein Falsch-Positiv identifiziert wird, soll der Analyst: (a) die Grundursache dokumentieren (falsch konfigurierte Regel, legitimer Geschäftsprozess, Umgebungsrauschen), (b) die angemessene Massnahme bestimmen (Regel abstimmen, Ausnahme hinzufügen, mit Ablaufdatum unterdrücken, akzeptieren), (c) die Änderung durch den Regeländerungskontrollprozess implementieren und (d) verifizieren, dass die Abstimmung keine echten Positiven unterdrückt. Persistente Falsch-Positiv-Quellen (>10 Vorkommen pro Woche aus derselben Regel) sollen innerhalb von 5 Arbeitstagen zur Abstimmung priorisiert werden.

---

## Überwachungsüberprüfungsplan

| Überprüfungstyp | Häufigkeit | Verantwortlich | Umfang |
|----------------|------------|----------------|--------|
| **Echtzeit-Alarmierung** | Laufend | Informationssicherheit / MDR | Kritische und hochgradige Ereignisse lösen sofortige Benachrichtigung aus |
| **Alarmwarteschlangen-Überprüfung** | Täglich | Informationssicherheitsanalyst | Ausstehende Alarme triage; Falsch-Positive schliessen; bestätigte Ereignisse eskalieren |
| **Erkennungsregel-Überprüfung** | Monatlich | Informationssicherheit | Regeln abstimmen; neue Erkennungen hinzufügen; validierte Falsch-Positive unterdrücken |
| **Überwachungsabdeckungs-Überprüfung** | Vierteljährlich | IT-Betrieb / Informationssicherheit | Alle im Geltungsbereich befindlichen Systeme überwacht verifizieren; Lücken identifizieren; neue Systeme onboarden |
| **Grundsatz-Überprüfung** | Vierteljährlich | Informationssicherheit | Verhaltensgrundsätze für Änderungen in Systemen, Benutzern oder Geschäftsbetrieb aktualisieren |
| **Effektivitätsüberprüfung** | Halbjährlich | ISB | MTTD- und MTTR-Metriken überprüfen; Erkennungsabdeckung gegen MITRE ATT&CK bewerten; an Management berichten. **Lieferergebnisse**: schriftlicher Effektivitätsbericht einschliesslich: Abdeckungslückenanalyse, MITRE-ATT&CK-Technikabdeckungs-Heatmap (Prozentsatz relevanter Techniken mit aktiven Erkennungsregeln), Trendanalyse von MTTD/MTTR/Falsch-Positiv-Raten und empfohlene Verbesserungen für den nächsten Zeitraum |

---

## Schlüsselleistungsindikatoren

Folgende Metriken sollen verfolgt werden, um Überwachungseffektivität zu messen:

| # | Metrik | Ziel | Berichterstattung |
|---|--------|------|-------------------|
| 1 | **Mean Time to Detect (MTTD)** | Kritische Ereignisse innerhalb von 15 Minuten nach Eintreten erkannt | Monatlich an ISB |
| 2 | **Mean Time to Respond (MTTR)** | Kritische Alarme innerhalb der Reaktions-SLA triage | Monatlich an ISB |
| 3 | **Überwachungsabdeckung** | 100 % der kritischen Systeme, ≥95 % aller im Geltungsbereich befindlichen Systeme. Abdeckung = (Systeme mit aktivem Überwachungsagenten + Systeme mit Protokollweiterleitung an SIEM) / gesamte im Geltungsbereich befindliche Systeme aus Inventarverzeichnis. Systeme als ausserhalb des Geltungsbereichs markiert erfordern dokumentierte Begründung. | Vierteljährlich |
| 4 | **Falsch-Positiv-Rate** | <20 % für hochgradige Alarme | Monatlich |
| 5 | **Aktualität der Erkennungsregeln** | Alle Regeln innerhalb der letzten 90 Tage überprüft | Vierteljährlich |
| 6 | **Alarmrückstand** | Kritisch: keine nicht triagerten Alarme älter als 1 Stunde; Hoch: 4 Stunden; Mittel: 24 Stunden; Niedrig: 48 Stunden | Wöchentlich |

---

## Mitarbeiterprivatsphäre und Überwachung

### Rechtliche Anforderungen

Überwachungsaktivitäten sollen dem schweizerischen Arbeitsrecht entsprechen:

- **ArGV3 Art. 26**: Überwachungs- oder Kontrollsysteme, deren einziger oder hauptsächlicher Zweck die Überwachung des Mitarbeiterverhaltens ist, sind verboten.
- **OR Art. 328b**: Mitarbeiterdatenverarbeitung muss verhältnismässig und auf das für das Arbeitsverhältnis oder zur Überprüfung der Eignung des Mitarbeitenden Notwendige beschränkt sein.
- **nDSG**: Verarbeitung von Mitarbeiterdaten durch Überwachung erfordert Rechtmässigkeit, Verhältnismässigkeit, Zweckbindung und Transparenz.

### Datenschutzgarantien

Folgende Garantien sollen angewendet werden:

- Überwachung soll **legitimen Sicherheitszwecken** dienen (Bedrohungserkennung, Vorfalluntersuchung, Compliance-Verifikation) — nicht Verhaltensüberwachung oder Leistungsmanagement.
- Mitarbeitende sollen **im Voraus informiert** werden, dass Überwachung stattfindet, was überwacht wird und warum, durch die Richtlinie zur akzeptablen Nutzung und die Anstellungsdokumentation.
- Es sollen nur die **minimal notwendigen Daten** erfasst und aufbewahrt werden (Datensparsamkeit).
- Überwachungsdaten sollen **nicht verwendet** werden für HR-Leistungsbewertung, Disziplinarmassnahmen für Nicht-Sicherheitsangelegenheiten oder allgemeines Verhaltens-Profiling.
- **Personalisierte Analyse** (Identifizierung individueller Benutzer) soll nur erfolgen, wenn: (a) ein Alarm auf einen potenziellen Sicherheitsvorfall oder eine Richtlinienverletzung hinweist und (b) die Untersuchung mit Begründung dokumentiert ist.
- Wo Überwachungsdaten mit externen Parteien geteilt werden (z. B. MDR-Anbieter, forensische Ermittler), sollen personenbezogene Identifikatoren, soweit machbar, minimiert oder anonymisiert werden.
- Eine Datenschutz-Folgenabschätzung (DSFA) gemäss nDSG Art. 22 soll vor dem Einsatz von Überwachung durchgeführt werden, die eines der folgenden Kriterien erfüllt:
  - Überwachung aller Mitarbeiter-Netzwerkaktivitäten (vollständige Paketerfassung, URL-Protokollierung).
  - Einsatz von User-and-Entity-Behaviour-Analytics (UEBA), die individuelle Mitarbeitende profilieren.
  - Überwachung, die Mitarbeiter-Standortdaten erfasst (VPN-Verbindungs-Geolokalisierung, WLAN-Positionierung).
  - Überwachung der persönlichen Geräteaktivität im Rahmen von BYOD-Vereinbarungen.
  - Jede Überwachungsaktivität, bei der der Datenschutzbeauftragte oder Datenschutzberater bestimmt, dass die Verarbeitung wahrscheinlich ein hohes Risiko für die Persönlichkeitsrechte der Mitarbeitenden darstellt.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; Genehmigung von Überwachungsumfang und Erkennungsprioritäten; Eskalationspunkt für kritische Alarme; halbjährliche Effektivitätsüberprüfung |
| **Informationssicherheitsanalyst** | Tägliche Alarm-Triage; Vorfallseskalation; Pflege von Erkennungsregeln; Falsch-Positiv-Management; monatliches Abstimmen |
| **IT-Betrieb / Plattformteam** | Überwachungsplattform-Administration; Agenten-Einsatz; Protokollquellen-Onboarding; Kapazitätsmanagement; Systemgesundheitsüberwachung |
| **Systemadministratoren** | Sicherstellen, dass Überwachungsagenten auf verwalteten Systemen installiert und betriebsbereit sind; Überwachungsfehler oder -lücken melden |
| **MDR-Anbieter** (falls anwendbar) | 24/7-Alarmüberwachung; initiale Triage und Anreicherung; Eskalation bestätigter Ereignisse gemäss vereinbarten Runbooks |
| **Datenschutzberater** | Beratung zur Datenschutzauswirkung von Überwachungsaktivitäten; DSFA-Anforderungen; Mitarbeiterbenachrichtigungsanforderungen |

---

## Nachweise

Die folgenden Nachweise demonstrieren die Einhaltung dieser Richtlinie:

| # | Nachweis | Verantwortlich | Häufigkeit |
|---|----------|----------------|------------|
| 1 | **Überwachungsplattform-Konfiguration** und Systeminventar (Datenquellen, Erkennungsregeln, Alarmweiterleitung) | IT-Betrieb | *Konfiguration dokumentiert; Datenquelleninventar vierteljährlich überprüft* |
| 2 | **Überwachungsabdeckungsmetrik** (Prozentsatz der im Geltungsbereich befindlichen Systeme mit aktiver Überwachung) | IT-Betrieb / Informationssicherheit | *Vierteljährlich; Ziel: 100 % kritisch, ≥95 % alle im Geltungsbereich* |
| 3 | **Verhaltensgrundsatz-Dokumentation** für kritische Systeme und Benutzergruppen | Informationssicherheit | *Dokumentiert; vierteljährlich und nach wesentlichen Änderungen überprüft* |
| 4 | **Alarm-Triage-Aufzeichnungen** mit Klassifizierung, Triage-Entscheidung und Reaktionszeitplan | Informationssicherheit | *12 Monate aufbewahrt; bei Revision entnommen* |
| 5 | **Erkennungsregel-Änderungsprotokoll** (neue Regeln, abgestimmte Regeln, unterdrückte Regeln mit Begründung) | Informationssicherheit | *Monatlich; Protokoll 12 Monate aufbewahrt* |
| 6 | **MTTD- und MTTR-Metriken** an Management gemeldet | ISB | *Monatlich an ISB; halbjährlich an Management Review* |
| 7 | **Falsch-Positiv-Rate** und Alarmvolumen-Trends | Informationssicherheit | *Monatlich; Ziel <20 % Falsch-Positiv-Rate für hochgradige Alarme* |
| 8 | **Mitarbeiterbenachrichtigungsaufzeichnungen** (Richtlinie zur akzeptablen Nutzung, Datenschutzhinweis zur Überwachung) | HR / Informationssicherheit | *Bei Richtlinienänderung aktualisiert; Bestätigung jährlich verfolgt* |
| 9 | **DSFA-Aufzeichnungen** (falls grossmassstäbliche Überwachung implementiert) | Datenschutzberater | *Vor dem Einsatz abgeschlossen; jährlich überprüft* |
| 10 | **Überwachungsplattform-Gesundheitsaufzeichnungen** — Betriebszeit, Dateneinnahmeraten, Agenten-Gesundheit, Speicherkapazität (SOC 2: CC4.1) | IT-Betrieb | *Laufende Überwachung; monatlicher Zusammenfassungsbericht* |
| 11 | **Eskalationsaufzeichnungen** — dokumentierte Eskalationspfadnutzung, Eskalationsaktualität, Lösungsergebnisse | Informationssicherheit | *Pro Eskalation; monatlich überprüft* |
| 12 | **MITRE-ATT&CK-Abdeckungszuordnung** — von Erkennungsregeln abgedeckte Techniken, identifizierte Lücken, Sanierungspläne | Informationssicherheit | *Halbjährlich* |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheitsmanagement-Team soll die Einhaltung dieser Richtlinie durch Überwachungsabdeckungsüberprüfungen, Alarmreaktionsüberprüfungen, KPI-Tracking, interne und externe Revisionen sowie Rückmeldungen an den Richtlinieneigentümer verifizieren.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll im Voraus vom Informationssicherheitsbeauftragten genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum. Ausnahmen sollen dem Management-Review-Team gemeldet werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Änderungen der Überwachungstechnologien, Entwicklungen der Bedrohungslandschaft, regulatorische Anforderungen sowie Lessons Learned aus Vorfällen und Falsch-Positiv-Analysen berücksichtigen.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Richtlinie zu Überwachungsaktivitäten — Zuordnung der ISO-27001-Massnahmen

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Abschnitt 5.1 Führung und Verpflichtung | 5.1 Richtlinien zur Informationssicherheit |
| Abschnitt 5.2 Richtlinie | 5.4 Managementverantwortlichkeiten |
| Abschnitt 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| Abschnitt 9.1 Überwachung, Messung, Analyse und Bewertung | 5.37 Dokumentierte Betriebsverfahren |
| | 6.3 Informationssicherheitsbewusstsein, -ausbildung und -schulung |
| | 6.4 Disziplinarverfahren |
| | **8.16 Überwachungsaktivitäten** |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen; Art. 6 — Verhältnismässigkeit |
| Schweizerisches OR (Obligationenrecht) | Art. 328b — Einschränkungen der Mitarbeiterdatenverarbeitung |
| Schweizerische ArGV3 (Verordnung 3 zum Arbeitsgesetz) | Art. 26 — Verbot der Verhaltensüberwachung |
| EU-DSGVO (wo anwendbar) | Art. 32 — Sicherheit der Verarbeitung |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.16 |
| ISO/IEC 27002:2022 | Abschnitt 8.16 — Implementierungsleitfaden |
| NIST SP 800-53 Rev 5 | SI-4 (Information System Monitoring), AU-6 (Audit Record Review), CA-7 (Continuous Monitoring) |
| NIST CSF 2.0 | DE.CM (Continuous Monitoring), DE.AE (Adverse Event Analysis) |
| CIS Controls v8 | Control 8 (Audit Log Management), Control 13 (Network Monitoring and Defence) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
