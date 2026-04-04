<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.32-DE:framework:POL:a.8.32 -->
**ISMS-POL-A.8.32 – Änderungsmanagement**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Änderungsmanagement |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.32 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erste konsolidierte Richtlinie für ISO 27001:2022 Erstzertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL) / IT-Betriebsleiter
- Compliance: Rechts-/Compliance-Beauftragter
- Letzte Instanz: Geschäftsleitung (GF)

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-IMP-A.8.32.1-UG/TG (Bewertung des Änderungsprozesses)
- ISMS-IMP-A.8.32.2-UG/TG (Bewertung von Änderungstypen und -kategorien)
- ISMS-IMP-A.8.32.3-UG/TG (Bewertung der Umgebungstrennung)
- ISMS-REF-A.8.32 (Änderungsmanagement-Referenz – Vorlagen, Tools, Kurzanleitungen)
- ISO/IEC 27001:2022 Control A.8.32

---

## Zusammenfassung für die Geschäftsleitung

Diese Richtlinie legt die Anforderungen von [Organisation] an Änderungsmanagement-Kontrollen fest, um sichere und kontrollierte Modifikationen an Informationssystemen gemäss ISO/IEC 27001:2022 Control A.8.32 zu gewährleisten.

**Geltungsbereich**: Diese Richtlinie gilt für alle Änderungen an informationsverarbeitenden Systemen, Anwendungen, Infrastruktur, Netzwerkausrüstung und unterstützenden Systemen unabhängig vom Bereitstellungsmodell (On-Premises, Cloud, Hybrid). Alle Änderungstypen (Hardware, Software, Konfiguration, Infrastruktur, Daten, Prozesse, Dokumentation) und alle Umgebungen (Entwicklung, Test, Staging, Produktion, Disaster Recovery) sind abgedeckt.

**Zweck**: Organisatorische Anforderungen an die Implementierung und Steuerung des Änderungsmanagements definieren. Diese Richtlinie legt WAS beim Änderungsmanagement erforderlich ist und WER verantwortlich ist, fest. Implementierungsverfahren (WIE Änderungen durchgeführt werden) sind separat in den ISMS-IMP-A.8.32-Bewertungsarbeitsmappen dokumentiert. Vorlagen, Tools und Kurzanleitungen sind in ISMS-REF-A.8.32 (Nicht-ISMS-Technische Referenz) bereitgestellt.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen), einschliesslich ISO/IEC 27001:2022 Control 8.32, sowie bedingte branchenspezifische Anforderungen, die gelten, wo die Geschäftstätigkeit von [Organisation] die Anwendbarkeit auslöst.

---

# Kontrollausrichtung und Geltungsbereich

## ISO/IEC 27001:2022 Control A.8.32

**ISO/IEC 27001:2022 Anhang A.8.32 – Änderungsmanagement**

> *Änderungen an informationsverarbeitenden Einrichtungen und Informationssystemen sollten Änderungsmanagementverfahren unterliegen.*

**ISO/IEC 27002:2022 Leitlinien (paraphrasiert)**:

Änderungsmanagementverfahren sollten sicherstellen, dass:

- Änderungen geplant, auf Auswirkungen bewertet, autorisiert, getestet, kommuniziert, umgesetzt und dokumentiert werden
- Notfalländerungen beschleunigte Verfahren haben, während die Kontrolle aufrechterhalten wird
- Alle Änderungen die Informationssicherheit erhalten oder verbessern
- Risiken von Änderungen verstanden und gemindert werden

**Neun verbindliche Elemente (ISO/IEC 27002:2022)**:

| Element | Beschreibung | Abschnittsreferenz |
|---------|-------------|-------------------|
| **(a) Planung und Folgenabschätzung** | Mögliche Auswirkungen vor der Umsetzung bewerten | 2.1 |
| **(b) Autorisierung** | Angemessene Genehmigungen basierend auf Risiko/Auswirkung einholen | 2.1 |
| **(c) Kommunikation** | Interessengruppen über Änderungen und Auswirkungen informieren | 2.1 |
| **(d) Testen und Abnahme** | Prüfen, dass Änderungen vor dem Einsatz wie vorgesehen funktionieren | 2.3 |
| **(e) Umsetzung** | Änderungen auf kontrollierte Weise durchführen | 2.1 |
| **(f) Notfall und Kontingenzmassnahmen** | Dringende Änderungen mit beschleunigten Verfahren handhaben | 2.4 |
| **(g) Aufzeichnung** | Audit-Trail aller Änderungen führen | 2.1 |
| **(h) Dokumentationsaktualisierungen** | Betriebsverfahren und Runbooks aktualisieren | 2.1 |
| **(i) Aktualisierungen der Kontinuitätspläne** | Business-Continuity-Pläne bei Infrastrukturänderungen aktualisieren | 2.1 |

## Zweck

Diese Richtlinie legt den Änderungsmanagement-Rahmen von [Organisation] fest, der folgendes gewährleistet:

**Risikominderung**:

- Nicht autorisierte oder ungeplante Änderungen werden verhindert
- Auswirkungen von Änderungen werden vor der Umsetzung bewertet
- Änderungsfehler werden durch angemessenes Testen minimiert
- Rollback-Verfahren sind verfügbar, wenn Änderungen scheitern
- Die Systemverfügbarkeit wird während der Änderungsumsetzung aufrechterhalten

**Compliance und Audit**:

- Vollständiger Audit-Trail aller Änderungen
- Nachweis der Änderungsmanagement-Reife
- Belege für Due Diligence bei Systemmodifikationen
- Überprüfung der regulatorischen Compliance

**Betriebliche Exzellenz**:

- Standardisierter Ansatz für Änderungen
- Klare Verantwortlichkeiten für Änderungsentscheidungen
- Effiziente Genehmigungsabläufe basierend auf Risiko
- Kontinuierliche Verbesserung durch Reviews nach der Umsetzung

## Geltungsbereich

**Diese Richtlinie gilt für:**

**Informationssysteme** (alle Systeme, die Organisationsinformationen verarbeiten, speichern oder übertragen):

- Produktionssysteme (Geschäftsanwendungen, Datenbanken, ERP, CRM, Finanzsysteme)
- Infrastruktursysteme (Server, Storage, Virtualisierung, Netzwerkausrüstung)
- Sicherheitssysteme (Firewalls, IDS/IPS, SIEM, Authentifizierungssysteme, Verschlüsselungssysteme)
- Cloud-Dienste (IaaS, PaaS, SaaS – kundenkontrollierte Konfigurationen)
- Kommunikationssysteme (E-Mail, Kollaborationsplattformen, Telefonie)
- Entwicklungs- und Testumgebungen (einschliesslich CI/CD-Pipelines und Deployment-Automatisierung)
- Office-Produktivitätssysteme (E-Mail, Kollaboration, Dokumentenverwaltung)
- Websites und Webanwendungen (öffentlich und intern)

**Änderungstypen:**

- Hardware-Änderungen (Server-Installationen, Netzwerkausrüstungs-Upgrades, Storage-Erweiterungen)
- Software-Änderungen (Anwendungsaktualisierungen, OS-Patches, Sicherheitsupdates, Neuinstallationen)
- Konfigurationsänderungen (Parameteranpassungen, Regelaktualisierungen, Richtlinienänderungen)
- Infrastrukturänderungen (Netzwerktopologie, Virtualisierung, Cloud-Ressourcen)
- Datenänderungen (Datenbankschema-Anpassungen, Datenmigration, Stammdatenaktualisierungen)
- Prozessänderungen (Workflow-Modifikationen, Integrationsänderungen, Automatisierungsupdates)
- Dokumentationsänderungen (Betriebsverfahren, Konfigurationsdokumentation, Runbooks)

**Alle Umgebungen:**

- Entwicklung (Dev)
- Test / Qualitätssicherung (Test/QA)
- Staging / Vorproduktion (sofern vorhanden)
- Produktion (Prod)
- Disaster Recovery (DR)
- Übergänge zwischen Umgebungen (Förderung/Deployment)

**Nicht im Geltungsbereich:**

**Geschäftsprozessänderungen:**

- Organisatorische Umstrukturierungen (sofern keine IT-Systeme betroffen)
- Änderungen an Geschäftsrichtlinien (sofern keine IT-Systemkonfigurationen betroffen)
- Personaländerungen (Einstellungen, Kündigungen, Rollenwechsel)
  - *Ausnahme: Änderungen an Systemzugriffen/-berechtigungen folgen diesem Rahmen*

**Inhaltsänderungen:**

- Website-Inhaltsaktualisierungen (Texte, Bilder, Marketingmaterialien)
- Dokumenteninhaltsänderungen in Content-Management-Systemen
- E-Mail-/Kommunikationsinhalt
  - *Ausnahme: Änderungen an Website-Funktionen oder CMS-Konfigurationen folgen diesem Rahmen*

**Routinebetrieb:**

