<!-- ISMS-CORE:REF:ISMS-REF-NIS2-DE:framework:REF:nis2 -->
**ISMS-REF-NIS2-DE — Richtlinie über Netz- und Informationssicherheit 2 (NIS2) Anforderungsreferenz**
**EU-Cybersicherheitsanforderungen für wesentliche und wichtige Einrichtungen (Nicht-ISMS-Technische Referenz)**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | NIS2 Anforderungsreferenz |
| **Dokumententyp** | Intern — Technische Referenz (nicht ISMS) |
| **Dokumenten-ID** | ISMS-REF-NIS2-DE |
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
| 1.0 | [Datum] | ISB / Rechts-/Compliance-Abteilung | Erste technische Referenz für EU-Einrichtungen |

**Überprüfungszyklus:** Jährlich (oder bei Aktualisierungen nationaler Umsetzungsgesetze)
**Nächstes Überprüfungsdatum:** [Datum + 12 Monate]
**Genehmigende:** Rechts-/Compliance-Abteilung / ISB (technische Referenz, keine ISMS-Genehmigung erforderlich)

**Verbreitung:** Compliance-Team, ISB, Rechtsberatung (für NIS2-regulierte Organisationen)

---

⚠️ **WICHTIG – NICHT-ISMS TECHNISCHES UNTERSTÜTZUNGSDOKUMENT**

Dieses Dokument dient ausschließlich Informations- und Sensibilisierungszwecken.

- Dieses Dokument ist KEIN Teil des Informationssicherheitsmanagementsystems (ISMS).
- Dieses Dokument definiert KEINE zwingenden Anforderungen, außer wenn [Organisation] eine NIS2-regulierte Einrichtung ist.
- Dieses Dokument begründet KEINE verbindlichen Anforderungen, Fristen, KPIs oder SLAs für nicht regulierte Unternehmen.
- Dieses Dokument schreibt die Übernahme von NIS2-Anforderungen für nicht NIS2-pflichtige Organisationen NICHT vor.
- Dieses Dokument überschreibt oder erweitert keine ISMS-Richtlinie.

**Anwendbarkeitsbestimmung:**
NIS2-Anforderungen gelten NUR, wenn [Organisation]:

- Eine wesentliche oder wichtige Einrichtung ist, die in der EU in erfassten Sektoren tätig ist
- Unter Größenschwellen fällt (typischerweise mittlere/große Unternehmen)
- Dienstleistungen erbringt, die unter NIS2 Anhang I (wesentlich) oder Anhang II (wichtig) fallen
- In einem EU-Mitgliedstaat tätig ist, der NIS2 in nationales Recht umgesetzt hat

Für alle anderen Organisationen dient dieses Dokument ausschließlich als:

- Technische Referenz für potenzielle NIS2-Anforderungen
- Kontext für Geschäftsexpansion in EU-regulierte Sektoren
- Sensibilisierung für EU-Cybersicherheitsstandards
- **Dieses Dokument darf nicht als Audit-Nachweis verwendet werden, außer wenn [Organisation] NIS2-reguliert ist**

Die Verwendung dieses Dokuments impliziert keine NIS2-Anwendbarkeit, Compliance-Pflichten oder Regulierungsstatus.

**Wesentlicher Positionierungshinweis:**
Dieses Dokument enthält absichtlich regulatorische Details, die über das für die meisten Organisationen Zutreffende hinausgehen. Sein Zweck ist ausschließlich die Sensibilisierung von Organisationen, die bei Expansion ihrer Aktivitäten möglicherweise NIS2-pflichtig werden könnten, oder die Dienstleistungen für NIS2-regulierte Einrichtungen erbringen. Aus dem Vorhandensein, dem Fehlen oder dem Umsetzungsstatus eines hier aufgeführten NIS2-Requiremenst dürfen keine Audit-Schlussfolgerungen gezogen werden, außer wenn [Organisation] explizit NIS2-reguliert ist.

---

# Dokumentenzweck und Geltungsbereich

## Zweck

Dieses Dokument gibt einen technischen Überblick über die Anforderungen der Richtlinie über Netz- und Informationssicherheit 2 (Richtlinie (EU) 2022/2555) für wesentliche und wichtige Einrichtungen in der EU. Es soll unterstützen bei:

- Sensibilisierung für NIS2-Anforderungen für erfasste EU-Sektoren
- Verständnis des NIS2-Cybersicherheits-Risikomanagement-Rahmens
- Kontext für Organisationen, die in NIS2-regulierte Sektoren expandieren
- Zukünftige Anwendbarkeitsbeurteilung
- Zuordnung von NIS2-Anforderungen zu ISO 27001:2022 Kontrollen

## Was dieses Dokument NICHT ist

Dieses Dokument:

- Begründet KEINE zwingenden Anforderungen für nicht NIS2-regulierte Organisationen
- Definiert NICHT die Compliance-Pflichten von [Organisation] (siehe POL-00 für regulatorische Anwendbarkeit)
- Schafft KEINE Audit-Kriterien, außer wenn [Organisation] NIS2-reguliert ist
- Ersetzt KEINE Interpretation durch Rechts- oder Compliance-Beratung
- Stellt KEINE Rechtsberatung zur NIS2-Compliance dar
- Deckt NICHT alle nationalen Umsetzungsvarianten ab (NIS2 ist eine Richtlinie, die nationale Umsetzung erfordert)
- Begründet KEINE Umsetzungsverfahren oder Verifikationsprozesse

## Beziehung zum ISMS

Dieses Dokument ist eine **unverbindliche technische Referenz**, AUSSER wenn [Organisation] NIS2-pflichtig ist (wie in ISMS-POL-00 Abschnitt 3.3 festgestellt).

**Wenn [Organisation] NIS2-reguliert IST:**

- NIS2-Anforderungen werden gemäß POL-00 zu Stufe 1 (Zwingend)
- Dieses Dokument liefert Umsetzungshinweise
- ISMS-Kontrollen müssen NIS2-Compliance nachweisen
- Incident-Meldung und Koordination mit dem nationalen CSIRT erforderlich

**Wenn [Organisation] NICHT NIS2-reguliert ist:**

- NIS2 bleibt gemäß POL-00 bei Stufe 3 (Informativ)
- Dieses Dokument dient ausschließlich der Sensibilisierung
- Keine NIS2-Compliance-Pflichten
- ISMS-Kontrollen folgen ausschließlich ISO 27001:2022

## Inhaltsorganisation

Diese Referenz organisiert NIS2-Anforderungen nach:

- Geltungsbereich und Anwendbarkeit (Einrichtungen, Sektoren, Größenschwellen)
- Cybersicherheits-Risikomanagementmaßnahmen (Artikel 21)
- Meldepflichten bei Vorfällen (Artikel 23)
- Lieferkettensicherheit (Artikel 21)
- Aufsichtsrahmen und Sanktionen
- Zuordnung zu ISO 27001:2022 Annex-A-Kontrollen

---

# NIS2 — Überblick und Anwendbarkeit

## Was ist NIS2?

**Richtlinie (EU) 2022/2555** über Maßnahmen für ein hohes gemeinsames Cybersicherheitsniveau in der Union, ersetzt die ursprüngliche NIS-Richtlinie (2016/1148).

**Wichtige Daten:**

