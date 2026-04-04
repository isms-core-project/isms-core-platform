<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.30-8.13-14-DE:operational:OP-POL:a.5.30-8.13-14 -->
**ISMS-OP-POL-A.5.30-8.13-14 — Geschäftskontinuität und Disaster Recovery**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Geschäftskontinuität und Disaster Recovery |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.5.30-8.13-14 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erste operative Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Kontrolle A.5.30 — IKT-Bereitschaft für Geschäftskontinuität
- ISO/IEC 27001:2022 Kontrolle A.8.13 — Informations-Backup
- ISO/IEC 27001:2022 Kontrolle A.8.14 — Redundanz von Informationsverarbeitungseinrichtungen
- ISO/IEC 22301 — Business-Continuity-Managementsysteme (informativer Verweis)
- NIST SP 800-34 Rev 1 — Contingency Planning Guide for Federal Information Systems (informativer Verweis)

**Verwandte Annex-A-Kontrollen**:

| Kontrolle | Bezug zu Geschäftskontinuität und Disaster Recovery |
|-----------|------------------------------------------------------|
| A.5.9 Inventar von Informationen und anderen zugehörigen Assets | Asset-Inventar treibt BIA und Identifizierung des Backup-Umfangs |
| A.5.19–23 Lieferantenbeziehungen und Cloud-Dienste | BC/DR-Verpflichtungen von Lieferanten und Modell der geteilten Verantwortung |
| A.5.24–28 Incident-Management-Lebenszyklus | Grössere Vorfälle können die Aktivierung von BC/DR-Plänen auslösen |
| A.5.29 Informationssicherheit bei Störungen | Sicherheitskontinuität während BC/DR-Ereignissen |
| A.8.6 Kapazitätsmanagement | Kapazitätsplanung unterstützt Redundanz und DR-Infrastruktur |
| A.8.9 Konfigurationsmanagement | Konfigurationsbaselines für Systemwiederaufbau und -wiederherstellung erforderlich |
| A.8.15 Protokollierung | Backup- und Wiederherstellungsoperationen sollten protokolliert werden |
| A.8.16 Überwachungsaktivitäten | Backup-Überwachung und Redundanz-Health-Checks |

**Verwandte interne Richtlinien**:

- Asset-Management-Richtlinie
- Richtlinie zum Incident Management
- Richtlinie für Cloud-Dienste und Lieferantensicherheit
- Protokollierungsrichtlinie
- Richtlinie zu Überwachungsaktivitäten (A.8.16)
- Change-Management-Richtlinie

---

# Richtlinie zur Geschäftskontinuität und Disaster Recovery

## Zweck

Diese Richtlinie soll sicherstellen, dass die Organisation nach einem störenden Vorfall ihren kritischen Geschäftsbetrieb und ihre Informationsverarbeitungseinrichtungen fortführen oder wiederherstellen kann. Sie legt Anforderungen an Geschäftsauswirkungsanalyse, Informations-Backup, Systemredundanz und IKT-Kontinuitätsplanung fest.

Diese Richtlinie behandelt drei verwandte ISO-27001:2022-Kontrollen als einheitliches Framework, da sie als integriertes BC/DR-Ökosystem arbeiten: Backup bietet Datenwiederherstellungsfähigkeit (A.8.13), Redundanz bietet Systemverfügbarkeitsfähigkeit (A.8.14) und IKT-Bereitschaft bietet allgemeine Vorbereitung und Governance (A.5.30). Jede Kontrolle behält für Anwendbarkeitserklärungszwecke eigenständige Anforderungen.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 8, indem technische und organisatorische Massnahmen entsprechend dem Risiko zum Schutz der Verfügbarkeit und Integrität personenbezogener Daten und Informationsverarbeitungssysteme umgesetzt werden. Soweit die Organisation Daten von Personen in der EU/EEA verarbeitet, gelten auch die DSGVO-Art.-32(1)(c)-Anforderungen für die Fähigkeit, die Verfügbarkeit und den Zugang zu personenbezogenen Daten zeitnah wiederherzustellen.

## Geltungsbereich

Alle Mitarbeitenden und Drittnutzer.

Alle Informationssysteme, Anwendungen, Infrastruktur und Dienste, die im ISO-27001-Anwendungsbereich enthalten sind, einschliesslich:

- Server, Datenbanken und Code-Repositories
- Cloud-Infrastruktur und SaaS-Anwendungen
- Netzwerkinfrastruktur und Sicherheitssysteme
- Geschäftskritische Anwendungen und Daten
- Systemkonfigurationen und Infrastructure-as-Code

**Ausserhalb des Backup-Bereichs** (sofern nicht spezifisch risikobeurteilt):

- Desktop- und Laptop-Lokalspeicher (Daten sollten auf gesicherten Servern, Cloud-Diensten oder Repositories liegen; nur-lokale Daten sind durch dauerhaften Verlust gefährdet und durch diese Richtlinie nicht geschützt)
- Lokalspeicher mobiler Geräte

**Ausserhalb des Geltungsbereichs dieser Richtlinie**:

- Nicht-IKT-Geschäftskontinuität (organisatorisches BCM-Framework)
- Physische Aufzeichnungen und nicht-digitale Informationen (durch physische Sicherheitskontrollen abgedeckt)

## Grundsatz

**Die Sicherheit der Menschen hat stets oberste Priorität.**

Das Business-Continuity-Management und die Informationssicherheitskontinuität sollten Bedrohungen, Risiken und Vorfälle adressieren, die die Kontinuität des Betriebs beeinträchtigen. Das Framework basiert auf Best Practices der Branche und ist auf ISO 22301 Business Continuity Management ausgerichtet.

Die Organisation sollte:

- Geschäftsauswirkungsanalysen durchführen, um kritische Systeme zu identifizieren und Wiederherstellungsanforderungen zu bestimmen.
- Backup-Kopien von Informationen, Software und Systemen aufbewahren, die regelmässig getestet werden, um die Wiederherstellbarkeit zu bestätigen.
- Redundanz für kritische Informationsverarbeitungseinrichtungen implementieren, um Verfügbarkeitsanforderungen zu erfüllen.
- IKT-Kontinuität basierend auf Geschäftskontinuitätszielen planen, implementieren, aufrechterhalten und testen.

**Kritisches Grundsatz — «Ungetestete Wiederherstellung = Keine Wiederherstellung»**: Backup-Erfolg ohne Wiederherstellungstest, Redundanz ohne Failover-Test und BC-Pläne ohne Szenariotest bieten falsches Vertrauen. Evidenzbasierte Verifizierung durch systematisches Testen ist erforderlich.

