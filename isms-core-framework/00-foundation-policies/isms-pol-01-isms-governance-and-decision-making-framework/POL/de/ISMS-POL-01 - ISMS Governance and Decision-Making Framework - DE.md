<!-- ISMS-CORE:POLICY:ISMS-POL-01-DE:framework:POL:01 -->
**ISMS-POL-01 — ISMS Governance and Decision-Making Framework**

---

## Dokumentenkontrolle

| Feld | Wert |
|------|------|
| **Dokumenttitel** | ISMS Governance and Decision-Making Framework |
| **Dokumenttyp** | Richtlinie (Policy) |
| **Dokument-ID** | ISMS-POL-01 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung (Geschäftsleitung) |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Date - 4 Wochen] | ISB | Ersterstellung — Governance-Grenzen-Framework |

**Review-Zyklus**: Jährlich (oder bei wesentlichen ISMS-Änderungen)
**Nächstes Review-Datum**: [Gültigkeitsdatum + 12 Monate]

**Freigabekette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: Legal/Compliance Officer
- Finale Autorität: Geschäftsleitung (Geschäftsleitung)

**Verknüpfte Dokumente**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.1 (Policies for Information Security)
- Statement of Applicability (SoA)
- Risk Treatment Plan (ISO 27001 Clause 6.1.3)
- Risk Acceptance Register (Clause 6.1.3d)
- ISO 27001:2022 Clause 4.1 (Understanding the organisation and its context)
- ISO 27001:2022 Clause 5.3 (Roles, responsibilities and authorities)
- ISO 27001:2022 Clause 6.1.3 (Information security risk treatment)
- ISO 27001:2022 Clause 7.5.3 (Control of documented information)
- ISO 27001:2022 Clause 9.2 (Internal audit)
- ISO 27001:2022 Clause 9.3 (Management review)
- ISO 27001:2022 Clause 10.2 (Nonconformity and corrective action)

**Verteilung**: Alle ISMS-Stakeholder, Policy-Autoren, System-Owner, interne/externe Auditoren
**Referenziert durch**: Alle ISMS-Policy-Dokumente, Statement of Applicability, Risk Treatment Plan

## Zusammenfassung

Diese Richtlinie legt fest, **wo fachliches Urteilsvermögen** im Informationssicherheits-Managementsystem (ISMS) der Organisation ausgeübt wird, und stellt sicher, dass:

- **Modell-Design-Entscheidungen dokumentiert und autorisiert sind** (Kontrollinterpretation, regulatorische Anwendbarkeit, Risikoakzeptanz)
- **Entscheidungskompetenz klar zugewiesen ist** (ISB, Legal/Compliance, Geschäftsleitung — Zuständigkeit und Umfang)
- **Compliance-Kriterien durch kontrollierte Prozesse weiterentwickelt werden** (regulatorische Änderungen, Bedrohungsevolution, Audit-Feedback)
- **Audit-Verifizierung objektiv und evidenzbasiert ist** (Auditoren verifizieren dokumentiertes Design, interpretieren Anforderungen nicht neu)

**Zweck**: **Objektive Audit-Verifizierung** ermöglichen, indem fachliches Urteilsvermögen in die **Modell-Design-Phase** verlagert wird (dokumentierte Richtlinien, Risikobewertungen, Anwendbarkeitsentscheidungen) und nicht in die **Audit-Diskussionsphase** (subjektive Interpretation während der Zertifizierung).

**Geltungsbereich**: Alle ISMS-Entscheidungskompetenzen, Feststellungen zur regulatorischen Anwendbarkeit, Handhabung von Kontrollausnahmen, Weiterentwicklung von Compliance-Kriterien und Governance-Review-Prozesse.

**Grundprinzip**: **ISO-27001-Zertifizierung erfordert fachliches Urteilsvermögen in zwei Phasen:**

1. **Modell-Design** (Verantwortung der Organisation): ISO 27001 für den organisatorischen Kontext interpretieren, risikobasierte Kontrollen auswählen, ausreichende Nachweise definieren
2. **Modell-Verifizierung** (Verantwortung des Auditors): Bewerten, ob die organisatorische Interpretation ISO 27001 erfüllt, verifizieren, dass Umsetzung mit Dokumentation übereinstimmt

Diese Richtlinie dokumentiert das fachliche Urteilsvermögen der Organisation (Phase 1), um eine objektive Audit-Verifizierung (Phase 2) zu ermöglichen.

---

### Kurzübersicht

| Ich muss... | Weiterleitung zu |
|---|---|
| Verstehen, wer was entscheidet | Abschnitt 2.1 (Authority Boundaries) |
| Kompetenzanforderungen für eine Rolle prüfen | Abschnitt 2.3 (Competence Requirements) |
| Regulatorische Anwendbarkeit bestimmen | Abschnitt 3.1 (Regulatory Applicability) → POL-00 |
| Kontrollanwendbarkeit bestimmen | Abschnitt 3.2 (Control Applicability) → SoA |
| Meinungsverschiedenheit mit Auditor behandeln | Abschnitt 3.3 (Applicability Challenge Protocol) |
| Eine Kontrollausnahme bearbeiten | Abschnitt 4.2 (Exception Process — 5 Schritte) |
| Ausnahmenvolumen und -gesundheit verfolgen | Abschnitt 4.4 (Exception Volume Monitoring) |
| Eine Compliance-Kriterien-Änderung verwalten | Abschnitt 5.2 (Change Process — 6 Schritte) |
| Neubewertung nach einer Änderung verfolgen | Abschnitt 5.4 (Reassessment Tracking) |
| Jährliche Governance-Prüfung vorbereiten | Abschnitt 6.1 (Annual Governance Review) |
| Eine Lektion erfassen | Abschnitt 6.2 (Lessons Learned Register) |
| Dokumentation für ein Audit vorbereiten | Abschnitt 9.1 (Documents Provided to Auditors) |

---

## Policy-Autorität und Governance-Grenzen

### Zweck und Geltungsbereich

Diese Richtlinie definiert **Entscheidungskompetenz** für ISMS-Governance und stellt sicher:

- Klare Zuweisung der Verantwortlichkeit für Compliance-Interpretation
- Dokumentierte Prozesse für Anwendbarkeit, Ausnahmen und Weiterentwicklung
- Kompetenzanforderungen für Entscheidungsträger
- Objektive Kriterien für die Audit-Verifizierung

**Diese Richtlinie legt fest:**

- Kompetenzgrenzen für ISMS-Entscheidungen (Abschnitt 2: Wer entscheidet was, mit welcher Kompetenz)
- Regulatorische und Kontrollanwendbarkeits-Kompetenz (Abschnitt 3: Wer bestimmt, was gilt)
- Ausnahme- und Risikoakzeptanzprozesse (Abschnitt 4: Wie mit Kontrollen umgegangen wird, die nicht umgesetzt werden können)
- Compliance-Kriterien-Änderungskontrolle (Abschnitt 5: Wie das Modell sich weiterentwickelt)
- Monitoring der Governance-Wirksamkeit (Abschnitt 6: Wie Governance-Qualität bewertet wird)

**Diese Richtlinie legt NICHT fest:**

- Spezifische Kontrollumsetzungsanforderungen (adressiert in Annex-A-Kontrollrichtlinien: ISMS-POL-A.X.XX-Reihe)
- Risikobewertungsmethoden (adressiert im Risikobewertungsverfahren: Clause 6.1.2)
- Dokumentenkontrollverfahren (adressiert im Dokumentenkontrollverfahren: Clause 7.5.3)
- Internes Auditprogramm (adressiert im Internen Auditverfahren: Clause 9.2)

**Abgrenzungsprinzip**: Diese Richtlinie legt **Entscheidungskompetenz und -prozesse** fest. Die Entscheidungen selbst (welche Kontrollen, welche Verordnungen, welche Risiken zu akzeptieren) sind dokumentiert in **POL-00 (regulatorische Anwendbarkeit), SoA (Kontrollanwendbarkeit) und Risk Acceptance Register (Risikobehandlungsentscheidungen)**.

**Integration mit ISO 27001**:

- **Clause 4.1 (Context)**: Diese Richtlinie unterstützt das Verständnis des externen Kontexts (wie Verordnungen und Standards für den organisatorischen Kontext interpretiert werden)
- **Clause 5.3 (Roles and responsibilities)**: Formalisiert die Autoritätsstruktur für ISMS-Entscheidungen
- **Clause 6.1.3 (Risk treatment)**: Unterstützt risikobasierte Kontrollauswahl, alternative Kontrollen und Risikoakzeptanzkompetenz
- **Clause 7.5.3 (Document control)**: Legt Governance für Compliance-Kriterien-Änderungen fest
- **Clause 9.3 (Management review)**: Bietet Rahmen für die Prüfung der Governance-Wirksamkeit
- **Clause 10.1 (Continual improvement)**: Ermöglicht Governance-Prozessverbesserung durch Lektionen

## Kompetenzgrenzen und Qualifikationen

### Entscheidungskompetenz

**Kompetenzzuweisung**:

Die folgenden Rollen üben Entscheidungskompetenz in der ISMS-Governance aus. Jede Rolle agiert in einem definierten **Kompetenzbereich** — diese sind funktionale Verantwortlichkeiten, keine Hierarchie der Seniorität:

| Kompetenzbereich | Rolle | Entscheidungsumfang | Kompetenzanforderung |
|-----------------|------|---------------------|---------------------|
| **Technische Sicherheit** | Informationssicherheitsbeauftragter (ISB) | Technisches Kontroll-Design, operative Machbarkeit, Nachweisausreichendheit, tägliche Umsetzungsentscheidungen | Informationssicherheitsexpertise (CISSP/CISM oder gleichwertig, 5+ Jahre Erfahrung), technischer Hintergrund, ISO-27001-Kenntnisse |
| **Regulierung & Recht** | Legal/Compliance Officer | Interpretation regulatorischer Anforderungen, vertragliche Verpflichtungen, rechtliche Risikobewertung, POL-00-Tier-Zuordnungen | Rechtsausbildung oder Compliance-Zertifizierung, Fähigkeit zum regulatorischen Monitoring, Zugang zu externer Rechtsberatung |
| **Datenschutz** | Datenschutzbeauftragter (DSB) | Datenschutzspezifische Kontrollen (A.5.34, GDPR/nDSG-Compliance), Betroffenenrechte, Datenschutz-Folgenabschätzungen. Der DSB übt unabhängige Kompetenz in diesem Bereich gemäss GDPR Artikel 38.3 aus und darf bezüglich der Ausübung dieser Aufgaben keine Weisungen erhalten. | GDPR/nDSG-Expertise, Datenschutzzertifizierung (CIPP/E oder gleichwertig), Unabhängigkeit gemäss GDPR Artikel 38 |
| **Strategie & Risiko** | Geschäftsleitung (GF/Board) | Strategische Risikoentscheidungen, Ressourcenzuteilung, Risikoakzeptanz (Clause 6.1.3d), ISMS-Scope-Änderungen, grosse Architekturentscheidungen | Treuhandpflicht für organisatorisches Risiko, ultimative Verantwortlichkeit für ISO-27001-Zertifizierung, Budgetkompetenz |

**Entscheidungseskalationspfad**:

1. **Routineentscheidungen** (technische Umsetzung, Nachweisformat, Kontroll-Design):
   - **Kompetenz**: ISB
   - **Dokumentation**: POL/IMP-Dokumente, Kontroll-Design-Entscheidungen
   - **Prüfung**: Internes Audit (Clause 9.2), jährliches Management-Review (Clause 9.3)

2. **Regulatorische Interpretation** (POL-00 Tier-1/2-Anwendbarkeit, vertragliche Compliance-Anforderungen):
   - **Kompetenz**: Legal/Compliance Officer (bestimmt Anwendbarkeit) + ISB (setzt Kontrollen um)
   - **Dokumentation**: POL-00 Abschnitt 8 (Regulatory Applicability Matrix)
   - **Prüfung**: Vierteljährliches Monitoring (POL-00 Abschnitt 4.3), jährliche Gesamtprüfung

3. **Risikoakzeptanz** (Kontrollausschluss ohne Alternative, Restrisikoacceptanz gemäss Clause 6.1.3d):
   - **Kompetenz**: ISB schlägt vor (mit Risikobewertung), Geschäftsleitung genehmigt
   - **Dokumentation**: Risk Acceptance Register (Clause-6.1.3d-Dokumentationsanforderung)
   - **Prüfung**: Jährliches Management-Review (Clause 9.3), Aktualisierungen des Risk Treatment Plan

4. **Strategische Änderungen** (ISMS-Scope-Erweiterung, wesentliche Kontrollarchitektur-Änderung, Wechsel der Zertifizierungsstelle):
   - **Kompetenz**: Genehmigung der Geschäftsleitung erforderlich (ISB empfiehlt, GF/Board entscheidet)
   - **Dokumentation**: Management-Review-Protokolle (Clause 9.3.3), Sitzungsprotokolle bei Bedarf
   - **Prüfung**: Im Rahmen des strategischen Planungszyklus der Organisation

**Verpflichtende Anforderungen**:

1. Der ISB **muss** alle technischen Kontrollumsetzungen vor dem Einsatz genehmigen.
2. Der Legal/Compliance Officer **muss** alle Feststellungen zur regulatorischen Anwendbarkeit (POL-00 Tier-Zuordnungen) vor der Veröffentlichung oder Aktualisierung von POL-00 genehmigen.
3. Die Geschäftsleitung **muss** alle Risikoakzeptanzentscheidungen (Kontrollausschlüsse, Restrisikoacceptanz) gemäss ISO 27001 Clause 6.1.3d genehmigen.
4. Die Entscheidungseskalation **muss** dem oben definierten Pfad folgen. Entscheidungen, die ausserhalb der designierten Kompetenz getroffen werden, erfordern nachträgliche Genehmigung oder Korrekturmassnahmen gemäss Clause 10.2.

**Nachweis der Kompetenzzuordnung**:

- **Technische Kontrollen**: Genehmigungsunterschriften auf POL/IMP-Dokumenten (Abschnitt Dokumentenkontrolle)
- **Regulatorische Anwendbarkeit**: Genehmigungsunterschriften auf POL-00 Abschnitt 8 (Regulatory Applicability Matrix)
- **Risikoakzeptanz**: Unterschrift der Geschäftsleitung auf Einträgen im Risk Acceptance Register
- **Strategische Entscheidungen**: Management-Review-Protokolle (Clause 9.3) oder Beschlüsse der Geschäftsleitung

### Fachliches Urteilsvermögen in der ISO-27001-Zertifizierung

**ISO-27001-Zertifizierung erfordert fachliches Urteilsvermögen in zwei getrennten Phasen:**

**Phase 1: Modell-Design (Verantwortung der Organisation)**

Von der Organisation ausgeübtes fachliches Urteilsvermögen umfasst:

1. **Kontextinterpretation** (Clause 4.1):
   - Bestimmen, welche externen Faktoren (Verordnungen, Bedrohungen, Branchenpraktiken) für den ISMS-Scope relevant sind
   - Organisatorische Einschränkungen bewerten (Ressourcen, Architektur, Risikobereitschaft)
   - Dokumentiert in: Organisationskontextdokument, POL-00 (regulatorische Anwendbarkeit)

2. **Kontrollauswahl** (Clause 6.1.3):
   - Kontrollen basierend auf Risikobewertung auswählen (welche Risiken erfordern welche Kontrollen)
   - Kontrollanwendbarkeit bestimmen (anwendbar, nicht anwendbar, alternative Kontrolle)
   - Umsetzungsansatz entscheiden (technische Architektur, operative Prozesse)
   - Dokumentiert in: Statement of Applicability (SoA), Risk Treatment Plan, Kontroll-POL/IMP-Dokumente

3. **Nachweisausreichendheit**:
   - Definieren, welche Nachweise Kontrollwirksamkeit demonstrieren (Python-Arbeitsbücher, Logs, Konfigurationen)
   - Nachweishäufigkeit bestimmen (Echtzeit, täglich, monatlich, vierteljährlich)
   - Nachweisaufbewahrungsfristen festlegen (12 Monate, 3 Jahre, Zertifizierungszyklus)
   - Dokumentiert in: Kontroll-IMP-Dokumente (Nachweis-Abschnitt), Python-Skript-Design

4. **Regulatorische Anwendbarkeit** (POL-00):
   - Bestimmen, welche Verordnungen für die Organisation gelten (Tier-1/2/3-Framework)
   - Auslöser bedingter Verordnungen bewerten (DORA, NIS2, PCI-DSS-Anwendbarkeit)
   - Entscheiden, wann Neubewertung erforderlich ist (vierteljährliches Monitoring, ausgelöste Ereignisse)
   - Dokumentiert in: POL-00 Abschnitt 8 (Regulatory Applicability Matrix)

**Phase 2: Modell-Verifizierung (Verantwortung des Auditors)**

Vom Auditor ausgeübtes fachliches Urteilsvermögen umfasst:

1. **Prozessqualitätsbewertung**:
   - Ist die Risikobewertungsmethodik fundiert und konsistent angewendet? (Clause 6.1.2)
   - Sind Kontrollauswahlentscheidungen angesichts des organisatorischen Kontexts vernünftig? (Clause 6.1.3)
   - Sind Entscheidungsträger gemäss Abschnitt 2.1 kompetent?
   - Sind Governance-Prozesse dokumentiert und eingehalten? (diese Richtlinie)

2. **ISO-27001-Ausrichtung**:
   - Erfüllt die organisatorische Interpretation von Annex-A-Kontrollen die ISO-27001-Kontrollziele?
   - Sind verpflichtende Anforderungen adressiert? (Clause-4-10-Anforderungen, dokumentierte Informationen gemäss Clause 7.5)
   - Ist das Statement of Applicability vollständig und begründet? (alle 93 Kontrollen dokumentiert)

