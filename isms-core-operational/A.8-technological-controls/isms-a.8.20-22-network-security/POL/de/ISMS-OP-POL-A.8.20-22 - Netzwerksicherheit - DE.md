<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.20-22-DE:operational:OP-POL:a.8.20-22 -->
**ISMS-OP-POL-A.8.20-22 — Netzwerksicherheit**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Netzwerksicherheit |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.20-22 |
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

- ISO/IEC 27001:2022 Massnahmen A.8.20, A.8.21, A.8.22 — Netzwerksicherheit, Sicherheit von Netzwerkdiensten, Trennung von Netzwerken

**Verwandte Annex-A-Massnahmen**:

| Massnahme | Bezug zur Netzwerksicherheit |
|-----------|------------------------------|
| A.5.14 Informationsübertragung | Verschlüsselung und sichere Kanalanforderungen für Daten bei der Übertragung |
| A.5.15 Zugangskontrolle | Netzwerkzugangskontrolle abgestimmt auf Identitäts- und Zugriffsrichtlinie |
| A.5.23 Informationssicherheit für Cloud-Dienste | Cloud-Netzwerkverbindung und -segmentierung |
| A.8.1 Benutzer-Endgeräte | Endpunkt-Compliance vor Netzwerkzulassung |
| A.8.5 Sichere Authentifizierung | Authentifizierung für Netzwerkzugang (802.1X, VPN) |
| A.8.9 Konfigurationsmanagement | Netzwerkgerätekonfigurationsstandards und Härtung |
| A.8.15 Protokollierung | Netzwerkereignis- und Traffic-Protokollierung |
| A.8.16 Überwachungsaktivitäten | Netzwerküberwachung, IDS/IPS, Anomalieerkennung |
| A.8.23 Web-Filterung | URL/DNS-Filterung als netzwerkbasierte Kontrolle |
| A.8.24 Verwendung kryptografischer Verfahren | TLS/IPsec für verschlüsselten Netzwerktransport |

**Verwandte interne Richtlinien**:

- Zugangskontrollrichtlinie
- Richtlinie zur Verwendung kryptografischer Verfahren
- Richtlinie zur Informationsübertragung
- Richtlinie zur physischen und umgebungsbezogenen Sicherheit
- Asset-Management-Richtlinie
- Protokollierungsrichtlinie
- Richtlinie zu Überwachungsaktivitäten (A.8.16)

---

# Richtlinie zur Netzwerksicherheitsverwaltung

## Zweck

Zweck dieser Richtlinie ist es, den Schutz von Informationen in Netzwerken und den zugehörigen Informationsverarbeitungseinrichtungen sicherzustellen.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) und die Datenschutzverordnung (DSV) durch die Implementierung technischer und organisatorischer Massnahmen, die dem Risiko angemessen sind, um personenbezogene Daten (einschliesslich besonders schützenswerter Personendaten) durch Netzwerksicherheitskontrollen zu schützen. Soweit die Organisation Daten von Personen im EU/EWR-Raum verarbeitet, gelten zudem DSGVO-Anforderungen.

## Geltungsbereich

Alle Mitarbeitenden und Drittbenutzer.

Alle Netzwerke, Netzwerkdienste, Netzwerkverwaltungs- und -managementlösungen sowie Netzwerkgeräte der Organisation, die im Geltungsbereich der ISO-27001-Geltungsbereichserklärung definiert sind.

## Grundsatz

Das Netzwerk wird auf Basis des Least-Privilege-Prinzips mit Security by Design und Default verwaltet. Netzwerkzugang wird standardmässig verweigert und nur mit dokumentierter Genehmigung gewährt. Alle Netzwerkarchitekturentscheidungen sollen risikobasiert sein und dabei die Klassifizierung von Informationen und die Kritikalität von Systemen berücksichtigen.

---

## Netzwerkkontrollen

