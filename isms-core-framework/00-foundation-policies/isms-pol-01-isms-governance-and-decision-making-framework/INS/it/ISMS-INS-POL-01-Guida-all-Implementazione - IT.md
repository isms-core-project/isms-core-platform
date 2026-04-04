# ISMS-INS-POL-01 — Guida all'implementazione
## POL-01: Quadro di governance e processo decisionale del SGSI

**Data:** 2026-02-17
**Scopo:** Guida pratica all'implementazione per le organizzazioni che adottano POL-01
**Destinatari:** RSSI, Responsabile dell'implementazione, Consulente

---

## 1. Cosa fa concretamente POL-01 (in parole semplici)

POL-01 esiste per un motivo: **bloccare l'espansione arbitraria del perimetro da parte dell'auditor.**

La certificazione ISO 27001 implica due livelli di valutazione professionale:
1. **La vostra valutazione** — interpretare la norma ISO 27001 nel vostro contesto, selezionare i controlli, definire le prove
2. **La valutazione dell'auditor** — verificare che la vostra interpretazione sia ragionevole e attuata

Senza POL-01, il confine tra il livello 1 e il livello 2 è sfumato. Un auditor eccessivamente scrupoloso può mettere in discussione le vostre decisioni di progettazione dei controlli durante l'audit, trasformando un esercizio di verifica in una rinegoziazione. POL-01 trasferisce tutte le vostre decisioni di valutazione professionale in artefatti documentati, firmati e prodotti prima dell'audit. Al momento dell'arrivo dell'auditor, ogni decisione ha un'autorità nominata, un documento di competenza e una firma di approvazione. Il loro lavoro si riduce a una risposta binaria: avete seguito il vostro processo documentato? Sì o no.

**La complessità di POL-01 è il prodotto. Una politica di governance più semplice lascia più spazio di manovra agli auditor.**

---

## 2. Cosa deve cambiare nelle altre politiche

### 2.1 Modifiche richieste (da eseguire)

Solo 4 politiche necessitano aggiornamenti sostanziali. Vale la pena farli perché stabiliscono rimandi incrociati che gli auditor si aspetteranno di trovare quando esamineranno il quadro di governance.

#### POL-00 — Quadro di applicabilità normativa
**Dove:** Sezione 7 (Manutenzione e aggiornamenti)
**Cosa aggiungere:** Una sottosezione che spiega come i cambiamenti normativi rilevati tramite il monitoraggio di POL-00 attivino il processo di modifica di POL-01 (Sezione 5.2). Gli auditor cercheranno questo collegamento — senza di esso, il monitoraggio di POL-00 e il controllo delle modifiche di POL-01 appariranno scollegati.

```markdown
### Integrazione con la gestione dei cambiamenti

I cambiamenti normativi rilevati tramite il monitoraggio di POL-00 attivano il
processo di modifica dei criteri di conformità definito in ISMS-POL-01 (Sezione 5.2).
La valutazione dell'impatto delle modifiche, l'autorità di approvazione e il
monitoraggio delle rivalutazioni seguono il processo in 6 fasi definito in
POL-01 Sezione 5.2. I controlli interessati vengono rivalutati entro 90 giorni
come da POL-01 Sezione 5.4.
```

#### POL-A.5.1 — Politiche per la sicurezza delle informazioni
**Dove:** Sezione 1.3 o nuova Sezione 1.4
**Cosa aggiungere:** Un riferimento ai confini di governance. Questa è la politica quadro per tutti i controlli dell'Allegato A — indicare qui che l'autorità decisionale, le eccezioni e il controllo delle modifiche sono disciplinati da POL-01 significa che non occorre aggiungerlo in nessun altro luogo.

```markdown
### Quadro di governance

L'autorità decisionale per l'interpretazione della conformità al SGSI, la gestione
delle eccezioni ai controlli e il controllo delle modifiche ai criteri di conformità
è disciplinata da ISMS-POL-01 (Quadro di governance e processo decisionale del SGSI).
Tutte le politiche dei controlli dell'Allegato A operano entro i confini di autorità
e i processi definiti in POL-01.
```

#### POL-A.5.31 — Requisiti legali, normativi e contrattuali
**Dove:** Sezione di monitoraggio della conformità
**Cosa aggiungere:** Riferimento all'autorità di governance che collega il monitoraggio della conformità (POL-00) alla gestione delle eccezioni e al controllo delle modifiche (POL-01). Gli auditor che verificano la conformità ad A.5.31 vorranno vedere come i cambiamenti normativi confluiscono nel processo di governance.

