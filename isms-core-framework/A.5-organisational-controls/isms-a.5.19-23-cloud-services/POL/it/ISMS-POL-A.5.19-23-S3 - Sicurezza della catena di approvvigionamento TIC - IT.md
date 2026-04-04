<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S3-IT:framework:POL:a.5.19-23-s3 -->
**ISMS-POL-A.5.19-23-S3 — Sicurezza della catena di approvvigionamento TIC**
**Controllo A.5.21: Gestione della sicurezza delle informazioni nella catena di approvvigionamento TIC**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza della catena di approvvigionamento TIC |
| **Tipo di documento** | Sezione di politica |
| **Identificativo del documento** | ISMS-POL-A.5.19-23-S3 |
| **Autore del documento** | Responsabile della Sicurezza delle Informazioni (RSI) |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.5.19-23; ISMS-POL-A.5.19-23-S1; ISMS-POL-A.5.19-23-S2; ISO/IEC 27001:2022 Controllo A.5.21; ISO/IEC 27036-3; NIST SP 800-161

---

# Scopo

La presente sezione definisce i requisiti applicabili alla gestione dei rischi di sicurezza delle informazioni all'interno della catena di approvvigionamento TIC, in particolare i sub-responsabili del trattamento, i fornitori di componenti e le dipendenze software. Affronta il problema del "fornitore del fornitore" e i vettori di attacco specifici della catena di approvvigionamento.

**Principio fondamentale**: La postura di sicurezza dei vostri fornitori dipende dai loro stessi fornitori, che dipendono dai propri. Le violazioni di SolarWinds, Log4Shell e MOVEit illustrano la compromissione della catena di approvvigionamento come effetto moltiplicatore: una singola backdoor in un componente ampiamente utilizzato concede agli attaccanti l'accesso a migliaia di organizzazioni a valle. Questa politica richiede visibilità sistematica, propagazione dei requisiti di sicurezza e monitoraggio continuo lungo l'intera catena di approvvigionamento TIC multi-livello.

**ISO/IEC 27001:2022 Allegato A.5.21**

> *Devono essere definiti e concordati con i fornitori processi e procedure per gestire i rischi di sicurezza delle informazioni associati alla catena di approvvigionamento di prodotti e servizi TIC.*

---

# Perimetro

## Elementi della catena di approvvigionamento

| Elemento | Descrizione | Esempi |
|----------|-------------|--------|
| **Sub-responsabili del trattamento** | Fornitori ingaggiati dai fornitori principali | Subappaltatori, sub-responsabili del trattamento dei dati |
| **Parti di quarto livello** | Fornitori dei sub-responsabili | Fornitori di infrastruttura per gli editori SaaS |
| **Componenti software** | Dipendenze di codice e librerie | Pacchetti open source, SDK, API, framework |
| **Componenti hardware** | Componenti fisici dei prodotti TIC | Processori, moduli di memoria, chip di rete, firmware |
| **Dipendenze di servizi** | Servizi richiesti dai servizi principali | Fornitori DNS, reti CDN, gateway di pagamento |
| **Strumenti di sviluppo** | Strumenti utilizzati per costruire o consegnare prodotti | Piattaforme CI/CD, repository di codice, sistemi di build |

## Categorie di rischio della catena di approvvigionamento

| Categoria di rischio | Descrizione | Impatto |
|---------------------|-------------|--------|
| **Rischio di compromissione** | Codice malevolo o backdoor inseriti nella catena di approvvigionamento | Violazione dei dati, compromissione dei sistemi |
| **Rischio di disponibilità** | Interruzione della catena o punto singolo di guasto | Interruzione del servizio, perturbazione operativa |
| **Rischio di integrità** | Modifiche non autorizzate di componenti o servizi | Corruzione dei dati, instabilità dei sistemi |
| **Rischio di conformità** | Violazioni normative tramite la catena (RGPD, DORA, NIS2) | Sanzioni, responsabilità giuridica |
| **Rischio di concentrazione** | Eccessiva dipendenza da un unico fornitore, componente o territorio | Ampio impatto di un singolo guasto, vendor lock-in |
| **Rischio geopolitico** | Catena esposta a giurisdizioni ostili o sotto sanzioni | Accesso ai dati da parte di governi stranieri |

---

# Gestione dei sub-responsabili del trattamento

## Requisiti di visibilità dei sub-responsabili

