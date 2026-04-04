<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.12-DE:operational:OP-POL:a.8.12 -->
**ISMS-OP-POL-A.8.12 — Prävention von Datenlecks**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Prävention von Datenlecks |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.12 |
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

- ISO/IEC 27001:2022 Massnahme A.8.12 — Prävention von Datenlecks
- ISO/IEC 27002:2022 Abschnitt 8.12 — Implementierungsleitfaden für Massnahmen zur Prävention von Datenlecks
- NIST SP 800-53 Rev 5 — AC-4 (Information Flow Enforcement), SC-7 (Boundary Protection), SI-4 (System Monitoring)
- CIS Controls v8 — Safeguard 3.13 (Deploy a Data Loss Prevention Solution), 3.1–3.14 (Data Protection)

**Verwandte Annex-A-Massnahmen**:

| Massnahme | Bezug zur Prävention von Datenlecks |
|-----------|-------------------------------------|
| A.5.10 Akzeptable Nutzung von Informationen und anderen Werten | Definiert akzeptable Datenverarbeitungs- und Übertragungspraktiken, die durch DLP durchgesetzt werden |
| A.5.12 Klassifizierung von Informationen | Datenklassifizierung bestimmt DLP-Regelschwergrad und Durchsetzungsmodus |
| A.5.13 Beschriftung von Informationen | Dokumentenbeschriftungen ermöglichen DLP-Inhaltserkennung und Richtlinienabgleich |
| A.5.14 Informationsübertragung | Übertragungsrichtlinien durch DLP-Kanalüberwachung durchgesetzt |
| A.5.15–16–18 Identitäts- und Zugangsverwaltung | Benutzeridentitätskontext bei DLP-Regelauswertung und Ausnahmenmanagement genutzt |
| A.5.24–28 Vorfallmanagement-Lebenszyklus | DLP-Alarme fliessen in Vorfallmanagement-Workflow und Meldepflichtprozess ein |
| A.5.34 Datenschutz und Schutz personenbezogener Daten | DLP verhindert nicht autorisierte PII-Offenlegung; Datenschutzrecht begrenzt Überwachungsumfang |
| A.8.10 Informationslöschung | DLP ergänzt Löschkontrollen durch Verhinderung der Speicherung auf Wechseldatenträgern |
| A.8.11 Datenmaskierung | Maskierung vor Weitergabe reduziert DLP-Alarmvolumen und Restrisiko |
| A.8.15 Protokollierung | DLP-Ereignisse für Untersuchung, Korrelation und Compliance-Nachweis protokolliert |
| A.8.16 Überwachungsaktivitäten | DLP generiert Sicherheitsereignisse für SIEM-Integration und Verhaltensanalyse |
| A.8.20–22 Netzwerksicherheit | Netzwerksegmentierung definiert DLP-Sensor-Platzierung und Inspektionspunkte |
| A.8.23 Web-Filterung | Web-Filterung und DLP kontrollieren gemeinsam webbasierte Datenexfiltrationskanäle |
| A.8.24 Verwendung kryptografischer Verfahren | Verschlüsselte Kanäle können TLS-Inspektion für DLP-Inhaltsanalyse erfordern |

**Verwandte interne Richtlinien**:

- Richtlinie zur Informationsklassifizierung und -handhabung
- Richtlinie zur akzeptablen Nutzung
- Richtlinie zum Vorfallmanagement
- Protokollierungsrichtlinie
- Richtlinie zu Überwachungsaktivitäten (A.8.16)
- Netzwerksicherheitsrichtlinie
- Richtlinie zum Datenschutz und Schutz personenbezogener Daten
- Web-Filterungsrichtlinie

---

# Richtlinie zur Prävention von Datenlecks

## Zweck

Zweck dieser Richtlinie ist es, Anforderungen für DLP-Kontrollen (Data Leakage Prevention / Prävention von Datenlecks) zu etablieren, die unautorisierte Offenlegung, Übertragung oder Exfiltration sensibler Informationen aus organisatorischen Systemen, Netzwerken und Endpunkten erkennen, verhindern und darauf reagieren. DLP-Kontrollen adressieren sowohl böswillige Exfiltration (Insider-Bedrohungen, kompromittierte Konten, Advanced Persistent Threats) als auch versehentliche Offenlegung (Benutzerfehler, Fehlkonfiguration, fehlgeleitete Kommunikation).

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 8 durch die Implementierung technischer und organisatorischer Massnahmen, die dem Risiko angemessen sind, um von der Organisation verarbeitete Personendaten zu schützen. DLP-Überwachung wird in Übereinstimmung mit dem schweizerischen Arbeitsrecht implementiert, insbesondere Art. 26 ArGV 3 (Verbot von Überwachungssystemen zur Verhaltenskontrolle) und Art. 328b OR (verhältnismässige Verarbeitung von Mitarbeiterdaten). Soweit die Organisation Daten von Personen im EU/EWR-Raum verarbeitet, gelten zudem DSGVO Art. 32 (Sicherheit der Verarbeitung) und Art. 88 (Verarbeitung im Beschäftigungskontext).

## Serviceverpflichtungen und Kundendatenschutz

DLP-Kontrollen unterstützen die Verpflichtungen der Organisation gegenüber Kunden bezüglich des Schutzes von Kundendaten vor unautorisierten Offenlegungen. Kundenvereinbarungen umfassen typischerweise Verpflichtungen wie:

- „Der Dienstleister implementiert technische und organisatorische Massnahmen, um eine unautorisierte Offenlegung von Kundendaten zu verhindern."
- „Der Dienstleister benachrichtigt den Kunden innerhalb von [X Stunden] über jeden nicht autorisierten Zugang zu oder jede Offenlegung von Kundendaten."
- „Der Dienstleister unterhält Überwachungssysteme zur Erkennung und Verhinderung von Datenexfiltration."

### Anforderungen an den Kundendatenschutz

Von der Organisation verarbeitete Kundendaten sollen einen DLP-Schutz erhalten, der den vertraglichen Verpflichtungen entspricht:

| Kundendatentyp | DLP-Klassifizierung | Schutzstufe | Meldepflicht (bei Leak) |
|----------------|---------------------|-------------|-------------------------|
| **Kunden-PII** | Mindestens Vertraulich | E-Mail + Web + Endpunkt + Cloud-Überwachung; Blockierung an externe Empfänger | Kundenbenachrichtigung innerhalb [X Stunden] gemäss Vertrag; regulatorische Meldung gemäss nDSG Art. 24 |
| **Kundliche Geschäftsdaten** (Nicht-PII) | Vertraulich oder INTERN | E-Mail + Web-Überwachung mindestens; Blockierung oder Alarm gemäss Vertragsbedingungen | Kundenbenachrichtigung innerhalb [X Stunden] gemäss Vertrag |
| **Kundliche Zugangsdaten/API-Schlüssel** | Eingeschränkt | Alle Kanäle; sofortige Blockierung + Vorfallreaktion | Kundenbenachrichtigung sofort (innerhalb 1 Stunde) |
| **Aggregierte/anonymisierte Kundendaten** | INTERN | Nur Überwachung; Erkennung auf Re-Identifizierungsrisiko fokussiert | Kundenbenachrichtigung bei Verdacht auf De-Anonymisierung |

### Kundenbenachrichtigungsverfahren

Bei DLP-Vorfällen mit Kundendaten:

1. **Erstbewertung** (innerhalb 1 Stunde): Umfang, betroffene Kunden, Datentypen, Expositionsdauer bestimmen.
2. **Eindämmung** (sofort): Übertragung blockieren, Systeme isolieren, Zugangsdaten nach Bedarf widerrufen.
3. **Kundenbenachrichtigung** (gemäss Vertragsbedingungen, typischerweise 4–24 Stunden):
   - Zusammenfassung des Vorfalls (was geschah, wann entdeckt)
   - Betroffene Datentypen und -mengen
   - Betroffene Kunden (bei Multi-Tenant)
   - Von der Organisation ergriffene Massnahmen
   - Empfohlene Kundenaktionen
   - Ansprechpartner für Fragen
4. **Regulatorische Meldung** (falls anwendbar): nDSG Art. 24 (unverzüglich), DSGVO Art. 33 (72 Stunden).
5. **Folgekommunikation**: Bericht zur Grundursachenanalyse wird betroffenen Kunden innerhalb [X Arbeitstagen] zur Verfügung gestellt.

**Kundenspezifische Anforderungen**: Wo Kunden massgeschneiderte Benachrichtigungsfristen, Vorfallschwellenwerte oder Berichtspflichten verhandelt haben, sollen diese im Kundenvertragsregister dokumentiert und in DLP-Alarmsendepfade und Vorfallreaktions-Workflows integriert werden.

## Geltungsbereich

Diese Richtlinie gilt für alle Informationswerte, die gemäss dem Datenklassifizierungsschema der Organisation als INTERN, Vertraulich oder Eingeschränkt klassifiziert sind. Dies umfasst:

- Alle Systeme, Anwendungen, Netzwerke, Endpunkte und Dienste, die organisatorische Informationen verarbeiten, speichern oder übertragen.
- Alle Datenausgabekanäle: E-Mail (SMTP, Webmail), Web (HTTP/HTTPS-Uploads), Endpunkte (USB, lokaler Speicher, Drucken), Netzwerk (Dateiübertragungsprotokolle), Cloud-Dienste (SaaS, Cloud-Speicher), mobile Geräte (firmeneigene und BYOD) sowie Anwendungs-APIs.
- Alle Mitarbeitenden der Organisation (Angestellte, Auftragnehmer, Zeitpersonal) mit Zugang zu organisatorischen Informationen.
- Alle externen Dienstleister und Cloud-Dienste, die organisatorische Daten verarbeiten.
- Alle Bereitstellungsmodelle (On-Premises, Hybrid, Cloud-nativ).

**Ausserhalb des Geltungsbereichs**: Öffentliche Informationen ohne DLP-Schutzbedarf. Physische Sicherheit von Papierdokumenten (unter A.7.x Physische Sicherheit geregelt). Backup- und Archivierungsprozesse (unter A.8.13 Informations-Backup geregelt). Datenaufbewahrung und -löschung (unter A.8.10 Informationslöschung geregelt). Datenmaskierung und -anonymisierung (unter A.8.11 Datenmaskierung geregelt). Informationssicherheitskontrollen ohne Bezug zu Datenexfiltration (Zugangskontrolle, Authentifizierung und Patch-Management werden durch ihre jeweiligen Massnahmen adressiert).

## Grundsatz

Massnahmen zur Prävention von Datenlecks sollten auf Systeme, Netzwerke und alle anderen Geräte angewendet werden, die sensible Informationen verarbeiten, speichern oder übertragen (ISO 27001:2022 Massnahme A.8.12).

Die Organisation soll DLP-Kontrollen implementieren, die dem Schutzbedarf der zu schützenden Informationen und dem Risiko unautorisierten Offenlegung proportional sind. DLP-Kontrollen sollen klassifizierungsbasiert sein — Schutzanforderungen eskalieren mit der Datensensitivität. Die Organisation soll Sicherheitsüberwachung mit Mitarbeiterprivatsphärenrechten in Einklang bringen und sicherstellen, dass DLP-Überwachung transparent, verhältnismässig und auf Datenschutz statt auf Mitarbeiterverhaltensüberwachung ausgerichtet ist.

