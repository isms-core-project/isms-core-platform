<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.6-DE:operational:OP-POL:a.8.6 -->
**ISMS-OP-POL-A.8.6 — Kapazitätsmanagement**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Kapazitätsmanagement |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.6 |
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

**Überprüfungszyklus**: Jährlich (abgestimmt auf Kapazitätsplanungszyklus)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt von**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Control A.8.6 — Capacity management
- ISO/IEC 27002:2022 Section 8.6 — Implementation guidance for capacity management
- NIST SP 800-53 Rev 5 — AU-4 (Audit Log Storage Capacity), CP-2(2) (Capacity Planning), SC-5 (Denial-of-Service Protection)
- ITIL 4 — Capacity and Performance Management Practice

**Verwandte Annex-A-Controls**:

| Control | Bezug zum Kapazitätsmanagement |
|---------|-------------------------------|
| A.5.30–8.13–14 Business Continuity und DR | Kapazitätsplanung für Wiederherstellungsstandort; Backup-Speicherkapazität |
| A.7.11 Unterstützende Versorgungseinrichtungen | Kapazität der physischen Infrastruktur (Strom, Kühlung, Rack-Platz) |
| A.8.1–7–18–19 Endpunktsicherheit | Endpunkt-Ressourcenüberwachung und Fleet-Kapazität |
| A.8.8 Schwachstellenmanagement | Kapazität für Scanning-Tools; Ressourcenanforderungen für Patch-Deployment |
| A.8.9 Konfigurationsmanagement | Basiskonfigurationen enthalten Kapazitätsschwellenwerte |
| A.8.15 Protokollierung | Planung der Protokollspeicherkapazität und Aufbewahrungsmanagement |
| A.8.16 Überwachungsaktivitäten | Kapazitätskennzahlen als Teil des Gesamtmonitorings |
| A.8.20–22 Netzwerksicherheit | Netzwerkbandbreite und Durchsatzkapazität |

**Verwandte interne Richtlinien**:

- Richtlinie für Überwachungsaktivitäten (A.8.16)
- Richtlinie für Business Continuity und Disaster Recovery (A.5.30–8.13–14)
- Protokollierungsrichtlinie (A.8.15)
- Netzwerksicherheitsrichtlinie (A.8.20–22)
- Änderungsmanagementrichtlinie (A.8.32)

---

# Kapazitätsmanagement-Richtlinie

## Zweck

Zweck dieser Richtlinie ist es sicherzustellen, dass die Nutzung von Informationsverarbeitungsressourcen überwacht und in Übereinstimmung mit aktuellen und erwarteten Kapazitätsanforderungen angepasst wird, um Dienstunterbrechungen durch Ressourcenerschöpfung zu verhindern und fundierte Investitionsentscheidungen zu unterstützen.

Kapazitätsmanagement ist sowohl eine betriebliche Notwendigkeit als auch eine Sicherheitskontrolle. Unzureichende Kapazität kann Dienstausfälle verursachen, das Sicherheitsmonitoring beeinträchtigen, die Erfassung von Audit-Protokollen verhindern und Bedingungen schaffen, die durch Denial-of-Service-Angriffe ausgenutzt werden können. Proaktive Kapazitätsplanung stellt sicher, dass Infrastruktur, Anwendungen und unterstützende Dienste verfügbar, leistungsfähig und sicher bleiben.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 8, indem technische und organisatorische Massnahmen dem Risiko entsprechend implementiert werden, um die Verfügbarkeit und Integrität von Systemen zu schützen, die personenbezogene Daten verarbeiten. Soweit die Organisation Daten von Personen in der EU/im EWR verarbeitet, gelten auch die DSGVO-Art.-32-Anforderungen zur Gewährleistung der fortlaufenden Verfügbarkeit und Resilienz von Verarbeitungssystemen.

## Geltungsbereich

Diese Richtlinie gilt für alle Infrastruktur-, Anwendungs- und Serviceressourcen im ISMS-Geltungsbereich, die Kapazitätsüberwachung und -planung erfordern. Dies umfasst:

- **Rechenressourcen**: Server, virtuelle Maschinen, Container, Cloud-Instanzen (CPU- und Speicherauslastung).
- **Speicherressourcen**: Festplattenspeicher, Datenbankspeicher, Backup-Speicher, Archivspeicher, Protokollspeicher.
- **Netzwerkressourcen**: Bandbreite, Durchsatz, Verbindungen, Load-Balancer-Kapazität, DNS-Abfragekapazität.
- **Anwendungsressourcen**: Gleichzeitige Nutzer, Transaktionsraten, API-Rate-Limits, Nachrichtenwarteschlangentiefe.
- **Cloud-Service-Ressourcen**: Service-Kontingente, Instanzlimits, API-Aufruf-Limits, reservierte Kapazität.
- **Lizenzkapazität**: Softwarelizenzen, Abonnement-Seats, gleichzeitige Lizenznutzung.
- **Physische Infrastruktur**: Stromkapazität, Kühlkapazität, Rack-Platz (gemäss A.7.11).

Alle Mitarbeitenden, Auftragnehmer und Drittanbieter mit Verantwortung für Infrastruktur-, Anwendungs- oder Servicemanagement.

**Nicht im Geltungsbereich**: Leistungsoptimierung von Anwendungen und Code-Optimierung (abgedeckt durch sichere Entwicklung); detailliertes Software-Asset-Management und Lizenzbeschaffung (abgedeckt durch Asset-Management A.5.9); physische Gebäudekapazität ohne Bezug zur Informationsverarbeitung.

## Grundsatz

Die Organisation soll Kapazitätsanforderungen für alle kritischen Ressourcen proaktiv überwachen, prognostizieren und planen. Das Kapazitätsmanagement folgt dem Prinzip der Prävention gegenüber Reaktion — es ist wesentlich kostengünstiger und weniger disruptiv, Kapazitätswachstum zu planen, als auf Kapazitätserschöpfungsvorfälle zu reagieren.

