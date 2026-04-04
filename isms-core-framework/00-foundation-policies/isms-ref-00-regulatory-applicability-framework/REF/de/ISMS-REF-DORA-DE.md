<!-- ISMS-CORE:REF:ISMS-REF-DORA-DE:framework:REF:dora -->
**ISMS-REF-DORA-DE — Digital Operational Resilience Act (DORA) Anforderungsreferenz**
**EU-Anforderungen an die digitale Betriebsstabilität des Finanzsektors (Nicht-ISMS-Technische Referenz)**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | DORA Anforderungsreferenz |
| **Dokumententyp** | Intern — Technische Referenz (nicht ISMS) |
| **Dokumenten-ID** | ISMS-REF-DORA-DE |
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
| 1.0 | [Datum] | ISB / Rechts-/Compliance-Abteilung | Erste technische Referenz für EU-Finanzeinrichtungen |

**Überprüfungszyklus:** Jährlich (oder bei Aktualisierungen der technischen Regulierungsstandards zu DORA)
**Nächstes Überprüfungsdatum:** [Datum + 12 Monate]
**Genehmigende:** Rechts-/Compliance-Abteilung / ISB (technische Referenz, keine ISMS-Genehmigung erforderlich)

**Verbreitung:** Compliance-Team, ISB, Rechtsberatung (für DORA-regulierte Organisationen)

---

⚠️ **WICHTIG – NICHT-ISMS TECHNISCHES UNTERSTÜTZUNGSDOKUMENT**

Dieses Dokument dient ausschließlich Informations- und Sensibilisierungszwecken.

- Dieses Dokument ist KEIN Teil des Informationssicherheitsmanagementsystems (ISMS).
- Dieses Dokument definiert KEINE zwingenden Anforderungen, außer wenn [Organisation] eine DORA-regulierte Einrichtung ist.
- Dieses Dokument begründet KEINE verbindlichen Anforderungen, Fristen, KPIs oder SLAs für nicht regulierte Unternehmen.
- Dieses Dokument schreibt die Übernahme von DORA-Anforderungen für nicht DORA-pflichtige Organisationen NICHT vor.
- Dieses Dokument überschreibt oder erweitert keine ISMS-Richtlinie.

**Anwendbarkeitsbestimmung:**
DORA-Anforderungen gelten NUR, wenn [Organisation]:

- Ein in der EU tätiges Finanzunternehmen ist (Banken, Zahlungsinstitute, Wertpapierfirmen, Kryptowertedienstleister, Versicherungen usw.)
- Als kritischer oder wichtiger IKT-Drittdienstleister für EU-Finanzeinrichtungen eingestuft ist
- Vertragliche Pflichten zur Erfüllung von DORA-Anforderungen hat

Für alle anderen Organisationen dient dieses Dokument ausschließlich als:

- Technische Referenz für potenzielle DORA-Anforderungen
- Kontext für Dienstleisterbeziehungen mit EU-Finanzeinrichtungen
- Sensibilisierung für EU-Finanzsektor-Standards zur digitalen Betriebsstabilität
- **Dieses Dokument darf nicht als Audit-Nachweis verwendet werden, außer wenn [Organisation] DORA-reguliert ist**

Die Verwendung dieses Dokuments impliziert keine DORA-Anwendbarkeit, Compliance-Pflichten oder Regulierungsstatus.

**Wesentlicher Positionierungshinweis:**
Dieses Dokument enthält absichtlich regulatorische Details, die über das für die meisten Organisationen Zutreffende hinausgehen. Sein Zweck ist ausschließlich die Sensibilisierung von Organisationen, die möglicherweise DORA-pflichtig werden könnten, oder die IKT-Dienstleistungen für DORA-regulierte Finanzeinrichtungen erbringen. Aus dem Vorhandensein, dem Fehlen oder dem Umsetzungsstatus eines hier aufgeführten DORA-Requirements dürfen keine Audit-Schlussfolgerungen gezogen werden, außer wenn [Organisation] explizit DORA-reguliert ist.

---

# Dokumentenzweck und Geltungsbereich

## Zweck

Dieses Dokument gibt einen technischen Überblick über die Anforderungen des Digital Operational Resilience Act (Verordnung (EU) 2022/2554) für EU-Finanzsektor-Einrichtungen. Es soll unterstützen bei:

- Sensibilisierung für DORA-Anforderungen für EU-Finanzeinrichtungen
- Verständnis der fünf DORA-Säulen (IKT-Risikomanagement, Incident-Meldung, Tests, Drittparteien-Risiko, Informationsaustausch)
- Kontext für IKT-Dienstleister für EU-Finanzeinrichtungen
- Zukünftige Anwendbarkeitsbeurteilung
- Zuordnung von DORA-Anforderungen zu ISO 27001:2022 Kontrollen

## Was dieses Dokument NICHT ist

Dieses Dokument:

- Begründet KEINE zwingenden Anforderungen für nicht DORA-regulierte Organisationen
- Definiert NICHT die Compliance-Pflichten von [Organisation] (siehe POL-00 für regulatorische Anwendbarkeit)
- Schafft KEINE Audit-Kriterien, außer wenn [Organisation] DORA-reguliert ist
- Ersetzt KEINE Interpretation durch Rechts- oder Compliance-Beratung
- Stellt KEINE Rechtsberatung zur DORA-Compliance dar
- Begründet KEINE Umsetzungsverfahren oder Verifikationsprozesse
- Deckt technische Regulierungsstandards (RTS) NICHT erschöpfend ab

## Beziehung zum ISMS

Dieses Dokument ist eine **unverbindliche technische Referenz**, AUSSER wenn [Organisation] DORA-pflichtig ist (wie in ISMS-POL-00 Abschnitt 3.2 festgestellt).

**Wenn [Organisation] DORA-reguliert IST:**

- DORA-Anforderungen werden gemäß POL-00 zu Stufe 1 (Zwingend)
- Dieses Dokument liefert Umsetzungshinweise
- ISMS-Kontrollen müssen DORA-Compliance nachweisen
- Compliance-Bescheinigung erforderlich (aufsichtsrechtliche Berichterstattung)

**Wenn [Organisation] NICHT DORA-reguliert ist:**

- DORA bleibt gemäß POL-00 bei Stufe 3 (Informativ)
- Dieses Dokument dient ausschließlich der Sensibilisierung
- Keine DORA-Compliance-Pflichten
- ISMS-Kontrollen folgen ausschließlich ISO 27001:2022

**Wenn [Organisation] IKT-Dienstleistungen für DORA-Finanzeinrichtungen erbringt:**

- Kann als kritischer oder wichtiger Drittdienstleister eingestuft werden
- DORA-Überwachungsrahmen kann gelten (Kapitel V, Abschnitt II)
- Vertragliche Anforderungen werden wahrscheinlich DORA-Standards referenzieren
- Als Stufe 2 (Bedingt) bis zur Einstufung betrachten

## Inhaltsorganisation

Diese Referenz organisiert DORA-Anforderungen nach:

- Fünf-Säulen-Struktur (Kapitel II–VI von DORA)
- IKT-Risikomanagement-Rahmen (Kapitel II)
- Incident-Meldung (Kapitel III)
- Tests der digitalen Betriebsstabilität (Kapitel IV)
- IKT-Drittparteien-Risikomanagement (Kapitel V)
- Informationsaustauschvereinbarungen (Kapitel VI)
- Zuordnung zu ISO 27001:2022 Annex-A-Kontrollen

---

# DORA — Überblick und Anwendbarkeit

## Was ist DORA?

**Verordnung (EU) 2022/2554** über die digitale operationale Resilienz des Finanzsektors trat am 16. Januar 2023 in Kraft mit Geltung ab dem **17. Januar 2025**.

**Zweck:** Einheitliche Anforderungen für die digitale Betriebsstabilität im EU-Finanzsektor festlegen, um folgende Aspekte zu adressieren:

