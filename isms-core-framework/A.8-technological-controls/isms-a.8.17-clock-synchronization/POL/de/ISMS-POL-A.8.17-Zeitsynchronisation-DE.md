<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.17-DE:framework:POL:a.8.17 -->
**ISMS-POL-A.8.17 — Zeitsynchronisation**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumenttitel** | Zeitsynchronisation |
| **Dokumenttyp** | Richtlinie (Policy) |
| **Dokument-ID** | ISMS-POL-A.8.17 |
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
| 1.0 | [Datum] | ISB | Erstveröffentlichung für ISO-27001:2022-Erstzertifizierung |

**Review-Zyklus**: Jährlich
**Nächstes Review-Datum**: [Gültigkeitsdatum + 12 Monate]

**Freigabekette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL)
- Compliance: Legal/Compliance Officer
- Finale Autorität: Geschäftsleitung (Geschäftsleitung)

**Verknüpfte Dokumente**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.17.1-UG/TG (Zeitquellen-Konfiguration)
- ISMS-IMP-A.8.17.2-UG/TG (Synchronisationsverifizierungsprozess)
- ISMS-IMP-A.8.17.3-UG/TG (Ausnahmenmanagement)
- ISO/IEC 27001:2022 Control A.8.17
- ISMS-POL-A.8.21 (Network Services Security)
- ISMS-POL-A.8.15 (Logging)
- ISMS-POL-A.8.16 (Monitoring Activities)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] an die Zeitsynchronisation über alle informationsverarbeitenden Systeme hinweg fest, um Log-Korrelation, forensische Analyse und zuverlässige Prüfpfade in Übereinstimmung mit ISO/IEC 27001:2022 Control A.8.17 zu ermöglichen.

**Geltungsbereich**: Diese Richtlinie gilt für alle informationsverarbeitenden Systeme, die Protokolle erzeugen oder an sicherheitsrelevanten Operationen beteiligt sind, einschliesslich Server, Netzwerkgeräte, Sicherheitssysteme und Cloud-Instanzen.

**Zweck**: Organisatorische Anforderungen für die Umsetzung und Governance der Zeitsynchronisation definieren. Diese Richtlinie legt fest, WAS an Zeitsynchronisation erforderlich ist und WER verantwortlich ist. Umsetzungsverfahren (WIE) sind separat in ISMS-IMP-A.8.17 (UG/TG-Varianten) dokumentiert.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verpflichtende Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatory Applicability Framework), einschliesslich Swiss nDSG, EU GDPR und ISO/IEC 27001:2022. Bedingte branchenspezifische Anforderungen (PCI DSS v4.0.1, FINMA, DORA, NIS2) gelten dort, wo die Geschäftsaktivitäten von [Organisation] die Anwendbarkeit auslösen.

---

# Kontroll-Ausrichtung & Geltungsbereich

## ISO/IEC 27001:2022 Control A.8.17

**ISO/IEC 27001:2022 Annex A.8.17 — Zeitsynchronisation**

> *Die Uhren der von der Organisation verwendeten informationsverarbeitenden Systeme müssen mit genehmigten Zeitquellen synchronisiert sein.*

**Kontrollziel**: Organisatorische Richtlinie für die Zeitsynchronisation etablieren, die genaue, konsistente Zeitstempel über alle Informationssysteme hinweg sicherstellt, um Log-Korrelation zu ermöglichen, forensische Untersuchungen zu unterstützen, digitale Signaturen zu validieren und die Integrität von Prüfpfaden aufrechtzuerhalten.

**Diese Richtlinie adressiert**:

- Anforderungen an autoritative Zeitquellen und deren Hierarchie
- Anforderungen an die interne Zeitsynchronisationsinfrastruktur
- Synchronisationsanforderungen auf Systemebene und akzeptable Abweichungsschwellen
- Erkennung von Synchronisationsausfällen, Alarmierung und Reaktion
- Integration mit dem Risikobewertungs- und ISMS-Prozessen von [Organisation]

## Was diese Richtlinie tut

Diese Richtlinie:

- **Definiert** Zeitsynchronisationsanforderungen ausgerichtet an Systemkritikalität und betrieblichen Anforderungen
- **Etabliert** einen Governance-Rahmen für die Auswahl von Zeitquellen und die Verifizierung der Synchronisation
- **Legt fest**, wer für die Zeitsynchronisationsinfrastruktur und Compliance verantwortlich ist
- **Verweist** auf anwendbare regulatorische Anforderungen gemäss ISMS-POL-00

## Was diese Richtlinie NICHT tut

Diese Richtlinie tut NICHT:

- **Technische Umsetzungsdetails spezifizieren** (siehe ISMS-IMP-A.8.17.1 Zeitquellen-Konfiguration)
- **Plattformspezifische Konfigurationsverfahren definieren** (siehe ISMS-IMP-A.8.17.1, S2 für Linux, Windows, Netzwerkgeräte, Cloud-Plattformen)
- **Verifizierungs-Befehlssyntax bereitstellen** (siehe ISMS-IMP-A.8.17.2 Synchronisationsverifizierungsprozess)
- **NTP-Technologien oder Anbieter auswählen** (Technologieauswahl basiert auf Risikobewertung und Infrastrukturanforderungen von [Organisation])
- **Risikobewertung ersetzen** (Zeitsynchronisationskontrollen werden basierend auf der Risikobehandlung von [Organisation] ausgewählt)