Kapazitätsentscheidungen sollen datengesteuert sein, basierend auf gemessenen Auslastungstrends und dokumentierten Geschäftswachstumsprognosen, nicht auf Annahmen oder Einzelfallberichten. Ressourcen sollen ausreichenden Puffer aufrechterhalten, um unerwartete Nachfragespitzen ohne Leistungsverschlechterung aufzufangen.

---

## Ressourcenüberwachung

### Überwachungsabdeckung

Alle Produktionssysteme und -dienste sollen Kapazitätsüberwachung aktiviert haben. Die Überwachung soll mindestens die im Geltungsbereich aufgeführten Ressourcenkategorien abdecken.

**Abdeckungsanforderungen**:

| Umgebung | Abdeckungsziel | Überwachungsfrequenz |
|----------|----------------|---------------------|
| Produktionssysteme | 100% | Alle 5 Minuten oder weniger |
| Disaster-Recovery / Standby | 100% | Alle 15 Minuten oder weniger |
| Nicht-Produktion (Staging, Test) | 90% | Alle 15 Minuten oder weniger |

Die Überwachung soll mit [Monitoring Platform] implementiert werden (z. B. Prometheus, Zabbix, Datadog, Azure Monitor, CloudWatch oder gleichwertig). Die Plattform soll im Asset-Inventar mit Hosting-Modell, Datenspeicherort und administrativen Zugangskontrolle dokumentiert werden.

### Überwachte Kennzahlen

Folgende Kennzahlen sollen für jeden anwendbaren Ressourcentyp erfasst werden:

| Ressourcentyp | Kennzahlen | Einheiten |
|---------------|------------|-----------|
| **CPU** | Auslastung (Durchschnitt, Spitze), Load Average, Ready-Time | Prozent, Anzahl |
| **Arbeitsspeicher** | Auslastung, Swap-Nutzung, verfügbarer Speicher | Prozent, GB |
| **Speicher** | Genutzte Kapazität, verfügbare Kapazität, Wachstumsrate, IOPS | GB/TB, Prozent, Ops/Sek |
| **Netzwerk** | Bandbreitenauslastung, Paketverlust, Latenz, Verbindungsanzahl | Mbps/Gbps, Prozent, ms, Anzahl |
| **Anwendung** | Gleichzeitige Nutzer, aktive Sitzungen, Transaktionsrate, Warteschlangentiefe | Anzahl, Transaktionen/Sek |
| **Cloud-Kontingente** | Service-Limit-Auslastung pro Region und Konto | Prozent des Kontingents |
| **Lizenzen** | Aktive Zuweisungen im Vergleich zu Gesamtberechtigungen | Anzahl, Prozent |

### Kennzahlenaufbewahrung

- **Rohdaten**: Mindestens 30 Tage in voller Auflösung (für Vorfalluntersuchungen).
- **Aggregierte Kennzahlen**: Mindestens 12 Monate in stündlicher oder täglicher Granularität (für Trendanalysen).
- **Historische Zusammenfassungen**: Mindestens 36 Monate in monatlicher Granularität (für strategische Planung).

Kennzahlendaten sollen vor nicht autorisierter Änderung oder Löschung geschützt werden. Wo Kennzahlen das Sicherheitsmonitoring (A.8.16) speisen, gelten auch die Protokollintegritätsanforderungen aus der Protokollierungsrichtlinie (A.8.15).

---

## Schwellenwert-Framework und Alarmierung

### Schwellenwertstufen

Alle überwachten Ressourcen sollen definierte Kapazitätsschwellenwerte auf drei Stufen haben:

| Stufe | Zweck | Typischer Bereich | Massnahme |
|-------|-------|-------------------|-----------|
| **Warnung** | Frühzeitige Anzeige von Kapazitätsdruck | 70–80% Auslastung | Kapazitätsplanung überprüfen; Wachstumstrend untersuchen |
| **Kritisch** | Kapazität nähert sich Erschöpfung | 85–90% Auslastung | Sofortige Untersuchung; Kapazitätserweiterung oder Lastminderung einleiten |
| **Maximum** | Ressourcenerschöpfung unmittelbar bevorstehend oder eintretend | 95%+ Auslastung | Notfallreaktion; Incident-Management auslösen bei Dienstauswirkung |

Genaue Schwellenwerte sollen pro Ressourcentyp und Systemklassifizierung definiert, in der Monitoring-Plattform dokumentiert und vierteljährlich überprüft werden. Schwellenwerte sollen basierend auf Fehlalarmraten, Arbeitslastmustern und Beinahe-Vorfällen angepasst werden.

**Speicherspezifische Schwellenwerte** sollen auch die Wachstumsrate berücksichtigen: Wenn der Speicher voraussichtlich innerhalb von 30 Tagen bei aktueller Verbrauchsrate 95% erreicht, soll unabhängig vom aktuellen Prozentsatz eine Warnung generiert werden.

### Alarmkonfiguration

Kapazitätsschwellenwert-Alarme sollen konfiguriert werden mit:

- **Routing**: Alarme an das verantwortliche Operations-Team über [Alerting Tool] übermittelt (z. B. PagerDuty, Opsgenie, ServiceNow oder gleichwertig).
- **Lieferzeit**: Alarme innerhalb von 5 Minuten nach Erkennung der Schwellenwertüberschreitung übermittelt.
- **Eskalation**: Unbestätigte Warnungsalarme nach 4 Stunden eskaliert; unbestätigte kritische Alarme nach 30 Minuten eskaliert.
- **Deduplizierung**: Wiederholte Alarme für dieselbe Ressource und denselben Schwellenwert werden unterdrückt, um Alarmmüdigkeit zu vermeiden; erneute Alarmierung wenn die Bedingung über das Unterdrückungsfenster hinaus anhält.
- **Integration**: Kritische und Maximum-Alarme sollen automatisch Vorfälle in [ITSM Tool] erstellen (z. B. ServiceNow, Jira Service Management oder gleichwertig).

