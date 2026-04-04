<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.14-DE:operational:OP-POL:a.5.14 -->
**ISMS-OP-POL-A.5.14 — Informationsübertragung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Informationsübertragung |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.5.14 |
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

- ISO/IEC 27001:2022 Control A.5.14 — Information transfer

**Verwandte Annex-A-Kontrollen**:

| Kontrolle | Bezug zur Informationsübertragung |
|-----------|-----------------------------------|
| A.5.10 Akzeptable Nutzung von Informationen | Regeln zur akzeptablen Nutzung gelten für alle Informationsübertragungen |
| A.5.12–13 Informationsklassifizierung und -kennzeichnung | Klassifizierung bestimmt Übertragungsmethode und Verschlüsselungsanforderungen |
| A.5.19–23 Lieferantenbeziehungen | Drittanbieter-Übertragungsvereinbarungen und Cloud-Dienst-Übertragungen |
| A.5.31 Gesetzliche, gesetzgebungsbedingte, regulatorische Anforderungen | Rechtliche Anforderungen bei grenzüberschreitenden Übertragungen (nDSG Art. 16–17) |
| A.5.34 Datenschutz und Schutz personenbezogener Daten | Anforderungen an die Übertragung personenbezogener Daten und DSFA-Auslöser |
| A.7.10 Speichermedien | Verwaltung von Wechseldatenträgern und sichere Entsorgung |
| A.8.10 Löschung von Informationen | Sichere Löschung übertragener Daten von temporärem Speicher und Medien |
| A.8.13 Informations-Backup | Sicherheit beim Transport von Backup-Medien und Offsite-Übertragung |
| A.8.24 Verwendung von Kryptographie | Verschlüsselungsstandards für Daten bei der Übertragung |

**Verwandte interne Richtlinien**:

- Richtlinie zur Informationsklassifizierung und -handhabung
- Kryptographie-Richtlinie
- Zugangskontroll-Richtlinie
- Datenschutz- und PII-Schutz-Richtlinie
- Asset-Management-Richtlinie
- Vorfallsmanagement-Richtlinie

---

# Informationsübertragungs-Richtlinie

## Zweck

Der Zweck dieser Richtlinie ist es, die korrekte Behandlung bei der Übertragung von Informationen intern und extern zu gewährleisten und den Schutz der Informationsübertragung über alle Arten von Kommunikationseinrichtungen zu sichern.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) und die Datenschutzverordnung (DSV), indem sie technische und organisatorische Massnahmen proportional zum Risiko zum Schutz personenbezogener Daten (einschliesslich sensibler Personendaten) bei der Übertragung umsetzt. Wo die Organisation Daten natürlicher Personen im EU/EWR-Raum verarbeitet, gelten auch DSGVO-Anforderungen.

## Geltungsbereich

Alle Mitarbeitenden und Drittnutzer.

Informationen, die Teil von Systemen und Anwendungen sind, die gemäss dem ISO 27001-Geltungsbereich in Scope sind.

## Grundsätze

Die Datenübertragung muss allen anwendbaren gesetzlichen und regulatorischen Anforderungen entsprechen, einschliesslich des schweizerischen nDSG (revDSG) und, wo anwendbar, der EU DSGVO.

Formelle Vereinbarungen mit Vertraulichkeits- und Geheimhaltungsklauseln müssen vor der Datenübertragung mit Dritten vorhanden sein.

Personenbezogene Daten dürfen nicht ohne gültige Rechtsgrundlage nach nDSG Art. 16–17 (Angemessenheitsbeschluss, Standardvertragsklauseln oder anwendbare Ausnahme) ausserhalb der Schweiz übertragen werden. Siehe den Abschnitt Grenzüberschreitende Übertragungen unten.

Keine persönlichen oder vertraulichen Informationen dürfen unverschlüsselt übertragen werden.

Alle Übertragungen müssen in Übereinstimmung mit der Richtlinie zur Informationsklassifizierung und -handhabung erfolgen.

---

## Virenprüfung von Informationen

Zu übertragende Informationen müssen vor dem Versand oder vor dem Öffnen beim Empfang auf Malware geprüft werden. Dies gilt für alle elektronischen Übertragungen einschliesslich E-Mail-Anhänge, Dateiübertragungen und Wechseldatenträger.

## Verschlüsselung von Informationen

Persönliche und vertrauliche Informationen müssen immer vor der Übertragung verschlüsselt werden, gemäss der Kryptographie-Richtlinie.

