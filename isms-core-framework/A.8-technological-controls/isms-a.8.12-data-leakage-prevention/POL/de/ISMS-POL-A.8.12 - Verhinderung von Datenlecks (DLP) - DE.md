<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.12-DE:framework:POL:a.8.12 -->
**ISMS-POL-A.8.12 — Richtlinie zur Verhinderung von Datenlecks (DLP)**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Verhinderung von Datenlecks (DLP) |
| **Dokumententyp** | ISMS-Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.12 |
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
| 1.0 | [Date] | ISB | Erstveröffentlichung modularer Richtlinienrahmen (14 Dokumente) |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Implementierungsstatus**:
- **Deployment-Status**: [Vollständig operationell / Teildeployment / Geplant]
- **In Betrieb seit**: [Datum, an dem DLP-Infrastruktur operationell wurde]
- **Aktuelle Abdeckung**: [Prozentsatz]% der organisatorischen Ausgangskanäle geschützt
- **Letzte Beurteilung**: [Datum der letzten IMP-A.8.12-3-Kanalabdeckungsbeurteilung]
- **Nächste Beurteilung**: [Datum gemäss vierteljährlichem Überprüfungsplan]

*Hinweis: Implementierungsstatus wird in Übersichts-Dashboards verfolgt und der Geschäftsleitung quartalsweise berichtet.*

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL)
- Compliance: Datenschutzbeauftragter (DSB) / Legal/Compliance Officer
- Abschliessende Entscheidungsbefugnis: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Rahmen für regulatorische Anwendbarkeit)
- ISMS-IMP-A.8.12.1-UG/TG (DLP-Infrastrukturbeurteilung)
- ISMS-IMP-A.8.12.2-UG/TG (Datenklassifizierungsbeurteilung)
- ISMS-IMP-A.8.12.3-UG/TG (Kanalabdeckungsbeurteilung)
- ISMS-IMP-A.8.12.4-UG/TG (Überwachungs- und Reaktionsbeurteilung)
- ISO/IEC 27001:2022 Steuerung A.8.12
- Schweizerisches DSG (Datenschutzgesetz)
- EU DSGVO (Datenschutz-Grundverordnung)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] an DLP-Steuerungen (Data Leakage Prevention) zum Schutz sensitiver Informationen vor unbefugter Offenlegung, Übertragung oder Exfiltration gemäss ISO/IEC 27001:2022 Steuerung A.8.12 fest.

**Anwendungsbereich**: Diese Richtlinie gilt für alle als INTERN, Vertraulich oder Eingeschränkt klassifizierten Informationsassets; alle Datenausgangskanäle einschliesslich E-Mail, Web, Endpunkte, Netzwerk, Cloud und Mobil; alle Mitarbeitenden der Organisation; sowie alle DLP-Technologien unabhängig vom Deploymentmodell.

**Zweck**: Organisatorische Anforderungen für DLP-Steuerungsimplementierung und -Governance festlegen. Diese Richtlinie legt WAS an Datenleckage-Schutz erforderlich ist und WER rechenschaftspflichtig ist, fest. Implementierungsverfahren (WIE) sind separat in ISMS-IMP-A.8.12 (UG/TG-Varianten) dokumentiert. DLP-Steuerungen adressieren sowohl bösartige Exfiltration (Insider-Bedrohungen, kompromittierte Systeme) als auch versehentliche Offenlegung (Benutzerfehler, Fehlkonfiguration).

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00 (Rahmen für regulatorische Anwendbarkeit), einschliesslich Schweizer nDSG (Mitarbeiterüberwachung Art. 328b OR), EU DSGVO (rechtmässige Verarbeitung Art. 5, Sicherheit Art. 32) und ISO/IEC 27001:2022. Bedingte branchenspezifische Anforderungen (PCI DSS v4.0.1, FINMA, DORA, NIS2, HIPAA) gelten, wo die Geschäftstätigkeit von [Organisation] die Anwendbarkeit auslöst.

---

# Steuerungsausrichtung und Anwendungsbereich

## ISO/IEC 27001:2022 Steuerung A.8.12

**ISO/IEC 27001:2022 Anhang A.8.12 — Verhinderung von Datenlecks**

> *Massnahmen zur Verhinderung von Datenlecks sollten auf Systeme, Netzwerke und andere Geräte angewendet werden, die sensitive Informationen verarbeiten, speichern oder übertragen.*

**Steuerungsziel**: Organisatorische Richtlinie für DLP-Steuerungen zur Verhinderung unbefugter Datenexfiltration in der gesamten Informationsverarbeitungsumgebung von [Organisation] festlegen.

**Diese Richtlinie adressiert**:

- Anforderungen an Datenklassifizierung und -identifizierung für den DLP-Schutzumfang
- Anforderungen an Kanalschutz über alle Datenausgangspfade (E-Mail, Web, Endpunkt, Netzwerk, Applikation, Mobil)
- Anforderungen an Überwachung und Erkennung zur Identifizierung von Leckageversuchen
- Verfahren zur Vorfallreaktion und Behebung bei DLP-Ereignissen
- Organisatorische Rollen und Verantwortlichkeiten für DLP-Governance
- Ausnahme- und Vorfallmanagement-Rahmenwerke
- Integration mit den Risikobeurteilungs- und -behandlungsprozessen von [Organisation]
- Rechtliche und regulatorische Compliance-Anforderungen (Mitarbeiterüberwachung, Verhältnismässigkeit, Transparenz)

## Was diese Richtlinie leistet

Diese Richtlinie:

- **Definiert** DLP-Steuerungsanforderungen in Übereinstimmung mit Datenklassifizierung und organisatorischer Risikobereitschaft
- **Etabliert** Governance-Rahmen für DLP-Entscheidungsfindung und Rechenschaftspflicht
- **Legt fest** verbindliche Schutzanforderungen für sensitive Informationen über alle Ausgangskanäle
- **Verweist** auf anwendbare regulatorische Anforderungen gemäss ISMS-POL-00 (Tier 1/2/3-Rahmen)
- **Identifiziert** organisatorische Rollen und Verantwortlichkeiten für DLP-Implementierung
- **Adressiert** rechtliche Anforderungen für Mitarbeiterüberwachung (Schweizer DSG Art. 328b OR, DSGVO Art. 88)

## Was diese Richtlinie NICHT leistet

Diese Richtlinie legt NICHT fest:

- **Technische Implementierungsdetails** (siehe ISMS-IMP-A.8.12 Implementierungsanleitungen)
- **Spezifische DLP-Regeln, Muster oder Erkennungslogik** (siehe ISMS-IMP-A.8.12-2 Datenklassifizierungsbeurteilung)
- **Systemspezifische Konfigurationsverfahren** (siehe ISMS-IMP-A.8.12-1 Infrastrukturbeurteilung)
- **DLP-Technologien oder -Anbieter** (Technologieauswahl basierend auf Risikobeurteilung von [Organisation])
- **Risikobeurteilung** (DLP-Steuerungen werden basierend auf Risikobehandlung von [Organisation] ausgewählt)
- **Detaillierte Vorfallreaktionsverfahren** (siehe ISMS-IMP-A.8.12-4 Überwachungs- und Reaktionsbeurteilung)
- **Ausnahmeantrag-Workflows** (siehe ISMS-IMP-A.8.12 Ausnahmeverfahren)

**Begründung**: Die Trennung von Richtlinienanforderungen und Implementierungsanleitung ermöglicht:

- Richtlinienstabilität trotz sich entwickelnder Bedrohungslandschaft und DLP-Technologieänderungen
- Technische Agilität für DLP-Lösungsupdates, Regelanpassungen und Technologiemigration ohne Richtlinienrevision
- Klare Unterscheidung zwischen Governance (Richtlinie) und Ausführung (Implementierung)
- Fokussierter Revisionsumfang (Prüfer prüfen Richtliniencompliance, nicht technische DLP-Regelkonfiguration)

## Anwendungsbereich

**Diese Richtlinie gilt für**:

- Alle als **INTERN, Vertraulich oder Eingeschränkt** klassifizierten Informationsassets gemäss Datenklassifizierungsschema von [Organisation]
- Alle Systeme, Applikationen, Netzwerke, Endpunkte und Dienste, die organisatorische Informationen verarbeiten, speichern oder übertragen
- Alle Datenausgangskanäle: E-Mail (SMTP, Webmail), Web (HTTP/HTTPS), Endpunkte (USB, lokaler Speicher), Netzwerk (Dateiübertragungsprotokolle), Cloud-Dienste (SaaS, Cloud-Speicher), Mobilgeräte (dienstlich und BYOD), Applikations-APIs
- Alle Mitarbeitenden der Organisation (Angestellte, Auftragnehmer, Zeitarbeitskräfte) mit Zugang zu organisatorischen Informationen
- Alle Drittdienstleister und Cloud-Dienste, die organisatorische Daten verarbeiten
- Alle Deploymentmodelle (On-Premises-Infrastruktur, hybride Umgebungen, Cloud-native Dienste)

**Ausserhalb des Geltungsbereichs**:

- Öffentliche Informationen (als Öffentlich klassifizierte Daten erfordern keinen DLP-Schutz)
- Informationssicherheitssteuerungen ohne Bezug zu Datenexfiltration (Zugangskontrolle, Authentifizierung, Patching durch andere ISO 27001-Steuerungen abgedeckt)
- Physische Sicherheit von Papierdokumenten (geregelt durch ISMS-POL-A.7.X Physische Sicherheit)
- Sicherungs- und Archivierungsprozesse (geregelt durch ISMS-POL-A.8.13 Informationssicherung)
- Datenaufbewahrung und -löschung (geregelt durch ISMS-POL-A.8.10 Informationslöschung)
- Datenmaskierung und -anonymisierung (geregelt durch ISMS-POL-A.8.11 Datenmaskierung)

## Regulatorische Anwendbarkeit

Regulatorische Anforderungen werden gemäss **ISMS-POL-00 (Rahmen für regulatorische Anwendbarkeit)** kategorisiert.

**Tier 1: Verbindliche Compliance**

| Regulierung | Anwendbarkeit | Kernanforderungen |
|-------------|--------------|------------------|
| **Schweizer nDSG** | Alle Schweizer Operationen | Art. 26 (Pflichten des Verantwortlichen), Art. 328b OR (Transparenz und Verhältnismässigkeit der Mitarbeiterüberwachung) |
| **EU DSGVO** | Bei Verarbeitung personenbezogener Daten von EU-Betroffenen | Art. 5 (Rechtmässige Verarbeitung, Zweckbindung), Art. 32 (Sicherheitsmassnahmen), Art. 88 (Verarbeitung im Beschäftigungskontext) |
| **ISO/IEC 27001:2022** | Zertifizierungsumfang | Steuerung A.8.12 — Dokumentierte Richtlinie, Implementierungsnachweis, Wirksamkeitsüberwachung |

