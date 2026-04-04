<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.31.3-IT:framework:POL:a.5.31.3 -->
**ISMS-POL-A.5.31.3 — Quadro di estrazione dei requisiti e mappatura dei controlli**
**Requisiti legali, normativi e contrattuali**

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Quadro di estrazione dei requisiti e mappatura dei controlli |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.31.3 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI | Quadro di politica iniziale per la prima certificazione ISO 27001:2022 |

---

# Introduzione e relazione con le sezioni 5.31.1 e 5.31.2

## Scopo di questa sezione di politica

Questa sezione di politica stabilisce il quadro sistematico di [Organizzazione] per tradurre gli obblighi normativi in controlli di sicurezza azionabili con piena tracciabilità. Definisce i processi attraverso i quali il testo legale e normativo viene trasformato in requisiti implementabili, mappato ai controlli ISO 27001 e monitorato fino alle prove.

**Questo è il «livello di traduzione»** del quadro di conformità normativa — il collegamento critico tra l'identificazione delle normative applicabili e la dimostrazione della conformità attraverso i controlli implementati.

## Progressione: Applicabilità → Requisiti → Controlli

**ISMS-POL-A.5.31.1** ha stabilito l'architettura complessiva del quadro e la struttura di governance.

**ISMS-POL-A.5.31.2** ha definito la metodologia sistematica per determinare QUALI normative si applicano a [Organizzazione].

**ISMS-POL-A.5.31.3** (questo documento) definisce la metodologia sistematica per determinare COSA richiedono le normative applicabili e COME [Organizzazione] si conforma attraverso i controlli ISO 27001. Risponde alle domande: «Quali obblighi specifici impongono queste normative?»; «Quali controlli di sicurezza soddisfano questi obblighi?»; «Dove sono le lacune nell'implementazione dei controlli?»; «Come dimostriamo la conformità attraverso le prove?»

**ISMS-POL-A.5.31.4** (successivo) definirà come [Organizzazione] monitora i cambiamenti normativi, gestisce gli aggiornamenti del quadro e mantiene prove pronte per l'audit.

## La sfida della traduzione

Le normative sono scritte nel linguaggio legale, i controlli di sicurezza nel linguaggio tecnico e organizzativo. La metodologia definita in questo documento risolve questa sfida attraverso: estrazione sistematica dei requisiti; categorizzazione dei requisiti; mappatura dei controlli; analisi delle lacune; tracciabilità completa.

---

# Processo di estrazione dei requisiti

## Metodologia di estrazione dei requisiti

L'estrazione dei requisiti è il processo sistematico di analisi del testo normativo per identificare specifici obblighi obbligatori che [Organizzazione] deve soddisfare. Questo processo trasforma un testo legale prolisso e basato su principi in requisiti discreti e azionabili adatti alla mappatura dei controlli.

### Lettura sistematica del testo normativo

Le normative hanno una struttura, sebbene vari a seconda della giurisdizione e del tipo. I tipi di struttura includono: leggi e atti (capitoli, sezioni, sottosezioni); normative e direttive (articoli, sezioni, allegati); standard (clausole, sottoclausole, requisiti, raccomandazioni); contratti (sezioni, clausole, allegati).

**Processo di lettura sistematica**:

1. Rivedere l'intera normativa per comprendere l'intento e il perimetro generali
2. Identificare i confini strutturali (dove finisce un requisito e ne inizia un altro)
3. Analizzare ogni sezione/articolo per obblighi discreti
4. Distinguere tra obblighi obbligatori, raccomandazioni e informazioni contestuali
5. Estrarre ogni obbligo obbligatorio come requisito separato
6. Notare le interdipendenze dove i requisiti si riferiscono o dipendono da altri

### Identificazione del linguaggio obbligatorio vs. raccomandativo

**Linguaggio obbligatorio** (DEVE estrarre):

- **«deve»** (shall/must) — indicatore primario dell'obbligo legale
- **«è tenuto a»** — obbligo esplicito
- **«ha l'obbligo di»** — obbligo esplicito

**Linguaggio raccomandativo** (PUÒ estrarre come opzionale/buona pratica):

- **«dovrebbe»** (should) — raccomandazione, non obbligatoria
- **«è incoraggiato a»** — azione volontaria
- **«può»** — permissivo, opzionale

**Linguaggio condizionale** (estrarre CON le condizioni):