- Fragmentierte nationale Ansätze zum IKT-Risiko
- Zunehmende Cyberbedrohungen und IKT-Störungen
- Konzentrationsrisiko bei IKT-Drittdienstleistern
- Notwendigkeit harmonisierter Incident-Meldung
- Bedeutung des Austauschs von Bedrohungsinformationen

**Rechtsgrundlage:** EU-Verordnung (in allen Mitgliedstaaten direkt anwendbar, keine nationale Umsetzung erforderlich)

**Aufsichtsbehörde:** Europäische Aufsichtsbehörden (ESAs):

- Europäische Bankenaufsichtsbehörde (EBA)
- Europäische Wertpapier- und Marktaufsichtsbehörde (ESMA)
- Europäische Aufsichtsbehörde für das Versicherungswesen und die betriebliche Altersversorgung (EIOPA)
- Zusätzlich nationale zuständige Behörden

## Wer muss DORA einhalten?

**Finanzunternehmen** (Artikel 2):

| Kategorie | Beispiele | Aufsichtsbehörde |
|-----------|-----------|-----------------|
| **Kreditinstitute** | Banken | EBA + Nationale Behörde |
| **Zahlungsinstitute** | Zahlungsdienstleister | EBA + Nationale Behörde |
| **E-Geld-Institute** | E-Geld-Ausgeber | EBA + Nationale Behörde |
| **Wertpapierfirmen** | Broker, Portfolioverwalter | ESMA + Nationale Behörde |
| **Kryptowertedienstleister** | Kryptobörsen, Verwahrer | ESMA + Nationale Behörde |
| **Zentralverwahrer** | CSDs | ESMA + Nationale Behörde |
| **Handelsplätze** | Börsen, MTFs | ESMA + Nationale Behörde |
| **Transaktionsregister** | Transaktionsmeldung | ESMA + Nationale Behörde |
| **Verwalter alternativer Investmentfonds** | Hedgefonds, PE-Fonds | ESMA + Nationale Behörde |
| **Verwaltungsgesellschaften** | OGAW-Verwaltungsgesellschaften | ESMA + Nationale Behörde |
| **Datenbereitstellungsdienstleister** | Zugelassene Meldeanordnungen | ESMA + Nationale Behörde |
| **Versicherungs- und Rückversicherungsunternehmen** | Versicherer, Rückversicherer | EIOPA + Nationale Behörde |
| **Versicherungsvermittler** | Versicherungsmakler | EIOPA + Nationale Behörde |
| **Einrichtungen der betrieblichen Altersversorgung** | Pensionsfonds | EIOPA + Nationale Behörde |
| **Ratingagenturen** | Ratingagenturen | ESMA |
| **Verwalter kritischer Referenzwerte** | Referenzwertanbieter | ESMA |
| **Crowdfunding-Dienstleistungsanbieter** | Crowdfunding-Plattformen | ESMA + Nationale Behörde |
| **Verbriefungsregister** | Verbriefungsmeldung | ESMA + Nationale Behörde |

**IKT-Drittdienstleister** (Kapitel V, Abschnitt II):

- Cloud-Computing-Dienstleister
- Softwareanbieter
- Datenanbieter
- Rechenzentrumsbetreiber
- **Bei Einstufung als „kritisch":** Unterliegen dem DORA-Überwachungsrahmen
- **Bei Einstufung als „wichtig":** Erweiterte vertragliche Anforderungen

## Anwendbarkeitsbestimmung

**DORA gilt für [Organisation], WENN:**

| Kriterium | Status | Nachweis |
|-----------|--------|----------|
| In der EU tätiges Finanzunternehmen | ⬜ Ja ⬜ Nein | [Lizenztyp / Land] |
| EU-Bank oder Kreditinstitut | ⬜ Ja ⬜ Nein | [Banklizenz] |
| EU-Zahlungs- oder E-Geld-Institut | ⬜ Ja ⬜ Nein | [Zahlungslizenz] |
| EU-Wertpapierfirma | ⬜ Ja ⬜ Nein | [Investitionslizenz] |
| EU-Kryptowertedienstleister | ⬜ Ja ⬜ Nein | [MiCAR-Lizenz] |
| EU-Versicherungs- oder Rückversicherungsunternehmen | ⬜ Ja ⬜ Nein | [Versicherungslizenz] |
| Andere Finanzeinrichtung gemäß Artikel 2 | ⬜ Ja ⬜ Nein | [Typ angeben] |
| Kritischer IKT-Drittdienstleister | ⬜ Ja ⬜ Nein ⬜ Ausstehend | [Einstufungsschreiben] |

**Bei EINEM „Ja":** DORA-Anforderungen sind gemäß POL-00 Abschnitt 3.2 **Stufe 1 (Zwingend)**

**Bei ALLEN „Nein":** DORA-Anforderungen bleiben gemäß POL-00 **Stufe 3 (Informativ)**

**Bewertung als IKT-Dienstleister:**
Wenn [Organisation] IKT-Dienstleistungen für EU-Finanzeinrichtungen erbringt:

- Potenzielle Einstufung als kritischer Drittdienstleister überwachen
- Kundenverträge auf DORA-referenzierte Anforderungen prüfen
- Beurteilen, ob Dienste „kritische oder wichtige Funktionen" gemäß DORA Artikel 3(31)-(32) sind
- Kritische Einstufung löst DORA-Überwachungsrahmen aus (Artikel 31–44)

---

# DORA — Überblick über die fünf Säulen

## Säulenstruktur

DORA organisiert Anforderungen in fünf Säulen:

```
┌─────────────────────────────────────────────────────────────────┐
│                    DORA FÜNF SÄULEN                             │
├─────────────────────────────────────────────────────────────────┤
│  KAPITEL II:  IKT-Risikomanagement-Rahmen                       │
│               Artikel 5–16                                       │
│               - Governance und Strategie                         │
│               - IKT-Risiko: Identifikation, Schutz, Erkennung   │
│               - Reaktion und Wiederherstellung                   │
│               - Lernen und Weiterentwickeln                      │
│               - Kommunikation                                    │
├─────────────────────────────────────────────────────────────────┤
│  KAPITEL III: IKT-bezogenes Incident-Management & Meldung       │
│               Artikel 17–23                                      │
│               - Incident-Erkennung und -Klassifizierung          │
│               - Incident-Response-Verfahren                      │
│               - Meldung an zuständige Behörden                   │
├─────────────────────────────────────────────────────────────────┤
│  KAPITEL IV:  Tests der digitalen Betriebsstabilität            │
│               Artikel 24–27                                      │
│               - Testprogramme                                    │
│               - Erweiterte Tests (TLPT)                          │
│               - Verhältnismäßigkeitsprinzip                      │
├─────────────────────────────────────────────────────────────────┤
│  KAPITEL V:   IKT-Drittparteien-Risikomanagement               │
│               Artikel 28–44                                      │
│               - Drittparteien-Risikorahmen                       │
│               - Vertragliche Anforderungen                       │
│               - Aufsicht über kritische Anbieter                 │
├─────────────────────────────────────────────────────────────────┤
│  KAPITEL VI:  Informationsaustauschvereinbarungen               │
│               Artikel 45                                         │
│               - Austausch von Bedrohungsinformationen            │
└─────────────────────────────────────────────────────────────────┘
```

## Verhältnismäßigkeitsprinzip

DORA wendet Verhältnismäßigkeit an (Artikel 4):

- Anforderungen skalieren basierend auf:
  - Größe der Finanzeinrichtung
  - Art, Umfang und Komplexität der Aktivitäten
  - Gesamtrisikoprofil
- **Kleine und nicht miteinander verflochtene Wertpapierfirmen:** Vereinfachtes Regime
- **Kleinstunternehmen:** Weitere Vereinfachungen, wo gerechtfertigt
- **Alle Finanzeinrichtungen:** Kernanforderungen gelten weiterhin

