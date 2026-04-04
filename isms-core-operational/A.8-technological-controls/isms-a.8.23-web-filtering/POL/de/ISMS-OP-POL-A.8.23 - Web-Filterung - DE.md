<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.23-DE:operational:OP-POL:a.8.23 -->
**ISMS-OP-POL-A.8.23 — Web-Filterung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Web-Filterung |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.23 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Initiale operative Richtlinie für ISO 27001:2022 |

**Prüfzyklus**: Jährlich
**Nächstes Prüfdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Massnahme A.8.23 — Web-Filterung

**Verwandte Annex-A-Massnahmen**:

| Massnahme | Bezug zur Web-Filterung |
|-----------|-------------------------|
| A.5.7 Bedrohungsintelligenz | Bedrohungsintelligenz-Feeds informieren die Sperrlisten und URL-Kategorisierung der Web-Filterung |
| A.5.10 Akzeptable Nutzung von Informationen | Die Richtlinie zur akzeptablen Nutzung definiert erlaubte und untersagte Webnutzung |
| A.8.7 Schutz vor Malware | Web-Filterung verhindert die Übertragung von Malware über Drive-by-Downloads und bösartige Websites |
| A.8.16 Überwachungsaktivitäten | Web-Filter-Protokolle fliessen in die Sicherheitsüberwachung und Anomalieerkennung ein |
| A.8.20 Netzwerksicherheit | Web-Filterung ist eine Sicherheitsmassnahme auf Netzwerkebene |
| A.8.21 Sicherheit von Netzwerkdiensten | Secure Web Gateway (SWG) ist ein verwalteter Netzwerksicherheitsdienst |
| A.8.22 Netzwerksegmentierung | Web-Filterung wird an Netzwerksegmentgrenzen durchgesetzt |
| A.8.24 Einsatz von Kryptographie | Überlegungen zur TLS-Inspektion bei verschlüsseltem Webverkehr |

**Verwandte interne Richtlinien**:

- Richtlinie zur akzeptablen Nutzung
- Netzwerksicherheitsrichtlinie
- Endgerätesicherheitsrichtlinie
- Richtlinie zu Überwachungsaktivitäten (A.8.16)
- Richtlinie zum Schutz vor Malware
- Datenschutz- und Schutz von Personendaten-Richtlinie

---

# Richtlinie zur Web-Filterung

## Zweck

Zweck dieser Richtlinie ist es, den Zugriff auf externe Websites zu steuern, um die Exposition gegenüber bösartigen Inhalten zu reduzieren, Datenlecks über Web-Kanäle zu verhindern und die Anforderungen an die akzeptable Nutzung durchzusetzen. Web-Filterung schützt die Systeme der Organisation vor Malware, die über Drive-by-Downloads, Phishing-Seiten und andere webbasierte Bedrohungen verbreitet wird.

Web-Filterung ist eine wichtige Massnahme, die im Rahmen der Informationssicherheits-Risikobeurteilung der Organisation identifiziert wurde. Die Entscheidungen zu Filterumfang und Kategorien in dieser Richtlinie basieren direkt auf dem Risikobehandlungsplan und adressieren folgende Risiken: Malware-Infektion durch webbasierte Bedrohungen, Diebstahl von Anmeldedaten durch Phishing, Datenlecks über nicht autorisierte Webdienste sowie Reputationsschäden durch den Zugriff auf unangemessene Inhalte.

Diese Richtlinie unterstützt das schweizerische nDSG Art. 8, indem Web-Filterung als technische Massnahme zum Schutz von Personendaten vor der Kompromittierung durch webbasierte Angriffsvektoren implementiert wird. Web-Filterung, die das Surfverhalten von Mitarbeitenden überwacht, muss das schweizerische Arbeitsrecht (OR Art. 328/328b) und das Verbot zur Verhaltensüberwachung (ArGV3 Art. 26) einhalten. Sofern die Organisation Daten von Personen im EU/EWR-Raum bearbeitet, gelten auch die Anforderungen der DSGVO Art. 32.

## Geltungsbereich

Diese Richtlinie gilt für:

- Den gesamten Webverkehr (HTTP/HTTPS), der von organisationsverwalteten Geräten und Netzwerken ausgeht.
- Alle Mitarbeitenden, Auftragnehmer und Drittnutzer, die über die Infrastruktur der Organisation auf das Internet zugreifen.
- Alle Umgebungen: Unternehmensnetzwerk, Remote-Mitarbeitende (über VPN oder Cloud-Proxy) und Gastnetzwerke (eingeschränkter Umfang).
- Alle Web-Zugriffsmethoden: Browser, Anwendungen mit HTTP/HTTPS-Aufrufen und API-Verbindungen zu externen Diensten.

Nicht im Geltungsbereich:
- E-Mail-Filterung (geregelt durch Endgerätesicherheits- und Malware-Schutzrichtlinien).
- Anwendungsebenen-Massnahmen für spezifische SaaS-Plattformen (geregelt durch die Cloud-Dienste-Richtlinie, A.5.19-23).

## Grundsatz

Der Zugriff auf externe Websites soll so gesteuert werden, dass die Exposition gegenüber bösartigen Inhalten reduziert wird. Web-Filterung soll nach einem risikobasierten Ansatz erfolgen: bekannte Bedrohungen automatisch sperren, diskretionäre Kategorien richtlinienbasiert einschränken und legitimen geschäftlichen Zugriff ohne unnötige Reibung ermöglichen. Die Filterung soll unabhängig vom Standort oder Gerät des Nutzers einheitlich angewendet werden.