- **«deve, ove applicabile»** — obbligatorio quando la condizione è soddisfatta
- **«deve, se [condizione]»** — obbligatorio quando esiste una circostanza specifica

**Esempi di decisioni di estrazione**:

| Testo normativo | Obbligatorio? | Decisione di estrazione |
|----------------|---------------|------------------------|
| «Le organizzazioni devono implementare la cifratura per i dati a riposo» | Sì (deve) | Estrarre: «Implementare la cifratura per i dati a riposo» |
| «Le organizzazioni dovrebbero considerare l'autenticazione multi-fattore» | No (dovrebbe) | Notare come buona pratica, non estrarre come requisito |
| «Dove vengono trattati dati personali, le organizzazioni devono ottenere il consenso» | Condizionale | Estrarre: «Ottenere il consenso quando si trattano dati personali» |

### Linee guida sulla granularità

I requisiti devono essere estratti al giusto livello di dettaglio — abbastanza specifici da essere azionabili, ma non così prescrittivi da eliminare la flessibilità di implementazione.

**Troppo grossolano** (non azionabile): ❌ «Rispettare l'Articolo 32»; ❌ «Implementare misure di sicurezza adeguate».

**Troppo dettagliato** (eccessivamente prescrittivo): ❌ «Utilizzare la cifratura AES-256-GCM con derivazione della chiave PBKDF2 con 10.000 iterazioni».

**Giusto** (azionabile con flessibilità): ✅ «Implementare la cifratura per i dati a riposo utilizzando algoritmi standard del settore e lunghezze di chiave appropriate alla sensibilità dei dati»; ✅ «Condurre valutazioni delle vulnerabilità di tutti i sistemi rivolti a Internet almeno trimestralmente».

**Quadro di decisione sulla granularità**: Qualcuno può implementare questo senza indovinare? → Lascia spazio per scelte di implementazione ragionevoli? → Può essere mappato a uno o più controlli? → Può essere raccolta una prova per dimostrare la conformità?

## Categorizzazione dei requisiti

Una volta estratti, i requisiti vengono categorizzati per natura per facilitare la mappatura dei controlli.

### Requisiti tecnici

Requisiti che impongono specifiche misure di sicurezza tecniche, configurazioni di sistema o implementazioni tecnologiche.

**Caratteristiche**: Richiedono implementazione tecnica; implementati da team IT, Ingegneria della sicurezza, Sviluppo; possono essere verificati tecnicamente (scansioni, audit, test).

**Esempi generici**: «Implementare la segmentazione di rete per isolare i sistemi sensibili»; «Distribuire la protezione anti-malware su tutti gli endpoint»; «Abilitare la cifratura per i dati in transito utilizzando TLS 1.2 o superiore»; «Implementare la raccolta automatizzata dei log e l'archiviazione centralizzata».

**Mappature di controllo tipiche**: Controlli del Dominio 8 (Controlli tecnologici): A.8.1–A.8.34.

### Requisiti organizzativi

Requisiti che impongono politiche, procedure, strutture di governance, ruoli, formazione o processi organizzativi.

**Caratteristiche**: Richiedono documentazione di politica/procedura; implementati da Legale, Conformità, HR, Direzione; verificati attraverso la revisione dei documenti e le interviste.

**Esempi generici**: «Stabilire e mantenere una politica di sicurezza delle informazioni approvata dalla direzione generale»; «Definire ruoli e responsabilità per la protezione dei dati»; «Condurre controlli sui precedenti per il personale con accesso a informazioni sensibili»; «Fornire formazione sulla sensibilizzazione alla sicurezza a tutti i dipendenti annualmente».

**Mappature di controllo tipiche**: Dominio 5 (Controlli organizzativi): A.5.1–A.5.37; Dominio 6 (Controlli sulle persone): A.6.1–A.6.8.

### Requisiti di segnalazione

Requisiti che impongono presentazioni, notifiche, divulgazioni o relazioni alle autorità normative, agli interessati o ad altre parti esterne.

**Caratteristiche**: Sensibili al tempo (scadenze specifiche); rivolti all'esterno; spesso hanno formati o modelli prescritti; il mancato rispetto è direttamente visibile ai regolatori.

