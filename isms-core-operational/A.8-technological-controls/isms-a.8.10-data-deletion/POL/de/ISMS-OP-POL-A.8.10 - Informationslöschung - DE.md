<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.10-DE:operational:OP-POL:a.8.10 -->
**ISMS-OP-POL-A.8.10 — Informationslöschung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Informationslöschung |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.10 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
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

- ISO/IEC 27001:2022 Control A.8.10 — Information deletion

**Verwandte Annex-A-Controls**:

| Control | Bezug zur Informationslöschung |
|---------|-------------------------------|
| A.5.9 Inventar von Informationen und anderen zugehörigen Assets | Asset-Inventar definiert Löschumfang und Dateneigentümerschaft |
| A.5.10 Akzeptable Nutzung von Informationen und anderen zugehörigen Assets | Lebenszyklus der akzeptablen Nutzung umfasst Löschung am Ende der Nutzungsdauer |
| A.5.12–13 Informationsklassifizierung und -kennzeichnung | Klassifizierung bestimmt Löschmethode und Verifizierungsniveau |
| A.5.14 Informationsübertragung | Löschpflichten nach Abschluss der Übertragung |
| A.5.33 Schutz von Aufzeichnungen | Aufbewahrungspläne lösen Löschung bei Ablauf aus |
| A.5.34 Datenschutz und Schutz personenbezogener Daten | Löschansprüche von betroffenen Personen; Löschpflichten für personenbezogene Daten |
| A.7.10 Speichermedien | Physische Medienbereinigung und -entsorgung |
| A.7.14 Sichere Entsorgung oder Wiederverwendung von Geräten | Geräteausserdienststellung erfordert Datenlöschung |
| A.8.13 Informationssicherung | Backup-Kopien in Löschumfang eingeschlossen |
| A.8.24 Einsatz von Kryptographie | Kryptographische Löschung als Löschmethode |

**Verwandte interne Richtlinien**:

- Richtlinie zur Informationsklassifizierung und -handhabung
- Richtlinie zum Datenschutz und Schutz personenbezogener Daten
- Richtlinie zum Informationsschutz und Records Management
- Backup-Richtlinie
- Asset-Management-Richtlinie
- Richtlinie zum Einsatz von Kryptographie

---

# Richtlinie zur Informationslöschung

## Zweck

Zweck dieser Richtlinie ist es sicherzustellen, dass in Informationssystemen, Geräten oder anderen Speichermedien gespeicherte Informationen gelöscht werden, wenn sie nicht mehr benötigt werden, unter Verwendung von Methoden, die der Sensibilität der Daten und dem Medientyp angemessen sind, um unnötige Exposition zu verhindern und gesetzliche, regulatorische und vertragliche Anforderungen zu erfüllen.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 6(4) (Verhältnismässigkeit und Datensparsamkeit — personenbezogene Daten sind zu vernichten oder zu anonymisieren, sobald sie für den Zweck der Bearbeitung nicht mehr erforderlich sind) und Art. 8 (technische und organisatorische Massnahmen für die Datensicherheit). Soweit die Organisation Daten von Personen in der EU/im EWR verarbeitet, gelten auch die DSGVO Art. 5(1)(e) (Speicherbegrenzung) und Art. 17 (Recht auf Löschung).

## Geltungsbereich

Alle Mitarbeitenden und Drittnutzer.

Alle Informationen, die auf oder in organisationseigenen, verwalteten und kontrollierten Systemen, Geräten und Medien verarbeitet, gespeichert oder übertragen werden, die gemäss ISO-27001-Geltungsbereichserklärung als in den Geltungsbereich fallend eingestuft sind.

Dies umfasst:

- Alle Datenkategorien (personenbezogene Daten, vertrauliche Geschäftsinformationen, Finanzdaten, technische Daten, Kommunikation, Protokolle)
- Alle Speicherorte (On-Premises, Cloud, Drittanbieter, Backup, Disaster Recovery)
- Alle Medientypen (magnetisch, Solid-State, optisch, Papier, Wechselmedien, mobile Geräte)
- Alle Lebenszyklusphasen (aktive Nutzung, Archivierung, Backup, Entwicklung/Test, End-of-Life)

## Grundsatz

Informationen sollen nicht länger aufbewahrt werden als für ihren angegebenen geschäftlichen, rechtlichen oder regulatorischen Zweck erforderlich. Wenn Aufbewahrungsfristen ablaufen oder ein gültiger Löschanlass eintritt, sollen Informationen mit einer Methode gelöscht werden, die der Datensensibilität und dem Medientyp angemessen ist, mit nachprüfbaren Nachweisen, dass die Löschung durchgeführt wurde.

Es sollen ausschliesslich von der Organisation genehmigte Löschmethoden verwendet werden. Standard-Betriebssystem-Löschung (z. B. "Löschen" oder "Papierkorb leeren") ist für vertrauliche oder personenbezogene Daten unzureichend, da solche Methoden typischerweise wiederherstellbar sind.

---

## Aufbewahrungspläne und Löschauslöser

### Aufbewahrungsplan

Die Organisation soll einen Aufbewahrungsplan pflegen, der Aufbewahrungsfristen für alle Datenkategorien definiert. Aufbewahrungsfristen sollen auf der längsten anwendbaren Anforderung basieren aus:

- Gesetzliche und gesatzliche Pflichten (Schweizer OR, nDSG, Steuerrecht)
- Regulatorische Anforderungen (branchenspezifische Vorschriften)
- Vertragliche Pflichten (Kunden-, Lieferanten-, Partnervereinbarungen)
- Dokumentierter Geschäftsbedarf (mit Genehmigung des Eigentümers)

