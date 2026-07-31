<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.10-DE:framework:POL:a.8.10 -->
**ISMS-POL-A.8.10 — Richtlinie zur Informationslöschung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Richtlinie zur Informationslöschung |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.10 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Date] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstversion für ISO 27001:2022-Zertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL)
- Datenschutz: Datenschutzbeauftragter (DSB)
- Compliance: Rechts-/Compliance-Beauftragter
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-IMP-A.8.10.1 (Aufbewahrungs- und Löschauslöser-Bewertung)
- ISMS-IMP-A.8.10.2 (Löschmethoden-Bewertung)
- ISMS-IMP-A.8.10.3 (Drittanbieter- und Cloud-Löschbewertung)
- ISMS-IMP-A.8.10.4 (Verifizierungs- und Nachweisbewertung)
- ISO/IEC 27001:2022 Control A.8.10

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] an Informationslöschkontrollen fest, um die systematische Löschung von Informationen sicherzustellen, wenn diese nicht mehr benötigt werden — in Übereinstimmung mit ISO/IEC 27001:2022 Control A.8.10.

**Geltungsbereich**: Diese Richtlinie gilt für alle Informationsbestände unabhängig vom Speicherort (vor Ort, Cloud, Drittanbieter), alle Speichermedientypen (magnetisch, solid-state, optisch, Papier, Mobilgeräte), alle Systeme und Anwendungen (einschliesslich Backup-Infrastruktur) sowie alle Datenkategorien (personenbezogene Daten, Geschäftsunterlagen, technische Daten, Protokolle) während ihres gesamten Lebenszyklus.

**Zweck**: Definition der organisatorischen Anforderungen an die Implementierung und Steuerung von Informationslöschkontrollen. Diese Richtlinie legt fest, WELCHE Daten gelöscht werden müssen, WANN die Löschung erfolgen muss, WELCHE Methoden zulässig sind und WER verantwortlich ist. Implementierungsverfahren (WIE) sind separat in ISMS-IMP-A.8.10 dokumentiert.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen), einschliesslich des Schweizerischen Bundesgesetzes über den Datenschutz (nDSG) zu Datensparsamkeit und Recht auf Löschung, EU GDPR Artikel 17 (Recht auf Löschung) bei der Verarbeitung personenbezogener EU-Daten sowie ISO/IEC 27001:2022. Bedingt anwendbare branchenspezifische Anforderungen (PCI DSS v4.0.1, HIPAA, FINMA, DORA, NIS2) gelten, wenn die Geschäftstätigkeiten von [Organisation] deren Anwendbarkeit begründen.

---

# Kontrollausrichtung und Geltungsbereich

## ISO/IEC 27001:2022 Control A.8.10

**ISO/IEC 27001:2022 Annex A.8.10 — Informationslöschung**

> *Informationen, die in Informationssystemen, Geräten oder anderen Speichermedien gespeichert sind, sollten gelöscht werden, wenn sie nicht mehr benötigt werden.*

**Kontrollziel**: Etablierung einer organisatorischen Richtlinie für Informationslöschkontrollen, die die systematische Entfernung von Daten bei Erfüllung der Aufbewahrungsanforderungen gewährleistet und die Grundsätze der Datensparsamkeit, die regulatorische Compliance und den Schutz vor unbefugter Offenlegung unterstützt.

**Diese Richtlinie adressiert**:

- Aufbewahrungsfristen und Löschauslöser basierend auf gesetzlichen, regulatorischen, vertraglichen und geschäftlichen Anforderungen
- Löschmethoden, die für Medientypen, Datensensitivität und regulatorische Anforderungen geeignet sind
- Anforderungen an Verifizierung und Nachweise, um die durchgeführte Löschung zu belegen
- Löschverpflichtungen von Drittanbietern und Cloud-Dienstleistern sowie vertragliche Anforderungen
- Betroffenenrechte auf Löschung (GDPR Artikel 17, Schweizerisches nDSG)
- Management von Aufbewahrungssperren und Ausnahmebehandlung
- Integration in die Datenverwaltungs-, Datenschutz- und Risikobewertungsprozesse von [Organisation]

## Was diese Richtlinie bewirkt

Diese Richtlinie:

- **Definiert** Anforderungen an die Informationslöschung, ausgerichtet an Datenklassifizierung, regulatorischen Verpflichtungen und der Risikobereitschaft der Organisation
- **Etabliert** einen Governance-Rahmen für Löschentscheidungen, Ausnahmemanagement und Compliance-Überwachung
- **Spezifiziert** zulässige Löschmethoden und Auswahlkriterien basierend auf Medientyp und Datensensitivität
- **Referenziert** anwendbare regulatorische Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- **Identifiziert** organisatorische Rollen und Verantwortlichkeiten für die Implementierung und Überwachung von Löschkontrollen
- **Integriert** sich in verwandte Controls, einschliesslich Datenklassifizierung (A.5.12), Asset-Management (A.5.9), Datenschutz (A.5.34) und sichere Entsorgung (A.7.14)

## Was diese Richtlinie NICHT tut

Diese Richtlinie tut NICHT:

- **Löschtools oder -produkte festlegen** (Technologieauswahl basiert auf der Risikobewertung und den operativen Anforderungen von [Organisation])
- **Systemspezifische Löschverfahren definieren** (siehe ISMS-IMP-A.8.10 Assessment Guides für umgebungsspezifische Implementierungen)
- **Anbieterspezifische Löschanweisungen bereitstellen** (Cloud-Anbieter-Löschverfahren sind in ISMS-IMP-A.8.10.3 dokumentiert)
- **Die Datenklassifizierungsrichtlinie ersetzen** (Löschung baut auf dem bestehenden Klassifizierungsschema gemäss A.5.12 auf)
- **Aufbewahrungsfristen für alle Datentypen festlegen** (Aufbewahrungsfristen werden von Dateneigentümern mit rechtlichem/regulatorischem Input definiert und in ISMS-IMP-A.8.10.1 dokumentiert)
- **Zugangskontrollmechanismen definieren** (Zugangskontrollen sind durch A.5.15, A.5.18, A.8.3 abgedeckt)
- **Kryptografische Controls ersetzen** (Verschlüsselung zum Datenschutz ist in A.8.24 Kryptografie-Richtlinie abgedeckt; kryptografische Löschung als Löschmethode liegt jedoch im Geltungsbereich dieser Richtlinie)
- **Spezifische Sanitierungsstandards vorschreiben** (NIST SP 800-88 wird als Informationsreferenz verwendet, sofern nicht vertraglich gefordert)

## Geltungsbereich

**Diese Richtlinie gilt für**:

- **Alle Informationsbestände** (elektronisch und physisch) mit organisatorischen oder personenbezogenen Daten:
  - Personenbezogene Informationen (PII) gemäss GDPR/nDSG
  - Finanzdaten (Zahlungskartendaten, Finanzunterlagen, Transaktionsdetails)
  - Gesundheitsinformationen (medizinische Unterlagen, Mitarbeitergesundheitsdaten)
  - Authentifizierungsdaten (Passwörter, API-Schlüssel, Token, private Schlüssel)
  - Vertrauliche Geschäftsinformationen (Betriebsgeheimnisse, strategische Daten, Preisgestaltung, Verträge)
  - Technische Daten (Quellcode, Systemkonfigurationen, Netzwerkdiagramme)
  - Kommunikation (E-Mails, Sofortnachrichten, Anrufaufzeichnungen)
  - Systemprotokolle und Audit-Trails
  - Alle als Vertraulich oder Eingeschränkt klassifizierten Daten gemäss dem Klassifizierungsschema von [Organisation]

- **Alle Speicherorte**:
  - On-Premises-Infrastruktur (Rechenzentren, Serverräume, lokale Speicher)
  - Cloud-Umgebungen (IaaS, PaaS, SaaS bei allen Anbietern)
  - Drittanbieter-Verarbeiter (Managed Service Provider, Unterauftragnehmer, ausgelagerte Dienste)
  - Backup- und Notfallwiederherstellungssysteme (vor Ort, extern, cloudbasiert)
  - Endbenutzergeräte (Laptops, Desktops, Mobilgeräte, Wechselmedien)
  - Archive (physische Dokumentenspeicherung, Cold Storage, Magnetband)
  - Colocation-Einrichtungen und gehostete Infrastruktur

- **Alle Speichermedientypen**:
  - Magnetspeicher (Festplatten, Magnetbänder)
  - Solid-State-Speicher (SSDs, Flash-Laufwerke, SD-Karten)
  - Optische Medien (CDs, DVDs, Blu-rays)
  - Papierdokumente (gedruckte Dokumente, Formulare, Unterlagen)
  - Mobilgeräte (Smartphones, Tablets, Wearables)
  - Netzwerkgebundene Speicher (NAS, SAN)
  - Cloud-native Speicher (Objektspeicher, Blockspeicher, Dateispeicher)

- **Alle Lebenszyklusphasen**:
  - Operative Systeme (Produktionsdatenbanken, aktive Dateifreigaben)
  - Archivierte Daten (Compliance-Archive, inaktive Unterlagen)
  - Backup-Aufbewahrung (tägliche, wöchentliche, monatliche, jährliche Backups)
  - End-of-Life-Entsorgung (stillgelegte Systeme, ausgesonderte Medien)
  - Nicht-Produktionsumgebungen (Entwicklung, Test, QA, Schulung, Sandbox)

- **Alle Mitarbeiter und Dritte**:
  - Mitarbeiter (festangestellt, befristet, Praktikanten)
  - Auftragnehmer und Berater
  - Drittanbieter-Dienstleister, die organisatorische Daten verarbeiten
  - Cloud-Dienstleister, die Organisationsinformationen speichern
  - Ausgelagerte Entwicklungsteams und Managed Service Provider
  - Alle Geschäftsbereiche und geografischen Standorte von [Organisation]

**Ausserhalb des Geltungsbereichs**:

- **Aktive Legal-Hold-Daten**: Löschung ausgesetzt aufgrund von Rechtsstreitigkeiten, Ermittlungen oder Aufsichtsprüfungsanforderungen (separat in Abschnitt 2.6 geregelt)
- **Für laufende Aufsichtsprüfungen benötigte Daten**: Löschung bis zum Abschluss der Prüfung aufgeschoben; DSB/Rechtsgenehmigung erforderlich
- **Archivdokumente mit dauerhaften Aufbewahrungspflichten**: Löschung nicht anwendbar gemäss regulatorischen oder geschäftlichen Anforderungen; im Aufbewahrungsplan dokumentiert
- **Daten Dritter, bei denen [Organisation] nur als Auftragsverarbeiter handelt**: Löschung gemäss Weisung des Verantwortlichen
- **Absichtlich veröffentlichte öffentliche Informationen**: Separate Verfahren für Content-Management und Veröffentlichungsrücknahme
- **Anonymisierte Daten**: Unwiderruflich anonymisierte Daten (keine Identifizierung mehr möglich) erfordern keine datenschutzrechtliche Löschung

**Hinweis**: Ausnahmen vom Geltungsbereich befreien Systeme nicht von der Bewertung. ISMS-IMP-A.8.10-Bewertungen bestimmen die Anwendbarkeit; dokumentierte Ausnahmen erfordern geschäftliche Begründung und Genehmigung.

## Regulatorische Anwendbarkeit

Regulatorische Anforderungen werden gemäss **ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)** kategorisiert.

**Stufe 1: Verbindliche Compliance**

| Regulierung | Anwendbarkeit | Wesentliche Löschanforderungen |
|-------------|---------------|-------------------------------|
| **Schweizerisches nDSG (DSG)** | Alle Schweizer Tätigkeiten | Art. 6 – Grundsatz der Datensparsamkeit; Art. 12 – Recht der betroffenen Person auf Löschung; Art. 25 – Angemessene technische und organisatorische Sicherheitsmassnahmen; Art. 30 – Angemessene Sicherheit für die Datenverarbeitung |
| **EU GDPR** | Bei Verarbeitung personenbezogener EU-Daten | Art. 5(1)(e) – Grundsatz der Speicherbegrenzung; Art. 17 – Recht auf Löschung («Recht auf Vergessenwerden»); Art. 19 – Mitteilung der Löschung an Dritte; Art. 32 – Sicherheit der Verarbeitung einschliesslich Löschkontrollen |
| **ISO/IEC 27001:2022** | Zertifizierungsbereich | Control A.8.10 – Dokumentierte Informationslöschrichtlinie und -verfahren, implementierte Controls, Nachweise der Löscheffektivität |

