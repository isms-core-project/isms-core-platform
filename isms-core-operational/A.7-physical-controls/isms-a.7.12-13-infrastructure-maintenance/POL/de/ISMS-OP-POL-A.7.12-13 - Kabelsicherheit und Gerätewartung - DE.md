<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.12-13-DE:operational:OP-POL:a.7.12-13 -->
**ISMS-OP-POL-A.7.12-13 — Kabelsicherheit und Gerätewartung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Kabelsicherheit und Gerätewartung |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.7.12-13 |
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
| 1.0 | [Datum] | ISB | Erste operative Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt von**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Controls A.7.12, A.7.13 — Kabelsicherheit, Gerätewartung
- ISO/IEC 27002:2022 Abschnitte 7.12, 7.13 — Umsetzungshinweise
- NIST SP 800-53 Rev 5 PE-4 (Zugangskontrolle für Übertragung), PE-9 (Stromversorgungsgeräte und Verkabelung), MA-2 (Kontrollierte Wartung), MA-5 (Wartungspersonal)
- IEC 11801 / EN 50173 / TIA-568 — Strukturierte Verkabelungsstandards
- Schweizer NIN (Niederspannungs-Installationsnorm) — Niederspannungs-Installationsstandards

**Verwandte Annex-A-Controls**:

| Control | Bezug zu Kabelsicherheit und Gerätewartung |
|---------|-------------------------------------------|
| A.5.9 Inventar von Informationen und zugehörigen Assets | Asset-Inventar gewährleistet Vollständigkeit des Wartungsprogramms |
| A.5.24–28 Incident-Management-Lebenszyklus | Infrastrukturausfälle werden im Incident Management eskaliert |
| A.5.30 IKT-Bereitschaft für Geschäftskontinuität | Geräteverfügbarkeit unterstützt Geschäftskontinuitätsziele |
| A.7.1–3 Physische Sicherheitsperimeter und Eingang | Zugangskontrolle zu Kabelräumen und Verteilerräumen |
| A.7.4 Physische Sicherheitsüberwachung | Überwachung von Infrastrukturbereichen, durch die Kabel geführt werden |
| A.7.5 Schutz vor physischen und Umweltbedrohungen | Umweltschutz für Verkabelung und Geräte |
| A.7.8–9 Geräteaufstellung und -schutz | Geräteplatzierung berücksichtigt Kabelführung und Wartungszugang |
| A.7.14 Sichere Entsorgung oder Wiederverwendung von Geräten | Entsorgungsverfahren gelten bei Geräteausmusterung nach Wartungs-End-of-Life |
| A.8.6 Kapazitätsmanagement | Kapazitätsplanung informiert Wartungsplanung und Kabelinfrastrukturgrössenberechnung |
| A.8.32 Änderungsmanagement | Infrastruktur- und Verkabelungsänderungen folgen dem Änderungsmanagementprozess |

**Verwandte interne Richtlinien**:

- Richtlinie zur physischen Zugangskontrolle
- Richtlinie zur Sicherheit der physischen Infrastruktur
- Richtlinie zur Geräteaufstellung und zum -schutz
- Asset-Management-Richtlinie
- Änderungsmanagement-Richtlinie
- Incident-Management-Richtlinie
- Richtlinie zur Geschäftskontinuität und Disaster Recovery

---

# Richtlinie zur Kabelsicherheit und Gerätewartung

## Zweck

Zweck dieser Richtlinie ist der Schutz der physischen Infrastruktur, die Informationen überträgt und verarbeitet — insbesondere Strom- und Datenkabel sowie die daran angeschlossenen Geräte. Verkabelung bildet das Nervensystem der Informationsverarbeitungsumgebung der Organisation. Ungeschützte Kabel sind anfällig für Abhörmassnahmen, elektromagnetische Störungen und physische Beschädigungen. Unsachgemäss gewartete Geräte verschlechtern sich, fallen aus und verursachen Sicherheitsschwachstellen. Diese Richtlinie legt Anforderungen für beides fest.

Controls A.7.12 (Kabelsicherheit) und A.7.13 (Gerätewartung) sind zusammengefasst, da sie sich mit ergänzenden Aspekten des Infrastrukturschutzes befassen: Verkabelung stellt die Konnektivitätsgrundlage bereit, und Wartung gewährleistet die laufende Zuverlässigkeit. Sie teilen gemeinsame Einrichtungen, Personal und Bewertungsprozesse.

Diese Richtlinie unterstützt das Schweizer nDSG (revDSG) Art. 8 durch die Implementierung technischer und organisatorischer Massnahmen entsprechend dem Risiko zum Schutz der Verfügbarkeit, Integrität und Vertraulichkeit personenbezogener Daten durch physische Infrastrukturcontrols. Wo die Organisation Daten von Personen im EU/EWR-Raum verarbeitet, gelten auch DSGVO Art. 32-Anforderungen für die Sicherheit der Verarbeitung einschliesslich physischer Massnahmen.

## Geltungsbereich

Alle Mitarbeitenden, Auftragnehmer und Drittanbieter-Wartungspersonal mit Zugang zur Kabelinfrastruktur oder zu wartungsbedürftigen Geräten.

Dies umfasst:

- **Verkabelung**: Stromkabel, Netzwerkkabel (Kupfer und Glasfaser), Telekommunikationskabel, strukturierte Verkabelungssysteme, Patchfelder, Verteilungsrahmen, Kabelkanäle, Leerrohre und Kabelwege.
- **Geräte**: Server, Netzwerkgeräte (Switches, Router, Firewalls), Speichersysteme, USV-Einheiten, PDUs, HVAC-Systeme für die Informationsverarbeitung, physische Sicherheitssysteme (Zugangskontrolle, CCTV) und Telekommunikationsgeräte.
- **Einrichtungen**: Rechenzentren, Serverräume, Verteilerräume, Telekommunikationsräume, Kabelschächte und unterirdische Kabelwege.
- **Aktivitäten**: Kabelinstallation, Kabelinspektion, Gerätewartung, vorbeugende Wartung, korrektive Wartung, Fernwartung und Geräteausbau für Reparaturen.

**Nicht im Geltungsbereich**:

- Physische Zugangskontrolle zu Infrastrukturbereichen (abgedeckt durch A.7.1–3).
- Umweltüberwachung und -schutzsysteme (abgedeckt durch A.7.4–5-11).
- Geräteentsorgung und sichere Vernichtung (abgedeckt durch A.7.14 und A.7.10).
- Vollständig vom Cloud-Anbieter gewartete Cloud-Infrastruktur (abgedeckt durch Lieferantenmanagement, A.5.19–23). Wo die Organisation ausschliesslich Cloud-basiert ohne lokale Geräte betrieben wird, können Controls A.7.12 und A.7.13 in der Anwendbarkeitserklärung mit dokumentierter Begründung als „Nicht anwendbar" gekennzeichnet werden.

## Grundsatz

Kabel, die Strom oder Daten übertragen, sollten vor Abhörung, Störungen und Beschädigungen geschützt werden. Geräte sollten korrekt gewartet werden, um die Verfügbarkeit, Integrität und Vertraulichkeit von Informationen sicherzustellen. Schutz- und Wartungsstufen müssen proportional zur Kritikalität der betreuten Assets sein, die durch Risikobewertung und die Asset-Klassifizierung der Organisation bestimmt wird.

---

## Kabelschutzstandards (A.7.12)

> *Kabel, die Strom, Daten oder unterstützende Informationsdienste übertragen, sollten vor Abhörung, Störungen und Beschädigungen geschützt werden.*

### Physischer Kabelschutz

Alle Strom-, Daten- oder informationsdiensttragende Kabel müssen physisch geschützt werden:

- Kabel müssen durch geschützte Wege geführt werden — Leerrohre, Kabelkanäle, Doppelböden oder Deckenhohlräume — nicht freiliegend über offene Bereiche.
- Unterirdische Verkabelung muss mit gepanzerten Leerrohren oder Kanalsystemen gegen unbeabsichtigte Beschädigungen geschützt werden. Streckenmarkierungen müssen vergrabene Kabelwege kennzeichnen.
- Kabel müssen vor Umweltgefahren einschliesslich Wassereintritt, Wärmequellen, chemischer Exposition und physischen Stössen geschützt werden. Kabelwege müssen Bereiche mit hohem Beschädigungsrisiko vermeiden.
- Wo Kabel zwischen Gebäuden verlaufen, muss ein geeigneter Schutz angewendet werden (gepanzertes Kabel, versiegelte Leitung oder direkt eingegrabenes Leerrohr).
- Verteilerräume, Telekommunikationsräume und Kabelverteilungsrahmen müssen physisch gesichert sein. Diese Bereiche müssen bei Nichtbesetzung abgesperrt und der Zugang auf autorisiertes Personal beschränkt sein.
- Schacht- und Leerrohrzugangspunkte müssen gesichert und der Zugang protokolliert sein.