Wenn mehrere Anforderungen auf dieselben Daten anwendbar sind, gilt die längste anwendbare Aufbewahrungsfrist, sofern der Rechtsberater nicht anderes bestimmt.

**Referenzaufbewahrungsfristen für Schweizer KMUs**:

| Datenkategorie | Mindestaufbewahrung | Rechtsgrundlage | Hinweise |
|----------------|---------------------|-----------------|---------|
| **Buchhaltungsunterlagen** (Jahresberichte, Prüfberichte, Abschlüsse) | 10 Jahre ab Ende des Geschäftsjahres | Schweizer OR Art. 958f | Müssen in schriftlicher und unterzeichneter Form (Jahres-/Prüfberichte) oder elektronisch mit Integritätsgarantie aufbewahrt werden |
| **Buchhaltungsbelege** (Rechnungen, Quittungen, Kontoauszüge, MWST-Dokumente) | 10 Jahre ab Ende des Geschäftsjahres | Schweizer OR Art. 958f | Können elektronisch gemäss Olico-Anforderungen aufbewahrt werden |
| **Arbeitsverträge und HR-Akten** | 10 Jahre ab Ende des Arbeitsverhältnisses | Schweizer OR Art. 127–128 (Verjährungsfristen); kantonale Anforderungen | Lohnansprüche: 5-jährige Verjährung (OR Art. 128); Arbeitszeugnisse: 10-jährige Verjährung (OR Art. 127) |
| **Lohn- und Sozialversicherungsunterlagen** | 10 Jahre ab Ende des Geschäftsjahres | Schweizer OR Art. 958f; AHV/IV-Anforderungen | Umfasst Lohnausweise, Sozialversicherungsbeiträge |
| **Steuerunterlagen** | 10 Jahre ab Ende des Geschäftsjahres | Schweizer OR Art. 958f; kantonales Steuerrecht | Umfasst Körperschaft- und MWST-Unterlagen |
| **Kundenverträge** | Dauer + 10 Jahre | Schweizer OR Art. 127 (allgemeine Verjährung) | 10-jährige Verjährungsfrist für Vertragsansprüche |
| **Lieferanten- und Anbieterverträge** | Dauer + 10 Jahre | Schweizer OR Art. 127 | Für Verjährungszeitraum nach Vertragsende aufbewahren |
| **Personenbezogene Daten (allgemein)** | Nur so lange wie für den Bearbeitungszweck erforderlich | nDSG Art. 6(4) | Müssen gelöscht oder anonymisiert werden, wenn der Zweck erfüllt ist |
| **Aufzeichnungen über Einwilligung betroffener Personen** | Dauer der Bearbeitung + 3 Jahre | nDSG Art. 6; Best Practice | Nachweis der Rechtsgrundlage für die Bearbeitung |
| **Sicherheitsprotokolle und Audit-Trails** | 12 Monate (online), bis 3 Jahre (Archiv) | Organisationsrichtlinie; DSV Art. 4 | Längere Aufbewahrung für Protokolle der Verarbeitung sensibler Daten |
| **ISMS-Auditnachweis** | Mindestens 3 Jahre | ISO-27001-Zertifizierungszyklus | Über den gesamten Zertifizierungszyklus aufbewahren |
| **Incident-Untersuchungsaufzeichnungen** | 3 Jahre nach Abschluss | Organisationsrichtlinie | Länger wenn Rechtsstreitigkeiten erwartet werden |

Diese Tabelle enthält Mindestreferenzzeiträume. Der Records Manager soll den massgeblichen Aufbewahrungsplan pflegen, der jährlich vom Rechtsberater überprüft und von der Geschäftsleitung genehmigt wird.

### Löschauslöser

Die Löschung soll eingeleitet werden, wenn eines der folgenden Ereignisse eintritt:

| # | Auslöseereignis | Verantwortlicher | Zeitrahmen |
|---|-----------------|-----------------|------------|
| 1 | **Ablauf der Aufbewahrungsfrist** | Records Manager / Systemverantwortlicher | Innerhalb von 90 Tagen nach Ablauf (wenn möglich automatisiert) |
| 2 | **Löschantrag einer betroffenen Person** (nDSG / DSGVO Art. 17) | DSB / Datenschutzberater | Innerhalb von 30 Tagen nach validiertem Antrag |
| 3 | **Kündigung eines Vertrags oder einer Dienstleistungsvereinbarung** | Systemverantwortlicher | Gemäss Vertragsbedingungen (Standard: 90 Tage) |
| 4 | **Abschluss des Bearbeitungszwecks** | Dateneigentümer | Innerhalb von 90 Tagen nach Zweckerfüllung |
| 5 | **Aufhebung einer Aufbewahrungspflicht** | Rechtsberater | Innerhalb von 90 Tagen nach Aufhebung |
| 6 | **Ausserdienststellung eines Assets** | IT-Betrieb | Bevor Asset die organisationale Kontrolle verlässt |
| 7 | **Widerruf der Einwilligung** | DSB / Datenschutzberater | Innerhalb von 30 Tagen (sofern keine andere Rechtsgrundlage gilt) |

Wo automatisierte Löschung technisch machbar ist, sollte sie mit Schutzvorrichtungen gegen vorzeitige Löschung implementiert werden (Prüfungen auf Aufbewahrungspflichten, Benachrichtigung des Geschäftsverantwortlichen). Wo Automatisierung nicht machbar ist, sollen manuelle Löschverfahren mit definierten Verifizierungs-Checkpoints dokumentiert werden.

---

## Löschmethoden

### Bereinigungsstandards

Löschmethoden sollen mit NIST SP 800-88 Rev. 2 (Guidelines for Media Sanitization, September 2025) übereinstimmen, der drei Bereinigungsstufen definiert, sowie IEEE 2883 für medienspezifische Bereinigungstechniken.