- **Inkrafttreten:** 16. Januar 2023
- **Umsetzungsfrist:** 17. Oktober 2024 (EU-Mitgliedstaaten müssen in nationales Recht umsetzen)
- **Anwendung:** Variiert je nach Mitgliedstaat (typischerweise 6–12 Monate nach Veröffentlichung des nationalen Gesetzes)

**Zweck:**

- Stärkung der Cybersicherheitsresilienz in kritischen EU-Sektoren
- Harmonisierung der Cybersicherheitsanforderungen in den Mitgliedstaaten
- Erweiterung des Geltungsbereichs über die ursprüngliche NIS-Richtlinie hinaus
- Einrichtung eines Vorfallmelderahmens
- Einführung von Aufsichts- und Durchsetzungsmaßnahmen

**Rechtsnatur:**

- Richtlinie (keine Verordnung), daher müssen Mitgliedstaaten in nationales Recht umsetzen
- Nationale Variationen bei Umsetzungsdetails möglich
- Kernanforderungen bleiben EU-weit einheitlich

**Aufsichtsbehörden:**

- Nationale zuständige Behörden (von jedem Mitgliedstaat bestimmt)
- Computer Security Incident Response Teams (CSIRTs)
- Einzelne Ansprechpartner (Single Points of Contact, SPOCs)

## Geltungsbereich und erfasste Sektoren

NIS2 unterscheidet zwei Kategorien von Einrichtungen:

**Wesentliche Einrichtungen** (Anhang I — Höhere Auswirkung, strengere Anforderungen):

| Sektor | Teilsektoren |
|--------|-------------|
| **Energie** | Strom, Fernwärme/-kälte, Öl, Gas, Wasserstoff |
| **Verkehr** | Luft, Bahn, See, Straßenverkehr |
| **Bankwesen** | Kreditinstitute |
| **Finanzmarktinfrastrukturen** | Handelsplätze, zentrale Gegenparteien, Zentralverwahrer |
| **Gesundheit** | Gesundheitsdienstleister, EU-Referenzlaboratorien, Pharmahersteller für kritische Arzneimittel |
| **Trinkwasser** | Trinkwasserlieferanten und -verteiler |
| **Abwasser** | Abwasserentsorgung und -sammlung |
| **Digitale Infrastruktur** | Internetknoten, DNS-Dienstanbieter (außer Root-Nameserver), TLD-Namensregistrare, Cloud-Computing-Dienste, Rechenzentrumsdienstanbieter, Content-Delivery-Networks, Vertrauensdienstanbieter, öffentliche elektronische Kommunikationsnetze, öffentlich zugängliche elektronische Kommunikationsdienste |
| **IKT-Dienstverwaltung** | Managed-Service-Anbieter, Managed-Security-Service-Anbieter |
| **Öffentliche Verwaltung** | Zentrale Regierungsstellen |
| **Weltraum** | Betreiber bodengestützter Infrastruktur zur Unterstützung von Weltraumdiensten |

**Wichtige Einrichtungen** (Anhang II — Mittlere Auswirkung, verhältnismäßige Anforderungen):

| Sektor | Teilsektoren |
|--------|-------------|
| **Post- und Kurierdienste** | Post- und Kurierdienstanbieter |
| **Abfallbewirtschaftung** | Abfallsammlung, -behandlung, -entsorgung |
| **Herstellung, Produktion, Vertrieb chemischer Stoffe** | Chemische Stoffe und Gemische |
| **Lebensmittelproduktion, -verarbeitung, -vertrieb** | Lebensmittelunternehmer (großmaßstäblich) |
| **Herstellung** | Medizinprodukte, Computer/Elektronik/Optik, elektrische Ausrüstungen, Maschinen, Kraftfahrzeuge/Anhänger, andere Transportmittel |
| **Digitale Anbieter** | Online-Marktplätze, Online-Suchmaschinen, Plattformen sozialer Netzwerke |
| **Forschung** | Forschungsorganisationen |

## Größen- und Geltungsbereichskriterien

**Größenschwellen** (Artikel 2):

| Unternehmensgröße | Mitarbeitende | Jahresumsatz ODER Bilanzsumme | NIS2-Anwendbarkeit |
|-------------------|---------------|-------------------------------|-------------------|
| **Groß** | ≥ 250 | > €50 Mio. Umsatz ODER > €43 Mio. Bilanzsumme | Im Geltungsbereich (bei erfasstem Sektor) |
| **Mittel** | 50–249 | ≤ €50 Mio. Umsatz UND ≤ €43 Mio. Bilanzsumme | Im Geltungsbereich (bei erfasstem Sektor) |
| **Klein** | 10–49 | ≤ €10 Mio. Umsatz UND ≤ €10 Mio. Bilanzsumme | Grundsätzlich außerhalb des Geltungsbereichs |
| **Kleinstunternehmen** | < 10 | ≤ €2 Mio. Umsatz UND ≤ €2 Mio. Bilanzsumme | Außerhalb des Geltungsbereichs |

**Ausnahmen:**

- **Alleinanbieter:** Auch wenn klein, können sie im Geltungsbereich liegen, wenn sie der einzige Anbieter eines wesentlichen Dienstes sind
- **Öffentliche Verwaltung:** Größenschwellen gelten nicht
- **Kritische Infrastruktur:** Mitgliedstaaten können weitere Einrichtungen einbeziehen

## Anwendbarkeitsbestimmung

**NIS2 gilt für [Organisation], WENN:**

| Kriterium | Status | Nachweis |
|-----------|--------|----------|
| Tätig in einem EU-Mitgliedstaat | ⬜ Ja ⬜ Nein | [Land] |
| Gehört zu erfasstem Sektor (Anhang I oder II) | ⬜ Ja ⬜ Nein | [Sektor] |
| Erfüllt Größenschwellen (mittel oder groß) | ⬜ Ja ⬜ Nein | [Mitarbeitende / Umsatz] |
| Von nationaler Behörde bestimmt | ⬜ Ja ⬜ Nein ⬜ Unbekannt | [Bestimmungsschreiben falls zutreffend] |
| Mitgliedstaat hat NIS2 in nationales Recht umgesetzt | ⬜ Ja ⬜ Nein ⬜ Ausstehend | [Nationales Gesetz] |

**Bei erfüllten Kriterien:** NIS2-Anforderungen sind gemäß POL-00 Abschnitt 3.3 **Stufe 1 (Zwingend)**

**Bei nicht erfüllten Kriterien:** NIS2-Anforderungen bleiben gemäß POL-00 **Stufe 3 (Informativ)**

**Hinweis zur nationalen Umsetzung:**
Jeder EU-Mitgliedstaat setzt NIS2 durch nationales Gesetz um. Organisationen müssen ihre nationale Cybersicherheitsbehörde für spezifische Anforderungen konsultieren, da Umsetzungsdetails variieren können.

---

# Artikel 21 — Cybersicherheits-Risikomanagementmaßnahmen

## Überblick

Artikel 21 legt **Mindestanforderungen an Cybersicherheits-Risikomanagementmaßnahmen** fest, die wesentliche und wichtige Einrichtungen umsetzen müssen.

**Rechtspflicht** (Artikel 21(1)):
Mitgliedstaaten stellen sicher, dass Einrichtungen „geeignete und verhältnismäßige" technische, operative und organisatorische Maßnahmen ergreifen, um Cybersicherheitsrisiken zu bewältigen und die Auswirkungen von Vorfällen zu minimieren.

**Verhältnismäßigkeitsprinzip:**
Maßnahmen müssen angemessen sein in Bezug auf:

- Art und Umfang der Aktivitäten der Einrichtung
- Größe der Einrichtung
- Wahrscheinlichkeit und Schwere von Vorfällen
- Stand der Technik in der Cybersicherheit

## Zehn Mindestmaßnahmen (Artikel 21(2))

**1. Risikoanalyse und Sicherheitsrichtlinien für Informationssysteme**

**Anforderung:**

- Richtlinien zur Risikoanalyse und Informationssystem-Sicherheit
- Umfassende Risikobewertungsmethodik
- Regelmäßige Risikoüberprüfungen und -aktualisierungen
- Dokumentation der Risikobehandlungsentscheidungen

**ISO 27001:2022 Zuordnung:**

- Klausel 6.1.2: Informationssicherheits-Risikobewertung
- Klausel 6.1.3: Informationssicherheits-Risikobehandlung
- A.5.1: Richtlinien für Informationssicherheit

**Umsetzungshinweise:**

- Mindestens jährliche Risikobewertung
- Risikobasierter Ansatz ausgerichtet an Geschäftsauswirkung
- Risikoberichterstattung auf Vorstandsebene
- Integration ins unternehmerische Risikomanagement

---

**2. Incident-Handhabung**

**Anforderung:**

- Richtlinien und Verfahren zur Incident-Handhabung
- Erkennung, Klassifizierung, Reaktion und Wiederherstellung bei Vorfällen
- Kommunikationspläne (intern und extern)
- Lessons Learned und kontinuierliche Verbesserung

**ISO 27001:2022 Zuordnung:**

- A.5.24: Planung und Vorbereitung des Informationssicherheits-Incident-Managements
- A.5.25: Beurteilung und Entscheidung bei Informationssicherheitsereignissen
- A.5.26: Reaktion auf Informationssicherheitsvorfälle
- A.5.27: Lernen aus Informationssicherheitsvorfällen

**NIS2-spezifisch:**

- Meldung von Vorfällen an nationale Behörden (Artikel 23)
- Koordination mit dem nationalen CSIRT
- Kommunikation mit Kunden und Stakeholdern

---

**3. Betriebskontinuität und Krisenmanagement**

**Anforderung:**

- Betriebskontinuitätspläne (BCP)
- Disaster-Recovery-Pläne (DRP)
- Krisenmanagementverfahren
- Backup- und Wiederherstellungsfähigkeiten
- Tests und Validierung

**ISO 27001:2022 Zuordnung:**

- A.5.29: Informationssicherheit bei Störungen
- A.5.30: IKT-Bereitschaft für Betriebskontinuität
- A.8.13: Datensicherung
- A.8.14: Redundanz von Informationsverarbeitungseinrichtungen

**NIS2-Schwerpunkt:**

- Fokus auf Kontinuität wesentlicher Dienste
- Recovery Time Objectives (RTO) für kritische Funktionen
- Regelmäßige Tests (mindestens jährlich)

---

**4. Lieferkettensicherheit**

**Anforderung:**

- Maßnahmen zur Sicherung der Lieferkette
- Bewertung der Cybersicherheitspraktiken von Lieferanten
- Vertragliche Sicherheitsanforderungen
- Überwachung der Sicherheitslage von Lieferanten
- Risikobasierter Ansatz für Lieferantenbeziehungen

**ISO 27001:2022 Zuordnung:**

- A.5.19: Informationssicherheit in Lieferantenbeziehungen
- A.5.20: Berücksichtigung von Informationssicherheit in Lieferantenvereinbarungen
- A.5.21: Management der Informationssicherheit in der IKT-Lieferkette
- A.5.22: Überwachung, Überprüfung und Änderungsmanagement von Lieferantendienstleistungen

**NIS2-spezifisch:**

- Expliziter Fokus auf Cybersicherheitsaspekte der Lieferkette
- Umfasst sowohl direkte Lieferanten als auch Lieferkettenabhängigkeiten
- Offenlegung von Schwachstellen und Koordination mit Lieferanten

---

**5. Sicherheit bei Erwerb, Entwicklung und Wartung von Netz- und Informationssystemen**

**Anforderung:**

- Sicherer Entwicklungslebenszyklus
- Sicherheitsanforderungen bei der Beschaffung
- Sicherheitstests vor der Bereitstellung
- Wartungs- und Patch-Verfahren
- Änderungsmanagementkontrollen

**ISO 27001:2022 Zuordnung:**

- A.8.4: Zugang zu Quellcode
- A.8.8: Management technischer Schwachstellen
- A.8.9: Konfigurationsmanagement
- A.8.25: Sicherer Entwicklungslebenszyklus
- A.8.26: Anforderungen an Anwendungssicherheit
- A.8.27: Sichere Systemarchitektur und Entwicklungsprinzipien
- A.8.28: Sicheres Coding
- A.8.29: Sicherheitstests in Entwicklung und Abnahme
- A.8.30: Ausgelagerte Entwicklung

**Umsetzung:**

- Security-by-Design-Prinzipien
- Schwachstellenmanagementprogramm
- Patch-Management mit definierten SLAs
- Sichere Konfigurationsgrundlagen

---

**6. Richtlinien und Verfahren zur Bewertung der Wirksamkeit von Cybersicherheits-Risikomanagementmaßnahmen**

**Anforderung:**

- Regelmäßige Bewertung der Wirksamkeit von Sicherheitskontrollen
- Interne Audits
- Sicherheitsmetriken und KPIs
- Kontinuierliche Überwachung und Verbesserung

**ISO 27001:2022 Zuordnung:**

- Klausel 9.1: Überwachung, Messung, Analyse und Bewertung
- Klausel 9.2: Internes Audit
- Klausel 9.3: Managementbewertung
- Klausel 10.1–10.2: Kontinuierliche Verbesserung

**Bewertungsmethoden:**

- Interne Sicherheitsbewertungen
- Schwachstellenbewertungen
- Penetrationstests
- Drittprüfungen
- Compliance-Überprüfungen

---

**7. Grundlegende Cyber-Hygiene-Praktiken und Cybersicherheitsschulungen**

**Anforderung:**

- Sensibilisierungs- und Schulungsprogramme für Benutzer
- Grundlegende Cyber-Hygiene-Maßnahmen
- Rollenbasierte Sicherheitsschulungen
- Regelmäßige Sicherheitssensibilisierungskampagnen
- Messung der Schulungswirksamkeit

**ISO 27001:2022 Zuordnung:**

- A.6.3: Sensibilisierung, Aus- und Weiterbildung zur Informationssicherheit
- A.6.4: Disziplinarverfahren (Verantwortlichkeit)

**Cyber-Hygiene-Maßnahmen:**

- Starke Passwort-Richtlinien
- Multi-Faktor-Authentifizierung (MFA)
- Phishing-Sensibilisierung und Tests
- Leitfaden für sicheres Arbeiten im Homeoffice
- BYOD- und Mobilgeräte-Sicherheit
- E-Mail- und Web-Sicherheit

**Schulungsanforderungen:**

- Jährliche Pflichtschulung für alle Mitarbeitenden
- Spezialisierte Schulungen für IT- und Sicherheitspersonal
- Phishing-Simulationstests
- Verfolgung des Schulungsabschlusses

---

**8. Kryptographie und Verschlüsselung**

**Anforderung:**

- Verwendung von Kryptographie zum Datenschutz
- Verschlüsselung sensibler Daten im Ruhezustand und bei der Übertragung
- Verwaltung kryptographischer Schlüssel
- Ausrichtung an aktuellen Verschlüsselungsstandards

