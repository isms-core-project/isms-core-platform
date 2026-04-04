<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.10-DE:operational:OP-POL:a.7.10 -->
**ISMS-OP-POL-A.7.10 — Speichermedien**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Speichermedien |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.7.10 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 0.1 |
| **Versionsdatum** | [Date] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | [Date] | ISB | Erste operative Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt von**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Control A.7.10 — Speichermedien
- ISO/IEC 27002:2022 Abschnitt 7.10 — Umsetzungshinweise
- NIST SP 800-88 Rev. 2 — Richtlinien zur Mediensanitisierung (September 2025)
- IEEE 2883:2022 — Standard für die Sanitisierung von Speichermedien
- DIN 66399 — Vernichtung von Datenträgern (Sicherheitsstufen und Medienkategorien)
- Schweizer nDSG (revDSG) — Bundesgesetz über den Datenschutz
- Schweizer DSV (Datenschutzverordnung) — Art. 1–3 (Mindestanforderungen an die Datensicherheit)

**Verwandte Annex-A-Controls**:

| Control | Bezug zu Speichermedien |
|---------|------------------------|
| A.5.9 Inventar von Informationen und zugehörigen Assets | Asset-Register mit Speichermedieninventar |
| A.5.10–11 Akzeptable Nutzung und Rückgabe von Assets | Regeln zur akzeptablen Nutzung und Medienrückgabe beim Beschäftigungsaustritt |
| A.5.12–13 Informationsklassifizierung und -kennzeichnung | Klassifizierungsstufe bestimmt Anforderungen an Handhabung, Speicherung und Entsorgung |
| A.7.6–7–14 Gesicherte Bereiche, Clean Desk, sichere Entsorgung | Physische Sicherheit von Lagerbereichen; Entsorgungsmethoden für medienhaltige Geräte |
| A.8.10 Informationslöschung | Anforderungen an logische Löschung als Ergänzung zur physischen Mediensanitisierung |
| A.8.24 Einsatz von Kryptografie | Verschlüsselungsstandards für den Medienschutz im Ruhezustand und bei der Übertragung |

**Verwandte interne Richtlinien**:

- Richtlinie zur Informationsklassifizierung und -handhabung
- Richtlinie zu gesicherten Bereichen und Medienhandhabung
- Asset-Management-Richtlinie
- Endgerätesicherheitsrichtlinie
- Richtlinie zum Einsatz von Kryptografie

---

# Richtlinie für Speichermedien

## Zweck

Zweck dieser Richtlinie ist es sicherzustellen, dass alle Speichermedien über ihren gesamten Lebenszyklus hinaus sicher verwaltet werden — von der Beschaffung und Registrierung über Nutzung und Transport bis zur Entsorgung oder Wiederverwendung — in Übereinstimmung mit dem Informationsklassifizierungsschema der Organisation und den geltenden regulatorischen Anforderungen.

Diese Richtlinie unterstützt das Schweizer nDSG (revDSG) Art. 8 durch die Implementierung technischer und organisatorischer Massnahmen entsprechend dem Risiko zum Schutz personenbezogener Daten (einschliesslich besonders schützenswerter Personendaten) auf physischen und digitalen Medien. Wo die Organisation Daten von Personen im EU/EWR-Raum verarbeitet, gelten auch DSGVO-Anforderungen. Beide Regelwerke verlangen, dass personenbezogene Daten auf Speichermedien vor der Entsorgung oder Wiederverwendung unwiederbringlich gemacht werden.

Control A.7.10 deckt einen einzelnen Annex-A-Control ab, sein Geltungsbereich erstreckt sich jedoch über den gesamten Medienlebenszyklus: Beschaffung, Registrierung, Nutzung, Datentransfer, Transport, sichere Lagerung, Wiederverwendung und Entsorgung. Diese Richtlinie kombiniert die Richtlinienanforderungen mit operativen Hinweisen, die für ein KMU zur Implementierung und Compliance-Nachweisführung ausreichen.

## Geltungsbereich

Alle Mitarbeitenden, Auftragnehmer und Drittnutzer, die Speichermedien mit Organisationsinformationen handhaben, darauf zugreifen oder dafür verantwortlich sind.

**Betroffene Medientypen**:

- Digitale Wechselmedien: USB-Sticks, externe Festplatten, SD-/microSD-Karten, optische Medien (CD, DVD, Blu-ray)
- Festeinbauten: interne Festplatten (HDD), Solid-State-Drives (SSD), NVMe-Laufwerke
- Sicherungs- und Archivierungsmedien: LTO-Bänder, DAT/DLT-Kassetten, RDX-Kassetten
- Mobilgerätespeicher: Smartphones, Tablets und Geräte mit eingebettetem Speicher
- Cloud- und virtueller Speicher: Cloud-Backup, Cloud-Dateispeicher, virtuelle Maschinen-Disk-Images
- Papier und analoge Medien: Ausdrucke, Mikrofilm, Mikrofiche, fotografische Medien

**Abgedeckte Lebenszyklusphasen**: Beschaffung, Registrierung, Nutzung, Datentransfer, Transport, Lagerung, Wiederverwendung und Entsorgung.

**Nicht im Geltungsbereich**:

- Definition des Informationsklassifizierungsschemas (siehe Richtlinie zur Informationsklassifizierung und -handhabung, A.5.12–13)
- Cloud-Dienstleisterverträge und Drittanbieter-Management (siehe Cloud-Dienste-Richtlinie, A.5.19–23)
- Auswahl kryptografischer Algorithmen und Details des Schlüsselmanagements (siehe Richtlinie zum Einsatz von Kryptografie, A.8.24)

## Grundsatz

ISO/IEC 27001:2022 Annex A.7.10 legt fest:

> *Speichermedien sollten über ihren Lebenszyklus der Beschaffung, Nutzung, des Transports und der Entsorgung gemäss dem Klassifizierungsschema und den Handhabungsanforderungen der Organisation verwaltet werden.*

Speichermedien sollen proportional zur Sensibilität der enthaltenen oder jemals enthaltenen Informationen verwaltet werden. Die höchste Klassifizierungsstufe der jemals auf einem Medium gespeicherten Daten bestimmt die Handhabungs- und Entsorgungsanforderungen, unabhängig davon, ob diese Daten inzwischen gelöscht wurden.

Alle Speichermedien mit Organisationsinformationen müssen registriert, verfolgt und geschützt werden. Die Entsorgung muss Daten mithilfe von Methoden nach NIST SP 800-88 Rev. 2 und DIN 66399, angemessen für den Medientyp und die Informationsklassifizierung, unwiederbringlich machen.

Persönliche Wechselmedien dürfen nicht für Organisationsdaten verwendet werden. Nur von der Organisation genehmigte und verschlüsselte Medien sind zulässig.

---

## Wechselmedienverwaltung

### Genehmigung und Registrierung

Die Nutzung von Wechselspeichermedien muss vor dem Einsatz genehmigt werden:

- Mitarbeitende müssen vor der Nutzung von Wechselspeichermedien für Organisationsdaten die Genehmigung ihres Vorgesetzten einholen. Die Genehmigung muss den zulässigen Anwendungsfall, die Datenklassifizierung und die Dauer angeben (Standard 12 Monate, maximal 24 Monate).
- Alle Wechselmedien müssen im [Asset-Management-System] mit folgenden Angaben registriert werden: Medientyp, Kapazität, Seriennummer oder Asset-Tag, zugewiesener Nutzer, Zweck, maximale Klassifizierungsstufe der zu speichernden Daten und Ablaufdatum der Genehmigung.
- Nur von der Organisation ausgegebene oder genehmigte Wechselmedien dürfen für Organisationsdaten verwendet werden. Private USB-Sticks, externe Festplatten oder andere persönliche Speichergeräte dürfen unter keinen Umständen für VERTRAULICHE oder INTERNE Daten verwendet werden.
- Von der Organisation ausgegebene Wechselmedien müssen über genehmigte Lieferanten aus dem Beschaffungsprozess der Organisation bezogen werden. Nicht genehmigte oder unbekannte Medien dürfen nicht an Organisationssysteme angeschlossen werden.

