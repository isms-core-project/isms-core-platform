<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.15-DE:framework:POL:a.8.15 -->
**ISMS-POL-A.8.15 — Protokollierungsrichtlinie**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Protokollierungsrichtlinie |
| **Dokumententyp** | ISMS-Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.15 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|-----------|
| 1.0 | [Date] | ISB | Erstveröffentlichung Richtlinienrahmen |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Technische Überprüfung: Information Security Manager
- Betriebliche Überprüfung: Security Operations Center (SOC) Lead / IT-Betrieb Manager
- Datenschutzüberprüfung: Datenschutzbeauftragter (DSB)
- Compliance-Überprüfung: Legal/Compliance Officer
- Abschliessende Entscheidungsbefugnis: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Rahmen für regulatorische Anwendbarkeit)
- ISMS-IMP-A.8.15.1-UG/TG (Beurteilung Protokollquellen-Inventar)
- ISMS-IMP-A.8.15.2-UG/TG (Beurteilung Protokollsammlung und -zentralisierung)
- ISMS-IMP-A.8.15.3-UG/TG (Beurteilung Protokollschutz und -aufbewahrung)
- ISMS-IMP-A.8.15.4-UG/TG (Beurteilung Protokollanalyse und -überprüfung)
- ISMS-REF-A.8.15 (Protokollierungs-Standards-Referenz)
- ISMS-POL-A.8.16 (Überwachungsaktivitäten)
- ISMS-POL-A.8.17 (Zeitsynchronisation)
- ISMS-POL-A.5.24 (Vorfallmanagement)

---

# Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] an die Ereignisprotokollierung zur Unterstützung der Vorfallserkennung, forensischer Untersuchungen, Compliance-Verpflichtungen und Rechenschaftspflicht gemäss ISO/IEC 27001:2022 Steuerung A.8.15 fest.

**Zweck**: Organisatorische Anforderungen für die Implementierung und Governance von Ereignisprotokollierungssteuerungen festlegen. Diese Richtlinie legt fest:

- WAS protokolliert werden muss
- WIE LANGE Protokolle aufbewahrt werden müssen
- WER für das Protokollmanagement rechenschaftspflichtig ist
- WANN Protokolle überprüft werden müssen

Implementierungsverfahren (WIE Protokolle technisch konfiguriert werden) sind separat in ISMS-IMP-A.8.15 (UG/TG-Varianten) dokumentiert.

**ISO/IEC 27001:2022 Steuerung A.8.15 — Protokollierung**:
> *Ereignisprotokolle, die Benutzeraktivitäten, Ausnahmen, Fehler und Informationssicherheitsereignisse aufzeichnen, sollten erzeugt, aufbewahrt und regelmässig überprüft werden.*

---

# Anwendungsbereich

## Im Geltungsbereich liegende Systeme und Aktivitäten

**Diese Richtlinie gilt für**:

- Alle Informationssysteme, Applikationen und Infrastrukturkomponenten
- Netzwerkgeräte (Router, Switches, Firewalls, VPN-Gateways, Load Balancer)
- Sicherheits-Tools (SIEM, IDS/IPS, Anti-Malware, Endpunktschutz, DLP)
- Datenbanksysteme und Datenspeicherplattformen
- Cloud-Dienste und SaaS-Applikationen
- Authentifizierungs- und Identitätsmanagementsysteme
- Administrative Zugangsinfrastruktur (Jump Hosts, Bastion Hosts, PAM)

**Abgedeckte Deploymentmodelle**:

- On-Premises-Infrastruktur
- Cloud-Umgebungen (öffentlich, privat, hybrid)
- Extern gehostete Dienste Dritter

## Ausserhalb des Geltungsbereichs

- Geschäftsapplikations-Prüfpfade ohne Sicherheitsbezug
- Finanztransaktionsprotokolle für Buchhaltungszwecke (durch Finanzsteuerungsrichtlinien abgedeckt)
- Echtzeit-Überwachung und Alarmierung (geregelt durch ISMS-POL-A.8.16)

---

# Richtlinienanweisungen

## Anforderungen an die Ereignisprotokollierung

[Organisation] muss sicherheitsrelevante Ereignisse über alle im Geltungsbereich liegenden Systeme protokollieren.