| Bereinigungsstufe | Beschreibung | Wann zu verwenden | Beispielmethoden |
|-------------------|--------------|-------------------|-----------------|
| **Löschen (Clear)** | Logische Techniken, die Daten über Standardschnittstellen unzugänglich machen; Wiederherstellung mit Spezialtools möglich | Medien verbleiben unter organisationaler Kontrolle; Daten niedrigerer Sensibilität (Öffentlich, Intern) | Standard-Überschreiben, Hersteller-Reset, sicheres Löschen des Betriebssystems |
| **Bereinigen (Purge)** | Physische oder logische Techniken, die Daten selbst mit Laborwerkzeugen unzugänglich machen | Medien verlassen organisationale Kontrolle; sensible Daten (Vertraulich); Medienwiederverwendung durch Dritte | Kryptographische Löschung, Block-Erasure (Flash/SSD), Degaussing (Magnetmedien) |
| **Vernichten (Destroy)** | Physische Zerstörung, die Medien unbrauchbar und Datenwiederherstellung unmöglich macht | End-of-Life-Medien; höchst sensible Daten; Medien ohne zukünftigen Wert | Desintegration, Pulverisierung, Verbrennung, Einschmelzen, Schreddern |

### Löschmethode nach Klassifizierung und Medium

| Datenklassifizierung | Medien verbleiben intern | Medien verlassen Organisation | Medien End-of-Life |
|----------------------|--------------------------|------------------------------|---------------------|
| **Öffentlich** | Clear | Clear | Destroy (oder Recycling wenn verifiziert gelöscht) |
| **Intern** | Clear | Purge | Destroy |
| **Vertraulich** | Purge | Purge | Destroy |
| **Streng vertraulich** | Purge | Destroy | Destroy |

### Papierunterlagen

| Datenklassifizierung | Entsorgungsmethode |
|----------------------|-------------------|
| **Öffentlich** | Allgemeiner Abfall oder Recycling |
| **Intern** | Kreuzschnitt-Shreddern (DIN 66399 P-3 mindestens) |
| **Vertraulich** | Kreuzschnitt-Shreddern (DIN 66399 P-4 mindestens) oder dokumentierte Verbrennung |
| **Streng vertraulich** | DIN 66399 P-5 mindestens oder zertifizierte Drittanbieter-Vernichtung mit Zertifikat |

### Kryptographische Löschung

Kryptographische Löschung kann als gültige Purge-Methode verwendet werden, wenn Daten im Ruhezustand verschlüsselt wurden und die Verschlüsselung den Organisationsstandards entspricht (gemäss Richtlinie zum Einsatz von Kryptographie). Damit kryptographische Löschung im Rahmen dieser Richtlinie als Löschung gilt:

- Alle Zieldaten sollen vor der Speicherung verschlüsselt worden sein (nachträgliche Verschlüsselung qualifiziert sich nicht).
- Der Verschlüsselungsalgorithmus soll genehmigte Mindeststandards erfüllen (AES-256 oder gleichwertig).
- Ein dokumentiertes Daten-Schlüssel-Mapping soll existieren, das die Identifikation ermöglicht, welche Verschlüsselungsschlüssel welche Daten schützen.
- Die Schlüsselvernichtung soll durch einen verifizierten Prozess durchgeführt werden (HSM-Schlüsselbereinigung, KMS-Schlüssellöschung mit Audit-Protokoll oder gleichwertig).
- Schlüsselvernichtungsnachweis soll mindestens 3 Jahre aufbewahrt werden (Audit-Protokolle, HSM-Zertifikate).
- Backup-Kopien des Verschlüsselungsschlüssels sollen ebenfalls vernichtet werden — wenn Schlüssel-Backup, Hinterlegung oder externe Speicherung existiert und nicht als vernichtet verifiziert werden kann, soll kryptographische Löschung nicht als alleinige Löschmethode akzeptiert werden.

### Backup-Löschung

Die Löschung in Produktionssystemen soll sich auf alle Backup-Kopien erstrecken, die die gelöschten Daten enthalten, einschliesslich:

- Vollständige, inkrementelle und differentielle Backups
- Snapshots und Point-in-Time-Kopien
- Disaster-Recovery-Replikate
- Anwendungsseitige Backups (Datenbankexporte, VM-Exporte)
- Cloud-native Backup-Dienste mit unabhängigen Aufbewahrungsrichtlinien

Wo eine sofortige Löschung aus Backups technisch nicht machbar ist (z. B. unveränderliche Backup-Tapes, aufbewahrungsgesperrte Cloud-Backups), soll die Organisation:

1. Den Backup-Aufbewahrungsplan dokumentieren, der zeigt, wann die Daten natürlich überschrieben oder abgelaufen werden.
2. Genehmigung von ISB und Dateneigentümer für den verlängerten Aufbewahrungszeitraum einholen.
3. Zugriffskontrollen anwenden, um eine Wiederherstellung der Daten aus Backups zu verhindern.
4. Die ausstehende Löschung im Löschregister verfolgen, bis die Bestätigung vorliegt.

---

## Löschung durch Dritte und in der Cloud

### Vertragliche Anforderungen

Alle Verträge mit Dritten, die organisationale Daten verarbeiten, sollen Löschpflichten enthalten, die Folgendes spezifizieren:

- Maximale Löschfrist nach Vertragsbeendigung oder auf schriftlichen Antrag (Standard: 30 Tage)
- Bereinigungsstandard entsprechend der Datensensibilität (unter Bezugnahme auf NIST-SP-800-88-Stufen)
- Löschumfang, der alle Kopien einschliesst, einschliesslich Backups, Caches, Protokolle und Disaster-Recovery-Replikate
- Anforderung zur Bereitstellung eines Löschnachweises (Vernichtungszertifikat oder gleichwertige Bestätigung)
- Weitergabe der Löschanforderungen an Unterauftragsverarbeiter
- Recht zur Überprüfung der Lösch-Compliance

