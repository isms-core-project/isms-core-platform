<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.30-8.13-14-DE:framework:POL:a.5.30-8.13-14 -->
**ISMS-POL-A.5.30-8.13-14 — Business-Continuity- & Notfallwiederherstellungs-Framework**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Business-Continuity- & Notfallwiederherstellungs-Framework |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.5.30-8.13-14 |
| **Erstellt von** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Festzulegen] |
| **Klassifizierung** | INTERN |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstversion für ISO 27001:2022 Erstzertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL)
- Technisch: IT-Betriebsleiter / BC/DR-Koordinator
- Compliance: Rechts-/Compliance-Beauftragter
- Letztverantwortung: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-IMP-A.5.30-8.13-14-S1-UG/TG (BIA und RPO/RTO-Prozess)
- ISMS-IMP-A.5.30-8.13-14-S2-UG/TG (Backup-Implementierung)
- ISMS-IMP-A.5.30-8.13-14-S3-UG/TG (Redundanzimplementierung)
- ISMS-IMP-A.5.30-8.13-14-S4-UG/TG (Wiederherstellungstestprozess)
- ISO/IEC 27001:2022 Massnahmen A.8.13, A.8.14, A.5.30
- ISMS-POL-A.5.19-23 (Lieferanten-/Cloud-Dienste – Lieferanten-BC/DR-Anforderungen)
- ISMS-POL-A.5.24 (Incident Management)
- ISMS-POL-A.8.6 (Kapazitätsmanagement)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] an Business-Continuity- und Notfallwiederherstellungs-Massnahmen (BC/DR) fest, um organisatorische Resilienz durch systematische Backup-, Redundanz- und IKT-Kontinuitätsfähigkeiten gemäss ISO/IEC 27001:2022 Massnahmen A.8.13, A.8.14 und A.5.30 sicherzustellen.

**Geltungsbereich**: Diese Richtlinie gilt für alle Informationswerte, IKT-Systeme und Geschäftsprozesse unabhängig vom Einsatzmodell (On-Premises, Cloud, Hybrid) oder der Technologieplattform.

**Zweck**: Definition der organisatorischen Anforderungen für die Implementierung und Governance von BC/DR-Massnahmen. Diese Richtlinie legt fest, WELCHE Wiederherstellungsfähigkeiten erforderlich sind und WER verantwortlich ist. Implementierungsverfahren (WIE) sind separat in ISMS-IMP-A.5.30-8.13-14 (UG/TG-Varianten) dokumentiert. Technische Standards und Konfigurationen werden bewusst ausserhalb dieser Richtlinie definiert, um technologische Flexibilität zu erhalten.

**Kombinierter Massnahmenansatz**: Diese drei Massnahmen werden als einheitliches BC/DR-Framework implementiert, da sie als integriertes Ökosystem zusammenwirken: Backup stellt die Datenwiederherstell-Fähigkeit bereit (A.8.13), Redundanz stellt die Systemverfügbarkeitsfähigkeit sicher (A.8.14) und die IKT-BC-Bereitschaft gewährleistet Vorbereitung und Governance (A.5.30). Eine getrennte Implementierung würde zu unverbundenen Strategien führen, bei denen Backup-Richtlinien die Redundanzarchitektur ignorieren und BC-Pläne die tatsächlichen technischen Fähigkeiten nicht widerspiegeln. Trotz einheitlicher Implementierung behält jede Massnahme separate Anforderungen für die Zwecke der Erklärung zur Anwendbarkeit (SoA).

**Kritisches Prinzip – „Ungetestete Wiederherstellung = Keine Wiederherstellung"**: Dieses Framework schreibt regelmässige Tests aller Wiederherstellungsfähigkeiten vor. Backup-Erfolge ohne Wiederherstellungstests, Redundanz ohne Failover-Tests und BC-Pläne ohne Szenariotests vermitteln falsches Vertrauen. Der evidenzbasierte Nachweis durch systematische Tests ist nicht verhandelbar.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen), einschliesslich Schweizer nDSG, EU DSGVO, ISO/IEC 27001:2022 sowie bedingte Anforderungen für DORA (Unveränderlichkeit, Offsite-Backup, geografische Redundanz), NIS2 (3-2-1-Regelkonformität, 24-Stunden-Vorfallmeldung) und branchenspezifische Vorschriften, sofern die Geschäftsaktivitäten von [Organisation] eine Anwendbarkeit begründen.

---

# Massnahmenausrichtung & Geltungsbereich

## ISO/IEC 27001:2022 Massnahmen A.8.13, A.8.14, A.5.30

**ISO/IEC 27001:2022 Annex A.8.13 – Informationssicherung**

> *Backup-Kopien von Informationen, Software und Systemen sollten gemäss einer vereinbarten themenspezifischen Richtlinie erstellt und regelmässig getestet werden.*

**Massnahmenziel**: Sicherstellen, dass Informationen, Software und Systeme im Falle von Verlust, Beschädigung, Korruption oder Nichtverfügbarkeit wiederhergestellt werden können.

**Zusammenfassung ISO/IEC 27002:2022 Leitlinien**:

- Backup-Kopien sollten gemäss einer definierten und dokumentierten Backup-Richtlinie erstellt werden
- Backups sollten alle wesentlichen Informationen, Software, System-Images und Konfigurationen umfassen
- Backups sollten regelmässig getestet werden, um sicherzustellen, dass sie erfolgreich wiederhergestellt werden können
- Backups sollten mit demselben Schutzniveau wie die Originaldaten gesichert werden
- Mehrere Generationen von Backups sollten entsprechend den Geschäftsanforderungen aufbewahrt werden
- Backups sollten an einem sicheren, separaten Ort (extern oder offline) gespeichert werden

**ISO/IEC 27001:2022 Annex A.8.14 – Redundanz informationsverarbeitender Einrichtungen**

> *Informationsverarbeitende Einrichtungen sollten mit ausreichender Redundanz implementiert werden, um die Verfügbarkeitsanforderungen zu erfüllen.*

**Massnahmenziel**: Sicherstellen der Verfügbarkeit informationsverarbeitender Einrichtungen gemäss den organisatorischen Anforderungen.

**Zusammenfassung ISO/IEC 27002:2022 Leitlinien**:

- Redundanz sollte für kritische informationsverarbeitende Einrichtungen implementiert werden
- Der Redundanzgrad wird durch Verfügbarkeitsanforderungen bestimmt
- Redundanz kann Hardware, Software, Netzwerk, Strom und Kühlung umfassen
- Geografische Redundanz sollte zum Schutz vor standortweiten Katastrophen in Betracht gezogen werden
- Failover-Mechanismen sollten implementiert und getestet werden

**ISO/IEC 27001:2022 Annex A.5.30 – IKT-Bereitschaft für Business Continuity**

> *Die IKT-Bereitschaft sollte auf der Grundlage der Ziele für die Business Continuity und der IKT-Kontinuitätsanforderungen geplant, implementiert, aufrechterhalten und getestet werden.*

**Massnahmenziel**: Sicherstellen der IKT-Bereitschaft für Geschäftsunterbrechungen durch systematische Planung, Implementierung und Tests der IKT-Kontinuität.

**Zusammenfassung ISO/IEC 27002:2022 Leitlinien**:

- Business Impact Analysis (BIA) sollte durchgeführt werden, um kritische IKT-Abhängigkeiten zu identifizieren
- IKT-Kontinuitätspläne sollten entwickelt und gepflegt werden
- RTO und RPO sollten für kritische Systeme festgelegt werden
- BC/DR-Tests sollten regelmässig durchgeführt werden
- IKT-Kontinuität sollte in den umfassenderen BC-Plan der Organisation integriert werden

## Geltungsbereich

**In den Geltungsbereich einbezogene Informationswerte**:

- Alle Datenbanken, Dateisysteme und strukturierten Datenspeicher
- Betriebssystemimages und Systemkonfigurationen
- Anwendungssoftware und Konfigurationsdateien
- Kryptografisches Material (Zertifikate, Schlüssel) mit dokumentierten Backup-Verfahren
- Dokumentenverwaltungssysteme und Kollaborationsplattformen
- Vertragliche Unterlagen, Finanzdaten und regulierte Datensätze

**In den Geltungsbereich einbezogene informationsverarbeitende Einrichtungen**:

- Server (physisch, virtuell, Container-basiert) und Speichersysteme
- Netzwerkinfrastruktur (Firewalls, Router, Switches) mit Konfigurationen
- Cloud-Workloads (IaaS, PaaS) und SaaS-Anwendungen mit wichtigen Geschäftsdaten
- Endgeräte-Systeme, auf denen kritische Geschäftsprozesse laufen

**In den Geltungsbereich einbezogene Geschäftsprozesse**:

- Alle durch Business Impact Analysis (BIA) als kritisch eingestuften Prozesse
- Prozesse zur Unterstützung von Kundenverpflichtungen (SLA-gebunden)
- Gesetzlich oder regulatorisch verankerte Abläufe
- Finanzielle Transaktionsverarbeitung und Reporting

**Einsatzmodelle**:

- **On-Premises**: Physische Server, virtualisierten Umgebungen und lokalen Rechenzentren
- **Cloud (IaaS/PaaS)**: Virtuelle Maschinen, Container-Orchestrierung und verwaltete Dienste
- **SaaS**: Drittanbieter-Anwendungen mit kritischen Geschäftsdaten
- **Hybrid**: Kombinationen aus On-Premises- und Cloud-Infrastruktur

**Geografischer Geltungsbereich**: Alle Standorte von [Organisation], Remote-Arbeitskräfte und Cloud-Regionen, in denen Geschäftsdaten verarbeitet oder gespeichert werden.

**Regulatorische Anwendbarkeit**:

| Regulierung | Anwendbarkeit | BC/DR-Anforderungen |
|------------|--------------|---------------------|
| **Schweizer nDSG** | Obligatorisch für alle | Art. 8: Geeignete Schutzmassnahmen einschliesslich Backup und Verfügbarkeit |
| **EU DSGVO** | Wenn EU-Personendaten verarbeitet werden | Art. 32: Belastbarkeit, Wiederherstellungsfähigkeit nach Zwischenfällen |
| **ISO 27001:2022** | Zertifizierungsanforderung | A.8.13 (Backup), A.8.14 (Redundanz), A.5.30 (IKT-BC) |
| **DORA** | Wenn im EU-Finanzdienstleistungssektor tätig | Art. 12: Backup-Anforderungen inkl. Unveränderlichkeit und Offsite |
| **NIS2** | Wenn als kritische/wesentliche Einheit eingestuft | Art. 21: Backup-Management, BC und Krisenmanagement |
| **PCI DSS v4.0.1** | Wenn Kartendaten verarbeitet werden | Anf. 12.10: BC/DR-Anforderungen für Karteninhaberumgebungen |
| **FINMA** | Wenn schweizerische Finanzdienstleistung | Risikobasierte Anforderungen für Betriebskontinuität |

---

# Informationssicherung (A.8.13)

[Organisation] implementiert umfassende Backup-Schutzkontrollen für alle Informationswerte, die Backup-Schutz erfordern.

## Backup-Richtlinienrahmen

### Kernprinzipien der Backup-Sicherheit