- Tägliche Backups (geplant, automatisiert)
- Log-Rotation und -Archivierung (automatisierte Prozesse)
- Bestätigung von Monitoring-Alarmen
- Routinemässige Wartungsaufgaben (als Standard-Änderungen vorab genehmigt)

**Benutzeraktivitäten:**

- Vom Benutzer initiierte Self-Service-Aktionen (Passwort-Resets über genehmigtes Self-Service-Portal)
- Benutzereinstellungen innerhalb von Anwendungen
- Persönliche Dateiablage und -freigabe (innerhalb genehmigter Grenzen)

**Änderungen externer Dienstleister:**

- Vollständig vom SaaS-Anbieter verwaltete Änderungen (im Hintergrund)
- Infrastrukturänderungen des Cloud-Anbieters (ausserhalb der Kundenkontrolle)
  - *Ausnahme: Änderungen an kundenkontrollierten Konfigurationen folgen diesem Rahmen*

**Ausschlussgrund**: Diese Ausschlüsse betreffen Aktivitäten, die entweder (1) die Informationssicherheit nicht wesentlich beeinflussen, (2) durch separate Governance-Prozesse verwaltet werden, (3) vollständig automatisiert mit angemessenen Kontrollen sind, oder (4) ausserhalb der Kontrolle der Organisation liegen.

Änderungen in Graubereichen MÜSSEN zur Klassifizierung an den Change Manager eskaliert werden.

## Regulatorische Anwendbarkeit

Regulatorische Anforderungen sind gemäss **ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)** kategorisiert.

**Stufe 1: Verbindliche Compliance**

[Organisation] MUSS Änderungsmanagement-Anforderungen aus anwendbaren Vorschriften einhalten. Eine vollständige regulatorische Kategorisierung ist in **ISMS-POL-00 – Regulatorischer Anwendbarkeitsrahmen** zu finden.

**Schlüsselprinzip**: Diese Richtlinie stellt technologieunabhängige Anforderungen bereit. Organisationen bestimmen spezifische Kontrollen durch Risikobewertung unter Berücksichtigung ihres Betriebskontexts, ihrer Branche, Gerichtsbarkeit und regulatorischen Verpflichtungen.

## Was diese Richtlinie NICHT regelt

Diese Richtlinie regelt NICHT:

- **Spezifische Änderungsmanagement-Tools oder -Plattformen** (siehe ISMS-REF-A.8.32 für Tool-Bewertungskriterien)
- **Schritt-für-Schritt-Änderungsverfahren** (siehe ISMS-IMP-A.8.32.1 Bewertung des Änderungsprozesses)
- **Vorlagen für Änderungsantragsformulare** (siehe ISMS-REF-A.8.32 für Vorlagen)
- **Spezifische Genehmigungskompetenzen für bestimmte Systeme** (durch Risikobewertung von [Organisation] festgelegt)
- **Einträge im Standard-Änderungskatalog** (siehe ISMS-IMP-A.8.32.2 Bewertung von Änderungstypen)
- **Risikobewertungsmatrizen** (siehe ISMS-REF-A.8.32 für Risikobewertungsmethodik)
- **Technische Verfahren** (technische Umsetzung in ISMS-IMP-Dokumenten)
- **Tool-Konfigurationen** (Tool-spezifische Konfigurationen sind Umsetzungsdetails)

**Begründung**: Die Trennung von Richtlinienanforderungen und Umsetzungsleitlinien ermöglicht:

- Richtlinienstabilität trotz sich entwickelnder Technologie und Änderungsmanagement-Best-Practices
- Technische Agilität für Tool-Updates, Prozessverbesserungen und Methodenänderungen ohne Richtlinienrevision
- Klare Unterscheidung zwischen Governance (Richtlinie) und Ausführung (Umsetzung)
- Fokussierten Prüfungsumfang (Prüfer überprüfen Richtlinienkonformität, nicht Tool-Konfigurationen)
- Anpassungsfähigkeit für verschiedene Organisationskontexte, Branchen und Risikoprofile

## Definitionen

**Änderung**: Jede Hinzufügung, Modifikation oder Entfernung von Informationssystemkomponenten (Hardware, Software, Konfiguration, Daten, Dokumentation), die die Informationssicherheit oder Systemverfügbarkeit beeinflussen könnte.

**Change Advisory Board (CAB)**: Multidisziplinäre Gruppe, die fachkundige Überprüfung, Folgenabschätzung und Empfehlungen für Normal- und Notfalländerungen bereitstellt. Kann ständiger Ausschuss oder Ad-hoc-Gremium sein.

**Change Manager**: Für den Änderungsmanagementprozess, CAB-Koordination, Metriken-Tracking und kontinuierliche Verbesserung verantwortliche Person.

**Änderungsantrag**: Formeller Nachweis, der die vorgeschlagene Änderung dokumentiert, einschliesslich Beschreibung, Begründung, Folgenabschätzung, Umsetzungsplan, Testansatz und Rollback-Verfahren.

**Notfalländerung**: Änderung, die eine beschleunigte Umsetzung zur Behebung eines kritischen Vorfalls, einer Sicherheitslücke oder zur Vermeidung erheblicher Geschäftsauswirkungen erfordert. Notfalländerungen folgen einem beschleunigten Genehmigungsverfahren, behalten aber die Kontrollstrenge bei.

**Normale Änderung**: Änderung, die aufgrund eines mittleren oder hohen Risikos/Auswirkung eine vollständige Bewertung, CAB-Überprüfung und einen Standard-Genehmigungsablauf erfordert.

**Review nach der Umsetzung (Post-Implementation Review, PIR)**: Strukturierte Überprüfung nach der Änderungsumsetzung, die bestätigt, ob die Ziele erreicht wurden, Erfahrungen identifiziert und Verbesserungsmöglichkeiten erfasst.

**Produktionsumgebung**: Live-Betriebssysteme, die den Geschäftsbetrieb direkt unterstützen und für Endbenutzer zugänglich sind.

**Rollback**: Verfahren zum Rückgängigmachen einer Änderung und Rückführen des Systems in den vorherigen funktionierenden Zustand, wenn die Änderung fehlschlägt oder unerwartete Probleme verursacht.

**Standard-Änderung**: Vorab genehmigte, risikoarme, routinemässige Änderung, die einem dokumentierten Verfahren aus dem Standard-Änderungskatalog folgt. Kann ohne CAB-Überprüfung umgesetzt werden.

**Testumgebung**: Von der Produktion isolierte Nicht-Produktionsumgebung, in der Änderungen vor der Produktionsbereitstellung validiert werden.

---

# Anforderungen an das Änderungsmanagement

Dieser Abschnitt definiert Anforderungen an das Änderungsmanagement in drei Bereichen:

1. **Anforderungen an den Änderungsprozess** (2.1): Kernworkflow von der Einleitung bis zum Abschluss
2. **Anforderungen an die Änderungsklassifizierung** (2.2): Standard-, Normal- und Notfalländerungstypen
3. **Anforderungen an Notfalländerungen** (2.3): Beschleunigte Verfahren für dringende Situationen

## Anforderungen an den Änderungsprozess

**Zweck**: Den Kernprozess des Änderungsmanagements definieren, der den vollständigen Änderungslebenszyklus von der Einleitung bis zum Abschluss abdeckt. Diese Anforderungen setzen die ISO/IEC 27002:2022 Control 8.32 Elemente (a), (b), (c), (e), (g), (h) und (i) um.

### Einreichung von Änderungsanträgen

**REQ-PROCESS-001: Dokumentation von Änderungsanträgen**

[Organisation] MUSS für alle in den Geltungsbereich fallenden Änderungen formelle Änderungsanträge im Änderungsmanagementsystem verlangen.

**Begründung**: Formelle Änderungsanträge liefern einen Audit-Trail, ermöglichen eine ordentliche Bewertung, verhindern undokumentierte "Schatten-Änderungen" und schaffen eine einzige Quelle der Wahrheit.

**Mindesterforderliche Informationen**:

- Eindeutige Änderungskennung
- Änderungsbeschreibung und -umfang
- Geschäftliche Begründung
- Betroffene Systeme/Komponenten
- Umsetzungsdatum/-fenster
- Identifikation von Antragsteller und Umsetzer
- Folgenabschätzung (Verfügbarkeit, Vertraulichkeit, Integrität)
- Risikoeinstufung
- Rollback-Verfahren
- Testansatz
- Abhängigkeiten von anderen Änderungen
- Kommunikationsplan

**Bewertungskriterien**: ISMS-IMP-A.8.32.1 (Bewertung des Änderungsprozesses) überprüft, ob Änderungsantragsformulare die erforderlichen Informationen erfassen und das Änderungsmanagementsystem vollständige Aufzeichnungen führt.

**Ausnahmen**: Vorab genehmigte Standard-Änderungen können eine vereinfachte Einreichung verwenden, MÜSSEN aber weiterhin einen Änderungsantragsdatensatz erstellen.

