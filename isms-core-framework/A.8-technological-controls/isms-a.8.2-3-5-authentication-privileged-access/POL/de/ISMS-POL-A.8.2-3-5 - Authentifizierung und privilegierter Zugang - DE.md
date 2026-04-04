<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.2-3-5-DE:framework:POL:a.8.2-3-5 -->
**ISMS-POL-A.8.2-3-5 — Authentifizierung und privilegierter Zugang**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Richtlinie zur Authentifizierung und Sicherheit privilegierter Zugänge |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.2-3-5 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] | |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Date to be set] | ISB | Erstfassung für die ISO 27001:2022-Erstzertifizierung |

**Überprüfungsrhythmus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL)
- Security Operations: Security Operations Manager
- IT-Betrieb: IT-Betriebsleiter
- Compliance: Rechts-/Compliance-Officer
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-POL-A.5.15-16-18 (Identitäts- und Zugriffsmanagement — Grundlage)
- ISMS-IMP-A.8.2-3-5.S1-UG/TG (Authentifizierungsinventar)
- ISMS-IMP-A.8.2-3-5.S2-UG/TG (MFA-Abdeckung)
- ISMS-IMP-A.8.2-3-5.S3-UG/TG (Privilegierte Konten)
- ISMS-IMP-A.8.2-3-5.S4-UG/TG (Überwachung privilegierter Zugänge)
- ISMS-IMP-A.8.2-3-5.S5-UG/TG (Zugangsbeschränkungen)
- ISO/IEC 27001:2022 Massnahmen A.8.2, A.8.3, A.8.5
- ISO/IEC 27002:2022 (Implementierungshinweise)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] für Authentifizierungssicherheit, Privileged Access Management (PAM) und technische Zugangsdurchsetzung gemäss ISO/IEC 27001:2022 fest.

**Adressierte Massnahmen**:

- **A.8.5 — Sichere Authentifizierung**: Authentifizierungsmechanismen basierend auf Zugangsbeschränkungen
- **A.8.2 — Privilegierte Zugriffsrechte**: Einschränkung und Verwaltung privilegierter Zugänge
- **A.8.3 — Einschränkung des Informationszugangs**: Technische Durchsetzung von Zugangsmassnahmen

**Geltungsbereich**: Alle Authentifizierungsmechanismen, privilegierten Konten und technischen Zugangsmassnahmen auf allen Systemen, Plattformen und Umgebungen im Eigentum oder Betrieb von [Organisation].

**Zweck**: Festlegen, WAS für Authentifizierungs- und Zugangsmassnahmen erforderlich sind und WER dafür verantwortlich ist. Implementierungsverfahren (WIE) sind in ISMS-IMP-A.8.2-3-5 dokumentiert.

**Begründung für gestapelte Massnahmen**: Diese Massnahmen bilden untrennbare Schichten des Authentifizierungs- und Zugangssicherheits-Stacks. Eine getrennte Implementierung würde Lücken zwischen Authentifizierung, Privilegienverwaltung und Zugangsdurchsetzung erzeugen.

**Regulatorische Ausrichtung**: Gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen):

- **Verbindlich**: Schweizerisches nDSG (Art. 8), EU DSGVO (Art. 32), ISO 27001:2022
- **Bedingt**: FINMA, DORA, NIS2 (Art. 21(2)(e) — MFA-Pflicht), PCI DSS v4.0.1

---

# Massnahmenausrichtung und Geltungsbereich

## ISO/IEC 27001:2022 Massnahmenanforderungen

**Massnahme A.8.5 — Sichere Authentifizierung**:
> *Sichere Authentifizierungstechnologien und -verfahren sollten basierend auf Zugangsbeschränkungen für Informationen und der themenspezifischen Richtlinie zur Zugangskontrolle implementiert werden.*

**Massnahme A.8.2 — Privilegierte Zugriffsrechte**:
> *Die Zuweisung und Nutzung privilegierter Zugriffsrechte sollte eingeschränkt und verwaltet werden.*

**Massnahme A.8.3 — Einschränkung des Informationszugangs**:
> *Der Zugang zu Informationen und anderen zugehörigen Assets sollte gemäss der festgelegten themenspezifischen Richtlinie zur Zugangskontrolle eingeschränkt werden.*

## Geltungsbereichsdefinition

**Im Geltungsbereich**:

- Alle Benutzerauthentifizierung (Passwörter, MFA, SSO, Zertifikate, Biometrie)
- Alle privilegierten Konten (Administratoren, Root, Dienstkonten, Break-Glass)
- Alle technischen Zugangsmassnahmen (Betriebssystem, Datenbank, Anwendung, API, Cloud, Netzwerk)
- Alle Deployment-Modelle (On-Premises, Cloud, Hybrid, SaaS)
- Alle Nutzertypen (Mitarbeitende, Auftragnehmer, Lieferanten, Kunden wo anwendbar)