**Prinzip 1 – Backup-Vollständigkeit**: Alle kritischen Informationswerte müssen in den definierten Backup-Geltungsbereich einbezogen werden. Nicht-kritische Systeme unterliegen risikobasierter Backup-Planung.

**Prinzip 2 – Backup-Integrität**: Backups müssen regelmässig auf Vollständigkeit und Wiederherstellbarkeit geprüft werden. Erfolgreiche Backup-Abschlüsse ohne Wiederherstellungstest bieten keine echte Datenschutzgarantie.

**Prinzip 3 – Backup-Sicherheit**: Backups müssen mit demselben Schutzniveau wie die Originaldaten gesichert werden, einschliesslich Verschlüsselung, Zugangskontrolle und physischer Sicherheit.

**Prinzip 4 – Backup-Aufbewahrung**: Backup-Aufbewahrungszeiträume müssen auf geschäftlichen, regulatorischen und rechtlichen Anforderungen basieren. Aufbewahrungsrichtlinien müssen dokumentiert und konsistent durchgesetzt werden.

**Prinzip 5 – Backup-Portabilität**: Backups müssen auf alternativen Plattformen (physisch, virtuell, Cloud) wiederherstellbar sein. Anbieterbindung bei Backup-Lösungen sollte durch portable Formate und dokumentierte Verfahren zur Plattformmigration minimiert werden.

**Prinzip 6 – Backup-Überwachung**: Backup-Vorgänge müssen kontinuierlich überwacht werden. Backup-Fehler bei kritischen Systemen erfordern sofortige Untersuchung und Behebung.

### Backup-Geltungsbereichsanforderungen

**Systeme und Daten mit Backup-Pflicht**:

| Kategorie | Backup-Anforderung | Begründung |
|-----------|-------------------|------------|
| **Kritische Geschäftsdaten** | Obligatorisches Backup | Datenverlust würde den Betrieb erheblich beeinträchtigen |
| **Produktionssysteme** | Obligatorisches Backup (Daten + Konfiguration) | Erforderlich für Business Continuity |
| **Kritische Infrastrukturkonfigurationen** | Obligatorisches Backup | Erforderlich für Infrastruktur-Wiederherstellung |
| **Wichtige Geschäftsdaten** | Obligatorisches Backup | Datenverlust würde den Betrieb mässig beeinträchtigen |
| **Entwicklungs-/Testsysteme** | Risikobasiertes Backup | Backup, wenn Wiederherstellungskosten die Backup-Kosten übersteigen |
| **Ephemere Daten** | Kein Backup erforderlich | Daten absichtlich temporär (Caches, Logs mit Aufbewahrungsfrist) |
| **Unkritische Systeme** | Risikobasiertes Backup | Backup, wenn Wiederherstellungszeit nicht akzeptabel ist |

**Bestimmung des Backup-Geltungsbereichs**: Systemeigentümer legen in Abstimmung mit dem BC/DR-Koordinator die Backup-Anforderungen auf Basis folgender Kriterien fest:

- Ergebnisse der Business Impact Analysis (BIA)
- Datenkritikalitätsklassifizierung (gemäss ISMS-POL-A.5.12)
- Regulatorische Aufbewahrungsanforderungen
- Recovery Time Objectives (RTO) des Systems
- Analyse Wiederaufbaukomplexität versus Backup-Kosten

### Backup-Zeitplanungsanforderungen

**Backup-Häufigkeit nach Systemkritikalität**:

| System-Tier | Backup-Häufigkeit | RPO-Ziel | Begründung |
|-------------|-------------------|----------|------------|
| **Tier 1 (Kritisch)** | Kontinuierlich oder stündlich | ≤ 1 Stunde | Minimaler Datenverlust akzeptabel |
| **Tier 2 (Hoch)** | Alle 4–6 Stunden | ≤ 6 Stunden | Begrenzter Datenverlust akzeptabel |
| **Tier 3 (Mittel)** | Täglich | ≤ 24 Stunden | Täglicher Datenverlust akzeptabel |
| **Tier 4 (Niedrig)** | Wöchentlich oder bei Änderungen | ≤ 7 Tage | Wöchentlicher Datenverlust akzeptabel |

**Backup-Fenster**: Backups müssen innerhalb definierter Wartungsfenster abgeschlossen sein. Übersteigt die Backup-Dauer das verfügbare Fenster, müssen inkrementelle/differentielle Strategien oder kontinuierlicher Datenschutz implementiert werden.

### RPO-Anforderungen nach Kritikalität

**Recovery Point Objective (RPO) Framework**:

Das RPO definiert das maximal akzeptable Alter wiederherstellbarer Daten. Das RPO bestimmt die Anforderungen an die Backup-Häufigkeit.

| Systemkritikalität | Maximales RPO | Backup-Strategie | Beispieltechnologien |
|-------------------|---------------|------------------|----------------------|
| **Tier 1 (Kritisch)** | 1 Stunde oder weniger | Kontinuierliche Replikation oder stündliche Backups | CDP, Echtzeit-Replikation, stündliche Snapshots |
| **Tier 2 (Hoch)** | 4–6 Stunden | Mehrmals täglich | 4× täglich, regelmässige Snapshots |
| **Tier 3 (Mittel)** | 24 Stunden | Tägliche Backups | Nächtlich voll oder inkrementell |
| **Tier 4 (Niedrig)** | 7 Tage | Wöchentliche Backups | Wöchentliche Vollbackups |

**RPO-Berechnung**: Systemeigentümer müssen RPO-Anforderungen dokumentieren auf Basis von:

- Maximal akzeptablem Datenverlust in Zeiteinheiten (Stunden/Tage)
- Geschäftlichen Auswirkungen des Verlusts von X Stunden Transaktionen
- Regulatorischen Anforderungen zur Datenrekonstruktion
- Kosten der Backup-Infrastruktur gegenüber Kosten des Datenverlusts

**RPO-Ausnahmen**: Systeme, die definierte RPOs nicht einhalten können, folgen dem Ausnahmeverwaltungsprozess (Abschnitt 3.2).

### Backup-Technologieanforderungen

**Backup-Typen**:

| Backup-Typ | Beschreibung | Anwendungsfall | Vorteile | Nachteile |
|-----------|-------------|----------------|---------|----------|
| **Vollbackup** | Vollständige Kopie aller Daten | Basis, wöchentlich/monatlich | Einfachste Wiederherstellung | Zeit-/speicherintensiv |
| **Inkrementell** | Geänderte Daten seit letztem Backup (beliebiger Typ) | Tägliche Backups | Schnell, effizienter Speicher | Langsamere Wiederherstellung (alle Inkremente erforderlich) |
| **Differentiell** | Geänderte Daten seit letztem Vollbackup | Tägliche Backups | Schnellere Wiederherstellung als inkrementell | Mehr Speicher als inkrementell |
| **Snapshot** | Zeitpunktgenaue Kopie (Speicherebene) | Häufige Backups, VMs | Sehr schnell, platzsparend | Speicherabhängig, nicht portabel |
| **Kontinuierlicher Datenschutz (CDP)** | Echtzeit- oder Nahezu-Echtzeit-Replikation | Kritische Systeme (RPO < 1 Stunde) | Minimaler Datenverlust | Komplex, kostspielig |

**Auswahl der Backup-Strategie**: Systemeigentümer müssen geeignete Backup-Technologien auf Basis folgender Kriterien wählen:

- RPO- und RTO-Anforderungen
- Systemarchitektur (physisch, virtuell, Cloud, Datenbank)
- Änderungsrate der Daten (tägliches Datenänderungsvolumen)
- Verfügbares Backup-Fenster
- Speicherkapazität und Kostenbeschränkungen

**Backup-Aufbewahrungsanforderungen**:

Backups müssen gemäss folgenden Mindestaufbewahrungsfristen aufbewahrt werden:

| Backup-Typ | Mindestaufbewahrung | Regulatorische Hinweise |
|-----------|---------------------|------------------------|
| **Tägliche Backups** | 30 Tage | Die meisten Vorschriften erfordern 30-Tage-Wiederherstellungsfähigkeit |
| **Wöchentliche Backups** | 90 Tage | Quartalsweise Compliance- und Auditanforderungen |
| **Monatliche Backups** | 12 Monate | Jährliche Compliance-Überprüfung und historische Analyse |
| **Jährliche Backups** | 7 Jahre (oder gemäss Vorschrift) | Finanzdaten, Steuer-Compliance, Legal Hold |

**Erweiterte Aufbewahrung**: Zusätzliche Aufbewahrungsanforderungen können gelten aufgrund von:

- Regulatorischen Anforderungen (DSGVO, FINMA, PCI DSS v4.0.1, Steuerrecht)
- Legal-Hold-Anfragen
- Vertraglichen Verpflichtungen
- Geschäftsanforderungen (historische Analysen, Compliance-Audits)

**Ausnahmen bei der Aufbewahrungsrichtlinie**: Kürzere Aufbewahrungsfristen erfordern ISB-Genehmigung und dokumentierte Risikoakzeptanz.

### 3-2-1-1-0-Backup-Regel (Branchenbest Practice)

**Definition der 3-2-1-1-0-Regel**:

| Element | Anforderung | Begründung |
|---------|------------|------------|
| **3 Kopien** | Original + 2 Backup-Kopien | Schutz vor einem Single Point of Failure |
| **2 Medientypen** | Verschiedene Speichertechnologien | Schutz vor medienspezifischen Ausfällen |
| **1 Offsite-Kopie** | Geografisch getrennter Standort | Schutz vor standortbezogenen Katastrophen |
| **1 unveränderliche/Air-Gapped Kopie** | Write-Once-Read-Many oder offline | Schutz vor Ransomware und Insider-Bedrohungen |
| **0 Fehler** | Verifizierte Backup-Integrität | Nur verifizierte Backups sind zuverlässig |

**Implementierung für kritische Systeme** (Tier 1):

Kritische Systeme (Tier 1) müssen die 3-2-1-1-0-Regel implementieren:

- **3 Kopien**: Produktionsdaten + On-Premises-Backup + Cloud-/Offsite-Backup
- **2 Medientypen**: Festplattenbasiert + Band/Objektspeicher oder On-Premises + Cloud
- **1 Offsite**: Geografische Trennung (anderes Rechenzentrum, Region oder Cloud)
- **1 unveränderlich**: WORM-Speicher, Object Lock (S3) oder Air-Gapped-Band
- **0 Fehler**: Automatisierte Backup-Verifizierung, regelmässige Wiederherstellungstests

**Implementierung für hohe/mittlere Systeme** (Tier 2–3):

Hohe und mittlere Systeme sollten mindestens die 3-2-1-Regel implementieren:

- **3 Kopien**: Produktion + primäres Backup + sekundäres Backup
- **2 Medientypen**: Verschiedene Technologien (Disk + Cloud, Disk + Band)
- **1 Offsite**: Cloud-Backup oder entferntes Rechenzentrum

**Begründung**: 3-2-1-1-0 bietet Defense-in-Depth gegen mehrere Ausfallszenarien: Hardwareausfall, Ransomware, Naturkatastrophen, menschliche Fehler und Datenbeschädigung.

### Offsite- und Unveränderlichkeitsanforderungen

**Offsite-Backup-Anforderungen**:

| System-Tier | Offsite-Anforderung | Geografische Trennung | Replikationshäufigkeit |
|-------------|--------------------|-----------------------|------------------------|
| **Tier 1 (Kritisch)** | Obligatorisch | Mindestens 100 km oder andere Region | Kontinuierlich oder stündlich |
| **Tier 2 (Hoch)** | Obligatorisch | Mindestens 50 km oder andere Verfügbarkeitszone | Täglich |
| **Tier 3 (Mittel)** | Empfohlen | Anderer physischer Standort | Wöchentlich |
| **Tier 4 (Niedrig)** | Risikobasiert | Cloud-Speicher akzeptabel | Bei Änderungen |

**Kriterien für geografische Trennung**:

- **Anderes Gebäude**: Schutz vor Gebäudebrand, Überschwemmung, Stromausfall
- **Anderes Rechenzentrum**: Schutz vor rechenzentrumsweiten Katastrophen
- **Andere Stadt/Region**: Schutz vor regionalen Katastrophen (Erdbeben, Sturm)
- **Anderes Land/Jurisdiktion**: Schutz vor geopolitischen Risiken (für multinationale Betriebe)

**DORA-Compliance**: EU-Finanzeinheiten, die DORA unterliegen, müssen Offsite-Backups mit ausreichender geografischer Entfernung implementieren, um regionale Katastrophen abzusichern (Art. 12(4)).

**Unveränderlichkeits-Anforderungen**:

**Kritische Systeme** (Tier 1):

- Müssen unveränderliche Backups mittels WORM (Write-Once-Read-Many) Technologie implementieren
- Die Unveränderlichkeitsdauer muss mit der Aufbewahrungsrichtlinie übereinstimmen (mindestens 30 Tage)
- Unveränderliche Backups müssen von der Standard-Backup-Infrastruktur getrennt sein
- Technologien: Objektspeicher mit Object Lock (AWS S3 Object Lock, Azure Immutable Blob), Bandbibliotheken mit WORM-Medien, dedizierte unveränderliche Backup-Appliances

**Offline/Air-Gapped-Backup**: Bei kritischen Systemen sollte mindestens eine Backup-Kopie:

- Physisch vom Netzwerk getrennt sein (Air-Gapped-Band, Wechselmedien)
- An einem sicheren Offsite-Standort aufbewahrt werden
- Regelmässig rotiert werden (wöchentlich/monatlich)

**Begründung**: Unveränderliche und Air-Gapped-Backups bieten die letzte Verteidigungslinie gegen Ransomware-Angriffe, die Backup-Repositorys zu verschlüsseln oder zu löschen versuchen.

**Cloud-zu-On-Premises-Backup**: Für Cloud-Workloads sollten Backup-Kopien:

- In portable Formate exportierbar sein (Anbieterbindung vermeiden)
- Auf lokaler Infrastruktur wiederhergestellt werden können
- Einen dokumentierten Wiederherstellungsprozess für Cloud-Repatriierungsszenarien haben

### Backup-Portabilitätsanforderungen

**Massnahmen zur Minderung von Anbieterbindung**:

Um Flexibilität bei der Wiederherstellung sicherzustellen und die Abhängigkeit von bestimmten Backup-Anbietern oder Cloud-Providern zu vermeiden, müssen Backup-Implementierungen sicherstellen:

**Portabilität des Backup-Formats**:

- Backups müssen soweit möglich in branchenübliche Formate exportierbar sein
- Proprietäre Formate müssen dokumentierte Konvertierungsverfahren beinhalten
- Cloud-Backups müssen ohne anbieterspezifische Tools exportierbar sein

**Wiederherstellungsplattform-Unabhängigkeit**:

- Backups müssen auf verschiedenen Plattformen wiederherstellbar sein (physisch, virtuell, Cloud)
- Cloud-Backups müssen auf lokaler Infrastruktur wiederhergestellt werden können
- On-Premises-Backups müssen auf Cloud-Infrastruktur portierbar sein (On-Premises-zu-Cloud-Wiederherstellung)
- Backup-Lösungen müssen Export-/Migrationsverfahren dokumentieren
- Wiederherstellungsverfahren müssen Provider-Exit-Szenarien adressieren

**Begründung**: Anbieterbindung vermeiden, flexible DR-Strategien ermöglichen, Cloud-Repatriierungsszenarien unterstützen, Wiederherstellungsoptionen bei längeren Cloud-Ausfällen aufrechterhalten.

Diese Anforderung ist für Cloud-Unabhängigkeit kritisch und wird in Lieferantenvereinbarungen referenziert (ISMS-POL-A.5.19-23-S2 Abschnitt 8: Datenrückgabe und -vernichtung).

### Backup-Testanforderungen

**Wiederherstellungstest** (alle Backup-Tiers):

| System-Tier | Häufigkeit Wiederherstellungstest | Testumfang |
|-------------|----------------------------------|------------|
| **Tier 1** | Mindestens vierteljährlich | Vollständige Systemwiederherstellung in alternativer Umgebung |
| **Tier 2** | Mindestens halbjährlich | Repräsentative Datensätze, jährlich vollständiges System |
| **Tier 3** | Mindestens jährlich | Stichprobenweise Wiederherstellungsverifikation |
| **Tier 4** | Bei wesentlichen Änderungen | Stichprobenwiederherstellung oder Risikoakzeptanz |

**Anforderungen an die Testdokumentation**:

Jeder Backup-Wiederherstellungstest muss mit einer standardisierten Vorlage dokumentiert werden, einschliesslich:

1. **Test-Metadaten**: Test-ID, Datum, Typ (voll/teilweise), getestete Systeme, Testumgebung, Teilnehmer
2. **Vor-Test-Zustand**: Systeme im Geltungsbereich, Backup-Quelle (Datum/Ort), erwartetes RTO/RPO
3. **Testdurchführung**: Schrittweise Aufzeichnung der Wiederherstellungsaktionen, Zeitstempel, verwendete Befehle/Verfahren
4. **Ergebnisvalidierung**:
   - Datenintegritätsprüfung (Prüfsummen, Datensatzanzahl, Datenstichprobenprüfung)
   - Systemfunktionalitätsvalidierung (Anwendungsstart, Benutzerzugriff, Geschäftsprozesstest)
   - Leistungsvalidierung (erfüllt Produktionsanforderungen)
5. **Metriken**: Tatsächliche Wiederherstellungsdauer, wiederhergestellte Datenmenge (TB/GB), RTO-Abweichung (tatsächlich vs. Ziel)
6. **Beweisartefakte**: Screenshots des wiederhergestellten Systems, Validierungsberichte, Logauszüge mit Erfolgsnachweis
7. **Fehlerprotokoll**: Aufgetretene Probleme, angewandte Umgehungslösungen, Ursache falls identifiziert
8. **Abzeichnung**: Genehmigung durch BC/DR-Koordinator, Bestätigung der Funktionalität durch Systemeigentümer

**Standards für Testdokumentation**:
- Standardisierte Vorlage in ISMS-IMP-A.5.30-8.13-14-S4 (Wiederherstellungstestprozess) gepflegt
- Testdokumentation muss in [zentralem Repository/SharePoint/ISMS-Tool] gespeichert werden
- Mindestaufbewahrung: 3 Jahre oder gemäss regulatorischer Anforderung
- Testergebnisse in Arbeitsbuch 4 (BC/DR-Testergebnisse) referenziert

**Kritisches Prinzip**: Backup-Erfolgsmetriken (Backup erfolgreich abgeschlossen) validieren KEINE Wiederherstellungsfähigkeit. Nur Wiederherstellungstests validieren die Wiederherstellungsfähigkeit.

**Reaktion auf fehlgeschlagene Tests**: Backup-Tests, bei denen Wiederherstellungsfehler aufgedeckt werden, lösen folgendes aus:

- Sofortige Ursachenanalyse
- Behebung der identifizierten Probleme
- Wiederholungstest innerhalb von 30 Tagen
- Incident-Reporting bei kritischen Systemen

**DORA-Compliance**: Dem DORA unterliegende Finanzeinheiten müssen die Backup-Wiederherstellung mindestens jährlich testen (Art. 12(6)).

### Backup-Überwachungsanforderungen

Backup-Vorgänge müssen überwacht werden:

| Überwachungselement | Anforderung | Alarmschwelle |
|--------------------|-------------|---------------|
| **Backup-Erfolg/-Fehler** | Echtzeit-Überwachung | Sofortiger Alarm bei Fehler |
| **Backup-Dauer** | Trendanalyse | Alarm, wenn Dauer das Fenster überschreitet |
| **Backup-Grösse** | Trendanalyse | Alarm bei unerwartetem Wachstum/Rückgang |
| **Repository-Kapazität** | Kapazitätsüberwachung | Alarm bei 75 % Auslastung |
| **Aufbewahrungskonformität** | Automatisierte Validierung | Alarm bei Verletzung der Aufbewahrungsrichtlinie |

**Alarmierungsanforderungen**:

| Auslöser | Schwere | Benachrichtigung an |
|----------|---------|---------------------|
| Backup-Fehler kritisches System | Hoch | BC/DR-Koordinator + Systemeigentümer |
| Mehrfache aufeinanderfolgende Backup-Fehler | Hoch | BC/DR-Koordinator + ISB |
| Backup-Speicherkapazitätsschwelle (80 %) | Mittel | Backup-Administrator |
| Offsite-Replikationsfehler | Hoch | BC/DR-Koordinator |
| Backup-Integritätsverifizierungsfehler | Hoch | BC/DR-Koordinator + Systemeigentümer |

**Reporting**: Monatliche Backup-Statusberichte werden dem ISB bereitgestellt, einschliesslich:

- Backup-Abdeckungsgrad (gesicherte Systeme gegenüber Gesamtzahl)
- Backup-Erfolgsquote nach Systemkritikalität
- Status der Testdurchführung
- Offene Probleme und Behebungszeitplan

Überwachungsintegration: Backup-Alarme müssen in die organisatorische Überwachungsplattform integriert werden (ISMS-POL-A.8.16 Überwachungsaktivitäten).

### Wiederherstellungsverfahren

Wiederherstellungsverfahren müssen für jedes gesicherte System dokumentiert werden, einschliesslich:

- Schrittweiser Wiederherstellungsprozess
- Erforderliche Zugangsdaten und Genehmigung
- Schätzung der Wiederherstellungszeit (RTO)
- Validierungsschritte für die Wiederherstellung
- Bekannte Probleme und Umgehungslösungen
- Kontaktinformationen für Eskalation

Wiederherstellungsverfahren müssen bei Wiederherstellungsübungen getestet und anhand der Testergebnisse aktualisiert werden.

**Cloud-Backup-Überlegungen**:

**Backup durch Cloud-Dienstanbieter**:

- Das „Modell der geteilten Verantwortung" des Anbieters verstehen
- Dokumentieren, welche Backups in der Verantwortung des Anbieters und welche in der Kundenverpflichtung liegen
- Kundenseitige Backups implementieren, wenn der Anbieter keine RPO-Anforderungen garantiert

**Backup von SaaS-Anwendungen**:

- Backup- und Aufbewahrungsfähigkeiten des SaaS-Anbieters bewerten
- Backup-Lösung für SaaS von Drittanbietern implementieren, wenn Anbieterfähigkeiten unzureichend sind
- SaaS-Datenexport- und -importverfahren testen

