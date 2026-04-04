<!-- ISMS-CORE:REF:ISMS-REF-A.8.10-referenz-loeschmethoden-DE:framework:REF:a.8.10 -->
**ISMS-REF-A.8.10 — Referenz Löschmethoden**
**Mediensanitierungsstandards und Tool-Auswahl (Technische Nicht-ISMS-Referenz)**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Referenz Löschmethoden |
| **Dokumententyp** | Intern – Technische Referenz (nicht ISMS) |
| **Dokument-ID** | ISMS-REF-A.8.10 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | ISB (Technische Referenz – keine Executive-Genehmigung erforderlich) |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | INTERN |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB / IT-Betrieb | Erstversion als technische Referenz für ISO 27001:2022-Zertifizierung |

**Überprüfungszyklus**: Bei Bedarf (Technologie- und Tool-Entwicklung)
**Nächstes Überprüfungsdatum**: [Date + 12 months]
**Genehmiger**: IT-Operations-Manager / Security Architecture (technische Referenz, keine ISMS-Genehmigung erforderlich)

**Verteilung**: IT-Betrieb, Security Engineering, Systemeigentümer (zur technischen Implementierungsbewusstsein)

---

⚠️ **WICHTIG – NICHT-ISMS TECHNISCHES UNTERSTÜTZUNGSDOKUMENT**

Dieses Dokument dient ausschliesslich Informations- und Bewusstseinszwecken.

- Dieses Dokument ist **NICHT** Bestandteil des Informationssicherheits-Managementsystems (ISMS).
- Dieses Dokument definiert **KEINE** verbindlichen Löschkontrollen oder -anforderungen.
- Dieses Dokument begründet **KEINE** verbindlichen Anforderungen, Fristen, KPIs oder SLAs.
- Dieses Dokument schreibt **NICHT** die Verwendung, das Verbot oder die Konfiguration spezifischer Löschtools, Anbieter oder Plattformen vor.
- Dieses Dokument setzt **KEINE** ISMS-Richtlinie ausser Kraft oder erweitert sie.

Alle verbindlichen Löschanforderungen, Verpflichtungen und Governance-Entscheidungen sind ausschliesslich in **ISMS-POL-A.8.10 (Richtlinie zur Informationslöschung)** und anderen genehmigten ISMS-Dokumenten definiert.

Dieses Dokument dient ausschliesslich als technische Referenz zur:

- Beschreibung häufig verwendeter Löschmethoden und Mediensanitierungstechniken
- Verfolgung der Entwicklung von Industriestandards und Tool-Verfügbarkeit
- Unterstützung des Bewusstseins bei der Löschmethodenauswahl
- Information technischer Diskussionen und zukünftiger Implementierungsplanung
- **Dieses Dokument darf nicht als Prüfungsnachweis für die Implementierung verwendet werden**

Die Verwendung dieses Dokuments impliziert weder Implementierung, Compliance noch operative Reife.

**Kritische Positionierungsaussage**:
Dieses Dokument stellt absichtlich technische Details bereit, die über die für ISO/IEC 27001-Richtliniendokumentation erforderlichen hinausgehen. Es dient ausschliesslich der technischen Bewusstseinssteigerung. Kein Prüfer sollte Schlussfolgerungen aus dem Vorhandensein, der Abwesenheit oder der Klassifizierung von Löschmethoden, Tools oder Anbietern in diesem Dokument ziehen.

---

**Dokumentzweck und Geltungsbereich**

**Zweck**

Dieses Dokument bietet einen technischen Überblick über Löschmethoden und Mediensanitierungstechniken, die häufig zur Informationslöschung eingesetzt werden. Es dient der Unterstützung bei:

- Technischem Bewusstsein für verfügbare Löschoptionen
- Verständnis der Methodenwirksamkeit nach Medientyp
- Kontext für die Löschmethodenauswahl bei der Implementierung
- Planung zukünftiger Implementierungen
- Tool-Bewertungskriterien

## Was dieses Dokument NICHT ist

Dieses Dokument:

- Definiert NICHT die genehmigten oder verbotenen Löschmethoden von [Organisation]
- Begründet KEINE verbindlichen Implementierungsanforderungen
- Schafft KEINE Compliance-Verpflichtungen oder Prüfungskriterien
- Ersetzt NICHT die Anforderungen der ISMS-POL-A.8.10
- Schreibt KEINE spezifische Tool-Auswahl oder Lieferantenbeziehungen vor
- Etabliert KEINE Löschverfahren oder Verifizierungsprozesse

## Beziehung zum ISMS