**Esempi generici**: «Notificare all'autorità di vigilanza le violazioni dei dati personali entro 72 ore dall'acquisizione della consapevolezza»; «Presentare l'attestazione annuale di conformità all'organismo normativo entro il 31 marzo»; «Notificare agli interessati gli incidenti di sicurezza che coinvolgono le loro informazioni personali senza indebito ritardo».

### Requisiti operativi

Requisiti che impongono procedure operative, pratiche, processi o attività di gestione specifici.

**Esempi generici**: «Condurre valutazioni annuali del rischio per i sistemi di informazione»; «Mantenere un inventario di tutti i sistemi IT e degli asset informativi»; «Eseguire test di ripristino trimestrali dell'infrastruttura di backup»; «Rivedere e aggiornare le procedure operative documentate almeno annualmente».

## Registro dei requisiti

Tutti i requisiti estratti DEVONO essere documentati nel Registro dei requisiti — il repository centrale di tutti i requisiti normativi estratti.

**Attributi obbligatori**:

| Attributo | Descrizione | Esempio |
|-----------|-------------|---------|
| **ID requisito** | Identificativo univoco | REG-RGPD-32-001 |
| **ID normativa** | Collegamento a ISMS-POL-00 | REG-RGPD |
| **Citazione della normativa** | Articolo/sezione specifica | Art. 32(1)(a) |
| **Testo del requisito** | Obbligo estratto | «Implementare la cifratura appropriata dei dati personali» |
| **Categoria** | Tecnico/Organizzativo/Segnalazione/Operativo | Tecnico |
| **Priorità** | Critica/Alta/Media/Bassa | Alta |
| **Stato di implementazione** | Non iniziato/In corso/Implementato/Verificato | Implementato |
| **Data di implementazione** | Quando il requisito è stato soddisfatto | 2026-01-15 |
| **Controllo primario** | Controllo ISO 27001 principale | A.8.24 |
| **Data dell'ultima revisione** | Ultima verifica della mappatura | 2026-03-01 |

---

# Metodologia di mappatura dei controlli

## Struttura di mappatura

Ogni requisito estratto DEVE essere mappato ai controlli ISO 27001:2022 Allegato A che soddisfano quel requisito.

### Tipi di mappatura

| Tipo di mappatura | Simbolo | Definizione | Criteri |
|------------------|---------|-------------|---------|
| **Controllo primario** | P | Soddisfa direttamente e sostanzialmente il requisito | Controllo è progettato SPECIFICAMENTE per affrontare il requisito; implementazione del controllo soddisfa il requisito senza controlli aggiuntivi |
| **Controllo secondario** | S | Soddisfa parzialmente il requisito o supporta il soddisfacimento | Controllo è CORRELATO al requisito ma non lo soddisfa completamente da solo |
| **Controllo di supporto** | Su | Contribuisce indirettamente al soddisfacimento | Controllo ABILITA o MIGLIORA il controllo primario |

**Regola dei tre livelli**: Ogni requisito DEVE avere almeno un controllo Primario. I controlli Secondari e di Supporto sono opzionali ma raccomandati dove esiste un allineamento significativo. I controlli non correlati NON DEVONO essere mappati.

**Qualità della mappatura**: Preferibilità ai controlli Primari dove tecnicamente accurato. Utilizzo conservativo dei controlli Secondari (solo per allineamento parziale genuino). I controlli di Supporto riservati a contributi indiretti chiari.

## Approccio alla mappatura

**Processo di mappatura per ciascun requisito estratto**:

1. Leggere attentamente il testo del requisito e la citazione della normativa originale per il contesto
2. Identificare il concetto principale di sicurezza affrontato (controllo degli accessi, crittografia, gestione degli incidenti, ecc.)
3. Consultare la Guida all'implementazione IMP-A.5.31.3 per i pattern di mappatura comuni
4. Per ogni controllo ISO 27001 potenziale: determinare se il controllo è Primario, Secondario o di Supporto
5. Convalidare la mappatura con il linguaggio del controllo (il controllo è PROGETTATO per questo scopo?)

**Pattern di mappatura comuni**:

| Tipo di requisito | Controlli primari tipici |
|------------------|--------------------------|
| Cifratura dei dati | A.8.24 (Utilizzo della crittografia) |
| Controllo degli accessi | A.5.15 (Controllo degli accessi) |
| Formazione sulla sensibilizzazione | A.6.3 (Sensibilizzazione, formazione e addestramento) |
| Notifica di violazioni | A.5.24-A.5.28 (Gestione degli incidenti) |
| Gestione del rischio | A.5.31 (Requisiti normativi), contribuisce a Clausola 6.1 |
| Politica di sicurezza | A.5.1 (Politiche per la sicurezza delle informazioni) |
| Gestione dei fornitori | A.5.19-A.5.23 (Sicurezza dei fornitori) |
| Registrazione e audit | A.8.15 (Registrazione), A.8.16 (Monitoraggio) |