**Cloud-Backup-Portabilität**:

- Backup-Formate sollten eine Wiederherstellung beim alternativen Cloud-Anbieter oder On-Premises ermöglichen
- Wiederherstellungsverfahren für Cloud-zu-Cloud- und Cloud-zu-On-Premises-Szenarien dokumentieren
- Backup-Lösungen vermeiden, die Anbieterbindung erzeugen

**Lieferantenanforderungen**: Cloud-Backup-Anbieter müssen die Anforderungen gemäss ISMS-POL-A.5.19-23 (Lieferanten-/Cloud-Dienste) erfüllen, einschliesslich:

- Einstufung als Level-1-Lieferant (kritisch)
- Sicherheitsbewertung und Due Diligence
- Vertragliche Zusagen zu Verfügbarkeit, Datenschutz und Vorfallbenachrichtigung
- Auditrechte oder Drittpartei-Attestierung (SOC 2 Typ II, ISO 27001)

---

# Redundanz informationsverarbeitender Einrichtungen (A.8.14)

[Organisation] implementiert Redundanz für kritische informationsverarbeitende Einrichtungen, um Verfügbarkeitsanforderungen zu erfüllen und Single Points of Failure zu minimieren.

## Redundanzanforderungen nach Systemkritikalität

**Bestimmung des Redundanzgrades**:

| Systemkritikalität | Maximales RTO | Mindest-Redundanzanforderung |
|-------------------|---------------|------------------------------|
| **Kritisch** | ≤ 4 Stunden | Aktiv-Aktiv oder Aktiv-Passiv mit automatischem Failover |
| **Hoch** | ≤ 24 Stunden | Warm-Standby oder dokumentierter Cold-Standby mit getesteter Wiederherstellung |
| **Mittel** | ≤ 72 Stunden | Cold-Standby oder dokumentierte Neuaufbauverfahren |
| **Niedrig** | > 72 Stunden | Backup-basierte Wiederherstellung akzeptabel |

**Redundanzarchitekturoptionen**:

| Architektur | Beschreibung | Typisches RTO | Anwendungsfall |
|------------|-------------|---------------|----------------|
| **Aktiv-Aktiv** | Mehrere Systeme verarbeiten gleichzeitig Traffic | Minuten | Kritische Systeme mit kontinuierlicher Verfügbarkeitsanforderung |
| **Aktiv-Passiv** | Standby-System bereit für sofortigen Failover | Minuten bis Stunden | Kritische Systeme mit tolerierbarer kurzer Unterbrechung |
| **Warm-Standby** | Standby-Umgebung teilweise bereitgestellt | Stunden | Hochprioritäre Systeme mit moderatem RTO |
| **Cold-Standby** | Infrastruktur verfügbar, aber nicht bereitgestellt | Tage | Wichtige Systeme mit längerem akzeptablem RTO |

## Single Point of Failure (SPOF) Analyse

**SPOF-Identifikationsprozess**:

Systemeigentümer müssen für kritische und hochprioritäre Systeme eine SPOF-Analyse durchführen, um Komponenten zu identifizieren, deren Ausfall einen vollständigen Systemausfall verursachen würde:

**Beispiele für Infrastruktur-SPOFs**:

- Einzelner Server (kein Clustering oder Failover)
- Einzelner Netzwerkpfad (keine redundante Konnektivität)
- Einzelne Stromversorgung oder USV
- Einzelner Speicher-Controller
- Einzelne Verfügbarkeitszone oder Rechenzentrum
- Einzelner DNS-Server
- Einzelner Authentifizierungsserver

**SPOF-Analysedokumentation**:

- Komponenteninventar (Server, Netzwerk, Speicher, Strom, Kühlung)
- Abhängigkeitsmapping (was hängt wovon ab)
- SPOF-Identifikation (Komponenten ohne Redundanz)
- Auswirkungsbeurteilung (was fällt aus, wenn die Komponente ausfällt)
- Behebungsplan (wie SPOF eliminiert oder Risiko akzeptiert wird)

**SPOF-Behebungspriorität**:

| SPOF-Risikograd | Behebungsanforderung | Zeitrahmen |
|----------------|---------------------|------------|
| **SPOF kritisches System** | Obligatorische Behebung | 90 Tage oder Risikoakzeptanz |
| **SPOF hohes System** | Empfohlene Behebung | 180 Tage oder Risikoakzeptanz |
| **SPOF mittleres System** | Risikobasierte Entscheidung | Risikobewertung erforderlich |

**SPOF-Ausnahmen**: Akzeptierte SPOFs müssen im Ausnahmeregister mit Risikoakzeptanz durch den ISB dokumentiert werden.

## Failover- und Switchover-Anforderungen

**Failover-Mechanismen**:

| System-Tier | Failover-Typ | Wiederherstellungsmassnahme | RTO-Auswirkung |
|-------------|-------------|---------------------------|----------------|
| **Tier 1 (Kritisch)** | Automatischer Failover | System wechselt automatisch auf Standby | Minuten |
| **Tier 2 (Hoch)** | Manueller Failover mit Runbook | Operator führt dokumentiertes Verfahren aus | Stunden |
| **Tier 3 (Mittel)** | Neuaufbau oder Wiederherstellung | Neues System bereitstellen oder aus Backup wiederherstellen | Tage |

**Failover-Testanforderungen**:

Kritische und hochprioritäre Systeme mit Redundanz müssen Failover-Mechanismen testen:

| System-Tier | Häufigkeit Failover-Test | Testumfang |
|-------------|--------------------------|------------|
| **Tier 1 (Kritisch)** | Vierteljährlich | Vollständiger Failover in produktions- oder produktionsähnlicher Umgebung |
| **Tier 2 (Hoch)** | Halbjährlich | Dokumentierter Failover-Test oder Tabletop-Übung |
| **Tier 3 (Mittel)** | Jährlich | Tabletop-Übung oder Validierung dokumentierter Verfahren |

**Failover-Testdokumentation**:

- Testdatum und Umfang
- Getestete Systeme
- Failover-Auslösemechanismus (manuell oder automatisch)
- Tatsächliche Failover-Zeit gegenüber RTO-Ziel
- Identifizierte Probleme und Behebung
- Nachweis erfolgreichen Failovers

**Reaktion auf fehlgeschlagenen Failover**: Failover-Tests, bei denen die Unfähigkeit, das RTO einzuhalten, aufgedeckt wird, lösen sofortige Behebung und Risikobewertung aus.

## Geografische Redundanz

**Kritische Systeme**: Kritische Systeme sollten Redundanz mit ausreichendem Abstand implementieren, um Schutz gegen:

- Standortweite Katastrophen (Brand, Überschwemmung, Stromausfall)
- Regionale Katastrophen (Erdbeben, Sturm)
- Erweiterte Cloud-Provider-Ausfälle (Multi-Region-Deployment)

**Optionen für geografische Redundanz**:

| Redundanzgrad | Geografische Trennung | Schutz gegen | Beispiel |
|--------------|----------------------|--------------|---------|
| **Multi-Server** | Gleiches Rechenzentrum/Rack | Server-Hardwareausfall | Geclusterte Server |
| **Multi-Rack** | Gleiches Rechenzentrum | Strom-/Kühlungsausfall im Rack | Server in verschiedenen Racks |
| **Multi-Zone** | Gleiche Region, verschiedene Verfügbarkeitszonen | Rechenzentrumsseitiger Ausfall | AWS Multi-AZ, Azure Availability Zones |
| **Multi-Region** | Verschiedene geografische Regionen | Regionale Katastrophe | AWS eu-central-1 + eu-west-1 |
| **Multi-Cloud** | Verschiedene Cloud-Provider | Cloud-Provider-Ausfall | AWS + Azure-Redundanz |

**DORA/NIS2-Compliance**: Finanzeinheiten und wesentliche Einheiten sollten geografische Redundanz für kritische Systeme implementieren, um Anforderungen an die operative Resilienz zu erfüllen.

**Kosten-Nutzen-Analyse**: Entscheidungen zur geografischen Redundanz müssen abwägen:

- Kosten redundanter Infrastruktur
- Komplexität des Multi-Region-/Multi-Cloud-Managements
- Risiko regionaler Ausfälle
- Regulatorische Anforderungen (DORA, NIS2, FINMA)
- Geschäftliche Auswirkungen längerer Ausfälle

## Netzwerkredundanz

**Netzwerkredundanzanforderungen**:

Kritische Systeme müssen Netzwerkredundanz auf mehreren Ebenen implementieren:

| Netzwerkebene | Redundanzanforderung | Implementierungsbeispiel |
|--------------|---------------------|-------------------------|
| **Internet-Konnektivität** | Dual-ISPs oder Anbieter | Mehrere Internet-Anbindungen |
| **WAN-Konnektivität** | Redundante Leitungen | MPLS + Internet, Dual-Leitungen |
| **Internes Netzwerk** | Redundante Switches/Router | Switch-Stacking, HSRP/VRRP |
| **Load Balancing** | Mehrere Load Balancer | Aktiv-Aktiv-LB-Cluster |
| **Firewalls** | HA-Firewall-Paare | Aktiv-Passiv-Firewall-Cluster |

**Netzwerk-Failover-Tests**: Netzwerk-Failover-Mechanismen müssen vierteljährlich für kritische Systeme getestet werden.

## Cloud-zu-On-Premises-Redundanz

**Hybride Redundanzstrategien**:

Für Organisationen mit hybriden Cloud-Deployments sollten Redundanzstrategien Folgendes berücksichtigen:

**Cloud-First mit On-Premises-Fallback**:

- Primär: Cloud-Infrastruktur (AWS, Azure, GCP)
- Sekundär: Lokale Infrastruktur für erweiterte Cloud-Ausfälle
- Anwendungsfall: Cloud-Repatriierung bei mehrtägigen Cloud-Provider-Vorfällen

**On-Premises-First mit Cloud-Failover**:

- Primär: Lokale Infrastruktur
- Sekundär: Cloud-Infrastruktur für DR
- Anwendungsfall: Traditionelles On-Premises mit Cloud als Notfallwiederherstellungsziel

**Aktiv-Aktiv-Hybrid**:

- Traffic aufgeteilt zwischen Cloud und On-Premises
- Beide Umgebungen gleichzeitig aktiv
- Anwendungsfall: Geografische Verteilung, Leistungsoptimierung

**Implementierungsüberlegungen**:

- Datensynchronisation zwischen Cloud und On-Premises
- Netzwerkkonnektivitätsanforderungen (VPN, Direct Connect, ExpressRoute)
- Lizenzportabilität (Bring-Your-Own-License in die Cloud)
- Wiederherstellungsverfahren für bidirektionalen Failover

## Strom- und Umgebungsredundanz

**Redundanz kritischer Infrastruktur**:

Rechenzentren und kritische Infrastruktureinrichtungen müssen Redundanz für folgendes implementieren:

**Stromversorgungssysteme**:

- Doppelstromeinspeisung vom Versorgungsunternehmen (soweit verfügbar)
- Unterbrechungsfreie Stromversorgungssysteme (USV)
- Notstromaggregat mit Kraftstoffvorrat
- Automatische Transferschalter

**Kühlsysteme**:

- Redundante HVAC-Einheiten
- Umgebungsüberwachung (Temperatur, Luftfeuchtigkeit)
- Alarme bei Überschreitung von Umgebungsschwellenwerten

**Physische Sicherheit**:

- Redundante Zugangskontrollsysteme
- Backup-Sicherheitsüberwachung

**Cloud-Umgebungen**: Cloud-Provider implementieren typischerweise N+1- oder 2N-Strom-/Kühlungsredundanz. Redundanzaussagen des Anbieters verifizieren durch:

- SOC-2-Typ-II-Berichte
- Standortbesuche (soweit erlaubt)
- Drittpartei-Rechenzentrum-Zertifizierungen (Tier III/IV)

---

# IKT-Bereitschaft für Business Continuity (A.5.30)

[Organisation] implementiert IKT-Kontinuitätsplanung, um Bereitschaft für Geschäftsunterbrechungen sicherzustellen.

## Business Impact Analysis (BIA)

**BIA-Prozess**:

Business Impact Analysis muss durchgeführt werden, um:

- Kritische Geschäftsprozesse zu identifizieren
- IKT-Abhängigkeiten für jeden Geschäftsprozess zu bestimmen
- Auswirkungen von IKT-Unterbrechungen zu quantifizieren (finanziell, operativ, reputationsbezogen, regulatorisch)
- Maximale tolerierbare Ausfallzeit (MTD), Recovery Time Objective (RTO) und Recovery Point Objective (RPO) festzulegen

**BIA-Häufigkeit**: BIA muss durchgeführt werden:

- Erstmals bei der ISMS-Implementierung
- Mindestens jährlich
- Bei wesentlichen Geschäftsänderungen (neue Dienste, Akquisitionen, grössere Systemänderungen)
- Nach grösseren Vorfällen (Integration von Lessons Learned)

**BIA-Ergebnis**:

- Geschäftsprozessinventar mit Kritikalitätsbewertungen
- IKT-Systeminventar mit Kritikalitätsklassifizierungen (Tier 1–4)
- MTD, RTO und RPO für jedes kritische System
- Abhängigkeitsmapping (Systemwechselwirkungen)
- Auswirkungsquantifizierung (finanzieller Verlust pro Ausfallstunde)

**BIA-Dokumentation**: BIA-Ergebnisse müssen dokumentiert werden in:

- **Systemkritikalitätsregister**: Hauptinventar aller Systeme mit Tier-1–4-Klassifizierung, dokumentierten MTD/RTO/RPO, geschäftlicher Begründung und Unterschrift des Eigentümers. Gepflegt vom BC/DR-Koordinator in [ISMS-Tool/SharePoint/Datenbank]. Aktualisierung innerhalb von 30 Tagen nach jeder Systemklassifizierungsänderung.
- **Geschäftsprozess-Abhängigkeitskarten**: Visuelle oder tabellarische Dokumentation der IKT-Abhängigkeiten für jeden kritischen Geschäftsprozess mit vor-/nachgelagerten Systembeziehungen.
- **BIA-Bewertungsberichte**: Formaler BIA-Bericht mit Auswirkungsquantifizierung, Stakeholder-Interviews, Analysemethodik und Unterschriften der Geschäftsprozess- und ISB-Genehmigung.

BIA-Dokumentation muss:
- Versionskontrolliert mit Änderungsverfolgung sein
- Jährlich überprüft und genehmigt werden
- In Arbeitsbuch 3 (RPO/RTO-Compliance-Matrix) referenziert werden
- Zur Auditinspektion aufbewahrt werden (Mindestaufbewahrung 3 Jahre)

**BIA-Verantwortung**: Der BC/DR-Koordinator leitet den BIA-Prozess mit Beiträgen von Geschäftsprozess- und Systemeigentümern.

## IKT-Kontinuitätsstrategie

Basierend auf BIA-Ergebnissen muss [Organisation] eine IKT-Kontinuitätsstrategie definieren, einschliesslich:

**Wiederherstellungsstrategien nach System-Tier**:

| System-Tier | Wiederherstellungsstrategie | Infrastrukturansatz |
|-------------|---------------------------|---------------------|
| **Tier 1 (Kritisch)** | Aktiv-Aktiv oder Hot-Standby | Redundante Infrastruktur, automatischer Failover |
| **Tier 2 (Hoch)** | Warm-Standby oder schneller Neuaufbau | Vorbereitete Ressourcen, dokumentierte Verfahren |
| **Tier 3 (Mittel)** | Cold-Standby oder Backup-Wiederherstellung | Verfügbare Infrastruktur, Backup-Restore |
| **Tier 4 (Niedrig)** | Neuaufbau oder aufgeschobene Wiederherstellung | Standard-Neuaufbauverfahren |

**Strategie für Wiederherstellungsstandorte**:

Wiederherstellungsstandortstrategie von [Organisation]:

- **Hot Site**: Vollständig betriebsbereiter Standort für Tier-1-Systeme (Cloud-Multi-Region, alternatives Rechenzentrum)
- **Warm Site**: Teilweise bereitgestellter Standort für Tier-2-Systeme (Cloud-Reservekapazität, DR-Rechenzentrum)
- **Cold Site**: Infrastrukturbereiter Standort für Tier-3-Systeme (Vertrag mit Rechenzentrumsanbieter)

**Alternative Strategien**:

- Cloud als Wiederherstellungsstandort (On-Premises primär, Cloud-DR)
- Multi-Cloud-Redundanz (AWS + Azure, regionale Diversifizierung)
- Gegenseitige Vereinbarungen (gegenseitige DR-Vereinbarungen mit Partnern – selten genutzt)

## IKT-Wiederherstellungspläne

**Dokumentation der IKT-Kontinuitätspläne**:

IKT-Kontinuitätspläne müssen dokumentieren:

**Planstruktur**:
1. **Aktivierungskriterien**: Wann der Plan zu aktivieren ist (Katastrophendeklarationsprozess)
2. **Rollen und Verantwortlichkeiten**: Wiederherstellungsteamstruktur, Eskalationsverfahren
3. **Notfallkontakte**: Kontaktlisten für Wiederherstellungsteam, Lieferanten, Stakeholder
4. **Wiederherstellungsverfahren**: Schrittweise Systemwiederherstellungsanweisungen
5. **Kommunikationsverfahren**: Interne und externe Kommunikationsvorlagen
6. **Wiederherstellungsprioritäten**: Systemwiederherstellungsreihenfolge basierend auf Abhängigkeiten
7. **Validierungsverfahren**: Wie der Betriebsstatus der Systeme überprüft wird

**Systemspezifische Wiederherstellungsverfahren**:

Für jedes kritische und hochprioritäre System:

- Voraussetzungen (Infrastruktur, Netzwerk, Abhängigkeiten)
- Schrittweise Wiederherstellungsanweisungen
- Schätzungen der Wiederherstellungszeit
- Validierungsschritte zur Bestätigung erfolgreicher Wiederherstellung
- Rollback-Verfahren bei fehlgeschlagener Wiederherstellung
- Bekannte Probleme und Umgehungslösungen

**Planpflege**: IKT-Kontinuitätspläne müssen:

- Jährlich überprüft werden
- Nach Testübungen aktualisiert werden
- Nach grösseren Vorfällen aktualisiert werden
- Bei wesentlichen System- oder Infrastrukturänderungen aktualisiert werden
- Mit Versionskontrolle und Änderungsverfolgung verwaltet werden

## BC/DR-Testprogramm

**Testtypen**:

| Testtyp | Beschreibung | Häufigkeit | Umfang |
|---------|-------------|------------|--------|
| **Tabletop-Übung** | Diskussionsbasierter Walkthrough | Jährlich | Alle kritischen Prozesse |
| **Komponententest** | Test der Wiederherstellung einzelner Systeme | Vierteljährlich | Kritische Systeme |
| **Vollständiger DR-Test** | Kompletter Failover zum DR-Standort | Jährlich | Kritische Prozesse Ende-zu-Ende |
| **Überraschungstest** | Unangekündigter Test (optional) | Nach Bedarf | Ausgewählte Systeme |

**Testplan nach Kritikalität**:

| Kritikalität | Jährliche Testanforderung |
|-------------|--------------------------|
| **Kritisch** | Vollständiger DR-Test + 2 Komponententests |
| **Hoch** | Vollständiger DR-Test oder 2 Komponententests |
| **Mittel** | Komponententest oder Tabletop-Übung |
| **Niedrig** | Tabletop-Übung |

**DORA-Compliance**: Dem DORA unterliegende Finanzeinheiten müssen:

- BC-Massnahmen mindestens jährlich testen (Art. 11(9))
- IKT-Backup und Wiederherstellung mindestens jährlich testen (Art. 12(6))
- BC/DR-Tests mit bedrohungsgeführten Penetrationstests integrieren (Art. 26)

**Testdokumentation**: Jeder BC/DR-Test muss dokumentieren:

- Testdatum, Umfang, Ziele und Teilnehmer
- Testszenario und Bedingungen
- Testergebnisse (Erfolg/Fehlschlag/teilweise)
- Tatsächliches RTO/RPO gegenüber Ziel
- Während des Tests identifizierte Probleme
- Gewonnene Erkenntnisse und Massnahmenpunkte
- Erforderliche Planaktualisierungen basierend auf Testergebnissen
- Abzeichnung durch BC/DR-Koordinator und ISB

**Reaktion auf fehlgeschlagene Tests**: Tests, bei denen die Unfähigkeit, RTO/RPO einzuhalten, aufgedeckt wird, lösen folgendes aus:

- Sofortige Untersuchung und Ursachenanalyse
- Gap-Behebungsplan mit Zeitplan
- Risikobewertung der aktuellen Fähigkeiten
- Temporäre kompensierende Massnahmen falls erforderlich
- Benachrichtigung der Geschäftsleitung bei kritischen Systemen
- Wiederholungstest nach Behebung

## RPO/RTO-Compliance-Überwachung

**RPO/RTO-Ausrichtung**: Technische Fähigkeiten (Backup-Häufigkeit, Redundanzarchitektur) müssen mit den geschäftlich definierten RPO/RTO-Anforderungen übereinstimmen.

**Compliance-Bewertung**:

- Backup-Häufigkeit vs. RPO: Unterstützt der Backup-Plan das RPO?
- Redundanzfähigkeit vs. RTO: Kann der Failover das RTO einhalten?
- Testergebnisse vs. Ziele: Entsprechen tatsächliche Wiederherstellungszeiten dem RTO?

**Gap-Management**: Identifizierte Lücken zwischen Anforderungen und Fähigkeiten müssen:

- Mit Risikobewertung dokumentiert werden
- Einen Behebungsplan mit Zeitplan haben
- Risikoakzeptanz erfordern, wenn nicht sofort behebbar
- An ISB und Geschäftsleitung für kritische Systeme eskaliert werden

**Kontinuierliche Überwachung**: Automatisierte Überwachung verfolgt:

- Backup-Auftragsabschluss innerhalb des RPO-Fensters
- Redundanzintegritätsprüfungen
- Failover-Fähigkeitsverifikation
- Compliance mit dem Testzeitplan

**RPO/RTO-Reporting**: Quartalsberichte an den ISB müssen umfassen:

- Systeme, die RPO/RTO-Ziele einhalten vs. nicht einhalten
- Gap-Analyse mit kritikalitätspriorisierter Behebung
- Status der Testkonformität
- Trendanalyse (verbessernd vs. verschlechternd)

## Lieferanten- und Drittparteikoordination

**Lieferanten-BC/DR-Anforderungen**: Lieferanten, die kritische oder hochprioritäre Dienste erbringen, müssen die Anforderungen gemäss ISMS-POL-A.5.19-23 (Lieferanten-/Cloud-Dienste) erfüllen, einschliesslich:

- Dokumentierte BC/DR-Pläne
- Definiertes SLA einschliesslich RTO/RPO-Zusagen
- Jährliche BC/DR-Tests mit Weitergabe der Ergebnisse
- Verfahren zur Vorfallbenachrichtigung
- Überprüfung des Lieferanten-BC/DR-Plans bei der Due Diligence

**Koordination mit Cloud-Providern**: Für cloud-gehostete Systeme:

- BC/DR-Fähigkeiten und -Verantwortlichkeiten des Providers verstehen
- Validieren, ob Provider-SLA mit organisatorischen RTO/RPO übereinstimmt
- Kundenseitig verwaltetes DR implementieren, wenn Providerfähigkeiten unzureichend
- Verfahren zur Provider-Vorfallbenachrichtigung dokumentieren
- Wiederherstellungsverfahren einschliesslich Provider-Einbindung testen

**Koordination mit Managed-Service-Providern**: Für ausgelagerten IKT-Betrieb:

- Sicherstellen, dass MSP-Wiederherstellungspläne mit organisatorischen BC-Plänen integriert sind
- MSP-Rollen und -Verantwortlichkeiten bei Katastrophen festlegen
- MSP in BC/DR-Testübungen einbeziehen
- MSP-Personalverfügbarkeit und -ressourcen bei Katastrophen verifizieren

## Krisenkommunikation

**Anforderungen an den Kommunikationsplan**: BC/DR-Pläne müssen Kommunikationsverfahren enthalten für:

**Interne Kommunikation**:

- Aktivierungsbenachrichtigung (wer, wann, wie)
- Statusaktualisierungen während der Wiederherstellung
- Abschlussmeldung bei abgeschlossener Wiederherstellung
- Terminplanung der Post-Incident-Überprüfung

**Externe Kommunikation**:

- Kundenbenachrichtigung (proaktiv bei bekannten Ausfällen)
- Lieferanten-/Partnerkoordination (falls für die Wiederherstellung erforderlich)
- Behördenbenachrichtigung (falls regulatorisch vorgeschrieben)
- Öffentlichkeits-/Medienkommunikation (soweit anwendbar)

**Kommunikationskanäle**:

- Primär: Kommunikationsplattform von [Organisation] (E-Mail, Teams/Slack)
- Backup: SMS, Telefonanrufe (falls Primärkanal nicht verfügbar)
- Notfall: Vorab vereinbarter externer Kommunikationsdienst

---

# Übergreifende Anforderungen

## Integrierter Testansatz

**Übergreifende Tests**:

BC/DR-Tests müssen alle drei Massnahmen integrieren:

**Integriertes Testszenario**:
1. **Backup-Wiederherstellung** (A.8.13): System aus Backup wiederherstellen
2. **Redundanz-Failover** (A.8.14): Failover auf redundante Infrastruktur
3. **Business Continuity** (A.5.30): Vollständige Geschäftsprozesswiederherstellung ausführen

**Jährlicher integrierter Test**: Mindestens ein jährlicher BC/DR-Test muss üben:

- Backup-Wiederherstellung (Datenwiederherstellung aus Offsite-Backup)
- Redundanzaktivierung (Failover zum DR-Standort/Cloud-Region)
- Geschäftsprozessvalidierung (Bestätigen, dass Geschäftsbetrieb auf wiederhergestellten Systemen fortgesetzt werden kann)
- Kommunikationsverfahren (interne und externe Benachrichtigungen)

**Testerfolgskriterien**:

- Alle Systeme innerhalb der RTO-Ziele wiederhergestellt
- Daten wiederhergestellt entsprechen RPO-Zielen (akzeptabler Datenverlust)
- Geschäftsprozesse auf wiederhergestellten Systemen betriebsbereit
- Kommunikationsverfahren korrekt ausgeführt

## Anforderungen an die Beweiserhebung

**Auditnachweis-Dokumentation**:

Für jede BC/DR-Aktivität müssen Nachweise gepflegt werden:

**Backup-Nachweise**:

- Backup-Auftragsabschluss-Protokolle
- Backup-Speicherinventar (was gesichert wird, wo)
- Backup-Testergebnisse (Wiederherstellungstests mit Screenshots)
- Backup-Überwachungsalarme und Reaktionen

**Redundanz-Nachweise**:

- Redundanzarchitekturdiagramme
- SPOF-Analyseergebnisse
- Failover-Testergebnisse
- Redundanzintegritäts-Überwachungsdaten

**IKT-Kontinuität-Nachweise**:

- BIA-Ergebnisse und Genehmigung
- IKT-Kontinuitätspläne (aktuelle Versionen)
- Ergebnisse von Testübungen
- Planaktualisierungshistorie

**Nachweisrepository in Summary Dashboards**: Der BC/DR-Koordinator muss ein zentralisiertes Nachweisrepository pflegen, einschliesslich:

- Testergebnisdatenbank
- Planversionen und Änderungshistorie
- Ausnahmeregister
- Post-Mortems bei BC/DR-aktivierenden Vorfällen

## Gap-Management und Behebung

**Gap-Identifikation**:

Lücken in BC/DR-Fähigkeiten müssen identifiziert werden durch:

- Testfehlschläge (Systeme erfüllen RTO/RPO nicht)
- BIA-Aktualisierungen (neue kritische Systeme identifiziert)
- Auditfeststellungen (interne oder externe Audits)
- Lessons Learned aus Vorfällen (tatsächliche Katastrophenreaktion)
- Technologieänderungen (neue Systeme ohne Backup/Redundanz)

**Gap-Priorisierung**:

| Gap-Typ | Priorität | Behebungszeitrahmen |
|---------|----------|---------------------|
| **Kritisches System erfüllt RTO/RPO nicht** | P1 – Kritisch | 30 Tage oder Risikoakzeptanz |
| **Hochprioritäres Systemgap** | P2 – Hoch | 90 Tage |
| **Mittelprioritäres Systemgap** | P3 – Mittel | 180 Tage |
| **Test-Nichtkonformität** | P2 – Hoch | Nächster Testzyklus |

**Gap-Behebungsprozess**:
1. Gap identifiziert und dokumentiert
2. Ursachenanalyse
3. Behebungsplan entwickelt (technische Lösung, Zeitplan, Ressourcen)
4. ISB-Genehmigung des Plans
5. Implementierung und Validierung
6. Wiederholungstest zur Bestätigung der Gap-Schliesssung
7. Dokumentationsaktualisierung

**Gap-Register**: Der BC/DR-Koordinator muss ein Gap-Register pflegen, einschliesslich:

- Gap-Beschreibung
- Betroffenes System/Prozess
- Risikobewertung
- Behebungsplan und Zeitplan
- Behebungsstatus
- Zieldatum für Schliesssung

---

# Governance & Compliance

## Rollen & Verantwortlichkeiten

| Rolle | BC/DR-Verantwortlichkeiten |
|-------|---------------------------|
| **Geschäftsführer (GF)** | Letztverantwortung für Business Continuity; Genehmigung der BC/DR-Strategie und des Budgets; Erklärung von Katastrophen, die eine Planaktivierung erfordern |
| **Informationssicherheitsbeauftragter (ISB)** | BC/DR-Richtlinieneigentümer; Genehmigung von BC/DR-Anforderungen und Risikoakzeptanz; Sicherstellung ausreichender Ressourcen für BC/DR-Implementierung; Berichterstattung des BC/DR-Status an die Geschäftsleitung |
| **IT-Leiter (ITL)** | Operative Verantwortung für IKT-Kontinuität; Ressourcenzuteilung für Backup-/Redundanzimplementierung; Genehmigung von Technologieinvestitionen für BC/DR; Sicherstellung der Ausrichtung von IKT-Wiederherstellungsplänen an Geschäftsanforderungen |
| **BC/DR-Koordinator** | Tägliches BC/DR-Programmmanagement; Koordination des BIA-Prozesses; Pflege von Wiederherstellungsplänen; Planung und Facilitation von BC/DR-Tests; Verfolgung der Compliance mit Backup-/Redundanzanforderungen; Berichterstattung von BC/DR-Metriken und Gaps |
| **Backup-Administrator** | Implementierung und Verwaltung von Backup-Lösungen; Konfiguration von Backup-Zeitplänen und -Aufbewahrung; Überwachung von Backup-Aufträgen und Fehlersuche; Koordination von Backup-Tests; Pflege der Backup-Infrastruktur |
| **Systemadministratoren / Cloud-Administratoren** | Implementierung von Redundanz für zugewiesene Systeme; Konfiguration von Failover-Mechanismen; Teilnahme an BC/DR-Tests; Pflege von Systemwiederherstellungsdokumentation; Reaktion auf Systemausfälle und Wiederherstellungsereignisse |
| **Systemeigentümer / Anwendungseigentümer** | Definition von RTO/RPO-Anforderungen für ihre Systeme; Beitrag zum BIA-Prozess; Genehmigung von Systemwiederherstellungsprioritäten; Teilnahme an BC/DR-Tests; Validierung der Funktionalität wiederhergestellter Systeme |
| **Geschäftsprozesseigentümer** | Definition von Business-Continuity-Anforderungen; Identifikation kritischer Prozesse und Abhängigkeiten; Genehmigung von RTO/RPO für Geschäftsprozesse; Teilnahme an BC/DR-Übungen; Validierung der Wiederherstellung von Geschäftsprozessen |
| **Sicherheitsteam** | Überwachung der Sicherheit von Backup- und DR-Infrastruktur; Überprüfung der Verschlüsselungsimplementierung; Überprüfung der Sicherheit von DR-Standorten und Cloud-DR; Teilnahme an BC/DR-Tests; Koordination der Incident-Response |
| **Rechts-/Compliance-Beauftragter** | Bestimmung regulatorischer BC/DR-Anforderungen; Sicherstellung der Compliance mit DORA, NIS2 etc.; Überprüfung von Lieferanten-BC/DR-Verpflichtungen; Beratung zu Datenresidenz-Implikationen |

**Verantwortungsmatrix**:

| Aktivität | Verantwortlich | Unterstützung | Genehmigung | Informiert |
|-----------|---------------|---------------|-------------|------------|
| BIA-Prozess | BC/DR-Koordinator | Geschäftseigentümer, Systemeigentümer | ISB | ITL |
| Backup-Richtlinie | ISB | BC/DR-Koordinator | Geschäftsleitung | Alle Mitarbeitenden |
| Backup-Implementierung | Backup-Administrator | Systemadministratoren | ITL | BC/DR-Koordinator |
| Redundanzdesign | Systemeigentümer | Infrastrukturteam | ITL | BC/DR-Koordinator |
| Wiederherstellungsplanentwicklung | BC/DR-Koordinator | Systemeigentümer | ISB | Geschäftseigentümer |
| BC/DR-Tests | BC/DR-Koordinator | Gesamtes Wiederherstellungsteam | ISB | Geschäftsleitung |
| Gap-Behebung | Systemeigentümer | Infrastrukturteam | ISB (Risikoakzeptanz) | BC/DR-Koordinator |