**Verbindliche Ereigniskategorien**:

- **Authentifizierungsereignisse**: Anmeldeversuche (Erfolg und Misserfolg), Abmeldungen, Kontosperrungen, Passwortänderungen, MFA-Ereignisse
- **Autorisierungsereignisse**: Zugang zu sensitiven Daten, Rechteerweiterung, Änderungen der Zugangskontrolle
- **Administrative Aktionen**: Konfigurationsänderungen, Benutzerkonten-Management, Rechtevergaben, Änderungen der Sicherheitsrichtlinien
- **Sicherheitsereignisse**: Malware-Erkennung, Eindringalarme, Firewall-Sperrungen, DLP-Alarme
- **Systemereignisse**: Start/Herunterfahren, Dienststatus-Änderungen, Fehler, Ressourcenerschöpfung
- **Netzwerkereignisse**: Firewall-Treffer, VPN-Verbindungen, Segmentierungsgrenzen-Traversierungen
- **Applikationsereignisse**: Fehler, Ausnahmen, API-Authentifizierung, Ausführung privilegierter Funktionen

**Anforderungen an Protokollinhalte**: Jeder Protokolleintrag muss Zeitstempel, Benutzeridentität, Quellsystem, Ereignistyp, Ergebnis und relevanten Kontext enthalten. Detaillierte Feldspezifikationen sind in ISMS-REF-A.8.15 dokumentiert.

## Anforderungen an den Protokollschutz

[Organisation] muss Protokolle vor unberechtigtem Zugriff, Veränderung und Löschung schützen.

**Zugangssteuerungsgrundsätze**:

- Lesezugang auf autorisiertes Personal mit berechtigtem Bedarf beschränkt
- Schreibzugang auf Protokollierungsdienste beschränkt
- Administrativer Zugang erfordert erhöhte Rechte mit Aufgabentrennung
- Protokolladministrator-Aktionen müssen separat protokolliert werden

**Integritätsschutz**:

- Protokolle müssen für Sicherheitsereignisse innerhalb von 5 Minuten an die zentralisierte Sammlung weitergeleitet werden
- Zentralisierte Sammlung verhindert lokale Manipulation
- Kryptografischer oder Write-Once-Schutz sollte für Compliance-kritische Protokolle implementiert werden

**Sichere Übertragung**:

- Protokolle müssen verschlüsselt mit TLS 1.2 oder höher übertragen werden

## Anforderungen an die Protokollaufbewahrung

[Organisation] muss Protokolle für Zeiträume aufbewahren, die Untersuchungen und Compliance ausreichend unterstützen.

| Protokollkategorie | Online-Speicherung | Archiv-Speicherung | Gesamtaufbewahrung |
|-------------------|-------------------|-------------------|-------------------|
| Sicherheitsereignisse, Authentifizierung, administrative Aktionen | 12 Monate | 7 Jahre | 8 Jahre |
| Datenbankprotokolle (Zugang zu sensitiven Daten) | 12 Monate | 7 Jahre | 8 Jahre |
| Applikations-, Netzwerk- und Systemprotokolle | 6 Monate | 1 Jahr | 1,5 Jahre |

**Regulatorische Mindestanforderungen** (wenn anwendbar gemäss ISMS-POL-00):

- PCI DSS v4.0.1: 12 Monate Online
- HIPAA: 6 Jahre gesamt
- SOX: 7 Jahre gesamt

**Konfliktlösung**: Wenn mehrere Regulierungen auf dasselbe System anwendbar sind, gilt die **strengste Anforderung**. Beispiel: System, das sowohl Kartenzahlungsdaten als auch Gesundheitsdaten verarbeitet → 12 Monate Online (PCI DSS v4.0.1) + 7 Jahre Archiv (SOX/nDSG) = 8 Jahre Gesamtaufbewahrung.

**Speicherung und Entsorgung**:

- Mehrstufige Speicherarchitektur (Hot, Warm, Cold) optimiert Kosten und Zugänglichkeit
- Protokolle müssen nach Ablauf der Aufbewahrungsfrist mit genehmigten Methoden sicher gelöscht werden
- Legal-Hold-Verfahren müssen Löschung während Rechtsstreitigkeiten oder Untersuchungen aussetzen