DLP-Kontrollen dürfen nicht für Mitarbeiterleitungsbewertung, Zeiterfassung oder andere Zwecke als Informationssicherheit und Datenschutz verwendet werden.

---

## Datenklassifizierungsintegration

DLP-Kontrollen sollen auf Basis des Datenklassifizierungsschemas der Organisation angewendet werden. Die Klassifizierung bestimmt den Durchsetzungsmodus, die Kanalabdeckung und die Reaktionspriorität für jede Datenkategorie.

**Klassifizierungsbasierter DLP-Schutz**:

| Klassifizierungsstufe | DLP-Anforderung | Durchsetzungsmodus |
|----------------------|-----------------|-------------------|
| **Eingeschränkt** | Vollständige DLP-Überwachung und Blockierung über alle Ausgabekanäle | Blockieren und alarmieren |
| **Vertraulich** | DLP-Überwachung und Blockierung auf Hochrisikokanälen (E-Mail, Web, Endpunkt, Cloud) | Blockieren oder Benutzer zur Begründung auffordern |
| **INTERN** | DLP-Überwachung auf primären Ausgabekanälen (E-Mail, Web) | Überwachen und alarmieren (Erkennung ohne automatische Blockierung) |
| **Öffentlich** | Keine DLP-Kontrollen erforderlich | Nicht anwendbar |

**Sensible Datenkategorien mit DLP-Schutzpflicht**:

| Datenkategorie | Beispiele | Regulatorischer Treiber |
|---------------|-----------|-------------------------|
| **Personenbezogene Daten (PII)** | Namen, Adressen, nationale IDs, AHV-Nummern, Telefonnummern | Schweizerisches nDSG, DSGVO (wo anwendbar) |
| **Mitarbeiterdaten** | HR-Akten, Lohnbuchhaltung, Leistungsbeurteilungen, Gesundheitsinformationen | Schweizerisches nDSG Art. 328b OR |
| **Authentifizierungsdaten** | Passwörter, API-Schlüssel, Tokens, Zertifikate, SSH-Schlüssel | ISO 27001 A.5.17 |
| **Geistiges Eigentum** | Quellcode, Designs, Patente, Geschäftsgeheimnisse, strategische Pläne | Geschäftsrisiko |
| **Kundendaten** | Kundenlisten, Verträge, Preisgestaltung, Kommunikation | Vertragliche Verpflichtungen |
| **Finanzdaten** | Bankkontonummern, Zahlungsdaten, Finanzabschlüsse | Geschäftsrisiko, vertraglich |

**Datenidentifizierungsmethoden**:

Die Organisation soll mehrere Identifizierungsmethoden implementieren, um sensible Informationen im Transit zu erkennen:

- **Inhaltsinspektion**: Mustererkennung, reguläre Ausdrücke und Schlüsselworterkennung für strukturierte Daten (z. B. Kreditkartennummern, nationale IDs, AHV-Nummern).
- **Dokumentenbeschriftung**: In Dateien eingebettete Klassifizierungsmetadaten (Kopfzeilen, Fusszeilen, Eigenschaften), die es DLP ermöglichen, sensible Dokumente unabhängig vom Inhalt zu identifizieren.
- **Kontextanalyse**: Bewertung von Quellsystem, Benutzerrolle, Ziel, Übertragungsvolumen und Tageszeit zur Risikobewertung.
- **Fingerabdruck** (empfohlen): Hash-basiertes Tracking für hochwertige Dokumente wie Quellcode, Konstruktionsspezifikationen und strategische Pläne.

Die Organisation soll ein Inventar sensibler Daten mit DLP-Schutzbedarf führen, das vierteljährlich gegen das Inventarverzeichnis (A.5.9) abgeglichen wird. Spezifische Erkennungsmuster, Regex-Regeln und Klassifizierungsbeschriftungen sollen vom Security Team dokumentiert und gepflegt werden.

---

## Kanalschutz

Die Organisation soll DLP-Kontrollen über alle Datenausgabekanäle implementieren, um unautorisierte Informationsoffenlegung zu verhindern. Die Kanalabdeckung soll durch technische Tests mindestens vierteljährlich verifiziert werden.

### E-Mail-Schutz

Alle ausgehenden E-Mails (SMTP und Webmail) sollen DLP-Inhaltsinspektion unterliegen:

- Nachrichtentexte und Anhänge auf sensible Inhalte scannen, die DLP-Erkennungsregeln entsprechen.
- Empfänger-Domains validieren: interne, vertrauenswürdige externe und nicht vertrauenswürdige externe Empfänger unterscheiden.
- Nachrichten mit Eingeschränkten Daten an externe Empfänger blockieren oder in Quarantäne stellen.
- Bei Vertraulichen Daten an externe Empfänger alarmieren (Blockieren oder Benutzer zur Eingabe einer Begründung auffordern, abhängig von Klassifizierung und Ziel).
- Verschlüsselung (S/MIME, TLS) für genehmigte sensible E-Mails unterstützen, wo ein Geschäftsbedarf besteht.
- Browserbasierte Webmail-Dienste (z. B. Gmail, Outlook.com, Yahoo Mail) überwachen, um Umgehung von SMTP-basierten DLP-Kontrollen zu verhindern.

### Web- und Cloud-Kanalschutz

Webbasierte Datenausgabekanäle sollen überwacht und kontrolliert werden:

- **Web-Uploads**: Datei-Uploads zu Cloud-Speicherdiensten (z. B. Dropbox, Google Drive, persönliche OneDrive-Konten) überwachen und kontrollieren. Genehmigter Unternehmens-Cloud-Speicher [Cloud-Speicherplattform] soll von persönlichen oder nicht genehmigten Diensten unterschieden werden.
- **Cloud-Anwendungen**: [CASB] (Cloud Access Security Broker) oder gleichwertiges für SaaS-Anwendungsüberwachung (z. B. Microsoft 365, Google Workspace) integrieren. Datenweitergabe, externe Zusammenarbeit und Cloud-zu-Cloud-Übertragungen überwachen.
- **Web-Formulare**: Einfüge- und Formularausfüll-Aktivitäten auf externen Web-Formularen nach risikoangemessenem Umfang überwachen.
- **TLS-Inspektion**: Soweit rechtlich zulässig und technisch machbar, verschlüsselten Web-Traffic am Internet-Gateway inspizieren, um sensible Inhalte in HTTPS-Uploads zu erkennen. Die TLS-Inspektion soll Datenschutzanforderungen entsprechen und in der Datenschutzhinweiserklärung der Organisation dokumentiert sein.

### Endpunktschutz

Endpunkt-DLP-Kontrollen sollen auf allen verwalteten Geräten eingesetzt werden:

- **Wechseldatenträger**: Dateiübertragungen auf USB-Laufwerke, externe Festplatten, SD-Karten und andere Wechselspeicher überwachen und kontrollieren. Nicht autorisierten Wechseldatenträgereinsatz für Eingeschränkte und Vertrauliche Daten blockieren. Genehmigte Wechseldatenträger (z. B. verschlüsselte Unternehmens-USB-Geräte) sollen dokumentiert werden.
- **Lokaler Speicher**: Dateischreibvorgänge auf lokale Festplatten, Netzlaufwerke und Offline-Speicher für sensible Daten überwachen.
- **Drucken**: Druckaufträge für Eingeschränkte Daten überwachen. Drucken als PDF und virtuelle Druckeraktivitäten sollen in den Überwachungsumfang einbezogen sein.
- **Screenshots und Zwischenablage** (risikobasiert): Wo die Risikobewertung dies rechtfertigt, Bildschirmaufnahme-Tools und Zwischenablageoperationen für Eingeschränkte Daten überwachen. Diese Kontrolle soll nur auf spezifische Hochrisikorollen oder Datensätze angewendet werden, nicht organisationsweit.
- **Offline-Durchsetzung**: Endpunkt-DLP-Agenten sollen Richtlinien durchsetzen, wenn das Gerät vom Unternehmensnetzwerk getrennt ist.
- **Shadow-IT-Erkennung**: Nicht genehmigte Cloud-Speicher-, Messaging- und Dateifreigabe-Anwendungen auf verwalteten Endpunkten erkennen.

### Netzwerkschutz

Netzwerk-DLP-Kontrollen sollen Datenflüsse an Ausgangspunkten überwachen:

- Netzwerkverkehr an Internet-Gateways und Cloud-Verbindungspunkten überwachen.
- Dateiübertragungsprotokolle (FTP, SFTP, SCP, rsync) auf sensible Datenübertragungen überwachen.
- Datenexfiltration über verdeckte Kanäle (DNS-Tunneling, ICMP-Exfiltration, Steganografie) erkennen, wo die Bedrohungsbewertung dieses Risiko identifiziert.
- DLP-Alarme mit Firewall, Proxy und [SIEM] für Korrelation und Untersuchung integrieren.

### Schutz für mobile Geräte

Unternehmens-Daten auf mobilen Geräten sollen geschützt werden:

- DLP mit [MDM] (Mobile Device Management) integrieren, um Datenschutzrichtlinien auf mobilen Unternehmensgeräten durchzusetzen.
- Unternehmens-Anwendungen und -daten auf BYOD-Geräten containerisieren, um Datenlecks in persönliche Anwendungen zu verhindern.
- E-Mail- und Dokumentfreigabe von mobilen Geräten überwachen.
- Bedingte Zugriffsrichtlinien anwenden, die den Zugang zu sensiblen Daten auf konforme Geräte beschränken.

### Abdeckungsverifikation

Die Organisation soll die DLP-Kanalabdeckung durch technische Tests mindestens vierteljährlich verifizieren. Abdeckungslücken sollen dokumentiert werden mit:

- Lückenbeschreibung und betroffene Systeme oder Benutzer.
- Risikobewertung der Lücke.
- ISB-Genehmigung zur Risikoakzeptanz (falls anwendbar).
- Massnahmenplan mit Zeitplan (falls nicht akzeptiert).

Akzeptable Abdeckungsausnahmen (dokumentiert und ISB-genehmigt): Gastnetzwerke ohne Zugang zu sensiblen Daten; dedizierte B2B-Partnerverbindungen mit alternativen Kontrollen; Air-gapped-Netzwerke ohne Internetverbindung; spezifische Benutzergruppen mit dokumentierten und genehmigten Ausnahmen (z. B. Rechtsberater bei privilegierten Kommunikationen).

---

## Management von DLP-Drittanbietern

Soweit die Organisation cloudbasierte DLP-Lösungen nutzt (CASB, E-Mail-Security-Gateway-as-a-Service, Cloud-DLP-Plattformen):

### Lieferantenauswahlkriterien

DLP-Dienstleister sollen nach folgenden Kriterien bewertet werden:

