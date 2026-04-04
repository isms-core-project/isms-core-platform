<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.37-DE:operational:OP-POL:a.5.37 -->
**ISMS-OP-POL-A.5.37 — Dokumentierte Betriebsverfahren**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Dokumentierte Betriebsverfahren |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.5.37 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Initiale operative Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt von**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Control A.5.37 — Documented operating procedures
- ISO/IEC 27001:2022 Clause 7.5 — Documented information

**Verwandte Annex-A-Controls**:

| Control | Bezug zu Dokumentierten Betriebsverfahren |
|---------|------------------------------------------|
| A.5.1 Richtlinien für Informationssicherheit | Richtlinien definieren Anforderungen; Verfahren setzen sie um |
| A.5.24–28 Incident-Management-Lebenszyklus | Incident-Response-Verfahren gemäss dieser Richtlinie dokumentiert |
| A.6.3 Informationssicherheitsbewusstsein, -ausbildung und -schulung | Mitarbeitende in relevanten Verfahren geschult |
| A.8.32 Change Management | Verfahren über Change-Management-Prozess aktualisiert |
| A.8.9 Konfigurationsmanagement | Konfigurationsverfahren dokumentiert |

**Verwandte interne Richtlinien**:

- Informationssicherheitsrichtlinie
- Change-Management-Richtlinie
- Incident-Management-Richtlinie
- Richtlinie zur Informationssicherheits-Sensibilisierung und -Schulung

---

# Richtlinie Dokumentierte Betriebsverfahren

## Zweck

Zweck dieser Richtlinie ist es, sicherzustellen, dass Betriebsverfahren für Informationsverarbeitungseinrichtungen dokumentiert, gepflegt und dem Personal zur Verfügung gestellt werden, das sie benötigt, um konsistente, sichere und auditierbare Abläufe zu ermöglichen.

Diese Richtlinie unterstützt das Schweizer nDSG (revDSG) und die Datenschutzverordnung (DSV), indem dokumentierte technische und organisatorische Massnahmen entsprechend dem Risiko umgesetzt werden. Dokumentierte Verfahren belegen das Engagement der Organisation für systematischen Datenschutz und Sicherheitskontrollen. Sofern die Organisation Daten von Personen in der EU/EWR verarbeitet, gelten auch die DSGVO-Anforderungen.

## Geltungsbereich

Alle Mitarbeitenden und Drittanwender.

Alle Betriebsverfahren für Informationsverarbeitungseinrichtungen, Systeme, Anwendungen und Sicherheitskontrollen, die von der Organisation oder in ihrem Auftrag betrieben werden.

Alle Umgebungen: Produktion, Test, Entwicklung und Disaster Recovery.

## Grundsatz

Betriebsverfahren für Informationsverarbeitungseinrichtungen müssen dokumentiert und dem Personal zur Verfügung gestellt werden, das sie benötigt. Für das Informationssicherheitsmanagementsystem erforderliche Dokumente werden gesteuert, verwaltet und sind verfügbar. Ohne dokumentierte, getestete und gepflegte Verfahren ist ein sicherer Betrieb nicht möglich.

---

## Obligatorisch zu dokumentierende Verfahren

Die Organisation soll Betriebsverfahren für folgende Kategorien dokumentieren:

### Sicherheitsbetrieb

| Verfahrenskategorie | Beispiele |
|--------------------|-----------|
| **Zugriffsmanagement** | Benutzerbereitstellung, Zugriffsüberprüfung, Notfallzugang, Deprovisionierung |
| **Incident Response** | Erkennung, Triage, Eskalation, Kommunikation, Beweissicherung |
| **Schwachstellenmanagement** | Scanning, Bewertung, Priorisierung, Behebung |
| **Backup und Recovery** | Backup-Ausführung, Verifizierung, Wiederherstellungstests |
| **Monitoring und Protokollüberprüfung** | Protokollüberprüfung, Alarm-Response, Eskalation |
| **Patch-Management** | Bewertung, Tests, Deployment, Verifizierung |

