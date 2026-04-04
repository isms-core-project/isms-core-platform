<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.11-technische-referenz-datenmaskierung-DE:framework:CTX:a.8.11 -->
**ISMS-CTX-A.8.11 — Technische Referenz Datenmaskierung**
**Maskierungstechniken, Entdeckungsmethoden und Implementierungsmuster (Nicht-ISMS Technische Referenz)**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Technische Referenz Datenmaskierung |
| **Dokumententyp** | Intern — Technische Referenz (Kein ISMS) |
| **Dokument-ID** | ISMS-CTX-A.8.11 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | INTERN |
| **Status** | Lebendes Dokument |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|-----------|
| 1.0 | [Date] | Security Architecture Team | Erstveröffentlichung der technischen Referenz für ISO 27001:2022-Zertifizierung |

**Überprüfungszyklus**: Bei Bedarf (Technologie- und Technikenentwicklung)
**Nächstes Überprüfungsdatum**: [Date + 12 months]
**Genehmiger**: Sicherheitsarchitektur / Datenschutz-SME (technische Referenz, keine ISMS-Genehmigungskette erforderlich)

**Verteilung**: Security Engineering, Data Engineering, Entwicklungsteams, IT-Betrieb (zur Sensibilisierung und Implementierungsanleitung)

---

⚠️ **WICHTIG — KEIN ISMS-TECHNISCHES UNTERSTÜTZUNGSDOKUMENT**

Dieses Dokument dient ausschliesslich Informations- und Sensibilisierungszwecken.

- Dieses Dokument ist KEIN Bestandteil des Informationssicherheitsmanagementsystems (ISMS).
- Dieses Dokument legt KEINE verbindlichen Datenmaskierungssteuerungen fest.
- Dieses Dokument legt KEINE verbindlichen Anforderungen, Fristen, KPIs oder SLAs fest.
- Dieses Dokument mandatiert NICHT die Verwendung, das Verbot oder die Konfiguration spezifischer Maskierungs-Tools, Anbieter, Algorithmen oder Plattformen.
- Dieses Dokument setzt KEINE ISMS-Richtlinie ausser Kraft oder erweitert sie.

Alle verbindlichen Datenmaskierungsanforderungen, Verpflichtungen und Governance-Entscheidungen sind ausschliesslich in **ISMS-POL-A.8.11 (Richtlinie zur Datenmaskierung)** und anderen genehmigten ISMS-Dokumenten definiert.

Dieses Dokument dient ausschliesslich als technische Referenz um:

- Häufig anzutreffende Maskierungstechniken und ihre Implementierungen zu beschreiben
- Datenentdeckungs-Methodikanleitung für Praktiker bereitzustellen
- Technische Diskussionen und Implementierungsplanung zu unterstützen
- Tool-Auswahl und Architekturentscheidungen zu informieren (herstellerneutral)
- Kurzreferenzhandbücher für operative Maskierungsaktivitäten anzubieten
- **Dieses Dokument darf nicht als Revisionsnachweis für Implementierungen verwendet werden**

Die Verwendung dieses Dokuments impliziert keine Implementierung, Compliance oder operationale Reife. Implementierungsnachweise sind in ISMS-IMP-A.8.11-Beurteilungsarbeitsmappen dokumentiert.

**Kritische Positionierungsaussage**:
Dieses Dokument überschreitet bewusst den Detailgrad, der für ISO/IEC 27001-Richtliniendokumentation erforderlich ist. Sein Zweck ist technische Sensibilisierung und Praktikeranleitung ausschliesslich. Aus der Präsenz, Abwesenheit oder Klassifizierung einer Technik, eines Tools, eines Algorithmus oder eines Parameters in diesem Dokument dürfen keine Prüferschlussfolgerungen gezogen werden.

---

# Dokumentzweck und Anwendungsbereich

## Zweck

Dieses Dokument bietet einen technischen Tiefgang in Datenmaskierungs-Implementierungsmuster, -techniken und -methodiken, die in modernen Informationssystemen häufig anzutreffen sind. Es soll unterstützen bei:

- Technischer Sensibilisierung für Maskierungsimplementierungsoptionen
- Verständnis von Abwägungen bei der Technikauswahl
- Praktischer Anleitung für Datenentdeckung und -klassifizierung
- Kontext für Technologie- und Tool-Evaluation (herstellerneutral)
- Implementierungsplanung für Entwicklungs- und Betriebsteams
- Fehlerbehebung und Optimierung bestehender Maskierungslösungen

## Was dieses Dokument NICHT ist

Dieses Dokument legt NICHT fest:

- Die genehmigten oder verbotenen Maskierungstechniken von [Organisation] (siehe ISMS-POL-A.8.11 Abschnitt 2.2 und Anhang A)
- Verbindliche Implementierungsanforderungen (siehe ISMS-POL-A.8.11)
- Compliance-Verpflichtungen oder Revisionskriterien (siehe ISMS-POL-A.8.11)
- Ersatz für ISMS-POL-A.8.11-Richtlinienanforderungen
- Spezifische Tool-Anbieter oder -Produkte (Technologieauswahl basierend auf Risikobeurteilung von [Organisation])
- Datenklassifizierungsschemata (siehe Informationsklassifizierungsrichtlinie von [Organisation] gemäss A.5.12)
- Rollen und Verantwortlichkeiten (siehe ISMS-POL-A.8.11 Abschnitt 3.1)

## Beziehung zum ISMS

Dieses Dokument ist eine **nicht verbindliche technische Referenz**. Alle Anforderungen und Governance-Entscheidungen zur Datenmaskierungssteuerung sind ausschliesslich in ISMS-POL-A.8.11 (Richtlinie zur Datenmaskierung) definiert.

Implementierungsentscheidungen werden durch ISMS-IMP-A.8.11-Beurteilungsarbeitsmappen basierend auf Risikobeurteilung, betrieblichem Kontext, Datenklassifizierung und regulatorischen Anforderungen dokumentiert.

## Inhaltsorganisation

Diese Referenz organisiert Maskierungsanleitung nach:

- **Abschnitt 2**: Detaillierte Maskierungstechnik-Spezifikationen (Algorithmen, Parameter, Konfiguration)
- **Abschnitt 3**: Datenentdeckungsmethodiken (wie sensitive Daten gefunden werden)
- **Abschnitt 4**: Maskierungs-Tool-Landschaft (herstellerneutral, Fähigkeitsvergleich)
- **Abschnitt 5**: Implementierungsmuster (Architekturen und Integrationsansätze)
- **Abschnitt 6**: Kurzreferenzhandbücher (Entscheidungsbäume, häufige Szenarien, Fehlerbehebung)

---

# Maskierungstechnik-Spezifikationen

## Techniken der Statischen Datenmaskierung (SDM)

