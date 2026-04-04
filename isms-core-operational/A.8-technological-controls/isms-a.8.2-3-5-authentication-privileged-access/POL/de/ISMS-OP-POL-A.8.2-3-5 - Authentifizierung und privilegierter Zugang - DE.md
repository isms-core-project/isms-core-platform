<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.2-3-5-DE:operational:OP-POL:a.8.2-3-5 -->
**ISMS-OP-POL-A.8.2-3-5 — Authentifizierung und privilegierter Zugang**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Authentifizierung und privilegierter Zugang |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.2-3-5 |
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
| 1.0 | [Datum] | ISB | Erste operative Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt von**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Controls A.8.2, A.8.3, A.8.5 — Privilegierte Zugriffsrechte, Informationszugangsbeschränkung, sichere Authentifizierung

**Verwandte Annex-A-Controls**:

| Control | Bezug zu Authentifizierung und privilegiertem Zugang |
|---------|-----------------------------------------------------|
| A.5.3 Aufgabentrennung | Aufgabentrennung wird durch Zugangsbeschränkungen und abgestufte Berechtigungen durchgesetzt |
| A.5.15–18 Zugangssteuerung und Identitätsmanagement | Identitätslebenszyklus speist Authentifizierung; Zugriffsrechte definieren Beschränkungen |
| A.5.17 Authentifizierungsinformationen | Zugangsdatenverwaltung für Passwörter, Tokens und Geheimnisse |
| A.5.24–28 Incident Management | Kompromittierung von Zugangsdaten löst Incident-Response aus |
| A.8.1 Endgeräte | Endgerätesicherheit unterstützt Authentifizierung (Gerätevertrauen, Verschlüsselung) |
| A.8.9 Konfigurationsmanagement | Systemkonfigurationen setzen Authentifizierungs- und Zugangsbaselines durch |
| A.8.15 Protokollierung | Authentifizierungsereignisse und privilegierte Aktionen fliessen in zentrale Protokollierung |
| A.8.16 Überwachungsaktivitäten | Echtzeit-Überwachung von Authentifizierungsfehlern und privilegiertem Zugang |
| A.8.20–22 Netzwerksicherheit | Netzwerksegmentierung unterstützt Zugangszonen-Durchsetzung |
| A.8.24 Einsatz von Kryptografie | Kryptografischer Schutz von Zugangsdaten, Tokens und Sitzungen |

**Verwandte interne Richtlinien**:

- Richtlinie zur Identitäts- und Zugangsverwaltung
- Endgerätesicherheitsrichtlinie
- Netzwerksicherheitsrichtlinie
- Richtlinie zum Einsatz von Kryptografie
- Protokollierungsrichtlinie
- Richtlinie zu Überwachungsaktivitäten (A.8.16)
- Incident-Management-Richtlinie

---

# Richtlinie zur Authentifizierung und zum privilegierten Zugang

## Zweck

Zweck dieser Richtlinie ist es sicherzustellen, dass Authentifizierungsmechanismen entsprechend der Sensibilität der zugreifenden Informationen und Systeme implementiert werden, dass privilegierte Zugriffsrechte gemäss dem Prinzip der minimalen Rechtevergabe eingeschränkt und verwaltet werden, und dass technische Zugangskontrollen autorisierte Zugangsschranken durchsetzen.

Diese Richtlinie unterstützt das Schweizer nDSG (revDSG) und die Datenschutzverordnung (DSV) durch die Implementierung technischer und organisatorischer Massnahmen entsprechend dem Risiko zum Schutz personenbezogener Daten (einschliesslich besonders schützenswerter Personendaten) durch Authentifizierungs- und Zugangskontrollen. Wo die Organisation Daten von Personen im EU/EWR-Raum verarbeitet, gelten auch DSGVO-Anforderungen. Starke Authentifizierung und privilegiertes Zugangsverwaltung sind zentrale technische Massnahmen zur Nachweisführung der Compliance mit Datenschutzverpflichtungen im Rahmen beider Regelwerke.

## Geltungsbereich

Alle Mitarbeitenden und Drittnutzer.

Alle Authentifizierungsmechanismen, privilegierten Konten und technischen Zugangskontrollen über Systeme, Plattformen und Umgebungen, die der Organisation gehören oder von ihr betrieben werden und als im Geltungsbereich der ISO-27001-Scope-Erklärung befindlich gelten.

Dies umfasst On-Premises-, Cloud-, Hybrid- und SaaS-Umgebungen.

## Grundsatz

Authentifizierung und Zugangskontrollen werden nach dem Prinzip der gestaffelten Sicherheit (Defence in Depth) implementiert. Nutzer werden positiv identifiziert und authentifiziert, bevor sie Zugang erhalten. Privilegierter Zugang wird nur mit dokumentierter Genehmigung und auf das für die Aufgabe erforderliche Minimum beschränkt gewährt. Zugang wird standardmässig verweigert und nur auf ausdrückliche Autorisierung gewährt.

Alle Authentifizierungs- und Zugangsentscheidungen müssen risikobasiert sein und die Klassifizierung der Informationen und die Kritikalität des Systems berücksichtigen.

---

## IAM-Technologie-Infrastruktur

Die folgende Tabelle dokumentiert den IAM-Technologie-Stack der Organisation. Die tatsächliche Toolauswahl ist organisationsspezifisch; Beispiele dienen als Orientierung:

| Funktion | Lösung | Eigentümer | Primäre Nutzung |
|----------|--------|------------|-----------------|
| **Identity Provider (IdP)** | [z.B. Azure Active Directory (Entra ID), Okta, Google Workspace, JumpCloud] | IT-Betrieb | Zentrale Authentifizierung, SSO, Nutzerlebenszyklusverwaltung |
| **Privileged Access Management (PAM)** | [z.B. CyberArk, Delinea (Thycotic), BeyondTrust, Azure AD PIM] | IT-Sicherheit | Passwort-Vaulting, Sitzungsaufzeichnung, JIT-Zugang, Credential-Rotation |
| **Multi-Faktor-Authentifizierung (MFA)** | [z.B. Azure MFA, Okta Verify, Duo Security, YubiKey (FIDO2)] | IT-Betrieb | Zweiter Faktor für alle Nutzer |
| **Unternehmens-Passwort-Manager** | [z.B. 1Password Business, Bitwarden Teams, LastPass Enterprise] | IT-Sicherheit | Sichere Speicherung gemeinsamer Zugangsdaten; interim bis PAM für Service-Accounts |
| **Single Sign-On (SSO)** | [Integriert mit IdP via SAML 2.0 / OIDC] | IT-Betrieb | Anwendungsauthentifizierung über zentralen IdP |
| **Sitzungsaufzeichnung** | [z.B. PAM-nativ, CyberArk PSM, Teleport, Windows Defender for Identity] | IT-Sicherheit | Aufzeichnung und Prüfung von Tier-0-privilegierten Sitzungen |
| **Kompromittierte-Zugangsdaten-Screening** | [z.B. Azure AD Password Protection, Have I Been Pwned API, Enzoic] | IT-Sicherheit | Verhinderung der Nutzung bekannt verletzter Passwörter |
| **Identity Governance** | [z.B. Azure AD Access Reviews, SailPoint, Saviynt oder manuelle Tabellen-Workflow] | IT-Sicherheit | Zugangs-Zertifizierungs-Kampagnen, Compliance-Berichterstattung |

