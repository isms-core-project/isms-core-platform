<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.27-IT:framework:POL:a.8.27 -->
**ISMS-POL-A.8.27 — Architettura e principi di ingegneria dei sistemi sicuri**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Architettura e principi di ingegneria dei sistemi sicuri |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.27 |
| **Autore del documento** | RSSI |
| **Proprietario del documento** | RSSI |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DT → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.8.25-26-29 (Quadro di sviluppo sicuro); ISMS-POL-A.8.28 (Codifica sicura); ISMS-POL-A.8.9 (Gestione della configurazione); ISMS-POL-A.5.8; ISMS-IMP-A.8.27.1–4-UG/TG; ISO/IEC 27001:2022 Controllo A.8.27; NIST SP 800-160; NIST SP 800-207.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti fondamentali di [Organizzazione] per l'Ingegneria dei Sistemi Sicuri (SSE) — la disciplina che integra la sicurezza in ogni strato dell'architettura di sistema durante l'intero ciclo di vita del sistema.

**Scopo**: Definire i principi, gli approcci e i requisiti per la progettazione di sistemi sicuri e affidabili. Stabilisce COSA applicare ai principi di ingegneria sicura e CHI è responsabile della loro implementazione.

**Perimetro**: Si applica a tutti i nuovi sistemi e alle modifiche significative ai sistemi esistenti; a tutti gli ambienti (on-premise, cloud, ibrido, sistemi incorporati); e a tutti i tipi di sistema nel perimetro del SGSI.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Controllo ISO/IEC 27001:2022 A.8.27

> *Principi per la progettazione di sistemi sicuri devono essere stabiliti, documentati, mantenuti e applicati a qualsiasi attività di implementazione dei sistemi informativi.*

**Obiettivo del controllo**: Garantire che i sistemi informativi siano progettati con la sicurezza integrata fin dall'inizio, riducendo le vulnerabilità e i rischi attraverso principi architetturali consolidati.

---

# Principi di ingegneria dei sistemi sicuri

## Principi fondamentali (obbligatori per tutti i sistemi)

[Organizzazione] DEVE applicare i seguenti principi di ingegneria sicura a tutti i progetti di sistema.

**1. Minimo privilegio e separazione dei compiti**: I componenti del sistema DEVONO operare con i privilegi minimi necessari; le funzioni critiche DEVONO essere separate tra diversi componenti o utenti; i servizi DEVONO comunicare con le autorizzazioni minime richieste.

**2. Defense in Depth (Difesa in profondità)**: I sistemi DEVONO implementare più livelli di controlli di sicurezza; nessun singolo controllo DEVE essere il solo meccanismo di protezione; si presuppone che ogni livello possa fallire e vengono pianificati controlli compensativi.

**3. Fail Secure (Guasto sicuro)**: In caso di guasto, i sistemi DEVONO passare a uno stato sicuro (accesso negato) piuttosto che aperto; le condizioni di errore DEVONO essere gestite esplicitamente; il comportamento di guasto DEVE essere testato e documentato.

**4. Economia del meccanismo (Semplicità)**: I meccanismi di sicurezza DEVONO essere il più semplici possibile; la complessità aumenta la probabilità di vulnerabilità; le funzionalità non necessarie DEVONO essere rimosse.

**5. Mediazione completa**: Ogni accesso a ogni risorsa DEVE essere verificato; i meccanismi di caching o bypass del controllo degli accessi DEVONO essere esaminati attentamente.

**6. Privacy by Design**: La privacy DEVE essere integrata nell'architettura, non aggiunta in seguito; la raccolta dei dati DEVE essere minimizzata ai dati necessari; la conservazione e la cancellazione dei dati DEVONO essere pianificate dall'inizio.

**7. Zero Trust**: I sistemi DEVONO assumere che nessuna rete, utente o dispositivo sia intrinsecamente affidabile; l'autenticazione e l'autorizzazione DEVONO essere eseguite per ogni richiesta; la micro-segmentazione e l'ispezione del traffico est-ovest DEVONO essere implementate per i sistemi critici.

## Requisiti di threat modeling

[Organizzazione] DEVE condurre il threat modeling per i sistemi ad alto rischio.

**Ambito obbligatorio del threat modeling**: Tutti i nuovi sistemi che gestiscono dati Riservati o Limitati; sistemi con esposizione a Internet; sistemi con accesso privilegiato; modifiche significative ai sistemi esistenti.

**Metodologia**: La metodologia STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) o equivalente DEVE essere utilizzata; i risultati del threat modeling DEVONO documentare: superfici di attacco identificate, minacce e rischi, controlli di mitigazione, rischi residui accettati.

**Tempistica**: Il threat modeling DEVE essere completato durante la fase di progettazione, prima dell'inizio dello sviluppo; DEVE essere aggiornato a seguito di modifiche architetturali significative.

## Revisione dell'architettura di sicurezza

[Organizzazione] DEVE sottoporre i sistemi a revisioni dell'architettura di sicurezza.

**Ambito obbligatorio della revisione**: Tutti i nuovi sistemi di produzione; modifiche significative ai sistemi esistenti (definite come modifiche che influenzano l'autenticazione, l'autorizzazione, il trattamento dei dati o l'architettura di rete).

**Processo di revisione**: Revisione dell'architettura di sicurezza eseguita dal team di sicurezza o da architetti sicuri qualificati; verifica della conformità ai principi di ingegneria sicura definiti in questa politica; documentazione dei risultati e dei requisiti di rimedio; approvazione richiesta prima del dispiegamento in produzione per i sistemi critici.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approva le eccezioni ai principi di ingegneria sicura |
| **DT** | Garantisce l'applicazione dei principi di ingegneria sicura nei progetti tecnici |
| **Architetti dei sistemi/della sicurezza** | Progettazione dell'architettura conforme ai principi; conduzione delle revisioni dell'architettura; threat modeling |
| **Team di sviluppo** | Implementazione dei principi di ingegneria sicura nel codice e nelle configurazioni |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DT** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce i principi di architettura e ingegneria dei sistemi sicuri. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.27 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