Verschlüsselungsdaten für Benutzername und Passwort müssen, wo verwendet, über zwei separate und unterschiedliche Kommunikationsmethoden geteilt werden. Die bevorzugte Methode ist es, den Zugriffslink oder Benutzernamen per E-Mail zu teilen und das Passwort oder die Passphrase per Telefonanruf oder sicherem Nachrichtenkanal.

## Übertragungsvereinbarungen

Mit allen Drittempfängern persönlicher oder vertraulicher Daten müssen formelle Übertragungsvereinbarungen abgeschlossen werden. Übertragungsvereinbarungen müssen folgendes adressieren:

- Die beteiligten Parteien und ihre Datenschutzrollen (Verantwortlicher, Auftragsverarbeiter).
- Kategorien der betroffenen Personen und zu übertragende personenbezogene Daten.
- Zweck und Rechtsgrundlage der Übertragung.
- Technische und organisatorische Sicherheitsmassnahmen (Verschlüsselung, Zugriffskontrollen, Protokollierung).
- Datenspeicherungs- und Löschverpflichtungen.
- Fristen für die Benachrichtigung bei Datenpannen.
- Prüfungsrechte.
- Unterauftragsverarbeiter-Kontrollen (wo anwendbar).

Übertragungsvereinbarungen müssen jährlich oder bei wesentlichen Änderungen der Übertragungsvereinbarung überprüft werden.

---

## Datenübertragungsmethoden

### Bevorzugte Übertragungsmethode

Die bevorzugte Übertragungsmethode für vertrauliche und personenbezogene Daten ist eine von der Organisation genehmigte sichere Dateifreigabeplattform (z. B. [verschlüsselter Cloud-Dienst], sicheres Portal oder verwaltete Dateiübertragungslösung).

Alle von der Organisation genehmigten Übertragungsmethoden müssen unterstützen:

- Verschlüsselung bei der Übertragung (mindestens TLS 1.2, TLS 1.3 bevorzugt).
- Zugriffskontrollen und Authentifizierung.
- Audit-Protokollierung von Übertragungen.

### Elektronische Dateiübertragung

Für automatisierte oder Massenübertragungen müssen folgende Protokolle verwendet werden:

| Protokoll | Status |
|-----------|--------|
| SFTP (SSH File Transfer Protocol) | Genehmigt — bevorzugt für automatisierte Übertragungen |
| HTTPS | Genehmigt — für webbasierte Datei-Uploads und API-Übertragungen |
| FTPS (FTP over TLS) | Genehmigt — wo SFTP nicht verfügbar ist |
| FTP (unverschlüsselt) | Verboten |
| SCP | Akzeptabel — SFTP wird jedoch bevorzugt |

### Datenübertragung per E-Mail

E-Mail ist nicht die bevorzugte Methode für die Übertragung persönlicher oder vertraulicher Informationen, da sie nicht von Natur aus sicher ist und keine Zustellung garantiert.

Es muss immer eine alternative sichere Methode zur Übertragung sensibler Daten in Betracht gezogen werden, wo immer dies möglich und praktikabel ist.

E-Mail-Kommunikation darf nicht für die Übertragung unverschlüsselter persönlicher oder vertraulicher Informationen verwendet werden.

Wo vertrauliche Daten per E-Mail gesendet werden müssen:

- Muss ein verschlüsselter Anhang mit einer Schlüssellänge verwendet werden, die den Anforderungen der Kryptographie-Richtlinie entspricht (mindestens AES-256).
- Das Passwort oder der Entschlüsselungsschlüssel muss über einen separaten Kommunikationskanal geteilt werden (Telefonanruf, sicherer Nachrichtenkanal).
- Dateiname oder Betreffzeile dürfen nicht den vollständigen Inhalt von Anhängen preisgeben oder sensible Personendaten offenbaren.

E-Mail-Nachrichten mit sensiblen Übertragungen müssen klare Anweisungen zu den Verantwortlichkeiten des Empfängers und Anweisungen dazu enthalten, was zu tun ist, wenn sie nicht der richtige Empfänger sind.

Die Verwendung persönlicher E-Mail-Konten für die Übertragung von Organisationsdaten ist verboten. Wo technisch machbar, muss die Organisation Kontrollen zur Verhinderung der Weiterleitung von Organisations-E-Mails an externe persönliche Konten implementieren (z. B. Mail-Flow-Regeln, DLP-Richtlinien, bedingter Zugriff).

Die Organisation muss E-Mail-Domain-Authentifizierung (SPF, DKIM, DMARC) implementieren, um sich gegen E-Mail-Spoofing und -Abfangen zu schützen. Die DMARC-Richtlinie muss für Produktionsdomains auf **quarantine** oder **reject** (nicht **none**) gesetzt werden.