**Integrationspunkte**: IdP muss mit HR-System für Joiner/Mover/Leaver-Automatisierung integriert sein. PAM, IdP und SIEM müssen für zentrale Überwachung integriert sein. MFA muss über IdP-Conditional-Access-Richtlinien durchgesetzt werden. Sitzungsaufzeichnungsprotokolle müssen an SIEM weitergeleitet werden.

---

## Authentifizierungsanforderungen

### Passwortstandards

Der Zugang zu Systemen und Informationen wird durch Passwörter oder stärkere Mechanismen authentifiziert. Die Organisation muss folgende Passwortstandards, abgestimmt auf NIST SP 800-63B, durchsetzen:

| Anforderung | Standard |
|-------------|----------|
| Mindestlänge | 12 Zeichen (14 für privilegierte Konten) |
| Komplexität | Länge über Komplexität; keine obligatorischen Zusammensetzungsregeln |
| Maximallänge | Systeme müssen mindestens 64 Zeichen akzeptieren |
| Zeichenunterstützung | Alle druckbaren ASCII-Zeichen (inkl. Leerzeichen) und Unicode müssen akzeptiert werden |
| Screening | Passwörter müssen beim Setzen/Ändern und monatlich danach gegen bekannte kompromittierte/verletzten Zugangsdaten-Datenbanken validiert werden |
| Rotation | Nur ereignisbasiert — bei vermutetem oder bestätigtem Kompromiss; periodische erzwungene Rotation ist nicht erforderlich |
| Initialpasswörter | Müssen bei Erstnutzung geändert werden |
| Standardpasswörter | Vom Hersteller gelieferte und Standardpasswörter müssen unmittelbar nach der Installation geändert werden |
| Teilen | Passwörter dürfen nicht generisch, geteilt oder auf Gruppenebene gesetzt sein |
| Vertraulichkeit | Passwörter müssen vertraulich gehalten und nicht aufgeschrieben werden |
| Anzeige | Passwörter dürfen bei der Eingabe nicht angezeigt werden |
| Code | Passwörter dürfen nicht in Skripten, Code oder Makros kodiert oder eingeschlossen sein |
| Übertragung | Passwörter müssen bei der Übertragung über Netzwerke verschlüsselt sein |
| Speicherung | Passwörter müssen mit genehmigten kryptografischen Hash-Funktionen (bcrypt, scrypt, Argon2 oder PBKDF2) gespeichert und niemals im Klartext oder mit reversibler Verschlüsselung gespeichert werden |
| Sperrung | Systeme müssen Nutzer nach 6 fehlgeschlagenen Zugriffsversuchen sperren |
| Historie | Eine Passworthistorie von mindestens 24 vorherigen Passwörtern muss geführt werden, um Wiederverwendung zu verhindern |
| Passwort-Manager | Die Nutzung von von der Organisation genehmigten Passwort-Managern wird empfohlen |

**Implementierungsoptionen für kompromittiertes-Zugangsdaten-Screening**:

| Option | Implementierung | Hinweise |
|--------|----------------|---------|
| **Azure AD Password Protection** | Globale verbotene Passwortliste + benutzerdefinierte Liste aktivieren; lokal und on-premises durchsetzen (via DC-Agenten) | Empfohlen für Microsoft-Umgebungen |
| **Have I Been Pwned (HIBP) API** | k-Anonymitätsmodell (nur erste 5 Zeichen des Hash gesendet); Prüfung beim Setzen/Ändern und monatlicher Scan | Open-Source; erfordert Integrationsaufwand |
| **Drittanbieter-Lösung** | Enzoic, Specops Password Policy oder gleichwertig | Kommerziell; umfasst typischerweise zusätzliche Passwortrichtlinien-Durchsetzung |

In Verletzungsdatenbanken gefundene Passwörter müssen beim Setzen/Ändern abgelehnt und bei monatlichen Scans zur erzwungenen Änderung markiert werden. Screening-Abdeckungskennzahl: Prozentsatz der Passwort-Setz-/Änderungsereignisse, die gegen Verletzungsdatenbanken validiert werden (Ziel: 100%).

### Multi-Faktor-Authentifizierung (MFA)

Multi-Faktor-Authentifizierung muss erforderlich sein für:

- Alle privilegierten und Administrator-Konten.
- Alle Remote-Zugänge zu Organisationsnetzwerken und Cloud-Diensten.
- Alle extern zugänglichen Anwendungen mit Authentifizierung.
- Alle Zugänge zu Systemen, die vertrauliche oder personenbezogene Daten verarbeiten.
- Alle Cloud-Plattform-Administrationskonsolen.

**Akzeptable MFA-Methoden** (in Reihenfolge der Präferenz):

| Methode | Phishing-Resistenz | Empfohlener Einsatz |
|---------|-------------------|---------------------|
| Hardware-Sicherheitsschlüssel (FIDO2/WebAuthn) | Hoch | Erforderlich für Tier 0; empfohlen für alle privilegierten Konten |
| Authenticator-Apps (TOTP) | Mittel | Akzeptabel für Tier 1/2 und Standardnutzer |
| Push-Benachrichtigungen (mit Nummernabgleich) | Mittel | Akzeptabel, wo Nummernabgleich aktiviert ist |
| SMS/Sprach-OTP | Niedrig | Nur wo andere Methoden technisch nicht umsetzbar sind (Legacy-Systeme) |

SMS-basiertes OTP sollte wo möglich abgelöst werden aufgrund bekannter Schwachstellen (SIM-Swapping, Abfangen). Systeme, die ausschliesslich auf SMS-basierter MFA beruhen, müssen im Risikoregister mit Migrationsplan dokumentiert werden.

**MFA-Abdeckungsziele**:

- Privilegierte Nutzer: 100% MFA-Einschreibung.
- Alle Nutzer: 95%+ MFA-Einschreibung innerhalb von 12 Monaten nach Richtlinienannahme.
- Remote-Zugang: 100% MFA-Durchsetzung.

Systeme, die MFA nicht unterstützen können, müssen im Risikoregister mit technischer Begründung, Ausgleichsmassnahmen (z.B. Netzwerksegmentierung, erweiterte Überwachung, IP-Einschränkung) und jährlich überprüfter ISB-genehmigter Risikoakzeptanz dokumentiert werden.