**Stufe 2: Bedingte Anwendbarkeit**

Gilt nur, wenn spezifische Geschäftsbedingungen die Anwendbarkeit auslösen:

| Regulierung | Auslösebedingung | Löschanforderungen |
|------------|------------------|--------------------|
| **PCI DSS v4.0.1** | Verarbeitung von Zahlungskartendaten | Req. 3.1 – Karteninhaberdaten nur so lange aufbewahren wie für Geschäfts-/Rechtsanforderungen erforderlich; Req. 3.2 – Sichere Löschung; Req. 12.3.4 – Aufbewahrungs- und Entsorgungsverfahren |
| **HIPAA Security Rule** | Verarbeitung von US-Gesundheitsdaten (ePHI) | §164.310(d)(2)(i) – Entsorgungsstandard; §164.316(b)(2)(i) – Dokumentation 6 Jahre aufbewahren |
| **FINMA** | Reguliertes Schweizer Finanzinstitut | Aufbewahrung gemäss FINMA-Rundschreiben 2008/21; sichere Löschung nach Ablauf; Auslagerungsrisikomanagement (FINMA-RS 2018/3) |
| **DORA** | EU-Finanzdienstleistungseinheit | Art. 11 – IKT-Geschäftskontinuität; Art. 28 – IKT-Drittparteienrisikomanagement einschliesslich Datenlöschung bei Vertragsbeendigung |
| **NIS2** | Wesentliche/wichtige Einheit (EU) | Art. 21 – Cybersicherheits-Risikomanagement einschliesslich Datensicherheit und Löschung |
| **SOX** | US-börsennotiertes Unternehmen | 7-jährige Aufbewahrung von Prüfungsunterlagen; sichere Löschung danach |
| **CCPA/CPRA** | Verarbeitung von Daten Einwohner Kaliforniens | §1798.105 – Verbraucherrecht auf Löschung |

**Stufe 3: Informationsleitfäden**

Diese Rahmenwerke informieren die Implementierung, begründen jedoch keine verbindliche Compliance, sofern nicht vertraglich gefordert:

- **NIST SP 800-88 Rev. 1** – Leitfaden zur Mediensanitierung (Clear, Purge, Destroy)
- **ISO/IEC 27040:2015** – Speichersicherheit einschliesslich Sanitierungsleitfaden
- **ISO/IEC 27555:2024** – Leitlinien zur Löschung personenbezogener Daten
- **ISO/IEC 27017:2026** – Cloud-Dienste-Sicherheitskontrollen (Löschleitfaden)
- **DIN 66399** – Vernichtung von Datenträgern (7 Sicherheitsstufen)
- **DoD 5220.22-M** – Nationales Industrie-Sicherheitsprogramm (Altstandard, von NIST SP 800-88 abgelöst)

---

# Rahmenwerk für Anforderungen an die Informationslöschung

## Aufbewahrung und Löschauslöser

[Organisation] implementiert Aufbewahrungspläne, die festlegen, wann die Löschung erforderlich oder zulässig ist.

**Dateninventar und Klassifizierung**:

[Organisation] muss ein umfassendes Inventar der verarbeiteten Datenkategorien führen, das folgendes enthält:

- Datentyp und Format (strukturierte Datenbanken, unstrukturierte Dateien, E-Mail, Protokolle, Backups)
- Datenklassifizierungsstufe gemäss dem Klassifizierungsschema von [Organisation] (Eingeschränkt, Vertraulich, Intern, Öffentlich)
- Geschäftszweck und Verarbeitungsgrundlage
- Speicherort (System, Umgebung, Medientyp)
- Dateneigentümer, der für Aufbewahrungs- und Löschentscheidungen verantwortlich ist

**Überprüfung der Inventarvollständigkeit**:

Die Vollständigkeit des Inventars muss durch folgendes verifiziert werden:

- **(a) Automatisierte Discovery-Tools** für IT-Systeme (Scannen von Datenbanken, Dateifreigaben, Cloud-Speicher)
- **(b) Jährliche Attestierung** durch Systemeigentümer, die bestätigen, dass alle Datenkategorien in ihren Systemen im Inventar registriert sind
- **(c) Vierteljährliche Abstimmung** des Inventars mit dem IT-Asset-Register (gemäss ISMS-POL-A.5.9) und dem Cloud-Dienstleister-Register (gemäss ISMS-REF-A.5.23)

**Anforderungen an Aufbewahrungspläne**:

[Organisation] muss für alle Datenkategorien Aufbewahrungspläne erstellen, basierend auf:

- **Gesetzlichen Anforderungen**: Gesetze, Vorschriften, Gerichtsbeschlüsse mit spezifischen Aufbewahrungsfristen
- **Regulatorischen Anforderungen**: Branchenspezifische Vorschriften (PCI DSS, HIPAA, FINMA)
- **Vertraglichen Verpflichtungen**: Kundenverträge, Lieferantenvereinbarungen, Service-Level-Agreements
- **Dokumentierten Geschäftserfordernissen**: Operative Anforderungen, historische Analysen, begründet und genehmigt vom Dateneigentümer

Aufbewahrungspläne müssen dokumentieren:

- Datenkategorie und Unterkategorien
- Mindestaufbewahrungsfrist (gesetzliche/regulatorische Untergrenze)
- Höchstaufbewahrungsfrist (Datensparsamkeits-Obergrenze)
- Begründung der Aufbewahrungsfrist (Rechtsgrundlage, geschäftliche Begründung)
- Dateneigentümer und Genehmigung
- Überprüfungsdatum (mindestens jährlich)

**Löschauslöser**:

Die Löschung muss durch eines der folgenden Ereignisse ausgelöst werden:

**(a) Ablauf der Aufbewahrungsfrist**: Daten erreichen das Ende der genehmigten Aufbewahrungsfrist gemäss Aufbewahrungsplan

**(b) Löschanfrage der betroffenen Person**: Eine Person nimmt ihr Recht auf Löschung gemäss GDPR Artikel 17 oder Schweizerischem nDSG wahr (siehe Abschnitt 2.5)

**(c) Beendigung eines Vertrags oder einer Dienstleistungsvereinbarung**: Die Vertragsbeziehung endet, die Datenverpflichtung erlischt

**(d) Abschluss des Verarbeitungszwecks**: Der ursprüngliche Zweck der Datenerhebung/-verarbeitung ist nicht mehr gegeben

**(e) Aufhebung einer Aufbewahrungssperre (Legal Hold)**: Rechtsstreit, Ermittlung oder Aufsichtsprüfung abgeschlossen; Legal Hold wird aufgehoben (siehe Abschnitt 2.6)

**(f) Asset-Stilllegung**: IT-System, Gerät oder Speichermedium erreicht End-of-Life

**(g) Einwilligungswiderruf**: Betroffene Person widerruft Einwilligung zur Verarbeitung (wo Einwilligung Rechtsgrundlage gemäss GDPR Art. 6(1)(a))

**Konflikte bei Aufbewahrungsfristen**:

Bei mehreren auf dieselben Daten anwendbaren Aufbewahrungsanforderungen:

- Die **längste anwendbare Aufbewahrungsfrist** muss umgesetzt werden
- Bei Konflikten zwischen regulatorischen und vertraglichen Aufbewahrungspflichten ist eine Rechtsberatung erforderlich
- Konflikte sind im Aufbewahrungsplan mit Lösungsbegründung dokumentiert

**Automatisierte Löschprozesse**:

[Organisation] sollte automatisierte Löschprozesse implementieren, wo technisch möglich, einschliesslich:

- Aufbewahrungsmetadaten-Tagging (Erstellungsdatum, Aufbewahrungsfrist, Löschdatum)
- Automatisierte Löschplanung basierend auf Aufbewahrungsregeln
- Schutz vor vorzeitiger Löschung:
  - Prüfung auf Legal Holds vor der Löschausführung
  - Genehmigungsworkflow für Dateneigentümer bei wichtigen oder geschäftskritischen Daten
  - Löschbestätigung und Protokollierung

**Umsetzungshinweis**: Dateninventar-Methodik, Aufbewahrungsplan-Vorlagen, Löschauslöser-Workflows und Machbarkeitsbewertungsverfahren sind in **ISMS-IMP-A.8.10.1** dokumentiert.

---

## Anforderungen an Löschmethoden

[Organisation] implementiert Löschmethoden, die für Medientyp, Datensensitivität und regulatorische Anforderungen geeignet sind.

**Auswahl der Löschmethode**:

[Organisation] muss Löschmethoden auswählen, die geeignet sind für:

- **Medientyp**: Magnetisch (HDD), solid-state (SSD), optisch (CD/DVD), Papier, Cloud-Speicher, Band
- **Datenklassifizierungsstufe**: Eingeschränkt/Vertraulich erfordert stärkere Methoden als Intern/Öffentlich
- **Medienziel**: Interne Weiterverwendung vs. externe Übertragung vs. Entsorgung/Vernichtung
- **Wiederherstellungsrisikobewertung**: Wahrscheinlichkeit und Auswirkung einer unbefugten Datenwiederherstellung

**Zulässige Löschmethoden**:

Löschmethoden müssen mit anerkannten Sanitierungsstandards (NIST SP 800-88 oder Äquivalent) übereinstimmen:

| Methode | NIST SP 800-88-Stufe | Beschreibung | Anwendungsfälle |
|---------|---------------------|--------------|-----------------|
| **Clear** | Clear | Logische Techniken (Überschreiben, Blocklöschung) zum Schutz vor einfacher nicht-invasiver Wiederherstellung | Medien, die unter Organisationskontrolle verbleiben, mit Daten niedrigerer Sensitivität |
| **Purge** | Purge | Physische oder logische Techniken zum Schutz vor Labor-Angriffsmethoden (Entmagnetisierung, kryptografische Löschung, Secure Erase) | Medien, die die Organisationskontrolle verlassen; sensible Daten |
| **Destroy** | Destroy | Physische Zerstörung des Mediums (Schreddern, Pulverisieren, Verbrennen, Zerkleinern) | End-of-Life-Medien; Daten höchster Sensitivität |

**Löschmethoden nach Medientyp**:

| Medientyp | Zulässige Methoden | Hinweise |
|------------|-------------------|----------|
| **Magnetische HDD** | Überschreiben (7+ Durchläufe für sensible Daten), Entmagnetisieren, Physische Vernichtung | ATA Secure Erase zulässig, wenn unterstützt |
| **Solid-State (SSD, Flash)** | Kryptografische Löschung (bevorzugt), Secure-Erase-Befehl, Physische Vernichtung | Überschreiben wegen Wear-Leveling unzuverlässig; Secure Erase muss Erfolg verifizieren |
| **Optische Medien** | Physische Vernichtung (Schreddern, Pulverisieren) | Überschreiben nicht anwendbar; Vernichtung auf Purge-Niveau erforderlich |
| **Magnetband** | Entmagnetisieren, Physische Vernichtung | Überschreiben für Clear zulässig, aber zeitaufwändig |
| **Papierdokumente** | Kreuzschnitt-Schreddern (DIN 66399 P-4 Minimum für Vertraulich) | Sicherheitsstufe basiert auf Datensensitivität |
| **Mobilgeräte** | Werksreset + Verschlüsselungsverifizierung, Physische Vernichtung bei hoher Sensitivität | Verschlüsselung muss aktiviert gewesen sein; Werksreset allein unzureichend für Eingeschränkt |
| **Cloud-Speicher (IaaS/PaaS)** | API-Löschung + Verifizierung, Kryptografische Löschung bei kundenverwalteten Schlüsseln | Multi-Regions-Löschung verifizieren; Snapshot/Backup-Löschung einbeziehen |
| **Cloud-Speicher (SaaS)** | Anbieter-Löschprozess gemäss Vertrag; Löschnachweis einholen | Eingeschränkte Kundenkontrolle; auf SOC 2 Löschkontrollen des Anbieters verlassen |

