<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.24-DE:operational:OP-POL:a.8.24 -->
**ISMS-OP-POL-A.8.24 — Einsatz von Kryptographie**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Einsatz von Kryptographie |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.24 |
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

- ISO/IEC 27001:2022 Massnahme A.8.24 — Einsatz von Kryptographie

**Verwandte Annex-A-Massnahmen**:

| Massnahme | Bezug zur Kryptographie |
|-----------|------------------------|
| A.5.12–13 Klassifizierung und Kennzeichnung von Informationen | Bestimmt die Verschlüsselungsanforderungen je Klassifizierungsstufe |
| A.5.14 Informationsübertragung | Verschlüsselungsanforderungen für Daten in der Übertragung |
| A.5.23 Informationssicherheit für Cloud-Dienste | Verschlüsselung im Ruhezustand und bei der Übertragung für in der Cloud gehostete Daten |
| A.5.31 Gesetzliche, behördliche und vertragliche Anforderungen | Exportkontrollen, nDSG/DSGVO-Verschlüsselungspflichten |
| A.8.1 Benutzerendgeräte | Festplattenverschlüsselung, geräteseitige kryptographische Massnahmen |
| A.8.5 Sichere Authentifizierung | Kryptographischer Schutz von Authentifizierungsdaten |
| A.8.10 Löschung von Informationen | Kryptographische Löschung als sichere Löschmethode |
| A.8.13 Informationssicherung | Verschlüsselungsanforderungen für Backups |
| A.8.20 Netzwerksicherheit | TLS/IPsec zur Netzwerktransportverschlüsselung |
| A.8.28 Sicheres Coding | Einsatz genehmigter kryptographischer Bibliotheken in der Entwicklung |

**Verwandte interne Richtlinien**:

- Richtlinie zur Informationsklassifizierung und -handhabung
- Richtlinie zur Informationsübertragung
- Richtlinie zur Zugriffskontrolle
- Backup-Richtlinie
- Richtlinie zur sicheren Entwicklung

---

# Richtlinie zum Einsatz von Kryptographie

## Zweck

Zweck dieser Richtlinie ist es, den ordnungsgemässen und wirksamen Einsatz von Kryptographie zur Wahrung der Vertraulichkeit, Integrität und Authentizität von Informationen sicherzustellen.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) und die Datenschutzverordnung (DSV), indem technische und organisatorische Massnahmen entsprechend dem Risiko zum Schutz von Personendaten (einschliesslich besonders schützenswerter Personendaten) implementiert werden. Sofern die Organisation Daten von Personen im EU/EWR-Raum bearbeitet, gelten auch die DSGVO-Anforderungen. Verschlüsselung ist eine wichtige technische Massnahme zum Nachweis der Einhaltung von Datenschutzpflichten im Rahmen beider Regelwerke.

## Geltungsbereich

Vertrauliche und personenbezogene Informationen, die auf oder in organisationseigenen, verwalteten und kontrollierten Systemen und Anwendungen verarbeitet, gespeichert oder übertragen werden, die gemäss der ISO-27001-Scope-Erklärung im Geltungsbereich sind.

Alle Mitarbeitenden und Drittnutzer.

## Grundsatz

Informationen werden durch kryptographische Massnahmen auf der Grundlage der Klassifizierung gemäss der Richtlinie zur Informationsklassifizierung und -handhabung sowie auf der Grundlage der Risikobeurteilung geschützt.

Es darf ausschliesslich von der Organisation genehmigte Verschlüsselungstechnologie und -prozesse eingesetzt werden.

Der Export von Verschlüsselungstechnologien oder verschlüsselten Daten kann durch Vorschriften eingeschränkt sein, einschliesslich der schweizerischen Exportkontrollbestimmungen und dem Wassenaar-Arrangement. Personal soll bei Bedarf des Exports kryptographischer Technologien oder verschlüsselter Daten die Rechtsabteilung um Rat fragen.

Das kryptographische Schlüsselmanagement basiert auf branchenweit anerkannten Standards, darunter NIST SP 800-57 und die OWASP-Richtlinien zum Schlüsselmanagement. Kryptographische Schlüssel werden als Vertraulich klassifiziert.

