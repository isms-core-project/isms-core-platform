<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.12-13-DE:operational:OP-POL:a.5.12-13 -->
**ISMS-OP-POL-A.5.12-13 — Informationsklassifizierung und -handhabung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Informationsklassifizierung und -handhabung |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.5.12-13 |
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

- ISO/IEC 27001:2022 Controls A.5.12, A.5.13 — Classification of information, labelling of information

**Verwandte Annex-A-Kontrollen**:

| Kontrolle | Bezug zur Informationsklassifizierung |
|-----------|---------------------------------------|
| A.5.9 Inventar von Informationen und anderen Assets | Klassifizierung wird inventarisierten Informations-Assets zugewiesen |
| A.5.10 Akzeptable Nutzung von Informationen | Regeln zur akzeptablen Nutzung setzen Handhabungsanforderungen je Klassifizierung durch |
| A.5.14 Informationsübertragung | Übertragungsmethode durch Klassifizierungsstufe bestimmt |
| A.5.15–18 Zugangskontrolle und Identitätsverwaltung | Zugriffsrechte basierend auf Klassifizierung und Need-to-Know gewährt |
| A.5.33 Schutz von Aufzeichnungen | Aufbewahrung und Schutz von Aufzeichnungen an Klassifizierung ausgerichtet |
| A.5.34 Datenschutz und Schutz personenbezogener Daten | Klassifizierungs- und Handhabungsanforderungen für personenbezogene Daten |
| A.7.10 Speichermedien | Medienhandhabung und -entsorgung je Klassifizierung |
| A.7.14 Sichere Entsorgung oder Wiederverwendung von Geräten | Entsorgungsstandards durch Klassifizierung bestimmt |
| A.8.10 Löschung von Informationen | Sichere Löschstandards je Klassifizierungsstufe |
| A.8.11 Datenmaskierung | Maskierung klassifizierter Daten in Nicht-Produktionsumgebungen |
| A.8.12 Data-Leakage-Prevention | DLP-Kontrollen setzen Handhabungsregeln der Klassifizierung durch |
| A.8.24 Verwendung von Kryptographie | Verschlüsselungsanforderungen durch Klassifizierung bestimmt |

**Verwandte interne Richtlinien**:

- Asset-Management-Richtlinie
- Zugangskontroll-Richtlinie
- Informationsübertragungs-Richtlinie
- Kryptographie-Richtlinie
- Datenschutz- und PII-Schutz-Richtlinie
- Richtlinie zur akzeptablen Nutzung

---

# Richtlinie zur Informationsklassifizierung und -handhabung

## Zweck

Der Zweck dieser Richtlinie ist es, die korrekte Klassifizierung und Handhabung von Informationen basierend auf ihrer Sensitivität, ihrem Wert und den rechtlichen Anforderungen zu gewährleisten, damit Informationen über ihren gesamten Lebenszyklus hinweg ein angemessenes Schutzniveau erhalten.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) und die Datenschutzverordnung (DSV), indem sie technische und organisatorische Massnahmen proportional zum Risiko zum Schutz personenbezogener Daten (einschliesslich sensibler Personendaten) durch klassifizierungsbasierte Kontrollen umsetzt. Wo die Organisation Daten natürlicher Personen im EU/EWR-Raum verarbeitet, gelten auch DSGVO-Anforderungen.

## Geltungsbereich

Alle Mitarbeitenden und Drittnutzer.

Alle Informationen in jeglichem Format (digital, physisch, mündlich), die Teil von Systemen und Anwendungen sind, die gemäss dem ISO 27001-Geltungsbereich in Scope sind.

## Grundsatz

Informationen müssen im Hinblick auf rechtliche Anforderungen, Wert, Kritikalität und Sensitivität gegenüber unbefugter Offenlegung oder Veränderung klassifiziert werden. Die Klassifizierung bestimmt die Handhabungskontrollen, die während des gesamten Informationslebenszyklus angewendet werden — von der Erstellung über Speicherung und Übertragung bis zur Vernichtung.