---

## Web-Filterarchitektur

### Filteransatz

Die Organisation soll Web-Filterung unter Einsatz einer oder mehrerer der folgenden Technologien implementieren:

| Ebene | Technologie | Zweck |
|-------|-------------|-------|
| **DNS-Filterung** | DNS-Filterungsdienst (z. B. Cisco Umbrella, Cloudflare Gateway, DNSFilter oder gleichwertig) | Erste Verteidigungslinie; sperrt die Auflösung bösartiger und untersagter Domains, bevor eine Verbindung hergestellt wird |
| **URL-Filterung** | Secure Web Gateway (SWG) oder Proxy mit URL-Kategorisierungsdatenbank | Prüft den vollständigen URL-Pfad; setzt kategoriebasierte Richtlinien durch; ermöglicht granulare Steuerung |
| **TLS-Inspektion** | SWG oder Proxy mit SSL/TLS-Entschlüsselung und -Inspektion | Prüft verschlüsselten Webverkehr auf in HTTPS verborgene Bedrohungen (gilt für ausgewählte Kategorien — siehe Abschnitt TLS-Inspektion) |
| **Browser-Isolation** (optional) | Remote Browser Isolation (RBI) für risikoreiche oder unkategorisierte Websites | Rendert Webinhalte in einer Cloud-Sandbox; nur sichere visuelle Ausgabe wird an den Nutzer gestreamt |

### Einsatzmodell

| Umgebung | Filtermethode |
|----------|--------------|
| **Unternehmensnetzwerk** | SWG/Proxy oder DNS-Filterung am Netzwerkperimeter durchgesetzt |
| **Remote-Mitarbeitende** | Cloud-basierter SWG oder DNS-Filterungs-Agent auf verwalteten Endgeräten; einheitliche Richtlinie unabhängig vom Netzwerk |
| **BYOD-Geräte** | DNS-Filterung (leichtgewichtig, datenschutzgerecht); TLS-Inspektion soll **nicht** auf persönlichen Geräten durchgeführt werden |
| **Gastnetzwerk** | DNS-Filterung nur für Malware-/Phishing-Kategorien; Filterung diskretionärer Kategorien wird nicht angewendet |

DNS-Filterung soll auf allen verwalteten Geräten als Basisschutz durchgesetzt werden. Direkte DNS-Anfragen an externe Resolver (einschliesslich DNS over HTTPS (DoH) und DNS over TLS (DoT) an nicht genehmigte Resolver) sollen am Firewall gesperrt werden, um eine Umgehung der Filterung zu verhindern.

### Verfügbarkeit und Leistung (SOC 2: A1.1)

Die Web-Filterplattform soll folgende Service Level Objectives einhalten:

| SLO | Zielwert | Messung |
|-----|----------|---------|
| **Verfügbarkeit** | ≥99,9 % Betriebszeit (monatlich gemessen) | Plattform-Monitoring-Dashboard |
| **Latenz** | ≤50 ms zusätzliche Latenz pro Web-Anfrage (p95) | Regelmässige Leistungstests |
| **Failover** | Automatischer Failover auf sekundären Filterpfad oder Fail-Open innerhalb von 5 Minuten | Jährlicher Failover-Test |
| **Kapazität** | Plattform ausgelegt für Spitzenlast + 30 % Reserve | Vierteljährliche Kapazitätsprüfung |

Wenn die Filterplattform eine anhaltende Verschlechterung über den SLO-Grenzwerten aufweist, soll IT Operations das dokumentierte Incident-Response-Verfahren einleiten. Fail-Open (Zulassen von ungefiltertem Verkehr) ist nur als vorübergehende Massnahme bei einem Plattformausfall zulässig und soll protokolliert, dem ISB gemeldet und innerhalb von 4 Stunden behoben werden.

### Änderungsmanagement für Filterregeln (SOC 2: CC8.1)

Änderungen an der Web-Filter-Konfiguration (Kategorienrichtlinien, Sperr-/Zulasslisten, TLS-Inspektionseinstellungen, Einsatzarchitektur) sollen dem Änderungsmanagementprozess der Organisation folgen:

1. **Anfrage**: Änderungsantrag mit Begründung, Umfang und Risikobeurteilung einreichen.
2. **Prüfung**: IT-Sicherheit prüft die Änderung auf Sicherheitsimplikationen; der Datenschutzberater prüft die Datenschutzauswirkungen, wenn die Mitarbeiterüberwachung betroffen ist.
3. **Test**: Änderungen werden nach Möglichkeit in einer Staging-Umgebung oder bei eingeschränktem Rollout getestet.
4. **Genehmigung**: Standardänderungen werden vom IT-Sicherheitsleiter genehmigt; wesentliche Änderungen (neue Kategoriesperren, Änderungen des TLS-Inspektionsumfangs) werden vom ISB genehmigt.
5. **Umsetzung**: Änderung wird von IT Operations im genehmigten Wartungsfenster ausgerollt.
6. **Verifizierung**: Nachimplementierungsprüfung, ob die Änderung wie beabsichtigt funktioniert.
7. **Dokumentation**: Änderung wird im Änderungsprotokoll mit Konfigurationszuständen vor und nach der Änderung erfasst.