### Systembetrieb

| Verfahrenskategorie | Beispiele |
|--------------------|-----------|
| **Start und Herunterfahren** | Systemstart, geordnetes Herunterfahren, Notabschaltung |
| **Stapelverarbeitung** | Job-Scheduling, Monitoring, Fehlerbehandlung |
| **Fehlerbehandlung** | Fehlererkennung, Protokollierung, Eskalation |
| **Medienhandling** | Aufbewahrung, Transport, Entsorgung von Wechseldatenträgern |
| **Systemwartung** | Routinewartung, Housekeeping, Gesundheitsprüfungen |

### Administrativer Betrieb

| Verfahrenskategorie | Beispiele |
|--------------------|-----------|
| **Benutzersupport** | Antragsbearbeitung, Problemlösung |
| **Änderungsimplementierung** | Vorbereitungsprüfungen, Ausführung, Nachkontrolle |
| **Disaster Recovery** | DR-Aktivierung, Recovery-Ausführung, Rückkehr zum Normalbetrieb |

---

## Erstellung und Aktualisierung von Verfahren

### Dokumentationsstandards

Alle Betriebsverfahren sollen folgende obligatorische Elemente enthalten:

| Element | Anforderung |
|---------|-------------|
| **Dokument-ID** | Eindeutiger Bezeichner gemäss der Namenskonvention der Organisation: **[Format angeben, z. B. "PROC-[KATEGORIE]-[###]", wobei KATEGORIE = SEC (Sicherheit), OPS (Betrieb), ADM (Administration), DR (Disaster Recovery)]**. Beispiele: PROC-SEC-001 (Benutzerbereitstellung), PROC-DR-005 (Backup-Wiederherstellung) |
| **Titel** | Klarer, beschreibender Titel |
| **Version** | Versionsnummer und Datum |
| **Eigentümer** | Designierter Verfahrens-Eigentümer (Name und Rolle), verantwortlich für Richtigkeit und Aktualität |
| **Stellvertretender Eigentümer** | Designierter Stellvertreter für kritische Verfahren, um Single Points of Failure zu vermeiden |
| **Genehmigung** | Name des Genehmigenden und Datum |
| **Zweck** | Warum das Verfahren existiert |
| **Geltungsbereich** | Was das Verfahren abdeckt |
| **Voraussetzungen** | Erforderliche Bedingungen, Zugriff, Tools |
| **Schritte** | Sequenzielle, nummerierte Schritte |
| **Erwartete Ausgaben** | Was der Bediener in Schlüsselschritten sehen sollte |
| **Verifizierung** | Wie der erfolgreiche Abschluss bestätigt wird |
| **Rollback** | Wiederherstellungsschritte bei Verfahrensversagen |
| **Referenzen** | Verwandte Dokumente und Kontakte |

### Qualitätsanforderungen

- In einer für das Zielpublikum verständlichen Sprache geschrieben.
- Ausreichend detailliert, dass ein unvertrauter, aber kompetenter Bediener das Verfahren ausführen könnte.
- Frei von Mehrdeutigkeiten und unausgesprochenen Annahmen.
- Vor der Produktionsnutzung getestet.
- Vor der Veröffentlichung überprüft und genehmigt.

### Format und Medium

Verfahren sollen in elektronischem Format mit Standard-Office-Anwendungen oder nativen Betriebssystemen erstellt werden. Die Organisation soll eine angemessene Identifizierung und Beschreibung (Titel, Datum, Autor, Referenznummer), ein einheitliches Format (Sprache, Softwareversion, Grafiken) sowie Überprüfung und Genehmigung auf Eignung und Angemessenheit sicherstellen.

---

## Dokumentenspeicherung und Verfügbarkeit

### Autoritative Ablage

Verfahren sollen im Dokumentenmanagementsystem der Organisation gespeichert werden: **[Angabe: SharePoint, Confluence, Notion oder Äquivalent]**.

