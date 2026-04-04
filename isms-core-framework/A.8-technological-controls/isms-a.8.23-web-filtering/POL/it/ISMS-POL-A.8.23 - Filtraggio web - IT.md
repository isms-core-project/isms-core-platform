<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.23-IT:framework:POL:a.8.23 -->
**ISMS-POL-A.8.23 — Filtraggio web**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Filtraggio web |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.23 |
| **Autore del documento** | RSSI |
| **Proprietario del documento** | AD |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DSI → Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.23.1–3-UG/TG; ISO/IEC 27001:2022 Controllo A.8.23.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per i controlli di filtraggio web per proteggere gli utenti e le informazioni organizzative dalle minacce basate sul web, conformemente al Controllo A.8.23 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutti i segmenti di rete dove gli utenti accedono alle risorse Internet, a tutto il personale organizzativo e a tutte le tecnologie di filtraggio web indipendentemente dal modello di dispiegamento.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Controllo ISO/IEC 27001:2022 A.8.23

> *L'accesso ai siti web esterni deve essere gestito per ridurre l'esposizione a contenuti dannosi.*

**Obiettivo del controllo**: Proteggere gli utenti e le informazioni organizzative riducendo l'esposizione a contenuti web dannosi, malware distribuito via web e categorie di contenuto inappropriate.

---

# Enunciati di politica

## Requisiti dell'infrastruttura di filtraggio web

[Organizzazione] DEVE implementare il filtraggio web per tutti i segmenti di rete dove gli utenti accedono a Internet.

**Funzionalità obbligatorie del filtraggio web**: Filtraggio per categoria di URL (blocca le categorie dannose/inappropriate); reputazione degli URL e intelligence sulle minacce in tempo reale; ispezione SSL/TLS per il traffico HTTPS (con avvisi appropriati sulla privacy); filtraggio del DNS come livello di difesa aggiuntivo; prevenzione della perdita di dati via web (integrazione DLP).

**Copertura**: ≥95% di tutto il traffico internet degli utenti DEVE passare attraverso i controlli di filtraggio web; gli utenti remoti/VPN DEVONO essere soggetti allo stesso filtraggio degli utenti in sede.

## Categorie bloccate (blocco predefinito)

Le seguenti categorie DEVONO essere bloccate per impostazione predefinita per tutti gli utenti:

**Minacce alla sicurezza**: Siti di phishing; distribuzione di malware; botnet e server C2; siti di exploit; download drive-by; VPN anonimizzanti (che aggirano il filtraggio).

**Categorie di contenuto vietate**: Contenuto illegale (CSAM, attività illegale); contenuto per adulti su dispositivi aziendali; hacking/cracking/strumenti di sicurezza offensiva (tranne per il personale di sicurezza autorizzato); contenuto di odio/violento/estremista.

**Categorie di alto rischio** (bloccate per impostazione predefinita, sbloccabili con approvazione): Siti di condivisione di file/torrenting; siti di giochi d'azzardo; applicazioni di comunicazione consumer non approvate; mercati di criptovalute/dark web.

## Categorie consentite e personalizzazione

**Consentite per tutti gli utenti**: Notizie, ricerca, istruzione; servizi cloud approvati; strumenti di produttività aziendali; social media (limitato durante le ore lavorative, a discrezione della politica).

**Personalizzazione basata sul ruolo**: I ruoli con requisiti aziendali legittimi POSSONO richiedere l'accesso a categorie aggiuntive; le eccezioni DEVONO essere approvate dal responsabile del team e dal RSSI; le eccezioni DEVONO essere revisionate trimestralmente; le eccezioni DEVONO essere registrate per finalità di audit.

## Risposta agli incidenti di filtraggio web

**Avvisi automatici**: Il personale di sicurezza DEVE essere avvisato per: tentativi di accesso a malware noto/siti C2; volume elevato di siti bloccati da un singolo utente; tentativi di aggirare il filtraggio; accessi a categorie ad alto rischio non bloccate. **Risposta**: I tentativi di accesso a malware noto DEVONO innescare la revisione degli endpoint (per ISMS-POL-A.8.1-7-18-19); i tentativi ripetuti di aggirare il filtraggio DEVONO essere segnalati al responsabile e all'HR.

## Privacy e trasparenza

[Organizzazione] DEVE informare i dipendenti del filtraggio web: avviso relativo alla privacy che descrive le funzionalità di filtraggio; notifica agli utenti che i log di accesso web vengono registrati; esclusione dei siti personali sensibili dove tecnicamente fattibile; nessun monitoraggio degli accessi web al di fuori delle funzionalità della soluzione di sicurezza.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approvazione delle modifiche alle categorie bloccate; revisione delle eccezioni |
| **Operazioni IT** | Implementazione e manutenzione dell'infrastruttura di filtraggio web |
| **SOC** | Monitoraggio degli avvisi; risposta agli incidenti di sicurezza basati su web |
| **HR/Manager** | Comunicazione della politica; escalation delle violazioni |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce i requisiti per il filtraggio web. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.23 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
