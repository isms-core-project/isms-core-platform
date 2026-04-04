<!-- ISMS-CORE:POLICY:CLD-POL-A.4-IT:cloud:POL:a.4 -->
**CLD-POL-A.4 — Limitazione della raccolta**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Responsabile del trattamento di DCP nel cloud pubblico — Limitazione della raccolta |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | CLD-POL-A.4 |
| **Autore del documento** | RSSI / Responsabile della Protezione dei Dati (RPD) |
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
| 1.0 | [Data da definire] | RSSI / RPD | Politica iniziale per l'implementazione di ISO/IEC 27018:2025 Ed. 3 |

**Ciclo di revisione** : Annuale (o in caso di significativi cambiamenti normativi o del modello di servizio)
**Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** :
- Principale: RSSI / Responsabile Sicurezza Cloud
- Secondaria: Responsabile della Protezione dei Dati (RPD)
- Autorità finale: Direzione generale

**Documenti correlati** :
- PRIV-POL-00 (Quadro di applicabilità normativa sulla privacy)
- ISMS-POL-A.5.34 (Privacy e protezione dei DCP)
- CLD-POL-A.3 (Legittimità e specificazione della finalità)
- CLD-POL-A.5 (Minimizzazione dei dati)
- CLD-POL-A.6 (Limitazione dell'utilizzo, della conservazione e della divulgazione)
- ISO/IEC 27018:2025 Annex A, Sezione A.4 (Limitazione della raccolta — principio)
- ISO/IEC 27701:2025 Controlli A.2.4.2 (responsabile del trattamento — file temporanei) e A.2.4.3 (responsabile del trattamento — restituzione, trasferimento o smaltimento dei DCP)
- RGPD Articolo 5(1)(c) (principio di minimizzazione dei dati); Articolo 28(3)(a) (trattamento solo su istruzione)
- LPD svizzera Articolo 6(2) (proporzionalità); Articolo 9 (obblighi del responsabile del trattamento)

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] come responsabile del trattamento di DCP nel cloud pubblico in materia di limitazione della raccolta — specificamente l'obbligo di trattare solo il minimo di DCP necessario per erogare il servizio contrattuale, e di gestire qualsiasi DCP raccolta in eccesso durante l'erogazione del servizio — conformemente a ISO/IEC 27018:2025 Annex A, Sezione A.4.

**Perimetro** : Tutti i DCP raccolti, ricevuti o altrimenti ottenuti da [Organizzazione] nel corso dell'erogazione di servizi cloud ai titolari del trattamento dei DCP.

**Nota sul principio** : La Sezione A.4 opera a livello di principio. Questa politica traduce tale principio in obblighi operativi specifici per i servizi cloud di [Organizzazione]. I metodi tecnici di minimizzazione dei dati — inclusi anonimizzazione, pseudonimizzazione e gestione dei file temporanei — sono trattati in CLD-POL-A.5.

---

# Perimetro e applicabilità

## ISO/IEC 27018:2025 — Sezione A.4

**Sezione A.4 — Limitazione della raccolta (principio)**

La Sezione A.4 stabilisce il principio che un responsabile del trattamento di DCP nel cloud pubblico deve raccogliere solo i DCP necessari per il servizio contrattuale, documentare le proprie pratiche di raccolta e affrontare tempestivamente qualsiasi DCP in eccesso che si verifichi durante l'erogazione del servizio.

## Cosa questa politica NON copre

- Determinare quali DCP un titolare del trattamento può lecitamente raccogliere dagli interessati — questa è responsabilità del titolare del trattamento
- Metodi tecnici di anonimizzazione e cancellazione per i file temporanei — trattati in CLD-POL-A.5

## Quadro normativo

**Livello 1: Conformità obbligatoria** (per PRIV-POL-00):

- **RGPD UE** : Articolo 5(1)(c) (minimizzazione dei dati — adeguati, pertinenti e limitati a quanto necessario); Articolo 28(3)(a) (il responsabile del trattamento tratta solo su istruzione — nessuna raccolta eccessiva)
- **LPD svizzera** : Articolo 6(2) (proporzionalità — il trattamento dei dati personali deve essere proporzionato alla finalità)
- **ISO/IEC 27018:2025** : Principio della Sezione A.4

---

# Disposizioni della politica: Limitazione della raccolta (A.4)

## Raccolta del minimo necessario

[Organizzazione] DEVE raccogliere, conservare o altrimenti trattare solo il minimo di DCP necessario per erogare il servizio cloud contrattuale. [Organizzazione] NON DEVE:

- Richiedere o accettare categorie di DCP dal titolare del trattamento dei DCP al di là di quanto necessario per l'erogazione del servizio
- Conservare DCP in componenti di sistema, log o database operativi al di là della necessità operativa del trattamento
- Replicare DCP in ambienti (sviluppo, test, staging, produzione) per finalità diverse dall'erogazione e dalla resilienza del servizio senza esplicita autorizzazione del titolare del trattamento

## Documentazione delle pratiche di raccolta

[Organizzazione] DEVE documentare le pratiche di raccolta di DCP per ciascun servizio cloud, includendo:

- Le categorie di DCP raccolte o ricevute durante l'erogazione del servizio
- La giustificazione operativa per ciascuna categoria di DCP
- I componenti di sistema, i log e le posizioni di archiviazione in cui i DCP possono essere presenti
- I periodi di conservazione applicabili a ciascun tipo di raccolta

Questa documentazione DEVE essere mantenuta nel sistema di gestione dei documenti SGSI (o nella piattaforma GRC designata), rivista annualmente e aggiornata in caso di modifiche materiali all'architettura del servizio. Il RSSI è il proprietario designato della documentazione delle pratiche di raccolta.

## DCP in eccesso

Laddove [Organizzazione] determini che siano stati raccolti DCP che superano il perimetro del servizio contrattuale (es. un titolare del trattamento carica un dataset contenente categorie di DCP al di là del perimetro del servizio), [Organizzazione] DEVE:

1. Notificare il titolare del trattamento dei DCP dei DCP in eccesso entro 3 giorni lavorativi dall'identificazione
2. Concordare con il titolare del trattamento se i DCP in eccesso debbano essere restituiti o eliminati in modo sicuro
3. Completare l'azione concordata entro il termine concordato con il titolare del trattamento
4. Documentare l'evento e il suo esito

## Ambienti di sviluppo e test

[Organizzazione] DOVREBBE utilizzare dati anonimizzati o sintetici in ambienti non di produzione ovunque tecnicamente fattibile, e DEVE trattare l'utilizzo di DCP di produzione come ultima risorsa. I DCP degli ambienti di produzione NON DEVONO essere utilizzati in ambienti di sviluppo, test o staging senza esplicita autorizzazione scritta del titolare del trattamento dei DCP. Laddove venga ottenuta l'autorizzazione del titolare del trattamento, DEVE essere utilizzato il minimo necessario di DCP, gli stessi controlli di sicurezza applicabili in produzione DEVONO applicarsi (in conformità con CLD-POL-A.11) e l'accesso DEVE essere limitato al minimo personale richiesto per la finalità specifica.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI / Responsabile Sicurezza Cloud** | Garantisce che l'architettura del servizio raccolga il minimo necessario di DCP; mantiene la documentazione di raccolta; esamina il perimetro di raccolta durante la progettazione e le modifiche del servizio |
| **Responsabile della Protezione dei Dati (RPD)** | Esamina la documentazione di raccolta annualmente; fornisce consulenza sulle valutazioni di proporzionalità; monitora gli eventi di raccolta eccessiva |
| **Erogazione del servizio cloud / Ingegneria** | Implementa un'architettura di raccolta minima; segnala tempestivamente gli eventi di raccolta eccessiva a RSSI e RPD |
| **Responsabile Legale/Conformità** | Fornisce consulenza sugli obblighi di proporzionalità e minimizzazione ai sensi del RGPD e della LPD |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Documentazione delle pratiche di raccolta | Categorie di DCP documentate, giustificazioni e posizioni per servizio | In corso + versioni precedenti per 3 anni |
| Registrazioni di revisione annuale | Registrazioni firmate delle revisioni annuali delle pratiche di raccolta | 3 anni |
| Registrazioni di eventi di DCP in eccesso | Documentazione di qualsiasi evento di DCP in eccesso, notifiche ai titolari del trattamento e risoluzione | Durata del contratto + 3 anni |
| Registrazioni di autorizzazione per sviluppo/test | Autorizzazioni scritte dei titolari del trattamento per qualsiasi utilizzo di DCP di produzione in ambienti non di produzione | Durata dell'utilizzo + 3 anni |

---

# Considerazioni di audit

Gli auditor che verificano la conformità a CLD-POL-A.4 devono aspettarsi di trovare:

- Registrazioni di pratiche di raccolta documentate per ciascun servizio cloud con categorie di DCP e giustificazioni
- Prove di revisioni annuali delle pratiche di raccolta
- Nessuna categoria di DCP nei sistemi operativi che supera il perimetro del servizio contrattuale
- Qualsiasi evento di DCP in eccesso documentato con notifica al titolare del trattamento e registrazioni di risoluzione
- Nessun DCP di produzione in ambienti di sviluppo o test senza autorizzazione documentata del titolare del trattamento

---

<!-- QA_VERIFIED: 2026-04-04 -->