### Elektromagnetischer Schutz

- Kabel müssen durch geeignete Abschirmung, Trennung von Störungsquellen und Auswahl des für die Umgebung geeigneten Kabeltyps vor elektromagnetischen Störungen (EMV) geschützt werden.
- In Umgebungen mit hohen elektromagnetischen Störungen (z.B. in der Nähe schwerer elektrischer Geräte, Industriemaschinen oder Funkübertragungsanlagen) müssen abgeschirmte Kabel (STP/FTP) oder Glasfaserkabel verwendet werden.
- Kabelinstallationen müssen den von der Organisation übernommenen strukturierten Verkabelungsstandard (IEC 11801 / EN 50173 / TIA-568 nach Bedarf) für Abschirmungs- und Trennungsanforderungen einhalten.

---

## Kabeltrennung

### Strom- und Datentrennung

Stromkabel und Kommunikationskabel müssen zur Vermeidung elektromagnetischer Störungen getrennt werden:

- Mindestabstände müssen dem von der Organisation übernommenen strukturierten Verkabelungsstandard folgen. Als Grundlage: mindestens 200 mm Abstand zwischen unabgeschirmten Datenkabeln und parallel verlaufenden Stromkabeln. Wo Kreuzungen unvermeidbar sind, müssen Kabel im rechten Winkel kreuzen.
- Strom- und Datenkabel müssen separate Leerrohre, Kabelkanäle oder Wege verwenden. Gemeinsame Wege für unabgeschirmte Datenkabel und Stromkabel sind nicht zulässig.
- Trennungsanforderungen müssen im Verkabelungsstandard der Organisation dokumentiert und konsistent in allen Installationen angewendet werden.

### Trennung nach Netzwerkklassifizierung

- Kabel, die Traffic unterschiedlicher Sicherheitsklassifizierungen übertragen, müssen wo möglich physisch getrennt oder durch Farbkodierung oder Beschriftung klar gekennzeichnet sein, um Fehlverbindungen zu verhindern.
- Hochsicherheits-Netzwerkkabel (z.B. Management-Netzwerke, Finanzsysteme, Sicherheitssysteme) müssen durch konsistente Farbkodierung oder die von der Organisation festgelegte Beschriftungskonvention identifizierbar sein.

---

## Kabeldokumentation und -beschriftung

### Dokumentationsanforderungen

Kabelinfrastruktur muss dokumentiert und gepflegt werden:

- Ein Kabelregister oder eine Kabelmanagement-Datenbank muss alle strukturierten Kabelinstallationen einschliesslich Kabeltyp, Endpunkte, Route, Installationsdatum und Klassifizierung erfassen.
- As-built-Verkabelungsdiagramme müssen für alle Einrichtungen gepflegt werden. Diagramme müssen Kabelwege, Patchfeld-Standorte, Verteilungsrahmen und Verbindungen zeigen.
- Kabeldokumentation muss aktuell gehalten werden. Alle Kabeländerungen müssen innerhalb von 5 Arbeitstagen nach Abschluss in der Dokumentation abgebildet werden.
- Kabeldokumentation muss gesichert und zugangskontrolliert sein. Nur autorisiertes Personal darf Zugang zu detaillierten Verkabelungsdiagrammen haben (diese offenbaren Netzwerktopologie und physische Wege).

### Beschriftungsstandards

- Alle Kabel müssen an beiden Enden mit einer eindeutigen Kennung beschriftet sein, die dem Kabelregister zugeordnet werden kann.
- Patchfelder, Verteilungsrahmen und Telekommunikationsdosen müssen klar beschriftet sein.
- Beschriftungen müssen dauerhaft, lesbar und in der Lage sein, für Routineoperationen ohne Bezugnahme auf detaillierte Dokumentation identifiziert zu werden.
- Die Organisation muss eine konsistente Beschriftungskonvention definieren und dokumentieren (z.B. Gebäude-Etage-Raum-Rack-Port).

### Kabeländerungskontrolle

Alle Kabelinstallationen, -änderungen und -entfernungen müssen dem Änderungsmanagementprozess der Organisation (A.8.32) mit folgenden spezifischen Anforderungen folgen:

#### Anforderungen an Änderungsanträge

Kabeländerungsanträge müssen enthalten:
- **Geschäftsbegründung**: Warum die Änderung benötigt wird
- **Umfang**: Betroffene spezifische Kabel, Wege und Abschlusspunkte
- **Serviceauswirkungsbewertung**: Mögliche Ausfallzeit, betroffene Systeme/Dienste
- **Implementierungsplan**: Schritt-für-Schritt-Verfahren einschliesslich Testplan
- **Rollback-Plan**: Wie der Dienst bei Implementierungsversagen wiederhergestellt wird
- **Dokumentationsaktualisierungen**: Welche Diagramme und Register aktualisiert werden

#### Genehmigungsanforderungen

| Änderungstyp | Erforderliche Genehmigung | Erforderliche Tests | Dokumentationsaktualisierungsfrist |
|--------------|--------------------------|--------------------|------------------------------------|
| **Neue Kabelinstallation** | IT-Betriebsleiter + Gebäudemanager | Kabeltests (Kontinuität, Leistung) nach IEC/TIA-Standards | 5 Arbeitstage |
| **Kabelentfernung** | IT-Betriebsleiter | Keine aktiven Verbindungen vor Entfernung verifizieren | 5 Arbeitstage |
| **Kabelwegänderung** | IT-Betriebsleiter + Gebäudemanager | Kabeltests nach Änderung | 5 Arbeitstage |
| **Glasfaserinstallation/-änderung** | ISB + IT-Betriebsleiter (Hochsicherheitsinfrastruktur) | Glasfasertests (Dämpfung, Kontinuität) | 5 Arbeitstage |
| **Notfallreparatur** | IT-Betriebsleiter (nachträgliche Genehmigung innerhalb von 24 Stunden) | Post-Reparatur-Tests obligatorisch | 2 Arbeitstage |

#### Tests und Validierung

Alle Kabeländerungen müssen Post-Implementierungstests umfassen:
- **Kupferkabel**: Kontinuität, Drahtbelegung, Länge, Dämpfung, Nahend-Übersprechen (NEXT), Rücklaufverlust nach TIA-568 Kategorie 6A-Anforderungen als Minimum
- **Glasfaserkabel**: Optischer Verlust, Kontinuität, Polarität nach TIA-568 oder Herstellerspezifikationen
- **Dokumentation der Testergebnisse**: Testberichte werden mit dem Änderungsnachweis aufbewahrt; fehlgeschlagene Tests erfordern Behebung vor Abnahme
- **Abnahmekriterien**: Müssen einschlägige Kabelstandard-Leistungsspezifikationen erfüllen oder übertreffen

#### Post-Implementierungsüberprüfung

Innerhalb von 30 Tagen nach Kabeländerungen, die >10 Verbindungen oder kritische Infrastruktur betreffen:
- Tatsächliche vs. geplante Serviceauswirkung überprüfen
- Testergebnisse und etwaige Abweichungen vom Plan überprüfen
- Kabelstandards oder -verfahren auf Basis der Erkenntnisse aktualisieren
- Überprüfungsergebnisse im Änderungsnachweis dokumentieren

- Ungenutzte Kabel müssen getrennt, dokumentiert und entweder entfernt oder klar als inaktiv gekennzeichnet sein.
- Vierteljährliche physische Rundgänge müssen durchgeführt werden, um nicht autorisierte Ergänzungen, Änderungen oder Beschädigungen zu identifizieren. Befunde müssen gegen As-built-Diagramme und Änderungsnachweise abgeglichen werden, wobei Ergebnisse dokumentiert und vom Gebäudemanager unterzeichnet werden.

---

## Glasfaseranforderungen

Glasfaserkabel sollte in folgenden Umständen gegenüber Kupfer für die Datenübertragung bevorzugt werden:

- **Hochsicherheitsbereiche**: Serverräume, Rechenzentren und Sicherheitszonen, wo das Abhörrisiko erhöht ist. Glasfaserkabel emittieren keine elektromagnetische Strahlung und sind erheblich schwieriger unbemerkt anzuzapfen als Kupferkabel.
- **Langstreckenläufe**: Zwischen Gebäuden, zwischen Etagen (Steigschächte) und alle horizontalen Läufe über 90 Meter (Kupfer Kategorie 6A Distanzlimit).
- **Hochbandbreitenanforderungen**: Wo Bandbreitenbedarf Kupferfähigkeiten übersteigt (z.B. 40 Gbps und darüber).
- **EMV-empfindliche Umgebungen**: Bereiche mit hohen elektromagnetischen Störungen, wo die Kupferleistung beeinträchtigt würde.

Wo Glasfaser eingesetzt wird, muss Verschweissung für permanente Verbindungen (nicht mechanische Spleissverbindungen) in Sicherheitsbereichen verwendet werden. Glasfaser-Patchfelder müssen in abschliessbaren Gehäusen untergebracht sein.

Wo Kupferkabel in Bereichen mit Abhörrisiko verwendet wird, muss abgeschirmtes Kabel (STP/FTP) spezifiziert und Kabelwege physisch gesichert sein.

---

## Inspektion und Kabelwartung

Regelmässige Inspektion und Wartung der Kabelinfrastruktur muss durchgeführt werden:

- Kabelinfrastruktur muss im Wartungsprogramm der Organisation mit festgelegten Inspektionsintervallen enthalten sein.
- Sichtinspektionen müssen vierteljährlich für zugängliche Kabelwege durchgeführt werden, wobei auf Beschädigungen, nicht autorisierte Änderungen, Beschriftungsintegrität und Wegversperrungen geprüft wird.
- Formale Kabeltests (Kontinuität, Leistung) müssen jährlich oder nach gemeldeten Problemen durchgeführt werden.
- Beschädigte Kabel müssen zeitnah repariert oder ersetzt werden. Temporäre Reparaturen müssen dokumentiert und eine dauerhafte Reparatur innerhalb von 30 Kalendertagen geplant sein.
- Inspektionsbefunde müssen dokumentiert und mindestens 3 Jahre aufbewahrt werden.

---

## Wartungsprogramm (A.7.13)

> *Geräte sollten korrekt gewartet werden, um die Verfügbarkeit, Integrität und Vertraulichkeit von Informationen sicherzustellen.*

### Programmaufbau

Die Organisation muss ein Wartungsprogramm aufbauen und aufrechterhalten, das alle Geräte abdeckt, die Informationen verarbeiten, speichern oder die Verarbeitung von Informationen unterstützen:

- Alle im Anwendungsbereich befindlichen, im Asset-Inventar erfassten Geräte (gemäss A.5.9) müssen im Wartungsprogramm enthalten sein. Das Asset-Inventar ist die massgebliche Quelle für die Programmvollständigkeit.
- Vierteljährliche Abgleiche müssen sicherstellen, dass alle inventarisierten Geräte Wartungsabdeckung haben. Abgleichergebnisse und Unterzeichnung müssen als Nachweis aufbewahrt werden.
- Wartungspläne müssen Herstellerempfehlungen als Mindestwerte folgen. Abweichungen erfordern dokumentierte Risikoakzeptanz über das Ausnahmeregister.
- Das Wartungsprogramm muss über das [CMMS] oder ein gleichwertiges Wartungsverfolgungssystem verwaltet werden. Wo kein dediziertes CMMS eingesetzt wird, ist eine kontrollierte Tabelle oder ein Register zu verwenden.

### Wartungsplan

Folgende Mindestfrequenzen für vorbeugende Wartung gelten:

| Gerätekategorie | Häufigkeit vorbeugender Wartung | Aktivitäten |
|-----------------|--------------------------------|-------------|
| **Server** | Jährlich | Firmware-Updates, Reinigung, physische Inspektion, Komponentenzustandsprüfungen |
| **Netzwerkgeräte** (Switches, Router, Firewalls) | Halbjährlich | Firmware-Updates, Lüfterreinigung, Port-Inspektion, Protokollüberprüfung |
| **USV-Systeme** | Vierteljährliche Batterieprüfungen; jährlicher Vollkapazitätstest | Batteriezustand, Belastungstests, Übertragungstests, Verbindungsintegrität |
| **PDUs** | Jährlich | Verbindungsinspektion, Lastausgleichsüberprüfung, Thermalbildgebung |
| **HVAC/Kühlung** (für IT-Bereiche) | Vierteljährlich | Filterwechsel, Kältemittelprüfungen, Leistungsverifizierung |
| **Brandmeldung und -löschung** | Gemäss kantonalen Brandvorschriften (mindestens jährlich) | Detektortests, Systeminspektion, Löschmittelverifizierung |
| **Physische Sicherheitssysteme** (Zugangskontrolle, CCTV) | Halbjährlich | Kamerazustand, Lesertests, Controller-Firmware, Aufzeichnungsverifizierung |
| **Strukturierte Verkabelung** | Jährlich (visuell vierteljährlich) | Kabeltests, Weginspektionen, Beschriftungsverifizierung |

Wartungspläne müssen basierend auf Gerätealter, Umgebungsbedingungen, Herstellerhinweisen und Vorfallshistorie angepasst werden. Geräte, die sich dem End-of-Life nähern, müssen häufigere Wartung erhalten oder zur Ersetzung eingeplant sein.

---

## Verfügbarkeit und Dienstkontinuität

Kabel- und Geräteinfrastruktur unterstützt direkt die Dienstverfügbarkeitsverpflichtungen der Organisation gegenüber Kunden. Wartungsaktivitäten müssen geplant und ausgeführt werden, um Serviceunterbrechungen zu minimieren.

### Serviceauswirkungsbewertung

Alle Wartungsaktivitäten müssen vor der Planung auf potenzielle Serviceauswirkungen bewertet werden:

| Auswirkungsstufe | Definition | Kundenbenachrichtigung | Erforderliche Genehmigung |
|------------------|-----------|----------------------|--------------------------|
| **Keine Auswirkung** | Redundantes System; keine Serviceunterbrechung | Keine | IT-Betriebsleiter |
| **Geringfügige Auswirkung** | Mögliche kurze Leistungsminderung (<5 Minuten) | Vorankündigung 48 Stunden | IT-Betriebsleiter |
| **Moderate Auswirkung** | Geplante Serviceunterbrechung (5–60 Minuten) | Vorankündigung 5 Arbeitstage | ISB + Geschäftseigentümer |
| **Grosse Auswirkung** | Erweiterte Ausfallzeit (>60 Minuten) oder kundenseitiger Service offline | Vorankündigung 10 Arbeitstage | Geschäftsleitung + Kundengenehmigung (bei vertraglicher Pflicht) |

### Wartungsfenster

- **Standard-Wartungsfenster**: [Definieren: z.B. „Sonntags 02:00–06:00 Uhr Ortszeit" oder „Erster Samstag des Monats 20:00 Uhr–Mitternacht"]
- Alle nicht notfallbedingten Wartungsarbeiten, die Services beeinflussen können, müssen während genehmigter Wartungsfenster geplant sein
- Notfallwartung ausserhalb der Wartungsfenster erfordert ISB-Genehmigung und sofortige Kundenbenachrichtigung (wo Auswirkung SLA-Schwellenwerte übersteigt)

### Auswirkung auf Verfügbarkeitsziele

Das Infrastruktur-Wartungsprogramm muss die Verfügbarkeitsverpflichtungen der Organisation unterstützen:

| Dienst | Verfügbarkeitsverpflichtung | Maximale zulässige Ausfallzeit pro Jahr | Infrastrukturbeitrag |
|--------|-----------------------------|-----------------------------------------|---------------------|
| [Primärer Dienst] | 99,5% Betriebszeit | 43,8 Stunden | Geplante Wartung: <24 Stunden jährlich; Ungeplante Ausfälle: <20 Stunden jährlich |
| [Sekundärer Dienst] | 99,0% Betriebszeit | 87,6 Stunden | Geplante Wartung: <40 Stunden jährlich; Ungeplante Ausfälle: <48 Stunden jährlich |

**Planungsbeschränkung für vorbeugende Wartung**: Gesamte geplante Ausfallzeit für Infrastrukturwartung darf 50% des jährlichen zulässigen Ausfallzeit-Budgets nicht überschreiten, um Kapazität für ungeplante Ausfälle zu reservieren.

### Redundanzanforderungen

Das Gerätewartungsprogramm muss das Redundanzdesign berücksichtigen:

- **Single Points of Failure**: Geräte ohne Redundanz müssen während Niedriglastzeiten mit Vorankündigung an Kunden gewartet werden
- **Redundante Systeme**: Wo N+1 oder 2N-Redundanz besteht, muss Wartung versetzt werden, um jederzeit mindestens N-Kapazität aufrechtzuerhalten
- **Kritische Pfad-Geräte** (USV, Netzwerkkern, primäre Server): Wartung muss Vorwartungsverifizierung des Redundanzstatus und Post-Wartungs-Failover-Tests umfassen

### Kapazität während der Wartung

Wenn redundante Geräte zur Wartung abgeschaltet werden, muss die verbleibende Kapazität für die aktuelle Last plus 20% Puffer als ausreichend verifiziert sein:
- Wenn Kapazität unter die Pufferschwelle fallen würde, muss Wartung umgeplant oder zusätzliche temporäre Kapazität bereitgestellt werden
- Belastungstests nach der Wartung müssen volle Redundanzwiederherstellung verifizieren, bevor Geräte als „in Betrieb" markiert werden

### Abhängigkeiten von Geschäftskontinuität und Disaster Recovery

Das Infrastruktur-Wartungsprogramm muss die Geschäftskontinuitätsplanung unterstützen:

#### Identifizierung kritischer Infrastruktur

Für Geschäftskontinuität kritische Geräte und Verkabelung müssen identifiziert und priorisiert werden:

| Klassifizierung | Definition | Wartungspriorität | Ersatzteile |
|-----------------|-----------|------------------|-------------|
| **Tier 1 — Missionskritisch** | Geräte, deren Ausfall sofortigen Serviceausfall ohne Umgehung verursacht | Höchste Priorität; vorbeugende Wartung nie verschoben | Kritische Ersatzteile vor Ort oder <4h-Verfügbarkeit |
| **Tier 2 — Geschäftskritisch** | Geräte, deren Ausfall Serviceminderung oder Beeinträchtigung einer Nutzergruppe verursacht | Hohe Priorität; Wartung kann mit ISB-Genehmigung max. 30 Tage verschoben werden | Ersatzteile innerhalb von 24 Stunden verfügbar |
| **Tier 3 — Wichtig** | Geräte, deren Ausfall Unannehmlichkeiten verursacht, Services aber betriebsfähig bleiben | Standardpriorität; Verschiebungen mit dokumentierter Begründung zulässig | Ersatzteile auf Bestellung |

#### Tests der Disaster-Recovery-Infrastruktur

- **Jährlicher DR-Failover-Test** muss Infrastrukturkomponenten umfassen:
  - Notstromsysteme (USV, Generator falls vorhanden)
  - Redundante Netzwerkwege
  - Backup-Kühlsysteme
  - Kritische Kabelwege (verifizieren, dass dokumentierte Alternativwege bestehen)
- DR-Test muss verifizieren, dass das Wartungsprogramm die Infrastruktur in DR-bereitem Zustand gehalten hat
- DR-Testbefunde, die Infrastrukturlücken aufzeigen, müssen Wartungsprogrammaktualisierungen auslösen

#### Alternativer Standort-Infrastruktur

Falls die Organisation einen Disaster-Recovery-Standort unterhält:
- Alle Wartungsprogrammanforderungen gelten für DR-Standort-Geräte
- DR-Standort-Kabelinfrastruktur nach gleichen Standards wie Primärstandort dokumentiert
- Synchronisation der Wartungsaktivitäten (wenn primäre USV-Batterien ersetzt werden, DR-Standort-Batterien bewertet und bei Bedarf ersetzt)
- DR-Standort-Gerätewartung kann bei kontrollierter Umgebung und leicht genutzten Geräten mit niedrigerer Häufigkeit erfolgen (mit dokumentierter Begründung)

---

## Autorisierung von Wartungspersonal

### Internes Personal

- Nur Personal mit dokumentierter Autorisierung darf Wartungsarbeiten an informationsverarbeitenden Geräten durchführen.
- Wartungsautorisierung muss angeben, für welche Gerätekategorien und welche Wartungsaktivitäten die Person qualifiziert ist.
- Autorisierungsnachweise müssen gepflegt und jährlich überprüft werden.

### Drittanbieter-Wartungspersonal

- Drittanbieter-Wartung darf nur durch vertraglich gebundene und genehmigte Anbieter durchgeführt werden. Wartungsverträge müssen Vertraulichkeitsverpflichtungen und Sicherheitsanforderungen enthalten.
- Drittanbieter-Wartungspersonal muss identifiziert und verifiziert (amtlicher Ausweis) werden, bevor es Zugang zu Geräten erhält.
- Die Organisation muss ein Register genehmigter Drittanbieter-Wartungsdienstleister führen, das jährlich überprüft wird.

### Aufsichtsanforderungen

- Drittanbieter-Wartungspersonal muss beaufsichtigt werden, wenn es auf Geräte zugreift, die sensible oder vertrauliche Informationen verarbeiten oder speichern, es sei denn, eine dokumentierte Risikobewertung kommt zum Schluss, dass unbeaufsichtigter Zugang akzeptabel ist (z.B. dedizierter Wartungsvertrag mit sicherheitsüberprüftem Personal, isolierte Geräte).
- Unbeaufsichtigter Drittanbieter-Wartungszugang muss mit individueller Identifikation, Ein-/Ausgangszeit und aufgerufenem Gerät protokolliert werden.
- Aufsichtsnachweise müssen aufbewahrt werden.

---

## Management von Drittanbieter-Wartungsdienstleistern

### Vertragsanforderungen

Wartungsverträge mit Drittanbietern müssen enthalten:

| Vertragselement | Anforderung |
|-----------------|-------------|
| **Service Level Agreement (SLA)** | Reaktionszeit (Ankunft vor Ort); Lösungszeit; Eskalationsverfahren |
| **Abdeckungszeiten** | 24x7 für kritische Geräte; Geschäftszeiten für unkritische Geräte |
| **Ersatzteilverfügbarkeit** | Kritische Ersatzteile vor Ort oder <4-Stunden-Lieferverpflichtung |
| **Sicherheitsanforderungen** | Hintergrundüberprüfungen für Personal; Vertraulichkeitsverpflichtungen; Aufsichtsannahme |
| **Datenschutz** | Datenhandhabungsverfahren; sichere Löschfähigkeiten; Datenpannen-Meldepflichten |
| **Berichterstattung** | Monatliche Serviceberichte; jährliche Leistungsüberprüfungsgespräche |
| **Versicherung** | Berufshaftpflicht; Cyberhaftpflicht (für Fernzugriffsanbieter) |
| **Kündigungsrechte** | Kündigung bei Sicherheitsverletzung; Übergangshilfe-Verpflichtungen |

### Lieferantenleistungsüberwachung

Wartungsanbieter-Leistung muss verfolgt und überprüft werden:

| Kennzahl | Ziel | Überprüfungshäufigkeit |
|----------|------|------------------------|
| **SLA-Compliance (Reaktionszeit)** | >95% | Vierteljährlich |
| **SLA-Compliance (Lösungszeit)** | >90% | Vierteljährlich |
| **Wartungsqualität** | <5% Wiederholungsausfälle innerhalb von 30 Tagen | Vierteljährlich |
| **Sicherheitsvorfallrate** | 0 | Pro Ereignis |
| **Kundenzufriedenheit** (interne Nutzer) | >4/5 Bewertung | Pro Serviceereignis |
| **Dokumentations-Compliance** | 100% der Serviceberichte pünktlich erhalten | Vierteljährlich |

### Jährliche Anbieterbewertung

Jeder Wartungsanbieter erhält eine jährliche Überprüfung, die Folgendes abdeckt:
- SLA-Leistung gegen Ziele
- Sicherheits-Compliance (Einhaltung der Aufsichtsregeln, vorfallfreier Nachweis)
- Kosteneffizienz im Vergleich zu Alternativen
- Reaktionsfähigkeit und Kommunikationsqualität
- Empfehlung: Fortsetzen, neu verhandeln oder ersetzen

**Überprüfungsdokumentation**: 3 Jahre aufbewahrt; Erneuerungs-/Ersatzbeschlüsse mit Begründung dokumentiert.

### Lieferantensicherheitsvorfälle

Falls ein Wartungsanbieter einen Sicherheitsvorfall verursacht oder dazu beiträgt:
1. **Sofortmassnahme**: Anbieterzugang bis zum Abschluss der Untersuchung aussetzen
2. **Untersuchung**: Ursachenanalyse; Feststellung, ob Vertragsbruch vorliegt
3. **Korrekturmassnahme**: Vom Anbieter vorgelegter Behebungsplan; verstärkte Aufsicht bei Wiederherstellung des Zugangs
4. **Vertragsüberprüfung**: Bewertung, ob Kündigung gerechtfertigt ist; Entscheidung dokumentieren
5. **Erkenntnisse**: Verfahren für Lieferantenmanagement oder Vertragsanforderungen aktualisieren