---

### Planung und Folgenabschätzung

**REQ-PROCESS-002: Folgenabschätzung**

[Organisation] MUSS für alle Änderungen eine Folgenabschätzung verlangen, die folgendes bewertet:

- Technische Auswirkung (betroffene Systeme, Abhängigkeiten, Integrationspunkte)
- Geschäftliche Auswirkung (betroffene Dienste, Benutzerauswirkung, Unterbrechung des Geschäftsbetriebs)
- Sicherheitsauswirkung (Risiken für Vertraulichkeit, Integrität, Verfügbarkeit)
- Compliance-Auswirkung (regulatorische Verpflichtungen, Audit-Kontrollen)
- Risikoniveau (Wahrscheinlichkeit des Scheiterns × Ausmass der Auswirkung)

**Begründung**: Das Verständnis der Änderungsauswirkungen vor der Umsetzung verhindert Überraschungen, ermöglicht angemessene Genehmigungsniveaus und unterstützt eine fundierte Entscheidungsfindung.

**Bewertungskriterien**: Änderungsanträge weisen eine dokumentierte Folgenabschätzung nach. Hoch-Risiko-Änderungen zeigen eine detaillierte Analyse.

---

**REQ-PROCESS-003: Umsetzungsplanung**

[Organisation] MUSS Umsetzungspläne für Normal- und Notfalländerungen verlangen, die folgendes beinhalten:

- Schritt-für-Schritt-Verfahren
- Ressourcenanforderungen (Personal, Tools, Zugriff)
- Umsetzungszeitrahmen
- Abhängigkeiten und Voraussetzungen
- Verifikationsschritte
- Rollback-Auslöser und -Verfahren
- Kommunikationsprüfpunkte

**Begründung**: Detaillierte Planung reduziert Umsetzungsfehler, ermöglicht eine reibungslose Ausführung und bietet klare Leitlinien für Umsetzer.

**Bewertungskriterien**: Änderungsanträge enthalten Umsetzungspläne. Komplexe Änderungen weisen eine detaillierte Planung nach.

---

### Autorisierung und Genehmigung

**REQ-PROCESS-004: Genehmigungsabläufe**

[Organisation] MUSS die Genehmigungskompetenz basierend auf dem Änderungsrisikoniveau definieren:

| Risikoniveau | Genehmigungskompetenz | CAB-Überprüfung | Dokumentationsgrad |
|-------------|----------------------|-----------------|-------------------|
| **Niedrig** | Standard-Änderung (vorab genehmigt) | Nicht erforderlich | Standard-Änderungskatalog |
| **Mittel** | Service-Eigentümer / Team-Lead | Empfohlen | Standard |
| **Hoch** | IT-Betriebsleiter / ISB | Erforderlich | Umfassend |
| **Kritisch** | Geschäftsleitung | Erforderlich | Umfassend + Risikoakzeptanz |

**Umsetzung**: Die Genehmigungskompetenzmatrix ist in ISMS-IMP-A.8.32.1 (Bewertung des Änderungsprozesses) dokumentiert und benennt spezifische Rollen/Positionen mit Genehmigungskompetenz für jedes Risikoniveau. Die Matrix MUSS jährlich vom ISB überprüft und genehmigt werden sowie innerhalb von 30 Tagen nach Organisationsänderungen, die Genehmigungskompetenzen betreffen, aktualisiert werden.

**Bewertungskriterien**: ISMS-IMP-A.8.32.1 enthält eine aktuelle Genehmigungskompetenzmatrix mit benannten Rollen. Belege zeigen, dass Genehmigungen von designierten Instanzen gemäss Matrix eingeholt wurden. Jährliche Überprüfungsnachweise belegen die Genauigkeit der Matrix.

**Begründung**: Risikobasierte Genehmigungen balancieren Kontrolle mit Effizienz. Risikoarme Änderungen werden schnell bearbeitet; hochriskante Änderungen erhalten angemessene Aufsicht.

---

**REQ-PROCESS-005: Change Advisory Board (CAB)**

[Organisation] MUSS ein Change Advisory Board (CAB) für die Überprüfung von Normal- und Notfalländerungen einrichten.

**CAB-Aufgaben:**

- Änderungsanträge auf Vollständigkeit und Genauigkeit der Risikobewertung überprüfen
- Mögliche Konflikte zwischen geplanten Änderungen identifizieren
- Auswirkungen auf abhängige Systeme bewerten
- Genehmigung, Verschiebung oder Ablehnung empfehlen
- Notfalländerungen überprüfen (retrospektiv für zeitkritische Notfälle)

**CAB-Zusammensetzung** (Minimum):

- Change Manager (Vorsitz)
- Vertreter des IT-Betriebs
- Sicherheitsvertreter
- Geschäftsanwendungseigentümer (für relevante Änderungen)
- Weitere Fachexperten (nach Bedarf)

**Beschlussfähigkeitsanforderungen**: CAB-Sitzungen erfordern eine Mindestanwesenheit von (1) Change Manager (Vorsitz), (2) Vertreter des IT-Betriebs, (3) Sicherheitsvertreter und (4) mindestens einem weiteren CAB-Mitglied. Notfall-CAB-Sitzungen KÖNNEN bei reduzierter Beschlussfähigkeit (Change Manager + ein weiteres Mitglied) fortgesetzt werden, wenn zeitkritisch, wobei eine vollständige CAB-Retrospektivüberprüfung innerhalb von 48 Stunden erforderlich ist.

**Nachweise des Betriebs**: Der CAB-Betrieb wird durch folgendes belegt: (1) Sitzungsprotokoll für alle geplanten und Notfallsitzungen mit Datum, Teilnehmern, überprüften Änderungen, Entscheidungen, Begründungen und Aktionspunkten, (2) Anwesenheitsaufzeichnungen, die belegen, dass Beschlussfähigkeitsanforderungen erfüllt wurden, (3) Änderungsantragsaufzeichnungen mit CAB-Überprüfungsnotizen und Empfehlungen, (4) jährliche CAB-Charterüberprüfung. CAB-Sitzungsprotokolle werden mindestens 3 Jahre aufbewahrt und sind im Änderungsmanagementsystem/Dokumentenrepository zugänglich.

**CAB-Frequenz**:

- Regelmässige Sitzungen (wöchentlich empfohlen für aktive Änderungsumgebungen)
- Notfall-CAB-Sitzungen (nach Bedarf für dringende Änderungen)
- Virtuelle CAB-Überprüfung (für zeitkritische Änderungen zwischen Sitzungen)

**Begründung**: Multidisziplinäre Überprüfung verhindert einzelne Fehlerquellen bei der Änderungsbewertung, identifiziert Risiken, die Umsetzer möglicherweise übersehen, und bietet Governance-Aufsicht.

**Bewertungskriterien**: CAB-Charter dokumentiert. Sitzungsprotokolle belegen den regelmässigen Betrieb. Änderungsanträge zeigen CAB-Überprüfungsnotizen.

### Kommunikation

**REQ-PROCESS-006: Kommunikation mit Interessengruppen**

[Organisation] MUSS betroffene Interessengruppen über Änderungen informieren, einschliesslich:

- Änderungsplan und -zeitpunkt
- Erwartete Dienstauswirkung (Dauer, Umfang)
- Erforderliche Benutzeraktionen (falls vorhanden)
- Kontaktinformationen für Support
- Rollback-Entscheidung und Kommunikation

**Kommunikationszeitpunkte:**

- **Geplante Änderungen**: Mindest-Vorankündigung gemäss den Betriebsanforderungen von [Organisation]
- **Notfalländerungen**: Kommunikation so bald wie sicher möglich
- **Änderungsabschluss**: Bestätigung an Interessengruppen, wenn Änderung abgeschlossen

**Kommunikationskanäle**: E-Mail, Service-Portal-Benachrichtigungen, Kollaborationsplattformen oder andere für den Betrieb von [Organisation] geeignete Methoden.

**Begründung**: Vorankündigung ermöglicht Benutzern, ihre Arbeit rund um Dienstauswirkungen zu planen, reduziert den Support-Aufwand und zeigt Transparenz.

**Bewertungskriterien**: Änderungsaufzeichnungen zeigen gesendete Stakeholder-Benachrichtigungen. Kommunikationsvorlagen in ISMS-REF-A.8.32 dokumentiert.

---

### Umsetzungsausführung

**REQ-PROCESS-007: Kontrollierte Umsetzung**

[Organisation] MUSS Änderungen gemäss dem genehmigten Umsetzungsplan durchführen mit:

- Überprüfung von Voraussetzungen und Abhängigkeiten
- Ausführung dokumentierter Schritte
- Echtzeitüberwachung während der Umsetzung
- Verifikationstests nach der Umsetzung
- Dokumentation der tatsächlich durchgeführten Schritte

