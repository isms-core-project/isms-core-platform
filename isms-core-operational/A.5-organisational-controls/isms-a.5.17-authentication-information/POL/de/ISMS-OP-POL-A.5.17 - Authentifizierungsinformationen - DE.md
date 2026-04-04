<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.17-DE:operational:OP-POL:a.5.17 -->
**ISMS-OP-POL-A.5.17 — Authentifizierungsinformationen**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Authentifizierungsinformationen |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.5.17 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
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

- ISO/IEC 27001:2022 Kontrolle A.5.17 — Authentifizierungsinformationen
- NIST SP 800-63B-4 — Digital Identity Guidelines: Authentication and Authenticator Management

**Verwandte Annex-A-Kontrollen**:

| Kontrolle | Bezug zu Authentifizierungsinformationen |
|-----------|------------------------------------------|
| A.5.15–18 Zugriffskontrolle und Identitätsverwaltung | Identitätslebenszyklus fliesst in Authentifizierung; Zugriffsrechte bestimmen den Umfang der Anmeldedaten |
| A.5.24–28 Incident Management | Kompromittierte Anmeldedaten lösen Incident Response und erzwungene Passwortänderung aus |
| A.8.2 Privilegierte Zugriffsrechte | Privilegierte Konten erfordern strengere Authentifizierung (MFA, Hardware-Schlüssel) |
| A.8.3 Informationszugriffsbeschränkung | Authentifizierung setzt Zugriffsgrenzen durch |
| A.8.5 Sichere Authentifizierung | Technische Implementierung der Authentifizierungsmechanismen |
| A.8.15 Protokollierung | Authentifizierungsereignisse fliessen in die zentrale Protokollierung |
| A.8.16 Überwachungsaktivitäten | Echtzeit-Überwachung von Authentifizierungsfehlern und Anomalien |
| A.8.24 Einsatz von Kryptografie | Kryptografischer Schutz von Anmeldedaten, Tokens und Passwort-Hashes |

**Verwandte interne Richtlinien**:

- Richtlinie zur Identitäts- und Zugangsverwaltung
- Richtlinie zur Authentifizierung und privilegierten Zugriffen
- Richtlinie zum Einsatz von Kryptografie
- Protokollierungsrichtlinie
- Richtlinie zu Überwachungsaktivitäten (A.8.16)
- Richtlinie zum Incident Management

---

# Richtlinie zu Authentifizierungsinformationen

## Zweck

Diese Richtlinie soll sicherstellen, dass Authentifizierungsinformationen über definierte Lebenszyklusverfahren sicher zugeteilt, verwaltet, geschützt und widerrufen werden und dass das Personal in der sicheren Handhabung von Authentifizierungsdaten unterwiesen wird.

Diese Richtlinie legt Anforderungen an Passwortstandards, Multi-Faktor-Authentifizierung, Anmeldedatenverteilung und den Schutz von Authentifizierungsgeheimnissen fest, um unbefugten Zugriff auf die Systeme und Daten der Organisation zu verhindern.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 8, indem sie technische und organisatorische Massnahmen entsprechend dem Risiko zum Schutz personenbezogener Daten (einschliesslich besonders schützenswerter Personendaten) durch Authentifizierungskontrollen umsetzt. Soweit die Organisation Daten von Personen in der EU/EEA verarbeitet, gelten auch die DSGVO-Anforderungen.

## Geltungsbereich

Diese Richtlinie gilt für:

- Alle Mitarbeitenden, Auftragnehmer und Drittnutzer mit Zugang zu den Systemen der Organisation.
- Alle Authentifizierungsinformationen einschliesslich Passwörter, Passphrasen, PINs, kryptografische Schlüssel, Tokens, biometrische Templates, API-Schlüssel, Zertifikate und andere Authentifizierungsgeheimnisse.
- Alle Systeme, Anwendungen, Cloud-Dienste, Netzwerkgeräte und Datenbanken, die der Organisation gehören oder von ihr betrieben werden und im ISO-27001-Anwendungsbereich enthalten sind.
- Alle Authentifizierungslebenszyklusprozesse: Zuteilung, Verteilung, Nutzung, Speicherung, Zurücksetzung und Widerruf.

## Grundsatz

Authentifizierungsinformationen sollten auf den Grundsätzen der Vertraulichkeit, individuellen Rechenschaftspflicht und Tiefenverteidigung verwaltet werden. Jeder Benutzer sollte positiv identifiziert und authentifiziert werden, bevor er auf Systeme oder Daten zugreift. Authentifizierungsmechanismen sollten der Sensitivität der abgerufenen Informationen und Systeme angemessen sein.

Passwörter allein sind für Hochrisikozugriffe nicht ausreichend. Multi-Faktor-Authentifizierung bietet geschichteten Schutz gegen die Kompromittierung von Anmeldedaten. Authentifizierungskontrollen sollten risikobasiert sein und die Klassifizierung der Informationen sowie die Kritikalität des Systems berücksichtigen.

---

## Authentifizierungsinfrastruktur

> **Systemspezifikation**: Die Organisation nutzt die folgenden Systeme zur Implementierung von Authentifizierungskontrollen. Platzhalterverweise (z. B. [Identity Provider]) in dieser Richtlinie beziehen sich auf die unten aufgeführten Systeme.
>
> | Funktion | System/Tool | Eigentümer |
> |----------|-------------|------------|
> | **Identity Provider (IdP)** | [z. B. Microsoft Entra ID, Okta, Google Workspace Identity] | IT-Betrieb / IAM-Team |
> | **Passwort-Manager** | [z. B. 1Password Business, Bitwarden Enterprise, KeePass + zentralisierte Synchronisation] | IT-Sicherheit |
> | **MFA-Plattform** | [z. B. integriertes IdP-MFA, Duo Security, YubiKey-Verwaltung] | IT-Betrieb |
> | **Privileged Access Management (PAM)** | [z. B. CyberArk, Delinea Secret Server, HashiCorp Vault] | IT-Sicherheit |
> | **Verletzungsprüfungsdienst** | [z. B. Have I Been Pwned API (k-Anonymitätsmodell), Enzoic, Microsoft Password Protection] | IT-Betrieb |
> | **SIEM / Log-Management** | [z. B. Microsoft Sentinel, Splunk, Elastic SIEM] | IT-Sicherheit |

---

## Zuteilung von Authentifizierungsinformationen

### Identitätsverifizierung

