<!-- ISMS-CORE:POLICY:ISMS-POL-A.7.4-5-11-DE:framework:POL:a.7.4-5-11 -->
**ISMS-POL-A.7.4-5-11 — Physische Infrastruktursicherheit**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Richtlinie zur physischen Infrastruktursicherheit |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.7.4-5-11 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Informationssicherheitsbeauftragter (ISB) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum zu bestimmen] |
| **Version** | 1.0 |
| **Versionsdatum** | [Datum zu bestimmen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum zu bestimmen] | ISB | Erstkonsolidierte Richtlinie für ISO 27001:2022-Zertifizierung |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen Einrichtungsänderungen, Sicherheitsvorfällen oder regulatorischen Aktualisierungen)
**Nächstes Überprüfungsdatum**: [Gültigkeitsdatum + 12 Monate]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: Facility Manager
- Letzte Instanz: Unternehmensleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Rahmenwerk zur regulatorischen Anwendbarkeit)
- ISMS-POL-A.7.1-3 (Physische Zugangskontrolle)
- ISMS-POL-A.5.19-23 (Cloud-Dienste)
- ISMS-POL-A.5.24-28 (Incident Management)
- ISMS-POL-A.5.30-8.13-14 (Business Continuity)
- ISMS-IMP-A.7.4-5-11-S1-UG/TG (Beurteilung der physischen Überwachung)
- ISMS-IMP-A.7.4-5-11-S2-UG/TG (Implementierung des Umgebungsschutzes)
- ISMS-IMP-A.7.4-5-11-S3-UG/TG (Implementierung der Versorgungsresilienz)
- ISMS-IMP-A.7.4-5-11-S4-UG/TG (Einrichtungsbeurteilung)
- ISO/IEC 27001:2022 Controls A.7.4, A.7.5, A.7.11

---

# Zusammenfassung für die Unternehmensleitung

Diese Richtlinie legt die Anforderungen von [Organisation] für physische Infrastruktursicherheitskontrollen zum Schutz von Informationswerten durch umfassende Überwachung, Umgebungsschutz und Versorgungsresilienz gemäss ISO/IEC 27001:2022 Controls A.7.4, A.7.5 und A.7.11 fest.

**Zweck**: Definition der organisatorischen Anforderungen für die Governance der physischen Infrastruktursicherheit. Diese Richtlinie legt fest, WELCHER physische Sicherheitsschutz erforderlich ist und WER verantwortlich ist. Implementierungsverfahren (WIE) sind in ISMS-IMP-A.7.4-5-11 dokumentiert.

**Kombinierter Control-Ansatz**: Diese drei Controls werden als einheitliches Rahmenwerk für physische Infrastruktursicherheit umgesetzt, da sie auf derselben physischen Infrastruktur operieren, Wechselwirkungen aufweisen und gemeinsame Beurteilungsprozesse teilen. Jeder Control behält für die Anwendbarkeitserklärung (SoA) eigenständige Anforderungen.

---

# Geltungsbereich

## Im Geltungsbereich

**Einrichtungen**:

- Eigene Rechenzentren und Notfallwiederherstellungsstandorte
- Serverräume und Telekommunikationsschränke
- Unternehmensbüros (Hauptsitz, Regional-, Zweigstellen)
- Colocation-Einrichtungen (mit geteiltem Verantwortungsmodell)
- Entfernte und temporäre Einrichtungen mit unternehmenseigenen Geräten

**Personal**:

- Facility Management, Security Operations, IT Operations
- Alle Mitarbeitenden, die physische Einrichtungen nutzen
- Auftragnehmer, Anbieter und Besucher

## Reine Cloud-Organisationen

Organisationen, die zu 100% in Cloud-Umgebungen ohne physische Informationsverarbeitungseinrichtungen vor Ort tätig sind, können Controls A.7.4, A.7.5 und A.7.11 in der Anwendbarkeitserklärung als «Nicht anwendbar» kennzeichnen.

**Anforderungen an die Entscheidung zur Nichtanwendbarkeit**: Die Bestimmung «Nicht anwendbar» MUSS in der Anwendbarkeitserklärung mit Begründung dokumentiert werden, einschliesslich:
- Verweis auf Vermögenswertinventar, das keine Einrichtungen vor Ort bestätigt (ISMS-IMP-A.5.9)
- Verifizierung der physischen Sicherheit des Cloud-Anbieters durch SOC-2-Typ-II-Überprüfung (ISMS-IMP-A.5.19-23)
- Jährliche Überprüfungsbestätigung, dass der reiner-Cloud-Status korrekt bleibt

