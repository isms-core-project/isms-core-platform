<!-- ISMS-CORE:REF:ISMS-REF-A.8.32-IT-change-management-reference:framework:REF:a.8.32 -->
**ISMS-REF-A.8.32 — Riferimento per la gestione dei cambiamenti**
**Strumenti e modelli di implementazione (Riferimento tecnico non-SGSI)**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento per la gestione dei cambiamenti |
| **Tipo di documento** | Interno — Riferimento tecnico (non SGSI) |
| **Identificativo del documento** | ISMS-REF-A.8.32 |
| **Autore del documento** | Responsabile dei cambiamenti |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Responsabile dei cambiamenti (Riferimento tecnico — nessuna approvazione esecutiva richiesta) |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | Responsabile dei cambiamenti / Operazioni IT | Riferimento tecnico iniziale per la prima certificazione ISO 27001:2022 |

**Ciclo di revisione**: In base alle esigenze (evoluzione della tecnologia e degli strumenti)  
**Prossima data di revisione**: [Data + 12 mesi]

**Distribuzione**: Responsabile dei cambiamenti, membri del CAB, Operazioni IT, Implementatori dei cambiamenti (per la consapevolezza tecnica)

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione. Non fa parte del SGSI, non stabilisce requisiti obbligatori e non deve essere utilizzato come prova di audit. Tutti i requisiti vincolanti sono definiti in **ISMS-POL-A.8.32 (Politica di gestione dei cambiamenti)**.

---

## Scopo e organizzazione dei contenuti

Questo documento fornisce materiale di riferimento tecnico per l'implementazione della gestione dei cambiamenti, consolidando:

- Requisiti di capacità degli strumenti (ex ISMS-POL-A.8.32-S5.A)
- Modelli di modulo di richiesta di cambiamento (ex ISMS-POL-A.8.32-S5.B)
- Metodologia di valutazione del rischio (ex ISMS-POL-A.8.32-S5.C)
- Guida di riferimento rapido (ex ISMS-POL-A.8.32-S5.D)

---

# Requisiti di capacità degli strumenti

## Scopo

Definire le capacità minime richieste dai sistemi di gestione dei cambiamenti (strumenti ITSM, sistemi di ticketing, piattaforme di flusso di lavoro). Le organizzazioni possono utilizzare qualsiasi sistema che soddisfi questi requisiti di capacità.

**Importante**: Questo documento specifica le CAPACITÀ, non prodotti o fornitori specifici.

## Capacità principali della gestione dei cambiamenti

### CAP-001: Gestione delle richieste di cambiamento

**Capacità**: Il sistema DEVE consentire la creazione e la gestione delle richieste di cambiamento.

**Requisiti**:

- Creare richieste di cambiamento con identificatori univoci
- Acquisire tutti i campi richiesti per la Sezione 3 (Modello di modulo)
- Supportare descrizioni di testo avanzato e allegati di file
- Collegare cambiamenti, incidenti e problemi correlati
- Taggare/categorizzare i cambiamenti (per tipo, sistemi interessati, priorità)

**Valutazione**: Gli utenti possono inviare richieste di cambiamento complete? Tutti i campi richiesti vengono acquisiti?

---

### CAP-002: Gestione dello stato del cambiamento

**Capacità**: Il sistema DEVE tracciare lo stato del cambiamento attraverso il ciclo di vita definito.

**Stati richiesti (minimo)**:

- Richiesto / Bozza
- In valutazione / In revisione
- Pianificato / Approvato
- In implementazione
- Revisione (PIR)
- Chiuso
- Rifiutato
- Annullato

**Requisiti**:

- Transizioni di stato tracciate con timestamp e utente
- Flussi di lavoro basati sullo stato (alcune azioni disponibili solo in determinati stati)
- Cronologia degli stati visibile nel record di cambiamento

---

### CAP-003: Flusso di lavoro di approvazione

**Capacità**: Il sistema DEVE supportare flussi di lavoro di approvazione configurabili.

**Requisiti**:

- Approvazioni multi-livello (Responsabile dei cambiamenti, CAB, E-CAB, Direzione)
- Instradamento delle approvazioni basato sui ruoli
- Notifiche di approvazione agli approvatori
- Tracciamento delle scadenze di approvazione
- Approvazione con commenti/condizioni
- Cronologia delle approvazioni con identità dell'approvatore e timestamp
- Integrazione e-mail per le notifiche di approvazione