## Anforderungen an die Protokollüberprüfung

[Organisation] muss Protokolle regelmässig überprüfen und analysieren, um Sicherheitsvorfälle zu erkennen.

| Überprüfungstyp | Häufigkeit | Verantwortlichkeit |
|----------------|-----------|-------------------|
| Automatisierte Analyse | Kontinuierlich (24/7) | SIEM / SOC |
| Tägliche Überprüfung | Jeden Geschäftstag | SOC-Analysten |
| Wöchentliche Überprüfung | Wöchentlich | Sicherheitsteam |
| Monatliche Überprüfung | Monatlich | Information Security Manager |
| Vierteljährliche Überprüfung | Vierteljährlich | ISB |

**Automatisierte Erkennung** muss implementiert sein für:

- Brute-Force-Angriffe
- Rechteerweiterung
- Datenexfiltrationsindikatoren
- Malware-Indikatoren
- Richtlinienverstösse

**Kontinuitätsanforderungen für Überprüfungen**:

- SOC muss 24/7-Abdeckung durch Schichtrotation oder Bereitschaftsdienst aufrechterhalten
- Stellvertretende Prüfer müssen für jede Rolle bestimmt werden (im SOC-Dienstplan dokumentiert)
- Abwesenheiten über 5 Geschäftstage erfordern formelle, im Zugangsmanagementsystem dokumentierte Delegation
- Falls geplante Überprüfung nicht rechtzeitig abgeschlossen werden kann, muss der Information Security Manager innerhalb von 24 Stunden benachrichtigt werden
- SOC-Dienstplan und Backup-Zuweisungen müssen monatlich überprüft werden

## Datenschutz und Datenschutzrecht

[Organisation] muss Protokollierung in Übereinstimmung mit Datenschutzbestimmungen implementieren.

**Verbotene Daten in Protokollen**:

- Passwörter (Klartext oder verschlüsselt)
- Vollständige Kreditkartennummern (abgekürzte PANs gestattet: erste 6, letzte 4)
- Kartenprüfnummern (CVV/CVC)
- Nationalidentifikatoren (vollständige AHV-Nummer, Passnummer)
- Vollständige Inhalte persönlicher Kommunikationen (Betreffzeilen/Metadaten gestattet)
- Biometrische Vorlagen (rohe biometrische Daten verboten; pseudonymisierte Bezeichner gestattet)
- Weitere regulierte besondere Kategorien, die vom DSB gemäss DSGVO Art. 9 oder nDSG Art. 5 identifiziert wurden

**Autoritative Liste des DSB**: Der DSB muss eine autoritative Liste verbotener Datentypen führen, die vierteljährlich überprüft und bei neuen Datenkategorien aktualisiert wird.

**Datenschutzgrundsätze**:

- Erhebung personenbezogener Daten in Protokollen minimieren
- Pseudonymisierung einsetzen, wo durchführbar
- Benutzer über Überwachung durch Acceptable-Use-Richtlinie informieren
- DSB muss Protokollierungsimplementierungen mit Bezug zu personenbezogenen Daten überprüfen

---

# Rollen und Verantwortlichkeiten

## Verantwortungsmatrix

| Rolle | Verantwortlichkeit |
|-------|-------------------|
| **Geschäftsleitung** | Richtlinie genehmigen; angemessene Ressourcen sicherstellen; Restrisiken akzeptieren |
| **ISB** | Gesamtrichtlinienwirksamkeit; Ausnahmen genehmigen; Protokollierungsanforderungen basierend auf Risiko definieren |
| **Information Security Manager** | Richtlinienanforderungen implementieren; Protokollierungsaktivierung koordinieren; Ausnahmen verwalten |
| **SOC-Team** | Tägliche Protokollüberprüfung; Alarminvestigation; Vorfallseskalation; 24/7-Abdeckung |
| **IT-Betrieb** | Systemprotokollierung konfigurieren; Protokollweiterleitung sicherstellen; Zeitsynchronisation aufrechterhalten |
| **System-/Applikationseigentümer** | Geeignete Protokollierung aktivieren; Protokollereignisse dokumentieren; Onboarding koordinieren |
| **Protokolladministratoren** | SIEM-Plattform verwalten; Sammlung und Aufbewahrung konfigurieren; Aufgabentrennung aufrechterhalten |
| **DSB** | Datenschutz-Compliance überprüfen; Beratung zur Handhabung personenbezogener Daten; Betroffenenanfragen beantworten |
| **Alle Mitarbeitenden** | Acceptable-Use-Richtlinie einhalten; verstehen, dass Aktivitäten protokolliert werden |