### Alarmreaktion

| Alarmstufe | Reaktions-SLA | Reaktionsmassnahme |
|------------|---------------|--------------------|
| **Warnung** | Bestätigt innerhalb von 4 Stunden (Geschäftszeiten) | Trenddaten überprüfen; Kapazitätsprognose aktualisieren; Erweiterung planen sofern erforderlich |
| **Kritisch** | Bestätigt innerhalb von 30 Minuten | Ursache untersuchen; sofortige Minderung implementieren (Lastreduzierung, temporäre Skalierung); Kapazitätserweiterung einleiten |
| **Maximum** | Bestätigt innerhalb von 15 Minuten | Notfallreaktion ausführen; Incident-Management gemäss A.5.24–28 bei Dienstauswirkung auslösen; Notfall-Kapazitätserweiterung implementieren |

---

## Kapazitätsprognose

### Prognosehorizonte

Die Organisation soll Kapazitätsprognosen auf drei Horizonte entwickeln und pflegen:

| Horizont | Zeitraum | Zweck | Aktualisierungsfrequenz |
|----------|----------|-------|------------------------|
| **Kurzfristig** | 3–6 Monate | Taktische Planung; sofortige Beschaffung | Monatlich |
| **Mittelfristig** | 6–12 Monate | Budgetplanung; Vertragsverlängerungen | Vierteljährlich |
| **Langfristig** | 12–24 Monate | Strategische Planung; Rechenzentrum- oder Cloud-Migrationsentscheidungen | Jährlich |

### Prognosemethodik

Prognosen sollen basieren auf:

- **Historische Trendanalyse**: Extrapolation aus gemessenen Auslastungsdaten (mindestens 6 Monate Daten für zuverlässige Trends erforderlich).
- **Geschäftswachstumsprognosen**: Input von Anwendungsverantwortlichen und Geschäftsbereichen zu geplanten Projekten, Nutzerwachstum, Datenvolumenzunahmen und neuen Servicestarts.
- **Saisonale Muster**: Identifikation und Modellierung periodischer Nachfrageschwankungen (Monatsendverarbeitung, jährliche Berichtszyklen, Marketingkampagnen).
- **Geplante Änderungen**: Geplante Deployments, Migrationen, Stilllegungen und Infrastrukturänderungen.

Wo historische Daten unzureichend sind (neue Systeme oder Dienste), sollen konservative Schätzungen mit häufigerer Überprüfung in den ersten 6 Betriebsmonaten verwendet werden.

### Prognosegenauigkeit

- **Zielgenauigkeit**: Prognosen sollen innerhalb von +/-15% der tatsächlichen Auslastung liegen (vierteljährlich gemessen).
- **Neue Systeme (erste 6 Monate)**: +/-30% Genauigkeit akzeptabel, während Baselines etabliert werden.
- **Hoch variable Arbeitslasten**: +/-25% Genauigkeit mit dokumentierter Begründung.
- **Abweichungen über 15%**: Ursachenanalyse erforderlich innerhalb von 10 Arbeitstagen; Ergebnisse dokumentiert und in den nächsten Prognosezyklus eingebunden.

---

## Auto-Scaling-Richtlinien

Wo die Organisation Cloud-Infrastruktur betreibt, soll Auto-Scaling für Arbeitslasten mit variablen Nachfragemustern konfiguriert werden.

### Auto-Scaling-Anforderungen

| Anforderung | Standard |
|-------------|----------|
| **Skalierungsauslöser** | CPU-Auslastung, Arbeitsspeicherauslastung, Anfragerate, Warteschlangentiefe oder benutzerdefinierte Anwendungskennzahlen |
| **Scale-Out-Schwellenwert** | Pro Arbeitslast definiert; typischerweise 70–80% der Zielkennzahl für 3–5 Minuten anhaltend |
| **Scale-In-Schwellenwert** | Pro Arbeitslast definiert; typischerweise 30–40% der Zielkennzahl für 10–15 Minuten anhaltend |
| **Mindestinstanzen** | Mindestens 2 für Produktionsarbeitslasten (Verfügbarkeit); mindestens 1 für Nicht-Produktion |
| **Höchstinstanzen** | Pro Arbeitslast definiert, um Kostenüberschreitungen zu verhindern; mit Budgetbeschränkungen abgestimmt |
| **Abkühlungszeit** | Mindestens 5 Minuten zwischen Skalierungsaktionen, um Schwingungen zu verhindern |

### Auto-Scaling-Governance

- Auto-Scaling-Konfigurationen sollen dokumentiert und versionskontrolliert werden.
- Änderungen an Auto-Scaling-Richtlinien für Produktionsarbeitslasten sollen dem Änderungsmanagementprozess folgen (A.8.32).
- Maximalinstanz-Limits sollen vierteljährlich überprüft und mit genehmigten Budgets abgestimmt werden.
- Auto-Scaling-Ereignisse sollen protokolliert und monatlich auf Optimierungsmöglichkeiten überprüft werden.
- **Kostenlimits**: Maximale monatliche Ausgabenlimits sollen auf Ebene des Cloud-Kontos oder der Subscription konfiguriert werden. Auto-Scaling, das das Ausgabenlimit überschreiten würde, soll einen Alarm an den Infrastrukturmanager und FL-Stellvertreter auslösen.

Wo Auto-Scaling nicht verfügbar oder nicht angemessen ist (On-Premises-Infrastruktur, Dienste mit fester Kapazität), sollen manuelle Kapazitätserweiterungsverfahren mit definierten Beschaffungs- und Deployment-Vorlaufzeiten dokumentiert werden.

---

## Kapazitäts- und Kostenoptimierung