| Kriterium | Anforderung | Validierungsmethode |
|-----------|-------------|---------------------|
| **Sicherheitszertifizierungen** | SOC 2 Typ II (aktuell, innerhalb 12 Monate); ISO 27001 | Berichte jährlich anfordern und prüfen |
| **Datenresidenz** | Datenverarbeitung und -speicherung in der Schweiz oder EU/EWR (oder Angemessenheitsjurisdiktion gemäss nDSG) | Im Vertrag bestätigen; im SOC-2-Bericht verifizieren |
| **Datenschutz-Compliance** | DSGVO-konformer Auftragsverarbeitungsvertrag; nDSG-Compliance-Verpflichtung | Rechtliche Prüfung des AVV |
| **Erkennungsgenauigkeit** | <10% Falsch-Positiv-Rate bei Test; >95% Erkennungsrate für bekannte Testdatensätze | 30-tägiger Proof-of-Concept mit Produktionsverkehrsstichprobe |
| **Performance** | <500ms E-Mail-Latenz; <100ms Web-Proxy-Latenz (Inline-Modus) | Lasttests während der Testphase |
| **Integrationsfähigkeiten** | API-Integration mit [SIEM], [ITSM], Identitätsanbieter | Technische Validierung während POC |
| **Vorfallreaktion** | Anbieter bietet 24x7-Support; <1 Stunde Reaktionszeit für kritische Alarme | SLA-Bedingungen; Referenzprüfungen |

### Anforderungen an den Auftragsverarbeitungsvertrag

Verträge mit Cloud-DLP-Anbietern sollen umfassen:

- **Pflichten des Auftragsverarbeiters** (nDSG Art. 9; DSGVO Art. 28 wo anwendbar)
- **Offenlegung und Genehmigung von Unterauftragsverarbeitern** (Liste der Unterauftragsverarbeiter; Benachrichtigung bei Änderungen)
- **Datenaufbewahrung und -löschung** (automatische Löschung nach Aufbewahrungsfrist; Löschbestätigung auf Anfrage)
- **Sicherheitsvorfallbenachrichtigung** (Anbieter benachrichtigt Organisation innerhalb von 24 Stunden bei jedem Vorfall, der Kundendaten betrifft)
- **Prüfungsrechte** (Organisation oder Prüfer kann Anbieterkontrollen prüfen; SOC-2-Bericht genügt, wenn aktuell)
- **Datenportabilität** (DLP-Protokolle und -Richtlinien bei Vertragsende in Standardformat exportieren)
- **Gerichtsbarkeit und anwendbares Recht** (Schweizer Recht bevorzugt; EU-Recht akzeptabel; Streitigkeiten in der Schweiz)

### Laufende Anbieter-Performance-Überwachung

| Metrik | Ziel | Überprüfungshäufigkeit | Verantwortlich |
|--------|------|------------------------|----------------|
| **Dienstverfügbarkeit** | Gemäss Anbieter-SLA (typischerweise 99,5–99,9 %) | Monatlich | IT-Betrieb |
| **Falsch-Positiv-Rate** | <10 % | Monatlich | Security Team |
| **Erkennungsgenauigkeit** | >95 % für Testszenarien | Vierteljährlich | Security Team |
| **Performance (Latenz)** | Gemäss obigen Zielen | Wöchentlich | IT-Betrieb |
| **Support-Reaktionsfähigkeit** | Gemäss SLA (Kritisch: <1 Std.; Hoch: <4 Std.; Mittel: <24 Std.) | Pro Ticket | Security-Team-Lead |
| **Sicherheitsvorfälle beim Anbieter** | 0 mit Auswirkung auf Kundendaten | Pro Ereignis | ISB |

### Jährliche Anbieterüberprüfung

Cloud-DLP-Anbieter sollen eine jährliche Überprüfung erhalten, die Folgendes abdeckt:

- **SOC-2-Typ-II-Berichtsprüfung**: Aktuellen Bericht mit dem vorherigen vergleichen; neue Ausnahmen oder Vorbehalte identifizieren; verifizieren, dass das Kontrollumfeld akzeptabel bleibt.
- **Performance gegen SLAs**: Verfügbarkeit, Latenz, Support-Reaktionszeiten.
- **Falsch-Positiv-Trends**: Verbessernd, stabil oder verschlechternd?
- **Sicherheitsvorfälle**: Sicherheitsverletzungen oder Beinahe-Vorfälle auf Anbieterseite in den letzten 12 Monaten?
- **Roadmap-Ausrichtung**: Technologierichtung des Anbieters mit den Bedürfnissen der Organisation abgestimmt?
- **Kosten-Nutzen**: Gelieferter Mehrwert vs. Abonnementkosten; Vergleich mit Alternativen.
- **Empfehlung**: Verlängern, neu verhandeln oder ersetzen.

**Überprüfungsdokumentation**: 3 Jahre aufbewahrt; Verlängerungsentscheidungen mit Begründung dokumentiert.

### Eskalation bei Anbieter-Vorfällen

Falls ein Cloud-DLP-Anbieter einen Sicherheitsvorfall erlebt, der die Organisation betrifft:

1. **Sofortige Benachrichtigung**: Anbieter benachrichtigt Organisation innerhalb von 24 Stunden (gemäss Vertrag).
2. **Folgenabschätzung**: Security Team bewertet Auswirkungen auf Organisation und Kunden.
3. **Kundenbenachrichtigung**: Falls Kundendaten betroffen, Kunden gemäss Serviceverpflichtungen benachrichtigen.
4. **Regulatorische Meldung**: Falls Personendaten betroffen und Meldekriterien erfüllt (nDSG Art. 24), EDÖB benachrichtigen.
5. **Anbieter-Korrektivmassnahmen-Review**: Anbieter liefert Grundursachenanalyse und Massnahmenplan innerhalb von 10 Arbeitstagen.
6. **Vertragsprüfung**: Beurteilen, ob Vorfall einen wesentlichen Vertragsbruch darstellt; Anbieterwechsel in Betracht ziehen.

**Dokumentation von Anbieter-Vorfällen**: Mindestens 5 Jahre aufbewahrt; in der jährlichen Anbieterüberprüfung berücksichtigt.

---

## Überwachung und Erkennung

Die Organisation soll eine kontinuierliche Überwachung implementieren, um Datenleckversuche und Richtlinienverletzungen zu erkennen.

**Erkennungsmodi**:

| Modus | Beschreibung | Anwendungsfall |
|-------|--------------|----------------|
| **Nur überwachen** | Protokollieren und alarmieren ohne Blockierung | Initiale Einsatzphase, Niedrigrisikokanäle, Abstimmungszeitraum |
| **Benutzer auffordern** | Benutzerbegründung vor Übertragung einfordern | Vertrauliche Datenübertragungen an externe Empfänger |
| **Blockieren** | Datenübertragung verhindern und Security Team alarmieren | Eingeschränkte Daten an nicht vertrauenswürdige Ziele, Datenlecks von Zugangsdaten |
| **Quarantäne** | Übertragung für Security-Team-Prüfung zurückhalten | Verdächtige böswillige Exfiltration, nicht eindeutige Fälle |

**Alarmpriorität und Reaktionszeiten**:

| Priorität | Auslöserbeispiele | Reaktionszeit |
|-----------|-------------------|---------------|
| **Kritisch** | Eingeschränkte Daten extern exfiltriert; Datenleck von Zugangsdaten; Hochvolumen-Massenübertragung | Sofort (< 15 Minuten) |
| **Hoch** | Vertrauliche Daten an nicht vertrauenswürdige Domain; Privilegierte Benutzerrichtlinienverletzung; wiederholte Verstösse | < 1 Stunde |
| **Mittel** | Vertrauliche Daten an genehmigten externen Partner; Massenübertragung im normalen Geschäftskontext | < 4 Stunden |
| **Niedrig** | INTERNE Daten extern; informatorische Alarme; Falsch-Positiv-Kandidaten | < 24 Stunden |

**DLP-Ereignisprotokollierung**:

Alle DLP-Ereignisse sollen mit folgenden Informationen protokolliert werden:

- Zeitstempel (UTC, ISO-8601-Format).
- Benutzeridentität (Benutzername, Mitarbeiter-ID).
- Quellsystem (Hostname, IP-Adresse, Gerätekennung).
- Ziel (Empfänger-E-Mail, URL, externer Dienst, Wechseldatenträger-Kennung).
- Ausgelöste Datenklassifizierung (Eingeschränkt, Vertraulich, INTERN).
- Erkennungsmethode (Inhaltsinspektion, Beschriftung, Kontextanalyse).
- Ergriffene Massnahme (blockiert, erlaubt, quarantänisiert, benutzerbegründet).
- Datenauszug (erste 100 Zeichen oder bereinigter Auszug — beschränkt auf das für die Untersuchung notwendige Minimum, in Übereinstimmung mit Datenschutzanforderungen).

**Protokollaufbewahrung**:

- DLP-Sicherheitsereignisse (blockierte Übertragungen, Richtlinienverletzungen, kritische Alarme): Mindestens 12 Monate.
- DLP-Betriebsprotokolle (erlaubte Übertragungen, informatorische Ereignisse): Mindestens 90 Tage.
- Verlängerte Aufbewahrung, wenn regulatorische Anforderungen längere Fristen vorschreiben.
- Protokolle mit Integritäts- und Vertraulichkeitskontrollen gemäss A.8.15 geschützt.

**Verhaltensanalyse** (empfohlen): Soweit die Organisation UEBA (User and Entity Behaviour Analytics) einsetzt, sollen DLP-Daten mit der Baseline-Benutzeraktivität korreliert werden, um anomale Übertragungsmuster zu erkennen (z. B. ungewöhnliches Volumen, ungewöhnliches Ziel, ungewöhnliche Uhrzeit). Verhaltensanalysen sollen die in dieser Richtlinie definierten rechtlichen Anforderungen zur Mitarbeiterüberwachung einhalten.

**Bedrohungsintelligenz-Integration** (empfohlen): DLP-Systeme sollten mit Bedrohungsintelligenz-Feeds integriert werden, um bekannte Exfiltrationsindikatoren zu identifizieren (Command-and-Control-Domains, Malware-Signaturen, in MITRE ATT&CK dokumentierte APT-Techniken).

---

## DLP-Vorfallreaktion

DLP-Sicherheitsvorfälle sollen dem Vorfallmanagementprozess der Organisation (A.5.24-28) mit folgenden DLP-spezifischen Anforderungen folgen.

**DLP-Vorfallklassifizierung**:

| Schweregrad | Indikatoren | Erstmassnahmen |
|-------------|-------------|----------------|
| **Kritisch** | Eingeschränkte Daten bestätigt exfiltriert; Zugangsdaten extern geleakt; Insider-Bedrohungsindikatoren; APT-Exfiltrationsmuster | Benutzer blockieren; Endpunkt isolieren; ISB und DSB benachrichtigen; Vorfallreaktion einleiten |
| **Hoch** | Vertrauliche Daten an nicht vertrauenswürdigen Empfänger; Massenübertragung sensibler Daten; wiederholte Richtlinienverstösse desselben Benutzers | Übertragung blockieren; Benutzeraktivität untersuchen; an Security-Team-Lead eskalieren |
| **Mittel** | Vertrauliche Daten an genehmigten externen Partner über nicht genehmigten Kanal; Benutzerfehler mit begrenzter Exposition | Übertragung einschränken; Benutzer befragen; Umfang bewerten; beheben |
| **Niedrig** | Falsch-Positiv; Richtlinienabstimmung erforderlich; Benutzerklärung benötigt | Protokollieren; DLP-Regel abstimmen; ggf. mit Benutzer kommunizieren |