### Single Sign-On (SSO)

Die Organisation muss zentrales SSO über den Identity Provider mit SAML 2.0 oder OIDC mit folgenden Zielen implementieren:

- Neue SaaS-Anwendungen: SSO-Integration vor Beschaffungsgenehmigung erforderlich.
- Bestehende Anwendungen: SSO-Integration basierend auf untenstehendem Risikostufen-Tier priorisiert.
- Ziel: 80%+ SaaS-Anwendungsintegration innerhalb von 12 Monaten; 90%+ innerhalb von 24 Monaten.

**SSO-Integrationsprioritätsstufen**:

| Priorität | Kriterien | Zeitrahmen |
|-----------|----------|------------|
| **Priorität 1** | Verarbeitet vertrauliche Daten; >50 Nutzer; internet-zugänglich; Cloud-Infrastrukturkonsolen | 30 Tage |
| **Priorität 2** | Verarbeitet interne Daten; 20–50 Nutzer; Anwendungen mit privilegiertem Zugang | 90 Tage |
| **Priorität 3** | <20 Nutzer; begrenzte Datenexposition; seltene Nutzung | 180 Tage |
| **Priorität 4** | Legacy-Anwendungen mit SSO-Einschränkungen; zur Stilllegung geplante Apps; Anbieter ohne SSO-Unterstützung | 12 Monate (oder dokumentierte Ausnahme) |

Ein SSO-Integrationsinventar muss geführt werden, das jede Anwendung, ihren SSO-Status (integriert / in Bearbeitung / Ausnahme), Prioritätsstufe und Zieldatum auflistet. Das Inventar muss vierteljährlich überprüft werden.

Anwendungen ohne SSO-Fähigkeit erfordern eine dokumentierte Ausnahme mit Ausgleichsmassnahmen (z.B. individuelle MFA, erweiterte Überwachung, Passwort-Manager-Durchsetzung).

### Authentifizierungsprotokollierung

Alle Authentifizierungsereignisse müssen protokolliert und an das zentrale Protokollierungs-SIEM weitergeleitet werden:

- Erfolgreiche und fehlgeschlagene Authentifizierungsversuche.
- MFA-Einschreibung und Methodenänderungen.
- Passwortänderungen und -zurücksetzungen.
- Kontosperrungen und -entsperrungen.
- Sitzungserstellung und -beendigung.

Authentifizierungsprotokolle müssen mindestens 12 Monate aufbewahrt werden.

**Authentifizierungsüberwachungs-Alarmregeln**:

| Alarmregel | Schwelle | Schweregrad | Reaktions-SLA |
|------------|----------|-------------|---------------|
| Brute-Force-Angriff | ≥10 fehlgeschlagene Logins von einer IP in 5 Minuten | Hoch | 1 Stunde |
| Credential Stuffing | ≥5 fehlgeschlagene Logins über mehrere Konten von einer IP in 10 Minuten | Hoch | 1 Stunde |
| Unmögliche Reise | Erfolgreicher Login von Standorten >500 km entfernt innerhalb 1 Stunde | Hoch | 1 Stunde |
| Privilegiertes Konto — neues Gerät | Tier-0/1-Login von in 30 Tagen nicht gesehenem Gerät | Mittel | 4 Stunden |
| Privilegiertes Konto — unerwarteter Standort | Tier-0/1-Login aus Land ausserhalb der genehmigten Liste | Kritisch | Sofort |
| Service-Account interaktiver Login | Service-Account für RDP/SSH/Konsolenlogin verwendet | Hoch | 2 Stunden |
| MFA-Umgehungsversuch | Authentifizierung ohne erforderliche MFA | Hoch | 1 Stunde |
| Break-Glass-Kontonutzung | Notfall-/Break-Glass-Konto authentifiziert | Kritisch | Sofort; 24-Stunden-Überprüfung |
| Kontosperrungs-Spitze | ≥10 Sperrungen in der gesamten Umgebung in 1 Stunde | Mittel | Gleichtägige Untersuchung |

**Genehmigte geografische Standorte**: Schweiz, [weitere Länder gemäss Geschäftstätigkeit]. Logins aus nicht genehmigten Ländern lösen Alarme gemäss obiger Tabelle aus.

Alarmregeln müssen vierteljährlich überprüft und angepasst werden, um Falsch-Positiv-Raten zu reduzieren. Untersuchungsworkflow: Alarm empfangen → validieren (wahr/falsch positiv) → mit Kontext anreichern → eskalieren bei Bestätigung → Ergebnis dokumentieren.

### Anforderungen an Authentifizierungssysteme

Das Hauptzugangs-Authentifizierungssystem muss:

- System- oder Anwendungskennungen erst nach erfolgreichem Abschluss des Anmeldevorgangs anzeigen.
- Eine allgemeine Hinweiswarnung anzeigen, dass das System nur von autorisierten Nutzern zugegriffen werden darf.
- Keine Hilfemeldungen während des Anmeldeverfahrens anzeigen, die einem nicht autorisierten Nutzer helfen würden.
- Die Anmeldeinformationen erst bei vollständiger Eingabe aller Daten validieren. Tritt ein Fehlerzustand auf, darf das System nicht anzeigen, welcher Teil der Daten korrekt oder falsch ist.
- Gegen Brute-Force-Anmeldeversuche schützen.
- Erfolgreiche und fehlgeschlagene Versuche protokollieren.
- Ein Sicherheitsereignis auslösen, wenn ein potenzieller versuchter oder erfolgreicher Verstoss gegen Anmeldekontrollen erkannt wird.
- Einzugebendes Passwort nicht anzeigen.
- Passwörter nicht im Klartext über ein Netzwerk übertragen.
- Inaktive Sitzungen nach einem definierten Inaktivitätszeitraum beenden.
- Verbindungszeiten für Hochrisikoapplikationen einschränken, um zusätzliche Sicherheit zu bieten.

---

## Privilegiertes Zugangsverwaltung

### Grundsätze für privilegierten Zugang

Privilegierter Zugang muss basierend auf folgenden Grundsätzen eingeschränkt sein:

- **Minimale Rechtevergabe**: Minimaler Zugang, der für die Ausführung von Arbeitsaufgaben erforderlich ist.
- **Need-to-Know**: Zugang nur zu Informationen, die für spezifische Aufgaben benötigt werden.
- **Aufgabentrennung**: Kritische Funktionen auf mehrere Personen aufgeteilt.
- **Zeitlich begrenzter Zugang**: Just-in-Time (JIT)-Bereitstellung wo unterstützt.

### Privilegiertes Konto-Klassifizierung — Admin-Tiering-Modell

