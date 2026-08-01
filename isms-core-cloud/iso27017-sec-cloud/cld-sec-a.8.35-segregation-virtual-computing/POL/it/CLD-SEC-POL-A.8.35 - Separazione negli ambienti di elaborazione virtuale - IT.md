<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.8.35-IT:sec:POL:a.8.35 -->
**CLD-SEC-POL-A.8.35 — Separazione negli ambienti di elaborazione virtuale**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Separazione negli ambienti di elaborazione virtuale |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | CLD-SEC-POL-A.8.35 |
| **Autore del documento** | RSSI / Responsabile Sicurezza Cloud |
| **Proprietario del documento** | RSSI |
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
| 1.0 | [Data da definire] | RSSI | Politica iniziale per l'implementazione di ISO/IEC 27017:2026 Ed. 2 |

**Ciclo di revisione** : Annuale (o in caso di cambiamenti significativi all'architettura di virtualizzazione, o a seguito di un incidente relativo alla separazione)
**Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** :

- Principale: RSSI
- Secondaria: Responsabile Sicurezza Cloud
- Tecnica: Responsabile Ingegneria Cloud
- Autorità finale: Direzione generale

**Documenti correlati** :

- ISMS-POL-A.8.20-22 (Sicurezza di rete — politica SGSI principale per la separazione delle reti A.8.22)
- CLD-SEC-POL-A.5.38 (Ruoli e responsabilità condivisi in un ambiente di cloud computing)
- CLD-SEC-POL-A.8.36 (Rilevamento e prevenzione dell'uso non autorizzato dei servizi cloud)
- CLD-SEC-IMP-A.8.35-TG (Separazione negli ambienti di elaborazione virtuale — Guida tecnica, contiene gli schemi completi di separazione e il modello di architettura)
- CLD-SEC-REF-A.5-A.8 (Addendum di guidance sulla sicurezza cloud)
- ISO/IEC 27017:2026, Clausola 8.35 (CLD — Separazione negli ambienti di elaborazione virtuale)
- ISO/IEC 27040 (Sicurezza dello storage)

---

## Riepilogo esecutivo

Questa politica stabilisce come [Organizzazione] protegge gli ambienti dei tenant da accessi non autorizzati all'interno di ambienti di elaborazione virtuale multi-tenant, in conformità con ISO/IEC 27017:2026, Clausola 8.35.

**Perimetro** : Tutti gli ambienti di elaborazione virtuale in cui [Organizzazione] opera nell'ambito di un servizio cloud multi-tenant — sia il proprio ambiente virtuale di [Organizzazione] eseguito sul servizio cloud di un CSP terzo (ruolo CSC), sia l'infrastruttura multi-tenant che [Organizzazione] gestisce per i propri CSC (ruolo CSP).

**Nota sui controlli estesi** : ISO/IEC 27017:2026, Clausola 8.35 è uno dei quattro controlli estesi specifici per il cloud «CLD» introdotti dalla seconda edizione dello standard (insieme a 5.38, 5.39 e 8.36). È tematicamente più vicino — ed è implementato in parallelo — agli obblighi di separazione delle reti del controllo 8.22 dell'Annex A di ISO/IEC 27001:2022, ma affronta specificamente la separazione logica delle applicazioni virtualizzate, dello storage e delle risorse di rete, non solo il traffico di rete.

**Rischio fondamentale** : Una separazione inadeguata in un ambiente di elaborazione virtuale condiviso può esporre i dati o i carichi di lavoro di un tenant a un altro tenant, a terze parti o a personale non autorizzato del CSP. Poiché l'isolamento dei tenant è in gran parte non visibile al CSC, [Organizzazione] deve definire esplicitamente i propri requisiti di separazione (in qualità di CSC) e applicare rigorosamente la separazione logica (in qualità di CSP), anziché presumere che l'isolamento sia automaticamente adeguato. Un divario di separazione individuato in qualsiasi momento — durante l'onboarding, la verifica periodica o i test — è trattato come un rischio per la sicurezza delle informazioni che richiede una valutazione, non come una nota di configurazione da rivedere successivamente.

---

# Perimetro e applicabilità

## ISO/IEC 27017:2026 — Clausola 8.35

**Dichiarazione del controllo (ISO/IEC 27017:2026, 8.35):**
> «L'ambiente virtuale di un CSC in esecuzione su un servizio cloud dovrebbe essere protetto dall'accesso non autorizzato.»

**Finalità (ISO/IEC 27017:2026, 8.35):**
> «Prevenire l'accesso inappropriato o la divulgazione di informazioni attraverso una virtualizzazione non sicura.»

*(Traduzione di lavoro predisposta a partire dal testo originale inglese della norma, a fini di leggibilità; in caso di discrepanza, fa fede il testo inglese ufficiale di ISO/IEC 27017:2026.)*

## Applicabilità

Questa politica si applica a:

- Tutte le istanze di macchine virtuali, container, volumi di storage e reti virtuali di [Organizzazione] in esecuzione sul servizio cloud multi-tenant di un CSP terzo (ruolo CSC)
- Tutta l'infrastruttura virtualizzata multi-tenant che [Organizzazione] gestisce per erogare servizi cloud ai propri CSC (ruolo CSP)
- Tutto il personale con accesso amministrativo ai livelli di virtualizzazione, hypervisor o orchestrazione dei container

## Quadro normativo e degli standard

ISO/IEC 27017:2026 è un'estensione informativa di ISO/IEC 27002:2022. La clausola 8.35 non corrisponde ad alcun controllo numerato di ISO/IEC 27002:2022; è nuova nella seconda edizione 2026, sostituendo ed estendendo il CLD.9.5.1 della prima edizione del 2015 («Separazione negli ambienti di elaborazione virtuale»). È implementata in parallelo al controllo 8.22 dell'Annex A di ISO/IEC 27001:2022 (Separazione delle reti) e si basa sulle indicazioni sulla multi-tenancy sicura fornite da ISO/IEC 27040.

---

# Disposizioni della politica: Separazione negli ambienti di elaborazione virtuale (8.35)

## Obblighi in qualità di cliente di servizio cloud (CSC)

Quando [Organizzazione] agisce in qualità di cliente di servizio cloud, [Organizzazione] DEVE:

- Classificare i dati e il carico di lavoro da eseguire sul servizio cloud in base alla sensibilità, e definire i propri requisiti di separazione dell'ambiente di [Organizzazione] per ottenere l'isolamento dei tenant, prima della selezione del servizio
- Fissare un livello minimo di isolamento accettabile appropriato a tale classificazione (ad es. isolamento logico imposto dall'hypervisor per i carichi di lavoro standard, infrastruttura dedicata/mono-tenant per i carichi di lavoro più sensibili), e documentarlo nella dichiarazione dei requisiti di separazione (schema in CLD-SEC-IMP-A.8.35-TG, Sezione 1)
- Verificare, prima e periodicamente durante l'utilizzo del servizio, che il CSP soddisfi tali requisiti di separazione, utilizzando la documentazione del CSP incrociata con garanzie indipendenti (certificazioni, report di audit) laddove disponibili
- Effettuare una nuova verifica almeno annualmente, e ogniqualvolta il CSP annunci un cambiamento sostanziale alla propria architettura di virtualizzazione o multi-tenancy
- Laddove la verifica individui un divario tra i controlli di separazione del CSP e il requisito dichiarato da [Organizzazione], trattarlo come un rischio per la sicurezza delle informazioni e integrarlo nel processo documentato di valutazione e trattamento del rischio di [Organizzazione]

## Obblighi in qualità di fornitore di servizio cloud (CSP)

Quando [Organizzazione] agisce in qualità di fornitore di servizio cloud, [Organizzazione] DEVE:

- Applicare la separazione logica dei dati dei CSC, delle applicazioni virtualizzate, dei sistemi operativi, dello storage e delle risorse di rete, per garantire l'isolamento delle risorse utilizzate da tenant diversi in un ambiente multi-tenant, documentata per ciascun livello nella documentazione dell'architettura di separazione (modello in CLD-SEC-IMP-A.8.35-TG, Sezione 3)
- Valutare i rischi associati all'esecuzione di software fornito dai CSC all'interno dei servizi cloud offerti da [Organizzazione], prima di consentire l'esecuzione di tale software in infrastrutture condivise, applicando controlli compensativi laddove il confine di isolamento sia valutato insufficiente
- Applicare la separazione delle funzioni di amministrazione interna proprie di [Organizzazione] dalle risorse utilizzate dai CSC, mediante un percorso di accesso amministrativo distinto
- Pianificare test periodici dell'architettura di separazione (ad es. penetration test ai confini dei tenant, audit di configurazione dell'isolamento di hypervisor/container) per confermare che la progettazione documentata rimanga efficace nella pratica, non solo corretta sulla carta

## Implementazione dipendente dalla tecnologia

[Organizzazione] riconosce che l'implementazione della separazione logica dipende dalle tecnologie di virtualizzazione applicate. Le configurazioni di rete e storage possono essere virtualizzate tramite una funzione di virtualizzazione software che fornisce un ambiente virtuale (ad esempio, un sistema operativo virtuale o un meccanismo di isolamento dei container). Laddove tale virtualizzazione software sia utilizzata, [Organizzazione] DEVE progettare e implementare la separazione utilizzando le funzioni di separazione native di tale software, in aggiunta ai controlli fisici o di livello di rete sottostanti.

## Considerazioni legali e normative

Laddove leggi o normative applicabili richiedano la separazione delle reti o l'isolamento del traffico di rete per i dati trattati da [Organizzazione], [Organizzazione] DEVE assicurare che i propri controlli di separazione dell'elaborazione virtuale soddisfino tali requisiti in aggiunta ai requisiti di base della presente politica, e confermarlo nell'ambito della revisione annuale.

## Comunicazione e sensibilizzazione

[Organizzazione] DEVE comunicare i requisiti di separazione e le decisioni architetturali ai team interni che li progettano, gestiscono o su cui fanno affidamento (Ingegneria Cloud, Erogazione del servizio cloud, Operazioni di Sicurezza), tramite la documentazione dell'architettura di separazione e l'inclusione nel programma di sensibilizzazione alla sicurezza delle informazioni dell'organizzazione (vedere ISMS-POL-A.6.3). Laddove [Organizzazione] agisca in qualità di CSP, gli impegni di separazione chiave rilevanti per un CSC DEVONO essere comunicati a tale CSC tramite materiali di onboarding o documentazione del servizio.

## Dichiarazione dei requisiti di separazione — Contenuto minimo

La dichiarazione dei requisiti di separazione (schema completo in CLD-SEC-IMP-A.8.35-TG, Sezione 1) DEVE registrare, per ciascun servizio cloud utilizzato: l'identificativo del servizio; la classificazione dei dati/del carico di lavoro; il livello minimo di isolamento accettabile e la relativa motivazione; e la data in cui il requisito è stato definito.

## Documentazione dell'architettura di separazione — Contenuto minimo

La documentazione dell'architettura di separazione (modello completo in CLD-SEC-IMP-A.8.35-TG, Sezione 3) DEVE registrare, per ciascun ambiente multi-tenant gestito da [Organizzazione]: il meccanismo di separazione applicato a ciascun livello (dati dei CSC, applicazioni virtualizzate, sistemi operativi, storage, rete); la progettazione della separazione dell'amministrazione interna; e una sintesi dei test di separazione più recenti e dei relativi risultati.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|-----------------|
| **RSSI** | È proprietario di CLD-SEC-POL-A.8.35; approva l'architettura di separazione per gli ambienti multi-tenant gestiti da [Organizzazione] (ruolo CSP); approva l'accettazione dei controlli di separazione di un CSP per i carichi di lavoro critici (ruolo CSC); esamina le escalation di rischio relative alla separazione |
| **Responsabile Sicurezza Cloud** | Definisce i requisiti di separazione per i servizi utilizzati (ruolo CSC); verifica periodicamente i controlli di separazione del CSP; riferisce al RSSI gli indicatori di verifica e test della separazione |
| **Responsabile Ingegneria Cloud** | Progetta e implementa i controlli di separazione logica (hypervisor, container, storage, rete) per gli ambienti multi-tenant gestiti da [Organizzazione] (ruolo CSP); pianifica ed esamina i test di separazione periodici |
| **Erogazione del servizio cloud / Ingegneria** | Valuta il rischio del software fornito dai CSC prima di consentirne l'esecuzione in infrastrutture condivise; mantiene la separazione dell'accesso amministrativo interno dalle risorse dei CSC |

---

# Requisiti in materia di prove

| Prova | Descrizione | Responsabile | Conservazione |
|-------|-------------|--------------|---------------|
| Dichiarazione dei requisiti di separazione (ruolo CSC) | Requisiti di isolamento dei tenant documentati da [Organizzazione] per ciascun servizio cloud utilizzato | Responsabile Sicurezza Cloud | In corso + 3 anni |
| Registrazioni di verifica della separazione del CSP | Registrazioni della verifica periodica che i controlli di separazione di un CSP soddisfino i requisiti di [Organizzazione] | Responsabile Sicurezza Cloud | In corso + 3 anni |
| Documentazione dell'architettura di separazione (ruolo CSP) | Documentazione tecnica dei controlli di separazione logica implementati su applicazioni virtualizzate, storage e rete | Responsabile Ingegneria Cloud | Versione attuale + versioni precedenti per 3 anni |
| Valutazioni del rischio del software fornito dai CSC | Registrazioni delle valutazioni del rischio eseguite prima di consentire l'esecuzione di software fornito dai CSC in infrastrutture condivise | Erogazione del servizio cloud / Ingegneria | In corso + 3 anni |
| Registrazioni dei test di separazione | Risultati dei test periodici ai confini dei tenant e degli audit di configurazione dell'isolamento | Responsabile Ingegneria Cloud | In corso + 3 anni |
| Registrazioni di divari di separazione / rischi | Registrazioni di qualsiasi divario di separazione sottoposto a escalation nel processo di valutazione e trattamento del rischio, con relativa risoluzione | RSSI | In corso + 3 anni |

---

# Monitoraggio e indicatori

Il Responsabile Sicurezza Cloud riferisce al RSSI, con cadenza almeno trimestrale:

- La proporzione dei servizi cloud (ruolo CSC) con una verifica di separazione aggiornata negli ultimi 12 mesi
- I risultati e lo stato di remediation dei test di separazione più recenti (ruolo CSP)
- Il numero di divari di separazione individuati e sottoposti a escalation nel processo di valutazione e trattamento del rischio, con il relativo stato di risoluzione

---

# Considerazioni di audit

Gli auditor che verificano la conformità a CLD-SEC-POL-A.8.35 devono aspettarsi di trovare:

- Requisiti di separazione documentati per ogni servizio cloud che [Organizzazione] utilizza in qualità di CSC
- Prove della verifica periodica che i controlli di separazione del CSP soddisfino tali requisiti, e che i divari siano sottoposti a escalation come rischi anziché lasciati aperti
- Documentazione tecnica dell'architettura di separazione logica per qualsiasi ambiente multi-tenant gestito da [Organizzazione] in qualità di CSP, che copra dati, applicazioni virtualizzate, sistemi operativi, storage e rete
- Prove che l'accesso amministrativo interno di [Organizzazione] sia separato dalle risorse rivolte ai CSC
- Registrazioni di valutazione del rischio per il software fornito dai CSC eseguito all'interno dell'infrastruttura condivisa di [Organizzazione]
- Registrazioni di test di separazione periodici, non solo una revisione una tantum della progettazione dell'architettura

---

<!-- QA_VERIFIED: 2026-08-01 -->