### Bewertung von Cloud-Service-Anbietern

Vor der Beauftragung eines Cloud-Service-Anbieters soll die Organisation Löschfähigkeiten bewerten, einschliesslich:

- API-Unterstützung für Datenlöschung und Löschverifizierung
- Löschausbreitung auf alle Regionen, Verfügbarkeitszonen und Replikate
- Mandantenisolationsgarantie (Löschung betrifft keine anderen Mandanten; andere Mandanten können nicht auf Restdaten zugreifen)
- Backup- und Snapshot-Löschfähigkeiten und -zeiträume
- Kontrollen für Datenremanenz nach der Löschung
- Zertifizierung oder Bestätigung von Löschpraktiken (SOC 2 Typ II, ISO 27001 mit A.8.10 im Geltungsbereich)

### Drittanbieter-Löschverifizierung

Die Organisation soll Löschbestätigungen von Dritten durch eine oder mehrere der folgenden Methoden erhalten:

**Physische Medienvernichtung** — Vernichtungszertifikate enthaltend:
- Medienseriennummern oder Asset-Kennungen
- Vernichtungsmethode (Bezugnahme auf NIST-SP-800-88-Stufe oder DIN-66399-Sicherheitsstufe)
- Vernichtungsdatum und -ort
- Name und Akkreditierung des Zertifikatsausstellers (z. B. NAID AAA, ISO 21964)

**Logische Löschung durch den Service-Anbieter** — Eines von:
- SOC-2-Typ-II-Bericht mit Löschkontrolltests
- Unabhängiger Prüfbericht zur Verifizierung der Löschverfahren
- ISO-27001-Zertifizierung mit A.8.10 im Geltungsbereich

**Cloud/SaaS API-Löschung** — Protokollierte Nachweise enthaltend:
- API-Aufruf-Zeitstempel und authentifizierter Nutzer
- Gelöschte Ressourcenkennung(en)
- HTTP-Erfolgsmeldung (200/204)
- Bestätigung der Backup-/Snapshot-Löschung, wenn der Anbieter dies unterstützt

Für vertrauliche und streng vertrauliche Daten: Zertifikate von akkreditierten Vernichtungsanbietern oder unabhängige Prüfberichte sind erforderlich. API-Protokolle allein sind nicht ausreichend.

### Eskalation bei Drittanbieter-Löschversagen

| Zeitpunkt | Massnahme | Verantwortlicher |
|-----------|-----------|-----------------|
| T+0 Tage | Versagen im Lückenregister protokollieren; Follow-up mit Drittanbieter-Kontakt einleiten | IT-Betrieb |
| T+15 Tage | An Drittanbieter-Account-Manager eskalieren; ISB und DSB in Kopie | Systemverantwortlicher |
| T+30 Tage | An Drittanbieter-Führungskontakt eskalieren; Vertragsüberprüfung mit Rechtsberater einleiten | ISB |
| T+45 Tage | Vertragliche Abhilfe prüfen (Service-Gutschriften, Kündigung wegen wesentlicher Vertragsverletzung); Datenmigration zu konformem Anbieter erwägen | Geschäftsleitung |

Bei vertraulichen/streng vertraulichen Daten sind Eskalationsfristen verkürzt: T+7, T+15, T+21 Tage.

---

## Löschanträge betroffener Personen

### Annahme und Bearbeitung von Anträgen

Die Organisation soll Löschanträge betroffener Personen in Übereinstimmung mit dem schweizerischen nDSG Art. 6(4) und, soweit anwendbar, DSGVO Art. 17 (Recht auf Löschung / Recht auf Vergessenwerden) annehmen und bearbeiten.

**Antragsbearbeitungsprozess**:

| Schritt | Massnahme | Zeitrahmen | Verantwortlicher |
|---------|-----------|------------|-----------------|
| 1 | Antrag entgegennehmen (E-Mail, Webformular, Post, persönlich) | — | DSB / Datenschutzberater |
| 2 | Antrag im Datenschutz-Antragsregister protokollieren | Innerhalb von 24 Stunden | DSB / Datenschutzberater |
| 3 | Identität der betroffenen Person verifizieren | Innerhalb von 5 Arbeitstagen | DSB / Datenschutzberater |
| 4 | Alle Systeme, Datenbanken und Backups identifizieren, die die personenbezogenen Daten der betroffenen Person enthalten | Innerhalb von 10 Arbeitstagen | IT-Betrieb / Systemverantwortliche |
| 5 | Prüfen, ob Löschpflicht gilt oder eine rechtliche Ausnahme besteht | Innerhalb von 15 Arbeitstagen | DSB + Rechtsberater |
| 6 | Löschung ausführen oder begründete Ablehnung ausstellen | Innerhalb von 25 Arbeitstagen | IT-Betrieb / DSB |
| 7 | Abschluss der betroffenen Person schriftlich bestätigen | Innerhalb von 30 Tagen nach Antrag | DSB / Datenschutzberater |

### Rechtliche Ausnahmen für die Löschung

Die Löschung kann verweigert werden, wenn die Bearbeitung notwendig ist für:

- Einhaltung einer gesetzlichen Aufbewahrungspflicht (z. B. Schweizer OR Art. 958f Buchhaltungsunterlagen, Steuerpflichten)
- Begründung, Ausübung oder Verteidigung von Rechtsansprüchen
- Archivierungszwecke im öffentlichen Interesse, wissenschaftliche oder historische Forschung
- Gründe des öffentlichen Interesses im Bereich der öffentlichen Gesundheit
- Ausübung der Meinungs- und Informationsfreiheit