**Beziehung zu POL-A.8.10 Anhang A**: ISMS-POL-A.8.10 Anhang A (Genehmigte Löschmethoden-Matrix) stellt den **verbindlichen Organisationsstandard** für die Löschmethodenauswahl bereit. Diese technische Referenz (ISMS-REF-A.8.10) bietet zusätzliche technische Details und Kontext zur Unterstützung des Richtlinien-Anhangs, ersetzt aber keine Richtlinienanforderungen.

---

# NIST SP 800-88 Sanitierungsrahmenwerk

## Überblick

NIST Special Publication 800-88 Revision 1 («Leitfaden zur Mediensanitierung») bietet massgebliche Hinweise zu Mediensanitierungsmethoden. Obwohl es sich um eine informative Referenz handelt (nicht verbindlich, sofern nicht vertraglich gefordert), stellt es Industry Best Practice dar.

**Drei Sanitierungskategorien**:

1. **Clear**: Anwendung logischer Techniken zum Sanitieren von Daten in allen benutzeradressierbaren Speicherorten zum Schutz vor einfachen nicht-invasiven Datenwiederherstellungstechniken
2. **Purge**: Anwendung physischer oder logischer Techniken, um die Zieldatenwiederherstellung mit modernsten Labor-Techniken nicht machbar zu machen
3. **Destroy**: Unbrauchbarmachen des Mediums und Unüblichmachen der Zieldatenwiederherstellung mit modernsten Labor-Techniken

## Entscheidungsfaktoren für die Methodenauswahl

**Medienziel**:

- Verbleib in Organisationskontrolle → Clear ggf. ausreichend (abhängig von Klassifizierung)
- Verlässt Organisationskontrolle → Purge Minimum
- Entsorgung / End-of-Life → Destroy empfohlen für sensible Daten

**Datenklassifizierung**:

- Öffentliche Daten → Clear ausreichend
- Interne Daten → Clear oder Purge
- Vertrauliche Daten → Purge Minimum
- Eingeschränkte Daten → Destroy oder Purge mit Verifizierung

**Medienwiederverwendungsabsicht**:

- Wiederverwendung innerhalb der Organisation → Clear oder Purge
- Verkauf/Spende extern → Purge oder Destroy
- Entsorgung → Destroy

---

# Löschung magnetischer Medien (HDDs, Band)

## Festplatten (HDD)

**Medieneigenschaften**:

- Daten magnetisch auf rotierenden Scheiben gespeichert
- Standarddateilöschung entfernt nur Dateisystem-Zeiger, nicht die eigentlichen Daten
- Daten bleiben wiederherstellbar bis zur Überschreibung
- Gut etablierte Sanitierungsmethoden

**3.1.1 Clear-Methoden**

**Einmaliges Überschreiben**:

- Muster über alle adressierbaren Speicherorte schreiben
- NIST SP 800-88: Einzeldurchlauf für moderne Laufwerke ausreichend
- Legacy-Mehrfachdurchlauf-Methoden (DoD 5220.22-M 7-Durchläufe) gemäss NIST nicht länger notwendig
- Tools: `shred` (Linux), `sdelete` (Windows), `dd` (Unix/Linux)
- Wirksamkeit: Ausreichend für nicht sensible Daten, interne Wiederverwendung
- Einschränkungen: Adressiert keine defekten Sektoren oder firmware-reservierte Bereiche

**3.1.2 Purge-Methoden**

**ATA Secure Erase**:

- Eingebauter Laufwerksbefehl, der alle adressierbaren Speicherorte einschliesslich remappter Sektoren überschreibt
- Hersteller-implementiert, nutzt Controller-Kenntnis aller Speicherbereiche
- Einzelbefehl, schnelle Ausführung (typisch 1–4 Stunden für moderne Laufwerke)
- Tools: `hdparm` (Linux), Parted Magic, Hersteller-Utilities
- Wirksamkeit: Sehr hoch für HDDs, empfohlene Methode
- Verifizierung: SMART-Daten oder ATA-Befehlsabschlussstatus prüfen

**Entmagnetisieren (Degaussing)**:

- Laufwerk einem starken Magnetfeld aussetzen, um magnetische Domänen zu stören
- Macht Laufwerk dauerhaft funktionsuntüchtig (kann nicht wiederverwendet werden)
- Erfordert NSA Evaluated Products List (EPL)-Entmagnetisierer für klassifizierte Daten
- Wirksamkeit: Sehr hoch für magnetische Medien
- Einschränkungen: Laufwerk nach Entmagnetisierung unbrauchbar; teures Equipment erforderlich
- Anwendungsfall: Hochsicherheitsumgebungen, Entsorgung klassifizierter Daten

