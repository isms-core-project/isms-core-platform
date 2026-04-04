<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.15-16-18-DE:operational:OP-POL:a.5.15-16-18 -->
**ISMS-OP-POL-A.5.15-16-18 — Identitäts- und Zugangsverwaltung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Identitäts- und Zugangsverwaltung |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.5.15-16-18 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
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

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Controls A.5.15, A.5.16, A.5.18 — Access control, identity management, access rights

**Verwandte Annex-A-Kontrollen**:

| Kontrolle | Bezug zur IAM |
|-----------|---------------|
| A.5.3 Aufgabentrennung | SoD-Matrix durch Zugriffskontrollen durchgesetzt |
| A.5.10 Akzeptable Nutzung von Informationen | Akzeptable Nutzung hängt vom gewährten Zugriff ab |
| A.5.12–13 Klassifizierung und Kennzeichnung | Klassifizierung bestimmt die erforderliche Zugriffsebene |
| A.5.17 Authentifizierungsinformationen | Credential-Management für authentifizierte Identitäten |
| A.5.19–23 Lieferantenbeziehungen | Governance des Drittanbieter-Zugriffs |
| A.5.24–28 Vorfallsmanagement | Handhabung von Konto-Kompromittierungsvorfällen |
| A.8.2 Privilegierte Zugriffsrechte | Management privilegierter Zugänge |
| A.8.3 Informationszugriffsbeschränkung | Technische Durchsetzung von Zugriffsregeln |
| A.8.5 Sichere Authentifizierung | Authentifizierungsmechanismen zur Identitätsverifikation |
| A.8.11 Datenmaskierung | Maskierungskontrollen an Zugriffsklassifizierung ausgerichtet |

**Verwandte interne Richtlinien**:

- Richtlinie zur Informationsklassifizierung und -handhabung
- Authentifizierungs- und Privileged-Access-Richtlinie
- Vorfallsmanagement-Richtlinie
- Informationsübertragungs-Richtlinie
- Richtlinie zur sicheren Entwicklung

---

# Zugangskontroll-Richtlinie

## Zweck

Der Zweck dieser Richtlinie ist es, den korrekten Zugang zu den korrekten Informationen und Ressourcen durch die korrekten Personen zu gewährleisten und den gesamten Lebenszyklus von Benutzeridentitäten zu verwalten.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG), indem sie technische und organisatorische Massnahmen proportional zum Risiko zum Schutz personenbezogener Daten (einschliesslich sensibler Personendaten) durch Zugriffskontrollen umsetzt. Wo die Organisation Daten natürlicher Personen im EU/EWR-Raum verarbeitet, gelten auch DSGVO-Anforderungen.

## Geltungsbereich

Alle Mitarbeitenden und Drittnutzer.
Alle Systeme und Anwendungen, die gemäss dem ISO 27001-Geltungsbereich in Scope sind.
Der physische Zugang ist in der Physischen und Umwelt-Richtlinie definiert.

## Grundsatz

Zugangskontrolle wird nach dem Prinzip der minimalen Rechtevergabe gewährt. Nutzern wird nur Zugriff auf die Informationen gewährt, die sie zur Erfüllung ihrer Aufgaben und Rolle benötigen.

Zugriff wird standardmässig verweigert und nur mit dokumentierter Genehmigung gewährt. Alle Zugriffsentscheidungen müssen risikobasiert sein und die Klassifizierung der Informationen sowie die Kritikalität des Systems berücksichtigen.

---

## Geheimhaltungsvereinbarungen

Alle Mitarbeitenden und Auftragnehmer, denen Zugang zu vertraulichen Informationen gewährt wird, müssen vor der Gewährung des Zugangs zu Informationsverarbeitungseinrichtungen eine Geheimhaltungs- oder Vertraulichkeitsvereinbarung unterzeichnen.

## Rollenbasierter Zugang

Der Zugang zu Systemen basiert auf der Rolle. Der Zugriff wird vom Geschäftseigentümer, Systemeigentümer oder Dateneigentümer gewährt und formal genehmigt.

Die Organisation muss rollenbasierte Zugangskontrolle (RBAC) als bevorzugte Methode für die Zugriffszuweisung implementieren. Rollen müssen dokumentiert und jährlich von Geschäftseigentümern überprüft werden.

## Eindeutige Kennung