---

# Kapitel II — IKT-Risikomanagement-Rahmen

## Überblick (Artikel 5–16)

Finanzunternehmen müssen einen IKT-Risikomanagement-Rahmen einrichten, aufrechterhalten und überprüfen, der Resilienz, Kontinuität und Sicherheit der IKT-Systeme gewährleistet.

**Artikel 5: Governance und Organisation**

**Anforderungen:**

- Leitungsorgan letztverantwortlich für IKT-Risiko
- Genehmigung des IKT-Risikomanagement-Rahmens
- Zuweisung klarer Rollen und Verantwortlichkeiten
- Ausreichende Ressourcen für das IKT-Risikomanagement
- Interne Berichtswege zum Leitungsorgan

**Wichtige Rollen:**

- Leitungsorgan (Verantwortung auf Vorstandsebene)
- IKT-Risikomanagementfunktion (operative Verantwortung)
- Kontrollfunktionen (unabhängige Aufsicht)

**ISO 27001:2022 Zuordnung:**

- Klausel 5.1: Führung und Engagement
- Klausel 5.3: Organisatorische Rollen, Verantwortlichkeiten und Befugnisse
- A.5.1: Richtlinien für Informationssicherheit
- A.5.2: Rollen und Verantwortlichkeiten für Informationssicherheit

---

**Artikel 6: IKT-Risikomanagement-Rahmen**

**Anforderungen:**
Umfassender Rahmen, der Folgendes abdeckt:

- **Strategien, Richtlinien, Verfahren:** Dokumentierter IKT-Risikoansatz
- **IKT-Systeme und -Tools:** Inventar und Risikobewertung
- **IKT-Sicherheitsrichtlinien:** Schutzmaßnahmen
- **IKT-Kontinuitätsrichtlinien:** Betriebskontinuität und Disaster Recovery
- **IKT-Reaktions- und Wiederherstellungspläne:** Incident-Management
- **IKT-Tests:** Validierung von Kontrollen
- **IKT-Audit:** Unabhängige Gewissheit
- **IKT-Drittparteien-Risiko:** Lieferantenmanagement

**ISO 27001:2022 Zuordnung:**

- Klausel 4–10: Gesamter ISMS-Rahmen
- A.5.1: Richtlinien für Informationssicherheit
- A.5.8: Informationssicherheit im Projektmanagement
- A.5.9: Inventar von Informationen und anderen zugehörigen Werten
- A.8.13: Datensicherung
- A.5.29–5.30: Betriebskontinuität

---

**Artikel 8: Identifizierung**

**Anforderungen:**

- Umfassendes Inventar von IKT-Assets und Informationswerten
- Identifikation aller IKT-Risikoquellen (intern und extern)
- Risikobewertungsmethodik ausgerichtet an Geschäftskritikalität
- Dokumentation von Informationsverarbeitungsstandorten und Datenflüssen
- Identifikation von Legacy-IKT-Systemen und Risikobewertung

**ISO 27001:2022 Zuordnung:**

- A.5.9: Inventar von Informationen und anderen zugehörigen Werten
- A.5.12: Klassifizierung von Informationen
- Klausel 6.1.2: Informationssicherheits-Risikobewertung

**DORA-spezifische Anforderungen:**

- **Legacy-Systeme:** Explizite Identifizierung und kompensierende Kontrollen
- **Abhängigkeiten:** Zuordnung von Systemabhängigkeiten
- **Datenmapping:** Verarbeitungsstandorte und grenzüberschreitende Datenflüsse
- **Kritische Dienste:** Klassifizierung nach Geschäftsauswirkung

---

**Artikel 9: Schutz und Prävention**

**Anforderungen:**
IKT-Systemschutz durch:

- **Richtlinien, Verfahren, Protokolle:** Sicherheits-Baselines
- **IKT-Sicherheitstools:** Erkennungs- und Präventions­technologien
- **Verschlüsselung:** Datenschutz im Ruhezustand und bei der Übertragung
- **Netzwerksegmentierung:** Isolierung kritischer Funktionen
- **Zugangskontrolle:** Identity and Access Management
- **Physische Sicherheit:** Rechenzentrum und Infrastrukturschutz
- **Änderungsmanagement:** Kontrollierte Systemänderungen

**ISO 27001:2022 Zuordnung:**

- A.8.1: Benutzer-Endgeräte
- A.8.2–8.5: Zugangskontrolle
- A.8.7: Schutz vor Malware
- A.8.9: Konfigurationsmanagement
- A.8.18: Verwendung privilegierter Hilfsprogramme
- A.8.19: Installation von Software auf betrieblichen Systemen
- A.8.20: Netzwerksicherheit
- A.8.21: Sicherheit von Netzwerkdiensten
- A.8.22: Trennung von Netzwerken
- A.8.23: Web-Filterung
- A.8.24: Verwendung von Kryptographie
- A.7.4: Physische Sicherheitsüberwachung

**DORA-Schwerpunkte:**

- **Netzwerksegmentierung** ist explizit gefordert (nicht optional)
- **Verschlüsselung** zwingend für sensible Daten
- **Multi-Faktor-Authentifizierung** für privilegierten Zugang erwartet
- **Patching und Schwachstellenmanagement** sind kritische Anforderungen

---

**Artikel 10: Erkennung**

**Anforderungen:**

- Kontinuierliche Überwachungsmechanismen
- Erkennung anomaler Aktivitäten
- Echtzeit-Alarmierungsfähigkeiten
- Korrelation von Sicherheitsereignissen
- Integration von Bedrohungsinformationen

**ISO 27001:2022 Zuordnung:**

- A.8.15: Protokollierung
- A.8.16: Überwachungsaktivitäten
- A.5.24–5.25: Incident-Management-Planung
- A.5.7: Bedrohungsintelligenz

**Technologie-Beispiele:**

- SIEM (Security Information and Event Management)
- EDR (Endpoint Detection and Response)
- Netzwerkverkehrsanalyse (NTA)
- User and Entity Behavior Analytics (UEBA)
- Bedrohungsintelligenz-Plattformen (TIP)

---

**Artikel 11: Reaktion und Wiederherstellung**

**Anforderungen:**

- IKT-Incident-Response-Pläne
- Krisenmanagementverfahren
- Kommunikationspläne (intern und extern)
- Betriebskontinuitätspläne (BCP)
- Disaster-Recovery-Pläne (DRP)
- Recovery Time Objectives (RTO)
- Recovery Point Objectives (RPO)

**ISO 27001:2022 Zuordnung:**

- A.5.24–5.28: Incident-Management (vollständiger Zyklus)
- A.5.29: Informationssicherheit bei Störungen
- A.5.30: IKT-Bereitschaft für Betriebskontinuität
- A.8.13: Datensicherung
- A.8.14: Redundanz von Informationsverarbeitungseinrichtungen

**DORA-Erwartungen:**

- **RTO für kritische Funktionen:** Typischerweise 2–4 Stunden
- **RPO für kritische Daten:** Nahezu null (kontinuierliche Replikation bevorzugt)
- **Krisenkommunikation:** Interne und externe Stakeholder
- **Lessons Learned:** Post-Incident-Review zwingend

---

**Artikel 12: Lernen und Weiterentwickeln**

**Anforderungen:**

- Post-Incident-Reviews
- Ursachenanalyse
- Umsetzung von Korrekturmaßnahmen
- Integration von Lessons Learned
- Kontinuierliche Verbesserung des IKT-Risikorahmens
- Überwachung der Entwicklung der IKT-Risikolandschaft

**ISO 27001:2022 Zuordnung:**

- A.5.27: Lernen aus Informationssicherheitsvorfällen
- Klausel 10.1–10.2: Kontinuierliche Verbesserung

---