## Analisi delle lacune

Per ciascun requisito nel Registro dei requisiti, analizzare:

**Stato della lacuna**: Il requisito ha un controllo Primario? Se NO → **GAP CRITICO** — Nessun controllo soddisfa direttamente il requisito; se SÌ e implementato → **CONFORME**; se SÌ ma non implementato → **GAP DI IMPLEMENTAZIONE**.

**Valutazione della copertura**:

- **Copertura completa**: Controllo Primario identificato e implementato; prove sufficienti disponibili
- **Copertura parziale**: Controllo Primario identificato ma implementato solo parzialmente; oppure Controllo Secondario soddisfa il requisito in modo incompleto
- **Nessuna copertura**: Nessun controllo soddisfa il requisito

### Prioritizzazione delle lacune

Le lacune vengono prioritizzate per guidare la pianificazione del rimedio:

**Lacune critiche** (rimedio entro 30 giorni): Normativa di Livello 1 (Obbligatoria); rimedi di sicurezza immediati richiesti; scadenze normative imminenti.

**Lacune alte** (rimedio entro 90 giorni): Normativa di Livello 1; non critica ma materialmente significativa.

**Lacune medie** (rimedio entro 180 giorni): Normativa di Livello 1 con impatto moderato; normativa di Livello 2 con significativa probabilità futura.

**Lacune basse** (rimedio entro 365 giorni o accettazione del rischio): Normativa di Livello 2 con bassa probabilità di diventare obbligatoria; normativa di Livello 3.

### Approcci al rimedio delle lacune

Per ciascuna lacuna, l'approccio al rimedio DEVE essere selezionato e documentato:

**1. Adottare un nuovo controllo**: Identificare e implementare un controllo non attualmente nel SGSI di [Organizzazione]. Giustificazione: La lacuna rappresenta un requisito senza un controllo esistente nelle vicinanze.

**2. Migliorare un controllo esistente**: Espandere la portata o migliorare l'implementazione di un controllo esistente. Giustificazione: La lacuna è una copertura parziale; il controllo esiste ma non soddisfa completamente il requisito.

**3. Controllo compensativo**: Implementare uno o più controlli alternativi che insieme soddisfano il requisito normativo.

**4. Accettare il rischio**: Documentare la lacuna come rischio accettato con la comprensione delle implicazioni della non conformità. Requisiti: il rischio DEVE essere formalmente documentato; l'accettazione del rischio deve essere approvata dalla Direzione generale; il processo di accettazione del rischio DEVE valutare l'esposizione normativa.

**5. Eccezione**: Richiedere un'eccezione alla conformità alla normativa. Requisiti: giustificazione aziendale documentata; parere del consulente legale; approvazione della Direzione generale; monitoraggio continuo.

## Tracciabilità

Il quadro di conformità normativa DEVE mantenere una tracciabilità completa che consenta di tracciare da qualsiasi normativa attraverso i requisiti e i controlli fino alle prove, e viceversa.

### Tracciabilità in avanti (Normativa → Prove)

```
Normativa (ISMS-POL-00)
  ↓
Requisiti estratti (Registro dei requisiti)
  ↓
Controlli ISO 27001 (Matrice di mappatura dei controlli)
  ↓
Implementazione dei controlli (Prove di controllo)
  ↓
Prove di conformità (Registro delle prove)
```

**Caso d'uso**: Un auditor chiede «Come dimostrate la conformità all'Art. 32 del RGPD?»

[Organizzazione] segue la tracciabilità in avanti: Normativa RGPD → Requisiti Art. 32 estratti (Registro dei requisiti) → Controllo A.8.24 (Matrice di mappatura) → Politica di cifratura, configurazioni (Registro delle prove).

### Tracciabilità inversa (Prove → Normativa)

```
Prove di conformità (Registro delle prove)
  ↓
Controllo ISO 27001 (Matrice di mappatura dei controlli)
  ↓
Requisiti estratti (Registro dei requisiti)
  ↓
Normativa (ISMS-POL-00)
```