**Tier 2: Bedingte Anwendbarkeit**

Gilt nur, wenn spezifische Geschäftsbedingungen die Anwendbarkeit auslösen:

| Regulierung | Auslösebedingung | DLP-Anforderungen |
|-------------|-----------------|------------------|
| **PCI DSS v4.0.1** | Verarbeitung von Kartenzahlungsdaten | Req. 12.10 (Vorfallreaktion), Schutz von Karteninhaberdaten vor unbefugter Offenlegung |
| **FINMA** | Beaufsichtigtes Schweizer Finanzinstitut | Betriebliche Resilienz, Datenschutzmassnahmen nach Risikobeurteilung, Vorfallmeldung |
| **DORA** | EU-Finanzdienstleistungsunternehmen | IKT-Risikomanagement, Vorfallmeldung, Resilienztest |
| **NIS2** | Wichtige/kritische Einrichtung (EU) | Sicherheitsmassnahmen für Netz- und Informationssysteme, Vorfallmeldung |
| **HIPAA** | Verarbeitung von US-Gesundheitsdaten (PHI) | PHI-Schutz, Meldung von Datenpannen (gilt NUR wenn [Organisation] Covered Entity oder Business Associate) |

**Tier 3: Informelle Anleitung**

Diese Rahmenwerke informieren die Implementierung, begründen aber keine verbindliche Compliance, es sei denn, vertraglich vereinbart:

- NIST SP 800-53 Rev. 5 (SC-7: Boundary Protection, AC-4: Information Flow Enforcement, SI-4: System Monitoring)
- CIS Controls v8.1 (Steuerung 13: Netzwerküberwachung und -abwehr)
- ISO/IEC 27002:2022 (Abschnitt 8.12 detaillierte Implementierungsanleitung)
- OWASP (Data Loss Prevention Guide)
- Cloud Security Alliance (CSA) — Data Security Lifecycle
- SANS Institute — DLP Best Practices

**Compliance-Feststellung**: [Organisation] ermittelt anwendbare Tier-2-Regulierungen durch regelmässige Geschäftsaktivitätsbeurteilungen durch Legal/Compliance, ISB und DSB. Bei Überschneidung mehrerer Regulierungen gelten die strengsten Anforderungen.

---

# DLP-Anforderungsrahmen

## Anforderungen an Datenklassifizierung und -identifizierung

[Organisation] implementiert DLP-Steuerungen basierend auf der Datenklassifizierung, um den Schutz auf sensitive Informationen zu konzentrieren.

**Klassifizierungsbasierter Schutz**:

| Klassifizierungsstufe | DLP-Schutzanforderung | Implementierungspriorität | Mindeststeuerungen |
|----------------------|----------------------|--------------------------|-------------------|
| **Eingeschränkt** | Vollständige DLP-Überwachung und Blockierung über alle Kanäle | **Verbindlich** | E-Mail-DLP, Endpunkt-DLP, Netzwerk-DLP, Cloud-DLP, Mobil-DLP |
| **Vertraulich** | DLP-Überwachung und Blockierung auf Hochrisikokanälen | **Verbindlich** | E-Mail-DLP, Endpunkt-DLP, Netzwerk-DLP (Minimum) |
| **INTERN** | DLP-Überwachung (Erkennung ohne automatische Blockierung) | Empfohlen | E-Mail-Überwachung, Netzwerkflussüberwachung |
| **Öffentlich** | Keine DLP-Steuerungen erforderlich | N/A | Nicht anwendbar |

**Datenidentifizierungsmethoden**:

[Organisation] implementiert mehrere Identifizierungsmethoden zur Erkennung sensitiver Informationen:

| Methode | Beschreibung | Implementierungspriorität | Anwendungsfälle |
|---------|-------------|--------------------------|----------------|
| **Inhaltsinspektion** | Mustererkennung, Regex, Schlagworterkennung | **Verbindlich** | PII (AHV-Nr., Kreditkarten), Zugangsdaten, API-Schlüssel |
| **Dokumentenbezeichnung** | In Dateien eingebettete Klassifizierungsmetadaten | **Verbindlich** | Bezeichnete Dokumente (Vertraulich, Eingeschränkt) |
| **Kontextanalyse** | Quellsystem, Benutzerrolle, Zielanalyse | **Verbindlich** | Datenbankexporte, HR-Systemdaten, Finanzdaten |
| **Machine Learning** | KI-basierte Erkennung sensitiver Inhalte | Empfohlen | Unstrukturierte Daten, geistiges Eigentum, Geschäftsgeheimnisse |
| **Fingerprinting** | Hash-basierte Dokumentenverfolgung | Empfohlen | Quellcode, Designdokumente, strategische Pläne |

**Sensitive Datenkategorien**:

[Organisation] schützt folgende Datenkategorien durch DLP-Steuerungen:

| Datenkategorie | Beispiele | Regulatorischer Treiber | Erkennungsmethode |
|---------------|----------|------------------------|------------------|
| **Personenbezogene Daten (PII)** | Namen, Adressen, Nationalidentifikatoren, Telefonnummern | Schweizer nDSG, DSGVO | Inhaltsinspektion, Kontextanalyse |
| **Finanzdaten** | Bankkonten, Kreditkarten, Zahlungsdaten | PCI DSS v4.0.1 (bedingt) | Inhaltsinspektion, Mustererkennung |
| **Gesundheitsdaten** | Krankenakten, Gesundheitsinformationen | HIPAA (bedingt) | Kontextanalyse, Bezeichnung |
| **Authentifizierungszugangsdaten** | Passwörter, API-Schlüssel, Tokens, Zertifikate | ISO 27001 A.5.17 | Inhaltsinspektion, Mustererkennung |
| **Geistiges Eigentum** | Quellcode, Designs, Patente, Geschäftsgeheimnisse | Geschäftsrisiko | Fingerprinting, Kontextanalyse |
| **Kundendaten** | Kundenlisten, Verträge, Preisgestaltung | Vertragliche Verpflichtungen | Kontextanalyse, Bezeichnung |
| **Mitarbeiterdaten** | HR-Akten, Lohnbuchhaltung, Leistungsbeurteilungen | Schweizer nDSG Art. 328b | Kontextanalyse, Bezeichnung |

**Inventar sensitiver Daten**: [Organisation] führt ein quantifiziertes Inventar sensitiver Daten, die DLP-Schutz erfordern, dokumentiert in IMP-A.8.12-2 Datenklassifizierungsbeurteilung:
- **Eingeschränkte Daten**: [Volumen TB] über [Anzahl] Systeme
- **Vertrauliche Daten**: [Volumen TB] über [Anzahl] Systeme
- **Letzte Inventaraktualisierung**: [Datum]
- **Inventarabgleich**: Vierteljährlich mit Asset-Inventar (A.5.9)

**Implementierungshinweis**: Spezifische Datenmuster, Regex-Regeln, Klassifizierungsbezeichnungen und Machine-Learning-Modelle sind in ISMS-IMP-A.8.12-2 (Datenklassifizierungsbeurteilung) dokumentiert. Organisationen passen die Erkennungslogik an ihr spezifisches Dateninventar und ihre Risikobeurteilung an.

## Anforderungen an den Kanalschutz

[Organisation] implementiert DLP-Steuerungen über alle Datenausgangskanäle zur Verhinderung unbefugter Informationsoffenlegung.

**Erforderliche Kanalabdeckung**:

| Kanal | Schutzanforderung | Implementierungspriorität | Mindeststandard |
|-------|-------------------|--------------------------|----------------|
| **E-Mail (SMTP)** | Inhaltsinspektion, Anhang-Scanning, Empfängervalidierung | **Verbindlich** | Blockierung/Alarmierung bei sensitiven Daten an externe Empfänger |
| **Webmail (HTTP/HTTPS)** | TLS-Inspektion, Inhaltsanalyse, Upload-Blockierung | **Verbindlich** | Gmail, Outlook.com, Yahoo Mail Überwachung |
| **Web-Upload** | Datei-Upload-Blockierung, Cloud-Speicher-Überwachung | **Verbindlich** | Cloud-Speicher (Dropbox, Google Drive, private Konten) |
| **Web-Formulare** | Formularfeld-Überwachung, Einfügen-Verhinderung | Empfohlen | Stellengesuche, Umfragen, externe Formulare |
| **Endpunkt USB** | Wechseldatenträger-Überwachung, Kopierblocker | **Verbindlich** | USB-Sticks, externe Festplatten, SD-Karten |
| **Lokaler Endpunktspeicher** | Dateioperationen-Überwachung, Shadow-Copy-Erkennung | **Verbindlich** | Lokale Festplatte, Netzwerkfreigaben, Offline-Speicher |
| **Endpunkt Drucken** | Druckauftrag-Überwachung, Drucken-zu-PDF-Blockierung | Empfohlen | Physisches Drucken, virtuelle Drucker |
| **Endpunkt Screenshots** | Screenshot-Erkennung, Zwischenablagen-Überwachung | Risikobasiert | Bildschirmaufnahme-Tools, Zwischenablagen-Exporte |
| **Netzwerk-Dateiübertragung** | FTP, SFTP, SCP, rsync-Überwachung | **Verbindlich** | Dateiübertragungsprotokoll-Blockierung/-Überwachung |
| **Cloud-Applikationen** | SaaS-DLP, CASB-Integration, API-Überwachung | **Verbindlich** | Microsoft 365, Google Workspace, Salesforce |
| **Mobilgeräte** | Mobiler DLP-Agent, MDM-Integration | **Verbindlich** | Dienstliche Mobilgeräte, BYOD (risikobasiert) |
| **Applikations-APIs** | API-Gateway-Überwachung, Datenexport-Erkennung | Empfohlen | REST, GraphQL, SOAP APIs |

**Kanalspezifische Anforderungen**:

**E-Mail-DLP**:

- Alle ausgehenden E-Mails scannen (SMTP und Webmail)
- Sensitive Inhalte in Nachrichtentext und Anhängen erkennen
- Empfängerdomänen validieren (intern vs. extern, vertrauenswürdig vs. nicht vertrauenswürdig)
- Verschlüsselung unterstützen (S/MIME, PGP) für genehmigte sensitive E-Mails
- Nachrichten mit Eingeschränkten Daten an externe Empfänger blockieren oder in Quarantäne stellen
- Bei Vertraulichen Daten an externe Empfänger warnen (richtlinienbasierte Blockierung oder Überwachung)

**Endpunkt-DLP**:

- Dateioperationen überwachen (Kopieren, Verschieben, Umbenennen, Löschen)
- Nicht autorisierte Verwendung von Wechseldatenträgern blockieren
- Shadow-IT-Applikationen erkennen (nicht genehmigte Cloud-Speicher, Messaging)
- Mit Endpoint Protection Platform (EPP/EDR) integrieren
- Offline-Betrieb unterstützen (Richtlinien bei Netzwerktrennung durchsetzen)

**Netzwerk-DLP**:

- Netzwerkverkehr an Ausgangspunkten überwachen (Internet-Gateway, Cloud-Verbindungen)
- Verschlüsselten Verkehr inspizieren (TLS-Inspektion, wo rechtlich zulässig)
- Datenexfiltration über verdeckte Kanäle erkennen (DNS-Tunneling, ICMP-Exfiltration)
- Mit Firewall, Proxy und SIEM-Systemen integrieren

**Cloud-DLP**:

- Cloud Access Security Broker (CASB) Integration für SaaS-Überwachung
- API-basiertes DLP für Cloud-Speicher (Microsoft OneDrive, Google Drive, Dropbox)
- Datenweitergabe und externe Zusammenarbeitsüberwachung
- Cloud-zu-Cloud-Datentransfer-Erkennung

**Mobil-DLP**:

- Mobile Device Management (MDM) Integration
- App-Level-DLP für containerisierte Unternehmens-Apps
- E-Mail- und Dokumentenfreigabeüberwachung
- BYOD risikobasierte Steuerungen (Containerisierung, bedingter Zugang)

**Abdeckungsverifizierung**: [Organisation] muss die DLP-Abdeckung durch technische Tests und Netzwerktopologie-Mapping verifizieren. Testmethodik und Häufigkeit in ISMS-IMP-A.8.12-3 (Kanalabdeckungsbeurteilung) definiert.

**Aktueller Abdeckungsstatus** (gemäss letzter IMP-A.8.12-3-Beurteilung):
- **E-Mail**: [Prozentsatz]% des SMTP-Verkehrs, [Prozentsatz]% des Webmails
- **Endpunkt**: [Prozentsatz]% der verwalteten Geräte
- **Netzwerk**: [Prozentsatz]% der Internet-Ausgangsbandbreite
- **Cloud**: [Liste abgedeckter SaaS-Applikationen]
- **Mobil**: [Prozentsatz]% der Unternehmensgeräte, [Prozentsatz]% BYOD (falls zutreffend)
- **Letztes Beurteilungsdatum**: [Datum]
- **Nächste fällige Beurteilung**: [Datum]

**Dokumentation von Abdeckungslücken**: Jede Abdeckung unter 100% muss in der Kanalabdeckungsbeurteilung dokumentiert werden mit:
- Beschreibung der Lücke und betroffene Systeme/Benutzer
- Risikobeurteilung der Lücke
- ISB-Genehmigung zur Akzeptanz (falls zutreffend)
- Behebungsplan mit Zeitplan (falls nicht akzeptiert)

**Zulässige Abdeckungsausnahmen**:

- Gastnetzwerke (begrenzte DLP-Steuerungen, dokumentierte Risikoakzeptanz)
- Dedizierte B2B-Partnerverbindungen (dokumentiert, risikobewertet, ISB-genehmigt)
- Air-Gapped-Netzwerke ohne Internetverbindung (DLP nicht anwendbar)
- Spezifische Benutzergruppen mit dokumentierten und genehmigten Ausnahmen (Geschäftsleitung, Rechtsbeistand — risikobasiert)

## Anforderungen an Überwachung und Erkennung

[Organisation] implementiert kontinuierliche Überwachung zur Erkennung von Datenleckageversuchen und Richtlinienverstössen.

**Überwachungsanforderungen**:

| Überwachungstyp | Anforderung | Implementierungspriorität | Mindeststandard |
|----------------|-------------|--------------------------|----------------|
| **Echtzeiterkennung** | Alarm bei kritischen Datenleckageversuchen | **Verbindlich** | Eingeschränkte Daten, Zugangsdaten, Hochvolumentransfers |
| **Richtlinienverstoss-Alarme** | Benachrichtigung bei DLP-Richtlinienverstössen | **Verbindlich** | Benutzerbenachrichtigung, Sicherheitsteam-Alarm |
| **Verhaltensanalyse** | Anomalisches Benutzerverhalten erkennen | Empfohlen | Basislinien-Benutzeraktivität, Abweichungserkennung |
| **Bedrohungsintelligenz** | Exfiltrationsindikatoren integrieren | Empfohlen | C2-Domänen, Malware-Signaturen, APT-TTPs |
| **Trendanalyse** | Muster und aufkommende Risiken identifizieren | **Verbindlich** | Wöchentliche/monatliche Berichterstattung, Richtlinienanpassung |

**Erkennungsmodi**:

[Organisation] setzt DLP in mehreren Erkennungsmodi ein, basierend auf Risiko und betrieblichen Anforderungen:

| Modus | Beschreibung | Anwendungsfall | Genehmigungsbehörde |
|-------|-------------|---------------|---------------------|
| **Nur Überwachung** | Protokollieren und Alarmieren ohne Blockierung | Erstdeployment, Anpassungsphase, Niedrigrisikokanäle | Sicherheitsteam |
| **Benutzer auffordern** | Benutzerrechtfertigung bei sensitiven Transfers erforderlich | Vertrauliche Daten, vertrauenswürdige Benutzer | Sicherheitsteam |
| **Blockieren** | Datentransfer verhindern und alarmieren | Eingeschränkte Daten, nicht vertrauenswürdige Ziele | ISB (Richtlinienentscheid) |
| **Quarantäne** | Für Sicherheitsteam-Überprüfung halten | Verdächtige bösartige Exfiltration | Sicherheitsteam |

**Alarmpriorität**:

| Priorität | Auslöser | Reaktionszeit | Eskalation |
|-----------|---------|--------------|-----------|
| **Kritisch** | Eingeschränkte Daten an externe Empfänger, Zugangsdaten-Leck, Hochvolumentransfer | Sofort (< 15 Min.) | Sicherheitsteam + ISB |
| **Hoch** | Vertrauliche Daten an nicht vertrauenswürdige Domäne, Richtlinienverstoss durch privilegierten Benutzer | < 1 Std. | Sicherheitsteam |
| **Mittel** | Vertrauliche Daten an externe Empfänger (genehmigte Domäne), Massdateitransfer | < 4 Std. | Sicherheitsteam |
| **Niedrig** | Interne Daten nach extern, informationelle Alarme | < 24 Std. | Nur protokollieren, periodische Überprüfung |

**DLP-Leistungskennzahlen**:

[Organisation] verfolgt die DLP-Wirksamkeit durch folgende Key Performance Indicators (KPIs):

| Kennzahl | Zielwert | Akzeptabler Bereich | Überprüfungshäufigkeit |
|---------|---------|---------------------|----------------------|
| **Falsch-Positiv-Rate** | < 5% aller Alarme | < 10% Maximum | Monatlich |
| **SLA-Compliance Alarmreaktion** | > 95% innerhalb Zielzeiten | > 90% Minimum | Wöchentlich |
| **Kanalabdeckung** | 100% der kritischen Ausgangspfade | > 95% Minimum | Vierteljährlich |
| **Vorfallerkennungsrate** | 100% der Eingeschränkt-Daten-Exfiltrationsversuche | > 98% Minimum | Pro Vorfallüberprüfung |
| **Richtlinienanpassungs-Wirksamkeit** | > 20% FP-Reduktion pro Anpassungszyklus | Positiver Trend erforderlich | Vierteljährlich |
| **Benutzer gemeldete Probleme** | < 10 pro Monat | < 20 Maximum | Monatlich |

**Leistungsberichterstattung**: KPIs werden monatlich vom Sicherheitsteam überprüft, quartalsweise dem ISB berichtet und jährlich der Geschäftsleitung im Rahmen der Managementbewertung (ISO 27001 Klausel 9.3) berichtet.

**Massnahmen bei Unterschreitung von Zielwerten**: Falls Kennzahlen zwei aufeinanderfolgende Perioden unter dem akzeptablen Bereich liegen, muss der ISB:
1. Ursachenanalyse innerhalb von 30 Tagen durchführen
2. Korrekturmassnahmenplan mit Zeitplan implementieren
3. Behebungsstatus der Geschäftsleitung berichten
4. Erkenntnisse im entsprechenden Übersichts-Dashboard dokumentieren

**Protokollierungsanforderungen**:

[Organisation] führt umfassende Protokolle von DLP-Ereignissen für Vorfalluntersuchung und Compliance-Verifizierung:

**Protokollinhalt**:

- Zeitstempel (UTC, ISO 8601-Format)
- Benutzeridentität (Benutzername, E-Mail, Mitarbeiter-ID)
- Quellsystem (Hostname, IP-Adresse, Geräte-ID)
- Ziel (Empfänger-E-Mail, URL, externer Dienst, Wechseldatenträger-ID)
- Datenklassifizierung (Eingeschränkt, Vertraulich, INTERN)
- Erkennungsmethode (Inhaltsinspektion, Bezeichnung, Kontextanalyse)
- Durchgeführte Aktion (blockiert, erlaubt, Quarantäne, benutzergerechtfertigt)
- Datenauszug (erste 100 Zeichen oder bereinigter Ausschnitt — Datenschutz-konform)

**Protokollaufbewahrung**:

- DLP-Sicherheitsereignisse (blockierte Transfers, Richtlinienverstösse, kritische Alarme): Mindestens **12 Monate**
- DLP-Betriebsprotokolle (erlaubte Transfers, informationelle Ereignisse): Mindestens **90 Tage**
- Verlängerte Aufbewahrung gilt, wenn regulatorische Anforderungen längere Zeiträume vorschreiben (gemäss ISMS-POL-00)
- Protokolle mit geeigneten Integritäts- und Vertraulichkeitssteuerungen gemäss A.8.15 (Schutz von Protokollinformationen) geschützt
- Protokolllöschung erfordert dokumentierte Genehmigung und folgt Datenaufbewahrungsrichtlinien-Verfahren

**Datenschutz-Compliance**: DLP-Überwachung muss anwendbare Datenschutzbestimmungen gemäss ISMS-POL-00 einhalten. Benutzer werden durch Acceptable-Use-Richtlinie, Arbeitsverträge und Datenschutzhinweise über Überwachung informiert. Zugang zu DLP-Protokollen auf autorisiertes Personal (Sicherheitsteam, ISB, DSB, Legal) mit berechtigtem Bedarf beschränkt. Transparenzanforderungen für Mitarbeiterüberwachung in Anhang A dokumentiert.

**Implementierungshinweis**: Spezifische Alarmregeln, Eskalations-Workflows, Protokollformate und SIEM-Integrationsverfahren sind in ISMS-IMP-A.8.12-4 (Überwachungs- und Reaktionsbeurteilung) dokumentiert.