---

## Kryptographische Massnahmen

### Genehmigte Algorithmen und Schlüssellängen

Die Organisation soll folgende Mindeststandards für Kryptographie einsetzen:

| Anwendungsfall | Algorithmus | Mindestanforderung |
|----------------|-------------|-------------------|
| Symmetrische Verschlüsselung | AES | 256-Bit |
| Asymmetrische Verschlüsselung | RSA | Mindestens 2048-Bit; 4096-Bit empfohlen |
| Asymmetrische Verschlüsselung | ECDSA/ECDH | Mindestens P-256; P-384 empfohlen |
| Hash-Funktionen | SHA-2-Familie | Mindestens SHA-256; SHA-384/SHA-512 für hochsicherheitsrelevante Anwendungen |
| Digitale Signaturen | RSA | Mindestens 2048-Bit; 4096-Bit empfohlen |
| Digitale Signaturen | ECDSA | Mindestens P-256 |
| Schlüsselableitung | PBKDF2, scrypt, Argon2 | Gemäss aktueller NIST-Empfehlung |

**Verbotene Algorithmen:** MD5, SHA-1, DES, 3DES, RC4, RSA unter 2048-Bit. Diese dürfen für keinen Zweck eingesetzt werden.

Die Organisation soll die Post-Quanten-Kryptographie-Standards des NIST (FIPS 203 ML-KEM, FIPS 204 ML-DSA, FIPS 205 SLH-DSA) beobachten und die Migration planen, sobald Einführungszeitpläne festgelegt sind. Eine Krypto-Agilität-Bewertung soll durchgeführt werden, um Systeme und Datenspeicher zu identifizieren, die eine PQC-Migrationsplanung erfordern, wobei langlebige Schlüssel und Daten mit Aufbewahrungsfristen von mehr als 10 Jahren priorisiert werden.

### Transport Layer Security

Alle Netzwerkkommunikationen, die vertrauliche oder personenbezogene Daten übertragen, sollen verschlüsselten Transport einsetzen:

- TLS 1.2 ist die akzeptable Mindestversion.
- TLS 1.3 ist bevorzugt und soll eingesetzt werden, wo unterstützt.
- TLS 1.0 und TLS 1.1 sollen auf allen Systemen deaktiviert werden.
- SSL (alle Versionen) soll auf allen Systemen deaktiviert werden.
- Es sollen nur Cipher Suites mit AEAD (z. B. AES-GCM) aktiviert werden, soweit machbar.

### Verschlüsselung mobiler Geräte, Laptops und Wechselmedien

Mobile Geräte, Laptops und Wechselmedien sollen eine Festplattenverschlüsselung auf Hardware- oder Betriebssystemebene aktiviert haben.

- Geräteverschlüsselung soll nicht deaktiviert werden.
- Der Zugriff auf verschlüsselten Speicher soll durch ein Passwort, eine Passphrase, eine PIN oder biometrische Authentifizierung geschützt sein.
- Nur organisationseigene und verwaltete Wechselmedien dürfen zur Speicherung vertraulicher Daten verwendet werden.

### E-Mail-Verschlüsselung

E-Mail soll nicht zur Übertragung vertraulicher oder personenbezogener Daten in unverschlüsseltem Format verwendet werden, in Übereinstimmung mit der Richtlinie zur Informationsübertragung.

Wenn vertrauliche Daten per E-Mail gesendet werden müssen, soll ein verschlüsselter Anhang mit einer Schlüssellänge verwendet werden, die den oben genannten genehmigten Algorithmusanforderungen entspricht.

Die Organisation soll eine für ihre Anforderungen geeignete E-Mail-Verschlüsselungslösung evaluieren und genehmigen. Bis eine Lösung eingesetzt wird, sollen verschlüsselte Dateianhänge mit Out-of-Band-Schlüsselaustausch als Interimsmassnahme verwendet werden.

### Verschlüsselung von Web- und Cloud-Diensten

Web- und Cloud-Dienste, die vertrauliche oder personenbezogene Daten verarbeiten, speichern oder übertragen, sollen mindestens TLS 1.2 einsetzen, um Daten bei der Übertragung zu schützen.