---

## Sicherheit während der Wartung

### Datenschutz während der Wartung

- Sensible Daten müssen während aller Wartungsaktivitäten geschützt werden. Wartungspersonal darf keinen Zugang zu auf Geräten gespeicherten Daten haben, es sei denn, dies ist ausdrücklich erforderlich und autorisiert.
- Daten enthaltende Geräte dürfen für Wartungszwecke nicht vom Gelände entfernt werden, wenn eine Reparatur vor Ort möglich ist.
- Falls externe Wartung erforderlich ist, müssen Daten vor der Entfernung sicher vom Gerät gelöscht werden (gemäss A.7.14 Sicherheits-Entsorgungsverfahren), oder der Speicher muss entfernt und von der Organisation zurückbehalten werden.
- Bei Geräten, bei denen eine Datenlöschung vor der Entfernung nicht möglich ist (z.B. Fehler verhindert Zugang), muss eine dokumentierte Risikobewertung abgeschlossen und die Datenhandhabungsverpflichtungen des Wartungsanbieters schriftlich bestätigt werden.

### Physische Verifizierung nach der Wartung

- Nach der Wartung müssen Geräte vor der Rückgabe in Betrieb physisch inspiziert werden, um zu verifizieren, dass keine nicht autorisierten Änderungen vorgenommen wurden.
- Alle von Wartungspersonal mitgebrachten Werkzeuge und Geräte müssen vor und nach der Wartung erfasst sein.
- Firmware- und Softwareversionen müssen nach der Wartung verifiziert werden, um nicht autorisierte Änderungen zu bestätigen.

### Wartungszugangskontrolle

- Wartungszugang muss zeitlich begrenzt sein. Zugangsfenster müssen im Voraus vereinbart und dokumentiert sein.
- Jeder Wartungszugang muss protokolliert werden: wer die Arbeit ausgeführt hat, wann, auf welche Geräte zugegriffen wurde und welche Arbeit durchgeführt wurde.
- Wartungspersonal muss temporäre Zugangsdaten (Ausweise, Systemzugang) erhalten, die am Ende des Wartungsfensters ablaufen.

---

## Fernwartung

Fernwartung birgt zusätzliche Risiken. Folgende Controls müssen gelten:

- Fernwartung muss vor jeder Sitzung ausdrücklich autorisiert werden. Dauerhafte Autorisierung für Fernzugang ist nicht zulässig.
- Fernwartungssitzungen müssen verschlüsselte Verbindungen verwenden (VPN, SSH oder gleichwertige sichere Protokolle). Unverschlüsselter Fernzugang ist nicht zulässig.
- Fernwartungssitzungen müssen protokolliert werden, einschliesslich Sitzungsstartzeit/-endzeit, individueller Identität und durchgeführter Aktionen. Sitzungsaufzeichnung wird für kritische Geräte empfohlen.
- Fernzugang muss deaktiviert werden, wenn er nicht aktiv verwendet wird. Persistente Fernzugangsverbindungen für Wartungszwecke dürfen nicht offen bleiben.
- Fernwartung von Geräten mit sensiblen Daten erfordert dieselbe Autorisierung wie physischer Zugang zu diesen Geräten.
- Wo der Wartungsanbieter Fernzugang zu internen Systemen benötigt, muss ein dedizierter Jump-Host oder Bastion-Server mit Multi-Faktor-Authentifizierung verwendet werden.

---

## Geräteentfernung und -rückgabe

Wenn Geräte für externe Wartung vom Gelände entfernt werden müssen:

1. **Autorisierung**: Entfernung muss schriftlich vom Geräteeigentümer oder designierten Stellvertreter autorisiert werden.
2. **Datenschutz**: Daten müssen vor der Entfernung sicher gelöscht werden. Falls Löschung nicht möglich ist, muss der Speicher entfernt und von der Organisation zurückbehalten werden. Der Datenschutzansatz muss dokumentiert sein.
3. **Beweiskette**: Ein Beweisketten-Nachweis muss erstellt werden mit: Gerätekennung, Zustand bei Entfernung, Entfernungsdatum/-uhrzeit, autorisiert durch, Transporteur, Ziel, voraussichtliches Rückgabedatum.
4. **Geräteinspektionsbei Rückgabe**: Bei Rückgabe muss das Gerät auf Manipulation, nicht autorisierte Änderungen und korrekte Konfiguration inspiziert werden. Firmware- und Softwareversionen müssen verifiziert werden.
5. **Asset-Register-Aktualisierung**: Geräteerückgabe muss im [Asset-Management-System] mit Wartungszusammenfassung und Inspektionsergebnissen protokolliert werden.

---

## Incident-Response bei Infrastrukturausfällen

Infrastrukturausfälle (Kabelschäden, Gerätedefekte), die Services beeinflussen oder beeinflussen könnten, müssen über den Incident-Management-Prozess der Organisation behandelt werden.

### Incident-Klassifizierung für Infrastrukturereignisse

| Schweregrad | Definition | Beispiele | Reaktionszeit | Benachrichtigung |
|-------------|-----------|-----------|---------------|-----------------|
| **P1 — Kritisch** | Vollständiger Serviceausfall oder unmittelbares Risiko | Primärer Stromausfall, Core-Network-Switch-Ausfall, vollständiger Kabelschnitt | Sofortige Reaktion; 1-Stunden-Wiederherstellungsziel | ISB, Geschäftsleitung, betroffene Kunden sofort |
| **P2 — Hoch** | Erhebliche Serviceminderung; Redundanz verloren | USV-Ausfall (Netzstrom betriebsfähig), Backup-Leitungsausfall, partieller Kabelschaden | 2-Stunden-Reaktion; 4-Stunden-Wiederherstellungsziel | IT-Betriebsleiter, ISB, Kundenbenachrichtigung bei SLA-Auswirkung |
| **P3 — Mittel** | Geringfügige Minderung; Redundanz intakt | Einzelner Server-Ausfall (geclustert), Kühlgerät-Ausfall (Backup betriebsfähig) | 4-Stunden-Reaktion; 24-Stunden-Wiederherstellungsziel | IT-Betriebsleiter |
| **P4 — Niedrig** | Keine aktuelle Serviceauswirkung; Überwachungsalarme | Alternde USV-Batterie, Gerät läuft heiss aber innerhalb der Toleranzen | Reaktion nächster Arbeitstag; geplante Wartung | IT-Betrieb |

### Incident-Response-Workflow für Infrastruktur

1. **Erkennung und Protokollierung**
   - Infrastrukturüberwachungsalarme oder Nutzerberichte lösen Incident-Erstellung aus
   - Incident-Ticket erstellt im [Incident-Management-System] mit Schweregradklassifizierung
   - Erstbewertung: Auswirkungsumfang, betroffene Services, betroffene Kunden

2. **Eskalation**
   - P1: Sofortige Eskalation zu ISB und IT-Betriebsleiter
   - P2: Eskalation zum IT-Betriebsleiter innerhalb von 30 Minuten
   - P3/P4: Zugewiesen an diensthabenden Ingenieur

3. **Kommunikation**
   - **Intern**: Incident-Statusupdates alle 2 Stunden (P1), alle 4 Stunden (P2) bis zur Lösung
   - **Kunden**: Benachrichtigung gemäss Serviceauswirkungsbewertungstabelle oben; Statusupdates gemäss SLA-Bedingungen
   - **Anbieter**: Wartungsanbieter gemäss Vertragseskalationsverfahren einbeziehen

4. **Untersuchung und Behebung**
   - Ursachenanalyse obligatorisch für alle P1/P2-Incidents
   - Temporäre Umgehungen dokumentiert mit geplanter dauerhafter Lösung
   - Geräteausfälle: Wartungshistorie, Garantiestatus, Ersatzanforderungen bestimmen

5. **Post-Incident-Überprüfung**
   - P1/P2-Incidents: Post-Incident-Überprüfung innerhalb von 5 Arbeitstagen
   - Erkenntnisse: Präventivmassnahmen, Wartungsprogrammverbesserungen identifizieren
   - Dokumentation: Wartungsverfahren, Kabelstandards oder Überwachungsschwellen basierend auf Befunden aktualisieren

### Nachweis-Erfassung bei Infrastruktur-Incidents