Wenn die Löschung aufgrund einer rechtlichen Ausnahme verweigert wird:

1. Die spezifische rechtliche Grundlage dokumentieren.
2. Schriftliche Erklärung an die betroffene Person, einschliesslich der geltend gemachten Ausnahme und der Beschwerderechte (Recht auf Beschwerde beim EDÖB oder zuständiger Aufsichtsbehörde), bereitstellen.
3. Verarbeitungseinschränkung anwenden, wo möglich (Daten aufbewahrt, aber nicht aktiv verarbeitet).
4. Überprüfungsdatum setzen, um zu beurteilen, ob die Ausnahme noch gilt.

### Benachrichtigung von Dritten

Wenn personenbezogene Daten, die einem Löschantrag unterliegen, an Dritte weitergegeben wurden, soll die Organisation diese Dritten über den Löschantrag gemäss DSGVO Art. 19 und nDSG-Verpflichtungen benachrichtigen, es sei denn, dies erweist sich als unmöglich oder beinhaltet einen unverhältnismässigen Aufwand.

---

## Aufbewahrungspflicht-Management

### Auslöser für Aufbewahrungspflichten

Die Löschung soll ausgesetzt werden, wenn Daten einer Aufbewahrungspflicht aus einem der folgenden Gründe unterliegen:

- Rechtsstreitigkeiten (eingeleitet, angedroht oder vernünftigerweise zu erwarten)
- Behördliche Untersuchung oder Regulierungsprüfung
- Interne Untersuchung mit forensischem Aufbewahrungsbedarf (Betrug, Fehlverhalten, Datenpanne)
- Externer Audit, der spezifische Datenaufbewahrung erfordert

### Einleitung und Aufhebung

Nur der Rechtsberater (oder designierter Rechts-/Compliance-Officer) kann eine Aufbewahrungspflicht einleiten oder aufheben.

**Einleitungsprozess**:

1. Rechtsberater erlässt formale Aufbewahrungsanordnung mit Dokumentation: Fallname/-nummer, Umfang (Systeme, Datumsbereiche, Verwahrer, Datenkategorien), Inkrafttreten, Aufbewahrungspflichten.
2. Betroffene Verwahrer werden innerhalb von 24 Stunden benachrichtigt und sollen den Empfang innerhalb von 2 Arbeitstagen bestätigen.
3. IT-Betrieb setzt automatische Löschung für betroffene Systeme innerhalb von 48 Stunden aus und bestätigt die Aussetzung schriftlich.
4. Rechtsberater pflegt Aufbewahrungsregister mit: Aufbewahrungskennung, Fallname, Ausgabedatum, Umfang, betroffene Systeme, Verwahrer, Bestätigungsstatus, Überprüfungsdaten.

### Vierteljährliche Überprüfung

Aufbewahrungspflichten sollen mindestens vierteljährlich vom Rechtsberater überprüft werden. Jede Überprüfung soll eine dokumentierte Bewertung produzieren, einschliesslich:

- Aufbewahrungskennung und Einleitungsdatum
- Aktueller Rechtsstreit-/Untersuchungsstatus
- Feststellung der fortbestehenden Notwendigkeit mit Rechtsgrundlage
- Anpassung des Umfangs falls zutreffend (Einengung auf spezifische Datenkategorien)
- Voraussichtliches Aufhebungsdatum oder -auslösebedingung
- Name und Datum des Überprüfers

### Aufhebung und Löschung nach Aufhebung

Bei Aufhebung:

1. Rechtsberater erlässt formale Aufhebungsanzeige.
2. Verwahrer und IT-Betrieb werden innerhalb von 24 Stunden benachrichtigt.
3. IT-Betrieb reaktiviert normale Löschpläne.
4. Daten, die ausschliesslich aufgrund der Aufbewahrungspflicht über die normale Aufbewahrungsfrist hinaus aufbewahrt wurden, sollen innerhalb von 90 Tagen nach Aufhebung gelöscht werden, sofern keine genehmigte Geschäftsbegründung vorliegt.

### Konflikt mit Löschanträgen

Wenn ein Löschantrag einer betroffenen Person mit einer aktiven Aufbewahrungspflicht in Konflikt gerät:

- Die Aufbewahrungspflicht hat Vorrang.
- Verarbeitungseinschränkung soll angewendet werden (Daten aufbewahrt, aber nicht aktiv genutzt).
- Löschung soll innerhalb von 30 Tagen nach Aufhebung erfolgen.
- Die betroffene Person soll darüber informiert werden, dass der Antrag zur Kenntnis genommen wurde, derzeit aber nicht erfüllt werden kann, unter Angabe der geltenden rechtlichen Ausnahme, ohne Details preiszugeben, die Rechtsverfahren beeinträchtigen könnten.

---

## Verifizierung und Nachweise

### Lösch-Audit-Trail

Die Organisation soll Lösch-Audit-Trails pflegen, einschliesslich:

| Feld | Beschreibung |
|------|--------------|
| **Löschzeitstempel** | Datum und Uhrzeit der Löschausführung |
| **Datenkategorie** | Typ und Klassifizierung der gelöschten Daten |
| **Löschmethode** | Angewendete Bereinigungsmethode (Clear / Purge / Destroy / Kryptographische Löschung) |
| **Medienkennung** | Systemname, Gerätseriennummer oder Speicherort |
| **Löschauslöser** | Ereignis, das die Löschung ausgelöst hat (Fristablauf, DSR, Ausserdienststellung usw.) |
| **Verantwortliche Partei** | Person oder System, das die Löschung durchgeführt hat |
| **Verifizierungsergebnis** | Bestätigung, dass die Löschung erfolgreich war |

