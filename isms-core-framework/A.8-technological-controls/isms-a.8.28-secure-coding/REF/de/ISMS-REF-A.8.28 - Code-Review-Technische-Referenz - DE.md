<!-- ISMS-CORE:REF:ISMS-REF-A.8.28-code-review-technische-referenz-DE:framework:REF:a.8.28 -->
**ISMS-REF-A.8.28 — Code-Review-Technische Referenz**

**Dokumentenkontrolle — ISMS-REF-A.8.28**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Code-Review-Technische Referenz |
| **Dokumententyp** | Technische Referenz (REF) |
| **Dokument-ID** | ISMS-REF-A.8.28 |
| **Ersteller** | Application Security Lead |
| **Dokumenteneigentümer** | Application Security Lead |
| **Genehmigt von** | Application Security Lead |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Date] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

---

## Haftungsausschluss

**WICHTIG**: Dies ist ein informelles Referenzdokument und ist **NICHT** Bestandteil des formalen ISMS-Richtlinienrahmens.

Die hierin enthaltenen Informationen bieten technische Anleitungen und methodische Details, begründen jedoch **KEINE verbindlichen Anforderungen**.

**Verbindliche Richtlinienanforderungen** sind in **ISMS-POL-A.8.28 (Richtlinie zur sicheren Codierung)** definiert.

**Zweck**: Unterstützung der Umsetzung von Code-Reviews durch:

- Detaillierte Sicherheits-Checklisten für Code-Reviews
- Methodenvergleiche und Anleitungen
- Risikobasierte Prüfungsansätze
- Best Practices für die Umsetzung

**Verwendung**: Technische Referenz für Code-Reviewer, Security Champions und Entwicklungsteams. Inhalt muss möglicherweise aktualisiert werden, wenn sich Schwachstellenmuster weiterentwickeln — Veröffentlichungsdatum prüfen.

---

# Zweck und Geltungsbereich

## Referenzziel

Dieses Dokument stellt **handlungsorientierte Sicherheitskriterien** für Code-Reviewer bereit. Es setzt die Anforderungen an Code-Reviews aus ISMS-POL-A.8.28 Abschnitt 2.3 in praktische Prüfschritte um.

*"Das erste Prinzip ist, dass man sich selbst nicht täuschen darf — und man selbst ist die am leichtesten zu täuschende Person." — Richard Feynman*

**Ziel**: Code-Reviewer in die Lage versetzen, Sicherheitsprobleme systematisch zu identifizieren, ohne für jeden Review tiefgreifende Sicherheitsexpertise vorauszusetzen.

## Behandelte Themen

- Checkliste zur Vorbereitung auf den Review
- Zentrale Sicherheitsprüfkriterien (Authentifizierung, Eingabevalidierung, Autorisierung, Kryptographie, Protokollierung, Fehlerbehandlung)
- Risikobasierter Prüfungsansatz
- Gängige Muster und Anti-Muster
- Eskalationsverfahren

## Beziehung zur Richtlinie

**ISMS-POL-A.8.28 fordert** (verbindlich):

- Peer-Code-Review für den gesamten Produktionscode
- Sicherheitsfokussierte Prüfkriterien
- Beteiligung von Security Champions an Reviews
- Review durch das Application-Security-Team bei Hochrisikoänderungen

**Dieses REF-Dokument erläutert** (informativ):

- WIE sicherheitsfokussierte Code-Reviews durchzuführen sind
- WELCHE Sicherheitsprobleme zu suchen sind
- WANN an Security Champions oder das Application-Security-Team eskaliert werden soll
- Risikobasierte Anwendung der Checkliste

---

# Verwendung dieser Checkliste

## Nicht jedes Element für jeden Review

**Risikobasierter Ansatz**:

**Hochrisikoänderungen** (vollständige Checkliste verwenden):