> **Detaillierte Anleitung**: Anhang A enthält eine umfassende Löschmethoden-Auswahlmatrix, NIST SP 800-88-Zuordnung und methoden-/medienspezifische Anforderungen.

**Löschung in Produktionssystemen**:

Die Löschung in Produktionssystemen muss sich erstrecken auf:

- **ALLE Backup-Kopien**: Inkrementelle/differentielle Backups, vollständige Backups, Snapshots, Notfallwiederherstellungsreplikate
- **ALLE Replikate und Spiegel**: Datenbankreplikate, Speicherspiegel, CDN-Caches
- **ALLE temporären Kopien**: Auslagerungsdateien, temporäre Verarbeitungsdateien, Systemcaches
- **ALLE Protokolldateien**: Anwendungs-, System- und Zugriffsprotokolle, die die gelöschten Daten enthalten

**Backup-Löschverifizierung**:

Die Backup-Löschverifizierung muss die Backup-Technologiearchitektur berücksichtigen. Wo eine sofortige Backup-Löschung technisch nicht machbar ist, muss die **maximale Aufbewahrungsfrist dokumentiert** und von ISB + Dateneigentümer genehmigt werden.

**Genehmigung für aufgeschobene Backup-Löschung**: Wenn eine Löschung von mehr als 90 Tagen über die Standard-Aufbewahrungsfrist hinaus erforderlich ist, ist eine Genehmigung von ISB, Dateneigentümer und DSB (bei personenbezogenen Daten) einzuholen.

**Kryptografische Löschung als Löschmethode**:

Wo technisch machbar, sollte [Organisation] kryptografische Löschung nutzen:

- **Datenschlüssel-Zuordnung**: Dokumentieren, welche Verschlüsselungsschlüssel welche Datenkategorien schützen
- **Schlüsselvernichtungsverfahren**: Schlüsselvernichtung gemäss NIST SP 800-88 «Purge»-Niveau implementieren
- **Schlüsselvernichtungsverifizierung**: Durch Audit-Protokolle des Schlüsselmanagementsystems oder HSM-Zertifikate verifizieren
- **Integration mit A.8.24**: Schlüsselmanagement-Lebenszyklus gemäss ISMS-POL-A.8.24

Damit kryptografische Löschung als Löschung gemäss dieser Richtlinie gilt, muss die Vernichtung der Verschlüsselungsschlüssel die verschlüsselten Daten **unwiederbringlich** machen (kein Key Recovery, kein Key Escrow, keine aufbewahrten Schlüssel-Backups).

**Verbotene Löschpraktiken**:

Folgendes ist als Löschmethode NICHT zulässig:

- **Dateilöschung ohne Überschreiben**: Einfaches Löschen oder Papierkorb, bei dem Daten wiederherstellbar bleiben
- **Schnellformatierung ohne Überschreiben**: Dateisystem-Metadaten gelöscht, Daten bleiben erhalten
- **Einmaliges Überschreiben von Solid-State-Medien**: Wear-Leveling macht Überschreiben für SSDs unzuverlässig
- **Entmagnetisieren von Solid-State- oder optischen Medien**: Wirkungslos auf nicht-magnetischen Medien
- **Verschlüsselung ohne Schlüsselvernichtung**: Verschlüsselte Daten mit vorhandenen Schlüsseln sind nicht gelöscht
- **Umbenennen oder Verschieben von Dateien**: Verschleierung ist keine Löschung

---

## Löschung bei Drittanbietern und in der Cloud

[Organisation] implementiert Löschverpflichtungen für Drittanbieter und Cloud-Dienstleister, die Organisationsdaten verarbeiten.

**Vertragliche Löschanforderungen für Drittanbieter**:

[Organisation] muss Löschverpflichtungen in alle Verträge mit Drittanbietern aufnehmen, die Organisationsdaten verarbeiten:

**(a) Maximale Löschfrist**: Daten innerhalb einer festgelegten Frist nach Vertragsbeendigung oder auf Anfrage gelöscht (typisch 30–90 Tage)

**(b) Sanitierungsstandards**: Löschmethoden entsprechend der Datensensitivität (Verweis auf NIST SP 800-88 oder Äquivalent)

**(c) Löschungsumfang**: Alle Kopien einschliesslich Backups, Replikate, Archive, Notfallwiederherstellung sowie Entwicklungs-/Testumgebungen

**(d) Anforderung an Vernichtungsnachweis**: Anbieter muss einen Löschnachweis oder eine Bestätigung über den Abschluss der Löschung bereitstellen

**(e) Weitergabe an Sub-Verarbeiter**: Löschanforderungen gelten für alle Sub-Verarbeiter

**(f) Prüfungsrechte**: [Organisation] behält das Recht, die Löschung durch Prüfung oder Inspektion zu verifizieren

**Bewertung der Löschfähigkeiten von Cloud-Anbietern**:

[Organisation] muss die Löschfähigkeiten von Cloud-Anbietern vor der Beauftragung anhand folgender Mindestkriterien bewerten:

**(a) API-Löschunterstützung**: Programmatische Löschung und Verifizierungsmöglichkeit

**(b) Löschfrist-Zusagen**: SLA-gestützte Löschfrist (z.B. «innerhalb von 30 Tagen nach Anfrage gelöscht»)

**(c) Multi-Mandanten-Isolationsverifizierung**: Kundendatenlöschung beeinträchtigt keine anderen Mandanten

**(d) Geografische Löschungsabdeckung**: Löschung erfolgt in allen Regionen, in denen Daten repliziert werden

**(e) Backup-/Snapshot-Löschprozess**: Explizite Einbeziehung von Backups in den Löschungsumfang

**(f) Verfügbarkeit von Lösch-Audit-Trails**: Löschprotokolle für Kunden zur Compliance-Verifizierung zugänglich

Bewertungsergebnisse sind in **ISMS-REF-A.5.23 (Cloud-Dienstleister-Register)** zu dokumentieren.

**Drittanbieter-Löschverifizierung**:

[Organisation] muss Löschverifizierungen von Drittanbietern einholen durch:

**(a) Vernichtungsnachweise** (für physische Medienvernichtung)

**(b) Prüfberichte** (für logische Löschung durch Dienstleister):
- SOC 2 Type II-Bericht mit Prüfung der Löschkontrollen, oder
- Unabhängiger Prüfbericht zur Verifizierung der Löschverfahren, oder
- ISO 27001-Zertifizierung mit Annex A.8.10 im Zertifizierungsumfang

**(c) API-Antwortprotokollierung** (für Cloud-/SaaS-Löschung)

**Bei Hoch/Kritisch klassifizierten Daten**: Zertifikate von akkreditierten Vernichtungsanbietern (NAID AAA, ISO 21964) ODER unabhängige Prüfberichte sind erforderlich.

**Eskalation bei Löschversagen Dritter**:

| Zeitrahmen | Massnahme | Verantwortlich |
|------------|-----------|----------------|
| **T+0 Tage** | IT-Betrieb protokolliert Versagen im Gap-Register, leitet Nachfrage ein | IT-Betrieb |
| **T+15 Tage** | Systemeigentümer eskaliert an Account-Manager des Drittanbieters, informiert ISB + DSB | Systemeigentümer |
| **T+30 Tage** | ISB eskaliert an Führungskraft des Drittanbieters, leitet Vertragsüberprüfung mit Legal ein | ISB |
| **T+45 Tage** | Geschäftsleitung prüft vertragliche Rechtsbehelfe (Servicegutschriften, Kündigung wegen wesentlicher Verletzung) | Geschäftsleitung |

**Bei hochsensiblen Daten**: Eskalation beschleunigt (T+7, T+15, T+21, T+30 Tage).

---

## Verifizierungs- und Nachweisanforderungen

[Organisation] führt umfassende Löschnachweise, um die Compliance zu demonstrieren.

**Lösch-Audit-Trail**:

[Organisation] muss umfassende Lösch-Audit-Trails führen, einschliesslich:

- **Lösch-Zeitstempel**: Datum und Uhrzeit der Löschung
- **Datenkategorie**: Art der gelöschten Daten
- **Löschmethode**: Verwendete Technik (Clear, Purge, Destroy, kryptografische Löschung)
- **Medienidentifikator**: System, Gerät oder Speicherort, an dem die Löschung erfolgte
- **Löschauslöser**: Ereignis, das die Löschung ausgelöst hat
- **Verantwortliche Partei**: Person oder System, das die Löschung ausgeführt hat
- **Verifizierungsergebnis**: Bestätigung des Löscherfolgs oder Fehlerdetails

Löschprotokolle müssen:

- **Manipulationssicher** sein: Geschützt gegen unbefugte Änderung (Write-Once-Protokollierung, kryptografische Signierung, SIEM-Integration)
- **Aufbewahrt** werden: Mindestens **3 Jahre** oder gemäss den anwendbaren regulatorischen Anforderungen (je nachdem, was länger ist)
- **Zugänglich** sein: Für Prüfungen, Compliance-Verifizierungen und Anfragen betroffener Personen verfügbar

**Löschnachweise**:

[Organisation] muss Löschnachweise für folgendes erstellen oder einholen:

- **Hoch/Kritisch klassifizierte Daten**: Alle Löschungen von Eingeschränkten oder Vertraulichen Daten
- **Drittanbieter-Löschung**: Alle durch externe Parteien durchgeführten Löschungen
- **Physische Medienvernichtung**: Alle physischen Vernichtungen von Speichermedien
- **Löschanfragen betroffener Personen**: Alle GDPR/nDSG-Löschanfragen

**Nachweisanforderungen**:

| Nachweistyp | Zweck | Eigentümer | Aufbewahrung |
|-------------|-------|------------|--------------|
| **Löschausführungsprotokolle** | Nachweis planmässiger Löschungen | IT-Betrieb | 3 Jahre Minimum |
| **Aufbewahrungsplan** | Definition genehmigter Aufbewahrungsfristen nach Datenkategorie | Records Manager | Aktuelle + abgelöste Versionen (7 Jahre) |
| **Drittanbieter-Vernichtungsnachweise** | Verifizierung der Drittanbieter-Löschcompliance | IT-Betrieb | 3 Jahre ab Löschdatum |
| **Protokoll zu Anfragen betroffener Personen** | Nachweis der GDPR/nDSG-Rechte-Compliance | DSB | 3 Jahre ab Anfrageabschluss |
| **Legal-Hold-Register** | Begründung der Löschaussetzung | Rechts-/Compliance-Beauftragter | 3 Jahre ab Hold-Aufhebung |
| **Ausnahmegenehmigungen** | Dokumentation genehmigter Abweichungen | ISB | Dauer der Ausnahme + 3 Jahre |
| **Vierteljährliche Compliance-Berichte** | Aggregierte Löschmetriken, Gap-Analyse | ISB | 3 Jahre |
| **Dateninventar** | Festlegung des Löschungsumfangs | Records Manager | Aktuelle + vierteljährliche Snapshots (3 Jahre) |
| **Backup-Löschverifizierungsunterlagen** | Nachweis der Backup-Bereinigung | IT-Betrieb | 3 Jahre |

**Nachweiszugänglichkeit**: Alle Nachweise müssen für Prüfer, Regulatoren und interne Compliance-Überprüfungen leicht zugänglich sein. Nachweisanfragen müssen innerhalb von **5 Werktagen** bei Routineüberprüfungen und **24 Stunden** bei Aufsichtsprüfungen erfüllt werden.

---

## Löschanfragen betroffener Personen

[Organisation] implementiert Verfahren zur Bearbeitung von Löschanfragen betroffener Personen in Übereinstimmung mit GDPR Artikel 17 und Schweizerischem nDSG.

**Annahme und Protokollierung von Anfragen**:

[Organisation] muss Löschanfragen betroffener Personen annehmen und verarbeiten:

**(a) Mehrere Kanäle**: Anfragen per E-Mail, Webformular, Postweg oder persönlich an [Organisation]-Büros entgegennehmen

**(b) Sofortige Protokollierung**: Alle Anfragen innerhalb von **24 Stunden** nach Eingang im Anfragenregister protokollieren

