<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.8.35-DE:sec:POL:a.8.35 -->
**CLD-SEC-POL-A.8.35 — Trennung in virtuellen Rechenumgebungen**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Trennung in virtuellen Rechenumgebungen |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | CLD-SEC-POL-A.8.35 |
| **Dokumentersteller** | ISB / Cloud Security Manager |
| **Dokumenteigentümer** | ISB |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Noch festzulegen] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |
| **Cloud-Produktversion** | 1.0 |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Noch festzulegen] | ISB | Erstversion für ISO/IEC 27017:2026 Ausg. 2 Implementierung |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen Änderungen der Virtualisierungsarchitektur, oder nach einem trennungsbezogenen Vorfall)
**Nächstes Überprüfungsdatum**: [Datum des Inkrafttretens + 12 Monate]

**Genehmigungskette**:

- Primär: ISB
- Sekundär: Cloud Security Manager
- Technisch: Cloud Engineering Lead
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-A.8.20-22 (Netzwerksicherheit — übergeordnete ISMS-Richtlinie für die Netzwerktrennung gemäss A.8.22)
- CLD-SEC-POL-A.5.38 (Gemeinsame Rollen und Verantwortlichkeiten in einer Cloud-Computing-Umgebung)
- CLD-SEC-POL-A.8.36 (Erkennung und Verhinderung unbefugter Nutzung von Cloud-Diensten)
- CLD-SEC-IMP-A.8.35-TG (Trennung in virtuellen Rechenumgebungen — Technischer Leitfaden, enthält die vollständigen Trennungsschemata und die Architekturvorlage)
- CLD-SEC-REF-A.5-A.8 (Cloud-Sicherheits-Leitfadenanhang)
- ISO/IEC 27017:2026, Abschnitt 8.35 (CLD — Trennung in virtuellen Rechenumgebungen)
- ISO/IEC 27040 (Speichersicherheit)

---

## Zusammenfassung

Diese Richtlinie legt fest, wie [Organisation] Mandantenumgebungen innerhalb virtueller Mandanten-Rechenumgebungen vor unbefugtem Zugriff schützt, gemäss ISO/IEC 27017:2026, Abschnitt 8.35.

**Geltungsbereich**: Alle virtuellen Rechenumgebungen, in denen [Organisation] innerhalb eines Mandanten-Cloud-Dienstes tätig ist — sei es die eigene virtuelle Umgebung von [Organisation], die auf dem Cloud-Dienst eines Drittanbieter-CSP läuft (CSC-Rolle), oder die Mandanten-Infrastruktur, die [Organisation] für ihre eigenen CSC betreibt (CSP-Rolle).

**Hinweis zu erweiterten Kontrollen**: ISO/IEC 27017:2026, Abschnitt 8.35 ist eine von vier cloudspezifischen erweiterten „CLD"-Kontrollen, die mit der zweiten Ausgabe des Standards eingeführt wurden (neben 5.38, 5.39 und 8.36). Sie ist thematisch am ehesten den Netzwerktrennungspflichten der Kontrolle 8.22 im Annex A von ISO/IEC 27001:2022 vergleichbar — und wird parallel dazu umgesetzt —, behandelt jedoch speziell die logische Trennung virtualisierter Anwendungen, Speicher und Netzwerkressourcen, nicht nur den Netzwerkverkehr.

**Kernrisiko**: Unzureichende Trennung in einer gemeinsam genutzten virtuellen Rechenumgebung kann die Daten oder Workloads eines Mandanten einem anderen Mandanten, Dritten oder unbefugtem CSP-Personal aussetzen. Da die Mandantenisolation für den CSC weitgehend nicht einsehbar ist, muss [Organisation] ihre Trennungsanforderungen explizit definieren (als CSC) und die logische Trennung konsequent durchsetzen (als CSP), anstatt davon auszugehen, dass die Isolation automatisch angemessen ist. Eine zu irgendeinem Zeitpunkt festgestellte Trennungslücke — während der Einführung, periodischer Verifizierung oder Tests — wird als Informationssicherheitsrisiko behandelt, das einer Bewertung bedarf, nicht als ein später zu überarbeitender Konfigurationshinweis.

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27017:2026 — Abschnitt 8.35

