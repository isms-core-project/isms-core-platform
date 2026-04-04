# ISMS-INS-POL-01 — Implementierungsleitfaden
## POL-01: ISMS-Governance- und Entscheidungsrahmen

**Datum:** 2026-02-17
**Zweck:** Praktischer Implementierungsleitfaden für Organisationen, die POL-01 einführen
**Zielgruppe:** ISB, Implementierungsleitung, Berater

---

## 1. Was POL-01 tatsächlich bewirkt (Klartextbeschreibung)

POL-01 existiert aus einem einzigen Grund: **um Scope-Creep durch Auditoren zu unterbinden.**

Die ISO-27001-Zertifizierung umfasst zwei Stufen fachlichen Ermessens:
1. **Ihr Ermessen** — ISO 27001 für Ihren Kontext interpretieren, Kontrollen auswählen, Nachweise definieren
2. **Das Ermessen des Auditors** — verifizieren, ob Ihre Interpretation vernünftig und umgesetzt ist

Ohne POL-01 ist die Grenze zwischen Stage 1 und Stage 2 unscharf. Ein akribischer Auditor kann Ihre Kontrolldesign-Entscheidungen während des Audits anfechten und so eine Verifikationsübung in eine Neuverhandlung verwandeln. POL-01 überführt alle Ihre fachlichen Ermessensentscheidungen in dokumentierte, unterzeichnete, pre-audit-Artefakte. Wenn der Auditor eintrifft, hat jede Entscheidung eine benannte Autorität, einen Kompetenznachweis und eine Genehmigungsunterschrift. Ihre Aufgabe schrumpft auf das Binäre: Haben Sie Ihren dokumentierten Prozess befolgt? Ja oder Nein.

**Die Komplexität von POL-01 ist das Produkt. Eine einfachere Governance-Richtlinie gibt Auditoren mehr Spielraum.**

---

## 2. Was in anderen Richtlinien geändert werden muss

### 2.1 Erforderliche Änderungen (Diese vornehmen)

Nur 4 Richtlinien benötigen substanzielle Aktualisierungen. Diese lohnen sich, weil sie Querverweise herstellen, die Auditoren bei der Überprüfung des Governance-Rahmens erwarten werden.

#### POL-00 — Regulatorischer Anwendbarkeitsrahmen
**Wo:** Abschnitt 7 (Pflege & Aktualisierungen)
**Was hinzufügen:** Einen Unterabschnitt, der erklärt, dass über die POL-00-Überwachung erkannte regulatorische Änderungen den POL-01-Änderungsprozess (Abschnitt 5.2) auslösen. Auditoren werden nach dieser Verbindung suchen — ohne sie wirken POL-00-Überwachung und POL-01-Änderungskontrolle losgelöst voneinander.

```markdown
### Integration Änderungsmanagement

Durch POL-00-Überwachung erkannte regulatorische Änderungen lösen den Compliance-
Kriterien-Änderungsprozess gemäß ISMS-POL-01 (Abschnitt 5.2) aus. Änderungs-
Folgenabschätzung, Genehmigungsbefugnis und Neubewertungs-Tracking folgen dem
6-Schritte-Prozess gemäß POL-01 Abschnitt 5.2. Betroffene Kontrollen werden
innerhalb von 90 Tagen gemäß POL-01 Abschnitt 5.4 neu bewertet.
```

#### POL-A.5.1 — Richtlinien für Informationssicherheit
**Wo:** Abschnitt 1.3 oder neuer Abschnitt 1.4
**Was hinzufügen:** Eine Governance-Grenzen-Referenz. Dies ist die übergeordnete Richtlinie für alle Annex-A-Kontrollen — wenn hier festgehalten wird, dass Entscheidungsbefugnis, Ausnahmen und Änderungskontrolle durch POL-01 geregelt werden, muss dies nirgendwo sonst hinzugefügt werden.

```markdown
### Governance-Rahmen

Die Entscheidungsbefugnis für die ISMS-Compliance-Interpretation, den Umgang mit
Kontrollausnahmen und die Änderungskontrolle von Compliance-Kriterien wird durch
ISMS-POL-01 (ISMS-Governance- und Entscheidungsrahmen) geregelt. Alle Annex-A-
Kontrollrichtlinien operieren innerhalb der in POL-01 definierten
Autoritätsgrenzen und Prozesse.
```

#### POL-A.5.31 — Gesetzliche, regulatorische und vertragliche Anforderungen
**Wo:** Abschnitt Compliance-Überwachung
**Was hinzufügen:** Governance-Autoritätsreferenz, die Compliance-Überwachung (POL-00) mit Ausnahmenhandhabung und Änderungskontrolle (POL-01) verknüpft. Auditoren, die A.5.31 prüfen, werden sehen wollen, wie regulatorische Änderungen in den Governance-Prozess einfließen.

