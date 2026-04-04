<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.11-DE:operational:OP-POL:a.8.11 -->
**ISMS-OP-POL-A.8.11 — Datenmaskierung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Datenmaskierung |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.11 |
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
| 1.0 | [Datum] | ISB | Erstversion der operativen Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt von**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Massnahme A.8.11 — Datenmaskierung

**Verwandte interne Richtlinien**:

- Richtlinie zur Informationsklassifizierung und -handhabung
- Zugangskontrollrichtlinie
- Richtlinie zum Datenschutz und Schutz personenbezogener Daten
- Richtlinie zur Verwendung kryptografischer Verfahren
- Richtlinie zur sicheren Entwicklung
- Richtlinie zur Informationslöschung

**Verwandte Annex-A-Massnahmen**:

| Massnahme | Bezug zur Datenmaskierung |
|-----------|--------------------------|
| A.5.12 Klassifizierung von Informationen | Die Datenklassifizierung bestimmt die Maskierungsanforderungen je Schutzbedarf |
| A.5.15 Zugangskontrolle | Maskierung bietet Tiefenverteidigung über Zugriffskontrollen hinaus |
| A.5.34 Datenschutz und Schutz personenbezogener Daten | Pseudonymisierung und Anonymisierung als Datenschutzmassnahmen |
| A.8.3 Einschränkung des Informationszugangs | Privilegierte Benutzer können mit Überwachung auf unmaskierte Daten zugreifen |
| A.8.10 Informationslöschung | Löschung ist von Maskierung getrennt; beide reduzieren die Exposition |
| A.8.24 Verwendung von Kryptografie | Verschlüsselung schützt Daten im Ruhezustand/bei der Übertragung; Maskierung verschleiert Daten in Verwendung |
| A.8.25 Sicherer Entwicklungslebenszyklus | Entwickler verwenden maskierte Daten in Nicht-Produktionsumgebungen |

---

# Richtlinie zur Datenmaskierung

## Zweck

Zweck dieser Richtlinie ist es, den ordnungsgemässen Einsatz von Datenmaskierung zum Schutz sensibler Informationen — einschliesslich personenbezogener Daten (PII), Finanzdaten und Zugangsdaten — sicherzustellen, indem Daten verschleiert werden, wenn vollständige Einsicht für legitime Geschäftszwecke nicht erforderlich ist.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 7 (Datenschutz durch Technik und datenschutzfreundliche Voreinstellungen) und Art. 8 (Datensicherheit durch technische und organisatorische Massnahmen). Soweit die Organisation Daten von Personen im EU/EWR-Raum verarbeitet, gelten zudem die DSGVO Art. 25 (Datenschutz durch Technik und datenschutzfreundliche Voreinstellungen) und Art. 32 (Sicherheit der Verarbeitung, einschliesslich Pseudonymisierung). Datenmaskierung ist eine zentrale technische Massnahme zum Nachweis der Einhaltung von Datensparsamkeitspflichten unter beiden Rechtsrahmen.

## Geltungsbereich

Diese Richtlinie gilt für:

- Alle sensiblen Datenkategorien: personenbezogene Daten, Finanzdaten, Gesundheitsinformationen, Authentifizierungsdaten, proprietäre Geschäftsinformationen sowie alle als Vertraulich oder Eingeschränkt klassifizierten Daten.
- Alle Umgebungen: Produktion (soweit betrieblich angemessen), Test/QA, Entwicklung, Analyse, Schulung, Sandbox und Backup-/Archivsysteme.
- Alle Maskierungsanwendungsfälle: Bereitstellung von Daten in Nicht-Produktionsumgebungen, Berichtserstellung, Datenweitergabe an Dritte, Anwendungsentwicklung und -test, Analyse sowie Training von Machine-Learning-Modellen.
- Alle Mitarbeitenden, Auftragnehmer und externe Dienstleister, die sensible Daten verarbeiten.

Als Öffentlich klassifizierte Daten gemäss dem Klassifizierungsschema der Organisation sind vom Geltungsbereich ausgenommen. Der verschlüsselte Datenschutz wird unter A.8.24 (Verwendung kryptografischer Verfahren) behandelt. Datenlöschung und -vernichtung werden unter A.8.10 (Informationslöschung) geregelt.

## Grundsatz

Datenmaskierung wird auf Basis des Prinzips der Datensparsamkeit angewendet: Mitarbeitende sollen nur dann Zugang zu echten sensiblen Daten haben, wenn dies für ihre Rolle und Aufgabe unbedingt notwendig ist. In allen anderen Fällen sollen Daten in dem Ausmass maskiert, pseudonymisiert oder anonymisiert werden, dass der Geschäftsnutzen erhalten bleibt.

Es dürfen ausschliesslich von der Organisation genehmigte Maskierungsverfahren und -tools verwendet werden. Die Auswahl des Maskierungsverfahrens soll den Schutzbedarf der Daten, regulatorische Anforderungen, Reversibilitätsbedarf, Formaterhalt und referenzielle Integrität berücksichtigen.

---

## Datenklassifizierung und Maskierungsanforderungen

Maskierungsanforderungen werden durch das Informationsklassifizierungsschema der Organisation (gemäss Massnahme A.5.12) bestimmt. Die folgende Tabelle definiert die Maskierungspflicht je Klassifizierungsstufe:

| Klassifizierung | Maskierungsanforderung | Begründung |
|-----------------|------------------------|------------|
| **Eingeschränkt** | Obligatorische Maskierung in ALLEN Nicht-Produktionsumgebungen | Höchste Sensitivität — Exposition verursacht schwerwiegenden Schaden |
| **Vertraulich** | Obligatorische Maskierung in Nicht-Produktion; risikobasiert in Produktion | Hohe Sensitivität — Exposition verursacht erheblichen Schaden |
| **INTERN** | Risikobasierte Maskierung, wo PII oder regulatorische Anforderungen gelten | Mittlere Sensitivität — selektive Maskierung auf Basis des Inhalts |
| **Öffentlich** | Keine Maskierung erforderlich | Keine Vertraulichkeitsanforderung |