### Datenübertragung per Post oder Kurier

Datenübertragungen über physische Medien wie Papierberichte, Speicherkarten oder externe Festplatten dürfen nur über einen von der Organisation genehmigten sicheren Kurier versandt werden (einen Kurierdienst, der eine verfolgte, unterschriebene Zustellung mit manipulationssicherer Verpackung und Nachweis der Übergabekette bietet, z. B. Schweizer Post Einschreiben, DHL Express mit Unterschrift oder gleichwertig). Standardpostdienstleistungen dürfen nicht für vertrauliche oder personenbezogene Daten verwendet werden.

Der Empfänger muss auf dem Paket klar angegeben und die physischen Medien müssen sicher verpackt sein, um Beschädigung oder Manipulation zu verhindern. Manipulationssichere Verpackung muss für vertrauliches Material verwendet werden.

Der Empfänger muss im Voraus informiert werden, dass die Informationen gesendet werden, damit er weiss, wann er sie erwartet. Der Empfänger muss den sicheren Empfang bestätigen, sobald die Informationen eintreffen. Der Absender ist dafür verantwortlich zu bestätigen, dass die Daten sicher angekommen sind.

### Datenübertragung auf Wechseldatenträgern

Nur von der Organisation eigene Wechseldatenträger dürfen für die Übertragung von Informationen verwendet werden, gemäss der Asset-Management-Richtlinie. Das Gerät muss genehmigt, im Asset-Register verzeichnet, einem Nutzer zugewiesen und verschlüsselt sein (AES-256 Vollplattenverschlüsselung oder Dateiebenen-Verschlüsselung). Die Verschlüsselung muss von IT verifiziert werden, bevor das Gerät für vertrauliche Datenübertragungen genehmigt wird.

Unverschlüsselte USB-Laufwerke, persönliche Speichergeräte und nicht genehmigte Cloud-Speicher dürfen nicht für Organisationsdatenübertragungen verwendet werden.

Der Wechseldatenträger muss nach Abschluss der Übertragung an den Eigentümer zurückgegeben und die übertragenen Daten nach der Verwendung sicher vom Speichergerät gelöscht werden. Das Asset-Register muss aktualisiert werden.

Klare Anweisungen zu den Verantwortlichkeiten des Empfängers und Anweisungen dazu, was zu tun ist, wenn er nicht der beabsichtigte Empfänger ist, müssen gegeben werden.

Keine Begleitnachricht oder kein Dateiname darf den Inhalt der Medien preisgeben.

Der für Datenübertragungen per Post oder Kurier beschriebene Prozess muss für den physischen Versand von Wechseldatenträgern befolgt werden.

### Telefone, Mobiltelefone und allgemeine Gespräche

Da Telefongespräche überwacht, abgehört oder abgefangen werden können (absichtlich oder versehentlich), ist folgende Vorsicht geboten:

- In der Umgebung bewusst sein, insbesondere in öffentlichen Verkehrsmitteln und an öffentlichen Orten, wenn persönliche, vertrauliche oder anderweitig sensible Informationen besprochen werden.
- Personenbezogene Daten dürfen nicht übertragen oder telefonisch besprochen werden, es sei denn, die Identität und Berechtigung des Empfängers wurde bestätigt.
- Bei der Verwendung von Voicemail dürfen keine sensiblen oder vertraulichen Nachrichten hinterlassen oder personenbezogene Daten eingeschlossen werden. Es ist lediglich ein Kontaktweg anzugeben und auf ein persönliches Gespräch mit dem Empfänger zu warten.
- Beim Abhören von Voicemail-Nachrichten muss sichergestellt werden, dass diese nicht in Grossraumbüros abgespielt werden, wo das Risiko besteht, dass andere zuhören. Diese müssen sofort nach dem Abhören gelöscht werden.

### Datenübertragung über Bluetooth

Bluetooth ist nicht als Kommunikationsmethode für unverschlüsselte vertrauliche, personenbezogene oder anderweitig sensible Daten genehmigt.

Wo Bluetooth für genehmigte Zwecke verwendet wird (z. B. Peripheriegeräte wie Tastaturen, Headsets):