## Anforderungen an Vorfallreaktion und Behebung

[Organisation] implementiert strukturierte Vorfallreaktionsverfahren für DLP-Ereignisse.

**DLP-Vorfallklassifizierung**:

| Schweregrad | Indikatoren | Auswirkung | Reaktions-SLA |
|-------------|-----------|-----------|--------------|
| **Kritisch** | Eingeschränkte Daten exfiltriert, Zugangsdaten extern geleakt, Insider-Bedrohungsindikatoren, APT-Exfiltration | Datenpanne, regulatorische Meldepflicht, geschäftliche Auswirkung | Sofort (< 15 Min.) |
| **Hoch** | Vertrauliche Daten an nicht vertrauenswürdigen Empfänger, Massentransfer sensitiver Daten, wiederholte Richtlinienverstösse | Potenzielle Panne, Reputationsrisiko | < 1 Std. |
| **Mittel** | Vertrauliche Daten an genehmigten externen Partner, Benutzerfehler mit begrenzter Exposition | Begrenzte Exposition, Behebung erforderlich | < 4 Std. |
| **Niedrig** | Falsch-Positiv, Richtlinienklärung erforderlich, Anpassung erforderlich | Kein Datenverlust, betriebliche Verbesserung | < 24 Std. |

**Vorfallreaktions-Workflow**:

**Phase 1: Erkennung und Meldung**

- DLP-System generiert Alarm basierend auf Richtlinienverstoss
- Alarm durch Security Operations Center (SOC) oder Sicherheitsteam triagiert
- Vorfallklassifizierung (Kritisch/Hoch/Mittel/Niedrig)
- Erste Eindämmungsmassnahmen (Benutzer sperren, Endpunkt isolieren, Zugangsdaten widerrufen)

**Phase 2: Beurteilung und Untersuchung**

- Ursachenanalyse (bösartig vs. versehentlich, Insider vs. kompromittiertes Konto)
- Umfangsermittlung (Datenvolumen, Sensitivität, Empfänger, Expositionsdauer)
- Benutzerinterviews (bei versehentlich — Umstände verstehen)
- Forensische Beweissicherung (Protokolle, Netzwerkaufnahmen, Endpunkt-Forensik)

**Phase 3: Eindämmung und Beseitigung**

- Sofortige Eindämmung (Benutzerkonto sperren, Kanal deaktivieren, System isolieren)
- Zugangsdatenrotation (bei Zugangsdaten-Leck)
- Empfängerbenachrichtigung (wenn Daten an externe Partei gesendet — mit Legal/DSB koordinieren)
- Malware-Behebung (wenn Exfiltration über Malware)

**Phase 4: Wiederherstellung und Behebung**

- Normalbetrieb wiederherstellen (Benutzer reaktivieren, DLP-Richtlinie anpassen)
- Korrektivmassnahmen implementieren (Richtlinienanpassung, Benutzerschulung, technische Steuerungen)
- Benutzerkorrektivmassnahme (Schulung, Richtlinienbestätigung, Disziplinarmassnahme bei bösartigem Verhalten)

**Phase 5: Nachvorfallüberprüfung**

- Erkenntnissitzung (innerhalb von 30 Tagen)
- DLP-Richtlinienanpassungsempfehlungen
- Steuerungswirksamkeitsbeurteilung
- Vorfallberichtsdokumentation

**Regulatorische Meldepflicht**:

Soweit DLP-Vorfälle Datenpannen mit personenbezogenen Daten darstellen, folgt [Organisation] den regulatorischen Meldeanforderungen:

| Regulierung | Meldeanforderung | Frist | Behörde |
|-------------|----------------|-------|---------|
| **Schweizer nDSG** | Art. 24 — Pannenmeldung bei hohem Risiko für Betroffene | Ohne unangemessene Verzögerung | Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter (EDÖB) |
| **EU DSGVO** | Art. 33 — Pannenmeldung | 72 Stunden | Zuständige EU-Aufsichtsbehörde |
| **DSGVO Betroffene** | Art. 34 — Betroffene benachrichtigen bei hohem Risiko | Ohne unangemessene Verzögerung | Betroffene Datenpersonen |

**DSB-Konsultation**: Der Datenschutzbeauftragte (DSB) MUSS bei allen DLP-Vorfällen mit personenbezogenen Daten konsultiert werden, um Meldepflichten zu ermitteln.

**Vorfallsdokumentation**:

- Vorfallbericht (Zeitplan, Massnahmen, Auswirkung)
- Beweissicherung (Protokolle, Netzwerkaufnahmen, Benutzeraussagen)
- Regulatorische Meldungen (falls erforderlich)
- Behebungsmassnahmen und Verifizierung
- Erkenntnisse und Steuerungsverbesserungen

**Implementierungshinweis**: Detaillierte Vorfallreaktionsverfahren, Eskalationsmatrizen, Kommunikationsvorlagen und forensische Untersuchungsanleitungen sind in ISMS-IMP-A.8.12-4 (Überwachungs- und Reaktionsbeurteilung) dokumentiert.

---

# Rollen, Governance und Vorfallreaktion

## Rollen und Verantwortlichkeiten

**Geschäftsleitung / Verwaltungsrat**:

- **Accountable** für Genehmigung der DLP-Richtlinie und -Strategie
- Sicherstellung angemessener Ressourcen, Budget und organisatorischer Priorität
- Akzeptanz von Restrisiken, wo DLP-Steuerungen Datenleckagerisiken nicht vollständig mildern können
- Unterstützung des Sicherheitsprogramms und DLP-Initiativen

**Informationssicherheitsbeauftragter (ISB)**:

- **Accountable** für die Gesamteffektivität von DLP-Richtlinie und -Programm
- Genehmigung von DLP-Strategie, Risikobereitschaft und Steuerungsrahmen
- Genehmigung von Hochrisikoausnahmen und Richtlinienänderungen
- Eskalation kritischer DLP-Vorfälle an die Geschäftsleitung
- Jährliche Richtlinienüberprüfung und -genehmigung
- Budgetverantwortung für DLP-Technologie und -Ressourcen

**Datenschutzbeauftragter (DSB)**:

- **Beratend** bei allen DLP-Überwachungsaktivitäten mit Bezug zu personenbezogenen Daten
- Sicherstellung der Compliance mit Schweizer nDSG und EU DSGVO-Mitarbeiterüberwachungsanforderungen
- Überprüfung von DLP-Richtlinien auf Verhältnismässigkeit und Transparenz
- Beratung zu Datenpannen-Meldepflichten (Schweizer nDSG Art. 24, DSGVO Art. 33/34)
- Datenschutz-Folgenabschätzungen für DLP-Deployments

**Sicherheitsteam**:

- **Verantwortlich** für Implementierung von DLP-Richtlinienanforderungen
- Deployen und Warten von DLP-Lösungen (E-Mail, Endpunkt, Netzwerk, Cloud, Mobil)
- Konfigurieren von DLP-Richtlinien, Regeln und Erkennungslogik
- Überwachen von DLP-Alarmen und Reagieren auf Sicherheitsvorfälle
- Bearbeiten von Ausnahmeanträgen und Durchführen von Risikobeurteilungen
- Anpassen von DLP-Richtlinien zur Reduzierung von Falsch-Positiven
- Integration von Bedrohungsintelligenz-Feeds
- Durchführen regelmässiger Abdeckungsbeurteilungen und Wirksamkeitsüberprüfungen

**IT-Betrieb / Netzwerkteam**:

- **Verantwortlich** für Deployen und Warten der DLP-Infrastruktur
- Sicherstellung, dass Netzwerktopologie DLP-Abdeckung unterstützt (Datenverkehrsrouting, TLS-Inspektion)
- Technischen Support für DLP-Systeme bereitstellen
- Änderungen mit Sicherheitsteam koordinieren (Netzwerkmodifikationen, Systemupdates)
- Verfügbarkeit und Leistung des DLP-Systems aufrechterhalten

**Systemeigentümer / Dateneigentümer**:

- **Accountable** für Datenklassifizierungsentscheidungen in ihrer Domäne
- Datenschutzanforderungen auf Basis des Geschäftsrisikos definieren
- DLP-Abdeckung für Systeme anfordern, die sensitive Daten verarbeiten
- DLP-Vorfälle mit ihren Daten überprüfen
- Ausnahmen für geschäftlich begründete Datentransfers genehmigen

**Benutzer (Alle Mitarbeitenden)**:

- **Verantwortlich** für Einhaltung der DLP-Richtlinien und Acceptable-Use-Richtlinie
- Melden von DLP-Falsch-Positiven und Nutzungsproblemen
- Ausnahmeprozess für legitime Geschäftsbedürfnisse nutzen, die Abweichung von der DLP-Richtlinie erfordern
- **Verboten**: Versuche, DLP-Steuerungen zu umgehen (Verstoss unterliegt Disziplinarmassnahmen)
- Jährliche DLP-Sensibilisierungsschulung absolvieren

**Legal / Compliance**:

- **Beratend** bei regulatorischer Interpretation und Compliance-Verpflichtungen
- Überprüfung von DLP-Richtlinien auf rechtliche Compliance (Arbeitsrecht, Datenschutzrecht)
- Beratung zu Datenpannen-Meldeanforderungen
- Unterstützung bei DLP-Vorfalluntersuchungen, die juristische Expertise erfordern

**Human Resources (HR)**:

- **Beratend** zu Transparenzanforderungen für Mitarbeiterüberwachung
- Sicherstellung, dass Arbeitsverträge DLP-Überwachungsbestätigung enthalten
- Koordination mit Legal/ISB bei Disziplinarmassnahmen bei Richtlinienverstössen
- Unterstützung von Schulungs- und Sensibilisierungsprogrammen

**Detaillierte RACI-Matrix**: Vollständige Rollen- und Verantwortlichkeitsmatrix in ISMS-IMP-A.8.12 Implementierungsanleitungen dokumentiert.

## Beurteilung und Verifizierung

[Organisation] verifiziert die Wirksamkeit von DLP-Steuerungen durch strukturierte Beurteilung.

**Beurteilungsdomänen**:

1. **DLP-Infrastruktur** (ISMS-IMP-A.8.12-1): Eingesetzte Technologien, Fähigkeiten, Abdeckung, Architektur
2. **Datenklassifizierung** (ISMS-IMP-A.8.12-2): Inventar sensitiver Daten, Klassifizierungsschema, Erkennungsmethoden
3. **Kanalabdeckung** (ISMS-IMP-A.8.12-3): E-Mail-, Web-, Endpunkt-, Netzwerk-, Cloud-, Mobilschutz
4. **Überwachung und Reaktion** (ISMS-IMP-A.8.12-4): Alarmierung, Vorfallreaktion, Wirksamkeitskennzahlen

