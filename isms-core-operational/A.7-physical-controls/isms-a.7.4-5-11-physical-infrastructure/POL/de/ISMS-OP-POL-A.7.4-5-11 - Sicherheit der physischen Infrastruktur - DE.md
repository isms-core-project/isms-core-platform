<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.4-5-11-DE:operational:OP-POL:a.7.4-5-11 -->
**ISMS-OP-POL-A.7.4-5-11 — Sicherheit der physischen Infrastruktur**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Sicherheit der physischen Infrastruktur |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.7.4-5-11 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstveröffentlichung der operativen Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Controls A.7.4, A.7.5, A.7.11 — Physische Sicherheitsüberwachung, Schutz vor physischen und umgebungsbezogenen Bedrohungen, Versorgungseinrichtungen
- ISO/IEC 27002:2022 Abschnitte 7.4, 7.5, 7.11 — Implementierungshinweise

**Verwandte Annex-A-Controls**:

| Control | Bezug zur Sicherheit der physischen Infrastruktur |
|---------|---------------------------------------------------|
| A.7.1 Physische Sicherheitsperimeter | Perimetergrenzen definieren den Überwachungsumfang und die Umgebungsschutzzonen |
| A.7.2 Physischer Zutritt | Zutrittskontollen erzeugen Zugriffsereignisse für Überwachung und Korrelation |
| A.7.3 Sicherung von Büros, Räumen und Einrichtungen | Gesicherte Bereiche erfordern Umgebungsschutz und Versorgungsresilienz |
| A.7.8 Geräteaufstellung und -schutz | Gerätepositionierung berücksichtigt Umgebungsbedingungen und Versorgungsverfügbarkeit |
| A.7.12 Verkabelungssicherheit | Integrität von Strom- und Telekommunikationskabeln unterstützt Versorgungsresilienz |
| A.7.13 Gerätewartung | Wartungspläne für Umgebungs- und Versorgungssysteme |
| A.5.24–28 Lifecycle des Incident-Managements | Physische Sicherheits- und Umgebungsvorfälle werden ins Incident-Management eskaliert |
| A.5.30 ICT-Bereitschaft für die Geschäftskontinuität | Versorgungsresilienz unterstützt Geschäftskontinuitätsziele |
| A.8.16 Überwachungsaktivitäten | Physische Sicherheitsereignisse werden für korrelierte Erkennung in das SIEM integriert |

**Verwandte interne Richtlinien**:

- Richtlinie zur physischen Zugangskontrolle
- Incident-Management-Richtlinie
- Richtlinie zur Geschäftskontinuität und Disaster Recovery
- Protokollierungsrichtlinie
- Richtlinie zu Überwachungsaktivitäten (A.8.16)
- Richtlinie zu Cloud-Diensten und Lieferantensicherheit
- Asset-Management-Richtlinie

---

# Richtlinie zur Sicherheit der physischen Infrastruktur

## Zweck

Der Zweck dieser Richtlinie ist der Schutz von Informationsverarbeitungsanlagen und der damit verbundenen Infrastruktur durch physische Sicherheitsüberwachung, Schutz vor Umgebungsbedrohungen und Versorgungsresilienz. Sie legt Anforderungen an kontinuierliche Überwachung, Brand- und Wasserschutz, Klimatisierung sowie Strom- und Telekommunikationskontinuität fest.

Diese Richtlinie adressiert drei verwandte ISO 27001:2022-Controls als einheitliches Rahmenwerk, da sie auf derselben physischen Infrastruktur betrieben werden, gegenseitige Abhängigkeiten aufweisen und gemeinsame Bewertungsprozesse teilen: Überwachung erkennt Bedrohungen (A.7.4), Umgebungskontrollen verhindern Schäden (A.7.5) und Versorgungssysteme gewährleisten den Betrieb (A.7.11). Jeder Control behält für Zwecke der Anwendbarkeitserklärung eigenständige Anforderungen.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 8, indem sie technische und organisatorische Massnahmen proportional zum Risiko zum Schutz der Verfügbarkeit, Integrität und Vertraulichkeit von Personendaten durch physische Infrastruktursicherheitskontrollen umsetzt. Soweit die Organisation Daten von Personen in der EU/EWR verarbeitet, gelten zusätzlich die Anforderungen aus DSGVO Art. 32 zur Sicherheit der Verarbeitung einschliesslich physischer Massnahmen.

## Geltungsbereich

Alle Mitarbeitenden und Drittnutzer.

Alle eigenen, gemieteten oder Colocation-Räumlichkeiten der Organisation, einschliesslich:

- On-Premises-Rechenzentren und Disaster-Recovery-Standorte
- Serverräume und Telekommunikationsschränke
- Unternehmensbüros (Hauptsitz, Regionalstandorte, Niederlassungen)
- Colocation-Einrichtungen (mit geteiltem Verantwortungsmodell)
- Remote- und temporäre Einrichtungen, in denen organisationseigene Geräte stehen

**Nicht im Geltungsbereich**:

- Physische Sicherheit von tragbaren Geräten (abgedeckt durch A.7.9, A.8.1)
- Sicherheit beim Gerätetransport (abgedeckt durch A.7.13)
- Externe Backup-Medienspeicherung (abgedeckt durch A.8.13)
- Personalsicherheit und Hintergrundüberprüfungen (abgedeckt durch A.6.1–6.4)
- Physische Sicherheit von Einrichtungen Dritter und Lieferanten (abgedeckt durch A.5.19–23, ausser Colocation wie unten angegeben)

### Rein cloudbasierte Organisationen

Organisationen, die zu 100% in Cloud-Umgebungen ohne On-Premises-Informationsverarbeitungsanlagen betrieben werden, können die Controls A.7.4, A.7.5 und A.7.11 in der Anwendbarkeitserklärung als „Nicht anwendbar" kennzeichnen.

Die Feststellung „Nicht anwendbar" muss dokumentiert werden mit:

- Verweis auf das Asset-Inventar, der bestätigt, dass keine On-Premises-Informationsverarbeitungsanlagen vorhanden sind.
- Verifizierung der physischen Sicherheit des Cloud-Anbieters durch SOC 2 Type II-Bericht oder ISO 27001-Zertifizierungsüberprüfung.
- Jährliche Überprüfungsbestätigung, dass der rein cloudbasierte Status weiterhin zutreffend ist.

Die physische Sicherheit des Cloud-Anbieters muss über den Lieferantenmanagementprozess (A.5.19–23) bewertet werden.

### Colocation-Einrichtungen

Bei Nutzung von Colocation-Rechenzentrumsplatz werden die Verantwortlichkeiten für physische Infrastruktur zwischen dem Colocation-Anbieter und der Organisation geteilt. Die Organisation muss:

- Eine formelle Verantwortlichkeitsmatrix im Colocation-Vertrag führen, die dokumentiert, welche Partei für jeden physischen Infrastruktur-Control (Überwachung, Umgebung, Versorgung) verantwortlich ist.
- Anbieterkontrollen jährlich durch SOC 2 Type II-Auditberichte oder ISO 27001-Zertifizierung verifizieren.
- Die Verantwortung für Überwachungs- und Umgebungskontrollen innerhalb des zugewiesenen Bereichs der Organisation behalten (z. B. Umgebungsüberwachung auf Rack-Ebene, Cage-Zugangskontolen).

## Grundsatz

Physische und umgebungsbezogene Sicherheit basiert auf dem Prinzip, Informationsverarbeitungsanlagen vor unbefugtem Zugriff, Umgebungsbedrohungen und Versorgungsausfällen zu schützen — proportional zur Kritikalität der enthaltenen Werte. Controls werden auf Grundlage einer dokumentierten Risikobewertung und der in dieser Richtlinie definierten Einrichtungskritikalitätsstufen ausgewählt.

---

## Physische Sicherheitsüberwachung (A.7.4)

> *Räumlichkeiten sollten kontinuierlich auf unbefugten physischen Zugang überwacht werden.*

Die physische Sicherheitsüberwachung muss unbefugten physischen Zugang zu Einrichtungen und eingeschränkten Bereichen erkennen und abschrecken. Design und Implementierung des Überwachungssystems müssen der Einrichtungskritikalität proportional sein.

### Physische Sicherheitssysteme