**Umsetzungsfenster:**
[Organisation] SOLLTE bevorzugte Änderungsfenster (z.B. Wartungsfenster) einrichten, um Geschäftsunterbrechungen zu minimieren und dabei die betrieblichen Anforderungen zu berücksichtigen.

**Begründung**: Kontrollierte Ausführung reduziert Fehler, ermöglicht die Fehlerbehebung bei Problemen und erstellt einen Audit-Trail der tatsächlich durchgeführten Arbeit.

**Bewertungskriterien**: Änderungsaufzeichnungen dokumentieren Umsetzungsschritte. Verifikationstestergebnisse werden erfasst.

---

**REQ-PROCESS-008: Rollback-Ausführung**

[Organisation] MUSS das Rollback-Verfahren ausführen, wenn:

- Die Änderung ihre Ziele nicht erreicht
- Inakzeptable Leistungsbeeinträchtigung auftritt
- Eine Sicherheitslücke eingeführt wird
- Eine kritische Geschäftsfunktion beeinträchtigt wird
- Rollback-Auslöser (im Änderungsantrag definiert) erfüllt sind

**Rollback-Entscheidungsbefugnis**: Gleiche Genehmigungsbefugnis wie die ursprüngliche Änderung (oder höher bei Notfall-Rollback).

**Begründung**: Schnelle Rollback-Fähigkeit minimiert die Auswirkungen fehlgeschlagener Änderungen, erhält die Systemverfügbarkeit aufrecht und verhindert anhaltende Vorfälle.

**Bewertungskriterien**: Fehlgeschlagene Änderungen zeigen dokumentierte Rollback-Entscheidungen und -Ausführungen.

---

### Aufzeichnungsführung und Audit-Trail

**REQ-PROCESS-009: Änderungsaufzeichnungen**

[Organisation] MUSS vollständige Änderungsaufzeichnungen führen, einschliesslich:

- Alle Informationen aus dem Änderungsantrag (gemäss REQ-PROCESS-001)
- Genehmigungsnachweise mit Zeitstempeln und Genehmigern
- CAB-Überprüfungsnotizen und Empfehlungen
- Umsetzungsprotokolle und Verifikationsergebnisse
- Kommunikationsaufzeichnungen
- Vorfälle oder Probleme während der Umsetzung
- Rollback-Entscheidungen und -Ausführungen (falls zutreffend)
- Ergebnisse der Überprüfung nach der Umsetzung

**Aufbewahrungsdauer**: Mindest [von Organisation definierter] Zeitraum (empfohlen: 7 Jahre für Audit, 3 Jahre für Betriebsreferenz).

**Begründung**: Vollständige Aufzeichnungen ermöglichen Audit-Verifikation, Vorfallsuntersuchung, Trendanalyse und Nachweis der regulatorischen Compliance.

**Bewertungskriterien**: ISMS-IMP-A.8.32.1 (Bewertung des Änderungsprozesses) überprüft die Vollständigkeit der Aufzeichnungen. Stichprobenaudits zeigen verfügbare Aufzeichnungen.

---

### Dokumentationsaktualisierungen

**REQ-PROCESS-010: Aktualisierungen der Betriebsdokumentation**

[Organisation] MUSS die Betriebsdokumentation nach Änderungen aktualisieren:

- Systemkonfigurationsdokumentation
- Netzwerkdiagramme und -topologie
- Anwendungsarchitekturdokumente
- Betriebsverfahren und Runbooks
- Leitfäden zur Fehlerbehebung
- Disaster-Recovery-Verfahren
- Benutzerdokumentation (sofern zutreffend)

**Aktualisierungszeitraum**: Innerhalb des [von Organisation definierten] Zeitrahmens (empfohlen: 5 Werktage für Nicht-Notfalländerungen).

**Begründung**: Genaue Dokumentation ermöglicht einen effektiven Betrieb, unterstützt die Fehlerbehebung und gewährleistet Wissenskontinuität bei Personalwechseln.

**Bewertungskriterien**: Änderungsaufzeichnungen referenzieren Dokumentationsaktualisierungen. Stichprobenüberprüfung zeigt aktuelle Dokumentation.

---

**REQ-PROCESS-011: Aktualisierungen der Kontinuitätspläne**

[Organisation] MUSS Business-Continuity-Pläne überprüfen und aktualisieren, wenn Änderungen folgendes betreffen:

- Kritische Geschäftssysteme oder -anwendungen
- Infrastruktur, die die Business Continuity unterstützt
- Disaster-Recovery-Verfahren
- Recovery Time Objectives (RTO) oder Recovery Point Objectives (RPO)
- Backup- und Wiederherstellungsverfahren

**Überprüfungsauslöser**: Alle Änderungen an im Geltungsbereich liegenden Systemen MÜSSEN eine Überprüfung der Kontinuitätspläne auslösen.

**Begründung**: Business-Continuity-Pläne müssen aktuelle Systemkonfigurationen widerspiegeln, um eine wirksame Wiederherstellung bei Vorfällen zu gewährleisten.

**Bewertungskriterien**: Änderungen an kritischen Systemen zeigen eine Überprüfung der Kontinuitätspläne. Aktualisierungen sind dokumentiert, sofern Auswirkungen festgestellt wurden.

---

### Review nach der Umsetzung

**REQ-PROCESS-012: Review nach der Umsetzung (PIR)**

[Organisation] MUSS Reviews nach der Umsetzung durchführen für:

- Alle Notfalländerungen (obligatorisch)
- Alle fehlgeschlagenen Änderungen (obligatorisch)
- Normale Änderungen oberhalb eines [von Organisation definierten] Risikoschwellenwerts
- Standard-Änderungen, wenn Muster auf Überprüfungsbedarf hindeuten

**PIR-Inhalt:**

- Erzielte Ziele vs. geplante Ergebnisse
- Aufgetretene Umsetzungsprobleme
- Wirksamkeit von Planung und Ausführung
- Benutzerfeedback und Dienstauswirkung
- Erfahrungen und Verbesserungsmöglichkeiten

**PIR-Zeitrahmen**: Innerhalb des [von Organisation definierten] Zeitraums (empfohlen: 7 Werktage für Notfalländerungen, 14 Tage für normale Änderungen).

**Begründung**: Strukturierte Überprüfung treibt kontinuierliche Verbesserung voran, erfasst Erfahrungen, identifiziert Prozesslücken und erkennt erfolgreiche Praktiken an.

**Bewertungskriterien**: ISMS-IMP-A.8.32.1 zeigt PIR-Abschlussraten. PIR-Aufzeichnungen belegen Lernen und Verbesserungsmassnahmen.

---

## Anforderungen an die Änderungsklassifizierung

**Zweck**: Anforderungen für die Klassifizierung von Änderungen in drei Kategorien (Standard, Normal, Notfall) definieren. Die Klassifizierung bestimmt den Genehmigungsablauf, die Testanforderungen und den Dokumentationsgrad.

### Anforderungen an Standard-Änderungen

**REQ-CLASSIFY-001: Standard-Änderungskatalog**

[Organisation] MUSS einen Standard-Änderungskatalog führen, der vorab genehmigte, risikoarme Änderungen enthält, die:

- Gut verstandene Auswirkungen und Ergebnisse haben
- Dokumentierten, wiederholbaren Verfahren folgen
- Geringes Scheiternrisiko haben
- Definierte Rollback-Verfahren haben (falls erforderlich)

**Der Standard-Änderungskatalog MUSS folgendes enthalten:**

- Änderungsbeschreibung und -umfang
- Vorbedingungen und Voraussetzungen
- Schritt-für-Schritt-Verfahren
- Geschätzte Dauer
- Rollback-Verfahren
- Risikobewertung (einmalig bei Katalog-Genehmigung durchgeführt)

**Umsetzung**: Der Standard-Änderungskatalog wird im Änderungsmanagementsystem/Dokumentenrepository geführt und ist allen autorisierten Änderungsumsetzer zugänglich. Der Katalog wird vierteljährlich vom Change Manager mit CAB-Beitrag überprüft. Die aktuelle Katalogversion ist in ISMS-IMP-A.8.32.2 (Bewertung von Änderungstypen und -kategorien) dokumentiert.

**Katalogversionskontrolle**: Versionshistorie des Standard-Änderungskatalogs führen, in der dokumentiert ist: (1) Versionsnummer und Datum, (2) vorgenommene Änderungen (Hinzufügungen, Entfernungen, Anpassungen), (3) Grund für Änderungen, (4) Genehmiger. Frühere Versionen werden gemäss Aufbewahrungsrichtlinie der Organisation aufbewahrt.

**Bewertungskriterien**: ISMS-IMP-A.8.32.2 enthält den aktuellen Standard-Änderungskatalog mit allen erforderlichen Elementen. Vierteljährliche Überprüfungsnachweise belegen die Katalogpflege. Änderungstickets referenzieren Katalogeinträge für Standard-Änderungen.

