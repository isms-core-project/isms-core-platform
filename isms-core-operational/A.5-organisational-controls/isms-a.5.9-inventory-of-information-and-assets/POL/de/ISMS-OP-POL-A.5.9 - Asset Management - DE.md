<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.9-DE:operational:OP-POL:a.5.9 -->
**ISMS-OP-POL-A.5.9 — Asset Management**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Asset Management |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.5.9 |
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

- ISO/IEC 27001:2022 Control A.5.9 — Inventory of information and other associated assets

**Verwandte Annex-A-Kontrollen**:

| Kontrolle | Bezug zum Asset Management |
|-----------|---------------------------|
| A.5.10 Akzeptable Nutzung von Informationen und anderen Assets | Regeln zur akzeptablen Nutzung verweisen auf inventarisierte Assets |
| A.5.11 Rückgabe von Assets | Asset-Rückgabe im Inventar verfolgt; Register bei Rückgabe/Entsorgung aktualisiert |
| A.5.12–13 Informationsklassifizierung und -kennzeichnung | Klassifizierung den Informations-Assets im Register zugewiesen |
| A.5.14 Informationsübertragung | Übertragungskontrollen basierend auf Asset-Klassifizierung |
| A.5.15–18 Zugangskontrolle und Identitätsverwaltung | Zugriffsrechte von Asset-Eigentümern genehmigt |
| A.7.10 Speichermedien | Wechselmedien als Assets registriert |
| A.7.14 Sichere Entsorgung oder Wiederverwendung von Geräten | Entsorgung aktualisiert Inventarstatus |
| A.8.1 Benutzer-Endgeräte | Endgeräte im Asset-Inventar registriert |
| A.8.8 Management technischer Schwachstellen | Patch-Management erfordert vollständiges Asset-Inventar |
| A.8.9 Konfigurationsmanagement | Konfigurations-Baselines mit inventarisierten IT-Assets verknüpft |

**Verwandte interne Richtlinien**:

- Richtlinie zur Informationsklassifizierung und -handhabung
- Zugangskontroll-Richtlinie
- Endpoint-Sicherheits-Richtlinie
- Richtlinie zur akzeptablen Nutzung
- Datenschutz- und PII-Schutz-Richtlinie

---

# Asset-Management-Richtlinie

## Zweck

Der Zweck dieser Richtlinie ist die Identifizierung, Registrierung und Verwaltung von Organisationsassets, um angemessenen Schutz und Verantwortlichkeit über den gesamten Lebenszyklus zu gewährleisten.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) und die Datenschutzverordnung (DSV), indem sie technische und organisatorische Massnahmen proportional zum Risiko zum Schutz personenbezogener Daten umsetzt, einschliesslich der Kenntnis darüber, welche Daten existieren, wo sie gespeichert sind und wer dafür verantwortlich ist. Wo die Organisation Daten natürlicher Personen im EU/EWR-Raum verarbeitet, gelten auch DSGVO-Anforderungen.

## Geltungsbereich

Alle Mitarbeitenden und Drittnutzer.

Alle Informationen, IT-Infrastruktur, Anwendungen, physischen Assets und Cloud-Dienste der Organisation, die gemäss dem ISO 27001-Geltungsbereich in Scope sind.

## Grundsatz

Organisationsassets sind bekannt, identifiziert, klassifiziert und mit angemessenem Schutz verwaltet. Man kann nicht schützen, was man nicht weiss, dass man es hat. Das Asset-Inventar ist das Fundament, auf dem alle anderen Sicherheitskontrollen beruhen — Risikobeurteilung, Zugangskontrolle, Klassifizierung, Schwachstellenmanagement, Vorfallsreaktion und Geschäftskontinuitätsplanung.

### Asset-Register

Die Organisation muss das Asset-Register in einem zentralisierten Tool oder einer Plattform pflegen (z. B. IT-Asset-Management-System, CMDB oder strukturierte Tabellenkalkulation mit Zugriffskontrollen). Das Register muss für Asset-Eigentümer, IT- und Informationssicherheitsmanagement-Teammitglieder zugänglich und gegen unbefugte Änderungen geschützt sein.

---

## Asset-Kategorien

