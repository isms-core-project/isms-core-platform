<!-- ISMS-CORE:POLICY:ISMS-POL-00-DE:framework:POL:00 -->
**ISMS-POL-00 — Regulatory Applicability Framework**
**Autoritative Referenz für ISMS-Compliance-Verpflichtungen**

---

## Dokumentenkontrolle

| Feld | Wert |
|------|------|
| **Dokumenttitel** | Regulatory Applicability Framework |
| **Dokumenttyp** | Richtlinie (Policy) |
| **Dokument-ID** | ISMS-POL-00 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung (Geschäftsleitung) |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | [Date - 8 Wochen] | ISB | Ersterstellung — Drei-Stufen-Framework-Struktur |
| 0.2 | [Date - 6 Wochen] | ISB + Legal | DORA, NIS2, AI Act bedingte Verordnungen ergänzt |
| 0.3 | [Date - 4 Wochen] | DSB | GDPR/FADP-Abschnitte ausgebaut, Bewertungsmethodik ergänzt |
| 0.4 | [Date - 2 Wochen] | ISB/Legal/DSB | Stakeholder-Feedback aus Policy-Review eingearbeitet |
| 1.0 | [Date] | ISB/Legal/DSB | Erste freigegebene Version für Stage-1-Audit |

**Review-Zyklus**: Jährlich (oder bei wesentlichen regulatorischen Änderungen)
**Nächstes Review-Datum**: [Gültigkeitsdatum + 12 Monate]

**Freigabekette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: Legal/Compliance Officer
- Compliance: Datenschutzbeauftragter (DSB)
- Finale Autorität: Geschäftsleitung (Geschäftsleitung)

**Verknüpfte Dokumente**:

- Alle ISMS-Policy-Dokumente (verpflichtende Referenz)
- ISO/IEC 27001:2022 Clause 4.1 (Understanding the organisation and its context)
- ISO/IEC 27001:2022 Clause 4.2 (Understanding the needs and expectations of interested parties)

**Detaillierte Anforderungsreferenzen** (für bedingte Verordnungen — siehe Abschnitt 8.3):

- ISMS-REF-DORA — Digital Operational Resilience Act Requirements Reference
- ISMS-REF-EU-AI-ACT — EU Artificial Intelligence Act Requirements Reference
- ISMS-REF-FINMA — FINMA Circular 2023/1 Requirements Reference
- ISMS-REF-NIS2 — Network and Information Security Directive 2 Requirements Reference
- ISMS-REF-PCI-DSS — Payment Card Industry Data Security Standard Requirements Reference

**Verteilung**: Alle ISMS-Stakeholder, Policy-Autoren, System-Owner, Auditoren
**Referenziert durch**: Alle ISMS-Policy-Dokumente

**Sprachstrategie**: Wo technische oder regulatorische Begriffe international etabliert sind (z. B. GDPR, ISO/IEC, NIST), wird die englische Terminologie beibehalten, um Präzision zu gewährleisten und grenzüberschreitende regulatorische Referenzierung zu erleichtern.

---

## Zusammenfassung

Dieses Dokument ist die **autoritative Referenz** für die Interpretation der Anwendbarkeit von Verordnungen und Rahmenwerken im gesamten Informationssicherheits-Managementsystem (ISMS).

**Zweck**: Mehrdeutigkeiten und Inkonsistenzen bei der Referenzierung von Verordnungen und Rahmenwerken in ISMS-Richtlinien, -Verfahren und -Kontrollen zu beseitigen.

**Geltungsbereich**: Alle Verweise auf Gesetze, Verordnungen, Standards und Rahmenwerke in der ISMS-Dokumentation.

**Grundprinzip**: **Die Anwendbarkeit von Verordnungen muss explizit festgelegt, nicht angenommen werden.** Verweise auf Verordnungen und Rahmenwerke fallen in drei Kategorien:

1. **Pflichtige Compliance** — Rechtliche Verpflichtungen, die für die Organisation gelten
2. **Bedingte Anwendbarkeit** — Anforderungen, die nur unter bestimmten Umständen gelten
3. **Informative Referenz** — Best Practices und technische Orientierungshilfen

**Verwendung**: Alle ISMS-Richtlinien MÜSSEN Abschnitt 1.3 enthalten, der auf dieses Framework verweist, oder einen Abschnitt „Regulatory Framework" mit direkter Einbeziehung dieser Kategorien.

**Schlüsselbegriffe**: Definitionen für in dieser Richtlinie verwendete Begriffe (Mandatory, Conditional, Tier 1/2/3, Applicability Trigger usw.) sind im **Glossar** am Ende dieses Dokuments aufgeführt.

---

## Policy-Autorität und Grenzen

### Zweck und Geltungsbereich dieser Richtlinie

Diese Richtlinie definiert die **Identifizierung und Anwendbarkeit** gesetzlicher, behördlicher, regulatorischer und vertraglicher Anforderungen für das Informationssicherheits-Managementsystem der Organisation.

**Diese Richtlinie legt fest:**

- Welche Verordnungen und Standards für die Organisation gelten
- Kategorisierung regulatorischer Verpflichtungen (Mandatory, Conditional, Informational)
- Bewertungsmethodik zur Feststellung der Anwendbarkeit
- Überprüfungs- und Aktualisierungsprozesse für Änderungen der regulatorischen Landschaft

**Diese Richtlinie legt NICHT fest:**

- Risikobehandlungsentscheidungen (adressiert in Clause 6 — Risikomanagement)
- Anforderungen zur Kontrollumsetzung (adressiert in Annex-A-Kontrollen)
- Compliance-Status oder -Verifizierung (adressiert in Compliance-Monitoring-Prozessen)

Das Ergebnis der Bewertung der regulatorischen Anwendbarkeit dient als **Eingabe** für:

- Scoping-Entscheidungen für Kontrollen in Annex A
- Priorisierung bei Risikobewertung und -behandlung
- Verhältnismäßigkeitsentscheidungen bei der Kontrollumsetzung
- Auditplanung und Compliance-Verifizierung

**Abgrenzungsprinzip**: Diese Richtlinie legt die regulatorische Anwendbarkeit fest. Umsetzung, Durchsetzung und Verifizierung erfolgen in separaten ISMS-Prozessen.

**Integration mit ISO 27001 Clause 4:**

- **Clause 4.1 (Context of the Organisation)**: Diese Richtlinie adressiert den externen Kontext (Rechts- und Regulierungsumfeld). Der interne Kontext (Organisationsstruktur, Technologie, Kultur) wird im ISMS-Kontextdokument behandelt.
- **Clause 4.2 (Interested Parties)**: Anforderungen interessierter Parteien (Kundenverpflichtungen, regulatorische Erwartungen), die durch dieses Framework identifiziert werden, fliessen in das Interessensparteien-Register im ISMS-Kontextdokument ein.

**Integration mit der Risikobewertung (Clause 6):**

In dieser Richtlinie identifizierte regulatorische Verpflichtungen fliessen ein in:

- **ISMS-RISK-METHODOLOGY** (Clause 6.1.2 Risikobewertung): Regulatorische Anforderungen werden als externe Risikofaktoren mit inhärenter Priorität behandelt (Tier 1 = hohe Priorität, Tier 2 bedingt = mittlere Priorität wenn anwendbar, Tier 3 = informative Eingabe)
- **ISMS-RISK-TREATMENT** (Clause 6.1.3 Risikobehandlung): Die Auswahl und Priorisierung von Kontrollen berücksichtigt regulatorische Verpflichtungen neben technischen Risiken
- **Statement of Applicability (SoA)**: Die Begründung für die Kontrollanwendbarkeit verweist auf POL-00 Tier-Zuordnungen

---

**Kategorien der regulatorischen Anwendbarkeit**

**Kategorie-Definitionen**

**Pflichtige Compliance (Mandatory)**
Rechtliche oder vertragliche Verpflichtungen, denen die Organisation ZWINGEND nachkommen muss. Nicht-Einhaltung hat rechtliche Haftung, regulatorische Bussen, Vertragsbruch oder Zertifizierungsverlust zur Folge.

**Merkmale**:

- Durch Gesetz oder Vertrag durchsetzbar
- Nicht-Einhaltung hat rechtliche/finanzielle Konsequenzen
- Erfordert dokumentierte Nachweise der Compliance
- Unterliegt regulatorischen Audits und Inspektionen

**Informative Referenz / Best-Practice-Ausrichtung (Informational)**
Rahmenwerke und Standards, die für technische Orientierung, Benchmarking oder freiwillige Ausrichtung verwendet werden. Sie informieren Sicherheitspraktiken, stellen aber keine verpflichtenden Compliance-Anforderungen dar, es sei denn, sie werden ausdrücklich durch Vertrag oder Verordnung gefordert.

**Merkmale**:

- Freiwillige Annahme als Best Practice
- Kein rechtlicher Durchsetzungsmechanismus
- Für technische Implementierungsanleitung verwendet
- Können bei vertraglicher Referenzierung verpflichtend werden

**Bedingte Anwendbarkeit (Conditional)**
Anforderungen, die nur bei Erfüllung spezifischer Bedingungen gelten (z. B. Branchensektor, geografische Lage, Dienstleistungsart, Kundenverträge, regulatorischer Geltungsbereich).

**Merkmale**:

- Anwendbarkeit hängt vom organisatorischen Kontext ab
- Kann aufgrund geschäftlicher Aktivitäten verpflichtend werden
- Erfordert periodische Neubewertung mit Weiterentwicklung des Unternehmens
- Beispiele: PCI DSS v4.0.1 (nur bei Kartenverarbeitung), HIPAA (nur bei US-Gesundheitsdaten)

**Erläuterung zur Tier-Klassifizierung**: Die Tier-Klassifizierung (Mandatory, Conditional, Informational) bestimmt die **regulatorische Bindungswirkung** und impliziert für sich allein keine Umsetzungspflichten. Umsetzungsentscheidungen werden durch den Risikobewertungs- und -behandlungsprozess getroffen, wobei regulatorische Anforderungen neben Faktoren wie Risikobereitschaft, Geschäftskontext und technischer Machbarkeit berücksichtigt werden.

## Compliance-Hierarchie

```
┌─────────────────────────────────────────────────────────────────┐
│                    COMPLIANCE-HIERARCHIE                        │
├─────────────────────────────────────────────────────────────────┤
│  TIER 1: MANDATORY (Rechtlich/Vertraglich)                      │
│  • Swiss Federal Data Protection Act (FADP)                     │
│  • EU GDPR (bei Verarbeitung personenbezogener EU-Daten)        │
│  • ISO/IEC 27001:2022 (für Zertifizierung)                      │
│  • Branchenspezifische Verordnungen (soweit anwendbar)          │
│  • Kundenverträge (explizite Sicherheitsanforderungen)          │
│                                                                 │
│  TIER 2: CONDITIONAL (Kontextabhängig)                          │
│  • DORA (bei EU-Finanzdienstleistungsunternehmen)               │
│  • NIS2 (bei wesentlichen/wichtigen Einrichtungen in der EU)    │
│  • PCI DSS v4.0.1 (bei Zahlungskartenverarbeitung)              │
│  • HIPAA (bei Verarbeitung von US-Gesundheitsdaten)             │
│  • Branchenregelungen (sektorabhängig)                          │
│                                                                 │
│  TIER 3: INFORMATIONAL (Best Practice)                          │
│  • NIST SP 800-Reihe (technische Orientierung)                  │
│  • CIS Controls (Sicherheits-Benchmarks)                        │
│  • OWASP (Anwendungssicherheit)                                 │
│  • Branchenrahmenwerke (nur referenziell)                       │
└─────────────────────────────────────────────────────────────────┘
```