Notfalländerungen (z. B. Sperrung einer aktiven Phishing-Kampagne) können die Standardgenehmigung umgehen, müssen jedoch innerhalb von 24 Stunden nachträglich dokumentiert werden.

### Lieferantenmanagement (SOC 2: CC9.2)

Wenn Web-Filterung von einem Drittanbieterdienst (Cloud-SWG, DNS-Filteranbieter) erbracht wird:

- Der Lieferant soll in das Lieferantenrisikomanagementprogramm der Organisation aufgenommen werden.
- SOC-2-Typ-II-Bericht oder ISO-27001-Zertifizierung soll jährlich geprüft werden.
- SLA-Konformität (Verfügbarkeit, Latenz, Bedrohungserkennungsrate, Support-Reaktionszeit) soll anhand vertraglicher Schwellenwerte überwacht werden.
- Datenverarbeitungsverträge sollen Folgendes abdecken: Umgang mit Surfverhaltensdaten von Mitarbeitenden, Datenhaltungsort, Aufbewahrungsfristen und Benachrichtigung bei Vorfällen.
- Das Risiko einer Anbieterabhängigkeit soll bewertet werden; die Organisation soll in der Lage sein, innerhalb eines angemessenen Zeitrahmens zu einem alternativen Anbieter zu wechseln.

---

## URL-Kategorisierung und Filterregeln

### Pflichtmässige Sperrung — Sicherheitsbedrohungskategorien

Die folgenden Kategorien sollen für alle Nutzer ausnahmslos gesperrt werden:

| # | Kategorie | Begründung |
|---|-----------|-----------|
| 1 | **Malware-Verbreitung** | Websites, die aktiv Malware, Exploit-Kits oder Drive-by-Downloads hosten oder verbreiten |
| 2 | **Phishing und Betrug** | Websites, die darauf ausgelegt sind, Anmeldedaten, Finanzinformationen oder Personendaten abzufangen |
| 3 | **Command and Control (C2)** | Bekannte Botnetz- und APT-Infrastruktur |
| 4 | **Ransomware** | Websites zur Ransomware-Verbreitung, Zahlung und Kommunikation |
| 5 | **Spyware und Adware** | Websites, die unerwünschte Software oder Tracking-Tools verbreiten |
| 6 | **Krypto-Mining** | Websites, auf denen nicht autorisierte Kryptowährungs-Mining-Skripte ausgeführt werden |
| 7 | **Exploit-Kits** | Websites, die Browser- und Plugin-Exploitierungs-Frameworks hosten |
| 8 | **Dynamisches DNS (bösartig)** | Häufig für bösartige Infrastruktur eingesetzt; bekannte bösartige Dynamic-DNS-Anbieter sperren |
| 9 | **Illegale Inhalte** | Inhalte, die nach schweizerischem oder anwendbarem Recht verboten sind |
| 10 | **Kindesmissbrauchsmaterial** | Gesetzliche Pflicht zur Sperrung |

### Pflichtmässige Sperrung — Richtlinienkategorien

Die folgenden Kategorien sollen gesperrt werden, sofern keine genehmigte Ausnahme vorliegt:

| # | Kategorie | Begründung |
|---|-----------|-----------|
| 11 | **Proxy-Umgehung und Anonymisierer** | Web-Proxys, VPN-Dienste und Tor-Knoten zur Umgehung von Filterkontrollen |
| 12 | **Hacking-Tools und -Ressourcen** | Exploit-Datenbanken, Hacking-Anleitungen und Verbreitung von Angriffswerkzeugen (Ausnahme: Sicherheitsteam mit dokumentierter Begründung) |
| 13 | **Peer-to-Peer-Filesharing** | Datenleck-Risiko und Malware-Vektor |
| 14 | **Urheberrechtsverletzung / Piraterie** | Risiken für geistiges Eigentum und rechtliche Risiken |

### Diskretionäre Einschränkung — Überwachte Kategorien

Die folgenden Kategorien können je nach Organisationsrichtlinie eingeschränkt, überwacht oder erlaubt werden:

| # | Kategorie | Standardrichtlinie | Hinweise |
|---|-----------|-------------------|----------|
| 15 | **Persönlicher Cloud-Speicher** (Dropbox, Google Drive persönlich usw.) | Einschränken | Datenleck-Risiko; unternehmenseigener Cloud-Speicher erlaubt |
| 16 | **Persönliches Webmail** (Gmail, Outlook persönlich usw.) | Einschränken | Datenleck-Risiko; Unternehmens-E-Mail erlaubt |
| 17 | **Soziale Medien** | Erlaubt mit Überwachung | Geschäftliche Nutzung vorhanden; Uploads nach Möglichkeit einschränken |
| 18 | **Streaming-Medien / Video** | Erlaubt mit Bandbreitenlimits | Bandbreitenmanagement; bei Bedarf in Spitzenzeiten einschränken |
| 19 | **Gaming** | Während der Geschäftszeiten sperren | Produktivität; ausserhalb der Arbeitszeit nach Wunsch erlaubt |
| 20 | **Erwachseneninhalt** | Sperren | Angemessenheit am Arbeitsplatz |
| 21 | **Glücksspiel** | Sperren | Angemessenheit am Arbeitsplatz und rechtliche Risiken |

### Erlaubt — Geschäftskritische Kategorien

Die folgenden Kategorien sollen nicht gefiltert oder eingeschränkt werden:

| Kategorie | Beispiele |
|-----------|----------|
| **Geschäft und Finanzen** | Banken, Branchenportale, Beratungsdienstleistungen |
| **Behörden und Recht** | Regulierungsbehörden, Behördenportale, juristische Datenbanken |
| **Technologie und IT** | Software-Anbieter, Dokumentation, Entwicklerressourcen |
| **Bildung und Schulung** | E-Learning-Plattformen, berufliche Weiterentwicklung, akademische Ressourcen |
| **Nachrichten und Medien** | Grosse Nachrichtenportale, Branchenpublikationen |
| **Suchmaschinen** | Google, Bing, DuckDuckGo |
| **Unternehmens-SaaS-Anwendungen** | Genehmigte Cloud-Anwendungen gemäss dem SaaS-Register der Organisation |

### Unkategorisierte Websites

Websites, die von der Filterlösung nicht kategorisiert werden, sollen wie folgt behandelt werden:

- **Standard**: Erlaubt mit Protokollierung (für Organisationen mit niedrigerer Risikobereitschaft: Einschränkung mit Nutzer-Override-Option).
- Alle Zugriffe auf unkategorisierte Websites sollen für die Sicherheitsprüfung protokolliert werden.
- Wenn Browser-Isolation eingesetzt wird, sollten unkategorisierte Websites standardmässig über die Isolation gerendert werden.

---

## TLS-Inspektion

### Zweck

Ungefähr 80 % des Webverkehrs ist verschlüsselt (HTTPS). Ohne TLS-Inspektion können im verschlüsselten Verkehr verborgene Bedrohungen von der Web-Filterlösung nicht erkannt werden. TLS-Inspektion entschlüsselt, prüft und re-verschlüsselt HTTPS-Verkehr am SWG/Proxy.

### Anforderungen

| Anforderung | Spezifikation |
|-------------|---------------|
| **Einsatz** | TLS-Inspektion soll am SWG/Proxy für Verkehr von organisationsverwalteten Geräten aktiviert werden |
| **Zertifikat** | Ein privates Root-CA-Zertifikat soll über MDM, Gruppenrichtlinie oder gleichwertige Methoden auf allen verwalteten Endgeräten ausgerollt werden |
| **Firefox** | Firefox verwendet einen eigenen Zertifikats-Store; das private Root-CA-Zertifikat soll separat über die Firefox-Enterprise-Richtlinie ausgerollt werden |
| **Leistung** | SWG/Proxy soll für die TLS-Inspektionslast ausgelegt sein; QUIC-Protokoll (UDP 443) soll gesperrt werden, um TCP-basierte HTTPS-Inspektion zu erzwingen |

### Datenschutzausnahmen — Kategorien, die von der TLS-Inspektion ausgenommen werden

Die folgenden Kategorien sollen zum Schutz der Privatsphäre und zur Vermeidung technischer Probleme von der TLS-Inspektion **ausgenommen** werden:

| # | Kategorie | Begründung |
|---|-----------|-----------|
| 1 | **Finanzen / Banking** | Empfindlichkeit von Anmeldedaten; regulatorische Überlegungen |
| 2 | **Gesundheitswesen** | Datenschutz bei Gesundheitsdaten (nDSG besonders schützenswerte Personendaten) |
| 3 | **Behördenportale** | Regulatorische Sensibilität |
| 4 | **Zertifikats-gepinnte Anwendungen** | Technische Inkompatibilität (z. B. bestimmte APIs, Finanzanwendungen) |
| 5 | **Persönliche Geräte (BYOD)** | Keine Rechtsgrundlage für TLS-Inspektion auf persönlichen Geräten |

### Gesetzliche Anforderungen für die TLS-Inspektion

- Mitarbeitende sollen im Voraus darüber informiert werden, dass verschlüsselter Webverkehr zu Sicherheitszwecken entschlüsselt und geprüft werden kann.
- Die Richtlinie zur akzeptablen Nutzung soll die TLS-Inspektion und ihren Zweck dokumentieren.
- Daten aus der TLS-Inspektion sollen nur zu Sicherheitszwecken verarbeitet werden (Malware-Erkennung, Prävention von Datenlecks, Richtliniendurchsetzung) — nicht zur Verhaltensüberwachung.
- BYOD- und Gastnetzwerkverkehr soll **nicht** der TLS-Inspektion unterzogen werden.

---

## Integration von Bedrohungsintelligenz

### Aktualisierung der Sperrlisten

Sperrlisten der Web-Filterung sollen mit Bedrohungsintelligenz aus mehreren Quellen aktualisiert werden:

| Quellentyp | Beispiele | Aktualisierungsfrequenz |
|------------|----------|------------------------|
| **Vom Anbieter bereitgestellt** | URL-Kategorisierungsdatenbank des Filterungsanbieters | Echtzeit oder täglich (automatisch) |
| **Bedrohungsintelligenz-Feeds** | Brachen-ISACs, staatliche Cyber-Behörden (NCSC.ch, MELANI), kommerzielle Bedrohungs-Feeds | Automatisch sofern unterstützt; manuelle wöchentliche Überprüfung |
| **Interne Intelligenz** | IOCs aus Incident-Untersuchungen, Phishing-Meldungen von Mitarbeitenden, Sicherheitsteam-Recherche | Ad hoc; innerhalb von 4 Stunden nach Identifikation hinzugefügt |
| **Community-Feeds** | Open-Source-Bedrohungsintelligenz (MISP, abuse.ch, PhishTank, URLhaus) | Automatisch sofern unterstützt |