Nutzern wird eine eindeutige Benutzerkennung oder ID nach dem Prinzip eines Nutzers, einer ID zugewiesen, um individuelle Verantwortlichkeit zu gewährleisten. Benutzernamen und Kennungen dürfen nicht zwischen Nutzern geteilt werden.

Gemeinsam genutzte Konten sind verboten, ausser wo technisch unvermeidbar (Legacy-Systeme, vom Anbieter erforderliche Konten). Jede Ausnahme erfordert schriftliche ISB-Genehmigung mit dokumentierter Geschäftsbegründung, Ausgleichskontrollen (individuelle Benutzerprotokollierung, vierteljährliche Überprüfung) und formale Risikoakzeptanz. Gemeinsam genutzte Konten müssen im Privileged-Account-Register aufgenommen werden.

## Zugangsauthentifizierung

Nutzer werden positiv identifiziert und authentifiziert, bevor sie Zugang zu Systemen, Diensten oder Informationen erhalten.

Multi-Faktor-Authentifizierung (MFA) muss gefordert werden für:

- Alle Fernzugänge zu Organisationsnetzwerken und Cloud-Diensten.
- Alle privilegierten und Administrator-Konten.
- Alle extern zugänglichen Anwendungen.
- Alle Systeme, die vertrauliche oder personenbezogene Daten verarbeiten.

Systeme, die MFA nicht unterstützen können, müssen im Risikoregister mit technischer Begründung, Ausgleichskontrollen (z. B. Netzwerksegmentierung, erweiterte Überwachung) und ISB-genehmigter, jährlich überprüfter Risikoakzeptanz dokumentiert werden.

## Überprüfung der Zugriffsrechte

Der Benutzerzugang zu Systemen muss regelmässig überprüft werden, um sicherzustellen, dass er noch angemessen und relevant ist:

| Kontotyp | Überprüfungsfrequenz |
|----------|---------------------|
| Privilegierte / Administrator-Konten | Vierteljährlich |
| Drittanbieter- / Auftragnehmer-Zugriff | Vierteljährlich |
| Service-Konten | Vierteljährlich |
| Standard-Benutzerkonten | Jährlich |

Inaktive und ruhende Konten müssen untersucht werden. Ein Konto gilt als inaktiv, wenn es sich innerhalb des festgelegten Zeitraums nicht erfolgreich authentifiziert hat. Konten, die länger als 45 Tage inaktiv sind, müssen deaktiviert werden. Konten, die länger als 90 Tage inaktiv sind, müssen entfernt werden, es sei denn, eine dokumentierte Geschäftsbegründung besteht.

Service-Konten sind von der inaktivitätsbasierten Deaktivierung ausgenommen, müssen aber vierteljährlich überprüft werden, um zu verifizieren, dass sie noch aktiv genutzt werden und noch benötigt werden. Unbenutzte Service-Konten müssen sofort bei der Entdeckung deaktiviert werden.

## Privilegierte Konten / Administrator-Konten

Administrator-Konten dürfen Nutzern nicht für Standardaufgaben bereitgestellt werden, einschliesslich, aber nicht beschränkt auf Laptops und Mobilgeräte.

Wo machbar, müssen privilegierten und Administrator-Nutzern spezifische privilegierte Konten zusätzlich zu ihrem normalen Konto zugewiesen werden, für die spezifische Verwendung zur Ausführung privilegierter und Administrator-Aufgaben.

Privilegierte und Administrator-Konten müssen:

- Keine gemeinsam genutzten oder generischen Konten sein.
- Klar identifizierbar sein (Namenskonvention).
- Protokolliert und überwacht werden.
- Wo machbar zeitlich begrenzt sein (Just-in-Time-Zugriff bevorzugt).
- In einem gepflegten Inventar registriert sein.

## Service-Konten

Service-Konten (nicht-menschliche Konten, die von Anwendungen, Skripten oder automatisierten Prozessen verwendet werden) müssen gemäss folgenden Anforderungen verwaltet werden:

- Die Erstellung von Service-Konten muss vom Systemeigentümer und ISB genehmigt werden.
- Alle Service-Konten müssen mit Zweck, System/Anwendung, Eigentümer und Überprüfungsdatum dokumentiert werden.
- Service-Konten dürfen nur die für ihre Funktion erforderlichen Mindestberechtigungen erhalten.
- Service-Konten dürfen nicht für interaktive Anmeldungen durch Personal verwendet werden.
- Service-Konto-Credentials müssen in einer genehmigten Secrets-Management-Lösung gespeichert werden, nicht hartcodiert oder im Klartext gespeichert.
- Service-Konto-Aktivitäten müssen protokolliert und auf anomales Verhalten überwacht werden.
- Service-Konten müssen gemäss dem Zugriffsüberprüfungsplan vierteljährlich überprüft werden.

## Passwörter

Der Zugang zu Systemen und Informationen wird durch Passwörter authentifiziert. Die Organisation muss folgende Passwortstandards durchsetzen:

| Anforderung | Standard |
|-------------|----------|
| Mindestlänge | 12 Zeichen |
| Komplexität | Länge über Komplexität; keine obligatorischen Kompositionsregeln (gemäss NIST SP 800-63B) |
| Screening | Passwörter müssen gegen bekannte kompromittierte/datenpannen-betroffene Credential-Datenbanken validiert werden |
| Rotation | Nur ereignisbasiert — bei vermutetem oder bestätigtem Kompromiss; regelmässige erzwungene Rotation ist nicht erforderlich |
| Erstpasswörter | Müssen bei der ersten Verwendung geändert werden |
| Standardpasswörter | Vom Anbieter gelieferte und Standardpasswörter müssen sofort bei der Installation geändert werden |
| Weitergabe | Passwörter dürfen nicht generisch, geteilt oder auf Gruppenebene gesetzt sein |
| Vertraulichkeit | Passwörter müssen vertraulich gehalten und nicht aufgeschrieben werden |
| Anzeige | Passwörter dürfen bei der Eingabe nicht angezeigt werden |
| Code | Passwörter dürfen nicht in Skripten, Code oder Makros codiert oder eingeschlossen sein |
| Übertragung | Passwörter müssen bei der Netzwerkübertragung verschlüsselt sein |
| Speicherung | Passwörter müssen mit genehmigten kryptographischen Hash-Funktionen gespeichert werden (bcrypt, scrypt, Argon2 oder PBKDF2) und niemals im Klartext oder mit umkehrbarer Verschlüsselung |
| Kontosperrung | Systeme müssen Nutzer nach 6 fehlgeschlagenen Zugriffsversuchen sperren |
| Session-Timeout | System-Sessions, die 15 Minuten lang inaktiv sind, müssen erneute Authentifizierung erfordern (5 Minuten für Systeme, die sensible Personendaten oder Finanzdaten verarbeiten) |
| Passwortmanager | Die Verwendung von von der Organisation genehmigten Passwortmanagern wird empfohlen |

## Bereitstellung von Benutzerkonten

Kontoerstellung, -änderung und -löschung müssen von autorisiertem Personal durchgeführt und vollständig dokumentiert werden.

Die Organisation muss einen Joiner-Mover-Leaver (JML)-Prozess implementieren:

| HR-Ereignis | Zugriffsmasnahme | Zeitrahmen |
|-------------|-----------------|-----------|
| Neueinstellung | Kontoerstellung mit rollenbasiertem Zugriff | Zugriff bis zum Startdatum bereit |
| Rollenwechsel | Zugriff an neue Rolle angepasst; vorheriger Zugriff entfernt | Innerhalb von 2 Arbeitstagen |
| Kündigung (freiwillig) | Alle Zugänge widerrufen | Am gleichen Arbeitstag |
| Kündigung (fristlos) | Alle Zugänge widerrufen | Sofort (innerhalb von 1 Stunde) |
| Vertragsende | Auftragnehmer-/Anbieterzugang entfernt | Am Vertragsabschluss-Datum |

Geschäfts-, System- oder Informationseigentümer müssen den Zugang zu Systemen und Informationen genehmigen. Ein dokumentierter Antrag muss den erforderlichen Zugang klar angeben und ein Genehmigungsnachweis muss aufbewahrt werden.

**Zugriffsantragsworkflow:**

1. Nutzer reicht Antrag über IT-Service-Desk oder Zugangsverwaltungstool ein und gibt System, Rolle und Geschäftsbegründung an.
2. Vorgesetzter genehmigt den Geschäftsbedarf.
3. System- oder Dateneigentümer genehmigt die Zugriffsebene.
4. IT stellt den Zugriff bereit und zeichnet die Genehmigung auf.
5. Antragsteller bestätigt, dass der Zugriff funktioniert.