> *Falls Box-Zeichen nicht korrekt dargestellt werden, sind die Tier-Definitionen in den Abschnitten 3–5 nachzulesen.*

---

# Pflichtige Compliance (Tier 1)

## Swiss Federal Data Protection Act (FADP/nDSG)

**Anwendbarkeit**: Alle Tätigkeiten einer in der Schweiz ansässigen oder in der Schweiz tätigen Organisation

**Wesentliche Anforderungen**:

- Artikel 6: Grundsätze (Rechtmässigkeit, Verhältnismässigkeit, Zweckbindung)
- Artikel 7: Datensicherheit (angemessene technische und organisatorische Massnahmen)
- Artikel 8: Datenbearbeitung durch Auftragsbearbeiter
- Artikel 19: Auskunftsrecht (Betroffenenrechte)
- Artikel 328b OR (Obligationenrecht): Arbeitnehmerüberwachung und Persönlichkeitsschutz

**Auswirkungen auf das ISMS**:

- Datenschutz durch Technik und durch datenschutzfreundliche Voreinstellungen
- Technische Sicherheitsmassnahmen (Verschlüsselung, Zugriffskontrolle)
- Transparenz und Verhältnismässigkeit bei der Arbeitnehmerüberwachung
- Verzeichnis der Datenbearbeitungstätigkeiten (Art. 12)
- Meldung von Datenschutzverletzungen (Art. 24)

**Referenz**: Bundesgesetz über den Datenschutz (SR 235.1), in Kraft seit 1. September 2023

## EU General Data Protection Regulation (GDPR)

**Anwendbarkeit**: Bei Verarbeitung personenbezogener Daten von EU-Bürgerinnen und -Bürgern

**Wesentliche Anforderungen**:

- Artikel 5: Grundsätze der Verarbeitung (Rechtmässigkeit, Fairness, Transparenz, Zweckbindung)
- Artikel 6: Rechtsgrundlage der Verarbeitung
- Artikel 24: Verantwortlichkeiten des Verantwortlichen (Rechenschaftspflicht)
- Artikel 25: Datenschutz durch Technik und datenschutzfreundliche Voreinstellungen
- Artikel 28: Pflichten des Auftragsverarbeiters (Verträge, Sicherheitsmassnahmen)
- Artikel 32: Sicherheit der Verarbeitung (Verschlüsselung, Pseudonymisierung, Belastbarkeit)
- Artikel 33: Meldung von Verletzungen (72 Stunden an Aufsichtsbehörde)
- Artikel 35: Datenschutz-Folgenabschätzung (DPIA) bei Verarbeitungen mit hohem Risiko

**Auswirkungen auf das ISMS**:

- Technische und organisatorische Massnahmen (TOM)
- Verschlüsselung und Pseudonymisierung
- Zugriffskontrollen und Authentifizierung
- Verfahren zur Reaktion auf Datenschutzverletzungen
- Lieferantenmanagement (Auftragsverarbeitungsverträge)
- Datenschutz-Folgenabschätzungen

**Referenz**: Verordnung (EU) 2016/679, in Kraft seit 25. Mai 2018

## ISO/IEC 27001:2022

**Anwendbarkeit**: Wo die Organisation eine ISO-27001-Zertifizierung anstrebt

**Wesentliche Anforderungen**:

- Annex A Controls (93 Kontrollen in organisatorischen, personenbezogenen, physischen und technologischen Bereichen)
- Clause 4: Kontext der Organisation
- Clause 5: Führung und Verpflichtung
- Clause 6: Risikobewertung und -behandlung
- Clause 7: Unterstützung (Ressourcen, Kompetenz, Bewusstsein, Kommunikation, dokumentierte Information)
- Clause 8: Betrieb (Risikobehandlung, Bewertung)
- Clause 9: Leistungsbewertung (Überwachung, internes Audit, Management-Review)
- Clause 10: Verbesserung (Nichtkonformität, Korrekturmassnahmen, fortlaufende Verbesserung)

**Auswirkungen auf das ISMS**:

- Umsetzung des Policy-Frameworks
- Risikomanagement-Methodik
- Kontrollumsetzung und Nachweisführung
- Internes Auditprogramm
- Management-Review-Prozess
- Fortlaufende Verbesserung

**Referenz**: ISO/IEC 27001:2022 Information Security Management Systems

## Weitere verpflichtende Verordnungen

Organisationen sollten weitere verpflichtende Verordnungen auf Basis ihres spezifischen Kontexts dokumentieren:

| Verordnung | Auslöser | Beispiele |
|-----------|---------|----------|
| **Arbeitsrecht** | Mitarbeitende in der jeweiligen Jurisdiktion | Betriebliche Mitbestimmung (Deutschland), Gesetze zur Arbeitnehmerüberwachung |
| **Finanzmarktrecht** | Finanzdienstleistungen | FINMA (Schweiz), BaFin (Deutschland), MiFID II (EU) |
| **Telekommunikation** | Telekommunikationsdienste | Rechtmässige Überwachung, Vorratsdatenspeicherung |
| **Exportkontrolle** | Grenzüberschreitender Betrieb | Dual-Use-Güter, Kryptographie-Export |
| **Vertragsrecht** | Kundenvereinbarungen | Explizite Sicherheitsanforderungen in Serviceverträgen |

---

# Bedingte Anwendbarkeit (Tier 2)

Diese Verordnungen gelten **nur, wenn spezifische Geschäftsbedingungen erfüllt sind**:

## Swiss Financial Market Supervisory Authority (FINMA)

**Verordnung**: Eidgenössische Finanzmarktaufsicht (FINMA)
**Primäre Rundschreiben**:

- FINMA-Rundschreiben 2023/1 (Operationelle Risiken und Resilienz — Banken, in Kraft seit 1. Januar 2024)
- FINMA-Rundschreiben 2008/7 (Outsourcing — Banken)
- FINMA-Rundschreiben 2018/3 (Outsourcing — Versicherungen)

**Anwendbarkeitsauslöser**:

- Die Organisation ist ein von der FINMA reguliertes **schweizerisches Finanzinstitut**:
  - Banken (Banklizenz der FINMA)
  - Effektenhändler (Effektenhändlerlizenz)
  - Versicherungsunternehmen (Versicherungslizenz)
  - Finanzmarktinfrastrukturen (Börsen, Zentralverwahrer)
  - Kollektivanlagen (Fondsleitungslizenzen)

**Wesentliche Anforderungen**:

- **Operationelle Resilienz**: ICT-Risikomanagement, Business-Continuity-Planung, Disaster Recovery
- **Outsourcing**: Drittparteien-Risikomanagement, Due Diligence, Verträge, Exit-Strategien
- **Datenschutz**: Sicherheit, Vertraulichkeit und Verfügbarkeit von Kundendaten
- **Vorfallmeldung**: Wesentliche operationelle Vorfälle an die FINMA
- **Interne Kontrollen**: Governance, Risikomanagement, interne Revision
- **Sub-Outsourcing-Register** (FINMA-Rundschreiben 2023/1 Rz. 15): Banken müssen ein Register aller Sub-Outsourcing-Vereinbarungen führen, bei denen Dienstleister wesentliche Leistungen weiter delegieren. Das Register muss dokumentieren: Identität des Sub-Outsourcers, erbrachte Leistungen, Datenzugang, geografische Lage, Risikobewertung, Genehmigungsstatus.

**Auswirkungen auf das ISMS**:

- Erweiterte Business-Continuity- und Disaster-Recovery-Kontrollen
- Umfassendes Drittparteien-Risikomanagement (A.5.19-23)
- Incident-Response- und Meldeverfahren (A.5.24-28)
- Governance- und Aufsichtsstrukturen (A.5.1, 5.4)
- Sub-Outsourcing-Transparenz und -Genehmigung (A.5.19-23 S3: ICT Supply Chain Security)

**Bewertung**: Wenn die Organisation über eine FINMA-Lizenz oder -Registrierung verfügt → **Pflichtige Compliance**

### Sub-Outsourcing-Anforderungen (FINMA-Rundschreiben 2023/1)

Für dem FINMA-Rundschreiben 2023/1 unterstehende Schweizer Banken gelten folgende Sub-Outsourcing-Anforderungen:

**Definition Sub-Outsourcing:**
Wesentliche Leistungen, die eine Bank an einen Dienstleister ausgelagert hat und die der Dienstleister seinerseits an einen Sub-Outsourcer (Unterlieferant) weitergibt.

**Register-Anforderungen:**
- Umfassendes Register aller Sub-Outsourcing-Vereinbarungen führen
- Register bei Eingehung oder Änderung von Sub-Outsourcing aktualisieren
- Im Register enthalten:
  - Name und Jurisdiktion des Sub-Outsourcers
  - Erbrachte Leistungen (Beschreibung und Kritikalität)
  - Datenzugang und Datenverarbeitungsaktivitäten
  - Geografischer Ort der Leistungserbringung
  - Risikobewertung und Massnahmen zur Risikominderung
  - FINMA-Genehmigungsstatus (sofern erforderlich)

**Genehmigungsanforderungen:**
- Wesentliches Sub-Outsourcing erfordert Bankgenehmigung vor der Umsetzung
- Die Bank muss Sub-Outsourcing-Risiken bewerten (operationell, Konzentrationsrisiko, Datenschutz, Jurisdiktion)
- Vertragliche Weitergabe der Bankanforderungen an Sub-Outsourcer
- Recht zur Prüfung von Sub-Outsourcern (direkt oder über Dienstleister)

**Umsetzung:**
- Sub-Outsourcing-Register wird in ISMS-IMP-A.5.23.2 geführt (Due-Diligence-Arbeitsbuch — Sub-Supplier-Sheet)
- Sub-Outsourcing-Risikobewertung in ISMS-IMP-A.5.23.4 dokumentiert (Governance-Arbeitsbuch)
- Genehmigungsworkflow in den Lieferanten-Onboarding-Prozess integriert (Abschnitt 8: Lifecycle Management)

## Digital Operational Resilience Act (DORA)

**Verordnung**: Regulation (EU) 2022/2554 über die digitale operationelle Resilienz im Finanzsektor
**Inkrafttreten**: 17. Januar 2025

**Anwendbarkeitsauslöser**:

- Die Organisation ist ein **Finanzunternehmen in der EU**:
  - Kreditinstitute (Banken)
  - Zahlungsinstitute und E-Geld-Institute
  - Wertpapierfirmen
  - Anbieter von Krypto-Asset-Dienstleistungen
  - Versicherungs- und Rückversicherungsunternehmen
  - IKT-Drittanbieter für Finanzunternehmen (kritische/wichtige Einstufung)

**Wesentliche Anforderungen**:

- **IKT-Risikomanagement**: Umfassendes Framework für Identifizierung, Schutz, Erkennung, Reaktion, Wiederherstellung
- **Vorfallmeldung**: Wesentliche IKT-Vorfälle an zuständige Behörden
- **Testen der digitalen operationellen Resilienz**: Regelmässige Tests einschliesslich Threat-Led Penetration Testing (TLPT)
- **Drittparteienrisiko**: Überwachung von IKT-Dienstleistern, Verträge, Exit-Strategien
- **Informationsaustausch**: Austausch von Bedrohungsintelligenz und Cybersicherheitsinformationen

**Auswirkungen auf das ISMS**:

- Erweitertes IKT-Risikomanagement-Framework (über ISO 27001 hinaus)
- Erweiterte Incident-Erkennung und -Reaktion (A.5.24-28)
- Obligatorische Resilienz-Testprogramme
- Lieferantenrisikomanagement mit regulatorischer Aufsicht (A.5.19-23)
- Vereinbarungen zum Informationsaustausch

