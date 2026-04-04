<!-- ISMS-CORE:REF:ISMS-REF-A.8.15-protokollierungs-standards-referenz-DE:framework:REF:a.8.15 -->
**ISMS-REF-A.8.15 — Protokollierungs-Standards-Referenz**
**Protokollformat-Standards & Technische Spezifikationen (Nicht-ISMS Technische Referenz)**

---

**Dokumentensteuerung**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Protokollierungs-Standards-Referenz |
| **Dokumententyp** | Intern – Technische Referenz (kein ISMS-Dokument) |
| **Dokument-ID** | ISMS-REF-A.8.15 |
| **Dokumentenersteller** | Security Operations Center (SOC) / Security Architecture Team |
| **Dokumenteneigentümer** | Information Security Manager |
| **Genehmigt von** | ISB (Technische Referenz – keine Genehmigung durch Executive Management erforderlich) |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | INTERN |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | SOC / Security Architecture | Erstversion als technische Referenz für ISO 27001:2022-Zertifizierung |

**Überprüfungsturnus**: Vierteljährlich (Protokollformat-Standards und Technologien entwickeln sich häufig weiter)
**Nächstes Überprüfungsdatum**: [Date + 3 Monate]
**Genehmigende**: SOC Lead / Security Architecture Team (technische Referenz, keine ISMS-Genehmigung erforderlich)

**Verteiler**: SOC-Team, Security Engineers, Systemadministratoren, Anwendungsentwickler (zur technischen Implementierungskenntnis)

---

⚠️ **WICHTIG – NICHT-ISMS TECHNISCHES UNTERSTÜTZUNGSDOKUMENT**

Dieses Dokument dient ausschliesslich zu Informations- und Sensibilisierungszwecken.

- Dieses Dokument ist NICHT Bestandteil des Informationssicherheits-Managementsystems (ISMS).
- Dieses Dokument definiert KEINE verbindlichen Protokollierungskontrollen oder -anforderungen.
- Dieses Dokument begründet KEINE verbindlichen Anforderungen, Fristen, KPIs oder SLAs.
- Dieses Dokument schreibt NICHT die Verwendung, das Verbot oder die Konfiguration spezifischer Protokollformate, Tools oder Plattformen vor.
- Dieses Dokument hebt KEINE ISMS-Richtlinie auf und erweitert sie auch nicht.

Alle verbindlichen Protokollierungsanforderungen, -pflichten und Governance-Entscheide sind ausschliesslich in **ISMS-POL-A.8.15 (Protokollierungsrichtlinie)** und anderen genehmigten ISMS-Dokumenten festgelegt.

Dieses Dokument dient ausschliesslich als technische Referenz für folgende Zwecke:

- Beschreibung häufig verwendeter Protokollformate und -standards
- Bereitstellung von Feldbenennungskonventionen und Kodierungsstandards
- Unterstützung der technischen Implementierungsplanung
- Orientierung bei der Auswahl von Protokollformaten und der Entwicklung von Parsern
- **Dieses Dokument darf nicht als Prüfnachweis der Implementierung verwendet werden**

Die Verwendung dieses Dokuments impliziert keine Implementierung, Konformität oder operationelle Reife.

**Grundsätzliche Positionierung**:
Dieses Dokument enthält bewusst technische Details, die über die Anforderungen der ISO/IEC 27001-Richtliniendokumentation hinausgehen. Es dient ausschliesslich der technischen Sensibilisierung. Aus dem Vorhandensein, dem Fehlen oder der Klassifizierung eines hier aufgeführten Protokollformats, Feldnamens oder technischer Spezifikation dürfen keine Prüfungsschlüsse gezogen werden.

---

# Dokumentenzweck und Anwendungsbereich

## Zweck

Dieses Dokument bietet eine technische Referenz für Protokollformat-Standards, Feldbenennungskonventionen und Kodierungsanforderungen, die häufig bei der Implementierung von Sicherheitsprotokollierung eingesetzt werden. Es soll Folgendes unterstützen:

- Technische Implementierung der Protokollierungsanforderungen gemäss ISMS-POL-A.8.15
- Auswahl geeigneter Protokollformate basierend auf Systemtyp und Integrationsanforderungen
- Entwicklung von Log-Parsing-Regeln und SIEM-Integration
- Standardisierung von Feldnamen über organisationsweite Protokollquellen hinweg
- Verständnis branchenüblicher Protokollformate (Syslog, CEF, JSON)
- Zukünftige Weiterentwicklung von Protokollformaten und Parser-Wartung

## Was dieses Dokument NICHT ist

Dieses Dokument definiert NICHT:

- Von [Organisation] genehmigte oder verbotene Protokollformate
- Verbindliche Implementierungsanforderungen oder technische Kontrollen
- Compliance-Verpflichtungen oder Prüfungskriterien
- Ersatz für die Anforderungen der ISMS-POL-A.8.15
- Spezifische SIEM-Plattformen, Log-Management-Tools oder Anbieter
- Aufbewahrungsfristen, Überprüfungsturnus oder Governance-Anforderungen

## Beziehung zum ISMS

Dieses Dokument ist eine **nicht verbindliche technische Referenz**. Alle Anforderungen an Protokollierungskontrollen sind ausschliesslich in ISMS-POL-A.8.15 definiert.