- Gegenseitige Geräteauthentifizierung muss für alle Verbindungen durchgeführt werden.
- Verschlüsselung muss für alle Übertragungen aktiviert sein.
- Bluetooth-Sicherheitsmodus 4, Stufe 3 (authentifizierte Verschlüsselung) oder höher muss verwendet werden. Sicherheitsmodi 1 und 2 sind verboten.
- Geräte müssen auf nicht erkennbaren Modus gesetzt werden, wenn nicht aktiv gekoppelt wird.
- Die Kopplung muss in einem sicheren, nicht öffentlichen Bereich durchgeführt werden.
- Nutzer dürfen keine Übertragungen jeglicher Art von unbekannten oder verdächtigen Geräten annehmen.
- Bluetooth-Dateiübertragung (OBEX) muss deaktiviert sein, es sei denn, sie ist ausdrücklich genehmigt.
- Bluetooth-Profile müssen auf die für die genehmigte Funktion erforderlichen beschränkt werden.

---

## Grenzüberschreitende Datenübertragungen

Personenbezogene Daten dürfen nicht in ein Land ausserhalb der Schweiz übertragen werden, es sei denn, eine der folgenden Bedingungen ist erfüllt:

| Sicherungsmassnahme | Beschreibung |
|--------------------|-------------|
| Angemessenheitsbeschluss | Der Schweizerische Bundesrat hat festgestellt, dass das Zielland einen angemessenen Datenschutz bietet (Anhang 1, DSV). Dies umfasst alle EU/EWR-Staaten, das Vereinigte Königreich und andere aufgelistete Länder. |
| Swiss-US Data Privacy Framework | Für US-Empfänger, die unter dem DPF zertifiziert sind (wirksam ab September 2024). Der Zertifizierungsstatus muss vor jeder Übertragung verifiziert werden. |
| Standardvertragsklauseln | EU-SCC angepasst für das schweizerische nDSG mit dem schweizerischen EDÖB als Aufsichtsbehörde. Eine Transfer-Folgenabschätzung (TFA) muss abgeschlossen werden. |
| Verbindliche Unternehmensregeln | Vom schweizerischen EDÖB für gruppeninterne Übertragungen genehmigt. |
| Ausdrückliche Einwilligung | Die betroffene Person hat nach Information über die Risiken ausdrücklich und informiert in die spezifische Übertragung eingewilligt. |
| Vertragliche Notwendigkeit | Die Übertragung ist zur Erfüllung eines Vertrags mit der betroffenen Person erforderlich. |

Ein Register aller grenzüberschreitenden Datenübertragungen muss in der GRC-Plattform, dem Dokumentenmanagementsystem oder einem gleichwertigen zentralen Ort der Organisation gepflegt werden. Das Register muss den Empfänger, das Zielland, die Rechtsgrundlage, Sicherungsmassnahmen und das Überprüfungsdatum dokumentieren. Das Register muss jährlich vom ISB oder Datenschutzbeauftragten überprüft werden.

### Transfer-Folgenabschätzung (TFA)

Für Übertragungen in Länder ohne Angemessenheitsbeschluss (unter Berufung auf SCC oder andere Sicherungsmassnahmen) muss eine Transfer-Folgenabschätzung vor Beginn der Übertragung durchgeführt werden. Die TFA muss folgendes bewerten:

- **Rechtliches Umfeld**: Gesetze im Zielland, die den Datenschutz beeinflussen können (Staatlicher Zugriff, Überwachungsgesetze).
- **Praktische Umstände**: Ob der Empfänger widersprüchlichen Rechtsverpflichtungen oder staatlichen Datenzugriffsanfragen unterliegt.
- **Technische Massnahmen**: Verschlüsselung, Pseudonymisierung oder andere Sicherungsmassnahmen, die Daten für unbefugte Parteien unlesbar machen.
- **Vertragliche Massnahmen**: SCC, zusätzliche Vertragsklauseln, Prüfungsrechte, Rechtsbehelfe für betroffene Personen.
- **Restrisiko**: Ob ergänzende Massnahmen das Risiko auf akzeptable Niveaus reduzieren.

TFA-Ergebnisse müssen dokumentiert und vom ISB oder Datenschutzbeauftragten genehmigt werden, bevor die Übertragung autorisiert wird. TFAs müssen jährlich oder bei Änderung der Umstände überprüft werden (rechtliche Änderungen im Zielland, Sicherheitsvorfall).

---

## Verlorene oder fehlende Informationen

Wenn entdeckt wird oder der Verdacht besteht, dass Informationen verloren gegangen, fehlen, nicht angekommen sind oder an die falsche Person gelangt sind, muss der Mitarbeitende oder Drittnutzer sofort seinen Vorgesetzten und das Informationssicherheitsmanagement-Team informieren. Der Vorfallsmanagement-Prozess muss befolgt werden.

