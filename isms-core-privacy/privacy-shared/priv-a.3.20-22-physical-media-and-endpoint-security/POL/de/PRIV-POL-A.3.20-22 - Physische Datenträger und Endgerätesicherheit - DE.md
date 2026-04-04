<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.20-22-DE:privacy:POL:a.3.20-22 -->
**PRIV-POL-A.3.20-22 — Physische Datenträger und Endgerätesicherheit**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Physische Datenträger und Endgerätesicherheit |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | PRIV-POL-A.3.20-22 |
| **Dokumentersteller** | Datenschutzbeauftragter (DSB) |
| **Dokumentverantwortlicher** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |
| **Privacy-Produktversion** | 1.0 |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Date to be set] | DSB | Erstrichtlinie für ISO/IEC 27701:2025 Erstzertifizierung |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen regulatorischen oder organisatorischen Änderungen)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Datenschutzbeauftragter (DSB)
- Sekundär: Informationssicherheitsbeauftragter (ISB)
- Legal: Legal/Compliance Officer
- Letztentscheidung: Geschäftsleitung

**Zugehörige Dokumente**:

- PRIV-POL-00 (Regulatorischer Anwendbarkeitsrahmen für den Datenschutz)
- PRIV-POL-01 (Datenschutz-Governance und Entscheidungsrahmen)
- PRIV-IMP-A.3.20-22-UG (Physische Datenträger und Endgerätesicherheit — Benutzerhandbuch)
- PRIV-IMP-A.3.20-22-TG (Physische Datenträger und Endgerätesicherheit — Technisches Handbuch)
- ISMS-POL-A.7.8-10 (Clean Desk, Datenträger und Geräte — ISMS-Pendant)
- ISMS-POL-A.8.1 (Benutzer-Endgeräte — ISMS-Pendant)
- PRIV-POL-A.3.5-7 (Informationsklassifikation und -übermittlung — hier angewandtes Klassifikationsschema)
- ISO/IEC 27701:2025 Kontrollen A.3.20, A.3.21, A.3.22
- ISO/IEC 27701:2025 Anhang B (Implementierungsleitfaden B.3.20, B.3.21, B.3.22)
- GDPR Art. 32 (Sicherheit der Verarbeitung — einschliesslich Schutz von Daten auf Endgeräten und Datenträgern)
- CH FADP Art. 7 (Technische und organisatorische Massnahmen)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] für das Lebenszyklusmanagement von Speichermedien mit PII, die sichere Entsorgung oder Wiederverwendung von PII-haltigen Geräten und den Schutz von PII auf Benutzer-Endgeräten fest — gemäss ISO/IEC 27701:2025 Kontrollen A.3.20, A.3.21 und A.3.22.

**Anwendungsbereich**: Alle Speichermedien mit PII über ihren gesamten Lebenszyklus; alle Geräte mit PII-haltigen Speichermedien bei End-of-Life oder Neuzuweisung; alle Benutzer-Endgeräte, auf denen PII gespeichert, verarbeitet oder zugänglich ist.

**Zweck**: Festlegung organisatorischer Anforderungen für:

- PII-Speichermedien-Lebenszyklusmanagement abgestimmt auf das Klassifikationsschema (A.3.20)
- Sichere Verifikation, Löschung und Entsorgung von Geräten mit PII-Speichermedien (A.3.21)
- Schutz von PII auf Benutzer-Endgeräten (A.3.22)

Diese Richtlinie legt fest, **WAS** für Medienlebenszyklus-, Geräteentsorgungs- und Endgeräteschutzanforderungen für PII gelten, **WER** verantwortlich ist und **WANN** Kontrollen angewendet werden müssen. Implementierungsverfahren (**WIE**) sind in PRIV-IMP-A.3.20-22-UG und PRIV-IMP-A.3.20-22-TG dokumentiert.

**Rollenanwendbarkeit**: Diese Richtlinie gilt für [Organisation] in der Rolle als **PII-Verantwortlicher und PII-Auftragsverarbeiter**. Die Kontrollen A.3.20, A.3.21 und A.3.22 sind gemeinsame Kontrollen (Tabelle A.3) und gelten unabhängig von der Verarbeitungsrolle.