- Verantwortlichkeiten und Verfahren für das Management von Netzwerkgeräten sollen festgelegt und dokumentiert werden.
- Die betriebliche Verantwortung für Netzwerke soll, wo angemessen, von den Computeroperationen getrennt werden.
- Besondere Kontrollen sollen eingerichtet werden, um Vertraulichkeit und Integrität von Daten zu schützen, die über öffentliche Netzwerke oder drahtlose Netzwerke übertragen werden, sowie die verbundenen Systeme und Anwendungen zu sichern.
- Geeignete Protokollierung und Überwachung sollen angewendet werden, um die Aufzeichnung und Erkennung von Massnahmen zu ermöglichen, die die Informationssicherheit beeinflussen oder dafür relevant sind.
- Managementaktivitäten sollen eng koordiniert werden, sowohl um den Service für die Organisation zu optimieren als auch um sicherzustellen, dass Kontrollen konsistent über die Informationsverarbeitungsinfrastruktur angewendet werden.
- Systeme im Netzwerk sollen authentifiziert werden, bevor ihnen Zugang gewährt wird.
- Systemverbindungen zum Netzwerk sollen auf autorisierte und konforme Geräte beschränkt werden.
- Standard-Passwörter und -Konten von Netzwerkgeräten sollen vor dem Einsatz geändert oder deaktiviert werden.
- Administrativer Zugang zu Netzwerkgeräten soll verschlüsselte Verwaltungsprotokolle verwenden (SSH, HTTPS). Telnet und unverschlüsseltes SNMP (v1/v2c) sollen nicht verwendet werden.
- Firmware und Software von Netzwerkgeräten sollen auf aktuellen, vom Hersteller unterstützten Versionen gehalten werden. Sicherheits-Patches sollen gemäss folgenden Zeitplänen eingespielt werden:

| Schweregrad | Zeitrahmen |
|-------------|------------|
| Kritische Schwachstellen (CVSS 9.0+, aktive Ausnutzung) | Innerhalb von 14 Tagen |
| Hohe Schwachstellen (CVSS 7.0–8.9) | Innerhalb von 30 Tagen |
| Mittlere Schwachstellen (CVSS 4.0–6.9) | Innerhalb von 90 Tagen |
| Niedrige Schwachstellen (CVSS 0.1–3.9) | Im nächsten geplanten Wartungsfenster |

Notfall-Patches für aktiv ausgenutzte Schwachstellen können ohne Tests in der Nicht-Produktionsumgebung mit ISB-Genehmigung und dokumentierter Risikoakzeptanz eingespielt werden.

## Sicherheit von Netzwerkdiensten

Sicherheitsmechanismen, Servicelevel und Managementanforderungen aller Netzwerkdienste sollen identifiziert und in Netzwerkdienstvereinbarungen aufgenommen werden, unabhängig davon, ob diese Dienste intern oder ausgelagert erbracht werden.

Die Fähigkeit des Netzwerkdienstleisters, vereinbarte Dienste sicher zu verwalten, soll festgestellt und regelmässig überwacht werden, und das Prüfungsrecht soll vereinbart werden.

Die für bestimmte Dienste erforderlichen Sicherheitsvorkehrungen, wie Sicherheitsmerkmale, Servicelevel und Managementanforderungen, sollen identifiziert werden. Die Organisation soll sicherstellen, dass Netzwerkdienstleister diese Massnahmen implementieren.

Netzwerkdienste umfassen, sind aber nicht beschränkt auf:

- DNS-, DHCP- und NTP-Dienste.
- E-Mail-, Dateifreigabe- und Webanwendungsdienste.
- Firewall-, Einbruchserkennungs-/-verhinderungs- und Gateway-Sicherheitsdienste.
- Fernzugang- und VPN-Dienste.

## Trennung von Netzwerken

Grosse Netzwerke sollen in separate Netzwerkdomänen unterteilt werden. Die Domänen sollen auf Basis von Vertrauensstufen, Datenklassifizierung und Geschäftsfunktion gewählt werden.

Trennung kann durch physisch unterschiedliche Netzwerke oder durch verschiedene logische Netzwerke erreicht werden (z. B. VLANs, Software-Defined Networking).

Der Perimeter jeder Domäne soll klar definiert sein. Zugang zwischen Netzwerkdomänen soll am Perimeter durch ein Gateway kontrolliert werden (z. B. Firewall, Filterrouter) mit einer Default-Deny-Grundhaltung.

Die Kriterien für die Segmentierung von Netzwerken in Domänen und der über die Gateways erlaubte Zugang sollen auf einer Bewertung der Sicherheitsanforderungen jeder Domäne basieren. Die Bewertung soll in Übereinstimmung mit der Zugangskontrollrichtlinie, Zugriffsanforderungen, dem Wert und der Klassifizierung der verarbeiteten Informationen erfolgen und die relativen Kosten und Leistungsauswirkungen der Einbeziehung geeigneter Gateway-Technologie berücksichtigen.