Die Organisation muss gestufte Administration implementieren, um die Auswirkung kompromittierter Zugangsdaten zu begrenzen:

| Tier | Geltungsbereich | Beispiele | Anforderungen |
|------|----------------|-----------|---------------|
| **Tier 0** | Domäne/Unternehmen | Domain-Admins, Azure/M365 Global Admin, PKI, SIEM | Hardware-MFA (FIDO2); dedizierte Admin-Workstation; Sitzungsaufzeichnung obligatorisch |
| **Tier 1** | Server/Anwendung | Server-Admins, DBAs, Cloud-Abonnement-Admins | MFA erforderlich; dedizierte Admin-Workstation empfohlen |
| **Tier 2** | Workstation/Endgerät | Desktop-Support, Helpdesk mit lokalem Admin | MFA erforderlich; Standard-Workstation akzeptabel |

**Tier-Isolationsanforderungen**:

- Tier-0-Konten dürfen sich niemals auf Tier-1- oder Tier-2-Systemen authentifizieren.
- Tier-1-Konten dürfen sich niemals auf Tier-2-Systemen authentifizieren.
- Pro Tier sind separate Zugangsdaten zu verwenden (z.B. j.mueller.t0, j.mueller.t1).
- Tägliche Arbeitsaktivitäten (E-Mail, Web-Browsing) dürfen nicht auf dedizierten Admin-Workstations durchgeführt werden.

**Tier-Isolations-Durchsetzung**:

Technische Controls müssen Tier-Grenzen durchsetzen. Folgende Implementierungsoptionen stehen je nach Identitätsplattform der Organisation zur Verfügung:

*Conditional Access (Azure AD / Entra ID oder gleichwertig):*

| Richtlinie | Ziel | Durchsetzung |
|------------|------|-------------|
| Phishing-resistente MFA für Tier 0 erforderlich | Tier-0-Konten, alle Cloud-Apps | Nur FIDO2/WebAuthn; andere MFA-Methoden blockieren |
| Tier 0 von Nicht-Admin-Apps blockieren | Tier-0-Konten | Zugang zu Office 365, SharePoint, OneDrive, Teams blockieren |
| Kompatibles Gerät für Admin-Zugang erforderlich | Tier-0/1-Konten | Kompatibles oder hybrid-verbundenes Gerät erforderlich |
| Legacy-Authentifizierung blockieren | Alle Nutzer | IMAP, POP3, SMTP AUTH blockieren |
| Zugang aus nicht genehmigten Ländern blockieren | Alle Nutzer (Break-Glass ausgenommen) | Erlauben: CH + genehmigte Länder; alle anderen blockieren |
| MFA für alle Nutzer erforderlich | Alle Nutzer, alle Cloud-Apps | Anmeldefrequenz: 90 Tage |
| Hochrisiko-Anmeldungen blockieren | Alle Nutzer (erfordert Azure AD P2) | Vom Identity Protection als hohes Risiko eingestufte Anmeldungen blockieren |
| Sitzungs-Timeout für sensible Anwendungen | Finanzen, HR, Kundendatenbanken | Re-Authentifizierung alle 4 Stunden |

*On-Premises-Durchsetzung:*

- GPO-Anmeldebeschränkungen: Tier-0-Konten an lokalem Login auf Tier-1/2-Systemen verweigern; Tier-1-Konten auf Tier-2-Workstations verweigern.
- Netzwerksegmentierung: Tier-0-Admin-Workstations auf dediziertem VLAN; Tier 1 auf separatem VLAN; Standardnutzer auf Corporate-VLAN. Firewall-Regeln beschränken Cross-Tier-Zugang.

*SIEM-Alarmregeln für Tier-Verletzungen:*

| Alarm | Schweregrad | Benachrichtigung |
|-------|-------------|-----------------|
| Tier-0-Authentifizierung auf Tier-1/2-System | Kritisch | ISB sofort |
| Tier-1-Authentifizierung auf Tier-2-System | Hoch | IT-Sicherheitsmanager |
| Privilegiertes Konto von nicht genehmigtem Standort | Hoch | IT-Sicherheitsteam |

**Privilegierte Zugangs-Workstations (PAW)**:

| Tier | PAW-Anforderung |
|------|----------------|
| **Tier 0** | PAW obligatorisch |
| **Tier 1** | PAW empfohlen; obligatorisch für Phase 2 |
| **Tier 2** | Standard-Workstation akzeptabel |

*PAW-Konfigurationsbaseline (Tier 0/1):*

- **Hardware**: Dediziertes physisches Gerät; Vollplatten-Verschlüsselung; TPM 2.0; Secure Boot aktiviert.
- **Betriebssystem**: Gehärtet nach CIS Benchmark Level 2; automatische Updates; keine vom Nutzer installierte Software (Anwendungs-Allowlisting durchgesetzt).
- **Netzwerk**: Dediziertes Admin-VLAN; Firewall-Regeln beschränken Verbindungen auf Verwaltungsziele; kein allgemeines Internet-Browsing.
- **Anwendungen**: Nur RDP-/SSH-Client, PAM-Client und Admin-Tools. E-Mail, Web-Browser, Office-Suite und Collaboration-Tools (Teams/Slack) sind verboten.
- **Zugangskontrolle**: Lokaler Admin deaktiviert; PAM-Zugangsdaten erforderlich; MFA durchgesetzt; 10-Minuten-Bildschirmsperre.
- **Überwachung**: EDR-Agent installiert; alle Aktivitäten an SIEM weitergeleitet; Alarme bei nicht autorisierter Software, Verbindungen oder Browsing-Versuchen.

**Stufenweise Einführung**: Phase 1 (Jahr 1): Tier-0-PAWs eingeführt. Phase 2 (Jahr 2): Tier-1-PAWs eingeführt. Ausgleichsmassnahmen müssen für jeden Zeitraum dokumentiert werden, in dem PAWs noch nicht vorhanden sind (z.B. erweiterte Überwachung, dedizierte VMs, eingeschränkte Admin-Konten auf Standard-Workstations).

**Einführungsstatuserfassung**: Der aktuelle Einführungsstand (Planung, Pilot, teilweise Durchsetzung, vollständige Durchsetzung) muss für jeden Tier mit Ausgleichsmassnahmen für nicht durchgesetzte Tiers und Zielabschlussdaten dokumentiert sein.

### Privilegiertes Kontoverwaltung

Alle privilegierten Konten müssen:

- Nicht geteilt oder generisch sein (ein Nutzer, ein privilegiertes Konto pro Tier).
- Klar identifizierbar sein (Namenskonvention dokumentiert und durchgesetzt).
- Auf anomale Aktivitäten protokolliert und überwacht werden.
- Wo möglich zeitgebunden sein (JIT-Zugang gegenüber dauerhaften Berechtigungen bevorzugt).
- In einem gepflegten Privilegiertes-Konto-Inventar mit Eigentümer, Tier, Zweck und Überprüfungsdatum registriert sein.