**Begründung für die zusammengefassten Kontrollen**: A.3.20 (Speichermedien), A.3.21 (Geräteentsorgung) und A.3.22 (Endgeräte) behandeln PII im Ruhezustand in physischer Form und auf Geräten. Sie schliessen das physische Exponierungsfenster für PII: Medienlebenszykluskontrollen verhindern Fehlhandhabung während des aktiven Einsatzes; Entsorgungskontrollen verhindern residuelle PII-Exposition nach der Nutzung; Endgerätekontrollen schützen PII auf den Geräten, die am häufigsten verloren gehen, gestohlen oder missbraucht werden. Zusammen bilden sie die physische und gerätebezogene Schicht des PII-Schutzes.

---

# Anwendungsbereich und Gültigkeit

## ISO/IEC 27701:2025 Kontrollanforderungen

**Kontrolle A.3.20 — Speichermedien**
Kontrolle A.3.20 verlangt von [Organisation], Speichermedien mit PII über ihren vollständigen Lebenszyklus — Beschaffung, Nutzung, Transport und Entsorgung — gemäss dem Klassifikationsschema der Organisation und den zugehörigen Handhabungsanforderungen zu verwalten.

**Kontrolle A.3.21 — Sichere Entsorgung oder Wiederverwendung von Geräten**
Kontrolle A.3.21 verlangt von [Organisation], vor der Entsorgung oder Wiederverwendung jedes Geräts mit Speichermedien zu verifizieren, dass alle auf diesen Medien gespeicherten PII (und lizenzierte Software) entfernt oder sicher überschrieben wurden.

**Kontrolle A.3.22 — Benutzer-Endgeräte**
Kontrolle A.3.22 verlangt von [Organisation], PII zu schützen, die auf Benutzer-Endgeräten gespeichert ist, verarbeitet wird oder über diese zugänglich ist.

## Was diese Richtlinie abdeckt

**Speichermedien (A.3.20)**:

- Alle Speichermedien mit PII in jeglicher Form: Festplatten (intern und extern), SSDs, USB-Sticks, optische Medien, Backup-Bänder, als Medien behandelte gedruckte Dokumente, Mikrofilm und jedes andere Medium, das PII speichern kann
- Lebenszyklusphasen: Beschaffung, Registrierung, Nutzung, Transport, Wiederverwendung und Entsorgung

**Geräteentsorgung und -wiederverwendung (A.3.21)**:

- Alle Geräte mit Speichermedien, auf denen PII vorhanden sein könnte: Server, Arbeitsstationen, Laptops, Drucker mit internem Speicher, mobile Geräte, Netzwerkgeräte mit gespeicherten Konfigurationen und jedes Gerät, auf dem PII-Speicherung möglich ist
- Entsorgung: Ausserbetriebnahme, Verkauf, Spende, Recycling, Vernichtung
- Wiederverwendung: Neuzuweisung innerhalb von [Organisation] oder an Dritte

**Benutzer-Endgeräte (A.3.22)**:

- Laptops, Desktops, Tablets, Smartphones und jedes andere Endbenutzergerät, das PII speichert, verarbeitet oder auf PII zugreifen kann
- Sowohl unternehmenseigene als auch BYOD-Geräte, auf denen PII-Zugang erlaubt ist

## Was diese Richtlinie NICHT abdeckt

- Physische Sicherheit von Räumlichkeiten und Serverräumen (siehe ISMS-POL-A.7.1-6)
- Informationsübermittlungsverfahren (siehe PRIV-POL-A.3.5-7)
- Protokollierung und Überwachung von Endgeräteaktivitäten (siehe PRIV-POL-A.3.23-31)
- Software-Asset-Management ohne PII-Bezug (siehe ISMS-POL-A.8.8)

## Regulatorischer Rahmen

**Tier 1: Obligatorische Compliance** (gemäss PRIV-POL-00):

