<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.33-34-IT:operational:OP-POL:a.8.33-34 -->
**ISMS-OP-POL-A.8.33-34 — Informazioni di test e protezione dei sistemi informativi durante l'audit**

---

**Controllo del documento**

| Campo | Valore |
|-------|-------|
| **Titolo del documento** | Informazioni di test e protezione dei sistemi informativi durante l'audit |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.33-34 |
| **Creatore del documento** | Responsabile della Sicurezza delle Informazioni (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|---------|------|--------|---------|
| 1.0 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.8.33 — Informazioni di test
- ISO/IEC 27001:2022 Controllo A.8.34 — Protezione dei sistemi informativi durante l'audit
- ISO/IEC 27002:2022 Sezioni 8.33 e 8.34 — Linee guida di implementazione
- NIST SP 800-53 Rev 5 — SA-11 (Test e valutazione da parte degli sviluppatori), CA-8 (Penetration testing), AU-11 (Conservazione dei record di audit)
- CIS Controls v8 — Salvaguardia 3.1–3.14 (Protezione dei dati), Salvaguardia 18.1–18.5 (Penetration testing)

**Controlli Annex A correlati**:

| Controllo | Relazione con le informazioni di test e la protezione dell'audit |
|---------|------------------------------------------------------|
| A.5.9 Inventario delle informazioni e degli altri asset associati | Gli ambienti di test e gli strumenti di audit inclusi nell'inventario degli asset |
| A.5.15–16–18 Gestione delle identità e degli accessi | Provisioning degli accessi per auditor e tester, controlli degli accessi a tempo limitato |
| A.5.24–28 Ciclo di vita della gestione degli incidenti | Gestione degli incidenti durante l'audit; escalation della scoperta di vulnerabilità |
| A.5.34 Privacy e dati personali | Protezione dei dati personali nei dati di test; requisiti di anonimizzazione e pseudonimizzazione |
| A.8.2–3–5 Autenticazione e accesso privilegiato | Requisiti AMF per l'accesso all'ambiente di test; autenticazione degli auditor |
| A.8.8 Gestione delle vulnerabilità | Gestione delle vulnerabilità per i risultati del penetration testing e dell'audit |
| A.8.11 Mascheratura dei dati | Tecniche di mascheratura dei dati applicate ai dati di produzione utilizzati nei test |
| A.8.15 Registrazione | Audit trail per la gestione dei dati di test e le attività di accesso degli auditor |
| A.8.16 Monitoraggio | Monitoraggio in tempo reale durante l'audit attivo e il penetration testing |
| A.8.31 Separazione degli ambienti di sviluppo, test e produzione | Isolamento degli ambienti per la protezione dei dati di test |

**Politiche interne correlate**:

- Politica di gestione delle identità e degli accessi
- Politica di mascheratura dei dati
- Politica di registrazione e monitoraggio
- Politica delle attività di monitoraggio (A.8.16)
- Politica di gestione delle vulnerabilità
- Politica di gestione degli incidenti
- Politica di classificazione e gestione delle informazioni
- Politica di separazione degli ambienti

---

# Politica sulle informazioni di test e la protezione dell'audit

## Scopo

Lo scopo di questa politica è garantire che le informazioni di test siano selezionate, protette e gestite in modo appropriato, e che i test di audit e le altre attività di assurance che coinvolgono la valutazione dei sistemi operativi siano pianificati e concordati per minimizzare le interruzioni pur mantenendo l'integrità del sistema.

Questa politica affronta due preoccupazioni complementari: proteggere i dati sensibili dall'esposizione attraverso gli ambienti di test (A.8.33), e proteggere i sistemi operativi da impatti non intenzionali durante l'audit e il testing della sicurezza (A.8.34).

Questa politica supporta la nLPD svizzera (revDSG) Art. 8 implementando misure tecniche e organizzative appropriate al rischio per proteggere i dati personali utilizzati o esposti attraverso gli ambienti di test. Dove l'organizzazione tratta dati di individui nell'UE/SEE, si applicano anche i requisiti del GDPR Art. 25 (protezione dei dati fin dalla progettazione e per impostazione predefinita) e Art. 32 (sicurezza del trattamento). La gestione dei dati di test è una misura tecnica fondamentale per dimostrare che i dati personali non sono inutilmente esposti attraverso ambienti non di produzione.

## Ambito

Questa politica si applica a tutte le attività di selezione, creazione, protezione e smaltimento dei dati di test, e a tutte le attività di audit, penetration testing e assurance che coinvolgono la valutazione dei sistemi operativi.

Ciò include:

- Tutti i dati di test utilizzati negli ambienti di sviluppo, QA, staging, UAT, formazione, sandbox e dimostrazione.
- Tutte le copie, gli estratti o i derivati dei dati di produzione utilizzati a scopo di test.
- Tutti i dataset di test sintetici, anonimizzati, pseudonimizzati e mascherati.
- Tutti gli audit e le valutazioni di sicurezza interni.
- Tutti gli audit di certificazione esterni (ISO 27001 ed equivalenti).
- Tutti i penetration testing, le valutazioni delle vulnerabilità e i test di sicurezza attivi.
- Tutte le valutazioni di sicurezza di terze parti e gli audit di conformità normativa.
- Tutto il personale coinvolto nelle attività di test, audit o assurance, inclusi dipendenti, collaboratori esterni, auditor interni, auditor esterni e penetration tester.

**Fuori ambito**: Operazioni dell'ambiente di produzione (coperte dalle politiche operative); monitoraggio automatizzato di routine (coperto da A.8.16); specifiche delle tecniche di mascheratura dei dati e configurazione degli strumenti (coperto da A.8.11); architettura e requisiti di separazione degli ambienti (coperto da A.8.31); pratiche di codifica sicura e testing dello sviluppo (coperto da A.8.25–26–29).

## Principio

I dati di test devono essere trattati come un potenziale vettore di violazione dei dati. La posizione predefinita è che i dati di produzione contenenti dati personali, informazioni sensibili o dati aziendali riservati non devono essere utilizzati negli ambienti di test. Dove sono necessari dati derivati dalla produzione, devono essere anonimizzati, pseudonimizzati o mascherati prima dell'uso.

Le attività di audit e assurance devono essere condotte con l'accesso e l'impatto minimo necessari per raggiungere i propri obiettivi. Gli auditor devono ricevere l'accesso in sola lettura per impostazione predefinita, il testing deve essere limitato nel tempo e nell'ambito, e i sistemi operativi devono essere protetti da interruzioni non intenzionali.

---

## Selezione dei dati di test

L'organizzazione deve stabilire una chiara gerarchia di preferenze per le fonti dei dati di test.

**Gerarchia delle fonti di dati di test** (in ordine di preferenza):

| Priorità | Fonte di dati | Descrizione | Approvazione richiesta |
|----------|-------------|-------------|-------------------|
| 1 | **Dati sintetici** | Dati generati artificialmente senza alcuna relazione con individui o registrazioni aziendali reali | Responsabile dello sviluppo |
| 2 | **Dati anonimizzati** | Dati di produzione de-identificati irreversibilmente dove la re-identificazione non è ragionevolmente possibile | Responsabile della sicurezza delle informazioni |
| 3 | **Dati pseudonimizzati** | Dati di produzione con identificatori sostituiti da pseudonimi; re-identificabili con chiave separata | Responsabile della sicurezza delle informazioni + Proprietario dei dati |
| 4 | **Dati di produzione mascherati** | Dati di produzione con campi sensibili oscurati utilizzando tecniche di mascheratura approvate | RSSI + Proprietario dei dati |
| 5 | **Copia diretta della produzione** | Dati di produzione non modificati (solo in circostanze eccezionali) | RSSI + DPD + Proprietario dei dati |

Le copie dirette della produzione sono consentite solo dove tutte le altre opzioni sono dimostrativamente inadeguate, con giustificazione documentata, approvazione a tempo limitato (massimo 30 giorni), controlli degli accessi potenziati e cancellazione obbligatoria al completamento.

**Albero decisionale per la fonte dei dati di test**:

Per determinare la fonte appropriata dei dati di test, applicare la seguente logica decisionale:

```
Il test richiede caratteristiche di dati reali (distribuzioni, casi limite)?
+-- NO --> Utilizzare Dati sintetici (Priorità 1)
+-- SI
    +-- È possibile generare dati sintetici con quelle caratteristiche?
        +-- SI --> Utilizzare Dati sintetici (Priorità 1)
        +-- NO
            +-- I dati sono dati personali ai sensi della nLPD/GDPR?
                +-- NO --> Utilizzare Dati di produzione mascherati (Priorità 4)
                +-- SI
                    +-- È possibile rendere impossibile la re-identificazione?
                        +-- SI --> Utilizzare Dati anonimizzati (Priorità 2)
                        +-- NO --> Utilizzare Dati pseudonimizzati (Priorità 3)
                            (Richiede approvazione Responsabile sicurezza informazioni + Proprietario dati)
```

Dove una decisione risulta nella Priorità 3 o superiore, il Proprietario dei dati e il Responsabile della sicurezza delle informazioni devono essere consultati prima di procedere.

**Classificazione dei dati di test**: I dati di test devono essere classificati secondo lo schema di classificazione delle informazioni dell'organizzazione. I dati di test derivati dalla produzione ereditano la classificazione dei dati di origine fino a quando la mascheratura o l'anonimizzazione non è validata. I dati sintetici devono essere classificati in base al contesto aziendale (tipicamente Interno). La classificazione determina i controlli di protezione richiesti.

---

## Protezione dei dati di test

### Anonimizzazione e pseudonimizzazione

Quando si richiedono dati di produzione per i test, l'organizzazione deve applicare tecniche di protezione dei dati prima che i dati siano accessibili in qualsiasi ambiente di test.

**Requisiti di anonimizzazione**:

- L'anonimizzazione deve rendere la re-identificazione non ragionevolmente possibile, considerando i mezzi disponibili di re-identificazione, il costo della re-identificazione e lo scopo previsto.
- I dati anonimizzati non sono più dati personali ai sensi della nLPD o del GDPR e possono essere classificati a un livello inferiore con l'approvazione del Proprietario dei dati.
- Le tecniche di anonimizzazione devono essere validate prima dell'uso e revisionate annualmente per l'efficacia continua, tenendo conto dei progressi nelle tecniche di re-identificazione inclusi i metodi assistiti dall'IA.

**Requisiti di pseudonimizzazione**:

- I dati pseudonimizzati rimangono dati personali e devono essere protetti di conseguenza.
- La chiave di mappatura (pseudonimo-identità) deve essere archiviata separatamente dal dataset pseudonimizzato, con accesso limitato al personale autorizzato.
- I dati di test pseudonimizzati devono essere soggetti agli stessi controlli di accesso della classificazione originale dei dati.

### Mascheratura dei dati

La mascheratura dei dati deve essere applicata utilizzando [Strumento di mascheratura dei dati] (ad es. Informatica, Delphix, IBM InfoSphere Optim o equivalente) o metodi con script approvati.

**Requisiti di mascheratura**:

| Tipo di dati | Tecnica di mascheratura | Validazione |
|-----------|-------------------|------------|
| Nomi personali | Sostituzione con nomi sintetici | Verificare che non rimangano nomi originali |
| Indirizzi email | Sostituzione del dominio (ad es. @example.com) | Verificare che il formato sia preservato, nessun indirizzo reale |
| Identificatori nazionali (AVS/SSN) | Randomizzazione con preservazione del formato | Verificare che il formato sia valido ma inesistente |
| Dati finanziari (IBAN, numeri di conto) | Cifratura o randomizzazione con preservazione del formato | Verificare che il formato sia preservato, integrità referenziale mantenuta |
| Date di nascita | Spostamento delle date (scostamento coerente per record) | Verificare che le distribuzioni delle età siano preservate per il testing |
| Campi di testo libero | Redazione o sostituzione sintetica | Verificare che non vi siano fughe di dati personali nel testo non strutturato |
| Indirizzi | Sostituzione con indirizzi sintetici | Verificare che la distribuzione geografica sia preservata se necessario |

**Riferimento rapido per la mascheratura dei dati**:

| Tipo di dati | Tecnica consigliata | Esempio di strumento/metodo |
|-----------|----------------------|---------------------|
| Nomi | Sostituzione | Libreria Faker: `fake.name()` (locale svizzera) |
| Email | Cambio dominio | `user123@testdomain.example` |
| Numeri di telefono | Randomizzazione con preservazione del formato | Libreria Faker: `fake.phone_number()` |
| Date | Scostamento coerente | Tutte le date scalate di ±1-3 anni casualmente |
| Indirizzi | Sostituzione | Libreria Faker: `fake.address()` (locale svizzera) |
| Testo libero | Redazione o NER + sostituzione | Servizio cloud NLP + logica di sostituzione personalizzata |
| Valori finanziari | Cifratura con preservazione del formato | Algoritmo FPE con gestione delle chiavi approvata |

**Validazione della mascheratura**: I dati mascherati devono essere validati prima del rilascio negli ambienti di test per confermare che i valori sensibili originali non siano recuperabili, che il formato dei dati sia preservato per la compatibilità dell'applicazione, che l'integrità referenziale sia mantenuta tra i dataset correlati e che non esistano dati personali in chiaro nell'output mascherato. I risultati della validazione devono essere documentati e approvati dal Responsabile della sicurezza delle informazioni.

### Generazione di dati sintetici

Dove si utilizzano dati sintetici, questi devono essere generati per preservare le proprietà statistiche, le distribuzioni dei dati e l'integrità referenziale richiesta per un testing efficace senza contenere alcun dato personale o aziendale reale.

I generatori di dati sintetici devono essere documentati, sotto controllo versione e revisionati periodicamente per garantire che i dati generati rimangano adatti allo scopo. L'organizzazione deve mantenere registri dei parametri di generazione dei dati sintetici e dei risultati di validazione.

---

## Ciclo di vita dei dati di test

### Creazione e provisioning

- La creazione o il refresh dei dati di test deve essere richiesto attraverso un processo documentato.
- L'approvazione del Proprietario dei dati è richiesta prima che qualsiasi dato derivato dalla produzione entri in un ambiente di test.
- La mascheratura o l'anonimizzazione deve essere applicata prima che i dati siano accessibili nell'ambiente di test (non dopo).
- Tutte le attività di provisioning dei dati devono essere registrate a fini di audit.

### Conservazione e smaltimento

I dati di test contenenti dati di produzione mascherati o pseudonimizzati devono essere conservati solo per la durata del requisito di testing. Al completamento del progetto, i dati di test devono essere eliminati entro 30 giorni.

Per gli ambienti di testing continuo:

- I dati di test devono essere revisionati trimestralmente per la necessità continua.
- I dati più vecchi di 90 giorni senza utilizzo attivo documentato devono essere segnalati per l'eliminazione.
- La conservazione oltre i 90 giorni richiede l'approvazione del Proprietario dei dati con giustificazione aziendale documentata.
- Il monitoraggio automatico della conservazione deve avvisare quando i dati superano le soglie.

**Smaltimento**: Lo smaltimento dei dati di test deve seguire le stesse procedure di cancellazione sicura dei dati di produzione di classificazione equivalente. Lo smaltimento deve essere verificato e documentato.

### Refresh dei dati

Quando i dati di test vengono aggiornati dalle fonti di produzione:

- La nuova mascheratura deve essere applicata a ogni ciclo di refresh (la mascheratura precedente non si trasferisce).
- Le procedure di refresh devono essere documentate e approvate dal Proprietario dei dati.
- Le attività di refresh devono essere registrate, inclusi il sistema di origine, il volume, il metodo di mascheratura e l'operatore.
- I dati di test precedenti devono essere eliminati in modo sicuro prima o immediatamente dopo il completamento del refresh.

---

## Pianificazione dell'audit e governance

### Accordo pre-audit

Prima dell'inizio di qualsiasi test di audit, l'organizzazione deve stabilire un accordo formale tra il tester e la direzione appropriata che copra:

- **Ambito**: Sistemi, reti, applicazioni e dati da testare.
- **Metodologia**: Metodi, strumenti e tecniche di test da utilizzare.
- **Tempistiche**: Date di inizio e fine, finestre di test e periodi di esclusione.
- **Confini**: Sistemi e dati esplicitamente esclusi dal testing.
- **Escalation**: Procedure per problemi, incidenti o risultati critici durante il testing.
- **Riservatezza**: Requisiti di non divulgazione per i risultati dell'audit e i dati a cui si è avuto accesso.
- **Reportistica**: Deliverable attesi, formato e tempistiche per i risultati.

Gli accordi pre-audit devono essere documentati, firmati da entrambe le parti e conservati come evidenza.

### Pianificazione e coordinamento

Le attività di test di audit devono essere pianificate per minimizzare l'impatto operativo:

- I periodi aziendali critici (ad es. chiusura di fine mese, picchi di trading, finestre di manutenzione dei sistemi) devono essere evitati a meno che non si stia specificamente testando la resilienza durante quei periodi.
- Le finestre di test devono essere coordinate con le operazioni IT e i proprietari dei sistemi interessati.
- Gli stakeholder interessati devono essere notificati delle attività di test pianificate, incluse tempistiche, ambito e potenziale impatto.
- Il testing d'emergenza o non pianificato deve seguire un processo di approvazione accelerato con revisione post-facto entro 48 ore.

---

## Controllo degli accessi degli auditor

L'accesso concesso agli auditor, ai valutatori e ai penetration tester deve seguire il principio del privilegio minimo.

**Requisiti di accesso**:

| Requisito | Standard |
|-------------|----------|
| Livello di accesso predefinito | Solo lettura alle informazioni e al software |
| Accesso in scrittura o admin | Solo quando la sola lettura è insufficiente; un amministratore esegue l'accesso per conto dell'auditor dove fattibile |
| Autenticazione | AMF richiesta per l'accesso a qualsiasi sistema contenente dati sensibili |
| Durata | Limitata nel tempo al periodo di audit concordato; scadenza automatica |
| Ambito | Limitato ai sistemi e ai dati definiti nell'accordo pre-audit |
| Registrazione | Tutti gli accessi degli auditor registrati e monitorati per tutta la durata dell'incarico |

Dove l'accesso in sola lettura non è fattibile, un amministratore con i diritti di accesso necessari deve eseguire l'accesso al sistema o ai dati per conto dell'auditor, con l'auditor che osserva e dirige.

**Sicurezza dei dispositivi**: Prima di concedere l'accesso, l'organizzazione deve verificare che i dispositivi degli auditor soddisfino i requisiti minimi di sicurezza, inclusi patch del sistema operativo aggiornate, protezione endpoint attiva, cifratura completa del disco e assenza di malware noti. Gli auditor che utilizzano dispositivi non conformi devono ricevere dispositivi gestiti dall'organizzazione o accesso tramite desktop virtuale.

**Deprovisioning degli accessi**: L'accesso degli auditor deve essere revocato entro 24 ore dal completamento dell'audit o dalla data di scadenza dell'accesso concordato, a seconda di quale sia la prima. Il deprovisioning deve essere verificato e documentato.

---

## Controlli per il penetration testing

### Autorizzazione e regole di ingaggio

Il penetration testing e il testing di sicurezza attivo devono essere autorizzati per iscritto dal RSSI (o delegato) e dai proprietari dei sistemi interessati prima dell'inizio del testing.

**Le regole di ingaggio** devono documentare:

- L'ambito del testing autorizzato (intervalli IP, applicazioni, account, ubicazioni fisiche).
- Le attività vietate (denial of service, social engineering di individui specifici, esfiltrazione di dati reali).
- La metodologia e il framework di testing (ad es. OWASP Testing Guide, PTES, NIST SP 800-115).
- I protocolli di comunicazione (contatto principale, contatto d'emergenza, frequenza dei rapporti di stato).
- I requisiti per la gestione dei dati a cui si accede durante il testing.
- Le procedure per gli incidenti se il testing causa impatti operativi non intenzionali.
- La gestione delle evidenze e la distruzione sicura degli artefatti di test.

### Salvaguardie operative

Durante il penetration testing:

- Le operazioni IT devono essere in standby con la capacità di intervenire se i sistemi operativi sono interessati.
- Il testing deve essere condotto in ambienti isolati o non di produzione dove possibile.
- Dove è richiesto il testing in produzione, le procedure di rollback e ripristino devono essere preparate in anticipo.
- Il testing deve essere immediatamente sospeso se si verificano impatti operativi non intenzionali, e non deve riprendere senza l'approvazione esplicita del Responsabile delle operazioni IT e del RSSI.

### Gestione dei risultati

- Le vulnerabilità critiche scoperte durante il testing devono essere segnalate immediatamente al Team di sicurezza (non rinviate al rapporto finale).
- Le vulnerabilità devono essere gestite secondo il processo di gestione delle vulnerabilità dell'organizzazione (A.8.8).
- I tester non devono sfruttare le vulnerabilità oltre l'ambito necessario per la verifica e la valutazione del rischio.
- I rapporti di penetration testing devono essere classificati come Riservato e distribuiti solo ai destinatari autorizzati.

### Comunicazione dello stato del testing

Durante il penetration testing attivo o le attività di audit prolungate, il tester deve fornire aggiornamenti di stato giornalieri al contatto organizzativo designato. Gli aggiornamenti di stato devono includere:

- Sintesi delle attività completate nel periodo di riferimento.
- Sintesi dei risultati identificati (per gravità: Critico, Alto, Medio, Basso).
- Attività pianificate per il successivo periodo di riferimento.
- Eventuali problemi, preoccupazioni o impatti operativi osservati.

I risultati critici devono essere segnalati immediatamente per telefono al RSSI, oltre agli aggiornamenti di stato giornalieri. Il formato e la frequenza dei rapporti di stato devono essere concordati nell'accordo pre-audit.

---

## Gestione degli strumenti di audit

### Approvazione e controllo degli strumenti

Gli strumenti di audit e testing utilizzati per valutare i sistemi dell'organizzazione devono essere:

- Pre-approvati dal Responsabile della sicurezza delle informazioni prima dell'uso sui sistemi organizzativi.
- Verificati come privi di malware o funzionalità non autorizzate.
- Documentati nell'accordo pre-audit (nome dello strumento, versione, scopo).
- Limitati all'ambito di testing concordato.

Gli strumenti di audit non devono essere installati sui sistemi di produzione senza l'approvazione esplicita del RSSI. Dove possibile, gli strumenti di audit devono essere eseguiti da workstation di audit dedicate o ambienti virtuali isolati.

### Protezione degli strumenti

Gli strumenti di audit, gli script e i file di configurazione devono essere protetti da accessi non autorizzati sia durante che dopo l'incarico. Gli strumenti capaci di sfruttare vulnerabilità o di bypassare i controlli di sicurezza devono essere rimossi dai sistemi organizzativi al completamento dell'audit.

---

## Protezione del log di audit

I log generati durante le attività di audit e testing devono essere protetti da modifiche o cancellazioni non autorizzate per mantenere l'integrità dell'audit trail.

**Requisiti di protezione dei log**:

- I log di audit devono essere scritti in uno storage a prova di manomissione (ad es. supporti write-once, SIEM con controlli di integrità o equivalente).
- I log devono riportare: timestamp (UTC), identità dell'utente, IP di origine, azione eseguita, sistema interessato e risultato (successo/fallimento).
- I log generati durante l'audit testing devono essere conservati secondo la politica di conservazione dei log dell'organizzazione (minimo 1 anno per gli eventi di accesso, 3 anni per gli eventi di sicurezza).
- I log devono essere disponibili per la revisione se i risultati dell'audit sono contestati o richiedono chiarimenti.
- Durante il penetration testing attivo, il monitoraggio avanzato deve essere abilitato per distinguere le attività di testing autorizzate dagli eventi di sicurezza reali.

---

## Gestione degli incidenti durante l'audit testing

Se l'audit o il penetration testing causano impatti operativi non intenzionali:

1. **Sospensione immediata**: Il testing deve cessare immediatamente al rilevamento di impatti non intenzionali.
2. **Notifica**: Le operazioni IT devono essere notificate per il contenimento e il ripristino.
3. **Analisi della causa principale**: La causa dell'impatto non intenzionale deve essere documentata.
4. **Remediation**: I sistemi interessati devono essere ripristinati al normale funzionamento.
5. **Approvazione per la ripresa**: Il testing non deve riprendere senza l'approvazione esplicita del Responsabile delle operazioni IT.
6. **Lezioni apprese**: L'incidente deve essere documentato e incorporato nella pianificazione pre-audit futura.

Gli incidenti di sicurezza reali scoperti durante l'audit testing (ad es. evidenza di compromissione precedente, minacce attive) devono essere escalati immediatamente secondo il processo di gestione degli incidenti dell'organizzazione (A.5.24-28).

---

## Definizioni

| Termine | Definizione |
|------|------------|
| **Anonimizzazione** | Processo irreversibile di rimozione di tutte le informazioni identificative tale che la re-identificazione non sia ragionevolmente possibile |
| **Audit testing** | Esame sistematico di sistemi, controlli e processi per verificare la conformità e l'efficacia |
| **Mascheratura dei dati** | Processo di oscuramento dei dati originali con contenuto modificato mantenendo il formato e l'utilizzabilità per il testing |
| **Grey box testing** | Approccio di penetration testing in cui il tester ha una conoscenza parziale dell'ambiente target |
| **Penetration testing** | Attacco simulato autorizzato sui sistemi per identificare vulnerabilità di sicurezza sfruttabili |
| **Dati di produzione** | Dati operativi live dai sistemi aziendali contenenti informazioni personali o aziendali reali |
| **Pseudonimizzazione** | Sostituzione degli identificatori diretti con pseudonimi; re-identificabili con una chiave di mappatura archiviata separatamente |
| **Regole di ingaggio** | Accordo documentato che definisce l'ambito, i confini, i metodi e i vincoli per il penetration testing |
| **Dati sintetici** | Dati generati artificialmente privi di informazioni personali o aziendali reali, progettati per imitare le caratteristiche dei dati di produzione |
| **Ambiente di test** | Sistema non di produzione utilizzato per lo sviluppo, il testing, la formazione o la dimostrazione |

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|------|-----------------|
| **RSSI** | Proprietà della politica; autorizzazione del penetration testing; approvazione delle eccezioni per l'utilizzo diretto dei dati di produzione; supervisione della governance dell'audit testing; revisione annuale della politica; reportistica alla Direzione generale |
| **Responsabile della sicurezza delle informazioni** | Manutenzione della politica; coordinamento dell'audit; approvazione della validazione della mascheratura; revisione delle eccezioni; monitoraggio della conformità; reportistica trimestrale al RSSI |
| **Responsabile della protezione dei dati (DPD)** | Conformità della privacy dei dati di test; revisione dell'adeguatezza dell'anonimizzazione; allineamento alla nLPD e al GDPR; approvazione per l'utilizzo di dati pseudonimizzati |
| **Responsabile delle operazioni IT** | Protezione dei sistemi di produzione durante l'audit testing; coordinamento della pianificazione; risposta agli incidenti durante il testing; verifica dei dispositivi degli auditor |
| **Proprietari dei dati** | Autorizzazione dei dati di test; approvazione della mascheratura; decisioni di classificazione dei dati; revisione della conservazione per i dati di test derivati dai loro sistemi |
| **Responsabile dello sviluppo / Responsabile QA** | Gestione degli ambienti di test; procedure di provisioning dei dati di test; conformità degli sviluppatori e dei tester; supervisione della generazione dei dati sintetici |
| **Team di sicurezza** | Gestione degli strumenti di audit; coordinamento del penetration testing; gestione dei risultati delle vulnerabilità; monitoraggio avanzato durante il testing |
| **Audit interno** | Pianificazione e gestione degli incarichi di audit; preparazione degli accordi pre-audit; reportistica dei risultati e follow-up |
| **Auditor esterni e penetration tester** | Conformità alle restrizioni di accesso, alle regole di ingaggio e ai requisiti di riservatezza; rispetto dell'ambito; segnalazione immediata dei risultati critici |
| **Tutto il personale di testing** | Conformità ai requisiti di gestione dei dati di test; nessun utilizzo di dati di produzione non mascherati senza approvazione; segnalazione degli incidenti; smaltimento sicuro degli artefatti di test |

---

## Evidenze

Le seguenti evidenze dimostrano la conformità a questa politica:

| # | Evidenza | Proprietario | Frequenza | Conservazione |
|---|----------|-------|-----------|-----------|
| 1 | **Inventario dei dati di test** con tutti i dataset, tipo di fonte (sintetico/anonimizzato/mascherato), classificazione e team responsabile | Responsabile dello sviluppo / QA | Mantenuto continuamente; revisionato trimestralmente | Vita del dataset + 1 anno |
| 2 | **Registri di richiesta e approvazione dei dati di test** (richieste, giustificazioni, approvazioni dei Proprietari dei dati, metodo di mascheratura utilizzato) | Proprietari dei dati / Responsabile sicurezza informazioni | Per richiesta | 3 anni |
| 3 | **Registri di validazione della mascheratura dei dati** (risultati dei test di validazione, approvazione del Responsabile della sicurezza delle informazioni, data) | Responsabile sicurezza informazioni / Team di sicurezza | Per operazione di mascheratura | 3 anni |
| 4 | **Registri di generazione dei dati sintetici** (parametri del generatore, risultati di validazione, versione) | Responsabile dello sviluppo | Per generazione | 2 anni |
| 5 | **Registri di conservazione e smaltimento dei dati di test** (revisioni trimestrali, conferme di eliminazione, metodo di smaltimento) | Responsabile dello sviluppo / QA | Revisione trimestrale; per evento di smaltimento | 3 anni |
| 6 | **Accordi pre-audit e di penetration testing** (ambito, metodologia, tempistiche, regole di ingaggio, firme) | RSSI / Audit interno | Per incarico | 3 anni |
| 7 | **Registri degli accessi degli auditor e dei tester** (provisioning degli accessi, ambito, durata, conferma del deprovisioning) | Operazioni IT / Responsabile sicurezza informazioni | Per incarico | 3 anni |
| 8 | **Registri di verifica della conformità dei dispositivi degli auditor** (risultati del controllo di sicurezza, approvazione) | Operazioni IT | Per incarico | 1 anno |
| 9 | **Rapporti di penetration testing e risultati** (rapporti completi, monitoraggio della remediation, evidenza di chiusura) | RSSI / Team di sicurezza | Per incarico | 3 anni |
| 10 | **Registri di approvazione degli strumenti di audit** (nome dello strumento, versione, scopo, approvazione del Responsabile sicurezza informazioni) | Responsabile sicurezza informazioni | Per incarico | 2 anni |
| 11 | **Log delle attività di audit e testing** (log di accesso degli auditor, registri delle attività di testing, alert di monitoraggio) | Operazioni IT / Team di sicurezza | Continuamente | Per politica di conservazione dei log (1-3 anni) |
| 12 | **Rapporti sugli incidenti dalle attività di testing** (impatti non intenzionali, causa principale, remediation, lezioni apprese) | Operazioni IT / RSSI | Per incidente | 3 anni |
| 13 | **Registro delle eccezioni** (richieste di utilizzo diretto dei dati di produzione, approvazioni, controlli compensativi, scadenza) | Responsabile sicurezza informazioni | Mantenuto continuamente; revisionato trimestralmente | Durata eccezione + 3 anni |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui inventari dei dati di test, registri di validazione della mascheratura, documentazione degli incarichi di audit, log degli accessi, rapporti di penetration testing, audit interni ed esterni, e feedback al proprietario della politica.

**Metriche di conformità**:

| Metrica | Obiettivo | Frequenza di misurazione |
|--------|--------|-----------------------|
| Ambienti di test che utilizzano dati sintetici o anonimizzati (nessun dato di produzione non mascherato) | >= 95% | Trimestrale |
| Validazione della mascheratura completata e approvata prima del rilascio dei dati di test | 100% | Per operazione di mascheratura |
| Accordi pre-audit firmati prima dell'inizio del testing | 100% | Per incarico |
| Accesso degli auditor deprovisioning entro 24 ore dal completamento dell'audit | 100% | Per incarico |
| Risultati del penetration testing remediated entro SLA | >= 90% | Per incarico |
| Dati di test eliminati entro 30 giorni dal completamento del progetto | >= 90% | Trimestrale |

**Punteggio di conformità**:

| Componente | Peso | Calcolo |
|-----------|--------|-------------|
| Conformità della protezione dei dati di test | 40% | (Ambienti di test con fonti di dati approvate + validazioni di mascheratura completate) / Totale ambienti di test x 100 |
| Conformità della governance dell'audit | 30% | (Incarichi con accordi pre-audit firmati + accesso correttamente provisioned e deprovisioned) / Totale incarichi x 100 |
| Conformità della gestione dei risultati | 20% | (Risultati di penetration testing e audit remediated entro SLA) / Totale risultati x 100 |
| Conformità del ciclo di vita dei dati | 10% | (Dataset eliminati entro i tempi della politica) / Totale dataset che richiedono smaltimento x 100 |

**Gestione della non conformità**: Al di sotto del 70% è richiesta un'escalation immediata al RSSI e un piano di remediation. Tra il 70-89% è richiesta la supervisione del Responsabile della sicurezza delle informazioni con revisioni mensili. Al 90% e oltre si segue il monitoraggio trimestrale standard.

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata dal RSSI preventivamente, con accettazione del rischio documentata, controlli compensativi (registrazione avanzata, riduzione della conservazione, ulteriori restrizioni di accesso) e una data di revisione definita (massimo 12 mesi). Le eccezioni per l'utilizzo diretto dei dati di produzione negli ambienti di test richiedono inoltre l'approvazione del DPD. Le eccezioni devono essere segnalate al Team di revisione della direzione.

## Non conformità

Un dipendente che viola questa politica può essere soggetto a provvedimenti disciplinari, fino alla risoluzione del rapporto di lavoro. L'utilizzo di dati di produzione non mascherati negli ambienti di test senza approvazione deve essere trattato come un incidente sulla gestione dei dati e investigato di conseguenza. Le violazioni della politica devono essere documentate, investigate dal Responsabile della sicurezza delle informazioni e segnalate al RSSI.

## Miglioramento continuo

Questa politica viene revisionata e aggiornata come parte del processo di miglioramento continuo. Le revisioni devono considerare i progressi nelle tecniche di anonimizzazione e generazione di dati sintetici, i rischi emergenti di re-identificazione (inclusa la de-anonimizzazione assistita dall'IA), i cambiamenti nelle metodologie di penetration testing e nel panorama delle minacce, le modifiche normative (in particolare le linee guida della nLPD e i precedenti dell'applicazione del GDPR), i risultati degli audit e le lezioni apprese dagli incidenti di testing, e il feedback dei team di sviluppo, QA e audit.

---

# Aree della norma ISO 27001 affrontate

Politica sulle informazioni di test e la protezione dell'audit — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 7.3 Consapevolezza | 6.3 Consapevolezza, istruzione e formazione sulla sicurezza delle informazioni |
| Clausola 9.2 Audit interno | 8.11 Mascheratura dei dati |
| | **8.33 Informazioni di test** |
| | **8.34 Protezione dei sistemi informativi durante l'audit** |
| | 8.31 Separazione degli ambienti di sviluppo, test e produzione |

**Quadro normativo e legale**:

| Quadro | Pertinenza |
|-----------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative per la protezione dei dati; anonimizzazione e pseudonimizzazione come misure di protezione dei dati; i dati di test contenenti dati personali sono soggetti ai requisiti della nLPD |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1-3 — Requisiti minimi per la sicurezza dei dati, inclusi i controlli sull'ambiente di test |
| GDPR UE (ove applicabile) | Art. 5(1)(c) — Minimizzazione dei dati (nessun dato di produzione non necessario negli ambienti di test); Art. 25 — Protezione dei dati fin dalla progettazione e per impostazione predefinita; Art. 32 — Sicurezza del trattamento (la pseudonimizzazione come misura di sicurezza) |
| ISO/IEC 27001:2022 | Controlli Annex A 8.33 e 8.34 |
| ISO/IEC 27002:2022 | Sezioni 8.33 e 8.34 — Linee guida di implementazione |
| NIST SP 800-53 Rev 5 | SA-11 (Test e valutazione da parte degli sviluppatori), CA-8 (Penetration testing), AU-11 (Conservazione dei record di audit), SI-12 (Gestione e conservazione delle informazioni) |
| CIS Controls v8 | 3.1-3.14 (Protezione dei dati), 18.1-18.5 (Penetration testing) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
