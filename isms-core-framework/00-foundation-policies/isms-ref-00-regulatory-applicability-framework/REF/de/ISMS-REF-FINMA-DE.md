<!-- ISMS-CORE:REF:ISMS-REF-FINMA-DE:framework:REF:finma -->
**ISMS-REF-FINMA-DE — FINMA Rundschreiben 2023/1 Anforderungsreferenz**
**Informationssicherheitsanforderungen für Schweizer Finanzinstitute (Nicht-ISMS-Technische Referenz)**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | FINMA Rundschreiben 2023/1 Anforderungsreferenz |
| **Dokumententyp** | Intern — Technische Referenz (nicht ISMS) |
| **Dokumenten-ID** | ISMS-REF-FINMA-DE |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumentenverantwortlicher** | Geschäftsführer (GF) |
| **Genehmigt von** | ISB (Technische Referenz — keine Genehmigung der Geschäftsleitung erforderlich) |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB / Rechts-/Compliance-Abteilung | Erste technische Referenz für Schweizer Finanzinstitute |

**Überprüfungszyklus:** Jährlich (oder bei FINMA-Rundschreiben-Aktualisierungen)
**Nächstes Überprüfungsdatum:** [Datum + 12 Monate]
**Genehmigende:** Rechts-/Compliance-Abteilung / ISB (technische Referenz, keine ISMS-Genehmigung erforderlich)

**Verbreitung:** Compliance-Team, ISB, Rechtsberatung (für FINMA-beaufsichtigte Organisationen)

---

⚠️ **WICHTIG – NICHT-ISMS TECHNISCHES UNTERSTÜTZUNGSDOKUMENT**

Dieses Dokument dient ausschließlich Informations- und Sensibilisierungszwecken.

- Dieses Dokument ist KEIN Teil des Informationssicherheitsmanagementsystems (ISMS).
- Dieses Dokument definiert KEINE zwingenden Anforderungen, außer wenn [Organisation] ein FINMA-reguliertes Unternehmen ist.
- Dieses Dokument begründet KEINE verbindlichen Anforderungen, Fristen, KPIs oder SLAs für nicht regulierte Unternehmen.
- Dieses Dokument schreibt die Übernahme von FINMA-Anforderungen für nicht FINMA-beaufsichtigte Organisationen NICHT vor.
- Dieses Dokument überschreibt oder erweitert keine ISMS-Richtlinie.

**Anwendbarkeitsbestimmung:**
FINMA-Anforderungen gelten NUR, wenn [Organisation]:

- Eine FINMA-Lizenz besitzt (Bank, Effektenhändler, Versicherung, Fondsverwaltung, Zahlungsdienstleistungen)
- Der FINMA-Aufsicht unterliegt
- Als Schweizer Finanzinstitut tätig ist

Für alle anderen Organisationen dient dieses Dokument ausschließlich als:

- Technische Referenz für potenzielle FINMA-Anforderungen
- Kontext für Dienstleisterbeziehungen mit Schweizer Finanzinstituten
- Sensibilisierung für Sicherheitsstandards im Schweizer Finanzsektor
- **Dieses Dokument darf nicht als Audit-Nachweis verwendet werden, außer wenn [Organisation] FINMA-reguliert ist**

Die Verwendung dieses Dokuments impliziert keine FINMA-Anwendbarkeit, Compliance-Pflichten oder Regulierungsstatus.

**Wesentlicher Positionierungshinweis:**
Dieses Dokument enthält absichtlich regulatorische Details, die über das für die meisten Organisationen Zutreffende hinausgehen. Sein Zweck ist ausschließlich die Sensibilisierung von Organisationen, die möglicherweise der FINMA-Aufsicht unterliegen könnten, oder die Dienstleistungen für FINMA-regulierte Unternehmen erbringen. Aus dem Vorhandensein, dem Fehlen oder dem Umsetzungsstatus eines hier aufgeführten FINMA-Requiremenst dürfen keine Audit-Schlussfolgerungen gezogen werden, außer wenn [Organisation] explizit FINMA-reguliert ist.

---

# Dokumentenzweck und Geltungsbereich

## Zweck

Dieses Dokument gibt einen technischen Überblick über die Informationssicherheitsanforderungen der Eidgenössischen Finanzmarktaufsicht (FINMA) gemäß FINMA Rundschreiben 2023/1 „Operationelle Risiken und Resilienz — Banken" (in Kraft ab 1. Juni 2024). Es soll unterstützen bei:

- Sensibilisierung für FINMA-Anforderungen für Schweizer Finanzinstitute
- Verständnis der FINMA-Randnummerstruktur und zentraler Anforderungen
- Kontext für Organisationen, die Dienstleistungen für Schweizer Finanzinstitute erbringen
- Zukünftige Anwendbarkeitsbeurteilung
- Zuordnung von FINMA-Anforderungen zu ISO 27001:2022 Kontrollen

## Was dieses Dokument NICHT ist

Dieses Dokument:

- Begründet KEINE zwingenden Anforderungen für nicht FINMA-regulierte Organisationen
- Definiert NICHT die Compliance-Pflichten von [Organisation] (siehe POL-00 für regulatorische Anwendbarkeit)
- Schafft KEINE Audit-Kriterien, außer wenn [Organisation] FINMA-reguliert ist
- Ersetzt KEINE Interpretation durch Rechts- oder Compliance-Beratung
- Stellt KEINE Rechtsberatung zur FINMA-Compliance dar
- Begründet KEINE Umsetzungsverfahren oder Verifikationsprozesse

## Beziehung zum ISMS

Dieses Dokument ist eine **unverbindliche technische Referenz**, AUSSER wenn [Organisation] der FINMA-Aufsicht unterliegt (wie in ISMS-POL-00 Abschnitt 3.1 festgestellt).

**Wenn [Organisation] FINMA-reguliert IST:**

- FINMA-Anforderungen werden gemäß POL-00 zu Stufe 1 (Zwingend)
- Dieses Dokument liefert Umsetzungshinweise
- ISMS-Kontrollen müssen FINMA-Compliance nachweisen
- Jährliche FINMA-Compliance-Bescheinigung erforderlich

**Wenn [Organisation] NICHT FINMA-reguliert ist:**

- FINMA bleibt gemäß POL-00 bei Stufe 3 (Informativ)
- Dieses Dokument dient ausschließlich der Sensibilisierung
- Keine FINMA-Compliance-Pflichten
- ISMS-Kontrollen folgen ausschließlich ISO 27001:2022