Alle Server sollen ein gültiges Zertifikat besitzen, das von einer anerkannten Zertifizierungsstelle ausgestellt wurde. Systemeigentümer sind für die Zertifikatserneuerung und die Sicherstellung verantwortlich, dass Systeme vor Ablauf aktualisiert werden.

### Drahtlosverschlüsselung

- WEP soll nicht eingesetzt werden.
- WPA3 ist für alle Drahtlosnetzwerke bevorzugt.
- WPA2 Enterprise-Modus mit 802.1X-Authentifizierung und AES-Verschlüsselung ist der akzeptable Mindeststandard.
- WPA2 Personal-Modus kann für Nicht-Produktionsnetzwerke mit einer mindestens 16 Zeichen langen zufälligen Passphrase und AES-Verschlüsselung eingesetzt werden.

### Backup-Verschlüsselung

Backups mit vertraulichen oder personenbezogenen Daten sollen mit von der Organisation genehmigter Verschlüsselungstechnologie verschlüsselt werden, die den oben genannten Mindestanforderungen an Algorithmen entspricht.

Die Backup-Verschlüsselung soll sich nicht ausschliesslich auf herstellerspezifische Mechanismen ohne dokumentierte Zusicherung des verwendeten Verschlüsselungsstandards stützen.

### Datenbankverschlüsselung

Datenbanken mit vertraulichen Informationen oder Personendaten sollen im Ruhezustand entweder auf der Datenbankapplikationsebene oder auf der Festplatten-/Volume-Ebene verschlüsselt werden.

Wenn eine Festplatten- oder Volume-Verschlüsselung eingesetzt wird, kann kryptographische Löschung (Vernichtung des Verschlüsselungsschlüssels) als gültige sichere Löschmethode verwendet werden, sofern das Risiko bewertet, der Ansatz dokumentiert und genehmigt wurde.

### Verschlüsselung von Daten in Bewegung

Die Übertragung vertraulicher und personenbezogener Informationen soll über verschlüsselte Kanäle erfolgen. Verschlüsselung ist erforderlich für:

- Transport sensibler Dateien (SFTP, SCP oder gleichwertige verschlüsselte Übertragung).
- Den gesamten Netzwerkverkehr für den Fernzugriff (VPN oder gleichwertig).
- Datenbankabfragen oder Webdienstaufrufe, die sensible Daten übertragen.
- Privilegierten Zugriff auf Netzwerk- oder Servergeräte (SSH; Telnet ist verboten).

### Bluetooth

Bluetooth soll nicht als Kommunikationsmethode für unverschlüsselte vertrauliche, personenbezogene oder anderweitig sensible Daten verwendet werden. Siehe Richtlinie zur Informationsübertragung.

---

## Kryptographisches Schlüsselmanagement

### Schlüsselgenerierung

Kryptographische Schlüssel sollen innerhalb kryptographischer Module generiert werden, die mindestens FIPS 140-2 oder FIPS 140-3 entsprechen oder eine gleichwertige validierte Zusicherung bieten.

Alle für die Schlüsselgenerierung benötigten Zufallswerte sollen innerhalb des kryptographischen Moduls mit einem validierten Zufallsbit-Generator erzeugt werden.

Hardware-Kryptomodule (HSMs) sind für den Schutz hochwertiger Schlüssel gegenüber Software-Modulen bevorzugt.

### Schlüsselverteilung

Schlüssel sollen über sichere Kanäle übertragen werden. Schlüsselmaterial soll nicht im Klartext über ein Netzwerk übertragen werden.

### Schlüsselspeicherung