**Ablageort**: [URL oder Pfad: z. B. "https://company.sharepoint.com/sites/ISMS/Verfahren"]

**Zugriff**: Der Zugriff auf das Dokumentenrepository ist gemäss der Zugriffssteuerungsrichtlinie auf autorisiertes Personal beschränkt. Alle Mitarbeitenden können Verfahren einsehen, die für ihre Rolle relevant sind; nur Verfahrens-Eigentümer und designiertes Personal können bearbeiten.

Dieses Repository ist die einzige Quelle der Wahrheit für Betriebsverfahren. Lokale Kopien und Duplikate sind verboten, mit Ausnahme genehmigter Offline-Notfallkopien.

### Verfügbarkeitsanforderungen

| Verfahrenstyp | Verfügbarkeitsanforderung |
|---------------|--------------------------|
| **Notfall- und DR-Verfahren** | Gedruckte Kopien + Offline-Digitalkopie, vierteljährlich getestet |
| **Kritischer Betrieb** | 24/7 verfügbar mit redundantem Zugang |
| **Standardbetrieb** | 24/7 verfügbar, wo kundenseitige Infrastruktur unterstützt wird; Mindestens während Geschäftszeiten für andere |
| **Referenzverfahren** | Auf Abruf verfügbar |

### Notfall-Offline-Paket

Für kritische Dienste soll die Organisation ein Offline-Paket führen, das mindestens folgendes enthält:

- DR-Aktivierungsverfahren.
- Break-Glass / Notfallzugangsverfahren.
- Kernnetzwerkzugangsverfahren.
- Backup-Wiederherstellungsverfahren für kritische Systeme.

**Aufbewahrung und Zugang**:

- **Primärer Standort**: [Angabe: Verschlossener Tresor im Serverraum / feuerfester Schrank im Büro / gesicherte Aussenstelle]
- **Backup-Standort**: [Angabe: Gesicherter Heimtresor des IT Operations Managers / Backup-Aussenstelle]
- **Verwahrer**: IT Operations Manager ([Name oder "Aktueller Verwahrer: siehe Kontaktliste"])
- **Zugangsautorisierung**: ISB, GF, IT Operations Manager und [designierte Notfallkontakte]
- **Zugangsverfahren**: Break-Glass-Umschlag oder versiegelter Behälter; Zugang mit Datum, Zugangsperson und Grund protokolliert

Aktualität soll **vierteljährlich** mit einer aufgezeichneten Checkliste verifiziert werden, die die Versionsübereinstimmung mit dem autoritativen Repository bestätigt.

**Jährliches Audit**: Beim jährlichen internen Audit soll das Offline-Paket geöffnet und gegen das autoritative Repository verifiziert werden (100 % Versionsübereinstimmung erforderlich).

---

## Versionskontrolle und Genehmigung

### Richtliniendokumente

- Richtliniendokumente unterliegen Änderungen als Ergebnis des kontinuierlichen Verbesserungsprozesses.
- Änderungen an Richtliniendokumenten werden vom Informationssicherheitsmanagement-Team vorgenommen und vom Management-Review-Team genehmigt.
- Versionshistorie wird geführt und erfasst mindestens: Autor, Datum, Änderungsbeschreibung und neue Versionsnummer.

### Betriebsdokumente und Aufzeichnungen

- Betriebsdokumente und Aufzeichnungen werden vom Prozesseigentümer als Teil des Tagesgeschäfts und nach Bedarf aktualisiert.
- Versionshistorie wird geführt und erfasst mindestens: Autor, Datum, Änderungsbeschreibung und neue Versionsnummer.
- Benutzern soll nur die neueste genehmigte Version präsentiert werden.
- Frühere Versionen sollen archiviert (nicht gelöscht) werden für den Audit-Trail.
- Aktualisierungen sollen dem betroffenen Personal mitgeteilt werden.