**Artikel 13: Kommunikation**

**Anforderungen:**

- Kommunikationskanäle zur Meldung von IKT-Problemen
- Eskalationsverfahren zum Management
- Informationsaustausch mit Stakeholdern
- Koordination mit IKT-Drittdienstleistern
- Externe Kommunikation bei Vorfällen

**ISO 27001:2022 Zuordnung:**

- A.5.5: Kontakt mit Behörden
- A.5.6: Kontakt mit besonderen Interessensgruppen
- A.6.8: Meldung von Informationssicherheitsereignissen

---

**Artikel 15: IKT-Sicherheitssensibilisierung und Schulungen**

**Anforderungen:**

- Regelmäßige IKT-Sicherheitssensibilisierungsprogramme
- Rollenbasierte Schulungen für IKT-Personal
- Phishing-Simulationen und Tests
- Messung der Schulungswirksamkeit
- Sensibilisierung für Social-Engineering-Bedrohungen

**ISO 27001:2022 Zuordnung:**

- A.6.3: Sensibilisierung, Aus- und Weiterbildung zur Informationssicherheit

**DORA-Schwerpunkte:**

- Schulungsprogramme müssen dokumentiert und messbar sein
- Mindestens jährliche Pflichtschulung
- Spezialisierte Schulungen für privilegierte Benutzer
- Phishing-Tests als Standardpraxis erwartet

---

**Artikel 16: IKT-bezogene Richtlinien**

**Anforderungen:**
Finanzunternehmen müssen IKT-bezogene Richtlinien einrichten, die folgende Bereiche abdecken:

- IKT-Sicherheit
- IKT-Kontinuität
- IKT-Änderungsmanagement
- IKT-Betrieb
- IKT-Projektmanagement
- Netzwerksicherheit
- Verschlüsselung und Schlüsselverwaltung

**Richtlinienüberprüfung:** Mindestens jährlich oder bei wesentlichen Änderungen

**ISO 27001:2022 Zuordnung:**

- A.5.1: Richtlinien für Informationssicherheit
- A.5.36: Einhaltung von Richtlinien, Regeln und Standards für Informationssicherheit

---

# Kapitel III — IKT-bezogenes Incident-Management & Meldung

## Überblick (Artikel 17–23)

Finanzunternehmen müssen über Prozesse zur Erkennung, Handhabung, Meldung und Berichterstattung von IKT-bezogenen Vorfällen verfügen.

**Artikel 17: IKT-bezogener Incident-Management-Prozess**

**Anforderungen:**

- Frühwarnindikatoren
- Incident-Erkennungsverfahren
- Incident-Klassifizierungskriterien (schwerwiegend vs. nicht schwerwiegend)
- Incident-Response- und Wiederherstellungsverfahren
- Ursachenanalyse
- Eskalationsverfahren
- Kommunikationspläne

**Incident-Klassifizierung** (Artikel 18):
Finanzunternehmen müssen Vorfälle klassifizieren basierend auf:

- **Kritikalität:** Auswirkung auf den Geschäftsbetrieb
- **Dauer:** Länge der Dienstunterbrechung
- **Datenverlust:** Menge und Sensibilität betroffener Daten
- **Geografische Ausbreitung:** Anzahl betroffener Länder/Kunden
- **Reputationsauswirkung:** Öffentliche Wahrnehmung und Vertrauen

**Indikatoren für schwerwiegende Vorfälle:**

- Erhebliche Störung kritischer Funktionen
- Dienstverfügbarkeit unter Schwellenwert (z. B. 2 Stunden)
- Datenverletzung mit Auswirkung auf eine große Anzahl von Kunden
- Erheblicher finanzieller Verlust
- Potenzielles systemisches Risiko für die Finanzstabilität

**ISO 27001:2022 Zuordnung:**

- A.5.24: Planung und Vorbereitung des Informationssicherheits-Incident-Managements
- A.5.25: Beurteilung und Entscheidung bei Informationssicherheitsereignissen
- A.5.26: Reaktion auf Informationssicherheitsvorfälle

---

**Artikel 19: Erstmeldung und Zwischenberichte**

**Anforderung:** Finanzunternehmen müssen zuständige Behörden über **schwerwiegende IKT-bezogene Vorfälle** gemäß definierten Fristen benachrichtigen.

**Meldefrist:**

| Phase | Frist | Inhalt |
|-------|-------|--------|
| **Erstmeldung** | So bald wie möglich, spätestens nach angegebenen Stunden (typischerweise 4 Stunden nach Erkennung) | Vorfallbeschreibung, Erkennungszeitpunkt, Status, vorläufige Auswirkung |
| **Zwischenbericht** | Auf Anfrage oder bei wesentlicher Statusänderung | Aktualisierte Beurteilung, ergriffene Maßnahmen, laufende Reaktion |
| **Abschlussbericht** | Nach Vorfallbehebung (z. B. innerhalb von 1 Monat) | Ursache, Folgenabschätzung, Behebung, Lessons Learned |

**Meldekanäle:**

- Portal der nationalen zuständigen Behörde
- Standardisierte Meldevorlagen (gemäß RTS)
- Sichere Kommunikationskanäle

**ISO 27001:2022 Zuordnung:**

- A.5.5: Kontakt mit Behörden
- A.5.26: Reaktion auf Informationssicherheitsvorfälle

**Parallele Meldungen:**
DORA-Meldepflichten können sich überschneiden mit:

- GDPR-Meldungen bei Verletzungen des Schutzes personenbezogener Daten (Artikel 33–34)
- NIS2-Incident-Meldung (falls Einrichtung auch NIS2-pflichtig ist)
- Nationalen Incident-Meldeanforderungen

Einrichtungen sollten Meldungen koordinieren, um Doppelarbeit und Inkonsistenzen zu vermeiden.

---

**Artikel 20: Zentralisierte Meldung**

Finanzunternehmen melden an einen einzigen Ansprechpartner (nationale zuständige Behörde), der koordiniert mit:

- Europäischen Aufsichtsbehörden (ESAs)
- Europäischer Zentralbank (EZB) für systemische Risikobewertung
- Einheitlichem Abwicklungsausschuss (SRB) falls relevant
- Anderen EU-Behörden nach Bedarf

**Zweck:** EU-weite Sichtbarkeit von IKT-Vorfällen mit potenziell systemischer Auswirkung gewährleisten.

---

**Artikel 23: Freiwillige Meldung erheblicher Cyberbedrohungen**

Finanzunternehmen können zuständige Behörden auch ohne tatsächlichen Vorfall freiwillig über erhebliche Cyberbedrohungen informieren, um sektorweite Bewusstsein und Prävention zu fördern.

**Beispiele:**

- Erkennung einer Advanced Persistent Threat (APT)
- Entdeckung einer Zero-Day-Schwachstelle
- Ransomware-Kampagne gegen den Finanzsektor
- Credential-Stuffing-Angriffe in großem Umfang

---

# Kapitel IV — Tests der digitalen Betriebsstabilität

## Überblick (Artikel 24–27)

Finanzunternehmen müssen ein solides Testprogramm für die digitale Betriebsstabilität einrichten, aufrechterhalten und überprüfen.

**Artikel 24: Allgemeine Testanforderungen**

**Testprogramm-Komponenten:**

- Breites Spektrum an Bewertungen und Tests entsprechend dem IKT-Risiko der Einrichtung
- Schwachstellenbewertungen und -scans
- Open-Source-Analyse
- Netzwerksicherheitsbewertungen
- Lückenanalysen
- Prüfungen der physischen Sicherheit
- Szenariobasierte Tests
- Kompatibilitätstests
- Leistungstests
- End-to-End-Tests

**Testhäufigkeit:**

- Basistests: Mindestens jährlich
- Kritische Systeme: Häufigere Tests
- Nach wesentlichen Änderungen: Ausgelöste Tests