Notfallzugriff (Break-Glass) kann von IT mit mündlicher ISB-Genehmigung gewährt werden und muss innerhalb von 1 Arbeitstag formal dokumentiert werden.

Alle Nutzer, die Passwortrücksetzungen oder Änderungen an Authentifizierungs-Credentials beantragen, müssen ihre Identität durch mindestens eine der folgenden Methoden verifizieren:

- Verifikation eines vorregistrierten Sekundärkontakts (E-Mail, Telefon).
- Challenge-Response unter Verwendung vorher festgelegter Sicherheitsfragen.
- Persönliche Verifikation mit Lichtbildausweis.
- Bestätigung der Identität des Nutzers durch Vorgesetzten oder HR.

Selbstbedienungs-Passwortrücksetzung über den Identitätsanbieter (mit verifizierter MFA-Registrierung) ist akzeptabel und erfordert keine zusätzliche Identitätsverifikation.

## Ausscheidende Mitarbeitende

Vorgesetzte und HR müssen das Konto-Bereitstellungsteam über das Abgangsdatum eines Nutzers informieren.

Wenn ein Nutzer die Organisation verlässt, müssen alle Zugänge am gleichen Arbeitstag widerrufen werden, mindestens zur Hauptauthentifizierungstechnologie und zu allen in der rollenbasierten Zugriffsliste aufgeführten Systemen und Daten.

Benutzer-IDs, Passwörter und Authentifizierungs-Credentials ausscheidender Mitarbeitender dürfen nicht wiederverwendet werden.

## Authentifizierung

Das Hauptzugriffsauthentifizierungssystem muss:

- System- oder Anwendungskennungen nicht anzeigen, bis der Anmeldevorgang erfolgreich abgeschlossen wurde.
- Eine allgemeine Warnung anzeigen, dass das System nur von autorisierten Nutzern aufgerufen werden darf.
- Während des Anmeldeverfahrens keine Hilfsmeldungen bereitstellen, die einem nicht autorisierten Nutzer helfen würden.
- Die Anmeldeinformationen nur nach Abschluss aller Eingabedaten validieren. Bei einem Fehler darf das System nicht angeben, welcher Teil der Daten korrekt oder falsch ist.
- Vor Brute-Force-Anmeldeversuchen schützen.
- Erfolglose und erfolgreiche Versuche protokollieren.
- Ein Sicherheitsereignis auslösen, wenn ein potenzieller Versuch oder erfolgreicher Verstoss gegen Anmeldekontrollen erkannt wird.
- Ein eingegebenes Passwort nicht anzeigen.
- Passwörter nicht im Klartext über ein Netzwerk übertragen.
- Inaktive Sessions nach einem definierten Inaktivitätszeitraum beenden, insbesondere an Hochrisikoorten wie öffentlichen oder externen Bereichen ausserhalb des Sicherheitsmanagements der Organisation oder auf Mobilgeräten.
- Verbindungszeiten beschränken, um zusätzliche Sicherheit für Hochrisiko-Anwendungen zu bieten.

## Fernzugang

Der Fernzugang zu Organisationsnetzwerken, Cloud-basierten Diensten und extern zugänglichen Anwendungen folgt denselben Regeln dieser Richtlinie mit der zusätzlichen Anforderung der Multi-Faktor-Authentifizierung.

Fernverbindungen müssen nach einem definierten Inaktivitätszeitraum auf Trennung gesetzt werden.

Eine Liste der Nutzer mit Fernzugang zu internen Netzwerksystemen muss gepflegt und vierteljährlich überprüft werden.

## Fernzugang Dritter

Der Zugang wird Dritten nur unter einem laufenden Vertrag mit einer entsprechenden Geheimhaltungsvereinbarung gewährt.

Der Zugang wird für einen bestimmten Zeitraum, für ein bestimmtes System, für eine bestimmte Person und auf Erhalt eines formellen, gültigen, autorisierten Zugriffsantrags gewährt.

Der Zugang muss sofort nach Abschluss der Anforderung oder bei Vertragsende entfernt werden, je nachdem was zuerst eintritt.

Eine Liste der Dritten und Personen mit Zugang muss gepflegt und vierteljährlich überprüft werden.

## Überwachung und Berichterstattung