Die physische Sicherheit des Cloud-Anbieters MUSS durch das Lieferantenmanagement (Control A.5.19-23) beurteilt werden.

## Colocation-Einrichtungen

Bei Nutzung von Colocation-Rechenzentrumsraum werden die Verantwortlichkeiten für physische Infrastruktur zwischen dem Colocation-Anbieter und [Organisation] geteilt. Eine formale Verantwortlichkeitsmatrix MUSS im Colocation-Vertrag dokumentiert und im Lieferantenmanagement-Register (ISMS-POL-A.5.19-23) für zentralisiertes Tracking gepflegt werden. Anbieterkontrollen MÜSSEN jährlich durch Auditberichte (SOC 2 Typ II oder ISO 27001-Zertifizierung) verifiziert werden, mit in den Lieferantenbewertungsaufzeichnungen dokumentierter Überprüfung.

## Ausserhalb des Geltungsbereichs

- Physische Sicherheit tragbarer Geräte (geregelt unter A.7.7, A.8.1)
- Transportsicherheit für Geräte (geregelt unter A.7.13)
- Offsite-Backup-Medienspeicherung (geregelt unter A.8.13)
- Personalsicherheit und Hintergrundprüfungen (geregelt unter A.6.1–6.4)

---

# Richtlinienaussagen

## Physische Sicherheitsüberwachung (A.7.4)

> *Räumlichkeiten sollten kontinuierlich auf unbefugten physischen Zugang überwacht werden.*

**Kontrollziel**: Erkennen und Reagieren auf unbefugte physische Zutrittsversuche durch umfassende Überwachung.

[Organisation] MUSS:

1. **Zugangskontrolle**: Elektronische Zugangskontrolle an allen Einrichtungs-Ein-/Ausgangspunkten mit Authentifizierung, Protokollierung und Integration in das Identitätsmanagement implementieren
2. **Einbrucherkennung**: Für Einrichtungskritikalität und Risikobeurteilung angemessene Einbrucherkennungssysteme einsetzen
3. **Videoüberwachung**: CCTV-Abdeckung für Einrichtungseingänge, eingeschränkte Bereiche und kritische Infrastruktur bereitstellen
4. **Besuchermanagement**: Alle Besucher zur Registrierung, zum Erhalt einer temporären Identifikation und zur Begleitung in eingeschränkten Bereichen verpflichten
5. **Zugriffsüberprüfung**: Periodische Zugriffsüberprüfungen zur Identifizierung und Sperrung veralteter oder nicht autorisierter Zugriffsrechte durchführen
6. **Sicherheitsintegration**: Physische Sicherheitsereignisse in das SIEM (ISMS-POL-A.8.16) integrieren für Korrelation mit logischen Sicherheitsereignissen und Incident Response

**Compliance-Nachweis**: Die Compliance der physischen Sicherheitsüberwachung wird durch ISMS-IMP-A.7.4-5-11-S1 (Beurteilung der physischen Überwachung) nachgewiesen, das monatliche Workbooks generiert mit:
- Elektronischen Zugangskontrollprotokollen mit Authentifizierungserfolgs-/-fehlerquoten
- Verifizierung von CCTV-System-Verfügbarkeit und Abdeckung
- Warnmeldungen und Reaktionszeiten des Einbrucherkennungssystems
- Besuchermanagementaufzeichnungen mit Begleit-Compliance
- Ergebnissen der Zugriffsüberprüfung mit Sperrmassnahmen

## Umgebungsschutz (A.7.5)

> *Schutz vor physischen und umgebungsbedingten Bedrohungen sollte entworfen und implementiert werden.*

**Kontrollziel**: Schutz von Informationsverarbeitungseinrichtungen vor physischen und umgebungsbedingten Bedrohungen einschliesslich Brand, Überschwemmung und Klimabedingungen.

[Organisation] MUSS:

1. **Bedrohungsbeurteilung**: Risikobeurteilung für umgebungsbedingte Bedrohungen unter Berücksichtigung geografischer Lage und Einrichtungsmerkmale durchführen
2. **Brandschutz**: Für Einrichtungstyp und regulatorische Anforderungen angemessene Branderkennungs- und Löschsysteme implementieren
3. **Wasserschutz**: Wassererkennungssysteme installieren und Hochwasserschutzmassnahmen basierend auf Risikobeurteilung implementieren
4. **Klimakontrolle**: Temperatur und Luftfeuchtigkeit innerhalb akzeptabler Bereiche für Informationsverarbeitungsgeräte aufrechterhalten
5. **Strukturschutz**: Gebäudeintegrität sicherstellen und den identifizierten Bedrohungen angemessene physische Barrieren implementieren
6. **Notfallreaktion**: Notfallreaktionsverfahren für umgebungsbedingte Vorfälle dokumentieren und testen

**Compliance-Nachweis**: Die Compliance des Umgebungsschutzes wird durch ISMS-IMP-A.7.4-5-11-S2 (Umgebungsschutz-Beurteilung) nachgewiesen, das vierteljährliche Workbooks generiert mit:
- Brandanlagentestergebnissen und Inspektionszertifikaten
- Wassererkennungssystem-Protokollen und Wartungsaufzeichnungen
- Temperatur-/Luftfeuchtigkeitsüberwachungsdaten mit Schwellenwert-Compliance
- Überprüfungen der Beurteilung umgebungsbedingter Bedrohungen (jährlich)
- Notfallreaktions-Übungsaufzeichnungen und Feststellungen

## Versorgungsresilienz (A.7.11)

> *Informationsverarbeitungseinrichtungen sollten vor Stromausfällen und anderen Störungen durch Versorgungsausfälle geschützt werden.*

**Kontrollziel**: Sicherstellung der Kontinuität der Informationsverarbeitung durch resiliente Versorgungsinfrastruktur einschliesslich Strom, Kühlung und Telekommunikation.

[Organisation] MUSS:

1. **Stromschutz**: Unterbrechungsfreie Stromversorgungssysteme (USV) mit der Einrichtungskritikalität angemessener Kapazität implementieren
2. **Notstrom**: Notstromaggregat-Fähigkeit für kritische Einrichtungen bereitstellen, um den Betrieb während längerer Ausfälle sicherzustellen
3. **Kühlungsresilienz**: Kühlsysteme mit der Einrichtungskritikalität angemessener Redundanz implementieren
4. **Telekommunikation**: Telekommunikationsverbindung mit der Einrichtungskritikalität angemessener Redundanz sicherstellen
5. **Versorgungsüberwachung**: Versorgungssysteme in Echtzeit mit Warnmeldungen bei Ausfällen oder Schwellenwertüberschreitungen überwachen
6. **Fehlertest**: Regelmässige Tests der Versorgungsresilienz-Systeme gemäss Zeitplan durchführen:
   - USV-Failover-Test: Vierteljährlich
   - Notstromaggregat-Lasttest: Halbjährlich
   - Kühlungsredundanz-Verifizierung: Vierteljährlich
   - Telekommunikations-Failover: Jährlich

**Compliance-Nachweis**: Die Compliance der Versorgungsresilienz wird durch ISMS-IMP-A.7.4-5-11-S3 (Versorgungsresilienz-Beurteilung) nachgewiesen, das vierteljährliche Workbooks generiert mit:
- USV-Testprotokollen mit Failover-Erfolgs-/-Fehlerergebnissen
- Notstromaggregat-Lasttestberichten mit Kraftstoffverbrauchsverifizierung
- Kühlungssystem-Redundanzverifizierungsaufzeichnungen
- Telekommunikations-Failover-Testergebnissen
- Versorgungsüberwachungs-Warnhistorie und Reaktionszeiten

## Einrichtungs-Kritikalitätsstufen

Einrichtungen MÜSSEN basierend auf der Business-Impact-Analyse in Kritikalitätsstufen klassifiziert werden:

| Stufe | Definition | Überwachung | Umgebung | Versorgung | Überprüfungshäufigkeit |
|-------|------------|-------------|----------|------------|------------------------|
| **Stufe 1 – Kritisch** | Rechenzentren, primäre Serverräume, Notfallwiederherstellungsstandorte | 24/7-SOC-Überwachung, Reaktions-SLA <15 Min., Einbrucherkennung erforderlich | Brandunterdrückung + Erkennung, Wasserkennung alle Zonen, Temperatur 18–27°C ±2°C | N+1-USV (zwei Einheiten, je 30 Min. Laufzeit), Notstromaggregat (48h Kraftstoff), zwei Kühlpfade | Monatliche manuelle Verifizierung |
| **Stufe 2 – Standard** | Unternehmensbüros, Zweigstellen, unkritische Serverräume | 8/5-Überwachung, Reaktion am nächsten Geschäftstag, Einbrucherkennung optional | Branderkennung (Löschung bei Gerätewert >CHF 500k), Wasserkennung nur in Hochrisikobereichen, Temperatur 18–27°C ±5°C | Einzel-USV (mind. 15 Min. Laufzeit), kein Aggregat erforderlich, einzelne Kühlung | Vierteljährliche manuelle Verifizierung |

