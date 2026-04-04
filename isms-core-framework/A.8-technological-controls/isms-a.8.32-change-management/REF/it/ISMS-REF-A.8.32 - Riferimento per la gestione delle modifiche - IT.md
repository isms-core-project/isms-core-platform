<!-- ISMS-CORE:REF:ISMS-REF-A.8.32-IT-change-management-reference:framework:REF:a.8.32 -->
**ISMS-REF-A.8.32 — Riferimento per la gestione delle modifiche**
**Strumenti e modelli di implementazione (Riferimento tecnico non-SGSI)**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento per la gestione delle modifiche |
| **Tipo di documento** | Interno — Riferimento tecnico (non SGSI) |
| **Identificativo del documento** | ISMS-REF-A.8.32 |
| **Autore del documento** | Responsabile delle modifiche |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Responsabile delle modifiche (Riferimento tecnico — nessuna approvazione esecutiva richiesta) |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | Responsabile delle modifiche / Operazioni IT | Riferimento tecnico iniziale per la prima certificazione ISO 27001:2022 |

**Ciclo di revisione**: In base alle esigenze (evoluzione delle tecnologie e degli strumenti)  
**Prossima data di revisione**: [Data + 12 mesi]  
**Approvatori**: Responsabile delle modifiche / Responsabile delle operazioni IT (riferimento tecnico, nessuna approvazione SGSI richiesta)

**Distribuzione**: Responsabile delle modifiche, membri del CAB, Operazioni IT, Implementatori delle modifiche

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione.

- Questo documento NON fa parte del Sistema di Gestione della Sicurezza delle Informazioni (SGSI).
- Questo documento NON definisce controlli o requisiti obbligatori di gestione delle modifiche.
- Questo documento NON stabilisce requisiti vincolanti, scadenze, ICP o SLA.
- Questo documento NON impone l'uso, il divieto o la configurazione di specifici strumenti, fornitori o piattaforme di gestione delle modifiche.
- Questo documento NON sostituisce né estende alcuna politica SGSI.

Tutti i requisiti di gestione delle modifiche vincolanti, gli obblighi e le decisioni di governance sono definiti esclusivamente in **ISMS-POL-A.8.32 (Politica di gestione delle modifiche)** e in altri documenti SGSI approvati.

Questo documento serve esclusivamente come riferimento tecnico per:

- Descrivere le capacità e i requisiti degli strumenti di gestione delle modifiche
- Fornire modelli e moduli per le attività di gestione delle modifiche
- Tracciare le metodologie di valutazione del rischio e le matrici decisionali
- Supportare la pianificazione dell'implementazione della gestione delle modifiche
- Fornire guide di riferimento rapido per i professionisti
- **Questo documento non deve essere utilizzato come prova di audit dell'implementazione**

---

## Scopo e ambito del documento

**Scopo**

Questo documento fornisce materiale di riferimento tecnico per l'implementazione della gestione delle modifiche, consolidando:

- Requisiti di capacità degli strumenti (già ISMS-POL-A.8.32-S5.A)
- Modelli di moduli di richiesta di modifica (già ISMS-POL-A.8.32-S5.B)
- Metodologia di valutazione del rischio (già ISMS-POL-A.8.32-S5.C)
- Guida di riferimento rapido (già ISMS-POL-A.8.32-S5.D)

## Cosa NON è questo documento

Questo documento NON:

- Definisce i requisiti vincolanti di gestione delle modifiche di [Organizzazione] (vedere ISMS-POL-A.8.32)
- Stabilisce requisiti obbligatori per gli strumenti
- Crea obblighi di conformità o criteri di audit
- Sostituisce i requisiti della politica ISMS-POL-A.8.32
- Impone la selezione di strumenti specifici o relazioni con i fornitori
- Stabilisce flussi di approvazione o autorità

## Relazione con il SGSI