## Ausnahmeverwaltung

**Ausnahmeantragsverfahren**:

Ausnahmen von BC/DR-Anforderungen (z.B. System vom Backup ausgeschlossen, Redundanz nicht implementiert) folgen einem formalen Genehmigungsverfahren:

**Schritt 1: Einreichung des Ausnahmeantrags**

- Antragsteller: System- oder Geschäftseigentümer
- Erforderliche Informationen: System/Geltungsbereich, ausgenommene Anforderung, geschäftliche Begründung, Risikobewertung, vorgeschlagene kompensierende Massnahmen, Ausnahmedauer

**Schritt 2: Risikobewertung**

- Durchgeführt von: BC/DR-Koordinator + Sicherheitsteam
- Bewertung: Auswirkungen bei Eintreten einer Katastrophe, Wahrscheinlichkeit einer Katastrophe, regulatorische Implikationen, Risikoeinstufung

**Schritt 3: Genehmigungsentscheidung**

| Risikograd der Ausnahme | Genehmigungsbehörde |
|------------------------|---------------------|
| Niedriges Risiko (unkritisches System, kurze Dauer) | BC/DR-Koordinator |
| Mittleres Risiko | ISB |
| Hohes Risiko (kritisches System, regulatorische Auswirkungen) | ISB + ITL |
| Kritisches Risiko (schwerwiegende Geschäftsauswirkungen) | Geschäftsleitung (GF/ITL/ISB) |

**Schritt 4: Ausnahmeverfolgung**

- Alle Ausnahmen im Ausnahmeregister dokumentiert
- Regelmässige Überprüfung (vierteljährlich für temporäre Ausnahmen)
- Neu-Genehmigung bei Ablauf erforderlich
- Behebungsverfolgung bei temporären Ausnahmen

**Permanente Ausnahmen**: Dauerhaft von Backup-/Redundanzanforderungen ausgenommene Systeme müssen:

- Dokumentierte Risikoakzeptanz haben
- Jährlich überprüft werden
- ISB-Genehmigung für kritische/hochprioritäre Systeme erfordern
- Begründen, warum ein Standard-BC/DR-Ansatz nicht realisierbar ist

## Überwachung & Reporting

**Kontinuierliche Überwachung**:

- Erfolgs-/Fehlerquoten von Backup-Aufträgen
- Auslastung der Backup-Speicherkapazität
- Redundanzintegritätsprüfungen (Clustering, Replikationsstatus)
- RPO/RTO-Compliance-Metriken
- Einhaltung des Testzeitplans

**Reporting-Anforderungen**:

**Monatsberichte** (BC/DR-Koordinator → ISB):

- Backup-Erfolgsquote nach Kritikalität
- Fehlgeschlagene Backups, die Untersuchung erfordern
- Redundanzverfügbarkeitsstatus
- Anstehender Testzeitplan
- Offene Probleme und Behebungsstatus

**Quartalsberichte** (BC/DR-Koordinator → ISB + ITL):

- BC/DR-Programm-KPIs
- RPO/RTO-Compliance-Zusammenfassung
- Testergebnisse und Lessons Learned
- Gap-Analyse mit Priorisierung
- Ausnahmeregister-Überprüfung
- Trendanalyse

**Jahresberichte** (ISB → Geschäftsleitung):

- BC/DR-Reifegradbeurteilung
- Grössere Vorfälle und Wirksamkeit der Wiederherstellung
- Compliance mit regulatorischen Anforderungen
- Investitionsbedarf und strategische Empfehlungen

**Key Performance Indicators (KPIs)**:

| KPI | Ziel | Messung |
|-----|------|---------|
| Backup-Abdeckung (% gesicherter kritischer Systeme) | 100 % | Monatlich |
| Backup-Erfolgsquote | ≥ 99 % | Monatlich |
| Backup-Test-Compliance | ≥ 95 % | Vierteljährlich |
| RPO-Compliance (% Systeme erfüllen RPO) | 100 % kritisch, ≥ 95 % hoch | Vierteljährlich |
| RTO-Compliance (% Systeme erfüllen RTO bei Tests) | 100 % kritisch, ≥ 95 % hoch | Vierteljährlich |
| DR-Test-Erfolgsquote | ≥ 90 % | Jährlich |
| SPOF-Behebung (% kritische SPOFs mitigiert) | ≥ 90 % | Vierteljährlich |

## Vorfallmanagement

**BC/DR-Vorfalltypen**:

| Vorfalltyp | Beschreibung | Reaktion |
|-----------|-------------|----------|
| **Backup-Fehler** | Backup eines kritischen Systems schlägt mehrfach fehl | Sofortige Untersuchung, ggf. Wiederherstellung aus vorherigem Backup |
| **Speicherkapazität** | Backup-Speicher überschreitet Schwellenwert | Kapazität erweitern oder Aufbewahrungsrichtlinie anpassen |
| **Redundanzausfall** | Failover-Fähigkeit nicht verfügbar | Sofortige Behebung, Risikobewertung |
| **Testfehlschlag** | Wiederherstellungstest erfüllt RTO/RPO nicht | Ursachenanalyse, Behebungsplan |
| **Katastrophenereignis** | Tatsächliche Katastrophe erfordert Wiederherstellung | BC/DR-Plan aktivieren, Wiederherstellungsverfahren ausführen |

**Vorfallbenachrichtigung**:

- Backup-Fehler (kritische Systeme): BC/DR-Koordinator + Systemeigentümer sofort benachrichtigen
- Redundanzausfälle: BC/DR-Koordinator + ISB sofort benachrichtigen
- Katastrophendeklaration: Krisenkommunikationsplan aktivieren

**Integration mit Incident Management**: BC/DR-Vorfälle integrieren sich mit dem organisatorischen Incident-Management-Prozess (A.5.24–27) für:

- Vorfallerfassung und -verfolgung
- Ursachenanalyse
- Lessons Learned
- Kontinuierliche Verbesserung

## Richtlinien-Governance

**Richtlinienüberprüfung**:

- **Häufigkeit**: Mindestens jährlich
- **Auslöser**: Regulatorische Änderungen, grössere Vorfälle, wesentliche Geschäftsänderungen, Auditfeststellungen, Technologieänderungen
- **Prüfer**: ISB, BC/DR-Koordinator, ITL, Recht/Compliance
- **Genehmigung**: ISB (technisch), Geschäftsleitung (strategisch)

**Überprüfung von Implementierungsstandards**:

- **Häufigkeit**: Basierend auf technologischer Entwicklung (mindestens halbjährlich)
- **Zuständigkeit**: BC/DR-Koordinator schlägt Aktualisierungen vor, ISB genehmigt
- **Hinweis**: Aktualisierungen von Implementierungsstandards (ISMS-IMP-A.5.30-8.13-14) erfordern keine Richtlinienrevision

**Richtlinienaktualisierungen**:

- **Kleinere Änderungen** (Klarstellungen, Referenzen): ISB-Genehmigung, Kommunikation innerhalb von 30 Tagen
- **Grössere Änderungen** (Geltungsbereichsänderungen, neue Anforderungen): Vollständige Genehmigungskette, Implementierungszeitplan gemäss Änderungsmanagement
- **Notfalländerungen** (kritische regulatorische Änderung, Lessons Learned aus grösseren Vorfällen): ISB-Genehmigung, sofortige Kommunikation und Implementierung

**Kommunikation**: Richtlinie im ISMS-Dokumentenrepository veröffentlicht. Änderungen organisationsweit kommuniziert. Schulungen für wesentliche Änderungen mit Auswirkungen auf Verantwortlichkeiten oder Verfahren bereitgestellt.

---

# Implementierung & Referenzen

## Integration mit dem ISMS

Diese Richtlinie integriert sich mit dem Informationssicherheitsmanagementsystem von [Organisation]:

**Risikobewertung** (ISO 27001 Klausel 6.1):

- BC/DR-Massnahmen auf Basis der Risikobewertung von [Organisation] ausgewählt
- BIA-Ergebnisse fliessen in den Risikobewertungsprozess ein
- Risikobehandlungspläne dokumentieren BC/DR-Massnahmenimplementierung
- Restrisiken aus BC/DR-Ausnahmen dokumentiert

**Aktivinventar** (A.5.9):

- Systeme mit Backup-/Redundanzbedarf über das Aktivinventar identifiziert
- Aktivkritikalitätsklassifizierung bestimmt BC/DR-Anforderungen
- Änderungen am Aktivinventar lösen BC/DR-Überprüfung aus

**Konfigurationsmanagement** (A.8.9):

- Systemkonfigurationen gemäss Backup-Richtlinie gesichert
- Konfigurationsbaselines für die Wiederherstellung dokumentiert
- Infrastructure-as-Code ermöglicht schnellen Neuaufbau
- Integration: Konfigurationsbackups gemäss A.8.9-Anforderungen verwaltet

**Protokollierung** (A.8.15):

- Backup-Vorgänge protokolliert (Erfolg, Fehler, Dauer)
- Failover-Ereignisse protokolliert
- Wiederherstellungsvorgänge zur Prüfprotokollierung protokolliert
- Integration: BC/DR-Protokolle gemäss A.8.15-Anforderungen zentralisiert

**Überwachungsaktivitäten** (A.8.16):

- Backup-Überwachung in organisatorische Überwachungsplattform integriert
- Gesundheit redundanter Systeme kontinuierlich überwacht
- RPO/RTO-Compliance überwacht
- Integration: BC/DR-Überwachung gemäss A.8.16-Anforderungen

## Implementierungsressourcen

**Implementierungsleitfaden** (ISMS-IMP-A.5.30-8.13-14 Suite):

| Dokument | Zweck | Geltungsbereich |
|----------|-------|-----------------|
| **ISMS-IMP-A.5.30-8.13-14-S1** | BIA und RPO/RTO-Prozess | Business-Impact-Analysis-Methodik, Systemkritikalitätsklassifizierung, RPO/RTO-Bestimmung |
| **ISMS-IMP-A.5.30-8.13-14-S2** | Backup-Implementierung | Backup-Lösungsauswahl, Architekturdesign, Zeitplanung, Aufbewahrung, Überwachung, Wiederherstellungsverfahren |
| **ISMS-IMP-A.5.30-8.13-14-S3** | Redundanzimplementierung | SPOF-Identifikation, Redundanzarchitekturdesign, Failover-Mechanismen, geografische Redundanz |
| **ISMS-IMP-A.5.30-8.13-14-S4** | Wiederherstellungstestprozess | Backup-Wiederherstellungstest, Failover-Test, BC/DR-Szenariotests, Beweiserhebung |

**Bewertungswerkzeuge** (Excel-Arbeitsbücher):

- **Arbeitsbuch 1**: Backup-Inventar & Abdeckungsbewertung (gesicherte Systeme, RPO-Compliance, 3-2-1-1-0-Compliance)
- **Arbeitsbuch 2**: Redundanzanalyse (Redundanzarchitektur, SPOF-Analyse, RTO-Compliance)
- **Arbeitsbuch 3**: RPO/RTO-Compliance-Matrix (Geschäftsanforderungen vs. technische Fähigkeiten, Gap-Analyse)
- **Arbeitsbuch 4**: BC/DR-Testergebnisse (Testinventar, Ergebnisverfolgung, Behebungsstatus)

