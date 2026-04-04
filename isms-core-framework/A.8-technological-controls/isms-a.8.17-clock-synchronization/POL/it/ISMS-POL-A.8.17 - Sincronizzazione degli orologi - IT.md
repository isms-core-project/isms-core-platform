<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.17-IT:framework:POL:a.8.17 -->
**ISMS-POL-A.8.17 — Sincronizzazione degli orologi**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sincronizzazione degli orologi |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.17 |
| **Autore del documento** | RSSI |
| **Proprietario del documento** | AD |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DSI → Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.17.1–3-UG/TG; ISMS-POL-A.8.15 (Registrazione); ISMS-POL-A.8.16 (Monitoraggio); ISO/IEC 27001:2022 Controllo A.8.17.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la sincronizzazione degli orologi su tutti i sistemi di elaborazione delle informazioni per consentire la correlazione dei log, l'analisi forense e le piste di audit affidabili, conformemente al Controllo A.8.17 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutti i sistemi di elaborazione delle informazioni che generano log o partecipano a operazioni di sicurezza rilevanti, inclusi server, dispositivi di rete, sistemi di sicurezza e istanze cloud.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Controllo ISO/IEC 27001:2022 A.8.17

> *Gli orologi dei sistemi di elaborazione delle informazioni che utilizzano [Organizzazione] devono essere sincronizzati con fonti temporali di riferimento approvate.*

**Obiettivo del controllo**: Garantire che tutti i sistemi di elaborazione delle informazioni abbiano orologi accurati e sincronizzati per consentire la correlazione affidabile dei log di sicurezza, la ricostruzione degli incidenti, la risposta agli incidenti e la conformità normativa.

**Motivazione critica**: La deriva degli orologi non sincronizzati degrada la qualità dei log e può invalidare le prove forensi. La correlazione degli eventi su sistemi con orologi non sincronizzati è inaffidabile e può ostacolare le indagini sugli incidenti.

---

# Enunciati di politica

## Standard dell'ora di riferimento

[Organizzazione] DEVE utilizzare il Tempo Coordinato Universale (UTC) come fuso orario standard per tutti i sistemi che elaborano le informazioni.

**Gerarchia delle sorgenti NTP**: [Organizzazione] DEVE mantenere almeno due server NTP interni Stratum 2 sincronizzati con più sorgenti di riferimento temporale externe affidabili.

**Sorgenti NTP accettabili**: pool.ntp.org (pool pubblico NTP); fornitori cloud (AWS Time Sync, Azure NTP, Google Public NTP); istituti nazionali di standardizzazione del tempo (NIST, PTB); sorgenti GPS.

**Requisiti ridondanza**: Minimo due sorgenti NTP distinte per i server NTP interni; percorsi di rete indipendenti verso le sorgenti NTP esterne.

## Requisiti di precisione

| Tipo di sistema | Precisione massima consentita | Metodo di sincronizzazione |
|----------------|------------------------------|---------------------------|
| Sistemi critici (SIEM, PAM, sistemi di autenticazione) | ≤50 ms dalla fonte | NTP Stratum 2 internamente |
| Sistemi standard (server, applicazioni) | ≤500 ms | NTP Stratum 3 internamente |
| Endpoint (laptop, desktop) | ≤1 secondo | NTP via AD/LDAP o client NTP |
| Istanze cloud | ≤100 ms | Servizi NTP del provider cloud |
| Dispositivi di rete (firewall, switch, router) | ≤500 ms | NTP Stratum 3 internamente |

## Monitoraggio della sincronizzazione

[Organizzazione] DEVE monitorare la conformità alla sincronizzazione degli orologi.

**Verifica automatizzata**: Verifica giornaliera della sincronizzazione degli orologi su tutti i sistemi di produzione; avvisi automatici per deriva dell'orologio superiore alle soglie; monitoraggio della disponibilità del server NTP; rilevamento dei tentativi di manipolazione dell'ora del sistema.

**Soglie di avviso**:

| Gravità | Condizione | Azione |
|---------|------------|--------|
| **Critico** | Deriva >1 secondo su sistemi critici | Rimedio immediato + notifica al RSSI |
| **Alto** | Deriva >500 ms su qualsiasi sistema di produzione | Rimedio entro 4 ore |
| **Medio** | Server NTP non raggiungibile | Rimedio entro 24 ore |
| **Basso** | Deriva 100-500 ms | Rimedio entro 48 ore |

**Frequenza di verifica**: Copertura di verifica della sincronizzazione al 100% dei sistemi di produzione (giornaliera); revisione delle tendenze della deriva (mensile); audit completo della conformità NTP (trimestrale).

## Sicurezza del servizio NTP

**Protezione dei server NTP interni**: L'accesso ai server NTP interni DEVE essere limitato ai sistemi autorizzati; le richieste NTP provenienti da fonti non autorizzate DEVONO essere bloccate a livello di firewall; i log del server NTP DEVONO essere raccolti e monitorati per rilevare anomalie.

**Protezione dei client NTP**: I sistemi DEVONO utilizzare solo server NTP approvati; le modifiche manuali dell'ora del sistema DEVONO essere registrate e avvisate; l'autenticazione NTP (NTPsec o autenticazione MD5) DEVE essere implementata dove tecnicamente fattibile.

## Gestione delle eccezioni

**Sistemi non in grado di sincronizzarsi con NTP**: Sistemi air-gapped o reti isolate; apparecchiature legacy senza supporto NTP. **Requisiti di eccezione**: Procedura documentata di sincronizzazione dell'orologio manuale (almeno ogni 24 ore per i sistemi critici); avvisi automatici per derive; approvazione del RSSI richiesta; revisione semestrale dell'eccezione.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approva le eccezioni e la selezione delle sorgenti temporali |
| **Operazioni IT** | Distribuzione e manutenzione dei server NTP; configurazione dei client su tutti i sistemi |
| **SOC** | Monitoraggio degli avvisi di deriva degli orologi; indagine sulle anomalie di sincronizzazione |
| **Proprietari dei sistemi** | Garantire che i sistemi di proprietà siano configurati con NTP |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce i requisiti per la sincronizzazione degli orologi. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.17 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