Questo documento è un **riferimento tecnico non vincolante**. Tutti i requisiti di gestione delle modifiche sono definiti esclusivamente in ISMS-POL-A.8.32 (Politica di gestione delle modifiche).

## Organizzazione dei contenuti

Questo riferimento organizza il contenuto in quattro sezioni:

1. **Sezione 2**: Requisiti di capacità degli strumenti — Capacità minime per i sistemi di gestione delle modifiche
2. **Sezione 3**: Modello di modulo di richiesta di modifica — Modello standard per la raccolta coerente delle informazioni
3. **Sezione 4**: Metodologia di valutazione del rischio — Valutazione dettagliata impatto/probabilità e matrice del rischio
4. **Sezione 5**: Guida di riferimento rapido — Guida per i professionisti per gli scenari comuni

---

# Requisiti di capacità degli strumenti

## Scopo

Definire le capacità minime richieste dai sistemi di gestione delle modifiche (strumenti ITSM, sistemi di ticketing, piattaforme workflow). Le organizzazioni possono utilizzare qualsiasi sistema che soddisfi questi requisiti di capacità.

**Importante:** Questo documento specifica le CAPACITÀ, non prodotti o fornitori specifici.

## Capacità principali di gestione delle modifiche

### CAP-001: Gestione delle richieste di modifica

**Capacità:** Il sistema DEVE consentire la creazione e la gestione delle richieste di modifica.

**Requisiti:**

- Creazione di richieste di modifica con identificatori univoci
- Acquisizione di tutti i campi obbligatori secondo la Sezione 3 (Modello di modulo)
- Supporto per descrizioni in testo arricchito e allegati di file
- Collegamento di modifiche, incidenti e problemi correlati
- Tag/categorizzazione delle modifiche (per tipo, sistemi interessati, priorità)

**Valutazione:** Gli utenti possono inviare richieste di modifica complete? Tutti i campi obbligatori sono acquisiti?

---

### CAP-002: Gestione dello stato delle modifiche

**Capacità:** Il sistema DEVE tracciare lo stato delle modifiche attraverso il ciclo di vita definito.

**Stati obbligatori (minimo):**

- Richiesto / Bozza
- Valutazione / Revisione
- Pianificato / Approvato
- In implementazione
- Revisione (PIR)
- Chiuso
- Rifiutato
- Annullato

**Requisiti:**

- Transizioni di stato tracciate con timestamp e utente
- Workflow basati sullo stato (determinate azioni disponibili solo in determinati stati)
- Cronologia degli stati visibile nel record della modifica

---

### CAP-003: Workflow di approvazione

**Capacità:** Il sistema DEVE supportare workflow di approvazione configurabili.

**Requisiti:**

- Approvazioni a più livelli (Responsabile delle modifiche, CAB, E-CAB, Direzione)
- Instradamento delle approvazioni basato sui ruoli
- Notifiche di approvazione agli approvatori
- Monitoraggio delle scadenze di approvazione
- Approvazione con commenti/condizioni
- Cronologia delle approvazioni con identità dell'approvatore e timestamp
- Integrazione email per le notifiche di approvazione

---

### CAP-004: Calendario delle modifiche

**Capacità:** Il sistema DEVE fornire un calendario delle modifiche che mostri le modifiche pianificate.

**Requisiti:**

- Vista calendario visiva (giornaliera, settimanale, mensile)
- Evidenziazione dei conflitti tra modifiche
- Identificazione dei periodi di blocco delle modifiche e delle finestre di interruzione
- Filtraggio per sistema, tipo di modifica, livello di rischio, team
- Esportazione in formato iCalendar

---

### CAP-005: Reportistica e analisi

**Capacità:** Il sistema DEVE fornire capacità di reportistica per il monitoraggio delle metriche.

**Report obbligatori:**

- Volume delle modifiche (per tipo, periodo di tempo, livello di rischio)
- Tasso di successo delle modifiche
- Percentuale di modifiche di emergenza
- Durata media delle modifiche
- Incidenti correlati alle modifiche
- Tasso di completamento del PIR
- Utilizzo delle modifiche standard
- Analisi delle tendenze