### Aufbewahrung von Löschprotokollen

Löschprotokolle sollen mindestens 3 Jahre oder die anwendbare regulatorische Anforderung, je nachdem was länger ist, aufbewahrt werden. Löschprotokolle sollen nicht die gelöschten Daten selbst enthalten — nur Metadaten über das Löschereignis.

### Verifizierungsmethoden

Die Löscheffektivität soll verifiziert werden durch:

- **Automatische Verifizierung**: Systemgenerierte Bestätigung der erfolgreichen Löschung (API-Antwort, Tool-Output, Protokolleintrag)
- **Periodische Stichproben**: Vierteljährliche Stichprobe von Löschaufzeichnungen zur Verifizierung von Vollständigkeit und Richtigkeit (mindestens 10% Stichprobe der Löschungen pro Quartal)
- **Drittanbieter-Bestätigung**: Vernichtungszertifikate für physische Medien und externe Dienstleister
- **Stichprobenprüfungen**: Jährliche Stichprobenprüfung zufällig ausgewählter Systeme, um zu bestätigen, dass keine Daten über ihre Aufbewahrungsfrist hinaus existieren

---

## Ausnahmeverwaltung

### Ausnahmeanträge

Ausnahmen von standardmässigen Löschverfahren erfordern einen dokumentierten Antrag, einschliesslich:

- Datenkategorie und Klassifizierung
- Geschäftliche Begründung für die Ausnahme
- Risikobewertung (welches Risiko entsteht durch die Aufbewahrung der Daten über den normalen Zeitraum hinaus?)
- Kompensierende Kontrollen zur Minderung des Aufbewahrungsrisikos
- Vorgeschlagenes Ablaufdatum (Ausnahmen sollen nicht unbefristet sein)

### Genehmigungsbefugnis

| Datenklassifizierung | Ausnahmedauer | Genehmiger |
|----------------------|---------------|------------|
| Intern | Bis zu 12 Monate | Systemverantwortlicher + ISB |
| Vertraulich | Bis zu 6 Monate | ISB + DSB |
| Streng vertraulich | Jede Dauer | ISB + DSB + Rechtsberater + Geschäftsleitung |

### Verbotene Ausnahmen

Folgende Ausnahmen sollen nicht gewährt werden:

- Unbefristete Aufbewahrung ohne ein bestimmtes Enddatum oder einen Überprüfungsauslöser
- Ausnahmen zur Umgehung legitimer Löschanträge betroffener Personen
- Ausnahmen zur Umgehung regulatorischer Aufbewahrungsbeschränkungen
- Pauschale Ausnahmen für gesamte Datenkategorien ohne spezifische, dokumentierte Begründung

### Ausnahmeregister

Alle genehmigten Ausnahmen sollen im Ausnahmeregister mit Eigentümer, Genehmigungsdatum, Ablaufdatum, kompensierenden Kontrollen und Überprüfungsplan aufgezeichnet werden. Ausnahmen sollen vierteljährlich überprüft werden und automatisch ablaufen, sofern sie nicht durch den Genehmigungsprozess erneuert werden.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Informationslöschung** | Der Prozess des Entfernens von Daten aus Speichermedien, so dass sie durch normale oder, je nach Bereinigungsstufe, spezialisierte Methoden nicht wiederhergestellt werden können |
| **Datensanitierung** | Alle Methoden zur Unzugänglichmachung von Daten, einschliesslich Löschen, Bereinigen und Vernichten |
| **Löschen (Clear)** | Logische Sanitierung, die gegen Datenwiederherstellung mit Standard-Betriebssystemtools oder einfachen nicht-invasiven Techniken schützt |
| **Bereinigen (Purge)** | Physische oder logische Sanitierung, die gegen Datenwiederherstellung mit Laborangriffsverfahren schützt |
| **Vernichten (Destroy)** | Physische Zerstörung, die Medien unbrauchbar und Datenwiederherstellung durch jede bekannte Technik unmöglich macht |
| **Kryptographische Löschung** | Löschmethode, die verschlüsselte Daten durch sichere Vernichtung der Verschlüsselungsschlüssel unwiederherstellbar macht |
| **Aufbewahrungsfrist** | Definierter Zeitraum, während dessen Daten aufbewahrt werden müssen, bevor die Löschung erlaubt oder erforderlich ist |
| **Löschauslöser** | Ereignis oder Bedingung, die den Löschprozess einleitet (z. B. Fristablauf, Löschantrag) |
| **Aufbewahrungspflicht** | Aussetzung der Löschung zur Aufbewahrung von Daten für Rechtsstreitigkeiten, Untersuchungen, Regulierungsprüfungen oder Audits |
| **Löschantrag einer betroffenen Person** | Ein Antrag einer betroffenen Person, die ihr Recht auf Löschung gemäss nDSG oder DSGVO Art. 17 ausübt |
| **Vernichtungszertifikat** | Drittanbieter-Bestätigung, dass physische Medien gemäss einem bestimmten Standard vernichtet wurden |
| **Datenremanenz** | Restdaten, die nach Löschungsversuchen auf Speichermedien verbleiben; das Risiko, das Bereinigungsmethoden beseitigen sollen |
| **Dateneigentümer** | Einzelperson oder Rolle, die für die Definition des Geschäftszwecks, der Aufbewahrungsfrist und der Löschanforderungen für eine Datenkategorie verantwortlich ist |
| **Records Manager** | Rolle, die für die Pflege des organisationalen Aufbewahrungsplans und die Überwachung von Entsorgungsprozessen zuständig ist |

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; Genehmigung von Löschmethoden; Ausnahmegenehmigung; Compliance-Monitoring und -Kennzahlen; Eskalationspunkt bei Löschversagen |
| **DSB / Datenschutzberater** | Bearbeitung von Löschanträgen betroffener Personen; Datenschutz-Compliance; Überprüfung des Aufbewahrungsplans für personenbezogene Daten; Ausnahmegenehmigung (Vertraulich+) |
| **Rechtsberater** | Aufbewahrungspflicht-Management (Einleitung, Überprüfung, Aufhebung); Drittanbieter-Vertragsbedingungen (Löschklauseln); regulatorische Auslegung; Bewertung von Löschausnahmen |
| **Records Manager** | Pflege und jährliche Überprüfung des Aufbewahrungsplans; Entsorgungsaufsicht; Löschregisterverwaltung; Compliance-Tracking und -Berichterstattung |
| **IT-Betrieb** | Löschausführung; Verwaltung und Wartung von Löschtools; Backup-Löschung; Protokollierung und Verifizierung; Koordination der Drittanbieter-Löschung |
| **Systemverantwortliche** | Systemspezifische Löschimplementierung; Koordination mit IT-Betrieb; Ausnahmeanträge; Machbarkeitsbewertung automatisierter Löschung |
| **Dateneigentümer** | Definition der Aufbewahrungsfristen für eigene Datenkategorien; Genehmigung der Löschung geschäftskritischer Daten; Klassifizierungsentscheidungen |
| **Alle Mitarbeitenden** | Daten gemäss Klassifizierungs- und Aufbewahrungsanforderungen behandeln; keine Daten über autorisierte Zeiträume hinaus aufbewahren; vermutete Löschfehler melden |