- Änderungen an Authentifizierung oder Autorisierung
- Kryptographie-Implementierungen
- Verarbeitung von Zahlungs- oder Finanztransaktionen
- Verarbeitung personenbezogener Daten oder Datenexposition
- Änderungen an Sicherheitskontrollen
- Integrationen mit Drittanbietern bei sensiblen Daten

**Mittelrisikoänderungen** (relevante Abschnitte fokussieren):

- API-Endpunkte → Eingabevalidierung + Autorisierung
- Datenbankabfragen → SQL-Injection-Verhinderung
- Dateioperationen → Path-Traversal-Verhinderung
- Web-UI-Änderungen → XSS + CSRF-Verhinderung

**Niedrigrisikoänderungen** (minimaler Sicherheitsreview):

- Refactoring ohne Funktionsänderungen
- Dokumentationsaktualisierungen
- Konfigurationsänderungen (nicht sicherheitsrelevant)
- Reine Teständerungen

## Integrationspunkte

**Pull-Request-Vorlagen**:
```markdown
# Sicherheits-Checkliste (falls zutreffend)

- [ ] Eingabevalidierung vorhanden und korrekt
- [ ] Ausgabe-Encoding dem Kontext entsprechend
- [ ] SQL-Abfragen parametrisiert
- [ ] Keine hartcodierten Geheimnisse
- [ ] Autorisierungsprüfungen vorhanden

```

**Review-Tools**:

- Checklisten-Elemente in Review-Kommentaren verlinken (z.B. "Verstösst gegen 3.2.3: SQL-Injection-Risiko")
- Review-Tool-Labels verwenden (security-review-required, security-approved)

**Schulung**:

- Checkliste in Code-Review-Schulungsworkshops verwenden
- Security Champions erlernen die Anwendung der Checkliste
- Regelmässige Auffrischungen zur Checkliste

## Wann zu eskalieren

**Eskalation an Security Champion**:

- Checklisten-Element unklar oder mehrdeutig
- Sicherheitsbedenken jenseits der eigenen Fachkenntnis
- Mehrere Checklisten-Elemente nicht erfüllt
- Komplexes Sicherheitsmuster erfordert Validierung

**Eskalation an Application-Security-Team**:

- Vermutete Schwachstelle erfordert Expertenvalidierung
- Sicherheitsbedenken auf Architekturebene
- Bedarfsmodelliersitzung erforderlich
- Kritische/hohe Schwachstellenbefunde aus automatisierten Tools

**Eskalationskanäle**:

- Slack: #security-champions oder #appsec
- E-Mail: security@[organisation].com
- Im PR markieren: @security-champions oder @appsec-team

---

# Checkliste zur Vorbereitung des Reviews

**VOR dem Code-Review ausfüllen** (spart Zeit, sichert Qualität):

- [ ] **Automatisierte Prüfungen bestanden**: SAST, SCA, Unit-Tests, Linter — alle grün?
  - *Falls nicht*: Automatisierte Befunde zuerst prüfen, sicherstellen, dass sie behoben oder mit Begründung unterdrückt sind

- [ ] **Änderungsbeschreibung klar**: Erklärt die PR-Beschreibung, WAS geändert wurde und WARUM?
  - *Prüfen auf*: Vage Beschreibungen ("Bug behoben", "Updates"), fehlenden Kontext
  - *Massnahme*: Bei Unklarheit Klärung anfordern

- [ ] **Risikoniveau bestimmt**: Gibt die PR das Risikoniveau an (Kritisch/Hoch/Mittel/Niedrig)?
  - *Falls nicht bestimmt*: Risiko gemäss Kriterien aus Abschnitt 2.1 einschätzen

- [ ] **Sicherheitsrelevante Änderungen gekennzeichnet**: Identifiziert der PR-Ersteller Sicherheitsauswirkungen?
  - *Prüfen auf*: Authentifizierung, Autorisierung, Eingabeverarbeitung, Kryptographie, Datenzugriff
  - *Massnahme*: Bei Sicherheitsrelevanz ohne Kennzeichnung entsprechende Checklisten-Abschnitte anwenden