## Inhaltsorganisation

Diese Referenz organisiert FINMA-Anforderungen nach:

- FINMA Rundschreiben 2023/1 Randnummerstruktur
- Informationssicherheitsanforderungen (Randnummern 50–62)
- Protokollierungs- und Überwachungsanforderungen (Randnummern 63–72)
- Betriebskontinuitätsanforderungen (Randnummern 73–87)
- Auslagerungsanforderungen (FINMA 2008/7 und 2018/3)
- Zuordnung zu ISO 27001:2022 Annex-A-Kontrollen

---

# FINMA — Überblick und Anwendbarkeit

## Was ist FINMA?

**Eidgenössische Finanzmarktaufsicht (FINMA)** ist die Schweizer Finanzmarktaufsichtsbehörde, die für die Aufsicht über Banken, Versicherungsgesellschaften, Börsen, Effektenhändler und andere Finanzintermediäre in der Schweiz zuständig ist.

**Primäre gesetzliche Grundlage:**

- Finanzmarktaufsichtsgesetz (FINMAG)
- Bankengesetz (BankG)
- Versicherungsaufsichtsgesetz (VAG)
- Finanzinstitutsgesetz (FINIG)

**Durchsetzungsbefugnisse:**

- Lizenzierung und Bewilligung
- Vor-Ort-Prüfungen
- Fernaufsicht
- Durchsetzungsmaßnahmen (Bußen, Lizenzentzug)
- Meldepflichten bei Vorfällen

## FINMA-Rundschreiben

**Rundschreiben-Struktur:**
FINMA erlässt „Rundschreiben", die verbindliche Mindeststandards für beaufsichtigte Institute festlegen. Wichtige Rundschreiben für die Informationssicherheit:

**FINMA Rundschreiben 2023/1** — Operationelle Risiken und Resilienz (Banken):

- In Kraft: 1. Juni 2024
- Gilt für: Banken und Effektenhändler
- Geltungsbereich: Operationelles Risikomanagement, Betriebskontinuität, Informationssicherheit, Auslagerung
- **Randnummern 50–62:** Informationssicherheitsanforderungen
- **Randnummern 63–72:** Protokollierungs- und Überwachungsanforderungen
- **Randnummern 73–87:** Anforderungen an Betriebskontinuität und Resilienz

**FINMA Rundschreiben 2008/7** — Auslagerung (Banken):

- Risikomanagement in Auslagerungsbeziehungen
- Sorgfaltspflichten und vertragliche Anforderungen
- Datenschutz und Vertraulichkeit
- Betriebskontinuität bei Auslagerung

**FINMA Rundschreiben 2018/3** — Auslagerung (Versicherungen):

- Vergleichbare Anforderungen, angepasst für den Versicherungssektor
- Meldepflichten gegenüber der Aufsichtsbehörde

## Anwendbarkeitsbestimmung

**FINMA gilt für [Organisation], WENN:**

| Kriterium | Status | Nachweis |
|-----------|--------|----------|
| Besitzt FINMA-Bankenlizenz | ⬜ Ja ⬜ Nein | [Lizenznummer / N/A] |
| Besitzt FINMA-Effektenhändlerlizenz | ⬜ Ja ⬜ Nein | [Lizenznummer / N/A] |
| Besitzt FINMA-Versicherungslizenz | ⬜ Ja ⬜ Nein | [Lizenznummer / N/A] |
| Besitzt FINMA-Fondsverwaltungslizenz | ⬜ Ja ⬜ Nein | [Lizenznummer / N/A] |
| Besitzt FINMA-Zahlungsdienstleistungslizenz | ⬜ Ja ⬜ Nein | [Lizenznummer / N/A] |
| Unterliegt der FINMA-Aufsicht | ⬜ Ja ⬜ Nein | [Aufsichtsfeststellung] |

**Bei EINEM „Ja":** FINMA-Anforderungen sind gemäß POL-00 Abschnitt 3.1 **Stufe 1 (Zwingend)**

**Bei ALLEN „Nein":** FINMA-Anforderungen bleiben gemäß POL-00 **Stufe 3 (Informativ)**

**Status als Dienstleister:**
Wenn [Organisation] Dienstleistungen FÜR FINMA-regulierte Unternehmen erbringt:

- FINMA 2008/7 oder 2018/3 Auslagerungsanforderungen können gelten
- Kundenverträge können FINMA-gleichwertige Kontrollen vorschreiben
- Prüfungsrecht-Klauseln können FINMA-Compliance-Nachweis erfordern
- Als vertragliche Anforderungen betrachten (Stufe 1 bei vertraglicher Verpflichtung)

---

# FINMA Rundschreiben 2023/1 — Informationssicherheitsanforderungen

## Überblick (Randnummern 50–62)

FINMA Rundschreiben 2023/1 Randnummern 50–62 legen Informationssicherheitsanforderungen für Schweizer Banken und Effektenhändler fest.

**Kernprinzip:**
Organisationen müssen **risikobasierte** Informationssicherheitsmaßnahmen implementieren, die angemessen sind in Bezug auf:

- Art und Umfang der Geschäftstätigkeit
- Komplexität der IT-Systeme
- Sensibilität der verarbeiteten Daten
- Bedrohungslage und Risikobewertung

FINMA schreibt keine spezifischen technischen Kontrollen vor, sondern verlangt „angemessene organisatorische und technische Massnahmen".

## Randnummern 50–55: Informationssicherheitsrahmen

**Randnummer 50: Informationssicherheitsstrategie**

**Anforderung:**
Banken müssen eine Informationssicherheitsstrategie definieren und umsetzen, die ausgerichtet ist auf:

- Geschäftsstrategie und Risikobereitschaft
- IT-Strategie und Architektur
- Regulatorische Anforderungen
- Branchenbestpraktiken

**ISO 27001:2022 Zuordnung:**

- Klausel 5.2: Richtlinie
- Klausel 6.2: Informationssicherheitsziele
- A.5.1: Richtlinien für Informationssicherheit

**Umsetzungsüberlegungen:**

- Genehmigung der Informationssicherheitsstrategie auf Vorstandsebene
- Jährliche Überprüfung und Aktualisierung
- Integration ins unternehmerische Risikomanagement
- Klare Rollen und Verantwortlichkeiten (ISB, IT-Management, Geschäftsbereiche)