- Schlüssel sollen niemals im Klartextformat gespeichert werden.
- Schlüssel sollen in einem kryptographischen Tresor, einem HSM oder einem Cloud-Schlüsselverwaltungsdienst (KMS) gespeichert werden.
- Schlüssel sollen nicht im Quellcode hart kodiert, in Konfigurationsdateien im Klartext gespeichert oder per E-Mail oder Messaging geteilt werden. Dies gilt auch für API-Schlüssel, Tokens, Dienst-Anmeldedaten und andere Geheimnisse — diese sollen über eine dedizierte Secrets-Management-Lösung verwaltet werden (z. B. AWS KMS, Azure Key Vault, HashiCorp Vault oder gleichwertig). Geheimnisse erfordern nicht die gleichen Verschlüsselungs-im-Ruhezustand-Standards wie Datenverschlüsselungsschlüssel, dürfen jedoch niemals im Klartext gespeichert werden und sollen gemäss den oben genannten Schlüsselrotationszeiträumen rotiert werden.
- Schlüsselverschlüsselungsschlüssel (KEKs), die zur Umhüllung gespeicherter Schlüssel verwendet werden, sollen mindestens so stark sein wie die Schlüssel, die sie schützen.
- Auf Schlüssel sollen Integritätsschutzverfahren angewendet werden, während sie gespeichert sind.

### Schlüsselzugriffskontrolle

Der Zugriff auf kryptographische Schlüssel soll dem Prinzip der minimalen Rechtevergabe folgen.

- Administrativer und operativer Zugriff auf Schlüssel soll nach Möglichkeit getrennt werden.
- Multi-Faktor-Authentifizierung soll für Schlüsselverwalter erforderlich sein.
- Ein Register der Personen mit Zugriff auf Schlüsselmaterial soll geführt werden.

### Schlüsselrotation

Schlüsselrotationszeiträume sollen basierend auf Schlüsseltyp, Risiko und regulatorischen Anforderungen definiert werden.

Schlüssel sollen bei vermutetem oder bestätigtem Kompromiss sofort rotiert werden, unabhängig von geplanten Rotationsterminen.

**Minimale Schlüsselrotationszeiträume:**

| Schlüsseltyp | Maximale Lebensdauer |
|--------------|---------------------|
| TLS/SSL-Zertifikate | 398 Tage (gemäss CA/Browser Forum Baseline) |
| Symmetrische Datenverschlüsselungsschlüssel (AES) | 2 Jahre (oder gemäss NIST SP 800-57 Kryptoperiodengrenzwerten) |
| Asymmetrische Schlüsselpaare (RSA/ECDSA) | 3 Jahre |
| API-Schlüssel und Dienst-Tokens | 90 Tage (verlängerbar auf 1 Jahr mit dokumentierter Risikoakzeptanz) |
| Datenbankverschlüsselungsschlüssel | 1 Jahr |

Kürzere Rotationszeiträume können je nach Risikobeurteilung oder regulatorischen Anforderungen erforderlich sein.

### Schlüsselhinterlegung und -sicherung

Schlüsselmaterial soll gesichert werden, um die Wiederherstellung verschlüsselter Daten zu ermöglichen.

- Backup-Schlüsselspeicherung soll mit mindestens dem gleichen Sicherungsniveau wie die Betriebsschlüssel verschlüsselt werden.
- Signierschlüssel sollen nicht hinterlegt werden.
- Verschlüsselungsschlüssel können hinterlegt werden, wenn geschäftliche Anforderungen dies rechtfertigen.

### Schlüsselkompromiss und -wiederherstellung

Ein Schlüsselkompromiss-Wiederherstellungsplan soll dokumentiert, jährlich getestet und als referenziertes Verfahren gepflegt werden. Der Plan soll enthalten:

- Kontaktdaten der zu benachrichtigenden Personen und der für Wiederherstellungsmassnahmen Verantwortlichen.
- Die Methode und das Verfahren zur Neuverschlüsselung.
- Ein Inventar aller kryptographischen Schlüssel und ihrer Verwendung.
- Identifikation aller Daten oder anderer Schlüssel, die durch den kompromittierten Schlüssel geschützt sind.
- Überwachung der Neuverschlüsselungsvorgänge zur Bestätigung des Abschlusses.

### Trust Stores

Trust Stores sollen gegen das Einschleusen nicht autorisierter Root-Zertifikate geschützt werden. Zugangskontrollen sollen pro Entität und Anwendung verwaltet und durchgesetzt werden.

Ein sicheres Verfahren zur Aktualisierung des Trust Store soll implementiert werden.

### Kryptographische Bibliotheken

Es sollen ausschliesslich seriöse kryptographische Bibliotheken verwendet werden, die aktiv gepflegt, regelmässig aktualisiert und von Drittorganisationen validiert sind (z. B. NIST/FIPS, Common Criteria).