**3.1.3 Destroy-Methoden**

**Physische Desintegration**:

- Laufwerk in kleine Partikel schreddern (≤2 mm empfohlen gemäss DIN 66399)
- Verbrennen bei hoher Temperatur
- Pulverisieren
- Einschmelzen
- Anbieter-Services: NAID AAA-zertifizierte Vernichtungsanbieter
- Wirksamkeit: Höchste Stufe, Datenwiederherstellung nicht machbar
- Anwendungsfall: Höchstsensible Daten, End-of-Life-Entsorgung

**3.1.4 Kryptografische Löschung**

**Selbstverschlüsselnde Laufwerke (SED)**:

- Hardware-basierte Gesamtdatenträgerverschlüsselung
- Daten mit Data Encryption Key (DEK) verschlüsselt; DEK mit Authentication Key (AK) verschlüsselt
- Sanitierung: Kryptografische Schlüssel vernichten
- Tools: Hersteller-SED-Management-Utilities, sedutil
- Wirksamkeit: Sehr hoch WENN Verschlüsselung ab Inbetriebnahme aktiviert war
- Einschränkungen: Nur wirksam wenn Laufwerk verschlüsselt war; Verschlüsselungsstatus vor Crypto-Erase verifizieren

## Magnetband

**Medieneigenschaften**:

- Sequenzielles Zugriffs-Medium
- Häufig für Backup und Archivierung
- Mehrfache Lese-/Schreibvorgänge über dasselbe Medium

**3.2.1 Clear-Methode**

**Vollständige Bandüberschreibung**:

- Muster über die gesamte Bandlänge schreiben
- Zeitaufwändig (Stunden pro Band)
- Tools: Native Überschreibbefehle des Bandlaufwerks
- Wirksamkeit: Ausreichend für interne Wiederverwendung
- Einschränkung: Sehr langsam; adressiert keine beschädigten Bandsegmente

**3.2.2 Purge-Methode**

**Entmagnetisieren (Degaussing)**:

- Bevorzugte Methode für Bandmedien
- Schnell (Sekunden pro Band)
- Macht Band für zukünftige Verwendung unbrauchbar
- Erfordert NSA EPL-Entmagnetisierer für sensible Daten
- Wirksamkeit: Sehr hoch
- Anwendungsfall: Entsorgung sensibler Backup-Bänder, Stilllegung

**3.2.3 Destroy-Methode**

**Physische Vernichtung**:

- Schreddern
- Verbrennen
- Pulverisieren
- Wirksamkeit: Höchste
- Anwendungsfall: End-of-Life, höchste Sensitivität

---

# Löschung von Solid-State-Medien (SSD, NVMe, Flash)

## Eigenschaften von Solid-State-Medien

**Warum SSDs anders sind**:

- Wear-Leveling-Algorithmen verteilen Schreibvorgänge über alle Zellen
- Overprovisioning reserviert für das Betriebssystem nicht sichtbare Speicherzellen
- Garbage Collection verschiebt Datenblöcke
- TRIM-Befehl verwaltet gelöschte Blöcke
- Ergebnis: Standardüberschreibung sanitiert SSDs **NICHT** zuverlässig

**Sanitierungsherausforderungen**:

- Kann nicht garantieren, dass alle physischen Speicherorte überschrieben werden
- Firmware kontrolliert die tatsächliche Datemplatzierung
- Versteckte Bereiche (Overprovisioning, Fehlblock-Remapping)

## SSD / NVMe Sanitierungsmethoden

**4.2.1 Purge-Methoden**

**ATA Secure Erase / NVMe Sanitize**:

- Hersteller-implementierter Befehl
- SSD: ATA Security Erase-Befehl; NVMe: NVMe Sanitize (Crypto Erase oder Block Erase)
- Nutzt Firmware-Kenntnis aller Speicherzellen
- Tools: `nvme-cli` (NVMe), `hdparm` (SATA SSD), Parted Magic
- Wirksamkeit: Hoch (wenn vom Hersteller korrekt implementiert)
- Verifizierung: Tool-Abschlussstatus; Datenwiederherstellungsstichproben
- Achtung: Implementierungsqualität variiert je nach Hersteller

**Kryptografische Löschung**:

- Selbstverschlüsselnde Laufwerke (SED) oder softwarebasierte FDE
- Verschlüsselungsschlüssel vernichten, um Daten unzugänglich zu machen
- Sehr schnell (Sekunden)
- Tools: Hersteller-SED-Utilities, OS-FDE-Tools (BitLocker, FileVault, LUKS)
- Wirksamkeit: Sehr hoch WENN Laufwerk ab Inbetriebnahme verschlüsselt war
- **Kritische Anforderung**: Verschlüsselung verifizieren; nach Deployment aktivierte Verschlüsselung weniger wirksam
- Bevorzugte Methode für SSDs wo Verschlüsselung aktiviert

**4.2.2 Destroy-Methode**

**Physische Vernichtung**:

- Schreddern auf ≤2 mm-Partikel
- Desintegration
- Pulverisieren
- Verbrennen
- Wirksamkeit: Höchste, Datenwiederherstellung nicht machbar
- Anwendungsfall: Hochsensible Daten; wenn Secure Erase nicht verifiziert wirksam
- Hinweis: Kostspielig bei grossen Volumen

**4.2.3 NICHT empfohlen für SSDs**

❌ **Standard-Überschreiben**: Wegen Wear-Leveling und Overprovisioning unwirksam
❌ **Einzeldatei-Löschtools**: Sanitieren keinen gelöschten Speicherplatz auf SSDs
❌ **Mehrfachdurchlauf-Überschreiben**: Kein Zusatznutzen gegenüber Einzeldurchlauf, verschwendet Schreibzyklen

## USB-Flash-Laufwerke / SD-Karten

**Sanitierung**:

- Ähnliche Herausforderungen wie SSDs (Flash-Speicher, Wear-Leveling)
- Secure Erase: Falls unterstützt (bei Consumer-USB-Laufwerken selten)
- Kryptografische Löschung: Falls verschlüsselt (BitLocker To Go, hardware-verschlüsselte Laufwerke)
- **Praktischer Ansatz**: Physische Vernichtung oft zuverlässigste Methode
- Schreddern oder verbrennen für sensible Daten
- Günstige Medien machen Vernichtung wirtschaftlich vertretbar

---

# Cloud-Speicherlöschung

## Herausforderungen bei der Cloud-Löschung

**Multi-Tenancy**:

- Kundendaten logisch getrennt, aber physisch gemeinsam genutzt
- Risiko von Datenremanenzen oder mandantenübergreifender Leckage
- Abhängigkeit von Isolationskontrollen des Anbieters

**Datenverteilung**:

- Daten über mehrere geografische Standorte repliziert
- Mehrere Availability Zones und Regionen
- Backup-Kopien vom Anbieter verwaltet

**Eingeschränkte Kontrolle**:

- Kein physischer Zugang zu Speichermedien
- Abhängigkeit von Anbieter-Lösch-APIs und -verfahren
- Vertrauen auf Anbieter-Implementierung

## Cloud-Löschmethoden

**5.2.1 Logische Löschung (Clear)**

**API-basierte Löschung**:

- Cloud-Anbieter-API zur Löschung von Objekten, Volumes, Datenbanken verwenden
- Beispiele: AWS S3 DeleteObject, Azure Blob Delete, GCP Storage Delete
- Verifizierung: API-Antwortcodes (200/204 Erfolg)
- Wirksamkeit: Entfernt logischen Zugang; Anbieter bereinigt physischen Speicher gemäss eigenem Zeitplan
- Einschränkung: Vertrauen auf Anbieter für physische Speichersanitierung

**5.2.2 Kryptografische Löschung (Purge – Bevorzugt)**

**Kundenverwaltete Verschlüsselungsschlüssel**:

- Daten mit kundenverwalteten Schlüsseln (CMK) verschlüsseln
- AWS: KMS Customer Managed Keys, S3 SSE-C
- Azure: Customer Managed Keys (CMK), Azure Key Vault
- GCP: Customer-Managed Encryption Keys (CMEK)
- Löschung: Verschlüsselungsschlüssel vernichten, Daten unzugänglich machen
- Verifizierung: Schlüsselvernichtung im Key-Management-Service bestätigen
- Wirksamkeit: Sehr hoch; Daten kryptografisch nicht wiederherstellbar
- **Empfohlener Ansatz**: API-Löschung + Schlüsselvernichtung kombinieren

**5.2.3 Anbieter-Löschzertifikate**

Einige Cloud-Anbieter bieten Löschbestätigungen an:

- AWS: Löschbestätigung über CloudTrail-Protokolle
- Azure: Prüfprotokolle
- GCP: Cloud Audit Logs
- Drittanbieter-Zertifizierung: SOC 2 Type II-Berichte zu Löschkontrollen
- Anwendungsfall: Vertragliche Löschnachweise, regulatorische Compliance

