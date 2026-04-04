<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.15-IT:framework:POL:a.8.15 -->
**ISMS-POL-A.8.15 — Politica di registrazione (Logging)**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Politica di registrazione |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.15 |
| **Autore del documento** | RSSI |
| **Proprietario del documento** | AD |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → Responsabile Sicurezza Informatica → SOC Lead / Responsabile Operazioni IT → RPD → Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.15.1–4-UG/TG; ISMS-REF-A.8.15; ISMS-POL-A.8.16; ISMS-POL-A.8.17; ISMS-POL-A.5.24; ISO/IEC 27001:2022 Controllo A.8.15.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la registrazione degli eventi per supportare il rilevamento degli incidenti, le indagini forensi, gli obblighi di conformità e la responsabilità, conformemente al Controllo A.8.15 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutti i sistemi che generano eventi di sicurezza rilevanti (server, dispositivi di rete, applicazioni, servizi cloud, endpoint, sistemi di sicurezza), indipendentemente dall'ambiente (produzione, non produzione) o dalla piattaforma.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Controllo ISO/IEC 27001:2022 A.8.15

> *I log che registrano le attività degli utenti, le eccezioni, gli errori e gli eventi di sicurezza delle informazioni devono essere prodotti, archiviati, protetti e analizzati.*

**Obiettivo del controllo**: Garantire la registrazione sistematica degli eventi di sicurezza per consentire il rilevamento degli incidenti, le indagini forensi, la risposta agli incidenti e la dimostrazione della conformità normativa.

---

# Enunciati di politica

## Sorgenti di log obbligatorie

[Organizzazione] DEVE raccogliere i log dalle seguenti categorie di sorgenti:

**Infrastruttura**: Server (sistema operativo, eventi di sicurezza, accessi); dispositivi di rete (firewall, router, switch, bilanciatori di carico); infrastruttura cloud (log dei servizi cloud, log IAM, log dell'infrastruttura); sistemi di archiviazione (accessi, modifiche dei permessi).

**Sicurezza**: Sistemi SIEM; soluzioni EDR/anti-malware; sistemi IAM (eventi di autenticazione, modifiche dei permessi); DLP; sistemi di controllo degli accessi fisici.

**Applicazioni**: Applicazioni aziendali critiche (eventi di autenticazione, operazioni sui dati sensibili); applicazioni web (richieste di accesso, errori, anomalie); database (accessi, modifiche ai dati, escalation dei privilegi); API (autenticazione, errori, anomalie della velocità).

## Contenuto minimo dei log

Ogni voce di log DEVE includere: timestamp (UTC); identità dell'utente/account; indirizzo IP sorgente; azione eseguita; risorsa o oggetto interessato; risultato (successo/fallimento); nome del sistema o dell'applicazione.

## Raccolta centralizzata e protezione dei log

**SIEM centralizzato**: Tutti i log delle sorgenti critiche DEVONO essere inoltrati a un SIEM centralizzato; il SIEM DEVE essere ridondante e ad alta disponibilità; latenza massima di raccolta dei log: 5 minuti.

**Protezione dell'integrità dei log**: I log NON DEVONO essere modificabili dagli utenti standard; l'integrità DEVE essere applicata tramite: archiviazione solo in aggiunta (append-only); firme crittografiche; controllo degli accessi basato sui ruoli per i log (accesso in sola lettura per la maggior parte degli utenti); pista di audit delle modifiche ai log stessi.

## Periodi di conservazione

| Categoria di log | Periodo minimo | Base normativa |
|-----------------|----------------|----------------|
| Log di autenticazione (successo e fallimento) | 12 mesi | ISO 27001, GDPR |
| Log di accesso agli asset | 12 mesi | ISO 27001 |
| Log degli eventi di sicurezza (SIEM) | 12 mesi | ISO 27001, DORA |
| Log di accesso alle applicazioni | 6 mesi | Requisiti operativi |
| Log degli accessi con privilegi | 24 mesi | PCI DSS, FINMA |
| Log degli errori di sistema | 90 giorni | Requisiti operativi |

**Estensioni normative**: PCI DSS — 12 mesi minimi con 3 mesi immediatamente disponibili; DORA — fino a 5 anni per gli istituti finanziari UE.

## Analisi e revisione dei log

**Analisi automatizzata**: Il SIEM DEVE eseguire la correlazione degli eventi e il rilevamento delle anomalie in tempo reale; i casi d'uso obbligatori includono: tentativi di autenticazione multipli falliti; accesso fuori orario; esfiltrazione di dati; utilizzo di account privilegiati; modifiche al sistema.

**Revisione manuale**: Revisione quotidiana degli avvisi ad alta priorità dal SIEM; revisione settimanale dei trend e dei modelli degli avvisi; revisione mensile delle anomalie e delle tendenze a lungo termine.

## Privacy nella registrazione

I log DEVONO essere raccolti nel rispetto della privacy: i log che contengono DCP DEVONO essere minimizzati al necessario; l'accesso ai log è limitato su base need-to-know; la conservazione dei log che contengono DCP non DEVE superare i requisiti necessari; i dipendenti DEVONO essere informati sui tipi di log raccolti (avvisi relativi alla privacy).

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; definizione dei requisiti di registrazione |
| **Responsabile Sicurezza Informatica** | Definizione delle sorgenti di log obbligatorie; supervisione dell'analisi dei log |
| **SOC** | Monitoraggio e analisi in tempo reale dei log; risposta agli incidenti |
| **Operazioni IT** | Implementazione e manutenzione dell'infrastruttura di registrazione |
| **RPD** | Supervisione della privacy nella registrazione; conformità RGPD/nLPD |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **RPD** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce i requisiti di registrazione. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.15 (UG/TG). Il riferimento tecnico è in ISMS-REF-A.8.15.*

<!-- QA_VERIFIED: 2026-04-03 -->