**Begründung**: Die Trennung von Richtlinienanforderungen und Umsetzungsanleitung ermöglicht:

- Richtlinienstabilität trotz sich weiterentwickelnder Zeitsynchronisationstechnologien (NTP, chrony, PTP, Cloud-Zeitdienste)
- Technische Agilität für Protokollaktualisierungen und Infrastrukturänderungen ohne Richtlinienrevision
- Klare Unterscheidung zwischen Governance (Richtlinie) und Ausführung (Umsetzung)

## Geltungsbereich

**Diese Richtlinie gilt für**:

- Alle informationsverarbeitenden Systeme, die Protokolle erzeugen oder an sicherheitsrelevanten Operationen beteiligt sind
- Server (physisch, virtuell, Cloud-basiert)
- Netzwerkinfrastrukturgeräte (Router, Switches, Firewalls, Load Balancer)
- Sicherheitssysteme (SIEM, IDS/IPS, Authentifizierungssysteme, Schwachstellenscanner)
- Workstations und Endpunkte, wo Protokollierung oder Prüfung erforderlich ist
- Container und Cloud-Instanzen
- IoT- und eingebettete Systeme mit Protokollierungsfähigkeit

**Nicht im Geltungsbereich**:

- Standalone-Systeme ohne Netzwerkkonnektivität oder Protokollierungsfähigkeit
- Endbenutzergeräte, bei denen Zeitsynchronisation nicht sicherheitsrelevant ist
- Systeme, die durch dokumentierte Risikoakzeptanz explizit ausgeschlossen wurden (gemäss Ausnahmeprozess)
- Nicht vernetzte Air-Gapped-Systeme ohne alternative Zeitquellen

## Regulatorische Anwendbarkeit

Regulatorische Anforderungen werden gemäss **ISMS-POL-00 (Regulatory Applicability Framework)** kategorisiert.

**Tier 1: Pflichtige Compliance**

| Verordnung | Anwendbarkeit | Wesentliche Anforderungen |
|------------|---------------|--------------------------|
| **Swiss nDSG** | Alle Schweizer Operationen | Art. 8 — Angemessene technische Massnahmen einschliesslich genauer Protokollierung und Prüfpfade |
| **EU GDPR** | Bei Verarbeitung personenbezogener EU-Daten | Art. 32 — Sicherheitsmassnahmen einschliesslich Protokollierungs- und Monitoring-Fähigkeiten |
| **ISO/IEC 27001:2022** | Zertifizierungsumfang | Control A.8.17 — Dokumentierte Richtlinie und synchronisierte Zeitquellen |

**Tier 2: Bedingte Anwendbarkeit**

Gilt nur, wenn spezifische Geschäftsbedingungen die Anwendbarkeit auslösen:

| Verordnung | Auslösebedingung | Zeitsynchronisationsanforderungen |
|-----------|-----------------|----------------------------------|
| **PCI DSS v4.0.1** | Verarbeitung von Zahlungskarteninhaberdaten | Req. 10.4 — Zeitsynchronisationstechnologie, konsistente Zeiteinstellungen |
| **FINMA** | Schweizer reguliertes Finanzinstitut | Technische und organisatorische Massnahmen einschliesslich Prüfpfad-Integrität |
| **DORA** | EU-Finanzdienstleistungsunternehmen | IKT-Risikomanagement einschliesslich Protokollierungs- und Monitoring-Fähigkeiten |
| **NIS2** | Wesentliche/wichtige Einrichtung (EU) | Sicherheitsmassnahmen für Netz- und Informationssysteme einschliesslich Protokollierung |

**Tier 3: Informative Orientierung**

Diese Rahmenwerke informieren die Umsetzung, stellen aber keine verpflichtende Compliance dar, sofern nicht vertraglich gefordert:

- NIST SP 800-53 (AU-8: Time Stamps)
- CIS Controls v8.1 (Control 8: Audit Log Management)
- RFC 5905 (Network Time Protocol Version 4)
- NIST Time Services (time.nist.gov)

**Compliance-Feststellung**: [Organisation] bestimmt anwendbare Tier-2-Verordnungen durch periodische Bewertung der Geschäftsaktivitäten. Bei Überschneidung mehrerer Verordnungen gelten die strengsten Anforderungen.

---

# Framework der Zeitsynchronisationsanforderungen

## Anforderungen an autoritative Zeitquellen (Verpflichtend)

[Organisation] unterhält Zugang zu autoritativen Zeitquellen, um allen Informationssystemen genaue Referenzzeit bereitzustellen.

**Erforderliche Zeitquellen**:

| Anforderungskategorie | Spezifikation | Umsetzungspriorität |
|---------------------|--------------|---------------------|
| **Redundanz** | Mindestens ZWEI (2) autoritative Zeitquellen | **Verpflichtend** |
| **Stratum-Stufe** | Stratum-0- oder Stratum-1-Quellen | **Verpflichtend** |
| **Verfügbarkeit** | >99,9 % Betriebszeit je Quelle | **Verpflichtend** |
| **Geografische Diversität** | Quellen von unterschiedlichen Standorten wo möglich | Empfohlen |
| **Vertrauenswürdige Anbieter** | Staatliche, akademische oder seriöse kommerzielle Dienste | **Verpflichtend** |