**Nicht im Geltungsbereich**:

- Physische Zugangsmassnahmen (adressiert in A.7.x Physische Sicherheit)
- Details zur Netzwerksegmentierung (adressiert in A.8.20-22 Netzwerksicherheit)
- Verwaltung kryptografischer Schlüssel (adressiert in A.8.24 Kryptografie)

## Unabhängigkeit in der Anwendbarkeitserklärung (SoA)

Jede Massnahme behält unabhängige Anwendbarkeit:

- A.8.5 kann ohne A.8.2 anwendbar sein (nur Standard-Benutzerauthentifizierung)
- A.8.2 setzt A.8.5 voraus (privilegierter Zugang erfordert Authentifizierung)
- A.8.3 setzt sowohl A.8.5 als auch A.8.2 voraus (Durchsetzung erfordert Authentifizierung und Privilegdefinition)

---

# Authentifizierungsanforderungen (Massnahme A.8.5)

## Standards für Authentifizierungsmechanismen

[Organisation] muss Authentifizierungsmechanismen implementieren, die der Sensibilität der zugänglichen Informationen und Systeme entsprechen.

**Mindestanforderungen Authentifizierung**:

| Systemklassifikation | Mindestanforderung | MFA-Anforderung |
|---------------------|-------------------|-----------------|
| **Kritisch/Hochrisiko** | MFA verbindlich | Hardware-Token oder Authenticator-App |
| **Standard-Geschäftsbetrieb** | Passwort + MFA empfohlen | Authenticator-App akzeptabel |
| **Geringes Risiko/Öffentlich** | Passwort akzeptabel | Optional |
| **Privilegierter Zugang** | MFA verbindlich | Hardware-Token bevorzugt (FIDO2) |
| **Remote-Zugang** | MFA verbindlich | Für alle Remote-Verbindungen erforderlich |

**Passwortanforderungen** (wo Passwörter verwendet werden, gemäss NIST SP 800-63B):

- Mindestlänge: 12 Zeichen (14 für privilegierte Konten)
- Komplexität: Kombination aus Zeichentypen ODER Passphrase mit mindestens 16 Zeichen
- Keine Passwortablaufzeit, es sei denn, eine Kompromittierung wird vermutet oder festgestellt
- Kompromittierungserkennung: Passwörter werden gegen bekannte Datenpannen-Datenbanken geprüft (z. B. Have I Been Pwned API oder gleichwertig); kompromittierte Passwörter erfordern sofortiges Zurücksetzen
- Keine Passwortwiederverwendung: Mindestens 24 Passwörter als Historie

**Verifikation**: Passwortrichtliniendurchsetzung validiert über Konfigurationsexporte des Identity Providers; Alarme der Kompromittierungserkennung wöchentlich überprüft.

## Multi-Faktor-Authentifizierung (MFA)

**MFA muss verbindlich sein für**:

- Alle privilegierten Zugänge (Tier-0-, Tier-1-, Tier-2-Administratoren)
- Alle Remote-Zugänge (VPN, Remote Desktop, Cloud-Konsole)
- Alle Zugänge zu sensiblen Daten (Personendaten, Finanzdaten, geistiges Eigentum)
- Alle nach aussen gerichteten Anwendungen mit Authentifizierung
- Alle administrativen Cloud-Plattformkonsolen

**Zulässige MFA-Methoden** (in Reihenfolge der Präferenz mit Phishing-Resistenzbewertung):

| Methode | Phishing-Resistenz | Anwendungsfall |
|---------|-------------------|----------------|
| Hardware-Sicherheitsschlüssel (FIDO2/WebAuthn) | Hoch (phishing-resistent) | Für Tier 0 erforderlich, für alle Privilegierten empfohlen |
| Authenticator-Apps (TOTP) | Mittel | Akzeptabel für Tier 1/2 und Standardnutzer |
| Push-Benachrichtigungen (mit Nummernabgleich) | Mittel | Akzeptabel bei aktiviertem Nummernabgleich |
| SMS/Sprach-OTP | Niedrig | Nur wo andere Methoden nicht möglich (Legacy-Systeme) |

*Präferenzen für MFA-Methoden werden in Sicherheitssensibilisierungsschulungen und MFA-Registrierungsmitteilungen kommuniziert.*

**MFA-Abdeckungsziele**:

- Privilegierte Nutzer: 100 % MFA-Registrierung
- Alle Nutzer: ≥ 95 % MFA-Registrierung innerhalb von 12 Monaten nach Richtlinieneinführung
- Remote-Zugang: 100 % MFA-Durchsetzung