**Überblick**: Statische Datenmaskierung ersetzt sensitive Daten in nicht produktiven Datenbanken permanent durch realistische, aber fiktive Daten. Originaldaten werden bei einem einmaligen Maskierungsprozess irreversibel überschrieben.

### Substitutions- (Ersatz-) Techniken

**Zeichenebenen-Substitution**:

```
Original: „Max Müller"
Technik: Jedes Zeichen durch zufälliges Zeichen gleichen Typs ersetzen
Maskiert: „Tpx Qüjbk"

Konfiguration:

- Zeichenklassen-Beibehaltung: Buchstabe→Buchstabe, Ziffer→Ziffer, Sonderzeichen→Sonderzeichen
- Gross-/Kleinschreibung-Beibehaltung: Grossbuchstabe→Grossbuchstabe, Kleinbuchstabe→Kleinbuchstabe
- Längen-Beibehaltung: Gleiche Zeichenanzahl
```

**Wortebenen-Substitution**:

```
Original: „Max Müller"
Technik: Durch zufälligen Namen aus Namenswörterbuch ersetzen
Maskiert: „Thomas Schneider"

Konfiguration:

- Wörterbuchquelle: Eingebaute Namenslisten, externe Namens-Datenbanken
- Kultureller Kontext: Herkunft anpassen (westliche, asiatische, nahöstliche Namen)
- Geschlechts-Beibehaltung: Männlich→Männlich, Weiblich→Weiblich (wenn bestimmbar)
- Konsistenz: Gleiche Eingabe erzeugt immer gleiche Ausgabe (deterministisch)
```

**Format-erhaltende Substitution**:

```
Original-E-Mail: „max.mueller@example.com"
Technik: Teile ersetzen unter Beibehaltung des Formats
Maskiert: „thomas.schneider@example.com"

Konfiguration:

- Domäne für Zustellbarkeitstests beibehalten
- Lokalen Teil durch realistischen Namen ersetzen
- „@"- und „."-Positionen beibehalten
```

**Implementierungsüberlegungen**:

- **Referenzielle Integrität**: Deterministische Algorithmen verwenden (hash-basiert), um gleiche Eingabe über Tabellen hinweg konsistent zu maskieren
- **Datenverteilung**: Statistische Verteilung für Leistungstests aufrechterhalten (z.B. Namenshäufigkeitsverteilung)
- **Eindeutigkeit**: Sicherstellen, dass maskierte Werte eindeutig bleiben, wo Originaldaten eindeutig waren (Primärschlüssel)
- **Leistung**: Batch-Verarbeitung für grosse Datensätze, Datenbankoperationen optimieren

### Shuffle- (Permutations-) Techniken

**Spalten-Shuffle**:

```
Originaltabelle:
ID | Name            | E-Mail
1  | Max Müller      | max@example.com
2  | Anna Meier      | anna@example.com
3  | Thomas Koch     | thomas@example.com

Nach Spalten-Shuffle (E-Mail-Spalte):
ID | Name            | E-Mail
1  | Max Müller      | thomas@example.com
2  | Anna Meier      | max@example.com
3  | Thomas Koch     | anna@example.com
```

**Konfiguration**:

- Shuffle-Bereich: Innerhalb einer einzelnen Tabelle
- Zufalls-Seed: Deterministisch für Wiederholbarkeit
- Einschränkungs-Beibehaltung: Keine Eindeutigkeitsverletzungen
- Foreign-Key-Behandlung: Nur Nicht-FK-Spalten shuffeln oder tabellenübergreifend koordinieren

**Anwendungsfälle**:

- Person-zu-Merkmal-Verknüpfung aufbrechen unter Beibehaltung realer Datenverteilung
- Realistische Testdaten ohne direkte Einzelpersonenidentifizierung
- Geringerer Rechenaufwand als Substitution

**Einschränkungen**:

- Nicht geeignet für hochgradig einzigartige Kombinationen (möglicherweise noch identifizierbar)
- Referenzielle Integrität über mehrere Tabellen komplex
- Erfüllt möglicherweise nicht regulatorische De-Identifizierungsstandards (DSGVO, HIPAA)

### Varianz-/Rausch-Hinzufügung (Numerische Daten)

**Additives Rauschen**:

```
Originalgehalt: CHF 90'000
Technik: Zufällige Varianz ±10% hinzufügen
Maskiert: CHF 87'450 oder CHF 96'700

Konfiguration:

- Varianzbereich: ±5% bis ±20% typisch
- Verteilung: Gleichmässig, Gauss'sch oder andere
- Vorzeichenbeibehaltung: Positiv/Negativ erhalten
- Grenzkontrolle: Ergebnis innerhalb gültigem Bereich halten
```

**Multiplikatives Rauschen**:

```
Originalalter: 35
Technik: Mit zufälligem Faktor 0,9-1,1 multiplizieren
Maskiert: 33 oder 38

Konfiguration:

- Faktorbereich: 0,8-1,2 typisch für moderate Maskierung
- Rundung: Bei Alter auf Ganzzahlen, bei Währung auf Rappen
- Bereichsgrenzen: Alter zwischen 0-120 halten etc.
```

**Implementierungsüberlegungen**:

- **Statistische Gültigkeit**: Mittelwert, Median, Verteilungsform für Analysen aufrechterhalten
- **Ausreisserbehandlung**: Spezielle Behandlung für Extremwerte
- **Präzision**: Geeignete Dezimalstellen beibehalten
- **Wiederholbarkeit**: Seed-basierten Zufallsgenerator für Konsistenz verwenden

**Anwendungsfälle**:

- Finanzbeträge, bei denen exakte Werte nicht benötigt werden
- Alter, Grösse, Gewicht für Demografie
- Statistische Analysen, die realistische Verteilungen erfordern

### Nullungs-/Löschungstechniken

**Vollständige Nullung**:

```
Original: „Vertrauliches internes Memo"
Maskiert: NULL

Konfiguration:

- Spaltenexistenz erhalten (NULL vs. Spalte löschen)
- NOT-NULL-Einschränkungen behandeln (Platzhalter verwenden)
- Foreign-Key-Auswirkungen prüfen
```

**Partielle Nullung mit Platzhalter**:

```
Original: „max.mueller@example.com"
Maskiert: „maskiert@maskiert.com"

Konfiguration:

- Platzhalterwert: „MASKIERT", „GESCHWÄRZT", Leerstring oder gültiger Dummy
- Applikationskompatibilität: Sicherstellen, dass Apps Platzhalter korrekt behandeln
```

**Anwendungsfälle**:

- Felder ohne Nutzen in Testumgebungen
- Hochsensitive Daten ohne legitimen nicht produktiven Verwendungszweck
- Einfachster Maskierungsansatz, wenn Datennützlichkeit nicht erforderlich

### Datums- und Zeit-Maskierung

**Datumsverschiebung**:

```
Originaldatum: 15.03.2024
Technik: Zufälligen Versatz ±180 Tage hinzufügen
Maskiert: 22.01.2024 oder 10.08.2024

Konfiguration:

- Versatzbereich: Tage, Wochen oder Monate
- Konsistenz: Gleiche Person erhält gleichen Versatz (deterministisch nach ID)
- Sequenzbeibehaltung: Ereignisreihenfolge aufrechterhalten (Geburtsdatum < Einschreibung < Abschluss)
- Wochentag-Beibehaltung: Optional — gleichen Wochentag beibehalten
```

**Datumsgeneralisierung**:

```
Original: 15.03.2024
Maskiert: 01.03.2024 (März 2024, Tag entfernt)
Maskiert: Q1 2024 (Quartal 2024, Monat entfernt)
Maskiert: 2024 (Nur Jahr)

Konfiguration:

- Granularität: Tag, Monat, Quartal, Jahr
- Nullwertbehandlung: Fehlende Daten bleiben fehlend
- Altersberechnung: Abgeleitetes Alter bleibt ausreichend genau
```

**Implementierungsüberlegungen**:

- **Altersberechnungen**: Relative Alter zwischen Daten aufrechterhalten
- **Ereignissequenzen**: Chronologische Reihenfolge erhalten (Einstellungsdatum < Beförderungsdatum)
- **Schaltjahre**: 29. Februar angemessen behandeln
- **Zeitzonen**: Berücksichtigen, ob Zeiten mit Zeitzoneninformationen gespeichert sind

## Techniken der Dynamischen Datenmaskierung (DDM)

**Überblick**: Dynamische Datenmaskierung wendet Maskierungsregeln in Echtzeit am Punkt des Datenzugriffs auf Basis der Benutzerrolle oder des Kontexts an. Originaldaten bleiben im Speicher unverändert.

### Rollenbasierte Maskierung

**Datenbankebenen-DDM**:

```sql
-- Beispiel: PostgreSQL Row-Level Security mit Maskierungsfunktion

CREATE FUNCTION mask_email(email TEXT) RETURNS TEXT AS $$
BEGIN
  IF current_user_role() = 'admin' THEN
    RETURN email;  -- Admin sieht vollständige E-Mail
  ELSE
    RETURN REGEXP_REPLACE(email, '^(.{2}).*(@.*)$', '\1***\2');
    -- Standardbenutzer sehen: "ma***@example.com"
  END IF;
END;
$$ LANGUAGE plpgsql;

-- Auf View anwenden
CREATE VIEW maskierte_kunden AS
SELECT
  kunden_id,
  kundenname,
  mask_email(email) AS email,
  CASE
    WHEN current_user_role() = 'admin' THEN telefon
    ELSE '***-***-' || RIGHT(telefon, 4)  -- Nur letzte 4 Ziffern anzeigen
  END AS telefon
FROM kunden;
```

**Konfiguration**:

- Rollenzuordnung: Festlegen, welche Rollen welche Maskierungsebene sehen
- Maskierungsfunktionen: Bibliothek wiederverwendbarer Maskierungsfunktionen
- Leistung: Indizierte Spalten verlieren möglicherweise Indexvorteil
- Protokollierung: Alle Zugriffsversuche und angewendete Maskierungsregeln protokollieren

**Applikationsebenen-DDM**:

```python
# Beispiel: Applikationsebenen-Maskierung basierend auf Benutzerrechten

def get_kundendaten(kunden_id, benutzerrolle):
    kunde = db.query(f"SELECT * FROM kunden WHERE id={kunden_id}")

    if benutzerrolle == 'admin':
        return kunde  # Vollständige nicht maskierte Daten
    elif benutzerrolle == 'support':
        kunde.email = mask_email(kunde.email)
        kunde.telefon = mask_telefon(kunde.telefon)
        return kunde
    else:
        kunde.email = "***@***"
        kunde.telefon = "***-***-****"
        kunde.adresse = "[GESCHWÄRZT]"
        return kunde

def mask_email(email):
    teile = email.split('@')
    return f"{teile[0][:2]}***@{teile[1]}"

def mask_telefon(telefon):
    return f"***-***-{telefon[-4:]}"
```

**Konfiguration**:

- Middleware-Implementierung: Daten vor Präsentation abfangen
- Caching-Überlegungen: Cache nach Rolle + Daten strukturieren
- Konsistenz: Alle API-Endpunkte wenden gleiche Maskierungsregeln an
- Testing: Maskierung für jede Rolle validieren

### Kontextbasierte Maskierung

**Bildschirm-/Bericht-basierte Maskierung**:

```
Kontext: Kundendetailbildschirm → Teilweise Kreditkarte anzeigen
Kontext: Finanzberichtsexport → Vollständige Kreditkarte anzeigen (autorisierte Benutzer)
Kontext: E-Mail-Benachrichtigung → Maskierte Kreditkarte anzeigen (alle Benutzer)

Konfiguration:

- Kontexterkennung: Bildschirm-ID, Berichtstyp, Exportformat
- Regelpriorität: Kontextregeln überschreiben rollenbasierte Regeln
- Protokollierung: Kontext und angewendete Maskierungsregel protokollieren
```

**Zeit-basierte Maskierung**:

```
Bedingung: Aktuelle Zeit innerhalb Geschäftszeiten UND Benutzerstandort = 'Büro'
Aktion: Nicht maskierte Daten anzeigen

Bedingung: Ausserhalb der Geschäftszeiten ODER Benutzerstandort = 'Remote'
Aktion: Zusätzliche Maskierungsebene anwenden

Konfiguration:

- Zeitfenster: Geschäftszeiten, Wartungsfenster
- Standorterkennung: IP-Geolokalisierung, VPN-Erkennung
- Multi-Faktor: Zeit + Standort + Rolle kombinieren
```

### Abfrageebenen-Maskierung

**Partielle Ergebnis-Maskierung**:

```sql
-- Beispiel: Nur aggregierte/zusammenfassende Daten für nicht autorisierte Benutzer anzeigen

-- Autorisierte Benutzerabfrage:
SELECT mitarbeitername, gehalt FROM mitarbeiter;
-- Gibt zurück: Individuelle Gehälter

-- Gleiche Abfrage für nicht autorisierten Benutzer:
SELECT 'GESCHWÄRZT' AS mitarbeitername,
       CASE
         WHEN COUNT(*) < 10 THEN 'N/A'  -- Kleine Gruppenidentifizierung verhindern
         ELSE ROUND(AVG(gehalt), -3)     -- Nur gerundeter Durchschnitt
       END AS gehalt
FROM mitarbeiter
GROUP BY abteilung;
-- Gibt zurück: Nur aggregierte Daten
```

**Konfiguration**:

- Aggregationsschwellenwert: Mindestgruppengrösse (k-Anonymität)
- Rundungsebene: Präzisionsreduktion für De-Identifizierung
- NULL-Behandlung: Ergebnisse bei unzureichenden Daten unterdrücken