Folgende Kategorien von Assets müssen inventarisiert werden:

| Kategorie | Beschreibung | Beispiele |
|-----------|-------------|-----------|
| **Hardware** | Physische Geräte, die Informationen verarbeiten, speichern oder übertragen | Server, Workstations, Laptops, Mobilgeräte, Netzwerkgeräte (Router, Switches, Firewalls), Drucker |
| **Software und Lizenzen** | Installierte Software und Abonnementdienste | Betriebssysteme, Geschäftsanwendungen, Entwicklungstools, Sicherheitssoftware, SaaS-Abonnements |
| **Daten und Informationen** | Digitale und physische Informationen mit Wert für die Organisation | Datenbanken, Dateifreigaben, Backups, Archive, Verträge, geistiges Eigentum, Konfigurationsdaten |
| **Cloud-Dienste** | Extern gehostete Dienste, die Organisationsdaten verarbeiten | IaaS (virtuelle Maschinen, Speicher), PaaS (Datenbanken, Plattformen), SaaS (E-Mail, CRM, Zusammenarbeit) |
| **Physische Assets** | Materielle Ressourcen zur Unterstützung der Informationssicherheit | Büros, Serverräume, Safes, Wechselmedien (USB-Laufwerke, Backup-Bänder) |
| **Personalkompetenzen** | Schlüsselrollen und Spezialwissen, die für den Betrieb entscheidend sind | Kritische Rollen (Single Points of Failure), Spezialisierungszertifizierungen, institutionelles Wissen |

**Personalkompetenzen**: Das Register dokumentiert **Rollen und Kompetenzen**, keine individuellen Personendaten. Beispiel: "Datenbankadministrator-Kompetenz (2 qualifizierte Mitarbeitende)" — keine Individualnamen. Wo eine kritische Funktion von einer Einzelperson abhängt (Single Point of Failure), muss dies gekennzeichnet und ein Nachfolge- oder Wissenstransferplan zur Minderung des Risikos dokumentiert werden.

---

## Inventar von Hardware und IT-Infrastruktur

Alle Hardware- und IT-Infrastruktur-Assets müssen im Asset-Inventar registriert werden. Für jedes Asset müssen folgende Attribute erfasst werden:

**Pflichtattribute**:

| Attribut | Beschreibung |
|----------|-------------|
| **Asset-ID** | Eindeutige Kennung (z. B. HW-0042) |
| **Asset-Name** | Menschenlesbarer Name |
| **Asset-Typ** | Kategorie (Server, Laptop, Netzwerkgerät, Mobil, etc.) |
| **Beschreibung** | Zweck und Funktion |
| **Eigentümer** | Für das Asset verantwortliche Person (Name und Funktion) |
| **Abteilung** | Organisationseinheit |
| **Seriennummer / Asset-Tag** | Physische Kennung |
| **Standort** | Physischer Standort (Büro, Rack, Standort) |
| **Klassifizierung** | Gemäss der Richtlinie zur Informationsklassifizierung und -handhabung |
| **Status** | Aktiv / Im Lager / Ausser Betrieb genommen / Entsorgt |
| **Zuletzt überprüft** | Datum der letzten Verifikation des Eintrags |

**Empfohlene zusätzliche Attribute**:

- Kritikalität (Hoch / Mittel / Niedrig) — basierend auf: **Hoch** = Verlust würde erhebliche Betriebsunterbrechung, regulatorische Verletzung oder Datenverlust verursachen; **Mittel** = Verlust würde moderate Auswirkungen verursachen, Ausweichlösung verfügbar; **Niedrig** = Verlust verursacht minimale Auswirkungen, leicht ersetzbar
- IP-Adresse oder Hostname (für netzwerkverbundene Assets)
- Hersteller, Modell und Firmware-/Betriebssystemversion
- Anschaffungsdatum und Garantieablauf
- Verschlüsselungsstatus

---

## Inventar von Software- und Lizenz-Assets

Software und Softwarelizenzen müssen im Asset-Inventar registriert werden. Für jedes Software-Asset müssen folgende Attribute erfasst werden:

| Attribut | Beschreibung |
|----------|-------------|
| **Softwarename** | Produktname und Herausgeber |
| **Version** | Aktuell eingesetzte Version |
| **Eigentümer** | Verantwortliche Person |
| **Lizenztyp** | Dauerlizenz, Abonnement, Open Source, Freeware |
| **Lizenzanzahl** | Anzahl gekaufter vs. eingesetzter Lizenzen |
| **Verlängerungsdatum** | Abonnementablauf oder nächste Verlängerung |
| **Bereitstellungsort** | Wo die Software installiert oder gehostet ist |
| **Geschäftszweck** | Warum die Software verwendet wird |
| **Support-Status** | Vom Anbieter unterstützt / End of Life (EOL) / End of Support (EOS) |

Nur von der Organisation genehmigte und lizenzierte Software darf eingesetzt werden. Nicht autorisierte Software, die bei Inventarüberprüfungen entdeckt wird, muss dem Informationssicherheitsmanagement-Team zur Beurteilung und Entfernung gemeldet werden.

Software, die das End-of-Life oder End-of-Support erreicht hat, muss gekennzeichnet und für Upgrade oder Ersatz priorisiert werden. Wo nicht unterstützte Software nicht sofort ersetzt werden kann, muss das Risiko im Risikoregister mit Ausgleichskontrollen dokumentiert werden.

---

## Inventar von Cloud- und SaaS-Diensten

Cloud-Dienste (IaaS, PaaS, SaaS) müssen zusammen mit traditioneller Software im Asset-Inventar registriert werden. Für jeden Cloud-Dienst müssen folgende zusätzliche Attribute erfasst werden:

| Attribut | Beschreibung |
|----------|-------------|
| **Dienstanbieter** | Anbietername |
| **Diensttyp** | IaaS / PaaS / SaaS |
| **Datenresidenz** | Land oder Region, wo Daten gespeichert werden |
| **Datenklassifizierung** | Klassifizierung der vom Dienst verarbeiteten Daten |
| **SSO-Integration** | Ob der Dienst mit dem Identitätsanbieter der Organisation integriert ist |
| **Vertragseigentümer** | Für die Anbieterbeziehung verantwortliche Person |
| **Verlängerungsdatum** | Vertrags- oder Abonnementablauf |

Cloud-Dienste müssen klassifiziert werden als:

- **Genehmigt**: Von IT und Sicherheit für die Organisationsnutzung freigegeben.
- **Toleriert**: Bekannt, aber nicht formal genehmigt; in Überprüfung (maximal 90 Tage vor Genehmigung oder Verbot).
- **Verboten**: Nicht autorisiert; muss entfernt werden.

Neue Cloud-Dienste müssen im Asset-Inventar registriert werden, **bevor** Organisationsdaten im Dienst verarbeitet werden (oder innerhalb von 5 Arbeitstagen bei Notfallbereitstellungen mit ISB-Genehmigung).

Nicht genehmigte Cloud-Dienste (Schatten-IT) müssen durch regelmässige Überprüfungen von Spesenabrechnungen, SSO-Protokollen und Netzwerkverkehr identifiziert werden. Neu entdeckte Dienste müssen auf Sicherheit und Datenschutz-Compliance beurteilt werden, bevor sie genehmigt werden.

---

## Inventar von Daten- und Informations-Assets

Daten- und Informations-Assets müssen identifiziert und ein Inventar erstellt und gepflegt werden. Für jedes Daten-Asset müssen folgende Attribute erfasst werden:

| Attribut | Beschreibung |
|----------|-------------|
| **Asset-Name** | Name des Datensatzes, der Datenbank oder des Informationsspeichers |
| **Eigentümer** | Verantwortliche Person (die Geschäftspartei, nicht der technische Verwahrer) |
| **Klassifizierung** | Gemäss der Richtlinie zur Informationsklassifizierung und -handhabung |
| **Speicherort** | System oder Dienst, wo die Daten gespeichert sind |
| **Datenresidenz** | Land, wo Daten physisch gespeichert werden |
| **Aufbewahrungsfrist** | Wie lange die Daten entsprechend den Aufbewahrungsanforderungen aufbewahrt werden |
| **Personenbezogene Daten** | Ob der Datensatz personenbezogene Daten enthält (Ja / Nein) |