- [ ] **Änderungsumfang angemessen**: Ist die PR fokussiert (nicht 50 Dateien mit unzusammenhängenden Änderungen)?
  - *Falls zu gross*: Aufteilung in kleinere, überprüfbare PRs anfordern

- [ ] **Tests enthalten**: Sind sicherheitsrelevante Änderungen durch Tests abgedeckt?
  - *Prüfen auf*: Tests zur Eingabevalidierung, Autorisierungstests, negative Testfälle
  - *Richtlinienreferenz*: ISMS-POL-A.8.28 Abschnitt 2.3.1

---

# Zentrale Sicherheits-Checkliste

## Authentifizierung und Session-Management

- [ ] **Authentifizierungsprüfungen vorhanden**: Alle geschützten Endpunkte verifizieren die Benutzerauthentifizierung
  - *Prüfen auf*: Fehlende Authentifizierung bei API-Endpunkten, Admin-Seiten, Datenzugriff
  - *Test*: Kann auf den Endpunkt ohne Authentifizierung zugegriffen werden?
  - *Richtlinienreferenz*: ISMS-POL-A.8.28 Abschnitt 2.2

- [ ] **Session-Tokens sicher**: Tokens sind zufällig, nicht vorhersagbar, mit HttpOnly/Secure-Flags
  - *Prüfen auf*: Vorhersagbare Session-IDs, sequenzielle Tokens, Tokens in URLs
  - *Verifizieren*: Cookie-Attribute umfassen `HttpOnly`, `Secure`, `SameSite=Strict/Lax`

- [ ] **Passwortverarbeitung sicher**: Passwörter mit bcrypt/Argon2 gehasht, nie protokolliert
  - *Prüfen auf*: Passwörter im Klartext, schwaches Hashing (MD5, SHA1, SHA256 ohne Salt)
  - *Verifizieren*: Keine Passwörter in Logs, Fehlermeldungen oder Debug-Ausgaben
  - *Beispiel*: Siehe ISMS-CTX-A.8.28 Python Abschnitt 2.6

- [ ] **Multi-Faktor-Authentifizierung (MFA) erzwungen**: MFA für privilegierte Konten erforderlich
  - *Prüfen auf*: Admin-Konten, Finanzoperationen, die MFA umgehen

- [ ] **Session-Timeout angemessen**: Sessions verfallen nach Inaktivitätszeitraum
  - *Prüfen auf*: Kein Timeout, übermässig langer Timeout (>30 Min. bei Hochrisikoanwendungen)

- [ ] **Logout-Funktion sicher**: Logout macht Session serverseitig ungültig
  - *Prüfen auf*: Rein clientseitiger Logout, Session nach Logout noch gültig
  - *Test*: Session-Token nach Logout abgelehnt

## Eingabevalidierung

- [ ] **Alle Eingaben validiert**: Serverseitige Validierung für ALLE Benutzereingaben vorhanden
  - *Prüfen auf*: Nur clientseitige Validierung, fehlende Validierung bei API-Endpunkten
  - *Quellen*: Formulare, URL-Parameter, Header, Cookies, Dateiuploads, API-Anfragen
  - *Richtlinienreferenz*: ISMS-POL-A.8.28 Abschnitt 2.2

- [ ] **Allowlist-Ansatz verwendet**: Validierung verwendet Positivliste (nicht Negativliste)
  - *Prüfen auf*: Blocklist-Muster ("ablehnen, wenn X enthalten"), unvollständige Blocklisten
  - *Korrekt*: "Akzeptieren nur, wenn Y erfüllt" (z.B. nur alphanumerisch)