**ISO 27001:2022 Zuordnung:**

- A.8.24: Verwendung von Kryptographie

**Umsetzungsstandards:**

- TLS 1.2 Minimum (TLS 1.3 bevorzugt) für Daten bei der Übertragung
- AES-256 für Daten im Ruhezustand
- PKI und Zertifikatsverwaltung
- Keine Verwendung veralteter Algorithmen (DES, 3DES, MD5, SHA-1)
- Hardware Security Modules (HSM) für hochwertige Schlüssel

---

**9. Personalsicherheit, Zugangskontrollen und Asset-Management**

**Anforderungen:**

**Personalsicherheit:**

- Hintergrundprüfungen für sensible Positionen
- Sicherheitspflichten in Arbeitsverträgen
- Austrittsprozesse (Zugangsentzug)

**Zugangskontrolle:**

- Benutzeridentifikation und -authentifizierung
- Prinzip des minimalen Privilegs
- Regelmäßige Zugangsprüfungen
- Privileged Access Management

**Asset-Management:**

- Inventarisierung von Informationswerten
- Asset-Klassifizierung und -Handhabung
- Richtlinien zur akzeptablen Nutzung
- Asset-Entsorgungsverfahren

**ISO 27001:2022 Zuordnung:**

- A.5.9: Inventar von Informationen und anderen zugehörigen Werten
- A.5.10: Akzeptable Nutzung von Informationen und anderen Werten
- A.5.12: Klassifizierung von Informationen
- A.5.15: Zugangskontrolle
- A.5.16: Identitätsmanagement
- A.5.17: Authentifizierungsinformationen
- A.5.18: Zugriffsrechte
- A.6.1: Überprüfung
- A.6.2: Beschäftigungsbedingungen
- A.6.4: Disziplinarverfahren
- A.6.5: Verantwortlichkeiten nach Beendigung oder Wechsel des Arbeitsverhältnisses
- A.8.2: Privilegierte Zugriffsrechte
- A.8.3: Einschränkung des Informationszugriffs
- A.8.10: Löschung von Informationen

---

**10. Multi-Faktor-Authentifizierung, gesicherte Sprach-/Video-/Textkommunikation und Notfallkommunikation**

**Anforderungen:**

**Multi-Faktor-Authentifizierung (MFA):**

- MFA für Fernzugang
- MFA für privilegierte Konten
- MFA für Zugang zu sensiblen Systemen/Daten
- Risikobasierte Authentifizierung wo angemessen

**Gesicherte Kommunikation:**

- Verschlüsselung für Sprach-, Video- und Textkommunikation
- Sichere Kollaborationsplattformen
- Ende-zu-Ende-Verschlüsselung für sensible Kommunikation
- VPN für Fernzugang

**Notfallkommunikationssysteme:**

- Out-of-Band-Kommunikationskanäle für Vorfälle
- Notfallkontaktlisten
- Alternative Kommunikationsmethoden (SMS, Telefon, sichere Nachrichtenübermittlung)
- Krisenkommuni­kationsverfahren

**ISO 27001:2022 Zuordnung:**

- A.5.14: Informationsübertragung
- A.8.5: Sichere Authentifizierung
- A.8.20: Netzwerksicherheit
- A.8.23: Web-Filterung (Kommunikationssicherheit)

**NIS2-spezifisch:**
Dies ist eine der präskriptivsten Anforderungen in NIS2 und schreibt MFA und gesicherte Kommunikation explizit vor — spezifischer als typische ISO-27001-Umsetzungen.

---

## Verantwortung des Leitungsorgans (Artikel 21(3))

**Führungsverantwortung:**
Mitgliedstaaten stellen sicher, dass das Leitungsorgan:

- Cybersicherheits-Risikomanagementmaßnahmen **genehmigt**
- Die Umsetzung **überwacht**
- Bei Nichteinhaltung **haftbar gemacht** werden kann

**Haftungsbestimmungen** (Artikel 21(5)):

- Mitglieder des Leitungsorgans können haftbar gemacht werden
- Mitgliedstaaten können direkte Haftung vorsehen
- Schulung der Leitungsorganmitglieder erforderlich

**ISO 27001:2022 Zuordnung:**

- Klausel 5.1: Führung und Engagement
- Klausel 5.2: Richtlinie
- Klausel 9.3: Managementbewertung

**NIS2-Erweiterung:**
Die explizite Managementhaftung ist NIS2-spezifisch und nicht in ISO 27001 enthalten.

---

# Artikel 23 — Meldung von Vorfällen

## Überblick

Einrichtungen müssen das nationale CSIRT oder die zuständige Behörde über erhebliche Vorfälle informieren.

**Rechtspflicht:**

- **Unverzüglich:** Erstmeldung
- **Dreistufiges Verfahren:** Frühwarnung, Vorfallmeldung, Abschlussbericht

## Meldefrist

| Stufe | Frist | Inhalt |
|-------|-------|--------|
| **Frühwarnung** | Unverzüglich (≤ 24 Stunden nach Kenntnisnahme) | Kenntnis des erheblichen Vorfalls, erster Hinweis auf mögliche grenzüberschreitende Auswirkung |
| **Vorfallmeldung** | Unverzüglich (≤ 72 Stunden nach Kenntnisnahme) | Erstbewertung (Auswirkung, Schwere, Kompromittierungsindikatoren), vorläufige technische Details |
| **Abschlussbericht** | ≤ 1 Monat nach Vorfallmeldung | Detaillierte Beschreibung, Schwere, Auswirkung, Ursache, angewandte/laufende Abhilfemaßnahmen |
| **Zwischenberichte** | Auf Anfrage des CSIRT/der Behörde ODER bei wesentlicher Änderung im Umgang | Aktualisierter Status und Informationen |

## Kriterien für erhebliche Vorfälle

Vorfälle gelten als **erheblich**, wenn sie:

- Eine schwerwiegende Betriebsstörung verursacht haben oder wahrscheinlich verursachen werden
- Einen erheblichen finanziellen Verlust verursacht haben oder wahrscheinlich verursachen werden
- Andere natürliche oder juristische Personen betroffen haben oder wahrscheinlich betreffen werden (Kunden, Partner)

**Bewertungsfaktoren** (Anhang I der Richtlinie — Durchführungsrechtsakt):

- Anzahl betroffener Nutzer/Einrichtungen
- Dauer des Vorfalls
- Geografische Ausbreitung
- Schwere der Dienststörung
- Ausmaß der Auswirkung auf wirtschaftliche und gesellschaftliche Aktivitäten

## Meldeinhalt

**Frühwarnung** (24 Stunden):

- Hinweis, dass ein erheblicher Vorfall aufgetreten ist
- Ob der Vorfall als Ergebnis einer rechtswidrigen oder böswilligen Handlung vermutet wird
- Ob der Vorfall wahrscheinlich grenzüberschreitende Auswirkungen hat

**Vorfallmeldung** (72 Stunden):

- Beschreibung des Vorfalls (Typ, Umfang, Zeitablauf)
- Kompromittierungsindikatoren (IOCs), falls verfügbar
- Erstbewertung von Schwere und Auswirkung
- Art der Bedrohung oder Ursache (falls bekannt)
- Angewandte Abhilfemaßnahmen

**Abschlussbericht** (1 Monat):

