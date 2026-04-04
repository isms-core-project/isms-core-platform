<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.9-IT:framework:POL:a.8.9 -->
**ISMS-POL-A.8.9 — Gestione della configurazione**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Gestione della configurazione |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.9 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DSI → DT → Responsabile della Configurazione → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.9.1–4-UG/TG; ISMS-CTX-A.8.9 (Riferimento tecnico — NON SGSI); ISO/IEC 27001:2022 Controllo A.8.9.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per i controlli di gestione della configurazione, conformemente al Controllo A.8.9 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutti gli asset IT che richiedono la gestione della configurazione (infrastruttura di elaborazione, dispositivi di rete, sistemi di archiviazione, servizi cloud, applicazioni, strumenti di sicurezza, sistemi IoT/OT) in tutti gli ambienti (produzione, non produzione, cloud, on-premise) e in tutte le fasi del ciclo di vita (dispiegamento, operazione, cambio, disattivazione).

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE (dove applicabile); ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Controllo ISO/IEC 27001:2022 A.8.9

> *«Le configurazioni, incluse le configurazioni di sicurezza, di hardware, software, servizi e reti devono essere stabilite, documentate, implementate, monitorate e riviste.»*

**Obiettivo del controllo**: Stabilire configurazioni di base sicure, prevenire modifiche non autorizzate, rilevare il drift di configurazione, applicare l'hardening della sicurezza e consentire un ripristino rapido pur supportando le operazioni aziendali.

---

# Enunciati di politica

## Basi di configurazione

[Organizzazione] DEVE stabilire e documentare basi di configurazione sicure per tutti gli asset IT nel perimetro.

**Contenuto della base di configurazione**: Configurazioni hardware (firmware, BIOS/UEFI, parametri hardware); configurazioni del sistema operativo (impostazioni di sicurezza, policy, criteri di hardening); configurazioni delle applicazioni (parametri di sicurezza, accesso, registrazione); configurazioni di rete (regole del firewall, ACL, segmentazione); configurazioni cloud (politiche IAM, impostazioni di sicurezza del provider).

**Standard di hardening della sicurezza**: Le basi di configurazione DEVONO allinearsi agli standard del settore: CIS Benchmarks, NIST SP 800-53, guide di hardening del fornitore. Le deviazioni dagli standard del settore DEVONO essere documentate con giustificazione aziendale.

**Frequenza di revisione della base**: Revisione annuale di tutte le basi; revisioni attivate da aggiornamenti di sicurezza, cambiamenti della piattaforma, audit e incidenti.

## Controllo dei cambiamenti di configurazione

Tutte le modifiche alle configurazioni dei sistemi di produzione DEVONO seguire il processo di gestione dei cambiamenti (ISMS-POL-A.8.32).

**Approvazione del cambiamento**: I cambiamenti di configurazione DEVONO avere: richiesta di cambiamento documentata con giustificazione aziendale; impatto valutato sulla sicurezza; test in ambiente non di produzione (dove fattibile); approvazione del Comitato di Approvazione dei Cambiamenti (CAC) per i cambiamenti significativi; piano di rollback documentato.

**Modifiche di emergenza**: Approvazione post-implementazione consentita per i cambiamenti di emergenza; revisione obbligatoria entro 48 ore.

## Monitoraggio della configurazione e rilevamento del drift

[Organizzazione] DEVE implementare il monitoraggio continuo della configurazione.

**Requisiti del monitoraggio**: Scansioni di conformità automatizzate settimanali minime (giornaliere per i sistemi critici); comparazione con le basi approvate documentate; avvisi per i drift rilevati; dashboard di conformità per la visibilità operativa.

**Soglie di risposta al drift**: Sistemi critici — rimedio del drift entro 24 ore; sistemi standard — rimedio entro 7 giorni; i drift non rimediati che superano la soglia richiedono escalation al RSSI.

## Hardening della sicurezza

[Organizzazione] DEVE implementare misure di hardening della sicurezza per tutti i sistemi.

**Requisiti minimi**: Rimozione o disabilitazione dei servizi e degli account non necessari; disabilitazione delle funzionalità predefinite non sicure; applicazione del minimo privilegio per le configurazioni di sistema; cifratura dei dati sensibili archiviati nei file di configurazione; aggiornamento regolare delle configurazioni per affrontare le vulnerabilità note.

## Gestione del database di gestione della configurazione (CMDB)

[Organizzazione] DEVE mantenere un CMDB preciso che contenga: tutti gli asset nel perimetro con attributi di configurazione; relazioni e dipendenze tra gli asset; storico delle versioni di configurazione; proprietario e responsabile dell'asset.

**Accuratezza del CMDB**: Riconciliazione mensile dell'inventario degli asset; accuratezza obiettivo >95%; le discrepanze devono essere risolte entro 30 giorni.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approva le eccezioni; supervisione della conformità |
| **DSI/DT** | Responsabilità complessiva per l'efficacia della gestione della configurazione |
| **Responsabile della Configurazione** | Coordinamento quotidiano; gestione del CMDB; tracciamento della conformità |
| **Operazioni IT** | Implementazione e applicazione delle basi; dispiegamento dei cambiamenti |
| **Operazioni di Sicurezza** | Monitoraggio della sicurezza; indagine sulle modifiche di configurazione non autorizzate |
| **Proprietari dei sistemi** | Revisione e approvazione delle basi di configurazione per i sistemi di proprietà |

---

# Metriche di conformità

- Copertura della scansione di conformità della configurazione (obiettivo: ≥95%)
- Drift di configurazione risolti nei tempi (obiettivo: ≥95%)
- Cambiamenti non autorizzati rilevati (obiettivo: 0)
- Completamento della revisione della base di configurazione (obiettivo: 100%)
- Accuratezza del CMDB (obiettivo: ≥95%)

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **DT** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per la gestione della configurazione. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.9 (UG/TG). Il riferimento tecnico è in ISMS-CTX-A.8.9 (NON SGSI).*

<!-- QA_VERIFIED: 2026-04-03 -->