**Klassifizierungskriterien**: Einrichtungen MÜSSEN basierend auf der Business-Impact-Analyse (ISMS-POL-A.5.30-8.13-14) klassifiziert werden unter Berücksichtigung von:
- System-Kritikalität: Stufe-1/2-Anwendungen gehostet
- Datenklassifizierung: VERTRAULICHE Datenverarbeitung = Stufe 1
- Wiederherstellungszeit-Ziele: RTO <4h = Stufe 1, RTO >4h = Stufe 2

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Informationssicherheitsbeauftragter (ISB)** | Gesamtverantwortung für das physische Infrastruktursicherheits-Rahmenwerk; Richtliniengenehmigung; Budget-Zuweisung; Berichterstattung an Führungskräfte |
| **Facility Manager** | Täglicher Betrieb der physischen Infrastruktur; Wartung von Umgebungs- und Versorgungssystemen; Lieferantenmanagement |
| **Security Operations Manager** | Implementierung der physischen Sicherheitsüberwachung; Zugangskontrollmanagement; CCTV-Betrieb; Koordination der Incident Response |
| **System-Eigentümer** | Physische Sicherheitsanforderungen für eigene Systeme; Koordination der Geräteplatzierung; Vorfallbeteiligung |
| **IT Operations** | Physisch-logische Sicherheitsintegration (SIEM); Netzwerkinfrastruktur für Sicherheitssysteme; Überwachungs-Dashboards |
| **Internes Audit** | Jährliches physisches Sicherheits-Compliance-Audit; Kontrolltest; Nachweisüberprüfung |
| **Risikomanagement** | Risikobeurteilung für physische Sicherheit; Beurteilung umgebungsbedingter Bedrohungen; Pflege des Risikoregisters |
| **Compliance-Beauftragter** | Nachverfolgung regulatorischer Compliance; Nachweiserhebung; regulatorische Kontaktstelle |

---

# Governance und Compliance

## Beurteilungsrahmen

[Organisation] MUSS regelmässige Beurteilungen gemäss ISMS-IMP-A.7.4-5-11-Methodik durchführen:

- **Kontinuierlich**: Echtzeitüberwachung und Warnmeldungen
- **Monatlich**: Automatisierte Datenerhebung aus physischen Sicherheitssystemen
- **Vierteljährlich**: Manuelle Verifizierung und Überprüfung der Testcompliance
- **Jährlich**: Umfassendes Audit mit externer Verifizierung

## Compliance-Bewertung

| Punktzahl | Bewertung | Erforderliche Massnahme |
|-----------|-----------|------------------------|
| >90% | Ausgezeichnet | Aktuelle Kontrollen aufrechterhalten |
| 75–89% | Gut | Lücken im nächsten Überprüfungszyklus adressieren |
| 60–74% | Akzeptabel | Behebungsplan innerhalb von 30 Tagen entwickeln |
| <60% | Nicht compliant | Sofortige Behebung erforderlich, ISB-Eskalation |

**Bewertungsmethodik**: Die Compliance-Punktzahl wird aus den Summary-Dashboard-Metriken berechnet, die über die physischen Infrastrukturbeurteilungs-Workbooks mit gewichteten Metriken verfolgt werden:

| Metrik | Gewichtung | Messungsquelle |
|--------|-----------|----------------|
| Verfügbarkeit des Zugangskontrollsystems | 20% | Zugangskontrollsystem-Protokolle |
| Compliance mit Umgebungsparametern (Temp./Luftfeuchtigkeit innerhalb Schwellenwerte) | 20% | Umgebungsüberwachungssystem |
| Erfolgsquote der Versorgungsresilienz-Tests | 15% | Testaufzeichnungen (S3-Workbook) |
| Betriebsstatus des Brand-/Wassererkennungssystems | 15% | Inspektionsaufzeichnungen |
| Einhaltung der Reaktionszeit bei Sicherheitsvorfällen | 15% | Incident-Management-System |
| Compliance beim Besuchermanagement | 10% | Besucherprotokolle |
| Abschluss der Schulung zur physischen Sicherheit | 5% | LMS-Aufzeichnungen |