---

## Verfahrensüberprüfung und -pflege

### Überprüfungsplan

| Überprüfungstyp | Häufigkeit | Umfang |
|----------------|-----------|--------|
| **Geplante Überprüfung** | Jährlich (Minimum) | Alle Verfahren |
| **Post-Incident-Überprüfung** | Nach relevantem Incident | Betroffene Verfahren |
| **Änderungsausgelöste Überprüfung** | Nach Systemänderungen | Betroffene Verfahren |
| **Regulatorische Überprüfung** | Nach regulatorischen Änderungen | Betroffene Verfahren |

### Überprüfungsaktivitäten

- Richtigkeit gegen aktuelle Systeme und Prozesse verifizieren.
- Für Technologie- und Personaländerungen aktualisieren.
- Basierend auf Benutzer-Feedback und Erkenntnissen verbessern.
- Mit aktuellen Sicherheitsanforderungen abstimmen.
- Referenzen auf verwandte Dokumente aktualisieren.

### Kontinuierliche Verbesserung und Benutzer-Feedback

Mitarbeitende, die Verfahren nutzen, sollen folgendes melden:

- **Unrichtigkeiten**: Schritte, die nicht den aktuellen Systemen entsprechen oder unerwartete Ergebnisse erzeugen.
- **Unklarheiten**: Unklare Anweisungen oder fehlende Voraussetzungen.
- **Verbesserungen**: Vorschläge für Effizienz oder Klarheit.

**Feedback-Mechanismus**: [Angabe: E-Mail an Verfahrens-Eigentümer, Ticket in [System], Kommentarfunktion im Dokumentenrepository, vierteljährliche Verfahrensnutzer-Umfrage].

**Feedback-Behandlung**:

- Alle Rückmeldungen werden protokolliert und vom Verfahrens-Eigentümer innerhalb von **14 Tagen** überprüft.
- Feedback wird in die nächste geplante Überprüfung einbezogen oder sofort umgesetzt, wenn kritisch.
- Einsender wird über die Disposition benachrichtigt (angenommen / verschoben / abgelehnt mit Begründung).

### Verfahrenstests

Kritische Verfahren sollen in definierten Abständen getestet werden:

| Verfahrenstyp | Testanforderung |
|---------------|-----------------|
| **Disaster Recovery** | Jährlicher Volltest; vierteljährliche Tabletop-Übung |
| **Incident Response** | Halbjährliche Übung |
| **Backup und Wiederherstellung** | Monatlicher Wiederherstellungstest |
| **Notfallzugang** | Jährlicher Break-Glass-Test |
| **Kritischer Betrieb** | Nach wesentlichen Änderungen |

Tests sollen dokumentiert werden, einschliesslich: Testdatum und Teilnehmende, Testszenario, Ergebnisse (Erfolg/Teilweise/Fehlschlag), identifizierte Probleme und Behebungsmassnahmen.

**Testresultat-Klassifizierung**:

- **Erfolg**: Verfahren wie geschrieben mit erwarteten Ergebnissen abgeschlossen; keine Behebung erforderlich.
- **Teilerfolg**: Verfahren mit geringfügigen Abweichungen oder Workarounds abgeschlossen; Aktualisierungen nötig, aber Verfahren ist nutzbar.
- **Fehlschlag**: Verfahren konnte nicht wie geschrieben abgeschlossen werden oder führte zu falschem Ergebnis; sofortige Revision vor der nächsten Nutzung erforderlich.

**Massnahmen bei Testfehlschlag**:

- Verfahren im Repository als "In Überprüfung" markiert (sichtbares Kennzeichen für Benutzer).
- Innerhalb von **14 Tagen** für kritische Verfahren, **30 Tage** für nicht kritische Verfahren überarbeitet.
- Nach Revision vor Wiederherstellung des "Genehmigt"-Status erneut getestet.

---

## Verfahrensdokumentations-Metriken