**Bewertung**: Wenn die Organisation ein EU-Finanzunternehmen oder kritischer IKT-Dienstleister ist → **Pflichtige Compliance**

## Network and Information Security Directive 2 (NIS2)

**Richtlinie**: Directive (EU) 2022/2555 über Massnahmen für ein hohes gemeinsames Cybersicherheitsniveau
**Umsetzungsfrist**: 17. Oktober 2024 (EU-Mitgliedstaaten müssen in nationales Recht umsetzen)

**Anwendbarkeitsauslöser**:

- Die Organisation ist eine **wesentliche oder wichtige Einrichtung** in der EU in erfassten Sektoren:

**Wesentliche Einrichtungen** (strengere Anforderungen):

- Energie (Strom, Öl, Gas)
- Verkehr (Luft, Schiene, Wasser, Strasse)
- Banken und Finanzmarktinfrastrukturen
- Gesundheit (Gesundheitsdienstleister, EU-Referenzlabore, Pharmahersteller)
- Trinkwasser und Abwasser
- Digitale Infrastruktur (Internetknotenpunkte, DNS-Dienstleister, Cloud-Computing, Rechenzentren, CDNs, Vertrauensdienstleister)
- IKT-Servicemanagement (Managed-Service-Provider, Managed-Security-Service-Provider)
- Öffentliche Verwaltung (zentrale Regierungseinrichtungen)
- Weltraum (bodengestützte Infrastruktur für Raumsysteme)

**Wichtige Einrichtungen** (weniger streng):

- Post- und Kurierdienste
- Abfallwirtschaft
- Chemische Produktion und Vertrieb
- Lebensmittelproduktion und -vertrieb
- Fertigung (Medizinprodukte, Elektronik, Maschinenbau, Kraftfahrzeuge, Luft- und Raumfahrt)
- Digitale Anbieter (Online-Marktplätze, Suchmaschinen, soziale Netzwerke)
- Forschungsorganisationen

**Wesentliche Anforderungen**:

- **Risikomanagement**: Cybersicherheits-Risikobewertung und Sicherheitsrichtlinien
- **Vorfallbehandlung**: Erkennungs-, Reaktions- und Wiederherstellungsfähigkeiten
- **Business Continuity**: Backup-Management, Disaster Recovery
- **Sicherheit der Lieferkette**: Drittparteien-Risikomanagement
- **Netzwerksicherheit**: Zugangskontrollen, Verschlüsselung, Multi-Faktor-Authentifizierung
- **Vorfallmeldung**: 24-Stunden-Frühwarnung, 72-Stunden-Detailbericht an nationale CSIRT/zuständige Behörde
- **Aufsicht**: Periodische Audits, Sicherheitsbewertungen, Ex-post-Monitoring

**Auswirkungen auf das ISMS**:

- Umfassendes Cybersicherheits-Risikomanagement (Clause 6)
- Incident-Response mit regulatorischen Meldezeitplänen (A.5.24-28)
- Anforderungen an die Lieferkettensicherheit (A.5.19-23)
- Technische Sicherheitskontrollen (Verschlüsselung, Zugriffskontrolle) (A.8.x-Reihe)
- Business Continuity und Disaster Recovery (A.5.29-30)

**Bussgelder**: Bis zu 10 Mio. EUR oder 2 % des weltweiten Jahresumsatzes (wesentliche Einrichtungen), 7 Mio. EUR oder 1,4 % (wichtige Einrichtungen)

**Bewertung**: Wenn die Organisation in einem erfassten Sektor in der EU tätig ist und Grössen-/Kritikalitätsschwellen erfüllt → **Pflichtige Compliance**

## Payment Card Industry Data Security Standard (PCI DSS v4.0.1)

**Standard**: PCI DSS v4.0.1 (gültig ab 31. März 2024)
**Herausgebendes Gremium**: PCI Security Standards Council

**Anwendbarkeitsauslöser**:

- Die Organisation **speichert, verarbeitet oder überträgt** Zahlungskarteninhaberdaten:
  - Händler, die Kredit-/Debitkarten akzeptieren
  - Zahlungsverarbeiter und Zahlungs-Gateways
  - Dienstleister, die Karteninhaberdaten verarbeiten
  - Jede Einheit mit Zugang zur Karteninhaberdaten-Umgebung (CDE)

**Wesentliche Anforderungen**:

- **12 Anforderungen in 6 Kontrollzielen**:

  1. Netzwerksicherheitskontrollen installieren und pflegen
  2. Sichere Konfigurationen auf alle Systemkomponenten anwenden
  3. Gespeicherte Kontodaten schützen
  4. Karteninhaberdaten bei der Übertragung mit starker Kryptographie schützen
  5. Systeme und Netzwerke vor Schadsoftware schützen
  6. Sichere Systeme und Software entwickeln und pflegen
  7. Zugang zu Karteninhaberdaten nach dem Need-to-know-Prinzip beschränken
  8. Benutzer identifizieren und den Zugang zu Systemkomponenten authentifizieren
  9. Physischen Zugang zu Karteninhaberdaten beschränken
  10. Alle Zugriffe auf Systemkomponenten und Karteninhaberdaten protokollieren und überwachen
  11. Sicherheit von Systemen und Netzwerken regelmässig testen
  12. Informationssicherheit durch organisatorische Richtlinien und Programme unterstützen

**Auswirkungen auf das ISMS**:

- Netzwerksegmentierung und Firewall-Kontrollen (A.8.20-22)
- Verschlüsselung von Karteninhaberdaten im Ruhezustand und bei der Übertragung (A.8.24)
- Starke Zugriffskontrollen und Authentifizierung (A.5.15-18, A.8.2-5)
- Schwachstellenmanagement und Patch-Management (A.8.8)
- Protokollierung, Monitoring und Audit-Trails (A.8.15-16)
- Penetrationstests und Schwachstellenscans (A.8.8)

**Validierung**: Jährliche Vor-Ort-Prüfung (Level 1), Self-Assessment Questionnaire (SAQ) für kleinere Händler

**Bewertung**: Wenn die Organisation Zahlungskarten verarbeitet → **Pflichtige Compliance**

## EU Artificial Intelligence Act (AI Act)

**Verordnung**: Regulation (EU) 2024/1689 zur Festlegung harmonisierter Vorschriften für künstliche Intelligenz
**Inkrafttreten**: 1. August 2024 (stufenweise Umsetzung bis August 2028)

**Anwendbarkeitsauslöser**:

- Die Organisation ist ein **Anbieter** (entwickelt oder beauftragt KI-Systeme für den EU-Markt)
- Die Organisation ist ein **Betreiber** (verwendet KI-Systeme in eigener Verantwortung in der EU)
- Die Organisation ist ein **Importeur oder Händler** von KI-Systemen in der EU
- KI-System-Ausgaben betreffen Personen in der EU (unabhängig vom Standort des Anbieters)

**Risikoklassifizierung** (bestimmt Verpflichtungsstufe):

| Risikostufe | Beispiele | Hauptverpflichtungen |
|-------------|----------|----------------------|
| **Inakzeptabel** | Social Scoring, biometrische Echtzeit-Identifizierung (mit Ausnahmen), Manipulationstechniken | **Verboten** |
| **Hohes Risiko** | Personalentscheidungen, Kreditbewertung, Zugang zu wesentlichen Diensten, biometrische Kategorisierung, kritische Infrastruktur | Konformitätsbewertung, Risikomanagement, Daten-Governance, Transparenz, menschliche Aufsicht, Dokumentation |
| **Begrenztes Risiko** | Chatbots, Emotionserkennung, Deepfake-Erstellung | Transparenzpflichten (Offenlegung der KI-Interaktion) |
| **Minimales Risiko** | Spam-Filter, KI-gestützte Entwicklungstools, interne Analysen | Keine spezifischen Pflichten (freiwillige Verhaltenskodizes) |

**Wesentliche Anforderungen (Hochrisiko-Systeme)**:

- Artikel 9: Risikomanagementsystem über den gesamten Lebenszyklus des KI-Systems
- Artikel 10: Daten-Governance (Trainings-, Validierungs- und Testdatensätze)
- Artikel 11: Technische Dokumentation
- Artikel 12: Protokollierung und Aufzeichnung
- Artikel 13: Transparenz und Informationen für Betreiber
- Artikel 14: Massnahmen zur menschlichen Aufsicht
- Artikel 15: Genauigkeit, Robustheit und Cybersicherheit

**Wesentliche Anforderungen (alle Anbieter/Betreiber)**:

- Artikel 4: KI-Kompetenz für Mitarbeitende, die KI-Systeme betreiben
- Artikel 50: Transparenz für bestimmte KI-Systeme (Chatbots, synthetische Inhalte)

**Umsetzungszeitplan**:

- **Februar 2025**: Verbote für KI mit inakzeptablem Risiko
- **August 2025**: Pflichten für KI-Modelle mit allgemeinem Verwendungszweck
- **Dezember 2027**: Vollständige Anwendung für Hochrisiko-KI-Systeme (verschoben vom August 2026 durch den Digital Omnibus, Verordnung (EU) 2026/1744, in Kraft seit 27. Juli 2026)
- **August 2028**: Hochrisiko-KI in regulierten Produkten (Medizinprodukte, Maschinen) (verschoben vom August 2027 durch denselben Digital Omnibus)

**Auswirkungen auf das ISMS**:

- KI-System-Inventar und Risikoklassifizierung (A.5.9)
- Risikomanagement für KI-Systeme (Clause 6, A.5.7)
- Daten-Governance und Qualitätskontrollen (A.5.12-14)
- Protokollierung und Monitoring von KI-Ausgaben (A.8.15-16)
- Verfahren zur menschlichen Aufsicht (A.5.37)
- Mitarbeitendenschulung zur KI-Kompetenz (A.6.3)
- Lieferantenmanagement für KI-Komponenten (A.5.19-23)
- Dokumentation und Transparenz (A.5.37)

**Bussgelder**: Bis zu 35 Mio. EUR oder 7 % des weltweiten Jahresumsatzes (verbotene Praktiken), 15 Mio. EUR oder 3 % (andere Verstösse)

**Bewertung**: Wenn die Organisation KI-Systeme entwickelt, betreibt oder vertreibt, die EU-Bürgerinnen und -Bürger betreffen → Risikoklassifizierung und anwendbare Pflichten prüfen

## Health Insurance Portability and Accountability Act (HIPAA)

**Verordnung**: US-Bundesgesetz zum Schutz von Gesundheitsinformationen
**Inkrafttreten**: 1996 (mit Änderungen durch den HITECH Act 2009, Omnibus Rule 2013)

**Anwendbarkeitsauslöser**:

- Die Organisation ist eine **betroffene Einrichtung** oder ein **Geschäftspartner** (Business Associate), der US-Protected Health Information (PHI) verarbeitet:
  - Gesundheitsdienstleister (Ärzte, Krankenhäuser, Kliniken)
  - Krankenkassen (Versicherungen, HMOs, Medicare/Medicaid)
  - Healthcare-Clearingstellen
  - Business Associates (Anbieter, Auftragnehmer, die PHI im Auftrag betroffener Einrichtungen verarbeiten)

**Wesentliche Anforderungen**:

- **HIPAA Security Rule** (45 CFR Part 164):
  - **Verwaltungssicherheitsmassnahmen**: Sicherheitsmanagementprozess, Workforce-Sicherheit, Informationszugangsverwaltung, Sicherheitsbewusstseinstraining, Notfallplanung
  - **Physische Sicherheitsmassnahmen**: Zugangskontrolle zu Einrichtungen, Workstation-Sicherheit, Geräte- und Medienkontrollen
  - **Technische Sicherheitsmassnahmen**: Zugriffskontrollen, Audit-Kontrollen, Integritätskontrollen, Übertragungssicherheit (Verschlüsselung)