**(c) Identitätsverifizierung**: Identität der betroffenen Person vor der Bearbeitung verifizieren

**(d) Reaktionsfrist**: Antwort an betroffene Person innerhalb von **30 Tagen** (GDPR-Frist)

**Rechtliche Beurteilung der Löschpflicht**:

Der DSB muss beurteilen, ob eine Löschpflicht besteht oder rechtliche Ausnahmen vorliegen:

**Löschung ist ERFORDERLICH, wenn**:
- Personenbezogene Daten für den Erhebungszweck nicht mehr notwendig sind
- Betroffene Person Einwilligung widerruft
- Betroffene Person Widerspruch einlegt und keine vorrangigen legitimen Gründe vorliegen
- Personenbezogene Daten unrechtmässig verarbeitet wurden
- Löschung zur Erfüllung einer rechtlichen Verpflichtung erforderlich ist
- Daten für Informationsgesellschaftsdienste für Kinder erhoben wurden (GDPR Art. 8)

**Löschung kann VERWEIGERT werden** (GDPR Art. 17(3) Ausnahmen):
- Verarbeitung für die Ausübung des Rechts auf freie Meinungsäusserung und Information erforderlich
- Verarbeitung zur Erfüllung einer rechtlichen Verpflichtung erforderlich
- Verarbeitung im öffentlichen Interesse erforderlich
- Verarbeitung für Gesundheitszwecke im öffentlichen Interesse erforderlich
- Verarbeitung für im öffentlichen Interesse liegende Archivzwecke, Forschung oder statistische Zwecke erforderlich
- Verarbeitung zur Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen erforderlich

**Benachrichtigung Dritter**:

Bei Weitergabe personenbezogener Daten an Dritte muss [Organisation] diese gemäss GDPR Artikel 19 innerhalb von **7 Tagen** nach Ausführung der Löschung benachrichtigen.

**Ausführung der Löschung**:

Genehmigte Löschanfragen müssen ausgeführt werden:

**(a) Umfang**: Alle personenbezogenen Daten der betroffenen Person löschen über alle Systeme, Backups, Archive, Drittanbieter, Entwicklungs-/Testumgebungen und Protokolle

**(b) Frist**: Löschung innerhalb von **60 Tagen** ab Eingang der Anfrage abschliessen (30 Tage für Beurteilung + 30 Tage für Ausführung)

**(c) Verifizierung**: Vollständigkeit der Löschung durch Datenbankabfragen, Dateisystemsuchen, Drittanbieter-Vernichtungsnachweise und Backup-Verifizierung bestätigen

**Protokoll zu Anfragen betroffener Personen**:

Der DSB führt ein Protokoll mit folgenden Feldern:

| Feld | Beschreibung |
|------|--------------|
| **Anfrage-ID** | Eindeutiger Identifikator |
| **Eingangsdatum** | Datum des Anfrageneingangs |
| **Anfragekanal** | E-Mail, Webformular, Post, persönlich |
| **Betroffene Person** | Name und Kontakt (nach Abschluss anonymisiert) |
| **Identitätsverifizierung** | Methode und Datum |
| **Anfragetyp** | Löschung, Auskunft, Berichtigung, Übertragbarkeit, Widerspruch |
| **Beurteilung** | DSB-Entscheidung (genehmigen, ablehnen, teilweise) |
| **Rechtsgrundlage** | GDPR Art. 17(3)-Ausnahme bei Ablehnung |
| **Ausführungsdatum** | Datum des Löschungsabschlusses |
| **Drittanbieter-Benachrichtigung** | Benachrichtigte Dritte und Datum |
| **Antwortdatum** | Datum der Benachrichtigung der betroffenen Person |
| **Status** | Offen, In Bearbeitung, Abgeschlossen, Abgelehnt |

Aufbewahrungsdauer des Protokolls: **3 Jahre** ab Anfrageabschluss.

---

## Management von Aufbewahrungssperren (Legal Holds)

[Organisation] implementiert Legal-Hold-Verfahren, um die Löschung bei Rechtsstreitigkeiten, Ermittlungen oder Aufsichtsprüfungen auszusetzen.

**Definition einer Aufbewahrungssperre**:

Ein **Legal Hold** (Aufbewahrungssperre) ist eine Aussetzung normaler Löschprozesse zur Aufbewahrung von Daten für:

- **Rechtsstreitigkeiten**: Eingereichte Klagen, drohende oder vernünftigerweise antizipierte Rechtsstreitigkeiten
- **Behördliche Ermittlungen**: Regulatorische Untersuchung, strafverfolgungsrechtliche Anfrage, Vorladung, Durchsuchungsbefehl
- **Interne Ermittlungen**: Betrugsermittlung, Ethikverstoss, Sicherheitsvorfall mit forensischem Sicherungsbedarf
- **Externe Prüfung**: Aufsichtsprüfung, Finanzprüfung, Compliance-Prüfung

**Legal-Hold-Befugnis**:

AUSSCHLIESSLICH der **Rechts-/Compliance-Beauftragte** ist berechtigt:

**(a)** Einen Legal Hold zu initiieren
**(b)** Den Umfang des Holds zu definieren (Datenkategorien, Verwahrer, Zeitraum, Grund)
**(c)** Einen Legal Hold aufzuheben, wenn die rechtliche Verpflichtung endet

**Vierteljährliche Legal-Hold-Überprüfung**:

Legal Holds müssen **mindestens vierteljährlich** auf anhaltende Notwendigkeit überprüft werden. Jede Überprüfung muss einen **unterzeichneten Legal-Hold-Überprüfungsbericht** erstellen.

**Legal-Hold-Aufhebung und Löschung**:

Bei Aufhebung eines Legal Holds:

**(a)** Schriftliche Aufhebungsgenehmigung des Rechts-/Compliance-Beauftragten
**(b)** Ausführung der Löschung durch IT-Betrieb innerhalb von **90 Tagen** nach Hold-Aufhebung
**(c)** Verifizierung der Löschung gemäss Abschnitt 2.4

---

## Protokollierung und Überwachung

[Organisation] implementiert die Protokollierung von Löschaktivitäten zur Unterstützung der Sicherheitsüberwachung und Compliance-Verifizierung.

**Protokollierungsanforderungen bei Löschung**:

Folgende löschbezogene Ereignisse müssen protokolliert werden:

**(a) Ausführung des Löschprozesses**: Startzeit, Datenkategorie, Löschmethode, Umfang, Auslöser, Abschlusszeit und -status

**(b) Änderungen an der Löschkonfiguration**: Änderungen an Aufbewahrungsplänen, Löschregeln oder Löschmethoden

**(c) Ausnahmen und Umgehungen**: Eingereichte Ausnahmeanträge, Legal Holds, manuelle Überschreibungen

**Protokoll-Aufbewahrungsfristen**:

- **Löschprozess-Protokolle**: Minimum **90 Tage** (operatives Debugging)
- **Löschkonfigurations-Änderungen**: Minimum **12 Monate**
- **Ausnahme- und Umgehungsereignisse**: Minimum **12 Monate**
- **Protokolle zu Anfragen betroffener Personen**: Minimum **3 Jahre**
- **Legal-Hold-Register**: Minimum **3 Jahre ab Hold-Aufhebung**

**Überwachung und Alarmierung**:

[Organisation] überwacht:

**(a) Löschprozessfehler**: Alert IT-Betrieb innerhalb 1 Stunde, Eskalation an Systemeigentümer wenn nicht innerhalb 4 Stunden behoben

**(b) Wiederholte Umgehungsversuche**: Alert Security-Team sofort, mögliche Richtlinienverletzung untersuchen

**(c) Konfigurationsänderungen an Löschregeln**: Alert Security-Team innerhalb 1 Stunde, Genehmigungsverifizierung einfordern

**(d) Annähernde Fristen bei Anfragen betroffener Personen**: Bei Löschanfragen innerhalb von 7 Tagen der 30-tägigen GDPR-Frist ohne Abschluss — Alert an DSB sofort

---

# Rollen, Governance und Ausnahmemanagement

## Rollen und Verantwortlichkeiten

**Geschäftsleitung/Vorstand**:

- **Accountable für**: Genehmigung der Informationslöschrichtlinie und -strategie; Sicherstellung angemessener Ressourcen
- **Akzeptanz von Restrisiken**: Formale Risikoakzeptanz wo Löschung technisch oder operativ nicht machbar
- **Strategische Aufsicht**: Überprüfung der Effektivität des Löschprogramms durch vierteljährliche Compliance-Berichte

**Informationssicherheitsbeauftragter (ISB)**:

- **Accountable für**: Gesamte Informationslöschrichtlinie und Programmeffektivität
- **Richtlinieneigentümerschaft**: Genehmigung von Richtlinienaktualisierungen, Löschmethodenstandards und Implementierungsverfahren
- **Ausnahmegenehmigung**: Genehmigung von Hochrisiko-Ausnahmen gemäss Befugnismatrix (Abschnitt 3.3)
- **Risikomanagement**: Definition der Risikobereitschaft der Organisation für Datensicherheit
- **Jährliche Richtlinienüberprüfung**: Leitung der jährlichen Überprüfung mit DSB, Legal/Compliance und ITL

**Datenschutzbeauftragter (DSB)**:

- **Accountable für**: GDPR/nDSG-Compliance für Löschkontrollen; Management der Betroffenenrechte
- **Anfragen betroffener Personen**: Bearbeitung von Löschanfragen gemäss Abschnitt 2.5
- **Regulatorische Liaison**: Koordination mit FDPIC oder EU-Datenschutzbehörden

**Rechts-/Compliance-Beauftragter**:

- **Accountable für**: Legal-Hold-Management (Abschnitt 2.6); rechtliche Anforderungen an Aufbewahrungsfristen
- **Legal-Hold-Befugnis**: EINZIGE Rolle, die Legal Holds initiieren oder aufheben darf

**IT-Leiter (ITL) / IT-Direktor**:

- **Accountable für**: Technologieinfrastruktur für Löschkontrollen; Ressourcenzuteilung für IT-Betrieb

**IT-Betrieb**:

- **Verantwortlich für**: Ausführung der Löschprozesse; Pflege von Löschtools; Protokollierung von Löschaktivitäten

**Systemeigentümer**:

- **Verantwortlich für**: Löschimplementierung in ihren Systemen; Koordination mit IT-Betrieb und Dateneigentümern

**Dateneigentümer**:

- **Verantwortlich für**: Datenklassifizierung; Bestimmung von Aufbewahrungsfristen; Genehmigung der Löschung ihrer Datenbereiche

**RACI-Matrix**:

| Aktivität | Geschäftsleit. | ISB | DSB | Legal/Compl. | ITL | IT-Betr. | Sys.-Eig. | Daten-Eig. | Nutzer |
|-----------|----------------|------|-----|--------------|-----|----------|-----------|------------|--------|
| Richtliniengenehmigung | A | V | B | B | B | I | I | I | I |
| Aufbewahrungsfrist-Definition | I | B | B | B | I | I | B | V/A | I |
| Löschausführung | I | A | I | I | B | V | B | I | I |
| Anfragen betroffener Personen | I | B | V/A | B | I | B | I | I | I |
| Legal Holds | I | B | B | V/A | I | B | I | I | I |
| Ausnahmegenehmigung | A | V/A | B | B | I | I | B | V | I |
| Drittanbieter-Verifizierung | I | A | I | B | I | V | B | I | I |
| Überwachung & Alarmierung | I | A | I | I | B | V | B | I | I |

**Legende**: V = Verantwortlich (führt aus), A = Accountable (Ergebnisverantwortung), B = Beratend (Input gesucht), I = Informiert (wird informiert)

---

## Bewertung und Verifizierung

[Organisation] verifiziert die Effektivität der Löschkontrollen durch ein strukturiertes Bewertungsprogramm.

**Bewertungsdomänen**:

| Domäne | Bewertungsfokus | IMP-Dokument |
|--------|-----------------|--------------|
| **1. Dateninventar & Aufbewahrung** | Datenkategorien, Aufbewahrungspläne, Löschauslöser, Vollständigkeitsverifizierung | ISMS-IMP-A.8.10.1 |
| **2. Löschmethoden** | Medientypen, Löschtools, Backup-Koordination, Methodenangemessenheit | ISMS-IMP-A.8.10.2 |
| **3. Drittanbieter & Cloud** | Anbieterinventar, Löschfähigkeiten, Verträge, Zertifikate | ISMS-IMP-A.8.10.3 |
| **4. Verifizierung & Nachweis** | Löschprotokolle, Zertifikate, Anfragen betroffener Personen, Legal Holds | ISMS-IMP-A.8.10.4 |

**Bewertungsfrequenz**:

- **Umfassende Bewertung**: **Jährlich** — alle Domänen, alle Systeme, Executive-Überprüfung
- **Periodische Verifizierung**: **Vierteljährlich** — Hochrisikosysteme, kürzliche Änderungen
- **Ausgelöste Bewertung**: **Innerhalb von 30 Tagen** nach wesentlichen Sicherheitsvorfällen, grossen Systemänderungen, neuen Datenverarbeitungsaktivitäten oder regulatorischen Änderungen

---

## Ausnahmemanagement

**Verbotene Ausnahmen**:

Folgende Ausnahmeanträge sind **NICHT ZULÄSSIG**:

- **Unbegrenzte Aufbewahrung ohne spezifisches Enddatum**
- **Ausnahmen zur Umgehung legitimer Löschanfragen betroffener Personen**
- **Ausnahmen zur Umgehung regulatorisch vorgeschriebener Aufbewahrungsanforderungen**
- **Pauschalausnahmen für gesamte Datenkategorien ohne spezifische Begründung**
- **Ausnahmen ohne kompensierende Massnahmen**
- **Ausnahmen zur Umgehung von Legal-Hold-Anforderungen**
- **Wiederholte Ausnahmen für dasselbe Problem ohne Compliance-Fortschritt**

**Ausnahmedokumentation**:

Alle genehmigten Ausnahmen müssen dokumentiert werden, einschliesslich:

**(a) Ausnahmen-ID**: Eindeutige ID (Format: EXC-A810-JJJJ-NNN)

**(b) Anfragemetadaten**: Antragsdatum, anfragende Partei, Dateneigentümergenehmigung, betroffene Systeme

**(c) Geschäftliche Begründung**: Detaillierte Erläuterung, warum die Standard-Löschanforderung nicht erfüllt werden kann; Auswirkung bei Ablehnung; Bedauerfrist mit konkretem Start- und Enddatum

**(d) Risikobewertung**: Inhärentes Risiko, Bedrohungsszenarien, Compliance-Auswirkung, kompensierende Massnahmen, Restrisiko, Risikoakzeptanz

**(e) Genehmigungskette**: Dateneigentümer, Security-Team, ISB, Geschäftsleitung, Rechts-/Compliance-Beauftragter, DSB (je nach Anforderung)

**(f) Überwachung und Überprüfung**: Überprüfungsplan, Überwachungsanforderungen, Widerrufsauslöser

**(g) Compliance-Pfad**: Sanierungsplan mit Meilensteinen, Ressourcenbedarf, Zeitzielen

**Ausnahme-Überprüfungsplan**:

Aktive Ausnahmen werden überprüft:

**(a) Gemäss Plan**: Monatlich (Kritisch), Vierteljährlich (Hoch), Halbjährlich (Mittel)
**(b) Im Ausnahmeregister verfolgt**: Zentrales Register des Security-Teams
**(c) Widerrufen bei Änderungen**: Geschäftsbegründung entfällt; kompensierende Massnahmen versagen; Risikoprofil erhöht sich; Lösung verfügbar

**Ausnahmeverlängerung**:

Verlängerungen erfordern aktualisierte Risikobewertung, Neuzertifizierung der Geschäftsbegründung und Compliance-Fortschrittsnachweis. Mehr als zweifach verlängerte Ausnahmen erfordern Genehmigung der Geschäftsleitung. Zweite Verlängerung: maximal 6 Monate; dritte Verlängerung: maximal 3 Monate.

---

## Incident Response

[Organisation] reagiert auf Sicherheitsvorfälle bei der Datenlöschung gemäss dem Incident-Management-Rahmenwerk.

**Vorfälle bei der Datenlöschung**:

| Vorfalltyp | Schweregrad | Reaktionspriorität |
|------------|-------------|-------------------|
| **Unmaskierte sensible Daten in Nicht-Produktion** | Hoch | Sofort – Einschränken, Löschung implementieren, verifizieren |
| **Löschprozessfehler mit Datensicherheitsrisiko** | Kritisch | Sofort – Ursache untersuchen, beheben |
| **Aufbewahrung über genehmigte Frist hinaus** | Mittel-Hoch | Dringend – Umfang beurteilen, Löschung ausführen |
| **Erfolgreiche Wiederherstellung gelöschter Daten** | Hoch | Sofort – Löschmethodenschwäche beurteilen, Controls stärken |
| **Umgehungsversuch bei Löschung** | Hoch | Sofort – Absicht untersuchen, Disziplinarmassnahmen |
| **Legal-Hold-Verletzung (Löschung trotz Hold)** | Kritisch | Sofort – Legal/Compliance benachrichtigen, verbleibende Beweise sichern |
| **Versäumte Frist bei Löschanfrage betroffener Person** | Hoch | Sofort – Löschung abschliessen, betroffene Person benachrichtigen, GDPR-Meldepflicht prüfen |
| **Backup-Bereinigungsfehler** | Mittel | Dringend – Backup-Rotationsplan prüfen, maximale Aufbewahrung dokumentieren |
| **Datenexfiltration aus Umgebung mit unzureichender Löschung** | Kritisch | Sofort – Incident Response, Meldepflicht prüfen |

**Incident-Response-Prozess**:

**(a) Erkennung & Meldung**: Sofortige Meldung an Security-Team; Protokollierung im Incident-Register
**(b) Klassifizierung**: Schweregrad basierend auf Datensensitivität und Exponierungsumfang
**(c) Eindämmung**: Sofortmassnahmen innerhalb 1 Stunde (Kritisch/Hoch); Beweissicherung; Benachrichtigung von ISB, DSB, Legal/Compliance
**(d) Untersuchung**: Ursachenanalyse, Umfangsbestimmung, Auswirkungsbeurteilung, Zeitstrahl-Rekonstruktion
**(e) Behebung**: Löschimplementierung korrigieren; Löschung ausführen; Wirksamkeit validieren; Wiederholung verhindern
**(f) Meldung**: Interne Eskalation; GDPR/nDSG-Meldepflicht prüfen (72 Stunden an Aufsichtsbehörde bei Hochrisiko); Drittanbieter benachrichtigen

**Regulatorische Meldepflicht-Beurteilung**:

**(a) GDPR**: Meldung an Aufsichtsbehörde innerhalb **72 Stunden** (Art. 33); Benachrichtigung betroffener Personen **unverzüglich** bei Hochrisiko (Art. 34)
**(b) Schweizerisches nDSG**: Meldung an FDPIC bei **hohem Risiko** für Persönlichkeit oder Grundrechte (Art. 24)
**(c) Branchenspezifisch**: PCI DSS, HIPAA je nach Anwendbarkeit

---

## Richtlinien-Governance

**Überprüfungsplan**:

- **Frequenz**: Jährlich mindestens (typisch Q4, abgestimmt auf internes Prüfprogramm)
- **Umfassende Überprüfung**: ISB (Vorsitz), DSB, Rechts-/Compliance-Beauftragter, ITL

**Ausgelöste Überprüfung** (innerhalb von 30 Tagen):

- Regulatorische Änderungen (GDPR-Leitfäden, nDSG-Änderungen, branchenspezifische Änderungen)
- Wesentliche organisatorische Änderungen (Fusionen, neue Geschäftsbereiche, Infrastrukturmigration)
- Wesentliche Vorfälle (Löschvorfälle, externe Datenpannen, Prüfungsfeststellungen)
- Technologieänderungen (neue Löschfähigkeiten, veränderte Backup-Architektur)

**Richtlinienaktualisierungen**:

**(a) Geringfügige Updates** (Klarstellungen, Referenzaktualisierungen): ISB-Genehmigung ausreichend; E-Mail-Benachrichtigung innerhalb 30 Tage

**(b) Wesentliche Updates** (Geltungsbereichsänderungen, neue verbindliche Anforderungen): Vollständige Genehmigungskette; organisationsweite Ankündigung; Umsetzungsfrist 60–90 Tage

**(c) Notfall-Updates** (kritische Schwachstelle, dringendes regulatorisches Mandat): ISB-Genehmigung; Benachrichtigung der Geschäftsleitung innerhalb 24 Stunden; Ratifizierung durch vollständige Genehmigungskette innerhalb 30 Tage

**Schulung und Bewusstsein**:

**(a) Sicherheitsbewusstseinsschulung** (Alle Mitarbeiter – jährlich): Informationslöschung, Nutzerverantwortlichkeiten, Meldeverfahren

**(b) Technische Schulung** (IT-Betrieb, Systemeigentümer – Initial + jährlich): Löschmethoden, Backup-Koordination, Verifizierungsverfahren

**(c) Dateneigentümer-Schulung** (Initial + bei regulatorischen Änderungen): Datenklassifizierung, Ausnahmebeurteilung, regulatorische Anforderungen

**(d) Datenschutzschulung** (DSB-Büro – Initial + bei regulatorischen Änderungen): Bearbeitung von Anfragen betroffener Personen, GDPR Art. 17-Ausnahmenbeurteilung

**(e) Management-Schulung** (Geschäftsleitung, ISB, ITL – Initial + jährlich): Governance-Verantwortlichkeiten, Risikoakzeptanz

---

# Implementierung und Referenzen

## Integration in das ISMS

**Risikobewertungsintegration** (ISO 27001 Klausel 6.1):

Löschkontrollen werden basierend auf der Risikobewertungsmethodik von [Organisation] ausgewählt. Restrisiken (wo Löschung nicht machbar) sind im Risikoregister dokumentiert und von ISB + Geschäftsleitung formal akzeptiert.

**Anwendbarkeitserklärung** (ISO 27001 Klausel 6.1.3):

- Control A.8.10-Anwendbarkeit in der Anwendbarkeitserklärung (SoA) von [Organisation] begründet
- **SoA-Eintrag**: Control A.8.10 als «Implementiert» dokumentiert mit Verweisen auf ISMS-IMP-A.8.10.1 bis .4

**Integration verwandter Controls**:

| Control | Beziehung zur Informationslöschung |
|---------|------------------------------------|
| **A.5.9 (Inventar von Informationen und Assets)** | Grundlage – Asset-Inventar identifiziert Systeme mit Löschkontrollanforderungen |
| **A.5.12 (Klassifizierung von Informationen)** | Grundlage – Datenklassifizierung steuert Löschmethodenauswahl |
| **A.5.34 (Datenschutz und Schutz von PII)** | Integration – GDPR/nDSG-Löschrechte; Löschung unterstützt Datensparsamkeit |
| **A.8.13 (Informations-Backup)** | Kritische Integration – Backup-Aufbewahrung muss Löschanforderungen entsprechen |
| **A.8.24 (Einsatz von Kryptografie)** | Integration – Kryptografische Löschung; Schlüsselmanagement-Integration |
| **A.7.14 (Sichere Entsorgung oder Wiederverwendung von Ausrüstung)** | Integration – Geräteentsorgung beinhaltet Datensanitierung |

---

## Regulatorische Zuordnung