### Sensible Datenkategorien mit Bewertungspflicht

| Kategorie | Beispiele | Typische Klassifizierung |
|-----------|-----------|--------------------------|
| **Personenbezogene Daten (PII)** | Name, AHV-Nummer/SSN, Passnummer, E-Mail, Telefon, Adresse | Eingeschränkt / Vertraulich |
| **Finanzdaten** | Kreditkartennummer (PAN), IBAN, Kontostand, Gehalt, Steueridentifikationsnummer | Eingeschränkt / Vertraulich |
| **Gesundheitsinformationen** | Patientenaktennummer, Diagnosen, Verschreibungen, Laborbefunde | Eingeschränkt |
| **Authentifizierungsdaten** | Passwörter, API-Schlüssel, Tokens, private Schlüssel, Verbindungszeichenfolgen | Eingeschränkt |
| **Proprietäre Geschäftsdaten** | Geschäftsgeheimnisse, Preisstrategien, Kundenverträge | Vertraulich |
| **Besondere Kategorien** (DSGVO Art. 9 / nDSG besonders schützenswerte Personendaten) | Ethnische Herkunft, politische Meinungen, religiöse Überzeugungen, biometrische Daten | Eingeschränkt |

### Datenerkennung und -inventar

Die Organisation soll ein Inventar sensibler Daten, die maskiert werden müssen, führen, einschliesslich:

- Systeme und Datenbanken, die sensible Daten enthalten.
- Datenelemente (Tabellen, Spalten, Felder), die Maskierung erfordern.
- Datenklassifizierung je Element und anwendbare regulatorische Anforderungen.
- Dateneigentümer, der für Maskierungsentscheidungen verantwortlich ist.

Die Datenerkennung soll für alle Umgebungen mit Eingeschränkten oder Vertraulichen Daten automatisiert erfolgen, unter Verwendung von [Datenerkennungstool] oder gleichwertigem. Die automatisierte Erkennung soll bekannte sensible Datenmuster (PII-Muster, Kreditkartennummern, AHV-/SSN-Formate, Gesundheitsidentifikatoren) mindestens vierteljährlich scannen. Manuelle Inventarisierung ist für Organisationen mit begrenzten Datenbeständen und keinen Eingeschränkten Daten akzeptabel, soll jedoch durch automatisierte Erkennung ergänzt werden, wenn der Datenbestand wächst.

Dateneigentümer sind verantwortlich für die Klassifizierung von Daten in ihren Domänen, die Festlegung von Maskierungsanforderungen, die Genehmigung von Maskierungsverfahren für ihre Daten sowie die Validierung der Maskierungseffektivität.

---

## Genehmigte Maskierungsverfahren

Die folgenden Maskierungsverfahren sind für den organisatorischen Einsatz genehmigt:

| Verfahren | Beschreibung | Reversibilität | Primäre Anwendungsfälle |
|-----------|--------------|----------------|-------------------------|
| **Statische Datenmaskierung (SDM)** | Dauerhafte Ersetzung von Daten in Nicht-Produktionsdatenbanken, bevor Daten die Produktionsumgebung verlassen | Irreversibel | Nicht-Produktionsumgebungen, externe Datenweitergabe |
| **Dynamische Datenmaskierung (DDM)** | Echtzeitsmaskierung zum Zeitpunkt der Abfrage basierend auf Benutzerrolle; Originaldaten bleiben unverändert im Speicher | Nicht zutreffend (Original unverändert) | Produktionsbasierter Zugriff nach Rollen, Compliance-Anzeigeregeln |
| **Schwärzung / Nullifizierung** | Vollständige Entfernung oder Ersetzung durch Platzhalterzeichen (z. B. `****`, `[GESCHWÄRZT]`) | Irreversibel | Berichte, Exporte, Screenshots, UI-Anzeige |
| **Substitution** | Ersetzung durch realistische fiktive Daten unter Beibehaltung von Format und Verteilung | Irreversibel | Testdatengenerierung, Erhalt des Datennutzens |
| **Tokenisierung** | Ersetzung durch nicht-sensible Tokens; Originaldaten in sicherem Token-Tresor gespeichert | Reversibel (mit Tresor-Zugang) | Zahlungssysteme, referenzielle Integrität, PCI DSS |
| **Pseudonymisierung** | Ersetzung durch Pseudonyme; Re-Identifizierung nur mit separat gehaltenem Schlüssel möglich | Reversibel (mit Schlüssel) | DSGVO/nDSG-Compliance, Forschung, Analyse |
| **Anonymisierung** | Irreversible Entfernung aller identifizierenden Informationen; keine Schlüssel oder Zuordnungen werden beibehalten | Irreversibel | Öffentliche Datenpublikation, statistische Analyse, offene Datensätze |

### Auswahlkriterien für Verfahren

Bei der Auswahl eines Maskierungsverfahrens sollen folgende Faktoren berücksichtigt werden:

1. **Datensensitivität**: Höhere Sensitivität erfordert stärkere, weniger reversible Maskierung.
2. **Regulatorische Anforderungen**: DSGVO-Pseudonymisierung (Art. 32, Art. 89), PCI-DSS-Anzeigemaskierung (Req. 3.4–3.5), nDSG-Datensparsamkeit (Art. 6).
3. **Geschäftlicher Anwendungsfall**: Entwicklung/Test, Analyse, externe Weitergabe oder Schulung.
4. **Reversibilitätsbedarf**: Ob ein legitimer Bedarf besteht, Originaldaten wiederherzustellen.
5. **Formaterhalt**: Ob die Anwendung das Datenformat beibehalten erfordert.
6. **Referenzielle Integrität**: Ob tabellenübergreifende Beziehungen und Fremdschlüssel gültig bleiben müssen.
7. **Performance-Auswirkung**: Echtzeit-DDM-Overhead gegenüber Batch-SDM-Verarbeitung.