Detaillierte Berechnungsmethodik und Metrikdefinitionen sind in ISMS-IMP-A.7.4-5-11-S4 dokumentiert.

## Ausnahmenmanagement

Physische Infrastruktursicherheitsanforderungen können durch formalen Ausnahmeprozess dispensiert werden:

- **Gültige Szenarien**: Technische Undurchführbarkeit, unverhältnismässige Kosten, temporäre Abweichung während Übergängen
- **Genehmigungsbehörde**: Security Operations Manager (geringes Risiko), ISB (mittleres Risiko), Unternehmensleitung (hohes Risiko)
- **Anforderungen**: Dokumentierte Begründung, Risikobeurteilung, kompensierende Kontrollen, definierte Dauer (maximal 6 Monate)
- **Überprüfung**: Neubewertung bei Ablauf, Einrichtungsänderungen oder Vorfalleintreten

## Lückenbehebung

Durch Beurteilungen (Beurteilungsrahmen) identifizierte physische Infrastrukturkontroll-Defizite MÜSSEN wie folgt verwaltet werden:

**1. Dokumentation**: Defizite MÜSSEN in den physischen Sicherheitsbeurteilungsaufzeichnungen erfasst werden (über Summary Dashboard in jedem Beurteilungs-Workbook verfolgt) mit:
- Lückenbeschreibung und betroffene(r) Control(s) (A.7.4, A.7.5, A.7.11)
- Risikoschwere (Kritisch/Hoch/Mittel/Niedrig gemäss Vorfallklassifizierung)
- Zugewiesener Eigentümer und angestrebtes Abschlussdatum
- Kompensierende Kontrollen (falls anwendbar)
- Status (Offen/In Bearbeitung/Abgeschlossen)

**2. Nachverfolgung**: Das Lückenregister MUSS überprüft werden:
- Monatlich: Überprüfung durch Security Operations Manager mit Eigentümer-Follow-up
- Vierteljährlich: ISB-Überprüfung mit Führungskräfte-Eskalation bei überfälligen kritischen/hohen Lücken
- Jährlich: Internes Audit zur Verifizierung von Abschlussnachweisen

**3. Abschluss**: Lücken dürfen nur nach folgenden Schritten geschlossen werden:
- Behebung implementiert und verifiziert
- Nachweise dokumentiert (z.B. Systeminstallationsbeleg, Testergebnisse)
- Abzeichnung durch Security Operations Manager (Niedrig/Mittel) oder ISB (Hoch/Kritisch)

**4. Eskalation**: Über das Zieldatum hinaus offene Lücken MÜSSEN gemäss ISMS-POL-A.5.24-28 (Incident Management) eskaliert werden.

## Vorfallklassifizierung

| Schwere | Beispiele | Reaktion |
|---------|-----------|---------|
| **Kritisch** | Unbefugter Zugang zu eingeschränkten Bereichen; physischer Einbruch; Diebstahl; grösseres Umgebungsereignis | Sofortige Reaktion gemäss ISMS-POL-A.5.24-28 |
| **Hoch** | Wiederholte fehlgeschlagene Zugangsversuche; Tailgating; verlorene Badges; Umgebungswarnungen | Untersuchung und Reaktion am selben Tag |
| **Mittel** | Offengehaltene Tür; häufige Fehlalarme; geringfügige Umgebungsabweichungen | Dokumentiert und untersucht |
| **Niedrig** | Einzelner fehlgeschlagener Zugang; geringfügige Richtlinienverstösse | Für Trendanalyse protokolliert |

## Richtlinienüberprüfung

- **Häufigkeit**: Jährlich oder bei wesentlichem Auslöseereignis
- **Auslöseereignisse**: Einrichtungsänderungen, Sicherheitsvorfälle, regulatorische Aktualisierungen, Technologieänderungen
- **Teilnehmer**: ISB, Facility Manager, Security Operations Manager, Compliance-Beauftragter
- **Genehmigung**: ISB (geringfügige Änderungen), Unternehmensleitung (wesentliche Änderungen)

---

# Regulatorische Anwendbarkeit

## Obligatorische Compliance (Tier 1)