| Anforderungskategorie | Schweizerisches nDSG | EU GDPR | ISO 27001:2022 | PCI DSS v4.0.1* | HIPAA* | FINMA* |
|-----------------------|---------------------|---------|----------------|---------|--------|--------|
| **Datensparsamkeit / Speicherbegrenzung** | Art. 6 | Art. 5(1)(e) | A.8.10 | Req. 3.1 | §164.514 | Risikobasiert |
| **Aufbewahrungspläne** | Art. 6 | Art. 5(1)(e) | A.8.10 | Req. 3.1 | Allgemeine Regeln | FINMA RS 2008/21 |
| **Löschmethoden / Sanitierung** | Art. 8, 25, 30 | Art. 32(1) | A.8.10 | Req. 3.2 | §164.310(d)(2)(i) | Risikobasiert |
| **Recht auf Löschung** | Art. 12 | Art. 17 | A.5.34 (Ref.) | Nicht anwendbar | Eingeschränkt | Nicht anwendbar |
| **Löschverpflichtungen Dritter** | Art. 8 | Art. 28(3)(g) | A.8.10 | Req. 12.8.2 | §164.314(a)(2) | FINMA RS 2018/3 |
| **Nachweis der Löschung** | Art. 8 | Art. 5(2) Accountability | A.8.10 | Req. 12.3.4 | §164.316(b)(1)(ii) | Risikobasiert |

*Bedingte Anwendbarkeit gemäss ISMS-POL-00

---

## Dokumentenbeziehungen

```
Richtlinienebene (Governance – ISMS-gesteuert)
    │
    └── ISMS-POL-A.8.10 (Dieses Dokument)
        ├── Anhang A: Löschmethoden-Matrix
        ├── Anhang B: Vorlage für Löschanfragen betroffener Personen
        └── Anhang C: Ausnahmeantragsvorlage

Implementierungsebene (Bewertung & Nachweis – ISMS-gesteuert)
    │
    └── ISMS-IMP-A.8.10-Suite
        ├── ISMS-IMP-A.8.10.1: Aufbewahrung & Löschauslöser
        ├── ISMS-IMP-A.8.10.2: Löschmethoden
        ├── ISMS-IMP-A.8.10.3: Drittanbieter & Cloud-Löschung
        ├── ISMS-IMP-A.8.10.4: Verifizierung & Nachweis

Unterstützende Referenzen (ISMS-gesteuert)
    │
    └── ISMS-REF-A.5.23: Cloud-Dienstleister-Register
```

---

# Definitionen

**Anonymisierung**: Unwiderruflicher Prozess der Entfernung aller identifizierenden Informationen aus Daten, so dass eine Re-Identifizierung auch mit zusätzlichen Daten oder Aufwand nicht vertretbar erreichbar ist.

**Backup-Bereinigung**: Prozess der Löschung von Daten aus Backup-Systemen (vollständige/inkrementelle Backups, Snapshots, Notfallwiederherstellungsreplikate), um sicherzustellen, dass gelöschte Daten nicht in Backup-Kopien verbleiben.

**Clear (Löschmethode)**: Logische Sanitierungstechnik, die logische Techniken zum Sanitieren von Daten in allen benutzeradressierbaren Speicherorten anwendet und vor einfachen nicht-invasiven Datenwiederherstellungstechniken schützt.

**Datenkategorie**: Klassifizierung von Daten nach Typ für Aufbewahrungs- und Löschzwecke (z.B. PII, Finanzdaten, Gesundheitsinformationen, Anmeldedaten, Geschäftsunterlagen, Protokolle).

**Dateneigentümer**: Geschäfts- oder Funktionsleiter, der für Daten in seinem Bereich verantwortlich ist; zuständig für Datenklassifizierung, Aufbewahrungsfristen, Ausnahmegenehmigungen und Validierung der Löscheffektivität.

**Destroy (Löschmethode)**: Physische Zerstörung des Speichermediums, die das Medium unbrauchbar und die Datenwiederherstellung nicht machbar macht. Gemäss NIST SP 800-88: Desintegration, Pulverisierung, Einschmelzen, Verbrennen, Schreddern.

**Informationslöschung**: Prozess der Entfernung von Daten von Speichermedien, so dass sie mit normalen Methoden oder spezialisierten Datenwiederherstellungstechniken nicht wiederhergestellt werden können.

**Kompensierende Massnahme**: Alternative Sicherheitskontrolle, die implementiert wird, wenn die primäre Kontrolle (Löschung) technisch oder operativ nicht machbar ist und eine gleichwertige Risikoreduktion durch andere Mittel bietet.

**Kryptografische Löschung**: Datenlöschmethode, die verschlüsselte Daten unwiederbringlich macht, indem Verschlüsselungsschlüssel vernichtet werden, ohne die verschlüsselten Daten physisch zu verändern.

**Legal Hold (Aufbewahrungssperre)**: Aussetzung normaler Löschprozesse zur Aufbewahrung von Daten für Rechtsstreitigkeiten, Ermittlungen, Aufsichtsprüfungen oder Prüfungen. Übersteuert Aufbewahrungspläne und Löschauslöser bis zur formalen Aufhebung durch den Rechts-/Compliance-Beauftragten.

**Mediensanitierung**: Alle Methoden zur Unzugänglichmachung von Daten auf Speichermedien, einschliesslich Clear, Purge und Destroy.

**Purge (Löschmethode)**: Physische oder logische Sanitierungstechnik zum Schutz vor Labor-Angriffsmethoden. Gemäss NIST SP 800-88: kryptografische Löschung, Entmagnetisierung (Magnetmedien), physische Vernichtung.

**Recht auf Löschung**: Recht der betroffenen Person gemäss GDPR Artikel 17 und Schweizerischem nDSG Artikel 12 auf Antrag auf Löschung ihrer personenbezogenen Daten.

**Restrisiko**: Risiko, das nach Anwendung von Sicherheitskontrollen verbleibt. Muss von ISB und Geschäftsleitung formal akzeptiert werden.

**Speicherbegrenzung**: GDPR Artikel 5(1)(e)-Grundsatz, der verlangt, personenbezogene Daten nicht länger in einer Form aufzubewahren, die die Identifizierung der betroffenen Personen erlaubt, als für die Verarbeitungszwecke notwendig.

**Vernichtungsnachweis**: Drittanbieter-Bestätigung über die physische Vernichtung von Speichermedien, einschliesslich Medienidentifikatoren, Vernichtungsmethode und -datum sowie Zertifikatsaussteller.

---

# Anhang A: Zugelassene Löschmethoden-Matrix

**Zweck**: Dieser Anhang bietet technische Referenz für die Auswahl geeigneter Löschmethoden basierend auf Medientyp, Datensensitivität und Medienziel. Alle aufgelisteten Methoden sind für die organisatorische Verwendung gemäss Abschnitt 2.2 genehmigt.

## A.1 Löschmethoden-Auswahlmatrix

| Medientyp | Datensensitivität | Medienziel | Empfohlene Methode | Verifizierung |
|-----------|-------------------|------------|-------------------|----------------|
| **Magnetische HDD** | Eingeschränkt/Vertraulich | Externe Entsorgung | Entmagnetisieren + Physische Vernichtung | Vernichtungsnachweis |
| **Magnetische HDD** | Eingeschränkt/Vertraulich | Interne Wiederverwendung | ATA Secure Erase ODER Überschreiben (7+ Durchläufe) | Tool-Protokoll + Stichproben |
| **Magnetische HDD** | Intern/Öffentlich | Interne Wiederverwendung | Überschreiben (3 Durchläufe) ODER Schnellformat + Überschreiben | Tool-Protokoll |
| **Solid-State (SSD)** | Eingeschränkt/Vertraulich | Externe Entsorgung | Physische Vernichtung (Schreddern, Pulverisieren) | Vernichtungsnachweis |
| **Solid-State (SSD)** | Eingeschränkt/Vertraulich | Interne Wiederverwendung | Kryptografische Löschung (wenn verschlüsselt) ODER Secure Erase | Schlüsselvernichtungsprotokoll ODER Tool-Protokoll |
| **Solid-State (SSD)** | Intern/Öffentlich | Interne Wiederverwendung | Secure Erase ODER Werksreset | Tool-Protokoll |
| **Optische Medien (CD/DVD)** | Beliebige Sensitivität | Entsorgung | Physische Vernichtung (Schreddern P-4 oder höher) | Vernichtungsnachweis ODER bezeugte Vernichtung |
| **Magnetband** | Eingeschränkt/Vertraulich | Externe Entsorgung | Entmagnetisieren + Physische Vernichtung | Vernichtungsnachweis |
| **Magnetband** | Eingeschränkt/Vertraulich | Interne Wiederverwendung | Entmagnetisieren | Entmagnetisierer-Protokoll + Feldstärkeverifizierung |
| **Magnetband** | Intern/Öffentlich | Interne Wiederverwendung | Überschreiben (vollständiges Band) | Backup-Systemprotokoll |
| **Papierdokumente** | Eingeschränkt/Vertraulich | Entsorgung | Kreuzschnitt-Schreddern (DIN 66399 P-4 Minimum) | Vernichtungsnachweis ODER Schredderprotokoll |
| **Papierdokumente** | Intern/Öffentlich | Entsorgung | Kreuzschnitt-Schreddern (DIN 66399 P-3) | Schredderprotokoll ODER bezeugte Vernichtung |
| **Mobilgeräte (verschlüsselt)** | Eingeschränkt/Vertraulich | Externe Entsorgung | Kryptografische Löschung + Werksreset + Physische Vernichtung | Schlüsselvernichtung + Zertifikat |
| **Mobilgeräte (verschlüsselt)** | Eingeschränkt/Vertraulich | Interne Wiederverwendung | Kryptografische Löschung + Werksreset | Schlüsselvernichtungsprotokoll + Geräteverifizierung |
| **Mobilgeräte (unverschlüsselt)** | Eingeschränkt/Vertraulich | Beliebiges Ziel | Physische Vernichtung (NICHT allein Werksreset) | Vernichtungsnachweis |
| **Cloud-Speicher (IaaS/PaaS)** | Eingeschränkt/Vertraulich | Nicht anwendbar | API-Löschung + Kryptografische Löschung (wenn kundenverwaltete Schlüssel) | API-Erfolgsantwort + Schlüsselvernichtungsprotokoll |
| **Cloud-Speicher (IaaS/PaaS)** | Intern/Öffentlich | Nicht anwendbar | API-Löschung + Verifizierungsabfrage | API-Erfolgsantwort + Abwesenheitsverifizierung |
| **Cloud-Speicher (SaaS)** | Beliebige Sensitivität | Nicht anwendbar | Anbieter-Löschprozess gemäss Vertrag | Löschnachweis ODER SOC 2-Prüfbericht |
| **Datenbankeinträge** | Eingeschränkt/Vertraulich | Nicht anwendbar | SQL DELETE + Backup-Bereinigung | Datenbankprotokoll + Backup-Verifizierungsabfrage |

## A.2 NIST SP 800-88-Methoden-Zuordnung

| [Organisation]-Methode | NIST SP 800-88-Kategorie | Anwendbarkeit |
|-----------------------|--------------------------|---------------|
| **Überschreiben (mehrere Durchläufe)** | Clear | Magnetmedien (HDD, Band) – NICHT SSD |
| **ATA Secure Erase** | Purge (wenn korrekt implementiert) | HDD, einige SSDs (Abschluss verifizieren) |
| **Kryptografische Löschung** | Purge | Alle verschlüsselten Medien (Schlüssel müssen unwiederbringlich sein) |
| **Entmagnetisieren** | Purge | Nur Magnetmedien (HDD, Band) – NICHT SSD/optisch |
| **Physische Vernichtung (Desintegration)** | Destroy | Alle Medientypen |
| **Physische Vernichtung (Schreddern)** | Destroy | Papier (DIN 66399), optische Medien, einige elektronische |
| **Physische Vernichtung (Verbrennen)** | Destroy | Alle Medientypen |

## A.3 Methodenspezifische Anforderungen

### A.3.1 Überschreiben (Magnetmedien)

**Anwendbar für**: Magnetfestplatten (HDD), Magnetband
**NICHT anwendbar für**: SSDs, Flash-Laufwerke, optische Medien

**Anforderungen**:
- Mindestens **3 Durchläufe** für Intern/Öffentlich-Daten
- Mindestens **7 Durchläufe** für Vertraulich/Eingeschränkt-Daten
- Jeder Durchlauf muss ein anderes Muster schreiben (Nullen, Einsen, Zufallsdaten)
- Vollständige Medienüberschreibung (alle adressierbaren Sektoren einschliesslich Slack-Space)

**Verifizierung**: Tool-Protokoll über abgeschlossene Durchläufe ohne Fehler.