**Primäre Zeitquellen (Stratum 0/1 erforderlich)**:

- GPS-basierte Zeitserver (Stratum 0/1)
- NIST-Zeitserver (time.nist.gov)
- Nationale/regionale staatliche Zeitdienste
- Organisationseigene Atomuhr oder GPS-Empfänger

**Ergänzende/Backup-Quellen (Stratum 2+ akzeptabel)**:

- NTP-Pool-Projekt-Server (pool.ntp.org)
- Cloud-Anbieter-Zeitdienste (AWS Time Sync, Azure NTP, GCP NTP)

**Hinweis**: Interne NTP-Infrastruktur MUSS sich mit mindestens zwei primären (Stratum-0/1-) Quellen synchronisieren. NTP-Pool- und Cloud-Anbieter-Dienste können als ergänzende Quellen für Redundanz dienen, dürfen aber NICHT die einzige autoritative Referenz sein.

**Umsetzungshinweis**: Auswahl spezifischer Zeitquellen, Konfiguration und Verfügbarkeitsmonitoring sind in ISMS-IMP-A.8.17.1 (Zeitquellen-Konfiguration) definiert.

## Interne Zeitsynchronisationsinfrastruktur (Verpflichtend)

[Organisation] betreibt interne NTP-Infrastruktur zur Bereitstellung von Zeitsynchronisationsdiensten für alle Client-Systeme.

**Anforderungen an interne NTP-Infrastruktur**:

| Komponente | Anforderung | Begründung |
|-----------|------------|-----------|
| **Interne NTP-Server** | Mindestens ZWEI (2) Server (Stratum 2) | Redundanz und Failover-Fähigkeit |
| **Autoritätssync** | Synchronisation mit mehreren Stratum-1-Quellen | Genauigkeit und Zuverlässigkeit |
| **Server-Peering** | Peering zwischen internen Servern konfigurieren | Konsistenz und gegenseitige Validierung |
| **Geografische Verteilung** | Einsatz in getrennten Rechenzentren wo möglich | Resilienz und Verfügbarkeit |
| **Hohe Verfügbarkeit** | Automatische Failover-Konfiguration | Kontinuierliche Dienstverfügbarkeit |

**Sicherheitsanforderungen**:

Interne NTP-Server MÜSSEN gemäss den in ISMS-POL-A.8.21 (Network Services Security) definierten Sicherheitsanforderungen gehärtet werden, einschliesslich:

- Zugangskontroll- und Authentifizierungsmechanismen
- Firewall-Regeln zur Einschränkung des NTP-Datenverkehrs (UDP-Port 123)
- Rate-Limiting zur Verhinderung von Amplifikationsangriffen
- Protokollierung von Synchronisationsereignissen und Konfigurationsänderungen
- Regelmässige Sicherheitsupdates und Patching

**Monitoring-Anforderungen**:

Der Zustand interner NTP-Server MUSS kontinuierlich überwacht werden, mit automatischer Alarmierung bei:

- Verlust der Synchronisation mit autoritativen Quellen
- Übermässiger Abweichung (>100 ms von autoritativer Zeit)
- Ausfällen der Dienstverfügbarkeit
- Konfigurationsänderungen oder Anomalien

**Umsetzungshinweis**: NTP-Server-Einsatz, Härtungsverfahren und Monitoring-Konfiguration sind in ISMS-IMP-A.8.17.1 (Zeitquellen-Konfiguration) und ISMS-POL-A.8.21 (Network Services Security) dokumentiert.

## Systemsynchronisationsanforderungen (Verpflichtend)

Alle im Geltungsbereich befindlichen Systeme MÜSSEN so konfiguriert werden, dass sie die Zeit mit genehmigten Zeitquellen synchronisieren.

**Konfigurationsanforderungen für Client-Systeme**:

| Anforderung | Spezifikation | Gilt für |
|------------|--------------|---------|
| **Zeitquellenkonfiguration** | Primäre und sekundäre (Backup-)NTP-Server konfiguriert | Alle Systeme |
| **Synchronisationsmethode** | NTP, chrony, SNTP oder Cloud-Anbieter-Zeitdienst | Plattformabhängig |
| **Aktualisierungsintervall** | Geeignete Synchronisationshäufigkeit (typisch 64–1024 Sekunden) | Alle Systeme |
| **Automatische Korrektur** | Automatische Abweichungskorrektur aktiviert | Alle Systeme |
| **Ereignisprotokollierung** | Synchronisationsereignisse und -ausfälle protokollieren | Alle Systeme |

**Akzeptable Zeitabweichungsschwellen**:

| Systemkategorie | Maximale Abweichung | Gilt für |
|----------------|--------------------|---------|
| **Allgemeine Systeme** | ±1 Sekunde von autoritativer Quelle | Standard-Infrastruktur, Workstations |
| **Kritische Sicherheitssysteme** | ±100 Millisekunden von autoritativer Quelle | SIEM, Authentifizierung, Zertifikatsvalidierung |
| **Hochpräzisionsanforderungen** | ±10 Millisekunden von autoritativer Quelle | Finanzsysteme, regulatorische Compliance |

**Hinweise**:

- System-Eigentümer können strengere Schwellen basierend auf betrieblichen Anforderungen definieren, dürfen aber die obigen Maximalwerte für sicherheitsrelevante Systeme NICHT überschreiten
- Systeme, die akzeptable Abweichungsschwellen überschreiten, MÜSSEN Alarme für Untersuchung und Abhilfe generieren

**Umsetzungshinweis**: Plattformspezifische Konfigurationsverfahren (Linux, Windows, Netzwerkgeräte, Cloud-Plattformen, Container) sind in ISMS-IMP-A.8.17.1 (Zeitquellen-Konfiguration) dokumentiert.

## Sonderkonfigurationsfälle

**Cloud- und Virtualisierungsumgebungen**:

- Cloud-Instanzen KÖNNEN native Cloud-Anbieter-Zeitdienste (AWS Time Sync, Azure NTP, GCP NTP) verwenden
- Virtuelle Maschinen SOLLTEN sich mit dem Hypervisor-Host oder dedizierten NTP-Servern synchronisieren (nicht mit beiden gleichzeitig)
- Container-Umgebungen erben typischerweise die Hostzeit und erfordern keine unabhängige Konfiguration

**Air-Gapped-Systeme**:

- Systeme ohne Netzwerkkonnektivität zu externen Zeitquellen benötigen lokale GPS-Empfänger oder Atomuhr-Referenzen
- Alternative: Manuelle Zeitsynchronisation mit dokumentierten Verfahren und akzeptablen Abweichungsschwellen

**IoT- und eingebettete Geräte**:

- Geräte mit begrenzten Ressourcen KÖNNEN SNTP (Simple Network Time Protocol) verwenden
- Geräte ohne Zeitsynchronisationsfähigkeit erfordern eine dokumentierte Ausnahme und kompensierende Kontrollen

**Umsetzungshinweis**: Sonderkonfigurationen und Validierungsverfahren sind in ISMS-IMP-A.8.17.1 (Zeitquellen-Konfiguration) und ISMS-IMP-A.8.17.2 (Synchronisationsverifizierungsprozess) dokumentiert.

---

# Governance & Betrieb

## Rollen & Verantwortlichkeiten

**Informationssicherheitsbeauftragter (ISB)**:

- Gesamtverantwortung für Zeitsynchronisationsrichtlinie und Compliance
- Genehmigungskompetenz für Richtlinienausnahmen und Risikoakzeptanzen
- Prüfung und Genehmigung von Zeitsynchronisations-Compliance-Berichten
- Eskalationspunkt bei anhaltender Nicht-Compliance oder Infrastrukturausfällen

**Netzwerkbetrieb / IT-Infrastruktur**:

- Interne NTP-Server-Infrastruktur einsetzen und pflegen
- NTP-Server zur Synchronisation mit autoritativen Quellen konfigurieren
- Redundanz, Hochverfügbarkeit und Monitoring für NTP-Infrastruktur implementieren
- Auf NTP-Infrastrukturalarme und Serviceausfälle reagieren
- Vierteljährliche Bestandsaufnahmen der Zeitquellen durchführen
- Mit ISMS-Beauftragtem für Compliance-Berichterstattung koordinieren

**Systemadministratoren / IT-Betrieb**:

- Alle verwalteten Systeme zur Synchronisation mit genehmigten Zeitquellen konfigurieren
- Synchronisationsstatus bei der Systemeinführung verifizieren
- Auf Synchronisationsausfallalarme für verwaltete Systeme reagieren
- Synchronisationsausfälle innerhalb definierter Reaktionszeitrahmen beheben
- Systemzugang für automatisierte Sync-Status-Verifizierung bereitstellen
- Mit Security Operations für sicherheitskritische Systeme koordinieren

**Cloud-Plattform-Teams**:

- Cloud-Instanzen zur Nutzung geeigneter Zeitdienste konfigurieren
- Zeitsynchronisation in Cloud-Umgebungen verifizieren
- Cloud-spezifische Zeitsync-Konfigurationen dokumentieren
- Cloud-Zeitsync-Status in Monitoring-Systeme integrieren

**Security Operations Center (SOC)**:

- Zeitsynchronisationsstatus für sicherheitskritische Systeme überwachen
- Synchronisationsausfälle mit Auswirkungen auf den Sicherheitsbetrieb untersuchen
- Infrastrukturweite Synchronisationsausfälle eskalieren
- Zeitstempel-Konsistenz bei Sicherheitsuntersuchungen und Incident-Response validieren

**Informationssicherheit / ISMS-Beauftragter**:

- Diese Richtlinie und zugehörige Umsetzungsanleitung pflegen
- Monatliche Bewertungen des System-Synchronisationsstatus durchführen
- Summary-Dashboard-Berichte erstellen
- Behebung identifizierter Lücken und Nicht-Compliance verfolgen
- Compliance-Status ISB und Management präsentieren
- Mit Auditoren für Nachweisbereitstellung koordinieren

