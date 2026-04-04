<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S1-DE:framework:POL:a.5.19-23-s1 -->
**ISMS-POL-A.5.19-23-S1 — Grundlagen der Lieferantenbeziehungen**
**Massnahme A.5.19: Informationssicherheit in Lieferantenbeziehungen**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Grundlagen der Lieferantenbeziehungen |
| **Dokumenttyp** | Richtlinienabschnitt |
| **Dokument-ID** | ISMS-POL-A.5.19-23-S1 |
| **Dokumentersteller** | Information Security Officer (ISO) |
| **Dokumenteigentümer** | Informationssicherheitsbeauftragter (ISB) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Zu bestimmen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISO | Erstfassung für ISO 27001:2022 Massnahme A.5.19 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: Information Security Officer (ISO)
- Compliance: Legal/Compliance Officer
- Einkauf: Einkaufsleitung
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Rahmenwerk zur regulatorischen Anwendbarkeit)
- ISMS-POL-A.5.19-23 (Übergeordnete Richtlinie – Lieferanten- und Cloud-Dienste-Sicherheit)
- ISMS-POL-A.5.19-23-S2 (Anforderungen an Lieferantenvereinbarungen)
- ISMS-IMP-A.5.19-23.S1-UG/TG (Cloud-Dienste-Inventar & Klassifizierung)
- ISMS-REF-A.5.23 (Cloud-Anbieter-Referenzregister)
- ISO/IEC 27001:2022 Massnahme A.5.19
- ISO/IEC 27036-1 (Informationssicherheit in Lieferantenbeziehungen – Überblick und Konzepte)

---

# Zweck

Dieser Abschnitt definiert die grundlegenden Anforderungen für das Management von Informationssicherheitsrisiken in Lieferantenbeziehungen. Er legt das Klassifizierungsrahmenwerk, die Risikobewertungsmethodik und die Due-Diligence-Anforderungen fest, die für alle externen Lieferanten gelten.

**Kritischer Grundsatz – „Kennen Sie Ihre Lieferanten, bevor diese Ihre Daten kennen"**: Lieferantenbeziehungen sollen mit systematischer Risikobewertung und evidenzbasierter Due Diligence beginnen – nicht mit nachträglicher Entdeckung nach Vertragsabschluss. Die Vergabe von Lieferantenzugang ohne Klassifizierung, die Gewährung von Datenzugang ohne Due Diligence oder die Unterzeichnung von Verträgen ohne Sicherheitsbewertung schafft unakzeptable und potenziell nicht wiedergutzumachende Risiken. Die Lieferantenauswahl ist eine Sicherheitsentscheidung, nicht nur eine Einkaufsentscheidung.

**ISO/IEC 27001:2022 Massnahme A.5.19 – Informationssicherheit in Lieferantenbeziehungen**

> *Prozesse und Verfahren sollten definiert und mit Lieferanten vereinbart werden, um Informationssicherheitsrisiken im Zusammenhang mit der Nutzung von Produkten oder Diensten von Lieferanten zu managen.*

**Massnahmenziel**: Sicherstellen, dass Informationssicherheitsrisiken in Lieferantenbeziehungen über den gesamten Beziehungslebenszyklus identifiziert, bewertet und gemanagt werden.

**Zusammenfassung der ISO/IEC 27002:2022-Leitlinien**:

- Lieferantenbeziehungen sollen über definierte Prozesse des gesamten Lebenszyklus gemanagt werden (Auswahl, Onboarding, Betrieb, Beendigung)
- Lieferanten sollen basierend auf Art des Zugangs, Datensensitivität und Servicekritikalität identifiziert und klassifiziert werden
- Due Diligence soll durchgeführt werden, bevor Lieferanten Zugang zu Informationen oder Systemen der [Organisation] erhalten
- Sicherheitsanforderungen an Lieferanten sollen basierend auf Risiko- und Datenklassifizierung definiert werden
- Lieferantenleistung und Sicherheitsstatus sollen während der gesamten Beziehungsdauer überwacht werden
- Lieferantenbeendigungsverfahren sollen für eine sichere Beendigung und Datenrückgabe festgelegt werden
- Shadow IT und nicht genehmigter Lieferanteneinsatz sollen aktiv identifiziert und gemanagt werden
- Lieferantenabhängigkeit und Konzentrationsrisiko sollen für kritische Dienste bewertet werden