## Cloud-Anbieter-Löschung nach Dienstmodell

**IaaS (Compute, Storage)**:

- Virtuelle Maschinen: Instanz beenden + EBS-Volumes/Managed Disks löschen
- Objektspeicher: API-Objekte löschen + Bucket löschen + CMK vernichten
- Blockspeicher: Volumes + Snapshots + Backups löschen
- Verifizierung: API-Antworten, Service-Console-Bestätigung

**PaaS (Datenbanken, Anwendungen)**:

- Datenbanken: Datenbankinstanz + automatische Backups + manuelle Snapshots löschen
- Anwendungsdienste: Anwendung + Datenspeicher + Protokolle löschen
- Verifizierung: Dienstspezifische Löschbestätigungen

**SaaS (Anwendungen)**:

- Löschung auf Anwendungsebene (z.B. Benutzerkonto in SaaS-App löschen)
- Datenexport vor Löschung anfordern (GDPR-Portabilität)
- Löschbestätigung vom SaaS-Anbieter einholen
- Einschränkung: Minimale Kontrolle; vollständige Abhängigkeit von Anbieterverfahren

---

# Mobilgeräte

## Smartphones und Tablets

**Sanitierungsansatz**:

**Verschlüsselte Geräte** (Modernes iOS, Android mit aktivierter Verschlüsselung):
1. Mobile Device Management (MDM) Remote-Wipe
2. Werksreset
3. Vernichtung des Verschlüsselungsschlüssels
4. Verifizierung: MDM-Konsole-Bestätigung; Gerätezugangversuch nach Wipe
5. Wirksamkeit: Hoch für korrekt verschlüsselte Geräte

**Nicht verschlüsselte oder unbekannte Verschlüsselung**:
1. Physische Vernichtung des Speicherkomponenten (entfernen und schreddern)
2. Anwendungsfall: Hochsensible Daten auf älteren Geräten
3. Wirksamkeit: Höchste

**Tools**:

- MDM-Lösungen: Microsoft Intune, Jamf Pro, VMware Workspace ONE, MobileIron
- Nativ: iOS «Alle Inhalte und Einstellungen löschen», Android-Werksreset
- Verifizierung: MDM-Check-in-Versuch nach Wipe

## Laptops und Desktops

**Sanitierung**:

- Magnetische HDD: ATA Secure Erase oder physische Vernichtung
- SSD: Kryptografische Löschung (BitLocker, FileVault) oder physische Vernichtung
- Hybrid (HDD + SSD-Cache): Beide Komponenten sanitieren
- Ansatz: Speichermedien ausbauen, separat mit medienspezifischen Methoden sanitieren

---

# Papier und optische Medien

## Papierdokumente

**Schredder-Standards (DIN 66399)**:

| Sicherheitsstufe | Partikelgrösse | Anwendungsfall |
|-----------------|----------------|----------------|
| P-1 | <12 mm Streifen | Allgemeiner Abfall, keine Vertraulichkeit |
| P-2 | <6 mm Streifen | Interne Dokumente, geringe Sensitivität |
| P-3 | <2 mm Streifen oder 320 mm² Partikel | Vertrauliche Geschäftsdokumente |
| **P-4** | <2 mm Streifen oder 160 mm² Partikel | **Vertrauliche Daten, PII (empfohlenes Minimum)** |
| **P-5** | <0,8 mm Streifen oder 30 mm² Partikel | **Hochsensible PII, Eingeschränkte Daten** |
| P-6 | <1 mm Streifen oder 10 mm² Partikel | Klassifizierte Behördendaten |
| P-7 | ≤5 mm² Partikel | Streng geheime Daten |

**Methoden**:

- Kreuzschnitt-Schreddern (P-4 oder P-5 Minimum für sensible Daten)
- Grosse Volumen: Beauftragter Vernichtungsservice (NAID AAA-zertifizierter Anbieter)
- Vernichtungsnachweis erforderlich für vertrauliche/eingeschränkte Dokumente

**Vor-Ort vs. Auswärts**:

- Vor-Ort-Schreddern: Sofortige Vernichtung, Verwahrkette erhalten
- Auswärts-Schreddern: Abgesperrte Behälter, geplante Abholung, Zertifikat bereitgestellt
- Hochsensitiv: Vor-Ort-bezeugte Vernichtung bevorzugt

## Optische Medien (CD, DVD, Blu-ray)

**Eigenschaften**:

- Einmalig beschreibbare Medien (können nicht überschrieben werden)
- Physische Vernichtung erforderlich