- Detaillierte Vorfallbeschreibung
- Vorfalltyp und Ursachenanalyse
- Schwerebeurteilung mit Begründung
- Auswirkung auf Diensterbringung und Kunden
- Abhilfe- und Sanierungsmaßnahmen
- Bewertung grenzüberschreitender Auswirkungen (falls zutreffend)
- Lessons Learned

## Meldeausnahmen

Einrichtungen **können auf Meldung verzichten**, wenn:

- Der Vorfall von einer anderen sektorspezifischen Meldepflicht erfasst wird (z. B. GDPR, DORA für Finanzunternehmen)
- Vorausgesetzt, die Information erreicht das CSIRT oder die zuständige Behörde

**Koordination:**

- NIS2-Vorfallmeldungen können sich mit GDPR-Meldungen bei Verletzungen des Schutzes personenbezogener Daten überschneiden
- DORA-Meldungen für Finanzunternehmen können NIS2-Anforderungen erfüllen
- Mitgliedstaaten können ein einheitliches Meldeportal einrichten

**ISO 27001:2022 Zuordnung:**

- A.5.26: Reaktion auf Informationssicherheitsvorfälle (interne Meldung)
- A.5.5: Kontakt mit Behörden (externe Meldung)

**NIS2 vs. ISO 27001:**
ISO 27001 schreibt keine externen regulatorischen Meldefristen vor — dies ist NIS2-spezifisch.

---

# Lieferkettensicherheit (Artikel 21(2)(d) und Erwägungsgründe)

## Überblick

NIS2 verlangt ausdrücklich, dass Einrichtungen Cybersicherheitsrisiken in ihrer Lieferkette berücksichtigen.

**Anforderung:**

- Sicherheitsmaßnahmen zur Behebung von Schwachstellen bei einzelnen direkten Lieferanten
- Gesamtqualität der Produkte und Dienstleistungen
- Cybersicherheitspraktiken der Lieferanten

## Lieferantenbewertung

**Vorvertragliche Bewertung:**

- Bewertung der Cybersicherheitslage des Lieferanten
- Sicherheitszertifizierungen (ISO 27001, SOC 2, usw.)
- Vorfallhistorie und Reaktionsfähigkeiten
- Datenverarbeitungs- und Datenschutzpraktiken
- Risikobeurteilung für Unterauftragnehmer

**Laufende Überwachung:**

- Regelmäßige Sicherheitsüberprüfungen (mindestens jährlich)
- Kontinuierliche Überwachung wo angemessen
- Anforderungen zur Vorfallmeldung
- Sicherheitsprüfungsrechte
- Leistung gegenüber Sicherheits-SLAs

## Vertragliche Anforderungen

Verträge mit Lieferanten sollten enthalten:

- Sicherheitspflichten und -standards
- Anforderungen zur Vorfallmeldung
- Prüfungs- und Bewertungsrechte
- Datenschutz und Vertraulichkeit
- Einschränkungen bei Unterauftragsvergabe
- Haftung und Schadensersatz
- Kündigungsrechte bei Sicherheitsverletzungen

**ISO 27001:2022 Zuordnung:**

- A.5.19: Informationssicherheit in Lieferantenbeziehungen
- A.5.20: Berücksichtigung von Informationssicherheit in Lieferantenvereinbarungen
- A.5.21: Management der Informationssicherheit in der IKT-Lieferkette

## Lieferketten-Risikomanagement

**Risikobasierter Ansatz:**

- Kritikalitätsbewertung (Auswirkung bei Lieferantenausfall)
- Konzentrationsrisiko (Abhängigkeit von einem einzigen Lieferanten)
- Geografisches Risiko (Standort der Lieferanten/Daten)
- Substituierbarkeit (Verfügbarkeit von Alternativen)

**Minderungsstrategien:**

- Diversifizierung des Lieferantenstamms
- Vertragliche Schutzmaßnahmen
- Treuhandvereinbarungen für kritische Software
- Betriebskontinuitätsklauseln
- Exit-Strategien

---

# Aufsichts- und Durchsetzungsrahmen

## Nationale zuständige Behörden

Jeder Mitgliedstaat bestimmt:

- **Zuständige Behörde:** Zuständig für NIS2-Aufsicht
- **CSIRT (Computer Security Incident Response Team):** Technische Incident-Response
- **Single Point of Contact (SPOC):** Verbindungsfunktion für grenzüberschreitende Zusammenarbeit

**Aufsichtsbefugnisse** (Artikel 32):

- Vor-Ort- und Fernprüfungen
- Sicherheitsaudits durch qualifizierte Prüfer
- Informationsanfragen
- Anfragen nach Umsetzungsnachweisen
- Zugang zu Daten, Dokumenten, Einrichtungen

## Durchsetzungsmaßnahmen (Artikel 34)

**Verwaltungssanktionen:**

- Verbindliche Anweisungen
- Verwarnungen
- Compliance-Anordnungen
- Vorübergehendes Verbot von Mitgliedern des Leitungsorgans
- **Bußgelder** (siehe Abschnitt 6.3)
- Öffentliche Bekanntmachung der Nichteinhaltung

**Dringlichkeitsmaßnahmen:**
Bei ernstem und unmittelbarem Risiko können Behörden:

- Sofortige Umsetzung von Sicherheitsmaßnahmen anordnen
- Nutzung kompromittierter Systeme einschränken oder verbieten
- Dienste vorübergehend aussetzen

## Sanktionen (Artikel 34)

**Wesentliche Einrichtungen** (Anhang I):

- Bis zu **€10.000.000** ODER
- **2 % des gesamten weltweiten Jahresumsatzes** (je nachdem, welcher Betrag höher ist)

**Wichtige Einrichtungen** (Anhang II):

- Bis zu **€7.000.000** ODER
- **1,4 % des gesamten weltweiten Jahresumsatzes** (je nachdem, welcher Betrag höher ist)

**Berücksichtigte Faktoren:**

- Schwere und Dauer des Verstoßes
- Vorsätzlicher oder fahrlässiger Charakter
- Ergriffene Maßnahmen zur Schadensminderung
- Frühere Verstöße
- Erzielte finanzielle Vorteile oder vermiedene Verluste
- Kooperation mit der Behörde

**Managementhaftung** (Artikel 21(5)):

- Mitgliedstaaten können Mitglieder des Leitungsorgans persönlich haftbar machen
- Vorübergehendes Verbot von Managementpositionen möglich

---

# ISO 27001:2022 — NIS2 Zuordnung

## Kontroll-Zuordnungsmatrix

| NIS2 Anforderung | NIS2 Artikel | ISO 27001:2022 Kontrolle | Lückenanalyse |
|------------------|-------------|--------------------------|---------------|
| Risikoanalyse und Sicherheitsrichtlinien | Art. 21(2)(a) | Klausel 6.1.2–6.1.3, A.5.1 | Kongruent |
| Incident-Handhabung | Art. 21(2)(b) | A.5.24–5.27 | NIS2: Fügt externe Meldung hinzu |
| Betriebskontinuität & Krisenmanagement | Art. 21(2)(c) | A.5.29–5.30, A.8.13–8.14 | Kongruent |
| Lieferkettensicherheit | Art. 21(2)(d) | A.5.19–5.22 | NIS2: Expliziterer Fokus |
| Sicherer Erwerb, Entwicklung, Wartung | Art. 21(2)(e) | A.8.4, A.8.8–8.9, A.8.25–8.30 | Kongruent |
| Wirksamkeitsbewertung | Art. 21(2)(f) | Klausel 9.1–9.3, 10.1–10.2 | Kongruent |
| Cyber-Hygiene und Schulung | Art. 21(2)(g) | A.6.3 | Kongruent |
| Kryptographie und Verschlüsselung | Art. 21(2)(h) | A.8.24 | Kongruent |
| Personalsicherheit, Zugangskontrolle, Asset-Management | Art. 21(2)(i) | A.5.9–5.18, A.6.1–6.5, A.8.2–8.3 | Kongruent |
| MFA und gesicherte Kommunikation | Art. 21(2)(j) | A.5.14, A.8.5, A.8.20 | **NIS2-spezifisch:** Präskriptive MFA-Anforderung |
| Vorfallmeldung an Behörden | Art. 23 | A.5.5, A.5.26 | **NIS2-spezifisch:** Vorgeschriebene Fristen |
| Verantwortung des Leitungsorgans | Art. 21(3) | Klausel 5.1–5.2 | **NIS2-spezifisch:** Persönliche Haftung |