| Livello fornitore | Requisito di visibilità |
|------------------|------------------------|
| Livello 1 (Critico) | Registro completo per tutte le attività di trattamento dei dati e servizi critici |
| Livello 2 (Alto) | Registro per i servizi significativi o gli accessi ai dati |
| Livello 3 (Medio) | Conoscenza dei sub-responsabili chiave su richiesta |
| Livello 4 (Basso) | Non richiesta |

**Rafforzamento normativo**: Entità DORA: registro completo della sub-esternalizzazione richiesto ai sensi dell'Articolo 30; Entità NIS2: dichiarazione dei sub-responsabili per i servizi critici.

## Requisiti di controllo dei sub-responsabili

**I fornitori principali devono**:

| Requisito | Livello 1 | Livello 2 | Livelli 3-4 |
|-----------|-----------|-----------|------------|
| Notificare [Organizzazione] dei cambiamenti di sub-responsabili | ✓ 30 giorni di anticipo | ✓ Prima dell'ingaggio | — |
| Ottenere l'approvazione scritta per nuovi sub-responsabili | ✓ Richiesta | ✓ Notifica sufficiente | — |
| Trasmettere i requisiti di sicurezza ai sub-responsabili | ✓ In modo identico | ✓ In modo equivalente | — |
| Rimanere pienamente responsabili degli atti dei sub-responsabili | ✓ Richiesto | ✓ Richiesto | ✓ Richiesto |
| Fornire i report di audit dei sub-responsabili su richiesta | ✓ Entro 30 giorni | ✓ Per quanto possibile | — |
| Consentire a [Organizzazione] di opporsi a sub-responsabili specifici | ✓ Periodo di opposizione di 14 giorni | ✓ Opposizione ragionevole | — |

**Motivi di opposizione**: Sub-responsabile stabilito in una giurisdizione ad alto rischio; assenza delle certificazioni richieste; storico di incidenti di sicurezza; rischio di concentrazione; incompatibilità normativa.

---

# Sicurezza della catena di approvvigionamento software

## Rischi legati ai componenti software

| Rischio | Descrizione | Misura di mitigazione |
|---------|-------------|----------------------|
| Dipendenze vulnerabili | CVE noti in librerie, framework o componenti open source | Analisi continua delle vulnerabilità, SCA, applicazione rapida delle patch |
| Pacchetti malevoli | Attacchi di typosquatting, pacchetti legittimi compromessi | Verifica dei pacchetti, validazione delle somme di controllo |
| Software abbandonato | Componenti non mantenuti senza aggiornamenti di sicurezza | Monitoraggio del ciclo di vita, migrazione ad alternative mantenute |
| Compromissione del processo di build | Pipeline di build alterate, CI/CD compromesso | Rafforzamento del CI/CD sicuro, firma del codice, build riproducibili |

## Requisiti applicabili ai fornitori di software (Livelli 1 e 2)

| Requisito | Descrizione |
|-----------|-------------|
| **Nomenclatura software (SBOM)** | Mantenere una SBOM completa per tutti i software distribuiti, incluse le dipendenze |
| **Gestione delle vulnerabilità** | Analisi automatizzate regolari e applicazione rapida delle patch (critico: 14 giorni, alto: 30 giorni) |
| **Ciclo di sviluppo sicuro** | Seguire un SDLC sicuro (OWASP SAMM, Microsoft SDL o equivalente) |
| **Firma del codice** | Firmare digitalmente tutte le versioni e gli aggiornamenti per verificarne integrità e autenticità |
| **Sicurezza dei repository di codice** | AMF, protezione dei branch, registrazione degli audit, analisi dei segreti nei repository |
| **Notifica degli aggiornamenti** | Notificare a [Organizzazione] gli aggiornamenti relativi alla sicurezza entro 24 ore |

**Contenuto della SBOM**: Nome del componente; versione; fonte/repository; licenza (identificatore SPDX); diretto o transitivo; stato dei CVE noti con punteggi CVSS; criticità.

**Norme SBOM**: CycloneDX (OWASP) o SPDX (Linux Foundation), in formato JSON o XML.

---

# Sicurezza della catena di approvvigionamento hardware

## Requisiti di approvvigionamento hardware (Livelli 1 e 2)