- [ ] **SQL-Injection verhindert**: Parametrisierte Abfragen verwendet, keine String-Verkettung
  - *Prüfen auf*: String-Verkettung in SQL (f-Strings, +, .format()), dynamischer Abfrageaufbau
  - *Verifizieren*: Alle Datenbankabfragen nutzen parametrisierte Statements oder ORM sicher
  - *Beispiel*: Siehe ISMS-CTX-A.8.28 Python Abschnitt 2.2, SQL Abschnitt 7

- [ ] **Command-Injection verhindert**: Keine direkten Shell-Aufrufe mit Benutzereingaben
  - *Prüfen auf*: `os.system()`, `subprocess` mit `shell=True`, `eval()`, `exec()`
  - *Verifizieren*: Befehle verwenden Argumentlisten, keine String-Verkettung
  - *Beispiel*: Siehe ISMS-CTX-A.8.28 Python Abschnitt 2.3

- [ ] **Path Traversal verhindert**: Dateipfade validiert, kein Verzeichnisdurchlauf
  - *Prüfen auf*: Direkte Verkettung von Benutzereingaben mit Dateipfaden
  - *Verifizieren*: Pfade werden innerhalb des erlaubten Verzeichnisses aufgelöst und validiert
  - *Beispiel*: Siehe ISMS-CTX-A.8.28 Python Abschnitt 2.4

- [ ] **XML External Entity (XXE) verhindert**: XML-Parsing deaktiviert externe Entities
  - *Prüfen auf*: Standard-XML-Parser-Konfiguration (häufig angreifbar)
  - *Verifizieren*: Externe Entities in der Parser-Konfiguration explizit deaktiviert
  - *Beispiel*: Siehe ISMS-CTX-A.8.28 Java Abschnitt 4.3

- [ ] **Dateiupload-Validierung**: Typ-, Grössen- und Inhaltsvalidierung vorhanden
  - *Prüfen auf*: Reine Erweiterungsprüfung, keine Inhaltsvalidierung, keine Grössenrestriktionen
  - *Verifizieren*: Magic-Number-Validierung, Malware-Scan, Grössenrestriktionen erzwungen

- [ ] **Eingabelängenrestriktionen**: Maximale Länge erzwungen (verhindert Buffer-Overflow, DoS)
  - *Prüfen auf*: Unbegrenzte Eingabelänge, übermässig grosse Grenzwerte

## Ausgabe-Encoding und XSS-Verhinderung

- [ ] **XSS-Verhinderung**: Ausgabe kontextbezogen kodiert (HTML, JavaScript, URL, CSS)
  - *Prüfen auf*: Nicht kodierte Benutzereingaben in HTML, `innerHTML`, `dangerouslySetInnerHTML`
  - *Verifizieren*: Framework-Auto-Escaping genutzt oder manuelles Encoding angewendet
  - *Beispiel*: Siehe ISMS-CTX-A.8.28 JavaScript Abschnitt 3.2

- [ ] **Content-Security-Policy (CSP)-Header**: CSP zur Minderung von XSS-Auswirkungen konfiguriert
  - *Prüfen auf*: Fehlende CSP-Header, zu permissive CSP (`unsafe-inline`, `unsafe-eval`)
  - *Verifizieren*: CSP schränkt Skript-Quellen ein, deaktiviert Inline-Skripte wo möglich

- [ ] **CSRF-Schutz**: Tokens vorhanden bei zustandsverändernden Operationen
  - *Prüfen auf*: Fehlende CSRF-Tokens bei POST/PUT/DELETE/PATCH
  - *Verifizieren*: Tokens serverseitig validiert, Tokens nicht vorhersagbar
  - *Beispiel*: Siehe ISMS-CTX-A.8.28 JavaScript Abschnitt 3.4

- [ ] **HTTP-Sicherheits-Header**: Sicherheits-Header korrekt konfiguriert
  - *Prüfen auf*: Fehlende Header `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security`
  - *Verifizieren*: Header vorhanden und korrekt konfiguriert