Verlorene oder fehlgeleitete Informationen müssen klassifiziert werden als:

- **Kritisch**: Umfasst sensible Personendaten, vertrauliche Geschäftsdaten oder schafft hohes Risiko für betroffene Personen (potenzielle Meldepflicht bei Datenpanne nach nDSG).
- **Hoch**: Umfasst Personendaten oder vertrauliche Informationen, jedoch begrenzte betroffene Personen oder Volumen.
- **Mittel**: Umfasst interne oder nicht vertrauliche Daten ohne Personendaten.

Die Person, die die Daten gesendet hat, ist für die Einleitung des Vorfallsberichts und die Mitwirkung bei der Untersuchung verantwortlich.

---

## Nachweise

Die folgenden Nachweise demonstrieren die Einhaltung dieser Richtlinie:

- **Übertragungsvereinbarungsregister** (Drittanbietervereinbarungen mit Überprüfungsdaten) — *jährlich überprüft; bei neuen Vereinbarungen aktualisiert*
- **Grenzüberschreitendes Übertragungsregister** (Ziele, Rechtsgrundlagen, Sicherungsmassnahmen) — *jährlich vom ISB/DSB überprüft; bei neuen Übertragungen aktualisiert*
- **Sichere Dateiübertragungsprotokolle** (SFTP, HTTPS, Cloud-Freigabeplattform) — *12 Monate aufbewahrt; vierteljährlich auf Anomalien überprüft*
- **E-Mail-Domain-Authentifizierungsunterlagen** (SPF, DKIM, DMARC-Konfiguration und Compliance-Berichte) — *DMARC-Berichte monatlich überprüft*
- **Wechseldatenträger-Inventar und -Zuweisungsunterlagen** — *bei Ereignissen aktualisiert; halbjährlich mit Asset-Register abgeglichen*
- **Kuriersendungs- und Empfangsbestätigungsprotokolle** — *12 Monate aufbewahrt*
- **Vorfallsberichte** im Zusammenhang mit verlorenen oder fehlgeleiteten Informationen — *gemäss Vorfallsmanagement-Richtlinie aufbewahrt*
- **Transfer-Folgenabschätzungen** (für Übertragungen in Länder ohne Angemessenheitsbeschluss) — *jährlich oder bei rechtlichen Änderungen im Zielland überprüft*
- **Datenübertragungsprotokoll** (elektronische Übertragungen vertraulicher oder personenbezogener Daten) — *12 Monate aufbewahrt; für Audit zugänglich*

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheitsmanagement-Team wird die Einhaltung dieser Richtlinie durch verschiedene Methoden überprüfen, einschliesslich, aber nicht beschränkt auf, Übertragungsprotokoll-Audits, Vereinbarungsüberprüfungen, Vorfallsberichte, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vom Informationssicherheitsmanager im Voraus genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum. Ausnahmen müssen dem Management-Review-Team gemeldet werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterliegen, bis hin zur Beendigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen müssen Änderungen der Datenübertragungsstandards, aufkommende Bedrohungen, regulatorische Änderungen (einschliesslich Aktualisierungen der schweizerischen Angemessenheitsliste) und Lessons Learned aus Vorfällen berücksichtigen.

---

# Bereiche des ISO 27001-Standards, die adressiert werden

Informationsübertragungs-Richtlinie — ISO 27001-Kontrollzuordnung

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Managementverantwortung |
| Klausel 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| Klausel 7.3 Bewusstsein | **5.14 Informationsübertragung** |
| Klausel 7.5.3 Steuerung dokumentierter Informationen | 6.3 Sensibilisierung, Schulung und Training zur Informationssicherheit |
| | 6.4 Disziplinarverfahren |
| | 7.10 Speichermedien |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen; Art. 16–17 — Grenzüberschreitende Übertragungen |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit; Anhang 1 — Angemessenheitsliste |
| EU DSGVO (soweit anwendbar) | Art. 32 — Sicherheit der Verarbeitung; Art. 44–49 — Internationale Übertragungen |
| ISO/IEC 27001:2022 | Annex A Kontrolle 5.14 — Informationsübertragung |
| ISO/IEC 27002:2022 | Abschnitt 5.14 — Umsetzungshinweise für Informationsübertragung |
| NIST SP 800-53 Rev 5 | SC-8 (Transmission Confidentiality and Integrity), MP-5 (Media Transport) |
| CIS Controls v8 | Kontrolle 3 (Data Protection — Safeguard 3.10: Encrypt Sensitive Data in Transit) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