---

# Regulatorische Compliance

## Verbindliche Compliance (Tier 1)

| Regulierung | Anforderung | Referenz |
|-------------|-------------|---------|
| **ISO/IEC 27001:2022** | Ereignisprotokolle müssen erzeugt, aufbewahrt und regelmässig überprüft werden | Anhang A.8.15 |
| **Schweizer nDSG** | Geeignete technische Massnahmen einschliesslich Protokollierung für Datensicherheit | Art. 8 |
| **EU DSGVO** | Protokollierung als Sicherheitsmassnahme zum Schutz personenbezogener Daten | Art. 32 |

## Bedingte Compliance (Tier 2)

Gilt wenn gemäss ISMS-POL-00 ausgelöst:

| Regulierung | Auslöser | Hauptprotokollierungsanforderungen |
|-------------|---------|-----------------------------------|
| **DORA** | EU-Finanzdienstleistungen | IKT-Vorfallserkennung und -management |
| **NIS2** | Wichtige/kritische Einrichtung (EU) | Protokollierung für Cybersicherheits-Risikomanagement |
| **PCI DSS v4.0.1** | Kartenzahlungsverarbeitung | Req. 10: Umfassende Prüfpfade, 12 Monate Online-Aufbewahrung |
| **HIPAA** | US-Gesundheitsdaten | §164.312(b): Prüfsteuerungen, 6 Jahre Aufbewahrung |
| **SOX** | Finanzberichterstattung börsennotierter Unternehmen | Prüfpfade für Finanzsysteme, 7 Jahre Aufbewahrung |

---

# Ausnahmemanagement

## Ausnahmeprozess

**Anforderungen**:

- Formeller Ausnahmeantrag mit Geschäftsbegründung
- Risikobeurteilung erforderlich
- Kompensierende Massnahmen müssen implementiert werden
- Maximale Dauer: 12 Monate (verlängerbar)
- ISB-Genehmigung erforderlich; Genehmigung der Geschäftsleitung für Hochrisikoausnahmen

**Gültige Ausnahmetypen**:

- Legacy-Systeme, die keine Protokollweiterleitung unterstützen
- Leistungssensitive Systeme, bei denen Protokollierung den Betrieb beeinträchtigt
- Drittanbietersysteme ohne Protokollierungsfähigkeiten
- Kostenprohibitive Implementierungen

## Ausnahmedokumentation

Jede Ausnahme muss dokumentieren:

- Betroffenes System und Anforderung
- Geschäftliche Begründung
- Risikobeurteilung
- Kompensierende Massnahmen
- Dauer und Verlängerungsbedingungen
- Genehmigungsunterschriften

---

# Vorfallreaktion

## Protokollierungsbezogene Vorfälle

Folgendes muss als Sicherheitsvorfall klassifiziert werden:

- Protokollmanipulation erkannt
- Protokollsammlungsausfall über 15 Minuten für kritische Systeme
- Nicht autorisierter Protokollzugang
- Erschöpfung der Protokollspeicherkapazität
- SIEM-Plattform kompromittiert

## Vorfallklassifizierung und Eskalation

| Vorfalltyp | Schweregrad | Erste Reaktionszeit | Eskalationspfad |
|------------|-------------|--------------------|--------------------|
| Protokollmanipulation erkannt | Kritisch | Sofort (5 Min.) | SOC → Info Sec Manager → ISB → Geschäftsleitung |
| Protokollsammlungsausfall (kritische Systeme) | Hoch | 15 Minuten | SOC → Info Sec Manager → ISB (wenn > 1 Std.) |
| Nicht autorisierter Protokollzugang | Hoch | 30 Minuten | SOC → Info Sec Manager |
| SIEM-Plattform kompromittiert | Kritisch | Sofort (5 Min.) | SOC → ISB → Geschäftsleitung |
| Protokollspeicher zu 90% voll | Mittel | 4 Stunden | Protokolladministratoren → IT-Betrieb Manager |