---

### CAP-006: Traccia di audit

**Capacità:** Il sistema DEVE mantenere una traccia di audit completa.

**Requisiti:**

- Tutte le modifiche ai campi registrate (chi, cosa, quando)
- Transizioni di stato registrate
- Approvazioni registrate con timestamp
- Accesso al sistema registrato
- Registro di audit immutabile (non modificabile dopo la creazione)
- Conservazione del registro di audit allineata ai requisiti della politica

---

### CAP-007: Integrazione

**Capacità:** Il sistema DOVREBBE integrarsi con i sistemi correlati.

**Punti di integrazione:**

- Configuration Management Database (CMDB) — collegamento delle modifiche agli elementi di configurazione
- Gestione degli incidenti — collegamento delle modifiche agli incidenti
- Gestione dei problemi — collegamento delle modifiche ai problemi
- Catalogo dei servizi — modifiche standard come elementi del catalogo
- Sistemi di notifica — email, Slack, MS Teams
- Disponibilità API per l'automazione

---

## Lista di controllo per la valutazione degli strumenti

Le organizzazioni che valutano gli strumenti di gestione delle modifiche possono utilizzare questa lista di controllo:

- [ ] CAP-001: Capacità di gestione delle richieste di modifica presenti
- [ ] CAP-002: Gestione degli stati con tracciamento del ciclo di vita
- [ ] CAP-003: Workflow di approvazione configurabili
- [ ] CAP-004: Calendario delle modifiche con rilevamento dei conflitti
- [ ] CAP-005: Capacità di reportistica e analisi
- [ ] CAP-006: Capacità complete di traccia di audit
- [ ] CAP-007: Capacità di integrazione con sistemi CMDB/Incidenti/Problemi
- [ ] Interfaccia intuitiva per i richiedenti di modifiche
- [ ] Capacità di accesso mobile
- [ ] Gestione del Catalogo delle modifiche standard
- [ ] Operazioni di modifica in blocco supportate
- [ ] Controllo degli accessi basato sui ruoli
- [ ] Campi e workflow personalizzabili
- [ ] Supporto multi-tenant (se necessario)
- [ ] Distribuzione basata su cloud o on-premises (secondo i requisiti)

---

# Modello di modulo di richiesta di modifica

## Scopo

Fornire un modello standard per le richieste di modifica che garantisca la raccolta coerente delle informazioni. Utilizzare questo modello per configurare i moduli degli strumenti ITSM o come documento autonomo di richiesta di modifica.

## Modulo di richiesta di modifica

**Sezione 1: Informazioni di base**