## Autorisierung und Zugriffskontrolle

- [ ] **Autorisierung serverseitig erzwungen**: Alle Zugriffskontrollprüfungen auf dem Server
  - *Prüfen auf*: Rein clientseitige Autorisierung (versteckte UI-Elemente), fehlende Serverprüfungen
  - *Verifizieren*: Jede geschützte Ressource verfügt über serverseitige Autorisierungsprüfung

- [ ] **IDOR-Verhinderung**: Benutzereigentümerschaft vor Ressourcenzugriff verifiziert
  - *Prüfen auf*: Direkter ID-Zugriff ohne Eigentümerschaftsprüfung (z.B. `/api/orders/123` für jeden Benutzer zugänglich)
  - *Test*: Kann Benutzer auf Ressourcen anderer Benutzer zugreifen, indem er die ID ändert?

- [ ] **Prinzip der minimalen Rechte**: Operationen nutzen minimal notwendige Berechtigungen
  - *Prüfen auf*: Übermässig permissive Rollen, Admin-Level-Operationen für Benutzeraufgaben
  - *Verifizieren*: Datenbankverbindungen nutzen eingeschränkte Rechte, nicht Root/Admin

- [ ] **Rollenbasierte Zugriffskontrolle (RBAC)**: Rollen korrekt zugewiesen und geprüft
  - *Prüfen auf*: Hartcodierte Benutzer-IDs statt Rollen, fehlende Rollenprüfungen

- [ ] **Privilegieneskalation verhindert**: Keine unsachgemässe Rechteerweiterung möglich
  - *Prüfen auf*: Benutzerkontrollierbare Rollenzuweisungen, fehlende Autorisierung bei Privilegienänderungen
  - *Test*: Kann Benutzer sich selbst die Admin-Rolle zuweisen?

## Kryptographie

- [ ] **Nur genehmigte Algorithmen**: AES-256-GCM, RSA-2048+, ECDSA-256+, SHA-256+
  - *Prüfen auf*: DES, 3DES, RC4, MD5, SHA1, RSA-1024, ECB-Modus, eigene Kryptographie
  - *Richtlinienreferenz*: ISMS-POL-A.8.28 Abschnitt 2.2, ISMS-POL-A.8.24 (Kryptographie)

- [ ] **Keine hartcodierten Geheimnisse**: Zugangsdaten aus Umgebungsvariablen oder Secret-Manager
  - *Prüfen auf*: API-Schlüssel, Passwörter, Tokens, Private Keys im Code
  - *Tools*: Secret-Scanning-Tool verwenden (Gitleaks, TruffleHog, GitHub Secret Scanning)
  - *Massnahme*: Bei Fund sofort Zugangsdaten rotieren

- [ ] **Sichere Zufallsgenerierung**: Kryptographisch sicherer RNG verwendet
  - *Prüfen auf*: `random.random()`, `Math.random()`, zeitbasierte Seeds für Sicherheitstoken
  - *Verifizieren*: Verwendung von `secrets` (Python), `crypto.randomBytes()` (Node.js), `SecureRandom` (Java)
  - *Beispiel*: Siehe ISMS-CTX-A.8.28 sprachspezifische Abschnitte

- [ ] **Verschlüsselungsschlüssel-Management**: Schlüssel sicher gespeichert, nicht im Code oder in Konfigurationsdateien
  - *Prüfen auf*: Verschlüsselungsschlüssel in Umgebungsvariablen (besser, aber nicht ideal), Schlüssel im Code
  - *Verifizieren*: Schlüssel in eigenem Key-Management-Service (AWS KMS, Azure Key Vault, HashiCorp Vault)

- [ ] **TLS/HTTPS erzwungen**: Gesamte sensitive Kommunikation über HTTPS
  - *Prüfen auf*: HTTP für Authentifizierung, Übermittlung sensibler Daten
  - *Verifizieren*: HSTS-Header vorhanden, kein gemischter Inhalt