**Begründung**: Standard-Änderungen vereinfachen risikoarme Aktivitäten, reduzieren den CAB-Aufwand und ermöglichen eine schnellere Umsetzung unter Beibehaltung der Kontrolle.

---

**REQ-CLASSIFY-002: Ausführung von Standard-Änderungen**

Standard-Änderungen MÜSSEN:

- Im Änderungsmanagementsystem protokolliert werden (keine CAB-Genehmigung erforderlich)
- Dem dokumentierten Verfahren aus dem Standard-Änderungskatalog folgen
- Von autorisiertem Personal ausgeführt werden
- Eine Verifikation nach der Ausführung beinhalten

Standard-Änderungen KÖNNEN gegebenenfalls selbst bedient werden (z.B. Passwort-Resets über genehmigtes Portal).

**Begründung**: Auch vorab genehmigte Änderungen benötigen Verfolgung für den Audit-Trail und die Vorfallskorrelation.

**Bewertungskriterien**: Änderungstickets belegen, dass Standard-Änderungen protokolliert werden. Die Ausführung folgt Katalogverfahren.

---

**REQ-CLASSIFY-003: Überprüfung von Standard-Änderungen**

[Organisation] MUSS den Standard-Änderungskatalog überprüfen:

- Vierteljährlich (Minimum)
- Nach jedem Scheitern einer Standard-Änderung
- Wenn Nutzungsmuster auf Reklassifizierungsbedarf hindeuten

**Überprüfungskriterien:**

- Erfolgsrate bleibt hoch (>95% empfohlen)
- Keine wesentlichen Vorfälle durch Standard-Änderung verursacht
- Verfahren bleibt genau und vollständig

**Katalogaktualisierungen**: Neue Standard-Änderungen aus erfolgreichen normalen Änderungen hinzufügen. Standard-Änderungen mit Fehlermuster entfernen oder reklassifizieren.

**Begründung**: Regelmässige Überprüfung stellt sicher, dass der Katalog genau bleibt und Standard-Änderungen wirklich risikoarm sind.

**Bewertungskriterien**: Überprüfungsnachweise zeigen vierteljährliche Überprüfungen. Fehlgeschlagene Standard-Änderungen lösen Reklassifizierung aus.

---

### Anforderungen an normale Änderungen

**REQ-CLASSIFY-004: Prozess für normale Änderungen**

Normale Änderungen MÜSSEN dem vollständigen Änderungsmanagementprozess folgen, einschliesslich:

- Formeller Änderungsantrag mit Folgenabschätzung
- Risikobewertung und -klassifizierung
- CAB-Überprüfung und Empfehlung
- Genehmigung durch zuständige Instanz (gemäss REQ-PROCESS-004)
- Testen in Nicht-Produktionsumgebung (gemäss Abschnitt 2.3)
- Kommunikation mit Interessengruppen
- Geplante Umsetzung
- Verifikation nach der Umsetzung
- Review nach der Umsetzung (für hochriskante Änderungen)

**Begründung**: Das vollständige Verfahren bietet angemessene Kontrolle für mittlere und hochriskante Änderungen.

**Bewertungskriterien**: Stichproben normaler Änderungsanträge zeigen, dass der vollständige Prozess eingehalten wurde.

---

**REQ-CLASSIFY-005: Risikobewertung von Änderungen**

[Organisation] MUSS das Risiko normaler Änderungen mit einer [von Organisation definierten] Methodik bewerten, die folgendes berücksichtigt:

- **Auswirkung**: Umfang der betroffenen Systeme/Benutzer, Geschäftskritikalität, Datensensitivität
- **Wahrscheinlichkeit**: Komplexität, Neuheit, Erfahrung des Umsetzers, Vollständigkeit der Tests
- **Risikoniveau**: Kombination aus Auswirkung und Wahrscheinlichkeit

**Ergebnis der Risikobewertung**: Einstufung als Niedrig / Mittel / Hoch / Kritisch, die die Genehmigungsbefugnis und den Prüfungsgrad bestimmt.

**Begründung**: Risikobasierte Bewertung ermöglicht angemessene Aufsicht. Risikoarme Änderungen werden schnell abgewickelt; hochriskante Änderungen werden genau geprüft.

**Bewertungskriterien**: ISMS-REF-A.8.32 stellt die Risikobewertungsmethodik bereit. Änderungsanträge zeigen dokumentierte Risikobewertungen.

---

### Änderungskalender und -planung

**REQ-CLASSIFY-006: Änderungskalender**

[Organisation] MUSS einen Änderungskalender führen, der folgendes identifiziert:

- Geplante Änderungen (Datum, Uhrzeit, betroffene Systeme)
- Änderungssperrzeiten (keine Nicht-Notfalländerungen)
- Sperrfenster (geschäftskritische Perioden)
- Konflikte zwischen Änderungen (überlappende Auswirkungen)

**Änderungssperrzeiten** (Beispiele):

- Jahresendfinanzbuchhaltungsabschluss
- Wichtige Produkteinführungen
- Spitzengeschäftszeiten
- Wesentliche regulatorische Einreichungsperioden

**Begründung**: Der Änderungskalender verhindert Konflikte, schützt kritische Geschäftsperioden und ermöglicht teamübergreifende Koordination.

**Bewertungskriterien**: Änderungskalender gepflegt und zugänglich. Belege zeigen Einhaltung von Änderungssperrzeiten.

---

## Anforderungen an Tests und Validierung

**Zweck**: Anforderungen an Umgebungstrennung und umfassende Tests vor dem Produktions-Deployment definieren. Diese Anforderungen setzen ISO/IEC 27002:2022 Control 8.32 Element (d) um und integrieren sich mit Controls 8.29 (Sicherheitstests), 8.31 (Umgebungstrennung) und 8.33 (Testdatenschutz).

### Anforderungen an die Umgebungstrennung

**REQ-TEST-001: Nicht-Produktionsumgebungen**

[Organisation] MUSS separate Nicht-Produktionsumgebungen für Änderungstests unterhalten:

- **Entwicklungsumgebung**: Für die Erstellung und Unit-Tests von Änderungen
- **Test-/QA-Umgebung**: Für Integrationstests und User Acceptance Testing
- **Staging-/Vorproduktionsumgebung** (optional, aber empfohlen): Für die abschliessende Validierung vor der Produktion

**Anforderungen an die Umgebungsisolierung:**

- Logische oder physische Trennung von der Produktion
- Separate Anmeldeinformationen und Zugriffskontrollen
- Kein direkter Produktionsdatenzugriff aus der Nicht-Produktion
- Klare Kennzeichnung/Identifikation von Nicht-Produktionssystemen

**Begründung**: Getrennte Umgebungen ermöglichen sicheres Testen ohne Produktionsauswirkungen, verhindern, dass Testfehler den Betrieb beeinflussen, und schützen Produktionsdaten.

**Bewertungskriterien**: ISMS-IMP-A.8.32.3 (Bewertung der Umgebungstrennung) dokumentiert die Umgebungsarchitektur. Belege zeigen aufrechterhaltene logische/physische Trennung.

---

**REQ-TEST-002: Workflow zur Umgebungsförderung**

[Organisation] MUSS einen kontrollierten Förderungs-Workflow implementieren:

- **Dev → Test**: Code vollständig, Unit-Tests bestanden
- **Test → Staging**: Integrationstests bestanden, UAT abgeschlossen
- **Staging → Produktion**: Abschliessende Validierung abgeschlossen, Genehmigungen eingeholt

**Förderungskontrollen:**

- Formelle Abzeichnung in jeder Phase
- Verifikationstests in jeder Umgebung
- Dokumentation der Förderungsschritte
- Rollback-Möglichkeit in jeder Phase

**Begründung**: Kontrollierte Förderung verhindert, dass ungetestete Änderungen die Produktion erreichen, bietet mehrere Validierungsprüfpunkte und wahrt die Strenge der Änderungskontrolle.

**Bewertungskriterien**: Förderungsverfahren dokumentiert. Stichprobenänderungen zeigen Progression durch die Umgebungen.

---

**REQ-TEST-003: Schutz der Produktionsumgebung**

[Organisation] MUSS Produktionsänderungen beschränken auf:

- Nur autorisierte Änderungsumsetzer
- Änderungen mit abgeschlossenen Tests (ausser genehmigter Notfalländerungen)
- Geplante Änderungsfenster (ausser Notfällen)
- Änderungen mit entsprechenden Genehmigungen

**Produktionszugriffskontrollen:**

- Privilegiertes Zugriffsmanagement für Produktionsänderungen
- Multi-Faktor-Authentifizierung für Produktionszugriff
- Audit-Protokollierung aller Produktionsänderungen
- Aufgabentrennung (Entwickler deployen nicht in Produktion)

**Begründung**: Produktionsschutz verhindert nicht autorisierte Änderungen, stellt sicher, dass nur getestete Änderungen die Produktion erreichen, und schafft Verantwortlichkeit für Produktionsmodifikationen.