Neue Maskierungsverfahren oder wesentliche Änderungen an genehmigten Verfahren sollen dem Security Team vorgeschlagen werden, eine Sicherheitsüberprüfung und -testung durchlaufen und vor dem Einsatz vom ISB genehmigt werden.

### Pseudonymisierung vs. Anonymisierung (Regulatorische Unterscheidung)

Unter DSGVO und nDSG bleiben pseudonymisierte Daten personenbezogene Daten, da eine Re-Identifizierung mit dem separat gehaltenen Schlüssel möglich ist. Anonymisierte Daten — bei denen eine Re-Identifizierung vernünftigerweise nicht mehr möglich ist — fallen ausserhalb des Anwendungsbereichs der Datenschutzgesetzgebung. Die Organisation soll sicherstellen, dass das korrekte Verfahren angewendet wird, je nachdem, ob die Daten im Datenschutzbereich bleiben müssen (Pseudonymisierung) oder vollständig aus diesem Bereich entfernt werden können (Anonymisierung).

**Bewertung des Datennutzens bei Anonymisierung**: Vor Anwendung der Anonymisierung soll der Dateneigentümer prüfen, ob die anonymisierten Daten für den beabsichtigten Zweck ausreichenden Geschäftsnutzen behalten. Die Bewertung soll Folgendes berücksichtigen:

- Ob statistische Eigenschaften (Verteilungen, Korrelationen, Trends) erhalten bleiben.
- Ob die anonymisierten Daten den beabsichtigten Analyse-, Schulungs- oder Testanwendungsfall unterstützen.
- Ob übermässige Generalisierung oder Unterdrückung die Daten unbrauchbar macht.
- Abwägungen zwischen Datenschutz (höhere k-Anonymität) und Datennutzen (weniger Generalisierung).

Wo Anonymisierung den Datennutzen übermässig einschränkt, kann Pseudonymisierung mit angemessenen Zugriffskontrollen eine vorzugswürdige Alternative sein.

Pseudonymisierungsschlüssel sollen separat von den pseudonymisierten Daten gespeichert werden, mit folgenden Trennungsanforderungen:

- **Physische oder logische Trennung**: Schlüssel sollen in einem anderen System, einer anderen Datenbank oder einem anderen Sicherheitsbereich als die pseudonymisierten Daten gespeichert werden. Die gemeinsame Ablage von Schlüsseln und Daten auf demselben Server oder in derselben Datenbank ist untersagt.
- **Zugriffstrennung**: Mitarbeitende mit Zugang zu pseudonymisierten Daten sollen keinen Zugang zu Re-Identifizierungsschlüsseln haben, es sei denn, dies ist für einen dokumentierten Zweck spezifisch autorisiert. Für die Re-Identifizierung von Eingeschränkten Daten ist eine Zwei-Personen-Autorisierung (Dual Control) erforderlich.
- **Protokollierung von Re-Identifizierungen**: Alle Re-Identifizierungsvorgänge sollen mit Identität des Anforderers, Begründung, Datenumfang und Genehmigungsreferenz protokolliert werden.

Das Schlüsselmanagement soll der Richtlinie zur Verwendung kryptografischer Verfahren (A.8.24) folgen.

---

## Verbotene Praktiken

Folgende Praktiken sind NICHT als Maskierungsverfahren akzeptabel:

| Verbotene Praktik | Begründung |
|-------------------|------------|
| **ROT13 oder Caesar-Chiffre** | Trivial reversibel; nicht kryptografisch sicher |
| **Ausschliesslich reversible Kodierung** (Base64, URL-Kodierung, Hex) | Keine Maskierung — nur Kodierung; von jedem leicht umkehrbar |
| **Einfache Zeichensubstitution** (A=1, B=2) | Vorhersehbares Muster; trivial reversibel |
| **Ausschliesslich clientseitige Maskierung** (JavaScript / UI-Schicht) | Umgehbar — Daten bleiben im Backend unmaskiert |
| **Selbst entworfene „Verschlüsselung"** | Nicht validierte Sicherheit; für Compliance nicht akzeptiert |
| **Produktionsdaten in Nicht-Produktion ohne jegliche Maskierung** | Kernverstoss gegen die Richtlinie |
| **Unbegrenzte Verwendung desselben maskierten Datensatzes ohne Aktualisierung** | Veraltete Daten; potenzielle Umgehung im Laufe der Zeit |

Diese Praktiken erwecken den Anschein von Sicherheit ohne tatsächlichen Schutz. Sie sind unter keinen Umständen akzeptabel, und es kann keine Ausnahme für ihre Verwendung gewährt werden.

---

## Umgebungsabdeckungsanforderungen

Sensible Daten sollen in Umgebungen maskiert werden, in denen vollständige Datensichtbarkeit für den legitimen Geschäftsbetrieb nicht erforderlich ist.

| Umgebung | Maskierungsanforderung | Begründung |
|----------|------------------------|------------|
| **Produktion** | Risikobasiert; DDM anwenden, wo betrieblich durchführbar | Geschäftsbetrieb kann einige echte Daten erfordern; Begründung für unmaskierte Daten dokumentieren |
| **Test / QA** | Obligatorisch für Eingeschränkte und Vertrauliche Daten | Kein Geschäftsbedarf für echte sensible Daten beim Testen |
| **Entwicklung** | Obligatorisch für Eingeschränkte und Vertrauliche Daten | Entwickler benötigen keine echten sensiblen Daten |
| **Analyse / BI** | Obligatorisch, sofern Daten nicht aggregiert oder anonymisiert sind | Analyse kann mit maskierten oder aggregierten Daten funktionieren |
| **Schulung / Demo** | Obligatorisch für ALLE sensiblen Daten — keine Ausnahmen | Schulungsumgebungen müssen nicht-sensible Daten verwenden |
| **Sandbox / Experimentell** | Obligatorisch für ALLE sensiblen Daten — keine Ausnahmen | Unkontrollierte Umgebungen sind hohes Risiko |
| **Backup / Archiv** | Gleicher Schutz wie Quellumgebung | Backups spiegeln den Schutzbedarf der Quelldaten wider |