Vor der Ausstellung neuer oder Ersatz-Authentifizierungsdaten sollte die Identität der anfragenden Person durch mindestens eine der folgenden Methoden verifiziert werden:

- Verifizierung eines vorregistrierten sekundären Kontakts (E-Mail, Mobilnummer).
- Persönliche Verifizierung mit Lichtbildausweis.
- Bestätigung der Identität des Benutzers durch Vorgesetzte oder HR.
- MFA-verifizierter Self-Service-Prozess über den Identity Provider [Identity Provider].

Die verwendete Verifizierungsmethode sollte für Prüfzwecke dokumentiert werden.

### Sichere Verteilung

Authentifizierungsinformationen sollten über sichere Kanäle verteilt werden. Unsichere Methoden wie unverschlüsselte E-Mails oder Klartextnachrichten dürfen nicht für die Anmeldedatenverteilung verwendet werden.

| Authentifizierungstyp | Verteilungsmethode |
|-----------------------|--------------------|
| **Initiale Passwörter** | Sicherer Kanal (verschlüsselte E-Mail, versiegelter Umschlag oder Identity-Provider-Selbstregistrierung); getrennt vom Benutzernamen; erzwungene Änderung bei erster Verwendung |
| **Tokens / Hardware-Schlüssel** | Persönliche Übergabe mit Identitätsverifizierung und unterschriebenem Empfangsbeleg |
| **Zertifikate** | Sicherer Zertifikatsregistrierungsprozess; verifizierte E-Mail oder Identity-Provider-Workflow |
| **API-Schlüssel** | Verschlüsselter Kanal; begrenzte Gültigkeitsdauer; Ausstellung protokolliert; im Secrets-Vault gespeichert |

### Temporäre Authentifizierung

Temporäre Authentifizierungsdaten (Initialpasswörter, Zurücksetzungs-Tokens, Einmalcodes):

- Sollten eine maximale Gültigkeitsdauer von 24 Stunden haben.
- Sollten bei erster Verwendung geändert werden müssen.
- Sollten mit ausreichender Zufälligkeit und Länge generiert werden, um Rateangriffe zu widerstehen.
- Sollten nach erfolgreicher Verwendung ungültig gemacht werden.

### Verwaltung von Standard-Anmeldedaten

Vom Hersteller bereitgestellte und Standard-Passwörter sollten unmittelbar nach der Installation geändert werden, bevor ein System mit dem Produktionsnetzwerk verbunden wird.

Standard-Konten sollten deaktiviert oder umbenannt werden, sofern technisch möglich.

Wo Standard-Anmeldedaten nicht geändert werden können (Herstellerfirmware-Abhängigkeit, Systembeschränkung), sollten die folgenden Ausgleichskontrollen angewendet werden:

- Einzigartiges starkes Passwort pro Gerät festgelegt (nicht der Herstellerstandard).
- Netzwerksegmentierung, die den Zugriff auf das Gerät einschränkt.
- MFA angewendet, sofern unterstützt.
- Erweiterte Überwachung und Alarmierung für das Konto.
- Anmeldedaten im genehmigten Vault gespeichert [Password Manager].
- Dokumentierte Ausnahme mit ISB-Genehmigung und jährlicher Überprüfung.

---

## Passwortanforderungen

### Passwortstandards (NIST SP 800-63B-konform)

Die Organisation sollte die folgenden Passwortstandards durchsetzen, die mit NIST SP 800-63B-4 abgestimmt sind:

| Anforderung | Standard |
|-------------|----------|
| **Mindestlänge** | 12 Zeichen (15 Zeichen, wenn das Passwort der einzige Authentifikator ohne MFA ist) |
| **Maximale Länge** | Systeme sollten mindestens 64 Zeichen akzeptieren, um Passphrasen zu unterstützen |
| **Zeichenunterstützung** | Alle druckbaren ASCII-Zeichen (einschliesslich Leerzeichen) und Unicode sollten akzeptiert werden |
| **Komplexitätsregeln** | Keine obligatorischen Kompositionsregeln (keine erforderliche Mischung aus Gross-/Kleinbuchstaben, Zahlen, Symbolen); Länge ist der primäre Stärkefaktor |
| **Verletzungsprüfung** | Passwörter sollten bei der Erstellung gegen bekannte kompromittierte/geleakte Anmeldedatendatenbanken validiert werden (z. B. Have I Been Pwned API oder entsprechendes Verletzungskorpus, integriert in [Identity Provider]). **Prüfhäufigkeit**: Bei der Passworterstellung (obligatorisch), bei jeder Authentifizierung sofern technisch möglich (Echtzeit-Prüfung über IdP-Integration) und Batch-Prüfung aller gespeicherten Passwort-Hashes vierteljährlich (Offline-Prüfung gegen aktualisiertes Verletzungskorpus). |
| **Rotation** | Nur ereignisbasiert — bei vermutetem oder bestätigtem Kompromiss, Entdeckung gemeinsamer Anmeldedaten oder Änderung der Personalrolle, die den Zugriffsumfang betrifft; periodische erzwungene Rotation ist nicht erforderlich |
| **Initialpasswörter** | Sollten bei erster Verwendung geändert werden |
| **Standard-Passwörter** | Vom Hersteller bereitgestellte und Standard-Passwörter sofort nach der Installation geändert |
| **Wiederverwendung** | Eine Passworthistorie von mindestens 24 vorherigen Passwörtern sollte geführt werden, um Wiederverwendung zu verhindern |
| **Teilen** | Passwörter sollten nicht generisch, geteilt oder auf Gruppenebene festgelegt werden |
| **Sperrung** | Systeme sollten Benutzer nach 6 fehlgeschlagenen Zugriffsversuchen sperren; Sperrdauer mindestens 15 Minuten oder bis zur manuellen Zurücksetzung |
| **Passwort-Manager** | Die Verwendung von organisationsgenehmigten Passwort-Managern [Password Manager] wird empfohlen und unterstützt; Systeme sollten das Einfügen in Passwortfelder erlauben |

**Passwortstandards für privilegierte Konten**:

Privilegierte Konten (Administrator-, Tier-0/1-Konten) sollten Folgendes durchsetzen:

- Mindestens 16 Zeichen (oder 24 Zeichen für Service-Konten).
- Sperrung nach 3 fehlgeschlagenen Versuchen.
- Verletzungsprüfung bei der Erstellung und bei jeder Authentifizierung, sofern technisch möglich.
- Speicherung im genehmigten Anmeldedaten-Vault [Password Manager].