Das Kapazitätsmanagement soll Verfügbarkeit, Leistung und Kosten ausbalancieren. Überversorgung verschwendet Budget; Unterversorgung schafft Risiken. Die Organisation soll die Ressourcenzuweisung aktiv auf Basis gemessener Auslastungsdaten optimieren.

### Optimierungsstrategien

| Strategie | Beschreibung | Anwendbarkeit |
|-----------|-------------|---------------|
| **Right-Sizing** | Überversorgte Ressourcen eliminieren, wo die anhaltende Auslastung unter 40% liegt | Alle Umgebungen |
| **Reservierte Kapazität** | Reservierte Instanzen oder Nutzungsrabatte für Steady-State-Arbeitslasten erwerben (z. B. AWS RIs, Azure RIs, GCP CUDs) | Cloud-Umgebungen mit vorhersehbarer Baseline |
| **Spot-/präemptive Instanzen** | Für nicht kritische, unterbrechbare Arbeitslasten verwenden (Stapelverarbeitung, Tests, Entwicklung) | Cloud-Umgebungen mit fehlertoleranten Arbeitslasten |
| **Auto-Scaling** | Kapazität in Echtzeit an Nachfrage anpassen, um Zahlung für Leerlaufressourcen zu vermeiden | Cloud-Umgebungen mit variabler Nachfrage |
| **Speicher-Lifecycle** | Selten zugegriffene Daten in kostengünstigere Speicherklassen auslagern (z. B. S3 Glacier, Azure Cool/Archive, GCS Nearline/Coldline) | Alle Speicher mit definierten Zugriffsmustern |

### Vierteljährliche Kostenüberprüfung

Der Infrastrukturmanager soll eine vierteljährliche Kostenüberprüfung durchführen, die umfasst:

- Identifikation überversorgter Ressourcen (anhaltende Auslastung konstant unter 40%).
- Bewertung des Verhältnisses von reservierter Kapazität zu On-Demand-Ausgaben.
- Beurteilung von Speicher-Tiering-Möglichkeiten.
- Berichterstattung über ergriffene Kostenoptimierungsmassnahmen und erzielte Einsparungen.

Erkenntnisse aus der Kostenoptimierung sollen in den vierteljährlichen Kapazitätsüberprüfungsbericht aufgenommen werden, der dem ITL, ISB und FL-Stellvertreter vorgelegt wird.

---

## Kapazität und Service-Level-Ziele

Kapazitätsschwellenwerte sollen an Service-Level-Ziele (SLOs) angepasst werden, um sicherzustellen, dass Kapazitätsbeschränkungen die Servicequalität nicht unter vereinbarte Niveaus senken. Der Zusammenhang zwischen Ressourcenauslastung und Serviceleistung soll für jeden kritischen Dienst dokumentiert werden.

### SLO-Abstimmung

| Diensttyp | Typisches SLO | Kapazitätsschwellenwert-Abstimmung |
|-----------|---------------|-----------------------------------|
| Webanwendung | 99,9% Verfügbarkeit, <500ms p95 Latenz | CPU soll unter 75% Durchschnitt bleiben (Latenz verschlechtert sich über 75%) |
| API-Dienst | 99,95% Verfügbarkeit, <200ms p95 Latenz | CPU unter 70% Durchschnitt; Arbeitsspeicher unter 80% |
| Datenbank | 99,99% Verfügbarkeit, <50ms Abfrageantwort | IOPS unter 80% Maximum; Verbindungen unter 90% Maximum |
| Nachrichtenwarteschlange | 99,9% Verfügbarkeit, <5s Verarbeitungsverzögerung | Warteschlangentiefe unter 80% Maximum; Verbraucherkapazität aufrechterhalten |

Wo die gemessene Ressourcenauslastung Niveaus nähert, die die SLO-Leistung verschlechtern würden, sollen Kapazitätsschwellenwerte nach unten angepasst werden, um eine frühere Intervention auszulösen. Die SLO-Abstimmung soll vierteljährlich als Teil des Kapazitätsüberprüfungsprozesses überprüft werden.

---

## Kapazitätsberichterstattung

### Berichtsrhythmus

| Bericht | Zielgruppe | Häufigkeit | Inhalt |
|---------|-----------|------------|--------|
| **Betriebsdashboard** | IT-Betrieb | Kontinuierlich (Echtzeit) | Aktuelle Auslastung, aktive Alarme, Trendindikatoren |
| **Monatlicher Kapazitätsbericht** | IT-Führung, Infrastrukturmanager | Monatlich | Auslastungszusammenfassung, Alarmhistorie, Prognosehighlights, ergriffene Kapazitätsmassnahmen |
| **Vierteljährliche Kapazitätsüberprüfung** | ITL, ISB, FL-Stellvertreter | Vierteljährlich | Prognosen, Erweiterungspläne, Budgetauswirkungen, Gesundheits-Scorecard, Compliance-Kennzahlen |
| **Jährlicher Kapazitätsplan** | Geschäftsleitung | Jährlich | Strategischer Plan mit mehrjährigen Projektionen, Investitionsanforderungen, Risikobewertung |

### Berichtsinhaltsanforderungen

Monatliche und vierteljährliche Berichte sollen enthalten:

- Aktuelle Auslastung nach Ressourcentyp (Durchschnitt, Spitze, Trendrichtung).
- Anzahl der Schwellenwertüberschreitungen und Reaktionszeiten.
- Kapazitätsbezogene Vorfälle (Anzahl, Schweregrad, Ursachenzusammenfassung).
- Messung der Prognosegenauigkeit (tatsächlich vs. vorhergesagt).
- Geplante Kapazitätsänderungen (Erweiterungen, Stilllegungen, Migrationen).
- Budgetauslastung für Kapazitätsausgaben.