Die Organisation soll folgende Verfahrensdokumentations-Metriken verfolgen:

| Metrik | Ziel | Überprüfungshäufigkeit |
|--------|------|----------------------|
| **Vollständigkeit des Verfahrens-Inventars** (alle obligatorischen Kategorien dokumentiert) | 100 % | Vierteljährlich |
| **Überprüfungsaktualität** (Verfahren innerhalb des geplanten Zeitraums überprüft) | 100 % | Vierteljährlich |
| **Einhaltung des Dokumentationsstandards** (Stichprobenverfahren erfüllen obligatorische Elemente) | 100 % | Jährlich (via interner Audit-Stichprobe) |
| **Testabschlussrate** (kritische Verfahren gemäss Zeitplan getestet) | 100 % | Vierteljährlich |
| **Schulungsabschluss** (Bediener kritischer Verfahren geschult) | 100 % | Vierteljährlich |
| **Verfahrens-Test-Erfolgsrate** | ≥ 95 % | Jährlich |

Metriken, die Ziele verletzen, sollen an den ISB eskaliert und beim nächsten Management-Review gemeldet werden.

---

## Aufzeichnungsmanagement

### Beispiele für Aufzeichnungen

Aufzeichnungen sind Nachweise eines Ereignisses und werden für die operative Verwaltung und Auditierung verwendet. Sie umfassen, ohne darauf beschränkt zu sein:

- Sitzungsprotokolle.
- Schulungsaufzeichnungen.
- Audit-Berichte.
- Incident-Berichte.
- Änderungsaufzeichnungen.
- Risikobeurteilungsaufzeichnungen.

### Veraltete Dokumente und Aufzeichnungen

**Archivierung (erforderlich für Audit-/Rechts-/Regulierungszwecke)**:

- Veraltete Dokumente und Aufzeichnungen sollen gemäss den Aufbewahrungsanforderungen archiviert werden:
  - **Betriebsaufzeichnungen** (Änderungsprotokolle, Incident-Berichte): **3 Jahre** nach Veralterung.
  - **Audit-Nachweise** (Verfahrens-Versionshistorie): **7 Jahre** nach Veralterung.
  - **Rechtlich/Regulatorisch** (Compliance-Nachweise): Gemäss Legal Counsel oder regulatorischer Anforderung (typischerweise **7–10 Jahre**).
- Archivierte Dokumente aus dem allgemeinen Zugriff entfernt; nur für autorisiertes Audit-/Compliance-Personal zugänglich.

**Sichere Löschung (nicht für Aufbewahrung erforderlich)**:

- Veraltete Dokumente und Aufzeichnungen, die nicht für Audit- und/oder rechtliche und regulatorische Zwecke erforderlich sind, sollen gemäss der Richtlinie zur Informationsklassifizierung und -behandlung innerhalb von **90 Tagen** nach Feststellung der Veralterung sicher gelöscht werden.

### Dokumente externer Herkunft

Dokumentierte Informationen externer Herkunft, die die Organisation für die Planung und den Betrieb des Informationssicherheitsmanagementsystems als notwendig erachtet, sollen identifiziert und gesteuert werden (z. B. ISO-Standards, Lieferantendokumentation, regulatorische Leitlinien).

**Kontrollanforderungen für externe Dokumente**:

- **Identifizierung**: Externe Dokumente im Repository-Metadata als "Extern" gekennzeichnet.
- **Versionskontrolle**: Version und Veröffentlichungsdatum des externen Dokuments aufgezeichnet.
- **Überprüfung**: Jährlich auf Aktualität überprüft; aktualisierte Versionen bei Verfügbarkeit eingeholt.
- **Zugänglichkeit**: Im selben Repository wie interne Verfahren gespeichert, zur einfachen Referenz.
- **Keine Bearbeitung**: Externe Dokumente dürfen nicht modifiziert werden; Anmerkungen oder Zusammenfassungen als separate interne Dokumente erstellt.