Infrastruktur-Incidents müssen dokumentieren:
- Ereignis-Zeitlinie (Erkennung, Eskalation, ergriffene Massnahmen, Lösung)
- Auswirkungsbewertung (betroffene Services, Kundenauswirkung, Ausfallzeit)
- Ursachenanalyse (Gerätealter, Wartungshistorie, Umweltfaktoren)
- Lösungsmassnahmen (Reparaturen, Ersatz, Konfigurationsänderungen)
- Präventivmassnahmen (Wartungsplananpassungen, Überwachungsverbesserungen)

Post-Incident-Überprüfungsdokumentation mindestens 3 Jahre aufbewahrt.

---

## Wartungsnachweise

### Dokumentationsanforderungen

Alle Wartungen — vorbeugend und korrektiv — müssen dokumentiert werden:

- **Vorbeugende Wartung**: Datum, Gerätekennung, durchgeführte Wartungsaktivitäten, Befunde, ersetzte Teile, nächstes geplantes Wartungsdatum, das die Arbeit ausführende Personal.
- **Korrektive Wartung**: Datum, Gerätekennung, Fehlerbeschreibung, Ursache (wenn bestimmt), ergriffene Reparaturmassnahmen, ersetzte Teile, Post-Reparatur-Verifizierungsergebnisse, das die Arbeit ausführende Personal.
- **Fernwartung**: Sitzungsdatum/-uhrzeit, aufgerufene Geräte, individuelle Identität, durchgeführte Aktionen, Sitzungsdauer.

### Nachweisaufbewahrung

- Wartungsnachweise müssen mindestens 3 Jahre oder den Lebenszyklus des Geräts aufbewahrt werden, je nachdem was länger ist.
- Nachweise müssen jederzeit für Audits verfügbar sein.
- Nachweise müssen im [CMMS] oder einem gleichwertigen kontrollierten Register gespeichert sein.

### Wartungstrendanalyse

- Wartungsnachweise müssen vierteljährlich auf Trends überprüft werden: wiederkehrende Fehler, Geräte, die sich dem End-of-Life nähern, zunehmende Ausfallhäufigkeit oder Wartungs-SLA-Verletzungen.
- Trendanalyse muss Geräteersatzplanung und Wartungsprogrammanpassungen informieren.
- Vierteljährliche Trendberichte müssen dem IT-Betriebsleiter und ISB vorgelegt werden.

---

## Infrastrukturleistungsüberwachung

Über Wartungsabschluss-Kennzahlen hinaus muss die Organisation Infrastrukturgesundheitsindikatoren überwachen, um prädiktive Wartung zu ermöglichen und die Effektivität der Verfügbarkeit nachzuweisen.

### Gerätegesundheitsüberwachung

| Kennzahl | Überwachungsmethode | Alarmschwelle | Überprüfungshäufigkeit |
|----------|--------------------|--------------|-----------------------|
| **USV-Batteriegesundheit** | Impedanztests der Batterie | >20% Verschlechterung vom Ausgangswert | Monatliche Trendanalyse |
| **USV-Laufzeitkapazität** | Jährliche Last-Tests | <90% der Nennlaufzeit | Jährlich mit Trend |
| **Gerätetemperatur** | Umweltüberwachungssystem | >80% der maximalen Betriebstemperatur | Kontinuierliche Alarmierung |
| **Netzwerkgerätefehler** | SNMP-Überwachung / Syslog | >0,1% Schnittstellenfehlerrate | Tägliche Überprüfung |
| **Server-Hardware-Gesundheit** | Management-Interface-Überwachung (iDRAC, iLO) | Prädiktive Fehlermeldungen | Kontinuierliche Alarmierung |
| **HVAC-Leistung** | Temperatur-/Feuchtigkeitssensoren | Temp. >24°C oder <18°C; rel. Luftfeuchtigkeit >60% oder <40% | Kontinuierliche Alarmierung |
| **Stromverbrauchstrends** | PDU-Überwachung | >80% der Nennkapazität | Monatlicher Trend |
| **Kabelinfrastrukturprobleme** | Helpdesk-Tickets, Rundgangbefunde | Jegliche Beschädigungen, nicht autorisierte Änderungen | Vierteljährliche Überprüfung |

### Auslöser für prädiktive Wartung

Gesundheitsüberwachung muss frühzeitige Wartungsmassnahmen vor Ausfall auslösen:

| Indikator | Auslöseschwelle | Massnahme |
|-----------|----------------|-----------|
| USV-Batterieverschlechterung | 15–20% Kapazitätsverlust | Batterieersatz innerhalb von 30 Tagen planen |
| Gerättemperatur steigt | 3-Monats-Durchschnittszunahme >5°C | Kühlung untersuchen, Tiefenreinigung planen |
| Netzwerkschnittstellenfehler steigen | 3-Monats-Trend zeigt Verdoppelung der Fehler | Kabeltests, Schnittstelleninspektion planen |
| Prädiktiver Hardwarefehleralarm | SMART-Fehler, Speicher-ECC-Fehler | Ersatz vor Ausfall planen; Backup-Verifizierung |

### Verfügbarkeitskennzahlen-Dashboard

Monatliche Berichterstattung an IT-Betriebsleiter und ISB:

| Kennzahl | Ziel | Berechnung |
|----------|------|------------|
| **Ungeplante Infrastrukturausfallzeit** | <20 Stunden jährlich | Summe aller P1/P2-Incident-Dauern |
| **Geplante Wartungsausfallzeit** | <24 Stunden jährlich | Summe aller Wartungsfenster-Dauern mit Serviceauswirkung |
| **Infrastrukturverfügbarkeit** | >99,5% | (Gesamtstunden - Ausfallstunden) / Gesamtstunden x 100% |
| **Mean Time Between Failures (MTBF)** | Steigender Trend | Verfolgung nach Gerätekategorie |
| **Mean Time To Repair (MTTR)** | <4 Stunden (P1/P2) | Durchschnittszeit von Erkennung bis Lösung |
| **Vorbeugende Wartungs-Compliance** | 100% | Abgeschlossen pünktlich / Gesamtgeplant x 100% |
| **Geräte nach End-of-Life** | 0 kritische Geräte | Anzahl kritischer Geräte, die das Hersteller-EOL-Datum überschreiten |

**Vierteljährliche Trendanalyse**: Kennzahlen auf sich verschlechternde Trends überprüfen; Wartungsprogramm anpassen oder Geräteersatz einplanen.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Strukturierte Verkabelung** | Eine standardisierte Kabelinfrastruktur (Kupfer und Glasfaser) nach Industriestandards (IEC 11801, EN 50173, TIA-568), die einen flexiblen, zuverlässigen Rahmen für Sprach-, Daten- und Videokommunikation bietet |
| **Kabelinfrastruktur** | Alle Strom- und Kommunikationskabel, Leerrohre, Wege, Patchfelder, Verteilungsrahmen und Abschlusspunkte |
| **Glasfaserkabel** | Ein Kabel mit einer oder mehreren optischen Fasern, das Daten als Lichtimpulse überträgt, mit höherer Bandbreite, grösserer Distanz, EMV-Immunität und grösserem Widerstand gegen Abhörmassnahmen als Kupferkabel |
| **Vorbeugende Wartung** | Geplante Wartung in festgelegten Intervallen zur Vermeidung von Geräteausfällen und Aufrechterhaltung der Leistung innerhalb der Spezifikationen |
| **Korrektive Wartung** | Ungeplante Wartung zur Wiederherstellung des Betriebszustands von Geräten nach einem Fehler oder Ausfall |
| **Fernwartung** | Wartung über Fernzugriff auf das Netzwerk ohne physische Präsenz am Gerätestandort |
| **Beweiskette** | Ein dokumentierter chronologischer Nachweis des Verantwortungsübergangs für Geräte, der den Besitz von der Entfernung über die Wartung bis zur Rückgabe verfolgt |
| **CMMS** | Computerized Maintenance Management System — Software zur Planung, Verfolgung und Dokumentation von Wartungsaktivitäten |
| **EMV** | Elektromagnetische Verträglichkeit — unerwünschtes elektrisches Rauschen aus externen Quellen, das die Signalqualität in Datenkabeln beeinträchtigen kann |

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten für Kabel und Wartung |
|-------|-------------------------------------------|
| **Geschäftsleitung** | Richtlinie genehmigen; Budget für Infrastrukturwartung und Kabelanlage-Upgrades bereitstellen |
| **ISB** | Richtlinieneigentümerschaft; Sicherheitsstandards für Wartungsaktivitäten; Risikoakzeptanz für Ausnahmen; vierteljährliche Berichterstattung über Infrastruktur-Compliance |
| **IT-Betriebsleiter** | Gerätewartungsprogramm-Eigentümerschaft; Management von Wartungsanbietern; Wartungsplanoversicht; Trendanalyse-Überprüfung |
| **Gebäudemanager** | Kabelinfrastruktur-Eigentümerschaft; Kabelanlage-Wartung und -inspektion; Koordination mit Gebäudediensten; physisches Wegemanagement |
| **Systemeigentümer** | Sicherstellen, dass eigene Geräte im Wartungsprogramm enthalten sind; Geräteentfernung autorisieren; Datenschutzanforderungen für Wartung definieren |
| **IT-Betrieb** | Tägliche Wartungsausführung und -koordination; Wartungsprotokollführung; Fernwartungssitzungsmanagement |
| **Interne Revision** | Jährliche Verifizierung der Wartungsprogramm-Compliance; Kabelinfrastruktur-Audit; Nachweisüberprüfung |
| **Alle Mitarbeitenden** | Vermutete Kabelschäden, Gerätedefekte oder nicht autorisierte Infrastrukturänderungen sofort melden |

