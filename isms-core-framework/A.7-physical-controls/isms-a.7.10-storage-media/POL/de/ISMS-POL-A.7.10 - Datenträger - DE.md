<!-- ISMS-CORE:POLICY:ISMS-POL-A.7.10-DE:framework:POL:a.7.10 -->
**ISMS-POL-A.7.10 — Datenträger**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Datenträger |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.7.10 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Informationssicherheitsbeauftragter (ISB) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] | |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Date to be set] | ISB | Erstfassung der Richtlinie für die ISO 27001:2022-Zertifizierung |

**Überprüfungsrhythmus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Betriebsleiter
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-POL-A.5.12-13 (Informationsklassifikation und -kennzeichnung)
- ISMS-POL-A.7.6-7-14 (Gesicherte Bereiche und Medienverarbeitung)
- ISMS-POL-A.8.10 (Löschung von Informationen)
- ISMS-IMP-A.7.10.1-UG/TG (Datenträgerinventar)
- ISMS-IMP-A.7.10.2-UG/TG (Verfahren zur Datenträgerverwaltung)
- ISMS-IMP-A.7.10.3-UG/TG (Lebenszyklusverfolgung von Datenträgern)
- ISO/IEC 27001:2022 Massnahme A.7.10

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] für die Verwaltung von Datenträgern über den gesamten Lebenszyklus fest — von der Beschaffung über den Einsatz und den Transport bis hin zur Entsorgung.

**Geltungsbereich**: Diese Richtlinie gilt für alle Datenträger, die von [Organisation] verwendet werden, einschliesslich Wechseldatenträger, fest verbauter Speicher, Cloud-Speicher sowie physischer Dokumente mit schützenswerten Informationen.

**Zweck**: Anforderungen für die sichere Verwaltung von Datenträgern gemäss dem Klassifikationsschema und den Handhabungsanforderungen der Organisation festlegen. Diese Richtlinie legt fest, WAS für Datenträger gilt und WER dafür verantwortlich ist. Implementierungsverfahren (WIE) sind in ISMS-IMP-A.7.10 dokumentiert.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen), darunter das schweizerische nDSG, die EU DSGVO und ISO/IEC 27001:2022. Bedingt anwendbare sektorspezifische Anforderungen (FINMA, PCI DSS v4.0.1, DORA) gelten, wenn die Geschäftstätigkeit von [Organisation] deren Anwendbarkeit auslöst.

---

**Massnahmenausrichtung und Geltungsbereich**

**ISO/IEC 27001:2022 Massnahme A.7.10**

**ISO/IEC 27001:2022 Anhang A.7.10 — Datenträger**

> *Datenträger sollten über ihren Lebenszyklus der Beschaffung, Nutzung, des Transports und der Entsorgung gemäss dem Klassifikationsschema und den Handhabungsanforderungen der Organisation verwaltet werden.*

**Massnahmenziele**:

- Sicherstellen, dass die Offenlegung, Änderung, Entfernung oder Vernichtung von Informationen auf Datenträgern ausschliesslich durch autorisierte Personen erfolgt
- Schutz von Datenträgern über den gesamten Lebenszyklus
- Nachvollziehbarkeit für Datenträger mit schützenswerten Informationen gewährleisten
- Datenverlust durch unsachgemässe Handhabung von Datenträgern verhindern

**Massnahmentyp**: Präventiv
**Massnahmenkategorie**: Physisch

**Diese Richtlinie adressiert**:

- Autorisierung und Registrierung von Wechseldatenträgern
- Anforderungen an die Datenträgernutzung und Verschlüsselung
- Transport und Gewahrsamsnachweis (Chain of Custody)
- Speicheranforderungen nach Klassifikation
- Verfahren zur Entsorgung und Wiederverwendung

## Was diese Richtlinie regelt

Diese Richtlinie:

- **Definiert** Anforderungen für die Datenträgerverwaltung über den gesamten Lebenszyklus
- **Legt fest** Handhabungsanforderungen nach Informationsklassifikation
- **Spezifiziert** Transportanforderungen und Gewahrsamsnachweis
- **Verweist** auf anwendbare regulatorische Anforderungen gemäss ISMS-POL-00

## Was diese Richtlinie NICHT regelt

Diese Richtlinie regelt NICHT:

- **Das Informationsklassifikationsschema** (siehe ISMS-POL-A.5.12-13)
- **Spezifische Methoden zur sicheren Entsorgung** (siehe ISMS-POL-A.7.6-7-14)
- **Detaillierte Verfahren zur Informationslöschung** (siehe ISMS-POL-A.8.10)
- **Beschaffungsspezifikationen für Datenträger** (siehe ISMS-IMP-A.7.10)

**Begründung**: Die Trennung von Richtlinienanforderungen und Implementierungshinweisen ermöglicht:

- Stabilität der Richtlinie trotz technologischer Veränderungen
- Flexibilität für verschiedene Datenträgertypen und Anbieter
- Klare Unterscheidung zwischen Governance (Richtlinie) und Ausführung (Implementierung)

## Geltungsbereich

**Diese Richtlinie gilt für**:

- Digitale Datenträger: Festplatten (HDD/SSD), USB-Sticks, SD-Karten, optische Medien (CD/DVD), Backup-Bänder, Netzwerkspeicher
- Physische Dokumente: Papierdokumente, Mikrofilm, Mikrofiche
- Cloud-Speicher: Cloud-Backup-Speicher, Cloud-Dateispeicher (verwaltet gemäss A.5.19-23)
- Lebenszyklusphasen: Beschaffung, Nutzung, Transport, Lagerung, Entsorgung
- Personal: alle Mitarbeitenden, Auftragnehmer und Dritte, die Datenträger handhaben

**Nicht im Geltungsbereich**:

- Informationsklassifikationsschema (abgedeckt durch A.5.12-13)
- Methoden zur sicheren Entsorgung (abgedeckt durch A.7.14)
- Verträge mit externen Cloud-Speicheranbietern (abgedeckt durch A.5.19-23)

## Regulatorische Anwendbarkeit

Regulatorische Anforderungen werden gemäss **ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)** kategorisiert.

**Stufe 1: Verbindliche Compliance**

| Regulierung | Anwendbarkeit | Wesentliche Anforderungen |
|-------------|---------------|--------------------------|
| **Schweizerisches nDSG** | Alle Bearbeitungen von Personendaten | Art. 8 — Technische Massnahmen; Art. 6 — Datensparsamkeit |
| **ISO/IEC 27001:2022** | Zertifizierungsumfang | Massnahme A.7.10 |

**Stufe 2: Bedingte Anwendbarkeit**

Gilt nur, wenn spezifische Geschäftsbedingungen die Anwendbarkeit auslösen:

| Regulierung | Auslösebedingung | Anforderungen |
|------------|-----------------|---------------|
| **EU DSGVO** | Bearbeitung von EU-Personendaten, Niederlassung in der EU oder Angebot von Diensten für die EU | Art. 5(1)(f) Integrität/Vertraulichkeit; Art. 17 Recht auf Löschung |
| **PCI DSS v4.0.1** | Bearbeitung von Zahlungskartendaten | Anforderung 9.4 — Medienschutz |
| **FINMA** | Reguliertes Schweizer Finanzinstitut | Datenschutz- und Aufbewahrungsanforderungen |
| **DORA** | EU-Finanzdienstleistungsunternehmen | IKT-Asset-Management |

**Stufe 3: Informationsleitlinien**

Diese Rahmenwerke informieren die Implementierung, stellen jedoch keine verbindlichen Compliance-Anforderungen dar, es sei denn, sie sind vertraglich vorgeschrieben:

- NIST SP 800-88 Rev. 2 (Leitlinien zur Mediensanitisierung)
- ISO/IEC 27040 (Speichersicherheit)
- CIS Controls v8.1 (Massnahme 3 — Datenschutz)
- Branchenbest Practices für Datenträgerverwaltung