### PAM-Lösung

Die Organisation muss Privilegiertes-Zugangs-Controls implementieren, die eine dedizierte PAM-Lösung (siehe IAM-Infrastrukturtabelle) oder gleichwertige manuelle Controls umfassen können:

| Fähigkeit | Anforderung | Stufenweiser Ansatz für KMUs |
|-----------|-------------|------------------------------|
| **Passwort-Vaulting** | Privilegierte Passwörter im genehmigten Vault gespeichert, nicht im Klartext | Phase 1: Für Tier-0-Konten implementieren; auf Tier 1/2 ausdehnen |
| **Sitzungsaufzeichnung** | Tier-0-Sitzungen aufgezeichnet; Tier-1-Aufzeichnung empfohlen | Phase 1: Tier 0 obligatorisch; Tier 1 bei PAM-Ausdehnung |
| **Just-in-Time-Zugang** | Temporäre Berechtigungserweiterung mit automatischer Rücknahme | Phase 2: Implementieren wo PAM JIT-Workflows unterstützt |
| **Credential-Rotation** | Service-Account-Passwörter gemäss untenstehendem Plan rotiert | Phase 1: Manuelle Rotation mit dokumentiertem Nachweis |

Wo eine dedizierte PAM-Lösung noch nicht eingeführt ist, müssen Ausgleichsmassnahmen dokumentiert werden (z.B. manuelle Credential-Rotation, gemeinsamer Passwort-Manager mit Audit-Trail, alternative Sitzungsprotokollierung via SIEM).

**Anforderungen an Credential-Rotation**:

| Kontotyp | Rotationsfrequenz |
|----------|------------------|
| Service-Accounts (Tier 0) | Maximal 90 Tage |
| Service-Accounts (Tier 1/2) | Maximal 180 Tage |
| Break-Glass-Konten | Nach jeder Nutzung + maximal 365 Tage |
| Geteilte Admin-Konten (abgeraten) | 90 Tage; Migration zu individuellen Konten mit ISB-Ausnahme |

Alle Zugangsdaten müssen bei vermutetem oder bestätigtem Kompromiss sofort rotiert werden, unabhängig vom Plan.

### Service-Account-Verwaltung

Service-Accounts müssen durch einen definierten Lebenszyklus verwaltet werden:

1. **Antrag und Genehmigung**: Antragsteller stellt Antrag über Ticketing-System. IT-Sicherheitsmanager genehmigt innerhalb von 3 Arbeitstagen. Genehmigungskriterien: dokumentierte Geschäftsbegründung, definierte Minimalberechtigungen, designierter Eigentümer, designiertes Tier.
2. **Erstellung**: Namenskonvention `svc-[System]-[Zweck]` (z.B. `svc-erp-backup`). Mindestens 20 Zeichen langes Zufallspasswort. Zugangsdaten sicher über PAM-Vault oder gleichwertig geliefert (niemals per E-Mail oder Chat).
3. **Inventar**: Alle Service-Accounts registriert mit: Kontoname, Zweck, Eigentümer, Tier, Berechtigungen, Zugangsdaten-Standort (Vault-Referenz), letztes Rotationsdatum, nächstes Rotationsdatum.
4. **Zugangsprüfung**: Vierteljährliche Bestätigung durch Anwendungseigentümer. Ungenutzte Konten (keine Authentifizierung in 90 Tagen) sofort deaktiviert und nach 90-tägiger Aufbewahrung gelöscht.
5. **Credential-Rotation**: Automatisiert via PAM wo unterstützt; manuelle Rotation im Inventar dokumentiert wo PAM nicht verfügbar.
6. **Stilllegung**: Bei Serviceeinstellung Service-Account sofort deaktiviert, Zugangsdaten rotiert und Konto nach 90-tägiger Aufbewahrung gelöscht.

**Service-Account-Überwachung**: SIEM-Alarmregeln müssen interaktiven Login durch Service-Accounts, Authentifizierung von unerwarteten Standorten und fehlgeschlagene Authentifizierungsversuche erkennen. Ein vierteljährlicher Discovery-Scan identifiziert undokumentierte Service-Accounts.

### Just-In-Time (JIT) Privilegierter Zugang

JIT-Zugang wird gegenüber dauerhaften Berechtigungen bevorzugt. Folgender Workflow gilt je nach verfügbaren Tools:

**PAM-basiertes JIT** (bevorzugt):

1. Nutzer beantragt erhöhte Berechtigung über PAM-Portal mit Begründung.
2. Genehmigung: automatisch für vorab genehmigte Aufgaben; Manager-/IT-Sicherheits-Genehmigung für andere.
3. PAM stellt zeitlich begrenzte Zugangsdaten aus (Standard: 4 Stunden; Maximum: 8 Stunden).
4. Sitzung aufgezeichnet (Tier 0 obligatorisch; Tier 1 empfohlen).
5. Berechtigungen automatisch bei Ablauf entzogen.
6. Alle JIT-Sitzungen im PAM-Audit-Trail protokolliert.

**Azure AD PIM** (für Cloud-Rollen):

1. Berechtigte Rolle zugewiesen (nicht aktiv).
2. Nutzer aktiviert Rolle mit Begründung und MFA.
3. Genehmigung erforderlich für Global Admin und andere Tier-0-Rollen.
4. Zeitlich begrenzte Aktivierung (Standard: 4 Stunden; Maximum: 8 Stunden).
5. Automatische Deaktivierung bei Ablauf.
6. Alle Aktivierungen im Azure-AD-Audit-Protokoll protokolliert.

**Manuelle JIT** (interim wo PAM/PIM nicht eingeführt):

1. Nutzer beantragt Zugang über Ticketing-System mit Begründung.
2. IT-Sicherheit genehmigt und fügt temporäre Gruppenmitgliedschaft hinzu.
3. Kalender-Erinnerung für Entzugszeitpunkt gesetzt.
4. IT-Betrieb entzieht Zugang bei Ablauf manuell.
5. Ticket mit Entziehungsbestätigung geschlossen.

**JIT-Ziele**: Jahr 1: 50% des Tier-1-Zugangs via JIT. Jahr 2: 80% des Tier-1-Zugangs via JIT. Tier 0: dauerhafter Zugang für Bereitschaftsrollen; JIT für alle anderen.

### Privilegierte Zugangsüberprüfungen

| Kontotyp | Überprüfungsfrequenz |
|----------|---------------------|
| Tier-0-privilegierte Konten | Vierteljährlich (ISB oder IT-Sicherheitsmanager überprüft) |
| Tier-1/2-privilegierte Konten | Vierteljährlich (Systemeigentümer überprüfen) |
| Service-Accounts | Vierteljährlich (Systemeigentümer verifizieren fortlaufenden Bedarf) |