**Methoden**:

- Physisches Schreddern (kleine Partikel)
- Verbrennen
- Desintegration
- NICHT AKZEPTABEL: Kratzen, Brechen (Daten oft wiederherstellbar)

---

# Virtuelle Umgebungen

## Virtuelle Maschinen

**Löschungsumfang**:

- Virtuelle Festplatten-Dateien (VMDK, VHD, VHDX, qcow2)
- Snapshots (alle Snapshot-Dateien)
- Vorlagen (aus dieser VM erstellte VM-Vorlagen)
- Konfigurationsdateien
- Auslagerungsdateien

**Methoden**:

- **Standard**: VM + alle zugehörigen Dateien über Hypervisor löschen
- **Sicher**: Virtuelle Festplatten-Dateien sicher wischen vor VM-Löschung
- **Crypto Erase**: Falls virtuelle Festplatte verschlüsselt, Verschlüsselungsschlüssel vernichten
- Tools: Hypervisor-Management (vSphere, Hyper-V, KVM), `shred` für Festplatten-Dateien

## Container und Container-Images

**Löschungsumfang**:

- Container-Instanzen
- Container-Images (lokal und in Registry)
- Persistente Volumes
- Secrets und Konfiguration

**Methoden**:

- Container stoppen und entfernen: `docker rm`, `kubectl delete pod`
- Images löschen: `docker rmi`, Registry-Löschung
- Volumes löschen: `docker volume rm`, `kubectl delete pvc`
- Registry-Bereinigung: Images aus Container-Registry entfernen

## Datenbanken

**Löschmethoden**:

**Logische Löschung**:

- `DELETE FROM table WHERE ...` (Zeilen entfernen)
- `DROP TABLE` (Tabellenstruktur und Daten entfernen)
- `DROP DATABASE` (gesamte Datenbank entfernen)
- Folgemassnahme: `VACUUM` (PostgreSQL), `OPTIMIZE TABLE` (MySQL) zur Speicherrückgewinnung
- Einschränkung: Daten können in Transaktionsprotokollen, temporären Dateien verbleiben

**Kryptografische Löschung** (Transparent Data Encryption aktiviert):

- Verschlüsselte Datenbank löschen
- Verschlüsselungsschlüssel vernichten
- Wirksamkeit: Hoch für TDE-fähige Datenbanken
- Beispiele: SQL Server TDE, Oracle TDE, PostgreSQL pgcrypto

**Physische Löschung**:

- Datenbankdateien nach logischer Löschung löschen
- Zugrunde liegendes Speichermedium sicher wischen
- Transaktionsprotokolle, Backup-Dateien, temporäre Dateien einbeziehen

**Backup-Löschung**:

- Kritisch: Datenbank-Backups löschen, wenn Produktionsdatenbank gelöscht
- Einschliesslich vollständiger Backups, differentieller Backups, Transaktionsprotokolle, Snapshots

---

# Beispiele zugelassener Tools (Informativ)

**⚠️ KRITISCHER HAFTUNGSAUSSCHLUSS**: Die in diesem Abschnitt aufgeführten Tools und Anbieter dienen ausschliesslich **Bewusstseinszwecken**. Ihre Auflistung stellt NICHT dar:
- Genehmigung oder Empfehlung durch [Organisation]
- Befürwortung spezifischer Produkte oder Anbieter
- Zertifizierung, dass Tools den Anforderungen von [Organisation] entsprechen
- Garantie der Tool-Wirksamkeit oder -Eignung

[Organisation] wählt Löschtools durch formale Bewertung basierend auf Risikobewertung, Betriebsanforderungen, regulatorischer Compliance und Anbieter-Validierung gemäss ISMS-IMP-A.8.10.2 aus.

## Open-Source / Eingebaute Tools

**Überschreiben**:

- `shred` (Linux) – Datei- und Laufwerksüberschreibung
- `dd` (Unix/Linux) – Festplatten-Schreiben und -Wischen
- `sdelete` (Windows Sysinternals) – Sichere Löschung
- `wipe` (Linux) – Sichere Dateilöschung

**Secure Erase**:

- `hdparm` (Linux) – ATA Secure Erase für HDDs/SSDs
- `nvme-cli` (Linux) – NVMe Sanitize-Befehle
- Parted Magic (Bootfähiges Linux) – Laufwerks-Sanitierungs-Suite

**Verschlüsselung**:

- BitLocker (Windows) – Gesamtdatenträgerverschlüsselung
- FileVault (macOS) – Gesamtdatenträgerverschlüsselung
- LUKS (Linux) – Festplattenverschlüsselung
- VeraCrypt – Plattformübergreifende Verschlüsselung