**ISO 27001:2022 Zuordnung:**

- A.5.30: IKT-Bereitschaft für Betriebskontinuität (Testanforderung)
- A.8.8: Management technischer Schwachstellen
- A.8.34: Schutz von Informationssystemen bei Audit-Tests

---

**Artikel 25: Tests von IKT-Tools, -Systemen und -Prozessen**

Finanzunternehmen müssen Testmethoden implementieren, darunter:

**1. Schwachstellenbewertungen:**

- Identifikation von Systemschwächen
- Automatisierte Scanning-Tools
- Manuelle Überprüfung wo angemessen
- Schwerestufen-basierte Risikobewertung

**2. Szenariobasierte Tests:**

- Betriebskontinuitäts- und Disaster-Recovery-Tests
- Krisenmanagement-Übungen
- Validierung von Failover und Redundanz
- Validierung von Kommunikationsplänen

**3. Kompatibilitätstests:**

- Integration neuer Systeme
- Test von Upgrades und Migrationen
- Plattformübergreifende Kompatibilität

**4. Leistungstests:**

- Kapazitäts- und Lasttests
- Stresstests unter widrigen Bedingungen
- Skalierbarkeitsvalidierung

**Dokumentation:**

- Testpläne und -verfahren
- Testergebnisse und Befunde
- Abhilfepläne und Zeitrahmen
- Validierung der Abhilfe

---

**Artikel 26: Erweiterte Tests von IKT-Tools, -Systemen und -Prozessen (TLPT)**

**Threat-Led Penetration Testing (TLPT):**
Ausgewählte Finanzunternehmen müssen erweiterte Tests auf Basis von **Threat-Led Penetration Testing** mindestens alle **3 Jahre** durchführen.

**TLPT-Anwendbarkeit:**

- Bestimmung durch zuständige Behörden
- Typischerweise große, miteinander verflochtene Finanzeinrichtungen
- Einrichtungen mit hoher Bedeutung für die Finanzstabilität
- Kriterien: Größe, systemische Bedeutung, Verflechtung

**TLPT-Anforderungen** (gemäß Artikel 26 und RTS):

**Bedrohungsintelligenz:**

- Realitätsnahe Bedrohungsszenarien
- Simulation von Advanced Persistent Threats (APT)
- Basierend auf TIBER-EU oder gleichwertigen Rahmen

**Red-Team-Tests:**

- Simulierte Angriffe auf kritische Funktionen
- Physische und digitale Angriffsvektoren
- Social-Engineering-Elemente
- Tests der Erkennungs- und Reaktionsfähigkeiten

**Kontrolltests:**

- Purple-Team-Übungen (Red Team + Blue Team Zusammenarbeit)
- Tests von Überwachung, Erkennung und Reaktion
- Validierung von Incident-Response-Verfahren
- Tests von Kommunikation und Eskalation

**Abschluss und Behebung:**

- Detaillierter Befundbericht
- Abhilfeplan mit Zeitrahmen
- Management- und Vorstandsberichte
- Meldung an die Aufsichtsbehörde

**ISO 27001:2022 Zuordnung:**

- Keine direkte ISO-27001-Entsprechung (TLPT ist eine DORA-spezifische erweiterte Anforderung)
- Verwandt mit: A.8.34 (Audit-Tests), A.5.7 (Bedrohungsintelligenz)

**TLPT-Rahmenreferenzen:**

- **TIBER-EU:** Europäischer Rahmen für bedrohungsgeführtes ethisches Red Teaming
- **CBEST** (UK), **TIBER-NL** (Niederlande), **iCAST** (Irland): Nationale Rahmen

---

**Artikel 27: Anforderungen an Tester für TLPT**

TLPT muss durchgeführt werden von:

- Unabhängigen externen Testern
- Internen Testern mit Unabhängigkeitsschutzmaßnahmen
- Zuständige Behörden können einen Pool genehmigter Tester einrichten

**Qualifikationen der Tester:**

- Technisches Fachwissen in Bedrohungsintelligenz und Penetrationstests
- Kenntnisse der Finanzsektor-Abläufe
- Zertifizierungsanforderungen (z. B. CREST, OSCP, OSCE oder gleichwertig)
- Geheimhaltungs- und Vertraulichkeitsvereinbarungen

---

# Kapitel V — IKT-Drittparteien-Risikomanagement

## Überblick (Artikel 28–44)

Finanzunternehmen müssen IKT-Drittparteien-Risiken durch einen umfassenden Rahmen und Aufsicht verwalten.

**Artikel 28: Allgemeine Grundsätze**

**Drittparteien-Risikomanagement-Rahmen:**

- Strategie, Richtlinien und Verfahren
- Pflege eines IKT-Drittdienstleister-Registers
- Vorvertragliche Sorgfaltspflicht
- Vertragliche Vereinbarungen
- Laufende Überwachung und Aufsicht
- Exit-Strategien

**ISO 27001:2022 Zuordnung:**

- A.5.19: Informationssicherheit in Lieferantenbeziehungen
- A.5.20: Berücksichtigung von Informationssicherheit in Lieferantenvereinbarungen
- A.5.21: Management der Informationssicherheit in der IKT-Lieferkette
- A.5.22: Überwachung, Überprüfung und Änderungsmanagement von Lieferantendienstleistungen
- A.5.23: Informationssicherheit bei der Nutzung von Cloud-Diensten

---

**Artikel 29: Vorläufige Bewertung des IKT-Konzentrationsrisikos**

Finanzunternehmen müssen:

- Konzentrationsrisiko bei IKT-Drittdienstleistern identifizieren
- Potenzielle Single Points of Failure bewerten
- Alternative Anbieter oder Minderungsstrategien berücksichtigen
- Erhebliche Konzentrationsrisiken der zuständigen Behörde melden

**Konzentrationsrisikofaktoren:**

- Nutzung desselben Anbieters für mehrere kritische Funktionen
- Begrenzte alternative Anbieter verfügbar
- Geografische Konzentration (eine Region/ein Land)
- Abhängigkeitsketten (Anbieter hängt von Unteranbieter ab)

**DORA-spezifisch:**
Dies ist eine explizite Anforderung, die in ISO 27001 typischerweise nicht im Detail enthalten ist.

---

**Artikel 30: Wesentliche Vertragsbestimmungen**

**Obligatorische Vertragselemente** für IKT-Dienste, die kritische oder wichtige Funktionen unterstützen:

**1. Dienstleistungsbeschreibungen:**

- Klare Definition der erbrachten Dienstleistungen
- Service Level Agreements (SLAs)
- Standorte der Datenverarbeitung
- Unterstützung für Compliance-Pflichten der Finanzeinrichtung

**2. Sicherheitsanforderungen:**

- Datenschutz- und Vertraulichkeitsmaßnahmen
- Fristen für die Meldung von Sicherheitsvorfällen
- Einschränkungen und Genehmigungen für Unterauftragsvergabe
- Verfahren zur Datenrückgabe und -löschung

**3. Zugangs- und Prüfungsrechte:**

- Prüfungsrecht der Finanzeinrichtung
- Zugangs- und Prüfungsrecht der zuständigen Behörde
- Recht auf Vor-Ort-Prüfungen
- Informationszugang für Aufsichtszwecke

**4. Kündigung und Exit:**

- Exit-Strategien mit ausreichendem Übergangszeitraum
- Unterstützung bei Datenportabilität und -migration
- Dienstkontinuität während des Übergangs
- Rückgabe oder Löschung von Daten

**5. Gerichtsbarkeit und Streitbeilegung:**

- Geltendes Recht (Recht eines EU-Mitgliedstaates)
- Streitbeilegungsmechanismen
- Pflichten zur regulatorischen Zusammenarbeit

**ISO 27001:2022 Zuordnung:**