**Überprüfungsprozess**:

- Zugangsprüfungs-Kampagnen über Identity-Governance-Tool oder manuellen Prozess initiiert.
- Überprüfer: Direkte Vorgesetzte für Tier 1/2; ISB oder IT-Sicherheitsmanager für Tier 0.
- Überprüfungszeitraum: 10 Arbeitstage zum Abschluss.
- Keine Reaktion: Erinnerung an Tag 5; Eskalation zum Vorgesetzten des Überprüfers an Tag 8; Zugang bei fehlender Reaktion an Tag 15 ausgesetzt.
- Entfernungsanträge innerhalb von 48 Stunden bearbeitet.

### Zugangszertifizierungs-Kampagnenprozess

Vierteljährliche Zugangsprüfungen müssen einer strukturierten Kampagne folgen:

**Woche 1 — Kampagnenvorbereitung**:
- Bericht über privilegierte Konten, Service-Accounts und Gruppenmitgliedschaften aus Identity Provider und PAM generieren.
- An Überprüfer verteilen: Tier-0-Konten an ISB; Tier-1/2-Konten an Systemeigentümer; Service-Accounts an Anwendungseigentümer.

**Woche 2–3 — Überprüfungszeitraum (10 Arbeitstage)**:
- Überprüfer bestätigen jedes Konto: Genehmigen / Widerrufen / Übertragen / Nicht bestimmbar.
- Erinnerungen: Tag 5 (automatisiert), Tag 8 (Eskalation zum Vorgesetzten des Überprüfers), Tag 10 (letzte Warnung — Nichtreaktion als implizite Ablehnung gewertet, Zugang ausgesetzt).

**Woche 4 — Behebung**:
- IT-Betrieb bearbeitet Widerrufe innerhalb von 48 Stunden.
- Zusammenfassungsbericht mit ergriffenen Massnahmen generiert.

**Nach Kampagne**: Ergebnisse dem ISB bei nächster vierteljährlicher Überprüfung vorgestellt. Zertifizierungsnachweise 3 Jahre aufbewahrt.

**Kampagnen-Kennzahlen**: Überprüfungsabschlussrate (Ziel: 100%); durchschnittliche Überprüfungszeit (Ziel: ≤5 Arbeitstage); Widerrufsrate (gesunder Bereich: 5–15%; Raten ausserhalb dieses Bereichs erfordern Untersuchung).

### Break-Glass / Notfallzugang

Die Organisation muss Notfallzugangsverfahren für Situationen aufrechterhalten, in denen normale Authentifizierungskanäle nicht verfügbar sind:

- Break-Glass-Konten mit versiegelten Zugangsdaten gesichert (physischer Tresor oder PAM-Lösung (siehe IAM-Infrastrukturtabelle) versiegelter Umschlag).
- Vier-Augen-Autorisierung für Break-Glass-Nutzung erforderlich (Dual Control — zwei Personen für Zugangsdatenzugang erforderlich).
- Jede Break-Glass-Nutzung protokolliert, alarmiert und innerhalb von 24 Stunden überprüft.
- Zugangsdaten sofort nach Nutzung rotiert.
- Break-Glass-Konten halbjährlich getestet (z.B. Januar und Juli), um zu bestätigen, dass Zugangsdaten funktionieren und Verfahren aktuell sind.
- Testnachweise müssen Datum, Tester, Authentifizierungsbestätigung und Post-Test-Credential-Rotation dokumentieren.

---

## Zugangsbeschränkung

### Durchsetzungsgrundsätze

Der Zugang zu Informationen und anderen zugehörigen Assets muss gemäss dieser Richtlinie und der Richtlinie zur Identitäts- und Zugangsverwaltung eingeschränkt werden:

- **Standard-Ablehnen**: Zugang standardmässig verweigert; ausdrückliche Autorisierung erforderlich.
- **Rollenbasierte Zugangskontrolle (RBAC)**: Zugang basierend auf dokumentierten Arbeitsrollen.
- **Attributbasierte Zugangskontrolle (ABAC)**: Kontextbewusster Zugang (Standort, Gerätecompliance, Risikobewertung) wo vom Identity Provider unterstützt (siehe IAM-Infrastrukturtabelle).
- **Datenklassifizierungsausrichtung**: Zugangsbeschränkungen entsprechen der Klassifizierungsstufe der Informationen.

### Technische Zugangskontrollen

**Betriebssystemzugang**:

- Dateisystemberechtigungen gemäss Datenklassifizierung durchgesetzt.
- Privilegierte Befehle auf autorisierte Administratoren beschränkt.
- Lokale Administrator-Rechte von Standardnutzern entfernt (verwaltete Berechtigungserweiterung für Ausnahmen).

**Datenbankzugang**:

- Direkter Datenbankzugang auf autorisierte DBAs beschränkt.
- Anwendungszugang via Service-Accounts mit Minimalberechtigungen.
- Sensible Spalten für nicht-privilegierten Zugang verschlüsselt oder maskiert.

**Anwendungszugang**:

- Rollenbasierter Zugang innerhalb von Anwendungen.
- Sensible Funktionen erfordern zusätzliche Authentifizierung (Step-up MFA) wo unterstützt.

**API-Zugang**:

- API-Authentifizierung erforderlich (OAuth 2.0 oder API-Schlüssel mit Rotation gemäss Credential-Rotationsplan).
- Rate-Limiting auf allen APIs durchgesetzt.
- Sensible APIs erfordern zusätzliche Autorisierung.

**Cloud-Ressourcenzugang**:

- Cloud-IAM-Richtlinien folgen minimaler Rechtevergabe.
- Cross-Account-Zugang eingeschränkt, protokolliert und vierteljährlich überprüft.
- Ressourcen-Level-Berechtigungen durchgesetzt.

### Sitzungs-Timeouts

System-Sitzungen müssen folgende Timeout-Zeiträume durchsetzen:

| Klassifizierung | Leerlauf-Timeout | Absoluter Timeout |
|----------------|-----------------|-------------------|
| Vertrauliche / Kritische Systeme | 15 Minuten | 8 Stunden |
| Systeme mit sensiblen Personendaten | 5 Minuten | 4 Stunden |
| Privilegierte Admin-Konsolen | 10 Minuten | 4 Stunden |
| Standard-Geschäftssysteme | 30 Minuten | 12 Stunden |

Absoluter Timeout erfordert Re-Authentifizierung unabhängig von der Aktivität.

### Netzwerkbasierte Zugangsbeschränkungen