## Tokenisierungstechniken

**Überblick**: Tokenisierung ersetzt sensitive Daten durch nicht sensitive Tokens, während das Original in einem gesicherten Token-Vault gespeichert wird. Tokens behalten das Format bei, haben aber keine intrinsische Bedeutung.

### Format-erhaltende Tokenisierung

**Kreditkarten-Tokenisierung**:

```
Original-PAN: 4532-1234-5678-9010
Token: 4532-7821-3456-1098

Konfiguration:

- BIN-Beibehaltung: Erste 6 Ziffern (Bank Identification Number) beibehalten
- Letzte-4-Beibehaltung: Letzte 4 Ziffern für Kundenreferenz beibehalten
- Format-Beibehaltung: Bindestriche, Länge beibehalten
- Luhn-Check: Token besteht Luhn-Algorithmus-Validierung
- Vault-Speicherung: Original-PAN verschlüsselt im Token-Vault gespeichert
```

**Implementierungsbeispiel**:

```python
# Vereinfachtes Tokenisierungsbeispiel

class TokenVault:
    def __init__(self):
        self.token_zu_wert = {}  # In realer Implementierung verschlüsselt
        self.wert_zu_token = {}  # Für deterministische Tokenisierung

    def tokenisieren(self, pan, bin_erhalten=True, letzte4_erhalten=True):
        # Prüfen ob bereits tokenisiert
        if pan in self.wert_zu_token:
            return self.wert_zu_token[pan]

        # Format-erhaltenden Token generieren
        if bin_erhalten and letzte4_erhalten:
            bin = pan[:6]
            letzte4 = pan[-4:]
            mitte = zufaellige_ziffern_generieren(6)  # Zufällige Mittelziffern
            token = f"{bin}{mitte}{letzte4}"
            token = fuer_luhn_anpassen(token)  # Luhn-Check sicherstellen
        else:
            token = zufaellige_pan_generieren()

        # Bidirektionale Zuordnung speichern (verschlüsselt)
        self.token_zu_wert[token] = verschluesseln(pan)
        self.wert_zu_token[pan] = token

        return token

    def detokenisieren(self, token, anforder_autorisiert=True):
        if not anforder_autorisiert:
            raise PermissionError("Nicht autorisierte De-Tokenisierung")

        if token not in self.token_zu_wert:
            raise ValueError("Ungültiger Token")

        # De-Tokenisierungsanfrage protokollieren
        pruefprotokoll(f"De-Tokenisierung: token={token}, benutzer={aktueller_benutzer()}")

        return entschluesseln(self.token_zu_wert[token])
```

**Token-Vault-Sicherheit**:

- Verschlüsselung: Vault-Daten mit starker Verschlüsselung gesichert (AES-256)
- Zugangskontrolle: De-Tokenisierung erfordert explizite Autorisierung
- Prüfprotokollierung: Alle Tokenisierungs- und De-Tokenisierungsvorgänge protokolliert
- Schlüsselmanagement: Vault-Verschlüsselungsschlüssel gemäss Kryptografierichtlinie A.8.24 verwaltet
- Sicherung: Vault separat mit angemessener Sicherheit gesichert
- Hochverfügbarkeit: Vault-Verfügbarkeit für Betrieb kritisch

### Nicht-Format-erhaltende Tokenisierung

**Zufällige Token-Generierung**:

```
Original-AHV: 756.1234.5678.97
Token: 8f3d9a21-c8b4-4e7a-9d12-5c6f8a2e4b9d (UUID)

Konfiguration:

- Token-Format: UUID, zufällig alphanumerisch oder benutzerdefiniertes Format
- Token-Länge: Fest oder variabel
- Zeichensatz: Alphanumerisch, base64, hex
- Eindeutigkeitsgarantie: Kryptografische Zufälligkeit oder sequenziell mit grossem Namensraum
```

**Anwendungsfälle**:

- Interne Identifikatoren, bei denen Format-Erhaltung nicht erforderlich
- API-Schlüssel, Session-Tokens
- Datenbank-Foreign-Keys, wo Format-Unabhängigkeit akzeptabel

## Pseudonymisierungstechniken (DSGVO-Compliance)

**Überblick**: Pseudonymisierung ersetzt direkte Identifikatoren durch Pseudonyme, sodass Daten ohne zusätzliche Informationen (Schlüssel oder Zuordnung), die separat aufbewahrt werden, keine Einzelpersonen identifizieren können. Erfüllt DSGVO-Anforderungen für verarbeitungsrisikominimierte Behandlung.

### Kryptografische Pseudonymisierung

**HMAC-basierte Pseudonymisierung**:

```python
import hmac
import hashlib

def pseudonymisieren(bezeichner, geheimschluessel):
    """
    Pseudonym mittels HMAC-SHA256 generieren
    Deterministisch: Gleiche Eingabe + Schlüssel = Gleiches Pseudonym
    """
    pseudonym = hmac.new(
        key=geheimschluessel.encode(),
        msg=bezeichner.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    return pseudonym

# Beispiel
original_id = "max.mueller@example.com"
geheimschluessel = "organisations-spezifischer-geheimschluessel"  # Separat gespeichert, gemäss A.8.24

pseudonym = pseudonymisieren(original_id, geheimschluessel)
# Ergebnis: "8d3f9c2a1b4e5f6d7c8e9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c"
```

**Eigenschaften**:

- **Deterministisch**: Gleiche Person erhält immer gleiches Pseudonym (ermöglicht Verknüpfung über Datensätze)
- **Nicht umkehrbar** (ohne Schlüssel): Computertechnisch nicht machbar, Original aus Pseudonym zu rekonstruieren
- **Schlüsselmanagement**: Geheimschlüssel muss gemäss Kryptografierichtlinie geschützt werden
- **Format**: Typischerweise Hex-String, base64 oder gekürzter Hash

**Schlüsselbasierte Pseudonymisierung**:

```python
from cryptography.fernet import Fernet

def pseudonymisierungsschluessel_erstellen():
    """Pseudonymisierungsschlüssel generieren (sicher aufbewahren)"""
    return Fernet.generate_key()

def reversibel_pseudonymisieren(bezeichner, schluessel):
    """Pseudonymisierung mit Möglichkeit zur Re-Identifizierung (erfordert Schlüssel)"""
    cipher = Fernet(schluessel)
    pseudonym = cipher.encrypt(bezeichner.encode())
    return pseudonym.decode()

def de_pseudonymisieren(pseudonym, schluessel):
    """Aus Pseudonym re-identifizieren (erfordert Schlüssel und Autorisierung)"""
    cipher = Fernet(schluessel)
    original = cipher.decrypt(pseudonym.encode())
    return original.decode()

# Beispiel
schluessel = pseudonymisierungsschluessel_erstellen()
originalname = "Max Müller"

pseudonym = reversibel_pseudonymisieren(originalname, schluessel)
# Ergebnis: "gAAAAABh3f2k..." (Fernet-Token)

# Re-Identifizierung (wenn autorisiert)
wiederhergestellt = de_pseudonymisieren(pseudonym, schluessel)
# Ergebnis: "Max Müller"
```