### SDM-Implementierungsanforderungen

- SDM soll BEVOR Daten die Produktionsumgebung verlassen angewendet werden.
- SDM soll referenzielle Integrität über verknüpfte Tabellen hinweg wahren. Wo tabellenübergreifende Beziehungen bestehen, soll Maskierung konsistent unter Verwendung desselben Maskierungsschlüssels oder derselben Zuordnung angewendet werden, um Fremdschlüsselbeziehungen, Join-Integrität und tabellenübergreifende Geschäftsregeln zu erhalten. Die referenzielle Integrität soll durch automatisierte Tests nach jedem Maskierungszyklus validiert werden.
- SDM soll das Datenformat für die Anwendungskompatibilität erhalten. Hinweis: Formaterhalt kann die Maskierungsentropie (Anzahl möglicher maskierter Werte) reduzieren, was das Re-Identifizierungsrisiko erhöht. Für Eingeschränkte Daten soll die Organisation prüfen, ob formaterhaltende Maskierung ausreichende Sicherheit bietet, oder ob nicht-formaterhaltende Verfahren mit Anpassung auf Anwendungsebene erforderlich sind.
- Maskierte Daten sollen für Anwendungstests realistisch genug sein.
- **Aktualisierung maskierter Daten**: Nicht-Produktionsumgebungen, die SDM verwenden, sollen in einer definierten Häufigkeit mit neu maskierten Daten aktualisiert werden — mindestens vierteljährlich für aktive Entwicklungsumgebungen und halbjährlich für weniger aktive Umgebungen. Die Aktualisierungshäufigkeit soll Produktionsdatenänderungen, die die Testvalidität beeinflussen könnten, und das Risiko der Maskierungsumgehung durch angesammelte Kenntnisse veralteter maskierter Datensätze berücksichtigen.

### DDM-Implementierungsanforderungen

- DDM soll auf Datenbank- oder Anwendungsebene erzwungen werden — nicht clientseitig.
- DDM-Regeln sollen auf dokumentierten Benutzerrollen und dem Least-Privilege-Prinzip basieren.
- DDM soll von Benutzern ohne entsprechende Autorisierung nicht umgangen werden können. Umgehungsschutzkontrollen sollen umfassen:
  - Direkter Datenbankzugang (unter Umgehung der Anwendungsebene) soll auf autorisierte Datenbankadministratoren beschränkt sein.
  - DDM-Regeln sollen, wo unterstützt, auf Datenbankebene erzwungen werden, nicht ausschliesslich auf Anwendungsebene.
  - Versuche, zugrunde liegende unmaskierte Daten über Views, gespeicherte Prozeduren oder alternative Zugriffspfade abzufragen, sollen blockiert oder protokolliert und alarmiert werden.
  - Periodische Tests sollen verifizieren, dass DDM nicht durch SQL-Injection, Privilege-Eskalation oder Schema-Manipulation umgangen werden kann.
- Performance-Auswirkungen sollen bewertet und innerhalb definierter Schwellenwerte gehalten werden:
  - **Abfragelatenz**: DDM soll bei Standard-Abfragen nicht mehr als 15 % Latenz gegenüber Basis-Antwortzeiten hinzufügen.
  - **Durchsatz**: DDM soll den Datenbankdurchsatz unter normalen Betriebsbedingungen nicht um mehr als 10 % reduzieren.
  - **Basismessung**: Performance-Baselines sollen vor dem DDM-Einsatz festgestellt und vierteljährlich neu gemessen werden.
  - **Eskalation**: Wenn DDM Performance-Schwellenwerte überschreitet, soll das Security Team alternative Maskierungsansätze bewerten (SDM-Vorverarbeitung, Maskierung auf Anwendungsebene oder DDM-Regeloptimierung).

### Tokenisierungsanforderungen

- Der Token-Tresor soll mit Zugriffskontrollen und Verschlüsselung gesichert sein. Tressor-Verschlüsselungsschlüssel sollen:
  - In einem Hardware-Sicherheitsmodul (HSM) oder [KMS], wo verfügbar, generiert und gespeichert werden.
  - Mindestens jährlich rotiert werden, wobei automatisierte Rotation bevorzugt wird.
  - Gemäss den Schlüsselverwaltungsverfahren der Organisation (A.8.24) gesichert und wiederherstellbar sein.
  - Separat von den tokenisierten Daten zugangskontrolliert werden — Tresor-Administratoren sollen keinen direkten Zugang zu tokenisierten Datensätzen haben und umgekehrt.
- Tokens sollen, wo erforderlich, formaterhaltend sein (z. B. Kreditkartenformat für PCI DSS).
- Die De-Tokenisierung soll explizite Autorisierung erfordern und protokolliert werden. De-Tokenisierungs-Zugänge sollen vierteljährlich als Teil von Privileged-Access-Reviews überprüft werden.
- Das Tresor-Schlüsselmanagement soll der Richtlinie zur Verwendung kryptografischer Verfahren (A.8.24) folgen.

---

## Tests und Validierung

Maskierungsimplementierungen sollen vor dem Einsatz und nach Änderungen an der Maskierungskonfiguration getestet werden.