Berichte sollen aus Daten der [Monitoring Platform] generiert werden. Der jährliche Kapazitätsplan soll vom ITL genehmigt und in die Managementüberprüfung gemäss ISO-27001-Clause 9.3 aufgenommen werden.

---

## Speicherkapazitätsmanagement

Das Speicherkapazitätsmanagement erfordert besondere Aufmerksamkeit aufgrund seiner kontinuierlichen Wachstumscharakteristika und der direkten Sicherheitsauswirkung von Speichererschöpfung (Verlust von Audit-Protokollen, Unfähigkeit, Sicherheitsereignisse zu schreiben, Anwendungsausfälle).

### Protokollspeicher

- Die Protokollspeicherkapazität soll in Koordination mit der Protokollierungsrichtlinie (A.8.15) geplant werden, um sicherzustellen, dass Aufbewahrungsanforderungen ohne Speichererschöpfung erfüllt werden können.
- Der Protokollspeicher soll einen dedizierten Warnschwellenwert bei 70% und kritischen Schwellenwert bei 85% haben.
- Wenn der Protokollspeicher den kritischen Schwellenwert erreicht, soll automatische Protokollrotation oder -archivierung ausgelöst werden, bevor Datenverlust eintritt.
- Die Protokollspeicher-Wachstumsrate soll monatlich verfolgt und projiziert werden.

### Datenbankspeicher

- Das Datenbankwachstum soll separat vom Dateispeicher überwacht und prognostiziert werden.
- Datenbankwartungsaktivitäten (Vacuuming, Index-Rebuilds, Archivierung) sollen in die Kapazitätsplanung einfliessen.
- Datenbankspeicher-Schwellenwerte sollen den betrieblichen Overhead berücksichtigen (temporäre Tabellen, Transaktionsprotokolle, Replikationsverzögerung).

### Backup-Speicher

- Die Backup-Speicherkapazität soll geplant werden, um vollständige Backup-Sets für den erforderlichen Aufbewahrungszeitraum gemäss der Backup-Richtlinie (A.5.30–8.13–14) aufzunehmen.
- Das Wachstum des Backup-Speichers soll basierend auf dem Produktionsdatenwachstum und Änderungen der Aufbewahrungsrichtlinie prognostiziert werden.

---

## Lizenzkapazitätsmanagement

Die Softwarelizenzkapazität soll überwacht werden, um Compliance-Verstösse und Dienstunterbrechungen durch Lizenzerschöpfung zu verhindern.

### Lizenzüberwachungsanforderungen

| Anforderung | Standard |
|-------------|----------|
| **Lizenzinventar** | Im Asset-Inventar (A.5.9) gepflegt mit Berechtigungsanzahl, Ablaufdaten und Lizenztyp (gleichzeitig, namentlich, gerätebezogen) |
| **Nutzungsüberwachung** | Aktive Nutzung im Vergleich zur Berechtigung für alle kritischen Software verfolgt |
| **Warnschwellenwert** | Alarm wenn Nutzung 80% der Berechtigung erreicht |
| **Kritischer Schwellenwert** | Alarm wenn Nutzung 90% der Berechtigung erreicht |
| **Überprüfungsfrequenz** | Vierteljährliche Nutzungsüberprüfung; jährliche Verlängerungsplanung |

### Lizenzverlängerungsplanung

Lizenzverlängerungen sollen mit einer Mindest-Vorlaufzeit von 90 Tagen vor Ablauf verfolgt werden. Lizenzkapazitätsanforderungen sollen in die mittelfristige (6–12 Monate) Kapazitätsprognose aufgenommen und mit Budgetplanungszyklen abgestimmt werden.

---

## Kapazitätsvorfallreaktion

Wenn Kapazitätserschöpfung Dienstauswirkungen verursacht oder zu verursachen droht, soll der Incident-Management-Prozess der Organisation (A.5.24–28) ausgelöst werden.

### Kapazitätsspezifische Vorfallverfahren

| Szenario | Klassifizierung | Sofortige Reaktion |
|----------|----------------|-------------------|
| **Warnschwellenwert anhaltend >24 Stunden** | Kapazitätsereignis (kein Vorfall) | Überprüfen und planen; keine Notfallmassnahmen erforderlich |
| **Kritischer Schwellenwert anhaltend >1 Stunde** | Priorität-3-Vorfall | Lastminderung implementieren; Notfall-Kapazitätserweiterung einleiten |
| **Dienstbeeinträchtigung durch Kapazität** | Priorität-2-Vorfall | Notfallskalierung oder Lastreduzierung; Kundenbenachrichtigung bei externer Auswirkung |
| **Dienstausfall durch Kapazitätserschöpfung** | Priorität-1-Vorfall | Vollständige Vorfallreaktion; Notfallbeschaffung; Post-Incident-Review obligatorisch |

### Post-Incident-Review

Alle kapazitätsbezogenen Vorfälle der Priorität 1 oder 2 sollen innerhalb von 5 Arbeitstagen einem Post-Incident-Review unterzogen werden. Der Review soll feststellen:

- Warum Monitoring und Prognose den Vorfall nicht verhindert haben.
- Ob Schwellenwerte angepasst werden müssen.
- Ob die Prognosemethodik verbessert werden muss.
- Welche Kapazitätserweiterung zur Verhinderung einer Wiederholung erforderlich ist.
- Ob der Vorfall eine Lücke in der Überwachungsabdeckung aufgedeckt hat.

Erkenntnisse sollen im Kapazitätsverbesserungsregister verfolgt werden, bis die Behebung abgeschlossen ist.

---

## Denial-of-Service-Resilienz

Die Kapazitätsplanung soll Resilienz gegen Denial-of-Service-Bedingungen (DoS/DDoS) einbeziehen. Kapazität sollte nicht ausschliesslich für durchschnittliche oder erwartete Spitzenlasten geplant werden — es soll ein Puffer aufrechterhalten werden, um unerwartete Nachfragespitzen aufzufangen, einschliesslich solcher, die durch böswillige Aktivitäten verursacht werden.