### A.3.2 ATA Secure Erase / NVMe Secure Erase

**Anforderungen**:
- Herstellerbereitgestelltes Tool oder `hdparm` (Linux) / `nvme format` (NVMe) verwenden
- Erfolgreichen Abschluss bestätigen (kein Fehler im SMART-Protokoll)
- **Warnung**: SSD Secure-Erase-Zuverlässigkeit variiert je nach Hersteller; für Eingeschränkt-Daten ist physische Vernichtung gegenüber alleinigem Secure Erase vorzuziehen

### A.3.3 Kryptografische Löschung

**Anforderungen**:
- Verschlüsselung muss aktiviert gewesen sein BEVOR Daten geschrieben wurden
- ALLE Kopien der Verschlüsselungsschlüssel vernichten (Schlüsselmanagementsystem, Escrow, Benutzerkopien)
- Verifizieren, dass Schlüsselvernichtung unwiderruflich ist
- Schlüssel-zu-Daten-Zuordnung dokumentieren
- **Integration**: Kryptografische Löschverfahren müssen mit ISMS-POL-A.8.24 (Kryptografie-Richtlinie) übereinstimmen

### A.3.4 Entmagnetisieren

**Anwendbar für**: Nur Magnetmedien (HDD, Magnetband)
**NICHT anwendbar für**: SSD, Flash-Laufwerke, optische Medien (keine Wirkung)

**Anforderungen**:
- Entmagnetisierer mit ausreichender Feldstärke für Mediukoerzivität verwenden
- Für moderne Hochdichte-HDD (>1 TB): Mindestens **5.000 Oersted**
- Entmagnetisierung + physische Vernichtung kombinieren

### A.3.5 Physische Vernichtung

**Anforderungen nach Medientyp**:

| Medientyp | Vernichtungsanforderung | Normreferenz |
|-----------|------------------------|--------------|
| **HDD (magnetisch)** | Platten schreddern, pulverisieren oder desintegrieren zu ≤2 mm Partikeln | NIST SP 800-88 (Destroy) |
| **SSD (solid-state)** | Chips physisch vernichten (schreddern, pulverisieren) | NIST SP 800-88 (Destroy) |
| **Optisch (CD/DVD/Blu-ray)** | Kreuzschnitt-Schreddern zu ≤10 mm²-Partikeln (DIN 66399 O-4 Minimum für Vertraulich) | DIN 66399 |
| **Magnetband** | Band schreddern zu ≤6 mm-Streifen (DIN 66399 T-4 Minimum für Vertraulich) | DIN 66399 |
| **Papierdokumente** | Kreuzschnitt-Schreddern zu ≤160 mm²-Partikeln (DIN 66399 P-4 Minimum für Vertraulich) | DIN 66399 |
| **Mobilgeräte** | Gerät zerdrücken oder schreddern, Motherboard und Speicherchips vernichten | NIST SP 800-88 |

**Vernichtung durch Drittanbieter**:
- Zertifizierte Vernichtungsdienstleister verwenden (NAID AAA oder Äquivalent)
- Vernichtungsnachweis mit Medienseriennummern, Vernichtungsmethode, -datum, -ort und Aussteller einholen
- Verwahrkette von [Organisation] bis zum Vernichtungsdienstleister aufrechterhalten

## A.4 Backup-Löschkoordination

| Backup-Typ | Löschmethode | Verifizierung |
|------------|-------------|---------------|
| **Vollständig + Inkrementell** | Alle Backup-Sets löschen, die Zieldaten enthalten | Backup-Katalogabfrage zur Abwesenheitsbestätigung |
| **Vollständig + Differentiell** | Vollständiges Backup + alle differentiellen Backups löschen | Backup-Katalogabfrage |
| **Snapshot-basiert** | Alle Snapshots mit Zieldaten löschen ODER Aufbewahrungsrichtlinie mit garantiertem Löschdatum durchsetzen | Snapshot-Inventar; Richtlinien-Durchsetzungsprotokoll |
| **Cloud-native (AWS Backup, Azure Backup)** | API-Löschung von Wiederherstellungspunkten; Multi-Regions-Löschung verifizieren | API-Antwortprotokolle |
| **Anwendungsebene (DB-Dumps, VM-Exporte)** | Gelöschte Daten aus zukünftigen Dumps ausschliessen; bestehende Dumps löschen | Dump-Manifest-Verifizierung |
| **Band-Backups** | Bänder zur frühzeitigen Ausmusterung markieren ODER entmagnetisieren/vernichten | Band-Inventar mit Ausmusterungsdaten |

---

# Anhang B: Vorlage für Löschanfragen betroffener Personen

**Zweck**: Standardisiertes Formular zur Bearbeitung von Löschanfragen gemäss GDPR Artikel 17 und Schweizerischem nDSG Artikel 12.

**Verwendung**: DSB-Büro verwendet diese Vorlage zur Dokumentation aller Löschanfragen betroffener Personen.

---

## Formular für Löschanfragen betroffener Personen

**Anfrage-ID**: [AUTO-GENERIERT: DSR-A810-JJJJ-NNN]
**Antragsdatum**: [TT.MM.JJJJ HH:MM]
**Eingangskanal**: [ ] E-Mail [ ] Webformular [ ] Post [ ] Persönlich [ ] Telefon
**Bearbeitet von**: [Name des DSB-Büromitarbeiters]

---

### Angaben zur betroffenen Person

**Name**: [Vollständiger rechtlicher Name]
**E-Mail**: [E-Mail-Adresse für Korrespondenz]
**Telefon**: [Optionale Kontaktnummer]
**Adresse**: [Optionale Postadresse]
**Beziehung zu [Organisation]**: [ ] Aktueller Kunde [ ] Ehemaliger Kunde [ ] Mitarbeiter [ ] Ehemaliger Mitarbeiter [ ] Website-Besucher [ ] Sonstige: _______

**Konto-/Referenznummer** (falls anwendbar): [Kunden-ID, Mitarbeiter-ID, Kontonummer]

---

### Identitätsverifizierung

**Verwendete Verifizierungsmethode**:
- [ ] Konto-Login (authentifizierte Sitzung)
- [ ] Amtlicher Lichtbildausweis (Pass, nationale ID-Karte, Führerausweis)
- [ ] Persönliche Informationsbestätigung (Sicherheitsfragen, Kontodetails)
- [ ] Persönliche Identifizierung im Büro von [Organisation]
- [ ] Sonstige: [Methode angeben]

**Verifizierungsdatum**: [TT.MM.JJJJ]
**Verifizierungsstatus**: [ ] ✅ Verifiziert [ ] ⚠️ Teilweise verifiziert [ ] ❌ Verifizierung fehlgeschlagen
**Prüfer**: [Name des DSB-Büromitarbeiters]

---

### Antragsdetails

**Umfang des Antrags**:
- [ ] Alle personenbezogenen Daten bei [Organisation]
- [ ] Bestimmte Datenkategorien: [Liste]
- [ ] Bestimmte Systeme/Dienste: [Liste]
- [ ] Bestimmter Zeitraum: [Von TT.MM.JJJJ bis TT.MM.JJJJ]

**Grund des Antrags** (soweit von betroffener Person angegeben):
- [ ] Daten für ursprünglichen Zweck nicht mehr notwendig
- [ ] Einwilligung widerrufen
- [ ] Widerspruch zur Verarbeitung
- [ ] Daten unrechtmässig verarbeitet
- [ ] Kein Grund angegeben (nicht erforderlich gemäss GDPR/nDSG)

---

### Rechtliche Beurteilung

**DSB-Beurteilungsdatum**: [TT.MM.JJJJ]
**Geprüft von**: [DSB-Name und Unterschrift]

**Besteht eine Löschpflicht gemäss GDPR Art. 17(1)?**

[ ] ✅ JA – Löschung erforderlich
[ ] ❌ NEIN – Löschung abgelehnt (rechtliche Ausnahme gilt)

**Falls LÖSCHUNG ERFORDERLICH** – anwendbare Grundlagen nach GDPR Art. 17(1):
- [ ] Art. 17(1)(a): Daten für Erhebungszweck nicht mehr notwendig
- [ ] Art. 17(1)(b): Einwilligungswiderruf (kein anderer Rechtsgrund vorhanden)
- [ ] Art. 17(1)(c): Widerspruch (Art. 21) ohne vorrangige legitime Gründe
- [ ] Art. 17(1)(d): Unrechtmässige Verarbeitung
- [ ] Art. 17(1)(e): Löschung zur Erfüllung einer rechtlichen Verpflichtung
- [ ] Art. 17(1)(f): Daten für Informationsgesellschaftsdienste für Kinder erhoben

**Falls LÖSCHUNG ABGELEHNT** – anwendbare Ausnahme nach GDPR Art. 17(3):
- [ ] Art. 17(3)(a): Ausübung des Rechts auf freie Meinungsäusserung
- [ ] Art. 17(3)(b): Erfüllung rechtlicher Verpflichtung (EU/Mitgliedstaatsrecht)
  - **Rechtliche Verpflichtung**: [Spezifisches Gesetz zitieren, z.B. «Schweizerisches OR Art. 958f – 10-jährige Buchführungspflicht»]
- [ ] Art. 17(3)(c): Öffentliches Interesse oder hoheitliche Aufgabe
- [ ] Art. 17(3)(e): Archivzwecke im öffentlichen Interesse, Forschung, statistische Zwecke
- [ ] Art. 17(3)(f): Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen
  - **Rechtsanspruch**: [Beschreiben, z.B. «Anhängiges Verfahren Az. XYZ-2024-1234»]

**Legal-Hold-Konflikt**:
- [ ] JA – Daten unterliegen aktivem Legal Hold
  - **Hold-ID**: [Verweis auf Legal-Hold-Register]
  - **Massnahme**: Verarbeitungsbeschränkung gemäss GDPR Art. 18 angewendet
- [ ] NEIN – Kein Legal Hold aktiv

---

### Ausführungsplan der Löschung

| System / Datenbank | Datenkategorien | Löschmethode | Verantwortliche Partei | Zieldatum |
|-------------------|-----------------|--------------|----------------------|-----------|
| | | | | |
| | | | | |

**Backup-Löschung**:
- [ ] Ja, Backups werden gemäss Aufbewahrungsplan gelöscht
- [ ] Teilweise – Backup-Löschung geplant für: __________________
- [ ] Nicht erforderlich (begründen): __________________

**Benachrichtigung Dritter gemäss GDPR Art. 19**:
- [ ] Ja, Dritte innerhalb von 7 Tagen nach Löschausführung benachrichtigt
- [ ] Nein, Daten nicht an Dritte weitergegeben

---

### Antwort an betroffene Person

**Antwortdatum**: [TT.MM.JJJJ] (muss innerhalb von 30 Tagen nach Eingang liegen, GDPR Art. 12(3))
**Antwortmethode**: [ ] E-Mail [ ] Post [ ] Persönlich [ ] Sicheres Portal

**Bei Abschluss der Löschung**:
- [ ] Bestätigung der Löschung
- [ ] Liste der betroffenen Systeme/Datenkategorien
- [ ] Datum der Löschausführung
- [ ] Benachrichtigte Drittanbieter (falls anwendbar)

**Bei Ablehnung der Löschung**:
- [ ] Spezifische Ausnahmerechtsgrundlage (GDPR Art. 17(3)-Verweis)
- [ ] Erklärung in klarer Sprache
- [ ] Angebotene Alternativen (Verarbeitungsbeschränkung, Datenübertragbarkeit)
- [ ] Recht auf Beschwerde bei Aufsichtsbehörde:
  - Schweiz: Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter (EDÖB)
  - EU: Zuständige nationale Datenschutzbehörde des Wohnsitzes der betroffenen Person

---

### Abschluss und Ablage

**Anfragestatus**:
- [ ] Abgeschlossen – Löschung ausgeführt, Antwort versendet
- [ ] Abgeschlossen – Löschung abgelehnt, Antwort mit Begründung versendet
- [ ] Verlängert – 2-Monats-Verlängerung beantragt (GDPR Art. 12(3)), betroffene Person benachrichtigt
- [ ] Ausstehend – Wartet auf: __________________