**Firewall-Regelsteuerung:**

- Alle Firewall-Regeländerungen sollen einem dokumentierten Change-Management-Prozess mit Geschäftsbegründung und Genehmigung folgen.
- Firewall-Regelsätze sollen mindestens **jährlich** überprüft werden, um veraltete Regeln zu entfernen und die weitere Geschäftsbegründung zu verifizieren.
- Überprüfungen sollen mit Abzeichnung des Netzwerkadministrators und des ISB dokumentiert werden.
- Default-Deny-Richtlinie soll bei jeder Überprüfung verifiziert werden (gesamter Traffic blockiert, sofern nicht explizit erlaubt).

Mindest-Netzwerksegmente sollen umfassen:

| Segment | Zweck |
|---------|-------|
| Unternehmens-/Benutzernetzwerk | Standard-Mitarbeiter-Workstations und -geräte |
| Server-/Anwendungsnetzwerk | Geschäftsanwendungen und Datenbanken |
| Verwaltungsnetzwerk | Netzwerkgeräteverwaltung (Out-of-Band, soweit machbar) |
| Gastnetzwerk | Besucher- und Nicht-Unternehmensgerätezugang (vom Unternehmen isoliert) |
| IoT-/OT-Netzwerk | Internet-of-Things- und Betriebstechnologie-Geräte (isoliert) |

Zusätzliche Segmente (z. B. DMZ für öffentlich zugängliche Dienste, Entwicklungs-/Testumgebungen) sollen auf Basis einer Risikobewertung erstellt werden.

### Gastnetzwerkanforderungen

Gastnetzwerke sollen mit folgenden Sicherheitskontrollen konfiguriert werden:

- **Isolierung**: Kein Zugang zu Unternehmens-Netzwerksegmenten (Firewall-Regeln sollen Trennung durchsetzen).
- **Nur-Internet-Zugang**: Gäste sollen ausschliesslich auf das Internet, nicht auf interne Ressourcen zugreifen.
- **Verschlüsselung**: WPA2-Personal mindestens mit starkem Passwort oder WPA2-Enterprise mit Gast-Zugangsdaten.
- **Zeitlich begrenzter Zugang**: Gast-Zugangsdaten sollen nach einem definierten Zeitraum ablaufen (z. B. 24 Stunden) und bei Bedarf neu ausgestellt werden.
- **Überwachung**: Gastnetzwerk-Traffic soll für Sicherheitsuntersuchungen protokolliert werden, falls erforderlich.

Das Gastnetzwerk-Passwort soll mindestens **vierteljährlich** oder sofort bei Verdacht auf Kompromittierung geändert werden.

### Sicherheit für IoT- und OT-Geräte

IoT-(Internet of Things-) und OT-(Betriebstechnologie-)Geräte sollen in einem isolierten Netzwerksegment mit folgenden Kontrollen platziert werden:

- IoT/OT-Geräte sollen keinen direkten, unkontrollierten Internetzugang haben. Internetkommunikation soll über einen Proxy oder ein Gateway mit zugelassenen Zielen geleitet werden.
- IoT/OT-Geräte sollen ohne VPN und explizite Autorisierung nicht über das Internet erreichbar sein.
- Zugang vom Unternehmensnetzwerk zum IoT/OT-Segment soll durch Firewall-Regeln auf autorisiertes Personal beschränkt sein.
- Fernzugang von Drittanbieter-Anbietern zu IoT/OT-Geräten soll Genehmigung, VPN und zeitlich begrenzte Zugangsdaten erfordern.
- Alle Standard-Passwörter von IoT/OT-Geräten sollen vor dem Einsatz geändert werden.
- Alle IoT/OT-Geräte sollen im Asset-Register mit Eigentümer, Zweck und Netzwerkstandort erfasst werden.

### Drahtlosnetzwerk-Segmentierung

Drahtlose Netzwerke erfordern besondere Behandlung aufgrund des schlecht definierten Netzwerkperimeters. In sensiblen Umgebungen soll jeder Drahtloszugang als externe Verbindung behandelt und von internen Netzwerken isoliert werden, bis der Zugang durch ein Gateway gegangen ist, bevor Zugang zu internen Systemen gewährt wird.

Drahtlosnetzwerkzugang für Mitarbeitende und Gäste soll auf separaten SSIDs mit unterschiedlichen Sicherheitskontrollen segmentiert sein.