Implementierungsentscheide werden durch ISMS-IMP-A.8.15-Verfahren auf Basis von Risikobeurteilung, operativem Kontext und regulatorischen Anforderungen dokumentiert.

## Inhaltsorganisation

Diese Referenz organisiert Protokollformat-Standards nach:

- Syslog-Format (RFC 5424) für Infrastruktur- und Netzwerkgeräte
- Common Event Format (CEF) für Sicherheitstools und SIEM-Integration
- JSON Structured Logging für Anwendungen und Cloud-Dienste
- Feldbenennungskonventionen und Kodierungsstandards
- Zeitstempel-Formatanforderungen
- Zeichenkodierung und Escaping-Regeln

---

# Syslog-Format-Standards (RFC 5424)

## Überblick

**Syslog (RFC 5424)** ist das Standard-Protokollierungsprotokoll für Infrastrukturkomponenten, Betriebssysteme und Netzwerkgeräte.

**Häufige Anwendungsfälle**:

- Netzwerkgeräte (Router, Switches, Firewalls)
- Unix/Linux-Betriebssysteme
- Infrastrukturdienste (DNS, DHCP, NTP)
- Legacy-Anwendungen

**Protokoll**:

- UDP-Port 514 (traditionell, unverschlüsselt – NICHT EMPFOHLEN für Sicherheitsprotokolle)
- TCP-Port 514 oder 6514 (empfohlen für Zuverlässigkeit)
- TLS/TCP-Port 6514 (empfohlen für verschlüsselte Übertragung gemäss ISMS-POL-A.8.15 Abschnitt 2.2.3)

## Syslog-Nachrichtenformat

**RFC 5424-Nachrichtenstruktur**:

```
<PRI>VERSION TIMESTAMP HOSTNAME APP-NAME PROCID MSGID STRUCTURED-DATA MSG
```

**Beispiel**:
```
<134>1 2026-01-21T14:32:15.003+01:00 server01.example.com sshd 1234 ID47 [exampleSDID@32473 iut="3" eventSource="Application" eventID="1011"] Passwortauthentifizierung für ungültigen Benutzer admin von 10.0.1.50 Port 22 ssh2 fehlgeschlagen
```

## Syslog-Priorität (PRI)

**Prioritätsberechnung**: `PRI = (Facility * 8) + Severity`

**Facility-Codes** (häufige):

| Code | Facility | Verwendung |
|------|----------|------------|
| 0 | kernel | Kernel-Nachrichten |
| 1 | user | Nachrichten auf Benutzerebene |
| 2 | mail | Mail-System |
| 3 | daemon | System-Daemons |
| 4 | auth | Sicherheit/Authentifizierung |
| 5 | syslog | Syslog-intern |
| 10 | authpriv | Sicherheit/Autorisierung (privat) |
| 16 | local0-7 | Lokale Verwendung (benutzerdefinierte Anwendungen) |

**Schweregrade**:

| Code | Schweregrad | Beschreibung | Verwendungsrichtlinie |
|------|-------------|--------------|----------------------|
| 0 | Emergency | System ist nicht verwendbar | System-Absturz, unmittelbarer Ausfall |
| 1 | Alert | Sofortige Massnahme erforderlich | Kritischer Ressourcenausfall, Datenbeschädigung |
| 2 | Critical | Kritische Bedingungen | Hardware-Fehler, kritischer Dienstausfall |
| 3 | Error | Fehlerbedingungen | Nicht-kritische Fehler, Anwendungsausfälle |
| 4 | Warning | Warnbedingungen | Behebbare Fehler, Ressourcenwarnungen |
| 5 | Notice | Normal, aber bedeutsam | Bedeutsame Ereignisse (Privilege Escalation, Konfigurationsänderung) |
| 6 | Informational | Informationsnachrichten | Normalbetrieb, erfolgreiche Authentifizierungen |
| 7 | Debug | Debug-Nachrichten | Detaillierte Fehlerbehebungsinformationen |

**Empfohlene Schweregrad-Zuordnung**:

- **Sicherheitsereignisse**: Notice (5) für erfolgreiche Operationen, Warning (4) für Richtlinienverstösse, Error (3) für Angriffe
- **Authentifizierung**: Info (6) für Erfolg, Warning (4) für fehlgeschlagene Versuche, Error (3) für Kontosperrungen
- **Systemereignisse**: Je nach Kontext (Critical bei Dienstausfällen, Notice bei Konfigurationsänderungen)

## Syslog-Zeitstempelformat

**Erforderliches Format**: ISO 8601 mit Zeitzonenangabe

```
YYYY-MM-DDTHH:MM:SS.SSSSSS+TZ
```

**Beispiele**:

- `2026-01-21T14:32:15+01:00` (mit Zeitzonenoffset)
- `2026-01-21T13:32:15Z` (UTC-Notation)
- `2026-01-21T14:32:15.003+01:00` (mit Millisekunden)

**Best Practices**:

- Zeitzonenangabe immer einschliessen
- Millisekundengenauigkeit für Hochvolumensysteme verwenden, bei denen die Ereignisreihenfolge kritisch ist
- Systemuhren über NTP gemäss ISMS-POL-A.8.17 synchronisieren
- UTC für Mehrstandort-Umgebungen verwenden, um die Korrelation zu vereinfachen

## Syslog Structured Data