- **HIPAA Privacy Rule**: Patientenrechte, Mindestzugang, Nutzungs- und Offenlegungsbeschränkungen
- **Breach Notification Rule**: Benachrichtigung betroffener Personen (60 Tage), HHS, Medien (bei >500 Betroffenen)
- **Business Associate Agreements (BAAs)**: Verpflichtende Verträge mit allen Anbietern, die PHI verarbeiten

**Auswirkungen auf das ISMS**:

- Risikobewertung und Risikomanagement (gem. Security Rule verpflichtend)
- Zugriffskontrollen und Authentifizierung (A.5.15-18, A.8.2-5)
- Verschlüsselung von PHI (A.8.24)
- Audit-Protokollierung und Monitoring (A.8.15-16)
- Incident-Response und Datenpannenmeldung (A.5.24-28)
- Mitarbeitendenschulung und -bewusstsein (A.6.3)
- Business-Associate-Management (A.5.19-23)

**Bussgelder**: 100–50.000 USD pro Verstoss (bis zu 1,5 Mio. USD pro Jahr), strafrechtliche Sanktionen bei vorsätzlicher Vernachlässigung

**Bewertung**: Wenn die Organisation US-Gesundheitsdaten (PHI) verarbeitet → **Pflichtige Compliance**

## Federal Information Security Management Act (FISMA)

**Verordnung**: US-Bundesgesetz zur Cybersicherheit für Regierungssysteme
**Inkrafttreten**: 2002 (aktualisiert durch den FISMA Reform Act 2014)

**Anwendbarkeitsauslöser**:

- Die Organisation betreibt **Bundes-Informationssysteme** oder erbringt **Cloud-Dienste für US-Bundesbehörden**:
  - Bundesbehörden und -abteilungen
  - Bundesauftragnehmer und Cloud-Dienstleister (FedRAMP-Autorisierung)
  - Organisationen, die Bundesinformationen verarbeiten

**Wesentliche Anforderungen**:

- **Risikobasierter Ansatz für Cybersicherheit**: Gemäss NIST SP 800-53-Kontrollen
- **Kategorisierung**: Systemkategorisierung (Niedrig, Mittel, Hoch) gemäss FIPS 199
- **Kontrollumsetzung**: NIST SP 800-53-Sicherheitskontrollen basierend auf Auswirkungsniveau
- **Kontinuierliches Monitoring**: Fortlaufende Sicherheitsbewertung und Autorisierung (A&A)
- **FedRAMP (für Cloud)**: Federal Risk and Authorization Management Program
  - Drittparteien-Bewertung durch akkreditierte Prüfer (3PAO)
  - Autorisierung durch JAB (Joint Authorization Board) oder Agency ATO (Authority to Operate)

**Auswirkungen auf das ISMS**:

- Umsetzung von NIST SP 800-53-Kontrollen (umfassende Sicherheitskontrollen)
- Systemkategorisierung und Auswirkungsanalyse (A.5.9)
- Kontinuierliches Monitoring und Bewertung (A.8.15-16)
- Supply-Chain-Risikomanagement (A.5.19-23)
- Incident-Response gemäss NIST-Frameworks (A.5.24-28)

**Bewertung**: Wenn die Organisation US-Bundesverträge oder FedRAMP-Autorisierung hat → **Pflichtige Compliance**

## Weitere bedingte Verordnungen

Organisationen sollten die Anwendbarkeit auf Basis des Geschäftskontexts prüfen:

| Verordnung | Anwendbarkeitsauslöser | Region/Geltungsbereich |
|-----------|----------------------|----------------------|
| **Sarbanes-Oxley (SOX)** | US-börsennotiertes Unternehmen | Vereinigte Staaten |
| **GLBA (Gramm-Leach-Bliley)** | US-Finanzinstitut | Vereinigte Staaten |
| **CCPA/CPRA** | Verarbeitung von Daten californischer Einwohner | Kalifornien, USA |
| **China PIPL** | Verarbeitung personenbezogener Daten chinesischer Einwohner | China |
| **Australia Privacy Act** | Verarbeitung australischer personenbezogener Daten | Australien |
| **Singapore PDPA** | Verarbeitung personenbezogener Daten aus Singapur | Singapur |
| **LGPD** | Verarbeitung personenbezogener Daten aus Brasilien | Brasilien |
| **Branchenspezifisch** | Branchenabhängig (Telekommunikation, Energie, Pharma) | Variiert |

---

# Informative Referenz / Best Practice (Tier 3)

Diese Rahmenwerke bieten **technische Orientierung und Best Practices**, sind jedoch rechtlich nicht durchsetzbar:

## NIST Special Publications (SP 800-Reihe)

**Beschreibung**: Cybersicherheitsleitfäden des National Institute of Standards and Technology
**Anwendbarkeit**: Freiwillige Übernahme als Best Practice (sofern nicht durch FISMA/FedRAMP-Vertrag gefordert)

**Wichtige Publikationen**:

- **NIST SP 800-53**: Sicherheits- und Datenschutzkontrollen (umfassender Kontrollkatalog)
- **NIST SP 800-171**: Schutz kontrollierter nicht klassifizierter Informationen (CUI) in nicht-bundesbehördlichen Systemen
- **NIST Cybersecurity Framework (CSF)**: Identify, Protect, Detect, Respond, Recover
- **NIST SP 800-61**: Computer Security Incident Handling Guide
- **NIST SP 800-63**: Digital Identity Guidelines (Authentifizierung, Föderierung)

**Verwendung im ISMS**:

- Technische Implementierungsanleitung für ISO-27001-Kontrollen
- Entwicklung von Incident-Response-Playbooks (800-61)
- Identitäts- und Zugangsverwaltung (800-63)
- Methoden zur Risikobewertung (800-30, 800-37)

## CIS Controls

**Beschreibung**: Center for Internet Security Critical Security Controls
**Version**: CIS Controls v8.1 (18 Kontrollen)
**Anwendbarkeit**: Freiwillige Übernahme für Sicherheits-Benchmarking

**Wichtige Kontrollen**:
1. Inventar und Kontrolle von Unternehmens-Assets
2. Inventar und Kontrolle von Software-Assets
3. Datenschutz
4. Sichere Konfiguration von Unternehmens-Assets
5. Account-Management
6. Zugangskontrollmanagement
7. Kontinuierliches Schwachstellenmanagement
8. Audit-Log-Management
9–18. Weitere Kontrollen zu Backup, Incident-Response, Penetrationstests, Schulung

**Verwendung im ISMS**:

- Asset-Management-Praktiken (A.5.9)
- Konfigurationsmanagement (A.8.9)
- Schwachstellenmanagement (A.8.8)
- Benchmarking der organisatorischen Sicherheitsreife

## OWASP (Open Web Application Security Project)

**Beschreibung**: Community-gesteuerte Standards für Webanwendungssicherheit
**Anwendbarkeit**: Freiwillige Übernahme für sichere Softwareentwicklung

**Wichtige Ressourcen**:

- **OWASP Top 10**: Kritischste Webanwendungs-Sicherheitsrisiken
- **OWASP ASVS**: Application Security Verification Standard
- **OWASP SAMM**: Software Assurance Maturity Model
- **OWASP Cheat Sheets**: Orientierung für sicheres Coding

**Verwendung im ISMS**:

- Sicherer Software-Entwicklungslebenszyklus (A.8.25-28)
- Testen der Webanwendungssicherheit
- Sicherheitsschulung für Entwickler (A.6.3)
- Code-Review und Schwachstellenbewertung

## ISO/IEC 27002:2022

**Beschreibung**: Leitfaden für Informationssicherheitskontrollen
**Anwendbarkeit**: Unterstützende Orientierung für die ISO-27001-Umsetzung (nicht separat zertifizierbar)

**Verwendung im ISMS**:

- Detaillierte Implementierungsanleitung für Annex-A-Kontrollen
- Auswahl und Anpassung von Kontrollen
- Verhältnismässigkeit und Skalierbarkeitsaspekte

## Cloud Security Alliance (CSA)

**Beschreibung**: Best Practices für Cloud-Computing-Sicherheit
**Anwendbarkeit**: Freiwillige Übernahme für Cloud-Sicherheit

**Wichtige Rahmenwerke**:

- **CSA Cloud Controls Matrix (CCM)**: Cloud-Sicherheitskontroll-Framework
- **CSA Security Trust Assurance and Risk (STAR)**: Cloud-Anbieter-Zertifizierung
- **CSA Consensus Assessments Initiative Questionnaire (CAIQ)**: Cloud-Sicherheitsbewertung

**Verwendung im ISMS**:

- Bewertung von Cloud-Dienstleistern (A.5.23)
- Cloud-Sicherheitsarchitektur
- Lieferanten-Sicherheitsbewertungen

## Weitere Best-Practice-Rahmenwerke

Organisationen können je nach Branchenkontext weitere Rahmenwerke referenzieren:

| Rahmenwerk | Beschreibung | Anwendungsfall |
|-----------|-------------|---------------|
| **COBIT** | IT-Governance und -Management | IT-Governance-Ausrichtung |
| **ITIL** | IT-Service-Management | Service-Delivery-Prozesse |
| **ISO 22301** | Business-Continuity-Management | BCM-Programmstruktur |
| **ISO 27017/27018** | Cloud-Sicherheit und Datenschutz | Cloud-spezifische Kontrollen |
| **ENISA-Leitlinien** | Orientierung der EU-Cybersicherheitsagentur | EU-regulatorischer Kontext |

---

# US-amerikanische Bundesanforderungen (Sonderkategorie)

**Grundprinzip**: US-amerikanische Bundesanforderungen zur Cybersicherheit (FISMA, FIPS, FedRAMP, NIST CSF 2.0) gelten **nur, wenn die Organisation explizite vertragliche Verpflichtungen gegenüber dem US-Bund hat**.

**Hinweis zur Cloud-Infrastruktur:** Die Nutzung US-amerikanischer Cloud-Dienstleister (AWS, Azure, GCP) löst **nicht** automatisch US-amerikanische Bundeskonformitätspflichten aus. FedRAMP/FISMA gelten nur wenn:

- Die Organisation Dienste direkt für US-Bundesbehörden erbringt (Hauptauftragnehmer oder Unterauftragnehmer), ODER
- Der Kundenvertrag ausdrücklich FedRAMP-Autorisierung oder FISMA-Compliance verlangt

Die Nutzung von FedRAMP-autorisierten Cloud-Anbietern (z. B. AWS GovCloud) ist eine **Lieferantenrisikomanagement-Entscheidung** (A.5.19-23) und kein Nachweis dafür, dass FedRAMP für die Organisation gilt.

**Standardstatus**: **Nicht anwendbar**, sofern nicht:

- Die Organisation US-Bundesverträge hält
- Die Organisation Dienste für US-Bundesbehörden erbringt
- Der Vertrag ausdrücklich NIST-Kontrollen oder FedRAMP-Autorisierung verlangt

**Begründung**: US-amerikanische Bundesanforderungen haben keine extraterritoriale Wirkung und gelten nicht für Nicht-US-Organisationen, sofern nicht vertraglich vorgeschrieben.

**ISMS-Behandlung**:

- NIST-Rahmenwerke können als **informative Referenz** genutzt werden (Tier 3)
- FISMA/FedRAMP werden **verpflichtend** (Tier 1) nur mit Bundesverträgen
- NIST SP 800-Reihe für technische Orientierung ohne Compliance-Pflicht