### Drahtlossicherheitsstandards

Folgende Drahtlossicherheitsstandards sollen gelten:

- WPA3 ist für alle Drahtlosnetzwerke bevorzugt.
- WPA2-Enterprise-Modus mit 802.1X-Authentifizierung und AES-Verschlüsselung ist der Mindestakzeptanzstandard für Unternehmensnetzwerke.
- WPA2-Personal-Modus kann für Nicht-Produktionsnetzwerke (z. B. Gastzugang) mit einem mindestens 16-stelligen zufälligen Passwort und AES-Verschlüsselung verwendet werden.
- WEP soll unter keinen Umständen verwendet werden.
- WPA (original) und TKIP-Verschlüsselung sollen nicht verwendet werden.

## Zugang zu Netzwerken und Netzwerkdiensten

Benutzer sollen nur mit Zugang zu dem Netzwerk und den Netzwerkdiensten ausgestattet werden, für die sie spezifisch autorisiert wurden.

Zugang zu Netzwerken und Netzwerkdiensten soll in Übereinstimmung mit der Zugangskontrollrichtlinie erfolgen.

Vor der Verbindung mit dem Netzwerk sollen Geräte:

- Im Asset-Register registriert sein.
- Auf die neuesten Sicherheits-Patch-Levels aktualisiert worden sein.
- Geeigneten Malware-Schutz installiert und aktuell haben.
- Standard-Passwörter und -Konten geändert oder deaktiviert haben.
- Soweit möglich in das Netzwerkverwaltungs- und -überwachungssystem einbezogen worden sein.
- Nicht benötigte Ports, Dienste, Anwendungen und Gastkonten entfernt oder deaktiviert haben.

Die Organisation soll technische Kontrollen implementieren, um Geräte-Compliance vor dem Gewähren von Netzwerkzugang durchzusetzen. Durchsetzungsmechanismen umfassen Network-Access-Control-(NAC-)Lösungen, 802.1X-zertifikat- oder anmeldedatenbasierte Authentifizierung, VPN-Gateway-Posture-Assessment oder manuelle Registrierung und Genehmigung durch IT. Nicht konforme Geräte sollen in einem Quarantäne- oder eingeschränkten Segment platziert werden, bis Compliance erreicht ist.

## Fernzugang

Fernzugang zum Organisationsnetzwerk soll mit verschlüsselten Tunneln (VPN oder gleichwertig) mit Multi-Faktor-Authentifizierung gesichert werden.

VPN-Verbindungen sollen aktuelle, sichere Protokolle verwenden:

- WireGuard oder IKEv2/IPsec sind bevorzugt.
- OpenVPN ist akzeptabel, wo WireGuard oder IKEv2 nicht unterstützt werden.
- PPTP und L2TP ohne IPsec sollen nicht verwendet werden.

Fernverbindungen sollen nach einer definierten Inaktivitätsperiode getrennt werden.

Eine Liste der Benutzer mit Fernzugang soll gepflegt und vierteljährlich überprüft werden.

Split-Tunneling (das erlaubt, dass einiger Traffic das VPN umgeht) kann nur gestattet werden, wenn:

- Eine dokumentierte Risikobewertung akzeptables Restrisiko nachweist.
- Auf alle Organisationsressourcen (Dateifreigaben, Datenbanken, Anwendungen, E-Mail) ausschliesslich über den verschlüsselten Tunnel zugegriffen wird.
- Split-getunnelter Traffic auf nicht sensible, Nur-Internet-Ziele beschränkt ist.
- Das Endgerät des Benutzers alle Sicherheitsbaseline-Anforderungen erfüllt (aktuelle Patches, Antivirus/EDR, Verschlüsselung).
- Split-Tunneling für privilegierte Konten und Administratorkonten deaktiviert ist.

## Netzwerkstandorte

Netzwerkinfrastruktur und Datenverarbeitungsstandorte sollen auf Basis von Risikobewertung, Datenklassifizierung und anwendbaren Datenschutzanforderungen ausgewählt werden.

Für die Platzierung von Netzwerkinfrastruktur, Rechenzentren und Cloud-Diensten, die personenbezogene oder vertrauliche Daten verarbeiten, gilt folgende Präferenzhierarchie:

1. Innerhalb der Schweiz.
2. Innerhalb von Ländern, die vom Schweizerischen Bundesrat gemäss **Anhang 1 der Datenschutzverordnung (DSV)** als angemessenen Datenschutz bietend anerkannt wurden. Die aktuelle Angemessenheitsliste wird vom EDÖB (Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter) veröffentlicht und soll vor dem Einsatz von Infrastruktur oder Diensten in einer neuen Jurisdiktion verifiziert werden.
3. Innerhalb von Ländern, wo Standardvertragsklauseln (SCC) oder andere geeignete Garantien gemäss nDSG Art. 16–17 vorhanden sind.

Grenzüberschreitende Datenübertragungen sollen der Richtlinie zur Informationsübertragung und nDSG-Anforderungen entsprechen. Die Rechtsabteilung soll den Angemessenheitsstatus jedes Landes vor dem Einsatz verifizieren.

## Physische Netzwerkgeräte

Physische Netzwerkgeräte sollen in Übereinstimmung mit der Richtlinie zur physischen und umgebungsbezogenen Sicherheit verwaltet werden, insbesondere den Abschnitten über Kabelführungssicherheit, Geräteaufstellung und -schutz sowie Zugangskontrolle.

Physische Netzwerkgeräte sollen in Übereinstimmung mit der Richtlinie zur Informationsklassifizierung und -handhabung vernichtet werden, insbesondere dem Abschnitt über die Vernichtung elektronischer Medien und Geräte.

Physische Netzwerkgeräte sollen in Übereinstimmung mit der Asset-Management-Richtlinie verwaltet und dem Asset-Management-Prozess unterworfen werden.

## Web-Filterung

Zugang zu Websites, die illegale Informationen enthalten oder bekannt dafür sind, bösartige Inhalte zu enthalten, soll eingeschränkt werden.

Zugang zu folgenden Website-Typen soll, soweit praktikabel, blockiert werden:

- Websites mit einer Informations-Upload-Funktion, sofern nicht aus gültigen Geschäftsgründen erlaubt.
- Bekannte oder verdächtige bösartige Websites (Phishing, Malware-Verteilung).
- Command-and-Control-Server.
- In Bedrohungsintelligenz-Feeds identifizierte bösartige Websites.
- Websites mit illegalen Inhalten.
- Proxy- und Anonymisierungsdienste (sofern nicht für genehmigte Geschäftszwecke erforderlich).

Web-Filterung soll mit DNS-basierter Filterung, Web-Proxy oder gleichwertiger Technologie implementiert werden. Filterkategorien und Ausnahmen sollen vierteljährlich überprüft werden.

### DNS-Sicherheit

- DNS-Resolver sollten DNSSEC-Signaturen validieren, wo verfügbar, um vor DNS-Spoofing zu schützen.
- Interne DNS-Zonen sollen nicht dem Internet ausgesetzt werden. Split-Horizon-DNS ist für Organisationen mit interner und externer Namensauflösung empfohlen.
- DNS-Abfragen sollten für Sicherheitsuntersuchung und Bedrohungserkennung protokolliert werden.

## Host-Einbruch, Netzwerk-Einbruch, Malware und Antivirus

Netzwerkdienste und -geräte sollen in Übereinstimmung mit der Malware- und Antivirus-Richtlinie verwaltet werden.

Host-Einbruchserkennung und Netzwerk-Einbruchserkennung/-verhinderung sollen risikobasiert, nach Geschäftsbedarf und soweit praktikabel eingesetzt werden.

**Mindest-IDS/IPS-Einsatzorte:**

| Standort | Typ | Zweck |
|----------|-----|-------|
| Internet-Perimeter (Firewall/Gateway) | Netzwerk-IDS/IPS | Externe Angriffe und bösartigen eingehenden Traffic erkennen/verhindern |
| Zwischen Netzwerksegmenten (Inter-VLAN) | Netzwerk-IDS/IPS | Laterale Bewegung zwischen Trust-Zonen erkennen |
| Server-/Anwendungsnetzwerk | Netzwerk-IDS oder hostbasiertes IDS | Anomalen Zugang zu kritischen Systemen erkennen |
| Endpunkte (Workstations, Server) | Hostbasiertes IDS (EDR/XDR) | Endpunkt-Bedrohungen, dateilose Malware, verdächtige Prozesse erkennen |
| Cloud-Workloads (IaaS/PaaS) | Cloud-natives IDS oder CASB | Bedrohungen für Cloud-Infrastruktur erkennen |