Wo Daten-Assets personenbezogene Daten enthalten, sollte das Register zusätzliche Felder zur Unterstützung der schweizerischen nDSG-Compliance erfassen:

- Kategorien der betroffenen Personen
- Zweck der Verarbeitung
- Kategorien von Empfängern
- Ob grenzüberschreitende Übertragungen stattfinden (und anwendbare Sicherheitsmassnahmen)

Diese Informationen können im Daten-Asset-Inventar oder in einem separaten **Verzeichnis von Verarbeitungstätigkeiten (VVT)** nach nDSG Art. 12 mit einem Querverweis zwischen den beiden Registern erfasst werden.

---

## Eigentümerschaft von Assets

Jedem inventarisierten Asset muss ein Eigentümer zugewiesen werden. Eigentümerschaft darf nicht leer gelassen werden.

**Eigentümer** bedeutet die Person, die für die Sicherheit des Assets über den gesamten Lebenszyklus verantwortlich ist. Es bedeutet keine rechtlichen Eigentumsrechte. Der Eigentümer kann die tägliche Verwaltung an einen Verwahrer delegieren (z. B. IT verwaltet den Server, aber der Geschäftsbereichsleiter ist Eigentümer der darauf gespeicherten Daten), aber die Verantwortlichkeit verbleibt beim Eigentümer.

### Eigentümer-Verantwortlichkeiten

Asset-Eigentümer müssen:

- Sicherstellen, dass ihre Assets inventarisiert und Einträge korrekt sind.
- Assets entsprechend Geschäftswert und Risiko klassifizieren.
- Inventareinträge für eigene Assets mindestens jährlich überprüfen.
- Zugriffsanträge für eigene Assets genehmigen.
- Sicherheitsvorfälle, die eigene Assets betreffen, melden.
- An Asset-Lebenszyklusentscheidungen teilnehmen (Ausser-Betrieb-Nahme, Archivierung, Entsorgung).

### Eigentümerzuweisung

- Neuen Assets muss bei der Registrierung ein Eigentümer zugewiesen werden.
- Wo die Eigentümerschaft unklar ist, muss das Informationssicherheitsmanagement-Team innerhalb von **30 Kalendertagen** an den zuständigen Manager eskalieren.
- Assets ohne zugewiesenen Eigentümer nach 30 Tagen müssen an den ISB mit dokumentierter Begründung eskaliert werden.
- Eigentümerschaftsänderungen (z. B. Mitarbeiterabgang, Rollenwechsel) müssen innerhalb von **5 Arbeitstagen** im Register aktualisiert werden.

### Verwaiste Assets

**Entdeckte nicht registrierte Assets**: Assets, die im Einsatz, aber nicht im Inventar gefunden werden, müssen sofort mit einem temporären Eigentümer (dem Vorgesetzten des Entdeckers oder IT) registriert, innerhalb von **14 Arbeitstagen** untersucht werden, um den geschäftlichen Eigentümer und Zweck zu bestimmen, und entweder einem dauerhaften Eigentümer formal zugewiesen oder ausser Betrieb genommen werden.

**Eigentümerabgang**: Wenn ein Asset-Eigentümer die Organisation verlässt, muss die Eigentümerschaft innerhalb von **10 Arbeitstagen** nach dem Abgang auf den Vorgesetzten des scheidenden Mitarbeitenden oder einen designierten Nachfolger übertragen werden. Assets ohne neu zugewiesene Eigentümerschaft nach 30 Tagen müssen an den ISB eskaliert werden.

---

## Asset-Lebenszyklus

### Registrierung

Alle Assets müssen innerhalb von **5 Arbeitstagen** nach Anschaffung oder Bereitstellung im Asset-Inventar registriert werden. Assets dürfen nicht mit dem Netzwerk verbunden oder zur Verarbeitung von Organisationsdaten verwendet werden, bis sie registriert sind.

### Pflege und Änderung

Jede Änderung des Eigentümers, Standorts, der Klassifizierung oder des Status eines Assets muss innerhalb von **5 Arbeitstagen** nach der Änderung im Register wiedergespiegelt werden.

