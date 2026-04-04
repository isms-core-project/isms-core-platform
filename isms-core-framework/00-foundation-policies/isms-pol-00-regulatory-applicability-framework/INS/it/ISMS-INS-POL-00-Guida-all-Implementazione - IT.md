# ISMS-INS-POL-00 — Guida all'implementazione
## POL-00: Quadro di applicabilità normativa

**Data:** 2026-02-17
**Scopo:** Guida pratica all'implementazione per le organizzazioni che adottano POL-00
**Destinatari:** RSSI, Responsabile legale/conformità, RPD, Responsabile dell'implementazione

---

## 1. Cosa fa davvero POL-00 (in parole semplici)

POL-00 risponde a una sola domanda: **quali normative si applicano a questa organizzazione, e con quale forza vincolante?**

Senza questa politica, ogni autore di politiche del SGSI decide autonomamente se fare riferimento al RGPD, DORA, FINMA o NIST. Il risultato è incoerenza: alcune politiche citano normative non applicabili, altre omettono normative rilevanti, e i revisori spendono tempo nella Fase 1 a dipanare la matassa.

POL-00 risolve questo problema stabilendo tre livelli una volta sola, centralmente:

- **Livello 1 (Obbligatorio)** — si applica indipendentemente dall'attività aziendale. Non negoziabile.
- **Livello 2 (Condizionale)** — si applica solo se si verificano specifici trigger aziendali. Richiede una determinazione deliberata.
- **Livello 3 (Informativo)** — solo riferimento alle buone pratiche. Nessun obbligo di conformità.

Tutte le 53 politiche di controllo dell'Allegato A ereditano poi questa categorizzazione tramite riferimento a POL-00. La determinazione del Livello viene effettuata una sola volta, dall'ufficio legale/conformità, e tutte le politiche utilizzano tale determinazione in modo coerente.

**Il valore operativo**: quando emerge una nuova normativa, si aggiorna POL-00 (un solo documento), e la modifica si propaga logicamente a tutte le politiche di controllo. Non è necessario toccare 53 politiche singolarmente.

---

## 2. La parte difficile: le determinazioni del Livello 2

Il Livello 1 è semplice per un'organizzazione svizzera: la LPD (nLPD) e ISO 27001 sono di fatto obbligatorie se si persegue la certificazione e si opera in Svizzera. Il RGPD è obbligatorio se si trattano dati personali di residenti UE (per la maggior parte delle organizzazioni svizzere, la risposta è sì).

**Il Livello 2 è dove si svolge il vero lavoro.** Queste determinazioni richiedono giudizio, conoscenza giuridica e un'onesta valutazione del modello di business dell'organizzazione. Sbagliare ha conseguenze in entrambe le direzioni:

- **Over-applicazione** (applicare il Livello 2 quando il trigger non è soddisfatto): oneri di conformità non necessari, gold-plating, costi senza benefici
- **Sotto-applicazione** (mancanza di un trigger soddisfatto): esposizione normativa, potenziale azione di enforcement, non conformità nell'audit

### Lista di verifica per le decisioni di Livello 2

Analizzare ciascuna normativa in ordine. Per ognuna, rispondere onestamente alla domanda sul trigger. In caso di incertezza, è il Responsabile legale/conformità a prendere la determinazione e documentarne le motivazioni.

---

#### FINMA (Autorità federale di vigilanza sui mercati finanziari)

**Domanda trigger:** L'organizzazione è un'entità vigilata dalla FINMA?

Le entità vigilate dalla FINMA includono: banche, compagnie di assicurazione, società di titoli, borse valori, società di gestione fondi, organismi di investimento collettivo, infrastrutture dei mercati finanziari, fornitori di servizi di pagamento regolamentati ai sensi di FinSA/FinIA.

| Risposta | Livello | Azione |
|----------|---------|--------|
| Sì — direttamente vigilata dalla FINMA | Livello 2 Attivo | Applicare i requisiti della Circolare FINMA 2023/1; documentare nella DdA |
| Sì — fornitore ICT per un'entità FINMA | Livello 2 Attivo | Si applicano le regole FINMA sull'esternalizzazione; valutare i requisiti di sub-esternalizzazione |
| No | Livello 2 Non Attivo | Documentare «non è un'entità vigilata dalla FINMA» nella Matrice di applicabilità normativa |