### Phishing und Social Engineering

- Von Mitarbeitenden gemeldete Phishing-URLs sollen innerhalb von **4 Stunden** während der Geschäftszeiten bewertet und der Sperrliste hinzugefügt werden.
- Phishing-Simulations-URLs sollen während Testkampagnen von der Web-Filterung ausgenommen werden (koordiniert zwischen Informationssicherheit und IT Operations).

### Integration der Incident Response

Web-Filter-Ereignisse sollen mit dem Incident-Management-Prozess der Organisation (A.5.24-28) integriert werden. Die folgenden Schwellenwerte sollen die Erstellung eines Incidents auslösen:

| Auslöser | Schweregrad | Massnahme |
|----------|-------------|-----------|
| Nutzer greift auf bestätigte Malware-/C2-Website zu (Filterung umgangen oder ausgefallen) | Kritisch | Sofortiger Incident; Endgerät isolieren; forensische Untersuchung |
| Mehrere Nutzer werden innerhalb von 1 Stunde von derselben Phishing-URL gesperrt | Hoch | Potenzielle Phishing-Kampagne untersuchen; prüfen, ob Nutzer vor der Sperrung auf die URL zugegriffen haben |
| Einzelner Nutzer versucht wiederholt, auf gesperrte Kategorien zuzugreifen (>20 Versuche/Tag) | Mittel | Auf Richtlinienverstoss oder kompromittiertes Konto untersuchen |
| Umgehung der Filterplattform erkannt (DoH/Proxy-Evasion erfolgreich) | Hoch | Evasionsvektor sperren; Umfang untersuchen; Richtliniendurchsetzungslücken bewerten |
| Plötzlicher Anstieg gesperrter Anfragen (>200 % des Ausgangswerts) | Mittel | Auf Malware-Kampagne, kompromittierte Infrastruktur oder Fehlkonfiguration prüfen |

---

## Ausnahme- und Override-Prozess

### Beantragung des Zugriffs auf gesperrte Websites

Wenn ein Nutzer auf eine gesperrte Website stösst, die für legitime Geschäftszwecke erforderlich ist:

1. **Sperrseite**: Der Nutzer sieht eine Sperrseite mit dem Sperrgrund und einem Link zur Beantragung des Zugriffs.
2. **Antrag**: Nutzer stellt einen Ausnahmeantrag über [Ticketsystem / Self-Service-Portal] mit:
   - Angeforderter URL oder Domain.
   - Geschäftliche Begründung.
   - Benötigte Dauer (temporär oder dauerhaft).
   - Abteilung und Projektkontext.
3. **Prüfung**: Der Antrag wird geprüft von:
   - **Direktvorgesetzter**: Bestätigt die Geschäftsbegründung (innerhalb von 1 Werktag).
   - **IT-Sicherheit**: Bewertet das Sicherheitsrisiko (innerhalb von 1 Werktag).
4. **Entscheidung**:
   - **Genehmigt**: URL/Domain wird zur Zulassliste hinzugefügt (zeitlich befristete Genehmigung bevorzugt; Standard: 90 Tage).
   - **Abgelehnt**: Nutzer wird mit Begründung informiert; alternative Lösung wird nach Möglichkeit vorgeschlagen.
   - **Eskaliert**: Overrides für risikoreiche Kategorien (Proxy-Umgehung, Hacking-Tools) erfordern die Genehmigung des ISB.
5. **Umsetzung**: IT Operations fügt die genehmigte Ausnahme innerhalb von 4 Stunden nach Genehmigung zur Filterlösung hinzu.
6. **Dokumentation**: Ausnahme wird im Ausnahmenregister mit Antragsteller, Begründung, Genehmiger, Ablaufdatum und Prüfdatum erfasst.

### Ausnahmenregister

| Feld | Beschreibung |
|------|-------------|
| Ausnahme-ID | Eindeutige Kennung |
| URL/Domain | Was erlaubt ist |
| Antragsteller | Name, Abteilung |
| Geschäftliche Begründung | Warum Zugriff erforderlich ist |
| Risikobeurteilung | Ergebnis der Sicherheitsrisikobeurteilung |
| Genehmiger | Name und Datum |
| Ablaufdatum | Standard: 90 Tage (temporär) oder jährliche Überprüfung (dauerhaft) |
| Prüfdatum | Wann die Ausnahme als nächstes überprüft wird |
| Kompensierende Massnahmen | Etwaige zusätzliche Massnahmen (z. B. Überwachung, Protokollierung) |

### Ausnahmen-Governance

- Alle Ausnahmen sollen **vierteljährlich** von der IT-Sicherheit überprüft werden.
- Abgelaufene Ausnahmen sollen automatisch widerrufen werden.
- Nicht genutzte Ausnahmen (kein Zugriff in 90 Tagen verzeichnet) sollen entfernt werden.
- Die Gesamtzahl der aktiven Ausnahmen soll dem ISB vierteljährlich gemeldet werden.
- Ausnahmen sollen den minimal notwendigen Umfang haben: spezifische URL gegenüber vollständiger Domain bevorzugt; Domain gegenüber gesamter Kategorie bevorzugt.

---

## Remote-Mitarbeitende und BYOD

### Remote-Mitarbeitende (verwaltete Geräte)