**Berichterstattungsplan**: Monatliche Sicherheitsteamüberprüfung, vierteljährliche ISB-Überprüfung, jährliche Geschäftsleitungsbewertung (im Rahmen von ISO 27001 Klausel 9.3 Managementbewertung)

**Beurteilungsmethodik**:

Jede Domäne wird bewertet durch:

- Technologieinventar (eingesetzte DLP-Lösungen, Versionen, Lizenzen)
- Konfigurationsüberprüfung (Richtlinien, Regeln, Erkennungslogik)
- Abdeckungstest (Kanalverifizierung, Bypass-Tests)
- Wirksamkeitskennzahlen (Richtig-Positive, Falsch-Positive, blockierte Vorfälle)
- Lückenanalyse (identifizierte Risiken, Behebungsempfehlungen)
- Evidenzregister (Screenshots, Konfigurationsexporte, Testergebnisse)

**Beurteilungshäufigkeit**:

- **Umfassende Beurteilung**: Jährlich (ausgerichtet an internem Revisionsprogramm, typischerweise Q4)
- **Periodische Verifizierung**: Vierteljährlich (Abdeckungstest, Richtlinienwirksamkeit, Falsch-Positiv-Raten)
- **Anlassbezogene Beurteilung**: Innerhalb von 30 Tagen nach:
  - Kritischen DLP-Vorfällen (erfolgreiche Datenexfiltration, Insider-Bedrohung)
  - Wesentlichen Infrastrukturänderungen mit Auswirkung auf DLP-Abdeckung (Cloud-Migration, Netzwerkneugestaltung)
  - Deployment neuer DLP-Lösungen oder wesentlicher Versions-Upgrades
  - Revisionsergebnissen, die Behebungsverifizierung erfordern
  - Regulatorischen Änderungen mit Auswirkung auf Überwachungsanforderungen

## Ausnahmemanagement

**Anforderungen für Ausnahmeanträge**:

Ausnahmen von DLP-Richtlinienanforderungen erfordern:

- **Dokumentierte Geschäftsbegründung**: Spezifischer Anwendungsfall, geschäftliche Kritikalität, Zeitplan
- **Risikobeurteilung**: Wahrscheinlichkeit des Datenlecks, Auswirkung bei Leckage, Restrisikostufe
- **Kompensierende Massnahmen**: Alternative Schutzmassnahmen (Verschlüsselung, begrenzter Umfang, verstärkte Überwachung)
- **Zeitplan**: Temporär (spezifisches Enddatum) oder dauerhaft (fortlaufendes Geschäftsbedürfnis)
- **Formelle Genehmigung**: Gemäss Genehmigungsmatrix basierend auf Risikostufe

**Genehmigungsbehörde**:

| Ausnahmetyp | Risikostufe | Genehmigungsbehörde | Überprüfungshäufigkeit |
|-------------|-----------|---------------------|----------------------|
| **Einzeltransfer (einmalig)** | Niedrig | Sicherheitsteam-Leiter | N/A (einmalig) |
| **Benutzerausnahme (individuell)** | Mittel | Sicherheitsteam-Leiter + Vorgesetzte/r | Vierteljährlich |
| **Gruppenausnahme (Abteilung)** | Hoch | ISB + Abteilungsleitung | Vierteljährlich |
| **Kanalausnahme (Überwachung deaktivieren)** | Hoch | ISB + ITL | Monatlich |
| **Datenklassifizierungsausnahme** | Kritisch | ISB + Geschäftsleitung | Monatlich |

**Ausnahmebeschränkungen**:

Folgende Ausnahmen sind **UNTER KEINEN UMSTÄNDEN GESTATTET**:

- DLP-Schutz für Eingeschränkte Daten ohne kompensierende Massnahmen deaktivieren
- DLP für Zugangsdaten-Transfers umgehen (Passwörter, API-Schlüssel, Zertifikate)
- DLP-Überwachung für privilegierte Benutzer (Administratoren, Führungskräfte) ohne ISB-Genehmigung deaktivieren
- Dauerhafte Ausnahmen ohne dokumentierte kompensierende Massnahmen

**Ausnahmeüberwachung**:

Aktive Ausnahmen werden durch das DLP-Ausnahmeregister verfolgt und überwacht:

**Ausnahmeregister-Speicherort**: [SharePoint-Pfad / GRC-Plattformmodul / Excel-Registerpfad]
**Registereigentümer**: Sicherheitsteam-Leiter
**Aktuelle aktive Ausnahmen**: [Anzahl] per [Datum]
**Letztes Überprüfungsdatum**: [Datum]

**Ausnahmeregisterfelder**:
- Ausnahme-ID (Format: DLP-EX-JJJJ-NNN)
- Betroffener Benutzer/Gruppe/Kanal
- Geschäftliche Begründung
- Risikobeurteilungsergebnis
- Implementierte kompensierende Massnahmen
- Genehmigungsbehörde und Datum
- Ablaufdatum
- Überprüfungsplan

**Überprüfungsplan**:
- Hochrisikoausnahmen: Monatlich (erster Montag)
- Mittelrisikoausnahmen: Vierteljährlich (ausgerichtet an IMP-A.8.12-Beurteilungszyklus)
- Niedrigrisikoausnahmen: Halbjährlich

**Ausnahmelebenszyklus**:
- Aktivität auf Richtliniencompliance überwacht (verstärkte Protokollierung, periodische Überprüfung)
- Widerruf bei Änderung des Risikoprofils oder ungültiger Geschäftsbegründung
- Widerrufene Ausnahmen mit 12-monatiger Aufbewahrung für Revisionsspur archiviert

**Zugang zum Ausnahmeregister**: Sicherheitsteam (vollständiger Zugang), ISB (Lesen/Genehmigen), Interne Revision (nur Lesen), Externe Prüfer (nur Lesen auf Anfrage)

**Ausnahmevorlage**: ISMS-IMP-A.8.12-Ausnahmeantrag-Verfahren bieten standardisiertes Dokumentationsformat, Risikobeurteilungsvorlage und Genehmigungsworkflow.

## Vorfallreaktion

**DLP-Sicherheitsvorfälle** umfassen:

| Vorfalltyp | Indikatoren | Schweregrad | Erste Massnahmen |
|------------|-----------|-------------|----------------|
| **Datenexfiltration** | Eingeschränkte/Vertrauliche Daten extern gesendet | Kritisch/Hoch | Benutzer sperren, Endpunkt isolieren, ISB/DSB benachrichtigen |
| **Zugangsdaten-Leck** | Passwörter, API-Schlüssel, Zertifikate extern gesendet | Kritisch | Zugangsdatenrotation, Kontoüberprüfung, Malware-Scan |
| **Insider-Bedrohung** | Wiederholte Richtlinienverstösse, Massendaten-Downloads, Aktivität vor Kündigung | Kritisch/Hoch | HR-Koordination, rechtliche Beratung, forensische Untersuchung |
| **Kompromittiertes Konto** | Ungewöhnliche Transfermuster, Exfiltration über Malware | Kritisch/Hoch | Kontosperrung, Endpunkt-Forensik, Malware-Behebung |
| **Falsch-Positiv** | Legitime Geschäftsaktivität fälschlicherweise blockiert | Niedrig | DLP-Richtlinienanpassung, Benutzerkommunikation, Ausnahme falls erforderlich |
| **Richtlinienverstoss** | Benutzer umgeht DLP-Steuerungen (Proxy, Verschlüsselung) | Mittel/Hoch | Benutzerinterviews, Disziplinarmassnahme, verstärkte Überwachung |

**Reaktionsprozess**:

1. **Erkennung und Meldung**: DLP-Alarm löst Vorfallworkflow aus
2. **Beurteilung**: Vorfallklassifizierung, Umfangsermittlung, Dringlichkeitsbewertung
3. **Eindämmung**: Sofortmassnahmen zur Verhinderung weiterer Datenverluste (Benutzer sperren, System isolieren)
4. **Untersuchung**: Ursachenanalyse, forensische Beweissicherung, Benutzerinterviews
5. **Beseitigung**: Bedrohung entfernen (Malware-Behebung, Zugangsdatenrotation, Zugangsrevokation)
6. **Wiederherstellung**: Normalbetrieb wiederherstellen, Korrektivmassnahmen implementieren
7. **Nachvorfall**: Erkenntnisse, DLP-Richtlinienanpassung, Steuerungsverbesserungen

**DLP-zu-ITSM-Integration**:

DLP-Alarme erstellen automatisch Incident-Tickets zur Sicherstellung von Verfolgung und Verantwortlichkeit:
- **Integrationsziel**: [ServiceNow / Jira Service Management / ITSM-Plattform]
- **Automatische Ticket-Erstellung**: Kritische und Hoch-Schweregrad-DLP-Ereignisse
- **Manuelle Ticket-Erstellung**: Mittel- und Niedrig-Schweregrad-Ereignisse (nach Ermessen des Analysten)
- **Konfigurationsdatum der Integration**: [Datum]
- **Letztes Integrationstestdatum**: [Datum]

**Kritische Vorfälle**: Datenexfiltration von Eingeschränkten Daten oder Zugangsdaten-Leck werden als hochprioritäre Sicherheitsvorfälle behandelt, die sofortige ISB-Benachrichtigung und potenzielle regulatorische Pannenmeldung erfordern.

**Vorfallkoordination**:

- **Sicherheitsteam**: Leitet technische Untersuchung und Eindämmung
- **DSB**: Konsultiert bei Datenpannen mit personenbezogenen Daten, berät zu Meldepflichten
- **Legal**: Konsultiert bei regulatorischer Compliance, Rechtsstreitrisiko, Strafverfolgungskoordination
- **HR**: Konsultiert bei mitarbeiterbezogenen Vorfällen, Disziplinarmassnahmen
- **Kommunikation**: Konsultiert bei externen Meldungen (Kunden, Partner, Regulatoren)

## Richtlinien-Governance

**Richtlinienüberprüfung**:

- **Häufigkeit**: Mindestens jährlich (ausgerichtet an ISMS-Managementüberprüfungszyklus)
- **Auslöser**: Regulatorische Änderungen, wesentliche Vorfälle, wesentliche Bedrohungslandschaftsänderungen, organisatorische Änderungen (M&A, neue Geschäftsfelder), Revisionsergebnisse
- **Prüfer**: ISB, Sicherheitsteam, Legal/Compliance, DSB, IT-Betrieb, Dateneigentümer
- **Genehmigung**: ISB (technisch), Geschäftsleitung (strategisch)

**Überprüfung der Implementierungsstandards**:

- **Häufigkeit**: Basierend auf Bedrohungslandschaftsentwicklung und Technologieänderungen (mindestens halbjährlich)
- **Zuständigkeit**: Sicherheitsteam schlägt Updates vor, ISB genehmigt
- **Hinweis**: Updates der Implementierungsstandards (ISMS-IMP-A.8.12) erfordern keine Richtlinienrevision

**Richtlinienaktualisierungen**:

| Änderungstyp | Beispiele | Genehmigungsprozess | Implementierungsfrist |
|-------------|----------|---------------------|----------------------|
| **Geringfügig** | Klarstellungen, Referenz-Updates, Formatierung | ISB-Genehmigung | Kommunikation innerhalb 30 Tage |
| **Wesentlich** | Umfangsänderungen, neue Kanäle, Anforderungsänderungen | Vollständige Genehmigungskette (ISB, ITL, DSB, Geschäftsleitung) | Gemäss Änderungsmanagement, typischerweise 60-90 Tage |
| **Notfall** | Kritische Bedrohung, regulatorische Frist, wesentlicher Vorfall | ISB-Genehmigung mit nachträglicher Überprüfung | Sofortige Implementierung, Nachprüfung innerhalb 30 Tage |

**Kommunikation**:

Richtlinienaktualisierungen kommuniziert über:

- **Richtlinienportal**: ISMS-Dokumentenrepository (versionskontrolliert, Änderungsverfolgung)
- **E-Mail-Benachrichtigungen**: Alle Mitarbeitenden, Security Operations, IT-Betrieb, Dateneigentümer, Systemeigentümer
- **Schulungsupdates**: Sicherheitsbewusstsein (DLP-Zweck, akzeptable Verwendung), IT-Betrieb-Schulung (Vorfallreaktion), Dateneigentümer-Schulung (Klassifizierung, Ausnahmen)
- **Mitarbeiterbenachrichtigung**: DLP-Überwachungspraktiken (gesetzliche Anforderung gemäss Schweizer DSG, DSGVO)
- **Quartalsberichte**: ISB-Berichte an Geschäftsleitung über DLP-Wirksamkeit und Trends
- **Mitarbeitervertretungsbenachrichtigungen**: Wo gesetzlich vorgeschrieben (Schweiz, Deutschland, Frankreich, EU-Mitgliedsstaaten mit Mitbestimmungsrechten)

---

# Implementierung und Referenzen

## Integration ins ISMS

Diese Richtlinie ist in das Informationssicherheitsmanagementsystem von [Organisation] integriert:

**Verwandte Steuerungen**:

| Steuerung | Integrationspunkt |
|-----------|------------------|
| **A.5.10** | Akzeptable Verwendung von Informationen — Definiert akzeptable Datenhandhabungs- und Transferpraktiken |
| **A.5.12** | Klassifizierung von Informationen — DLP schützt Daten basierend auf Klassifizierungsbezeichnungen |
| **A.5.15** | Zugangskontrolle — DLP setzt Zugangsgrenzen an Ausgangspunkten durch |
| **A.5.17** | Authentifizierungsinformationen — DLP erkennt Zugangsdaten-Leckage |
| **A.5.19-23** | Lieferantensicherheit — DLP-Steuerungen für Datenweitergabe an Dritte |
| **A.5.24-28** | Vorfallmanagement — DLP-Alarme lösen Sicherheitsvorfallreaktion aus |
| **A.5.34** | Datenschutz und PII-Schutz — DLP verhindert unbefugte PII-Offenlegung |
| **A.8.10** | Informationslöschung — DLP verhindert unbefugte Datenaufbewahrung auf Wechseldatenträgern |
| **A.8.11** | Datenmaskierung — Ergänzende Datenschutztechnik (vor Weitergabe maskieren) |
| **A.8.15** | Protokollierung — DLP-Ereignisse protokolliert für Sicherheitsüberwachung und Untersuchung |
| **A.8.16** | Überwachungsaktivitäten — DLP generiert Sicherheitsereignisprotokolle für SIEM-Integration |
| **A.8.20** | Netzwerksicherheit — DLP operiert innerhalb des Netzwerksegmentierungsrahmens |
| **A.8.23** | Web-Filterung — Überschneidung beim Web-Kanal-Datenschutz und Exfiltrationsprävention |
| **A.8.24** | Kryptografie — Verschlüsselung ergänzt DLP (verschlüsselte Kanäle können TLS-Inspektion erfordern) |

## Schulung und Sensibilisierung

**Sicherheitsbewusstsein** (Alle Mitarbeitenden):

- **Jährliche Schulung**: DLP-Zweck, akzeptable Verwendung, Datenhandhabung, Überwachungstransparenz
- **Benutzerverantwortlichkeiten**: Sensitive Daten erkennen, geeignete Transfermethoden, Vorfälle melden
- **DLP-Interaktion**: Verständnis für blockierte Transfers, Ausnahmeanträge, Falsch-Positiv-Meldung
- **Datenschutzbewusstsein**: Transparenz bei Mitarbeiterüberwachung, Rechte der Betroffenen

**Technische Schulung** (IT/Sicherheitsteam):

- **DLP-Technologie**: Lösungskonfiguration, Regelerstellung, Richtlinienanpassung
- **Bedrohungsintelligenz**: Exfiltrationstechniken, Insider-Bedrohungsindikatoren, APT-TTPs
- **Vorfallreaktion**: DLP-Ereignisuntersuchung, forensische Beweissicherung, Behebungsverfahren
- **Ausnahmebewertung**: Risikobeurteilung, kompensierende Massnahmen, Genehmigungsworkflows

**Betriebliche Schulung** (IT-Betrieb, Helpdesk):

- **Falsch-Positiv-Behandlung**: Benutzerunterstützung, Eskalationsverfahren, temporäre Ausnahme-Workflows
- **Benutzerunterstützung**: DLP-Blockierungen erklären, legitime Transfers anleiten, Ausnahmeanträge
- **Häufige Szenarien**: Routinemässige Blockierungsfälle, Lösungsverfahren, Dokumentationsanforderungen

**Management-Schulung** (Dateneigentümer, Abteilungsleitung):

- **Datenklassifizierung**: Sensitive Daten identifizieren, geeignete Bezeichnungen anwenden, DLP-Abdeckung anfordern
- **Ausnahmegenehmigung**: Risikobeurteilung, Geschäftsbegründungsbewertung, Genehmigungsbefugnis
- **Compliance-Aufsicht**: DLP-Kennzahlen überprüfen, Lücken beheben, Sicherheitsprogramm unterstützen

---

# Definitionen

**Data Leakage Prevention (DLP)**: Eine Reihe von Technologien, Prozessen und Richtlinien zur Erkennung, Verhinderung und Reaktion auf unbefugte Offenlegung, Übertragung oder Exfiltration sensitiver Informationen aus organisatorischen Systemen, Netzwerken und Endpunkten. DLP-Steuerungen arbeiten auf mehreren Ebenen: Inhaltsinspektion (Mustererkennung, Machine Learning), Kontextanalyse (Quellsystem, Benutzerrolle, Ziel) und Richtliniendurchsetzung (Blockieren, Alarmieren, Quarantäne).

**Datenleckage**: Die unbeabsichtigte oder unbefugte Offenlegung sensitiver Informationen an externe Parteien oder nicht autorisierte interne Parteien. Umfasst versehentliche Offenlegung (Benutzerfehler, Fehlkonfiguration, Übersharing) und bösartige Exfiltration (Insider-Bedrohungen, Malware-basierte Exfiltration, Advanced Persistent Threats).

**Datenverlust**: Die permanente Vernichtung oder Nichtverfügbarkeit von Informationen aufgrund von Hardware-Ausfall, Korruption, Löschung oder Katastrophe. Datenverlust wird durch Sicherungs- und Notfallwiederherstellungssteuerungen adressiert (ISMS-POL-A.8.13, ISMS-POL-A.7.14), NICHT durch DLP. DLP verhindert unbefugte OFFENLEGUNG, nicht VERLUST von Daten.

**Exfiltration**: Der unbefugte Transfer von Daten aus den Systemen einer Organisation an externe Standorte oder Akteure. Exfiltrationsmethoden umfassen: E-Mail (an private Konten), Web-Upload (Cloud-Speicher, Dateifreigabe), Wechseldatenträger (USB-Sticks), Netzwerkprotokolle (FTP, DNS-Tunneling), Mobilgeräte (BYOD-Datensynchronisation) und Applikations-APIs (unbefugter Datenexport).

**Ausgangskanal**: Jeder Kommunikationspfad, über den Daten die Kontrolle der Organisation verlassen können. Ausgangskanäle umfassen: E-Mail (SMTP, Webmail), Web (HTTP/HTTPS-Uploads, Cloud-Speicher), Endpunkte (USB, lokaler Speicher, Drucken, Screenshots), Netzwerk (Dateiübertragungsprotokolle, verdeckte Kanäle), Cloud-Applikationen (SaaS-Datenweitergabe), Mobilgeräte (dienstlich und BYOD) und Applikations-APIs (REST, GraphQL, SOAP).

**Inhaltsinspektion**: Technische Methode zur Analyse von Dateninhalt auf sensitive Informationen. Methoden umfassen: Mustererkennung (Regex für Kreditkarten, AHV-Nummern), Schlagworterkennung (vertrauliche Begriffe, Projektnamen), Dokumenten-Fingerprinting (hash-basierte Verfolgung), Machine Learning (KI-basierte Klassifizierung) und Natural Language Processing (kontextuelles Verstehen).

**Kontextanalyse**: Bewertung des Datentransfer-Kontexts zur Bestimmung von Sensitivität und Risiko. Kontextfaktoren umfassen: Quellsystem (HR-Datenbank, Finanzsystem), Benutzerrolle (Privilegstufe, Abteilung), Ziel (intern vs. extern, vertrauenswürdige vs. nicht vertrauenswürdige Domäne), Tageszeit (Geschäftszeiten vs. ausserhalb), Transfervolumen (Einzeldatei vs. Massenexport) und Verhaltensmuster (Basislinie vs. Anomalie).

**Falsch-Positiv**: Legitime Geschäftsaktivität, die fälschlicherweise als DLP-Richtlinienverstoss identifiziert wird. Häufige Ursachen: zu breite Regeln, unzureichende Kontextanalyse, nicht angepasste Erkennungslogik. Falsch-Positive verursachen Benutzerreibung, betriebliche Verzögerungen und Sicherheitsteam-Arbeitsbelastung. Minimiert durch Richtlinienanpassung, Ausnahmemanagement und Machine Learning.

**Falsch-Negativ**: Datenleckage, die trotz DLP-Steuerungen auftritt (umgangen oder unerkannt). Ursachen: Abdeckungslücken, Erkennungslogikbeschränkungen, verschlüsselte Kanäle, verdeckte Exfiltrationstechniken. Falsch-Negative stellen Restrisiken dar und treiben kontinuierliche DLP-Verbesserung an.