| Testtyp | Zweck | Wann erforderlich |
|---------|-------|-------------------|
| **Effektivitätstests** | Verifikation, dass Originaldaten aus maskiertem Output nicht wiederherstellbar sind | Vor dem Einsatz; nach Änderungen |
| **Tests der referenziellen Integrität** | Verifikation, dass tabellenübergreifende Beziehungen erhalten bleiben | Vor dem Einsatz |
| **Formatvalidierungstests** | Verifikation, dass maskierte Daten Anwendungsvalidierungsregeln bestehen | Vor dem Einsatz |
| **Performance-Tests** | Verifikation, dass DDM-Overhead innerhalb akzeptabler Grenzen liegt | Vor dem DDM-Einsatz |
| **Re-Identifizierungsrisikobewertung** | Verifikation, dass anonymisierte/pseudonymisierte Daten nicht re-identifiziert werden können | Jährlich; nach Datenstrukturänderungen |
| **Regressionstests** | Verifikation, dass Maskierung nach Systemänderungen weiterhin funktioniert | Nach Änderungen der Maskierungskonfiguration |

### Validierungsmethoden

- Stichprobendateninspektion: manueller Vergleich von maskierten und unmaskierten Daten.
- Automatisierte Mustererkennung: Scannen von Nicht-Produktionsumgebungen auf nicht maskierte sensible Datenmuster (z. B. Kreditkartennummern, AHV-Nummern, E-Mail-Adressen).
- Versuche zur Rückentwicklung: Versuche, Originaldaten aus maskiertem Output wiederzugewinnen.
- Für Anonymisierung: statistische Analyse mit risikobasierten Schwellenwerten:
  - **Eingeschränkte Daten**: k-Anonymität >= 20, l-Diversität >= 5 (wo anwendbar).
  - **Vertrauliche Daten**: k-Anonymität >= 10, l-Diversität >= 3 (wo anwendbar).
  - **INTERNE Daten**: k-Anonymität >= 5 Minimum.
  - Wo k-Anonymitätsschwellenwerte nicht erreicht werden können, soll der Datennutzen gegen das Re-Identifizierungsrisiko abgewogen und alternative Techniken (Generalisierung, Unterdrückung, Rauschen) angewendet werden, um den Zielschwellenwert zu erreichen.

### Abnahmekriterien

Maskierung ist akzeptabel, wenn:

- Originale sensible Datenwerte NICHT in maskierten Datensätzen vorhanden sind.
- Datenformat und referenzielle Integrität erhalten sind.
- Anwendungsfunktionalität nicht beeinträchtigt ist.
- Performance-Auswirkungen innerhalb akzeptabler Grenzen liegen.
- Regulatorische Anforderungen erfüllt sind.

Wenn Tests Fehler identifizieren, soll die Implementierung vor dem Produktionseinsatz korrigiert, die Grundursache dokumentiert und eine Wiederholung der Tests durchgeführt werden.

### Bewertungshäufigkeit

- **Umfassende Bewertung**: jährlich (abgestimmt auf das interne Revisionsprogramm).
- **Periodische Verifikation**: vierteljährlich für Hochrisikosysteme und kürzlich geänderte Umgebungen.
- **Anlassbezogene Bewertung**: innerhalb von 30 Tagen nach einem erheblichen Datenschutzvorfall, einer grossen Systemänderung mit Auswirkung auf sensible Daten, der Einführung einer neuen Maskierungslösung oder einer Änderung regulatorischer Anforderungen.

---

## Protokollierung und Überwachung

Die folgenden maskierungsbezogenen Ereignisse sollen, soweit technisch machbar, protokolliert werden:

- Ausführung des Maskierungsprozesses (Start, Abschluss, Fehler).
- Änderungen der Maskierungskonfiguration (Verfahrensänderungen, Regelaktualisierungen). Konfigurationsänderungen sollen dem Change-Management-Prozess der Organisation folgen: durch autorisiertes Personal angefordert, vom Security Team überprüft, in einer Nicht-Produktionsumgebung getestet, vom Dateneigentümer und Security-Team-Lead vor dem Produktionseinsatz genehmigt sowie mit Vor-/Nachkonfigurationszuständen protokolliert.
- Maskierungsausnahmen und -umgehungen (genehmigt oder versucht).
- Anwendung dynamischer Maskierungsregeln (wer auf welche Daten mit welcher Maskierungsregel zugegriffen hat).
- Maskierungsfehler (Prozesse, die nicht abgeschlossen wurden).

**Protokollaufbewahrung**:

| Ereignistyp | Mindestaufbewahrung |
|-------------|---------------------|
| Maskierungsprozessprotokolle | 90 Tage |
| Konfigurationsänderungen | 12 Monate |
| Ausnahmen und Umgehungsereignisse | 12 Monate |
| Dynamische Maskierungs-Zugriffsprotokolle | 90 Tage (Vertraulich+) |

Verlängerte Aufbewahrung gilt, wenn regulatorische Anforderungen längere Fristen vorschreiben.

Die Organisation soll Maskierungsprozessfehler, wiederholte Umgehungsversuche, nicht autorisierte Konfigurationsänderungen und DDM-Performance-Verschlechterung überwachen. Alarme sollen in das Sicherheitsüberwachungsprogramm der Organisation integriert werden.

**Erkennung von Re-Identifizierungsversuchen**: Die Organisation soll Überwachungsmassnahmen implementieren, um potenzielle Re-Identifizierungsversuche zu erkennen, einschliesslich:

- Ungewöhnliche Abfragemuster gegen pseudonymisierte oder anonymisierte Datensätze (z. B. systematische Aufzählung, Querverweise mit externen Datenquellen).
- Massenextraktion von Daten aus Umgebungen mit maskierten Daten.
- Versuche durch nicht autorisiertes Personal, auf Pseudonymisierungsschlüssel oder Token-Tresore zuzugreifen.
- Korrelationsabfragen, die maskierte Datensätze mit unmaskierten Referenzdaten verknüpfen.

Erkannte Re-Identifizierungsversuche sollen als Sicherheitsvorfälle mit hohem Schweregrad behandelt und sofort untersucht werden.

---

## Vorfallreaktion bei Maskierungsfehlern

Sicherheitsvorfälle bei der Datenmaskierung umfassen:

| Vorfalltyp | Schweregrad | Reaktion |
|------------|-------------|----------|
| Nicht maskierte sensible Daten in Nicht-Produktion entdeckt | Hoch | Eindämmung innerhalb 1 Stunde — Datenfluss stoppen, exponierte Daten löschen, Dateneigentümer benachrichtigen |
| Maskierungsprozessfehler, der sensible Daten exponiert | Kritisch | Eindämmung innerhalb 15 Minuten — Exposition stoppen, betroffene Systeme isolieren, ISB benachrichtigen |
| Erfolgreiche Re-Identifizierung maskierter Daten | Hoch | Verfahrensschwachstelle bewerten, Maskierung stärken |
| Maskierungsumgehung oder -umgehungsversuch | Hoch | Untersuchen, Wiederholung verhindern |
| Nicht autorisierter Zugang zu Token-Tresor oder Pseudonymisierungsschlüsseln | Kritisch | Schlüsselkompromittierungsreaktion gemäss A.8.24 |
| Datenexfiltration aus unzureichend maskierter Umgebung | Kritisch | Vollständige Vorfallreaktion, Meldepflichtbewertung |

### Reaktionsprozess

1. **Erkennen und melden**: über Überwachung, Benutzerberichte oder Tests.
2. **Klassifizieren**: Schweregrad basierend auf Datensensitivität und Expositionsumfang.
3. **Einschränken**: Datenfluss stoppen, Systeme isolieren, weitere Exposition verhindern.
4. **Untersuchen**: Grundursachenanalyse, Umfangsbestimmung, Folgenabschätzung.
5. **Beheben**: Maskierung reparieren, Effektivität validieren, Wiederholung verhindern.
6. **Benachrichtigen**: interne Eskalation; regulatorische Meldepflichtanforderungen prüfen.
7. **Überprüfen**: Lessons Learned, Verbesserungen der Kontrollen.

### Meldepflichtbewertung

Datenexpositionsvorfälle sollen auf Meldepflichtanforderungen bewertet werden:

- **Schweizerisches nDSG**: Meldung an den EDÖB (Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter), wenn hohes Risiko für die Persönlichkeit oder die Grundrechte besteht (Art. 24).
- **EU-DSGVO** (wo anwendbar): Meldung innerhalb von 72 Stunden bei Risiko für Rechte und Freiheiten (Art. 33–34).
- **Branchenspezifisch**: PCI-DSS-Datenschutzverletzungsmeldung, HIPAA-Datenschutzverletzungsmeldung (falls anwendbar).

Der Datenschutzbeauftragte (DSB) und der Rechts-/Compliance-Bereich sollen in alle Meldepflichtentscheidungen einbezogen werden.

---

## Ausnahmenmanagement

Ausnahmen von Datenmaskierungsanforderungen erfordern:

- Dokumentierte Geschäftsbegründung, warum Maskierung nicht implementiert werden kann.
- Risikobewertung, die Wahrscheinlichkeit und Auswirkung der Datenexposition abdeckt.
- Ausgleichskontrollen (verstärkte Zugriffskontrollen, Verschlüsselung, Überwachung).
- Definierte Dauer und Weg zur vollständigen Compliance.
- Genehmigung des Dateneigentümers für die betroffene Datendomäne.
- ISB-Genehmigung für Ausnahmen bei Vertraulichen/Eingeschränkten Daten.

| Ausnahmetyp | Erforderliche Genehmigung | Maximale Dauer |
|-------------|---------------------------|----------------|
| Einzelsystem (geringe Sensitivität) | Security-Team-Lead + Dateneigentümer | 12 Monate, mit Meilensteinüberprüfung nach 6 Monaten |
| Einzelsystem (hohe Sensitivität) | ISB + Dateneigentümer | 6 Monate, mit Meilensteinüberprüfung nach 3 Monaten |
| Umgebungsweite Ausnahme | ISB + Dateneigentümer | 6 Monate, mit monatlichem Fortschrittsbericht |
| Produktionsmaskierungsverzicht | ISB + Geschäftsleitung | Jährliche Neugenehmigung, mit vierteljährlichen Meilensteinüberprüfungen |
| Überschreibung verbotener Verfahren | NICHT GESTATTET | Nicht zutreffend |

Aktive Ausnahmen sollen vierteljährlich überprüft, bei Änderung der Geschäftsbegründung widerrufen und am Ende der genehmigten Dauer automatisch ablaufen (keine implizite Erneuerung).

---

## Optional: Zahlungskartenkontrollen (PCI DSS)

*Nur anwendbar, wenn Zahlungskartendaten verarbeitet werden und ein PCI-Geltungsbereich besteht.*

Falls ein PCI-Geltungsbereich besteht, gelten folgende zusätzliche Datenmaskierungsanforderungen:

- Primäre Kontonummern (PANs) sollen überall, wo sie gespeichert sind, unlesbar gemacht werden, gemäss PCI DSS Req. 3.4 (Tokenisierung, Trunkierung, Hashing oder starke Verschlüsselung).
- Bei der Anzeige von PANs soll Maskierung maximal die ersten sechs und letzten vier Ziffern zeigen, gemäss PCI DSS Req. 3.5.1.
- Vollständige PANs sollen in Nicht-Produktionsumgebungen nicht vorhanden sein, es sei denn, die Nicht-Produktionsumgebung erfüllt alle anwendbaren PCI-DSS-Kontrollen. SDM oder Tokenisierung soll angewendet werden, bevor Daten die Karteninhaber-Datenumgebung verlassen.
- Die Nicht-Produktionsverwendung von Zahlungskartendaten soll durch eine dokumentierte Datennutzungsrichtlinie gemäss PCI DSS Req. 12.3 geregelt werden.

---

## Schulung und Sensibilisierung

**Alle Mitarbeitenden** sollen jährliche Sicherheitsbewusstseinsschulungen erhalten, die Folgendes umfassen:

- Die Verpflichtung, maskierte Daten in Nicht-Produktionsumgebungen zu verwenden.
- Wie nicht maskierte sensible Daten erkannt und gemeldet werden.
- Das Verbot, maskierte, pseudonymisierte oder anonymisierte Daten re-identifizieren zu versuchen.

**Technisches Personal** (Security Team, IT-Betrieb, Entwickler) soll Schulungen erhalten zu:

- Genehmigten Maskierungsverfahren und Toolbedienung.
- Test- und Validierungsverfahren.
- Vorfallreaktion bei Maskierungsfehlern.

**Dateneigentümer** sollen über Folgendes informiert werden:

- Verantwortlichkeiten bei Datenklassifizierung und Maskierungsentscheidungen.
- Kriterien für die Bewertung und Genehmigung von Ausnahmeanträgen.
- Validierung der Maskierungseffektivität für ihre Datendomänen.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Anonymisierung** | Irreversible Entfernung aller identifizierenden Informationen, so dass eine Re-Identifizierung nicht möglich ist. Anonymisierte Daten sind gemäss DSGVO/nDSG keine personenbezogenen Daten mehr. |
| **Datenmaskierung** | Prozess der Verschleierung von Originaldaten durch modifizierte Inhalte zum Schutz sensibler Informationen unter Beibehaltung von Datenformat und -nutzbarkeit. |
| **Dynamische Datenmaskierung (DDM)** | Echtzeitsmaskierung, die zum Zeitpunkt des Datenzugriffs basierend auf Benutzerrolle oder Kontext angewendet wird. Originaldaten bleiben unverändert im Speicher. |
| **Pseudonymisierung** | Ersetzung direkter Identifikatoren durch Pseudonyme, so dass Daten Personen ohne zusätzliche Informationen (Schlüssel), die separat gehalten werden, nicht identifizieren können. Pseudonymisierte Daten bleiben personenbezogene Daten. |
| **Re-Identifizierung** | Prozess der Bestimmung der ursprünglichen Identität einer betroffenen Person aus maskierten, pseudonymisierten oder anonymisierten Daten. |
| **Referenzielle Integrität** | Aufrechterhaltung gültiger Beziehungen zwischen zusammenhängenden Daten über Tabellen oder Datensätze hinweg nach der Maskierung. |
| **Statische Datenmaskierung (SDM)** | Dauerhafte Ersetzung sensibler Daten durch maskierte Werte in Nicht-Produktionsdatenbanken. Originaldaten werden irreversibel ersetzt. |
| **Tokenisierung** | Ersetzung sensibler Daten durch nicht-sensible Tokens; Originaldaten in sicherem Token-Tresor gespeichert, was kontrollierte Reversibilität ermöglicht. |

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortung |
|-------|---------------|
| **Geschäftsleitung** | Genehmigung der Datenmaskierungsrichtlinie; Sicherstellung angemessener Ressourcen; Akzeptanz von Restrisiken, wenn Maskierung nicht machbar ist |
| **ISB** | Accountable für Maskierungsrichtlinie und Programmeffektivität; Genehmigung von Hochrisiko-Ausnahmen und neuen Verfahren; jährliche Richtlinienüberprüfung |
| **Datenschutzbeauftragter (DSB)** | Beratung zur DSGVO/nDSG-Compliance für Maskierungsimplementierungen; Überprüfung von Pseudonymisierungs- und Anonymisierungsverfahren auf regulatorische Angemessenheit |
| **Dateneigentümer** | Klassifizierung von Daten; Festlegung von Maskierungsanforderungen; Genehmigung von Verfahren und Ausnahmen für ihre Datendomänen; Validierung der Maskierungseffektivität |
| **Security Team** | Implementierung der Maskierungsrichtlinie; Bewertung und Auswahl von Tools; Konfiguration und Wartung von Lösungen; Durchführung von Effektivitätstests |
| **IT-Betrieb** | Einsatz und Wartung der Maskierungsinfrastruktur; Ausführung von SDM-Batch-Jobs und DDM-Konfiguration; Überwachung der Maskierungsprozessleistung |
| **Entwicklungsteams** | Verwendung maskierter Daten in Nicht-Produktion; Implementierung von DDM in Anwendungen, wo erforderlich; Meldung von Maskierungsproblemen; Umgehung von Kontrollen ist untersagt |
| **Alle Mitarbeitenden** | Einhaltung der Maskierungsrichtlinie; Meldung vermutlich nicht maskierter sensibler Daten in Nicht-Produktion; Versuche zur Re-Identifizierung sind untersagt |

---

## Nachweise