Der Zugang zu Systemen muss überwacht und gemeldet werden. Aktionen, die direkt oder indirekt die Vertraulichkeit, Integrität oder Verfügbarkeit von Daten beeinflussen oder beeinflussen könnten, müssen über den Vorfallsmanagement-Prozess verwaltet werden.

## Datenmaskierung

Die Organisation maskiert Daten gemäss gesetzlichen und regulatorischen Verpflichtungen, einschliesslich der Anforderungen des schweizerischen nDSG und der DSGVO, wo anwendbar.

---

## Nachweise

Die folgenden Nachweise demonstrieren die Einhaltung dieser Richtlinie:

- **Benutzerkonto-Inventar** (aktive Konten nach Typ: Mitarbeitende, Auftragnehmer, Service, geteilt) — *im Identitätsanbieter oder Zugangsverwaltungstool gepflegt; vierteljährlich exportiert*
- **JML-Prozessunterlagen** (Workflow-Protokolle für Joiner/Mover/Leaver mit Zeitstempeln) — *12 Monate nach Abgang aufbewahrt; halbjährlich auditiert*
- **Zugriffsüberprüfungs-Abschlussunterlagen** (vierteljährlich privilegiert, jährlich Standard) — *von Systemeigentümern unterzeichnet; 3 Jahre aufbewahrt*
- **Protokolle zur Behebung verwaister/ruhender Konten** — *monatlich überprüft; deaktivierte Konten dokumentiert*
- **MFA-Registrierungsunterlagen** über Systeme — *Coverage-Bericht vierteljährlich generiert; Ziel 100% für In-Scope-Systeme*
- **Privilegiertes Konto-Register und Nutzungsprotokolle** — *vierteljährlich überprüft; anomale Nutzung untersucht*
- **Service-Konto-Register** (Eigentümer, Zweck, System, Überprüfungsdatum) — *vierteljährlich überprüft*
- **Drittanbieter-Zugriffsregister** mit Vertragsablaufdaten — *vierteljährlich überprüft; Zugriff bei Vertragsende widerrufen*
- **Passwortkonfigurations-Nachweise** (System-Screenshots oder Audit-Exporte) — *jährlich oder bei Änderung erfasst*
- **Zugriffsantrags- und Genehmigungsunterlagen** — *12 Monate aufbewahrt; Stichprobe bei internen Audits geprüft*

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheitsmanagement-Team wird die Einhaltung dieser Richtlinie durch verschiedene Methoden überprüfen, einschliesslich, aber nicht beschränkt auf, Zugriffsüberprüfungsberichte, JML-Audit-Trails, Überwachung privilegierter Zugänge, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vom Informationssicherheitsmanager im Voraus genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum. Ausnahmen müssen dem Management-Review-Team gemeldet werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterliegen, bis hin zur Beendigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen müssen Änderungen der Identitäts- und Zugangsverwaltungsstandards, aufkommende Bedrohungen, regulatorische Änderungen und Lessons Learned aus Vorfällen berücksichtigen.

---

# Bereiche des ISO 27001-Standards, die adressiert werden

Identitäts- und Zugangsverwaltungs-Richtlinie — ISO 27001-Kontrollzuordnung

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.3 Aufgabentrennung |
| Klausel 6.2 Informationssicherheitsziele | 5.4 Managementverantwortung |
| Klausel 7.3 Bewusstsein | **5.15 Zugangskontrolle** |
| Klausel 7.5.3 Steuerung dokumentierter Informationen | **5.16 Identitätsverwaltung** |
| | 5.17 Authentifizierungsinformationen |
| | **5.18 Zugriffsrechte** |
| | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| | 8.2 Privilegierte Zugriffsrechte |
| | 8.3 Informationszugriffsbeschränkung |
| | 8.5 Sichere Authentifizierung |
| | 8.11 Datenmaskierung |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen einschliesslich Zugriffskontrollen |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (soweit anwendbar) | Art. 32 — Sicherheit der Verarbeitung (Zugriffskontrollen als angemessene Massnahme) |
| ISO/IEC 27001:2022 | Annex A Kontrollen 5.15, 5.16, 5.18 |
| ISO/IEC 27002:2022 | Abschnitte 5.15, 5.16, 5.18 — Umsetzungshinweise |
| NIST SP 800-63B | Richtlinien für digitale Identität und Authentifizierung |
| CIS Controls v8 | Kontrollen 5 (Account Management) und 6 (Access Control Management) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