- Netzwerksegmentierung muss Vertrauenszonen zur Unterstützung der Zugangsbeschränkung trennen (detailliert in der Netzwerksicherheitsrichtlinie).
- Firewall-Regeln müssen Zugangsschranken zwischen Netzwerksegmenten durchsetzen.
- Netzwerkzugangskontrolle (NAC) oder gleichwertig muss Endpunkt-Compliance vor der Zugangsvergabe verifizieren, wo möglich.

### Datenmaskierung

Die Organisation maskiert Daten gemäss gesetzlichen und regulatorischen Verpflichtungen, einschliesslich Schweizer nDSG und DSGVO-Anforderungen. Datenmaskierung muss angewendet werden auf:

- Personenbezogene Daten, die in Nicht-Produktionsumgebungen angezeigt werden.
- Sensible Datenfelder, die Nutzern ohne berechtigten Bedarf nach vollständigem Zugang sichtbar sind.
- In Berichten, Dashboards oder Protokollen angezeigte Daten, wo Vollwerte nicht erforderlich sind.

### Zugangskontroll-Verifizierung

Die Organisation muss Zugangskontrollen durch Folgendes verifizieren:

- Jährliche Penetrationstests mit Versuchen zur Umgehung von Zugangskontrollen.
- Vierteljährliche Berechtigungsaudits für kritische Systeme und privilegierte Konten.
- Automatisiertes Compliance-Scanning auf Konfigurationsdrift wo möglich.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Geschäftsleitung** | Richtlinie genehmigen; Budget für Authentifizierungsinfrastruktur, MFA-Einführung und PAM bereitstellen; Sicherheitskennzahlen vierteljährlich überprüfen |
| **ISB** | Gesamtverantwortung für Authentifizierungs- und Zugangs-Sicherheit; PAM-Strategie und Admin-Tiering-Modell genehmigen; Ausnahmen (mittel/hoch Risiko) genehmigen; vierteljährliche Berichte überprüfen |
| **IT-Sicherheitsmanager** | Tägliches Management der Authentifizierungsinfrastruktur; Authentifizierungs- und privilegierte Zugangsalarme überwachen; vierteljährliche Zugangszertifizierungs-Kampagnen durchführen; Service-Account-Anträge genehmigen; Niedrigrisiko-Ausnahmen genehmigen |
| **IT-Betrieb / IAM-Team** | Identity-Provider- und SSO-Infrastruktur verwalten; privilegierte Zugangs- und JIT-Anträge bearbeiten; MFA-Einschreibung pflegen; Bereitstellung und Aufhebung ausführen; Zugangszertifizierungsberichte generieren; Service-Account-Inventar pflegen; PAW-Einführung verwalten |
| **Systemadministratoren** | Zugangskontrollen auf verwalteten Systemen implementieren; Admin-Tiering-Anforderungen erfüllen; dedizierte privilegierte Konten nutzen; Zugangskontroll-Anomalien melden |
| **Alle Nutzer** | Authentifizierungs-Zugangsdaten schützen; vermuteten Zugangsdaten-Kompromiss sofort melden; MFA-Einschreibung innerhalb erforderlicher Frist abschliessen; Konten oder Zugangsdaten nicht teilen; nicht versuchen, Zugangskontrollen zu umgehen |

---

## Key Performance Indicators

Folgende Kennzahlen müssen zur Messung der Wirksamkeit von Authentifizierungs- und privilegierten Zugangskontrollen verfolgt werden:

| Kennzahl | Ziel | Häufigkeit |
|----------|------|------------|
| MFA-Einschreibung (alle Nutzer) | ≥95% | Monatlich |
| MFA-Einschreibung (privilegierte Nutzer) | 100% | Monatlich |
| Privilegierte Zugangsprüfungs-Abschluss | 100% | Vierteljährlich |
| Passwortrichtlinien-Compliance | ≥98% | Monatlich |
| SSO-Anwendungsintegration | ≥80% (Jahr 1); ≥90% (Jahr 2) | Vierteljährlich |
| Privilegierte Sitzungsaufzeichnung (Tier 0) | 100% | Monatlich |
| Credential-Rotations-Compliance (Service-Accounts) | 100% im Plan | Vierteljährlich |
| Break-Glass-Konto-Test-Abschluss | 100% | Halbjährlich |
| JIT-Zugangs-Akzeptanz (Tier 1) | ≥50% (Jahr 1); ≥80% (Jahr 2) | Vierteljährlich |
| Service-Account-Inventar-Vollständigkeit | 100% | Vierteljährlich |
| Zugangszertifizierungs-Abschlussrate | 100% | Vierteljährlich |
| Conditional-Access-Richtlinien-Abdeckung | 100% der definierten Richtlinien durchgesetzt | Vierteljährlich |
| Kompromittiertes-Zugangsdaten-Screening | 100% der Setz-/Änderungsereignisse validiert | Monatlich |

Kennzahlen müssen dem ISB vierteljährlich gemeldet werden. Kennzahlen unterhalb des Ziels müssen einen Behebungsplan mit Eigentümer und Zieldatum enthalten.

---

## Nachweise

Die folgenden Nachweise belegen die Compliance mit dieser Richtlinie:

| # | Nachweis | Eigentümer | Häufigkeit |
|---|----------|------------|------------|
| 1 | **Passwortrichtlinien-Konfigurationsnachweis** (Identity-Provider-Einstellungen, Breach-Screening-Konfiguration) | IT-Betrieb | *Jährlich oder bei Änderung erfasst* |
| 2 | **MFA-Einschreibungsberichte** (Abdeckungsprozentsatz nach Nutzertyp: privilegiert, Standard, Remote) | IT-Sicherheit | *Monatlich für privilegierte; vierteljährlich für alle Nutzer* |
| 3 | **SSO-Anwendungsintegrations-Inventar** (integriert vs. nicht integriert, Ausnahmenachweise) | IT-Betrieb | *Vierteljährlich überprüft* |
| 4 | **Privilegiertes-Konto-Inventar** (Konto, Eigentümer, Tier, Zweck, letztes Überprüfungsdatum) | IT-Sicherheit | *Vierteljährlich überprüft* |
| 5 | **Privilegierte Zugangsprüfungs-Abschlussnachweise** (Bestätigung, Überprüfer, Datum, ergriffene Massnahmen) | IT-Sicherheit | *Vierteljährlich; 3 Jahre aufbewahrt* |
| 6 | **Sitzungsaufzeichnungs-Stichproben** (Tier-0-Sitzungen; zufällige Stichprobe auf Anomalien überprüft) | IT-Sicherheit | *Vierteljährlich überprüft* |
| 7 | **Break-Glass-Konto-Testnachweise** (Datum, Tester, Ergebnis, Post-Test-Rotationsbestätigung) | IT-Sicherheit | *Halbjährlich* |
| 8 | **Credential-Rotationsprotokolle** (Service-Accounts, Break-Glass-Konten, geteilte Konten) | IT-Betrieb | *Pro Rotationsereignis; halbjährlich geprüft* |
| 9 | **Authentifizierungsereignisprotokolle** (erfolgreiche/fehlgeschlagene Logins, Sperrungen, Anomalie-Untersuchungen) | IT-Sicherheit | *12 Monate aufbewahrt; Anomalien innerhalb von 24 Stunden untersucht* |
| 10 | **Penetrationstest- und Berechtigungsaudit-Berichte** (Zugangskontroll-Befunde und Behebungsstatus) | IT-Sicherheit | *Penetrationstest jährlich; Berechtigungsaudits vierteljährlich* |
| 11 | **Service-Account-Inventar** (Kontoname, Eigentümer, Tier, Zweck, Zugangsdaten-Standort, letztes/nächstes Rotationsdatum) | IT-Sicherheit | *Kontinuierlich gepflegt; vierteljährlich überprüft; 3 Jahre aufbewahrt* |
| 12 | **JIT-Zugangs-Protokolle** (Anträge, Genehmigungen, Dauer, automatische Entzugsbestätigung) | IT-Sicherheit | *Pro Ereignis; vierteljährlich geprüft; 12 Monate aufbewahrt* |
| 13 | **Zugangszertifizierungs-Kampagnennachweise** (Kampagnenergebnisse, Überprüfer-Bestätigungen, bearbeitete Widerrufe) | IT-Sicherheit | *Vierteljährlich; 3 Jahre aufbewahrt* |
| 14 | **Conditional-Access-Richtlinien-Dokumentation** (Richtliniendefinitionen, Einführungsstatus, Ausnahmen) | IT-Betrieb | *Vierteljährlich überprüft; bei Richtlinienänderungen aktualisiert* |
| 15 | **PAW-Einführungsstatus** (PAW-Inventar, Konfigurationskonformität, Einführungsphasen-Erfassung) | IT-Sicherheit | *Vierteljährlich überprüft; 3 Jahre aufbewahrt* |
| 16 | **SSO-Integrations-Inventar** (Anwendungen, SSO-Status, Prioritätsstufe, Ausnahmenachweise) | IT-Betrieb | *Vierteljährlich überprüft; 3 Jahre aufbewahrt* |

---

# Richtlinien-Compliance

## Compliance-Messung

Das Informationssicherheits-Managementteam überprüft die Compliance mit dieser Richtlinie durch verschiedene Methoden, darunter Identity-Provider-Konfigurations-Audits, MFA-Abdeckungsberichte, privilegierte Zugangsprüfungen, Penetrationstests, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vom Informationssicherheitsmanager im Voraus genehmigt und dokumentiert werden, mit dokumentierter Risikoakzeptanz, Ausgleichsmassnahmen und einem definierten Überprüfungsdatum. Ausnahmen müssen dem Management-Review-Team gemeldet werden. Maximale Ausnahmedauer: 12 Monate, verlängerbar mit erneuter Genehmigung.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstösst, kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung des Arbeitsverhältnisses.

**Progressiver Reaktionsplan** (innerhalb eines rollenden 12-Monats-Zeitraums):

| Vorkommen | Reaktion | Zeitrahmen | Eigentümer |
|-----------|---------|------------|------------|
| Erste | Bewusstseins-Erinnerung und gezielte Schulung | Innerhalb von 5 Arbeitstagen | IT-Sicherheit |
| Zweite (innerhalb von 90 Tagen) | Vorgesetzten-Benachrichtigung + dokumentierte Verwarnung | Innerhalb von 3 Arbeitstagen | IT-Sicherheit + HR |
| Dritte (innerhalb von 12 Monaten) | Zugangsbeschränkung bis zur Behebung | Sofort | IT-Sicherheit + Vorgesetzter |
| Vorsätzlicher / kritischer Verstoss | Disziplinarische Massnahmen gemäss HR-Richtlinien | Sofortige Eskalation | HR + ISB |

**Kritische Verstösse**, die unabhängig von der Vorgeschichte sofortige Eskalation erfordern:

- Teilen privilegierter Zugangsdaten.
- Absichtliche Umgehung von Sicherheitskontrollen.
- Tier-Isolationsverstösse.
- Nicht autorisierte Nutzung von Break-Glass-Konten.

**Phishing-Simulations-Misserfolge** (innerhalb eines rollenden 12-Monats-Zeitraums):

- 1 Misserfolg: Gezielte Bewusstseinsschulung (innerhalb von 7 Tagen).
- 2 Misserfolge: Vorgesetzten-Benachrichtigung + zusätzliche Schulung (innerhalb von 5 Tagen).
- 3+ Misserfolge: Privilegierter Zugang ausgesetzt; Standardzugang eingeschränkt bis zur nachgewiesenen Verbesserung.

## Kontinuierliche Verbesserung

Diese Richtlinie wird als Teil des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen berücksichtigen Änderungen an Authentifizierungsstandards (einschliesslich NIST SP 800-63B-Revisionen), aufkommende Bedrohungen (Credential Stuffing, Phishing, MFA-Umgehungstechniken), regulatorische Änderungen und Erkenntnisse aus Incidents.

---

# Abgedeckte Bereiche des ISO-27001-Standards

Richtlinie zur Authentifizierung und zum privilegierten Zugang — ISO-27001-Controls-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Managementverantwortung |
| Klausel 6.2 Informationssicherheitsziele | 5.15 Zugangssteuerung |
| Klausel 7.3 Bewusstsein | 5.17 Authentifizierungsinformationen |
| Klausel 7.5.3 Steuerung dokumentierter Informationen | 5.36 Compliance mit Richtlinien, Regeln und Standards |
| | 6.3 Informationssicherheits-Bewusstsein, Ausbildung und Schulung |
| | 6.4 Disziplinarverfahren |
| | **8.2 Privilegierte Zugriffsrechte** |
| | **8.3 Informationszugangsbeschränkung** |
| | **8.5 Sichere Authentifizierung** |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizer nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen einschliesslich Authentifizierungs- und Zugangskontrollen |
| Schweizer DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (sofern anwendbar) | Art. 32 — Sicherheit der Verarbeitung (Authentifizierungskontrollen als angemessene Massnahme) |
| ISO/IEC 27001:2022 | Annex A Controls 8.2, 8.3, 8.5 |
| ISO/IEC 27002:2022 | Abschnitte 8.2, 8.3, 8.5 — Umsetzungshinweise |
| NIST SP 800-63B | Digitale Identitäts- und Authentifizierungsrichtlinien (gespeicherte Geheimnisse, MFA) |
| NIST CSF 2.0 | PR.AA (Identitätsverwaltung, Authentifizierung und Zugangskontrolle) |
| CIS Controls v8 | Control 5 (Kontoverwaltung), Control 6 (Zugangskontrollverwaltung) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