### Pufferanforderungen

| Ressource | Mindestpuffer bei Spitzenlast | Begründung |
|-----------|-------------------------------|------------|
| **CPU** | 20% | Verkehrsspitzen ohne Leistungsverschlechterung absorbieren |
| **Arbeitsspeicher** | 20% | Out-of-Memory-Ausfälle unter Last verhindern |
| **Speicher** | 3 Monate bei aktuellem Wachstum | Vorlaufzeit für Beschaffung und Bereitstellung |
| **Netzwerkbandbreite** | 30% während Geschäftszeiten | Verkehrsspitzen absorbieren; DDoS-Minderungs-Overhead aufnehmen |

Wo extern erreichbare Dienste DDoS-Risiken ausgesetzt sind, sollen zusätzliche Minderungsmassnahmen (CDN, DDoS-Schutzdienste, Rate-Limiting) in Koordination mit der Netzwerksicherheitsrichtlinie (A.8.20–22) implementiert werden.

---

## Kapazitätsplanungsausschuss

Organisationen mit komplexer oder grossskaliger Infrastruktur (50+ Server oder gleichwertige Cloud-Arbeitslasten) sollten einen Kapazitätsplanungsausschuss einrichten, um das Kapazitätsmanagement teamübergreifend zu koordinieren und die Abstimmung zwischen technischen Kapazitätsentscheidungen und Geschäftsstrategie sicherzustellen.

### Ausschussstruktur

| Rolle | Funktion |
|-------|----------|
| **Infrastrukturmanager** (Vorsitz) | Tagesordnung festlegen; Kapazitätsdaten und Prognosen präsentieren |
| **Cloud-Architekt / Platform-Engineer** | Cloud-Kapazitätstrends, Auto-Scaling-Effektivität, Kostenoptimierung |
| **Datenbankadministrator** | Datenbankwachstum, Performance-Kapazität, Replikationskapazität |
| **Anwendungsverantwortliche** (rotierend) | Geschäftswachstumsprognosen, geplante Launches, Nachfrageänderungen |
| **FL-Stellvertreter** | Budgetüberprüfung, Investitionsgenehmigung, Kosten-Nutzen-Analyse |

### Sitzungsrhythmus

Der Kapazitätsplanungsausschuss soll vierteljährlich tagen. Die Tagesordnung soll umfassen:

- Überprüfung von Kapazitätsprognosen und Prognosegenauigkeit.
- Genehmigung geplanter Kapazitätserweiterungen und zugehöriger Budgets.
- Überprüfung kapazitätsbezogener Vorfälle und Beinahe-Ereignisse.
- Budgetauswirkungsdiskussion und Kostenoptimierungsmöglichkeiten.
- Identifikation aufkommender Kapazitätsrisiken durch Geschäftswachstum oder Technologieänderungen.

Sitzungsprotokolle sollen als Governance-Nachweis aufbewahrt werden (Nachweis Nr. 10).

Wo die Organisation zu klein ist, um einen formellen Ausschuss zu rechtfertigen, soll das vierteljährliche Kapazitätsüberprüfungsmeeting zwischen Infrastrukturmanager und ITL diese Governance-Funktion erfüllen.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Auto-Scaling** | Automatische Anpassung von Rechenressourcen (Instanzen, Container) als Reaktion auf gemessene Nachfrage, typischerweise in Cloud-Umgebungen |
| **Kapazitätsprognose** | Projektion zukünftiger Ressourcenanforderungen basierend auf historischen Trends, Geschäftswachstumsplänen und saisonalen Mustern |
| **Kapazitätspuffer** | Verbleibende ungenutzte Kapazität, die für Wachstum oder unerwartete Nachfrage über der aktuellen Spitzenauslastung verfügbar ist |
| **Kapazitätsschwellenwert** | Ein definiertes Auslastungsniveau, das bei Überschreitung Alarme oder Massnahmen auslöst (Warnung, kritisch oder Maximum) |
| **Abkühlungszeit** | Mindestintervall zwischen Auto-Scaling-Aktionen, um schnelle Schwingungen zwischen Scale-in und Scale-out zu verhindern |
| **DDoS** | Distributed Denial-of-Service — ein Angriff, der versucht, einen Dienst durch Überflutung mit Datenverkehr aus mehreren Quellen zu überlasten |
| **Wachstumsrate** | Die Rate, mit der der Ressourcenverbrauch über die Zeit zunimmt, typischerweise gemessen als Prozentsatz pro Monat oder absolute Einheiten pro Monat |
| **IOPS** | Input/Output-Operationen pro Sekunde — eine Speicher-Leistungskennzahl, die die Rate von Lese- und Schreiboperationen misst |
| **Lastreduzierung** | Bewusste Reduzierung der Systemlast bei Kapazitätsdruck durch Priorisierung nicht wesentlicher Arbeitslasten oder Rate-Limiting von Anfragen |
| **Right-Sizing** | Anpassung der Ressourcenzuweisung an die tatsächliche Auslastung, Beseitigung über- oder unterversorgter Ressourcen |
| **Scale-in** | Reduzierung der Anzahl zugewiesener Ressourcen (Instanzen, Container) bei sinkender Nachfrage |
| **Scale-out** | Erhöhung der Anzahl zugewiesener Ressourcen (Instanzen, Container) bei steigender Nachfrage |
| **SLO** | Service-Level-Ziel — ein messbares Ziel für die Serviceleistung (z. B. Verfügbarkeit, Latenz), das die Kapazität unterstützen muss |
| **Auslastung** | Der Anteil der Gesamtkapazität einer Ressource, der aktuell verwendet wird, typischerweise als Prozentsatz ausgedrückt |

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; Sicherstellung der Kapazität für Sicherheitssysteme (SIEM, Protokollierung, EDR); Compliance-Verifizierung für A.8.6; Eskalation von Kapazitätsrisiken, die die Sicherheitslage beeinflussen; jährliche Richtlinienüberprüfung |
| **ITL / IT-Direktor** | Gesamtverantwortung für die Effektivität des Kapazitätsmanagement-Programms; Genehmigung von Kapazitätserweiterungsplänen; strategische Kapazitätsplanung; Budget-Aufsicht |
| **FL / Finanzen** | Genehmigung von Kapazitätsmanagement-Budgets (CapEx und OpEx); Finanzüberprüfung von Kapazitätsinvestitionen; Kostenoptimierungs-Aufsicht |
| **Infrastrukturmanager / IT-Betriebsmanager** | Tägliche Kapazitätsüberwachung und Alarmreaktion; Schwellenwert-Konfiguration und -Anpassung; Kapazitätsprognose; Berichterstattung; Notfall-Kapazitätsminderung |
| **Cloud-Architekt / Platform-Engineer** | Design und Implementierung von Auto-Scaling-Richtlinien; Cloud-Kontingent-Management; Kostenoptimierung für Cloud-Ressourcen; Planung reservierter Instanzen |
| **Anwendungsverantwortliche / Systemverantwortliche** | Geschäftswachstumsprognosen für Kapazitätsplanung; Teilnahme an Kapazitätsüberprüfungsmeeetings; Budget für anwendungsspezifische Kapazität |
| **Information Security Manager** | Richtlinienpflege; Ausnahmenüberprüfung; Compliance-Berichterstattung; Audit-Koordination; Nachverfolgung von Nichtkonformitäten |
| **Alle Mitarbeitenden** | Meldung beobachteter Leistungsprobleme; Einhaltung genehmigter Ressourcennutzungsrichtlinien |

