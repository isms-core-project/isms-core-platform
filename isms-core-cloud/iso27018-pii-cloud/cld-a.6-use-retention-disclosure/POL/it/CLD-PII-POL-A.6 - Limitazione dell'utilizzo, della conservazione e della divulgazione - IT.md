<!-- ISMS-CORE:POLICY:CLD-PII-POL-A.6-IT:cloud:POL:a.6 -->
**CLD-PII-POL-A.6 — Limitazione dell'utilizzo, della conservazione e della divulgazione**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Responsabile del trattamento di DCP nel cloud pubblico — Limitazione dell'utilizzo, della conservazione e della divulgazione |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | CLD-PII-POL-A.6 |
| **Autore del documento** | Responsabile della Protezione dei Dati (RPD) / RSSI |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Data da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |
| **Versione del prodotto Cloud** | 1.0 |

**Cronologia delle versioni** :

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 1.0 | [Data da definire] | RPD / RSSI | Politica iniziale per l'implementazione di ISO/IEC 27018:2025 Ed. 3 |

**Ciclo di revisione** : Annuale (o in caso di significativi cambiamenti normativi o del modello di servizio)
**Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** :
- Principale: Responsabile della Protezione dei Dati (RPD)
- Secondaria: RSSI / Responsabile Sicurezza Cloud
- Autorità finale: Direzione generale

**Documenti correlati** :
- PRIV-POL-00 (Quadro di applicabilità normativa sulla privacy)
- ISMS-POL-A.5.34 (Privacy e protezione dei DCP)
- ISMS-POL-A.5.33 (Protezione dei registri)
- CLD-PII-POL-A.3 (Legittimità e specificazione della finalità)
- CLD-PII-POL-A.5 (Minimizzazione dei dati)
- CLD-PII-POL-A.10 (Accountability — notifica delle violazioni, restituzione/smaltimento)
- ISO/IEC 27018:2025 Annex A, Sezione A.6 e Controlli A.6.1–A.6.2
- ISO/IEC 27701:2025 Controlli A.2.5.4 (registrazioni delle divulgazioni di DCP a terze parti), A.2.5.5 (notifica delle richieste di divulgazione di DCP) e A.2.5.6 (divulgazioni vincolanti di DCP)
- RGPD Articolo 5(1)(b) e (e) (limitazione della finalità, limitazione della conservazione); Articolo 28(3)(a); Articolo 28(3)(f)
- LPD svizzera Articolo 6(3) (limitazione della finalità); Articolo 9(2)(d) (obbligo di assistenza del responsabile del trattamento)

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] come responsabile del trattamento di DCP nel cloud pubblico in materia di limitazione dell'utilizzo, della conservazione e della divulgazione — specificamente l'obbligo di notificare ai titolari del trattamento dei DCP le divulgazioni vincolanti di DCP a terze parti, e di mantenere registrazioni di tutte tali divulgazioni — conformemente a ISO/IEC 27018:2025 Annex A, Sezione A.6 e Controlli A.6.1 e A.6.2.

**Perimetro** : Tutti i DCP conservati da [Organizzazione] per conto di titolari del trattamento dei DCP, e tutte le divulgazioni di tali DCP a terze parti incluse forze dell'ordine, autorità di regolamentazione e altre entità.

**Motivazione dei controlli combinati** : A.6.1 e A.6.2 affrontano lo scenario critico nel cloud pubblico in cui organi governativi o regolatori impongono al responsabile del trattamento di divulgare DCP senza la conoscenza del titolare del trattamento. Insieme richiedono trasparenza (notificare al titolare del trattamento) e accountability (registrare tutte le divulgazioni), garantendo che il titolare del trattamento possa adempiere ai propri obblighi di notifica normativa.

---

# Perimetro e applicabilità

## Enunciati dei controlli ISO/IEC 27018:2025

**Sezione A.6 — Limitazione dell'utilizzo, della conservazione e della divulgazione (principio)**

La Sezione A.6 stabilisce il principio che i DCP devono essere conservati solo per il tempo necessario alla finalità specificata, con calendari di conservazione documentati e applicati, e che le divulgazioni a terze parti devono essere limitate ai destinatari autorizzati e al minimo necessario.

**Controllo A.6.1 — Notifica di divulgazione di DCP**

Il Controllo A.6.1 richiede che il responsabile del trattamento notifichi al titolare del trattamento dei DCP quando è legalmente obbligato a divulgare DCP a una terza parte — prima della divulgazione ove possibile, o alla prima opportunità utile dopo la cessazione di qualsiasi divieto legale di notifica.

**Controllo A.6.2 — Registrazione delle divulgazioni di DCP**