---

# Geltungsbereich

## Anwendbare Lieferantentypen

| Lieferantentyp | Beschreibung | Beispiele |
|----------------|-------------|----------|
| **Cloud-Dienstanbieter** | Anbieter von IaaS-, PaaS-, SaaS- und XDR-Diensten | Rechenleistung, Speicher, E-Mail, Sicherheitsplattformen |
| **Managed Service Provider** | Ausgelagerte IT-Operationen und Support | Helpdesk, Netzwerkmanagement, SOC-Dienste |
| **Software-Anbieter** | Anbieter lizenzierter oder abonnierbarer Software | ERP, CRM, Entwicklungswerkzeuge |
| **Hardware-Anbieter** | Anbieter physischer IT-Ausrüstung | Server, Netzwerkgeräte, Endpunkte |
| **Professional Services** | Berater mit System-/Datenzugang | Prüfer, Integratoren, Entwickler |
| **Rechenzentrumsanbieter** | Rechenzentrum- und Hosting-Dienste | Colocation, physische Sicherheit |
| **Telekommunikation** | Netzwerk- und Konnektivitätsanbieter | Internet, WAN, Sprachdienste |

## Ausnahmen

Diese Richtlinie gilt nicht für:

- Lieferanten, die Waren/Dienste ohne Zugang zu Informationen der [Organisation] bereitstellen
- Einmalige Käufe ohne laufende Beziehung
- Einzelne Kunden der Dienste der [Organisation]

---

# Lieferantenklassifizierung

## Klassifizierungskriterien

Lieferanten sollen anhand der folgenden Faktoren klassifiziert werden:

| Faktor | Gewichtung | Bewertungsfragen |
|--------|-----------|------------------|
| **Datenzugang** | Hoch | Auf welche Datenklassifizierungsstufen kann der Lieferant zugreifen? |
| **Systemzugang** | Hoch | Hat der Lieferant Zugang zu Produktionssystemen? |
| **Servicekritikalität** | Hoch | Würde ein Lieferantenausfall den Geschäftsbetrieb beeinträchtigen? |
| **Ersetzbarkeit** | Mittel | Wie leicht kann der Lieferant ersetzt werden? |
| **Integrationstiefe** | Mittel | Wie tief sind die Lieferantendienste integriert? |
| **Regulatorische Auswirkung** | Hoch | Beeinflusst der Lieferant die regulatorische Compliance? |

## Klassifizierungsstufen

### Stufe 1: Kritische Lieferanten

**Kriterien (eines davon löst Stufe 1 aus):**

- Zugang zu eingeschränkten oder vertraulichen Daten
- Direkter Zugang zu Produktionssystemen oder Infrastruktur
- Single Point of Failure für kritische Geschäftsprozesse
- Regulatorische Compliance-Abhängigkeit (DORA kritischer Anbieter, NIS2 wesentlicher Dienst, DSGVO-Auftragsverarbeiter für Hochrisikoverarbeitung)

**Anforderungen:**

- Jährliche Vor-Ort- oder detaillierte Fernbewertung
- Vierteljährliche Leistungs- und Sicherheitsüberprüfungen
- Dokumentierter Business-Continuity-Plan
- Prüfungsrecht verpflichtend
- Executive Sponsor zugewiesen
- SOC 2 Type II oder ISO/IEC 27001-Zertifizierung erforderlich
- Störungsmeldung innerhalb von 4 Stunden
- Sub-Auftragsverarbeiter-Offenlegung und Genehmigung

### Stufe 2: Hochrisikolieferanten

**Kriterien:**

- Zugang zu internen Daten
- Zugang zu Nicht-Produktionssystemen (Entwicklung, Test)
- Wichtige, aber nicht kritische Geschäftsfunktion
- Mehrere Lieferantenoptionen verfügbar
- DSGVO-Auftragsverarbeiter für Standardrisikoverarbeitung

**Anforderungen:**