---

## Klassifizierungsschema

Informationen müssen in eine von drei Stufen klassifiziert werden:

| Stufe | Beschreibung | Auswirkung unbefugter Offenlegung |
|-------|-------------|-----------------------------------|
| **VERTRAULICH** | Informationen, deren Offenlegung der Organisation, ihren Kunden oder betroffenen Personen erheblichen Schaden verursachen würde. Umfasst gesetzlich geschützte Daten. | Schwerer finanzieller Verlust, regulatorische Strafen, Rechtsklage, erheblicher Reputationsschaden, hohes Risiko für betroffene Personen |
| **INTERN** | Informationen für den internen Gebrauch innerhalb der Organisation. Nicht zur öffentlichen Bekanntgabe bestimmt. | Geringfügige betriebliche Unannehmlichkeiten, geringfügige Beeinträchtigung, begrenzte Reputationsauswirkungen |
| **ÖFFENTLICH** | Für die Veröffentlichung genehmigte Informationen. Offenlegung verursacht keinen Schaden. | Keine nachteiligen Auswirkungen |

**Standard-Klassifizierung**: Informationen, die nicht explizit klassifiziert wurden, müssen bis zur Klassifizierung durch ihren Eigentümer als **INTERN** behandelt werden.

### Klassifizierung nach Informationstyp

| Informationstyp | Mindestklassifizierung |
|-----------------|----------------------|
| **Sensible Personendaten** (nDSG Art. 5: Gesundheit, rassische/ethnische Herkunft, religiöse/politische Überzeugungen, Strafregistereinträge, genetische Daten, biometrische Daten) | **VERTRAULICH** |
| **Personenbezogene Daten** (Namen, E-Mail-Adressen, Telefonnummern, Mitarbeiterdaten) | **INTERN** (mindestens); **VERTRAULICH** bei >1.000 Datensätzen oder Kombination mit sensiblen Kategorien |
| **Finanzdaten** (Konten, Transaktionen, Gehaltsinformationen, Bankverbindungen) | **VERTRAULICH** |
| **Geschäftsgeheimnisse und geistiges Eigentum** (proprietäre Methoden, Quellcode, Designs, Formeln) | **VERTRAULICH** |
| **Passwörter, kryptographische Schlüssel, Zugangsdaten** | **VERTRAULICH** |
| **Verträge und Rechtsvereinbarungen** | **VERTRAULICH** |
| **Interne Richtlinien, Verfahren, Sitzungsprotokolle** | **INTERN** |
| **Organigramme, interne Kommunikation** | **INTERN** |
| **Marketingmaterialien, Pressemitteilungen, veröffentlichte Inhalte** | **ÖFFENTLICH** |
| **Bereits öffentlich zugängliche Informationen** | **ÖFFENTLICH** |

### Klassifizierungsverantwortlichkeiten

- **Informationseigentümer** (gemäss der Asset-Management-Richtlinie definiert) sind für die Klassifizierung ihrer Informations-Assets verantwortlich.
- Die Klassifizierung muss bei der Erstellung oder beim Empfang von Informationen zugewiesen werden.
- Die Klassifizierung muss überprüft werden, wenn Informationen wesentlich geändert, mit neuen Parteien geteilt oder sich Geschäftsumstände ändern.
- Überklassifizierung muss vermieden werden — alles als VERTRAULICH zu klassifizieren verwässert die Bedeutung und verschwendet Ressourcen.
- **Aggregationsrisiko**: Informationen, die einzeln als INTERN klassifiziert sind, können eine Umklassifizierung zu VERTRAULICH erfordern, wenn sie mit anderen Datensätzen kombiniert werden und die Aggregation ein wesentlich höheres Schadensrisiko schafft (z. B. Kombination von Namen mit Gesundheitszustand oder Kombination individueller Gehaltseinträge zu einem abteilungsweiten Vergütungsbericht). Informationseigentümer müssen bei der Klassifizierung von Datensätzen das Aggregationsrisiko berücksichtigen.