**Baseline-Bewertung**: Vor der Zieldurchsetzung muss [Organisation] die aktuelle MFA-Abdeckungs-Baseline über Registrierungsberichte des Identity Providers erfassen. Baseline in Arbeitsmappe 2 dokumentiert; Lückenschliessungsplan erforderlich, wenn Baseline < 80 %.

**Deployment-Fahrplan**: Falls aktuelle MFA-Abdeckung unter dem Ziel liegt, müssen Deployment-Meilensteine in Arbeitsmappe 2 mit Zieldaten dokumentiert werden (z. B. 80 % bis Monat 3, 90 % bis Monat 6, 95 % bis Monat 12). Fortschritt vierteljährlich verfolgt.

**Verifikation**: MFA-Registrierungsstatus über Exporte des Identity-Provider-Dashboards verifiziert (Microsoft Entra ID, Okta oder gleichwertig); wöchentliche Berichte für privilegierte Nutzer, monatlich für alle Nutzer.

## Single Sign-On (SSO)

[Organisation] muss zentralisiertes SSO mit einem Ziel von ≥ 90 % SaaS-Anwendungsintegration implementieren:

- Neue SaaS-Anwendungen: SSO-Integration vor Beschaffungsgenehmigung erforderlich
- Bestehende Anwendungen: SSO-Integration priorisiert nach Risiko und Nutzungsvolumen
- Reduziert Passwort-Erschöpfung und verbessert den Sicherheitsstatus
- Ermöglicht zentralisierten Zugangsentzug bei Kündigung

**Ausnahmen**: Anwendungen ohne SSO-Fähigkeit erfordern eine dokumentierte Ausnahme mit kompensierenden Massnahmen (z. B. individuelle MFA, verstärkte Überwachung).

**Verifikation**: SSO-Anwendungsinventar in Arbeitsmappe 1 geführt; Integrationsanteil vierteljährlich verfolgt.

## Protokollierung der Authentifizierung

Alle Authentifizierungsereignisse müssen protokolliert werden:

- Erfolgreiche und fehlgeschlagene Authentifizierungsversuche
- MFA-Registrierung und Methodenänderungen
- Passwortänderungen und -zurücksetzungen
- Kontosperrungen und -freigaben
- Sitzungserstellung und -beendigung

**Verifikation**: Authentifizierungsprotokolle über SIEM-Integration überprüft; Anomalien innerhalb von 24 Stunden untersucht.

---

# Anforderungen für privilegierten Zugang (Massnahme A.8.2)

## Grundsätze für privilegierten Zugang

[Organisation] muss privilegierten Zugang basierend auf folgenden Grundsätzen einschränken:

- **Minimalprinzip (Least Privilege)**: Minimal erforderlicher Zugang zur Ausführung von Aufgaben
- **Need-to-Know**: Zugang nur zu für spezifische Aufgaben benötigten Informationen
- **Funktionstrennung (Separation of Duties)**: Kritische Funktionen auf mehrere Personen verteilt
- **Zeitlich begrenzter Zugang**: Just-in-Time (JIT)-Bereitstellung wo möglich

## Klassifikation privilegierter Konten

**Admin-Tiering-Modell** — [Organisation] muss abgestufte Administration implementieren:

| Tier | Umfang | Beispiele | Anforderungen |
|------|--------|-----------|---------------|
| **Tier 0** | Domain/Unternehmen | Domain Admins, Azure Global Admin, PKI, SIEM | Hardware-MFA, PAW erforderlich, Sitzungsaufzeichnung verbindlich |
| **Tier 1** | Server/Anwendung | Serveradministratoren, DBAs, Cloud-Subscription-Admins | MFA erforderlich, dedizierte Administratorworkstation empfohlen |
| **Tier 2** | Workstation/Endgerät | Desktop-Support, Helpdesk mit lokalem Admin | MFA erforderlich, Standard-Workstation akzeptabel |

**Tier-Isolierungsanforderungen**:

- Tier-0-Konten dürfen sich NIEMALS bei Tier-1- oder Tier-2-Systemen authentifizieren
- Tier-1-Konten dürfen sich NIEMALS bei Tier-2-Systemen authentifizieren
- Getrennte Zugangsdaten je Tier erforderlich (z. B. max.muster.t0, max.muster.t1)

**Technische Durchsetzung der Tier-Isolierung**:

- Technische Massnahmen: Conditional-Access-Richtlinien, GPO-Einschränkungen oder Firewall-Regeln zur Verhinderung von Tier-übergreifender Authentifizierung
- Überwachung: SIEM-Alarme für Tier-Verletzungsversuche konfiguriert
- PAW-Deployment: Tier-0 Privileged Access Workstations physisch oder logisch vom Standardnetzwerk getrennt