---

**Randnummer 51: Informationssicherheitsorganisation**

**Anforderung:**
Klare Organisationsstruktur für Informationssicherheit mit:

- Definierten Rollen und Verantwortlichkeiten
- Funktionstrennung (Entwicklung, Betrieb, Sicherheit)
- Unabhängige Sicherheitsfunktion mit ausreichender Autorität
- Eskalationswege zur Geschäftsleitung und zum Vorstand

**ISO 27001:2022 Zuordnung:**

- Klausel 5.3: Organisatorische Rollen, Verantwortlichkeiten und Befugnisse
- A.5.2: Rollen und Verantwortlichkeiten für Informationssicherheit

**Wichtige Rollen** (FINMA-Erwartung):

- Informationssicherheitsbeauftragter (ISB) oder Äquivalent
- Informationssicherheitsausschuss
- Systemverantwortliche
- Sicherheitsarchitekten
- Security-Operations-Team

---

**Randnummer 52: Risikobewertung**

**Anforderung:**
Regelmäßige Informationssicherheits-Risikobewertungen, die abdecken:

- Identifikation von Informationswerten
- Bedrohungs- und Schwachstellenbewertung
- Risikobewertung und Priorisierung
- Risikobehandlungsentscheidungen
- Akzeptanz von Restrisiken

**ISO 27001:2022 Zuordnung:**

- Klausel 6.1.2: Informationssicherheits-Risikobewertung
- Klausel 6.1.3: Informationssicherheits-Risikobehandlung
- Klausel 8.2: Informationssicherheits-Risikobewertung
- Klausel 8.3: Informationssicherheits-Risikobehandlung

**FINMA-Erwartungen:**

- Mindestens jährliche Risikobewertung
- Ausgelöste Bewertungen bei wesentlichen Änderungen
- Vorstandsberichterstattung zu Schlüsselrisiken
- Dokumentation von Risikoentscheidungen

---

**Randnummer 53: Sicherheitsrichtlinien und -standards**

**Anforderung:**
Umfassende Informationssicherheitsrichtlinien und -standards, die abdecken:

- Informationsklassifizierung
- Zugriffskontrolle
- Kryptographie
- Physische Sicherheit
- Incident-Management
- Betriebskontinuität

**ISO 27001:2022 Zuordnung:**

- A.5.1: Richtlinien für Informationssicherheit
- A.5.10: Akzeptable Nutzung von Informationen und anderen Werten
- A.5.12: Klassifizierung von Informationen

**Dokumentationsanforderungen:**

- Richtlinienhierarchie (Strategie → Richtlinie → Standards → Verfahren)
- Regelmäßige Überprüfung und Aktualisierung
- Kommunikation und Sensibilisierung
- Genehmigung durch das Management

---

**Randnummer 54: Sicherheitsbewusstsein und Schulung**

**Anforderung:**
Programm zur Informationssicherheitsbewusstsein und -schulung, das sicherstellt:

- Alle Mitarbeitenden kennen ihre Sicherheitspflichten
- Rollenspezifische Schulungen für Sicherheitsverantwortlichkeiten
- Regelmäßige Sensibilisierungskampagnen
- Prüfung und Validierung der Wirksamkeit des Bewusstseins

**ISO 27001:2022 Zuordnung:**

- A.6.3: Sensibilisierung, Aus- und Weiterbildung zur Informationssicherheit

**FINMA-Erwartungen:**

- Jährliche Pflichtschulung für alle Mitarbeitenden
- Spezialisierte Schulungen für privilegierte Nutzer
- Phishing-Simulationen und Tests
- Verfolgung des Schulungsabschlusses und Metriken

---

**Randnummer 55: Drittparteien-Risikomanagement**

**Anforderung:**
Risikobasierter Ansatz für die Sicherheit von Drittparteien, einschließlich:

- Sicherheitsbewertungen von Lieferanten
- Vertragliche Sicherheitsanforderungen
- Laufende Überwachung der Lieferantenleistung
- Prüfungsrecht und Informationszugang

**ISO 27001:2022 Zuordnung:**

- A.5.19: Informationssicherheit in Lieferantenbeziehungen
- A.5.20: Berücksichtigung von Informationssicherheit in Lieferantenvereinbarungen
- A.5.21: Management der Informationssicherheit in der IKT-Lieferkette

**FINMA-spezifisch:**

- FINMA Rundschreiben 2008/7 gilt für Auslagerungsbeziehungen
- Wesentliche Auslagerungen erfordern FINMA-Meldung
- Exit-Strategien und Übergangsplanung sind zwingend

---

## Randnummer 56: Authentifizierung und Zugangskontrolle

**Anforderung:**
Implementierung starker Authentifizierungs- und Zugangskontrollmechanismen:

- Benutzeridentifikation und -authentifizierung
- Eindeutige Benutzerkonten (keine gemeinsam genutzten Konten)
- Multi-Faktor-Authentifizierung für kritische Systeme
- Zugang mit minimalen Rechten (Least Privilege)
- Regelmäßige Zugangsprüfungen

**Spezifische Anforderungen:**

**Authentifizierung:**

- Starke Authentifizierung für alle Benutzer
- Multi-Faktor-Authentifizierung (MFA) für:
  - Fernzugang
  - Privilegierte Konten
  - Zugang zu sensiblen Daten
- Passwort-Komplexität und Rotationsrichtlinien
- Kontosperrung nach Fehlversuchen

**Zugangskontrolle:**

- Rollenbasierte Zugangskontrolle (RBAC)
- Prinzip des minimalen Privilegs
- Regelmäßige Zugangsbestätigung (mindestens jährlich)
- Automatisierte Bereitstellung und Aufhebung
- Privileged Access Management (PAM) für Administratoren

**ISO 27001:2022 Zuordnung:**

- A.5.15: Zugangskontrolle
- A.5.16: Identitätsmanagement
- A.5.17: Authentifizierungsinformationen
- A.5.18: Zugriffsrechte
- A.8.2: Privilegierte Zugriffsrechte
- A.8.3: Einschränkung des Informationszugriffs
- A.8.5: Sichere Authentifizierung

**Umsetzungshinweise:**

- Identity and Access Management (IAM) Plattform
- Single Sign-On (SSO) mit MFA
- Privileged Access Management (PAM) Lösung
- Automatisierte Zugangsprüfungen und -bestätigungen
- Prozessautomatisierung für Eintritte/Wechsel/Austritte (JML)