---

## Informationskennzeichnung

### Kennzeichnungsanforderungen

Alle Informationen müssen entsprechend ihrer Klassifizierungsstufe gekennzeichnet werden:

| Format | Kennzeichnungsmethode |
|--------|----------------------|
| **Digitale Dokumente** (Word, PDF, Excel) | Klassifizierung in der Kopf- oder Fusszeile des Dokuments auf jeder Seite (z. B. "VERTRAULICH") |
| **E-Mail** | Klassifizierungspräfix in der Betreffzeile (z. B. "[VERTRAULICH] Betreff") |
| **Physische Dokumente** | Klassifizierung auf der Deckseite; Kopf- oder Fusszeile auf nachfolgenden Seiten |
| **Physische Medien** (USB-Laufwerke, Backup-Bänder) | Physisches Etikett am Gerät oder Behälter befestigt |
| **Datei-Metadaten** | Klassifizierung in Dateieigenschaften oder Dokumentenmanagementsystem-Metadaten aufgezeichnet |
| **Datenbankeinträge** | Klassifizierungsspalte oder Metadaten-Tag pro Datensatz |

**ÖFFENTLICHE** Informationen erfordern kein Klassifizierungsetikett, es sei denn, sie werden auf internen Plattformen veröffentlicht, wo ihr öffentlicher Status unklar sein könnte.

**Nicht gekennzeichnete Informationen** müssen standardmässig als **INTERN** behandelt werden.

Wo die Organisation Microsoft 365 oder gleichwertige Plattformen einsetzt, sollten Sensitivitätsetiketten konfiguriert werden, um die Klassifizierungsdurchsetzung zu automatisieren, einschliesslich Verschlüsselung, Zugangsbeschränkungen und visueller Markierungen.

---

## Informationshandhabung

### Handhabungsmatrix

| Handhabungsaspekt | ÖFFENTLICH | INTERN | VERTRAULICH |
|-------------------|-----------|--------|-------------|
| **Digitale Speicherung** | Keine Einschränkungen | Nur von der Organisation verwaltete Systeme; nicht auf persönlichen Geräten ohne MDM | Verschlüsselt im Ruhezustand (AES-256); zugangskontrollierte Ordner; kein Wechseldatenträger ohne Verschlüsselung |
| **Physische Speicherung** | Keine Einschränkungen | Büroräumlichkeiten; Standardablage | Abgeschlossene Schränke oder Räume mit eingeschränktem Zugang; Clean Desk durchgesetzt |
| **E-Mail-Übertragung** | Keine Einschränkungen | Interne E-Mail oder verschlüsselt extern | Verschlüsselte E-Mail obligatorisch; Passwort/Entschlüsselungsschlüssel über separaten Kanal |
| **Dateiübertragung** | Keine Einschränkungen | Nur genehmigte Dateifreigabeplattformen | Nur verschlüsselte Übertragung (SFTP, HTTPS); keine nicht genehmigten Cloud-Dienste |
| **Physische Übertragung** | Keine Einschränkungen | Versiegelter Umschlag; Hauspost | Manipulationssichere Verpackung; genehmigter Kurier mit Sendungsverfolgung; Empfangsbestätigung |
| **Weitergabe — intern** | Uneingeschränkt | Innerhalb der Organisation | Need-to-Know-Basis mit dokumentierter Genehmigung des Informationseigentümers |
| **Weitergabe — extern** | Uneingeschränkt | NDA erforderlich; genehmigte Kanäle | NDA + spezifische Genehmigung des Informationseigentümers; Übertragungsvereinbarung wo erforderlich |
| **Drucken** | Keine Einschränkungen | Sofort abholen; keine vergessenen Ausdrucke | Sicherer Druckauftrag (Badge/PIN); sofort abholen |
| **Cloud-Speicherung** | Genehmigte Dienste | Genehmigte Dienste; Daten in der Schweiz oder angemessenem Land | Genehmigte Dienste; Daten vorzugsweise in der Schweiz; Verschlüsselung mit von der Organisation verwalteten Schlüsseln |
| **Mobilgeräte** | Keine Einschränkungen | Nur von der Organisation MDM-registrierte Geräte | MDM-registriert; Geräteverschlüsselung; Remote-Wipe-Fähigkeit |
| **Backup** | Standard-Backup | Verschlüsseltes Backup | Verschlüsseltes Backup; eingeschränkter Wiederherstellungszugriff |