**Überlegung zum FedRAMP Marketplace:**

Wenn die Organisation Dienste auf dem FedRAMP Marketplace (fedramp.gov) anbieten möchte, um US-Bundesbehörden zu bedienen, wird die FedRAMP-Autorisierung **verpflichtend** (Tier 1). Diese Entscheidung löst aus:

- Tier-2-zu-Tier-1-Übergang für FISMA/FedRAMP
- Verpflichtende Neubewertung gemäss Abschnitt 5 (Wann neu bewerten)
- Aktualisierung der Regulatory Applicability Matrix in Abschnitt 8.1
- Beauftragung einer 3PAO (Third-Party Assessment Organisation)
- Einleitung des JAB (Joint Authorisation Board) oder Agency ATO (Authority to Operate)

---

# Bestimmung der regulatorischen Anwendbarkeit

## Bewertungsprozess

Organisationen MÜSSEN jährliche Bewertungen der regulatorischen Anwendbarkeit durchführen:

**Schritt 1: Geschäftsaktivitäten identifizieren**

- Geografische Standorte des Betriebs
- Bediente Branchen und Sektoren
- Arten der verarbeiteten Daten (personenbezogene Daten, Gesundheitsdaten, Finanzdaten usw.)
- Kundenbasis (B2B, B2C, öffentlicher Sektor)
- Erbrachte Dienstleistungen (Cloud, Beratung, Software usw.)

**Schritt 2: Verordnungen auf Aktivitäten abbilden**

| Geschäftsaktivität | Ausgelöste Verordnungen |
|-------------------|------------------------|
| Verarbeitung von Daten EU-ansässiger Personen | GDPR (verpflichtend) |
| Tätigkeit in der Schweiz | Swiss FADP (verpflichtend) |
| Ziel: ISO-27001-Zertifizierung | ISO 27001 (verpflichtend) |
| Verarbeitung von Zahlungskarten | PCI DSS v4.0.1 (bedingt — wenn ja, verpflichtend) |
| EU-Finanzdienstleistungen | DORA (bedingt — wenn ja, verpflichtend) |
| Entwicklung/Betrieb von KI-Systemen mit EU-Wirkung | EU AI Act (bedingt — wenn ja, verpflichtend) |
| US-Bundesverträge | FISMA/FedRAMP (bedingt — wenn ja, verpflichtend) |

**Schritt 3: Anwendbarkeitsfeststellung dokumentieren**

- Regulatory Applicability Matrix erstellen
- Begründung für die Anwendbarkeitsfeststellung dokumentieren
- Verantwortlichkeit zuweisen (Legal, Compliance, ISB, DSB)
- Jährlich oder bei Geschäftsänderungen aktualisieren

**Hinweis**: Dieser Bewertungsprozess identifiziert **welche Verordnungen gelten**, nicht wie Compliance umgesetzt oder verifiziert wird. Umsetzung und Verifizierung werden durch separate ISMS-Prozesse adressiert (Risikobewertung, Kontrollumsetzung, Compliance-Monitoring).

## Vorlage für die Regulatory Applicability Matrix

Organisationen sollten eine Regulatory Applicability Matrix führen:

| Verordnung | Tier | Status | Auslöser | Verantwortlich | Zuletzt geprüft | Geprüft von | Genehmigt von |
|-----------|------|--------|----------|---------------|-----------------|-------------|---------------|
| Swiss FADP | 1 — Mandatory | Anwendbar | Schweizer Betrieb | DSB | [Date] | [DSB Name] | [Exec Mgmt] |
| EU GDPR | 1 — Mandatory | Anwendbar | EU-Kundendaten | DSB | [Date] | [DSB Name] | [Exec Mgmt] |
| ISO 27001 | 1 — Mandatory | Anwendbar | Zertifizierungsziel | ISB | [Date] | [ISB Name] | [Exec Mgmt] |
| DORA | 2 — Conditional | Nicht anwendbar | Kein Finanzunternehmen | N/A | [Date] | [ISB/Legal] | [ISB] |
| PCI DSS v4.0.1 | 2 — Conditional | Anwendbar | Kartenverarbeitung | ISB | [Date] | [ISB Name] | [Exec Mgmt] |
| EU AI Act | 2 — Conditional | [Zu bewerten] | Entwicklung/Betrieb von KI-Systemen mit EU-Wirkung | ISB | [Date] | [ISB/Legal] | [TBD] |
| NIST SP 800-53 | 3 — Informational | Nur Referenz | Technische Orientierung | ISB | [Date] | [ISB Name] | [ISB] |

## Wann neu bewerten

**Auslöseereignisse für Neubewertung**:

- Neue Geschäftslinie oder Dienstleistungsangebot
- Expansion in neue geografische Märkte
- Akquisition oder Fusion
- Neue Kundenverträge mit regulatorischen Anforderungen
- Regulatorische Änderungen (neue Gesetze, aktualisierte Standards)
- Änderungen des Zertifizierungsumfangs (ISO-27001-Erweiterung)

**Häufigkeit**: Jährliches Minimum + anlassbezogene Neubewertungen

**Verantwortlichkeit**: ISB + Legal/Compliance + DSB (vierteljährliches Monitoring), Genehmigung der Geschäftsleitung (jährliche Gesamtüberprüfung)

## Monitoring-Ansatz für bedingte Verordnungen

Organisationen sollten ein systematisches Monitoring für bedingte Tier-2-Verordnungen einrichten, um Anwendbarkeitsauslöser frühzeitig zu erkennen:

| Verordnung | Monitoring-Methode | Häufigkeit | Verantwortlich |
|-----------|-------------------|-----------|---------------|
| **DORA** | Kundenverträge auf DORA-Compliance-Klauseln prüfen; überwachen, ob Kunden zu DORA-regulierten Finanzunternehmen werden | Vierteljährlich (bei Kundenvertragsprüfungen) | ISB + Legal |
| **NIS2** | Geschäftsentwicklungspläne auf Expansion in erfasste Sektoren (Energie, Verkehr, digitale Infrastruktur) überwachen; nationale NIS2-Gesetze der EU-Mitgliedstaaten verfolgen | Vierteljährlich (Geschäftsstrategie-Reviews) + Ad-hoc (nationale Gesetzesveröffentlichungen) | ISB + Legal |
| **FINMA** | Geschäftsentwicklung auf Anträge für Finanzdienstleistungslizenzen überwachen; prüfen, ob Dienstleistungen an FINMA-regulierte Einrichtungen erbracht werden (Outsourcing-Regelungen könnten greifen) | Vierteljährlich (Geschäftsstrategie-Reviews) | Legal + ISB |
| **PCI DSS** | Entscheidungen zur Zahlungsverarbeitung überwachen; Händlerkonten oder Zahlungs-Gateway-Integrationen verfolgen | Vierteljährlich (Finance/Business-Development-Abstimmung) | ISB |
| **EU AI Act** | KI-System-Entwicklungs-/Betriebsentscheidungen überwachen; KI-Tool-Beschaffung verfolgen; prüfen, ob KI-Ausgaben EU-Bürgerinnen und -Bürger betreffen | Vierteljährlich (Technologiestrategie-Reviews) + Ausgelöst (neue KI-Tool-Einführung) | ISB |
| **HIPAA** | Kundendatentypen überwachen; Verarbeitung von US-Gesundheitsdaten verfolgen | Vierteljährlich (Datenverarbeitungs-Inventurprüfungen) | DSB + ISB |

**Eskalation:** Bei erkanntem wahrscheinlichem Anwendbarkeitsauslöser → Detaillierte Bewertung gemäss Abschnitt 5 innerhalb von 30 Tagen einleiten → Abschnitt-8-Matrix aktualisieren → Geschäftsleitung informieren bei Tier-2-zu-Tier-1-Übergang.

**Monitoring der regulatorischen Umsetzungszeitpläne:** Das vierteljährliche Monitoring soll Appendix A (Regulatory Implementation Timelines) heranziehen, um bevorstehende Compliance-Fristen für bedingte Verordnungen mit stufenweiser Umsetzung (DORA, EU AI Act, PCI DSS v4.0.1, nationale NIS2-Gesetze) vorwegzunehmen.

**Behandlung von Fehlalarmen:**

Wenn das Monitoring einen potenziellen Anwendbarkeitsauslöser erkennt, die detaillierte Bewertung (gemäss Abschnitt 5) aber ergibt, dass die Verordnung **nicht anwendbar** ist:

- Bewertung im **Triggered Assessment Register** dokumentieren
- Festhalten: Erkannter Auslöser, durchgeführte Bewertung, Schlussfolgerung (nicht anwendbar), Begründung
- Für Audit-Trail aufbewahren (zeigt, dass Monitoring funktioniert — nicht jeder Auslöser bedeutet Anwendbarkeit)
- Beispiel: „Kundenvertrag erwähnte DORA. Bewertung: Kunde ist kein DORA-reguliertes Unternehmen, Vertragsklausel ist allgemeine Sicherheitsanforderung, kein DORA-spezifisches Erfordernis. DORA bleibt nicht anwendbar."

---

# Verwendung in ISMS-Richtlinien

## Standard-Referenzsprache

Alle ISMS-Richtlinien MÜSSEN eine der folgenden Formulierungen enthalten:

**Option A: Abschnitt-1.3-Referenz** (empfohlen für die meisten Richtlinien):

```markdown
## Anwendbarkeit regulatorischer Rahmenwerke

Verweise auf Standards, Rahmenwerke und Verordnungen in diesem ISMS
werden gemäss ISMS-POL-00 (Regulatory Applicability Framework) kategorisiert:

**Pflichtige Compliance:**

- Swiss Federal Data Protection Act (FADP)
- EU GDPR (bei Verarbeitung personenbezogener EU-Daten)
- ISO/IEC 27001:2022
- [Weitere verpflichtende Verordnungen gemäss ISMS-POL-00]

**Informative Referenz / Best-Practice-Ausrichtung:**

- NIST Special Publications (SP 800-Reihe)
- [Weitere Rahmenwerke gemäss ISMS-POL-00]

**US-amerikanische Bundesanforderungen:**
US-amerikanische Bundesrahmenwerke (FISMA, FedRAMP, NIST) gelten nur, wenn explizite
vertragliche Verpflichtungen gegenüber dem US-Bund bestehen (siehe ISMS-POL-00,
Abschnitt US-amerikanische Bundesanforderungen).

Für eine vollständige regulatorische Kategorisierung siehe ISMS-POL-00.
```

**Option B: Dedizierter Regulatory-Framework-Abschnitt** (für kontrollspezifische Verordnungen):

```markdown
# Regulatorisches Framework

Diese Kontrolle implementiert Anforderungen aus Verordnungen, die gemäss
ISMS-POL-00 (Regulatory Applicability Framework) kategorisiert sind.

## Pflichtige Compliance
[Kontrollspezifische verpflichtende Anforderungen]

## Bedingte Anwendbarkeit
[Kontrollspezifische bedingte Anforderungen]

## Informative Referenz
[Kontrollspezifische Best Practices]

Für eine vollständige regulatorische Kategorisierung siehe ISMS-POL-00.
```

## Audit-Referenzen

**Für interne Audits**:

- Sicherstellen, dass alle ISMS-Richtlinien auf ISMS-POL-00 verweisen
- Bestätigen, dass die Regulatory Applicability Matrix aktuell ist (jährlich geprüft)
- Validieren, dass Anwendbarkeitsfeststellungen eine dokumentierte Begründung haben

**Für externe Audits**:

- ISMS-POL-00 als Grundlagendokument bereitstellen
- Regulatory Applicability Matrix referenzieren
- Jährlichen Neubewertungsprozess und Verantwortlichkeiten nachweisen