---

## Nachweise

Die folgenden Nachweise belegen die Konformität mit dieser Richtlinie:

| # | Nachweis | Eigentümer | Häufigkeit | Aufbewahrung |
|---|---------|-----------|------------|--------------|
| 1 | **Überwachungsabdeckungsbericht** mit Prozentsatz der überwachten Produktions- und Nicht-Produktionssysteme | Infrastrukturmanager | Monatlich | 3 Jahre |
| 2 | **Schwellenwert-Konfigurationsdokumentation** für alle überwachten Ressourcen | Infrastrukturmanager | Vierteljährlich überprüft; bei Bedarf aktualisiert | Aktuell + 2 Jahre |
| 3 | **Alarmhistorie und Reaktionsaufzeichnungen** (ausgelöste, bestätigte, gelöste Alarme, Reaktionszeiten) | IT-Betrieb | Kontinuierlich | 3 Jahre |
| 4 | **Monatliche Kapazitätsberichte** mit Auslastungszusammenfassungen und Trenddaten | Infrastrukturmanager | Monatlich | 3 Jahre |
| 5 | **Vierteljährliche Kapazitätsprognosen** mit Genauigkeitsmessungen (tatsächlich vs. vorhergesagt) | Infrastrukturmanager | Vierteljährlich | 3 Jahre |
| 6 | **Jährlicher Kapazitätsplan** mit strategischen Projektionen und Investitionsanforderungen | ITL / Infrastrukturmanager | Jährlich | 5 Jahre |
| 7 | **Auto-Scaling-Konfigurationsaufzeichnungen** und Änderungshistorie | Cloud-Architekt / Platform-Engineer | Kontinuierlich gepflegt; vierteljährlich überprüft | Lebensdauer der Konfiguration + 1 Jahr |
| 8 | **Kapazitätsbezogene Vorfallaufzeichnungen** und Post-Incident-Review-Berichte | IT-Betrieb / Infrastrukturmanager | Pro Vorfall | 3 Jahre |
| 9 | **Lizenzinventar und Nutzungsberichte** mit Berechtigungen vs. aktiven Zuweisungen | IT-Betrieb / Beschaffung | Vierteljährlich | 3 Jahre |
| 10 | **Sitzungsprotokolle des Kapazitätsplanungsausschusses** oder Kapazitätsüberprüfungsmeeting-Notizen | Infrastrukturmanager | Pro Meeting | 3 Jahre |
| 11 | **Ausnahmeregister** für Kapazitätsrichtlinienausnahmen mit Genehmigungen und kompensierenden Kontrollen | Information Security Manager | Kontinuierlich gepflegt; vierteljährlich überprüft | Ausnahmedauer + 3 Jahre |
| 12 | **Speicherwachstums-Trendberichte** (einschliesslich Protokoll-, Datenbank- und Backup-Speicher) | Infrastrukturmanager | Monatlich | 3 Jahre |
| 13 | **Kostenoptimierungsberichte** mit dokumentierten Right-Sizing-Massnahmen, Entscheidungen zur reservierten Kapazität und erzielten Einsparungen | Infrastrukturmanager / Cloud-Architekt | Vierteljährlich | 3 Jahre |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheits-Managementteam verifiziert die Einhaltung dieser Richtlinie durch Monitoring-Abdeckungs-Audits, Schwellenwert-Konfigurationsüberprüfungen, Prognosegenauigkeitsbewertungen, Pünktlichkeit der Kapazitätsberichterstattung, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

**Konformitätskennzahlen**:

| Kennzahl | Ziel | Messhäufigkeit |
|----------|------|----------------|
| Produktionssysteme mit aktiviertem Kapazitätsmonitoring | 100% | Monatlich |
| Nicht-Produktionssysteme mit aktiviertem Kapazitätsmonitoring | >= 90% | Vierteljährlich |
| Ressourcen mit definierten und dokumentierten Schwellenwerten | >= 95% | Vierteljährlich |
| Warnungsalarme innerhalb von 4 Stunden bestätigt (Geschäftszeiten) | >= 90% | Monatlich |
| Kritische Alarme innerhalb von 30 Minuten bestätigt | >= 95% | Monatlich |
| Kapazitätsprognosegenauigkeit (innerhalb +/-15%) | >= 80% der Prognosen | Vierteljährlich |
| Monatliche Kapazitätsberichte termingerecht geliefert | 100% | Monatlich |
| Kapazitätsbezogene Dienstausfälle pro Quartal | < 2 | Vierteljährlich |