**Errore comune:** Le PMI che forniscono servizi IT alle banche presumono che la FINMA non si applichi. Se la banca classifica il servizio come esternalizzazione materiale ai sensi della Circolare FINMA 2023/1, i requisiti FINMA si ripercuotono contrattualmente. Verificare il contratto quadro di servizi.

---

#### DORA (Digital Operational Resilience Act)

**Domanda trigger:** L'organizzazione è un'entità finanziaria o un fornitore terzo di servizi ICT (ITSP) per entità finanziarie UE?

Le entità finanziarie UE ai sensi di DORA includono: banche, compagnie di assicurazione, imprese di investimento, istituti di pagamento, istituti di moneta elettronica, fornitori di servizi su cripto-attività e altri. Le disposizioni DORA sugli ITSP si applicano ai fornitori di servizi ICT critici o importanti per queste entità.

| Risposta | Livello | Azione |
|----------|---------|--------|
| Entità finanziaria UE | Livello 2 Attivo | Piena applicabilità DORA inclusi i test TLPT |
| Fornitore ICT designato come critico/importante dall'entità finanziaria | Livello 2 Attivo | Si applica il Capitolo V DORA (quadro di supervisione) |
| Fornitore ICT — non ancora designato | Livello 2 Watch | Monitorare; verificare se i requisiti DORA si ripercuotono contrattualmente tramite gli accordi con i clienti |
| Nessuna connessione con entità finanziarie UE | Livello 2 Non Attivo | Documentare la determinazione; rivedere annualmente |

**Data di applicazione DORA:** 17 gennaio 2025. Se Livello 2 Attivo, i requisiti dovrebbero essere già in vigore o in fase di implementazione.

**Errore comune:** I fornitori ICT svizzeri per banche UE presumono che DORA non si applichi perché non hanno sede nell'UE. La portata extraterritoriale di DORA copre i fornitori ICT non UE che servono entità finanziarie UE. Verificare l'elenco dei clienti.

---

#### NIS2 (Direttiva sulla sicurezza delle reti e dei sistemi informativi 2)

**Domanda trigger:** L'organizzazione opera in un settore elencato nell'Allegato I o II di NIS2 e soddisfa la soglia dimensionale?

NIS2 si applica alle **Entità essenziali** (Allegato I: energia, trasporti, settore bancario, sanità, acqua, infrastrutture digitali, pubblica amministrazione, spazio) e alle **Entità importanti** (Allegato II: servizi postali, gestione dei rifiuti, produzione alimentare, produzione manifatturiera, fornitori digitali, ricerca).

Soglia dimensionale: medie imprese (50+ dipendenti O fatturato annuo ≥ 10 milioni EUR) nei settori coperti. Le entità più piccole solo se specificamente designate dallo Stato membro.

| Risposta | Livello | Azione |
|----------|---------|--------|
| Settore nell'ambito + soddisfa la soglia dimensionale | Livello 2 Attivo | Si applicano le misure di gestione dei rischi di cybersicurezza (Art. 21) e la notifica degli incidenti (Art. 23) |
| Settore nell'ambito + al di sotto della soglia | Livello 2 Watch | Monitorare; gli Stati membri possono estendere l'ambito |
| Settore fuori ambito | Livello 2 Non Attivo | Documentare la determinazione |

**Per le organizzazioni svizzere:** NIS2 è una legge UE. Si applica direttamente solo se l'organizzazione ha operazioni UE o fornisce servizi a entità UE nell'ambito. La Svizzera ha la propria revisione dell'ISG (Informationssicherheitsgesetz) — valutare entrambe.

---

#### PCI DSS v4.0.1

**Domanda trigger:** L'organizzazione archivia, elabora o trasmette dati dei titolari di carta (numeri di carte di pagamento, CVV, PIN)?

La risposta è binaria. Non esistono soglie — qualsiasi organizzazione che gestisce dati di carta rientra nell'ambito.