---

## Nachweise

Die folgenden Nachweise belegen die Konformität mit dieser Richtlinie:

| # | Nachweis | Eigentümer | Häufigkeit | Aufbewahrung |
|---|---------|-----------|------------|--------------|
| 1 | **Aufbewahrungsplan** (aktuelle Version, genehmigt von Rechtsberater und Geschäftsleitung) | Records Manager | *Jährlich überprüft; versionskontrolliert* | Aktuelle + frühere Versionen (7 Jahre) |
| 2 | **Löschausführungsprotokolle** (Zeitstempel, Datenkategorien, Methoden, Verifizierungsergebnisse) | IT-Betrieb | *Kontinuierlich; vierteljährlich überprüft* | 3 Jahre |
| 3 | **Drittanbieter-Vernichtungszertifikate** (physische Medien, akkreditierte Anbieterzertifikate) | IT-Betrieb | *Pro Vernichtungsereignis* | 3 Jahre ab Vernichtungsdatum |
| 4 | **Datenschutz-Antragsregister** (eingegangene Anträge, Bewertung, Ergebnis, Abschlussdatum) | DSB / Datenschutzberater | *Pro Antrag; Register vierteljährlich überprüft* | 3 Jahre nach Antragsabschluss |
| 5 | **Aufbewahrungspflicht-Register** (aktive Pflichten, Umfang, vierteljährliche Überprüfungen, Aufhebungsaufzeichnungen) | Rechtsberater | *Aktive Pflichten vierteljährlich überprüft; Register kontinuierlich gepflegt* | 3 Jahre nach Aufhebung |
| 6 | **Ausnahmeregister** (genehmigte Ausnahmen mit Begründung, kompensierenden Kontrollen, Ablaufdaten) | ISB | *Vierteljährlich überprüft; beim Management-Review präsentiert* | Lebensdauer der Ausnahme + 3 Jahre |
| 7 | **Dateninventar** mit Aufbewahrungsfristen und Löschumfang pro Datenkategorie | Records Manager | *Jährlich überprüft; vierteljährliche Snapshots* | Aktuell + vierteljährliche Snapshots (3 Jahre) |
| 8 | **Vierteljährlicher Compliance-Bericht** (Löschkennzahlen: pünktliche Löschrate, überfällige Elemente, Ausnahmen, DSR-Reaktionszeiten) | ISB / Records Manager | *Vierteljährlich; beim Management-Review präsentiert* | 3 Jahre |
| 9 | **Cloud/SaaS-API-Löschprotokolle** (API-Aufrufaufzeichnungen, Ressourcenkennungen, Erfolgsbestätigungen) | IT-Betrieb | *Pro Löschereignis* | 3 Jahre |
| 10 | **Drittanbieter-Vertragsüberprüfungsaufzeichnungen** (Löschklauseln, Bewertungen der Drittanbieter-Löschfähigkeiten) | Rechtsberater / ISB | *Pro Vertrag; bei Vertragsverlängerung überprüft* | Vertragsdauer + 3 Jahre |
| 11 | **Automatische Löschkonfigurationsaufzeichnungen** (in Systemen konfigurierte Aufbewahrungsrichtlinien, Aufbewahrungspflicht-Integrationsstatus) | IT-Betrieb | *Halbjährlich überprüft* | Aktuelle Konfiguration + 3 Jahre |
| 12 | **Löschverifizierungs-Stichprobenergebnisse** (vierteljährliche Stichprobenaufzeichnungen, Stichprobenprüfungsbefunde) | Informationssicherheit | *Vierteljährliche Stichproben; jährliche Stichprobenprüfung* | 3 Jahre |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheits-Managementteam verifiziert die Einhaltung dieser Richtlinie durch verschiedene Methoden, einschliesslich unter anderem Löschprotokoll-Audits, Überprüfungen der Aufbewahrungsplan-Compliance, Tracking der Reaktionen auf Datenschutzanträge, Überprüfungen der Drittanbieter-Löschverifizierung, Ausnahmeregister-Reviews sowie interne und externe Audits.

**Wichtige Compliance-Kennzahlen**:

| # | Kennzahl | Ziel | Messhäufigkeit |
|---|----------|------|----------------|
| 1 | Pünktliche Löschrate (Löschungen innerhalb von 90 Tagen nach Fristablauf ausgeführt) | ≥ 95% | Vierteljährlich |
| 2 | Löschanträge betroffener Personen innerhalb von 30 Tagen abgeschlossen | 100% | Pro Antrag; vierteljährlich gemeldet |
| 3 | Drittanbieter-Vernichtungszertifikate für vertrauliche+ Daten erhalten | 100% | Pro Ereignis; vierteljährlich gemeldet |
| 4 | Aufbewahrungspflichten innerhalb des vierteljährlichen Zyklus überprüft | 100% | Vierteljährlich |
| 5 | Ausnahmeregister überprüft und aktuell (keine abgelaufenen, ungeprüften Ausnahmen) | 100% | Vierteljährlich |
| 6 | Aufbewahrungsplan-Abdeckung (Prozentsatz der Datenkategorien mit definierter Aufbewahrung) | 100% | Jährlich |
| 7 | Backup-Löschungsabschluss (Daten aus allen Backup-Kopien innerhalb dokumentierten Zeitrahmens gelöscht) | ≥ 90% | Vierteljährlich |

Kennzahlen, die Ziele verfehlen, sollen für sofortige Aufmerksamkeit an den ISB eskaliert und beim nächsten Management-Review gemeldet werden.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll im Voraus vom Information Security Manager genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, kompensierenden Kontrollen und einem definierten Überprüfungsdatum. Ausnahmen sollen dem Management-Review-Team gemeldet werden. Aufbewahrungsbezogene Ausnahmen erfordern die Genehmigung des Rechtsberaters.

## Nichtkonformität

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterzogen werden, bis hin zur Beendigung des Arbeitsverhältnisses. Unterlassung der Löschung personenbezogener Daten in Übereinstimmung mit gesetzlichen Anforderungen kann die Organisation zusätzlich regulatorischen Sanktionen aussetzen (nDSG Art. 60–66; DSGVO Art. 83 soweit anwendbar).

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Änderungen an Datenschutzvorschriften (nDSG, DSGVO, kantonale Anforderungen), Medienbereinigungsstandards (NIST SP 800-88, IEEE 2883), Cloud-Service-Anbieter-Löschfähigkeiten, aufkommenden Speichertechnologien, Audit-Befunde sowie Erkenntnisse aus Löschfehlern oder Datenschutzbeschwerden berücksichtigen.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Richtlinie zur Informationslöschung — ISO-27001-Controls-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Engagement | 5.1 Richtlinien zur Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Verantwortlichkeiten des Managements |
| Klausel 6.2 Informationssicherheitsziele | 5.9 Inventar von Informationen und anderen zugeordneten Werten |
| Klausel 7.3 Bewusstsein | 5.12 Klassifizierung von Informationen |
| Klausel 7.5.3 Kontrolle dokumentierter Informationen | 5.33 Schutz von Aufzeichnungen |
| | 5.34 Datenschutz und Schutz personenbezogener Daten |
| | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| | 6.3 Bewusstsein, Schulung und Training zur Informationssicherheit |
| | 6.4 Disziplinarverfahren |
| | 7.10 Speichermedien |
| | 7.14 Sichere Entsorgung oder Wiederverwendung von Betriebsmitteln |
| | **8.10 Informationslöschung** |
| | 8.13 Sicherung von Informationen |
| | 8.24 Einsatz von Kryptographie |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 6 — Grundsätze (Verhältnismässigkeit, Zweckbindung, Speicherbegrenzung); Art. 8 — Datensicherheit (technische und organisatorische Massnahmen); Art. 25 — Auskunftsrecht (umfasst Löschrechte); Art. 24 — Meldepflicht bei Datenpannen |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| Schweizer OR (Obligationenrecht) | Art. 957–958f — Buchführungs- und Aufzeichnungsaufbewahrungspflichten (10 Jahre); Art. 127–128 — Verjährungsfristen für Ansprüche |
| EU DSGVO (soweit anwendbar) | Art. 5(1)(e) — Speicherbegrenzung; Art. 17 — Recht auf Löschung; Art. 19 — Benachrichtigungspflicht bezüglich Löschung; Art. 32 — Sicherheit der Verarbeitung |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.10 — Informationslöschung |
| ISO/IEC 27002:2022 | Abschnitt 8.10 — Implementierungsleitfaden für die Informationslöschung |
| NIST SP 800-88 Rev. 2 | Guidelines for Media Sanitization (Clear, Purge, Destroy; kryptographische Löschung) |
| IEEE 2883 | Standard for Sanitizing Storage (medienspezifische Bereinigungstechniken) |
| NIST SP 800-53 Rev 5 | MP-6 (Media Sanitization), SI-12 (Information Management and Retention) |
| DIN 66399 | Klassifizierung von Sicherheitsstufen für die Vernichtung von Papier und Medien |

**Bedingte Frameworks** (gelten, wenn Geschäftsaktivitäten die Anwendbarkeit auslösen):

| Framework | Bedingung |
|-----------|-----------|
| PCI DSS v4.0 | Anwendbar wenn Zahlungskartendaten verarbeitet werden; erfordert sichere Löschung von Karteninhaberdaten wenn nicht mehr benötigt |
| FINMA-Rundschreiben | Anwendbar wenn die Organisation ein beaufsichtigtes Schweizer Finanzinstitut ist |
| HIPAA Security Rule | Anwendbar wenn US-amerikanische geschützte Gesundheitsinformationen verarbeitet werden |

---

<!-- QA_VERIFIED: 2026-03-29 -->