Individuelle kryptographische Implementierungen sollen nicht entwickelt werden, es sei denn, sie wurden vom ISB mit dokumentierter Begründung ausdrücklich genehmigt.

---

## Optional: Massnahmen für Zahlungskartendaten (PCI DSS)

*Nur anwendbar, wenn Zahlungskartendaten verarbeitet werden und PCI-Geltungsbereich besteht.*

Wenn PCI-Geltungsbereich besteht, gelten die folgenden zusätzlichen Anforderungen:

- Geheime und private Schlüssel zur Ver-/Entschlüsselung von Karteninhaberdaten sollen mit einem Schlüsselverschlüsselungsschlüssel gespeichert werden, der mindestens so stark ist wie der Datenverschlüsselungsschlüssel, separat vom Datenverschlüsselungsschlüssel gespeichert oder innerhalb eines PTS-genehmigten Geräts oder HSM aufbewahrt werden.
- Die Verschlüsselung der Karteninhaberdaten-Umgebung soll zusätzlich zu dieser Richtlinie die PCI-DSS-Anforderungen erfüllen.

---

## Nachweise

Die folgenden Nachweise belegen die Konformität mit dieser Richtlinie:

- **Kryptographie-Inventar** (verwendete Algorithmen, Schlüssellängen, Protokolle über alle Systeme) — *vierteljährlich von IT-Sicherheit gepflegt*
- **Ergebnisse der TLS-Konfigurationsscans** (z. B. SSL Labs, testssl.sh) — *monatliche automatische Scans*
- **Zertifikatsinventar und Ablaufüberwachungsunterlagen** — *automatische Überwachung, monatlich überprüft*
- **KMS-Zugriffsprotokolle und Schlüsselnutzungs-Audit-Trails** — *12 Monate aufbewahrt, vierteljährlich überprüft*
- **Schlüsselrotationsunterlagen** — *im KMS protokolliert, halbjährlich auditiert*
- **Verschlüsselungskonfigurationsdokumentation** für Datenbanken, Backups, Endgeräte — *jährlich überprüft*
- **Schlüsselkompromiss-Wiederherstellungsplan** (dokumentiert und jährlich getestet)

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheits-Management-Team überprüft die Einhaltung dieser Richtlinie durch verschiedene Methoden, einschliesslich, aber nicht beschränkt auf technische Konfigurationsaudits, TLS-/Zertifikatsscans, interne und externe Audits sowie Feedback an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll vorab durch den Information Security Manager genehmigt und mit dokumentierter Risikoakzeptanz, kompensierenden Massnahmen und einem definierten Prüfdatum erfasst werden. Ausnahmen sollen dem Management-Review-Team gemeldet werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstösst, kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Änderungen der kryptographischen Standards, neue Bedrohungen (einschliesslich Entwicklungen im Bereich Post-Quanten-Kryptographie), regulatorische Änderungen und Erkenntnisse aus Incidents berücksichtigen.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Richtlinie zum Einsatz von Kryptographie — Zuordnung zu ISO-27001-Massnahmen

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Abschnitt 5.1 Führung und Verpflichtung | 5.1 Leitlinien für Informationssicherheit |
| Abschnitt 5.2 Richtlinie | 5.4 Managementverantwortung |
| Abschnitt 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Normen |
| Abschnitt 7.3 Bewusstsein | 6.3 Bewusstsein, Schulung und Training zur Informationssicherheit |
| | 6.4 Disziplinarverfahren |
| | 8.1 Benutzerendgeräte |
| | **8.24 Einsatz von Kryptographie** |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmenwerk | Relevanz |
|------------|---------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen zum Datenschutz |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (sofern anwendbar) | Art. 32 — Sicherheit der Verarbeitung (Verschlüsselung als geeignete Massnahme) |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.24 — Einsatz von Kryptographie |
| ISO/IEC 27002:2022 | Abschnitt 8.24 — Implementierungsleitfaden für kryptographische Massnahmen |
| NIST SP 800-57 | Empfehlungen zum Schlüsselmanagement |

---

<!-- QA_VERIFIED: 2026-03-29 -->