**Compliance-Bestimmung**: [Organisation] ermittelt anwendbare Stufe-2-Regulierungen durch periodische Bewertung der Geschäftstätigkeit. Bei Überschneidung mehrerer Regulierungen gelten die strengsten Anforderungen.

---

# Richtlinienaussagen

## Datenträgerrichtlinie

[Organisation] muss geeignete Verfahren, technische Massnahmen und organisationsweite Richtlinien für die Nutzung von Datenträgern gemäss dem Klassifikationsschema und den Datenanforderungen der Organisation festlegen und implementieren.

**Richtlinienaussage**:

- Alle Datenträger mit Organisationsinformationen müssen gemäss dieser Richtlinie verwaltet werden
- Die Nutzung von Wechseldatenträgern muss eingeschränkt und kontrolliert werden
- Datenträger mit schützenswerten Informationen müssen während des Transports geschützt werden
- Die Entsorgung muss sicherstellen, dass Daten nicht wiederhergestellt werden können

## Verwaltung von Wechseldatenträgern

### Autorisierung und Registrierung

**Autorisierungsanforderungen**:

- Die Nutzung von Wechseldatenträgern muss durch die direkte Führungskraft autorisiert werden
- Die Autorisierung muss zulässige Anwendungsfälle und Datenklassifikationen festlegen
- Persönliche Wechseldatenträger dürfen nicht für Organisationsdaten verwendet werden
- Organisationseigene Datenträger müssen im Asset-Management-System registriert werden

**Zugelassene Datenträger**:

- Es dürfen nur organisationszugelassene und verschlüsselte Wechseldatenträger verwendet werden
- Für VERTRAULICHE Daten müssen hardwareverschlüsselte USB-Geräte eingesetzt werden
- Datenträger müssen über zugelassene Lieferanten beschafft werden
- Mitarbeitereigene Datenträger (Bring-your-own) sind für VERTRAULICHE/INTERNE Daten untersagt

### Nutzungsanforderungen

**Datenübertragung**:

- Die Übertragung von VERTRAULICHEN Daten auf Wechseldatenträger erfordert die Genehmigung des Managements
- Daten müssen vor der Übertragung auf Wechseldatenträger verschlüsselt werden
- Übertragungsprotokolle müssen für VERTRAULICHE Daten geführt werden
- Daten müssen von Datenträgern entfernt werden, sobald sie nicht mehr benötigt werden

**Zugangskontrolle**:

- Datenträger müssen passwortgeschützt oder verschlüsselt sein
- Datenträger dürfen nicht unbeaufsichtigt gelassen werden
- Datenträger müssen bei Nichtgebrauch sicher aufbewahrt werden
- Datenträgerinhalte müssen vor der Nutzung auf Schadsoftware überprüft werden

### Datenträgerinventar

**Registrierung**:

- Alle Wechseldatenträger müssen im Asset-Inventar registriert werden
- Die Registrierung muss umfassen: Datenträgertyp, Kapazität, zugewiesener Nutzer, Verwendungszweck, Klassifikationsstufe
- Vierteljährliche Inventarprüfungen müssen 100 % der registrierten Wechseldatenträger mit den Asset-Aufzeichnungen abgleichen; der Abgleich muss physischen Standort, Verschlüsselungsstatus und zugewiesenen Nutzer überprüfen. Abweichungen müssen innerhalb von 1 Arbeitstag gemäss den Incident-Response-Verfahren eskaliert werden

## Transport von Datenträgern

### Sicherer Transport

**Kurieranforderungen**:

- VERTRAULICHE Datenträger dürfen ausschliesslich über zugelassene sichere Kurierdienste transportiert werden
- Der Gewahrsamsnachweis (Chain of Custody) muss dokumentiert werden
- Der Empfänger muss den Erhalt verifizieren und bestätigen
- Manipulationsgeschütztes Verpackungsmaterial muss verwendet werden

**Persönlicher Transport**:

- Datenträger müssen während Reisen im Handgepäck mitgeführt werden (nicht als aufgegebenes Gepäck)
- Datenträger müssen verschlüsselt sein
- Datenträger dürfen während des Transports nicht unbeaufsichtigt gelassen werden
- Transport durch Hochrisikogebiete muss vermieden werden

### Nachverfolgung und Verantwortlichkeit

**Gewahrsamsnachweis**:

- Die Übergabe von Datenträgern zwischen Personen muss dokumentiert werden
- Die Dokumentation muss umfassen: Datum, Übergeber, Übernehmer, Datenträgerkennung, Zweck
- Eine Empfangsbestätigung muss eingeholt werden

## Lagerungsanforderungen

### Physische Lagerung

**Sichere Aufbewahrung**:

- Datenträger mit VERTRAULICHEN Informationen müssen in abschliessenden Schränken oder Tresoren aufbewahrt werden
- Lagerungsorte müssen über geeignete Zugangsmassnahmen verfügen
- Umgebungsbedingungen müssen die Integrität der Datenträger schützen (Temperatur, Luftfeuchtigkeit, Magnetfelder)
- Backup-Datenträger müssen getrennt von Systemen aufbewahrt werden

**Aufbewahrungsfristen**:

- Datenträger müssen gemäss den Aufbewahrungsanforderungen im Aufbewahrungsplan (ISMS-REG-RETENTION) aufbewahrt werden
- Aufbewahrungsfristen für spezifische Datentypen und Datenträgerkategorien sind in ISMS-REG-RETENTION dokumentiert
- Datenträger müssen nach Ablauf der Aufbewahrungsfrist entsorgt werden; Backup-Bänder und Cloud-Snapshots müssen in die Aufbewahrungsplanabdeckung einbezogen sein, mit dokumentierten Auslösern für die Entsorgung/Löschung

### Schutzanforderungen nach Klassifikation

| Klassifikation | Lagerungsanforderung | Verschlüsselung | Zugangskontrolle |
|----------------|---------------------|-----------------|-----------------|
| **VERTRAULICH** | Verschliessbarer Tresor/Schrank | Obligatorisch (gemäss ISMS-POL-A.8.24) | Nur namentlich benannte Personen |
| **INTERN** | Verschliessbarer Schrank | Empfohlen (gemäss ISMS-POL-A.8.24) | Autorisierte Mitarbeitende |
| **ÖFFENTLICH** | Standardlagerung | Optional | Allgemeiner Zugang |

**Verschlüsselungsimplementierung**: Plattformspezifische Verschlüsselungsmechanismen (BitLocker/FileVault für Endpunkte, LUKS für Linux, S3 SSE-KMS für Cloud-Objektspeicher, Storage-Array-Verschlüsselung, Band-Verschlüsselung) sind in ISMS-IMP-A.7.10.2 definiert und müssen den kryptografischen Standards in ISMS-POL-A.8.24 entsprechen.

## Entsorgung von Datenträgern

### Entsorgungsanforderungen

Entsorgung und Sanitisierung müssen sicherstellen, dass Informationen nicht wiederhergestellt werden können, unter Anwendung organisationszugelassener Sanitisierungs-/Vernichtungsmethoden, die dem Datenträgertyp und dem Klassifikationsniveau der jemals darauf gespeicherten Daten entsprechen.

**Anforderungen an das Entsorgungsergebnis nach Klassifikation**:

| Klassifikation | Erforderliches Ergebnis | Verifikation |
|----------------|------------------------|--------------|
| **VERTRAULICH** | Nicht wiederherstellbar mit beliebigen Mitteln | Vernichtungsnachweis des zugelassenen Anbieters; beglaubigte Vernichtung bei hochsensiblen Daten |
| **INTERN** | Nicht wiederherstellbar ohne Spezialausrüstung | Dokumentierter Nachweis der erfolgreichen Löschung |
| **ÖFFENTLICH** | Standardlöschung akzeptabel | Dokumentation der Entsorgung |