---

## Geschäftsauswirkungsanalyse und Systemkritikalität

### Geschäftsauswirkungsanalyse

Geschäftskontinuität sollte auf einer dokumentierten Geschäftsauswirkungsanalyse (BIA) und Risikobewertung basieren. Die BIA sollte:

- Kritische Geschäftsprozesse und ihre IKT-Abhängigkeiten identifizieren.
- Die Auswirkungen von IKT-Störungen quantifizieren (finanziell, operativ, reputationsmässig, regulatorisch).
- Recovery Point Objectives (RPO) und Recovery Time Objectives (RTO) für jedes kritische System festlegen.
- Gegenseitige Abhängigkeiten zwischen Systemen identifizieren.

**BIA-Häufigkeit**: Die BIA sollte zunächst bei der ISMS-Implementierung durchgeführt, jährlich überprüft und bei wesentlichen Geschäftsänderungen (neue Dienste, Akquisitionen, wesentliche Systemänderungen) oder nach grösseren Vorfällen aktualisiert werden.

### Systemkritikalitätsstufen

Systeme sollten basierend auf BIA-Ergebnissen in Kritikalitätsstufen klassifiziert werden. Diese Stufen bestimmen Backup-Häufigkeit, Redundanzanforderungen und Testpläne:

| Stufe | Klassifizierung | Maximales RPO | Maximales RTO | Beispiele |
|-------|-----------------|---------------|---------------|-----------|
| **Stufe 1** | Kritisch | 1 Stunde | 4 Stunden | Kerngeschäftsanwendung, primäre Datenbank, Authentifizierungssystem |
| **Stufe 2** | Hoch | 6 Stunden | 24 Stunden | E-Mail, Kollaborationsplattform, sekundäre Geschäftsanwendungen |
| **Stufe 3** | Mittel | 24 Stunden | 72 Stunden | Interne Tools, Entwicklungsumgebungen, Berichtssysteme |
| **Stufe 4** | Niedrig | 7 Tage | > 72 Stunden | Archive, nicht-kritische interne Dienste |

Systemeigentümer sollten in Abstimmung mit dem BC/DR-Koordinator die geeignete Stufe für jedes System anhand der BIA-Ergebnisse bestimmen.

**Rollenzuweisung**: Wenn die Organisation keinen dedizierten BC/DR-Koordinator hat, sollte der IT-Betriebsmanager die BC/DR-Koordinationsverantwortlichkeiten übernehmen. Diese Zuweisung sollte formal in der Rollenbeschreibung dokumentiert werden.

### RPO und RTO

**Recovery Point Objective (RPO)** definiert den maximal akzeptablen Datenverlust, gemessen in Zeit. RPO bestimmt die Backup-Häufigkeit. Beispiel: Ein RPO von 6 Stunden bedeutet, dass ein Datenverlust von bis zu 6 Stunden akzeptabel ist, sodass Backups mindestens alle 6 Stunden erfolgen müssen.

**Recovery Time Objective (RTO)** definiert die maximal akzeptable Zeit zur Wiederherstellung eines Systems nach einer Störung. RTO bestimmt Redundanz und Wiederherstellungsstrategie. Beispiel: Ein RTO von 4 Stunden bedeutet, dass das System innerhalb von 4 Stunden nach einem Ausfall betriebsbereit sein muss.

Systeme, die ihre definierten RPO oder RTO nicht erfüllen können, sollten dem Ausnahmemanagementprozess folgen (siehe Richtlinienkonformität — Ausnahmen).

---

## Informations-Backup

### Backup-Umfang

Die folgenden Informationskategorien sollten gesichert werden:

| Kategorie | Backup-Anforderung |
|-----------|-------------------|
| Kritische Geschäftsdaten (Kunden, Finanzen, Betrieb) | Obligatorisch |
| Produktionssystemdaten und -konfigurationen | Obligatorisch |
| Anwendungssoftware und Abhängigkeiten | Obligatorisch |
| Sicherheitskonfigurationen und Zugriffssteuerungsdaten | Obligatorisch |
| Wichtige Geschäftsdaten | Obligatorisch |
| Entwicklungs-/Testumgebungen | Risikobasiert (Backup, wenn Wiederherstellungskosten Backup-Kosten übersteigen) |
| Ephemere Daten (Caches, temporäre Protokolle) | Nicht erforderlich |

### Backup-Zeitplan und Aufbewahrung

Ein Backup-Zeitplan, Aufbewahrungsplan und Testzeitplan sollte geführt und zur Verfügung gestellt werden. Die Backup-Häufigkeit sollte dem RPO für jede Systemstufe entsprechen:

| Systemstufe | Backup-Häufigkeit | Mindestaufbewahrung |
|-------------|-------------------|---------------------|
| **Stufe 1 (Kritisch)** | Kontinuierliche Replikation oder stündlich | Täglich: 30 Tage; Wöchentlich: 90 Tage; Monatlich: 12 Monate |
| **Stufe 2 (Hoch)** | Alle 4–6 Stunden | Täglich: 30 Tage; Wöchentlich: 90 Tage; Monatlich: 12 Monate |
| **Stufe 3 (Mittel)** | Täglich | Täglich: 7 Tage; Wöchentlich: 28 Tage; Monatlich: 12 Monate |
| **Stufe 4 (Niedrig)** | Wöchentlich oder bei Änderung | Wöchentlich: 28 Tage; Monatlich: 12 Monate |

**Verlängerte Aufbewahrung**: Längere Aufbewahrungszeiträume können durch Vorschriften (z. B. Finanzunterlagen 7–10 Jahre), gesetzliche Aufbewahrungspflichten oder vertragliche Verpflichtungen erforderlich sein. Verlängerte Aufbewahrung sollte begründet sein (regulatorische Anforderung, gesetzliche Aufbewahrungspflicht oder vertragliche Verpflichtung), um unnötige Datenakkumulation zu verhindern. Kürzere Aufbewahrungszeiträume erfordern ISB-Genehmigung mit dokumentierter Risikoakzeptanz.

### Backup-Typen

Die Organisation sollte geeignete Backup-Strategien basierend auf Systemanforderungen auswählen:

| Backup-Typ | Beschreibung | Verwendungsfall |
|------------|--------------|-----------------|
| **Voll** | Vollständige Kopie aller Daten | Basis-Backup; wöchentlich oder monatlich |
| **Inkrementell** | Geänderte Daten seit letztem Backup (beliebiger Typ) | Tägliche Backups; schnell, speichereffizient |
| **Differenziell** | Geänderte Daten seit letztem vollständigen Backup | Tägliche Backups; schnellere Wiederherstellung als inkrementell |
| **Snapshot** | Point-in-Time-Kopie auf Speicherebene | Häufige Backups; VMs und Cloud-Workloads |
| **Kontinuierlicher Datenschutz** | Echtzeit- oder nahezu Echtzeitreplikation | Stufe-1-Systeme mit RPO < 1 Stunde |

### 3-2-1-Backup-Regel

Die Organisation sollte die 3-2-1-Backup-Regel als Minimum für Stufe-1- und Stufe-2-Systeme implementieren:

| Element | Anforderung |
|---------|------------|
| **3 Kopien** | Originaldaten plus mindestens 2 Backup-Kopien |
| **2 Medientypen** | Verschiedene Speichertechnologien (z. B. Disk + Cloud, Disk + Tape) |
| **1 Offsite-Kopie** | Geografisch getrennter Standort (anderes Gebäude, Region oder Cloud-Region) |

**Unveränderliche Backups**: Für Stufe-1- und Stufe-2-Systeme sollte mindestens eine Backup-Kopie unveränderlich (Write-Once-Read-Many) oder air-gapped sein, um gegen Ransomware und versehentliches Löschen zu schützen. Technologien umfassen Objekt-Speicher mit Object Lock (z. B. AWS S3 Object Lock, Azure Immutable Blob Storage oder Äquivalent), WORM-Tape oder Air-Gapped-Offline-Medien.

**Bedingt**: Organisationen, die DORA unterliegen (EU-Finanzinstitute), sollten unveränderliche Backup-Kopien implementieren, sofern technisch möglich (Art. 12(4)), und Offsite-Backup-Speicherung in ausreichender geografischer Entfernung.

### Backup-Sicherheit

- Backups sollten sowohl bei der Übertragung als auch im Ruhezustand mit AES-256 oder Äquivalent verschlüsselt werden, gemäss der Richtlinie zum Einsatz von Kryptografie (A.8.24). Die Backup-Lösung (z. B. Veeam, Commvault, AWS Backup, Azure Backup oder Äquivalent) sollte integrierte Verschlüsselung unterstützen.
- In Cloud-basierten Lösungen gespeicherte Backups sollten mindestens bei einem ISO-27001-zertifizierten Anbieter gehostet werden.
- Wenn Backup auf physische Medien erfolgt:
  - Die Medien sollten verschlüsselt sein.
  - Die Medien sollten beschriftet und sicher mit eingeschränkter, autorisierungspflichtiger Zugangskontrolle gespeichert werden.
  - Offsite-Transfer sollte einen genehmigten sicheren Kurier oder verschlüsselten elektronischen Transfer verwenden.
- Backups sollten mindestens auf dem gleichen Sicherheitsniveau wie die Originaldaten geschützt sein.
- **Backup-Verschlüsselungs-Schlüsselverwaltung**: Verschlüsselungsschlüssel sollten getrennt von Backup-Daten verwaltet werden. Schlüsselwiederherstellungsverfahren sollten dokumentiert und getestet werden (Schlüssel müssen zugänglich sein, wenn primäre Systeme nicht verfügbar sind). Schlüssel sollten jährlich oder bei vermutetem Kompromiss rotiert werden. Schlüssel-Escrow oder geteilte Schlüsselverwahrung wird für Backups kritischer Systeme empfohlen. Schlüsselverwaltung sollte der Richtlinie zum Einsatz von Kryptografie (A.8.24) entsprechen.

### Backup-Portabilität

Um Anbieterabhängigkeit zu vermeiden, sollten Backup-Implementierungen sicherstellen:

- Backups sind in branchenübliche Formate exportierbar, sofern möglich.
- Cloud-Backups sind in alternative Umgebungen wiederherstellbar (anderer Cloud-Anbieter oder vor Ort).
- Wiederherstellungsverfahren adressieren Anbieterausstiegsszenarien.

### Backup-Überwachung

Backup-Operationen sollten überwacht werden:

| Element | Anforderung |
|---------|------------|
| Backup-Erfolg/Misserfolg | Echtzeit-Überwachung; sofortige Meldung bei Misserfolg für Stufe-1-2-Systeme |
| Backup-Dauer | Meldung wenn Dauer das Backup-Fenster überschreitet |
| Speicherkapazität | Warnung bei 70 % Auslastung; Meldung bei 80 %; kritisch bei 90 % |
| Offsite-Replikation | Meldung bei Replikationsfehler |

Backup-Protokolle sollten erstellt und mindestens wöchentlich auf Fehler und Performance überprüft werden. Wenn Fehler gefunden werden, sollten Korrekturmassnahmen ergriffen und aufgezeichnet werden.

Monatliche Backup-Statusberichte sollten dem ISB bereitgestellt werden, einschliesslich Backup-Abdeckung, Erfolgsraten und offener Probleme.

### Backup-Tests und Verifizierung

Backups sollten regelmässig getestet werden, um sicherzustellen, dass sie im Notfall verlässlich sind und den Anforderungen der Geschäftskontinuitätspläne entsprechen:

| Systemstufe | Wiederherstellungstest-Häufigkeit | Testumfang |
|-------------|-----------------------------------|-----------|
| **Stufe 1 (Kritisch)** | Vierteljährlich | Vollständige Systemwiederherstellung in alternative Umgebung |
| **Stufe 2 (Hoch)** | Halbjährlich | Repräsentative Datensätze; vollständiges System jährlich |
| **Stufe 3 (Mittel)** | Jährlich | Stichproben-Wiederherstellungsverifizierung |
| **Stufe 4 (Niedrig)** | Bei wesentlicher Änderung | Stichproben-Wiederherstellung oder dokumentierte Risikoakzeptanz |

Jeder Wiederherstellungstest sollte dokumentieren: Testdatum, getestete Systeme, Backup-Quelle, erwartete vs. tatsächliche Wiederherstellungszeit, Datenintegritätsverifizierung, aufgetretene Probleme und Abzeichnung durch den Testeigentümer.

**Reaktion auf fehlgeschlagene Tests**: Wiederherstellungstests, die Wiederherstellungsfehler aufdecken, sollten eine Eskalation basierend auf der Systemstufe auslösen:

| Stufe | Benachrichtigung | Behebungsplan | Statusaktualisierungen | Eskalation |
|-------|-----------------|---------------|------------------------|------------|
| **Stufe 1** | Geschäftsleitungsbenachrichtigung innerhalb von 4 Stunden | Innerhalb von 24 Stunden | Täglich | Bei nächster Managementüberprüfung gemeldet; wiederkehrende Fehler (dasselbe System zweimal in 12 Monaten) lösen Architekturüberprüfung aus |
| **Stufe 2** | ISB-Benachrichtigung innerhalb von 24 Stunden | Innerhalb von 5 Werktagen | Wöchentlich | Bei nächster Managementüberprüfung gemeldet |
| **Stufe 3–4** | Risikoregister-Aktualisierung innerhalb von 10 Werktagen | Nächstes Wartungsfenster | Monatlich | Vierteljährliche Überprüfung |

Neutest sollte innerhalb von 30 Tagen nach der Behebung für Stufe-1-2-Systeme erfolgen.

**Bedingt**: Organisationen, die DORA unterliegen, sollten Backup-Wiederherstellung mindestens jährlich testen (Art. 12(6)).

### Wiederherstellungsverfahren

Backup- und Wiederherstellungsverfahren sollten dokumentiert, gepflegt und zugänglich gehalten werden (auch wenn primäre Systeme nicht verfügbar sind). Wiederherstellungsverfahren für jedes kritische System sollten umfassen:

- Schritt-für-Schritt-Wiederherstellungsprozess.
- Erforderliche Zugangsdaten und Autorisierung.
- Schätzung der Wiederherstellungszeit vs. RTO-Ziel (einschliesslich 25 % Puffer für unvorhergesehene Komplikationen).
- Validierungsschritte zur Bestätigung der erfolgreichen Wiederherstellung.
- Eskalationskontakte.

### Cloud-Backup-Verantwortlichkeiten

Für Cloud-gehostete Systeme sollte die Organisation:

- Das Modell der geteilten Verantwortung des Anbieters verstehen (was der Anbieter sichert vs. was der Kunde sichern muss).
- Vom Kunden verwaltete Backups implementieren, wenn Anbieterfähigkeiten RPO-Anforderungen nicht erfüllen.
- SaaS-Datenexport- und Wiederherstellungsverfahren testen.
- Cloud-zu-lokal-Wiederherstellungsverfahren für erweiterte Cloud-Ausfallszenarien dokumentieren.

### Ausrichtung an Cloud-Anbieter-SLA

- Cloud-Anbieter-SLA-Garantien sollten gegen die RTO-Anforderungen der Organisation für jede Systemstufe verifiziert werden.
- Historische Anbieter-Verfügbarkeit und Incident-Response-Performance sollten während der Anbieterbeurteilung dokumentiert werden (gemäss A.5.19–23).
- Wenn Anbieter-SLA für Stufe-1- oder Stufe-2-Systeme unzureichend ist, sollte vom Kunden verwaltete Redundanz implementiert werden.
- BC/DR-Fähigkeiten des Cloud-Anbieters (Multi-AZ, Backup/Wiederherstellung, Failover) sollten dokumentiert werden.
- BC/DR-Verpflichtungen des Cloud-Anbieters sollten in die Lieferanten-Risikobewertung einbezogen werden.
- Anbieter sollten die ISO-22301-Zertifizierung oder Äquivalent führen, sofern verfügbar.

---

## Redundanz von Informationsverarbeitungseinrichtungen

### Redundanzanforderungen nach Stufe

Informationsverarbeitungseinrichtungen sollten mit ausreichender Redundanz implementiert werden, um Verfügbarkeitsanforderungen zu erfüllen:

| Systemstufe | Mindestredundanz | Failover-Typ | Ziel-RTO |
|-------------|-----------------|--------------|----------|
| **Stufe 1 (Kritisch)** | Aktiv-Aktiv oder Aktiv-Passiv mit automatisiertem Failover | Automatisch | Minuten |
| **Stufe 2 (Hoch)** | Warm-Standby oder dokumentierter manueller Failover | Manuell mit Runbook | Stunden |
| **Stufe 3 (Mittel)** | Cold-Standby oder Wiederaufbau aus Backup | Wiederaufbau | Tage |
| **Stufe 4 (Niedrig)** | Backup-basierte Wiederherstellung | Wiederherstellen | Gemäss RTO |

**Redundanzarchitekturoptionen**:

- **Aktiv-Aktiv**: Mehrere Systeme bedienen gleichzeitig Traffic; Ausfall wird durch verbleibende Systeme behandelt.
- **Aktiv-Passiv**: Primärsystem bedient Traffic; Standby-System bereit zur sofortigen Aktivierung bei Ausfall.
- **Warm-Standby**: Standby-Umgebung teilweise bereitgestellt; erfordert Datensynchronisation, bevor sie betriebsbereit wird.
- **Cold-Standby**: Infrastruktur verfügbar, aber nicht bereitgestellt; erfordert Bereitstellung und Datenwiederherstellung.

### Single-Point-of-Failure (SPOF)-Analyse

Systemeigentümer sollten SPOF-Analysen für Stufe-1- und Stufe-2-Systeme durchführen, um Komponenten zu identifizieren, deren Ausfall vollständige Systemunavailability verursachen würde. Übliche SPOFs umfassen:

- Einzelner Server ohne Clustering oder Failover.
- Einzelner Netzwerkpfad ohne redundante Konnektivität.
- Einzelner Speicher-Controller, Netzteil oder USV.
- Einzelne Cloud-Verfügbarkeitszone oder Rechenzentrum.
- Einzelner DNS- oder Authentifizierungsserver.

**SPOF-Behebung**: Identifizierte SPOFs für Stufe-1-Systeme sollten innerhalb von 90 Tagen behoben werden oder eine dokumentierte Risikoakzeptanz vom ISB haben. Stufe-2-System-SPOFs sollten innerhalb von 180 Tagen behoben werden oder eine dokumentierte Risikoakzeptanz haben.

### Failover-Tests

Systeme mit Redundanz sollten ihre Failover-Mechanismen testen lassen:

| Systemstufe | Failover-Test-Häufigkeit |
|-------------|--------------------------|
| **Stufe 1 (Kritisch)** | Vierteljährlich (vollständiger Failover in Produktions- oder produktionsähnlicher Umgebung) |
| **Stufe 2 (Hoch)** | Halbjährlich (dokumentierter Failover-Test oder Tabletop-Übung) |
| **Stufe 3 (Mittel)** | Jährlich (Tabletop-Übung oder Verfahrensvalidierung) |

Jeder Failover-Test sollte dokumentieren: getestete Systeme, Failover-Auslösemechanismus, tatsächliche Failover-Zeit vs. RTO-Ziel, identifizierte Probleme und Abzeichnung.