**Format**: Schlüssel-Wert-Paare in eckigen Klammern

```
[SD-ID@PEN key1="value1" key2="value2"]
```

**Beispiel**:
```
[secureAuth@123456 user="jdoe" src="10.0.1.50" action="login" result="success"]
```

**Empfohlene Structured-Data-Elemente**:

- `user="Benutzername"` – Benutzerkennung
- `src="IP-Adresse"` – Quell-IP
- `dst="IP-Adresse"` – Ziel-IP
- `action="Verb"` – Durchgeführte Aktion
- `result="success|failure"` – Ergebnis
- `reason="Beschreibung"` – Fehlergrund oder zusätzlicher Kontext

## Syslog-Konfigurationsbeispiel

**Linux rsyslog-Konfiguration** (TCP mit TLS):

```
# Sicherheitsprotokolle an zentrales SIEM senden
*.* @@(o)siem.example.com:6514
$ActionSendStreamDriverMode 1
$ActionSendStreamDriverAuthMode x509/name
$ActionSendStreamDriverPermittedPeer siem.example.com
```

**Syslog-Konfigurationsbeispiel für Netzwerkgeräte** (Cisco):

```
logging host 10.0.2.100 transport tcp port 6514
logging trap informational
logging origin-id hostname
logging source-interface Loopback0
```

---

# Common Event Format (CEF)

## Überblick

**Common Event Format (CEF)** ist ein standardisiertes Protokollformat für Sicherheitsereignisse, das für die SIEM-Integration entwickelt wurde.

**Entwickelt von**: ArcSight (jetzt Micro Focus), weit verbreiteter Branchenstandard

**Häufige Anwendungsfälle**:

- Sicherheitstools (Firewalls, IDS/IPS, Web Application Firewalls)
- Endpoint Protection Platforms
- Data Loss Prevention-Systeme
- Authentifizierungs- und Zugangskontrollsysteme
- SIEM-Integration aus verschiedenen Sicherheitsprodukten

## CEF-Nachrichtenformat

**Struktur**:

```
CEF:Version|Device Vendor|Device Product|Device Version|Signature ID|Name|Severity|Extension
```

**Beispiel**:
```
CEF:0|Palo Alto Networks|PAN-OS|9.1.0|THREAT|URL Filtering|7|rt=Jan 21 2026 14:32:15 src=10.0.1.50 dst=93.184.216.34 spt=52341 dpt=443 request=https://malicious.example.com act=blocked
```

## CEF-Header-Felder

| Feld | Beschreibung | Beispiel |
|------|--------------|---------|
| **Version** | CEF-Formatversion | 0 (aktueller Standard) |
| **Device Vendor** | Herstellername | Palo Alto Networks, Cisco, Check Point |
| **Device Product** | Produktname | PAN-OS, ASA, FortiGate |
| **Device Version** | Produktversion | 9.1.0 |
| **Signature ID** | Ereigniskennung | THREAT, AUTH, CONFIG |
| **Name** | Menschenlesbarer Ereignisname | URL Filtering, Login Failed |
| **Severity** | Skala 0–10 | 0=Niedrig, 5=Mittel, 10=Kritisch |

**Schweregradskala**:

- 0–3: Niedrig (informativ, geringfügige Probleme)
- 4–6: Mittel (Warnungen, Richtlinienverstösse)
- 7–8: Hoch (Sicherheitsbedrohungen, Angriffe)
- 9–10: Kritisch (schwere Bedrohungen, erfolgreiche Sicherheitsverletzungen)

## CEF-Erweiterungsfelder

**Standard-Erweiterungsschlüssel** (häufig verwendet):

| Schlüssel | Vollständiger Name | Beschreibung | Beispiel |
|-----------|-------------------|--------------|---------|
| **src** | Source Address | Quell-IP-Adresse | 10.0.1.50 |
| **dst** | Destination Address | Ziel-IP-Adresse | 93.184.216.34 |
| **spt** | Source Port | Quell-TCP/UDP-Port | 52341 |
| **dpt** | Destination Port | Ziel-TCP/UDP-Port | 443 |
| **suser** | Source User Name | Quellbenutzername | jdoe |
| **duser** | Destination User Name | Zielbenutzername | admin |
| **act** | Action | Durchgeführte Aktion | blocked, allowed, alerted |
| **app** | Application Protocol | Anwendungsprotokoll | HTTP, HTTPS, SSH, FTP |
| **request** | Request URL | Vollständige Anfrage-URL oder Befehl | https://example.com/pfad |
| **requestMethod** | Request Method | HTTP-Methode | GET, POST, PUT, DELETE |
| **cn1–cn3** | Custom Number 1–3 | Benutzerdefinierte numerische Felder | 1234 (übertragene Bytes) |
| **cs1–cs6** | Custom String 1–6 | Benutzerdefinierte String-Felder | "User-Agent: Mozilla/5.0" |
| **rt** | Receipt Time | Ereignis-Empfangszeit | Jan 21 2026 14:32:15 |
| **outcome** | Outcome | Ereignisergebnis | success, failure, unknown |
| **reason** | Reason | Grund für Aktion oder Fehler | Invalid credentials |
| **fileHash** | File Hash | Datei-Hash (MD5, SHA256) | a1b2c3d4e5f6... |
| **filePath** | File Path | Vollständiger Dateipfad | /var/log/suspicious.exe |