**Kontrollaussage (ISO/IEC 27017:2026, 8.35):**
> „Die virtuelle Umgebung eines CSC, die auf einem Cloud-Dienst läuft, sollte vor unbefugtem Zugriff geschützt werden."

**Zweck (ISO/IEC 27017:2026, 8.35):**
> „Verhinderung unangemessenen Zugriffs oder unangemessener Offenlegung von Informationen durch unsichere Virtualisierung."

*(Arbeitsübersetzung des englischen Originaltextes der Norm zur besseren Lesbarkeit; bei Abweichungen ist der offizielle englische Text von ISO/IEC 27017:2026 massgebend.)*

## Anwendbarkeit

Diese Richtlinie gilt für:

- Alle virtuellen Maschineninstanzen, Container, Speichervolumes und virtuellen Netzwerke von [Organisation], die auf dem Mandanten-Cloud-Dienst eines Drittanbieter-CSP laufen (CSC-Rolle)
- Alle Mandanten-virtualisierte Infrastruktur, die [Organisation] betreibt, um Cloud-Dienste für ihre eigenen CSC bereitzustellen (CSP-Rolle)
- Alle Mitarbeitenden mit administrativem Zugriff auf Virtualisierungs-, Hypervisor- oder Container-Orchestrierungsebenen

## Regulatorischer und normativer Rahmen