Zusätzliche Einsatzorte sollen durch Risikobewertung bestimmt werden. Wo dedizierte IDS/IPS-Appliances nicht machbar sind, sind gleichwertige Erkennungsfähigkeiten (z. B. EDR mit Netzwerksichtbarkeit, cloud-native Sicherheits-Tools) akzeptabel.

Netzwerkverkehr soll auf anomales Verhalten überwacht werden. Sicherheitsalarme sollen gemäss dem Vorfallmanagementprozess triage und eskaliert werden.

---

## Nachweise

Die folgenden Nachweise demonstrieren die Einhaltung dieser Richtlinie:

- **Netzwerkarchitekturdiagramm** (aktuell, mit Segmenten, Trust-Zonen, Gateways) — *bei Änderung aktualisiert; jährlich überprüft*
- **Firewall- und Gateway-Regelsätze** mit dokumentierter Änderungshistorie und jährlicher Überprüfungsabzeichnung — *Regeländerungen 3 Jahre aufbewahrt; jährliche Überprüfung mit ISB-Abzeichnung dokumentiert*
- **Netzwerkgeräteinventar und Konfigurationsstandards** — *innerhalb von 5 Arbeitstagen nach Änderung aktualisiert; jährlich geprüft*
- **Drahtlossicherheitskonfigurationsaufzeichnungen** (WPA3/WPA2-Enterprise) — *halbjährlich überprüft*
- **VPN-Zugriffsliste und vierteljährliche Überprüfungsaufzeichnungen** — *vierteljährlich überprüft; inaktive Konten deaktiviert*
- **Web-Filterkonfiguration und Ausnahmen-Protokolle** — *Ausnahmen vierteljährlich überprüft; Filterkategorien monatlich aktualisiert*
- **Netzwerküberwachungs- und IDS/IPS-Alarmberichte** — *mindestens 12 Monate aufbewahrt; kritische Alarme täglich überprüft*
- **Netzwerkzugangsüberprüfung und Geräte-Compliance-Aufzeichnungen** — *vierteljährlich für privilegierten Zugang; jährlich für Standard überprüft*
- **Patch-Compliance-Berichte** (Netzwerkgeräte gemäss CVSS-Zeitplan-Tabelle) — *monatlich überprüft*
- **Gastnetzwerk-Passwort-Rotationsaufzeichnungen** — *vierteljährliche Rotation dokumentiert*

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheitsmanagement-Team soll die Einhaltung dieser Richtlinie durch verschiedene Methoden verifizieren, einschliesslich, aber nicht beschränkt auf, Netzwerkkonfigurationsüberprüfungen, Penetrationstests, Schwachstellen-Scans, interne und externe Revisionen sowie Rückmeldungen an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll im Voraus vom Informationssicherheitsbeauftragten genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum. Ausnahmen sollen dem Management-Review-Team gemeldet werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Änderungen der Netzwerksicherheitsstandards, aufkommende Bedrohungen, regulatorische Änderungen sowie Lessons Learned aus Vorfällen berücksichtigen.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Netzwerksicherheitsrichtlinie — Zuordnung der ISO-27001-Massnahmen

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Abschnitt 5.1 Führung und Verpflichtung | 5.1 Richtlinien zur Informationssicherheit |
| Abschnitt 5.2 Richtlinie | 5.4 Managementverantwortlichkeiten |
| Abschnitt 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| Abschnitt 7.3 Bewusstsein | 6.3 Informationssicherheitsbewusstsein, -ausbildung und -schulung |
| | 6.4 Disziplinarverfahren |
| | **8.20 Netzwerksicherheit** |
| | **8.21 Sicherheit von Netzwerkdiensten** |
| | **8.22 Trennung von Netzwerken** |
| | 8.23 Web-Filterung |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen für den Datenschutz |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit; Anhang 1 — Angemessenheitsliste |
| EU-DSGVO (wo anwendbar) | Art. 32 — Sicherheit der Verarbeitung (Netzwerkkontrollen als angemessene Massnahme) |
| ISO/IEC 27001:2022 | Annex-A-Massnahmen 8.20, 8.21, 8.22 |
| ISO/IEC 27002:2022 | Abschnitte 8.20, 8.21, 8.22 — Implementierungsleitfaden |
| NIST SP 800-53 Rev 5 | SC-7 (Boundary Protection), SC-8 (Transmission Confidentiality) |
| CIS Controls v8 | Control 12 (Network Infrastructure Management), Control 13 (Network Monitoring and Defense) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