## Nachweise für diese Richtlinie

**Stage-1-Nachweise (Dokumentationsprüfung):**
Erforderliche Nachweise, dass diese Richtlinie angemessen dokumentiert und genehmigt ist:

- ✅ Dieses Richtliniendokument (ISMS-POL-00 v1.0)
- ✅ Unterschriften von ISB, Legal/Compliance, DSB, Geschäftsleitung
- ✅ Struktur des Regulatory-Applicability-Frameworks (Tier-1/2/3-Taxonomie definiert)
- ✅ Bewertungsmethodik dokumentiert (Abschnitt 5)
- ✅ Standard-Referenzsprache für ISMS-Richtlinien (Abschnitt 6)

**Stage-2-Nachweise (Operative Wirksamkeit):**
Erforderliche Nachweise, dass diese Richtlinie operativ wirksam ist:

- Regulatory Applicability Matrix mit aktuellem Organisationsstatus befüllt (Abschnitt 8)
- Prüfprotokolle: Vierteljährliche Monitoring-Protokolle, Protokolle der jährlichen Gesamtprüfung
- Anwendbarkeitsfeststellungsdokumente: Begründung für Tier-Zuordnungen (insbesondere Tier-2-Entscheidungen)
- Ausgelöste Bewertungsunterlagen: Auswirkungsbewertungen bei Geschäftserweiterung und regulatorischen Änderungen
- Historische Versionen: Frühere POL-00-Versionen, die die Rahmenwerk-Entwicklung zeigen

**Aktueller operativer Nachweisstatus**: Vierteljährliche Monitoring-Protokolle, ausgelöste Bewertungsunterlagen und der jüngste Prüfnachweis werden gemäss dem im Abschnitt Bewertungsmethodik definierten Format geführt (siehe Aktueller regulatorischer Status → Ausführung der Bewertungsmethodik).

**Erläuterung zu Compliance-Nachweisen:**
Diese Richtlinie legt die regulatorische Anwendbarkeit fest (WELCHE Verordnungen gelten). Sie legt NICHT fest:

- **Nachweise zur Kontrollumsetzung** (adressiert in Annex-A-Kontrolldokumentation)
- **Compliance-KPIs/Dashboards** (adressiert in ISMS-POL-A.5.31-S4 §6)
- **Regulatorische Audit-Feststellungen** (adressiert in Compliance-Monitoring-Prozessen)

Die Grenze lautet: POL-00 identifiziert Verpflichtungen → Risikobewertung priorisiert → Kontrollen setzen um → Separate Prozesse verifizieren Compliance.

---

# Pflege & Aktualisierungen

## Prüfplan

**Vierteljährliche Prüfung** (ISB + Legal + DSB):

- Regulatorische Änderungen überwachen (GDPR-Leitlinienaktualisierungen, neue Richtlinien)
- Organisatorische Änderungen verfolgen (neue Dienstleistungen, neue Märkte)
- Applicability Matrix bei Änderung von Auslösern aktualisieren
- Prüfung im vierteljährlichen ISMS-Review-Meeting dokumentieren

**Jährliche Prüfung** (Genehmigung durch Geschäftsleitung):

- Umfassende Bewertung der regulatorischen Landschaft
- ISMS-POL-00 für neue Verordnungen aktualisieren
- Policy-Referenzsprache bei Bedarf überarbeiten
- Genehmigung der Geschäftsleitung zu Compliance-Verpflichtungen
- Versionskontrolle und Verteilung aktualisieren

**Anlassbezogene Prüfung**:

- Neue Verordnung veröffentlicht (DORA in Kraft, AI Act veröffentlicht)
- Geschäftserweiterung (neues Land, neue Dienstleistung)
- Fusion/Akquisition
- Grosser Vertrag mit neuen regulatorischen Anforderungen

**Verantwortlichkeit**:

- **Regulatorisches Monitoring**: Legal/Compliance Officer (primär), ISB (unterstützend)
- **Anwendbarkeitsbewertung**: ISB + Legal/Compliance + DSB (gemeinsame Verantwortung)
- **Matrix-Aktualisierungen**: ISB (Eigentümer), DSB (Datenschutzverordnungen)
- **Richtlinienaktualisierungen**: ISB (Autor), Geschäftsleitung (Genehmigung)

## Quellen für regulatorisches Monitoring

**Primäre Monitoring-Quellen:**

- **nDSG/FADP**: Website und Leitlinienpublikationen des Eidgenössischen Datenschutz- und Öffentlichkeitsbeauftragten (EDÖB)
- **GDPR**: Leitlinien des European Data Protection Board (EDPB), nationale Datenschutzbehörden, EU-Amtsblatt
- **ISO-Standards**: ISO-Publikationen, BSI-Aktualisierungen (British Standards Institution), Benachrichtigungen von Zertifizierungsstellen
- **DORA/NIS2**: EU-Amtsblatt, ENISA-Publikationen, nationale zuständige Behörden
- **PCI DSS**: PCI Security Standards Council (pcisecuritystandards.org), Updates für teilnehmende Organisationen
- **FINMA**: FINMA-Rundschreiben und Orientierungshilfen (finma.ch)
- **EU AI Act**: EU-Amtsblatt, Publikationen des AI Office, nationale KI-Behörden
- **Rechtsmonitoring**: Externer Rechtsberatungs-Abonnementdienst, internes Monitoring der Rechtsabteilung

**Monitoring-Häufigkeit:** Wöchentlicher Scan regulatorischer Quellen, vierteljährliche Gesamtprüfung

## Kommunikation

**Richtlinienaktualisierungen werden kommuniziert über**:

- Policy-Portal-Aktualisierung
- E-Mail an alle Policy-Eigentümer
- Legal/Compliance-Briefing
- ISB-Briefing an Geschäftsleitung
- Aktualisierung der Schulungsmaterialien (bei wesentlichen Änderungen)

**Benachrichtigte Stakeholder**:

- Alle ISMS-Policy-Autoren (unmittelbare Auswirkung)
- System-Owner (Auswirkung auf Kontroll-Scoping)
- Interne Revision (Auditplanung)
- Externe Auditoren (Zertifizierungsumfang)

## Versionskontrolle

**Hauptversion (X.0)**:

- Neue verpflichtende Verordnungen hinzugefügt (Tier-1-Änderungen)
- Tier-Änderungen (informativ → verpflichtend)
- Strukturelle Änderungen am Framework
- Entfernung von Verordnungen (nicht mehr anwendbar)

**Nebenversion (X.Y)**:

- Klarstellungen zu bestehenden Verordnungen
- Zusätzliche informative Rahmenwerke (Tier 3)
- Referenzaktualisierungen (NIST-Publikationsversionen, GDPR-Leitlinien)
- Nicht-strukturelle Verbesserungen

---

# Verknüpfte Dokumente

**Interne Referenzen**:

- Alle ISMS-Richtlinien (ISMS-POL-A.X.XX-Reihe)
- ISMS-Risikobewertungsmethodik (Clause 6)
- ISMS Statement of Applicability (Annex-A-Scoping)
- ISMS-Compliance-Monitoring-Prozesse

**Externe Referenzen**:

- Swiss Federal Data Protection Act (SR 235.1)
- EU GDPR (Regulation 2016/679)
- ISO/IEC 27001:2022
- NIST Special Publications (nist.gov)
- PCI DSS v4.0.1 (pcisecuritystandards.org)
- DORA (Regulation 2022/2554)
- NIS2 (Directive 2022/2555)

---

# Aktueller regulatorischer Status

**Status der Anwendbarkeitsbewertung (Stand [Date]):**

Dieser Abschnitt dokumentiert die aktuellen regulatorischen Compliance-Verpflichtungen der Organisation, wie durch die in Abschnitt 5 definierte Bewertungsmethodik festgestellt.

## Tier 1: Pflichtige Compliance (Aktiv)

| Verordnung | Begründung der Anwendbarkeit | Umsetzungsstatus | Nächste Prüfung |
|-----------|------------------------------|-----------------|----------------|
| **Swiss FADP (nDSG)** | ✅ Anwendbar — Schweizer Organisation mit Schweizer Betrieb und Mitarbeitenden | Kontrollen gemäss Annex A umgesetzt (A.5.12-14 Datenschutz, A.5.34 Privacy Protection) | [Date + 12 Monate] |
| **EU GDPR** | ✅ Anwendbar — Verarbeitung personenbezogener Daten von EU-Bürgerinnen und -Bürgern durch Kundenbeziehungen | Kontrollen gemäss Annex A umgesetzt (A.5.34, A.8.11 Data Masking, A.8.10 Information Deletion) | [Date + 12 Monate] |
| **ISO/IEC 27001:2022** | ✅ Anwendbar — Zertifizierung angestrebt (Zertifizierungsziel im ISMS-Scope dokumentiert) | 48 von 93 Kontrollen umgesetzt (52 %), Stage-1-Readiness erreicht, Stage-2-Vorbereitung läuft | Kontinuierlich (Zertifizierungspflege) |

## Tier 2: Bedingte Anwendbarkeit

### Derzeit nicht anwendbar (unter Monitoring)

| Verordnung | Bewertungsstatus | Aktuelle Entscheidung | Monitoring-Auslöser | Verantwortlich | Zuletzt bewertet |
|-----------|-----------------|----------------------|--------------------|--------------|--------------------|
| **DORA** | ✅ Bewertet | **Nicht anwendbar** — Organisation ist weder EU-Finanzunternehmen noch als kritischer IKT-Dienstleister für Finanzunternehmen eingestuft | Geschäftsmodellwechsel (Eintritt Finanzdienstleistungen), Kundenverträge mit DORA-Compliance-Pflicht | ISB + Legal | [Date] |
| **NIS2** | ✅ Bewertet | **Nicht anwendbar** — Organisation ist keine wesentliche/wichtige Einrichtung in erfassten Sektoren (Energie, Verkehr, Banken, Gesundheit, digitale Infrastruktur) | Expansion in NIS2-erfasste Sektoren, Einstufung als wesentliche/wichtige Einrichtung | ISB + Legal | [Date] |
| **PCI DSS v4.0.1** | ✅ Bewertet | **Nicht anwendbar** — Organisation speichert, verarbeitet oder überträgt derzeit keine Zahlungskarteninhaberdaten | Geschäftsentscheidung zur Kartenakzeptanz, Einrichtung eines Händlerkontos | ISB | [Date] |
| **FINMA** | ✅ Bewertet | **Nicht anwendbar** — Organisation hält keine FINMA-Lizenz (keine Schweizer Bank, kein Effektenhändler, keine Versicherung, kein regulierter Finanzmarktinfrastrukturbetreiber) | Erwerb einer Finanzdienstleistungslizenz, Dienstleistungserbringung für FINMA-regulierte Einrichtungen | Legal + ISB | [Date] |

### Unter Bewertung (Entscheidung ausstehend)

| Verordnung | Bewertungsstatus | Erwarteter Abschluss | Vorläufige Erkenntnisse | Verantwortlich |
|-----------|-----------------|---------------------|------------------------|---------------|
| **EU AI Act** | 🔄 In Bearbeitung | TBD — ausstehend bis zur Veröffentlichung der delegierten Rechtsakte des EU AI Act (Ziel Q2 2026; siehe nachstehende Bewertungsschritte) | Organisation nutzt KI-Tools (GitHub Copilot für Entwicklungsunterstützung, potenzielle zukünftige KI-gestützte Sicherheitstools). Bewertungsschwerpunkt: Sind diese Systeme „KI-Systeme" im Sinne von Artikel 3? Falls ja, Risikoklassifizierung gemäss Anhang III. **Zusammenspiel mit GDPR Artikel 22:** Wenn KI-Systeme automatisierte Entscheidungen mit rechtlichen/erheblichen Auswirkungen auf Einzelpersonen umfassen (GDPR Art. 22), gelten zusätzliche Anforderungen (Recht auf menschliche Überprüfung, Transparenz, Datenschutz-Folgenabschätzung). Vorläufig: Wahrscheinlich **minimales Risiko** (Tier 3) oder **begrenztes Risiko** (nur Transparenzpflichten). **Empfehlung:** Detaillierte Bewertung bis [Date] abschliessen, in ISMS-REF-AI-ACT dokumentieren sofern Pflichten bestehen. | ISB + Legal |