| # | Nachweis | Verantwortlich | Häufigkeit | Aufbewahrung |
|---|----------|----------------|------------|--------------|
| 1 | Sensibles Dateninventar (Systeme, Datenelemente, Klassifizierung, Maskierungsstatus) | Dateneigentümer / Security Team | Jährliche Überprüfung, laufende Aktualisierung | 3 Jahre |
| 2 | Maskierungsverfahrensinventar (genehmigte Verfahren, Tools, Konfigurationen) | Security Team | Jährliche Überprüfung | 3 Jahre |
| 3 | Umgebungsabdeckungsbewertung (welche Umgebungen maskiert sind, Lücken, Ausnahmen) | Security Team | Jährlich, vierteljährlich für Hochrisikobereiche | 3 Jahre |
| 4 | Ergebnisse von Maskierungseffektivitätstests (Stichprobeninspektionen, Musterscans) | Security Team | Vor dem Einsatz; nach Änderungen | 3 Jahre |
| 5 | Ausnahmenregister (aktive Ausnahmen, Genehmigungen, Ausgleichskontrollen, Ablaufdaten) | ISB / Security Team | Vierteljährliche Überprüfung | 3 Jahre |
| 6 | Maskierungsprozessprotokolle und Konfigurationsänderungsaufzeichnungen | IT-Betrieb | Laufend | Gemäss Protokollaufbewahrungstabelle |
| 7 | Vorfallaufzeichnungen für Maskierungsfehler | Security Team | Pro Vorfall | 3 Jahre |
| 8 | **Datenweitergabevereinbarungen mit Dritten** (Maskierungsanforderungen, Re-Identifizierungsverbot, Prüfungsrechte) | Rechtsabteilung / Security Team | Pro Weitergabevereinbarung; jährliche Überprüfung | Aktiv + 3 Jahre |
| 9 | **Ergebnisse der Re-Identifizierungsrisikobewertung** (k-Anonymitätsmessungen, l-Diversität, Datennutzenbewertungen) | Security Team / Dateneigentümer | Jährlich; nach Datenstrukturänderungen | 3 Jahre |
| 10 | **Maskierungskonfigurationsänderungsaufzeichnungen** (Änderungsanträge, Genehmigungen, Vor-/Nachzustände, Testergebnisse) (SOC 2: CC8.1) | Security Team / IT-Betrieb | Pro Änderung | 3 Jahre |
| 11 | **DDM-Performance-Überwachungsaufzeichnungen** (Basismessungen, vierteljährliche Leistungsberichte, Schwellenalarme) | IT-Betrieb | Vierteljährlich | 12 Monate |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheitsmanagement-Team verifiziert die Einhaltung dieser Richtlinie durch verschiedene Methoden, einschliesslich, aber nicht beschränkt auf, automatisierte Scans von Nicht-Produktionsumgebungen auf sensible Daten, Maskierungseffektivitätstests, Ausnahmenregisterüberprüfungen, interne und externe Revisionen sowie Rückmeldungen an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll im Voraus vom Informationssicherheitsbeauftragten genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum. Ausnahmen sollen dem Management-Review-Team gemeldet werden. Verbotene Verfahren können unter keinen Umständen ausgenommen werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung des Arbeitsverhältnisses. Absichtliche Versuche, Maskierungskontrollen zu umgehen oder maskierte Daten zu re-identifizieren, werden als schwerwiegende Sicherheitsverstösse behandelt.

## Anforderungen an die Datenweitergabe an Dritte

Wenn die Organisation maskierte, pseudonymisierte oder anonymisierte Daten an Dritte weitergibt (Lieferanten, Partner, Forscher, Kunden):

- **Vertragliche Anforderungen**: Datenweitergabevereinbarungen sollen Folgendes festlegen:
  - Das angewendete Maskierungsverfahren und die Klassifizierung der Originaldaten.
  - Verbot, maskierte, pseudonymisierte oder anonymisierte Daten zu re-identifizieren.
  - Rückgabe- oder Vernichtungspflichten bei Beendigung der Weitergabevereinbarung.
  - Prüfungsrechte zur Verifikation der Datenverarbeitungspraktiken des Dritten.
  - Meldepflichten des Dritten, wenn entdeckt wird, dass Daten re-identifiziert oder exponiert wurden.
- **Risikobewertung**: Vor der erstmaligen Weitergabe soll eine Datenweitergabe-Risikobewertung durchgeführt werden, die Re-Identifizierungsrisiko, Datenverarbeitungsreife des Dritten und regulatorische Implikationen bewertet.
- **Laufende Überwachung**: Datenweitergabevereinbarungen sollen jährlich und bei wesentlichen Änderungen der Umgebung des Dritten oder des freigegebenen Datenumfangs überprüft werden.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Änderungen der Datenschutzvorschriften, neue Re-Identifizierungsverfahren, neue Maskierungstechnologien, Revisionsergebnisse und Lessons Learned aus Maskierungsvorfällen berücksichtigen.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Richtlinie zur Datenmaskierung — Zuordnung der ISO-27001-Massnahmen

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Abschnitt 5.1 Führung und Verpflichtung | 5.1 Richtlinien zur Informationssicherheit |
| Abschnitt 5.2 Richtlinie | 5.12 Klassifizierung von Informationen |
| Abschnitt 6.1 Massnahmen zum Umgang mit Risiken | 5.15 Zugangskontrolle |
| Abschnitt 6.2 Informationssicherheitsziele | 5.34 Datenschutz und Schutz personenbezogener Daten |
| Abschnitt 7.3 Bewusstsein | 8.3 Einschränkung des Informationszugangs |
| | 8.10 Informationslöschung |
| | **8.11 Datenmaskierung** |
| | 8.24 Verwendung kryptografischer Verfahren |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz | Anwendbarkeit |
|--------|----------|---------------|
| Schweizerisches nDSG (revDSG) | Art. 7 — Datenschutz durch Technik und datenschutzfreundliche Voreinstellungen; Art. 8 — Datensicherheit (technische und organisatorische Massnahmen) | Obligatorisch |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit | Obligatorisch |
| EU-DSGVO (wo anwendbar) | Art. 25 — Datenschutz durch Technik und datenschutzfreundliche Voreinstellungen; Art. 32 — Sicherheit der Verarbeitung (Pseudonymisierung); Art. 89 — Schutzgarantien für Forschung/Statistik | Wo EU/EWR-Personendaten verarbeitet werden |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.11 — Datenmaskierung | Zertifizierungsumfang |
| ISO/IEC 27002:2022 | Abschnitt 8.11 — Implementierungsleitfaden für Datenmaskierungskontrollen | Leitfaden |
| PCI DSS v4.0 | Req. 3.4–3.5 — PAN-Maskierung und Unlesbarkeit; Req. 12.3 — Richtlinien für Nicht-Produktionsdaten | Bei Verarbeitung von Zahlungskartendaten |
| HIPAA Privacy Rule | §164.514 — De-Identifizierungsstandards (Expert Determination / Safe Harbor) | Bei Verarbeitung von US-Gesundheitsdaten (ePHI) |
| FINMA | Kundendatenschutz; Outsourcing-Risikomanagement (Rundschreiben 2018/3) | Bei regulierten Schweizer Finanzinstituten |

---

<!-- QA_VERIFIED: 2026-03-29 -->