**Unterstützende Materialien**:

- Vorlagen für Wiederherstellungsverfahren
- BIA-Fragebogen-Vorlagen
- Test-Checklisten und -Szenarien
- Ausnahmeantrag-Formulare
- Vorlagen zur Verfolgung der Gap-Behebung

## Regulatorisches Mapping

Diese Richtlinie adressiert BC/DR-Anforderungen aus anwendbaren Vorschriften:

| Anforderungskategorie | Schweizer nDSG | EU DSGVO | ISO 27001 | DORA* | NIS2* | PCI DSS v4.0.1* | FINMA* |
|----------------------|---------------|----------|-----------|-------|-------|---------|--------|
| Backup-Anforderungen | Art. 8 | Art. 32 | A.8.13 | Art. 12 | Art. 21 | Anf. 12.10 | Risikobasiert |
| Offsite-Backup | Art. 8 | Art. 32 | A.8.13 | Art. 12 (Pflicht) | Art. 21 (Pflicht) | Anf. 12.10 | Risikobasiert |
| Unveränderlichkeit | – | – | A.8.13 | Art. 12 (Pflicht) | Art. 21 (Empfohlen) | – | Risikobasiert |
| Redundanz | Art. 8 | Art. 32 | A.8.14 | Art. 12 | Art. 21 | – | Risikobasiert |
| IKT-Kontinuitätsplanung | Art. 8 | Art. 32 | A.5.30 | Art. 12, 14 | Art. 21 | Anf. 12.10 | Risikobasiert |
| Testanforderungen | Art. 8 | Art. 32 | A.8.13, A.5.30 | Art. 12 | Art. 21 | Anf. 12.10 | Risikobasiert |
| Vorfallbenachrichtigung | Art. 24 | Art. 33 | A.5.24 | Art. 19 (24 h) | Art. 23 (24 h) | Anf. 12.10 | Incident Mgmt |
| Lieferanten-BC/DR | Art. 9 | Art. 28 | A.5.19–23 | Art. 28 | Art. 22 | Anf. 12.8 | Outsourcing |

*Bedingte Anwendbarkeit gemäss ISMS-POL-00

**DORA-spezifisches Mapping** (Art. 11–12):

- IKT-Business-Continuity-Richtlinie → Abschnitt 2.3
- Backup-Richtlinien und -Verfahren → Abschnitt 2.1
- Notfallwiederherstellungspläne → Abschnitt 2.3.3
- Unveränderliche Backups → Abschnitt 2.1.6
- Offsite-Backup-Speicherung → Abschnitt 2.1.6
- Jährliche Backup-Tests → Abschnitt 2.1.8
- Jährliche BC-Plan-Tests → Abschnitt 2.3.4

**NIS2-spezifisches Mapping** (Art. 21):

- Business Continuity und Krisenmanagement → Abschnitt 2.3
- Backup-Management und Wiederherstellung → Abschnitt 2.1
- 3-2-1-Backup-Regel → Abschnitt 2.1.5
- 24-Stunden-Vorfallmeldung → ISMS-POL-A.5.24 (Incident Management)

## Schulung & Sensibilisierung

**Sicherheitsbewusstsein** (alle Mitarbeitenden):

- Jährliches Schulungsmodul zur BC/DR-Sensibilisierung
- Verantwortlichkeiten der Nutzenden bei Katastrophen
- Best Practices für Datensicherung (für den persönlichen Verantwortungsbereich)
- Business-Continuity-Denkweise und -Kultur

**BC/DR-Team-Schulung** (BC/DR-Koordinator, Backup-Administratoren, Systemadministratoren):

- BC/DR-Richtlinie und -Verfahren
- Konfiguration und Verwaltung von Backup-Technologien
- Ausführung von Wiederherstellungsverfahren
- Test-Methodik und -Dokumentation
- Incident Response bei Katastrophen

**Schulung des Wiederherstellungsteams**:

- Jährliche Überprüfung von Wiederherstellungsplänen
- Teilnahme an BC/DR-Übungen
- Rollenspezifische Wiederherstellungsverfahren
- Krisenkommunikationsverfahren

**Schulung der Geschäftsleitung**:

- BC/DR-Strategie und Governance
- Kriterien und Verfahren für die Katastrophendeklaration
- Verantwortlichkeiten der Krisenführung
- Regulatorische Compliance-Anforderungen

---

# Definitionen

**Backup**: Kopie von Daten, Software oder Systemkonfiguration, die zum Zweck der Wiederherstellung bei Verlust, Beschädigung, Korruption oder Nichtverfügbarkeit erstellt wird. Backups werden typischerweise getrennt von Produktionssystemen gespeichert.

**Redundanz**: Implementierung von Duplikaten oder alternativen informationsverarbeitenden Einrichtungen zur Sicherstellung der Verfügbarkeit bei Ausfall. Redundanz kann hardware-basiert (mehrere Server), software-basiert (Clustering) oder geografisch (mehrere Rechenzentren) sein.

**Business Continuity (BC)**: Fähigkeit einer Organisation, Geschäftsbetrieb während und nach störenden Ereignissen aufrechtzuerhalten. BC umfasst sowohl IKT-Systeme als auch Nicht-IKT-Geschäftsprozesse.

**Notfallwiederherstellung (DR – Disaster Recovery)**: Prozess der Wiederherstellung von IKT-Systemen und -Daten nach einer Unterbrechung. DR ist ein Teilbereich der Business Continuity, der sich speziell auf die IKT-Wiederherstellung konzentriert.

**Recovery Point Objective (RPO)**: Maximal akzeptable Datenverlustmenge, gemessen in Zeit. Das RPO definiert, wie häufig Backups erstellt werden müssen. Beispiel: RPO von 4 Stunden bedeutet, dass Backups mindestens alle 4 Stunden erstellt werden müssen und bis zu 4 Stunden Datenverlust akzeptabel ist.

**Recovery Time Objective (RTO)**: Maximal akzeptable Zeit zur Wiederherstellung eines Systems nach einer Unterbrechung. Das RTO definiert, wie schnell die Wiederherstellung erfolgen muss. Beispiel: RTO von 24 Stunden bedeutet, dass das System innerhalb von 24 Stunden nach dem Ausfall wiederhergestellt sein muss.

**Maximale tolerierbare Ausfallzeit (MTD – Maximum Tolerable Downtime)**: Absolut maximale Zeit, die ein Geschäftsprozess nicht verfügbar sein kann, bevor inakzeptable Konsequenzen eintreten. Die MTD ist typischerweise länger als das RTO, da sie Zeit für Workarounds und manuelle Prozesse einschliesst.

**Business Impact Analysis (BIA)**: Systematischer Prozess zur Identifikation und Bewertung potenzieller Auswirkungen von Unterbrechungen kritischer Geschäftsabläufe. Die BIA bestimmt MTD, RTO und RPO für Geschäftsprozesse und unterstützende IKT-Systeme.

**Single Point of Failure (SPOF)**: Komponente, deren Ausfall zum vollständigen Ausfall eines Systems oder Prozesses führen würde. Die SPOF-Analyse identifiziert Komponenten ohne Redundanz.

**Failover**: Prozess der automatischen oder manuellen Umschaltung auf ein redundantes oder Standby-System bei Ausfall des Primärsystems.

**Hot Site**: Vollständig betriebsbereite Backup-Einrichtung mit Ausrüstung, Konnektivität und Datenreplikation, die sofortigen Failover ermöglicht.

**Warm Site**: Backup-Einrichtung mit Ausrüstung und Konnektivität, die jedoch vor Betriebsbereitschaft eine Datenwiederherstellung erfordert.

**Cold Site**: Backup-Einrichtung mit grundlegender Infrastruktur (Strom, Kühlung, Fläche), die jedoch vor Betriebsbereitschaft Ausrüstungsinstallation und Datenwiederherstellung erfordert.

**Aktiv-Aktiv**: Redundanzarchitektur, bei der mehrere Systeme gleichzeitig aktiv Traffic bedienen. Der Ausfall eines Systems wird von den verbleibenden aktiven Systemen aufgefangen.

**Aktiv-Passiv**: Redundanzarchitektur, bei der das Primärsystem aktiv Traffic bedient, während das Standby-System im Leerlauf verbleibt, aber bei Ausfall des Primärsystems sofort aktivierbar ist.

**Unveränderliches Backup (Immutable Backup)**: Backup, das nach der Erstellung nicht geändert oder gelöscht werden kann (WORM – Write Once Read Many). Bietet Schutz gegen Ransomware und versehentliches Löschen.

**Air-Gapped-Backup**: Backup, das physisch vom Netzwerk getrennt ist und so Isolation gegen Cyberangriffe bietet.

**Offsite-Backup**: An einem geografisch vom primären Datenspeicherort getrennten Ort gespeichertes Backup, das Schutz gegen standortspezifische Katastrophen bietet.

**3-2-1-Backup-Regel**: Branchenbest Practice, die 3 Kopien der Daten (Original + 2 Backups) auf 2 verschiedenen Medientypen mit 1 Kopie am Offsite-Standort empfiehlt.

**3-2-1-1-0-Backup-Regel**: Erweiterte Backup-Regel, die 1 unveränderliche/Air-Gapped-Kopie und 0 Fehler bei der Backup-Verifizierung hinzufügt.

**Inkrementelles Backup**: Backup nur der Daten, die seit dem letzten Backup (beliebiger Typ) geändert wurden, was Backup-Zeit und Speicher reduziert.

**Differentielles Backup**: Backup der Daten, die seit dem letzten Vollbackup geändert wurden, was eine schnellere Wiederherstellung als inkrementell ermöglicht, aber mehr Speicher benötigt.

**Vollbackup**: Vollständiges Backup aller Daten, das die einfachste Wiederherstellung bietet, aber am meisten Zeit und Speicher erfordert.

**Cloud-Repatriierung**: Prozess der Migration von Workloads und Daten von der Cloud zurück auf lokale Infrastruktur, relevant bei längeren Cloud-Ausfällen oder strategischen Änderungen.

**Multi-Cloud**: Architektur, die mehrere Cloud-Provider für Redundanz, Vermeidung von Anbieterbindung oder Diensteoptimierung nutzt.

**Hybrid-Cloud**: Architektur, die lokale Infrastruktur mit Cloud-Diensten kombiniert und flexible Wiederherstellungsszenarien unterstützt.

---

# Genehmigungsnachweis

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Datum] |
| **IT-Leiter (ITL)** | [Name] | [Datum] |
| **BC/DR-Koordinator** | [Name] | [Datum] |
| **Rechts-/Compliance-Beauftragter** | [Name] | [Datum] |
| **Geschäftsleitung** | [Name] | [Datum] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt BC/DR-Anforderungen fest. Implementierungsverfahren sind in ISMS-IMP-A.5.30-8.13-14-S1 bis S4 (UG/TG) dokumentiert. Jedes Bewertungsarbeitsbuch enthält ein eigenes Summary Dashboard zur Compliance-Überprüfung.*

<!-- QA_VERIFIED: 2026-03-28 -->
