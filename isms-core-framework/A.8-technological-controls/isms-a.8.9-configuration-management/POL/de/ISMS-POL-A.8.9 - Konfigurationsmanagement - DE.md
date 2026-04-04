<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.9-DE:framework:POL:a.8.9 -->
**ISMS-POL-A.8.9 — Konfigurationsmanagement**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Konfigurationsmanagement |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.9 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB / Configuration Manager | Erstversion für ISO 27001:2022-Zertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Technisch: IT-Leiter (ITL)
- Operativ: Technischer Leiter (TL)
- Governance: Configuration Manager
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Rahmen zur regulatorischen Anwendbarkeit)
- ISMS-IMP-A.8.9.1-UG/TG (Basiskonfigurationsbewertung)
- ISMS-IMP-A.8.9.2-UG/TG (Change-Control-Bewertung)
- ISMS-IMP-A.8.9.3-UG/TG (Konfigurationsüberwachungsbewertung)
- ISMS-IMP-A.8.9.4-UG/TG (Security-Hardening-Bewertung)
- ISMS-CTX-A.8.9 (Konfigurationsmanagement-Referenz — NICHT ISMS)
- ISO/IEC 27001:2022 Control A.8.9

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] an Konfigurationsmanagement-Controls gemäss ISO/IEC 27001:2022 Control A.8.9 fest.

**Geltungsbereich**: Diese Richtlinie gilt für alle IT-Assets, die Konfigurationsmanagement erfordern (Compute-Infrastruktur, Netzwerkgeräte, Speichersysteme, Cloud-Dienste, Anwendungen, Sicherheits-Tools, IoT/OT-Systeme) in allen Umgebungen (Produktion, Nicht-Produktion, Cloud, On-Premises) und in allen Lebenszyklusstadien (Bereitstellung, Betrieb, Änderung, Ausserbetriebnahme).

**Zweck**: Organisationale Anforderungen an das Konfigurationsmanagement definieren. Diese Richtlinie legt WAS konfiguriert werden muss, WANN Änderungen eine Genehmigung erfordern, WER verantwortlich ist und WELCHE Standards gelten, fest. Implementierungsverfahren (WIE) sind in ISMS-IMP-A.8.9 beschrieben. Technische Referenzen befinden sich in ISMS-CTX-A.8.9 (NICHT ISMS).

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert Pflichtanforderungen gemäss ISMS-POL-00, einschliesslich des Schweizer nDSG, der EU DSGVO/GDPR (sofern anwendbar) und ISO/IEC 27001:2022. Bedingte Anforderungen (PCI DSS v4.0.1, HIPAA, FINMA, DORA, NIS2) gelten, wenn die Aktivitäten von [Organisation] deren Anwendbarkeit begründen.

---

# Control-Ausrichtung & Geltungsbereich

## ISO/IEC 27001:2022 Control A.8.9

**ISO/IEC 27001:2022 Annex A.8.9 — Konfigurationsmanagement**

> *"Konfigurationen, einschliesslich Sicherheitskonfigurationen, von Hardware, Software, Diensten und Netzwerken müssen festgelegt, dokumentiert, umgesetzt, überwacht und überprüft werden."*

**Control-Ziel**: Sichere Basiskonfigurationen festlegen, unberechtigte Änderungen verhindern, Konfigurationsabweichungen erkennen, Security Hardening durchsetzen und eine rasche Wiederherstellung ermöglichen, während der Geschäftsbetrieb unterstützt wird.

**Diese Richtlinie behandelt**:

- Festlegung und Dokumentation von Basiskonfigurationen
- Change-Control und Genehmigungsworkflows
- Konfigurationsüberwachung und Erkennung von Konfigurationsabweichungen
- Security Hardening und Compliance-Verifizierung
- Rollen und Verantwortlichkeiten im Konfigurationsmanagement
- Ausnahmen- und Incident-Management
- Integration mit Risikobewertungsprozessen

## Was diese Richtlinie leistet

Diese Richtlinie:

- **Definiert** Konfigurationsmanagement-Anforderungen entsprechend der Asset-Kritikalität
- **Etabliert** den Governance-Rahmen für Konfigurationsentscheidungen
- **Legt** Pflichtanforderungen für Baseline, Änderungen, Überwachung und Hardening fest
- **Referenziert** regulatorische Anforderungen gemäss ISMS-POL-00
- **Benennt** Rollen und Verantwortlichkeiten

## Was diese Richtlinie nicht leistet

Diese Richtlinie:

- **Gibt keine Tools oder Hersteller vor** (Auswahl basiert auf der Bewertung durch [Organisation])
- **Definiert keine systemspezifischen Baselines** (technische Standards siehe ISMS-CTX-A.8.9)
- **Enthält keine schrittweisen Verfahren** (siehe ISMS-IMP-A.8.9 Assessments)
- **Ersetzt nicht das Asset-Management** (aufbauend auf A.5.9 Asset-Inventar)
- **Definiert keine Change-System-Workflows** (Organisationen passen an bestehende ITIL/ServiceNow/Jira an)

**Begründung**: Richtlinienstabilität trotz sich entwickelnder Technologien; technische Agilität ohne Richtlinienrevision; klare Trennung von Governance und Ausführung; fokussierter Prüfungsumfang; Anpassbarkeit an verschiedene Kontexte.

## Geltungsbereich

**Asset-Typen**: Compute & Infrastruktur, Netzwerk & Konnektivität, Speicher & Backup, Cloud & SaaS, Anwendungen & Middleware, Sicherheit & Identität, IoT & OT-Systeme

**Umgebungen**: Produktion, Nicht-Produktion (Dev/Test/QA/Staging), Disaster Recovery, Training, Sandbox

**Lebenszyklusstadien**: Baseline-Definition, Bereitstellung, operative Änderungen, Überwachung, Ausserbetriebnahme