**System-Eigentümer**:

- Spezifische Abweichungsschwellen für eigene Systeme definieren (innerhalb Richtliniengrenzen)
- Dokumentiertes Risiko für von Zeitsynchronisationsanforderungen ausgeschlossene Systeme akzeptieren
- Abhilfepläne für Synchronisationsausfälle bei eigenen Systemen genehmigen
- Bewertungsergebnisse und Compliance-Status für eigene Systeme prüfen

**Verantwortungsmatrix**:

| Aktivität | ISB | Netzwerkbetrieb | IT-Betrieb | System-Eigentümer | ISMS-Beauftragter | SOC |
|----------|------|-----------------|-----------|-------------------|-------------------|-----|
| Richtliniengenehmigung | A | B | I | I | V | I |
| NTP-Infrastruktur-Einsatz | I | A/V | B | I | I | I |
| Client-Systemkonfiguration | I | B | A/V | B | I | I |
| Synchronisationsmonitoring | I | V | V | I | B | A |
| Compliance-Bewertung | V | B | B | I | A | B |
| Ausnahmegenehmigung | A | I | I | V | B | I |
| Incident-Response | B | V | V | I | B | A |

Legende: A = Accountable (Rechenschaftspflichtig), V = Verantwortlich, B = Beratend, I = Informiert

## Monitoring & Berichterstattung

**Monitoring-Anforderungen**:

[Organisation] überwacht die Zeitsynchronisation, um sicherzustellen, dass:

- Alle im Geltungsbereich befindlichen Systeme aktive Synchronisation mit genehmigten Zeitquellen aufrechterhalten
- Zeitabweichung innerhalb der in Abschnitt 2.3 definierten akzeptablen Schwellen bleibt
- NTP-Infrastrukturverfügbarkeit und -leistung die Serviceanforderungen erfüllen
- Synchronisationsausfälle zeitnah erkannt und behoben werden

**Schlüsselmetriken**:

| Metrik | Ziel | Compliance-Schwelle | Gilt für |
|--------|------|--------------------|---------|
| **Synchronisations-Compliance** | ≥98 % | ≥95 % | Alle im Geltungsbereich befindlichen Systeme |
| **Durchschnittliche Zeitabweichung** | <500 ms | <1 Sekunde | Allgemeine Systeme |
| **Kritische System-Abweichung** | <50 ms | <100 ms | Sicherheitskritische Systeme |
| **Kritische System-Compliance** | 100 % | 100 % | SIEM, Authentifizierung, Zertifikatssysteme |
| **Infrastrukturverfügbarkeit** | >99,9 % | >99,5 % | Interne NTP-Server |

**Definitionen**:

- **Ziel**: Betriebsziel, das einen gesunden Zustand anzeigt
- **Compliance-Schwelle**: Maximal akzeptabler Wert gemäss Abschnitt 2.3; Überschreitungen erfordern Abhilfe
- **Synchronisations-Compliance**: Prozentsatz der im Geltungsbereich befindlichen Systeme mit verifiziertem Synchronisationsstatus innerhalb der letzten 7 Tage, der die Abweichung innerhalb der anwendbaren Schwelle für die Systemkategorie zeigt

**Begründung für 95-%-Compliance-Schwelle**: Diese Schwelle erkennt an, dass vorübergehende Synchronisationsausfälle während Wartungsfenstern, Systemneustarts und Netzwerkunterbrechungen auftreten. Systeme unterhalb der Schwelle werden zur Behebung verfolgt. Anhaltende Nicht-Compliance (>30 Tage) löst Eskalation unabhängig vom Gesamtprozentsatz aus.

**Berichterstattung**:

- **Häufigkeit**: Monatliche Compliance-Berichte, vierteljährliche Executive-Zusammenfassungen
- **Zielgruppe**: ISB (monatlich), Geschäftsleitung (vierteljährlich), IT-Betrieb (kontinuierliches Monitoring)
- **Format**: Summary Dashboard mit Sync-Status, Abweichungsmetriken, Lücken und Abhilfeverfolgung
- **Eskalation**: Sofortige Benachrichtigung bei Synchronisationsausfällen kritischer Systeme, Infrastrukturausfällen oder Compliance unter 90 %

**Nachweisaufbewahrung**:

Compliance-Nachweise (Synchronisationsstatusberichte, Abweichungsmessungen, Bewertungsarbeitsbücher und Abhilfeunterlagen) MÜSSEN für mindestens **3 Jahre** aufbewahrt werden, um Auditzyklen und regulatorische Anfragen zu unterstützen. Die Nachweisaufbewahrung orientiert sich am ISO-27001-Zertifizierungszyklus und ermöglicht Trendanalysen über mehrere Bewertungszeiträume.

**Detaillierte Verfahren**: ISMS-IMP-A.8.17.2 (Synchronisationsverifizierungsprozess) enthält Monitoring-Konfiguration, Verifizierungsverfahren, Metrik-Berechnungen und Berichtsvorlagen.

## Ausnahmenmanagement

**Anforderungen an Ausnahmenanträge**:

Ausnahmen von Anforderungen der Zeitsynchronisationsrichtlinie erfordern:

- Dokumentierte geschäftliche oder technische Begründung (z. B. Air-Gapped-System ohne GPS, Anbietereinschränkung)
- Risikobewertung (Wahrscheinlichkeit und Auswirkung ungenauer Zeit, Restrisiko)
- Kompensierende Kontrollen wo machbar (manuelle Zeitverifizierung, Log-Isolierung, reduzierte Protokollierung)
- Zeitplan für vollständige Compliance (bei vorübergehender Ausnahme)
- Formale Genehmigung gemäss Kompetenzmatrix

**Genehmigungskompetenz**:

- **Technische Ausnahmen** (spezifische Systemkonfigurationen, alternative Zeitquellen): ISB-Genehmigung
- **Richtlinienebenen-Ausnahmen** (Anforderungsverzicht, dauerhafter Ausschluss): Genehmigung der Geschäftsleitung
- **Maximale Dauer**: 12 Monate für vorübergehende Ausnahmen
- **Verlängerung**: Erfordert aktualisierte Risikobewertung und Begründung

**Ausnahmen-Neubewertung**: Verlängerungen von Ausnahmen erfordern Neubewertung gegen aktuelle Richtlinienanforderungen, nicht nur Weiterführung der ursprünglichen Begründung.

**Verhinderung veralteter Ausnahmen**:
- Ausnahmen, die innerhalb von 90 Tagen vor dem jährlichen Richtlinien-Review gewährt wurden, MÜSSEN in diesem Review-Zyklus explizit neu bewertet werden
- Alle Ausnahmen, die sich ihrem 12-monatigen Ablauf nähern, MÜSSEN 60 Tage vor Ablauf zur Neubewertung vorgemerkt werden
- Der ISMS-Beauftragte MUSS einen Ausnahmenkalender mit proaktiven Verlängerungsbenachrichtigungen führen
- Abgelaufene Ausnahmen ohne Verlängerung fallen automatisch auf Standard-Richtlinienanforderungen zurück; betroffene System-Eigentümer werden 30 Tage vor Ablauf benachrichtigt

**Kompensierende Kontrollen** für ausgenommene Systeme können umfassen:

- Manuelle Zeitverifizierungsverfahren mit dokumentierter Häufigkeit
- Log-Isolierung (nicht mit anderen Systemen für forensische Analyse korreliert)
- Reduzierte Log-Aufbewahrung oder keine Protokollierungsanforderung
- Risikoakzeptanzdokumentation mit Anerkennung der Einschränkungen

**Monitoring**: Aktive Ausnahmen werden vierteljährlich vom ISB geprüft. Wirksamkeit kompensierender Kontrollen verifiziert. Ausnahmen werden widerrufen, wenn sich das Risikoprofil ändert, kompensierende Kontrollen versagen oder Compliance machbar wird.

## Incident-Response

**Sicherheitsvorfälle bei der Zeitsynchronisation** umfassen:

- Weitreichende Synchronisationsausfälle, die mehrere Systeme oder kritische Infrastruktur betreffen
- Übermässige Zeitabweichung bei sicherheitskritischen Systemen (SIEM, Authentifizierungsserver, Zertifizierungsstellen)
- Kompromittierung der NTP-Infrastruktur oder vermutete böswillige Zeitmanipulation
- Nichtverfügbarkeit von Zeitquellen oder Verlust der Redundanz
- Systeme, die trotz Abhilfemassnahmen dauerhaft keine Synchronisation herstellen können

**Reaktionsprozess**:
1. **Erkennung & Meldung**: Monitoring-Systeme generieren Alarme; SOC oder IT-Betrieb wird sofort benachrichtigt
2. **Bewertung**: Vorfallschweregradklassifizierung (Kritisch, Hoch, Mittel, Niedrig) basierend auf betroffenen Systemen und Sicherheitsauswirkungen
3. **Untersuchung**: Ursachenanalyse (NTP-Serverausfall, Netzwerkkonnektivität, Fehlkonfiguration, Infrastrukturproblem)
4. **Eindämmung**: Sofortmassnahmen basierend auf Vorfalltyp (Failover zu Backup-NTP, Dienst wiederherstellen, betroffene Systeme isolieren)
5. **Wiederherstellung**: Systemwiederherstellung, Konfigurationskorrektur und Verifizierung des Synchronisationsstatus
6. **Nach dem Vorfall**: Gewonnene Erkenntnisse, Kontrollverbesserungen und Präventivmassnahmen

**Kritische Vorfälle**:

- Synchronisationsausfälle bei sicherheitskritischen Systemen (SIEM, Authentifizierung) werden als **hochprioritäre Vorfälle** behandelt, die sofortige Reaktion erfordern
- Infrastrukturweite Ausfälle werden innerhalb von 1 Stunde an IT-Management und ISB eskaliert
- Vermutete Zeitmanipulation wird zur Sicherheitsuntersuchung an das SOC eskaliert

**Reaktionszeitrahmen**:

- **Kritische Systeme**: Untersuchung innerhalb 1 Stunde, Abhilfeplan innerhalb 4 Stunden, Lösung innerhalb 24 Stunden
- **Standardsysteme**: Untersuchung innerhalb 4 Geschäftsstunden, Abhilfeplan innerhalb 1 Geschäftstag, Lösung innerhalb 3 Geschäftstagen

**NTP-Infrastrukturklassifizierung**: Interne NTP-Server und Konnektivität zu autoritativen Zeitquellen sind als kritische Infrastruktur klassifiziert. Ausfälle folgen den Reaktionszeitrahmen für kritische Systeme.

**Detaillierte Verfahren**: ISMS-IMP-A.8.17.2 (Synchronisationsverifizierungsprozess) enthält Vorfallklassifizierungskriterien, Reaktions-Workflows, Eskalationsverfahren und Koordination mit Endpunktschutz- und Infrastrukturteams.

## Richtlinien-Governance

**Richtlinienprüfung**:

- **Häufigkeit**: Jährliches Minimum
- **Auslöser**: Regulatorische Änderungen, schwerwiegende Vorfälle, wesentliche Infrastrukturänderungen (Rechenzentrum-Migration, Cloud-Einführung), Technologieänderungen (neue Zeitsynch-Protokolle), Audit-Befunde
- **Prüfende**: ISB, IT-Security-Team, Netzwerkbetrieb, IT-Betrieb, Legal/Compliance
- **Genehmigung**: ISB (technisch), Geschäftsleitung (strategisch)

**Prüfung der Umsetzungsstandards**:

- **Häufigkeit**: Halbjährlich (Zeitsynchronisationstechnologien und -protokolle entwickeln sich regelmässig weiter)
- **Kompetenz**: IT-Security-Team und Netzwerkbetrieb schlagen Aktualisierungen vor, ISB genehmigt
- **Hinweis**: Aktualisierungen des Umsetzungsstandards (ISMS-IMP-A.8.17) erfordern keine Richtlinienrevision

**Richtlinienaktualisierungen**:

- **Geringfügig** (Klarstellungen, Referenzen, Schwellenwertsanpassungen): ISB-Genehmigung, Kommunikation innerhalb 30 Tage
- **Wesentlich** (Scope-Änderungen, neue Anforderungen, Infrastrukturänderungen): Vollständige Genehmigungskette, Umsetzungszeitplan gemäss Änderungsmanagement
- **Notfall** (kritische Sicherheitsschwachstellen, NTP-Protokollprobleme): ISB-Genehmigung, sofortige Kommunikation und Umsetzung

**Kommunikation**: Richtlinie im ISMS-Dokumentenrepository veröffentlicht. Änderungen organisationsweit an betroffenes Personal kommuniziert (Netzwerkbetrieb, Systemadministratoren, Security Operations). Schulung bei wesentlichen Änderungen der Verantwortlichkeiten oder Verfahren.

---

# Umsetzung & Referenzen

## Integration mit dem ISMS

Diese Richtlinie integriert sich in das Informationssicherheits-Managementsystem von [Organisation]:

**Risikobewertung** (ISO 27001 Clause 6.1):

- Zeitsynchronisationskontrollen basierend auf Risikobewertung von [Organisation] ausgewählt
- Systemkritikalität bestimmt Synchronisationsanforderungen und akzeptable Abweichungsschwellen
- Risikobehandlungspläne dokumentieren Zeitsynchronisationskontrollumsetzung und Ausnahmen

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Control-A.8.17-Anwendbarkeit in SoA von [Organisation] begründet
- Umsetzungsstatus durch Compliance-Bewertungen verfolgt und berichtet

**Verwandte Kontrollen**:

- A.8.21 (Network Services Security): Stellt sichere NTP-Infrastruktur bereit, von der A.8.17 abhängt
- A.8.15 (Logging): Durch synchronisierte Zeit für Log-Korrelation und forensische Analyse ermöglicht
- A.8.16 (Monitoring Activities): Schliesst Zeitsynchronisationsstatus als überwachten Parameter ein
- A.5.9 (Inventory of Information and Assets): Stellt Systeminventar für den Synchronisationsbewertungsumfang bereit
- A.8.9 (Configuration Management): NTP-Konfiguration als Teil der Systembaseline verwaltet
- A.5.28 (Collection of Evidence): Zeitsynchronisierte Protokolle liefern zulässige forensische Nachweise

## Umsetzungsressourcen

**Umsetzungsanleitung** (ISMS-IMP-A.8.17-Suite):

- ISMS-IMP-A.8.17.1: Zeitquellen-Konfiguration (autoritative Quellen, interne NTP-Server, Client-Konfiguration für Linux, Windows, Netzwerkgeräte, Cloud-Plattformen)
- ISMS-IMP-A.8.17.2: Synchronisationsverifizierungsprozess (Verifizierungsbefehle je Plattform, Abweichungsmessung, automatisierte Statuserfassung, Compliance-Bewertung)

**Bewertungswerkzeuge**:

- Excel-basierte Bewertungsarbeitsbücher mit automatisierten Compliance-Berechnungen
- Zeitquellen-Inventarvorlagen
- Systemsynchronisationsstatus-Verfolgung
- Summary Dashboard und Lückenanalyse
- Nachweisregister für Audit-Unterstützung