**Begründung für ereignisbasierte Rotation**: NIST SP 800-63B-4 stellt fest, dass obligatorische periodische Passwortrotation zu schwächeren Passwörtern (vorhersehbare Muster, minimale inkrementelle Änderungen) ohne messbaren Sicherheitsvorteil führt. Ereignisbasierte Rotation kombiniert mit Verletzungsprüfung und MFA bietet stärkeren Schutz.

### Verbotene Passwortpraktiken

Das Personal darf nicht:

- Passwörter mit anderen Personen teilen, einschliesslich IT-Support-Personal.
- Passwörter an ungeschützten Orten aufschreiben (Haftnotizen, unverschlüsselte Dateien, Notizbücher).
- Passwörter in Klartextdateien, Dokumenten, Tabellen oder Browser-Autofill ohne einen genehmigten Passwort-Manager speichern.
- Dasselbe Passwort für mehrere Systeme oder Dienste verwenden.
- Passwörter in Skripte, Code, Makros oder Konfigurationsdateien aufnehmen.
- Passwörter über unverschlüsselte Kanäle übermitteln (E-Mail-Textkörper, Sofortnachricht, SMS).

### Passwortspeicherung

Systeme sollten Passwörter mit genehmigtem Einweg-Kryptografie-Hashing mit einzigartiger Passwortsalzung speichern:

- **Genehmigte Algorithmen**: bcrypt, Argon2id, scrypt oder PBKDF2 (mit der aktuellen Hardwarefähigkeit angemessener Iterationszahl).
- **Klartextspeicherung ist unter allen Umständen verboten.**
- **Reversible Verschlüsselung von Passwörtern ist verboten.**
- Passwortdatenbanken sollten mit Verschlüsselung im Ruhezustand geschützt und der Zugriff auf autorisierte Service-Konten beschränkt werden.

---

## Multi-Faktor-Authentifizierung

### MFA-Anforderungen

Multi-Faktor-Authentifizierung sollte für die folgenden Zugriffstypen erforderlich sein:

| Zugriffstyp | MFA-Anforderung |
|-------------|-----------------|
| **Fernzugriff** (VPN, Cloud-Dienste, extern zugängliche Anwendungen) | Obligatorisch |
| **Privilegierte / Administrator-Konten** | Obligatorisch |
| **Kritische Systeme und Infrastruktur** | Obligatorisch |
| **Systeme, die personenbezogene Daten verarbeiten** (nDSG / DSGVO-Bereich) | Obligatorisch |
| **E-Mail** (externer Zugriff) | Obligatorisch |
| **Cloud-Plattform-Administrationskonsolen** | Obligatorisch |
| **Standardmässiger interner Zugriff** (vor Ort, vertrauenswürdiges Netzwerk) | Risikobasiert; Implementierung durch Systemklassifizierung bestimmt und in der Bedingten-Zugriffs-Richtlinie von [Identity Provider] erfasst |

**MFA-Abdeckungsziele**:

- Privilegierte Benutzer: 100 % MFA-Registrierung ab Datum der Richtlinienwirksamkeit.
- Alle Benutzer (Fernzugriff): 100 % MFA-Durchsetzung.
- Alle Benutzer (gesamter Zugriff): 95 %+ MFA-Registrierung innerhalb von 12 Monaten nach Richtlinienannahme.

### MFA-Faktortypen

Akzeptable Authentifizierungsfaktoren sollten aus mindestens zwei verschiedenen Kategorien stammen:

| Faktorkategorie | Beispiele | Hinweise |
|-----------------|-----------|----------|
| **Etwas, das Sie wissen** | Passwort, Passphrase, PIN | Gemäss Passwortstandards oben |
| **Etwas, das Sie haben** | Hardware-Sicherheitsschlüssel (FIDO2/WebAuthn), Authenticator-App (TOTP), Smartcard | Auf einzelnen Benutzer registriert; Hardware-Schlüssel für privilegierten Zugriff bevorzugt |
| **Etwas, das Sie sind** | Fingerabdruck, Gesichtserkennung, Iris-Scan | Biometrisches Template sicher gespeichert; als lokaler Entsperrfaktor verwendet |

### MFA-Methodenpräferenz

MFA-Methoden sollten mit Präferenz für Phishing-Resistenz ausgewählt werden:

| Methode | Phishing-Resistenz | Empfohlene Verwendung |
|---------|--------------------|-----------------------|
| **Hardware-Sicherheitsschlüssel** (FIDO2/WebAuthn) | Hoch — kryptografisch an den Ursprung gebunden | Erforderlich für höchstprivilegierte Konten; empfohlen für alle Benutzer |
| **Passkeys** (gerätegebunden, nicht exportierbar) | Hoch — ursprungsgebunden, benutzerverifiziert | Für alle Zugriffstypen akzeptabel; gegenüber TOTP bevorzugt |
| **Authenticator-Apps** (TOTP) | Mittel — Codes können in Echtzeit phishing-gephisht werden | Für Standard- und mittelstark privilegierte Zugriffe akzeptabel |
| **Push-Benachrichtigungen** (mit Nummernabgleich) | Mittel — erfordert Nummernabgleich zur Minderung von Ermüdungsangriffen | Akzeptabel, wenn Nummernabgleich durchgesetzt wird |
| **SMS / Voice OTP** | Niedrig — anfällig für SIM-Swapping und Abfangen | Nur wenn keine andere Methode technisch möglich ist; dokumentierte Ausnahme erforderlich |

SMS-basiertes OTP sollte im Risikoregister mit einem Migrationsplan zu einer stärkeren Methode dokumentiert werden. Neue Systemimplementierungen sollten kein SMS-basiertes MFA als einzigen zweiten Faktor implementieren.

**Migrations-Roadmap für phishing-resistente Authentifizierung**:

Die Organisation sollte die Migration hin zu phishing-resistenter Authentifizierung (FIDO2/WebAuthn-Passkeys) als primäre MFA-Methode planen und durchführen. FIDO2 verwendet Public-Key-Kryptografie, die an den legitimen Dienstherkunft gebunden ist und die Phishing von Anmeldedaten verhindert, selbst wenn Benutzer durch betrügerische Websites getäuscht werden.