- Jährliche Sicherheitsbewertung (Fragebogen + Nachweise)
- Halbjährliche Leistungsüberprüfungen
- Business-Continuity-Überlegungen dokumentiert
- Prüfungsrecht empfohlen
- SOC 2 oder ISO/IEC 27001-Zertifizierung erforderlich
- Störungsmeldung innerhalb von 24 Stunden
- Sub-Auftragsverarbeiter-Offenlegung

### Stufe 3: Mittelrisikolieferanten

**Kriterien:**

- Begrenzter Datenzugang (öffentlich oder minimaler interner Zugang)
- Kein direkter Systemzugang
- Unterstützende Geschäftsfunktion
- Leicht ersetzbar
- Keine regulatorische Compliance-Auswirkung

**Anforderungen:**

- Zweijährliche Sicherheitsbewertung
- Jährliche Leistungsüberprüfung
- Standard-Vertragssicherheitsklauseln
- Zertifizierung bevorzugt, wenn Organisationsdaten verarbeitet werden
- Störungsmeldung innerhalb von 72 Stunden

### Stufe 4: Niedrigrisikolieferanten

**Kriterien:**

- Kein Zugang zu Organisationsdaten
- Kein Systemzugang
- Standardisierte Dienste
- Mehrere Alternativen verfügbar
- Keine regulatorische Auswirkung

**Anforderungen:**

- Initiale Due Diligence
- Standardvertragsbedingungen
- Überprüfung bei Vertragsverlängerung

## Klassifizierungsmatrix

```
                    │ Kein System- │ Nicht-Prod.  │ Produktions- │
                    │ zugang       │ zugang       │ zugang       │
────────────────────┼──────────────┼──────────────┼──────────────┤
Eingeschränkte Daten│ Stufe 2      │ Stufe 1      │ Stufe 1      │
Vertrauliche Daten  │ Stufe 2      │ Stufe 1      │ Stufe 1      │
Interne Daten       │ Stufe 3      │ Stufe 2      │ Stufe 2      │
Nur öffentl. Daten  │ Stufe 4      │ Stufe 3      │ Stufe 3      │
Kein Datenzugang    │ Stufe 4      │ Stufe 4      │ Stufe 3      │
```

**Neubewertung der Klassifizierung**: Die Lieferantenklassifizierung soll neu bewertet werden:

- Jährlich für alle Lieferanten
- Bei wesentlicher Änderung des Leistungsumfangs
- Bei Fusion/Akquisition des Lieferanten
- Bei wesentlichem Sicherheitsvorfall
- Bei regulatorischen Geltungsbereichsänderungen (z.B. DORA/NIS2-Anwendbarkeit)

---

# Lieferantenrisikobewertung

## Risikokategorien

| Kategorie | Beschreibung | Bewertungsfokus |
|-----------|-------------|----------------|
| **Vertraulichkeitsrisiko** | Unbefugte Offenlegung von Informationen | Datenhandhabung, Zugriffskontrollen, Verschlüsselung |
| **Integritätsrisiko** | Unbefugte Änderung von Daten/Systemen | Änderungsmanagement, Eingabevalidierung, Qualitätskontrollen |
| **Verfügbarkeitsrisiko** | Dienstunterbrechung oder Datenverlust | Redundanz, Backup, Disaster Recovery, SLA-Verpflichtungen |
| **Compliance-Risiko** | Regulatorische oder vertragliche Verstösse | Zertifizierungen, Auditberichte, Attestierungen, regulatorische Ausrichtung |
| **Konzentrationsrisiko** | Überabhängigkeit von einem einzelnen Lieferanten | Marktaltternativen, Exit-Machbarkeit, Vendor Lock-in |
| **Geopolitisches Risiko** | Jurisdiktions- oder politische Faktoren | Datenresidenz, Rechtsrahmen, US CLOUD Act Exposition |

## Risikobewertungsprozess

**Schritt 1: Informationssammlung**

- Ausfüllen des Lieferantensicherheitsfragebogens
- Dokumentationsprüfung (Zertifizierungen, Richtlinien, Verfahren)
- Analyse technischer Dokumentation (Architektur, Datenflüsse)
- Finanzstabilitätsbewertung (für Stufe-1-Lieferanten)
- Referenzprüfungen bei bestehenden Kunden

**Schritt 2: Risikoidentifikation**