- A.5.20: Berücksichtigung von Informationssicherheit in Lieferantenvereinbarungen
- A.5.23: Informationssicherheit bei der Nutzung von Cloud-Diensten (Exit-Strategien)

**DORA-Erweiterung:**
DORA enthält wesentlich präskriptivere vertragliche Anforderungen als ISO 27001, insbesondere bezüglich:

- Zugangs- und Prüfungsrechten für Behörden
- Obligatorischer Exit-Strategien
- Governance der Unterauftragsvergabe
- Datenlokalisierung und -portabilität

---

**Artikel 31: IKT-Drittdienstleister-Register**

Finanzunternehmen müssen ein Register aller IKT-Drittdienstleister pflegen und aktualisieren, einschließlich:

- Anbieteridentifikation
- Erbrachte Dienstleistungen
- Kritikalitätsklassifizierung (kritisch, wichtig, nicht kritisch)
- Vertragsdaten und -verlängerung
- Gründungsland und Datenverarbeitungsstandorte
- Verwendete Unterauftragnehmer

**Berichterstattung:** Jährliche Übermittlung an die zuständige Behörde (oder häufiger auf Anfrage)

**ISO 27001:2022 Zuordnung:**

- A.5.19 (erfordert Lieferantenregister, weniger präskriptiv als DORA)

---

**Artikel 32–44: Überwachungsrahmen für kritische IKT-Drittdienstleister**

**Einstufung als kritischer Anbieter:**
Europäische Aufsichtsbehörden (ESAs) können IKT-Drittdienstleister als „kritisch" einstufen basierend auf:

- Systemischer Auswirkung auf die Finanzstabilität
- Anzahl und Art der bedienten Finanzeinrichtungen
- Komplexität und Kritikalität der Dienste
- Substituierbarkeit und Konzentrationsrisiko

**Einstufungsprozess** (Artikel 33):

- ESA-Empfehlung an Finanzeinrichtungs-Kunden
- Kriterienbewertung (Faktoren gemäß Artikel 31(1))
- IKT-Anbieter hat Gelegenheit zur Informationsübermittlung
- Bestimmung der federführenden Aufsichtsbehörde (LOA)

**Aufsichtsaktivitäten** (Artikel 35–40):

- Allgemeine Untersuchungen und Vor-Ort-Prüfungen
- Informations- und Dokumentationsanfragen
- Empfehlungen zur Behebung
- Sanktionen bei Nichteinhaltung

**IKT-Anbieterpflichten** (Artikel 37–41):

- Zusammenarbeit mit der federführenden Aufsichtsbehörde
- Bereitstellung von Informationen und Dokumentation
- Ermöglichung von Prüfungen
- Umsetzung von Empfehlungen

**DORA-spezifisch:** ISO 27001 hat keinen gleichwertigen regulatorischen Überwachungsrahmen für Dienstleister.

---

# Kapitel VI — Informationsaustauschvereinbarungen

## Artikel 45: Informationsaustausch

Finanzunternehmen können an Informationsaustauschvereinbarungen teilnehmen, um Bedrohungsintelligenz und Abwehrfähigkeiten zu verbessern.

**Erlaubter Informationsaustausch:**

- Informationen und Bedrohungsintelligenz zu Cybervorfällen
- Kompromittierungsindikatoren (IOCs)
- Taktiken, Techniken und Vorgehensweisen (TTPs)
- Schwachstellen und Sicherheitshinweise
- Wirksame Sicherheitspraktiken

**Bedingungen:**

- Freiwillige Teilnahme
- Schutz vertraulicher und sensibler Informationen
- Einhaltung des Datenschutzrechts (GDPR)
- Kein Austausch wettbewerbssensibler Informationen
- Keine Einschränkung der Meldepflichten gegenüber Behörden

**ISO 27001:2022 Zuordnung:**

- A.5.7: Bedrohungsintelligenz

**Informationsaustausch-Plattformen:**

- Financial Services Information Sharing and Analysis Center (FS-ISAC)
- European Financial ISAC (EU FS-ISAC)
- Nationale CERTs und CSIRTs
- Sektorspezifische Austauschgruppen

---

# ISO 27001:2022 — DORA Zuordnung

## Kontroll-Zuordnungsmatrix

| DORA Anforderung | DORA Artikel | ISO 27001:2022 Kontrolle | Lückenanalyse |
|------------------|-------------|--------------------------|---------------|
| IKT-Risiko-Governance | Art. 5 | Klausel 5.1, 5.3, A.5.1, A.5.2 | DORA: Explizite Verantwortung des Leitungsorgans |
| IKT-Risikorahmen | Art. 6 | Klausel 4–10 (gesamtes ISMS) | DORA: Präskriptivere Rahmenelemente |
| Asset-Identifizierung | Art. 8 | A.5.9, A.5.12 | DORA: Legacy-Systeme explizit, Datenmapping erforderlich |
| Schutz & Prävention | Art. 9 | A.8.1–8.24, A.7.4 | DORA: Netzwerksegmentierung obligatorisch |
| Erkennung | Art. 10 | A.8.15, A.8.16, A.5.7 | DORA: Echtzeit-Überwachung erwartet |
| Reaktion & Wiederherstellung | Art. 11 | A.5.24–5.30, A.8.13–8.14 | DORA: RTO/RPO für kritische Funktionen |
| Lernen & Weiterentwickeln | Art. 12 | A.5.27, Klausel 10 | Kongruent |
| Sensibilisierung & Schulung | Art. 15 | A.6.3 | DORA: Messbare Schulungsprogramme |
| Incident-Klassifizierung | Art. 18 | A.5.25 | DORA: Spezifische Klassifizierungskriterien (schwerwiegend) |
| Incident-Meldung | Art. 19–20 | A.5.5, A.5.26 | **DORA-spezifisch:** Regulatorische Meldefristen |
| Testprogramm | Art. 24–25 | A.5.30, A.8.8 | DORA: Umfassendere Testanforderungen |
| TLPT | Art. 26–27 | Kein Äquivalent | **DORA-einzigartig:** Bedrohungsgeführte Penetrationstests |
| Drittanbieter-Register | Art. 31 | A.5.19 | DORA: Präskriptives Register und Berichterstattung |
| Drittanbieter-Verträge | Art. 30 | A.5.20, A.5.23 | **DORA-spezifisch:** Obligatorische Vertragsbestimmungen |
| Konzentrationsrisiko | Art. 29 | Keine direkte Entsprechung | **DORA-einzigartig:** Explizite Konzentrationsrisikobewertung |
| Kritische Anbieter-Aufsicht | Art. 32–44 | Kein Äquivalent | **DORA-einzigartig:** Regulatorischer Überwachungsrahmen |
| Informationsaustausch | Art. 45 | A.5.7 | Kongruent |

## Wesentliche Lücken zwischen ISO 27001:2022 und DORA

**Lücke 1: Regulatorische Incident-Meldung**

- ISO 27001: Internes Incident-Management
- DORA: Pflichtmeldung an zuständige Behörden mit Fristen

**Lücke 2: Threat-Led Penetration Testing (TLPT)**

- ISO 27001: Kein Äquivalent
- DORA: Erforderlich für bestimmte Finanzeinrichtungen alle 3 Jahre

**Lücke 3: Drittanbieter-Vertragsbestimmungen**

- ISO 27001: Allgemeine Lieferantenvereinbarungshinweise
- DORA: Spezifische obligatorische Vertragsklauseln

**Lücke 4: Kritische Anbieter-Aufsicht**

- ISO 27001: Kein regulatorisches Aufsichtskonzept
- DORA: ESA-Überwachungsrahmen für kritische IKT-Anbieter

**Lücke 5: Konzentrationsrisiko**

- ISO 27001: Indirekt durch Risikobewertung adressiert
- DORA: Explizite Bewertungs- und Meldepflicht

---

# Umsetzungsüberlegungen

## DORA-Compliance-Zeitplan