## Reaktionsanforderungen

- ISB-Benachrichtigung innerhalb von 15 Minuten bei kritischen Vorfällen
- Forensische Sicherung: Sofort bei allen Kritisch- und Hoch-Vorfällen
- Ursachenanalyse: Innerhalb von 48 Stunden bei Kritisch, 5 Tage bei Hoch
- Integration mit ISMS-POL-A.5.24-Vorfallreaktionsrahmen
- Nachvorfall-Überprüfung für alle kritischen Vorfälle innerhalb von 7 Tagen

---

# Richtlinien-Governance

## Überprüfungsplan

| Überprüfungstyp | Häufigkeit | Zuständigkeit |
|----------------|-----------|--------------|
| Richtlinienüberprüfung | Mindestens jährlich | ISB + Geschäftsleitung |
| Implementierungsstandards | Vierteljährlich | Sicherheitsteam, ISB-Genehmigung |

**Überprüfungsauslöser**:

- Regulatorische Änderungen
- Wesentliche Protokollierungsvorfälle
- Organisatorische Änderungen
- Revisionsergebnisse
- Technologieänderungen

## Aktualisierungsklassifizierung

| Typ | Beispiele | Genehmigung |
|-----|----------|-------------|
| **Geringfügig** | Klarstellungen, Referenzen, Korrekturen | ISB |
| **Wesentlich** | Neue Anforderungen, Umfangsänderungen, Aufbewahrungsänderungen | ISB + Geschäftsleitung |
| **Notfall** | Kritische Sicherheitsprobleme, dringende regulatorische Anforderungen | ISB mit Geschäftsleitungsbenachrichtigung |

---

# Implementierungsressourcen

## Unterstützende Dokumente

| Dokument | Zweck |
|----------|-------|
| **ISMS-IMP-A.8.15.1-UG/TG** | Beurteilung Protokollquellen-Inventar |
| **ISMS-IMP-A.8.15.2-UG/TG** | Beurteilung Protokollsammlung und -zentralisierung |
| **ISMS-IMP-A.8.15.3-UG/TG** | Beurteilung Protokollschutz und -aufbewahrung |
| **ISMS-IMP-A.8.15.4-UG/TG** | Beurteilung Protokollanalyse und -überprüfung |
| **ISMS-REF-A.8.15** | Protokollierungs-Standards-Referenz (Formate, Schemata, technische Spezifikationen) |

## Verwandte Steuerungen

| Steuerung | Integration |
|-----------|------------|
| **A.8.16 (Überwachung)** | Echtzeit-Überwachung verwendet Protokolle für Alarmierung |
| **A.8.17 (Zeitsynchronisation)** | Genaue Zeitstempel für Protokollkorrelation |
| **A.5.24 (Vorfallmanagement)** | Protokolle liefern Vorfallserkennungs- und Untersuchungsnachweise |
| **A.5.17-18 (Authentifizierung/Zugang)** | Authentifizierungs- und Autorisierungsereignisse protokolliert |

---

# Compliance-Verifizierung

## Beurteilungsplan

| Domäne | Häufigkeit | Verfahren | Nachweisausgabe |
|--------|-----------|-----------|----------------|
| Protokollquellen-Inventar | Jährlich (vierteljährliche Updates) | ISMS-IMP-A.8.15.1-UG/TG | Inventar-Arbeitsmappe mit Abdeckungs-% |
| Sammlung und Zentralisierung | Jährlich (vierteljährliche Kennzahlen) | ISMS-IMP-A.8.15.2-UG/TG | Weiterleitungs-Compliance-Bericht |
| Schutz und Aufbewahrung | Halbjährlich | ISMS-IMP-A.8.15.3-UG/TG | Aufbewahrungs-Compliance-Arbeitsmappe |
| Analyse und Überprüfung | Vierteljährlich | ISMS-IMP-A.8.15.4-UG/TG | Überprüfungsabschluss-Protokolle |

## Nachweis-Speicherort und Zugang