**Dokumentation Implementierungsstatus**: Admin-Tiering-Deployment-Phase (Planung, Pilotbetrieb, Teildurchsetzung, vollständige Durchsetzung) muss in Arbeitsmappe 3 dokumentiert werden. Bei stufenweisem Deployment werden kompensierende Massnahmen für nicht durchgesetzte Tiers dokumentiert.

**Verifikation**: Tier-Isolierung über Analyse von Authentifizierungsprotokollen verifiziert (keine Tier-0-Anmeldungen bei Tier-1/2-Systemen); vierteljährliche Prüfung von Conditional-Access-Richtlinien; PAW-Konfiguration gegen Baseline validiert.

## Privileged Access Management (PAM)

[Organisation] muss Massnahmen für privilegierten Zugang implementieren:

**Erforderliche Massnahmen**:

- Inventar privilegierter Konten: Alle privilegierten Konten dokumentiert und klassifiziert
- Passwortvaultierung: Privilegierte Passwörter in zugelassener PAM-Lösung gespeichert
- Sitzungsaufzeichnung: Tier-0-Sitzungen aufgezeichnet; Tier-1-Aufzeichnung empfohlen
- Just-in-Time-Zugang: Temporäre Privilegienerweiterung mit automatischem Widerruf
- Zugangsdatenrotation: Dienstkonto-Passwörter gemäss definiertem Zeitplan rotiert

**Zugangsdatenrotationsanforderungen**:

| Kontotyp | Standard-Rotation | Risikobasierte Anpassung |
|----------|------------------|--------------------------|
| Dienstkonten (Tier 0) | Maximal 90 Tage | Kann auf 180 Tage verlängert werden mit Genehmigung IT-Sicherheitsmanager und dokumentierter Risikoakzeptanz |
| Dienstkonten (Tier 1/2) | Maximal 180 Tage | Kann auf 365 Tage verlängert werden mit Genehmigung IT-Sicherheitsmanager und kompensierenden Massnahmen |
| Break-Glass-Konten | Nach jeder Nutzung + maximal 365 Tage | Keine Anpassung — immer nach Nutzung rotieren |
| Gemeinsame Administratorkonten | 90 Tage (nicht empfohlen) | Migration zu individuellen Konten; gemeinsame Konten erfordern ISB-Ausnahmegenehmigung |

**Genehmigung risikobasierter Anpassungen**: Alle Rotationsverlängerungen erfordern dokumentierte Begründung, Genehmigungsunterschrift, kompensierende Massnahmen (z. B. verstärkte Überwachung, eingeschränkter Zugang) und jährliche Erneuerung. Genehmigte Anpassungen in Arbeitsmappe 3 verfolgt.

**PAM-Lösungsanforderungen**:

- Passwortvaultierung: Alle Tier-0/1-Privilegienzugangsdaten in zugelassener PAM-Lösung gespeichert
- Sitzungsaufzeichnung: Tier-0-Sitzungen über PAM oder gleichwertiges System aufgezeichnet; Aufzeichnungen gemäss Abschnitt 8.3 aufbewahrt
- Just-in-Time (JIT): Anfragen zur Privilegienerweiterung protokolliert; automatischer Widerruf nach definiertem Zeitraum

**Dokumentation Deployment-Status**: PAM-Deployment-Phase (Evaluierung, Pilot, Tier-0-Onboarding, Tier-1-Onboarding, Vollbetrieb) muss in Arbeitsmappe 3 dokumentiert werden. Falls PAM nicht vollständig betriebsbereit, müssen kompensierende Massnahmen (z. B. manuelle Zugangsdatenrotation, alternative Sitzungsprotokollierung) mit Zieldatum für vollständiges Deployment dokumentiert werden.

**Verifikation**: PAM-Lösungs-Deployment-Status in Arbeitsmappe 3 dokumentiert; Anteil vaultierter Konten verfolgt; Stichproben der Sitzungsaufzeichnungen vierteljährlich vom IT-Sicherheitsmanager überprüft.

## Überprüfungen privilegierter Zugänge

**Überprüfungsfrequenz**:

- Vierteljährlich: Alle privilegierten Zugriffsrechte überprüft und rezertifiziert
- Sofort: Bei Rollenwechsel, Kündigung oder Sicherheitsvorfall
- Jährlich: Vollständige Prüfung privilegierter Zugänge mit externer Validierung

**Überprüfungsprozess**:

- Zugriffsüberprüfungskampagnen über Identity-Governance-Tool oder manuellen Prozess initiiert
- Prüfer: Direkte Führungskräfte für privilegierten Standardzugang; ISB/Sicherheitsmanager für Tier 0
- Überprüfungszeitraum: 10 Arbeitstage zur Vervollständigung
- Keine Reaktion: Automatische Erinnerung an Tag 5; Eskalation an die Führungskraft des Prüfers an Tag 8; Zugang gesperrt an Tag 15 bei fehlender Reaktion
- Bestätigung: Prüfer bestätigt, dass jeder Zugang noch benötigt wird; Entfernungsanfragen innerhalb von 48 Stunden bearbeitet