## CEF-Beispiele nach Ereignistyp

**Authentifizierungsereignis** (Fehlgeschlagene Anmeldung):
```
CEF:0|Microsoft|Windows|Server 2019|4625|An account failed to log on|5|rt=Jan 21 2026 14:32:15 suser=admin src=10.0.1.50 outcome=failure reason=Unknown user name or bad password cs1Label=Domain cs1=EXAMPLE
```

**Firewall-Ereignis** (Gesperrte Verbindung):
```
CEF:0|Palo Alto Networks|PAN-OS|9.1.0|TRAFFIC|deny|8|rt=Jan 21 2026 14:32:15 src=10.0.1.50 dst=203.0.113.100 spt=52341 dpt=22 proto=TCP act=deny app=SSH
```

**Malware-Erkennung**:
```
CEF:0|CrowdStrike|Falcon|6.42|MALWARE|Malware Detected|9|rt=Jan 21 2026 14:32:15 src=10.0.2.15 filePath=C:\\Users\\jdoe\\Downloads\\malware.exe fileHash=a1b2c3d4e5f6 act=quarantined outcome=success
```

**Web Application Firewall** (SQL-Injection blockiert):
```
CEF:0|F5 Networks|BIG-IP ASM|15.1.0|SQL_INJECTION|SQL Injection Attack|9|rt=Jan 21 2026 14:32:15 src=203.0.113.50 request=https://webapp.example.com/login?id=1' OR '1'='1 requestMethod=GET act=blocked
```

## CEF Best Practices

1. **Standard-Erweiterungsschlüssel verwenden**, wo anwendbar (src, dst, suser) für SIEM-Kompatibilität
2. **Benutzerdefinierte Felder für nicht-standardisierte Daten** (cs1–cs6 für Strings, cn1–cn3 für Zahlen)
3. **Zeitstempel immer einschliessen** (rt-Feld) für genaue Ereigniskorrelation
4. **Pipe-Zeichen in Erweiterungswerten escapen** (Backslash verwenden: \|)
5. **Backslashes in Erweiterungswerten escapen** (doppelter Backslash: \\)
6. **Gleichheitszeichen in benutzerdefinierten Feldwerten escapen** (Backslash: \=)

---

# JSON Structured Logging

## Überblick

**JSON (JavaScript Object Notation)** ist der moderne Standard für Anwendungsprotokollierung und Cloud-Dienst-Logs.

**Häufige Anwendungsfälle**:

- Moderne Webanwendungen und Microservices
- Container- und Kubernetes-Umgebungen
- Cloud-native Anwendungen (AWS, Azure, GCP)
- API-Gateways und serverlose Funktionen
- SaaS-Anwendungsprotokolle

**Vorteile**:

- Menschenlesbar und maschinenverarbeitbar
- Native Unterstützung in modernen SIEM- und Log-Aggregationsplattformen
- Flexibles Schema (kann jede Feldstruktur aufnehmen)
- Einfach aus Anwendungscode zu erzeugen (Bibliotheken für alle Sprachen verfügbar)

## JSON-Protokollstruktur

**Mindestpflichtfelder**:

```json
{
  "timestamp": "2026-01-21T14:32:15.003+01:00",
  "level": "INFO",
  "message": "Benutzeranmeldung erfolgreich",
  "logger": "auth.service",
  "context": {
    "user": "jdoe",
    "source_ip": "10.0.1.50",
    "action": "login",
    "outcome": "success"
  }
}
```

## Standard-Feldnamen

**Empfohlene JSON-Feldbenennungskonvention** (snake_case):

| Feldname | Typ | Beschreibung | Beispiel |
|----------|-----|--------------|---------|
| **timestamp** | string (ISO 8601) | Ereigniszeitstempel mit Zeitzone | "2026-01-21T14:32:15+01:00" |
| **level** | string | Protokollebene | "INFO", "WARN", "ERROR", "DEBUG" |
| **message** | string | Menschenlesbare Nachricht | "Benutzeranmeldung erfolgreich" |
| **logger** | string | Logger-Name oder Modul | "auth.service", "app.controller" |
| **user_id** | string | Benutzerkennung | "jdoe", "user@example.com" |
| **session_id** | string | Sitzungskennung | "abc123def456" |
| **request_id** | string | Anfrage-Trace-ID | "req-7f8a9b0c" |
| **source_ip** | string | Quell-IP-Adresse | "10.0.1.50" |
| **destination_ip** | string | Ziel-IP-Adresse | "93.184.216.34" |
| **action** | string | Durchgeführte Aktion | "login", "create", "delete", "read" |
| **resource** | string | Betroffene Ressource | "/api/users", "datei.txt" |
| **outcome** | string | Ergebnis der Aktion | "success", "failure", "error" |
| **error_code** | string | Fehlercode oder Ausnahmetyp | "AUTH001", "NullPointerException" |
| **duration_ms** | number | Dauer in Millisekunden | 250 |
| **http_method** | string | HTTP-Methode | "GET", "POST", "PUT", "DELETE" |
| **http_status** | number | HTTP-Statuscode | 200, 404, 500 |
| **user_agent** | string | User-Agent-String | "Mozilla/5.0..." |

## Protokollebenen

**Standard-Protokollebenen** (RFC 5424-Äquivalenz):

