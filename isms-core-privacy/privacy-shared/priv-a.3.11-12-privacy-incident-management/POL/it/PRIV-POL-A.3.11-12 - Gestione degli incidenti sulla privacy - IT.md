<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.11-12-IT:privacy:POL:a.3.11-12 -->
**PRIV-POL-A.3.11-12 — Gestione degli incidenti sulla privacy**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Gestione degli incidenti sulla privacy |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | PRIV-POL-A.3.11-12 |
| **Autore del documento** | Responsabile della Protezione dei Dati (RPD) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |
| **Versione del prodotto Privacy** | 1.0 |

**Cronologia delle versioni** :

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 1.0 | [Data da definire] | RPD | Politica iniziale per la prima certificazione ISO/IEC 27701:2025 |

**Ciclo di revisione** : Annuale | **Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** : Principale: RPD; Secondaria: RSSI; Legale: Responsabile Legale/Conformità; Autorità finale: Direzione generale.

**Documenti correlati** :
- PRIV-POL-00 / PRIV-POL-01; PRIV-IMP-A.3.11-12-UG / TG
- ISMS-POL-A.5.24-28 (Ciclo di vita della gestione degli incidenti — parallelo SGSI)
- ISMS-POL-A.6.8 (Segnalazione degli eventi di sicurezza)
- ISO/IEC 27701:2025 Controlli A.3.11, A.3.12
- RGPD Articolo 33 (Notifica all'autorità di controllo); Articolo 34 (Comunicazione agli interessati)
- LPD svizzera Articolo 24 (Notifica delle violazioni della sicurezza dei dati)

**Applicabilità del ruolo** : Questa politica si applica all'organizzazione che agisce sia come **Titolare del trattamento che come Responsabile del trattamento dei DCP**. I controlli A.3.11 e A.3.12 sono controlli condivisi (Tabella A.3). Gli obblighi di notifica differiscono materialmente tra i ruoli di titolare e responsabile del trattamento e vengono trattati separatamente in questa politica.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la pianificazione, la preparazione e la risposta agli incidenti di sicurezza delle informazioni relativi al trattamento dei DCP — conformemente ai controlli A.3.11 e A.3.12 di ISO/IEC 27701:2025.

**Perimetro** : Tutti gli incidenti di sicurezza delle informazioni che coinvolgono, incidono o potrebbero incidere sulla riservatezza, l'integrità o la disponibilità dei DCP trattati da [Organizzazione]; tutto il personale con ruoli nel rilevamento, l'escalation, la gestione o la notifica degli incidenti di privacy.

**Motivazione dei controlli combinati** : A.3.11 (pianificazione e preparazione) e A.3.12 (risposta) sono le due fasi della stessa capacità. Una risposta efficace è impossibile senza una pianificazione preventiva; la pianificazione senza procedure di risposta testate è teorica. Vengono implementati insieme come programma integrato di gestione degli incidenti di protezione dei dati.

---

# Perimetro e applicabilità

## Enunciati dei controlli ISO/IEC 27701:2025

**Controllo A.3.11 — Pianificazione e preparazione della gestione degli incidenti di sicurezza delle informazioni**
Il controllo A.3.11 richiede che [Organizzazione] pianifichi e si prepari agli incidenti di sicurezza delle informazioni relativi al trattamento dei DCP definendo, stabilendo e comunicando i processi, i ruoli e le responsabilità di gestione degli incidenti che disciplineranno la risposta specifica alla privacy.

**Controllo A.3.12 — Risposta agli incidenti di sicurezza delle informazioni**
Il controllo A.3.12 richiede che [Organizzazione] risponda agli incidenti di sicurezza delle informazioni relativi al trattamento dei DCP in conformità con le procedure documentate di risposta agli incidenti.

## Perimetro degli incidenti DCP

I seguenti incidenti costituiscono incidenti relativi ai DCP che richiedono gestione ai sensi di questa politica: accesso non autorizzato ai DCP (confermato o sospetto); divulgazione accidentale di DCP a un destinatario non autorizzato; perdita o furto di un dispositivo, supporto o documento contenente DCP; ransomware, malware o compromissione del sistema che incide sui sistemi di trattamento dei DCP; cancellazione o corruzione accidentale di DCP; trattamento illecito dei DCP; notifica da parte di un fornitore/responsabile del trattamento di un incidente che interessa i DCP di [Organizzazione].

## Quadro normativo

**Obbligatorio (Livello 1)** (per PRIV-POL-00):
- **RGPD UE** : Articolo 33 (notifica all'autorità di controllo entro 72 ore); Articolo 34 (comunicazione agli interessati in caso di rischio elevato); Articolo 5(1)(f) (principio di integrità e riservatezza)
- **LPD svizzera** : Articolo 24 (notifica all'IFPDT delle violazioni suscettibili di comportare un rischio elevato per gli interessati, senza indebito ritardo)
- **ISO/IEC 27701:2025** : Controlli A.3.11, A.3.12 (normativi)

---

# Pianificazione e preparazione della gestione degli incidenti di privacy (A.3.11)

## Programma di gestione degli incidenti di protezione dei dati

[Organizzazione] DEVE pianificare e prepararsi a gestire gli incidenti di sicurezza delle informazioni relativi al trattamento dei DCP come programma definito, stabilito e comunicato. Questo programma estende il quadro SGSI di gestione degli incidenti (ISMS-POL-A.5.24-28) con processi, ruoli e obblighi specifici ai DCP.

### Piano di Risposta agli Incidenti di Privacy (PRIP)

[Organizzazione] DEVE mantenere un Piano di Risposta agli Incidenti di Privacy (PRIP) che definisce: criteri di classificazione degli incidenti DCP e livelli di gravità; ruoli e responsabilità per la gestione degli incidenti di protezione dei dati; catene di escalation e comunicazione per ogni livello di gravità; logica decisionale per le notifiche normative; criteri e processo di notifica agli interessati; obblighi di notifica ai responsabili del trattamento (quando [Organizzazione] agisce come responsabile del trattamento); requisiti di conservazione delle prove per gli incidenti DCP; processo di revisione post-incidente e lezioni apprese.

Il PRIP è un documento controllato mantenuto dal RPD. La struttura e i requisiti di contenuto sono definiti in PRIV-IMP-A.3.11-12-UG.

### Classificazione della gravità degli incidenti DCP

Gli incidenti DCP DEVONO essere classificati per gravità per determinare l'escalation e l'urgenza della risposta:

| Gravità | Criteri | Urgenza di risposta |
|---------|---------|-------------------|
| **Critica** | Violazione su larga scala; DCP di categoria speciale interessati; alta probabilità di danno significativo agli interessati; compromissione sistemica dei sistemi di trattamento dei DCP | Immediata — team di risposta agli incidenti attivato entro 2 ore |
| **Alta** | Violazione dei dati personali confermata; notifica normativa probabile; rischio di danno significativo agli interessati; volume significativo di DCP interessati | Stesso giorno — RPD coinvolto entro 4 ore |
| **Media** | Violazione sospetta in corso di indagine; DCP limitati interessati; rischio di danno basso ma non trascurabile; contenimento raggiunto | 24 ore — RPD coinvolto entro 24 ore |
| **Bassa** | Quasi-incidente o evento potenziale; nessun accesso DCP confermato; violazione procedurale senza violazione effettiva | Standard — valutato entro 5 giorni lavorativi |

### Requisiti di preparazione

[Organizzazione] DEVE mantenere la prontezza agli incidenti di protezione dei dati attraverso: **Ruoli assegnati e comunicati** : tutti i ruoli di gestione degli incidenti di protezione dei dati definiti, documentati e comunicati; **Formazione** : il personale con ruoli negli incidenti di protezione dei dati riceve formazione specifica al ruolo; **Test** : il PRIP DEVE essere testato al minimo annualmente attraverso esercitazioni tabletop; **Manutenzione dei contatti** : le informazioni di contatto delle autorità di controllo (per RGPD; IFPDT per LPD svizzera) e l'accesso ai portali di notifica DEVONO essere mantenuti aggiornati; **Modelli di notifica** : bozze di modelli di notifica per le autorità di controllo e gli interessati DEVONO essere preparate, esaminate da Legale/RPD, e mantenute pronte per un rapido dispiegamento.

---

# Risposta agli incidenti di protezione dei dati (A.3.12)

## Requisiti di risposta

Le risposte agli incidenti di sicurezza delle informazioni relativi al trattamento dei DCP DEVONO essere condotte secondo le procedure documentate nel PRIP e PRIV-IMP-A.3.11-12-UG.

### Valutazione della violazione dei dati personali

Quando viene rilevato un incidente relativo ai DCP, [Organizzazione] DEVE valutare prontamente se l'incidente costituisce una **violazione dei dati personali** — definita come una violazione della sicurezza che comporta la distruzione, la perdita, la modifica, la divulgazione non autorizzata o l'accesso non autorizzato a dati a carattere personale.

La valutazione DEVE considerare: se i DCP sono stati o potrebbero essere stati accessibili, divulgati, persi o distrutti senza autorizzazione; le categorie e il volume approssimativo di DCP coinvolti; le probabili conseguenze per gli interessati; se la violazione è suscettibile di comportare un rischio (o un rischio elevato) per i diritti e le libertà delle persone fisiche.

La valutazione e il suo esito DEVONO essere documentati indipendentemente dalla conclusione.

### Notifica normativa: in qualità di Titolare del trattamento dei DCP

Quando [Organizzazione] agisce come Titolare del trattamento dei DCP e una violazione dei dati personali è confermata o ragionevolmente sospettata:

**RGPD — Notifica all'autorità di controllo (Articolo 33)** :

Il termine di 72 ore inizia quando [Organizzazione] ha ragionevole certezza che si sia verificata una violazione dei dati personali — non al momento del primo sospetto. Laddove l'indagine iniziale sia non conclusiva, il termine inizia quando vengono stabiliti fatti sufficienti per confermare che si è verificata una violazione. Un'indagine prolungata senza una determinazione preliminare non è accettabile; laddove una violazione non possa essere esclusa entro 24 ore, il RPD DEVE effettuare una notifica provvisoria all'autorità di controllo e integrarla man mano che emergono ulteriori informazioni.

- LADDOVE la violazione sia suscettibile di comportare un rischio per i diritti e le libertà delle persone fisiche: notificare l'autorità di controllo competente **senza indebito ritardo e, ove possibile, entro 72 ore** dall'esserne venuta a conoscenza
- LADDOVE la notifica venga effettuata dopo le 72 ore: includere una giustificazione motivata del ritardo
- LADDOVE la violazione non sia suscettibile di comportare un rischio: notifica non richiesta, ma la violazione DEVE essere documentata internamente (registro delle violazioni)
- Contenuto della notifica: natura della violazione; categorie e numero approssimativo di interessati; categorie e numero approssimativo di registrazioni; nome/contatto del RPD; probabili conseguenze; misure adottate o proposte

**LPD svizzera — Notifica all'IFPDT (Articolo 24)** : LADDOVE la violazione sia suscettibile di comportare un rischio elevato per la personalità o i diritti fondamentali degli interessati: notificare l'IFPDT **il prima possibile** secondo il formato specificato dall'IFPDT.

**RGPD — Comunicazione agli interessati (Articolo 34)** : LADDOVE la violazione sia suscettibile di comportare un **rischio elevato** per i diritti e le libertà degli interessati: comunicare agli interessati **senza indebito ritardo**; la comunicazione può essere ritardata per considerazioni di polizia giudiziaria (coordinamento con il Legale richiesto).

### Notifica normativa: in qualità di Responsabile del trattamento dei DCP

Quando [Organizzazione] agisce come Responsabile del trattamento dei DCP e viene rilevata una violazione (o potenziale violazione) che incide sui DCP di un cliente: notificare il Titolare del trattamento (cliente) **senza indebito ritardo** non appena viene confermata o ragionevolmente sospettata una violazione — la notifica non è condizionata al completamento dell'indagine interna. La notifica del responsabile del trattamento consente al Titolare del trattamento di avviare il proprio termine di 72 ore; [Organizzazione] NON DEVE ritardare la notifica al responsabile del trattamento in attesa di conferma completa. Termine massimo di notifica: 24 ore dal momento in cui [Organizzazione] viene a conoscenza che si è verificata o è ragionevolmente sospettata una violazione. La notifica DEVE essere effettuata al contatto di sicurezza o protezione dei dati designato dal cliente specificato nel contratto di trattamento. [Organizzazione] NON DEVE notificare direttamente l'autorità di controllo o gli interessati senza autorizzazione esplicita del Titolare del trattamento o obbligo legale indipendente.

### Azioni di risposta agli incidenti

La risposta agli incidenti di protezione dei dati DEVE includere, in ordine di priorità:

1. **Contenere** : Fermare la violazione in corso o prevenire ulteriore esposizione dei DCP
2. **Valutare** : Determinare il perimetro, le categorie di DCP interessate, il volume e gli interessati
3. **Preservare** : Mettere in sicurezza le prove (log, registrazioni, sistemi interessati) — coordinare con il RSSI per ISMS-POL-A.5.24-28
4. **Notificare** : Eseguire le notifiche normative e agli interessati secondo le soglie applicabili
5. **Recuperare** : Ripristinare il trattamento dei DCP al normale funzionamento con appropriate garanzie
6. **Esaminare** : Condurre la revisione post-incidente; aggiornare PRIP e controlli secondo necessità

### Registro delle violazioni della protezione dei dati

[Organizzazione] DEVE mantenere un Registro delle violazioni della protezione dei dati che registra tutte le violazioni dei dati personali, indipendentemente dal fatto che fosse richiesta una notifica normativa. Il registro DEVE includere: riferimento dell'incidente e data di scoperta; natura della violazione e categorie di DCP interessati; numero approssimativo di interessati e registrazioni; esito della valutazione dei rischi; decisioni di notifica e date; azioni di remediation adottate; riferimento alla revisione post-incidente.

Il RPD mantiene il Registro delle violazioni. Conservazione: minimo 5 anni.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RPD** | Responsabile degli incidenti di protezione dei dati — attiva il PRIP; prende le decisioni di notifica normativa; comunica con le autorità di controllo; approva le comunicazioni agli interessati; mantiene il Registro delle violazioni; guida la revisione post-incidente |
| **RSSI** | Responsabile tecnico degli incidenti — coordina il contenimento e il recupero; conserva le prove forensi; gestisce l'indagine tecnica |
| **Legale/Conformità** | Consulenza legale sugli obblighi di notifica; esamina le notifiche all'autorità di controllo; consulenza sugli obblighi del responsabile del trattamento |
| **Referenti per la privacy** | Primo punto di escalation per il personale che segnala incidenti DCP nella propria unità; triage iniziale ed escalation al RPD |
| **Team Sicurezza IT** | Indagine e contenimento tecnico; isolamento e recupero del sistema; conservazione delle prove per ISMS-POL-A.5.24-28 |
| **Direzione generale** | Informata di tutti gli incidenti Alti e Critici; approva le comunicazioni di crisi; supporta il coinvolgimento normativo a livello senior |
| **Comunicazione** | Redazione delle notifiche agli interessati (con approvazione RPD); gestione delle relazioni pubbliche |
| **Tutto il personale** | Segnala immediatamente gli incidenti DCP sospetti al proprio Referente per la privacy o direttamente al RPD; conserva le prove; coopera all'indagine |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Piano di Risposta agli Incidenti di Privacy (PRIP) | Versione approvata corrente con ruoli, processi, logica decisionale di notifica | In corso + 3 anni |
| Registro delle violazioni della protezione dei dati | Registro di tutte le violazioni dei dati personali con valutazione dei rischi e decisioni di notifica | 5 anni |
| Notifiche alle autorità di controllo | Copie di tutte le notifiche Articolo 33 / LPD Articolo 24 inviate | 5 anni |
| Comunicazioni agli interessati | Copie delle comunicazioni Articolo 34 agli interessati | 5 anni |
| Registrazioni di test del PRIP | Prove delle esercitazioni tabletop annuali con risultati e miglioramenti | 3 anni |
| Registrazioni della cronologia di risposta agli incidenti | Prove della conformità alla finestra di notifica di 72 ore (o giustificazione documentata del ritardo) | 5 anni |
| Rapporti di revisione post-incidente | Lezioni apprese e azioni di miglioramento del PRIP/controlli | 3 anni |

---

# Considerazioni di audit

**Per A.3.11 (Pianificazione e preparazione)** : PRIP documentato con processi e ruoli specifici ai DCP; prove che i ruoli siano assegnati e il personale sia consapevole delle proprie responsabilità; registrazioni di test annuale del PRIP; informazioni di contatto delle autorità di controllo mantenute aggiornate; modelli di notifica preparati ed esaminati.

**Per A.3.12 (Risposta)** : Registro delle violazioni con tutti gli incidenti registrati, incluse le determinazioni di non notifica; per le violazioni notificate: notifiche entro la finestra di 72 ore (o giustificazione documentata del ritardo); documentazione di valutazione delle violazioni per gli incidenti Alti/Critici; rapporti di revisione post-incidente con azioni seguite fino al completamento; prove che gli obblighi di notifica del responsabile del trattamento siano stati adempiuti (notifica tempestiva al cliente quando si agisce come responsabile del trattamento).

---

<!-- QA_VERIFIED: 2026-04-03 -->