**Qualitätsprüfung**:
Geprüft von: __________________  Prüfdatum: __________________
Prüfergebnis: [ ] Genehmigt [ ] Korrekturen erforderlich

**Aufbewahrungsfrist**: **3 Jahre Minimum** (oder gemäss anwendbarer regulatorischer Anforderung)

---

# Anhang C: Ausnahmeantragsvorlage

**Zweck**: Standardisierter Antrag auf Ausnahme von Standard-Löschverfahren oder Aufbewahrungsfristen.

---

## Ausnahmeantrag zur Informationslöschungsrichtlinie

**Ausnahme-ID**: [AUTO-GENERIERT: EXC-A810-JJJJ-NNN]
**Antragsdatum**: [TT.MM.JJJJ]
**Beantragt von**: [Name, Rolle, Abteilung]
**Dringlichkeit**: [ ] Standard (10 Werktage) [ ] Dringend (3 Werktage – ISB-Genehmigung erforderlich)

---

### Informationen zu den betroffenen Daten

**Datenkategorie**: __________________
**Klassifizierung**: [ ] Öffentlich [ ] Intern [ ] Vertraulich [ ] Eingeschränkt
**Aktuelle Aufbewahrungsfrist**: __________________
**Standard-Löschdatum**: __________________
**Enthält personenbezogene Daten**: [ ] Ja [ ] Nein

---

### Beantragte Ausnahme

**Ausnahmetyp**:
- [ ] Verlängerte Aufbewahrung (über Standard-Aufbewahrungsfrist hinaus aufbewahren)
- [ ] Alternative Löschmethode (andere Methode als in Richtlinie verwenden)
- [ ] Aufgeschobene Löschung (geplantes Löschdatum verschieben)
- [ ] Temporäre Löschaussetzung (aus operativen Gründen)
- [ ] Sonstige: __________________

**Maximale Ausnahmedauer** (gemäss Richtlinie Abschnitt 3.3):
- Intern/Öffentlich: 12 Monate Maximum
- Vertraulich: 6 Monate Maximum
- Eingeschränkt: 6 Monate Maximum (erfordert ISB + DSB + Dateneigentümer-Genehmigung)

**Ausnahme-Startdatum**: [TT.MM.JJJJ]
**Ausnahme-Enddatum**: [TT.MM.JJJJ]

---

### Geschäftliche Begründung

**Detaillierte Begründung** (spezifisch sein):

__________________

**Auswirkung bei Ablehnung der Ausnahme**:

__________________

**Compliance-Pfad** (wie wird vollständige Lösch-Compliance erreicht? – PFLICHTFELD):

| Meilenstein | Aktivität | Zieldatum | Verantwortlich | Status |
|------------|-----------|-----------|----------------|--------|
| [z.B. Tool-Evaluation] | [z.B. Backup-Löschtools evaluieren] | [TT.MM.JJJJ] | [IT-Betrieb] | [Nicht begonnen] |
| [z.B. Implementierung] | [z.B. Neue Backup-Lösung einführen] | [TT.MM.JJJJ] | [IT-Betrieb] | [Nicht begonnen] |

---

### Risikobewertung

**Inhärentes Risiko** (ohne Löschkontrolle):

**Wahrscheinlichkeit der Datenexponierung**:
- [ ] Niedrig (1) – Unwahrscheinlich (starke kompensierende Massnahmen)
- [ ] Mittel (2) – Möglich (moderate kompensierende Massnahmen)
- [ ] Hoch (3) – Wahrscheinlich (schwache kompensierende Massnahmen)
- [ ] Kritisch (4) – Sehr wahrscheinlich (minimale kompensierende Massnahmen)

**Auswirkung bei Exponierung**:
- [ ] Niedrig (1) – Minimaler Schaden (Intern/Öffentlich, begrenzter Umfang)
- [ ] Mittel (2) – Moderater Schaden
- [ ] Hoch (3) – Erheblicher Schaden (Vertraulich, grosse Datenmenge)
- [ ] Kritisch (4) – Schwerwiegender Schaden (Eingeschränkt, breiter Umfang; regulatorische Meldepflicht wahrscheinlich)

**Inhärenter Risiko-Score**: [Wahrscheinlichkeit × Auswirkung = X]

---

### Kompensierende Massnahmen

**Implementierte alternative Schutzkontrollen** (PFLICHTFELD für Genehmigung):

- [ ] **Erweiterte Zugangskontrollen**: Rollen mit Zugang auf [Liste] reduziert; MFA durchgesetzt; PAM implementiert
- [ ] **Verschlüsselung**: Daten im Ruhezustand verschlüsselt; Schlüssel separat verwaltet; kryptografische Löschung geplant
- [ ] **Erweiterte Überwachung**: Zugangsprotokolle aktiviert; Benachrichtigungen bei unbefugtem Zugang; SIEM-Integration
- [ ] **Datensparsamkeit**: Datensatz auf notwendige Felder/Zeitraum reduziert; sensible Felder maskiert
- [ ] **Netzwerksegmentierung**: Systeme mit nicht gelöschten Daten isoliert; Firewall-Regeln eingeschränkt
- [ ] **Sonstige**: [Zusätzliche kompensierende Massnahme beschreiben]

**Wirksamkeit der kompensierenden Massnahmen**:
- **Geschätzte Risikoreduktion**: [Prozentsatz oder qualitativ, z.B. «40% Reduktion»]
- **Restrisiko-Score**: [Angepasste Wahrscheinlichkeit × Auswirkung = Y]

---

### Genehmigungen

**Dateneigentümer**:
- Name: [Name und Titel des Dateneigentümers]
- **Bestätigt**: Risiko für Daten unter meiner Verantwortung; Verantwortung für kompensierende Massnahmen
- Unterschrift: ________________  Datum: [TT.MM.JJJJ]

---

**Security-Team-Überprüfung**:
- Prüfer: [Name des Security-Team-Leiters]
- **Risikobewertung**: [ ] ✅ Akzeptabel mit kompensierenden Massnahmen [ ] ⚠️ Akzeptabel mit Bedingungen [ ] ❌ Nicht akzeptabel
- Unterschrift: ________________  Datum: [TT.MM.JJJJ]

---

**ISB-Genehmigung** (erforderlich für Vertraulich/Eingeschränkt-Daten):
- Name: [ISB Name]
- [ ] ✅ **Genehmigt** [ ] ⚠️ **Genehmigt mit Bedingungen** [ ] ❌ **Abgelehnt**
- Unterschrift: ________________  Datum: [TT.MM.JJJJ]
- **Risikoakzeptanz**: Ich akzeptiere den Restrisiko-Score von [Y] für eine Ausnahmedauer von [X Monaten]

---

**DSB-Genehmigung** (erforderlich für Eingeschränkt-Daten oder personenbezogene Daten):
- Name: [DSB Name]
- [ ] ✅ **Genehmigt** (Datenschutz-Compliance mit kompensierenden Massnahmen akzeptabel)
- [ ] ⚠️ **Genehmigt mit Bedingungen**
- [ ] ❌ **Abgelehnt** (inakzeptables Datenschutzrisiko oder regulatorischer Verstoss)
- Unterschrift: ________________  Datum: [TT.MM.JJJJ]

---

**Genehmigung Geschäftsleitung** (erforderlich für Produktionsausnahmen):
- Name: [Name und Titel der Geschäftsleitung]
- [ ] ✅ **Genehmigt** [ ] ❌ **Abgelehnt**
- Unterschrift: ________________  Datum: [TT.MM.JJJJ]

---

### Überwachung und Compliance

**Überprüfungsplan**:
- [ ] Monatlich (für Kritisch/Eingeschränkt-Datensensitivität)
- [ ] Vierteljährlich (für Hoch/Vertraulich-Datensensitivität)
- [ ] Halbjährlich (für Mittel/Intern-Datensensitivität)

**Widerrufsauslöser** (Bedingungen, unter denen die Ausnahme sofort widerrufen wird):
- [ ] Versagen kompensierender Massnahmen (z.B. Verschlüsselung deaktiviert, Zugangskontrollen umgangen)
- [ ] Sicherheitsvorfall mit nicht gelöschten Daten
- [ ] Geschäftliche Begründung nicht mehr gültig
- [ ] Lösung verfügbar vor Zeitplan
- [ ] Anfrage betroffener Person kann nicht erfüllt werden (GDPR-Verstossrisiko)
- [ ] Ausnahmedauer abgelaufen (automatischer Widerruf, keine implizite Verlängerung)

---

### Ausnahmeverlängerung (falls beantragt)

**Aktualisierte Risikobewertung**:
- Vorheriges Restrisiko: [Y]
- Aktuelles Restrisiko: [Z] (neu bewertet)
- Risikotendenz: [ ] Abnehmend [ ] Stabil [ ] Zunehmend

**Verlängerungsbeschränkungen**:
- **Zweite Verlängerung**: Maximum 6 Monate (auch wenn erste Ausnahme 12 Monate war)
- **Dritte Verlängerung**: Maximum 3 Monate + Genehmigung der Geschäftsleitung erforderlich
- **Verlängerungsbegrenzung**: Mehr als zweifach verlängerte Ausnahmen ohne nachweisbaren Compliance-Fortschritt werden ABGELEHNT

---

### Ausnahmeabschluss

**Abschlussdatum**: [TT.MM.JJJJ]
**Abschlussgrund**:
- [ ] Compliance erreicht (Löschanforderung jetzt erfüllt)
- [ ] Ausnahme abgelaufen (Dauer erreicht)
- [ ] Ausnahme widerrufen (Widerrufsauslöser eingetreten)
- [ ] Geschäftliche Begründung entfallen

**Abschlussverifizierung**:
- [ ] Löschkontrolle jetzt implementiert
- [ ] Kompensierende Massnahmen ausser Betrieb genommen
- [ ] Risikoregister aktualisiert
- [ ] Ausnahmeregister aktualisiert (Status auf Geschlossen geändert)
- [ ] Lernpunkte dokumentiert

**Abschluss genehmigt von**: [ISB-Name und Unterschrift]
**Abschlussdatum**: [TT.MM.JJJJ]

---

**Ausnahmendokumentation**: Alle genehmigten Ausnahmen werden im Ausnahmeregister (verfolgt in ISMS-IMP-A.8.10.3) geführt und für **Dauer der Ausnahme + 3 Jahre** aufbewahrt.

---

# Nachweise für diese Richtlinie

**Stufe 1 (Dokumentationsüberprüfung) – Nachweise**:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.8.10 v1.0)
- ✅ Genehmigungsunterschriften von ISB, DSB, Legal/Compliance, Geschäftsleitung
- ✅ Dokumentierte Aufbewahrungsfristen
- ✅ Löschmethoden nach Datensensitivität spezifiziert
- ✅ Anforderungen für Drittanbieter- und Cloud-Löschung definiert
- ✅ Verifizierungsanforderungen dokumentiert
- ✅ Prozess für Löschanfragen betroffener Personen definiert

**Stufe 2 (Operative Wirksamkeit) – Nachweise**:

- Löschausführungsprotokolle
- Aufbewahrungsplan (aktuelle + abgelöste Versionen)
- Vernichtungsnachweise von Drittanbietern
- GDPR-Anfragenprotokoll
- Legal-Hold-Register
- Ausnahmegenehmigungen
- Vierteljährliche Compliance-Berichte
- Dateninventar mit Löschungsumfang

---

# Genehmigungsdokumentation

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date] |
| **IT-Leiter (ITL)** | [Name] | [Date] |
| **Datenschutzbeauftragter (DSB)** | [Name] | [Date] |
| **Rechts-/Compliance-Beauftragter** | [Name] | [Date] |
| **Geschäftsleitung** | [Name] | [Date] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

*Diese Richtlinie legt Anforderungen fest. Implementierungsverfahren sind in der ISMS-IMP-A.8.10-Suite dokumentiert (Aufbewahrungs- & Löschauslöser, Löschmethoden, Drittanbieter- & Cloud-Löschung, Verifizierung & Nachweis).*

---

<!-- QA_VERIFIED: 2026-03-28 -->