**Genehmigungslebenszyklus**:
- 30 Tage vor Ablauf: Automatische E-Mail-Erinnerung an Mitarbeitenden und Vorgesetzten aus dem [Asset-Management-System]
- Bei Ablauf: Medienstatus im System auf „Abgelaufen" geändert
- Falls Medien nicht innerhalb von 15 Tagen nach Ablauf erneuert oder zurückgegeben: IT-Betrieb kontaktiert Mitarbeitenden für Rückgabe oder Erneuerung
- Erneuerung: Mitarbeitender stellt Erneuerungsantrag mit weiterhin bestehendem Geschäftsbedarf; Vorgesetzter genehmigt (maximal 24 Monate pro Genehmigung; nach 24 Monaten Bedarf von Grund auf neu begründen)
- Rückgabe: Mitarbeitender gibt Medien an IT-Betrieb zurück; Medien gemäss Entsorgungsverfahren sicher gelöscht (auch wenn Medien neu ausgegeben werden — Löschung zwischen Nutzern); [Asset-Management-System] aktualisiert
- Eskalation bei nicht zurückgegebenen Medien: 15 Tage überfällig → Eskalation zum Vorgesetzten; 30 Tage überfällig → ISB-Eskalation, Medien als „Vermisst" markiert, Verlustuntersuchung eingeleitet; 60 Tage überfällig → als verloren/gestohlen annehmen, Incident-Response gemäss Verlorene-Medien-Verfahren einleiten
- Kennzahlen: Compliance-Rate für Mediengenehmigungen (% rechtzeitig zurückgegeben oder erneuert) — Ziel >95%; überfällige Medien (>15 Tage nach Ablauf) — Ziel <3 Einträge; Berichterstattung im vierteljährlichen Management-Review

### Genehmigte Medientypen

Die Organisation führt eine Liste genehmigter Wechselmedientypen. Als Minimum:

- **USB-Sticks**: Hardware-verschlüsselt, nur von der Organisation ausgegeben (z.B. [Verschlüsseltes USB-Modell]). Software-Verschlüsselung ist für INTERNE Daten akzeptabel, wo hardware-verschlüsselte Geräte nicht verfügbar sind, mit ISB-Genehmigung und folgenden Ausgleichsmassnahmen:
  - VERTRAULICHE Daten erfordern Hardware-Verschlüsselung — keine Ausnahmen für reine Software-Verschlüsselung
  - Maximale Ausnahmedauer: 6 Monate (verlängerbar mit ISB-Genehmigung)
  - Genehmigte Software-Tools: BitLocker To Go (Windows, AES-256), FileVault (macOS, AES-256), VeraCrypt (plattformübergreifend, AES-256)
  - Starkes Passwort obligatorisch: Mindestens 16 Zeichen, gespeichert im [Passwort-Manager]
  - Medien müssen vor der ersten Nutzung verschlüsselt werden (nicht nach bereits erfolgter Datenschreibung — Risiko verbleibender unverschlüsselter Daten)
  - Erweiterte Überwachung: Nutzung software-verschlüsselter Medien protokolliert, monatliche Überprüfung der Zugriffsmuster
  - Vierteljährliche Neugenehmigung: Nutzer bestätigt alle 3 Monate den Geschäftsbedarf; bei wegfallendem Bedarf Medienrückgabe zur sicheren Entsorgung
  - Migration zu Hardware-Verschlüsselung: Software-verschlüsselte Ausnahmen werden schrittweise abgelöst, sobald hardware-verschlüsselte Medien verfügbar sind (Ziel: alle INTERNEN Daten auf Hardware-Verschlüsselung innerhalb von 12 Monaten)
- **Externe Festplatten**: AES-256-hardware-verschlüsselte Modelle von genehmigten Lieferanten.
- **Optische Medien (CD/DVD/Blu-ray)**: Von der Organisation ausgegeben, beschriftet mit Klassifizierung, Asset-Referenz, Schreibdatum, Inhaltsbeschreibung und Aufbewahrungsablaufdatum. Einmal-beschreibbare Medien (CD-R, DVD-R, BD-R) obligatorisch für: VERTRAULICHE Archivierung (Rechtsdokumente, Prüfungsunterlagen, Finanzunterlagen), Beweissicherung (forensische Images, Incident-Beweise, rechtliche Aufbewahrungspflichten) und Langzeitaufbewahrung (>5 Jahre). Wiederbeschreibbare Medien (CD-RW, DVD-RW, BD-RE) nur für temporäre INTERNE Datenübertragung und Test-/Entwicklungsdaten zulässig (maximal 12 Monate, dann sicher vernichtet). Lagerung: Jewel-Cases oder Slim-Cases (nicht Papierhüllen — Kratzerrisiko), vertikale Ausrichtung (nicht flach gestapelt — Verformungsrisiko), kühle trockene Umgebung ohne Sonneneinstrahlung. Migration auf neue Medien bei 5-Jahres-Marke für Langzeitaufbewahrungsdaten einplanen.
- **SD-/microSD-Karten**: Nur für spezifische genehmigte Zwecke zulässig (z.B. Kameras, eingebettete Systeme). Müssen verschlüsselt werden, sofern das Gerät dies unterstützt.

Unverschlüsselte Wechselmedien dürfen nicht für VERTRAULICHE Daten verwendet werden. Ausnahmen erfordern dokumentierte ISB-Genehmigung mit Ausgleichsmassnahmen und einer Zeitbegrenzung von höchstens 6 Monaten.

### Pflege der genehmigten Medienliste

Die genehmigte Medienliste wird regelmässig überprüft und gepflegt:

- **Jährliche Überprüfung**: IT-Betrieb und ISB überprüfen die genehmigte Medienliste im 4. Quartal
- **Anlassbasierte Überprüfung**: Bei Verfügbarkeit neuer Medientechnologien, Entdeckung einer Sicherheitsschwachstelle in einem aktuell genehmigten Modell oder bei Bekanntwerden eines eingestellten Modells

Überprüfungskriterien:
- Verschlüsselungsstandard aktuell (AES-256 Minimum für VERTRAULICH, AES-128 Minimum für INTERN)
- Hardware-Verschlüsselung bevorzugt (FIPS 140-2 Level 2 oder höher für VERTRAULICHE Medien)
- Hersteller-Supportstatus (aktiver Support, Sicherheitsupdates verfügbar)
- Kosteneffizienz (Preis pro GB, Sammelbestellung verfügbar)
- Kompatibilität mit Endgeräten der Organisation (Windows, macOS, Linux)

Genehmigungsverfahren: IT-Betrieb schlägt Ergänzungen oder Streichungen mit technischer Bewertung vor; ISB genehmigt Änderungen; Einkauf aktualisiert die Vorzugslieferantenliste; genehmigte Medienliste im Intranet veröffentlicht und an alle Mitarbeitenden kommuniziert. Liste muss Versionsdatum und nächstes Überprüfungsdatum enthalten.

### Vierteljährliches Medien-Audit

Ein risikobasiertes Audit registrierter Wechselmedien wird vierteljährlich durchgeführt:

**Audit-Umfang nach Risikostufe**:

| Risikostufe | Kriterien | Vierteljährliche Stichprobe | Jährliche Abdeckung |
|-------------|-----------|----------------------------|---------------------|
| **Hoch** | Medien, die VERTRAULICHE Daten gespeichert haben (aktuell oder historisch); regelmässig extern transportierte Medien; Führungskräften oder privilegierten Nutzern zugewiesene Medien | 100% Verifizierung | 100% pro Quartal |
| **Mittel** | Medien nur mit INTERNEN Daten; nur bürobasierte Nutzung | 50% rotierende Stichprobe | 100% über 2 Quartale |
| **Niedrig** | Medien nur mit ÖFFENTLICHEN Daten; Medien in Langzeit-Sicherheitsarchiv | 25% rotierende Stichprobe | 100% jährlich |

**Audit-Verfahren**:
1. Stichprobenliste aus dem [Asset-Management-System] nach Risikostufe generieren
2. Physische Verifizierung: Standort, Inhaber, Verschlüsselungsstatus und Seriennummer mit Eintrag abgleichen
3. Verschlüsselungs-Stichprobe: 10% der stichprobenartig geprüften Medien zufällig testen (Zugriffsversuch ohne Passwort/Verschlüsselungsschlüssel)
4. Ergebnisse dokumentieren: Abstimmungsbericht mit Befunden, Abweichungen und Folgemassnahmen