- **EU GDPR**: Art. 32 (angemessene technische Massnahmen für PII im Ruhezustand — einschliesslich Datenträger und Endgeräte); Art. 5(1)(f) (Integrität und Vertraulichkeit)
- **CH FADP**: Art. 7 (technische Massnahmen — physischer Datenträgerschutz und sichere Entsorgung)
- **ISO/IEC 27701:2025**: Kontrollen A.3.20, A.3.21, A.3.22 (normativ)

**Tier 3: Informative Referenz** (gemäss PRIV-POL-00):

- **ISO/IEC 27002:2022**: Implementierungsleitfaden für Datenträgerhandhabung (7.10), Geräteentsorgung (7.14) und Endgeräte (8.1)
- **ISO/IEC 27701:2025 Anhang B**: B.3.20, B.3.21, B.3.22

Für eine vollständige regulatorische Kategorisierung siehe PRIV-POL-00.

---

# Richtlinienanforderungen: Speichermedien-Lebenszyklus für PII (A.3.20)

## Anforderungen an Speichermedien

[Organisation] **muss** Speichermedien mit PII über ihren vollständigen Lebenszyklus gemäss dem in PRIV-POL-A.3.5-7 definierten Klassifikationsschema und den nachstehenden Handhabungsanforderungen verwalten.

### Medienbeschaffung und -registrierung

- Alle Wechseldatenträger, die PII enthalten werden oder könnten, **müssen** bei der Beschaffung im Medienregister registriert werden
- Jeder registrierte Datenträger **muss** einem zugewiesenen Eigentümer (verantwortliche Person oder Team) haben
- Die Medienklassifikation **muss** bei der ersten Nutzung basierend auf dem gespeicherten PII-Inhalt zugewiesen werden

### Medien im Einsatz

- Speichermedien mit PII **müssen** gemäss der zugewiesenen Klassifikationsstufe (gemäss PRIV-POL-A.3.5-7-Handhabungsanforderungen) behandelt werden
- Medien mit EINGESCHRÄNKTER PII (besondere Kategorien) **müssen** stets verschlüsselt sein
- Medien mit VERTRAULICHER PII **müssen** bei Transport ausserhalb gesicherter Räumlichkeiten verschlüsselt sein
- Unbeaufsichtigte Medien mit PII **müssen** gesichert sein (in verschlossener Aufbewahrung oder in verschlossenen Geräten) — konsistent mit den Clean-Desk-Anforderungen in PRIV-POL-A.3.17-19

### Medientransport

- Der Transport von Medien mit PII ausserhalb gesicherter Räumlichkeiten **muss** protokolliert werden, einschliesslich Zielort, Zweck und Rückgabedatum
- Extern transportierte Medien mit VERTRAULICHER PII **müssen** genehmigte verschlüsselte Medien oder einen genehmigten Sicherheitskurier verwenden
- Verlust von Medien während des Transports **muss** sofort als PII-Vorfall gemäss PRIV-POL-A.3.11-12 gemeldet werden

### Medienentsorgung

- Speichermedien mit PII **dürfen** nicht über normale Abfallwege entsorgt werden
- Vor der Entsorgung **muss** PII mit einer für den Medientyp geeigneten Methode unwiderruflich entfernt werden: kryptografische Löschung (für vollständig verschlüsselte Medien, unter den Bedingungen in A.3.21), sichere Überschreibung gemäss NIST SP 800-88 (der primäre Referenzstandard für Mediensanierung) oder physische Vernichtung. Hinweis: Mehrfach-Überschreibungsstandards wie DoD 5220.22-M sind für Flash-basierte Medien (SSDs, USB-Sticks, eMMC) nicht zuverlässig; für solche Medien **muss** kryptografische Löschung gemäss NIST SP 800-88 oder physische Vernichtung verwendet werden
- Die Entsorgungsmethode **muss** im Medienregister dokumentiert werden, einschliesslich verwendeter Methode, Datum und verantwortlicher Person
- Entsorgung durch Drittanbieter-Vernichtungsdienste **muss** ein Vernichtungszertifikat produzieren, das als Nachweis aufbewahrt wird

---

# Richtlinienanforderungen: Sichere Entsorgung und Wiederverwendung von PII-Geräten (A.3.21)