## Fehlerbehandlung und Protokollierung

- [ ] **Generische Fehlermeldungen für Benutzer**: Keine Stack-Traces, SQL-Fehler oder Dateipfade exponiert
  - *Prüfen auf*: Detaillierte Fehlermeldungen, die Systeminformationen preisgeben
  - *Verifizieren*: Benutzerseitige Fehler sind generisch ("Ein Fehler ist aufgetreten"), Details serverseitig protokolliert

- [ ] **Sicherheitsereignisse protokolliert**: Authentifizierungs-, Autorisierungsfehler, Eingabevalidierungsfehler werden protokolliert
  - *Prüfen auf*: Fehlende Protokollierung von Sicherheitsereignissen
  - *Verifizieren*: Ausreichende Details für Vorfalluntersuchungen (Benutzer, Aktion, Ergebnis, Zeitstempel)
  - *Richtlinienreferenz*: ISMS-POL-A.8.28 Abschnitt 2.2

- [ ] **Keine sensiblen Daten in Logs**: Passwörter, Tokens, personenbezogene Daten aus Logs ausgeschlossen
  - *Prüfen auf*: Vollständige Request-/Response-Protokollierung, Passwort-Logging, Kreditkartennummern
  - *Verifizieren*: Sensible Daten geschwärzt oder ausgeschlossen

- [ ] **Ausnahmen sicher behandelt**: Catch-Blöcke geben keine sensiblen Informationen preis
  - *Prüfen auf*: Leere Catch-Blöcke, an die Benutzeroberfläche propagierte Ausnahmen

## Datenschutz

- [ ] **Sensible Daten verschlüsselt**: Personenbezogene Daten, Finanzdaten, Zugangsdaten im Ruhezustand und bei der Übermittlung verschlüsselt
  - *Prüfen auf*: Speicherung sensibler Daten im Klartext
  - *Richtlinienreferenz*: ISMS-POL-A.8.24 (Kryptographie)

- [ ] **Datensparsamkeit**: Nur notwendige Daten gesammelt und aufbewahrt
  - *Prüfen auf*: Übermässige Datenerhebung, unbefristete Aufbewahrung

- [ ] **Sichere Datenlöschung**: Sensible Daten bei Nichtmehrbedarf sicher gelöscht
  - *Verifizieren*: Nicht nur als gelöscht markiert, sondern tatsächlich entfernt oder kryptographisch gelöscht
  - *Richtlinienreferenz*: ISMS-POL-A.8.10 (Informationslöschung)

## Abhängigkeiten von Drittanbietern

- [ ] **Abhängigkeiten auf Schwachstellen geprüft**: SCA-Tool-Berichte überprüft
  - *Prüfen auf*: Neu eingeführte angreifbare Abhängigkeiten
  - *Verifizieren*: Keine kritischen/hohen Schwachstellen in Abhängigkeiten

- [ ] **Abhängigkeiten aus vertrauenswürdigen Quellen**: Offizielle Repositories verwendet
  - *Prüfen auf*: Abhängigkeiten aus unbekannten oder nicht vertrauenswürdigen Quellen
  - *Verifizieren*: Paketintegrität (Prüfsummen, Signaturen)

- [ ] **Abhängigkeitsversionen fixiert**: Lock-Dateien vorhanden und aktualisiert
  - *Prüfen auf*: Nicht fixierte Versionen, fehlende Lock-Dateien
  - *Verifizieren*: `package-lock.json`, `requirements.txt`, `Gemfile.lock` eingecheckt

---

# Risikobasierte Review-Leitlinien

## Kritische Risikoänderungen

**Auslöser**:

- Änderungen am Authentifizierungssystem
- Änderungen am Autorisierungsmodell
- Kryptographische Implementierungen
- Zahlungsverarbeitung
- Änderungen an der Verarbeitung personenbezogener Daten

**Review-Ansatz**:

- Vollständige Checkliste anwenden (alle Abschnitte)
- Verpflichtender Review durch Security Champion oder Application-Security-Team
- Bedrohungsmodellierungssitzung (bei architektonischer Änderung)
- Penetrationstest (bei wesentlicher Änderung)
- Umfangreiche Tests einschliesslich negativer Testfälle

**Genehmigung**:

- Development Manager + Security Champion + Application Security Lead

## Hochrisikoänderungen

**Auslöser**:

- Neue API-Endpunkte mit Datenzugriff
- Änderungen an Datenbankabfragen
- Dateiupload-Funktionalität
- Integrationen mit Drittanbietern und Datenweitergabe
- Änderungen an Admin-Oberflächen

**Review-Ansatz**:

- Relevante Checklisten-Abschnitte (Fokus auf Eingabevalidierung, Autorisierung, Datenschutz)
- Security-Champion-Review empfohlen
- Sicherheitstests (SAST, DAST)
- Funktionale und sicherheitsbezogene Testfälle

**Genehmigung**:

- Development Manager + Security Champion

## Mittelrisikoänderungen

**Auslöser**:

- UI-Änderungen mit Benutzereingaben
- Report-Generierung mit Datenzugriff
- Konfigurationsänderungen mit Sicherheitsauswirkung
- Änderungen an Protokollierung oder Überwachung

**Review-Ansatz**:

- Gezielte Checklisten-Elemente (Eingabevalidierung, XSS-Verhinderung)
- Peer-Review mit Sicherheitsbewusstsein
- Automatisiertes Sicherheitsscanning

**Genehmigung**:

- Peer-Reviewer mit Sicherheitsschulung

## Niedrigrisikoänderungen

**Auslöser**:

- Refactoring ohne Funktionsänderungen
- Dokumentationsaktualisierungen
- Reine Teständerungen
- UI-Styling (CSS) ohne Logikänderungen

**Review-Ansatz**:

- Standard-Code-Review
- Keine unbeabsichtigten Sicherheitsauswirkungen verifizieren
- Kurze Prüfung auf versehentlich eingeführte Probleme

**Genehmigung**:

- Standard-Peer-Review

---

# Gängige Muster und Anti-Muster

## Sichere Muster (fördern)

**Eingabevalidierungs-Muster**:
```python
# Allowlist-Validierung
ALLOWED_FIELDS = {'name', 'email', 'age'}
def validate_input(data):
    if not all(key in ALLOWED_FIELDS for key in data.keys()):
        raise ValidationError("Ungültiges Feld")
    # Weitere Validierung...
```

**Autorisierungs-Muster**:
```python
# Eigentümerschaftsprüfung vor Ressourcenzugriff
def get_order(order_id, current_user):
    order = Order.query.get(order_id)
    if order.user_id != current_user.id:
        raise Forbidden("Zugriff verweigert")
    return order
```

**Sicheres Konfigurationsmuster**:
```python
# Umgebungsbasierte Konfiguration
API_KEY = os.environ.get('API_KEY')
if not API_KEY:
    raise ConfigError("API_KEY muss gesetzt sein")
```

## Anti-Muster (vermeiden)

**String-Verkettung für SQL**:
```python
# ANTI-MUSTER — SQL-Injection-Schwachstelle
query = f"SELECT * FROM users WHERE id = {user_id}"
```

**Clientseitige Autorisierung**:
```javascript
// ANTI-MUSTER — Autorisierung muss serverseitig sein
if (user.role === 'admin') {
  showAdminPanel();  // Nur clientseitig, leicht zu umgehen
}
```

**Schwaches Password-Hashing**:
```python
# ANTI-MUSTER — Schwaches Hashing
import hashlib
hash = hashlib.md5(password.encode()).hexdigest()
```

---

# Review-Dokumentation

## Vorlage für Review-Kommentare

