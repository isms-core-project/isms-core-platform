<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.17-DE:operational:OP-POL:a.8.17 -->
**ISMS-OP-POL-A.8.17 — Zeitsynchronisation**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Zeitsynchronisation |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.17 |
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
| 1.0 | [Datum] | ISB | Erstversion der operativen Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt von**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Massnahme A.8.17 — Zeitsynchronisation

**Verwandte Annex-A-Massnahmen**:

| Massnahme | Bezug zur Zeitsynchronisation |
|-----------|-------------------------------|
| A.8.15 Protokollierung | Genaue Zeitstempel sind eine Voraussetzung für aussagekräftige Protokolleinträge |
| A.8.16 Überwachungsaktivitäten | Ereigniskorrelation hängt von synchronisierten Uhren über Systeme hinweg ab |
| A.5.24–28 Vorfallmanagement | Forensische Untersuchung erfordert einen konsistenten Zeitplan über alle Systeme hinweg |
| A.5.28 Sammlung von Beweisen | Uhrengenauigkeit unterstützt die rechtliche Zulässigkeit digitaler Beweise |
| A.8.20 Netzwerksicherheit | Netzwerkgeräte müssen für Sicherheitsereignis-Korrelation zeitsynchronisiert sein |

**Verwandte interne Richtlinien**:

- Protokollierungsrichtlinie (A.8.15)
- Richtlinie zu Überwachungsaktivitäten (A.8.16)
- Richtlinie zum Vorfallmanagement
- Netzwerksicherheitsrichtlinie

---

# Zeitsynchronisationsrichtlinie

## Zweck

Zweck dieser Richtlinie ist es, sicherzustellen, dass die Uhren aller relevanten Informationsverarbeitungssysteme innerhalb der Organisation mit einer einzigen, konsistenten Referenzzeitquelle synchronisiert werden. Genaue und konsistente Zeitstempel sind unerlässlich für Protokollkorrelation, Vorfalluntersuchung, forensische Beweise, regulatorische Compliance und die Integrität verteilter Systeme.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 8 durch die Aufrechterhaltung der Datenintegrität durch verifizierbare Zeitstempel. Soweit die Organisation Daten von Personen im EU/EWR-Raum verarbeitet, gilt zudem DSGVO Art. 32 (Sicherheit der Verarbeitung). Die DSV-Art.-4-Protokollierungspflichten für die Verarbeitung besonders schützenswerter Personendaten erfordern genaue Zeitstempel, um Protokollintegrität und Nachvollziehbarkeit sicherzustellen.

## Geltungsbereich

Diese Richtlinie gilt für alle Systeme, die Protokolldaten oder zeitkritische Aufzeichnungen generieren, einschliesslich:

- Server und Workstations (physisch und virtuell).
- Netzwerkinfrastruktur (Router, Switches, Firewalls, Load Balancer, Wireless-Controller).
- Sicherheitsgeräte (IDS/IPS, EDR-Agenten, Zugangskontrollsysteme).
- Cloud-Dienste und SaaS-Plattformen.
- Datenbankserver und Anwendungsserver.
- Physische Sicherheitssysteme (CCTV, Zugangsleser), sofern in IT-Protokollierung integriert.
- IoT- und Betriebstechnologie-(OT-)Geräte im ISMS-Geltungsbereich.

Alle Mitarbeitenden und Drittbenutzer, die für Systemadministration oder -bereitstellung verantwortlich sind, sind für die Sicherstellung der Zeitsynchronisation auf von ihnen verwalteten Systemen verantwortlich.

## Grundsatz

Alle Uhren sollen mit einer einzigen, organisatorisch genehmigten Referenzzeitquelle synchronisiert werden. Zeitdaten sollen vor nicht autorisierter Änderung geschützt werden. Zeitstempel sollen in einem konsistenten Format aufgezeichnet werden, um zuverlässige Korrelation über Systeme, Standorte und Dienstleister hinweg zu ermöglichen.

---

## Autoritative Zeitquellen

### Primäre Referenz

Die Organisation soll eine primäre autoritative Zeitquelle bestimmen:

| Attribut | Anforderung |
|----------|-------------|
| **Primärquelle** | METAS (Eidgenössisches Institut für Metrologie) NTP-Server: `ntp.metas.ch`, `ntp11.metas.ch`, `ntp12.metas.ch`, `ntp13.metas.ch` — Stratum 1, rückführbar auf UTC(CH) |
| **Sekundärquelle** | Schweizerischer NTP-Pool: `0.ch.pool.ntp.org`, `1.ch.pool.ntp.org`, `2.ch.pool.ntp.org`, `3.ch.pool.ntp.org` |
| **Mindestquellen** | Jeder interne Zeitserver soll mit mindestens **zwei** unabhängigen externen Quellen synchronisiert sein (gemäss CIS Control 8.4) |
| **Rückführbarkeit** | Die Primärquelle soll auf ein nationales Metrologie-Institut oder GPS/GNSS-Zeitsignal rückführbar sein |

### Interne Zeitarchitektur

Die Organisation soll interne NTP-Server in einer abgestuften Architektur einsetzen:

| Stufe | Rolle | Konfiguration |
|-------|-------|---------------|
| **Internes Stratum 2** | Primäre interne NTP-Server, direkt mit externen Stratum-1-Quellen (METAS) synchronisiert | Mindestens 2 Server für Redundanz; geografisch getrennt, soweit machbar |
| **Internes Stratum 3** | Standort- oder abteilungsebene Server (optional für grössere Umgebungen) | Synchronisation mit internem Stratum 2; bedient lokale Clients |
| **Clients** | Alle Endpunkte, Anwendungsserver, Netzwerkgeräte | Synchronisation mit internem Stratum 2 oder Stratum 3 über NTP |

Für kleine Organisationen: Der primäre Domain-Controller oder ein designierter interner Server kann als einziger interner NTP-Server dienen, synchronisiert mit mindestens zwei externen Quellen.

Wo die Organisation GPS-disziplinierte Oszillatoren (GPSDOs) für Stratum-0/1-Unabhängigkeit betreibt (z. B. Air-gapped-Netzwerke), sollen diese dokumentiert und gemäss Herstellerspezifikationen gewartet werden.

---

## Synchronisationsprotokoll

### NTP-Konfiguration

Das Network Time Protocol (NTP) soll für die Zeitsynchronisation über alle Standard-Unternehmenssysteme verwendet werden.

| Anforderung | Spezifikation |
|-------------|---------------|
| **Protokoll** | NTPv4 (RFC 5905) Minimum |
| **Sicherheit** | Network Time Security (NTS, RFC 8915) soll aktiviert werden, wo von Client und Server unterstützt. Wo NTS nicht unterstützt wird, soll NTP-Kommunikation durch Firewall-Regeln oder Zugriffskontrolllisten auf genehmigte Server beschränkt werden. |
| **Authentifizierung** | NTP-symmetrische Schlüsselauthentifizierung oder NTS soll zwischen internen Servern und externen Quellen verwendet werden |
| **Abfrageintervall** | Standard (64–1024 Sekunden); kürzere Intervalle für kritische Systeme, falls erforderlich |
| **Firewall-Regeln** | Ausgehendes NTP (UDP 123) nur zu genehmigten externen Quellen erlaubt; eingehendes NTP auf interne Server beschränkt |

### Precision Time Protocol (PTP)

Wo Sub-Mikrosekunden-Genauigkeit erforderlich ist (z. B. Finanzhandel, industrielle Steuerung, Hochfrequenz-Datenverarbeitung), soll IEEE 1588 Precision Time Protocol (PTPv2) eingesetzt werden:

- PTP-fähige Netzwerk-Switches (Boundary- oder Transparent-Clocks) sind erforderlich.
- Eine PTP-Grandmaster-Clock (GPS-diszipliniert) soll eingesetzt werden.
- PTP ist eine Ergänzung zu — kein Ersatz für — NTP im allgemeinen Unternehmen.

Die PTP-Anwendbarkeit wird während des Systemdesigns bestimmt und in der Systemarchitektur dokumentiert.

---

## Zeitstempelformat

### Standardformat

Alle Systeme sollen Zeitstempel in einem der folgenden Formate aufzeichnen:

| Format | Beispiel | Anwendungsfall |
|--------|---------|----------------|
| **UTC** (bevorzugt) | `2026-02-07T14:30:00Z` | Server, Datenbanken, Netzwerkgeräte, SIEM, alle Infrastruktur |
| **Lokalzeit mit UTC-Offset** | `2026-02-07T15:30:00+01:00` | Anwendungsprotokolle, benutzerorientierte Berichte (wo UTC unpraktisch) |

**Obligatorische Regeln:**