### Eskalationspfad

- Entdeckte Kabelschäden oder nicht autorisierte Änderungen: Meldende Person benachrichtigt Gebäudemanager. Gebäudemanager bewertet Auswirkung und benachrichtigt ISB bei sicherheitsrelevanten Befunden.
- Gerätewartungsausfälle: IT-Betrieb benachrichtigt IT-Betriebsleiter. Kritische Geräteausfälle werden zum ISB eskaliert.
- Sicherheitsbedenken während der Wartung: Jedes Mitarbeitende benachrichtigt direkt den ISB.

---

## Nachweise

Die folgenden Nachweise belegen die Compliance mit dieser Richtlinie. **Für SOC-2-Typ-II-Audits** prüfen Auditoren die Betriebswirksamkeit über den Prüfzeitraum (typischerweise 12 Monate).

| # | Nachweis | Eigentümer | Häufigkeit | Audit-Trail-Anforderungen |
|---|----------|------------|------------|--------------------------|
| 1 | **Kabelregister / Kabelmanagement-Datenbank** mit Dokumentation aller strukturierten Kabelinstallationen mit Typ, Endpunkten, Route und Klassifizierung | Gebäudemanager | *Kontinuierlich gepflegt; jährlich überprüft* | Aktuelles Register mit Versionshistorie der Aktualisierungen |
| 2 | **As-built-Verkabelungsdiagramme** für alle Einrichtungen, aktuell und versionskontrolliert | Gebäudemanager | *Innerhalb von 5 Arbeitstagen nach Änderungen aktualisiert; jährlich überprüft* | Diagrammversionen mit Änderungsnachweisen korreliert |
| 3 | **Vierteljährliche Kabel-Rundgangberichte** mit Befunden, Abgleich gegen Diagramme und Unterzeichnung | Gebäudemanager | *Vierteljährlich; 3 Jahre aufbewahrt* | Unterzeichneter Rundgangbericht mit Befunden und Behebungsmassnahmen |
| 4 | **Kabeltestnachweise** (Kontinuität, Leistung) für neue Installationen und jährliche Verifizierung | Gebäudemanager | *Jährlich und pro Installation; 3 Jahre aufbewahrt* | Testberichte mit Bestanden/Nicht-bestanden-Ergebnissen nach Kabelstandard |
| 5 | **Wartungsprogramm** mit allen im Geltungsbereich befindlichen Geräten und Plänen nach Herstellerempfehlungen | IT-Betriebsleiter | *Vierteljährlich überprüft; 3 Jahre aufbewahrt* | Programmdokument mit vierteljährlicher Überprüfungsunterzeichnung |
| 6 | **Vierteljährlicher Abgleich** von Asset-Inventar gegen Wartungsprogramm-Abdeckung | IT-Betriebsleiter | *Vierteljährlich; 3 Jahre aufbewahrt* | Abgleichbericht mit Abdeckungsprozentsatz und Lückenbeseitigung |
| 7 | **Vorbeugende Wartungsnachweise** mit abgeschlossener Wartung, Befunden und nächstem geplanten Datum | IT-Betrieb | *Pro Wartungsereignis; mindestens 3 Jahre aufbewahrt* | Individuelle Wartungsnachweise mit Abschluss-Zeitstempeln |
| 8 | **Korrektive Wartungsnachweise** mit Fehlern, Ursache, Reparaturmassnahmen und Post-Reparatur-Verifizierung | IT-Betrieb | *Pro Ereignis; mindestens 3 Jahre aufbewahrt* | Incident-verknüpfte Wartungsnachweise mit Ursachenanalyse |
| 9 | **Wartungspersonal-Autorisierungsnachweise** (intern und Drittanbieter) | IT-Betriebsleiter | *Jährlich überprüft; 3 Jahre aufbewahrt* | Autorisierungsregister mit jährlicher Überprüfungsunterzeichnung |
| 10 | **Drittanbieter-Wartungsdienstleister-Register** mit Vertragsdetails und jährlicher Überprüfung | IT-Betriebsleiter | *Jährlich überprüft; aktiv + 2 Jahre aufbewahrt* | Anbieterregister mit Vertragszusammenfassungen und Überprüfungsdaten |
| 11 | **Fernwartungssitzungsprotokolle** mit individueller Identifikation, Zeiten und Aktionen | IT-Betrieb | *Pro Sitzung; 3 Jahre aufbewahrt* | Sitzungsprotokolle mit Autorisierungsnachweisen |
| 12 | **Geräteentfernungs- und -rückgabenachweise** mit Beweiskette, Datenschutznachweis und Rückgabeinspektion | IT-Betrieb | *Pro Ereignis; 3 Jahre aufbewahrt* | Beweiskettenformulare mit Inspektionsunterzeichnung |
| 13 | **Wartungstrendanalyse-Berichte** mit wiederkehrenden Problemen und Gerätezyklusempfehlungen | IT-Betriebsleiter | *Vierteljährlich; 3 Jahre aufbewahrt* | Trendbericht mit umsetzbaren Empfehlungen und Management-Reaktion |
| 14 | **Ausnahmeregister** für genehmigte Abweichungen von Wartungsplänen oder Kabelstandards | ISB | *Pro Ereignis; vierteljährlich überprüft; aktiv + 2 Jahre aufbewahrt* | Ausnahmenachweise mit Risikobewertung und Ausgleichsmassnahmen |
| 15 | **Serviceauswirkungsbewertungen** für Wartungsaktivitäten | IT-Betrieb | *Pro Wartungsereignis mit Serviceauswirkung* | Änderungsantrag mit Auswirkungsbewertung, Genehmigung, Kundenbenachrichtigung (falls zutreffend) |
| 16 | **Wartungsfenster-Nutzungsbericht** | IT-Betriebsleiter | *Vierteljährlich* | Zusammenfassung: geplante Ausfallzeit vs. Verfügbarkeitsbudget, SLA-Compliance, gesendete Kundenbenachrichtigungen |
| 17 | **Infrastrukturverfügbarkeitskennzahlen** | IT-Betriebsleiter | *Monatlich; vierteljährlich aggregiert* | Dashboard mit Betriebszeit %, ungeplanter Ausfallzeit, MTBF, MTTR nach Gerätekategorie |
| 18 | **Infrastruktur-Incident-Nachweise** (P1/P2) | IT-Betrieb | *Pro Incident* | Incident-Ticket mit: Zeitlinie, Ursachenanalyse, Kundenauswirkung, Lösung, Post-Incident-Überprüfung |
| 19 | **Gerätegesundheitsüberwachungsberichte** | IT-Betrieb | *Monatlich* | USV-Batteriegesundheitstrends, Temperaturüberwachung, Fehlerrattrends, prädiktive Fehlermeldungen |
| 20 | **Anbieterleistungs-Scorecards** | IT-Betriebsleiter | *Vierteljährlich pro Anbieter* | SLA-Compliance-Daten, Qualitätskennzahlen, Sicherheitsvorfallverfolgung, Kundenzufriedenheit |
| 21 | **Jährliche Anbieterbewertungen** | IT-Betriebsleiter | *Jährlich pro Anbieter* | Überprüfungsdokument mit Leistungsbewertung, Erneuerungs-/Ersatzempfehlung, Genehmigungsunterschrift |
| 22 | **DR-Infrastrukturtest-Ergebnisse** | IT-Betriebsleiter | *Jährlich (oder pro DR-Test)* | DR-Testbericht über Infrastruktur-Failover-Tests, Befunde, Korrekturmassnahmen |
| 23 | **Kabeländerungsmanagement-Nachweise** | Gebäudemanager | *Pro Kabeländerung* | Änderungsantrag, Genehmigung, Testergebnisse, As-built-Diagrammaktualisierungen, Abschlussunterzeichnung |