**Bewertungskriterien**: Produktionszugriffskontrollen dokumentiert. Zugriffsprotokolle zeigen eingeschränkten Zugriff. Aufgabentrennung aufrechterhalten.

---

### Testanforderungen

**REQ-TEST-004: Testverfahren**

[Organisation] MUSS Tests verlangen, die dem Änderungsrisiko angemessen sind:

| Änderungsrisiko | Erforderliche Tests |
|----------------|---------------------|
| **Niedrig** | Verifikationstest durch Umsetzer |
| **Mittel** | Funktionstest, Integrationstest |
| **Hoch** | Umfassende Tests: Funktion, Integration, Performance, UAT |
| **Kritisch** | Vollständige Testsuite: Funktion, Integration, Performance, Sicherheit, UAT, Disaster Recovery |

**Mindest-Testanforderungen (alle Änderungen):**

- Funktionstest (Änderung erreicht beabsichtigten Zweck)
- Integrationstest (Änderung beschädigt keine abhängigen Systeme)
- Rollback-Test (Rollback-Verfahren verifiziert)

**Durchsetzung**: Das Änderungsmanagementsystem erzwingt Testanforderungen, indem die Dokumentation von Testergebnissen erforderlich ist, bevor der Genehmigungsablauf zur Produktions-Deployment-Phase übergeht. Hoch- und kritisch-riskante Änderungen können ohne dokumentierten Nachweis nicht für das Produktions-Deployment genehmigt werden: (1) Testplan abgeschlossen, (2) Abnahmekriterien erfüllt, (3) Testergebnisse vom designierten Genehmiger gezeichnet. Die Testdurchsetzung wird durch den Audit-Trail des Änderungsantrags im Änderungsmanagementsystem überprüft.

**Begründung**: Risikoangemessene Tests balancieren gründliche Validierung mit Umsetzungsgeschwindigkeit.

**Bewertungskriterien**: Änderungsanträge zeigen durchgeführte Tests und dokumentierte Ergebnisse. Audit-Trail belegt Durchsetzung von Test-Gates.

---

**REQ-TEST-005: Integration von Sicherheitstests**

[Organisation] MUSS Sicherheitstests in Änderungen einbeziehen, die:

- Authentifizierungs- oder Autorisierungsmechanismen betreffen
- Sicherheitskontrollen oder -konfigurationen ändern
- Neue externe Schnittstellen bereitstellen
- Eingeschränkte oder vertrauliche Daten verarbeiten
- Kryptografische Implementierungen betreffen

**Arten von Sicherheitstests:**

- Schwachstellenscanning (automatisiert)
- Überprüfung der Sicherheitskonfiguration
- Penetrationstests (für hochriskante Änderungen an externen Schnittstellen)
- Code-Sicherheitsprüfung (für Anwendungsänderungen)

**Integration mit Control 8.29**: Sicherheitstestanforderungen stimmen mit ISMS-POL-A.8.25-26-29 (Secure Development Lifecycle) überein.

**Begründung**: Sicherheitstests verhindern die Einführung von Schwachstellen, validieren die Wirksamkeit von Sicherheitskontrollen und unterstützen Defense-in-Depth.

**Bewertungskriterien**: Sicherheitsrelevante Änderungen zeigen durchgeführte Sicherheitstests. Integration mit dem sicheren Entwicklungslebenszyklus nachgewiesen.

---

**REQ-TEST-006: Abnahmekriterien**

[Organisation] MUSS Abnahmekriterien für Änderungen definieren, einschliesslich:

- Funktionale Anforderungen erfüllt
- Leistungsanforderungen erfüllt (keine inakzeptable Verschlechterung)
- Integrationspunkte validiert
- Sicherheitsanforderungen validiert
- Keine kritischen oder hochschweren Fehler
- Benutzerakzeptanz eingeholt (soweit zutreffend)

**Abnahmezeichnung**: Vor dem Produktions-Deployment erforderlich für mittel- und hochriskante Änderungen.

**Begründung**: Klare Abnahmekriterien verhindern subjektive "sieht gut aus"-Bewertungen, stellen sicher, dass Änderungen wirklich produktionsreif sind, und dokumentieren die formelle Abnahme.

**Bewertungskriterien**: Änderungsanträge definieren Abnahmekriterien. Testergebnisse zeigen erfüllte Kriterien. Zeichnungen dokumentiert.

---

### Testdatenmanagement

**REQ-TEST-007: Schutz von Produktionsdaten**

[Organisation] MUSS Produktionsdaten in Testumgebungen schützen:

- Produktionsdaten DÜRFEN NICHT ohne Schutz in Testumgebungen verwendet werden
- Wenn Produktionsdaten für Tests erforderlich sind, MÜSSEN Daten gemäss ISMS-POL-A.8.11 (Datenmaskierung) maskiert/anonymisiert werden
- Synthetische Testdaten SOLLTEN verwendet werden, wo durchführbar
- Testdaten MÜSSEN gemäss ISMS-POL-A.5.12 (Klassifizierung von Informationen) klassifiziert und geschützt werden

**Integration mit Control 8.33**: Testdatenanforderungen stimmen mit ISO/IEC 27001:2022 Control 8.33 (Testinformationen) überein.

**Begründung**: Ungeschützte Produktionsdaten in Testumgebungen schaffen Datenschutzverletzungsrisiken, regulatorische Nichteinhaltungsrisiken und unautorisierte Zugriffsrisiken.

**Bewertungskriterien**: Testumgebungen zeigen Datenmaskierung/Anonymisierung oder synthetische Daten. Keine ungeschützten Produktionsdaten in Tests.

---

## Anforderungen an Notfalländerungen

**Zweck**: Anforderungen für die beschleunigte Behandlung dringender Änderungen definieren und dabei Kontrolle und Aufsicht aufrechterhalten. Diese Anforderungen setzen ISO/IEC 27002:2022 Control 8.32 Element (f) um.

### Kriterien für Notfalländerungen

**REQ-EMERGENCY-001: Notfallklassifizierung**

[Organisation] MUSS Änderungen nur dann als Notfall klassifizieren, wenn:

- Ein aktiver Sicherheitsvorfall oder eine Schwachstelle behoben wird
- Ein kritischer Dienstausfall wiederhergestellt wird
- Ein unmittelbarer Systemausfall verhindert wird
- Eine dringende regulatorische Anforderung adressiert wird
- Eine aktive Datenpanne gemindert wird

**Notfalländerungen DÜRFEN NICHT verwendet werden für:**

- Komfort oder Termindruck
- Schlechte Planung
- Routinearbeiten
- Gewünschte Funktionen

**Begründung**: Die Notfallbezeichnung ermöglicht ein beschleunigtes Verfahren, erfordert aber eine starke Begründung. Übermässige Nutzung von Notfalländerungen deutet auf Prozessversagen hin.

**Bewertungskriterien**: Notfall-Änderungsanträge weisen eine gültige Begründung nach. Der Prozentsatz der Notfalländerungen wird verfolgt (Ziel: <5% aller Änderungen).

---

**REQ-EMERGENCY-005: Schwellenwertmanagement für Notfalländerungen**

[Organisation] MUSS den Prozentsatz der Notfalländerungen monatlich überwachen. Wenn Notfalländerungen den Zielschwellenwert (<5% aller Änderungen) zwei aufeinanderfolgende Monate überschreiten, MUSS der Change Manager:

- Eine Ursachenanalyse zur Identifikation systemischer Probleme durchführen
- Ergebnisse dem CAB mit Abhilfemassnahmen vorlegen
- Korrektive Massnahmen innerhalb von 30 Tagen umsetzen
- Schwellenwertüberschreitung und Abhilfeplan dem ISB melden

**Bewertungskriterien**: Monatlicher Prozentsatz der Notfalländerungen wird in den Zusammenfassungs-Dashboard-Tabellenblättern der Bewertungsarbeitsmappen verfolgt (ISMS-IMP-A.8.32.1-4). Belege zeigen Ursachenanalyse und korrektive Massnahmen bei Schwellenwertüberschreitung.

---

### Genehmigung von Notfalländerungen

**REQ-EMERGENCY-002: Beschleunigter Genehmigungsprozess**

Notfalländerungen MÜSSEN eine Genehmigung einholen von:

- IT-Betriebsleiter oder ISB (Minimum)
- Weitere Genehmigungen, soweit zeitlich möglich
- Retrospektive CAB-Überprüfung innerhalb des [von Organisation definierten] Zeitraums (empfohlen: 24–48 Stunden)

**Genehmigungsdokumentation:**

- Notfallbegründung
- Bewertetes Risiko und Auswirkung
- Betrachtete Alternativen
- Risikoakzeptanzentscheidung

**Begründung**: Beschleunigter Genehmigungsprozess ermöglicht eine schnelle Reaktion unter Beibehaltung der Führungsaufsicht und Verantwortlichkeit.