## Wesentliche Lücken zwischen ISO 27001:2022 und NIS2

**Lücke 1: Regulatorische Vorfallmeldung mit Fristen**

- ISO 27001: Internes Incident-Management, optionaler Behördenkontakt
- NIS2: Pflichtmeldung an nationales CSIRT/Behörde innerhalb von 24/72 Stunden

**Lücke 2: Präskriptive MFA-Anforderung**

- ISO 27001: Sichere Authentifizierung (Methode flexibel)
- NIS2: Explizite Multi-Faktor-Authentifizierungs-Anforderung

**Lücke 3: Managementhaftung**

- ISO 27001: Keine gesetzlichen Haftungsbestimmungen
- NIS2: Leitungsorgan kann haftbar gemacht werden, einschließlich persönlicher Sanktionen

**Lücke 4: Durchsetzung und Sanktionen**

- ISO 27001: Aussetzung/Entzug der Zertifizierung
- NIS2: Erhebliche finanzielle Sanktionen (bis zu €10 Mio. oder 2 % des Umsatzes)

## NIS2-Compliance auf ISO-27001-Grundlage

**Kernaussage:**
Die ISO-27001:2022-Zertifizierung bietet eine starke Grundlage für NIS2-Compliance. Die Hauptlücken sind:
1. Vorfallmeldeprozess und -fristen
2. MFA-Umsetzungsvalidierung
3. Leitungsorganaufsicht und Haftungsrahmen
4. Nationale Registrierung und Aufsicht

Organisationen mit ISO 27001 benötigen typischerweise **10–20 % zusätzlichen Aufwand** zur Erreichung der NIS2-Compliance, vor allem beim Incident-Reporting-System und der Management-Governance.

---

# Umsetzungsüberlegungen

## NIS2-Compliance-Zeitplan

**Wenn [Organisation] eine NIS2-regulierte Einrichtung ist:**

**Vor Anwendung (bevor nationales Recht in Kraft tritt):**

- NIS2-Anwendbarkeitsstatus bestätigen
- Lückenanalyse gegenüber Artikel-21-Maßnahmen
- Incident-Meldeprozess einrichten
- Information und Genehmigung des Leitungsorgans

**0–6 Monate (Erstüberprüfungszeitraum):**

- Zwingend vorgeschriebene Cybersicherheitsmaßnahmen umsetzen
- Incident-Meldefähigkeit etablieren
- Bei nationaler zuständiger Behörde registrieren (falls erforderlich)
- Lieferkettensicherheitsbewertungen

**6–12 Monate (Reifephase):**

- Tests und Validierung aller Maßnahmen
- Aufsichtsmechanismen des Leitungsorgans
- Incident-Meldung testen
- Erste jährliche Überprüfung und Bewertung

**Laufend:**

- Kontinuierliche Überwachung und Verbesserung
- Jährliche Wirksamkeitsbewertung
- Vorfallmeldung (bei Vorfällen)
- Managementbewertungen und Vorstandsberichte

## Ressourcenanforderungen

**Personal:**

- Cybersicherheitsfunktion mit definierten Verantwortlichkeiten
- Incident-Response-Team
- Spezialisten für Lieferkettensicherheit
- Compliance- und Meldefunktion
- Einbindung des Leitungsorgans (Schulung und Aufsicht)

**Technologie:**

- MFA-Infrastruktur (unternehmensweit)
- Incident-Erkennungs- und Response-Tools (SIEM, EDR)
- Backup- und Disaster-Recovery-Infrastruktur
- Verschlüsselte Kommunikationsplattformen
- Schwachstellenmanagement-Tools

**Externe Unterstützung:**

- Rechtsberatung mit NIS2-Kenntnissen (mitgliedstaatsspezifisch)
- Externe Prüfer für Wirksamkeitsbewertung
- Incident-Response-Retainer (DFIR-Dienste)
- Managed Security Service Provider (MSSP) bei Bedarf

## Kostenfolgen

NIS2-Compliance erfordert typischerweise:

- Erweiterte technische Kontrollen (MFA, Verschlüsselung, Überwachung)
- Incident-Reporting-Infrastruktur
- Lieferkettensicherheitsprogramm
- Management-Aufsichtsrahmen
- Schulungs- und Sensibilisierungsprogramme

Geschätzte Mehrkosten: **10–25 % Aufschlag** über die Basis-ISO-27001-Compliance für mittelgroße Einrichtungen.

**Sanktionsrisiko:**
Sanktionen bei Nichteinhaltung können erheblich sein (€7–10 Mio. oder 1,4–2 % des Umsatzes), wodurch Compliance-Investitionen zur kosteneffektiven Risikominderung werden.

---

# Häufige Fallstricke und Erfahrungswerte

## Häufige NIS2-Compliance-Herausforderungen

**Herausforderung 1: Anwendbarkeit bestimmen**

- Einrichtungsklassifizierung (wesentlich vs. wichtig) kann mehrdeutig sein
- Größenschwellen auf Konzern- vs. Tochtergesellschaftsebene
- Nationale Umsetzungsvariationen in den Mitgliedstaaten
- Alleinanbieter-Bestimmungen

**Herausforderung 2: Vorfallmeldeprozess**

- 24-Stunden-Frühwarnung ist sehr knappe Frist
- Incident-Klassifizierungskriterien erfordern Beurteilung
- Koordination mit bestehenden Meldepflichten (GDPR, sektorspezifisch)
- Meldeprozess vor echten Vorfällen testen

**Herausforderung 3: Einbindung des Leitungsorgans**

- Vorstandsmitglieder können Cybersicherheitskenntnisse fehlen
- Haftungsbedenken erfordern klaren Governance-Rahmen
- Schulung und Sensibilisierung für nicht-technische Führungskräfte
- Balance zwischen Aufsicht und operativer Delegation

**Herausforderung 4: Komplexität der Lieferkette**

- Große Anzahl zu bewertender Lieferanten
- Begrenzter Einfluss bei Hauptlieferanten (z. B. Cloud-Anbieter)
- Transparenzherausforderungen bei Unterauftragnehmern
- Balance zwischen Sicherheit und operativer Effizienz

**Herausforderung 5: MFA-Implementierung im Maßstab**

- Legacy-Systeme unterstützen möglicherweise keine MFA
- Herausforderungen bei Nutzererfahrung und -akzeptanz
- Kosten der MFA-Infrastruktur für alle Benutzer
- Ausnahmen und kompensatorische Kontrollen bei technischen Einschränkungen