| Regulierung | Kernanforderungen |
|-------------|-------------------|
| **Schweizerisches nDSG** | Art. 8 – Technische und organisatorische Massnahmen für physische Sicherheit |
| **EU-DSGVO** | Art. 32 – Sicherheit der Verarbeitung einschliesslich physischer Massnahmen |
| **ISO/IEC 27001:2022** | Controls A.7.4, A.7.5, A.7.11 – Dokumentierte Richtlinie und Implementierung |

## Bedingte Compliance (Tier 2)

| Regulierung | Auslösebedingung |
|-------------|------------------|
| **FINMA-Rundschreiben 2023/1** | Schweizerisch reguliertes Finanzinstitut |
| **DORA (EU) 2022/2554** | EU-Finanzdienstleistungseinheit |
| **NIS2-Richtlinie (EU) 2022/2555** | Wesentliche/wichtige Einrichtung in der EU |

Vollständige regulatorische Kategorisierung in ISMS-POL-00 (Rahmenwerk zur regulatorischen Anwendbarkeit).

---

# Verwandte Dokumente

## Interne ISMS-Referenzen

| Dokument | Beziehung |
|----------|-----------|
| ISMS-POL-00 | Rahmenwerk zur regulatorischen Anwendbarkeit |
| ISMS-POL-A.7.1-3 | Physische Zugangskontrolle (Voraussetzung) |
| ISMS-POL-A.5.19-23 | Cloud-Dienste (Cloud-Anbieter-Beurteilung) |
| ISMS-POL-A.5.24-28 | Incident Management (Incident Response) |
| ISMS-POL-A.5.30-8.13-14 | Business Continuity (BC/DR-Integration) |

## Implementierungsleitfaden

| Dokument | Zweck |
|----------|-------|
| ISMS-IMP-A.7.4-5-11-S1 | Beurteilung der physischen Überwachung |
| ISMS-IMP-A.7.4-5-11-S2 | Umgebungsschutz-Beurteilung |
| ISMS-IMP-A.7.4-5-11-S3 | Versorgungsresilienz-Beurteilung |

## Externe Normen

- ISO/IEC 27001:2022 – Informationssicherheitsmanagementsysteme
- ISO/IEC 27002:2022 – Informationssicherheitskontrollen
- NIST SP 800-53 Rev 5 – Physischer und Umgebungsschutz (PE)
- Uptime Institute Tier Standards – Rechenzentrumsklassifizierung
- TIA-942 – Telekommunikationsinfrastrukturnorm für Rechenzentren

---

# ISMS-Integration

## Anwendbarkeitserklärung

| Control | Status | Implementierungsreferenz |
|---------|--------|--------------------------|
| **A.7.4 – Physische Sicherheitsüberwachung** | Anwendbar | Diese Richtlinie, ISMS-IMP-A.7.4-5-11-S1 |
| **A.7.5 – Schutz vor physischen und umgebungsbedingten Bedrohungen** | Anwendbar | Diese Richtlinie, ISMS-IMP-A.7.4-5-11-S2 |
| **A.7.11 – Versorgungseinrichtungen** | Anwendbar | Diese Richtlinie, ISMS-IMP-A.7.4-5-11-S3 |

## Verwandte Controls

| Control | Beziehung |
|---------|-----------|
| **A.7.1-3** | Physische Zugangskontrolle (Voraussetzung für Überwachung) |
| **A.7.8-9** | Geräteplatzierung und Sicherheit ausserhalb der Räumlichkeiten |
| **A.5.19-23** | Beurteilung der physischen Sicherheit von Cloud-Anbietern |
| **A.5.24-28** | Incident Management für physische Sicherheitsereignisse |
| **A.5.30-8.13-14** | Business-Continuity-Integration |
| **A.8.16** | SIEM-Integration für physisch-logische Korrelation |

---

# Definitionen