Folgende physische Sicherheitssysteme müssen implementiert und unterhalten werden. Organisationen müssen die tatsächlich eingesetzten Systeme (oder den Auswahlstatus) für jede Kategorie angeben:

| Systemkategorie | Zweck | Beispiellösungen | Status |
|----------------|-------|-----------------|--------|
| **Zugangskontrollsystem** | Badge-basierter Zutritt/Austritt mit Ereignisprotokollierung | Verkada, Genetec, Honeywell, Lenel, ASSA ABLOY, Salto | [Angabe oder „Auswahl läuft"] |
| **CCTV / Videoüberwachung** | Visuelle Überwachung und Aufzeichnung | Verkada, Axis, Milestone, Genetec | [Angabe oder „Auswahl läuft"] |
| **Einbruchmeldeanlage** | Perimeter- und Innenraum-Einbrucherkennung | Honeywell, Bosch, DSC, Texecom | [Angabe oder „Auswahl läuft"] |
| **Alarmüberwachungsdienst** | 24/7-Alarmreaktions- und Einsatzdienst | Securitas, Protectas, lokale Leitstelle | [Angabe oder „Auswahl läuft"] |
| **Umgebungsüberwachung** | Temperatur-, Feuchtigkeits-, Wassererkennungssensoren | Paessler PRTG, Raritan, APC NetBotz, Sensaphone | [Angabe oder „Auswahl läuft"] |
| **Gebäudemanagementsystem (BMS)** | Zentralisierte Gebäudedienststeuerung (HVAC, Beleuchtung, Strom) | Siemens Desigo, Honeywell Niagara, Schneider EcoStruxure | [Angabe oder „Auswahl läuft"] |
| **Brandmeldung und -löschung** | Rauch-/Wärmedetektion und Löschanlage mit Inertgas | Siemens, Minimax, Kidde, Wagner | [Angabe oder „Auswahl läuft"] |
| **USV-Systeme** | Unterbrechungsfreie Stromversorgung für kritische Geräte | Eaton, APC/Schneider, Vertiv/Liebert, Riello | [Angabe oder „Auswahl läuft"] |
| **Notstromaggregat** | Erweiterte Stromkontinuität | Caterpillar, Cummins, MTU, SDMO | [Angabe oder „Auswahl läuft"] |

**Integrationsanforderungen**: Wo technisch machbar, sollten physische Sicherheitssysteme Ereignisse an [SIEM] zur Korrelation mit logischen Sicherheitsereignissen weiterleiten. Mindestens müssen Zugangskontollereignisse und Einbruchmeldealerme weitergeleitet werden.

### Elektronische Zugangskontrolle

- Elektronische Zugangskontrolle muss an allen Eingangs- und Ausgangspunkten der Einrichtung mit Authentifizierung, Ereignisprotokollierung und Integration in das Identitätsmanagement implementiert sein.
- Zugriffsereignisse (gewährt, abgelehnt, erzwungene Tür, Tür offen gehalten) müssen mit Zeitstempel, individueller Identität und Türkennung protokolliert werden.
- Zugriffsprotokolle müssen mindestens 12 Monate aufbewahrt werden.
- Zugriffsrechte müssen halbjährlich überprüft und widerrufen werden, wenn sie nicht mehr benötigt werden (z. B. Rollenwechsel, Kündigung).
- Der taggleiche Zugangswiderruf muss bei Beendigung des Arbeitsverhältnisses durchgesetzt werden.

#### Prozess zur Zugriffsrechteüberprüfung

Physische Zugriffsrechte müssen halbjährlich anhand des folgenden strukturierten Workflows überprüft werden:

| Schritt | Massnahme | Eigentümer | Zeitrahmen |
|---------|-----------|------------|------------|
| 1 | Zugriffsrechtebericht aus [Zugangskontrollsystem] erstellen, der alle Personen nach Zone und Abteilung auflistet | Facilities Manager | 1. Arbeitstag des Überprüfungsmonats |
| 2 | Zonenspezifische Zugangslisten zur Bestätigung an autorisierende Manager verteilen | Facilities Manager | Innerhalb von 2 Arbeitstagen |
| 3 | Manager überprüfen den Zugang jeder Person: bestätigen als erforderlich, markieren zur Entfernung oder eskalieren Anfragen | Direkte Vorgesetzte | Innerhalb von 10 Arbeitstagen |
| 4 | Manager-Antworten zusammenstellen; Widerrufsliste für nicht mehr benötigten Zugang erstellen | Facilities Manager | Innerhalb von 2 Arbeitstagen nach Bestätigungsfrist |
| 5 | Zugangswiderrufe im [Zugangskontrollsystem] durchführen | Facilities Manager | Innerhalb von 5 Arbeitstagen |
| 6 | Bestätigung der abgeschlossenen Widerrufe; Bestätigungsunterlagen ablegen | Facilities Manager | Innerhalb von 2 Arbeitstagen |

**Eskalation bei Nicht-Antwort**:
- Manager-Nicht-Antwort nach 10 Arbeitstagen → Erinnerung mit 5-tägiger Verlängerung
- Manager-Nicht-Antwort nach 15 Arbeitstagen → Eskalation an Abteilungsleiter
- Manager-Nicht-Antwort nach 20 Arbeitstagen → Zugang für nicht bestätigte Personen in eingeschränkten Zonen bis zur Bestätigung gesperrt

**Abschlusskennzahlen**:
- Ziel: 100% der Zugriffsrechte pro Zyklus überprüft
- Ziel: Alle Widerrufe innerhalb von 5 Arbeitstagen nach Bestätigung durchgeführt
- Nichterfüllung wird dem ISB im vierteljährlichen Compliance-Bericht gemeldet

### Videoüberwachung (CCTV)

- CCTV-Abdeckung muss an Einrichtungseingängen, Zugangspunkten zu eingeschränkten Bereichen und kritischen Infrastrukturstandorten (Serverräume, Versorgungsräume) gewährleistet sein.
- CCTV-Systeme müssen mindestens während der Betriebszeiten kontinuierlich aufzeichnen; für Tier-1-Einrichtungen ist eine 24/7-Aufzeichnung erforderlich.
- Aufzeichnungsaufbewahrung: mindestens 30 Tage für allgemeine Bereiche, 90 Tage für eingeschränkte Bereiche. Bei Incident-Untersuchungen kann eine längere Aufbewahrung erforderlich sein.
- CCTV-Systeme müssen die anwendbaren Datenschutzanforderungen (schweizerisches nDSG, kantonale Vorschriften) einhalten. An überwachten Bereichen muss eine Beschilderung auf die Videoüberwachung hinweisen.
- Die Kameraqualität (Konnektivität, Bildqualität, Speicherkapazität) muss wöchentlich überprüft werden.

### Einbrucherkennung

- Einbruchmeldesysteme müssen in Tier-1-Einrichtungen installiert sein und Perimetertüren, Fenster und Zugangspunkte zu eingeschränkten Bereichen abdecken.
- Einbrucherkennung wird für Tier-2-Einrichtungen auf Grundlage der Risikobewertung empfohlen.
- Alarme müssen mit einem überwachten Reaktionspunkt verbunden sein (Security Operations, Alarmüberwachungsdienst oder [Alarmüberwachungsanbieter]).
- Das Einbruchmeldesystem muss vierteljährlich auf korrekte Funktion getestet werden.

### Besuchermanagement

- Alle Besucher müssen sich bei der Ankunft registrieren, eine temporäre Identifikation erhalten und in eingeschränkten Bereichen begleitet werden.
- Besucheraufzeichnungen (Name, Organisation, Gastgeber, Ankunfts-/Abfahrtszeit) müssen mindestens 12 Monate aufbewahrt werden.
- Besucher-Badges müssen den Besucherstatus klar kennzeichnen, den Zugang zu eingeschränkten Bereichen verweigern und am Ende des Ausgabetags automatisch ablaufen.

### Überwachung und Integration von Sicherheitsereignissen

- Physische Sicherheitsereignisse (Zugang verweigert, erzwungener Zutritt, Einbruchmeldesystemalarm, Tür offen gehalten) sollten, wo technisch machbar, zur Korrelation mit logischen Sicherheitsereignissen an [SIEM] weitergeleitet werden.
- Wiederholte fehlgeschlagene Zugriffsversuche (3 oder mehr innerhalb von 30 Minuten) lösen Alert und Untersuchung aus.

### Schutz des Überwachungssystems

- Design und Konfiguration der Überwachungssysteme müssen vertraulich behandelt werden.
- Überwachungssysteme müssen gegen Manipulation, unbefugte Deaktivierung und Remote-Interferenz geschützt sein.
- Überwachungsgeräte müssen an USV-gesicherter Stromversorgung betrieben werden, um den kontinuierlichen Betrieb bei Stromausfällen sicherzustellen.

---

## Umgebungsschutz (A.7.5)

> *Schutz vor physischen und umgebungsbezogenen Bedrohungen sollte konzipiert und umgesetzt werden.*

Umgebungsschutzmassnahmen müssen Schäden durch Feuer, Wasser, Klimaextreme und andere physische Bedrohungen verhindern oder mindern. Der Schutzgrad muss der Einrichtungskritikalität proportional sein.

### Bewertung von Umgebungsbedrohungen

- Für jede Einrichtung muss eine Risikobewertung der Umgebungsbedrohungen durchgeführt werden, unter Berücksichtigung geografischer Lage, Gebäudeeigenschaften, historischer Ereignisse und angrenzender Gefahren.
- Die Bewertung muss jährlich überprüft und nach Vorfällen oder wesentlichen Einrichtungsänderungen aktualisiert werden.
- Zu berücksichtigende Bedrohungen umfassen: Brand, Überschwemmung, Wassereintritt, Temperaturextreme, Feuchtigkeit, Blitzschlag, seismische Aktivität, Strukturversagen, zivile Unruhen und industrielle Gefahren.

### Branderkennung und -löschung

Branderkennung muss in allen Einrichtungen implementiert sein, die Informationsverarbeitungsgeräte enthalten.

| Anforderung | Tier 1 — Kritische Einrichtungen | Tier 2 — Standardeinrichtungen |
|-------------|----------------------------------|--------------------------------|
| **Erkennung** | Rauchdetektion (VESDA/Ansaugrauchmelder oder konventionell) in allen Zonen; Wärmedetektion in Versorgungsbereichen | Konventionelle Rauchdetektion in Server-/Gerätebereichen |
| **Löschung** | Löschanlage mit Inertgas (z. B. IG-541/Inergen, IG-55/Argonite oder gleichwertig) in Serverräumen und Rechenzentrumsetagen | Löschanlage erforderlich, wenn Gerätewert CHF 500'000 übersteigt oder Datenkritikalität dies erfordert; andernfalls tragbare Feuerlöscher |
| **Alarmintegration** | Verbunden mit Gebäudemanagementsystem (BMS), Feuerwehr und Sicherheitsüberwachung | Verbunden mit Gebäude-Brandmeldeanlagentableau |
| **Inspektion** | Halbjährliche Inspektion und jährlicher Volltest gemäss kantonalen Brandschutzvorschriften | Jährliche Inspektion gemäss kantonalen Brandschutzvorschriften |

**Hinweise zu Löschmitteln**: Für besetzte Räume mit elektronischen Geräten sind Löschmittelsysteme erforderlich, die NFPA 2001 und ISO 14520 entsprechen. Wasserbasierte Sprinkleranlagen dürfen nicht in Serverräumen oder Rechenzentren eingesetzt werden. Organisationen sollten bei der Auswahl von Löschmittelsystemen die langfristige Verfügbarkeit und das Umweltprofil der ausgewählten Mittel berücksichtigen.

#### Auswahlhilfe für Löschmittel

Organisationen, die Löschmittelsysteme für Serverräume und Rechenzentren auswählen, sollten Optionen nach Wirksamkeit, Sicherheit, Umweltprofil und langfristiger regulatorischer Verfügbarkeit bewerten:

| Mittel | Typ | Ozonabbau | Globales Erwärmungspotenzial | Sicherheit (besetzte Räume) | Verfügbarkeitsaussicht | Empfehlung |
|--------|-----|-----------|-----------------------------|-----------------------------|----------------------|------------|
| **IG-541 (Inergen)** | Inertgasgemisch (N₂, Ar, CO₂) | Null | Null | Sicher — atembar bei Auslegungskonzentration | Langfristig stabil | **Empfohlen** für Neuinstallationen |
| **IG-55 (Argonite)** | Inertgasgemisch (N₂, Ar) | Null | Null | Sicher — atembar bei Auslegungskonzentration | Langfristig stabil | Empfohlene Alternative |
| **IG-100 (Stickstoff)** | Reiner Stickstoff | Null | Null | Sicher — atembar bei Auslegungskonzentration | Langfristig stabil | Geeignet für grosse Volumen |
| **FK-5-1-12 (Novec 1230)** | Fluoroketon | Null | 1 | Sicher — geringe Toxizität | Stabil (3M-Produktion läuft) | Akzeptabel für platzbeschränkte Installationen |
| **HFC-227ea (FM-200)** | Fluorkohlenwasserstoff | Null | 3.220 | Sicher — geringe Toxizität bei Auslegungskonzentration | **Phase-down** unter EU F-Gas-Verordnung und Kigali-Ergänzung | **Nicht empfohlen** für Neuinstallationen |

**Auswahlkriterien für Neuinstallationen**:
1. Inertgassysteme (IG-541, IG-55) bevorzugt aufgrund null Umweltauswirkungen und langfristiger regulatorischer Sicherheit
2. FK-5-1-12 (Novec 1230) akzeptabel bei begrenztem Zylinderstauraum (geringerer Volumenbedarf als Inertgase)
3. HFC-227ea (FM-200) nicht für Neuinstallationen empfohlen aufgrund des regulatorischen Phase-down-Pfads

**Bestehende FM-200-Systeme**: Kein sofortiger Austausch erforderlich. Gemäss Herstellerplan warten. Budget für Ersatz durch Inertgassystem bei der nächsten grösseren Sanierung oder innerhalb von 10 Jahren (je nachdem, was früher eintritt) einplanen. Austauschzeitplan im Einrichtungs-Investitionsplan dokumentieren.

- Brandschutztüren an Sicherheitsperimetern müssen gemäss anwendbaren Brandschutzvorschriften alarmiert, überwacht und getestet werden.
- Notbeleuchtung und Evakuierungswege müssen gewartet und halbjährlich getestet werden.

### Wassererkennung und -schutz

- Wassererkennungssensoren müssen in Tier-1-Einrichtungen installiert sein — unter Doppelböden, über abgehängten Decken, in der Nähe der Kühlinfrastruktur und in allen Zonen, in denen Wassereintritt möglich ist.
- Tier-2-Einrichtungen müssen Wassererkennung in Risikobereichen aufweisen (in der Nähe von Leitungen, HVAC-Systemen, ebenerdigen Räumen).
- Wasseralarme müssen sofortige Alerts an das Einrichtungsmanagement auslösen.
- Einrichtungen müssen Entwässerung, Wasserdichtung und physische Barrieren entsprechend dem identifizierten Überschwemmungsrisiko implementieren.

### Klimatisierung

Informationsverarbeitungsgeräte müssen in kontrollierten Temperatur- und Feuchtigkeitsbereichen betrieben werden, um Schäden zu verhindern und einen zuverlässigen Betrieb zu gewährleisten.

| Parameter | Empfohlener Bereich (ASHRAE A1–A4-Klasse) | Warnschwelle | Kritische Schwelle |
|-----------|-------------------------------------------|--------------|--------------------|
| **Temperatur** | 18–27 °C (64–81 °F) | Ausserhalb 18–27 °C | Unter 15 °C oder über 32 °C |
| **Feuchtigkeit** | 20–80% relative Luftfeuchtigkeit (RH) | Ausserhalb 20–80% RH | Unter 10% RH oder über 90% RH |
| **Temperaturänderungsrate** | < 5 °C pro Stunde | Überschreitet 5 °C/h | Überschreitet 10 °C/h |

**Tier-1-Einrichtungen**: Temperatur muss bei 18–27 °C mit einer Toleranz von +/- 2 °C gehalten werden. Kontinuierliche Umgebungsüberwachung mit Echtzeit-Alerting ist erforderlich.

**Tier-2-Einrichtungen**: Temperatur muss bei 18–27 °C mit einer Toleranz von +/- 5 °C gehalten werden. Umgebungsüberwachung mit Alerting während der Betriebszeiten ist erforderlich.

Umgebungsüberwachungsdaten (Temperatur, Feuchtigkeit) müssen protokolliert und mindestens 12 Monate aufbewahrt werden.

#### Konfiguration der Umgebungsüberwachungs-Alerts

Umgebungsüberwachungssysteme müssen mit folgenden Alarmschwellen, Reaktionsanforderungen und Eskalationspfaden konfiguriert sein:

| Parameter | Warnalert | Kritischer Alert | Reaktionszeit (Tier 1) | Reaktionszeit (Tier 2) |
|-----------|-----------|-----------------|----------------------|----------------------|
| **Temperatur** | Ausserhalb 18–27 °C | Unter 15 °C oder über 32 °C | 15 Minuten | Nächster Arbeitstag |
| **Feuchtigkeit** | Ausserhalb 20–80% RH | Unter 10% oder über 90% RH | 15 Minuten | Nächster Arbeitstag |
| **Temperaturänderungsrate** | Überschreitet 5 °C/Stunde | Überschreitet 10 °C/Stunde | 15 Minuten | 1 Stunde |
| **Wassererkennung** | Beliebige Sensoraktivierung | Mehrere Sensoren oder steigendes Wasser | Sofort | 30 Minuten |
| **Strom (USV auf Batterie)** | USV wechselt auf Batterie | Batterie unter 50% Kapazität | Sofort | 15 Minuten |
| **Kühlsystem** | Ausfall einer Einheit (redundante Einheit aktiv) | Alle Kühleinheiten ausgefallen | 30 Minuten | 1 Stunde |

**Alert-Routing**:
- Warnalerts → Facilities Manager + IT-Betrieb (E-Mail + Dashboard)
- Kritische Alerts → Facilities Manager + IT-Betrieb + ISB (E-Mail + SMS + Dashboard)
- Kritische Alerts ausserhalb der Geschäftszeiten → Bereitschafts-Einrichtungskontakt + IT-Betriebs-Bereitschaft

**Eskalation**:
- Warnalert nach 30 Minuten nicht bestätigt → Auf kritisch eskalieren
- Kritischer Alert nach 15 Minuten nicht bestätigt → An ISB + Geschäftsleitung eskalieren

**Alert-Tests**: Umgebungsüberwachungs-Alert-Pfade müssen vierteljährlich getestet werden (Schwellenwertüberschreitung simulieren; Alertzustellung an alle konfigurierten Empfänger innerhalb der Zielfrist verifizieren).

### Strukturelle und physische Schutzmassnahmen

- Gebäudeaussenhülle (Dach, Wände, Böden) muss solide und den identifizierten Bedrohungen angemessen konstruiert sein.
- Blitzschutz muss für Gebäude mit Informationsverarbeitungsanlagen angebracht werden. Überspannungsschutz muss an eingehenden Strom- und Telekommunikationsleitungen installiert sein.
- Die Gerätepositionierung muss das Risiko durch identifizierte Umgebungsbedrohungen minimieren (z. B. Kellerlagen in überschwemmungsgefährdeten Gebieten und Standorte neben Gefahrenprozessen vermeiden).
- Richtlinien zu Essen, Trinken und Rauchen in der Nähe von Informationsverarbeitungsanlagen müssen festgelegt und kommuniziert werden.

### Notfallreaktion

Notfallreaktionsverfahren müssen für Umgebungsvorfälle dokumentiert und regelmässig getestet werden. Notfallkontaktinformationen müssen an Einrichtungseingängen und in Serverräumen ausgehängt sein.

#### Brandnotfallreaktion

| Schritt | Massnahme | Eigentümer | Zeitrahmen |
|---------|-----------|------------|------------|
| 1 | Brandmeldeanlage aktiviert (automatische Erkennung oder manueller Druckknopfmelder) | Automatisch / beliebiges Personal | Sofort |
| 2 | Betroffene Zone evakuieren; Sammlung am designierten Sammelplatz | Alle Mitarbeitenden | Innerhalb von 3 Minuten |
| 3 | Feuerwehr benachrichtigt (automatisch via BMS oder manuell) | Facilities Manager / Empfang | Innerhalb von 2 Minuten |
| 4 | Bestätigung, dass alle Mitarbeitenden evakuiert sind (Kopfzählung am Sammelplatz) | Etagen-Notfallwarte | Innerhalb von 5 Minuten |
| 5 | Bei Aktivierung der Gaslöschanlage: NICHT wieder betreten bis die Gaskonzentration als sicher verifiziert wurde | Facilities Manager | Nach Löschung |
| 6 | Feuerwehr gibt Räumlichkeiten frei; Schadensbeurteilung eingeleitet | Facilities Manager + ISB | Nach Entwarnung |

**Massnahmen nach Brand**: Geräteschadensbeurteilung innerhalb von 24 Stunden; Datenintegritätsverifizierung für betroffene Systeme; Vorfallbericht innerhalb von 48 Stunden; Versicherungsbenachrichtigung falls zutreffend.

#### Wassereintritt / Überschwemmungs-Notfallreaktion

| Schritt | Massnahme | Eigentümer | Zeitrahmen |
|---------|-----------|------------|------------|
| 1 | Wasseralarm ausgelöst oder Wasser visuell erkannt | Automatisch / beliebiges Personal | Sofort |
| 2 | Wasserquelle identifizieren (Leitungen, externen Eintritt, HVAC-Kondensat) | Facilities Manager | Innerhalb von 15 Minuten |
| 3 | Falls Quelle kontrollierbar: Isolieren (Absperrventil schliessen, Fluss umleiten) | Facilities Manager | Sofort |
| 4 | Geräte und Medien über den Wasserstand heben oder in trockenen Bereich bringen | IT-Betrieb + Einrichtungen | Sofort |
| 5 | Strom zu gefährdeten Geräten trennen (wenn sicher durchführbar) | IT-Betrieb | Nach Bedarf |
| 6 | Wasserextraktion einsetzen (Pumpen, Nasssauger); Notfallrestaurierungsunternehmen bei ausgedehntem Schaden beauftragen | Facilities Manager | Innerhalb von 1 Stunde |

#### Kühlungsausfall-Notfallreaktion

| Schritt | Massnahme | Eigentümer | Zeitrahmen |
|---------|-----------|------------|------------|
| 1 | Temperaturalert empfangen (Warnschwelle überschritten) | Automatischer Alert an IT-Betrieb | Sofort |
| 2 | Kühlsystemstatus prüfen; Neustart oder Failover auf redundante Einheit versuchen | Facilities Manager | Innerhalb von 15 Minuten |
| 3 | Bei Temperaturannäherung an kritischen Schwellenwert (32 °C): Geordnetes Herunterfahren nicht wesentlicher Systeme beginnen, um Wärmelast zu reduzieren | IT-Betrieb | Innerhalb von 30 Minuten |
| 4 | Temporäre Kühlung einsetzen (tragbare Klimageräte) falls verfügbar | Facilities Manager | Innerhalb von 1 Stunde |
| 5 | Bei Überschreitung des kritischen Schwellenwerts: Geordnetes Herunterfahren aller Systeme; Stakeholder benachrichtigen | IT-Betrieb + ISB | Nach Bedarf |
| 6 | HVAC-Auftragnehmer für Notfallreparatur beauftragen | Facilities Manager | Innerhalb von 2 Stunden |

#### Vollständiger Stromausfall-Notfallreaktion

| Schritt | Massnahme | Eigentümer | Zeitrahmen |
|---------|-----------|------------|------------|
| 1 | Netzstromausfall erkannt; USV aktiviert automatisch | Automatisch | Sofort |
| 2 | Generatorstart verifizieren (Tier 1) oder USV-Last-Sustaining bestätigen | Facilities Manager | Innerhalb von 2 Minuten |
| 3 | Bei Generatorstartversagen: Geordnetes Herunterfahren nicht wesentlicher Systeme beginnen | IT-Betrieb | Innerhalb von 10 Minuten |
| 4 | Versorgungsunternehmen benachrichtigen; geschätzte Wiederherstellungszeit anfordern | Facilities Manager | Innerhalb von 15 Minuten |
| 5 | Bei Annäherung der USV-Laufzeit an Limit und kein Generator verfügbar: Vollständiges geordnetes Herunterfahren aller Systeme | IT-Betrieb | Vor USV-Erschöpfung |
| 6 | Nach Wiederherstellung: Alle Systeme auf korrekten Neustart prüfen; Datenintegrität für betroffene Systeme prüfen | IT-Betrieb | Nach Stromwiederherstellung |

Notfallverfahren müssen mindestens jährlich durch Übungen oder Tabletop-Übungen getestet werden.

### Physische Sicherheits-Awareness-Schulung

Alle Personen mit Einrichtungszugang müssen eine physische Sicherheits-Awareness-Schulung absolvieren. Die Schulung wird jährlich durchgeführt, wobei neue Mitarbeitende sie innerhalb von 10 Arbeitstagen nach Gewährung des Einrichtungszugangs abschliessen müssen.

#### Schulungslehrplan

| Modul | Inhalt | Dauer | Zielgruppe |
|-------|--------|-------|------------|
| **Modul 1: Grundlagen der Einrichtungssicherheit** | Einrichtungskritikalitätsstufen; Sicherheitszonenmodell; Badge-Nutzung und Verantwortlichkeiten; Besuchermanagementpflichten; Tailgating-Prävention | 10 Minuten | Alle Mitarbeitenden |
| **Modul 2: Umgebungsbewusstsein** | Brandschutz und Evakuierungswege; Wassererkennungsbewusstsein; Bedeutung der Klimatisierung; Meldung von Umgebungsanomalien; Notfallkontaktnummern | 10 Minuten | Alle Mitarbeitenden |
| **Modul 3: Erkennung und Meldung von Vorfällen** | Erkennen physischer Sicherheitsereignisse (unbefugte Personen, offengehaltene Türen, Umgebungsanomalien); Meldekanäle und Erwartungen; Beweissicherung (nicht berühren/bewegen) | 5 Minuten | Alle Mitarbeitenden |
| **Modul 4: Rollenspezifische Verantwortlichkeiten** | Besucherbegleitungsverfahren; Serverraumzugangsprotokolle; Notfallwartenpflichten; Bewusstsein für Versorgungssysteme | 5 Minuten | Personal mit Tier-1-Einrichtungszugang oder Begleitungsverantwortung |

**Gesamtdauer**: 30 Minuten (alle Module).

**Beurteilung**: Kurzquiz (5 Fragen, 80% Bestehensquote erforderlich). Nicht bestanden: Wiederholung innerhalb von 5 Arbeitstagen.

**Tier-1-Einrichtungsorientierung** (zusätzlich, persönlich):
- Physische Führung durch Notausgänge, Feuerlöscherstandorte und Sammelplätze
- Demonstration der Kartenlesegeräte und Zugangsverfahren
- Einführung in Umgebungsüberwachungsanzeigen (wo zutreffend)
- Dauer: 15 Minuten, durchgeführt vom Facilities Manager oder Beauftragten

**Schulungsabschluss-Ziel**: 95% des Personals mit Einrichtungszugang jährlich. Abschluss über [LMS oder Schulungsregister] verfolgt. Nichtabschluss nach 30 Tagen Überfälligkeit an direkten Vorgesetzten eskaliert; Einrichtungszugang nach 60 Tagen Überfälligkeit gesperrt.

---

## Versorgungseinrichtungen (A.7.11)

> *Informationsverarbeitungsanlagen sollten vor Stromausfällen und anderen Störungen durch Ausfälle von Versorgungseinrichtungen geschützt werden.*

Versorgungssysteme müssen mit Kapazität und Redundanz proportional zur Einrichtungskritikalität implementiert und regelmässig getestet werden, um die Betriebsbereitschaft zu gewährleisten.

### Stromschutz — Unterbrechungsfreie Stromversorgung (USV)

| Anforderung | Tier 1 — Kritische Einrichtungen | Tier 2 — Standardeinrichtungen |
|-------------|----------------------------------|--------------------------------|
| **Konfiguration** | N+1-Redundanz (zwei USV-Einheiten) | Einzelne USV |
| **Laufzeit** | Mindestens 30 Minuten pro Einheit (ausreichend für Generatorstart und -stabilisierung oder geordnetes Herunterfahren) | Mindestens 15 Minuten (ausreichend für geordnetes Herunterfahren) |
| **Überwachung** | Echtzeit-Überwachung mit automatischem Alerting bei Batteriestatus, Last und Transferereignissen | Überwachung während der Betriebszeiten |
| **Wartung** | Batterieaustausch gemäss Herstellerplan; jährlicher Kapazitätstest | Batterieaustausch gemäss Herstellerplan |

- USV-Systeme müssen alle kritischen Informationsverarbeitungsgeräte, Netzwerkinfrastruktur und Sicherheitssysteme (Zugangskontrolle, CCTV, Branderkennung) schützen.
- USV-Systeme müssen für das geordnete Herunterfahren von Geräten konfiguriert sein, die kritische Geschäftsoperationen unterstützen, wenn ein verlängerter Ausfall die USV-Laufzeit überschreitet.

#### USV-Bemessungsmethodik

Die USV-Kapazität muss anhand folgenden Vier-Schritt-Prozesses berechnet werden, um eine ausreichende Laufzeit für geschützte Geräte zu gewährleisten:

**Schritt 1 — Lastberechnung**:
- Alle zu schützenden Geräte inventarisieren (Server, Netzwerk-Switches, Speicher, Sicherheitssysteme)
- Gesamten Strombedarf in Watt (W) oder Voltampere (VA) aus Geräteschildern oder gemessenem Stromverbrauch summieren
- Leistungsfaktorkorrektur anwenden, wenn VA-Werte verwendet werden (typischer IT-Last-Leistungsfaktor: 0,9)

**Schritt 2 — Wachstumsfaktor**:
- 20–30% Wachstumsreserve über die aktuelle Last anwenden, um geplante Gerätezugaben zu berücksichtigen
- Tier-1-Einrichtungen: 30% Wachstumsreserve (3-Jahres-Planungshorizont)
- Tier-2-Einrichtungen: 20% Wachstumsreserve

**Schritt 3 — USV-Kapazitätsauswahl**:
- USV-Einheit(en) mit Nennleistung über dem Gesamtwert aus Schritt 2 auswählen
- Tier 1: N+1-Redundanz (zwei USV-Einheiten, jede in der Lage, die volle Last unabhängig zu tragen)
- Tier 2: Einzelne USV mit Kapazität über dem Gesamtwert aus Schritt 2
- Batterieleistung bei berechneter Last verifizieren, dass sie die Mindestanforderungen erfüllt (30 Minuten Tier 1, 15 Minuten Tier 2)

**Schritt 4 — Laufzeitverifizierung**:
- Nach Installation: Vollast-Entladetest durchführen, um tatsächliche Laufzeit zu verifizieren
- Tatsächliche vs. berechnete Laufzeit dokumentieren
- Falls tatsächliche Laufzeit < Mindestanforderung: Batteriemodule hinzufügen oder geschützte Last reduzieren
- Jährlich beim Kapazitätstest neu verifizieren (Batterieabbau reduziert die Laufzeit mit der Zeit)

**USV-Bemessungsaufzeichnung**: Dokumentiert im Einrichtungs-Asset-Register mit Lastberechnung, ausgewähltem USV-Modell, Nennleistung, gemessener Last, berechneter Laufzeit und tatsächlich getesteter Laufzeit.

### Notstromversorgung

| Anforderung | Tier 1 — Kritische Einrichtungen | Tier 2 — Standardeinrichtungen |
|-------------|----------------------------------|--------------------------------|
| **Generator** | Notstromaggregat erforderlich | Nicht erforderlich (risikobasierte Entscheidung) |
| **Kraftstoffkapazität** | Mindestens 48 Stunden bei Volllast | Nicht zutreffend, es sei denn, Generator installiert |
| **Startzeit** | Automatischer Start innerhalb von 30 Sekunden nach Netzstromausfall; automatischer Transferschalter (ATS) | Manuell oder automatisch je nach Bedarf |
| **Kraftstoffmanagement** | Kraftstoffqualität jährlich getestet; Betankungsverträge vorhanden | Gemäss Herstelleranforderungen |

- Wo Generatoren installiert sind, müssen diese wöchentlich inspiziert und gemäss dem unten stehenden Testplan belastet werden.

#### Kraftstoffauswahl und -management für Generatoren

Der Kraftstofftyp muss basierend auf Einrichtungsanforderungen, lokaler Infrastruktur und Umweltüberlegungen ausgewählt werden:

| Kraftstofftyp | Vorteile | Nachteile | Empfohlener Einsatz |
|--------------|---------|-----------|---------------------|
| **Diesel** | Hohe Energiedichte; lange Lagerlebensdauer (12–18 Monate mit Behandlung); weit verbreitet; zuverlässiger Kaltstart | Erfordert Kraftstofflagerung vor Ort; Kraftstoffqualität verschlechtert sich mit der Zeit; Umweltvorschriften für Tanklagerung | Tier-1-Einrichtungen mit langer autonomer Laufzeit (48+ Stunden) |
| **Erdgas** | Keine Kraftstofflagerung vor Ort; unbegrenzte Laufzeit (Versorgungsnetz); geringere Emissionen; reduzierter Wartungsaufwand | Abhängig von der Gas-Versorgungsleitung (kann bei regionaler Katastrophe ausfallen); geringere Energiedichte; erfordert gas-zertifiziertes Aggregat | Tier-1-Einrichtungen mit zuverlässiger Gas-Infrastruktur und getrenntem Versorgungspfad von der Stromversorgung |
| **Propan (LPG)** | Lange Haltbarkeit (unbegrenzt); saubere Verbrennung; zuverlässig in kaltem Klima | Erfordert Drucktanklagerung; geringere Energiedichte als Diesel; Tankbetankungslogistik | Tier-2-Einrichtungen; Backup für Erdgasgeneratoren |

**Kraftstoffkapazitätsberechnung** (Dieselgeneratoren):
1. Kraftstoffverbrauchsrate des Generators bei Volllast bestimmen (Liter/Stunde, aus Herstellerdaten)
2. Mit erforderlicher Laufzeit multiplizieren (48 Stunden für Tier 1)
3. 20% Sicherheitsreserve addieren
4. Ergebnis = minimale Kraftstofftankkapazität

**Kraftstoffmanagementanforderungen** (Diesel):
- Kraftstoffqualität jährlich getestet (Wassergehalt, mikrobielle Kontamination, Oxidationsstabilität)
- Kraftstoffbehandlung (Biozid, Stabilisator) gemäss Herstellerplan angewendet
- Tankinspektion jährlich (interne Korrosion, Wasseransammlung, strukturelle Integrität)
- Betankungsvertrag vorhanden mit garantierter Lieferung innerhalb von 24 Stunden nach Anfrage
- Mindest-Kraftstoffstand bei 75% Kapazität gehalten (automatische Überwachung wo möglich)

### Kühlsysteme

| Anforderung | Tier 1 — Kritische Einrichtungen | Tier 2 — Standardeinrichtungen |
|-------------|----------------------------------|--------------------------------|
| **Redundanz** | Duale Kühlpfade (mindestens N+1) | Einzelnes Kühlsystem |
| **Überwachung** | Kontinuierliche Temperaturüberwachung mit automatischem Alerting | Überwachung während der Betriebszeiten |
| **Ausfallreaktion** | Automatischer Failover auf redundante Einheit; Alert an Einrichtungsmanagement | Alert an Einrichtungsmanagement; manuelle Reaktion |

- Kühlkapazität muss für die aktuelle Wärmelast plus geplantes Wachstum ausreichend sein.
- Kühlsysteme müssen gemäss den Herstellerserviceplänen gewartet werden, wobei Luftfilter in den empfohlenen Intervallen ausgetauscht werden.

### Telekommunikationsredundanz

| Anforderung | Tier 1 — Kritische Einrichtungen | Tier 2 — Standardeinrichtungen |
|-------------|----------------------------------|--------------------------------|
| **Internetkonnektivität** | Dualer ISP mit automatischem Failover | Einzelner ISP (sekundärer ISP empfohlen auf Grundlage der Risikobewertung) |
| **Pfaddiversität** | Verschiedene physische Eintrittspunkte wo machbar | Einzelner Eintritt akzeptabel |
| **Überwachung** | Kontinuierlich mit automatischem Failover und Alerting | Überwachung während der Betriebszeiten |

- Strom- und Telekommunikationskabel, die Daten übertragen oder Informationsdienste unterstützen, müssen vor Abhören, Störungen oder Beschädigung geschützt sein.
- Stromkabel müssen von Kommunikationskabeln getrennt werden, um Störungen zu vermeiden.
- Der Zugang zu Kabelräumen und Patch-Panels muss durch physische Zugangskontolen eingeschränkt sein.

#### Telekommunikations-Failover-Verfahren

Automatisierte und manuelle Failover-Verfahren müssen dokumentiert und getestet werden, um Konnektivitätskontinuität sicherzustellen:

**Automatischer Failover** (Tier-1-Einrichtungen mit dualem ISP):

| Schritt | Massnahme | Zielzeit |
|---------|-----------|----------|
| 1 | Primärer ISP-Ausfall erkannt (Link ausgefallen, Paketverlust >5%, Latenz >200ms) | Erkennung innerhalb von 30 Sekunden |
| 2 | Automatischer Failover auf sekundären ISP durch Netzwerkgeräte eingeleitet | Failover innerhalb von 60 Sekunden |
| 3 | Alert an IT-Betrieb generiert (E-Mail + Überwachungsdashboard) | Sofort |
| 4 | IT-Betrieb verifiziert Dienstwiederherstellung und untersucht primären ISP-Ausfall | Innerhalb von 15 Minuten |
| 5 | Primärer ISP wiederhergestellt → automatisches Failback (oder manuelles Failback falls konfiguriert) | Gemäss ISP-Wiederherstellung |

**Manueller Failover** (Tier-2-Einrichtungen oder Single-ISP mit Backup):

| Schritt | Massnahme | Eigentümer |
|---------|-----------|------------|
| 1 | ISP-Ausfall gemeldet oder über Überwachung erkannt | IT-Betrieb |
| 2 | Verifizieren, dass Ausfall ISP-seitig ist (nicht interner Geräteausfall) | IT-Betrieb |
| 3 | Backup-Konnektivität aktivieren (4G/5G-Failover, mobiler Hotspot oder alternativer ISP) | IT-Betrieb |
| 4 | Betroffene Nutzer über eingeschränkte Konnektivität und geschätzte Wiederherstellungszeit informieren | IT-Betrieb |
| 5 | Primäre ISP-Wiederherstellung überwachen; normales Routing bei Verfügbarkeit wiederherstellen | IT-Betrieb |

**Einzelner ISP-Backup für Tier-2-Einrichtungen**: Wo ein einzelner ISP eingesetzt wird, muss ein 4G/5G-Mobilfunk-Failover-Gerät (z. B. Cradlepoint, Peplink oder gleichwertig) als Backup verfügbar sein. Das Failover-Gerät muss vierteljährlich getestet werden, um SIM-Aktivierung und ausreichende Bandbreite für kritische Dienste zu bestätigen.

### Testplan für Versorgungseinrichtungen

Alle Versorgungsresilienz-Systeme müssen regelmässig getestet werden, um die Betriebsbereitschaft zu verifizieren:

| System | Testtyp | Häufigkeit | Bestehensvoraussetzungen | Eigentümer |
|--------|---------|------------|--------------------------|------------|
| **USV** | Failover-Test (Netzstromausfall simulieren, Transfer auf Batterie verifizieren) | Vierteljährlich | Sauberer Transfer innerhalb der Nennzeit; Last für Nennlaufzeit gehalten | Facilities Manager |
| **USV** | Batteriekapazitätstest (Volllast-Entladung) | Jährlich | Batteriekapazität >= 80% der Nennkapazität | Facilities Manager |
| **Notstromaggregat** | Leerlaufstarttest | Monatlich | Start innerhalb von 30 Sekunden; stabile Spannung und Frequenz innerhalb von 60 Sekunden | Facilities Manager |
| **Notstromaggregat** | Lastbank-Test (mindestens 30% Nennleistung, 30 Minuten) | Halbjährlich | Trägt Nennlast; Abgastemperatur innerhalb der Grenzwerte | Facilities Manager |
| **Notstromaggregat** | Vollast-Transfer-Test (End-to-End mit ATS) | Jährlich | Automatischer Transfer und Rücktransfer ohne Unterbrechung der geschützten Last | Facilities Manager |
| **Kühlung** | Redundanz-Failover-Verifizierung | Vierteljährlich | Standby-Einheit aktiviert; Temperatur bleibt innerhalb der Schwellenwerte | Facilities Manager |
| **Telekommunikation** | ISP-Failover-Test | Jährlich | Automatischer oder manueller Failover innerhalb der dokumentierten Zielzeit; Dienste wiederhergestellt | IT-Betrieb |

Testergebnisse müssen dokumentiert werden mit: Testdatum, getestetes System, Testverfahren, Bestehen/Fehlschlagen-Ergebnis, identifizierte Probleme und Korrekturmassnahmen. Testaufzeichnungen müssen 5 Jahre aufbewahrt werden.

**Reaktion bei Testversagen**: Jedes Testversagen löst sofortige Untersuchung, vorübergehende Kompensationskontrollen (z. B. Einrichtungsnutzung einschränken, Überwachung intensivieren) und Behebung innerhalb von 30 Tagen aus. Wiederholte Versagen werden an den ISB eskaliert.

### Versorgungsüberwachung

- Versorgungssysteme (Strom, Kühlung, Telekommunikation) müssen in Echtzeit mit Alerting bei Ausfällen, Schwellenwertüberschreitungen und Verschlechterungszuständen überwacht werden.
- Versorgungsüberwachungssysteme sollten für zentrale Sichtbarkeit in [BMS] oder [Umgebungsüberwachungssystem] integriert werden.
- Versorgungsvorfälle müssen protokolliert und gemäss dem Incident-Management-Prozess gemeldet werden.

---

## Einrichtungskritikalitätsstufen

Einrichtungen müssen basierend auf der Geschäftsfolgenanalyse in Kritikalitätsstufen klassifiziert werden. Die Stufenklassifizierung steuert Überwachungsintensität, Umgebungsschutzanforderungen und Versorgungsresilienz-Niveaus in dieser Richtlinie.

| Attribut | Tier 1 — Kritisch | Tier 2 — Standard |
|----------|-------------------|-------------------|
| **Definition** | Rechenzentren, primäre Serverräume, Disaster-Recovery-Standorte | Unternehmensbüros, Niederlassungen, nicht-kritische Serverräume |
| **Klassifizierungskriterien** | Hostet Tier-1/2-Geschäftssysteme; verarbeitet VERTRAULICHE Daten; RTO < 4 Stunden | Hostet Tier-3/4-Systeme; verarbeitet INTERNE Daten; RTO > 4 Stunden |
| **Überwachung** | 24/7-Überwachung (SOC oder Alarmüberwachungsdienst); < 15-Min-Reaktions-SLA; Einbrucherkennung erforderlich | Überwachung während Geschäftszeiten (8/5); Reaktion am nächsten Arbeitstag akzeptabel; Einbrucherkennung risikobasiert |
| **Umgebung** | Brandlöschung + -erkennung; Wassererkennung in allen Zonen; Temperatur 18–27 °C +/- 2 °C; kontinuierliche Überwachung | Branderkennung obligatorisch (Löschung wenn Gerätewert > CHF 500k); Wassererkennung in Risikobereichen; Temperatur 18–27 °C +/- 5 °C |
| **Versorgung — Strom** | N+1-USV (dual, je 30 Min Laufzeit); Notstromaggregat (48 Std. Kraftstoff); ATS | Einzelne USV (mindestens 15 Min Laufzeit); Generator optional |
| **Versorgung — Kühlung** | Duale Kühlpfade (N+1); kontinuierliche Überwachung | Einzelnes Kühlsystem; Überwachung während Betriebszeiten |
| **Versorgung — Telecom** | Dualer ISP mit automatischem Failover; diverser Pfadeintritt | Einzelner ISP; sekundärer ISP empfohlen |
| **Überprüfungshäufigkeit** | Monatliche manuelle Verifizierung aller Systeme | Vierteljährliche manuelle Verifizierung aller Systeme |

**Stufenzuweisungsprozess**: Systemeigentümer bestimmen in Absprache mit dem Facilities Manager und ISB die geeignete Stufe für jede Einrichtung auf Grundlage der Geschäftsfolgenanalyse-Ergebnisse. Stufenzuweisungen müssen jährlich überprüft werden.

---

## Vorfallklassifizierung

Physische Infrastruktursicherheitsereignisse müssen basierend auf dem Schweregrad klassifiziert und beantwortet werden:

| Schweregrad | Beispiele | Erforderliche Reaktion |
|-------------|---------|----------------------|
| **Kritisch** | Unbefugter Zugang zu eingeschränkten Bereichen; physischer Einbruch; Geräteraub; grösserer Brand oder Überschwemmung; vollständiger Strom- oder Kühlungsausfall | Sofortige Reaktion; Incident-Management-Prozess aktivieren; ISB und Geschäftsleitung innerhalb von 1 Stunde benachrichtigen |
| **Hoch** | Wiederholte fehlgeschlagene Zugriffsversuche; Tailgating erkannt; verlorene Zugangsbadges; Umgebungsalerts nähern sich kritischen Schwellenwerten; partieller Versorgungsausfall | Untersuchung und Reaktion am selben Tag; ISB innerhalb von 4 Stunden benachrichtigen |
| **Mittel** | Tür-offen-gehalten-Alerts; häufige Fehlalarme; geringfügige Umgebungsüberschreitungen (innerhalb Alert- aber nicht kritischer Schwellenwerte); einzelnes Testversagen | Innerhalb von 5 Arbeitstagen dokumentiert und untersucht; Trendanalyse |
| **Niedrig** | Einzelner fehlgeschlagener Zugriffsversuch; geringfügige Richtlinienverstösse; geplante Wartungsbenachrichtigungen | Für Trendanalyse protokolliert; monatlich überprüft |

Physische Sicherheitsvorfälle müssen über den Incident-Management-Prozess der Organisation (A.5.24–28) gemeldet und verwaltet werden.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeit |
|-------|-------------------|
| **Informationssicherheitsbeauftragter (ISB)** | Gesamtverantwortung für die Richtlinie zur physischen Infrastruktursicherheit; Risikoakzeptanz für Ausnahmen; Budgetgenehmigung; Berichterstattung an die Geschäftsleitung zur physischen Sicherheitslage |
| **Facilities Manager** | Täglicher Betrieb der physischen Infrastruktur; Wartung von Umgebungs- und Versorgungssystemen; Lieferantenmanagement für Gebäudedienste; Durchführung des Testprogramms für Versorgungseinrichtungen |
| **Security Operations Manager** | Implementierung der physischen Sicherheitsüberwachung; Verwaltung des Zugangskontrollsystems; CCTV-Betrieb; Einbruchmeldeanlagenverwaltung; Koordination von physischen Sicherheitsvorfällen |
| **IT-Betrieb** | Physisch-logische Sicherheitsintegration (SIEM); Netzwerkinfrastruktur zur Unterstützung von Sicherheitssystemen; Verwaltung der Telekommunikationsredundanz |
| **Systemeigentümer** | Definieren physische Sicherheitsanforderungen für eigene Systeme; nehmen an der Einrichtungsstufenklassifizierung teil; melden physische Sicherheitsvorfälle |
| **Interne Revision** | Jährliche Verifizierung der physischen Sicherheits-Compliance; Nachweisüberprüfung; Control-Tests |
| **Alle Mitarbeitenden** | Melden physische Sicherheitsvorfälle und verdächtige Aktivitäten; halten Zugangskontroll- und Besuchermanagementverfahren ein; befolgen Notfallverfahren bei Umgebungsvorfällen |

---

## Nachweise für diese Richtlinie

| # | Nachweis | Eigentümer | Häufigkeit |
|---|---------|------------|------------|
| 1 | **Physische Zugangsprotokolle** (Zugang gewährt/verweigert Ereignisse mit individueller Identifikation) | Security Operations Manager | *Kontinuierliche Protokollierung; monatlich überprüft; 12 Monate aufbewahrt* |
| 2 | **CCTV-Systembetriebsaufzeichnungen** (Verfügbarkeitsberichte, Kamera-Gesundheitsprüfungen, Aufzeichnungsverifizierung) | Security Operations Manager | *Wöchentliche Gesundheitsprüfungen; 12 Monate aufbewahrt* |
| 3 | **Einbruchmeldeanlagen-Testaufzeichnungen** (vierteljährliche Testergebnisse, Alarmreaktionsverifizierung) | Security Operations Manager | *Vierteljährlich; 3 Jahre aufbewahrt* |
| 4 | **Besuchermanagementprotokolle** (Besucherregister mit Name, Organisation, Gastgeber, Begleitungs-Compliance) | Security Operations Manager | *Kontinuierlich; 12 Monate aufbewahrt* |
| 5 | **Zugriffsrechteüberprüfungsunterlagen** (halbjährliche Überprüfungsergebnisse, Widerrufsaktionen) | Security Operations Manager | *Halbjährlich; 3 Jahre aufbewahrt* |
| 6 | **Brand-Inspektions- und Testaufzeichnungen** (Erkennungs- und Löschsystem-Zertifikate, Brandschutztürentests) | Facilities Manager | *Halbjährlich / jährlich nach Stufe; 5 Jahre aufbewahrt* |
| 7 | **Umgebungsüberwachungsdaten** (Temperatur-, Feuchtigkeitsprotokolle; Schwellenwertüberschreitungsaufzeichnungen) | Facilities Manager | *Kontinuierliche Protokollierung; 12 Monate aufbewahrt* |
| 8 | **Wassererkennungssystem-Wartungs- und Testaufzeichnungen** | Facilities Manager | *Vierteljährliche Verifizierung; 3 Jahre aufbewahrt* |
| 9 | **USV-Testaufzeichnungen** (vierteljährliche Failover-Tests, jährliche Kapazitätstests) | Facilities Manager | *Gemäss Testplan; 5 Jahre aufbewahrt* |
| 10 | **Generator-Testaufzeichnungen** (monatliche Starttests, halbjährliche Belastungstests, jährliche Transfertests) | Facilities Manager | *Gemäss Testplan; 5 Jahre aufbewahrt* |
| 11 | **Kühlungsredundanz-Verifizierungsaufzeichnungen** (vierteljährliche Failover-Tests) | Facilities Manager | *Vierteljährlich; 3 Jahre aufbewahrt* |
| 12 | **Telekommunikations-Failover-Testaufzeichnungen** | IT-Betrieb | *Jährlich; 3 Jahre aufbewahrt* |
| 13 | **Umgebungsbedrohungs-Risikobewertung** (einrichtungsspezifische Risikobewertung mit Überprüfungshistorie) | Facilities Manager / ISB | *Jährliche Überprüfung; 5 Jahre aufbewahrt* |
| 14 | **Notfallübungsaufzeichnungen** (Übungsdatum, Szenario, Teilnehmer, Ergebnisse, Massnahmen) | Facilities Manager | *Jährlich; 3 Jahre aufbewahrt* |
| 15 | **Ausnahmenregister** (genehmigte Abweichungen von der Richtlinie mit Risikoakzeptanz und Kompensationskontrollen) | ISB | *Pro Ereignis; vierteljährlich überprüft; aktiv + 2 Jahre aufbewahrt* |

---

# Richtlinien-Compliance

## Compliance-Messung

Das Informationssicherheits-Management-Team überprüft die Compliance mit dieser Richtlinie durch verschiedene Methoden, einschliesslich, aber nicht beschränkt auf, Berichte von physischen Sicherheitssystemen, Versorgungstestaufzeichnungen, Umgebungsüberwachungsdaten, Einrichtungsinspektionen, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

Die Compliance wird anhand folgender gewichteter Kennzahlen bewertet:

| Kennzahl | Gewichtung | Messquelle |
|----------|------------|------------|
| Verfügbarkeit des Zugangskontrollsystems und Vollständigkeit der Protokolle | 20% | [Zugangskontrollsystem]-Protokolle |
| Compliance der Umgebungsparameter (Temperatur/Feuchtigkeit innerhalb der Schwellenwerte) | 20% | [Umgebungsüberwachungssystem] / [BMS] |
| Erfolgsquote der Versorgungsresilienz-Tests (alle Tests planmässig bestanden) | 15% | Testaufzeichnungen |
| Betriebsstatus der Brand- und Wassererkennungssysteme | 15% | Inspektionsaufzeichnungen |
| Einhaltung der Reaktionszeiten bei physischen Sicherheitsvorfällen | 15% | Vorfallaufzeichnungen |
| Besuchermanagement-Compliance (Registrierung, Begleitung, Badge-Rückgabe) | 10% | Besucherprotokolle |
| Schulungsabschluss zur physischen Sicherheits-Awareness | 5% | Schulungsunterlagen |

| Bewertung | Rating | Massnahme |
|-----------|--------|-----------|
| > 90% | Ausgezeichnet | Aktuelle Controls beibehalten |
| 75–89% | Gut | Mängel im nächsten Überprüfungszyklus beheben |
| 60–74% | Akzeptabel | Massnahmenplan innerhalb von 30 Tagen entwickeln |
| < 60% | Nicht-Compliant | Sofortige Behebung erforderlich; ISB-Eskalation |

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vorab vom Informationssicherheitsbeauftragten genehmigt und dokumentiert werden, mit dokumentierter Risikobewertung, Kompensationskontrollen und einem definierten Überprüfungsdatum (maximal 6 Monate, verlängerbar). Gültige Ausnahmeszenarien umfassen technische Undurchführbarkeit, unverhältnismässige Kosten im Verhältnis zum Risiko und temporäre Abweichungen bei Einrichtungsübergängen. Ausnahmen sind dem Management-Review-Team zu melden.

## Nicht-Compliance

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen bis hin zur Kündigung des Arbeitsverhältnisses unterliegen.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen berücksichtigen Änderungen im Einrichtungsbetrieb, Umgebungsrisikoprofile, regulatorische Anforderungen, technologische Fortschritte bei physischen Sicherheitssystemen, aus Vorfällen und Versorgungstestversagen gezogene Lehren sowie Audit-Ergebnisse.

---

# Abgedeckte Bereiche des ISO 27001-Standards

Richtlinie zur Sicherheit der physischen Infrastruktur — ISO 27001-Control-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien zur Informationssicherheit |
| Klausel 5.2 Politik | 5.4 Managementverantwortlichkeiten |
| Klausel 6.2 Informationssicherheitsziele | 5.36 Compliance mit Richtlinien, Regeln und Standards |
| Klausel 7.3 Bewusstsein | 6.3 Informationssicherheitsbewusstsein, -schulung und -ausbildung |
| | 6.4 Disziplinarverfahren |
| | **7.4 Physische Sicherheitsüberwachung** |
| | **7.5 Schutz vor physischen und umgebungsbezogenen Bedrohungen** |
| | 7.8 Geräteaufstellung und -schutz |
| | **7.11 Versorgungseinrichtungen** |
| | 7.12 Verkabelungssicherheit |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmenwerk | Relevanz |
|------------|---------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen für die physische Sicherheit von Datenverarbeitungsanlagen |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit einschliesslich physischer Massnahmen |
| EU DSGVO (soweit anwendbar) | Art. 32 — Sicherheit der Verarbeitung einschliesslich physischer Massnahmen |
| ISO/IEC 27001:2022 | Annex A Controls 7.4 (Physische Sicherheitsüberwachung), 7.5 (Umgebungsschutz), 7.11 (Versorgungseinrichtungen) |
| ISO/IEC 27002:2022 | Abschnitte 7.4, 7.5, 7.11 — Implementierungshinweise |
| ASHRAE | Thermische Richtlinien für Datenverarbeitungsumgebungen (Temperatur/Feuchtigkeit) |
| NFPA 2001 / ISO 14520 | Löschmittelsysteme für besetzte Räume |
| NFPA 110 | Prüfanforderungen für Not- und Ersatzstromsysteme |
| NIST SP 800-53 Rev 5 | PE-1 bis PE-20 — Familie der physischen und umgebungsbezogenen Schutzkontrollen |
| CIS Controls v8 | Control 1 (Inventar), Control 12 (Netzwerkinfrastruktur — physische Verkabelung) |
| **Bedingt**: FINMA Rundschreiben 2023/1 | Schweizerisches reguliertes Finanzinstitut — erweiterte physische Sicherheitsanforderungen |
| **Bedingt**: DORA (EU) 2022/2554 | EU-Finanzdienstleistungseinheit — operative Resilienz für ICT-Infrastruktur |
| **Bedingt**: NIS2 (EU) 2022/2555 | Wesentliche/wichtige Einheit in der EU — physische Sicherheit für kritische Infrastruktur |

---

<!-- QA_VERIFIED: 2026-03-29 -->