**Reaktions-Workflow**:

1. **Erkennen**: DLP-System generiert Alarm basierend auf Richtlinienverletzung.
2. **Triage**: Security Team klassifiziert Vorfallschweregrad, bestimmt Umfang und leitet Eindämmung ein.
3. **Eindämmung**: Benutzerkonto blockieren, Endpunkt isolieren, Zugangsdaten widerrufen oder Übertragung quarantänisieren.
4. **Untersuchung**: Grundursachenanalyse (böswillig vs. versehentlich), Umfangsbestimmung (Datenvolumen, Sensitivität, Empfänger, Expositionsdauer), Beweissicherung.
5. **Beseitigung**: Zugangsdaten rotieren (bei Datenleck von Zugangsdaten), Malware-Bereinigung (bei Exfiltration über Malware), Zugang widerrufen.
6. **Wiederherstellung**: Normalbetrieb wiederherstellen, DLP-Richtlinie anpassen, Benutzer mit angemessenen Kontrollen reaktivieren.
7. **Nach-Vorfallüberprüfung**: Lessons Learned (innerhalb 30 Tagen), DLP-Richtlinienabstimmung, Empfehlungen zur Kontrollverbesserung.

**Regulatorische Meldepflicht bei Datenverletzungen**:

Wo DLP-Vorfälle Verletzungen personenbezogener Daten darstellen, soll die Organisation Meldepflichtanforderungen einhalten:

| Regulation | Anforderung | Frist |
|-----------|-------------|-------|
| **Schweizerisches nDSG** | Art. 24 — EDÖB benachrichtigen, wenn Verletzung hohes Risiko für betroffene Personen birgt | Unverzüglich |
| **EU-DSGVO** (wo anwendbar) | Art. 33 — Aufsichtsbehörde benachrichtigen | 72 Stunden |
| **DSGVO-betroffene Personen** | Art. 34 — Personen benachrichtigen bei hohem Risiko | Unverzüglich |

Der Datenschutzbeauftragte (DSB) oder designierter Datenschutzverantwortlicher soll bei allen DLP-Vorfällen mit personenbezogenen Daten konsultiert werden, um Meldepflichten zu bestimmen.

**DLP-zu-Vorfallmanagement-Integration**: Kritische und hochgradige DLP-Ereignisse sollen automatisch Incident-Tickets in [ITSM-Plattform] (z. B. ServiceNow, Jira Service Management oder gleichwertig) erstellen. Nicht innerhalb der Reaktions-SLA bestätigte Tickets sollen gemäss Vorfallmanagement-Verfahren automatisch eskaliert werden.

---

## Rechtliche Anforderungen zur Mitarbeiterüberwachung

DLP-Überwachung stellt eine Form der Mitarbeiterüberwachung nach schweizerischem Recht dar. Die Organisation soll folgende rechtliche Anforderungen einhalten, bevor DLP-Kontrollen eingesetzt und betrieben werden.

### Schweizerischer Rechtsrahmen

**Art. 26 ArGV 3 (Verordnung 3 zum Arbeitsgesetz)**: Überwachungs- und Kontrollsysteme dürfen nicht eingesetzt werden, wenn ihr einziger oder hauptsächlicher Zweck die Verhaltensüberwachung von Mitarbeitenden ist. DLP-Systeme sind zulässig, weil ihr primärer Zweck der Schutz organisatorischer Daten vor unautorisierten Offenlegungen ist — nicht die Überwachung des individuellen Mitarbeiterverhaltens. Die DLP-Implementierung muss jedoch nachweisbar einem Datenschutzziel dienen, und jede beiläufige Überwachung des Mitarbeiterverhaltens muss verhältnismässig sein.

**Art. 328b OR (Schweizerisches Obligationenrecht)**: Der Arbeitgeber darf Daten über Arbeitnehmer nur bearbeiten, soweit sie deren Eignung für das Arbeitsverhältnis betreffen oder zur Erfüllung des Arbeitsvertrages erforderlich sind. DLP-Überwachungsdaten sollen ausschliesslich für Informationssicherheitszwecke verarbeitet werden. DLP-Daten dürfen NICHT verwendet werden für:

- Mitarbeiterleistungsbewertung oder -einstufung.
- Zeiterfassung und Anwesenheitsüberwachung.
- Überwachung des persönlichen Surfens oder der persönlichen Kommunikation.
- Jeden Zweck, der nicht mit Datensicherheit und Prävention von Datenlecks zusammenhängt.

**Schweizerische nDSG-Grundsätze**:

- **Rechtmässigkeit**: DLP-Überwachung muss eine rechtliche Grundlage haben (Schutz organisatorischer Daten ist ein berechtigtes Interesse).
- **Verhältnismässigkeit**: Der Überwachungsumfang soll auf das für den Datenschutz Notwendige beschränkt sein. Die Organisation soll nicht umfassender überwachen als erforderlich.
- **Zweckbindung**: Durch DLP erhobene Daten sollen ausschliesslich für Sicherheitszwecke verwendet und nicht für andere Ziele zweckentfremdet werden.
- **Transparenz**: Mitarbeitende sollen über DLP-Überwachung informiert werden, bevor diese aktiviert wird.

### EU-DSGVO-Anforderungen (Wo anwendbar)

Soweit die Organisation Daten von Personen im EU/EWR-Raum verarbeitet:

- **Art. 6(1)(f) Berechtigtes Interesse**: DLP-Überwachung stützt sich auf das berechtigte Interesse des Schutzes organisatorischer Daten, abgewogen gegen Mitarbeiterprivatsphärenrechte.
- **Art. 32 Sicherheit der Verarbeitung**: DLP ist eine angemessene technische Massnahme zum Schutz personenbezogener Daten.
- **Art. 88 Verarbeitung im Beschäftigungskontext**: DLP-Überwachung muss dem nationalen Arbeitsrecht in jeder EU-Jurisdiktion entsprechen, in der die Organisation tätig ist.

### Verhältnismässigkeitsbewertung

Die Organisation soll eine Verhältnismässigkeitsbewertung vor dem Einsatz von DLP-Kontrollen durchführen. Die Bewertung soll verifizieren, dass:

**Verhältnismässig (zulässig)**:
- Ausgabekanäle auf sensible Datenmuster überwachen (E-Mail-Anhänge, Web-Uploads, USB-Übertragungen).
- DLP-Alarme mit begrenzter Aufbewahrung protokollieren (90 Tage routinemässig, 12 Monate Sicherheitsereignisse).
- Zugang zu DLP-Protokollen auf Security Team, ISB und DSB nach Kenntnis-nach-Bedarf-Prinzip beschränken.
- Initial im Nur-Überwachen-Modus einsetzen, bevor Blockierung aktiviert wird.
- Datenauszüge in Protokollen auf das für die Untersuchung notwendige Minimum begrenzen.

**Unverhältnismässig (nicht zulässig)**:
- Alle E-Mail-Inhalte unabhängig von der Sensitivität unbegrenzt aufzeichnen.
- Alle Web-Surfaktivitäten ohne risikobasierte Umfangsbegrenzung überwachen.
- Tastatureingabe-Logging oder kontinuierliche Bildschirmaufzeichnung ohne spezifische dokumentierte Begründung.
- HR oder Vorgesetzte DLP-Alarme für Leistungsmanagement durchsuchen lassen.
- Persönliche Geräte auf Nicht-Arbeitsaktivitäten überwachen.
- DLP-Daten für Mitarbeiterbewertung oder Disziplinarmassnahmen ohne Bezug zur Datensicherheit verwenden.

### Transparenzanforderungen

Die Organisation soll alle Mitarbeitenden über DLP-Überwachung informieren durch:

1. **Arbeitsverträge oder Ergänzungen**: Klare Angabe, dass DLP-Überwachung besteht, ihr Umfang, Zweck und Datenaufbewahrungsfristen.
2. **Datenschutzhinweis / Mitarbeiterhandbuch**: Detaillierte Erklärung, was überwacht wird, was nicht überwacht wird, wie Daten verwendet werden und wer Zugang hat.
3. **Richtlinie zur akzeptablen Nutzung**: Ausdrückliches Verbot von Datenexfiltration, Beispiele verbotener Aktivitäten, Konsequenzen von Verstössen und der Ausnahmeprozess.
4. **Sicherheitsbewusstseinsschulung**: Jährliches Schulungsmodul zu DLP-Zweck, Benutzerverantwortlichkeiten, Ausnahmeanträgen und Berichterstattung.
5. **Arbeitnehmervertretung** (wo anwendbar): In Jurisdiktionen, die Mitbestimmung erfordern, soll die Arbeitnehmervertretung vor dem Einsatz von DLP-Überwachung konsultiert werden.

**Kritisch**: Das Versäumnis, Transparenz zu gewährleisten, kann DLP-Überwachung rechtswidrig machen. DLP-Überwachung soll erst aktiviert werden, nachdem die Mitarbeiterbenachrichtigung abgeschlossen und dokumentiert wurde. Die Organisation soll Nachweise der Mitarbeiterbenachrichtigung aufbewahren (unterzeichnete Bestätigungen, Schulungsabschlussaufzeichnungen, Datenschutzhinweis-Verteilungsaufzeichnungen).

### Durchsetzungsrisiko

Nichteinhaltung der Anforderungen zur Mitarbeiterüberwachung setzt die Organisation folgenden Risiken aus:

- **Schweizerisches nDSG**: Bussen bis CHF 250'000 für individuelle Verstösse; Durchsetzungsmassnahmen des EDÖB.
- **EU-DSGVO**: Bussen bis EUR 20'000'000 oder 4 % des weltweiten Jahresumsatzes.
- **Arbeitsrecht**: Rechtswidrige Überwachung kann Grundlage für Mitarbeiteransprüche nach Persönlichkeitsrechten (Art. 28 ZGB) sein; rechtswidrig erlangte DLP-Beweise können in Disziplinarverfahren unzulässig sein.

---

## Sensibilisierung und akzeptable Nutzung

Alle Mitarbeitenden sollen über DLP-Kontrollen und ihre Verantwortlichkeiten informiert werden.

**Benutzerverantwortlichkeiten**:

- Sensible Daten gemäss ihrer Klassifizierung und der Richtlinie zur akzeptablen Nutzung verarbeiten.
- Genehmigte Kanäle für Datenübertragungen verwenden (Unternehmens-E-Mail, genehmigter Cloud-Speicher, verschlüsselte Übertragungstools).
- Ausnahmen über den formellen Ausnahmeprozess für legitime Geschäftsbedürfnisse anfordern, die eine Abweichung von der DLP-Richtlinie erfordern.
- Falsch-Positive und Nutzbarkeitsprobleme dem Security Team oder Help Desk melden.
- Jährliche DLP-Sensibilisierungsschulung absolvieren.

**Verbotene Aktivitäten**:

- Versuche, DLP-Kontrollen durch Proxys, Datenverschlüsselung zur Umgehung der Inspektion, Nutzung nicht genehmigter Cloud-Dienste oder andere Umgehungsmethoden zu überwinden.
- Übertragung Eingeschränkter oder Vertraulicher Daten an persönliche E-Mail-Konten, persönlichen Cloud-Speicher oder nicht genehmigte externe Dienste.
- Deaktivierung oder Manipulation von Endpunkt-DLP-Agenten.
- Weitergabe von DLP-Ausnahme-Zugangsdaten oder genehmigten Übertragungsmethoden an nicht autorisierte Personen.

Verstösse gegen die DLP-Richtlinie unterliegen disziplinarischen Massnahmen gemäss HR-Richtlinie. Absichtliche oder wiederholte Versuche, DLP-Kontrollen zu umgehen, können zur Kündigung des Arbeitsverhältnisses führen.

**Wenn DLP eine Übertragung blockiert**:

1. Datenklassifizierung überprüfen — handelt es sich tatsächlich um sensible Daten?
2. Eine genehmigte Übertragungsmethode verwenden (Unternehmens-E-Mail mit Verschlüsselung, genehmigte Cloud-Freigabe, sicherer Dateitransfer).
3. Falls die Übertragung ein legitimes Geschäftsbedürfnis ist, einen Ausnahmeantrag beim Security Team einreichen.
4. Help Desk bei dringender Hilfe oder zur Meldung eines Falsch-Positiv kontaktieren.

---

## DLP-Performance und -Abstimmung

Die Organisation soll DLP-Effektivität durch Schlüsselleistungsindikatoren verfolgen und DLP-Regeln kontinuierlich abstimmen, um Falsch-Positive zu reduzieren und gleichzeitig die Erkennungsabdeckung aufrechtzuerhalten.

**Leistungsmetriken**:

| Metrik | Ziel | Akzeptabler Bereich | Überprüfungshäufigkeit |
|--------|------|---------------------|------------------------|
| Falsch-Positiv-Rate | < 5 % der Gesamtalarme | < 10 % Maximum | Monatlich |
| Alarm-Reaktions-SLA-Einhaltung | > 95 % innerhalb der Zielzeiten | > 90 % Minimum | Wöchentlich |
| Kanalabdeckung (kritische Ausgabepfade) | 100 % | > 95 % Minimum | Vierteljährlich |
| Vorfallerkennungsrate (Eingeschränkte Daten) | 100 % der Exfiltrationsversuche | > 98 % Minimum | Pro Vorfallüberprüfung |
| Richtlinienabstimmungs-Effektivität | > 20 % FP-Reduktion pro Abstimmungszyklus | Positiver Trend erforderlich | Vierteljährlich |
| Benutzergemeldete Probleme | < 10 pro Monat | < 20 Maximum | Monatlich |

**Abstimmungsprozess**:

- **Monatlich**: Security Team überprüft Falsch-Positiv-Trends und passt Erkennungsregeln an.
- **Vierteljährlich**: Umfassende Überprüfung der DLP-Regeleffektivität, Abdeckungslücken und aufkommender Datentypen.
- **Pro Vorfall**: Nach-Vorfallüberprüfung identifiziert Verbesserungen der Erkennungsregeln und Abdeckungserweiterungen.
- **Jährlich**: Vollständige DLP-Programmüberprüfung als Teil des Management Reviews (ISO 27001 Abschnitt 9.3), einschliesslich Technologiebewertung und Anbieterevaluierung.

**Reaktion bei Unterschreitung**: Wenn Metriken für zwei aufeinanderfolgende Messzeiträume den akzeptablen Bereich unterschreiten, soll der ISB innerhalb von 30 Tagen eine Grundursachenanalyse durchführen, einen Korrektivmassnahmenplan implementieren und den Sanierungsstatus der Geschäftsleitung berichten.

---

## DLP-Systemverfügbarkeit und Performance-Auswirkung

DLP-Systeme, die Latenz einführen, legitime Geschäftsvorgänge blockieren oder in einer Weise ausfallen, die Dienste unterbricht, können sich negativ auf die Verfügbarkeitsverpflichtungen der Organisation auswirken.

### DLP-Systemverfügbarkeitsanforderungen

| Komponente | Verfügbarkeitsziel | Auswirkung bei Ausfall | Failover/Redundanz |
|------------|-------------------|------------------------|-------------------|
| **E-Mail-DLP-Gateway** | 99,5 % | E-Mail-Zustellverzögerungen oder -ausfälle | Hochverfügbarkeitspaar; Fail-Open-Option für unkritische Klassifizierungen |
| **Web-DLP-Proxy** | 99,5 % | Web-Zugang-Verschlechterung oder -Blockierung | Redundante Proxys; Fail-Open mit Protokollierung für Nicht-Eingeschränkte Daten |
| **Endpunkt-DLP-Agenten** | 99 % (pro Endpunkt) | Nur Offline-Durchsetzung; keine Netzwerksynchronisation | Agenten setzen Offline-Durchsetzung fort; Alarm bei längerem Trennung (>72 Std.) |
| **Netzwerk-DLP-Sensoren** | 99 % | Sichtbarkeitsverlust; keine Blockierungsfähigkeit auf Netzwerkebene | Passive Überwachung; unterbricht keine Verbindung |
| **Cloud-DLP (CASB)** | 99,5 % (Anbieter-SLA) | Cloud-Dienst-Zugang kann bei Inline-Modus beeinträchtigt sein; API-Modus läuft weiter | Anbieterbereitgestellte Redundanz; Inline- vs. API-Moduskonfiguration |

### Fail-Safe-Modi

DLP-Systeme sollen mit explizitem Fail-Safe-Verhalten konfiguriert werden, um Dienstunterbrechungen zu verhindern:

| Szenario | Fail-Safe-Verhalten | Begründung |
|----------|---------------------|------------|
| **E-Mail-DLP-Gateway-Ausfall** | Fail-Open für INTERNE und Vertrauliche Daten (Zustellung läuft mit Protokollierung weiter); Fail-Closed für Eingeschränkte Daten (E-Mail in Warteschlange bis Systemwiederherstellung) | Verfügbarkeit vs. Sicherheit basierend auf Datensensitivität abwägen |
| **Web-DLP-Proxy-Ausfall** | Fail-Open mit vollständiger Protokollierung; Alarme für gesamten Traffic während Fail-Open-Zeitraum generiert | Geschäftskontinuität aufrechterhalten; Aktivität während Ausfallfenster untersuchen |
| **Endpunkt-DLP-Agent-Absturz** | Offline-Richtliniendurchsetzung fortsetzen; IT-Betrieb zur Behebung alarmieren | Grundschutz aufrechterhalten; vollständige Überwachung so bald wie möglich wiederherstellen |
| **DLP-Datenbank/Management-Konsolen-Ausfall** | Agenten verwenden letzte bekannte funktionierende Richtlinie; keine neuen Regeln bis zur Wiederherstellung | Verlust der Richtliniendurchsetzung verhindern |

### Performance-Überwachung

Die DLP-Systemleistung soll überwacht werden, um Dienstbeeinträchtigungen zu verhindern:

| Metrik | Ziel | Alarmauslöser | Überprüfungshäufigkeit |
|--------|------|---------------|------------------------|
| **E-Mail-Verarbeitungslatenz** | <500 ms pro Nachricht | >2 Sekunden anhaltend für 5 Minuten | Echtzeit-Überwachung |
| **Web-Proxy-Latenz** | <100 ms hinzugefügte Latenz | >300 ms anhaltend für 5 Minuten | Echtzeit-Überwachung |
| **CPU-Auslastung Endpunkt-Agent** | <5 % Durchschnitt | >15 % anhaltend für 10 Minuten | Stündliche Überwachung |
| **Speicherauslastung Endpunkt-Agent** | <200 MB | >500 MB | Stündliche Überwachung |
| **Falsch-Positiv-Rate mit Produktivitätsauswirkung** | <5 % der Benutzer melden Blockierungen bei legitimen Aktivitäten | >10 % Benutzerbeschwerden pro Monat | Monatliche Benutzerrückmeldungsanalyse |
| **DLP-System-Betriebszeit** | Gemäss Verfügbarkeitszielen oben | <99 % in einem Kalendermonat | Monatliche SLA-Überprüfung |

### Kapazitätsplanung

- DLP-Systeme sollen so dimensioniert sein, dass sie Spitzenverkehr mit 30 % Puffer bewältigen.
- Jährliche Kapazitätsüberprüfung soll Wachstum projizieren und Skalierungsbedarf identifizieren.
- E-Mail-Volumen, Web-Traffic, Endpunktanzahl und Datenübertragungsvolumina vierteljährlich verfolgen.
- Kapazitätsalarme bei 70 % Auslastung; Upgrade vor 85 % Auslastung geplant.

### Auswirkungen von Vorfällen auf Dienste

DLP-Vorfälle können die Dienstverfügbarkeit durch Eindämmungsmassnahmen beeinträchtigen:

| Eindämmungsmassnahme | Dienstauswirkung | Minderung |
|---------------------|-----------------|-----------|
| **Benutzerkonto deaktiviert** (Insider-Bedrohung) | Benutzer kann nicht arbeiten; Dienste können für andere Benutzer fortgesetzt werden | Schnelle Untersuchung (<1 Stunde), um zu bestimmen, ob vollständige Blockierung oder teilweise Einschränkung gerechtfertigt |
| **Endpunkt isoliert** (Datenexfiltration in Gange) | Benutzer kann nicht auf Netzwerk zugreifen; Cloud-Dienste möglicherweise zugänglich | Sauberes Leihgerät bereitstellen, wenn Untersuchung 4 Stunden überschreitet |
| **Servicekonto-Zugangsdaten widerrufen** (API-Schlüssel geleakt) | Anwendung oder Integration kann ausfallen | Mit Anwendungseigentümer koordinieren; neue Zugangsdaten generieren; vor Widerruf testen, wo machbar |
| **Netzwerksegment quarantänisiert** (Massenexfiltration) | Mehrere Benutzer betroffen | Selten; erfordert ISB-Genehmigung; Kundenbenachrichtigung bei Auswirkungen auf externe Dienste |

**Kundenbenachrichtigung**: Falls DLP-Eindämmungsmassnahmen kundenorientierte Dienste beeinträchtigen, sollen Kunden gemäss Vorfallkommunikationsverfahren benachrichtigt werden (typischerweise innerhalb 1 Stunde bei Vorfällen mit Kundenauswirkung).

### Geschäftskontinuität und Notfallwiederherstellung

DLP-Kontrollen sollen die Geschäftskontinuitäts- und Notfallwiederherstellungsziele der Organisation unterstützen:

#### DLP in Notfallwiederherstellungs-Szenarien

Bei Aktivierung von Notfallwiederherstellungsverfahren:

| DR-Szenario | DLP-Durchsetzung | Begründung |
|-------------|-----------------|------------|
| **Primäres Rechenzentrum ausgefallen; Failover auf DR-Standort** | Vollständige DLP-Durchsetzung aufrechterhalten (DR-Standort-DLP identisch zum Primär konfiguriert) | Datenschutzanforderungen unverändert |
| **E-Mail-System ausgefallen; Notfalleinsatz alternativer E-Mail** | E-Mail-DLP gilt für alternatives System; falls technisch nicht machbar, verstärkte Überwachung und manuelle Überprüfung | Datenleck während Störung verhindern |
| **Netzwerkinfrastruktur ausgefallen; temporäre alternative Konnektivität** | Netzwerk-DLP kann reduziert sein; Endpunkt-DLP wird primäre Kontrolle | Endpunkteinheiten setzen Durchsetzung während Netzwerkstörung fort |
| **Ransomware-Vorfall; isolierte Netzwerksegmente** | DLP kann vorübergehend für Isolierung/Sanierung umgangen werden; verstärkte manuelle Aufsicht und Nachvorfallüberprüfung | Sicherheitsreaktion hat Vorrang; manuelle Kontrollen substituieren |

#### DLP-System-Wiederherstellungsprioritäten

DLP-Systeme sollen in die Notfallwiederherstellungsplanung mit definierten Wiederherstellungsprioritäten einbezogen werden:

| DLP-Komponente | Recovery Time Objective (RTO) | Recovery Point Objective (RPO) | Prioritätsstufe |
|----------------|------------------------------|-------------------------------|-----------------|
| **E-Mail-DLP** | 4 Stunden (kritisch für Geschäftsbetrieb) | 1 Stunde (Richtlinien/Regeländerungen) | Stufe 1 |
| **Endpunkt-DLP-Agenten** | Nicht anwendbar (unabhängig betrieben) | 24 Stunden (Richtliniensynchronisation) | Stufe 2 (Richtlinien-Push) |
| **Netzwerk-DLP** | 8 Stunden (Überwachung; keine Blockierung) | 24 Stunden (Protokolle) | Stufe 2 |
| **DLP-Management-Konsole** | 24 Stunden (für Richtlinienänderungen) | 4 Stunden (Konfiguration) | Stufe 2 |
| **CASB / Cloud-DLP** | Anbietermanaged (gemäss Anbieter-SLA) | Anbietermanaged | Stufe 1 (Anbieterverantwortung) |

#### Vorübergehende DLP-Richtlinienlockerung

In Ausnahmesituationen (grosser Vorfall, Notfallwiederherstellung, Notfallbetrieb) kann eine vorübergehende Lockerung von DLP-Richtlinien autorisiert werden:

- **Genehmigung erforderlich**: ISB + ITL (oder GF, falls beide nicht verfügbar).
- **Dokumentation**: Ausnahme mit Begründung, Ausgleichskontrollen, Dauer dokumentiert.
- **Ausgleichskontrollen**: Verstärkte manuelle Überprüfung, auf spezifische Benutzer/Datentypen beschränkt, zeitlich begrenzt.
- **Maximale Dauer**: 72 Stunden; Verlängerung erfordert erneute Genehmigung.
- **Prüfpfad**: Alle Aktivitäten während des Lockerungszeitraums protokolliert und nach dem Vorfall überprüft.

**Beispielszenario**: Während der Ransomware-Wiederherstellung muss das IT-Team grosse Datenmengen an einen normalerweise nicht genehmigten Cloud-Backup-Dienst übertragen. DLP erlaubt diese spezifische Übertragung vorübergehend mit verstärkter Protokollierung und Security-Team-Aufsicht.

#### Jährliche DR-Tests

DLP-Systeme sollen in jährliche Notfallwiederherstellungstests einbezogen werden:
- Verifizieren, dass DLP-Durchsetzung während Failover auf DR-Standort fortgesetzt wird.
- DLP-System-Wiederherstellung innerhalb RTO testen.
- Richtliniensynchronisation nach Wiederherstellung validieren.
- Testergebnisse und Lücken zur Behebung dokumentieren.

---

## DLP-Effektivitätstests

Die Organisation soll strukturierte Tests durchführen, um zu validieren, dass DLP-Kontrollen unautorisierte Datenoffenlegung wie vorgesehen erkennen und verhindern.

### Testprogramm

| Testtyp | Häufigkeit | Methode | Erfolgskriterien | Verantwortlich |
|---------|------------|---------|------------------|----------------|
| **Positiver Erkennungstest** (DLP soll blockieren) | Vierteljährlich | Test-E-Mails/Dateien mit simulierten sensiblen Daten (Test-Kreditkartennummern, Test-PII, Test-Zugangsdaten) an externe Adressen senden; Web-Uploads versuchen; USB-Übertragungen | 100 % Erkennung und Blockierung für Eingeschränkte Daten; >95 % für Vertrauliche Daten | Security Team |
| **Negativtest** (DLP soll erlauben) | Vierteljährlich | Legitime Geschäftskommunikation senden, die historisch Falsch-Positive generiert hat; Abstimmungseffektivität verifizieren | <5 % Falsch-Positiv-Rate | Security Team |
| **Kanalabdeckungsverifikation** | Vierteljährlich | Jeden überwachten Kanal (E-Mail, Webmail, Cloud-Upload, USB, Drucken, Mobile) mit Testdaten testen | Alle Kanäle im Geltungsbereich erkennen Testdaten | Security Team |
| **Umgehungsversuch-Tests** | Halbjährlich | Versuche, DLP durch gängige Techniken zu umgehen (Verschlüsselung, Verschleierung, alternative Kanäle, Protokoll-Tunneling) | Umgehungsversuche erkannt oder verhindert | Security Team + Red Team (falls verfügbar) |
| **Performance-Auswirkungs-Tests** | Jährlich | E-Mail-Latenz, Web-Proxy-Latenz, Endpunkt-CPU/Speicherauslastung bei Spitzenlast messen | Performance innerhalb Zielwerte (siehe Verfügbarkeitsabschnitt) | IT-Betrieb + Security Team |
| **Alarmweiterleitung und Eskalation** | Vierteljährlich | Test-Kritischalarm generieren; verifizieren, dass Incident-Ticket erstellt, Eskalation erfolgt, Reaktionszeit innerhalb SLA | 100 % der Testalarme korrekt verarbeitet | Security Team |

### Testdatenverwaltung

- **Testdatensätze**: Bibliothek von Testdateien mit simulierten sensiblen Daten pflegen:
  - Test-Kreditkartennummern (mit ungültigen Luhn-Algorithmusergebnissen)
  - Test-Schweizer AHV-Nummern mit bekannt ungültigen Prüfziffern
  - Test-PII (Namen, Adressen, E-Mails von fiktiven Personen)
  - Test-Zugangsdaten (gefälschte Passwörter, API-Schlüssel, Zertifikate)
- **Test-E-Mail-Konten**: Externe Test-E-Mail-Adressen für Senden/Empfangen von Testnachrichten pflegen.
- **Test-Dokumentation**: Jeder Test dokumentiert mit Datum, Testszenario, erwartetem Ergebnis, tatsächlichem Ergebnis, Bestanden/Nicht bestanden, Folgekorrekturen.

### Red-Team / Purple-Team-Tests

Soweit Ressourcen vorhanden sind, DLP in jährliche Sicherheitstestübungen einbeziehen:

- **Red Team**: Versucht Datenexfiltration mit realistischen Angreiferechniken (Insider-Bedrohungssimulation, kompromittiertes Kontonachbildung, APT-Exfiltrationsmuster).
- **Blue Team** (SOC/Security Team): Erkennt und reagiert unter Verwendung von DLP-Alarmen und anderer Überwachung.
- **Nachbesprechung**: Identifiziert DLP-Erkennungslücken, Regelverbesserungen, Abdeckungserweiterungen.
- **Verbesserungs-Tracking**: Massnahmenpunkte aus der Übung im Korrektivmassnahmen-Register verfolgt.

**Für Organisationen ohne Red-Team-Kapazität**: Tischübungen zur Simulation von Datenexfiltrationsszenarien dienen als akzeptable Alternative. Szenarien sollten abdecken:
- Insider-Bedrohung (unzufriedener Mitarbeiter exfiltriert Kundendaten)
- Kompromittiertes Konto (Angreifer nutzt gestohlene Zugangsdaten zur Datenexfiltration)
- Versehentliche Offenlegung (Benutzer sendet sensible Daten an falschen Empfänger)
- Supply-Chain-Angriff (System eines Dritten zur Datenexfiltration genutzt)

### Test-Dokumentation

Alle Testaktivitäten dokumentiert mit:
- Testdatum, Tester, Testumfang.
- Testszenarien und erwartete Ergebnisse.
- Tatsächliche Ergebnisse (Bestanden/Nicht bestanden, Erkennungsraten, Falsch-Positive).
- Identifizierte Lücken und Schweregradbeurteilung.
- Korrektivmassnahmen mit Fälligkeitsdaten und Verantwortlichen.
- Folgevalidierung von Korrektivmassnahmen.

**Testaufzeichnungen 3 Jahre aufbewahrt; Testfehler an ISB eskaliert; kritische Lücken innerhalb 30 Tage behoben.**

---

## Management-Berichterstattung und Aufsicht

DLP-Programmeffektivität und -Compliance sollen der Geschäftsleitung gemeldet werden, um Governance und Aufsicht nachzuweisen.

### Vierteljährliches Executive Dashboard

Der ISB soll der Geschäftsleitung vierteljährlich eine DLP-Programmzusammenfassung mit folgenden Inhalten vorlegen:

| Abschnitt | Enthaltene Metriken | Zweck |
|-----------|---------------------|-------|
| **Programmstatus** | Kanalabdeckung %; aktive Ausnahmen; Falsch-Positiv-Rate-Trend | Gesamtzustand des Programms |
| **Bedrohungserkennung** | Erkannte kritische/hohe Vorfälle; blockierte Exfiltrationsversuche; Insider-Bedrohungsindikatoren | Gelieferten Mehrwert demonstrieren |
| **Compliance-Status** | Vollständigkeit der Mitarbeiterbenachrichtigung; aktuelle Verhältnismässigkeitsbewertung; regulatorische Anforderungen erfüllt | Rechtliche/regulatorische Zusicherung |
| **Performance** | Verfügbarkeit %; Falsch-Positiv-Trend; Benutzerreklamationen | Betriebseffektivität |
| **Kontinuierliche Verbesserung** | Durchgeführte Richtlinienabstimmungsaktionen; behobene Abdeckungslücken; Testergebnisse | Programmreife |

### Jährliches Management Review

Im Rahmen des ISO-27001-Management-Reviews (Abschnitt 9.3) soll der ISB eine jährliche DLP-Programmüberprüfung mit folgenden Inhalten vorlegen:

- **Programmeffektivität**: Hat DLP Datenverletzungen verhindert? Erkannte vs. verpasste Vorfälle.
- **Compliance**: Compliance mit schweizerischem Arbeitsrecht; Compliance mit Datenschutzrecht; Prüfungsergebnisse.
- **Technologiebewertung**: Aktuelle DLP-Technologie angemessen? Anbieterleistung? Lücken, die Investitionen erfordern?
- **Risikolandschaft-Änderungen**: Neue Exfiltrationsbedrohungen; neue zu schützende Datentypen; neue Ausgabekanäle.
- **Budget und Ressourcen**: Aktuelle Personalausstattung angemessen? Technologie-Erneuerungsbedarf? Schulungsanforderungen.
- **Strategische Empfehlungen**: Programmverbesserungen; Richtlinienänderungen; Investitionsprioritäten.