**Insider-Bedrohung**: Sicherheitsrisiko durch Personen mit autorisiertem Zugang, die absichtlich oder unabsichtlich Schaden verursachen. DLP adressiert Insider-Datenexfiltration einschliesslich: böswillige Insider (Diebstahl für finanziellen Gewinn, Wettbewerbsvorteil), fahrlässige Insider (versehentliche Offenlegung, schlechte Sicherheitshygiene) und kompromittierte Insider (Kontoübernahme, Social Engineering).

**Verhältnismässigkeitsprinzip**: Gesetzliche Anforderung (Schweizer DSG Art. 6, DSGVO Art. 5), dass Sicherheitsüberwachung dem legitimen Sicherheitsziel verhältnismässig sein muss. DLP-Überwachung muss Datenschutzbedürfnisse gegen Mitarbeiterprivatsphäre-Rechte abwägen. Unverhältnismässige Überwachung (übermässiger Umfang, Aufbewahrung, Eingriffstiefe) kann rechtlich nicht konform sein unabhängig von der Sicherheitsbegründung.

**Transparenzanforderung**: Gesetzliche Verpflichtung (Schweizer DSG Art. 19, DSGVO Art. 13/14, Schweizer OR Art. 328b), Mitarbeitende über Überwachungsaktivitäten zu informieren. DLP-Deployments erfordern klare Kommunikation in: Arbeitsverträgen, Acceptable-Use-Richtlinien, Datenschutzhinweisen und Mitarbeiterhandbüchern. Fehlende Transparenz kann die Überwachung rechtlich ungültig machen.

**Mitarbeiterüberwachung**: Überwachung von Mitarbeiteraktivitäten und -kommunikationen. In der Schweiz und der EU unterliegt Mitarbeiterüberwachung strengen gesetzlichen Anforderungen: Rechtsgrundlage (berechtigtes Interesse, Einwilligung, gesetzliche Verpflichtung), Verhältnismässigkeit (notwendig und angemessen), Transparenz (klare Benachrichtigung), Zweckbindung (nur Sicherheit, nicht Leistungsmanagement). DLP-Überwachung muss Arbeitsrecht einhalten unabhängig von der Sicherheitsbegründung.

**Kompensierende Massnahme**: Alternative Sicherheitsmassnahmen, die implementiert werden, wenn primäre Steuerungen nicht vollständig angewendet werden können. Im DLP-Kontext: Verschlüsselung (für sensitive Transfers, die DLP-Ausnahme erfordern), verstärkte Überwachung (erhöhte Protokollierung für Ausnahmen), begrenzter Umfang (zeitgebundene oder benutzerspezifische Ausnahmen), manuelle Überprüfung (Quarantäne statt automatischer Blockierung).

**Ausnahme**: Formelle Abweichung von Standard-DLP-Richtlinienanforderungen, gewährt durch risikobasierten Genehmigungsprozess. Ausnahmen dokumentieren: Geschäftsbegründung, Risikobeurteilung, kompensierende Massnahmen, Genehmigungsbehörde, Zeitlimit (temporär vs. dauerhaft), Überwachungsanforderungen und Überprüfungshäufigkeit.

**Quarantäne**: Temporäres Halten von Datentransfers bis zur Überprüfung durch das Sicherheitsteam. Verwendet für: verdächtige bösartige Exfiltration (manuelle Untersuchung erforderlich), Hochrisiko-Transfers (sensitive Daten an externe Partei), erstmalige Transfers (Basislinie etablieren) und mehrdeutige Fälle (automatische Entscheidung unzureichend).

---

# Anhang A: Rechtliche Anforderungen an Mitarbeiterüberwachung

**Anwendungsbereich**: Dieser Anhang legt rechtliche Compliance-Anforderungen für DLP-Überwachung von Mitarbeiteraktivitäten unter dem Schweizer Datenschutzgesetz (DSG) und der EU Datenschutz-Grundverordnung (DSGVO) fest.

## A.1 Schweizer Rechtsrahmen (DSG und Obligationenrecht)

**Schweizer Datenschutzgesetz (DSG/nDSG) — In Kraft seit 01.09.2023**:

**Artikel 6 — Grundsätze der Datenbearbeitung**:

- **Rechtmässigkeit**: Datenbearbeitung muss eine Rechtsgrundlage haben (berechtigtes Interesse am Datenschutz)
- **Verhältnismässigkeit**: Bearbeitung muss dem Zweck verhältnismässig sein (Überwachungsumfang auf Sicherheitsziele beschränkt)
- **Zweckbindung**: Für Sicherheitszwecke erhobene Daten dürfen nicht für andere Zwecke verwendet werden (z.B. Leistungsmanagement)
- **Transparenz**: Betroffene (Mitarbeitende) müssen über Überwachung informiert werden

**Artikel 19 — Auskunftsrecht**:
Mitarbeitende haben das Recht zu wissen:

- Dass Überwachung stattfindet (Transparenz)
- Welche Daten erhoben werden (Überwachungsumfang)
- Zweck der Überwachung (Verhinderung von Datenleckagen)
- Wer Zugang zu Überwachungsdaten hat (Sicherheitsteam, ISB, DSB)
- Aufbewahrungsfrist (Protokollaufbewahrung: 90 Tage Betrieb, 12 Monate Sicherheitsereignisse)

**Schweizer Obligationenrecht (OR) — Artikel 328b: Schutz der Persönlichkeit des Arbeitnehmers**:

> *„Der Arbeitgeber hat im Arbeitsverhältnis die Persönlichkeit des Arbeitnehmers zu achten und zu schützen... Der Arbeitgeber darf Daten über den Arbeitnehmer nur bearbeiten, soweit sie dessen Eignung für das Arbeitsverhältnis betreffen oder zur Erfüllung des Arbeitsvertrages erforderlich sind."*

**DLP-Compliance-Anforderungen**:

- Überwachung muss **arbeitsbezogen** sein (Datenschutz ist legitimes Geschäftsinteresse)
- Überwachung muss **verhältnismässig** sein (Sicherheitsziel rechtfertigt Umfang)
- Überwachung muss **transparent** sein (Mitarbeitende informiert via Arbeitsvertrag, Datenschutzhinweis)
- Persönliche Daten ohne Arbeitsbezug sind geschützt (private E-Mails, privates Surfen ausserhalb der Arbeitszeit)

## A.2 EU DSGVO-Rahmen (anwendbar bei Verarbeitung personenbezogener Daten von EU-Betroffenen)

**DSGVO Artikel 5 — Grundsätze der Verarbeitung**:

- Rechtmässigkeit, Fairness, Transparenz
- Zweckbindung (nur Sicherheitsüberwachung)
- Datenminimierung (nur Notwendiges erheben)
- Richtigkeit
- Speicherbegrenzung (Aufbewahrung dem Zweck entsprechend)
- Integrität und Vertraulichkeit

**DSGVO Artikel 6 — Rechtsgrundlage für die Verarbeitung**:

DLP-Überwachung stützt sich typischerweise auf:

- **Berechtigtes Interesse** (Art. 6(1)(f)): Schutz organisatorischer Daten ist berechtigtes Interesse, abgewogen gegen Mitarbeiterprivatsphäre
- **Rechtliche Verpflichtung** (Art. 6(1)(c)): Wo Regulierungen Sicherheitsüberwachung vorschreiben (z.B. Finanzsektor)
- **Vertrag** (Art. 6(1)(b)): Arbeitsvertrag enthält Acceptable-Use- und Überwachungsbestimmungen

**DSGVO Artikel 32 — Sicherheit der Verarbeitung**:
Organisationen müssen geeignete technische und organisatorische Massnahmen implementieren (DLP ist eine Sicherheitsmassnahme).

**DSGVO Artikel 88 — Verarbeitung im Beschäftigungskontext**:
Mitgliedstaaten können spezifische Regeln für die Verarbeitung von Mitarbeiterdaten vorsehen. DLP-Überwachung muss nationales Arbeitsrecht in jeder EU-Jurisdiktion einhalten.

## A.3 Verhältnismässigkeitsbeurteilung

**Verhältnismässige DLP-Überwachung (Rechtlich konform)**:

✅ Ausgangskanäle nur auf sensitive Daten überwachen (E-Mail, Web, Endpunkt, Netzwerk)
✅ Hochrisiko-Daten im Fokus (PII, Finanzieren, IP, Zugangsdaten)
✅ DLP-Alarme mit begrenzter Aufbewahrung protokollieren (90 Tage Routine, 12 Monate Vorfälle)
✅ Zugang zu DLP-Protokollen beschränken (Sicherheitsteam, ISB, DSB — auf Need-to-Know-Basis)
✅ Zunächst nur im Überwachungsmodus deployen (beobachten vor Blockieren)
✅ Benutzerbenachrichtigungen bereitstellen (Transparenz via Acceptable-Use-Richtlinie)
✅ Datenauszüge in Protokollen begrenzen (erste 100 Zeichen, bereinigter Ausschnitt)

**Unverhältnismässige Überwachung (Rechtlich nicht konform)**:

❌ Alle E-Mail-Inhalte unbegrenzt aufzeichnen (übermässiger Umfang und Aufbewahrung)
❌ Gesamtes Web-Browsing unabhängig vom Risiko überwachen (übermässige Breite)
❌ HR-Zugang zu DLP-Alarmen für Leistungsmanagement ermöglichen (Zweckentfremdung)
❌ Tastatureingaben oder Bildschirmaufnahmen ohne spezifische dokumentierte Begründung (invasiv)
❌ Private Geräte auf Nicht-Arbeitsaktivitäten überwachen (Übergriff)
❌ Vollständige Nachrichteninhalte ohne spezifische Vorfallbegründung lesen (Datenschutzverletzung)
❌ DLP-Daten für Mitarbeiterbewertung oder nicht sicherheitsbezogene Disziplinarmassnahmen verwenden

**Verhältnismässigkeitstest**: Würde eine vernünftige Person diese Überwachung angesichts des Sicherheitsziels als übermässig betrachten? Wenn ja, ist sie unverhältnismässig und wahrscheinlich nicht konform.

## A.4 Transparenzanforderungen

**[Organisation] MUSS Mitarbeitende über DLP-Überwachung informieren durch**:

**1. Arbeitsvertrag / Nachtrag**:

- Klare Aussage, dass DLP-Überwachung vorhanden ist
- Überwachungsumfang (Ausgangskanäle: E-Mail, Web, Endpunkt, Netzwerk, Cloud, Mobil)
- Zweck (Verhinderung von Datenleckagen, Schutz sensitiver Informationen)
- Erhobene Daten (Metadaten, Inhaltsauszüge für Sicherheitsereignisse)
- Aufbewahrungsfristen (90 Tage Routine, 12 Monate Vorfälle)
- Mitarbeiterrechte (Zugang zu persönlichen Daten, Berichtigung, Beschwerde bei Datenschutzbehörde)

