<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.16-IT:framework:POL:a.8.16 -->
**ISMS-POL-A.8.16 — Attività di monitoraggio**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Attività di monitoraggio |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.16 |
| **Autore del documento** | RSSI |
| **Proprietario del documento** | AD |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DSI → SOC Lead → Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.8.15 (Registrazione); ISMS-POL-A.5.24-28 (Gestione degli incidenti); ISMS-IMP-A.8.16.1–4-UG/TG; ISO/IEC 27001:2022 Controllo A.8.16.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per le attività di monitoraggio per rilevare comportamenti anomali e potenziali incidenti di sicurezza delle informazioni, conformemente al Controllo A.8.16 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutte le reti, i sistemi e le applicazioni dove il monitoraggio è tecnicamente fattibile; tutti gli utenti (dipendenti, appaltatori, account di servizio); e tutte le tecnologie di monitoraggio indipendentemente dal fornitore o dal modello di dispiegamento.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Controllo ISO/IEC 27001:2022 A.8.16

> *Le reti, i sistemi e le applicazioni devono essere monitorati per identificare comportamenti anomali e adottare le misure appropriate per valutare i potenziali incidenti di sicurezza delle informazioni.*

**Obiettivo del controllo**: Rilevare i comportamenti anomali, le minacce attive e i potenziali incidenti di sicurezza attraverso il monitoraggio continuo e la correlazione degli eventi, consentendo una risposta tempestiva.

---

# Enunciati di politica

## Infrastruttura di monitoraggio

[Organizzazione] DEVE implementare un'infrastruttura di monitoraggio centralizzata basata su SIEM.

**Requisiti del SIEM**: Raccolta dei log da tutte le sorgenti critiche (per ISMS-POL-A.8.15); correlazione degli eventi in tempo reale; avvisi automatici per i casi d'uso di sicurezza; dashboard per la visibilità operativa; conservazione dei log per almeno 12 mesi online.

**Disponibilità**: Il SIEM DEVE avere un'uptime di disponibilità del ≥99,5% (misurato mensilmente); i guasti del SIEM DEVONO essere trattati come incidenti di sicurezza Alti e richiedono il rimedio entro 4 ore.

## Casi d'uso obbligatori del monitoraggio

[Organizzazione] DEVE implementare il rilevamento per almeno i seguenti scenari:

**Autenticazione e accesso**: Tentativi di accesso falliti multipli (soglia: 5 in 10 minuti); accesso da ubicazioni geograficamente anomale; accesso fuori dall'orario normale per account privilegiati; accesso ai sistemi critici al di fuori dei modelli stabiliti.

**Minacce agli endpoint**: Rilevamento di malware e avvisi EDR; modifiche non autorizzate ai file di sistema; esecuzione di processi sospetti; attività di ricognizione della rete.

**Rete e infrastruttura**: Scansione delle porte e attività di ricognizione; grandi trasferimenti di dati verso destinazioni esterne; comunicazione C2 (Command and Control); modifica delle regole del firewall o delle policy di sicurezza.

**Privilegi e accesso ai dati**: Escalation dei privilegi; utilizzo degli account di emergenza; accesso in blocco ai dati sensibili; modifica delle credenziali degli account privilegiati.

## Tempistiche di risposta agli avvisi

| Livello di avviso | Tempo di riconoscimento | Tempo di triage | Azione |
|------------------|------------------------|-----------------|--------|
| **Critico** | 15 minuti (24/7) | 30 minuti | Avviare la risposta agli incidenti immediatamente |
| **Alto** | 30 minuti (ore lavorative); 1 ora (fuori orario) | 2 ore | Indagare e contenere |
| **Medio** | 4 ore (ore lavorative) | 8 ore | Indagare e documentare |
| **Basso** | 1 giorno lavorativo | 3 giorni lavorativi | Revisione e documentazione |

**Gestione dei falsi positivi**: Il tasso di falsi positivi degli avvisi DEVE essere monitorato; l'obiettivo è <20% di falsi positivi per gli avvisi Critici/Alti; le regole devono essere messe a punto mensilmente per ridurre il rumore degli avvisi.

## Linea di base del comportamento

[Organizzazione] DEVE stabilire linee di base del comportamento normale per rilevare le anomalie.

**Linee di base obbligatorie**: Orari di accesso normali per utente e ruolo; accesso tipico alle risorse per funzione lavorativa; modelli di traffico di rete normali per segmento; utilizzo abituale delle risorse di sistema. **Aggiornamento**: Le linee di base DEVONO essere riviste e aggiornate trimestralmente.

## Copertura del monitoraggio

**Obiettivi di copertura**:

| Tipo di sistema | Copertura del monitoraggio obiettivo |
|----------------|--------------------------------------|
| Sistemi di produzione critici | 100% |
| Tutti i sistemi di produzione | ≥95% |
| Ambienti non di produzione | ≥80% |
| Endpoint | ≥90% |

**Lacune di copertura**: Le lacune identificate DEVONO essere documentate; rimedio richiesto entro 30 giorni per i sistemi critici, 90 giorni per i sistemi standard.

## Monitoraggio e privacy

Il monitoraggio DEVE essere condotto nel rispetto della privacy dei dipendenti: i dipendenti DEVONO essere informati delle attività di monitoraggio (avviso relativo alla privacy); il monitoraggio DEVE essere limitato a scopi legittimi di sicurezza; l'accesso ai dati di monitoraggio DEVE essere limitato su base need-to-know; il RPD DEVE rivedere le nuove funzionalità di monitoraggio prima dell'implementazione.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approva i casi d'uso del monitoraggio; supervisione degli incidenti critici |
| **SOC** | Monitoraggio 24/7; triage e risposta agli avvisi; ricerca delle minacce |
| **Responsabile Sicurezza Informatica** | Definizione delle regole di rilevamento; ottimizzazione delle prestazioni del SIEM |
| **Operazioni IT** | Infrastruttura SIEM e manutenzione; integrazione delle sorgenti di log |
| **RPD** | Revisione della conformità del monitoraggio alla privacy |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce i requisiti per le attività di monitoraggio. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.16 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