### Informationsspeicherung

Organisationsinformationen dürfen nicht auf persönlichen Geräten, persönlichen E-Mail-Konten oder persönlichem Cloud-Speicher gespeichert werden, es sei denn, dies wurde vom ISB genehmigt und in einem genehmigten Register aufgezeichnet.

Organisationsinformationen müssen durch Zugriffskontrollen gemäss der Zugangskontroll-Richtlinie geschützt werden.

Vertrauliche Informationen müssen im Ruhezustand und bei der Übertragung über jedes System verschlüsselt werden, in Übereinstimmung mit der Kryptographie-Richtlinie.

Vertrauliche und interne Informationen dürfen nicht in Entwicklungs- oder Testumgebungen gespeichert oder verarbeitet werden, es sei denn, die Daten wurden maskiert, anonymisiert oder pseudonymisiert. Wo Produktionsdaten in Nicht-Produktionsumgebungen verwendet werden müssen, ist die Genehmigung des Informationseigentümers und des ISB erforderlich, und die Daten müssen auf der gleichen Klassifizierungsstufe wie in der Produktion behandelt werden.

Wo die Organisation Data-Leakage-Prevention-Tools (DLP) einsetzt, müssen DLP-Richtlinien mit dem Klassifizierungsschema abgestimmt werden, um unbefugte Übertragung oder Offenlegung von VERTRAULICHEN Informationen zu erkennen und zu verhindern (z. B. Blockierung externer E-Mails mit als VERTRAULICH gekennzeichneten Dateien, Verhinderung des Uploads zu nicht genehmigten Cloud-Diensten).

### Handhabung mündlicher Informationen

Mündlich besprochene vertrauliche Informationen (in Meetings, Telefonaten oder Gesprächen) müssen mit angemessener Sorgfalt behandelt werden:

- Besprechungen vertraulicher Informationen müssen in privaten Umgebungen stattfinden (geschlossene Büros, Besprechungsräume mit geschlossenen Türen) — nicht in Grossraumbüros, öffentlichen Räumen oder öffentlichen Verkehrsmitteln.
- Virtuelle Meetings, in denen vertrauliche Informationen besprochen werden, müssen verschlüsselte Plattformen mit auf autorisierte Teilnehmer beschränktem Zugang verwenden.
- Teilnehmer müssen zu Beginn des Meetings an den vertraulichen Charakter der Diskussion erinnert werden.
- Notizen oder Protokolle vertraulicher Diskussionen müssen entsprechend klassifiziert und behandelt werden.

### Kontrolle von Geräten und Medien

Alle elektronischen und Papiermedien mit vertraulichen Informationen müssen physisch vor unbefugtem Zugriff durch Sicherung in abgeschlossenen Schubladen, Schränken oder eingeschränkten Räumen geschützt werden.

Wechseldatenträger (USB-Laufwerke, externe Festplatten, Backup-Bänder) mit vertraulichen Daten müssen verschlüsselt und gemäss der Asset-Management-Richtlinie im Asset-Inventar registriert werden.

### Informations-Backup