| Phase | Zeitrahmen | Umfang | Ziel |
|-------|------------|--------|------|
| **Phase 1 — Pilotprojekt** | Monate 1–3 | IT-Team, Sicherheitsteam, ISB | 100 % der Pilotgruppe verwendet FIDO2-Hardware-Schlüssel |
| **Phase 2 — Privilegierte Benutzer** | Monate 3–6 | Alle privilegierten/Admin-Konten, Führungskräfte | 100 % privilegierte Konten auf FIDO2/Passkeys |
| **Phase 3 — Hochrisikobenutzer** | Monate 6–12 | Benutzer mit Zugriff auf vertrauliche Daten, Remote-Mitarbeitende | 80 %+ der Hochrisikobenutzer migriert |
| **Phase 4 — Allgemeiner Rollout** | Monate 12–24 | Alle Benutzer | 90 %+ aller Benutzer verwenden phishing-resistentes MFA; SMS/Voice OTP eliminiert |

**Migrationsverfolgung**: Fortschritt wird vierteljährlich an den ISB gemeldet mit: migrierte Benutzer (Anzahl und %), verbleibende SMS/TOTP-Benutzer, Hindernisse (Legacy-Systeme, Benutzerresistenz), Inventarstatus der Hardware-Schlüssel.

### MFA-Wiederherstellungsprozess

Wenn ein Benutzer den Zugang zu seinem MFA-Gerät verliert (verlorenes Telefon, beschädigter Hardware-Schlüssel, Werksreset):

1. **Helpdesk-Kontakt**: Benutzer kontaktiert IT-Helpdesk mit Identitätsverifizierung (gleiche Vorgehensweise wie bei helpdeskunterstützter Passwort-Zurücksetzung).
2. **Temporärer Zugriff**: Helpdesk stellt einen zeitlich begrenzten Bypass-Code aus (maximale 24-Stunden-Gültigkeit, einmalige Verwendung), um sofortigen Zugriff während der MFA-Neuregistrierung zu ermöglichen.
3. **MFA-Neuregistrierung**: Benutzer registriert MFA innerhalb von 24 Stunden neu über das Self-Service-Portal von [Identity Provider]. Wenn die Neuregistrierung nicht innerhalb von 24 Stunden abgeschlossen wird, wird der Zugriff bis zum Abschluss der Registrierung gesperrt.
4. **Verlorener Hardware-Schlüssel**: Als Sicherheitsvorfall gemeldet (mögliche physische Kompromittierung). Vorheriger Schlüssel sofort deregistriert. Ersatzschlüssel über persönliche Übergabe mit Identitätsverifizierung ausgestellt.
5. **Backup-MFA-Methode**: Benutzer werden ermutigt, eine Backup-MFA-Methode zu registrieren (z. B. zweiter Hardware-Schlüssel sicher aufbewahrt, Backup-Authenticator-App). Privilegierte Benutzer sollten mindestens zwei unabhängige MFA-Methoden registrieren.
6. **Protokollierung**: Alle MFA-Wiederherstellungsereignisse im [SIEM] mit Benutzer, Zeitstempel, Verifizierungsmethode und verwendeter Wiederherstellungsmethode protokolliert. Anomale Muster (z. B. derselbe Benutzer, der MFA mehrmals wiederherstellt) werden innerhalb von 24 Stunden untersucht.

### Biometrische Authentifizierungsanforderungen

Wenn biometrische Authentifizierung verwendet wird (Fingerabdruck, Gesichtserkennung, Iris-Scan):

- **Template-Speicherung**: Biometrische Templates sollten wo technisch möglich lokal auf dem Gerät gespeichert werden (nicht zentralisiert). Wenn zentralisierte Speicherung erforderlich ist, sollten Templates im Ruhezustand mit AES-256 verschlüsselt werden.
- **Lebenderkennung**: Biometrische Systeme sollten Lebenderkennung implementieren, um Replay-Angriffe zu verhindern (z. B. Fotografien, Silikonfingerprägeabdrücke).
- **Fallback**: Eine nicht biometrische Fallback-Authentifizierungsmethode sollte immer verfügbar sein (Biometrik darf nicht der einzige Authentifizierungsfaktor sein).
- **Einwilligung**: Das Personal sollte eine informierte Einwilligung vor der biometrischen Registrierung geben, in Übereinstimmung mit den schweizerischen nDSG-Anforderungen für die Verarbeitung besonders schützenswerter Personendaten.
- **Widerruf**: Biometrische Templates sollten bei Beendigung des Arbeitsverhältnisses oder wenn die betreffende Person die Einwilligung widerruft, gelöscht werden.
- **Genauigkeit**: Biometrische Systeme sollten mit einer falschen Akzeptanzrate (FAR) konfiguriert werden, die dem Risikoniveau angemessen ist (empfohlen: FAR <= 1:50.000 für Standardzugriff, FAR <= 1:1.000.000 für privilegierten Zugriff).

### Systeme ohne MFA-Unterstützung

Systeme, die MFA nicht unterstützen können, sollten im Risikoregister dokumentiert werden mit:

- Technischer Begründung für die Einschränkung.
- Ausgleichskontrollen (Netzwerksegmentierung, IP-Beschränkung, erweiterte Überwachung, reduzierter Sitzungs-Timeout).
- ISB-genehmigte Risikoakzeptanz.
- Jährliche Überprüfung und Migrationsplan, sofern möglich.

---

## Schutz von Authentifizierungsinformationen

### Benutzerverantwortlichkeiten

Alle Mitarbeitenden sollten:

- Authentifizierungsinformationen vertraulich halten und sie nicht an andere Personen weitergeben.
- Starke, einzigartige Passwörter oder Passphrasen für jedes System verwenden.
- Den organisationsgenehmigten Passwort-Manager [Password Manager] zur sicheren Anmeldedatenspeicherung verwenden.
- Vermutete oder bestätigte Kompromittierung von Anmeldedaten sofort dem IT-Service-Desk und dem Sicherheitsteam melden.

### Reaktion auf Kompromittierung von Anmeldedaten

Wenn eine Kompromittierung von Anmeldedaten vermutet oder bestätigt wird:

1. **Sofortige Passwort-Zurücksetzung**: Betroffener Benutzer setzt Passwort über den Self-Service von [Identity Provider] (MFA-verifiziert) oder helpdeskunterstützten Prozess zurück. Bei privilegierten Konten: IT-Sicherheit erzwingt sofortige Passwort-Zurücksetzung.
2. **MFA-Überprüfung**: Verifizieren, dass MFA-Faktoren nicht manipuliert wurden (keine nicht autorisierten registrierten Geräte). Wenn verdächtige MFA-Geräte gefunden werden, alle MFA-Registrierungen entfernen und von einem vertrauenswürdigen Gerät neu registrieren.
3. **Sitzungsbeendigung**: Alle aktiven Sitzungen für das betroffene Konto sofort über die Admin-Konsole von [Identity Provider] beendet.
4. **Bewertung des Verletzungsumfangs**: IT-Sicherheit untersucht: Was wurde mit den kompromittierten Anmeldedaten abgerufen? Waren andere Konten betroffen (Wiederverwendung von Anmeldedaten)? Wurden Daten exfiltriert?
5. **Verletzungsprüfung**: Kompromittierten Passwort-Hash gegen Verletzungskorpus prüfen. Wenn in externer Verletzungsdatenbank gefunden, Umfang der Exposition bewerten.
6. **Benachrichtigung**: Wenn die Kompromittierung einen Zugriff auf personenbezogene Daten umfasste, Benachrichtigungspflichten gemäss A.5.24–28 Incident Management und geltendem Datenschutzrecht bewerten.
7. **Ursachenanalyse**: Bestimmen, wie Anmeldedaten kompromittiert wurden (Phishing, Malware, Social Engineering, Brute Force, Verletzung externer Dienste). Gezielte Abhilfemassnahmen implementieren (z. B. Phishing-Sensibilisierungsschulung, wenn Phishing der Angriffsvektor war).
8. **Dokumentation**: Vorfall in [ITSM Tool] erfasst mit: betroffenes Konto, Kompromittierungsvektor, Umfang des Zugriffs während des Kompromittierungsfensters, Abhilfemassnahmen, Ursache, Präventivmassnahmen.

Zusätzlich sollten alle Mitarbeitenden:

- Anderen nicht erlauben, ihre Anmeldedaten zu verwenden oder sich in ihrem Namen zu authentifizieren.
- MFA-Registrierung innerhalb des erforderlichen Zeitrahmens abschliessen.
- Nicht versuchen, Authentifizierungskontrollen zu umgehen.

### Systemanforderungen

Das Hauptzugriffsauthentifizierungssystem sollte:

- System- oder Anwendungsidentifikatoren nicht anzeigen, bis der Anmeldevorgang erfolgreich abgeschlossen wurde.
- Eine allgemeine Hinweiswarnung anzeigen, dass das System nur von autorisierten Benutzern abgerufen werden sollte.
- Während des Anmeldevorgangs keine Hilfemeldungen bereitstellen, die einem nicht autorisierten Benutzer nützen würden.
- Die Anmeldeinformationen erst nach Abschluss aller Eingabedaten validieren; wenn ein Fehlerzustand auftritt, sollte das System nicht angeben, welcher Teil der Daten korrekt oder falsch ist.
- Gegen Brute-Force-Anmeldeversuche schützen (Ratenbegrenzung, progressive Verzögerung, CAPTCHA oder Kontosperrung).
- Alle erfolgreichen und fehlgeschlagenen Authentifizierungsversuche protokollieren.
- Ein Sicherheitsereignis auslösen, wenn ein möglicher versuchter oder erfolgreicher Verstoss gegen Anmeldekontrollen erkannt wird.
- Ein eingegebenes Passwort nicht anzeigen (Eingabe maskieren).
- Passwörter nicht im Klartext über ein Netzwerk übertragen.
- Inaktive Sitzungen nach einem definierten Inaktivitätszeitraum beenden.
- Verbindungszeiten einschränken, um zusätzliche Sicherheit für Hochrisikoanwendungen bereitzustellen.

**Sitzungs-Timeout-Anforderungen**:

| Systemklassifizierung | Leerlauf-Timeout | Absoluter Timeout |
|-----------------------|------------------|-------------------|
| Vertrauliche / kritische Systeme | 15 Minuten | 8 Stunden |
| Systeme, die sensible Personendaten verarbeiten | 5 Minuten | 4 Stunden |
| Privilegierte Admin-Konsolen | 10 Minuten | 4 Stunden |
| Standardmässige Geschäftssysteme | 30 Minuten | 12 Stunden |

Absoluter Timeout erfordert eine erneute Authentifizierung unabhängig von der Aktivität.

### Gemeinsam genutzte Authentifizierungsinformationen

Gemeinsam genutzte Authentifizierungsinformationen werden abgeraten und sollten wo immer möglich vermieden werden. Wo gemeinsame Anmeldedaten erforderlich sind (Legacy-Systeme, vom Hersteller obligatorische Konten):

- ISB-Genehmigung ist obligatorisch mit dokumentierter Geschäftsbegründung.
- Anmeldedaten sollten im genehmigten Anmeldedaten-Vault [Password Manager] gespeichert werden, nicht in Klartextdokumenten, E-Mails oder Chat.
- Für jede gemeinsame Anmeldeinformation sollte ein benannter Verwalter zugewiesen werden.
- Checkout-Protokollierung mit Benutzeridentifikation und Zeitstempel sollte geführt werden.
- Sitzungsaufzeichnung wird für privilegierte gemeinsame Konten empfohlen, wo technisch möglich.
- Individuelle Rechenschaftspflicht sollte durch Prüfprotokollierung aufrechterhalten werden.
- Zugriff und Nutzung sollten vierteljährlich überprüft werden; jährliche Neuautorisierung erforderlich.
- Gemeinsame Konten sollten im Register privilegierter Konten und im Zugriffsüberprüfungsprozess enthalten sein.

---

## Passwort-Zurücksetzung und Wiederherstellung

### Self-Service-Passwort-Zurücksetzung

Wo Self-Service-Passwort-Zurücksetzung über [Identity Provider] implementiert ist:

- MFA-basierte Verifizierung (Authenticator-Push, FIDO2 oder Hardware-Token) sollte vor einer Passwort-Zurücksetzung verlangt werden.
- Wissensbasierte Sicherheitsfragen sollten nicht als einzige Verifizierungsmethode verwendet werden, da sie anfällig für Social Engineering sind.
- Zurücksetzungs-Tokens sollten zeitlich begrenzt sein (maximale 1-Stunden-Gültigkeit) und einmalig verwendet werden.
- Alle Zurücksetzungsaktivitäten sollten protokolliert werden, einschliesslich der verwendeten Verifizierungsmethode.
- Der Benutzer sollte über die Passwortänderung über einen registrierten sekundären Kontakt (E-Mail oder Mobiltelefon) benachrichtigt werden.
- Der Zurücksetzungsprozess sollte nicht offenbaren, ob ein Konto existiert (Kontoenumeration verhindern).