| Begriff | Definition |
|---------|------------|
| **Physische Sicherheitsüberwachung** | Kontinuierliche Überwachung und Erkennung von physischen Zugriffsversuchen und Umgebungsbedingungen |
| **Umgebungsbedingte Bedrohung** | Natürliche oder von Menschen verursachte Gefahren, die Einrichtungen schädigen können (Brand, Überschwemmung, Temperaturextreme, seismische Ereignisse) |
| **Versorgungseinrichtungen** | Infrastrukturdienste, die für den Einrichtungsbetrieb erforderlich sind (Strom, Kühlung, Telekommunikation) |
| **Einrichtungs-Kritikalitätsstufe** | Klassifizierung von Einrichtungen basierend auf Geschäftsauswirkung und erforderlichem Schutzniveau |
| **N+1-Redundanz** | Konfiguration, bei der eine zusätzliche Einheit über dem Minimum verfügbar ist |
| **Lückenregister** | Dokumentierte Liste von Kontrollmängeln mit Behebungsverfolgung |
| **SOC 2 Typ II** | Service-Organization-Control-Auditbericht, der die Kontrollwirksamkeit über einen Zeitraum nachweist |

---

# Nachweise für diese Richtlinie

**Nachweise Stufe 1 (Dokumentenüberprüfung):**

- ✅ Dieses Richtliniendokument (ISMS-POL-A.7.4-5-11 v1.0)
- ✅ Genehmigungsunterschriften von ISB, Facility Manager, Unternehmensleitung
- ✅ Anforderungen an physische Sicherheitsüberwachung dokumentiert (Abschnitt: Richtlinienaussagen)
- ✅ Anforderungen an Umgebungsschutz dokumentiert (Abschnitt: Richtlinienaussagen)
- ✅ Anforderungen an Versorgungsresilienz dokumentiert (Abschnitt: Richtlinienaussagen)
- ✅ Einrichtungs-Kritikalitätsstufen definiert (Abschnitt: Einrichtungs-Kritikalitätsstufen)
- ✅ Rollen und Verantwortlichkeiten zugewiesen (Abschnitt: Rollen und Verantwortlichkeiten)
- ✅ Compliance-Bewertungsmethodik dokumentiert (Abschnitt: Governance und Compliance)
- ✅ Lückenbehebungsprozess dokumentiert (Abschnitt: Lückenbehebung)

**Nachweise Stufe 2 (Operative Wirksamkeit):**

**Nachweis-Repository und -Generierung**:

| Nachweistyp | Repository-Standort | Generierungsmethode | Eigentümer | Aufbewahrung |
|-------------|--------------------|--------------------|------------|--------------|
| Physisches Überwachungs-Workbook | [GRC-Plattform] – Physisches Sicherheitsmodul | Monatlich automatisierte Erhebung via ISMS-IMP-A.7.4-5-11-S1 | Security Operations Manager | 3 Jahre |
| Umgebungsschutz-Beurteilung | [GRC-Plattform] – Physisches Sicherheitsmodul | Vierteljährliche Beurteilung via ISMS-IMP-A.7.4-5-11-S2 | Facility Manager | 3 Jahre |
| Versorgungsresilienz-Beurteilung | [GRC-Plattform] – Physisches Sicherheitsmodul | Vierteljährlicher Test via ISMS-IMP-A.7.4-5-11-S3 | Facility Manager | 3 Jahre |
| Physisches Sicherheits-Lückenregister | [GRC-Plattform] – Risikoregister | Kontinuierliches Tracking, monatliche Überprüfung | Security Operations Manager | Aktiv + 2 Jahre |
| Zugangskontrollprotokolle | [Physisches Zugangssystem] | Automatisierte Protokollierung | Security Operations | 12 Monate |
| CCTV-Aufzeichnungen | [Video-Management-System] | Kontinuierliche Aufzeichnung | Security Operations | 30–90 Tage gemäss Richtlinie |
| Umgebungsüberwachungsdaten | [BMS/Umgebungsüberwachungssystem] | Kontinuierliche Sensordaten | Facility Manager | 12 Monate |
| Versorgungstestaufzeichnungen | [CMMS/Wartungssystem] | Gemäss Testzeitplan | Facility Manager | 5 Jahre |
| Ausnahmenaufzeichnungen | [GRC-Plattform] – Ausnahmenregister | Gemäss Ausnahmenanforderung | ISB | Aktiv + 2 Jahre |

**Nachweiszugänglichkeit**: Alle Nachweise MÜSSEN Auditoren auf Anfrage innerhalb von 2 Geschäftstagen zugänglich sein.

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Datum zu bestimmen] |
| **Facility Manager** | [Name] | [Datum zu bestimmen] |
| **Unternehmensleitung** | [Name] | [Datum zu bestimmen] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt die Anforderungen von [Organisation] für physische Infrastruktursicherheit fest. Implementierungsverfahren sind in ISMS-IMP-A.7.4-5-11 (UG/TG) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