- Ein Cloud-basierter SWG oder DNS-Filterungs-Agent soll auf allen verwalteten Endgeräten installiert sein.
- Web-Filterrichtlinien sollen einheitlich gelten, unabhängig davon, ob der Nutzer sich im Unternehmensnetzwerk, im heimischen WLAN, über einen mobilen Hotspot oder in einem öffentlichen Netzwerk befindet.
- Split Tunneling (VPN) soll die Web-Filterung nicht umgehen; Webverkehr soll unabhängig von der VPN-Konfiguration durch die Filterlösung geleitet werden.

### BYOD (Persönliche Geräte)

- DNS-Filterung ist der minimale Basisschutz für BYOD-Geräte, die auf Unternehmensressourcen zugreifen.
- TLS-Inspektion soll auf persönlichen Geräten **nicht** durchgeführt werden (Datenschutz- und rechtliche Einschränkungen).
- Ein verwalteter Browser oder ein sicherer Workspace-Container (z. B. Microsoft Edge for Business, VMware Workspace ONE) sollte für BYOD-Zugriff auf unternehmenseigene Web-Anwendungen in Betracht gezogen werden.
- Für BYOD gelten im Vergleich zu unternehmenseigenen Geräten separate, weniger einschneidende Filterrichtlinien.

---

## Mitarbeiterdatenschutz und Web-Filterung

### Gesetzliche Anforderungen

Web-Filterung, die Surfverhaltensdaten von Mitarbeitenden verarbeitet, soll das schweizerische Arbeitsrecht einhalten:

- **ArGV3 Art. 26**: Web-Filtersysteme sollen nicht primär zur Überwachung des Mitarbeiterverhaltens eingesetzt werden. Ihr Zweck ist die Sicherheit (Malware-Prävention, Prävention von Datenlecks, Richtliniendurchsetzung).
- **OR Art. 328b**: Die Verarbeitung von Web-Surfverhaltensdaten der Mitarbeitenden soll verhältnismässig und auf Sicherheitszwecke beschränkt sein.
- **nDSG**: Rechtmässigkeit, Verhältnismässigkeit, Zweckbindung und Transparenz gelten für alle Web-Surfverhaltensdaten.

### Datenschutzmassnahmen

- **Transparenz**: Mitarbeitende sollen darüber informiert werden, dass Web-Filterung vorhanden ist, welche Kategorien gefiltert werden und dass der Zugriff auf gesperrte Websites protokolliert wird. Diese Informationen sollen in die Richtlinie zur akzeptablen Nutzung und in die Beschäftigungsunterlagen aufgenommen werden.
- **Standardmässig nicht-personalisierte Überwachung**: Web-Filter-Protokolle sollen aggregiert für die Sicherheitsüberwachung überprüft werden (z. B. Gesamtzahl gesperrter Anfragen nach Kategorie, häufigste gesperrte Domains). Das individuelle Surfverhalten einzelner Nutzer soll nicht überprüft werden, es sei denn:
  - (a) ein Sicherheitsalarm deutet auf einen potenziellen Incident oder eine Richtlinienverletzung hin, und
  - (b) die Untersuchung ist mit Begründung dokumentiert.
- **Zweckbindung**: Web-Filter-Daten sollen nicht für die HR-Leistungsbewertung, Disziplinarmassnahmen in nicht sicherheitsrelevanten Angelegenheiten oder allgemeine Verhaltensprofilierung verwendet werden.
- **Datensparsamkeit**: Web-Filter-Protokolle sollen nur so lange aufbewahrt werden, wie es für Sicherheitszwecke erforderlich ist (gemäss Protokollaufbewahrungsplan in der Protokollierungsrichtlinie, A.8.15).
- **DSFA**: Wenn die Web-Filterung TLS-Inspektion oder detaillierte nutzerbezogene Protokollierung in grossem Umfang umfasst, kann eine Datenschutz-Folgenabschätzung gemäss nDSG Art. 22 erforderlich sein.

---

## Schulung und Sensibilisierung

- Alle Mitarbeitenden sollen geschult werden zu:
  - Der Web-Filterungsrichtlinie der Organisation und der akzeptablen Webnutzung.
  - Wie Browser-Sicherheitswarnungen erkannt werden (Zertifikatsfehler, Phishing-Indikatoren).
  - Wie verdächtige bösartige Websites der Informationssicherheit gemeldet werden.
  - Dem Ausnahme-Antragsverfahren für den Zugriff auf gesperrte Websites.
- Die Schulung soll in das jährliche Informationssicherheits-Sensibilisierungsprogramm einbezogen werden.
- Systemadministratoren, die für die Web-Filter-Wartung zuständig sind, sollen plattformspezifische Schulungen erhalten.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; Genehmigung von Kategorienfilterungsentscheidungen; Genehmigung risikoreicher Ausnahmen; Aufsicht über die Wirksamkeit der Web-Filterung |
| **IT Operations / Netzwerkteam** | Einsatz, Konfiguration und Wartung der Web-Filterplattform; Ausnahmenimplementierung; Kapazitätsmanagement; TLS-Inspektionszertifikatsverwaltung |
| **Informationssicherheit** | Integration von Bedrohungsintelligenz; Aktualisierung der Sperrlisten; Risikobeurteilung für Ausnahmen; vierteljährliche Ausnahmenüberprüfung; Analyse von Web-Filter-Protokollen |
| **Direktvorgesetzte** | Prüfung der Geschäftsbegründung für Ausnahmeanträge |
| **Alle Mitarbeitenden** | Einhaltung der Web-Filterungsrichtlinie; Meldung verdächtiger bösartiger Websites; Nutzung des Ausnahme-Antragsverfahrens für legitime Geschäftsbedürfnisse |
| **Datenschutzberater** | DSFA-Bewertung für TLS-Inspektion; Beratung zu Datenschutzmassnahmen für Mitarbeitende |