| Requisito | Descrizione |
|-----------|-------------|
| Canali autorizzati | Acquisto esclusivamente da distributori autorizzati dal produttore |
| Catena di custodia | Documentazione completa della movimentazione e del trasporto |
| Verifica dell'integrità | Verifica delle guarnizioni antimanomissione, integrità dell'imballaggio, autenticazione dei numeri di serie |
| Verifica del firmware | Validazione delle versioni firmware rispetto al database del produttore, verifica delle firme digitali |
| Configurazione di fabbrica | Hardware consegnato nello stato predefinito di fabbrica |

---

# Mitigazione degli attacchi alla catena di approvvigionamento

## Vettori di attacco comuni

| Vettore | Descrizione | Esempio reale | Misura di mitigazione |
|---------|-------------|--------------|----------------------|
| Aggiornamenti compromessi | Aggiornamenti software malevoli distribuiti tramite canali legittimi | SolarWinds Orion | Verifica della firma del codice, distribuzioni progressive |
| Confusione di dipendenze | Pacchetti malevoli con lo stesso nome in repository pubblici | Attacchi di confusione di dipendenze npm | Configurazione di registro privato |
| Furto di credenziali | Credenziali del fornitore rubate e usate per l'accesso | Violazioni Okta/LastPass | AMF, monitoraggio delle credenziali |
| Minaccia interna | Dipendente o subappaltatore del fornitore malevolo | Esfiltrazione tipo Snowden | Verifiche dei precedenti, controlli degli accessi |

## Controlli di sicurezza della catena di approvvigionamento

| Controllo | Descrizione |
|-----------|-------------|
| Segmentazione di rete dei fornitori | Isolare gli accessi dei fornitori in segmenti dedicati, senza movimento laterale verso la produzione |
| Gestione degli accessi privilegiati | Richiedere PAM per tutti gli accessi amministrativi dei fornitori |
| Monitoraggio continuo | Registrare e allertare sulle attività dei fornitori, analisi comportamentale |
| Verifica dell'integrità | Verificare somme di controllo e firme per aggiornamenti e comunicazioni dei fornitori |
| Risposta agli incidenti | Integrare gli scenari di compromissione della catena di approvvigionamento nei piani di risposta |

---

# Monitoraggio e revisione

## Metriche e KPI della catena di approvvigionamento

| Metrica | Obiettivo | Metodo di misurazione |
|---------|-----------|----------------------|
| Visibilità dei sub-responsabili (Livello 1) | 100% documentati | Audit di completezza del registro |
| Dipendenze critiche identificate | 100% documentate | Completezza dell'inventario delle dipendenze |
| Copertura SBOM (software critici) | 100% disponibili, aggiornate ogni 90 giorni | Raccolta e validazione delle SBOM |
| Dipendenze vulnerabili | 0 critiche, < 5 alte | Risultati degli strumenti SCA |
| Incidenti della catena di approvvigionamento | Monitorare i trend, ACR per tutti | Sistema di gestione degli incidenti |
| Tasso di certificazione dei sub-responsabili (N1) | > 90% ISO 27001 o SOC 2 | Monitoraggio delle certificazioni |

---

# Requisiti normativi

## Sub-esternalizzazione DORA (Articolo 30)

Per i servizi TIC rientranti in DORA, mantenere un registro completo di sub-esternalizzazione includente: tutti gli accordi di sub-esternalizzazione a cascata conclusi dai fornitori terzi di servizi TIC; natura delle funzioni sub-esternalizzate; giurisdizioni in cui avviene la sub-esternalizzazione; data dei contratti di sub-esternalizzazione; notifica preventiva a [Organizzazione] prima di qualsiasi sub-esternalizzazione.

## Sub-esternalizzazione FINMA (Circolare 2023/1)

Per le banche svizzere soggette alla Circolare FINMA 2023/1: registro completo di tutti gli accordi di sub-esternalizzazione a cascata; approvazione preventiva della banca prima di qualsiasi sub-esternalizzazione materiale; valutazione del rischio; trasmissione contrattuale dei requisiti; diritti di audit estesi ai sub-esternalizzatori.

## Sicurezza della catena di approvvigionamento NIS2 (Articolo 21)

Per le entità coperte da NIS2: politiche relative all'acquisizione, sviluppo e manutenzione dei sistemi TIC; requisiti di sicurezza per le relazioni con i fornitori; notifica degli incidenti da parte dei fornitori per consentire la segnalazione normativa entro 24 ore; valutazione del rischio della catena di approvvigionamento.

---

*«La vostra sicurezza è forte quanto il vostro fornitore più debole... del vostro fornitore più debole.»*

<!-- QA_VERIFIED: 2026-04-03 -->
