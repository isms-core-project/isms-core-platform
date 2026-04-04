<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.32-IT:framework:POL:a.8.32 -->
**ISMS-POL-A.8.32 — Gestione dei cambiamenti**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Gestione dei cambiamenti |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.32 |
| **Autore del documento** | RSSI |
| **Proprietario del documento** | AD |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DSI/Responsabile Operazioni IT → Conformità → AD.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.32.1–3-UG/TG; ISMS-REF-A.8.32 (Modelli e guide rapide); ISO/IEC 27001:2022 Controllo A.8.32.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per i controlli di gestione dei cambiamenti per garantire modifiche sicure e controllate ai sistemi informativi, conformemente al Controllo A.8.32 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutte le modifiche ai sistemi di elaborazione delle informazioni, alle applicazioni, all'infrastruttura, alle apparecchiature di rete e ai sistemi di supporto, indipendentemente dal modello di dispiegamento (on-premise, cloud, ibrido). Tutti i tipi di cambiamento (hardware, software, configurazione, infrastruttura, dati, processo, documentazione) e tutti gli ambienti (sviluppo, test, staging, produzione, disaster recovery) sono inclusi.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Controllo ISO/IEC 27001:2022 A.8.32

> *Le modifiche alle strutture di elaborazione delle informazioni e ai sistemi informativi devono essere soggette a procedure di gestione dei cambiamenti.*

**Obiettivo del controllo**: Garantire che tutte le modifiche ai sistemi informativi siano valutate, approvate, testate, implementate e riviste in modo controllato per minimizzare i rischi di interruzione del servizio e vulnerabilità di sicurezza.

---

# Enunciati di politica

## Classificazione dei cambiamenti

[Organizzazione] DEVE classificare tutti i cambiamenti prima dell'elaborazione.

**Tipi di cambiamento**:

| Tipo | Descrizione | Esempio | Approvazione richiesta |
|------|-------------|---------|----------------------|
| **Cambiamento standard** | Cambiamenti pre-approvati a basso rischio | Aggiornamenti OS di routine, patch di sicurezza | Pre-approvato — nessuna revisione del CAC |
| **Cambiamento normale** | Cambiamenti pianificati a rischio medio/alto | Nuove funzionalità dell'applicazione, modifiche all'infrastruttura | Revisione e approvazione del CAC |
| **Cambiamento di emergenza** | Cambiamenti urgenti per risolvere incidenti critici | Patch di sicurezza zero-day, ripristino dopo un'interruzione | Approvazione rapida + revisione post-implementazione |

## Processo di cambiamento normale

[Organizzazione] DEVE seguire un processo formale per tutti i cambiamenti normali.

**Passaggi obbligatori del processo**:

1. **Richiesta di cambiamento**: Documenta il cambiamento proposto, la giustificazione aziendale e l'impatto previsto
2. **Valutazione dell'impatto**: Valuta sicurezza, disponibilità, conformità e impatto operativo; identifica i sistemi dipendenti
3. **Pianificazione del test**: Definisce i test richiesti e i criteri di successo
4. **Pianificazione del rollback**: Documenta come invertire il cambiamento se necessario
5. **Approvazione del CAC**: Il Comitato di Approvazione dei Cambiamenti (CAC) rivede e approva
6. **Implementazione**: Implementa il cambiamento secondo il piano approvato
7. **Test post-implementazione**: Verifica che il cambiamento abbia raggiunto il risultato previsto
8. **Chiusura**: Documenta i risultati e chiude la richiesta di cambiamento

**Requisiti di documentazione**: Tutte le richieste di cambiamento DEVONO essere registrate nel sistema di gestione dei cambiamenti; i record DEVONO essere conservati per almeno 3 anni.

## Comitato di Approvazione dei Cambiamenti (CAC)

[Organizzazione] DEVE mantenere un CAC per la supervisione dei cambiamenti.

**Composizione del CAC**: Presidente: Responsabile Operazioni IT o delegato; Membri principali: Responsabile Sicurezza Informatica, Responsabile Operazioni IT, Responsabile delle Applicazioni; Membri aggiuntivi (dove rilevante): Proprietari dei sistemi interessati, rappresentanti delle aree aziendali.

**Frequenza delle riunioni**: Settimanale per i cambiamenti normali pianificati; su richiesta per i cambiamenti urgenti; il quorum richiede almeno 3 membri.

**Autorità di approvazione**:

| Tipo di cambiamento | Autorità di approvazione |
|--------------------|--------------------------|
| Standard (pre-approvato) | Nessuna revisione del CAC richiesta |
| Normale a basso rischio | Presidente del CAC o delegato |
| Normale ad alto rischio | Piena approvazione del CAC |
| Emergenza | CAC di emergenza (minimo 2 membri) + revisione post-implementazione |

## Cambiamenti di emergenza

[Organizzazione] DEVE gestire i cambiamenti di emergenza in modo controllato pur consentendo una risposta rapida.

**Definizione di emergenza**: Un cambiamento è di emergenza quando il ritardo causerebbe: un incidente di sicurezza attivo o in peggioramento; un'interruzione significativa del servizio; un rischio normativo critico; un impatto finanziario grave.

**Processo di cambiamento di emergenza**: Notifica immediata al presidente del CAC e al RSSI; approvazione verbale minima da 2 membri del CAC (incluso il RSSI per i cambiamenti di sicurezza); implementazione con documentazione simultanea; revisione post-implementazione obbligatoria entro 48 ore; documentazione completa entro 72 ore.

## Valutazione della sicurezza

[Organizzazione] DEVE valutare l'impatto sulla sicurezza di tutti i cambiamenti non standard.

**Requisiti obbligatori di valutazione della sicurezza**: Per tutti i cambiamenti normali: conferma che il cambiamento non introduce vulnerabilità note; per i cambiamenti che influenzano l'autenticazione/autorizzazione: revisione da parte del Responsabile Sicurezza Informatica; per i cambiamenti che influenzano il trattamento dei DCP: revisione della conformità alla privacy; per i cambiamenti dell'infrastruttura di produzione: revisione dell'architettura di sicurezza.

## Finestre di cambiamento

[Organizzazione] DEVE definire finestre di cambiamento approvate per minimizzare l'impatto operativo.

**Finestre di cambiamento standard**: Fuori dalle ore di punta (giorni feriali, fuori dall'orario lavorativo principale); durante i periodi di manutenzione pianificata. **Periodi di blocco dei cambiamenti**: Nessun cambiamento ai sistemi critici durante i periodi di punta identificati (es. fine anno, lancio di prodotti critici); esenzioni richiedono l'approvazione del RSSI + DSI.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; rappresentante della sicurezza nel CAC; approva i cambiamenti di sicurezza ad alto rischio |
| **Responsabile Operazioni IT** | Presidente del CAC; supervisione del processo di cambiamento; coordinamento dell'implementazione |
| **Responsabile Sicurezza Informatica** | Valutazione della sicurezza dei cambiamenti; avvisi di sicurezza al CAC |
| **Proprietari dei sistemi** | Approvazione dei cambiamenti ai sistemi di proprietà; partecipazione ai test |
| **Team IT** | Implementazione dei cambiamenti approvati; documentazione dei risultati |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce i requisiti per la gestione dei cambiamenti. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.32 (UG/TG). I modelli e le guide rapide sono in ISMS-REF-A.8.32.*

<!-- QA_VERIFIED: 2026-04-03 -->