**Konformitätsbewertung**:

| Komponente | Gewichtung | Berechnung |
|------------|-----------|------------|
| Überwachungsabdeckung | 30% | (Überwachte Produktionssysteme / Gesamte Produktionssysteme) x 100 |
| Schwellenwert und Alarmierung | 25% | (Ressourcen mit konformen Schwellenwerten + Alarme innerhalb SLA beantwortet) / Gesamt x 100 |
| Prognose und Planung | 25% | (Genaue Prognosen + termingerecht gelieferte Prognosen) / Gesamte Prognosen x 100 |
| Berichterstattung und Governance | 20% | (Termingerecht gelieferte Berichte + abgeschlossene Reviews) / Gesamte Anforderungen x 100 |

**Handhabung von Nichtkonformität**: Unter 70% erfordert sofortige ITL- und ISB-Eskalation mit Sanierungsplan innerhalb von 10 Arbeitstagen. 70–89% erfordert Infrastrukturmanager-Aufsicht mit monatlichen Verbesserungsüberprüfungen. 90% und darüber folgt dem standardmässigen vierteljährlichen Monitoring.

**Sanierungsverantwortung nach Score-Komponente**:

| Komponente | Unter Ziel | Sanierungsverantwortlicher | Eskalation |
|------------|-----------|---------------------------|------------|
| Überwachungsabdeckung | <100% Produktion | Infrastrukturmanager | ITL nach 30 Tagen überfällig |
| Schwellenwert und Alarmierung | <95% | IT-Betrieb / Infrastrukturmanager | ISB nach 15 Tagen überfällig |
| Prognose und Planung | <80% Genauigkeit | Infrastrukturmanager | ITL bei vierteljährlicher Überprüfung |
| Berichterstattung und Governance | <100% termingerecht | Infrastrukturmanager | ITL nach 15 Tagen überfällig |

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll im Voraus vom Information Security Manager genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, kompensierenden Kontrollen und einem definierten Überprüfungsdatum (Maximum 12 Monate). Ausnahmen für kritische Produktionssysteme erfordern gemeinsame ITL- und ISB-Genehmigung. Alle aktiven Ausnahmen sollen vierteljährlich überprüft und dem Management-Review-Team gemeldet werden.

## Nichtkonformität

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterzogen werden, bis hin zur Beendigung des Arbeitsverhältnisses. Richtlinienverstösse sollen dokumentiert, vom Information Security Manager untersucht und dem ISB gemeldet werden. Kapazitätsbezogene Vorfälle, die durch Richtlinienverstösse verursacht wurden (z. B. Versäumnis zu überwachen, Versäumnis auf Alarme zu reagieren), sollen in Post-Mortem-Reviews als beitragende Faktoren behandelt werden.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Änderungen an Infrastrukturplattformen und Cloud-Diensten, Trends bei kapazitätsbezogenen Vorfällen und Beinahe-Vorfällen, Verbesserungen bei Monitoring- und Prognosewerkzeugen, regulatorische Änderungen, die Verfügbarkeitsanforderungen betreffen, Kostenoptimierungsmöglichkeiten sowie Erkenntnisse aus Kapazitätserschöpfungsereignissen berücksichtigen.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Kapazitätsmanagement-Richtlinie — ISO-27001-Controls-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Engagement | 5.1 Richtlinien zur Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Verantwortlichkeiten des Managements |
| Klausel 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| Klausel 9.1 Überwachung, Messung, Analyse und Bewertung | 5.37 Dokumentierte Betriebsverfahren |
| Klausel 9.3 Management Review | 6.3 Bewusstsein, Schulung und Training zur Informationssicherheit |
| | **8.6 Kapazitätsmanagement** |
| | 8.13 Sicherung von Informationen |
| | 8.14 Redundanz von Informationsverarbeitungseinrichtungen |
| | 8.16 Überwachungsaktivitäten |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen; Kapazitätsmanagement gewährleistet die Verfügbarkeit von Systemen, die personenbezogene Daten verarbeiten |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit umfassen die Systemverfügbarkeit |
| EU DSGVO (soweit anwendbar) | Art. 32(1)(b) — Fähigkeit zur dauerhaften Gewährleistung der Vertraulichkeit, Integrität, Verfügbarkeit und Belastbarkeit der Verarbeitungssysteme und -dienste |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.6 — Kapazitätsmanagement |
| ISO/IEC 27002:2022 | Abschnitt 8.6 — Implementierungsleitfaden für das Kapazitätsmanagement |
| NIST SP 800-53 Rev 5 | AU-4 (Audit Log Storage Capacity), CP-2(2) (Capacity Planning), SC-5 (Denial-of-Service Protection) |
| NIST CSF 2.0 | PR.IR-01 (Networks and environments are protected from unauthorized logical access), DE.CM (Continuous Monitoring) |
| CIS Controls v8 | Control 8 (Audit Log Management — log storage capacity), Control 13 (Network Monitoring and Defence) |
| ITIL 4 | Capacity and Performance Management Practice |
| FINMA (soweit anwendbar) | Rundschreiben 2023/1 — IKT-Betriebsresilienz umfasst Kapazitätsmanagement |
| DORA (soweit anwendbar) | Art. 11 — IKT-Kapazitätsplanung für digitale operationale Resilienz |
| NIS2 (soweit anwendbar) | Art. 21(2) — Business Continuity umfasst Kapazitätsmanagement |

---

<!-- QA_VERIFIED: 2026-03-29 -->