**Verifikation**: Vierteljährliche Zugriffsüberprüfungen in Arbeitsmappe 4 mit Bestätigungsunterschriften dokumentiert; Abschlussquoten als KPI verfolgt (Ziel: 100 %); Bestätigungsnachweise für Prüfungen aufbewahrt.

## Break-Glass / Notfallzugang

[Organisation] muss Notfallzugangsverfahren unterhalten:

- Break-Glass-Konten mit versiegelten Zugangsdaten gesichert (physischer Tresor oder versiegelter PAM-Umschlag)
- Mehrpersonenautorisierung für Break-Glass-Nutzung erforderlich (Vier-Augen-Prinzip)
- Alle Break-Glass-Nutzungen protokolliert, alarmiert und innerhalb von 24 Stunden überprüft
- Zugangsdaten sofort nach Nutzung rotiert

**Periodische Tests**: Break-Glass-Konten halbjährlich getestet (Q1 und Q3, z. B. Januar und Juli), um sicherzustellen, dass Zugangsdaten funktionieren und Verfahren aktuell sind. Tests dokumentiert mit Datum, Tester, Bestätigung erfolgreicher Authentifizierung und Zugangsdatenrotation nach dem Test.

**Verifikation**: Break-Glass-Nutzungsprotokoll monatlich überprüft (erwartet: minimale Nutzung); Testunterlagen in Arbeitsmappe 4 geführt; Rotation nach Nutzung über PAM oder manuelle Verifikation bestätigt.

---

# Anforderungen für Zugangsbeschränkungen (Massnahme A.8.3)

## Grundsätze der Zugangsdurchsetzung

[Organisation] muss Zugangsbeschränkungen durch technische Massnahmen durchsetzen:

- **Standard-Verweigerung (Default Deny)**: Zugang standardmässig verweigert; explizite Autorisierung erforderlich
- **Rollenbasierte Zugangskontrolle (RBAC)**: Zugang basierend auf Arbeitsstellen
- **Attributbasierte Zugangskontrolle (ABAC)**: Kontextbewusster Zugang wo unterstützt
- **Ausrichtung an Datenklassifikation**: Zugangsbeschränkungen entsprechen der Datensensibilität

## Technische Zugangsmassnahmen

**Betriebssystemzugang**:

- Dateisystemberechtigungen gemäss Datenklassifikation durchgesetzt
- Privilegierte Befehle auf autorisierte Administratoren beschränkt
- Lokale Administratorrechte von Standardnutzern entfernt

**Datenbankzugang**:

- Direkter Datenbankzugang auf Datenbankadministratoren beschränkt
- Anwendungszugang über Dienstkonten mit Mindestprivilegien
- Sensible Spalten für nicht privilegierten Zugang verschlüsselt oder maskiert

**Anwendungszugang**:

- Rollenbasierter Zugang innerhalb von Anwendungen
- Sensible Funktionen erfordern zusätzliche Authentifizierung (Step-up-MFA)
- Sitzungs-Timeouts durchgesetzt:

| Klassifikation | Inaktivitäts-Timeout | Absolutes Timeout |
|---------------|---------------------|-------------------|
| Sensibel/Kritisch | 15 Minuten | 8 Stunden |
| Standard-Geschäftsbetrieb | 30 Minuten | 12 Stunden |
| Privilegierte Administratorkonsolen | 10 Minuten | 4 Stunden |
| Nicht klassifiziert (Standard) | 30 Minuten | 12 Stunden |

*Absolutes Timeout erfordert erneute Authentifizierung unabhängig von der Aktivität.*

**API-Zugang**:

- API-Authentifizierung erforderlich (OAuth 2.0, API-Schlüssel mit Rotation)
- Rate Limiting durchgesetzt
- Sensible APIs erfordern zusätzliche Autorisierung

**Cloud-Ressourcenzugang**:

- Cloud-IAM-Richtlinien folgen dem Minimalprinzip
- Cross-Account-Zugang eingeschränkt und protokolliert
- Ressourcenebenen-Berechtigungen durchgesetzt

## Netzwerkbasierte Zugangsbeschränkungen

- Netzwerksegmentierung trennt Vertrauenszonen
- Firewall-Regeln setzen Zugangsgrenzen durch
- Network Access Control (NAC) verifiziert Endgeräte-Compliance vor Zugang

## Zugangsmassnahmen-Tests

[Organisation] muss Zugangsmassnahmen verifizieren:

- Jährliche Penetrationstests umfassen Versuche zur Umgehung von Zugangsmassnahmen
- Vierteljährliche Berechtigungsprüfungen für kritische Systeme
- Automatisiertes Compliance-Scanning auf Konfigurationsabweichungen

**Verifikation**: Penetrationstest-Berichte dokumentieren Wirksamkeit der Zugangsmassnahmen; Befunde gemäss Risikobewertung behoben.

---

# Rollen und Verantwortlichkeiten

## Geschäftsleitung

- Richtlinie zur Authentifizierung und privilegierten Zugangssicherheit genehmigen
- Budget für PAM-Lösungen, MFA-Deployment, Sicherheitswerkzeuge bereitstellen
- Kennzahlen zur privilegierten Zugangssicherheit vierteljährlich überprüfen
- Eskalationsstelle bei grösseren Vorfällen mit privilegierten Zugängen

## Informationssicherheitsbeauftragter (ISB)

- Gesamtverantwortung für Authentifizierungs- und Zugangssicherheit
- PAM-Lösungsauswahl und MFA-Strategie genehmigen
- Implementierung des Admin-Tiering-Modells genehmigen
- Ausnahmen für privilegierte Zugänge genehmigen (mittleres/hohes Risiko)
- Vierteljährliche Berichte zu privilegierten Zugängen überprüfen

**Delegation**: ISB kann Genehmigungsbehörde an stellvertretenden ISB oder IT-Sicherheitsmanager für operative Entscheidungen delegieren. Delegierte Genehmigungen erfordern nachträgliche ISB-Überprüfung innerhalb von 5 Arbeitstagen.

## IT-Sicherheitsmanager

- Tägliches Management der Authentifizierungsinfrastruktur
- Authentifizierungs- und Privilegzugangsalarme überwachen
- Vierteljährliche Überprüfungen privilegierter Zugänge durchführen
- Niedrigrisikoausnahmen genehmigen
- Incident-Response bei Zugangsdaten-Kompromittierung koordinieren

## Identity & Access Management (IAM) Team

- Identity Provider und SSO-Infrastruktur verwalten
- Anfragen für privilegierten Zugang bearbeiten
- MFA-Registrierung und Support gewährleisten
- Zugangsbereitstellung und -entzug durchführen
- Zugangszertifizierungsberichte erstellen

## Systemadministratoren

- Zugangsmassnahmen auf verwalteten Systemen implementieren
- Admin-Tiering-Anforderungen einhalten
- Dedizierte privilegierte Konten verwenden (nicht persönliche Konten)
- Zugangsmassnahmen-Anomalien melden
- An Zugriffsüberprüfungen für eigene Systeme teilnehmen

## Alle Nutzer

- Authentifizierungszugangsdaten schützen
- Vermutete Zugangsdaten-Kompromittierung sofort melden
- MFA-Registrierung innerhalb der erforderlichen Frist abschliessen
- Konten oder Zugangsdaten nicht teilen
- Keine Versuche, Zugangsmassnahmen zu umgehen

---

# Governance und Compliance

## Richtlinien-Compliance-Überwachung

**Kontinuierliche Überwachung**:

- MFA-Registrierungsstatus täglich verfolgt
- Aktivitäten mit privilegiertem Zugang in Echtzeit überwacht
- Authentifizierungsfehler im SIEM korreliert

**Periodische Bewertung**:

- Vierteljährlich: Abschlussquote Überprüfungen privilegierter Zugänge
- Vierteljährlich: MFA-Abdeckungskennzahlen
- Jährlich: Vollständige Bewertung Authentifizierung und Zugangsmassnahmen

## Ausnahmenmanagement

**Ausnahmeprozess**:

- Alle Ausnahmen erfordern dokumentierte geschäftliche Begründung
- Risikobewertung erforderlich für mittleres/hohes Risiko
- Kompensierende Massnahmen verbindlich für alle Ausnahmen
- Maximale Ausnahmedauer: 12 Monate (verlängerbar mit erneuter Genehmigung)

**Genehmigungsbehörde für Ausnahmen**:

| Risikoniveau | Genehmiger | Überprüfungsfrequenz |
|-------------|-----------|---------------------|
| Niedrig | IT-Sicherheitsmanager | Jährlich |
| Mittel | ISB | Vierteljährlich |
| Hoch | ISB + Risikoausschuss | Monatlich |

## Umgang mit Nichtkonformität

**Abgestuftes Vorgehen** (innerhalb von 12 rollierende Monate):