## Kommerzielle Tools

**Unternehmens-Löschsoftware**:

- Blancco Drive Eraser – Zertifizierte Datenlöschung, Zertifikatserstellung
- White Canyon WipeDrive – Plattformübergreifendes Laufwerks-Wischen
- DBAN (Darik's Boot and Nuke) – Kostenlose HDD-Wischsoftware (Legacy, nicht mehr gepflegt)
- Ontrack Eraser – Zertifizierte Löschlösung

**Physische Vernichtungsgeräte**:

- Entmagnetisierer: Garner, Proton Data Security, VS Security Products
- Schredder: HSM, Whitaker Brothers, SEM, MBM

**MDM-Lösungen**:

- Microsoft Intune
- Jamf Pro (Apple-Geräte)
- VMware Workspace ONE
- MobileIron / Ivanti

## Cloud-native Tools

**AWS**:

- AWS CLI (Löschoperationen)
- AWS KMS (Schlüsselmanagement und -vernichtung)
- AWS Backup (Backup-Löschung)

**Azure**:

- Azure CLI / PowerShell (Löschoperationen)
- Azure Key Vault (Schlüsselmanagement)
- Azure Backup (Backup-Löschung)

**GCP**:

- gcloud CLI (Löschoperationen)
- Cloud KMS (Schlüsselmanagement)
- Cloud Backup (Backup-Löschung)

---

# Cloud-Anbieter-Löschfähigkeiten

**Aktualitätshinweis**: Cloud-Anbieter-Fähigkeiten entwickeln sich rasch. Diese Referenz spiegelt die Fähigkeiten zum Zeitpunkt [Dokumentdatum] wider. Organisationen sollten aktuelle Anbieter-Löschfähigkeiten bei der Cloud-Anbieter-Bewertung gemäss ISMS-POL-A.8.10 Abschnitt 2.3 verifizieren und Ergebnisse in ISMS-REF-A.5.23 dokumentieren.

## Hyperscale-Anbieter (Tier 1)

**Amazon Web Services (AWS)**:

- Lösch-APIs: S3 DeleteObject, EC2 TerminateInstances, RDS DeleteDBInstance
- Verschlüsselung: KMS Customer-Managed Keys (CMK)
- Verifizierung: CloudTrail-Protokolle, API-Antworten
- Zertifizierungen: SOC 2 Type II, ISO 27001, ISO 27017, ISO 27018

**Microsoft Azure**:

- Lösch-APIs: Storage Delete, VM Delete, SQL Database Delete
- Verschlüsselung: Customer Managed Keys (CMK) via Azure Key Vault
- Verifizierung: Azure Monitor-Protokolle, Aktivitätsprotokolle
- Zertifizierungen: SOC 2 Type II, ISO 27001, ISO 27017, ISO 27018

**Google Cloud Platform (GCP)**:

- Lösch-APIs: Storage Delete, Compute Instance Delete, Cloud SQL Delete
- Verschlüsselung: Customer-Managed Encryption Keys (CMEK)
- Verifizierung: Cloud Audit Logs, Stackdriver-Protokollierung
- Zertifizierungen: SOC 2 Type II, ISO 27001, ISO 27017, ISO 27018

**Gemeinsame Fähigkeiten**:

- API-basierte programmatische Löschung
- Kundenverwaltete Verschlüsselungsschlüssel
- Prüfprotokollierung von Löschoperationen
- Multi-Regions-Löschunterstützung
- Zertifizierungen zu Löschkontrollen

## Andere Cloud-Anbieter

Für Tier 2–10-Anbieter gemäss ISMS-REF-A.5.23:

- Löschfähigkeiten bei Anbieterbewertung prüfen
- Lösch-SLA vertraglich vereinbaren
- Löschzertifikate oder Bestätigungen einholen
- Multi-Mandanten-Isolationsverfahren prüfen
- SOC 2 Type II-Berichte zu Löschkontrollen prüfen

---

# Verifizierung und Validierung

## Verifizierungsmethoden

**Automatisierte Verifizierung**:

- Tool-Abschlussstatus (Exit-Codes, Protokolle)
- API-Antwortcodes (HTTP 200/204 bei erfolgreicher Löschung)
- MDM-Konsole-Bestätigung (Mobilgeräte-Wipes)
- Key-Management-System-Protokolle (Verschlüsselungsschlüssel-Vernichtung)

**Manuelle Verifizierung**:

- Stichprobenprüfung: Zufällige Medien auswählen, Datenwiederherstellung versuchen
- Forensische Validierung: Wiederherstellungstools auf sanitierten Medien verwenden
- Sichtprüfung: Verifizierung physischer Vernichtung
- Zertifikatsprüfung: Vernichtungsnachweise Dritter prüfen

**Verifizierung Dritter**:

- Vernichtungsnachweise von zertifizierten Anbietern
- SOC 2 Type II-Prüfberichte (Verifizierung der Löschkontrollen)
- Cloud-Anbieter-Löschbestätigungen

## Stichprobenrichtlinien

Bei Grosslöschoperationen:

- 5–10 % der Löschereignisse stichprobenweise prüfen
- Höhere Stichprobenrate (10–20 %) bei hochsensiblen Daten
- Stichprobenprüfung bei neuen Löschmethoden oder Tools fokussieren
- Stichprobenergebnisse und etwaige Fehler dokumentieren

## Fehlerbehandlung

Bei Verifizierungsversagen:

- Löschmethode sofort einstellen
- Medien zur erneuten Sanitierung unter Quarantäne stellen
- IT-Security-Team eskalieren
- Robustere Löschmethode verwenden (z.B. physische Vernichtung)
- Versagen für Lessons Learned dokumentieren

---

# Industriestandards-Referenz

**NIST Special Publications**:

- **NIST SP 800-88 Rev. 1**: Leitfaden zur Mediensanitierung (primäre Referenz)
- NIST SP 800-53 Rev. 5: Sicherheitskontrollen (MP-Familie – Medienschutz)
- NIST SP 800-171: Schutz von CUI (Mediensanitierungsanforderungen)

**ISO-Normen**:

- ISO/IEC 27040:2015: Speichersicherheit (Sanitierungsleitfaden)
- ISO/IEC 27555:2021: Leitlinien zur PII-Löschung
- ISO/IEC 27017:2015: Cloud-Dienste-Sicherheit (Löschanforderungen)

**Industriestandards**:

- **DIN 66399**: Vernichtung von Datenträgern (Papier-Schredder-Stufen)
- IEEE 2883-2022: Standard zur Speichersanitierung
- ANSI/NAID AAA: Sichere Vernichtungsstandards (Dienstleister)

**Ältere Referenzen** (überholt, können aber in Verträgen erscheinen):

- DoD 5220.22-M: Datensanitierung (von NIST SP 800-88 abgelöst)
- NSA/CSS Manual 130-2: Datensanitierung (klassifizierte Daten, überholt)

---

# Anhang A: Arbeitsblatt zur Auswahl der Löschmethode

Organisationen können dieses Arbeitsblatt bei der Implementierung verwenden, um Entscheidungen zur Löschmethodenauswahl zu dokumentieren:

**Datenkategorie**: _______________________
**Klassifizierungsstufe**: ⬜ Öffentlich ⬜ Intern ⬜ Vertraulich ⬜ Eingeschränkt

**Medientyp**: _______________________
**Medienziel**: ⬜ Interne Wiederverwendung ⬜ Externe Übertragung ⬜ Entsorgung

**Empfohlene Methode** (basierend auf NIST SP 800-88 und Datenklassifizierung):

- Clear: _______________________
- Purge: _______________________
- Destroy: _______________________

**Gewählte Methode**: _______________________
**Begründung**: _______________________

**Tool/Anbieter**: _______________________
**Verifizierungsmethode**: _______________________

**Genehmigt von**: _______________________
**Datum**: _______________________

**Genehmigungsworkflow**:
- Technische Machbarkeit geprüft von: _______________________ (IT-Betrieb)
- Risikobewertung geprüft von: _______________________ (Security-Team)
- Endgenehmigung gemäss POL-A.8.10 Abschnitt 2.2 durch: _______________________ (ISB oder Delegierter)

**Hinweis**: Dieses Arbeitsblatt unterstützt Entscheidungen zur Löschmethodenauswahl, die in ISMS-IMP-A.8.10.2 (Löschmethoden-Bewertung) dokumentiert werden. Ausgefüllte Arbeitsblätter werden mit Implementierungsnachweisen abgelegt.

---

**ENDE DER TECHNISCHEN REFERENZ**

---

*Diese technische Referenz unterstützt die Implementierung von ISMS-POL-A.8.10. Alle verbindlichen Anforderungen sind im Richtliniendokument definiert.*

**DIESES DOKUMENT IST NICHT BESTANDTEIL DES ISMS.**

<!-- QA_VERIFIED: 2026-03-28 -->