- ISO 8601 / RFC 3339 Format soll für alle maschinengenerierten Zeitstempel verwendet werden.
- **UTC ist der Standard** für alle Infrastruktur-, Protokollierungs- und Sicherheitssysteme.
- Lokalzeit mit explizitem UTC-Offset ist nur auf der Anwendungs-/Präsentationsebene gestattet.
- Lokalzeit **ohne** UTC-Offset (z. B. `15:30:00 CET`) ist **nicht akzeptabel** — Zeitzonen-Abkürzungen sind mehrdeutig (CET/CEST-Übergänge erzeugen doppelte Stunden).
- Benannte Zeitzonen-Abkürzungen sollen in Protokollzeitstempeln nicht verwendet werden.

### Sommerzeit

UTC eliminiert Sommerzeit-(DST-)Mehrdeutigkeit. Beim Herbstübergang (MESZ → MEZ) wiederholt sich die Stunde 02:00–03:00. Systeme, die Lokalzeit ohne Offset verwenden, können zwischen den beiden Vorkommen nicht unterscheiden. Systeme, die in UTC aufzeichnen, sind davon nicht betroffen.

Alle Systeme sollen UTC oder expliziten Offset verwenden, um DST-bedingte Zeitstempel-Mehrdeutigkeit zu verhindern.

---

## Uhrendrift-Toleranzen

### Maximale akzeptable Abweichung

Systeme sollen Uhrengenauigkeit innerhalb der folgenden Toleranzen aufrechterhalten:

| Systemstufe | Maximale Abweichung | Überwachungsschwelle | Massnahme |
|-------------|---------------------|---------------------|-----------|
| **Kritisch** (Authentifizierung, SIEM, Finanzen, Datenbanken) | < 1 ms | Alarm bei > 1 ms | Sofort untersuchen und resynchronisieren |
| **Standard-Unternehmen** (Server, Netzwerkgeräte) | < 50 ms | Alarm bei > 50 ms | Innerhalb von 4 Stunden untersuchen |
| **Allgemein** (Workstations, Drucker) | < 500 ms | Alarm bei > 500 ms | Beim nächsten Abfragezyklus resynchronisieren |
| **Alarm** (jedes System) | > 128 ms | NTP-Step-Schwelle | NTP-Client führt Step (Sprung) durch; Ereignis protokollieren |
| **Panik** (jedes System) | > 1000 Sekunden | NTP-Panik-Schwelle | NTP-Daemon beendet; manuelle Intervention erforderlich |

### Drift-Überwachung

Uhrendrift soll kontinuierlich mit Systemüberwachungstools überwacht werden (z. B. Prometheus, Nagios, CloudWatch oder gleichwertig):

- NTP-Offset-, Jitter- und Stratum-Metriken sollen von allen überwachten Systemen erfasst werden.
- Alarm, wenn Offset die Systemstufen-Schwelle überschreitet.
- Alarm bei Stratum-Änderungen (z. B. ein Server, der von Stratum 2 auf Stratum 16 fällt, zeigt Verlust der Upstream-Synchronisation an).
- Uhrendrift-Alarme sollen an die zentralisierte Überwachungsplattform weitergeleitet werden.
- Monatliche Trendanalyse der Uhrendrift über den gesamten Bestand.

---

## Cloud-Dienst-Zeitsynchronisation

### Anbieterspezifische Zeitquellen

Wo Systeme in Cloud-Umgebungen betrieben werden, soll der Zeitsynchronisationsdienst des Anbieters verwendet werden:

| Anbieter | Zeitdienst | Zugang | Hinweise |
|----------|-----------|--------|---------|
| **AWS** | Amazon Time Sync Service | `169.254.169.123` (Link-Local) | Atomuhren + GPS pro Region; auf Amazon Linux vorkonfiguriert; verwendet Schaltsekundenglättung |
| **Azure** | VMICTimeSync (Hypervisor PTP) | PTP-Gerät innerhalb VM | Zeit über Hypervisor geliefert, nicht über Netzwerk-NTP; Chrony empfohlen |
| **GCP** | Google Public NTP | `time.google.com` | Auf Compute Engine vorkonfiguriert; verwendet Schaltsekundenglättung (24 Stunden) |

### Hybridumgebungsanforderungen

Wo die Organisation über On-Premises- und Cloud-Umgebungen hinweg betrieben wird:

- **Keine gemischten geglätteten und nicht geglätteten Zeitquellen** in derselben Umgebung verwenden. Cloud-Anbieter (AWS, GCP) glätten Schaltsekunden über 24 Stunden; traditionelle NTP-Quellen (METAS, pool.ntp.org) springen. Mischen erzeugt Zeitdiskrepanzen bei Schaltsekunden-Ereignissen.
- Dokumentieren, welche Zeitquelle jede Umgebung verwendet.
- Für Hybrid-Architekturen bestimmen, ob Cloud- oder On-Premises-Zeit autoritativ ist, und Synchronisationsrichtung entsprechend konfigurieren.
- Cloud-VM-Zeitdrift überwachen — Virtualisierungs-Scheduling und Live-Migration können Uhrenverzerrung einführen.