**DSGVO-Compliance-Überlegungen**:

- Pseudonymisierungsschlüssel separat von pseudonymisierten Daten gespeichert (anderes System, Zugangskontrolle)
- Re-Identifizierung erfordert explizite Autorisierung über Datenzugang hinaus
- Schlüsselrotation: Plan für periodische Schlüsselrotation erstellen (erfordert Neupseudonymisierung)
- Prüfung: Alle Re-Identifizierungsversuche protokollieren

### Pseudonym-Zuordnungstabellen

**Getrennter Zuordnungsansatz**:

```
Pseudonymisierter Datensatz:
PseudonymID | Alter | Stadt    | Diagnose
PS001       | 45    | Zürich   | Diabetes
PS002       | 32    | Genf     | Hypertonie
PS003       | 58    | Basel    | Keine

Zuordnungstabelle (separat gespeichert, eingeschränkter Zugang):
PseudonymID | EchterName
PS001       | Max Müller
PS002       | Anna Meier
PS003       | Thomas Koch
```

**Konfiguration**:

- Speicherungstrennung: Zuordnungstabelle in separater Datenbank/System
- Zugangskontrolle: Unterschiedliche Berechtigungen für pseudonymisierte Daten vs. Zuordnung
- Verschlüsselung: Zuordnungstabelle bei Ruhezustand verschlüsselt
- Prüfung: Alle Zugriffe auf Zuordnungstabelle protokolliert

**Vorteile**:

- Einfache Implementierung
- Leichte Verwaltung der Zuordnung
- Klare Trennung von identifizierten/de-identifizierten Daten

**Nachteile**:

- Zuordnungstabelle ist hochwertiges Angriffsziel
- Sicherungskomplexität (Zuordnung separat sichern)
- Skalierbarkeitsbedenken bei grossen Datensätzen

### k-Anonymität und l-Diversität

**k-Anonymität**:

Sicherstellen, dass jede Kombination von Quasi-Identifikatoren mindestens k-mal vorkommt:

```
Originaldaten:
Alter | PLZ   | Diagnose
25    | 8001  | Grippe
26    | 8002  | Diabetes
27    | 8001  | Hypertonie

k-Anonymität (k=2) generalisiert:
Altersbereich | PLZ-Bereich | Diagnose
20-30         | 8000-8099   | Grippe
20-30         | 8000-8099   | Diabetes
20-30         | 8000-8099   | Hypertonie

Ergebnis: Jede Altersbereich + PLZ-Bereich-Kombination erscheint mindestens 2x
```

**Generalisierungstechniken**:

- Alter: Genaues Alter → Altersbereiche (20-30, 30-40 etc.)
- PLZ: 4-stellige PLZ → 2-stelliges PLZ-Präfix
- Datum: Genaues Datum → Monat oder Quartal
- Einkommen: Genauer Betrag → Einkommensklassen

**l-Diversität**:

k-Anonymität erweitern, um sicherzustellen, dass sensitive Merkmale innerhalb jeder Äquivalenzklasse divers sind:

```
k-Anonymität (k=3) aber nicht l-divers:
Altersbereich | PLZ-Bereich | Diagnose
20-30         | 8000-8099   | Diabetes
20-30         | 8000-8099   | Diabetes
20-30         | 8000-8099   | Diabetes
Problem: Alle Datensätze haben gleiches sensitives Merkmal (Diabetes)

l-Diversität (l=2):
Altersbereich | PLZ-Bereich | Diagnose
20-30         | 8000-8099   | Diabetes
20-30         | 8000-8099   | Grippe
20-30         | 8000-8099   | Hypertonie
Lösung: Mindestens 2 verschiedene sensitive Merkmale in der Gruppe
```

**Beispiele für Implementierungstools** (herstellerneutral):

- ARX Data Anonymization Tool (Open Source)
- Amnesia (Open Source)
- IBM InfoSphere Optim Data Privacy
- Microsoft Azure Data Catalog (Datenklassifizierungsfunktionen)

## Anonymisierungstechniken (irreversibel)

**Überblick**: Anonymisierung entfernt Identifizierungsinformationen irreversibel, sodass Re-Identifizierung auch mit zusätzlichen Daten nicht möglich ist. Anonymisierte Daten sind unter der DSGVO keine Personendaten mehr.

### Aggregation und statistische Offenlegungskontrolle

**Aggregation**:

```
Originalmikrodaten (individuelle Datensätze):
Mitarbeiter | Alter | Gehalt
Max         | 35    | 90'000
Anna        | 42    | 98'000
Thomas      | 38    | 95'000

Aggregierte Daten (anonym):
Altersbereich | Mitarbeiteranzahl | Durchschnittsgehalt
30-40         | 3                 | 94'333

Ergebnis: Einzelpersonen nicht identifizierbar, Datennützlichkeit für Analyse erhalten
```

**Mindestgruppengrösse**:

```
Konfiguration:

- k-Anonymität: Mindestens 5-10 Personen pro Gruppe (regulatorischer Standard)
- Unterdrückung: Gruppen kleiner als k werden unterdrückt oder zusammengeführt
```

**Rundung und Perturbation**:

```
Originaldurchschnitt: 94'333.33
Gerundet: 94'000 (auf nächste 1'000)
Perturbriert: 94'000 ± zufälliges Rauschen

Konfiguration:

- Rundungsebene: 100er, 1'000er, 10'000er
- Rauschverteilung: Gleichmässig, Gauss'sch
- Abwägung: Mehr Rundung/Rauschen = weniger Nützlichkeit, höhere Privatsphäre
```

### Datenunterdrückung

**Zellenunterdrückung**:

```
Originaldaten mit seltenen Kombinationen:
Alter | Ort        | Diagnose
25    | Willisau   | Seltene Krankheit X  ← Nur 1 Person, hohes Re-Identifizierungsrisiko

Unterdrückt:
Alter | Ort        | Diagnose
*     | Willisau   | *                    ← Unterdrückt zum Schutz der Identität
```

**Konfiguration**:

- Unterdrückungsschwellenwert: Typischerweise k < 5 löst Unterdrückung aus
- Primäre Unterdrückung: Direkte Unterdrückung verletzender Zellen
- Sekundäre Unterdrückung: Zusätzliche Zellen zur Verhinderung von Inferenz

---

# Datenentdeckungsmethodiken

## Automatisierte Mustererkennung

**Reguläre-Ausdrücke-Scanning**:

```python
# Beispielmuster für die Erkennung sensitiver Daten

MUSTER = {
    'kreditkarte': r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13})\b',
    'ahv': r'\b756\.\d{4}\.\d{4}\.\d{2}\b',
    'iban': r'\b[A-Z]{2}\d{2}[A-Z0-9]{1,30}\b',
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'telefon': r'\b(?:\+?\d{1,3}[-.]?)?\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b',
    'ip_adresse': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
}

def spalte_nach_mustern_durchsuchen(spaltendaten, stichprobengrösse=1000):
    """Spaltendaten auf sensitive Datenmuster durchsuchen"""
    ergebnisse = {}
    stichprobe = spaltendaten.sample(min(stichprobengrösse, len(spaltendaten)))

    for mustername, muster in MUSTER.items():
        treffer = stichprobe.str.contains(muster, regex=True, na=False)
        trefferquote = (treffer.sum() / len(stichprobe)) * 100

        if trefferquote > 10:  # >10% Treffer deutet auf diesen Datentyp hin
            ergebnisse[mustername] = trefferquote

    return ergebnisse
```

**Named Entity Recognition (NER)**:

```python
# Beispiel mit NLP zur PII-Erkennung

import spacy

nlp = spacy.load("de_core_news_sm")  # Deutsches Sprachmodell

def pii_entitaeten_erkennen(textdaten):
    """NER zur Erkennung von Personennamen, Organisationen, Standorten verwenden"""
    doc = nlp(textdaten)

    entitaeten = {
        'PERSON': [],
        'ORG': [],
        'GPE': [],  # Geopolitische Entitäten (Länder, Städte)
        'DATE': [],
    }

    for ent in doc.ents:
        if ent.label_ in entitaeten:
            entitaeten[ent.label_].append(ent.text)

    return entitaeten
```

## Datenbank-Metadaten-Analyse

**Spaltenname-Heuristik**:

```python
# Indikatoren für sensitive Daten in Spaltennamen

SENSITIVE_SCHLUESSELWÖRTER = {
    'PII': ['name', 'vorname', 'nachname', 'email', 'telefon', 'adresse',
            'ahv', 'pass', 'ausweis', 'geburtsdatum', 'geburt'],
    'Finanzdaten': ['karte', 'konto', 'iban', 'swift', 'bankleitzahl', 'guthaben',
                   'gehalt', 'einkommen', 'zahlung', 'kredit'],
    'Gesundheitsdaten': ['medizin', 'diagnose', 'verschreibung', 'patient', 'gesundheit',
                        'versicherung', 'behandlung', 'zustand'],
    'Zugangsdaten': ['passwort', 'geheimnis', 'token', 'schluessel', 'anmeldedaten',
                    'apikey', 'privat'],
}

def spalte_nach_name_klassifizieren(spaltenname):
    """Spalte anhand des Namens klassifizieren"""
    spalte_klein = spaltenname.lower()

    for kategorie, schluesselwörter in SENSITIVE_SCHLUESSELWÖRTER.items():
        if any(sw in spalte_klein for sw in schluesselwörter):
            return kategorie

    return 'Unbekannt'
```

## Datenprofiling und statistische Analyse

**Verteilungsanalyse**:

```python
def spalte_profilieren(spaltendaten):
    """Spalteneigenschaften analysieren"""
    profil = {
        'zeilenanzahl': len(spaltendaten),
        'nullanzahl': spaltendaten.isnull().sum(),
        'eindeutiganzahl': spaltendaten.nunique(),
        'datentyp': str(spaltendaten.dtype),
        'eindeutigkeitsquote': spaltendaten.nunique() / len(spaltendaten),
    }

    # Hohe Eindeutigkeit deutet auf Identifikatoren oder PII hin
    if profil['eindeutigkeitsquote'] > 0.95:
        profil['wahrscheinlich_identifikator'] = True

    # Beispielwerte (zur manuellen Überprüfung — niemals echte Werte protokollieren!)
    profil['beispielstruktur'] = [
        len(str(v)) for v in spaltendaten.dropna().head(10)
    ]

    return profil
```

## Datenentdeckungs-Tools (herstellerneutrale Kategorien)

**Datenbank-Scanning-Tools**:

- Cloud-nativ: Azure Purview, AWS Macie, Google Cloud DLP API
- On-Premises: IBM InfoSphere, Informatica Data Privacy Management
- Open Source: DataHub, Amundsen, Apache Atlas

**Applikationsebenen-Scanning**:

- API-Scanning: API-Antworten auf sensitive Daten prüfen
- Protokolldatei-Scanning: Protokolle auf versehentliche PII-Offenlegung durchsuchen
- Konfigurations-Scanning: Hartcodierte Zugangsdaten erkennen

---

# Maskierungs-Tool-Landschaft (herstellerneutral)

## Tool-Fähigkeitsmatrix

| Fähigkeit | Datenbank-nativ | Dedizierte Maskierungs-Tools | ETL-Tools | Applikationsebene |
|-----------|-----------------|------------------------------|-----------|-------------------|
| **Statische Datenmaskierung** | Begrenzt | Ausgezeichnet | Gut | Begrenzt |
| **Dynamische Datenmaskierung** | Gut | Ausgezeichnet | Nein | Ausgezeichnet |
| **Format-Erhaltung** | Begrenzt | Ausgezeichnet | Gut | Begrenzt |
| **Referenzielle Integrität** | Gut | Ausgezeichnet | Ausgezeichnet | Manuell |
| **Leistung** | Ausgezeichnet | Gut | Gut | Variiert |
| **Lernkurve** | Niedrig | Mittel | Hoch | Hoch |
| **Kosten** | Niedrig (eingebaut) | Hoch | Mittel | Niedrig (Entwicklungsaufwand) |

## Implementierungsarchitekturen

**Datenbank-natives DDM**:

```
Architektur:
Benutzer → Applikation → Datenbank (mit DDM) → Maskierte Daten zurückgegeben

Vorteile:

- Zentralisierte Durchsetzung
- Keine Applikationsänderungen erforderlich
- Leistungsoptimiert

Nachteile:

- Datenbankspezifische Implementierung
- Kann Abfrageoptimierung beeinträchtigen
- Begrenzte Maskierungslogik
```

**Proxy-basierte Maskierung**:

```
Architektur:
Benutzer → Applikation → Maskierungs-Proxy → Datenbank → Proxy wendet Maskierung an

Vorteile:

- Datenbankagnostisch
- Zentralisiertes Richtlinienmanagement
- Kann mehrere Datenbanken maskieren

Nachteile:

- Zusätzliche Infrastruktur erforderlich
- Leistungsoverhead
- Single Point of Failure (wenn kein HA)
```

---

# Kurzreferenzhandbücher

## Technikauswahl-Entscheidungsbaum