---

## Randnummer 58: Funktionstrennung

**Anforderung:**
Funktionstrennung definieren und umsetzen, um Interessenkonflikte zu verhindern und das Betrugsrisiko zu reduzieren:

- Kritische Geschäftsprozesse identifizieren, die Funktionstrennung erfordern
- Inkompatible Rollen und Aktivitäten definieren
- Kontrollen implementieren, um Funktionstrennungsverletzungen zu verhindern
- Funktionstrennungskonflikte überwachen und erkennen
- Kompensatorische Kontrollen, wo Funktionstrennung nicht möglich

**Kritische Trennungsbeispiele:**

- Entwicklung vs. Produktionszugang
- Änderungsinitiator vs. Änderungsgenehmiger
- Zahlungsinitiator vs. Zahlungsgenehmiger
- Sicherheitsadministrator vs. Systemadministrator
- Backup-Administrator vs. Wiederherstellungsanforderer

**ISO 27001:2022 Zuordnung:**

- A.5.15: Zugangskontrolle (Prinzip der Funktionstrennung)
- A.5.18: Zugriffsrechte (rollenbasierte Trennung)
- A.8.2: Privilegierte Zugriffsrechte (administrative Trennung)

**Umsetzungsansätze:**

- Rollenbasierte Zugangskontrolle (RBAC) mit Funktionstrennung-Regeln
- Automatisierte Erkennung von Funktionstrennungskonflikten (z. B. SAP GRC, Oracle GRC)
- Regelmäßige Berichterstattung über Funktionstrennungsverletzungen und Behebung
- Dokumentation kompensatorischer Kontrollen (z. B. verstärkte Überwachung, Dual-Authorisation)

**FINMA-Erwartungen:**

- Funktionstrennung-Matrix mit dokumentierten inkompatiblen Aktivitäten
- Automatisierte Funktionstrennung-Überwachung, wo möglich
- Vierteljährliche Berichterstattung über Funktionstrennungsverletzungen an das Management
- Bewusstsein auf Vorstandsebene für kritische Funktionstrennungslücken

---

## Randnummer 62: Verschlüsselung

**Anforderung:**
Kryptographie implementieren, um sensible Daten zu schützen:

- Datenverschlüsselung im Ruhezustand und bei der Übertragung
- Verschlüsselungsschlüsselverwaltung
- Ausrichtung an aktuellen Verschlüsselungsstandards
- Regelmäßige kryptographische Überprüfung

**Spezifische Anforderungen:**

**Daten bei der Übertragung:**

- TLS 1.2 Minimum (TLS 1.3 bevorzugt)
- Starke Cipher-Suites (keine veralteten Algorithmen)
- Zertifikatsverwaltung und -rotation
- Sichere Protokolle für alle sensiblen Datenübertragungen

**Daten im Ruhezustand:**

- Vollständige Datenträgerverschlüsselung für Endpunkte (Laptops, mobile Geräte)
- Datenbankverschlüsselung für sensible Daten
- Datei-/Ordnerverschlüsselung für vertrauliche Dokumente
- Backup-Verschlüsselung

**Schlüsselverwaltung:**

- Zentrales Schlüsselverwaltungssystem
- Trennung von Schlüsselverwaltung und Datenzugang
- Schlüsselrotation und Lebenszyklus-Management
- Sichere Schlüsselablage (Hardware Security Module bevorzugt)
- Schlüssel-Backup und Wiederherstellungsverfahren

**Verschlüsselungsstandards:**

- AES-256 für symmetrische Verschlüsselung
- RSA 2048-Bit Minimum oder ECC 256-Bit für asymmetrische Verschlüsselung
- SHA-256 Minimum für Hashing
- Keine Verwendung veralteter Algorithmen (DES, 3DES, MD5, SHA-1)

**ISO 27001:2022 Zuordnung:**

- A.8.24: Verwendung von Kryptographie

**Umsetzungshinweise:**