**Bisherige Bewertungsliefergegenstände:**
- [Date]: KI-System-Inventar abgeschlossen (dokumentiert in ISMS-REF-AI-ACT-INVENTORY)
  - GitHub Copilot (Code-Generierung, als minimales Risiko bewertet)
  - [Weitere Tools sofern zutreffend]
- [Date]: Analyse der Überschneidung mit GDPR Artikel 22 abgeschlossen (keine automatisierten Entscheidungen mit rechtlichen/erheblichen Auswirkungen identifiziert)
- **Nächster Liefergegenstand:** Risikoklassifizierungsbericht fällig [Date + 2 Wochen]

**Bewertungsansatz für EU AI Act:**
1. **KI-Nutzung inventarisieren** (Fällig: [Date + 2 Wochen])

   - GitHub Copilot (Code-Generierungsassistent)
   - [Weitere KI-Tools aufführen, sofern vorhanden]

2. **Analyse der Überschneidung mit GDPR Artikel 22** (Fällig: [Date + 2 Wochen])
   - Für jedes KI-System prüfen: Trifft es automatisierte Entscheidungen mit rechtlichen oder ähnlich erheblichen Auswirkungen auf Einzelpersonen?
   - Beispiele, die GDPR Art. 22 auslösen:
     - Automatisiertes Bewerbungs-Screening (Auswirkung auf Beschäftigung)
     - Automatisierte Zugangskontrollentscheidungen (Auswirkung auf Dienstleistungsverweigerung)
     - Automatisierte Klassifizierung von Sicherheitsvorfällen (betrifft Datenschutzrechte von Einzelpersonen)
   - Wenn ja → GDPR Art. 22-Anforderungen gelten (Recht auf menschliche Überprüfung, Transparenz, DPIA)
   - Überschneidung in ISMS-REF-AI-ACT-Bewertung dokumentieren

3. **Risikoklassifizierung gemäss AI-Act-Anhang III** (Fällig: [Date + 4 Wochen])

   - Gegen Hochrisikokategorien prüfen (Beschäftigung, Kreditbewertung, Biometrie, kritische Infrastruktur, Strafverfolgung)
   - Vorläufige Einschätzung: Keine der aktuellen KI-Nutzungen fällt unter Hochrisikokategorien

4. **Entscheidung dokumentieren** (Fällig: [Date + 6 Wochen])

   - Bei minimalem/begrenztem Risiko → Tier 3 (Informational) mit Transparenzpflichten
   - Bei hohem Risiko → Tier 2 (Conditional → Mandatory bei Bestätigung)
   - ISMS-REF-AI-ACT erstellen, wenn Pflichten identifiziert

## Tier 3: Informative Referenz (Aktiv in Verwendung)

| Rahmenwerk | Nutzung | Referenziert in | Begründung |
|-----------|---------|----------------|-----------|
| **NIST SP 800-Reihe** | Technische Implementierungsanleitung | Mehrere Annex-A-Kontrollen (A.8.8 Vulnerability Management referenziert NIST SP 800-40, A.5.24-28 Incident Response referenziert NIST SP 800-61) | Branchenübliche technische Orientierung für Kontrollumsetzung |
| **CIS Controls v8.1** | Sicherheits-Benchmarking | Interne Sicherheitspositionsbewertung, Kontroll-Gap-Analyse | Weitgehend anerkannte Sicherheitsbasis zum Vergleich |
| **OWASP** | Sichere Entwicklungspraktiken | A.8.25-28 Secure Development Lifecycle | Best Practices für Webanwendungssicherheit |
| **ISO/IEC 27002:2022** | Kontrollumsetzungsanleitung | Alle Annex-A-Kontrollen | Offizielle Implementierungsanleitung für ISO-27001-Kontrollen |

## Ausführung der Bewertungsmethodik

**Jährliche Gesamtprüfung:**

- **Geplant:** Jährlich im Q4 (Dezember)
- **Teilnehmende:** ISB (Leitung), Legal Counsel, DSB, Compliance Officer
- **Liefergegenstand:** Aktualisierter Abschnitt 8 + Briefing der Geschäftsleitung
- **Genehmigung:** Geschäftsleitung

**Vierteljährliche Monitoring-Prüfung:**

- **Geplant:** Ende jedes Quartals (März, Juni, September, Dezember)
- **Teilnehmende:** ISB, Legal, DSB
- **Schwerpunkt:** Erkannte regulatorische Änderungen, geschäftliche Auslöseereignisse, Statusaktualisierungen zu bedingten Verordnungen
- **Liefergegenstand:** Regulatorisches Monitoring-Protokoll, Auslöseereignis-Bewertungen

**Inhalte des regulatorischen Monitoring-Protokolls:**
- Datum der Prüfung
- Erkannte regulatorische Änderungen (neue Gesetze, Leitlinienaktualisierungen, Durchsetzungsmassnahmen)
- Organisatorische Auslöseereignisse (neue Dienstleistungen, Markterweiterung, Kundenverträge)
- Auswirkungsbewertung auf Anwendbarkeit (betrifft die Änderung den Tier-1/2/3-Status?)
- Erforderliche Massnahmen (POL-00 aktualisieren, detaillierte Bewertung einleiten, keine Massnahme)
- Unterschriften der Prüfenden (ISB, Legal, DSB)

**Protokollformat und -ablage:**
- Format: Strukturierte Tabelle oder GRC-Plattform-Einträge
- Ablage: Excel-Register unter [SharePoint]/ISMS/Compliance/POL-00-Monitoring.xlsx (Übergangslösung; bis [date] auf GRC-Plattform zu migrieren)
- Aufbewahrung: Mindestens 3 Jahre (umfasst vollständigen Zertifizierungszyklus)
- Zugang: ISB, Legal, DSB, Interne Revision, Externe Auditoren

**Mindestfelder:**

| Feld | Beschreibung | Beispiel |
|------|-------------|---------|
| Prüfdatum | Vierteljährliches Monitoring-Datum | 2024-12-31 |
| Teilnehmende | Namen und Unterschriften | [ISB], [Legal], [DSB] |
| Regulatorische Änderungen | Erkannte neue Gesetze/Leitlinien | Delegierte Rechtsakte des EU AI Act veröffentlicht |
| Auslöseereignisse | Geprüfte Geschäftsänderungen | Keine / Neuer Kundenvertrag mit FINMA-Compliance-Pflicht |
| Auswirkung auf Anwendbarkeit | Tier-Änderungen | Keine / FINMA Tier 2 → Tier 1 aufgrund Kundenvertrag |
| Erforderliche Massnahmen | Folgeaufgaben | Keine / FINMA-Compliance-Bewertung einleiten |
| Nächstes Prüfdatum | Vierteljährlicher Turnus | 2025-03-31 |

**Nachweise zur Ausführung des regulatorischen Monitorings:**
Vierteljährliche Monitoring-Protokolle werden in [GRC-Plattform / Compliance-Register] geführt mit:
- Monitoring-Datum und Teilnehmende (Unterschriften von ISB, Legal, DSB)
- Erkannte regulatorische Änderungen (keine/Liste mit Auswirkungsbewertung)
- Geprüfte Auslöseereignisse (Geschäftserweiterungen, Kundenverträge)
- Entscheidungen zur Neubewertung der Anwendbarkeit (Tier-Änderungen dokumentiert)
- Eskalationsunterlagen (bei erkanntem Tier-2-zu-Tier-1-Übergang)

**Jüngste Nachweise:**
- Q4 2024 Monitoring-Protokoll: [Date], geprüft von [ISB/Legal/DSB], keine Tier-Änderungen
- Jährliche Prüfung 2024: [Date], genehmigt von Geschäftsleitung, POL-00 v1.0 veröffentlicht
- EU AI Act-Bewertung: [Date] Schritt 1 abgeschlossen (KI-Inventar dokumentiert in [Ablageort])

**Triggered Assessment Register:**
Wird unter [Ablageort] geführt mit:
- Beschreibung des Auslöseereignisses (Kundenvertrag, regulatorische Änderung, Geschäftserweiterung)
- Bewertungsdatum und Bewerter
- Anwendbarkeitsfeststellung (Anwendbar / Nicht anwendbar / Weitere Bewertung erforderlich)
- Begründung (dokumentierte Rechtfertigung der Feststellung)
- Ergriffene Massnahmen (Tier-Änderung, Kontrollumsetzung, keine Massnahme erforderlich)
- Genehmigungsstelle (ISB, Legal, Geschäftsleitung bei Tier-Änderung)

**Aufbewahrt in:** [Compliance-System — z. B. GRC-Plattform, Dokumentenablage]

**Ausgelöste Bewertungen:**

- Geschäftserweiterung (neue Märkte, Dienstleistungen)
- Kundenvertragsanforderungen (explizite regulatorische Verpflichtungen)
- Regulatorische Veröffentlichungen (neue Gesetze, Durchsetzungsleitlinien)
- **Aktuelles Beispiel:** EU AI Act am 1. August 2024 in Kraft getreten → Ausgelöste Bewertung (derzeit in Bearbeitung gemäss Abschnitt 8.2.2)

**Nächste geplante Aktivitäten:**

- **[Date + 2 Wochen]:** EU AI Act-Bewertung abschliessen (Schritt 1: KI-Nutzungsinventar)
- **Q4 [Jahr]:** Jährliche Gesamt-Regulierungsüberprüfung
- **[Date + 12 Monate]:** Anwendbarkeitsbestätigung für FADP/GDPR

## Detaillierte Anforderungsreferenzen

Für bedingte Verordnungen mit komplexen Anforderungen (unabhängig vom aktuellen Anwendbarkeitsstatus) führt die Organisation detaillierte Anforderungsreferenzdokumente für zukünftige Anwendbarkeitsszenarien und Bereitschaft.