| Risposta | Livello | Azione |
|----------|---------|--------|
| Sì — qualsiasi dato di carta gestito | Livello 2 Attivo | Determinare il livello SAQ; applicare i requisiti pertinenti all'ambiente dei dati dei titolari di carta (CDE) |
| No — completamente esternalizzato a PSP (es. Stripe, PayPal), nessun dato di carta tocca i sistemi propri | Livello 2 Ridotto | Solo ambito SAQ-A; verificare l'approccio di tokenizzazione/reindirizzamento |
| Nessuna elaborazione di carte | Livello 2 Non Attivo | Documentare la determinazione |

**Errore comune:** Presumere che l'utilizzo di un elaboratore di pagamenti rimuova tutti gli obblighi PCI DSS. Se i propri sistemi reindirizzano a una pagina di pagamento ospitata e non vedono mai i dati della carta, si applica SAQ-A (semplificato). Se i propri sistemi vedono dati di carta in transito, si applica l'ambito completo.

---

#### AI Act UE

**Domanda trigger:** L'organizzazione sviluppa, distribuisce o utilizza sistemi AI nell'UE?

| Risposta | Livello | Azione |
|----------|---------|--------|
| Sviluppa o distribuisce sistemi AI vietati | Non consentito | Stop immediato |
| Sviluppa o distribuisce AI ad alto rischio (Allegato III) | Livello 2 Attivo | Valutazione di conformità, registrazione, documentazione tecnica obbligatorie |
| Distribuisce AI di uso generale in contesto ad alto rischio | Livello 2 Attivo | Obblighi ai sensi dell'Art. 50 (trasparenza) e valutazione del caso d'uso |
| Utilizza strumenti AI (es. Microsoft Copilot, ChatGPT) come deployer | Livello 2 Watch | Monitorare; si applicano obblighi di trasparenza e supervisione umana |
| Nessuno sviluppo o distribuzione di AI | Livello 2 Non Attivo | Documentare; rivedere annualmente — l'adozione dell'AI cambia rapidamente |

**Nota sulle scadenze:** Gli obblighi per l'AI ad alto rischio sono in fase di introduzione progressiva a partire da agosto 2025. Le disposizioni sui sistemi AI vietati sono attive da febbraio 2025. Le date di conformità sono in evoluzione — verificare il calendario di pubblicazione degli atti delegati.

---

#### HIPAA / FISMA / CCPA (USA federale/statale)

Queste si applicano solo se l'organizzazione:
- Tratta informazioni sanitarie protette di persone statunitensi (HIPAA)
- È un'agenzia federale statunitense o un appaltatore federale (FISMA)
- Raccoglie dati personali di residenti in California e soddisfa le soglie di fatturato/volume di dati (CCPA)

Per la maggior parte delle organizzazioni con sede in Svizzera senza operazioni negli USA, queste sono **Livello 3 (Informativo)**. Documentare la determinazione. Rivedere in caso di pianificata espansione nel mercato statunitense.

---

## 3. Prima configurazione — Completamento della Matrice di applicabilità normativa

La Matrice di applicabilità normativa (Sezione 8.2 di POL-00) è il registro formale delle determinazioni di Livello. Prima di completarla, rispondere a queste domande a livello organizzativo:

**Sull'organizzazione:**
1. Registrata in Svizzera? (LPD svizzera = Livello 1)
2. Tratta dati personali di residenti UE? (RGPD = Livello 1 o Livello 2 a seconda del volume/natura)
3. Entità vigilata dalla FINMA o fornitore IT materiale per una di esse? (FINMA Livello 2)
4. Fornisce servizi ICT a entità finanziarie UE? (DORA Livello 2)
5. Opera in un settore dell'Allegato I/II di NIS2 con 50+ dipendenti o ≥ 10 milioni EUR di fatturato? (NIS2 Livello 2)
6. Archivia, elabora o trasmette dati di carte di pagamento? (PCI DSS Livello 2)
7. Sviluppa, distribuisce o utilizza sistemi AI nell'UE? (AI Act UE Livello 2 Watch/Attivo)
8. Dati sanitari USA, contratti federali o clienti in California? (HIPAA/FISMA/CCPA Livello 2 o 3)

