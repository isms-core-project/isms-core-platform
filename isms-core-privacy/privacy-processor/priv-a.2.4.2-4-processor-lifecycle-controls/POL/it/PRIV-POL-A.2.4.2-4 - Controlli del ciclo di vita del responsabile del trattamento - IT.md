<!-- ISMS-CORE:POLICY:PRIV-POL-A.2.4.2-4-IT:privacy:POL:a.2.4.2-4 -->
**PRIV-POL-A.2.4.2-4 — Controlli del ciclo di vita del responsabile del trattamento**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Controlli del ciclo di vita del responsabile del trattamento |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | PRIV-POL-A.2.4.2-4 |
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

**Catena di approvazione** : Principale: RPD; Secondaria: RSSI; Autorità finale: Direzione generale.

**Documenti correlati** :
- PRIV-POL-00 / PRIV-POL-01; PRIV-IMP-A.2.4.2-4-UG / TG
- PRIV-POL-A.2.2.2-7 (Accordi e obblighi del responsabile del trattamento)
- PRIV-POL-A.1.4.6-10 (Ciclo di vita dei DCP — controparte lato titolare del trattamento)
- PRIV-POL-A.3.5-7 (Classificazione e trasferimento)
- ISO/IEC 27701:2025 Controlli A.2.4.2, A.2.4.3, A.2.4.4
- RGPD Articolo 28(3)(g) (restituzione o cancellazione al termine del servizio); Articolo 32(1)(a) (sicurezza delle trasmissioni)
- LPD svizzera Articolo 9 (misure di sicurezza equivalenti)

**Applicabilità del ruolo** : Questa politica si applica a [Organizzazione] che agisce in qualità di **Responsabile del trattamento dei DCP unicamente**. I controlli A.2.4.2–A.2.4.4 sono specifici per il responsabile del trattamento (Tabella A.2).

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] quando agisce come responsabile del trattamento dei DCP per lo smaltimento dei file temporanei, la restituzione/trasferimento/smaltimento sicuro dei DCP del cliente al termine del servizio, e i controlli di trasmissione dei DCP — conformemente ai controlli A.2.4.2, A.2.4.3 e A.2.4.4 di ISO/IEC 27701:2025.

**Perimetro** : Tutti i file temporanei creati durante il trattamento dei DCP del cliente; tutta la gestione di fine servizio dei DCP del cliente; qualsiasi trasmissione di DCP su reti dati per conto dei clienti.

---

# Perimetro e applicabilità

## Enunciati dei controlli ISO/IEC 27701:2025

**Controllo A.2.4.2 — File temporanei**
Il controllo A.2.4.2 richiede che [Organizzazione] garantisca che i file temporanei creati durante il trattamento dei DCP vengano smaltiti entro un periodo definito e documentato utilizzando procedure documentate.

**Controllo A.2.4.3 — Restituzione, trasferimento o smaltimento dei DCP**
Il controllo A.2.4.3 richiede che [Organizzazione] sia in grado di restituire, trasferire o smaltire in modo sicuro i DCP del cliente, e di rendere disponibile ai clienti la propria politica di restituzione/smaltimento.

**Controllo A.2.4.4 — Controlli di trasmissione dei DCP**
Il controllo A.2.4.4 richiede che [Organizzazione] applichi controlli appropriati ai DCP trasmessi su reti dati per conto dei clienti, per garantire che i dati raggiungano la destinazione prevista.

## Quadro normativo

**Obbligatorio (Livello 1)** (per PRIV-POL-00):
- **RGPD UE** : Articolo 28(3)(g) (il responsabile del trattamento cancella o restituisce i DCP al termine del servizio secondo la scelta del titolare del trattamento e cancella le copie salvo obbligo legale); Articolo 32(1)(a) (pseudonimizzazione, cifratura e sicurezza delle trasmissioni)
- **LPD svizzera** : Articolo 9 (misure di sicurezza equivalenti ai requisiti del titolare del trattamento)
- **ISO/IEC 27701:2025** : Controlli A.2.4.2–A.2.4.4 (normativi)

---

# Disposizioni della politica

## A.2.4.2 — File temporanei (responsabile del trattamento)

[Organizzazione] DEVE garantire che i file temporanei creati durante il trattamento dei DCP per conto dei clienti vengano smaltiti entro periodi documentati e specificati.

I requisiti di smaltimento dei file temporanei per le attività del responsabile del trattamento sono coerenti con la politica generale sui file temporanei in PRIV-POL-A.1.4.6-10 (A.1.4.7), applicata ai contesti DCP del cliente:
- File di cache e staging di trattamento: smaltiti entro 48 ore dal completamento del trattamento
- Log di errori/eccezioni contenenti DCP del cliente: smaltiti entro 30 giorni (rotazione automatizzata)
- File di esportazione generati per la consegna al cliente: smaltiti entro 72 ore dopo la consegna confermata al cliente

I periodi specifici sono documentati in PRIV-IMP-A.2.4.2-4-TG. I meccanismi di eliminazione automatizzata sono preferiti.

---

## A.2.4.3 — Restituzione, trasferimento o smaltimento dei DCP del cliente