#### POL-A.5.35-36 — Compliance-Überprüfung / Unabhängige Überprüfung
**Wo:** Abschnitt Überprüfungsprozess
**Was hinzufügen:** Verweis auf POL-01 Abschnitt 6.1 (jährliche Governance-Überprüfung) als Teil des Geltungsbereichs der unabhängigen Prüfung. Damit wird sichergestellt, dass die Governance-Wirksamkeit explizit im Prüfungsbereich liegt.

---

### 2.2 Diese überspringen (nicht sinnvoll)

**POL-01 zu Verwandte Dokumente in allen 53 Annex-A-Richtlinien hinzufügen.**

Der ISMS-Copilot hat dies als Phase 3 vorgeschlagen. Nicht tun. Begründung:

- Die Beziehung zwischen POL-01 und allen Kontrollrichtlinien wird durch die ISMS-Struktur, das SoA und durch POL-A.5.1 (die übergeordnete Richtlinie) hergestellt
- Auditoren verifizieren Governance nicht durch Überprüfung von 53 „Verwandte Dokumente"-Listen
- 53 Richtlinienbearbeitungen × Pflegeaufwand = dauerhafter Wartungsschulden, wann immer POL-01 sich ändert
- Eine Zeile in jeder Richtlinie hinzufügen erzeugt die Illusion von Integration ohne die Substanz

**Wenn ein Auditor fragt, warum POL-01 nicht in den Verwandten Dokumenten einer bestimmten Kontrollrichtlinie steht**, auf POL-A.5.1 Abschnitt 1.X (den oben hinzugefügten Governance-Verweis) hinweisen. Das genügt.

---

## 3. Operative Anlaufphase — Was vor Stage-2-Audit vorhanden sein muss

Hier werden die meisten Organisationen erwischt. POL-01 definiert Prozesse. Prozesse benötigen Nachweise. Nachfolgend das minimale realisierbare Nachweisset für ein erstes Stage-2-Audit.

### 3.1 Muss vorhanden sein (Auditor wird fragen)

| Nachweis | Was es ist | Wer es pflegt | Häufigkeit |
|----------|-----------|---------------|-----------|
| **POL-00 Überwachungsprotokolle** | Unterzeichneter Nachweis, dass das regulatorische Umfeld überprüft wurde | Rechts-/Compliance + ISB | Quartalsweise (4 pro Jahr) |
| **Ausnahmenregister** | Protokoll der Kontrollen, die nicht wie vorgesehen umgesetzt werden konnten, mit dokumentiertem 5-Schritte-Prozess | ISB | Bei Auftreten von Ausnahmen |
| **Risikoakzeptanzregister** | Geschäftsleitung-Unterschriften für akzeptierte Risiken | Geschäftsleitung | Bei Entscheidungen |
| **ISMS-Änderungsprotokoll** | Nachweis von Compliance-Kriterien-Änderungen mit 6-Schritte-Prozess | ISB | Bei Änderungen |
| **Kompetenzunterlagen** | Zertifizierungen/Erfahrungsnachweise für ISB, Rechts-/Compliance, DSB, Geschäftsleitung | HR / ISB | Bei Rollenbesetzung |
| **Jahres-Governance-Überprüfungsprotokoll** | Besprechungsprotokoll, das zeigt, dass 6 Themen mit Teilnahme der Geschäftsleitung behandelt wurden | ISB | Jährlich |

### 3.2 Wünschenswert (Stärkt die Position)

| Nachweis | Was es ist |
|----------|-----------|
| Lückenregister | Verfolgung von Neubewertungen nach Änderungen (POL-01 Abschnitt 5.4) |
| Lessons-Learned-Register | Governance-Verbesserungsmaßnahmen (POL-01 Abschnitt 6.2) |
| Ausgefülltes ISMS-CHK-POL-01-Arbeitsbuch | Quartalsweise Governance-Selbstbewertung (20 Anforderungen, GOV-01–GOV-20) |

### 3.3 Was auf das Überwachungsaudit verschoben werden kann

- Vollständige vierteljährliche Bewertungshistorie mit ISMS-CHK-POL-01 (4 Quartale)
- Vollständiges Lessons-Learned-Register mit mehreren Einträgen
- Detailliertes Lückenregister mit >95% Abschlussverfolgung

Beim **erstmaligen Zertifizierungsaudit** akzeptieren Auditoren, dass Prozesse neu sind. Was sie nicht akzeptieren können, ist das vollständige Fehlen von Nachweisen. Selbst ein abgeschlossenes Quartal Überwachungsprotokolle + ein Ausnahmenregister mit 0–3 Einträgen ist besser als nichts.

---

## 4. Implementierungshinweise

### 4.1 Das Quartalsüberwachungsprotokoll ist die wichtigste Voraussetzung

Alles in POL-01 ist letztlich mit der POL-00-Quartalsüberwachung verknüpft. Wenn das Quartalsprotokoll vorhanden und von Rechts-/Compliance + ISB unterzeichnet ist, demonstriert es:
- GOV-05 (Domäne Anwendbarkeitsentscheidungen) ✅
- Dass die Organisation aktiv das regulatorische Bewusstsein aufrechterhält ✅
- Dass POL-01 Abschnitt 3 operativ aktiv ist ✅