**Failback-Tests**: Failover-Tests sollten auch den Failback-Prozess validieren (Rückkehr zur primären Infrastruktur nach der Wiederherstellung). Failback-Verfahren sollten dokumentiert und zusammen mit Failover getestet werden, um vollständige Wiederherstellungszyklusfähigkeit sicherzustellen.

**Reaktion auf fehlgeschlagenen Failover**: Tests, die die Unfähigkeit zur Erfüllung des RTO aufdecken, sollten sofortige Behebung und Risikobewertung gemäss der Eskalationstabelle in Backup-Tests und Verifizierung auslösen.

### Geografische und Netzwerkredundanz

**Geografische Redundanz**: Für Stufe-1-Systeme sollte Redundanz in ausreichender geografischer Entfernung implementiert werden, um gegen standortweite Katastrophen zu schützen:

| Entfernungsstufe | Trennung | Schutz gegen |
|------------------|----------|--------------|
| **Minimum** | Anderes Gebäude oder Campus | Lokale Vorfälle (Brand, Überschwemmung, Stromausfall) |
| **Empfohlen** | Andere Stadt oder Region (> 100 km) | Regionale Katastrophen |
| **Best Practice** | Andere geografische oder seismische Zone | Grossflächige Naturkatastrophen |

Cloud-spezifische Leitlinien: Multi-AZ-Deployment (Dutzende Kilometer Trennung) erfüllt die Mindeststufe. Multi-Region-Deployment (Hunderte bis Tausende Kilometer) erfüllt die empfohlene Stufe.

**Netzwerkredundanz**: Kritische Systeme sollten Netzwerkredundanz implementieren, einschliesslich doppelter ISPs oder Anbieter, redundanter Switches/Router und redundanter Firewalls, sofern die Infrastruktur der Organisation dies unterstützt.

**Kosten-Nutzen-Analyse**: Redundanzentscheidungen sollten die Kosten redundanter Infrastruktur gegen die Geschäftsauswirkungen verlängerter Ausfälle und regulatorischer Anforderungen abwägen. Für viele KMU bietet cloud-native Redundanz (Multi-AZ-Deployment) kostengünstige geografische Redundanz ohne Pflege separater physischer Infrastruktur.

**Bedingt**: Organisationen, die DORA oder NIS2 unterliegen, sollten geografische Redundanz für kritische Systeme implementieren, um operationale Resilienzanforderungen zu erfüllen.

---

## IKT-Kontinuitätsplanung

### Geschäftskontinuitätspläne

Die Organisation sollte dokumentierte Verfahren für die Reaktion auf einen störenden Vorfall und für die Fortführung oder Wiederherstellung ihrer Aktivitäten innerhalb vorbestimmter Zeitrahmen pflegen. Geschäftskontinuitätspläne sollten die Anforderungen derjenigen berücksichtigen, die sie verwenden werden.

**Geschäftskontinuitätspläne sollten abdecken**:

- Rollen und Verantwortlichkeiten für Personen und Teams mit Autorität während und nach einem Vorfall.
- Einen Prozess zur Aktivierung der Reaktion.
- Details zur Verwaltung der unmittelbaren Folgen eines störenden Vorfalls, unter gebührender Berücksichtigung des Wohlergehens der Personen.
- Strategische, taktische und operative Optionen für die Reaktion auf Störungen.
- Verhinderung weiterer Verluste oder Nichtverfügbarkeit priorisierter Aktivitäten.
- Wie und unter welchen Umständen die Organisation mit Mitarbeitenden und deren Angehörigen, wichtigen interessierten Parteien und Notkontakten kommunizieren wird.
- Wie die Organisation ihre priorisierten Aktivitäten innerhalb vorbestimmter Zeitrahmen fortführen oder wiederherstellen wird.
- Details zur Medienreaktion der Organisation nach einem Vorfall, einschliesslich Kommunikationsstrategie, bevorzugter Schnittstelle mit den Medien und Leitlinien für die Erstellung von Pressemitteilungen.
- Einen Prozess zur Beendigung nach Abschluss des Vorfalls.

**Jeder Plan sollte definieren**: Zweck und Umfang, Ziele, Aktivierungskriterien und -verfahren, Implementierungsverfahren, Rollen und Befugnisse, Kommunikationsanforderungen, interne und externe Abhängigkeiten, Ressourcenanforderungen sowie Informationsfluss und Dokumentationsprozesse.

### IKT-Wiederherstellungspläne

Für jedes Stufe-1- und Stufe-2-System sollte die Organisation IKT-Wiederherstellungspläne pflegen, die dokumentieren:

1. **Aktivierungskriterien** — Wann der Plan aktiviert werden soll (Katastrophen-Erklärungsprozess).
2. **Wiederherstellungsteam** — Rollen, Verantwortlichkeiten und Eskalationsverfahren.
3. **Notkontakte** — Wiederherstellungsteam, Lieferanten, Stakeholder.
4. **Wiederherstellungsverfahren** — Schritt-für-Schritt-Systemwiederherstellungsanweisungen in Prioritätsreihenfolge.
5. **Kommunikationsverfahren** — Interne und externe Kommunikationsvorlagen.
6. **Wiederherstellungsprioritäten** — Systemwiederherstellungsreihenfolge basierend auf Abhängigkeiten und Stufenklassifizierung.
7. **Validierungsverfahren** — Wie nach der Wiederherstellung überprüft wird, ob Systeme betriebsbereit sind.
8. **Rollback-Verfahren** — Massnahmen wenn Wiederherstellung fehlschlägt.

Wiederherstellungspläne sollten versionskontrolliert, jährlich überprüft und nach Testübungen, grösseren Vorfällen oder wesentlichen Systemänderungen aktualisiert werden.

### Katastrophen-Erklärungsprozess

Eine Katastrophe sollte erklärt werden, wenn:

- Ein Stufe-1-Systemausfall 50 % seines definierten RTO überschreitet.
- Mehrere Systeme gleichzeitig ausfallen.
- Ein verlängerter Infrastrukturausfall (Rechenzentrum, Cloud-Region, Netzwerk) bestätigt wird.
- Ein Cyber-Vorfall (Ransomware, Datenschutzverletzung) den Normalbetrieb verhindert.
- Physischer Standortverlust oder Unzugänglichkeit eintritt.