**Bewertungskriterien**: Notfalländerungen zeigen angemessene Genehmigungen. Retrospektive CAB-Überprüfungen dokumentiert.

---

### Testen von Notfalländerungen

**REQ-EMERGENCY-003: Risikogerechtes Testen**

Notfalländerungen MÜSSEN einem den Zeitbeschränkungen angemessenen Testen unterzogen werden:

- **Minimum**: Verifikationstest durch Umsetzer in isolierter Umgebung (sofern möglich)
- **Bevorzugt**: Eingeschränktes Testen in Testumgebung
- **Wenn kein Testen möglich**: Dokumentierte Risikoakzeptanz und Rollback-Plan

**Zulässige Testabkürzungen (dokumentiert und begründet):**

- Abgekürzte Testfälle
- Testen in Produktion mit Monitoring
- Paralleles Deployment mit Fallback
- Tests auf kritische Funktionalität beschränkt

**Begründung**: Balanciert Dringlichkeit mit Kontrolle. Einige Tests sind besser als keine Tests. Risikoakzeptanz ist explizit, wenn Tests nicht durchführbar sind.

**Bewertungskriterien**: Notfalländerungen dokumentieren durchgeführte Tests oder Risikoakzeptanz für Testabkürzungen.

---

### Überprüfung nach dem Notfall

**REQ-EMERGENCY-004: Obligatorisches Review nach der Umsetzung**

[Organisation] MUSS für ALLE Notfalländerungen innerhalb des [von Organisation definierten] Zeitraums (empfohlen: 5 Werktage) ein Review nach der Umsetzung durchführen, das folgendes adressiert:

- Notfallbegründung validiert
- Verfügbare Alternativansätze
- Wirksamkeit der Änderung
- Prozessverbesserungen zur Vermeidung künftiger Notfälle
- Ob die Änderung dem Standard-Änderungskatalog hinzugefügt werden sollte

**Teilnehmer der Überprüfung**: Change Manager, ISB, CAB-Mitglieder, Umsetzer.

**Begründung**: Notfalländerungen deuten oft auf Prozesslücken hin. Strukturierte Überprüfung treibt Verbesserungen voran und verhindert wiederkehrende Notfälle.

**Bewertungskriterien**: Alle Notfalländerungen haben PIR innerhalb des Zeitrahmens abgeschlossen. PIR-Aufzeichnungen belegen Lernen und Verbesserungsmassnahmen.

---

### Zeitrahmenspezifikationen

**REQ-PROCESS-013: Organisationsdefinierte Zeitrahmen**

[Organisation] MUSS spezifische Zeitrahmen für Änderungsmanagementaktivitäten in ISMS-IMP-A.8.32.1 (Bewertung des Änderungsprozesses) dokumentieren, basierend auf Betriebsanforderungen und Risikobewertung. Erforderliche Zeitrahmenspezifikationen:

| Aktivität | Empfohlener Standardwert | Referenz |
|-----------|--------------------------|----------|
| Dokumentationsaktualisierungen nach Änderungen | 5 Werktage | REQ-PROCESS-010 |
| Auslöser für Kontinuitätsplanüberprüfung | Innerhalb des Änderungsgenehmigungsprozesses | REQ-PROCESS-011 |
| Review nach der Umsetzung (normale Änderungen) | 14 Werktage | REQ-PROCESS-012 |
| Review nach der Umsetzung (Notfalländerungen) | 5 Werktage | REQ-EMERGENCY-004 |
| Retrospektive CAB-Überprüfung für Notfälle | 24–48 Stunden | REQ-EMERGENCY-002 |
| Vorlaufzeit für Stakeholder-Kommunikation | Gemäss Betriebsanforderungen | REQ-PROCESS-006 |
| Aufbewahrung von Änderungsaufzeichnungen | 7 Jahre (Audit), 3 Jahre (Betrieb) | REQ-PROCESS-009 |

Zeitrahmen MÜSSEN bei der jährlichen Richtlinienüberprüfung überprüft und aktualisiert werden, um betriebliche Realitäten widerzuspiegeln.

---

# Rollen und Verantwortlichkeiten

[Organisation] MUSS klare Verantwortlichkeiten für das Änderungsmanagement mit einer RACI-Matrix festlegen (V=Verantwortlich, A=Accountable, B=Beratend, I=Informiert).

## Schlüsselrollen

**Change Manager**:

- **Accountable** für den Änderungsmanagementprozess
- Führt den Vorsitz im Change Advisory Board (CAB)
- Pflegt den Standard-Änderungskatalog
- Verfolgt Änderungsmetriken und -trends
- Treibt kontinuierliche Verbesserung

**Change Advisory Board (CAB)**:

- Überprüft und empfiehlt zu normalen und Notfalländerungen
- Identifiziert Konflikte zwischen Änderungen
- Bewertet Risiken und Auswirkungen
- Multidisziplinäre Mitgliedschaft (IT-Betrieb, Sicherheit, Geschäftsbereiche, Fachexperten)

**Änderungsantragsteller**:

- Reicht Änderungsanträge mit vollständigen Informationen ein
- Holt geschäftliche Begründung und Unterstützung ein
- Nimmt an der Folgenabschätzung teil

**Änderungsumsetzer**:

- Führt genehmigte Änderungen gemäss dokumentierten Verfahren aus
- Überprüft Voraussetzungen und Abhängigkeiten
- Führt Verifikation nach der Umsetzung durch
- Dokumentiert Umsetzungsschritte und Probleme

**Systemeigentümer**:

- Überprüft Änderungen an eigenen Systemen
- Liefert Folgenabschätzung für eigene Systeme
- Genehmigt Änderungen gemäss Genehmigungskompetenzmatrix
- Accountable für Systemverfügbarkeit und -sicherheit

**ISB / Informationssicherheit**:

- Überprüft sicherheitsrelevante Änderungen
- Liefert Sicherheitsrisikobewertung
- Genehmigt hochriskante Änderungen
- Überwacht änderungsbedingte Sicherheitsvorfälle

**IT-Betriebsleiter**:

- Genehmigt mittel- und hochriskante Änderungen
- Führt den Vorsitz bei Notfall-CAB-Sitzungen
- Koordiniert Änderungsfenster
- Löst Konflikte und Eskalationen

**Geschäftsleitung**:

- Genehmigt kritisch-riskante Änderungen
- Gibt strategische Richtung für das Änderungsmanagement vor
- Erhält Änderungsmetriken und Risikoberichte

## RACI-Matrix

[Detaillierte RACI-Matrix, die Verantwortlichkeiten für jede Änderungsmanagementaktivität über alle Rollen hinweg definiert – vollständige Matrix in ISMS-IMP-A.8.32.1]

---

# Richtlinien-Governance

## Richtlinieneigentümerschaft

**Richtlinieneigentümer**: Informationssicherheitsbeauftragter (ISB)

**Verantwortlichkeiten**:

- Gesamtverantwortung für das Änderungsmanagement-Richtlinienrahmenwerk
- Richtlinienaktualisierungen und -versionen genehmigen
- Ausrichtung der Richtlinie auf ISO/IEC 27001:2022 Anforderungen sicherstellen
- Wirksamkeit der Richtlinie an die Geschäftsleitung berichten
- Richtlinienausnahmen autorisieren

## Richtlinienlebenszyklus

### Richtlinienüberprüfungsplan

**Jährliche Überprüfung** (obligatorisch):

- Umfassende Überprüfung der Richtlinie
- Zeitpunkt: Q4 jedes Jahres (empfohlen)
- Geleitet von: Change Manager
- Teilnehmer: CAB, Sicherheitsteam, IT-Betrieb, Rechts-/Compliance-Abteilung

**Anlassbezogene Überprüfungen**:

- Aktualisierungen des ISO/IEC 27001 Standards, die Control 8.32 betreffen
- Wesentliche regulatorische Änderungen
- Wesentliche Organisationsänderungen
- Technologieänderungen (neue Änderungsmanagement-Tools)
- Wesentliche Änderungsmanagement-Vorfälle oder -Fehler
- Audit-Findings, die Richtlinienaktualisierungen erfordern

### Richtlinienaktualisierungsprozess

**Standard-Richtlinienänderungen:**
1. Änderungsantrag an Richtlinieneigentümer (ISB)
2. Folgenabschätzung (betroffene Interessengruppen, Systeme, Prozesse)
3. Stakeholder-Konsultation (Change Manager, IT-Betrieb, CAB, Rechtsabteilung)
4. Entwurfsrevision
5. Überprüfungszeitraum (14 Tage)
6. Genehmigung (erforderliche Genehmiger zeichnen ab)
7. Kommunikation (Richtlinienaktualisierungen an alle Mitarbeitenden kommuniziert)
8. Umsetzung (30-tägiger Übergangszeitraum, sofern nicht dringend)