#### POL-A.5.35-36 — Revisione della conformità / Revisione indipendente
**Dove:** Sezione sul processo di revisione
**Cosa aggiungere:** Riferimento a POL-01 Sezione 6.1 (revisione annuale della governance) come parte del perimetro della revisione indipendente. Questo garantisce che l'efficacia della governance rientri esplicitamente nel perimetro dell'audit.

---

### 2.2 Da omettere (non vale la pena farlo)

**Aggiungere POL-01 ai Documenti correlati di tutte le 53 politiche dell'Allegato A.**

L'ISMS Copilot ha suggerito questo come Fase 3. Non fatelo. Ecco perché:

- Il rapporto tra POL-01 e tutte le politiche dei controlli è stabilito dalla struttura del SGSI, dalla DdA e da POL-A.5.1 (la politica quadro)
- Gli auditor non verificano la governance controllando 53 elenchi di Documenti correlati
- 53 modifiche alle politiche × costi di manutenzione = debito perpetuo ogni volta che POL-01 cambia
- Aggiungere una riga a ogni politica crea l'illusione di integrazione senza la sostanza

**Se un auditor chiede perché POL-01 non è nei Documenti correlati di una specifica politica di controllo**, indicatelo a POL-A.5.1 Sezione 1.X (il riferimento alla governance che avete aggiunto sopra). È sufficiente.

---

## 3. Avvio operativo — Cosa deve esistere prima dell'audit di Fase 2

È qui che molte organizzazioni vengono colte in falta. POL-01 definisce i processi. I processi necessitano di prove. Ecco il set minimo di prove per un primo audit di Fase 2.

### 3.1 Da avere obbligatoriamente (l'auditor lo chiederà)