- Lieferantendienste den Risikokategorien zuordnen
- Potenzielle Bedrohungsszenarien pro Kategorie identifizieren
- Vorhandene Kontrollen dokumentieren (lieferantenseitig + organisationsseitig)
- Modell der geteilten Verantwortung bewerten (für Cloud-Dienste)
- Sub-Auftragsverarbeiter- und Lieferketten-Risiken bewerten

**Schritt 3: Risikobewertung**

- Wahrscheinlichkeit und Auswirkung pro Risikokategorie bewerten
- Risikowert pro Kategorie mittels Matrix berechnen (Abschnitt 4.3)
- Gesamtes Lieferantenrisiko-Rating bestimmen
- Mit Risikobereitschaft und -toleranz vergleichen

**Schritt 4: Risikobehandlung**

- **Akzeptieren**: Risiko innerhalb der Toleranz, Akzeptanz mit ISB-Genehmigung dokumentieren
- **Mitigieren**: Zusätzliche Kontrollen erforderlich (Vertragsklauseln, technische Kontrollen, Überwachung)
- **Transferieren**: Versicherungs- oder vertragliche Haftungsregelungen
- **Vermeiden**: Lieferantenbeziehung nicht eingehen

**Schritt 5: Dokumentation**

- Risikobewertungsbericht mit Befunden und Empfehlungen
- Risikobehandlungsplan mit zugewiesenen Verantwortlichkeiten und Fristen
- Genehmigungsnachweise (ISB für hohes/kritisches Risiko)
- Integration in das Lieferantenregister

## Risikobewertung

| Wahrscheinlichkeit | Auswirkung: Gering | Auswirkung: Mittel | Auswirkung: Hoch | Auswirkung: Kritisch |
|--------------------|-------------------|-------------------|-----------------|---------------------|
| **Selten** | 1 | 2 | 3 | 4 |
| **Unwahrscheinlich** | 2 | 4 | 6 | 8 |
| **Möglich** | 3 | 6 | 9 | 12 |
| **Wahrscheinlich** | 4 | 8 | 12 | 16 |
| **Nahezu sicher** | 5 | 10 | 15 | 20 |

**Risiko-Rating-Schwellenwerte:**

- **1–4:** Geringes Risiko → Standardkontrollen, jährliche Überprüfung
- **5–9:** Mittleres Risiko → Erweiterte Kontrollen, halbjährliche Überprüfung
- **10–15:** Hohes Risiko → Wesentliche Kontrollen + ISB-Genehmigung + vierteljährliche Überprüfung
- **16–20:** Kritisches Risiko → Genehmigung durch Geschäftsleitung + kontinuierliche Überwachung + obligatorischer Mitigierungsplan

**Nicht akzeptables Risiko**: Risikopunkte von 16–20 ohne machbare Mitigierung sollen zur Lieferantenablehnung oder Beziehungsbeendigung führen.

---

# Due-Diligence-Anforderungen

## Due Diligence nach Klassifizierungsstufe

| Anforderung | Stufe 1 | Stufe 2 | Stufe 3 | Stufe 4 |
|-------------|---------|---------|---------|---------|
| Sicherheitsfragebogen | ✓ Detailliert | ✓ Standard | ✓ Basis | — |
| Zertifizierungsverifizierung | ✓ Erforderlich | ✓ Erforderlich | ✓ Wenn behauptet | — |
| Prüfung von Richtliniendokumenten | ✓ Erforderlich | ✓ Erforderlich | — | — |
| Technische Bewertung | ✓ Erforderlich | ✓ Risikobasiert | — | — |
| Finanzstabilitätsprüfung | ✓ Erforderlich | ✓ Empfohlen | — | — |
| Referenzprüfungen | ✓ Erforderlich | ✓ Empfohlen | — | — |
| Vor-Ort-Bewertung | ✓ Risikobasiert | — | — | — |
| Prüfung von Penetrationstestergebnissen | ✓ Erforderlich | ✓ Wenn verfügbar | — | — |
| Bewertung von Sub-Auftragsverarbeitern | ✓ Erforderlich | ✓ Wenn anwendbar | — | — |
| Datenverarbeitungsvereinbarung | ✓ Erforderlich | ✓ Erforderlich | ✓ Bei Datenzugang | — |
| Überprüfung der Betriebskontinuität | ✓ Erforderlich | ✓ Erforderlich | ✓ Bei Kritikalität | — |