---

## Schaltsekundenbehandlung

Eine Schaltsekunde ist eine Ein-Sekunden-Anpassung (positiv oder negativ), die auf UTC angewendet wird, um sie mit der Erdrotation in Einklang zu halten. Seit 1972 wurden 27 Schaltsekunden hinzugefügt; die Praxis wird voraussichtlich bis spätestens 2035 abgeschafft (gemäss CGPM-Resolution 4, November 2022).

### Organisationsstrategie

Die Organisation soll eine **einzige, konsistente Schaltsekundenbehandlungsstrategie** über alle Umgebungen hinweg übernehmen:

| Strategie | Beschreibung | Anwendung |
|-----------|-------------|-----------|
| **Sprung** (traditionell) | Einfügung oder Entfernung einer Sekunde bei 23:59:60 UTC | On-Premises-Systeme mit traditionellen NTP-Quellen (METAS, pool.ntp.org) |
| **Glättung** | Verteilung der Extra-Sekunde über 24 Stunden durch leichte Anpassung der Taktrate | Cloud-Umgebungen mit Anbieter-Zeitdiensten (AWS, GCP) |

**Regeln:**

- Nie gemischte gesprungene und geglättete Zeitquellen in derselben Umgebung.
- Die gewählte Strategie dokumentieren und an Systemadministratoren kommunizieren.
- Schaltsekundenbehandlung vor jedem geplanten Schaltsekunden-Ereignis testen.
- Systeme für 24 Stunden nach einem Schaltsekunden-Ereignis überwachen.
- Sobald Schaltsekunden abgeschafft werden (voraussichtlich bis 2035), Konfigurationen aktualisieren, um Schaltsekundenbehandlungslogik zu entfernen.

---

## NTP-Sicherheit

### Schutz gegen zeitbasierte Angriffe

NTP-Infrastruktur soll gegen Spoofing-, Replay- und Denial-of-Service-Angriffe geschützt werden:

| Bedrohung | Minderung |
|-----------|-----------|
| **NTP-Spoofing** | NTS (RFC 8915) oder NTP-symmetrische Schlüsselauthentifizierung aktivieren; NTP-Quellen auf genehmigte Server beschränken |
| **Replay-Angriffe** | NTS bietet Replay-Schutz via eindeutigen Cookies pro Austausch |
| **DDoS-Amplifikation** | NTP-Monlist deaktivieren (`restrict ... noquery`); NTP-Zugang auf interne Clients beschränken |
| **Nicht autorisierte Änderung** | NTP-Server-Konfigurationen durch Zugriffskontrollen geschützt; Änderungen erfordern Change-Management-Genehmigung |
| **Single Point of Failure** | Mindestens zwei unabhängige externe Quellen; interne Server-Redundanz |

### Konfigurationsschutz

- NTP-Konfigurationsdateien sollen vor nicht autorisierter Änderung geschützt werden (Dateiberechtigungen, Integritätsüberwachung).
- Änderungen an der NTP-Konfiguration sollen dem Change-Management-Prozess folgen.
- NTP-Dienststatus soll überwacht werden; Dienstausfall soll einen Alarm generieren.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; Genehmigung der Zeitsynchronisationsarchitektur; Eskalationspunkt bei anhaltenden Drift-Problemen |
| **IT-Betrieb / Plattformteam** | NTP-Server-Einsatz und -Wartung; Überwachungskonfiguration; Cloud-Zeitquellen-Konfiguration; Schaltsekunden-Ereignismanagement |
| **Systemadministratoren** | Sicherstellen, dass NTP auf verwalteten Systemen konfiguriert ist; Synchronisationsfehler melden; Zeiteinstellungen bei der Systemeinrichtung verifizieren |
| **Netzwerkadministratoren** | NTP-Konfiguration auf Netzwerkgeräten; Firewall-Regeln für NTP-Verkehr; NTS-Einsatz auf unterstützten Geräten |
| **Cloud-Ingenieure** | Cloud-spezifische Zeitquellen-Konfiguration; Hybrid-Architektur-Zeitquellen-Dokumentation; Cloud-VM-Drift-Überwachung |

---