| Ebene | Schweregrad | Verwendung | Beispiel |
|-------|-------------|------------|---------|
| **TRACE** | Debug | Sehr detailliertes Debugging | Variablenwerte, Funktionseinstieg/-austritt |
| **DEBUG** | Debug | Detailliertes Debugging | Logikfluss, Zwischenergebnisse |
| **INFO** | Informational | Normalbetrieb | Dienst gestartet, Benutzer angemeldet, Transaktion abgeschlossen |
| **WARN** | Warning | Potenzielle Probleme | Veraltete API verwendet, Wiederholungsversuch, Schwellenwert wird erreicht |
| **ERROR** | Error | Fehlerbedingungen | Datenbankverbindung fehlgeschlagen, API-Aufruf fehlgeschlagen, Validierungsfehler |
| **FATAL/CRITICAL** | Critical | Schwerwiegende Fehler | Anwendungsabsturz, nicht behebbarer Fehler, Datenbeschädigung |

**Empfehlung für Produktivbetrieb**:

- **Sicherheitsprotokolle**: INFO und höher (INFO für Erfolg, WARN für Richtlinienverstösse, ERROR für Angriffe)
- **Anwendungsprotokolle**: WARN und höher (Störungen minimieren, Probleme erfassen)
- **DEBUG/TRACE**: Im Produktivbetrieb deaktiviert (temporär zur Fehlerbehebung aktivieren, Leistungsaspekte beachten)

## Strukturierter Kontext

**Verschachtelter Kontext für zusammengehörige Felder**:

```json
{
  "timestamp": "2026-01-21T14:32:15.003+01:00",
  "level": "ERROR",
  "message": "Authentifizierung fehlgeschlagen",
  "logger": "auth.service",
  "user": {
    "id": "jdoe",
    "email": "jdoe@example.com",
    "role": "user"
  },
  "request": {
    "id": "req-7f8a9b0c",
    "method": "POST",
    "path": "/api/auth/login",
    "source_ip": "10.0.1.50",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
  },
  "auth": {
    "method": "password",
    "outcome": "failure",
    "reason": "invalid_credentials",
    "attempts": 3
  },
  "error": {
    "code": "AUTH001",
    "type": "AuthenticationException",
    "message": "Ungültiger Benutzername oder Passwort"
  }
}
```

## JSON-Beispiele nach Ereignistyp

**Authentifizierungserfolg**:
```json
{
  "timestamp": "2026-01-21T14:32:15.003+01:00",
  "level": "INFO",
  "message": "Benutzer erfolgreich authentifiziert",
  "logger": "auth.service",
  "user_id": "jdoe",
  "session_id": "sess-abc123",
  "source_ip": "10.0.1.50",
  "action": "login",
  "outcome": "success",
  "auth_method": "password_mfa",
  "duration_ms": 125
}
```

**API-Anfrage-Protokoll**:
```json
{
  "timestamp": "2026-01-21T14:32:16.120+01:00",
  "level": "INFO",
  "message": "API-Anfrage verarbeitet",
  "logger": "api.gateway",
  "request_id": "req-7f8a9b0c",
  "http_method": "GET",
  "http_path": "/api/users/jdoe",
  "http_status": 200,
  "source_ip": "10.0.1.50",
  "user_id": "admin",
  "duration_ms": 45,
  "response_size_bytes": 1024
}
```

**Datenbankabfrage-Protokoll**:
```json
{
  "timestamp": "2026-01-21T14:32:17.250+01:00",
  "level": "INFO",
  "message": "Datenbankabfrage ausgeführt",
  "logger": "database.service",
  "query_type": "SELECT",
  "table": "users",
  "user_id": "system",
  "duration_ms": 15,
  "rows_returned": 1,
  "query_hash": "a1b2c3d4"
}
```

**Fehler mit Stack-Trace**:
```json
{
  "timestamp": "2026-01-21T14:32:18.500+01:00",
  "level": "ERROR",
  "message": "Unbehandelte Ausnahme bei der Zahlungsverarbeitung",
  "logger": "payment.service",
  "request_id": "req-payment-001",
  "user_id": "customer123",
  "error": {
    "type": "PaymentGatewayException",
    "message": "Zeitüberschreitung beim Zahlungsgateway",
    "code": "GATEWAY_TIMEOUT",
    "stack_trace": "PaymentGatewayException: Gateway timeout\n  at PaymentService.processPayment(PaymentService.java:123)\n  at PaymentController.handlePayment(PaymentController.java:45)"
  },
  "transaction": {
    "id": "txn-789xyz",
    "amount": 99.99,
    "currency": "CHF"
  }
}
```

## JSON Best Practices

1. **Zeitstempel immer einschliessen** mit Zeitzone (ISO 8601-Format)
2. **snake_case verwenden** für Feldnamen (einheitliche Konvention)
3. **Verschachtelung minimieren** (maximal 1–2 Ebenen für Lesbarkeit und Parsing-Effizienz)
4. **Keine sensiblen Daten protokollieren** (keine Passwörter, vollständige Kreditkartennummern, personenbezogene Daten sofern nicht erforderlich)
5. **Kontextidentifikatoren einschliessen** (request_id, session_id, user_id) für Korrelation
6. **Strukturierte Daten verwenden** anstatt Strings im Nachrichtenfeld zu verketten
7. **Konsistentes Schema** über die gesamte Anwendung (Protokollbibliothek mit Schema-Validierung verwenden)
8. **Ein Protokollereignis pro Zeile** (zeilentrennungsbasiertes JSON für einfaches Parsing)