### Prüfung des administrativen Zugriffs (SOC 2: CC6.1)

Der administrative Zugriff auf die Web-Filterplattform soll:

- Auf IT-Operations- und Informationssicherheitspersonal mit dokumentiertem Bedarf beschränkt sein.
- Vierteljährlich überprüft werden, um sicherzustellen, dass nur autorisiertes Personal Zugriff behält.
- Mit MFA und Privileged-Access-Management-Massnahmen geschützt sein.
- Protokolliert werden — alle administrativen Aktionen (Regeländerungen, Konfigurationsmodifikationen, Ausnahmenhinzufügungen) sollen auditierbar sein.
- Innerhalb von 24 Stunden widerrufen werden, wenn Personen die Rolle wechseln oder die Organisation verlassen.

---

## Nachweise

Die folgenden Nachweise belegen die Konformität mit dieser Richtlinie:

| # | Nachweis | Verantwortlicher | Häufigkeit |
|---|----------|-----------------|------------|
| 1 | **Konfiguration der Web-Filterplattform** (gesperrte/erlaubte Kategorien, TLS-Inspektionseinstellungen, DNS-Filterkonfiguration) | IT Operations | *Dokumentiert; halbjährlich und nach Richtlinienänderungen überprüft* |
| 2 | **Aufzeichnungen zur Aktualisierung der Sperrlisten** (Bedrohungsintelligenz-Quellen, Aktualisierungsfrequenz, manuelle Ergänzungen aus Incident-Untersuchungen) | Informationssicherheit | *Kontinuierliche automatische Updates; manuelle Ergänzungen mit Datum und Quelle protokolliert* |
| 3 | **Ausnahmenregister** (aktive Ausnahmen mit Begründung, Genehmiger, Ablauf und Prüfdatum) | Informationssicherheit | *Kontinuierlich gepflegt; vierteljährlich überprüft; Gesamtanzahl dem ISB vierteljährlich gemeldet* |
| 4 | **Zusammenfassung der Web-Filter-Protokolle** (aggregierte Statistiken: Gesamtanfragen, gesperrte Anfragen nach Kategorie, häufigste gesperrte Domains) | Informationssicherheit | *Monatliche Zusammenfassung; 12 Monate aufbewahrt* |
| 5 | **Datenschutzausschlussliste der TLS-Inspektion** (von der Inspektion ausgenommene Kategorien) | IT Operations | *Dokumentiert; jährlich überprüft* |
| 6 | **Mitarbeiterbenachrichtigungsunterlagen** (Bestätigung der Richtlinie zur akzeptablen Nutzung einschliesslich Web-Filter-Offenlegung) | HR / Informationssicherheit | *Bei Richtlinienänderungen aktualisiert; Bestätigung jährlich erfasst* |
| 7 | **Filterabdeckung für Remote-Mitarbeitende** (Prozentsatz verwalteter Remote-Endgeräte mit aktivem Filtering-Agent) | IT Operations | *Vierteljährlich; Ziel: 100 % der verwalteten Remote-Geräte* |
| 8 | **DSFA-Unterlagen** (sofern TLS-Inspektion oder detaillierte nutzerbezogene Protokollierung implementiert ist) | Datenschutzberater | *Vor Einsatz abgeschlossen; jährlich überprüft* |
| 9 | **SLO-Berichte der Filterplattform** — Verfügbarkeits-, Latenz- und Incident-Lösungsmetriken (SOC 2: A1.1) | IT Operations | *Monatlich; 12 Monate aufbewahrt* |
| 10 | **Aufzeichnungen zu Filterregeländerungen** — Änderungsanträge, Risikobeurteilungen, Genehmigungen, Umsetzungsdaten (SOC 2: CC8.1) | IT Operations / Informationssicherheit | *Pro Änderung; 12 Monate aufbewahrt* |
| 11 | **Lieferantenrisikobeurteilungsunterlagen** — Bewertungen von Drittanbieter-SWG/DNS-Anbietern, SLA-Konformität, SOC-2/ISO-27001-Berichte (SOC 2: CC9.2) | Informationssicherheit / Beschaffung | *Jährlich; aktiver Vertrag + 2 Jahre aufbewahrt* |
| 12 | **Aufzeichnungen zur Prüfung des administrativen Zugriffs** — Admin-Zugriffsliste der Filterplattform, Prüfergebnisse, Zugriffsmodifikationen (SOC 2: CC6.1) | IT Operations / Informationssicherheit | *Vierteljährlich; 12 Monate aufbewahrt* |
| 13 | **Testergebnisse zur Filterwirksamkeit** — Test-URLs, Ergebnisse der Bypass-Versuche, Erkennungsraten (SOC 2: CC4.1) | Informationssicherheit | *Halbjährlich; 12 Monate aufbewahrt* |
| 14 | **Management-Berichterstattung** — monatliche Kennzahlenzusammenfassung, vierteljährliche Trendanalyse, jährliche Wirksamkeitsprüfung (SOC 2: CC4.2) | ISB / Informationssicherheit | *Monatlich/vierteljährlich/jährlich wie angegeben* |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheits-Management-Team überprüft die Einhaltung dieser Richtlinie durch Konfigurationsprüfungen der Web-Filterung, Audits des Ausnahmenregisters, Analyse der Sperrraten, Überprüfung der Remote-Gerätabdeckung sowie interne und externe Audits, und gibt Feedback an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll gemäss dem oben definierten Ausnahme- und Override-Prozess genehmigt und erfasst werden. Ausnahmen von der gesamten Web-Filterungsrichtlinie (z. B. Systeme, die nicht gefiltert werden können) sollen vom ISB mit dokumentierter Risikoakzeptanz und kompensierenden Massnahmen genehmigt werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstösst — einschliesslich des Versuchs, Web-Filterkontrollen zu umgehen (z. B. durch Nutzung eines persönlichen VPN, Proxy-Umgehungstools oder nicht autorisierter DNS-Resolver) — kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung des Arbeitsverhältnisses.