```
**Sicherheitsproblem: [Problem-Typ]**

**Schweregrad**: [Kritisch/Hoch/Mittel/Niedrig]

**Problem**: [Kurze Beschreibung des Sicherheitsproblems]

**Speicherort**: [Datei und Zeilennummer]

**Risiko**: [Was ein Angreifer tun könnte]

**Empfehlung**: [Wie zu beheben]

**Referenz**: ISMS-POL-A.8.28 Abschnitt [X.Y] / Checklisten-Element [4.X]

**Beispiel**: [Codebeispiel oder Link zu ISMS-CTX-A.8.28]
```

## Kommentar zur Sicherheitsgenehmigung

```
**Sicherheitsreview abgeschlossen**

Geprüft von: [Name des Security Champions]
Datum: [TT.MM.JJJJ]

Angewandte Checklisten-Abschnitte:

- [X] Authentifizierung (4.1)
- [X] Eingabevalidierung (4.2)
- [X] Autorisierung (4.4)

Befunde:

- [Problem 1]: Behoben in Commit [Hash]
- [Problem 2]: Risiko akzeptiert mit Begründung [Link]

**Zur Zusammenführung freigegeben** ohne offene Sicherheitsprobleme.
```

---

# Eskalationsverfahren

## Wann zu eskalieren

**An Security Champion**:

- Unklare Anwendung der Checkliste
- Validierung eines Sicherheitsmusters erforderlich
- Mehrere Checklisten-Elemente nicht erfüllt
- Schulungs- oder Anleitungsbedarf

**An Application-Security-Team**:

- Vermutete kritische/hohe Schwachstelle
- Sicherheitsbedenken auf Architekturebene
- Bedarf an Bedrohungsmodellierung
- Tool-Befunde erfordern Expertenvalidierung
- Empfehlung eines Penetrationstests

## Eskalationskanäle

| Problem-Typ | Kanal | Reaktionszeit |
|-------------|-------|---------------|
| **Frage während des Reviews** | Slack #security-champions | < 4 Stunden (Geschäftszeiten) |
| **Sicherheitsbedenken (nicht dringend)** | Slack #appsec | < 1 Werktag |
| **Sicherheitsschwachstelle (Hoch)** | E-Mail security@[organisation].com + Slack | < 4 Stunden |
| **Sicherheitsschwachstelle (Kritisch)** | Incident-Response-Prozess | Sofort |

---

# Dokumentenpflege

**Aktualisierungsfrequenz**: Vierteljährlich oder wenn:

- OWASP Top 10 aktualisiert wird
- Neue Schwachstellenmuster identifiziert werden
- Sich der organisatorische Technologie-Stack ändert
- Richtlinienanforderungen ändern (Aktualisierungen von ISMS-POL-A.8.28)

**Verantwortlicher**: Application Security Lead

**Überprüfungsauslöser**:

- Grössere Sicherheitsvorfälle, die Checklisten-Aktualisierungen erfordern
- Entwickler-Feedback zu Klarheit oder Vollständigkeit der Checkliste
- Änderungen bei Sicherheitstools-Integrationen
- Feedback zur Schulungseffektivität

**Zusammenarbeit**:

- Security Champions validieren die praktische Anwendbarkeit
- Entwicklungsteams geben Feedback zur Benutzerfreundlichkeit
- Application-Security-Team stellt technische Korrektheit sicher

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | Application Security Lead | Erstveröffentlichung — Code-Review-Referenz aus konsolidierter Richtlinie extrahiert |

---

**ENDE VON ISMS-REF-A.8.28**

*Dieses technische Referenzdokument unterstützt die Umsetzung von ISMS-POL-A.8.28. Verbindliche Anforderungen sind in der Richtlinie, nicht in diesem Dokument, festgelegt.*

**DIESES DOKUMENT IST NICHT BESTANDTEIL DES ISMS.**

<!-- QA_VERIFIED: 2026-03-29 -->