---

# Zeitstempel-Standards

## Erforderliches Format: ISO 8601

**Standard**: ISO 8601 mit Zeitzonenangabe

**Format**: `YYYY-MM-DDTHH:MM:SS.SSSSSS±HH:MM` oder `YYYY-MM-DDTHH:MM:SS.SSSZ`

**Beispiele**:

- `2026-01-21T14:32:15+01:00` (Mitteleuropäische Zeit mit Offset)
- `2026-01-21T13:32:15Z` (UTC, Suffix 'Z' zeigt UTC an)
- `2026-01-21T14:32:15.003+01:00` (mit Millisekunden)
- `2026-01-21T14:32:15.123456+01:00` (mit Mikrosekunden)

## Zeitzonenbehandlung

**Empfehlung**: UTC für alle zentralisierten Protokollspeicher verwenden

**Begründung**:

- Eliminiert Zeitzonenkonversionsfehler
- Vereinfacht Korrelation über geografische Standorte hinweg
- Vermeidet Komplikationen durch Sommerzeit
- Universelle Referenz für Mehrstandort-Organisationen

**Ortszeit mit Offset** (Alternative):

- Akzeptabel für Einzelstandort-Deployments
- MUSS Zeitzonenoffset einschliessen (z.B. +01:00, -05:00)
- SIEM muss zur Korrelation auf UTC normalisieren

## Genauigkeitsanforderungen

**Mindestanforderung**: Sekundengenauigkeit (`YYYY-MM-DDTHH:MM:SS`)

**Empfohlen**: Millisekundengenauigkeit (`YYYY-MM-DDTHH:MM:SS.SSS`)

- Erforderlich für Hochvolumensysteme (Hunderte Ereignisse pro Sekunde)
- Ermöglicht genaue Ereignissortierung innerhalb derselben Sekunde
- Notwendig für Korrelation schneller Ereignissequenzen

**Optional**: Mikrosekundengenauigkeit (`YYYY-MM-DDTHH:MM:SS.SSSSSS`)

- Nützlich für sehr leistungsintensive Systeme
- Datenbankprotokollierung mit Sub-Millisekunden-Granularität

## Zeitsynchronisation

**Anforderung**: Alle Protokollquellen MÜSSEN ihre Zeit mit einer autoritativen Zeitquelle synchronisieren gemäss ISMS-POL-A.8.17 (Zeitsynchronisation).

**NTP-Konfiguration**:

- Primärer NTP-Server (Stratum 1 oder 2)
- Sekundäre NTP-Server für Redundanz
- Maximale Uhrenabweichung: ±100 ms
- Alarm bei NTP-Synchronisationsfehler

**Bedeutung**: Genaue Zeitstempel sind kritisch für:

- Ereigniskorrelation über mehrere Systeme hinweg
- Rekonstruktion von Vorfallszeitlinien
- Forensische Analyse und Beweismittel für Rechtsverfahren
- Compliance-Verifizierung

---

# Feldbenennungskonventionen

## Benennungsstandards

**Einheitliche Benennungskonvention verwenden**:

| Konvention | Beispiel | Anwendungsfall |
|------------|---------|----------------|
| **snake_case** | `source_ip`, `user_id`, `event_type` | JSON-Logs, Python-Anwendungen |
| **camelCase** | `sourceIp`, `userId`, `eventType` | JavaScript-Anwendungen, einige SIEMs |
| **dot.notation** | `event.type`, `user.id`, `source.ip` | ECS (Elastic Common Schema), verschachtelte Felder |

**Empfehlung**: EINE Konvention wählen und organisationsweit einheitlich anwenden. snake_case wird bei der Sicherheitsprotokollierung zunehmend gängiger.

## Standard-Feldnamen

**Identitätsfelder**:

- `user_id` / `user` / `username` – Benutzerkennung
- `user_email` – E-Mail-Adresse des Benutzers
- `service_account` – Dienstkontoidentifikator
- `session_id` – Sitzungskennung
- `request_id` / `trace_id` – Anfrage-Trace-Kennung
- `transaction_id` – Transaktionskennung

**Netzwerkfelder**:

- `source_ip` / `src_ip` – Quell-IP-Adresse
- `destination_ip` / `dst_ip` – Ziel-IP-Adresse
- `source_port` / `src_port` – Quell-TCP/UDP-Port
- `destination_port` / `dst_port` – Ziel-TCP/UDP-Port
- `protocol` – Netzwerkprotokoll (TCP, UDP, ICMP)
- `hostname` – System-Hostname

**Aktionsfelder**:

- `action` / `event_action` – Durchgeführte Aktion (login, create, delete, read, update)
- `event_type` / `event_category` – Ereigniskategorie (authentication, authorisation, configuration)
- `outcome` / `result` – Ergebnis (success, failure, error)
- `reason` – Grund für Ergebnis oder Aktion
- `severity` / `level` – Schweregrad

**Ressourcenfelder**:

- `resource` / `object` – Betroffene Ressource
- `file_path` – Dateipfad
- `file_hash` – Datei-Hash (MD5, SHA256)
- `url` / `request_url` – URL oder Endpunkt
- `api_endpoint` – API-Endpunkt