**Wenn [Organisation] eine DORA-regulierte Finanzeinrichtung ist:**

**Januar 2025 (Geltungsdatum):**

- DORA wird anwendbar
- Zuständige Behörden können Aufsichtsbewertungen durchführen

**Empfohlener Vorbereitungszeitplan:**

**6–12 Monate vorher (Jul 2024 — Dez 2024):**

- Lückenanalyse gegenüber DORA-Anforderungen
- Verbesserung des IKT-Risikomanagement-Rahmens
- Incident-Meldeprozess einrichten
- Drittparteien-Risikomanagement überprüfen
- Vertragsverhandlungen mit kritischen IKT-Anbietern

**0–6 Monate danach (Jan 2025 — Jun 2025):**

- Test der Incident-Meldefähigkeit
- Start des Testprogramms für digitale Betriebsstabilität
- Drittanbieter-Register einrichten
- Informationsaustausch-Teilnahme
- Umsetzung technischer Regulierungsstandards (RTS) bei Verabschiedung

**Laufend (nach Jun 2025):**

- Jährliche Tests und kontinuierliche Verbesserung
- Vierteljährliche Incident-Meldung (bei Vorfällen)
- Jährliche Drittanbieter-Register-Übermittlung
- 3-Jahres-TLPT-Zyklus (falls bestimmt)

## Ressourcenanforderungen

**Personal:**

- IKT-Risikomanagementfunktion (dediziert)
- Incident-Response-Team mit 24/7-Fähigkeit
- Drittparteien-Risikomanagement-Spezialisten
- Test- und Prüfungsressourcen (intern oder extern)
- Compliance- und regulatorische Berichtsfunktion

**Technologie:**

- Erweiterte SIEM- und SOC-Fähigkeiten
- Test-Tools (Schwachstellen-Scanner, Penetrationstest-Plattformen)
- Drittparteien-Risikomanagement-Plattform
- Integration mit Incident-Meldungsportal
- Backup- und Disaster-Recovery-Infrastruktur

**Externe Unterstützung:**

- Rechtsberatung mit DORA-Expertise
- Externe Prüfer und Penetrationstester
- Managed Security Service Providers (MSSP) bei Bedarf
- Bedrohungsintelligenz-Dienste

## Kostenfolgen

DORA-Compliance erfordert typischerweise:

- Verbesserter IKT-Risikomanagement-Rahmen
- Erweiterte Testfähigkeiten (TLPT)
- Ausgebaute Drittparteien-Aufsicht
- Incident-Meldungsinfrastruktur
- Schulungs- und Sensibilisierungsprogramme

Geschätzte Mehrkosten: 20–35 % Aufschlag über die Basis-ISO-27001-Compliance für mittelgroße Finanzeinrichtungen.

---

# Häufige Fallstricke und Erfahrungswerte

## Häufige DORA-Compliance-Herausforderungen

**Herausforderung 1: Unterschätzung der regulatorischen Meldekomplexität**

- Incident-Meldefristen sind eng (Erstbericht innerhalb von Stunden)
- Klassifizierungskriterien erfordern Beurteilung und Konsistenz
- Meldungsinfrastruktur muss vor Vorfällen getestet werden

**Herausforderung 2: Vertragsverhandlungen mit Drittanbietern**

- Große Cloud-Anbieter könnten DORA-spezifischen Vertragsklauseln widerstehen
- Verhandlungszeiträume können 6–12 Monate dauern
- Manche Anbieter akzeptieren möglicherweise keine Prüfungsrechte für Behörden

**Herausforderung 3: TLPT-Bereitschaft**

- Organisationen ohne Red-Team-Erfahrung könnten Schwierigkeiten haben
- Setzt reife Erkennungs- und Reaktionsfähigkeiten voraus
- Blue-Team-Bereitschaft kritisch für realistische Tests

**Herausforderung 4: Bewertung des Konzentrationsrisikos**

- Konzentrationsrisiko schwierig zu quantifizieren
- Begrenzte alternative Anbieter in manchen Dienstleistungskategorien
- Minderungsstrategien können kostspielig sein (Multi-Cloud, Anbieterdiversifizierung)

**Herausforderung 5: Legacy-System-Herausforderungen**

- Ältere Systeme können unzureichende Protokollierung und Überwachung haben
- Patching und Upgrades können nicht durchführbar sein
- Kompensierende Kontrollen erforderlich, können aber Risiko nicht vollständig mindern

## Bestpraktiken

**Praktik 1:** Zuständige Behörde frühzeitig für Leitlinien kontaktieren
**Praktik 2:** ISO 27001 als Grundlage nutzen und DORA-spezifische Anforderungen ergänzen
**Praktik 3:** Incident-Meldeprozess einrichten und quartalsweise testen
**Praktik 4:** Kritische IKT-Dienstleisterbeziehungen priorisieren
**Praktik 5:** Interne TLPT-Vorbereitung auch ohne formelle Bestimmung durchführen
**Praktik 6:** An Sektor-Informationsaustauschvereinbarungen teilnehmen

---

# Referenzen und Ressourcen

## DORA-Rechtstexte

**Primäre Verordnung:**

- Verordnung (EU) 2022/2554 (DORA) — Amtsblatt der EU

**Technische Regulierungsstandards (RTS):**

- Delegierte Verordnung der Kommission zum IKT-Risikomanagement (Verabschiedung 2024 erwartet)
- Delegierte Verordnung der Kommission zur Incident-Meldung (Verabschiedung 2024 erwartet)
- Delegierte Verordnung der Kommission zu Tests der digitalen Betriebsstabilität (Verabschiedung 2024 erwartet)
- Delegierte Verordnung der Kommission zur Drittparteien-Risiko-Aufsicht (Verabschiedung 2024 erwartet)

**ESA-Websites:**

- Europäische Bankenaufsichtsbehörde (EBA): https://www.eba.europa.eu/
- Europäische Wertpapier- und Marktaufsichtsbehörde (ESMA): https://www.esma.europa.eu/
- Europäische Aufsichtsbehörde für das Versicherungswesen (EIOPA): https://www.eiopa.europa.eu/

## Verwandte Standards und Rahmenwerke

**ISO-Standards:**

- ISO/IEC 27001:2022: Informationssicherheitsmanagementsysteme
- ISO/IEC 27002:2022: Informationssicherheitskontrollen
- ISO/IEC 27005:2022: Informationssicherheits-Risikomanagement
- ISO 22301:2019: Managementsysteme für Betriebskontinuität

**TLPT-Rahmen:**

- **TIBER-EU:** Threat Intelligence-Based Ethical Red Teaming (EZB-Rahmen)
- CBEST: UK-Rahmen für bedrohungsgeführte Penetrationstests
- TIBER-NL: Niederländischer TLPT-Rahmen
- iCAST: Irischer TLPT-Rahmen

**NIST-Publikationen** (informative Referenz):

- NIST Cybersecurity Framework (CSF)
- NIST SP 800-53: Sicherheits- und Datenschutzkontrollen
- NIST SP 800-61: Leitfaden zur Handhabung von Computer-Sicherheitsvorfällen

## Branchenhinweise

**Finanzsektor:**

- FS-ISAC: Financial Services Information Sharing and Analysis Center
- SWIFT Customer Security Programme (CSP)
- PCI DSS: Payment Card Industry Data Security Standard (wo anwendbar)

**Compliance-Beratung:**
DORA-pflichtige Organisationen sollten einbinden:

- Rechtsberatung mit Expertise im EU-Finanzrecht
- Prüfer mit DORA-Compliance-Erfahrung
- Cybersicherheitsberater mit Kenntnissen zu TIBER-EU und TLPT

---

# Anhang A: DORA Compliance-Selbstbewertungs-Checkliste