### Helpdeskunterstützte Passwort-Zurücksetzung

Helpdeskunterstützte Passwort-Zurücksetzungen sollten diesem Verfahren folgen:

1. **Identität verifizieren**: Der Helpdesk sollte die Identität des Anrufers mithilfe von mindestens einer vorregistrierten Verifizierungsmethode verifizieren (sekundäre E-Mail, registrierte Mobilnummer, Bestätigung durch Vorgesetzte oder persönlich mit Lichtbildausweis).
2. **Temporäres Passwort generieren**: Ein zufälliges temporäres Passwort sollte generiert werden, das die Mindestlängenanforderungen erfüllt.
3. **Sicher kommunizieren**: Das temporäre Passwort sollte über einen sicheren Kanal kommuniziert werden (nicht unverschlüsselte E-Mail); wo möglich, den sicheren Zurücksetzungslink des Identity Providers verwenden.
4. **Änderung erzwingen**: Das temporäre Passwort sollte bei erster Verwendung ablaufen und den Benutzer zur sofortigen Festlegung eines neuen Passworts zwingen.
5. **Dokumentieren**: Die Zurücksetzungsanfrage, die verwendete Verifizierungsmethode und der Zeitstempel sollten im IT-Service-Management-System erfasst werden.

Helpdesk-Personal sollte nach der Ausstellung keinen Zugriff auf die Anzeige von Benutzerpasswörtern haben.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|----------------------|
| **Geschäftsleitung** | Richtlinie genehmigen; Budget für Authentifizierungsinfrastruktur (MFA, Passwort-Manager, Identity Provider) bereitstellen; Sicherheitsmetriken vierteljährlich überprüfen |
| **ISB** | Richtlinieneigentümerschaft und Accountability; MFA-Strategie und Roadmap für phishing-resistente Authentifizierung genehmigen; Ausnahmen genehmigen (mittleres/hohes Risiko); vierteljährliche Compliance-Berichte überprüfen |
| **IT-Sicherheitsmanager** | Tägliche Verwaltung der Authentifizierungssicherheit; Authentifizierungsalarme und Anomalien überwachen; vierteljährliche MFA-Abdeckungsüberprüfungen durchführen; Ausnahmen mit geringem Risiko genehmigen |
| **IT-Betrieb / IAM-Team** | [Identity Provider] und Authentifizierungsinfrastruktur verwalten; Anmeldedatenausstellung und -zurücksetzungen verarbeiten; MFA-Registrierung pflegen; Passwortrichtlinieneinstellungen konfigurieren; Verletzungsprüfung integrieren |
| **Helpdesk** | Helpdeskunterstützte Passwort-Zurücksetzungen gemäss dokumentiertem Verfahren ausführen; Benutzeridentität vor Änderungen an Anmeldedaten verifizieren; verdächtige Zurücksetzungsanfragen an IT-Sicherheit eskalieren |
| **Systemeigentümer** | Sicherstellen, dass Systeme unter ihrer Eigentümerschaft die Authentifizierungsanforderungen erfüllen; MFA dort implementieren, wo vorgeschrieben; Lücken bei Authentifizierungskontrollen melden |
| **Alle Mitarbeitenden** | Authentifizierungsdaten schützen; MFA-Registrierung innerhalb des erforderlichen Zeitrahmens abschliessen; vermutete Kompromittierung von Anmeldedaten sofort melden; Konten oder Anmeldedaten nicht teilen; Passwortstandards einhalten |

---

## Nachweise

Die folgenden Nachweise belegen die Einhaltung dieser Richtlinie:

| Nr. | Nachweis | Eigentümer | Häufigkeit |
|-----|----------|------------|------------|
| 1 | **Passwortrichtlinien-Konfigurationsnachweis** ([Identity Provider]-Einstellungen: Mindestlänge, Verletzungsprüfung, Sperrung, Verlauf) | IT-Betrieb | Jährlich und bei Änderungen erfasst |
| 2 | **MFA-Registrierungsberichte** (Abdeckungsprozentsatz nach Benutzertyp: privilegiert, Standard, Fernzugriff) | IT-Sicherheit | Monatlich für privilegierte; vierteljährlich für alle Benutzer |
| 3 | **MFA-Methodenverteilung** (FIDO2, TOTP, Push, SMS — Migrationsfortschritt hin zu phishing-resistenten Methoden) | IT-Sicherheit | Vierteljährlich |
| 4 | **Verletzungsprüfungs-Konfigurationsnachweis** (Integration mit kompromittierter Anmeldedatendatenbank, Prüfhäufigkeit) | IT-Betrieb | Jährlich und bei Änderungen |
| 5 | **Standard-Anmeldedaten-Scan-Ergebnisse** (keine Standard- oder vom Hersteller bereitgestellten Anmeldedaten in der Produktion) | IT-Sicherheit | Vierteljährlich |
| 6 | **Authentifizierungsereignisprotokolle** (erfolgreiche/fehlgeschlagene Anmeldungen, Sperrungen, Anomalieuntersuchungen, Impossible-Travel-Warnungen) | IT-Sicherheit | 12 Monate aufbewahrt; Anomalien innerhalb von 24 Stunden untersucht |

**Beispiele für Authentifizierungsanomalien** (Indikatoren, die eine Untersuchung auslösen):