- **ID della richiesta di modifica:** [Generato automaticamente dal sistema]
- **Data di invio:** [Compilato automaticamente]
- **Richiesto da:** [Nome, Email, Dipartimento]
- **Telefono di contatto:** [Per il coordinamento dell'implementazione]

**Sezione 2: Classificazione della modifica**

- **Tipo di modifica:** [Elenco a discesa: Standard / Normale / Emergenza]
- **Se modifica standard — Voce del catalogo delle modifiche standard:** [Elenco a discesa: Selezionare dal catalogo]
- **Se modifica di emergenza — Giustificazione dell'emergenza:** [Testo: Perché si applica la classificazione di emergenza]
- **Priorità:** [Elenco a discesa: Critica / Alta / Media / Bassa]
- **Livello di rischio:** [Calcolato automaticamente o manuale: Critico / Alto / Medio / Basso]

**Sezione 3: Descrizione della modifica**

- **Titolo della modifica:** [Titolo breve e descrittivo — max 80 caratteri]
- **Descrizione della modifica:** [Cosa viene modificato? Qual è l'ambito? Quali sono le modifiche specifiche?]
- **Giustificazione aziendale:** [Perché è necessaria questa modifica? Motivazione aziendale, benefici attesi, conseguenze se non implementata]

**Sezione 4: Valutazione dell'impatto**

- **Sistemi/Componenti interessati:** [Elencare gli elementi di configurazione dal CMDB]
- **Utenti/Parti interessate:** [Gruppi di utenti, numero approssimativo, ubicazioni geografiche]
- **Impatto sul servizio:** [Elenco a discesa: Nessun impatto / Limitato / Interruzione parziale / Interruzione totale]
- **Downtime richiesto:** [Sì / No] **Se Sì, Durata:** [Stima in minuti/ore]

**Sezione 5: Valutazione del rischio**

- **Livello di impatto:** [Elenco a discesa: Basso / Medio / Alto / Critico] + Giustificazione
- **Livello di probabilità:** [Elenco a discesa: Basso / Medio / Alto] + Giustificazione
- **Rischio complessivo:** [Calcolato automaticamente dalla matrice Impatto × Probabilità]
- **Misure di mitigazione del rischio:** [Come verranno ridotti i rischi?]

**Sezione 6: Dipendenze e prerequisiti**

- **Dipendenze:** [Altre modifiche, sistemi o attività da cui dipende questa modifica]
- **Prerequisiti:** [Cosa deve essere completato prima di questa modifica — tecnico, aziendale, approvazione]
- **Conflitti:** [Eventuali conflitti noti con altre modifiche o attività?]

**Sezione 7: Piano di implementazione**

- **Data/Ora di implementazione proposta:** [Selezione data, Selezione ora — includere fuso orario]
- **Finestra di implementazione:** [Stima della durata]
- **Passaggi di implementazione:** [Procedura ad alto livello numerata]
- **Team di implementazione:** [Implementatore principale, Implementatori aggiuntivi, Personale di verifica]
- **Requisiti di risorse:** [Personale, Strumenti/Software, Budget]

**Sezione 8: Test e validazione**

- **Ambiente di test:** [Dove verrà testata la modifica?]
- **Test eseguiti:** [Test unitari, Test di integrazione, Test di sicurezza, UAT — S/N e risultati]
- **Risultati dei test:** [Allegare documentazione dei test]
- **Criteri di accettazione:** [Come verrà misurato il successo?]

**Sezione 9: Piano di rollback**

- **Procedura di rollback:** [Rollback passo-passo se la modifica fallisce]
- **Durata del rollback:** [Tempo necessario per il rollback]
- **Criteri di decisione per il rollback:** [Quando deve essere avviato il rollback?]
- **Considerazioni sui dati:** [Il rollback causerà perdita di dati? Come mitigato?]

**Sezione 10: Piano di comunicazione**

- **Notifica alle parti interessate richiesta:** [Sì / No]
- **Se Sì:** Chi deve essere notificato, metodo di notifica, tempi, responsabile della comunicazione
- **Comunicazione agli utenti:** [Gli utenti finali avranno bisogno di un preavviso?]

**Sezione 11: Documentazione**

- **Aggiornamenti della documentazione richiesti:** [Sì / No]
- **Se Sì:** Documentazione del sistema, Procedure operative, Guide utente, Diagrammi di rete, Altro
- **Responsabile della documentazione:** [Chi aggiornerà la documentazione?]

**Sezione 12: Post-implementazione**

- **PIR richiesto:** [Determinato automaticamente in base al tipo/rischio della modifica]
- **Criteri di successo:** [Come verrà misurato il successo della modifica?]
- **Durata del monitoraggio:** [Per quanto tempo verrà monitorata la modifica post-implementazione?]

---

# Metodologia di valutazione del rischio

## Scopo

Fornire una metodologia dettagliata per la valutazione del rischio delle modifiche in base all'impatto e alla probabilità, determinare l'autorità di approvazione appropriata e identificare le strategie di mitigazione del rischio.

## Valutazione dell'impatto

### Definizioni dei livelli di impatto

| Livello di impatto | Definizione | Ambito |
|-------------------|-------------|--------|
| **Basso** | Impatto minimo, facilmente reversibile | Singolo utente, singolo sistema non critico, recupero <15 min |
| **Medio** | Impatto moderato, rollback fattibile | Team/più utenti, sistemi non critici, recupero <2 ore |
| **Alto** | Impatto significativo, rollback complesso | Dipartimento, sistema principale, interruzione del processo aziendale, recupero <8 ore |
| **Critico** | Impatto grave, recupero difficile | A livello organizzativo, sistema mission-critical, rivolto ai clienti, recupero >8 ore o irreversibile |

### Dimensioni della valutazione dell'impatto

**Utenti interessati:** Basso: <10 / Medio: 10-100 / Alto: 100-1000 / Critico: >1000

**Processi aziendali:** Basso: Opzionale / Medio: Importante / Alto: Critico con soluzioni alternative / Critico: Mission-critical

**Impatto finanziario:** Basso: <10.000 € / Medio: 10.000-100.000 € / Alto: 100.000-1.000.000 € / Critico: >1.000.000 €

**Normativo/Conformità:** Basso: Nessuno / Medio: Reportistica interessata / Alto: Rischio di scadenza / Critico: Potenziale violazione

**Reputazione:** Basso: Solo interno / Medio: Inconveniente per i clienti / Alto: Visibilità pubblica / Critico: Impatto importante

**Complessità del recupero:** Basso: <15 min / Medio: <2 ore / Alto: <8 ore / Critico: Molto complesso o irreversibile

**Impatto complessivo:** Livello più alto in tutte le dimensioni (valutazione più conservativa)

## Valutazione della probabilità

### Definizioni dei livelli di probabilità

| Probabilità | Definizione | Tasso di successo tipico |
|-------------|-------------|--------------------------|
| **Bassa** | Molto improbabile che fallisca | >95% di successo |
| **Media** | Moderata possibilità di problemi | 75-95% di successo |
| **Alta** | Significativa possibilità di problemi | <75% di successo |

### Fattori di valutazione della probabilità

**Complessità della modifica:** Bassa: Semplice / Media: Moderata / Alta: Complessa

**Stabilità dell'ambiente:** Bassa: Stabile / Media: Problemi occasionali / Alta: Problemi frequenti

**Esperienza del team:** Bassa: Esperto / Media: Qualche esperienza / Alta: Nuova procedura/team

**Completezza dei test:** Bassa: Ampiamente testato / Media: Ben testato / Alta: Limitato/Non testato

**Dipendenze:** Bassa: Nessuna / Media: Poche / Alta: Molte dipendenze complesse

## Matrice del rischio

**Rischio complessivo = Impatto × Probabilità**

| Impatto ↓ / Probabilità → | Bassa | Media | Alta |
|--------------------------|-------|-------|------|
| **Basso** | Basso | Basso | Medio |
| **Medio** | Basso | Medio | Alto |
| **Alto** | Medio | Alto | Critico |
| **Critico** | Alto | Critico | Critico |

## Autorità di approvazione per livello di rischio

| Livello di rischio | Autorità di approvazione | Requisiti aggiuntivi |
|-------------------|--------------------------|----------------------|
| **Basso** | Responsabile delle modifiche | Documentazione standard |
| **Medio** | CAB | Documentazione standard |
| **Alto** | CAB + Direzione IT senior | Documentazione completa |
| **Critico** | CAB + RSSI + Direzione generale | Documentazione completa + Briefing esecutivo |
| **Emergenza** | E-CAB (Resp. Operazioni IT + RSSI) | Revisione CAB retrospettiva entro 48 ore |

---

# Guida di riferimento rapido

## Albero decisionale per il tipo di modifica

**INIZIA QUI → È necessaria questa modifica?**

```
├─ La modifica è già nel Catalogo delle modifiche standard?
│   ├─ SÌ → Modifica standard
│   │        ▼
│   │   • Inviare la richiesta di modifica (self-service OK)
│   │   • Nessuna approvazione CAB necessaria
│   │   • Seguire la procedura del catalogo
│   │   • Registrare nel sistema delle modifiche
│   │
│   └─ NO → Continuare...
│
├─ È una situazione di emergenza?
│   ├─ SÌ → Soddisfa TUTTI i criteri di emergenza?
│   │        • Azione immediata richiesta?
│   │        • Incidente critico/sicurezza/guasto?
│   │        • Rischio dell'inazione > rischio dell'azione?
│   │        ▼
│   │   ├─ SÌ → Modifica di emergenza
│   │   │        • Contattare E-CAB immediatamente
│   │   │        • Documentare la giustificazione
│   │   │        • Approvazione accelerata
│   │   │        • PIR obbligatorio entro 2 giorni
│   │   │
│   │   └─ NO → Modifica normale urgente
│   │            • Convocare una riunione CAB speciale
│   │            • Accelerare ma seguire il processo completo
│   │
│   └─ NO → Modifica normale
│            ▼
│       • Inviare la richiesta di modifica
│       • Valutazione del rischio
│       • Revisione CAB
│       • Processo completo
```

## Riferimento rapido per l'autorità di approvazione

| Livello di rischio | Chi approva | Tempistica tipica |
|-------------------|-------------|-------------------|
| **Basso** (Standard) | Responsabile delle modifiche | Immediato — 1 giorno |
| **Medio** (Normale) | CAB | Riunione CAB settimanale |
| **Alto** (Normale) | CAB + Direzione IT senior | 1-2 settimane |
| **Critico** (Normale) | CAB + RSSI + Direzione generale | 2-4 settimane |
| **Emergenza** | E-CAB | <4 ore |

## Lista di controllo delle informazioni richieste

**Ogni richiesta di modifica necessita di:**

- [ ] Descrizione chiara (cosa viene modificato?)
- [ ] Giustificazione aziendale (perché?)
- [ ] Valutazione del rischio (impatto + probabilità)
- [ ] Sistemi interessati (dal CMDB)
- [ ] Piano di implementazione (passo-passo)
- [ ] Test completati (o piano se emergenza)
- [ ] Piano di rollback (come annullare)
- [ ] Piano di comunicazione (chi notificare)

## Lista di controllo per le modifiche di emergenza

**Prima di dichiarare l'emergenza:**

- [ ] Incidente critico o vulnerabilità di sicurezza?
- [ ] Azione immediata richiesta per prevenire un impatto significativo?
- [ ] Rischio del NON modificare > rischio della modifica?
- [ ] Nessun tempo per la normale revisione CAB?

**Se SÌ a tutte le precedenti → Modifica di emergenza:**
1. Contattare E-CAB (Resp. Operazioni IT + RSSI)
2. Documentare la giustificazione dell'emergenza
3. Ottenere l'approvazione accelerata
4. Implementare con monitoraggio
5. Condurre il PIR entro 48 ore
6. Presentare al CAB retrospettivamente

## Contatti chiave

**Responsabile delle modifiche:** [Nome, Email, Telefono]  
**Presidente del CAB:** [Nome, Email, Telefono]  
**E-CAB (Emergenza):** [Nomi, Email, Telefoni]  
**Responsabile delle operazioni IT:** [Nome, Email, Telefono]  
**RSSI:** [Nome, Email, Telefono]

**Percorso di escalation:**
1. Responsabile delle modifiche
2. Responsabile delle operazioni IT
3. RSSI
4. CIO

## Errori comuni da evitare

1. ❌ **Invio di richieste di modifica incomplete** → Approvazioni mancanti ritardate
2. ❌ **Saltare i test "perché urgente"** → Incidenti in produzione
3. ❌ **Nessun piano di rollback** → Interruzioni prolungate quando la modifica fallisce
4. ❌ **Dimenticare di comunicare** → Utenti e dirigenti insoddisfatti
5. ❌ **Classificazione errata come emergenza** → Erosione del processo
6. ❌ **Nessun aggiornamento della documentazione** → Confusione operativa
7. ❌ **Saltare il PIR** → Lezioni non apprese, errori ripetuti
8. ❌ **Implementare senza approvazione** → Violazione della conformità, rischio di carriera

## Consigli per il successo

✅ **Iniziare la richiesta di modifica in anticipo** — Non aspettare l'ultimo momento  
✅ **Essere accurati nella valutazione del rischio** — Meglio sicuri che dispiaciuti  
✅ **Testare in ambienti non di produzione** — Individuare i problemi prima della produzione  
✅ **Avere il piano di rollback pronto** — Sperare per il meglio, prepararsi per il peggio  
✅ **Comunicare in modo proattivo** — Le parti interessate apprezzano il preavviso  
✅ **Documentare tutto** — Il futuro te stesso ringrazierà il te stesso attuale  
✅ **Imparare dai fallimenti** — Il PIR è per il miglioramento, non per il biasimo

---

# Guida alla selezione degli strumenti

## Valutazione delle piattaforme ITSM

**Criteri chiave:**

- Soddisfa i requisiti minimi di capacità (Sezione 2)
- Interfaccia intuitiva per i richiedenti di modifiche
- Integrazione con gli strumenti esistenti (CMDB, ticketing)
- Capacità di reportistica e analisi
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
- Opzioni open-source (OTRS, iTop, osTicket)

## Migliori pratiche di configurazione

**Durante la configurazione degli strumenti di gestione delle modifiche:**
1. Iniziare con i workflow predefiniti, personalizzare solo quando necessario
2. Implementare i campi obbligatori per garantire la completezza
3. Configurare i workflow di approvazione basati sulla matrice del rischio
4. Configurare le notifiche email per tutte le parti interessate
5. Configurare il calendario delle modifiche con i periodi di blocco
6. Abilitare l'integrazione con il CMDB per una valutazione accurata dell'impatto
7. Configurare dashboard per il Responsabile delle modifiche e il CAB
8. Configurare modelli di report per le metriche richieste
9. Formare gli utenti prima del go-live
10. Pianificare la manutenzione e gli aggiornamenti continui

---

# Appendice: Modelli di moduli

## A.1 Modulo di richiesta di modifica (vuoto)

[Modulo vuoto completo corrispondente alla struttura della Sezione 3.2]

## A.2 Modello di giustificazione per le modifiche di emergenza

**Richiesta di modifica di emergenza**

- **ID modifica:** ___________
- **Inviato da:** ___________
- **Data/Ora:** ___________

**Criteri di emergenza soddisfatti:**

- [ ] Incidente critico che richiede risoluzione immediata
- [ ] Vulnerabilità di sicurezza che richiede patch immediata
- [ ] Guasto del sistema che richiede ripristino immediato
- [ ] Prevenzione di un guasto imminente del sistema
- [ ] Requisito normativo urgente

**Descrizione della situazione:**
[Descrivere la situazione critica che richiede la modifica di emergenza]

**Impatto se NON implementata immediatamente:**
[Descrivere le conseguenze del ritardo]

**Rischio se implementata senza test completi:**
[Riconoscere i rischi dell'implementazione accelerata]

**Misure di mitigazione:**
[Descrivere come i rischi verranno minimizzati nonostante l'urgenza]

**Approvazione E-CAB:**

- Responsabile delle operazioni IT: ___________ Data: ___________
- RSSI: ___________ Data: ___________

---

**FINE DEL RIFERIMENTO TECNICO**

---

*Questo riferimento tecnico supporta l'implementazione di ISMS-POL-A.8.32. Tutti i requisiti vincolanti sono definiti nel documento di politica.*

<!-- QA_VERIFIED: 2026-04-04 -->