| Vorkommnis | Massnahme | Zeitrahmen | Verantwortlich |
|------------|----------|-----------|---------------|
| Erstes | Sensibilisierungserinnerung und Schulung | Innerhalb von 5 Arbeitstagen | IT-Sicherheit |
| Zweites (innerhalb von 90 Tagen) | Managerbenachrichtigung + dokumentierte Verwarnung | Innerhalb von 3 Arbeitstagen | IT-Sicherheit + HR |
| Drittes (innerhalb von 12 Monaten) | Zugangssperrung bis zur Behebung | Sofort | IT-Sicherheit + Manager |
| Vorsätzliche/Kritische Verletzung | Disziplinarisches Verfahren gemäss HR-Richtlinien | Sofortige Eskalation | HR + ISB |

**Kritische Verletzungen** (sofortige Eskalation unabhängig von Vorgeschichte):

- Teilen privilegierter Zugangsdaten
- Umgehung von Sicherheitsmassnahmen
- Tier-Isolierungsverstösse

**Phishing-Simulationsfehler** (innerhalb von 12 rollierenden Monaten):

- 1 Fehler: Gezielte Sensibilisierungsschulung (innerhalb von 7 Tagen)
- 2 Fehler: Managerbenachrichtigung + zusätzliche Schulung (innerhalb von 5 Tagen)
- 3+ Fehler: Privilegierter Zugang gesperrt; Standardzugang eingeschränkt bis zur nachgewiesenen Verbesserung

**Verifikation**: Nichtkonformitäts-Vorfälle im Sicherheitsvorfallregister verfolgt; Reaktionszeitrahmen prüfbar.

## Kennzahlen und Reporting

**Key Performance Indicators**:

| Kennzahl | Ziel | Häufigkeit |
|---------|------|-----------|
| MFA-Registrierung (alle Nutzer) | ≥ 95 % | Monatlich |
| MFA-Registrierung (Privilegierte) | 100 % | Wöchentlich |
| Abschlussquote Überprüfungen privilegierter Zugänge | 100 % | Vierteljährlich |
| Passwortrichtlinien-Compliance | ≥ 98 % | Monatlich |
| SSO-Anwendungsintegration | ≥ 90 % | Vierteljährlich |
| Sitzungsaufzeichnung privilegierter Sitzungen (Tier 0) | 100 % | Monatlich |

**Reporting und Visualisierung**: KPIs in Summary Dashboards mit Trendvisualisierung verfolgt. Monatliche Berichte an IT-Sicherheitsmanager; vierteljährliche Executive-Zusammenfassung an ISB und Geschäftsleitung mit Compliance-Status und Behebungsprioritäten.

---

# Integration mit anderen Massnahmen

## Verwandte ISMS-Massnahmen

| Massnahme | Beziehung |
|-----------|-----------|
| **A.5.15-16-18 (IAM-Grundlage)** | Diese Richtlinie baut auf der IAM-Grundlage auf; Identitätslebenszyklus speist Authentifizierung |
| **A.5.17 (Authentifizierungsinformationen)** | Zugangsdaten-Verwaltungsverfahren unterstützen diese Richtlinie |
| **A.5.18 (Zugriffsrechte)** | Zugangsprovisionierung implementiert Anforderungen dieser Richtlinie |
| **A.6.1-2 (Beschäftigungssicherheit)** | Überprüfung und Arbeitsbedingungen unterstützen das Vertrauen in privilegierte Zugänge |
| **A.8.1 (Benutzer-Endgeräte)** | Endgerätesicherheit unterstützt Authentifizierungssicherheit |
| **A.8.15-16 (Protokollierung & Überwachung)** | Authentifizierungs- und Zugangsprotokolle fliessen in Sicherheitsüberwachung |
| **A.8.20-22 (Netzwerksicherheit)** | Netzwerksegmentierung unterstützt Zugangsbeschränkung |
| **A.5.24-27 (Vorfallmanagement)** | Zugangsdaten-Kompromittierung löst Incident-Response aus |

## Regulatorisches Mapping

| Anforderung | Schweizerisches nDSG | EU DSGVO | ISO 27001 | NIS2* |
|-------------|---------------------|---------|-----------|-------|
| Authentifizierungsmassnahmen | Art. 8 | Art. 32 | A.8.5 | Art. 21(2)(e) |
| Verwaltung privilegierter Zugänge | Art. 8 | Art. 32 | A.8.2 | Art. 21(2)(i) |
| Zugangsbeschränkungen | Art. 8 | Art. 32 | A.8.3 | Art. 21(2)(c) |

*NIS2 anwendbar, wenn [Organisation] als wesentliche oder wichtige Einrichtung eingestuft ist.

---

# Nachweise für diese Richtlinie

**Stage 1 (Dokumentationsüberprüfung) Nachweise:**

Erforderliche Nachweise zur Demonstration ausreichender Dokumentation und Genehmigung:

- Dieses Richtliniendokument (ISMS-POL-A.8.2-3-5 v1.0)
- Genehmigungsunterschriften von ISB, ITL, Geschäftsleitung
- Authentifizierungsanforderungen definiert (Abschnitt 2 — A.8.5)
- Admin-Tiering-Modell dokumentiert (Abschnitt 3 — A.8.2)
- Zugangsbeschränkungsanforderungen spezifiziert (Abschnitt 4 — A.8.3)
- Rollen und Verantwortlichkeiten zugewiesen
- Referenzen auf Bewertungsarbeitsmappen dokumentiert (ISMS-IMP-A.8.2-3-5)

**Stage 2 (Operationale Wirksamkeit) Nachweise:**

Erforderliche Nachweise zur Demonstration operationaler Wirksamkeit:

**A.8.5 (Authentifizierung)**:
- Inventar der Authentifizierungsmechanismen
- MFA-Registrierungsberichte und Abdeckungskennzahlen
- Passwortrichtlinienkonfigurationen
- SSO-Anwendungsintegrationsstatus
- Stichproben von Authentifizierungsprotokollen

**A.8.2 (Privilegierter Zugang)**:
- Inventar privilegierter Konten mit Tier-Klassifikation
- PAM-Lösungs-Deployment-Dokumentation
- Stichproben der Sitzungsaufzeichnungen (Tier 0)
- Vierteljährliche Zugriffsüberprüfungsbestätigungen
- Zugangsdatenrotations-Protokolle

**A.8.3 (Zugangsbeschränkung)**:
- Zugangsmassnahmenkonfigurationen (Betriebssystem, Datenbank, Anwendung)
- Berechtigungsprüfungsberichte
- Penetrationstest-Befunde (Abschnitt Zugangsmassnahmen)
- Netzwerksegmentierungsdokumentation

**Bewertungsarbeitsmappen** (ISMS-IMP-A.8.2-3-5-Suite):
- Arbeitsmappe 1: Authentifizierungsinventar (A.8.5)
- Arbeitsmappe 2: MFA-Abdeckungsbewertung (A.8.5)
- Arbeitsmappe 3: Inventar privilegierter Konten (A.8.2)
- Arbeitsmappe 4: Überwachung privilegierter Zugänge (A.8.2)
- Arbeitsmappe 5: Compliance Zugangsbeschränkungen (A.8.3)

**Nachweisaufbewahrung**:
- Authentifizierungsprotokolle: Mindestens 12 Monate (länger gemäss regulatorischen Anforderungen)
- Zugriffsüberprüfungsbestätigungen: 3 Jahre
- Aufzeichnungen privilegierter Sitzungen: Mindestens 12 Monate
- Bewertungsarbeitsmappen: Aktuelle + 2 frühere Versionen

---

# Anhang A: Schnellreferenz Admin-Tiering

**Zweck**: Schnellreferenz für Administratoren zu Tier-Klassifikation und Isolierungsanforderungen.

## Tier-Klassifikations-Zusammenfassung

| Tier | Umfang | MFA-Anforderung | Workstation | Sitzungsaufzeichnung |
|------|--------|-----------------|-------------|---------------------|
| **Tier 0** | Domain/Unternehmen | Hardware (FIDO2) | PAW erforderlich | Verbindlich |
| **Tier 1** | Server/Anwendung | Authenticator-App | Dediziert empfohlen | Empfohlen |
| **Tier 2** | Workstation/Endgerät | Authenticator-App | Standard | Optional |

## Tier-Isolierungsregeln

**NIEMALS**:

- Tier-0-Konten auf Tier-1- oder Tier-2-Systemen
- Tier-1-Konten auf Tier-2-Systemen
- Tagesarbeit (E-Mail, Surfen) auf PAWs

**IMMER**:

- Getrennte Zugangsdaten je Tier
- Unterschiedliche Passwörter je Tier-Konto
- Dedizierte PAWs für Tier-0-Administration

## Reaktion auf Tier-Verletzungen

Alle Tier-Verletzungen generieren KRITISCHE Alarme. Wiederholte Verstösse führen zu:
1. Erstes Vorkommnis: Schulung und dokumentierte Verwarnung
2. Zweites Vorkommnis: Manager-Eskalation
3. Drittes Vorkommnis: Sperrung des privilegierten Zugangs bis zur Überprüfung

---

# Genehmigungsnachweis

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date to be set] |
| **IT-Leiter (ITL)** | [Name] | [Date to be set] |
| **IT-Betriebsleiter** | [Name] | [Date to be set] |
| **Rechts-/Compliance-Officer** | [Name] | [Date to be set] |
| **Geschäftsleitung** | [Name] | [Date to be set] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt die Anforderungen für Authentifizierungssicherheit, Privileged Access Management und technische Zugangsdurchsetzung fest. Implementierungsverfahren, Bewertungsmethoden und Arbeitsmappenspezifikationen sind in ISMS-IMP-A.8.2-3-5 (UG/TG) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