## Sicherheitszertifizierungen

**Bevorzugte Zertifizierungen (in Präferenzreihenfolge):**

| Zertifizierung | Geltungsbereich | Gültigkeit | Hinweise |
|----------------|----------------|-----------|---------|
| ISO/IEC 27001 | Informationssicherheitsmanagement | 3 Jahre (jährliche Überwachung) | Globaler Standard, umfassend |
| SOC 2 Type II | Trust-Service-Kriterien | 12 Monate | US-fokussiert, detaillierte Kontrollen |
| SOC 2 Type I | Zeitpunktbezogene Bewertung | Zeitpunktbezogen | Weniger streng als Type II |
| ISO/IEC 27017 | Cloud-Sicherheitskontrollen | 3 Jahre | Cloud-spezifische Erweiterung |
| ISO/IEC 27018 | Cloud-Datenschutz | 3 Jahre | Datenschutz in der Cloud |
| CSA STAR | Cloud-Sicherheitsreife | Variiert je Stufe | Von Selbstbewertung bis zertifiziert |

**Zertifizierungsanforderungen nach Stufe:**

- **Stufe 1:** ISO/IEC 27001 oder SOC 2 Type II erforderlich (aktuell, nicht älter als 12 Monate)
- **Stufe 2:** ISO/IEC 27001 oder SOC 2 (Type I akzeptabel) erforderlich (aktuell, nicht älter als 12 Monate)
- **Stufe 3:** Zertifizierung bevorzugt, aber nicht obligatorisch bei Verarbeitung von Organisationsdaten
- **Stufe 4:** Keine Zertifizierungsanforderung

**Zertifizierungsakzeptanzkriterien:**

- Zertifikat muss aktuell sein (innerhalb der Gültigkeitsdauer)
- Geltungsbereich muss die der [Organisation] bereitgestellten Dienste abdecken
- Ausstellende Stelle muss akkreditiert sein (ISO: akkreditierte Zertifizierungsstelle; SOC: lizenzierte CPA-Firma)
- Bei mehrjährigen Zertifikaten (ISO) müssen jährliche Überwachungsaudits abgeschlossen sein

**Alternative Attestierungen**: Wenn ISO/SOC-Zertifizierungen nicht verfügbar sind, kann die [Organisation] akzeptieren:

- Staatlich ausgestellte Zertifizierungen (FedRAMP, C5 in Deutschland)
- Branchenspezifische Zertifizierungen (PCI DSS v4.0.1 für Zahlungsabwickler, HITRUST für das Gesundheitswesen)
- Detaillierte Drittanbieter-Sicherheitsprüfberichte (erfordert ISB-Genehmigung)

## Due-Diligence-Dokumentation

Alle Due-Diligence-Aktivitäten sollen dokumentiert werden, einschliesslich:

- Ausgefüllte Sicherheitsfragebögen mit Nachweisen
- Zertifikatskopien mit Gültigkeitsverifizierung
- Risikobewertungsergebnisse und Bewertung
- Entscheidungsbegründung und Genehmigungsnachweise
- Identifizierte Lücken und Abhilfepläne
- Kompensierende Kontrollen wo anwendbar
- Lieferantenantworten auf Befunde
- Follow-up-Punkte und Abschlussverfolgung

**Aufbewahrung der Dokumentation**: Due-Diligence-Dokumentation soll aufbewahrt werden für:

- Dauer der Lieferantenbeziehung + 7 Jahre (regulatorische Anforderung)
- Mindestens 3 Jahre nach Beziehungsbeendigung
- Dauerhafte Aufbewahrung für Stufe-1-Lieferanten mit wesentlichen Vorfällen

---

# Informationssicherheitsanforderungen

## Basisanforderungen (Alle Lieferanten mit Datenzugang)