## Anforderungen an Geräteentsorgung und -wiederverwendung

Vor der Entsorgung oder Wiederverwendung jedes Geräts mit Speichermedien (innerhalb oder ausserhalb von [Organisation]) **muss** [Organisation] verifizieren, dass alle PII entfernt oder sicher überschrieben wurden.

### Vorab-Entsorgungsverifikation

Alle für Entsorgung oder Neuzuweisung vorgesehenen Geräte **müssen** folgende Schritte durchlaufen:

1. **Inventarprüfung**: Bestätigen, ob PII auf dem Speichermedium des Geräts gespeichert war oder sein könnte
2. **Datenlöschung**: Alle Speicher mit einem genehmigten Löschstandard überschreiben (gemäss PRIV-IMP-A.3.20-22-TG) oder den Speicher physisch vernichten, wenn Löschung technisch nicht möglich ist
3. **Verifikation**: Bestätigen, dass die Löschung erfolgreich war (Nachverifizierungsscan nach der Löschung)
4. **Dokumentation**: Geräte-Asset-ID, PII-Status (PII vorhanden/nicht bestätigt), Löschmethode, Verifizierungsergebnis, Datum und verantwortliche Person im Entsorgungsregister aufzeichnen

### Löschstandards

Die primäre Referenz für die Mediensanierung ist **NIST SP 800-88 (Guidelines for Media Sanitization)**. Folgende Methoden gelten:

- **Software-Löschung (magnetische Medien / HDDs)**: Sichere Überschreibung mittels NIST SP 800-88 Clear- oder Purge-Techniken entsprechend der Datensensibilität. Mehrfach-Überschreibungstechniken (z.B. DoD 5220.22-M) sind für HDDs akzeptabel, **dürfen** aber für Flash-basierte Medien (SSDs, USB-Sticks, eMMC) nicht als primäre Löschmethode verwendet werden, da Wear-Levelling die Überschreibung unzuverlässig macht
- **Kryptografische Löschung**: Vernichtung von Verschlüsselungsschlüsseln ist als Löschmethode nur akzeptabel, wenn die vollständige Festplattenverschlüsselung ab dem Zeitpunkt des ersten Datenschreibens auf diesen Medien bestätigt aktiv war und die Verschlüsselungsimplementierung validiert ist (z.B. Hardware-AES-256). Bei Unsicherheit über die Verschlüsselungsabdeckung **muss** stattdessen physische Vernichtung verwendet werden
- **Physische Vernichtung**: Schreddern oder Entmagnetisieren von Speichermedien — erforderlich für EINGESCHRÄNKTE PII auf Flash-basierten Medien und für alle Medien, bei denen Software-Löschung nicht verifiziert werden kann; Vernichtung muss mit Methode und bestätigender Person dokumentiert werden

### Wiederverwendung innerhalb von [Organisation]

Vor der Neuzuweisung von Geräten an einen anderen Benutzer innerhalb von [Organisation]:

- Alle PII aus dem Profil des vorherigen Benutzers **müssen** entfernt werden
- Das Gerät **muss** abgebildet oder auf die Baseline-Konfiguration zurückgesetzt werden
- Ein neuer Benutzerzugangsdatensatz **muss** erstellt werden; der Zugang des vorherigen Benutzers muss gemäss PRIV-POL-A.3.8-10 widerrufen werden

### Entsorgung durch Dritte

Wenn Geräte durch einen Drittanbieter-Service entsorgt werden (Recycler, Wiederverkäufer, Wohltätigkeitsorganisation):

- Der Dritte **muss** vor dem Verlassen der Obhut von [Organisation] ein Datenlöschungszertifikat bereitstellen
- Für Geräte mit EINGESCHRÄNKTER PII ist physische Vernichtung des Speichermediums erforderlich (Verkauf oder Spende ohne bestätigte Vernichtung nicht zulässig)
- Das Vernichtungszertifikat **muss** für mindestens 5 Jahre im Entsorgungsregister aufbewahrt werden

---

# Richtlinienanforderungen: Schutz von PII auf Benutzer-Endgeräten (A.3.22)

## Endgeräteanforderungen für PII