Organisationsinformationen müssen gemäss dem Backup-Zeitplan gesichert, aufbewahrt und getestet werden. Backups müssen mit starker Verschlüsselung verschlüsselt werden. Alle Backups müssen an sicheren Orten mit auf autorisiertes Personal beschränktem Zugang gespeichert werden.

---

## Vernichtung von Informationen

Wenn Informationen nicht mehr benötigt werden und ihre Aufbewahrungsfrist abgelaufen ist, müssen sie gemäss ihrer Klassifizierungsstufe sicher vernichtet werden.

### Vernichtung von Papierdokumenten

| Klassifizierung | Vernichtungsstandard |
|----------------|---------------------|
| **VERTRAULICH** | Kreuzschnitt-Schreddern nach DIN 66399 Sicherheitsstufe P-4 oder höher, oder Einwurf in genehmigte Vertraulichkeits-Abfallbehälter eines zertifizierten Vernichtungsanbieters |
| **INTERN** | Kreuzschnitt-Schreddern nach DIN 66399 Sicherheitsstufe P-3 oder höher, oder genehmigte Vertraulichkeits-Abfallbehälter |
| **ÖFFENTLICH** | Standard-Recycling oder allgemeiner Abfall |

### Vernichtung elektronischer Informationen

| Klassifizierung | Vernichtungsstandard |
|----------------|---------------------|
| **VERTRAULICH** | Kryptographische Löschung (Verschlüsselungsschlüssel vernichten) oder NIST SP 800-88-konformes Überschreiben; Verifikation der Löschung dokumentiert |
| **INTERN** | Sichere Löschung (Überschreiben); Standard-Mediensäuberung |
| **ÖFFENTLICH** | Standard-Löschung |

Protokolle der Wipe-Vorgänge müssen aufbewahrt werden, wo das Säuberungstool dies unterstützt.

### Vernichtung elektronischer Medien und Geräte

Elektronische Medien und Geräte, auf denen vertrauliche oder interne Informationen gespeichert waren, müssen bei Nichtmehr-Bedarf durch genehmigte Methoden vernichtet werden:

- **SSDs und Flash-Speicher**: Kryptographische Löschung (ATA Secure Erase) oder physische Vernichtung.
- **Festplatten**: NIST SP 800-88-konformes Überschreiben oder physische Vernichtung (Entmagnetisierung, Schreddern).
- **Backup-Bänder**: Entmagnetisierung oder physische Vernichtung.
- **Optische Medien**: Physisches Schreddern.

Die Vernichtung vertraulicher Medien muss von genehmigten spezialisierten Drittanbietern durchgeführt werden, wo eine interne Vernichtung nicht möglich ist. Vernichtungszertifikate müssen eingeholt und als Nachweis aufbewahrt werden.

Ein Inventar der Geräte, einschliesslich vernichteter, muss gemäss der Asset-Management-Richtlinie gepflegt werden.

---

## Umklassifizierung

Die Informationsklassifizierung ist nicht dauerhaft. Informationen müssen umklassifiziert werden, wenn:

- Die Sensitivität oder der Wert der Informationen sich ändert.
- Gesetzliche oder regulatorische Anforderungen sich ändern.
- Eine vertragliche Verpflichtung ausläuft (z. B. NDA-Periode endet).
- Informationen für die Veröffentlichung genehmigt werden.
- Der Informationseigentümer bestimmt, dass die aktuelle Klassifizierung nicht mehr angemessen ist.

Die Umklassifizierung wird vom Informationseigentümer durchgeführt und die Kennzeichnung entsprechend aktualisiert.

---

## Nachweise

Die folgenden Nachweise demonstrieren die Einhaltung dieser Richtlinie:

- **Dokumentation des Informationsklassifizierungsschemas** (diese Richtlinie) — *jährlich überprüft*
- **Beispiele klassifizierter Dokumente** mit korrekter Kennzeichnung (Kopfzeilen, Fusszeilen, E-Mail-Präfixe) — *Stichprobe von 5–10 Dokumenten pro Klassifizierungsstufe beim jährlichen Audit gesammelt*
- **Umsetzungsnachweise der Handhabungsmatrix** (Zugriffskontrollen, Verschlüsselungseinstellungen, Weitergabebeschränkungen) — *System-Konfigurations-Screenshots oder Audit-Exporte; jährlich überprüft*
- **Vernichtungsnachweise für vertrauliche Medien** (Vernichtungszertifikate, Wipe-Protokolle) — *5 Jahre aufbewahrt; jährlich mit Asset-Entsorgungsunterlagen abgeglichen*
- **Informations-Asset-Register** mit Klassifizierungszuweisungen (gemäss Asset-Management-Richtlinie) — *Ziel: 100% der Informations-Assets klassifiziert; jährlich gemessen*
- **Schulungsunterlagen** mit Mitarbeitenden, die zu Klassifizierungs- und Handhabungsanforderungen ausgebildet wurden — *jährliches Sensibilisierungstraining; Abschluss verfolgt*
- **Ausnahmeunterlagen** für Abweichungen von Handhabungsregeln — *vierteljährlich überprüft; beim Management-Review vorgestellt*
- **DLP-Richtlinienkonfiguration und Vorfallsberichte** (wo DLP eingesetzt) — *vierteljährlich überprüft*

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheitsmanagement-Team wird die Einhaltung dieser Richtlinie durch verschiedene Methoden überprüfen, einschliesslich, aber nicht beschränkt auf, Dokumentenstichproben für korrekte Kennzeichnung, Zugangskontroll-Audits, Medienvernichtungsunterlagen, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vom Informationssicherheitsmanager im Voraus genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum. Ausnahmen müssen dem Management-Review-Team gemeldet werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterliegen, bis hin zur Beendigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen müssen Änderungen der Klassifizierungsstandards, regulatorische Anforderungen (einschliesslich Entwicklungen bei nDSG und DSGVO), aufkommende Datenschutzrisiken und Lessons Learned aus Vorfällen berücksichtigen.

---

# Bereiche des ISO 27001-Standards, die adressiert werden

Informationsklassifizierungs- und -handhabungs-Richtlinie — ISO 27001-Kontrollzuordnung

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Managementverantwortung |
| Klausel 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| Klausel 7.3 Bewusstsein | **5.12 Klassifizierung von Informationen** |
| Klausel 7.5.2 Erstellen und Aktualisieren von Dokumentation | **5.13 Kennzeichnung von Informationen** |
| Klausel 7.5.3 Steuerung dokumentierter Informationen | 6.3 Sensibilisierung, Schulung und Training zur Informationssicherheit |
| | 6.4 Disziplinarverfahren |
| | 7.10 Speichermedien |
| | 7.14 Sichere Entsorgung oder Wiederverwendung von Geräten |
| | 8.10 Löschung von Informationen |
| | 8.11 Datenmaskierung |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 5 — Definition sensibler Personendaten (entspricht VERTRAULICH); Art. 8 — Technische und organisatorische Massnahmen |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (soweit anwendbar) | Art. 5 — Datenschutzgrundsätze; Art. 9 — Besondere Kategorien personenbezogener Daten; Art. 32 — Sicherheit der Verarbeitung |
| ISO/IEC 27001:2022 | Annex A Kontrollen 5.12, 5.13 |
| ISO/IEC 27002:2022 | Abschnitte 5.12, 5.13 — Umsetzungshinweise |
| NIST SP 800-53 Rev 5 | RA-2 (Security Categorisation), AC-16 (Security and Privacy Attributes), MP-3 (Media Marking), MP-6 (Media Sanitisation) |
| CIS Controls v8 | Kontrolle 3 (Data Protection — einschliesslich Klassifizierung, Verschlüsselung, Entsorgung) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