Il Controllo A.6.2 richiede che il responsabile del trattamento mantenga registrazioni di tutte le divulgazioni di DCP a terze parti, acquisendo il destinatario, la data, le categorie di DCP, la base giuridica e se il titolare del trattamento è stato notificato, e che renda tali registrazioni disponibili al titolare del trattamento su richiesta.

## Cosa questa politica NON copre

- I periodi di conservazione primari per i DCP a riposo — questi sono stabiliti dalle istruzioni del titolare del trattamento dei DCP e inclusi negli accordi di servizio. Laddove un'istruzione di conservazione sia in conflitto con un blocco legale o un'ordinanza di conservazione vincolante, [Organizzazione] conserva i DCP per il periodo legalmente richiesto e notifica il titolare del trattamento. Vedere CLD-PII-POL-A.10.3 per la restituzione e lo smaltimento al termine del contratto.
- La restituzione o lo smaltimento dei DCP alla risoluzione del contratto — trattato in CLD-PII-POL-A.10.3

## Quadro normativo

**Livello 1: Conformità obbligatoria** (per PRIV-POL-00):

- **RGPD UE** : Articolo 5(1)(b) (limitazione della finalità); Articolo 5(1)(e) (limitazione della conservazione); Articolo 28(3)(a) (trattamento solo su istruzione); Articolo 28(3)(f) (il responsabile del trattamento assiste il titolare del trattamento per gli obblighi degli Articoli 32–36)
- **LPD svizzera** : Articolo 6(3) (limitazione della finalità); Articolo 9(2)(d) (il responsabile del trattamento assiste il titolare del trattamento)
- **ISO/IEC 27018:2025** : Controlli A.6.1 e A.6.2

---

# Disposizioni della politica: Limitazione della conservazione (principio A.6)

## Rispetto del calendario di conservazione

[Organizzazione] DEVE conservare i DCP per conto dei titolari del trattamento solo per la durata specificata nell'accordo di servizio. Laddove l'accordo di servizio non specifichi un periodo di conservazione, [Organizzazione] DEVE richiedere istruzioni scritte esplicite dal titolare del trattamento dei DCP prima di implementare qualsiasi configurazione di conservazione.

[Organizzazione] DEVE implementare l'applicazione automatizzata della conservazione (eliminazione o archiviazione automatizzata) ove tecnicamente fattibile. Il ricorso all'eliminazione manuale è accettabile solo laddove l'applicazione automatizzata non sia tecnicamente possibile, nel qual caso l'eliminazione manuale DEVE essere documentata e riesaminata trimestralmente.

---

# Disposizioni della politica: Notifica di divulgazione di DCP (A.6.1)

## Obbligo di notifica preventiva

Laddove [Organizzazione] riceva una richiesta vincolante da un'autorità di polizia giudiziaria, un'autorità di regolamentazione, un tribunale o un altro organo governativo che richiede la divulgazione di DCP appartenenti a un titolare del trattamento dei DCP, [Organizzazione] DEVE:

1. Notificare il titolare del trattamento dei DCP rilevante della richiesta di divulgazione **prima della divulgazione**, includendo:
   - L'identità dell'autorità richiedente (nella misura legalmente consentita)
   - Le categorie e il perimetro dei DCP richiesti
   - La base giuridica citata per la richiesta
   - Il termine richiesto per la divulgazione

2. Concedere al titolare del trattamento dei DCP almeno 5 giorni lavorativi per richiedere una contestazione legale o un provvedimento d'urgenza prima della divulgazione, laddove il termine di divulgazione lo consenta. Laddove il termine non consenta 5 giorni lavorativi, [Organizzazione] concede il massimo tempo disponibile

3. Procedere alla divulgazione solo dopo che:
   - La notifica al titolare del trattamento sia stata data e il periodo di risposta sia scaduto, oppure
   - Il termine di divulgazione richieda un'azione immediata, nel qual caso il titolare del trattamento DEVE essere notificato simultaneamente alla divulgazione

## Notifica vietata dalla legge