### Ausser-Betrieb-Nahme und Entsorgung

Wenn ein Asset ausser Betrieb genommen oder entsorgt wird:

- Daten müssen gemäss der Richtlinie zur Informationsklassifizierung und -handhabung sicher gelöscht oder vernichtet werden, unter Verwendung von Methoden, die **NIST SP 800-88** (Guidelines for Media Sanitization) entsprechen: Clear (logisches Überschreiben) für INTERNE Daten, Purge (kryptographische Löschung oder Entmagnetisierung) für VERTRAULICHE Daten, oder Destroy (physische Vernichtung) wo erforderlich.
- Softwarelizenzen müssen zurückgefordert oder deaktiviert werden.
- Das Asset-Register muss aktualisiert werden, um die Entsorgung einschliesslich Datum und Entsorgungsmethode widerzuspiegeln.
- Für Assets, auf denen vertrauliche oder personenbezogene Daten gespeichert waren, müssen Nachweise der Datensäuberung aufbewahrt werden (z. B. Vernichtungsnachweis, Löschbestätigungsprotokoll).

### BYOD (Bring Your Own Device)

Wo BYOD erlaubt ist, müssen persönlich eigene Geräte, die für den Zugriff auf Organisationsdaten verwendet werden, mit einer Kennzeichnung der persönlichen Eigentümerschaft im Asset-Inventar registriert werden. Mindest-BYOD-Registrierungsattribute:

- Gerätetyp und Betriebssystem
- Name des Mitarbeitenden
- Umfang der geschäftlichen Nutzung (nur E-Mail, vollständiger Zugriff, etc.)
- MDM-Registrierungsstatus
- BYOD-Vereinbarung unterschrieben (Datum)

Bei Kündigung oder Vertragsende müssen Organisationsdaten vom persönlichen Gerät gelöscht und der BYOD-Eintrag aktualisiert werden.

---

## Akzeptable Nutzung von Assets

Die akzeptable Nutzung von Assets muss in Übereinstimmung mit der Richtlinie zur akzeptablen Nutzung erfolgen.

Nutzer dürfen keine nicht autorisierte Software installieren, nicht genehmigte Geräte mit dem Netzwerk verbinden oder Organisationsassets für Zwecke ausserhalb ihres Tätigkeitsbereichs verwenden.

---

## Rückgabe von Assets

Alle Mitarbeitenden und Drittnutzer müssen bei Beendigung ihrer Beschäftigung, ihres Vertrags oder ihrer Vereinbarung alle in ihrem Besitz befindlichen Organisationsassets zurückgeben.

Wo ein Mitarbeitender oder Drittnutzer eigene persönliche Geräte (BYOD) verwendet hat, müssen Verfahren sicherstellen, dass alle Organisationsinformationen an die Organisation übertragen und sicher vom persönlichen Gerät gelöscht werden.

Während der Kündigungsfristen muss die Organisation angemessene Massnahmen ergreifen, um das unbefugte Kopieren von Organisationsinformationen durch scheidende Mitarbeitende oder Drittnutzer zu verhindern.

Das Asset-Register muss aktualisiert werden, um alle zurückgegebenen, neu zugewiesenen oder entsorgten Assets widerzuspiegeln.

---

## Asset-Überprüfung

Das Asset-Inventar muss in folgenden Intervallen überprüft werden:

| Überprüfungstyp | Frequenz | Verantwortlicher |
|----------------|----------|-----------------|
| **Ereignisgesteuerte Aktualisierungen** | Laufend (innerhalb von 5 Arbeitstagen nach Änderung) | Asset-Eigentümer und IT |
| **Eigentümer-Bestätigung** | Jährlich | Jeder Asset-Eigentümer bestätigt die Genauigkeit seiner zugewiesenen Assets |
| **Vollständiges Inventar-Audit** | Jährlich (abgestimmt mit Management-Review) | Informationssicherheitsmanagement-Team |
| **Cloud/SaaS-Discovery-Überprüfung** | Vierteljährlich | IT und Informationssicherheitsmanagement-Team |
| **Software-Lizenz-Compliance** | Halbjährlich | IT |