---

### CAP-004: Calendario dei cambiamenti

**Capacità**: Il sistema DEVE fornire un calendario dei cambiamenti che mostri i cambiamenti pianificati.

**Requisiti**:

- Vista calendario visiva (giornaliera, settimanale, mensile)
- Evidenziare i conflitti tra i cambiamenti
- Identificare i periodi di blocco dei cambiamenti e le finestre di esclusione
- Filtrare per sistema, tipo di cambiamento, livello di rischio, team
- Esportare in formato iCalendar

---

### CAP-005: Report e analisi

**Capacità**: Il sistema DEVE fornire capacità di reporting per il tracciamento delle metriche.

**Report richiesti**:

- Volume dei cambiamenti (per tipo, periodo di tempo, livello di rischio)
- Tasso di successo dei cambiamenti
- Percentuale di cambiamenti di emergenza
- Durata media dei cambiamenti
- Incidenti correlati ai cambiamenti
- Tasso di completamento del PIR
- Utilizzo dei cambiamenti standard
- Analisi delle tendenze

---

### CAP-006: Pista di audit

**Capacità**: Il sistema DEVE mantenere una pista di audit completa.

**Requisiti**:

- Tutte le modifiche ai campi registrate (chi, cosa, quando)
- Transizioni di stato registrate
- Approvazioni registrate con timestamp
- Accesso al sistema registrato
- Registro di audit immutabile (non modificabile dopo la creazione)
- Conservazione del registro di audit allineata ai requisiti della politica

---

### CAP-007: Integrazione

**Capacità**: Il sistema DOVREBBE integrarsi con i sistemi correlati.

**Punti di integrazione**:

- Configuration Management Database (CMDB) — collegare i cambiamenti alle CI
- Gestione degli incidenti — collegare i cambiamenti agli incidenti
- Gestione dei problemi — collegare i cambiamenti ai problemi
- Catalogo dei servizi — cambiamenti standard come elementi del catalogo
- Sistemi di notifica — email, Slack, MS Teams
- Disponibilità API per l'automazione

---

## Lista di controllo per la valutazione degli strumenti

Le organizzazioni che valutano gli strumenti di gestione dei cambiamenti possono utilizzare questa lista:

- [ ] CAP-001: Capacità di gestione delle richieste di cambiamento presenti
- [ ] CAP-002: Gestione degli stati con tracciamento del ciclo di vita
- [ ] CAP-003: Flussi di lavoro di approvazione configurabili
- [ ] CAP-004: Calendario dei cambiamenti con rilevamento dei conflitti
- [ ] CAP-005: Capacità di report e analisi
- [ ] CAP-006: Capacità complete di pista di audit
- [ ] CAP-007: Capacità di integrazione con CMDB/Incidenti/Problemi
- [ ] Interfaccia intuitiva per i richiedenti di cambiamenti
- [ ] Capacità di accesso mobile
- [ ] Gestione del Catalogo dei cambiamenti standard
- [ ] Operazioni di cambiamento in blocco supportate
- [ ] Controllo degli accessi basato sui ruoli
- [ ] Campi e flussi di lavoro personalizzabili
- [ ] Supporto multi-tenant (se necessario)
- [ ] Distribuzione basata su cloud o on-premises (in base ai requisiti)

---

# Modello di modulo di richiesta di cambiamento

## Scopo

Fornire un modello standard per le richieste di cambiamento che garantisca un'acquisizione coerente delle informazioni. Utilizzare questo modello per configurare i moduli degli strumenti ITSM o come documento autonomo di richiesta di cambiamento.

## Modulo di richiesta di cambiamento

**Sezione 1: Informazioni di base**