Laddove la legge applicabile vieti a [Organizzazione] di notificare al titolare del trattamento dei DCP una richiesta di divulgazione (es. un'ordinanza di segretezza legale), [Organizzazione] DEVE:

- Documentare il divieto legale e la data a partire dalla quale la notifica è vietata
- Notificare il titolare del trattamento dei DCP alla **prima opportunità utile** dopo la cessazione del divieto legale
- Se [Organizzazione] è permanentemente impedita dal notificare il titolare del trattamento (es. ordinanza permanente di sicurezza nazionale), [Organizzazione] DEVE pubblicare un rapporto di trasparenza o un warrant canary nella misura massima legalmente consentita. Il warrant canary DEVE essere riesaminato e aggiornato al minimo trimestralmente, con il Responsabile Legale/Conformità responsabile del mantenimento della sua accuratezza

## Divulgazione minima

Tutte le divulgazioni legalmente vincolanti DEVONO essere limitate al minimo di DCP necessario per soddisfare l'obbligo legale. [Organizzazione] NON DEVE fornire un accesso più ampio o dataset più estesi di quanto specificamente richiesto dall'ordinanza legale. Il RSSI DEVE confermare che [Organizzazione] disponga della capacità tecnica per produrre estratti di DCP delimitati prima di qualsiasi divulgazione, e DEVE utilizzare tale capacità per limitare il perimetro dei dati forniti.

---

# Disposizioni della politica: Registrazione delle divulgazioni di DCP (A.6.2)

## Registro delle divulgazioni

[Organizzazione] DEVE mantenere un **Registro delle divulgazioni di DCP** che registra ogni divulgazione di DCP a una terza parte, incluse le divulgazioni legalmente vincolanti. Ogni voce DEVE registrare:

| Campo | Descrizione |
|-------|-------------|
| **Data della divulgazione** | Data in cui i DCP sono stati divulgati o trasferiti |
| **Destinatario** | Identità della parte ricevente (autorità, entità o individuo) |
| **Categorie di DCP divulgati** | Tipi di DCP trasferiti (es. dati di identità, dati di contatto, log di trattamento) |
| **Volume** | Numero approssimativo di interessati coinvolti |
| **Base giuridica** | Autorità legale o istruzione del titolare del trattamento che autorizza la divulgazione |
| **Titolare del trattamento notificato** | Sì / No — e se No, motivo e data della notifica successiva |
| **Autorizzato da** | Responsabile di [Organizzazione] che ha autorizzato la divulgazione. Laddove la pre-autorizzazione non fosse possibile a causa dell'urgenza, il responsabile autorizzante DEVE essere documentato entro 24 ore dalla divulgazione |

## Accesso e conservazione

Il Registro delle divulgazioni di DCP DEVE essere:

- Mantenuto dal RPD e protetto contro modifiche non autorizzate
- Reso disponibile a qualsiasi titolare del trattamento dei DCP su richiesta (per le registrazioni relative ai loro DCP)
- Conservato per un minimo di **5 anni** dalla data di ciascuna divulgazione registrata — la conservazione di 5 anni riflette il termine di prescrizione contrattuale standard applicabile nelle giurisdizioni UE e svizzere per le controversie relative agli accordi di trattamento, e supporta i requisiti di audit regolatorio retrospettivo
- Soggetto a revisione trimestrale da parte del RPD

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **Responsabile della Protezione dei Dati (RPD)** | Proprietario del Registro delle divulgazioni di DCP; esamina e autorizza tutte le divulgazioni di DCP a terze parti; gestisce il processo di notifica ai titolari del trattamento; monitora la cessazione dei divieti di notifica |
| **Responsabile Legale/Conformità** | Valuta la validità legale delle richieste di divulgazione; fornisce consulenza sulle opzioni di contestazione legale; interpreta le ordinanze di divieto di notifica; gestisce gli aggiornamenti del warrant canary |
| **RSSI / Responsabile Sicurezza Cloud** | Implementa l'applicazione automatizzata della conservazione; garantisce che la divulgazione sia tecnicamente limitata al perimetro minimo richiesto |
| **Direzione generale** | Approva le divulgazioni in scenari ambigui o ad alto rischio; autorizza i rapporti di trasparenza |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Registro delle divulgazioni di DCP | Log completo di tutte le divulgazioni di DCP a terze parti con i campi obbligatori | 5 anni da ciascuna data di divulgazione |
| Registrazioni di configurazione della conservazione | Documentazione tecnica dell'applicazione automatizzata della conservazione per servizio | In corso + 3 anni |
| Registrazioni di notifica ai titolari del trattamento | Registrazioni di tutte le notifiche inviate ai titolari del trattamento riguardanti le divulgazioni vincolanti | 5 anni |
| Documentazione del divieto legale | Registrazioni delle ordinanze di divieto di notifica e date della notifica successiva | 5 anni |
| Rapporti di trasparenza / Warrant canary | Dichiarazioni pubblicate riguardanti l'assenza di ordinanze legali non divulgate | 5 anni |

---

# Considerazioni di audit

Gli auditor che verificano la conformità a CLD-PII-POL-A.6 devono aspettarsi di trovare:

- Un Registro delle divulgazioni di DCP mantenuto che copra tutte le divulgazioni a terze parti con i campi obbligatori completi
- Prove che i titolari del trattamento dei DCP siano stati notificati di tutte le divulgazioni legalmente vincolanti (o documentazione del motivo per cui la notifica era legalmente vietata)
- Configurazioni di applicazione automatizzata della conservazione allineate con i periodi di conservazione degli accordi di servizio
- Dossier legali/conformità che documentano come le richieste di divulgazione legalmente vincolanti siano state valutate e gestite

---

<!-- QA_VERIFIED: 2026-04-04 -->