**Sequenza:**
1. Il RSSI e il Responsabile legale/conformità lavorano insieme sulla lista di verifica sopra
2. Il Responsabile legale/conformità prende le determinazioni di Livello 2 e documenta le motivazioni
3. Il RPD convalida le determinazioni relative alla privacy (RGPD, LPD svizzera, AI Act UE)
4. La Matrice viene completata con Livello + motivazione della determinazione per ogni normativa
5. La Direzione generale approva la Matrice completata
6. La Matrice viene datata e firmata — diventa la prova d'audit per la Fase 1

**La Matrice non deve essere perfetta.** Deve essere deliberata. Un revisore accetterà una determinazione motivata che DORA non si applica, supportata da una valutazione documentata della base clienti. Non accetterà «non ci abbiamo pensato».

---

## 4. Il Registro di monitoraggio trimestrale (in pratica)

La Sezione 4.3 di POL-00 richiede un monitoraggio trimestrale del panorama normativo. Questa è la prova che le determinazioni di Livello vengono mantenute aggiornate.

**Cosa significa in pratica il monitoraggio:**

Non significa assumere un team legale per condurre ricerche normative ogni trimestre. Significa:

1. Esaminare un insieme curato di fonti di monitoraggio normativo (Appendice POL-00 — Fonti di monitoraggio normativo)
2. Confermare se si sono verificati sviluppi normativi rilevanti nel trimestre
3. Valutare se tali sviluppi influenzano le attuali determinazioni di Livello
4. Documentare la revisione e firmare

**Modello per una tipica voce del registro trimestrale (nessuna modifica):**

```
REGISTRO DI MONITORAGGIO NORMATIVO — T[X] [ANNO]
Periodo: [GG.MM.AAAA] al [GG.MM.AAAA]

Fonti di monitoraggio esaminate:
☑ IFPDT (Incaricato federale della protezione dei dati e della trasparenza) — notizie e orientamenti
☑ FINMA — circolari e aggiornamenti degli orientamenti
☑ EUR-Lex / Gazzetta ufficiale UE — atti di implementazione DORA/NIS2/AI Act
☑ PCI Security Standards Council — aggiornamenti DSS
☑ ENISA — orientamenti di implementazione NIS2

Risultati:
Nel presente trimestre non sono stati identificati sviluppi normativi rilevanti
che influenzino le attuali determinazioni di Livello 1/2/3.

Valutazione richiesta: No

Esaminato da: [Nome Responsabile legale/conformità]          Data: [GG.MM.AAAA]
Confermato da: [Nome RSSI]                                   Data: [GG.MM.AAAA]
```

**Se qualcosa è cambiato:** Documentare il cambiamento, valutare quali determinazioni di Livello o politiche di controllo sono interessate, avviare il processo di modifica di POL-01 Sezione 5.2, e registrare il riferimento alla valutazione avviata.

**La cosa più importante del registro:** Farlo nella stessa data ogni trimestre. Impostare un appuntamento ricorrente nel calendario. Un registro con date coerenti (fine marzo, giugno, settembre, dicembre) sembra deliberato. Un registro con date irregolari sembra retroattivo.

---

## 5. Valutazioni avviate — Quando rivalutare a metà trimestre

I seguenti eventi aziendali dovrebbero avviare una rivalutazione immediata al di fuori del ciclo trimestrale (Sezione 5 di POL-00):

| Evento | Cosa valutare |
|--------|---------------|
| Ingresso in un nuovo mercato (UE, USA, ecc.) | Nuovi obblighi normativi in quella giurisdizione |
| Acquisizione o fusione con un'altra entità | Gli obblighi normativi dell'entità target si trasferiscono |
| Lancio di un nuovo prodotto che tratta dati personali | Ambito RGPD/LPD, AI Act se abilitato all'AI |
| Inizio elaborazione dati di carte di pagamento | Trigger PCI DSS |
| Aggiudicazione di un contratto con un'entità finanziaria UE | Disposizioni DORA sugli ITSP |
| Raggiungimento di 50 dipendenti o 10 milioni EUR di fatturato | Soglia dimensionale NIS2 superata |
| Aggiornamento normativo rilevante (azione di enforcement, nuovi orientamenti) | Determinazione di Livello interessata |