## IKT-Risikomanagement-Rahmen (Kapitel II)

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| Genehmigung des IKT-Risikorahmens durch Leitungsorgan | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| IKT-Risikomanagementfunktion eingerichtet | ⬜ Ja ⬜ Nein | | |
| Umfassendes IKT-Asset-Inventar | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Legacy-Systeme identifiziert und risikobewertert | ⬜ Ja ⬜ Nein | | |
| Netzwerksegmentierung implementiert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Verschlüsselung sensibler Daten (Ruhezustand und Übertragung) | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Kontinuierliche Überwachung und Erkennung | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Betriebskontinuitäts- und Disaster-Recovery-Pläne | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| RTO/RPO für kritische Funktionen definiert | ⬜ Ja ⬜ Nein | | |
| Post-Incident-Reviews und Lessons Learned | ⬜ Ja ⬜ Nein | | |
| Jährliche IKT-Sicherheitsschulungen | ⬜ Ja ⬜ Nein | | |

## Incident-Management & Meldung (Kapitel III)

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| Incident-Klassifizierungskriterien etabliert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Definition schwerwiegender Vorfälle dokumentiert | ⬜ Ja ⬜ Nein | | |
| Incident-Meldeprozess an zuständige Behörde | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Erstmeldefähigkeit (innerhalb von Stunden) | ⬜ Ja ⬜ Nein | | |
| Incident-Meldungstests durchgeführt | ⬜ Ja ⬜ Nein | | |

## Tests der digitalen Betriebsstabilität (Kapitel IV)

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| Jährliches Testprogramm etabliert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Regelmäßige Schwachstellenbewertungen durchgeführt | ⬜ Ja ⬜ Nein | | |
| Szenariobasierte BCP/DR-Tests | ⬜ Ja ⬜ Nein | | |
| TLPT durchgeführt (falls bestimmt) | ⬜ Ja ⬜ Nein ⬜ N/A ⬜ Ausstehend | | |
| Testergebnisse dokumentiert und behoben | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |

## IKT-Drittparteien-Risikomanagement (Kapitel V)

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| Drittparteien-Risikomanagement-Rahmen | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| IKT-Drittdienstleister-Register | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Vorvertraglicher Sorgfaltspflicht-Prozess | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| DORA-konforme Verträge für kritische Anbieter | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Exit-Strategien für kritische IKT-Dienste | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Konzentrationsrisikobewertung durchgeführt | ⬜ Ja ⬜ Nein | | |
| Jährliche Register-Übermittlung an Behörde | ⬜ Ja ⬜ Nein ⬜ N/A | | |

## Informationsaustausch (Kapitel VI)

| Anforderung | Status | Nachweis-Speicherort | Bemerkungen |
|-------------|--------|----------------------|-------------|
| Teilnahme am Bedrohungsintelligenz-Austausch | ⬜ Ja ⬜ Nein ⬜ Geplant | | |
| Mitgliedschaft in FS-ISAC oder ähnlichem | ⬜ Ja ⬜ Nein ⬜ Geplant | | |

---

# Anhang B: Vorlage für schwerwiegenden IKT-Vorfall (DORA)

**DORA Schwerwiegender IKT-bezogener Vorfall — Erstmeldung**

**An:** [Nationale Zuständige Behörde — Einziger Ansprechpartner]
**Von:** [Name der Finanzeinrichtung]
**Kontakt:** [Name Incident-Response-Manager, Telefon, E-Mail]
**Datum/Uhrzeit:** [ISO 8601 Format]
**LEI (Legal Entity Identifier):** [LEI]
**Meldungstyp:** ⬜ Erstmeldung ⬜ Zwischenbericht ⬜ Abschlussbericht

---

**ABSCHNITT 1: VORFALLZUSAMMENFASSUNG**

**Vorfall-ID:** [Interne Referenznummer]
**Erkennungsdatum/-uhrzeit:** [ISO 8601]
**Vorfall-Startdatum/-uhrzeit** (geschätzt): [ISO 8601]
**Aktueller Status:** ⬜ Laufend ⬜ Eingedämmt ⬜ Gelöst

**Vorfalltyp:**
⬜ Cyberangriff (näher angeben: Ransomware, DDoS, Malware, Phishing usw.)
⬜ Systemausfall (näher angeben: Hardware, Software, Netzwerk)
⬜ Datenverletzung / Datenverlust
⬜ Ausfall eines Drittanbieters
⬜ Auswirkung durch Naturkatastrophe
⬜ Sonstiges (näher angeben): _____________

---

**ABSCHNITT 2: FOLGENABSCHÄTZUNG**

**Betroffene kritische oder wichtige Funktionen:**

- [Funktion 1]: [Auswirkungsbeschreibung]
- [Funktion 2]: [Auswirkungsbeschreibung]

**Dienstunterbrechung:**

- **Dauer:** [Stunden/Minuten der Störung]
- **Betroffene Kunden:** [Anzahl und Typ]
- **Geografischer Umfang:** [Betroffene Länder]
- **Dienstverfügbarkeit:** [Welche Dienste sind nicht verfügbar]

**Datenauswirkung:**
⬜ Keine Daten betroffen
⬜ Daten möglicherweise kompromittiert: [Typ, Menge, Sensibilität]
⬜ Daten bestätigt kompromittiert: [Details]

**Finanzielle Auswirkung** (vorläufig):
⬜ Noch nicht bestimmt
⬜ Geschätzt: [Betrag und Grundlage]

**Reputationsauswirkung:**
⬜ Gering ⬜ Mittel ⬜ Hoch
[Kurzbeschreibung]

---

**ABSCHNITT 3: URSACHE** (vorläufig)

[Kurzbeschreibung der vermuteten oder bestätigten Ursache]

---

**ABSCHNITT 4: REAKTIONSMASSNAHMEN**

**Ergriffene Massnahmen:**
1. [Massnahme 1 — Zeitstempel]
2. [Massnahme 2 — Zeitstempel]
3. [Massnahme 3 — Zeitstempel]

**Aktueller Reaktionsstatus:**
[Kurzbeschreibung der laufenden Reaktion]

**Laufende Massnahmen:**

- [Massnahme mit erwartetem Abschluss]

---

**ABSCHNITT 5: EXTERNE KOORDINATION**

**Beteiligte Drittanbieter:**

- [Anbieter 1]: [Beteiligung]
- [Anbieter 2]: [Beteiligung]

**Externe Benachrichtigungen:**

- **Kunden:** ⬜ Ja ⬜ Nein ⬜ Geplant [Datum/Uhrzeit]
- **GDPR-Datenschutzbehörde:** ⬜ Ja ⬜ Nein ⬜ N/A
- **Andere Behörden:** [Angabe]

---

**ABSCHNITT 6: NÄCHSTE AKTUALISIERUNG**

**Nächster Bericht fällig:** [Datum/Uhrzeit]
**Berichtstyp:** ⬜ Zwischenbericht ⬜ Abschlussbericht

---

**ERKLÄRUNG**

Ich bestätige, dass die in dieser Meldung gemachten Angaben nach bestem Wissen und Gewissen zum Stand [Datum/Uhrzeit] korrekt sind.

**Name:** [Vertreter der Geschäftsleitung]
**Titel:** [Titel]
**Unterschrift:** [Digitale Signatur falls zutreffend]

---

**ENDE DER TECHNISCHEN REFERENZ**

---

*Diese technische Referenz unterstützt potenzielle DORA-Compliance-Anforderungen gemäß ISMS-POL-00. Alle Feststellungen zur regulatorischen Anwendbarkeit und verbindlichen Anforderungen sind in ISMS-POL-00 und genehmigten ISMS-Richtliniendokumenten definiert.*

*Für Organisationen, die NICHT DORA-pflichtig sind, dient dieses Dokument ausschließlich der informativen Sensibilisierung und begründet KEINE Compliance-Pflichten.*

<!-- QA_VERIFIED: 2026-03-28 -->