Abteilungsleiter müssen während der jährlichen Überprüfung bestätigen, dass ihre Asset-Listen aktuell sind. Diskrepanzen müssen untersucht und innerhalb von 30 Tagen behoben werden.

---

## Nachweise

Die folgenden Nachweise demonstrieren die Einhaltung dieser Richtlinie:

- **Asset-Inventarregister** (Hardware, Software, Daten, Cloud-Dienste — mit ausgefüllten Pflichtattributen) — *in zentralisiertem Tool gepflegt; für Audit-Nachweise exportiert*
- **Asset-Eigentümerzuweisungsunterlagen** — *Ziel: 100% der Assets mit zugewiesenen Eigentümern; vierteljährlich gemessen*
- **Eigentümer-Bestätigungsunterlagen** (jährliche Überprüfungsbestätigungen) — *von jedem Asset-Eigentümer unterzeichnet; 3 Jahre aufbewahrt*
- **Cloud/SaaS-Dienstregister** mit Datenresidenz und Klassifizierung — *bei Ereignissen aktualisiert; vierteljährlich überprüft*
- **Software-Lizenz-Compliance-Unterlagen** (gekaufte vs. eingesetzte Lizenzen) — *halbjährlich auditiert*
- **Asset-Entsorgungsunterlagen** (Datum, Methode, NIST SP 800-88-Säuberungsnachweise, Vernichtungszertifikate) — *5 Jahre aufbewahrt*
- **BYOD-Registrierungsunterlagen und Vereinbarungsunterschriften** (falls anwendbar) — *bei Ereignissen aktualisiert; jährlich überprüft*
- **Jährlicher Inventar-Auditbericht** mit Befunden und Korrekturmassnahmen — *beim Management-Review vorgestellt*
- **Inventar-Vollständigkeitsmetrik** — *Ziel: ≥95% der bekannten Assets mit vollständigen Pflichtattributen registriert; jährlich gemessen*
- **Shadow-IT-Discovery-Berichte** — *vierteljährliche Überprüfungen mit Beurteilungsergebnissen dokumentiert*

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheitsmanagement-Team wird die Einhaltung dieser Richtlinie durch verschiedene Methoden überprüfen, einschliesslich, aber nicht beschränkt auf, Asset-Register-Audits, Eigentümer-Bestätigungsüberprüfungen, Lizenz-Compliance-Prüfungen, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vom Informationssicherheitsmanager im Voraus genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum. Ausnahmen müssen dem Management-Review-Team gemeldet werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterliegen, bis hin zur Beendigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen müssen Änderungen der Asset-Management-Standards, organisatorische Änderungen (Akquisitionen, Umstrukturierungen), Cloud-Dienst-Adoption, regulatorische Änderungen und Lessons Learned aus Vorfällen und Audits berücksichtigen.

---

# Bereiche des ISO 27001-Standards, die adressiert werden

Asset-Management-Richtlinie — ISO 27001-Kontrollzuordnung

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Managementverantwortung |
| Klausel 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| Klausel 7.3 Bewusstsein | **5.9 Inventar von Informationen und anderen Assets** |
| | 5.10 Akzeptable Nutzung von Informationen und anderen Assets |
| | 5.11 Rückgabe von Assets |
| | 6.3 Sensibilisierung, Schulung und Training zur Informationssicherheit |
| | 6.4 Disziplinarverfahren |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen (erfordert Kenntnis darüber, welche Daten existieren und wo); Art. 12 — Verzeichnis von Verarbeitungstätigkeiten |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (soweit anwendbar) | Art. 5 — Rechenschaftspflicht-Grundsatz; Art. 30 — Verzeichnis von Verarbeitungstätigkeiten; Art. 32 — Sicherheit der Verarbeitung |
| ISO/IEC 27001:2022 | Annex A Kontrolle 5.9 — Inventar von Informationen und anderen Assets |
| ISO/IEC 27002:2022 | Abschnitt 5.9 — Umsetzungshinweise |
| NIST SP 800-53 Rev 5 | CM-8 (System Component Inventory), PM-5 (System Inventory) |
| CIS Controls v8 | Kontrolle 1 (Inventory and Control of Enterprise Assets), Kontrolle 2 (Inventory and Control of Software Assets) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