3. **Umsetzungswirksamkeit** (Phase 2):
   - Stimmt die tatsächliche Umsetzung mit dem dokumentierten Design überein? (POL → IMP → Python → Nachweis-Kette)
   - Sind Nachweise ausreichend, um den Kontrollbetrieb nachzuweisen? (Vollständigkeit, Aktualität, Rückverfolgbarkeit)
   - Werden Nichtkonformitäten und Korrekturmassnahmen angemessen behandelt? (Clause 10.2)

4. **Fortlaufende Verbesserung**:
   - Entwickelt sich das ISMS weiter? (interne Auditbefunde adressiert, Management-Review wirksam, Lektionen umgesetzt)
   - Sind Änderungen kontrolliert? (Dokumentenversionskontrolle, Neubewertung nach Änderungen)

**Zusammenarbeitsprinzip**:

Wenn der Auditor potenzielle Lücken im fachlichen Urteilsvermögen der Organisation identifiziert (z. B. Kontrollinterpretation erfüllt ISO-27001-Ziel möglicherweise nicht vollständig, Nachweise könnten unzureichend sein), folgt die Lösung dem **Abschnitt 3.3 Applicability Challenge Protocol**: Die Diskussion konzentriert sich auf die Ausrichtung an ISO-27001-Klauseln und dokumentierte Begründung, nicht auf persönliche Präferenzen oder Autoritätskonflikte.

**Ergebnis**: Das Auditorenurteil konzentriert sich auf die **Verifizierung der Qualität des organisatorischen Urteils**, nicht auf das **Ersetzen organisatorischer Entscheidungen**. Wenn die Auditorenbewertung echte Lücken identifiziert, löst die Organisation Korrekturmassnahmen gemäss Clause 10.2 (Nichtkonformität und Korrekturmassnahmen) aus.

### Kompetenzanforderungen für Entscheidungsträger

**Begründung**: Kompetenz ohne Qualifikation untergräbt die Glaubwürdigkeit der Governance. Dieser Abschnitt legt Mindest-Kompetenzerwartungen für Rollen fest, die ISMS-Entscheidungskompetenz ausüben.

**Kompetenzanforderungen**:

| **Rolle** | **Mindest-Kompetenz** | **Verifizierung** |
| --- | --- | --- |
| **ISB** | - Informationssicherheitszertifizierung (CISSP, CISM oder gleichwertig) - 5+ Jahre Informationssicherheitserfahrung - Technischer Hintergrund (Infrastruktur, Entwicklung oder Sicherheitsbetrieb) - ISO-27001-Kenntnisse (Schulung oder Implementierungserfahrung) | - Lebenslauf mit Erfahrungsnachweis - Professionelle Zertifizierungen (aktuell, nicht abgelaufen) - ISO-27001-Schulungsunterlagen (Lead Implementer oder gleichwertig) |
| **Legal/Compliance Officer** | - Rechtsausbildung (Jurastudium oder Compliance-Zertifizierung wie CCEP, CRCM) - Fähigkeit zum regulatorischen Monitoring (Rechtsdatenbanken, Zugang zu externer Rechtsberatung) - Vertragsüberprüfungserfahrung - Verständnis von ISO-27001-Scope und -Anwendbarkeit | - Rechtsberufsqualifikationen oder Compliance-Zertifizierungen - Unterlagen zur Beauftragung externer Rechtsberatung (für komplexe Interpretationen) - Dokumentierter regulatorischer Monitoring-Prozess (POL-00 Abschnitt 4.3) |
| **Datenschutzbeauftragter (DSB)** | - GDPR/nDSG-Expertise (CIPP/E, CIPM oder gleichwertig) - Unabhängigkeit von der operativen Leitung (gemäss GDPR Artikel 38.3) - Direktberichtslinie zur obersten Führungsebene - Verständnis technischer Datenschutzmassnahmen | - Datenschutzzertifizierungen (IAPP oder gleichwertig) - Organigramm mit Berichtslinie (Unabhängigkeitsnachweis) - GDPR/nDSG-Schulungsunterlagen |
| **Geschäftsleitung** | - Treuhandpflicht für organisatorisches Risiko (GF, FL, Board) - Verständnis der Implikationen der ISO-27001-Zertifizierung - Kompetenz zur Budget- und Ressourcenzuteilung - Verantwortlichkeit für Risikoakzeptanzentscheidungen | - Rollennachweis (Arbeitsvertrag, Boardernennung) - ISO-27001-Executive-Briefing (in Management-Review protokolliert) - Dokumentation der Budgetkompetenz |

**Kompetenzverifizierung**:

- **Erstbenennung**: Kompetenz wird verifiziert, bevor die Rolle ISMS-Entscheidungskompetenz übernimmt (HR-Unterlagen, Beglaubigungsverifizierung)
- **Jährliche Prüfung**: Kompetenz wird jährlich im Management-Review neu bewertet (Clause 9.3) — Zertifizierungen aktuell, Schulung auf dem neuesten Stand, externe Beratung bei Bedarf
- **Kompetenzlücken**: Wenn Kompetenzlücken identifiziert → Adressiert durch Schulung, externe Unterstützung (Berater, Rechtsanwälte) oder Rollenneubesetzung

**Auditor-Verifizierung**:

Während Stage-1- und Stage-2-Audits kann der Auditor verlangen:
- Nachweis der Entscheidungsträger-Kompetenz (Zertifizierungen, Schulungsunterlagen, Erfahrungsdokumentation)
- Verifizierung, dass Entscheidungen mit der zugewiesenen Kompetenz übereinstimmen (z. B. Risikoakzeptanzen von der Geschäftsleitung genehmigt, nicht vom ISB selbst)
- Beurteilung, ob Entscheidungsträger in der Praxis Kompetenz demonstrieren (Qualität der SoA-Begründungen, Risikobewertungen, regulatorische Feststellungen prüfen)

**Hinweis**: Kompetenzanforderungen sind **Mindesterwartungen**, keine erschöpfenden Qualifikationen. Organisationen können diese übertreffen. Kompetenzverifizierung demonstriert Auditoren, dass fachliches Urteilsvermögen (Abschnitt 2.2) von **qualifizierten Personen** ausgeübt wird, nicht als willkürliche Entscheidungsfindung.

## Compliance-Anwendbarkeitskompetenz

### Regulatorische Anwendbarkeit

**Framework**: Regulatorische Anwendbarkeit wird gemäss **ISMS-POL-00 (Regulatory Applicability Framework)** bestimmt, der festlegt:

- **Tier 1 (Mandatory)**: Rechtliche oder vertragliche Verpflichtungen (Swiss nFADP, GDPR wo anwendbar, ISO 27001:2022 für Zertifizierung)
- **Tier 2 (Conditional)**: Anforderungen, die nur bei Erfüllung spezifischer Auslöser gelten (DORA, NIS2, PCI DSS, FINMA, EU AI Act)
- **Tier 3 (Informational)**: Freiwillige Best Practices und technische Orientierung (NIST SP 800-Reihe, CIS Controls, OWASP)

**Entscheidungskompetenz**:

1. **Tier-Bestimmung**: Legal/Compliance Officer bestimmt regulatorische Anwendbarkeit gemäss POL-00 Abschnitt 5 (Bewertungsprozess)
2. **Kontrollumsetzung**: ISB setzt Kontrollen um, um anwendbare Verordnungen zu erfüllen
3. **Genehmigung**: Geschäftsleitung genehmigt die POL-00 Regulatory Applicability Matrix jährlich (POL-00 Abschnitt 7: Annual Review)

**Dokumentation**:

- **POL-00 Abschnitt 8.1**: Tier 1 (Mandatory Compliance) — aktueller Status und Begründung der Anwendbarkeit
- **POL-00 Abschnitt 8.2**: Tier 2 (Conditional Applicability) — Bewertungsstatus, Auslöser, Monitoring-Ansatz
- **POL-00 Abschnitt 8.3**: Tier 3 (Informational Reference) — für technische Orientierung verwendete Rahmenwerke

**Prüfzyklus**:

- **Vierteljährliches Monitoring** (POL-00 Abschnitt 4.3): Legal/Compliance + ISB prüfen regulatorische Änderungen und organisatorische Auslöseereignisse
- **Jährliche Gesamtprüfung** (POL-00 Abschnitt 7): Genehmigung der Geschäftsleitung für regulatorische Anwendbarkeitsfeststellungen
- **Ausgelöste Neubewertung** (POL-00 Abschnitt 5): Geschäftserweiterung, regulatorische Änderungen, Kundenvertragsanforderungen

**Auditor-Verifizierung**:

Auditor verifiziert:
- Bewertungsmethodik zur Anwendbarkeit ist fundiert (POL-00 Abschnitt-5-Prozess ist dokumentiert und rational)
- Neubewertungsauslöser werden überwacht (vierteljährliche Monitoring-Protokolle existieren, ausgelöste Bewertungen sind dokumentiert)
- Tier-Zuordnungen sind angesichts des organisatorischen Kontexts vernünftig (z. B. „Keine Zahlungskartenverarbeitung" → PCI DSS Tier 2 Nicht Anwendbar ist begründet)

Auditor ersetzt NICHT das Urteil bei Anwendbarkeitsentscheidungen (Organisation bestimmt Geschäftsaktivitäten, Auditor verifiziert die Qualität des Bewertungsprozesses).

### Kontrollanwendbarkeit (ISO 27001 Annex A)

**Framework**: Kontrollanwendbarkeit wird gemäss **ISO 27001 Clause 6.1.3 (Risk Treatment)** bestimmt, der fordert:

- Risikobasierte Kontrollauswahl (Kontrollen ausgewählt, um identifizierte Risiken gemäss Clause-6.1.2-Risikobewertung anzugehen)
- Statement of Applicability (SoA) Dokumentation (alle 93 Annex-A-Kontrollen mit Umsetzungsstatus und Begründung dokumentiert)
- Risikobehandlungsentscheidungen (Kontrolle umsetzen, alternative Kontrolle, Risiko gemäss Clause 6.1.3d akzeptieren)

**Entscheidungskompetenz**:

1. **Kontrollauswahl**: ISB schlägt Kontrollumsetzungsansatz basierend auf Risikobewertung vor (Clause 6.1.2)
2. **Risikoakzeptanz**: Geschäftsleitung genehmigt Kontrollausschlüsse (wenn Kontrolle „Nicht Anwendbar" ist oder Risiko ohne Minderung gemäss Clause 6.1.3d akzeptiert wird)
3. **Alternative Kontrollen**: ISB bestimmt Äquivalenz alternativer Kontrollen (dasselbe ISO-27001-Kontrollziel durch andere Mittel erreichen)

**Dokumentation**:

- **Statement of Applicability (SoA)**: Alle 93 Kontrollen dokumentiert mit:
  - **Umsetzungsstatus**: Anwendbar (umgesetzt), Nicht Anwendbar (begründeter Ausschluss), Alternative Kontrolle (andere Umsetzung, die dasselbe Ziel erreicht)
  - **Begründung**: Technische/operative Begründung (warum Kontrolle gilt, warum ausgeschlossen oder warum Alternative verwendet)
  - **Referenz**: POL/IMP-Dokumente für umgesetzte Kontrollen, Risikobewertung für Ausschlüsse
- **Risk Treatment Plan** (Clause 6.1.3): Risikobasierte Begründung für Kontrollauswahl, Priorität und Umsetzungszeitplan
- **Risk Acceptance Register** (Clause 6.1.3d): Genehmigung der Geschäftsleitung für Kontrollen, die ohne alternative Minderung ausgeschlossen wurden

**Entscheidungskriterien für Kontrollanwendbarkeit**:

| Status | Kriterien | Beispiel | Erforderliche Dokumentation |
|--------|----------|---------|----------------------------|
| **Anwendbar** | Risiko existiert, Kontrolle mindert Risiko, Umsetzung machbar | A.8.15 (Logging): Organisation betreibt Server, Logging für Incident-Erkennung erforderlich | POL-A.8.15 + IMP-A.8.15 + Python-Arbeitsbuch |
| **Nicht Anwendbar** | Risiko existiert nicht aufgrund organisatorischen Kontexts | A.8.23 (Web filtering): Infrastruktur ist nur server-seitig, kein Nutzer-Webbrowsing | SoA-Begründung: „Keine Webbrowsing-Dienste für Nutzer bereitgestellt, Infrastruktur ist nur API/Backend. Kontrollziel (Zugriff auf schädliche Websites verhindern) nicht anwendbar." + Risikobewertung |
| **Alternative Kontrolle** | Standardkontrolle nicht machbar, Alternative erreicht dasselbe Ziel | A.7.4 (Physical monitoring): Infrastruktur in Colocation-Einrichtung, CCTV vom Anbieter vertraglich betrieben | SoA-Begründung: „Physische Sicherheitsüberwachung durch Colocation-Anbieter-Vertrag umgesetzt (24/7 CCTV, vierteljährliche Auditberichte). Erreicht dasselbe Ziel (unautorisierten physischen Zugang erkennen)." + Vertragsklausel-Referenz |
| **Risiko Akzeptiert** | Risiko existiert, Kontrolle nicht umgesetzt, Restrisiko von Geschäftsleitung akzeptiert | A.8.11 (Data masking): Produktionsdaten in Entwicklung verwendet (technische Einschränkung), Restrisiko mit kompensierenden Kontrollen akzeptiert | SoA-Begründung: „Data Masking nicht umgesetzt aufgrund [technischer Einschränkung]. Restrisiko von Geschäftsleitung akzeptiert [Date]. Kompensierende Kontrollen: A.5.18 (Zugriffsrechte eingeschränkt), A.8.24 (Verschlüsselung im Ruhezustand)." + Risk-Acceptance-Register-Eintrag mit Unterschrift der Geschäftsleitung |

**Auditor-Verifizierung**:

Auditor verifiziert:
- Alle 93 Kontrollen sind in SoA dokumentiert (Vollständigkeitsprüfung)
- Begründungen sind vernünftig und stimmen mit dem organisatorischen Kontext überein (Clause 4.1)
- Risikobehandlungsentscheidungen folgen dokumentiertem Prozess (Clause 6.1.3)
- Risikoakzeptanzen haben Genehmigung der Geschäftsleitung (Clause-6.1.3d-Anforderung)
- Alternative Kontrollen erreichen ISO-27001-Kontrollziele (Wirksamkeitsbewertung)

### Applicability Challenge Protocol

**Zweck**: Strukturierter Prozess zur Lösung von Meinungsverschiedenheiten bei Anwendbarkeitsfeststellungen (regulatorische Tier-Zuordnungen, Kontrollausschlüsse) zwischen Organisation und Auditor.

**Wann dieses Protokoll gilt**:

- Auditor hinterfragt Feststellung zur regulatorischen Anwendbarkeit (z. B. „Gilt GDPR angesichts Ihrer Kundenbasis wirklich?")
- Auditor beanstandet Kontrollausschluss (z. B. „Kontrolle A.8.15 als Nicht Anwendbar markiert, aber Risikobewertung zeigt Logging-Anforderung")
- Auditor ist der Meinung, dass alternative Kontrolle ISO-27001-Ziel nicht erreicht

**Protokollschritte**:

**Schritt 1: Auditor äussert Bedenken**

Auditor dokumentiert spezifische Bedenken:
- Welche Anwendbarkeitsfeststellung wird hinterfragt? (POL-00 Tier-Zuordnung, SoA-Kontrollstatus)
- Welche Nachweise deuten darauf hin, dass die Feststellung möglicherweise falsch ist?
- Welche ISO-27001-Anforderung oder welches Kontrollziel ist möglicherweise nicht erfüllt?

**Schritt 2: Organisation liefert Dokumentation**

Organisation liefert dokumentierte Begründung:

- **Für regulatorische Anwendbarkeit** (POL-00 Tier-Herausforderung):
  - Bewertung gemäss POL-00 Abschnitt 5 (Methodik eingehalten)
  - Auslöser-Bewertung (objektive Kriterien bewertet)
  - Genehmigungsnachweis (Legal/Compliance + Unterschrift der Geschäftsleitung)
  - Unterstützende Nachweise
- **Für Kontrollausschluss** (SoA „Nicht Anwendbar"):
  - Risikobewertung, die zeigt, warum Risiko nicht existiert (Clause 6.1.2)
  - SoA-Begründung (technische/operative Begründung)
  - Organisationskontextdokumentation (Clause 4.1)
- **Für alternative Kontrolle**:
  - Kontrollziel-Mapping (ISO-27001 Annex-A-Ziel → alternative Umsetzung)
  - Wirksamkeitsnachweis (alternative Kontrolle betreibt und erreicht Ziel)
  - Genehmigungsnachweis (ISB-Genehmigung des alternativen Ansatzes)

**Schritt 3: Gemeinsame Bewertung**

Organisation und Auditor bewerten:

1. **Ist die dokumentierte Begründung angesichts des organisatorischen Kontexts vernünftig?**
   - Stimmt Begründung mit ISO 27001 Clause 4.1 überein?
   - Ist Entscheidung gemäss Abschnitt 2.1 dokumentiert und genehmigt?
2. **Gibt es widersprüchliche Nachweise?**
   - Behauptet Organisation „keine EU-Daten", aber Datenschutzrichtlinie erwähnt GDPR?
   - Behauptet SoA „keine Logging-Anforderung", aber Incident-Response-Plan referenziert Logs?
3. **Erfüllt die Interpretation ISO-27001-Anforderungen?**
   - Wenn Kontrolle ausgeschlossen: Ist ISO-27001-Kontrollziel wirklich nicht anwendbar?
   - Wenn alternative Kontrolle: Erreicht sie dasselbe Sicherheitsergebnis?

**Schritt 4: Lösung**

**Ergebnis A: Auditor akzeptiert Begründung**
- Dokumentierte Begründung ist vernünftig und nachweisgestützt
- Kein Widerspruch existiert
- ISO-27001-Anforderungen sind erfüllt
- **Ergebnis**: Anwendbarkeitsfeststellung bleibt bestehen, kein Befund

**Ergebnis B: Organisation erkennt Lücke an**
- Auditor nennt spezifische ISO-27001-Klausel oder Kontrollziel, das nicht erfüllt ist
- Organisation prüft und stimmt zu, dass Feststellung falsch oder unzureichend war
- **Ergebnis**: Organisation löst Korrekturmassnahmen gemäss ISO 27001 Clause 10.2 aus:
  - Ursachenanalyse (warum wurde Anwendbarkeit falsch bestimmt?)
  - Abhilfe (POL-00 aktualisieren, SoA, fehlende Kontrolle umsetzen oder Risiko neu bewerten)
  - Verifizierung (internes Audit bestätigt Korrektur umgesetzt)
  - Zeitplan (Korrekturmassnahmenplan mit Ziel-Abschlussdatum)

**Ergebnis C: Meinungsverschiedenheit besteht fort**
- Organisation hält Begründung für fundiert, Auditor hält Bedenken für gültig
- Beide Parteien haben dokumentierte Begründung
- **Ergebnis**: Eskalation zur technischen Prüfung der Zertifizierungsstelle:
  - Organisation liefert: Dokumentierte Begründung, ISO-27001-Klausel-Ausrichtungsargument, Nachweise
  - Auditor liefert: Spezifische Bedenken, möglicherweise nicht erfüllte ISO-27001-Anforderung, alternative Interpretation
  - Zertifizierungsstelle: Prüft beide Positionen, gibt technische Entscheidung heraus
  - Organisation: Akzeptiert Entscheidung (wenn gegen Organisation → Korrekturmassnahmen gemäss Ergebnis B)

**Prinzipien**:

- **Evidenzbasiert**: Meinungsverschiedenheiten durch dokumentierte Begründung und ISO-27001-Referenz gelöst, nicht durch Autorität
- **Kollaborativ**: Ziel ist gemeinsames Verständnis der ISO-27001-Anforderungen, keine adversarielle Debatte
- **Verhältnismässig**: Kleinere Klärungen in Schritt 2 behandelt, wesentliche Lücken durch formalen Prozess eskaliert
- **Verbesserungsorientiert**: Wenn Anwendbarkeitsfeststellung wirklich falsch war, lernt und verbessert die Organisation (Clause 10.1)

**Dokumentation der Challenge-Protocol-Ausführung**:

Bei Aktivierung des Challenge Protocols:
- Im Audit-Befunde-Log dokumentieren (auch wenn in Schritt 3 ohne formalen Befund gelöst)
- Bereitgestellte Begründung und Lösungsergebnis festhalten
- Wenn Korrekturmassnahmen ausgelöst → Im Gap-Register gemäss Clause 10.2 verfolgen
- Bei jährlicher Governance-Prüfung prüfen (Abschnitt 6.1) — Muster von Herausforderungen kann systematisches Problem anzeigen

## Ausnahmehandhabung und Risikoakzeptanz

### Ausnahmeszenarien

**Definition**: Eine Ausnahme entsteht, wenn eine ISO-27001-Annex-A-Kontrolle nicht wie in der Kontrollrichtlinie (POL-A.X.XX) dokumentiert umgesetzt werden kann und einen alternativen Ansatz oder Risikoakzeptanz erfordert.

**Häufige Ausnahmeszenarien**:

| Szenario | Beschreibung | Beispiel | Lösungspfad |
|----------|-------------|---------|------------|
| **Technische Unmachbarkeit** | Kontrolle setzt Technologie/Architektur voraus, die in der Organisation nicht vorhanden ist | A.8.22 (Network segregation): Infrastruktur ist aus Designentscheidung ein einziges flaches Netzwerk | Alternative Kontrolle: Host-basierte Isolierung, Zugriffskontrollen auf Anwendungsebene |
| **Unverhältnismässige Kosten** | Kontrollkosten übersteigen Risikoreduktionsnutzen angesichts des Organisationsumfangs | A.8.16 (SIEM deployment): 3-Server-Infrastruktur, manuelle Log-Prüfung erreicht dasselbe Ziel zu geringeren Kosten | Alternative Kontrolle: Dokumentierter manueller Log-Prüfprozess mit definierter Häufigkeit |
| **Risiko bereits gemindert** | Alternative Umsetzung erreicht dasselbe ISO-27001-Kontrollziel | A.8.5 (MFA for all accounts): Service-Accounts verwenden zertifikatsbasierte Authentifizierung (funktional äquivalent zu MFA) | Alternative Kontrolle: Zertifikatsauthentifizierung als MFA-Äquivalent dokumentiert |
| **Regulatorischer Konflikt** | Kontrollumsetzung würde höher priorisierte rechtliche Anforderung verletzen (selten) | A.8.10 (Data deletion): GDPR erfordert Löschung, aber Schweizer Recht verlangt 10-jährige Aufbewahrung für Finanzunterlagen | Risikoakzeptanz: Rechtliche Verpflichtung dokumentiert überwiegt Kontrolle, Datentrennung umgesetzt um Scope zu minimieren |
| **Ressourceneinschränkung** | Organisation verfügt nicht über Kapazität zur vollständigen Umsetzung (vorübergehend) | A.6.3 (Annual security training): Schulungsprogramm entworfen, aber noch nicht allen Mitarbeitenden bereitgestellt | Aufgeschobene Umsetzung: Kontrolle für Abschluss innerhalb [Zeitraum] geplant, Übergangsmassnahmen dokumentiert |

**Ungültige Ausnahmeszenarien**:
- „Wir wussten nichts von dieser Anforderung" → Schulungslücke, keine Ausnahme
- „Es ist zu schwierig" → Ressourcenplanungsproblem, keine Ausnahme
- „Unser vorheriger Auditor hat das nicht verlangt" → Audit-Interpretationsabweichung, keine Ausnahme

### Ausnahmeprozess

**Verpflichtender Prozess** (gemäss ISO 27001 Clause 6.1.3 Risk Treatment):

Alle Ausnahmen **müssen** diesem 5-Schritte-Prozess folgen:

**Schritt 1: Grund dokumentieren**

Klare Erklärung bereitstellen:
- **Technische Erklärung**: Warum Kontrolle nicht wie geschrieben umgesetzt werden kann
- **Auswirkungsbewertung**: Welches Sicherheitsziel nicht vollständig erreicht wird
- **Kontextbegründung**: Warum diese Einschränkung existiert

Dokumentationsformat: Ausnahme-Antragsformular oder SoA-Begründungseintrag

**Schritt 2: Restrisiko bewerten** (ISO 27001 Clause 6.1.2)

Risiko ohne Kontrolle quantifizieren:
- **Wahrscheinlichkeit**: Wahrscheinlichkeit, dass Bedrohung Schwachstelle ausnutzt
- **Auswirkung**: Konsequenz, wenn Bedrohung eintritt
- **Restrisikostufe**: Kombinierte Risikoeinstufung gemäss Risikobewertungsmethodik
- **Vergleich Risikobereitschaft**: Liegt Restrisiko innerhalb akzeptabler Risikobereitschaft?

Dokumentation: Risikobewertungseintrag mit Restrisikokalkulation

**Schritt 3: Lösung vorschlagen**

Einen von drei Pfaden auswählen:

**Option A: Alternative Kontrolle**
- Andere Kontrolle umsetzen, die dasselbe ISO-27001-Kontrollziel erreicht
- Dokumentieren: Kontrollziel-Mapping + Wirksamkeitsnachweis
- Beispiel: A.7.4 (Physical monitoring) → Colocation-Anbieter-CCTV statt selbst betriebener Kameras

**Option B: Risikoakzeptanz** (ISO 27001 Clause 6.1.3d)
- Restrisiko ohne zusätzliche Minderung akzeptieren
- Erfordert: Risiko liegt innerhalb akzeptabler Risikobereitschaft UND Genehmigung der Geschäftsleitung
- Dokumentieren: Risikoakzeptanzbegründung, kompensierende Kontrollen (sofern vorhanden), Prüfzeitplan

**Option C: Aufgeschobene Umsetzung**
- Kontrolle für zukünftige Umsetzung geplant (vorübergehende Ausnahme)
- Erfordert: Umsetzungszeitplan dokumentiert, Übergangsmassnahmen definiert, periodische Prüfung

**Schritt 4: Genehmigung einholen** (gemäss Abschnitt 2.1)

| Lösung | Genehmigungskompetenz | Erforderliche Nachweise |
|----------|-------------------|------------------------|
| **Alternative Kontrolle** | ISB | Kontrollziel-Mapping, Wirksamkeitsdokumentation, technische Machbarkeitsbewertung |
| **Risikoakzeptanz** | Geschäftsleitung (GF/FL) | Risikobewertung mit Restrisiko, Akzeptanzbegründung, Dokumentation kompensierender Kontrollen |
| **Aufgeschobene Umsetzung** | ISB (Zeitplan) + Geschäftsleitung (Restrisiko während Aufschubzeitraum) | Umsetzungsplan, Übergangsmassnahmen, Ressourcenzuteilungsverpflichtung |

**Schritt 5: Im Statement of Applicability dokumentieren**

SoA aktualisieren mit:
- **Kontrollstatus**: „Alternative Control" oder „Risk Accepted" oder „Implementation Deferred"
- **Begründung**: Zusammenfassung der Schritte 1-3
- **Genehmigung**: Verweis auf Genehmigungskompetenz und Datum
- **Prüfung**: Nächstes Prüfdatum (jährliches Minimum)

Beispiel SoA-Eintrag:

```
Kontrolle A.8.22 (Network Segregation)
Status: Alternative Control
Begründung: Infrastruktur ist aus Designentscheidung ein einziges flaches Netzwerk (Cloud-native-Architektur mit Isolierung auf Anwendungsebene).
Alternative: Host-basierte Firewall-Regeln + Kubernetes-Netzwerkrichtlinien erreichen dasselbe Ziel (unautorisierten lateralen Bewegung verhindern).
Genehmigt von: ISB [Name], [Date]
Nächste Prüfung: [Date + 12 Monate]
Referenz: POL-A.8.22 Abschnitt 6 (Alternative Umsetzung), IMP-A.8.22 (Network Policy Configuration)
```

### Ausnahme-Register

**Zweck**: Zentrale Verfolgung aller Ausnahmen zur Kontrollumsetzung.

**Geführt von**: ISB (Eigentümer), bei Ausnahmenbearbeitung aktualisiert

**Inhalte**:

| Feld | Beschreibung | Beispiel |
|------|-------------|---------|
| Ausnahme-ID | Eindeutige Kennung | EXC-2025-001 |
| Kontrolle | Annex-A-Kontrollreferenz | A.8.22 (Network Segregation) |
| Grund | Warum Ausnahme erforderlich (Schritt 1) | Infrastruktur ist flaches Netzwerk aus Designentscheidung |
| Restrisiko | Risikostufe ohne Kontrolle (Schritt 2) | Mittel (Wahrscheinlichkeit: Niedrig, Auswirkung: Hoch) |
| Lösung | Alternative Kontrolle / Risikoakzeptanz / Aufgeschoben (Schritt 3) | Alternative Kontrolle: Kubernetes-Netzwerkrichtlinien |
| Genehmigt von | Kompetenz gemäss Abschnitt 2.1 (Schritt 4) | ISB [Name] |
| Genehmigungsdatum | Datum der Genehmigung | 2025-01-15 |
| Prüfdatum | Nächstes Ausnahme-Prüfdatum | 2026-01-15 (jährlich) |
| Status | Offen / Gelöst / Geschlossen | Offen (alternative Kontrolle umgesetzt) |

**Prüfzyklus**:
- **Vierteljährlich**: ISB prüft offene Ausnahmen
- **Jährlich**: Alle Ausnahmen im Management-Review geprüft (Abschnitt 6.1)

### Ausnahmenvolumen-Monitoring

**Zweck**: Ausnahmenvolumen ist eine Governance-Gesundheitsmetrik.

**Metriken**:

| Metrik | Ziel | Eskalationsschwelle | Massnahme bei Überschreitung |
|--------|------|--------------------|-----------------------------|
| **Gesamtausnahmen** | <5 % der Kontrollen (4-5 Ausnahmen) | >10 % (10+ Ausnahmen) | Prüfung durch Geschäftsleitung: Ist ISMS-Scope realistisch? |
| **Risikoakzeptanzen** | <3 % der Kontrollen (2-3) | >5 % (5+) | Neubewertung Risikobereitschaft |
| **Aufgeschobene Umsetzungen** | <2 % der Kontrollen (1-2) | >5 % oder Aufschub >180 Tage | Ressourcenzuteilungsprüfung |
| **Ausnahmen ausstehend >90 Tage** | 0 | Jede >90 Tage ohne Verlängerung | Eskalation zur Geschäftsleitung |

**Prüfhäufigkeit**:
- **Vierteljährlich**: ISB berichtet Ausnahmenmetriken
- **Jährlich**: Trendanalyse im Management-Review

## Compliance-Kriterien-Änderungskontrolle

### Änderungsauslöser

**Externe Änderungsauslöser**:

| Auslöserkategorie | Beschreibung | Beispiele | Erkennungsmethode |
|------------------|-------------|---------|------------------|
| **Regulatorische Änderungen** | Neue Gesetze oder offizielle Leitlinien | GDPR-Durchführungsakte, ISO-27001-Änderungen, nDSG-Leitlinienaktualisierungen | POL-00 vierteljährliches Monitoring, Rechtsberatungsbenachrichtigungen |
| **Standard-Revisionen** | ISO 27001 oder verwandte Standards aktualisiert | ISO 27001:2022 → mögliche zukünftige ISO 27001:202X | ISO-Publikationsmonitoring, Zertifizierungsstellen-Benachrichtigungen |
| **Vertragsänderungen** | Kundenverträge fügen neue Sicherheitsanforderungen hinzu | Neuer Kunde erfordert PCI-DSS-Scope-Erweiterung | Vertragsprüfungsprozess |
| **Bedrohungslandschaft** | Neue Angriffsmuster erfordern Kontrollaktualisierungen | Ransomware zielt auf Backups → A.8.13 erfordert Offline/unveränderliche Kopien | Bedrohungsintelligenz-Monitoring (A.5.7) |
| **Technologieänderungen** | Infrastruktur- oder Architekturverschiebungen | Cloud-Migration → A.5.23 jetzt anwendbar | IT-Änderungsmanagementprozess |

**Interne Änderungsauslöser**:

| Auslöserkategorie | Beschreibung | Beispiele | Erkennungsmethode |
|------------------|-------------|---------|------------------|
| **Audit-Befunde** | Externer Auditor identifiziert Kontrollücke | Stage-2-Befund: „Logging-Aufbewahrung unzureichend für A.8.15-Ziel" | Audit-Befunde-Log (Clause 10.2) |
| **Interne Audit-Entdeckungen** | Internes Audit identifiziert Nichtkonformität | Internes Audit: „Ausnahmegenehmigung ohne Unterschrift der Geschäftsleitung" | Interne Auditberichte |
| **Sicherheitsvorfälle** | Incident-Response offenbart Kontrollschwäche | Vorfall: Phishing-Angriff erfolgreich → A.6.3-Schulungshäufigkeit erhöht | Incident-Response-Prozess (A.5.24-28) |
| **Management-Review** | Clause-9.3-Review identifiziert strategische Verbesserung | Management-Review: „Höheres Restrisiko für Kontrollen mit geringer Auswirkung akzeptieren" | Management-Review-Protokolle |
| **Fortlaufende Verbesserung** | Proaktive Identifikation von Effizienzgewinnen | ISB-Vorschlag: „A.8.15-Log-Analyse mit SIEM automatisieren" | ISMS-Review-Meetings |

### Änderungsbewertungs- und -umsetzungsprozess

**Verpflichtender 6-Schritte-Prozess**:

**Schritt 1: Änderung identifiziert**
- Auslöserereignis erkannt gemäss Abschnitt-5.1-Quellen
- **Verantwortlich**: ISB (koordiniert Bewertung), Legal/Compliance (regulatorische Änderungen)
- **Ausgabe**: Eintrag im Change Trigger Log

**Schritt 2: Auswirkung bewertet**

Änderungsumfang und -implikationen bewerten:
1. Welche Richtlinien/Kontrollen sind betroffen?
2. Welche Compliance-Lücke existiert? (aktueller Zustand vs. geforderter Zustand)
3. Welche Abhilfe ist erforderlich?
4. Welches Risiko besteht während des Übergangs?

**Schritt 3: Änderungsvorschlag dokumentiert**

Formalisierung der Änderungsempfehlung mit:
1. Begründung (warum Änderung notwendig)
2. Betroffene Kontrollen (Liste der Annex-A-Kontrollen)
3. Umsetzungsplan (technische Aufgaben, Dokumentationsaufgaben, Zeitplan, Ressourcen)
4. Risiko während Übergang
5. Verifizierungsplan

**Schritt 4: Genehmigung eingeholt** (gemäss Abschnitt 2.1)

| Änderungstyp | Genehmigungskompetenz | Genehmigungskriterien |
|-------------|-------------------|--------------------|
| **Technische Änderungen** | ISB | Technisch fundiert, Ressourcen verfügbar |
| **Regulatorische Änderungen** | ISB + Legal/Compliance (gemeinsam) | Regulatorische Interpretation korrekt |
| **Strategische Änderungen** | Geschäftsleitung | Ressourcenzuteilung genehmigt, Risikobereitschafts-Ausrichtung bestätigt |
| **Notfalländerungen** | ISB (sofort) + Geschäftsleitung (nachträgliche Genehmigung innerhalb 7 Tage) | Dringlichkeit begründet |

**Schritt 5: Umsetzung ausgeführt**

- Richtlinienaktualisierungen (gemäss ISO 27001 Clause 7.5.3)
- Kontrollen-Neubewertung
- Nachweise-Regeneration
- Change-Log-Aktualisierung

**Schritt 6: Verifizierung abgeschlossen**

- Interne Audit-Verifizierung (ISO 27001 Clause 9.2)
- Lückenschliessung
- Management-Review (ISO 27001 Clause 9.3)

### Versionskontrolle und Änderungsverfolgung

**Dokumentversionsformat**: `v[Major].[Minor]`

| Änderungstyp | Versionserhöhung | Beispiel | Auslöser |
|-------------|-----------------|---------|---------|
| **Hauptversion** | Hauptnummer erhöhen, Nebennummer auf 0 zurücksetzen | v1.3 → v2.0 | Wesentliche Anforderungsänderung |
| **Nebenversion** | Nebennummer erhöhen | v1.3 → v1.4 | Klarstellung oder nicht wesentliche Änderung |

**Zentrales ISMS-Änderungslog**:

| Feld | Beschreibung | Beispiel |
|------|-------------|---------|
| Änderungs-ID | Eindeutige Kennung | CHG-[JAHR]-[SEQ] |
| Änderungsdatum | Datum der Änderungsumsetzung | [Date] |
| Auslöser | Was Änderung auslöste | GDPR-Leitlinienaktualisierung |
| Betroffene Richtlinien/Kontrollen | Welche Dokumente aktualisiert | POL-A.8.24 v1.5 → v2.0 |
| Änderungszusammenfassung | Kurzbeschreibung | Verschlüsselungsminimum von AES-128 auf AES-256 aktualisiert |
| Begründung | Warum Änderung notwendig war | GDPR-Leitlinie erfordert jetzt AES-256 |
| Genehmigung | Kompetenz (gemäss Abschnitt 2.1) | ISB + Legal/Compliance |
| Verifizierungsstatus | Änderung als wirksam verifiziert? | Verifiziert — internes Audit bestätigte AES-256-Einsatz |

### Neubewertungs-Tracking

**Neubewertungsanforderungen**:

| Feld | Beschreibung | Beispiel |
|------|-------------|---------|
| Lücken-ID | Verknüpft mit Änderungs-ID | GAP-[JAHR]-[SEQ] |
| Kontrolle | Betroffene Annex-A-Kontrolle | A.8.24 |
| Lückenbeschreibung | Was neue Anforderung nicht erfüllt | Aktuelle Umsetzung verwendet AES-128, neue Anforderung AES-256 |
| Eigentümer | Verantwortlich für Abhilfe | Infrastruktur-Teamleiter |
| Zielabschluss | Abhilfefrist | [Date + 90 Tage] |
| Status | Aktueller Zustand | In Bearbeitung (60 % abgeschlossen) |
| Verifizierung | Wie Abschluss bestätigt wird | Internes Audit + Python-Arbeitsbuch-Regeneration |

**Neubewertungs-Abschlussmetriken**:

| Metrik | Ziel | Eskalationsschwelle |
|--------|------|---------------------|
| Abschlussrate | >95 % innerhalb 90 Tage | <80 % → Prüfung durch Geschäftsleitung |
| Überfällige Neubewertungen | 0 Einträge >90 Tage | Jeder Eintrag >90 Tage ohne Verlängerung → Eskalation |
| Fehlgeschlagene Verifizierungen | <5 % | >10 % → Prozessprüfung |

## Governance-Wirksamkeits-Monitoring

### Jährliche Governance-Prüfung

**Häufigkeit**: Jährlich (ausgerichtet an ISO 27001 Clause 9.3 Management Review)

**Zeitplan**: Q4 jedes Jahres

**Teilnehmende**:
- Geschäftsleitung (GF/FL — Entscheidungskompetenz)
- ISB (Governance-Eigentümer, präsentiert Ergebnisse)
- Legal/Compliance Officer (regulatorische Bewertung)
- Interne Revision (Prozessverifizierungsperspektive)
- Repräsentative Kontroll-Eigentümer (operative Einsicht)

**Prüfthemen**:

**1. Kompetenzgrenzen (Abschnitt 2.1)**
- Sind Rollen und Verantwortlichkeiten klar verstanden?
- Funktionieren Eskalationsprozesse?
- Erfordern Streitigkeiten Prozessverbesserung?
- Wird Kompetenz aufrechterhalten?

**2. Anwendbarkeits-Framework (Abschnitt 3)**
- Ist POL-00 Tier-1/2/3-Framework wirksam?
- Werden Auslöser bedingter Verordnungen überwacht?
- Sind SoA-Begründungen ausreichend?

**3. Ausnahmehandhabung (Abschnitt 4)**
- Wie viele Ausnahmen im vergangenen Jahr bearbeitet?
- Sind Risikoakzeptanzen angemessen?
- Wird Ausnahmeprozess eingehalten?

**4. Änderungsmanagement (Abschnitt 5)**
- Wie viele Compliance-Kriterien-Änderungen im vergangenen Jahr?
- Wie hoch ist die Neubewertungs-Abschlussrate?
- Sind Änderungen proaktiv oder reaktiv?

**5. Auditor-Feedback**
- Was haben externe Auditoren zu Governance kommentiert?
- Wurden Interpretationen herausgefordert?

**6. Governance-Effizienz**
- Sind Governance-Prozesse effizient?
- Gibt es bürokratische Engpässe?

**Jährliche Governance-Prüfungs-Ausgaben**:

1. **Governance-Gesundheitsbericht**: Dokument mit obigen 6 Themen
2. **Massnahmen zur fortlaufenden Verbesserung**: Spezifische Massnahmen zur Verbesserung
3. **Richtlinienaktualisierungen**: Falls Lücken identifiziert → POL-GOVERNANCE aktualisieren
4. **Management-Review-Protokoll**: Governance-Prüfung in Clause-9.3-Review einbezogen

### Lessons Learned Register

**Zweck**: Verbesserungen aus Governance-Prozessausführung erfassen (ISO 27001 Clause 10.1)

**Geführt von**: ISB (vierteljährlich oder bei identifizierter Lektion aktualisiert)

**Register-Inhalte**:

| Datum | Ereignis | Lektion | Massnahme | Status | Verifiziert |
|-------|---------|---------|-----------|--------|------------|
| *Q1 [Jahr]* | *Auditor hinterfragte A.8.15-Interpretation* | *Explizitere Begründung in SoA — Auditor benötigte spezifisches ISO-27001-Kontrollziel-Mapping* | *SoA-Vorlage erweitert: verpflichtende „ISO-27001-Objective-Mapping"-Feld für alle „Nicht Anwendbar"-Kontrollen* | *Umgesetzt* | *Internes Audit Q2 [Jahr] bestätigte SoA-Aktualisierungen* |
| *Q2 [Jahr]* | *Ausnahmegenehmigung 30 Tage verzögert* | *Stellvertretende Genehmigungskompetenz für dringende Ausnahmen etablieren* | *Abschnitt 4.2 aktualisiert: FL kann Risikoakzeptanzen in Abwesenheit des GF genehmigen* | *Umgesetzt* | *Richtlinie aktualisiert, Genehmigungsworkflow getestet Q3 [Jahr]* |

## Integration mit ISMS-Prozessen

### Risikobewertung und -behandlung (Clause 6)

- **Clause 6.1.2**: Risikobewertungsmethodik informiert Kontrollauswahlentscheidungen (dokumentiert in SoA)
- **Clause 6.1.3**: Risk Treatment Plan dokumentiert Kontrollumsetzungsansatz, alternative Kontrollen und Risikoakzeptanzen
- **Governance-Kompetenz** (Abschnitt 2.1): ISB schlägt Risikobehandlung vor, Geschäftsleitung genehmigt Risikoakzeptanz

### Internes Audit (Clause 9.2)

- **Internes Auditprogramm** umfasst Verifizierung der Governance-Prozess-Compliance
- **Vor-Audit-Verifizierung**: Interne Audits vor externen Audits verifizieren Governance-Dokumentation
- **Audit-Scope-Anpassung**: Bei Compliance-Kriterien-Änderungen werden betroffene Kontrollen in nächsten internen Audit-Scope aufgenommen

### Management-Review (Clause 9.3)

**Management-Review-Eingaben** (Clause 9.3.2):
- Änderungs-Log-Zusammenfassung (Abschnitt 5.3)
- Governance-bezogene Audit-Befunde (Abschnitt 6.1 Thema 5)
- Lektionen (Abschnitt 6.2), identifizierte Governance-Prozessverbesserungen

**Management-Review-Ausgaben** (Clause 9.3.3):
- Genehmigung von Risikoakzeptanzen
- Genehmigung strategischer Änderungen
- Ressourcenzuteilung für Abhilfe

### Nichtkonformität und Korrekturmassnahmen (Clause 10.2)

**Nichtkonformitäts-Auslöser** — Governance-bezogen:
- Governance-Prozess nicht eingehalten
- Audit-Befund offenbart Interpretationslücke
- Vorfall offenbart Kontrollschwäche

**Korrekturmassnahmen-Prozess**:
- Ursachenanalyse: Ist dies ein Governance-Prozessversagen oder ein isolierter Vorfall?
- Abhilfe: Richtlinie gemäss Abschnitt 5.2 aktualisieren oder Prozessausführung verbessern
- Verifizierung: Internes Audit bestätigt Korrekturmassnahme wirksam

## Nachweise für diese Richtlinie

### Stage-1-Nachweise (Dokumentationsprüfung)

- Dieses Richtliniendokument (ISMS-POL-01)
- Genehmigungsunterschriften von ISB, Legal/Compliance, Geschäftsleitung
- Governance-Struktur dokumentiert (Abschnitt 2.1 Authority-Boundaries-Tabelle)
- Kompetenzanforderungen definiert (Abschnitt 2.3)
- Ausnahmehandhabungsprozess dokumentiert (Abschnitt 4.2 5-Schritte-Prozess)
- Änderungsmanagementprozess dokumentiert (Abschnitt 5.2 6-Schritte-Prozess)
- Jährlicher Prüfungsprozess definiert (Abschnitt 6.1)

### Stage-2-Nachweise (Operative Wirksamkeit)

**Kompetenzgrenzen-Nachweise** (Abschnitt 2):
- Kompetenzverifizierungsunterlagen (Abschnitt 2.3)
- Entscheidungsgenehmigungsnachweise (Unterschriften auf POL-Dokumenten)

**Anwendbarkeitskompetenz-Nachweise** (Abschnitt 3):
- POL-00 vierteljährliche Monitoring-Protokolle (4 Quartale)
- SoA mit Begründungen für alle 93 Kontrollen

**Ausnahmehandhabungs-Nachweise** (Abschnitt 4):
- Ausnahme-Register (Abschnitt 4.3) mit Einträgen
- Risk Acceptance Register mit Unterschriften der Geschäftsleitung

**Änderungsmanagement-Nachweise** (Abschnitt 5):
- ISMS-Änderungslog (Abschnitt 5.3)
- Neubewertungs-Tracking (Abschnitt 5.4 Gap-Register)

**Governance-Wirksamkeits-Nachweise** (Abschnitt 6):
- Jährliche Governance-Prüfungs-Meeting-Protokolle
- Lessons-Learned-Register mit Einträgen

### Assessment-Arbeitsbuch

**Governance Compliance Assessment Workbook**: ISMS-CHK-POL-01

**Domain 1: Authority Boundaries** (Abschnitt 2)
- GOV-01: Technische Kontrollumsetzungen von ISB genehmigt
- GOV-02: Regulatorische Anwendbarkeitsfeststellungen von Legal/Compliance genehmigt
- GOV-03: Risikoakzeptanzentscheidungen von Geschäftsleitung genehmigt
- GOV-04: Kompetenzanforderungen verifiziert

**Domain 2: Applicability Decisions** (Abschnitt 3)
- GOV-05: POL-00 vierteljährliches Monitoring abgeschlossen
- GOV-06: Ausgelöste Bewertungen dokumentiert
- GOV-07: SoA-Begründungen vollständig (alle 93 Kontrollen)
- GOV-08: Challenge Protocol bei Aktivierung eingehalten

**Domain 3: Exception Handling** (Abschnitt 4)
- GOV-09: Ausnahmen folgen 5-Schritte-Prozess
- GOV-10: Restrisiko für alle Ausnahmen bewertet
- GOV-11: Risikoakzeptanzen von Geschäftsleitung genehmigt
- GOV-12: Ausnahmenvolumen innerhalb Zielen

**Domain 4: Change Management** (Abschnitt 5)
- GOV-13: Compliance-Kriterien-Änderungen dokumentiert
- GOV-14: Änderungen folgen 6-Schritte-Prozess
- GOV-15: Neubewertungen innerhalb 90 Tage abgeschlossen
- GOV-16: Änderungen durch internes Audit verifiziert

**Domain 5: Governance Review** (Abschnitt 6)
- GOV-17: Jährliche Governance-Prüfung abgeschlossen
- GOV-18: Prüfung deckt alle erforderlichen Themen ab
- GOV-19: Massnahmen zur fortlaufenden Verbesserung dokumentiert
- GOV-20: Lessons-Learned-Register geführt

**Bewertungshäufigkeit**: Vierteljährlich (Q1, Q2, Q3, Q4)

## Audit-Vorbereitung und Dokumentenpaket

### Für Auditoren bereitgestellte Dokumente

**Stage-1-Audit** (Dokumentationsprüfung):

- ISMS-POL-01 (diese Richtlinie)
- ISMS-POL-00 (Regulatory Applicability Framework)
- Statement of Applicability (SoA)
- Risk Treatment Plan (Clause 6.1.3)
- Risk Acceptance Register (Clause 6.1.3d)
- Organisationskontextdokument (Clause 4.1/4.2)
- ISMS-Änderungslog (Abschnitt 5.3)

**Stage-2-Audit** (Umsetzungsverifizierung):

- Governance Compliance Assessment Workbook (ISMS-CHK-POL-01)
- Ausnahme-Register (Abschnitt 4.3)
- POL-00 vierteljährliche Monitoring-Protokolle
- Ausgelöste Bewertungsunterlagen
- Interne Auditberichte (Clause 9.2)
- Management-Review-Protokolle (Clause 9.3)
- Jährlicher Governance-Prüfungsbericht (Abschnitt 6.1)
- Lessons-Learned-Register (Abschnitt 6.2)
- Kompetenzverifizierungsunterlagen (Abschnitt 2.3)

### Audit-Koordination

**Vor-Audit-Koordination** (2 Wochen vor Audit):

1. **Dokumentenpaket-Zusammenstellung**: Dokumente gemäss Abschnitt 9.1 sammeln
2. **ISMS-Struktur-Briefing**: Auditor mit Governance-Framework-Überblick versorgen
3. **Nachweis-Standortleitfaden**: Auditor informieren, wo Nachweise aufbewahrt werden
4. **Ansprechpartner**: ISB oder Stellvertreter als primären Auditor-Kontakt benennen

**Ton**: Kollaborativ und informativ

---

## Schlussaussage

Diese Richtlinie legt fest, **wo fachliches Urteilsvermögen** im ISMS der Organisation ausgeübt wird, und ermöglicht:

**Objektive Audit-Verifizierung**: Compliance wird gegen dokumentierte organisatorische Entscheidungen bewertet, nicht gegen Auditorenermessen.

**Klare Entscheidungskompetenz**: Rollen (ISB, Legal/Compliance, Geschäftsleitung) haben explizite Kompetenzgrenzen mit Qualifikationsanforderungen.

**Kontrollierte Weiterentwicklung**: Compliance-Kriterien ändern sich durch dokumentierten 6-Schritte-Prozess mit Neubewertungs-Tracking, Verifizierung und Genehmigung.

**Kollaborative Audit-Beziehung**: Auditorenurteil konzentriert sich auf Verifizierung der Qualität des organisatorischen Urteils, nicht auf das Ersetzen organisatorischer Entscheidungen.

---

**Was diese Richtlinie erreicht:**

✅ **Klarheit**: Compliance-Kriterien sind explizit (POL-00, SoA, Risk Treatment Plan, dokumentierte Richtlinien)
✅ **Konsistenz**: Änderungen sind kontrolliert (Abschnitt 5, Versionskontrolle, Neubewertungs-Tracking)
✅ **Verteidigbarkeit**: Entscheidungen sind dokumentiert und begründet (Kompetenz-Unterschriften, Risikobewertungen)
✅ **Auditierbarkeit**: Nachweise demonstrieren, dass Governance-Prozesse eingehalten werden
✅ **Verbesserung**: Lektionen und Governance-Reviews ermöglichen fortlaufende Verbesserung (Clause 10.1)

---

**Das Paradigmenwechsel:**

**Traditionelles ISMS**: Fachliches Urteilsvermögen während des Audits ausgeübt (Auditor interpretiert Anforderungen, Organisation verteidigt im Nachhinein)

**Dieses ISMS**: Fachliches Urteilsvermögen während des Modell-Designs ausgeübt (Organisation dokumentiert Interpretation, Auditor verifiziert Qualität und ISO-27001-Ausrichtung)

**Ergebnis**: Audit wird zur objektiven Verifizierung des dokumentierten Designs, kein subjektiver Interpretationswettbewerb.

---

**Governance-Review**: Diese Richtlinie selbst unterliegt fortlaufender Verbesserung. Jährliche Governance-Prüfung (Abschnitt 6.1) bewertet, ob Governance-Prozesse wirksam sind. Falls Governance-Lücken identifiziert, wird diese Richtlinie gemäss Abschnitt 5.2 Änderungskontrollprozess aktualisiert.

---

**Genehmigung und Pflege**:

Diese Richtlinie ist von der Geschäftsleitung genehmigt und wird vom ISB gepflegt. Prüfzyklus ist jährlich oder bei wesentlichen ISMS-Änderungen, die Governance-Prozessaktualisierungen erfordern.

---

**ENDE VON ISMS-POL-01**

<!-- QA_VERIFIED: 2026-03-28 -->