**Notfall-Richtlinienänderungen:**

- Verkürzter Überprüfungszeitraum (3–5 Werktage)
- Notfallgenehmigung durch ISB mit Executive-Benachrichtigung
- Sofortige Umsetzung
- Retrospektive Stakeholder-Überprüfung innerhalb von 30 Tagen

## Ausnahmenmanagement

### Wann Ausnahmen angemessen sind

**Gültige Ausnahmeszenarien:**

- Technische Einschränkungen verhindern vollständige Compliance
- Geschäftliche Umstände erfordern vorübergehende Abweichung
- Alternative kompensierende Kontrollen bieten gleichwertigen Schutz
- Notfallsituationen (formalisiert über den Notfalländerungsprozess)

**Ausnahmen NICHT angemessen bei:**

- Komfort oder Präferenz
- Ressourcenengpässen
- Ablehnung der Richtlinienabsicht
- "So haben wir es immer gemacht"

### Ausnahmeantragsprozess

**Ein Ausnahmeantrag MUSS enthalten:**

- Anforderung, für die eine Ausnahme beantragt wird
- Geschäftliche oder technische Begründung
- Dauer der Ausnahme
- Kompensierende Kontrollen (falls vorhanden)
- Restrisikobewertung
- Ausnahmeeigentümer und Genehmiger

**Ausnahmegenehmigungsbefugnis:**

- Ausnahmen für Standardanforderungen: Change Manager
- Ausnahmen für kritische Anforderungen: ISB
- Alle Ausnahmen: Risikoakzeptanz durch Systemeigentümer

**Ausnahmenüberprüfung**: Alle Ausnahmen werden vierteljährlich überprüft. Abgelaufene Ausnahmen erfordern eine Erneuerung oder Behebung.

## Compliance-Monitoring

**Compliance-Metriken** (verfolgt über Zusammenfassungs-Dashboard-Tabellenblätter in Bewertungsarbeitsmappen ISMS-IMP-A.8.32.1-4):

- Änderungserfolgsquote
- Prozentsatz der Notfalländerungen
- PIR-Abschlussquote
- Nutzungsgrad des Standard-Änderungskatalogs
- Änderungsbedingte Vorfälle
- Durchschnittliche Änderungsdauer
- CAB-Sitzungsfrequenz und Anwesenheit

**Compliance-Berichterstattung**:

- Vierteljährliches Zusammenfassungs-Dashboard an ISB
- Jährliche Compliance-Zusammenfassung an die Geschäftsleitung
- Verfolgung von Audit-Findings und Behebung

## Integration in das ISMS

**Das Änderungsmanagement integriert sich mit verwandten ISO 27001 Controls:**

- **A.5.30** (IKT-Kontinuität): Kontinuitätspläne nach Infrastrukturänderungen aktualisiert
- **A.5.37** (Dokumentierte Verfahren): Betriebsdokumentation nach Änderungen aktualisiert
- **A.8.19** (Software-Installation): Software-Deployment-Kontrollen
- **A.8.29** (Sicherheitstests): Sicherheitstests vor dem Deployment
- **A.8.31** (Umgebungstrennung): Dev/Test/Prod-Isolierung
- **A.8.33** (Testinformationen): Produktionsdatenschutz im Test

**Informationsflüsse:**

- **Änderung → Vorfall**: Fehlgeschlagene Änderungen lösen Incident-Response aus
- **Änderung → Asset**: Änderungen aktualisieren das Asset-Inventar
- **Änderung → Kontinuität**: Infrastrukturänderungen aktualisieren Kontinuitätspläne
- **Änderung → Dokumentation**: Änderungen aktualisieren Systemdokumentation

---

# Integration und Ressourcen

## Integration mit verwandten Controls

Das Änderungsmanagement (A.8.32) integriert sich mit sechs verwandten ISO 27001 Controls:

**Control 5.30 – IKT-Kontinuitätsplanung**:

- Kontinuitätspläne werden aktualisiert, wenn Infrastrukturänderungen RTO/RPO betreffen
- Das Änderungsmanagement berücksichtigt Kontinuitätsauswirkungen
- DR-Verfahren werden nach relevanten Änderungen aktualisiert

**Control 5.37 – Dokumentierte Betriebsverfahren**:

- Betriebsverfahren werden nach Systemänderungen aktualisiert
- Runbooks und Leitfäden zur Fehlerbehebung werden aktuell gehalten
- Dokumentationsaktualisierungen werden in Änderungsaufzeichnungen verfolgt

**Control 8.19 – Installation von Software auf Betriebssystemen**:

- Software-Installation folgt dem Änderungsmanagementprozess
- Installationskontrollen werden durch Änderungsgenehmigung durchgesetzt
- Software-Änderungen unterliegen Testanforderungen

**Control 8.29 – Sicherheitstests in Entwicklung und Abnahme**:

- Sicherheitstests sind in Änderungstestverfahren integriert
- Sicherheitsrelevante Änderungen werden zusätzlich validiert
- Sicherheitstestergebnisse für Abnahme erforderlich

**Control 8.31 – Trennung von Entwicklungs-, Test- und Produktionsumgebungen**:

- Umgebungstrennung wird durch den Änderungsförderungs-Workflow durchgesetzt
- Produktionsumgebung ist vor nicht autorisierten Änderungen geschützt
- Tests werden in Nicht-Produktionsumgebungen durchgeführt

**Control 8.33 – Testinformationen**:

- Produktionsdaten sind in Testumgebungen geschützt
- Testdatenanforderungen werden durch den Änderungsprozess durchgesetzt
- Datenmaskierung/Anonymisierung wird vor dem Testen validiert

## Umsetzungsressourcen

**Umsetzungsleitlinien** (ISMS-IMP-A.8.32-Suite):

[Organisation] setzt Änderungsmanagement-Kontrollen mit strukturierten Bewertungsarbeitsmappen um:

- **ISMS-IMP-A.8.32.1-UG/TG**: Bewertung des Änderungsprozesses (Prozessreife, Tools, Workflows, Genehmigungen, Dokumentation)
- **ISMS-IMP-A.8.32.2-UG/TG**: Bewertung von Änderungstypen und -kategorien (Standard-Änderungskatalog, normale Änderungs-Workflows, Risikoklassifizierung)
- **ISMS-IMP-A.8.32.3-UG/TG**: Bewertung der Umgebungstrennung (Dev/Test/Prod-Architektur, Förderungs-Workflows, Zugriffskontrollen)

**Technische Referenz** (Nicht-ISMS):

- **ISMS-REF-A.8.32**: Änderungsmanagement-Referenz (Tool-Anforderungen, Formularvorlagen, Risikobewertungsmethodik, Kurzanleitungen)

**Bewertungstools**:

- Python-generierte Excel-Arbeitsmappen mit automatisierten Compliance-Berechnungen
- Datenvalidierungs-Dropdowns (Antwortwerte: Ja/Nein/Teilweise/Geplant/K.A.)
- KPI-Berechnungen und Gap-Analyse
- Evidenzregister und Remediation-Tracking
- Executive-Dashboard mit Trendanalyse

**Automatisierung**: Alle Bewertungsarbeitsmappen werden über Python-Skripte generiert, um Konsistenz, Wiederholbarkeit und Wartbarkeit sicherzustellen.

## Schulung und Bewusstsein

**Allgemeines Bewusstsein** (alle Mitarbeitenden):

- Jährliches Schulungsmodul zum Änderungsmanagement
- Benutzerverantwortlichkeiten bei Änderungen
- Wie Änderungen beantragt werden
- Erkennen nicht autorisierter Änderungen

**Technische Schulung** (Änderungsumsetzer):

- Schulung zu Änderungsmanagementprozessen und -tools
- Verfahren aus dem Standard-Änderungskatalog
- Testanforderungen und Verifikation
- Ausführung von Rollback-Verfahren

**CAB-Schulung** (CAB-Mitglieder):

- CAB-Verantwortlichkeiten und -Befugnisse
- Techniken zur Folgenabschätzung
- Risikoeinstufungsmethodik
- Konfliktidentifikation

**Management-Schulung** (Genehmigungsinstanzen):

- Verantwortlichkeiten der Genehmigungsbefugnis
- Risikoakzeptanzentscheidungen
- Ausnahmenmanagement
- Metriken-Interpretation

---

# Genehmigungsnachweis

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date] |
| **IT-Leiter (ITL)** | [Name] | [Date] |
| **IT-Betriebsleiter** | [Name] | [Date] |
| **Rechts-/Compliance-Beauftragter** | [Name] | [Date] |
| **Geschäftsleitung (GF)** | [Name] | [Date] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen an das Änderungsmanagement fest. Umsetzungsverfahren, Vorlagen, Tools und Kurzanleitungen sind in ISMS-IMP-A.8.32 (Bewertungsarbeitsmappen) und ISMS-REF-A.8.32 (Technische Referenz) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-29 -->