Quando un contratto con il cliente termina o un cliente richiede la restituzione o la cancellazione dei propri DCP, [Organizzazione] DEVE essere in grado di:

- **Restituire** i DCP al cliente in un formato strutturato e concordato
- **Trasferire** i DCP a un altro responsabile del trattamento designato dal cliente
- **Smaltire** i DCP in modo sicuro utilizzando metodi di cancellazione approvati

[Organizzazione] DEVE scegliere tra queste opzioni in conformità con l'istruzione documentata del cliente. In assenza di un'istruzione specifica del cliente al termine del contratto, [Organizzazione] DEVE richiedere istruzioni e seguire il valore predefinito specificato nel contratto di trattamento.

### Standard di smaltimento

Lo smaltimento dei DCP al termine del contratto segue i metodi definiti in PRIV-POL-A.1.4.6-10 (A.1.4.9):
- Record di database: SQL DELETE o equivalente; o cancellazione crittografica per i depositi cifrati
- File system: cancellazione crittografica o sovrascrittura approvata
- Supporti di backup: allineati al calendario di conservazione dei backup; backup scaduti purgati secondo il calendario; o cancellazione fuori ciclo su istruzione del cliente con conferma. Laddove la successiva scadenza del backup pianificata non avvenga entro la finestra di cancellazione richiesta dal cliente, [Organizzazione] DEVE immediatamente isolare e limitare l'accesso ai backup contenenti i DCP di quel cliente come misura provvisoria, in attesa della cancellazione fisica alla successiva scadenza

La conferma dello smaltimento DEVE essere fornita per iscritto al cliente entro il periodo specificato nel contratto di trattamento; il valore predefinito organizzativo è 30 giorni dopo la fine del servizio, salvo che il contratto non specifichi diversamente.

**Valore predefinito al termine del contratto** : Laddove non vengano ricevute istruzioni dal cliente e il contratto di trattamento non specifichi un valore predefinito, [Organizzazione] DEVE richiedere istruzioni al cliente entro 5 giorni lavorativi dalla fine del servizio. Se non viene ricevuta alcuna risposta entro 30 giorni da tale notifica, [Organizzazione] cancellerà in modo sicuro tutti i DCP del cliente e confermerà la cancellazione al cliente per iscritto.

### Disponibilità della politica

[Organizzazione] DEVE mettere a disposizione dei clienti la propria politica di restituzione, trasferimento e smaltimento su richiesta e, ove contrattualmente richiesto, come parte della documentazione del contratto di trattamento.

---

## A.2.4.4 — Controlli di trasmissione dei DCP (responsabile del trattamento)

[Organizzazione] DEVE sottoporre i DCP trasmessi per conto dei clienti su reti dati a controlli appropriati per garantire che raggiungano la destinazione prevista.

I controlli di trasmissione sono coerenti con PRIV-POL-A.3.5-7 (regole di trasferimento) e PRIV-POL-A.3.23-31 (controlli crittografici):
- Tutti i DCP trasmessi su reti DEVONO essere cifrati in transito (minimo TLS 1.2; TLS 1.3 preferito)
- Le trasmissioni di DCP RISERVATI e LIMITATI DEVONO utilizzare metodi di trasferimento sicuro approvati
- Deve essere ottenuta la conferma di consegna o la ricevuta di conferma per le trasmissioni di DCP LIMITATI a terze parti
- I log di trasmissione per i DCP trasportati su reti sono mantenuti per PRIV-POL-A.3.25 (registrazione)

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RPD** | Gestisce il processo di restituzione/smaltimento dei DCP a fine servizio; conferma il completamento ai clienti; mantiene i registri di smaltimento |
| **RSSI / Team Sicurezza IT** | Implementa i meccanismi di eliminazione dei file temporanei; esegue lo smaltimento; configura l'applicazione di TLS; fornisce la conferma di smaltimento |
| **Customer Success** | Coordina con i clienti l'opzione di restituzione/smaltimento preferita al termine del contratto; segue il completamento dello smaltimento |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Registrazioni di eliminazione dei file temporanei | Conferma automatizzata/manuale dell'eliminazione dei file temporanei DCP del cliente | 3 anni dalla data di eliminazione |
| Registrazioni di smaltimento a fine servizio | Conferma scritta di restituzione/trasferimento/smaltimento per cliente | 5 anni |
| Conferma di smaltimento dei DCP del cliente | Conferma scritta inviata ai clienti al termine del contratto | 5 anni |
| Configurazione della cifratura delle trasmissioni | Registrazioni di configurazione TLS per la trasmissione dei DCP del cliente | In corso + 3 anni |

---

# Considerazioni di audit

- Periodi di smaltimento dei file temporanei documentati e meccanismi automatizzati in atto
- Gestione dei DCP a fine servizio: prove di restituzione, trasferimento o smaltimento secondo istruzione del cliente
- Conferma scritta dello smaltimento fornita ai clienti entro il periodo contrattuale
- Applicazione di TLS per la trasmissione dei DCP (prove di configurazione)
- Politica di restituzione/smaltimento disponibile per i clienti

---

<!-- QA_VERIFIED: 2026-04-03 -->