**Zeitfelder**:

- `timestamp` / `event_time` – Ereigniszeitstempel
- `duration` / `duration_ms` – Dauer in Millisekunden
- `start_time` – Startzeitstempel
- `end_time` – Endzeitstempel

**Anwendungsfelder**:

- `application` / `app_name` – Anwendungsname
- `environment` – Umgebung (production, staging, development)
- `version` / `app_version` – Anwendungsversion
- `component` / `module` – Komponenten- oder Modulname

**Fehlerfelder**:

- `error_code` – Fehlercode
- `error_type` / `exception_type` – Ausnahmeklassenname
- `error_message` / `exception_message` – Fehlerbeschreibung
- `stack_trace` – Stack-Trace (bei Fehlern)

## Mehrdeutige Namen vermeiden

**NICHT VERWENDEN**:

- `data` – Zu allgemein; spezifischen Namen verwenden (z.B. `user_data`, `request_data`)
- `info` – Mehrdeutig; spezifischen Namen verwenden (z.B. `user_info` → `user_email`)
- `value` – Nicht beschreibend; semantischen Namen verwenden
- `temp` – Unklarer Zweck; beschreibenden Namen verwenden

**VERWENDEN**:

- Beschreibende, selbstdokumentierende Namen
- Einheitliche Terminologie in der gesamten Organisation
- Standardnamen aus ECS (Elastic Common Schema) soweit anwendbar

---

# Zeichenkodierung und Escaping

## Zeichenkodierung

**Standard**: UTF-8-Kodierung für alle Protokolle

**Begründung**:

- Universelle Unterstützung für internationale Zeichen
- Effizient für ASCII (1 Byte pro Zeichen)
- Kompatibel mit JSON, XML, modernen Anwendungen

**Implementierung**:

- Protokollquellen zur UTF-8-Ausgabe konfigurieren
- SIEM-Parser für UTF-8-Erwartung konfigurieren
- Mit Nicht-ASCII-Zeichen testen (ä, ö, ü, é, ñ, 中文)

## Sonderzeichen-Escaping

**Syslog (RFC 5424)**:

- Im MSG-Feld ist kein besonderes Escaping erforderlich
- Structured-Data-Format für Schlüssel-Wert-Paare verwenden (automatisches Escaping)

**CEF**:

- Pipe-Zeichen escapen: `|` → `\|`
- Backslashes escapen: `\` → `\\`
- Gleichheitszeichen in Erweiterungswerten escapen: `=` → `\=`
- Zeilenumbrüche escapen: `\n` → `\\n`

**Beispiel**:
```
# Originalnachricht: Benutzer von C:\Programme\Anwendung angemeldet
# Für CEF escaped:
cs1=C:\\Programme\\Anwendung
```

**JSON**:

- JSON-Bibliotheken escapen Sonderzeichen automatisch
- Manuelles Escaping (falls erforderlich):
  - Anführungszeichen: `"` → `\"`
  - Backslashes: `\` → `\\`
  - Zeilenumbrüche: Zeilenumbruchzeichen → `\n`
  - Tabulatoren: Tabulatorzeichen → `\t`

**Beispiel**:
```json
{
  "message": "Benutzer von \"C:\\Programme\\Anwendung\" angemeldet"
}
```

## Maximale Feldlängen

**Empfehlungen** (SIEM-Kompatibilität):

| Feldtyp | Maximale Länge | Begründung |
|---------|----------------|------------|
| **String-Felder** | 1024 Zeichen | SIEM-Datenbankfeldgrenzen |
| **Nachrichtenfeld** | 8192 Zeichen | Protokollnachrichten können Stack-Traces enthalten |
| **URL-Felder** | 2048 Zeichen | Unterstützung moderner URL-Längen |
| **Dateipfad** | 4096 Zeichen | Unix/Linux-Pfadmaximum |
| **Benutzerkennung** | 256 Zeichen | E-Mail-Adressen, LDAP-DN |

**Kürzungsstrategie**:

- Bei narrativen Feldern (Nachrichten, Beschreibungen) am Ende kürzen
- Bei URLs in der Mitte kürzen (Domain und Parameter erhalten)
- Kennungen (Benutzer-IDs, Transaktions-IDs) nie kürzen – bei zu grosser Länge ablehnen

---

# Implementierungsleitfaden

## Protokollformat-Auswahlmatrix

**Entscheidungshilfe**: Protokollformat basierend auf Systemtyp auswählen

| Systemtyp | Empfohlenes Format | Begründung |
|-----------|-------------------|------------|
| **Netzwerkgeräte** (Firewall, Router, Switch) | Syslog (RFC 5424) | Native Unterstützung, minimale Konfiguration |
| **Unix/Linux-BS** | Syslog (RFC 5424) | Native Unterstützung, Standard-Infrastruktur |
| **Windows-BS** | Windows Event Log (nativ) | Native Unterstützung; für SIEM zu CEF oder JSON konvertieren |
| **Sicherheitstools** (IDS, Firewall, WAF) | CEF | SIEM-Integration, standardisierte Sicherheitsereignisse |
| **Webanwendungen** | JSON | Einfach zu erzeugen, flexibles Schema |
| **Microservices** | JSON | Cloud-native, container-freundlich |
| **Cloud-Dienste** (AWS, Azure, GCP) | JSON (CloudWatch, Azure Monitor, Cloud Logging) | Natives Format, nahtlose Integration |
| **Datenbankprotokolle** | JSON oder Syslog | Anwendungsspezifisch; JSON bevorzugt für strukturierte Abfragen |

## SIEM-Integrationsüberlegungen

**Parser-Entwicklung**:

- Syslog: Eingebaute Parser verwenden, für Structured-Data-Extraktion anpassen
- CEF: Eingebaute CEF-Parser verwenden, Erweiterungsfelder auf SIEM-Schema abbilden
- JSON: JSON-Parser konfigurieren, Feldzuordnungen definieren

**Feldzuordnung**:

- Protokollquell-Felder auf gemeinsames SIEM-Schema abbilden (Feldnamen normalisieren)
- Berechnete Felder für abgeleitete Daten erstellen (z.B. Geolokalisierung aus IP)
- Ereignisse mit Threat Intelligence anreichern (Abfragen bekannter schädlicher IPs)

**Leistungsoptimierung**:

- Geeignete Protokollebenenfilterung verwenden (INFO und höher für Produktivbetrieb)
- Sampling für Hochvolumen-/Niedrigwert-Protokolle implementieren (Debug-Logs)
- Protokolle vor der Übertragung komprimieren (gzip, sofern vom SIEM unterstützt)
- Batch-Log-Weiterleitung (Collect-and-Forward vs. Echtzeit)

## Empfehlungen für Protokollbibliotheken

**Nach Programmiersprache**:

| Sprache | Empfohlene Bibliothek | Strukturierte Protokollierungsunterstützung |
|---------|----------------------|---------------------------------------------|
| **Python** | `structlog`, `python-json-logger` | Ja (JSON-Ausgabe) |
| **Java** | `Logback`, `Log4j2` | Ja (JSON-Encoder verfügbar) |
| **JavaScript/Node.js** | `winston`, `pino` | Ja (JSON nativ) |
| **Go** | `zap`, `logrus` | Ja (JSON nativ) |
| **C#/.NET** | `Serilog`, `NLog` | Ja (JSON-Formatter) |
| **Ruby** | `Lograge`, `semantic_logger` | Ja (JSON-Ausgabe) |
| **PHP** | `Monolog` | Ja (JSON-Formatter) |

**Konfigurationsbeispiel** (Python structlog):

```python
import structlog

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    logger_factory=structlog.stdlib.LoggerFactory(),
)