| Anomalietyp | Erkennungsmethode | Reaktion |
|-------------|-------------------|----------|
| **Impossible Travel** | Anmeldung von zwei geografisch weit entfernten Standorten innerhalb unmöglicher Reisezeit | Zweite Sitzung sperren; Benutzer benachrichtigen; untersuchen |
| **Brute Force** | > 10 fehlgeschlagene Anmeldeversuche innerhalb von 5 Minuten von einer einzigen Quelle | Quell-IP sperren; IT-Sicherheit benachrichtigen |
| **Credential Stuffing** | Mehrere Konten mit fehlgeschlagenen Anmeldungen aus demselben IP-Bereich angegriffen | IP-Bereich sperren; betroffene Konten überprüfen; IT-Sicherheit benachrichtigen |
| **MFA-Müdigkeit** | > 3 abgelehnte MFA-Push-Benachrichtigungen innerhalb von 10 Minuten | Konto sperren; Benutzer über sekundären Kanal kontaktieren, um zu verifizieren |
| **Ungewöhnliche Zeiten** | Anmeldung ausserhalb der normalen Arbeitszeiten für Nicht-Schichtarbeiter | Protokollieren und überprüfen; Alarm wenn in Kombination mit anderen Anomalien |
| **Neues Gerät/Standort** | Erstmalige Anmeldung von nicht erkanntem Gerät oder Standort | Stufenweise Authentifizierung (zusätzliche MFA-Herausforderung); Benutzer benachrichtigen |
| **Privilege Escalation** | Benutzer erhält erhöhte Berechtigungen ohne genehmigten Änderungsantrag | Sofortige Untersuchung; rückgängig machen wenn nicht autorisiert |
| 7 | **Passwort-Zurücksetzungsaufzeichnungen** (Self-Service und helpdeskunterstützt; Identitätsverifizierungsmethode dokumentiert) | IT-Betrieb | Pro Ereignis; halbjährlich auditiert |
| 8 | **Register gemeinsamer Anmeldedaten** (Konto, Verwalter, Vault-Standort, letzte Überprüfung, Neuautorisierungsdatum) | IT-Sicherheit | Vierteljährlich überprüft |
| 9 | **Ausnahmeregister** (Systeme ohne MFA, Legacy-Passworteinschränkungen, SMS-only-MFA — mit Ausgleichskontrollen und ISB-Genehmigung) | IT-Sicherheit | Vierteljährlich überprüft; jede Ausnahme max. 12 Monate |
| 10 | **Schulungsabschlussaufzeichnungen zur Authentifizierungssensibilisierung** | HR / IT-Sicherheit | Jährlich |

### Schulungsanforderungen für Authentifizierung

Alle Mitarbeitenden sollten wie folgt Sensibilisierungsschulungen zur Authentifizierung abschliessen:

| Schulungsmodul | Zielgruppe | Häufigkeit | Inhalt |
|----------------|------------|------------|--------|
| **Sicherheitsbewusstsein — Authentifizierungsgrundlagen** | Alle Mitarbeitenden | Jährlich (als Teil der obligatorischen Sicherheitssensibilisierung) | Passworthygiene, MFA-Registrierung, Phishing-Erkennung, Melden von Anmeldedaten |
| **Passwort-Manager-Einführung** | Alle Mitarbeitenden | Bei der Einarbeitung + bei Tooländerungen | [Password Manager]-Einrichtung, Vault-Erstellung, Browser-Erweiterung, Mobile App, Notfallzugang |
| **Schulung für privilegierten Zugriff** | Privilegierte Benutzer (Admins, DBAs, Sicherheitsteam) | Jährlich + bei Rollenzuweisung | PAM-Tool-Nutzung, Anmeldedaten-Vault-Checkout/-Checkin, Sitzungsaufzeichnungsbewusstsein, MFA-Hardware-Schlüsselverwaltung |
| **Phishing-Simulation** | Alle Mitarbeitenden | Vierteljährlich | Simulierte Phishing-Kampagnen zur Prüfung des Bewusstseins für Anmeldedatenerfassung; Ergebnisse an ISB gemeldet; gezielte Nachschulung für Personal, das versagt |
| **Service-Account-Verwaltung** | Systemeigentümer, DevOps, IT-Betrieb | Jährlich | Service-Account-Lebenszyklus, Anmeldedatenspeicherung (kein Hardcoding), Rotationsverfahren, Ausserdienststellung |

**Messung der Schulungseffektivität**: Phishing-Simulation-Klickrate vierteljährlich verfolgt (Ziel: < 5 %). Personal, das Phishing-Simulationen zweimal innerhalb von 12 Monaten nicht besteht, erhält obligatorisches 1:1-Sicherheitscoaching.

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheits-Management-Team sollte die Einhaltung dieser Richtlinie durch verschiedene Methoden verifizieren, einschliesslich, aber nicht beschränkt auf, Audits der Identity-Provider-Konfiguration, MFA-Abdeckungsberichte, Verletzungsprüfungsverifizierung, Authentifizierungsprotokollanalyse, Penetrationstests, interne und externe Audits sowie Feedback an den Richtlinieneigentümer.

**Wichtige Leistungsindikatoren**:

| Metrik | Ziel | Häufigkeit |
|--------|------|------------|
| MFA-Registrierung (alle Benutzer) | >= 95 % | Monatlich |
| MFA-Registrierung (privilegierte Benutzer) | 100 % | Monatlich |
| Passwortrichtlinien-Compliance | >= 98 % | Monatlich |
| Standard-Anmeldedatenfunde in der Produktion | 0 | Vierteljährlich |
| Verletzungsgeprüfte Passwortabdeckung | 100 % neuer Passwörter | Monatlich |
| Authentifizierungsanomalie-Untersuchung (innerhalb von 24 Stunden) | 100 % | Laufend |
| SMS-basierte MFA-Reduktion (Jahr für Jahr) | Abnehmender Trend | Jährlich |
| Passwort-Manager-Einführung (organisationsweit) | >= 80 % der Benutzer mit aktivem Vault | Vierteljährlich |
| Passwort-Manager einzigartiges Passwortverhältnis | >= 90 % einzigartige Passwörter über Vaults | Vierteljährlich |
| Service-Account-Anmeldedaten-Rotations-Compliance | 100 % innerhalb definierter Rotationsperiode | Vierteljährlich |

Metriken sollten dem ISB vierteljährlich gemeldet werden. Metriken, die unter dem Ziel liegen, sollten einen Abhilfeplan mit Eigentümer und Zieldatum enthalten.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie sollte vom Information Security Manager im Voraus genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum. Ausnahmen sollten dem Management-Review-Team gemeldet werden. Maximale Ausnahmedauer: 12 Monate, verlängerbar mit erneuter Genehmigung.

**Zulässige Ausnahmen** (mit Ausgleichskontrollen):

- Legacy-Systeme, die die Passwortlängenanforderungen nicht erfüllen können (Ausgleichskontrolle: Netzwerksegmentierung, erweiterte Überwachung, eingeschränkter Zugriff).
- Mit MFA inkompatible Systeme (Ausgleichskontrolle: IP-Beschränkung, erweiterte Protokollierung, reduzierter Sitzungs-Timeout, VPN-only-Zugriff).
- Service-Konten, die andere Authentifizierungsrichtlinien erfordern (Ausgleichskontrolle: Anmeldedaten-Vaulting, automatisierte Rotation, erweiterte Überwachung).

