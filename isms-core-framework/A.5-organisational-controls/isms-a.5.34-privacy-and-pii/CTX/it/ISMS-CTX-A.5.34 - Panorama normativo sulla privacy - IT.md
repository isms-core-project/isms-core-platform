<!-- ISMS-CORE:CTX:ISMS-CTX-A.5.34-IT-privacy-regulatory-landscape:framework:CTX:a.5.34 -->
**ISMS-CTX-A.5.34 — Riferimento al panorama normativo sulla privacy**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento al panorama normativo sulla privacy |
| **Tipo di documento** | Documento di contesto (materiale di supporto non vincolante) |
| **Identificativo del documento** | ISMS-CTX-A.5.34 |
| **Autore del documento** | Responsabile della protezione dei dati (RPD) / Team legale |
| **Proprietario del documento** | Responsabile della protezione dei dati (RPD) |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Documenti correlati**: ISMS-POL-A.5.34 (Politica principale), ISMS-POL-00 (Quadro di applicabilità normativa), ISMS-IMP-A.5.34 (Suite di guida all'implementazione)

---

## CRITICO: Posizionamento e limitazioni del documento

### Questo documento NON fa parte del SGSI

**Classificazione**: Si tratta di un **documento di supporto** che fornisce informazioni contestuali sulle normative sulla privacy. **NON** fa parte dell'ambito di certificazione ISO/IEC 27001:2022 e **NON** è soggetto ai requisiti di audit del SGSI.

**Cosa è questo documento**: Risorsa educativa per i membri del team della privacy; sensibilizzazione al panorama normativo per i team tecnici; materiale di riferimento per la comprensione del contesto RGPD/LPD.

**Cosa NON è questo documento**:

- ❌ NON un requisito di conformità
- ❌ NON parte della documentazione obbligatoria del SGSI
- ❌ NON soggetto all'audit di certificazione ISO 27001:2022
- ❌ NON una consulenza legale (consultare un consulente legale qualificato)
- ❌ NON un sostituto dei requisiti della politica ISMS-POL-A.5.34

**Nota per i revisori**: La presenza o assenza di questo documento e il suo contenuto **non hanno alcun impatto** sulla conformità al Controllo A.5.34 della ISO/IEC 27001:2022. Tutti i requisiti di conformità sono definiti esclusivamente in ISMS-POL-A.5.34.

---

# Scopo e ambito del documento

## Scopo

Questo documento di supporto fornisce informazioni contestuali sulle normative sulla privacy (RGPD, LPD) per aiutare il personale di [Organizzazione] a comprendere il panorama normativo nell'implementazione dei controlli sulla privacy ai sensi del Controllo A.5.34 della ISO/IEC 27001:2022.

**Pubblico destinatario**: Responsabili della protezione dei dati / Responsabili della privacy; Responsabili legali / di conformità; CISO e team di sicurezza; Proprietari di sistemi e sviluppatori; Team di gestione dei fornitori; Sviluppatori di materiali di formazione.

## Panoramica dei contenuti

**Sezione 2**: RGPD — Analisi approfondita (ambito territoriale, principi, basi giuridiche, categorie speciali, sanzioni)

**Sezione 3**: LPD svizzera (nLPD) — Analisi approfondita (requisiti specifici svizzeri, differenze dalla LPD precedente, approccio di applicazione)

**Sezione 4**: Analisi comparativa RGPD vs. LPD (principali somiglianze e differenze, strategie di doppia conformità)

**Sezione 5**: Meccanismi internazionali di trasferimento dei dati (decisioni di adeguatezza, clausole contrattuali standard, Schrems II)

**Sezione 6**: Framework e standard sulla privacy (ISO/IEC 27701:2019, NIST Privacy Framework, principi OCSE)

**Sezione 7**: Panorama di applicazione (azioni di applicazione notevoli, lezioni apprese)

## Limitazioni e avvertenze

**Avvertenza legale**: Questo documento fornisce informazioni generali e NON costituisce consulenza legale. Le organizzazioni devono consultare un consulente legale qualificato per l'interpretazione legale.

**Aggiornamento**: Le normative sulla privacy e gli orientamenti delle autorità di vigilanza evolvono rapidamente. Consultare sempre le fonti ufficiali (EDPB, GPDP/RPD, testi normativi ufficiali) e un consulente legale qualificato.

---

# RGPD (Regolamento generale sulla protezione dei dati) — Contesto dettagliato

## Panoramica e applicabilità del RGPD

**Regolamento (UE) 2016/679**

**Adozione**: 27 aprile 2016 | **Data di efficacia**: 25 maggio 2018 | **Ambito geografico**: Unione europea (27 Stati membri) + Spazio economico europeo (Islanda, Liechtenstein, Norvegia). Il RGPD del Regno Unito è sostanzialmente simile post-Brexit.

**Natura legislativa**: Regolamento (direttamente applicabile in tutti gli Stati membri senza legislazione di attuazione nazionale).

**Applicazione**: Decentrata attraverso le Autorità di protezione dei dati (APD) di ciascuno Stato membro, coordinate dall'European Data Protection Board (EDPB).

**Principali APD** (esempi): Germania (BfDI + 16 autorità dei Länder), Francia (CNIL), Irlanda (DPC — supervisiona molte operazioni UE di aziende tecnologiche statunitensi), Paesi Bassi (AP), Spagna (AEPD), Italia (Garante per la protezione dei dati personali), Belgio (APD/GBA).

---

## Ambito territoriale del RGPD (Articolo 3)

**Quando si applica il RGPD?**

**Criterio 1: Stabilimento** (Articolo 3(1))

Il RGPD si applica al trattamento di dati personali **nel contesto delle attività di uno stabilimento** del titolare o del responsabile del trattamento nell'UE, **indipendentemente dal luogo in cui avviene il trattamento**.

**"Stabilimento"** (interpretazione CGUE): Esercizio effettivo e reale di un'attività tramite **accordi stabili**; forma giuridica irrilevante (filiale, sussidiaria, ufficio, rappresentante); il potere decisionale non è richiesto.

**Esempi**:
- ✅ Filiale UE di società madre extra-UE che tratta dati dei dipendenti → si applica il RGPD
- ✅ Società extra-UE con ufficio vendite UE (anche se i dati vengono trattati negli USA) → si applica il RGPD
- ❌ Società extra-UE con solo sito web passivo accessibile nell'UE → il RGPD non si applica (a meno che non sia soddisfatto il Criterio 2)

---

**Criterio 2: Targeting** (Articolo 3(2))

Il RGPD si applica al trattamento di dati personali di **interessati che si trovano nell'UE** da parte di titolari o responsabili **non stabiliti nell'UE**, quando le attività di trattamento riguardano:

**(a) L'offerta di beni o servizi** (a prescindere dalla richiesta di pagamento) **agli interessati nell'UE**

**Indicatori di "offerta"** (Linee guida EDPB 3/2018):
- ✅ Sito web disponibile in una o più lingue UE (diverse dalla lingua del paese del commerciante)
- ✅ Possibilità di ordinare beni/servizi in tale lingua
- ✅ Menzione di clienti o utenti nell'UE
- ✅ Domini nazionali UE (.de, .fr, .it)
- ✅ Marketing o pubblicità specifici per l'UE
- ✅ Prezzi in EUR o altre valute UE
- ❌ La semplice accessibilità al sito web nell'UE non è sufficiente (deve dimostrare l'intenzione di offrire agli interessati dell'UE)
- ❌ Un sito web solo in inglese non è sufficiente (l'inglese è la lingua internazionale degli affari)

**(b) Il monitoraggio del comportamento** degli interessati **che si svolge nell'UE**

**"Monitoraggio"** (interpretazione EDPB): Tracciamento di individui su internet (cookie, fingerprinting del dispositivo, pubblicità comportamentale); tracciamento della posizione nell'UE; profilazione degli interessati nell'UE per analizzare o prevedere il comportamento.

---

**Articolo 3(3) — Requisito di rappresentante**

I titolari o responsabili non stabiliti nell'UE ma soggetti al RGPD ai sensi dell'Art. 3(2) **devono designare un rappresentante nell'UE** (a meno che il trattamento non sia occasionale, a basso rischio, escluda categorie speciali o sia effettuato da un'autorità pubblica).

---

## Principi fondamentali del RGPD (Articolo 5)

**Articolo 5 — Principi applicabili al trattamento dei dati personali**

Questi principi sono **obblighi fondamentali** applicabili a tutto il trattamento. Le violazioni possono comportare sanzioni fino a 20 milioni di euro o il 4% del fatturato annuo globale.

**Principio 1: Liceità, correttezza e trasparenza** (Art. 5(1)(a))

**Liceità**: Il trattamento deve avere una base giuridica ai sensi dell'Articolo 6 (o Art. 9 per le categorie speciali). Non è possibile trattare senza una base giuridica valida.

**Correttezza**: Il trattamento non deve essere fuorviante, manipolativo o ingannevole. I dark pattern sono vietati (design dell'interfaccia fuorviante che inganna gli utenti nelle loro decisioni).

**Trasparenza**: Le informazioni devono essere fornite agli interessati (Art. 12-14). Le comunicazioni devono essere concise, trasparenti, intelligibili, facilmente accessibili, chiare e in linguaggio semplice.

---

**Principio 2: Limitazione della finalità** (Art. 5(1)(b))

I dati personali devono essere **raccolti per finalità determinate, esplicite e legittime** e non ulteriormente trattati in modo **incompatibile con tali finalità**.

**"Determinate, esplicite, legittime"**: Finalità chiaramente identificate e articolate; espressamente comunicate agli interessati; conformi alla legge.

**Trattamento compatibile** (Art. 6(4)): Fattori da considerare — collegamento tra le finalità, contesto della raccolta, natura dei dati, conseguenze per gli interessati, garanzie.

**Esempi**:
- ✅ **Compatibile**: Dati raccolti per l'evasione degli ordini dei clienti → Utilizzo per la prevenzione delle frodi
- ❌ **Incompatibile**: Dati raccolti per il reclutamento → Utilizzo per il marketing di prodotti non correlati

---

**Principio 3: Minimizzazione dei dati** (Art. 5(1)(c))

I dati personali devono essere **adeguati, pertinenti e limitati a quanto necessario** rispetto alle finalità per le quali sono trattati.

**Applicazione pratica**:
- Progettare i sistemi per raccogliere il minimo di dati necessari
- Porsi la domanda per ogni campo dati: ne abbiamo davvero bisogno?
- Evitare la raccolta di dati "comodo avere" — raccogliere solo quelli "necessari"
- Rivedere periodicamente la raccolta dei dati ed eliminare i campi non necessari

**Esempi**:
- ❌ Iscrizione newsletter che richiede: nome, email, telefono, indirizzo, data di nascita, professione → **Eccessivo** (l'email è sufficiente per la newsletter)
- ✅ Iscrizione newsletter che richiede: solo email → **Proporzionato**

---

**Principio 4: Esattezza** (Art. 5(1)(d))

I dati personali devono essere **esatti** e, se necessario, **aggiornati**. I dati inesatti devono essere **cancellati o rettificati senza indugio**.

**Obbligo proattivo**: Non solo reattivo (rispondere alle richieste di rettifica); il titolare deve adottare **misure ragionevoli** per garantire l'esattezza.

**Misure pratiche**: Validazione al momento dell'immissione dei dati; audit periodici della qualità dei dati; consentire agli interessati di aggiornare i propri dati (portali self-service); campagne periodiche per verificare l'accuratezza dei dati.

---

**Principio 5: Limitazione della conservazione** (Art. 5(1)(e))

I dati personali devono essere **conservati in una forma che consenta l'identificazione degli interessati per un arco di tempo non superiore a quello necessario** alle finalità per le quali sono trattati.

**Giustificazioni della conservazione**: Obbligo legale (periodi di conservazione legali); contratto (dati necessari per la relazione contrattuale in corso); pretese legali (periodo ragionevole per il periodo di prescrizione); interesse legittimo (giustificazione aziendale forte + valutazione di necessità).

**Approccio pratico**: Schedari di conservazione; cancellazione automatica; archiviazione con accesso limitato vs. archiviazione operativa online; anonimizzazione quando non è più necessaria l'identificazione.

**Esempi di periodi di conservazione**: Dati sulle transazioni dei clienti: 7-10 anni (conformità fiscale); opt-in marketing: fino alla revoca del consenso + periodo ragionevole; dati sui candidati: 6-12 mesi dopo il rifiuto; filmati CCTV: 30-90 giorni.

---

**Principio 6: Integrità e riservatezza** (Art. 5(1)(f))

I dati personali devono essere **trattati in maniera da garantire un'adeguata sicurezza**, compresa la protezione contro:
- Il trattamento non autorizzato o illecito (riservatezza)
- La perdita, la distruzione o il danno accidentali (disponibilità, integrità)

Mediante adeguate **misure tecniche o organizzative**.

**Integrazione con la sicurezza delle informazioni**: I requisiti di sicurezza del RGPD sono allineati con le migliori pratiche di sicurezza delle informazioni. I controlli ISO/IEC 27001/27002 supportano la conformità alla sicurezza del RGPD.

---

**Principio 7: Responsabilizzazione** (Art. 5(2))

Il titolare è **responsabile** e deve essere in grado di **dimostrare il rispetto** dei principi 1-6.

**Misure di responsabilizzazione**: Politiche e procedure documentate; Registro delle attività di trattamento (RAT) (Art. 30); Valutazioni d'impatto sulla protezione dei dati (DPIA) (Art. 35); accordi con il responsabile (Art. 28); Valutazioni degli interessi legittimi (VIL); registri del consenso; registri di formazione; rapporti di audit; registri delle violazioni dei dati; registri delle richieste di esercizio dei diritti degli interessati.

**Implicazione pratica**: "Facciamo bene la privacy" è insufficiente. Bisogna mostrare le prove: "Ecco le nostre politiche, procedure, registri di formazione, rapporti di audit, che dimostrano la conformità."

---

## Basi giuridiche del RGPD — Interpretazione pratica

**Concetto critico**: Il trattamento è **illecito** senza una base giuridica valida. L'Articolo 6 è il **punto di partenza obbligatorio** per tutto il trattamento.

**Articolo 6(1) — Sei basi giuridiche**

I titolari devono identificare UNA base giuridica (non si possono combinare per la stessa finalità). La scelta della base giuridica ha conseguenze: il **consenso** può essere revocato, si applica il diritto alla portabilità; il **contratto** non consente obiezione (ma si applica il diritto alla portabilità); l'**interesse legittimo** consente obiezione, è richiesta una valutazione.

---

**Base giuridica 1: Consenso** (Art. 6(1)(a))

**Quando usarla**: Trattamento facoltativo; marketing diretto; cookie non essenziali; ricerca; condivisione dei dati con soggetti non responsabili.

**Vantaggi**: Dimostra chiaramente il controllo dell'interessato; appropriato per funzionalità facoltative.

**Svantaggi**: Può essere revocato in qualsiasi momento; standard più elevato per la validità (liberamente prestato, specifico, informato, inequivocabile); squilibri di potere problematici (il consenso del dipendente è discutibile); onere amministrativo.

**Errori comuni**:
- ❌ Utilizzo del consenso per i dati dei dipendenti (squilibrio di potere)
- ❌ Rendere il consenso condizionale al servizio
- ❌ Caselle pre-spuntate (non è un'indicazione inequivocabile)
- ❌ Consenso raggruppato (più finalità in un unico consenso)
- ❌ Nascosto nelle condizioni generali

---

**Base giuridica 2: Contratto** (Art. 6(1)(b))

**Quando usarla**: Trattamento necessario per **eseguire un contratto** con l'interessato; trattamento necessario per **adottare misure precontrattuali** su richiesta dell'interessato.

**"Necessario" = Oggettivamente necessario**: Il contratto sarebbe impossibile o privo di significato senza il trattamento? L'EDPB adotta un'interpretazione rigorosa: veramente necessario per l'esecuzione del contratto.

**Esempi**:
- ✅ **Necessario**: Nome/indirizzo del cliente per la consegna del prodotto
- ✅ **Necessario**: Coordinate bancarie del dipendente per il pagamento dello stipendio
- ❌ **Non necessario**: Cronologia di navigazione del cliente per la consegna del prodotto (usare interesse legittimo o consenso)
- ❌ **Non necessario**: Email marketing ai clienti (usare consenso)

---

**Base giuridica 3: Obbligo legale** (Art. 6(1)(c))

**Quando usarla**: Trattamento richiesto dalla legislazione UE o degli Stati membri; un obbligo legale specifico si applica al titolare.

**Esempi**: Reporting fiscale; conformità AML/KYC; conformità al diritto del lavoro; requisiti contabili legali; adempimento di ordinanze del tribunale.

**Requisiti**: L'obbligo legale deve essere **specifico** (non solo "buona pratica"); deve citare la specifica disposizione legale.

---

**Base giuridica 4: Interessi vitali** (Art. 6(1)(d))

**Quando usarla**: Emergenza di vita o di morte; proteggere gli interessi vitali dell'interessato o di un'altra persona; ultima risorsa (quando non è disponibile un'altra base giuridica).

**Applicazione rara**: Emergenza medica; risposta a catastrofi naturali; operazioni di ricerca e salvataggio; emergenze di protezione dell'infanzia.

**"Vitali" significa vita o morte**, non "molto importante per l'azienda."

---

**Base giuridica 5: Compito di interesse pubblico** (Art. 6(1)(e))

**Quando usarla**: Autorità pubblica che svolge un compito di interesse pubblico; autorità pubblica che esercita pubblici poteri.

**Applicabilità**: Principalmente per enti governativi, organismi pubblici. In genere **non applicabile** al settore privato. Il compito di interesse pubblico deve essere stabilito dalla legge UE o degli Stati membri.

---

**Base giuridica 6: Interesse legittimo** (Art. 6(1)(f))

**Quando usarla**: Trattamento necessario per gli interessi legittimi del titolare o di terzi; interessi non prevalenti sugli interessi/diritti/libertà dell'interessato; base più flessibile (ma richiede giustificazione).

**Test in tre parti**:
1. **Test delle finalità**: Esiste un interesse legittimo?
2. **Test di necessità**: Il trattamento è necessario per tale interesse?
3. **Test di bilanciamento**: L'interesse legittimo prevale sui diritti dell'interessato?

**Interessi legittimi comuni**:
- ✅ Prevenzione e rilevamento delle frodi
- ✅ Sicurezza delle reti e delle informazioni
- ✅ Marketing diretto ai clienti esistenti (contesto B2B)
- ✅ Amministrazione interna e report gestionali
- ✅ Due diligence per fusioni e acquisizioni
- ✅ Difesa di pretese legali
- ✅ CCTV per la sicurezza dei locali

**Non applicabile quando**: L'interessato chiaramente non se lo aspetterebbe (il fattore sorpresa fa fallire il test di bilanciamento); categorie speciali di dati (Art. 9); autorità pubbliche che svolgono compiti pubblici.

---

## Dati di categorie speciali del RGPD (Articolo 9)

**Articolo 9(1) — Divieto generale**: Il trattamento dei dati di categorie speciali è **vietato** salvo una delle eccezioni dell'Articolo 9(2).

**Categorie speciali** (Art. 9(1)): Origine razziale o etnica; opinioni politiche; credenze religiose o filosofiche; appartenenza sindacale; dati genetici; dati biometrici per l'identificazione univoca; dati relativi alla salute; dati relativi alla vita sessuale o all'orientamento sessuale.

**Requisito in due fasi**:
1. Deve esistere una base giuridica ai sensi dell'Articolo 6
2. **E** deve esistere una condizione specifica dell'Articolo 9(2) (eccezione al divieto)

**Principali eccezioni all'Articolo 9(2)**:

**(a) Consenso esplicito**: Standard più elevato rispetto al consenso standard dell'Art. 6(1)(a); deve essere una dichiarazione espressa (non dedotta da azioni).

**(b) Lavoro, sicurezza sociale, protezione sociale**: Necessario per adempiere obblighi/diritti del titolare/interessato; deve essere autorizzato dalla legge UE/degli Stati membri.

**(c) Interessi vitali (quando l'interessato è incapace)**: Emergenze mediche in cui il paziente è incosciente o altrimenti incapace di prestare il consenso.

**(f) Pretese legali**: Necessario per l'accertamento, l'esercizio o la difesa di pretese in giudizio.

**(h) Assistenza sanitaria o sociale**: Necessario per medicina preventiva o del lavoro, diagnosi medica, erogazione di cure sanitarie o sociali; professionista soggetto a obbligo di segretezza.

**(j) Archiviazione, ricerca, statistiche**: Necessario per archiviazione di interesse pubblico, ricerca scientifica/storica, fini statistici; con adeguate garanzie (misure tecniche/organizzative).

**Implicazioni pratiche**: I dati di categorie speciali richiedono misure di sicurezza rafforzate, controlli di accesso più rigorosi, DPIA obbligatoria per il trattamento su larga scala (Art. 35(3)(b)).

---

## Sanzioni e applicazione del RGPD

**Struttura delle sanzioni a due livelli** (Art. 83):

**Livello 1** (violazioni minori) — **Fino a 10 milioni di euro o 2% del fatturato annuo globale** (il maggiore dei due): Violazioni degli obblighi del titolare/responsabile (Art. 8, 11, 25-39, 42-43).

**Livello 2** (violazioni gravi) — **Fino a 20 milioni di euro o 4% del fatturato annuo globale** (il maggiore dei due): Violazioni dei principi fondamentali (Art. 5, 6, 7, 9); violazioni dei diritti degli interessati (Art. 12-22); violazioni delle restrizioni ai trasferimenti (Art. 44-49); inosservanza degli ordini dell'autorità di vigilanza (Art. 58).

**Fattori che incidono sull'importo della sanzione** (Art. 83(2)): Natura, gravità, durata della violazione; carattere intenzionale o colposo; misure adottate per attenuare il danno; grado di responsabilità; infrazioni precedenti; grado di cooperazione con l'autorità di vigilanza; categorie di dati personali interessate; come è diventata nota l'infrazione (auto-segnalata vs. scoperta).

**Esempi notevoli**: Amazon (Lussemburgo, 2021): 746 milioni di euro — violazioni dei principi; Meta/Facebook (Irlanda, 2023): 1,2 miliardi di euro — trasferimenti illeciti di dati verso gli USA; Google (CNIL Francia, 2019): 50 milioni di euro — consenso inadeguato per la pubblicità personalizzata; H&M (Amburgo, 2020): 35,3 milioni di euro — sorveglianza eccessiva dei dipendenti; British Airways (ICO UK, 2020): 20 milioni di sterline — violazione dei dati, sicurezza inadeguata.

---

# LPD svizzera (nLPD) — Contesto dettagliato

## Panoramica della LPD (nDSG riveduta)

**Legge federale sulla protezione dei dati (RS 235.1)**

**Legge precedente**: Legge federale del 19 giugno 1992 sulla protezione dei dati (vecchia LPD) | **Nuova legge**: Legge federale del 25 settembre 2020 sulla protezione dei dati (LPD riveduta / nLPD) | **Data di entrata in vigore**: 01 settembre 2023 | **Applicazione**: Incaricato federale della protezione dei dati e della trasparenza (IFPDT / Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter, EDÖB)

**Scopo della revisione**: Allineare la legge svizzera con il RGPD UE (facilitare il flusso di dati tra Svizzera e UE), modernizzare per l'era digitale, rafforzare i diritti degli interessati.

**Relazione Svizzera-UE**: La Svizzera NON è nell'UE o nel SEE ma ha una decisione di adeguatezza da parte dell'UE (riconosciuta come in grado di garantire un'adeguata protezione dei dati). La LPD riveduta era necessaria per mantenere lo status di adeguatezza post-RGPD.

---

## Ambito e applicabilità della LPD

**Articolo 3 — Ambito territoriale**: La LPD si applica alle circostanze che **producono effetti in Svizzera**, anche se avviate all'estero.

**Più ampio del test di stabilimento del RGPD**: Il RGPD richiede uno "stabilimento" (presenza fisica); la LPD richiede solo un "effetto in Svizzera" (targeting). Se il trattamento colpisce persone in Svizzera, si applica la LPD (anche senza uno stabilimento svizzero).

**Implicazione pratica**: L'ambito territoriale della LPD è potenzialmente più ampio del RGPD (test dell'effetto vs. test dello stabilimento/targeting).

---

## Definizioni chiave della LPD (Articolo 5)

**Dati personali** (Art. 5(a)): Qualsiasi informazione relativa a una **persona fisica identificata o identificabile**. Allineato con il RGPD: la LPD copre **solo le persone fisiche** (le persone giuridiche/aziende NON sono coperte dalla LPD).

**Dati personali degni di particolare protezione** (Art. 5(c)): Dati relativi a: opinioni o attività religiose, filosofiche, politiche o sindacali; salute, sfera privata o appartenenza a una razza o etnia; dati genetici; dati biometrici che identificano univocamente una persona fisica; dati relativi a procedimenti e sanzioni amministrativi e penali; dati relativi a misure di assistenza sociale.

**Profilazione** (Art. 5(f)): Qualsiasi forma di trattamento automatizzato di dati personali che utilizza dati per valutare determinati aspetti personali, in particolare per analizzare o prevedere aspetti concernenti le prestazioni lavorative, la situazione economica, la salute, le preferenze personali, gli interessi, l'affidabilità, il comportamento, l'ubicazione, i movimenti.

**Profilazione ad alto rischio** (Art. 5(g)): Profilazione che comporta un **elevato rischio per la personalità o i diritti fondamentali** dell'interessato mediante abbinamento di dati (attiva obblighi supplementari).

**Titolare** (Art. 5(j)): Persona privata o organo federale che, **da solo o insieme ad altri**, **determina le finalità e i mezzi** del trattamento.

**Responsabile** (Art. 5(k)): Persona privata o organo federale che **tratta dati personali per conto del titolare**.

---

## Principi di protezione dei dati della LPD (Articolo 6)

**1. Liceità** (Art. 6(1)): I dati personali devono essere **trattati lecitamente**.

**2. Buona fede** (Art. 6(2)): Il trattamento deve avvenire in **buona fede** ed essere **proporzionato**. "Buona fede": il trattamento deve essere leale, trasparente, non ingannevole. "Proporzionato": il trattamento deve essere proporzionato alle finalità (simile alla minimizzazione dei dati del RGPD).

**3. Limitazione della finalità** (Art. 6(3)): I dati personali possono essere raccolti solo per **una finalità specifica** riconoscibile dall'interessato; possono essere ulteriormente trattati solo in modo **compatibile con tale finalità**. Allineato con il RGPD.

**4. Minimizzazione dei dati / Limitazione della conservazione** (Art. 6(4)): I dati personali devono essere **distrutti o anonimizzati non appena non siano più necessari** per le finalità del trattamento. Combina i concetti del RGPD di minimizzazione e limitazione della conservazione.

**5. Esattezza** (Art. 6(5)): Chiunque tratti dati personali deve **assicurarsi che siano esatti**. Deve adottare tutte le **misure appropriate per correggere, cancellare o distruggere i dati inesatti o incompleti**. Simile al principio di esattezza del RGPD.

---

## Sicurezza dei dati della LPD (Articolo 8)

Il titolare e il responsabile devono garantire **un'adeguata sicurezza dei dati** mediante idonee misure tecniche e organizzative, progettate per prevenire: il trattamento non autorizzato; la perdita di dati; l'alterazione dei dati.

**Approccio basato sul rischio**: Le misure devono essere adeguate alla natura dei dati, alla portata del trattamento, ai rischi per gli interessati. Allineato con il RGPD Art. 32.

---

## Diritti degli interessati della LPD

**Diritto di accesso** (Art. 25): L'interessato ha il diritto di ottenere **conferma** che il titolare tratti i suoi dati personali e di ricevere **informazioni** su: dati disponibili; finalità del trattamento; periodo di conservazione; fonte dei dati; divulgazione/trasferimento; processo decisionale automatizzato. **Termine di risposta**: entro **30 giorni** (prorogabile se giustificato).

**Diritto di rettifica** (Art. 32): L'interessato può richiedere la **rettifica dei dati personali inesatti**.

**Diritto alla cancellazione** (Art. 32): L'interessato può richiedere la **cancellazione dei dati personali** se: i dati non sono più necessari; il trattamento è illecito; l'interessato revoca il consenso; esistono altri motivi legali per la cancellazione.

**Diritto alla portabilità dei dati** (Art. 28): L'interessato ha il diritto di **ricevere i dati personali forniti al titolare** in un **formato strutturato, di uso comune e leggibile da macchina** e di **trasmetterli a un altro titolare**. Solo per i dati forniti dall'interessato, trattati sulla base del consenso o del contratto, trattati con mezzi automatizzati. Identico al RGPD Art. 20.

**Diritto di opposizione** (Art. 30): L'interessato può opporsi al trattamento dei propri dati personali se causa la violazione dei suoi interessi giuridicamente protetti e il titolare non può dimostrare **motivi legittimi prevalenti**.

**Diritto di opposizione al marketing diretto** (Art. 31): L'interessato ha il diritto di opporsi al trattamento per scopi di **marketing diretto** (inclusa la profilazione per il marketing diretto). Il titolare deve cessare il trattamento per il marketing diretto dopo l'opposizione (senza eccezioni).

---

## Notifica delle violazioni dei dati della LPD (Articolo 24)

Il titolare deve informare l'IFPDT **il più presto possibile** se è probabile che la violazione comporti un **elevato rischio** per la personalità o i diritti fondamentali dell'interessato.

**Soglia "alto rischio"**: Più rigorosa del RGPD (RGPD: notifica per "rischio", comunicazione agli interessati per "alto rischio"; LPD: notifica all'IFPDT solo per "alto rischio").

**Nessun termine di 72 ore**: La LPD richiede la notifica "il più presto possibile" (nessun termine specifico di 72 ore come il RGPD).

**Nessun requisito esplicito di notifica agli interessati**: La LPD non richiede esplicitamente la notifica diretta agli interessati (a differenza del RGPD Art. 34).

---

## Trasferimenti internazionali di dati della LPD (Articoli 16-17)

**Articolo 16**: I dati personali possono essere comunicati all'estero solo se: il paese garantisce **un livello adeguato di protezione** (l'IFPDT pubblica l'elenco); **garanzie appropriate** garantiscono un'adeguata protezione; si applica una **deroga** (Art. 17).

**Paesi adeguati** (elenco IFPDT): Tutti gli Stati membri UE/SEE; Regno Unito; altri paesi determinati dal Consiglio federale svizzero.

**Differenza chiave dall'UE**: La Svizzera NON ha un equivalente del DPF con gli Stati Uniti. I trasferimenti verso gli USA richiedono le CSS o altre garanzie anche se il destinatario è certificato DPF.

**Garanzie appropriate** (Art. 16(2)): Clausole contrattuali approvate dall'IFPDT; norme vincolanti d'impresa approvate dall'IFPDT; clausole standard di protezione dei dati adottate dall'IFPDT; meccanismi di certificazione.

**Deroghe** (Art. 17): Consenso dopo informazione sui rischi; necessità contrattuale; interesse pubblico; pretese legali; interessi vitali; registro pubblico.

---

# Analisi comparativa RGPD vs. LPD

## Principali somiglianze

**Concetti fondamentali allineati**: Definizione di dati personali; distinzione titolare/responsabile; principi fondamentali di protezione dei dati (liceità, limitazione della finalità, minimizzazione dei dati, esattezza, limitazione della conservazione, sicurezza); diritti degli interessati (accesso, rettifica, cancellazione, portabilità, opposizione); restrizioni ai trasferimenti transfrontalieri; approccio basato sul rischio alla sicurezza.

**Perché sono simili**: Il legislatore svizzero ha intenzionalmente allineato la LPD al RGPD per mantenere la decisione di adeguatezza UE, facilitare i flussi di dati UE-Svizzera e adottare le migliori pratiche del RGPD.

---

## Principali differenze

| Aspetto | RGPD | LPD | Implicazione pratica |
|---------|------|-----|----------------------|
| **Ambito territoriale** | Stabilimento O targeting | Effetto in Svizzera (più ampio) | La LPD si applica potenzialmente più ampiamente |
| **Basi giuridiche** | 6 basi esplicite (Art. 6) | Basato su principi (liceità, buona fede, proporzionalità) | Il RGPD è più prescrittivo |
| **Definizione di consenso** | Requisiti dettagliati | Meno dettagliata | Standard del RGPD spesso applicato per la LPD |
| **Categorie speciali** | Elenco esplicito (Art. 9) | "Dati degni di particolare protezione" (Art. 5(c)) | Largamente allineati, ma la LPD include la "sfera privata" (concetto più ampio) |
| **Requisito RPD** | Obbligatorio per certi titolari (Art. 37) | Nessun RPD obbligatorio | Il RGPD è più prescrittivo |
| **RAT** | Obbligatorio (Art. 30) | Nessun requisito esplicito | Il RGPD è più prescrittivo; migliore prassi per la LPD |
| **DPIA** | Obbligatoria per trattamento ad alto rischio (Art. 35) | Nessun requisito esplicito | Il RGPD è più prescrittivo |
| **Soglia notifica violazioni** | Notifica per "rischio", comunicazione per "alto rischio" | Notifica solo per "alto rischio" | Soglia LPD più alta |
| **Termine notifica violazioni** | 72 ore all'autorità | "Il più presto possibile" (nessun termine) | Il RGPD è più prescrittivo |
| **Notifica agli interessati** | Comunicazione obbligatoria se "alto rischio" (Art. 34) | Nessun requisito esplicito | Il RGPD è più prescrittivo |
| **Sanzioni** | Fino a 20 milioni di euro o 4% del fatturato globale (sanzioni amministrative alle organizzazioni) | Fino a CHF 250.000 (sanzioni penali alle persone fisiche) | Diverso modello di applicazione |
| **Applicazione** | APD UE (decentrata), coordinamento EDPB | IFPDT (autorità svizzera centralizzata) | Il RGPD è più complesso |
| **Età del consenso (minori)** | 16 anni (gli Stati membri possono abbassare a 13) | 13 anni | Soglia LPD più bassa rispetto al RGPD predefinito |

---

## Strategia di doppia conformità

**Organizzazioni che trattano dati personali sia di interessati UE che svizzeri**:

**Approccio pragmatico — Allinearsi allo standard più rigoroso**: Poiché il RGPD è generalmente più prescrittivo e dettagliato della LPD, le organizzazioni spesso implementano lo **standard RGPD in modo uniforme** per raggiungere efficacemente la doppia conformità.

**Doppia conformità pratica**:

| Requisito | Approccio |
|-----------|-----------|
| **Basi giuridiche** | Usare il quadro dell'Art. 6 del RGPD (la LPD accetta queste come dimostrazione di liceità) |
| **Consenso** | Applicare lo standard di consenso del RGPD (soddisfa la LPD) |
| **Dati di categorie speciali** | Applicare le restrizioni dell'Art. 9 del RGPD (soddisfa i requisiti LPD per i dati sensibili) |
| **RPD** | Nominare il RPD se richiesto dal RGPD (o volontariamente per la LPD) |
| **RAT** | Mantenere il RAT dell'Art. 30 del RGPD (supera le aspettative implicite della LPD) |
| **DPIA** | Condurre DPIA per il RGPD Art. 35 (dimostra l'approccio basato sul rischio della LPD) |
| **Notifica violazioni** | Applicare il quadro del RGPD 72 ore/alto rischio (supera il requisito "solo alto rischio" della LPD) |
| **Diritti degli interessati** | Implementare tutti i diritti del RGPD (allineati con i diritti della LPD) |
| **Trasferimenti transfrontalieri** | Usare i meccanismi del RGPD (CSS, NBV) — l'IFPDT accetta le CSS UE con addendum svizzero |

**Raccomandazione**: Per le organizzazioni operanti in entrambe le giurisdizioni, implementare lo standard RGPD. I vantaggi di un unico quadro superano i risparmi marginali sui costi di un approccio solo-LPD.

---

## Errori comuni nella doppia conformità

**Errore 1: Supporre che le CSS UE funzionino in modo identico in Svizzera**. Realtà: l'IFPDT richiede un **addendum svizzero** alle CSS standard UE per i trasferimenti verso paesi non adeguati. Non è possibile utilizzare le CSS UE da sole per i dati svizzeri.

**Errore 2: Supporre che le liste di adeguatezza siano identiche**. Realtà: le liste di adeguatezza svizzera (IFPDT) e UE (Commissione europea) differiscono. Ad esempio, gli USA hanno l'EU-US Data Privacy Framework ma non un equivalente svizzero. I trasferimenti verso gli USA richiedono garanzie aggiuntive per i dati svizzeri anche se coperti dal DPF per i dati UE.

**Errore 3: Ignorare il concetto svizzero specifico di "sfera privata"**. Realtà: i "dati degni di particolare protezione" della LPD includono la "sfera privata" — più ampio rispetto alle categorie specifiche del RGPD.

**Errore 4: Supporre che la soglia di notifica delle violazioni "rischio" del RGPD si applichi alla Svizzera**. Realtà: la LPD richiede la notifica solo per violazioni a "alto rischio". Potrebbe essere necessario notificare all'APD UE (RGPD) ma non all'IFPDT (LPD) per la stessa violazione.

---

# Meccanismi internazionali di trasferimento dei dati — Analisi approfondita

## Perché esistono le restrizioni ai trasferimenti transfrontalieri

**Principio fondamentale**: La protezione dei dati personali non dovrebbe essere minata trasferendo i dati in giurisdizioni con protezione più debole.

**Considerazioni sui rischi**: Sorveglianza governativa nei paesi terzi (FISA 702, accesso alla sicurezza nazionale); mancanza di un'autorità di vigilanza indipendente; meccanismi di applicazione deboli; diverse tradizioni giuridiche; sfruttamento commerciale dei dati senza limiti.

---

## Decisioni di adeguatezza — Contesto dettagliato

**Concetto**: La Commissione europea (RGPD) o il Consiglio federale svizzero (LPD) determinano che un paese terzo garantisce un livello "adeguato" di protezione dei dati, rendendo i trasferimenti ammissibili senza garanzie aggiuntive.

**Criteri di valutazione** (RGPD Art. 45(2)): Stato di diritto, rispetto dei diritti fondamentali; esistenza e funzionamento di un'autorità di vigilanza indipendente; impegni internazionali; meccanismi di applicazione efficaci; diritti degli interessati e rimedi efficaci.

**Attuali decisioni di adeguatezza UE** (verificare l'elenco aggiornato): Adeguatezza completa: Andorra, Argentina, Canada (solo PIPEDA), Isole Faroe, Guernsey, Israele, Isola di Man, Giappone, Jersey, Nuova Zelanda, Repubblica di Corea, Svizzera, Regno Unito, Uruguay. Adeguatezza parziale: **EU-US Data Privacy Framework** (DPF) — limitato alle organizzazioni statunitensi che si auto-certificano al DPF.

---

**EU-US Data Privacy Framework (DPF)**: Efficace dal 10 luglio 2023. Sostituisce lo Privacy Shield (invalidato nel 2020). Il Dipartimento del Commercio degli USA mantiene un elenco di organizzazioni certificate. Le organizzazioni statunitensi si auto-certificano. Salvaguardie vincolanti che limitano l'accesso del governo statunitense ai dati UE (Ordine esecutivo 14086). La "Data Protection Review Court" (DPRC) gestisce i reclami individuali UE sulla sorveglianza statunitense. Sfide legali in corso.

**Elenco di adeguatezza svizzero** (IFPDT): La Svizzera riconosce l'adeguatezza per tutti gli Stati UE/SEE; Regno Unito; altri paesi determinati dal Consiglio federale svizzero. Differenza chiave: la Svizzera NON ha un equivalente DPF con gli USA.

---

## Clausole contrattuali standard (CSS) — Guida pratica

**CSS standard UE** (Decisione della Commissione europea 2021/914): Adottate il 4 giugno 2021. Sostituiscono le vecchie CSS del 2001/2004.

**Quattro moduli**: Modulo 1: Da titolare a titolare; Modulo 2: Da titolare a responsabile; Modulo 3: Da responsabile a sub-responsabile; Modulo 4: Da responsabile a titolare.

**Caratteristiche principali**: Struttura modulare; allegati flessibili; clausola di adesione; conformità al diritto locale; diritti degli interessati come beneficiari terzi; diritti di audit.

**Non possono essere modificate**: Le CSS sono "standard" — gli obblighi principali non possono essere alterati. Gli allegati possono essere personalizzati.

**CSS svizzere**: L'IFPDT fornisce CSS specifiche per la Svizzera OPPURE accetta le CSS UE con **addendum svizzero** (adattamento per la Svizzera, IFPDT come autorità di vigilanza competente, legge svizzera come legge applicabile).

---

**Valutazione d'impatto del trasferimento (TIA) — Requisito Schrems II**:

**Schrems II** (CGUE Causa C-311/18, luglio 2020) ha invalidato lo Privacy Shield e stabilito il requisito di una **valutazione caso per caso** della legge del paese terzo quando ci si avvale delle CSS.

**Requisito TIA**: Anche con le CSS in vigore, l'esportatore di dati deve valutare se: la legislazione locale nel paese terzo consente all'importatore di rispettare le CSS; l'accesso governativo ai dati nel paese terzo mina le protezioni; sono necessarie **misure supplementari** (tecniche/organizzative) oltre alle CSS.

**Fasi della TIA** (per Raccomandazioni EDPB 01/2020):
1. Conoscere i trasferimenti (mappatura)
2. Verificare lo strumento di trasferimento
3. Valutare il paese terzo (leggi sull'accesso ai dati, sorveglianza)
4. Identificare le misure supplementari
5. Passaggi procedurali (documentare, informare gli interessati se impossibile trasferire)
6. Rivalutare periodicamente

**Misure supplementari** (per EDPB): Tecniche: cifratura end-to-end (l'importatore non ha la chiave di decifratura); pseudonimizzazione; minimizzazione dei dati; controlli di accesso. Organizzative: trasparenza (informare gli interessati); impegni legali (l'importatore si impegna a contestare le richieste governative, a notificare l'esportatore).

---

## Altri meccanismi di trasferimento

**Norme vincolanti d'impresa (NBV)** (RGPD Art. 47, LPD Art. 16(2)(e)): Politiche interne di protezione dei dati approvate per i gruppi multinazionali, che consentono i trasferimenti intra-gruppo. Vantaggi: singola approvazione per tutti i trasferimenti intra-gruppo; standard globali uniformi. Svantaggi: richiede l'approvazione dell'APD (processo lungo, tipicamente 12-24 mesi); complesso da redigere; solo per i trasferimenti intra-gruppo.

**Codici di condotta** (RGPD Art. 40, 46(2)(e)): Codici specifici del settore approvati dall'APD. Meccanismo disponibile ma pochi codici approvati finora.

**Meccanismi di certificazione** (RGPD Art. 42, 46(2)(f)): Certificazione di protezione dei dati combinata con impegni vincolanti dell'importatore. Meccanismo disponibile ma poche certificazioni disponibili.

---

## Deroghe (eccezioni di ultima istanza)

**RGPD Articolo 49 / LPD Articolo 17 — Deroghe per situazioni specifiche**: I trasferimenti sono consentiti **senza adeguatezza o garanzie** in circostanze eccezionali specifiche.

**Limitazione critica**: Le deroghe sono **ultima risorsa**. Non possono essere utilizzate per: trasferimenti di routine; trasferimenti ripetitivi; trasferimenti strutturali (relazioni continuative); trasferimenti che potrebbero essere coperti da CSS o altri meccanismi.

**Deroga del consenso esplicito** (RGPD Art. 49(1)(a), LPD Art. 17(1)(a)): Il trasferimento è consentito se l'interessato ha **esplicitamente acconsentito** dopo essere stato **informato dei possibili rischi** dovuti all'assenza di adeguatezza/garanzie. Il consenso deve essere esplicito; l'interessato deve essere informato dei rischi specifici nel paese terzo.

**Deroga per necessità contrattuale** (RGPD Art. 49(1)(b), LPD Art. 17(1)(b)): Il trasferimento è consentito se **necessario per l'esecuzione di un contratto** tra l'interessato e il titolare, o per misure precontrattuali su richiesta dell'interessato.

**Deroga per pretese legali** (RGPD Art. 49(1)(e), LPD Art. 17(1)(d)): Il trasferimento è consentito se necessario per **l'accertamento, l'esercizio o la difesa di pretese in giudizio**.

**Deroga per interessi vitali** (RGPD Art. 49(1)(f), LPD Art. 17(1)(e)): Solo vita o morte: emergenza medica, risposta a disastri, ricerca e salvataggio.

---

# Framework e standard sulla privacy — Panoramica

## ISO/IEC 27701:2019 — Sistema di gestione delle informazioni sulla privacy

**Standard**: ISO/IEC 27701:2019 — Estensione a ISO/IEC 27001 e ISO/IEC 27002 per la gestione delle informazioni sulla privacy.

**Scopo**: Estendere il SGSI ISO/IEC 27001 con requisiti e controlli specifici per la privacy.

**Struttura**: Estensione a ISO/IEC 27001 (requisiti aggiuntivi per SGPI); Estensione a ISO/IEC 27002 (controlli privacy aggiuntivi per i titolari e responsabili del trattamento).

**Mappatura al RGPD**: L'Allegato D fornisce la mappatura al RGPD (controlli che supportano la conformità al RGPD).

**Quando considerarlo**: Organizzazioni in cerca di un approccio strutturato alla privacy, operazioni internazionali, requisiti di certificazione della privacy per clienti/partner.

---

## NIST Privacy Framework

**Framework**: NIST Privacy Framework: uno strumento per migliorare la privacy attraverso la gestione del rischio aziendale (2020). Sviluppato dal National Institute of Standards and Technology (NIST) degli USA.

**Funzioni principali**: Identify-P (comprendere il rischio per la privacy); Govern-P (sviluppare la struttura di governance della privacy); Control-P (sviluppare e implementare i controlli sulla privacy); Communicate-P (comunicare con le parti interessate); Protect-P (sviluppare e implementare le salvaguardie per la protezione dei dati).

**Applicabilità**: Riferimento utile per le organizzazioni che sviluppano programmi sulla privacy, in particolare le entità statunitensi o regolamentate negli USA.

---

## Principi OCSE sulla privacy

**Linee guida**: OCSE — Linee guida sulla protezione della privacy e i flussi transfrontalieri di dati personali (1980, rivedute 2013).

**Rilevanza storica**: Fondamento di molte leggi nazionali sulla privacy (inclusi RGPD, LPD).

**Otto principi**: Limitazione della raccolta; qualità dei dati; specificazione della finalità; limitazione dell'uso; garanzie di sicurezza; apertura; partecipazione individuale; responsabilità.

---

# Panorama di applicazione — Contesto da casi notevoli

## Lezioni chiave dalle principali azioni di applicazione

**Amazon (APD Lussemburgo, 2021) — 746 milioni di euro**: Violazione dei principi di protezione dei dati, pubblicità comportamentale senza base giuridica adeguata. **Lezione**: Il consenso per la pubblicità comportamentale deve soddisfare lo standard RGPD.

**Meta/Facebook (DPC Irlanda, 2023) — 1,2 miliardi di euro**: Trasferimenti illeciti di dati verso gli USA dopo Schrems II (basati su CSS senza adeguata TIA). **Lezione**: Le valutazioni d'impatto del trasferimento (TIA) sono obbligatorie quando ci si avvale delle CSS; i rischi della sorveglianza governativa devono essere affrontati.

**Google (CNIL Francia, 2019) — 50 milioni di euro**: Mancanza di trasparenza, consenso inadeguato per gli annunci personalizzati. **Lezione**: Il consenso deve essere liberamente prestato, specifico, granulare; non può essere raggruppato; gli obblighi di trasparenza sono rigorosi.

**H&M (APD Amburgo, 2020) — 35,3 milioni di euro**: Sorveglianza eccessiva dei dipendenti, registrazione di conversazioni personali, profilazione comportamentale dettagliata. **Lezione**: Il contesto lavorativo richiede maggiore sensibilità; la minimizzazione dei dati è fondamentale; i dipendenti hanno ragionevoli aspettative di privacy.

**British Airways (ICO UK, 2020) — 20 milioni di sterline**: Violazione dei dati di 400.000 clienti, sicurezza inadeguata (attacco di skimming del sito web). **Lezione**: Le misure di sicurezza devono essere adeguate al rischio (Art. 32); i titolari sono responsabili per le violazioni della sicurezza; la cooperazione con l'APD può ridurre le sanzioni.

---

## Pattern di violazione comuni

**Pattern 1: Consenso inadeguato**: Caselle pre-spuntate; consenso raggruppato; consenso nascosto nelle condizioni generali; processo di revoca difficile.

**Pattern 2: Raccolta eccessiva di dati**: Raccolta di dati "per ogni evenienza"; mancata valutazione della necessità; funzione creep (utilizzo dei dati per finalità aggiuntive senza base giuridica).

**Pattern 3: Trasferimenti transfrontalieri illeciti**: Basarsi sullo Privacy Shield invalidato dopo Schrems II; utilizzo di CSS senza valutazione d'impatto del trasferimento; trasferimento verso gli USA senza garanzie adeguate.

**Pattern 4: Notifica ritardata delle violazioni**: Attendere troppo per valutare la violazione; sottovalutare il rischio per gli interessati; mancato rispetto del termine di 72 ore.

**Pattern 5: Risposta inadeguata ai diritti degli interessati**: Ritardo nelle risposte oltre 1 mese; rifiuto delle richieste senza giustificazione valida; verifica inadeguata dell'identità; risposte incomplete.

---

# Conclusione

Questo documento di contesto fornisce informazioni supplementari sul panorama normativo della privacy per supportare l'implementazione del programma di privacy di [Organizzazione].

**Ricordare**: Questo è un **documento di supporto**, NON parte dell'ambito di certificazione del SGSI. Tutti i requisiti di conformità sono definiti in **ISMS-POL-A.5.34**. Consultare **un consulente legale qualificato** per la consulenza legale. Fare sempre riferimento alle **fonti normative ufficiali** per le decisioni di conformità.

**Prossimi passi consigliati**:
1. Rivedere ISMS-POL-A.5.34 (requisiti della politica principale)
2. Valutare l'applicabilità normativa per ISMS-POL-00
3. Implementare i controlli sulla privacy per ISMS-IMP-A.5.34
4. Condurre valutazioni della privacy utilizzando i libri di lavoro ISMS-IMP-A.5.34
5. Coinvolgere un consulente legale per la guida specifica per la giurisdizione

---

**FINE DI ISMS-CTX-A.5.34**

*«Il contesto informa, ma la politica governa. Comprendere il panorama per implementare efficacemente.»*

<!-- QA_VERIFIED: 2026-04-04 -->