## Bestpraktiken

**Praktik 1:** Nationale zuständige Behörde frühzeitig zu Anwendbarkeitsfragen konsultieren
**Praktik 2:** ISO 27001 als Grundlage nutzen und NIS2-spezifische Anforderungen ergänzen
**Praktik 3:** Incident-Meldungsinfrastruktur einrichten und quartalsweise testen
**Praktik 4:** MFA unternehmensweit implementieren (nicht nur für NIS2-Compliance)
**Praktik 5:** NIS2 in bestehende ERM- und Compliance-Programme integrieren
**Praktik 6:** Vorstand regelmäßig zu Cybersicherheit schulen und berichten
**Praktik 7:** Verhältnismäßigkeitsbegründungen für risikobasierte Entscheidungen dokumentieren

---

# Referenzen und Ressourcen

## NIS2-Rechtstexte

**Primäre Richtlinie:**

- Richtlinie (EU) 2022/2555 (NIS2-Richtlinie) — Amtsblatt der EU

**Durchführungsrechtsakte und Leitlinien:**

- Durchführungsverordnung der Kommission zur Vorfallmeldung (erwartet 2024–2025)
- ENISA-Leitlinien zur NIS2-Umsetzung
- Nationale Umsetzungsgesetze (variiert je nach Mitgliedstaat)

**EU-Agenturen:**

- **ENISA** (Agentur der Europäischen Union für Cybersicherheit): https://www.enisa.europa.eu/
- NIS2-spezifische Seiten und Umsetzungsunterstützung

## Nationale zuständige Behörden

Organisationen müssen ihre **nationale Cybersicherheitsbehörde** konsultieren für:

- Spezifikationen des nationalen Umsetzungsgesetzes
- Registrierungsanforderungen
- Vorfallmeldeverfahren
- Aufsichtserwartungen

**Beispiele nationaler Behörden:**