**Beispiele**: ISO/IEC 27001:2022-Standard, Lieferantenprodukthandbücher, regulatorische Leitlinien vom EDÖB, NIST-Frameworks.

### Dokumentenklassifizierung

Dokumente sollen gemäss der Richtlinie zur Informationsklassifizierung und -behandlung klassifiziert werden.

**Typische Verfahrensklassifizierungen**:

- **Öffentlich**: Keine (Verfahren sind operative Details, nicht zur öffentlichen Bekanntgabe).
- **INTERN**: Standard-Betriebsverfahren, nicht sensible administrative Verfahren.
- **Vertraulich**: Sicherheitsverfahren (Incident Response, Schwachstellenmanagement), DR-Verfahren, Break-Glass-Verfahren, Verfahren mit Zugangsdaten oder Details zur Sicherheitsarchitektur.

Klassifizierte Verfahren sollen entsprechend ihrer Klassifizierungsstufe behandelt, gespeichert und übertragen werden. Vertrauliche Verfahren sollen eingeschränkten Zugang haben (rollenbasiert, Need-to-Know).

---

## Schulung und Kompetenz

### Bedienerschulung

Mitarbeitende sollen in relevanten Verfahren geschult werden, bevor sie diese selbstständig ausführen.

- Schulungsaufzeichnungen sollen geführt werden.
- Kompetenz soll durch Beobachtung, Bewertung oder Vorgesetzenfreigabe verifiziert werden.
- Auffrischungsschulung soll bereitgestellt werden, wenn Verfahren wesentlich aktualisiert werden.
- Cross-Training soll für kritische Verfahren implementiert werden, um Single Points of Failure zu vermeiden.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|--------------------|
| **ISB** | Richtlinieneigentümer; Sicherheitsverfahrensstandards; Genehmigung von Sicherheitsverfahren |
| **IT Operations Manager** | Eigentümerschaft von Infrastrukturverfahren; Verwahrer des Offline-Pakets; Koordination der Verfahrenstests |
| **Verfahrens-Eigentümer** | Richtigkeit, Aktualität und Qualität der eigenen Verfahren; Durchführung von Überprüfungen; Genehmigung von Aktualisierungen |
| **Stellvertretende Verfahrens-Eigentümer** | Kompetent zur Überprüfung und Genehmigung von Aktualisierungen in Abwesenheit des primären Eigentümers; im Verfahrensinhalt cross-geschult; über alle Verfahrensaktualisierungen benachrichtigt (für kritische Verfahren erforderlich) |
| **Qualitäts-/Records Manager** | Verfahrensvorlagenstandards; Überprüfungs-Tracking; Repository-Governance |
| **Alle technischen Mitarbeitenden** | Verfahren befolgen; Probleme und Unrichtigkeiten melden; Verbesserungen vorschlagen |

---

## Nachweise

Die folgenden Nachweise belegen die Einhaltung dieser Richtlinie:

| # | Nachweis | Eigentümer | Häufigkeit |
|---|---------|-----------|------------|
| 1 | **Verfahrens-Inventar** mit Metadaten (Eigentümer, Version, zuletzt überprüft, nächste Überprüfung) | Qualitäts-/Records Manager | *Kontinuierlich gepflegt; vollständiges Audit jährlich; Ziel: 100 % mit aktuellem Eigentümer* |
| 2 | **Stichprobenverfahren** mit Dokumentationsstandards (obligatorische Elemente vorhanden) | Qualitäts-/Records Manager | *Stichprobe von 5–10 Verfahren jährlich während internem Audit überprüft* |
| 3 | **Überprüfungs-Abschlussaufzeichnungen** (Verfahren innerhalb des geplanten Zeitraums überprüft) | Qualitäts-/Records Manager | *Vierteljährlich nachverfolgt; Ziel: 100 % innerhalb des Überprüfungszeitraums* |
| 4 | **Verfahrens-Testergebnisse** (DR, Incident Response, Backup-Wiederherstellung, Break-Glass) | IT Operations Manager | *Gemäss Testzeitplan; 3 Jahre aufbewahrt* |
| 5 | **Schulungsaufzeichnungen** für Verfahrensbediener (Abschluss, Kompetenzverifizierung) | HR / IT Operations | *Pro Ereignis; Ziel: 100 % der kritischen Verfahrensbediener geschult* |
| 6 | **Versionskontrollnachweise** aus dem Repository (Änderungs-Audit-Trail) | Qualitäts-/Records Manager | *Kontinuierlich; während jährlichem Audit verifiziert* |
| 7 | **Notfall-Offline-Paket** Aktualitätsverifizierungsaufzeichnungen | IT Operations Manager | *Vierteljährlich; Checkliste unterzeichnet und aufbewahrt* |
| 8 | **Veraltete Dokument**-Archivierungs- und Löschaufzeichnungen | Qualitäts-/Records Manager | *Pro Ereignis; gemäss Aufbewahrungsplan aufbewahrt* |

---

# Richtlinien-Compliance

## Compliance-Messung

Das Informationssicherheitsmanagement-Team wird die Einhaltung dieser Richtlinie durch verschiedene Methoden verifizieren, einschliesslich, aber nicht beschränkt auf Verfahrens-Inventar-Audits, Stichproben-Qualitätsüberprüfungen, Überprüfungs-Abschluss-Tracking, Verfahrens-Testergebnis-Analysen, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme zu dieser Richtlinie muss vom Information Security Manager vorab genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, ausgleichenden Controls und einem definierten Überprüfungsdatum (maximal 90 Tage, verlängerbar). Ausnahmen müssen dem Management-Review-Team gemeldet werden. Kritische Verfahren und Sicherheitsverfahren dürfen nicht ohne Dokumentation betrieben werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Änderungen der betrieblichen Standards, Technologieänderungen, Audit-Ergebnisse, regulatorische Änderungen sowie Erkenntnisse aus Incidents und Verfahrens-Testfehlschlägen berücksichtigen.

---

# Adressierte Bereiche des ISO 27001-Standards

Richtlinie Dokumentierte Betriebsverfahren — ISO 27001-Controls-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Engagement | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Politik | 5.4 Managementverantwortlichkeiten |
| Klausel 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| Klausel 7.3 Bewusstsein | **5.37 Dokumentierte Betriebsverfahren** |
| Klausel 7.5.1 Dokumentierte Informationen — Allgemein | 5.13 Kennzeichnung von Informationen |
| Klausel 7.5.2 Erstellung und Aktualisierung von Dokumenten | 6.3 Informationssicherheitsbewusstsein, -ausbildung und -schulung |
| Klausel 7.5.3 Steuerung dokumentierter Informationen | 6.4 Disziplinarverfahren |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizer nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen (dokumentierte Verfahren als organisatorische Massnahme) |
| Schweizer DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit (dokumentierte Prozesse) |
| EU DSGVO (sofern anwendbar) | Art. 5 Abs. 2 — Rechenschaftspflicht (dokumentierte Verfahren belegen Compliance); Art. 32 — Sicherheit der Verarbeitung |
| ISO/IEC 27001:2022 | Annex A Control 5.37; Klauseln 7.5.1, 7.5.2, 7.5.3 — Dokumentierte Informationen |
| ISO/IEC 27002:2022 | Abschnitt 5.37 — Umsetzungsanleitung |
| NIST SP 800-53 Rev 5 | PL-2 (Sicherheits- und Datenschutzpläne), SA-5 (Systemdokumentation), PS-1 (Richtlinie und Verfahren) |
| CIS Controls v8 | Control 16 (Anwendungssoftware-Sicherheit — Absicherung 16.1: Einen sicheren Anwendungsentwicklungsprozess aufbauen und aufrechterhalten — erfordert dokumentierte Verfahren) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