[Organisation] **muss** sicherstellen, dass PII, die auf Benutzer-Endgeräten gespeichert ist, verarbeitet wird oder über diese zugänglich ist, geschützt wird.

### Mindest-Endgerätekontrollen für PII

Alle unternehmenseigenen Endgeräte, die PII speichern, verarbeiten oder darauf zugreifen, **müssen** konfiguriert sein mit:

- **Vollständiger Festplattenverschlüsselung**: Aktiv und durchgesetzt; Schlüsselmanagement gemäss Kryptografiestandards (PRIV-POL-A.3.23-31)
- **Bildschirmsperre**: Automatische Sperre nach maximaler Leerlaufzeit (konfiguriert gemäss PRIV-IMP-A.3.20-22-TG)
- **Remote-Wipe-Fähigkeit**: Remote-Wipe oder -Sperrmöglichkeit für das Gerät registriert; Wipe-Fähigkeit mindestens jährlich getestet
- **Geräteverwaltungs-Enrolment**: In unternehmenseigene Mobile Device Management (MDM)- oder Unified Endpoint Management (UEM)-Lösung eingeschrieben, wo technisch möglich
- **Aktuelle Patches**: Betriebssystem- und Sicherheitspatches innerhalb der in ISMS-POL-A.8.8 definierten Fristen angewandt

### PII-Speicherbeschränkungen auf Endgeräten

- Massendownload oder -speicherung von PII auf Endgeräten **muss** auf das für die Arbeitsfunktion Notwendige beschränkt sein
- Kopieren oder Speichern grosser PII-Mengen (Massenexport aus Datenbanken oder Anwendungen) auf lokale Endgeräte erfordert die Genehmigung des Data Owner
- EINGESCHRÄNKTE PII (besondere Kategorien) **darf** nicht lokal auf Endgeräten gespeichert werden, ausser wenn operativ notwendig mit DSB-Benachrichtigung; wenn lokal gespeichert, muss sie sich in einem verschlüsselten Container mit Zugriffskontrollen getrennt vom allgemeinen Dateisystemzugang befinden

### BYOD (Bring Your Own Device)

Wenn persönliche Geräte für den PII-Zugang zugelassen sind (anwendbare BYOD-Richtlinie):

- BYOD-Geräte **müssen** in eine MDM/Containerisierungs-Lösung eingeschrieben sein, die einen verwalteten PII-Arbeitsbereich getrennt von persönlichen Daten erstellt
- Mindestkontrollen (Verschlüsselung, Bildschirmsperre, Remote Wipe) **müssen** für den verwalteten Arbeitsbereich gelten
- Das Recht der Organisation, den verwalteten Arbeitsbereich per Remote Wipe zu löschen, **muss** schriftlich vereinbart werden, bevor PII-Zugang gewährt wird
- PII **darf** nicht ausserhalb des verwalteten Arbeitsbereichs auf BYOD-Geräten gespeichert werden

### Verlust oder Diebstahl von Endgeräten

Verlust oder Diebstahl eines Endgeräts mit PII oder PII-Zugang **muss**:

- Sofort dem IT-Sicherheitsteam und DSB gemeldet werden
- Als vermuteter PII-Vorfall behandelt und gemäss PRIV-POL-A.3.11-12 verwaltet werden
- Remote Wipe für das Gerät so schnell wie möglich und innerhalb von 4 Stunden nach gemeldeter Bestätigung des Verlusts an das IT-Sicherheitsteam initiiert werden. Wenn Remote Wipe innerhalb von 4 Stunden technisch nicht möglich ist (z.B. Gerät ist offline), muss der DSB sofort benachrichtigt und die Verzögerung dokumentiert werden; kompensatorische Massnahmen (Passwortreset, Kontosperrung, PII-Zugangswiderruf) sind sofort bis zur Wipe-Bestätigung zu ergreifen

---

# Rollen und Verantwortlichkeiten

## Verantwortungsmatrix