## Tests und Validierung (SOC 2: CC4.1)

Die Wirksamkeit der Web-Filterkontrollen soll regelmässig getestet werden:

| Test | Häufigkeit | Methode | Verantwortlicher |
|------|-----------|---------|-----------------|
| **Sperrverifizierung** | Monatlich | Zugriffsversuch auf bekannte gesperrte URLs von Testkonten; Verifizierung der korrekten Anzeige der Sperrseite | Informationssicherheit |
| **Bypass-Tests** | Halbjährlich | Versuche, die Filterung mit üblichen Evasionstechniken zu umgehen (DoH an nicht genehmigte Resolver, VPN, Proxy) | Informationssicherheit |
| **Malware-Erkennungsrate** | Vierteljährlich | Bekannte bösartige URLs (aus Test-Feeds) durch die Filterlösung einreichen; Erkennungsrate messen | Informationssicherheit |
| **TLS-Inspektionsverifizierung** | Vierteljährlich | Sicherstellen, dass TLS-Inspektion für den erwarteten Verkehr aktiv ist; Korrektheit der Datenschutzausnahmen bestätigen | IT Operations |
| **Remote-Mitarbeitende-Abdeckung** | Vierteljährlich | Sicherstellen, dass Filtering-Agent auf einer Stichprobe verwalteter Remote-Endgeräte aktiv ist | IT Operations |

Testergebnisse sollen dokumentiert und Massnahmen zur Behebung identifizierter Schwachstellen nachverfolgt werden.

## Kennzahlen und Management-Berichterstattung (SOC 2: CC4.2)

Folgende Kennzahlen sollen berichtet werden:

| Kennzahl | Zielwert | Berichterstattung |
|----------|----------|-------------------|
| Verfügbarkeit der Filterplattform | ≥99,9 % Betriebszeit | Monatlich an IT Operations |
| Malware-/Phishing-Sperrrate | ≥99 % bekannter Bedrohungen gesperrt | Vierteljährlich an ISB |
| Bearbeitungszeit für Ausnahmeanträge | ≤2 Werktage von Antrag bis Entscheidung | Monatlich an ISB |
| Anzahl aktiver Ausnahmen | Abnehmend oder stabil | Vierteljährlich an ISB |
| Filterabdeckung für Remote-Mitarbeitende | 100 % der verwalteten Remote-Endgeräte | Vierteljährlich an ISB |
| Verarbeitung von Mitarbeiter-gemeldeten Phishing-URLs | Innerhalb 4-Stunden-SLA | Monatlich an Informationssicherheit |

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Veränderungen in der Web-Bedrohungslandschaft, Fähigkeiten der Filtertechnologie, regulatorische Anforderungen, Mitarbeiter-Feedback zu gesperrtem legitimem Zugriff sowie False-Positive-/False-Negative-Raten berücksichtigen.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Richtlinie zur Web-Filterung — Zuordnung zu ISO-27001-Massnahmen

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Abschnitt 5.1 Führung und Verpflichtung | 5.1 Leitlinien für Informationssicherheit |
| Abschnitt 5.2 Richtlinie | 5.4 Managementverantwortung |
| Abschnitt 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Normen |
| | 5.37 Dokumentierte Betriebsverfahren |
| | 6.3 Bewusstsein, Schulung und Training zur Informationssicherheit |
| | 6.4 Disziplinarverfahren |
| | **8.23 Web-Filterung** |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmenwerk | Relevanz |
|------------|---------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen; Art. 6 — Verhältnismässigkeit |
| Schweizerisches OR (Obligationenrecht) | Art. 328b — Einschränkungen der Mitarbeiterdatenverarbeitung |
| Schweizerische ArGV3 (Verordnung 3 zum Arbeitsgesetz) | Art. 26 — Verbot zur Verhaltensüberwachung |
| EU DSGVO (sofern anwendbar) | Art. 32 — Sicherheit der Verarbeitung |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.23 |
| ISO/IEC 27002:2022 | Abschnitt 8.23 — Implementierungsleitfaden |
| NIST SP 800-53 Rev 5 | AC-4 (Informationsfluss-Durchsetzung), SC-7 (Grenzschutz), SC-7(8) (Verkehr über Proxy leiten), SI-3 (Schutz vor bösartigem Code) |
| NIST CSF 2.0 | PR.DS (Datensicherheit), PR.IR (Infrastrukturresilienz), DE.CM (Kontinuierliche Überwachung) |
| CIS Controls v8 | Massnahme 9.2 (DNS-Filterdienste), Massnahme 9.3 (Netzwerk-URL-Filter) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