**Überprüfungsdokumentation**: 3 Jahre aufbewahrt; Managemententscheidungen und Massnahmenpunkte verfolgt.

### Vorstandsberichterstattung (falls anwendbar)

Für Organisationen mit Prüfungsausschüssen oder Risikoaufsicht auf Vorstandsebene, jährliche DLP-Zusammenfassung mit folgenden Inhalten:

- Hochrangige Programmeffektivität (kritische Vorfälle, regulatorischer Compliance-Status).
- Bedeutende DLP-Vorfälle und Lessons Learned.
- Regulatorische Risiken und Compliance-Postur (Arbeitsrecht, Datenschutzrecht).
- Strategische Investitionen und Programmreife-Progression.
- Benchmarking gegen Branchenkollegen (falls verfügbar).

**Vorstandsberichterstattung mindestens 7 Jahre aufbewahrt (Corporate-Governance-Aufzeichnungen).**

---

## Ausnahmenmanagement

Ausnahmen von DLP-Richtlinienanforderungen sollen schriftlich beantragt werden und umfassen:

- Spezifische Anforderungen, für die eine Ausnahme beantragt wird.
- Geschäftsbegründung und Anwendungsfall-Beschreibung.
- Risikobewertung (Wahrscheinlichkeit des Datenlecks, Auswirkung bei Datenleck).
- Ausgleichskontrollen (Verschlüsselung, verstärkte Überwachung, begrenzter Umfang, zeitgebundener Zugang).
- Beantragte Ausnahmedauer (maximal 12 Monate; Einmalübertragungen können ohne laufende Ausnahme genehmigt werden).

**Genehmigungsbehörde**:

| Ausnahmetyp | Erforderliche Genehmigung |
|-------------|--------------------------|
| Einmalige Einzelübertragung | Security-Team-Lead |
| Individuelle Benutzerausnahme | Security-Team-Lead + Vorgesetzter |
| Abteilungs- oder Gruppenausnahme | ISB + Abteilungsleiter |
| Kanalausnahme (Überwachung für einen Kanal deaktivieren) | ISB + ITL |
| Datenklassifizierungsausnahme (Schutz für eine Datenkategorie reduzieren) | ISB + Geschäftsleitung |

**Einschränkungen**: Folgende Ausnahmen sind unter keinen Umständen gestattet:

- DLP-Schutz für Eingeschränkte Daten ohne Ausgleichskontrollen deaktivieren.
- DLP für Zugangsdaten-Übertragungen (Passwörter, API-Schlüssel, Zertifikate) umgehen.
- Dauerhafte Ausnahmen ohne dokumentierte Ausgleichskontrollen und regelmässige Überprüfung.

Alle aktiven Ausnahmen sollen im DLP-Ausnahmenregister (Format: DLP-EX-JJJJ-NNN) aufgezeichnet, mindestens vierteljährlich überprüft und widerrufen werden, wenn die Geschäftsbegründung entfällt oder sich das Risikoprofil ändert.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **CASB** | Cloud Access Security Broker — Sicherheitsrichtlinien-Durchsetzungspunkt zwischen Cloud-Dienstkonsumenten und Cloud-Dienstanbietern |
| **Inhaltsinspektion** | Analyse von Dateninhalten zur Erkennung sensibler Informationen mittels Mustererkennung, Schlüsselworterkennung und regulären Ausdrücken |
| **Kontextanalyse** | Bewertung des Datenübertragungskontexts (Quelle, Ziel, Benutzerrolle, Volumen, Zeitpunkt) zur Risikobewertung |
| **Datenleck** | Unbeabsichtigte oder unautorisierte Offenlegung sensibler Informationen gegenüber externen oder nicht autorisierten internen Parteien |
| **Prävention von Datenlecks (DLP)** | Technologien, Prozesse und Richtlinien zur Erkennung, Verhinderung und Reaktion auf unautorisierte Datenoffenlegung |
| **Erkennungsmodus** | Betriebsmodus, der die DLP-Reaktion bestimmt: Nur überwachen, Benutzer auffordern, blockieren oder quarantänisieren |
| **Ausgabekanal** | Jeder Kommunikationspfad, über den Daten die Kontrolle der Organisation verlassen können (E-Mail, Web, Endpunkt, Netzwerk, Cloud, Mobile, API) |
| **Exfiltration** | Nicht autorisierte Übertragung von Daten aus organisatorischen Systemen an externe Standorte oder Akteure |
| **Falsch-Negativ** | Datenleck, das trotz DLP-Kontrollen auftritt (umgangen oder nicht erkannt) |
| **Falsch-Positiv** | Legitime Geschäftsaktivität, die fälschlicherweise als DLP-Richtlinienverletzung identifiziert wird |
| **Fingerabdruck** | Hash-basiertes Dokument-Tracking, das DLP ermöglicht, spezifische Dokumente unabhängig von Dateiname oder Formatänderungen zu identifizieren |
| **Insider-Bedrohung** | Sicherheitsrisiko durch Personen mit autorisiertem Zugang, die absichtlich oder unabsichtlich Datenoffenlegungen verursachen |
| **MDM** | Mobile Device Management — Technologie zur Verwaltung und Sicherung mobiler Geräte mit Zugang zu Unternehmensdaten |
| **Verhältnismässigkeit** | Rechtliche Anforderung, dass Sicherheitsüberwachung dem legitimen Sicherheitsziel proportional und nicht übermässig in die Privatsphäre der Mitarbeitenden eingreifend sein muss |
| **Quarantäne** | Vorübergehende Zurückhaltung von Datenübertragungen für die Überprüfung durch das Security Team vor Freigabe oder dauerhafter Blockierung |
| **SIEM** | Security Information and Event Management — Plattform für zentralisierte Protokollsammlung, -korrelation und Sicherheitsalarme |
| **TLS-Inspektion** | Entschlüsselung und Wiederverschlüsselung von TLS-verschlüsseltem Traffic an einem Netzwerk-Gateway für DLP-Inhaltsanalyse |
| **Transparenz** | Rechtliche Verpflichtung, Mitarbeitende vor Aktivierung über Überwachungsaktivitäten zu informieren |

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; DLP-Programmaufsicht; Genehmigung von Hochrisiko-Ausnahmen und Kanalausnahmen; Eskalation kritischer DLP-Vorfälle an Geschäftsleitung; jährliche Richtlinienüberprüfung; Budgetverantwortung für DLP-Technologie |
| **Informationssicherheitsbeauftragter** | Tägliche Richtlinienpflege; Ausnahmenüberprüfung; Sicherheitsüberwachung und Vorfalluntersuchung; Revisionskoordination; vierteljährliche Compliance-Berichterstattung an ISB |
| **Datenschutzbeauftragter (DSB)** | DLP-Überwachung auf Verhältnismässigkeit und Transparenz-Compliance prüfen; zu Meldepflichten beraten (nDSG Art. 24, DSGVO Art. 33/34); DLP-Einsatz aus Datenschutzperspektive genehmigen; Legitimate-Interest-Bewertungen durchführen oder überprüfen |
| **Security Team** | DLP-Lösungen über alle Kanäle einsetzen und pflegen; Erkennungsregeln und -richtlinien konfigurieren; Alarme überwachen und auf Vorfälle reagieren; Ausnahmeanträge bearbeiten; Richtlinien zur Reduzierung von Falsch-Positiven abstimmen; Abdeckungsbewertungen durchführen |
| **IT-Betrieb / Netzwerkteam** | DLP-Infrastruktur einsetzen und pflegen; sicherstellen, dass die Netzwerktopologie DLP-Abdeckung unterstützt (Traffic-Routing, TLS-Inspektionspunkte); DLP-Systemverfügbarkeit und -leistung aufrechterhalten; mit Security Team bei Netzwerkänderungen koordinieren |
| **Dateneigentümer / Systemeigentümer** | Daten in ihrer Domäne klassifizieren; Schutzanforderungen definieren; DLP-Vorfälle mit ihren Daten überprüfen; Ausnahmen für geschäftlich begründete Übertragungen genehmigen |
| **HR** | Sicherstellen, dass Arbeitsverträge DLP-Überwachungsbestätigung beinhalten; bei Disziplinarmassnahmen bei Richtlinienverstössen koordinieren; Transparenzanforderungen unterstützen (Datenschutzhinweise, Aktualisierungen des Mitarbeiterhandbuchs) |
| **Rechtsabteilung / Compliance** | DLP-Richtlinien auf rechtliche Compliance prüfen (Arbeitsrecht, Datenschutzrecht); zu regulatorischer Auslegung beraten; Vorfalluntersuchungen mit rechtlicher Expertise unterstützen |
| **Alle Mitarbeitenden** | DLP-Richtlinien und Anforderungen zur akzeptablen Nutzung einhalten; Falsch-Positive und Nutzbarkeitsprobleme melden; Ausnahmeprozess für legitime Geschäftsbedürfnisse nutzen; jährliche DLP-Sensibilisierungsschulung absolvieren; keine Versuche, DLP-Kontrollen zu umgehen |

---

## Nachweise

Die folgenden Nachweise demonstrieren die Einhaltung dieser Richtlinie. **Für SOC-2-Typ-II-Revisionen** werden Prüfer die Betriebseffektivität über den Revisionszeitraum (typischerweise 12 Monate) testen.