| Anforderung | Beschreibung |
|-------------|-------------|
| **Zugangskontrolle** | Prinzip der geringsten Berechtigung, eindeutige Konten, rollenbasierter Zugang, Zugangsprotokollierung |
| **Authentifizierung** | Starke Authentifizierung (komplexe Passwörter oder Zertifikate), MFA für privilegierten Zugang |
| **Verschlüsselung bei Übertragung** | Daten bei Übertragung verschlüsselt mittels TLS 1.2+ oder gleichwertig |
| **Störungsmeldung** | Sicherheitsvorfälle an die [Organisation] innerhalb von 24 Stunden nach Kenntnis gemeldet |
| **Personalsicherheit** | Hintergrundüberprüfungen entsprechend dem Zugangniveau für Personal mit Zugang zu Daten der [Organisation] |
| **Vertraulichkeit** | NDA oder gleichwertige vertragliche Vertraulichkeitsverpflichtung |
| **Datenminimierung** | Zugang nur zu für die Diensterbringung notwendigen Daten |
| **Datenresidenz** | Datenverarbeitung innerhalb genehmigter Jurisdiktionen gemäss Vertrag |

## Erweiterte Anforderungen (Lieferanten der Stufe 1 und 2)

| Anforderung | Beschreibung |
|-------------|-------------|
| **Verschlüsselung im Ruhezustand** | Daten im Ruhezustand verschlüsselt mit starken Algorithmen (AES-256 oder gleichwertig) |
| **Schwachstellenmanagement** | Regelmässige Schwachstellen-Scans, zeitnahe Patches (kritisch: innerhalb 30 Tage, hoch: innerhalb 60 Tage) |
| **Sicherheitsüberwachung** | Protokollierung, Alarme, SIEM-Integration wo anwendbar, Aufbewahrung gemäss regulatorischen Anforderungen |
| **Betriebskontinuität** | Dokumentierte BC/DR-Pläne und jährliche Tests mit bereitgestellten Nachweisen |
| **Prüfungsrechte** | Die [Organisation] kann prüfen oder Drittanbieter-Auditberichte prüfen (SOC 2, ISO 27001-Überwachung) |
| **Unterlieferantenkontrollen** | Sicherheitsanforderungen werden an Unterlieferanten weitergegeben, Offenlegung der Unterlieferanten erforderlich |
| **Änderungsmanagement** | Formale Änderungskontrolle mit Benachrichtigung der [Organisation] bei wesentlichen Änderungen |
| **Datentrennung** | Logische oder physische Trennung von anderen Kunden (Multi-Tenancy-Kontrollen) |
| **Sichere Entwicklung** | SDLC mit Sicherheitstests für kundenspezifische Entwicklungen oder Integrationen |
| **Incident Response** | Dokumentierter Incident-Response-Plan mit Kontaktinformationen und Eskalationsverfahren |

## Anforderungskommunikation

Sicherheitsanforderungen sollen Lieferanten mitgeteilt werden durch:

- Sicherheitsanforderungsanhang in Verträgen (siehe ISMS-POL-A.5.19-23-S2)
- Lieferantensicherheitshandbuch (falls anwendbar)
- Onboarding-Dokumentation und Einführung
- Regelmässige Beziehungsüberprüfungen und Leistungsgespräche
- Ad-hoc-Kommunikation für neue Sicherheitsanforderungen oder Bedrohungsinformationen

**Verifizierung**: Die Einhaltung der Sicherheitsanforderungen durch Lieferanten soll verifiziert werden durch:

- Selbstbewertungsfragebögen
- Drittanbieter-Zertifizierungen und Auditberichte
- Technische Sicherheitstests (für Stufe-1-Lieferanten)
- Leistungsüberwachung und SLA-Verfolgung
- Vorfallsanalyse und Post-Mortem-Reviews

---

# Lieferantenregister

## Registeranforderungen

Die [Organisation] soll ein umfassendes Lieferantenregister führen, das folgende Felder enthält:

| Feld | Beschreibung | Aktualisierungsauslöser |
|------|-------------|------------------------|
| Lieferantenname | Juristischer Unternehmensname | Vertragsänderung |
| Lieferantentyp | Gemäss Kategorien aus Abschnitt 2.1 | Dienstleistungsänderung |
| Klassifizierungsstufe | Stufe 1–4 gemäss Abschnitt 3 | Jährliche Überprüfung |
| Erbrachte Dienste | Beschreibung der Dienste/Produkte | Dienstleistungsänderung |
| Datenzugang | Klassifizierung der zugänglichen Daten | Zugriffsänderung |
| Systemzugang | Systeme, auf die der Lieferant zugreifen kann | Zugriffsänderung |
| Vertragsreferenz | Link zur Vereinbarung und Ergänzungen | Vertragsänderung |
| Geschäftsverantwortlicher | Interner Beziehungsverantwortlicher | Organisationsänderung |
| Sicherheitskontakt | Sicherheitsansprechpartner beim Lieferanten | Lieferantenänderung |
| Letztes Bewertungsdatum | Datum der letzten Sicherheitsbewertung | Bewertungsabschluss |
| Nächstes Überprüfungsdatum | Geplantes Überprüfungsdatum | Klassifizierungsänderung |
| Risikobewertung | Aktueller Risikowert gemäss Abschnitt 4.3 | Bewertungsabschluss |
| Zertifizierungen | Aktuelle Zertifizierungen mit Ablaufdaten | Zertifikatserneuerung |
| Regulatorischer Geltungsbereich | DORA/NIS2/DSGVO-Anwendbarkeit | Geschäftsänderung |
| Exit-Komplexität | Leichtigkeit des Dienstersatzes (Gering/Mittel/Hoch) | Jährliche Überprüfung |

## Registerpflege

- Register wird bei Neuaufnahme von Lieferanten aktualisiert (innerhalb von 5 Werktagen)
- Register wird bei Vertragsänderungen aktualisiert (innerhalb von 10 Werktagen)
- Vierteljährliche Genauigkeitsprüfung durch Information Security Officer
- Jährliches Vollständigkeitsaudit durch Interne Revision oder ISB
- Registerverfügbarkeit: Zugänglich für Einkauf, IT, Sicherheit, Recht, Revision

**Register-Tools**: Das Lieferantenregister kann geführt werden in:

- Dedizierter GRC-Plattform (Governance, Risk, Compliance)
- Beschaffungsmanagementsystem mit Sicherheitsmodul
- Excel/Datenbank mit Versionskontrolle (Minimalanforderung)
- Bewertungsarbeitsmappe ISMS-IMP-A.5.19-23-1 (Cloud-Dienste-Inventar)

**Registerberichterstattung**: Vierteljährliche Lieferanten-Zusammenfassungsberichte sollen umfassen:

- Gesamtzahl der Lieferanten nach Klassifizierungsstufe
- Zertifizierungsstatus (aktuell vs. abgelaufen vs. fehlend)
- Bevorstehende Überprüfungen und Bewertungen
- Hochrisikolieferanten, die Aufmerksamkeit erfordern
- In diesem Quartal neu aufgenommene Lieferanten
- In diesem Quartal ausgeschiedene Lieferanten

---

# Shadow-IT-Prävention

## Definition Shadow IT

**Shadow IT**: Nutzung nicht genehmigter Lieferanten, Cloud-Dienste oder Software ohne IT- und Sicherheitsgenehmigung. Shadow IT umgeht Sicherheitskontrollen, Due Diligence und Vertragsschutz und schafft unkontrollierte und oft nicht erkennbare Risiken.

## Präventionsmassnahmen

| Massnahme | Beschreibung |
|----------|-------------|
| **Genehmigter Dienstkatalog** | Liste genehmigter Lieferanten und Dienste pflegen und kommunizieren |
| **Einkaufsintegration** | IT/Sicherheitsgenehmigung im Beschaffungsworkflow verlangen |
| **Netzwerküberwachung** | Netzwerkverkehr auf nicht genehmigte Cloud-Dienste überwachen |
| **Endpunktkontrollen** | Anwendungs-Whitelisting oder Überwachung auf nicht genehmigte Software |
| **Benutzersensibilisierung** | Regelmässige Schulungen zum Lieferantengenehmigungsprozess und Shadow-IT-Risiken |
| **Meldekanal** | Einfacher Mechanismus für Benutzer zur Anforderung der Bewertung neuer Dienste |

## Shadow-IT-Entdeckung

**Entdeckungsmethoden:**