**Caso d'uso**: Viene raccolto un nuovo elemento di prova. Quali requisiti normativi supporta?

### Tracciabilità dei cambiamenti

Quando le normative cambiano: aggiornare il Registro dei requisiti (aggiungere/modificare/rimuovere requisiti interessati); aggiornare la Matrice di mappatura (adeguare le mappature dei controlli interessati); identificare le lacune di prove (prove esistenti ancora valide?).

## Gestione dei requisiti sovrapposti da più normative

Quando più normative applicabili contengono requisiti che si sovrappongono, [Organizzazione] adotta il **principio del requisito più stringente**.

**Processo di identificazione dei requisiti sovrapposti**:

1. Per ogni coppia di normative in ISMS-POL-00, identificare aree di sovrapposizione potenziale
2. Esaminare i requisiti estratti da entrambe le normative per la stessa area (es. cifratura, controllo degli accessi, notifica delle violazioni)
3. Se due o più requisiti affrontano lo stesso controllo/processo di sicurezza, classificare come set sovrapposto

**Determinazione del più stringente**: Confrontare i requisiti sovrapposti utilizzando: standard tecnici (standard di cifratura più forti soddisfano tutti); frequenze dei processi (la frequenza più alta soddisfa tutte); requisiti di documentazione (la documentazione più completa soddisfa tutti); scadenze (la scadenza più breve soddisfa tutte).

**Esempio**:

| Requisito | Frequenza | Confronto della stringenza |
|-----------|-----------|--------------------------|
| REG-RGPD: «Rivedere i diritti di accesso periodicamente» | Non specificato | Meno stringente |
| REG-FIN05: «Rivedere i diritti di accesso annualmente» | Annuale | Moderatamente stringente |
| REG-PCI: «Rivedere i diritti di accesso trimestralmente» | Trimestrale | **Più stringente** (più frequente) |

**Implementazione**: Revisioni trimestrali degli accessi (soddisfa tutti e tre i requisiti)

---

# Controllo del documento e documenti correlati

**ID documento**: ISMS-POL-A.5.31.3
**Frequenza di revisione**: Annuale o in caso di significativi cambiamenti normativi che interessano più normative; aggiornamenti principali della norma ISO 27001; cambiamenti organizzativi che interessano il perimetro della conformità.

**Documenti correlati**:

- ISMS-POL-A.5.31.1 (fondamento del quadro e struttura di governance)
- ISMS-POL-A.5.31.2 (determina QUALI normative si applicano — input a questo documento)
- ISMS-POL-00 (registro normativo principale — fonte delle normative per l'estrazione dei requisiti)
- ISMS-POL-A.5.31.4 (gestione dei cambiamenti e delle prove — a valle)
- ISMS-IMP-A.5.31.3-UG/TG (guida passo-passo per il processo di estrazione e mappatura)
- Classeur 3 (Registro dei requisiti — modello per il Registro dei requisiti)
- Classeur 4 (Matrice di mappatura dei controlli — prepopolata con 93 controlli dell'Allegato A)

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Mappatura dei controlli** | Processo di collegamento dei requisiti normativi ai controlli ISO 27001 che soddisfano tali requisiti |
| **Lacuna** | Requisito normativo per il quale non esiste alcun controllo o i controlli esistenti sono inadeguati |
| **Controllo primario (P)** | Controllo che soddisfa direttamente e sostanzialmente un requisito normativo |
| **Registro dei requisiti** | Repository autorevole di tutti i requisiti estratti dalle normative applicabili |
| **Controllo secondario (S)** | Controllo che soddisfa parzialmente o supporta il soddisfacimento di un requisito normativo |
| **Controllo di supporto (Su)** | Controllo che contribuisce indirettamente al soddisfacimento di un requisito normativo |
| **Tracciabilità** | Capacità di tracciare in avanti (normativa → prove) e all'indietro (prove → normativa) attraverso requisiti e controlli |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile del SGSI / Responsabile della Conformità** | [Nome] | [Data] |
| **Consulente legale** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce la metodologia di traduzione dal testo normativo ai controlli azionabili, consentendo a [Organizzazione] di dimostrare COME soddisfa i requisiti normativi attraverso l'implementazione sistematica dei controlli.*

<!-- QA_VERIFIED: 2026-04-03 -->