- **ID richiesta di cambiamento**: [Generato automaticamente dal sistema]
- **Data di presentazione**: [Popolato automaticamente]
- **Richiesto da**: [Nome, Email, Dipartimento]
- **Telefono di contatto**: [Per il coordinamento dell'implementazione]

**Sezione 2: Classificazione del cambiamento**

- **Tipo di cambiamento**: [Elenco a discesa: Standard / Normale / Emergenza]
- **Se cambiamento standard — Voce del catalogo dei cambiamenti standard**: [Elenco a discesa: Selezionare dal catalogo]
- **Se cambiamento di emergenza — Giustificazione dell'emergenza**: [Testo: Perché si applica la classificazione di emergenza]
- **Priorità**: [Elenco a discesa: Critica / Alta / Media / Bassa]
- **Livello di rischio**: [Calcolato automaticamente o manuale: Critico / Alto / Medio / Basso]

**Sezione 3: Descrizione del cambiamento**

- **Titolo del cambiamento**: [Titolo breve e descrittivo — max 80 caratteri]
- **Descrizione del cambiamento**: [Cosa viene modificato? Qual è l'ambito? Quali sono le modifiche specifiche?]
- **Giustificazione aziendale**: [Perché è necessario questo cambiamento? Driver aziendale, benefici attesi, conseguenze se non implementato]

**Sezione 4: Valutazione dell'impatto**

- **Sistemi/componenti interessati**: [Elenco delle voci di configurazione dal CMDB]
- **Utenti/stakeholder interessati**: [Gruppi di utenti, numero approssimativo, ubicazioni geografiche]
- **Impatto sul servizio**: [Elenco a discesa: Nessun impatto / Limitato / Interruzione parziale / Interruzione totale]
- **Tempo di inattività richiesto**: [Sì / No] **Se sì, durata**: [Minuti/ore stimati]

**Sezione 5: Valutazione del rischio**

- **Livello di impatto**: [Elenco a discesa: Basso / Medio / Alto / Critico] + Giustificazione
- **Livello di probabilità**: [Elenco a discesa: Bassa / Media / Alta] + Giustificazione
- **Rischio complessivo**: [Calcolato automaticamente dalla matrice Impatto × Probabilità]
- **Misure di mitigazione del rischio**: [Come verranno ridotti i rischi?]

**Sezione 6: Dipendenze e prerequisiti**

- **Dipendenze**: [Altri cambiamenti, sistemi o attività da cui dipende questo cambiamento]
- **Prerequisiti**: [Cosa deve essere completato prima di questo cambiamento — tecnico, aziendale, approvazione]
- **Conflitti**: [Conflitti noti con altri cambiamenti o attività?]

**Sezione 7: Piano di implementazione**

- **Data/ora di implementazione proposta**: [Selettore di data, selettore di ora — includere il fuso orario]
- **Finestra di implementazione**: [Stima della durata]
- **Fasi di implementazione**: [Procedura di alto livello numerata]
- **Team di implementazione**: [Implementatore principale, Implementatori aggiuntivi, Personale di verifica]
- **Requisiti di risorse**: [Personale, Strumenti/Software, Budget]

**Sezione 8: Test e validazione**

- **Ambiente di test**: [Dove verrà testato il cambiamento?]
- **Test eseguiti**: [Test unitari, Test di integrazione, Test di sicurezza, UAT — Sì/No e risultati]
- **Risultati dei test**: [Allegare la documentazione dei test]
- **Criteri di accettazione**: [Come verrà misurato il successo?]

**Sezione 9: Piano di rollback**

- **Procedura di rollback**: [Rollback passo per passo se il cambiamento fallisce]
- **Durata del rollback**: [Tempo richiesto per il rollback]
- **Criteri di decisione per il rollback**: [Quando deve essere avviato il rollback?]
- **Considerazioni sui dati**: [Il rollback causerà perdita di dati? Come mitigato?]

**Sezione 10: Piano di comunicazione**

- **Notifica degli stakeholder richiesta**: [Sì / No]
- **Se sì**: Chi deve essere notificato, metodo di notifica, tempistica, responsabile della comunicazione
- **Comunicazione agli utenti**: [Gli utenti finali hanno bisogno di preavviso?]

**Sezione 11: Documentazione**

- **Aggiornamenti della documentazione richiesti**: [Sì / No]
- **Se sì**: Documentazione di sistema, Procedure operative, Guide utente, Diagrammi di rete, Altro
- **Responsabile della documentazione**: [Chi aggiornerà la documentazione?]

**Sezione 12: Post-implementazione**

- **PIR richiesto**: [Determinato automaticamente in base al tipo/rischio del cambiamento]
- **Criteri di successo**: [Come verrà misurato il successo del cambiamento?]
- **Durata del monitoraggio**: [Per quanto tempo verrà monitorato il cambiamento dopo l'implementazione?]

---

# Metodologia di valutazione del rischio

## Scopo

Fornire una metodologia dettagliata per valutare il rischio del cambiamento in base all'impatto e alla probabilità, determinare l'autorità di approvazione appropriata e identificare le strategie di mitigazione del rischio.

## Valutazione dell'impatto

### Definizioni del livello di impatto

| Livello di impatto | Definizione | Ambito |
|-------------------|-------------|--------|
| **Basso** | Impatto minimo, facilmente reversibile | Singolo utente, singolo sistema non critico, recupero <15 min |
| **Medio** | Impatto moderato, rollback fattibile | Team/più utenti, sistemi non critici, recupero <2 ore |
| **Alto** | Impatto significativo, rollback complesso | Dipartimento, sistema principale, interruzione del processo aziendale, recupero <8 ore |
| **Critico** | Impatto grave, recupero difficile | A livello organizzativo, sistema mission-critical, rivolto ai clienti, recupero >8 ore o irreversibile |

### Dimensioni della valutazione dell'impatto

**Utenti interessati**: Basso: <10 / Medio: 10-100 / Alto: 100-1000 / Critico: >1000

**Processi aziendali**: Basso: Opzionale / Medio: Importante / Alto: Critico con soluzioni alternative / Critico: Mission-critical

**Impatto finanziario**: Basso: <$10K / Medio: $10K-$100K / Alto: $100K-$1M / Critico: >$1M

**Normativa/Conformità**: Basso: Nessuna / Medio: Report interessati / Alto: Rischio di scadenza / Critico: Potenziale violazione

**Reputazione**: Basso: Solo interno / Medio: Disagio per i clienti / Alto: Visibilità pubblica / Critico: Impatto significativo

**Complessità del recupero**: Basso: <15 min / Medio: <2 ore / Alto: <8 ore / Critico: Molto complesso o irreversibile

**Impatto complessivo**: Livello più alto tra tutte le dimensioni (valutazione più conservativa)

## Valutazione della probabilità

### Definizioni del livello di probabilità

| Probabilità | Definizione | Tasso di successo tipico |
|-------------|-------------|--------------------------|
| **Bassa** | Molto improbabile che fallisca | >95% di successo |
| **Media** | Probabilità moderata di problemi | 75-95% di successo |
| **Alta** | Probabilità significativa di problemi | <75% di successo |

### Fattori della valutazione della probabilità

**Complessità del cambiamento**: Bassa: Semplice / Media: Moderata / Alta: Complessa

**Stabilità dell'ambiente**: Bassa: Stabile / Media: Problemi occasionali / Alta: Problemi frequenti

**Esperienza del team**: Bassa: Esperto / Media: Qualche esperienza / Alta: Nuova procedura/team

**Completezza dei test**: Bassa: Ampiamente testato / Media: Ben testato / Alta: Limitato/Non testato

**Dipendenze**: Bassa: Nessuna / Media: Poche / Alta: Molte dipendenze complesse

## Matrice del rischio

**Rischio complessivo = Impatto × Probabilità**

| Impatto ↓ / Probabilità → | Bassa | Media | Alta |
|---------------------------|-------|-------|------|
| **Basso** | Basso | Basso | Medio |
| **Medio** | Basso | Medio | Alto |
| **Alto** | Medio | Alto | Critico |
| **Critico** | Alto | Critico | Critico |

## Autorità di approvazione per livello di rischio

| Livello di rischio | Autorità di approvazione | Requisiti aggiuntivi |
|-------------------|--------------------------|----------------------|
| **Basso** | Responsabile dei cambiamenti | Documentazione standard |
| **Medio** | CAB | Documentazione standard |
| **Alto** | CAB + Direzione IT senior | Documentazione completa |
| **Critico** | CAB + RSSI + Direzione generale | Documentazione completa + Briefing esecutivo |
| **Emergenza** | E-CAB (Resp. Oper. IT + RSSI) | Revisione retrospettiva del CAB entro 48 ore |

---

# Guida di riferimento rapido

## Albero decisionale per il tipo di cambiamento

**INIZIA QUI → Il cambiamento è necessario?**

```
├─ Il cambiamento è già nel catalogo dei cambiamenti standard?
│   ├─ SÌ → Cambiamento standard
│   │        ▼
│   │   • Inviare la richiesta di cambiamento (self-service OK)
│   │   • Nessuna approvazione CAB necessaria
│   │   • Seguire la procedura del catalogo
│   │   • Registrare nel sistema dei cambiamenti
│   │
│   └─ NO → Continuare...
│
├─ Si tratta di una situazione di emergenza?
│   ├─ SÌ → Soddisfa TUTTI i criteri di emergenza?
│   │        • Azione immediata richiesta?
│   │        • Incidente critico/sicurezza/guasto?
│   │        • Rischio di inazione > rischio di azione?
│   │        ▼
│   │   ├─ SÌ → Cambiamento di emergenza
│   │   │        • Contattare E-CAB immediatamente
│   │   │        • Documentare la giustificazione
│   │   │        • Approvazione accelerata
│   │   │        • PIR obbligatorio entro 2 giorni
│   │   │
│   │   └─ NO → Cambiamento normale urgente
│   │            • Convocare riunione CAB speciale
│   │            • Accelerare ma seguire il processo completo
│   │
│   └─ NO → Cambiamento normale
│            ▼
│       • Inviare la richiesta di cambiamento
│       • Valutazione del rischio
│       • Revisione del CAB
│       • Processo completo
```

## Riferimento rapido all'autorità di approvazione

| Livello di rischio | Chi approva | Tempistica tipica |
|-------------------|-------------|-------------------|
| **Basso** (Standard) | Responsabile dei cambiamenti | Immediato - 1 giorno |
| **Medio** (Normale) | CAB | Riunione CAB settimanale |
| **Alto** (Normale) | CAB + Direzione IT senior | 1-2 settimane |
| **Critico** (Normale) | CAB + RSSI + Direzione gen. | 2-4 settimane |
| **Emergenza** | E-CAB | <4 ore |

## Lista di controllo delle informazioni richieste

**Ogni richiesta di cambiamento necessita di**:

- [ ] Descrizione chiara (cosa viene modificato?)
- [ ] Giustificazione aziendale (perché?)
- [ ] Valutazione del rischio (impatto + probabilità)
- [ ] Sistemi interessati (dal CMDB)
- [ ] Piano di implementazione (passo per passo)
- [ ] Test completati (o piano se emergenza)
- [ ] Piano di rollback (come annullare)
- [ ] Piano di comunicazione (chi notificare)

## Lista di controllo per i cambiamenti di emergenza

**Prima di dichiarare un'emergenza**:

- [ ] Incidente critico o vulnerabilità di sicurezza?
- [ ] Azione immediata richiesta per prevenire un impatto significativo?
- [ ] Il rischio di NON modificare > il rischio di modificare?
- [ ] Nessun tempo per la normale revisione del CAB?

**Se SÌ a tutti i punti sopra → Cambiamento di emergenza**:
1. Contattare E-CAB (Resp. Oper. IT + RSSI)
2. Documentare la giustificazione dell'emergenza
3. Ottenere l'approvazione accelerata
4. Implementare con monitoraggio
5. Condurre il PIR entro 48 ore
6. Presentare al CAB in modo retrospettivo

## Contatti chiave

**Responsabile dei cambiamenti**: [Nome, Email, Telefono]  
**Presidente del CAB**: [Nome, Email, Telefono]  
**E-CAB (Emergenza)**: [Nomi, Email, Telefoni]  
**Responsabile delle operazioni IT**: [Nome, Email, Telefono]  
**RSSI**: [Nome, Email, Telefono]

**Percorso di escalation**:
1. Responsabile dei cambiamenti
2. Responsabile delle operazioni IT
3. RSSI
4. CIO

## Errori comuni da evitare

1. ❌ **Inviare richieste di cambiamento incomplete** → Approvazioni ritardate
2. ❌ **Saltare i test "perché urgente"** → Incidenti in produzione
3. ❌ **Nessun piano di rollback** → Interruzioni prolungate quando il cambiamento fallisce
4. ❌ **Dimenticare di comunicare** → Utenti e dirigenti insoddisfatti
5. ❌ **Classificare erroneamente come emergenza** → Erosione del processo
6. ❌ **Nessun aggiornamento della documentazione** → Confusione operativa
7. ❌ **Saltare il PIR** → Lezioni non apprese, errori ripetuti
8. ❌ **Implementare senza approvazione** → Violazione della conformità

## Suggerimenti per il successo

✅ **Iniziare la richiesta di cambiamento in anticipo** — Non aspettare l'ultimo minuto  
✅ **Essere approfonditi nella valutazione del rischio** — Meglio prudenti  
✅ **Testare prima in un ambiente non di produzione** — Individuare i problemi prima della produzione  
✅ **Avere il piano di rollback pronto** — Sperare per il meglio, prepararsi per il peggio  
✅ **Comunicare proattivamente** — Gli stakeholder apprezzano il preavviso  
✅ **Documentare tutto** — Il te futuro ringrazierà il te presente  
✅ **Imparare dai fallimenti** — Il PIR è per il miglioramento, non per le colpe

---

# Guida alla selezione degli strumenti

## Valutazione delle piattaforme ITSM

**Criteri chiave**:

- Soddisfa i requisiti minimi di capacità (Sezione 2)
- Intuitivo per i richiedenti di cambiamenti
- Integrazione con gli strumenti esistenti (CMDB, ticketing)
- Capacità di reporting e analisi
- Costo totale di proprietà (licenze, manutenzione, formazione)
- Stabilità del fornitore e qualità del supporto
- Modello di distribuzione cloud vs on-premises

**Piattaforme ITSM popolari** (esempi, non raccomandazioni):

- ServiceNow
- Jira Service Management
- BMC Remedy
- Cherwell
- Freshservice
- ManageEngine
- Opzioni open source (OTRS, iTop, osTicket)

## Migliori pratiche di configurazione

Quando si configurano gli strumenti di gestione dei cambiamenti:

1. Iniziare con i flussi di lavoro predefiniti, personalizzare solo quando necessario
2. Implementare i campi obbligatori per garantire la completezza
3. Configurare i flussi di lavoro di approvazione in base alla matrice del rischio
4. Impostare le notifiche e-mail per tutti gli stakeholder
5. Configurare il calendario dei cambiamenti con i periodi di blocco
6. Abilitare l'integrazione con il CMDB per una valutazione accurata dell'impatto
7. Impostare i dashboard per il Responsabile dei cambiamenti e il CAB
8. Configurare i modelli di report per le metriche richieste
9. Formare gli utenti prima del go-live
10. Pianificare la manutenzione e gli aggiornamenti continui

---

# Appendice: Modelli di moduli

## A.1 Modulo di richiesta di cambiamento (vuoto)

[Modulo vuoto completo che corrisponde alla struttura della Sezione 3.2]

## A.2 Modello di giustificazione del cambiamento di emergenza

**Richiesta di cambiamento di emergenza**

- **ID cambiamento**: ___________
- **Inviato da**: ___________
- **Data/Ora**: ___________

**Criteri di emergenza soddisfatti**:

- [ ] Incidente critico che richiede risoluzione immediata
- [ ] Vulnerabilità di sicurezza che richiede patch immediata
- [ ] Guasto del sistema che richiede ripristino immediato
- [ ] Prevenzione di guasto imminente del sistema
- [ ] Requisito normativo urgente

**Descrizione della situazione**:
[Descrivere la situazione critica che richiede il cambiamento di emergenza]

**Impatto se NON implementato immediatamente**:
[Descrivere le conseguenze del ritardo]

**Rischio se implementato senza test completi**:
[Riconoscere i rischi dell'implementazione accelerata]

**Misure di mitigazione**:
[Descrivere come i rischi verranno minimizzati nonostante l'urgenza]

**Approvazione E-CAB**:

- Responsabile delle operazioni IT: ___________ Data: ___________
- RSSI: ___________ Data: ___________

---

**FINE DEL RIFERIMENTO TECNICO**

---

*Questo riferimento tecnico supporta l'implementazione di ISMS-POL-A.8.32. Tutti i requisiti vincolanti sono definiti nel documento di politica.*
<!-- QA_VERIFIED: 2026-04-04 -->