### Service-Account-Authentifizierung

Service-Konten (nicht-interaktive Konten für Anwendungs-zu-Anwendungs-Kommunikation, geplante Aufgaben und Automatisierung) sollten die folgenden Anforderungen erfüllen:

| Anforderung | Standard |
|-------------|----------|
| **Namenskonvention** | Präfix `svc-` gefolgt von Anwendungs-/Funktionsname (z. B. `svc-backup-agent`, `svc-crm-integration`) |
| **Passwortlänge** | Mindestens 24 Zeichen, zufällig generiert |
| **Anmeldedatenspeicherung** | Genehmigter Secrets-Vault [PAM / Password Manager] — nicht in Skripten, Konfigurationsdateien oder Quellcode |
| **Rotation** | Automatisierte Rotation alle 90 Tage, wo technisch möglich; manuelle Rotation alle 180 Tage mit dokumentierter Begründung |
| **Interaktive Anmeldung** | Verboten — Service-Konten sollten nicht für die interaktive Anmeldung verwendet werden. Technische Kontrollen (GPO/IdP-Richtlinie) sollten die interaktive Anmeldung wo unterstützt verhindern. |
| **Eigentümerschaft** | Benannter menschlicher Eigentümer (Systemeigentümer oder Anwendungsmanager) verantwortlich für das Lebenszyklusmanagement |
| **Überprüfung** | Vierteljährliche Überprüfung aller Service-Konten: noch erforderlich? Eigentümer noch gültig? Anmeldedaten rotiert? Berechtigungen noch angemessen? |
| **Ausserdienststellung** | Innerhalb von 5 Werktagen nach Anwendungsausserdienststellung deaktiviert; Anmeldedaten sofort rotiert |

**Service-Account-Inventar**: In [PAM / Asset-Management-System] mit: Kontoname, Zweck, Eigentümer, Erstellungsdatum, letztes Rotationsdatum, nächstes Rotationsdatum, zugehörige Anwendung, Berechtigungsumfang geführt.

- Systeme, bei denen SMS die einzige verfügbare MFA-Methode ist (Ausgleichskontrolle: IP-Beschränkung, Anomalieüberwachung, dokumentierter Migrationsplan).

**Nicht als Ausnahmen zulässig**:

- Eliminierung von MFA für privilegierten Zugriff.
- Erlaubnis zur Passwortfreigabe ohne Rechenschaftspflicht.
- Erlaubnis von Standard-Anmeldedaten in Produktionsumgebungen.
- Deaktivierung der Authentifizierungsprotokollierung.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstösst, kann disziplinarischen Massnahmen unterworfen werden, bis hin zur Kündigung des Arbeitsverhältnisses.

**Progressives Vorgehen** (innerhalb eines rollierenden 12-Monats-Zeitraums):

| Vorkommen | Reaktion | Zeitrahmen | Eigentümer |
|-----------|----------|------------|------------|
| Erstes Mal | Sensibilisierungserinnerung und gezielte Schulung | Innerhalb von 5 Werktagen | IT-Sicherheit |
| Zweites Mal (innerhalb von 90 Tagen) | Vorgesetzte benachrichtigen + dokumentierte Warnung | Innerhalb von 3 Werktagen | IT-Sicherheit + HR |
| Drittes Mal (innerhalb von 12 Monaten) | Zugriffsbeschränkung bis zur Abhilfe | Sofort | IT-Sicherheit + Vorgesetzte |
| Vorsätzliche / kritische Verletzung | Disziplinäre Massnahmen gemäss HR-Richtlinien | Sofortige Eskalation | HR + ISB |

**Kritische Verletzungen**, die unabhängig von der Vorgeschichte eine sofortige Eskalation rechtfertigen:

- Teilen von privilegierten Anmeldedaten.
- Absichtliches Umgehen von Authentifizierungskontrollen.
- Speichern von Anmeldedaten im Klartext an gemeinsam genutzten Orten.
- Verwenden von Standard- oder vom Hersteller bereitgestellten Anmeldedaten in der Produktion nach Benachrichtigung.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollten Änderungen an Authentifizierungsstandards (einschliesslich NIST SP 800-63B-Revisionen), neue Bedrohungen (Credential Stuffing, Phishing, MFA-Umgehungstechniken wie Adversary-in-the-Middle und MFA-Müdigkeit), Fortschritte bei der phishing-resistenten Authentifizierung (FIDO2/WebAuthn, Passkeys), regulatorische Änderungen und Erkenntnisse aus Vorfällen berücksichtigen.

---

# Bereiche des ISO-27001-Standards, die abgedeckt werden

Richtlinie zu Authentifizierungsinformationen — ISO-27001-Kontrollmapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Managementverantwortlichkeiten |
| Klausel 6.2 Informationssicherheitsziele | **5.17 Authentifizierungsinformationen** |
| Klausel 7.3 Bewusstsein | 5.15 Zugangskontrolle |
| Klausel 7.5.3 Kontrolle dokumentierter Informationen | 5.16 Identitätsverwaltung |
| | 5.18 Zugriffsrechte |
| | 5.36 Konformität mit Richtlinien, Regeln und Standards |
| | 6.3 Informationssicherheitsbewusstsein, Ausbildung und Schulung |
| | 6.4 Disziplinarischer Prozess |
| | 8.2 Privilegierte Zugriffsrechte |
| | 8.5 Sichere Authentifizierung |
| | 8.24 Einsatz von Kryptografie |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizer nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen einschliesslich Authentifizierungskontrollen zum Datenschutz |
| Schweizer DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (soweit anwendbar) | Art. 32 — Sicherheit der Verarbeitung (Authentifizierungskontrollen als angemessene technische Massnahme) |
| ISO/IEC 27001:2022 | Annex A Kontrolle 5.17 — Authentifizierungsinformationen |
| ISO/IEC 27002:2022 | Abschnitt 5.17 — Implementierungsleitfaden für Authentifizierungsinformationen |
| NIST SP 800-63B-4 | Digital Identity Guidelines — gespeicherte Geheimnisse, Multi-Faktor-Authentifizierung, Verifiziereranforderungen |
| CIS Controls v8 | Kontrolle 5 (Account Management), Kontrolle 6 (Access Control Management) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