| # | Nachweis | Verantwortlich | Häufigkeit | Aufbewahrung |
|---|----------|----------------|------------|--------------|
| 1 | **DLP-Lösungsinventar** mit Einsatzumfang, Kanalabdeckung und Versionsinformationen | Security Team | Laufend gepflegt; vierteljährlich überprüft | Lebenszeit des Einsatzes + 3 Jahre |
| 2 | **Datenklassifizierungsinventar** mit sensiblen Datenkategorien, Erkennungsregeln und DLP-Regelzuordnungen | Security Team / Dateneigentümer | Laufend gepflegt; vierteljährlich gegen Inventarverzeichnis abgeglichen | 3 Jahre |
| 3 | **Kanalabdeckungsbewertung** mit Testergebnissen pro Kanal (E-Mail, Web, Endpunkt, Netzwerk, Cloud, Mobile) | Security Team | Vierteljährlich | 3 Jahre |
| 4 | **DLP-Alarm- und Vorfallprotokoll** (blockierte Übertragungen, Richtlinienverletzungen, kritische Alarme, Vorfallberichte) | Security Team | Laufend | Sicherheitsereignisse: 12 Monate; Betriebsprotokolle: 90 Tage |
| 5 | **DLP-Leistungsmetriken** (Falsch-Positiv-Rate, SLA-Einhaltung, Abdeckung, Erkennungsrate, Abstimmungseffektivität) | Security Team / ISB | Monatliche Metriken; vierteljährliche Überprüfung | 3 Jahre |
| 6 | **DLP-Ausnahmenregister** (Anträge, Genehmigungen, Ausgleichskontrollen, Ablaufdaten, Überprüfungsaufzeichnungen) | Security-Team-Lead | Laufend gepflegt; vierteljährlich überprüft | Ausnahmedauer + 3 Jahre |
| 7 | **Verhältnismässigkeitsbewertung** zur Dokumentation, dass DLP-Überwachung dem Sicherheitsziel proportional ist | DSB / ISB | Vor dem Einsatz; jährlich überprüft | Lebenszeit des Einsatzes + 3 Jahre |
| 8 | **Mitarbeiterbenachrichtigungsaufzeichnungen** (unterzeichnete Verträge/Ergänzungen, Datenschutzhinweis-Verteilung, Akzeptanznutzungsbestätigungen) | HR / Rechtsabteilung | Pro Onboarding; jährlich für Sensibilisierungsschulung | Beschäftigungsdauer + 3 Jahre |
| 9 | **DLP-Sensibilisierungsschulungsabschlussaufzeichnungen** | ISB / HR | Jährlich | Beschäftigungsdauer + 3 Jahre |
| 10 | **DLP-Vorfallreaktionsaufzeichnungen** (Zeitplan, Eindämmung, Untersuchung, Sanierung, Lessons Learned) | Security Team | Pro Vorfall | 3 Jahre |
| 11 | **Datenschutzverletzungs-Meldungsaufzeichnungen** (eingereichte regulatorische Meldungen, gesendete Betroffenenbenachrichtigungen) | DSB / Rechtsabteilung | Pro Vorfall | 7 Jahre |
| 12 | **DLP-Regelabstimmungsprotokoll** (geänderte Regeln, Falsch-Positiv-Reduktion, Begründung, Genehmigung) | Security Team | Pro Änderung | 3 Jahre |
| 13 | **Arbeitnehmervertretungs-Konsultationsaufzeichnungen** (wo anwendbar) | HR | Vor dem Einsatz; pro Umfangsänderung | Lebenszeit des Einsatzes + 3 Jahre |
| 14 | **DLP-Protokollzugangskontrollen-Aufzeichnungen** (wer Zugang hat, Begründung, Überprüfungsaufzeichnungen) | IT-Betrieb / Security Team | Laufend gepflegt; vierteljährlich überprüft | 3 Jahre |
| 15 | **Kundendatenschutz-Zuordnung** (Kundenverträge zu Datenklassifizierung zu DLP-Regeln) | Security Team + Rechtsabteilung | Pro Kunde; vierteljährlich überprüft | 3 Jahre |
| 16 | **Kundenbenachrichtigungsaufzeichnungen** (DLP-Vorfälle mit Kundendaten) | Security Team + Customer Success | Pro Vorfall | 7 Jahre |
| 17 | **DLP-Systemverfügbarkeitsberichte** (Betriebszeit, Leistungs-, Kapazitätsmetriken) | IT-Betrieb | Monatlich | 3 Jahre |
| 18 | **DLP-Effektivitäts-Testergebnisse** (vierteljährliche positive/negative/Umgehungstests) | Security Team | Vierteljährlich | 3 Jahre |
| 19 | **Anbieter-SOC-2-Berichte** (für Cloud-DLP, CASB-Anbieter) | IT-Betrieb / Security Team | Jährlich (Anbieterberichterhalt) | 3 Jahre |
| 20 | **Anbieter-Performance-Reviews** (für Cloud-DLP-Anbieter) | Security-Team-Lead | Jährlich pro Anbieter | 3 Jahre |
| 21 | **Notfallwiederherstellungs-Testergebnisse** (DLP-Wiederherstellungstests) | IT-Betriebsleiter | Jährlich (pro DR-Test) | 3 Jahre |
| 22 | **Vierteljährliche Executive Dashboards** (DLP-Programmstatus) | ISB | Vierteljährlich | 3 Jahre |
| 23 | **Jährliche Management-Review-Präsentation** (DLP-Programmüberprüfung) | ISB | Jährlich | 3 Jahre |

### SOC-2-Typ-II-Revisions-Stichprobenerwartungen

Prüfer werden typischerweise Stichproben nehmen von:
- **25 DLP-Alarmen** über Schweregradebenen (Reaktion innerhalb SLA verifizieren, Dokumentation vollständig).
- **Alle kritischen/hohen Vorfälle** (Eindämmung, Untersuchung, Kundenbenachrichtigung falls anwendbar verifizieren).
- **Alle aktiven Ausnahmen** (Genehmigung verifizieren, Überprüfungsplan eingehalten, Ausgleichskontrollen dokumentiert).
- **Alle vierteljährlichen Testzyklen** (Tests durchgeführt, Ergebnisse dokumentiert, Lücken behoben verifizieren).
- **Alle Anbieterüberprüfungen** (abgeschlossen, aktuelle SOC-2-Berichte erhalten verifizieren).
- **Mitarbeiterbenachrichtigungsnachweise** für **25 Mitarbeitende** (Schulungsabschluss, Bestätigung dokumentiert verifizieren).
- **Verhältnismässigkeitsbewertung** (aktuell, von DSB/ISB genehmigt verifizieren).

**Vollständigkeit ist kritisch**: Fehlende Nachweise für ein Stichprobenelement stellen einen Revisionsbefund dar. Kontinuierliche Dokumentation während des gesamten Revisionszeitraums sicherstellen.

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheitsmanagement-Team verifiziert die Einhaltung dieser Richtlinie durch verschiedene Methoden, einschliesslich, aber nicht beschränkt auf, DLP-Systemreports, Kanalabdeckungsbewertungen, Vorfallreaktionsaufzeichnungen, Ausnahmenregisterüberprüfungen, Mitarbeiterbenachrichtigungsüberprüfungen, interne und externe Revisionen sowie Rückmeldungen an den Richtlinieneigentümer.

**Compliance-Metriken**:

| Metrik | Ziel | Messhäufigkeit |
|--------|------|----------------|
| DLP-Kanalabdeckung (kritische Ausgabepfade) | >= 95 % | Vierteljährlich |
| DLP-Alarmreaktion innerhalb SLA | >= 95 % | Wöchentlich |
| Falsch-Positiv-Rate | < 10 % | Monatlich |
| Aktive Ausnahmen planmässig überprüft | 100 % | Vierteljährlich |
| Mitarbeiter-DLP-Sensibilisierungsschulung abgeschlossen | >= 95 % | Jährlich |
| Mitarbeiterüberwachungs-Transparenzdokumentation vollständig | 100 % | Jährlich |
| Verhältnismässigkeitsbewertung aktuell und genehmigt | 100 % | Jährlich |

**Compliance-Bewertung**:

| Komponente | Gewichtung | Berechnung |
|------------|------------|------------|
| Kanalabdeckung | 30 % | (Kanäle mit verifizierter DLP-Abdeckung) / (Gesamte kritische Ausgabekanäle) x 100 |
| Vorfallreaktionseffektivität | 25 % | (Vorfälle innerhalb SLA reagiert) / (Gesamte Vorfälle) x 100 |
| Richtlinienabstimmung und Falsch-Positiv-Management | 20 % | Kehrwert der Falsch-Positiv-Rate + Abstimmungsverbesserungstrend |
| Rechtliche Compliance (Transparenz, Verhältnismässigkeit) | 15 % | (Abgeschlossene rechtliche Anforderungen) / (Gesamte rechtliche Anforderungen) x 100 |
| Ausnahmenmanagement | 10 % | (Planmässig überprüfte Ausnahmen) / (Gesamte aktive Ausnahmen) x 100 |

**Umgang mit Nichteinhaltung**: Unter 70 % erfordert sofortige ISB-Eskalation und Massnahmenplan innerhalb 30 Tagen. 70–89 % erfordert Aufsicht des Informationssicherheitsbeauftragten mit monatlichen Überprüfungen. 90 % und höher folgt der standardmässigen vierteljährlichen Überwachung.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll im Voraus vom Informationssicherheitsbeauftragten genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum (maximal 12 Monate). Ausnahmen sollen dem Management-Review-Team gemeldet werden. Dauerhafte Ausnahmen sind ohne dokumentierte Ausgleichskontrollen und vierteljährliche Überprüfung nicht gestattet.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung des Arbeitsverhältnisses. Absichtliche Versuche, DLP-Kontrollen zu umgehen, sollen als schwerwiegendes Fehlverhalten behandelt werden. Richtlinienverstösse sollen dokumentiert, vom Informationssicherheitsbeauftragten untersucht und dem ISB gemeldet werden. Wo Verstösse Verletzungen personenbezogener Daten beinhalten, soll der DSB konsultiert werden.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Änderungen der DLP-Technologiefähigkeiten, sich entwickelnde Datenexfiltrationstechniken (Insider-Bedrohungen, Advanced Persistent Threats, Supply-Chain-Angriffe), regulatorische Änderungen zur Mitarbeiterüberwachung oder zu Datenschutzanforderungen, Revisionsergebnisse, DLP-Leistungsmetriken und -trends, Falsch-Positiv-Rückmeldungen von Benutzern sowie Lessons Learned aus DLP-Vorfällen berücksichtigen.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Richtlinie zur Prävention von Datenlecks — Zuordnung der ISO-27001-Massnahmen

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Abschnitt 5.1 Führung und Verpflichtung | 5.1 Richtlinien zur Informationssicherheit |
| Abschnitt 5.2 Richtlinie | 5.10 Akzeptable Nutzung von Informationen und anderen Werten |
| Abschnitt 6.1 Massnahmen zum Umgang mit Risiken | 5.12 Klassifizierung von Informationen |
| Abschnitt 6.2 Informationssicherheitsziele | 5.13 Beschriftung von Informationen |
| Abschnitt 7.3 Bewusstsein | 5.14 Informationsübertragung |
| Abschnitt 9.1 Überwachung, Messung, Analyse und Bewertung | **8.12 Prävention von Datenlecks** |
| Abschnitt 9.3 Management Review | 8.15 Protokollierung |
| Abschnitt 10.1 Kontinuierliche Verbesserung | 8.16 Überwachungsaktivitäten |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen für den Datenschutz; DLP als technische Massnahme. Art. 6 — Grundsätze der Verhältnismässigkeit, Zweckbindung und Transparenz |
| Schweizerisches OR Art. 328b | Mitarbeiterdatenverarbeitung begrenzt auf Eignung für Arbeitsverhältnis und Vertragserfüllung; DLP-Überwachung muss entsprechen |
| Schweizerische ArGV 3 Art. 26 | Verbot von Überwachungssystemen zur Verhaltenskontrolle; DLP zulässig, wenn primärer Zweck der Datenschutz ist |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU-DSGVO (wo anwendbar) | Art. 5 (Verarbeitungsgrundsätze), Art. 6 (Rechtmässige Grundlage), Art. 32 (Sicherheitsmassnahmen), Art. 33/34 (Datenpannenmeldung), Art. 88 (Verarbeitung im Beschäftigungskontext) |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.12 — Prävention von Datenlecks |
| ISO/IEC 27002:2022 | Abschnitt 8.12 — Implementierungsleitfaden für Massnahmen zur Prävention von Datenlecks |
| NIST SP 800-53 Rev 5 | AC-4 (Information Flow Enforcement), SC-7 (Boundary Protection), SI-4 (System Monitoring) |
| CIS Controls v8 | 3.1–3.14 (Data Protection), 3.13 (Deploy a Data Loss Prevention Solution) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