### SOC-2-Typ-II-Testerwartungen

Auditoren entnehmen typischerweise Stichproben von:
- **25 vorbeugenden Wartungsereignissen** über den Prüfzeitraum (verifizieren: geplant, pünktlich abgeschlossen, dokumentiert)
- **Allen P1/P2-Infrastruktur-Incidents** (verifizieren: Klassifizierung, Eskalation, Kundenbenachrichtigung, Post-Incident-Überprüfung)
- **Allen Anbieterleistungsüberprüfungen** (verifizieren: abgeschlossen, Kennzahlen verfolgt, Entscheidungen dokumentiert)
- **Allen Kabelinfrastrukturänderungen** (verifizieren: Änderungsgenehmigung, Tests, Dokumentationsaktualisierungen)
- **Vierteljährlichen Abgleichen** (Asset-Inventar vs. Wartungsprogramm-Abdeckung)
- **Monatlichen Verfügbarkeitskennzahlen** (Genauigkeit verifizieren, Trendanalyse, Eskalation von Problemen)

**Vollständigkeit ist kritisch**: Fehlende Nachweise für jeden Punkt der Stichprobe = Audit-Befund.

---

# Richtlinien-Compliance

## Compliance-Messung

Das Informationssicherheits-Managementteam überprüft die Compliance mit dieser Richtlinie durch verschiedene Methoden, darunter Kabelinfrastruktur-Audits, Wartungsprogramm-Überprüfungen, Wartungsnachweis-Audits, physische Inspektionen, Anbieter-Compliance-Bewertungen, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

Die folgenden Kennzahlen sind zu verfolgen und dem ISB vierteljährlich zu berichten:

| Kennzahl | Ziel | Rotschwelle |
|----------|------|-------------|
| Planmässig abgeschlossene vorbeugende Wartungen | 100% | < 85% |
| Auf versäumte oder unzureichende Wartung zurückzuführende Geräteausfälle | 0 | Jedes Vorkommnis |
| Kabeldokumentationsgenauigkeit (Rundgangbefunde vs. Diagramme) | > 95% | < 85% |
| Entdeckte nicht autorisierte Kabeländerungen | 0 | Jedes Vorkommnis |
| Wartungsbedingte Sicherheitsvorfälle | 0 | Jedes Vorkommnis |
| Asset-Inventar-zu-Wartungsprogramm-Abgleich | 100% Abdeckung | < 90% Abdeckung |
| Drittanbieter-Wartungspersonal ordnungsgemäss autorisiert und beaufsichtigt | 100% | < 95% |

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vom ISB vorab genehmigt und dokumentiert werden, mit dokumentierter Risikobewertung, Ausgleichsmassnahmen und einem definierten Überprüfungsdatum (maximal 6 Monate, verlängerbar). Gültige Ausnahmeszenarien umfassen:

- Verschobene Wartung für kritische Systeme, wo das Wartungsfenster ohne inakzeptable Geschäftsauswirkung nicht geplant werden kann (mit kompensierender Überwachung).
- Verlängerte Wartungsintervalle für geringkritische Geräte (mit dokumentierter Begründung und Herstellerkonsultation falls anwendbar).
- Kupferkabelverwendung an Standorten, wo Glasfaser spezifiziert, aber Installation nicht machbar ist (mit Abschirmungs- und physischen Schutz-Ausgleichsmassnahmen).
- Drittanbieter-Wartung ohne volle Aufsicht (mit verstärkter Protokollierung und Post-Wartungsinspektion).

Ausnahmen müssen im Ausnahmeregister erfasst und dem Management-Review-Team berichtet werden.

**Nicht zulässig**:

- Überspringen sicherheitskritischer Wartungen (USV, Brandschutzsysteme, Sicherheitssysteme) ohne Ausgleichsmassnahmen.
- Undokumentierte Kabeländerungen.
- Unbeaufsichtigte und nicht protokollierte Drittanbieter-Wartung an Geräten mit sensiblen Daten.
- Dauerhafte Ausnahmen von der Wartungsprogramm-Abdeckung.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstösst, kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung des Arbeitsverhältnisses. Ohne Autorisierung oder Dokumentation vorgenommene Kabeländerungen werden als Sicherheitsvorfall behandelt und entsprechend untersucht. Ohne Genehmigung umgangene Gerätewartung muss dem ISB zur Risikobewertung gemeldet werden.

## Kontinuierliche Verbesserung

Diese Richtlinie wird als Teil des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen berücksichtigen Änderungen an Anlagenbetrieb, Infrastrukturtechnologie, Kabelstandards, Hersteller-Wartungsempfehlungen, Gerätelebenszyklusstatus, regulatorischen Anforderungen, Audit-Befunden, Incident-Trends und Erkenntnissen aus Geräteausfällen. Abweichungen in Bezug auf diese Richtlinie müssen aufgezeichnet und durch den ISMS-Korrekturmassnahmenprozess (Klausel 10.2) mit Ursachenanalyse und verfolgter Behebung behandelt werden.

---

# Abgedeckte Bereiche des ISO-27001-Standards

Richtlinie zur Kabelsicherheit und Gerätewartung — ISO-27001-Controls-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.9 Inventar von Informationen und zugehörigen Assets |
| Klausel 6.1 Massnahmen zum Umgang mit Risiken und Chancen | 5.30 IKT-Bereitschaft für Geschäftskontinuität |
| Klausel 7.3 Bewusstsein | 7.4 Physische Sicherheitsüberwachung |
| Klausel 8.1 Betriebliche Planung und Steuerung | 7.5 Schutz vor physischen und Umweltbedrohungen |
| Klausel 9.1 Überwachung, Messung, Analyse und Bewertung | 7.8 Geräteaufstellung und -schutz |
| Klausel 10.2 Nichtkonformität und Korrekturmassnahmen | **7.12 Kabelsicherheit** |
| | **7.13 Gerätewartung** |
| | 7.14 Sichere Entsorgung oder Wiederverwendung von Geräten |
| | 8.32 Änderungsmanagement |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizer nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen für die physische Sicherheit der Datenverarbeitungsinfrastruktur |
| Schweizer DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit einschliesslich physischer Massnahmen |
| Schweizer NIN (Niederspannungs-Installationsnorm) | Niederspannungs-Elektrische-Installationsstandards für Stromverkabelung in Gebäuden |
| Schweizer Bundesverordnung über Niederspannungsinstallationen (SR 734.27) | Voraussetzungen und Inspektionsanforderungen für elektrische Installationen |
| EU DSGVO (sofern anwendbar) | Art. 32 — Sicherheit der Verarbeitung einschliesslich physischer Infrastrukturmassnahmen |
| ISO/IEC 27001:2022 | Annex A Controls 7.12 (Kabelsicherheit), 7.13 (Gerätewartung) |
| ISO/IEC 27002:2022 | Abschnitte 7.12, 7.13 — Umsetzungshinweise für Kabelsicherheit und Gerätewartung |
| IEC 11801 / EN 50173 | Internationale und europäische strukturierte Verkabelungsstandards für generische Verkabelung in Kundengebäuden |
| TIA-568 / TIA-942 | Nordamerikanische strukturierte Verkabelungs- und Rechenzentrums-Verkabelungsstandards |
| NIST SP 800-53 Rev 5 | PE-4 (Zugangskontrolle für Übertragung), PE-9 (Stromversorgungsgeräte und Verkabelung), MA-2 (Kontrollierte Wartung), MA-5 (Wartungspersonal) |
| CIS Controls v8 | Control 1 (Inventar und Kontrolle von Enterprise Assets), Control 12 (Netzwerkinfrastrukturmanagement) |
| **Bedingt**: FINMA Rundschreiben 2023/1 | Schweizer reguliertes Finanzinstitut — erweiterte Infrastrukturresilienzanforderungen |
| **Bedingt**: DORA (EU) 2022/2554 | EU-Finanzdienstleistungsunternehmen — IKT-Betriebsresilienz für Infrastruktur |
| **Bedingt**: NIS2 (EU) 2022/2555 | Wesentliche/wichtige Einrichtung in der EU — Infrastrukturschutzanforderungen |

---

<!-- QA_VERIFIED: 2026-03-29 -->