**Zugelassene Methoden**: Spezifische Sanitisierungs- und Vernichtungsmethoden pro Datenträgertyp (HDD, SSD, Band, optisch, mobile Geräte) sind in ISMS-IMP-A.7.10.3 definiert, ausgerichtet an den Grundsätzen des NIST SP 800-88 Rev. 2. Physische Entsorgungsanforderungen werden in ISMS-POL-A.7.6-7-14 adressiert.

### Interne Wiederverwendung

Vor der Wiederverwendung eines Datenträgers innerhalb der Organisation:

- Alle schützenswerten Daten müssen sicher gelöscht werden
- Die Löschung muss verifiziert werden
- Datenträger müssen auf physische Integrität überprüft werden
- Asset-Aufzeichnungen müssen aktualisiert werden

### Externe Entsorgung

Extern zu entsorgende Datenträger müssen:

- Alle Daten sicher gelöscht oder physisch vernichtet haben
- Über zugelassene Entsorgungsanbieter entsorgt werden
- Die Entsorgung mit aufzubewahrenden Zertifikaten dokumentieren
- Niemals mit wiederherstellbaren Daten verkauft oder gespendet werden

## Papierdokumente und physische Medien

### Handhabungsanforderungen

**Papierdokumente**:

- Dokumente müssen klassifiziert und gemäss dem Klassifikationsschema gehandhabt werden
- VERTRAULICHE Dokumente müssen in abschliessenden Schränken aufbewahrt werden
- Dokumente müssen unmittelbar nach dem Druckvorgang vom Drucker abgeholt werden
- Die Clean-Desk-Richtlinie muss eingehalten werden

### Entsorgung

**Sichere Vernichtung**:

- VERTRAULICHE Papierdokumente müssen kreuzgeschnitten geschreddert werden
- INTERNE Papierdokumente müssen geschreddert werden
- Das Schreddern muss vor Ort oder durch zugelassene Auftragnehmer erfolgen
- Bei Massenvernichtung muss diese begleitet oder zertifiziert werden

---

# Rollen und Verantwortlichkeiten

## Verantwortlichkeitsmatrix (RACI)

| Rolle | Verantwortlichkeiten für Datenträger |
|-------|-------------------------------------|
| **Geschäftsleitung** | Richtlinie genehmigen, Ressourcen für Datenträgersicherheit bereitstellen |
| **ISB** | Richtlinieneigentümerschaft, Standards, Compliance-Überwachung |
| **IT-Betrieb** | Datenträgerbeschaffung, Verschlüsselungsimplementierung, Entsorgungsdurchführung |
| **Direkte Führungskräfte** | Datenträgernutzung autorisieren, Team-Compliance sicherstellen |
| **Asset Management** | Datenträgerinventar, Nachverfolgung, Lebenszyklusverwaltung |
| **Alle Mitarbeitenden** | Datenträger richtlinienkonform handhaben, Verluste sofort melden |

## Eskalationspfad

- Datenträgerverlust/-diebstahl: Mitarbeitende → Direkte Führungskraft + IT-Betrieb (sofort) → ISB
- Fragen zur Datenträgerrichtlinie: Mitarbeitende → IT-Betrieb → ISB

---

# Governance und Compliance

## Bewertungsrahmen

| Bewertung | Häufigkeit | Verantwortlich | Nachweise |
|-----------|-----------|---------------|-----------|
| Prüfung Wechseldatenträger | Vierteljährlich | IT-Betrieb | Inventarabgleich |
| Compliance-Prüfung Verschlüsselung | Monatlich | IT-Sicherheit | Berichte des Endpunktverwaltungssystems |
| Prüfung Entsorgungsprozess | Halbjährlich | Interne Revision | Entsorgungsunterlagen, Zertifikate |
| Überprüfung Transportsicherheit | Jährlich | ISB | Prozessüberprüfung |

**Governance-Kennzahlen**:

- Registrierte Datenträger mit Verschlüsselung (Ziel: 100 %)
- Datenträgerverluste (Ziel: 0)
- Entsorgungen mit Zertifikat (Ziel: 100 % für VERTRAULICH)
- Überfällige Datenträgerrückgaben (Ziel: < 3)
- Abschlussquote Datenträgerprüfungen (Ziel: 100 %)

## Richtlinienüberprüfung

- **Häufigkeit**: Mindestens jährlich
- **Auslöser**: Datenträgervorfälle, technologische Änderungen, Prüfungsbefunde, regulatorische Aktualisierungen
- **Prüfer**: ISB, IT-Betrieb, Asset Management
- **Genehmigung**: Geschäftsleitung

## Ausnahmenmanagement

**Zulässige Ausnahmen**:

- Unverschlüsselte Datenträger für spezifische betriebliche Anforderungen (mit verstärkten Massnahmen)
- Verlängerte Aufbewahrungsfristen über Standardfristen hinaus (mit dokumentierter Begründung)
- Alternative Transportmethoden (mit Risikoakzeptanz)

**Ausnahmeprozess**:

1. Geschäftliche Begründung dokumentieren
2. Risikobewertung einschliesslich der Auswirkungen auf die Datenklassifikation
3. ISB-Genehmigung mit kompensierenden Massnahmen
4. Befristete Genehmigung (maximal 6 Monate)
5. Dokumentation im Ausnahmenregister

**Nicht zulässig**:

- VERTRAULICHE Daten auf unverschlüsselten Wechseldatenträgern ohne kompensierende Massnahmen
- Persönliche Datenträger für VERTRAULICHE Organisationsdaten
- Entsorgung ohne Verifikation bei VERTRAULICHEN Datenträgern

Alle Ausnahmen müssen im Ausnahmenregister (ISMS-REG-EXCEPTIONS) erfasst werden.

## Verknüpfung mit Korrekturmassnahmen

Nichtkonformitäten in Bezug auf diese Richtlinie (z. B. verlorene Datenträger, nicht registrierte Datenträger, unsachgemässe Entsorgung, fehlende Verschlüsselung) müssen im ISMS-Korrekturmassnahmenprozess (Abschnitt 10.2) erfasst und verwaltet werden, mit Ursachenanalyse und nachverfolgter Behebung.

---

# Implementierung und Referenzen

## Integration in das ISMS

Diese Richtlinie integriert sich in das Informationssicherheits-Managementsystem von [Organisation]:

**Risikobeurteilung** (ISO 27001 Abschnitt 6.1):

- Risiken durch Datenträgerverlust und -diebstahl fliessen in die Handhabungsanforderungen ein
- Datenverlustrisiken werden durch Verschlüsselung und Massnahmen adressiert
- Risikopläne dokumentieren Schutzmassnahmen für Datenträger

**Anwendbarkeitserklärung** (ISO 27001 Abschnitt 6.1.3):

- Anwendbarkeit der Massnahme A.7.10 ist in der SoA von [Organisation] begründet
- Implementierungsstatus wird verfolgt und berichtet

**Verwandte Massnahmen**:

| Massnahme | Beziehung |
|-----------|-----------|
| **A.5.9** | Asset-Inventar einschliesslich Datenträger |
| **A.5.12-13** | Informationsklassifikation als Grundlage für Handhabungsanforderungen |
| **A.7.6-7-14** | Gesicherte Bereiche, Clean-Desk, sichere Entsorgung |
| **A.8.10** | Anforderungen zur Informationslöschung |
| **A.8.24** | Kryptografie für die Datenträgerverschlüsselung |

**Integration gestapelter Massnahmen**:

A.7.10 (Datenträger) ist mit verwandten Massnahmen gestapelt:

| Gestapelte Massnahme | Integrationspunkt | Beitrag von A.7.10 |
|---------------------|-------------------|-------------------|
| **A.5.12-13** (Klassifikation) | Handhabungsanforderungen | Klassifikation bestimmt Schutzniveaus gemäss A.7.10 |
| **A.7.6-7-14** (Gesicherte Bereiche/Entsorgung) | End-of-Life | A.7.10 verwaltet den Lebenszyklus; A.7.14 regelt die Entsorgung |
| **A.8.24** (Kryptografie) | Verschlüsselung | A.7.10 schreibt Verschlüsselung vor; A.8.24 legt Standards fest |