Le valutazioni avviate utilizzano la stessa metodologia di valutazione della revisione trimestrale, ma vengono documentate separatamente. Fare riferimento all'evento trigger, all'esito della valutazione e al fatto che sia stato avviato un processo di modifica POL-01.

---

## 6. Connessioni con altri documenti

**→ POL-01 (Quadro di governance e processo decisionale del SGSI)**
POL-00 genera il *cosa* (quali normative si applicano). POL-01 disciplina il *processo* per modificare quella determinazione. Quando un registro di monitoraggio trimestrale identifica una modifica normativa rilevante, viene avviato il processo in sei fasi della Sezione 5.2 di POL-01. Le due politiche funzionano in tandem.

**→ Dichiarazione di Applicabilità (DdA)**
Le determinazioni di Livello 1 e Livello 2 Attivo influenzano direttamente le selezioni dei controlli nella DdA. DORA attivo → i controlli di resilienza (A.5.29, A.5.30, A.8.13, A.8.14) sono probabilmente obbligatori. PCI DSS attivo → i controlli di cifratura e accesso (A.8.24, A.8.2, A.5.15) ricevono una giustificazione aggiuntiva. La DdA dovrebbe fare riferimento a POL-00 come fonte per la motivazione dell'inclusione dei controlli.

**→ Politiche di controllo dell'Allegato A**
Le politiche di controllo non devono enumerare singolarmente ogni normativa applicabile. Fanno riferimento a POL-00 per il quadro normativo e citano normative specifiche solo dove queste determinano un requisito di controllo specifico (es. Articolo 32 RGPD nella politica di cifratura A.8.24).

---

## 7. Prove per i revisori

### Fase 1 (Revisione documentale)

Il revisore vuole verificare che gli obblighi normativi siano identificati e categorizzati esplicitamente. Prove:

- [X] POL-00 v1.0 — approvata, firmata, datata
- [X] Matrice di applicabilità normativa (Sezione 8.2) — completata con determinazioni di Livello e motivazioni per ogni normativa
- [X] Documentazione delle determinazioni di Livello 2 — giustificazione scritta per le decisioni Attivo/Non Attivo per ogni normativa condizionale
- [X] Firme di approvazione — RSSI, Responsabile legale/conformità, RPD, Direzione generale

**Cosa rilevano i revisori in Fase 1:** Determinazioni di Livello 2 mancanti o vaghe («DORA — in revisione»), Matrici non firmate, incoerenza tra le determinazioni di Livello di POL-00 e le selezioni dei controlli nella DdA.

### Fase 2 (Efficacia operativa)

Il revisore vuole verificare che POL-00 sia effettivamente mantenuta. Prove:

- [X] Registri di monitoraggio trimestrale — minimo 4 trimestri (o dal momento dell'istituzione del SGSI se meno di un anno)
- [X] Ogni registro firmato da Responsabile legale/conformità + RSSI
- [X] Almeno un registro di valutazione avviata (se si è verificato un evento aziendale rilevante)
- [X] Prova che la DdA è stata aggiornata a seguito di qualsiasi modifica della determinazione di Livello

**Cosa rilevano i revisori in Fase 2:** Registri trimestrali che sembrano un modello ma non genuinamente esaminati (testo identico in tutti e 4 i trimestri senza variazioni), firme mancanti, assenza di risposta a sviluppi normativi noti (es. la data di applicazione di DORA passa ma nessuna voce del registro la riconosce).

---

## 8. Osservazioni sull'implementazione

### 8.1 Il trimestre «nessuna modifica» va bene — ma variare il linguaggio

Quattro voci di registro trimestrale identiche con testo copiato incollato sembrano un esercizio di spunta. I revisori lo notano. Anche quando nulla è cambiato in modo sostanziale, variare ciò che è stato esaminato, annotare i documenti di orientamento specifici verificati e menzionare eventuali sviluppi valutati e ritenuti irrilevanti.

### 8.2 La sovrapposizione RGPD e LPD svizzera — gestirla una sola volta, non due

Per le organizzazioni svizzere che trattano dati personali UE, si applicano sia il RGPD che la LPD svizzera. Hanno requisiti sovrapposti ma non identici. L'approccio più sicuro: implementare allo standard più rigoroso per ogni requisito specifico (di solito il RGPD). Documentarlo nella Matrice di applicabilità normativa. Non scrivere due programmi di conformità separati — questo crea incoerenza e confusione.

### 8.3 Il Livello 2 «Watch» è uno stato legittimo

Non ogni normativa di Livello 2 è binaria Attivo/Non Attivo. «Watch» (monitoraggio della situazione senza obblighi di conformità completi) è appropriato per:
- DORA quando si servono entità finanziarie tramite intermediari (esposizione non chiara)
- AI Act UE dove gli strumenti AI sono utilizzati ma la classificazione completa del rischio è in corso di valutazione
- NIS2 dove si è vicini ma non chiaramente oltre la soglia dimensionale

Documentare la motivazione del Watch. Impostare un trigger di revisione. Non lasciare le voci Watch indefinitamente — dovrebbero risolversi in Attivo o Non Attivo entro 12 mesi.

### 8.4 Il panorama normativo si muove rapidamente (2025-2026)

Tre importanti normative di Livello 2 sono in fase di implementazione attiva:
- **DORA** — in vigore dal 17 gennaio 2025, enforcement in corso
- **AI Act UE** — AI vietati da febbraio 2025, AI ad alto rischio da agosto 2025
- **NIS2** — scadenza di recepimento ottobre 2024, enforcement variabile per Stato membro

Il registro di monitoraggio trimestrale avrà probabilmente contenuti genuini per i prossimi 2-3 anni solo da queste tre normative. Non trattare il monitoraggio come una formalità in questo periodo.

### 8.5 La Matrice di applicabilità normativa è un'ancora d'audit

I revisori in Fase 1 passeranno molto tempo su POL-00 perché è alla base dei riferimenti normativi di tutte le altre politiche. Una Matrice ben completata — con determinazioni esplicite, motivazione firmata e chiare assegnazioni di Livello — crea una forte prima impressione e previene domande dettagliate sulle singole politiche di controllo.

Investire tempo per fare bene la Matrice. Paga dividendi su tutto l'audit.

---

## 9. Sequenza di implementazione minima indispensabile

1. **Rispondere alle 8 domande organizzative** (Sezione 3) — RSSI + Responsabile legale/conformità insieme
2. **Completare la Matrice di applicabilità normativa** — prima Livello 1, poi determinazioni di Livello 2 con motivazione scritta
3. **Il RPD convalida le determinazioni sulla privacy** — sezioni RGPD, LPD svizzera, AI Act UE
4. **La Direzione generale approva e firma la Matrice**
5. **Approvare e firmare POL-00** — catena di approvazione completa (RSSI → Legale/conformità → RPD → Direzione generale)
6. **Completare il primo registro di monitoraggio trimestrale** — anche solo un trimestre prima dell'audit Fase 1
7. **Verificare incrociando la DdA** — confermare che le selezioni dei controlli riflettano le determinazioni Livello 1/2 Attivo
8. **Aggiornare la Sezione 7 di POL-00** — aggiungere il testo sull'integrazione con la gestione dei cambiamenti di POL-01 (vedere la guida INS di POL-01)
9. **Pianificare il monitoraggio trimestrale** — appuntamento ricorrente nel calendario, stesse date ogni trimestre

I passi 1-6 sono il minimo per la prontezza all'audit Fase 1. I passi 7-9 completano l'integrazione.

---

## 10. Posizioni dei file

| Documento | Posizione |
|-----------|----------|
| Politica POL-00 | `POL/ISMS-POL-00 - Regulatory Applicability Framework.md` |
| Questa guida all'implementazione | `INS/ISMS-INS-POL-00-Guida-all-Implementazione - IT.md` |
| Guida all'implementazione POL-01 | `../isms-pol-01-.../INS/ISMS-INS-POL-01-Guida-all-Implementazione - IT.md` |
| Documenti di riferimento normativi | `isms-ref-dora/`, `isms-ref-eu-ai-act/`, ecc. |

---

<!-- QA_VERIFIED: 2026-04-03 -->