- **Deutschland:** BSI (Bundesamt für Sicherheit in der Informationstechnik)
- **Frankreich:** ANSSI (Agence nationale de la sécurité des systèmes d'information)
- **Niederlande:** NCSC (National Cyber Security Centrum)
- **Italien:** ACN (Agenzia per la Cybersicurezza Nazionale)
- **Spanien:** CCN-CERT (Centro Criptológico Nacional)
- **Polen:** NASK (Naukowa i Akademicka Sieć Komputerowa)

## Verwandte Standards und Rahmenwerke

**ISO-Standards:**

- ISO/IEC 27001:2022: Informationssicherheitsmanagementsysteme
- ISO/IEC 27002:2022: Informationssicherheitskontrollen
- ISO/IEC 27005:2022: Informationssicherheits-Risikomanagement
- ISO 22301:2019: Managementsysteme für Betriebskontinuität

**NIST-Publikationen** (informative Referenz):

- NIST Cybersecurity Framework (CSF)
- NIST SP 800-53: Sicherheits- und Datenschutzkontrollen

**Branchenhinweise:**

- ENISA NIS2 Leitlinien und Bestpraktiken
- Nationale CSIRT-Incident-Handling-Leitfäden
- Sektorspezifische Hinweise (variiert je nach Branche)

## Compliance-Ressourcen

NIS2-pflichtige Organisationen sollten einbinden:

- Rechtsberatung mit Kenntnissen im EU-Cybersicherheitsrecht
- Prüfer mit NIS2-Compliance-Erfahrung
- Cybersicherheitsberater mit Kenntnissen der nationalen Umsetzung
- Nationale zuständige Behörde für Klärungen

---

# Anhang A: NIS2 Compliance-Selbstbewertungs-Checkliste

## Anwendbarkeitsbestimmung

| Kriterium | Status | Bemerkungen |
|-----------|--------|-------------|
| Einrichtung tätig in EU-Mitgliedstaat | ⬜ Ja ⬜ Nein | [Land/Länder angeben] |
| Einrichtung gehört zu Anhang-I- oder -II-Sektoren | ⬜ Ja (Anhang I) ⬜ Ja (Anhang II) ⬜ Nein | [Sektor angeben] |
| Einrichtung erfüllt Größenschwellen (≥50 Mitarbeitende) | ⬜ Ja ⬜ Nein | [Mitarbeitende: ___ / Umsatz: ___] |
| Einrichtung von nationaler Behörde bestimmt | ⬜ Ja ⬜ Nein ⬜ Unbekannt | |
| Nationales Umsetzungsgesetz in Kraft | ⬜ Ja ⬜ Nein ⬜ Ausstehend | [Nationales Gesetz] |

**Gesamte NIS2-Anwendbarkeit:** ⬜ Wesentliche Einrichtung ⬜ Wichtige Einrichtung ⬜ Nicht anwendbar

---

## Artikel 21(2) — Cybersicherheits-Risikomanagementmaßnahmen

| Massnahme | Status | Nachweis-Speicherort | Bemerkungen |
|-----------|--------|----------------------|-------------|
| (a) Risikoanalyse und Sicherheitsrichtlinien | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| (b) Incident-Handhabungsverfahren | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| (c) Betriebskontinuität und Krisenmanagement | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| (d) Lieferkettensicherheitsmaßnahmen | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| (e) Sicherheit bei Erwerb, Entwicklung, Wartung | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| (f) Wirksamkeitsbewertungsverfahren | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| (g) Grundlegende Cyber-Hygiene und Schulung | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| (h) Kryptographie und Verschlüsselung | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| (i) Personalsicherheit, Zugangskontrolle, Asset-Management | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| (j) MFA, gesicherte Kommunikation, Notfallkommunikation | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |

---

## Artikel 21(3) — Verantwortung des Leitungsorgans

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| Genehmigung der Risikomanagementmaßnahmen durch Leitungsorgan | ⬜ Ja ⬜ Nein | | |
| Überwachung der Umsetzung durch Leitungsorgan | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Cybersicherheitsschulung für Leitungsorganmitglieder | ⬜ Ja ⬜ Nein ⬜ Geplant | | |
| Regelmäßige Cybersicherheitsberichterstattung an Leitungsorgan | ⬜ Ja ⬜ Nein | | |

---

## Artikel 23 — Vorfallmeldung

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| Incident-Klassifizierungskriterien definiert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Vorfallmeldeprozess an CSIRT/Behörde | ⬜ Ja ⬜ Nein | | |
| Frühwarnfähigkeit (24 Stunden) | ⬜ Ja ⬜ Nein | | |
| Vorfallmeldefähigkeit (72 Stunden) | ⬜ Ja ⬜ Nein | | |
| Abschlussberichtsfähigkeit (1 Monat) | ⬜ Ja ⬜ Nein | | |
| Vorfallmeldungstests durchgeführt | ⬜ Ja ⬜ Nein ⬜ Geplant | | |
| Kontakt zu CSIRT/Behörde hergestellt | ⬜ Ja ⬜ Nein | | |

---

## Registrierung und Aufsicht

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| Bei nationaler zuständiger Behörde registriert (falls erforderlich) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Ansprechpartner bestimmt | ⬜ Ja ⬜ Nein | | |
| Auf Aufsichtsprüfungen vorbereitet | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |

---

# Anhang B: Vorfallmeldevorlage (NIS2)

**NIS2 Meldung eines erheblichen Vorfalls**

**An:** [Nationales CSIRT / Zuständige Behörde]
**Von:** [Name der Einrichtung]
**Kontakt:** [Name Incident-Response-Manager, Telefon, E-Mail]
**Datum/Uhrzeit:** [ISO 8601 Format]
**Einrichtungsklassifizierung:** ⬜ Wesentlich (Anhang I) ⬜ Wichtig (Anhang II)
**Sektor:** [Sektor gemäß Anhang I oder II angeben]
**Meldungstyp:** ⬜ Frühwarnung ⬜ Vorfallmeldung ⬜ Abschlussbericht ⬜ Zwischenbericht

---

## ABSCHNITT 1: VORFALLZUSAMMENFASSUNG

**Vorfall-ID:** [Interne Referenznummer]
**Kenntnisnahme Datum/Uhrzeit:** [Wann die Einrichtung Kenntnis erlangte — ISO 8601]
**Vorfall-Startdatum/-uhrzeit** (geschätzt): [ISO 8601]
**Aktueller Status:** ⬜ Laufend ⬜ Eingedämmt ⬜ Gelöst

**Vorfalltyp:**
⬜ Cyberangriff (näher angeben: Ransomware, DDoS, Malware, Phishing, Datenverletzung, usw.)
⬜ Systemausfall (näher angeben: Hardware, Software, Netzwerk, Strom)
⬜ Problem mit Drittanbieter
⬜ Naturkatastrophe
⬜ Menschlicher Fehler
⬜ Sonstiges (näher angeben): _____________

---

## ABSCHNITT 2: ERHEBLICHKEITSBEWERTUNG

**Warum ist dieser Vorfall erheblich?** (Alle Zutreffenden ankreuzen):
⬜ Hat schwerwiegende Betriebsstörung des wesentlichen Dienstes verursacht/wird wahrscheinlich verursachen
⬜ Hat erheblichen finanziellen Verlust verursacht/wird wahrscheinlich verursachen
⬜ Hat andere natürliche oder juristische Personen betroffen/wird wahrscheinlich betreffen (Kunden, Partner, Öffentlichkeit)

**Dienstauswirkung:**

- **Dauer der Störung:** [Stunden/Minuten]
- **Anzahl betroffener Nutzer/Kunden:** [Schätzung]
- **Geografischer Umfang:** [Betroffene Länder/Regionen]
- **Betroffene wesentliche Dienste:** [Liste]

---

## ABSCHNITT 3: GRENZÜBERSCHREITENDE AUSWIRKUNG

**Wird grenzüberschreitende Auswirkung vermutet?**
⬜ Ja ⬜ Nein ⬜ Unbekannt

**Falls Ja:**

- **Betroffene Länder:** [Liste]
- **Art der grenzüberschreitenden Auswirkung:** [Beschreibung]

---

## ABSCHNITT 4: BEWERTUNG BÖSWILLIGER HANDLUNG

**Wird vermutet, dass der Vorfall das Ergebnis einer rechtswidrigen oder böswilligen Handlung ist?**
⬜ Ja ⬜ Nein ⬜ Unbekannt

**Falls Ja:**

- **Art der Bedrohung:** [z. B. Ransomware, APT, Insider-Bedrohung]
- **Kompromittierungsindikatoren (IOCs):** [Liste falls verfügbar]

---

## ABSCHNITT 5: TECHNISCHE DETAILS (Für Vorfallmeldung & Abschlussbericht)

**Ursache** (falls bekannt):
[Beschreibung]

**Angriffsvektor** (falls zutreffend):
⬜ Phishing/Social Engineering
⬜ Ausnutzung von Schwachstellen
⬜ Brute Force / Credential Stuffing
⬜ Lieferkettenkompromittierung
⬜ Insider-Bedrohung
⬜ Sonstiges: _____________

**Betroffene Systeme:**

- [System 1]: [Auswirkung]
- [System 2]: [Auswirkung]

---

## ABSCHNITT 6: REAKTIONSMASSNAHMEN

**Ergriffene Abhilfemassnahmen:**
1. [Massnahme 1 — Zeitstempel]
2. [Massnahme 2 — Zeitstempel]
3. [Massnahme 3 — Zeitstempel]

**Laufende Reaktion:**
[Beschreibung der aktuellen Reaktionsaktivitäten]

**Geschätzte Wiederherstellungszeit:** [Falls bekannt]

---

## ABSCHNITT 7: FOLGENABSCHÄTZUNG (Für Abschlussbericht)

**Operative Auswirkung:**

- **Serviceausfallzeit:** [Gesamtstunden]
- **Zeitraum eingeschränkter Dienste:** [Stunden]
- **Anzahl betroffener Nutzer:** [Endauswertung]

**Finanzielle Auswirkung:**
⬜ Noch nicht quantifiziert
⬜ Geschätzt: [Betrag und Grundlage]
⬜ Keine wesentliche finanzielle Auswirkung

**Datenauswirkung:**
⬜ Keine Daten betroffen
⬜ Daten möglicherweise kompromittiert: [Typ, Menge]
⬜ Daten bestätigt kompromittiert: [Details]

**Reputationsauswirkung:**
⬜ Gering ⬜ Mittel ⬜ Hoch
[Beschreibung]

---

## ABSCHNITT 8: LESSONS LEARNED (Für Abschlussbericht)

**Zusammenfassung der Ursachenanalyse:**
[Detaillierte Ursache]

**Beitragende Faktoren:**
[Faktoren, die den Vorfall ermöglicht oder verschlimmert haben]

**Abhilfemassnahmen:**
1. [Massnahme zur Vermeidung von Wiederholungen]
2. [Massnahme zur Verbesserung der Erkennung]
3. [Massnahme zur Verbesserung der Reaktion]

**Zeitplan für Abhilfemassnahmen:** [Abschlussdaten]

---

## ABSCHNITT 9: EXTERNE KOORDINATION

**Benachrichtigte weitere Behörden:**
⬜ Datenschutzbehörde (GDPR-Verletzung): [Datum]
⬜ Strafverfolgungsbehörden: [Welche Behörde, Datum]
⬜ Andere Regulatoren: [Angabe]

**Öffentliche Kommunikation:**
⬜ Ja ⬜ Nein ⬜ Geplant
[Falls ja, Umfang und Zeitplan beschreiben]

---

## ABSCHNITT 10: NÄCHSTE SCHRITTE

**Nächster Berichtstyp:** ⬜ Zwischenbericht ⬜ Abschlussbericht ⬜ Kein weiterer erwartet
**Nächster Bericht fällig:** [Datum/Uhrzeit falls zutreffend]

---

**ERKLÄRUNG**

Ich bestätige, dass die in dieser Meldung gemachten Angaben nach bestem Wissen und Gewissen zum Stand [Datum/Uhrzeit] korrekt sind.

**Name:** [Bevollmächtigter Vertreter]
**Titel:** [Titel]
**Unterschrift:** [Digitale Signatur falls zutreffend]

---

**ENDE DER TECHNISCHEN REFERENZ**

---

*Diese technische Referenz unterstützt potenzielle NIS2-Compliance-Anforderungen gemäß ISMS-POL-00. Alle Feststellungen zur regulatorischen Anwendbarkeit und verbindlichen Anforderungen sind in ISMS-POL-00 und genehmigten ISMS-Richtliniendokumenten definiert.*

*Für Organisationen, die NICHT NIS2-pflichtig sind, dient dieses Dokument ausschließlich der informativen Sensibilisierung und begründet KEINE Compliance-Pflichten.*

<!-- QA_VERIFIED: 2026-03-28 -->