ISO/IEC 27017:2026 ist eine informative Erweiterung von ISO/IEC 27002:2022. Abschnitt 8.35 entspricht keiner nummerierten Kontrolle von ISO/IEC 27002:2022; er ist neu in der zweiten Ausgabe 2026 und ersetzt und erweitert die CLD.9.5.1 der ersten Ausgabe 2015 („Trennung in virtuellen Rechenumgebungen"). Er wird parallel zur Kontrolle 8.22 im Annex A von ISO/IEC 27001:2022 (Netzwerktrennung) umgesetzt und stützt sich auf die Leitlinien zur sicheren Mandantenfähigkeit in ISO/IEC 27040.

---

# Richtlinienaussagen: Trennung in virtuellen Rechenumgebungen (8.35)

## Pflichten als Cloud-Service-Kunde (CSC)

Wenn [Organisation] als Cloud-Service-Kunde handelt, muss [Organisation]:

- Die auf dem Cloud-Dienst auszuführenden Daten und Workloads nach Sensitivität klassifizieren und ihre Anforderungen zur Trennung der Umgebung von [Organisation] zur Erreichung der Mandantenisolation vor der Auswahl des Dienstes definieren
- Ein der Klassifizierung angemessenes Mindestisolationsniveau festlegen (z. B. hypervisorerzwungene logische Isolation für Standard-Workloads, dedizierte/Einzelmandanten-Infrastruktur für die sensibelsten Workloads) und dies in der Erklärung der Trennungsanforderungen dokumentieren (Schema in CLD-SEC-IMP-A.8.35-TG, Abschnitt 1)
- Vor und periodisch während der Nutzung des Dienstes verifizieren, dass der CSP diese Trennungsanforderungen erfüllt, unter Verwendung von CSP-Dokumentation, die – sofern verfügbar – mit unabhängigen Nachweisen (Zertifizierungen, Prüfberichten) abgeglichen wird
- Mindestens jährlich sowie immer dann, wenn der CSP eine wesentliche Änderung seiner Virtualisierungs- oder Mandantenfähigkeits-Architektur ankündigt, eine erneute Verifizierung durchführen
- Wo die Verifizierung eine Lücke zwischen den Trennungskontrollen des CSP und der von [Organisation] festgelegten Anforderung feststellt, dies als Informationssicherheitsrisiko behandeln und in den dokumentierten Risikobeurteilungs- und Behandlungsprozess von [Organisation] einbringen

## Pflichten als Cloud-Service-Anbieter (CSP)

Wenn [Organisation] als Cloud-Service-Anbieter handelt, muss [Organisation]:

- Die logische Trennung von CSC-Daten, virtualisierten Anwendungen, Betriebssystemen, Speicher und Netzwerkressourcen durchsetzen, um die Isolation der von verschiedenen Mandanten genutzten Ressourcen in einer Mandanten-Umgebung sicherzustellen, dokumentiert je Ebene in der Trennungsarchitektur-Dokumentation (Vorlage in CLD-SEC-IMP-A.8.35-TG, Abschnitt 3)
- Die mit dem Ausführen von CSC-bereitgestellter Software innerhalb der von [Organisation] angebotenen Cloud-Dienste verbundenen Risiken bewerten, bevor eine solche Software in gemeinsam genutzter Infrastruktur ausgeführt werden darf, und Kompensationskontrollen anwenden, wo die Isolationsgrenze als unzureichend bewertet wird
- Die Trennung der eigenen internen Verwaltungsfunktionen von [Organisation] von den durch CSC genutzten Ressourcen durch einen separaten administrativen Zugangspfad durchsetzen
- Periodische Tests der Trennungsarchitektur planen (z. B. Penetrationstests der Mandantengrenzen, Konfigurationsprüfungen der Hypervisor-/Container-Isolation), um zu bestätigen, dass das dokumentierte Design in der Praxis wirksam bleibt, nicht nur auf dem Papier korrekt ist

## Technologieabhängige Umsetzung

[Organisation] erkennt an, dass die Umsetzung der logischen Trennung von den angewendeten Virtualisierungstechnologien abhängt. Netzwerk- und Speicherkonfigurationen können durch eine Software-Virtualisierungsfunktion virtualisiert werden, die eine virtuelle Umgebung bereitstellt (zum Beispiel ein virtuelles Betriebssystem oder einen Container-Isolationsmechanismus). Wird eine solche Software-Virtualisierung eingesetzt, muss [Organisation] die Trennung unter Verwendung der dieser Software eigenen Trennungsfunktionen gestalten und umsetzen, zusätzlich zu den zugrundeliegenden physischen oder netzwerkbezogenen Kontrollen.

## Rechtliche und regulatorische Erwägungen

Wo anwendbare Gesetze oder Vorschriften die Trennung von Netzwerken oder die Isolation des Netzwerkverkehrs für von [Organisation] verarbeitete Daten verlangen, muss [Organisation] sicherstellen, dass ihre Trennungskontrollen für virtuelle Rechenumgebungen diese Anforderungen zusätzlich zu den Basisanforderungen dieser Richtlinie erfüllen, und dies im Rahmen der jährlichen Überprüfung bestätigen.

## Kommunikation und Sensibilisierung

[Organisation] muss Trennungsanforderungen und Architekturentscheidungen den internen Teams kommunizieren, die diese entwerfen, betreiben oder sich darauf verlassen (Cloud Engineering, Cloud-Diensteerbringung, Security Operations), über die Trennungsarchitektur-Dokumentation und die Einbindung in das Informationssicherheits-Sensibilisierungsprogramm der Organisation (siehe ISMS-POL-A.6.3). Wo [Organisation] als CSP handelt, müssen die für einen CSC relevanten wesentlichen Trennungszusagen diesem CSC über Einführungsunterlagen oder Dienstdokumentation kommuniziert werden.

## Erklärung der Trennungsanforderungen — Mindestinhalt

Die Erklärung der Trennungsanforderungen (vollständiges Schema in CLD-SEC-IMP-A.8.35-TG, Abschnitt 1) muss je genutztem Cloud-Dienst erfassen: die Dienstkennung; die Daten-/Workload-Klassifizierung; das Mindestisolationsniveau und dessen Begründung; sowie das Datum, an dem die Anforderung definiert wurde.

## Trennungsarchitektur-Dokumentation — Mindestinhalt

Die Trennungsarchitektur-Dokumentation (vollständige Vorlage in CLD-SEC-IMP-A.8.35-TG, Abschnitt 3) muss je von [Organisation] betriebener Mandanten-Umgebung erfassen: den auf jeder Ebene angewendeten Trennungsmechanismus (CSC-Daten, virtualisierte Anwendungen, Betriebssysteme, Speicher, Netzwerk); das Design der internen Verwaltungstrennung; sowie eine Zusammenfassung der letzten Trennungstests und ihrer Ergebnisse.

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|----------------------|
| **ISB** | Ist Eigentümer von CLD-SEC-POL-A.8.35; genehmigt die Trennungsarchitektur für von [Organisation] betriebene Mandanten-Umgebungen (CSP-Rolle); genehmigt die Akzeptanz der Trennungskontrollen eines CSP für kritische Workloads (CSC-Rolle); prüft trennungsbezogene Risikoeskalationen |
| **Cloud Security Manager** | Definiert Trennungsanforderungen für genutzte Dienste (CSC-Rolle); verifiziert periodisch die Trennungskontrollen des CSP; berichtet dem ISB Kennzahlen zu Trennungsverifizierung und -tests |
| **Cloud Engineering Lead** | Entwirft und implementiert logische Trennungskontrollen (Hypervisor, Container, Speicher, Netzwerk) für von [Organisation] betriebene Mandanten-Umgebungen (CSP-Rolle); plant und überprüft periodische Trennungstests |
| **Cloud-Diensteerbringung / Engineering** | Bewertet das Risiko von CSC-bereitgestellter Software vor Zulassung ihrer Ausführung in gemeinsam genutzter Infrastruktur; pflegt die Trennung des internen Verwaltungszugriffs von CSC-Ressourcen |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Verantwortlich | Aufbewahrungsdauer |
|----------|-------------|-----------------|---------------------|
| Erklärung der Trennungsanforderungen (CSC-Rolle) | Von [Organisation] dokumentierte Mandantenisolationsanforderungen für jeden genutzten Cloud-Dienst | Cloud Security Manager | Aktuell + 3 Jahre |
| CSP-Trennungsverifizierungsnachweise | Nachweise der periodischen Verifizierung, dass die Trennungskontrollen eines CSP die Anforderungen von [Organisation] erfüllen | Cloud Security Manager | Aktuell + 3 Jahre |
| Trennungsarchitektur-Dokumentation (CSP-Rolle) | Technische Dokumentation der über virtualisierte Anwendungen, Speicher und Netzwerk implementierten logischen Trennungskontrollen | Cloud Engineering Lead | Aktuelle Version + Vorgängerversionen für 3 Jahre |
| Risikobewertungen für CSC-bereitgestellte Software | Nachweise der vor Zulassung der Ausführung von CSC-bereitgestellter Software in gemeinsam genutzter Infrastruktur durchgeführten Risikobewertungen | Cloud-Diensteerbringung / Engineering | Aktuell + 3 Jahre |
| Trennungstestnachweise | Ergebnisse periodischer Tests der Mandantengrenzen und Konfigurationsprüfungen der Isolation | Cloud Engineering Lead | Aktuell + 3 Jahre |
| Trennungslücken-/Risikonachweise | Nachweise jeder in den Risikobeurteilungs- und Behandlungsprozess eskalierten Trennungslücke, mit Lösung | ISB | Aktuell + 3 Jahre |

---

# Überwachung und Kennzahlen

Der Cloud Security Manager berichtet dem ISB mindestens vierteljährlich:

- Den Anteil der Cloud-Dienste (CSC-Rolle) mit einer aktuellen Trennungsverifizierung innerhalb der letzten 12 Monate
- Die Ergebnisse und den Behebungsstatus der letzten Trennungstests (CSP-Rolle)
- Die Anzahl der identifizierten und in den Risikobeurteilungs- und Behandlungsprozess eskalierten Trennungslücken sowie deren Lösungsstatus

---

# Prüfungshinweise

Prüfende, die die Compliance mit CLD-SEC-POL-A.8.35 verifizieren, sollten Folgendes vorfinden:

- Dokumentierte Trennungsanforderungen für jeden von [Organisation] als CSC genutzten Cloud-Dienst
- Nachweise der periodischen Verifizierung, dass die Trennungskontrollen des CSP diese Anforderungen erfüllen, und dass Lücken als Risiken eskaliert statt offengelassen werden
- Technische Dokumentation der logischen Trennungsarchitektur für jede von [Organisation] als CSP betriebene Mandanten-Umgebung, die Daten, virtualisierte Anwendungen, Betriebssysteme, Speicher und Netzwerk abdeckt
- Belege, dass der interne Verwaltungszugriff von [Organisation] von CSC-gerichteten Ressourcen getrennt ist
- Risikobewertungsnachweise für CSC-bereitgestellte Software, die innerhalb der gemeinsam genutzten Infrastruktur von [Organisation] ausgeführt wird
- Nachweise periodischer Trennungstests, nicht nur eine einmalige Überprüfung des Architekturdesigns

---

<!-- QA_VERIFIED: 2026-08-01 -->