**Eskalation bei Befunden**:
- Fehlende Hochrisiko-Medien: Sofortige Eskalation zum ISB (gleichentags); als verloren/gestohlen annehmen; Datenschutzverletzungsbewertung gemäss Verlorene-Medien-Incident-Response-Verfahren einleiten
- Fehlende Mittelrisiko-Medien: Eskalation innerhalb von 2 Arbeitstagen; Untersuchung durch IT-Betrieb
- Fehlende Niedrigrisiko-Medien: Dokumentieren und innerhalb von 5 Arbeitstagen nachverfolgen

**Jährliches Gesamt-Audit**: 100% Verifizierung ALLER Medien (alle Risikostufen) einmal jährlich durchgeführt (4. Quartal oder wie vom ISB geplant).

Audit-Ergebnisse sind zu dokumentieren und 12 Monate aufzubewahren.

---

## Anforderungen an die Mediennutzung

### Datentransfer auf Wechselmedien

- Transfer VERTRAULICHER Daten auf Wechselmedien erfordert eine dokumentierte Managementgenehmigung vor dem Transfer. Der Genehmigungsnachweis muss die Geschäftsbegründung, den Empfänger und das voraussichtliche Rückgabedatum enthalten.
- Alle auf Wechselmedien übertragenen Daten müssen verschlüsselt sein. Für VERTRAULICHE Daten ist AES-256-Verschlüsselung (Hardware oder Software) obligatorisch. Für INTERNE Daten ist AES-128 oder stärker erforderlich.
- Transferprotokolle müssen für VERTRAULICHE Daten geführt werden mit: Datum, Nutzer, Medienkennung, Datenbeschreibung und Empfänger.
- Daten müssen von Wechselmedien entfernt werden, sobald sie für den genehmigten Zweck nicht mehr benötigt werden.

### Zugriffskontrolle und Schutz

- Medien mit VERTRAULICHEN Daten müssen passwortgeschützt oder mit starker Authentifizierung verschlüsselt sein (PIN, Passphrase oder biometrische Entsperrung am Gerät).
- Medien dürfen zu keinem Zeitpunkt unbeaufsichtigt gelassen werden. Bei Nichtgebrauch müssen Medien in verschlossener, der Klassifizierung angemessener Aufbewahrung gesichert sein.
- Wechselmedien dürfen nicht an nicht vertrauenswürdige oder öffentliche Systeme angeschlossen werden.
- Medieninhalte müssen vor dem Öffnen oder Übertragen auf Organisationssysteme durch [Endgeräteschutz-Tool] auf Malware gescannt werden. Auto-Run und Auto-Play müssen über die Richtlinie des [Endgeräte-Management-Tools] auf allen Endgeräten deaktiviert sein.

### Steuerung von USB-Ports und Wechselmedien

- USB-Ports und Wechselmedienzugriff müssen zentral über das [Endgeräte-Management-Tool] verwaltet werden (z.B. Gruppenrichtlinie, MDM oder Endgeräteschutzplattform).
- Standardrichtlinie: USB-Massenspeichergeräte auf allen Endgeräten gesperrt. Ausnahmen werden pro Geräteseriennummer nur für registrierte, verschlüsselte Medien gewährt.
- Alle USB-Verbindungsereignisse müssen von der Endgeräteschutzplattform protokolliert werden. Protokolle sind mindestens 12 Monate aufzubewahren.

**USB-Port-Steuerung nach Workstation-Typ**:

| Workstation-Typ | USB-Massenspeicher | Genehmigte Medien | Protokollierung |
|-----------------|-------------------|-------------------|-----------------|
| **Standard-Büro-Desktop/-Laptop** | Standardmässig gesperrt | Ausnahme per Seriennummer (nur registrierte verschlüsselte Medien) | Alle Verbindungsversuche protokolliert |
| **Entwickler-Workstation** | Zulässig nur für registrierte verschlüsselte Medien | Von Organisation ausgegebene verschlüsselte USB + genehmigte Entwicklungstools (Yubikey, Hardware-Sicherheitsschlüssel) | Alle Verbindungen protokolliert |
| **Führungskraft-/Mobilarbeiter-Laptop** | Zulässig nur für registrierte verschlüsselte Medien | Von Organisation ausgegebene verschlüsselte USB | Alle Verbindungen protokolliert; vierteljährliche Zugriffsüberprüfung |
| **Kiosk-/öffentliches System** | Gesperrt (keine Ausnahmen) | Keine | Alle Verbindungsversuche protokolliert und alarmiert |
| **Server-/Infrastruktur** | Gesperrt (keine Ausnahmen ausser durch autorisierten IT-Betrieb bei Wartung) | Nur genehmigte Rettungs-/Diagnosemedien (verschlüsselt, möglichst schreibgeschützt) | Alle Verbindungen protokolliert und alarmiert |

Implementierung über [Endgeräte-Management-Tool]: Gerätekontrollrichtlinie mit Whitelist nach Geräteseriennummer (nicht Gerätetyp); unterschiedliche Richtliniengruppen pro Workstation-Typ (AD-gruppen- oder gerätetagbasiert). Alarm bei: nicht autorisierten USB-Verbindungsversuchen, USB-Verbindungen ausserhalb der Geschäftszeiten, Massendatenübertragungen (>1 GB), mehrfachen fehlgeschlagenen Authentifizierungsversuchen auf verschlüsselten Medien.

**Temporäre Ausnahme** (Besucher/Auftragnehmer, Kurzzeitbedarf <7 Tage): Genehmigung durch IT-Betrieb + Vorgesetzten; maximal 7 Tage; erweiterte Protokollierung und tägliche Überprüfung; Ausnahme wird bei Ablauf automatisch aus der Whitelist entfernt.

---

## Transport von Speichermedien

### Anforderungen an den sicheren Transport

Beim Transport von Speichermedien gelten folgende Anforderungen:

**Kurier- und Postsendungen**:

- VERTRAULICHE Medien dürfen nur durch genehmigte Sicherheitskurierdienste mit Sendungsverfolgung und Empfangsbestätigung transportiert werden. Standardpostdienste dürfen für VERTRAULICHE Daten nicht verwendet werden.
- INTERNE Medien sollten mittels verfolgbarer Kurierdienste transportiert werden. Standardpostdienste sind mit eingeschriebener/verfolgter Sendung zulässig.
- Manipulationssichere Verpackung ist für alle VERTRAULICHE Daten enthaltenden Medien zu verwenden. Der Empfänger muss die Verpackung auf Manipulationszeichen prüfen und etwaige Auffälligkeiten sofort melden.
- Begleitdokumente zur Beweiskette müssen alle Sendungen VERTRAULICHER Medien begleiten (siehe Abschnitt Beweiskette unten).

**Persönlicher Transport (Handgepäck)**:

- Medien müssen bei Reisen im Handgepäck mitgeführt werden (niemals im aufgegebenem Gepäck).
- Medien müssen verschlüsselt sein und dürfen während des Transports zu keinem Zeitpunkt unbeaufsichtigt sein.
- Transport durch Hochrisikogebiete (öffentliche Verkehrsknotenpunkte, Konferenzen, ausländische Rechtsordnungen ohne angemessenen Datenschutz) sollte vermieden werden, wo Alternativen bestehen. Falls unvermeidbar, sind zusätzliche Verschlüsselungs- und Zugangskontrollmassnahmen anzuwenden.

**Alternative elektronische Übertragung**:

Wo möglich, sollte verschlüsselte elektronische Übertragung (z.B. sichere Dateifreigabe, SFTP, verschlüsselte E-Mail) dem physischen Medientransport vorgezogen werden. Physischer Transport sollte nur verwendet werden, wenn elektronische Übertragung unpraktisch oder verboten ist.

**Umweltschutz beim Transport**:

Speichermedien (insbesondere Magnetbänder und Festplatten) sind während des Transports empfindlich gegenüber Temperatur, Luftfeuchtigkeit und physischen Stössen:

- **Sommertransport (Umgebungstemperatur >30 °C)**: Isolierte Transportbehälter verwenden; Medien nicht in Fahrzeugen zurücklassen; Same-Day- oder Overnight-Lieferung bevorzugen, um Transitzeit zu minimieren
- **Wintertransport (Umgebungstemperatur <5 °C)**: Isolierte Transportbehälter verwenden; Medien vor Nutzung bei Raumtemperatur akklimatisieren (mindestens 2 Stunden) bei Exposition gegenüber Frost
- **Stosssicherung**: Antistatische Luftpolsterfolie + starrer Aussencontainer (keine gepolsterte Hülle); Aufschrift „Fragil — Elektronische Medien" auf allen Seiten; „Diese Seite oben" für Bandkassetten kennzeichnen
- **Feuchtigkeitsschutz**: Trockenmittelpakete (Silicagel) in Transportbehältern für feuchte Klimata oder schnelle Feuchtigkeitswechsel verwenden