Die Bewertung von A.7.10 sollte die Bewertungen gestapelter Massnahmen für eine vollständige Abdeckung berücksichtigen.

## Implementierungsressourcen

**Implementierungshinweise** (ISMS-IMP-A.7.10-Suite):

| Dokument-ID | Titel | Zweck |
|-------------|-------|-------|
| **ISMS-IMP-A.7.10.1-UG/TG** | Verfahren für das Datenträgerinventar | Registrierungs- und Nachverfolgungsverfahren |
| **ISMS-IMP-A.7.10.2-UG/TG** | Verfahren zur Datenträgerverwaltung | Nutzungs- und Transportverfahren |
| **ISMS-IMP-A.7.10.3-UG/TG** | Verfahren zur Datenträgerentsorgung | Entsorgungs- und Vernichtungsverfahren |

---

# Nachweise für diese Richtlinie

**Stage 1 (Dokumentationsüberprüfung) Nachweise:**

Erforderliche Stage-1-Nachweise umfassen:

- Dieses Richtliniendokument (ISMS-POL-A.7.10 v1.0)
- Dokumentierte Genehmigung durch ISB, IT-Betriebsleiter, Geschäftsleitung
- Nachweis der Kommunikation an betroffene Rollen
- Anforderungen für Wechseldatenträger dokumentiert (Verwaltung von Wechseldatenträgern)
- Transportanforderungen dokumentiert (Transport von Datenträgern)
- Entsorgungsanforderungen dokumentiert (Entsorgung von Datenträgern)
- Rollen und Verantwortlichkeiten zugewiesen (Rollen und Verantwortlichkeiten)

Der Nachweisstatus wird im ISMS-Nachweisregister verfolgt.

**Stage 2 (Operationale Wirksamkeit) Nachweise:**

Erforderliche Nachweise zur Demonstration der operationalen Wirksamkeit dieser Richtlinie:

- Datenträgerinventar mit Verschlüsselungsstatus
- Autorisierungsunterlagen für Datenträger
- Gewahrsamsnachweis-Unterlagen für Transporte
- Entsorgungsunterlagen mit Zertifikaten
- Prüfberichte für Datenträger mit Abgleichsdokumentation
- Vorfallberichte für verlorene/gestohlene Datenträger
- Schulungsnachweise für den Umgang mit Datenträgern

---

# Definitionen

| Begriff | Definition |
|---------|------------|
| **Datenträger** | Jedes Gerät oder Material, das Daten speichern kann, einschliesslich digitaler und physischer Formate |
| **Wechseldatenträger** | Tragbare Speichergeräte, die aus Systemen entfernt werden können (USB-Sticks, externe Laufwerke, optische Discs) |
| **Sicheres Überschreiben** | Prozess des Überschreibens gespeicherter Daten mit Mustern, um eine Wiederherstellung zu verhindern |
| **Entmagnetisierung (Degaussing)** | Verwendung starker Magnetfelder zur Löschung von Daten auf magnetischen Speichermedien |
| **Gewahrsamsnachweis (Chain of Custody)** | Dokumentierter chronologischer Nachweis über Handhabung, Übergabe und Aufbewahrung von Datenträgern |
| **Vernichtungsnachweis** | Schriftliche Bestätigung eines zugelassenen Anbieters, dass ein Datenträger vernichtet wurde |

---

# Genehmigungsnachweis

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date to be set] |
| **IT-Betriebsleiter** | [Name] | [Date to be set] |
| **Geschäftsleitung** | [Name] | [Date to be set] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt die Anforderungen für die Datenträgerverwaltung fest. Implementierungsverfahren sind in ISMS-IMP-A.7.10 (UG/TG) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