**2. Datenschutzhinweis / Mitarbeiterhandbuch**:

- Detaillierte Erläuterung der DLP-Überwachungspraktiken
- Was überwacht wird (spezifische Kanäle und Systeme)
- Was NICHT überwacht wird (private Geräte ausserhalb des Arbeitskontexts, private Kommunikation über private Konten)
- Wie Daten verwendet werden (nur Sicherheitsvorfallserkennung und -reaktion)
- Wer Zugang hat (Sicherheitsteam, ISB, DSB, Legal — beschränkter Zugang)

**3. Acceptable-Use-Richtlinie**:

- Ausdrückliches Verbot von Datenexfiltration
- Beispiele verbotener Aktivitäten (vertrauliche Daten an private E-Mail senden, Hochladen auf nicht genehmigte Cloud-Speicher)
- Konsequenzen von Richtlinienverstössen (Disziplinarmassnahmen, potenzielle Kündigung)
- Ausnahmeprozess für legitime Geschäftsbedürfnisse

**4. Sicherheitsbewusstseinsschulung**:

- Jährliches Schulungsmodul zu DLP-Zweck und akzeptabler Verwendung
- Benutzerverantwortlichkeiten für Datenschutz
- Ausnahmeanträge für legitime Geschäftstransfers stellen
- Verdächtige Falsch-Positive oder Sicherheitsvorfälle melden

**5. Mitwirkungsorgan-Konsultation** (wo anwendbar):
In Jurisdiktionen, die Mitbestimmung erfordern (Deutschland, Frankreich, Belgien, Niederlande, Schweiz in bestimmten Fällen):

- Mitwirkungsorgan VOR Deployment der DLP-Überwachung konsultieren
- Mitwirkungsorganvereinbarung oder ausgehandelten Kompromiss dokumentieren
- Vereinbarte Schutzmassnahmen implementieren (z.B. verstärkte Datenschutzschutzmassnahmen, begrenzter Protokollzugang)

## A.5 Implementierungscheckliste

Vor dem Deployment der DLP-Überwachung MUSS [Organisation] folgendes abschliessen:

| Anforderung | Status | Abschlussdatum | Verifiziert durch | Nachweis-Speicherort |
|------------|--------|----------------|------------------|---------------------|
| **Rechtliche Überprüfung** | [Abgeschlossen / In Bearbeitung / Nicht begonnen] | [Datum] | [Name — Legal/DSB] | [Dokumentreferenz] |
| **Berechtigtes-Interesse-Beurteilung** (DSGVO Art. 6(1)(f)) | [Status] | [Datum] | [Name — DSB] | [Beurteilungsdokumentpfad] |
| **Verhältnismässigkeitsbeurteilung** | [Status] | [Datum] | [Name — DSB/ISB] | [Beurteilungsdokumentpfad] |
| **Arbeitsverträge aktualisiert** | [Status] | [Datum] | [Name — HR/Legal] | [Vertragsvorlagenversion] |
| **Datenschutzhinweise verteilt** | [Status] | [Datum] | [Name — HR/Kommunikation] | [Verteilungsregisterpfad] |
| **Mitwirkungsorgan-Konsultation** | [Status / N/A] | [Datum] | [Name — HR] | [Konsultationsregisterpfad] |
| **Formelle DSB-Genehmigung** | [Status] | [Datum] | [Name — DSB] | [Genehmigungsdokumentpfad] |
| **Sicherheitsbewusstseinsschulung durchgeführt** | [Status] | [Datum] | [Name — Sicherheitsteam] | [Schulungsabschluss: ___%] |
| **DLP-Protokollzugangskontrolle konfiguriert** | [Status] | [Datum] | [Name — IT-Betrieb] | [Zugangskontrollliste] |
| **Protokollaufbewahrungsrichtlinien konfiguriert** | [Status] | [Datum] | [Name — IT-Betrieb] | [Aufbewahrungsrichtlinie-Konfiguration] |
| **Revisionsdokumentation vollständig** | [Status] | [Datum] | [Name — ISB] | [Compliance-Ordnerpfad] |

**Gesamt-Compliance-Status**: [Alle Abgeschlossen / Teilweise / Unvollständig]
**Freigegeben für Produktionsdeployment**: [JA / NEIN]
**Genehmigt durch**: [Name — ISB] | **Datum**: [Datum]

**Compliance-Status-Verfolgung**: Diese Checkliste MUSS überprüft werden:
- Vierteljährlich (im Rahmen des regulären DLP-Beurteilungsüberprüfungszyklus)
- Bei jeder DLP-Umfangserweiterung (neue Kanäle, neue Jurisdiktionen)
- Bei regulatorischen Änderungen mit Auswirkung auf Mitarbeiterüberwachungsanforderungen

**Kritisch**: Die Nichteinhaltung gesetzlicher Anforderungen kann das DLP-Deployment rechtswidrig machen, [Organisation] regulatorischen Bussgeldern aussetzen (DSG: CHF 250'000, DSGVO: €20 Mio. oder 4% des globalen Jahresumsatzes) und Mitarbeiterbeziehungsprobleme verursachen (Mitwirkungsorganstreitigkeiten, Arbeitsrechtsverletzungen, Mitarbeiterklagen).

## A.6 Regulatorisches Durchsetzungsrisiko

**Schweizer DSG-Durchsetzung**:

- Maximale Busse: CHF 250'000 (individuelle Verstösse)
- Durchsetzung durch den Eidgenössischen Datenschutz- und Öffentlichkeitsbeauftragten (EDÖB)
- Private Klagen durch Mitarbeitende wegen Persönlichkeitsrechtsverletzungen

**EU DSGVO-Durchsetzung**:

- Maximale Busse: €20'000'000 oder 4% des jährlichen globalen Umsatzes (je nachdem, was höher ist)
- EU-Aufsichtsbehörden (Datenschutzbehörden) können Warnungen, Rügen, Verarbeitungsverbote und Bussgelder verhängen
- Private Klagen durch Mitarbeitende auf Schadensersatz (DSGVO Art. 82)
- Sammelklagen durch Mitarbeitervertreter oder Datenschutzorganisationen

**Arbeitsrechtliche Risiken**:

- Rechtswidrige Überwachung kann ein Grund für Kündigung des Arbeitsvertrags durch Mitarbeitende sein
- Mitwirkungsorgane können Überwachung vor Arbeitsgerichten anfechten
- Rechtswidrig erlangter DLP-Nachweis kann in Disziplinarverfahren unzulässig sein

---

# Anhang B: Kurzreferenzhandbuch

**Einseitige Zusammenfassung: Data Leakage Prevention (DLP) für Benutzer**

## Was ist DLP?

Data Leakage Prevention (DLP) schützt sensitive Informationen von [Organisation] vor unbefugter Offenlegung durch technische Überwachung und Richtliniendurchsetzung.

## Was überwacht DLP?

✓ E-Mail (an externe Empfänger)
✓ Web-Uploads (Cloud-Speicher, Dateifreigabe)
✓ USB-Sticks und Wechseldatenträger
✓ Dateiübertragungen (FTP, Cloud-Synchronisation)
✓ Mobilgeräte (Unternehmensdaten)
✓ Applikations-Datenexporte

## Welche Daten sind geschützt?

- **Eingeschränkt**: Hochsensitiv (Legal, regulatorisch, kritisches IP) — Vollständiger DLP-Schutz
- **Vertraulich**: Geschäftssensitiv (Kundendaten, Finanzdaten, interne Dokumente) — DLP-Überwachung und -Blockierung
- **INTERN**: Nur für Organisation (Richtlinien, Verfahren) — DLP-Überwachung (nur Erkennung)
- **Öffentlich**: Kein DLP-Schutz

## Ihre Verantwortlichkeiten

✅ **Sensitive Daten korrekt behandeln**: Klassifizierungs- und Acceptable-Use-Richtlinien befolgen
✅ **Genehmigte Kanäle verwenden**: Unternehmens-E-Mail, genehmigter Cloud-Speicher (OneDrive, SharePoint)
✅ **Ausnahmen beantragen**: Sicherheitsteam für legitime Geschäftsbedürfnisse kontaktieren, die DLP-Ausnahme erfordern
✅ **Probleme melden**: Falsch-Positive, dringende Geschäftsbedürfnisse, verdächtige Sicherheitsvorfälle
❌ **NICHT TUN**: DLP-Steuerungen zu umgehen versuchen (Proxy, Verschlüsselung, nicht genehmigter Cloud-Speicher)

## Wenn DLP Ihren Transfer blockiert

1. **Datenklassifizierung prüfen**: Sind dies tatsächlich Vertrauliche/Eingeschränkte Daten?
2. **Genehmigte Methode verwenden**: Unternehmens-E-Mail, verschlüsselter Transfer, sichere Dateifreigabe
3. **Ausnahme beantragen**: Bei legitimem Geschäftsbedarf das Sicherheitsteam kontaktieren
4. **Helpdesk kontaktieren**: Für dringende Unterstützung oder Falsch-Positiv-Meldung

## Rechtlicher Hinweis — Mitarbeiterüberwachung

[Organisation] überwacht Datentransfers zu Sicherheitszwecken in Übereinstimmung mit Schweizer DSG (Art. 328b OR) und EU DSGVO (Art. 88). Die Überwachung ist auf Ausgangskanäle beschränkt, auf den Schutz sensitiver Daten ausgerichtet und unterliegt Verhältnismässigkeitsgrundsätzen. Sie wurden über diese Überwachung durch Ihren Arbeitsvertrag und diesen Hinweis informiert. DLP-Protokolle werden 90 Tage (Routine) und 12 Monate (Sicherheitsvorfälle) aufbewahrt und sind nur für Sicherheitsteam, ISB und DSB auf Need-to-Know-Basis zugänglich.

## Fragen oder Bedenken?

- **Sicherheitsteam**: security@[organisation].example
- **Helpdesk**: helpdesk@[organisation].example (dringende Transfersperrungen)
- **Datenschutzbeauftragter (DSB)**: dpo@[organisation].example (Datenschutzbedenken)

**Vielen Dank, dass Sie zum Schutz der Informationsassets von [Organisation] beitragen.**

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date] |
| **IT-Leiter (ITL)** | [Name] | [Date] |
| **Datenschutzbeauftragter (DSB)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Geschäftsleitung** | [Name] | [Date] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen zur Verhinderung von Datenleckagen fest. Implementierungsverfahren, technische Standards und Beurteilungsarbeitsmappen sind in ISMS-IMP-A.8.12 (UG/TG) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