```
START: Sensitive Daten maskieren

F1: Ist Datennützlichkeit in der maskierten Umgebung erforderlich?
    NEIN → Verwenden: Schwärzung/Nullung (einfachste Methode)
    JA → Weiter

F2: Muss die Maskierung reversibel sein?
    JA → F2a: Wer muss umkehren?

        - Nur autorisierte Benutzer → Verwenden: Tokenisierung oder Pseudonymisierung
        - Applikation benötigt referenzielle Integrität → Verwenden: Tokenisierung

    NEIN → Weiter

F3: Ist dies für Produktionszugriffskontrolle?
    JA → Verwenden: Dynamische Datenmaskierung (DDM)
    NEIN → Weiter (Nicht-Produktions-Verwendung)

F4: Muss referenzielle Integrität über Tabellen erhalten bleiben?
    JA → Verwenden: Deterministische Statische Datenmaskierung (SDM) mit konsistentem Algorithmus
    NEIN → Verwenden: Zufällige Statische Datenmaskierung (SDM)

F5: Regulatorische Anforderung (DSGVO, PCI DSS, HIPAA)?

    - DSGVO-Pseudonymisierung → Verwenden: Kryptografische Pseudonymisierung
    - PCI-DSS-Maskierung → Verwenden: Tokenisierung oder Format-erhaltendes SDM
    - HIPAA-De-Identifizierung → Verwenden: Anonymisierung (Safe Harbor oder Expert Determination)
    - Keine → Verwenden: SDM mit Substitution
```

## Häufige Maskierungsszenarien

**Szenario 1: Testdatenbank aus Produktion**

```
Problem: Realistische Testdaten ohne PII-Offenlegung benötigt

Lösung:
1. Produktionsschema und Daten exportieren
2. Statische Datenmaskierung (SDM) anwenden:

   - Namen: Durch Fantasienamen ersetzen (deterministisch für Konsistenz)
   - E-Mails: Format-erhaltende Substitution
   - Adressen: Durch fiktive, aber gültige Adressen ersetzen
   - Telefonnummern: Format-erhaltende Zufallsziffern
   - Daten: Um konsistenten zufälligen Versatz pro Person verschieben

3. Referenzielle Integrität validieren
4. In Testumgebung laden
5. Maskierungswirksamkeit testen

Tools: Datenbankexport-Tools + SDM-Tool (kommerziell oder benutzerdefinierte Skripte)
Zeitaufwand: 1-2 Tage für Ersteinrichtung, danach automatisiert
```

**Szenario 2: Analyse mit PII-Schutz**

```
Problem: Business Intelligence benötigt aggregierte Daten ohne Einzelpersonenidentifizierung

Lösung:
1. Identifikatoren pseudonymisieren (kunden_id, email)
2. Quasi-Identifikatoren generalisieren (alter → altersbereich, PLZ → PLZ-Präfix)
3. Sensitive Metriken aggregieren (einzelumsatz → segmentumsatz)
4. k-Anonymität implementieren (k=5 minimum)
5. Seltene Kombinationen entfernen oder unterdrücken

Tools: ETL-Tools mit Maskierungsfähigkeiten, Python/R-Skripte
Validierung: Re-Identifizierungsrisikobeurteilung
```

**Szenario 3: Produktionszugang für Kundensupport**

```
Problem: Supportmitarbeiter benötigen Kundendaten, aber nicht vollständige PII

Lösung:
1. Dynamische Datenmaskierung (DDM) in Produktionsdatenbank implementieren
2. Rollenbasierte Regeln konfigurieren:

   - Support: Teilweise E-Mail anzeigen (ma***@example.com), letzte 4 Ziffern Telefon
   - Vorgesetzte: Vollständige E-Mail, vollständiges Telefon
   - Admin: Alle nicht maskierten Daten

3. Alle Zugriffe auf sensitive Felder protokollieren
4. Auf Bypass-Versuche überwachen

Tools: Datenbank-natives DDM oder Maskierungs-Proxy
Compliance: DSGVO-Zugangsprotokollierungsanforderungen
```

## Fehlerbehebungsanleitung

**Problem: Maskierte Daten brechen Applikationslogik**

```
Problem: Applikationsvalidierung schlägt bei maskierten Daten fehl
Ursache: Maskierte Daten entsprechen nicht erwartetem Format oder Einschränkungen

Lösungen:

- Format-erhaltende Maskierungstechniken verwenden
- Validierungsregeln anpassen, um maskierte Formate zu akzeptieren
- Realistische Substitutionsdaten verwenden, die Validierung bestehen
- Maskierte Daten vor Bereitstellung in Test gegen Applikation testen
```

**Problem: Referenzielle Integritätsverletzungen nach Maskierung**

```
Problem: Foreign Keys zeigen nach Maskierung auf nicht existierende Datensätze
Ursache: Nicht-deterministische Maskierung oder unvollständige Maskierung verwandter Tabellen

Lösungen:

- Deterministische Maskierung verwenden (gleiche Eingabe → gleiche Ausgabe)
- Alle verwandten Tabellen zusammen maskieren
- FK-Beziehungszuordnung während Maskierung aufrechterhalten
- Referenzielle Integrität nach Maskierung validieren
```

**Problem: Leistungsbeeinträchtigung durch DDM**

```
Problem: Abfragen verlangsamen sich signifikant nach Aktivierung von DDM
Ursache: Maskierungsfunktionen verhindern Indexnutzung, zusätzlicher Verarbeitungsoverhead

Lösungen:

- Maskierungsfunktionen optimieren (gecacht, wo möglich indiziert)
- Abfrageausführungspläne überprüfen
- Stattdessen statische Maskierung für Nicht-Produktion in Betracht ziehen
- Caching-Schicht für häufig zugegriffene maskierte Daten implementieren
- Materialisierte Views mit vorgemaskierten Daten verwenden
```

## Compliance-Checkliste

**PCI DSS-Maskierungsanforderungen (Req. 3.4-3.5)**:

- [ ] Primary Account Number (PAN) bei Anzeige maskiert (max. erste 6 + letzte 4 Ziffern)
- [ ] PAN in nicht produktiven Umgebungen unleserlich (Maskierung, Kürzung oder Tokenisierung)
- [ ] CVV2/CVC2 niemals gespeichert (Maskierung nicht anwendbar — darf nicht gespeichert werden)
- [ ] Maskierungslösung verhindert nicht autorisierten Zugang zu nicht maskierter PAN
- [ ] Dokumentierte Maskierungsverfahren und -standards
- [ ] Jährliche Validierung der Maskierungswirksamkeit

**DSGVO-Pseudonymisierung (Art. 32, 89)**:

- [ ] Pseudonymisierungsschlüssel separat von pseudonymisierten Daten gespeichert
- [ ] Re-Identifizierung erfordert zusätzliche dem Datenverarbeiter nicht verfügbare Informationen
- [ ] Technische und organisatorische Massnahmen verhindern nicht autorisierte Re-Identifizierung
- [ ] Pseudonymisierung in Datenschutz-Folgenabschätzung (DSFA) dokumentiert
- [ ] Regelmässige Überprüfung der Pseudonymisierungswirksamkeit
- [ ] Betroffene Personen über Pseudonymisierung informiert, wo anwendbar

**HIPAA-De-Identifizierung (§164.514)**:

- [ ] Safe-Harbor-Methode: Alle 18 HIPAA-Identifikatoren entfernt, ODER
- [ ] Expert Determination: Statistische Verifikation durch qualifizierten Experten
- [ ] Kein tatsächliches Wissen über Re-Identifizierungsmöglichkeit
- [ ] Re-Identifizierungscode (falls erforderlich) separat gespeichert
- [ ] Dokumentation der De-Identifizierungsmethode und Validierung
- [ ] Periodische Neubewertung der De-Identifizierungswirksamkeit

---

# Implementierungs-Best-Practices

## Maskierungs-Prozess-Workflow

```
1. ENTDECKEN
   ├─ Systeme und Datenbanken inventarisieren
   ├─ Auf sensitive Datenmuster scannen
   ├─ Daten nach Sensitivität klassifizieren
   └─ Regulatorische Anforderungen identifizieren

2. ENTWERFEN
   ├─ Geeignete Maskierungstechniken auswählen
   ├─ Maskierungsregeln pro Datenelement definieren
   ├─ Aufrechterhaltung referenzieller Integrität planen
   └─ Maskierungsspezifikationen dokumentieren

3. ENTWICKELN/KONFIGURIEREN
   ├─ Maskierungs-Tool konfigurieren oder Skripte entwickeln
   ├─ Maskierungsalgorithmen implementieren
   ├─ Token-Vaults einrichten (bei Tokenisierung)
   └─ Maskierungsausführungs-Workflows erstellen

4. TESTEN
   ├─ Maskierungswirksamkeit validieren (Originaldaten nicht vorhanden)
   ├─ Referenzielle Integrität testen (Joins funktionieren korrekt)
   ├─ Applikationskompatibilität verifizieren (Apps funktionieren mit maskierten Daten)
   ├─ Leistungstests (akzeptabler Overhead)
   └─ Re-Identifizierungstests (Original nicht wiederherstellbar)

5. DEPLOYEN
   ├─ Initiale Maskierung ausführen (SDM) oder Regeln aktivieren (DDM)
   ├─ Deployment-Erfolg validieren
   ├─ Auf Fehler und Leistung überwachen
   └─ Deployment dokumentieren

6. ÜBERWACHEN & WARTEN
   ├─ Periodische Wirksamkeitstests
   ├─ Auf Offenlegung nicht maskierter Daten überwachen
   ├─ Maskierungsregeln für neue Datentypen aktualisieren
   ├─ Jährliche Compliance-Validierung
   └─ Vorfallreaktion bei Maskierungsfehlern
```

## Häufige Fallstricke vermeiden

**Fallstrick 1: Nur „offensichtliche" PII maskieren**

```
Fehler: Name, E-Mail, Telefon maskieren, aber ignorieren...

- Benutzername (oft gleich wie E-Mail)
- Kommentar-/Notizfelder (können Freitext-PII enthalten)
- Protokolldateien (können sensitive Daten protokollieren)
- Sicherungs-/Archivsysteme (vergessene Umgebungen)

Lösung: Umfassende Datenentdeckung über ALLE Systeme und Formate
```

**Fallstrick 2: Inkonsistente Maskierung über Umgebungen**

```
Fehler: Entwicklungsumgebung maskiert, aber QA-Umgebung hat nicht maskierte Kopie
Ergebnis: Sensitive Daten immer noch offengelegt, Compliance-Verletzung

Lösung: Automatisierte Maskierung in Datenprovisionierungs-Pipeline, keine manuellen Ausnahmen
```

**Fallstrick 3: „Später maskieren"-Mentalität**

```
Fehler: Produktion in Nicht-Produktion kopieren, Maskierung „wenn Zeit da ist" planen
Ergebnis: Nicht maskierte sensitive Daten wochenlang/monatelang in Nicht-Produktion

Lösung: Maskierung als Teil des Datenkopier-Prozesses, keine nicht maskierten Daten in Nicht-Produktion
```

**Fallstrick 4: Nur Client-seitige Maskierung**

```
Fehler: JavaScript maskiert Daten in UI, aber Backend gibt vollständige nicht maskierte Daten zurück
Ergebnis: Trivial zu umgehen durch Anzeige des Netzwerkverkehrs

Lösung: Maskierung serverseitig durchsetzen (Datenbank- oder Applikationsebene)
```

---

# Glossar technischer Begriffe

**Format-Preserving Encryption (FPE)**: Verschlüsselung, die das Format der Originaldaten beibehält (z.B. verschlüsselte Kreditkartennummer sieht immer noch wie eine Kreditkartennummer aus).

**Luhn-Algorithmus**: Prüfsummenformel für Kreditkartenvalidierung. Format-erhaltende Maskierung von Kreditkarten sollte Luhn-Gültigkeit aufrechterhalten.

**Quasi-Identifikator**: Merkmal, das Einzelpersonen in Kombination mit anderen Merkmalen identifizieren kann (Alter + PLZ + Geschlecht).

**Re-Identifizierungsangriff**: Versuch, die ursprüngliche Identität einer Person aus maskierten, pseudonymisierten oder anonymisierten Daten durch Verknüpfung, Inferenz oder statistische Analyse zu rekonstruieren.

**Salt (kryptografisch)**: Zufällige Daten, die vor dem Hashing/Verschlüsseln zur Eingabe hinzugefügt werden, um Rainbow-Table-Angriffe zu verhindern und eindeutige Ausgaben auch bei identischen Eingaben sicherzustellen.

**Token-Vault**: Gesicherte Datenbank, die in Tokenisierungssystemen die Zuordnung zwischen Tokens und ursprünglichen sensitiven Werten speichert.

---

**ENDE DER TECHNISCHEN REFERENZ**

**Dokumentstatus**: Lebendes Dokument — wird aktualisiert, wenn sich Maskierungstechnologien, -techniken und Best Practices weiterentwickeln.

**Feedback**: Technische Korrekturen, Ergänzungen oder Verbesserungen sollten dem Security Architecture-Team zur Überprüfung und Einarbeitung eingereicht werden.

**Erinnerung**: Dieses Dokument ist KEIN ISMS-Dokument. Verbindliche Anforderungen sind in ISMS-POL-A.8.11 (Richtlinie zur Datenmaskierung) definiert.

**DIESES DOKUMENT IST NICHT BESTANDTEIL DES ISMS.**

<!-- QA_VERIFIED: 2026-03-28 -->