## Nachweise

Die folgenden Nachweise demonstrieren die Einhaltung dieser Richtlinie:

| # | Nachweis | Verantwortlich | Häufigkeit |
|---|----------|----------------|------------|
| 1 | **NTP-Architekturdokumentation** (interne Server, externe Quellen, Stratum-Hierarchie, Protokoll-/Sicherheitseinstellungen) | IT-Betrieb | *Dokumentiert; jährlich und bei Architekturänderungen überprüft* |
| 2 | **NTP-Compliance-Abdeckungsmetrik** (Prozentsatz der im Geltungsbereich befindlichen Systeme mit verifizierter NTP-Konfiguration und genehmigten Zeitquellen) | IT-Betrieb | *Vierteljährlich; Ziel: 100 % der kritischen Systeme, ≥95 % aller im Geltungsbereich* |
| 3 | **Uhrendrift-Überwachungsaufzeichnungen** (Offset-, Jitter-, Stratum-Metriken; generierte und gelöste Alarme) | IT-Betrieb | *Kontinuierliche Überwachung; monatlicher Trendbericht; Alarme 12 Monate aufbewahrt* |
| 4 | **Cloud-Zeitquellen-Dokumentation** (Anbieter-Dienst, Konfiguration, Glättungsstrategie, Hybrid-Überlegungen) | Cloud-Ingenieure | *Pro Cloud-Dienst dokumentiert; jährlich überprüft* |
| 5 | **NTP-Sicherheitskonfiguration** (NTS-Status, Authentifizierung, Firewall-Regeln, Zugangsbeschränkungen) | IT-Betrieb / Netzwerk | *Konfiguration dokumentiert; jährlich überprüft* |
| 6 | **Zeitstempelformat-Compliance** (Muster-Protokolleinträge von 5+ Systemen, die UTC oder Offset-Format demonstrieren) | Informationssicherheit | *Jährlich während Revision verifiziert* |
| 7 | **Schaltsekundenstrategiedokumentation** (gewählter Ansatz, Testaufzeichnungen, Überwachung während Ereignissen) | IT-Betrieb | *Dokumentiert; vor jedem Schaltsekunden-Ereignis getestet (oder jährlich, falls keines geplant)* |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheitsmanagement-Team soll die Einhaltung dieser Richtlinie durch NTP-Konfigurationsüberprüfungen, Drift-Überwachungsreviews, Zeitstempelformat-Verifikation, interne und externe Revisionen sowie Rückmeldungen an den Richtlinieneigentümer verifizieren.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll im Voraus vom Informationssicherheitsbeauftragten genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum. Ausnahmen sollen dem Management-Review-Team gemeldet werden.

Systeme, die NTP nicht unterstützen können (z. B. ältere OT-Geräte, isolierte Testumgebungen), sollen mit Begründung dokumentiert werden, und manuelle Zeitverifikation soll in einer definierten Häufigkeit durchgeführt werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Änderungen der NTP-Standards, Zeitquellenverfügbarkeit, Cloud-Anbieter-Zeitdienste, Schaltsekunden-Richtlinienentwicklungen sowie Lessons Learned aus Uhrendrift-Vorfällen oder forensischen Untersuchungen berücksichtigen.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Zeitsynchronisationsrichtlinie — Zuordnung der ISO-27001-Massnahmen

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Abschnitt 5.1 Führung und Verpflichtung | 5.1 Richtlinien zur Informationssicherheit |
| Abschnitt 5.2 Richtlinie | 5.4 Managementverantwortlichkeiten |
| Abschnitt 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| | 5.37 Dokumentierte Betriebsverfahren |
| | 6.3 Informationssicherheitsbewusstsein, -ausbildung und -schulung |
| | **8.17 Zeitsynchronisation** |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen (Datenintegrität) |
| Schweizerische DSV (Datenschutzverordnung) | Art. 4 — Protokollierungspflichten (genaue Zeitstempel erforderlich) |
| EU-DSGVO (wo anwendbar) | Art. 32 — Sicherheit der Verarbeitung |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.17 |
| ISO/IEC 27002:2022 | Abschnitt 8.17 — Implementierungsleitfaden |
| NIST SP 800-53 Rev 5 | AU-8 (Time Stamps), AU-8(1) (Synchronisation with Authoritative Source), SC-45 (System Time Synchronisation) |
| NIST CSF 2.0 | PR.PS-04 (Log records generated for continuous monitoring) |
| CIS Controls v8 | Control 8.4 (Standardise Time Synchronisation) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