| Prova | Di cosa si tratta | Chi la gestisce | Cadenza |
|-------|-------------------|----------------|---------|
| **Registri di monitoraggio POL-00** | Registrazione firmata della revisione del panorama normativo | Legale/Conformità + RSSI | Trimestrale (4 all'anno) |
| **Registro delle eccezioni** | Registro dei controlli non implementabili come scritti, con processo in 5 fasi documentato | RSSI | Man mano che sorgono eccezioni |
| **Registro delle accettazioni del rischio** | Firme della Direzione generale sui rischi accettati | Direzione generale | Man mano che vengono prese le decisioni |
| **Registro delle modifiche al SGSI** | Registro delle modifiche ai criteri di conformità con processo in 6 fasi | RSSI | Man mano che avvengono le modifiche |
| **Documenti di competenza** | Certificazioni / dossier di esperienza per RSSI, Legale/Conformità, RPD, Direzione generale | HR / RSSI | All'assegnazione del ruolo |
| **Verbali della revisione annuale della governance** | Verbali della riunione che mostrano la trattazione di 6 argomenti con la presenza della Direzione generale | RSSI | Annuale |

### 3.2 Da avere preferibilmente (rafforza la posizione)

| Prova | Di cosa si tratta |
|-------|-------------------|
| Registro delle lacune | Monitoraggio delle rivalutazioni dopo le modifiche (POL-01 Sezione 5.4) |
| Registro degli insegnamenti appresi | Azioni di miglioramento della governance (POL-01 Sezione 6.2) |
| Classeur ISMS-CHK-POL-01 completato | Auto-valutazione trimestrale della governance (20 requisiti, GOV-01–GOV-20) |

### 3.3 Cosa si può rinviare all'audit di sorveglianza

- Storico completo delle valutazioni trimestrali ISMS-CHK-POL-01 (4 trimestri)
- Registro completo degli insegnamenti appresi con voci multiple
- Registro dettagliato delle lacune con monitoraggio del completamento > 95 %

All'**audit di certificazione iniziale**, gli auditor accettano che i processi siano nuovi. Quello che non possono accettare è l'assenza totale di prove. Anche un solo trimestre di registri di monitoraggio completati + un registro delle eccezioni con 0-3 voci è meglio di niente.

---

## 4. Osservazioni sull'implementazione

### 4.1 Il registro di monitoraggio trimestrale è la dipendenza chiave

Tutto in POL-01 si ricollega in ultima analisi al monitoraggio trimestrale di POL-00. Se il registro trimestrale esiste ed è firmato da Legale/Conformità + RSSI, dimostra:
- GOV-05 (dominio Decisioni di applicabilità) ✅
- Che l'organizzazione mantiene attivamente la consapevolezza normativa ✅
- Che POL-01 Sezione 3 è operativamente attiva ✅

Create un modello semplice per il registro di monitoraggio e compilatelo trimestralmente, anche se la risposta è "nessun cambiamento rilevato." La firma è ciò che conta.

### 4.2 Il registro delle eccezioni è la vostra rete di sicurezza

Il processo in 5 fasi per le eccezioni (POL-01 Sezione 4.2) non è burocrazia — è la vostra giustificazione documentata per ogni controllo che non avete potuto o scelto di non implementare completamente. Senza di esso, un auditor può classificare qualsiasi lacuna come non conformità. Con di esso, la stessa lacuna diventa un'eccezione documentata, valutata rispetto ai rischi e approvata dalla direzione. Questa è la differenza tra una non conformità maggiore e un'accettazione del rischio accettabile.

Iniziate subito il registro, anche se vuoto. Un registro vuoto con la struttura giusta è meglio di nessun registro.

### 4.3 Le firme della Direzione generale sono non negoziabili

La clausola 6.1.3d della norma ISO 27001 richiede esplicitamente l'approvazione della direzione per le decisioni di accettazione del rischio. POL-01 formalizza questo attraverso il Registro delle accettazioni del rischio. Se non riuscite a ottenere le firme della Direzione generale sul registro, non potete completare il trattamento del rischio e non potete ottenere la certificazione. Questo è l'unico processo per cui non esiste una soluzione alternativa — ottenete le firme.

### 4.4 Il registro delle modifiche è facile da dimenticare

Il processo di modifica in 6 fasi (POL-01 Sezione 5.2) si attiva solo quando i criteri di conformità cambiano — il che potrebbe non accadere spesso. Il rischio è dimenticare di registrare una modifica quando si verifica (nuova normativa, feedback dell'audit, minaccia significativa). Designate il RSSI come responsabile del registro e aggiungete "verifica del registro delle modifiche" come punto fisso all'ordine del giorno della revisione annuale della governance.

### 4.5 Non complicare eccessivamente la revisione della governance

POL-01 Sezione 6.1 richiede una revisione annuale della governance che tratti 6 argomenti. Non deve essere una riunione formale del consiglio di amministrazione. Una sessione documentata di 2 ore con il RSSI e un rappresentante della Direzione generale, con verbali che coprono i 6 argomenti, soddisfa il requisito. Un verbale di una pagina è meglio di un processo elaborato che non viene mai realizzato.

---

## 5. Sequenza di implementazione minima vitale

Per un'organizzazione che implementa POL-01 da zero, nell'ordine:

1. **Approvare e firmare POL-01** — il RSSI redige, Legale/Conformità rivede, la Direzione generale approva
2. **Creare i documenti di competenza** — documentare che RSSI, Legale/Conformità, RPD soddisfano i criteri della Sezione 2.3
3. **Creare il Registro delle eccezioni** — solo il modello, anche se vuoto
4. **Creare il Registro delle accettazioni del rischio** — solo il modello, anche se vuoto
5. **Creare il Registro delle modifiche al SGSI** — solo il modello, anche se vuoto
6. **Completare il primo registro di monitoraggio trimestrale POL-00** — anche un solo trimestre
7. **Aggiornare POL-00 Sezione 7** — aggiungere il riferimento all'integrazione con la gestione dei cambiamenti
8. **Aggiornare POL-A.5.1** — aggiungere il riferimento al quadro di governance
9. **Pianificare la revisione annuale della governance** — inserirla nel calendario ora
10. **Generare il classeur ISMS-CHK-POL-01** — eseguire lo script, completare un ciclo di valutazione

I passi 1-6 sono prerequisiti per l'audit di Fase 2. I passi 7-10 rafforzano la posizione.

---

## 6. Posizioni dei file

| Documento | Posizione |
|-----------|-----------|
| Politica POL-01 | `POL/ISMS-POL-01 - Quadro di governance e processo decisionale del SGSI.md` |
| Generatore del classeur di valutazione | `SCR/ISMS-SCR-CHK-POL-01.py` |
| Classeur di valutazione generato | `WKBK/ISMS-CHK-POL-01_...xlsx` |
| Questa guida all'implementazione | `INS/ISMS-INS-POL-01-Guida-all-Implementazione - IT.md` |
| Analisi dei rimandi incrociati del Copilot | `96-isms-core-audit-reports/.../isms-copilot-pol-01-referencing-instructions.md` |

---

<!-- QA_VERIFIED: 2026-04-03 -->