| Medientyp | Temperaturtoleranz (nicht in Betrieb) | Stossempfindlichkeit | Empfohlene Verpackung |
|-----------|---------------------------------------|---------------------|----------------------|
| Magnetband (LTO, DAT) | –40 bis 65 °C | Hoch (mechanische Teile) | Antistatisch + starres Gehäuse + „Fragil"-Aufschrift |
| HDD | –40 bis 70 °C | Hoch (bewegliche Teile) | Antistatisch + Schaumstoffpolsterung + starres Gehäuse |
| SSD / Flash | –40 bis 85 °C | Niedrig (keine beweglichen Teile) | Antistatisch + Standardverpackung |
| Optisch (CD/DVD) | 5 bis 50 °C | Niedrig | Jewel-Case + gepolsterter Versandumschlag |

Kurieranweisungen für VERTRAULICHE Medien: Handhabungsanweisungen an Kurier übergeben; Unterschrift bei Lieferung erforderlich (kein „Vor Tür abstellen"); Sendung in Echtzeit verfolgen; Untersuchung bei Lieferverzögerung >24 Stunden. Empfänger prüft Verpackung bei Erhalt auf Schäden und meldet physische Schäden sofort.

### Beweiskette

Alle Übergaben von VERTRAULICHE Daten enthaltenden Medien zwischen Personen, Standorten oder Organisationen sind zu dokumentieren mit:

- Datum und Uhrzeit der Übergabe
- Identität der übergebenden Partei (Name, Funktion)
- Identität der empfangenden Partei (Name, Funktion, Organisation bei externer Partei)
- Medienkennung (Asset-Tag, Seriennummer)
- Inhaltsbeschreibung (Klassifizierungsstufe, allgemeine Datenkategorie — nicht die Daten selbst)
- Empfangsbestätigung (Unterschrift oder elektronische Bestätigung)
- Voraussichtliches Rückgabedatum (sofern zutreffend)

Beweiskettenunterlagen sind 7 Jahre aufzubewahren.

**Beweiskette bei logischem Datentransfer**: Wenn Daten elektronisch statt über physische Medien übertragen werden, ist die Beweiskette ebenfalls zu dokumentieren:
- Erforderliche Dokumentation: Datum/Uhrzeit, Absender, Empfänger, Dateinamen/-grössen, Klassifizierung, Übertragungsmethode (E-Mail/SFTP/sichere Dateifreigabe), Verschlüsselungsmethode (z.B. „AES-256 über [Tool]"), Link-Ablauf (bei linkbasierter Übertragung)
- Protokollierung: Automatische Erfassung über [Sichere-Dateifreigabe-Tool]-/[E-Mail-Gateway]-Audit-Protokolle wo verfügbar
- Aufbewahrung: 12 Monate (Protokolle); 7 Jahre (VERTRAULICHE Übertragungsunterlagen)

*Bevorzugte Übertragungsmethode nach Szenario*:

| Szenario | Bevorzugte Methode | Begründung |
|----------|--------------------|------------|
| Datei <100 MB | Verschlüsselte E-Mail oder sichere Dateifreigabe (z.B. [Tool]) | Schneller; kein physisches Medienrisiko |
| Datei 100 MB–10 GB | Sichere Dateifreigabe mit Ablauflink | Vermeidet E-Mail-Grössenbeschränkungen; nachvollziehbar |
| Datei >10 GB | Verschlüsselter USB per Kurier oder SFTP/Cloud-Sync | Physische Medien praktisch für grosse Übertragungen |
| Archivierung/Backup (TB-Massstab) | Verschlüsseltes Band per Kurier | Kostengünstigste Lösung für Massenarchivierung |

Bei VERTRAULICHEN logischen Übertragungen: Ende-zu-Ende-Verschlüsselung obligatorisch (vor Upload/Versand verschlüsselt, Empfänger entschlüsselt). Linkbasierte Freigabe: Ablaufende Links (maximal 7 Tage), passwortgeschützt, Download-Benachrichtigung an Absender. E-Mail: Verschlüsselter Anhang (GPG/PGP oder [Sicheres E-Mail-Tool]), Empfängeridentität vor dem Versand verifiziert.

---

## Lagerungsanforderungen

### Physische Lagerung nach Klassifizierung

Speichermedien müssen in Bedingungen gelagert werden, die sowohl der Sensibilität der Informationen als auch der physischen Integrität des Mediums angemessen sind:

| Klassifizierung | Physische Lagerung | Verschlüsselung | Zugangskontrolle | Umweltanforderungen |
|-----------------|-------------------|-----------------|------------------|---------------------|
| **VERTRAULICH** | Verschlossener Tresor oder gesicherter Schrank in eingeschränktem Bereich | Obligatorisch — AES-256 (gemäss Kryptografierichtlinie) | Nur namentlich genannte Personen; Zugang protokolliert | Temperatur 15–25 °C; 30–60% rel. Luftfeuchtigkeit; fernab von Magnetfeldern und direkter Sonneneinstrahlung |
| **INTERN** | Abschliessbarer Schrank oder abschliessbare Schublade | Empfohlen — AES-128 oder stärker | Autorisierte Mitarbeitende mit berechtigtem Geschäftsbedarf | Normale Bürobedingungen; fernab von Umweltgefahren |
| **ÖFFENTLICH** | Standardmässige Büroaufbewahrung | Optional | Allgemeiner Zugang; physische Sicherheit aufrechterhalten | Normale Bürobedingungen |

### Lagerung von Backup-Medien

- Backup-Bänder und -Kassetten müssen an einem anderen physischen Ort als die gesicherten Systeme gelagert werden (extern oder in einer separaten Brandschutzzone).
- Backup-Medien müssen mit starker Hersteller-Verschlüsselung oder einem von der Organisation genehmigten Verschlüsselungs-Tool verschlüsselt sein.
- Backup-Medien müssen im Medieninventar erfasst und demselben vierteljährlichen Audit unterzogen werden wie Wechselmedien.

### Aufbewahrung und Ablauf

- Medien sind gemäss dem Datenaufbewahrungsplan der Organisation aufzubewahren. Aufbewahrungsfristen werden nach Datentyp, regulatorischen Anforderungen und Geschäftsbedarf festgelegt.
- Nach Ablauf der Aufbewahrungsfrist für Daten auf einem Medium ist das Medium gemäss dem Entsorgungsabschnitt dieser Richtlinie zu sanitisieren oder zu vernichten.
- Backup-Bänder und Cloud-Snapshots müssen dokumentierte Entsorgungs- oder Löschauslöser haben, die mit dem Aufbewahrungsplan übereinstimmen. „Unbegrenzte" Aufbewahrung ist ohne dokumentierte ISB-Genehmigung und jährliche Überprüfung nicht zulässig.

**Backup-Medien-Aufbewahrungsrahmen** — Zweistu-Ansatz zur Trennung von operativer Wiederherstellung und rechtlicher/Compliance-Aufbewahrung:

*Operative Backup-Aufbewahrung* (für Disaster Recovery und operative Wiederherstellung):
- Tägliche Backups: 30 Tage
- Wöchentliche Backups: 90 Tage (3 Monate)
- Monatliche Backups: 12 Monate
- Jährliche Backups: 3 Jahre (langfristiges Wiederherstellungs-Sicherheitsnetz)

*Rechtliche/Compliance-Datenaufbewahrung* (für regulatorische, rechtliche und Audit-Zwecke):
- Getrennt von operativen Backups — strukturierten Archivspeicher verwenden, nicht bandbasierte vollständige System-Backups
- Finanzunterlagen: 10 Jahre (Schweizer OR Art. 958f)
- Personalunterlagen: 10 Jahre
- Kundendaten: Gemäss Vertrag oder anwendbaren Vorschriften

*Backup-Löschauslöser*:

| Backup-Typ | Löschauslöser | Methode |
|------------|---------------|---------|
| Tägliche Backups >30 Tage | Automatische Löschung durch Backup-Tool | Aufbewahrungsrichtlinie in [Backup-Tool], protokolliert |
| Wöchentliche Backups >90 Tage | Automatische Löschung durch Backup-Tool | Aufbewahrungsrichtlinie in [Backup-Tool] |
| Monatliche Backups >12 Monate | Manuelle Überprüfung + Genehmigung des IT-Betriebsleiters | Vierteljährliche Überprüfung; Löschung mit unterzeichneter Genehmigung |
| Jährliche Backups >3 Jahre | Manuelle Überprüfung + ISB-Genehmigung | Jährliche Überprüfung; Löschung mit unterzeichneter Genehmigung |
| Cloud-Snapshots (verwaist) | Vierteljährliche Identifizierung + 90-tägige Kulanzfrist | Lifecycle-Richtlinie; verwaiste Snapshots vierteljährlich überprüfen |

*Ausnahme bei rechtlicher Aufbewahrungspflicht*: Bei Daten unter rechtlicher Aufbewahrungspflicht (Rechtsstreit, Untersuchung, Audit) ist die Backup-Löschung für betroffene Daten auszusetzen. Aufbewahrungspflicht im [Asset-Management-System] mit Haltegrund, Startdatum und Überprüfungsdatum dokumentiert. Wiederaufnahme der Löschung erfordert Genehmigung von Recht/Compliance.

---

## Entsorgung von Speichermedien

### Entsorgungsgrundsätze

Entsorgung und Sanitisierung müssen sicherstellen, dass Informationen nicht wiederhergestellt werden können, unter Verwendung von für den Medientyp und die höchste jemals auf dem Medium gespeicherte Klassifizierung geeigneten, von der Organisation genehmigten Methoden.

Die Organisation übernimmt den NIST SP 800-88 Rev. 2-Rahmen für die Mediensanitisierung, abgestimmt auf die technischen Empfehlungen von IEEE 2883:2022 für die Speichergerätesanitisierung:

| Sanitisierungsstufe | Methode | Beschreibung | Anwendungsfall |
|---------------------|---------|--------------|----------------|
| **Löschen (Clear)** | Logisches Überschreiben | Überschreibt nutzerzugängliche Speicherorte mit nicht sensiblen Daten mittels Standard-Lese-/Schreibbefehlen. Schützt vor einfachen, nicht-invasiven Datenwiederherstellungstechniken. | ÖFFENTLICHE Daten; interne Wiederverwendung von geringempfindlichen Geräten |
| **Bereinigen (Purge)** | Kryptografische Löschung, Block-Erase oder Firmware-Befehle | Macht Datenwiederherstellung mit modernsten Labortechniken undurchführbar. Umfasst kryptografische Löschung (Zerstörung von Verschlüsselungsschlüsseln bei selbstverschlüsselnden Laufwerken) und herstellerspezifische Secure-Erase-Befehle gemäss IEEE 2883. | INTERNE Daten; interne Wiederverwendung; externe Übergabe von zuvor INTERNEN Geräten |
| **Vernichten (Destroy)** | Physische Vernichtung | Macht Medien durch Schreddern, Zerlegung, Pulverisierung oder Verbrennung physisch unbrauchbar. Datenwiederherstellung ist unabhängig vom Aufwand nicht möglich. | VERTRAULICHE Daten; alle externen Entsorgungen von Medien mit sensiblen Daten; End-of-Life für Medien, bei denen Sanitisierung nicht verifiziert werden kann |

### Entsorgungsanforderungen nach Klassifizierung

| Klassifizierung | Erforderliches Ergebnis | NIST-Mindeststufe | Verifizierung |
|-----------------|------------------------|-------------------|---------------|
| **VERTRAULICH** | Durch keinerlei Mittel wiederherstellbar, einschliesslich modernster Labortechniken | Vernichten (oder Bereinigen nur bei interner Wiederverwendung mit verifizierter kryptografischer Löschung) | Vernichtungszertifikat vom genehmigten Anbieter; bezeugte Vernichtung bei hochsensiblen Daten |
| **INTERN** | Ohne Spezialtechnik nicht wiederherstellbar | Bereinigen | Verifizierung erfolgreicher Löschung mit Tool-Ausgabeprotokoll dokumentiert |
| **ÖFFENTLICH** | Standardlöschung mit dokumentierter Entsorgung | Löschen | Dokumentation der Entsorgung im Asset-Register |

### Entsorgungsmethoden nach Medientyp

| Medientyp | VERTRAULICH | INTERN | ÖFFENTLICH |
|-----------|-------------|--------|------------|
| **Festplatten (HDD)** | Physische Vernichtung: Schreddern oder Degaussing + Schreddern | Bereinigen: Hersteller Secure Erase (ATA Secure Erase, NVMe Sanitize) oder Einzel-Pass-Überschreibung mit Verifizierung, oder physische Vernichtung | Formatieren und neuinstallieren |
| **Solid-State-Drives (SSD/NVMe)** | Physische Vernichtung: Schreddern oder Zerlegung | Kryptografische Löschung oder Hersteller Secure Erase gemäss IEEE 2883; physische Vernichtung falls Krypto-Erase nicht verfügbar | Secure-Erase-Befehl |
| **USB-Sticks / SD-Karten** | Physische Vernichtung: Schreddern | Sicheres Überschreiben oder physische Vernichtung | Formatieren |
| **LTO / Backup-Bänder** | Physische Vernichtung: Schreddern oder Verbrennung | Degaussing + Überschreiben oder physische Vernichtung | Degaussing oder Überschreiben |
| **Optische Medien (CD/DVD/Blu-ray)** | Physische Vernichtung: Schreddern oder Verbrennung | Physische Vernichtung: Schreddern | Physische Vernichtung oder Unlesbarkeitsbehandlung |
| **Mobilgeräte** | Physische Vernichtung der Speicherkomponenten | Werksreset + Verifizierung der kryptografischen Löschung | Werksreset |
| **Drucker / Kopierer (interne HDD/SSD)** | Entfernung + Vernichtung interner Speicher | Entfernung interner Speicher + Sicherlöschung | Speicher löschen / Werksreset |
| **Cloud / Virtueller Speicher** | Kryptografische Löschung + Löschbestätigung + Verlassen auf SOC-2-/ISO-27001-Zertifizierung des Anbieters | Kryptografische Löschung + Löschbestätigung vom Anbieter | Standardlöschung über Provider-API/Konsole |

**Wichtiger Hinweis zu SSD und Flash-Medien**: Herkömmliche Überschreibmethoden sind für SSDs und Flash-Speicher aufgrund von Wear-Levelling, Overprovisioning und Write Amplification unzuverlässig. Für SSD- und Flash-basierte Medien sind kryptografische Löschung (bei Unterstützung durch selbstverschlüsselnde Laufwerke) oder vom Hersteller bereitgestellte Secure-Erase-Befehle gemäss IEEE 2883:2022 die genehmigten Bereinigungsmethoden. Wo keines verfügbar oder verifizierbar ist, ist physische Vernichtung erforderlich.

**HDD-Überschreibung — NIST SP 800-88 Rev. 2-Hinweis**: NIST SP 800-88 Rev. 2 (September 2025) bestätigt, dass eine Einzel-Pass-Überschreibung für moderne Festplatten (Fertigung nach 2001) ausreicht. Mehr-Pass-Überschreibung (z.B. veraltete DoD 5220.22-M 3-Pass- oder 7-Pass-Methoden) ist nicht mehr erforderlich und bietet bei modernen Laufwerken keinen zusätzlichen Sicherheitsvorteil. Genehmigte Bereinigungsmethoden für HDDs: Hersteller Secure Erase (ATA Secure Erase, NVMe Sanitize) oder Einzel-Pass-Überschreibung mit Verifizierung unter Verwendung eines genehmigten Tools (z.B. DBAN, nwipe, shred oder dd). Verifizierung umfasst Tool-Abschlussbericht mit Seriennummer, Zeitstempel und Bestanden/Nicht-bestanden-Status.

**Degaussing-Anforderungen für magnetische Medien**: Die Effektivität des Degaussings hängt von der magnetischen Feldstärke des Degaussers relativ zur Koerzitivkraft des Mediums ab. Der Degausser muss für den zu sanitisierenden Medientyp ausgelegt sein:

| Medientyp | Koerzitivkraftbereich | Minimale Degausser-Leistung |
|-----------|----------------------|----------------------------|
| LTO-7/8/9-Bänder | ~2.800–3.200 Oe | ≥7.000 Gauss (NSA/CSS EPL-gelistet empfohlen) |
| LTO-5/6-Bänder | ~2.500–2.800 Oe | ≥5.000 Gauss |
| DAT/DLT-Kassetten | ~1.500–2.000 Oe | ≥5.000 Gauss |
| Festplatten (veraltet, vor SSD) | ~2.000–5.000 Oe | ≥9.000 Gauss für zuverlässige Löschung |

Degausser-Validierung: Degaussing-Geräte müssen jährlich (oder gemäss Herstellerempfehlungen) getestet werden, um zu verifizieren, dass die Feldstärke innerhalb der Spezifikation liegt. Testergebnisse sind aufzubewahren. SSDs und Flash-Medien können nicht degaussiert werden — Degaussing hat keine Wirkung auf Festkörperspeicher.

**Entsorgung von Cloud- und virtuellem Speicher**: Grosse Cloud-Anbieter (AWS, Azure, GCP) stellen keine individuellen Vernichtungszertifikate für virtuellen Speicher aus. Bei der Cloud-Entsorgung muss die Organisation:
- Volumes/Objekte über Cloud-Konsole oder API löschen und Verschlüsselungsschlüssel aus KMS löschen (kryptografische Löschung)
- Löschbestätigung als Nachweis aufbewahren (Screenshot oder API-Audit-Protokoll mit Volume-ID und Lösch-Zeitstempel)
- Sich auf die SOC-2-Typ-II-/ISO-27001-Zertifizierung des Anbieters verlassen, die bestätigt, dass gelöschter Speicher gemäss NIST SP 800-88 vor Hardware-Wiederverwendung oder -entsorgung sanitisiert wird
- Verlassen auf Anbieterzertifizierung im Entsorgungsnachweis dokumentieren (z.B. „AWS SOC 2 Typ II vom [Date]")
- Bei höchstsensiblen VERTRAULICHEN Daten: Client-seitige Verschlüsselung als Minderungsmassnahme verwenden (Organisation kontrolliert Schlüssel, nicht Anbieter) — selbst wenn Anbieter Löschung versäumt, bleiben Daten verschlüsselt
- Geschäftsleitung bestätigt jährlich im Management-Review das Verlassen auf anbieterzertifizierte Löschprozesse

### Interne Wiederverwendung

Vor der Wiederverwendung von Medien innerhalb der Organisation:

- Alle Daten müssen mit einer für die vorherige Datenklassifizierung geeigneten, genehmigten Methode sicher gelöscht werden.
- Die Löschung muss mit dem [Sicherlösch-Tool] verifiziert und das Verifizierungsprotokoll aufbewahrt werden.
- Medien müssen auf physische Integrität geprüft werden. Beschädigte Medien dürfen nicht wiederverwendet, sondern müssen vernichtet werden.
- Datensätze im [Asset-Management-System] müssen mit neuer Zuweisung, Datum und Sanitisierungsnachweis aktualisiert werden.
- Lizenzierte Software muss gemäss Lizenzbedingungen übertragen oder entfernt werden.

### Externe Entsorgung

Extern zu entsorgende Medien müssen:

- Alle Daten auf erforderlichem Niveau sicher gelöscht haben oder physisch vernichtet sein.
- Nur durch genehmigte Vernichtungsanbieter entsorgt werden.
- Mit für 7 Jahre aufzubewahrenden Vernichtungszertifikaten dokumentiert sein.
- Niemals mit wiederherstellbaren Daten verkauft, gespendet oder entsorgt werden.

Geräte, die VERTRAULICHE Daten gespeichert haben, dürfen nicht extern wiederverwendet werden. Speichermedien müssen vor jeder externen Weitergabe physisch vernichtet werden.

### Vernichtungszertifikate

Für alle durch externen [Vernichtungsanbieter] oder Speziallieferanten vernichteten Medien:

- Ein Vernichtungszertifikat ist für jeden Stapel oder jeden einzelnen vernichteten Gegenstand einzuholen.
- Zertifikate müssen auf individuelle Seriennummern oder Asset-Tags verweisen, nicht nur auf Stapelkennungen.
- Vernichtungsmethode und Compliance-Standard (z.B. NIST SP 800-88 Destroy, DIN 66399-Stufe) müssen angegeben sein.
- Zertifikate müssen gegen die Übergabedokumentation abgeglichen werden, um sicherzustellen, dass alle Gegenstände erfasst sind. Abweichungen sind sofort zu eskalieren und als Sicherheitsereignis zu protokollieren.
- Zertifikate sind mit dem Entsorgungsnachweis abzulegen und 7 Jahre aufzubewahren.

---

## Papierdokumente und physische Medien

### Handhabung von Papierdokumenten

- Papierdokumente sind gemäss der Richtlinie zur Informationsklassifizierung und -handhabung zu klassifizieren und zu handhaben.
- VERTRAULICHE Dokumente müssen in verschlossenen Schränken oder Tresoren aufbewahrt werden, wenn sie nicht unmittelbar in Verwendung sind:
  - **Abschliessbarer Aktenschrank**: Geeignet für standardmässige VERTRAULICHE Geschäftsdokumente (Verträge, Finanzunterlagen, Kundenlisten) bis ca. 1 Schublade (~1.000 Blatt). Metallschrank mit Schlüssel- oder Kombinationsschloss, soweit möglich am Boden/an der Wand befestigt.
  - **Abschliessbarer Tresor**: Erforderlich für Geschäftsgeheimnisse, M&A-Dokumente, rechtlich privilegierte Materialien und hochsensible Personendaten (Gesundheitsunterlagen von Führungskräften, Ergebnisse von Hintergrundüberprüfungen). Feuerfester Tresor (mindestens 1-Stunden-Widerstand), Kombinations- oder elektronisches Schloss, Zugang auf 2–3 namentlich genannte Personen beschränkt.
  - **Dokumententresor/-sicherheitsraum**: Erforderlich für grossvolumige VERTRAULICHE Archivlagerung (>10 Dateiboxen). Dedizierter verschlossener Raum mit Kartenzugangskontrolle, CCTV und Umweltsteuerung (Feuerlöschung, Luftfeuchtigkeit).
- Dokumente müssen sofort nach dem Drucken, Kopieren und Faxen entnommen werden. Sicherer Druckauftrag (Pull-Printing) sollte wo verfügbar implementiert werden.
- Clean-Desk-Richtlinie ist jederzeit einzuhalten (siehe Richtlinie zu gesicherten Bereichen und Medienhandhabung, A.7.6–7–14).

### Vernichtung von Papierdokumenten

Papiervernichtung muss DIN-66399-Normen entsprechen. DIN 66399 definiert Sicherheitsstufen mit einem Buchstabenpräfix für die Medienkategorie (P = Papier) und einer Zahl für die Sicherheitsstufe (1–7, höher = kleinere Partikel):

| Klassifizierung | DIN-66399-Stufe | Partikelgrösse | Methode |
|-----------------|-----------------|----------------|---------|
| **VERTRAULICH** | P-4 Minimum (P-5 empfohlen für sensible Personendaten) | P-4: max. 160 mm², Breite max. 6 mm | Kreuzschnittschreddern |
| **INTERN** | P-3 Minimum | P-3: max. 320 mm², Breite max. 2 mm | Kreuzschnitt- oder Streifenschreddern |
| **ÖFFENTLICH** | Keine Mindestanforderung | Entf. | Normaler Abfall / Recycling |

- Schreddern sollte wo möglich vor Ort mit organisationseigenen Schreddern durchgeführt werden. Für Massenvernichtung können genehmigte externe Anbieter mit Abholung in verschlossenen Vertraulichkeitsmüllbehältern und Vernichtungszertifikaten eingesetzt werden.
- Vertraulichkeitsmüllbehälter sind an zugänglichen Standorten im gesamten Büro bereitzustellen. Behälter müssen verschlossen und planmässig durch autorisiertes Personal oder [Vernichtungsanbieter] geleert werden.
- Massenvernichtungsereignisse (Büroumzüge, Archivbereinigungen) müssen bezeugt oder zertifiziert sein.

### Mikrofilm, Mikrofiche und fotografische Medien

- Vernichtung muss DIN-66399-Medienkategorie F (Film) auf Sicherheitsstufen entsprechend der Klassifizierung der Informationen folgen.
- VERTRAULICH: F-4 Minimum (max. 160 mm² Partikelgrösse). INTERN: F-3 Minimum.
- Wo die Vernichtung von Filmmedien vor Ort nicht möglich ist, ist ein genehmigter externer Anbieter zu beauftragen.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten für Speichermedien |
|-------|----------------------------------------|
| **Geschäftsleitung** | Richtlinie genehmigen; Ressourcen für Mediensicherheitsinfrastruktur und Anbieterverträge bereitstellen |
| **ISB** | Richtlinieneigentümerschaft; Sanitisierungsstandards definieren; Compliance überwachen; Ausnahmen genehmigen; Ergebnisse des vierteljährlichen Audits überprüfen |
| **IT-Betrieb** | Medienbeschaffung und -bereitstellung; Verschlüsselungsimplementierung; Sanitisierung und Vernichtung durchführen; Entsorgungsnachweise pflegen; [Sicherlösch-Tool] und [Endgeräte-Management-Tool] verwalten |
| **Gebäudemanager** | Physische Lagerinfrastruktur verwalten (Tresore, verschlossene Schränke); Bereitstellung und Abholung von Vertraulichkeitsmüllbehältern koordinieren; Schreddergeräte vor Ort verwalten |
| **Vorgesetzte** | Wechselmedieneinsatz für ihre Teams genehmigen; Team-Compliance mit Handhabungs- und Lagerungsanforderungen sicherstellen; Audit-Befunde bearbeiten |
| **Einkauf / Lieferantenmanagement** | [Vernichtungsanbieter]-Verträge verwalten; Anbieterzertifizierungen verifizieren; Vernichtungszertifikate einsammeln und prüfen |
| **Asset Management** | Medieninventar im [Asset-Management-System] pflegen; vierteljährliche Medien-Audits durchführen; Datensätze abstimmen; Asset-Status bei Entsorgung aktualisieren |
| **Alle Mitarbeitenden** | Medien gemäss Klassifizierungsanforderungen handhaben; Medien beim Beschäftigungsaustritt zurückgeben; verlorene, gestohlene oder beschädigte Medien sofort melden; keine persönlichen Medien für Organisationsdaten verwenden |

**Eskalationspfad**:

- Verlorene oder gestohlene Medien: Mitarbeitender --> Vorgesetzter + IT-Betrieb (sofort) --> ISB
- Fragen zur Medienrichtlinie: Mitarbeitender --> IT-Betrieb --> ISB
- Fehlende Vernichtungszertifikate: IT-Betrieb --> Einkauf --> ISB
- Vierteljährliche Audit-Abweichungen: Asset Management --> ISB --> Geschäftsleitung (falls nicht innerhalb von 5 Arbeitstagen gelöst)

### Incident-Response bei verlorenem oder gestohlenen Medium

Bei Meldung eines Medienverlusts oder -diebstahls sind folgende Sofortmassnahmen zu ergreifen:

**Innerhalb von 15 Minuten nach Meldung**:

1. **Schweregrad beurteilen**:
   - Klassifizierung der Daten auf den Medien (VERTRAULICH = Kritisch, INTERN = Hoch, ÖFFENTLICH = Niedrig)
   - Verschlüsselungsstatus (verschlüsselt = geringeres Risiko, unverschlüsselt = höheres Risiko)
   - Anzahl der betroffenen Personendatensätze (>100 Personen = höheres Risiko für Meldepflicht)

2. **Sofortige Eindämmung** (bei unverschlüsselten oder VERTRAULICHEN Daten):
   - IT-Betrieb: Fernlöschung der Medien, falls Fernlöschfähigkeit besteht (z.B. Mobilgerät, cloud-synchronisierte Medien)
   - IT-Betrieb: Zugehörige Zugangsdaten deaktivieren, falls Medien Zugangsdaten enthielten (API-Schlüssel, Passwörter)
   - IT-Betrieb: Medienseriennummer aus genehmigter Medienliste deaktivieren (Verhinderung erneuter Verbindung bei Fund)

**Innerhalb von 1 Stunde**:

3. **Incident-Klassifizierung**:
   - VERTRAULICH + unverschlüsselt = Kritischer Schweregrad (Datenschutzverletzung annehmen, Verletzungsreaktion gemäss A.5.24–28 einleiten)
   - VERTRAULICH + verschlüsselt = Hoher Schweregrad (Schlüsselsicherheit beurteilen, Entschlüsselungspotenzial)
   - INTERN + unverschlüsselt = Hoher Schweregrad
   - INTERN + verschlüsselt ODER ÖFFENTLICH = Mittlerer/Niedriger Schweregrad

4. **Eskalation und Untersuchung**:
   - ISB benachrichtigt (kritischer/hoher Schweregrad)
   - DSB benachrichtigt (bei beteiligten Personendaten — Meldepflichtbewertung gemäss nDSG Art. 24 / DSGVO Art. 33)
   - Untersuchung: Wie gingen die Medien verloren? Umstände, Zeitlinie, letzter bekannter Standort

**Innerhalb von 24 Stunden**:

5. **Bewertung der Verletzungsmeldung**:
   - Falls nDSG-/DSGVO-Verletzungskriterien erfüllt: EDÖB/Aufsichtsbehörde gemäss anwendbarem Zeitplan benachrichtigen (nDSG: so bald wie möglich; DSGVO: 72 Stunden)
   - Falls vertragliche Meldepflicht besteht (Kunden-DPA): Kunden gemäss Vertragsbedingungen benachrichtigen
   - Verletzungsentscheidung im Incident-Protokoll dokumentieren

6. **Behebung**:
   - Medien ersetzen, falls Nutzer weiterhin Wechselmedien für Geschäftstätigkeit benötigt
   - Verschlüsselte Medien neu ausgeben, falls verlorene Medien unverschlüsselt waren
   - [Asset-Management-System] aktualisieren: Medien als „Verloren" mit Incident-Referenz markieren
   - Beratung/Schulung des Nutzers bei Verlust durch Fahrlässigkeit

**Nach dem Incident**:
- Ursachenanalyse: Warum gingen Medien verloren? Prozesslücke? Richtlinienverstoss?
- Vorbeugungsmassnahmen: Bei Muster von Verlusten (z.B. reisebezogen), zusätzliche Controls implementieren
- Berichterstattung im vierteljährlichen Management-Review: Statistiken zu verlorenen/gestohlenen Medien, Trends, Behebungsmassnahmen

---

## Nachweise für diese Richtlinie

| # | Nachweis | Eigentümer | Häufigkeit | Aufbewahrung |
|---|----------|------------|------------|--------------|
| 1 | Wechselmedieinventar (vollständiges Register mit Verschlüsselungsstatus) | Asset Management | Kontinuierlich; vierteljährliches Audit | Lebensdauer des Asset-Datensatzes |
| 2 | Mediengenehmigungsnachweise (Managementgenehmigungen für Wechselmedieneinsatz) | Vorgesetzte | Pro Genehmigungsereignis | 3 Jahre |
| 3 | Übertragungsprotokolle für VERTRAULICHE Daten (Datum, Nutzer, Medienkennung, Datenbeschreibung, Empfänger) | IT-Betrieb | Pro Übertragungsereignis | 7 Jahre |
| 4 | Vierteljährliche Medien-Audit-Berichte (Abstimmungsergebnisse, Abweichungen, Lösungen) | Asset Management | Vierteljährlich | 3 Jahre |
| 5 | Geräteentsorgungsnachweise (Asset-Tag, Klassifizierung, Methode, Datum, Operator) | IT-Betrieb | Pro Entsorgungsereignis | 7 Jahre |
| 6 | Vernichtungszertifikate vom [Vernichtungsanbieter] | Einkauf | Pro Vernichtungsereignis | 7 Jahre |
| 7 | Sicherlösch-Verifizierungsprotokolle (Tool-Ausgabe pro Asset) | IT-Betrieb | Pro Löschereignis | 7 Jahre |
| 8 | Beweiskettenunterlagen für Medientransport | IT-Betrieb | Pro Transportereignis | 7 Jahre |
| 9 | USB-Port- und Wechselspeicherverbindungsprotokolle (Endgerätetelemetrie) | IT-Betrieb | Kontinuierlich | 12 Monate |
| 10 | Abholungs- und Schredderprotokolle für Vertraulichkeitsmüllbehälter | Gebäudemanager | Pro Abholevent | 3 Jahre |
| 11 | Anbieter-Due-Diligence-Nachweise für Vernichtungsdienstleister | Einkauf | Jährliche Überprüfung | Vertragslaufzeit + 2 Jahre |
| 12 | Richtlinienbestätigungsnachweise (Medienhandhabungsschulung) | HR / ISB | Jährlich | Beschäftigungsdauer + 1 Jahr |
| 13 | Incident-Berichte zu verlorenen/gestohlenen Medien (Schweregrad, Eindämmung, Verletzungsbewertung) | ISB | Pro Incident | 7 Jahre |
| 14 | Mediengenehmigungsablauf- und -erneuerungsnachweise | IT-Betrieb | Pro Ereignis | Zuteilungsdauer + 1 Jahr |
| 15 | Versionshistorie und Überprüfungsnachweise der genehmigten Medienliste | IT-Betrieb / ISB | Jährlich + anlassbasiert | 3 Jahre |

---

## Optional: Zahlungskarteninhaberdaten-Controls (PCI DSS)

*Nur anwendbar, wenn Zahlungskarteninhaberdaten verarbeitet werden und PCI-Geltungsbereich besteht.*

Falls PCI-DSS-Geltungsbereich besteht, sind folgende Zusatzanforderungen zu erfüllen:

- Medien mit Karteninhaberdaten müssen physisch vernichtet werden, wenn sie für Geschäfts- oder rechtliche Zwecke nicht mehr benötigt werden (PCI DSS Anforderung 9.4).
- Ein Inventar der Medien mit Karteninhaberdaten ist zu führen und mindestens jährlich abzugleichen (PCI DSS Anforderung 9.4.1).
- Sichere Entsorgung von Karteninhaberdaten-Medien muss mit Vernichtungszertifikaten dokumentiert sein (PCI DSS Anforderung 9.4.7).
- Interner und externer Transport von Medien mit Karteninhaberdaten muss sicheren Kurier verwenden und protokolliert sein (PCI DSS Anforderung 9.4.3–9.4.4).

---

# Richtlinien-Compliance

## Compliance-Messung

Das Informationssicherheits-Managementteam überprüft die Compliance mit dieser Richtlinie durch verschiedene Methoden, darunter:

- Vierteljährliche Wechselspeichermedien-Audits gemäss risikobasierter Stichprobenmethodik (100% jährliche Abdeckung).
- Monatliche Überprüfung von USB-Verbindungsprotokollen und Endgeräteschutzalarmen für ungenehmigte Medien.
- Halbjährliche Überprüfung der Entsorgungsnachweise gegen das Asset-Register zur Identifizierung nicht erfasster Entsorgungen.
- Jährliche Überprüfung der [Vernichtungsanbieter]-Verträge, Zertifizierungen und Vollständigkeit der Vernichtungszertifikate.
- Jährliche Verifizierung, dass genehmigte Medienliste, Sanitisierungs-Tools und Verfahren aktuell sind.
- Interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

**Governance-Kennzahlen**:

| Kennzahl | Ziel |
|----------|------|
| Registrierte Medien mit Verschlüsselungs-Compliance | 100% |
| Medienverluste oder -diebstähle (pro Quartal) | 0 |
| Entsorgungen mit Zertifikat (VERTRAULICH) | 100% |
| Sicherlösch-Verifizierung abgeschlossen (pro Entsorgung) | 100% |
| Vierteljährliche Audit-Abschlussrate | 100% |
| Überfällige Medienrückgaben | < 3 |
| Seriennummern-Übereinstimmungsrate bei Vernichtungszertifikaten | 100% |

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vom ISB vorab genehmigt und dokumentiert werden, mit dokumentierter Risikoakzeptanz, Ausgleichsmassnahmen und einem definierten Überprüfungsdatum von höchstens 6 Monaten. Ausnahmen sind dem Management-Review-Team zu melden.

Zulässige Ausnahmen umfassen:

- Unverschlüsselte Wechselmedien für spezifische betriebliche Anforderungen, wo Verschlüsselung technisch inkompatibel ist, mit verstärkten physischen Controls und zeitlich befristeter Genehmigung.
- Verlängerte Aufbewahrung über Standardfristen hinaus mit dokumentierter Geschäfts- oder rechtlicher Begründung und jährlicher Überprüfung.
- Alternative Transportmethoden mit vom ISB unterzeichneter Risikoakzeptanz.

Ausnahmen dürfen nicht gewährt werden für:

- VERTRAULICHE Daten auf unverschlüsselten Wechselmedien ohne jegliche Ausgleichsmassnahmen.
- Persönliche Medien für VERTRAULICHE oder INTERNE Organisationsdaten.
- Entsorgung VERTRAULICHER Medien ohne Verifizierung oder Zertifikat.
- Umgehung der vierteljährlichen Medien-Audit-Anforderungen.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstösst, kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung des Arbeitsverhältnisses.

Unsachgemässe Handhabung oder Entsorgung von Medien mit Personendaten kann zusätzlich einen Verstoss gegen das Schweizer nDSG darstellen und möglicherweise eine regulatorische Untersuchung durch den Eidgenössischen Datenschutz- und Öffentlichkeitsbeauftragten (EDÖB) und, sofern anwendbar, EU-Datenschutzbehörden unter der DSGVO nach sich ziehen.

Verlust unverschlüsselter Medien mit Personendaten muss als Datenschutzverletzung gemeldet und gemäss den Incident-Management-Verfahren der Organisation und den anwendbaren Meldepflichten bewertet werden.

## Kontinuierliche Verbesserung

Diese Richtlinie wird als Teil des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen berücksichtigen:

- Änderungen an Sanitisierungsstandards (einschliesslich NIST SP 800-88-Updates, IEEE-2883-Revisionen, DIN-66399-Änderungen)
- Neue Speichertechnologien (z.B. NVMe, persistenter Speicher, neue Flash-Architekturen)
- Änderungen am Schweizer nDSG, DSGVO oder anderen anwendbaren Vorschriften
- Audit-Befunde und Entsorgungsvorfälle
- Rückmeldungen aus vierteljährlichen Medien-Audits und Anbieterüberprüfungen
- Änderungen am Informationsklassifizierungsschema der Organisation

---

# Abgedeckte Bereiche des ISO-27001-Standards

Richtlinie für Speichermedien — ISO-27001-Controls-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Managementverantwortung |
| Klausel 6.1 Massnahmen zum Umgang mit Risiken | 5.9 Inventar von Informationen und zugehörigen Assets |
| Klausel 7.3 Bewusstsein | 5.10 Akzeptable Nutzung von Informationen und zugehörigen Assets |
| Klausel 7.5 Dokumentierte Informationen | 5.12 Klassifizierung von Informationen |
| Klausel 8.1 Betriebliche Planung und Steuerung | 5.13 Kennzeichnung von Informationen |
| Klausel 10.2 Nichtkonformität und Korrekturmassnahmen | **7.10 Speichermedien** |
| | 7.14 Sichere Entsorgung oder Wiederverwendung von Ausrüstung |
| | 8.10 Informationslöschung |
| | 8.24 Einsatz von Kryptografie |

# Regulatorischer Rahmen

| Rahmen | Relevanz |
|--------|----------|
| Schweizer nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen; Unwiederherstellbarkeit personenbezogener Daten vor Entsorgung |
| Schweizer DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit einschliesslich physischer Mediensicherung |
| EU DSGVO (sofern anwendbar) | Art. 5(1)(f) — Integrität und Vertraulichkeit; Art. 17 — Recht auf Löschung; Art. 32 — Sicherheit der Verarbeitung |
| ISO/IEC 27001:2022 | Annex A Control 7.10 — Lebenszyklusmanagement von Speichermedien |
| ISO/IEC 27002:2022 | Abschnitt 7.10 — Umsetzungshinweise für Speichermedien |
| NIST SP 800-88 Rev. 2 | Richtlinien zur Mediensanitisierung — Löschen, Bereinigen, Vernichten (September 2025; ersetzt Rev. 1) |
| IEEE 2883:2022 | Standard für die Sanitisierung von Speichermedien — technische Methoden für Laufwerke und Medien |
| DIN 66399 | Vernichtung von Datenträgern — Sicherheitsstufen (P/F/O/T/H/E-Kategorien, Stufen 1–7) und Schutzklassen |

---

<!-- QA_VERIFIED: 2026-03-29 -->