log = structlog.get_logger()
log.info("user_login", user_id="jdoe", source_ip="10.0.1.50", outcome="success")
```

---

# Dokumentenwartung

## Aktualisierungsanlässe

Dieses Referenzdokument kann aktualisiert werden, wenn:

- Neue Protokollformat-Standards entstehen oder bestehende Standards aktualisiert werden
- Änderungen der SIEM-Plattform neue Formatunterstützung erfordern
- Log-Parsing-Probleme identifiziert werden, die eine Formatpräzisierung erfordern
- Anwendungsentwicklungsteams Orientierung zu neuen Protokollformaten anfordern
- Branchenbest Practices sich weiterentwickeln (z.B. ECS-Schema-Aktualisierungen)

## Verantwortlichkeit

**Dokumenteneigentümer**: SOC Lead / Security Architecture Team
**Überprüfungsturnus**: Vierteljährlich oder nach Bedarf
**Aktualisierungsbefugnis**: Technische Aktualisierung (kein ISMS-Genehmigungsprozess erforderlich)

## Versionskontrolle

Alle Versionen werden als Referenz aufbewahrt. Wesentliche Änderungen sind in der Versionshistorie-Tabelle dokumentiert. Frühere Versionen sind im Dokumentenrepository verfügbar.

---

# Beziehung zu ISMS-POL-A.8.15

Dieses Dokument bietet **technischen Implementierungsleitfaden**, der Folgendes unterstützen kann:

- Auswahl von Protokollformaten bei der System-Einbindung (ISMS-IMP-A.8.15.1)
- Entwicklung von Log-Parsern für die SIEM-Integration (ISMS-IMP-A.8.15.2)
- Standardisierung von Feldnamen über organisationsweite Protokollquellen hinweg
- Schulung von Entwicklern und Systemadministratoren zu Protokollierungsstandards

Dieses Dokument definiert NICHT:

- Anforderungen der ISMS-POL-A.8.15 aufzuheben oder zu erweitern
- Verbindliche Protokollformat-Auswahlen festzulegen
- Compliance-Verpflichtungen zu begründen
- Prüfungskriterien zu definieren

Alle Anforderungen an Protokollierungskontrollen sind ausschliesslich in ISMS-POL-A.8.15 definiert und werden durch ISMS-IMP-A.8.15-Verfahren auf Basis von Risikobeurteilung und operativem Kontext implementiert.

---

**ENDE DES DOKUMENTS**

*Dies ist ein technisches Referenzdokument ausschliesslich zu Informationszwecken. Es begründet keine ISMS-Anforderungen und schafft keine Compliance-Verpflichtungen.*

**DIESES DOKUMENT IST NICHT BESTANDTEIL DES ISMS.**

<!-- QA_VERIFIED: 2026-03-29 -->