| Rolle | Verantwortlichkeiten für A.3.20–A.3.22 |
|-------|----------------------------------------|
| **Datenschutzbeauftragter (DSB)** | Definiert PII-spezifische Datenträger- und Endgeräteanforderungen; wird über EINGESCHRÄNKTE PII auf Endgeräten benachrichtigt; überprüft Entsorgungsregister auf Angemessenheit; wird über verlorene/gestohlene Geräte informiert |
| **ISB** | Setzt technische Standards für Löschung, Verschlüsselung und Endgeräteverwaltung; konfiguriert MDM/UEM; pflegt Entsorgungsregister; untersucht verlorene/gestohlene Geräte |
| **IT-Sicherheitsteam** | Implementiert Verschlüsselung und MDM; führt Medienlöschung und -entsorgung durch; pflegt Medienregister und Entsorgungsregister; initiiert Remote Wipe bei verlorenen Geräten |
| **Data Owner** | Genehmigt Massen-PII-Download auf Endgeräte; wird über PII-haltige Medienentsorgung in seinem Bereich benachrichtigt |
| **Alle Mitarbeitenden** | Melden verlorene oder gestohlene Geräte sofort; halten Clean-Screen-Anforderungen ein; beschränken PII auf das Notwendige auf Endgeräten |

---

# Nachweisanforderungen

Folgende Nachweise belegen den Betrieb dieser Richtlinie:

| Nachweis | Beschreibung | Aufbewahrung |
|---------|-------------|--------------|
| Medienregister | Inventar von Wechseldatenträgern mit PII, Eigentümer, Klassifikation und Status | Aktuell + 3 Jahre |
| Medientransportprotokoll | Aufzeichnungen von PII-Datenträgern, die ausserhalb gesicherter Räumlichkeiten transportiert wurden | 3 Jahre |
| Entsorgungsregister | Geräteentsorgungsaufzeichnungen mit PII-Status, Löschmethode, Verifikation und Datum | 5 Jahre |
| Vernichtungszertifikate | Drittanbieter-Vernichtungszertifikate für PII-haltige Geräte | 5 Jahre |
| Endgerät-Verschlüsselungsstatus | Konfigurationsberichte, die Vollständige-Festplatten-Verschlüsselung auf Unternehmensgeräten bestätigen | Aktuell + 3 Jahre |
| MDM/UEM-Enrolment-Aufzeichnungen | In Endgeräteverwaltung eingeschriebene Geräte, einschliesslich BYOD-verwalteter Arbeitsbereiche | Aktuell + 3 Jahre |
| Berichte über verlorene/gestohlene Geräte | Aufzeichnungen über Geräteverlust/-diebstahl, Remote-Wipe-Aktionen und PII-Vorfallsbewertungen | 3 Jahre |

---

# Prüfungshinweise

Prüfer, die die Compliance mit A.3.20, A.3.21 und A.3.22 verifizieren, sollten Folgendes vorfinden:

**Für A.3.20 (Speichermedien)**:
- Medienregister mit PII-Datenträgerinventar
- Nachweis, dass Medien mit PII verschlüsselt sind (besonders EINGESCHRÄNKTE PII)
- Transportprotokoll für ausserhalb gesicherter Räumlichkeiten bewegte Medien
- Entsorgungsaufzeichnungen einschliesslich Löschmethode und Verifikation

**Für A.3.21 (Geräteentsorgung)**:
- Entsorgungsregister mit PII-Statusprüfungen vor der Entsorgung
- Nachweis der angewandten genehmigten Löschmethode
- Vernichtungszertifikate von Drittanbieter-Entsorgungsdiensten
- Keine Entsorgung von EINGESCHRÄNKTER PII-Geräten ohne bestätigte physische Vernichtung

**Für A.3.22 (Endgeräte)**:
- Konfigurationsberichte zur Vollständigen-Festplatten-Verschlüsselung
- MDM/UEM-Enrolment-Aufzeichnungen
- Nachweis über Remote-Wipe-Tests
- Schriftliche Vereinbarungen für BYOD, wenn persönliche Geräte auf PII zugreifen
- Aufzeichnungen über Reaktion auf verloren/gestohlene Geräte mit Remote-Wipe-Bestätigung

---

<!-- QA_VERIFIED: 2026-03-29 -->