- Microsoft BitLocker / FileVault für Endpunktverschlüsselung
- Azure Key Vault / AWS KMS für Cloud-Schlüsselverwaltung
- Hardware Security Module (HSM) für hochwertige Schlüssel
- Zertifikat-Lebenszyklusverwaltung (Let's Encrypt, DigiCert, usw.)
- Regelmäßige kryptographische Inventarisierung und Compliance-Scanning

---

## Randnummern 63–72: Protokollierung und Überwachung

**Randnummern 63–65: Protokollierung sicherheitsrelevanter Ereignisse**

**Anforderung:**
Umfassende Protokollierung sicherheitsrelevanter Ereignisse:

- Benutzerauthentifizierung und -autorisierung
- Privilegierte Operationen
- Systemänderungen und -konfigurationen
- Sicherheitsvorfälle und -alarme
- Datenzugriff (insbesondere sensible Daten)

**Anforderungen an Protokollinhalte:**

- Wer: Benutzeridentifikation
- Was: Durchgeführte Aktion
- Wann: Zeitstempel (synchronisiert)
- Wo: System/Anwendung/IP-Adresse
- Ergebnis: Erfolg oder Misserfolg

**Protokollaufbewahrung:**

- Sicherheitsprotokolle: mindestens 12 Monate (FINMA-Erwartung)
- Audit-Protokolle: 10 Jahre (je nach Datentyp)
- Backup-Protokolle für Langzeitaufbewahrung

**ISO 27001:2022 Zuordnung:**

- A.8.15: Protokollierung
- A.8.16: Überwachungsaktivitäten

---

**Randnummern 66–68: Zentrales Log-Management**

**Anforderung:**
Zentralisierte Sammlung, Speicherung und Analyse von Sicherheitsprotokollen:

- SIEM (Security Information and Event Management) oder Äquivalent
- Echtzeit-Protokollerfassung aus allen kritischen Systemen
- Schutz der Protokollintegrität (unveränderliche Protokolle)
- Sichere Protokollspeicherung mit Zugriffskontrollen

**SIEM-Funktionen:**

- Protokollaggregation aus mehreren Quellen
- Korrelation und Analyse
- Alarme und Benachrichtigungen
- Berichte und Dashboards
- Integration mit Incident Response

**ISO 27001:2022 Zuordnung:**

- A.8.15: Protokollierung (zentrales Log-Management)
- A.8.16: Überwachungsaktivitäten (SIEM-Korrelation)

**Umsetzungsbeispiele:**

- Splunk Enterprise Security
- Microsoft Sentinel (Azure)
- Elastic Security (ELK Stack)
- IBM QRadar
- LogRhythm

---

**Randnummern 69–72: Echtzeit-Überwachung und Alarmierung**

**Anforderung:**
Kontinuierliche Überwachung und Echtzeit-Alarmierung bei Sicherheitsereignissen:

- 24/7-Sicherheitsüberwachung (SOC oder Äquivalent)
- Automatisierte Alarmierung bei kritischen Sicherheitsereignissen
- Definierte Eskalationsverfahren
- Integration mit Incident Response

**Alarmkategorien:**

- Kritisch: Sofortmaßnahme erforderlich (innerhalb von 15 Minuten)
- Hoch: Reaktion innerhalb von 1 Stunde
- Mittel: Reaktion innerhalb von 4 Stunden
- Niedrig: Reaktion innerhalb von 24 Stunden

**Überwachte Ereignisse:**

- Fehlgeschlagene Authentifizierungsversuche (Brute Force)
- Nutzung privilegierter Konten
- Unbefugte Zugriffsversuche
- Malware-Erkennung
- Indikatoren für Datenexfiltration
- Systemkonfigurationsänderungen
- Ausfälle von Sicherheitskontrollen

**ISO 27001:2022 Zuordnung:**

- A.8.16: Überwachungsaktivitäten
- A.5.24: Planung und Vorbereitung des Informationssicherheits-Incident-Managements
- A.5.25: Beurteilung und Entscheidung bei Informationssicherheitsereignissen

**Umsetzungsansätze:**

- Internes SOC (Security Operations Center)
- Managed Security Service Provider (MSSP)
- Co-managed SOC (hybrides Modell)

---

## Randnummern 73–87: Betriebskontinuität und Resilienz

**Überblick:**
FINMA Rundschreiben 2023/1 Randnummern 73–87 legen umfassende Anforderungen an Betriebskontinuität und Disaster Recovery für Schweizer Finanzinstitute fest.

**Randnummern 73–75: Business Impact Analysis (BIA)**

**Anforderung:**
Regelmäßige Business Impact Analysis durchführen, um:

- Kritische Geschäftsprozesse zu identifizieren
- Recovery Time Objectives (RTO) zu definieren
- Recovery Point Objectives (RPO) zu definieren
- Finanzielle und operative Auswirkungen zu bewerten

**ISO 27001:2022 Zuordnung:**

- Klausel 8.1: Operative Planung und Steuerung (Betriebskontinuität)
- A.5.29: Informationssicherheit bei Störungen
- A.5.30: IKT-Bereitschaft für Betriebskontinuität

**FINMA-Erwartungen:**

- RTO für kritische Prozesse: typischerweise 2–4 Stunden
- RPO für kritische Daten: typischerweise 15 Minuten bis 1 Stunde
- Jährliche BIA-Überprüfung und -Aktualisierung
- Vorstandsgenehmigung für RTO/RPO-Ziele

---

**Randnummern 76–80: Business Continuity Plans (BCP)**

**Anforderung:**
Dokumentierte und getestete Betriebskontinuitätspläne, einschließlich:

- Incident-Response-Verfahren
- Krisenmanagement-Struktur
- Kommunikationspläne (intern und extern)
- Ausweichverarbeitungsstandorte
- Datensicherungs- und Wiederherstellungsverfahren

**Plankomponenten:**

- Rollen und Verantwortlichkeiten (Krisenmanagement-Team)
- Aktivierungskriterien und Eskalation
- Kommunikationsprotokolle (FINMA-Meldeanforderungen)
- Wiederherstellungsverfahren (Schritt für Schritt)
- Lieferanten- und Anbieterkoordination
- Rückkehr zum Normalbetrieb

**ISO 27001:2022 Zuordnung:**

- A.5.29: Informationssicherheit bei Störungen
- A.5.30: IKT-Bereitschaft für Betriebskontinuität
- A.8.13: Datensicherung
- A.8.14: Redundanz von Informationsverarbeitungseinrichtungen

---

**Randnummern 81–84: Tests und Validierung**

**Anforderung:**
Regelmäßige Tests der Betriebskontinuitäts- und Disaster-Recovery-Fähigkeiten:

- Jährlicher vollständiger DR-Test (Minimum)
- Teiltests quartalsweise oder halbjährlich
- Tabletop-Übungen
- Komponententests (Backup-Wiederherstellung, Failover)

**Testtypen:**

- **Tabletop-Übung:** Diskussionsbasiert, keine Systemaktivierung
- **Teiltest:** Test spezifischer Komponenten (z. B. Datenbank-Failover)
- **Vollständiger DR-Test:** Vollständiger Failover zu Ausweichstandort
- **Überraschungstest:** Unangekündigte Aktivierung zur Überprüfung der Bereitschaft

**ISO 27001:2022 Zuordnung:**

- A.5.30: IKT-Bereitschaft für Betriebskontinuität (Testanforderung)

**FINMA-Erwartungen:**

- Jährlicher vollständiger DR-Test dokumentiert und berichtet
- Testergebnisse vom Vorstand überprüft
- Identifizierte Lücken innerhalb definierter Fristen behoben
- Einbeziehung von Drittparteien getestet (Auslagerungspartner)

---

**Randnummern 85–87: Incident-Management und Meldung**

**Anforderung:**
Formeller Incident-Management-Prozess, einschließlich:

- Incident-Klassifizierung und Schweregrade
- Eskalationsverfahren
- FINMA-Meldeanforderungen
- Ursachenanalyse
- Lessons Learned und kontinuierliche Verbesserung

**FINMA-Incident-Meldung:**
Banken müssen FINMA melden bei:

- **Sofort:** Schwerwiegende Vorfälle, die kritische Geschäftsprozesse beeinträchtigen
- **Innerhalb von 24 Stunden:** Sicherheitsverletzungen, Datenlecks, erhebliche Ausfälle
- **Nach dem Vorfall:** Detaillierter Vorfallbericht innerhalb definierter Fristen

**Meldeinhalt:**

- Vorfallbeschreibung und Zeitablauf
- Folgenabschätzung (Kunden, Betrieb, finanziell)
- Ursachenanalyse
- Ergriffene Abhilfemaßnahmen
- Maßnahmen zur Vermeidung von Wiederholungen

**ISO 27001:2022 Zuordnung:**

- A.5.24: Planung und Vorbereitung des Informationssicherheits-Incident-Managements
- A.5.25: Beurteilung und Entscheidung bei Informationssicherheitsereignissen
- A.5.26: Reaktion auf Informationssicherheitsvorfälle
- A.5.27: Lernen aus Informationssicherheitsvorfällen
- A.5.28: Beweissicherung

---

# FINMA Rundschreiben 2008/7 — Auslagerung (Banken)

## Überblick

FINMA Rundschreiben 2008/7 legt Anforderungen für Banken fest, die Geschäftsfunktionen oder IT-Dienstleistungen an Drittanbieter auslagern.

**Anwendbarkeit:**

- Gilt für Banken und Effektenhändler
- Deckt Auslagerung wesentlicher Funktionen ab
- Umfasst sowohl inländische als auch grenzüberschreitende Auslagerung
- Cloud-Dienste gelten als Auslagerung

## Wesentliche Anforderungen

**Risikobewertung:**

- Umfassende Risikobewertung vor der Auslagerung
- Bewertung der Fähigkeiten des Dienstleisters
- Bewertung des Konzentrationsrisikos
- Überlegungen zu Datenresidenz und Datensouveränität

**Vertragliche Anforderungen:**

- Klare Definition von Dienstleistungen und SLAs
- Sicherheits- und Vertraulichkeitspflichten
- Prüfungsrecht und Informationszugang
- Einschränkungen bei Unterauslagerung
- Datenschutzklauseln
- Anforderungen an Betriebskontinuität
- Exit-Strategie und Übergangsbestimmungen

**Laufende Überwachung:**

- Regelmäßige Überprüfungen der Dienstleisterleistung
- Periodische Sicherheitsbewertungen und Audits
- Meldepflichten bei Vorfällen
- Jährliche Compliance-Bescheinigung (z. B. SOC 2 Typ II)

**ISO 27001:2022 Zuordnung:**

- A.5.19: Informationssicherheit in Lieferantenbeziehungen
- A.5.20: Berücksichtigung von Informationssicherheit in Lieferantenvereinbarungen
- A.5.21: Management der Informationssicherheit in der IKT-Lieferkette
- A.5.22: Überwachung, Überprüfung und Änderungsmanagement von Lieferantendienstleistungen
- A.5.23: Informationssicherheit bei der Nutzung von Cloud-Diensten

---

# ISO 27001:2022 — FINMA Zuordnung

## Kontroll-Zuordnungsmatrix

| FINMA Anforderung | FINMA Randnummer | ISO 27001:2022 Kontrolle | Umsetzungspriorität |
|-------------------|-----------------|--------------------------|---------------------|
| Informationssicherheitsstrategie | 50 | Klausel 5.2, A.5.1 | Kritisch |
| Sicherheitsorganisation | 51 | Klausel 5.3, A.5.2 | Kritisch |
| Risikobewertung | 52 | Klausel 6.1.2, 6.1.3, 8.2, 8.3 | Kritisch |
| Sicherheitsrichtlinien | 53 | A.5.1, A.5.10, A.5.12 | Kritisch |
| Sensibilisierung und Schulung | 54 | A.6.3 | Hoch |
| Drittparteien-Risiko | 55 | A.5.19, A.5.20, A.5.21 | Kritisch |
| Authentifizierung & Zugangskontrolle | 56 | A.5.15, A.5.16, A.5.17, A.5.18, A.8.2, A.8.3, A.8.5 | Kritisch |
| Funktionstrennung | 58 | A.5.15, A.5.18, A.8.2 | Kritisch |
| Verschlüsselung | 62 | A.8.24 | Kritisch |
| Sicherheitsprotokollierung | 63–65 | A.8.15 | Kritisch |
| Zentrales Log-Management | 66–68 | A.8.15, A.8.16 | Kritisch |
| Überwachung und Alarmierung | 69–72 | A.8.16, A.5.24, A.5.25 | Kritisch |
| Business Impact Analysis | 73–75 | A.5.29, A.5.30 | Kritisch |
| Betriebskontinuitätspläne | 76–80 | A.5.29, A.5.30, A.8.13, A.8.14 | Kritisch |
| BC/DR-Tests | 81–84 | A.5.30 | Kritisch |
| Incident-Management | 85–87 | A.5.24, A.5.25, A.5.26, A.5.27, A.5.28 | Kritisch |
| Auslagerung (FINMA 2008/7) | N/A | A.5.19, A.5.20, A.5.21, A.5.22, A.5.23 | Kritisch |

## Lückenanalyse-Ansatz

Für FINMA-regulierte Organisationen:

**Schritt 1:** FINMA-Anwendbarkeitsstatus bestätigen
**Schritt 2:** ISO-27001:2022-Compliance-Baseline-Bewertung durchführen
**Schritt 3:** FINMA-spezifische Anforderungen über ISO 27001 hinaus identifizieren
**Schritt 4:** Lücken dokumentieren und Abhilfepläne entwickeln
**Schritt 5:** Kritische FINMA-Randnummern priorisieren (56, 58, 62, 63–72)
**Schritt 6:** Kontrollen mit FINMA-Compliance-Nachweisen umsetzen
**Schritt 7:** Interne Prüfung mit FINMA-Fokus durchführen
**Schritt 8:** Vorbereitung auf potenzielle FINMA-Prüfung

## Compliance-Nachweisanforderungen

FINMA erwartet dokumentierte Nachweise für:

- Vom Management genehmigte Richtlinien und Verfahren
- Risikobewertungen und Behandlungsentscheidungen
- Zugangskontrollkonfigurationen und -überprüfungen
- Protokollaufbewahrung und Überwachungsfähigkeiten
- BC/DR-Testergebnisse und Abhilfemaßnahmen
- Vorfallberichte und Lessons Learned
- Drittparteien-Risikobewertungen und Verträge
- Prüfungsberichte (intern und extern)

---

# Umsetzungsüberlegungen

## FINMA-Compliance-Zeitplan

**Wenn [Organisation] FINMA-reguliert wird:**

**Monate 1–3: Lückenanalyse**

- FINMA-Anwendbarkeitsbestimmung bestätigen
- Aktuellen ISO-27001-Compliance-Status dokumentieren
- FINMA-spezifische Lücken identifizieren
- Abhilfemaßnahmen priorisieren

**Monate 4–6: Umsetzung kritischer Kontrollen**

- Authentifizierung und Zugangskontrolle (Randnummer 56)
- Funktionstrennung (Randnummer 58)
- Verschlüsselung (Randnummer 62)
- Protokollierungsinfrastruktur (Randnummern 63–68)

**Monate 7–9: Überwachung und Resilienz**

- SIEM-Implementierung und -Optimierung (Randnummern 69–72)
- Verbesserung der Betriebskontinuität (Randnummern 73–80)
- Incident-Response-Verfahren (Randnummern 85–87)

**Monate 10–12: Tests und Validierung**

- Interne Prüfung mit FINMA-Fokus
- BC/DR-Tests (Randnummern 81–84)
- Dokumentation der Compliance-Nachweise
- Management- und Vorstandsberichterstattung

**Laufend:** Jährlicher Zyklus aus Tests, Bewertung und Verbesserung

## Ressourcenanforderungen

**Personal:**

- ISB oder Äquivalent (von FINMA gefordert)
- Compliance-Officer mit FINMA-Kenntnissen
- Security-Operations-Team (SOC)
- Business-Continuity-Manager
- Interne Revision mit IT-Sicherheitskenntnissen

**Technologie:**

- Identity and Access Management (IAM) Plattform
- Privileged Access Management (PAM)
- SIEM-Plattform mit 24/7-Überwachung
- Verschlüsselungs-Schlüsselverwaltung (HSM oder Cloud KMS)
- Business-Continuity-Tools und Ausweichstandort

**Externe Unterstützung:**

- Rechtsberatung mit FINMA-Erfahrung
- Externe Prüfer mit FINMA-Kenntnissen
- Managed Security Service Provider (MSSP) bei Bedarf

## Kostenfolgen

FINMA-Compliance erfordert typischerweise:

- Erweiterte Sicherheitstechnologie (IAM, PAM, SIEM, HSM)
- Erhöhter Personalbestand (ISB, SOC, Compliance)
- Externe Prüfungs- und Beratungskosten
- Business-Continuity-Infrastruktur (DR-Standort)
- Laufende Schulungs- und Sensibilisierungsprogramme

Geschätzte Mehrkosten: 15–25% über die Basis-ISO-27001-Compliance für kleine und mittlere Finanzinstitute.

---

# Häufige Fallstricke und Erfahrungswerte

## Häufige FINMA-Compliance-Herausforderungen

**Herausforderung 1: Unterschätzung der FINMA-Strenge**

- FINMA-Prüfungen sind gründlich und nachweisbasiert
- Dokumentation muss umfassend und aktuell sein
- Richtlinien allein genügen nicht; Nachweise der Umsetzung sind erforderlich

**Herausforderung 2: Unzureichende Funktionstrennung**

- Funktionstrennungsverletzungen in kleinen Instituten häufig
- Kompensatorische Kontrollen müssen robust und dokumentiert sein
- Automatisierte Funktionstrennung-Überwachung wird dringend empfohlen

**Herausforderung 3: Unzureichende Protokollierung und Überwachung**

- Protokollaufbewahrung oft kürzer als FINMA-Erwartung (mindestens 12 Monate)
- SIEM nicht auf Anwendungsfälle von Finanzinstituten optimiert
- SOC-Besetzung unzureichend für 24/7-Abdeckung

**Herausforderung 4: BC/DR-Testlücken**

- Vollständige DR-Tests werden nicht jährlich durchgeführt
- Testergebnisse nicht ausreichend dokumentiert
- Lücken nicht zeitnah behoben

**Herausforderung 5: Outsourcing-Risikomanagement**

- Cloud-Dienste als „Technologie" und nicht als Auslagerung behandelt
- FINMA-Meldeanforderungen übersehen
- Prüfungsrecht-Klauseln in Verträgen fehlen

## Bestpraktiken

**Praktik 1:** FINMA-erfahrene Prüfer frühzeitig einbinden
**Praktik 2:** Vierteljährliche interne FINMA-Compliance-Überprüfungen durchführen
**Praktik 3:** Umfassendes Compliance-Nachweis-Repository führen
**Praktik 4:** FINMA-Anforderungen ins Änderungsmanagement integrieren
**Praktik 5:** Vorstand und Geschäftsleitung zu FINMA-Erwartungen schulen
**Praktik 6:** Direkten Kommunikationskanal mit FINMA-Aufseher einrichten

---

# Referenzen und Ressourcen

## FINMA-Publikationen

**Primäre Quellen:**

- FINMA Rundschreiben 2023/1: Operationelle Risiken und Resilienz — Banken
- FINMA Rundschreiben 2008/7: Auslagerung — Banken
- FINMA Rundschreiben 2018/3: Auslagerung — Versicherungen
- FINMA Guidance 05/2023: Cloud-Auslagerung

**FINMA-Website:** https://www.finma.ch/
**FINMA-Rundschreiben:** https://www.finma.ch/de/dokumentation/finma-rs/

## Verwandte Standards und Rahmenwerke

**ISO-Standards:**

- ISO/IEC 27001:2022: Informationssicherheitsmanagementsysteme
- ISO/IEC 27002:2022: Informationssicherheitskontrollen
- ISO/IEC 27017:2015: Sicherheit für Cloud-Dienste
- ISO/IEC 27018:2019: Schutz personenbezogener Daten in der öffentlichen Cloud

**NIST-Publikationen:**

- NIST SP 800-53: Sicherheits- und Datenschutzkontrollen (informative Referenz)
- NIST Cybersecurity Framework (informative Referenz)

**Branchenhinweise:**

- Schweizerische Bankiervereinigung: IT-Sicherheitsrichtlinien
- EBA-Leitlinien zu IKT- und Sicherheitsrisikomanagement (EU-Kontext)

## Rechts- und Compliance-Ressourcen

**Schweizerische Bundesgesetze:**

- Finanzmarktaufsichtsgesetz (FINMAG)
- Bankengesetz (BankG)
- Datenschutzgesetz (nDSG)

**Compliance-Beratung:**
Organisationen, die der FINMA-Aufsicht unterliegen, sollten einbinden:

- Rechtsberatung mit Expertise im Schweizer Finanzrecht
- Prüfer mit Erfahrung in FINMA-Prüfungen
- Compliance-Berater mit FINMA-Kenntnissen

---

# Anhang A: FINMA Compliance-Selbstbewertungs-Checkliste

Diese Checkliste unterstützt die initiale Lückenanalyse für FINMA-beaufsichtigte Organisationen:

## Informationssicherheitsrahmen (Randnummern 50–55)

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| Informationssicherheitsstrategie dokumentiert und vorstandsgenehmigt | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| ISB oder äquivalente Rolle eingerichtet | ⬜ Ja ⬜ Nein | | |
| Jährliche Informationssicherheits-Risikobewertung durchgeführt | ⬜ Ja ⬜ Nein | | |
| Umfassende Sicherheitsrichtlinien dokumentiert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Jährliche Sicherheitsschulung für alle Mitarbeitenden | ⬜ Ja ⬜ Nein | | |
| Drittparteien-Risikobewertungsprozess eingerichtet | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |

## Authentifizierung und Zugangskontrolle (Randnummer 56)

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| MFA für Fernzugang implementiert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| MFA für privilegierte Konten implementiert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Rollenbasierte Zugangskontrolle (RBAC) implementiert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Jährliche Zugangsbestätigung durchgeführt | ⬜ Ja ⬜ Nein | | |
| Privileged Access Management (PAM) implementiert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |

## Funktionstrennung (Randnummer 58)

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| Funktionstrennung-Matrix dokumentiert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Automatisierte Funktionstrennung-Überwachung implementiert | ⬜ Ja ⬜ Nein | | |
| Funktionstrennungsverletzungen vierteljährlich gemeldet | ⬜ Ja ⬜ Nein | | |
| Kompensatorische Kontrollen für unvermeidliche Konflikte dokumentiert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |

## Verschlüsselung (Randnummer 62)

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| TLS 1.2+ für alle Daten bei der Übertragung | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Vollständige Datenträgerverschlüsselung für Endpunkte | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Datenbankverschlüsselung für sensible Daten | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Zentrales Schlüsselverwaltungssystem | ⬜ Ja ⬜ Nein | | |
| Keine Verwendung veralteter Verschlüsselungsalgorithmen | ⬜ Ja ⬜ Nein | | |

## Protokollierung und Überwachung (Randnummern 63–72)

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| Umfassende Protokollierung sicherheitsrelevanter Ereignisse | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Protokollaufbewahrung mindestens 12 Monate | ⬜ Ja ⬜ Nein | | |
| Zentrales Log-Management (SIEM) | ⬜ Ja ⬜ Nein | | |
| 24/7-Sicherheitsüberwachung (SOC) | ⬜ Ja ⬜ Nein | | |
| Echtzeit-Alarmierung bei kritischen Ereignissen | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |

## Betriebskontinuität (Randnummern 73–87)

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| Business Impact Analysis (BIA) durchgeführt | ⬜ Ja ⬜ Nein | | |
| RTO/RPO definiert und vorstandsgenehmigt | ⬜ Ja ⬜ Nein | | |
| Betriebskontinuitätspläne dokumentiert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Jährlicher vollständiger DR-Test durchgeführt | ⬜ Ja ⬜ Nein | | |
| Incident-Response-Verfahren dokumentiert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| FINMA-Incident-Meldeprozess eingerichtet | ⬜ Ja ⬜ Nein | | |

## Auslagerung (FINMA 2008/7)

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| Wesentliche Auslagerungsvereinbarungen bei FINMA gemeldet | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Dienstleister-Risikobewertungen durchgeführt | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Verträge enthalten Prüfungsrecht-Klauseln | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Jährliche SOC-2-Typ-II-Berichte von Anbietern eingeholt | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Exit-Strategien für kritische Anbieter dokumentiert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |

---

# Anhang B: FINMA-Meldeformularvorlage

**Betreff:** Meldung [Vorfalltyp] — [Name der Organisation]

**An:** FINMA-Aufsichtsteam
**Von:** [Name ISB / Compliance-Officer]
**Datum:** [Datum]
**Organisation:** [Rechtliche Einheit]
**FINMA-Lizenznummer:** [Nummer]

**Vorfallzusammenfassung:**

- **Vorfalltyp:** [Sicherheitsverletzung / Systemausfall / Datenverlust / Sonstiges]
- **Entdeckungsdatum/-uhrzeit:** [ISO 8601 Format]
- **Vorfall-Startdatum/-uhrzeit:** [ISO 8601 Format]
- **Aktueller Status:** [Laufend / Eingedämmt / Gelöst]

**Folgenabschätzung:**

- **Betroffene kritische Geschäftsprozesse:** [Liste]
- **Kundenauswirkungen:** [Anzahl Kunden, Serviceunterbrechung]
- **Datenauswirkungen:** [Arten und Menge betroffener Daten]
- **Finanzielle Auswirkungen:** [Schätzung, falls bekannt]

**Ursache** (vorläufig bei laufendem Vorfall):
[Kurzbeschreibung]

**Ergriffene Abhilfemaßnahmen:**
1. [Massnahme 1 — Datum/Uhrzeit]
2. [Massnahme 2 — Datum/Uhrzeit]
3. [Massnahme 3 — Datum/Uhrzeit]

**Laufende Massnahmen:**

- [Massnahme mit erwartetem Abschlussdatum]

**Benachrichtigte externe Parteien:**

- [Kunden: Ja/Nein/Geplant]
- [Datenschutzbehörde: Ja/Nein/N/A]
- [Andere Regulatoren: Angabe]

**Nächste Aktualisierung:** [Datum/Uhrzeit der nächsten Meldung an FINMA]

**Kontaktinformationen:**

- **Primärer Kontakt:** [Name, Titel, Telefon, E-Mail]
- **Stellvertretender Kontakt:** [Name, Titel, Telefon, E-Mail]

---

**ENDE DER TECHNISCHEN REFERENZ**

---

*Diese technische Referenz unterstützt potenzielle FINMA-Compliance-Anforderungen gemäß ISMS-POL-00. Alle Feststellungen zur regulatorischen Anwendbarkeit und verbindlichen Anforderungen sind in ISMS-POL-00 und genehmigten ISMS-Richtliniendokumenten definiert.*

*Für Organisationen, die NICHT der FINMA-Aufsicht unterliegen, dient dieses Dokument ausschließlich der informativen Sensibilisierung und begründet KEINE Compliance-Pflichten.*

<!-- QA_VERIFIED: 2026-03-28 -->