Eine einfache Vorlage für das Überwachungsprotokoll erstellen und quartalsweise ausfüllen, auch wenn die Antwort lautet „keine Änderungen festgestellt." Die Unterschrift ist entscheidend.

### 4.2 Das Ausnahmenregister ist Ihr Sicherheitsnetz

Der 5-Schritte-Ausnahmeprozess (POL-01 Abschnitt 4.2) ist keine Bürokratie — er ist Ihre dokumentierte Begründung für jede Kontrolle, die Sie nicht oder nicht vollständig umsetzen konnten oder wollten. Ohne ihn kann ein Auditor jede Lücke als Nichtkonformität einstufen. Mit ihm wird dieselbe Lücke zu einer dokumentierten, risikobewerteten, management-genehmigten Ausnahme. Das ist der Unterschied zwischen einer schwerwiegenden Nichtkonformität und einer akzeptablen Risikoakzeptanz.

Register sofort anlegen, auch wenn es leer ist. Ein leeres Register mit der richtigen Struktur ist besser als kein Register.

### 4.3 Unterschriften der Geschäftsleitung sind nicht verhandelbar

ISO 27001 Klausel 6.1.3d fordert ausdrücklich die Genehmigung der Geschäftsleitung für Risikoakzeptanzentscheidungen. POL-01 formalisiert dies durch das Risikoakzeptanzregister. Wenn die Geschäftsleitung das Register nicht unterzeichnen kann, kann keine Risikobehandlung abgeschlossen werden, und es kann keine Zertifizierung erlangt werden. Dies ist der einzige Prozess ohne Workaround — holen Sie die Unterschriften.

### 4.4 Das Änderungsprotokoll ist leicht zu vergessen

Der 6-Schritte-Änderungsprozess (POL-01 Abschnitt 5.2) wird nur aktiviert, wenn Compliance-Kriterien sich ändern — was nicht häufig vorkommen mag. Das Risiko besteht darin, eine Änderung nicht zu protokollieren, wenn sie doch eintritt (neue Vorschrift, Audit-Feedback, erhebliche Bedrohung). Den ISB als Protokollverantwortlichen bestimmen und „Änderungsprotokoll prüfen" als festen Tagesordnungspunkt bei der jährlichen Governance-Überprüfung aufnehmen.

### 4.5 Governance-Überprüfung nicht überentwickeln

POL-01 Abschnitt 6.1 schreibt eine jährliche Governance-Überprüfung vor, die 6 Themen abdeckt. Dies muss keine förmliche Vorstandssitzung sein. Eine dokumentierte zweistündige Sitzung mit dem ISB und einem Geschäftsleitungsvertreter, mit einem Protokoll, das die 6 Themen abdeckt, erfüllt die Anforderung. Ein einseitiges Protokoll ist besser als ein aufwendiger Prozess, der nie stattfindet.

---

## 5. Minimale realisierbare Implementierungssequenz

Für eine Organisation, die POL-01 von Grund auf implementiert, in Reihenfolge:

1. **POL-01 genehmigen und unterzeichnen** — ISB entwirft, Rechts-/Compliance prüft, Geschäftsleitung genehmigt
2. **Kompetenzunterlagen erstellen** — dokumentieren, dass ISB, Rechts-/Compliance, DSB die Kriterien aus Abschnitt 2.3 erfüllen
3. **Ausnahmenregister anlegen** — nur Vorlage, auch wenn leer
4. **Risikoakzeptanzregister anlegen** — nur Vorlage, auch wenn leer
5. **ISMS-Änderungsprotokoll anlegen** — nur Vorlage, auch wenn leer
6. **Erstes POL-00-Quartalsüberwachungsprotokoll erstellen** — auch ein Quartal genügt
7. **POL-00 Abschnitt 7 aktualisieren** — Verweis auf Änderungsmanagement-Integration hinzufügen
8. **POL-A.5.1 aktualisieren** — Governance-Rahmen-Verweis hinzufügen
9. **Jährliche Governance-Überprüfung planen** — jetzt in den Kalender eintragen
10. **ISMS-CHK-POL-01-Arbeitsbuch generieren** — Skript ausführen, einen Bewertungszyklus abschließen

Schritte 1–6 sind Voraussetzungen für Stage-2-Audit. Schritte 7–10 stärken die Position.

---

## 6. Dateispeicherorte

| Dokument | Speicherort |
|----------|-------------|
| POL-01 Richtlinie | `POL/ISMS-POL-01 - ISMS Governance and Decision-Making Framework.md` |
| Bewertungsarbeitsbuch-Generator | `SCR/ISMS-SCR-CHK-POL-01.py` |
| Generiertes Bewertungsarbeitsbuch | `WKBK/ISMS-CHK-POL-01_...xlsx` |
| Dieser Implementierungsleitfaden | `INS/de/ISMS-INS-POL-01-Implementierungsleitfaden-DE.md` |

---

<!-- ISMS-CORE:INS:ISMS-INS-POL-01-DE:framework:INS:01 -->

<!-- QA_VERIFIED: 2026-03-28 -->