- Netzwerkverkehrsanalyse (DNS-Abfragen, HTTPS SNI, Cloud-Dienst-IP-Bereiche)
- Cloud Access Security Broker (CASB)-Überwachung
- Spesenberichtanalyse (Software-Abonnements, Cloud-Dienst-Gebühren)
- Benutzerumfragen und Audits
- Kreditkartentransaktionsüberwachung (Firmenkarten)

**Reaktion auf Entdeckung:**
1. Dienst und Benutzer identifizieren
2. Risiko bewerten (Datenzugang, Kritikalität, Compliance-Auswirkung)
3. Entscheidung: Nachträgliche Genehmigung, Migration zu genehmigter Alternative oder Beendigung
4. Bei Genehmigung: Beschleunigtes Onboarding mit Risikoakzeptanz durchführen
5. Bei Beendigung: Benutzer informieren, Zugang sperren, Daten ggf. migrieren
6. Ursachenanalyse: Warum haben Benutzer den Genehmigungsprozess umgangen?

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Geschäftsverantwortlicher** | Lieferantenbedarf identifizieren, Beziehung pflegen, sicherstellen, dass der Dienst Geschäftsanforderungen erfüllt, Budgetgenehmigung |
| **Einkauf** | Koordination des Lieferantenauswahlprozesses, Vertragsverhandlung und -management, Wettbewerbsausschreibung |
| **Information Security Officer** | Risikobewertung, Definition von Sicherheitsanforderungen, Bewertungsüberprüfung und -genehmigung, Lieferantenregisterpflege |
| **Legal/Compliance** | Vertragsprüfung, regulatorische Compliance-Verifizierung, Prüfung von Datenverarbeitungsvereinbarungen, Streitbeilegung |
| **IT-Betrieb** | Technische Implementierung, Zugangsvergabe, Integrationsunterstützung, Leistungsüberwachung |
| **ISB** | Richtliniengenehmigung, Genehmigung von Hochrisikolieferanten, Ausnahmegenehmigung, Berichterstattung an Geschäftsleitung |
| **Datenschutzbeauftragter** | DSGVO-Compliance-Verifizierung, Genehmigung von Datenverarbeitungsvereinbarungen, Datenschutz-Folgenabschätzung |

**Verantwortungsmatrix** (RACI):

| Aktivität | Geschäftsverantwortl. | Einkauf | Sicherheit | Recht | IT-Betrieb | ISB |
|-----------|-----------------------|---------|-----------|-------|-----------|------|
| Lieferantenidentifikation | V | B | I | I | B | I |
| Risikobewertung | B | B | V | B | B | A |
| Vertragsverhandlung | I | V | B | V | I | I |
| Sicherheitsüberprüfung | I | I | V | B | B | A |
| Onboarding | B | B | B | I | V | I |
| Laufende Überwachung | A | B | V | I | B | I |
| Ausnahmegenehmigung | I | I | B | B | I | A |

*V=Verantwortlich, A=Accountable, B=Beratend, I=Informiert*

---

# Referenzen

| Dokument | Beziehung |
|----------|----------|
| **ISMS-POL-A.5.19-23** | Übergeordnetes Richtlinienrahmenwerk |
| **ISMS-POL-A.5.19-23-S2** | Anforderungen an Lieferantenvereinbarungen (Massnahme A.5.20) |
| **ISMS-POL-A.5.19-23-S3** | ICT-Lieferkettensicherheit (Massnahme A.5.21) |
| **ISMS-IMP-A.5.19-23.S1-UG/TG** | Cloud-Dienste-Inventar-Bewertungsarbeitsmappe |
| **ISMS-IMP-A.5.19-23.S2-UG/TG** | Lieferanten-Due-Diligence-Bewertungsarbeitsmappe |
| **ISO/IEC 27036-1:2021** | Informationssicherheit in Lieferantenbeziehungen – Überblick |
| **NIST SP 800-161** | Cybersecurity Supply Chain Risk Management |

---

**Nächstes Dokument:** ISMS-POL-A.5.19-23-S2 — Anforderungen an Lieferantenvereinbarungen (Massnahme A.5.20)

---

*„Die Stärke Ihrer Sicherheit ist nur so stark wie Ihr schwächster Lieferant."*
<!-- QA_VERIFIED: 2026-03-28 -->