**Erklärungsautoritätshierarchie**: Bereitschaftsingenieur bewertet → eskaliert an IT-Betriebsmanager → ISB bewertet innerhalb von 30 Minuten → GF/Geschäftsleitung autorisiert Erklärung falls erforderlich → BC/DR-Pläne aktiviert und Wiederherstellungsteams benachrichtigt.

**Aktivierungsbenachrichtigung**: Vorab genehmigte Benachrichtigungsvorlagen sollten im BC/DR-Plan gepflegt werden. Benachrichtigung sollte gleichzeitig über primäre Kanäle (E-Mail, Kollaborationsplattform) und Backup-Kanäle (SMS, Telefon) ausgestellt werden.

**Vorfall-zu-Katastrophe-Eskalation**: Nicht jeder Vorfall ist eine Katastrophe. Die Incident-Management-Richtlinie (A.5.24–28) regelt die erste Vorfallsreaktion. Eskalation zur Katastrophen-Erklärung erfolgt, wenn die Vorfallsreaktion bestimmt, dass eine normale Wiederherstellung innerhalb des RTO nicht erreichbar ist.

### BC/DR-Testprogramm

Geschäftskontinuitätspläne und technische Wiederherstellungspläne sollten mindestens jährlich und bei wesentlichen Änderungen getestet werden.

**Testtypen**:

| Testtyp | Beschreibung | Häufigkeit |
|---------|--------------|------------|
| **Tabletop-Übung** | Diskussionsbasierter Durchgang eines Szenarios mit Schlüsselpersonal | Jährlich (alle kritischen Prozesse) |
| **Komponententest** | Einzelne Systemwiederherstellung testen (Backup-Wiederherstellung, Failover) | Vierteljährlich für Stufe 1; halbjährlich für Stufe 2 |
| **Vollständiger DR-Test** | Vollständiger Failover zum DR-Standort oder alternativer Umgebung | Jährlich für Stufe-1-Systeme |

**Jährlicher integrierter Test**: Mindestens ein jährlicher BC/DR-Test sollte Backup-Wiederherstellung, Redundanzaktivierung, Geschäftsprozessvalidierung und Kommunikationsverfahren zusammen üben, um end-to-end-Wiederherstellungsfähigkeit zu verifizieren.

**Testdokumentation**: Jeder Test sollte dokumentieren: Testdatum, Umfang, Ziele, Teilnehmer, Szenario, Ergebnisse (Erfolg/Teilweise/Misserfolg), tatsächliche vs. Ziel-RTO/RPO, identifizierte Probleme, Erkenntnisse, Massnahmen und Abzeichnung.

**Reaktion auf fehlgeschlagene Tests**: Tests, die die Unfähigkeit zur Erfüllung von RTO/RPO aufdecken, sollten sofortige Untersuchung, Gap-Behebungsplan, vorläufige Ausgleichskontrollen und Geschäftsleitungsbenachrichtigung für Stufe-1-Systeme auslösen.

**Bedingt**: Organisationen, die DORA unterliegen, sollten BC-Arrangements mindestens jährlich testen (Art. 11(9)) und IKT-Backup und -Wiederherstellung mindestens jährlich testen (Art. 12(6)).

### BC/DR-Schulung und -Bewusstsein

| Zielgruppe | Schulungsinhalt | Häufigkeit |
|------------|-----------------|------------|
| **Alle Mitarbeitenden** | BC/DR-Bewusstsein (individuelle Verantwortlichkeiten, Meldeverfahren, Kommunikationskanäle, Grundkonzepte) | Jährlich |
| **Wiederherstellungsteam-Mitglieder** | Rollenspezifische Schulung (Wiederherstellungsverfahren, Kommunikationsprotokolle, Tool-Nutzung) | Jährlich; neue Mitglieder innerhalb von 30 Tagen nach Zuweisung geschult |
| **Geschäftsleitung** | Krisenentscheidungsfindung, Katastrophen-Erklärungsprozess, Medienhandhabung | Jährlich (Tabletop-Übung) |

Post-Test-Schulung: BC/DR-Testergebnisse und Erkenntnisse sollten innerhalb von 30 Tagen nach jedem Test an alle Teilnehmer kommuniziert werden.

**Schulungsziele**: 100 % des Wiederherstellungsteams geschult; 95 % aller Mitarbeitenden haben BC/DR-Bewusstsein abgeschlossen.

### Krisenkommunikation

BC/DR-Pläne sollten Kommunikationsverfahren für Folgendes enthalten:

**Interne Kommunikation**:

- Aktivierungsbenachrichtigung innerhalb von 30 Minuten nach Katastrophen-Erklärung (wer benachrichtigt wird, über welche Kanäle).
- Statusaktualisierungen während der Wiederherstellung in definierten Abständen (stündlich für Stufe 1, alle 4 Stunden für Stufe 2).
- Entwarnung-Benachrichtigung, wenn die Wiederherstellung abgeschlossen und Systeme validiert sind.

**Externe Kommunikation**:

- Kundenbenachrichtigung (proaktiv für bekannte Ausfälle, die den Dienst betreffen).
- Lieferanten-/Partner-Koordination (falls für die Wiederherstellung benötigt).
- Regulatorische Benachrichtigung (falls erforderlich — z. B. Benachrichtigung bei Datenschutzverletzung gemäss nDSG Art. 24 oder DSGVO Art. 33).

**Kommunikationskanäle**: Primäre Kanäle (E-Mail, [Kollaborationsplattform]); Backup-Kanäle (SMS, Telefon) wenn primäre Kanäle nicht verfügbar sind. Kontaktlisten sollten gepflegt, offline zugänglich (gedruckt oder auf mobilen Geräten) und vierteljährlich überprüft werden.

### Wiederherstellungsverfahren

Die Organisation sollte dokumentierte Verfahren zur Wiederherstellung und Rückkehr von Geschäftsaktivitäten von vorübergehenden Massnahmen während eines Vorfalls zum normalen Geschäftsbetrieb pflegen.

**Wiederherstellungsvalidierungs-Checkliste**: Vor der Erklärung der Systemwiederherstellung und Rückkehr zum Normalbetrieb sollte Folgendes verifiziert werden:

- Datenintegrität bestätigt (Prüfsummen, Datensatzzählungen, Anwendungsebenen-Validierung).
- Alle abhängigen Systeme und Integrationen betriebsbereit.
- Benutzerzugang wiederhergestellt und getestet.
- Sicherheitskontrollen wieder aktiviert und verifiziert (EDR, Firewall-Regeln, Protokollierung).
- Performance innerhalb akzeptabler Parameter.
- Abzeichnung durch Systemeigentümer.