**Nachweis-Repository-Struktur**:
- **Beurteilungsarbeitsmappen**: [GRC-Plattform / SharePoint] → ISMS → Steuerungen → A.8.15 → [Beurteilungsname]
- **SIEM-Konfigurationsprotokolle**: CMDB → Protokollierung → [Systemname]
- **Protokollaufbewahrungsberichte**: SIEM → Berichte → Compliance → Protokoll_Aufbewahrung_Monatlich
- **Überprüfungsabschluss-Protokolle**: SIEM → Fälle → [Überprüfungsperiode] ODER SOC-Ticketing-System → A.8.15-Überprüfungen
- **Ausnahmeregister**: [GRC-Plattform / SharePoint] → ISMS → Ausnahmen → A.8.15
- **Lückenregister**: [GRC-Plattform] → ISMS → Lückenregister (Filter: Steuerung = A.8.15)

**Zugangsprozess**:
- Interne Prüfer: Self-Service-Zugang via GRC-Plattform-Rolle „Prüfer"
- Externe Prüfer: Evidenzpaket-Anfrage über ISB oder Information Security Manager
- Nachweisverantwortlicher: Information Security Manager (primär), ISB (Backup)
- Reaktionsfrist: Nachweis innerhalb von 2 Geschäftstagen nach Anfrage bereitgestellt

**Nachweis-Aufbewahrung**: Beurteilungsnachweis muss mindestens 3 Jahre aufbewahrt werden (entspricht ISO 27001-Zertifizierungszyklus).

## Lücken- und Befundmanagement

**Lückenidentifizierung und -erfassung**:
- Erkenntnisse aus Protokollbeurteilungen (IMP-A.8.15.1-4) müssen im organisatorischen Lückenregister (ISMS-REG-LÜCKEN oder GRC-Plattform-Äquivalent) erfasst werden
- Jeder Befund muss enthalten:
  - Steuerungs-ID: A.8.15
  - Befundbeschreibung (spezifische nicht erfüllte Anforderung)
  - Schweregrad: Kritisch / Hoch / Mittel / Niedrig
  - Betroffene Systeme/Umfang
  - Grundursache (falls identifiziert)
  - Verantwortliche Partei (Eigentümer für Behebung)
  - Ziel-Abschlussdatum
  - Aktueller Status (Offen / In Bearbeitung / Abgeschlossen)

**Anforderungen für Lückenschliessung**:
- Lückenschliessung erfordert Nachweisverifizierung durch den Information Security Manager
- Akzeptierte Nachweistypen: Aktualisierte Beurteilungsarbeitsmappe, SIEM-Konfigurationsänderungsprotokoll, Überprüfungsprotokolle
- Hoch-/Kritisch-Lücken erfordern ISB-Genehmigung für Schliessung
- Geschlossene Lücken bleiben für Revisionsspur im Register (mindestens 3 Jahre)

**Eskalation und Berichterstattung**:
- Offene Lücken müssen monatlich dem ISB berichtet werden (als Teil der Sicherheitskennzahlen)
- Hoch-Schweregrad-Lücken, die über 30 Tage offen sind, müssen an die Geschäftsleitung eskaliert werden
- Kritisch-Lücken, die über 14 Tage offen sind, erfordern eine Geschäftsleitungsentscheidung: Risiko akzeptieren ODER Notfallressourcen zuweisen

---

# Genehmigungsprotokoll

| Rolle | Name | Unterschrift | Datum |
|-------|------|-------------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | | [Date] |
| **Information Security Manager** | [Name] | | [Date] |
| **Security Operations Center (SOC) Lead** | [Name] | | [Date] |
| **IT-Betrieb Manager** | [Name] | | [Date] |
| **Datenschutzbeauftragter (DSB)** | [Name] | | [Date] |
| **Legal/Compliance Officer** | [Name] | | [Date] |
| **Geschäftsleitung** | [Name] | | [Date] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen für Ereignisprotokollierungssteuerungen fest. Implementierungsverfahren sind in ISMS-IMP-A.8.15 (UG/TG) dokumentiert. Technische Standards sind in ISMS-REF-A.8.15 dokumentiert.*

<!-- QA_VERIFIED: 2026-03-29 -->