**Organisational**: Alle Mitarbeitenden von [Organisation], Auftragnehmer, Dritte, Cloud-Anbieter

**Nicht im Geltungsbereich**: BYOD, das nicht von [Organisation] verwaltet wird; öffentliche Systeme ohne Sicherheitsbedarf; temporäre Systeme mit weniger als 24 Stunden Lebenszyklus (ausser bei der Verarbeitung sensibler Daten); risikobewertete Ausnahmen mit ISB-Genehmigung

## Regulatorische Anwendbarkeit

Gemäss **ISMS-POL-00 (Rahmen zur regulatorischen Anwendbarkeit)**:

**Tier 1: Pflicht** (immer anwendbar)

| Regulierung | Anforderungen |
|-------------|---------------|
| ISO/IEC 27001:2022 | Implementierung von Control A.8.9 |
| Schweizer nDSG | Art. 8 — Datensicherheit durch Konfigurationsmanagement |
| EU DSGVO/GDPR | Art. 32 — Sicherheit der Verarbeitung (bei Verarbeitung von EU-Daten) |

**Tier 2: Bedingt** (wenn ausgelöst)

| Regulierung | Auslöser | Anforderungen |
|-------------|---------|---------------|
| PCI DSS v4.0.1 | Verarbeitung von Zahlungskarten | Anf. 1–4, 6, 11: Konfigurationsstandards |
| HIPAA | US-amerikanische Gesundheitsdaten | §164.308(a)(8), §164.310: Konfigurationscontrols |
| FINMA | Schweizer Finanzdienstleistungen | Risikobasiertes Konfigurationsmanagement |
| DORA | EU-kritische Finanzunternehmen | Art. 9, 21: IKT-Risiko & Incident-Management |
| NIS2 | Wesentliche/wichtige EU-Einrichtungen | Art. 21: Cybersecurity-Risikomanagement |

**Tier 3: Informativ**

NIST SP 800-53/128, CIS Controls v8.1, ITIL 4, COBIT 2019, CIS Benchmarks, DISA STIGs

---

# Konfigurationsmanagement-Anforderungen

## Vier-Domänen-Rahmen

[Organisation] implementiert Konfigurationsmanagement durch **vier Domänen**:

1. **Basiskonfiguration** — Sichere Baselines definieren
2. **Change Control** — Konfigurationsänderungen genehmigen
3. **Konfigurationsüberwachung** — Unbefugte Änderungen erkennen
4. **Security Hardening** — Sicherheitsstandards durchsetzen

Jede Domäne hat Richtlinienanforderungen (dieses Dokument), ein Implementations-Assessment (ISMS-IMP-A.8.9.X), Excel-Workbooks, Nachweisregister (über 100 Einträge) und eine dreistufige Genehmigung.

## Basiskonfigurationsmanagement

[Organisation] legt sichere Basiskonfigurationen fest, dokumentiert und pflegt sie.

**2.2.1 Baseline-Definition**

**Abdeckung**:

[Organisation] muss Baselines für folgendes definieren:

- Aktiv eingesetzte Asset-Typen (nicht einzelne Assets)
- Kritische Systemkonfigurationen
- Netzwerksicherheitsgeräte
- Identitäts- und Zugriffssysteme
- Sicherheits-Tooling