| Verordnung | Referenzdokument | Zweck | Pflegestatus | Zuletzt aktualisiert | Nächste Prüfung |
|-----------|-----------------|-------|-------------|---------------------|----------------|
| **DORA** | ISMS-REF-DORA — Digital Operational Resilience Act Requirements Reference | Detaillierte IKT-Risikomanagement-, Vorfallmeldungs-, Resilienztest- und Drittparteienrisiko-Anforderungen gemäss DORA-Artikeln 3–49. Wird für zukünftige Anwendbarkeitsbewertung gepflegt, falls Organisation in EU-Finanzdienstleistungen einsteigt. | Gepflegt (aktualisiert bei Veröffentlichung technischer DORA-Regulierungsstandards) | [Date DORA RTS geprüft] | Jährlich oder bei DORA-RTS-Aktualisierungen |
| **FINMA** | ISMS-REF-FINMA — FINMA Circular 2023/1 Requirements Reference | Anforderungen zur operationellen Resilienz und zum Outsourcing für Schweizer Finanzinstitute. Wird für zukünftige Anwendbarkeit gepflegt, falls Organisation FINMA-Lizenz erwirbt oder FINMA-regulierten Kunden dient. | Gepflegt (aktualisiert gemäss FINMA-Rundschreibenrevisionen) | [Date Rundschreiben 2023/1 geprüft] | Jährlich oder bei FINMA-Rundschreiben-Revisionen |
| **NIS2** | ISMS-REF-NIS2 — Network and Information Security Directive 2 Requirements Reference | Anforderungen an Cybersicherheits-Risikomanagement, Vorfallmeldung, Lieferkettensicherheit und Governance gemäss NIS2-Artikeln 20–23. Wird für zukünftige Anwendbarkeit gepflegt, falls Organisation als wesentliche/wichtige Einrichtung eingestuft wird. | Gepflegt (aktualisiert bei Umsetzung von NIS2 in nationales Recht durch EU-Mitgliedstaaten) | [Date nationale NIS2-Gesetze geprüft] | Halbjährlich (Monitoring der nationalen Umsetzung) |
| **PCI DSS v4.0.1** | ISMS-REF-PCI-DSS — Payment Card Industry Data Security Standard Requirements Reference | 12 PCI-DSS-v4.0.1-Anforderungen für Netzwerksicherheit, Datenschutz, Schwachstellenmanagement, Zugriffskontrolle, Monitoring und Tests. Wird für zukünftige Anwendbarkeit gepflegt, falls Organisation beginnt Zahlungskarten zu verarbeiten. | Gepflegt (aktualisiert gemäss PCI-SSC-Veröffentlichungen, derzeit v4.0 gültig ab März 2024) | [Date v4.0.1 eingearbeitet] | Jährlich oder bei PCI-SSC-Aktualisierungen |
| **EU AI Act** | ISMS-REF-EU-AI-ACT — EU Artificial Intelligence Act Requirements Reference | Risikobasiertes KI-Governance-Framework für verbotene Praktiken (Artikel 5), Hochrisiko-KI-Systeme (Artikel 9–72), Transparenzpflichten bei begrenztem Risiko (Artikel 50) und Anforderungen an KI-Modelle mit allgemeinem Verwendungszweck (Artikel 53–54). Wird für zukünftige Anwendbarkeit gepflegt, falls Organisation KI-Systeme entwickelt oder betreibt, die EU-Bürgerinnen und -Bürger betreffen. | In Entwicklung (aktualisiert bei Veröffentlichung delegierter und durchführender Rechtsakte des EU AI Act, stufenweise Umsetzung 2025–2028) | [Date Erstentwurf] | Bei Veröffentlichung delegierter Rechtsakte des AI Act |

**Begründung für die Pflege von Anforderungsreferenzen für „nicht anwendbare" Verordnungen:**

1. **Bereitschaft:** Bei Änderung des Geschäftskontexts (z. B. Erwerb einer Finanzdienstleistungslizenz, Eintritt in NIS2-erfasste Sektoren, Aufnahme der Kartenverarbeitung) kann die Organisation rasch Gap- und Umsetzungsaufwand bewerten.

2. **Kunden-Due-Diligence:** Kunden können auch bei aktuell nicht anwendbaren bedingten Verordnungen Bereitschaftsnachweise verlangen (z. B. „Falls wir künftig PCI-DSS-v4.0.1-Compliance verlangen, können Sie diese erreichen?").

3. **Regulatorisches Monitoring:** Die Pflege von Anforderungsreferenzen ermöglicht proaktives Monitoring von regulatorischen Änderungen, die zukünftige Anwendbarkeit beeinflussen könnten (z. B. technische DORA-Standards, nationale NIS2-Umsetzungen, PCI-DSS-v4.0.1-Versionsaktualisierungen).

4. **Effizienz bei der Kontroll-Abbildung:** Anforderungsreferenzen erleichtern die Abbildung bedingter Verordnungen auf bestehende ISO-27001-Annex-A-Kontrollen und zeigen Überschneidungen und potenzielle Wiederverwendung (z. B. „Falls DORA gilt, schätzen wir, dass 70 % der Anforderungen bereits durch bestehende Kontrollen abgedeckt sind").

5. **Strategische Planung:** Die Geschäftsleitung kann fundierte Entscheidungen zum Eintritt in regulierte Märkte treffen, indem sie den erforderlichen Compliance-Aufwand versteht.

**Zugang und Verwendung:**

- **ISMS-REF-XXX-Dokumente sind KEINE verpflichtenden Compliance-Materialien** (Verordnungen sind Tier 2 — Nicht anwendbar).
- **Zweck:** Strategische Bereitschaft, Kundenanfragen, Business-Development-Due-Diligence.
- **Prüfzyklus:** Jährliche Prüfung im Rahmen der POL-00-Prüfung (Vergewissern, dass Verordnung sich nicht geändert hat und Bewertung nicht veraltet ist).
- **Eigentümerschaft:** ISB (pflegt technische Anforderungen), Legal (pflegt rechtliche Interpretation und Anwendbarkeitsauslöser).

**Hinweis für Auditoren:**
Die Pflege von Anforderungsreferenzen für nicht anwendbare Verordnungen ist ein **Reifeindikator**, der proaktives Compliance-Management demonstriert — kein Anzeichen für Scope-Creep. ISO 27001 Clause 4.1 (Understanding the organisation and its context) fördert das Verständnis sowohl aktueller als auch potenzieller zukünftiger Compliance-Verpflichtungen.

---

# Glossar

| Begriff | Definition |
|---------|-----------|
| **Applicable (Anwendbar)** | Verordnung gilt für Organisation aufgrund von Geschäftsaktivitäten, Compliance erforderlich |
| **Conditional (Bedingt)** | Verordnung gilt nur, wenn spezifische Auslöser erfüllt sind (Branche, Geografie, Datentyp) |
| **Mandatory (Verpflichtend)** | Rechtliche Verpflichtung, durch Gesetz oder Vertrag durchsetzbar, Nicht-Einhaltung hat Konsequenzen |
| **Informational (Informativ)** | Referenz für Best Practices, nicht rechtlich durchsetzbar, freiwillige Übernahme |
| **Tier 1** | Pflichtige Compliance (rechtlich, vertraglich) |
| **Tier 2** | Bedingte Compliance (kontextabhängig) |
| **Tier 3** | Informative Referenz (Best Practice, freiwillig) |
| **Binding Force (Bindungswirkung)** | Rechtliche oder vertragliche Durchsetzbarkeit einer Verordnung |
| **Implementation Obligation (Umsetzungspflicht)** | Anforderung zur Umsetzung spezifischer Kontrollen (festgestellt durch Risikobewertung) |
| **Regulatory Monitoring (Regulatorisches Monitoring)** | Systematische vierteljährliche Überprüfung regulatorischer Änderungen und organisatorischer Auslöseereignisse zur Erkennung von Anwendbarkeitsänderungen bei bedingten Tier-2-Verordnungen |
| **Applicability Trigger (Anwendbarkeitsauslöser)** | Ereignis oder Bedingung, die eine bedingte Verordnung (Tier 2) verpflichtend macht (Tier 1) und eine Übergangs- und Compliance-Umsetzungsbewertung erfordert |
| **Triggered Assessment (Ausgelöste Bewertung)** | Ungeplante Regulierungsanwendbarkeitsbewertung, ausgelöst durch Erkennung eines Anwendbarkeitsauslösers (z. B. Geschäftserweiterung, Kundenvertrag, regulatorische Änderung) |

---

# Anhang A: Regulatorische Umsetzungszeitpläne

**Verordnungen mit stufenweiser Umsetzung (für Monitoring):**

| Verordnung | Wesentliche Umsetzungsdaten | Organisatorische Relevanz |
|-----------|---------------------------|--------------------------|
| **DORA** | **17. Januar 2025:** Vollständige Anwendung für Finanzunternehmen | Überwachen: Falls Organisation vor 2025-01-17 EU-Finanzunternehmen oder kritischer IKT-Dienstleister wird, gilt DORA sofort als Tier 1 |
| **EU AI Act** | **2. Februar 2025:** Verbote (KI mit inakzeptablem Risiko)<br>**2. August 2025:** Pflichten für KI-Modelle mit allgemeinem Verwendungszweck<br>**2. Dezember 2027:** Hochrisiko-KI-Systeme (verschoben vom 2. August 2026 durch den Digital Omnibus, Verordnung (EU) 2026/1744, in Kraft seit 27. Juli 2026)<br>**2. August 2028:** Hochrisiko-KI in regulierten Produkten (verschoben vom 2. August 2027 durch denselben Digital Omnibus)<br>**2. August 2030:** Übergangsfrist für bestehende Systeme bei Behörden endet (unverändert) | Überwachen: Falls Organisation KI-Systeme entwickelt oder betreibt, die EU-Bürgerinnen und -Bürger betreffen → Compliance bis zur anwendbaren Frist erforderlich. Bestehende Systeme haben eine Übergangsfrist bis zum jeweils anwendbaren Datum oben (Dezember 2027 / August 2028); für von Behörden genutzte Systeme gilt unverändert die Übergangsfrist bis 2030, sofern nicht wesentlich geändert |
| **PCI DSS v4.0.1** | **31. März 2024:** v4.0 gültig (v3.2.1 eingestellt)<br>**31. März 2025:** Neue Anforderungen (in v4.0 als „zukünftig datiert" markiert) werden verpflichtend | Derzeit nicht anwendbar. Falls Zahlungskartenverarbeitung beginnt → v4.0-Anforderungen gelten sofort (v3.2.1 eingestellt). Zukünftig datierte Anforderungen (MFA-Erweiterung, kryptographische Verbesserungen, Anti-Phishing) ab März 2025 verpflichtend |
| **NIS2** | **17. Oktober 2024:** EU-Mitgliedstaaten müssen in nationales Recht umsetzen<br>**2024–2025:** Nationale Umsetzungen variieren je Mitgliedstaat<br>**Variiert nach Mitgliedstaat:** Anwendungsdaten hängen von nationalem Umsetzungsgesetz ab | Überwachen: Nationale Umsetzungen können Anwendbarkeitsfeststellung beeinflussen, falls Organisation in mehreren EU-Mitgliedstaaten tätig ist. Nationale Cybersicherheitsbehörde für spezifische Inkraftretensdaten konsultieren |

---

# Schlussaussage

Diese Richtlinie begründet die regulatorische Anwendbarkeit für das Informationssicherheits-Managementsystem der Organisation.

**Was diese Richtlinie festlegt:**

- Identifizierung anwendbarer Verordnungen (verpflichtend, bedingt, informativ)
- Bewertungsmethodik zur Feststellung der regulatorischen Anwendbarkeit
- Überprüfungs- und Aktualisierungsprozesse für Änderungen der regulatorischen Landschaft

**Was diese Richtlinie NICHT festlegt:**

- Risikobehandlungsentscheidungen (adressiert in Clause 6 — Risikomanagement)
- Anforderungen zur Kontrollumsetzung (adressiert in Annex-A-Kontrollen)
- Compliance-Status oder -Verifizierung (adressiert in Compliance-Monitoring-Prozessen)

**Aufgabentrennung:**

- **Diese Richtlinie (POL-00)**: Definiert WELCHE Verordnungen gelten
- **Risikomanagement (Clause 6)**: Bestimmt WIE auf regulatorische Anforderungen reagiert wird
- **Kontrollumsetzung (Annex A)**: Setzt SPEZIFISCHE Kontrollen um
- **Compliance-Monitoring**: Verifiziert und verfolgt den COMPLIANCE-STATUS

---

**ENDE VON ISMS-POL-00**

*„Regulatorische Anwendbarkeit ist das Fundament. Umsetzung und Compliance sind das darauf errichtete Bauwerk."*

<!-- QA_VERIFIED: 2026-07-31 -->