**Unterstützungsmaterialien**:

- Ausnahmenantragsverfahren und -vorlagen
- Incident-Response-Playbooks
- Plattformspezifische Kurzreferenzleitfäden
- Schulungsmaterialien für Netzwerkbetrieb und Systemadministratoren

## Regulatorisches Mapping

Diese Richtlinie adressiert Zeitsynchronisationsanforderungen aus:

| Anforderungskategorie | Swiss nDSG | EU GDPR | ISO 27001 | PCI DSS v4.0.1* | FINMA* | DORA/NIS2* |
|----------------------|-----------|---------|-----------|---------|--------|------------|
| Synchronisierte Zeitquellen | Art. 8 | Art. 32 | A.8.17 | Req. 10.4 | Risikobasiert | Protokollierungsfähigkeit |
| Protokollierung und Prüfpfade | Art. 8 | Art. 32 | A.8.15, A.8.17 | Req. 10 | Prüfpfad | IKT-Risikomanagement |
| Monitoring und Alarmierung | Art. 8 | Art. 32 | A.8.16, A.8.17 | Req. 10 | Monitoring | Monitoring-Massnahmen |
| Forensische Analysefähigkeit | Art. 8 | Art. 33 | A.8.17, A.5.28 | Req. 10, 12.10 | Incident-Mgmt | Incident-Response |

*Bedingte Anwendbarkeit gemäss ISMS-POL-00

**Hinweis**: Spezifische regulatorische Interpretation und Compliance-Verifizierungsverfahren sind im Summary Dashboard von ISMS-IMP-A.8.17.2 (Synchronisationsverifizierungsprozess) dokumentiert.

## Schulung & Sensibilisierung

**Sicherheitssensibilisierung** (Alle Mitarbeitenden):

- Jährliches Schulungsmodul zur Bedeutung genauer Zeit für Sicherheitsoperationen
- Verständnis der Rolle der Zeitsynchronisation bei Log-Korrelation und Incident-Response
- Verfahren zur Meldung beobachteter Zeitabweichungen

**Technische Schulung** (Netzwerkbetrieb, Systemadministratoren):

- NTP-Infrastruktur-Einsatz und -Konfiguration
- Plattformspezifische Zeitsynchronisationskonfiguration (Linux, Windows, Netzwerkgeräte, Cloud)
- Fehlerbehebung bei Synchronisationsausfällen
- Verifizierungsverfahren und Bewertungswerkzeuge
- Alarmreaktion und Abhilfeverfahren

**Betriebliche Schulung** (IT-Betrieb, Security Operations):

- Überwachung des Zeitsynchronisationsstatus
- Reaktion auf Synchronisationsalarme
- Eskalationsverfahren bei kritischen Ausfällen
- Koordination zwischen Infrastrukturteams und Sicherheitsteams

---

# Definitionen

**Autoritative Zeitquelle**: Externe Referenzuhr, die genaue Zeit aus Atomuhren, GPS-Satelliten oder gleichwertigen hochpräzisen Quellen bereitstellt (Stratum 0 oder Stratum 1).

**Stratum**: Hierarchische Stufe in der NTP-Architektur, die den Abstand von der autoritativen Zeitquelle angibt. Niedrigere Stratum-Nummer bedeutet grössere Nähe zur Referenzuhr (Stratum 0 = Atomuhr, Stratum 1 = direkt mit Stratum 0 verbunden, Stratum 2 = mit Stratum 1 synchronisiert usw.).

**Zeitabweichung**: Abweichung zwischen der Uhr eines Systems und der autoritativen Zeitquelle, gemessen in Sekunden oder Millisekunden. Akzeptable Abweichungsschwellen variieren je nach Systemkritikalität.

**Synchronisationsstatus**: Zustand, der anzeigt, ob ein System aktiv Zeitsynchronisation mit konfigurierten Zeitquellen aufrechterhält (synchronisiert, nicht synchronisiert, unbekannt).

**NTP (Network Time Protocol)**: Branchenstandard-Protokoll für Zeitsynchronisation über paketvermittelte Netzwerke (RFC 5905). Bietet hierarchische Zeitverteilung mit typischerweise wenige Dutzend Millisekunden Genauigkeit.

**Interner NTP-Server**: Von der Organisation betriebener Zeitserver (typischerweise Stratum 2), der sich mit externen autoritativen Quellen synchronisiert und Zeitdienste für interne Client-Systeme bereitstellt.

**Kritisches Sicherheitssystem**: System, bei dem Zeitgenauigkeit direkt den Sicherheitsbetrieb beeinflusst (z. B. SIEM für Log-Korrelation, Authentifizierungsserver für Token-Validierung, Zertifizierungsstellen für Zertifikatsgültigkeit).

**Zeitquellen-Redundanz**: Konfiguration mehrerer unabhängiger Zeitquellen zur Sicherstellung von Verfügbarkeit und Genauigkeit trotz Einzelquellenausfall.

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date] |
| **IT-Leiter (ITL)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Geschäftsleitung (Geschäftsleitung)** | [Name] | [Date] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen fest. Umsetzungsverfahren sind in ISMS-IMP-A.8.17 (UG/TG) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