### Ransomware-Wiederherstellung

Angesichts der Prävalenz von Ransomware-Bedrohungen ergänzen die folgenden spezifischen Wiederherstellungsüberlegungen das allgemeine BC/DR-Framework:

**Sofortige Massnahmen bei Ransomware-Erkennung**:

1. Infizierte Systeme vom Netzwerk isolieren (nicht ausschalten — forensische Beweise erhalten).
2. Incident-Response-Team gemäss der Incident-Management-Richtlinie (A.5.24–28) aktivieren.
3. Backup-Integrität bewerten — verifizieren, dass Backup-Kopien nicht kompromittiert sind, bevor mit der Wiederherstellung begonnen wird.

**Wiederherstellungsüberlegungen**:

- Aus bekannt sauberen Backups wiederaufbauen, die als vor der Infektion datierend verifiziert sind.
- Die ausgenutzte Schwachstelle patchen, bevor Systeme in die Produktion zurückgestellt werden.
- Alle Anmeldedaten (Benutzer, Service-Account, Administrator) zurücksetzen, bevor der Zugang wiederhergestellt wird.
- Erweiterte Überwachung für 30–90 Tage nach der Wiederherstellung implementieren, um Persistenzmechanismen zu erkennen.

**Bedeutung unveränderlicher Backups**: WORM-Speicher, Object Lock oder Air-Gapped-Medien stellen sicher, dass mindestens ein Wiederherstellungspunkt immun gegen Ransomware-Verschlüsselung ist.

**Lösegeld-Zahlung**: Die Organisation sollte keine Lösegeldzahlungen ohne ausdrückliche Genehmigung der Geschäftsleitung und vorherige Rücksprache mit dem Rechtsbeistand und dem Cyber-Versicherungsanbieter (falls zutreffend) leisten.

### Vorfalls- und Geschäftskontinuitätsberichterstattung

Ein Incident-Management-Prozess sollte vorhanden sein und befolgt werden. Geschäftskontinuitätsvorfälle sollten zusätzlich:

- In einem Register erfasst und verfolgt werden.
- Dem Management-Review-Team gemeldet werden.
- Einer Post-Incident-Überprüfung zur Erfassung von Erkenntnissen unterzogen werden.

---

## Rollen und Verantwortlichkeiten

| Rolle | BC/DR-Verantwortlichkeiten |
|-------|---------------------------|
| **GF / Geschäftsleitung** | Letzte Verantwortung für Geschäftskontinuität; BC/DR-Strategie und Budget genehmigen; Katastrophen erklären, die Planaktivierung erfordern |
| **ISB** | BC/DR-Richtlinieneigentümer; Anforderungen und Risikoakzeptanzen genehmigen; ausreichende Ressourcen sicherstellen; BC/DR-Status vierteljährlich an Geschäftsleitung berichten |
| **BC/DR-Koordinator** | Tägliches BC/DR-Programmmanagement; BIA-Prozess koordinieren; Wiederherstellungspläne pflegen; Tests planen und erleichtern; Compliance mit Backup- und Redundanzanforderungen verfolgen; BC/DR-Schulungsprogramm verwalten; Änderungsauswirkungen auf BC/DR-Pläne bewerten |
| **Systemadministratoren / Cloud-Administratoren** | Backup-Lösungen implementieren und verwalten; Redundanz und Failover-Mechanismen konfigurieren; Backup-Jobs überwachen; an BC/DR-Tests teilnehmen; Wiederherstellungsdokumentation pflegen |
| **Systemeigentümer / Anwendungseigentümer** | RTO/RPO-Anforderungen definieren; Input für BIA bereitstellen; Systemwiederherstellungsprioritäten genehmigen; wiederhergestellte Systeme validieren; an BC/DR-Tests teilnehmen |
| **Alle Mitarbeitenden** | Geschäftskontinuitätsvorfälle melden; BC-Plänen bei Störungen folgen; an BC/DR-Sensibilisierungsschulungen teilnehmen |

---

## BC/DR-Metriken und Berichterstattung

Die folgenden Metriken sollten verfolgt werden, um die Effektivität des BC/DR-Programms zu messen:

| Nr. | Metrik | Ziel | Überwachung | Berichterstattung |
|-----|--------|------|-------------|-------------------|
| 1 | **Backup-Erfolgsrate** | ≥ 99 % Stufe 1; ≥ 98 % Stufe 2–3 | Täglich | Monatlich an ISB |
| 2 | **Wiederherstellungstest-Abschluss** | 100 % gemäss Zeitplan | Pro Test | Vierteljährlich |
| 3 | **RTO/RPO-Testergebnisse** | 100 % Stufe 1 im Ziel; ≥ 95 % Stufe 2 | Pro Test | Vierteljährlicher Trend |
| 4 | **Failover-Test-Abschluss** | 100 % gemäss Zeitplan | Pro Test | Vierteljährlich |
| 5 | **BC/DR-Plan-Aktualität** | 100 % im Jahresüberprüfungszyklus überprüft | Vierteljährlich | Vierteljährlich |
| 6 | **SPOF-Behebung** | ≥ 90 % behoben oder risikoakzeptiert innerhalb des Zeitrahmens | Vierteljährlich | Vierteljährlich |
| 7 | **Wiederherstellungsteam-Schulung** | 100 % geschult | Jährlich | Jährlich |

Metriken, die Ziele für zwei aufeinanderfolgende Berichtsperioden unterschreiten, sollten an den ISB eskaliert und bei der nächsten Managementüberprüfung gemeldet werden.

---

## Nachweise

Die folgenden Nachweise belegen die Einhaltung dieser Richtlinie:

| Nr. | Nachweis | Eigentümer | Häufigkeit |
|-----|----------|------------|------------|
| 1 | **Geschäftsauswirkungsanalyse** mit Systemkritikalitätsstufen, RPO/RTO und Abhängigkeitsmapping | BC/DR-Koordinator / ISB | *Jährliche Überprüfung; bei wesentlichen Änderungen aktualisiert; 5 Jahre aufbewahrt* |
| 2 | **Backup-Inventar** (gesicherte Systeme, Backup-Typ, Häufigkeit, Aufbewahrung, Offsite-Status) | Systemadministratoren | *Laufend gepflegt; vierteljährlich überprüft; 3 Jahre aufbewahrt* |
| 3 | **Backup-Überwachungsprotokolle und -berichte** (Erfolgs-/Misserfolgsraten, Fehlerbehebungsaufzeichnungen) | Systemadministratoren | *Wöchentliche Protokollprüfungen; monatliche Berichte an ISB; 12 Monate aufbewahrt* |
| 4 | **Backup-Wiederherstellungstestergebnisse** (Testdatum, Systeme, tatsächliche vs. Ziel-RTO/RPO, Datenintegritätsverifizierung) | BC/DR-Koordinator | *Gemäss Zeitplan (vierteljährlich bis jährlich nach Stufe); 3 Jahre aufbewahrt* |
| 5 | **SPOF-Analyse** für Stufe-1- und Stufe-2-Systeme mit Behebungsstatus | Systemeigentümer | *Jährliche Überprüfung; bei Infrastrukturänderungen aktualisiert; 3 Jahre aufbewahrt* |
| 6 | **Failover-Testergebnisse** (Failover-Zeit, Probleme, Abzeichnung) | BC/DR-Koordinator | *Gemäss Zeitplan (vierteljährlich bis jährlich nach Stufe); 3 Jahre aufbewahrt* |
| 7 | **BC/DR-Pläne** (Geschäftskontinuitätspläne und IKT-Wiederherstellungspläne, aktuelle Versionen) | BC/DR-Koordinator / ISB | *Jährliche Überprüfung; nach Tests und Vorfällen aktualisiert; aktuelle + 2 frühere Versionen aufbewahrt* |
| 8 | **BC/DR-Testaufzeichnungen** (Tabletop-Übungen, Komponententests, vollständige DR-Tests mit Szenarien und Ergebnissen) | BC/DR-Koordinator | *Jährlich mindestens; 3 Jahre aufbewahrt* |
| 9 | **Ausnahmeregister** (Systeme, die RPO/RTO nicht erfüllen, Risikoakzeptanzen, Ausgleichskontrollen) | ISB | *Pro Ereignis; vierteljährlich überprüft; 5 Jahre aufbewahrt* |
| 10 | **Krisenkommunikations-Kontaktlisten** (internes Team, externe Kontakte, Lieferantenkontakte, offline verfügbar) | BC/DR-Koordinator | *Vierteljährlich überprüft; bei Änderungen aktualisiert* |
| 11 | **BC/DR-Schulungsaufzeichnungen** (Schulungsabschluss des Wiederherstellungsteams, jährliche Sensibilisierungsabschlussraten) | BC/DR-Koordinator | *Jährlich; 3 Jahre aufbewahrt* |
| 12 | **BC/DR-Metrikberichte** (Backup-Erfolgsraten, Testabschluss, Plan-Aktualitätstrends) | BC/DR-Koordinator | *Monatlich an ISB; vierteljährliche Trendberichte; 3 Jahre aufbewahrt* |
| 13 | **Cloud-Anbieter-SLA und BC/DR-Fähigkeitsdokumentation** (SLA-Garantien, Modell der geteilten Verantwortung, BC/DR-Ausrichtungsverifizierung) | Systemeigentümer / Cloud-Administratoren | *Jährlich und bei Vertragsverlängerung überprüft; 3 Jahre aufbewahrt* |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheits-Management-Team sollte die Einhaltung dieser Richtlinie durch verschiedene Methoden verifizieren, einschliesslich, aber nicht beschränkt auf, Backup-Überwachungsberichte, Wiederherstellungstestaufzeichnungen, BC/DR-Testergebnisse, SPOF-Analyseberichte, interne und externe Audits sowie Feedback an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie (z. B. System aus Backup ausgeschlossen, Redundanz nicht implementiert, RPO/RTO nicht erfüllt) sollte vom Information Security Manager im Voraus genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum (maximal 12 Monate, verlängerbar). Ausnahmen sollten dem Management-Review-Team gemeldet werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstösst, kann disziplinarischen Massnahmen unterworfen werden, bis hin zur Kündigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollten Änderungen im Geschäftsbetrieb, Technologieinfrastruktur, regulatorischen Anforderungen, Erkenntnisse aus BC/DR-Tests und tatsächlichen Vorfällen, Audit-Befunden, neuen Bedrohungen (z. B. Ransomware, Lieferkettenstörungen), Umwelt-Bedrohungsbewertungen und Kapazitätsprognosen für Backup- und DR-Infrastruktur berücksichtigen.

Die Organisation verpflichtet sich zur Entwicklung und kontinuierlichen Verbesserung des Geschäftskontinuitätsprozesses, der Pläne und des Systems.

---

# Bereiche des ISO-27001-Standards, die abgedeckt werden

Richtlinie zur Geschäftskontinuität und Disaster Recovery — ISO-27001-Kontrollmapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Managementverantwortlichkeiten |
| Klausel 6.2 Informationssicherheitsziele | 5.29 Informationssicherheit bei Störungen |
| Klausel 7.3 Bewusstsein | **5.30 IKT-Bereitschaft für Geschäftskontinuität** |
| Klausel 8.1 Operationale Planung und Kontrolle | 5.36 Konformität mit Richtlinien, Regeln und Standards |
| | 6.3 Informationssicherheitsbewusstsein, Ausbildung und Schulung |
| | 6.4 Disziplinarischer Prozess |
| | **8.13 Informations-Backup** |
| | **8.14 Redundanz von Informationsverarbeitungseinrichtungen** |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizer nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen einschliesslich Verfügbarkeitsschutz und Datenwiederherstellungsfähigkeit |
| Schweizer DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (soweit anwendbar) | Art. 32(1)(c) — Fähigkeit, Verfügbarkeit und Zugang zu personenbezogenen Daten zeitnah wiederherzustellen |
| ISO/IEC 27001:2022 | Annex A Kontrollen 5.30 (IKT-Bereitschaft), 8.13 (Informations-Backup), 8.14 (Redundanz) |
| ISO/IEC 27002:2022 | Abschnitte 5.30, 8.13, 8.14 — Implementierungsleitfaden |
| ISO/IEC 22301 | Business-Continuity-Managementsysteme (informativer Verweis) |
| NIST SP 800-34 Rev 1 | Contingency Planning Guide (informativer Verweis) |
| CIS Controls v8 | Kontrolle 11 (Data Recovery) |
| DORA (bedingt) | Art. 11–12 — IKT-Geschäftskontinuität, Backup-Richtlinien, Disaster-Recovery-Pläne, jährliches Testen |
| NIS2 (bedingt) | Art. 21 — Geschäftskontinuität und Krisenmanagement, Backup-Management |
| FINMA (bedingt) | Geschäftskontinuitätsmanagement für Schweizer Finanzinstitute |

---

<!-- QA_VERIFIED: 2026-03-29 -->