**Granularität**: Auf Asset-Typ-Ebene (z. B. „Windows Server 2022 DC Baseline"), NICHT auf Ebene einzelner Assets

**Begründung**: Skalierbarkeit (100 Server ≠ 100 Baselines), Compliance-Verifizierung, schnelle Bereitstellung, vereinfachte Wartung

**Komponenten**:

Baselines müssen folgendes dokumentieren:

- Betriebssystemkonfigurationen (Sicherheitseinstellungen, Dienste, Registry, Kernel-Parameter)
- Anwendungskonfigurationen
- Netzwerkkonfigurationen (IP, Routing, Firewall-Regeln, ACLs)
- Sicherheitskonfigurationen (Authentifizierung, Verschlüsselung, Logging, Audit)
- Angewendete Hardening-Standards (CIS, STIG, Herstellerleitfäden)
- Ausnahmen und Abweichungen mit Begründung
- Validierungskriterien

**2.2.2 Genehmigung**

**Workflow**: Dreistufig

- Tier 1: Technical Lead validiert Genauigkeit/Machbarkeit
- Tier 2: Security Architect validiert Hardening/Compliance
- Tier 3: Configuration Manager/ISB genehmigt

**Kriterien**: Technische Korrektheit, Security Hardening, regulatorische Compliance, operative Machbarkeit, vollständige Dokumentation

**Fristen**:

- Neue Baselines: **14 Tage**
- Aktualisierungen: **7 Tage**
- Notfall: **24 Stunden**

**2.2.3 Golden Images**

Golden Images müssen:

- Genehmigte Baselines implementieren
- In der Nicht-Produktion getestet sein
- Ausschliesslich genehmigte/lizenzierte Software enthalten
- Aktuelle Sicherheitspatches umfassen
- Versioniert und nachverfolgt sein
- Vierteljährlich aktualisiert werden

**Genehmigung**: Durch autorisiertes Personal erstellt, durch Security validiert, durch Configuration Manager genehmigt

**2.2.4 Dokumentation**

Baselines müssen dokumentiert sein mit:

- Baseline-ID (z. B. „BASE-WIN2022-DC-v1.2")
- Asset-Typ, Version, Datum, Genehmigungsstatus
- Konfigurationsparametern und -werten
- Sicherheitsbegründung
- Testvalidierung
- Abweichungsverfahren

**Repository**: Versionskontrolliert, zugangskontrolliert, wöchentlich gesichert, mit Audit-Logging

**Überprüfung**: Jährlich (mindestens), vierteljährlich (kritische Systeme), anlassbezogen (Technologie-/Schwachstellen-/regulatorische Änderungen)

**2.2.4.1 Baseline-Inventarstatus**

[Organisation] pflegt Baseline-Dokumentation für Produktions-Asset-Typen:

- **Baseline-Abdeckungsziel**: ≥ 90 % der Produktions-Asset-Typen
- **Kritische Systeme** (Tier 1/2): Prioritäts-Baselines für Betriebssysteme, Netzwerkgeräte, Cloud-Dienste, Sicherheits-Tools
- **Repository-Speicherort**: Versionskontrolliertes Repository (referenziert in ISMS-IMP-A.8.9.1)
- **Letzte Prüfung**: Configuration Manager überprüft das Baseline-Inventar vierteljährlich

**Detailliertes Inventar**: In ISMS-IMP-A.8.9.1 Workbook zur Basiskonfigurationsbewertung gepflegt.

**2.2.4.2 Baseline-Ausmusterung**

Bei Ausserbetriebnahme oder Ersatz eines Asset-Typs:
- Baseline wird mit Wirkungsdatum als „DEPRECATED" markiert
- Verbleibt 3 Jahre im Repository als historische Referenz
- Aus aktiver Compliance-Überwachung entfernt
- Ersatz-Baseline (sofern vorhanden) in der Versionskontrolle verknüpft

**2.2.5 Infrastructure as Code**

[Organisation] sollte IaC einsetzen, wo machbar:

- Baselines als Code definieren (Terraform, Ansible, CloudFormation, Kubernetes)
- In Versionskontrolle speichern (Git)
- Review-Workflows implementieren (Pull Requests, automatisiertes Testing)
- Für automatisierte Bereitstellung verwenden (CI/CD)
- Auf Fehlkonfigurationen scannen

**Governance**: IaC muss Code-Review, Branch-Schutz, automatisiertes Testing und Change-Control-Integration erfordern

## Change Control & Konfigurationsaktualisierungen

[Organisation] stellt sicher, dass alle Konfigurationsänderungen genehmigten Prozessen mit Autorisierung, Testing und Dokumentation folgen.

**2.3.1 Änderungsklassifizierung**

**Änderungstypen**:

| Typ | Definition | Genehmigung | Testing | Beispiele |
|-----|-----------|------------|---------|-----------|
| **Standard** | Vorab genehmigt, geringes Risiko, wiederholbar | Vorab genehmigt (SOP) | Gemäss SOP | Passwort-Resets, Standard-Patches, Zertifikatserneuerungen |
| **Normal** | Erfordert Bewertung und Genehmigung | CAB-Genehmigung | Erforderlich (Testumgebung) | Systemupgrades, Firewall-Regeln, Baseline-Änderungen |
| **Notfall** | Dringend bei Vorfällen/Schwachstellen | Beschleunigt (ITL/ISB) | Verkürzt/entfällt | Sicherheits-Exploits, kritische Ausfälle, kritische Fehler |

**Klassifizierungskriterien**: Auswirkung (betroffene Benutzer/Systeme), Risiko (Wahrscheinlichkeit × Konsequenz), Dringlichkeit (Geschäftszeitplan), Komplexität (Implementierungsschwierigkeit), Reversibilität (Rollback-Einfachheit)

**Notfalländerungen**:

- MÜSSEN eine echte Dringlichkeitsbegründung haben
- DÜRFEN NICHT aus Bequemlichkeit oder schlechter Planung genutzt werden
- Die Notfallklassifizierung MUSS nach der Implementierung überprüft werden
- Ziel: Weniger als 10 % aller Änderungen sollten Notfalländerungen sein

**2.3.1.1 Überprüfungsverfahren für Notfalländerungen**

Alle Notfalländerungen müssen innerhalb von **5 Arbeitstagen** einer Nachimplementierungsüberprüfung unterzogen werden:

1. **Retrospektive CAB-Überprüfung**: CAB prüft, ob die Notfallklassifizierung angemessen war
2. **Klassifizierungsanfechtung**: Wenn das CAB feststellt, dass keine echte Notlage vorlag:
   - **Erster Vorfall**: Änderungsanforderer erhält Schulung zur korrekten Klassifizierung
   - **Wiederholungsfall**: Eskalation an ITL/ISB, ggf. Einschränkung der Änderungsrechte
3. **Trendanalyse**: Configuration Manager berichtet monatlich über die Notfalländerungsrate
4. **Schwellenwertwarnung**: Wenn die Notfallrate in einem Monat 15 % übersteigt, wird ein Prozessaudit ausgelöst

**Begründung**: Verhindert, dass „Notfalländerung" zur Abkürzung bei schlechter Planung wird.

**2.3.2 Change Advisory Board (CAB)**

**Zusammensetzung**:

- **CAB-Vorsitz**: Configuration Manager oder leitende IT-Führungskraft (Entscheidungsbefugnis)
- **Kernmitglieder**: Security Architect, Network Manager, Vertreter der Application Owner
- **Wechselnde Mitglieder**: Service Owner, Herstellervertreter, Compliance Officer (nach Bedarf)

**Aufgaben**:

- Normale Änderungen prüfen und genehmigen/ablehnen/verschieben
- Änderungsauswirkungen und -risiken bewerten
- Testing- und Rollback-Pläne prüfen
- Änderungen bei Konflikten priorisieren
- Nachimplementierungsüberprüfungen für Notfalländerungen durchführen
- Änderungstrends und Prozessverbesserungen identifizieren

**Betrieb**:

- **Reguläre Sitzungen**: Wöchentlich oder zweiwöchentlich (abhängig vom Änderungsvolumen)
- **Notfallsitzungen**: Ad hoc für kritische Änderungen
- **Virtuelle Überprüfungen**: E-Mail-Genehmigung für geringfügige Änderungen
- **Dokumentation**: Sitzungsprotokolle, Anwesenheit, Entscheidungen mit Begründung

**2.3.2.1 CAB-Betriebsnachweise**

Der CAB-Betrieb muss durch folgendes belegt werden:

1. **Sitzungsprotokolle**: Für alle Sitzungen dokumentiert, einschliesslich Datum, Dauer, Teilnehmer (Quorumprüfung), geprüfte Änderungen (Änderungs-IDs, Anforderer), Entscheidungen (Genehmigung/Ablehnung/Verschiebung) mit Begründung, Aktionspunkte und Verantwortliche

2. **Anwesenheitsverfolgung**: Beteiligung der Kernmitglieder zur Einhaltung des ≥ 80 %-Ziels nachverfolgt

3. **Entscheidungsregister**: Alle CAB-Genehmigungen/-Ablehnungen im Change-Management-System protokolliert

4. **Aufbewahrung**: CAB-Unterlagen mindestens **3 Jahre** für Prüfungszwecke aufbewahrt

**Mindestsitzungshäufigkeit**: Wie oben definiert; wenn keine Änderungen ausstehen, kann die Sitzung mit dokumentierter Absage entfallen; Notfallgenehmigungen werden innerhalb von 24 Stunden rückwirkend dokumentiert

**Genehmigungskriterien**: Geschäftliche Begründung gültig, Risikobewertung vollständig und akzeptabel, Testplan ausreichend, Rollback-Plan vorhanden, Implementierungsfenster angemessen, erforderliche Ressourcen verfügbar, Abhängigkeiten koordiniert

**2.3.3 Genehmigungsworkflows**

**Genehmigungsstufen nach Risiko**:

| Risikoniveau | Genehmigungsstufen | Genehmiger | Frist |
|-------------|-------------------|-----------|-------|
| **Standard** | Keine (vorab genehmigt) | Entfällt | Sofortige Ausführung |
| **Geringes Risiko** | Einstufig | Technical Lead / System Owner | 1–2 Arbeitstage |
| **Mittleres Risiko** | Zweistufig | Technical Lead + Service Owner | 3–5 Arbeitstage |
| **Hohes Risiko** | Dreistufig | Technical Lead + Service Owner + CAB | 5–10 Arbeitstage |
| **Notfall** | Beschleunigt | ITL oder ISB (mündlich/E-Mail) | < 4 Stunden; retro CAB innerhalb von 5 Tagen |

**Notfall-Workflow**:

- Sofortige mündliche Genehmigung durch ITL/ISB/CAB-Vorsitz
- Implementierung unter Aufsicht
- Dokumentation innerhalb von **24 Stunden**
- Retrospektive CAB-Überprüfung innerhalb von **5 Arbeitstagen**

**2.3.4 Testing und Validierung**

**Testing-Anforderungen**:

Normale Änderungen müssen getestet werden:

- **Dev/Test-Umgebung**: Nicht-Produktions-Testing obligatorisch
- **Validierungskriterien**: Erfolgskriterien vor dem Testing definiert
- **Testdokumentation**: Ergebnisse und Probleme dokumentiert
- **Performance-Testing**: Keine inakzeptable Leistungsverschlechterung prüfen
- **Security-Testing**: Keine eingeführten Schwachstellen prüfen

**Testing-Ausnahmen**:

- Standard-Änderungen (folgen vorgetesteten Verfahren)
- Notfalländerungen (kritische Dringlichkeit, Risiko durch Genehmigungsbehörde akzeptiert)
- Geringrisikoänderungen (Configuration Manager hat Ausnahme vorab genehmigt)

**Post-Implementierungsvalidierung**: Funktionsprüfung, Auswirkungsverifizierung, Performance-Prüfung, Security-Prüfung, Verifizierung der Rollback-Fähigkeit

**Go/No-Go-Entscheidung**: Vor der Produktion formelle Entscheidung unter Berücksichtigung der Testergebnisse, Rollback-Bereitschaft, Business-Bereitschaft, Kommunikationsabschluss

**2.3.5 Rollback und Wiederherstellung**

**Rollback-Planung**:

Änderungen müssen einen Rollback-Plan enthalten, der folgendes dokumentiert:

- **Auslösekriterien**: Wann auszuführen (spezifische Fehlerbedingungen)
- **Verfahren**: Schrittweise Anweisungen
- **Zeitplan**: Wie lange der Rollback dauert
- **Datenverlustrisiko**: Nicht wiederherstellbare Daten
- **Backup-Verifizierung**: Backup vor der Änderung bestätigen

**Rollback-Testing**: Hochrisikoänderungen müssen in der Nicht-Produktion getestet werden, Ergebnisse dokumentiert, vor der Produktion verifiziert, innerhalb der definierten RTO ausführbar

**Rollback-Auslöser**: Änderung besteht Validierung nicht, inakzeptable Leistungsverschlechterung, eingeführte Sicherheitsschwachstelle, beeinträchtigte Geschäftsfunktionalität, Anweisung durch Genehmigungsbehörde

**Rollback-Befugnis**:

- CAB-Vorsitz oder ITL: Wesentliche Produktionsänderungen
- Service Owner: Servicespezifische Änderungen
- On-Call-Ingenieur: Ausserhalb der Geschäftszeiten (mit Managementbenachrichtigung)

**2.3.6 Kennzahlen zum Änderungserfolg**

**KPIs**:

| Kennzahl | Ziel | Messung |
|---------|------|---------|
| **Änderungserfolgsrate** | ≥ 95 % | % der Änderungen ohne Rollback |
| **Notfalländerungsrate** | < 10 % | % als Notfall klassifiziert |
| **Genehmigungs-SLA** | ≥ 90 % | % innerhalb der Frist genehmigt |
| **CAB-Anwesenheit** | ≥ 80 % | Durchschnittliche Anwesenheit der Pflichtmitglieder |
| **PIR-Abschluss** | 100 % | % mit abgeschlossenem PIR innerhalb von 5 Tagen |

**Berichterstattung**: Monatlich berechnet, an ISB/ITL gemeldet, vierteljährlich analysiert, Prozessverbesserungen bei sinkenden Kennzahlen

## Konfigurationsüberwachung & Erkennung von Konfigurationsabweichungen

[Organisation] überwacht Konfigurationen kontinuierlich und erkennt unbefugte Änderungen.

**2.4.1 Kontinuierliche Überwachung**

**Abdeckungsziele**:

| Tier | Abdeckungsziel | Häufigkeit | Akzeptable Lücke |
|------|----------------|-----------|-----------------|
| **Tier 1 (Kritisch)** | 100 % | Echtzeit oder stündlich | 0 % |
| **Tier 2 (Hoch)** | ≥ 95 % | Täglich | < 5 % |
| **Tier 3 (Mittel)** | ≥ 85 % | Wöchentlich | < 15 % |
| **Tier 4 (Niedrig)** | ≥ 70 % | Monatlich | < 30 % |

**Überwachungsfähigkeiten**:

Überwachungs-Tools MÜSSEN:

- Für Tier-1- und Tier-2-Assets eingesetzt werden
- Tatsächliche Konfiguration mit genehmigter Baseline vergleichen
- Alarme für Konfigurationsabweichungen erzeugen
- Ergebnisse für die Prüfung aufbewahren (mindestens 90 Tage)

Überwachung SOLLTE:

- Automatisiert sein (agentenbasiert oder agentenlos)
- Betriebssystemeinstellungen, Anwendungen, Netzwerkgeräte, Sicherheits-Tools abdecken
- Mit SIEM für zentrale Alarmierung integriert sein
- Häufigkeit an Asset-Kritikalität ausrichten

**Tool-Auswahl**: [Organisation] wählt Tools auf Basis der technischen Umgebung und Risikobewertung; Tools MÜSSEN Baseline-Vergleich und Konfigurationsabweichungserkennung unterstützen

**2.4.1.1 Implementierungsstatus Überwachungs-Tools**

[Organisation] hat Konfigurationsüberwachung implementiert für:
- **Tier-1-Assets**: Ziel 100 % Abdeckung mit Echtzeit- oder stündlicher Überwachung
- **Tier-2-Assets**: Ziel ≥ 95 % Abdeckung mit täglicher Überwachung

**Abdeckungslücken**: Asset-Typen ohne automatisierte Überwachung müssen dokumentiert sein mit:
- Geplantem Bereitstellungsdatum
- Interimsmassnahmen (manuelle vierteljährliche Prüfungen)
- Risikoakzeptanz durch ISB (im Risikoregister dokumentiert)

**Operative Kennzahlen**: Status der Überwachungsbereitstellung und Alarmvolumen müssen monatlich an Configuration Manager und vierteljährlich an ISB gemeldet werden.

**2.4.2 Konfigurationsabweichungserkennung und Alarmierung**

**Klassifizierung von Konfigurationsabweichungen**:

| Schweregrad | Definition | Reaktions-SLA | Beispiel |
|-------------|-----------|--------------|---------|
| **Kritisch** | Sicherheitscontrol deaktiviert | < 1 Stunde | Firewall deaktiviert, unbefugtes Admin-Konto, Verschlüsselung deaktiviert |
| **Hoch** | Sicherheitsrelevante Änderung | < 4 Stunden | Passwortrichtlinie geschwächt, Logging deaktiviert, unbefugter Dienst |
| **Mittel** | Nicht-sicherheitsrelevante Abweichung | < 24 Stunden | Dienstport geändert, unkritische Einstellung, Dokumentationsabweichung |
| **Niedrig** | Informative Abweichung | < 5 Arbeitstage | Kosmetische Änderungen, nicht-funktionale Einstellungen |

**Alarmierungsanforderungen**:

Kritische Konfigurationsabweichungen MÜSSEN:

- Sofortigen SOC-Alarm auslösen
- Enthalten: Asset-ID, erkannte Änderung, erwarteter Baseline-Wert, tatsächlicher Wert, Zeitstempel
- Bis zur Behebung verfolgt werden

Alarmweiterleitung:

- Kritisch/Hoch: SOC + Configuration Manager + System Owner
- Mittel: Configuration Manager + System Owner
- Niedrig: Configuration Manager (täglicher konsolidierter Bericht)

**2.4.3 Behebung von Konfigurationsabweichungen**

**Behebungsworkflow**:
1. **Erkennung**: Automatisierte Überwachung erkennt Abweichung
2. **Triage**: Configuration Manager untersucht Ursache
3. **Klassifizierung**: Autorisiert, nicht autorisiert oder False Positive
4. **Massnahme**:

   - Autorisiert: Baseline aktualisieren, Vorfall abschliessen
   - Nicht autorisiert: Auf Baseline zurücksetzen, Grundursache untersuchen, Vorfall abschliessen
   - False Positive: Überwachung anpassen, Vorfall abschliessen

**Behebungsfristen**:

| Schweregrad | Behebungs-SLA | Eskalation |
|-------------|--------------|-----------|
| **Kritisch** | < 4 Stunden | Eskalation an ISB bei Nichtbehebung |
| **Hoch** | < 24 Stunden | Eskalation an Configuration Manager |
| **Mittel** | < 5 Arbeitstage | Eskalation an IT Operations Manager |
| **Niedrig** | < 30 Tage | Bestmögliche Umsetzung |

**Nachverfolgung**: Alle Vorfälle durch Konfigurationsabweichungen im Incident-Management protokolliert, bis zum Abschluss verfolgt, wiederkehrende Abweichungen lösen Grundursachenanalyse aus, Trends monatlich analysiert

**2.4.3.1 Eskalationsbefugnis bei Behebung von Konfigurationsabweichungen**

Bei Nichteinhaltung des Behebungs-SLA:

**Schritt 1**: Configuration Manager eskaliert an den Vorgesetzten des System Owner
**Schritt 2**: Wenn nach 48 Stunden noch nicht behoben, prüft der ISB und kann:
- **Option A**: Ausnahme mit kompensierenden Controls gewähren (maximal 30 Tage)
- **Option B**: Notfalländerung zur Erzwingung der Behebung einleiten
- **Option C**: Nicht-konformes System aus der Produktion isolieren (bei inakzeptablem Risiko)

**Letzte Instanz**: Der ISB ist befugt, Systeme bei ungelösten kritischen Konfigurationsabweichungen aus der Produktion zu entfernen, wenn ein inakzeptables Risiko besteht.

**Dokumentation**: Alle Eskalationen und Behebungen im Konfigurationsabweichungs-Vorfallsprotokoll dokumentiert.

## Security Hardening & Compliance

[Organisation] wendet branchenübliche Security-Hardening-Standards an und gewährleistet Compliance.

**2.5.1 Auswahl des Hardening-Standards**

**Auswahlkriterien**: Asset-Typ/Technologie, regulatorische Anforderungen (gemäss ISMS-POL-00), branchenübliche Best Practices, organisationaler Risikoappetit, operative Machbarkeit

**Anerkannte Standards** (Beispiele):

| Standard | Herausgeber | Verwendung |
|---------|------------|-----------|
| **CIS Benchmarks** | Center for Internet Security | Primäre Referenz für gängige Plattformen |
| **DISA STIGs** | Defense Information Systems Agency | Hohe Sicherheit, Regierung/Verteidigung |
| **Herstellerleitfäden** | Microsoft, AWS, Azure, GCP usw. | Cloud- und Herstellerplattformen |
| **NIST Baselines** | NIST SP 800-53, 800-128 | Framework-Ausrichtung |

**Priorisierung**: Regulatorisch vorgeschrieben → Branchenspezifisch → CIS Benchmarks → Herstellerleitfäden → Eigene Standards

**2.5.2 Hardening-Implementierung**

**Implementierungsanforderungen**:

Alle Produktions-Assets müssen:

- Vor der Produktivbereitstellung gemäss anwendbaren Standards gehärtet sein
- Kritische Sicherheitscontrols zu ≥ 95 % implementiert haben
- Vor der Produktivaufnahme auf Hardening geprüft worden sein
- Hardening-Lücken dokumentiert und risikobewertet haben

Hardening sollte:

- Automatisiert sein (Golden Images, IaC, Konfigurationsmanagement-Tools)
- Zunächst in der Nicht-Produktion validiert werden
- Nach wesentlichen Änderungen erneut verifiziert werden

**Abdeckungsziele**:

| Tier | Kritische Controls | Gesamtcompliance | Akzeptable Lücken |
|------|-------------------|-----------------|-------------------|
| **Tier 1** | 100 % | ≥ 95 % | 0 kritische Lücken |
| **Tier 2** | ≥ 95 % | ≥ 90 % | < 5 kritische Lücken |
| **Tier 3** | ≥ 90 % | ≥ 80 % | < 10 kritische Lücken |
| **Tier 4** | ≥ 80 % | ≥ 70 % | Bestmögliche Umsetzung |

**Kritische Controls**: Je Standard definiert (Authentifizierung, Verschlüsselung, Logging, Zugangskontrolle, Patch-Management)

**2.5.3 Compliance-Verifizierung**

**Verifizierungsanforderungen**:

Hardening-Compliance muss:

- Mindestens jährlich für alle Produktionssysteme bewertet werden
- Automatisierte Scan-Tools verwenden, sofern verfügbar
- Compliance-Rate je Standard dokumentieren
- Lücken identifizieren und Behebung empfehlen

**Häufigkeit automatisierter Scans**:

| Asset-Tier | Scan-Häufigkeit | Manuelle Verifizierung (wenn Automatisierung nicht verfügbar) |
|------------|----------------|--------------------------------------------------------------|
| **Tier 1 (Kritisch)** | Vierteljährlich (automatisiert) | Halbjährlich (manuell) |
| **Tier 2 (Hoch)** | Halbjährlich (automatisiert) | Jährlich (manuell) |
| **Tier 3/4 (Mittel/Niedrig)** | Jährlich (automatisiert) | Jährlich (manuell) |

**Implementierungsstatus**: Stand des Richtlinienversionsdate müssen automatisierter Scan-Abdeckungsstatus und Interims-Handbewertungen in ISMS-IMP-A.8.9.4 dokumentiert sein

**Verifizierungs-Tools**: OpenSCAP, Nessus, Qualys, Tenable, Cloud-native Tools, Herstellerbewertungstools

**Compliance-Berichterstattung**: Berichte müssen enthalten: Gesamtcompliance-%, kritische Lücken, Hochrisikolücken, Behebungsempfehlungen; für Prüfungszwecke aufbewahrt (mindestens 3 Jahre)

**2.5.4 Lückenbehebung**

**Priorisierung der Behebung**:

| Risikoniveau | Frist | Ausnahmegenehmigungsbefugnis |
|-------------|-------|------------------------------|
| **Kritisch** | < 30 Tage | Nur ISB |
| **Hoch** | < 90 Tage | Configuration Manager + Security Architect |
| **Mittel** | < 180 Tage | Configuration Manager |
| **Niedrig** | Bestmögliche Umsetzung | Configuration Manager |

**Behebungsprozess**: Lückenidentifikation → Risikobewertung → Behebungsplanung → Implementierung → Verifizierung → Ausnahmemanagement (sofern nicht machbar)

**Nachverfolgung**: Alle Lücken im Behebungsregister, dem System Owner mit Frist zugewiesen, Status monatlich an ISB gemeldet, Überfälligkeit löst Eskalation aus

---

# Rollen und Verantwortlichkeiten

[Organisation] definiert klare Verantwortlichkeiten für das Konfigurationsmanagement.

**3.1 RACI-Matrix**

| Aktivität | ISB | ITL/TL | Config Mgr | Sec Architect | Sys Owner | Sys Admin | CAB | Auditor |
|-----------|------|---------|------------|---------------|-----------|-----------|-----|---------|
| **Richtliniengenehmigung** | A | B | V | B | I | I | I | I |
| **Baseline-Definition** | B | I | A | V | B | V | I | I |
| **Baseline-Genehmigung** | A | B | V | V | B | I | I | I |
| **Änderungsgenehmigung (Normal)** | I | I | A | B | B | V | V | I |
| **Änderungsimplementierung** | I | I | B | I | A | V | I | I |
| **Überwachungskonfiguration** | B | I | A | V | B | V | I | I |
| **Behebung von Konfigurationsabweichungen** | I | I | B | B | A | V | I | I |
| **Hardening-Implementierung** | B | I | B | A | B | V | I | I |
| **Compliance-Bewertung** | A | B | V | V | B | B | I | V |
| **Prüfungsunterstützung** | B | I | V | B | B | B | I | A |

**Legende**: V=Verantwortlich, A=Accountable, B=Beratend, I=Informiert

**3.2 Rollenbeschreibungen**

**Informationssicherheitsbeauftragter (ISB)**:

- **Accountable** für Konfigurationsmanagement-Richtlinie und -Programm
- Genehmigt Baselines, Hardening-Standards und Ausnahmen
- Überprüft Compliance-Kennzahlen und autorisiert Behebungsprioritäten
- Letzte Eskalationsinstanz für Konfigurationsvorfälle

**IT-Leiter (ITL) / Technischer Leiter (TL)**:

- **Beratend** bei Richtlinien- und Baseline-Entscheidungen
- Genehmigt Notfalländerungen
- Stellt Ressourcen für das Konfigurationsmanagement-Programm bereit
- Überprüft Kennzahlen zum Änderungserfolg

**Configuration Manager**:

- **Accountable** für den täglichen Betrieb des Konfigurationsmanagements
- Vorsitz im CAB
- Verwaltet Baseline-Repository und Versionskontrolle
- Koordiniert Überwachungs- und Behebungsaktivitäten
- Berichtet Kennzahlen an ISB/ITL

**Security Architect**:

- **Verantwortlich** für die Auswahl von Hardening-Standards
- Überprüft Baselines auf Sicherheits-Compliance
- Definiert Sicherheitsanforderungen für Konfigurationen
- Validiert Sicherheitscontrols in Änderungen

**System Owner**:

- **Accountable** für Konfigurationscompliance der eigenen Systeme
- Genehmigt Änderungen, die eigene Systeme betreffen
- Gewährleistet zeitnahe Behebung von Konfigurationsabweichungen
- Stellt Ressourcen für die Hardening-Implementierung bereit

**Systemadministrator / DevOps-Ingenieur**:

- **Verantwortlich** für die Implementierung von Baselines und Änderungen
- Führt Einrichtung der Konfigurationsüberwachung durch
- Setzt genehmigte Änderungen um
- Triagiert Konfigurationsabweichungs-Alarme
- Dokumentiert den Konfigurationszustand

**Change Advisory Board (CAB)**:

- **Accountable** für Änderungsgenehmigungsentscheidungen
- Überprüft Normale Änderungen auf Auswirkung und Risiko
- Validiert Testing- und Rollback-Pläne
- Führt Nachimplementierungsüberprüfungen durch

**Interne/externe Prüfer**:

- **Verantwortlich** für unabhängige Verifizierung
- Prüfen Richtlinienkonformität
- Überprüfen Nachweise und Dokumentation
- Berichten Befunde an die Geschäftsleitung

---

# Richtlinien-Governance

**4.1 Richtlinienlebenszyklus**

**Überprüfungsplan**: Jährliche Überprüfung (mindestens); anlassbezogene Überprüfungen bei regulatorischen Änderungen, Sicherheitsvorfällen, Technologieänderungen

**Überprüfungsprozess**: Configuration Manager koordiniert, Fachexperten liefern Beiträge, ISB genehmigt Aktualisierungen, Geschäftsleitung ratifiziert wesentliche Änderungen

**Versionskontrolle**: Alle Richtlinienversionen **3 Jahre** aufbewahrt; Änderungshistorie dokumentiert; Stakeholder über Aktualisierungen informiert

**4.2 Ausnahmemanagement**

**Ausnahmeantragsverfahren**:

Ausnahmen von Konfigurationsanforderungen müssen:

- Schriftlich mit geschäftlicher Begründung beantragt werden
- Risikobewertung und kompensierende Controls enthalten
- Durch Security Architect geprüft werden
- Durch die zuständige Instanz genehmigt werden (gemäss Abschnitt 2.5.4)
- Ein definiertes Ablaufdatum haben (maximal 12 Monate)
- Jährlich auf Verlängerung oder Widerruf überprüft werden

**Ausnahmenerfassung**: Alle Ausnahmen im Ausnahmenregister, vierteljährlich überprüft, abgelaufene Ausnahmen lösen Behebung oder Verlängerung aus

**4.3 Compliance-Messung**

**Compliance-Kennzahlen**:

| Kennzahl | Ziel | Häufigkeit | Verantwortlich |
|---------|------|-----------|---------------|
| **Baseline-Abdeckung** | ≥ 90 % der Asset-Typen | Monatlich | Configuration Manager |
| **Änderungserfolgsrate** | ≥ 95 % | Monatlich | CAB-Vorsitz |
| **Notfalländerungsrate** | < 10 % aller Änderungen | Monatlich | CAB-Vorsitz |
| **CAB-Sitzungscompliance** | 100 % dokumentiert | Monatlich | CAB-Vorsitz |
| **Behebungs-SLA-Konfigurationsabweichungen** | ≥ 90 % innerhalb SLA | Monatlich | Configuration Manager |
| **Hardening-Compliance** | ≥ 90 % kritische Controls | Vierteljährlich | Security Architect |
| **CAB-Anwesenheit** | ≥ 80 % Kernmitglieder | Monatlich | CAB-Vorsitz |
| **Ausnahmen-Überprüfungscompliance** | 100 % jährlich überprüft | Vierteljährlich | Configuration Manager |
| **Abschluss der RCA bei fehlgeschlagenen Änderungen** | 100 % | Monatlich | CAB-Vorsitz |

**Hinweis**: Alle Änderungen, die einen Rollback erfordern, müssen eine Grundursachenanalyse innerhalb von 10 Arbeitstagen abgeschlossen haben, dem CAB vorgestellt und Korrekturmassnahmen nachverfolgt werden.

**Berichterstattung**: Kennzahlen-Dashboard monatlich durch ISB, vierteljährlich durch Geschäftsleitung überprüft

**4.4 Konsequenzen bei Nichtkonformität**

**Progressives Vorgehen**:

- **Erster Verstoss**: Verwarnung und Korrekturmassnahmenplan
- **Wiederholte Verstösse**: Managementskalation und Leistungsüberprüfung
- **Schwerwiegende Verstösse**: Disziplinarmassnahmen gemäss HR-Richtlinie
- **Systemische Nichtkonformität**: Programmprüfung und Prozessverbesserung

**Schwerwiegende Verstösse**: Unbefugte Änderungen an Tier-1-Systemen, Deaktivierung von Sicherheitscontrols, Umgehung des Change Control, Verschweigen von Konfigurationsabweichungen

**4.5 Kontinuierliche Verbesserung**

**Verbesserungsquellen**:

- Gelehrte Lektionen aus Vorfällen
- Analyse von Änderungstrends
- Prüfungsbefunde
- Branchenübliche Best Practices
- Technologieentwicklung

**Verbesserungsprozess**: Möglichkeiten identifizieren, Machbarkeit bewerten, Änderungen pilotieren, Verbesserungen implementieren, Wirksamkeit messen

---

# Definitionen

**Basiskonfiguration**: Dokumentierter Satz von Sicherheits- und operativen Konfigurationsparametern für einen Asset-Typ, der als Referenz für Bereitstellung und Compliance-Verifizierung dient.

**Change Advisory Board (CAB)**: Funktionsübergreifendes Team, das für die Bewertung, Genehmigung und Überprüfung von Konfigurationsänderungen verantwortlich ist, um Risiken zu minimieren und Koordination zu gewährleisten.

**Änderungserfolgsrate**: Prozentsatz der implementierten Änderungen, die das beabsichtigte Ergebnis ohne Rollback erzielen; Messgrösse für die Wirksamkeit des Änderungsprozesses.

**Konfigurationsabweichung**: Abweichung der tatsächlichen Systemkonfiguration von der genehmigten Baseline, die auf unbefugte Änderungen oder Dokumentationslücken in der Baseline hinweisen kann.

**Configuration Item (CI)**: Asset, Dienst oder Komponente, das/die durch Konfigurationsmanagement verwaltet wird und in der CMDB mit definierten Attributen und Beziehungen verfolgt wird.

**Configuration Management Database (CMDB)**: Repository zum Speichern von Konfigurationsbaselines, Golden Images, Asset-Konfigurationen, Änderungshistorie und Beziehungen zwischen CIs.

**Notfalländerung**: Dringende Konfigurationsänderung zur Behebung eines kritischen Sicherheitsvorfalls, Dienstausfalls oder einer Schwachstelle, die einem beschleunigten Genehmigungsverfahren mit nachträglicher Überprüfung folgt.

**Golden Image**: Vorkonfiguriertes Systemabbild, das die genehmigte Basiskonfiguration implementiert und für die schnelle konsistente Bereitstellung neuer Systeme verwendet wird.

**Hardening**: Prozess der Absicherung von Systemkonfigurationen durch Implementierung anerkannter Sicherheitsstandards (CIS Benchmarks, DISA STIGs) und Entfernung nicht benötigter Dienste, Konten und Funktionen.

**Infrastructure as Code (IaC)**: Praxis der Verwaltung von Konfigurationsbaselines und Infrastrukturbereitstellung durch maschinenlesbaren Code, der in Versionskontrollsystemen gespeichert wird.

**Normale Änderung**: Konfigurationsänderung, die eine individuelle Bewertung und CAB-Genehmigung erfordert und dem Standardprozess für Change Control mit Testing und Rollback-Planung folgt.

**Rollback**: Prozess der Rückgängigmachung einer Konfigurationsänderung zur Wiederherstellung des Systemzustands vor der Änderung, der ausgeführt wird, wenn die Änderung Validierungskriterien nicht erfüllt oder ein inakzeptables Risiko einführt.

**Standard-Änderung**: Vorab genehmigte, risikoarme, wiederholbare Konfigurationsänderung nach dokumentiertem Verfahren, die ohne individuelle CAB-Überprüfung ausgeführt werden kann.

---

# Genehmigungsnachweis

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date] |
| **IT-Leiter (ITL)** | [Name] | [Date] |
| **Technischer Leiter (TL)** | [Name] | [Date] |
| **Configuration Manager** | [Name] | [Date] |
| **Geschäftsleitung** | [Name] | [Date] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen fest. Implementierungsverfahren sind in ISMS-IMP-A.8.9 (UG/TG) dokumentiert. Technische Referenzinformationen befinden sich in ISMS-CTX-A.8.9 (NICHT ISMS).*

<!-- QA_VERIFIED: 2026-03-28 -->
